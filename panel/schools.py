"""
Schools: each establishment, what it is each year, and what it declared in 2016.

    python -m panel.schools               # download (cached), validate and load the MEN directory and snapshot
    python -m panel.schools --areas       # read the Saber 11 files again for the area and site of each exam

The unit is the establishment (decision 38): one rector, one institutional project, one school fund, one
administration, whatever the number of its buildings. Its sites (sedes) are not modelled as entities; the
site where a student sat the exam stays on the student's record, with its area (urban or rural), because
an establishment can have sites in both.

Sources (datos.gov.co, MEN):
- cfw5-qzt5, directory of establishments, one row per establishment and year, 2015-2025: secretariat
  (the certified entity), municipality, sector, character, calendar, enrolment and number of sites. The
  rector, address, phone and e-mail are not read.
- upkm-vdjb, snapshot of 2016 with what each establishment declared: zone, type, levels, grades, shifts,
  specialties, educational models, languages, ethnic groups, disabilities served, boarding, stratum,
  service provider, owner of the building, indigenous reserve, contracted enrolment. Lists come as one
  field separated by commas; each value goes to its own row (SchoolAttributes, fourth normal form).

Validation before loading (DataQualityFlags, source 'men'):
- a code that is not 12 digits, or a municipality outside Municipalities: error, not loaded;
- the same establishment twice in a year with different values: error, neither row loaded;
- the municipality inside the code (digits 2-6) differs from the municipality of the row: inconsistent,
  loaded with the row's municipality (an establishment keeps the code of the municipality it was created in);
- a secretariat that is not a certified entity: inconsistent, loaded without secretariat;
- character missing: missing;
- enrolment that jumps more than threefold, or falls below a third, from one year to the next (with at
  least 200 students on one side): break, annotated.
- 2023 is broken at the source: every code lost its last six digits (315176012345 became 315176000000)
  and each establishment is repeated once per municipality of its secretariat. The distinct records are
  rebuilt by (code prefix, name, sector, calendar, enrolment, sites) and each one gets back its code when
  exactly one establishment of 2022 or 2024 has the same six-digit prefix and the same name (letters and
  digits only). Rebuilt rows are annotated as inconsistent; the rest are errors, not loaded.

Loads Education_Outcomes.SchoolCalendars, SchoolCharacters, Schools (establishments of the directory are
added; name and municipality from their latest year), SchoolYears, SchoolAttributeKinds,
SchoolAttributeValues and SchoolAttributes. Structural_Violence.SchoolsByMunicipality is a view over
SchoolYears.
"""
import argparse
import csv
import re
import tempfile
import unicodedata
from pathlib import Path

import pandas as pd

from panel.load_db import connect, load

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "cache" / "men"
DIRECTORY, SNAPSHOT = "cfw5-qzt5", "upkm-vdjb"
DIRECTORY_FIELDS = ("a_o, cod_secretaria, cod_dane_municipio, codigo_dane, nombre_establecimiento, cod_sector, sector, "
                    "cod_caracter, caracter, cod_calendario, calendario, total_matricula, cantidad_sedes")
SNAPSHOT_FIELDS = ("a_o, codigomunicipio, codigoestablecimiento, nombreestablecimiento, zona, tipo_establecimiento, prestador_de_servicio, "
                   "propiedad_planta_fisica, resguardo, matricula_contratada, especialidad, internado, "
                   "estrato_socio_economico, idiomas, jornada, niveles, grados, modelos_educativos, discapacidades, "
                   "etnias, modelos")
