"""Simple fusion of the upgraded versions of a batch, in and out of sample.

Members are chosen by a rule that reads the TRAINING period only (``runs/<fid>/sweepfinal_<tag>.json`` for the
candidates a fixed rule picked on train / valid; ``runs/_batch_<B>/cluster_<tag>.json`` for which of them belong to
the known family):

    orig    every factor's original expression                                              (the "before")
    upg     per factor, its rule-picked candidate with the best training pure-long Sharpe, whatever its family
    indep   per factor, its best own candidate that is NOT in a known-family cluster, if that candidate's
            training pure-long Sharpe is >= 1.5 (so: at most one per factor, and only its own content)
    known   the head of the best known-family cluster

Fusions -- the mean of the members' daily cross-sectional z-ranks (a name needs at least half of the members):

    O = orig, equal weights          U = upg, equal weights            A = indep, equal weights
    B = known alone                  C = indep + known, equal weights  D = 0.5 known + 0.5 mean(indep)

Two ways to smooth.  ``each``: every member is first smoothed at its own half-life (the one its pure long book
prefers on the training period), the smoothed members are fused, and the fusion is smoothed once more.  ``once``:
the raw members are fused and the fusion is smoothed once.  Every half-life of the grid is scored on both
periods; the half-life "chosen" is the one the pure long book prefers on the training period.

The test period of every fusion is read here -- one ledgered read.

    python scripts/batch_fuse.py batches/B01_single_factors.yaml [--tag s2] [--min-sharpe 1.5]
"""
import json
import math
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.guard import MemoryGuard, limit_threads, slot  # noqa: E402

limit_threads(4)
import numpy as np  # noqa: E402
import yaml  # noqa: E402

from partura import books as bk  # noqa: E402
from partura import diagnose as dg  # noqa: E402
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.panels import SHARED_CACHE, PanelSet  # noqa: E402
from partura.splits import SPLITS, Ledger  # noqa: E402

argv = sys.argv[1:]


def opt(name, default=None):
    return argv[argv.index(name) + 1] if name in argv else default


TAG = opt("--tag", "s2")
SH_MIN = float(opt("--min-sharpe", 1.5))
batch = yaml.safe_load(open(PARTURA_ROOT / argv[0], encoding="utf-8"))
bname = Path(argv[0]).stem.split("_")[0]
first = yaml.safe_load(open(PARTURA_ROOT / "configs" / f"{batch['factors'][0]['id']}.yaml", encoding="utf-8"))
for k, v in first["splits"].items():
    SPLITS[k] = (str(v[0]), str(v[1]))
K = json.loads((PARTURA_ROOT / "runs" / f"_batch_{bname}" / f"cluster_{TAG}.json").read_text(encoding="utf-8"))
key_of = {v["expr"].replace(" ", ""): k for k, v in K["info"].items()}
# each candidate's OWN verdict (batch_cluster measures it per candidate); older cluster files only have the head's
known_fam = {k: (v["known_like"] if v.get("known_like") is not None else None) for k, v in K["info"].items()}
for c in K["clusters"]:
    for m in c["members"]:
        if known_fam.get(m) is None:
            known_fam[m] = c["known_family"]


def train_sharpe(key):
    x = K["info"][key]["books"]["utrain"]["long_sharpe"]
    return x if x == x else -9.0


