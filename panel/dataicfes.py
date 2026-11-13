"""
Saber 11 microdata, one row per exam taker, 2000-2022, from the ICFES period files.

    python -m panel.dataicfes [--data "E:/Datos/proyecto/Data/3. Resultados Saber11"]
    python -m panel.dataicfes --refresh 20061,20062     # read some periods' scores and answers again
    python -m panel.dataicfes --derive                  # only the cleaning and the municipal scores

Every run ends with the same cleaning: a test written as -1 is NULL; an exam with every test at 0 was not
taken or was annulled, so its scores are NULL; global_mean is the simple mean of the five tests, the
only global score before 2014-2, when ICFES started publishing its own weighted one (global_score).

Reads every SB11_<year><semester> file (and Data_Icfes_SABER11_2022-1_v2.TXT) and appends to
Education_Outcomes.Students / StudentScores / Schools and Student_Context.StudentHousehold /
StudentPractices, then computes Education_Outcomes.MunicipalScoresMicro (municipal mean and z-score of
mathematics and of the global score, against the national mean and SD of each period). Run it after
`python -m panel.load_db`, which creates the schemas.

ICFES (DataIcfes) has published these files in three generations:
- 2000 to about 2005: separated by "|", Latin-1, nine subject areas, the school's municipality by name;
- up to 2022: separated by "¬", with DANE codes and a longer questionnaire (books, reading, internet use,
  hours of work);
- the exam changed in 2014-2: five tests and a global score.
Column names change between generations, so each field is read from a list of aliases. For the old
exam, natural sciences is the mean of biology, chemistry and physics, social is the mean of history and
geography, critical reading is language. Municipalities given by name are matched within their
department; failing that, through the school's ICFES code as later files place it.

2023-2025 are only on DataIcfes (icfes.gov.co), which answered 403 Forbidden from this machine.
"""
import argparse
import csv
import re
import tempfile
from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd

from panel import dane, governments
from panel.indepaz import key
from panel.load_db import code_int, connect

