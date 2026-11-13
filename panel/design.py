"""
The decision log: research/decisions.csv into Research_Design.Decisions and DecisionObjects.

    python -m panel.design

research/decisions.csv is the place to write a decision: one row each, with its date, topic, who took it
(researcher, assistant, or both), what was decided, why, and the tables, modules or documents it governs
(separated by ';'). A decision that replaces another names it in a column superseded_by of the old row.
The file is versioned with the code, so the log has its own history.
"""
from pathlib import Path

import pandas as pd

from panel.load_db import connect, load

ROOT = Path(__file__).resolve().parent.parent
CSV = ROOT / "research" / "decisions.csv"


def main():
    d = pd.read_csv(CSV, dtype=str, keep_default_na=False)
    db = connect()
    cur = db.cursor()
    cur.execute("SELECT code, id FROM Research_Design.DecisionTopics")
    topics = dict(cur.fetchall())
    unknown = set(d["topic"]) - set(topics)
    if unknown:
        raise SystemExit(f"unknown topics in {CSV.name}: {sorted(unknown)}")
    bad = set(d["decided_by"]) - {"researcher", "assistant", "both"}
    if bad:
        raise SystemExit(f"decided_by must be researcher, assistant or both: {sorted(bad)}")
    d["topic_id"] = d["topic"].map(topics)
    d["superseded_by"] = d["superseded_by"] if "superseded_by" in d else ""
    d["superseded_by"] = d["superseded_by"].replace("", pd.NA)
    d["reason"] = d["reason"].replace("", pd.NA)
    objects = (d.assign(object_name=d["objects"].str.split(";")).explode("object_name")
               .assign(object_name=lambda x: x["object_name"].str.strip()))
    objects = objects[objects["object_name"] != ""]
    cur.execute("SET FOREIGN_KEY_CHECKS = 0")
    for t in ("DecisionObjects", "Decisions"):
        cur.execute(f"TRUNCATE TABLE Research_Design.{t}")
    load(cur, "Research_Design.Decisions", d,
         ["id", "decided_on", "topic_id", "decision", "reason", "decided_by", "superseded_by"])
    load(cur, "Research_Design.DecisionObjects", objects.rename(columns={"id": "decision_id"}), ["decision_id", "object_name"])
    cur.execute("SET FOREIGN_KEY_CHECKS = 1")
    db.commit()
    db.close()


if __name__ == "__main__":
    main()
