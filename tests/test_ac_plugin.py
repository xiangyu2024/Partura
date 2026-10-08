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
from alphacube.plugins import SearchHooks, load_plugins, search_hooks_from  # noqa: E402
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
    # 244 of AlphaCube's own + Partura's kernels (every nd one twice, as X and nt_X).  It was 304 with 45 kernels
    # (15 of them nd); main has since added the four nd kernels cs_last_{high,low}{10,05}: 4 + 4 more entries = 312
    assert len(reg) == 312
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
@pytest.fixture
def in_sustain_fix():
    """The opt-in ``in_sustain`` fix on for one test -- and its two process-wide traces (the names added to
    ``catalog.REAL_VALUED_OVERRIDES``, and the registry built with them) taken out again afterwards, so no later
    test sees a vocabulary of 289 where ``main``'s route has 286."""
    ac_plugin.set_fixes(["in_sustain"])
    try:
        yield
    finally:
        ac_plugin.set_fixes(None)
        catalog.REAL_VALUED_OVERRIDES.difference_update(ac_plugin._AC_REAL_VALUED)
        catalog._DEFAULT = None


def test_load_plugins_registers_partura_and_declares_in_sustain_real_valued(in_sustain_fix):
    # (with the opt-in fix on: by default the declaration is NOT made, see the next test)
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


def test_load_plugins_by_default_leaves_the_in_sustain_kernels_flagged_as_main_had_them():
    """``main``'s monkeypatching route only ever cleared Partura's own kernels' flags.  Declaring AlphaCube's
    ``in_sustain_mean`` / ``_stddev`` / ``_product`` real-valued is correct for them but enlarges the search
    vocabulary by 3 (286 -> 289 with resource-risk operators allowed), so every ``dt``-face pick maps the same random
    number to a different operator: not the same experiment as any stored episode.  It is the ``in_sustain`` fix."""
    assert not (set(ac_plugin._AC_REAL_VALUED) & catalog.REAL_VALUED_OVERRIDES)
    catalog._DEFAULT = None
    assert load_plugins(["partura.ac_plugin"]) == ["partura.ac_plugin"]
    assert "partura" in scorer_kinds()
    reg = default_registry()
    searchable = {s.name for s in reg.searchable(include_boolean=False, include_resource_risk=True)}
    for name in ac_plugin._AC_REAL_VALUED:
        sp = reg.get(name)
        assert (sp.boolean_output or sp.trivial_boolean) and name not in searchable
    assert not (set(ac_plugin._AC_REAL_VALUED) & catalog.REAL_VALUED_OVERRIDES)


def test_default_vocabulary_is_alphacubes_own_plus_partura_s_kernels_unflagged():
    """What ``main``'s route builds: AlphaCube's registry untouched, plus every Partura kernel (and nt_ twin)
    searchable.  Pinned structurally: take Partura's names out of the build and what is left must be what the
    plugin route searches, name for name and in the same order (the order is part of the draw)."""
    catalog._DEFAULT = None
    load_plugins(["partura.ac_plugin"])
    theirs = {n for n in ac_plugin.partura_operator_names()}
    with_partura = default_registry()
    got = [s.name for s in with_partura.searchable(include_boolean=False, include_resource_risk=True)]
    for n in ops_ext.NEW_OPERATORS:                         # every kernel is in; an nd one also as nt_<name>
        assert n in with_partura._ops, n
    for n in theirs:                                        # (a dt-face kernel has no nt_ twin: nothing to find)
        sp = with_partura._ops.get(n)
        if sp is not None:
            assert not (sp.boolean_output or sp.trivial_boolean), n
            assert n in got, n
    excluded = catalog.EXCLUDED_KERNELS
    catalog.EXCLUDED_KERNELS = {**excluded, **{n: "left out for this test" for n in ops_ext.NEW_OPERATORS}}
    try:
        alone = [s.name for s in build_registry().searchable(include_boolean=False, include_resource_risk=True)]
    finally:
        catalog.EXCLUDED_KERNELS = excluded
        catalog._DEFAULT = None
    assert [n for n in got if n not in theirs] == alone


