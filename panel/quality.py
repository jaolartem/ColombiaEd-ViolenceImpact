"""
Data quality, source by source, as the validation step of the ETL.

    python -m panel.quality

Each source is checked against its own rules: what its values can be, how its parts must add up, what its
series can do from one year to the next. Every finding is one row of RelationsAndConclusions.DataQualityFlags:

- error:        a value the measure does not allow (a share above 1). Not used.
- missing:      no value where one could be expected, for a known reason (the municipality did not exist).
- inconsistent: the source contradicts itself (two counts of the same thing that do not match).
- break:        the series jumps from one year to the next by more than the thing it measures can.
- small_base:   atypical only because few people stand behind it. The smoothed value is the one to use.
- extreme:      atypical after taking its base into account. A real case: kept as it is, and annotated.

Nothing is overwritten. Where a value rests on a base that can be weighed (person-years behind a rate,
students behind a mean or a share), empirical Bayes pulls it toward the municipalities of its own kind,
more the fewer people stand behind it, and the result goes to RelationsAndConclusions.SmoothedValues:
Marshall's (1991) local estimator for rates, normal-normal shrinkage for means and shares.

Municipalities are compared with their peers, never with the whole country: the peer group is DNP's
rurality category (cities and agglomerations, intermediate, rural, dispersed rural; TerriData indicator
010010007). The 21 territories DNP does not classify (the Amazon's non-municipalized areas, San Andres,
Nuevo Belen de Bajira) are compared within their department.

Atypical is judged in one of two ways, depending on the source:
- dense measures, where most municipalities have cases every period (homicide, intra-family violence,
  scores): a robust z above 3.5 (median and median absolute deviation) within the period and the
  rurality category, on the log
  scale for rates and the logit scale for shares;
- sparse measures, where most municipalities have no case in a period (massacres, kidnapping, landmines):
  the Poisson probability of seeing that many events if the municipality had the rate of its rurality
  category. Below 1 in 1,000 is an extreme; a rate ten times the category's that is not that improbable is
  a small base.

Writes the two tables and docs/data_quality.md.
"""
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import poisson

from panel.load_db import connect, load

ROOT = Path(__file__).resolve().parent.parent
THRESHOLD = 3.5
P_EXTREME = 0.001
FLAG_COLUMNS = ["source", "source_table", "column_name", "municipality_id", "period", "kind", "value", "smoothed_value",
                "median", "robust_z", "note"]
SMOOTH_COLUMNS = ["source_table", "column_name", "municipality_id", "period", "raw_value", "smoothed_value", "weight",
                  "reference"]


# --------------------------------------------------------------------------------------------- tools

def query(cur, sql):
    cur.execute(sql)
    return pd.DataFrame(cur.fetchall(), columns=[d[0] for d in cur.description])


def robust_z(x: pd.Series) -> pd.Series:
    med = x.median()
    mad = (x - med).abs().median()
    if mad > 0:
        return 0.6745 * (x - med) / mad
    mean_ad = (x - med).abs().mean()            # more than half the values equal: the mean deviation instead
    if mean_ad > 0:
        return (x - med) / (1.253314 * mean_ad)
    return pd.Series(0.0, index=x.index)


def logit(p: pd.Series) -> pd.Series:
    p = p.clip(0.005, 0.995)
    return np.log(p / (1 - p))


def zscore(values: pd.Series, period: pd.Series, scale=None) -> pd.Series:
    v = scale(values) if scale else values
    return v.groupby(period).transform(robust_z)


def eb_rates(df, keys):
    """Marshall's local empirical Bayes rate, per keys and peer group. Returns rate, weight, reference."""
    by = [df[k] for k in keys + ["peer"]]
    r = df["cases"] / df["person_years"]
    m = df["cases"].groupby(by).transform("sum") / df["person_years"].groupby(by).transform("sum")
    nbar = df["person_years"].groupby(by).transform("mean")
    s2 = (df["person_years"] * (r - m) ** 2).groupby(by).transform("sum") / df["person_years"].groupby(by).transform("sum")
    a = (s2 - m / nbar).clip(lower=0)
    w = (a / (a + m / df["person_years"])).where(m > 0, 1.0)
    return m + w * (r - m), w, m


