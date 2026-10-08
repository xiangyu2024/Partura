"""K002 tooling, part D: scripts/group_final.py -- the K002 reading rule as amended on 2026-10-07 20:45 PDT (README, 现行规则).

Pure pieces (gates, the two selection paths, the distinctness walks, paired statistics, exposure, the verdict ladder, the
multiplicity pass, the once-only guard) are tested on hand-made inputs; the whole script is run end to end on a synthetic world
with the REAL scripts/sweep.py in front of it (--only-extra, with `lock:` / `base:` / `twin:` / `kind:` keys) and a PanelSet
stand-in (tests/k002_helpers.py, tests/k002_world.py); and the role logic is run on the shape of the REAL hypotheses file.
"""
import ast
import copy
import importlib.util
import json
import shutil
import sys
import types
from pathlib import Path

import numpy as np
import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import k002_helpers as H  # noqa: E402
import k002_world as W  # noqa: E402

from partura import books as bk  # noqa: E402
from partura import diagnose as dg  # noqa: E402
from partura.splits import SPLITS, Ledger  # noqa: E402

from alphacube.metrics import long_short_weights  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]


def _load_gf():
    spec = importlib.util.spec_from_file_location("group_final_under_test", H.SCRIPTS / "group_final.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


GF = _load_gf()


@pytest.fixture(autouse=True)
def _isolation(monkeypatch):
    import torch
    saved, threads = dict(SPLITS), torch.get_num_threads()
    monkeypatch.setenv("PARTURA_RANK_DEVICE", "")
    yield
    SPLITS.clear()
    SPLITS.update(saved)
    torch.set_num_threads(threads)


# ============================================================================================ gates and the standalone ranking
def _v(**over):
    v = {"kind": "hypo", "cov": 1.0, "dist": 1.0, "sign": 1.0, "hl_long_u": 5.0, "expr": "x",
         "train_long": {"long_ann": 0.05}, "valid_long": {"long_ann": 0.03}, "utrain_long": {"long_sharpe": 1.0, "long_ann": 0.04}}
    v.update(over)
    return v


def test_gates_are_those_of_sweep_final():
    assert GF.gate_failures(_v()) == []
    assert GF.gate_failures(_v(cov=0.95, dist=0.5)) == []                              # >= : the boundary passes
    assert "coverage" in GF.gate_failures(_v(cov=0.9499))[0]
    assert "distinctness" in GF.gate_failures(_v(dist=0.4999))[0]
    assert GF.gate_failures(_v(cov=float("nan")))                                      # undefined fails, as `nan >= .95` does
    assert GF.gate_failures(_v(dead=True)) == ["dead (no rank IC on train)"]
    assert GF.gate_failures(_v(kind="bench")) and GF.gate_failures(_v(kind="base"))
    # long leg positive on BOTH train and valid; zero, None and NaN are not positive
    for bad in (0.0, -0.01, None, float("nan")):
        assert any("train" in r for r in GF.gate_failures(_v(train_long={"long_ann": bad})))
        assert any("valid" in r for r in GF.gate_failures(_v(valid_long={"long_ann": bad})))
    assert len(GF.gate_failures(_v(train_long={"long_ann": -1}, valid_long={"long_ann": -1}, cov=0.1, dist=0.1))) == 4
    # a modification is judged on its difference against its base: the gates without the long legs
    assert GF.gate_failures(_v(train_long={"long_ann": -1}, valid_long={"long_ann": -1}), legs=False) == []
    assert len(GF.gate_failures(_v(cov=0.1, dist=0.1, train_long={"long_ann": -1}), legs=False)) == 2


def test_gates_agree_with_the_filter_in_sweep_final():
    """The same predicate as the `ok` list of scripts/sweep_final.py, evaluated on random records."""
    import random
    src = (H.SCRIPTS / "sweep_final.py").read_text(encoding="utf-8")
    line = next(ln for ln in src.splitlines() if "v[\"cov\"] >= 0.95" in ln)
    assert "v[\"dist\"] >= 0.5" in line and GF.COV_MIN == 0.95 and GF.DIST_MIN == 0.5
    rnd = random.Random(4)
    for _ in range(400):
        v = _v(cov=rnd.choice([0.5, 0.95, 0.99, float("nan")]), dist=rnd.choice([0.3, 0.5, 0.9]), kind=rnd.choice(["hypo", "bench", "base", "leaf"]),
               train_long={"long_ann": rnd.choice([-0.1, 0.0, 0.1, float("nan"), None])}, valid_long={"long_ann": rnd.choice([-0.1, 0.0, 0.1, None])})
        old = (not v.get("dead") and v["cov"] >= 0.95 and v["dist"] >= 0.5 and v["kind"] not in ("bench", "base")
               and (v["train_long"]["long_ann"] or -1) > 0 and (v["valid_long"]["long_ann"] or -1) > 0)
        assert (GF.gate_failures(v) == []) == bool(old), v


def test_standalones_are_ranked_by_the_training_period_sharpe():
    R = {"b_low": _v(utrain_long={"long_sharpe": 0.4}), "b_high": _v(utrain_long={"long_sharpe": 1.7}),
         "b_nan": _v(utrain_long={"long_sharpe": float("nan")}), "b_mid_b": _v(utrain_long={"long_sharpe": 0.9}),
         "b_mid_a": _v(utrain_long={"long_sharpe": 0.9}),
         "b_cov": _v(cov=0.2), "b_valid_neg": _v(valid_long={"long_ann": -0.02}), "b_dead": {"dead": True, "kind": "hypo"}}
    ranked, fail = GF.rank_standalone(R, list(R))
    assert ranked == ["b_high", "b_mid_a", "b_mid_b", "b_low", "b_nan"]            # ties by id; an undefined Sharpe sorts last
    assert set(fail) == {"b_cov", "b_valid_neg", "b_dead"}
    assert GF.rank_standalone(R, []) == ([], {})


# ================================================================================================== roles, twins, the plan
RULERS = set(GF.DEFAULT_RULERS)


def test_the_default_rulers_are_the_readmes_list():
    assert GF.DEFAULT_RULERS == ("v_base", "k_known", "k_known_xfrozen", "a_size", "a_tsize", "a_turn20", "a_amt20", "a_known_in_size",
                                 "a_size_in_known", "a_known_in_turn", "a_size_plus_known", "e_main_only", "e_wide_only", "e_xage1y")


def test_roles_follow_the_id_and_the_keys_the_sweep_carries():
    g = ("b_", "c_", "d_", "e_")
    role = lambda k, **kw: GF.role_of(k, _v(**kw), RULERS, g)                       # noqa: E731
    assert role("a_size") == "ruler" and role("e_main_only", base="k_known") == "ruler" and role("v_base", kind="base") == "ruler"
    assert role("b_x") == "standalone" and role("c_x", base="k_known") == "modification" and role("e_x", base="x_car") == "modification"
    assert role("b_x_twin") == "twin" and role("e_xmicro10_twin", base="k_known") == "twin" and role("d_p_twin", base="a_known_in_size", lock=True) == "twin"
    assert role("x_sync") == "carrier" and role("z_declared", declared_kind="carrier") == "carrier"
    assert role("a_young") == "other" and role("zz_other") == "other"
    # with a ruler list of its own, the same id is a candidate again
    assert GF.role_of("e_main_only", _v(), set(), g) == "standalone"


def test_a_twin_is_found_by_name_or_by_the_explicit_key():
    R = {"c_p": _v(), "c_p_twin": _v(), "c_q": _v(twin="k_known"), "k_known": _v(), "c_r": _v(twin="c_s_twin"), "c_s_twin": _v(), "c_none": _v()}
    assert GF.twin_of(R, "c_p") == "c_p_twin"
    assert GF.twin_of(R, "c_q") == "k_known"                                        # an existing object named by the key
    assert GF.twin_of(R, "c_r") == "c_s_twin"
    assert GF.twin_of(R, "c_none") is None
    R["c_p"]["twin"] = "k_known"
    assert GF.twin_of(R, "c_p") == "k_known"                                        # the key wins over the name
    assert GF.twin_of({"c_t": _v(twin="gone")}, "c_t") is None                      # a twin the sweep does not have is no twin


def test_a_base_chain_is_followed_and_a_cycle_stops_it():
    R = {"m": _v(base="b1"), "b1": _v(base="b2"), "b2": _v(), "c1": _v(base="c2"), "c2": _v(base="c1"), "lone": _v(base="gone")}
    assert GF.base_chain(R, "m") == ["b1", "b2"] and GF.base_chain(R, "b2") == []
    assert GF.base_chain(R, "c1") == ["c2"] and GF.base_chain(R, "lone") == []


def test_make_plan_decides_from_the_sweep_alone():
    R = {k: _v(kind="bench" if k in GF.BASE_IDS else "hypo") for k in GF.DEFAULT_RULERS}
    R["v_base"]["kind"] = "base"
    R.update({"b_stand": _v(), "b_cov": _v(cov=0.1), "b_mod": _v(base="k_known"), "b_mod_nobase": _v(base="gone"), "b_mod_deadbase": _v(base="x_dead"),
              "x_dead": {"dead": True, "kind": "hypo"}, "x_car": _v(), "b_twin_x_twin": _v(base="k_known"), "b_stand_twin": _v(),
              "c_stand": _v(), "e_only_mod": _v(base="x_car"), "a_young": _v()})
    plan = GF.make_plan(R, ["b_", "c_", "d_", "e_"], None, ["k_known", "a_size"])
    assert plan["always"] == list(GF.DEFAULT_RULERS) and plan["unread"] == {}
    b = plan["groups"]["b_"]
    assert (b["n_standalone"], b["n_modification"]) == (2, 3)                           # twins, carriers, rulers and a_ leftovers do not count
    assert b["standalone"]["eligible"] == ["b_stand"] and list(b["standalone"]["gate_fail"]) == ["b_cov"]
    assert b["modification"]["gated"] == ["b_mod"]
    assert set(b["modification"]["gate_fail"]) == {"b_mod_nobase", "b_mod_deadbase"}
    assert "not in the sweep" in b["modification"]["gate_fail"]["b_mod_nobase"][0] and "dead" in b["modification"]["gate_fail"]["b_mod_deadbase"][0]
    assert plan["groups"]["c_"]["standalone"]["eligible"] == ["c_stand"] and plan["groups"]["c_"]["modification"]["gated"] == []
    e = plan["groups"]["e_"]                                                            # the e_ rulers are not candidates; E may have no standalone at all
    assert (e["n_standalone"], e["n_modification"], e["standalone"]["eligible"], e["modification"]["gated"]) == (0, 1, [], ["e_only_mod"])
    # --always replaces the default list (the benchmarks and the pair references are read regardless)
    p2 = GF.make_plan(R, ["b_", "e_"], ["b_cov"], ["k_known"])
    assert p2["always"] == ["v_base", "k_known", "k_known_xfrozen", "b_cov"]
    assert p2["groups"]["e_"]["n_standalone"] == 3                                      # e_main_only / e_wide_only / e_xage1y are ordinary ids now
    with pytest.raises(SystemExit, match="not in the sweep"):
        GF.make_plan(R, ["b_"], ["nonesuch"], ["k_known"])
    with pytest.raises(SystemExit, match="not in the sweep"):
        GF.make_plan(R, ["b_"], None, ["k_known", "a_missing"])
    del R["e_xage1y"]
    with pytest.raises(SystemExit, match="e_xage1y"):
        GF.make_plan(R, ["b_"], None, ["k_known"])                                      # a default ruler the sweep lacks is an error, not a silent gap
    R["e_xage1y"] = {"dead": True, "kind": "hypo"}
    assert "e_xage1y" in GF.make_plan(R, ["b_"], None, ["k_known"])["unread"]
    R["a_size"] = {"dead": True, "kind": "hypo"}
    with pytest.raises(SystemExit, match="dead"):
        GF.make_plan(R, ["b_"], None, ["k_known", "a_size"])                          # a pair reference cannot be dead
    with pytest.raises(SystemExit, match="no"):
        GF.make_plan({"k_known": _v()}, ["b_"], None, [])


def _real_hypotheses_as_a_sweep():
    d = yaml.safe_load((ROOT / "studies" / "K002_daily_fields" / "hypo.yaml").read_text(encoding="utf-8"))
    rec = lambda **kw: _v(**kw)                                                     # noqa: E731
    R = {"v_base": rec(kind="base"), "k_known": rec(kind="bench"), "k_known_xfrozen": rec(kind="bench")}
    for k, v in d.items():
        R[k] = rec(expr=v["expr"], **{a: v[b] for a, b in (("base", "base"), ("twin", "twin"), ("declared_kind", "kind")) if v.get(b)})
    return d, R


def test_the_roles_on_the_shape_of_the_real_hypotheses_file():
    d, R = _real_hypotheses_as_a_sweep()
    plan = GF.make_plan(R, ["b_", "c_", "d_", "e_"], None, ["k_known", "a_size"])
    counts = {p: (g["n_standalone"], g["n_modification"]) for p, g in plan["groups"].items()}
    assert counts == {"b_": (35, 5), "c_": (25, 3), "d_": (15, 15), "e_": (0, 38)}      # README, 现行规则: 参加挑选的 B 35+5, C 25+3, D 15+15, E 0+38
    assert plan["always"] == list(GF.DEFAULT_RULERS) and plan["unread"] == {}
    cand = {k for g in plan["groups"].values() for k in g["standalone"]["eligible"] + g["modification"]["gated"] + list(g["standalone"]["gate_fail"]) + list(g["modification"]["gate_fail"])}
    twins = [k for k in d if k.endswith("_twin")]
    carriers = [k for k in d if k.startswith("x_")]
    assert len(twins) == 36 and len(carriers) == 6
    assert not cand & set(twins) and not cand & set(carriers) and not cand & set(GF.DEFAULT_RULERS)
    assert all(GF.role_of(k, R[k], set(GF.DEFAULT_RULERS), ("b_", "c_", "d_", "e_")) == "twin" for k in twins)       # also the ten that carry a base
    assert sum(1 for k in twins if d[k].get("base")) == 10
    # the three ruler ids carry base: k_known; they are rulers, not candidates of group E
    assert {k: d[k].get("base") for k in ("e_main_only", "e_wide_only", "e_xage1y")} == {"e_main_only": "k_known", "e_wide_only": "k_known", "e_xage1y": "k_known"}
    # twins: by name, and the seven explicit ones
    assert GF.twin_of(R, "c_dturn10") == "c_dturn10_twin"
    explicit = {k: v["twin"] for k, v in d.items() if v.get("twin")}
    assert len(explicit) == 7 and all(GF.twin_of(R, p) == t for p, t in explicit.items())
    assert explicit["d_vol_board"] == "d_vollim20_twin" and explicit["c_dturn30"] == "k_known"
    # every base of a selectable modification resolves, within one step
    assert all(len(GF.base_chain(R, k)) == 1 for k in d if d[k].get("base") and not k.endswith("_twin"))
    assert GF.base_chain(R, "b_f111_in_size") == ["b_sync_in_size"]                      # a base may be an ordinary hypothesis


def test_check_hypo_accepts_the_real_hypotheses_file():
    import runpy
    old_argv = sys.argv
    sys.argv = ["check_hypo.py", str(ROOT / "studies" / "K002_daily_fields" / "hypo.yaml")]
    try:
        with pytest.raises(SystemExit) as e:
            runpy.run_path(str(H.SCRIPTS / "check_hypo.py"), run_name="__main__")
    finally:
        sys.argv = old_argv
    assert e.value.code == 0


# ============================================================================================ the modification path
def test_diff_stats_and_the_eligibility_of_a_modification():
    rng = np.random.default_rng(1)
    n = 200
    m_tr = np.arange(n) < 120
    m_va = ~m_tr
    d = rng.normal(0.001, 0.004, n)
    st = GF.diff_stats(d, m_tr, m_va)
    assert st["mean_train"] == pytest.approx(d[:120].mean()) and st["mean_valid"] == pytest.approx(d[120:].mean())
    assert st["ir"] == pytest.approx(d.mean() / d.std() * np.sqrt(252)) and st["ann"] == pytest.approx(d.mean() * 252) and st["n"] == n and not st["noop"]
    d2 = d.copy()
    d2[5] = np.nan
    assert GF.diff_stats(d2, m_tr, m_va)["n"] == n - 1
    # identically zero: a no-op screen; a tiny float residue still counts as zero, a real difference does not
    z = GF.diff_stats(np.zeros(n), m_tr, m_va)
    assert z["noop"] is True and GF.modification_failures(z) == ["the paired difference against its base is identically zero (a no-op)"]
    assert GF.diff_stats(np.full(n, 1e-14), m_tr, m_va)["noop"] is True
    one = np.zeros(n)
    one[50] = 1e-4
    assert GF.diff_stats(one, m_tr, m_va)["noop"] is False
    # the mean must be positive on BOTH train and valid
    pos = np.where(m_tr, 0.002, 0.001) + rng.normal(0, 0.0005, n)
    assert GF.modification_failures(GF.diff_stats(pos, m_tr, m_va)) == []
    neg_valid = np.where(m_tr, 0.002, -0.001) + rng.normal(0, 0.0005, n)
    assert "valid" in GF.modification_failures(GF.diff_stats(neg_valid, m_tr, m_va))[0]
    neg_train = np.where(m_tr, -0.002, 0.001) + rng.normal(0, 0.0005, n)
    assert "train" in GF.modification_failures(GF.diff_stats(neg_train, m_tr, m_va))[0]
    assert len(GF.modification_failures(GF.diff_stats(-np.abs(d), m_tr, m_va))) == 2
    assert GF.modification_failures(GF.diff_stats(np.full(n, np.nan), m_tr, m_va))              # nothing to read


def test_modifications_are_ranked_by_the_information_ratio_of_their_difference():
    rng = np.random.default_rng(2)
    n = 200
    m_tr = np.arange(n) < 120
    m_va = ~m_tr
    mk = lambda mu, sd: GF.diff_stats(rng.normal(mu, sd, n), m_tr, m_va)           # noqa: E731
    stats = {"m_hi": mk(0.003, 0.002), "m_lo": mk(0.0012, 0.004), "m_big_mean_noisy": mk(0.004, 0.02), "m_bad": GF.diff_stats(-np.abs(rng.normal(0.002, 0.001, n)), m_tr, m_va),
             "m_noop": GF.diff_stats(np.zeros(n), m_tr, m_va)}
    ranked, fail = GF.rank_modifications(list(stats), stats)
    assert set(fail) == {"m_bad", "m_noop"}
    assert ranked == sorted(ranked, key=lambda k: -stats[k]["ir"]) and ranked[0] == "m_hi"
    assert GF.rank_modifications([], {}) == ([], {})


def test_series_corr_and_the_walk_on_difference_series():
    rng = np.random.default_rng(3)
    a = rng.normal(0, 1, 300)
    b = a + 0.1 * rng.normal(0, 1, 300)
    c = rng.normal(0, 1, 300)
    assert GF.series_corr(a, a) == pytest.approx(1.0) and GF.series_corr(a, -a) == pytest.approx(-1.0)
    assert GF.series_corr(a, b) == pytest.approx(np.corrcoef(a, b)[0, 1]) and abs(GF.series_corr(a, c)) < 0.2
    a2 = a.copy()
    a2[:10] = np.nan
    assert GF.series_corr(a2, b) == pytest.approx(np.corrcoef(a[10:], b[10:])[0, 1])             # only the days both have
    assert GF.series_corr(a[:15], b[:15]) != GF.series_corr(a[:15], b[:15])                       # fewer than 20 days: undefined
    assert GF.series_corr(np.ones(50), a[:50]) != GF.series_corr(np.ones(50), a[:50])             # no variance: undefined
    feats = {"A": a, "B": b, "C": c, "D": c + 0.05 * rng.normal(0, 1, 300)}
    kept, walk, left = GF.select_group(["A", "B", "C", "D"], feats.__getitem__, 5, 0.7, similarity=GF.series_corr)
    assert kept == ["A", "C"] and left == []
    by = {w["id"]: w for w in walk}
    assert by["B"]["with"] == "A" and by["B"]["max_corr"] > 0.9 and by["D"]["with"] == "C"
    # a NEGATIVE correlation of two difference series does not make them duplicates (the rule drops >= 0.7)
    kept, _, _ = GF.select_group(["A", "N"], {"A": a, "N": -a}.__getitem__, 5, 0.7, similarity=GF.series_corr)
    assert kept == ["A", "N"]


# ============================================================================================ the distinctness walk (standalone)
def _walk_inputs():
    rng = np.random.default_rng(0)
    base = rng.normal(size=(60, 80))
    other = rng.normal(size=base.shape)
    panels = {"A": base, "B": base + 0.05 * rng.normal(size=base.shape), "C": other, "D": base + 0.3 * rng.normal(size=base.shape),
              "E": other + 0.05 * rng.normal(size=base.shape)}
    return {k: dg.rank_rows(v) for k, v in panels.items()}


def test_the_walk_keeps_a_candidate_only_if_it_is_distinct_from_every_one_already_kept():
    ranks = _walk_inputs()
    kept, walk, left = GF.select_group(["A", "B", "C", "D", "E"], ranks.__getitem__, 5, 0.7)
    assert kept == ["A", "C"] and left == []
    by = {w["id"]: w for w in walk}
    assert by["B"]["decision"] == "dropped" and by["B"]["with"] == "A" and by["B"]["max_corr"] > 0.95
    assert by["D"]["decision"] == "dropped" and by["D"]["with"] == "A"
    # E is a copy of the SECOND one kept, not of the first: the walk compares against all of them
    assert by["E"]["decision"] == "dropped" and by["E"]["with"] == "C" and by["E"]["corr_with_kept"]["A"] < 0.2
    assert by["C"]["decision"] == "kept" and abs(by["C"]["max_corr"]) < 0.2
    assert [w["rank"] for w in walk] == [1, 2, 3, 4, 5]
    assert by["A"]["with"] is None and by["A"]["max_corr"] != by["A"]["max_corr"]       # nobody to compare with


def test_the_walk_stops_at_the_limit_and_asks_for_nothing_beyond_it():
    ranks = _walk_inputs()
    asked = []

    def ranks_of(k):
        asked.append(k)
        return ranks[k]
    kept, walk, left = GF.select_group(["A", "C", "B", "D"], ranks_of, 2, 0.7)
    assert kept == ["A", "C"] and left == ["B", "D"] and [w["id"] for w in walk] == ["A", "C"]
    assert asked == ["A", "C"]                                                       # B and D were never looked at
    kept, walk, left = GF.select_group(["A", "B", "C"], ranks.__getitem__, 1, 0.7)
    assert kept == ["A"] and left == ["B", "C"]


def test_fewer_than_the_limit_is_fine_and_so_is_nobody():
    ranks = _walk_inputs()
    kept, walk, left = GF.select_group(["A", "B", "D"], ranks.__getitem__, 3, 0.7)
    assert kept == ["A"] and left == [] and [w["decision"] for w in walk] == ["kept", "dropped", "dropped"]
    assert GF.select_group([], ranks.__getitem__, 3, 0.7) == ([], [], [])
    assert GF.select_group(["A"], ranks.__getitem__, 0, 0.7) == ([], [], ["A"])


def test_the_threshold_is_inclusive_and_an_undefined_correlation_does_not_drop():
    ranks = _walk_inputs()
    rho = GF.mean_daily_rank_corr(ranks["B"], ranks["A"])
    assert 0.95 < rho < 1
    assert GF.select_group(["A", "B"], ranks.__getitem__, 2, rho)[0] == ["A"]                 # corr == threshold: dropped (README: >= 0.7)
    assert GF.select_group(["A", "B"], ranks.__getitem__, 2, rho + 1e-9)[0] == ["A", "B"]
    flat = {"A": ranks["A"], "N": np.full_like(ranks["A"], np.nan), "K": np.ones_like(ranks["A"])}
    kept, walk, _ = GF.select_group(["A", "N", "K"], flat.__getitem__, 3, 0.7)
    assert kept == ["A", "N", "K"] and walk[1]["max_corr"] != walk[1]["max_corr"]


def test_the_traded_signal_is_direction_times_the_ema_at_the_half_life():
    rng = np.random.default_rng(2)
    raw = rng.normal(size=(50, 30)).astype(np.float32)
    for sign, hl in ((1.0, 0.0), (-1.0, 5.0), (1.0, 20.0)):
        got = GF.traded_ranks_in_sample(raw, sign, hl)
        want = dg.rank_rows(bk.smoothed(sign * raw.astype(np.float64), hl))
        assert np.array_equal(got, want, equal_nan=True)
    r1, r2 = GF.traded_ranks_in_sample(raw, 1.0, 0.0), GF.traded_ranks_in_sample(raw, -1.0, 0.0)
    assert np.allclose(r1 + r2, 31.0)                                              # a negative direction reverses the ranks of an unsmoothed signal


# ================================================================================================== paired statistics
def test_paired_stats_on_a_hand_made_series():
    a = np.tile([0.010, 0.002, -0.004, 0.006], 10)
    b = np.tile([0.004, 0.001, -0.002, 0.001], 10)
    d = np.tile([0.006, 0.001, -0.002, 0.005], 10)                                        # a - b: mean 0.0025, population std sqrt(1.025e-5)
    got = GF.paired_stats(a, b)
    std = np.sqrt(1.025e-5)
    assert got["n"] == 40
    assert got["ann"] == pytest.approx(0.0025 * 252)
    assert got["ir"] == pytest.approx(0.0025 / std * np.sqrt(252))
    assert got["t"] == pytest.approx(0.0025 / std * np.sqrt(40))
    assert got["t"] == pytest.approx(got["ir"] * np.sqrt(40 / 252))                       # t = ir x sqrt(years)
    assert GF.paired_stats(b, a)["ann"] == pytest.approx(-got["ann"]) and GF.paired_stats(b, a)["t"] == pytest.approx(-got["t"])
    assert GF.paired_stats(d + 1.0, np.full(40, 1.0)) == pytest.approx(got)               # only the difference matters
    a2, b2 = a.copy(), b.copy()
    a2[3], b2[10] = np.nan, np.nan
    g2 = GF.paired_stats(a2, b2)
    assert g2["n"] == 38 and np.isfinite(g2["t"])                                         # undefined days are skipped
    short = GF.paired_stats(a[:19], b[:19])
    assert short["n"] == 19 and all(np.isnan(short[k]) for k in ("ann", "ir", "t"))
    flat = GF.paired_stats(a, a)
    assert flat["n"] == 40 and all(np.isnan(flat[k]) for k in ("ann", "ir", "t"))


def test_paired_stats_is_the_function_scripts_sweep_final_runs():
    """Cut out of sweep_final.py (it is nested in a `with` block) and run on random series, NaNs included."""
    tree = ast.parse((H.SCRIPTS / "sweep_final.py").read_text(encoding="utf-8"))
    fn = next(n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name == "paired")
    ns = {"np": np}
    exec(compile(ast.Module(body=[fn], type_ignores=[]), "sweep_final.py", "exec"), ns)
    rng = np.random.default_rng(8)
    for n in (5, 19, 20, 21, 250):
        a, b = rng.normal(0.001, 0.01, n), rng.normal(0.0, 0.01, n)
        a[rng.random(n) < 0.1] = np.nan
        want, got = ns["paired"](a, b), GF.paired_stats(a, b)
        assert want.keys() == got.keys()
        for k in want:
            assert (want[k] != want[k] and got[k] != got[k]) or want[k] == pytest.approx(got[k], rel=1e-12, abs=0)
    z = np.zeros(30)
    assert ns["paired"](z, z)["t"] != ns["paired"](z, z)["t"] and GF.paired_stats(z, z)["t"] != GF.paired_stats(z, z)["t"]


# ==================================================================================================== exposure to size
def test_book_overlap_and_the_size_labels():
    held_a = np.zeros((3, 10), dtype=bool)
    held_b = np.zeros((3, 10), dtype=bool)
    held_a[0, :2], held_b[0, :2] = True, True                       # identical books: overlap 1
    held_a[1, :2], held_b[1, 1:3] = True, True                      # one name in common out of two
    held_a[2, :2] = True                                            # the other book holds nothing: undefined
    got = GF.book_overlap_by_day(held_a, held_b)
    assert got[0] == 1.0 and got[1] == 0.5 and np.isnan(got[2])
    held_c = np.zeros((1, 10), dtype=bool)
    held_c[0, :4] = True
    assert GF.book_overlap_by_day(held_a[:1], held_c)[0] == pytest.approx(2 / 4)       # unequal sizes: common / max(size_a, size_b)
    assert GF.book_overlap_by_day(held_c, held_a[:1])[0] == pytest.approx(2 / 4)       # symmetric
    # long_mask is the top decile by signal, ties by symbol order
    sm = np.arange(50, dtype=float)[None, :].repeat(2, 0)
    mask = GF.long_mask(sm)
    assert mask.sum(1).tolist() == [5, 5] and mask[0, 45:].all() and not mask[0, :45].any()
    # the labels: rank correlation >= 0.7, or overlap >= 0.5; either one is enough; undefined is not "size"
    assert GF.is_size_exposure(0.70, 0.0) and not GF.is_size_exposure(0.699, 0.0)
    assert GF.is_size_exposure(0.0, 0.50) and not GF.is_size_exposure(0.0, 0.499)
    assert GF.is_size_exposure(0.2, 0.9) and GF.is_size_exposure(0.9, 0.0) and not GF.is_size_exposure(0.2, 0.3)
    assert not GF.is_size_exposure(float("nan"), float("nan")) and GF.is_size_exposure(float("nan"), 0.6)


# ===================================================================================================== the verdicts
@pytest.mark.parametrize("t,ann_in,label", [
    (3.0, 0.02, "成立"), (2.0, 0.001, "成立"), (1.99, 0.02, "方向对、证据不够"), (1.0, 0.02, "方向对、证据不够"),
    (0.99, 0.02, "没有"), (0.0, 0.02, "没有"), (-0.001, 0.02, "更差"), (-3.0, -0.02, "更差"),
    (2.5, -0.01, "方向对、证据不够"), (2.5, 0.0, "方向对、证据不够"), (2.5, float("nan"), "方向对、证据不够"),   # t >= 2 but the in-sample difference is not positive
    (float("nan"), 0.02, GF.NA), (None, 0.02, GF.NA)])
def test_the_verdict_ladder(t, ann_in, label):
    assert GF.classify(t, ann_in) == label and GF.classify_vs_known(t, ann_in) == label


def test_the_level_criterion_and_its_noise_band():
    row = lambda ann, sh: {"long_ann": ann, "long_sharpe": sh}               # noqa: E731
    assert GF.level_reading(row(0.08, 1.0))["remains"] is True                  # Sharpe >= 1 is inclusive
    assert GF.level_reading(row(0.08, 0.999))["remains"] is False
    assert GF.level_reading(row(0.0, 1.5))["remains"] is False                  # the net excess must be positive
    assert GF.level_reading(row(-0.01, 1.5))["remains"] is False
    assert GF.level_reading(row(float("nan"), 1.5))["remains"] is False and GF.level_reading(row(0.05, float("nan")))["remains"] is False
    assert GF.level_reading(row(0.10, 1.6))["edge"] is False and GF.level_reading(row(0.10, 0.75))["edge"] is True       # +-0.3 Sharpe
    assert GF.level_reading(row(0.025, 2.0))["edge"] is True and GF.level_reading(row(-0.03, 0.2))["edge"] is True       # +-3 points
    assert GF.level_reading(row(0.12, 1.31))["edge"] is False


def test_the_level_criterion_is_asked_of_group_b_standalones_and_a_known_in_size_only():
    assert GF.needs_level("b_x", "standalone") and GF.needs_level("a_known_in_size", "ruler")
    assert not GF.needs_level("b_x", "modification") and not GF.needs_level("c_x", "standalone") and not GF.needs_level("d_x", "modification")
    assert not GF.needs_level("a_known_in_turn", "ruler") and not GF.needs_level("b_x_twin", "twin")


def _pair(t_oos, ann_in, ann_oos=0.01, n=700):
    return {"utrain": {"ann": ann_in, "ir": 0.0, "t": 0.0, "n": 900}, "oos": {"ann": ann_oos, "ir": 0.0, "t": t_oos, "n": n}}


ROW = {"long_ann": 0.07, "long_sharpe": 1.2}


def test_a_standalone_is_judged_against_the_known_family_and_size_exposure_relabels_only_an_established_one():
    j = GF.judge_convention("c_x", "standalone", "k_known", _pair(2.4, 0.03), _pair(2.4, 0.03), _pair(0.4, 0.02), ROW)
    assert j["label"] == "成立" and j["label_paired"] == "成立" and j["ref"] == "k_known" and j["level"] is None
    assert j["vs_ref"]["t_oos"] == 2.4 and j["vs_size"]["t_oos"] == 0.4                           # "有没有赢过小市值" is reported, and decides nothing
    j = GF.judge_convention("c_x", "standalone", "k_known", _pair(2.4, 0.03), None, None, ROW, is_size=True)
    assert j["label"] == "就是市值" and j["label_paired"] == "成立"
    for t, lab in ((1.5, "方向对、证据不够"), (0.5, "没有"), (-1.0, "更差")):                    # only 成立 is relabelled
        assert GF.judge_convention("c_x", "standalone", "k_known", _pair(t, 0.03), None, None, ROW, is_size=True)["label"] == lab
    j = GF.judge_convention("c_x", "standalone", "k_known", _pair(2.4, -0.03), None, None, ROW)
    assert j["label"] == "方向对、证据不够" and "样本内" in j["note"]
    same = {"utrain": _pair(0, 0)["utrain"], "oos": {"ann": float("nan"), "ir": float("nan"), "t": float("nan"), "n": 700}}
    j = GF.judge_convention("v_base", "ruler", "k_known", same, None, None, ROW)
    assert j["label"] == GF.NA and "逐日相同" in j["note"]
    short = {"utrain": same["utrain"], "oos": {**same["oos"], "n": 10}}
    assert GF.judge_convention("v_base", "ruler", "k_known", short, None, None, ROW)["note"] == ""
    assert GF.judge_convention("c_x", "standalone", "k_known", None, None, None, ROW)["label"] == GF.NA


def test_a_modification_is_judged_against_its_base_and_reports_the_known_family_as_a_description():
    j = GF.judge_convention("d_pen", "modification", "a_known_in_size", _pair(2.2, 0.02), _pair(0.5, 0.0), _pair(0.3, 0.0), ROW)
    assert j["label"] == "成立" and j["ref"] == "a_known_in_size" and j["vs_ref"]["t_oos"] == 2.2
    assert j["vs_known"]["t_oos"] == 0.5 and j["vs_size"]["t_oos"] == 0.3                       # description only
    j = GF.judge_convention("d_pen", "modification", "a_known_in_size", _pair(0.4, 0.02), _pair(3.0, 0.02), None, ROW)
    assert j["label"] == "没有" and j["vs_known"]["label"] == "成立"                          # a great difference vs the known family does not make it better than its carrier
    assert GF.judge_convention("d_pen", "modification", "a_known_in_size", _pair(2.2, 0.02), None, None, ROW, is_size=True)["label"] == "就是市值"
    assert GF.judge_convention("d_pen", "modification", "x_car", _pair(2.2, 0.02), None, None, ROW)["level"] is None


def test_rulers_are_described_and_never_relabelled_and_carriers_and_twins_get_no_verdict():
    j = GF.judge_convention("a_amt20", "ruler", "k_known", _pair(2.4, 0.03), None, None, ROW, is_size=True)
    assert j["label"] == "成立"                                                                  # the ladder's label, as a description; no 就是市值
    j = GF.judge_convention("e_main_only", "ruler", "k_known", _pair(-1.0, 0.03), None, None, ROW)
    assert j["label"] == "更差" and j["ref"] == "k_known"
    assert GF.judge_convention("k_known", "ruler", None, None, None, None, ROW)["label"] == "基准"
    for role, oid in (("carrier", "x_car"), ("twin", "b_x_twin")):
        j = GF.judge_convention(oid, role, None, _pair(2.4, 0.03), _pair(2.4, 0.03), _pair(2.4, 0.03), ROW, is_size=True)
        assert j["label"] == "一起读" and j["level"] is None and j["twin"] is None
    lv = GF.judge_convention("a_known_in_size", "ruler", "k_known", _pair(0.5, 0.0), None, None, ROW)["level"]
    assert lv["remains"] is True and lv["sharpe"] == 1.2
    assert GF.judge_convention("b_x", "standalone", "k_known", _pair(0.5, 0.0), None, None, {"long_ann": 0.07, "long_sharpe": 0.9})["level"]["remains"] is False
    assert GF.judge_convention("c_x", "standalone", "k_known", _pair(0.5, 0.0), None, None, ROW)["level"] is None


def test_the_twin_reading_is_parent_minus_twin_and_the_field_contributes_only_at_t_two():
    j = GF.judge_convention("c_p", "standalone", "k_known", _pair(0.5, 0.0), None, None, ROW, pair_twin=_pair(2.0, 0.01))
    assert j["twin"]["label"] == GF.TWIN_OK and j["twin"]["t_oos"] == 2.0
    for t, in_, lab in ((1.99, 0.01, "方向对、证据不够"), (0.5, 0.01, "没有"), (-0.5, 0.01, "更差"), (2.5, -0.01, "方向对、证据不够")):
        assert GF.judge_convention("c_p", "standalone", "k_known", _pair(0.5, 0.0), None, None, ROW, pair_twin=_pair(t, in_))["twin"]["label"] == lab
    assert GF.judge_convention("c_p", "standalone", "k_known", _pair(0.5, 0.0), None, None, ROW)["twin"] is None


def test_the_fixed_half_life_decides_when_the_two_reads_disagree_and_the_disagreement_is_written():
    fit = GF.judge_convention("b_x", "standalone", "k_known", _pair(2.4, 0.03), None, None, ROW, pair_twin=_pair(2.4, 0.01))          # 成立, level yes, twin contributes
    fix = GF.judge_convention("b_x", "standalone", "k_known", _pair(1.2, 0.03), None, None, {"long_ann": 0.07, "long_sharpe": 0.8}, pair_twin=_pair(0.2, 0.01))
    v = GF.combine_conventions(fit, fix, 5.0, 10.0)
    assert v["final"] == "方向对、证据不够" and v["final_level"]["remains"] is False and v["agree"] is False and v["final_twin"]["label"] == "没有"
    assert any("拟合半衰期 5" in n and "固定半衰期 10" in n and "以固定半衰期的为准" in n and "成立" in n for n in v["notes"])
    assert any("水平读数" in n for n in v["notes"]) and any("孪生" in n for n in v["notes"])
    same = GF.combine_conventions(fit, copy.deepcopy(fit), 10.0, 10.0)
    assert same["final"] == "成立" and same["agree"] is True and same["notes"] == []
    assert GF.combine_conventions(fix, fit, 5.0, 10.0)["final"] == "成立"
    plain = GF.judge_convention("c_x", "standalone", "k_known", _pair(1.2, 0.03), None, None, ROW)
    assert GF.combine_conventions(plain, plain, 3.0, 10.0)["final_level"] is None
    assert v["role"] == "standalone" and v["ref"] == "k_known"


# ====================================================================================================== multiplicity
def _picks(*specs):
    return {k: {"group": g, "label": lab, "t": t} for k, g, lab, t in specs}


ALWAYS, NEVER = (lambda a, b: True), (lambda a, b: False)


def test_a_lone_established_hypothesis_with_t_between_two_and_three_is_a_candidate():
    out = GF.apply_multiplicity(_picks(("a", "b_", "成立", 2.4), ("b", "b_", "没有", 0.5), ("c", "c_", "更差", -1.0)), ALWAYS)
    assert out["a"]["label"] == "候选成立" and "整轮只有这一个成立" in out["a"]["note"] and "2.40" in out["a"]["note"]
    assert out["b"] == {"label": "没有", "note": ""} and out["c"]["label"] == "更差"
    assert GF.apply_multiplicity({}, ALWAYS) == {}


def test_t_of_three_or_more_is_established_outright():
    assert GF.apply_multiplicity(_picks(("a", "b_", "成立", 3.0)), NEVER)["a"] == {"label": "成立", "note": ""}
    assert GF.apply_multiplicity(_picks(("a", "b_", "成立", 2.99)), NEVER)["a"]["label"] == "候选成立"
    assert GF.apply_multiplicity(_picks(("a", "b_", "成立", 2.0)), NEVER)["a"]["label"] == "候选成立"


def test_two_mutually_distinct_picks_of_one_group_both_established_are_established_outright():
    out = GF.apply_multiplicity(_picks(("a", "d_", "成立", 2.2), ("b", "d_", "成立", 2.6)), ALWAYS)
    assert out["a"]["label"] == out["b"]["label"] == "成立"
    out = GF.apply_multiplicity(_picks(("a", "d_", "成立", 2.2), ("b", "d_", "成立", 3.4)), NEVER)       # one of them clears three on its own; the other is a duplicate of it
    assert out["b"]["label"] == "成立" and out["a"]["label"] == "候选成立"
    out = GF.apply_multiplicity(_picks(("a", "d_", "成立", 2.2), ("b", "d_", "成立", 2.6)), NEVER)       # not distinct: one piece of evidence, counted twice
    assert out["a"]["label"] == out["b"]["label"] == "候选成立" and "同组里没有第二个互不相关的" in out["a"]["note"]


def test_established_picks_of_different_groups_do_not_confirm_each_other():
    out = GF.apply_multiplicity(_picks(("a", "b_", "成立", 2.2), ("b", "d_", "成立", 2.6), ("c", "d_", "没有", 0.1)), ALWAYS)
    assert out["a"]["label"] == out["b"]["label"] == "候选成立" and out["c"]["label"] == "没有"
    # ... unless a pick has a distinct, established partner of its own group
    out = GF.apply_multiplicity(_picks(("a", "b_", "成立", 2.2), ("b", "d_", "成立", 2.6), ("c", "d_", "成立", 2.3)), ALWAYS)
    assert out["a"]["label"] == "候选成立" and out["b"]["label"] == out["c"]["label"] == "成立"


def test_labels_other_than_established_are_never_touched_by_the_pass():
    picks = _picks(("a", "b_", "就是市值", 2.5), ("b", "b_", "方向对、证据不够", 1.5), ("c", "b_", "没有", 0.2), ("d", "b_", GF.NA, float("nan")))
    out = GF.apply_multiplicity(picks, ALWAYS)
    assert {k: v["label"] for k, v in out.items()} == {"a": "就是市值", "b": "方向对、证据不够", "c": "没有", "d": GF.NA}


# ========================================================================================================= guard etc
def test_prior_reads_sees_a_ledger_entry_of_the_stage_or_a_result_file(tmp_path):
    assert GF.prior_reads(tmp_path, "T001", "s1") == []
    lp = tmp_path / "runs" / "T001" / "ledger.json"
    Ledger(lp).record("holdout", 5, "an old read", "sweep_final_s1")
    Ledger(lp).record("holdout", 5, "another sweep", "group_final_s2")
    assert GF.prior_reads(tmp_path, "T001", "s1") == []
    Ledger(lp).record("holdout", 5, "the read", "group_final_s1")
    found = GF.prior_reads(tmp_path, "T001", "s1")
    assert len(found) == 1 and "ledger entry" in found[0]
    (tmp_path / "runs" / "T001" / "group_final_s3.json").write_text("{}", encoding="utf-8")
    assert "result file" in GF.prior_reads(tmp_path, "T001", "s3")[0]


def test_clean_makes_a_result_strict_json():
    out = GF.clean({"a": np.float32(1.5), "b": [np.nan, np.inf, np.int64(3)], "c": np.array([1.0, np.nan]), "d": np.bool_(True), 3: None})
    assert out == {"a": 1.5, "b": [None, None, 3], "c": [1.0, None], "d": True, "3": None}
    json.dumps(out, allow_nan=False)
    assert GF.same_number(float("nan"), float("nan")) and GF.same_number(1.0, 1.0 + 1e-12) and not GF.same_number(1.0, 1.1)


# ============================================================================================ the whole script
@pytest.fixture(scope="module")
def swept(tmp_path_factory):
    """scripts/sweep.py --only-extra on the synthetic world, once for the module."""
    saved = dict(SPLITS)
    root = tmp_path_factory.mktemp("sweep_root")
    w, entries = W.build()
    with pytest.MonkeyPatch.context() as mp:
        data = W.sweep(mp, root, w, entries)
    SPLITS.clear()
    SPLITS.update(saved)
    return types.SimpleNamespace(world=w, entries=entries, sweep=data, root=root)


@pytest.fixture
def root(swept, tmp_path):
    shutil.copytree(swept.root / "configs", tmp_path / "configs")
    (tmp_path / "runs" / "T001").mkdir(parents=True)
    shutil.copy(swept.root / "runs" / "T001" / "sweep_s1.json", tmp_path / "runs" / "T001" / "sweep_s1.json")
    return tmp_path


def run_gf(monkeypatch, root, world, argv, end=None):
    monkeypatch.setattr(GF, "PARTURA_ROOT", root)
    monkeypatch.setattr(GF, "PanelSet", H.fake_panelset(world))
    monkeypatch.setenv("PARTURA_LOCK_DIR", str(root / "locks"))
    return GF.main(["T001", "--end", end or world.dates[-1]] + list(argv))


def _load(root, name):
    text = (root / "runs" / "T001" / name).read_text(encoding="utf-8")

    def refuse(c):
        raise ValueError(f"not strict JSON: {c}")
    return json.loads(text, parse_constant=refuse)


def result(root):
    return _load(root, "group_final_s1.json")


def selection(root):
    return _load(root, "group_select_s1.json")["selection"]


@pytest.fixture(scope="module")
def read_once(swept, tmp_path_factory):
    """One real read of the synthetic world, shared by the tests that only look at its output."""
    saved = dict(SPLITS)
    root = tmp_path_factory.mktemp("read_root")
    shutil.copytree(swept.root / "configs", root / "configs")
    (root / "runs" / "T001").mkdir(parents=True)
    shutil.copy(swept.root / "runs" / "T001" / "sweep_s1.json", root / "runs" / "T001" / "sweep_s1.json")
    import contextlib
    import io
    buf = io.StringIO()
    with pytest.MonkeyPatch.context() as mp, contextlib.redirect_stdout(buf):
        mp.setenv("PARTURA_RANK_DEVICE", "")
        rc = run_gf(mp, root, swept.world, [])
    SPLITS.clear()
    SPLITS.update(saved)
    assert rc == 0
    return types.SimpleNamespace(root=root, out=result(root), text=buf.getvalue())


def test_the_synthetic_sweep_is_what_the_tests_below_assume(swept):
    R = swept.sweep["results"]
    assert {k for k in R if k.startswith("a_")} == {k for k in W.R_EXPR if k.startswith("a_")}
    assert {k: R[k]["sign_locked"] for k in W.R_EXPR if k.startswith("a_")} == {k: k in W.A_LOCKED for k in W.R_EXPR if k.startswith("a_")}
    assert R["a_tsize"]["sign"] == 1.0 and R["a_tsize"]["sign_ic"] == -1.0 and R["a_tsize"]["sign_by"] == "locked"
    assert R["a_turn20"]["sign"] == -1.0 and R["a_turn20"]["sign_by"] == "long_book"
    assert swept.sweep.get("only_extra") is True
    # base / twin / declared kind / lock travel from the hypotheses file into the sweep file
    assert {k: v["base"] for k, v in R.items() if v.get("base")} == {**W.BASES, **W.RULER_BASES}
    assert {k: v["twin"] for k, v in R.items() if v.get("twin")} == W.TWIN_KEYS
    assert [k for k, v in R.items() if v.get("declared_kind")] == ["x_car", "x_car2"] and R["x_car"]["declared_kind"] == "carrier"
    assert {k for k, v in R.items() if v.get("lock")} == set(W.A_LOCKED) | set(W.H_LOCKED)


def test_both_selection_paths_and_the_read_along_set(monkeypatch, root, swept, capsys):
    R = swept.sweep["results"]
    assert run_gf(monkeypatch, root, swept.world, ["--dry-run", "--per-group", "3"]) == 0
    sel = selection(root)
    g = sel["groups"]
    sharpe = lambda k: R[k]["utrain_long"]["long_sharpe"]                       # noqa: E731
    # --- standalone path (group B): gates, then Sharpe, then the rank-correlation walk
    sb = g["b_"]["standalone"]
    assert set(sb["eligible"]) == {"b_strong", "b_dup", "b_alt", "b_coarse"} and sb["eligible"] == sorted(sb["eligible"], key=lambda k: (-sharpe(k), k))
    assert set(sb["gate_fail"]) == {"b_lowcov", "b_wrong"}                       # coverage / distinctness / locked-wrong-way
    top = max(("b_strong", "b_dup"), key=sharpe)
    other = "b_dup" if top == "b_strong" else "b_strong"
    assert set(sb["kept"]) == {top, "b_alt"}                                      # the near copies go; fewer than 3 is fine
    walk = {w["id"]: w for w in sb["walk"]}
    assert walk[other]["decision"] == "dropped" and walk[other]["with"] == top and walk[other]["max_corr"] >= 0.7 and walk["b_coarse"]["decision"] == "dropped"
    assert g["b_"]["modification"]["gated"] == [] and g["b_"]["modification"]["kept"] == []         # a group with an empty list for one type is normal
    # --- modification path (group D): the difference against the base, in-sample, built from the panels
    md = g["d_"]["modification"]
    assert set(md["gated"]) == {"d_pen1", "d_pen2", "d_pen3", "d_noop", "d_bad"}                 # d_pen1_twin has a base but is a twin: it never competes
    assert set(md["eligible"]) == {"d_pen1", "d_pen2", "d_pen3"}
    assert "identically zero" in md["not_eligible"]["d_noop"][0] and "train" in " ".join(md["not_eligible"]["d_bad"]) and "valid" in " ".join(md["not_eligible"]["d_bad"])
    assert md["eligible"] == sorted(md["eligible"], key=lambda k: (-md["stats"][k]["ir"], k))     # ranked by the information ratio of the difference
    pen = max(("d_pen1", "d_pen2"), key=lambda k: md["stats"][k]["ir"])
    pen_other = "d_pen1" if pen == "d_pen2" else "d_pen2"
    assert set(md["kept"]) == {pen, "d_pen3"}
    mw = {w["id"]: w for w in md["walk"]}
    assert mw[pen_other]["decision"] == "dropped" and mw[pen_other]["with"] == pen and mw[pen_other]["max_corr"] >= 0.7
    assert mw["d_pen3"]["decision"] == "kept" and mw["d_pen3"]["max_corr"] < 0.7
    # the in-sample difference statistics are the ones of the books rebuilt from the panels (not of summary numbers)
    w_ = swept.world
    us = slice(0, w_.cut["valid_end"])

    def net(k):
        sm = bk.smoothed(R[k]["sign"] * w_.panels[R[k]["expr"]].astype(np.float64)[: us.stop], R[k]["hl_long_u"])
        return bk.long_book(long_short_weights(sm, bk.TOP_FRAC), sm, w_.target[: us.stop])[0]
    d = net("d_pen3") - net("x_car")
    fin = np.isfinite(d)
    assert md["stats"]["d_pen3"]["ir"] == pytest.approx(d[fin].mean() / d[fin].std() * np.sqrt(252), rel=1e-9)
    tr = np.arange(us.stop) < w_.cut["train_end"]
    assert md["stats"]["d_pen3"]["mean_train"] == pytest.approx(d[tr & fin].mean(), rel=1e-9)
    assert md["stats"]["d_pen3"]["mean_valid"] == pytest.approx(d[~tr & fin].mean(), rel=1e-9)
    # --- group E has no standalone hypothesis at all; its modifications are judged against k_known
    assert g["e_"]["standalone"]["eligible"] == [] and g["e_"]["standalone"]["kept"] == [] and g["e_"]["modification"]["kept"] == ["e_screen"]
    assert g["c_"]["standalone"]["kept"] == ["c_solo"] and g["c_"]["modification"]["kept"] == ["c_mod"]
    # --- who is read: the rulers, every pick, the base of every selected modification, the twin of every pick
    d_kept = g["d_"]["standalone"]["kept"]
    assert len(d_kept) == 1 and d_kept[0] in ("d_one", "d_two")
    picks = {top, "b_alt", "c_solo", "c_mod", d_kept[0], pen, "d_pen3", "e_screen"}
    twins = {"b_alt_twin", "c_solo_twin", "e_screen_twin"} | ({"k_known"} if top == "b_dup" else set()) | ({"d_two"} if d_kept[0] == "d_one" else set())
    assert set(sel["read"]) == set(GF.DEFAULT_RULERS) | picks | {"x_car", "x_car2"} | twins          # x_car's own base is read too: a chain is followed
    roles = sel["roles"]
    assert {k for k, i in roles.items() if i["role"] == "ruler"} == set(GF.DEFAULT_RULERS)
    assert {k for k, i in roles.items() if i["role"] == "standalone"} == {top, "b_alt", "c_solo", d_kept[0]}
    assert {k for k, i in roles.items() if i["role"] == "modification"} == {"c_mod", pen, "d_pen3", "e_screen"}
    assert roles["x_car"] == {"role": "carrier", "group": "d_", "needed_by": ["d_pen3"]}
    assert roles["x_car2"] == {"role": "carrier", "group": "d_", "needed_by": ["x_car"]}
    assert roles["c_solo_twin"]["role"] == "twin" and roles["c_solo_twin"]["needed_by"] == ["c_solo"]
    assert "d_pen1_twin" not in roles and "e_lowcov" not in roles and "b_wrong" not in roles       # a twin of an unselected pick is not read; nor a gate failure
    assert roles["a_known_in_size"]["role"] == "ruler"                                               # the base of d_pen*: a ruler already, read once, as a ruler
    # nothing out of sample: no result file, no ledger anywhere; the in-sample reproduction check ran and passed
    assert not (root / "runs" / "T001" / "group_final_s1.json").exists()
    assert not (root / "runs" / "T001" / "ledger.json").exists() and not (root / "runs" / "_forward").exists()
    out = capsys.readouterr().out
    assert "没有读任何样本外数字" in out and "复现检查" in out and "通过" in out and "样本外读数" not in out and "暴露" in out


def test_the_selection_cannot_see_anything_after_the_in_sample_period(monkeypatch, root, swept):
    """Same sweep, same in-sample days, OTHER out-of-sample days (labels and panels replaced by noise): an identical selection,
    identical correlations to the last digit -- for both selection paths."""
    w = swept.world
    n_in = w.cut["valid_end"]
    w2 = copy.deepcopy(w)
    rng = np.random.default_rng(99)
    w2.target[n_in:] = rng.normal(0, 0.05, w2.target[n_in:].shape)
    for e in w2.panels:
        w2.panels[e][n_in:] = rng.normal(size=w2.panels[e][n_in:].shape).astype(np.float32)
    run_gf(monkeypatch, root, w, ["--dry-run", "--per-group", "3"])
    a = _load(root, "group_select_s1.json")
    run_gf(monkeypatch, root, w2, ["--dry-run", "--per-group", "3"])
    b = _load(root, "group_select_s1.json")
    assert a["selection"] == b["selection"] and a["repro"] == b["repro"] and a["exposure"] == b["exposure"]
    assert a["repro"]["pass"] is True and a["selection"]["groups"]["d_"]["modification"]["walk"]
    assert not np.allclose(np.nan_to_num(w.target[n_in:]), np.nan_to_num(w2.target[n_in:]))     # ... while the poisoned world really is another world


def test_the_read_is_ledgered_and_happens_once(monkeypatch, root, swept, capsys):
    w = swept.world
    assert run_gf(monkeypatch, root, w, ["--per-group", "3"]) == 0
    out = result(root)
    n = len(out["selection"]["read"])
    entries = Ledger(root / "runs" / "T001" / "ledger.json").entries
    assert [(e.split, e.stage, e.n_expressions) for e in entries] == [("holdout", "group_final_s1", n)]
    fwd = Ledger(root / "runs" / "_forward" / "ledger.json").entries
    assert [(e.split, e.stage, e.n_expressions) for e in fwd] == [("forward", "group_final_T001_s1", n)]
    assert w.dates[w.cut["holdout_end"]] in fwd[0].purpose and w.dates[-1] in fwd[0].purpose
    text = capsys.readouterr().out
    assert "样本外读数" in text and "判读汇总" in text
    # a second read of the same sweep tag is refused -- before anything is computed
    monkeypatch.setattr(GF, "PanelSet", lambda *a, **k: (_ for _ in ()).throw(AssertionError("must refuse before building panels")))
    monkeypatch.setattr(GF, "PARTURA_ROOT", root)
    with pytest.raises(SystemExit, match="--again"):
        GF.main(["T001", "--end", w.dates[-1]])
    assert len(Ledger(root / "runs" / "T001" / "ledger.json").entries) == 1
    # a dry run is not a read: it is still allowed
    assert run_gf(monkeypatch, root, w, ["--dry-run"]) == 0
    assert len(Ledger(root / "runs" / "T001" / "ledger.json").entries) == 1
    # --again reads again, and says so in the ledger
    assert run_gf(monkeypatch, root, w, ["--again"]) == 0
    entries = Ledger(root / "runs" / "T001" / "ledger.json").entries
    assert len(entries) == 2 and "AGAIN" in entries[1].purpose and "AGAIN" not in entries[0].purpose
    assert len(Ledger(root / "runs" / "_forward" / "ledger.json").entries) == 2
    assert result(root)["args"]["again"] is True
    # a result file alone also counts as "already read"
    (root / "runs" / "T001" / "ledger.json").unlink()
    monkeypatch.undo()
    monkeypatch.setattr(GF, "PARTURA_ROOT", root)
    with pytest.raises(SystemExit, match="already read"):
        GF.main(["T001", "--end", w.dates[-1]])


def test_every_object_is_read_in_the_direction_the_sweep_recorded_and_the_locked_ones_are_marked(read_once, swept):
    R = swept.sweep["results"]
    out, text = read_once.out, read_once.text
    res = out["results"]
    assert set(res) == set(out["selection"]["read"])
    for k, r in res.items():
        assert r["sign_user"] == R[k]["sign"], k                                  # EVERY object, the original and the benchmarks included
        assert r["sign_locked"] is bool(R[k]["sign_locked"]) and r["sign_by"] == R[k]["sign_by"], k
    assert all(res[k]["sign_locked"] and res[k]["sign_user"] == 1.0 for k in W.A_LOCKED)
    assert all(not res[k]["sign_locked"] for k in ("a_turn20", "a_amt20", "v_base", "k_known"))
    assert res["k_known_xfrozen"]["sign_user"] == 1.0 and res["k_known_xfrozen"]["sign_ic_utrain"] == -1.0 and res["k_known_xfrozen"]["sign_flip"] is True
    assert res["a_tsize"]["sign_user"] == 1.0 and res["a_tsize"]["sign_ic_utrain"] == -1.0 and res["a_tsize"]["sign_flip"] is True
    assert res["a_turn20"]["sign_user"] == -1.0 and res["a_turn20"]["sign_by"] == "long_book"
    assert out["selection"]["locked"] == [k for k in out["selection"]["read"] if res[k]["sign_locked"]]
    assert res["a_tsize"]["conv"]["fitted"]["books"]["holdout"]["long_ann"] < 0                  # read as written: a ruler that points the wrong way loses
    assert "| a_tsize | 尺子 | +1 锁 |" in text and "| a_turn20 | 尺子 | -1 |" in text


def test_the_numbers_are_the_books_of_the_rule_recomputed_from_the_raw_panels(read_once, swept):
    w, R = swept.world, swept.sweep["results"]
    out = read_once.out
    n_in, n_ho, n = w.cut["valid_end"], w.cut["holdout_end"], len(w.dates)
    us, ho, fw, oos = slice(0, n_in), slice(n_in, n_ho), slice(n_ho, n), slice(n_in, n)
    tgt = w.target

    def net(sm, sl):
        return bk.long_book(long_short_weights(sm[sl], bk.TOP_FRAC), sm[sl], tgt[sl])[0]

    series = {}
    names = ["k_known", "a_known_in_size", "c_solo", "c_mod", "d_pen3", "x_car"]
    for k in names:
        raw = w.panels[R[k]["expr"]].astype(np.float64)
        sign = R[k]["sign"]
        hl_fit = bk.fit_halflives(sign * raw, tgt[:n_in], us)["hl_long"]
        for conv, hl in (("fitted", hl_fit), ("fixed", 10.0)):
            sm = bk.smoothed(sign * raw, hl)
            c = out["results"][k]["conv"][conv]
            assert c["hl"] == hl
            for nm, sl in (("utrain", us), ("holdout", ho), ("forward", fw), ("oos", oos)):
                want = bk.book_row(sm, tgt, sl)
                for key in ("long_ann", "long_sharpe", "long_mdd", "long_turnover"):
                    assert c["books"][nm][key] == pytest.approx(want[key], rel=1e-12, abs=1e-15), (k, conv, nm, key)
            series[(k, conv)] = {"utrain": net(sm, us), "holdout": net(sm, ho), "forward": net(sm, fw)}
            series[(k, conv)]["oos"] = np.concatenate([series[(k, conv)]["holdout"], series[(k, conv)]["forward"]])   # as idea_final: two books, started apart

    def check(obj, ref):
        for conv in ("fitted", "fixed"):
            for nm in ("utrain", "holdout", "forward", "oos"):
                want = GF.paired_stats(series[(obj, conv)][nm], series[(ref, conv)][nm])
                assert out["paired"][ref][obj][conv][nm] == pytest.approx(want, nan_ok=True), (obj, ref, conv, nm)
    for obj in ("c_solo", "c_mod", "d_pen3", "a_known_in_size"):
        check(obj, "k_known")                                                      # the description every object carries (c_mod: also its base)
    check("d_pen3", "x_car")                                                       # a modification against its own carrier
    assert "k_known" not in out["paired"]["k_known"] and "a_size" not in out["paired"]["a_size"]
    # the per-day series and their calendar, for charts
    assert out["dates"]["utrain"] == w.dates[:n_in] and out["dates"]["holdout"] == w.dates[n_in:n_ho] and out["dates"]["forward"] == w.dates[n_ho:]
    got = np.array([np.nan if v is None else v for v in out["series"]["c_solo"]["fitted"]["holdout"]])
    assert np.allclose(got, series[("c_solo", "fitted")]["holdout"], atol=1e-7, equal_nan=True) and got.size == n_ho - n_in
    assert set(out["series"]["c_solo"]["fixed"]) == {"utrain", "holdout", "forward"}
    assert out["periods"]["forward"] == [w.dates[n_ho], w.dates[-1]] and out["periods"]["oos"] == [w.dates[n_in], w.dates[-1]]
    assert out["years"]["forward"] == pytest.approx(np.isfinite(tgt[fw]).any(1).sum() / 252.0)


def test_each_verdict_rests_on_the_difference_the_amended_rule_names(read_once, swept):
    out = read_once.out
    v, paired = out["verdicts"], out["paired"]
    sel = out["selection"]["groups"]
    for pfx, g in sel.items():
        for k in g["standalone"]["kept"]:
            assert v[k]["ref"] == "k_known" and v[k]["role"] == "standalone"
            assert v[k]["fixed"]["vs_ref"]["t_oos"] == pytest.approx(paired["k_known"][k]["fixed"]["oos"]["t"])
        for k in g["modification"]["kept"]:
            base = swept.sweep["results"][k]["base"]
            assert v[k]["ref"] == base and v[k]["role"] == "modification"
            assert v[k]["fixed"]["vs_ref"]["t_oos"] == pytest.approx(paired[base][k]["fixed"]["oos"]["t"])
            assert v[k]["fixed"]["vs_known"]["t_oos"] == pytest.approx(paired["k_known"][k]["fixed"]["oos"]["t"])                            # also reported against the known family
            assert v[k]["fixed"]["vs_size"]["t_oos"] == pytest.approx(paired["a_size"][k]["fixed"]["oos"]["t"])                              # "有没有赢过小市值"
    for k, b in W.RULER_BASES.items():                                              # a ruler that carries a base is read against it
        assert v[k]["ref"] == b and v[k]["role"] == "ruler" and v[k]["fixed"]["vs_ref"]["t_oos"] == pytest.approx(paired[b][k]["fixed"]["oos"]["t"])
    assert v["a_size"]["ref"] == "k_known" and v["k_known"]["fixed"]["label"] == "基准"
    assert v["x_car"]["fixed"]["label"] == "一起读" and v["c_solo_twin"]["fixed"]["label"] == "一起读" and v["x_car"]["ref"] is None      # carriers and twins: read along only
    for k, vv in v.items():                                                          # the final label is the fixed half-life's (before the multiplicity pass); a disagreement is written out
        assert vv["final_paired"] == vv["fixed"]["label"]
        assert vv["agree"] == (not any("不一致" in n for n in vv["notes"]))


def test_a_twin_is_read_and_parent_minus_twin_is_reported_whichever_way_it_was_declared(read_once, swept):
    out = read_once.out
    v, paired, sel = out["verdicts"], out["paired"], out["selection"]["groups"]
    # by name: c_solo / c_solo_twin
    assert out["results"]["c_solo"]["twin"] == "c_solo_twin" and out["roles"]["c_solo_twin"]["role"] == "twin"
    tw = v["c_solo"]["fixed"]["twin"]
    assert tw["t_oos"] == pytest.approx(paired["c_solo_twin"]["c_solo"]["fixed"]["oos"]["t"])
    assert tw["label"] == (GF.TWIN_OK if GF.classify(tw["t_oos"], tw["ann_in"]) == "成立" else GF.classify(tw["t_oos"], tw["ann_in"]))
    # by the explicit key: a twin that is an existing object (here the known family), and another hypothesis
    if "b_dup" in sel["b_"]["standalone"]["kept"]:
        assert out["results"]["b_dup"]["twin"] == "k_known" and v["b_dup"]["fixed"]["twin"]["t_oos"] == pytest.approx(paired["k_known"]["b_dup"]["fixed"]["oos"]["t"])
    if sel["d_"]["standalone"]["kept"] == ["d_one"]:
        assert out["results"]["d_one"]["twin"] == "d_two" and out["roles"]["d_two"]["role"] == "twin"          # read along, though it is a standalone by itself
        assert v["d_one"]["fixed"]["twin"]["t_oos"] == pytest.approx(paired["d_two"]["d_one"]["fixed"]["oos"]["t"])
    assert v["d_pen3"]["fixed"]["twin"] is None and out["results"]["d_pen3"]["twin"] is None            # a hypothesis without a twin has no twin reading
    assert "d_pen1_twin" not in out["results"]                                                           # an unselected hypothesis' twin is not read


def test_the_exposure_numbers_are_the_insample_rank_correlation_and_book_overlap_with_a_size(read_once, swept):
    w, R = swept.world, swept.sweep["results"]
    out = read_once.out
    n_in = w.cut["valid_end"]

    def traded(k):
        r = out["results"][k]
        return bk.smoothed(r["sign_user"] * w.panels[R[k]["expr"]].astype(np.float64)[:n_in], r["fit"]["hl_long"])

    def spearman_days(a, b):
        cs = []
        for t in range(n_in):
            m = np.isfinite(a[t]) & np.isfinite(b[t])
            if m.sum() < 3:
                continue
            ra, rb = np.argsort(np.argsort(a[t, m])), np.argsort(np.argsort(b[t, m]))
            cs.append(np.corrcoef(ra, rb)[0, 1])
        return float(np.mean(cs))

    def overlap_days(a, b):
        ov = []
        for t in range(n_in):
            top = []
            for x in (a, b):
                idx = np.nonzero(np.isfinite(x[t]))[0]
                k = max(1, int(np.floor(idx.size * 0.1)))
                order = idx[np.argsort(x[t, idx], kind="stable")]
                top.append(set(order[-k:].tolist()))
            ov.append(len(top[0] & top[1]) / max(len(top[0]), len(top[1])))
        return float(np.mean(ov))
    size = traded("a_size")
    for k in ("b_alt", "a_amt20", "c_mod", "a_known_in_size"):
        e = out["results"][k]["exposure"]
        assert e["rank_corr_size"] == pytest.approx(spearman_days(traded(k), size), abs=1e-9), k
        assert e["book_overlap_size"] == pytest.approx(overlap_days(traded(k), size), abs=1e-9), k
    for k, r in out["results"].items():                                              # both numbers for EVERY object read, and the label follows them
        e = r["exposure"]
        assert e["rank_corr_size"] == e["rank_corr_size"] and e["book_overlap_size"] == e["book_overlap_size"]
        assert e["is_size"] is bool(e["rank_corr_size"] >= 0.7 or e["book_overlap_size"] >= 0.5), k
    assert out["results"]["a_size"]["exposure"] == {"rank_corr_size": 1.0, "book_overlap_size": 1.0, "is_size": True}
    flags = {k: r["exposure"]["is_size"] for k, r in out["results"].items()}
    assert any(flags.values()) and not all(flags.values())                           # the synthetic world has both kinds
    # the label: 成立 against the reference AND size exposure -> 就是市值; any other label stands
    for k, vv in out["verdicts"].items():
        if vv["role"] in ("standalone", "modification"):
            for conv in ("fitted", "fixed"):
                j = vv[conv]
                assert j["label"] == ("就是市值" if (j["label_paired"] == "成立" and flags[k]) else j["label_paired"]), (k, conv)


def test_a_modification_reports_how_much_of_its_carriers_book_it_changes(read_once, swept):
    w, R = swept.world, swept.sweep["results"]
    out = read_once.out
    n_in, n = w.cut["valid_end"], len(w.dates)
    assert {k for k, r in out["results"].items() if "changed_share" in r} == {k for k, i in out["roles"].items() if i["role"] == "modification"}
    for k in ("d_pen3", "c_mod"):
        base = R[k]["base"]
        for conv in ("fitted", "fixed"):
            held = {}
            for o in (k, base):
                hl = out["results"][o]["conv"][conv]["hl"]
                sm = bk.smoothed(out["results"][o]["sign_user"] * w.panels[R[o]["expr"]].astype(np.float64), hl)
                held[o] = long_short_weights(sm, bk.TOP_FRAC) > 0
            by_day = np.array([(held[k][t] & held[base][t]).sum() / max(held[k][t].sum(), held[base][t].sum()) if held[k][t].any() and held[base][t].any() else np.nan for t in range(n)])
            ch = out["results"][k]["changed_share"][conv]
            assert ch["in_sample"] == pytest.approx(1 - np.nanmean(by_day[:n_in]), abs=1e-9)
            assert ch["oos"] == pytest.approx(1 - np.nanmean(by_day[n_in:]), abs=1e-9)
            assert 0.0 < ch["in_sample"] < 1.0 and 0.0 < ch["oos"] < 1.0


def test_the_multiplicity_pass_is_applied_to_the_selected_hypotheses_verdicts(monkeypatch, root, swept):
    """Lower the bar for 'established' so that several picks reach it, and check the pass against a hand count of the output."""
    monkeypatch.setattr(GF, "T_ESTABLISHED", -1e9)
    monkeypatch.setattr(GF, "T_OUTRIGHT", 1e9)                                       # nothing is outright: only a distinct same-group partner confirms
    assert run_gf(monkeypatch, root, swept.world, []) == 0
    out = result(root)
    v, info = out["verdicts"], out["roles"]
    picks = [k for k, i in info.items() if i["role"] in ("standalone", "modification")]
    est = [k for k in picks if v[k]["final_paired"] == "成立"]
    assert len(est) >= 3                                                              # the lowered bar lets most of them through (those with a positive in-sample difference)
    series = {k: np.array([np.nan if x is None else x for x in out["series"][k]["fixed"]["utrain"]]) for k in out["series"]}

    def evidence(k):
        return series[k] - series[v[k]["ref"]]

    def distinct(a, b):
        return info[a]["role"] == info[b]["role"] or not (GF.series_corr(evidence(a), evidence(b)) >= 0.7)
    for k in picks:
        if k in est:
            partner = [j for j in est if j != k and info[j]["group"] == info[k]["group"] and distinct(k, j)]
            assert v[k]["final"] == ("成立" if partner else "候选成立"), k
        else:
            assert v[k]["final"] == v[k]["final_paired"], k
    assert any(v[k]["final"] == "候选成立" for k in est) and any(v[k]["final"] == "成立" for k in est)
    assert all("多重比较" in " ".join(v[k]["notes"]) for k in est if v[k]["final"] == "候选成立")
    # rulers are descriptions: their labels are not touched, and carriers / twins have none
    assert all(v[k]["final"] == v[k]["final_paired"] for k, i in info.items() if i["role"] not in ("standalone", "modification"))


def test_the_level_criterion_appears_for_b_standalones_and_a_known_in_size_only(read_once):
    out = read_once.out
    have = {k for k, v in out["verdicts"].items() if v["final_level"] is not None}
    b_stand = {k for k, i in out["roles"].items() if i["role"] == "standalone" and i["group"] == "b_"}
    assert have == b_stand | {"a_known_in_size"} and b_stand
    for k in have:
        lv = out["verdicts"][k]["final_level"]
        row = out["results"][k]["conv"]["fixed"]["books"]["oos"]
        assert lv["remains"] == bool(row["long_ann"] > 0 and row["long_sharpe"] >= 1.0)


def test_the_printed_tables_carry_the_new_columns(read_once):
    text = read_once.text
    for needle in ("## 尺子(总是读;描述,不拿来挑)", "独立假设", "修改型假设(对自己的载体判)", "一起读的载体与孪生", "有没有赢过小市值", "改动载体多大比例",
                   "父 − 孪生", "秩相关 / 书重合", "判读汇总", "就是市值?", "d_pen3", "x_car"):
        assert needle in text, needle


def test_the_numbers_of_the_user_convention_are_the_ones_scripts_sweep_final_reads(monkeypatch, root, swept):
    """Run the REAL sweep_final.py on the same sweep and compare, number for number, with group_final's fitted-half-life read of
    the same objects (user's training-period half-life, direction as picked, pure-long book net of 15 bp)."""
    w = swept.world
    ids = ["a_tsize", "a_size", "b_alt", "c_solo", "d_pen3"]
    H.run_script(monkeypatch, root, "sweep_final.py", ["T001", "--sweep", "s1", "--ids", ",".join(ids)], H.fake_panelset(w))
    old = json.loads((root / "runs" / "T001" / "sweepfinal_s1.json").read_text(encoding="utf-8"))["results"]
    for p in (root / "runs" / "T001").glob("ledger.json"):
        p.unlink()                                                              # sweep_final ledgered its own read; this is a separate one
    run_gf(monkeypatch, root, w, [])
    out = result(root)
    compared = 0
    for k, r in old.items():
        if k not in out["results"]:
            continue
        mine = out["results"][k]
        if mine["sign_user"] != r["sign_user"]:
            continue                                                           # the original / benchmarks: sweep_final re-derives the sign from the rank IC
        theirs = r["books_user"]["by_rank"]["long"]
        assert mine["conv"]["fitted"]["hl"] == theirs["hl"], k
        for nm in ("utrain", "holdout"):
            for key in ("long_ann", "long_sharpe", "long_turnover", "long_mdd"):
                got = mine["conv"]["fitted"]["books"][nm][key]
                assert got == pytest.approx(theirs["splits"][nm][key], rel=1e-12, abs=1e-15), (k, nm, key)
        if k != "k_known" and out["results"]["k_known"]["sign_user"] == old["k_known"]["sign_user"]:           # same direction for the reference too
            for nm in ("utrain", "holdout"):
                got = {a: (np.nan if b is None else b) for a, b in out["paired"]["k_known"][k]["fitted"][nm].items()}
                assert got == pytest.approx(r["paired"]["k_known"][nm], nan_ok=True), (k, nm)
        compared += 1
    assert compared >= 5        # the objects of the first line above, v_base / k_known / k_known_xfrozen where the signs agree


def test_a_sweep_that_does_not_reproduce_on_the_view_stops_everything_before_a_number_exists(monkeypatch, root, swept, capsys):
    path = root / "runs" / "T001" / "sweep_s1.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data["results"]["a_tsize"]["utrain_long"]["long_sharpe"] += 0.5
    path.write_text(json.dumps(data), encoding="utf-8")
    rc = run_gf(monkeypatch, root, swept.world, [])
    out = capsys.readouterr().out
    assert rc == 4 and "a_tsize" in out and "do not reproduce" in out and "未通过" in out
    assert not (root / "runs" / "T001" / "group_final_s1.json").exists() and not (root / "runs" / "T001" / "ledger.json").exists()
    assert not (root / "runs" / "_forward").exists()
    assert run_gf(monkeypatch, root, swept.world, ["--tol-sharpe", "0.6"]) == 0                  # the same failure, with the tolerance opened up, goes through
    assert (root / "runs" / "T001" / "group_final_s1.json").exists()


def test_without_a_forward_segment_the_combined_period_is_the_test_period(monkeypatch, root, swept, capsys):
    w = swept.world
    end = w.dates[w.cut["holdout_end"] - 1]                                  # the view ends with the holdout
    assert run_gf(monkeypatch, root, w, [], end=end) == 0
    out = result(root)
    assert out["periods"]["forward"] is None and out["periods"]["oos"] == out["periods"]["holdout"]
    k = out["results"]["c_solo"]["conv"]["fitted"]["books"]
    assert "forward" not in k and k["oos"] == k["holdout"]
    assert not (root / "runs" / "_forward").exists()                         # no forward segment, no forward ledger entry
    assert len(Ledger(root / "runs" / "T001" / "ledger.json").entries) == 1
    assert "没有前推段" in capsys.readouterr().out


def test_always_groups_and_pair_options(monkeypatch, root, swept):
    run_gf(monkeypatch, root, swept.world, ["--dry-run", "--groups", "c_", "--always", "a_tsize", "--pair", "k_known,a_tsize"])
    sel = selection(root)
    assert sel["rulers"] == ["v_base", "k_known", "k_known_xfrozen", "a_tsize"] and list(sel["groups"]) == ["c_"]
    assert {k for k, i in sel["roles"].items() if i["role"] == "ruler"} == {"v_base", "k_known", "k_known_xfrozen", "a_tsize"}
    assert set(sel["read"]) >= {"c_solo", "c_mod", "c_solo_twin"}
    with pytest.raises(SystemExit, match="not in the sweep"):
        run_gf(monkeypatch, root, swept.world, ["--dry-run", "--always", "a_nonesuch"])
    # --pair only adds references: the verdicts are defined against k_known (and described against a_size) whatever it says
    assert run_gf(monkeypatch, root, swept.world, ["--groups", "c_", "--always", "a_tsize", "--pair", "a_tsize", "--again"]) == 0
    out = result(root)
    assert out["verdicts"]["c_solo"]["fixed"]["vs_ref"] is not None and "c_solo" in out["paired"]["k_known"] and "a_tsize" in out["paired"]
    assert out["verdicts"]["c_solo"]["fixed"]["vs_size"] is None and out["results"]["c_solo"]["exposure"]["is_size"] is False        # a_size is not read here: no size reading
    run_gf(monkeypatch, root, swept.world, ["--dry-run", "--per-group", "1"])        # at most one of EACH type per group
    g = selection(root)["groups"]
    assert all(len(g[p][t]["kept"]) <= 1 for p in g for t in ("standalone", "modification"))
    assert g["d_"]["standalone"]["kept"] and g["d_"]["modification"]["kept"] and len(g["d_"]["modification"]["unexamined"]) >= 1


def test_a_selection_that_changed_since_the_dry_run_is_flagged(monkeypatch, root, swept, capsys):
    w = swept.world
    run_gf(monkeypatch, root, w, ["--dry-run", "--per-group", "1"])
    capsys.readouterr()
    run_gf(monkeypatch, root, w, ["--per-group", "3"])
    assert "from an earlier dry run" in capsys.readouterr().out