def test_register_is_safe_to_call_more_than_once_in_one_process():
    ac_plugin.register()
    ac_plugin.register()
    assert SCORER_FACTORIES["partura"] is ac_plugin._partura_scorer_factory


@pytest.fixture
def no_plugin_hooks():
    """Leave ``ac_plugin``'s hook state exactly as it was found: it is module
    state, and a test that sets it must not leak an opinion into the next one."""
    before = ac_plugin._hooks
    ac_plugin.set_search_hooks(None)
    try:
        yield
    finally:
        ac_plugin.set_search_hooks(before)


def test_search_hooks_is_empty_until_a_caller_sets_one(no_plugin_hooks):
    """REGRESSION (WP11 review, defect 1): ``search_hooks()`` used to return a
    hardcoded opinion -- an ``op_weight`` zeroing every resource-risk operator
    outside ``ops_ext`` -- so ``--plugin partura.ac_plugin`` steered every
    AlphaCube run with no way to turn it off.  The design asks for "a
    SearchHooks built from module state the caller sets" (step 3); with nothing
    set that is the EMPTY bundle."""
    ac_plugin.register()
    h = ac_plugin.search_hooks()
    assert isinstance(h, SearchHooks)
    assert h == SearchHooks()
    assert (h.op_weight, h.accept, h.daily_fields, h.daily_leaf_prob, h.leaf_slots) == (None, None, (), 0.0, {})
    # ... and that is what the CLI's --plugin / $ALPHACUBE_PLUGINS route reads
    assert search_hooks_from(["partura.ac_plugin"]) == SearchHooks()


def test_loading_the_plugin_does_not_cancel_allow_resource_risk(no_plugin_hooks):
    """REGRESSION (WP11 review, defect 1a): measured against the live registry,
    the old hardcoded ``op_weight`` forced exactly these four of the 281 specs
    ``--allow-resource-risk`` makes searchable to weight 0 -- silently undoing
    the flag the caller passed, with no opt-out."""
    catalog._DEFAULT = None
    load_plugins(["partura.ac_plugin"])
    reg = default_registry()
    searchable = {s.name for s in reg.searchable(include_boolean=False, include_resource_risk=True)}
    cancelled = ("in_mask_nearby_ones", "nt_ts_pearson", "nt_ts_spearman", "pow")
    assert set(cancelled) <= searchable
    hooks = search_hooks_from(["partura.ac_plugin"])
    assert hooks.op_weight is None            # nothing left that could re-zero them


def test_loading_the_plugin_leaves_the_generator_byte_identical(no_plugin_hooks):
    """REGRESSION (WP11 review, defect 1b): with the CLI default
    ``allow_resource_risk=False`` the old hook changed NO weight (all 277 specs
    1.0) yet still diverged the population at index 0, because
    ``op_weight is not None`` routes ``_pick`` into ``_pick_weighted``
    (``random.choices`` instead of ``random.choice``).  So ``alphacube mine
    --plugin partura.ac_plugin --seed 7``, run only for Partura's operators,
    was not comparable to the same command without ``--plugin``.  The hooks are
    fed in exactly as ``mining/gp.py`` feeds them."""
    catalog._DEFAULT = None
    load_plugins(["partura.ac_plugin"])
    reg = default_registry()
    hooks = search_hooks_from(["partura.ac_plugin"])
    for rr in (False, True):
        plain = TypedTreeGenerator(reg, seed=7, allow_resource_risk=rr)
        hooked = TypedTreeGenerator(reg, seed=7, allow_resource_risk=rr, op_weight=hooks.op_weight,
                                    accept=hooks.accept, daily_fields=hooks.daily_fields,
                                    daily_leaf_prob=hooks.daily_leaf_prob, leaf_slots=hooks.leaf_slots)
        assert [e.key() for e in hooked.generate_population(30)] == \
               [e.key() for e in plain.generate_population(30)]