def eb_means(df, value, keys, unit_var):
    """Normal-normal shrinkage toward the peer group; unit_var / students is the sampling variance."""
    d = df.dropna(subset=[value])
    by = [d[k] for k in keys + ["peer"]]
    n = d["students"].astype(float)
    mu = (d[value] * n).groupby(by).transform("sum") / n.groupby(by).transform("sum")
    v = (unit_var(mu) if callable(unit_var) else unit_var) / n
    spread = d[value].groupby(by).transform(lambda s: s.var(ddof=0))
    tau2 = (spread - v.groupby(by).transform("mean")).clip(lower=0)
    b = (tau2 / (tau2 + v)).fillna(0)
    return (mu + b * (d[value] - mu)).reindex(df.index), b.reindex(df.index), mu.reindex(df.index)


class Findings:
    """The rows a source produces for the two tables."""

    def __init__(self, source):
        self.source, self.flags, self.smoothed = source, [], []

    def add(self, frame, mask, table, column, period, kind, value=None, smoothed=None, median=None, z=None, note=None):
        mask = mask.fillna(False) if hasattr(mask, "fillna") else mask
        idx = frame.index[np.asarray(mask, dtype=bool)]
        if not len(idx):
            return
        pick = lambda x: (x.loc[idx].values if isinstance(x, pd.Series) else x)
        self.flags.append(pd.DataFrame({
            "source": self.source, "source_table": table, "column_name": column,
            "municipality_id": frame.loc[idx, "municipality_id"].values, "period": pick(period), "kind": kind,
            "value": pick(value) if value is not None else np.nan,
            "smoothed_value": pick(smoothed) if smoothed is not None else np.nan,
            "median": pick(median) if median is not None else np.nan,
            "robust_z": pick(z) if z is not None else np.nan, "note": pick(note) if note is not None else None}))

    def smooth(self, frame, table, column, period, raw, smoothed, weight, reference):
        ok = smoothed.notna()
        self.smoothed.append(pd.DataFrame({
            "source_table": table, "column_name": column, "municipality_id": frame.loc[ok, "municipality_id"].values,
            "period": period[ok].values, "raw_value": raw[ok].values, "smoothed_value": smoothed[ok].values,
            "weight": weight[ok].values, "reference": reference[ok].values}))

    def dense(self, frame, table, column, period, raw, smoothed, scale):
        """Extreme if still atypical after smoothing; small base if atypical only before."""
        ok = raw.notna()
        key = compared(frame, period)[ok]
        z_raw = zscore(raw[ok], key, scale)
        z_s = zscore(smoothed[ok], key, scale)
        med = raw[ok].groupby(key).transform("median")
        f = frame[ok]
        extreme = z_s.abs() > THRESHOLD
        self.add(f, extreme, table, column, period[ok], "extreme", raw[ok], smoothed[ok], med, z_s)
        self.add(f, (z_raw.abs() > THRESHOLD) & ~extreme, table, column, period[ok], "small_base", raw[ok], smoothed[ok],
                 med, z_raw)

    def plain(self, frame, table, column, period, values, scale=None):
        """Extremes where there is no base to weigh. Skipped when most values sit at zero."""
        ok = values.notna()
        if (values[ok] == 0).mean() > 0.5:
            return
        key = compared(frame, period)[ok]
        z = zscore(values[ok], key, scale)
        med = values[ok].groupby(key).transform("median")
        self.add(frame[ok], z.abs() > THRESHOLD, table, column, period[ok], "extreme", values[ok], median=med, z=z)


def compared(frame, period):
    """What a value is compared with: the same period and the same peer group."""
    return period.astype(str) + "|" + frame["peer"]


