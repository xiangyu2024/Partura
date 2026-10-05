"""studies/F113_nested_tsmax_demean/x2_increment.py -- 工单 R2 (B)。

区块 1~5 按工单原文:H12 交叉表(区块1)、候选多头腿的已知暴露剖面(区块2)、
多头腿重合率(区块3)、增量①残差(区块4)、增量②名单分解(区块5)。
只用 train / valid;st.slice("holdout") 会直接报错,本脚本不触碰。所有"全长"计算
(区块4的残差 books、区块7)都手动把范围限定在 scope = train.start..utrain.stop,
不碰 utrain 之后的任何一行。

---- 区块 6、7 是什么(不是工单原文要的脚本区块,是补 (A) S2_bench 的一个缺口) ----
(A) 跑完后,diagnostics.by_year 只给了 kf_mean30/cb_c4_kf30 两行,diagnostics.neutralise
只给了 kf_mean30 一行 —— c4_nodemean_out 两个都没有,尽管这次往两个列表里都加了它。
读 partura/runner.py 确认原因(不是求值失败,是设计如此,不是 bug):
  - L76/L201: `ok = {vid: panels[vid] for vid in variants if vid in panels}`,而
    `variants = _variants_of(cfg, stages)` 只收当次 `run` 命令行传的 stage(s)自己的
    变体 —— 这次 `run` 只传了 `S2_bench`,`ok` 里只有这次的 10 个新变体。
  - L234 的 by_year 和 L253 的 neutralise 都要求 `v in ok`,所以 `c4_nodemean_out`
    (S1_chain 的变体)即使写进这两个 diagnostics 列表也不会被算。这跟 corr_ids /
    conditional / profile_ids 不一样 —— 那几个走的是 L108 的 `refs` 机制,跨阶段的
    id 一样能算(这就是为什么 rank_corr_train 里 c4_nodemean_out 那一行是全的)。
  - 真要修,需要再起一次把 `S1_chain` 也传进 `run` 的 stage 参数(或者单独重跑
    S1_chain,带上新的 by_year/neutralise 列表)。但工单把这张工单锁定在 2 次服务器
    运行,(A)+(B) 已经用满,没有再起一次。
区块 6/7 改用 partura.study_tools.Study 直接调 bk/dg(跟 runner.py 内部用的是同一套
函数,公式逐行对应 L263-290/L236-250),在这次 (B) 里把这两个数字算出来,口径和主表
(kf_mean30 那两张表)保持一致,可以直接并排比较。这是执行为了把工单第 6/7 项数字落
地做的变通,不是工单原文的脚本区块,结果卡里会单独说明。
  **唯一的口径差异**:dg.neutralise 内部要求当天有效股票数 >=50 才回归(否则整天
  NaN),工单给区块4定的门槛是"<30 弃"。区块6复用的是主表自己用的同一个 dg.neutralise
  (没有另写一个 50->30 的版本),因为这样才能和 kf_mean30 的 all_controls 数字同口径
  比较;这个门槛差异比工单原文更严格(弃的天更多),不会凭空制造 alpha。

任一区块失败打印一行 "[BLOCK k FAILED] <原因>" 后继续跑后面的区块 —— 除了开头对真实
数据的自检:自检不过直接 raise,按工单要求"标红"停下,不跑后面的区块。

本脚本的新函数(decile_matrix / pct_matrix / pick_legs 的 floor 改动)已经在本机用
合成数据做过逐位核对(scratchpad/pretest_helpers.py,手算 vs 代码逐位相同),这里的
_selftest() 是搬进服务器环境后再跑一遍同样的断言 + 一个真实会用到 dg.neutralise 的
已知答案自检。
"""
import warnings

import numpy as np

warnings.filterwarnings("ignore")

from partura.study_tools import Study, bk, dg  # noqa: E402

FID = "F113_nested_tsmax_demean"
STEP, MIN_NAMES = 5, 30
TOP_FRAC_DEFAULT = 0.10

E_VBASE = ("pow_1_5(ts_max(pow_2(cs_demean(mul(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(day_mean(Ret), 5), "
           "-5)), 30)), 20), 5))), 30))")
E_G = "ts_max(pow_2(ts_max(cs_demean(ts_max(day_mean(Ret), 5)), 30)), 20)"
E_C4 = "ts_max(ts_max(pow_2(ts_max(cs_demean(ts_max(day_mean(Ret), 5)), 30)), 20), 30)"
E_M1 = "ts_max(ts_max(cs_demean(day_mean(Ret)), 50), 30)"
E_N2 = "ts_max(ts_max(day_mean(Ret), 50), 30)"