DEFAULT_DATA = Path("E:/Datos/proyecto/Data/3. Resultados Saber11")
ALIASES = {
    "id": ["ESTU_CONSECUTIVO"],
    "periodo": ["PERIODO"],
    "sex": ["ESTU_GENERO"],
    "birth_year": ["ESTU_NACIMIENTO_ANNO"],
    "birth_date": ["ESTU_FECHANACIMIENTO"],
    "school_dane": ["COLE_COD_DANE_ESTABLECIMIENTO", "COLE_COD_DANE_INSTITUCION"],
    "school_icfes": ["COLE_CODIGO_ICFES", "COLE_COD_ICFES"],
    "school_name": ["COLE_NOMBRE_ESTABLECIMIENTO", "COLE_NOMBRE_SEDE"],
    "sector": ["COLE_NATURALEZA"],
    "area": ["COLE_AREA_UBICACION"],
    "mpio_code": ["COLE_COD_MCPIO_UBICACION"],
    "mpio_name": ["COLE_MCPIO_UBICACION"],
    "depto_name": ["COLE_DEPTO_UBICACION"],
    "pres_code": ["ESTU_COD_MCPIO_PRESENTACION", "ESTU_EXAM_COD_MPIO_PRESENTACIO"],
    "pres_mpio": ["ESTU_MCPIO_PRESENTACION", "ESTU_MPIO_PRESENTACION"],
    "pres_depto": ["ESTU_DEPTO_PRESENTACION", "ESTU_DEPT_PRESENTACION"],
    "math": ["PUNT_MATEMATICAS"],
    "critical_reading": ["PUNT_LECTURA_CRITICA", "PUNT_LENGUAJE"],
    "social_direct": ["PUNT_SOCIALES_CIUDADANAS", "PUNT_CIENCIAS_SOCIALES", "PUNT_C_SOCIALES"],
    "history": ["PUNT_HISTORIA"], "geography": ["PUNT_GEOGRAFIA"],
    "science_direct": ["PUNT_C_NATURALES"],
    "biology": ["PUNT_BIOLOGIA"], "chemistry": ["PUNT_QUIMICA"], "physics": ["PUNT_FISICA"],
    "english": ["PUNT_INGLES", "PUNT_IDIOMA"],
    "global": ["PUNT_GLOBAL"],
    "stratum": ["FAMI_ESTRATOVIVIENDA", "FAMI_ESTRATO_VIVIENDA"],
    "persons": ["FAMI_PERSONASHOGAR", "FAMI_PERSONAS_HOGAR"],
    "rooms": ["FAMI_CUARTOSHOGAR", "FAMI_CUARTOS_HOGAR"],
    "floor": ["FAMI_PISOSHOGAR", "FAMI_PISOS_HOGAR"],
    "internet": ["FAMI_TIENEINTERNET", "FAMI_INTERNET"],
    "computer": ["FAMI_TIENECOMPUTADOR", "FAMI_COMPUTADOR"],
    "car": ["FAMI_TIENEAUTOMOVIL", "FAMI_AUTOMOVIL"],
    "washer": ["FAMI_TIENELAVADORA", "FAMI_LAVADORA"],
    "mother": ["FAMI_EDUCACIONMADRE", "FAMI_EDUCA_MADRE"],
    "father": ["FAMI_EDUCACIONPADRE", "FAMI_EDUCA_PADRE"],
    "ethnic": ["ESTU_ETNIA", "ESTU_TIENEETNIA"],
    "work_hours": ["ESTU_HORASSEMANATRABAJA", "ESTU_HORAS_TRABAJA"],
    "books": ["FAMI_NUMLIBROS"],
    "reading": ["ESTU_DEDICACIONLECTURADIARIA"],
    "internet_hours": ["ESTU_DEDICACIONINTERNET"],
    # only the labelled brackets (2009-2 to 2016-2); 2000-2009 code them 0-9 or 1-7 without a dictionary in hand
    "income": ["FAMI_INGRESOFMILIARMENSUAL"],
}
YES = {"si": 1, "s": 1, "no": 0, "n": 0, "1": 1, "0": 0}     # 2008-2009 answer internet, car and washer with 1 / 0
SECTOR_CODES = {"O": "OFICIAL", "N": "NO OFICIAL"}
AREA_CODES = {"U": "URBANO", "R": "RURAL"}
# Student_Context.IncomeBrackets: family monthly income in legal minimum wages (SMLV)
INCOME_BRACKETS = {"menos de 1 smlv": 1, "entre 1 y menos de 2 smlv": 2, "entre 2 y menos de 3 smlv": 3,
                   "entre 3 y menos de 5 smlv": 4, "entre 5 y menos de 7 smlv": 5, "entre 7 y menos de 10 smlv": 6,
                   "10 o mas smlv": 7}


def files(folder: Path):
    found = []
    for f in sorted(folder.iterdir()):
        m = re.match(r"(?:SB11_|Data_Icfes_SABER11_)(\d{4})[-_]?(\d)", f.name, re.I)
        if f.is_file() and m and f.suffix.lower() in (".txt", ".csv"):
            found.append((int(m.group(1) + m.group(2)), f))
    return found


def to_tsv(path: Path, tmp: Path):
    """The file with its separator turned into a tab, and its encoding."""
    head = path.open("rb").readline()
    if b"\xc2\xac" in head:
        sep, encoding = b"\xc2\xac", "utf-8"
    elif b"\xac" in head:
        sep, encoding = b"\xac", "latin-1"
    else:
        sep = b"|"
        sample = path.open("rb").read(2_000_000)
        try:
            sample[:sample.rfind(b"\n")].decode("utf-8"); encoding = "utf-8"
        except UnicodeDecodeError:
            encoding = "latin-1"
    with path.open("rb") as src, tmp.open("wb") as dst:
        for line in src:
            dst.write(line.replace(b"\t", b" ").replace(sep, b"\t"))
    return encoding


