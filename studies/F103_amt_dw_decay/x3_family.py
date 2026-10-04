"""X3 -- after S1 / X1 / X2 the tree is  (amount level) x (roughness of the 30-day average intraday Amt curve)^k.
What is still open (hypotheses H13..H18 in notes/05_hypotheses.md, written before this script ran):

A. H13  Is the distilled skeleton the same family as F001's distilled factor cross_max(day_std(Amt), 9)?
B. H14  Do the scale-free concentration measures of the average curve (p_cv, p_peak) carry the signal alone,
        and what do exponent scans of day_sum * X^k look like for them?
C.      Year by year (books at the train-fitted half-life): which skeleton holds up after 2021?
D. H13/H14  Residual rank IC by year after neutralising on the known family.
E. H15  Is the valid long leg of the low-k variants a micro-cap tilt?
F. H16  5x5 dependent sorts amount x {p_peak, p_cv}: is "less concentrated is better" stable in the low-amount rows?
G. H17  Which minute is the peak of the average curve?
H. H18  The book smooths RAW values before ranking: is a monotone transform (log / rank) still a no-op?

Only `train` / `valid` rows are ever touched.
"""
import time

import numpy as np

from partura.study_tools import Study, bk, dg

B = "cross_decay_linear(Amt, 30)"
EXPR = {
    "G": "cross_max(mul(day_close(Amt), ts_min(pow_3(day_durbin_watson(cross_decay_linear(Amt, 30))), 1)), 5)",
    "C": f"day_durbin_watson({B})",
    "dsum": "day_sum(Amt)",
    "C_inner": f"day_durbin_watson(in_slice({B}, 2, 237))",
    "p_cv": f"div(day_std({B}), day_mean({B}))",
    "p_peak": f"div(day_max({B}), day_sum({B}))",
    "p_close": f"div(day_last({B}), day_sum({B}))",
    "p_open": f"div(day_first({B}), day_sum({B}))",
    "p_bar1": f"div(day_sum(in_slice({B}, 1, 1)), day_sum({B}))",
    "argmaxB": f"day_argmax({B})",
    "stdB": f"day_std({B})",
    "skewB": f"day_skew({B})",
    "p_peak15": "div(day_max(cross_decay_linear(Amt, 15)), day_sum(cross_decay_linear(Amt, 15)))",
    "p_peak60": "div(day_max(cross_decay_linear(Amt, 60)), day_sum(cross_decay_linear(Amt, 60)))",
    "p_peak_norm": "day_max(cross_decay_linear(div(Amt, day_sum(Amt)), 30))",
}


def powpos(x, k):
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.where(x > 0, x, np.nan) ** k


def xs_std_log(x, s):
    with np.errstate(divide="ignore", invalid="ignore"):
        lx = np.log(np.where(x[s] > 0, x[s], np.nan).astype(np.float64))
    return float(np.nanmean(np.nanstd(lx, axis=1)))


