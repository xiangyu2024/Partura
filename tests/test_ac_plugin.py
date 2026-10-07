"""WP11: partura.ac_plugin (plugin module), ops_ext without the build_registry
monkeypatch, scripts/idea_search.py without rebinding TypedTreeGenerator, and
partura.panels.PanelSet.view_id's daily-fields cache-identity fix.

    ALPHACUBE_ROOT=~/Desktop/AlphaCube-steering PYTHONPATH=~/Desktop/AlphaCube-steering/src:. \
        python -m pytest tests/test_ac_plugin.py -q
"""
import re
import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from partura import ac_plugin, ops_ext
from partura.bridge import ensure_alphacube_on_path
from partura.steer import RewardContext

ensure_alphacube_on_path()

import alphacube.catalog as catalog  # noqa: E402
from alphacube.catalog import build_registry, default_registry  # noqa: E402
from alphacube.mining.generator import TypedTreeGenerator  # noqa: E402
from alphacube.mining.scoring import SCORER_FACTORIES, scorer_kinds  # noqa: E402
from alphacube.plugins import SearchHooks, load_plugins  # noqa: E402
from alphacube.store import CubeStore  # noqa: E402
from alphacube.synthetic import write_daily_fields, write_synthetic_store  # noqa: E402

PARTURA_ROOT = Path(__file__).resolve().parents[1]

NINE_MISFLAGGED = ("day_flat_ratio", "day_zero_ratio", "day_flat_run_max", "day_at_max_ratio",
                   "day_at_min_ratio", "day_distinct_ratio", "cross_flat_ratio", "cs_bucket_demean",
                   "cs_bucket_zscore")


# ---------------------------------------------------------------- ops_ext: no more build_registry patch
def test_unpatched_build_registry_flags_none_of_the_nine_kernels():
    """``ops_ext`` is imported (module scope, above) but ``install_kernels`` /
    ``ac_plugin.register`` are NOT called here -- this is the literal
    'unpatched alphacube.catalog.build_registry' the design's test plan asks
    for. Before WP11 this flagged 11 registry entries (9 base names + the two
    nt_ twins of cs_bucket_demean / cs_bucket_zscore); real_valued=True at the
    nine kernels' own @op(...) now does it without any build_registry patch,
    and none exists any more to patch (``build_registry`` is a plain function
    object, not wrapped)."""
    assert not hasattr(catalog.build_registry, "_partura")
    reg = build_registry()
    assert len(reg) == 304
    flagged = [n for name in NINE_MISFLAGGED for n in (name, "nt_" + name)
              if (sp := reg._ops.get(n)) is not None and (sp.boolean_output or sp.trivial_boolean)]
    assert flagged == []


def test_real_valued_is_set_at_the_nine_kernels_definition_site_not_by_override():
    """The nine kernels are real-valued because of their own ``@op(real_valued=True)``,
    not because ``catalog.REAL_VALUED_OVERRIDES`` happens to name them (that
    channel is for AlphaCube's OWN ``in_sustain_*`` -- see :func:`ac_plugin.register`)."""
    reg = build_registry()
    for name in NINE_MISFLAGGED:
        sp = reg.get(name)
        assert sp.boolean_output is False and sp.trivial_boolean is False
        assert name not in catalog.REAL_VALUED_OVERRIDES


def test_install_kernels_populates_the_legacy_tables_and_is_idempotent():
    import alphacube.operators as ops
    ops_ext.install_kernels()
    ops_ext.install_kernels()          # must not raise the second time
    for name in ops_ext.NEW_OPERATORS:
        assert (name in ops.operator_dict_DT) or (name in ops.operator_dict_ND)


# ---------------------------------------------------------------- load_plugins / register
def test_load_plugins_registers_partura_and_declares_in_sustain_real_valued():
    catalog._DEFAULT = None
    loaded = load_plugins(["partura.ac_plugin"])
    assert loaded == ["partura.ac_plugin"]
    assert "partura" in scorer_kinds()
    assert SCORER_FACTORIES["partura"] is ac_plugin._partura_scorer_factory
    reg = default_registry()
    for name in ("in_sustain_mean", "in_sustain_stddev", "in_sustain_product"):
        sp = reg.get(name)
        assert sp.boolean_output is False and sp.trivial_boolean is False
    # in_sustain itself is genuinely boolean (a 0/1 propagation mask) and must stay flagged
    assert reg.get("in_sustain").boolean_output or reg.get("in_sustain").trivial_boolean