def test_set_search_hooks_round_trips_and_clearing_restores_the_empty_bundle(no_plugin_hooks):
    """The opt-out the old hardcoded opinion had none of: an opinion exists
    only while a caller has set one, and ``None`` puts it back."""
    mine = SearchHooks(op_weight=lambda s: 1.0, daily_leaf_prob=0.25)
    ac_plugin.set_search_hooks(mine)
    assert ac_plugin.search_hooks() is mine
    assert search_hooks_from(["partura.ac_plugin"]) is mine
    ac_plugin.set_search_hooks(None)
    assert ac_plugin.search_hooks() == SearchHooks()
    with pytest.raises(TypeError):
        ac_plugin.set_search_hooks({"op_weight": None})          # not a SearchHooks


def test_partura_operator_names_covers_ops_ext_and_its_nt_twins():
    names = ac_plugin.partura_operator_names()
    assert set(ops_ext.NEW_OPERATORS) <= names
    assert {"nt_" + n for n in ops_ext.NEW_OPERATORS} <= names
    assert len(names) == 2 * len(set(ops_ext.NEW_OPERATORS))


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
    again = scorer.score(panel, gated=False)
    # (a level reward leaves the paired columns -- p_share, p_ir_*, p_dann_* -- NaN, and NaN != NaN)
    assert out_combined.keys() == again.keys()
    assert all(out_combined[k] == again[k] or (out_combined[k] != out_combined[k] and again[k] != again[k]) for k in again)
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
BOOST = 8.0
IDEA_OP, PENALISED_OP = "day_mean", "day_max"


def _arm_pair(accept=None):
    """``scripts/idea_search.py``'s own two arms, built the way the script
    builds them: ONE keyword set, the arm name the only thing that varies."""
    reg = default_registry()
    kw = dict(risky={s.name for s in reg.list_all() if s.resource_risk},
              ext=ac_plugin.partura_operator_names(), opw={PENALISED_OP: 0.25},
              idea_ops={IDEA_OP}, boost=BOOST, accept=accept)
    return reg, ac_plugin.arm_hooks("control", **kw), ac_plugin.arm_hooks("steer", **kw)


def test_arm_hooks_gives_the_boost_and_the_guidance_to_the_steer_arm_only():
    """REGRESSION (WP11 review, defect 2): nothing pinned WHICH arm got the
    guidance and the idea boost -- swapping them in ``scripts/idea_search.py``
    left the whole file green, because the old test built two hand-made hooks
    with identical ``op_weight`` and then asserted a fact about the generator.
    The arm construction is now ``ac_plugin.arm_hooks``, asserted on directly."""
    def guidance(tree):
        return True

    reg, control, steer = _arm_pair(accept=guidance)
    # the guidance is the steer arm's, and only the steer arm's
    assert control.accept is None and steer.accept is guidance
    # the idea's operator is boosted in the steer arm and untouched in the control arm
    idea_spec = reg.get(IDEA_OP)
    assert control.op_weight(idea_spec) == 1.0
    assert steer.op_weight(idea_spec) == BOOST
    # the guidance's own per-operator weight likewise reaches only the steer arm
    pen_spec = reg.get(PENALISED_OP)
    assert control.op_weight(pen_spec) == 1.0
    assert steer.op_weight(pen_spec) == 0.25
    # ... while the base library filter is identical in both: AlphaCube's own resource-risk
    # operators out, Partura's ops_ext kernels in, everything else 1.0
    ext = ac_plugin.partura_operator_names()
    risky_not_ext = [s for s in reg.list_all() if s.resource_risk and s.name not in ext]
    assert risky_not_ext
    for s in risky_not_ext:
        assert control.op_weight(s) == steer.op_weight(s) == 0.0
    for s in [s for s in reg.list_all() if s.resource_risk and s.name in ext]:
        assert control.op_weight(s) == steer.op_weight(s) == 1.0
    # and the arms differ in NOTHING else (the design's "differ in exactly the op_weight/accept fields")
    assert (control.daily_fields, control.daily_leaf_prob, control.leaf_slots) == \
           (steer.daily_fields, steer.daily_leaf_prob, steer.leaf_slots) == ((), 0.0, {})


