# Data dictionary

Generated from the loaded database by `python -m panel.dictionary`. The model and its frame are in
`Tables_and_relations.sql`; how to rebuild everything is in the README.

## RelationsAndConclusions

| Table | Rows | What it is |
|---|---:|---|
| `Departments` | 33 | DANE departments. |
| `Municipalities` | 1,123 | DANE municipalities (2018 census geography). `id` is the DANE code as a number; every fact joins on it. |
| `Sexes` | 3 | F, M, U (unknown, not reported, or total). |
| `Population` | 53,881 | DANE projections and back-projections (2018 census base), mid-year, all areas, 1995-2042. |
| `PopulationBySexAge` | 2,263,002 | The same by sex and age: 5-year bands, single ages 15-19 (the Saber 11 cohort), 80+. |
| `Governments` | 6 | Presidential terms, 7 August to 7 August: Uribe I and II, Santos I and II, Duque, Petro. |
| `Government_Phases` | 7 | Terms, with Santos II split at the final peace agreement (24 Nov 2016). |
| `Sources` | 9 | Institutions the data comes from, with their kind: official record, memory observatory, press-based, census, administrative. |
| `SourceDatasets` | 41 | Each dataset, file or page read, with its coverage. |
| `ViolenceIndicators` | 7 | Catalogue of count indicators and the Galtung dimension they belong to (the legend, not a cause). |
| `ViolenceCases` | 75,725 | Medicina Legal: homicide, suicide, intra-family violence (children; other relatives and older adults), partner and sexual violence, per municipality, year and victim's sex. Definitive 2015-2024, preliminary January 2025 to July 2026. |
| `PoliceDailyCases` | 1,095,782 | Police (MinDefensa): homicide, intra-family violence, sexual offences per municipality and day, January 2003 to the last update. |
| `PeriodRates` | 382,768 | Cases per 100,000 person-years by government and by phase, per municipality and measure, over the exact days each source covers. |
| `FinalViolenceIndex` | 12,350 | Geometric mean of the four dimension indices, 2015-2025. |
| `SmoothedValues` | 642,826 | Empirical Bayes value of each rate, mean and share that rests on a base, pulled toward the department; written by `panel.quality`. |
| `DataQualityFlags` | 30,864 | What the validation of each source found, per municipality, column and period: error, missing, inconsistent, break, small base or extreme. Detail in docs/data_quality.md. |

## Physical_violence

| Table | Rows | What it is |
|---|---:|---|
| `EventModalities` | 11 | CNMH modalities of armed-conflict violence (massacre, selective killing, forced disappearance, kidnapping, landmines, recruitment, attack on a town, act of war, damage to civilian property, sexual violence, terrorist attack). |
| `Perpetrators` | 15 | Presumed perpetrators as the source writes them. |
| `ViolenceEvents` | 372,654 | One row per event: CNMH (all modalities, from 1958), INDEPAZ massacres (2020-), Police massacres (2022-). Date and its precision, municipality, victims, presumed perpetrator, displacement and confinement marks, and the massacre cluster. |
| `EventLinks` | 459 | Triangulation of massacres across sources: same municipality, at most 3 days apart (15 when one date is month-only), one to one. |
| `PhysicalViolenceIndex` | 12,350 | Homicide, suicide, violence against children, other intra-family violence (Medicina Legal), 2015-2025. |

## Cultural_violence

| Table | Rows | What it is |
|---|---:|---|
| `IdentityGroups` | 359 | Categories of victim identity as Medicina Legal records them: racial ancestry, group, indigenous people, sexual orientation, gender identity, circumstance. |
| `IdentityViolenceCases` | 145,195 | Homicides and suicides per municipality, year and identity category. |
| `CulturalViolenceIndex` | 12,350 | Homicide of Black, Indigenous and Mulatto victims, of members of vulnerable groups, and socio-political homicide. |

## GENDER_VIOLENCE

| Table | Rows | What it is |
|---|---:|---|
| `GenderViolenceIndex` | 12,350 | Partner and sexual violence per 100,000 inhabitants; homicide and suicide of women per 100,000 women. |

## Structural_Violence

| Table | Rows | What it is |
|---|---:|---|
| `Census2018Municipal` | 1,122 | DANE census 2018 per municipality: IPM (census source) and its 15 deprivations, NBI and components, floors, public services including internet, people by energy stratum. |
| `Inequality` | 0 | Empty: no municipal Gini is published yearly. Documented gap. |
| `SchoolsByMunicipality` | 18,817 | MEN directory: establishments, sites and enrolment by municipality, year and sector, 2015-2025. |
| `HealthSites` | 2,914 | MinSalud REPS: registered health sites by municipality, class of provider and legal nature. |
| `StructuralViolenceIndex` | 1,122 | Census 2018 deprivation (IPM, NBI, no internet) and lack of health sites. |

