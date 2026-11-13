"""PROD W02L: the portfolio-level merge of research/prod_W02L/PAIR_PLAN.md (written before any of this ran) -- a W02L book built
the way ruler D sees each head, and the mined champion's own book, combined as two books (not as one signal).  Server, CPU;
`source tmp/w02l_env.sh` first.  View 2018-01-02 ~ 2025-12-31 (ruler D's): nothing of 2026 is computed.

    python scripts/w02l_pair.py
        1. ruler D's basis (5 controls with squares and cubes + the two champions + size / liquidity / price decile dummies);
        2. check: every D-head's D train / valid Sharpe recomputed from runs/prod_W02L/two_level/_signals + that basis vs
           d_scores.jsonl (>= 95% within 0.02, else stop);
        3. legs: X = the mined champion (direction and half-life on train); W79 = the 79 deduplicated heads, each as ruler D
           processes it (z-rank -> EMA at its D half-life -> residual on the basis -> its D sign), z-scored per day, averaged,
           processed once more (rank -> residual); W244 and W79b (the average of the 79 heads' own D books) for description;
        4. merge: a * X + (1 - a) * W, a on train (grid 0.01, max Sharpe), fixed after; -> research/prod_W02L/pair.{json,md}
"""
import hashlib
import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
os.environ.pop("PARTURA_RANK_DEVICE", None)
os.environ.pop("PARTURA_REWARD_DEVICE", None)
from partura.guard import MemoryGuard, limit_threads, slot  # noqa: E402

limit_threads(int(os.environ.get("PARTURA_THREADS", 16)))
import numpy as np  # noqa: E402

from partura import books as bk  # noqa: E402
from partura import diagnose as dg  # noqa: E402
from partura import ops_ext  # noqa: E402,F401
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.panels import SHARED_CACHE, PanelSet  # noqa: E402
from partura.steer import Guidance, band_basis, neutral_residual  # noqa: E402

assert os.environ.get("PARTURA_RANK_FIRST") == "1" and os.environ.get("PARTURA_NEUTRAL_POWERS") == "1,2,3" \
    and os.environ.get("PARTURA_STUDY_DIR") == "prod_W02L", "source tmp/w02l_env.sh first"
START, END, SPLIT = "20180102", "20251231", "20230808"
D = PARTURA_ROOT / "research" / "prod_W02L"
W = PARTURA_ROOT / "runs" / "prod_W02L" / "two_level"
CHAMPS = {"H": "runs/prod_W01/two_level/champions/signal_手写库冠军_20260916.npy",
          "X": "runs/prod_W01/two_level/champions/signal_挖掘冠军_20260916.npy"}
CHAMP_DATES = "runs/prod_W01/two_level/champions/two_level_forward_20260916.json"
STORE = os.environ.get("PARTURA_STORE", "/root/autodl-tmp/qmt_daily_data/fast_factor_compute")
MIRROR = os.environ.get("PARTURA_MIRROR")
MIRROR = MIRROR if MIRROR and os.path.isdir(MIRROR) else None
CHECK_TOL, CHECK_SHARE, A_STEP = 0.02, 0.95, 0.01                     # PAIR_PLAN.md, fixed in advance


def key(e):
    return hashlib.sha1(e.encode()).hexdigest()[:20]


def log(*a):
    print("[pair]", *a, flush=True)


t0 = time.time()
# ---------------------------------------------------------------------------------------------------- ruler D's context
# (the same arithmetic as scripts/w02l_backtest.py --d-jsonl, which wrote d_scores.jsonl)
from alphacube.metrics import zscore_rows  # noqa: E402
from alphacube.plugins import load_plugins  # noqa: E402

load_plugins(["partura.ac_plugin"])
G = Guidance.load(PARTURA_ROOT / "guidance" / "C05_base.yaml")
ps = PanelSet(STORE, START, END, warmup=60, device="cpu", cache_dir=str(SHARED_CACHE), mirror_root=MIRROR, workdir=str(PARTURA_ROOT / "tmp"),
              label_kind="open_vwap15", label_buyable=True, batch=8, daily_root=os.environ.get("PARTURA_DAILY_ROOT") or None)
