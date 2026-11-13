"""
Long-term comparison by government, 2002-2026: Uribe I and II, Santos I and II, Duque, Petro.

    python -m panel.build        # first: writes population.csv and saber_11.csv
    python -m panel.longterm [--out output/panel]

Two kinds of violence source, each read over the days it covers:

- Police records (MinDefensa): homicide, intra-family and sexual violence, January 2003 to the last
  update. Each case has its date. Months are read whole and the first six days of August are moved to
  the outgoing government, because terms start on 7 August.
- Massacres from the Centro Nacional de Memoria Historica (Observatorio de Memoria y Conflicto,
  SIEVCAC), built from press, judicial and social-organisation sources, one row per massacre with its
  exact date and presumed perpetrator, from 1958 to the cut-off in the dataset's description. Its
  definition (conflict massacres) is not the Police one (three or more people killed in one event, a
  table that only starts in 2022), and its most recent years are documented with a lag: the two do not
  measure the same thing, and only this one covers every government.

Rates are cases per 100,000 person-years over the days each source covers, so terms of different
length and municipalities of different size compare.

Saber 11 changed in 2014-2 (no global score before it), so it is compared as a z-score: each
municipality's mean against the national mean and standard deviation of the same exam period. A calendar
A exam of year Y counts for the government in office on 1 September of Y. In `phase`, November 2016
counts as negotiation (the agreement was signed on the 24th) for the Police monthly series.

Writes violence_events.csv, government_panel.csv, phase_panel.csv, by_government.csv and
massacres_by_perpetrator.csv.
"""
import argparse
import re
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

from panel import dane, governments, socrata, sources

POLICE = {
    "homicide": ("m8fd-ahd9", "cantidad"),
    "domestic_violence": ("gepp-dxcs", "cantidad"),
    "sexual_violence": ("bz43-8ahq", "cantidad"),
}
POLICE_START = date(2003, 1, 1)
CNMH_MASSACRES = "d78j-f66e"
INDICATORS = list(POLICE) + ["massacres", "massacre_victims"]
Z_SCORES = ["punt_matematicas", "punt_global"]
MIN_STUDENTS = 30        # municipalities with fewer exam takers in a term are left out of the correlations


def police_events(token):
    """Police cases by municipality and day (month resolution, exact around 7 August)."""
    frames, coverage = [], {}
    for indicator, (dataset, field) in POLICE.items():
        monthly = socrata.query(dataset, select=f"cod_muni, date_trunc_ym(fecha_hecho) as month, sum({field}) as cases",
                                group="cod_muni, month", token=token)
        monthly["day"] = pd.to_datetime(monthly["month"]).dt.date + timedelta(days=6)      # the 7th of the month
        early = socrata.query(dataset, select=f"cod_muni, date_extract_y(fecha_hecho) as y, sum({field}) as cases",
                              where="date_extract_m(fecha_hecho) = 8 and date_extract_d(fecha_hecho) < 7",
                              group="cod_muni, y", token=token)
        moved_in = early.assign(day=[date(int(y), 8, 1) for y in early["y"]])
        moved_out = early.assign(day=[date(int(y), 8, 7) for y in early["y"]],
                                 cases=-pd.to_numeric(early["cases"]))
        df = pd.concat([monthly[["cod_muni", "day", "cases"]], moved_in[["cod_muni", "day", "cases"]],
                        moved_out[["cod_muni", "day", "cases"]]], ignore_index=True)
        df["indicator"] = indicator
        last = date.fromisoformat(socrata.query(dataset, select="max(fecha_hecho) as last", token=token)["last"][0][:10])
        coverage[indicator] = (POLICE_START, last + timedelta(days=1))
        print(f"  {indicator:<18} {dataset}: {pd.to_numeric(monthly['cases']).sum():>10,.0f} cases, {POLICE_START} to {last}")
        frames.append(df)
    df = pd.concat(frames, ignore_index=True)
    df["cases"] = pd.to_numeric(df["cases"])
    df["cod_mpio"] = dane.normalize_code(df["cod_muni"])
    return df.dropna(subset=["cod_mpio"])[["indicator", "cod_mpio", "day", "cases"]], coverage


