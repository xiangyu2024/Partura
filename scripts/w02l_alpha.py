"""PROD W02L, ruler E of research/prod_W02L/ALPHA_PLAN.md (written before any of this ran): every D-head's book judged by its
alpha on the mined champion's book (time-series regression of daily net excess), heads picked on train only, the picked books
averaged into one leg and merged with the champion at the portfolio level; valid is read.  Server, CPU; `source tmp/w02l_env.sh`
first.  View 2018-01-02 ~ 2025-12-31 (ruler D's): nothing of 2026 is computed.

    python scripts/w02l_alpha.py
"""
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
from partura.steer import Guidance, band_basis, neutral_residual, signal_input  # noqa: E402

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
CHECK_TOL, CHECK_SHARE, A_STEP, T_PICK, RAW_HL = 0.02, 0.95, 0.01, 2.0, (0.0, 5.0, 20.0)   # ALPHA_PLAN.md, fixed in advance


def log(*a):
    print("[alpha]", *a, flush=True)


t0 = time.time()
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
log(f"context: {n} days x {tgt.shape[1]} names, train to {dates[cut - 1]} ({time.time() - t0:.0f}s)")


def daily_long(sm):
    return bk.long_book(bk.long_short_weights(sm, bk.TOP_FRAC), sm, tgt)[0]


# the champions' books (as in w02l_pair.py)
legs = {}
for k in ("X", "H"):
    sig = champ[k]
    ic = dg.ic_row(sig[tr], tgt[tr], target_ranks=dg.rank_rows(tgt[tr]))
    sgn = -1.0 if np.isfinite(ic["rank_ic"]) and ic["rank_ic"] < 0 else 1.0
    hl = bk.fit_halflives(sgn * sig, tgt, tr)["hl_long"]
    legs[k] = daily_long(bk.smoothed(sgn * sig, hl))
    log(f"champion {k}: hl {hl:g}, valid Sharpe {bk.stats(legs[k][va])['sharpe']:.2f}")
x_all, h_all = legs["X"], legs["H"]


def regress(w, regs, sl):
    """w on [1, regs...] over sl: alpha (annualised), its t, betas, appraisal ratio (annualised), corr with the first regressor"""
    cols = [r[sl] for r in regs]
    y = w[sl]
    ok = np.isfinite(y)
    for c in cols:
        ok &= np.isfinite(c)
    y = y[ok]
    X = np.column_stack([np.ones(ok.sum())] + [c[ok] for c in cols])
    b, *_ = np.linalg.lstsq(X, y, rcond=None)
    e = y - X @ b
    s2 = e @ e / (len(y) - X.shape[1])
    se = np.sqrt(s2 * np.linalg.inv(X.T @ X)[0, 0])
    return {"alpha_ann": float(b[0] * 252), "alpha_t": float(b[0] / se), "beta": [float(v) for v in b[1:]],
            "appraisal": float(b[0] / np.sqrt(s2) * np.sqrt(252)), "corr": float(np.corrcoef(y, X[:, 1])[0, 1]), "n": int(ok.sum())}


def judge(w):
    return {seg: {"X": regress(w, [x_all], sl), "XH": regress(w, [x_all, h_all], sl), "own": bk.stats(w[sl])}
            for seg, sl in (("train", tr), ("valid", va))}


# ---------------------------------------------------------------------------------------------------- every head, two books
drec = {}
for line in open(D / "d_scores.jsonl", encoding="utf-8"):
    if line.strip():
        x = json.loads(line)
        if "D" in x:
            drec[x["expr"]] = x["D"]