def rates(fd: Findings, df, table, column, dense: bool):
    """A rate per municipality and period: df has municipality_id, peer, period, cases, person_years."""
    df = df.copy()
    nobase = ~(df["person_years"] > 0)
    fd.add(df, nobase, table, column, df["period"], "missing", note="no population behind the rate")
    df = df[~nobase]
    s, w, m = eb_rates(df, ["period"])
    raw = df["cases"] / df["person_years"] * 1e5
    smoothed = s * 1e5
    fd.smooth(df, table, column, df["period"], raw, smoothed, w, m * 1e5)
    if dense:
        fd.dense(df, table, column, df["period"], raw, smoothed, lambda x: np.log1p(x))
        return
    by = [df["period"], df["peer"]]
    national = df["cases"].groupby(by).transform("sum") / df["person_years"].groupby(by).transform("sum")
    expected = national * df["person_years"]
    p = pd.Series(poisson.sf(df["cases"] - 1, expected.clip(lower=1e-12)), index=df.index)
    extreme = (p < P_EXTREME) & (df["cases"] > 0)
    note = df["cases"].astype(int).astype(str) + " observed, " + expected.round(2).astype(str) + " expected at the rate of its rurality category"
    fd.add(df, extreme, table, column, df["period"], "extreme", raw, smoothed, national * 1e5, None, note)
    fd.add(df, ~extreme & (df["cases"] > 0) & (raw > 10 * national * 1e5), table, column, df["period"], "small_base",
           raw, smoothed, national * 1e5, None, note)


# --------------------------------------------------------------------------------------------- sources

def dane_population(cur, dept):
    fd = Findings("DANE")
    p = query(cur, "SELECT municipality_id, year, population FROM RelationsAndConclusions.Population")
    p["population"] = p["population"].astype(float)
    p = p.sort_values(["municipality_id", "year"]).reset_index(drop=True)
    first = p[p["population"] > 0].groupby("municipality_id")["year"].min()
    zero = p["population"] <= 0
    before = p["year"] < p["municipality_id"].map(first)
    fd.add(p, zero & before, "Population", "population", p["year"].astype(str), "missing", p["population"],
           note="before the municipality was created")
    fd.add(p, zero & ~before, "Population", "population", p["year"].astype(str), "missing", p["population"],
           note="DANE gives 0: the territory was absorbed or is not projected")
    prev = p.groupby("municipality_id")["population"].shift()
    change = p["population"] / prev - 1
    fd.add(p, (prev > 0) & (p["population"] > 0) & (change.abs() > 0.2), "Population", "population",
           p["year"].astype(str), "break", p["population"],
           note=change.map(lambda c: f"{c:+.0%} from the year before: territory gained or lost"))
    s = query(cur, "SELECT municipality_id, year, SUM(population) s FROM RelationsAndConclusions.PopulationBySexAge "
                   "WHERE sex_id IN ('F', 'M') GROUP BY 1, 2").merge(p, on=["municipality_id", "year"])
    diff = s["s"].astype(float) / s["population"] - 1
    fd.add(s, (s["population"] > 0) & (diff.abs() > 0.01), "PopulationBySexAge", "population", s["year"].astype(str),
           "inconsistent", s["s"].astype(float), note=diff.map(lambda d: f"sex and age add up to {d:+.1%} of the total"))
    return fd


