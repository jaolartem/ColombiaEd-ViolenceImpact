"""
Police records (MinDefensa), by municipality and day, January 2003 to the last update.

    python -m panel.police [--out output/panel]

Homicide (with the victim's sex), intra-family violence and sexual offences (with the victim's sex).
Read by day, so every case falls in the government in office on its date with no approximation.

Police-recorded intra-family and sexual violence rises three to five times between 2003 and 2026: it
follows reporting (complaint channels, registration systems) more than prevalence, and is documented as
such. Homicide is the reliable long series.

Writes police_daily.csv: indicator, cod_mpio, day, sex, cases.
"""
import argparse
from pathlib import Path

import pandas as pd

from panel import dane, socrata

DATASETS = {
    "homicide": "m8fd-ahd9",
    "domestic_violence": "gepp-dxcs",
    "sexual_violence": "bz43-8ahq",
}
SEX = {"MASCULINO": "M", "FEMENINO": "F", "HOMBRE": "M", "MUJER": "F"}


def build(token) -> pd.DataFrame:
    frames = []
    for indicator, dataset in DATASETS.items():
        has_sex = "sexo" in socrata.dataset_columns(dataset)
        sex = ", sexo" if has_sex else ""
        df = socrata.query(dataset, select=f"cod_muni, fecha_hecho{sex}, sum(cantidad) as cases",
                           group=f"cod_muni, fecha_hecho{sex}", token=token)
        df["indicator"] = indicator
        df["sex"] = df["sexo"].str.upper().map(SEX).fillna("U") if has_sex else "U"
        print(f"  {indicator:<18} {dataset}: {len(df):>9,} municipality-days, {pd.to_numeric(df['cases']).sum():>10,.0f} cases")
        frames.append(df)
    df = pd.concat(frames, ignore_index=True)
    df["cod_mpio"] = dane.normalize_code(df["cod_muni"])
    df["day"] = pd.to_datetime(df["fecha_hecho"]).dt.date
    df["cases"] = pd.to_numeric(df["cases"])
    missing = df[df["cod_mpio"].isna()].groupby("indicator")["cases"].sum()
    if missing.any():
        print("  cases without a municipality code:", missing.to_dict())
    return (df.dropna(subset=["cod_mpio"])
              .groupby(["indicator", "cod_mpio", "day", "sex"], as_index=False)["cases"].sum())


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", default="output/panel", type=Path)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    print("police records")
    df = build(socrata.app_token())
    df.to_csv(args.out / "police_daily.csv", index=False)
    print(f"wrote {len(df):,} rows, {df['day'].min()} to {df['day'].max()}")


if __name__ == "__main__":
    main()
