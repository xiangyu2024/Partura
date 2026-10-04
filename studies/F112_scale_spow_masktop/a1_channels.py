"""A1_channels — R1 工单第 2 件。五个小节(§1~§5)各自 try/except,互不拖累。
附加一节(非工单原文,见结果卡"做了什么"):原始日频面板口径的 rank 相关,补工单"要带回来的数字"第 3 项
(标准 diagnostics 只给交易信号口径一套矩阵,这一套没有现成工具,这里用 Study.rank_corr 在原始面板上补。)

脚本开头先用小规模已知答案自检 rolling-sum / mask-replace 两个手写算子,再进 Study 用真实面板跑五节。
"""
import math
import sys
import traceback

import numpy as np


# ------------------------------------------------------------------ 手写算子(纯 numpy,自检用,也是五节共用的管线)

def rolling_nansum_causal(x: np.ndarray, window: int) -> np.ndarray:
    """逐列(股票)因果滚动 nansum:第 t 行 = sum(x[max(0,t-window+1):t+1]),NaN 当 0。"""
    filled = np.where(np.isfinite(x), x, 0.0)
    cums = np.cumsum(filled, axis=0)
    out = cums.copy()
    if window < cums.shape[0]:
        out[window:] -= cums[:-window]
    return out


def rolling_count_causal(finite_mask: np.ndarray, window: int) -> np.ndarray:
    m = finite_mask.astype(np.float64)
    cums = np.cumsum(m, axis=0)
    out = cums.copy()
    if window < cums.shape[0]:
        out[window:] -= cums[:-window]
    return out


def rolling_mean_causal(x: np.ndarray, window: int) -> np.ndarray:
    s = rolling_nansum_causal(x, window)
    c = rolling_count_causal(np.isfinite(x), window)
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.where(c > 0, s / c, np.nan)


def ts_scale_like(E: np.ndarray, window: int, eps: float) -> np.ndarray:
    denom = rolling_nansum_causal(E, window)
    denom_g = np.where(np.abs(denom) < eps, 1.0, denom)
    return E / denom_g


def mask_replace_lowest(C: np.ndarray, topn_fn):
    """逐日:把有效值里最低的 topn_fn(count) 只换成当天全部有效值的均值。返回 (D, replaced_mask)。
    并列:np.argsort(..., kind='stable') 对升序排列后、值相等的元素按它们在 `vals` 里的原始顺序(=按股票在
    面板里的列序排列,因为 idx_valid 已经是按列序升序取出的)决定先后,与源码里两次 stable argsort 打破并列
    的方式语义一致(都是"按原始位置顺序"),但不是同一段实现,这里只保证"语义一致"不保证逐位复现并列边界。
    """
    T, N = C.shape
    D = C.copy()
    replaced = np.zeros((T, N), dtype=bool)
    for t in range(T):
        row = C[t]
        valid = np.isfinite(row)
        cnt = int(valid.sum())
        if cnt == 0:
            continue
        n_top = int(topn_fn(cnt))
        n_top = max(0, min(n_top, cnt))
        if n_top == 0:
            continue
        idx_valid = np.flatnonzero(valid)
        vals = row[idx_valid]
        order = np.argsort(vals, kind="stable")
        lo_idx = idx_valid[order[:n_top]]
        m = float(vals.mean())
        D[t, lo_idx] = m
        replaced[t, lo_idx] = True
    return D, replaced


def reconstruct_F(C: np.ndarray, topn_fn, window: int, eps: float):
    D, replaced = mask_replace_lowest(C, topn_fn)
    E = np.sign(D) * D ** 2
    F = ts_scale_like(E, window, eps)
    return F, D, replaced, E