def dane_census(cur, dept):
    fd = Findings("DANE")
    c = query(cur, "SELECT * FROM Structural_Violence.Census2018Municipal").merge(dept, on="municipality_id")
    cols = [x for x in c.columns if x not in ("municipality_id", "peer")]
    c[cols] = c[cols].astype(float)
    t, period = "Census2018Municipal", pd.Series("2018", index=c.index)
    for col in cols:
        if col == "dwellings_occupied":
            fd.add(c, c[col] < 1, t, col, period, "error", c[col], note="no occupied dwellings")
            fd.plain(c, t, col, period, c[col], np.log1p)
            continue
        top = 1 if col.startswith("share_") else 100
        fd.add(c, (c[col] < 0) | (c[col] > top), t, col, period, "error", c[col], note=f"outside [0, {top}]")
        fd.plain(c, t, col, period, c[col], lambda x, top=top: logit(x / top))
    strata = c[[f"share_stratum_{i}" for i in range(1, 7)]].sum(axis=1)
    fd.add(c, strata > 1.01, t, "share_stratum", period, "inconsistent", strata, note="the six strata add up to more than 1")
    fd.add(c, strata < 0.8, t, "share_stratum", period, "missing", 1 - strata,
           note=(1 - strata).map(lambda x: f"{x:.0%} of occupied dwellings have no stratum"))
    pair = c["share_stratum_1_2"] - c["share_stratum_1"] - c["share_stratum_2"]
    fd.add(c, pair.abs() > 0.01, t, "share_stratum_1_2", period, "inconsistent", c["share_stratum_1_2"],
           note="differs from strata 1 and 2 added")
    parts = ["nbi_misery", "nbi_housing", "nbi_services", "nbi_overcrowding", "nbi_school_non_attendance", "nbi_economic_dependency"]
    fd.add(c, c["nbi"] + 0.1 < c[parts].max(axis=1), t, "nbi", period, "inconsistent", c["nbi"],
           note="below one of its components")
    fd.add(c, c["nbi_misery"] > c["nbi"] + 0.1, t, "nbi_misery", period, "inconsistent", c["nbi_misery"], note="above NBI")
    both = c["share_electricity"] + c["share_no_electricity_service"]
    fd.add(c, both > 1.05, t, "share_electricity", period, "inconsistent", c["share_electricity"],
           note=both.map(lambda x: f"with the dwellings without the service it adds up to {x:.2f}"))
    ratio = np.log(c["ipm"]) - np.log(c["nbi"])
    z = robust_z(ratio)
    main = c[parts[1:]].idxmax(axis=1).str.replace("nbi_", "")
    fd.add(c, z.abs() > THRESHOLD, t, "ipm_vs_nbi", period, "extreme", c["ipm"], z=z,
           note="IPM " + c["ipm"].round(1).astype(str) + " against NBI " + c["nbi"].round(1).astype(str)
                + "; NBI's largest component: " + main)
    pop = query(cur, "SELECT municipality_id, population FROM RelationsAndConclusions.Population WHERE year = 2018")
    m = c.merge(pop, on="municipality_id")
    ppd = m["population"].astype(float) / m["dwellings_occupied"]
    fd.add(m, (ppd > 6) | (ppd < 2), t, "dwellings_occupied", pd.Series("2018", index=m.index), "inconsistent",
           m["dwellings_occupied"],
           note=ppd.map(lambda x: f"{x:.1f} persons per occupied dwelling against DANE's 2018 population: census coverage"))
    return fd


def period_rates(cur, dept, source, prefix, sparse_measures):
    fd = Findings(source)
    pr = query(cur, f"SELECT municipality_id, period_kind, period_code, measure, cases, person_years "
                    f"FROM RelationsAndConclusions.PeriodRates WHERE measure LIKE '{prefix}%'").merge(dept, on="municipality_id")
    pr[["cases", "person_years"]] = pr[["cases", "person_years"]].astype(float)
    pr["period"] = pr["period_kind"] + ":" + pr["period_code"]
    for measure, g in pr.groupby("measure"):
        rates(fd, g, "PeriodRates", measure, dense=measure not in sparse_measures)
    return fd


def police(cur, dept):
    sparse = {"police_massacre_events", "police_massacre_victims"}
    fd = period_rates(cur, dept, "POLICE", "police_", sparse)
    # a count that multiplies from one year to the next follows the reporting, not the events
    y = query(cur, "SELECT municipality_id, YEAR(day) year, indicator_id, SUM(cases) cases "
                   "FROM RelationsAndConclusions.PoliceDailyCases WHERE YEAR(day) < 2026 GROUP BY 1, 2, 3")
    names = {1: "police_homicide", 4: "police_domestic_violence", 6: "police_sexual_violence"}
    y["cases"] = y["cases"].astype(float)
    full = (y.set_index(["municipality_id", "indicator_id", "year"])["cases"]
            .unstack("year", fill_value=0).stack().rename("cases").reset_index())
    full = full.sort_values(["municipality_id", "indicator_id", "year"]).reset_index(drop=True)
    before = full.groupby(["municipality_id", "indicator_id"])["cases"].transform(lambda s: s.shift().rolling(3, min_periods=3).mean())
    jump = (full["cases"] >= 20) & (full["cases"] >= 5 * before.clip(lower=1))
    for ind, name in names.items():
        sub = full["indicator_id"] == ind
        fd.add(full[sub], jump[sub], "PoliceDailyCases", name, full.loc[sub, "year"].astype(str), "break",
               full.loc[sub, "cases"], note=before[sub].map(lambda b: f"against {b:.1f} a year in the three years before"))
    return fd


