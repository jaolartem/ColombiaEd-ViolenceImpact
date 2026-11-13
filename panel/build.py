"""
Builds the municipal panel.

    python -m panel.build [--out output/panel]

Writes, one row per DANE municipality code:
    violence_cases.csv    indicator, cod_mpio, year, sex, cases, preliminary
    saber_11.csv          cod_mpio, periodo, year, calendar, sex, students, mean scores
    men_education.csv     cod_mpio, year, enrolment / dropout / approval rates
    population.csv        cod_mpio, year, population (DANE)
    municipal_panel.csv   cod_mpio x year: population, cases and rates per 100k, physical violence
                          index, Saber 11 calendar A means, MEN rates
"""
import argparse
from pathlib import Path

import pandas as pd

from panel import dane, index, socrata, sources

FIRST_YEAR, LAST_YEAR = 2010, 2026
VIOLENCE_FROM = 2015          # first year of the Medicina Legal series
PRELIMINARY_FROM = 2025
PARTIAL_YEAR = 2026           # preliminary data run January to July
PHYSICAL = ["homicide", "suicide", "violence_children", "domestic_violence"]
SEX = {"Hombre": "M", "Mujer": "F", "M": "M", "F": "F"}


def violence(token) -> pd.DataFrame:
    frames = []
    for indicator, parts in sources.VIOLENCE.items():
        for dataset, where, preliminary in parts:
            ml = sources.ML
            df = socrata.query(dataset, select=f"{ml['code']}, {ml['year']}, {ml['sex']}, count(*) as cases",
                               where=where, group=f"{ml['code']}, {ml['year']}, {ml['sex']}", token=token)
            df = df.rename(columns={ml["code"]: "cod_mpio", ml["year"]: "year", ml["sex"]: "sex"})
            df["indicator"], df["preliminary"] = indicator, preliminary
            frames.append(df)
            print(f"  {indicator:<18} {dataset}: {pd.to_numeric(df['cases']).sum():>9,.0f} cases")
    df = pd.concat(frames, ignore_index=True)
    df["cases"] = pd.to_numeric(df["cases"])
    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    df["sex"] = df["sex"].map(SEX).fillna("U")
    df["cod_mpio"] = dane.normalize_code(df["cod_mpio"])
    unplaced = df[df["cod_mpio"].isna()].groupby("indicator")["cases"].sum()
    if unplaced.any():
        print("  cases without a municipality code (left out):", unplaced.to_dict())
    df = df.dropna(subset=["cod_mpio", "year"])
    df["year"] = df["year"].astype(int)
    df = df[(df["year"] < PRELIMINARY_FROM) != df["preliminary"]]    # each year from one series only
    return (df.groupby(["indicator", "cod_mpio", "year", "sex", "preliminary"], as_index=False)["cases"].sum()
              [["indicator", "cod_mpio", "year", "sex", "cases", "preliminary"]])