def self_check() -> bool:
    ok = True
    try:
        # rolling_nansum_causal,含 NaN,window=2,对照手算
        x = np.array([[1.0, np.nan], [3.0, 4.0], [np.nan, 6.0], [7.0, 8.0]])
        got = rolling_nansum_causal(x, 2)
        want = np.array([[1.0, 0.0], [4.0, 4.0], [3.0, 10.0], [7.0, 14.0]])
        assert np.allclose(got, want), f"rolling_nansum_causal 不对:\n{got}\nvs\n{want}"

        # EPS 分母保护:窗口和≈0 时退化成 E 本身
        E = np.array([[5.0], [-5.0]])
        got2 = ts_scale_like(E, 2, 1e-6)
        assert np.isclose(got2[1, 0], -5.0), f"EPS 保护分支不对:{got2[1,0]} 应为 -5.0"

        # mask_replace_lowest:4 个有效值,top_ratio=0.1 -> n_top=ceil(0.4)=1,换成最低的那个
        row = np.array([[10.0, 20.0, 30.0, np.nan, 5.0]])
        D, rep = mask_replace_lowest(row, lambda cnt: math.ceil(cnt * 0.1))
        assert np.isnan(D[0, 3]), "NaN 位应保持 NaN"
        assert np.isclose(D[0, 4], 16.25), f"最低值应被替换成均值 16.25,实际 {D[0,4]}"
        assert D[0, 0] == 10.0 and D[0, 1] == 20.0 and D[0, 2] == 30.0, "其余值应原样保留"
        assert rep[0, 4] and not rep[0, 0], "replaced 掩码不对"

        # 随机数组过一遍形状/NaN,确保不崩
        rng = np.random.default_rng(0)
        R = rng.normal(size=(40, 15)).astype(np.float64)
        R[rng.random(R.shape) < 0.15] = np.nan
        R[3, :] = np.nan  # 整天 NaN
        Fr, Dr, repr_, Er = reconstruct_F(R, lambda cnt: math.ceil(cnt * 0.1), 10, 1e-12)
        assert Fr.shape == R.shape
        assert np.isnan(Fr[3]).all(), "全天 NaN 的那一天,F 应该全 NaN"
        print("[self-check] 全部断言通过(rolling_nansum_causal / EPS 保护 / mask_replace_lowest / 随机数组形状)")
    except AssertionError as exc:
        ok = False
        print(f"[self-check] 失败:{exc}")
        traceback.print_exc()
    except Exception:
        ok = False
        print("[self-check] 跑的时候报了别的异常:")
        traceback.print_exc()
    return ok


def cross_sectional_skew(x: np.ndarray) -> np.ndarray:
    xm = x - np.nanmean(x, axis=1, keepdims=True)
    var = np.nanmean(xm ** 2, axis=1)
    m3 = np.nanmean(xm ** 3, axis=1)
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.where(var > 0, m3 / np.power(var, 1.5), np.nan)


def bucket_index(gate: np.ndarray, dg, buckets: int = 5) -> np.ndarray:
    """与 partura.diagnose.conditional_ic 同一套分桶算法(rank_rows 后按比例切),纯复用,不是新设计。"""
    rg = dg.rank_rows(np.asarray(gate, dtype=np.float64))
    n = np.isfinite(rg).sum(axis=1, keepdims=True)
    with np.errstate(invalid="ignore"):
        b = np.floor((rg - 1.0) / np.maximum(n, 1) * buckets)
    return b


def daily_spearman_mean(dg, x: np.ndarray, y: np.ndarray, sl) -> float:
    daily = dg.cs_pearson(dg.rank_rows(np.asarray(x, dtype=np.float64)),
                          dg.rank_rows(np.asarray(y, dtype=np.float64)))
    return float(dg.nanmean_quiet(daily[sl]))


def section(name: str) -> None:
    print(f"\n=== {name} ===", flush=True)