def pick(df: pd.DataFrame, role: str):
    for name in ALIASES[role]:
        if name in df.columns:
            return df[name]
    return pd.Series(pd.NA, index=df.index, dtype="string")      # the file does not have this field


def number(s: pd.Series) -> pd.Series:
    return pd.to_numeric(s.astype(str).str.replace(",", ".", regex=False).str.strip(), errors="coerce")


def yes_no(s: pd.Series, codes=True) -> pd.Series:
    """1 / 0 from si / no. codes=False leaves the bare digits out: what 2 or 3 mean is not documented."""
    table = YES if codes else {k: v for k, v in YES.items() if not k.isdigit()}
    return s.astype(str).map(lambda v: table.get(key(v))).astype("Int64")


def income_bracket(s: pd.Series) -> pd.Series:
    return s.astype(str).map(lambda v: INCOME_BRACKETS.get(key(v))).astype("Int64")


def stratum(s: pd.Series) -> pd.Series:
    def one(v):
        k = key(v)
        if k.startswith("sin estrato"):
            return 0
        m = re.search(r"(\d)", k)
        return int(m.group(1)) if m else None
    return s.astype(str).map(one).astype("Int64")


def municipality_lookup():
    names = dane.municipalities()
    by_name = {(key(d), key(m)): c for d, m, c in zip(names["department"], names["municipality"], names["cod_mpio"])}
    # ICFES spellings of the past that differ from DANE's
    for (d, m), c in list(by_name.items()):
        by_name.setdefault((d, m.replace("san jose de ", "")), c)
    by_name[("bogota", "bogota d c")] = by_name[("bogota d c", "bogota d c")]
    by_name[("bogota d c", "bogota")] = by_name[("bogota d c", "bogota d c")]
    by_name[("bogota", "bogota")] = by_name[("bogota d c", "bogota d c")]
    by_name[("antioquia", "antioquia")] = by_name[("antioquia", "santafe de antioquia")]   # its old name
    only_mpio = {}
    for (d, m), c in by_name.items():
        only_mpio.setdefault(m, set()).add(c)
    return by_name, {m: next(iter(c)) for m, c in only_mpio.items() if len(c) == 1}


def resolve_municipality(df, by_name, unique_name, icfes_map):
    code = dane.normalize_code(pick(df, "mpio_code"))
    names = [(key(d), key(m)) for d, m in zip(pick(df, "depto_name").fillna(""), pick(df, "mpio_name").fillna(""))]
    by_school = pick(df, "school_icfes").astype(str).str.strip().map(icfes_map)
    pres = dane.normalize_code(pick(df, "pres_code"))
    pres_names = [(key(d), key(m)) for d, m in zip(pick(df, "pres_depto").fillna(""), pick(df, "pres_mpio").fillna(""))]
    out = []
    for c, n, s, p, pn in zip(code, names, by_school, pres, pres_names):
        if isinstance(c, str):
            out.append(c)
        elif n in by_name:
            out.append(by_name[n])
        elif n[1] in unique_name:
            out.append(unique_name[n[1]])
        elif isinstance(s, str):
            out.append(s)
        elif isinstance(p, str):
            out.append(p)
        elif pn in by_name:
            out.append(by_name[pn])
        else:
            out.append(None)
    return code_int(pd.Series(out, index=df.index))