## Education_Outcomes

| Table | Rows | What it is |
|---|---:|---|
| `ExamPeriods` | 45 | Saber 11 periods, calendar, scale (the exam changed in 2014-2) and government in office. |
| `MunicipalScores` | 25,717 | Saber 11 per municipality of the school, period and sex, 2010-2022 (ICFES API): students and mean scores, and z-scores against the national mean and SD of the period. |
| `Schools` | 13,222 | Schools seen in the Saber 11 microdata: DANE code, name, municipality, sector (official or not) and area (urban or rural), as the newest file that names each school records them. 796 have no area. |
| `MunicipalScoresMicro` | 28,232 | Saber 11 per municipality and period from the microdata, 2000-2022: students, mean and z-score of mathematics and of the global score: ICFES's own since 2014-2, the simple mean of the five tests before. |
| `Students` | 11,817,681 | Each exam taker, 2000-1 to 2022-2 (ICFES period files). |
| `StudentScores` | 11,817,681 | Each exam taker's scores; before 2014-2 sciences and social are means of the old areas. global_mean, the simple mean of the five tests, exists for every period. |
| `EnrolmentAndDropout` | 15,704 | MEN: net enrolment, dropout, approval, repetition per municipality, 2011-2024. |
| `SaberProByMunicipality` | 12,804 | Saber Pro 2018-2022 by the municipality of the school the student finished: the other side of the door. |
| `HigherEdEnrolment` | 9,481 | MEN higher-education enrolment by municipality where the programme is offered, 2015-2021. |
| `GeneracionE` | 3,336 | Generacion E beneficiaries by municipality, 2021 cut-offs. |
| `IcetexCredits` | 13,855 | ICETEX new credits and renewals by department of origin (no municipality is published). |

## Student_Context

| Table | Rows | What it is |
|---|---:|---|
| `StudentHousehold` | 11,817,681 | What each exam taker reports about home; each period asked different questions, so blanks mean not asked. |
| `StudentPractices` | 4,440,331 | Books at home, daily reading, internet use (asked since the 2010s). |
| `MunicipalStudentContext` | 12,633 | What a municipality's exam takers report, 2010-2022 (ICFES API): internet, computer, car, washing machine, stratum 1-2, mother's education. |

## Sources and coverage

| Source | Dataset | Description | From | To | Preliminary |
|---|---|---|---|---|---|
| medicina_legal | 2kpj-cktv | Medicina Legal, homicide |  |  | 1 |
| medicina_legal | 79dd-d24f | Medicina Legal, violence_children |  |  | 1 |
| medicina_legal | 9fs6-37ea | Medicina Legal, partner_violence |  |  | 0 |
| medicina_legal | ers2-kerr | Medicina Legal, violence_children |  |  | 0 |
| medicina_legal | f75u-mirk | Medicina Legal, suicide |  |  | 0 |
| medicina_legal | hyqu-diue | Medicina Legal, sexual_violence |  |  | 0 |
| medicina_legal | vtub-3de2 | Medicina Legal, homicide |  |  | 0 |
| police | ('bz43-8ahq', 'cantidad') | Police, sexual_violence |  |  | 0 |
| police | ('gepp-dxcs', 'cantidad') | Police, domestic_violence |  |  | 0 |
| police | ('m8fd-ahd9', 'cantidad') | Police, homicide |  |  | 0 |
| police | u8eq-92tb | Police, massacres | 2022-01-02 | 2026-09-30 | 0 |
| cnmh | 39qq-a72j | CNMH SIEVCAC, act of war | 1946-02-02 | 2026-03-31 | 0 |
| cnmh | 3xsy-8xcp | CNMH SIEVCAC, attack on a town | 1948-04-09 | 2026-03-31 | 0 |
| cnmh | 9r7i-ek3s | CNMH SIEVCAC, forced disappearance | 1948-02-13 | 2026-03-31 | 0 |
| cnmh | cdw6-jexv | CNMH SIEVCAC, kidnapping | 1946-03-15 | 2026-03-31 | 0 |
| cnmh | d78j-f66e | CNMH SIEVCAC, massacre | 1947-03-16 | 2026-03-31 | 0 |
| cnmh | grup-7tjb | CNMH SIEVCAC, landmines and explosive remnants | 1953-01-31 | 2026-03-31 | 0 |
| cnmh | hzd2-7ea7 | CNMH SIEVCAC, recruitment of children and adolescents | 1962-07-01 | 2026-03-31 | 0 |
| cnmh | k9qg-2svz | CNMH SIEVCAC, sexual violence | 1947-04-20 | 2026-03-31 | 0 |
| cnmh | sysu-pezb | CNMH SIEVCAC, selective killing | 1944-07-07 | 2026-03-31 | 0 |
| cnmh | x27p-cm5t | CNMH SIEVCAC, damage to civilian property | 1945-10-07 | 2026-03-31 | 0 |
| cnmh | yfd7-8c9d | CNMH SIEVCAC, terrorist attack | 1944-08-03 | 2026-03-31 | 0 |
| indepaz | indepaz-masacres | INDEPAZ massacre list (web page) | 2020-01-05 | 2026-10-05 | 0 |
| dane | anexo-censal-pobreza-municipal-2018.xlsx | DANE census 2018 |  |  | 0 |
| dane | CNPV-2018-NBI.xlsx | DANE census 2018 |  |  | 0 |
| dane | DCD-area-proypoblacion-Mun-1995-2004.xlsx | DANE population projections |  |  | 0 |
| dane | DCD-area-proypoblacion-Mun-2005-2017_VP.xlsx | DANE population projections |  |  | 0 |
| dane | DCD-area-sexo-edad-proypoblacion-Mun-1995-2004.xlsx | DANE population projections |  |  | 0 |
| dane | DCD-area-sexo-edad-proypoblacion-Mun-2005-2017_VP.xlsx | DANE population projections |  |  | 0 |
| dane | PPED-AreaMun-2018-2042_VP.xlsx | DANE population projections |  |  | 0 |
| dane | PPED-AreaSexoEdadMun-2018-2042_VP.xlsx | DANE population projections |  |  | 0 |
| dane | VIVIENDAS_Cuadros_CNPV_2018.XLSX | DANE census 2018 |  |  | 0 |
| icfes | kgxf-xxbe | Saber 11 results 2010-2022 |  |  | 0 |
| icfes | u37r-hjmu | Saber Pro results 2018-2022 |  |  | 0 |
| men | 5wck-szir | MEN higher-education enrolment |  |  | 0 |
| men | 6sqn-9wh9 | MEN Generacion E beneficiaries |  |  | 0 |
| men | cfw5-qzt5 | MEN directory of schools |  |  | 0 |
| men | nudc-7mev | MEN enrolment and dropout by municipality |  |  | 0 |
| minsalud | c36g-9fc2 | REPS health providers and sites |  |  | 0 |
| icetex | f673-3gn8 | ICETEX new beneficiaries |  |  | 0 |
| icetex | nvcf-b8a3 | ICETEX renewals |  |  | 0 |

