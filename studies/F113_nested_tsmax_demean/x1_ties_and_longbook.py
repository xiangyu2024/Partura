"""studies/F113_nested_tsmax_demean/x1_ties_and_longbook.py -- 工单 R1 (B)。

六个区块(H1/H2/H6/H7)+ 主研补注 B 节(H11:多头腿是不是按股票代码挑的)。
只用 train / valid;st.slice("holdout") 会直接报错,本脚本不触碰。

口径说明(写在这里,免得散在各处):
  - "多头腿"/"空头腿"全部由 sig = st.signal(panel)(方向 x 面板,按多头口径半衰期平滑)决定成员,
    tie-break 用 alphacube.metrics.long_short_weights 的口径(argsort kind='stable',非有限值排最后)。
    n_long = round(0.10 * 当天有效股票数)——工单明确要求 round;生产的 long_short_weights 用的是
    floor(max(1, floor(n*0.10))),源码见 alphacube/metrics.py:282 的注释。两者只在 n*0.10 恰好
    卡在 .5 附近时相差 <=1 个名额,结果卡里会提一句,不单独修正。
  - 区块 1 的"dist 自检"和区块 2 的 A 面板,显式要求用"raw 面板、不翻方向不平滑",所以这两处用的是
    p_base / A 的原始值,不是 sig。区块 1 的"多头腿内部不同取值数/并列组/切割点"这几项,因为问的是
    "这个名额是不是靠 tie-break 选出来的"(第 3 条明确写的是"sig 值"),用的是 sig,不是 raw 面板
    ——sig 在 hl=1 下对"偶然""某一天恰好相同"的名字基本不会保留并列(EMA 是全历史的确定性函数,
    两个历史不同的股票几乎不可能在 float64 下精确相等),但对"历史上持续精确相同"的退化股票(比如
    连续多天 Ret 精确为 0)仍然会精确相等——这正是 H1/H11 想抓的那类并列,用 sig 量更干净。
  - 区块 1~5 的"每个抽样日"用同一套抽样日集合(train / valid 分开,每 5 天取 1 天,用 p_base 当天
    有效股票数 >= 30 过滤),和 partura/diagnose.py:136 的 distinct_fraction 对齐。区块 6 要的是
    "年化"数字,用的是整个 split 的全部交易日(不抽样),口径和主表的 Lgross/short 一致。

任一区块失败打印一行 "[BLOCK k FAILED] <原因>" 后继续跑后面的区块。
"""
import warnings

import numpy as np

warnings.filterwarnings("ignore")

from partura.study_tools import Study, bk, dg  # noqa: E402

FID = "F113_nested_tsmax_demean"
STEP, MIN_NAMES = 5, 30  # 和 partura/diagnose.py:136 distinct_fraction 对齐
TOP_FRAC_DEFAULT = 0.10

V_BASE_EXPR = ("pow_1_5(ts_max(pow_2(cs_demean(mul(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(day_mean(Ret), 5), "
               "-5)), 30)), 20), 5))), 30))")
G_EXPR = "ts_max(pow_2(ts_max(cs_demean(ts_max(day_mean(Ret), 5)), 30)), 20)"
A_EXPR = "day_mean(Ret)"
C9_EXPR = ("pow_1_5(ts_max(pow_2(cs_demean(cs_rank(ts_max(pow_2(ts_max(cs_demean(ts_max(day_mean(Ret), 5)), 30)), "
           "20)))), 30))")

CONTROL_NAMES = ["ctl_amt", "ctl_cap", "ctl_turnrate", "ctl_ivol", "ctl_dvol20", "ctl_rev1", "ctl_mom20",
                 "known_stdamt_mean30", "known_stdamt_max9", "known_amt_max9"]
KNOWN_NAMES = ["known_stdamt_mean30", "known_stdamt_max9"]

BOARD_MAP = {"600": "沪主板", "601": "沪主板", "603": "沪主板", "605": "沪主板",
             "000": "深主板+中小", "001": "深主板+中小", "002": "深主板+中小", "003": "深主板+中小",
             "300": "创业板", "301": "创业板", "688": "科创板"}


def hdr(s):
    print("\n" + "=" * 8 + " " + s + " " + "=" * 8, flush=True)


