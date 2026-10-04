"""Probes this tree needs: abs_(cs_demean(day_skew(Low))).

The tree is "a moment of the intraday PRICE-LEVEL path -> minus the cross-sectional
mean -> magnitude".  None of the built-in probes answers what one needs to know
to read it:

* ``pinned_path_response`` -- day_skew is fed a price LEVEL, so it is a statistic
  of how long the price sat at each level (an occupancy distribution), not of
  returns.  What does it read on a day the price is pinned at one extreme for a
  fraction p of the minutes (a limit board, a one-jump day)?  Analytic answer for
  a two-point path: (1-2p)/sqrt(p(1-p)).
* ``constant_row_output`` -- a day whose price never moves (one-word limit board,
  no trades).  The kernel divides by the path's own std; is the output NaN, 0, or
  float garbage?  In float32, as the engine runs it.
* ``tick_grid_sensitivity`` -- does a coarse price grid (a low-priced stock moves
  over 3-5 ticks a day) inflate |output| by itself?  If so the factor would be a
  price-level artefact.
* ``common_path_share`` -- N stocks following "common path + own path": how does
  the mean of |skew_i - mean_j skew_j| move with the idiosyncratic share of the
  variance, and does it depend on the volatility level?  This is the composite
  the tree builds, measured with the real kernel.
* ``abs_reorders_after_shift`` -- for cs_demean: abs after a common shift is not
  the same ordering as abs alone; how fast does the ordering change with the size
  of the shift (in units of the cross-sectional std)?

Every probe carries a self-check on a kernel whose answer is known (day_mean,
day_std, day_kurt), reported under "selfcheck"; a probe whose self-check fails
must not be used to read day_skew.
"""

import math

import torch

from partura.probes import ProbeContext, is_cross_sectional, is_day_reducer, probe

M = 241


def _kernel(name):
    from alphacube.catalog import default_registry
    return default_registry()._ops[name].fn


def _day_unary(s):
    return is_day_reducer(s) and s.arity == 1 and not s.requires_window


def _two_point(p: float, lo: float = 10.0, hi: float = 11.0, rows: int = 4) -> torch.Tensor:
    """A path that sits at ``hi`` for a fraction p of the minutes and at ``lo`` otherwise."""
    n_hi = int(round(p * M))
    x = torch.full((rows, M), lo, dtype=torch.float64)
    x[:, M - n_hi:] = hi
    return x


@probe("pinned_path_response",
       question="价格在 p 比例的分钟里钉在最高位(其余在低位)时,输出是多少?(价格水平路径的占用分布)",
       applies=_day_unary)
def _pinned(ctx: ProbeContext):
    ps = (0.5, 0.8, 0.9, 0.98)
    out, analytic = {}, {}
    for p in ps:
        q = round(p * M) / M                       # the fraction actually realised on a 241 grid
        out[p] = round(float(ctx.call([_two_point(p)]).flatten()[0]), 3)
        analytic[p] = round((1 - 2 * q) / math.sqrt(q * (1 - q)), 3)
    # known answers: day_mean reads lo + q*(hi-lo); day_std reads sqrt(q(1-q))*(hi-lo).
    # (day_mean casts its input to float32 -- `C._mean(x.float())` -- so its tolerance is a float32 one.)
    mean_ok = all(abs(float(_kernel("day_mean")(_two_point(p)).flatten()[0]) - (10.0 + round(p * M) / M)) < 1e-5
                  for p in ps)
    std_ok = all(abs(float(_kernel("day_std")(_two_point(p)).flatten()[0])
                     - math.sqrt((round(p * M) / M) * (1 - round(p * M) / M))) < 1e-9 for p in ps)
    # mirror: pinned at the LOW for a fraction p
    mirror = round(float(ctx.call([21.0 - _two_point(0.9)]).flatten()[0]), 3)
    return {"output_by_p": out, "two_point_skew_analytic": analytic, "pinned_low_p0.9": mirror,
            "selfcheck": {"day_mean_reads_p": mean_ok, "day_std_reads_sqrt_pq": std_ok}}


@probe("constant_row_output",
       question="全天价格一动不动(一字板 / 无成交)时输出什么?float32 下是 NaN、0 还是舍入垃圾?",
       applies=_day_unary)
