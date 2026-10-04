"""Probes this tree needs:  D * | M - Q |

    D = Close_last / Open_first - 1
    G = log(Volume) - in_forward_valid_part(log(Volume))          (minute log-volume change)
    M = day_mean(in_sustain_stddev(G > mean(G) + std(G), Ret, 5)) (5-min return std hanging off volume SURGES)
    Q = day_mean(in_sustain_stddev(G < mean(G) - std(G), Ret, 5)) (the same hanging off volume DROPS)

The built-in probes are blind here for three reasons: the trigger kernel is fed random floats (mask == 1
never holds, so every built-in reading on `in_sustain_stddev` is vacuous), `in_forward_valid_part` is a
LOOKUP whose behaviour is in what it skips, and the interesting property of this tree is a property of the
COMPOSITION (two masks built from the same series with opposite signs), not of any one kernel.

Five questions, each with a self-check on a kernel / a case whose answer is known:

* ``prev_valid_lookup``     which minute does `in_forward_valid_part` read, and what does it do at a 0 / NaN
                            hole?  (self-check: `in_delay(x, 1)` must read exactly offset -1 and must NOT skip)
* ``unary_domain``          f(0), f(1), f(-e), f(tiny): is log(0) -inf or NaN, what happens to log of a
                            negative number, where is the EPS cut?  (self-check: on `abs_` the answers are 0, 1, e)
* ``trigger_window``        which minutes does the trigger kernel read relative to the trigger, which statistic
                            (population / sample), what at the end of the row, what on a row with no trigger?
                            (self-check: `in_stddev_full` on a 5-wide ramp must read 1.4142)
* ``comparison_semantics``  NaN and ties in the comparison that builds the masks.
* ``spike_composite``       the whole S = |M - Q| built from the real kernels on synthetic days whose answer is
                            analytic: an isolated one-minute volume spike at j fires SURGE at j and DROP at j+1,
                            the two 5-minute windows overlap in 4 minutes, and S must equal
                            0.4 * | |r_j| - |r_{j+5}| |  (population std of one non-zero value among five is
                            0.4 * |value|).  Also: a closing-auction-like last minute, a zero-volume gap,
                            homogeneity of S in Ret and in Volume, and whether swapping surge / drop changes S.
"""

import math

import torch

from partura.probes import ProbeContext, probe


def _kernel(name):
    from alphacube.catalog import default_registry
    from alphacube.fullcatalog import default_full_catalog
    reg = default_registry()
    if name in reg._ops:
        return reg._ops[name].fn
    return default_full_catalog().get(name).fn


def _minute_keeps_m(s):
    return s.compute_axis == "M" and not getattr(s, "reduces_m", False)


# ------------------------------------------------------------------ prev_valid_lookup
def _lookup_profile(call, shape):
    """What minute j of the output reads, and what a 0 / NaN hole at j-1 does."""
    R, T = shape
    j = T // 2
    g = torch.Generator().manual_seed(101)
    x = torch.randn(shape, generator=g, dtype=torch.float64).abs() + 1.0
    base = call(x).double()
    hits = []
    for k in range(-j, T - j):
        x2 = x.clone()
        x2[:, j + k] += 10.0
        out = call(x2).double()
        a, b = base[:, j], out[:, j]
        if bool(((a - b).abs() > 1e-9)[torch.isfinite(a) & torch.isfinite(b)].any()) or \
                bool((torch.isfinite(a) != torch.isfinite(b)).any()):
            hits.append(k)

    def hole(v):
        x2 = x.clone()
        x2[:, j - 1] = v
        o = call(x2).double()[:, j]
        if bool(torch.isnan(o).all()):
            return "nan"
        if bool(((o - x[:, j - 2]).abs() < 1e-9).all()):
            return "skips_to_j-2"
        if v == v and bool(((o - v).abs() < 1e-9).all()):
            return "returns_the_hole"
        return "other"

    return {"reads": hits if len(hits) <= 6 else f"all {len(hits)} of {T} minutes (incl. later ones)",
            "zero_at_j-1": hole(0.0), "nan_at_j-1": hole(float("nan")),
            "first_minute_is_nan": bool(torch.isnan(base[:, 0]).all())}


@probe("prev_valid_lookup",
       question="第 j 分钟的输出读了哪一分钟的输入?上一分钟是 0 / NaN 时怎么办?(自检:in_delay(x,1) 只读 j-1 且不跳过)",
       applies=lambda s: _minute_keeps_m(s) and s.arity == 1 and not s.requires_window)
def _prev_valid(ctx: ProbeContext):
    res = _lookup_profile(lambda x: ctx.call([x]), ctx.shape)
    delay = _kernel("in_delay")
    chk = _lookup_profile(lambda x: delay(x, 1), ctx.shape)
    ok = chk["reads"] == [-1] and chk["zero_at_j-1"] == "returns_the_hole" and chk["nan_at_j-1"] == "nan"
    if not ok:
        raise RuntimeError(f"self-check failed on in_delay: {chk}")
    res["selfcheck_in_delay"] = "ok"
    return res


