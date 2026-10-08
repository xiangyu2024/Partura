"""Several runs of one idea (different seeds), read together: does the steered arm find more than the control?

Local.  Reads episodes/<prefix><seed>_<idea>/evidence.json for every seed found and counts, per run and per arm,
by the one definition of a find (partura.steer.is_discovery) and by family (Guidance.family_key):

    scored / gate failures     what the arm paid for
    finds (families)           distinct candidates that count as a find, and the number of families among them
    size                       for the paired rewards: families whose book earns >= 1 point a year more than the
                               reference in BOTH periods (dann_train, dann_valid), and the best such size
    per 100                    families of finds per 100 paid evaluations

    python scripts/episode_summary.py <prefix> <idea> [<prefix2> ...]      e.g.  e4k I1_frozen_state e4p
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.steer import PAIRED, Guidance, is_discovery  # noqa: E402

root = Path(__file__).resolve().parents[1]
args = [a for a in sys.argv[1:] if not a.startswith("-")]
idea = next(a for a in args if a.startswith("I"))
prefixes = [a for a in args if a != idea]
ARM = {"steer": "带指引", "control": "对照"}
out = {}
for pre in prefixes:
    runs = sorted((root / "episodes").glob(f"{pre}[0-9]*_{idea}/evidence.json"))
    rows, tot = [], {"steer": [0, 0, 0, 0], "control": [0, 0, 0, 0]}
    wins = 0
    print(f"\n== {pre}*_{idea}: {len(runs)} runs")
    print(f"{'run':8s} {'arm':8s} {'scored':>6s} {'gate':>5s} {'finds':>6s} {'fam':>4s} {'fam>=1pt both':>14s} {'best size (min of periods)':>27s} {'fam/100':>8s} {'best score':>10s}")
    for p in runs:
        E = json.loads(p.read_text(encoding="utf-8"))
        G = Guidance.load(root / E.get("guidance", "guidance/B01.yaml"))
        kind, thr = E["reward"], float(E.get("threshold", 1.0))
        per = {}
        for arm, A in E["arms"].items():
            cs = sorted([c for c in A["candidates"] if c.get("score") == c.get("score") and abs(c["score"]) != float("inf")], key=lambda c: -c["score"])
            seen, fams, sized = set(), {}, {}
            for c in cs:
                try:
                    k, f = G.dedup_key(c["expr"]), G.family_key(c["expr"])
                except ValueError:
                    k = f = c["expr"]
                if k in seen:
                    continue
                seen.add(k)
                if is_discovery(kind, c["score"], c.get("s_train"), c.get("s_valid"), thr):
                    fams.setdefault(f, c)
                if kind in PAIRED and c.get("dann_train") == c.get("dann_train") and min(c["dann_train"], c["dann_valid"]) >= 0.01:
                    if f not in sized or min(c["dann_train"], c["dann_valid"]) > min(sized[f]["dann_train"], sized[f]["dann_valid"]):
                        sized[f] = c
            finds = sum(1 for c in cs if is_discovery(kind, c["score"], c.get("s_train"), c.get("s_valid"), thr))
            best = max(sized.values(), key=lambda c: min(c["dann_train"], c["dann_valid"]), default=None)
            per[arm] = {"scored": A["scored"], "gate": A["gate_fail"], "finds": finds, "families": len(fams), "sized": len(sized),
                        "best_size": None if best is None else [best["dann_train"], best["dann_valid"], best["expr"]],
                        "best_score": cs[0]["score"] if cs else None, "heads": [[c["score"], c.get("dann_train"), c.get("dann_valid"), c["sign"], c["hl"], c["expr"]] for c in list(fams.values())[:6]],
                        "seconds": A["seconds"], "code": E.get("code"), "screen_base": E.get("screen_base")}
            t = tot[arm]
            t[0] += A["scored"]; t[1] += len(fams); t[2] += len(sized); t[3] += A["seconds"]
            bs = "—" if best is None else f"{min(best['dann_train'], best['dann_valid']):+.1%}"
            print(f"{p.parent.name.split('_')[0]:8s} {arm:8s} {A['scored']:6d} {A['gate_fail']:5d} {finds:6d} {len(fams):4d} {len(sized):14d} {bs:>27s} {100 * len(fams) / max(A['scored'], 1):8.1f} "
                  f"{'—' if not cs else format(cs[0]['score'], '+.2f'):>10s}")
        if "steer" in per and "control" in per and per["steer"]["families"] > per["control"]["families"]:
            wins += 1
        rows.append({"run": p.parent.name, **per})
    s, c = tot["steer"], tot["control"]
    verdict = ("evidence" if (s[1] >= 2 * c[1] and s[1] > 0 and wins >= 2) else "no evidence")
    print(f"total    steer   scored {s[0]} families {s[1]} sized-families {s[2]} ({s[3] / 60:.0f} min)   |   control scored {c[0]} families {c[1]} sized-families {c[2]} ({c[3] / 60:.0f} min)"
          f"   |   seeds where steer > control: {wins}/{len(runs)}   ->   {verdict}")
    out[pre] = {"runs": rows, "total": {"steer": dict(zip(("scored", "families", "sized", "seconds"), s)), "control": dict(zip(("scored", "families", "sized", "seconds"), c))},
                "seeds_steer_ahead": wins, "verdict": verdict}
(root / "episodes" / f"{'_'.join(prefixes)}_{idea}_summary.json").write_text(json.dumps(out, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
