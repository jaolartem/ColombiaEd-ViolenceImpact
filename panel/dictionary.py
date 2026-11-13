"""
Writes docs/data_dictionary.md from the loaded database: what each table is, its source, its row count
and coverage, and the known problems of the data.

    python -m panel.dictionary

Descriptions live here; numbers come from the database, so the document says what is loaded.
"""
from pathlib import Path

import pandas as pd

from panel.load_db import connect

ROOT = Path(__file__).resolve().parent.parent

TABLES = {
    "RelationsAndConclusions": {
        "Departments": "DANE departments.",
        "Municipalities": "DANE municipalities (2018 census geography). `id` is the DANE code as a number; every fact joins on it.",
        "Sexes": "F, M, U (unknown, not reported, or total).",
        "Population": "DANE projections and back-projections (2018 census base), mid-year, all areas, 1995-2042.",
        "PopulationBySexAge": "The same by sex and age: 5-year bands, single ages 15-19 (the Saber 11 cohort), 80+.",
        "Governments": "Presidential terms, 7 August to 7 August: Uribe I and II, Santos I and II, Duque, Petro.",
        "Government_Phases": "Terms, with Santos II split at the final peace agreement (24 Nov 2016).",
        "Sources": "Institutions the data comes from, with their kind: official record, memory observatory, press-based, census, administrative.",
        "SourceDatasets": "Each dataset, file or page read, with its coverage.",
        "ViolenceIndicators": "Catalogue of count indicators and the Galtung dimension they belong to (the legend, not a cause).",
        "ViolenceCases": "Medicina Legal: homicide, suicide, intra-family violence (children; other relatives and older adults), partner and sexual violence, per municipality, year and victim's sex. Definitive 2015-2024, preliminary January 2025 to July 2026.",
        "PoliceDailyCases": "Police (MinDefensa): homicide, intra-family violence, sexual offences per municipality and day, January 2003 to the last update.",
        "PeriodRates": "Cases per 100,000 person-years by government and by phase, per municipality and measure, over the exact days each source covers.",
        "FinalViolenceIndex": "Geometric mean of the four dimension indices, 2015-2025.",
        "SmoothedValues": "Empirical Bayes value of each rate, mean and share that rests on a base, pulled toward the department; written by `panel.quality`.",
        "DataQualityFlags": "What the validation of each source found, per municipality, column and period: error, missing, inconsistent, break, small base or extreme. Detail in docs/data_quality.md.",
    },
    "Physical_violence": {
        "EventModalities": "CNMH modalities of armed-conflict violence (massacre, selective killing, forced disappearance, kidnapping, landmines, recruitment, attack on a town, act of war, damage to civilian property, sexual violence, terrorist attack).",
        "Perpetrators": "Presumed perpetrators as the source writes them.",
        "ViolenceEvents": "One row per event: CNMH (all modalities, from 1958), INDEPAZ massacres (2020-), Police massacres (2022-). Date and its precision, municipality, victims, presumed perpetrator, displacement and confinement marks, and the massacre cluster.",
        "EventLinks": "Triangulation of massacres across sources: same municipality, at most 3 days apart (15 when one date is month-only), one to one.",
        "PhysicalViolenceIndex": "Homicide, suicide, violence against children, other intra-family violence (Medicina Legal), 2015-2025.",
    },
    "Cultural_violence": {
        "IdentityGroups": "Categories of victim identity as Medicina Legal records them: racial ancestry, group, indigenous people, sexual orientation, gender identity, circumstance.",
        "IdentityViolenceCases": "Homicides and suicides per municipality, year and identity category.",
        "CulturalViolenceIndex": "Homicide of Black, Indigenous and Mulatto victims, of members of vulnerable groups, and socio-political homicide.",
    },
    "GENDER_VIOLENCE": {
        "GenderViolenceIndex": "Partner and sexual violence per 100,000 inhabitants; homicide and suicide of women per 100,000 women.",
    },
    "Structural_Violence": {
        "Census2018Municipal": "DANE census 2018 per municipality: IPM (census source) and its 15 deprivations, NBI and components, floors, public services including internet, people by energy stratum.",
        "Inequality": "Empty: no municipal Gini is published yearly. Documented gap.",
        "SchoolsByMunicipality": "MEN directory: establishments, sites and enrolment by municipality, year and sector, 2015-2025.",
        "HealthSites": "MinSalud REPS: registered health sites by municipality, class of provider and legal nature.",
        "StructuralViolenceIndex": "Census 2018 deprivation (IPM, NBI, no internet) and lack of health sites.",
    },
    "Education_Outcomes": {
        "ExamPeriods": "Saber 11 periods, calendar, scale (the exam changed in 2014-2) and government in office.",
        "MunicipalScores": "Saber 11 per municipality of the school, period and sex, 2010-2022 (ICFES API): students and mean scores, and z-scores against the national mean and SD of the period.",
        "Schools": "Schools seen in the Saber 11 microdata: DANE code, name, municipality, sector (official or not) and area (urban or rural), as the newest file that names each school records them. 796 have no area.",
        "MunicipalScoresMicro": "Saber 11 per municipality and period from the microdata, 2000-2022: students, mean and z-score of mathematics and of the global score: ICFES's own since 2014-2, the simple mean of the five tests before.",
        "Students": "Each exam taker, 2000-1 to 2022-2 (ICFES period files).",
        "StudentScores": "Each exam taker's scores; before 2014-2 sciences and social are means of the old areas. global_mean, the simple mean of the five tests, exists for every period.",
        "EnrolmentAndDropout": "MEN: net enrolment, dropout, approval, repetition per municipality, 2011-2024.",
        "SaberProByMunicipality": "Saber Pro 2018-2022 by the municipality of the school the student finished: the other side of the door.",
        "HigherEdEnrolment": "MEN higher-education enrolment by municipality where the programme is offered, 2015-2021.",
        "GeneracionE": "Generacion E beneficiaries by municipality, 2021 cut-offs.",
        "IcetexCredits": "ICETEX new credits and renewals by department of origin (no municipality is published).",
    },
    "Student_Context": {
        "StudentHousehold": "What each exam taker reports about home; each period asked different questions, so blanks mean not asked.",
        "StudentPractices": "Books at home, daily reading, internet use (asked since the 2010s).",
        "MunicipalStudentContext": "What a municipality's exam takers report, 2010-2022 (ICFES API): internet, computer, car, washing machine, stratum 1-2, mother's education.",
    },
}