# ------------------------------------------------------------------ unary_domain
@probe("unary_domain",
       question="f(0)、f(1)、f(-e)、f(很小的正数) 各是多少?(log(0) 是 -inf 还是 NaN;自检:abs_ 应给 0、1、e)",
       applies=lambda s: s.compute_axis is None and s.face == "shared" and s.category == "unary")
def _domain(ctx: ProbeContext):
    pts = [0.0, 1.0, -math.e, 1e-3, 1e-6, 1e-9, 1e-12]
    x = torch.tensor([pts], dtype=torch.float64)
    y = ctx.call([x]).double().flatten().tolist()
    chk = _kernel("abs_")(x).double().flatten().tolist()
    if not (chk[0] == 0.0 and chk[1] == 1.0 and abs(chk[2] - math.e) < 1e-12):
        raise RuntimeError(f"self-check failed on abs_: {chk[:3]}")

    def r(v):
        return "nan" if v != v else ("-inf" if v == float("-inf") else round(v, 4))

    finite_small = [p for p, v in zip(pts[3:], y[3:]) if v == v and abs(v) != float("inf")]
    return {"f(0)": r(y[0]), "f(1)": r(y[1]), "f(-e)": r(y[2]),
            "smallest_positive_input_still_finite": min(finite_small) if finite_small else None}


