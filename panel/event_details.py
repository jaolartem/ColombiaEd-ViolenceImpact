"""
CNMH events in full: the specific armed group and the acts committed together with each event.

    python -m panel.event_details          # after panel.load_db has loaded Physical_violence.ViolenceEvents

Every CNMH case names its presumed perpetrator at two levels: a category (guerrilla, paramilitary group, agent
of the State, ...) and the group (FARC, ELN, AUC, National Army, ...). It also records up to eleven acts
committed with the event (forced displacement, threat, torture, extortion, pillage, gender-based violence,
confinement, abandonment or dispossession, attack on a medical mission, injured civilians, other). Some are
marked 0/1, some count the persons who suffered the act, and gender-based violence is written as its form
(physical violence, forced domestic work, ...).

Normalised (decision 29): the group is a catalog under its category (PerpetratorGroups); the acts are a
catalog (SimultaneousActs) and each event-act pair is a connection (EventSimultaneousActs) with the persons
it reached or, when the source writes a form, the form (ActForms). An act at 0 is not recorded.
"""
import numpy as np
import pandas as pd

from panel import socrata
from panel.events import CNMH, FIELDS
from panel.load_db import connect, load

ACTS = {   # code -> (name, candidate field names)
    "abandonment_or_dispossession": ("Forced abandonment or dispossession", ["abandono_o_despojo_forzado"]),
    "threat": ("Threat or intimidation", ["amenaza_o_intimidaci_n", "amenaza_o_intimidacion"]),
    "attack_on_medical_mission": ("Attack on a medical mission", ["ataque_contra_misi_n_m_dica", "ataque_contra_mision_medica"]),
    "confinement": ("Confinement or restriction of movement", ["confinamiento_o_restricci", "confinamiento_o_restriccion"]),
    "forced_displacement": ("Forced displacement", ["desplazamiento_forzado"]),
    "extortion": ("Extortion", ["extorsi_n", "extorsion"]),
    "injured_civilians": ("Injured civilians", ["lesionados_civiles"]),
    "pillage": ("Pillage", ["pillaje"]),
    "torture": ("Torture", ["tortura"]),
    "gender_based_violence": ("Gender-based violence", ["violencia_basada_en_g_nero", "violencia_basada_en_genero"]),
    "other": ("Other simultaneous act", ["otro_hecho_simult_neo"]),
}


