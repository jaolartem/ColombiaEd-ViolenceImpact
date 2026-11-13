# Data Science Project: Exploring the Relationship between Violence and Colombian Saber Test Results

In this repository, we delve into the intricate world of violence and its potential impact on educational outcomes, as represented by the Saber tests in Colombia. Employing rigorous data analysis methodologies and a systematic approach, this project seeks to shed light on patterns and correlations that might be instrumental for decision-makers in the educational and public policy sectors.

## :construction: Project Status: In Progress

The project has made significant strides in understanding, processing, and preparing the data for detailed analysis. While the extraction phase has been largely completed, the transformation phase is currently underway. The next steps will involve a thorough data analysis, visualization, and modeling to decipher the intricate relationship between violence and educational outcomes.

### :heavy_check_mark: Done

- **Data**: every source is read by DANE municipality code.
  - Violence: Medicina Legal, Police by day 2003-2026, CNMH conflict events in 11 modalities, INDEPAZ massacres, with the three massacre sources triangulated event by event.
  - DANE: population by sex and age 1995-2042, census 2018.
  - Education: Saber 11 aggregates and microdata 2000-2022, Saber Pro, MEN enrolment and dropout, higher education, Generacion E, ICETEX.
  - Access: schools and health sites.
- **Model**: seven schemas loaded into MariaDB, with rates by government and phase, and the physical, cultural, gender, structural and final indices.
- **Documentation**: data dictionary with coverage and the known problems of each source.

### :soon: Next

1. Define the research questions and the kind of analysis (cartography of associations, municipal trajectories, networks of co-occurrence, multilevel models as one more inscription).
2. Saber 11 2023-2025 from DataIcfes.
3. Maps by government.

## :triangular_ruler: Research Design

**The exam as an operator.** Saber 11 translates years of a student's life into a number that universities, scholarships and credits know how to read. In some places that number opens a door, and in others it does not. Violence is followed as a material effect that opens or closes those doors: a closed road, a mine on the way to school, a recruitment, a confinement, a massacre.

The project takes symmetric sociology as its frame. It assumes no structure that explains in advance. It records the associations (territory, armed actor, kind of event, school, exam, higher education, scholarship) so they can be described. Class, structure and power are where the description may arrive, Marx included; they are not where it starts.

**Galtung as the map's legend.** Harm is classified as **physical** (homicide, suicide, intra-family violence, conflict events), **cultural** (violence that targets an identity), **gender** (partner and sexual violence, homicide and suicide of women) and **structural** (avoidable deprivation and access). Each dimension has an index: rates per 100,000 become sub-indices between fixed goalposts, combined with a geometric mean as in the UNDP Human Development Index. The indices are one more inscription on the map, not the explanation.

**Two levels.** The **municipality** (DANE code) carries everything that comes from external sources. The **student** carries the scores and what each exam taker reports about home and family. The students' answers never enter an index. They are set beside what the 2018 census says about the same municipality: only those who reached grade 11 sit the exam, so the gap measures who did not.

**Time.** Every dated fact is placed in a government: Uribe I and II, Santos I and II, the latter split into negotiation and implementation of the peace agreement, Duque, and Petro. This gives the long-term comparison from 2002 to 2026.

The model is in `Tables_and_relations.sql` (seven schemas). What each table holds, its coverage and the known problems of the data are in [`docs/data_dictionary.md`](docs/data_dictionary.md).

## :inbox_tray: Getting the Data

The public datasets on datos.gov.co need no user or password. An app token (environment variable `SOCRATA_APP_TOKEN`, or `api.app_token` in `config.json`) only raises the rate limit. Each module writes CSV files to `output/panel/` and documents its sources at the top of the file.

```bash
pip install -r requirements.txt
python -m panel.build            # Medicina Legal 2015-2026, Saber 11 2010-2022 (API), MEN 2011-2024, DANE population
python -m panel.longterm         # comparison by government with the monthly Police series and CNMH massacres
python -m panel.police           # Police records by day, 2003-2026: homicide, intra-family and sexual violence
python -m panel.events           # CNMH (11 modalities), INDEPAZ and Police massacres, and their triangulation
python -m panel.identity         # homicides and suicides by the victim's identity and the circumstance
python -m panel.census           # DANE census 2018 (IPM, NBI, dwellings, stratum) and population by sex and age
python -m panel.door             # Saber Pro, higher-education enrolment, Generacion E, ICETEX
python -m panel.access           # schools (MEN) and health sites (REPS)
python -m panel.student_context  # what each municipality's exam takers report, 2010-2022
python -m panel.load_db          # everything into MariaDB/MySQL (DB_HOST, DB_USER, DB_PASS), with rates and indices
python -m panel.dataicfes --data "path/to/Saber11 files"   # Saber 11 microdata 2000-2022, one row per student
python -m panel.dictionary       # rewrites docs/data_dictionary.md from the database
```

Saber 11 microdata come from the ICFES period files (`SB11_<year><semester>`). 2023-2025 are only published on [DataIcfes](https://www.icfes.gov.co/investigaciones/data-icfes/).

## :wrench: Tools and Technologies Used

- **Python**: The backbone of the project, instrumental in data processing and analysis.
- **SQL**: For structured data storage and complex query operations.
- **Excel**: Initial data understanding and minor transformations.
- **PowerBI** (Planned): For crafting informative and interactive dashboards.
- **Tableau** (Planned): Another visualization tool to diversify representation.

## :man_teacher: About Me

Hello! I'm Jaime Olarte, a seasoned professional with expertise in quantitative research and data analysis across social, political, and educational spheres. My odyssey has been characterized by harnessing data to drive evidence-based decisions, from analyzing academic performance reports to influencing public policies. With a robust background encompassing roles like Social Sciences Teacher, Assistant Professor, and Sales & Business Trainer, I've constantly strived to bridge data with actionable insights. Proficient with tools such as SQL, Python, Excel, and Power BI, I communicate fluently in English and Spanish. Dive into my [LinkedIn](www.linkedin.com/in/jaime-andrés-olarte-martínez) for a deeper dive into my professional journey.

## :raising_hand: Contributing & Feedback

As someone passionate about data and its potential, I believe in collaborative growth. Your feedback, suggestions, or contributions can significantly enrich this project. Feel free to raise an issue or submit a pull request.