def board_of(sym):
    """A 股代码前缀 -> 板块;代码不是 3 位以上数字前缀时退化成前 3 个字符(工单原文的兜底条款)。"""
    s = str(sym)
    digits = "".join(ch for ch in s if ch.isdigit())
    pfx = digits[:3] if len(digits) >= 3 else s[:3]
    if pfx in BOARD_MAP:
        return BOARD_MAP[pfx]
    if pfx[:1] in ("8", "4"):
        return "北交所"
    return "其他"


def pick_legs(row, top_frac=TOP_FRAC_DEFAULT):
    """production(alphacube.metrics.long_short_weights)的 tie-break 口径:
    argsort(kind='stable'),非有限值推成 +inf(排最后,升序中垫底)。
    n_long = n_short = round(top_frac * 有效股票数)(工单明确要求 round,见模块 docstring)。
    返回 (long_mask, short_mask, n_valid, k, order)。"""
    row = np.asarray(row, dtype=np.float64)
    fin = np.isfinite(row)
    n = int(fin.sum())
    lmask = np.zeros(row.shape[0], dtype=bool)
    smask = np.zeros(row.shape[0], dtype=bool)
    if n < 2:
        return lmask, smask, n, 0, None
    k = max(1, int(round(top_frac * n)))
    order = np.argsort(np.where(fin, row, np.inf), kind="stable")
    smask[order[:k]] = True
    lmask[order[n - k:n]] = True
    return lmask, smask, n, k, order


def col_quantiles(valid_cols_sorted):
    """给定(已按原始列序升序排好的)有效列下标数组,返回 {col: (rank+0.5)/n} 分位字典。"""
    n = valid_cols_sorted.size
    if n == 0:
        return {}
    q = (np.arange(n) + 0.5) / n
    return dict(zip(valid_cols_sorted.tolist(), q.tolist()))


def sampled_rows(day_slice, ref_valid_count, step=STEP, min_names=MIN_NAMES):
    start, stop = day_slice.start, day_slice.stop
    idx = np.arange(start, stop, step)
    return idx[ref_valid_count[idx] >= min_names]


def med(xs):
    a = np.asarray([x for x in xs if x is not None and np.isfinite(x)], dtype=np.float64)
    return float(np.median(a)) if a.size else float("nan")


def med_p90(xs):
    a = np.asarray([x for x in xs if x is not None and np.isfinite(x)], dtype=np.float64)
    if a.size == 0:
        return float("nan"), float("nan")
    return float(np.median(a)), float(np.percentile(a, 90))


def ann_pct(x):
    f = np.asarray(x, dtype=np.float64)
    f = f[np.isfinite(f)]
    return float(np.nanmean(f) * 252 * 100) if f.size else float("nan")


def build_weights_round(sig_slice, top_frac=TOP_FRAC_DEFAULT):
    """和 alphacube.metrics.long_short_weights 同样的输出格式(等权 +-0.5/k,gross 1),
    但 k 用 round(本脚本统一口径),不是生产的 floor。逐日循环,D 不大(<=~1000)时很快。"""
    D, S = sig_slice.shape
    w = np.zeros((D, S), dtype=np.float64)
    for t in range(D):
        lmask, smask, n, k, order = pick_legs(sig_slice[t], top_frac)
        if k > 0:
            w[t, lmask] = 0.5 / k
            w[t, smask] = -0.5 / k
    return w