# ------------------------------------------------------------------ trigger_window
def _is_trigger(ctx: ProbeContext) -> bool:
    if ctx.arity != 2:
        return False
    R, T = ctx.shape
    data = ctx.sample(301, positive=False)
    none = ctx.call([torch.zeros(ctx.shape, dtype=torch.float64), data]).double()
    one = torch.zeros(ctx.shape, dtype=torch.float64)
    one[:, T // 2] = 1.0
    hit = ctx.call([one, data]).double()
    return bool(torch.isfinite(none).sum() == 0 and torch.isfinite(hit).sum() == R)


@probe("trigger_window",
       question="触发型算子:相对触发分钟读了哪些分钟?是总体 std 还是样本 std?窗口跑出行尾怎么办?没有触发的行给什么?"
                "(自检:in_stddev_full 在 5 宽斜坡上应读出 1.4142)",
       applies=lambda s: _minute_keeps_m(s) and s.category == "pair_rolling")
def _trigger_window(ctx: ProbeContext):
    if not _is_trigger(ctx):
        return "不是触发型算子"
    R, T = ctx.shape
    j = T // 2
    data = ctx.sample(201, positive=False)
    mask = torch.zeros(ctx.shape, dtype=torch.float64)
    mask[:, j] = 1.0
    base = ctx.call([mask, data]).double()[:, j]
    offs = []
    for k in range(-j, T - j):
        d2 = data.clone()
        d2[:, j + k] += 10.0
        if bool(((ctx.call([mask, d2]).double()[:, j] - base).abs() > 1e-9).any()):
            offs.append(k)
    ramp = torch.arange(T, dtype=torch.float64).reshape(1, T).repeat(R, 1)
    left = {}
    for m_left in (T // 2, 4, 3, 2, 1):
        mk = torch.zeros(ctx.shape, dtype=torch.float64)
        mk[:, T - m_left] = 1.0
        left[f"ramp_{m_left}_minutes_left"] = round(float(ctx.call([mk, ramp]).double()[0, T - m_left]), 4)
    five = torch.arange(5, dtype=torch.float64).reshape(1, 5).repeat(R, 1)
    chk = float(_kernel("in_stddev_full")(five).double()[0, 0])
    if abs(chk - math.sqrt(2.0)) > 1e-6:
        raise RuntimeError(f"self-check failed: in_stddev_full on a 5-wide ramp gave {chk}")
    fires = []
    for v in (1.0, 2.0, 0.5, float("nan")):
        mk = torch.zeros(ctx.shape, dtype=torch.float64)
        mk[:, j] = v
        if bool(torch.isfinite(ctx.call([mk, data]).double()[:, j]).all()):
            fires.append(v)
    # a NaN inside the data window: is it skipped (nan-aware) or does it poison the value?
    d3 = data.clone()
    d3[:, j + 1] = float("nan")
    nan_in_window = "skipped" if bool(torch.isfinite(ctx.call([mask, d3]).double()[:, j]).all()) else "poisons"
    return {"offsets_read": offs, **left, "fires_on": fires, "nan_in_window": nan_in_window,
            "non_trigger_minutes": "nan", "selfcheck_in_stddev_full": "ok"}


# ------------------------------------------------------------------ comparison_semantics
@probe("comparison_semantics",
       question="比较算子遇到 NaN、相等时给什么?(决定第一分钟、零成交分钟算不算触发)",
       applies=lambda s: s.compute_axis is None and s.face == "shared" and s.category == "general")
def _cmp(ctx: ProbeContext):
    if ctx.arity != 2:
        return None
    a = torch.tensor([[1.0, 2.0, float("nan"), 3.0, 0.0]], dtype=torch.float64)
    b = torch.tensor([[2.0, 1.0, 1.0, float("nan"), 0.0]], dtype=torch.float64)
    out = ctx.call([a, b])
    vals = out.double().flatten().tolist()
    if not set(v for v in vals if v == v) <= {0.0, 1.0}:
        return None                                   # an arithmetic binary (add / sub / mul / div), not a comparison
    return {"a<b": vals[0], "a>b": vals[1], "nan_left": vals[2], "nan_right": vals[3], "equal": vals[4],
            "dtype": str(out.dtype).replace("torch.", "")}


# ------------------------------------------------------------------ spike_composite
def _S(vol: torch.Tensor, ret: torch.Tensor, d: int = 5, swap: bool = False, parts: bool = False):
    """S = |M - Q| built from the real kernels, exactly as the tree writes it."""
    log, fwd = _kernel("log"), _kernel("in_forward_valid_part")
    mean_full, std_full = _kernel("in_mean_full"), _kernel("in_stddev_full")
    is_gt, is_lt = _kernel("is_gt"), _kernel("is_lt")
    sustain, day_mean = _kernel("in_sustain_stddev"), _kernel("day_mean")
    e = log(vol)
    g = e - fwd(e)
    h, i = mean_full(g), std_full(g)
    k, o = is_gt(g, h + i), is_lt(g, h - i)
    if swap:
        k, o = o, k
    m = day_mean(sustain(k, ret, d)).double().reshape(-1)
    q = day_mean(sustain(o, ret, d)).double().reshape(-1)
    s = (m - q).abs()
    return (s, m, q, k, o) if parts else s


@probe("spike_composite",
       question="把 S=|M−Q| 用真实内核搭出来:孤立的一分钟放量在 j 触发『放量』、在 j+1 触发『缩量』,"
                "S 是否等于 0.4·||r_j|−|r_{j+5}||?收盘集合竞价那一格、零成交缺口、对 Ret / Volume 的齐次度、对换放量缩量是否对称?",
       applies=lambda s: _minute_keeps_m(s) and s.category == "pair_rolling")
def _spike(ctx: ProbeContext):
    T, j = 60, 20
    a, b = 0.03, 0.01

    def day(spike=10.0):
        v = torch.full((1, T), 1000.0, dtype=torch.float64)
        v[0, j] *= spike
        r = torch.zeros((1, T), dtype=torch.float64)
        r[0, j], r[0, j + 5] = a, -b
        return v, r

    v, r = day()
    s, m, q, k, o = _S(v, r, parts=True)
    surge = torch.nonzero(k[0] == 1).flatten().tolist()
    drop = torch.nonzero(o[0] == 1).flatten().tolist()
    want = 0.4 * abs(abs(a) - abs(b))
    out = {"surge_fires_at_j_plus": [x - j for x in surge], "drop_fires_at_j_plus": [x - j for x in drop],
           "S_over_analytic_0.4*||r_j|-|r_j+5||": round(float(s[0]) / want, 6),
           "M_over_0.4|r_j|": round(float(m[0]) / (0.4 * a), 6), "Q_over_0.4|r_j+5|": round(float(q[0]) / (0.4 * b), 6)}
    if abs(float(s[0]) / want - 1.0) > 1e-6:
        raise RuntimeError(f"self-check failed: isolated spike gave S = {float(s[0])}, analytic {want}")
    # homogeneity: Ret x3 -> S x3 ; Volume x7 -> S unchanged ; swapping the two masks -> S unchanged
    out["S(3*Ret)/S"] = round(float(_S(v, 3.0 * r)[0] / s[0]), 6)
    out["S(7*Volume)/S"] = round(float(_S(7.0 * v, r)[0] / s[0]), 6)
    out["S(swap surge,drop)/S"] = round(float(_S(v, r, swap=True)[0] / s[0]), 6)
    # only one side ever fires (a permanent step up in volume): is S NaN?
    v2 = torch.full((1, T), 1000.0, dtype=torch.float64)
    v2[0, j:] *= 10.0
    out["step_up_only(no drop trigger)"] = "nan" if bool(torch.isnan(_S(v2, r)[0])) else round(float(_S(v2, r)[0]), 6)
    # closing-auction-like end of row: two zero-volume minutes, then a big last minute
    v3, r3 = day()
    v3[0, T - 3:T - 1] = 0.0
    v3[0, T - 1] = 5000.0
    r3[0, T - 1] = 0.02
    s3, m3, q3, k3, o3 = _S(v3, r3, parts=True)
    out["closing_bar_fires_surge"] = bool(k3[0, T - 1] == 1)
    out["M_with_closing_bar_over_M_without"] = round(float(m3[0] / m[0]), 4)   # 0.5 = the closing trigger adds a zero
    # zero-volume gap right after the spike: the drop is measured against the last NON-ZERO minute
    v4, r4 = day()
    v4[0, j + 1:j + 3] = 0.0
    s4, m4, q4, k4, o4 = _S(v4, r4, parts=True)
    out["zero_gap_drop_fires_at_j_plus"] = [x - j for x in torch.nonzero(o4[0] == 1).flatten().tolist()]
    return out