def test_register_is_safe_to_call_more_than_once_in_one_process():
    ac_plugin.register()
    ac_plugin.register()
    assert SCORER_FACTORIES["partura"] is ac_plugin._partura_scorer_factory


def test_search_hooks_has_no_opinion_without_configuration_beyond_op_weight():
    ac_plugin.register()
    h = ac_plugin.search_hooks()
    assert isinstance(h, SearchHooks)
    assert h.accept is None and h.daily_fields == () and h.daily_leaf_prob == 0.0 and h.leaf_slots == {}
    reg = default_registry()
    ext = set(ops_ext.NEW_OPERATORS) | {"nt_" + n for n in ops_ext.NEW_OPERATORS}
    risky_not_ext = [s for s in reg.list_all() if s.resource_risk and s.name not in ext]
    if risky_not_ext:
        assert h.op_weight(risky_not_ext[0]) == 0.0
    risky_ext = [s for s in reg.list_all() if s.resource_risk and s.name in ext]
    for s in risky_ext:
        assert h.op_weight(s) == 1.0


# ---------------------------------------------------------------- ParturaScorer / _partura_scorer_factory
def _toy_ctx(n_days=40, n_sym=12, seed=0):
    rng = np.random.default_rng(seed)
    tgt = rng.normal(size=(n_days, n_sym))
    base = rng.normal(size=(n_days, n_sym))
    liq = rng.normal(size=(n_days, n_sym))
    pool = rng.normal(size=(n_days, n_sym))
    cut = n_days // 2
    return RewardContext(tgt, slice(0, cut), slice(cut, n_days), untradable=None, liq=liq, pool=pool,
                         base=base, halflives=(0.0, 5)), cut


def test_scorer_factory_requires_dates_and_a_valid_warmup():
    ctx, cut = _toy_ctx()
    ac_plugin.set_scorer_state(ctx, "long", "20200101")
    with pytest.raises(ValueError):
        ac_plugin._partura_scorer_factory(ctx.tgt, dates=None)
    dates = [f"2020{(i % 12) + 1:02d}{(i % 27) + 1:02d}" for i in range(ctx.tgt.shape[0])]
    with pytest.raises(ValueError):
        ac_plugin._partura_scorer_factory(ctx.tgt, dates=dates, warmup=len(dates))      # == len(dates): out of range
    with pytest.raises(ValueError):
        ac_plugin._partura_scorer_factory(ctx.tgt, dates=dates, warmup=-1)


def test_scorer_factory_rejects_a_misshapen_target():
    ctx, _ = _toy_ctx()
    ac_plugin.set_scorer_state(ctx, "long", "20200101")
    dates = [f"2020{(i % 12) + 1:02d}{(i % 27) + 1:02d}" for i in range(ctx.tgt.shape[0] + 5)]
    with pytest.raises(RuntimeError):
        # 5 extra leading (warm-up) rows claimed, but target itself was never widened to match
        ac_plugin._partura_scorer_factory(ctx.tgt, dates=dates, warmup=5)


def test_scorer_factory_warmup_zero_reproduces_the_scripts_own_cut():
    """``scripts/idea_search.py``'s one caller always has warmup == 0 (its
    START is the store's first date, so its view's lead-in is empty) -- the
    case this pins is that the factory's own split then lands on exactly the
    cut idea_search.py used to compute itself from a closed-over ``cut``."""
    ctx, cut = _toy_ctx(n_days=50, seed=2)
    split_date = "20200615"
    dates = sorted({f"2020{(i % 12) + 1:02d}{(i % 27) + 1:02d}" for i in range(200)})[:ctx.tgt.shape[0]]
    want_cut = int(np.searchsorted(np.asarray(dates), split_date))
    ac_plugin.set_scorer_state(ctx, "long", split_date)
    n0 = len(ac_plugin.SCORERS)
    scorer = ac_plugin._partura_scorer_factory(ctx.tgt, dates=dates, warmup=0, min_coverage=0.0,
                                               min_scored_days=0.0)
    assert scorer._cut == want_cut
    assert len(ac_plugin.SCORERS) == n0 + 1 and ac_plugin.SCORERS[-1] is scorer


