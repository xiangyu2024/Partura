"""audit_1 -- 审查员的反驳实验。只读 train / valid(utrain = 两者之和);留出段的行从不被索引。

要检验的两件事(都是报告里"已确立"或推荐理由的一部分):

A. "删节点 / 提纯让多头腿更好"是不是只是半衰期 2 -> 10?
   各变体的半衰期是各自按多空夏普拟合的(原式选中 2,提纯版选中 10/20)。在**同一个半衰期**下
   比较原式、纯删节点(k=3)、推荐者(k=2)、k=1、纯成交额的两本书(train / valid / utrain)。
B. 推荐者相对原式 / 纯成交额的日度配对差(多空净收益、多头腿净超额)有没有统计意义。
C. "成交最活跃 x 曲线最集中的 4% 是这棵树最稳的发现":这个角落是不是 C 特有的?
   在成交额最高 1/5 里,把第二排序换成已知的"热门股"代理(换手率、20 日波动、日内波动、动量、MAX、小市值、低价、
   成交额本身),看角落是不是一样深;C 对这些已知暴露做组内残差之后角落还剩多少;剔掉近 5/30 日涨停过的票之后还剩多少;逐年。
D. 多头十分位里标签缺失(停牌 / 开盘封板买不进,记 0 收益)的权重占比。
0. 顺带把 src 打不出来的内部函数源码印出来(核对 NaN / 边界语义)。
"""
import inspect
import time

import numpy as np

from partura.study_tools import Study, bk

EXPR = {
    "G": "cross_max(mul(day_close(Amt), ts_min(pow_3(day_durbin_watson(cross_decay_linear(Amt, 30))), 1)), 5)",
    "A": "day_close(Amt)",
    "C": "day_durbin_watson(cross_decay_linear(Amt, 30))",
    "dsum": "day_sum(Amt)",
}


def dump_sources():
    print("== 0. 内部函数源码(服务器上的 AlphaCube) ==")
    try:
        import alphacube.metrics as mm
        import alphacube.operators.common as mc
        import alphacube.operators.dt_cross as mx
        import alphacube.operators.dt_day as md
    except Exception as exc:                                   # noqa: BLE001
        print(f"[audit] import failed: {exc}")
        return
    todo = [(mx, "rolling_reduce"), (mx, "decay_linear_last"), (mx, "nanmax_last"), (md, "last_valid_last"),
            (mc, "pow_"), (mm, "ema_rows"), (mm, "long_short_weights")]
    try:
        todo.append((getattr(md, "C"), "_sum"))
    except Exception:                                          # noqa: BLE001
        pass
    for mod, name in todo:
        try:
            fn = inspect.unwrap(getattr(mod, name))
            src = inspect.getsource(fn).splitlines()
            print(f"--- {getattr(mod, '__name__', mod)}.{name}  ({len(src)} lines)")
            print("\n".join(src[:70]))
        except Exception as exc:                               # noqa: BLE001
            print(f"--- {name}: unavailable ({type(exc).__name__}: {exc})")


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
    return np.where(n > 0, s, np.nan)


def qcut(v, k=5):
    r = np.argsort(np.argsort(v, kind="stable"), kind="stable")
    return np.floor(r / v.size * k).astype(int)


def zr(v):
    _, inv, cnt = np.unique(v, return_inverse=True, return_counts=True)
    start = np.cumsum(cnt) - cnt
    r = (start + (cnt - 1) / 2.0)[inv]                          # 0-based average rank, ties share a rank
    return r / max(v.size - 1, 1) - 0.5


def tstat(d):
    f = d[np.isfinite(d)]
    return (float(f.mean() * 252 * 100), float(f.mean() / f.std() * np.sqrt(f.size))) if f.size > 5 and f.std() > 0 else (np.nan, np.nan)


