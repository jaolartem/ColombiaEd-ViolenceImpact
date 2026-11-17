"""
INDEPAZ massacre list, 2020 onwards.

INDEPAZ (Instituto de Estudios para el Desarrollo y la Paz) keeps a list of massacres built from press
and regional reports, published as one HTML table per year on
https://indepaz.org.co/informe-de-masacres-en-colombia-durante-el-2020-2021/ (robots.txt allows it).
Each row: date, department, municipality, number of victims.

The tables do not share a column order and some have no header row, so each column is recognised by
its content. A table that repeats part of a year already listed (the page keeps an older snapshot of
2026) is dropped: for each year the longest table wins.

Municipalities are written by name, so they are matched to the DANE code within their department:
accents, case and punctuation are ignored, a few known aliases are applied, and what is left is matched
to the closest name in the same department only if it is very close. What does not match is reported,
never guessed.
"""
import difflib
import io
import re
import unicodedata
from datetime import date
from pathlib import Path

import pandas as pd
import requests

from panel import dane

URL = "https://indepaz.org.co/informe-de-masacres-en-colombia-durante-el-2020-2021/"
DATE = re.compile(r"^\s*(\d{1,2})/(\d{1,2})/(\d{4}|\d{2})\s*$")      # 2024 and 2025 write 12/01/25
MONTHS = {m: i + 1 for i, m in enumerate(["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto",
                                          "septiembre", "octubre", "noviembre", "diciembre"])}

# INDEPAZ name -> DANE name, both normalised with `key`. Each one checked against the DANE list.
ALIASES = {
    ("bogota d c", "bogota"): "bogota d c",
    ("bogota d c", "bogota sumapaz"): "bogota d c",
    ("bolivar", "cartagena"): "cartagena de indias",
    ("amazonas", "puerto alegria"): "puerto alegria anm",
    ("cauca", "piendamo"): "piendamo tunia",
    ("narino", "andes sotomayor"): "los andes",
    ("narino", "colon genova"): "colon",
    ("putumayo", "leguizamo"): "puerto leguizamo",
    ("antioquia", "caucacia"): "caucasia",
    ("caqueta", "montanita"): "la montanita",
    ("guaviare", "retorno"): "el retorno",
    ("norte de santander", "guamalito"): "el carmen",       # Guamalito is a corregimiento of El Carmen
    ("norte de santander", "cucuta"): "san jose de cucuta",
    ("narino", "tumaco"): "san andres de tumaco",
    ("valle del cauca", "buga"): "guadalajara de buga",
    ("narino", "magui payan"): "magui",
    ("magdalena", "cienega"): "cienaga",
}
DEPARTMENT_ALIASES = {
    "bogota": "bogota d c",
    "bogota dc": "bogota d c",
    "norte santander": "norte de santander",
    "valle": "valle del cauca",
    "guajira": "la guajira",
    "san andres": "archipielago de san andres providencia y santa catalina",
}


def key(text) -> str:
    text = unicodedata.normalize("NFKD", str(text)).encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", text)).strip()


def fetch(cache_dir: Path = Path("cache/indepaz"), refresh: bool = False) -> str:
    cache_dir.mkdir(parents=True, exist_ok=True)
    path = cache_dir / f"masacres-{date.today():%Y%m%d}.html"
    if refresh or not path.is_file():
        response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0 (research: ColombiaEd-ViolenceImpact)"}, timeout=120)
        response.raise_for_status()
        path.write_text(response.text, encoding="utf-8")
    return path.read_text(encoding="utf-8")


def _columns(table: pd.DataFrame, departments: set) -> dict:
    """Which column is the date, the victims, the department and the municipality, by content."""
    cells = table.astype(str)
    share = lambda col, test: cells[col].map(test).mean()
    is_date = lambda v: bool(DATE.match(v))
    is_count = lambda v: v.strip().isdigit()
    roles = {"date": max(cells.columns, key=lambda c: share(c, is_date))}
    rest = [c for c in cells.columns if c != roles["date"]]
    numeric = sorted(rest, key=lambda c: share(c, is_count), reverse=True)[:2]
    # of the two numeric columns, the row number is the one that counts 1, 2, 3 ...
    sequence = lambda c: pd.to_numeric(cells[c], errors="coerce").diff().eq(1).mean()
    roles["number"], roles["victims"] = sorted(numeric, key=sequence, reverse=True)
    text = [c for c in rest if c not in numeric]
    roles["department"] = max(text, key=lambda c: share(c, lambda v: key(v) in departments))
    roles["municipality"] = next(c for c in text if c != roles["department"])
    return roles


