"""partura.steer on synthetic data: every reward kind runs and behaves; the matcher and the canonical form.

    ALPHACUBE_ROOT=~/Desktop/AlphaCube-steering PYTHONPATH=~/Desktop/AlphaCube-steering/src:. python -m pytest tests/test_steer.py -q
"""
import numpy as np
import pytest

from partura.steer import Guidance, Pattern, RewardContext, REWARDS, _bucket_rank, nonneg, parse_expr, reward, simplify, neutral_basis


def _world(seed=0, D=260, S=300):
    rng = np.random.default_rng(seed)
    alpha = rng.normal(size=(D, S))                      # a persistent signal with real predictive power
    alpha = np.cumsum(alpha, axis=0) / np.sqrt(np.arange(1, D + 1))[:, None]
    liq = rng.normal(size=(1, S)) + 0.1 * rng.normal(size=(D, S))
    tgt = 0.002 * alpha - 0.001 * liq + 0.02 * rng.normal(size=(D, S))   # low liquidity is paid, too
    tgt[rng.random((D, S)) < 0.02] = np.nan
    frozen = rng.random((D, S)) < 0.1
    pool = -liq + 0.3 * rng.normal(size=(D, S))
    from partura import diagnose as dg
    return alpha, liq, tgt, frozen, dg._zrank(pool)


@pytest.mark.parametrize("kind", REWARDS)
def test_every_reward_runs_and_is_finite(kind):
    # (alpha is a real signal in this world, so every reward -- the paired ones included -- has something to measure)
    alpha, liq, tgt, frozen, pool = _world()
    ctx = RewardContext(tgt, slice(0, 180), slice(180, 260), untradable=frozen, liq=liq, pool=pool, base=pool, halflives=(0.0, 5))
    ctx.neutral_Q = neutral_basis([liq, pool])               # C03: what reward "long_neutral" regresses out
    r = reward(alpha, ctx, kind)
    assert np.isfinite(r["score"]) and r["sign"] in (1.0, -1.0) and r["hl"] in (0.0, 5.0)
    assert set(r["train"]) >= {"long_ann", "long_sharpe", "long_turnover"}


def test_direction_is_chosen_by_the_long_book():
    alpha, liq, tgt, frozen, pool = _world(1)
    ctx = RewardContext(tgt, slice(0, 180), slice(180, 260), untradable=frozen, liq=liq, pool=pool, base=pool, halflives=(0.0,))
    a, b = reward(alpha, ctx, "long"), reward(-alpha, ctx, "long")
    assert a["sign"] == -b["sign"] and a["score"] == pytest.approx(b["score"])
    assert a["sign"] == 1.0 and a["score"] > 1.0


