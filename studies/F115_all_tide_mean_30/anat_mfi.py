"""F115 R1 / x1_anat_mfi: anatomy of N = L x (1/M) on the six raw daily panels.

Order: notes/F115_all_tide_mean_30/orders/R1.md, "第 2 件". Train split only -- never calls
st.slice("holdout"). Letters D/I/F/M/L/N/O below are the ORDER's own names (its "怎么量" table),
not the 04_grammar.md A..O node letters:

  D  潮顶的分钟下标           = day_argmax(in_local_mean(...))                  (几何: 事件定位)
  I  潮前谷的分钟下标         = day_argmin(in_slice_from_start(..., D))
  F  潮后谷的分钟下标         = day_argmin(in_slice_to_end(..., D))
  M  = F - I                两谷相隔的分钟数(几何通道)
  L  = (Close[F] - Close[I]) / Close[I]     两谷之间的涨跌幅(带符号价格通道)
  N  = L / M                 原式求和之前的逐日量(幅度通道 = |N|)
  O  = cross_mean(N, 20)     原式本身, 必须与 configs/F115_all_tide_mean_30.yaml 的 expression
                             逐字符相同 -- 用字符串自检(见下)钉死,不依赖手工目测。

三层自检(从便宜到贵):
  (a) 纯字符串,不碰任何数据: cross_mean(N,20) 拼出来必须和配置里的 expression 逐字符相同。
      本机已经用同一段 python 预先跑过一遍确认 True(见 R1 结果卡),这里在服务器上再跑一遍留痕。
  (b) 合成小数组,不碰服务器数据: 分位数 / 阈值占比 / 按十分位取中位数 三个工具在手算答案上的正确性,
      包括用这里真正会用到的 dg.rank_rows 做十分位(而不是另写一套参照实现)。
  (c) 真实数据: st.ic(O, "train") 应 ~= +0.0374 (S0_baseline 的 rIC tr; 本机 digest 已重新核对过)。
"""
import warnings

import numpy as np
import yaml

from partura.bridge import PARTURA_ROOT
from partura.study_tools import Study, bk, dg

warnings.simplefilter("ignore", RuntimeWarning)
FID = "F115_all_tide_mean_30"


def say(*a):
    print(*a, flush=True)


# ---------------------------------------------------------------- expressions (building blocks,
# each used more than once below -- composed, not retyped, to avoid a hand-copy paren mistake;
# self-check (a) proves the composition is byte-identical to the order/config)
VOL5 = "in_local_mean(in_slice(Volume, 31, 211), 5)"
D_EXPR = f"day_argmax({VOL5})"
I_EXPR = f"day_argmin(in_slice_from_start({VOL5}, {D_EXPR}))"
F_EXPR = f"day_argmin(in_slice_to_end({VOL5}, {D_EXPR}))"
M_EXPR = f"sub({F_EXPR}, {I_EXPR})"
CLOSE_SLICE = "in_slice(Close, 31, 211)"
LOC_F = f"day_locate({CLOSE_SLICE}, {F_EXPR})"
LOC_I = f"day_locate({CLOSE_SLICE}, {I_EXPR})"
L_EXPR = f"div(sub({LOC_F}, {LOC_I}), {LOC_I})"
N_EXPR = f"div({L_EXPR}, {M_EXPR})"
O_FROM_N = f"cross_mean({N_EXPR}, 20)"

# ---------------------------------------------------------------- self-check (a): pure string,
# no data, no server call -- must pass before anything else runs
_cfg_expr = yaml.safe_load((PARTURA_ROOT / "configs" / f"{FID}.yaml").read_text(encoding="utf-8"))["expression"]
assert O_FROM_N == _cfg_expr, (
    "[self-check a] FAILED: cross_mean(N,20) 拼出来和 configs 的 expression 不是逐字符相同 -- "
    "D/I/F/M/L/N 某条抄错了,下面任何数字都不要信。\n拼出来的: " + O_FROM_N + "\n配置里的 : " + _cfg_expr)
say("[self-check a] 通过:自己拼的 cross_mean(N,20) 与 configs 的 expression 逐字符相同")


# ---------------------------------------------------------------- small helpers + self-check (b)
def pctline(x, qs=(1, 5, 10, 25, 50, 75, 90, 95, 99)):
    v = x[np.isfinite(x)]
    if v.size == 0:
        return "n=0 (全是 NaN)"
    parts = " ".join(f"p{q}={np.percentile(v, q):+.3f}" for q in qs)
    return f"n={v.size} {parts} mean={v.mean():+.3f}"


