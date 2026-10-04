"""Probes this tree needs:  ES/VaR of the right tail of minute returns  minus  ES/VaR of the left tail.

    side(q) = [ sum(Ret beyond day_quantile(Ret, q)) / (count + 1e-6) ] / ( |day_quantile(Ret, q)| + 1e-6 )
    X       = side(0.95) - side(0.05)

Every operator in it is elementary (a quantile, a strict comparison, a where, a sum, a
ratio), so the per-operator built-in probes have nothing surprising to say.  What decides
how the tree reads real data is the COMPOSITE, and three things in it that a name cannot tell:

* which order statistic `day_quantile(., 0.95)` actually is on a 241-minute row, and what
  happens to it when one minute is missing (interpolation)        -> `quantile_order_statistic`
* the denominator is `quantile + 1e-6`.  Minute returns are full of exact zeros (a price that
  did not move), so on a day with fewer than ~5% up-minutes the 95% quantile is exactly 0 and
  the ratio becomes  ES x 1e6 .  Where is that knot, and how big is the jump?  -> `tail_ratio_knot`
* inside the regular regime the ratio is scale free; inside the blown-up regime it is NOT
  (it reads the SIZE of the few up-moves times 1e6)                -> `scale_degree_by_regime`
* how often does a tick grid alone put a stock into the blown-up regime (price level x
  volatility)?                                                     -> `tick_grid_regime_share`
* how much does ONE outlying minute (an opening gap, if Ret's first minute carries it)
  move the regular-regime value?                                   -> `single_minute_leverage`

The composite is built from the SERVER's own kernels (`alphacube.operators`), in float32 as
the engine runs it.  Every probe carries a self-check with a known answer under "selfcheck";
a probe whose self-check fails must not be used to read the tree.
"""

import math

import torch

from partura.probes import ProbeContext, probe

M = 241
EPS = 1e-6


def _mods():
    from alphacube.operators import common as C, dt_day as DD
    return C, DD


def _is_day_quantile(s) -> bool:
    return str(getattr(s, "name", "")).startswith("day_quantile") or "day_quantile" in str(getattr(s, "kernel_id", ""))


def side(r: torch.Tensor, q: float, eps: float = EPS):
    """One side of the tree, node by node as the expression writes it.
    Returns (ratio, expected_shortfall, quantile, count)."""
    C, DD = _mods()
    quant = DD.day_quantile(r, q)                                   # (rows, 1)
    zero = C.create_like(r, 0)
    if q > 0.5:
        mask = C.is_gt(r, quant)
        picked = C.select_where(mask, r, zero)
        qabs = quant
    else:
        mask = C.is_lt(r, quant)
        picked = C.select_where(mask, C.abs_(r), zero)
        qabs = C.abs_(quant)
    e = C.create_like(quant, eps)
    cnt = DD.day_sum(mask.to(r.dtype))                              # the engine hands the 0/1 mask on as a float
    es = C.div(DD.day_sum(picked.to(r.dtype)), C.add(cnt, e))
    return C.div(es, C.add(qabs, e)), es, quant, cnt


def tree(r: torch.Tensor, eps: float = EPS) -> torch.Tensor:
    return (side(r, 0.95, eps)[0] - side(r, 0.05, eps)[0]).flatten()


def _gauss(rows: int, sigma: float = 0.001, seed: int = 0) -> torch.Tensor:
    g = torch.Generator().manual_seed(seed)
    return (torch.randn((rows, M), generator=g, dtype=torch.float64) * sigma).float()


def _sparse(k_up: int, k_dn: int, tick: float = 0.002, rows: int = 4, drop_first: bool = False) -> torch.Tensor:
    """A tick-constrained day: k_up minutes of about +tick, k_dn minutes of about -tick, the rest exactly 0.
    Sizes differ by 1% steps (a tick is a slightly different return at each price level)."""
    x = torch.zeros((rows, M), dtype=torch.float32)
    for j in range(k_up):
        x[:, 5 + 2 * j] = tick * (1.0 + 0.01 * j)
    for j in range(k_dn):
        x[:, 6 + 2 * j] = -tick * (1.0 + 0.01 * j)
    if drop_first:
        x[:, 0] = float("nan")
    return x


# ------------------------------------------------------------------ 1. which order statistic
@probe("quantile_order_statistic",
       question="241 个分钟的一行上,这个分位数读的是第几个顺序统计量?少一个分钟(240 个有效值)时是不是插值?",
       applies=_is_day_quantile)
def _qpos(ctx: ProbeContext):
    C, DD = _mods()
    ramp = torch.arange(M, dtype=torch.float32).reshape(1, M).repeat(3, 1)
    full = float(ctx.call([ramp]).flatten()[0])
    holed = ramp.clone()
    holed[:, 0] = float("nan")                                       # first minute missing -> 240 valid values 1..240
    part = float(ctx.call([holed]).flatten()[0])
    med = float(DD.day_quantile(ramp, 0.5).flatten()[0])
    mx = float(DD.day_max(ramp).flatten()[0])
    return {"position_on_ramp_0..240": round(full, 4),
            "position_with_first_minute_missing(values 1..240)": round(part, 4),
            "is_exact_order_statistic_at_241": abs(full - round(full)) < 1e-4,
            "is_interpolated_at_240": abs(part - round(part)) > 1e-3,
            "selfcheck": {"median_of_ramp_is_120": abs(med - 120.0) < 1e-4, "max_of_ramp_is_240": abs(mx - 240.0) < 1e-4}}


