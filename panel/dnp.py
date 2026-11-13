"""
DNP TerriData: every indicator DNP publishes per municipality and department, all years.

    python -m panel.dnp            # download (if not cached), transform, validate, load

TerriData is DNP's territorial statistics system. Its bulk file
(terridata.dnp.gov.co/assets/docs/txt/dimensiones/TerriData.txt.zip, 190 MB zipped, 3.3 GB of text) is one
row per entity, indicator, year and month, with the dimension, subcategory, source and unit. It gathers what
DNP and other entities publish: demography, education, health, housing, armed conflict, public finance,
municipal performance (MDM), fiscal performance, economy (municipal value added), environment, poverty
(DANE's departmental and city Gini), labour, justice, royalties, peace and victims, and the classifications
of each municipality (rurality category, development environment, DNP typology, Law 617 category, PDET).

Transform:
- municipalities (DANE codes, checked against DANE's list) and department totals (codes ending in 000);
- numbers are written with a dot for thousands and a comma for decimals;
- the indicator is identified by its nine-digit code; its name, unit and dimension are kept as published.
DNP gives no data for 21 territories: the 19 non-municipalized areas of the Amazon, San Andres and Nuevo
Belen de Bajira.

Validate. Every row goes first to a staging table and is checked there; only what passes reaches the model.
- a key (place, indicator, year, month) given twice with different values: neither is loaded (inconsistent);
  exact repetitions are loaded once;
- a negative count (people, events, hectares, number of ...) or a negative percentage that is not a change:
  not loaded (error);
- a percentage above 100: loaded and annotated (inconsistent); some indicators legitimately exceed 100;
- a value more than ten times, or less than a tenth of, the year before: loaded and annotated (break).
The findings go to RelationsAndConclusions.DataQualityFlags with source DNP.

Load, in the schema Territorial_Context:
- TerriDataIndicators: one row per indicator (code, dimension, subcategory, name, unit);
- TerriDataSources: the source entities;
- TerriDataCategories: the categories text indicators take, each label once per indicator;
- MunicipalIndicators and DepartmentalIndicators: place, indicator, year, month, numeric value or category,
  source.
Writes output/panel/terridata_inventory.csv: per dimension and indicator, years, municipalities and rows.
"""
import csv
import zipfile
from pathlib import Path

import pandas as pd
import requests

from panel import dane
from panel.load_db import connect, load

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "cache" / "dnp"
OUT = ROOT / "output" / "panel"
URL = "https://terridata.dnp.gov.co/assets/docs/txt/dimensiones/TerriData.txt.zip"
DICTIONARY_URL = "https://terridata.dnp.gov.co/assets/docs/Diccionario%20de%20variables%20Terridata.xlsx"
COLUMNS = ["dept_code", "dept", "entity_code", "entity", "dimension", "subcategory", "indicator", "indicator_code",
           "value", "value_text", "year", "month", "source", "unit"]
STAGED = ["level", "place", "indicator_code", "year", "month", "value_num", "text", "source_id"]
COUNT_UNITS = ("Personas", "Hombres", "Mujeres", "Hectáreas", "Eventos", "Número", "Numero", "Casos", "Víctimas",
               "Kilómetros cuadrados", "Hogares", "Viviendas", "Estudiantes", "Predios")
CHANGE_WORDS = ("Variaci", "Crecimiento", "Cambio", "Diferencia", "Brecha")
NULL = "\\N"


def download():
    CACHE.mkdir(parents=True, exist_ok=True)
    for url, name in ((URL, "TerriData.txt.zip"), (DICTIONARY_URL, "Diccionario de variables Terridata.xlsx")):
        path = CACHE / name
        if not path.exists():
            with requests.get(url, stream=True, timeout=600, headers={"User-Agent": "Mozilla/5.0"}) as r:
                r.raise_for_status()
                with path.open("wb") as f:
                    for block in r.iter_content(1 << 20):
                        f.write(block)
    return CACHE / "TerriData.txt.zip"


def number(s: pd.Series) -> pd.Series:
    return pd.to_numeric(s.str.replace(".", "", regex=False).str.replace(",", ".", regex=False).str.strip(), errors="coerce")


