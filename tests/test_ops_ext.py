"""Regression tests for the extension operators: every case below was a defect found by the independent audit
(handoff/workflows/wf_b7c13476-92d) or by a lead reading a table, reproduced before it was fixed.

    ALPHACUBE_ROOT=~/Desktop/AlphaCube PYTHONPATH=~/Desktop/AlphaCube/src:. python -m pytest tests/test_ops_ext.py -q
"""
import numpy as np
import pytest
import torch

from partura.bridge import ensure_alphacube_on_path

ensure_alphacube_on_path()
from partura import ops_ext as X  # noqa: E402

NAN = float("nan")


def _old_lexi(y, x, lo, hi, shift):
    ok = torch.isfinite(y) & torch.isfinite(x)
    rx, ry = X._pct_rank(x, ok), X._pct_rank(y, ok)
    return torch.where(ok, ry + shift * ((rx > lo) & (rx <= hi)).to(y.dtype), torch.full_like(y, NAN))


def test_screen_band_never_splits_a_tie_block():
    g = torch.Generator().manual_seed(0)
    S = 1000
    y = torch.rand(1, S, generator=g)
    count = torch.full((1, S), 241.0)
    young = torch.randperm(S, generator=g)[:71]
    count[0, young] = torch.randint(1, 240, (71,), generator=g).float()
    out = X.cs_last_high20(y, -count)                       # "send the 20% youngest to the bottom"
    pushed = (out < 0).nonzero()[:, 1]
    assert set(pushed.tolist()) == set(young.tolist())      # only the genuinely young; no mature name by column order
    perm = torch.randperm(S, generator=g)
    out_p = X.cs_last_high20(y[:, perm], -count[:, perm])
    assert torch.equal((out_p < 0)[0], (out < 0)[0][perm])  # invariant to the order of the stocks
    assert out.unique().numel() == S                        # the output keeps a distinct value per stock


@pytest.mark.parametrize("op,lo,hi,shift", [("cs_last_high20", 0.8, 1.0, -1.0), ("cs_first_low40", 0.0, 0.4, 1.0),
                                            ("cs_last_low20", 0.0, 0.2, -1.0), ("cs_first_high40", 0.6, 1.0, 1.0)])
def test_screen_unchanged_on_continuous_keys(op, lo, hi, shift):
    g = torch.Generator().manual_seed(1)
    y, x = torch.rand(6, 400, generator=g), torch.rand(6, 400, generator=g)
    y[torch.rand(6, 400, generator=g) < 0.2] = NAN
    x[torch.rand(6, 400, generator=g) < 0.1] = NAN
    new, old = getattr(X, op)(y, x), _old_lexi(y, x, lo, hi, shift)
    assert torch.equal(torch.isnan(new), torch.isnan(old)) and torch.equal(torch.nan_to_num(new), torch.nan_to_num(old))


def test_cross_zscore_of_a_constant_amount_is_zero():
    for dtype in (torch.float32, torch.float64):
        z = X.cross_zscore(torch.full((10, 1, 1), 1.5e9, dtype=dtype), 3)[:, 0, 0]
        assert torch.isnan(z[0]) and torch.all(z[1:] == 0)
    x = torch.tensor([1.0, 2.0, 4.0, 3.0, 5.0]).view(5, 1, 1)
    w = np.array([2.0, 4.0, 3.0])
    assert X.cross_zscore(x, 3)[3, 0, 0].item() == pytest.approx((3.0 - w.mean()) / w.std(), rel=1e-5)


def test_flip_by_state_gives_no_signal_without_a_state():
    g = torch.tensor([[NAN, NAN], [1.0, 2.0]])
    y = torch.tensor([[0.3, -0.1], [0.5, -0.5]])
    out = X.cs_flip_by_state(y, g)
    assert torch.isnan(out[0]).all() and torch.isfinite(out[1]).all()


def test_es_ratio_matches_a_float64_reference_at_the_real_width():
    rng = np.random.default_rng(7)
    x = rng.standard_normal((500, 1, 241))
    got_hi = X.day_es_ratio_hi(torch.tensor(x, dtype=torch.float32)).numpy().reshape(-1)
    got_lo = X.day_es_ratio_lo(torch.tensor(x, dtype=torch.float32)).numpy().reshape(-1)
    assert got_hi.dtype == np.float32
    x32 = x.astype(np.float32).astype(np.float64)[:, 0, :]
    for got, q, hi in ((got_hi, 0.95, True), (got_lo, 0.05, False)):
        v = np.quantile(x32, q, axis=1)
        ref = np.array([r[(r > t) if hi else (r < t)].mean() / t for r, t in zip(x32, v)])
        ok = np.isfinite(got) & (np.abs(v) > 1e-8)
        assert np.max(np.abs(got[ok] / ref[ok] - 1)) < 1e-4


@pytest.mark.parametrize("dtype", [torch.float32, torch.float64])
def test_expanding_zscore_on_amount_sized_input(dtype):
    x = (1e9 + np.arange(241.0))[None, None, :]
    got = X.in_zscore_expand(torch.tensor(x, dtype=dtype)).numpy()[0, 0]
    xr = np.asarray(torch.tensor(x, dtype=dtype).double())[0, 0]
    ref = np.array([np.nan if t < 4 else (xr[t] - xr[:t + 1].mean()) / (xr[:t + 1].std() + 1e-9) for t in range(241)])
    assert np.all(np.isnan(got[:4])) and np.nanmax(np.abs(got[4:] - ref[4:])) < 1e-3
    flat = X.in_zscore_expand(torch.full((1, 1, 30), 12.34, dtype=dtype))[0, 0]
    assert torch.all(flat[4:] == 0)


def test_flat_run_on_a_one_minute_day_is_nan_not_a_crash():
    assert torch.isnan(X.day_flat_run_max(torch.tensor([[[5.0]]]))).all()
    x = torch.tensor([[[1.0, 1.0, 1.0, 2.0, 2.0, 3.0]]])
    assert X.day_flat_run_max(x).reshape(-1)[0].item() == pytest.approx(2 / 6)


@pytest.mark.parametrize("scale", [1.0, 1e9, 1e16])
def test_cross_ema_keeps_its_coverage_at_any_magnitude(scale):
    torch.manual_seed(0)
    x = (torch.rand(300, 20, 1) * scale).float()
    x[torch.rand(300, 20, 1) < 0.1] = NAN
    y = X.cross_ema(x, 5)
    a = 1 - 0.5 ** (1 / 5)
    n = torch.zeros(20, 1, dtype=torch.float64)
    den = torch.zeros(20, 1, dtype=torch.float64)
    ref = torch.empty(300, 20, 1, dtype=torch.float64)
    for t in range(300):
        ok = torch.isfinite(x[t])
        n = (1 - a) * n + a * torch.where(ok, x[t].double(), torch.zeros_like(n))
        den = (1 - a) * den + a * ok.double()
        ref[t] = torch.where(den > 1e-12, n / den.clamp(min=1e-12), torch.full_like(n, NAN))
    good = torch.isfinite(ref)
    assert torch.equal(torch.isfinite(y), good)
    assert ((y.double() - ref).abs() / ref.abs().clamp(min=1e-30))[good].max().item() < 1e-5
