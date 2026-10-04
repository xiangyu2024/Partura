"""rev1 -- 修订阶段的补充分析。只读 train / valid(utrain = 两者之和);留出段的行从不被索引。

审查指出原报告有三处归因没有在同一口径下比:(1) 各变体的半衰期各自拟合,多头腿的差别混着半衰期;
(2) 推荐者的多头腿没有和"已知家族自己、同半衰期"比;(3) "活跃 x 集中"的角落没有和已知的热门股代理比增量。
审查员的 audit_1.py 已经对 day_sum 那条链(原式 / k3 / k2 / k1 / 纯成交额)做了 (1)(2),对角落做了替换与残差。
这里补它没覆盖的三件事,全部只用 train / valid:

A. 事前登记的首选 f_std9_k1 = stdamt9 * C 和它的已知家族基准 stdamt9 = cross_max(day_std(Amt), 9)
   在**同一个半衰期**下的两本书(连同原式、k3、k2、k1、纯成交额,同一段代码出同一张表)。
B. 日度配对差(多空净收益、多头腿净超额;年化均值差与 t 值;逐年):
   C 给已知家族加了什么(stdamt9*C@h - stdamt9@h),事前首选相对原式 / 纯成交额 / k2 的差。
C. 配对差对"纯成交额水平的收益"回归:加 C 之后的增量是 alpha 还是减掉了一部分成交额水平暴露(多空、多头腿各一次),
   以及均值 / 波动各贡献多少夏普。
D. 剔除名单的增量:在全市场等权组合里,先剔掉已知的两类(成交额最高 1/5 里换手率最高 1/5;近 5 日有过 >= 9.5% 涨幅的票),
   再剔"成交额最高 1/5 x C 最高 1/5",还能多拿多少;C 角落里既不属于换手率角落、近 5 日也没涨停过的那部分票自己的次日超额。

自检:A 的 orig@2 / stdamt9*C@2 / stdamt9@0 必须复现 S2 / S_final 的引擎数字(train / valid 多空夏普)。
"""
import time

import numpy as np

from partura.study_tools import Study, bk

EXPR = {
    "G": "cross_max(mul(day_close(Amt), ts_min(pow_3(day_durbin_watson(cross_decay_linear(Amt, 30))), 1)), 5)",
    "C": "day_durbin_watson(cross_decay_linear(Amt, 30))",
    "dsum": "day_sum(Amt)",
}
# 引擎(S2 / S_final 的 JSON)里的数字:(train 多空夏普, valid 多空夏普, train 多头腿净超额)
EXPECT = {("orig", 2): (4.140, 2.216, 0.0631), ("std9*C", 2): (3.315, 4.361, 0.1150), ("std9", 0): (2.472, 4.437, 0.0926),
          ("dsum*C^2", 10): (3.326, 3.781, 0.1138)}
HLS = (0, 2, 5, 10, 20)


def tstat(d):
    f = d[np.isfinite(d)]
    if f.size < 6 or f.std() == 0:
        return np.nan, np.nan
    return float(f.mean() * 252 * 100), float(f.mean() / f.std() * np.sqrt(f.size))


def qcut(v, k=5):
    r = np.argsort(np.argsort(v, kind="stable"), kind="stable")
    return np.floor(r / v.size * k).astype(int)


def rsum(x, d):
    s = np.zeros(x.shape)
    n = np.zeros(x.shape)
    for k in range(d):
        sh = np.full(x.shape, np.nan)
        sh[k:] = x[:x.shape[0] - k] if k else x
        ok = np.isfinite(sh)
        s += np.where(ok, sh, 0.0)
        n += ok
    return np.where(n > 0, s, np.nan)