# ------------------------------------------------------------------ 自检(合成数据,不碰真实面板)
def _selftest():
    hdr("自检(合成数据,不是真实面板)")
    rng = np.random.default_rng(0)
    S = 50
    row = rng.normal(size=S)
    row[:10] = 3.0  # 一个 10 只股票的并列组,且是全场最大值(极端并列场景)
    row[10:13] = np.nan  # 缺失

    lmask, smask, n, k, order = pick_legs(row, top_frac=0.10)
    assert n == S - 3, f"自检失败: n={n}"
    assert k == max(1, round(0.10 * n)), f"自检失败: k={k}"
    assert lmask.sum() == k and smask.sum() == k, "自检失败: 多/空头腿人数不等于 k"
    tie_cols = np.where(row == 3.0)[0]
    in_long = lmask[tie_cols]
    print(f"[selftest] n={n} k={k} 并列组大小=10(全场最大值),多头腿里有 {int(in_long.sum())}/10 个"
          f"(k={k}<10 时应恰为 k)")
    assert in_long.sum() == min(k, 10)

    allnan = np.full(S, np.nan)
    lmask2, smask2, n2, k2, _ = pick_legs(allnan)
    assert n2 == 0 and lmask2.sum() == 0 and smask2.sum() == 0, "自检失败: 全 NaN 行应返回空腿"

    valid_cols = np.where(np.isfinite(row))[0]
    q = col_quantiles(valid_cols)
    assert abs(q[valid_cols[0]] - 0.5 / valid_cols.size) < 1e-9
    assert abs(q[valid_cols[-1]] - (valid_cols.size - 0.5) / valid_cols.size) < 1e-9
    print(f"[selftest] col_quantiles: 首位分位={q[valid_cols[0]]:.4f}  末位分位={q[valid_cols[-1]]:.4f}"
          f"(应分别接近 0 和 1)")

    for sym, exp in [("600519", "沪主板"), ("000001", "深主板+中小"), ("300750", "创业板"),
                      ("688981", "科创板"), ("430047", "北交所"), ("900901", "其他")]:
        got = board_of(sym)
        flag = "" if got == exp else "  <-- 不一致!"
        print(f"[selftest] board_of({sym}) = {got} (预期 {exp}){flag}")
        assert got == exp

    const_row = np.full((10, S), 7.0)
    df_const = dg.distinct_fraction(const_row)
    uniq_row = np.tile(np.arange(S, dtype=np.float64), (10, 1))
    df_uniq = dg.distinct_fraction(uniq_row)
    print(f"[selftest] distinct_fraction: 全常数矩阵={df_const:.4f}(预期 {1.0 / S:.4f})  "
          f"全不同矩阵={df_uniq:.4f}(预期 1.0000)")
    assert abs(df_const - 1.0 / S) < 1e-6 and abs(df_uniq - 1.0) < 1e-6

    # build_weights_round 的 gross/净 0 自检
    D = 20
    sig_syn = rng.normal(size=(D, S))
    w = build_weights_round(sig_syn, 0.10)
    gross = np.abs(w).sum(1)
    net = w.sum(1)
    assert np.allclose(gross, 1.0), f"自检失败: gross 应恒为 1,实际 {gross[:3]}"
    assert np.allclose(net, 0.0), f"自检失败: net 应恒为 0,实际 {net[:3]}"
    print(f"[selftest] build_weights_round: gross={gross[0]:.4f} net={net[0]:.6f}(预期 1.0000 / 0.000000)")
    print("[selftest] 全部通过\n", flush=True)


_selftest()