def cnmh(cur, dept):
    pr = query(cur, "SELECT DISTINCT measure FROM RelationsAndConclusions.PeriodRates WHERE measure LIKE 'cnmh_%'")
    return period_rates(cur, dept, "CNMH", "cnmh_", set(pr["measure"]))


def indepaz(cur, dept):
    return period_rates(cur, dept, "INDEPAZ", "indepaz_", {"indepaz_massacre_events", "indepaz_massacre_victims"})


def medicina_legal(cur, dept):
    fd = Findings("MEDICINA_LEGAL")
    v = query(cur, "SELECT municipality_id, year, indicator, cases, population FROM RelationsAndConclusions.ViolenceRates")
    v = v.merge(dept, on="municipality_id")
    v["cases"], v["person_years"] = v["cases"].astype(float), v["population"].astype(float)
    v["period"] = v["year"].astype(str)
    for ind, g in v.groupby("indicator"):
        rates(fd, g, "ViolenceCases", ind, dense=ind != "sociopolitical_homicide")
    return fd


def saber11(cur, dept):
    fd = Findings("ICFES")
    ms = query(cur, "SELECT municipality_id, exam_period_id, students, math_z, global_z "
                    "FROM Education_Outcomes.MunicipalScoresMicro").merge(dept, on="municipality_id")
    ms[["students", "math_z", "global_z"]] = ms[["students", "math_z", "global_z"]].astype(float)
    ms["period"] = ms["exam_period_id"].astype(str)
    for col in ("math_z", "global_z"):          # z-scores are in student standard deviations: variance 1 / students
        s, b, mu = eb_means(ms, col, ["period"], 1.0)
        fd.smooth(ms, "MunicipalScoresMicro", col, ms["period"], ms[col], s, b, mu)
        fd.dense(ms, "MunicipalScoresMicro", col, ms["period"], ms[col], s, None)
    # exam takers that double or halve from one year to the next, same calendar
    ms["year"], ms["calendar"] = ms["exam_period_id"] // 10, np.where(ms["exam_period_id"] % 10 == 1, "B", "A")
    ms = ms.sort_values(["municipality_id", "calendar", "year"])
    prev = ms.groupby(["municipality_id", "calendar"])["students"].shift()
    prev_year = ms.groupby(["municipality_id", "calendar"])["year"].shift()
    ratio = ms["students"] / prev
    fd.add(ms, (prev_year == ms["year"] - 1) & (np.maximum(ms["students"], prev) >= 30) & ((ratio > 2) | (ratio < 0.5)),
           "MunicipalScoresMicro", "students", ms["period"], "break", ms["students"],
           note=prev.map(lambda x: f"{x:.0f} exam takers the year before" if pd.notna(x) else None))
    return fd


def student_context(cur, dept):
    fd = Findings("ICFES")
    ctx = query(cur, "SELECT * FROM Student_Context.MunicipalStudentContext").merge(dept, on="municipality_id")
    ctx["period"] = ctx["exam_period_id"].astype(str)
    shares = [c for c in ctx.columns if c.startswith("share_")]
    ctx[shares + ["students"]] = ctx[shares + ["students"]].astype(float)
    t = "MunicipalStudentContext"
    for col in shares:
        fd.add(ctx, (ctx[col] < 0) | (ctx[col] > 1), t, col, ctx["period"], "error", ctx[col], note="outside [0, 1]")
        s, b, mu = eb_means(ctx, col, ["period"], lambda p: (p * (1 - p)).clip(lower=1e-6))
        fd.smooth(ctx, t, col, ctx["period"], ctx[col], s, b, mu)
        fd.dense(ctx, t, col, ctx["period"], ctx[col], s, logit)
    both = ctx["share_mother_higher_ed"] + ctx["share_mother_primary_or_less"]
    fd.add(ctx, both > 1.001, t, "share_mother_higher_ed", ctx["period"], "inconsistent", both,
           note="higher and primary-or-less education of the mother add up to more than 1")
    return fd


