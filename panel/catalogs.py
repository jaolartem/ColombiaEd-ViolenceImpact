"""
Catalogs for the categories the facts were storing as text, and the keys that bind them.

    python -m panel.catalogs        # also run at the end of panel.load_db

Each category that repeats is its own table and the fact points to it by key (decision 29):
- Measures: what each measure of PeriodRates is, taken apart: its source, the CNMH modality or the
  Medicina Legal / Police indicator it counts, and its unit (events, victims or cases);
- Periods: the governments and phases PeriodRates are computed over, with their keys;
- HealthProviderClasses, LegalNatures (REPS); SchoolSectors, SchoolAreas (MEN, ICFES); IcetexLevels;
  HigherEdSectors, HigherEdLevels (SNIES codes; their names wait for the SNIES codebook); SaberProPeriods.
Values written two ways are made one: the school sector 'NO OFICIAL' and 'NO_OFICIAL'; ICETEX's sex
(Femenino, Masculino, SIN INFORMACION, Intersexual) becomes the key of RelationsAndConclusions.Sexes.
"""
from panel.load_db import connect

STATEMENTS = [
    # ---- what each rate measures
    """INSERT IGNORE INTO RelationsAndConclusions.Measures (code, source_code, modality_code, indicator_id, unit)
       SELECT DISTINCT r.measure,
              SUBSTRING_INDEX(r.measure, '_', 1),
              CASE WHEN r.measure LIKE '%massacre%' THEN 'MA'
                   WHEN r.measure LIKE 'cnmh_%' THEN (SELECT m.code FROM Physical_violence.EventModalities m
                        WHERE REPLACE(r.measure, '_', ' ') LIKE CONCAT('cnmh ', m.name, '%') LIMIT 1) END,
              CASE WHEN r.measure LIKE 'police_%' AND r.measure NOT LIKE '%massacre%'
                   THEN (SELECT i.id FROM RelationsAndConclusions.ViolenceIndicators i
                         WHERE i.code = SUBSTRING(r.measure, LENGTH('police_') + 1)) END,
              CASE WHEN r.measure LIKE '%\\_events' THEN 'events' WHEN r.measure LIKE '%\\_victims' THEN 'victims' ELSE 'cases' END
       FROM RelationsAndConclusions.PeriodRates r""",
    """INSERT IGNORE INTO RelationsAndConclusions.Periods (kind, code, government_id, phase_id)
       SELECT 'government', g.code, g.id, NULL FROM RelationsAndConclusions.Governments g
       UNION ALL
       SELECT 'phase', p.code, p.government_id, p.id FROM RelationsAndConclusions.Government_Phases p""",
    # ---- REPS
    "INSERT IGNORE INTO Structural_Violence.HealthProviderClasses (name) SELECT DISTINCT provider_class FROM Structural_Violence.HealthSites",
    "INSERT IGNORE INTO Structural_Violence.LegalNatures (name) SELECT DISTINCT legal_nature FROM Structural_Violence.HealthSites",
    # ---- schools: one spelling per sector
    "UPDATE Education_Outcomes.Schools SET sector = REPLACE(sector, ' ', '_') WHERE sector LIKE '% %'",
    "INSERT IGNORE INTO Education_Outcomes.SchoolSectors (code) SELECT DISTINCT sector FROM Structural_Violence.SchoolsByMunicipality",
    "INSERT IGNORE INTO Education_Outcomes.SchoolSectors (code) SELECT DISTINCT sector FROM Education_Outcomes.Schools WHERE sector IS NOT NULL",
    "INSERT IGNORE INTO Education_Outcomes.SchoolAreas (code) SELECT DISTINCT area FROM Education_Outcomes.Schools WHERE area IS NOT NULL",
    # ---- ICETEX: sex as the model's key
    "INSERT IGNORE INTO RelationsAndConclusions.Sexes VALUES ('I', 'Intersex')",
    """UPDATE Education_Outcomes.IcetexCredits SET sex = CASE sex WHEN 'Femenino' THEN 'F' WHEN 'Masculino' THEN 'M'
                                                               WHEN 'Intersexual' THEN 'I' ELSE 'U' END
       WHERE CHAR_LENGTH(sex) > 1""",
    "INSERT IGNORE INTO Education_Outcomes.IcetexLevels (name) SELECT DISTINCT level FROM Education_Outcomes.IcetexCredits",
    # ---- SNIES and Saber Pro
    "INSERT IGNORE INTO Education_Outcomes.HigherEdSectors (id) SELECT DISTINCT sector_id FROM Education_Outcomes.HigherEdEnrolment",
    "INSERT IGNORE INTO Education_Outcomes.HigherEdLevels (id) SELECT DISTINCT level_id FROM Education_Outcomes.HigherEdEnrolment",
    """INSERT IGNORE INTO Education_Outcomes.SaberProPeriods (id, year)
       SELECT DISTINCT periodo, year FROM Education_Outcomes.SaberProByMunicipality""",
]


def build(cur):
    for sql in STATEMENTS:
        cur.execute(sql)
    for table in ("RelationsAndConclusions.Measures", "RelationsAndConclusions.Periods",
                  "Structural_Violence.HealthProviderClasses", "Structural_Violence.LegalNatures",
                  "Education_Outcomes.SchoolSectors", "Education_Outcomes.SchoolAreas", "Education_Outcomes.IcetexLevels",
                  "Education_Outcomes.HigherEdSectors", "Education_Outcomes.HigherEdLevels", "Education_Outcomes.SaberProPeriods"):
        cur.execute(f"SELECT COUNT(*) FROM {table}")
        print(f"  {table:<45} {cur.fetchone()[0]:>6,}")
    cur.execute("SELECT code FROM RelationsAndConclusions.Measures WHERE source_code = 'cnmh' AND modality_code IS NULL")
    left = [r[0] for r in cur.fetchall()]
    if left:
        print("  CNMH measures without a modality:", left)


def main():
    db = connect()
    cur = db.cursor()
    build(cur)
    db.commit()
    db.close()


if __name__ == "__main__":
    main()
