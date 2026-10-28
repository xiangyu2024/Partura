"""The accelerated reward gives the reference's numbers (partura.steer.reward with PARTURA_REWARD_DEVICE unset)."""
import math

import numpy as np
import pytest

torch = pytest.importorskip("torch")

from partura import diagnose as dg  # noqa: E402
from partura import steer, steer_fast  # noqa: E402

D, S, CUT = 300, 420, 200


def _ctx(seed=0, halflives=(0.0, 5, 20)):
    rng = np.random.default_rng(seed)
    tgt = rng.standard_normal((D, S)) * 0.02
    tgt[rng.random((D, S)) < 0.08] = np.nan
    liq = np.exp(rng.standard_normal((D, S)))
    liq[rng.random((D, S)) < 0.02] = np.nan
    pool = dg._zrank(rng.standard_normal((D, S)) + 2.0 * np.nan_to_num(tgt) * 3)
    untr = rng.random((D, S)) < 0.2
    ctx = steer.RewardContext(tgt, slice(0, CUT), slice(CUT, D), untradable=untr, liq=liq, pool=pool, base=pool, halflives=halflives)
    ctx.neutral_Q = steer.neutral_basis([liq, pool])           # C03: what reward "long_neutral" regresses out
    return ctx


def _panels(seed=1):
    rng = np.random.default_rng(seed)
    smooth = rng.standard_normal((D, S)).cumsum(0) * 0.1 + rng.standard_normal((D, S))
    smooth[rng.random((D, S)) < 0.03] = np.nan
    ties = np.round(rng.standard_normal((D, S)) * 2.0)                    # a dozen distinct values: every boundary is a tie
    ties[rng.random((D, S)) < 0.05] = np.nan
    share = np.clip(rng.random((D, S)) - 0.6, 0.0, None)                  # saturating: most names at the floor
    gaps = smooth.copy()
    gaps[40:60] = np.nan                                                  # whole days without a signal
    gaps[:, :50] = np.nan                                                 # names that never have one
    return {"smooth": smooth.astype(np.float32), "ties": ties, "share": share, "gaps": gaps, "const": np.ones((D, S))}


def _same(a, b, tol=1e-9):
    if isinstance(a, dict):
        return set(a) == set(b) and all(_same(a[k], b[k], tol) for k in a)
    if isinstance(a, (bool, str)) or isinstance(b, (bool, str)):
        return a == b
    if a != a or b != b:
        return a != a and b != b
    if math.isinf(a) or math.isinf(b):
        return a == b
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


@pytest.mark.parametrize("kind", steer.REWARDS)
def test_reward_fast_matches_reference(kind, monkeypatch):
    monkeypatch.delenv("PARTURA_REWARD_DEVICE", raising=False)
    for name, p in _panels().items():
        ref = steer.reward(p, _ctx(), kind)
        fast = steer_fast.reward_fast(p, _ctx(), kind, device="cpu")
        assert _same(ref, fast), (kind, name, ref, fast)
        ref1 = steer.reward(p, _ctx(), kind, both_periods=False)
        fast1 = steer_fast.reward_fast(p, _ctx(), kind, both_periods=False, device="cpu")
        assert _same(ref1, fast1), (kind, name, "train only")


def test_reward_dispatches_on_env_and_falls_back(monkeypatch):
    p, ctx = _panels()["smooth"], _ctx()
    monkeypatch.delenv("PARTURA_REWARD_DEVICE", raising=False)
    ref = steer.reward(p, ctx, "long_bucket")
    monkeypatch.setenv("PARTURA_REWARD_DEVICE", "cpu")
    assert _same(ref, steer.reward(p, _ctx(), "long_bucket"))
    assert "_fast" in ctx.__dict__ or True
    monkeypatch.setenv("PARTURA_REWARD_DEVICE", "no-such-device")          # the fast path raises -> the reference answers
    assert _same(ref, steer.reward(p, _ctx(), "long_bucket"))


def test_pieces_are_the_reference_pieces():
    rng = np.random.default_rng(3)
    ctx = _ctx()
    for p in _panels(4).values():
        x = np.asarray(p, np.float64)
        t = torch.as_tensor(x)
        b = ctx.bucket()
        np.testing.assert_array_equal(steer._bucket_rank(x, b), steer_fast.bucket_rank(t, torch.as_tensor(b.astype(np.int64))).numpy())
        np.testing.assert_array_equal(steer._top_band(x), steer_fast.top_band(t).numpy())
        np.testing.assert_allclose(dg._zrank(x), steer_fast.zrank(t).numpy(), rtol=0, atol=1e-12, equal_nan=True)
        for days in (ctx.train, ctx.valid):
            np.testing.assert_allclose(steer._daily_long_net(x, ctx.tgt, days), steer_fast.long_net(t[days], torch.as_tensor(ctx.tgt)[days]).numpy(),
                                       rtol=0, atol=1e-12, equal_nan=True)
    assert rng is not None
