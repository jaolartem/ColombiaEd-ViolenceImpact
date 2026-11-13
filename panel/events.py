"""
Violence events, one row per event, and the triangulation of massacres across sources.

    python -m panel.events [--out output/panel]

Sources
- CNMH, Observatorio de Memoria y Conflicto (SIEVCAC) on datos.gov.co: eleven modalities of armed-
  conflict violence, built from press, judicial and social-organisation sources, from 1958 to the
  cut-off written in each dataset's description. Each case has a date, a municipality, a presumed
  perpetrator, its victims, and marks of what happened with it (forced displacement, confinement).
- INDEPAZ massacre list, 2020 onwards (panel/indepaz.py), built from press and regional reports.
- Police massacre table (MinDefensa, u8eq-92tb), 2022 onwards.

Triangulation: two massacres from different sources are the same event when they happened in the same
municipality within 3 days (15 when one of them only has the month). Matching is one to one, nearest
first. Linked events are grouped into clusters, so each distinct massacre appears once with the sources
that record it.

Writes events.csv, event_links.csv, massacre_clusters.csv and massacre_overlap.csv.
"""
import argparse
import re
from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd

from panel import dane, indepaz, socrata

CNMH = {
    "MA": ("d78j-f66e", "massacre"),
    "AS": ("sysu-pezb", "selective killing"),
    "DF": ("9r7i-ek3s", "forced disappearance"),
    "SE": ("cdw6-jexv", "kidnapping"),
    "MI": ("grup-7tjb", "landmines and explosive remnants"),
    "RU": ("hzd2-7ea7", "recruitment of children and adolescents"),
    "AP": ("3xsy-8xcp", "attack on a town"),
    "AB": ("39qq-a72j", "act of war"),
    "DB": ("x27p-cm5t", "damage to civilian property"),
    "VS": ("k9qg-2svz", "sexual violence"),
    "AT": ("yfd7-8c9d", "terrorist attack"),
}
POLICE_MASSACRES = "u8eq-92tb"
FIELDS = {          # role -> candidate field names, first one present wins
    "id": ["id_caso"],
    "year": ["a_o", "ano"],
    "month": ["mes"],
    "day": ["d_a", "dia"],
    "code": ["c_digo_dane_de_municipio", "codigo_dane_de_municipio"],
    "perpetrator": ["presunto_responsable", "grupo_armado_1"],
    "victims": ["total_de_v_ctimas_del_caso"],
    "displacement": ["desplazamiento_forzado"],
    "confinement": ["confinamiento_o_restricci", "confinamiento_o_restriccion"],
}
WINDOW_DAYS, WINDOW_MONTH = 3, 15
COLUMNS = ["source", "source_event_id", "modality", "day", "date_precision", "cod_mpio", "victims",
           "perpetrator", "displacement", "confinement"]


def _date(y, m, d):
    """Date and its precision; unknown month -> 1 July, unknown day -> the 15th."""
    if pd.isna(y) or not 1900 <= y <= 2100:      # some CNMH cases have year 0: the date is unknown
        return None, None
    precision = "day"
    if pd.isna(m) or not 1 <= m <= 12:
        m, d, precision = 7, 1, "year"
    elif pd.isna(d) or not 1 <= d <= 31:
        d, precision = 15, "month"
    while True:
        try:
            return date(int(y), int(m), int(d)), precision
        except ValueError:
            d -= 1


