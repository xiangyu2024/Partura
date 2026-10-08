"""A 2 x 2 x 2 ablation of the steer arm (seeds / hood / priors), read from the episodes of each cell.

Local.  Cells are given as  label=prefix[:arm]  where the label is the set of parts that were ON (letters s, h, r; "0"
for none):  e.g.  0=e4k:control  shr=e4k:steer  s=e5s  h=e5h  r=e5r  sh=e5sh  sr=e5sr  hr=e5hr.  For every cell: the
families of finds over its seeds, the paid evaluations, families per 100 evaluations.  For every part: the main effect =
mean over the four settings of the other two parts of (on - off), and in how many of the four the part helped.

    python scripts/factorial_summary.py I1_frozen_state 0=e4k:control shr=e4k:steer s=e5s h=e5h r=e5r sh=e5sh sr=e5sr hr=e5hr
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.steer import Guidance, is_discovery  # noqa: E402

root = Path(__file__).resolve().parents[1]
idea, cells = sys.argv[1], dict(a.split("=") for a in sys.argv[2:])
G = Guidance.load(root / "guidance" / "B01.yaml")
T = {}
for label, spec in cells.items():
    pre, arm = (spec.split(":") + ["steer"])[:2]
    fam = scored = runs = meas = 0
    per, per_m = [], []
    for p in sorted((root / "episodes").glob(f"{pre}[0-9]_{idea}/evidence.json")):
        E = json.loads(p.read_text(encoding="utf-8"))
        A = E["arms"][arm]
        keys = set()
        for c in A["candidates"]:
            if is_discovery(E["reward"], c.get("score"), c.get("s_train"), c.get("s_valid"), float(E.get("threshold", 1.0))):
                try:
                    keys.add(G.family_key(c["expr"]))
                except ValueError:
                    keys.add(c["expr"])
        fam += len(keys); scored += A["scored"]; runs += 1
        per.append(len(keys))
        # finds that are distinct BY MEASUREMENT: mutual rank correlation of the traded signals below 0.7 (the search
        # script computes it).  A family key only merges renamings and root wrappers; one lucky structure bred into
        # twenty window / nesting variants is twenty "families" and one find (e5r1: 27 families, 4 distinct).
        m = A.get("independent_distinct") or 0
        meas += m
        per_m.append(m)
    T["".join(sorted(label.replace("0", "")))] = {"families": fam, "scored": scored, "runs": runs, "per_seed": per, "rate": 100.0 * fam / max(scored, 1),
                                                  "distinct": meas, "distinct_per_seed": per_m, "distinct_rate": 100.0 * meas / max(scored, 1)}
print(f"{'parts on':22s} {'runs':>4s} {'scored':>6s} {'families':>8s} {'per seed':>12s} {'per 100':>8s} | {'distinct':>8s} {'per seed':>12s} {'per 100':>8s}")
NAME = {"s": "seeds", "h": "hood", "r": "priors"}
for k in ("", "s", "h", "r", "hs", "rs", "hr", "hrs"):
    if k in T:
        t = T[k]
        print(f"{'+'.join(NAME[x] for x in k) or 'none (control)':22s} {t['runs']:4d} {t['scored']:6d} {t['families']:8d} {str(t['per_seed']):>12s} {t['rate']:8.1f} | {t['distinct']:8d} {str(t['distinct_per_seed']):>12s} {t['distinct_rate']:8.1f}")
out = {"cells": T, "effects": {}, "effects_distinct": {}}
for metric, rate, cnt, slot, unit in (("families (pre-registered)", "rate", "families", "effects", 2.0), ("measured-distinct finds", "distinct_rate", "distinct", "effects_distinct", 0.5)):
    print(f"\n-- main effects on {metric}, per 100 paid evaluations")
    for part in "shr":
        diffs = []
        for other in ("", *[x for x in "shr" if x != part], "".join(x for x in "shr" if x != part)):
            on, off = "".join(sorted(other + part)), "".join(sorted(other))
            if on in T and off in T and T[on]["runs"] and T[off]["runs"]:
                diffs.append((off or "none", T[on][rate] - T[off][rate], T[on][cnt] - T[off][cnt]))
        if diffs:
            m = sum(d[1] for d in diffs) / len(diffs)
            helped = sum(d[1] > 0 for d in diffs)
            # the pre-registered reading (families): useful = helped in >= 3 of 4 and >= 2 per 100; useless = within +-1
            verdict = "有用" if (helped >= 3 and m >= unit) else "没用" if abs(m) <= unit / 2 else "不确定"
            out[slot][NAME[part]] = {"mean_rate_diff": m, "helped": helped, "of": len(diffs), "diffs": diffs, "verdict": verdict}
            print(f"{NAME[part]:7s} on - off: " + ", ".join(f"given {d[0]}: {d[1]:+.1f} ({d[2]:+d})" for d in diffs) + f"   mean {m:+.1f}; helped in {helped}/{len(diffs)}  ->  {verdict}")
(root / "episodes" / f"e5_{idea}_factorial.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
