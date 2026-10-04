"""Probes this tree needs:  day_max(pow_1_5(pow_2(nt_ts_kurt(Close, 30)))).

Read by name it says "the day's maximum of a 30-DAY time-series kurtosis of the close".
Read by kernel it is something else, and the built-in probes cannot say what:

* `nt_ts_kurt` is the ND kernel `ts_kurt` put on the NT face.  The kernel rolls along
  axis 0 of whatever it is handed; on the NT face the engine hands it one day's
  (minute x stock) slab, so the window is 30 MINUTES inside one day, left-padded with
  NaN (no look-back across days).  The first minutes of every day therefore see windows
  of 1, 2, 3 ... points.                                   -> `partial_window_values`
* the kernel is `m4 / (var**2 + EPS) - 3` with a fixed EPS.  On a PRICE LEVEL in yuan
  `var**2` of a quiet 30-minute window is of the order of EPS, so the statistic is not
  scale-free: it is pulled towards -3 when the window's price variance is small.
                                                           -> `kurt_eps_knee`
* which price paths make it large: an isolated jump after a quiet stretch.  How fast
  does a level shift age out of the statistic, and how big must a jump be against the
  background noise?                                        -> `jump_response`
* the composite (`pow_2` folds the sign of an EXCESS kurtosis, `pow_1_5` restores a
  monotone cube, `day_max` keeps the largest):  on synthetic stocks that share the SAME
  return dynamics and differ only in price level (tick = 0.01), what does the tree read?
                                                           -> `tree_by_price_level`

Every probe carries a self-check on a case whose answer is known analytically, reported
under "selfcheck"; a probe whose self-check fails must not be used to read the tree.
"""

import math

import torch

from partura.probes import ProbeContext, is_day_reducer, probe

M = 241


def _kernel(name):
    from alphacube.catalog import default_registry
    return default_registry()._ops[name].fn


def _is_roll_kurt(s):
    return bool(s.requires_window) and "kurt" in str(s.kernel_id)


def _is_day_max(s):
    return is_day_reducer(s) and s.name == "day_max"


def _two_level(delta: float, n: int = 90, p0: float = 10.0, dtype=torch.float64) -> torch.Tensor:
    """(n, 1) column alternating p0, p0+delta: every full even window is a 50/50 two-point
    distribution, whose scale-free kurtosis is exactly 1 (excess -2)."""
    col = torch.full((n, 1), p0, dtype=dtype)
    col[1::2, 0] = p0 + delta
    return col


# ------------------------------------------------------------------ 1. the EPS knee
@probe("kurt_eps_knee",
       question="峰度核在多小的输入尺度下不再是无量纲的?(两点 50/50 分布,真峰度恒为 1;按价差 δ 读输出)",
       applies=_is_roll_kurt)
def _knee(ctx: ProbeContext):
    w = int(ctx.window or 30)
    out, eps = {}, []
    for delta in (0.01, 0.02, 0.03, 0.05, 0.10, 1.0):
        k = float(ctx.call([_two_level(delta)])[-1, 0])
        var = (delta / 2.0) ** 2
        f = k + 3.0                                    # = var^2 / (var^2 + EPS) when the true kurtosis is 1
        out[f"delta_{delta}"] = round(k, 4)
        if 0.0 < f < 0.999:
            eps.append(var * var * (1.0 - f) / f)
    eps_hat = sum(eps) / len(eps) if eps else float("nan")
    # float32, the cube's dtype
    k32 = float(ctx.call([_two_level(0.01, dtype=torch.float32)])[-1, 0])
    # one-tick blip in an otherwise flat 30-minute window: scale-free answer is (n^2-3n+3)/(n-1) - 3
    blip = torch.full((3 * w, 1), 10.0, dtype=torch.float64)
    blip[2 * w, 0] = 10.01
    k_blip = float(ctx.call([blip])[2 * w, 0])
    blip_big = blip.clone()
    blip_big[2 * w, 0] = 11.0
    k_blip_big = float(ctx.call([blip_big])[2 * w, 0])
    analytic = (w * w - 3 * w + 3) / (w - 1) - 3.0
    # known answer on a scale-free kernel: day_kurt (C._kurt, plain division) must read -2 at every delta
    dk = _kernel("day_kurt")
    free = [float(dk(_two_level(d, n=w).T)[0, 0]) for d in (0.01, 0.05, 1.0)]
    return {
        **out,
        "implied_EPS": float(f"{eps_hat:.3e}"),
        "delta_at_half_damping": round(2.0 * eps_hat ** 0.25, 5) if eps_hat == eps_hat else None,
        "two_level_delta_0.01_float32": round(k32, 4),
        "one_tick_blip_in_flat_window": round(k_blip, 4),
        "one_yuan_blip_in_flat_window": round(k_blip_big, 4),
        "selfcheck": {
            "large_scale_two_level_reads_-2": abs(out["delta_1.0"] + 2.0) < 1e-4,
            "implied_EPS_constant_across_delta": (max(eps) / min(eps) < 1.01) if eps else False,
            "big_blip_matches_analytic_(n^2-3n+3)/(n-1)-3": abs(k_blip_big - analytic) < 1e-3,
            "scale_free_day_kurt_reads_-2_at_all_delta": all(abs(v + 2.0) < 1e-6 for v in free),
        },
    }