def transform(zip_path: Path):
    municipalities = set(dane.municipalities()["cod_mpio"])
    departments = {c[:2] for c in municipalities}
    facts = OUT / "terridata_staged.tsv"
    OUT.mkdir(parents=True, exist_ok=True)
    indicators, sources, inventory = {}, {}, []
    rows = kept = 0
    with zipfile.ZipFile(zip_path) as z, z.open("TerriData.txt") as f, facts.open("w", encoding="utf-8", newline="") as out:
        reader = pd.read_csv(f, sep="|", dtype=str, header=0, names=COLUMNS, quoting=csv.QUOTE_NONE,
                             encoding="utf-8", chunksize=1_000_000, keep_default_na=False)
        for chunk in reader:
            rows += len(chunk)
            code = chunk["entity_code"].str.strip().str.zfill(5)
            department = code.str.endswith("000") & code.str[:2].isin(departments)
            chunk = chunk[code.isin(municipalities) | department].copy()
            chunk["level"] = department[chunk.index].map({True: "D", False: "M"})
            chunk["place"] = code[chunk.index].astype(int)
            chunk.loc[chunk["level"] == "D", "place"] //= 1000          # 5000 -> department 5
            for c in ("indicator_code", "dimension", "subcategory", "indicator", "unit", "source"):
                chunk[c] = chunk[c].str.strip()
            for k, d, s, n, u in chunk[["indicator_code", "dimension", "subcategory", "indicator", "unit"]] \
                    .drop_duplicates("indicator_code").itertuples(index=False):
                indicators.setdefault(k, (d, s, n, u))
            for s in chunk["source"].unique():
                sources.setdefault(s, len(sources) + 1)
            chunk["value_num"] = number(chunk["value"])
            text = chunk["value_text"].str.strip().str.replace(r"[\t\r\n\\]", " ", regex=True).str.slice(0, 255)
            chunk["text"] = text.where((text != "") & (text.str.upper() != "NA"))
            chunk = chunk[chunk["value_num"].notna() | chunk["text"].notna()]
            chunk["source_id"] = chunk["source"].map(sources)
            chunk["year"] = pd.to_numeric(chunk["year"], errors="coerce").astype("Int64")
            chunk["month"] = pd.to_numeric(chunk["month"], errors="coerce").fillna(0).astype(int)
            chunk = chunk[chunk["year"].notna()]
            mun = chunk[chunk["level"] == "M"]
            inventory.append(mun.groupby("indicator_code").agg(
                rows=("place", "size"), municipalities=("place", "nunique"),
                first_year=("year", "min"), last_year=("year", "max")).reset_index())
            chunk[STAGED].to_csv(out, sep="\t", header=False, index=False, na_rep=NULL, lineterminator="\n",
                                 quoting=csv.QUOTE_NONE, quotechar="\x07")
            kept += len(chunk)
            print(f"  {rows:>12,} rows read, {kept:>12,} staged", flush=True)
    inv = pd.concat(inventory).groupby("indicator_code").agg(
        rows=("rows", "sum"), municipalities=("municipalities", "max"), first_year=("first_year", "min"),
        last_year=("last_year", "max")).reset_index()
    cat = pd.DataFrame([(k, *v) for k, v in indicators.items()], columns=["code", "dimension", "subcategory", "name", "unit"])
    inv = cat.merge(inv, left_on="code", right_on="indicator_code", how="left").drop(columns="indicator_code")
    inv.to_csv(OUT / "terridata_inventory.csv", index=False, encoding="utf-8")
    src = pd.DataFrame([(i, s) for s, i in sources.items()], columns=["id", "name"])
    return cat, src, facts


FLAG = ("INSERT INTO RelationsAndConclusions.DataQualityFlags "
        "(source, source_table, column_name, municipality_id, period, kind, value, note) ")


def validate(cur):
    """Checks the staged rows: writes the findings and marks the rows that must not be loaded."""
    st = "Territorial_Context._staging"
    cur.execute("DELETE FROM RelationsAndConclusions.DataQualityFlags WHERE source = 'DNP'")
    # the same key twice with different values: neither is loaded
    cur.execute("DROP TEMPORARY TABLE IF EXISTS Territorial_Context._dup")
    cur.execute(f"""CREATE TEMPORARY TABLE Territorial_Context._dup AS
                    SELECT level, place, indicator_code, year, month, MIN(value) lo, MAX(value) hi,
                           COUNT(DISTINCT CONCAT(COALESCE(value, ''), '|', COALESCE(value_text, ''))) versions
                    FROM {st} GROUP BY level, place, indicator_code, year, month HAVING COUNT(*) > 1""")
    cur.execute(FLAG + """SELECT 'DNP', 'MunicipalIndicators', indicator_code, place, year, 'inconsistent', hi,
                          CONCAT('given twice with different values (', COALESCE(lo, 'text'), ' and ', COALESCE(hi, 'text'),
                                 '); not loaded')
                          FROM Territorial_Context._dup WHERE versions > 1 AND level = 'M'""")
    cur.execute(f"""UPDATE {st} s JOIN Territorial_Context._dup d USING (level, place, indicator_code, year, month)
                    SET s.reject = 1 WHERE d.versions > 1""")
    counts = " OR ".join(f"i.unit LIKE '{u}%'" for u in COUNT_UNITS)
    change = " OR ".join(f"i.name LIKE '%{w}%'" for w in CHANGE_WORDS)
    rules = ((f"s.value < 0 AND ({counts})", "negative count; not loaded"),
             (f"s.value < 0 AND i.unit LIKE 'Porcentaje%' AND NOT ({change})", "negative percentage; not loaded"))
    for where, note in rules:
        cur.execute(FLAG + f"""SELECT 'DNP', 'MunicipalIndicators', s.indicator_code, s.place, s.year, 'error', s.value, '{note}'
                               FROM {st} s JOIN Territorial_Context.TerriDataIndicators i ON i.code = s.indicator_code
                               WHERE s.level = 'M' AND s.reject = 0 AND {where}""")
        cur.execute(f"""UPDATE {st} s JOIN Territorial_Context.TerriDataIndicators i ON i.code = s.indicator_code
                        SET s.reject = 1 WHERE {where}""")
    cur.execute(FLAG + f"""SELECT 'DNP', 'MunicipalIndicators', s.indicator_code, s.place, s.year, 'inconsistent', s.value,
                           'percentage above 100'
                           FROM {st} s JOIN Territorial_Context.TerriDataIndicators i ON i.code = s.indicator_code
                           WHERE s.level = 'M' AND s.reject = 0 AND s.value > 100 AND i.unit LIKE 'Porcentaje%'
                             AND i.unit NOT LIKE '%multiplicado%'""")
    # yearly series that jump tenfold from one year to the next
    cur.execute(FLAG + f"""SELECT 'DNP', 'MunicipalIndicators', indicator_code, place, year, 'break', value,
                           CONCAT(ROUND(value / prev, 1), ' times the year before (', prev, ')')
                           FROM (SELECT s.place, s.indicator_code, s.year, s.value,
                                        LAG(s.value) OVER (PARTITION BY s.place, s.indicator_code ORDER BY s.year) prev,
                                        LAG(s.year) OVER (PARTITION BY s.place, s.indicator_code ORDER BY s.year) prev_year
                                 FROM {st} s WHERE s.level = 'M' AND s.month IN (0, 12) AND s.reject = 0
                                   AND s.value IS NOT NULL) t
                           WHERE prev_year = year - 1 AND prev > 0 AND value > 0 AND (value / prev > 10 OR value / prev < 0.1)""")
    cur.execute("SELECT kind, COUNT(*) FROM RelationsAndConclusions.DataQualityFlags WHERE source = 'DNP' GROUP BY kind")
    for kind, n in cur.fetchall():
        print(f"  DNP {kind:<14} {n:>9,}")


