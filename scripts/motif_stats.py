"""What did the batch sweeps teach about ACTIONS?  Evidence for search priors, from our own scored variants.

Every sweep scores a few hundred variants of one factor, and a large share of them are the SAME intervention applied
to fifteen different bases (wrap in a day-axis memory, fold, rank, screen ...) or a single-node edit of the base
(delete this node, replace this operator by that one, swap this leaf).  Each is a paired experiment: variant against
its own base, same data, same convention.  Pooled over the batch they say which actions help, which do nothing and
which destroy the long leg -- the raw material for an operator / sub-structure prior in the search.

Local, reads runs/<fid>/sweep_<tag>.json only (train / valid; no test period):

    python scripts/motif_stats.py batches/B01_single_factors.yaml [--tag s2]

Writes guidance/motif_stats_<tag>.json and prints the tables.  "d" below is the change in the pure-long Sharpe on
the user's training period (variant minus its base); "both" is the share of cases where the long-leg net excess
improves on train AND on valid; "dead" is the share that fails the gates (constant / too few distinct values /
coverage) -- an invalid-expression rate.
"""
import json
import re
import statistics as st
import sys
from collections import defaultdict
from pathlib import Path

import yaml

root = Path(__file__).resolve().parents[1]
argv = sys.argv[1:]
TAG = argv[argv.index("--tag") + 1] if "--tag" in argv else "s2"
batch = yaml.safe_load(open(root / argv[0], encoding="utf-8"))
NOISE = 0.3          # pure-long Sharpe: differences inside this band are not read


def shp(v, split="utrain_long"):
    x = (v.get(split) or {}).get("long_sharpe")
    return x if x is not None and x == x else None


def ann(v, split):
    x = (v.get(split) or {}).get("long_ann")
    return x if x is not None and x == x else None


def gate_fail(v):
    return bool(v.get("dead")) or v.get("cov", 1) < 0.95 or v.get("dist", 1) < 0.5


rows = []            # one per variant: (factor, id, kind, why, expr, d_sharpe, both, dead, rho_orig, rho_known, against)
for f in batch["factors"]:
    p = root / "runs" / f["id"] / f"sweep_{TAG}.json"
    if not p.is_file():
        continue
    R = json.loads(p.read_text(encoding="utf-8"))["results"]
    base, known = R.get("v_base"), R.get("k_known")
    for k, v in R.items():
        if v["kind"] in ("base", "bench"):
            continue
        ref = known if v["kind"] in ("overlay", "screen") or (v["kind"] == "hypo" and "day_std(Amt)" in v["expr"]) else base
        dead = gate_fail(v)
        d = both = None
        if not dead and ref and shp(v) is not None and shp(ref) is not None:
            d = shp(v) - shp(ref)
            a, b = ann(v, "train_long"), ann(v, "valid_long")
            ra, rb = ann(ref, "train_long"), ann(ref, "valid_long")
            both = None if None in (a, b, ra, rb) else bool(a > ra and b > rb)
        rows.append({"f": f["id"].split("_")[0], "id": k, "kind": v["kind"], "why": str(v.get("why") or ""), "expr": v["expr"], "d": d, "both": both,
                     "dead": dead, "ro": v.get("corr_orig"), "rk": v.get("corr_known"), "sh": shp(v), "against": "known" if ref is known else "base"})


def agg(rs):
    ds = [r["d"] for r in rs if r["d"] is not None]
    bs = [r["both"] for r in rs if r["both"] is not None]
    ro = [abs(r["ro"]) for r in rs if r["ro"] is not None and r["ro"] == r["ro"]]
    # n counts every variant of the group; the shares (up / down / both) and the medians are over n_live, the
    # ones that passed the gates and have a base to be compared with -- two different denominators, both reported
    return {"n": len(rs), "n_live": len(ds), "factors": len({r["f"] for r in rs}), "factors_live": len({r["f"] for r in rs if r["d"] is not None}),
            "dead": sum(r["dead"] for r in rs) / max(len(rs), 1),
            "d_median": st.median(ds) if ds else None, "d_mean": st.mean(ds) if ds else None,
            "up": sum(d > NOISE for d in ds) / len(ds) if ds else None, "down": sum(d < -NOISE for d in ds) / len(ds) if ds else None,
            "both": sum(bs) / len(bs) if bs else None, "rho_orig_median": st.median(ro) if ro else None}