def thresh_shares(x, ks):
    v = x[np.isfinite(x)]
    eq0 = float((v == 0).mean()) if v.size else float("nan")
    les = {k: (float((v <= k).mean()) if v.size else float("nan")) for k in ks}
    return v.size, eq0, les


def decile_by(factor_2d, value_2d):
    """逐日按 factor_2d 做截面十分位(dg.rank_rows,ties 平均、NaN 保留),再把同一桶的样本跨天汇总
    (方法二选一里的"先按天分桶再把同一桶的样本汇总")。返回 dec 数组,0=Q1 … 9=Q10。"""
    r = dg.rank_rows(np.asarray(factor_2d, dtype=np.float64))
    n = np.isfinite(r).sum(1, keepdims=True).astype(np.float64)
    dec = np.floor((r - 1.0) / np.maximum(n, 1.0) * 10.0)
    return np.where(np.isfinite(r), np.minimum(dec, 9), -1.0)


# -- self-check (b): hand-computed answers on tiny synthetic arrays (NaN handled, no ties)
_x = np.array([0., 1., 2., 3., 4., 5., 6., 7., 8., 9., np.nan])
_pl = pctline(_x, qs=(10, 50, 90))
assert "n=10" in _pl and "p50=+4.500" in _pl, _pl
_n, _eq0, _les = thresh_shares(_x, (2, 5))
assert _n == 10 and abs(_eq0 - 0.1) < 1e-9 and abs(_les[2] - 0.3) < 1e-9 and abs(_les[5] - 0.6) < 1e-9, (_n, _eq0, _les)
_day = np.arange(10.0)
_O2 = np.vstack([_day, _day])                                    # O ascending 0..9 both days -> rank 1..10
_M2 = np.vstack([np.arange(100, 0, -10.0)] * 2)                  # M descending: rank1->100 ... rank10->10
_dec = decile_by(_O2, _M2)
assert np.nanmedian(_M2[_dec == 0]) == 100.0 and np.nanmedian(_M2[_dec == 9]) == 10.0, _dec
say("[self-check b] 通过:pctline / thresh_shares / decile_by 在手算答案上都对")


