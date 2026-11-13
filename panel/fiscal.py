"""
The money of each municipality, as reported to CUIPO, 2023 onwards.

    python -m panel.fiscal

CUIPO (Categoria Unica de Informacion del Presupuesto Ordinario) is the budget report every territorial
entity files each quarter to the Contaduria General de la Nacion and the Contraloria General de la
Republica. The Contraloria publishes it on datos.gov.co:
- 9axr-9gnb, execution of income: what was collected, by account and funding source;
- 4f7r-epif, execution of expenditure: commitments, obligations and payments, by sector and funding source.
Each quarter is cumulative, so only the year-end close (YYYY1201) and the latest quarter are kept.

The entity code is CHIP's nine digits; for municipalities its last five are the DANE code
(211054810 is Tibu, 54810). The account plan is a tree: every level is the sum of the ones below it
(1 income, 1.1 current income, 1.1.01 tax income, 1.1.02.06.001 SGP, 1.1.02.06.001.01 SGP education ...).
All levels are kept, with their depth, so any level can be read without adding.

Before 2023 the same money is in DNP's TerriData (panel.dnp), dimension "Finanzas publicas", 2000-2024:
income, tax income, transfers, royalties, investment by sector, SGP allocations by sector and the
fiscal performance index.

Loads Territorial_Context.CuipoAccounts, CuipoFundingSources, CuipoSectors, MunicipalIncome and
MunicipalSpending.
"""
import pandas as pd

from panel import dane
from panel.load_db import connect, load
from panel.socrata import app_token, query

INCOME, SPENDING = "9axr-9gnb", "4f7r-epif"


def periods(dataset):
    p = query(dataset, "periodo", where="ambito_nombre='Municipios'", group="periodo", token=app_token())["periodo"]
    p = sorted(p)
    keep = [x for x in p if x.endswith("1201")]
    if p[-1] not in keep:
        keep.append(p[-1])                              # the latest quarter, while the year is open
    return keep


def municipality(code: pd.Series) -> pd.Series:
    return dane.normalize_code(code.str[-5:])


def income():
    frames = []
    for per in periods(INCOME):
        df = query(INCOME, "periodo, codigo_entidad, cuenta, nombre_cuenta, cod_fuentes_financiacion, "
                           "nom_fuentes_financiacion, sum(total_recaudo) as collected",
                   where=f"ambito_nombre='Municipios' AND periodo='{per}'",
                   group="periodo, codigo_entidad, cuenta, nombre_cuenta, cod_fuentes_financiacion, nom_fuentes_financiacion",
                   token=app_token())
        print(f"  income {per}: {len(df):,} rows", flush=True)
        frames.append(df)
    return pd.concat(frames, ignore_index=True)


def spending():
    """Twelve million rows do not aggregate in one request: one query per period and department."""
    departments = sorted({c[:2] for c in dane.municipalities()["cod_mpio"]})
    frames = []
    for per in periods(SPENDING):
        n = 0
        for d in departments:
            df = query(SPENDING, "periodo, codigo_entidad, cod_sector, nom_sector, cod_fuentes_financiacion, "
                                 "nom_fuentes_financiacion, sum(compromisos) as commitments, sum(obligaciones) as obligations, "
                                 "sum(pagos) as payments",
                       where=f"ambito_nombre='Municipios' AND periodo='{per}' AND codigo_entidad like '%{d}___'",
                       group="periodo, codigo_entidad, cod_sector, nom_sector, cod_fuentes_financiacion, nom_fuentes_financiacion",
                       token=app_token())
            n += len(df)
            frames.append(df)
        print(f"  spending {per}: {n:,} rows", flush=True)
    return pd.concat(frames, ignore_index=True)