heads = [h["expr"] for h in json.loads((D / "library" / "heads_D.json").read_text(encoding="utf-8"))]
assert all(e in drec for e in heads)
rows, daily = [], {"D": np.full((len(heads), n), np.nan), "raw": np.full((len(heads), n), np.nan)}
with slot():
    mem = MemoryGuard(self_limit_gb=200, cgroup_limit_gb=850).start()
    P = {}
    for i, e in enumerate(heads):
        if i % 8 == 0:
            ps._mem.clear()
            part = heads[i:i + 8]
            P = ps.compute({f"h{i + j}": x for j, x in enumerate(part)})
            miss = [f"h{i + j}" for j in range(len(part)) if f"h{i + j}" not in P]
            if miss:
                raise SystemExit(f"no panel for {miss}: {[str(ps.errors.get(k))[:120] for k in miss]}")
        z = signal_input(np.asarray(P.pop(f"h{i}"), np.float64))
        rd = drec[e]
        dsm = float(rd["sign"]) * neutral_residual(bk.smoothed(z, float(rd["hl"])), Q)            # ruler D's book
        got = (bk.book_row(dsm, tgt, tr)["long_sharpe"], bk.book_row(dsm, tgt, va)["long_sharpe"])
        best = None                                                                                 # the raw book
        for hl in RAW_HL:
            sm0 = bk.smoothed(z, hl)
            for sgn in (1.0, -1.0):
                s_ = bk.book_row(sgn * sm0, tgt, tr)["long_sharpe"]
                k_ = float(np.nan_to_num(s_, nan=-9e9))
                if best is None or k_ > best[0]:
                    best = (k_, sgn, hl)
        _, rsgn, rhl = best
        daily["D"][i] = daily_long(dsm)
        daily["raw"][i] = daily_long(rsgn * bk.smoothed(z, rhl))
        rows.append({"expr": e, "D_rec": [rd["train"], rd["valid"]], "D_got": [float(got[0]), float(got[1])],
                     "raw_sign": rsgn, "raw_hl": rhl, "D": judge(daily["D"][i]), "raw": judge(daily["raw"][i])})
        if (i + 1) % 20 == 0 or i + 1 == len(heads):
            log(f"heads {i + 1}/{len(heads)} ({time.time() - t0:.0f}s)")
    mem.stop()
dev = np.array([max(abs(r["D_got"][0] - r["D_rec"][0]), abs(r["D_got"][1] - r["D_rec"][1])) for r in rows])
ok_share = float(np.mean(dev <= CHECK_TOL))
log(f"check: {ok_share:.1%} within {CHECK_TOL} of the recorded D (max dev {np.nanmax(dev):.3f})")
if not ok_share >= CHECK_SHARE:
    raise SystemExit("the recomputed D does not match d_scores.jsonl: the plan stops here")
np.savez_compressed(W / "alpha_daily.npz", D=daily["D"], raw=daily["raw"], X=x_all, H=h_all, dates=dates)


# ---------------------------------------------------------------------------------------------------- pick on train, read valid
def st(x):
    s = bk.stats(x)
    return {"ann": s["ann"], "sharpe": s["sharpe"], "mdd": s["mdd"]}


res = {"plan": "research/prod_W02L/ALPHA_PLAN.md", "view": [str(dates[0]), str(dates[-1])], "train_end": str(dates[cut - 1]),
       "check": {"ok_share": ok_share, "max_dev": float(np.nanmax(dev))}, "t_pick": T_PICK, "versions": {}}
for book in ("D", "raw"):
    pick = [i for i, r in enumerate(rows) if r[book]["train"]["X"]["alpha_t"] >= T_PICK]
    v = {"picked": len(pick), "picked_exprs": [rows[i]["expr"] for i in pick],
         "counts": {"train_t>=2": len(pick),
                    "alpha>0_both": sum(r[book]["train"]["X"]["alpha_ann"] > 0 and r[book]["valid"]["X"]["alpha_ann"] > 0 for r in rows),
                    "valid_t>=2_among_picked": sum(rows[i][book]["valid"]["X"]["alpha_t"] >= T_PICK for i in pick)}}
    if pick:
        w = np.nanmean(daily[book][pick], axis=0)
        grid = np.round(np.arange(0.0, 1.0 + 1e-9, A_STEP), 4)
        sh = [bk.stats(a * x_all[tr] + (1 - a) * w[tr])["sharpe"] for a in grid]
        a = float(grid[int(np.nanargmax(sh))])
        v["a"] = a
        v["segments"] = {}
        for seg, sl in (("train", tr), ("valid", va)):
            c, h = a * x_all + (1 - a) * w, 0.5 * x_all + 0.5 * w
            d = (c - x_all)[sl]
            d = d[np.isfinite(d)]
            v["segments"][seg] = {"x": st(x_all[sl]), "w": st(w[sl]), "merged": st(c[sl]), "half": st(h[sl]),
                                  "w_on_x": regress(w, [x_all], sl), "w_on_xh": regress(w, [x_all, h_all], sl),
                                  "merged_minus_x": {"ann": float(d.mean() * 252), "t": float(d.mean() / d.std() * np.sqrt(d.size)) if d.std() > 0 else float("nan")}}
        s = v["segments"]["valid"]
        t_, m_, x_ = s["w_on_x"]["alpha_t"], s["merged"]["sharpe"], s["x"]["sharpe"]
        v["verdict"] = ("在冠军之外有 alpha,合并更好" if t_ >= 2 and m_ > x_ else
                        "方向对、证据不够" if s["w_on_x"]["alpha_ann"] > 0 else "没有")
    res["versions"][book] = v
