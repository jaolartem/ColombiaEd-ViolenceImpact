"""
Violence by the identity of the victim (Medicina Legal), by DANE municipality and year.

    python -m panel.identity [--out output/panel]

For homicides and suicides: racial ancestry, group the victim belongs to (peasants, displaced people,
ethnic groups, people living on the street, ...), indigenous people, sexual orientation, gender identity,
and the detailed circumstance of the event (armed confrontation, political killing, socio-political
violence, partner conflict, ...). Definitive 2015-2024 and preliminary from January 2025.

The same category is written in several ways ("Sin información" / "Sin Información", "Indigena" /
"Indígena"): spellings that differ only in accents and case are merged, keeping the most frequent one.
Sexual orientation and gender identity read "No había sido implementada" in the years before the
variable was collected; that is kept as written, so its coverage is visible.

Writes identity_cases.csv: indicator, kind, group_name, cod_mpio, year, cases, preliminary.
"""
import argparse
from pathlib import Path

import pandas as pd

from panel import dane, indepaz, socrata

DATASETS = [   # (indicator, dataset, where, preliminary)
    ("homicide", "vtub-3de2", None, False),
    ("suicide", "f75u-mirk", None, False),
    ("homicide", "2kpj-cktv", "manera_de_muerte like '1 %'", True),
    ("suicide", "2kpj-cktv", "manera_de_muerte like '2 %'", True),
]
KINDS = {      # kind -> candidate field names
    "racial_ancestry": ["ancestro_racial"],
    "vulnerable_group": ["pertenencia_grupal"],
    "indigenous_people": ["pueblo_indigena"],
    "sexual_orientation": ["orientacion_sexual"],
    "gender_identity": ["identidad_de_genero"],
    "circumstance": ["circunstancia_del_hecho_detallada", "circunstancia_del_hecho"],
}


def build(token) -> pd.DataFrame:
    frames = []
    for indicator, dataset, where, preliminary in DATASETS:
        columns = socrata.dataset_columns(dataset)
        for kind, names in KINDS.items():
            field = next((n for n in names if n in columns), None)
            if not field:
                print(f"  {dataset}: no field for {kind}")
                continue
            df = socrata.query(dataset, select=f"codigo_dane_municipio, a_o_del_hecho, {field}, count(*) as cases",
                               where=where, group=f"codigo_dane_municipio, a_o_del_hecho, {field}", token=token)
            df = df.rename(columns={"codigo_dane_municipio": "cod_mpio", "a_o_del_hecho": "year", field: "group_name"})
            frames.append(df.assign(indicator=indicator, kind=kind, preliminary=preliminary))
        print(f"  {indicator:<9} {dataset}")
    df = pd.concat(frames, ignore_index=True)
    df["cases"] = pd.to_numeric(df["cases"])
    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    df["cod_mpio"] = dane.normalize_code(df["cod_mpio"])
    df["group_name"] = df["group_name"].fillna("Sin información").astype(str).str.strip()
    # merge spellings that differ only in accents and case: keep the most frequent spelling
    df["group_key"] = df["kind"] + "|" + df["group_name"].map(indepaz.key)
    spelling = (df.groupby(["group_key", "group_name"])["cases"].sum().reset_index()
                  .sort_values("cases").drop_duplicates("group_key", keep="last").set_index("group_key")["group_name"])
    df["group_name"] = df["group_key"].map(spelling)
    df = df.dropna(subset=["cod_mpio", "year"])
    df["year"] = df["year"].astype(int)
    df = df[(df["year"] < 2025) != df["preliminary"]]
    return (df.groupby(["indicator", "kind", "group_name", "cod_mpio", "year", "preliminary"], as_index=False)["cases"].sum())


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", default="output/panel", type=Path)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    print("identity (Medicina Legal)")
    df = build(socrata.app_token())
    df.to_csv(args.out / "identity_cases.csv", index=False)
    print(df.groupby(["indicator", "kind"])["cases"].sum().to_string())
    print(f"wrote {len(df):,} rows")


if __name__ == "__main__":
    main()
