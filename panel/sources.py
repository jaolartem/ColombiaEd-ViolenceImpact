"""
What is read from datos.gov.co, by DANE municipality and year.

Violence (Instituto Nacional de Medicina Legal y Ciencias Forenses): definitive figures 2015-2024 and
preliminary figures from January 2025 (2026 is a partial year). The preliminary datasets put all
fatal and all non-fatal cases in one table each; the context column says which kind of case it is,
with the same numbering as the definitive datasets.

Education: Saber 11 results (ICFES) and enrolment, dropout and approval rates (MEN).
"""

ML = dict(code="codigo_dane_municipio", year="a_o_del_hecho", sex="sexo_de_la_victima")
FATAL_PRELIMINARY = "2kpj-cktv"       # Lesiones fatales de causa externa, enero 2025 en adelante
NONFATAL_PRELIMINARY = "79dd-d24f"    # Lesiones no fatales de causa externa, enero 2025 en adelante

# indicator -> [(dataset, where, preliminary)]
VIOLENCE = {
    "homicide": [
        ("vtub-3de2", None, False),
        (FATAL_PRELIMINARY, "manera_de_muerte like '1 %'", True),
    ],
    "suicide": [
        ("f75u-mirk", None, False),
        (FATAL_PRELIMINARY, "manera_de_muerte like '2 %'", True),
    ],
    # Intra-family violence is split so the parts do not overlap: against children and adolescents
    # (context 3), and against other relatives and older adults (contexts 4 and 5). Partner violence
    # (context 6) is its own indicator and belongs to the gender dimension.
    "violence_children": [
        ("ers2-kerr", "contexto_del_hecho like '3 %'", False),
        (NONFATAL_PRELIMINARY, "contexto_de_violencia like '3 %'", True),
    ],
    "domestic_violence": [
        ("ers2-kerr", "contexto_del_hecho like '4 %' or contexto_del_hecho like '5 %'", False),
        (NONFATAL_PRELIMINARY, "contexto_de_violencia like '4 %' or contexto_de_violencia like '5 %'", True),
    ],
    "partner_violence": [
        ("9fs6-37ea", None, False),
        (NONFATAL_PRELIMINARY, "contexto_de_violencia like '6 %'", True),
    ],
    "sexual_violence": [
        ("hyqu-diue", None, False),
        (NONFATAL_PRELIMINARY, "contexto_de_violencia like '2 %'", True),
    ],
}

# Saber 11, 2010-2022. Two facts about this dataset shape the query:
# - periods 20194 and 20224 list every student twice (1,096,524 rows for 546,211 students), so
#   students are counted by their distinct `estu_consecutivo`;
# - calendar A 2018, 2020 and 2021 are not in it, nor is anything after 2022: those come from
#   DataIcfes (https://www.icfes.gov.co/investigaciones/data-icfes/), which publishes files, not an API.
SABER = dict(
    dataset="kgxf-xxbe",
    code="cole_cod_mcpio_ubicacion",
    scores=["punt_global", "punt_matematicas", "punt_lectura_critica", "punt_sociales_ciudadanas",
            "punt_c_naturales", "punt_ingles"],
)

MEN = dict(
    dataset="nudc-7mev",
    code="c_digo_municipio",
    year="a_o",
    columns={
        "cobertura_neta": "net_enrolment",
        "cobertura_neta_media": "net_enrolment_upper_secondary",
        "deserci_n": "dropout",
        "deserci_n_media": "dropout_upper_secondary",
        "aprobaci_n": "approval",
        "repitencia": "repetition",
    },
)