def table(title, groups, min_n=3, sort="d_median"):
    out = {k: agg(v) for k, v in groups.items() if len(v) >= min_n}
    print(f"\n== {title}(n ≥ {min_n};d = 训练段纯多头夏普的变化,变体 − 它自己的底座)")
    print(f"{'动作':34s} {'n':>4s} {'可用':>4s} {'因子数':>5s} {'废品率':>6s} {'d 中位':>7s} {'d 均值':>7s} {'升>0.3':>7s} {'降>0.3':>7s} {'两段都升':>8s} {'ρ原式':>6s}")
    for k, a in sorted(out.items(), key=lambda kv: -(kv[1][sort] if kv[1][sort] is not None else -9)):
        f = lambda x, p=False: "    —" if x is None else (f"{x:6.0%}" if p else f"{x:+6.2f}")  # noqa: E731
        print(f"{k[:34]:34s} {a['n']:4d} {a['n_live']:4d} {a['factors']:5d} {a['dead']:6.0%} {f(a['d_median']):>7s} {f(a['d_mean']):>7s} {f(a['up'], 1):>7s} {f(a['down'], 1):>7s} {f(a['both'], 1):>8s} "
              f"{'   —' if a['rho_orig_median'] is None else format(a['rho_orig_median'], '6.2f')}")
    return out


# 1. the generic wrappers: the same outer action on every base
G = defaultdict(list)
for r in rows:
    if r["kind"] in ("memory", "shape", "neutral", "overlay", "screen", "segment") or r["id"] in ("rk", "win", "z60", "rel60"):
        G[re.sub(r"\d+$", "", r["id"]) if r["kind"] == "memory" else r["id"]].append(r)
W = table("通用外层动作(同一个动作套在每条因子上;叠加 / 筛子类是和已知族比,其余和原式比)", G, min_n=8)
Gm = defaultdict(list)
for r in rows:
    if r["kind"] == "memory":
        Gm[r["id"]].append(r)
Wm = table("日轴记忆 × 窗口", Gm, min_n=8)

# 2. deleting a node: which operators are passengers
A = defaultdict(list)
for r in rows:
    m = re.search(r"删掉 \w+ = ([A-Za-z_0-9]+)", r["why"])
    # create_like(X, c) "deleted" is replaced by its shape donor X, not by nothing: those rows mix removing an
    # epsilon, removing a mask's zero branch and removing the 1 of "ratio - 1", and say nothing about any of them
    if r["kind"] == "ablate" and m and m.group(1) != "create_like":
        A[m.group(1)].append(r)
AB = table("删掉一个节点(d ≈ 0 且 ρ原式 ≈ 1 = 这个节点是乘客)", A, min_n=2, sort="rho_orig_median")

# 3. replacing one operator by another
S, SB, SA = defaultdict(list), defaultdict(list), defaultdict(list)
for r in rows:
    m = re.match(r"([A-Za-z_0-9]+)(?:\s*[((][^))]*[))])? → ([A-Za-z_0-9]+)", r["why"])
    if r["kind"] == "substitute" and m:
        S[f"{m.group(1)} → {m.group(2)}"].append(r)
        SB[f"→ {m.group(2)}"].append(r)
        SA[f"{m.group(1)} →"].append(r)
unmatched = sum(1 for r in rows if r["kind"] == "substitute" and not re.match(r"([A-Za-z_0-9]+)(?:\s*[((][^))]*[))])? → ([A-Za-z_0-9]+)", r["why"]))
print(f"\n(substitute rows whose pair could not be read from `why`: {unmatched})")
ST = table("把算子 A 换成 B(成对)", S, min_n=3)
STB = table("换进来的算子 B(不论换掉谁)", SB, min_n=4)
STA = table("被换掉的算子 A(不论换成谁;d 很负 = 这个算子不可替代)", SA, min_n=4)

# 4. leaves and fields
LF = defaultdict(list)
for r in rows:
    if r["kind"] in ("leaf", "field"):
        m = re.search(r"(?:叶子|字段) (\S+) (?:换成|→) (.+?)(?:\(|:|$)", r["why"])
        LF[(m.group(1) + " → " + m.group(2).strip()) if m else r["id"]].append(r)
LT = table("换叶子 / 换字段", LF, min_n=2)

out = {"tag": TAG, "n_variants": len(rows), "substitute_unmatched": unmatched, "noise_band": NOISE, "dead_rate": sum(r["dead"] for r in rows) / max(len(rows), 1),
       "wrappers": W, "memory_by_window": Wm, "ablate_by_operator": AB, "substitute_pairs": ST, "substitute_incoming": STB,
       "substitute_outgoing": STA, "leaf_field": LT,
       "note": "paired within factor: variant minus its own base (overlay / screen kinds: minus the known-family benchmark); train+valid only"}
d = root / "guidance"
d.mkdir(exist_ok=True)
(d / f"motif_stats_{TAG}.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"\n{len(rows)} variants; overall dead rate {out['dead_rate']:.1%}; wrote guidance/motif_stats_{TAG}.json")
