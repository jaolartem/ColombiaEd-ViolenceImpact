"""
The four dimension indices and the final index, by the Human Development Index method (panel/index.py):
each sub-index between fixed goalposts (0 and the 99th percentile of the whole panel, or 0 and 1 for a
share), combined with a geometric mean. Higher = more violence or more deprivation.

Galtung's dimensions are the legend: physical, cultural (violence that targets an identity), gender and
structural (census 2018 deprivation and access). Rates are per 100,000 inhabitants, or per 100,000 women
for the homicide and suicide of women. Years 2015-2025; 2026 is a partial year and is left out.
"""
import numpy as np
import pandas as pd

from panel import index
from panel.indepaz import key

YEARS = range(2015, 2026)
ETHNIC = {"negro", "indigena", "mulato", "raizal", "palenquero"}
NOT_A_GROUP = {"ninguno", "sin informacion", "otro", "no aplica"}
SOCIOPOLITICAL = {"asesinato politico", "violencia sociopolitica"}


def _scored(rates: pd.DataFrame, components: list, prefix="subin_") -> pd.DataFrame:
    upper = index.goalposts(rates, components)
    out = rates[["cod_mpio", "year"]].copy()
    for c in components:
        out[prefix + c] = (rates[c] / upper[c]).clip(0, 1) if upper[c] > 0 else 0.0
    out["index"] = index.dimension_index(rates, components, upper)
    return out


def _grid(population: pd.DataFrame) -> pd.DataFrame:
    return population[population["year"].isin(YEARS)][["cod_mpio", "year", "population"]].copy()


def physical(cases: pd.DataFrame, population: pd.DataFrame) -> pd.DataFrame:
    grid = _grid(population)
    totals = cases.groupby(["cod_mpio", "year", "indicator"])["cases"].sum().unstack("indicator").reset_index()
    grid = grid.merge(totals, on=["cod_mpio", "year"], how="left")
    parts = ["homicide", "suicide", "violence_children", "domestic_violence"]
    for c in parts:
        grid[c] = grid[c].fillna(0) / grid["population"] * 1e5
    return _scored(grid, parts).rename(columns={"index": "physical_violence_index"})


def gender(cases: pd.DataFrame, population: pd.DataFrame, by_sex_age: pd.DataFrame) -> pd.DataFrame:
    grid = _grid(population)
    women = by_sex_age[by_sex_age["sex"] == "F"].groupby(["cod_mpio", "year"], as_index=False)["population"].sum()
    grid = grid.merge(women.rename(columns={"population": "women"}), on=["cod_mpio", "year"], how="left")
    totals = cases.groupby(["cod_mpio", "year", "indicator"])["cases"].sum().unstack("indicator").reset_index()
    female = (cases[cases["sex"] == "F"].groupby(["cod_mpio", "year", "indicator"])["cases"].sum()
              .unstack("indicator").reset_index())
    grid = grid.merge(totals[["cod_mpio", "year", "partner_violence", "sexual_violence"]], on=["cod_mpio", "year"], how="left")
    grid = grid.merge(female[["cod_mpio", "year", "homicide", "suicide"]].rename(
        columns={"homicide": "female_homicide", "suicide": "female_suicide"}), on=["cod_mpio", "year"], how="left")
    for c in ("partner_violence", "sexual_violence"):
        grid[c] = grid[c].fillna(0) / grid["population"] * 1e5
    for c in ("female_homicide", "female_suicide"):
        grid[c] = grid[c].fillna(0) / grid["women"] * 1e5
    return _scored(grid, ["partner_violence", "sexual_violence", "female_homicide", "female_suicide"]).rename(
        columns={"index": "gender_violence_index"})


def cultural(identity: pd.DataFrame, population: pd.DataFrame) -> pd.DataFrame:
    grid = _grid(population)
    hom = identity[identity["indicator"] == "homicide"].copy()
    hom["k"] = hom["group_name"].map(key)
    measures = {
        "ethnic_homicide": hom[(hom["kind"] == "racial_ancestry") & hom["k"].isin(ETHNIC)],
        "vulnerable_group_homicide": hom[(hom["kind"] == "vulnerable_group") & ~hom["k"].isin(NOT_A_GROUP)],
        "sociopolitical_homicide": hom[(hom["kind"] == "circumstance") & hom["k"].isin(SOCIOPOLITICAL)],
    }
    for name, d in measures.items():
        grid = grid.merge(d.groupby(["cod_mpio", "year"], as_index=False)["cases"].sum().rename(columns={"cases": name}),
                          on=["cod_mpio", "year"], how="left")
        grid[name] = grid[name].fillna(0) / grid["population"] * 1e5
    return _scored(grid, list(measures)).rename(columns={"index": "cultural_violence_index"})


def structural(census: pd.DataFrame, health_sites: pd.DataFrame, population: pd.DataFrame) -> pd.DataFrame:
    """Census 2018 deprivation (shares, goalposts 0 and 1) and the lack of health sites."""
    out = census[["cod_mpio"]].copy()
    out["subin_multidimensional_poverty"] = (census["ipm"] / 100).clip(0, 1)
    out["subin_unsatisfied_needs"] = (census["nbi"] / 100).clip(0, 1)
    out["subin_no_internet"] = (1 - census["share_internet"]).clip(0, 1)
    pop = population[population["year"] == 2025][["cod_mpio", "population"]]
    sites = health_sites.groupby("cod_mpio", as_index=False)["sites"].sum().merge(pop, on="cod_mpio", how="right")
    sites["per_100k"] = sites["sites"].fillna(0) / sites["population"] * 1e5
    upper = sites["per_100k"].quantile(0.99)
    sites["subin_health_access"] = 1 - (sites["per_100k"] / upper).clip(0, 1)
    out = out.merge(sites[["cod_mpio", "subin_health_access"]], on="cod_mpio", how="left")
    parts = ["subin_multidimensional_poverty", "subin_unsatisfied_needs", "subin_no_internet", "subin_health_access"]
    complete = out[parts].notna().all(axis=1)
    out["structural_violence_index"] = np.exp(np.log(out[parts].clip(lower=index.FLOOR)).mean(axis=1)).where(complete)
    return out


def final(physical_df, cultural_df, gender_df, structural_df) -> pd.DataFrame:
    out = (physical_df[["cod_mpio", "year", "physical_violence_index"]]
           .merge(cultural_df[["cod_mpio", "year", "cultural_violence_index"]], on=["cod_mpio", "year"], how="outer")
           .merge(gender_df[["cod_mpio", "year", "gender_violence_index"]], on=["cod_mpio", "year"], how="outer")
           .merge(structural_df[["cod_mpio", "structural_violence_index"]], on="cod_mpio", how="left"))
    parts = ["physical_violence_index", "cultural_violence_index", "gender_violence_index", "structural_violence_index"]
    complete = out[parts].notna().all(axis=1)
    out["final_violence_index"] = np.exp(np.log(out[parts].clip(lower=index.FLOOR)).mean(axis=1)).where(complete)
    return out