T0 = time.time()
dump_sources()
with Study("F103_amt_dw_decay") as st:
    P = {k: np.asarray(v, dtype=np.float64) for k, v in st.panels(EXPR).items()}
    tr, va, ut = st.slice("train"), st.slice("valid"), st.slice("utrain")
    cut = va.stop                                              # nothing at or after this row is ever touched
    assert ut.stop <= cut and tr.stop <= cut
    tgt = np.asarray(st.target(), dtype=np.float64)[:cut]
    cost, top = float(st.cfg.get("cost_per_side", bk.COST)), float(st.cfg.get("top_frac", bk.TOP_FRAC))
    dates = np.asarray(st.dates)[:cut]
    years = np.asarray([d[:4] for d in dates])
    G, A, C, dsum = (P[k][:cut] for k in ("G", "A", "C", "dsum"))
    ctl = {n: np.asarray(st.control(n), dtype=np.float64)[:cut] for n in
           ("ctl_amt", "ctl_cap", "ctl_turnrate", "ctl_ivol", "ctl_dvol20", "ctl_mom20", "ctl_price", "ctl_rev1")}
    SPL = (("train", tr), ("valid", va), ("utrain", ut))
    print(f"[audit] panels ready {time.time() - T0:.0f}s; rows used 0..{cut} ({dates[tr][0]}..{dates[va][-1]}); "
          f"sign(train): G {st.sign(P['G']):+.0f}  dsum*C^2 {st.sign(P['dsum'] * P['C'] ** 2):+.0f}", flush=True)

    V = {"orig G": G, "A*C^3 (no max)": A * C ** 3, "dsum*C^3": dsum * C ** 3, "dsum*C^2 (REC)": dsum * C ** 2,
         "dsum*C^1": dsum * C, "dsum (amt only)": dsum}

    # ------------------------------------------------------------------ A
    print("\n== A. 固定半衰期下的两本书(方向一律 -1;每格 = 扣费多空夏普 | 多头腿净超额 | 纯多头夏普 | 多空日换手) ==")
    SM = {}
    KEEP = {("dsum*C^2 (REC)", 10), ("orig G", 2), ("orig G", 10), ("dsum*C^3", 10), ("dsum (amt only)", 10), ("dsum*C^1", 10)}
    for name, p in V.items():
        sig = -p
        fit_tr = bk.fit_halflives(sig, tgt, tr, cost, top)
        fit_ut = bk.fit_halflives(sig, tgt, ut, cost, top)
        print(f"\n{name}:  按多空夏普选的半衰期 train {fit_tr['hl_ls']:.0f} / utrain {fit_ut['hl_ls']:.0f};"
              f"  按纯多头夏普选 train {fit_tr['hl_long']:.0f} / utrain {fit_ut['hl_long']:.0f}")
        print("   utrain 上各半衰期的多空夏普: " + "  ".join(f"hl{s['halflife']:.0f} {s['ls_sharpe']:+.2f}" for s in fit_ut["sweep"]))
        for hl in (2, 5, 10, 20):
            sm = bk.smoothed(sig, hl)
            if (name, hl) in KEEP:
                SM[(name, hl)] = sm
            cells = []
            for sn, sl in SPL:
                r = bk.book_row(sm, tgt, sl, cost, top)
                cells.append(f"{sn} {r['ls_sharpe']:+.2f} | {r['long_ann'] * 100:+5.1f}% | {r['long_sharpe']:+.2f} | {r['ls_turnover'] * 100:4.1f}%")
            print(f"   hl{hl:<2d}  " + "    ".join(cells), flush=True)
    print(f"[audit] A done {time.time() - T0:.0f}s", flush=True)

    # ------------------------------------------------------------------ B
    print("\n== B. 日度配对差(a - b):年化均值差(%) 与 t 值;LS = 多空净收益,L = 多头腿净超额 ==")

    DAILY = {}

    def daily(key, sl):
        ck = (key, sl.start, sl.stop)
        if ck not in DAILY:
            DAILY[ck] = _daily(key, sl)
        return DAILY[ck]

    def _daily(key, sl):
        sm, t = SM[key][sl], tgt[sl]
        w = bk.long_short_weights(sm, top)
        ls_net, _, _ = bk.portfolio_returns(w, t, cost)
        net, _, _ = bk.long_book(w, sm, t, cost)
        return np.asarray(ls_net, dtype=np.float64), np.asarray(net, dtype=np.float64)

    pairs = [(("dsum*C^2 (REC)", 10), ("orig G", 2), "REC@10 - 原式@2(报告里的对比)"),
             (("dsum*C^2 (REC)", 10), ("orig G", 10), "REC@10 - 原式@10(同半衰期)"),
             (("dsum*C^3", 10), ("orig G", 10), "纯删节点 k3@10 - 原式@10(同半衰期)"),
             (("orig G", 10), ("orig G", 2), "原式@10 - 原式@2(只改半衰期)"),
             (("dsum*C^2 (REC)", 10), ("dsum*C^3", 10), "REC@10 - k3@10(只改指数)"),
             (("dsum*C^2 (REC)", 10), ("dsum (amt only)", 10), "REC@10 - 纯成交额@10(C^2 加了什么)"),
             (("dsum*C^2 (REC)", 10), ("dsum*C^1", 10), "REC@10 - k1@10")]
    for a, b, lab in pairs:
        out = []
        for sn, sl in SPL:
            la, na = daily(a, sl)
            lb, nb = daily(b, sl)
            (m1, t1), (m2, t2) = tstat(la - lb), tstat(na - nb)
            out.append(f"{sn}: LS {m1:+5.1f}% (t {t1:+.1f})  L {m2:+5.1f}% (t {t2:+.1f})")
        print(f"{lab:38s} " + "   ".join(out), flush=True)
    print(f"[audit] B done {time.time() - T0:.0f}s", flush=True)

    # ------------------------------------------------------------------ E
    print("\n== E. C 给已知家族加的东西是 alpha 还是'减掉一部分成交额水平暴露'?  d = 加了 C 的多空净收益 - 没加的;"
          "回归 d = a + b * (纯成交额水平的多空净收益) ==")
    std9 = np.asarray(st.control("known_stdamt_max9"), dtype=np.float64)[:cut]
    SM[("std9", 0)] = -std9
    SM[("std9*C", 2)] = bk.smoothed(-(std9 * C), 2)
    SM[("dsum (amt only)", 5)] = bk.smoothed(-dsum, 5)
    for a, b, f_, lab in ((("std9*C", 2), ("std9", 0), ("dsum (amt only)", 5), "F001蒸馏*C@2 - F001蒸馏@0"),
                          (("dsum*C^2 (REC)", 10), ("dsum (amt only)", 10), ("dsum (amt only)", 10), "REC@10 - 纯成交额@10")):
        for sn, sl in SPL:
            d = daily(a, sl)[0] - daily(b, sl)[0]
            x = daily(f_, sl)[0]
            ok = np.isfinite(d) & np.isfinite(x)
            d_, x_ = d[ok], x[ok]
            beta = float(np.cov(d_, x_)[0, 1] / x_.var(ddof=1))
            alpha = d_ - beta * x_
            print(f"{lab:28s} {sn:6s}: d 年化 {d_.mean() * 25200:+5.1f}% (t {d_.mean() / d_.std() * np.sqrt(d_.size):+.1f})   "
                  f"b {beta:+.2f}  corr {np.corrcoef(d_, x_)[0, 1]:+.2f}   a 年化 {alpha.mean() * 25200:+5.1f}% "
                  f"(t {alpha.mean() / alpha.std() * np.sqrt(alpha.size):+.1f})   "
                  f"夏普: 没加 {daily(b, sl)[0][ok].mean() / daily(b, sl)[0][ok].std() * np.sqrt(252):+.2f} -> 加了 "
                  f"{daily(a, sl)[0][ok].mean() / daily(a, sl)[0][ok].std() * np.sqrt(252):+.2f}", flush=True)
        yrs = sorted(set(years[ut].tolist()))
        da, db = daily(a, ut)[0] - daily(b, ut)[0], years[ut]
        print(f"{'':28s} 逐年 d 年化(utrain 连续建书): " + "  ".join(f"{y} {np.nanmean(da[db == y]) * 25200:+5.1f}%" for y in yrs))
    print(f"[audit] E done {time.time() - T0:.0f}s", flush=True)

    # ------------------------------------------------------------------ D
    print("\n== D. 多头十分位里标签缺失(记 0 收益)的权重占比 ==")
    for key in (("dsum*C^2 (REC)", 10), ("orig G", 2), ("dsum (amt only)", 10)):
        out = []
        for sn, sl in SPL[:2]:
            w = bk.long_short_weights(SM[key][sl], top)
            wl = np.clip(w, 0.0, None) * 2.0
            miss = (wl * ~np.isfinite(tgt[sl])).sum(1)
            allmiss = (~np.isfinite(tgt[sl]) & np.isfinite(SM[key][sl])).sum(1) / np.maximum(np.isfinite(SM[key][sl]).sum(1), 1)
            out.append(f"{sn}: 多头 {np.nanmean(miss) * 100:.2f}%  全市场(有信号的票) {np.nanmean(allmiss) * 100:.2f}%")
        print(f"{key[0]}@hl{key[1]:<3d} " + "   ".join(out), flush=True)

    # ------------------------------------------------------------------ C
    print("\n== C. 成交额最高 1/5 里的角落:是不是 C 特有的 ==")
    amt, cap, turn = ctl["ctl_amt"], ctl["ctl_cap"], ctl["ctl_turnrate"]
    rev1 = ctl["ctl_rev1"]
    lim = (rev1 >= 1.095).astype(np.float64)
    lim[~np.isfinite(rev1)] = np.nan
    lim5, lim30, max30 = rroll(lim, 5, "sum"), rroll(lim, 30, "sum"), rroll(rev1, 30, "max")
    sorts = {"C(集中度)": C, "成交额(组内再取最高)": amt, "换手率": turn, "20日波动": ctl["ctl_dvol20"], "日内波动": ctl["ctl_ivol"],
             "20日动量": ctl["ctl_mom20"], "30日MAX": max30, "小市值": -cap, "低价": -ctl["ctl_price"]}
    csets = {"换手率+市值": ["turn", "cap"],
             "全部已知": ["turn", "cap", "dvol20", "ivol", "mom20", "price", "max30", "lim30", "amt"]}
    cpan = {"turn": turn, "cap": cap, "dvol20": ctl["ctl_dvol20"], "ivol": ctl["ctl_ivol"], "mom20": ctl["ctl_mom20"],
            "price": ctl["ctl_price"], "max30": max30, "lim30": np.where(np.isfinite(lim30), lim30, np.nan), "amt": amt}
    rec = {}                                                     # key -> per-day array

    def put(k, t, v):
        if k not in rec:
            rec[k] = np.full(cut, np.nan)
        rec[k][t] = v

    for t in range(tr.start, cut):
        a_, c_, y_ = amt[t], C[t], tgt[t]
        m = np.isfinite(a_) & np.isfinite(c_) & np.isfinite(y_)
        if m.sum() < 500:
            continue
        idx = np.nonzero(m)[0]
        ex = y_[idx] - y_[idx].mean()
        qa = qcut(a_[idx])
        topi, ext = idx[qa == 4], ex[qa == 4]
        put("row", t, ext.mean())
        for nm, X in sorts.items():
            x = X[t][topi]
            f = np.isfinite(x)
            if f.sum() < 100:
                continue
            q = qcut(x[f])
            put(f"s5|{nm}", t, ext[f][q == 4].mean())
            put(f"s1|{nm}", t, ext[f][q == 0].mean())
        qC = qcut(c_[topi])
        corner = qC == 4
        l5, l30 = lim5[t][topi], lim30[t][topi]
        put("share5_corner", t, float((l5[corner] > 0).mean()))
        put("share30_corner", t, float((l30[corner] > 0).mean()))
        put("share5_row", t, float((l5 > 0).mean()))
        put("share30_row", t, float((l30 > 0).mean()))
        for lab, sel in (("corner_nolim5", corner & ~(l5 > 0)), ("corner_lim5", corner & (l5 > 0)),
                         ("corner_nolim30", corner & ~(l30 > 0)), ("corner_lim30", corner & (l30 > 0)),
                         ("rest_lim5", ~corner & (l5 > 0)), ("rest_nolim5", ~corner & ~(l5 > 0)),
                         ("rest_lim30", ~corner & (l30 > 0)), ("rest_nolim30", ~corner & ~(l30 > 0))):
            if sel.sum() >= 5:
                put(lab, t, ext[sel].mean())
        for sn_, names in csets.items():
            cols = [cpan[n][t][topi] for n in names]
            f = np.isfinite(c_[topi])
            for x in cols:
                f &= np.isfinite(x)
            if f.sum() < 100:
                continue
            yv = zr(c_[topi][f])
            Z = np.column_stack([np.ones(int(f.sum()))] + [zr(x[f]) for x in cols])
            beta, *_ = np.linalg.lstsq(Z, yv, rcond=None)
            res = yv - Z @ beta
            e = ext[f]
            put(f"r2|{sn_}", t, 1.0 - float((res ** 2).sum()) / float(((yv - yv.mean()) ** 2).sum()))
            q, q0 = qcut(res), qcut(yv)
            put(f"res5|{sn_}", t, e[q == 4].mean())
            put(f"res1|{sn_}", t, e[q == 0].mean())
            put(f"raw5|{sn_}", t, e[q0 == 4].mean())
            put(f"raw1|{sn_}", t, e[q0 == 0].mean())
            re_ = zr(e)
            put(f"icres|{sn_}", t, float(np.corrcoef(zr(res), re_)[0, 1]))
            put(f"icraw|{sn_}", t, float(np.corrcoef(yv, re_)[0, 1]))
            # the mirror question: do the known exposures predict inside the row once C is taken out?
            fit = Z @ beta
            put(f"icfit|{sn_}", t, float(np.corrcoef(zr(fit), re_)[0, 1]))
            qf = qcut(fit)
            put(f"fit5|{sn_}", t, e[qf == 4].mean())
    print(f"[audit] C loop done {time.time() - T0:.0f}s", flush=True)

    yy = sorted(set(years[tr.start:cut].tolist()))
    PER = [("train", np.arange(cut)[tr]), ("valid", np.arange(cut)[va])] + [(y, np.nonzero(years == y)[0]) for y in yy]

    def ann(k, rows):
        return float(np.nanmean(rec[k][rows]) * 252 * 100) if k in rec else np.nan

    def avg(k, rows):
        return float(np.nanmean(rec[k][rows])) if k in rec else np.nan

    hdr = "".join(f"{n:>9s}" for n, _ in PER)
    print("\nC1. 成交额最高 1/5 内,按不同变量再五分:最高一组(那 4%)的次日超额(年化 %);括号行 = 最高组 - 最低组")
    print(f"{'':26s}{hdr}")
    print(f"{'整行(成交额最高 1/5)平均':26s}" + "".join(f"{ann('row', r):+9.1f}" for _, r in PER))
    for nm in sorts:
        print(f"{nm:26s}" + "".join(f"{ann('s5|' + nm, r):+9.1f}" for _, r in PER))
        print(f"{'   (5 - 1)':26s}" + "".join(f"{ann('s5|' + nm, r) - ann('s1|' + nm, r):+9.1f}" for _, r in PER))

    print("\nC2. C 角落(成交额最高 1/5 x C 最高 1/5)按近期是否涨停过(日收益 >= 9.5%)拆开:次日超额(年化 %)与占比")
    print(f"{'':26s}{hdr}")
    for lab, k in (("角落里近5日涨停过的占比", "share5_corner"), ("整行里近5日涨停过的占比", "share5_row"),
                   ("角落里近30日涨停过的占比", "share30_corner"), ("整行里近30日涨停过的占比", "share30_row")):
        print(f"{lab:26s}" + "".join(f"{avg(k, r) * 100:8.1f}%" for _, r in PER))
    for lab, k in (("角落 且 近5日涨停过", "corner_lim5"), ("角落 且 近5日没涨停", "corner_nolim5"),
                   ("非角落 且 近5日涨停过", "rest_lim5"), ("非角落 且 近5日没涨停", "rest_nolim5"),
                   ("角落 且 近30日涨停过", "corner_lim30"), ("角落 且 近30日没涨停", "corner_nolim30"),
                   ("非角落 且 近30日涨停过", "rest_lim30"), ("非角落 且 近30日没涨停", "rest_nolim30")):
        print(f"{lab:26s}" + "".join(f"{ann(k, r):+9.1f}" for _, r in PER))

    print("\nC3. 成交额最高 1/5 内,C 对已知暴露做组内秩回归:残差的最高组 / (5-1) / 组内 rank IC,对照同一批票上的原始 C")
    print(f"{'':26s}{hdr}")
    for sn_ in csets:
        print(f"-- 控制变量: {sn_}  (组内 R2 train {avg('r2|' + sn_, PER[0][1]):.3f} / valid {avg('r2|' + sn_, PER[1][1]):.3f})")
        print(f"{'原始 C 最高组':26s}" + "".join(f"{ann('raw5|' + sn_, r):+9.1f}" for _, r in PER))
        print(f"{'残差 C 最高组':26s}" + "".join(f"{ann('res5|' + sn_, r):+9.1f}" for _, r in PER))
        print(f"{'已知暴露拟合值 最高组':26s}" + "".join(f"{ann('fit5|' + sn_, r):+9.1f}" for _, r in PER))
        print(f"{'原始 C (5-1)':26s}" + "".join(f"{ann('raw5|' + sn_, r) - ann('raw1|' + sn_, r):+9.1f}" for _, r in PER))
        print(f"{'残差 C (5-1)':26s}" + "".join(f"{ann('res5|' + sn_, r) - ann('res1|' + sn_, r):+9.1f}" for _, r in PER))
        print(f"{'原始 C 组内 rank IC':26s}" + "".join(f"{avg('icraw|' + sn_, r):+9.4f}" for _, r in PER))
        print(f"{'残差 C 组内 rank IC':26s}" + "".join(f"{avg('icres|' + sn_, r):+9.4f}" for _, r in PER))
        print(f"{'拟合值 组内 rank IC':26s}" + "".join(f"{avg('icfit|' + sn_, r):+9.4f}" for _, r in PER))
    print(f"[audit] done {time.time() - T0:.0f}s", flush=True)