# ------------------------------------------------------------------ 2. the knot
@probe("tail_ratio_knot",
       question="一天里只有 k 个上涨分钟(其余为 0)时,右侧 ES/(q95+1e-6) 读多少?结在第几个 k?",
       applies=_is_day_quantile)
def _knot(ctx: ProbeContext):
    out241, out240 = {}, {}
    for k in (0, 1, 6, 11, 12, 13, 14, 24, 60):
        out241[k] = round(float(side(_sparse(k, 40), 0.95)[0].flatten()[0]), 3)
        out240[k] = round(float(side(_sparse(k, 40, drop_first=True), 0.95)[0].flatten()[0]), 3)
    # mirror: k DOWN-minutes, the left side
    left = {k: round(float(side(_sparse(40, k), 0.05)[0].flatten()[0]), 3) for k in (1, 12, 13, 24)}
    # the whole tree on the four corner cases (up-sparse, down-sparse, both sparse, neither)
    corners = {"up_sparse(5 up,40 dn)": round(float(tree(_sparse(5, 40))[0]), 2),
               "dn_sparse(40 up,5 dn)": round(float(tree(_sparse(40, 5))[0]), 2),
               "both_sparse(5 up,5 dn)": round(float(tree(_sparse(5, 5))[0]), 2),
               "neither(40 up,40 dn)": round(float(tree(_sparse(40, 40))[0]), 3),
               "price_never_moves": round(float(tree(_sparse(0, 0))[0]), 3)}
    # known answers: Gaussian minutes -> ES/VaR at 95% is phi(z)/(0.05 z) = 1.254 on both sides, tree ~ 0
    r = _gauss(4000, seed=11)
    R, L = side(r, 0.95)[0].flatten().double(), side(r, 0.05)[0].flatten().double()
    z = 1.6448536
    analytic = math.exp(-0.5 * z * z) / math.sqrt(2 * math.pi) / 0.05 / z
    # Is the tree odd in Ret?  In exact arithmetic it is (the two sides are mirror images).  In float32 the
    # 0.95-quantile position 0.95 * 240 lands a hair BELOW 228, so the "quantile" is a hair below the 229th
    # order statistic and the strict `>` keeps that observation: the right tail averages 13 minutes, the left 12.
    cnt_r32, cnt_l32 = float(side(r, 0.95)[3].flatten().median()), float(side(r, 0.05)[3].flatten().median())
    r64 = r.double()
    cnt_r64, cnt_l64 = float(side(r64, 0.95)[3].flatten().median()), float(side(r64, 0.05)[3].flatten().median())
    gap32 = float((tree(r).double() + tree(-r).double()).abs().max())
    gap64 = float((tree(r64) + tree(-r64)).abs().max())
    return {"right_ratio_by_k_up(241 valid)": out241, "right_ratio_by_k_up(240 valid)": out240,
            "left_ratio_by_k_dn(241 valid)": left, "tree_on_corner_cases": corners,
            "gaussian_mean_right": round(float(R.mean()), 4), "gaussian_mean_left": round(float(L.mean()), 4),
            "gaussian_sd_of_tree": round(float((R - L).std()), 4),
            "tail_minutes_float32(right,left)": [cnt_r32, cnt_l32],
            "tail_minutes_float64(right,left)": [cnt_r64, cnt_l64],
            "max_abs(tree(r)+tree(-r))_float32": round(gap32, 4),
            "selfcheck": {"gaussian_right_near_1.254": abs(float(R.mean()) - analytic) < 0.08,
                          "gaussian_left_near_1.254": abs(float(L.mean()) - analytic) < 0.08,
                          "tree_is_odd_in_float64": gap64 < 1e-3}}


# ------------------------------------------------------------------ 3. scale
@probe("scale_degree_by_regime",
       question="把分钟收益整体放大 c 倍:常规区间里整棵树变不变?分母塌掉的区间里呢?",
       applies=_is_day_quantile)
def _scale(ctx: ProbeContext):
    C, DD = _mods()
    reg = _gauss(500, seed=3)
    deg = _sparse(5, 40, rows=8)
    res = {}
    for c in (2.0, 4.0):
        a, b = tree(reg).double(), tree(reg * c).double()
        res[f"regular_max_abs_change_c{c:g}"] = round(float((a - b).abs().max()), 5)
        d0, d1 = tree(deg).double(), tree(deg * c).double()
        res[f"blown_up_ratio_c{c:g}"] = round(float((d1 / d0).mean()), 4)
    s0 = DD.day_std(reg).flatten().double()
    s2 = DD.day_std(reg * 2.0).flatten().double()
    return {**res, "selfcheck": {"day_std_has_degree_1": bool(torch.allclose(s2, 2.0 * s0, rtol=1e-4)),
                                 "regular_is_scale_free": res["regular_max_abs_change_c2"] < 0.02}}