# 区块 2 用(和 x1_ties_and_longbook.py 的 CONTROL_NAMES 相同的 10 个)
CONTROL_NAMES_10 = ["ctl_amt", "ctl_cap", "ctl_turnrate", "ctl_ivol", "ctl_dvol20", "ctl_rev1", "ctl_mom20",
                     "known_stdamt_mean30", "known_stdamt_max9", "known_amt_max9"]
# 区块 6 用(主表 neutralise 诊断用的 9 个:controls 7 个 + external_controls 2 个)
CONTROL_NAMES_9 = ["ctl_amt", "ctl_price", "ctl_ivol", "ctl_range", "ctl_rev1", "ctl_mom20", "ctl_dvol20",
                    "ctl_cap", "ctl_turnrate"]


def hdr(s):
    print("\n" + "=" * 8 + " " + s + " " + "=" * 8, flush=True)


# ------------------------------------------------------- 辅助函数(复用自 x1_ties_and_longbook.py)
def pick_legs(row, top_frac=TOP_FRAC_DEFAULT):
    """production(alphacube.metrics.long_short_weights)的 tie-break 口径:
    argsort(kind='stable'),非有限值推成 +inf(排最后)。
    **本工单(R2)的改动**:n_long=n_short 从 R1 用的 round(top_frac*n) 改成
    floor(top_frac*n)(和生产 long_short_weights 一致)。返回
    (long_mask, short_mask, n_valid, k, order)。"""
    row = np.asarray(row, dtype=np.float64)
    fin = np.isfinite(row)
    n = int(fin.sum())
    lmask = np.zeros(row.shape[0], dtype=bool)
    smask = np.zeros(row.shape[0], dtype=bool)
    if n < 2:
        return lmask, smask, n, 0, None
    k = max(1, int(np.floor(top_frac * n)))
    order = np.argsort(np.where(fin, row, np.inf), kind="stable")
    smask[order[:k]] = True
    lmask[order[n - k:n]] = True
    return lmask, smask, n, k, order


def col_quantiles(valid_cols_sorted):
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


# ------------------------------------------------------- 本脚本新增的矩阵级辅助函数(已在本机预检,见模块 docstring)
def decile_matrix(sub, n=10):
    """逐行(逐日)分成 n 档,档 n = 值最高;和 partura/books.py:quantile_profile 的
    分桶公式(floor(pos/cnt*n))逐位相同。NaN 保留,返回 (labels 1..n 或 NaN, cnt)。"""
    sub = np.asarray(sub, dtype=np.float64)
    fin = np.isfinite(sub)
    order = np.argsort(np.where(fin, sub, np.inf), axis=1, kind="stable")
    cnt = fin.sum(axis=1)
    pos = np.empty_like(order)
    np.put_along_axis(pos, order, np.arange(sub.shape[1])[None, :].repeat(sub.shape[0], 0), axis=1)
    with np.errstate(invalid="ignore", divide="ignore"):
        q = np.floor(pos / np.maximum(cnt, 1)[:, None] * n)
    lab = np.where(fin, np.minimum(q, n - 1) + 1, np.nan)
    return lab, cnt


def pct_matrix(sub):
    """逐行(逐日)截面百分位 (0,1),同值用平均秩(dg.rank_rows 的口径)。"""
    sub = np.asarray(sub, dtype=np.float64)
    r = dg.rank_rows(sub)
    cnt = np.isfinite(sub).sum(axis=1, keepdims=True)
    with np.errstate(invalid="ignore", divide="ignore"):
        return (r - 0.5) / cnt


def resid_row(resid, info, tgt_tr, cost, top):
    """和 partura/runner.py 的内部函数 `_resid_row`(约 L263-272)逐行对应。"""
    icr = dg.ic_row(resid, tgt_tr, sign=1.0)
    br = bk.book_row(resid, tgt_tr, slice(0, resid.shape[0]), cost, top)
    return {"r2": info["mean_r2"], "rank_ic": icr["rank_ic"], "rank_icir": icr["rank_icir"],
            **{k: br[k] for k in ("ls_sharpe", "ls_gross_sharpe", "long_gross_ann", "short_gross_ann",
                                   "long_ann", "long_sharpe", "ls_turnover", "long_turnover")}}


def _years_of(study):
    try:
        y = np.asarray(study.ps.years)
        if y.size:
            return y
    except Exception:
        pass
    return np.asarray([int(d[:4]) for d in study.dates])


