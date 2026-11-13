"""
Loads everything into MariaDB/MySQL, in the model of Tables_and_relations.sql.

    python -m panel.load_db [--out output/panel] [--mysql PATH_TO_mysql]

Run the extraction modules first (build, longterm, events, identity, police, census, door, access,
student_context): they write the CSV files this reads. The loader

1. recreates the seven schemas from Tables_and_relations.sql (with the mysql client, so the script runs
   as written);
2. loads places, population, sources, cases, events and links, census, education and access, with
   LOAD DATA LOCAL INFILE;
3. computes in Python and loads: rates per government and per phase over exact days, Saber 11 z-scores,
   and the indices (panel/indices.py);
4. checks: rows per table, and facts whose municipality is not a DANE municipality.

Connection: environment variables DB_HOST, DB_USER, DB_PASS (default localhost, root, empty). Running it
again rebuilds the same database.
"""
import argparse
import glob
import os
import shutil
import subprocess
from datetime import date, timedelta
from pathlib import Path

import mysql.connector
import numpy as np
import pandas as pd

from panel import dane, events as events_module, governments, indices, longterm, socrata, sources

ROOT = Path(__file__).resolve().parent.parent
TMP = ROOT / "cache" / "load"
INDICATOR_IDS = {"homicide": 1, "suicide": 2, "violence_children": 3, "domestic_violence": 4,
                 "partner_violence": 5, "sexual_violence": 6, "sociopolitical_homicide": 7}
SOURCE_IDS = {"medicina_legal": 1, "police": 2, "cnmh": 3, "indepaz": 4, "dane": 5, "icfes": 6, "men": 7,
              "minsalud": 8, "icetex": 9}
INDEPAZ_DATASET = "indepaz-masacres"
DEPRIVATIONS = {   # census.py column (Spanish, normalised) -> model column
    "deprivation_analfabetismo": "dep_illiteracy",
    "deprivation_bajo_logro_educativo": "dep_low_educational_attainment",
    "deprivation_barreras_a_servicios_para_cuidado_de_la_primera_infancia": "dep_early_childhood_care_barriers",
    "deprivation_barreras_de_acceso_a_servicios_de_salud": "dep_health_access_barriers",
    "deprivation_tasa_de_dependencia": "dep_dependency_rate",
    "deprivation_hacinamiento_critico": "dep_critical_overcrowding",
    "deprivation_inadecuada_eliminacion_de_excretas": "dep_inadequate_excreta_disposal",
    "deprivation_inasistencia_escolar": "dep_school_non_attendance",
    "deprivation_material_inadecuado_de_paredes_exteriores": "dep_inadequate_wall_material",
    "deprivation_material_inadecuado_de_pisos": "dep_inadequate_floor_material",
    "deprivation_rezago_escolar": "dep_school_lag",
    "deprivation_sin_acceso_a_fuente_de_agua_mejorada": "dep_no_improved_water",
    "deprivation_sin_aseguramiento_en_salud": "dep_no_health_insurance",
    "deprivation_trabajo_infantil": "dep_child_labour",
    "deprivation_trabajo_informal": "dep_informal_work",
}


# ---------------------------------------------------------------------------------------- plumbing

def mysql_client(explicit: str = None) -> str:
    candidates = [explicit, shutil.which("mysql"), shutil.which("mariadb")]
    candidates += sorted(glob.glob("F:/laragon/bin/mysql/*/bin/mysql.exe")) + sorted(glob.glob("C:/laragon/bin/mysql/*/bin/mysql.exe"))
    for c in candidates:
        if c and Path(c).exists():
            return c
    raise SystemExit("No mysql client found: pass --mysql")


def connect():
    return mysql.connector.connect(host=os.environ.get("DB_HOST", "localhost"), user=os.environ.get("DB_USER", "root"),
                                   password=os.environ.get("DB_PASS", ""), allow_local_infile=True, autocommit=True)


