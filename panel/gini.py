"""
A municipal income Gini estimated from the Saber 11 family income brackets, checked against DANE.

    python -m panel.gini

There is no yearly municipal Gini in Colombia. DANE publishes the income Gini by department and for 23
cities (GEIH household survey; in TerriData, indicator 140010003). Saber 11 asked each exam taker's family
its monthly income in brackets of legal minimum wages (SMLV), 2009-2 to 2016-2 (Student_Context.
IncomeBrackets). From those brackets a Gini is estimated per municipality and year (decision 23):

- calendar A only (the periods ending in 2 or 4): calendar B is mostly private high-cost schools;
- each bracket is worth its midpoint in SMLV; the open bracket (10 or more) is worth the mean of a Pareto
  tail fitted each year on the two highest brackets (Parker and Fenwick's method for grouped data);
- the Gini is that of the Lorenz curve of the brackets. It ignores inequality inside each bracket, so it
  falls below the survey's Gini: what can be compared is its order and its movement, not its level;
- only families that answered, and only municipality-years with at least 30 of them;
- it describes the families with a child who reached grade 11, not the whole municipality.

Check: the same estimate for each department and each department capital, against DANE's Gini of the same
year. The correlation and the mean difference are printed and written to output/panel/gini_check.csv.

Result (2026-11-13, decision 37): the estimate failed its check (correlation 0.07 with DANE's departmental
Gini, -0.05 with the city Gini), so it is not loaded; run with --load only if a revised method passes.
Loads Structural_Violence.Inequality (measure 'saber11_income_brackets'). DANE's own Gini stays in
Territorial_Context (MunicipalIndicators for cities, DepartmentalIndicators for departments).
"""
from pathlib import Path

import numpy as np
import pandas as pd

from panel.load_db import connect, load

ROOT = Path(__file__).resolve().parent.parent
MIDPOINTS = {1: 0.5, 2: 1.5, 3: 2.5, 4: 4.0, 5: 6.0, 6: 8.5}
MIN_FAMILIES = 30
DANE_GINI = "140010003"


def query(cur, sql):
    cur.execute(sql)
    return pd.DataFrame(cur.fetchall(), columns=[d[0] for d in cur.description])


def top_mean(counts: pd.Series) -> float:
    """Mean of the open bracket (10+ SMLV) from a Pareto tail through the 7-10 and 10+ brackets."""
    above7, above10 = counts.get(6, 0) + counts.get(7, 0), counts.get(7, 0)
    if above10 <= 0 or above7 <= above10:
        return 15.0
    alpha = np.log(above7 / above10) / np.log(10 / 7)
    return float(alpha * 10 / (alpha - 1)) if alpha > 1.05 else 15.0


def gini(counts: pd.Series, top: float) -> float:
    """Gini of grouped data: households per bracket, each bracket at its value."""
    values = pd.Series({**MIDPOINTS, 7: top})
    c = counts.reindex(values.index, fill_value=0).astype(float)
    if c.sum() == 0:
        return np.nan
    p = c / c.sum()
    income = p * values
    lorenz = (income.cumsum() / income.sum()).values
    prev = np.concatenate([[0], lorenz[:-1]])
    return float(1 - np.sum(p.values * (lorenz + prev)))


def main():
    db = connect()
    cur = db.cursor()
    h = query(cur, """
        SELECT s.exam_period_id DIV 10 year, s.municipality_id, m.department_id, h.income_bracket_id bracket, COUNT(*) n
        FROM Education_Outcomes.Students s
        JOIN Student_Context.StudentHousehold h ON h.student_id = s.id
        JOIN RelationsAndConclusions.Municipalities m ON m.id = s.municipality_id
        WHERE h.income_bracket_id IS NOT NULL AND s.exam_period_id % 10 IN (2, 4)
        GROUP BY 1, 2, 3, 4""")
    h["n"] = h["n"].astype(int)
    tops = {y: top_mean(g.groupby("bracket")["n"].sum()) for y, g in h.groupby("year")}
    print("  open bracket worth (SMLV):", {int(y): round(v, 1) for y, v in tops.items()})

    rows = []
    for (y, m), g in h.groupby(["year", "municipality_id"]):
        c = g.set_index("bracket")["n"]
        rows.append((int(m), int(y), gini(c, tops[y]) if c.sum() >= MIN_FAMILIES else np.nan, int(c.sum())))
    mun = pd.DataFrame(rows, columns=["municipality_id", "year", "gini", "households"])
    dep = pd.DataFrame([(int(d), int(y), gini(g.groupby("bracket")["n"].sum(), tops[y]))
                        for (y, d), g in h.groupby(["year", "department_id"])], columns=["department_id", "year", "estimate"])

    dane_dep = query(cur, f"SELECT department_id, year, value dane FROM Territorial_Context.DepartmentalIndicators "
                          f"WHERE indicator_code = '{DANE_GINI}'")
    dane_city = query(cur, f"SELECT municipality_id, year, value dane FROM Territorial_Context.MunicipalIndicators "
                           f"WHERE indicator_code = '{DANE_GINI}'")
    checks = []
    for label, est, ref, key in (("departments", dep, dane_dep, "department_id"),
                                 ("cities", mun.rename(columns={"gini": "estimate"}), dane_city, "municipality_id")):
        both = est.merge(ref, on=[key, "year"]).dropna()
        both["dane"] = both["dane"].astype(float)
        r = both[["estimate", "dane"]].corr().iloc[0, 1]
        within = both.groupby("year")[["estimate", "dane"]].corr().xs("estimate", level=1)["dane"].mean()
        print(f"  {label}: {len(both)} place-years; correlation {r:.2f} (within each year {within:.2f}); "
              f"estimate {both['estimate'].mean():.3f} against DANE {both['dane'].mean():.3f}")
        checks.append(both.assign(level=label).rename(columns={key: "place_id"}))
    pd.concat(checks).to_csv(ROOT / "output" / "panel" / "gini_check.csv", index=False)

    import sys
    if "--load" not in sys.argv:                    # decision 37: the estimate did not pass its check
        db.close()
        return
    cur.execute("SET FOREIGN_KEY_CHECKS = 0")
    cur.execute("DELETE FROM Structural_Violence.Inequality WHERE measure = 'saber11_income_brackets'")
    load(cur, "Structural_Violence.Inequality", mun.dropna(subset=["gini"]).assign(measure="saber11_income_brackets"),
         ["municipality_id", "year", "measure", "gini", "households"])
    cur.execute("SET FOREIGN_KEY_CHECKS = 1")
    db.commit()
    db.close()


if __name__ == "__main__":
    main()