def test_arm_hooks_control_ignores_the_boost_the_weights_and_the_accept_hook():
    """One call site passes the same keywords for both arms, so "control gets
    none of it" has to be ``arm_hooks``'s own doing, not the caller's."""
    reg, control, _ = _arm_pair(accept=lambda tree: False)
    plain = ac_plugin.arm_hooks("control", risky=set(), ext=set())
    for name in (IDEA_OP, PENALISED_OP, "cs_rank"):
        assert control.op_weight(reg.get(name)) == plain.op_weight(reg.get(name)) == 1.0
    assert control.accept is None


def test_arm_hooks_rejects_an_unknown_arm_and_a_bad_boost():
    assert ac_plugin.ARMS == ("control", "steer")
    with pytest.raises(ValueError):
        ac_plugin.arm_hooks("steerr")
    with pytest.raises(ValueError):
        ac_plugin.arm_hooks("steer", boost=float("inf"))
    with pytest.raises(ValueError):
        ac_plugin.arm_hooks("steer", boost=-1.0)


def test_a_generator_built_from_each_arm_draws_the_idea_operator_as_expected():
    """The design's test bullet, actually exercised: "a generator built from
    each yields the expected populations".  The boost is a sampling claim, so
    it is checked by sampling -- not by comparing two hooks that happened to
    share an ``op_weight``."""
    reg, control, steer = _arm_pair()
    gens = {}
    for arm, hooks in (("control", control), ("steer", steer)):
        gens[arm] = TypedTreeGenerator(reg, seed=23, allow_resource_risk=True, min_depth=2, max_depth=2,
                                       op_weight=hooks.op_weight, accept=hooks.accept)
    n = {arm: sum(repr(e).count(IDEA_OP) for e in g.generate_population(300)) for arm, g in gens.items()}
    assert n["steer"] > n["control"], n
    # the penalised operator goes the other way, and neither arm can draw a non-Partura
    # resource-risk operator at all (weight 0 in both)
    ext = ac_plugin.partura_operator_names()
    banned = {s.name for s in reg.list_all() if s.resource_risk and s.name not in ext}
    for arm, g in gens.items():
        drawn = set()
        for e in TypedTreeGenerator(reg, seed=29, allow_resource_risk=True, min_depth=2, max_depth=2,
                                    op_weight=gens[arm].op_weight).generate_population(300):
            drawn.update(re.findall(r"[A-Za-z_][A-Za-z_0-9]*(?=\()", repr(e)))
        assert not (drawn & banned), (arm, sorted(drawn & banned))


def test_arm_hooks_matches_opw_and_idea_ops_on_the_nt_twin_too():
    """REGRESSION (branch verification): ``opw`` keys come from ``Guidance
    .operator_weights()`` (the heads of hand-written rule patterns) and
    ``idea_ops`` from scraping the idea's expression text, so both are written in
    ND-face spelling -- while every nd-face kernel is registered TWICE, as ``X``
    and as ``nt_X``.  Matching ``spec.name`` alone steered half the kernel and
    left the other half fully live: measured on AlphaCube over 400 seeds x
    ``generate_population(25)``, zeroing one nd-face name took its ND-face draws
    148 -> 0 and left the twin's at 17 -> 17.  ``ext`` already expanded the twins
    itself (``partura_operator_names``); these two did not.  ``cs_mean`` /
    ``cs_rank`` stand in for the real guidance's nd-face kernels."""
    reg = default_registry()
    nd, idea_nd = "cs_mean", "cs_rank"
    assert {f"nt_{nd}", f"nt_{idea_nd}"} <= {s.name for s in reg.list_all()}, "both twins must exist"

    kw = dict(risky=set(), ext=set(), opw={nd: 0.0}, idea_ops={idea_nd}, boost=BOOST, nt_twins=True)   # the opt-in fix
    steer = ac_plugin.arm_hooks("steer", **kw)
    assert steer.op_weight(reg.get(nd)) == 0.0
    assert steer.op_weight(reg.get(f"nt_{nd}")) == 0.0          # was 1.0: half-steered
    assert steer.op_weight(reg.get(idea_nd)) == BOOST
    assert steer.op_weight(reg.get(f"nt_{idea_nd}")) == BOOST   # was 1.0: half-boosted

    # An explicit nt_ entry still wins, so the two faces can be weighted apart on purpose.
    split = ac_plugin.arm_hooks("steer", risky=set(), ext=set(), opw={nd: 0.0, f"nt_{nd}": 2.0}, nt_twins=True)
    assert split.op_weight(reg.get(nd)) == 0.0
    assert split.op_weight(reg.get(f"nt_{nd}")) == 2.0
    # The control arm is still the base filter alone -- the twin rule must not leak into it.
    control = ac_plugin.arm_hooks("control", **kw)
    for name in (nd, f"nt_{nd}", idea_nd, f"nt_{idea_nd}"):
        assert control.op_weight(reg.get(name)) == 1.0
    # A dt-face operator has no twin at all, and is untouched by either key.
    assert steer.op_weight(reg.get("day_mean")) == 1.0


