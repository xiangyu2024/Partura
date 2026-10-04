"""X1 -- anatomy of F103's two operands, before any stage is designed.

Questions (each is about THIS tree; none is answered by a stock diagnostic):

1. Is `ts_min(., 1)` an exact identity?                                (node removal)
2. What sits in the first / last bars of the 241 grid?  Is `day_close(Amt)` the closing
   call auction, and did it change for Shanghai on 2018-08-20?         (H9)
3. In log space G ~ log A + 3 log C.  Which operand owns the cross-sectional ranking,
   and are A and C related?                                            (H5, H6)
4. What is C = DW(30-day average intraday Amt curve) made of: auction spikes (H2),
   interior lumpiness (H3), or the level of trading?  Does averaging first matter (H4)?
5. Exponent scan k in A * C^k (numerical rebuild, self-checked against the engine at k=3).
6. What does each decile of the traded signal look like on the known exposures, and how
   many of its labels are missing (locked at limit-up)?                (H8, H8b)

Only `train` / `valid` rows are ever touched.
"""
import time

import numpy as np

from partura.study_tools import Study, bk, dg

B = "cross_decay_linear(Amt, 30)"
EXPR = {
    "G": "cross_max(mul(day_close(Amt), ts_min(pow_3(day_durbin_watson(cross_decay_linear(Amt, 30))), 1)), 5)",
    "G_nomin": "cross_max(mul(day_close(Amt), pow_3(day_durbin_watson(cross_decay_linear(Amt, 30)))), 5)",
    "A": "day_close(Amt)",
    "C": f"day_durbin_watson({B})",
    "dsum": "day_sum(Amt)",
    "bar0": "day_sum(in_slice(Amt, 0, 0))",
    "bar1": "day_sum(in_slice(Amt, 1, 1))",
    "bar238_239": "day_sum(in_slice(Amt, 238, 239))",
    "bar240": "day_sum(in_slice(Amt, 240, 240))",
    "C_inner": f"day_durbin_watson(in_slice({B}, 2, 237))",
    "p_close": f"div(day_last({B}), day_sum({B}))",
    "p_open": f"div(day_first({B}), day_sum({B}))",
    "p_cv": f"div(day_std({B}), day_mean({B}))",
    "dw_today": "day_durbin_watson(Amt)",
    "C_swap": "cross_decay_linear(day_durbin_watson(Amt), 30)",
    "cv_today": "div(day_std(Amt), day_mean(Amt))",
    # C mixes three things: per-minute lumpiness, the fixed auction bars, and DAY-level burstiness
    # (B averages raw amounts, so one 10x-volume day owns the average curve and its noise is not averaged out)
    "amt_cv30": "div(cross_stddev(day_sum(Amt), 30), cross_mean(day_sum(Amt), 30))",
    "amt_peak30": "div(cross_max(day_sum(Amt), 30), cross_mean(day_sum(Amt), 30))",
    "C_norm": "day_durbin_watson(cross_decay_linear(div(Amt, day_sum(Amt)), 30))",
}


def rmax(x, d):
    out = x.copy()
    for k in range(1, d):
        sh = np.full_like(x, np.nan)
        sh[k:] = x[:-k]
        out = np.fmax(out, sh)
    return out


def rmean(x, d):
    s = np.zeros(x.shape, dtype=np.float64)
    n = np.zeros(x.shape, dtype=np.float64)
    for k in range(d):
        sh = np.full(x.shape, np.nan)
        sh[k:] = x[:x.shape[0] - k] if k else x
        ok = np.isfinite(sh)
        s += np.where(ok, sh, 0.0)
        n += ok
    return np.where(n > 0, s / np.maximum(n, 1), np.nan)


def xs_std_log(x, s):
    with np.errstate(divide="ignore", invalid="ignore"):
        lx = np.log(np.where(x[s] > 0, x[s], np.nan).astype(np.float64))
    return float(np.nanmean(np.nanstd(lx, axis=1)))


def pct(x):
    return dg._zrank(x) + 0.5


