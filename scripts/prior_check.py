"""Do the priors tell good candidates from bad ones -- on candidates they never filtered?

Local.  Takes the full archives of CONTROL arms (every live candidate an unsteered search scored; pull them with
``rsync`` from episodes/<run>/control/checkpoints/archive_gen*.csv on the server into runs/_ideas/archives/) and
asks, for each class of the guidance -- lets through / down-weights / bans / an equivalent re-spelling -- and for
each rule: how many candidates does it touch, how many of them are finds, what is their median score.  A prior that
works puts the finds in the "lets through" class; one that does not is a tax on the search.

    python scripts/prior_check.py "runs/_ideas/archives/e4k*_control.csv" [--reward long_screen] [--threshold 1.0] [--tag e4k]

Caveat printed with the result: an archive holds the candidates that passed the gates, so what a prior saves by
refusing candidates that would have been DEAD is not visible here (compare the gate-failure rates of the arms).
"""
import collections
import csv
import glob
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.steer import PAIRED, Guidance, is_discovery  # noqa: E402

root = Path(__file__).resolve().parents[1]
argv = sys.argv[1:]


def opt(name, default=None):
    return argv[argv.index(name) + 1] if name in argv else default


KIND, THR, TAG = opt("--reward", "long_screen"), float(opt("--threshold", 1.0)), opt("--tag", "check")
G = Guidance.load(root / opt("--guidance", "guidance/B01.yaml"))


def num(r, k):
    try:
        return float(r.get(k, "nan"))
    except ValueError:
        return float("nan")


rows = []
for p in sorted(glob.glob(str(root / argv[0]))):
    seen = set()
    for r in csv.DictReader(open(p, encoding="utf-8")):
        e = r["expression"]
        try:
            key, w, rules = G.dedup_key(e), G.weight(e), [x.id for x in G.explain(e)]
        except ValueError:
            key, w, rules = e, 1.0, ["(unread)"]
        dup = key in seen
        seen.add(key)
        sc = num(r, "score_p_score")
        live = math.isfinite(num(r, "fitness"))
        find = live and is_discovery(KIND, sc, num(r, "score_p_s_train"), num(r, "score_p_s_valid"), THR)
        rows.append({"file": Path(p).name, "w": w, "rules": rules, "dup": dup, "find": find, "score": sc if live else float("nan")})
n, nf = len(rows), sum(r["find"] for r in rows)
out = {"files": sorted({r["file"] for r in rows}), "n": n, "finds": nf, "classes": {}, "rules": {}}
print(f"{n} archived candidates of {len(out['files'])} control arms; {nf} finds ({KIND}, line {THR:g})\n")
print(f"{'':46s} {'n':>5s} {'share':>6s} {'finds':>6s} {'rate':>6s} {'median score':>13s}")


def grp(name, sel, store):
    S = [r for r in rows if sel(r)]
    if not S:
        return
    sc = sorted(r["score"] for r in S if r["score"] == r["score"])
    f = sum(r["find"] for r in S)
    store[name.strip()] = {"n": len(S), "finds": f, "rate": f / len(S), "median_score": sc[len(sc) // 2] if sc else None}
    print(f"{name:46s} {len(S):5d} {len(S) / n:6.1%} {f:6d} {f / len(S):6.1%} {sc[len(sc) // 2] if sc else float('nan'):+13.2f}")


grp("let through (weight >= 1)", lambda r: r["w"] >= 1 and not r["dup"], out["classes"])
grp("down-weighted (0 < weight < 1)", lambda r: 0 < r["w"] < 1 and not r["dup"], out["classes"])
grp("banned (weight 0)", lambda r: r["w"] <= 0 and not r["dup"], out["classes"])
grp("an equivalent re-spelling of an earlier one", lambda r: r["dup"], out["classes"])
print("by rule (a candidate can hit several):")
for rid, _ in collections.Counter(x for r in rows for x in r["rules"]).most_common(16):
    grp("   " + rid, lambda r, rid=rid: rid in r["rules"], out["rules"])
paid = sum(min(1.0, r["w"]) for r in rows if not r["dup"])
kept = sum(min(1.0, r["w"]) * r["find"] for r in rows if not r["dup"])
out["thinned"] = {"paid": paid, "finds": kept, "per_100": 100 * kept / max(paid, 1e-9), "unfiltered_per_100": 100 * nf / max(n, 1)}
print(f"\nthe same candidates thinned by the guidance (accept with probability = weight, equivalents dropped): {paid:.0f} paid of {n}, {kept:.1f} finds of {nf}"
      f"  ->  {out['thinned']['per_100']:.2f} finds per 100 paid, against {out['thinned']['unfiltered_per_100']:.2f} unfiltered")
print("(archives hold gate-passers only: what the priors save on DEAD candidates is not in this table)")
d = root / "runs" / "_ideas"
d.mkdir(parents=True, exist_ok=True)
(d / f"prior_check_{TAG}.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
