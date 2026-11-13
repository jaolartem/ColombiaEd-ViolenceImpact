"""
Long-term comparison by government, 2003-2026: Uribe I and II, Santos I and II, Duque, Petro.

    python -m panel.build        # first: writes population.csv and saber_11.csv
    python -m panel.longterm [--out output/panel]

Violence comes from the Police records (MinDefensa), the only municipal series on datos.gov.co that runs
from January 2003: each case has its date, so it is assigned to the government in office that day. Months
are read whole and the first six days of August are moved to the outgoing government, because terms start
on 7 August. (In `phase`, November 2016 counts as negotiation: the agreement was signed on the 24th.)

Rates are cases per 100,000 person-years, so terms of different length and municipalities of different
size compare. Uribe I is covered from January 2003 only.

Saber 11 changed in 2014-2 (no global score before it), so it is compared as a z-score: each
municipality's mean against the national mean and standard deviation of the same exam period. A calendar
A exam of year Y counts for the government in office on 1 September of Y.

Writes police_monthly.csv, government_panel.csv, phase_panel.csv and by_government.csv.
"""
import argparse
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
# Not here: the massacres table (u8eq-92tb) only starts in 2022, so it cannot compare governments.
COVERAGE_START = date(2003, 1, 1)
Z_SCORES = ["punt_matematicas", "punt_global"]
MIN_STUDENTS = 30        # municipalities with fewer exam takers in a term are left out of the correlations


def police_monthly(token) -> pd.DataFrame:
    frames = []
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
        last = socrata.query(dataset, select="max(fecha_hecho) as last", token=token)["last"][0][:10]
        print(f"  {indicator:<18} {dataset}: {pd.to_numeric(monthly['cases']).sum():>10,.0f} cases to {last}")
        frames.append(df.assign(last=last))
    df = pd.concat(frames, ignore_index=True)
    df["cases"] = pd.to_numeric(df["cases"])
    df["cod_mpio"] = dane.normalize_code(df["cod_muni"])
    return df.dropna(subset=["cod_mpio"])[["indicator", "cod_mpio", "day", "cases", "last"]]


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


def by_period(police, population, saber, key: str, periods, coverage_end) -> pd.DataFrame:
    police = police.copy()
    police["period"] = [getattr(governments, key)(d) for d in police["day"]]
    cases = (police.dropna(subset=["period"])
             .groupby(["cod_mpio", "period", "indicator"])["cases"].sum().unstack("indicator"))
    exposure = governments.person_years(population, periods, COVERAGE_START, coverage_end)
    panel = exposure.merge(cases.reset_index(), on=["cod_mpio", "period"], how="left")
    for indicator in POLICE:
        panel[indicator] = panel[indicator].fillna(0)
        panel[f"{indicator}_rate"] = panel[indicator] / panel["person_years"] * 1e5

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
        row = {"period": period, "person_years_millions": d["person_years"].sum() / 1e6}
        for indicator in POLICE:
            row[f"{indicator}_rate"] = d[indicator].sum() / d["person_years"].sum() * 1e5
        enough = d[(d["saber_students"] >= MIN_STUDENTS) & d["punt_matematicas_z"].notna()]
        row["municipalities_with_saber"] = len(enough)
        row["corr_homicide_vs_math_z"] = (enough["homicide_rate"].corr(enough["punt_matematicas_z"], method="spearman")
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

    print("police records (MinDefensa)")
    police = police_monthly(token)
    coverage_end = min(date.fromisoformat(d) for d in police["last"].unique()) + timedelta(days=1)
    print("saber 11 z-scores")
    z = saber_z(saber, token)

    government_panel = by_period(police, population, z, "government",
                                 [(k, s, e) for k, _, s, e in governments.TERMS], coverage_end)
    phase_panel = by_period(police, population, z, "phase", governments.PHASES, coverage_end)
    table = summary(government_panel)

    police.drop(columns="last").to_csv(args.out / "police_monthly.csv", index=False)
    government_panel.to_csv(args.out / "government_panel.csv", index=False)
    phase_panel.to_csv(args.out / "phase_panel.csv", index=False)
    table.to_csv(args.out / "by_government.csv", index=False)
    pd.set_option("display.width", 200)
    print(table.round(3).to_string(index=False))
    print(summary(phase_panel)[["period", "homicide_rate", "corr_homicide_vs_math_z"]]
          .round(3).to_string(index=False))


if __name__ == "__main__":
    main()
