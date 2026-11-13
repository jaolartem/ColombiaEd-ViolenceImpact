"""
DANE: population by sex and age 1995-2042, and the 2018 census (CNPV) by municipality.

    python -m panel.census [--out output/panel]

Population (projections and back-projections based on the 2018 census), area "Total", by sex and age
band. Single ages 15 to 19 are kept apart: they are the cohort that sits Saber 11, so the share of a
municipality's 17-year-olds who reach the exam can be measured.

2018 census, one row per municipality, to set beside what the students report:
- multidimensional poverty (IPM, census source) and its 15 deprivations (overcrowding, low educational
  attainment, school non-attendance, child labour, earth floors, no improved water, ...);
- unsatisfied basic needs (NBI) and its components;
- occupied dwellings by floor material and by public services, internet included;
- people by energy stratum.

The DANE files are not consistent with each other (the 1995-2004 file has the code in DPMP and the
2005-2017 one in MPIO), so the code column is found by its content.

Writes population_sex_age.csv and census_2018.csv.
"""
import argparse
import re
from pathlib import Path

import openpyxl
import pandas as pd
import requests

from panel import dane
from panel.indepaz import key

CACHE = Path("cache/dane")
POPULATION = [
    "DCD-area-sexo-edad-proypoblacion-Mun-1995-2004.xlsx",
    "DCD-area-sexo-edad-proypoblacion-Mun-2005-2017_VP.xlsx",
    "PPED-AreaSexoEdadMun-2018-2042_VP.xlsx",
]
CNPV = {
    "anexo-censal-pobreza-municipal-2018.xlsx":
        "https://www.dane.gov.co/files/investigaciones/condiciones_vida/pobreza/2018/informacion-censal/",
    "CNPV-2018-NBI.xlsx": "https://www.dane.gov.co/files/censo2018/informacion-tecnica/",
    "VIVIENDAS_Cuadros_CNPV_2018.XLSX": "https://www.dane.gov.co/files/censo2018/informacion-tecnica/",
}
AGE_BANDS = ([(a, a + 4) for a in range(0, 15, 5)] + [(a, a) for a in range(15, 20)]
             + [(a, a + 4) for a in range(20, 80, 5)] + [(80, 200)])
SEX_AGE = re.compile(r"(hombres|mujeres)\D*(\d+)", re.I)


def _download(name: str, base: str, folder: Path) -> Path:
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / name
    if not path.is_file():
        response = requests.get(base + name, headers={"User-Agent": "Mozilla/5.0"}, timeout=600)
        response.raise_for_status()
        path.write_bytes(response.content)
    return path


def population_by_sex_age() -> pd.DataFrame:
    frames = []
    for name in POPULATION:
        path = _download(name, dane.BASE_URL, CACHE)
        wb = openpyxl.load_workbook(path, read_only=True)
        ws = wb[wb.sheetnames[-1]]
        rows = ws.iter_rows(values_only=True)
        header = None
        for row in rows:
            if row and row[0] == "DP":
                header = list(row)
                break
        sub = next(rows)                      # 2018-2042 has a second header row with the age labels
        if any(isinstance(v, str) and SEX_AGE.search(v) for v in sub):
            labels = [s if isinstance(s, str) and SEX_AGE.search(s) else h for h, s in zip(header, sub)]
            first = []
        else:
            labels, first = header, [sub]
        ages = [(i, SEX_AGE.search(l)) for i, l in enumerate(labels) if isinstance(l, str) and SEX_AGE.search(l)]
        year_col = labels.index("AÑO")
        area_col = labels.index("ÁREA GEOGRÁFICA")
        code_col = None
        records = []
        for row in first + list(rows):
            if row is None or row[area_col] != "Total":
                continue
            if code_col is None:
                code_col = next(i for i in range(4) if isinstance(row[i], str) and re.fullmatch(r"\d{5}", row[i]))
            for i, m in ages:
                records.append((row[code_col], int(row[year_col]), "M" if m.group(1).lower() == "hombres" else "F",
                                int(m.group(2)), row[i] or 0))
        wb.close()
        df = pd.DataFrame(records, columns=["cod_mpio", "year", "sex", "age", "population"])
        print(f"  {name}: {df['year'].min()}-{df['year'].max()}, {df['cod_mpio'].nunique()} municipalities")
        frames.append(df)
    df = pd.concat(frames, ignore_index=True)
    df["cod_mpio"] = dane.normalize_code(df["cod_mpio"])
    band = {age: b for b in AGE_BANDS for age in range(b[0], min(b[1], 120) + 1)}
    df["age_from"] = df["age"].map(lambda a: band[min(a, 120)][0])
    df["age_to"] = df["age"].map(lambda a: band[min(a, 120)][1])
    df = df.groupby(["cod_mpio", "year", "sex", "age_from", "age_to"], as_index=False)["population"].sum()
    df["age_to"] = df["age_to"].where(df["age_to"] < 200, None)       # 80+ has no upper bound
    return df.drop_duplicates(["cod_mpio", "year", "sex", "age_from"], keep="last")