def test_marginal_is_a_paired_difference_on_the_blend_s_own_cells():
    alpha, liq, tgt, frozen, pool = _world(2)
    ctx = RewardContext(tgt, slice(0, 180), slice(180, 260), untradable=frozen, liq=liq, pool=pool, base=pool, halflives=(0.0,))
    # the pool itself adds nothing to the pool: the two books are the same book, and "changes nothing" is a rejection
    assert reward(pool, ctx, "long_marginal")["score"] == float("-inf")
    # ... and still nothing when the candidate is missing on the names with the lowest returns: before the fix the
    # pool kept those names in ITS benchmark and such a zero-information candidate scored about -1
    worst = np.argsort(np.nanmean(tgt, axis=0))[: tgt.shape[1] // 10]
    holed = pool.copy()
    holed[:, worst] = np.nan
    assert reward(holed, ctx, "long_marginal")["score"] == float("-inf")
    r = reward(alpha, ctx, "long_marginal")
    assert r["score"] > 1.0 and r["score_train"] > 0 and r["score_valid"] > 0 and r["sign"] == 1.0


def test_screen_reward_cuts_whole_tie_blocks_and_rejects_a_no_op():
    alpha, liq, tgt, frozen, pool = _world(4)
    rng = np.random.default_rng(4)
    ctx = RewardContext(tgt, slice(0, 180), slice(180, 260), untradable=None, liq=liq, pool=pool, base=pool, halflives=(0.0,))
    # a saturating candidate: 70% of the names tied at the floor, the rest marking genuinely bad names
    bad = (-alpha > np.nanquantile(-alpha, 0.85, axis=1, keepdims=True)).astype(float) * (1 + rng.random(alpha.shape))
    r = reward(bad, ctx, "long_screen")
    assert 0.0 < r["screened_share"] <= 0.2 + 1e-9 and r["sign"] == 1.0 and r["score"] > 0.5
    # a candidate that is constant across names can screen nobody in either direction: rejected, not scored 0
    assert reward(np.ones_like(alpha), ctx, "long_screen")["score"] == float("-inf")


def test_unknown_reward_is_an_error():
    alpha, liq, tgt, frozen, pool = _world()
    ctx = RewardContext(tgt, slice(0, 180), slice(180, 260), untradable=frozen, liq=liq, pool=pool, base=pool, halflives=(0.0,))
    with pytest.raises(ValueError):
        reward(alpha, ctx, "long_typo")


def test_bucket_reward_does_not_pay_for_the_liquidity_tilt():
    alpha, liq, tgt, frozen, pool = _world(3)
    ctx = RewardContext(tgt, slice(0, 180), slice(180, 260), untradable=None, liq=liq, pool=pool, base=pool, halflives=(0.0,))
    tilt = -liq                                                    # a pure liquidity factor: paid by `long`, not inside buckets
    assert reward(tilt, ctx, "long")["score"] > 1.0
    assert reward(tilt, ctx, "long_bucket")["score"] < 0.5 * reward(tilt, ctx, "long")["score"]
    assert reward(alpha, ctx, "long_bucket")["score"] > 1.0


def test_bucket_rank_matches_brute_force():
    rng = np.random.default_rng(0)
    sm = rng.normal(size=(4, 50))
    sm[0, 5] = np.nan
    bucket = rng.integers(0, 4, size=(4, 50)).astype(np.int8)
    bucket[1, 7] = -1
    r = _bucket_rank(sm, bucket, 4)
    for d in range(4):
        for j in range(50):
            if not np.isfinite(sm[d, j]) or bucket[d, j] < 0:
                assert np.isnan(r[d, j])
                continue
            m = np.isfinite(sm[d]) & (bucket[d] == bucket[d, j])
            assert r[d, j] == pytest.approx((sm[d][m] <= sm[d, j]).sum() / m.sum())


def test_patterns():
    t = parse_expr("cross_ema(abs_(cs_demean(day_gini(Low))), 30)")
    assert Pattern.compile("root: {cross_ema|cross_mean}(_, {30|60})").matches(t)
    assert not Pattern.compile("root: cross_ema(_, 60)").matches(t)
    assert Pattern.compile("day_gini(@price)").matches(t) and not Pattern.compile("day_gini(@flow)").matches(t)
    assert Pattern.compile("day_cov(_1, _1)").matches(parse_expr("cross_max(day_cov(Amt, Amt), 3)"))
    assert not Pattern.compile("day_cov(_1, _1)").matches(parse_expr("cross_max(day_cov(Amt, Low), 3)"))
    assert Pattern.compile("div(_, add(_, create_like(_, $w)))").matches(parse_expr("div(day_sum(Ret), add(day_quantile(Ret, 0.95), create_like(day_quantile(Ret, 0.95), 1e-06)))"))
    assert str(parse_expr("sub(ts_max(day_mean(Ret), 5), -5)")) == "sub(ts_max(day_mean(Ret), 5), -5)"


def test_simplify_and_sign():
    assert nonneg(parse_expr("cross_ema(abs_(cs_demean(day_gini(Low))), 30)"))
    assert not nonneg(parse_expr("day_mean(Ret)")) and not nonneg(parse_expr("sub(Close, Open)"))
    assert str(simplify(parse_expr("abs_(cross_ema(abs_(abs_(cs_demean(cs_demean(day_gini(Low))))), 241))"))) == "cross_ema(abs_(cs_demean(day_gini(Low))), 241)"
    assert str(simplify(parse_expr("abs_(Ret)"))) == "abs_(Ret)"


def test_guidance_file_loads_and_judges():
    from pathlib import Path
    G = Guidance.load(Path(__file__).resolve().parents[1] / "guidance" / "B01.yaml")
    assert G.banned("cross_zscore(day_std(Ret), 30)") and not G.banned("cross_ema(day_std(Ret), 30)")
    assert G.canonical("ts_max(day_mean(Ret), 1)") == "day_mean(Ret)"
    assert G.dedup_key("ts_spearman(day_quantile(Low), 10)") != G.dedup_key("ts_spearman(day_quantile(Close), 10)")
    assert G.family_key("ts_spearman(day_quantile(Low), 10)") == G.family_key("ts_spearman(day_quantile(Close), 10)")
    assert len({G.family_key(e) for e in ("sub(High, Low)", "sub(Close, Open)", "sub(High, Close)")}) == 1       # one family: two distinct prices
    assert G.family_key("sub(High, Low)") != G.family_key("sub(Close, Close)")                                     # ... but not a degenerate one
    assert G.family_key("day_corr(High, Low)") != G.family_key("day_corr(High, High)")
    assert G.canonical("cs_winsor(day_std(Ret))") == "cs_winsor(day_std(Ret))"                                    # not an equivalence any more
    ow = G.operator_weights()
    assert "cross_zscore" not in ow and "cs_mean" not in ow and ow.get("ts_product") == 0.0                         # root-only bans stay out of the vocabulary
    assert G.weight("cross_ema(cross_ema(abs_(cs_demean(day_gini(Low))), 10), 241)") < G.weight("cross_ema(abs_(cs_demean(day_gini(Low))), 30)")
    hits = [G.accept("cross_ema(day_std(Ret), 30)", u=u) for u in (0.01, 0.99)]
    assert hits[0] and isinstance(hits[1], bool)


def test_is_discovery_paired_needs_both_periods():
    """A paired reward's combined ratio is dominated by the training period: a find needs each period on its own."""
    from partura.steer import is_discovery

    assert is_discovery("long", 1.2)                                         # level reward: the score is the whole test
    assert not is_discovery("long", 0.9)
    assert not is_discovery("long", float("nan")) and not is_discovery("long", float("-inf"))
    assert is_discovery("long_screen", 1.5, 1.46, 1.41)
    assert not is_discovery("long_screen", 2.9, 5.06, 0.08)                  # e3_I1: only the training period carries it
    assert not is_discovery("long_marginal", 1.5, 1.4, None)                 # a period that was not measured does not pass
    assert not is_discovery("long_marginal", 0.8, 0.9, 0.9)                  # below the line on the combined period
    assert is_discovery("long_marginal", 0.8, 0.9, 0.9, threshold=0.5)


def test_family_key_strips_order_preserving_root_wrappers():
    """pow_05(X) orders a cross-section as X does: a sibling of X (family), not X itself (dedup)."""
    from partura.steer import Guidance, parse_expr, strip_root_monotone

    g = Guidance({"priors": [{"id": "fam", "action": "family", "w": 0.3, "pattern": "root: {pow_05|pow_1_5|pow_2|sqrt|sigmoid}(_)"},
                             {"id": "px", "action": "family", "w": 0.3, "pattern": "@price"}]})
    x = "ts_std(pow_1_5(day_flat_ratio(Vwap)), 20)"
    assert g.family_key(f"pow_05({x})") == g.family_key(x) == g.family_key(f"pow_05(pow_05({x}))")
    assert g.dedup_key(f"pow_05({x})") != g.dedup_key(x)                       # never the same experiment
    assert g.family_key(f"pow_1_5({x})") == g.family_key(x)                    # the operand (a std) is never negative
    # x**2 of something that can be negative folds it: not order-preserving, not a sibling
    assert g.family_key("pow_2(cs_demean(day_std(Ret)))") != g.family_key("cs_demean(day_std(Ret))")
    assert g.family_key("sqrt(sub(Close, Open))") != g.family_key("sub(Close, Open)")      # sqrt(|x|) folds as well
    # only at the root: the same wrapper inside the tree is a different factor
    assert g.family_key(f"cross_mean(pow_05(day_std(Ret)), 5)") != g.family_key("cross_mean(day_std(Ret), 5)")
    # a wrapper the rule does not name is left alone, and the price-leaf family still works underneath
    assert g.family_key("pow_3(day_std(Low))") != g.family_key("day_std(Low)")
    assert g.family_key("pow_05(day_std(Low))") == g.family_key("day_std(Close)")
    assert str(strip_root_monotone(parse_expr("pow_3(sigmoid(neg(Close)))"))) == str(parse_expr("neg(Close)"))
    assert g.family_weight == 0.3


def test_sized_ratio_discounts_small_differences():
    """A paired information ratio has no scale: a tiny, steady difference must not outrank one that is worth something."""
    from partura.steer import PAIRED_SIZE, _sized

    assert PAIRED_SIZE == 0.01
    assert _sized(2.0, 0.002) == pytest.approx(0.4)          # +0.2 points a year, very steady: e3_I1's control "finds"
    assert _sized(1.4, 0.032) == pytest.approx(1.4)          # +3.2 points a year: keeps its ratio
    assert _sized(1.0, 0.01) == pytest.approx(1.0)
    assert _sized(-0.7, -0.02) == -0.7                       # a loss is not softened
    assert _sized(0.0, 0.0) == 0.0
    assert _sized(float("nan"), 0.01) != _sized(float("nan"), 0.01)
    assert _sized(2.0, 0.002) < _sized(1.4, 0.032)