def load(cursor, table: str, df: pd.DataFrame, columns: list):
    """LOAD DATA LOCAL INFILE of `columns` of `df` into `table` ("Schema.Table")."""
    TMP.mkdir(parents=True, exist_ok=True)
    path = TMP / (table.replace(".", "__") + ".tsv")
    out = df[columns].copy()
    for c in out.columns:
        if out[c].dtype == object:
            out[c] = out[c].map(lambda v: v if not isinstance(v, str) else v.replace("\t", " ").replace("\n", " ").replace("\r", " "))
        elif out[c].dtype == bool:
            out[c] = out[c].astype(int)
    out.to_csv(path, sep="\t", index=False, header=False, na_rep="\\N", lineterminator="\n")
    schema, name = table.split(".")
    cols = ", ".join(f"`{c}`" for c in columns)
    cursor.execute(f"LOAD DATA LOCAL INFILE '{path.as_posix()}' INTO TABLE `{schema}`.`{name}` "
                   f"CHARACTER SET utf8mb4 FIELDS TERMINATED BY '\\t' LINES TERMINATED BY '\\n' ({cols})")
    cursor.execute(f"SELECT COUNT(*) FROM `{schema}`.`{name}`")
    n = cursor.fetchone()[0]
    print(f"  {table:<50} {n:>10,} rows")
    return n


def known(df: pd.DataFrame, municipalities: set, column="municipality_id", label="") -> pd.DataFrame:
    """Keep rows whose municipality is a DANE municipality; report the rest."""
    ok = df[column].isin(municipalities)
    if (~ok).any():
        print(f"    {label}: {int((~ok).sum()):,} rows with a code that is not a DANE municipality, left out")
    return df[ok]


def read(out: Path, name: str, **kw) -> pd.DataFrame:
    return pd.read_csv(out / name, dtype={"cod_mpio": str, "periodo": str}, **kw)


def code_int(series):
    return pd.to_numeric(series, errors="coerce").astype("Int64")


# ---------------------------------------------------------------------------------------- periods

def assign(days: pd.Series, periods) -> pd.Series:
    """The period code each day falls in (None outside every period)."""
    starts = np.array([np.datetime64(s) for _, s, _ in periods])
    ends = np.array([np.datetime64(e) for _, _, e in periods])
    d = pd.to_datetime(days).values.astype("datetime64[D]")
    i = np.searchsorted(starts, d, side="right") - 1
    valid = (i >= 0) & (d < ends[np.clip(i, 0, len(ends) - 1)])
    keys = np.array([k for k, _, _ in periods], dtype=object)
    return pd.Series(np.where(valid, keys[np.clip(i, 0, len(keys) - 1)], None), index=days.index)


def period_rates(records: pd.DataFrame, population: pd.DataFrame, windows: dict) -> pd.DataFrame:
    """records: measure, cod_mpio, day, value. windows: measure -> (start, end). Rates per 100,000 person-years."""
    terms = [(k, s, e) for k, _, s, e in governments.TERMS]
    frames = []
    for kind, periods in (("government", terms), ("phase", governments.PHASES)):
        exposures = {}
        for measure, d in records.groupby("measure"):
            start, end = windows[measure]
            d = d[(pd.to_datetime(d["day"]) >= pd.Timestamp(start)) & (pd.to_datetime(d["day"]) < pd.Timestamp(end))]
            d = d.assign(period=assign(d["day"], periods)).dropna(subset=["period"])
            cases = d.groupby(["cod_mpio", "period"], as_index=False)["value"].sum()
            if (start, end) not in exposures:
                exposures[(start, end)] = governments.person_years(population, periods, start, end)
            frame = exposures[(start, end)].merge(cases, on=["cod_mpio", "period"], how="left")
            frame["value"] = frame["value"].fillna(0)
            frames.append(frame.assign(measure=measure, period_kind=kind))
    out = pd.concat(frames, ignore_index=True)
    out["rate_per_100k"] = (out["value"] / out["person_years"] * 1e5).where(out["person_years"] > 0)
    return out.rename(columns={"period": "period_code", "value": "cases"})


# ---------------------------------------------------------------------------------------- main