# ================================================================== 真实数据
with Study(FID) as st:
    O_EXPR = st.cfg["expression"]
    P = st.panels({"D": D_EXPR, "I": I_EXPR, "F": F_EXPR, "M": M_EXPR, "L": L_EXPR, "N": N_EXPR,
                   "O": O_EXPR, "cm_M20": f"cross_mean({M_EXPR}, 20)"})
    missing = [k for k in ("D", "I", "F", "M", "L", "N", "O", "cm_M20") if k not in P]
    if missing:
        say(f"[警告] 以下面板求值失败,没有拿到: {missing} (看上面 [study] ... failed 那一行的报错)")

    def f64(x):
        return np.asarray(x, dtype=np.float64)

    tr = st.slice("train")
    Dp, Ip, Fp = f64(P["D"]), f64(P["I"]), f64(P["F"])
    Mp, Lp, Np, Op = f64(P["M"]), f64(P["L"]), f64(P["N"]), f64(P["O"])
    CmM20 = f64(P["cm_M20"])

    # ---- 1 自检 (c): 已知答案 + 六个面板的 shape / NaN 占比 ---------------------------------
    say("\n== 1 自检(c)与面板概况")
    ic_tr = st.ic(Op, "train")
    say(f"  st.ic(O,'train')['rank_ic'] = {ic_tr['rank_ic']:+.4f}  (对照 S0_baseline rIC tr +0.0374;"
        f"完整返回 = {ic_tr})")
    say(f"  面板 shape(全长) = {Dp.shape}")
    for nm, x in (("D", Dp), ("I", Ip), ("F", Fp), ("M", Mp), ("L", Lp), ("N", Np)):
        xt = x[tr]
        say(f"  {nm}: train 段 NaN 占比 = {np.isnan(xt).mean():.4f}  (finite n={np.isfinite(xt).sum()})")

    # ---- 2 M 的分布 + N 的 NaN 占比(核对 M=0 -> N=NaN) --------------------------------------
    say("\n== 2 M 的分布(train)")
    Mt = Mp[tr]
    say("  M: " + pctline(Mt))
    n_valid, eq0, shares = thresh_shares(Mt, (2, 5, 10, 20))
    say(f"  M 有效格子 n={n_valid}  M==0 占比 {eq0:.4f}  " + "  ".join(f"M<={k} 占比 {v:.4f}" for k, v in shares.items()))
    Nt = Np[tr]
    nan_N = np.isnan(Nt).mean()
    say(f"  N 的 NaN 占比(train,全体)= {nan_N:.4f}")
    m0 = Mt == 0
    if m0.any():
        say(f"  额外交叉检验(M==0 -> N 是否为 NaN):M==0 的格子里 N 是 NaN 的占比 = {np.isnan(Nt[m0]).mean():.4f}"
            f"  (M==0 的格子数 = {int(m0.sum())})")
    else:
        say("  额外交叉检验:train 段里一个 M==0 的格子都没有,没法做这个交叉检验")

    # ---- 3 D / I / F 的分布 ------------------------------------------------------------------
    say("\n== 3 D / I / F 的分布(train;下标范围应落在 [0,180] 内,180 = in_slice(·,31,211) 的宽度)")
    say("  D: " + pctline(Dp[tr]))
    say("  I: " + pctline(Ip[tr]))
    say("  F: " + pctline(Fp[tr]))

    # ---- 4 L / N / |N| 的分布 ----------------------------------------------------------------
    say("\n== 4 L / N / |N| 的分布(train)")
    say("  L    : " + pctline(Lp[tr]))
    say("  N    : " + pctline(Nt))
    say("  |N|  : " + pctline(np.abs(Nt)))

    # ---- 5 H3 直接检验:按因子 O 做截面十分位,看 Q1/Q5/Q10 里 M 和 |N| 的中位数 --------------
    say("\n== 5 H3 检验:按 O 的截面十分位分桶(逐日算 rank,再把同一桶的样本跨天汇总后取一个中位数"
        " -- playbook 允许的两种口径里用的是这一种),Q1=空头端 Q10=多头端")
    Ot = Op[tr]
    dec = decile_by(Ot, Ot)            # 用 O 自己的截面排名分桶(dec 的 shape 与 train 段一致)
    absNt = np.abs(Nt)
    for lbl, k in (("Q1", 0.0), ("Q5", 4.0), ("Q10", 9.0)):
        m = dec == k
        say(f"  {lbl}(dec={int(k)}): n={int(m.sum())}  median(M)={np.nanmedian(Mt[m]):.3f}"
            f"  median(|N|)={np.nanmedian(absNt[m]):.5f}")

    # ---- 6 rank 相关(train,逐日算再对天取平均 = st.rank_corr / dg.pair_rank_corr) -----------
    say("\n== 6 rank 相关(train)")
    say("-- 原始日频面板(未平滑)--")
    say(f"  N ~ L          {st.rank_corr(Np, Lp, 'train'):+.4f}")
    say(f"  N ~ M          {st.rank_corr(Np, Mp, 'train'):+.4f}")
    say(f"  |N| ~ M        {st.rank_corr(np.abs(Np), Mp, 'train'):+.4f}")
    say(f"  O ~ cross_mean(M,20)   {st.rank_corr(Op, CmM20, 'train'):+.4f}")
    ks = f64(st.control("known_stdamt_mean30"))
    iv = f64(st.control("ctl_ivol"))
    mo = f64(st.control("ctl_mom20"))
    say(f"  O ~ known_stdamt_mean30   {st.rank_corr(Op, ks, 'train'):+.4f}")
    say(f"  O ~ ctl_ivol              {st.rank_corr(Op, iv, 'train'):+.4f}")
    say(f"  O ~ ctl_mom20             {st.rank_corr(Op, mo, 'train'):+.4f}")

    say("-- 再用实际交易的信号重做最后三项(sign x O,按多头口径半衰期平滑;sign/hl 都在 train 上拟合)--")
    sgn = st.sign(Op, "train")
    hl_info = bk.fit_halflives(sgn * Op, st.target(), tr,
                               float(st.cfg.get("cost_per_side", 0.0015)), float(st.cfg.get("top_frac", 0.10)))
    say(f"  (核对:sign={sgn:+.0f}  hl_long={hl_info.get('hl_long')}  hl_ls={hl_info.get('hl_ls')}"
        f"  -- 应与 v_base/S0_baseline 的 hlL=10、hlS=10、sgn=- 一致)")
    sig = st.signal(Op)
    say(f"  sig ~ known_stdamt_mean30   {st.rank_corr(sig, ks, 'train'):+.4f}")
    say(f"  sig ~ ctl_ivol              {st.rank_corr(sig, iv, 'train'):+.4f}")
    say(f"  sig ~ ctl_mom20             {st.rank_corr(sig, mo, 'train'):+.4f}")

    say("\ndone")
