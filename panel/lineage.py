"""
Split municipalities: who comes from whom, and territories whose borders do not change.

    python -m panel.lineage

DANE's population series show when a municipality is born (its first year with population after years at
zero or absent) and when one disappears (zero after years with population). The territory came from, or
went to, municipalities of the same department that in that year lost (or gained) population against
their own trend: expected = last year's population times last year's growth.

- Lineage (RelationsAndConclusions.MunicipalLineage): only clear cases, where one municipality explains
  the change (its loss is 0.6 to 1.6 times the newborn's population) and no other municipality of the
  department was born that year. Evidence 'inferred_population' until DANE's DIVIPOLA confirms it.
  The rest are annotated in DataQualityFlags (source dane, missing) with their candidates.
- Constant territories (ConstantTerritories, ConstantTerritoryMembers): every municipality whose borders
  changed together with another's, joined: the newborn and every municipality of its department that lost
  at least half the newborn's population that year (and, for a disappearance, every one that gained at
  least half of it). The union has the same borders every year, so its series do not break; when the
  exact mother is unknown the territory is only larger. Municipalities that never changed are territories
  of their own.

Two readings follow (decision 25): the territory as it was each year (the original tables) and the constant
territory (views PopulationConstantTerritory, PeriodRatesConstantTerritory).
"""
import numpy as np
import pandas as pd

from panel.load_db import connect, load


def query(cur, sql):
    cur.execute(sql)
    return pd.DataFrame(cur.fetchall(), columns=[d[0] for d in cur.description])


def expected(w, m, y):
    """Population of m in year y had nothing happened: last year's times last year's growth."""
    prev = w.loc[m, y - 1]
    before = w.loc[m, y - 2] if (y - 2) in w.columns else np.nan
    growth = prev / before if before and before > 0 else 1.0
    return prev * growth


def main():
    db = connect()
    cur = db.cursor()
    p = query(cur, """SELECT p.municipality_id mun, p.year, p.population pop, m.name, m.department_id dept
                      FROM RelationsAndConclusions.Population p
                      JOIN RelationsAndConclusions.Municipalities m ON m.id = p.municipality_id""")
    p["pop"] = p["pop"].astype(float)
    w = p.pivot_table(index="mun", columns="year", values="pop")
    info = p.drop_duplicates("mun").set_index("mun")[["name", "dept"]]
    events = []                                   # (municipality, year, kind, population)
    for m, row in w.iterrows():
        s = row.dropna()
        alive = s > 0
        for y in s.index[1:]:
            if alive[y] and not alive[y - 1]:
                events.append((m, y, "born", s[y]))
            if not alive[y] and alive[y - 1]:
                events.append((m, y, "gone", s[y - 1]))
        if s.index[0] > w.columns[0] and alive.iloc[0]:          # appears in the series already alive
            pass
    ev = pd.DataFrame(events, columns=["mun", "year", "kind", "pop"])
    ev["dept"] = ev["mun"].map(info["dept"])

    links, flags, unions = [], [], []
    for (dept, year), group in ev.groupby(["dept", "year"]):
        peers = [m for m in info.index[info["dept"] == dept]
                 if m not in set(group["mun"]) and (year - 1) in w.columns and w.loc[m, year - 1] > 0]
        for _, e in group.iterrows():
            change = {}
            for m in peers:
                diff = expected(w, m, year) - w.loc[m, year]          # loss for a birth
                change[m] = diff if e["kind"] == "born" else -diff     # gain for a disappearance
            ratio = {m: c / e["pop"] for m, c in change.items()}
            candidates = sorted([m for m, r in ratio.items() if r >= 0.5], key=lambda m: -ratio[m])
            unions.append([e["mun"], *candidates])
            clear = (len(group) == 1 and len(candidates) == 1 and 0.6 <= ratio[candidates[0]] <= 1.6)
            if e["kind"] == "born" and clear:
                links.append((e["mun"], candidates[0], int(year)))
            else:
                names = ", ".join(f"{info.loc[m, 'name']} ({ratio[m]:.2f})" for m in candidates[:4]) or "none"
                verb = "born" if e["kind"] == "born" else "disappears"
                flags.append((int(e["mun"]), str(year), float(e["pop"]),
                              f"{verb}; candidates by population change (ratio to its population): {names}"[:200]))

    # connected components: every group of municipalities whose borders changed together
    parent = {m: m for m in info.index}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for u in unions:
        for m in u[1:]:
            parent[find(m)] = find(u[0])
    comp = pd.Series({m: find(m) for m in info.index})
    ids = {root: i + 1 for i, root in enumerate(sorted(comp.unique()))}
    members = pd.DataFrame({"territory_id": comp.map(ids).values, "municipality_id": comp.index})
    size = members.groupby("territory_id")["municipality_id"].transform("size")
    names = members.assign(name=members["municipality_id"].map(info["name"])) \
        .sort_values("municipality_id").groupby("territory_id")["name"].agg(" + ".join)
    territories = pd.DataFrame({"id": names.index, "name": names.str.slice(0, 255).values})
    lineage = pd.DataFrame(links, columns=["daughter_id", "mother_id", "created_in"]).assign(evidence="inferred_population")
    fl = pd.DataFrame(flags, columns=["municipality_id", "period", "value", "note"]).assign(
        source="dane", source_table="MunicipalLineage", column_name="mother_id", kind="missing")

    cur.execute("DELETE FROM RelationsAndConclusions.DataQualityFlags WHERE source = 'dane' AND source_table = 'MunicipalLineage'")
    cur.execute("SET FOREIGN_KEY_CHECKS = 0")
    for t in ("MunicipalLineage", "ConstantTerritoryMembers", "ConstantTerritories"):
        cur.execute(f"TRUNCATE TABLE RelationsAndConclusions.{t}")
    load(cur, "RelationsAndConclusions.MunicipalLineage", lineage, ["daughter_id", "mother_id", "created_in", "evidence"])
    load(cur, "RelationsAndConclusions.ConstantTerritories", territories, ["id", "name"])
    load(cur, "RelationsAndConclusions.ConstantTerritoryMembers", members, ["territory_id", "municipality_id"])
    if len(fl):
        load(cur, "RelationsAndConclusions.DataQualityFlags", fl,
             ["source", "source_table", "column_name", "municipality_id", "period", "kind", "value", "note"])
    cur.execute("SET FOREIGN_KEY_CHECKS = 1")
    db.commit()
    print(f"  {len(ev)} births and disappearances; {len(lineage)} clear lineages; {len(fl)} left for DIVIPOLA; "
          f"{int((size > 1).groupby(members['territory_id']).first().sum())} territories join more than one municipality")
    db.close()


if __name__ == "__main__":
    main()
