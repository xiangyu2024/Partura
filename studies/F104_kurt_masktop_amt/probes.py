"""Probes this tree needs:  day_kurt(nt_cs_mask_top_replace_mean_neg(abs_(Amt))).

Read by name it says "kurtosis of intraday turnover after masking the top".
Read by kernel it is something else, and the built-in probes cannot say what:

* `nt_cs_mask_top_replace_mean_neg` works per MINUTE across STOCKS and overwrites the
  LOWEST 10% of the cross-section with that minute's cross-sectional MEAN.  Two things
  decide what that does to one stock's intraday series:
    - WHICH cells are overwritten when the row has ties.  Minute turnover ties all the
      time (zero-trade minutes).  The kernel ranks with a stable ordinal sort, so a tie
      is broken by COLUMN INDEX -- i.e. by stock code.     -> `tie_break_replaced_set`
    - WHAT they are overwritten with, relative to the stock's own level.  Turnover is
      right-skewed across stocks, so "the cross-sectional mean" is a value tens to
      hundreds of times an illiquid stock's own minute.     -> `replacement_vs_own_level`
* `day_kurt` then collapses 241 minutes.  If k of them were overwritten with a value far
  above the stock's own level, the kurtosis stops measuring "tail shape of the stock's
  own turnover" and becomes a NON-MONOTONE meter of k.     -> `spike_count_response`
* The composite on a synthetic market (stocks that differ only in liquidity level, no
  other structure): what does the tree read by liquidity decile?  -> `composite_by_liquidity`

Every probe carries a self-check on a case whose answer is known analytically, reported
under "selfcheck"; a probe whose self-check fails must not be used to read the tree.
"""

import math

import torch

from partura.probes import ProbeContext, is_cross_sectional, is_day_reducer, probe

M = 241


def _kernel(name):
    from alphacube.catalog import default_registry
    return default_registry()._ops[name].fn


def _is_mask(s):
    return is_cross_sectional(s) and s.arity == 1 and "mask_top_replace" in s.name


def _day_unary(s):
    return is_day_reducer(s) and s.arity == 1 and not s.requires_window


# ------------------------------------------------------------------ 1. ties
@probe("tie_break_replaced_set",
       question="一行里有并列(比如 30% 的股票这一分钟成交额为 0)时,被替换的是哪些格子?并列靠什么破?",
       applies=_is_mask)
def _ties(ctx: ProbeContext):
    n = 200
    neg = ctx.spec.name.endswith("_neg")
    g = torch.Generator().manual_seed(3)
    base = torch.rand((1, n), generator=g, dtype=torch.float64) + 1.0          # distinct, in (1, 2)
    perm = torch.randperm(n, generator=g)
    res = {}
    for frac in (0.05, 0.30):
        tied = perm[: int(n * frac)]
        x = base.clone()
        x[0, tied] = 0.0 if neg else 5.0            # the extreme the operator targets
        y = ctx.call([x])
        changed = torch.nonzero((y - x).abs()[0] > 1e-12).flatten()
        tied_sorted = torch.sort(tied).values
        ch_tied = torch.tensor([int(i) for i in changed if int(i) in set(tied.tolist())])
        n_top = math.ceil(n * 0.1)
        if len(ch_tied) == len(tied):
            which = "all tied cells"
        elif len(ch_tied) == 0:
            which = "none of the tied cells"
        elif set(ch_tied.tolist()) == set(tied_sorted[-len(ch_tied):].tolist()):
            which = "HIGHEST column index among the tied"
        elif set(ch_tied.tolist()) == set(tied_sorted[: len(ch_tied)].tolist()):
            which = "LOWEST column index among the tied"
        else:
            which = "neither end (mixed)"
        res[f"tied_frac_{frac}"] = {"n_tied": int(len(tied)), "n_changed": int(len(changed)),
                                    "n_changed_expected_ceil(0.1n)": n_top,
                                    "changed_among_tied": int(len(ch_tied)), "which": which}
    # known answer, tie-free row: exactly the ceil(0.1 n) extreme cells change, each to the row mean
    y = ctx.call([base])
    ch = torch.nonzero((y - base).abs()[0] > 1e-12).flatten()
    k = math.ceil(n * 0.1)
    order = torch.argsort(base[0], descending=not neg)
    ok_set = set(ch.tolist()) == set(order[:k].tolist())
    ok_val = bool(((y[0, ch] - base.mean()).abs() < 1e-9).all())
    return {**res, "selfcheck": {"tie_free_changes_exactly_the_extreme_decile": ok_set,
                                 "replacement_is_row_mean_incl_replaced_cells": ok_val}}