# ------------------------------------------------------------------ 自检
def _selftest():
    hdr("自检(合成数据)")
    rng = np.random.default_rng(0)
    S = 50

    row27 = rng.normal(size=27)
    _, _, n27, k27, _ = pick_legs(row27, 0.10)
    k27_round = max(1, int(round(0.10 * n27)))
    print(f"[selftest] pick_legs floor 改动:n={n27}  floor(0.10n)={k27}  round(0.10n)={k27_round}"
          f"  (0.10*{n27}={0.10 * n27:.2f},两者应该不同)")
    assert k27 == max(1, int(np.floor(0.10 * n27))) and k27 != k27_round

    row = rng.normal(size=S)
    row[:10] = 3.0
    row[10:13] = np.nan
    lmask, smask, n, k, order = pick_legs(row, top_frac=0.10)
    assert n == S - 3, f"自检失败: n={n}"
    assert k == max(1, int(np.floor(0.10 * n))), f"自检失败: k={k}"
    assert lmask.sum() == k and smask.sum() == k, "自检失败: 多/空头腿人数不等于 k"

    allnan = np.full(S, np.nan)
    _, _, n2, k2, _ = pick_legs(allnan)
    assert n2 == 0 and k2 == 0, "自检失败: 全 NaN 行应返回空腿"

    valid_cols = np.where(np.isfinite(row))[0]
    q = col_quantiles(valid_cols)
    assert abs(q[valid_cols[0]] - 0.5 / valid_cols.size) < 1e-9
    assert abs(q[valid_cols[-1]] - (valid_cols.size - 0.5) / valid_cols.size) < 1e-9

    uniq_row = np.arange(50, dtype=np.float64).reshape(1, 50)
    lab, cnt = decile_matrix(uniq_row, n=10)
    assert cnt[0] == 50
    assert list(lab[0, :5]) == [1.0] * 5 and list(lab[0, 45:]) == [10.0] * 5
    assert np.all(np.diff(lab[0]) >= 0), "decile_matrix 应该随值单调不降"
    print("[selftest] decile_matrix:50 个不同值分 10 档,每档 5 个,档位单调 -- 通过")

    row_tie = np.concatenate([np.arange(20, dtype=np.float64), np.full(5, 7.0)])
    lab_t, cnt_t = decile_matrix(row_tie.reshape(1, -1), n=10)
    assert cnt_t[0] == 25 and np.isfinite(lab_t).all()
    print(f"[selftest] decile_matrix 对并列值不报错,cnt={int(cnt_t[0])} -- 通过")

    pm = pct_matrix(uniq_row)
    assert pm[0, 0] < pm[0, -1] and 0.0 < pm[0, 0] < pm[0, -1] < 1.0
    tie_row = np.array([[1.0, 2.0, 2.0, 2.0, 3.0]])
    pm2 = pct_matrix(tie_row)
    assert abs(pm2[0, 1] - pm2[0, 2]) < 1e-9 and abs(pm2[0, 2] - pm2[0, 3]) < 1e-9, "并列应该拿到同一个百分位"
    assert abs(pm2[0, 1] - 0.5) < 1e-6, pm2
    print(f"[selftest] pct_matrix:单调 {pm[0, 0]:.3f}->{pm[0, -1]:.3f};三个并列的百分位相同={pm2[0, 1]:.3f} -- 通过")

    T, Sn = 30, 200
    rng2 = np.random.default_rng(1)
    ctl_raw = rng2.normal(size=(T, Sn))
    y_raw = 2.0 * ctl_raw + 0.01 * rng2.normal(size=(T, Sn))
    y_z = dg._zrank(y_raw)
    ctl_z = {"x": dg._zrank(ctl_raw)}
    resid, info = dg.neutralise(y_z, ctl_z, panel_ready=True, controls_ready=True)
    print(f"[selftest] dg.neutralise 已知答案自检:y=2*ctl+小噪声,all_controls R2={info['mean_r2']:.3f}(预期接近 1)")
    assert info["mean_r2"] > 0.9, f"自检失败: R2={info['mean_r2']}"

    print("[selftest] 全部通过\n", flush=True)


_selftest()


