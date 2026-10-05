"""F115 R2 / x2_increment: 增量权重曲线(H6)+ 残差多头腿 + H9(封板票)+ H7b 确认(第 2 件,见
orders/R2.md "第 2 件")。Train / valid only -- 不调用 st.slice("holdout")。

本脚本的字母对应工单(orders/R2.md)自己的记号,不是 04_grammar.md 的 A..O:
  O   = v_base(S0_baseline 的原式,configs 里的顶层 expression)
  P   = a_no_rate(S1_anatomy,删掉 ÷M 的提纯版)
  K30 = known_stdamt_mean30 = cross_mean(day_std(Amt), 30)  (gates,与一等变体 k_stdamt_mean30 同一表达式)
  K9  = known_stdamt_max9  = cross_max(day_std(Amt), 9)     (gates,与新变体 k_stdamt_max9 同一表达式)

输出顺序按工单要求:(0) 自检/环境 -> (0b) by_year 工具缺口的补算 -> (4) -> (3) -> (2) -> (1),
最重要的权重曲线放最后,这样 `wait` 只回显的日志尾部 200 行一定能看到它。完整日志见
logs/F115_all_tide_mean_30_x2_increment.log。
"""
import inspect
import warnings

import numpy as np
import yaml

from partura.bridge import PARTURA_ROOT
from partura.study_tools import Study, bk, dg

warnings.simplefilter("ignore", RuntimeWarning)
FID = "F115_all_tide_mean_30"


def say(*a):
    print(*a, flush=True)


# ---------------------------------------------------------------- expression strings (same building
# blocks as studies/F115_all_tide_mean_30/anat_mfi.py's self-check (a), reused rather than retyped)
VOL5 = "in_local_mean(in_slice(Volume, 31, 211), 5)"
D_EXPR = f"day_argmax({VOL5})"
I_EXPR = f"day_argmin(in_slice_from_start({VOL5}, {D_EXPR}))"
F_EXPR = f"day_argmin(in_slice_to_end({VOL5}, {D_EXPR}))"
M_EXPR = f"sub({F_EXPR}, {I_EXPR})"
CLOSE_SLICE = "in_slice(Close, 31, 211)"
LOC_F = f"day_locate({CLOSE_SLICE}, {F_EXPR})"
LOC_I = f"day_locate({CLOSE_SLICE}, {I_EXPR})"
L_EXPR = f"div(sub({LOC_F}, {LOC_I}), {LOC_I})"
O_FROM_PARTS = f"cross_mean(div({L_EXPR}, {M_EXPR}), 20)"
P_FROM_PARTS = f"cross_mean({L_EXPR}, 20)"


def variant_expr(cfg: dict, stage_id: str, variant_id: str) -> str:
    for s in cfg["stages"]:
        if s["id"] == stage_id:
            for v in s["variants"]:
                if v["id"] == variant_id:
                    return v["expr"]
    raise KeyError((stage_id, variant_id))


def rank_pct(x: np.ndarray) -> np.ndarray:
    """逐日截面百分位秩,[0,1],NaN 保留。(r-1)/(n-1):最小值 ->0,最大值 ->1,ties 用 rank_rows 的平均秩。"""
    r = dg.rank_rows(np.asarray(x, dtype=np.float64))
    n = np.isfinite(r).sum(axis=1, keepdims=True).astype(np.float64)
    return (r - 1.0) / np.maximum(n - 1.0, 1.0)


def by_year_like_engine(sm_full: np.ndarray, tgt_full: np.ndarray, years_full: np.ndarray, scope: slice,
                        cost: float, top_frac: float) -> list:
    """逐年 book_row,与 partura/runner.py 算 diagnostics.by_year 的方法逐行相同(同一个 bk.book_row,
    同一种按 years==y 再和 scope 取交集求下标的办法),只是这里手动对一个跨阶段变体(k_stdamt_mean30)
    补算 -- 该变体属于 S1_anatomy,这次 run 只传了 S2_increment,工具的 by_year 诊断只认"当前这次 run
    自己阶段里的变体"(见下面(0b)的说明),所以配置里 by_year: [...] 列的 k_stdamt_mean30 被静默跳过。"""
    rows = []
    for y in sorted(set(years_full[scope].tolist())):
        idx = np.nonzero(years_full == y)[0]
        idx = idx[(idx >= scope.start) & (idx < scope.stop)]
        if idx.size < 20:
            continue
        rows.append({"year": y, "days": int(idx.size),
                     **bk.book_row(sm_full, tgt_full, slice(int(idx[0]), int(idx[-1]) + 1), cost, top_frac)})
    return rows


