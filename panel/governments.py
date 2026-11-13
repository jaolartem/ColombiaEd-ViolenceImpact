"""
Presidential terms, for comparing long-term trends by government.

Every term starts on 7 August. Santos II is also split at the signing of the final peace agreement with
the FARC-EP (24 November 2016): `phase` keeps the negotiation and the implementation apart.
"""
from datetime import date

import pandas as pd

TERMS = [
    ("uribe_1", "Álvaro Uribe I", date(2002, 8, 7), date(2006, 8, 7)),
    ("uribe_2", "Álvaro Uribe II", date(2006, 8, 7), date(2010, 8, 7)),
    ("santos_1", "Juan Manuel Santos I", date(2010, 8, 7), date(2014, 8, 7)),
    ("santos_2", "Juan Manuel Santos II", date(2014, 8, 7), date(2018, 8, 7)),
    ("duque", "Iván Duque", date(2018, 8, 7), date(2022, 8, 7)),
    ("petro", "Gustavo Petro", date(2022, 8, 7), date(2026, 8, 7)),
]
PEACE_AGREEMENT = date(2016, 11, 24)
PHASES = [
    ("uribe_1", TERMS[0][2], TERMS[0][3]),
    ("uribe_2", TERMS[1][2], TERMS[1][3]),
    ("santos_1", TERMS[2][2], TERMS[2][3]),
    ("santos_2_negotiation", TERMS[3][2], PEACE_AGREEMENT),
    ("santos_2_implementation", PEACE_AGREEMENT, TERMS[3][3]),
    ("duque", TERMS[4][2], TERMS[4][3]),
    ("petro", TERMS[5][2], TERMS[5][3]),
]
ORDER = [t[0] for t in TERMS]
PHASE_ORDER = [p[0] for p in PHASES]


def _lookup(day: date, periods) -> str:
    for key, start, end in periods:
        if start <= day < end:
            return key
    return None


def government(day: date) -> str:
    return _lookup(day, [(k, s, e) for k, _, s, e in TERMS])


def phase(day: date) -> str:
    return _lookup(day, PHASES)


def days_in(year: int, start: date, end: date) -> int:
    """Days of calendar `year` that fall inside [start, end)."""
    lo, hi = max(date(year, 1, 1), start), min(date(year + 1, 1, 1), end)
    return max((hi - lo).days, 0)


def person_years(population: pd.DataFrame, periods, coverage_start: date, coverage_end: date) -> pd.DataFrame:
    """
    Person-years lived in each municipality during each period, counting only the days the data covers.
    `population` has cod_mpio, year, population (DANE mid-year estimate).
    """
    rows = []
    for key, start, end in periods:
        start, end = max(start, coverage_start), min(end, coverage_end)
        for year in range(start.year, end.year + 1):
            share = days_in(year, start, end) / (366 if year % 4 == 0 else 365)
            if share:
                rows.append((key, year, share))
    shares = pd.DataFrame(rows, columns=["period", "year", "share"])
    merged = population.merge(shares, on="year")
    merged["person_years"] = merged["population"] * merged["share"]
    return merged.groupby(["cod_mpio", "period"], as_index=False)["person_years"].sum()