## Coverage by year

Rows (or cases) per source and year.

| | 2002 | 2003 | 2004 | 2005 | 2006 | 2007 | 2008 | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Medicina Legal cases |  |  |  |  |  |  |  |  |  |  |  |  |  | 110k | 112k | 115k | 119k | 118k | 79k | 91k | 105k | 110k | 100k | 97k | 55k |
| Police cases |  | 38k | 35k | 35k | 43k | 43k | 43k | 48k | 45k | 51k | 60k | 60k | 74k | 110k | 133k | 141k | 149k | 167k | 162k | 177k | 153k | 161k | 181k | 186k | 156k |
| CNMH events | 30k | 25k | 19k | 14k | 9,514 | 7,930 | 5,857 | 6,432 | 5,077 | 4,478 | 5,580 | 4,438 | 2,733 | 1,629 | 960 | 1,935 | 1,347 | 1,041 | 976 | 747 | 1,444 | 1,093 | 1,237 | 1,158 | 47 |
| INDEPAZ massacres |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 91 | 96 | 94 | 93 | 76 | 78 | 97 |
| Police massacres |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 93 | 100 | 87 | 90 | 82 |
| Saber 11 students |  |  |  |  |  |  |  |  | 571k | 572k | 581k | 576k | 569k | 568k | 561k | 559k | 20k | 559k | 15k | 16k | 553k |  |  |  |  |
| Saber 11 microdata | 434k | 355k | 431k | 451k | 472k | 502k | 506k | 525k | 571k | 572k | 581k | 576k | 569k | 568k | 561k | 559k | 562k | 567k | 520k | 549k | 553k |  |  |  |  |
| Saber Pro students |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 157k | 172k | 168k | 167k | 150k |  |  |  |  |
| MEN enrolment/dropout |  |  |  |  |  |  |  |  |  | 1,122 | 1,122 | 1,122 | 1,122 | 1,122 | 1,122 | 1,122 | 1,122 | 1,122 | 1,121 | 1,121 | 1,121 | 1,121 | 1,122 |  |  |
| Population | 40.2M | 40.7M | 41.2M | 41.7M | 42.2M | 42.7M | 43.1M | 43.6M | 44.1M | 44.6M | 45.0M | 45.4M | 45.9M | 46.3M | 46.8M | 47.4M | 48.3M | 49.3M | 50.4M | 51.1M | 51.6M | 52.1M | 52.6M | 53.1M | 53.4M |

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
