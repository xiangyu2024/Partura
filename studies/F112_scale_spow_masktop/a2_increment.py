"""A2_increment -- R2 工单运行 2。五节(§0 自检 → §1 独立对照 → §2 残差增量 → §3 合成增量 → §4 mask 机制),
各自 try/except,互不拖累,按工单"被打断时保下来的顺序"(§0→§1→§2→§3 先 K1,w=0.5 →§4→§3 其余)依次产出。

四个固定候选表达式(不依赖运行 1 / S2_combo 的结果,可独立提交):
  E0 原式           ts_scale(signedpower(cs_mask_top_replace_mean_neg(add(day_quantile(Close), day_kurt(High)))), 30)
  E1 mask去掉×w30   ts_scale(signedpower(add(day_quantile(Close), day_kurt(High))), 30)        (≡ s1_noMask ≡ s2_f30)
  E2 mask去掉×w60   cross_scale(signedpower(add(day_quantile(Close), day_kurt(High))), 60)      (≡ s2_f_x60)
  E3 两节点×w60     cross_scale(day_quantile(Close), 60)                                        (≡ s1_plain60)
这四个与已有阶段的变体表达式逐字相同,是故意的(免费的一次交叉核对,工单 S2_combo 的 why 字段写过同样的理由)。

本脚本自己写的两个核心函数(§0 先用本机随机数组 + 手算答案自检,过了才在服务器面板上用):
  pctrank_centered(x)   逐日横截面百分位秩,再 -0.5 居中(与 partura.diagnose._zrank 同一个公式,独立实现,不依赖私有符号)
  daily_ols_resid(y,xs) 逐日横截面 OLS(百分位秩空间、带截距)取残差,额外返回每日 R²(dg.neutralise 只给聚合均值,
                        这里要分 train/valid 两段分别算,所以自己写;同时用一个 >=50 名的合成面板与 dg.neutralise
                        交叉核对,确认与库里已验证的实现数值一致)
  long_gross_excess_ann(panel, target, day_slice) 手写的"多头十分位毛超额"(复用 bk.long_short_weights / bk.long_book /
                        bk.stats 这几个 books.py 本来就有的向量化原语,不经过 st.books,所以不会重新选 sign/半衰期)
"""
import sys
import traceback

import numpy as np


# ------------------------------------------------------------------ 手写函数(自检用,也是 §2/§3 共用的管线)

def pctrank_centered(x: np.ndarray, dg) -> np.ndarray:
    """逐日(行)横截面百分位秩,-0.5 居中(并列用平均秩,由 dg.rank_rows 处理;NaN 保持 NaN)。
    公式与 partura.diagnose._zrank 相同,这里不导入私有符号,自己写一遍再自检。"""
    r = dg.rank_rows(np.asarray(x, dtype=np.float64))
    n = np.isfinite(r).sum(axis=1, keepdims=True).astype(np.float64)
    with np.errstate(invalid="ignore", divide="ignore"):
        u = (r - 1.0) / np.maximum(n - 1.0, 1.0) - 0.5
    return u


def daily_ols_resid(y_raw: np.ndarray, xs_raw: dict, dg, min_names: int = 30):
    """逐日横截面 OLS:y、每个 x 先各自转成 pctrank_centered,再加截距回归,取残差。
    返回 (resid 面板(T,N), r2 每日数组(T,))。某天有效名字数 < min_names 时该天整行 NaN、r2[t]=NaN。
    控制变量把因子"精确张满"(rss/ss<1e-10)时同样整行 NaN,不把浮点噪声误报成残差 alpha(与 dg.neutralise 同一防护)。"""
    y = pctrank_centered(y_raw, dg)
    xs = {k: pctrank_centered(v, dg) for k, v in xs_raw.items()}
    T, N = y.shape
    out = np.full((T, N), np.nan)
    r2 = np.full(T, np.nan)
    names = list(xs)
    for t in range(T):
        m = np.isfinite(y[t])
        for k in names:
            m &= np.isfinite(xs[k][t])
        n = int(m.sum())
        if n < min_names:
            continue
        X = np.column_stack([np.ones(n)] + [xs[k][t][m] for k in names])
        yv = y[t][m]
        beta, *_ = np.linalg.lstsq(X, yv, rcond=None)
        resid = yv - X @ beta
        ss = float(((yv - yv.mean()) ** 2).sum())
        rss = float((resid ** 2).sum())
        if ss > 0:
            r2[t] = 1.0 - rss / ss
        if ss > 0 and rss / ss < 1e-10:
            continue
        out[t, m] = resid
    return out, r2


