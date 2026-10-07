"""Priors for a generator, learned from that generator's own archives.

Local.  The guidance in guidance/<batch>.yaml was learned from Partura's own batch sweeps (hand-made actions applied
to fifteen bases).  Episode e5 showed that most of those rules never fire on what AlphaCube's GP actually proposes:
the two generators propose different things.  This script reads the GP's OWN archives (every live candidate a run
scored, with its fitness) and asks which operators, root operators, parent>child pairs and leaves are over- or
under-represented among a run's best and worst candidates.

    python scripts/gp_archive_priors.py "runs/_ideas/alphacube_archives/gp_*_1.csv" [--tag fullmarket] [--top 0.2] [--min-n 30]

Fitness is compared INSIDE a run (percentile), so runs with different fitness kinds can be pooled.  "top" = the best
fifth of a run's archive, "bottom" = the worst fifth.  lift = share of the feature's candidates that are in the top
(bottom) fifth, divided by 0.2: 1.0 means the feature says nothing.  "runs" counts in how many of the runs where the
feature has at least 8 candidates it leans the same way.  Also checks the existing guidance on these candidates.

Use only archives of runs that ended before the holdout (meta.json: end <= 20230807): a prior learned on fitness
that saw the test period would leak it into every later search.
"""
import collections
import csv
import glob
import json
import math
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.steer import Guidance, parse_expr, walk  # noqa: E402

root = Path(__file__).resolve().parents[1]
argv = sys.argv[1:]


def opt(name, default=None):
    return argv[argv.index(name) + 1] if name in argv else default


TOP, MIN_N, TAG = float(opt("--top", 0.2)), int(opt("--min-n", 30)), opt("--tag", "gp")
G = Guidance.load(root / opt("--guidance", "guidance/B01.yaml"))
rows = []
for p in sorted(glob.glob(str(root / argv[0]))):
    R = []
    for r in csv.DictReader(open(p, encoding="utf-8")):
        try:
            f = float(r["fitness"])
        except (KeyError, ValueError):
            continue
        if math.isfinite(f):
            R.append((f, r["expression"]))
    R.sort(key=lambda x: x[0])
    n = len(R)
    for i, (f, e) in enumerate(R):
        pct = (i + 0.5) / n
        feats = {"op": set(), "root": set(), "pair": set(), "leaf": set()}
        try:
            t = parse_expr(e)
            feats["root"].add(t.name)
            for node, _ in walk(t):
                if node.args is not None:
                    feats["op"].add(node.name)
                    for a in node.args:
                        if a.args is not None:
                            feats["pair"].add(f"{node.name}>{a.name}")
                elif not node.is_number:
                    feats["leaf"].add(node.name)
            w = G.weight(e)
            rules = [x.id for x in G.explain(e)]
        except ValueError:
            feats["op"] = set(re.findall(r"[A-Za-z_][A-Za-z_0-9]*(?=\()", e))
            w, rules = 1.0, ["(unread)"]
        rows.append({"run": Path(p).stem, "pct": pct, "top": pct >= 1 - TOP, "bottom": pct <= TOP, "feats": feats, "w": w, "rules": rules, "size": len(re.findall(r"\(", e))})
runs = sorted({r["run"] for r in rows})
print(f"{len(rows)} archived candidates of {len(runs)} runs ({', '.join(runs)}); top / bottom = the best / worst {TOP:.0%} of each run's archive\n")


def table(kind, title):
    S = collections.defaultdict(list)
    for r in rows:
        for f in r["feats"][kind]:
            S[f].append(r)
    out = {}
    for f, rs in S.items():
        if len(rs) < MIN_N:
            continue
        n = len(rs)
        t, b = sum(r["top"] for r in rs) / n, sum(r["bottom"] for r in rs) / n
        same = tot = 0
        for run in runs:
            rr = [r for r in rs if r["run"] == run]
            if len(rr) >= 8:
                tot += 1
                same += (sum(r["top"] for r in rr) / len(rr) - sum(r["bottom"] for r in rr) / len(rr)) * (t - b) > 0
        z = (t - b) * n / math.sqrt(max(n * 2 * TOP, 1e-9))            # top minus bottom, against "says nothing"
        out[f] = {"n": n, "share": n / len(rows), "lift_top": t / TOP, "lift_bottom": b / TOP, "z": z, "runs_same": same, "runs": tot,
                  "median_pct": sorted(r["pct"] for r in rs)[n // 2]}
    print(f"== {title}  (n >= {MIN_N}; sorted by top-minus-bottom)")
    print(f"{'':34s} {'n':>5s} {'share':>6s} {'lift top':>9s} {'lift bottom':>12s} {'median pct':>11s} {'z':>6s} {'runs':>6s}")
    order = sorted(out, key=lambda f: -(out[f]["lift_top"] - out[f]["lift_bottom"]))
    show = order if len(order) <= 24 else order[:12] + ["..."] + order[-12:]
    for f in show:
        if f == "...":
            print("   ...")
            continue
        o = out[f]
        print(f"{f[:34]:34s} {o['n']:5d} {o['share']:6.1%} {o['lift_top']:9.2f} {o['lift_bottom']:12.2f} {o['median_pct']:11.2f} {o['z']:+6.1f} {o['runs_same']:>3d}/{o['runs']:<2d}")
    print()
    return out


res = {"runs": runs, "n": len(rows), "top": TOP, "op": table("op", "operators (anywhere in the tree)"), "root": table("root", "root operator"),
       "pair": table("pair", "parent > child"), "leaf": table("leaf", "leaves")}
# the existing guidance on these candidates
print("== the existing guidance on these candidates")
gc = {}
for name, sel in (("let through (weight >= 1)", lambda r: r["w"] >= 1), ("down-weighted (0 < weight < 1)", lambda r: 0 < r["w"] < 1), ("banned (weight 0)", lambda r: r["w"] <= 0)):
    S = [r for r in rows if sel(r)]
    if S:
        gc[name] = {"n": len(S), "lift_top": sum(r["top"] for r in S) / len(S) / TOP, "lift_bottom": sum(r["bottom"] for r in S) / len(S) / TOP}
        print(f"{name:34s} {len(S):5d} {len(S) / len(rows):6.1%} {gc[name]['lift_top']:9.2f} {gc[name]['lift_bottom']:12.2f}")
rc = {}
for rid, c in collections.Counter(x for r in rows for x in r["rules"]).most_common(14):
    S = [r for r in rows if rid in r["rules"]]
    rc[rid] = {"n": len(S), "lift_top": sum(r["top"] for r in S) / len(S) / TOP, "lift_bottom": sum(r["bottom"] for r in S) / len(S) / TOP}
    print(f"   {rid[:31]:31s} {len(S):5d} {len(S) / len(rows):6.1%} {rc[rid]['lift_top']:9.2f} {rc[rid]['lift_bottom']:12.2f}")
res["guidance_classes"], res["guidance_rules"] = gc, rc
d = root / "guidance"
(d / f"gp_archive_stats_{TAG}.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"\nwrote guidance/gp_archive_stats_{TAG}.json")