KNOWN_PROBLEMS = """
## Known problems of the data

- **Saber 11 on datos.gov.co** (`kgxf-xxbe`): periods 20194 and 20224 list every student twice
  (1,096,524 rows for 546,211 students), so students are counted by distinct id. Calendar A 2018, 2020
  and 2021 are missing, and nothing after 2022 is there: those come from DataIcfes files. Seven 2011 rows
  write a score with a decimal comma and are left out. Before 2014-2 there is no global score and only
  mathematics and English are present; periods are compared as z-scores.
- **The exam changed in 2014-2**: scores before and after are not on the same scale.
- **Saber 11 microdata, cleaned on load**: a test written as -1 (2005-2007) is NULL, and an exam with every
  test at 0 was not taken or was annulled, so its scores are NULL. A single test at 0 is kept. In 2008-2009
  the computer question is coded 0/1/2 or 0/3 without a codebook and is left NULL. Floor, books, reading,
  internet hours and work hours exist only in the periods whose questionnaire asked them.
- **Police intra-family and sexual violence** rise three to five times between 2003 and 2026: they follow
  reporting (complaint channels, registration) more than prevalence. Homicide is the reliable long series.
- **Massacres disagree across sources.** From 2020, INDEPAZ and Police agree on 75-79% of events each way;
  80% of CNMH massacres are in INDEPAZ, but CNMH holds only 15% of INDEPAZ's, and 45% of those with four
  or more victims. The gap is mostly CNMH coverage or lag, not the 3-versus-4-victims definition.
  The Police massacre table starts in 2022.
- **INDEPAZ** is a web page: column order changes by year, some rows swap department and municipality,
  2024-2025 write two-digit years, a few have no victim count yet. Two rows place a municipality in the
  wrong department (La Ceja in Risaralda, Cimitarra in Norte de Santander) and are left without a code.
- **CNMH** cases with year 0 have no date. Its latest months are documented with a lag (cut-off in each
  dataset's description).
- **Medicina Legal** sexual orientation and gender identity read "No habia sido implementada" before the
  variable was collected.
- **DANE files** do not agree on where the code is (the 1995-2004 file has it in DPMP, 2005-2017 in MPIO).
- **ICETEX** publishes the department of origin only.
- **No municipal Gini** is published yearly: `Structural_Violence.Inequality` is empty on purpose.
- **The cultural index sits near its floor** in most municipality-years: socio-political homicide is rare,
  so one component is often zero, and a geometric mean with a zero component collapses to the floor
  (0.001). Multi-year windows, or another way of combining that dimension, are an analysis decision.
- **Saber 11 2023-2025** are only published on DataIcfes (icfes.gov.co), which answers 403 Forbidden from
  the machine that built this database. The microdata here run 2000-1 to 2022-2, from the ICFES period
  files. Before 2014-2 the exam had other areas: natural sciences is the mean of biology, chemistry and
  physics, social is the mean of history and geography, critical reading is language.
- **Saber 11 microdata gaps and codes**: there is no 2003-1 file (calendar B, first semester of 2003). Inside
  the files the second semester of 2019-2022 is coded 20194, 20204, 20214, 20224 (the file names say 20192 ...);
  the database keeps the code written inside the file. The 2019-1 file writes its column names in lowercase.
- **Saber 11 microdata 2000-2009** place the school's municipality by name; it is matched within the
  department, or through the school's ICFES code as later files place it.
- **Codes**: Medicina Legal writes 5001, ICFES and DANE 05001. Every source is normalised to the DANE code;
  names never join.
"""