dates = np.asarray([str(d) for d in ps.dates])
n = len(dates)
cut = int(np.searchsorted(dates, SPLIT))
tgt = np.array(ps.target(1), np.float64)
tr, va = slice(0, cut), slice(cut, n)
known_spec = G.spec["pool"][0]
aux = ps.compute({"liq": "cross_mean(day_sum(Amt), 30)", "known": known_spec["expr"], "n_vol": "cross_mean(day_std(Ret), 20)",
                  "n_rev": "div(day_last(Close), ts_delay(day_last(Close), 20))", "n_size": "LogFloatCap", "price": "day_last(Close)"})
cd = [str(d) for d in json.loads((PARTURA_ROOT / CHAMP_DATES).read_text(encoding="utf-8"))["dates"]]
pos = {d: j for j, d in enumerate(cd)}
take = np.array([pos[d] for d in dates])
champ = {k: np.asarray(np.load(PARTURA_ROOT / f, mmap_mode="r"), np.float64)[take] for k, f in CHAMPS.items()}
ctl5 = [aux["liq"], aux["n_vol"], aux["n_rev"], aux["known"], aux["n_size"]]
Q = band_basis(ctl5 + [champ["H"], champ["X"]], [aux["n_size"], aux["liq"], aux["price"]])
full_dates = np.load(W / "W" / "dates.npy").astype(str)                  # the _signals view (2018-01-02 .. 2026-09-16)
if list(full_dates[:n]) != list(dates):
    raise SystemExit("the _signals view does not start with ruler D's view")
log(f"context: {n} days x {tgt.shape[1]} names, train to {dates[cut - 1]}, basis {Q.shape} ({time.time() - t0:.0f}s)")

# ---------------------------------------------------------------------------------------------------- heads, check
drec = {}
for line in open(D / "d_scores.jsonl", encoding="utf-8"):
    if line.strip():
        x = json.loads(line)
        if "D" in x:
            drec[x["expr"]] = x["D"]
heads = [h["expr"] for h in json.loads((D / "library" / "heads_D.json").read_text(encoding="utf-8"))]
kept = [h["expr"] for h in json.loads((D / "library" / "W_dedup.json").read_text(encoding="utf-8"))["kept"]]
assert set(kept) <= set(heads) and all(e in drec for e in heads)


def processed(e):
    """the head as ruler D processes it (sign included)"""
    z = np.load(W / "_signals" / f"{key(e)}.npy", mmap_mode="r")[:n].astype(np.float64)
    r = drec[e]
    return float(r["sign"]) * neutral_residual(bk.smoothed(z, float(r["hl"])), Q)


def daily_long(sm):
    return bk.long_book(bk.long_short_weights(sm, bk.TOP_FRAC), sm, tgt)[0]


check, acc = [], {"W79": [None, None], "W244": [None, None]}
own79 = []
with slot():
    mem = MemoryGuard(self_limit_gb=200, cgroup_limit_gb=850).start()
    for i, e in enumerate(heads):
        r = processed(e)
        got_tr, got_va = bk.book_row(r, tgt, tr)["long_sharpe"], bk.book_row(r, tgt, va)["long_sharpe"]
        check.append({"expr": e, "D_train": drec[e]["train"], "D_valid": drec[e]["valid"], "got_train": float(got_tr), "got_valid": float(got_va)})
        z = zscore_rows(r)
        for nm in (("W79", "W244") if e in kept else ("W244",)):
            s, c = acc[nm]
            f = np.isfinite(z)
            acc[nm] = [np.where(f, z, 0.0) if s is None else s + np.where(f, z, 0.0), f.astype(np.int32) if c is None else c + f]
        if e in kept:
            own79.append(daily_long(r))
        if (i + 1) % 20 == 0 or i + 1 == len(heads):
            log(f"heads {i + 1}/{len(heads)} ({time.time() - t0:.0f}s)")
    mem.stop()
