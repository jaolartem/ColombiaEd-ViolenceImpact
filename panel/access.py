"""
Access: health services within each municipality (schools: panel.schools).

    python -m panel.access [--out output/panel]

- Health (MinSalud, REPS c36g-9fc2): registered health providers and their sites, as of the latest
  cut-off. Counted by the municipality of the site, by class of provider and legal nature.

Writes health_sites.csv.
"""
import argparse
from pathlib import Path

import pandas as pd

from panel import dane, socrata


def health(token) -> pd.DataFrame:
    df = socrata.query("c36g-9fc2",
                       select="municipiosede, claseprestador, naturalezajuridica, count(*) as sites, max(fecha_corte_reps) as cutoff",
                       group="municipiosede, claseprestador, naturalezajuridica", token=token)
    df = df.rename(columns={"municipiosede": "cod_mpio", "claseprestador": "provider_class",
                            "naturalezajuridica": "legal_nature"})
    df["cod_mpio"] = dane.normalize_code(df["cod_mpio"])
    df["sites"] = pd.to_numeric(df["sites"])
    print(f"  health sites: {df['sites'].sum():,}, cut-off {df['cutoff'].max()}")
    return df.dropna(subset=["cod_mpio"])


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", default="output/panel", type=Path)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    token = socrata.app_token()
    print("access")
    health(token).to_csv(args.out / "health_sites.csv", index=False)


if __name__ == "__main__":
    main()
