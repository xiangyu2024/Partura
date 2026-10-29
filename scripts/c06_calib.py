"""C06 (PLAN §3, the auditor's calibration): every seed expression Partura proposed, accepted or rejected by the audit.  Local.

    python scripts/c06_calib.py      -> research/coldstart_C06/calib.json  [{seed, round, slot, expr, group, why}]

accepted = a seed kept in a slot that passed its last audit (what the GP was seeded with);
rejected = every other seed any draft of that round proposed: struck by the auditor, struck by the correlation table, in a slot that
           did not pass, or dropped in a rewrite.  Cores and R variants are not seeds and are left out.
"""
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / "research" / "coldstart_C06"
rows = []
for P in sorted((D / "partura").glob("s8*")):
    S = int(P.name[1:])
    for k in (1, 2, 3):
        R = P / f"r{k}"
        rec_f = R / "audit_record.json"
        if not rec_f.is_file():
            continue
        rec = json.loads(rec_f.read_text(encoding="utf-8"))
        accepted = {}
        for s in rec["slots"]:
            if s["pass"]:
                accepted.update({e: s["slot"] for e in s["seeds_kept"]})
        last = {s["slot"]: s for s in rec["slots"]}
        proposed = {}                                     # expr -> (slot, attempts that proposed it)
        for q in sorted(R.glob("corr_*.request.json"), key=lambda f: int(f.name.split("_")[1].split(".")[0])):
            n = int(q.name.split("_")[1].split(".")[0])
            for r in json.loads(q.read_text(encoding="utf-8")):
                w = r["where"].split()
                if len(w) >= 3 and w[0] == "slot" and w[2] == "seed":
                    proposed.setdefault(r["expr"], [w[1], []])[1].append(n)
        for e, (j, ns) in proposed.items():
            if e in accepted:
                rows.append({"seed": S, "round": k, "slot": accepted[e], "expr": e, "group": "accepted", "why": "kept"})
                continue
            s = last.get(j)
            if s is None or e not in s["seeds_all"]:
                why = "dropped in a rewrite"
            elif not s["pass"] and e in s["seeds_kept"]:
                why = "slot did not pass"
            else:
                why = "struck"
            rows.append({"seed": S, "round": k, "slot": j, "expr": e, "group": "rejected", "why": why, "attempts": ns})
(D / "calib.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
by = {}
for r in rows:
    by.setdefault((r["group"], r["why"]), 0)
    by[(r["group"], r["why"])] += 1
print(f"wrote {D / 'calib.json'}: {len(rows)} rows, {len({r['expr'] for r in rows})} distinct expressions; {by}")