def load_db(cat, src, facts):
    db = connect()
    cur = db.cursor()
    cur.execute("SET FOREIGN_KEY_CHECKS = 0")
    for t in ("MunicipalIndicators", "DepartmentalIndicators", "TerriDataCategories", "TerriDataIndicators", "TerriDataSources"):
        cur.execute(f"TRUNCATE TABLE Territorial_Context.{t}")
    for c in ("dimension", "subcategory", "name", "unit"):
        cat[c] = cat[c].str.slice(0, 255)
    load(cur, "Territorial_Context.TerriDataIndicators", cat, ["code", "dimension", "subcategory", "name", "unit"])
    src["name"] = src["name"].str.slice(0, 255)
    load(cur, "Territorial_Context.TerriDataSources", src, ["id", "name"])
    cur.execute("DROP TABLE IF EXISTS Territorial_Context._staging")
    cur.execute("""CREATE TABLE Territorial_Context._staging (
                       level CHAR(1), place INT, indicator_code CHAR(9), year SMALLINT, month TINYINT,
                       value DOUBLE, value_text VARCHAR(255), source_id INT, reject TINYINT NOT NULL DEFAULT 0,
                       KEY (level, place, indicator_code, year, month))""")
    tab, newline, null = "\\t", "\\n", "\\\\N"
    cur.execute(f"LOAD DATA LOCAL INFILE '{facts.as_posix()}' INTO TABLE Territorial_Context._staging "
                f"CHARACTER SET utf8mb4 FIELDS TERMINATED BY '{tab}' ESCAPED BY '' LINES TERMINATED BY '{newline}' "
                f"(level, place, indicator_code, year, month, @v, @t, source_id) "
                f"SET value = NULLIF(@v, '{null}'), value_text = NULLIF(@t, '{null}')")
    cur.execute("SELECT level, COUNT(*) FROM Territorial_Context._staging GROUP BY level")
    print("  staged:", {k: f"{n:,}" for k, n in cur.fetchall()})
    validate(cur)
    cur.execute("""INSERT INTO Territorial_Context.TerriDataCategories (indicator_code, label)
                   SELECT DISTINCT indicator_code, value_text FROM Territorial_Context._staging
                   WHERE value_text IS NOT NULL AND reject = 0""")
    for level, table in (("M", "MunicipalIndicators"), ("D", "DepartmentalIndicators")):
        cur.execute(f"""INSERT IGNORE INTO Territorial_Context.{table}
                        SELECT s.place, s.indicator_code, s.year, s.month, s.value, c.id, s.source_id
                        FROM Territorial_Context._staging s
                        LEFT JOIN Territorial_Context.TerriDataCategories c
                               ON c.indicator_code = s.indicator_code AND c.label = s.value_text
                        WHERE s.level = '{level}' AND s.reject = 0""")
        cur.execute(f"SELECT COUNT(*) FROM Territorial_Context.{table}")
        print(f"  Territorial_Context.{table:<24} {cur.fetchone()[0]:>12,} rows")
    cur.execute("DROP TABLE Territorial_Context._staging")
    cur.execute("SET FOREIGN_KEY_CHECKS = 1")
    db.commit()
    db.close()


def main():
    cat, src, facts = transform(download())
    load_db(cat, src, facts)


if __name__ == "__main__":
    main()
