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


def test_metric_row_agrees_with_alphacubes_own_backtester():
    """Partura must not quietly compute a different Sharpe from AlphaCube's.
    Same panel, same cost, same book -> same numbers."""
    from alphacube.metrics import backtest_metrics, cs_pearson
    from partura.diagnose import COST_PER_SIDE, TOP_FRAC, TURNOVER_CAP
    sig, fwd = _fake_panel(5)
    mine = metric_row(sig, fwd, sign=1.0)
    theirs = backtest_metrics(cs_pearson(sig, fwd), sig, fwd, top_frac=TOP_FRAC,
                              cost_per_side=COST_PER_SIDE, turnover_cap=TURNOVER_CAP)
    for a, b in (("ic", "ic_mean"), ("icir", "icir"), ("turnover", "turnover"),
                 ("sharpe", "sharpe"), ("sharpe_net", "sharpe_net"), ("sharpe_capped", "sharpe_capped")):
        assert mine[a] == pytest.approx(theirs[b], rel=1e-9, abs=1e-12), a


def test_rank_corr_matrix_is_filled_on_both_sides():
    """The row for a later name used to be reset after earlier pairs wrote into
    it, so half the published table was NaN."""
    from partura.diagnose import rank_corr_matrix
    rng = np.random.default_rng(11)
    panels = {n: rng.normal(size=(50, 40)) for n in ("a", "b", "c")}
    m = rank_corr_matrix(panels)
    for a in panels:
        for b in panels:
            assert np.isfinite(m[a][b]), (a, b)
            assert m[a][b] == pytest.approx(m[b][a])
        assert m[a][a] == pytest.approx(1.0)


# ---------------------------------------------------------------- probes / propose / lab
def test_probe_registry_marks_inapplicable_instead_of_guessing():
    from partura.probes import run_probes
    from partura.bridge import ensure_alphacube_on_path
    ensure_alphacube_on_path()
    from alphacube.catalog import default_registry
    res = run_probes(default_registry().get("day_cov"))
    # a day-collapser has no day-axis window, so the causality probe must not invent an answer
    assert res["causal_on_day_axis"]["applicable"] is False
    assert "value" not in res["causal_on_day_axis"]
    assert res["homogeneity_degree"]["value"] == 2.0


def test_effective_quantile_probe_self_checks():
    """A probe is only usable on unknown operators once it reproduces known ones."""
    from partura.probes import load_study_probes, run_probes, values
    from partura.bridge import PARTURA_ROOT, ensure_alphacube_on_path
    ensure_alphacube_on_path()
    from alphacube.catalog import default_registry
    load_study_probes(PARTURA_ROOT / "studies" / "F002_crosscov_highvar" / "probes.py")
    reg = default_registry()
    assert values(run_probes(reg.get("ts_quantile_q75"), 5))["effective_quantile"] == pytest.approx(0.75)
    assert values(run_probes(reg.get("cross_max"), 9))["effective_quantile"] == pytest.approx(1.0)
    assert values(run_probes(reg.get("cross_min"), 9))["effective_quantile"] == pytest.approx(0.0)


def test_study_probes_are_tagged_with_their_file():
    from partura.probes import PROBES, load_study_probes
    from partura.bridge import PARTURA_ROOT
    load_study_probes(PARTURA_ROOT / "studies" / "F002_crosscov_highvar" / "probes.py")
    assert PROBES["cross_lag_response"].origin.endswith("probes.py")
    assert PROBES["homogeneity_degree"].origin == "builtin"


def test_proposals_differ_between_structurally_different_trees():
    """The whole point: the plan is a property of the expression."""
    from partura.propose import propose
    a = propose("cross_max(mul(cross_max(day_cov(Amt, Low), 9), pow_3(day_durbin_watson(Open))), 5)")
    b = propose("ts_quantile_q75(cross_cov(day_max(High), day_var(Ret), 15), 5)")
    ka, kb = {c.kind for c in a}, {c.kind for c in b}
    assert "interaction" in ka and "interaction" not in kb      # only A has a binary elementwise node
    assert not ({c.expr for c in a} & {c.expr for c in b})
    # substitutes are chosen by measured neighbourhood, so cov gets its scale-free twin
    assert any("cross_corr" in c.expr for c in b)


def test_proposals_never_include_the_original_or_a_rewrite_of_it():
    from partura.propose import propose
    src = "cross_max(mul(cross_max(day_cov(Amt, Low), 9), pow_3(day_durbin_watson(Open))), 5)"
    from partura.panels import parse_research
    base = parse_research(src).key()
    for c in propose(src):
        assert parse_research(c.expr).key() != base, c.id


def test_lab_recall_is_operator_scoped(tmp_path):
    from partura.lab import Finding, Lab
    from partura.panels import parse_research
    lab = Lab(tmp_path / "f.yaml")
    lab.record(Finding(id="x", claim="c", evidence="e", study="s", operators=["day_durbin_watson"]))
    lab.record(Finding(id="y", claim="c2", evidence="e2", study="s", pattern="O:day_cov(F:Amt"))
    assert {f.id for f in lab.recall(parse_research("day_durbin_watson(Open)"))} == {"x"}
    assert {f.id for f in lab.recall(parse_research("cross_max(day_cov(Amt, Low), 9)"))} == {"y"}
    assert lab.recall(parse_research("day_sum(Amt)")) == []
