"""X2 -- after S1: the tree is (amount level) x (roughness of the 30-day average intraday Amt curve),
and the roughness branch only predicts among actively traded names.  Questions S1 cannot answer:

a. Year by year, which component carries the signal: the amount level, or the part of the roughness
   that is NOT explained by the amount level (eps_C = rank residual of C on log amount)?
b. A dependent 5x5 sort (amount quintile, then C quintile inside it): where is the long end, where
   is the short end, and is the picture the same in train and valid?
c. H9 -- is 2018H1 partly an exchange bet (Shanghai had no closing call auction before 2018-08-20)?
d. Exponent scan with the whole-day amount and no extremum memory: day_sum * C^k.
e. Which part of C matters?  Replace C by other descriptions of the same average curve, with the
   exponent chosen so that every replacement carries the SAME log-dispersion as C^3 (equal weight).
f. Is eps_C a known thing -- limit-up / MAX / volatility events of the last 30 days?
g. Does slower smoothing help the long leg in BOTH train and valid?

Only `train` / `valid` rows are ever touched.
"""
import time

import numpy as np

from partura.study_tools import Study, bk, dg

B = "cross_decay_linear(Amt, 30)"
EXPR = {
    "G": "cross_max(mul(day_close(Amt), ts_min(pow_3(day_durbin_watson(cross_decay_linear(Amt, 30))), 1)), 5)",
    "A": "day_close(Amt)",
    "C": f"day_durbin_watson({B})",
    "dsum": "day_sum(Amt)",
    "C_inner": f"day_durbin_watson(in_slice({B}, 2, 237))",
    "p_cv": f"div(day_std({B}), day_mean({B}))",
    "p_peak": f"div(day_max({B}), day_sum({B}))",
    "p_first2": f"div(day_sum(in_slice({B}, 0, 1)), day_sum({B}))",
    "p_open10": f"div(day_sum(in_slice({B}, 0, 10)), day_sum({B}))",
    "p_close": f"div(day_last({B}), day_sum({B}))",
    "C10": "day_durbin_watson(cross_decay_linear(Amt, 10))",
    "C15": "day_durbin_watson(cross_decay_linear(Amt, 15))",
    "C60": "day_durbin_watson(cross_decay_linear(Amt, 60))",
    "C_flat": "day_durbin_watson(cross_mean(Amt, 30))",
    "dw_today": "day_durbin_watson(Amt)",
}


def rroll(x, d, how):
    x = np.asarray(x, dtype=np.float64)
    if how == "max":
        out = x.copy()
        for k in range(1, d):
            sh = np.full_like(x, np.nan)
            sh[k:] = x[:-k]
            out = np.fmax(out, sh)
        return out
    s = np.zeros(x.shape)
    n = np.zeros(x.shape)
    for k in range(d):
        sh = np.full(x.shape, np.nan)
        sh[k:] = x[:x.shape[0] - k] if k else x
        ok = np.isfinite(sh)
        s += np.where(ok, sh, 0.0)
        n += ok
    if how == "sum":
        return np.where(n > 0, s, np.nan)
    return np.where(n > 0, s / np.maximum(n, 1), np.nan)


def xs_std_log(x, s):
    with np.errstate(divide="ignore", invalid="ignore"):
        lx = np.log(np.where(x[s] > 0, x[s], np.nan).astype(np.float64))
    return float(np.nanmean(np.nanstd(lx, axis=1)))