# snapshot field -> (kind code, description, several values per school)
KINDS = {
    "zona": ("zone", "Zone of its sites as declared (urban, rural or both)", True),
    "tipo_establecimiento": ("establishment_type", "Institucion educativa (all levels) or centro educativo", False),
    "prestador_de_servicio": ("service_provider", "Who provides the service", False),
    "propiedad_planta_fisica": ("building_owner", "Who owns the buildings", False),
    "resguardo": ("indigenous_reserve", "Indigenous reserve where it is, or NO APLICA", False),
    "matricula_contratada": ("contracted_enrolment", "Whether it serves enrolment contracted by the State", False),
    "especialidad": ("specialty", "Specialties of upper secondary (academic, technical branches)", True),
    "internado": ("boarding", "Boarding regimes", True),
    "estrato_socio_economico": ("stratum", "Socio-economic strata it serves", True),
    "idiomas": ("language", "Languages of instruction besides Spanish", True),
    "jornada": ("shift", "School shifts", True),
    "niveles": ("level", "Levels offered", True),
    "grados": ("grade", "Grades offered, as MEN codes them", True),
    "modelos_educativos": ("educational_model", "Educational models (traditional, Escuela Nueva, flexible models)", True),
    "discapacidades": ("disability", "Disabilities it serves", True),
    "etnias": ("ethnic_group", "Ethnic groups it serves", True),
    "modelos": ("exceptional_talent", "Models for exceptional capacities and talents", True),
}


def download():
    """The two datasets, cached in cache/men (a rerun reads the cache)."""
    from panel.socrata import query
    CACHE.mkdir(parents=True, exist_ok=True)
    for name, dataset, fields in (("directory", DIRECTORY, DIRECTORY_FIELDS), ("snapshot_2016", SNAPSHOT, SNAPSHOT_FIELDS)):
        path = CACHE / f"{name}.csv"
        if not path.exists():
            query(dataset, fields, order=":id").to_csv(path, index=False)
    return (pd.read_csv(CACHE / "directory.csv", dtype=str), pd.read_csv(CACHE / "snapshot_2016.csv", dtype=str))


def name_key(s):
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode().upper()
    return re.sub(r"[^A-Z0-9]", "", s)


def code_int(s: pd.Series) -> pd.Series:
    return pd.to_numeric(s.astype(str).str.replace(r"\.0+$", "", regex=True), errors="coerce").astype("Int64")


class Flags:
    def __init__(self):
        self.frames = []

    def add(self, df, mask, column, kind, value, note):
        if not mask.any():
            return
        f = df[mask]
        self.frames.append(pd.DataFrame({
            "source": "men", "source_table": "SchoolYears", "column_name": column,
            "municipality_id": f["municipality_id"].values, "period": f["year"].astype(str).values, "kind": kind,
            "value": value[mask].values if isinstance(value, pd.Series) else value,
            "note": note[mask].values if isinstance(note, pd.Series) else note}))

    def frame(self):
        frames = [f.dropna(axis=1, how="all") for f in self.frames]
        return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()


def rebuild_2023(d: pd.DataFrame, flags: Flags, municipalities: set) -> pd.DataFrame:
    y = d[d["a_o"] == "2023"].copy()
    y["prefix"], y["key"] = y["codigo_dane"].str[:6], y["nombre_establecimiento"].map(name_key)
    record = ["prefix", "key", "cod_sector", "cod_calendario", "total_matricula", "cantidad_sedes", "cod_secretaria"]
    y = y.drop_duplicates(record).copy()
    ref = d[d["a_o"].isin(["2022", "2024"])].copy()
    ref["prefix"], ref["key"] = ref["codigo_dane"].str[:6], ref["nombre_establecimiento"].map(name_key)
    # a name of either year counts: an establishment renamed between 2022 and 2024 is found by both names
    cand = ref.drop_duplicates(["prefix", "key", "codigo_dane"])[["prefix", "key", "codigo_dane", "cod_dane_municipio"]]
    n = cand.groupby(["prefix", "key"])["codigo_dane"].transform("size")
    m = y.drop(columns=["codigo_dane", "cod_dane_municipio"]).merge(cand[n == 1], on=["prefix", "key"], how="left")
    m.loc[m["codigo_dane"].duplicated(keep=False) & m["codigo_dane"].notna(), "codigo_dane"] = None   # one code, two records
    lost = m["codigo_dane"].isna()
    # the unrecovered are annotated where the prefix places them
    m["year"], m["municipality_id"] = 2023, pd.to_numeric(m["prefix"].str[1:], errors="coerce")
    ok = m["municipality_id"].isin(municipalities)
    flags.add(m, lost & ok, "codigo_dane", "error", pd.to_numeric(m["total_matricula"], errors="coerce"),
              "2023: code truncated at the source and the name matches no single establishment of 2022 or 2024; not loaded")
    print(f"  2023: {len(m):,} distinct records, {(~lost).sum():,} rebuilt, {lost.sum():,} not loaded")
    m = m[~lost].copy()
    m["rebuilt"] = True
    return m.drop(columns=["prefix", "key", "year", "municipality_id"])