def validate(inc, spe):
    """CUIPO's own rules, checked before anything is loaded.
    - negative pesos collected or spent: error, not loaded;
    - payments above obligations, or obligations above commitments: inconsistent, loaded and annotated;
    - a parent account that differs by more than 1% from the sum of its children: inconsistent, annotated."""
    flags = []

    def add(df, mask, table, column, kind, value, note):
        if mask.any():
            f = df[mask]
            flags.append(pd.DataFrame({"source": "CUIPO", "source_table": table, "column_name": column,
                                       "municipality_id": f["municipality_id"], "period": f["period"].astype(str),
                                       "kind": kind, "value": value[mask], "note": note if isinstance(note, str) else note[mask]}))

    neg = inc["collected"] < 0
    add(inc, neg, "MunicipalIncome", inc["cuenta"], "error", inc["collected"], "negative collection; not loaded")
    inc = inc[~neg]
    neg = (spe[["commitments", "obligations", "payments"]] < 0).any(axis=1)
    add(spe, neg, "MunicipalSpending", spe["cod_sector"], "error", spe["payments"], "negative spending; not loaded")
    spe = spe[~neg]
    tol = lambda a, b: a > b * 1.01 + 1
    bad = tol(spe["payments"], spe["obligations"]) | tol(spe["obligations"], spe["commitments"])
    add(spe, bad, "MunicipalSpending", spe["cod_sector"], "inconsistent", spe["payments"],
        "payments above obligations or obligations above commitments")
    # the account tree: each parent is the sum of its children (all funding sources together)
    tot = inc.groupby(["municipality_id", "period", "cuenta"], as_index=False)["collected"].sum()
    tot["parent"] = tot["cuenta"].str.rsplit(".", n=1).str[0].where(tot["cuenta"].str.contains(r"\."))
    kids = tot.dropna(subset=["parent"]).groupby(["municipality_id", "period", "parent"], as_index=False)["collected"].sum()
    kids = kids.rename(columns={"parent": "cuenta", "collected": "children"})
    tree = tot.merge(kids, on=["municipality_id", "period", "cuenta"])
    off = (tree["collected"] - tree["children"]).abs() > 0.01 * tree["collected"].abs() + 1000
    add(tree, off, "MunicipalIncome", tree["cuenta"], "inconsistent", tree["collected"],
        "children add up to " + tree["children"].round(0).astype("int64").astype(str))
    out = pd.concat(flags, ignore_index=True) if flags else pd.DataFrame()
    for kind, n in (out.groupby("kind").size().items() if len(out) else []):
        print(f"  CUIPO {kind:<14} {n:>9,}")
    return inc, spe, out


def main():
    known = set(dane.municipalities()["cod_mpio"])
    inc, spe = income(), spending()
    for df in (inc, spe):
        df["mun"] = municipality(df["codigo_entidad"])
        out = ~df["mun"].isin(known)
        if out.any():
            print(f"  {out.sum():,} rows of entities whose code is not a DANE municipality: "
                  f"{sorted(df.loc[out, 'codigo_entidad'].unique())[:10]}")
        df.drop(df.index[out], inplace=True)
        df["municipality_id"] = df["mun"].astype(int)
        df["period"] = df["periodo"].astype(int)
    accounts = inc.drop_duplicates("cuenta")[["cuenta", "nombre_cuenta"]].rename(columns={"cuenta": "code", "nombre_cuenta": "name"})
    accounts["depth"] = accounts["code"].str.count(r"\.") + 1
    funding = pd.concat([inc[["cod_fuentes_financiacion", "nom_fuentes_financiacion"]],
                         spe[["cod_fuentes_financiacion", "nom_fuentes_financiacion"]]]) \
        .drop_duplicates("cod_fuentes_financiacion").set_axis(["code", "name"], axis=1)
    sectors = spe.drop_duplicates("cod_sector")[["cod_sector", "nom_sector"]].set_axis(["code", "name"], axis=1)
    for t in (accounts, funding, sectors):
        t["name"] = t["name"].str.slice(0, 255)
    inc["collected"] = pd.to_numeric(inc["collected"], errors="coerce")
    for c in ("commitments", "obligations", "payments"):
        spe[c] = pd.to_numeric(spe[c], errors="coerce")
    inc = inc.groupby(["municipality_id", "period", "cuenta", "cod_fuentes_financiacion"], as_index=False)["collected"].sum()
    spe = spe.groupby(["municipality_id", "period", "cod_sector", "cod_fuentes_financiacion"], as_index=False)[
        ["commitments", "obligations", "payments"]].sum()

    inc, spe, flags = validate(inc, spe)
    db = connect()
    cur = db.cursor()
    cur.execute("DELETE FROM RelationsAndConclusions.DataQualityFlags WHERE source = 'CUIPO'")
    if len(flags):
        load(cur, "RelationsAndConclusions.DataQualityFlags", flags,
             ["source", "source_table", "column_name", "municipality_id", "period", "kind", "value", "note"])
    cur.execute("SET FOREIGN_KEY_CHECKS = 0")
    for t in ("MunicipalIncome", "MunicipalSpending", "CuipoAccounts", "CuipoFundingSources", "CuipoSectors"):
        cur.execute(f"TRUNCATE TABLE Territorial_Context.{t}")
    load(cur, "Territorial_Context.CuipoAccounts", accounts, ["code", "name", "depth"])
    load(cur, "Territorial_Context.CuipoFundingSources", funding, ["code", "name"])
    load(cur, "Territorial_Context.CuipoSectors", sectors, ["code", "name"])
    load(cur, "Territorial_Context.MunicipalIncome", inc.rename(columns={"cuenta": "account", "cod_fuentes_financiacion": "funding_source"}),
         ["municipality_id", "period", "account", "funding_source", "collected"])
    load(cur, "Territorial_Context.MunicipalSpending", spe.rename(columns={"cod_sector": "sector", "cod_fuentes_financiacion": "funding_source"}),
         ["municipality_id", "period", "sector", "funding_source", "commitments", "obligations", "payments"])
    cur.execute("SET FOREIGN_KEY_CHECKS = 1")
    db.commit()
    db.close()


if __name__ == "__main__":
    main()