res["rows"] = rows
(D / "alpha.json").write_text(json.dumps(res, ensure_ascii=False, indent=1, default=float), encoding="utf-8")


def report(r):
    L = ["# 尺子 E:按相对挖掘冠军的 alpha 重筛 W02L 的 head(2026 未算)\n",
         f"做法见 ALPHA_PLAN.md。视窗 {r['view'][0]} ~ {r['view'][1]},train 到 {r['train_end']};纯多头头部十分位、15 bp、减全市场等权的逐日净超额。"
         f"核对:{r['check']['ok_share']:.1%} 的 head 重算的 D 与记录一致(最大差 {r['check']['max_dev']:.3f})。\n",
         "挑选只用 train(对挖掘冠军的 α 的 t ≥ 2);valid 上的 α 没参与挑选，但 head 本身是按 D 在 train + valid 挑的。\n"]
    for book, title in (("D", "D 组合(主)"), ("raw", "原样组合")):
        v = r["versions"][book]
        c = v["counts"]
        L.append(f"## {title}:train 上挑中 {v['picked']} 个;两段 α 都为正的 {c['alpha>0_both']} 个;挑中的里 valid 上 t ≥ 2 的 {c['valid_t>=2_among_picked']} 个\n")
        if not v["picked"]:
            continue
        L += [f"合并比例 a = {v['a']:.2f}(挖掘冠军占 {v['a']:.0%})。**valid 判读:{v['verdict']}**\n",
              "| 段 | 挖掘冠军 | W_E 腿 | 合并(a) | 合并(各半) | 两腿相关 | W_E 对冠军 α(t) | 评估比率 | 对两冠军 α(t) | 合并 − 冠军 |",
              "|---|---|---|---|---|---|---|---|---|---|"]
        for seg, s in v["segments"].items():
            f = lambda z: f"{z['ann']:+.1%} / {z['sharpe']:.2f}"  # noqa: E731
            g, g2 = s["w_on_x"], s["w_on_xh"]
            L.append(f"| {seg} | {f(s['x'])} | {f(s['w'])} | {f(s['merged'])} | {f(s['half'])} | {g['corr']:.2f} | "
                     f"{g['alpha_ann']:+.1%}({g['alpha_t']:+.2f}) | {g['appraisal']:.2f} | {g2['alpha_ann']:+.1%}({g2['alpha_t']:+.2f}) | "
                     f"{s['merged_minus_x']['ann']:+.2%}(t {s['merged_minus_x']['t']:+.2f}) |")
        L.append("")
    L += ["## 两段较差的评估比率最高的 30 个(head × 组合;只作描述)\n",
          "| # | 组合 | train α(t) | valid α(t) | 评估比率 train / valid | 与冠军相关 valid | 自身夏普 valid | head |", "|---|---|---|---|---|---|---|---|"]
    cand = [(min(rw[b]["train"]["X"]["appraisal"], rw[b]["valid"]["X"]["appraisal"]), b, rw) for rw in r["rows"] for b in ("D", "raw")]
    for k, (m, b, rw) in enumerate(sorted(cand, key=lambda t: -t[0])[:30]):
        a_, v_ = rw[b]["train"]["X"], rw[b]["valid"]["X"]
        L.append(f"| {k + 1} | {b} | {a_['alpha_ann']:+.1%}({a_['alpha_t']:+.1f}) | {v_['alpha_ann']:+.1%}({v_['alpha_t']:+.1f}) | "
                 f"{a_['appraisal']:.2f} / {v_['appraisal']:.2f} | {v_['corr']:.2f} | {rw[b]['valid']['own']['sharpe']:.2f} | `{rw['expr'][:90]}` |")
    return "\n".join(L) + "\n"


(D / "alpha.md").write_text(report(res), encoding="utf-8")
print((D / "alpha.md").read_text(encoding="utf-8"))
log(f"done ({time.time() - t0:.0f}s)")