def test_arm_hooks_by_default_matches_opw_and_idea_ops_by_name_only_like_mains_pick():
    """The default is ``main``'s: its ``pick`` looked ``opw`` and the idea's operators up by ``spec.name``, so an
    ND-face operator's ``nt_`` twin kept weight 1.0.  (The branch's fix for that half is the ``nt_twins`` opt-in,
    tested above: it changes which operators the steer arm draws.)"""
    reg = default_registry()
    nd, idea_nd = "cs_mean", "cs_rank"
    steer = ac_plugin.arm_hooks("steer", risky=set(), ext=set(), opw={nd: 0.0}, idea_ops={idea_nd}, boost=BOOST)
    assert steer.op_weight(reg.get(nd)) == 0.0 and steer.op_weight(reg.get(idea_nd)) == BOOST
    assert steer.op_weight(reg.get(f"nt_{nd}")) == 1.0
    assert steer.op_weight(reg.get(f"nt_{idea_nd}")) == 1.0


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
    assert "hooks=ac_plugin.search_hooks()" in src


def test_idea_search_builds_each_arms_hooks_from_that_arms_own_name():
    """REGRESSION (WP11 review, defect 2): the arm -> hooks assignment used to
    be a literal table in the script, which the suite only grepped for
    (``'HOOKS = {"control":' in src or "HOOKS[arm]" in src`` -- satisfied by the
    second branch alone), so swapping the two arms' hooks left every test
    green.  There is no table any more: the script must build the running arm's
    hooks from the loop variable itself, through the one tested helper, so
    there is nothing left to swap.  (What the hooks then ARE is asserted on
    ``ac_plugin.arm_hooks`` directly, above -- not grepped.)"""
    import ast
    src = (PARTURA_ROOT / "scripts" / "idea_search.py").read_text(encoding="utf-8")
    tree = ast.parse(src, filename="idea_search.py")
    calls = [n for n in ast.walk(tree)
             if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
             and n.func.attr == "arm_hooks"]
    assert len(calls) == 1, f"expected exactly one ac_plugin.arm_hooks(...) call, found {len(calls)}"
    call = calls[0]
    assert isinstance(call.func.value, ast.Name) and call.func.value.id == "ac_plugin"
    # the arm is passed, not named: arm_hooks(arm, ...) with arm the loop variable, never a literal
    assert len(call.args) == 1 and isinstance(call.args[0], ast.Name) and call.args[0].id == "arm"
    loops = [n for n in ast.walk(tree)
             if isinstance(n, ast.For) and isinstance(n.target, ast.Name) and n.target.id == "arm"
             and any(c is call for c in ast.walk(n))]
    assert loops, "the arm_hooks(arm, ...) call must sit inside the `for arm in ARMS:` loop"
    # and no local copy of the weight formula may come back alongside it
    assert "def base_weight(" not in src and "def weighted(" not in src