def load_tsv(cur, table, df, columns, tmpdir):
    path = Path(tmpdir) / (table.replace(".", "__") + ".tsv")
    out = df[columns].copy()
    for c in out.columns:          # a backslash in a text would be read as an escape by the server
        if out[c].dtype == object or str(out[c].dtype) == "string":
            out[c] = out[c].map(lambda v: v.replace("\\", "/") if isinstance(v, str) else v)
    # \N must reach the server as written: it is how LOAD DATA reads NULL. No escaping, no quoting.
    out.to_csv(path, sep="\t", index=False, header=False, na_rep="\\N", lineterminator="\n",
               quoting=csv.QUOTE_NONE, quotechar="\x07")
    schema, name = table.split(".")
    cur.execute(f"LOAD DATA LOCAL INFILE '{path.as_posix()}' IGNORE INTO TABLE `{schema}`.`{name}` CHARACTER SET utf8mb4 "
                f"FIELDS TERMINATED BY '\\t' LINES TERMINATED BY '\\n' ({', '.join('`' + c + '`' for c in columns)})")


def scores_frame(chunk, ids):
    mean = lambda *cols: pd.concat([number(pick(chunk, c)) for c in cols], axis=1).mean(axis=1)
    social = number(pick(chunk, "social_direct")).fillna(mean("history", "geography"))
    science = number(pick(chunk, "science_direct")).fillna(mean("biology", "chemistry", "physics"))
    scores = pd.DataFrame({
        "student_id": ids, "math": number(pick(chunk, "math")),
        "critical_reading": number(pick(chunk, "critical_reading")), "social_citizenship": social,
        "natural_sciences": science, "english": number(pick(chunk, "english")), "global_score": number(pick(chunk, "global")),
    })
    return scores


def household_frames(chunk, ids):
    household = pd.DataFrame({
        "student_id": ids, "stratum": stratum(pick(chunk, "stratum")),
        "persons_in_household": pick(chunk, "persons").str.slice(0, 40), "rooms": pick(chunk, "rooms").str.slice(0, 40),
        "floor_type": pick(chunk, "floor").str.slice(0, 80), "has_internet": yes_no(pick(chunk, "internet")),
        "has_computer": yes_no(pick(chunk, "computer"), codes=False), "has_car": yes_no(pick(chunk, "car")),
        "has_washing_machine": yes_no(pick(chunk, "washer")),
        "mother_education": pick(chunk, "mother").str.slice(0, 100), "father_education": pick(chunk, "father").str.slice(0, 100),
        "ethnic_group": pick(chunk, "ethnic").str.slice(0, 80), "work_hours_per_week": pick(chunk, "work_hours").str.slice(0, 40),
        "income_bracket_id": income_bracket(pick(chunk, "income")),
    })
    practices = pd.DataFrame({
        "student_id": ids, "books_at_home": pick(chunk, "books").str.slice(0, 40),
        "reading_for_pleasure": pick(chunk, "reading").str.slice(0, 40),
        "internet_hours_per_day": pick(chunk, "internet_hours").str.slice(0, 40),
    })
    return household, practices


CLEAN_TESTS = ("math", "critical_reading", "social_citizenship", "natural_sciences", "english")


def clean_scores(cur):
    """The cleaning every load ends with. It only touches what the files themselves mark as no score."""
    t = "Education_Outcomes.StudentScores"
    # -1 is how 2005-2007 write a test that was not scored
    cur.execute(f"UPDATE {t} SET " + ", ".join(f"{c} = IF({c} < 0, NULL, {c})" for c in CLEAN_TESTS)
                + " WHERE " + " OR ".join(f"{c} < 0" for c in CLEAN_TESTS))
    print(f"  tests marked -1 set to NULL: {cur.rowcount:,} students")
    # every test at 0 is an exam not taken or annulled, not a score
    cur.execute(f"UPDATE {t} SET " + ", ".join(f"{c} = NULL" for c in CLEAN_TESTS + ("global_score",))
                + " WHERE " + " AND ".join(f"COALESCE({c}, 0) = 0" for c in CLEAN_TESTS)
                + " AND (" + " OR ".join(f"{c} IS NOT NULL" for c in CLEAN_TESTS + ("global_score",)) + ")")
    print(f"  exams with every test at 0 set to NULL: {cur.rowcount:,} students")
    cur.execute(f"UPDATE {t} SET global_mean = ROUND((" + " + ".join(CLEAN_TESTS) + ") / 5, 2)")
    print("  simple global mean written for every student with the five tests")


