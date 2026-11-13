"""
DANE municipal codes and population.

Sources write the same code in different ways: Medicina Legal drops the leading zero ("5001"),
ICFES and DANE keep it ("05001"), and names vary ("Bogotá, D.C." / "Bogotá D.C."). Everything is
joined on the 5-character DANE code, never on names.
"""
from pathlib import Path

import pandas as pd
import requests

POPULATION_FILES = {
    # Back-projections 1995-2004 and 2005-2017 and the 2018-2042 projection, all based on the 2018 census.
    "DCD-area-proypoblacion-Mun-1995-2004.xlsx": dict(header=11, code="DPMP", year="AÑO", value="Población"),
    "DCD-area-proypoblacion-Mun-2005-2017_VP.xlsx": dict(header=11, code="MPIO", year="AÑO", value="Población"),
    "PPED-AreaMun-2018-2042_VP.xlsx": dict(sheet="PobMunicipalxÁrea", header=7, code="MPIO", year="AÑO", value="TOTAL"),
}
BASE_URL = "https://www.dane.gov.co/files/censo2018/proyecciones-de-poblacion/Municipal/"


def normalize_code(codes: pd.Series) -> pd.Series:
    """'5001', 5001, '05001', '5001.0' -> '05001'. Anything that is not a municipality code -> NA."""
    text = codes.astype("string").str.strip().str.replace(r"\.0$", "", regex=True)
    valid = text.str.fullmatch(r"\d{4,5}").fillna(False)
    return text.where(valid).str.zfill(5)


def load_population(cache_dir: Path = Path("cache/dane")) -> pd.DataFrame:
    """Total population per municipality and year (all areas), 1995-2042: columns cod_mpio, year, population."""
    cache_dir.mkdir(parents=True, exist_ok=True)
    frames = []
    for name, spec in POPULATION_FILES.items():
        path = cache_dir / name
        if not path.is_file():
            response = requests.get(BASE_URL + name, headers={"User-Agent": "Mozilla/5.0"}, timeout=300)
            response.raise_for_status()
            path.write_bytes(response.content)
        df = pd.read_excel(path, sheet_name=spec.get("sheet", 0), header=spec["header"], dtype={spec["code"]: str})
        df = df[df["ÁREA GEOGRÁFICA"] == "Total"]
        frames.append(pd.DataFrame({
            "cod_mpio": normalize_code(df[spec["code"]]),
            "year": pd.to_numeric(df[spec["year"]], errors="coerce"),
            "population": pd.to_numeric(df[spec["value"]], errors="coerce"),
        }).dropna())
    population = pd.concat(frames, ignore_index=True)
    population["year"] = population["year"].astype(int)
    return population.drop_duplicates(["cod_mpio", "year"], keep="last")