# ------------------------------------------------------------------ 2. replacement vs own level
@probe("replacement_vs_own_level",
       question="被替换成的截面均值,是被替换股票自己水平的多少倍?(截面对数正态,σ 取 1.0/1.5/2.0)",
       applies=_is_mask)
def _ratio(ctx: ProbeContext):
    neg = ctx.spec.name.endswith("_neg")
    out = {}
    for sigma in (1.0, 1.5, 2.0):
        g = torch.Generator().manual_seed(11)
        x = torch.exp(sigma * torch.randn((50, 4000), generator=g, dtype=torch.float64))
        y = ctx.call([x])
        ch = (y - x).abs() > 1e-12
        ratio = (y[ch] / x[ch])
        out[f"sigma_{sigma}"] = {"changed_frac": round(float(ch.double().mean()), 4),
                                 "median_new_over_old": round(float(ratio.median()), 3),
                                 "p10_new_over_old": round(float(ratio.quantile(0.1)), 3)}
    # known answer for a lognormal: mean = exp(s^2/2); the median of the bottom decile sits at the 5th
    # percentile exp(-1.645 s), so new/old ~ exp(s^2/2 + 1.645 s) for the _neg (bottom) variant, and the
    # top decile's median is exp(+1.645 s) so new/old ~ exp(s^2/2 - 1.645 s) for the top variant.
    s = 1.5
    expect = math.exp(s * s / 2 + (1.645 if neg else -1.645) * s)
    got = out["sigma_1.5"]["median_new_over_old"]
    return {**out, "selfcheck": {"lognormal_sigma1.5_expected_ratio": round(expect, 3),
                                 "within_10pct": abs(got / expect - 1) < 0.10,
                                 "changed_frac_is_0.1": abs(out["sigma_1.5"]["changed_frac"] - 0.1) < 0.002}}


# ------------------------------------------------------------------ 3. spike count -> kurtosis
def _spiky(k: int, ratio: float, noise: float, rows: int = 400, seed: int = 0) -> torch.Tensor:
    g = torch.Generator().manual_seed(seed)
    x = torch.exp(noise * torch.randn((rows, M), generator=g, dtype=torch.float64)) if noise > 0 \
        else torch.ones((rows, M), dtype=torch.float64)
    if k > 0:
        x[:, :k] = ratio * (math.exp(noise * noise / 2) if noise > 0 else 1.0)
    return x


@probe("spike_count_response",
       question="241 分钟里有 k 分钟被换成自身水平 R 倍的值,输出随 k 怎么变?(是不是一个非单调的「个数计」)",
       applies=_day_unary)