def directory(d: pd.DataFrame, municipalities: set, entities: set, flags: Flags):
    rows = pd.concat([d[d["a_o"] != "2023"].assign(rebuilt=False), rebuild_2023(d, flags, municipalities)], ignore_index=True)
    df = pd.DataFrame({
        "school_id": code_int(rows["codigo_dane"]),
        "year": rows["a_o"].astype(int),
        "municipality_id": code_int(rows["cod_dane_municipio"]),
        "secretariat_id": code_int(rows["cod_secretaria"]),
        "sector": rows["sector"].str.strip().str.replace(" ", "_"),
        "sector_code": code_int(rows["cod_sector"]),
        "calendar_code": code_int(rows["cod_calendario"]),
        "calendar": rows["calendario"].str.strip(),
        "character_code": code_int(rows["cod_caracter"].where(rows["cod_caracter"].str.strip() != "-")),
        "character": rows["caracter"].where(rows["cod_caracter"].str.strip() != "-").str.strip(),
        "name": rows["nombre_establecimiento"].str.strip().str.slice(0, 255),
        "enrolment": pd.to_numeric(rows["total_matricula"], errors="coerce").astype("Int64"),
        "sites": pd.to_numeric(rows["cantidad_sedes"], errors="coerce").astype("Int64"),
        "rebuilt": rows["rebuilt"].values,
        "code_text": rows["codigo_dane"].astype(str),
    })
    bad = ~df["code_text"].str.fullmatch(r"\d{12}") | ~df["municipality_id"].isin(municipalities)
    known = df["municipality_id"].isin(municipalities)
    flags.add(df, bad & known, "codigo_dane", "error", df["enrolment"].astype(float), "code is not 12 digits; not loaded")
    print(f"  {bad.sum():,} rows with a bad code or an unknown municipality ({(~known).sum():,}); not loaded")
    df = df[~bad].copy()

    facts = ["municipality_id", "secretariat_id", "sector", "calendar_code", "character_code", "enrolment", "sites"]
    same = df.drop_duplicates(["school_id", "year"] + facts)
    twice = same.duplicated(["school_id", "year"], keep=False)
    flags.add(same, twice, "codigo_dane", "error", same["enrolment"].astype(float),
              "the same establishment twice in the year with different values; neither row loaded")
    print(f"  {twice.sum():,} rows of establishments listed twice with different values; not loaded")
    df = same[~twice].copy()

    inside = pd.to_numeric(df["code_text"].str[1:6])
    moved = inside != df["municipality_id"]
    flags.add(df, moved, "municipality_id", "inconsistent", inside.astype(float),
              "the code was created in another municipality (value); loaded with the row's municipality")
    unknown = ~df["secretariat_id"].isin(entities)
    flags.add(df, unknown, "secretariat_id", "inconsistent", df["secretariat_id"].astype(float),
              "secretariat is not a certified entity; loaded without it")
    df.loc[unknown, "secretariat_id"] = pd.NA
    flags.add(df, df["character_code"].isna(), "character_code", "missing", None, "character not reported")
    flags.add(df, df["rebuilt"], "codigo_dane", "inconsistent", df["enrolment"].astype(float),
              "2023: code rebuilt from the name, the source truncated it")

    df = df.sort_values(["school_id", "year"])
    prev = df.groupby("school_id")["enrolment"].shift()
    gap = df["year"] - df.groupby("school_id")["year"].shift()
    e, p = df["enrolment"].astype(float), prev.astype(float)
    jump = (gap == 1) & (pd.concat([e, p], axis=1).max(axis=1) >= 200) & ((e > 3 * p) | (e < p / 3))
    flags.add(df, jump.fillna(False), "enrolment", "break", e, "enrolment " + p.fillna(0).astype(int).astype(str) + " the year before")
    return df


