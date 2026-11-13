"""
The door on the other side of the exam: higher education and the scholarships that open it.

    python -m panel.door [--out output/panel]

- Saber Pro (ICFES, u37r-hjmu), 2018-2022: the exit exam of higher education. Counted by the
  municipality of the school where the student finished secondary (estu_cod_cole_mcpio_termino), so it
  says how many of a municipality's school leavers got to the end of a degree, and with what scores.
- Higher-education enrolment (MEN, 5wck-szir), 2015-2021, by the municipality where the programme is
  offered: whether there is higher education within reach.
- Generacion E beneficiaries (MEN, 6sqn-9wh9), 2021, by municipality.
- ICETEX new beneficiaries (f673-3gn8) and renewals (nvcf-b8a3): published by department of origin
  only, so they stay at department level.

Writes saber_pro.csv, higher_ed_enrolment.csv, generacion_e.csv, icetex.csv.
"""
import argparse
from pathlib import Path

import pandas as pd

from panel import dane, socrata

SABER_PRO_SCORES = ["mod_razona_cuantitat_punt", "mod_lectura_critica_punt", "mod_competen_ciudada_punt",
                    "mod_ingles_punt", "mod_comuni_escrita_punt"]


def saber_pro(token) -> pd.DataFrame:
    periods = socrata.query("u37r-hjmu", select="periodo", group="periodo", token=token)["periodo"]
    averages = ", ".join(f"avg({c}::number) as {c}" for c in SABER_PRO_SCORES)
    frames = []
    for periodo in periods:
        try:
            frames.append(socrata.query(
                "u37r-hjmu",
                select=f"estu_cod_cole_mcpio_termino, periodo, estu_genero, count(distinct estu_consecutivo) as students, {averages}",
                where=f"periodo = '{periodo}'", group="estu_cod_cole_mcpio_termino, periodo, estu_genero", token=token))
        except RuntimeError as error:       # a score the server cannot cast: count only
            print(f"  saber pro {periodo}: scores left out ({str(error)[:80]})")
            frames.append(socrata.query(
                "u37r-hjmu", select="estu_cod_cole_mcpio_termino, periodo, estu_genero, count(distinct estu_consecutivo) as students",
                where=f"periodo = '{periodo}'", group="estu_cod_cole_mcpio_termino, periodo, estu_genero", token=token))
    df = pd.concat(frames, ignore_index=True).rename(columns={"estu_cod_cole_mcpio_termino": "cod_mpio", "estu_genero": "sex"})
    df["cod_mpio"] = dane.normalize_code(df["cod_mpio"])
    df["year"] = df["periodo"].str[:4].astype(int)
    for c in ["students"] + SABER_PRO_SCORES:
        df[c] = pd.to_numeric(df.get(c), errors="coerce")
    print(f"  saber pro: {df['students'].sum():,.0f} students, {df['cod_mpio'].isna().mean():.1%} rows without school municipality")
    return df


def enrolment(token) -> pd.DataFrame:
    df = socrata.query("5wck-szir",
                       select="c_digo_del_municipio_programa, a_o, semestre, id_sector, id_nivel_formacion, sum(matriculados_2015) as enrolled",
                       group="c_digo_del_municipio_programa, a_o, semestre, id_sector, id_nivel_formacion", token=token)
    df = df.rename(columns={"c_digo_del_municipio_programa": "cod_mpio", "a_o": "year", "semestre": "semester",
                            "id_sector": "sector_id", "id_nivel_formacion": "level_id"})
    df["cod_mpio"] = dane.normalize_code(df["cod_mpio"])
    df["enrolled"] = pd.to_numeric(df["enrolled"])
    print(f"  higher-ed enrolment: {len(df):,} rows, {df['year'].min()}-{df['year'].max()}")
    return df


def generacion_e(token) -> pd.DataFrame:
    df = socrata.query("6sqn-9wh9", select="fecha_de_corte, divipola_municipio, indicador_1_beneficiarios_ge",
                       order="fecha_de_corte, divipola_municipio", token=token)
    df = df.rename(columns={"divipola_municipio": "cod_mpio", "indicador_1_beneficiarios_ge": "beneficiaries",
                            "fecha_de_corte": "cutoff"})
    df["cod_mpio"] = dane.normalize_code(df["cod_mpio"])
    df["cutoff"] = pd.to_datetime(df["cutoff"], dayfirst=True).dt.date
    df["beneficiaries"] = pd.to_numeric(df["beneficiaries"], errors="coerce")
    return df


def icetex(token) -> pd.DataFrame:
    new = socrata.query("f673-3gn8",
                        select="vigencia, codigo_de_departamento_de, sexo_al_nacer, nivel_de_formacion, sum(numero_de_nuevos_beneficiarios) as n",
                        group="vigencia, codigo_de_departamento_de, sexo_al_nacer, nivel_de_formacion", token=token)
    new["kind"] = "new"
    renewed = socrata.query("nvcf-b8a3",
                            select="vigencia, codigo_de_departamento_de, sexo_al_nacer, nivel_de_formacion, sum(numero_de_renovaciones) as n",
                            group="vigencia, codigo_de_departamento_de, sexo_al_nacer, nivel_de_formacion", token=token)
    renewed["kind"] = "renewal"
    df = pd.concat([new, renewed], ignore_index=True).rename(columns={
        "vigencia": "year", "codigo_de_departamento_de": "department_id", "sexo_al_nacer": "sex",
        "nivel_de_formacion": "level", "n": "beneficiaries"})
    df["beneficiaries"] = pd.to_numeric(df["beneficiaries"], errors="coerce")
    df["department_id"] = pd.to_numeric(df["department_id"], errors="coerce")
    print(f"  icetex: {df['beneficiaries'].sum():,.0f} credits, {df['year'].min()}-{df['year'].max()}")
    return df


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", default="output/panel", type=Path)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    token = socrata.app_token()
    print("higher education")
    saber_pro(token).to_csv(args.out / "saber_pro.csv", index=False)
    enrolment(token).to_csv(args.out / "higher_ed_enrolment.csv", index=False)
    generacion_e(token).to_csv(args.out / "generacion_e.csv", index=False)
    icetex(token).to_csv(args.out / "icetex.csv", index=False)


if __name__ == "__main__":
    main()