def main():
    with Study(FID) as st:
        cost = float(st.cfg.get("cost_per_side", 0.0015))
        top_frac = float(st.cfg.get("top_frac", 0.10))
        rank_by = st.cfg.get("rank_by", "long")
        hl_key = "hl_long" if rank_by == "long" else "hl_ls"

        hdr("面板(应大多命中 S1_chain 留下的共享缓存:p_base=v_base,G=c3_g_fold1,c9=c9_rankfold)")
        P = st.panels({"base": V_BASE_EXPR, "G": G_EXPR, "A": A_EXPR, "c9": C9_EXPR})
        missing = [k for k in ("base", "G", "A", "c9") if k not in P]
        if missing:
            print("MISSING panels:", missing, flush=True)
        p_base64 = np.asarray(P["base"], dtype=np.float64)
        G64 = np.asarray(P["G"], dtype=np.float64)
        A64 = np.asarray(P["A"], dtype=np.float64)
        c9_64 = np.asarray(P["c9"], dtype=np.float64)

        tgt64 = np.asarray(st.target(), dtype=np.float64)
        raw64 = np.asarray(st.target(buyable=False), dtype=np.float64)
        tr_sl, va_sl = st.slice("train"), st.slice("valid")
        ut_sl = st.slice("utrain")

        sig_base = np.asarray(st.signal(P["base"]), dtype=np.float64)
        sig_c9 = np.asarray(st.signal(P["c9"]), dtype=np.float64)

        valid_count_base = np.isfinite(p_base64).sum(1)
        tr_idx = sampled_rows(tr_sl, valid_count_base)
        va_idx = sampled_rows(va_sl, valid_count_base)
        all_idx = np.concatenate([tr_idx, va_idx])
        print(f"抽样:train 全长 {tr_sl.stop - tr_sl.start} 天中取 {tr_idx.size} 天;"
              f"valid 全长 {va_sl.stop - va_sl.start} 天中取 {va_idx.size} 天", flush=True)

        syms = np.asarray(st.symbols)
        print(f"symbols: n={syms.size}  前 5 个={list(syms[:5])}  后 5 个={list(syms[-5:])}", flush=True)

        def legs_table(sig64, idx):
            return {int(t): pick_legs(sig64[t], top_frac) for t in idx}

        legs_base = legs_table(sig_base, all_idx)
        legs_c9 = legs_table(sig_c9, all_idx)

        # ---------------------------------------------------------- 区块 1
        try:
            hdr("区块 1 -- 并列结构(H1,最重要)")
            dist_train_only = dg.distinct_fraction(p_base64[tr_sl])
            pooled = []
            for sl in (tr_sl, va_sl):
                for t in range(sl.start, sl.stop, STEP):
                    r = p_base64[t]
                    r = r[np.isfinite(r)]
                    if r.size >= MIN_NAMES:
                        pooled.append(np.unique(r).size / r.size)
            dist_pooled = float(np.median(pooled)) if pooled else float("nan")
            print(f"[自检] dist(train 单独切片,等同生产 S0 的口径 dg.distinct_fraction(p64[train])) "
                  f"= {dist_train_only:.4f}")
            print(f"[自检] dist(train+valid,按工单原文字面'合起来的中位数') = {dist_pooled:.4f}   "
                  f"S0 公布值 = 0.5847")
            print(f"[自检] train-only 对上(±0.02)? {abs(dist_train_only - 0.5847) <= 0.02}   "
                  f"train+valid 合并对上? {abs(dist_pooled - 0.5847) <= 0.02}")

            def tie_block(idx):
                out = {k: [] for k in ("dist", "tie2", "tie10", "maxgrp", "dist_s", "tie2_s", "tie10_s", "maxgrp_s",
                                        "cut_n", "cut_in", "cut_out", "cut_n_s", "cut_in_s", "cut_out_s")}
                for t in idx:
                    row = sig_base[t]  # 并列/切割点问的是实际交易信号里的并列,见模块 docstring
                    fin = np.isfinite(row)
                    if fin.sum() < MIN_NAMES:
                        continue
                    lmask, smask, n, k, order = legs_base[t]
                    if n < MIN_NAMES:
                        continue
                    vals = row[fin]
                    uniq, inv, counts = np.unique(vals, return_inverse=True, return_counts=True)
                    grp = np.full(row.shape[0], np.nan)
                    grp[fin] = counts[inv]
                    gl, gs = grp[lmask], grp[smask]
                    out["dist"].append(np.unique(row[lmask]).size / max(int(lmask.sum()), 1))
                    out["tie2"].append(float((gl >= 2).mean()))
                    out["tie10"].append(float((gl >= 10).mean()))
                    out["maxgrp"].append(float(gl.max()) if gl.size else np.nan)
                    out["dist_s"].append(np.unique(row[smask]).size / max(int(smask.sum()), 1))
                    out["tie2_s"].append(float((gs >= 2).mean()))
                    out["tie10_s"].append(float((gs >= 10).mean()))
                    out["maxgrp_s"].append(float(gs.max()) if gs.size else np.nan)
                    cutoff_l = row[order[n - k]]
                    tie_l = fin & (row == cutoff_l)
                    out["cut_n"].append(int(tie_l.sum()))
                    out["cut_in"].append(int((tie_l & lmask).sum()))
                    out["cut_out"].append(int((tie_l & ~lmask).sum()))
                    cutoff_s = row[order[k - 1]]
                    tie_s = fin & (row == cutoff_s)
                    out["cut_n_s"].append(int(tie_s.sum()))
                    out["cut_in_s"].append(int((tie_s & smask).sum()))
                    out["cut_out_s"].append(int((tie_s & ~smask).sum()))
                return {k: med_p90(v) for k, v in out.items()}

            r_tr, r_va = tie_block(tr_idx), tie_block(va_idx)
            print("\n多头腿(sig 口径,train / valid,中位数 / p90):")
            for key, label in [("dist", "不同取值数/n_long"), ("tie2", "并列组>=2 占比"),
                                ("tie10", "并列组>=10 占比"), ("maxgrp", "腿内最大并列组大小")]:
                mt, pt = r_tr[key]
                mv, pv = r_va[key]
                print(f"  {label:<18} train {mt:.3f}/{pt:.3f}   valid {mv:.3f}/{pv:.3f}")
            print("空头腿(对照,同一套 sig,train / valid,中位数 / p90):")
            for key, label in [("dist_s", "不同取值数/n_short"), ("tie2_s", "并列组>=2 占比"),
                                ("tie10_s", "并列组>=10 占比"), ("maxgrp_s", "腿内最大并列组大小")]:
                mt, pt = r_tr[key]
                mv, pv = r_va[key]
                print(f"  {label:<18} train {mt:.3f}/{pt:.3f}   valid {mv:.3f}/{pv:.3f}")
            print("切割点并列(train / valid,中位数 / p90):")
            for key, label in [("cut_n", "多头切割点同值股票数"), ("cut_in", "  其中进了多头腿"),
                                ("cut_out", "  其中被切掉"), ("cut_n_s", "空头切割点同值股票数"),
                                ("cut_in_s", "  其中进了空头腿"), ("cut_out_s", "  其中被切掉")]:
                mt, pt = r_tr[key]
                mv, pv = r_va[key]
                print(f"  {label:<20} train {mt:.3f}/{pt:.3f}   valid {mv:.3f}/{pv:.3f}")
        except Exception as exc:
            print(f"[BLOCK 1 FAILED] {type(exc).__name__}: {exc}", flush=True)

        # ---------------------------------------------------------- 区块 2
        try:
            hdr("区块 2 -- 退化票(H1 的机械来源;A = day_mean(Ret),raw、不翻方向不平滑)")
            ut_fin = np.isfinite(A64[ut_sl])
            full_ratio = float((A64[ut_sl] == 0.0).sum() / max(int(ut_fin.sum()), 1))
            print(f"全样本(train+valid 合并,有值格子里 A==0 的比例) = {full_ratio:.4f}")

            def zero_block(idx):
                r_l, r5_l, r_s, r5_s, r_m, r5_m = [], [], [], [], [], []
                for t in idx:
                    row = A64[t]
                    fin = np.isfinite(row)
                    if fin.sum() < MIN_NAMES:
                        continue
                    lmask, smask, n, k, order = legs_base[t]
                    if n < MIN_NAMES:
                        continue
                    is0 = fin & (row == 0.0)
                    if t >= 4:
                        hist = A64[t - 4:t + 1]
                        all0 = np.all(hist == 0.0, axis=0) & np.all(np.isfinite(hist), axis=0)
                    else:
                        all0 = np.zeros(row.shape[0], dtype=bool)
                    r_l.append(float(is0[lmask].mean()) if lmask.sum() else np.nan)
                    r5_l.append(float(all0[lmask].mean()) if lmask.sum() else np.nan)
                    r_s.append(float(is0[smask].mean()) if smask.sum() else np.nan)
                    r5_s.append(float(all0[smask].mean()) if smask.sum() else np.nan)
                    r_m.append(float(is0[fin].mean()) if fin.sum() else np.nan)
                    r5_m.append(float(all0[fin].mean()) if fin.sum() else np.nan)
                return r_l, r5_l, r_s, r5_s, r_m, r5_m

            for name, idx in (("train", tr_idx), ("valid", va_idx)):
                r_l, r5_l, r_s, r5_s, r_m, r5_m = zero_block(idx)
                ml, m5l, ms, m5s, mm, m5m = med(r_l), med(r5_l), med(r_s), med(r5_s), med(r_m), med(r5_m)
                enrich1 = ml / mm if mm else float("nan")
                enrich5 = m5l / m5m if m5m else float("nan")
                print(f"[{name}] A==0 占比中位数:多头腿 {ml:.4f}  空头腿 {ms:.4f}  全市场 {mm:.4f}"
                      f"  (多头腿富集倍数 {enrich1:.2f}x)")
                print(f"[{name}] 过去5天A全部==0 占比中位数:多头腿 {m5l:.4f}  空头腿 {m5s:.4f}  全市场 {m5m:.4f}"
                      f"  (多头腿富集倍数 {enrich5:.2f}x)")
        except Exception as exc:
            print(f"[BLOCK 2 FAILED] {type(exc).__name__}: {exc}", flush=True)

        # ---------------------------------------------------------- 区块 3
        try:
            hdr("区块 3 -- 折叠中心在哪(H2;G = ts_max(pow_2(ts_max(cs_demean(ts_max(day_mean(Ret),5)),30)),20))")

            def g_block(idx):
                qmean_list, ql_list, qs_list = [], [], []
                for t in idx:
                    row = G64[t]
                    fin = np.isfinite(row)
                    if fin.sum() < MIN_NAMES:
                        continue
                    lmask, smask, n, k, order = legs_base[t]
                    if n < MIN_NAMES:
                        continue
                    vals = row[fin]
                    m = float(np.nanmean(vals))
                    qmean_list.append(float((vals <= m).mean()))
                    rk = np.argsort(np.argsort(vals, kind="stable"))
                    pr = (rk + 0.5) / vals.size
                    full_pr = np.full(row.shape[0], np.nan)
                    full_pr[fin] = pr
                    ql_list.append(float(np.nanmedian(full_pr[lmask])) if lmask.sum() else np.nan)
                    qs_list.append(float(np.nanmedian(full_pr[smask])) if smask.sum() else np.nan)
                return qmean_list, ql_list, qs_list

            for name, idx in (("train", tr_idx), ("valid", va_idx)):
                qmean_list, ql_list, qs_list = g_block(idx)
                arr = np.asarray(qmean_list, dtype=np.float64)
                if arr.size:
                    print(f"[{name}] nanmean(G) 在当天 G 分布里的分位:中位数 {np.median(arr):.3f}  "
                          f"Q1 {np.percentile(arr, 25):.3f}  Q3 {np.percentile(arr, 75):.3f}  (H2 预期 >=0.75)")
                else:
                    print(f"[{name}] 无有效抽样日")
                print(f"[{name}] 多头腿成员当天 G 分位的中位数 = {med(ql_list):.3f}   "
                      f"空头腿 = {med(qs_list):.3f}   (全市场基准 0.50;H2 预期多头腿贴着上面那行的分位,不贴 0.5)")
        except Exception as exc:
            print(f"[BLOCK 3 FAILED] {type(exc).__name__}: {exc}", flush=True)

        # ---------------------------------------------------------- 区块 4
        ctl_panels = {}
        try:
            hdr("区块 4 -- 多头腿的已知暴露成分(分辨;study_playbook.md §6.5 的口径)")
            for name in CONTROL_NAMES:
                try:
                    ctl_panels[name] = np.asarray(st.control(name), dtype=np.float64)
                except Exception as exc:
                    print(f"  控制变量 {name} 取不到: {type(exc).__name__}: {exc}")

            def ctl_block(idx, cp):
                rl, rs = [], []
                for t in idx:
                    row = cp[t]
                    fin = np.isfinite(row)
                    if fin.sum() < MIN_NAMES:
                        continue
                    lmask, smask, n, k, order = legs_base[t]
                    if n < MIN_NAMES:
                        continue
                    vals = row[fin]
                    rk = np.argsort(np.argsort(vals, kind="stable"))
                    pr = (rk + 0.5) / vals.size
                    full_pr = np.full(row.shape[0], np.nan)
                    full_pr[fin] = pr
                    rl.append(float(np.nanmedian(full_pr[lmask])) if lmask.sum() else np.nan)
                    rs.append(float(np.nanmedian(full_pr[smask])) if smask.sum() else np.nan)
                return rl, rs

            print(f"{'控制变量':<22}{'多头腿分位 train':>17}{'valid':>9}{'空头腿分位 train':>17}{'valid':>9}")
            for name, cp in ctl_panels.items():
                rl_tr, rs_tr = ctl_block(tr_idx, cp)
                rl_va, rs_va = ctl_block(va_idx, cp)
                print(f"{name:<22}{med(rl_tr):17.3f}{med(rl_va):9.3f}{med(rs_tr):17.3f}{med(rs_va):9.3f}")
            print("(全市场基准 = 0.50)")
        except Exception as exc:
            print(f"[BLOCK 4 FAILED] {type(exc).__name__}: {exc}", flush=True)

        # ---------------------------------------------------------- 区块 5
        try:
            hdr("区块 5 -- 与已知家族多头腿的重合率(H7)")
            known_sig = {}
            for name in KNOWN_NAMES:
                panel = ctl_panels.get(name)
                if panel is None:
                    panel = np.asarray(st.control(name), dtype=np.float64)
                try:
                    sg = st.sign(panel, "train")
                    hl = bk.fit_halflives(sg * panel, st.target(), st.slice("train"), cost, top_frac)[hl_key]
                    sigk = np.asarray(st.signal(panel, sign=sg, halflife=hl), dtype=np.float64)
                    print(f"  {name}: 工具选到 sign={sg:+.0f}  hl({rank_by})={hl:g}")
                except Exception as exc:
                    print(f"  {name}: st.signal 失败({type(exc).__name__}: {exc}),退回 sign=-1, hl=0")
                    sigk = bk.smoothed(-1.0 * panel, 0.0)
                known_sig[name] = sigk

            def overlap_block(idx, k_sig):
                ovl_l, ovl_s = [], []
                for t in idx:
                    lmask, smask, n, k, order = legs_base[t]
                    if n < MIN_NAMES:
                        continue
                    klmask, ksmask, kn, kk, korder = pick_legs(k_sig[t], top_frac)
                    if kn < MIN_NAMES:
                        continue
                    ovl_l.append(float((lmask & klmask).sum()) / max(int(lmask.sum()), 1))
                    ovl_s.append(float((smask & ksmask).sum()) / max(int(smask.sum()), 1))
                return ovl_l, ovl_s

            for name in KNOWN_NAMES:
                for split_name, idx in (("train", tr_idx), ("valid", va_idx)):
                    ovl_l, ovl_s = overlap_block(idx, known_sig[name])
                    print(f"  [{name}][{split_name}] 多头腿重合率中位数 = {med(ovl_l):.3f}   "
                          f"空头腿重合率中位数 = {med(ovl_s):.3f}   (随机基准 ~0.10)")
        except Exception as exc:
            print(f"[BLOCK 5 FAILED] {type(exc).__name__}: {exc}", flush=True)

        # ---------------------------------------------------------- 区块 6
        try:
            hdr("区块 6 -- 空头腿里有多少是封板票撑的(H6);权重用本脚本统一的 round(k) 口径(见 docstring)")

            for name, sl in (("train", tr_sl), ("valid", va_sl)):
                s = sig_base[sl]
                w = build_weights_round(s, top_frac)
                short_mask, long_mask = w < 0, w > 0
                short_ex_buy = bk.short_leg_excess(w, s, tgt64[sl])
                short_ex_raw = bk.short_leg_excess(w, s, raw64[sl])
                long_gross_buy = bk.long_book(w, s, tgt64[sl], cost)[1]
                long_gross_raw = bk.long_book(w, s, raw64[sl], cost)[1]
                print(f"[{name}] 空头腿毛年化超额:buyable(tgt) {ann_pct(short_ex_buy):+.1f}%   "
                      f"raw(不折成0) {ann_pct(short_ex_raw):+.1f}%")
                print(f"[{name}] 多头腿毛年化超额:buyable(tgt) {ann_pct(long_gross_buy):+.1f}%   "
                      f"raw(不折成0) {ann_pct(long_gross_raw):+.1f}%  (预期几乎不受影响,§6.6)")
                locked = np.isnan(tgt64[sl]) & np.isfinite(raw64[sl])
                for leg_name, mask in (("空头腿", short_mask), ("多头腿", long_mask)):
                    cells = mask & locked
                    frac = float(cells.sum()) / max(float(mask.sum()), 1.0)
                    raw_vals = np.where(cells, raw64[sl], np.nan)
                    mean_ann_pct = ann_pct(raw_vals[np.isfinite(raw_vals)]) if cells.sum() else float("nan")
                    print(f"[{name}] {leg_name}格子里「tgt=NaN 但 raw_tgt 有值」(封板票)占比 = {frac:.4f}   "
                          f"这些格子 raw_tgt 的年化均值 = {mean_ann_pct:+.1f}%")
        except Exception as exc:
            print(f"[BLOCK 6 FAILED] {type(exc).__name__}: {exc}", flush=True)

        # ---------------------------------------------------------- B 节(主研补注,H11)
        try:
            hdr("B 节(主研补注) -- 多头腿的成员资格是不是按股票代码定的(H11)")
            all_boards = [board_of(s) for s in syms]
            ub, cb = np.unique(all_boards, return_counts=True)
            tot = int(cb.sum())
            print("全市场板块占比基准(静态股票列表,不逐日重算): " +
                  "  ".join(f"{b} {c / tot:.1%}" for b, c in zip(ub, cb)))

            def section_b(name, legs_dict):
                for split_name, idx in (("train", tr_idx), ("valid", va_idx)):
                    colq_l, colq_s, long_cols_all = [], [], []
                    cut_med_in, cut_med_out = [], []
                    for t in idx:
                        lmask, smask, n, k, order = legs_dict[t]
                        if n < MIN_NAMES:
                            continue
                        fin = np.zeros(syms.shape[0], dtype=bool)
                        fin[order[:n]] = True  # order 的前 n 个就是全部有限值列(按值排序,列本身顺序不重要)
                        valid_cols = np.where(fin)[0]
                        q = col_quantiles(valid_cols)
                        lcols = np.where(lmask)[0]
                        scols = np.where(smask)[0]
                        colq_l.append(float(np.median([q[c] for c in lcols])))
                        colq_s.append(float(np.median([q[c] for c in scols])))
                        long_cols_all.append(lcols)
                        # 切割点并列(复用 legs_dict 里已经排好的 order/k/n,不重新 argsort)
                        row_sig = sig_base if legs_dict is legs_base else sig_c9
                        row = row_sig[t]
                        cutoff_l = row[order[n - k]]
                        tie_mask = np.isfinite(row) & (row == cutoff_l)
                        tie_cols = np.where(tie_mask)[0]
                        in_cols = np.where(tie_mask & lmask)[0]
                        out_cols = np.where(tie_mask & ~lmask)[0]
                        if in_cols.size and out_cols.size:
                            cut_med_in.append(float(np.median(in_cols)))
                            cut_med_out.append(float(np.median(out_cols)))
                    print(f"  [{name}][{split_name}] 多头腿列序分位中位数 = {med(colq_l):.3f}   "
                          f"空头腿列序分位中位数 = {med(colq_s):.3f}   (全市场基准 0.50)")
                    if long_cols_all:
                        pooled_cols = np.concatenate(long_cols_all)
                        boards = [board_of(syms[c]) for c in pooled_cols]
                        ubx, cbx = np.unique(boards, return_counts=True)
                        totx = int(cbx.sum())
                        print(f"  [{name}][{split_name}] 多头腿板块占比(把全部抽样日的名额汇总后算,"
                              f"不是先按天算比例再取中位数): " +
                              "  ".join(f"{b} {c / totx:.1%}" for b, c in zip(ubx, cbx)))
                    print(f"  [{name}][{split_name}] 切割点上「进了」列下标中位数 = {med(cut_med_in):.1f}   "
                          f"「被切掉」列下标中位数 = {med(cut_med_out):.1f}   "
                          f"(有双边并列、两组都非空的抽样日数 = {len(cut_med_in)})")

            print("\n-- v_base --")
            section_b("v_base", legs_base)
            print("\n-- c9_rankfold --")
            section_b("c9_rankfold", legs_c9)
        except Exception as exc:
            print(f"[BLOCK B FAILED] {type(exc).__name__}: {exc}", flush=True)

    print("\n[x1_ties_and_longbook done]", flush=True)


if __name__ == "__main__":
    main()