def main() -> None:
    print("[a1_channels] 脚本启动,先自检")
    self_check()

    from partura.study_tools import Study, bk, dg  # noqa: F401  (bk 目前没直接用到,留着跟 playbook 示例一致)

    FID = "F112_scale_spow_masktop"
    with Study(FID) as st:
        P = st.panels({
            "F": "ts_scale(signedpower(cs_mask_top_replace_mean_neg(add(day_quantile(Close), day_kurt(High)))), 30)",
            "C": "add(day_quantile(Close), day_kurt(High))",
            "A": "day_quantile(Close)",
            "B": "day_kurt(High)",
            "Fn": "ts_scale(cs_mask_top_replace_mean_neg(add(day_quantile(Close), day_kurt(High))), 30)",
        })
        tr = st.slice("train")
        C = np.asarray(P["C"], dtype=np.float64)
        A = np.asarray(P["A"], dtype=np.float64)
        B = np.asarray(P["B"], dtype=np.float64)
        Fe = np.asarray(P["F"], dtype=np.float64)

        shared = {}  # 跨小节传递重建结果,§3/§4 不要求 §1 自检通过也能用

        # =========================================================== §1
        section("§1 重建 + 自检(是 §2 §5 的前置闸门)")
        s1_selfcheck_pass = False
        try:
            eps_used = 1e-12
            F_rec, D, replaced, E = reconstruct_F(C, lambda cnt: math.ceil(cnt * 0.1), 30, eps_used)
            daily = dg.cs_pearson(dg.rank_rows(F_rec), dg.rank_rows(Fe))
            m_tr = float(dg.nanmean_quiet(daily[tr]))
            min_tr = float(np.nanmin(daily[tr]))
            rel = np.abs(F_rec[tr] - Fe[tr]) / (np.abs(Fe[tr]) + 1e-12)
            rel_fin = rel[np.isfinite(rel)]
            med_rel = float(np.median(rel_fin)) if rel_fin.size else float("nan")
            p99_rel = float(np.percentile(rel_fin, 99)) if rel_fin.size else float("nan")
            print(f"EPS={eps_used}: spearman(F_rec,F) train 均值={m_tr:.5f}  最小值={min_tr:.5f}  "
                  f"相对误差中位数={med_rel:.3e}  99分位={p99_rel:.3e}")
            if m_tr < 0.999:
                eps_used = 1e-8
                F_rec, D, replaced, E = reconstruct_F(C, lambda cnt: math.ceil(cnt * 0.1), 30, eps_used)
                daily = dg.cs_pearson(dg.rank_rows(F_rec), dg.rank_rows(Fe))
                m_tr = float(dg.nanmean_quiet(daily[tr]))
                min_tr = float(np.nanmin(daily[tr]))
                rel = np.abs(F_rec[tr] - Fe[tr]) / (np.abs(Fe[tr]) + 1e-12)
                rel_fin = rel[np.isfinite(rel)]
                med_rel = float(np.median(rel_fin)) if rel_fin.size else float("nan")
                p99_rel = float(np.percentile(rel_fin, 99)) if rel_fin.size else float("nan")
                print(f"EPS={eps_used}(改用 1e-8 重试): spearman 均值={m_tr:.5f}  最小值={min_tr:.5f}  "
                      f"相对误差中位数={med_rel:.3e}  99分位={p99_rel:.3e}")
            s1_selfcheck_pass = m_tr >= 0.999
            shared.update(D=D, replaced=replaced, E=E, F_rec=F_rec, eps_used=eps_used)
            print(f"自检{'通过' if s1_selfcheck_pass else '没过(<0.999)'}")
            if not s1_selfcheck_pass:
                print("§1 自检失败,§2/§5 跳过(按工单授权);§3/§4 不依赖重建数值精度,照跑。")
        except Exception:
            print("§1 抛了异常,整节失败;§2/§5 因为依赖它的产物,这两节也跳过;§3/§4 继续:")
            traceback.print_exc()

        # =========================================================== §2
        section("§2 公布值的出入(H9,优先级最低)")
        if not s1_selfcheck_pass:
            print("§1 自检没过,按工单规定跳过 §2")
        else:
            try:
                D0, replaced0 = shared["D"], shared["replaced"]
                eps_used = shared["eps_used"]
                F_rec = shared["F_rec"]

                def round_fn(cnt):
                    return round(cnt * 0.1)  # python round,银行家取整(.5 入偶)

                R_, _, _, _ = reconstruct_F(C, round_fn, 30, eps_used)
                W_ = F_rec.copy()
                finite = np.isfinite(W_)
                for j in range(W_.shape[1]):
                    idx = np.flatnonzero(finite[:, j])[:29]
                    W_[idx, j] = np.nan

                us = st.slice("utrain")

                def ls_lgross(panel):
                    b = st.books(panel, fit="utrain", evals=("utrain",))
                    ls = b["by_rank"]["ls"]["splits"]["utrain"]["ls_sharpe"]
                    lg = b["by_rank"]["long"]["splits"]["utrain"]["long_gross_ann"]
                    return ls, lg

                for name, panel in (("F_rec(ceil,§1 重建)", F_rec), ("R(round 版)", R_), ("W(前29天置NaN版)", W_)):
                    ls, lg = ls_lgross(panel)
                    print(f"  {name}: utrain LS={ls:+.2f}  Lgross={lg:+.1%}")

                pub = st.cfg.get("published", {})
                print(f"  对照:Partura v_base utrain LS +2.59/Lgross +9.1%;用户公布 "
                      f"LS {pub.get('ls', ['?'])[0]}/Lgross {pub.get('long', ['?'])[0]}")

                cnt = np.isfinite(C[tr]).sum(axis=1)
                n_ceil = np.ceil(cnt * 0.1)
                n_round = np.round(cnt * 0.1)  # numpy round 同样是银行家取整(.5 入偶),与 python round 一致
                days_with_names = cnt > 0
                diff_days = (n_ceil != n_round) & days_with_names
                frac_diff_days = float(diff_days.mean()) if days_with_names.any() else float("nan")
                mean_abs_diff = float(np.abs(n_ceil - n_round)[days_with_names].mean()) if days_with_names.any() else float("nan")
                print(f"  ceil 与 round 取值不同的交易日占比(train)={frac_diff_days:.1%};"
                      f"不同时平均相差 {mean_abs_diff:.2f} 只股票")
            except Exception:
                print("§2 抛了异常:")
                traceback.print_exc()

        # =========================================================== §3
        section("§3 封板票与质点(H5 + H4)")
        try:
            sig = st.signal(Fe)  # 方向 x hl20(长腿最优半衰期) EMA 之后的交易信号,全长
            tgt = st.target()
            raw = st.target(buyable=False)

            from alphacube.metrics import long_short_weights  # 与 books.py 内部用的是同一个函数
            w = long_short_weights(sig, float(st.cfg.get("top_frac", 0.10)))
            long_mask = w > 0
            short_mask = w < 0

            def leg_report(label_panel, label_name):
                lp = np.asarray(label_panel, dtype=np.float64)
                ok_all = np.isfinite(sig) & np.isfinite(lp)
                ew_num = np.where(ok_all, lp, 0.0).sum(axis=1)
                ew_cnt = ok_all.sum(axis=1)
                with np.errstate(invalid="ignore", divide="ignore"):
                    ew = np.where(ew_cnt > 0, ew_num / np.maximum(ew_cnt, 1), np.nan)
                for leg_name, mask in (("多头十分位", long_mask), ("空头十分位", short_mask)):
                    grp = np.where(mask, lp, np.nan)
                    with np.errstate(invalid="ignore"):
                        g_mean = np.nanmean(grp, axis=1)
                    m1 = float(np.nanmean(g_mean[tr])) * 252  # ① 组内等权收益,年化
                    m2 = float(np.nanmean((g_mean - ew)[tr])) * 252  # ② 组内等权收益 - 全市场有信号有标签等权收益,年化
                    print(f"  [{label_name}] {leg_name}: ①组内等权={m1:+.1%}  ②超额(减全市场有信号有标签等权)={m2:+.1%}")

            leg_report(tgt, "tgt(buyable=True,官方标签)")
            leg_report(raw, "raw(buyable=False,不剔除封板)")

            frac_nan_market = float(np.isnan(tgt[tr]).mean())
            frac_nan_long = float(np.isnan(tgt[tr])[long_mask[tr]].mean()) if long_mask[tr].any() else float("nan")
            frac_nan_short = float(np.isnan(tgt[tr])[short_mask[tr]].mean()) if short_mask[tr].any() else float("nan")
            frac_unbuyable_market = float((np.isfinite(raw[tr]) & np.isnan(tgt[tr])).mean())
            print(f"  tgt 为 NaN 的格子占比(train):全市场 {frac_nan_market:.2%}  多头十分位内 {frac_nan_long:.2%}  "
                  f"空头十分位内 {frac_nan_short:.2%}(其中「买不进」即 raw 有值但 tgt 为 NaN 的全市场占比 {frac_unbuyable_market:.2%})")

            if "replaced" in shared:
                replaced = shared["replaced"]
                n_names = np.isfinite(C).sum(axis=1)
                n_rep = replaced.sum(axis=1)
                frac_rep = np.where(n_names > 0, n_rep / np.maximum(n_names, 1), np.nan)
                print(f"  质点①每天被替换的股票数/占比(train 均值):{float(np.nanmean(n_rep[tr])):.1f} 只 / "
                      f"{float(np.nanmean(frac_rep[tr])):.2%}")

                roll30 = rolling_nansum_causal(replaced.astype(np.float64), 30)
                day_idx = np.arange(replaced.shape[0])
                persistent = (roll30 >= 29.999) & (day_idx[:, None] >= 29)
                n_persist_daily = persistent[tr].sum(axis=1)
                print(f"  质点②「过去 30 个交易日每天都被替换」的股票数(train 日均):{float(n_persist_daily.mean()):.2f} 只;"
                      f"train 期间**出现过**这种情况的不同股票数(去重):{int(persistent[tr].any(axis=0).sum())} 只")

                if n_persist_daily.sum() > 0:
                    Fv = Fe[tr]
                    pmask = persistent[tr]
                    r_full = dg.rank_rows(Fv)                       # 一次性批量排名,不逐天调用
                    fin_full = np.isfinite(Fv)
                    cnt_full = fin_full.sum(axis=1, keepdims=True)
                    with np.errstate(invalid="ignore", divide="ignore"):
                        rankpct = np.where(fin_full, (r_full - 1.0) / np.maximum(cnt_full - 1, 1), np.nan)
                    vals = rankpct[pmask]
                    vals = vals[np.isfinite(vals)]
                    if vals.size:
                        q = np.percentile(vals, [25, 50, 75])
                        print(f"  质点②这群股票当天 F 的横截面百分位:均值={float(vals.mean()):.3f}  "
                              f"四分位=[{q[0]:.3f}, {q[1]:.3f}, {q[2]:.3f}]  (0=当天最低,1=当天最高,n={vals.size})")
                else:
                    print("  质点②:train 里没有任何股票连续 30 天都被替换,跳过百分位统计")
            else:
                print("  §1 没跑出 D/replaced,质点①②跳过(与§1整体异常同源,见上)")

            max_ties = []
            for t in range(tr.start, tr.stop):
                row = Fe[t]
                row = row[np.isfinite(row)]
                if row.size == 0:
                    continue
                _, counts = np.unique(row, return_counts=True)
                max_ties.append(counts.max())
            if max_ties:
                max_ties = np.array(max_ties)
                print(f"  每天 F 完全相同的最大并列组(train):均值={max_ties.mean():.2f}  最大值={int(max_ties.max())}  "
                      f"(n_days={max_ties.size})")
        except Exception:
            print("§3 抛了异常:")
            traceback.print_exc()

        # =========================================================== §4
        section("§4 通道分解(H1 / H2 / H2b / H6)——最重要")
        try:
            mean30A = rolling_mean_causal(A, 30)
            mean30B = rolling_mean_causal(B, 30)
            mean30C = rolling_mean_causal(C, 30)
            devA = A - mean30A
            devB = B - mean30B
            with np.errstate(invalid="ignore", divide="ignore"):
                e = C / mean30C - 1.0
                termP = devA / mean30C
                termK = devB / mean30C

            sp_P = daily_spearman_mean(dg, Fe, termP, tr)
            sp_K = daily_spearman_mean(dg, Fe, termK, tr)
            sp_PK = daily_spearman_mean(dg, Fe, termP + termK, tr)
            sp_e = daily_spearman_mean(dg, Fe, e, tr)
            print(f"spearman(F,termP)={sp_P:+.3f}  spearman(F,termK)={sp_K:+.3f}  "
                  f"spearman(F,termP+termK)={sp_PK:+.3f}  spearman(F,e)={sp_e:+.3f}")

            std_P_daily = np.nanstd(termP, axis=1)
            std_K_daily = np.nanstd(termK, axis=1)
            med_std_P = float(np.median(std_P_daily[tr]))
            med_std_K = float(np.median(std_K_daily[tr]))
            print(f"幅度(train 中位数):std(termP)={med_std_P:.4g}  std(termK)={med_std_K:.4g}  "
                  f"比值 P/K={med_std_P / med_std_K if med_std_K else float('nan'):.2f}")

            lag1_meanA = np.full_like(mean30A, np.nan)
            lag1_meanA[1:] = mean30A[:-1]
            bidx = bucket_index(lag1_meanA, dg, 5)
            print("按滞后一日 mean30A 分 5 桶(train 均值;桶0=滞后价位最低):")
            for k in range(5):
                xk = np.where(bidx == k, Fe, np.nan)
                pk = np.where(bidx == k, termP, np.nan)
                kk = np.where(bidx == k, termK, np.nan)
                sp_pk = daily_spearman_mean(dg, xk, pk, tr)
                sp_kk = daily_spearman_mean(dg, xk, kk, tr)
                sdp = float(np.nanmedian(np.nanstd(pk, axis=1)[tr]))
                sdk = float(np.nanmedian(np.nanstd(kk, axis=1)[tr]))
                print(f"  桶{k}: spearman(F,termP)={sp_pk:+.3f}  spearman(F,termK)={sp_kk:+.3f}  "
                      f"std(termP)={sdp:.4g}  std(termK)={sdk:.4g}")

            skew_daily = cross_sectional_skew(e)
            skew_mean = float(np.nanmean(skew_daily[tr]))
            skew_med = float(np.nanmedian(skew_daily[tr]))
            e_tr = e[tr]
            e_fin = e_tr[np.isfinite(e_tr)]
            pq = np.percentile(e_fin, [1, 5, 50, 95, 99]) if e_fin.size else [float("nan")] * 5
            print(f"e 的横截面偏度(train):均值={skew_mean:+.3f}  中位数={skew_med:+.3f};"
                  f"e 分位(train 池化)1/5/50/95/99={pq[0]:.3f}/{pq[1]:.3f}/{pq[2]:.3f}/{pq[3]:.3f}/{pq[4]:.3f}")

            if "replaced" in shared:
                clean = ~shared["replaced"]
                Fc = np.where(clean, Fe, np.nan)
                Pc = np.where(clean, termP, np.nan)
                Kc = np.where(clean, termK, np.nan)
                sp_Pc = daily_spearman_mean(dg, Fc, Pc, tr)
                sp_Kc = daily_spearman_mean(dg, Fc, Kc, tr)
                print(f"排除被替换格子(D==C 的等价判据:用 §1 的 replaced 掩码取反,而不是逐位浮点比较)后:"
                      f"spearman(F,termP)={sp_Pc:+.3f}  spearman(F,termK)={sp_Kc:+.3f}")
            else:
                print("§1 没有产出 replaced 掩码,跳过「排除 mask 污染」这一步")
        except Exception:
            print("§4 抛了异常(本节最重要,已照规定专门告警):")
            traceback.print_exc()

        # =========================================================== §5
        section("§5 signedpower 的二阶项(H3)")
        if not s1_selfcheck_pass:
            print("§1 自检没过,按工单规定跳过 §5")
        else:
            try:
                Fn = np.asarray(P["Fn"], dtype=np.float64)
                sp_FFn = daily_spearman_mean(dg, Fe, Fn, tr)
                print(f"spearman(F,Fn)={sp_FFn:+.4f}  (H3 的直接判据,阈值 0.9)")

                mean30C = rolling_mean_causal(C, 30)
                with np.errstate(invalid="ignore", divide="ignore"):
                    e = C / mean30C - 1.0
                m2 = rolling_mean_causal(e ** 2, 30)
                delta = Fe - 2.0 * Fn
                target_term = e ** 2 - m2
                sp_delta = daily_spearman_mean(dg, delta, target_term, tr)
                print(f"spearman(Δ, e²−m2)={sp_delta:+.4f}  (Δ=F−2·Fn,代数上应接近 (1/30)(e²−m2)−1/30 这个折叠通道)")

                mean30C2 = rolling_mean_causal(C ** 2, 30)
                var_c = np.maximum(mean30C2 - mean30C ** 2, 0.0)
                disp = np.sqrt(var_c) / mean30C
                sig = st.signal(Fe)
                rc_disp = st.rank_corr(sig, disp, "train")
                rc_known = st.rank_corr(sig, st.control("known_stdamt_mean30"), "train")
                print(f"rank_corr(sig, disp)={rc_disp:+.3f}  rank_corr(sig, known_stdamt_mean30)={rc_known:+.3f}")
            except Exception:
                print("§5 抛了异常:")
                traceback.print_exc()

        # =========================================================== 附:原始日频面板口径 rank 相关(补要带回数字 #3)
        section("附:S1_minimal 10 变体 与 v_base / 5 个参照的原始日频面板口径 rank 相关")
        try:
            variant_exprs = {
                "s1_noK": "ts_scale(signedpower(cs_mask_top_replace_mean_neg(day_quantile(Close))), 30)",
                "s1_noP": "ts_scale(signedpower(cs_mask_top_replace_mean_neg(day_kurt(High))), 30)",
                "s1_noMask": "ts_scale(signedpower(add(day_quantile(Close), day_kurt(High))), 30)",
                "s1_noSpow": "ts_scale(cs_mask_top_replace_mean_neg(add(day_quantile(Close), day_kurt(High))), 30)",
                "s1_plain30": "ts_scale(day_quantile(Close), 30)",
                "s1_w10": "ts_scale(signedpower(cs_mask_top_replace_mean_neg(add(day_quantile(Close), day_kurt(High)))), 10)",
                "s1_x30": "cross_scale(signedpower(cs_mask_top_replace_mean_neg(add(day_quantile(Close), day_kurt(High)))), 30)",
                "s1_x60": "cross_scale(signedpower(cs_mask_top_replace_mean_neg(add(day_quantile(Close), day_kurt(High)))), 60)",
                "s1_x241": "cross_scale(signedpower(cs_mask_top_replace_mean_neg(add(day_quantile(Close), day_kurt(High)))), 241)",
                "s1_plain60": "cross_scale(day_quantile(Close), 60)",
            }
            VP = st.panels(variant_exprs)
            refs = {
                "v_base": Fe,
                "ctl_mom20": st.control("ctl_mom20"),
                "ctl_price": st.control("ctl_price"),
                "known_stdamt_mean30": st.control("known_stdamt_mean30"),
                "known_stdamt_max9": st.control("known_stdamt_max9"),
                "known_amt_max9": st.control("known_amt_max9"),
            }
            ranked_refs = {k: dg.rank_rows(np.asarray(v, dtype=np.float64))[tr] for k, v in refs.items()}
            print("variant        | " + " | ".join(f"{k:>20}" for k in refs))
            for vid, expr in variant_exprs.items():
                panel = VP.get(vid)
                if panel is None:
                    print(f"{vid:<14} | 求值失败,跳过")
                    continue
                rp = dg.rank_rows(np.asarray(panel, dtype=np.float64))[tr]
                vals = []
                for k in refs:
                    c = float(dg.nanmean_quiet(dg.cs_pearson(rp, ranked_refs[k])))
                    vals.append(f"{c:+.3f}")
                print(f"{vid:<14} | " + " | ".join(v.rjust(20) for v in vals))
            print("(原始日频面板,未平滑,两侧都没有乘方向;与前面主表里「交易信号口径」的矩阵是两套不同的数字,不要混用)")
        except Exception:
            print("附加节抛了异常:")
            traceback.print_exc()

    print("\n[a1_channels] 全部小节跑完")


if __name__ == "__main__":
    main()
