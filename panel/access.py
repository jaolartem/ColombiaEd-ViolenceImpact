"""
Access: schools and health services within each municipality.

    python -m panel.access [--out output/panel]

- Schools (MEN, cfw5-qzt5): every pre-school, primary and secondary establishment by year, with its
  sector, number of sites and enrolment. Counted by municipality, year and sector.
- Health (MinSalud, REPS c36g-9fc2): registered health providers and their sites, as of the latest
  cut-off. Counted by the municipality of the site, by class of provider and legal nature.

Writes schools.csv and health_sites.csv.
"""
import argparse
from pathlib import Path

import pandas as pd

from panel import dane, socrata


def schools(token) -> pd.DataFrame:
    df = socrata.query("cfw5-qzt5",
                       select="a_o, cod_dane_municipio, sector, count(*) as establishments, sum(cantidad_sedes) as sites, sum(total_matricula) as enrolment",
                       group="a_o, cod_dane_municipio, sector", token=token)
    df = df.rename(columns={"a_o": "year", "cod_dane_municipio": "cod_mpio"})
    df["cod_mpio"] = dane.normalize_code(df["cod_mpio"])
    for c in ("year", "establishments", "sites", "enrolment"):
        df[c] = pd.to_numeric(df[c], errors="coerce")
    print(f"  schools: {df['year'].min():.0f}-{df['year'].max():.0f}, {df['establishments'].sum():,.0f} establishment-years")
    return df.dropna(subset=["cod_mpio"])


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
    schools(token).to_csv(args.out / "schools.csv", index=False)
    health(token).to_csv(args.out / "health_sites.csv", index=False)


if __name__ == "__main__":
    main()