def saber(token) -> pd.DataFrame:
    s = sources.SABER
    periods = socrata.query(s["dataset"], select="periodo", group="periodo", token=token)["periodo"]
    averages = ", ".join(f"avg({c}::number) as {c}" for c in s["scores"])
    # A few rows write a score with a decimal comma ("35,2"), which the server cannot cast to a number
    # (seven in 20112). They are found first and left out by student id.
    commas = " or ".join(f"{c} like '%,%'" for c in s["scores"])
    bad = socrata.query(s["dataset"], select="periodo, estu_consecutivo", where=commas, order="estu_consecutivo", token=token)
    frames = []
    for periodo in periods:
        where = f"periodo = '{periodo}'"
        excluded = bad[bad["periodo"] == periodo]["estu_consecutivo"].tolist() if len(bad) else []
        if excluded:
            where += " and estu_consecutivo not in (" + ", ".join(f"'{e}'" for e in excluded) + ")"
        frames.append(socrata.query(
            s["dataset"],
            select=f"{s['code']}, periodo, estu_genero, count(distinct estu_consecutivo) as students, {averages}",
            where=where,   # every row is a school student (estu_estudiante = ESTUDIANTE)
            group=f"{s['code']}, periodo, estu_genero", token=token))
    if not any(len(f) for f in frames):
        raise RuntimeError("Saber 11: the API returned no rows")
    df = pd.concat(frames, ignore_index=True).rename(columns={s["code"]: "cod_mpio", "estu_genero": "sex"})
    df["cod_mpio"] = dane.normalize_code(df["cod_mpio"])
    df["year"] = df["periodo"].str[:4].astype(int)
    df["calendar"] = df["periodo"].str[-1].map(lambda d: "B" if d == "1" else "A")
    df["sex"] = df["sex"].map(SEX).fillna("U")
    for c in ["students"] + s["scores"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    print(f"  saber 11: {df['students'].sum():,.0f} students, periods {', '.join(sorted(periods))}")
    return df.dropna(subset=["cod_mpio"])[["cod_mpio", "periodo", "year", "calendar", "sex", "students"] + s["scores"]]


def men(token) -> pd.DataFrame:
    m = sources.MEN
    df = socrata.query(m["dataset"], select=", ".join([m["code"], m["year"], *m["columns"]]),
                       order=f"{m['year']}, {m['code']}", token=token)
    df = df.rename(columns={m["code"]: "cod_mpio", m["year"]: "year", **m["columns"]})
    df["cod_mpio"] = dane.normalize_code(df["cod_mpio"])
    df["year"] = pd.to_numeric(df["year"]).astype(int)
    for c in m["columns"].values():
        df[c] = pd.to_numeric(df[c], errors="coerce")
    print(f"  MEN: {len(df):,} municipality-years, {df['year'].min()}-{df['year'].max()}")
    return df.dropna(subset=["cod_mpio"])


def panel(population, cases, saber_df, men_df) -> pd.DataFrame:
    grid = population[population["year"].between(FIRST_YEAR, LAST_YEAR)].copy()

    totals = cases.groupby(["cod_mpio", "year", "indicator"])["cases"].sum().unstack("indicator")
    grid = grid.merge(totals, on=["cod_mpio", "year"], how="left")
    covered = grid["year"] >= VIOLENCE_FROM
    for indicator in sources.VIOLENCE:
        grid.loc[covered, indicator] = grid.loc[covered, indicator].fillna(0)
        grid[f"{indicator}_rate"] = grid[indicator] / grid["population"] * 1e5
    grid["preliminary"] = grid["year"] >= PRELIMINARY_FROM
    grid["partial_year"] = grid["year"] == PARTIAL_YEAR

    full_years = grid[covered & ~grid["partial_year"]]
    rates = [f"{c}_rate" for c in PHYSICAL]
    upper = index.goalposts(full_years, rates)
    grid["physical_violence_index"] = index.dimension_index(grid, rates, upper).where(covered & ~grid["partial_year"])
    print("  goalposts (99th percentile, per 100k):", {k: round(v, 1) for k, v in upper.items()})

    scores = sources.SABER["scores"]
    a = saber_df[saber_df["calendar"] == "A"].copy()
    for c in scores:
        a[c] = a[c] * a["students"]
    a = a.groupby(["cod_mpio", "year"], as_index=False)[["students"] + scores].sum()
    for c in scores:
        a[c] = a[c] / a["students"]
    a = a.rename(columns={"students": "saber_students", **{c: f"saber_{c}" for c in scores}})
    grid = grid.merge(a, on=["cod_mpio", "year"], how="left")
    return grid.merge(men_df, on=["cod_mpio", "year"], how="left")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", default="output/panel", type=Path)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    token = socrata.app_token()
    print("datos.gov.co", "with app token" if token else "without app token (works, with a lower rate limit)")

    print("violence (Medicina Legal)");  cases = violence(token)
    print("education (ICFES, MEN)");     saber_df, men_df = saber(token), men(token)
    print("population (DANE)");          population = dane.load_population()

    result = panel(population, cases, saber_df, men_df)
    for name, df in [("violence_cases", cases), ("saber_11", saber_df), ("men_education", men_df),
                     ("population", population), ("municipal_panel", result)]:
        df.to_csv(args.out / f"{name}.csv", index=False)
    print(f"wrote {args.out}: {len(result):,} municipality-years, {result['cod_mpio'].nunique():,} municipalities")


if __name__ == "__main__":
    main()