def attributes(s: pd.DataFrame, municipalities: set):
    """Establishments of the 2016 snapshot (some are not in the directory) and their declared values."""
    s = s[s["codigoestablecimiento"].str.fullmatch(r"\d{12}", na=False)].copy()
    s["school_id"], s["municipality_id"] = code_int(s["codigoestablecimiento"]), code_int(s["codigomunicipio"])
    s = s[s["municipality_id"].isin(municipalities)]
    schools = s[["school_id", "nombreestablecimiento", "municipality_id"]].set_axis(["id", "name", "municipality_id"], axis=1)
    schools["name"] = schools["name"].str.strip().str.slice(0, 255)
    rows = []
    for field, (kind, _, _) in KINDS.items():
        v = s[["school_id", field]].dropna()
        v = v.assign(value=v[field].str.split(",")).explode("value")
        v["value"] = v["value"].str.strip().str.rstrip("_").str.strip()
        rows.append(v[v["value"] != ""][["school_id", "value"]].assign(kind_code=kind))
    a = pd.concat(rows, ignore_index=True).drop_duplicates()
    a["value"] = a["value"].str.slice(0, 120)
    values = a[["kind_code", "value"]].drop_duplicates().reset_index(drop=True)
    values["id"] = values.index + 1
    a = a.merge(values, on=["kind_code", "value"]).assign(year=2016)
    print(f"  snapshot 2016: {a['school_id'].nunique():,} establishments, {len(values):,} values, {len(a):,} attributes")
    return schools, values, a[["school_id", "year", "id"]].rename(columns={"id": "value_id"})


def main():
    d, snap = download()
    db = connect()
    cur = db.cursor()
    cur.execute("SELECT id FROM RelationsAndConclusions.Municipalities")
    municipalities = {r[0] for r in cur.fetchall()}
    cur.execute("SELECT id FROM Education_Outcomes.CertifiedEntities")
    entities = {r[0] for r in cur.fetchall()}
    flags = Flags()
    df = directory(d, municipalities, entities, flags)

    calendars = df[["calendar_code", "calendar"]].drop_duplicates("calendar_code").set_axis(["code", "name"], axis=1)
    characters = df.dropna(subset=["character_code"]).sort_values("character")
    characters = characters.drop_duplicates("character_code")[["character_code", "character"]].set_axis(["code", "name"], axis=1)
    latest = df.sort_values("year").drop_duplicates("school_id", keep="last")
    schools = latest[["school_id", "name", "municipality_id"]].rename(columns={"school_id": "id"})
    declared, values, attrs = attributes(snap, municipalities)
    extra = declared[~declared["id"].isin(schools["id"])]
    print(f"  {len(extra):,} establishments only in the 2016 snapshot")
    schools = pd.concat([schools, extra], ignore_index=True)
    kinds = pd.DataFrame([(k, desc, int(multi)) for k, desc, multi in KINDS.values()], columns=["code", "name", "multivalued"])
    f = flags.frame()
    for kind, n in (f.groupby("kind").size().items() if len(f) else []):
        print(f"  MEN directory {kind:<14} {n:>8,}")

    cur.execute("SET FOREIGN_KEY_CHECKS = 0")
    cur.execute("DELETE FROM RelationsAndConclusions.DataQualityFlags WHERE source = 'men' AND source_table = 'SchoolYears'")
    if len(f):
        load(cur, "RelationsAndConclusions.DataQualityFlags", f,
             ["source", "source_table", "column_name", "municipality_id", "period", "kind", "value", "note"])
    for t in ("SchoolAttributes", "SchoolAttributeValues", "SchoolAttributeKinds", "SchoolYears", "SchoolCalendars", "SchoolCharacters"):
        cur.execute(f"TRUNCATE TABLE Education_Outcomes.{t}")
    load(cur, "Education_Outcomes.SchoolCalendars", calendars, ["code", "name"])
    load(cur, "Education_Outcomes.SchoolCharacters", characters, ["code", "name"])
    # establishments of the directory: added, or their name and municipality refreshed from their latest year
    cur.execute("DROP TABLE IF EXISTS Education_Outcomes._schools")
    cur.execute("CREATE TABLE Education_Outcomes._schools (id BIGINT PRIMARY KEY, name VARCHAR(255), municipality_id INT)")
    load(cur, "Education_Outcomes._schools", schools, ["id", "name", "municipality_id"])
    cur.execute("""INSERT INTO Education_Outcomes.Schools (id, name, municipality_id)
                   SELECT id, name, municipality_id FROM Education_Outcomes._schools n
                   ON DUPLICATE KEY UPDATE name = n.name, municipality_id = n.municipality_id""")
    cur.execute("DROP TABLE Education_Outcomes._schools")
    load(cur, "Education_Outcomes.SchoolYears", df,
         ["school_id", "year", "secretariat_id", "sector", "calendar_code", "character_code", "enrolment", "sites"])
    load(cur, "Education_Outcomes.SchoolAttributeKinds", kinds, ["code", "name", "multivalued"])
    load(cur, "Education_Outcomes.SchoolAttributeValues", values, ["id", "kind_code", "value"])
    load(cur, "Education_Outcomes.SchoolAttributes", attrs, ["school_id", "year", "value_id"])
    cur.execute("SET FOREIGN_KEY_CHECKS = 1")
    db.commit()
    print(f"  loaded {len(schools):,} establishments, {len(df):,} establishment-years")
    db.close()