T0 = time.time()
with Study("F103_amt_dw_decay") as st:
    P = st.panels(EXPR)
    for k in EXPR:
        if k not in P:
            print(f"[x3] MISSING panel {k}")
    P = {k: np.asarray(v, dtype=np.float64) for k, v in P.items()}
    tr, va = st.slice("train"), st.slice("valid")
    use = slice(tr.start, va.stop)                       # train + valid only; holdout rows are never indexed
    cut = va.stop
    tgt = st.target()
    cost, top = float(st.cfg.get("cost_per_side", bk.COST)), float(st.cfg.get("top_frac", bk.TOP_FRAC))
    dates = np.asarray(st.dates)
    years = np.asarray([d[:4] for d in dates])
    yy = sorted(set(years[use].tolist()))
    ysl = {}
    for y in yy:
        idx = np.nonzero(years == y)[0]
        idx = idx[(idx >= tr.start) & (idx < cut)]
        ysl[y] = slice(int(idx[0]), int(idx[-1]) + 1)
    G, C, dsum = P["G"], P["C"], P["dsum"]
    amt = np.asarray(st.control("ctl_amt"), dtype=np.float64)
    cap = np.asarray(st.control("ctl_cap"), dtype=np.float64)
    turn = np.asarray(st.control("ctl_turnrate"), dtype=np.float64)
    std9 = np.asarray(st.control("known_stdamt_max9"), dtype=np.float64)
    amt9 = np.asarray(st.control("known_amt_max9"), dtype=np.float64)
    print(f"[x3] panels ready {time.time() - T0:.0f}s; train {dates[tr][0]}..{dates[tr][-1]}  valid {dates[va][0]}..{dates[va][-1]}", flush=True)

    CAND = {
        "G 原式": G,
        "dsum": dsum,
        "dsum*C": dsum * powpos(C, 1),
        "dsum*C^2": dsum * powpos(C, 2),
        "dsum*C^3": dsum * powpos(C, 3),
        "dsum*p_peak^2": dsum * powpos(P["p_peak"], 2),
        "dsum*p_cv^3": dsum * powpos(P["p_cv"], 3),
        "p_peak": P["p_peak"],
        "p_cv": P["p_cv"],
        "C": C,
        "C_inner": P["C_inner"],
        "stdB": P["stdB"],
        "stdamt9(F001 蒸馏)": std9,
    }

    def row(name, p, extra=""):
        p = np.asarray(p, dtype=np.float64)
        sg = st.sign(p)
        b = st.books(p, fit="train", evals=("train", "valid"), sign=sg)
        s1, s2 = b["splits"]["train"], b["splits"]["valid"]
        i1, i2 = st.ic(p, "train", sign=sg), st.ic(p, "valid", sign=sg)
        alt = b.get("splits_at_hl_long")
        a = (f"  | hlL {b['hl_long']:>2.0f}: Lnet {alt['train']['long_ann'] * 100:+5.1f}%/{alt['valid']['long_ann'] * 100:+5.1f}% "
             f"Lshp {alt['train']['long_sharpe']:+.2f}/{alt['valid']['long_sharpe']:+.2f}") if alt else "  | hlL = hl"
        print(f"{name:26s} {'+' if sg > 0 else '-'} {b['hl_used']:>2.0f} {i1['rank_ic']:+.4f} {i2['rank_ic']:+.4f}  "
              f"{s1['ls_sharpe']:+.2f} {s2['ls_sharpe']:+.2f}  {s1['long_gross_ann'] * 100:+5.1f}%/{s2['long_gross_ann'] * 100:+5.1f}%  "
              f"{s1['long_ann'] * 100:+5.1f}%/{s2['long_ann'] * 100:+5.1f}%  {s1['long_sharpe']:+.2f}/{s2['long_sharpe']:+.2f}  "
              f"{s1['ls_turnover'] * 100:4.1f}% {st.rank_corr(p, G):+.3f}{a}{extra}", flush=True)
        return sg, b["hl_used"]

    HDR = f"{'':26s} s hl  rIC tr  rIC va  LS tr LS va  Lgross tr/va   Lnet tr/va     Lshp tr/va   TO   corrG"

    # ---------- A. 相关矩阵(train):这些骨架彼此、与已知家族是不是同一个东西 ----------
    print("== A. 日截面 rank 相关(train) ==")
    refs = {"ctl_amt": amt, "ctl_cap": cap, "ctl_turn": turn, "amt_max9": amt9}
    mat = dg.rank_corr_matrix({**{k: v[tr] for k, v in CAND.items()}, **{k: v[tr] for k, v in refs.items()}})
    cols = ["G 原式", "dsum", "dsum*C", "dsum*C^2", "dsum*p_peak^2", "p_peak", "p_cv", "C", "stdamt9(F001 蒸馏)", "ctl_amt", "ctl_cap", "ctl_turn"]
    short = {"G 原式": "G", "stdamt9(F001 蒸馏)": "std9", "dsum*p_peak^2": "d*pk^2", "dsum*C^2": "d*C^2", "dsum*C": "d*C"}
    print(f"{'':22s}" + " ".join(f"{short.get(c, c)[:8]:>8s}" for c in cols))
    for n in list(CAND) + ["amt_max9"]:
        print(f"{n:22s}" + " ".join(f"{mat[n][c]:+8.2f}" for c in cols))
    print("log 离散度(日截面 std of log, train): " + "  ".join(
        f"{k} {xs_std_log(P[k], tr):.3f}" for k in ("dsum", "C", "C_inner", "p_cv", "p_peak", "p_peak_norm", "p_peak15", "p_peak60", "stdB"))
          + f"  stdamt9 {xs_std_log(std9, tr):.3f}")
    print(f"[x3] {time.time() - T0:.0f}s", flush=True)

    # ---------- B. 单独的集中度、指数扫描、能不能给 F001 的蒸馏结果加东西 ----------
    print("\n== B. 两本书(方向/半衰期在 train 上定;'hlL' = 按纯多头夏普选的半衰期下的多头腿) ==")
    print(HDR)
    row("G 原式", G)
    row("dsum (k=0)", dsum)
    print("-- 尺度无关的集中度,单独 --")
    for n in ("p_cv", "p_peak", "p_peak_norm", "skewB", "C_inner", "p_close", "p_bar1"):
        row(n, P[n], extra=f"  corr(.,amt) {st.rank_corr(P[n], amt):+.3f}")
    print("-- 已知家族 / 朴素等价物 --")
    row("stdamt9 (F001 蒸馏)", std9)
    row("stdB = day_std(B)", P["stdB"])
    print("-- day_sum * p_peak^k --")
    for k in (1.0, 2.0, 3.0, 5.0):
        row(f"dsum*p_peak^{k:g}", dsum * powpos(P["p_peak"], k))
    print("-- day_sum * p_cv^k --")
    for k in (1.5, 3.0):
        row(f"dsum*p_cv^{k:g}", dsum * powpos(P["p_cv"], k))
    print("-- 窗口 / 归一化方式的邻域(k=2) --")
    for n in ("p_peak15", "p_peak60", "p_peak_norm"):
        row(f"dsum*{n}^2", dsum * powpos(P[n], 2))
    print("-- C 或 p_peak 能不能给 F001 的蒸馏结果加东西 --")
    for k in (1.0, 2.0):
        row(f"stdamt9*C^{k:g}", std9 * powpos(C, k))
    row("stdamt9*p_peak^2", std9 * powpos(P["p_peak"], 2))
    print(f"[x3] {time.time() - T0:.0f}s", flush=True)

    # ---------- H. 保序变换在 "先 EMA 再排名" 的口径下是不是 no-op ----------
    print("\n== H. 同一面板的原值 / log / 截面排名(逐日排名完全相同,只有 EMA 的对象不同) ==")
    print(HDR)
    for n in ("dsum", "dsum*C", "dsum*C^2", "dsum*p_peak^2"):
        x = CAND[n]
        row(f"{n} 原值", x)
        with np.errstate(invalid="ignore", divide="ignore"):
            row(f"log({n})", np.log(np.where(x > 0, x, np.nan)))
        if n in ("dsum*C^2", "dsum*p_peak^2"):
            rk = np.full(x.shape, np.nan)
            rk[:cut] = dg._zrank(x[:cut])
            row(f"rank({n})", rk)
    print(f"[x3] {time.time() - T0:.0f}s", flush=True)

    # ---------- C. 逐年:train 上定的方向/半衰期,逐年各自起一本书 ----------
    print("\n== C. 逐年(方向/半衰期在 train 上定):rank IC(对齐方向后) | 扣费多空夏普 | 多头腿净超额% ==")
    print(f"{'':22s} hl  " + "  ".join(f"{y:>20s}" for y in yy))
    for n in ("G 原式", "dsum", "dsum*C", "dsum*C^2", "dsum*C^3", "dsum*p_peak^2", "dsum*p_cv^3", "p_peak", "p_cv", "stdamt9(F001 蒸馏)"):
        p = CAND[n]
        sg = st.sign(p)
        fit = bk.fit_halflives(sg * p, tgt, tr, cost, top)
        sm = bk.smoothed(sg * p, fit["hl_ls"])
        ric = dg.rank_ic_series(sg * p[use], tgt[use])
        cells = []
        for y in yy:
            r = bk.book_row(sm, tgt, ysl[y], cost, top)
            cells.append(f"{np.nanmean(ric[years[use] == y]):+.4f} {r['ls_sharpe']:+5.2f} {r['long_ann'] * 100:+6.1f}")
        print(f"{n:22s} {fit['hl_ls']:>2.0f}  " + "  ".join(f"{c:>20s}" for c in cells), flush=True)
    print(f"[x3] {time.time() - T0:.0f}s", flush=True)

    # ---------- D. 对已知家族中性化之后还剩什么(原始日频面板,秩空间,逐年 rank IC;负 = 值越高未来越差) ----------
    print("\n== D. 残差 rank IC(原始方向;负 = 值越高未来越差) ==")
    Z = {"amt": dg._zrank(amt[use]), "cap": dg._zrank(cap[use]), "turn": dg._zrank(turn[use]), "std9": dg._zrank(std9[use])}
    TR = dg.rank_rows(tgt[use])
    sets = {"无": [], "amt": ["amt"], "amt+cap+turn": ["amt", "cap", "turn"], "amt+std9": ["amt", "std9"]}
    ntr = tr.stop - tr.start
    print(f"{'':22s} {'中性化对象':14s}  R2    train    valid   | " + "  ".join(f"{y:>7s}" for y in yy))
    for n in ("G 原式", "dsum*C", "dsum*C^2", "dsum*p_peak^2", "p_peak", "p_cv", "C", "C_inner", "stdamt9(F001 蒸馏)"):
        zy = dg._zrank(CAND[n][use])
        for sn, ks in sets.items():
            if n.startswith("stdamt9") and "std9" in ks:
                continue
            if ks:
                res, info = dg.neutralise(zy, {k: Z[k] for k in ks}, panel_ready=True, controls_ready=True)
                r2 = info["mean_r2"]
            else:
                res, r2 = zy, float("nan")
            ric = dg.rank_ic_series(res, tgt[use], target_ranks=TR)
            print(f"{n:22s} {sn:14s} {r2:5.3f}  {np.nanmean(ric[:ntr]):+.4f}  {np.nanmean(ric[ntr:]):+.4f}  | "
                  + "  ".join(f"{np.nanmean(ric[years[use] == y]):+.4f}" for y in yy), flush=True)
    print(f"[x3] {time.time() - T0:.0f}s", flush=True)

    # ---------- E. 多头十分位的市值/成交额位置;对市值中性化之后的两本书 ----------
    print("\n== E. 多头/空头十分位在市值、成交额上的截面百分位(train | valid),以及对 ctl_cap 中性化之后的两本书 ==")
    capP = np.full(cap.shape, np.nan)
    capP[:cut] = dg._zrank(cap[:cut]) + 0.5
    amtP = np.full(amt.shape, np.nan)
    amtP[:cut] = dg._zrank(amt[:cut]) + 0.5
    Zcap = dg._zrank(cap[:cut])
    print(HDR)
    for n in ("G 原式", "dsum", "dsum*C", "dsum*C^2", "dsum*C^3", "dsum*p_peak^2", "p_peak", "stdamt9(F001 蒸馏)"):
        p = CAND[n]
        sg = st.sign(p)
        fit = bk.fit_halflives(sg * p, tgt, tr, cost, top)
        sm = bk.smoothed(sg * p, fit["hl_ls"])
        tilt = []
        for sl in (tr, va):
            w = bk.long_short_weights(sm[sl], top)
            tilt.append(f"多头 cap {np.nanmean(capP[sl][w > 0]):.2f} amt {np.nanmean(amtP[sl][w > 0]):.2f} / "
                        f"空头 cap {np.nanmean(capP[sl][w < 0]):.2f} amt {np.nanmean(amtP[sl][w < 0]):.2f}")
        print(f"{n:22s} hl {fit['hl_ls']:>2.0f}  train: {tilt[0]}  | valid: {tilt[1]}", flush=True)
        res = np.full(p.shape, np.nan)
        r_, info = dg.neutralise(dg._zrank(p[:cut]), {"cap": Zcap}, panel_ready=True, controls_ready=True)
        res[:cut] = r_
        row(f"  {n[:14]} ⟂ cap", res, extra=f"  R2 {info['mean_r2']:.3f}")
    print(f"[x3] {time.time() - T0:.0f}s", flush=True)

    # ---------- F. 5x5:先按成交额五分,再在组内按集中度五分 ----------
    print("\n== F. 先按成交额五分、再在组内按 X 五分:次日超额(年化%,相对当日等权) ==")
    for xn in ("p_peak", "p_cv"):
        X = P[xn]
        for sname, sl in (("train", tr), ("valid", va)):
            tot = np.zeros((5, 5))
            cnt = np.zeros((5, 5))
            for t in range(sl.start, sl.stop):
                a_, c_, y_ = amt[t], X[t], tgt[t]
                m = np.isfinite(a_) & np.isfinite(c_) & np.isfinite(y_)
                if m.sum() < 500:
                    continue
                idx = np.nonzero(m)[0]
                ex = y_[idx] - y_[idx].mean()
                qa_ = np.floor(np.argsort(np.argsort(a_[idx])) / idx.size * 5).astype(int)
                for i in range(5):
                    sub = np.nonzero(qa_ == i)[0]
                    qc_ = np.floor(np.argsort(np.argsort(c_[idx][sub])) / sub.size * 5).astype(int)
                    for j in range(5):
                        tot[i, j] += ex[sub][qc_ == j].mean()
                        cnt[i, j] += 1
            mean = tot / np.maximum(cnt, 1) * 252 * 100
            print(f"[{xn} | {sname}]  列 = {xn} 从低到高;行 = 成交额从低到高")
            print("            X1      X2      X3      X4      X5   | X5-X1")
            for i in range(5):
                print(f"  amt Q{i + 1} " + " ".join(f"{mean[i, j]:+7.1f}" for j in range(5)) + f"  | {mean[i, 4] - mean[i, 0]:+7.1f}")
    print(f"[x3] {time.time() - T0:.0f}s", flush=True)

    # ---------- G. 平均曲线的峰值是哪一分钟 ----------
    print("\n== G. day_argmax(B) 的分布(格子占比 %),以及按峰值位置分组后 p_peak 的 rank IC ==")
    am = P["argmaxB"]
    bins = [("第0根 9:30(开盘集合竞价)", (0, 0)), ("第1根 9:31", (1, 1)), ("第2-30根", (2, 30)), ("第31-236根", (31, 236)),
            ("第237-239根", (237, 239)), ("第240根 15:00(收盘集合竞价)", (240, 240))]
    for sname, sl in (("2018-01..08-17", slice(tr.start, int(np.searchsorted(dates, "20180820")))),
                      ("train 其余", slice(int(np.searchsorted(dates, "20180820")), tr.stop)), ("valid", va)):
        a_ = am[sl]
        fin = np.isfinite(a_)
        print(f"{sname:16s} " + "  ".join(f"{bn}: {((a_ >= lo) & (a_ <= hi) & fin).sum() / max(fin.sum(), 1) * 100:.1f}%" for bn, (lo, hi) in bins))
    for gname, (lo, hi) in (("峰值在开盘(第0-1根)", (0, 1)), ("峰值在收盘竞价(第240根)", (240, 240)), ("峰值在别处(第2-239根)", (2, 239))):
        sel = (am[use] >= lo) & (am[use] <= hi)
        ric = dg.rank_ic_series(np.where(sel, P["p_peak"][use], np.nan), np.where(sel, tgt[use], np.nan))
        nn = sel.sum(1).mean()
        ex = np.where(sel & np.isfinite(tgt[use]), tgt[use] - np.nanmean(tgt[use], axis=1, keepdims=True), np.nan)
        print(f"{gname:22s} 平均 {nn:6.0f} 只/天   p_peak 组内 rank IC: train {np.nanmean(ric[:ntr]):+.4f}  valid {np.nanmean(ric[ntr:]):+.4f}"
              f"   组的次日超额(年化): train {np.nanmean(np.nanmean(ex[:ntr], axis=1)) * 252 * 100:+.1f}%  valid {np.nanmean(np.nanmean(ex[ntr:], axis=1)) * 252 * 100:+.1f}%")
    print(f"p_peak 与 p_close / p_bar1 / p_open 的 rank 相关(train): {st.rank_corr(P['p_peak'], P['p_close']):+.3f} / "
          f"{st.rank_corr(P['p_peak'], P['p_bar1']):+.3f} / {st.rank_corr(P['p_peak'], P['p_open']):+.3f}")
    print(f"[x3] done {time.time() - T0:.0f}s", flush=True)