T0 = time.time()
with Study("F103_amt_dw_decay") as st:
    P = st.panels(EXPR)
    print("[x1] panels:", sorted(P), f"{time.time() - T0:.0f}s", flush=True)
    tr, va = st.slice("train"), st.slice("valid")
    tgt = st.target()
    dates = np.asarray(st.dates)
    syms = np.asarray(st.symbols)
    print("[x1] dates", dates[0], dates[tr][-1], dates[va][0], dates[va][-1], "| symbols", list(syms[:3]), list(syms[-3:]), len(syms))
    G, A, C, dsum = P["G"], P["A"], P["C"], P["dsum"]

    # ---------- 1. ts_min(., 1) ----------
    print("\n== 1. ts_min(.,1) 是不是恒等 ==")
    g2 = P["G_nomin"]
    same_nan = float((np.isfinite(G[tr]) == np.isfinite(g2[tr])).mean())
    both = np.isfinite(G[tr]) & np.isfinite(g2[tr])
    rel = np.abs(G[tr][both] - g2[tr][both]) / np.maximum(np.abs(G[tr][both]), 1e-30)
    print(f"rank corr(G, G 去掉 ts_min) = {st.rank_corr(G, g2):.6f}; NaN 位置一致率 {same_nan:.6f}; 最大相对差 {rel.max():.3e}")

    # ---------- 2. 241 网格首尾放的是什么 ----------
    print("\n== 2. 首尾分钟的成交额占全天的比例(格子中位数) ==")
    is_sh = np.asarray([s.startswith("6") or s.upper().endswith("SH") or s.upper().startswith("SH") for s in syms])
    is_sz = np.asarray([(s[:1] in "03" or s.upper().endswith("SZ") or s.upper().startswith("SZ")) and not sh
                        for s, sh in zip(syms, is_sh)])
    print(f"沪市 {is_sh.sum()} 只, 深市 {is_sz.sum()} 只, 其他 {(~is_sh & ~is_sz).sum()} 只")
    periods = {"2018-01-02~08-17": (dates >= "20180102") & (dates <= "20180817"),
               "2018-08-20~2021": (dates >= "20180820") & (dates <= "20211231"),
               "valid": (dates >= "20220101") & (dates <= "20230807")}
    with np.errstate(divide="ignore", invalid="ignore"):
        shares = {k: P[k] / dsum for k in ("bar0", "bar1", "bar238_239", "bar240", "A") if k in P}
    for pn, dm in periods.items():
        for en, em in (("沪", is_sh), ("深", is_sz)):
            cells = np.ix_(dm, em)
            line = [f"{pn} {en}:"]
            for k, v in shares.items():
                x = v[cells]
                line.append(f"{k}/全天 中位 {np.nanmedian(x) * 100:.2f}% (==0: {np.mean(x[np.isfinite(x)] == 0) * 100:.1f}%)")
            if "bar240" in P:
                a_eq = np.isfinite(A[cells]) & np.isfinite(P["bar240"][cells])
                eq = np.mean(np.isclose(A[cells][a_eq], P["bar240"][cells][a_eq], rtol=1e-5)) if a_eq.any() else np.nan
                line.append(f"A==bar240 {eq * 100:.1f}%; bar240 有值的格子占 A 有值的 {a_eq.sum() / max(np.isfinite(A[cells]).sum(), 1) * 100:.1f}%")
            print("  ".join(line))

    # ---------- 3. 谁决定排名 ----------
    print("\n== 3. log 空间里两支的离散度与关系(train) ==")
    A5 = rmax(A, 5)
    with np.errstate(divide="ignore", invalid="ignore"):
        share_today = A / dsum
    print(f"日截面 std: log A = {xs_std_log(A, tr):.3f}, log max5(A) = {xs_std_log(A5, tr):.3f}, "
          f"log C = {xs_std_log(C, tr):.3f} (x3 = {3 * xs_std_log(C, tr):.3f}), log G = {xs_std_log(G, tr):.3f}, "
          f"log day_sum = {xs_std_log(dsum, tr):.3f}")
    ctl = {n: st.control(n) for n in ("ctl_amt", "ctl_cap", "ctl_turnrate", "ctl_ivol", "ctl_mom20", "ctl_rev1",
                                      "ctl_price", "ctl_dvol20", "known_amt_max9", "known_stdamt_max9")}
    others = {"A": A, "max5(A)": A5, "C": C, "A/day_sum 当日": share_today, "max5(A/day_sum)": rmax(share_today, 5),
              "p_close 平均曲线尾盘占比": P.get("p_close"), "p_open 平均曲线首根占比": P.get("p_open"),
              "C_inner 切掉首尾的DW": P.get("C_inner"), "p_cv 平均曲线CV": P.get("p_cv"),
              "dw_today 当日DW(Amt)": P.get("dw_today"), "C_swap 先DW再30日均": P.get("C_swap"),
              "cv_today 当日CV": P.get("cv_today"),
              "amt_cv30 30日日成交额CV": P.get("amt_cv30"), "amt_peak30 30日峰值/均值": P.get("amt_peak30"),
              "C_norm 先按日归一再平均的DW": P.get("C_norm"), **ctl}
    print(f"{'':34s} corr(.,G)  corr(.,C)  corr(.,max5A)")
    for n, v in others.items():
        if v is None:
            print(f"{n:34s} (面板失败)")
            continue
        print(f"{n:34s} {st.rank_corr(v, G):+.3f}     {st.rank_corr(v, C):+.3f}     {st.rank_corr(v, A5):+.3f}")
    if all(P.get(k) is not None for k in ("C_inner", "p_close", "p_open", "amt_cv30")):
        for nm, cs in (("C_inner", ("C_inner",)), ("p_close", ("p_close",)), ("amt_cv30", ("amt_cv30",)),
                       ("C_inner + p_close + p_open", ("C_inner", "p_close", "p_open")),
                       ("C_inner + p_close + p_open + amt_cv30", ("C_inner", "p_close", "p_open", "amt_cv30"))):
            _, info = dg.neutralise(C[tr], {k: P[k][tr] for k in cs})
            print(f"秩空间里 C 被 [{nm}] 张成的 R2 = {info['mean_r2']:.3f}")
    for nm, cs in (("C", {"C": C}), ("max5(A)", {"A5": A5}), ("C + max5(A)", {"C": C, "A5": A5}),
                   ("C + max5(A) + ctl_amt", {"C": C, "A5": A5, "amt": ctl["ctl_amt"]})):
        _, info = dg.neutralise(G[tr], {k: v[tr] for k, v in cs.items()})
        print(f"秩空间里 G 被 [{nm}] 张成的 R2 = {info['mean_r2']:.3f}")
    # 截面上 log C 对 log 成交额的斜率:C^3 能约掉多少成交额尺度
    sl = []
    for t in range(tr.start, tr.stop, 10):
        with np.errstate(divide="ignore", invalid="ignore"):
            x, y = np.log(dsum[t].astype(np.float64)), np.log(C[t].astype(np.float64))
        m = np.isfinite(x) & np.isfinite(y)
        if m.sum() > 200:
            sl.append(np.polyfit(x[m], y[m], 1)[0])
    print(f"截面回归 log C ~ log day_sum 的斜率: 中位 {np.median(sl):+.3f} (x3 = {3 * np.median(sl):+.3f})")
    sl = []
    for t in range(tr.start, tr.stop, 10):
        with np.errstate(divide="ignore", invalid="ignore"):
            x, y = np.log(dsum[t].astype(np.float64)), np.log(A[t].astype(np.float64))
        m = np.isfinite(x) & np.isfinite(y)
        if m.sum() > 200:
            sl.append(np.polyfit(x[m], y[m], 1)[0])
    print(f"截面回归 log A ~ log day_sum 的斜率: 中位 {np.median(sl):+.3f}")
    print(f"[x1] {time.time() - T0:.0f}s", flush=True)

    # ---------- 4/5. 各支和指数扫描的两本书 ----------
    print("\n== 4/5. 各支单独、以及 A*C^k 的指数扫描(方向/半衰期在 train 上定) ==")
    recon = rmax(A.astype(np.float64) * C.astype(np.float64) ** 3, 5)
    print(f"自检: 数值重建 max5(A*C^3) 与引擎面板 G 的 rank 相关 = {st.rank_corr(recon, G):.6f}")
    cands = {"G 原式(引擎)": G}
    for k in (0.0, 0.5, 1.0, 2.0, 3.0, 5.0, 8.0):
        cands[f"max5(A*C^{k:g})"] = rmax(A.astype(np.float64) * C.astype(np.float64) ** k, 5)
    cands["C 单独"] = C
    cands["A*C^3 不取极值"] = A.astype(np.float64) * C.astype(np.float64) ** 3
    cands["mean5(A*C^3)"] = rmean(A.astype(np.float64) * C.astype(np.float64) ** 3, 5)
    cands["max5(A/day_sum)"] = rmax(share_today, 5)
    for k in ("p_close", "C_inner", "p_cv", "C_swap", "amt_cv30", "amt_peak30", "C_norm"):
        if P.get(k) is not None:
            cands[k] = P[k]
    if P.get("C_inner") is not None:
        cands["max5(A*C_inner^3)"] = rmax(A.astype(np.float64) * P["C_inner"].astype(np.float64) ** 3, 5)
    if P.get("C_swap") is not None:
        cands["max5(A*C_swap^3)"] = rmax(A.astype(np.float64) * P["C_swap"].astype(np.float64) ** 3, 5)
    if P.get("C_norm") is not None:
        cands["max5(A*C_norm^3)"] = rmax(A.astype(np.float64) * P["C_norm"].astype(np.float64) ** 3, 5)
    cands["max5(day_sum*C^3)"] = rmax(dsum.astype(np.float64) * C.astype(np.float64) ** 3, 5)
    print(f"{'':24s} sgn hl  rIC tr  rIC va   LS tr  LS va  Lgross tr/va    Lnet tr/va     Lshp tr/va   TO    corrG")
    for n, p in cands.items():
        p = np.asarray(p, dtype=np.float64)
        sg = st.sign(p)
        b = st.books(p, fit="train", evals=("train", "valid"), sign=sg)
        s1, s2 = b["splits"]["train"], b["splits"]["valid"]
        i1, i2 = st.ic(p, "train", sign=sg), st.ic(p, "valid", sign=sg)
        print(f"{n:24s} {'+' if sg > 0 else '-'}  {b['hl_used']:>2.0f} {i1['rank_ic']:+.4f} {i2['rank_ic']:+.4f}  "
              f"{s1['ls_sharpe']:+.2f}  {s2['ls_sharpe']:+.2f}  {s1['long_gross_ann'] * 100:+5.1f}%/{s2['long_gross_ann'] * 100:+5.1f}%  "
              f"{s1['long_ann'] * 100:+5.1f}%/{s2['long_ann'] * 100:+5.1f}%  {s1['long_sharpe']:+.2f}/{s2['long_sharpe']:+.2f}  "
              f"{s1['ls_turnover'] * 100:4.1f}%  {st.rank_corr(p, G):+.3f}", flush=True)
    print(f"[x1] {time.time() - T0:.0f}s", flush=True)

    # ---------- 6. 十分位画像 ----------
    print("\n== 6. 交易信号(-G, EMA hl=2)各十分位的画像(train; Q1 = 空头端 = G 最高) ==")
    sm = bk.smoothed(-np.asarray(G, dtype=np.float64), 2)[tr]
    t_tr = tgt[tr]
    okS = np.isfinite(sm)
    r = dg.rank_rows(sm)
    n = okS.sum(1, keepdims=True)
    with np.errstate(invalid="ignore"):
        q = np.floor((r - 1.0) / np.maximum(n, 1) * 10)
    lim5 = rmax((ctl["ctl_rev1"] >= 1.095).astype(np.float64), 5)[tr]
    lim1 = (ctl["ctl_rev1"] >= 1.095).astype(np.float64)[tr]
    prof = {"成交额": pct(ctl["ctl_amt"][tr]), "市值": pct(ctl["ctl_cap"][tr]), "换手率": pct(ctl["ctl_turnrate"][tr]),
            "日内波动": pct(ctl["ctl_ivol"][tr]), "动量20": pct(ctl["ctl_mom20"][tr]), "当日收益": pct(ctl["ctl_rev1"][tr]),
            "价格": pct(ctl["ctl_price"][tr]), "max5(A)": pct(A5[tr]), "C": pct(C[tr]), "尾盘占比": pct(share_today[tr])}
    ew = np.nanmean(np.where(okS & np.isfinite(t_tr), t_tr, np.nan), axis=1, keepdims=True)
    print("Q   " + "  ".join(f"{k:>7s}" for k in prof) + "   标签缺失  当日涨停  5日内涨停  次日超额(年化)")
    for k in range(10):
        sel = (q == k)
        line = [f"Q{k + 1:<2d}"]
        for v in prof.values():
            line.append(f"{np.nanmean(np.where(sel, v, np.nan)):7.2f}")
        miss = float((sel & ~np.isfinite(t_tr)).sum() / max(sel.sum(), 1))
        l1 = float(np.nansum(np.where(sel, lim1, 0.0)) / max(sel.sum(), 1))
        l5 = float(np.nansum(np.where(sel, lim5, 0.0)) / max(sel.sum(), 1))
        ex = float(np.nanmean(np.where(sel & np.isfinite(t_tr), t_tr - ew, np.nan)) * 252)
        print("  ".join(line) + f"   {miss * 100:6.2f}%  {l1 * 100:6.2f}%  {l5 * 100:7.2f}%   {ex * 100:+7.1f}%")
    allmiss = float((okS & ~np.isfinite(t_tr)).sum() / max(okS.sum(), 1))
    print(f"全市场(有信号的格子)标签缺失率 {allmiss * 100:.2f}%")

    # ---------- 7. 乘法是门控还是两路信号 ----------
    print("\n== 7. 条件 rank IC(train; 原始方向,负 = 值越高未来越差) ==")
    for fn, f, gn, g in (("C", C, "max5(A)", A5), ("max5(A)", A5, "C", C), ("G", G, "当日尾盘占比", share_today),
                         ("C", C, "ctl_amt", ctl["ctl_amt"]), ("max5(A)", A5, "ctl_amt", ctl["ctl_amt"])):
        rows = dg.conditional_ic(np.asarray(f[tr], dtype=np.float64), tgt[tr], np.asarray(g[tr], dtype=np.float64), buckets=5)
        print(f"{fn} | {gn} 五分桶: " + "  ".join(f"Q{x['bucket'] + 1} {x['rank_ic']:+.4f}" for x in rows))
    print(f"[x1] done {time.time() - T0:.0f}s", flush=True)