def _cuadro(path: Path, sheet: str, area_total: str) -> pd.DataFrame:
    """A municipal CNPV table: rows of the municipal total, with the DANE code."""
    df = pd.read_excel(path, sheet_name=sheet, header=None)
    department = df[0].ffill().astype(str).str.extract(r"^(\d{2})_")[0]
    municipality = df[1].ffill().astype(str).str.extract(r"^(\d{3,5})_")[0]
    code = [m if isinstance(m, str) and len(m) == 5 else (d + m if isinstance(m, str) and isinstance(d, str) else None)
            for d, m in zip(department, municipality)]
    df["cod_mpio"] = code
    keep = df[2].astype(str).str.strip().eq(area_total)
    if sheet.startswith("7V"):
        keep &= df[3].astype(str).str.strip().eq("Total")
    df = df[keep & df["cod_mpio"].notna() & df[1].notna()]
    return df


def census_2018() -> pd.DataFrame:
    folder = CACHE / "cnpv"
    paths = {name: _download(name, base, folder) for name, base in CNPV.items()}

    ipm = pd.read_excel(paths["anexo-censal-pobreza-municipal-2018.xlsx"], sheet_name="2_IPM Mpio y Dpt",
                        header=0, dtype={"ID": str})
    ipm = pd.DataFrame({"cod_mpio": dane.normalize_code(ipm["ID"]), "ipm": pd.to_numeric(ipm["IPM Municipal"], errors="coerce")})
    priv = pd.read_excel(paths["anexo-censal-pobreza-municipal-2018.xlsx"], sheet_name="6_Privaciones IPM Dpt-Mpio",
                         header=1, dtype={"ID": str})
    priv.columns = ["cod_mpio", "municipality"] + ["deprivation_" + key(c).replace(" ", "_") for c in priv.columns[2:]]
    priv["cod_mpio"] = dane.normalize_code(priv["cod_mpio"])
    priv = priv.drop(columns="municipality")
    for c in priv.columns[1:]:
        priv[c] = pd.to_numeric(priv[c], errors="coerce")

    nbi = pd.read_excel(paths["CNPV-2018-NBI.xlsx"], sheet_name="Municipios", header=None, skiprows=10,
                        dtype={0: str, 2: str})
    nbi = pd.DataFrame({
        "cod_mpio": dane.normalize_code(nbi[0].str.zfill(2) + nbi[2].str.zfill(3)),
        "nbi": nbi[4], "nbi_misery": nbi[5], "nbi_housing": nbi[6], "nbi_services": nbi[7],
        "nbi_overcrowding": nbi[8], "nbi_school_non_attendance": nbi[9], "nbi_economic_dependency": nbi[10],
    })
    for c in nbi.columns[1:]:
        nbi[c] = pd.to_numeric(nbi[c], errors="coerce")

    viv = paths["VIVIENDAS_Cuadros_CNPV_2018.XLSX"]
    floors = _cuadro(viv, "7V_MPIO", "Total municipal")
    floors = pd.DataFrame({"cod_mpio": floors["cod_mpio"], "dwellings_occupied": floors[4],
                           "share_earth_floor": floors[10] / floors[4]})
    services = _cuadro(viv, "8V_MPIO", "Total municipal")
    services = pd.DataFrame({
        "cod_mpio": services["cod_mpio"],
        "share_electricity": services[5] / services[4], "share_water": services[8] / services[7],
        "share_sewer": services[11] / services[10], "share_gas": services[14] / services[13],
        "share_garbage": services[18] / services[17], "share_internet": services[21] / services[20],
    })
    strata = _cuadro(viv, "10V_MPIO", "Total")
    total = strata[3].astype(float)
    strata = pd.DataFrame({
        "cod_mpio": strata["cod_mpio"],
        **{f"share_stratum_{k}": strata[5 + k] / total for k in range(1, 7)},
        "share_no_electricity_service": strata[4] / total,
    })
    strata["share_stratum_1_2"] = strata["share_stratum_1"] + strata["share_stratum_2"]

    out = ipm.merge(priv, on="cod_mpio", how="outer")
    for part in (nbi, floors, services, strata):
        part["cod_mpio"] = dane.normalize_code(part["cod_mpio"])
        out = out.merge(part.drop_duplicates("cod_mpio"), on="cod_mpio", how="outer")
    out = out.dropna(subset=["cod_mpio"])
    for c in out.columns[1:]:
        out[c] = pd.to_numeric(out[c], errors="coerce")
    print(f"  census 2018: {len(out)} municipalities, {out.shape[1] - 1} indicators")
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", default="output/panel", type=Path)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    print("DANE")
    census = census_2018()
    census.to_csv(args.out / "census_2018.csv", index=False)
    population = population_by_sex_age()
    population.to_csv(args.out / "population_sex_age.csv", index=False)
    print(f"  population by sex and age: {len(population):,} rows")


if __name__ == "__main__":
    main()