def men(cur, dept):
    fd = Findings("MEN")
    en = query(cur, "SELECT * FROM Education_Outcomes.EnrolmentAndDropout").merge(dept, on="municipality_id")
    cols = [c for c in en.columns if c not in ("municipality_id", "year", "peer")]
    en[cols] = en[cols].astype(float)
    en = en.sort_values(["municipality_id", "year"]).reset_index(drop=True)
    period, t = en["year"].astype(str), "EnrolmentAndDropout"
    for col in cols:
        fd.add(en, en[col] < 0, t, col, period, "error", en[col], note="negative")
        if col.startswith("net_enrolment"):
            # MEN divides the enrolment by DANE's projected population of that age: students who come from other
            # municipalities, or a projection below the real population, take it above 100
            fd.add(en, en[col] > 100, t, col, period, "inconsistent", en[col],
                   note="above 100: enrolment from other municipalities or a projected population below the real one")
        else:
            fd.add(en, en[col] > 100, t, col, period, "error", en[col], note="above 100")
        ok = (en[col] >= 0) & (en[col] <= 100)
        fd.plain(en[ok], t, col, period[ok], en.loc[ok, col], lambda x: logit(x / 100))
        prev = en.groupby("municipality_id")[col].shift()
        prev_year = en.groupby("municipality_id")["year"].shift()
        fd.add(en, (prev_year == en["year"] - 1) & ((en[col] - prev).abs() > 30), t, col, period, "break", en[col],
               note=prev.map(lambda x: f"{x:.1f} the year before" if pd.notna(x) else None))
    return fd


def saber_pro(cur, dept):
    fd = Findings("ICFES")
    sp = query(cur, "SELECT * FROM Education_Outcomes.SaberProByMunicipality").merge(dept, on="municipality_id")
    sp["period"] = sp["periodo"].astype(str) + ":" + sp["sex_id"]
    t = "SaberProByMunicipality"
    for col in ("quantitative_reasoning", "critical_reading", "citizenship", "english", "written_communication"):
        sp[col] = sp[col].astype(float)
        fd.add(sp, (sp[col] < 0) | (sp[col] > 300), t, col, sp["period"], "error", sp[col], note="outside [0, 300]")
        # Saber Pro modules are scaled to a standard deviation of about 30 points
        s, b, mu = eb_means(sp, col, ["period"], 900.0)
        fd.smooth(sp, t, col, sp["period"], sp[col], s, b, mu)
        fd.dense(sp, t, col, sp["period"], sp[col], s, None)
    return fd


SOURCES = [dane_population, dane_census, police, cnmh, indepaz, medicina_legal, saber11, student_context, men, saber_pro]


# --------------------------------------------------------------------------------------------- run

def peers(cur):
    """Each municipality's peer group: DNP's rurality category, or its department when DNP gives none."""
    m = query(cur, """
        SELECT m.id municipality_id, m.department_id,
               (SELECT mi.value_text FROM Territorial_Context.MunicipalIndicators mi
                WHERE mi.municipality_id = m.id AND mi.indicator_code = '010010007' AND mi.value_text IS NOT NULL
                ORDER BY mi.year DESC LIMIT 1) rurality
        FROM RelationsAndConclusions.Municipalities m""")
    m["peer"] = m["rurality"].fillna("department " + m["department_id"].astype(str))
    return m[["municipality_id", "peer"]]


