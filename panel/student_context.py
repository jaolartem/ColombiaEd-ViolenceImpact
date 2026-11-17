"""
What a municipality's Saber 11 exam takers report about home and family, 2010-2022 (ICFES API).

    python -m panel.student_context [--out output/panel]

Per municipality of the school and exam period: the share of students who report internet, a computer,
a car and a washing machine at home, who live in stratum 1 or 2, and whose mother finished tertiary
education or did not go beyond primary. Shares are over the students who answered (blank, "No sabe"
and "No Aplica" are left out). Periods 20194 and 20224 list every student twice, which does not change
a share.

These are the students' own words, set beside what DANE's 2018 census says of the same municipality
(Student_Context.StudentsVersusCensus). They never enter a violence index.

Writes student_context.csv.
"""
import argparse
from pathlib import Path

import pandas as pd

from panel import dane, indepaz, socrata, sources

YES_NO = {"fami_tieneinternet": "internet", "fami_tienecomputador": "computer",
          "fami_tieneautomovil": "car", "fami_tienelavadora": "washing_machine"}
NOT_AN_ANSWER = {"", "no sabe", "no aplica", "none", "nan"}
HIGHER_ED = {"tecnica o tecnologica completa", "educacion profesional completa", "postgrado"}
PRIMARY_OR_LESS = {"ninguno", "primaria incompleta", "primaria completa"}


def _counts(dataset, code, periodo, field, token):
    df = socrata.query(dataset, select=f"{code}, {field}, count(*) as n", where=f"periodo = '{periodo}'",
                       group=f"{code}, {field}", token=token)
    if df.empty:
        return df
    df = df.rename(columns={code: "cod_mpio", field: "answer"})
    df["answer"] = df.get("answer", pd.Series(dtype=str)).fillna("").map(indepaz.key)
    df["n"] = pd.to_numeric(df["n"])
    return df[~df["answer"].isin(NOT_AN_ANSWER)]


def build(token) -> pd.DataFrame:
    s = sources.SABER
    periods = socrata.query(s["dataset"], select="periodo", group="periodo", token=token)["periodo"]
    rows = []
    for periodo in periods:
        shares = {}
        for field, name in YES_NO.items():
            c = _counts(s["dataset"], s["code"], periodo, field, token)
            if len(c):
                t = c.pivot_table(index="cod_mpio", columns="answer", values="n", aggfunc="sum", fill_value=0)
                shares[f"share_{name}"] = t.get("si", 0) / t.sum(axis=1)
        c = _counts(s["dataset"], s["code"], periodo, "fami_estratovivienda", token)
        if len(c):
            t = c.groupby("cod_mpio")["n"].sum()
            low = c[c["answer"].isin({"estrato 1", "estrato 2"})].groupby("cod_mpio")["n"].sum()
            shares["share_stratum_1_2"] = low.reindex(t.index, fill_value=0) / t
        c = _counts(s["dataset"], s["code"], periodo, "fami_educacionmadre", token)
        if len(c):
            t = c.groupby("cod_mpio")["n"].sum()
            for name, group in (("share_mother_higher_ed", HIGHER_ED), ("share_mother_primary_or_less", PRIMARY_OR_LESS)):
                shares[name] = c[c["answer"].isin(group)].groupby("cod_mpio")["n"].sum().reindex(t.index, fill_value=0) / t
        if shares:
            df = pd.DataFrame(shares)
            df.index.name = "cod_mpio"
            rows.append(df.reset_index().assign(periodo=periodo))
        print(f"  {periodo}: {len(shares)} measures")
    df = pd.concat(rows, ignore_index=True)
    df["cod_mpio"] = dane.normalize_code(df["cod_mpio"])
    return df.dropna(subset=["cod_mpio"])


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", default="output/panel", type=Path)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    print("student context (ICFES questionnaire)")
    df = build(socrata.app_token())
    df.to_csv(args.out / "student_context.csv", index=False)
    print(f"wrote {len(df):,} municipality-periods")


if __name__ == "__main__":
    main()