def long_gross_excess_ann(panel_full: np.ndarray, target_full: np.ndarray, day_slice, bk, top_frac: float = 0.10):
    """手写的"多头十分位毛超额"(年化):直接复用 books.py 的向量化原语(long_short_weights / long_book / stats),
    不经过 st.books,所以不会对 panel_full 重新选方向或半衰期——panel_full 必须已经是"越高越看多"的取向。
    返回 (年化毛超额, 该段覆盖率)。"""
    s = np.asarray(panel_full[day_slice], dtype=np.float64)
    t = np.asarray(target_full[day_slice], dtype=np.float64)
    w = bk.long_short_weights(s, top_frac)
    _, gross, _ = bk.long_book(w, s, t, cost=0.0)
    return bk.stats(gross)["ann"], float(np.isfinite(s).mean())


# ------------------------------------------------------------------ §4 复用 a1_channels.py 的重建管线(同一份算法,独立抄一遍)

def rolling_nansum_causal(x: np.ndarray, window: int) -> np.ndarray:
    filled = np.where(np.isfinite(x), x, 0.0)
    cums = np.cumsum(filled, axis=0)
    out = cums.copy()
    if window < cums.shape[0]:
        out[window:] -= cums[:-window]
    return out


def mask_replace_lowest(C: np.ndarray, topn_fn):
    """逐日:把有效值里最低的 topn_fn(count) 只换成当天全部有效值的均值。返回 (D, replaced_mask)。与
    a1_channels.py 的同名函数逐字相同(§1 自检已经验证过一遍,这里不重复验证,只重复使用)。"""
    T, N = C.shape
    D = C.copy()
    replaced = np.zeros((T, N), dtype=bool)
    for t in range(T):
        row = C[t]
        valid = np.isfinite(row)
        cnt = int(valid.sum())
        if cnt == 0:
            continue
        import math
        n_top = int(math.ceil(cnt * 0.1)) if topn_fn is None else int(topn_fn(cnt))
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


def ts_scale_like(E: np.ndarray, window: int, eps: float) -> np.ndarray:
    denom = rolling_nansum_causal(E, window)
    denom_g = np.where(np.abs(denom) < eps, 1.0, denom)
    return E / denom_g


def reconstruct_F(C: np.ndarray, window: int, eps: float):
    import math
    D, replaced = mask_replace_lowest(C, lambda cnt: math.ceil(cnt * 0.1))
    E = np.sign(D) * D ** 2
    F = ts_scale_like(E, window, eps)
    return F, D, replaced, E


def bucket_index(x: np.ndarray, dg, buckets: int = 10) -> np.ndarray:
    """与 a1_channels.py 同一套分桶算法(rank_rows 后按比例切),用于 §4 的"按 F 分 10 个分位"。"""
    rg = dg.rank_rows(np.asarray(x, dtype=np.float64))
    n = np.isfinite(rg).sum(axis=1, keepdims=True)
    with np.errstate(invalid="ignore"):
        b = np.floor((rg - 1.0) / np.maximum(n, 1) * buckets)
    return b


# ------------------------------------------------------------------ §0 本机自检(不依赖服务器/Study)