# ---------------------------------------------------------------- self-check (a): pure string, no data
_cfg_raw = yaml.safe_load((PARTURA_ROOT / "configs" / f"{FID}.yaml").read_text(encoding="utf-8"))
_O_cfg = _cfg_raw["expression"]
_P_cfg = variant_expr(_cfg_raw, "S1_anatomy", "a_no_rate")
assert O_FROM_PARTS == _O_cfg, (
    "[self-check a] FAILED: 拼出来的 O(cross_mean(div(L,M),20)) 与 configs 的 expression 不是逐字符相同,"
    "下面任何数字都不要信。\n拼出来的: " + O_FROM_PARTS + "\n配置里的 : " + _O_cfg)
assert P_FROM_PARTS == _P_cfg, (
    "[self-check a] FAILED: 拼出来的 P(cross_mean(L,20)) 与 configs 的 S1_anatomy/a_no_rate 不是逐字符相同。"
    "\n拼出来的: " + P_FROM_PARTS + "\n配置里的 : " + _P_cfg)
say("[self-check a] 通过:O=cross_mean(div(L,M),20)、P=cross_mean(L,20) 与 configs 逐字符相同"
    "(P 就是 O 去掉外层 ÷M)")

# ---------------------------------------------------------------- self-check (b): tiny synthetic arrays
_x = np.array([[10.0, 20.0, np.nan, 30.0], [5.0, 5.0, 10.0, np.nan]])
_rp = rank_pct(_x)
assert np.allclose(_rp[0, [0, 1, 3]], [0.0, 0.5, 1.0]) and np.isnan(_rp[0, 2]), _rp[0]
assert np.allclose(_rp[1, [0, 1, 2]], [0.25, 0.25, 1.0]) and np.isnan(_rp[1, 3]), _rp[1]       # 5,5 并列平均秩
_rpX = np.array([[0.2, np.nan, 0.8], [0.9, 0.1, 0.5]])
_rpK = np.array([[0.3, 0.4, np.nan], [0.6, 0.2, 0.7]])
_both = np.isfinite(_rpX) & np.isfinite(_rpK)
_blend = 0.5 * _rpX + 0.5 * _rpK
assert _both.tolist() == [[True, False, False], [True, True, True]]
assert np.isnan(_blend[0, 1]) and np.isnan(_blend[0, 2]) and abs(_blend[0, 0] - 0.25) < 1e-12, _blend
say("[self-check b] 通过:rank_pct 的 ties/NaN、以及 w*rpX+(1-w)*rpK 的 NaN 自动传播 == '两腿都有值才参与'")

_rng = np.random.default_rng(0)
_NDAYS, _NSYM = 40, 6                                              # >=20 天/年,过 by_year_like_engine 自己的最小天数门槛
_sm_syn = _rng.normal(size=(_NDAYS, _NSYM))
_tgt_syn = _rng.normal(size=(_NDAYS, _NSYM)) * 0.02
_years_syn = np.array(["2000"] * 20 + ["2001"] * 20)
_rows_syn = by_year_like_engine(_sm_syn, _tgt_syn, _years_syn, slice(0, _NDAYS), 0.0015, 0.5)
_direct0 = bk.book_row(_sm_syn, _tgt_syn, slice(0, 20), 0.0015, 0.5)
_direct1 = bk.book_row(_sm_syn, _tgt_syn, slice(20, 40), 0.0015, 0.5)
assert len(_rows_syn) == 2
assert _rows_syn[0]["year"] == "2000" and _rows_syn[0]["days"] == 20
assert _rows_syn[1]["year"] == "2001" and _rows_syn[1]["days"] == 20
for _k, _v in _direct0.items():
    if isinstance(_v, float) and np.isfinite(_v):
        assert abs(_rows_syn[0][_k] - _v) < 1e-9, ("y2000", _k, _rows_syn[0][_k], _v)
for _k, _v in _direct1.items():
    if isinstance(_v, float) and np.isfinite(_v):
        assert abs(_rows_syn[1][_k] - _v) < 1e-9, ("y2001", _k, _rows_syn[1][_k], _v)
say("[self-check b] 通过:by_year_like_engine 在合成数据(2 年 x 20 天)上与直接 bk.book_row(同一切片) 逐字段相同"
    "(含最小 20 天/年的门槛,与 partura/runner.py 一致)")


