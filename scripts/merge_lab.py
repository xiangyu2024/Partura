"""Merge the lab findings the leads returned (handoff/<fid>/results/{synthesis,verdict}.json) into lab/findings.yaml.

Idempotent: an id already in the file is left alone.  Ids are prefixed with the factor so that two studies cannot
collide; every entry keeps the study it came from and the condition under which it should be re-checked.

    python scripts/merge_lab.py [--kinds verdict,synthesis]
"""
import json
import re
import sys
from pathlib import Path

import yaml

root = Path(__file__).resolve().parents[1]
kinds = (sys.argv[sys.argv.index("--kinds") + 1] if "--kinds" in sys.argv else "verdict").split(",")
p = root / "lab" / "findings.yaml"
L = yaml.safe_load(p.read_text(encoding="utf-8"))
have = {x["id"] for x in L["findings"]}
added = 0
for kind in kinds:
    for fp in sorted((root / "handoff").glob(f"F*/results/{kind}.json")):
        fid = fp.parts[-3]
        V = json.loads(fp.read_text(encoding="utf-8"))
        V = V.get("result", V)
        for x in V.get("lab_findings", []) or []:
            if not isinstance(x, dict) or not x.get("claim"):
                continue
            slug = re.sub(r"[^a-z0-9]+", "-", str(x.get("id", "")).lower()).strip("-") or f"l{added}"
            i = f"{fid.split('_')[0].lower()}-{slug}"
            if i in have:
                continue
            ops = x.get("operators")
            if isinstance(ops, str):
                ops = re.findall(r"[A-Za-z_][A-Za-z_0-9]*", ops)
            L["findings"].append({"id": i, "claim": str(x["claim"]).strip(), "evidence": str(x.get("evidence", "")).strip(), "study": fid,
                                  "date": "2026-10-05", "source": f"batch {kind}", "operators": ops or [],
                                  "confidence": str(x.get("confidence", "medium")), "recheck": str(x.get("recheck", "")).strip()})
            have.add(i)
            added += 1
p.write_text(yaml.safe_dump(L, allow_unicode=True, sort_keys=False, width=1000), encoding="utf-8")
print(f"added {added}; lab/findings.yaml now has {len(L['findings'])} findings")
