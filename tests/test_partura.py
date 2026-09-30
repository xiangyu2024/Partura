"""Tests for the parts of Partura that are easy to get silently wrong."""
import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from partura.decompose import decompose
from partura.diagnose import conditional_ic, metric_row, neutralise, pair_rank_corr, sign_from
from partura.semantics import dossier
from partura.splits import Ledger


def test_probes_match_the_source():
    """The four facts the F001 report leans on, straight from the kernels."""
    assert dossier("day_cov").measured["homogeneity_degree"] == 2.0        # scale carrier
    assert dossier("day_cov").measured["shift_invariant"] is True          # demeaned
    dw = dossier("day_durbin_watson").measured
    assert dw["homogeneity_degree"] == 0.0                                 # scale free
    assert dw["shift_invariant"] is False                                  # divides by sum x^2, not the variance
    assert dw["order_dependent_on_minutes"] is True                        # path statistic
    cm = dossier("cross_max", window=9).measured
    assert cm["causal_on_day_axis"] is True                                # no look-ahead
    assert dossier("pow_3").measured["rank_preserving"] is True            # cannot change a rank book on its own


def test_path_lookback_composes_where_alphacube_takes_a_max():
    d = decompose("cross_max(mul(cross_max(day_cov(Amt, Low), 9), pow_3(day_durbin_watson(Open))), 5)")
    assert d.max_day_window == 9            # what alphacube.expression.max_window reports
    assert d.path_day_lookback == 13        # what the tree actually reads
    assert [s.var for s in d.steps] == list("ABCDEF")
    assert d.fields == ["Amt", "Low", "Open"]


def _fake_panel(seed=0, D=300, S=200):
    rng = np.random.default_rng(seed)
    sig = rng.normal(size=(D, S))
    fwd = 0.02 * sig + rng.normal(size=(D, S)) * 0.02
    return sig, fwd


def test_sign_is_fitted_once_and_applied():
    sig, fwd = _fake_panel()
    s = sign_from(-sig, fwd)
    assert s == -1.0
    m = metric_row(-sig, fwd, sign=s)
    assert m["rank_ic"] > 0 and m["sign"] == -1.0


def test_neutralise_kills_a_pure_control_clone():
    sig, fwd = _fake_panel(1)
    resid, info = neutralise(sig, {"same": sig})
    assert info["mean_r2"] > 0.99
    # The residual is exactly zero, so it must come back empty rather than as
    # ranked float noise (which scored a spurious |rank IC| of 0.08 before the guard).
    assert not np.isfinite(resid).any()
    assert np.isnan(metric_row(resid, fwd)["rank_ic"])


def test_neutralise_keeps_an_orthogonal_signal():
    sig, fwd = _fake_panel(2)
    rng = np.random.default_rng(9)
    unrelated = rng.normal(size=sig.shape)
    resid, info = neutralise(sig, {"noise": unrelated})
    assert info["mean_r2"] < 0.05
    assert metric_row(resid, fwd)["rank_ic"] > 0.5 * metric_row(sig, fwd)["rank_ic"]


def test_conditional_ic_sees_a_real_gate():
    """A signal that only works where the gate is high must show a rising profile."""
    rng = np.random.default_rng(3)
    D, S = 400, 300
    gate = rng.normal(size=(D, S))
    sig = rng.normal(size=(D, S))
    live = (gate > gate.mean(axis=1, keepdims=True))
    fwd = np.where(live, 0.05 * sig, 0.0) + rng.normal(size=(D, S)) * 0.02
    rows = conditional_ic(sig, fwd, gate, buckets=5)
    assert rows[0]["rank_ic"] < 0.05 < rows[-1]["rank_ic"]


def test_pair_rank_corr_is_one_for_a_monotone_rewrite():
    sig, _ = _fake_panel(4)
    assert pair_rank_corr(sig, np.exp(sig)) > 0.999
    assert pair_rank_corr(sig, -sig) < -0.999


def test_ledger_warns_once_the_holdout_is_reused(tmp_path):
    led = Ledger(tmp_path / "ledger.json")
    led.record("holdout", 3, "final check")
    assert "1 次" in led.warning()
    led.record("holdout", 5, "second look")
    assert "不是干净的测试集" in led.warning()
    assert Ledger(tmp_path / "ledger.json").summary()["holdout"]["expressions"] == 8
