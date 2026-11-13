# Data Science Project: Exploring the Relationship between Violence and Colombian Saber Test Results

In this repository, we delve into the intricate world of violence and its potential impact on educational outcomes, as represented by the Saber tests in Colombia. Employing rigorous data analysis methodologies and a systematic approach, this project seeks to shed light on patterns and correlations that might be instrumental for decision-makers in the educational and public policy sectors.

## :construction: Project Status: In Progress

The project has made significant strides in understanding, processing, and preparing the data for detailed analysis. While the extraction phase has been largely completed, the transformation phase is currently underway. The next steps will involve a thorough data analysis, visualization, and modeling to decipher the intricate relationship between violence and educational outcomes.

### :heavy_check_mark: Achievements So Far:

- **Modular Design**: Developed a modular and systematic approach to the ETL process, with separate modules for different file formats.
- **Data Extraction**: Successfully extracted data from multiple file formats, including CSV and TXT.
- **Database Schemas**: Designed a robust database structure with multiple schemas to represent different facets of violence.
- **File Processing**: Implemented functionalities to detect and process various file formats and backup for traceability.

### :soon: Upcoming Milestones:

1. Complete the data transformation phase, ensuring data integrity, relevance, and alignment with the database structure.
2. Load the transformed data into the designed database tables.
3. Embark on a thorough Exploratory Data Analysis (EDA) to understand patterns and correlations.
4. Apply machine learning techniques to predict or classify based on the data.
5. Visualize findings using tools like Tableau and PowerBI to provide clear and actionable insights.
6. Translate findings into geospatial representations for a holistic understanding of the data.
7. Document the complete project, including methodologies, decisions, results, and insights.

## :triangular_ruler: Research Design

Violence is measured per municipality (DANE code) and year in Galtung's terms, plus gender: **direct** (homicide, suicide, intra-family violence), **structural** (poverty, inequality, access to education and health), **cultural** (violence that targets identities) and **gender** (partner and sexual violence). Each indicator becomes a rate per 100,000, then a sub-index between fixed goalposts, and the sub-indices are combined with a geometric mean, as in the UNDP Human Development Index.

The analysis has two levels. The **municipality** carries the violence indices, built only from external sources (Medicina Legal, Police, DANE, MEN). The **student** carries the Saber 11 scores and what each student reports about home and family. The students' answers never enter a violence index, because the index is what explains the scores. They describe the students' lives and are compared with what DANE says about the same municipality. Only students who reached grade 11 take the exam, so the gap between the two sources measures who drops out.

Trends are compared by government: Uribe I and II, Santos I and II (negotiation and implementation of the peace agreement), Duque and Petro. The data model is in `Tables_and_relations.sql`.

## :inbox_tray: Getting the Data

The public datasets on datos.gov.co need no user or password. An app token (environment variable `SOCRATA_APP_TOKEN`, or `api.app_token` in `config.json`) only raises the rate limit.

```bash
pip install -r requirements.txt
python -m panel.build       # violence 2015-2026, Saber 11 2010-2022, MEN 2011-2024, DANE population
python -m panel.longterm    # Police records 2003-2026 by government, Saber 11 as z-scores
```

Both write CSV files to `output/panel/`. What each source covers, and its known problems, is written at the top of `panel/sources.py` and `panel/longterm.py`. Saber 11 before 2010 and after 2022 is only published by ICFES as files, in [DataIcfes](https://www.icfes.gov.co/investigaciones/data-icfes/).

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