def cnmh(token) -> pd.DataFrame:
    frames = []
    for modality, (dataset, label) in CNMH.items():
        meta = socrata.dataset_columns(dataset)
        chosen = {role: next((c for c in names if c in meta), None) for role, names in FIELDS.items()}
        select = ", ".join(c for c in chosen.values() if c)
        rows = socrata.query(dataset, select=select, order=chosen["id"], token=token)
        rows = rows.rename(columns={c: role for role, c in chosen.items() if c})
        for role in FIELDS:
            if role not in rows:
                rows[role] = np.nan
        num = {r: pd.to_numeric(rows[r], errors="coerce") for r in ("year", "month", "day")}
        dated = [_date(y, m, d) for y, m, d in zip(num["year"], num["month"], num["day"])]
        cut = re.search(r"(\d{1,2})\s*-\s*(\d{1,2})\s*-\s*(\d{4})", socrata.dataset_description(dataset))
        frames.append(pd.DataFrame({
            "source": "cnmh",
            "source_event_id": modality + "-" + rows["id"].astype(str),
            "modality": modality,
            "day": [x[0] for x in dated],
            "date_precision": [x[1] for x in dated],
            "cod_mpio": dane.normalize_code(rows["code"]),
            "victims": pd.to_numeric(rows["victims"], errors="coerce"),
            "perpetrator": rows["perpetrator"],
            "displacement": pd.to_numeric(rows["displacement"], errors="coerce"),
            "confinement": pd.to_numeric(rows["confinement"], errors="coerce"),
        }).assign(cutoff=date(int(cut.group(3)), int(cut.group(2)), int(cut.group(1))) if cut else None))
        print(f"  CNMH {modality} {label:<40} {len(rows):>8,} cases")
    return pd.concat(frames, ignore_index=True)


def indepaz_events() -> pd.DataFrame:
    events, unmatched = indepaz.load()
    if len(unmatched):
        print(f"  INDEPAZ rows without a DANE code (source errors, left out of the links): {len(unmatched)}")
    out = pd.DataFrame({
        "source": "indepaz",
        "source_event_id": ["IND-" + d.strftime("%Y%m%d") + f"-{i}" for i, d in enumerate(events["day"])],
        "modality": "MA", "day": events["day"], "date_precision": events["date_precision"],
        "cod_mpio": events["cod_mpio"], "victims": events["victims"],
        "perpetrator": np.nan, "displacement": np.nan, "confinement": np.nan,
    })
    print(f"  INDEPAZ massacres {len(out):>8,}")
    return out


def police_massacres(token) -> pd.DataFrame:
    rows = socrata.query(POLICE_MASSACRES, select="fecha_hecho, cod_muni, casos, victimas",
                         order="fecha_hecho, cod_muni", token=token)
    rows["casos"] = pd.to_numeric(rows["casos"], errors="coerce").fillna(1).astype(int)
    rows = rows.loc[rows.index.repeat(rows["casos"].clip(lower=1))].reset_index(drop=True)   # one row per event
    out = pd.DataFrame({
        "source": "police",
        "source_event_id": [f"POL-{i}" for i in range(len(rows))],
        "modality": "MA", "day": pd.to_datetime(rows["fecha_hecho"]).dt.date, "date_precision": "day",
        "cod_mpio": dane.normalize_code(rows["cod_muni"]),
        "victims": pd.to_numeric(rows["victimas"], errors="coerce") / rows["casos"].clip(lower=1),
        "perpetrator": np.nan, "displacement": np.nan, "confinement": np.nan,
    })
    print(f"  Police massacres {len(out):>8,}")
    return out


def link(a: pd.DataFrame, b: pd.DataFrame) -> pd.DataFrame:
    """One-to-one links between two sources' massacres: same municipality, nearest date within the window."""
    pairs = a.reset_index().merge(b.reset_index(), on="cod_mpio", suffixes=("_a", "_b"))
    if pairs.empty:
        return pd.DataFrame(columns=["event_a", "event_b", "day_gap"])
    pairs["gap"] = [abs((x - y).days) for x, y in zip(pairs["day_a"], pairs["day_b"])]
    month = (pairs["date_precision_a"] == "month") | (pairs["date_precision_b"] == "month")
    pairs = pairs[pairs["gap"] <= np.where(month, WINDOW_MONTH, WINDOW_DAYS)].sort_values("gap")
    used_a, used_b, kept = set(), set(), []
    for row in pairs.itertuples():
        if row.source_event_id_a in used_a or row.source_event_id_b in used_b:
            continue
        used_a.add(row.source_event_id_a); used_b.add(row.source_event_id_b)
        kept.append((row.source_event_id_a, row.source_event_id_b, row.gap))
    return pd.DataFrame(kept, columns=["event_a", "event_b", "day_gap"])