def _constant(ctx: ProbeContext):
    prices = [3.37, 5.01, 10.01, 27.3, 61.88, 123.45, 9.99, 14.56, 2.03, 48.17]
    res = {}
    for dtype, tag in ((torch.float32, "float32"), (torch.float64, "float64")):
        devs = ["cpu"] + (["cuda"] if torch.cuda.is_available() else [])
        for dev in devs:
            x = torch.tensor(prices, dtype=dtype, device=dev).reshape(-1, 1).repeat(1, M)
            y = ctx.call([x]).flatten().double().cpu()
            fin = torch.isfinite(y)
            res[f"{tag}/{dev}"] = {"finite_frac": round(float(fin.double().mean()), 2),
                                   "values": [round(float(v), 3) if math.isfinite(float(v)) else "nan" for v in y]}
    x32 = torch.tensor(prices, dtype=torch.float32).reshape(-1, 1).repeat(1, M)
    std = _kernel("day_std")(x32).flatten().double()
    mean = _kernel("day_mean")(x32).flatten().double()
    return {**res, "selfcheck": {"day_std_max_on_constant": float(std.max()),
                                 "day_mean_max_abs_err": float((mean - torch.tensor(prices, dtype=torch.float32).double()).abs().max())}}


def _walks(n: int, sigma: float, seed: int, tick: float = 0.0, p0: float = 10.0) -> torch.Tensor:
    g = torch.Generator().manual_seed(seed)
    r = torch.randn((n, M), generator=g, dtype=torch.float64) * sigma
    x = p0 * torch.exp(torch.cumsum(r, dim=1))
    return torch.round(x / tick) * tick if tick > 0 else x


@probe("tick_grid_sensitivity",
       question="价格网格变粗(低价股一天只在 3~5 个价位上跳)会不会单独把 |输出| 抬高?",
       applies=_day_unary)
def _tick(ctx: ProbeContext):
    sigma = 0.0008                                  # ~1.2% a day over 241 minutes
    out = {}
    for tick in (0.0, 0.01, 0.05, 0.10):            # on a 10-yuan path: continuous, 10bp, 50bp, 100bp grid
        x = _walks(3000, sigma, 7, tick=tick)
        y = ctx.call([x]).flatten().double()
        fin = torch.isfinite(y)
        levels = torch.tensor([float(torch.unique(row).numel()) for row in x[:300]]).mean()
        out[f"tick_{tick}"] = {"mean_abs": round(float(y[fin].abs().mean()), 3),
                               "finite_frac": round(float(fin.double().mean()), 3),
                               "avg_levels": round(float(levels), 1)}
    # known answer: the mean of the path does not care about a 1-tick grid
    a = _kernel("day_mean")(_walks(3000, sigma, 7)).flatten()
    b = _kernel("day_mean")(_walks(3000, sigma, 7, tick=0.05)).flatten()
    return {**out, "selfcheck": {"day_mean_max_shift_at_50bp_grid": round(float((a - b).abs().max()), 4)}}


@probe("common_path_share",
       question="N 只股票 = 共同路径 + 自有路径:|skew_i − 截面均值| 的均值怎样随「自有份额」变?随波动水平变不变?",
       applies=lambda s: _day_unary(s) and s.name == "day_skew")
def _common(ctx: ProbeContext):
    n, days = 300, 40
    out = {}
    for vol_mult in (1.0, 3.0):
        row = {}
        for share in (0.0, 0.25, 0.5, 0.75, 1.0):
            acc = []
            for d in range(days):
                g = torch.Generator().manual_seed(1000 + d)
                mkt = torch.randn((1, M), generator=g, dtype=torch.float64)
                own = torch.randn((n, M), generator=g, dtype=torch.float64)
                r = 0.0008 * vol_mult * (math.sqrt(1 - share) * mkt + math.sqrt(share) * own)
                x = 10.0 * (1.0 + torch.cumsum(r, dim=1))          # arithmetic path: exact affine copies at share 0
                sk = ctx.call([x]).flatten().double()
                acc.append(float((sk - sk.mean()).abs().mean()))
            row[share] = round(sum(acc) / len(acc), 4)
        out[f"vol_x{vol_mult:g}"] = row
    return {"mean_abs_dev_by_idio_share": out,
            "selfcheck": {"share0_is_zero": out["vol_x1"][0.0] < 1e-6,
                          "vol_free": abs(out["vol_x1"][1.0] - out["vol_x3"][1.0]) < 1e-6}}


@probe("abs_reorders_after_shift",
       question="先减去一个共同偏移再取绝对值,排序和直接取绝对值差多少?(偏移以截面标准差为单位)",
       applies=lambda s: is_cross_sectional(s) and s.name == "cs_demean")
def _reorder(ctx: ProbeContext):
    g = torch.Generator().manual_seed(5)
    z = torch.randn((60, 3000), generator=g, dtype=torch.float64)
    out = {}
    for mu in (0.0, 0.1, 0.25, 0.5, 1.0):
        x = z + mu
        a = ctx.call([x]).abs()
        out[mu] = round(sum(ctx.spearman(a[i], x[i].abs()) for i in range(60)) / 60, 3)
    return {"spearman(|x-mean|,|x|)_by_shift_in_sd": out, "selfcheck": {"shift0_is_one": out[0.0] > 0.995}}