def municipal_scores(cur):
    cur.execute("TRUNCATE TABLE Education_Outcomes.MunicipalScoresMicro")
    cur.execute("""
        INSERT INTO Education_Outcomes.MunicipalScoresMicro
        SELECT s.municipality_id, s.exam_period_id, COUNT(*), AVG(sc.math),
               (AVG(sc.math) - n.m_math) / NULLIF(n.sd_math, 0), AVG(sc.g), (AVG(sc.g) - n.m_global) / NULLIF(n.sd_global, 0)
        FROM Education_Outcomes.Students s
        JOIN (SELECT student_id, math, COALESCE(global_score, global_mean) g FROM Education_Outcomes.StudentScores) sc
          ON sc.student_id = s.id
        JOIN (SELECT s2.exam_period_id, AVG(x.math) m_math, STDDEV_POP(x.math) sd_math,
                     AVG(COALESCE(x.global_score, x.global_mean)) m_global,
                     STDDEV_POP(COALESCE(x.global_score, x.global_mean)) sd_global
              FROM Education_Outcomes.Students s2 JOIN Education_Outcomes.StudentScores x ON x.student_id = s2.id
              GROUP BY s2.exam_period_id) n ON n.exam_period_id = s.exam_period_id
        WHERE s.municipality_id IS NOT NULL
        GROUP BY s.municipality_id, s.exam_period_id""")


def derive(cur):
    clean_scores(cur)
    print("  municipal scores from the microdata")
    municipal_scores(cur)
    cur.execute("SET FOREIGN_KEY_CHECKS = 1")
    for t in ("Education_Outcomes.Students", "Education_Outcomes.StudentScores", "Education_Outcomes.Schools",
              "Student_Context.StudentHousehold", "Student_Context.StudentPractices", "Education_Outcomes.MunicipalScoresMicro"):
        cur.execute(f"SELECT COUNT(*) FROM {t}")
        print(f"  {t:<45} {cur.fetchone()[0]:>12,}")