def main():
    db = connect()
    cur = db.cursor()
    dept = peers(cur)
    flags, smooth = [], []
    for check in SOURCES:
        fd = check(cur, dept)
        flags += fd.flags
        smooth += fd.smoothed
        n = sum(len(f) for f in fd.flags)
        print(f"  {check.__name__:<18} {n:>8,} findings  {sum(len(s) for s in fd.smoothed):>9,} values smoothed", flush=True)
    flags = pd.concat(flags, ignore_index=True)
    smooth = pd.concat(smooth, ignore_index=True)
    cur.execute("SET FOREIGN_KEY_CHECKS = 0")
    # the loaders that validate on entry (panel.dnp, panel.fiscal) keep their own findings
    own = ", ".join(f"'{s}'" for s in flags["source"].unique())
    cur.execute(f"DELETE FROM RelationsAndConclusions.DataQualityFlags WHERE source IN ({own})")
    cur.execute("TRUNCATE TABLE RelationsAndConclusions.SmoothedValues")
    load(cur, "RelationsAndConclusions.SmoothedValues", smooth, SMOOTH_COLUMNS)
    load(cur, "RelationsAndConclusions.DataQualityFlags", flags, FLAG_COLUMNS)
    cur.execute("SET FOREIGN_KEY_CHECKS = 1")
    db.commit()
    report(cur)
    db.close()


KINDS = ("error", "missing", "inconsistent", "break", "small_base", "extreme")
ORDER = ["DANE", "DNP", "CUIPO", "ICFES", "MEN", "POLICE", "CNMH", "INDEPAZ", "MEDICINA_LEGAL"]


def report(cur):
    f = query(cur, """
        SELECT f.source, f.source_table, f.column_name, f.kind, f.period, f.note, m.name municipality, d.name department
        FROM RelationsAndConclusions.DataQualityFlags f
        JOIN RelationsAndConclusions.Municipalities m ON m.id = f.municipality_id
        JOIN RelationsAndConclusions.Departments d ON d.id = m.department_id""")
    f["place"] = f["municipality"] + " (" + f["department"].str.title() + ")"
    lines = [
        "# Data quality",
        "",
        "Written by `python -m panel.quality` from `RelationsAndConclusions.DataQualityFlags`; the rules of each source",
        "are at the top of `panel/quality.py`. Nothing in the source tables is changed.",
        "",
        "| Kind | Meaning | What to do with the value |",
        "|---|---|---|",
        "| error | a value the measure does not allow | leave it out |",
        "| missing | no value, for a known reason | nothing to use |",
        "| inconsistent | the source contradicts itself | use with the note in mind |",
        "| break | a jump between years larger than the thing can make | do not read it as change |",
        "| small_base | atypical only because few people stand behind it | use the smoothed value (`SmoothedValues`) |",
        "| extreme | atypical after weighing its base: a real case | keep it |",
        "",
    ]
    for source in ORDER:
        s = f[f["source"] == source]
        if not len(s):
            continue
        lines += [f"## {source.replace('_', ' ').title() if source not in ('DANE', 'DNP', 'CUIPO', 'ICFES', 'MEN', 'CNMH', 'INDEPAZ') else source}", "",
                  "| Table | Column | " + " | ".join(KINDS) + " |", "|---|---|" + "---:|" * len(KINDS)]
        counts = s.pivot_table(index=["source_table", "column_name"], columns="kind", values="period", aggfunc="count", fill_value=0)
        for (t, c), r in counts.iterrows():
            lines.append(f"| {t} | {c} | " + " | ".join(f"{int(r.get(k, 0)):,}" for k in KINDS) + " |")
        lines.append("")
        for (t, c), g in s.groupby(["source_table", "column_name"]):
            lines.append(f"**{t}.{c}**")
            lines.append("")
            for kind in KINDS:
                k = g[g["kind"] == kind]
                if not len(k):
                    continue
                top = k["place"].value_counts()
                if len(k) <= 6 and k["note"].notna().all():
                    items = "; ".join(f"{p}, {per}: {n}" for p, per, n in zip(k["place"], k["period"], k["note"]))
                else:
                    items = ", ".join(f"{p} [{n}]" for p, n in top.head(12).items())
                    items += f" and {len(top) - 12} more" if len(top) > 12 else ""
                lines.append(f"- {kind} ({len(top)} municipalities): {items}.")
            lines.append("")
    out = ROOT / "docs" / "data_quality.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