def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", default="output/panel", type=Path)
    parser.add_argument("--mysql", default=None)
    args = parser.parse_args()
    out = args.out

    print("schemas")
    with open(ROOT / "Tables_and_relations.sql", "rb") as sql:
        subprocess.run([mysql_client(args.mysql), "-h", os.environ.get("DB_HOST", "localhost"),
                        "-u", os.environ.get("DB_USER", "root")] +
                       ([f"-p{os.environ['DB_PASS']}"] if os.environ.get("DB_PASS") else []),
                       stdin=sql, check=True)
    db = connect()
    cur = db.cursor()
    cur.execute("SET FOREIGN_KEY_CHECKS = 0")

    # ------------------------------------------------------------------ places and population
    print("places and population")
    names = dane.municipalities()
    names["id"] = code_int(names["cod_mpio"])
    departments = names.assign(id=names["cod_mpio"].str[:2].astype(int)).drop_duplicates("id")[["id", "department"]]
    load(cur, "RelationsAndConclusions.Departments", departments.rename(columns={"department": "name"}), ["id", "name"])
    names["department_id"] = names["cod_mpio"].str[:2].astype(int)
    load(cur, "RelationsAndConclusions.Municipalities", names.rename(columns={"municipality": "name"}),
         ["id", "name", "department_id"])
    municipalities = set(names["id"].astype(int))

    population = read(out, "population.csv")
    p = population.assign(municipality_id=code_int(population["cod_mpio"]))
    load(cur, "RelationsAndConclusions.Population", known(p, municipalities, label="population"),
         ["municipality_id", "year", "population"])
    by_sex_age = read(out, "population_sex_age.csv")
    p = by_sex_age.assign(municipality_id=code_int(by_sex_age["cod_mpio"]), sex_id=by_sex_age["sex"],
                          age_to=by_sex_age["age_to"].astype("Int64"))
    load(cur, "RelationsAndConclusions.PopulationBySexAge", known(p, municipalities, label="population by sex and age"),
         ["municipality_id", "year", "sex_id", "age_from", "age_to", "population"])

    # ------------------------------------------------------------------ datasets
    print("datasets")
    rows = []
    for indicator, parts in sources.VIOLENCE.items():
        for dataset, _, preliminary in parts:
            rows.append(("medicina_legal", dataset, f"Medicina Legal, {indicator}", int(preliminary)))
    rows += [("police", d, f"Police, {i}", 0) for i, d in {**{k: v for k, v in longterm.POLICE.items()},
                                                            "massacres": events_module.POLICE_MASSACRES}.items()]
    rows += [("cnmh", d, f"CNMH SIEVCAC, {label}", 0) for d, label in events_module.CNMH.values()]
    rows += [("indepaz", INDEPAZ_DATASET, "INDEPAZ massacre list (web page)", 0)]
    rows += [("dane", f, "DANE population projections", 0) for f in list(dane.POPULATION_FILES) + [
             "DCD-area-sexo-edad-proypoblacion-Mun-1995-2004.xlsx", "DCD-area-sexo-edad-proypoblacion-Mun-2005-2017_VP.xlsx",
             "PPED-AreaSexoEdadMun-2018-2042_VP.xlsx"]]
    rows += [("dane", f, "DANE census 2018", 0) for f in ("anexo-censal-pobreza-municipal-2018.xlsx", "CNPV-2018-NBI.xlsx",
                                                          "VIVIENDAS_Cuadros_CNPV_2018.XLSX")]
    rows += [("icfes", "kgxf-xxbe", "Saber 11 results 2010-2022", 0), ("icfes", "u37r-hjmu", "Saber Pro results 2018-2022", 0),
             ("men", "nudc-7mev", "MEN enrolment and dropout by municipality", 0),
             ("men", "cfw5-qzt5", "MEN directory of schools", 0), ("men", "5wck-szir", "MEN higher-education enrolment", 0),
             ("men", "6sqn-9wh9", "MEN Generacion E beneficiaries", 0), ("minsalud", "c36g-9fc2", "REPS health providers and sites", 0),
             ("icetex", "f673-3gn8", "ICETEX new beneficiaries", 0), ("icetex", "nvcf-b8a3", "ICETEX renewals", 0)]
    datasets = pd.DataFrame(rows, columns=["source", "dataset", "description", "preliminary"]).drop_duplicates("dataset")
    datasets["id"] = range(1, len(datasets) + 1)
    datasets["source_id"] = datasets["source"].map(SOURCE_IDS)
    dataset_id = dict(zip(datasets["dataset"], datasets["id"]))

    # ------------------------------------------------------------------ Medicina Legal cases
    print("violence cases")
    cases = read(out, "violence_cases.csv")
    ds = {(i, prelim): d for i, parts in sources.VIOLENCE.items() for d, _, prelim in parts}
    cases["dataset_id"] = [dataset_id[ds[(i, bool(p))]] for i, p in zip(cases["indicator"], cases["preliminary"])]
    c = cases.assign(municipality_id=code_int(cases["cod_mpio"]), indicator_id=cases["indicator"].map(INDICATOR_IDS),
                     sex_id=cases["sex"])
    load(cur, "RelationsAndConclusions.ViolenceCases", known(c, municipalities, label="Medicina Legal"),
         ["municipality_id", "year", "indicator_id", "sex_id", "dataset_id", "cases"])

    police = read(out, "police_daily.csv")
    c = police.assign(municipality_id=code_int(police["cod_mpio"]), indicator_id=police["indicator"].map(INDICATOR_IDS),
                      sex_id=police["sex"])
    load(cur, "RelationsAndConclusions.PoliceDailyCases", known(c, municipalities, label="Police daily"),
         ["municipality_id", "day", "indicator_id", "sex_id", "cases"])

    # ------------------------------------------------------------------ events and links
    print("events")
    ev = read(out, "events.csv")
    ev["dataset"] = np.where(ev["source"] == "cnmh", ev["modality"].map(lambda m: events_module.CNMH.get(m, (None,))[0]),
                             np.where(ev["source"] == "indepaz", INDEPAZ_DATASET, events_module.POLICE_MASSACRES))
    ev["day"] = pd.to_datetime(ev["day"], errors="coerce")           # CNMH cases with year 0 have no date
    ev["cutoff"] = pd.to_datetime(ev["cutoff"], errors="coerce")
    coverage = ev.groupby("dataset").agg(coverage_from=("day", "min"), cutoff=("cutoff", "max"), last=("day", "max"))
    datasets = datasets.merge(coverage, left_on="dataset", right_index=True, how="left")
    datasets["coverage_to"] = datasets["cutoff"].fillna(datasets["last"]).dt.date
    datasets["coverage_from"] = datasets["coverage_from"].dt.date
    ev["day"] = ev["day"].dt.date
    ev["cutoff"] = ev["cutoff"].dt.date
    load(cur, "RelationsAndConclusions.SourceDatasets", datasets,
         ["id", "source_id", "dataset", "description", "coverage_from", "coverage_to", "preliminary"])

    perpetrators = pd.DataFrame({"name": sorted(ev["perpetrator"].dropna().astype(str).str.strip().unique())})
    perpetrators["id"] = range(1, len(perpetrators) + 1)
    load(cur, "Physical_violence.Perpetrators", perpetrators, ["id", "name"])
    clusters = read(out, "massacre_clusters.csv")[["source_event_id", "cluster"]]
    ev = ev.merge(clusters, on="source_event_id", how="left")
    ev["id"] = range(1, len(ev) + 1)
    ev["dataset_id"] = ev["dataset"].map(dataset_id)
    ev["municipality_id"] = code_int(ev["cod_mpio"])
    unknown = ev["municipality_id"].notna() & ~ev["municipality_id"].isin(municipalities)
    if unknown.any():
        print(f"    events: {int(unknown.sum()):,} with a code that is not a DANE municipality: municipality left empty")
    ev.loc[unknown, "municipality_id"] = pd.NA
    ev["perpetrator_id"] = ev["perpetrator"].astype(str).str.strip().map(dict(zip(perpetrators["name"], perpetrators["id"])))
    ev = ev.rename(columns={"modality": "modality_code", "cluster": "massacre_cluster"})
    load(cur, "Physical_violence.ViolenceEvents", ev,
         ["id", "dataset_id", "source_event_id", "modality_code", "day", "date_precision", "municipality_id", "victims",
          "perpetrator_id", "massacre_cluster"])        # group and simultaneous acts: panel.event_details
    links = read(out, "event_links.csv")
    ids = dict(zip(ev["source_event_id"], ev["id"]))
    links = links.assign(event_a_id=links["event_a"].map(ids), event_b_id=links["event_b"].map(ids))
    load(cur, "Physical_violence.EventLinks", links.dropna(subset=["event_a_id", "event_b_id"]), ["event_a_id", "event_b_id", "day_gap"])

    # ------------------------------------------------------------------ identity
    print("identity")
    identity = read(out, "identity_cases.csv")
    groups = identity[["kind", "group_name"]].drop_duplicates().reset_index(drop=True)
    groups["group_name"] = groups["group_name"].str.slice(0, 200)
    groups = groups.drop_duplicates()
    groups["id"] = range(1, len(groups) + 1)
    load(cur, "Cultural_violence.IdentityGroups", groups.rename(columns={"group_name": "name"}), ["id", "kind", "name"])
    identity["group_name"] = identity["group_name"].str.slice(0, 200)
    identity = identity.merge(groups, on=["kind", "group_name"])
    i = identity.assign(municipality_id=code_int(identity["cod_mpio"]), indicator_id=identity["indicator"].map(INDICATOR_IDS),
                        identity_group_id=identity["id"], preliminary=identity["preliminary"].astype(int))
    i = i.groupby(["municipality_id", "year", "indicator_id", "identity_group_id", "preliminary"], as_index=False)["cases"].sum()
    load(cur, "Cultural_violence.IdentityViolenceCases", known(i, municipalities, label="identity"),
         ["municipality_id", "year", "indicator_id", "identity_group_id", "preliminary", "cases"])

    # ------------------------------------------------------------------ structural
    print("structural")
    census = read(out, "census_2018.csv").rename(columns=DEPRIVATIONS)
    census["municipality_id"] = code_int(census["cod_mpio"])
    census_cols = ["municipality_id", "ipm"] + list(DEPRIVATIONS.values()) + [
        "nbi", "nbi_misery", "nbi_housing", "nbi_services", "nbi_overcrowding", "nbi_school_non_attendance",
        "nbi_economic_dependency", "dwellings_occupied", "share_earth_floor", "share_electricity", "share_water",
        "share_sewer", "share_gas", "share_garbage", "share_internet"] + [f"share_stratum_{k}" for k in range(1, 7)] + [
        "share_no_electricity_service", "share_stratum_1_2"]
    census["dwellings_occupied"] = census["dwellings_occupied"].round().astype("Int64")
    load(cur, "Structural_Violence.Census2018Municipal", known(census, municipalities, label="census"), census_cols)
    schools = read(out, "schools.csv")
    s = schools.assign(municipality_id=code_int(schools["cod_mpio"]), sector=schools["sector"].fillna("SIN INFORMACION"))
    s = s.groupby(["municipality_id", "year", "sector"], as_index=False)[["establishments", "sites", "enrolment"]].sum()
    load(cur, "Structural_Violence.SchoolsByMunicipality", known(s, municipalities, label="schools"),
         ["municipality_id", "year", "sector", "establishments", "sites", "enrolment"])
    health = read(out, "health_sites.csv")
    h = health.assign(municipality_id=code_int(health["cod_mpio"]),
                      provider_class=health["provider_class"].fillna("Sin informacion").str.slice(0, 120),
                      legal_nature=health["legal_nature"].fillna("Sin informacion").str.slice(0, 60))
    h = h.groupby(["municipality_id", "provider_class", "legal_nature"], as_index=False)["sites"].sum()
    load(cur, "Structural_Violence.HealthSites", known(h, municipalities, label="health sites"),
         ["municipality_id", "provider_class", "legal_nature", "sites"])

    # ------------------------------------------------------------------ education
    print("education")
    saber = read(out, "saber_11.csv")
    student_context = read(out, "student_context.csv")
    periods = pd.DataFrame({"periodo": sorted(set(saber["periodo"]) | set(student_context["periodo"]))})
    periods["id"] = periods["periodo"].astype(int)
    periods["year"] = periods["periodo"].str[:4].astype(int)
    periods["calendar"] = np.where(periods["periodo"].str[-1] == "1", "B", "A")
    periods["scale"] = np.where(periods["id"] < 20142, "pre_2014", "since_2014_2")
    gov_ids = {k: n + 1 for n, (k, *_rest) in enumerate(governments.TERMS)}
    periods["government_id"] = [gov_ids.get(governments.government(date(y, 9, 1))) for y in periods["year"]]
    periods["government_id"] = periods["government_id"].astype("Int64")
    load(cur, "Education_Outcomes.ExamPeriods", periods, ["id", "year", "calendar", "scale", "government_id"])

    z = longterm.saber_z(saber, socrata.app_token())
    national = z.drop_duplicates("periodo").set_index("periodo")
    sc = saber.assign(municipality_id=code_int(saber["cod_mpio"]), exam_period_id=saber["periodo"].astype(int), sex_id=saber["sex"])
    for col in ("punt_matematicas", "punt_global"):
        mean = pd.to_numeric(sc["periodo"].map(national[f"{col}_mean"]), errors="coerce")
        sd = pd.to_numeric(sc["periodo"].map(national[f"{col}_sd"]), errors="coerce")
        sc[f"{col}_z"] = (sc[col] - mean) / sd
    sc = sc.rename(columns={"punt_global": "mean_global", "punt_matematicas": "mean_math", "punt_lectura_critica": "mean_critical_reading",
                            "punt_sociales_ciudadanas": "mean_social", "punt_c_naturales": "mean_science", "punt_ingles": "mean_english",
                            "punt_matematicas_z": "math_z", "punt_global_z": "global_z"})
    load(cur, "Education_Outcomes.MunicipalScores", known(sc, municipalities, label="Saber 11"),
         ["municipality_id", "exam_period_id", "sex_id", "students", "mean_global", "mean_math", "mean_critical_reading",
          "mean_social", "mean_science", "mean_english", "math_z", "global_z"])

    students = saber.groupby(["cod_mpio", "periodo"], as_index=False)["students"].sum()
    ctx = student_context.merge(students, on=["cod_mpio", "periodo"], how="left")
    ctx = ctx.assign(municipality_id=code_int(ctx["cod_mpio"]), exam_period_id=ctx["periodo"].astype(int),
                     students=ctx["students"].fillna(0).astype(int))
    load(cur, "Student_Context.MunicipalStudentContext", known(ctx, municipalities, label="student context"),
         ["municipality_id", "exam_period_id", "students", "share_internet", "share_computer", "share_car",
          "share_washing_machine", "share_stratum_1_2", "share_mother_higher_ed", "share_mother_primary_or_less"])

    men = read(out, "men_education.csv")
    load(cur, "Education_Outcomes.EnrolmentAndDropout", known(men.assign(municipality_id=code_int(men["cod_mpio"])), municipalities, label="MEN"),
         ["municipality_id", "year", "net_enrolment", "net_enrolment_upper_secondary", "dropout", "dropout_upper_secondary",
          "approval", "repetition"])

    pro = read(out, "saber_pro.csv")
    pro = pro.assign(municipality_id=code_int(pro["cod_mpio"]), sex_id=pro["sex"].map({"F": "F", "M": "M"}).fillna("U"),
                     periodo=pro["periodo"].astype(int))
    pro = pro.rename(columns={"mod_razona_cuantitat_punt": "quantitative_reasoning", "mod_lectura_critica_punt": "critical_reading",
                              "mod_competen_ciudada_punt": "citizenship", "mod_ingles_punt": "english",
                              "mod_comuni_escrita_punt": "written_communication"})
    scores = ["quantitative_reasoning", "critical_reading", "citizenship", "english", "written_communication"]
    for col in scores:
        pro[col + "_w"] = pro[col] * pro["students"]
    pro = pro.groupby(["municipality_id", "periodo", "year", "sex_id"], as_index=False)[["students"] + [c + "_w" for c in scores]].sum(min_count=1)
    for col in scores:
        pro[col] = pro[col + "_w"] / pro["students"]
    load(cur, "Education_Outcomes.SaberProByMunicipality", known(pro, municipalities, label="Saber Pro"),
         ["municipality_id", "periodo", "year", "sex_id", "students"] + scores)

    hed = read(out, "higher_ed_enrolment.csv")
    hed = hed.assign(municipality_id=code_int(hed["cod_mpio"]))
    hed = hed.groupby(["municipality_id", "year", "semester", "sector_id", "level_id"], as_index=False)["enrolled"].sum()
    load(cur, "Education_Outcomes.HigherEdEnrolment", known(hed, municipalities, label="higher education"),
         ["municipality_id", "year", "semester", "sector_id", "level_id", "enrolled"])
    ge = read(out, "generacion_e.csv")
    ge = ge.assign(municipality_id=code_int(ge["cod_mpio"])).groupby(["municipality_id", "cutoff"], as_index=False)["beneficiaries"].sum()
    load(cur, "Education_Outcomes.GeneracionE", known(ge, municipalities, label="Generacion E"), ["municipality_id", "cutoff", "beneficiaries"])
    ic = read(out, "icetex.csv")
    ic = ic.assign(sex=ic["sex"].fillna("Sin informacion").str.slice(0, 20), level=ic["level"].fillna("Sin informacion").str.slice(0, 80))
    ic = ic.dropna(subset=["department_id", "year"]).groupby(["department_id", "year", "sex", "level", "kind"], as_index=False)["beneficiaries"].sum()
    ic = ic[ic["department_id"].isin(set(departments["id"]))]
    ic["sex"] = ic["sex"].map({"Femenino": "F", "Masculino": "M", "Intersexual": "I"}).fillna("U")   # the key of Sexes
    load(cur, "Education_Outcomes.IcetexCredits", ic, ["department_id", "year", "sex", "level", "kind", "beneficiaries"])

    # ------------------------------------------------------------------ rates by government and phase
    print("rates by government and phase")
    records = [police.assign(measure="police_" + police["indicator"], value=police["cases"])[["measure", "cod_mpio", "day", "value"]]]
    ev_dated = ev.dropna(subset=["day", "cod_mpio"])
    for source, d in ev_dated.groupby("source"):
        for modality, dm in d.groupby("modality_code"):
            label = f"{source}_{events_module.CNMH[modality][1].replace(' ', '_') if source == 'cnmh' else 'massacre'}"
            records.append(dm.assign(measure=label + "_events", value=1)[["measure", "cod_mpio", "day", "value"]])
            records.append(dm.assign(measure=label + "_victims", value=dm["victims"].fillna(0))[["measure", "cod_mpio", "day", "value"]])
    records = pd.concat(records, ignore_index=True)
    police_end = pd.to_datetime(police["day"]).max().date() + timedelta(days=1)
    cnmh_end = pd.to_datetime(ev[ev["source"] == "cnmh"]["cutoff"]).max().date() + timedelta(days=1)
    windows = {}
    for m in records["measure"].unique():
        if m.startswith("police_massacre") or m.startswith("police_") and "massacre" in m:
            windows[m] = (date(2022, 1, 1), police_end)
        elif m.startswith("police_"):
            windows[m] = (longterm.POLICE_START, police_end)
        elif m.startswith("cnmh_"):
            windows[m] = (governments.TERMS[0][2], cnmh_end)
        elif m.startswith("indepaz_"):
            windows[m] = (date(2020, 1, 1), date.today())
    rates = period_rates(records, population, windows)
    rates["municipality_id"] = code_int(rates["cod_mpio"])
    load(cur, "RelationsAndConclusions.PeriodRates", known(rates, municipalities, label="period rates"),
         ["municipality_id", "period_kind", "period_code", "measure", "cases", "person_years", "rate_per_100k"])

    # ------------------------------------------------------------------ indices
    print("indices")
    phys = indices.physical(cases, population)
    cult = indices.cultural(read(out, "identity_cases.csv"), population)
    gend = indices.gender(cases, population, by_sex_age)
    stru = indices.structural(read(out, "census_2018.csv"), health, population)
    fin = indices.final(phys, cult, gend, stru)
    for df in (phys, cult, gend, stru, fin):
        df["municipality_id"] = code_int(df["cod_mpio"])
    load(cur, "Physical_violence.PhysicalViolenceIndex", known(phys, municipalities, label="physical index"),
         ["municipality_id", "year", "subin_homicide", "subin_suicide", "subin_violence_children", "subin_domestic_violence",
          "physical_violence_index"])
    load(cur, "Cultural_violence.CulturalViolenceIndex", known(cult, municipalities, label="cultural index"),
         ["municipality_id", "year", "subin_ethnic_homicide", "subin_vulnerable_group_homicide", "subin_sociopolitical_homicide",
          "cultural_violence_index"])
    load(cur, "GENDER_VIOLENCE.GenderViolenceIndex", known(gend, municipalities, label="gender index"),
         ["municipality_id", "year", "subin_partner_violence", "subin_sexual_violence", "subin_female_homicide",
          "subin_female_suicide", "gender_violence_index"])
    load(cur, "Structural_Violence.StructuralViolenceIndex", known(stru, municipalities, label="structural index"),
         ["municipality_id", "subin_multidimensional_poverty", "subin_unsatisfied_needs", "subin_no_internet",
          "subin_health_access", "structural_violence_index"])
    fin = fin.rename(columns={"physical_violence_index": "physical_index", "cultural_violence_index": "cultural_index",
                              "gender_violence_index": "gender_index", "structural_violence_index": "structural_index"})
    load(cur, "RelationsAndConclusions.FinalViolenceIndex", known(fin, municipalities, label="final index"),
         ["municipality_id", "year", "physical_index", "cultural_index", "gender_index", "structural_index", "final_violence_index"])

    # ------------------------------------------------------------------ catalogs of the categories the facts store
    print("catalogs")
    from panel import catalogs          # imported here: catalogs uses this module's connect
    catalogs.build(cur)

    # ------------------------------------------------------------------ checks
    cur.execute("SET FOREIGN_KEY_CHECKS = 1")
    print("checks")
    cur.execute("""SELECT COUNT(*) FROM information_schema.TABLE_CONSTRAINTS
                   WHERE CONSTRAINT_TYPE = 'FOREIGN KEY' AND TABLE_SCHEMA IN ('RelationsAndConclusions','Physical_violence',
                   'Structural_Violence','Cultural_violence','GENDER_VIOLENCE','Student_Context','Education_Outcomes',
                   'Territorial_Context','State_Action','Research_Design')""")
    print(f"  foreign keys declared: {cur.fetchone()[0]}")
    orphans = 0
    cur.execute("""SELECT k.TABLE_SCHEMA, k.TABLE_NAME, k.COLUMN_NAME, k.REFERENCED_TABLE_SCHEMA, k.REFERENCED_TABLE_NAME,
                          k.REFERENCED_COLUMN_NAME FROM information_schema.KEY_COLUMN_USAGE k
                   WHERE k.REFERENCED_TABLE_NAME IS NOT NULL AND k.TABLE_SCHEMA IN ('RelationsAndConclusions','Physical_violence',
                   'Structural_Violence','Cultural_violence','GENDER_VIOLENCE','Student_Context','Education_Outcomes',
                   'Territorial_Context','State_Action','Research_Design')""")
    for s, t, c, rs, rt, rc in cur.fetchall():
        cur.execute(f"SELECT COUNT(*) FROM `{s}`.`{t}` x LEFT JOIN `{rs}`.`{rt}` r ON r.`{rc}` = x.`{c}` "
                    f"WHERE x.`{c}` IS NOT NULL AND r.`{rc}` IS NULL")
        n = cur.fetchone()[0]
        if n:
            orphans += n
            print(f"  ORPHANS {s}.{t}.{c} -> {rt}: {n:,}")
    print(f"  rows pointing to nothing: {orphans}")
    db.close()


if __name__ == "__main__":
    main()