members, groups = {}, {"orig": [], "upg": [], "indep": []}
bench = {}
for f in batch["factors"]:
    fid, s = f["id"], f["id"].split("_")[0]
    F = json.loads((PARTURA_ROOT / "runs" / fid / f"sweepfinal_{TAG}.json").read_text(encoding="utf-8"))
    R = F["results"]

    def put(cid, name):
        r = R[cid]
        members[name] = {"expr": r["expr"], "sign": float(r["sign_user"]), "hl": float(r["books_user"]["by_rank"]["long"]["hl"]),
                         "fid": fid, "cid": cid, "kind": r["kind"], "cluster_key": key_of.get(r["expr"].replace(" ", "")),
                         **{x: (K["info"].get(key_of.get(r["expr"].replace(" ", "")), {}) or {}).get(x) for x in ("known_like", "rho_known", "ovl_known", "ovl_known_xfrozen")}}
        return name

    for b, name in (("k_known", "known"), ("k_known_xfrozen", "known_xfrozen")):
        if b in R and name not in bench:
            bench[name] = {"expr": R[b]["expr"], "sign": float(R[b]["sign_user"]), "hl": float(R[b]["books_user"]["by_rank"]["long"]["hl"])}
    groups["orig"].append(put("v_base", f"{s}.orig"))
    cand = [(c, key_of.get(R[c]["expr"].replace(" ", ""))) for c in R if c not in ("v_base", "k_known", "k_known_xfrozen")]
    cand = [(c, k) for c, k in cand if k is not None]
    best = max(cand, key=lambda ck: train_sharpe(ck[1]), default=None)
    if best and train_sharpe(best[1]) > train_sharpe(key_of[R["v_base"]["expr"].replace(" ", "")]):
        groups["upg"].append(put(best[0], f"{s}.{best[0]}"))
    else:
        groups["upg"].append(f"{s}.orig")
    own = [(c, k) for c, k in cand if c in F["picks"] and known_fam.get(k) is False and "day_std(Amt)" not in R[c]["expr"]]
    bi = max(own, key=lambda ck: train_sharpe(ck[1]), default=None)
    if bi and train_sharpe(bi[1]) >= SH_MIN:
        groups["indep"].append(put(bi[0], f"{s}.{bi[0]}"))
kh = K["known_head"]
members["known_head"] = {"expr": K["info"][kh]["expr"], "sign": float(K["info"][kh]["sign"]), "hl": float(K["info"][kh]["hl"]),
                         "fid": K["info"][kh].get("fid"), "cid": K["info"][kh].get("cid"), "kind": K["info"][kh].get("kind"), "cluster_key": kh}
for name, b in bench.items():
    members[name] = {**b, "fid": "", "cid": name, "kind": "bench", "cluster_key": name}
print(f"[fuse] {bname} {TAG}: orig {len(groups['orig'])}, upg {len(groups['upg'])}, indep {len(groups['indep'])}, known head {kh}", flush=True)
for g in ("upg", "indep"):
    print(f"  {g}: " + ", ".join(groups[g]), flush=True)

