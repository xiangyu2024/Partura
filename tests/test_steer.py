"""partura.steer on synthetic data: every reward kind runs and behaves; the matcher and the canonical form.

    ALPHACUBE_ROOT=~/Desktop/AlphaCube PYTHONPATH=~/Desktop/AlphaCube/src:. python -m pytest tests/test_steer.py -q
"""
import numpy as np
import pytest

from partura.steer import Guidance, Pattern, RewardContext, REWARDS, _bucket_rank, nonneg, parse_expr, reward, simplify


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
    alpha, liq, tgt, frozen, pool = _world()
    ctx = RewardContext(tgt, slice(0, 180), slice(180, 260), untradable=frozen, liq=liq, pool=pool, base=pool, halflives=(0.0, 5))
    r = reward(alpha, ctx, kind)
    assert np.isfinite(r["score"]) and r["sign"] in (1.0, -1.0) and r["hl"] in (0.0, 5.0)
    assert set(r["train"]) >= {"long_ann", "long_sharpe", "long_turnover"}


def test_direction_is_chosen_by_the_long_book():
    alpha, liq, tgt, frozen, pool = _world(1)
    ctx = RewardContext(tgt, slice(0, 180), slice(180, 260), untradable=frozen, liq=liq, pool=pool, base=pool, halflives=(0.0,))
    a, b = reward(alpha, ctx, "long"), reward(-alpha, ctx, "long")
    assert a["sign"] == -b["sign"] and a["score"] == pytest.approx(b["score"])
    assert a["sign"] == 1.0 and a["score"] > 1.0


def test_marginal_of_the_pool_itself_is_about_zero_and_a_real_signal_adds():
    alpha, liq, tgt, frozen, pool = _world(2)
    ctx = RewardContext(tgt, slice(0, 180), slice(180, 260), untradable=frozen, liq=liq, pool=pool, base=pool, halflives=(0.0,))
    same = reward(np.where(frozen, np.nan, pool), ctx, "long_marginal")
    assert abs(same["score_train"]) < 1e-9 and abs(same["score_valid"]) < 1e-9      # blend of the pool with itself = the pool, same universe
    assert reward(alpha, ctx, "long_marginal")["score"] > 0.3


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
    assert G.dedup_key("ts_spearman(day_quantile(Low), 10)") == G.dedup_key("ts_spearman(day_quantile(Close), 10)")
    assert G.weight("cross_ema(cross_ema(abs_(cs_demean(day_gini(Low))), 10), 241)") < G.weight("cross_ema(abs_(cs_demean(day_gini(Low))), 30)")
    hits = [G.accept("cross_ema(day_std(Ret), 30)", u=u) for u in (0.01, 0.99)]
    assert hits[0] and isinstance(hits[1], bool)