def _spikes(ctx: ProbeContext):
    ks = (0, 1, 2, 5, 12, 24, 60, 120, 180, 217, 236, 240)
    out = {}
    for ratio in (10.0, 50.0):
        out[f"R={ratio:g},own_noise_sigma=0.8"] = {
            k: round(float(ctx.call([_spiky(k, ratio, 0.8)]).flatten().median()), 2) for k in ks}
    pure = {k: round(float(ctx.call([_spiky(k, 50.0, 0.0, rows=2)]).flatten()[0]), 3) for k in ks if k > 0}
    # known answers on the pure two-point input (k cells at R, the rest at 1):
    #   day_kurt = 1/(w(1-w)) - 6 with w = k/M;   day_mean = 1 + w (R - 1)
    kurt = _kernel("day_kurt")
    mean = _kernel("day_mean")
    ok_k = all(abs(float(kurt(_spiky(k, 50.0, 0.0, rows=2)).flatten()[0]) - (1 / ((k / M) * (1 - k / M)) - 6)) < 1e-6
               for k in ks if k > 0)
    ok_m = all(abs(float(mean(_spiky(k, 50.0, 0.0, rows=2)).flatten()[0]) - (1 + k / M * 49.0)) < 1e-4
               for k in ks if k > 0)
    return {**out, "pure_two_point(R=50,no_noise)": pure,
            "selfcheck": {"day_kurt_matches_1/(w(1-w))-6": ok_k, "day_mean_matches_1+w(R-1)": ok_m}}


# ------------------------------------------------------------------ 4. the composite on a synthetic market
@probe("composite_by_liquidity",
       question="合成市场(股票只在流动性水平上不同,日内各分钟独立同分布):先做本算子再取 day_kurt,按流动性十分位读到什么?",
       applies=_is_mask)
def _composite(ctx: ProbeContext):
    n = 2000
    g = torch.Generator().manual_seed(21)
    level = torch.exp(1.5 * torch.randn((n,), generator=g, dtype=torch.float64))     # stock liquidity level
    x = level[None, :] * torch.exp(0.8 * torch.randn((M, n), generator=g, dtype=torch.float64))  # (minutes, stocks)
    kurt = _kernel("day_kurt")
    y = ctx.call([x])                                           # NT face: rows = minutes, columns = stocks
    k = ((y - x).abs() > 1e-12).double().sum(0)                 # minutes overwritten, per stock
    kb = kurt(y.transpose(0, 1).contiguous()).flatten()         # the tree
    kn = kurt(x.transpose(0, 1).contiguous()).flatten()         # the same statistic without the mask node
    order = torch.argsort(level)
    dec = {}
    for d in range(10):
        idx = order[d * n // 10:(d + 1) * n // 10]
        dec[f"liq_decile_{d + 1}"] = {"minutes_overwritten": round(float(k[idx].mean()), 1),
                                      "tree_kurt_median": round(float(kb[idx].median()), 2),
                                      "plain_kurt_median": round(float(kn[idx].median()), 2)}
    untouched = k == 0
    same = bool(((kb[untouched] - kn[untouched]).abs() < 1e-9).all())
    return {**dec,
            "spearman(tree, plain) over all stocks": round(ctx.spearman(kb, kn), 3),
            "spearman(tree, liquidity level)": round(ctx.spearman(kb, level), 3),
            "spearman(plain, liquidity level)": round(ctx.spearman(kn, level), 3),
            "selfcheck": {"untouched_stocks_read_plain_kurt_exactly": same,
                          "total_overwritten_frac": round(float(k.sum() / (n * M)), 4)}}


def selfcheck_report(reg) -> None:
    """Print every probe's self-check on the operators of this tree (and their siblings)."""
    from partura.probes import run_probes, values
    for op in ("cs_mask_top_replace_mean", "cs_mask_top_replace_mean_neg", "day_kurt", "day_mean"):
        spec = reg._ops.get(op) or reg._ops.get("nt_" + op)
        if spec is None:
            print(f"[selfcheck] {op}: not in registry")
            continue
        res = run_probes(spec, only=["tie_break_replaced_set", "replacement_vs_own_level",
                                     "spike_count_response", "composite_by_liquidity"])
        for name, r in res.items():
            if not r.get("applicable"):
                continue
            if "error" in r:
                print(f"[selfcheck] {name} on {op}: ERROR {r['error']}")
                continue
            sc = r["value"].get("selfcheck", {})
            flags = [v for v in sc.values() if isinstance(v, bool)]
            print(f"[selfcheck] {name:<26} on {op:<30} {'PASS' if all(flags) else 'FAIL'}  {sc}")
            print(f"            value: { {k: v for k, v in r['value'].items() if k != 'selfcheck'} }")