def parse(html: str) -> pd.DataFrame:
    departments = {key(d) for d in dane.municipalities()["department"]} | set(DEPARTMENT_ALIASES)
    rows = []
    for table in pd.read_html(io.StringIO(html)):
        table = table.dropna(how="all")
        if table.shape[1] != 5 or not table.astype(str).apply(lambda c: c.str.match(DATE.pattern)).any().any():
            continue
        roles = _columns(table, departments)
        t = pd.DataFrame({role: table[col].astype(str) for role, col in roles.items()})
        parts = t["date"].str.extract(DATE.pattern)
        full = parts.notna().all(axis=1)
        years = parts[2].dropna().map(lambda y: int(y) + 2000 if len(y) == 2 else int(y))
        table_year = int(years.mode()[0])
        days, precision = [], []
        for text, (d, m, y) in zip(t["date"], parts.values):
            if isinstance(y, str):
                days.append(date(int(y) + 2000 if len(y) == 2 else int(y), int(m), int(d))); precision.append("day")
            elif key(text) in MONTHS:       # one 2022 row only says "Enero"
                days.append(date(table_year, MONTHS[key(text)], 15)); precision.append("month")
            else:
                days.append(None); precision.append(None)
        t["day"], t["date_precision"] = days, precision
        t = t.dropna(subset=["day"])
        t["victims"] = pd.to_numeric(t["victims"], errors="coerce")     # "Por determinar" -> unknown
        t["year"] = [d.year for d in t["day"]]
        rows.append(t)
    found = pd.concat([t.assign(table=i) for i, t in enumerate(rows)], ignore_index=True)
    sizes = found.groupby(["year", "table"]).size().reset_index(name="n")
    keep = sizes.sort_values("n").drop_duplicates("year", keep="last")
    found = found.merge(keep[["year", "table"]], on=["year", "table"])
    return (found[["day", "date_precision", "year", "department", "municipality", "victims"]]
            .sort_values("day").reset_index(drop=True))


def match_municipalities(df: pd.DataFrame):
    names = dane.municipalities()
    names["dk"], names["mk"] = names["department"].map(key), names["municipality"].map(key)
    lookup = {(d, m): c for d, m, c in zip(names["dk"], names["mk"], names["cod_mpio"])}
    by_department = names.groupby("dk")["mk"].apply(list).to_dict()

    departments = set(by_department)
    codes, how = [], []
    for department, municipality in zip(df["department"], df["municipality"]):
        dk = DEPARTMENT_ALIASES.get(key(department), key(department))
        if dk not in departments:          # some rows have the two columns swapped
            swapped = DEPARTMENT_ALIASES.get(key(municipality), key(municipality))
            if swapped in departments:
                dk, municipality = swapped, department
        mk = ALIASES.get((dk, key(municipality)), key(municipality))
        if (dk, mk) in lookup:
            codes.append(lookup[(dk, mk)]); how.append("exact"); continue
        first = key(re.split(r",| y ", str(municipality))[0])   # "Copacabana y Bello": the first place is kept
        first = ALIASES.get((dk, first), first)
        if first != mk and (dk, first) in lookup:
            codes.append(lookup[(dk, first)]); how.append("first_of_several"); continue
        close = difflib.get_close_matches(mk, by_department.get(dk, []), n=1, cutoff=0.88)
        if close:
            codes.append(lookup[(dk, close[0])]); how.append("close"); continue
        codes.append(None); how.append("unmatched")
    out = df.assign(cod_mpio=codes, match=how)
    return out, out[out["match"] == "unmatched"][["day", "department", "municipality"]]


def load(refresh: bool = False):
    events, unmatched = match_municipalities(parse(fetch(refresh=refresh)))
    return events, unmatched