dev = np.array([max(abs(c["got_train"] - c["D_train"]), abs(c["got_valid"] - c["D_valid"])) for c in check])
ok_share = float(np.mean(dev <= CHECK_TOL))
log(f"check: {ok_share:.1%} of {len(heads)} heads within {CHECK_TOL} of their recorded D (max dev {np.nanmax(dev):.3f})")
(D / "pair_check.json").write_text(json.dumps({"tol": CHECK_TOL, "ok_share": ok_share, "rows": check}, ensure_ascii=False, indent=1), encoding="utf-8")
if not ok_share >= CHECK_SHARE:
    raise SystemExit("the recomputed D does not match d_scores.jsonl: the plan stops here")

# ---------------------------------------------------------------------------------------------------- legs
legs, meta = {}, {}
for nm, (s, c) in acc.items():
    avg = np.where(c > 0, s / np.maximum(c, 1), np.nan)
    sig = neutral_residual(avg, Q)                                       # the average, processed once more (rank -> residual)
    np.save(W / f"W_D{nm[1:]}.npy", sig.astype(np.float32))
    legs[nm] = daily_long(sig)
    meta[nm] = {"heads": len(kept) if nm == "W79" else len(heads), "hl": 0.0}
legs["W79b"] = np.nanmean(np.stack(own79), axis=0)
meta["W79b"] = {"heads": len(kept), "hl": "each head's own"}
for k, nm in (("X", "挖掘冠军"), ("H", "手写库冠军")):
    sig = champ[k]
    ic = dg.ic_row(sig[tr], tgt[tr], target_ranks=dg.rank_rows(tgt[tr]))
    sgn = -1.0 if np.isfinite(ic["rank_ic"]) and ic["rank_ic"] < 0 else 1.0
    hl = bk.fit_halflives(sgn * sig, tgt, tr)["hl_long"]
    legs[nm] = daily_long(bk.smoothed(sgn * sig, hl))
    meta[nm] = {"sign": sgn, "hl": hl}
log("legs: " + ", ".join(f"{k} {bk.stats(v[va])['sharpe']:.2f}" for k, v in legs.items()) + " (valid Sharpe)")


# ---------------------------------------------------------------------------------------------------- merge
def st(x):
    s = bk.stats(x)
    return {"ann": s["ann"], "sharpe": s["sharpe"], "mdd": s["mdd"], "vol": float(np.nanstd(x) * np.sqrt(252))}


def regress(w, x):
    """w on x (daily): alpha (annualised), beta, alpha t, appraisal ratio (annualised)"""
    ok = np.isfinite(w) & np.isfinite(x)
    w, x = w[ok], x[ok]
    X = np.column_stack([np.ones_like(x), x])
    b, *_ = np.linalg.lstsq(X, w, rcond=None)
    e = w - X @ b
    s2 = e @ e / (len(w) - 2)
    se = np.sqrt(s2 * np.linalg.inv(X.T @ X)[0, 0])
    return {"alpha_ann": float(b[0] * 252), "beta": float(b[1]), "alpha_t": float(b[0] / se),
            "appraisal": float(b[0] / np.sqrt(s2) * np.sqrt(252)), "corr": float(np.corrcoef(w, x)[0, 1]), "n": int(ok.sum())}