def self_check_local() -> bool:
    ok = True
    try:
        import partura.diagnose as dg_local  # 只用来调 rank_rows,不碰私有符号

        # --- pctrank_centered:含 NaN 行、全 NaN 行、常数行(并列) ---
        x = np.array([
            [1.0, 2.0, 3.0, 4.0, 5.0],          # 正常行
            [1.0, np.nan, 3.0, 4.0, 5.0],       # 含 NaN
            [np.nan, np.nan, np.nan, np.nan, np.nan],  # 全 NaN
            [7.0, 7.0, 7.0, 7.0, 7.0],          # 常数行(全部并列)
        ])
        u = pctrank_centered(x, dg_local)
        # 正常行:5 个值秩 1..5,(r-1)/4-0.5 = -0.5,-0.25,0,0.25,0.5
        want_row0 = np.array([-0.5, -0.25, 0.0, 0.25, 0.5])
        assert np.allclose(u[0], want_row0), f"pctrank 正常行不对:{u[0]} vs {want_row0}"
        # 含 NaN 行:NaN 位置应仍是 NaN,其余 4 个值按 4 个名字重新算秩(1..4 -> -0.5,-1/6? 用 (r-1)/3-0.5)
        assert np.isnan(u[1, 1]), "NaN 位应保持 NaN"
        finite_vals = u[1][np.isfinite(u[1])]
        assert np.allclose(sorted(finite_vals), [-0.5, -1.0 / 6, 1.0 / 6, 0.5], atol=1e-9), \
            f"含 NaN 行的百分位秩不对:{sorted(finite_vals)}"
        # 全 NaN 行:输出应整行 NaN,不报错
        assert np.isnan(u[2]).all(), "全 NaN 行应整行 NaN"
        # 常数行(全并列):平均秩 = (n+1)/2 = 3,(3-1)/4-0.5 = 0,全部应为 0
        assert np.allclose(u[3], 0.0), f"常数行(全部并列)应全部居中为 0:{u[3]}"

        # --- daily_ols_resid:手算完美拟合 + 与 dg.neutralise 交叉核对(>=50 个名字,两条实现应几乎相同) ---
        rng = np.random.default_rng(0)
        T, N = 4, 60
        x1 = rng.normal(size=(T, N))
        x2 = rng.normal(size=(T, N))
        # 完美拟合:y_raw 直接取成 x1 本身(同一组原始值)。daily_ols_resid 内部会把 y 和每个 x 都各自转成
        # pctrank_centered 再回归——百分位秩是非线性(保序)变换,"y 是 x1、x2 的某个线性组合"这个关系在转换后
        # 一般不会继续精确成立,所以不能拿"组合"去测;但"y_raw 与某个回归量逐值相同"在转换后仍然逐值相同
        # (同一个值过同一个变换两次结果一样),这才是能精确手算的完美拟合:系数应为 1(x1)、0(x2)、截距 0,残差精确为 0。
        y_perfect = x1.copy()
        resid_p, r2_p = daily_ols_resid(y_perfect, {"x1": x1, "x2": x2}, dg_local, min_names=10)
        # 完美拟合(rss/ss<1e-10)会命中"控制变量把因子精确张满"的保护分支:R2≈1,但残差应是 NaN(不是≈0)——
        # 这是故意的(与 dg.neutralise 同一防护,见该函数文档字符串),不把浮点舍入误差误报成残差 alpha。
        assert np.nanmin(r2_p) > 1 - 1e-6, f"完美拟合 R2 应几乎为 1,实际最小 {np.nanmin(r2_p)}"
        assert np.isnan(resid_p).all(), f"完美拟合应触发'控制变量精确张满'保护分支,残差应整体为 NaN,实际有 {np.isfinite(resid_p).sum()} 个有限值"

        y_noisy = pctrank_centered(x1, dg_local) + rng.normal(scale=0.3, size=(T, N))
        resid_mine, r2_mine = daily_ols_resid(y_noisy, {"x1": x1}, dg_local, min_names=10)
        resid_lib, info_lib = dg_local.neutralise(y_noisy, {"x1": x1})  # 库里已验证的实现,min_names 门槛是 50(本例 N=60,不会被跳过)
        diff = np.nanmax(np.abs(resid_mine - resid_lib))
        assert diff < 1e-9, f"与 dg.neutralise 交叉核对不一致,最大差 {diff}"

        # --- 显式测 NaN 行、全 NaN 行、常数行(放进真正要用的 daily_ols_resid 路径里,不只是 pctrank) ---
        y2 = y_noisy.copy()
        y2[1, :] = np.nan                      # 整天 NaN
        x1b = x1.copy()
        x1b[2, 5] = np.nan                     # 单个名字 NaN(那天其余名字应仍能拟合)
        x1b[3, :] = 5.0                        # 常数行(与截距列共线)
        resid3, r2_3 = daily_ols_resid(y2, {"x1": x1b}, dg_local, min_names=10)
        assert np.isnan(resid3[1]).all() and np.isnan(r2_3[1]), "整天 NaN 的那天,残差与 R2 都应是 NaN"
        assert np.isfinite(resid3[2]).sum() == N - 1, "单个名字 NaN 的那天,其余名字应正常参与回归"
        assert np.isfinite(r2_3[3]) or np.isnan(r2_3[3]), "常数行(与截距共线)不应抛异常,R2 给 NaN 或有限值都算过"

        print("[self-check] 本机自检全部通过(pctrank_centered 的 NaN/全NaN/常数行;"
              "daily_ols_resid 完美拟合、与 dg.neutralise 交叉核对、NaN/常数行边界)")
    except AssertionError as exc:
        ok = False
        print(f"[self-check] 失败:{exc}")
        traceback.print_exc()
    except Exception:
        ok = False
        print("[self-check] 跑的时候报了别的异常:")
        traceback.print_exc()
    return ok