def test_score_combined_matches_score_ungated_and_tracks_n_and_gate():
    ctx, _ = _toy_ctx(n_days=60, n_sym=20, seed=4)
    dates = [f"d{i:04d}" for i in range(ctx.tgt.shape[0])]
    ac_plugin.set_scorer_state(ctx, "long", dates[30])
    scorer = ac_plugin._partura_scorer_factory(ctx.tgt, dates=dates, warmup=0, min_coverage=0.0,
                                               min_scored_days=0.0)
    panel = 0.3 * ctx.tgt + np.random.default_rng(5).normal(size=ctx.tgt.shape)
    out_gated = scorer.score(panel, gated=True)
    out_combined = scorer.score_combined(panel)
    assert out_combined == scorer.score(panel, gated=False)
    assert scorer.n == 3
    assert set(ac_plugin.ParturaScorer.columns) <= set(out_gated)


def test_scorer_needs_set_scorer_state_first():
    ac_plugin._ctx, ac_plugin._kind, ac_plugin._split = None, None, None
    try:
        with pytest.raises(RuntimeError):
            ac_plugin._partura_scorer_factory(np.zeros((10, 3)), dates=[str(i) for i in range(10)], warmup=0)
    finally:
        ctx, _ = _toy_ctx()
        ac_plugin.set_scorer_state(ctx, "long", "20200101")      # leave state sane for later tests


# ---------------------------------------------------------------- SearchHooks + a real generator
def test_search_hooks_for_control_and_steer_differ_only_in_op_weight_and_accept():
    control = SearchHooks(op_weight=lambda s: 1.0)
    calls = []

    def steer_accept(tree):
        calls.append(tree)
        return True

    steer = SearchHooks(op_weight=lambda s: 1.0, accept=steer_accept)
    assert control.accept is None and steer.accept is steer_accept
    assert control.op_weight is not steer.op_weight
    assert (control.daily_fields, control.daily_leaf_prob, control.leaf_slots) == \
           (steer.daily_fields, steer.daily_leaf_prob, steer.leaf_slots) == ((), 0.0, {})

    reg = default_registry()
    gen_c = TypedTreeGenerator(reg, seed=11, op_weight=control.op_weight, accept=control.accept)
    gen_s = TypedTreeGenerator(reg, seed=11, op_weight=steer.op_weight, accept=steer.accept)
    pop_c = [e.key() for e in gen_c.generate_population(50)]
    pop_s = [e.key() for e in gen_s.generate_population(50)]
    # the same (uniform) op_weight -> the same population; an always-True accept adds a call, not a change
    assert pop_c == pop_s
    assert len(calls) >= 50


def test_op_weight_hook_removes_an_entire_face_from_generation():
    reg = default_registry()

    def no_shared(s):
        return 0.0 if s.face == "shared" else 1.0

    gen = TypedTreeGenerator(reg, seed=13, op_weight=no_shared, min_depth=2, max_depth=2)
    pop = gen.generate_population(150)
    shared_names = {s.name for s in reg.list_all() if s.face == "shared"}
    used = set()
    for e in pop:
        used.update(re.findall(r"[A-Za-z_][A-Za-z_0-9]*(?=\()", repr(e)))
    assert not (used & shared_names)


def test_a_boosted_operator_is_drawn_more_often_than_under_uniform_weight():
    reg = default_registry()
    boosted = "day_mean"
    assert boosted in {s.name for s in reg.list_all()}

    def boost(s):
        return 50.0 if s.name == boosted else 1.0

    gen_u = TypedTreeGenerator(reg, seed=17, op_weight=lambda s: 1.0, min_depth=2, max_depth=2)
    gen_b = TypedTreeGenerator(reg, seed=17, op_weight=boost, min_depth=2, max_depth=2)
    n_u = sum(repr(e).count(boosted) for e in gen_u.generate_population(300))
    n_b = sum(repr(e).count(boosted) for e in gen_b.generate_population(300))
    assert n_b > n_u


# ---------------------------------------------------------------- PanelSet.view_id / cache identity
def _tiny_store(tmp_path):
    return write_synthetic_store(tmp_path / "cube", n_symbols=6, n_days=20, n_minutes=4, seed=3)