# ------------------------------------------------------------------ 2. the start of the day
@probe("partial_window_values",
       question="每天开头不足一个窗口的那些分钟,输出是什么?(NT 面逐日调用、左侧补 NaN,窗口从 1 个点长起)",
       applies=_is_roll_kurt)
def _partial(ctx: ProbeContext):
    g = torch.Generator().manual_seed(5)
    steps = torch.randn((M, 200), generator=g, dtype=torch.float64)
    x = 50.0 + torch.cumsum(0.03 * steps, dim=0)          # a yuan-scale Gaussian walk (3 ticks a minute)
    y = ctx.call([x])
    r0, r1, r2 = y[0], y[1], y[2]
    absmax = y.abs().nan_to_num(nan=-1.0).max(dim=0).values          # the tree's day_max(|K|)
    floor_hit = float(((absmax - r1.abs()).abs() < 1e-9).double().mean())
    # equal first two closes: the 2-point window has zero variance -> NaN, the floor moves to the first change
    x2 = x.clone()
    x2[1] = x2[0]
    y2 = ctx.call([x2])
    # known answers need a scale at which EPS is invisible: the same walk in units 1000x larger
    big = ctx.call([5.0e7 + torch.cumsum(3.0e4 * steps, dim=0)])
    return {
        "row0_all_nan": bool(torch.isnan(r0).all()),
        "row1_range(yuan_scale)": [round(float(r1[torch.isfinite(r1)].min()), 4),
                                   round(float(r1[torch.isfinite(r1)].max()), 4)],
        "row2_range(yuan_scale)": [round(float(r2[torch.isfinite(r2)].min()), 4),
                                   round(float(r2[torch.isfinite(r2)].max()), 4)],
        "share_of_days_whose_max_abs_K_is_the_2pt_opening_window(gaussian_walk)": round(floor_hit, 3),
        "median_day_max_abs_K(gaussian_walk)": round(float(absmax.median()), 3),
        "row1_when_first_two_closes_equal": "nan" if bool(torch.isnan(y2[1]).all()) else "finite",
        "selfcheck": {
            "two_points_read_-2": bool(((big[1] + 2.0).abs() < 1e-4).all()),      # any 2 distinct points: kurtosis 1
            "three_points_read_-1.5": bool(((big[2] + 1.5).abs() < 1e-4).all()),  # any 3 points: kurtosis 1.5
        },
    }


# ------------------------------------------------------------------ 3. what a jump does
def _shift_path(k_new: int, w: int, jump: float, noise: float, cols: int, seed: int) -> torch.Tensor:
    """(w, cols): w - k_new minutes at 20, then k_new minutes at 20 + jump, plus iid noise."""
    g = torch.Generator().manual_seed(seed)
    x = torch.full((w, cols), 20.0, dtype=torch.float64)
    x[w - k_new:] += jump
    if noise > 0:
        x = x + noise * torch.randn((w, cols), generator=g, dtype=torch.float64)
    return x


@probe("jump_response",
       question="一次水平跳变进入窗口后,峰度读数随「新水平上的分钟数」怎么衰减?跳变要比背景噪声大多少才读得出来?",
       applies=_is_roll_kurt)
