# Review of the data model

The model is in `Tables_and_relations.sql`. Its rules (decision 29 in `research/decisions.csv`):

- **Third normal form at least.** Every kind of thing is its own table and everything said of it depends
  only on its key. A category that repeats (a sector, a level, a type) is a catalog with its own key.
- **Every connection is its own table, in fourth normal form.** A relation between two things holds
  only the two keys and what belongs to that relation (its validity, who coded it). Two independent
  many-valued facts about the same thing never share a table.
- **What changes in time carries its validity**, or its year.
- **Nothing reaches the model without its source's validation** (decision 24); what fails is annotated in
  `RelationsAndConclusions.DataQualityFlags`.

## The schemas

| Schema | What it holds |
|---|---|
| `RelationsAndConclusions` | place (departments, municipalities, lineage of split municipalities), population, time (governments, phases), sources, Medicina Legal and Police cases, rates by period, the final index, data quality |
| `Physical_violence` | conflict events (CNMH, INDEPAZ, Police), modalities, perpetrators, triangulation links, physical index |
| `Cultural_violence` | identity groups and violence against them, cultural index |
| `GENDER_VIOLENCE` | gender index |
| `Structural_Violence` | census 2018, schools and health sites by municipality, inequality, structural index |
| `Education_Outcomes` | Saber 11 (students, scores, schools, periods, municipal aggregates), Saber Pro, MEN, higher education, scholarships, certified entities and who runs each municipality's education |
| `Student_Context` | what each exam taker reports; municipal aggregates |
| `Territorial_Context` | DNP TerriData (every indicator per municipality and department) and CUIPO (income and spending) |
| `State_Action` | the State as a network: entities, their jurisdictions, functions and successions; norms, provisions, literal excerpts; the coding of responsibilities, objectives, problems and resources, and their connections |
| `Research_Design` | the decision log, the municipal typology and the cases chosen from it |

## What is in order

- Place, time, population, cases and events are keyed by DANE code, year or day and catalogs
  (`Sexes`, `ViolenceIndicators`, `EventModalities`, `Perpetrators`, `IdentityGroups`, `ExamPeriods`).
- Students, scores, household and practices are one row per student, keyed by the student.
- TerriData values are keyed by place, indicator, year and month; categories are a catalog
  (`TerriDataCategories`); department figures have their own table.
- CUIPO accounts, funding sources and sectors are catalogs; income and spending are keyed by
  municipality, period, account or sector, and funding source.
- `State_Action` and `Research_Design` follow the rules above: every connection is its own table, and in
  `State_Action` the coder is part of each connection's key, so two readings can be compared.

## What is not, and how it is fixed

| # | Where | Problem | Fix |
|---|---|---|---|
| 1 | `Physical_violence.ViolenceEvents` | CNMH names the perpetrator at two levels (category and group) and up to eleven acts committed with each event; only the category and two acts were kept, as columns | catalog `PerpetratorGroups` under `Perpetrators`; catalog `SimultaneousActs` and connection `EventSimultaneousActs (event_id, act_id, persons, form_id)`, forms in `ActForms` (`panel.event_details`) |
| 2 | `Education_Outcomes.Students.school_id` | no foreign key to `Schools` | add the key; schools seen only in the students are already in `Schools` |
| 3 | `Education_Outcomes.Schools.sector`, `.area`; `Structural_Violence.SchoolsByMunicipality.sector` | free text | catalogs `SchoolSectors`, `SchoolAreas` |
| 4 | `Education_Outcomes.Schools` | an establishment and its sites (sedes) are one thing | `Schools` (establishment) and `SchoolSites` (sede) from the MEN directory; schools as entities in `State_Action.StateEntities` (kind school) |
| 5 | `Structural_Violence.HealthSites.provider_class`, `.legal_nature` | free text inside the key | catalogs `HealthProviderClasses`, `LegalNatures` |
| 6 | `Education_Outcomes.IcetexCredits.sex`, `.level`, `.kind` | free text inside the key; sex does not point to `Sexes` | catalogs and the key to `Sexes` |
| 7 | `Education_Outcomes.HigherEdEnrolment.sector_id`, `.level_id` | codes without a catalog | catalogs `HigherEdSectors`, `HigherEdLevels` |
| 8 | `RelationsAndConclusions.PeriodRates.measure` | the name carries source, modality and unit (`cnmh_massacre_victims`); `period_code` is text with no key to `Governments` or `Government_Phases` | catalog `Measures (id, source_id, modality_code, indicator_id, unit)`; a `Periods` table (kind, government, phase) referenced by key |
| 9 | `Territorial_Context.TerriDataIndicators.dimension`, `.subcategory` | the dimension depends on the subcategory, which depends on the indicator (transitive) | catalogs `TerriDataDimensions`, `TerriDataSubcategories` |
| 10 | `RelationsAndConclusions.DataQualityFlags.source` | text, not a key to `Sources`; DNP, CUIPO and the MEN directory are not in `Sources` | add them to `Sources` and reference by key |
| 11 | `Student_Context.StudentHousehold`, `StudentPractices` | the raw answer of each period: education of the mother has 34 spellings and codes, ethnicity 49 | per variable a catalog of harmonised categories, and a connection `ResponseMap (period, raw answer, category)`; numeric codes of 2000-2009 wait for the ICFES dictionaries |
| 12 | `Education_Outcomes.MunicipalScores` and `MunicipalScoresMicro` | the same fact twice (ICFES API and microdata) | the microdata are canonical; the API table stays only as a check, documented as such |
| 13 | `Education_Outcomes.CertifiedEntities` | a certified entity is a State entity | becomes a view over `State_Action.StateEntities` (kind education secretariat) once that table is filled |
| 14 | `Education_Outcomes.SaberProByMunicipality.periodo` | period without a catalog | a Saber Pro periods catalog |

Done:
- 1: 83 armed groups under their categories; 122,989 event-act connections; displacement and confinement
  moved from columns of `ViolenceEvents` into the connection.
- 2: students point to their school by key, with no orphans.
- 3, 5, 6, 7, 8, 14: catalogs filled from the data by `panel.catalogs` (also at the end of `panel.load_db`)
  and every fact points to them by key. `Measures` takes each measure apart (source, modality or indicator,
  unit); `Periods` keys the governments and phases. The school sector was written two ways and is now one;
  ICETEX's sex is the key of `Sexes`, which gains 'I' (intersex). The names of the SNIES sector and level
  codes wait for the SNIES codebook.
- 10: `DataQualityFlags.source` points to `Sources.code`, with DNP and CUIPO added.
- 12: the data dictionary names the microdata as canonical.

- 9: TerriData's 24 dimensions and 134 subcategories are catalogs; each indicator points to its subcategory.

Pending: 4 (schools and their sites, from the MEN directory), 11 (the questionnaire, which needs the ICFES dictionaries for the oldest
periods) and 13 (waits for the State entities to be loaded).

## Tables of the analysis log

`DataQualityFlags` and `SmoothedValues` name the table and column they refer to as text (`source_table`,
`column_name`). That is deliberate: they are a log about any table of the model, and a foreign key cannot
point to "any table". They are not a source of facts.