def merge(xn, wn):
    x, w = legs[xn], legs[wn]
    grid = np.round(np.arange(0.0, 1.0 + 1e-9, A_STEP), 4)
    sh = [bk.stats(a * x[tr] + (1 - a) * w[tr])["sharpe"] for a in grid]
    a = float(grid[int(np.nanargmax(sh))])
    out = {"x": xn, "w": wn, "a": a, "segments": {}}
    for seg, sl in (("train", tr), ("valid", va)):
        c, h = a * x + (1 - a) * w, 0.5 * x + 0.5 * w
        k = np.nanstd(x[tr]) / np.nanstd(c[tr])                          # same volatility as X on train
        rg = regress(w[sl], x[sl])
        sx = bk.stats(x[sl])["sharpe"]
        d = (c - x)[sl]
        d = d[np.isfinite(d)]
        out["segments"][seg] = {"x": st(x[sl]), "w": st(w[sl]), "merged": st(c[sl]), "half": st(h[sl]),
                                "merged_same_vol_ann": float(np.nanmean(k * c[sl]) * 252), "scale": float(k),
                                "w_on_x": rg, "sr_max_theory": float(np.sqrt(sx ** 2 + rg["appraisal"] ** 2)) if sx > 0 else float("nan"),
                                "merged_minus_x": {"ann": float(d.mean() * 252), "t": float(d.mean() / d.std() * np.sqrt(d.size))}}
    return out


res = {"plan": "research/prod_W02L/PAIR_PLAN.md", "view": [str(dates[0]), str(dates[-1])], "train_end": str(dates[cut - 1]),
       "check": {"ok_share": ok_share, "tol": CHECK_TOL, "max_dev": float(np.nanmax(dev))}, "legs": meta,
       "merges": [merge("挖掘冠军", "W79"), merge("挖掘冠军", "W244"), merge("挖掘冠军", "W79b"), merge("手写库冠军", "W79"),
                  merge("挖掘冠军", "手写库冠军")]}
(D / "pair.json").write_text(json.dumps(res, ensure_ascii=False, indent=1, default=float), encoding="utf-8")


def report(r):
    L = ["# 组合层合并:D 口径的 W02L 组合 + 冠军组合(2026 未算)\n",
         f"做法见 PAIR_PLAN.md。视窗 {r['view'][0]} ~ {r['view'][1]},train 到 {r['train_end']}。纯多头头部十分位、15 bp、减全市场等权的逐日净超额。\n",
         f"核对:{r['check']['ok_share']:.1%} 的 head 重算的 D 与记录相差 ≤ {r['check']['tol']}(最大差 {r['check']['max_dev']:.3f})。\n",
         "valid 段对 W 腿偏乐观(head 按 D 的 train 和 valid 较差者挑);a 在 train 上定。\n"]
    for m in r["merges"]:
        L += [f"## {m['x']} + {m['w']}(a = {m['a']:.2f},即 {m['x']} 占 {m['a']:.0%})\n",
              "| 段 | X 腿 | W 腿 | 合并(a) | 合并(0.5) | 两腿相关 | W 对 X 的 alpha(t) | 评估比率 | 理论最优夏普 | 合并 − X |",
              "|---|---|---|---|---|---|---|---|---|---|"]
        for seg, s in m["segments"].items():
            f = lambda z: f"{z['ann']:+.1%} / {z['sharpe']:.2f}"  # noqa: E731
            g = s["w_on_x"]
            L.append(f"| {seg} | {f(s['x'])} | {f(s['w'])} | {f(s['merged'])} | {f(s['half'])} | {g['corr']:.2f} | "
                     f"{g['alpha_ann']:+.1%}({g['alpha_t']:+.2f}) | {g['appraisal']:.2f} | {s['sr_max_theory']:.2f} | "
                     f"{s['merged_minus_x']['ann']:+.2%}(t {s['merged_minus_x']['t']:+.2f}) |")
        L.append("")
    L.append("单元格是「年化净超额 / 夏普」。合并(a)按 train 波动缩放到与 X 同波动后的年化见 pair.json(merged_same_vol_ann)。")
    return "\n".join(L) + "\n"


(D / "pair.md").write_text(report(res), encoding="utf-8")
print((D / "pair.md").read_text(encoding="utf-8"))
log(f"done ({time.time() - t0:.0f}s)")