def areas(folder: Path):
    """The area (urban, rural) and the site of the school of each exam, read again from the Saber 11 files
    into Students.area and Students.site_code (files from 2010 on name the site)."""
    from panel.dataicfes import DEFAULT_DATA, files, load_tsv, to_tsv
    folder = folder or DEFAULT_DATA
    db = connect()
    cur = db.cursor()
    cur.execute("DROP TABLE IF EXISTS Education_Outcomes._areas")
    cur.execute("CREATE TABLE Education_Outcomes._areas (student_id VARCHAR(40) PRIMARY KEY, area VARCHAR(40), site_code BIGINT)")
    with tempfile.TemporaryDirectory() as tmp:
        for periodo, path in files(folder):
            tsv = Path(tmp) / "file.tsv"
            encoding = to_tsv(path, tsv)
            header = [str(h).strip().upper() for h in pd.read_csv(tsv, sep="\t", nrows=0, encoding=encoding, quoting=csv.QUOTE_NONE).columns]
            if "COLE_AREA_UBICACION" not in header:
                tsv.unlink()
                continue
            want = [h for h in ("ESTU_CONSECUTIVO", "COLE_AREA_UBICACION", "COLE_COD_DANE_SEDE") if h in header]
            for chunk in pd.read_csv(tsv, sep="\t", dtype=str, encoding=encoding, quoting=csv.QUOTE_NONE, chunksize=500_000,
                                     usecols=lambda c: str(c).strip().upper() in want, on_bad_lines="skip", encoding_errors="replace"):
                chunk.columns = [str(c).strip().upper() for c in chunk.columns]
                site = pd.to_numeric(chunk.get("COLE_COD_DANE_SEDE"), errors="coerce") if "COLE_COD_DANE_SEDE" in chunk else None
                out = pd.DataFrame({"student_id": chunk["ESTU_CONSECUTIVO"].str.strip(),
                                    "area": chunk["COLE_AREA_UBICACION"].str.strip().str.upper().replace({"": None, "U": "URBANO", "R": "RURAL"}),
                                    "site_code": site.where(site < 1e15).astype("Int64") if site is not None else pd.NA})
                load_tsv(cur, "Education_Outcomes._areas", out.dropna(subset=["student_id"]).drop_duplicates("student_id"),
                         ["student_id", "area", "site_code"], tmp)
            tsv.unlink()
            print(f"  {path.name:<40} {periodo}", flush=True)
    cur.execute("INSERT IGNORE INTO Education_Outcomes.SchoolAreas (code) SELECT DISTINCT area FROM Education_Outcomes._areas WHERE area IS NOT NULL")
    cur.execute("""UPDATE Education_Outcomes.Students s JOIN Education_Outcomes._areas a ON a.student_id = s.id
                   SET s.area = a.area, s.site_code = a.site_code""")
    print(f"  Students: {cur.rowcount:,} rows with area or site")
    cur.execute("DROP TABLE Education_Outcomes._areas")
    db.commit()
    db.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--areas", action="store_true", help="read the Saber 11 files again for area and site")
    parser.add_argument("--data", type=Path, default=None)
    a = parser.parse_args()
    areas(a.data) if a.areas else main()