def _jump(ctx: ProbeContext):
    w = int(ctx.window or 30)
    aged = {}
    for k_new in (1, 2, 3, 4, 5, 6, 10, 15):
        aged[f"minutes_at_new_level_{k_new}"] = round(float(ctx.call([_shift_path(k_new, w, 1.0, 0.0, 1, 0)])[-1, 0]), 3)
    snr = {}
    for ratio in (1, 2, 3, 5, 10, 20):
        y = ctx.call([_shift_path(1, w, float(ratio) * 0.05, 0.05, 2000, 7)])[-1]
        snr[f"jump_over_noise_sd_{ratio}"] = round(float(y.median()), 3)
    p = lambda k: k / w
    an = lambda k: (1 - 3 * p(k) * (1 - p(k))) / (p(k) * (1 - p(k))) - 3.0
    return {
        "level_shift_aging": aged,
        "fresh_jump_vs_background_noise(median)": snr,
        # a shift reads > 3 twice: right after it (new level is the minority) and again ~w minutes later,
        # when the last 1-3 old-level minutes are about to leave the window (old level is the minority)
        "minutes_above_3_right_after_a_shift": int(sum(1 for k in range(1, w // 2) if an(k) > 3.0)),
        "echo_minutes_above_3_as_the_shift_leaves_the_window": int(sum(1 for k in range(w // 2, w) if an(k) > 3.0)),
        "selfcheck": {
            "aging_matches_two_point_formula": all(
                abs(aged[f"minutes_at_new_level_{k}"] - an(k)) < 5e-3 for k in (1, 2, 3, 4, 5, 6, 10, 15)),
            "pure_noise_window_is_near_0": abs(float(ctx.call([_shift_path(1, w, 0.0, 0.05, 4000, 9)])[-1].mean())
                                               - (-6.0 / (w + 1))) < 0.15,       # E[g2] of a normal sample ~ -6/(n+1)
        },
    }


# ------------------------------------------------------------------ 4. the composite, by price level
@probe("tree_by_price_level",
       question="整棵树 day_max(|K30|^3) 在「收益过程完全相同、只有价格水平不同(tick=0.01)」的合成股票上读出什么?",
       applies=_is_day_max)
def _tree(ctx: ProbeContext):
    kurt, p2, p15 = _kernel("nt_ts_kurt"), _kernel("pow_2"), _kernel("pow_1_5")
    S = 600
    g = torch.Generator().manual_seed(17)
    # minute log-returns: 0.08% sd, Student-t(4)-like tails -- identical for every price level
    z = torch.randn((M, S), generator=g, dtype=torch.float64)
    chi = (torch.randn((M, S, 4), generator=g, dtype=torch.float64) ** 2).sum(-1) / 4.0
    r = 0.0008 * z / chi.sqrt() / math.sqrt(2.0)
    r[0] = 0.0
    path = torch.exp(torch.cumsum(r, dim=0))
    out = {}
    for price in (2.0, 5.0, 10.0, 20.0, 50.0, 200.0):
        px = (torch.round(price * path * 100.0) / 100.0).to(torch.float32)       # tick-rounded, the cube's dtype
        k = kurt(px, 30)                                                         # (M, S), rolling along minutes
        kmax = k.nan_to_num(nan=-9.0).max(dim=0).values
        kmin = k.nan_to_num(nan=9.0).min(dim=0).values
        d = ctx.call([p15(p2(k)).T.contiguous()]).flatten()                      # the tree: day_max over minutes
        root = d.double() ** (1.0 / 3.0)
        ok = torch.isfinite(root)
        out[f"price_{price:g}"] = {
            "median_max_abs_K": round(float(root[ok].median()), 3),
            "share_fold_active(|Kmin|>Kmax)": round(float(((-kmin) > kmax)[ok].double().mean()), 3),
            "share_Kmin_below_-2.05(EPS_damped)": round(float((kmin < -2.05)[ok].double().mean()), 3),
            "share_Kmax_above_3": round(float((kmax > 3.0)[ok].double().mean()), 3),
        }
    # known answer: flat at 20 with one 1-yuan one-minute spike at minute 100 -> 29 flat + 1 outlier
    flat = torch.full((M, 1), 20.0, dtype=torch.float32)
    flat[100, 0] = 21.0
    d1 = float(ctx.call([p15(p2(kurt(flat, 30))).T.contiguous()]).flatten()[0])
    expect = ((30 * 30 - 3 * 30 + 3) / 29.0 - 3.0) ** 3
    # an opening gap followed by a dead-flat half hour is the same 29 + 1 window, read at minute 29
    gap = torch.full((M, 1), 20.5, dtype=torch.float32)
    gap[0, 0] = 20.0
    d2 = float(ctx.call([p15(p2(kurt(gap, 30))).T.contiguous()]).flatten()[0])
    # a day with exactly two distinct closes at the open and nothing else reads the fold's floor, 2^3 = 8
    two = torch.full((2, 1), 20.0, dtype=torch.float32)
    two[1, 0] = 20.5
    d3 = float(ctx.call([p15(p2(kurt(two, 30))).T.contiguous()]).flatten()[0])
    return {**out, "selfcheck": {
        "single_spike_reads_((n^2-3n+3)/(n-1)-3)^3": abs(d1 / expect - 1.0) < 1e-3,
        "single_spike_value": round(d1, 1),
        "opening_gap_then_flat_reads_the_same": abs(d2 / expect - 1.0) < 1e-3,
        "two_point_window_reads_8_after_the_fold": abs(d3 - 8.0) < 1e-2,
    }}