T0 = time.time()
with Study("F103_amt_dw_decay") as st:
    P = st.panels(EXPR)
    for k in EXPR:
        if k not in P:
            print(f"[x2] MISSING panel {k}")
    tr, va = st.slice("train"), st.slice("valid")
    use = slice(tr.start, va.stop)                       # train + valid only; holdout rows are never indexed
    tgt = st.target()
    dates = np.asarray(st.dates)
    years = np.asarray([d[:4] for d in dates])
    syms = np.asarray(st.symbols)
    G, A, C, dsum = (np.asarray(P[k], dtype=np.float64) for k in ("G", "A", "C", "dsum"))
    amt = st.control("ctl_amt")
    rev1 = np.asarray(st.control("ctl_rev1"), dtype=np.float64)
    ivol = np.asarray(st.control("ctl_ivol"), dtype=np.float64)

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

    HDR = f"{'':26s} s hl  rIC tr  rIC va  LS tr LS va  Lgross tr/va   Lnet tr/va     Lshp tr/va   TO   corrG"

    # ---------- a. 逐年:成交额水平 vs 成交额中性的粗糙度 ----------
    print("== a. 逐年 rank IC(原始方向:负 = 值越高未来越差) ==")
    zC = dg._zrank(C[use])
    eps_use, info = dg.neutralise(zC, {"amt": dg._zrank(np.asarray(amt[use], dtype=np.float64))},
                                  panel_ready=True, controls_ready=True)
    eps = np.full(C.shape, np.nan)
    eps[use] = eps_use
    print(f"eps_C = rank(C) 对 rank(log 成交额) 的逐日残差; 成交额张成 C 的 R2 = {info['mean_r2']:.3f}")
    series = {"G 原式": G, "day_sum(成交额水平)": dsum, "C 粗糙度": C, "eps_C 成交额中性的粗糙度": eps,
              "p_cv 平均曲线CV": P["p_cv"]}
    yy = sorted(set(years[use].tolist()))
    print(f"{'':26s} " + "  ".join(f"{y:>7s}" for y in yy))
    for n, p in series.items():
        ric = dg.rank_ic_series(np.asarray(p[use], dtype=np.float64), tgt[use])
        print(f"{n:26s} " + "  ".join(f"{np.nanmean(ric[years[use] == y]):+.4f}" for y in yy))
    # eps_C inside the top amount quintile, by year
    ra = dg.rank_rows(np.asarray(amt[use], dtype=np.float64))
    na = np.isfinite(ra).sum(1, keepdims=True)
    with np.errstate(invalid="ignore"):
        qa = np.floor((ra - 1.0) / np.maximum(na, 1) * 5)
    for lab, sel in (("C | 成交额最高 1/5", qa == 4), ("C | 成交额最低 1/5", qa == 0)):
        ric = dg.rank_ic_series(np.where(sel, C[use], np.nan), np.where(sel, tgt[use], np.nan))
        print(f"{lab:26s} " + "  ".join(f"{np.nanmean(ric[years[use] == y]):+.4f}" for y in yy))
    print(f"[x2] {time.time() - T0:.0f}s", flush=True)

    # ---------- b. 5x5 依次分组 ----------
    print("\n== b. 先按成交额五分、再在组内按 C 五分:次日超额(年化%,相对当日等权) ==")
    for sname, sl in (("train", tr), ("valid", va)):
        tot = np.zeros((5, 5))
        cnt = np.zeros((5, 5))
        for t in range(sl.start, sl.stop):
            a_, c_, y_ = amt[t].astype(np.float64), C[t], tgt[t]
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
        print(f"[{sname}]  列 = C 从平滑到粗糙;行 = 成交额从低到高")
        print("            C1      C2      C3      C4      C5   | C5-C1")
        for i in range(5):
            print(f"  amt Q{i + 1} " + " ".join(f"{mean[i, j]:+7.1f}" for j in range(5)) + f"  | {mean[i, 4] - mean[i, 0]:+7.1f}")
    print(f"[x2] {time.time() - T0:.0f}s", flush=True)

    # ---------- c. H9: 2018 上半年是不是在按交易所分组 ----------
    print("\n== c. 沪市在 2018-08-20 之前没有收盘集合竞价:C 和 G 的截面位置按交易所差多少 ==")
    is_sh = np.asarray([s.endswith("SH") for s in syms])
    pr = {"A": dg._zrank(A[use]) + 0.5, "C": dg._zrank(C[use]) + 0.5, "G": dg._zrank(G[use]) + 0.5,
          "成交额": dg._zrank(np.asarray(amt[use], dtype=np.float64)) + 0.5}
    du = dates[use]
    per = {"2018-01~2018-08-17": du <= "20180817", "2018-08-20~2018-12": (du >= "20180820") & (du <= "20181231"),
           "2019": years[use] == "2019", "2020~2021": (years[use] == "2020") | (years[use] == "2021")}
    for pn, dm in per.items():
        print(f"{pn:22s} " + "  ".join(
            f"{k}: 沪 {np.nanmean(v[np.ix_(dm, is_sh)]):.3f} / 深 {np.nanmean(v[np.ix_(dm, ~is_sh)]):.3f}" for k, v in pr.items()))
    for pn, dm in (("2018-01~2018-08-17", du <= "20180817"), ("2018-08-20~2018-12", (du >= "20180820") & (du <= "20181231"))):
        gg, tt = G[use][dm], tgt[use][dm]
        ric_all = np.nanmean(dg.rank_ic_series(gg, tt))
        ric_sh = np.nanmean(dg.rank_ic_series(np.where(is_sh[None, :], gg, np.nan), np.where(is_sh[None, :], tt, np.nan)))
        ric_sz = np.nanmean(dg.rank_ic_series(np.where(~is_sh[None, :], gg, np.nan), np.where(~is_sh[None, :], tt, np.nan)))
        print(f"{pn:22s} G 的 rank IC: 全市场 {ric_all:+.4f}  只在沪市内 {ric_sh:+.4f}  只在深市内 {ric_sz:+.4f}")
    print(f"[x2] {time.time() - T0:.0f}s", flush=True)

    # ---------- f. eps_C 是不是近 30 日的涨停 / MAX / 波动事件 ----------
    print("\n== f. eps_C(成交额中性的粗糙度)与近 30 日事件变量的 rank 相关(train) ==")
    lim = (rev1 >= 1.095).astype(np.float64)
    lim[~np.isfinite(rev1)] = np.nan
    ev = {"30日涨停次数": rroll(lim, 30, "sum"), "30日最大日收益(MAX)": rroll(rev1, 30, "max"),
          "30日日内波动均值": rroll(ivol, 30, "mean"), "30日日成交额峰值/均值": rroll(dsum, 30, "max") / rroll(dsum, 30, "mean"),
          "p_cv": P["p_cv"], "p_peak 峰值分钟占比": P["p_peak"], "p_first2 头两根占比": P["p_first2"],
          "p_open10 开盘10分钟占比": P["p_open10"], "p_close 收盘竞价占比": P["p_close"], "C_inner": P["C_inner"],
          "ctl_mom20": st.control("ctl_mom20"), "ctl_dvol20": st.control("ctl_dvol20"), "ctl_turnrate": st.control("ctl_turnrate")}
    for n, v in ev.items():
        print(f"{n:26s} corr(.,eps_C) {st.rank_corr(v, eps):+.3f}   corr(.,C) {st.rank_corr(v, C):+.3f}   corr(.,G) {st.rank_corr(v, G):+.3f}")
    zc = {k: dg._zrank(np.asarray(v[tr], dtype=np.float64)) for k, v in ev.items()}
    ze = dg._zrank(eps[tr])
    for nm, ks in (("涨停次数 + MAX + 日内波动 + 日成交额峰均比", ["30日涨停次数", "30日最大日收益(MAX)", "30日日内波动均值", "30日日成交额峰值/均值"]),
                   ("p_first2 + p_close + C_inner", ["p_first2 头两根占比", "p_close 收盘竞价占比", "C_inner"]),
                   ("p_cv", ["p_cv"])):
        _, inf = dg.neutralise(ze, {k: zc[k] for k in ks}, panel_ready=True, controls_ready=True)
        print(f"秩空间里 eps_C 被 [{nm}] 张成的 R2 = {inf['mean_r2']:.3f}")
    print(f"[x2] {time.time() - T0:.0f}s", flush=True)

    # ---------- d. 指数扫描:全天成交额、不取极值 ----------
    print("\n== d. day_sum * C^k(不取极值;方向/半衰期在 train 上定;'hlL' = 按纯多头夏普选的半衰期下的多头腿) ==")
    print(HDR)
    row("G 原式", G)
    for k in (0.0, 0.5, 1.0, 1.5, 2.0, 3.0):
        row(f"day_sum*C^{k:g}", dsum * C ** k)
    row("eps_C 单独", eps)
    print(f"[x2] {time.time() - T0:.0f}s", flush=True)

    # ---------- g. 慢记忆 ----------
    print("\n== g. 给 day_sum*C^k 套 20 日均值(慢记忆) ==")
    print(HDR)
    for k in (0.0, 1.0, 2.0, 3.0):
        row(f"mean20(day_sum*C^{k:g})", rroll(dsum * C ** k, 20, "mean"))
    row("mean20(day_sum)*C^2", rroll(dsum, 20, "mean") * C ** 2)
    print(f"[x2] {time.time() - T0:.0f}s", flush=True)

    # ---------- e. C 里到底哪一部分有用:同等权重的替换 ----------
    print("\n== e. 把 C 换成同一条平均曲线的别的描述:day_sum * X^kX,kX 使 kX*log X 的截面离散度 = 3*log C 的 ==")
    target_disp = 3 * xs_std_log(C, tr)
    print(f"3*std(log C) = {target_disp:.3f}")
    print(HDR)
    for n in ("C", "C_inner", "p_cv", "p_peak", "p_first2", "p_open10", "p_close", "C10", "C15", "C60", "C_flat", "dw_today"):
        X = np.asarray(P[n], dtype=np.float64)
        sd = xs_std_log(X, tr)
        kx = target_disp / sd
        with np.errstate(invalid="ignore", divide="ignore"):
            row(f"day_sum*{n}^{kx:.2f}", dsum * np.where(X > 0, X, np.nan) ** kx,
                extra=f"  corr(X,C) {st.rank_corr(X, C):+.3f}")
    print(f"[x2] done {time.time() - T0:.0f}s", flush=True)