def main():
    with Study(FID) as st:
        cost = float(st.cfg.get("cost_per_side", 0.0015))
        top_frac = float(st.cfg.get("top_frac", 0.10))

        hdr("面板(大多应命中 S2_bench/S1_chain 留下的共享缓存)")
        P = st.panels({"vbase": E_VBASE, "G": E_G, "c4": E_C4, "m1": E_M1, "n2": E_N2})
        missing = [k for k in ("vbase", "G", "c4", "m1", "n2") if k not in P]
        if missing:
            print("MISSING panels:", missing, flush=True)
        p_vbase = np.asarray(P["vbase"], dtype=np.float64)
        p_G = np.asarray(P["G"], dtype=np.float64)
        p_c4 = np.asarray(P["c4"], dtype=np.float64)
        p_m1 = np.asarray(P["m1"], dtype=np.float64)
        p_n2 = np.asarray(P["n2"], dtype=np.float64)
        p_kf30 = np.asarray(st.control("known_stdamt_mean30"), dtype=np.float64)
        p_kf9 = np.asarray(st.control("known_stdamt_max9"), dtype=np.float64)
        p_dvol20 = np.asarray(st.control("ctl_dvol20"), dtype=np.float64)

        tgt = np.asarray(st.target(), dtype=np.float64)
        tr_sl, va_sl = st.slice("train"), st.slice("valid")
        ut_sl = st.slice("utrain")

        # -------------------------------------------- 开头自检(真实数据);不通过就 raise(工单要求"标红"停下)
        hdr("开头自检(真实数据):复现 S1_chain 里 c4_nodemean_out 的 +6.9% / +13.3%")
        b_c4 = st.books(p_c4, fit="train", evals=("train", "valid"))
        tr_long = b_c4["splits"]["train"]["long_ann"]
        va_long = b_c4["splits"]["valid"]["long_ann"]
        print(f"[自检] c4_nodemean_out train long_ann = {tr_long * 100:+.2f}%  (S1_chain 报的是 +6.9%,容差 ±0.3pp)")
        print(f"[自检] c4_nodemean_out valid long_ann = {va_long * 100:+.2f}%  (S1_chain 报的是 +13.3%,容差 ±0.5pp)")
        print(f"[自检] hl_long={b_c4['hl_long']:g}  hl_used={b_c4['hl_used']:g}  rank_by={b_c4['rank_by']}")
        ok_tr = abs(tr_long - 0.069) <= 0.003
        ok_va = abs(va_long - 0.133) <= 0.005
        if not (ok_tr and ok_va):
            raise SystemExit(f"[自检失败 -- 标红] c4_nodemean_out 复现不上 S1_chain: "
                              f"train {tr_long * 100:+.2f}%(差 {abs(tr_long - 0.069) * 100:.2f}pp,容差0.3pp) "
                              f"valid {va_long * 100:+.2f}%(差 {abs(va_long - 0.133) * 100:.2f}pp,容差0.5pp)")
        print("[自检] 通过 -- 方向/半衰期/选腿/标签四件事都和主表同口径\n")

        sig_vbase = st.signal(p_vbase)
        sig_c4 = st.signal(p_c4)
        sig_m1 = st.signal(p_m1)
        sig_n2 = st.signal(p_n2)
        sig_kf30 = st.signal(p_kf30)
        sig_kf9 = st.signal(p_kf9)
        sig_dvol20 = st.signal(p_dvol20)
        print(f"选到的方向(sign):vbase={st.sign(p_vbase):+.0f}  c4={st.sign(p_c4):+.0f}  m1={st.sign(p_m1):+.0f}"
              f"  n2={st.sign(p_n2):+.0f}  kf30={st.sign(p_kf30):+.0f}  kf9={st.sign(p_kf9):+.0f}"
              f"  ctl_dvol20={st.sign(p_dvol20):+.0f}", flush=True)

        valid_count_vbase = np.isfinite(p_vbase).sum(1)
        tr_idx = sampled_rows(tr_sl, valid_count_vbase)
        va_idx = sampled_rows(va_sl, valid_count_vbase)
        print(f"抽样:train 全长 {tr_sl.stop - tr_sl.start} 天中取 {tr_idx.size} 天;"
              f"valid 全长 {va_sl.stop - va_sl.start} 天中取 {va_idx.size} 天", flush=True)

        # ---------------------------------------------------------- 区块 1 (H12)
        try:
            hdr("区块 1 -- H12:低 G 端被 v_base 排到哪里去了(分类口径见下)")
            print("口径:(a)(b) 按 v_base 的 sig 十分档 x G 面板的截面十分档联合分类;"
                  "(c) 的'全市场' = 当天有标签(不论有没有信号)的全部股票。")
            lab_vbase_tr, _ = decile_matrix(sig_vbase[tr_idx])
            lab_vbase_va, _ = decile_matrix(sig_vbase[va_idx])
            lab_G_tr, cnt_G_tr = decile_matrix(p_G[tr_idx])
            lab_G_va, cnt_G_va = decile_matrix(p_G[va_idx])
            pctG_tr = pct_matrix(p_G[tr_idx])
            pctG_va = pct_matrix(p_G[va_idx])

            def block1_for_split(name, idx, lab_vb, lab_g, pct_g, cnt_g):
                per_day_by_decile = {d: [] for d in range(1, 11)}
                pool_counts = {1: np.zeros(10), 10: np.zeros(10)}
                pool_vbdec = {1: [], 10: []}
                excess = {1: [], 10: []}
                for i, t in enumerate(idx):
                    vb_row, g_row, pg_row = lab_vb[i], lab_g[i], pct_g[i]
                    if cnt_g[i] < MIN_NAMES:
                        continue
                    fin_vb = np.isfinite(vb_row) & np.isfinite(g_row)
                    if fin_vb.sum() < MIN_NAMES:
                        continue
                    for d in range(1, 11):
                        sel = fin_vb & (vb_row == d)
                        if sel.any():
                            per_day_by_decile[d].append(float(np.nanmedian(pg_row[sel])))
                    tgt_row = tgt[t]
                    uni = np.isfinite(tgt_row)
                    ew = float(np.nanmean(tgt_row[uni])) if uni.any() else float("nan")
                    for gd in (1, 10):
                        sel_g = fin_vb & (g_row == gd)
                        if sel_g.any():
                            vb_of_sel = vb_row[sel_g]
                            for d in range(1, 11):
                                pool_counts[gd][d - 1] += float((vb_of_sel == d).sum())
                            pool_vbdec[gd].extend(vb_of_sel.tolist())
                            sel_g_lbl = sel_g & uni
                            if sel_g_lbl.any() and np.isfinite(ew):
                                excess[gd].append(float(np.nanmean(tgt_row[sel_g_lbl])) - ew)
                print(f"\n[{name}] (a) v_base 各档(1..10,10=多头端)成员的 G 截面分位中位数:")
                print("   " + "  ".join(f"{med(per_day_by_decile[d]):.3f}" for d in range(1, 11)))
                for gd in (1, 10):
                    tot = pool_counts[gd].sum()
                    frac = pool_counts[gd] / tot if tot > 0 else pool_counts[gd]
                    print(f"[{name}] (b) G 档{gd:>2} 成员落在 v_base 各档(1..10)的占比"
                          f"(池化,共{int(tot)}个名额-天):")
                    print("   " + "  ".join(f"{x:.3f}" for x in frac) +
                          f"   v_base 档位中位数={med(pool_vbdec[gd]):.2f}")
                for gd in (1, 10):
                    print(f"[{name}] (c) G 档{gd:>2} 成员等权标签减全市场等权标签,年化 = "
                          f"{ann_pct(excess[gd]):+.2f}%  (抽样日数={len(excess[gd])})")

            block1_for_split("train", tr_idx, lab_vbase_tr, lab_G_tr, pctG_tr, cnt_G_tr)
            block1_for_split("valid", va_idx, lab_vbase_va, lab_G_va, pctG_va, cnt_G_va)
        except Exception as exc:
            print(f"[BLOCK 1 FAILED] {type(exc).__name__}: {exc}", flush=True)

        # ---------------------------------------------------------- 区块 2
        try:
            hdr("区块 2 -- 候选多头腿的已知暴露剖面(每个面板用它自己的长腿)")
            panels2 = {"c4": sig_c4, "m1": sig_m1, "n2": sig_n2, "kf_mean30": sig_kf30}
            order_panels = ["c4", "m1", "n2", "kf_mean30"]
            ctl_panels = {}
            for name in CONTROL_NAMES_10:
                try:
                    ctl_panels[name] = np.asarray(st.control(name), dtype=np.float64)
                except Exception as exc:
                    print(f"  控制变量 {name} 取不到: {type(exc).__name__}: {exc}")

            def legs_of(sig, idx):
                return [pick_legs(sig[t], top_frac) for t in idx]

            legs_by_panel = {name: {"train": legs_of(sig, tr_idx), "valid": legs_of(sig, va_idx)}
                              for name, sig in panels2.items()}

            def ctl_long_median_pct(cp, idx, legs):
                sub_pct = pct_matrix(cp[idx])
                vals = []
                for j in range(len(idx)):
                    lmask, smask, n, k, order = legs[j]
                    if n < MIN_NAMES or lmask.sum() == 0:
                        continue
                    v = sub_pct[j][lmask]
                    v = v[np.isfinite(v)]
                    if v.size:
                        vals.append(float(np.median(v)))
                return med(vals)

            print(f"\n{'控制变量':<22}{'c4_tr':>8}{'c4_va':>8}{'m1_tr':>8}{'m1_va':>8}"
                  f"{'n2_tr':>8}{'n2_va':>8}{'kf30_tr':>9}{'kf30_va':>9}")
            for cname, cp in ctl_panels.items():
                row_vals = []
                for p in order_panels:
                    row_vals.append(ctl_long_median_pct(cp, tr_idx, legs_by_panel[p]["train"]))
                    row_vals.append(ctl_long_median_pct(cp, va_idx, legs_by_panel[p]["valid"]))
                print(f"{cname:<22}" + "".join(f"{v:8.3f}" for v in row_vals[:6]) +
                      "".join(f"{v:9.3f}" for v in row_vals[6:]))
            print("(全市场基准 = 0.50;只算多头腿,省时间)")
        except Exception as exc:
            print(f"[BLOCK 2 FAILED] {type(exc).__name__}: {exc}", flush=True)

        # ---------------------------------------------------------- 区块 3
        try:
            hdr("区块 3 -- 多头腿(与空头腿)重合率(随机基准约 0.10)")
            pairs = [("c4", sig_c4, "kf30", sig_kf30), ("c4", sig_c4, "kf9", sig_kf9),
                     ("c4", sig_c4, "dvol20", sig_dvol20), ("m1", sig_m1, "kf30", sig_kf30),
                     ("n2", sig_n2, "kf30", sig_kf30)]
            for na, siga, nb, sigb in pairs:
                for split_name, idx in (("train", tr_idx), ("valid", va_idx)):
                    ovl_l, ovl_s = [], []
                    for t in idx:
                        la, sa, n_a, k_a, _ = pick_legs(siga[t], top_frac)
                        lb, sb, n_b, k_b, _ = pick_legs(sigb[t], top_frac)
                        if n_a < MIN_NAMES or n_b < MIN_NAMES:
                            continue
                        ovl_l.append(float((la & lb).sum()) / max(int(la.sum()), 1))
                        ovl_s.append(float((sa & sb).sum()) / max(int(sa.sum()), 1))
                    print(f"  ({na},{nb})[{split_name}] 多头腿重合率中位数={med(ovl_l):.3f}"
                          f"  空头腿重合率中位数={med(ovl_s):.3f}")
        except Exception as exc:
            print(f"[BLOCK 3 FAILED] {type(exc).__name__}: {exc}", flush=True)

        # ---------------------------------------------------------- 区块 4
        try:
            hdr("区块 4 -- 增量①:对已知家族中性化之后的残差(sign 固定 +1.0)")
            scope = slice(tr_sl.start, ut_sl.stop)

            def full_from_scope(resid_scope, total_len):
                out = np.full((total_len, resid_scope.shape[1]), np.nan)
                out[scope] = resid_scope
                return out

            y_z = dg._zrank(sig_c4[scope])
            ctl_z = {"kf30": dg._zrank(sig_kf30[scope]), "kf9": dg._zrank(sig_kf9[scope])}
            resid_c4_s, info_c4 = dg.neutralise(y_z, ctl_z, panel_ready=True, controls_ready=True)
            resid_c4_full = full_from_scope(resid_c4_s, sig_c4.shape[0])
            b_resid_c4 = st.books(resid_c4_full, fit="train", evals=("train", "valid"), sign=1.0)
            print(f"[c4 对 kf30+kf9 中性化] R2(fit段,rank空间)={info_c4['mean_r2']:.3f}  天数={info_c4['days']}"
                  f"  书用的半衰期 hl_used={b_resid_c4['hl_used']:g}(对残差重新拟合的,不是 c4 自己的)")
            for sp in ("train", "valid"):
                row = b_resid_c4["splits"][sp]
                ic = st.ic(resid_c4_full, sp, sign=1.0)
                print(f"  [{sp}] Lnet={row['long_ann'] * 100:+.2f}%  Lshp={row['long_sharpe']:+.2f}"
                      f"  Lgross={row['long_gross_ann'] * 100:+.2f}%  LTO={row['long_turnover'] * 100:.1f}%"
                      f"  rank_ic={ic['rank_ic']:+.4f}")

            y_z2 = dg._zrank(sig_kf30[scope])
            ctl_z2 = {"c4": dg._zrank(sig_c4[scope])}
            resid_kf30_s, info_kf30 = dg.neutralise(y_z2, ctl_z2, panel_ready=True, controls_ready=True)
            resid_kf30_full = full_from_scope(resid_kf30_s, sig_kf30.shape[0])
            b_resid_kf30 = st.books(resid_kf30_full, fit="train", evals=("train", "valid"), sign=1.0)
            print(f"\n[kf30 对 c4 中性化(反向)] R2(fit段,rank空间)={info_kf30['mean_r2']:.3f}"
                  f"  天数={info_kf30['days']}  hl_used={b_resid_kf30['hl_used']:g}")
            for sp in ("train", "valid"):
                row = b_resid_kf30["splits"][sp]
                ic = st.ic(resid_kf30_full, sp, sign=1.0)
                print(f"  [{sp}] Lnet={row['long_ann'] * 100:+.2f}%  Lshp={row['long_sharpe']:+.2f}"
                      f"  Lgross={row['long_gross_ann'] * 100:+.2f}%  LTO={row['long_turnover'] * 100:.1f}%"
                      f"  rank_ic={ic['rank_ic']:+.4f}")
            print("\n(注:这里的 hl_used 是 st.books 对残差本身重新拟合的半衰期,区块6/主表的 neutralise\n"
                  " 诊断用的是不重新平滑的 book_row —— 两种残差口径不是一回事,见文件头说明。)")
        except Exception as exc:
            print(f"[BLOCK 4 FAILED] {type(exc).__name__}: {exc}", flush=True)

        # ---------------------------------------------------------- 区块 5
        try:
            hdr("区块 5 -- 增量②:多头腿名单的收益分解(c4 vs kf30)")
            legs_c4_tr = [pick_legs(sig_c4[t], top_frac) for t in tr_idx]
            legs_c4_va = [pick_legs(sig_c4[t], top_frac) for t in va_idx]
            legs_kf30_tr = [pick_legs(sig_kf30[t], top_frac) for t in tr_idx]
            legs_kf30_va = [pick_legs(sig_kf30[t], top_frac) for t in va_idx]

            def decomp(idx, legs_a, legs_b):
                groups = {"only_c4": {"n": [], "ex": []}, "only_kf30": {"n": [], "ex": []},
                          "both": {"n": [], "ex": []}}
                for j, t in enumerate(idx):
                    la, _, na_, _, _ = legs_a[j]
                    lb, _, nb_, _, _ = legs_b[j]
                    if na_ < MIN_NAMES or nb_ < MIN_NAMES:
                        continue
                    tgt_row = tgt[t]
                    uni = np.isfinite(tgt_row)
                    if not uni.any():
                        continue
                    ew = float(np.nanmean(tgt_row[uni]))
                    only_c4 = la & ~lb
                    only_kf = lb & ~la
                    both = la & lb
                    for key, mask in (("only_c4", only_c4), ("only_kf30", only_kf), ("both", both)):
                        sel = mask & uni
                        groups[key]["n"].append(int(mask.sum()))
                        if sel.any():
                            groups[key]["ex"].append(float(np.nanmean(tgt_row[sel])) - ew)
                return groups

            for split_name, idx, la_, lb_ in (("train", tr_idx, legs_c4_tr, legs_kf30_tr),
                                               ("valid", va_idx, legs_c4_va, legs_kf30_va)):
                g = decomp(idx, la_, lb_)
                print(f"\n[{split_name}]")
                for key in ("only_c4", "only_kf30", "both"):
                    ex = np.asarray(g[key]["ex"], dtype=np.float64)
                    ex = ex[np.isfinite(ex)]
                    med_ann = float(np.median(ex) * 252 * 100) if ex.size else float("nan")
                    mean_ann = ann_pct(ex)
                    print(f"  {key:<10} 股票数中位数={med(g[key]['n']):.1f}   "
                          f"超额年化 中位数={med_ann:+.2f}%  均值={mean_ann:+.2f}%   (抽样日数={ex.size})")
        except Exception as exc:
            print(f"[BLOCK 5 FAILED] {type(exc).__name__}: {exc}", flush=True)

        # ---------------------------------------------------------- 区块 6(补充,见文件头说明)
        try:
            hdr("区块 6(补充,非工单原文区块) -- c4_nodemean_out 对 9 个通用控制变量的中性化")
            ctl9 = {}
            for name in CONTROL_NAMES_9:
                try:
                    ctl9[name] = np.asarray(st.control(name), dtype=np.float64)
                except Exception as exc:
                    print(f"  控制变量 {name} 取不到: {type(exc).__name__}: {exc}")
            tr = tr_sl
            ctl_z9 = {k: dg._zrank(v[tr]) for k, v in ctl9.items()}
            y_z9 = dg._zrank(sig_c4[tr])
            base_ic = dg.ic_row(sig_c4[tr], tgt[tr], sign=1.0)
            b0 = b_c4["splits"]["train"]
            print(f"  (未中性化)        rIC={base_ic['rank_ic']:+.4f}  Lgross={b0['long_gross_ann'] * 100:+.1f}%"
                  f"  Lnet={b0['long_ann'] * 100:+.1f}%  short={b0['short_gross_ann'] * 100:+.1f}%"
                  f"  LSgross={b0['ls_gross_sharpe']:+.2f}  LS={b0['ls_sharpe']:+.2f}"
                  f"  TO={b0['long_turnover'] * 100:.1f}%")
            resid_all, info_all = dg.neutralise(y_z9, ctl_z9, panel_ready=True, controls_ready=True)
            row_all = resid_row(resid_all, info_all, tgt[tr], cost, top_frac)
            raw_z9 = dg._zrank(np.asarray(p_c4[tr], dtype=np.float64))
            r2_raw = dg.neutralise(raw_z9, ctl_z9, panel_ready=True, controls_ready=True)[1]["mean_r2"]
            print(f"  all_controls  R2={row_all['r2']:.3f}(原始面板R2={r2_raw:.3f})  残差rIC={row_all['rank_ic']:+.4f}"
                  f"  Lgross={row_all['long_gross_ann'] * 100:+.1f}%  Lnet={row_all['long_ann'] * 100:+.1f}%"
                  f"  short={row_all['short_gross_ann'] * 100:+.1f}%  LSgross={row_all['ls_gross_sharpe']:+.2f}"
                  f"  LS={row_all['ls_sharpe']:+.2f}  TO={row_all['long_turnover'] * 100:.1f}%"
                  f"  (回归天数={info_all['days']})")
            for name in CONTROL_NAMES_9:
                if name not in ctl_z9:
                    continue
                resid1, info1 = dg.neutralise(y_z9, {name: ctl_z9[name]}, panel_ready=True, controls_ready=True)
                row1 = resid_row(resid1, info1, tgt[tr], cost, top_frac)
                print(f"  {name:<14} R2={row1['r2']:.3f}  残差rIC={row1['rank_ic']:+.4f}"
                      f"  Lgross={row1['long_gross_ann'] * 100:+.1f}%  Lnet={row1['long_ann'] * 100:+.1f}%"
                      f"  short={row1['short_gross_ann'] * 100:+.1f}%  LSgross={row1['ls_gross_sharpe']:+.2f}"
                      f"  LS={row1['ls_sharpe']:+.2f}  TO={row1['long_turnover'] * 100:.1f}%")
            print("  (口径与 (A) 里 kf_mean30 那张中性化表一致;dg.neutralise 的 n<50 门槛比工单给区块4\n"
                  "   定的 n<30 更严,见文件头说明,可以和 kf_mean30 的数字并排比较)")
        except Exception as exc:
            print(f"[BLOCK 6 FAILED] {type(exc).__name__}: {exc}", flush=True)

        # ---------------------------------------------------------- 区块 7(补充,见文件头说明)
        try:
            hdr("区块 7(补充,非工单原文区块) -- c4_nodemean_out 逐年 Lnet/LS")
            years = _years_of(st)
            scope = slice(tr_sl.start, ut_sl.stop)
            for yr in sorted(set(years[scope].tolist())):
                idx_y = np.nonzero(years == yr)[0]
                idx_y = idx_y[(idx_y >= scope.start) & (idx_y < scope.stop)]
                if idx_y.size < 20:
                    continue
                row = bk.book_row(sig_c4, tgt, slice(int(idx_y[0]), int(idx_y[-1]) + 1), cost, top_frac)
                print(f"  {int(yr)}  天数={idx_y.size:<4}  Lnet={row['long_ann'] * 100:+.1f}%"
                      f"  LS={row['ls_sharpe']:+.2f}")
        except Exception as exc:
            print(f"[BLOCK 7 FAILED] {type(exc).__name__}: {exc}", flush=True)

    print("\n[x2_increment done]", flush=True)


if __name__ == "__main__":
    main()