# ------------------------------------------------------------------ 4. tick grid
def _tick_paths(rows: int, p0: float, sigma: float, seed: int, tick: float = 0.01) -> torch.Tensor:
    """Minute returns of a geometric random walk observed on a `tick` price grid (first minute = 0)."""
    g = torch.Generator().manual_seed(seed)
    z = torch.randn((rows, M), generator=g, dtype=torch.float64) * sigma
    p = p0 * torch.exp(torch.cumsum(z, dim=1))
    if tick > 0:
        p = torch.round(p / tick) * tick
    prev = torch.cat([torch.full((rows, 1), p0, dtype=torch.float64), p[:, :-1]], dim=1)
    return (p / prev - 1.0).float()


@probe("tick_grid_regime_share",
       question="只因为价格网格(低价 × 低波动),一只股票有多大比例的日子掉进「分母塌掉」的区间?",
       applies=_is_day_quantile)
def _tick(ctx: ProbeContext):
    out = {}
    for sigma, tag in ((0.0008, "vol~1.2%/day"), (0.0004, "vol~0.6%/day")):
        row = {}
        for p0 in (2.0, 3.0, 5.0, 10.0, 30.0):
            r = _tick_paths(1500, p0, sigma, seed=int(p0 * 10))
            R, L = side(r, 0.95)[0].flatten(), side(r, 0.05)[0].flatten()
            x = (R - L).double()
            row[f"price_{p0:g}"] = {"right_blown": round(float((R >= 500).float().mean()), 3),
                                    "left_blown": round(float((L >= 500).float().mean()), 3),
                                    "any_side_ge5": round(float(((R >= 5) | (L >= 5)).float().mean()), 3),
                                    "median_abs_tree": round(float(x.abs().median()), 2)}
        out[tag] = row
    cont = _tick_paths(1500, 10.0, 0.0008, seed=5, tick=0.0)
    Rc = side(cont, 0.95)[0].flatten()
    return {**out, "selfcheck": {"continuous_price_never_blows_up": float((Rc >= 5).float().mean()) == 0.0,
                                 "continuous_right_ratio_near_1.25": abs(float(Rc.mean()) - 1.254) < 0.1}}


# ------------------------------------------------------------------ 5. one outlying minute
@probe("single_minute_leverage",
       question="常规区间里,一个分钟的离群收益(比如开盘跳空 g 倍分钟波动)能把整棵树推多远?",
       applies=_is_day_quantile)
def _lever(ctx: ProbeContext):
    sigma = 0.001
    base = _gauss(3000, sigma, seed=21)
    out = {}
    for g in (0.0, 3.0, 5.0, 10.0, 20.0, -10.0):
        r = base.clone()
        r[:, 0] = g * sigma
        out[g] = round(float(tree(r).double().mean()), 3)
    z = 1.6448536
    # the gap replaces one of the ~12 tail minutes: d(tree) ~ (g - E[tail]) / (12 * z), E[tail] ~ 2.06 sigma
    approx = {g: round((g - 2.06) / (12 * z), 3) for g in (5.0, 10.0, 20.0)}
    sd = round(float(tree(base).double().std()), 3)
    return {"mean_tree_by_gap_in_sigma": out, "first_order_estimate": approx, "sd_of_tree_without_gap": sd,
            "selfcheck": {"no_gap_is_centred": abs(out[0.0]) < 0.03,
                          "mirror_gap_flips_sign": abs(out[10.0] + out[-10.0]) < 0.05}}


def selfcheck_report() -> None:
    """Print every probe's value and self-check with whatever kernels this interpreter imports."""
    from alphacube.catalog import default_registry
    from partura.probes import run_probes
    reg = default_registry()
    spec = reg._ops.get("day_quantile")
    caller = lambda args: _mods()[1].day_quantile(args[0], 0.95)      # noqa: E731
    res = run_probes(spec, only=["quantile_order_statistic", "tail_ratio_knot", "scale_degree_by_regime",
                                 "tick_grid_regime_share", "single_minute_leverage"], caller=caller, n_operands=1)
    for name, r in res.items():
        if not r.get("applicable"):
            print(f"[selfcheck] {name}: not applicable to {getattr(spec, 'name', spec)}")
            continue
        if "error" in r:
            print(f"[selfcheck] {name}: ERROR {r['error']}")
            continue
        sc = r["value"].get("selfcheck", {})
        flags = [v for v in sc.values() if isinstance(v, bool)]
        print(f"[selfcheck] {name:<26} {'PASS' if all(flags) else 'FAIL'}  {sc}")
        for k, v in r["value"].items():
            if k != "selfcheck":
                print(f"            {k}: {v}")


if __name__ == "__main__":
    selfcheck_report()