def main():
    token = socrata.app_token()
    detail, acts = [], []
    for modality, (dataset, label) in CNMH.items():
        meta = socrata.dataset_columns(dataset)
        idf = next(c for c in FIELDS["id"] if c in meta)
        perp = next((c for c in FIELDS["perpetrator"] if c in meta), None)
        fields = {code: next((c for c in names if c in meta), None) for code, (_, names) in ACTS.items()}
        cols = [idf, perp, "descripci_n_presunto"] + [c for c in fields.values() if c]
        cols = [c for c in cols if c and c in meta]
        rows = socrata.query(dataset, select=", ".join(cols), order=idf, token=token)
        rows["source_event_id"] = modality + "-" + rows[idf].astype(str)
        detail.append(pd.DataFrame({"source_event_id": rows["source_event_id"],
                                    "perpetrator": rows[perp].astype(str).str.strip() if perp else np.nan,
                                    "group": rows.get("descripci_n_presunto", pd.Series(np.nan, index=rows.index))}))
        for code, field in fields.items():
            if not field or field not in rows:
                continue
            raw = rows[field].astype(str).str.strip()
            n = pd.to_numeric(raw, errors="coerce")
            text = raw.where(n.isna() & ~raw.isin(["", "nan", "None", "NO APLICA", "SIN INFORMACION", "SIN INFORMACIÓN"]))
            keep = (n > 0) | text.notna()
            acts.append(pd.DataFrame({"source_event_id": rows.loc[keep, "source_event_id"], "act": code,
                                      "persons": n[keep], "form": text[keep]}))
        print(f"  CNMH {modality} {label:<40} {len(rows):>8,} cases", flush=True)
    detail = pd.concat(detail, ignore_index=True)
    acts = pd.concat(acts, ignore_index=True)

    db = connect()
    cur = db.cursor()
    cur.execute("SELECT source_event_id, id FROM Physical_violence.ViolenceEvents WHERE source_event_id NOT LIKE 'IND-%'")
    event_id = dict(cur.fetchall())
    cur.execute("SELECT name, id FROM Physical_violence.Perpetrators")
    perpetrator_id = dict(cur.fetchall())

    detail["group"] = detail["group"].astype(str).str.strip().replace({"nan": np.nan, "": np.nan, "NO APLICA": np.nan})
    detail["perpetrator_id"] = detail["perpetrator"].map(perpetrator_id)
    groups = detail.dropna(subset=["group", "perpetrator_id"]).drop_duplicates(["perpetrator_id", "group"])[["perpetrator_id", "group"]]
    groups = groups.sort_values(["perpetrator_id", "group"]).reset_index(drop=True)
    groups["id"] = range(1, len(groups) + 1)
    groups["name"] = groups["group"].str.slice(0, 200)
    detail = detail.merge(groups[["perpetrator_id", "group", "id"]].rename(columns={"id": "perpetrator_group_id"}),
                          on=["perpetrator_id", "group"], how="left")
    detail["event_id"] = detail["source_event_id"].map(event_id)

    catalog = pd.DataFrame([(i + 1, code, name) for i, (code, (name, _)) in enumerate(ACTS.items())], columns=["id", "code", "name"])
    acts["act_id"] = acts["act"].map(dict(zip(catalog["code"], catalog["id"])))
    acts["event_id"] = acts["source_event_id"].map(event_id)
    forms = acts.dropna(subset=["form"]).drop_duplicates(["act_id", "form"])[["act_id", "form"]].reset_index(drop=True)
    forms["id"] = range(1, len(forms) + 1)
    forms["label"] = forms["form"].str.slice(0, 200)
    acts = acts.merge(forms[["act_id", "form", "id"]].rename(columns={"id": "form_id"}), on=["act_id", "form"], how="left")
    missing = acts["event_id"].isna().sum() + detail["event_id"].isna().sum()
    if missing:
        print(f"  {missing:,} rows whose event is not in ViolenceEvents (left out)")
    acts = acts.dropna(subset=["event_id"]).drop_duplicates(["event_id", "act_id"])
    acts["persons"] = acts["persons"].round().astype("Int64")

    cur.execute("SET FOREIGN_KEY_CHECKS = 0")
    for t in ("EventSimultaneousActs", "ActForms", "SimultaneousActs", "PerpetratorGroups"):
        cur.execute(f"TRUNCATE TABLE Physical_violence.{t}")
    load(cur, "Physical_violence.PerpetratorGroups", groups, ["id", "perpetrator_id", "name"])
    load(cur, "Physical_violence.SimultaneousActs", catalog, ["id", "code", "name"])
    load(cur, "Physical_violence.ActForms", forms, ["id", "act_id", "label"])
    load(cur, "Physical_violence.EventSimultaneousActs", acts, ["event_id", "act_id", "persons", "form_id"])
    upd = detail.dropna(subset=["event_id", "perpetrator_group_id"])[["event_id", "perpetrator_group_id"]].astype(int)
    cur.execute("CREATE TEMPORARY TABLE Physical_violence._grp (event_id INT PRIMARY KEY, perpetrator_group_id INT)")
    load(cur, "Physical_violence._grp", upd, ["event_id", "perpetrator_group_id"])
    cur.execute("""UPDATE Physical_violence.ViolenceEvents e JOIN Physical_violence._grp g ON g.event_id = e.id
                   SET e.perpetrator_group_id = g.perpetrator_group_id""")
    print(f"  events with their armed group: {cur.rowcount:,}")
    cur.execute("SET FOREIGN_KEY_CHECKS = 1")
    db.commit()
    db.close()


if __name__ == "__main__":
    main()