def section(name: str) -> None:
    print(f"\n=== {name} ===", flush=True)


def main() -> None:
    print("[a2_increment] 脚本启动,先做本机自检(不依赖服务器)")
    local_ok = self_check_local()
    if not local_ok:
        print("本机自检没过,按工单规定(§0 是硬门槛):不进入服务器部分,直接退出。")
        return

    from partura.study_tools import Study, bk, dg

    FID = "F112_scale_spow_masktop"
    E0 = "ts_scale(signedpower(cs_mask_top_replace_mean_neg(add(day_quantile(Close), day_kurt(High)))), 30)"
    E1 = "ts_scale(signedpower(add(day_quantile(Close), day_kurt(High))), 30)"
    E2 = "cross_scale(signedpower(add(day_quantile(Close), day_kurt(High))), 60)"
    E3 = "cross_scale(day_quantile(Close), 60)"

    with Study(FID) as st:
        tr = st.slice("train")
        va = st.slice("valid")
        tgt = st.target()

        P = st.panels({"E0": E0, "E1": E1, "E2": E2, "E3": E3,
                       "C": "add(day_quantile(Close), day_kurt(High))"})
        K1 = st.control("known_stdamt_mean30")
        K2 = st.control("known_stdamt_max9")
        mom20 = st.control("ctl_mom20")
        price = st.control("ctl_price")

        pipeline_ok = False
        gross_fn_ok = False

        # =========================================================== §0(服务器部分)两条硬门槛自检
        section("§0 服务器管线自检(两条都要过,过不了就把依赖它的节跳掉)")
        try:
            b_e0 = st.books(P["E0"], fit="train", evals=("train", "valid"))
            long_tr = b_e0["by_rank"]["long"]["splits"]["train"]
            long_va = b_e0["by_rank"]["long"]["splits"]["valid"]
            hl_long = b_e0["hl_long"]
            print(f"  books(E0): hl_long={hl_long}  Lnet train={long_tr['long_ann']:+.4%} valid={long_va['long_ann']:+.4%}  "
                  f"Lshp train={long_tr['long_sharpe']:+.3f} valid={long_va['long_sharpe']:+.3f}")
            c1 = (abs(long_tr['long_ann'] - 0.037) < 0.002 and abs(long_va['long_ann'] - 0.053) < 0.002
                  and abs(long_tr['long_sharpe'] - 0.66) < 0.03 and abs(long_va['long_sharpe'] - 0.91) < 0.03
                  and abs(hl_long - 20.0) < 1e-9)
            print(f"  复现 v_base(Lnet +3.7%/+5.3%、Lshp +0.66/+0.91、hlL=20,容差 0.2pp/0.03):{'通过' if c1 else '没通过'}")

            sig_e0 = st.signal(P["E0"])
            lg_train, cov_train = long_gross_excess_ann(sig_e0, tgt, tr, bk)
            print(f"  手写 long_gross_excess_ann(E0 traded signal, train) = {lg_train:+.4%}  覆盖率={cov_train:.4f}")
            c2 = abs(lg_train - 0.086) < 0.003
            print(f"  复现 v_base Lgross train +8.6%(容差 0.3pp):{'通过' if c2 else '没通过'}")

            pipeline_ok = bool(c1 and c2)
            gross_fn_ok = bool(c2)
            if not pipeline_ok:
                print("  至少一条没过:按工单规定(这两条是 §1~§3 全部数字的地基),§1~§3 本次不算,"
                      "只把这两条自检的实际差距报回去;§4 用的是另一套自检(重建 spearman),不受这里影响,照跑。")
        except Exception:
            print("§0 服务器自检抛了异常:")
            traceback.print_exc()

        # =========================================================== §1 独立对照表
        section("§1 E0..E3 + K1/K2 的独立对照表(fit=train, evals=train/valid)")
        book_results = {}
        if not pipeline_ok:
            print("  §0 没过,按工单规定跳过 §1。")
        else:
            try:
                panels_1 = {"E0": P["E0"], "E1": P["E1"], "E2": P["E2"], "E3": P["E3"], "K1": K1, "K2": K2}
                for name, panel in panels_1.items():
                    b = st.books(panel, fit="train", evals=("train", "valid"))
                    book_results[name] = b
                print("  variant | sign | hlL |  Lnet tr |  Lnet va | Lshp tr | Lshp va | Lgross tr | Lgross va |  LTO tr")
                for name, panel in panels_1.items():
                    b = book_results[name]
                    sg = st.sign(panel, "train")
                    lt, lv = b["by_rank"]["long"]["splits"]["train"], b["by_rank"]["long"]["splits"]["valid"]
                    print(f"  {name:<7} | {sg:+.0f}  | {b['hl_long']:>3.0f} | {lt['long_ann']:+.3%} | {lv['long_ann']:+.3%} | "
                          f"{lt['long_sharpe']:+.3f} | {lv['long_sharpe']:+.3f} | {lt['long_gross_ann']:+.3%} | "
                          f"{lv['long_gross_ann']:+.3%} | {lt['long_turnover']:.2%}")
                print("  交叉核对(与已有阶段里同表达式的变体比,应逐位或近乎逐位相同):")
                print(f"    E0 vs v_base(S0/S1):     期望 Lnet tr+3.7% va+5.3%")
                print(f"    E1 vs s1_noMask/s2_f30:  期望 Lnet tr+7.1% va+9.3%")
                print(f"    E2 vs s2_f_x60:          期望 Lnet tr+7.8% va+8.5%")
                print(f"    E3 vs s1_plain60:        期望 Lnet tr+7.6% va+6.7%,hl 应在 10 见顶(不是 20)")
                print(f"    K1 vs S0_baseline.json diagnostics.controls.known_stdamt_mean30: 期望 Lnet tr+12.6% va+22.3%,sign=-1,hl_long=0")
                print(f"    K2 vs S0_baseline.json diagnostics.controls.known_stdamt_max9:   期望 Lnet tr+13.7% va+22.2%,sign=-1,hl_long=5")
            except Exception:
                print("§1 抛了异常:")
                traceback.print_exc()

        # =========================================================== §2 残差检验(H8 第一半)
        section("§2 残差检验:对 E0..E3 各自的交易信号,回归 {K1,K2} 与 {K1,K2,ctl_mom20},取残差")
        resid_cache = {}  # (E,group) -> (resid_full, r2_full)
        if not pipeline_ok:
            print("  §0 没过,按工单规定跳过 §2。")
        else:
            try:
                groupA = {"K1": K1, "K2": K2}
                groupB = {"K1": K1, "K2": K2, "ctl_mom20": mom20}
                print("  变体 | 组 | 日均R2(tr) | 日均R2(va) | 残差rIC tr | 残差rIC va | 残差Lgross tr | 残差Lgross va | 残差cov tr | 残差cov va | 判定tr | 判定va")
                for ekey in ("E0", "E1", "E2", "E3"):
                    sig_e = st.signal(P[ekey])  # 实际交易的信号:sign x panel, train 上选的 hl 平滑,全长
                    own_b = book_results.get(ekey)
                    own_lgross_tr = own_b["by_rank"]["long"]["splits"]["train"]["long_gross_ann"] if own_b else float("nan")
                    own_lgross_va = own_b["by_rank"]["long"]["splits"]["valid"]["long_gross_ann"] if own_b else float("nan")
                    # "自己的" rICtraded = 已经签过方向、按 hl 平滑过的交易信号自己的 rank IC(与主表 rICtraded 同一字段)
                    ic_tr_full = dg.ic_row(np.asarray(sig_e, dtype=np.float64)[tr], tgt[tr], sign=1.0)
                    ic_va_full = dg.ic_row(np.asarray(sig_e, dtype=np.float64)[va], tgt[va], sign=1.0)
                    own_ric_tr = ic_tr_full["rank_ic"]
                    own_ric_va = ic_va_full["rank_ic"]

                    for gname, gdict in (("A={K1,K2}", groupA), ("B={K1,K2,mom20}", groupB)):
                        resid_full, r2_full = daily_ols_resid(sig_e, gdict, dg, min_names=30)
                        resid_cache[(ekey, gname)] = (resid_full, r2_full)
                        r2_tr = float(np.nanmean(r2_full[tr]))
                        r2_va = float(np.nanmean(r2_full[va]))
                        ric_series = dg.rank_ic_series(resid_full, tgt)
                        ric_tr = dg.nanmean_quiet(ric_series[tr])
                        ric_va = dg.nanmean_quiet(ric_series[va])
                        lg_tr, cov_tr = long_gross_excess_ann(resid_full, tgt, tr, bk)
                        lg_va, cov_va = long_gross_excess_ann(resid_full, tgt, va, bk)

                        def verdict(lg, ric, own_lg, own_ric):
                            if not (np.isfinite(lg) and np.isfinite(own_lg) and own_lg != 0 and
                                    np.isfinite(ric) and np.isfinite(own_ric) and own_ric != 0):
                                return "数据不足"
                            lg_ok = lg >= 0.5 * own_lg
                            ric_ok = ric >= 0.5 * own_ric
                            return "有残差增量" if (lg_ok and ric_ok) else "无残差增量"

                        v_tr = verdict(lg_tr, ric_tr, own_lgross_tr, own_ric_tr)
                        v_va = verdict(lg_va, ric_va, own_lgross_va, own_ric_va)
                        print(f"  {ekey:<3} | {gname:<16} | {r2_tr:.3f} | {r2_va:.3f} | {ric_tr:+.4f} | {ric_va:+.4f} | "
                              f"{lg_tr:+.3%} | {lg_va:+.3%} | {cov_tr:.3f} | {cov_va:.3f} | {v_tr} | {v_va}")
                    print(f"    ({ekey} 自身未中性化(已平滑交易信号,与主表 rICtraded/Lgross 同一字段):"
                          f"Lgross tr={own_lgross_tr:+.3%} va={own_lgross_va:+.3%}  "
                          f"rICtraded tr={own_ric_tr:+.4f} va={own_ric_va:+.4f};判据的'一半'门槛就是这两个数的一半)")
            except Exception:
                print("§2 抛了异常:")
                traceback.print_exc()

        # =========================================================== §3 合成检验(H8 第二半,决定性问题)
        section("§3 合成检验:Z = w·pctrank(sE·PE) + (1-w)·pctrank(sK·PK),从原始面板构造,st.books 自己选半衰期")
        if not pipeline_ok:
            print("  §0 没过,按工单规定跳过 §3。")
        else:
            try:
                raw_panels = {"E1": P["E1"], "E2": P["E2"], "E3": P["E3"]}
                K_panels = {"K1": K1, "K2": K2}
                order_pairs = [("E1", "K1", 0.5), ("E2", "K1", 0.5), ("E3", "K1", 0.5),
                               ("E1", "K2", 0.5), ("E2", "K2", 0.5), ("E3", "K2", 0.5),
                               ("E1", "K1", 0.3), ("E2", "K1", 0.3), ("E3", "K1", 0.3),
                               ("E1", "K2", 0.3), ("E2", "K2", 0.3), ("E3", "K2", 0.3)]
                print("  组合 | w | sign | hlL | Lnet tr | Lnet va | Lshp tr | Lshp va | LTO tr | cov tr | 判定tr | 判定va  ||  家族单独 Lnet/Lshp tr,va")
                for ekey, kkey, w in order_pairs:
                    sE = st.sign(raw_panels[ekey], "train")
                    sK = st.sign(K_panels[kkey], "train")
                    pr_E = pctrank_centered(sE * np.asarray(raw_panels[ekey], dtype=np.float64), dg)
                    pr_K = pctrank_centered(sK * np.asarray(K_panels[kkey], dtype=np.float64), dg)
                    both = np.isfinite(pr_E) & np.isfinite(pr_K)
                    Z = np.where(both, w * pr_E + (1.0 - w) * pr_K, np.nan)
                    cov_tr = float(np.isfinite(Z[tr]).mean())
                    bz = st.books(Z, fit="train", evals=("train", "valid"))
                    lt, lv = bz["by_rank"]["long"]["splits"]["train"], bz["by_rank"]["long"]["splits"]["valid"]
                    sgz = st.sign(Z, "train")

                    kb = book_results.get(kkey)
                    if kb is None:
                        kb = st.books(K_panels[kkey], fit="train", evals=("train", "valid"))
                        book_results[kkey] = kb
                    klt = kb["by_rank"]["long"]["splits"]["train"]
                    klv = kb["by_rank"]["long"]["splits"]["valid"]

                    def verdict_syn(lnet, lshp, k_lnet, k_lshp):
                        return "合成有增量" if (lnet > k_lnet + 0.03 and lshp > k_lshp + 0.3) else "无增量"

                    v_tr = verdict_syn(lt['long_ann'], lt['long_sharpe'], klt['long_ann'], klt['long_sharpe'])
                    v_va = verdict_syn(lv['long_ann'], lv['long_sharpe'], klv['long_ann'], klv['long_sharpe'])
                    print(f"  {ekey}+{kkey} | {w} | {sgz:+.0f} | {bz['hl_long']:>3.0f} | {lt['long_ann']:+.3%} | {lv['long_ann']:+.3%} | "
                          f"{lt['long_sharpe']:+.3f} | {lv['long_sharpe']:+.3f} | {lt['long_turnover']:.2%} | {cov_tr:.3f} | "
                          f"{v_tr} | {v_va}  ||  {kkey}单独: {klt['long_ann']:+.3%}/{klt['long_sharpe']:+.3f}, "
                          f"{klv['long_ann']:+.3%}/{klv['long_sharpe']:+.3f}")
            except Exception:
                print("§3 抛了异常:")
                traceback.print_exc()

        # =========================================================== §4 mask 的损害机制(H10 预测②③④)
        section("§4 mask 损害机制:按 F 分 10 桶的被替换占比 / 多头十分位的低价股占比 / 最大并列组日期")
        try:
            C = np.asarray(P["C"], dtype=np.float64)
            F_rec, D, replaced, E_ = reconstruct_F(C, 30, 1e-12)
            Fe = np.asarray(P["E0"], dtype=np.float64)
            daily = dg.cs_pearson(dg.rank_rows(F_rec), dg.rank_rows(Fe))
            m_tr = float(dg.nanmean_quiet(daily[tr]))
            print(f"  §4 自己的重建自检(与 a1_channels.py §1 同一套代码,独立跑一遍):spearman(F_rec,E0) train 均值={m_tr:.5f}")
            s4_ok = m_tr >= 0.999
            if not s4_ok:
                print("  自检没过(<0.999),§4 剩余内容跳过。")
            else:
                # --- 1) 按 v_base 的 F 分 10 桶,每桶被替换占比 ---
                bidx = bucket_index(Fe, dg, 10)
                print("  1) 按 v_base F 分 10 桶(0=F最低、9=F最高;sign=-1 下多头端是桶0)的被替换占比(train 均值):")
                for k in range(10):
                    mask_k = (bidx == k)
                    with np.errstate(invalid="ignore", divide="ignore"):
                        frac_k = np.where(mask_k.sum(axis=1) > 0,
                                          (replaced & mask_k).sum(axis=1) / np.maximum(mask_k.sum(axis=1), 1), np.nan)
                    print(f"     桶{k}: {float(np.nanmean(frac_k[tr])):.2%}")

                # --- 2) v_base 与 E1 的多头十分位,低价股(全市场最低 1/5)占比 ---
                from alphacube.metrics import long_short_weights as lsw
                price_rank = dg.rank_rows(price)
                n_price = np.isfinite(price_rank).sum(axis=1, keepdims=True)
                with np.errstate(invalid="ignore", divide="ignore"):
                    price_pct = (price_rank - 1.0) / np.maximum(n_price - 1.0, 1.0)
                bottom_quintile = price_pct <= 0.20  # 全市场最低 1/5(价位最低)

                sig_vb = st.signal(P["E0"])
                sig_e1 = st.signal(P["E1"])
                for name, sig in (("v_base(E0)", sig_vb), ("E1(去mask)", sig_e1)):
                    w = lsw(np.asarray(sig, dtype=np.float64), float(st.cfg.get("top_frac", 0.10)))
                    long_mask = w > 0
                    with np.errstate(invalid="ignore", divide="ignore"):
                        frac_bottom = np.where(long_mask.sum(axis=1) > 0,
                                               (long_mask & bottom_quintile).sum(axis=1) / np.maximum(long_mask.sum(axis=1), 1),
                                               np.nan)
                    print(f"  2) {name} 多头十分位里,全市场最低价位 1/5 的占比(train 均值):{float(np.nanmean(frac_bottom[tr])):.2%}")

                # --- 3) 最大并列组的日期 + train 里并列>500 的天数 ---
                max_ties = []
                max_ties_dates = []
                for t_idx in range(tr.start, tr.stop):
                    row = Fe[t_idx]
                    row = row[np.isfinite(row)]
                    if row.size == 0:
                        max_ties.append(0)
                        max_ties_dates.append(st.dates[t_idx])
                        continue
                    _, counts = np.unique(row, return_counts=True)
                    max_ties.append(int(counts.max()))
                    max_ties_dates.append(st.dates[t_idx])
                max_ties_arr = np.array(max_ties)
                i_argmax = int(np.argmax(max_ties_arr))
                n_over_500 = int((max_ties_arr > 500).sum())
                print(f"  3) train 里最大并列组出现在 {max_ties_dates[i_argmax]}(并列 {max_ties_arr[i_argmax]} 只);"
                      f"并列 > 500 的天数:{n_over_500} / {len(max_ties_arr)}")
        except Exception:
            print("§4 抛了异常:")
            traceback.print_exc()

        # =========================================================== 附加节(非工单 §0~§4 原文,补"要带回来的数字"第 4 项
        # 的后一半):S2_combo 的 10 个 s2_* 变体,原始日频面板口径(未平滑、未乘方向)rank 相关,
        # 标准 diagnostics.rank_corr_train 只给交易信号口径一套矩阵,做法照抄 a1_channels.py 的附加节。
        section("附加节:S2_combo 10 个变体与 6 个参照的原始日频面板口径 rank 相关")
        try:
            s2_exprs = {
                "s2_f30": "ts_scale(signedpower(add(day_quantile(Close), day_kurt(High))), 30)",
                "s2_k30": "ts_scale(add(day_quantile(Close), day_kurt(High)), 30)",
                "s2_p30": "ts_scale(signedpower(day_quantile(Close)), 30)",
                "s2_n30": "ts_scale(day_quantile(Close), 30)",
                "s2_f_t50": "ts_scale(signedpower(add(day_quantile(Close), day_kurt(High))), 50)",
                "s2_f_x60": "cross_scale(signedpower(add(day_quantile(Close), day_kurt(High))), 60)",
                "s2_f_x241": "cross_scale(signedpower(add(day_quantile(Close), day_kurt(High))), 241)",
                "s2_n_t50": "ts_scale(day_quantile(Close), 50)",
                "s2_n_x241": "cross_scale(day_quantile(Close), 241)",
                "s2_masktop": "ts_scale(signedpower(cs_mask_top_replace_mean(add(day_quantile(Close), day_kurt(High)))), 30)",
            }
            S2P = st.panels(s2_exprs)
            refs = {
                "v_base": P["E0"],
                "s1_noMask(=s2_f30)": P["E1"],
                "ctl_mom20": mom20,
                "ctl_price": price,
                "K1(known_stdamt_mean30)": K1,
                "K2(known_stdamt_max9)": K2,
            }
            ranked_refs = {k: dg.rank_rows(np.asarray(v, dtype=np.float64))[tr] for k, v in refs.items()}
            print("  variant        | " + " | ".join(f"{k:>22}" for k in refs))
            for vid, expr in s2_exprs.items():
                panel = S2P.get(vid)
                if panel is None:
                    print(f"  {vid:<14} | 求值失败,跳过")
                    continue
                rp = dg.rank_rows(np.asarray(panel, dtype=np.float64))[tr]
                vals = []
                for k in refs:
                    c = float(dg.nanmean_quiet(dg.cs_pearson(rp, ranked_refs[k])))
                    vals.append(f"{c:+.4f}")
                print(f"  {vid:<14} | " + " | ".join(v.rjust(22) for v in vals))
            print("  (原始日频面板,未平滑、未乘方向;与前面 S2_combo 主表里交易信号口径的矩阵是两套不同的数字,不要混用。"
                  "s1_noMask/s1_plain30 在 diagnostics.rank_corr_train 里不存在(跨阶段 id 被静默丢掉,R1 已记录同一现象);"
                  "这里改用 s2_f30/s2_n30 的面板直接算,数值上就是 vs-s1_noMask / vs-s1_plain30。)")
        except Exception:
            print("附加节抛了异常:")
            traceback.print_exc()

    print("\n[a2_increment] 全部小节跑完")


if __name__ == "__main__":
    main()