def cnmh_massacres(token):
    """CNMH massacres from the first government on: one row per massacre, with its victims."""
    first = governments.TERMS[0][2]
    rows = socrata.query(CNMH_MASSACRES,
                         select="id_caso, a_o, mes, d_a, c_digo_dane_de_municipio, presunto_responsable, total_de_v_ctimas_del_caso",
                         where=f"a_o >= {first.year}", order="id_caso", token=token)
    year, month, day = (pd.to_numeric(rows[c], errors="coerce") for c in ("a_o", "mes", "d_a"))
    month, day = month.where(month.between(1, 12), 7), day.where(day.between(1, 31), 15)   # unknown -> mid-period

    def safe(y, m, d):
        while True:
            try:
                return date(int(y), int(m), int(d))
            except ValueError:
                d -= 1
    rows["day"] = [safe(y, m, d) for y, m, d in zip(year, month, day)]
    rows = rows[rows["day"] >= first]
    rows["cod_mpio"] = dane.normalize_code(rows["c_digo_dane_de_municipio"])
    rows["victims"] = pd.to_numeric(rows["total_de_v_ctimas_del_caso"], errors="coerce").fillna(0)
    rows["perpetrator"] = rows["presunto_responsable"].fillna("SIN INFORMACION")

    description = socrata.dataset_description(CNMH_MASSACRES)
    cut = re.search(r"(\d{1,2})\s*-\s*(\d{1,2})\s*-\s*(\d{4})", description)
    last = date(int(cut.group(3)), int(cut.group(2)), int(cut.group(1))) if cut else max(rows["day"])
    print(f"  massacres (CNMH)   {CNMH_MASSACRES}: {len(rows):>10,} massacres, {int(rows['victims'].sum()):,} victims, "
          f"{first} to {last}")

    events = pd.concat([
        rows.assign(indicator="massacres", cases=1),
        rows.assign(indicator="massacre_victims", cases=rows["victims"]),
    ])[["indicator", "cod_mpio", "day", "cases"]].dropna(subset=["cod_mpio"])
    coverage = {k: (first, last + timedelta(days=1)) for k in ("massacres", "massacre_victims")}
    return events, coverage, rows


def saber_z(saber: pd.DataFrame, token) -> pd.DataFrame:
    """Municipal z-scores per calendar A exam period, against the national mean and SD of that period."""
    commas = " or ".join(f"{c} like '%,%'" for c in sources.SABER["scores"])
    bad = socrata.query(sources.SABER["dataset"], select="estu_consecutivo", where=commas,
                        order="estu_consecutivo", token=token)
    where = None
    if len(bad):
        where = "estu_consecutivo not in (" + ", ".join(f"'{e}'" for e in bad["estu_consecutivo"]) + ")"
    stats = ", ".join(f"avg({c}::number) as {c}_mean, stddev_pop({c}::number) as {c}_sd" for c in Z_SCORES)
    national = socrata.query(sources.SABER["dataset"], select=f"periodo, {stats}", where=where,
                             group="periodo", token=token)

    a = saber[saber["calendar"] == "A"].copy()
    a["periodo"] = a["periodo"].astype(str)
    for c in Z_SCORES:
        a[c] = a[c] * a["students"]
    a = a.groupby(["cod_mpio", "periodo", "year"], as_index=False)[["students"] + Z_SCORES].sum(min_count=1)
    for c in Z_SCORES:
        a[c] = a[c] / a["students"]
    a = a.merge(national, on="periodo", how="left")
    for c in Z_SCORES:
        a[f"{c}_z"] = (a[c] - pd.to_numeric(a.get(f"{c}_mean"))) / pd.to_numeric(a.get(f"{c}_sd"))
    a["government"] = [governments.government(date(int(y), 9, 1)) for y in a["year"]]
    a["phase"] = [governments.phase(date(int(y), 9, 1)) for y in a["year"]]
    return a