# ================================================================== 真实数据
with Study(FID) as st:
    cost = float(st.cfg.get("cost_per_side", 0.0015))
    top_frac = float(st.cfg.get("top_frac", 0.10))
    tr, va = st.slice("train"), st.slice("valid")
    utr = st.slice("utrain")
    years_full = np.asarray(st.ps.years)

    panels = st.panels({"O": st.cfg["expression"], "P": variant_expr(st.cfg, "S1_anatomy", "a_no_rate")})
    missing = [k for k in ("O", "P") if k not in panels]
    if missing:
        say(f"[警告] 面板求值失败: {missing}")
    O = np.asarray(panels["O"], dtype=np.float64)
    P = np.asarray(panels["P"], dtype=np.float64)
    K30 = np.asarray(st.control("known_stdamt_mean30"), dtype=np.float64)
    K9 = np.asarray(st.control("known_stdamt_max9"), dtype=np.float64)
    ctl_mom20 = np.asarray(st.control("ctl_mom20"), dtype=np.float64)
    ctl_dvol20 = np.asarray(st.control("ctl_dvol20"), dtype=np.float64)
    tgt = st.target()                        # buyable=True,与配置一致(label.buyable: true)

    # ---- 0 自检与环境确认 ------------------------------------------------------------------
    say("\n== 0 自检与环境确认")
    ic_tr = st.ic(O, "train")
    ok_ic = abs(ic_tr["rank_ic"] - 0.0374) < 0.0015
    say(f"  st.ic(O,'train')['rank_ic'] = {ic_tr['rank_ic']:+.4f}  (对照 +0.0374,"
        f"{'通过' if ok_ic else '不通过!!'})")
    if not ok_ic:
        raise SystemExit("[自检(0)不通过] st.ic(O,'train') 与已知值偏离超过容差,停下,不产出后面的数字。"
                          f"完整返回 = {ic_tr}")

    sig_books = inspect.signature(Study.books)
    sig_signal = inspect.signature(Study.signal)
    say(f"  inspect.signature(Study.books)  = {sig_books}")
    say(f"  inspect.signature(Study.signal) = {sig_signal}")
    can_pin = any(k in sig_books.parameters for k in ("halflife", "hl", "halflives"))
    say(f"  [结论] Study.books 签名里{'有' if can_pin else '没有'} halflife/hl 参数 -> "
        f"{'能' if can_pin else '不能'}直接钉住半衰期;它内部总是调 bk.books()->bk.fit_halflives(),"
        f"对全部 7 个候选半衰期各跑一次再选最优,**不能**跳过这个 sweep。")
    say("  但可以绕到底层 bk 模块自己钉住:bk.smoothed(sig, 0.0) 在 halflife=0.0(假值)时直接返回原信号、"
        "不做任何 EMA;配合 bk.book_row(sm, target, days, cost, top_frac) 直接算一个单一 hl 下的 book,"
        "完全跳过 fit_halflives 的 sweep。下面 (1)(2)(4) 的'pin hl=0'都是这么做的,不是通过 Study.books。")
    say("  --- Study.books 源码 ---\n" + inspect.getsource(Study.books))
    say("  --- Study.signal 源码 ---\n" + inspect.getsource(Study.signal))
    say("  st.signal 的 sign/hl 在哪个段上定:签名默认 fit='train' -- 两者都只在 train 上拟合一次,"
        "然后对全长(含 valid)原样套用,不重新拟合。")

    info = {}
    for nm, arr in (("O", O), ("P", P), ("K30", K30), ("K9", K9)):
        sgn = st.sign(arr, "train")
        hl_info = bk.fit_halflives(sgn * arr, tgt, tr, cost, top_frac)
        info[nm] = {"sign": sgn, "hl_long": hl_info["hl_long"], "hl_ls": hl_info["hl_ls"]}
        say(f"  {nm}: sign={sgn:+.0f}  hl_long={hl_info['hl_long']:.0f}  hl_ls={hl_info['hl_ls']:.0f}"
            f"  (预期 O: -1/10,P: -1/20,K30: -1/0)")

    sig_O = st.signal(O)      # fit='train' 默认:sign+hl_long 都在 train 上定,再套用到全长
    sig_P = st.signal(P)
    sig_K30 = st.signal(K30)
    sig_K9 = st.signal(K9)

    # 免费的参照:v_base / a_no_rate / known_stdamt_mean30 自己的主表数字,现场重算(面板全部已缓存,
    # 不产生新的求值开销),给 (1) 的两端自检用,不依赖抄表或读 JSON
    ref_books = {"O": st.books(O, fit="train", evals=("train", "valid")),
                 "P": st.books(P, fit="train", evals=("train", "valid")),
                 "K30": st.books(K30, fit="train", evals=("train", "valid"))}

    def ref_row(name, split):
        return ref_books[name]["by_rank"]["long"]["splits"][split]

    say(f"  [免费自检] 现场重算 st.books(O,...) vs 主表 v_base: train Lnet={ref_row('O','train')['long_ann']*100:+.2f}%"
        f" (对照 +5.6%)  valid Lnet={ref_row('O','valid')['long_ann']*100:+.2f}% (对照 +0.2%)")
    say(f"  [免费自检] 现场重算 st.books(P,...) vs 主表 a_no_rate: train Lnet={ref_row('P','train')['long_ann']*100:+.2f}%"
        f" (对照 +6.4%)  valid Lnet={ref_row('P','valid')['long_ann']*100:+.2f}% (对照 +2.0%)")
    say(f"  [免费自检] 现场重算 st.books(K30,...) vs 主表 k_stdamt_mean30: train Lnet={ref_row('K30','train')['long_ann']*100:+.2f}%"
        f" (对照 +12.6%)  valid Lnet={ref_row('K30','valid')['long_ann']*100:+.2f}% (对照 +22.3%)")

    # ---- 0b 工具缺口:by_year 对跨阶段变体(k_stdamt_mean30)静默跳过,手动补算 -------------------
    say("\n== 0b by_year 诊断的工具缺口(k_stdamt_mean30),以及补算")
    say("  根因(读 partura/runner.py 确认):diagnostics.by_year 只在 `for vid,v in variants.items()` 这个"
        "循环里给 traded_full[vid] 赋值,而 variants 只是**本次 run 传的 stage(S2_increment)自己的变体**;"
        "k_stdamt_mean30 属于 S1_anatomy,不在这次的 variants 里,所以即使配置的 by_year: [...] 列了它的 id,"
        "也进不了 traded_full,digest 里静默缺这一行(S2_increment.json 的 diagnostics.by_year 只有"
        "'c_pure'/'m_blend_pure_k30' 两个 key,没有 'v_base'/'k_stdamt_mean30')。corr_ids/corr_with 不受"
        "影响,因为 runner 另有一段专门把 refs(含跨阶段 id)喂给 traded(不是 traded_full)。")
    rows_k30_by_year = by_year_like_engine(sig_K30, tgt, years_full, utr, cost, top_frac)
    for r in rows_k30_by_year:
        say(f"  [补算] k_stdamt_mean30 {r['year']}: Lnet={r['long_ann']*100:+.2f}%  LS={r['ls_sharpe']:+.2f}"
            f"  days={r['days']}")
    say("  补算方法与 partura/runner.py 算 by_year 的那段代码逐行一致(同一个 bk.book_row,同样按 "
        "years==y 再与 scope 取交集定下标),已经用合成数据自检过(见上面 self-check b);range 限定在 "
        f"st.slice('utrain') = [{st.ps.dates[utr.start]}, {st.ps.dates[utr.stop-1]}],没有碰 holdout。")

    # ---- 4 H7b 确认:O 在固定 hl 下的 Lgross/Lnet/LTO(train)------------------------------------
    say("\n== 4 H7b 直接确认(可选,能做):O 在固定 hl 下的 Lgross/Lnet/LTO(train)")
    say("  能做:st.books 不能钉 hl,但 bk.smoothed(sign*O, hl) + bk.book_row(...) 可以绕过 sweep 直接钉住。")
    ref_gross_h7b = {0.0: 0.097, 2.0: 0.092, 5.0: 0.092, 10.0: 0.094, 20.0: 0.076}   # 07_S1_anatomy.md 解读
    sgn_O = info["O"]["sign"]
    for hl in (0.0, 2.0, 5.0, 10.0, 20.0):
        sm = bk.smoothed(sgn_O * O, hl)
        row = bk.book_row(sm, tgt, tr, cost, top_frac)
        say(f"  hl={hl:>4.0f}: Lgross={row['long_gross_ann']*100:+.2f}%  Lnet={row['long_ann']*100:+.2f}%"
            f"  LTO={row['long_turnover']*100:.2f}%  (反推对照 Lgross~={ref_gross_h7b[hl]*100:+.1f}%)")

    # ---- 3 H9:O 在两套标签下的多头/空头腿、long_share、LS --------------------------------------
    say("\n== 3 H9:O(=v_base)在 buyable=True / False 两套标签下(train, valid)")
    tgt_T = tgt
    tgt_F = st.target(buyable=False)
    exp_share, exp_ls, exp_short = 0.265, 2.53, 0.261
    for split_name, sl_ in (("train", tr), ("valid", va)):
        for lbl_name, tgt_case in (("buyable=True", tgt_T), ("buyable=False", tgt_F)):
            row = bk.book_row(sig_O, tgt_case, sl_, cost, top_frac)
            say(f"  {split_name:5s} {lbl_name:13s}: long_gross={row['long_gross_ann']*100:+.2f}%"
                f"  short_gross={row['short_gross_ann']*100:+.2f}%  long_share={row['long_share']:.4f}"
                f"  LS={row['ls_sharpe']:+.3f}  long_net={row['long_ann']*100:+.2f}%")
    chk = bk.book_row(sig_O, tgt_T, tr, cost, top_frac)
    ok3 = (abs(chk["long_share"] - exp_share) < 0.01 and abs(chk["ls_sharpe"] - exp_ls) < 0.05
           and abs(chk["short_gross_ann"] - exp_short) < 0.01)
    say(f"  对账(buyable=True, train): long_share={chk['long_share']:.4f}(对照~0.265) "
        f"LS={chk['ls_sharpe']:+.3f}(对照~+2.53) short={chk['short_gross_ann']*100:+.2f}%(对照~+26.1%)"
        f"  -> {'通过,下面 buyable=False 的数字可以当结论用' if ok3 else '不通过!buyable=False 的数字不要当结论用'}")

    # ---- 2 残差多头腿(H6 另一半):rank_pct(sig_X) 对 [K30]/[K30,K9]/[K30,K9,mom20,dvol20] 中性化 ----
    say("\n== 2 残差多头腿(秩空间回归,被解释变量 = rank_pct(sig_X))")
    say("  判读提醒:残差不再平滑、换手会更高,看 alpha 还在不在要看 Lgross 和 rIC,不是 Lnet(playbook §1)")
    ctrl_groups = {"a": {"K30": K30}, "b": {"K30": K30, "K9": K9},
                  "c": {"K30": K30, "K9": K9, "mom20": ctl_mom20, "dvol20": ctl_dvol20}}
    for X_name, X_sig in (("O", sig_O), ("P", sig_P)):
        for g_name, ctrls in ctrl_groups.items():
            resid, stat = dg.neutralise(X_sig, ctrls, space="rank")
            ric_tr = st.ic(resid, "train")["rank_ic"]
            ric_va = st.ic(resid, "valid")["rank_ic"]
            sgn_r = st.sign(resid, "train")
            bks = st.books(resid, fit="train", evals=("train", "valid"), sign=sgn_r)
            btr, bva = bks["by_rank"]["long"]["splits"]["train"], bks["by_rank"]["long"]["splits"]["valid"]
            rc = st.rank_corr(resid, K30, "train")
            say(f"  X={X_name} grp={g_name}({'+'.join(ctrls)}): meanR2={stat['mean_r2']:.4f}"
                f"  rIC(tr/va)={ric_tr:+.4f}/{ric_va:+.4f}  sign_resid={sgn_r:+.0f}  hl={bks['hl_used']:.0f}"
                f"  Lgross(tr/va)={btr['long_gross_ann']*100:+.2f}%/{bva['long_gross_ann']*100:+.2f}%"
                f"  Lnet(tr/va)={btr['long_ann']*100:+.2f}%/{bva['long_ann']*100:+.2f}%"
                f"  Lshp(tr/va)={btr['long_sharpe']:+.3f}/{bva['long_sharpe']:+.3f}"
                f"  LTO={btr['long_turnover']*100:.2f}%  rank_corr(resid,K30)={rc:+.4f}")

    # ---- 1 增量权重曲线(本轮最重要的一张表,H6)--------------------------------------------------
    say("\n== 1 增量权重曲线:blend_w = w*rank_pct(sig_X) + (1-w)*rank_pct(sig_K30)")
    Ws = (0.0, 0.10, 0.25, 0.50, 0.75, 1.00)
    rp_K30 = rank_pct(sig_K30)
    end_rows = {}                                      # 缓存 w=0/1 两端,给自检用
    for X_name, X_sig in (("O", sig_O), ("P", sig_P)):
        rp_X = rank_pct(X_sig)
        both = np.isfinite(rp_X) & np.isfinite(rp_K30)
        cov_tr, cov_va = float(both[tr].mean()), float(both[va].mean())
        say(f"  -- X={X_name}  覆盖率(两腿都有值) cov_tr={cov_tr:.4f} cov_va={cov_va:.4f} --")
        for w in Ws:
            blend = w * rp_X + (1.0 - w) * rp_K30
            pin_tr = bk.book_row(blend, tgt, tr, cost, top_frac)
            pin_va = bk.book_row(blend, tgt, va, cost, top_frac)
            sgn_b = st.sign(blend, "train")
            auto = st.books(blend, fit="train", evals=("train", "valid"), sign=sgn_b)
            auto_tr = auto["by_rank"]["long"]["splits"]["train"]
            auto_va = auto["by_rank"]["long"]["splits"]["valid"]
            say(f"  w={w:.2f} sgn_auto={sgn_b:+.0f}"
                f" | pin(hl=0)  Lnet {pin_tr['long_ann']*100:+.2f}%/{pin_va['long_ann']*100:+.2f}%"
                f" Lshp {pin_tr['long_sharpe']:+.3f}/{pin_va['long_sharpe']:+.3f}"
                f" Lgross {pin_tr['long_gross_ann']*100:+.2f}%/{pin_va['long_gross_ann']*100:+.2f}%"
                f" LTO {pin_tr['long_turnover']*100:.2f}%/{pin_va['long_turnover']*100:.2f}%"
                f" | auto(hl={auto['hl_used']:.0f}) Lnet {auto_tr['long_ann']*100:+.2f}%/{auto_va['long_ann']*100:+.2f}%"
                f" Lshp {auto_tr['long_sharpe']:+.3f}/{auto_va['long_sharpe']:+.3f}"
                f" Lgross {auto_tr['long_gross_ann']*100:+.2f}%/{auto_va['long_gross_ann']*100:+.2f}%"
                f" LTO {auto_tr['long_turnover']*100:.2f}%/{auto_va['long_turnover']*100:.2f}%")
            if w in (0.0, 1.0):
                end_rows[(X_name, w)] = {"pin_tr": pin_tr, "pin_va": pin_va, "auto_tr": auto_tr, "auto_va": auto_va}

    say("\n  -- 两端自检(偏离量 = 这一端的 blend 数字 - 对应主表参照;就是二次平滑/覆盖率限制的代价)--")
    for X_name in ("O", "P"):
        ref_name = X_name
        for split in ("train", "valid"):
            ref = ref_row(ref_name, split)
            e = end_rows[(X_name, 1.0)][f"pin_{'tr' if split=='train' else 'va'}"]
            ea = end_rows[(X_name, 1.0)][f"auto_{'tr' if split=='train' else 'va'}"]
            say(f"  w=1 X={X_name} {split}: ref(st.books({X_name})) Lnet={ref['long_ann']*100:+.2f}% Lshp={ref['long_sharpe']:+.3f}"
                f"  | pin 偏离 dLnet={100*(e['long_ann']-ref['long_ann']):+.2f}pp dLshp={e['long_sharpe']-ref['long_sharpe']:+.3f}"
                f"  | auto 偏离 dLnet={100*(ea['long_ann']-ref['long_ann']):+.2f}pp dLshp={ea['long_sharpe']-ref['long_sharpe']:+.3f}")
        for split in ("train", "valid"):
            ref = ref_row("K30", split)
            e = end_rows[(X_name, 0.0)][f"pin_{'tr' if split=='train' else 'va'}"]
            ea = end_rows[(X_name, 0.0)][f"auto_{'tr' if split=='train' else 'va'}"]
            say(f"  w=0 X={X_name} {split}: ref(st.books(K30)) Lnet={ref['long_ann']*100:+.2f}% Lshp={ref['long_sharpe']:+.3f}"
                f"  | pin 偏离 dLnet={100*(e['long_ann']-ref['long_ann']):+.2f}pp dLshp={e['long_sharpe']-ref['long_sharpe']:+.3f}"
                f"  | auto 偏离 dLnet={100*(ea['long_ann']-ref['long_ann']):+.2f}pp dLshp={ea['long_sharpe']-ref['long_sharpe']:+.3f}")

    say("\ndone")