def main():
    db = connect()
    cur = db.cursor()
    lines = ["# Data dictionary", "",
             "Generated from the loaded database by `python -m panel.dictionary`. The model and its frame are in",
             "`Tables_and_relations.sql`; how to rebuild everything is in the README.", ""]
    for schema, tables in TABLES.items():
        lines += [f"## {schema}", "", "| Table | Rows | What it is |", "|---|---:|---|"]
        for table, text in tables.items():
            cur.execute(f"SELECT COUNT(*) FROM `{schema}`.`{table}`")
            lines.append(f"| `{table}` | {cur.fetchone()[0]:,} | {text} |")
        lines.append("")

    lines += ["## Sources and coverage", "", "| Source | Dataset | Description | From | To | Preliminary |", "|---|---|---|---|---|---|"]
    cur.execute("""SELECT s.code, d.dataset, d.description, d.coverage_from, d.coverage_to, d.preliminary
                   FROM RelationsAndConclusions.SourceDatasets d JOIN RelationsAndConclusions.Sources s ON s.id = d.source_id
                   ORDER BY s.id, d.dataset""")
    for row in cur.fetchall():
        lines.append("| " + " | ".join("" if v is None else str(v) for v in row) + " |")
    lines.append("")

    lines += ["## Coverage by year", "", "Rows (or cases) per source and year.", ""]
    queries = {
        "Medicina Legal cases": "SELECT year, SUM(cases) FROM RelationsAndConclusions.ViolenceCases GROUP BY year",
        "Police cases": "SELECT YEAR(day), SUM(cases) FROM RelationsAndConclusions.PoliceDailyCases GROUP BY YEAR(day)",
        "CNMH events": "SELECT YEAR(e.day), COUNT(*) FROM Physical_violence.ViolenceEvents e JOIN RelationsAndConclusions.SourceDatasets d ON d.id = e.dataset_id WHERE d.source_id = 3 GROUP BY YEAR(e.day)",
        "INDEPAZ massacres": "SELECT YEAR(e.day), COUNT(*) FROM Physical_violence.ViolenceEvents e JOIN RelationsAndConclusions.SourceDatasets d ON d.id = e.dataset_id WHERE d.source_id = 4 GROUP BY YEAR(e.day)",
        "Police massacres": "SELECT YEAR(e.day), COUNT(*) FROM Physical_violence.ViolenceEvents e JOIN RelationsAndConclusions.SourceDatasets d ON d.id = e.dataset_id WHERE d.source_id = 2 GROUP BY YEAR(e.day)",
        "Saber 11 students": "SELECT p.year, SUM(m.students) FROM Education_Outcomes.MunicipalScores m JOIN Education_Outcomes.ExamPeriods p ON p.id = m.exam_period_id GROUP BY p.year",
        "Saber 11 microdata": "SELECT p.year, COUNT(*) FROM Education_Outcomes.Students s JOIN Education_Outcomes.ExamPeriods p ON p.id = s.exam_period_id GROUP BY p.year",
        "Saber Pro students": "SELECT year, SUM(students) FROM Education_Outcomes.SaberProByMunicipality GROUP BY year",
        "MEN enrolment/dropout": "SELECT year, COUNT(*) FROM Education_Outcomes.EnrolmentAndDropout GROUP BY year",
        "Population": "SELECT year, SUM(population) FROM RelationsAndConclusions.Population GROUP BY year",
    }
    matrix = {}
    for label, q in queries.items():
        cur.execute(q)
        matrix[label] = {int(y): float(n) for y, n in cur.fetchall() if y is not None}
    years = list(range(2002, 2027))
    lines.append("| | " + " | ".join(str(y) for y in years) + " |")
    lines.append("|---|" + "---:|" * len(years))
    for label, row in matrix.items():
        cells = []
        for y in years:
            v = row.get(y)
            cells.append("" if not v else (f"{v / 1e6:.1f}M" if v >= 1e6 else f"{v / 1e3:.0f}k" if v >= 1e4 else f"{v:,.0f}"))
        lines.append(f"| {label} | " + " | ".join(cells) + " |")
    lines += ["", KNOWN_PROBLEMS.strip(), ""]

    path = ROOT / "docs" / "data_dictionary.md"
    path.parent.mkdir(exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {path}")
    db.close()


if __name__ == "__main__":
    main()