def by_period(events, coverage, population, saber, key: str, periods) -> pd.DataFrame:
    events = events.copy()
    events["period"] = [getattr(governments, key)(d) for d in events["day"]]
    cases = (events.dropna(subset=["period"])
             .groupby(["cod_mpio", "period", "indicator"])["cases"].sum().unstack("indicator"))

    exposures = {}
    for indicator in INDICATORS:
        window = coverage[indicator]
        if window not in exposures:
            exposures[window] = governments.person_years(population, periods, *window)
    longest = max(exposures, key=lambda w: w[1] - w[0])
    panel = exposures[longest].merge(cases.reset_index(), on=["cod_mpio", "period"], how="left")
    for indicator in INDICATORS:
        exposure = exposures[coverage[indicator]].rename(columns={"person_years": f"{indicator}_person_years"})
        panel = panel.merge(exposure, on=["cod_mpio", "period"], how="left")
        panel[indicator] = panel[indicator].fillna(0) if indicator in panel else 0.0
        panel[f"{indicator}_rate"] = panel[indicator] / panel[f"{indicator}_person_years"] * 1e5

    s = saber.dropna(subset=[key]).copy()
    zs = [f"{c}_z" for c in Z_SCORES]
    for c in zs:
        s[f"{c}_w"] = s[c] * s["students"]
        s[f"{c}_n"] = s["students"].where(s[c].notna(), 0)
    s = s.groupby(["cod_mpio", key], as_index=False).agg(
        saber_students=("students", "sum"), saber_exams=("year", "nunique"),
        **{f"{c}_w": (f"{c}_w", "sum") for c in zs}, **{f"{c}_n": (f"{c}_n", "sum") for c in zs})
    for c in zs:
        s[c] = s[f"{c}_w"] / s[f"{c}_n"].replace(0, np.nan)
    s = s.drop(columns=[f"{c}_{x}" for c in zs for x in ("w", "n")])
    panel = panel.merge(s.rename(columns={key: "period"}), on=["cod_mpio", "period"], how="left")
    order = governments.ORDER if key == "government" else governments.PHASE_ORDER
    panel["period"] = pd.Categorical(panel["period"], categories=order, ordered=True)
    return panel.sort_values(["period", "cod_mpio"])


def summary(panel: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for period, d in panel.groupby("period", observed=True):
        row = {"period": period}
        for indicator in INDICATORS:
            row[f"{indicator}_rate"] = d[indicator].sum() / d[f"{indicator}_person_years"].sum() * 1e5
        row["massacres"] = d["massacres"].sum()
        enough = d[(d["saber_students"] >= MIN_STUDENTS) & d["punt_matematicas_z"].notna()]
        row["municipalities_with_saber"] = len(enough)
        for indicator in ("homicide", "massacre_victims"):
            row[f"corr_{indicator}_vs_math_z"] = (
                enough[f"{indicator}_rate"].corr(enough["punt_matematicas_z"], method="spearman")
                if len(enough) > 30 else np.nan)
        rows.append(row)
    return pd.DataFrame(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", default="output/panel", type=Path)
    args = parser.parse_args()
    token = socrata.app_token()

    population = pd.read_csv(args.out / "population.csv", dtype={"cod_mpio": str})
    saber = pd.read_csv(args.out / "saber_11.csv", dtype={"cod_mpio": str, "periodo": str})

    print("violence")
    police, coverage = police_events(token)
    massacres, cnmh_coverage, massacre_rows = cnmh_massacres(token)
    events, coverage = pd.concat([police, massacres], ignore_index=True), {**coverage, **cnmh_coverage}
    print("saber 11 z-scores")
    z = saber_z(saber, token)

    terms = [(k, s, e) for k, _, s, e in governments.TERMS]
    government_panel = by_period(events, coverage, population, z, "government", terms)
    phase_panel = by_period(events, coverage, population, z, "phase", governments.PHASES)
    table = summary(government_panel)

    massacre_rows["government"] = pd.Categorical([governments.government(d) for d in massacre_rows["day"]],
                                                 categories=governments.ORDER, ordered=True)
    perpetrators = (massacre_rows.groupby(["government", "perpetrator"], observed=True)
                    .agg(massacres=("id_caso", "count"), victims=("victims", "sum")).reset_index())

    events.to_csv(args.out / "violence_events.csv", index=False)
    government_panel.to_csv(args.out / "government_panel.csv", index=False)
    phase_panel.to_csv(args.out / "phase_panel.csv", index=False)
    table.to_csv(args.out / "by_government.csv", index=False)
    perpetrators.to_csv(args.out / "massacres_by_perpetrator.csv", index=False)

    pd.set_option("display.width", 220)
    print(table.round(3).to_string(index=False))
    print(summary(phase_panel)[["period", "homicide_rate", "massacres", "massacre_victims_rate",
                                "corr_homicide_vs_math_z"]].round(3).to_string(index=False))
    print(perpetrators.pivot_table(index="perpetrator", columns="government", values="massacres",
                                   fill_value=0, observed=True).astype(int).to_string())


if __name__ == "__main__":
    main()
