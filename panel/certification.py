"""
Who runs education in each municipality, year by year: the certified territorial entity (ETC).

    python -m panel.certification

Under Law 715 of 2001 a certified territorial entity (entidad territorial certificada, ETC) runs public
education itself: it receives the SGP for education, hires and pays the teachers, contracts school meals and
transport, and sets local rules. Municipalities of more than 100,000 inhabitants were certified by law; others
by the Ministry of Education (MEN) on request. A municipality that is not certified is run by its
department's education secretariat. So the unit that administers a school is not always its municipality:
it is the ETC, a certified municipality or a department.

Source: MEN, statistics of preschool, basic and secondary education by municipality (datos.gov.co
nudc-7mev), which names each municipality's ETC every year, 2011 onwards.

Transform and validate:
- the ETC code is written as an integer in most years and, in 2021, with a thousands point that also lost
  its trailing zeros ("3.76" is 3760, "10.85" is 10850): it is read back to the integer;
- the same ETC under several spellings takes its most frequent name;
- an ETC that runs exactly one municipality is a certified municipality (or district); one that runs
  several is a department;
- a municipality-year assigned to "NACIONAL" (code 0) or to no ETC is not loaded and is annotated in
  RelationsAndConclusions.DataQualityFlags (source MEN, inconsistent or missing);
- an ETC that changes for a municipality between years is a certification (or its loss): annotated as a
  break so it is read as an administrative change, not as noise.

Before 2011 this source says nothing; the year each ETC was certified is not in it.

Loads Education_Outcomes.CertifiedEntities and Education_Outcomes.EducationAuthority.
"""
import numpy as np
import pandas as pd

from panel import dane
from panel.load_db import connect, load
from panel.socrata import app_token, query

DATASET = "nudc-7mev"


def etc_code(raw: pd.Series) -> pd.Series:
    s = raw.astype(str).str.strip()
    dotted = s.str.contains(r"\.")
    out = pd.to_numeric(s, errors="coerce")
    out[dotted] = (pd.to_numeric(s[dotted], errors="coerce") * 1000).round()
    return out.astype("Int64")


def main():
    df = query(DATASET, "a_o, c_digo_municipio, c_digo_etc, etc", token=app_token(), order="a_o, c_digo_municipio")
    df["year"] = df["a_o"].astype(int)
    df["municipality_id"] = dane.normalize_code(df["c_digo_municipio"]).astype(float).astype("Int64")
    df["etc_id"] = etc_code(df["c_digo_etc"])
    df["etc"] = df["etc"].str.strip()
    known = {int(c) for c in dane.municipalities()["cod_mpio"]}
    df = df[df["municipality_id"].isin(known)].copy()

    flags = []
    def add(mask, kind, note):
        f = df[mask]
        if len(f):
            flags.append(pd.DataFrame({"source": "MEN", "source_table": "EducationAuthority", "column_name": "entity_id",
                                       "municipality_id": f["municipality_id"].astype(int), "period": f["year"].astype(str),
                                       "kind": kind, "value": f["etc_id"].astype(float),
                                       "note": note[mask].values if isinstance(note, pd.Series) else note}))

    national = df["etc_id"] == 0
    add(national, "inconsistent", "assigned to NACIONAL, not to a certified entity; not loaded")
    nothing = df["etc_id"].isna()
    add(nothing, "missing", "no certified entity named; not loaded")
    df = df[~national & ~nothing]
    twice = df.duplicated(["municipality_id", "year"], keep=False)
    add(twice, "inconsistent", "two certified entities in the same year; not loaded")
    df = df[~twice]

    names = df.groupby("etc_id")["etc"].agg(lambda s: s.value_counts().index[0])
    runs = df.groupby("etc_id")["municipality_id"].nunique()
    only = df.groupby("etc_id")["municipality_id"].first()
    dept = df.groupby("etc_id")["municipality_id"].agg(lambda s: (s.iloc[0] // 1000))
    entities = pd.DataFrame({"id": names.index.astype(int), "name": names.str.replace(r"\s*\(ETC\)\s*$", "", regex=True).values,
                             "kind": np.where(runs.values == 1, "municipality", "department"),
                             "department_id": dept.values.astype(int),
                             "municipality_id": np.where(runs.values == 1, only.values, pd.NA)})

    df = df.sort_values(["municipality_id", "year"])
    prev = df.groupby("municipality_id")["etc_id"].shift()
    change = prev.notna() & (prev != df["etc_id"])
    add(change, "break", "the certified entity changes: " + prev.astype("Int64").astype(str) + " to " + df["etc_id"].astype(str))

    flags = pd.concat(flags, ignore_index=True) if flags else pd.DataFrame()
    print(f"  {len(entities)} certified entities: {int((entities['kind'] == 'municipality').sum())} municipalities, "
          f"{int((entities['kind'] == 'department').sum())} departments")
    for kind, n in (flags.groupby("kind").size().items() if len(flags) else []):
        print(f"  MEN {kind:<14} {n:>6,}")

    db = connect()
    cur = db.cursor()
    cur.execute("DELETE FROM RelationsAndConclusions.DataQualityFlags WHERE source = 'MEN' AND source_table = 'EducationAuthority'")
    if len(flags):
        load(cur, "RelationsAndConclusions.DataQualityFlags", flags,
             ["source", "source_table", "column_name", "municipality_id", "period", "kind", "value", "note"])
    cur.execute("SET FOREIGN_KEY_CHECKS = 0")
    for t in ("EducationAuthority", "CertifiedEntities"):
        cur.execute(f"TRUNCATE TABLE Education_Outcomes.{t}")
    load(cur, "Education_Outcomes.CertifiedEntities", entities, ["id", "name", "kind", "department_id", "municipality_id"])
    load(cur, "Education_Outcomes.EducationAuthority", df.rename(columns={"etc_id": "entity_id"}),
         ["municipality_id", "year", "entity_id"])
    cur.execute("SET FOREIGN_KEY_CHECKS = 1")
    db.commit()
    db.close()


if __name__ == "__main__":
    main()