def test_view_id_changes_when_the_daily_fields_directory_changes_and_is_stable_otherwise(tmp_path, monkeypatch):
    from partura.panels import PanelSet
    monkeypatch.delenv("ALPHACUBE_DAILY_FIELDS", raising=False)
    store = _tiny_store(tmp_path)
    start, end = store.dates[0], store.dates[-1]

    def pset():
        return PanelSet(str(store.directory), start, end, warmup=0, device="cpu")

    id_none_1 = pset().view_id
    id_none_2 = pset().view_id
    assert id_none_1 == id_none_2            # stable: same inputs, same hash, twice, two fresh instances

    one = np.ones((store.n_symbols, store.n_days))
    root_a = write_daily_fields(tmp_path / "daily_a", {"FloatCap": one}, store.symbols, store.dates)
    monkeypatch.setenv("ALPHACUBE_DAILY_FIELDS", str(root_a))
    id_a_1 = pset().view_id
    id_a_2 = pset().view_id
    assert id_a_1 == id_a_2
    assert id_a_1 != id_none_1               # attaching a daily store at all must move the id

    # a later rebuild that changes the daily store's OWN identity (here: one more field) -- not just
    # the symbols/dates/store path PanelSet.view_id already hashed -- must move the id again
    root_b = write_daily_fields(tmp_path / "daily_b", {"FloatCap": one, "TotalCap": one},
                                store.symbols, store.dates)
    monkeypatch.setenv("ALPHACUBE_DAILY_FIELDS", str(root_b))
    id_b = pset().view_id
    assert id_b != id_a_1 and id_b != id_none_1

    monkeypatch.delenv("ALPHACUBE_DAILY_FIELDS", raising=False)
    assert pset().view_id == id_none_1       # removing it again returns to exactly the old identity


def test_view_id_matches_contract_hash_byte_identical_claim_with_no_daily_source(tmp_path, monkeypatch):
    """Backward compatibility item 7: a store with no daily source attached
    builds the same contract_hash it always did, so view_id's new term is a
    no-op for every cache entry written before WP11."""
    from partura.panels import PanelSet
    monkeypatch.delenv("ALPHACUBE_DAILY_FIELDS", raising=False)
    store = _tiny_store(tmp_path)
    plain = CubeStore(store.directory)
    assert plain.contract_hash == store.contract_hash
    ps = PanelSet(str(store.directory), store.dates[0], store.dates[-1], warmup=0, device="cpu")
    assert ps.store.contract_hash == store.contract_hash


# ---------------------------------------------------------------- no monkeypatching left anywhere
def test_no_monkeypatch_remnants_anywhere_in_the_partura_tree():
    # Built from fragments so this assertion does not match its OWN source line -- this file is
    # part of the tree the loop below walks.
    needles = ("asc" + ".make_scorer", "agp" + ".make_scorer", "T" + "._pick", "T" + ".acceptable",
              "FITNESS_" + "KINDS", "dataclasses" + ".replace")
    this_file = Path(__file__).resolve()
    hits = []
    for path in sorted(PARTURA_ROOT.rglob("*.py")):
        if "/.git/" in str(path) or path.resolve() == this_file:
            continue
        text = path.read_text(encoding="utf-8")
        for needle in needles:
            if needle in text:
                hits.append(f"{path.relative_to(PARTURA_ROOT)}: {needle}")
    assert hits == []


def test_idea_search_script_loads_the_plugin_and_builds_plain_search_hooks():
    """scripts/idea_search.py is a script (reads sys.argv at import time), so it
    cannot be imported or run end-to-end here (and its GP runs need a GPU and a
    real store).  This pins the structural shape the rewrite must keep: it is
    syntactically valid, it loads the plugin before building anything that
    would touch default_registry(), it hands the generator plain SearchHooks
    rather than rebinding TypedTreeGenerator, and it never reads self._rng for
    the guidance draw."""
    import ast
    src = (PARTURA_ROOT / "scripts" / "idea_search.py").read_text(encoding="utf-8")
    tree = ast.parse(src, filename="idea_search.py")
    assert any(isinstance(n, ast.ImportFrom) and n.module == "alphacube.plugins"
              and any(a.name == "load_plugins" for a in n.names) for n in ast.walk(tree))
    assert "ac_plugin.set_scorer_state(" in src
    assert "ac_plugin.SCORERS" in src
    assert "hook_rng.random()" in src
    assert "self._rng.random()" not in src
    assert "SearchHooks(op_weight=" in src
    assert 'HOOKS = {"control":' in src or "HOOKS[arm]" in src