T0 = time.time()
with Study("F103_amt_dw_decay") as st:
    P = {k: np.asarray(v, dtype=np.float64) for k, v in st.panels(EXPR).items()}
    tr, va, ut = st.slice("train"), st.slice("valid"), st.slice("utrain")
    cut = va.stop                                              # 这一行及之后的任何行都不会被碰到
    assert ut.stop <= cut and tr.stop <= cut
    tgt = np.asarray(st.target(), dtype=np.float64)[:cut]
    cost, top = float(st.cfg.get("cost_per_side", bk.COST)), float(st.cfg.get("top_frac", bk.TOP_FRAC))
    dates = np.asarray(st.dates)[:cut]
    years = np.asarray([d[:4] for d in dates])
    G, C, dsum = (P[k][:cut] for k in ("G", "C", "dsum"))
    std9_full = np.asarray(st.control("known_stdamt_max9"), dtype=np.float64)
    std9 = std9_full[:cut]
    SPL = (("train", tr), ("valid", va), ("utrain", ut))
    SD = dict(SPL)
    V = {"orig": G, "dsum*C^3": dsum * C ** 3, "dsum*C^2": dsum * C ** 2, "dsum*C^1": dsum * C, "dsum": dsum,
         "std9*C": std9 * C, "std9": std9}
    print(f"[rev1] panels ready {time.time() - T0:.0f}s; rows 0..{cut} ({dates[tr][0]}..{dates[va][-1]}); "
          f"sign(train): " + "  ".join(f"{k} {st.sign(v):+.0f}" for k, v in V.items()), flush=True)

    # ------------------------------------------------------------------ A
    print("\n== A. 固定半衰期下的两本书(方向一律 -1)。每格 = 扣费多空夏普 | 多空净年化 | 多头腿毛超额 | 多头腿净超额 | 纯多头夏普 | 多头腿最大回撤 | 多空日换手 ==")
    SM, ROW = {}, {}
    for name, p in V.items():
        sig = -p
        fit_tr = bk.fit_halflives(sig, tgt, tr, cost, top)
        fit_ut = bk.fit_halflives(sig, tgt, ut, cost, top)
        print(f"\n{name}:  按多空夏普选的半衰期 train {fit_tr['hl_ls']:.0f} / utrain {fit_ut['hl_ls']:.0f};"
              f"  按纯多头夏普选 train {fit_tr['hl_long']:.0f} / utrain {fit_ut['hl_long']:.0f}")
        print("   utrain 各半衰期 多空夏普: " + "  ".join(f"hl{s['halflife']:.0f} {s['ls_sharpe']:+.2f}" for s in fit_ut["sweep"]))
        print("   utrain 各半衰期 多头腿净超额: " + "  ".join(f"hl{s['halflife']:.0f} {s['long_ann'] * 100:+.1f}%" for s in fit_ut["sweep"]))
        print("   utrain 各半衰期 纯多头夏普: " + "  ".join(f"hl{s['halflife']:.0f} {s['long_sharpe']:+.2f}" for s in fit_ut["sweep"]))
        for hl in HLS:
            sm = bk.smoothed(sig, hl)
            SM[(name, hl)] = sm
            cells = []
            for sn, sl in SPL:
                r = bk.book_row(sm, tgt, sl, cost, top)
                ROW[(name, hl, sn)] = r
                cells.append(f"{sn} {r['ls_sharpe']:+.2f} | {r['ls_ann'] * 100:+5.1f}% | {r['long_gross_ann'] * 100:+5.1f}% | "
                             f"{r['long_ann'] * 100:+5.1f}% | {r['long_sharpe']:+.2f} | {r['long_mdd'] * 100:+5.1f}% | {r['ls_turnover'] * 100:4.1f}%")
            print(f"   hl{hl:<2d}  " + "    ".join(cells), flush=True)
    print("\n自检(引擎 JSON 里的数字 -> 这里的数值重建):")
    for (name, hl), (e_tr, e_va, e_l) in EXPECT.items():
        a, b, c = ROW[(name, hl, "train")]["ls_sharpe"], ROW[(name, hl, "valid")]["ls_sharpe"], ROW[(name, hl, "train")]["long_ann"]
        ok = abs(a - e_tr) < 0.01 and abs(b - e_va) < 0.01 and abs(c - e_l) < 0.001
        print(f"   {name}@hl{hl}: train {e_tr:+.3f} -> {a:+.3f}   valid {e_va:+.3f} -> {b:+.3f}   train 多头腿净 {e_l * 100:+.2f}% -> {c * 100:+.2f}%   "
              f"{'OK' if ok else 'MISMATCH'}")
    print(f"[rev1] A done {time.time() - T0:.0f}s", flush=True)

    # ------------------------------------------------------------------ B
    print("\n== B. 日度配对差(a - b):年化均值差(%) 与 t 值;LS = 多空净收益,L = 多头腿净超额;逐年是 utrain 连续建书 ==")
    DAILY = {}

    def daily(key, sn):
        ck = (key, sn)
        if ck not in DAILY:
            sl = SD[sn]
            sm, t = SM[key][sl], tgt[sl]
            w = bk.long_short_weights(sm, top)
            ls_net, _, _ = bk.portfolio_returns(w, t, cost)
            net, _, _ = bk.long_book(w, sm, t, cost)
            DAILY[ck] = (np.asarray(ls_net, dtype=np.float64), np.asarray(net, dtype=np.float64))
        return DAILY[ck]

    yrs = sorted(set(years[ut].tolist()))
    pairs = [(("orig", 10), ("orig", 2), "原式@10 - 原式@2(只改半衰期)"),
             (("dsum*C^3", 10), ("orig", 10), "k3@10 - 原式@10(只删节点)"),
             (("dsum*C^2", 10), ("dsum*C^3", 10), "k2@10 - k3@10(只改指数)"),
             (("dsum*C^2", 10), ("dsum", 10), "k2@10 - 纯成交额@10"),
             (("std9*C", 2), ("orig", 2), "事前首选@2 - 原式@2(官方半衰期,都是 2)"),
             (("std9*C", 10), ("orig", 10), "事前首选@10 - 原式@10"),
             (("std9*C", 0), ("std9", 0), "stdamt9*C@0 - stdamt9@0(C 给已知家族加了什么)"),
             (("std9*C", 2), ("std9", 2), "stdamt9*C@2 - stdamt9@2"),
             (("std9*C", 5), ("std9", 5), "stdamt9*C@5 - stdamt9@5"),
             (("std9*C", 10), ("std9", 10), "stdamt9*C@10 - stdamt9@10"),
             (("std9*C", 2), ("std9", 0), "stdamt9*C@2 - stdamt9@0(报告里的对比)"),
             (("std9*C", 10), ("dsum", 10), "事前首选@10 - 纯成交额@10"),
             (("std9*C", 10), ("dsum*C^1", 10), "事前首选@10 - k1@10"),
             (("std9*C", 10), ("dsum*C^2", 10), "事前首选@10 - k2@10"),
             (("std9", 10), ("dsum", 10), "stdamt9@10 - 纯成交额@10")]
    for a, b, lab in pairs:
        out = []
        for sn, _ in SPL:
            la, na = daily(a, sn)
            lb, nb = daily(b, sn)
            (m1, t1), (m2, t2) = tstat(la - lb), tstat(na - nb)
            out.append(f"{sn}: LS {m1:+5.1f}% (t {t1:+.1f})  L {m2:+5.1f}% (t {t2:+.1f})")
        print(f"{lab:44s} " + "   ".join(out))
        dl, dn, yy = daily(a, "utrain")[0] - daily(b, "utrain")[0], daily(a, "utrain")[1] - daily(b, "utrain")[1], years[ut]
        print(f"{'':44s} 逐年 LS: " + "  ".join(f"{y} {np.nanmean(dl[yy == y]) * 25200:+5.1f}%" for y in yrs)
              + "   逐年 L: " + "  ".join(f"{y} {np.nanmean(dn[yy == y]) * 25200:+5.1f}%" for y in yrs), flush=True)
    print(f"[rev1] B done {time.time() - T0:.0f}s", flush=True)

    # ------------------------------------------------------------------ C
    print("\n== C. 加 C 之后的增量 d = a - b 对纯成交额水平同一本书的收益回归:d = alpha + beta * x ==")
    print("   (LS 行:x = 纯成交额@同半衰期 的多空净收益;L 行:x = 纯成交额@同半衰期 的多头腿净超额。"
          "夏普变化拆成两步:只换波动(均值不变)/ 再换均值)")
    for a, b, f_, lab in ((("std9*C", 2), ("std9", 2), ("dsum", 2), "stdamt9*C@2 - stdamt9@2"),
                          (("std9*C", 10), ("std9", 10), ("dsum", 10), "stdamt9*C@10 - stdamt9@10"),
                          (("dsum*C^2", 10), ("dsum", 10), ("dsum", 10), "k2@10 - 纯成交额@10"),
                          (("dsum*C^3", 10), ("dsum", 10), ("dsum", 10), "k3@10 - 纯成交额@10")):
        for leg, j in (("LS", 0), ("L ", 1)):
            for sn, _ in SPL:
                ya, yb, x = daily(a, sn)[j], daily(b, sn)[j], daily(f_, sn)[j]
                ok = np.isfinite(ya) & np.isfinite(yb) & np.isfinite(x)
                ya, yb, x = ya[ok], yb[ok], x[ok]
                d = ya - yb
                beta = float(np.cov(d, x)[0, 1] / x.var(ddof=1))
                al = d - beta * x
                sa, sb = ya.mean() / ya.std() * np.sqrt(252), yb.mean() / yb.std() * np.sqrt(252)
                s_vol = yb.mean() / ya.std() * np.sqrt(252)                 # b 的均值配上 a 的波动
                print(f"{lab:28s} {leg} {sn:6s}: d {d.mean() * 25200:+5.1f}% (t {d.mean() / d.std() * np.sqrt(d.size):+.1f})  "
                      f"beta {beta:+.2f}  corr {np.corrcoef(d, x)[0, 1]:+.2f}  alpha {al.mean() * 25200:+5.1f}% "
                      f"(t {al.mean() / al.std() * np.sqrt(al.size):+.1f})   年化波动 {yb.std() * np.sqrt(252) * 100:.2f}% -> {ya.std() * np.sqrt(252) * 100:.2f}%   "
                      f"夏普 {sb:+.2f} -> {sa:+.2f}(只换波动 {s_vol - sb:+.2f},再换均值 {sa - s_vol:+.2f})", flush=True)
    print(f"[rev1] C done {time.time() - T0:.0f}s", flush=True)

    # ------------------------------------------------------------------ D
    print("\n== D. 剔除名单:C 角落在已知的两类剔除之外还有没有增量 ==")
    amt = np.asarray(st.control("ctl_amt"), dtype=np.float64)[:cut]
    turn = np.asarray(st.control("ctl_turnrate"), dtype=np.float64)[:cut]
    rev1 = np.asarray(st.control("ctl_rev1"), dtype=np.float64)[:cut]
    lim = (rev1 >= 1.095).astype(np.float64)
    lim[~np.isfinite(rev1)] = np.nan
    lim5 = rsum(lim, 5)
    rec = {}

    def put(k, t, v):
        if k not in rec:
            rec[k] = np.full(cut, np.nan)
        rec[k][t] = v

    for t in range(tr.start, cut):
        a_, c_, u_, y_ = amt[t], C[t], turn[t], tgt[t]
        m = np.isfinite(a_) & np.isfinite(c_) & np.isfinite(u_) & np.isfinite(y_)
        if m.sum() < 500:
            continue
        idx = np.nonzero(m)[0]
        y = y_[idx]
        ew = y.mean()
        ex = y - ew
        row = qcut(a_[idx]) == 4
        ri = np.nonzero(row)[0]
        Cc = np.zeros(idx.size, dtype=bool)
        Tc = np.zeros(idx.size, dtype=bool)
        Cc[ri[qcut(c_[idx][ri]) == 4]] = True
        Tc[ri[qcut(u_[idx][ri]) == 4]] = True
        L5 = np.nan_to_num(lim5[t][idx], nan=0.0) > 0            # 全市场:近 5 日(含当天)有过 >= 9.5% 的日涨幅
        K = Tc | L5                                              # 已知的两类剔除
        sets = {"C角落": Cc, "换手率角落": Tc, "近5日涨停(全市场)": L5, "已知两类之并": K,
                "C角落 且 不在已知两类里": Cc & ~K, "C角落 且 在已知两类里": Cc & K,
                "成交额最高1/5 且 不在三类里": row & ~K & ~Cc}
        for nm, s in sets.items():
            put(f"n|{nm}", t, s.mean())
            if s.sum() >= 5:
                put(f"ex|{nm}", t, ex[s].mean())
        for nm, s in (("剔 C角落", Cc), ("剔 换手率角落", Tc), ("剔 近5日涨停", L5), ("剔 已知两类", K), ("剔 已知两类 + C角落", K | Cc)):
            put(f"gain|{nm}", t, y[~s].mean() - ew)
        put("gain|增量:已知两类之后再剔 C角落", t, y[~(K | Cc)].mean() - y[~K].mean())
        put("gain|增量:C角落之后再剔 已知两类", t, y[~(K | Cc)].mean() - y[~Cc].mean())
        # 在"干净的活跃票"(成交额最高 1/5、不在已知两类里)内部,C 还排不排得动
        cl = np.nonzero(row & ~K)[0]
        if cl.size >= 100:
            q = qcut(c_[idx][cl])
            put("clean|C5", t, ex[cl][q == 4].mean() - ex[cl].mean())
            put("clean|C1", t, ex[cl][q == 0].mean() - ex[cl].mean())
            rc = np.argsort(np.argsort(c_[idx][cl])).astype(np.float64)
            re_ = np.argsort(np.argsort(ex[cl])).astype(np.float64)
            put("clean|ic", t, float(np.corrcoef(rc, re_)[0, 1]))

    yy = sorted(set(years[tr.start:cut].tolist()))
    PER = [("train", np.arange(cut)[tr]), ("valid", np.arange(cut)[va])] + [(y, np.nonzero(years == y)[0]) for y in yy]
    hdr = "".join(f"{n:>9s}" for n, _ in PER)

    def ann(k, rows):
        return float(np.nanmean(rec[k][rows]) * 252 * 100) if k in rec else np.nan

    def tt(k, rows):
        f = rec[k][rows]
        f = f[np.isfinite(f)]
        return float(f.mean() / f.std() * np.sqrt(f.size)) if f.size > 5 and f.std() > 0 else np.nan

    print("\nD1. 各集合占全市场(有信号有标签的票)的比例(%)与次日超额(年化 %,相对全市场等权)")
    print(f"{'':34s}{hdr}")
    for nm in ("C角落", "换手率角落", "近5日涨停(全市场)", "已知两类之并", "C角落 且 在已知两类里", "C角落 且 不在已知两类里", "成交额最高1/5 且 不在三类里"):
        print(f"{'占比 ' + nm:34s}" + "".join(f"{np.nanmean(rec['n|' + nm][r]) * 100:8.2f}%" for _, r in PER))
        print(f"{'超额 ' + nm:34s}" + "".join(f"{ann('ex|' + nm, r):+9.1f}" for _, r in PER))
    print("\nD2. 全市场等权组合剔掉某个集合之后,相对不剔的年化超额(%);括号行 = 日度 t 值")
    print(f"{'':34s}{hdr}")
    for nm in ("剔 C角落", "剔 换手率角落", "剔 近5日涨停", "剔 已知两类", "剔 已知两类 + C角落", "增量:已知两类之后再剔 C角落", "增量:C角落之后再剔 已知两类"):
        print(f"{nm:34s}" + "".join(f"{ann('gain|' + nm, r):+9.2f}" for _, r in PER))
        print(f"{'   (t)':34s}" + "".join(f"{tt('gain|' + nm, r):+9.1f}" for _, r in PER))
    print("\nD3. 干净的活跃票(成交额最高 1/5、不在已知两类里)内部按 C 再五分:最高 / 最低组相对这批票平均的次日超额(年化 %)与组内 rank IC")
    print(f"{'':34s}{hdr}")
    print(f"{'C 最高组 - 这批票平均':34s}" + "".join(f"{ann('clean|C5', r):+9.1f}" for _, r in PER))
    print(f"{'C 最低组 - 这批票平均':34s}" + "".join(f"{ann('clean|C1', r):+9.1f}" for _, r in PER))
    print(f"{'组内 rank IC':34s}" + "".join(f"{float(np.nanmean(rec['clean|ic'][r])):+9.4f}" for _, r in PER))
    print(f"{'   (t)':34s}" + "".join(f"{tt('clean|ic', r):+9.1f}" for _, r in PER))
    print(f"[rev1] done {time.time() - T0:.0f}s", flush=True)