def triangulate(events: pd.DataFrame):
    massacres = events[(events["modality"] == "MA") & events["cod_mpio"].notna() & events["day"].notna()]
    by_source = {s: d for s, d in massacres.groupby("source")}
    windows = {s: (d["day"].min(), d["cutoff"].dropna().max() if d["cutoff"].notna().any() else d["day"].max())
               for s, d in by_source.items()}
    links, overlap = [], []
    names = sorted(by_source)
    for i, sa in enumerate(names):
        for sb in names[i + 1:]:
            start = max(windows[sa][0], windows[sb][0])
            end = min(windows[sa][1], windows[sb][1])
            a = by_source[sa][(by_source[sa]["day"] >= start) & (by_source[sa]["day"] <= end)]
            b = by_source[sb][(by_source[sb]["day"] >= start) & (by_source[sb]["day"] <= end)]
            l = link(a, b)
            links.append(l)
            matched_a, matched_b = set(l["event_a"]), set(l["event_b"])
            for year in sorted({d.year for d in a["day"]} | {d.year for d in b["day"]}):
                ay = a[[d.year == year for d in a["day"]]]
                by = b[[d.year == year for d in b["day"]]]
                for threshold in (3, 4):          # the definition test: only events with 4+ victims
                    af, bf = ay[ay["victims"].fillna(0) >= threshold], by[by["victims"].fillna(0) >= threshold]
                    overlap.append({
                        "source_a": sa, "source_b": sb, "year": year, "min_victims": threshold,
                        "events_a": len(af), "events_b": len(bf),
                        "a_found_in_b": af["source_event_id"].isin(matched_a).sum(),
                        "b_found_in_a": bf["source_event_id"].isin(matched_b).sum(),
                    })
    links = pd.concat(links, ignore_index=True)

    # clusters: connected components of the links
    parent = {e: e for e in massacres["source_event_id"]}
    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    for a, b in zip(links["event_a"], links["event_b"]):
        parent[root(a)] = root(b)
    clusters = massacres[["source_event_id", "source", "day", "cod_mpio", "victims"]].copy()
    clusters["cluster"] = [root(e) for e in clusters["source_event_id"]]
    overlap = pd.DataFrame(overlap)
    overlap["share_a_in_b"] = overlap["a_found_in_b"] / overlap["events_a"].replace(0, np.nan)
    overlap["share_b_in_a"] = overlap["b_found_in_a"] / overlap["events_b"].replace(0, np.nan)
    return links, clusters, overlap


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", default="output/panel", type=Path)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    token = socrata.app_token()

    print("events")
    events = pd.concat([cnmh(token), indepaz_events(), police_massacres(token)], ignore_index=True)
    events = events[COLUMNS + ["cutoff"]]
    print(f"  without a DANE code: {events['cod_mpio'].isna().sum():,} of {len(events):,}")
    links, clusters, overlap = triangulate(events)

    events.to_csv(args.out / "events.csv", index=False)
    links.to_csv(args.out / "event_links.csv", index=False)
    clusters.to_csv(args.out / "massacre_clusters.csv", index=False)
    overlap.to_csv(args.out / "massacre_overlap.csv", index=False)

    pd.set_option("display.width", 200)
    o = overlap[overlap["min_victims"] == 3].groupby(["source_a", "source_b"])[["events_a", "events_b", "a_found_in_b", "b_found_in_a"]].sum()
    o["share_a_in_b"], o["share_b_in_a"] = o["a_found_in_b"] / o["events_a"], o["b_found_in_a"] / o["events_b"]
    print("overlap (all massacres):"); print(o.round(2).to_string())
    o4 = overlap[overlap["min_victims"] == 4].groupby(["source_a", "source_b"])[["events_a", "events_b", "a_found_in_b", "b_found_in_a"]].sum()
    o4["share_a_in_b"], o4["share_b_in_a"] = o4["a_found_in_b"] / o4["events_a"], o4["b_found_in_a"] / o4["events_b"]
    print("overlap (4+ victims):"); print(o4.round(2).to_string())
    recent = clusters[[d.year >= 2020 for d in clusters["day"]]]
    per = recent.groupby("cluster").agg(year=("day", lambda s: min(s).year), sources=("source", lambda s: "+".join(sorted(set(s)))))
    print("distinct massacres by year and sources that record them (2020+):")
    print(per.pivot_table(index="year", columns="sources", aggfunc="size", fill_value=0).to_string())


if __name__ == "__main__":
    main()