def refresh(cur, folder, periods, tmpdir):
    """Reads again the scores and the household answers of some periods, for the students already loaded:
    for when a field was missed because its column had a name the aliases did not know."""
    staging = {"Education_Outcomes.StudentScores": "Education_Outcomes._refresh_scores",
               "Student_Context.StudentHousehold": "Student_Context._refresh_household"}
    for target, tmp in staging.items():
        cur.execute(f"DROP TABLE IF EXISTS {tmp}")
        cur.execute(f"CREATE TABLE {tmp} LIKE {target}")
    columns = {}
    for periodo, path in files(folder):
        if periodo not in periods:
            continue
        tsv = Path(tmpdir) / "file.tsv"
        encoding = to_tsv(path, tsv)
        header = pd.read_csv(tsv, sep="\t", nrows=0, encoding=encoding, quoting=csv.QUOTE_NONE).columns
        known_names = {n for names in ALIASES.values() for n in names}
        wanted = [h for h in header if str(h).strip().upper() in known_names]
        for chunk in pd.read_csv(tsv, sep="\t", dtype=str, usecols=wanted, encoding=encoding, quoting=csv.QUOTE_NONE,
                                 chunksize=200_000, on_bad_lines="skip", encoding_errors="replace"):
            chunk.columns = [str(c).strip().upper() for c in chunk.columns]
            chunk = chunk.dropna(subset=["ESTU_CONSECUTIVO"])
            ids = chunk["ESTU_CONSECUTIVO"].str.strip()
            scores = scores_frame(chunk, ids)
            household, _ = household_frames(chunk, ids)
            for target, frame in (("Education_Outcomes.StudentScores", scores), ("Student_Context.StudentHousehold", household)):
                columns[target] = list(frame.columns)
                load_tsv(cur, staging[target], frame, list(frame.columns), tmpdir)
        tsv.unlink()
        print(f"  {path.name:<40} {periodo}  read again", flush=True)
    for target, tmp in staging.items():
        cols = [c for c in columns.get(target, []) if c != "student_id"]
        if cols:
            cur.execute(f"UPDATE {target} t JOIN {tmp} r ON r.student_id = t.student_id SET "
                        + ", ".join(f"t.{c} = r.{c}" for c in cols))
            print(f"  {target}: {cur.rowcount:,} rows changed")
        cur.execute(f"DROP TABLE {tmp}")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--data", default=DEFAULT_DATA, type=Path)
    parser.add_argument("--resume", action="store_true", help="keep the periods already loaded and continue with the rest")
    parser.add_argument("--refresh", help="comma-separated periods, as in the file names, whose scores and household "
                                          "answers are read again; then the cleaning and the municipal scores")
    parser.add_argument("--derive", action="store_true", help="only the cleaning and the municipal scores")
    args = parser.parse_args()
    db = connect()
    cur = db.cursor()
    cur.execute("SET FOREIGN_KEY_CHECKS = 0")
    cur.execute("SET UNIQUE_CHECKS = 0")
    if args.refresh or args.derive:
        if args.refresh:
            with tempfile.TemporaryDirectory(dir=Path("cache")) as tmpdir:
                refresh(cur, args.data, {int(p) for p in args.refresh.split(",")}, tmpdir)
        derive(cur)
        db.close()
        return
    done = set()
    if args.resume:
        cur.execute("SELECT DISTINCT exam_period_id FROM Education_Outcomes.Students")
        done = {r[0] for r in cur.fetchall()}
        cur.execute("TRUNCATE TABLE Education_Outcomes.MunicipalScoresMicro")
    else:
        for t in ("Student_Context.StudentPractices", "Student_Context.StudentHousehold", "Education_Outcomes.StudentScores",
                  "Education_Outcomes.Students", "Education_Outcomes.Schools", "Education_Outcomes.MunicipalScoresMicro"):
            cur.execute(f"TRUNCATE TABLE {t}")
    cur.execute("SELECT id FROM RelationsAndConclusions.Municipalities")
    municipalities = {r[0] for r in cur.fetchall()}
    by_name, unique_name = municipality_lookup()
    gov_ids = {k: n + 1 for n, (k, *_rest) in enumerate(governments.TERMS)}

    todo = files(args.data)
    # newest first: later files place each ICFES school code in a municipality, which the oldest need
    todo.sort(key=lambda x: -x[0])
    icfes_map, schools = {}, {}
    with tempfile.TemporaryDirectory(dir=Path("cache")) as tmpdir:
        for periodo, path in todo:
            # inside the files the second semester of 2019-2022 is 20194 ... 20224; the file names say 20192
            same_exam = lambda p: (p // 10, "B" if p % 10 == 1 else "A")
            if same_exam(periodo) in {same_exam(p) for p in done}:
                print(f"  {path.name:<40} {periodo}  already loaded", flush=True)
                continue
            tsv = Path(tmpdir) / "file.tsv"
            encoding = to_tsv(path, tsv)
            header = pd.read_csv(tsv, sep="\t", nrows=0, encoding=encoding, quoting=csv.QUOTE_NONE).columns
            known_names = {n for names in ALIASES.values() for n in names}
            wanted = [h for h in header if str(h).strip().upper() in known_names]     # 2019-1 writes them in lowercase
            total = matched = 0
            for chunk in pd.read_csv(tsv, sep="\t", dtype=str, usecols=wanted, encoding=encoding, quoting=csv.QUOTE_NONE,
                                     chunksize=200_000, on_bad_lines="skip", encoding_errors="replace"):
                chunk.columns = [str(c).strip().upper() for c in chunk.columns]
                chunk = chunk.dropna(subset=["ESTU_CONSECUTIVO"])
                per = pick(chunk, "periodo").fillna(str(periodo)).str.strip()
                per = pd.to_numeric(per, errors="coerce").fillna(periodo).astype(int)
                mun = resolve_municipality(chunk, by_name, unique_name, icfes_map)
                mun = mun.where(mun.isin(municipalities))
                # learn where each ICFES school code is
                codes = pick(chunk, "school_icfes").astype(str).str.strip()
                for sc, m in zip(codes, mun):
                    if pd.notna(m) and sc not in icfes_map and sc not in ("nan", ""):
                        icfes_map[sc] = str(int(m)).zfill(5)
                birth = pick(chunk, "birth_year")
                if birth.isna().all():
                    birth = pick(chunk, "birth_date").astype(str).str.extract(r"(\d{4})")[0]
                birth = pd.to_numeric(birth, errors="coerce")
                school = pd.to_numeric(pick(chunk, "school_dane"), errors="coerce")
                school = school.where(school < 1e15).astype("Int64")
                students = pd.DataFrame({
                    "id": chunk["ESTU_CONSECUTIVO"].str.strip(),
                    "exam_period_id": per,
                    "school_id": school,
                    "municipality_id": mun,
                    "sex_id": pick(chunk, "sex").astype(str).str.strip().str.upper().str[:1].where(lambda s: s.isin(["F", "M"]), "U"),
                    "birth_year": birth.where(birth.between(1900, 2015)).astype("Int64"),
                })
                scores = scores_frame(chunk, students["id"])
                household, practices = household_frames(chunk, students["id"])
                for sid, name, m, sector, area in zip(school, pick(chunk, "school_name"), mun, pick(chunk, "sector"), pick(chunk, "area")):
                    if pd.notna(sid) and sid not in schools:
                        sector = str(sector).strip().upper() if pd.notna(sector) else None
                        area = str(area).strip().upper() if pd.notna(area) else None
                        # some periods write the one-letter code instead of the word
                        schools[sid] = (str(name)[:255] if pd.notna(name) else None, m,
                                        SECTOR_CODES.get(sector, sector), AREA_CODES.get(area, area))
                for p in students["exam_period_id"].unique():
                    year = int(str(p)[:4])
                    cur.execute("INSERT IGNORE INTO Education_Outcomes.ExamPeriods VALUES (%s, %s, %s, %s, %s)",
                                (int(p), year, "B" if str(p).endswith("1") else "A", "pre_2014" if p < 20142 else "since_2014_2",
                                 gov_ids.get(governments.government(date(year, 9, 1)))))
                load_tsv(cur, "Education_Outcomes.Students", students,
                         ["id", "exam_period_id", "school_id", "municipality_id", "sex_id", "birth_year"], tmpdir)
                load_tsv(cur, "Education_Outcomes.StudentScores", scores,
                         ["student_id", "math", "critical_reading", "social_citizenship", "natural_sciences", "english", "global_score"], tmpdir)
                load_tsv(cur, "Student_Context.StudentHousehold", household, list(household.columns), tmpdir)
                if practices[["books_at_home", "reading_for_pleasure", "internet_hours_per_day"]].notna().any().any():
                    load_tsv(cur, "Student_Context.StudentPractices", practices, list(practices.columns), tmpdir)
                total += len(students)
                matched += int(students["municipality_id"].notna().sum())
            print(f"  {path.name:<40} {periodo}  {total:>9,} students, municipality found for {matched / max(total, 1):.1%}", flush=True)
            tsv.unlink()

        sch = pd.DataFrame([(k, *v) for k, v in schools.items()], columns=["id", "name", "municipality_id", "sector", "area"])
        load_tsv(cur, "Education_Outcomes.Schools", sch, ["id", "name", "municipality_id", "sector", "area"], tmpdir)

    derive(cur)
    db.close()


if __name__ == "__main__":
    main()