with slot():
    mem = MemoryGuard(self_limit_gb=34, cgroup_limit_gb=70).start()
    t0 = time.time()
    ps = PanelSet("/root/autodl-tmp/qmt_daily_data/fast_factor_compute", SPLITS["full"][0], SPLITS["full"][1],
                  warmup=int(first.get("warmup", 60)), device="cuda", gpu_fraction=0, cache_dir=str(SHARED_CACHE),
                  mirror_root="/root/autodl-tmp/AlphaCube/mirror", workdir=str(PARTURA_ROOT / "tmp"),
                  label_kind="open_vwap15", label_buyable=True, batch=8)
    P = ps.compute({k: v["expr"] for k, v in members.items()})
    tgt = ps.target(1)
    us, ho = ps.split_slice("utrain"), ps.split_slice("holdout")
    yrs = ps.years
    from alphacube.metrics import long_short_weights

    def by_year_net(sm):
        out = {}
        for y in sorted(set(yrs)):
            d = np.nonzero(yrs == y)[0]
            sl = slice(int(d[0]), int(d[-1]) + 1)
            w = long_short_weights(sm[sl], bk.TOP_FRAC)
            out[str(y)] = float(np.nanmean(bk.long_book(w, sm[sl], tgt[sl])[0]) * 252)
        return out

    def daily(sm):
        """Net excess of the pure long book, one continuous book over the whole period (for the equity curve)."""
        w = long_short_weights(sm, bk.TOP_FRAC)
        return [None if x != x else round(float(x), 7) for x in bk.long_book(w, sm, tgt)[0]]

    def rows(sm):
        return {"train": bk.book_row(sm, tgt, us), "test": bk.book_row(sm, tgt, ho)}

    Zs, Zr = {}, {}
    for k, v in members.items():
        raw = v["sign"] * np.asarray(P[k], dtype=np.float64)
        sm = bk.smoothed(raw, v["hl"])
        v["rows"] = rows(sm)
        v["by_year_long_net"] = by_year_net(sm)
        if k in ("known", "known_xfrozen", "known_head"):
            v["daily"] = daily(sm)
        Zs[k] = dg._zrank(sm).astype(np.float32)
        Zr[k] = dg._zrank(raw).astype(np.float32)
    print(f"[fuse] {len(members)} members ready in {time.time() - t0:.0f}s", flush=True)

    def fuse(keys, Z, weights=None):
        z = np.stack([Z[k] for k in keys]).astype(np.float64)
        w = np.asarray(weights if weights is not None else [1.0] * len(keys), dtype=np.float64)[:, None, None]
        fin = np.isfinite(z)
        with np.errstate(invalid="ignore", divide="ignore"):
            out = (np.where(fin, z, 0.0) * w).sum(0) / (fin * w).sum(0)
        return np.where(fin.sum(0) >= math.ceil(len(keys) / 2), out, np.nan)

    def half(keys, Z):
        a, b = fuse(keys, Z), Z["known_head"].astype(np.float64)
        return np.where(np.isfinite(a) & np.isfinite(b), 0.5 * a + 0.5 * b, np.nan)

    plan = {"O": ("原式等权", groups["orig"], lambda Z: fuse(groups["orig"], Z)),
            "U": ("升级版等权(每条因子一个,不论哪一族)", groups["upg"], lambda Z: fuse(groups["upg"], Z)),
            "A": ("独立的升级版等权", groups["indep"], lambda Z: fuse(groups["indep"], Z)),
            "B": ("已知族里最好的升级版,单独", ["known_head"], lambda Z: Z["known_head"].astype(np.float64)),
            "C": ("独立的升级版 + 已知族最好的一个,等权", groups["indep"] + ["known_head"], lambda Z: fuse(groups["indep"] + ["known_head"], Z)),
            "D": ("一半已知族最好的一个 + 一半独立升级版的均值", ["known_head"] + groups["indep"], lambda Z: half(groups["indep"], Z))}
    fusions = {}
    for name, (label, keys, build) in plan.items():
        fusions[name] = {"label": label, "members": keys, "methods": {}}
        for method, Z in (("each", Zs), ("once", Zr)):
            sig = build(Z)
            grid, best = [], None
            for hl in bk.HALFLIVES:
                sm = bk.smoothed(sig, hl)
                r = rows(sm)
                grid.append({"hl": float(hl), **r})
                key = float(np.nan_to_num(r["train"]["long_sharpe"], nan=-9e9))
                if best is None or key > best[0]:
                    best = (key, float(hl), sm)
            fusions[name]["methods"][method] = {"grid": grid, "chosen_hl": best[1], "by_year_long_net": by_year_net(best[2]), "daily": daily(best[2])}
            c = next(g for g in grid if g["hl"] == best[1])
            print(f"  {name} {method:4s} hl {best[1]:>3g} | 训练 {c['train']['long_ann']:+6.1%} 夏普 {c['train']['long_sharpe']:+.2f} | "
                  f"测试 {c['test']['long_ann']:+6.1%} 夏普 {c['test']['long_sharpe']:+.2f} | {label}", flush=True)
    Ledger(PARTURA_ROOT / "runs" / f"_batch_{bname}" / "ledger.json").record(
        "holdout", len(plan) * 2, f"batch fuse {TAG}: fusions O/U/A/B/C/D x (each, once), members chosen by a fixed rule on utrain; "
        "every half-life of the grid scored on both periods", f"batch_fuse_{TAG}")
    mem.stop()

out = {"batch": bname, "tag": TAG, "rule": __doc__.split("    python")[0].strip(), "min_sharpe": SH_MIN,
       "split": {"train": list(SPLITS["utrain"]), "test": list(SPLITS["holdout"])}, "dates": list(ps.dates),
       "groups": groups, "known_head": kh,
       "members": {k: {x: v.get(x) for x in ("expr", "sign", "hl", "fid", "cid", "kind", "cluster_key", "known_like", "rho_known", "ovl_known", "ovl_known_xfrozen", "rows", "by_year_long_net", "daily")} for k, v in members.items()},
       "fusions": fusions}
p = PARTURA_ROOT / "runs" / f"_batch_{bname}" / f"fuse_{TAG}.json"
p.write_text(json.dumps(out, ensure_ascii=False, default=float), encoding="utf-8")
print(f"\nwrote {p} ({time.time() - t0:.0f}s)")
