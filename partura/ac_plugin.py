"""The AlphaCube plugin AlphaCube loads back: ``--plugin partura.ac_plugin`` /
``alphacube.plugins.load_plugins(["partura.ac_plugin"])``.

AlphaCube never imports Partura on its own -- a caller always names this module
itself.  Importing it is what used to require ``ops_ext.install()``'s
``catalog.build_registry`` monkeypatch and a bespoke ``install(arm)`` that
rebound ``TypedTreeGenerator._pick`` / ``.acceptable`` inside
``scripts/idea_search.py``; both are gone (WP11).  What is left:

* :func:`register` -- called once by ``load_plugins`` before the registry is
  (re)built: wires ``ops_ext``'s legacy-table entries and registers the
  ``"partura"`` fitness kind (see ``alphacube.mining.scoring.register_scorer``).
  With the opt-in fix ``"in_sustain"`` (below) it also declares AlphaCube's own
  three ``in_sustain_*`` kernels real-valued.
* :func:`set_search_hooks` / :func:`search_hooks` -- the steering opinion a
  caller sets as module state and the CLI / ``alphacube.plugins.
  search_hooks_from`` reads back.  **Empty by default**: loading this plugin
  for its operators alone steers nothing.
* :func:`arm_hooks` -- the one place the operator-weight formula
  ``scripts/idea_search.py``'s two arms are built from, so the control arm and
  the steer arm cannot drift apart (nor be swapped) unnoticed.
* :class:`ParturaScorer` / :func:`_partura_scorer_factory` -- the reward
  ``scripts/idea_search.py`` used to define inline, with its ``ctx`` / ``KIND``
  closure replaced by :func:`set_scorer_state` (module state the caller sets
  once, before ``run_mining``) and its train/valid split recomputed from the
  ``dates`` / ``warmup`` the factory itself receives rather than from a
  script-level global.
* :func:`asked_from` -- which generator method an ``accept`` hook is being asked
  for (the one thing the hook signature does not say; see there).

**This route is a re-plumbing of ``main``'s, not a different experiment.**  With
nothing switched on, the vocabulary, the operator weights, the filter and the
reward are those of the monkeypatching ``scripts/idea_search.py`` of ``main``
(``tests/test_plugin_equivalence.py`` and ``tests/test_ac_plugin.py`` pin each of
them, and the real scripts were run side by side on a synthetic store: same
candidates, same order, same scores, same counters).  Two changes the WP11 branch
made on top of that move the draws, so they are OFF unless asked for -- by
``$PARTURA_AC_FIXES=in_sustain,nt_twins`` or :func:`set_fixes`, and a run that
switches one on records it (``evidence["plugin_fixes"]``) because its numbers
are then no longer comparable with the stored episodes:

* ``in_sustain`` -- AlphaCube's ``in_sustain_mean`` / ``_stddev`` / ``_product``
  are declared real-valued, which puts 3 more operators into the search
  vocabulary (286 -> 289 with resource-risk operators allowed).  Every pick from
  the ``dt`` face then maps the same random number to a different operator.
* ``nt_twins`` -- the guidance's per-operator weights and the idea boost also
  reach an ND-face operator's ``nt_`` twin, which ``main``'s ``pick`` never did.

One difference is AlphaCube's and cannot be switched off from here: when
``TypedTreeGenerator.generate()`` runs out of its 64 tries, the baseline returned
the minimal tree without asking ``acceptable`` and AlphaCube-steering asks it
(with a hook installed, up to 64 more times).  It takes 64 refusals in a row --
5e-6 per call at the lowest acceptance of any stored steer arm -- and
``tests/test_plugin_equivalence.py`` documents it.

See docs/alphacube_steering_design.md, "丙 Migration" and "### WP11"."""
from __future__ import annotations

import math
import os
import sys
import time
from typing import Callable, Dict, FrozenSet, Iterable, List, Mapping, Optional

import numpy as np

from .bridge import ensure_alphacube_on_path

ensure_alphacube_on_path()

from alphacube.mining import scoring as asc  # noqa: E402
from alphacube.mining.generator import nd_twin_base  # noqa: E402
from alphacube.mining.scoring import register_scorer  # noqa: E402
from alphacube.plugins import SearchHooks, declare_real_valued  # noqa: E402

from . import diagnose as dg  # noqa: E402
from . import ops_ext  # noqa: E402
from .steer import RewardContext, reward as steer_reward  # noqa: E402

# AlphaCube's own three kernels that are genuinely real-valued but live outside
# this plugin's definition site -- see docs/alphacube_steering_design.md's
# must_fix #5 (the measured 218->221 / 214->217 split) and "Backward
# compatibility" item 9 (AlphaCube's own WP1 declares nothing).
_AC_REAL_VALUED = ("in_sustain_mean", "in_sustain_stddev", "in_sustain_product")

# -- the WP11 branch's two changes that move the draws away from ``main``'s
# monkeypatching route; OFF by default (see the module docstring).
KNOWN_FIXES = ("in_sustain", "nt_twins")
_fixes_explicit: Optional[FrozenSet[str]] = None


def _parse_fixes(text: str) -> FrozenSet[str]:
    names = frozenset(x.strip() for x in str(text).replace(";", ",").split(",") if x.strip())
    unknown = sorted(names - set(KNOWN_FIXES))
    if unknown:
        raise ValueError(f"unknown plugin fix(es) {unknown}; choose from {KNOWN_FIXES}")
    return names


def set_fixes(names: Optional[Iterable[str]]) -> None:
    """Switch the opt-in fixes on for this process (``None``: go back to what
    ``$PARTURA_AC_FIXES`` says).  Call it BEFORE ``load_plugins`` -- the
    ``in_sustain`` declaration is made by :func:`register`."""
    global _fixes_explicit
    _fixes_explicit = None if names is None else _parse_fixes(",".join(names))


def fixes() -> FrozenSet[str]:
    """The opt-in fixes in force: :func:`set_fixes` if it was called, else
    ``$PARTURA_AC_FIXES`` (comma separated; empty = none)."""
    if _fixes_explicit is not None:
        return _fixes_explicit
    return _parse_fixes(os.environ.get("PARTURA_AC_FIXES", ""))


# -- module state a caller sets once, before run_mining, in place of the
# ctx/KIND closure scripts/idea_search.py used to build ParturaScorer with
# inline.  Every arm of one run shares the same reward, context and split.
_ctx: Optional[RewardContext] = None
_kind: Optional[str] = None
_split: Optional[str] = None
_known: Optional[np.ndarray] = None      # z-rank of the known family, for p_rho_known (None: ctx.base)

# -- the generator-side steering opinion, likewise module state a caller sets
# (:func:`set_search_hooks`) and :func:`search_hooks` reads back.  ``None`` --
# the default, and what nothing-but-``load_plugins`` leaves it at -- means NO
# opinion: see :func:`search_hooks` for why that has to be the default.
_hooks: Optional[SearchHooks] = None

ARMS = ("control", "steer")

# Every ParturaScorer ever constructed, in construction order -- the caller
# slices this by its own high-water mark (``n0 = len(SCORERS)`` before an
# arm's run) to read back .n / .gate / .seconds for just that arm; nothing
# here ever clears it.
SCORERS: List["ParturaScorer"] = []


def set_scorer_state(ctx: RewardContext, kind: str, split: str, known: Optional[np.ndarray] = None) -> None:
    """Tell :func:`_partura_scorer_factory` what reward context, reward kind
    and train/valid split date to score with.  ``ctx`` must be built over the
    SAME view GPMiner itself mines on (its ``tgt`` / ``untradable`` / ``liq`` /
    ``pool`` / ``base`` planes are taken as already correctly trimmed of
    whatever lead-in warm-up rows that view carries -- see
    :func:`_partura_scorer_factory`).  Call this once per run, before
    ``run_mining``; it is the same for every arm of one run.

    ``known`` is the z-rank plane of the known family that ``p_rho_known`` (the
    rank correlation recorded for every candidate) is measured against.  It is
    NOT always ``ctx.base``: with ``--screen-base pool`` the context's base is
    the pool's strongest member while ``p_rho_known`` has always been taken
    against the unscreened known family.  ``None`` keeps the earlier behaviour
    (``ctx.base``)."""
    global _ctx, _kind, _split, _known
    _ctx, _kind, _split, _known = ctx, str(kind), str(split), known


# C02 (research/coldstart_C02/PLAN.md): a candidate whose |rank correlation| with the known family (the same p_rho_known
# this scorer reports: the signed raw panel against the known family's z-rank, training days, every 5th) is at least
# $PARTURA_RHO_REJECT gets fitness -inf -- it is scored and reported, but never bred from.  Unset = off (every earlier episode).
RHO_REJECT = float(os.environ["PARTURA_RHO_REJECT"]) if os.environ.get("PARTURA_RHO_REJECT") else None


class ParturaScorer:
    """Partura's pure-long reward (``partura.steer.reward``) as an AlphaCube
    scorer, plus the ``p_*`` archive columns ``scripts/idea_search.py`` reads
    back out of the GP archive.  Registered under the fitness kind
    ``"partura"`` by :func:`register`; built by :func:`_partura_scorer_factory`,
    not directly, so its train/valid split is always derived from the
    ``dates`` / ``warmup`` the factory was given."""

    # (the paired rewards' raw ratio and the size -- net excess a year -- behind the sized score come last)
    columns = ("p_score", "p_s_train", "p_s_valid", "p_share", "p_sign", "p_hl", "p_train_sharpe",
               "p_valid_sharpe", "p_train_ann", "p_valid_ann", "p_turnover", "p_dist", "p_rho_known",
               "p_ir_train", "p_ir_valid", "p_dann_train", "p_dann_valid")

    def __init__(self, target: np.ndarray, warmup: int, cut: int, **kw) -> None:
        if _ctx is None or _kind is None:
            raise RuntimeError("partura.ac_plugin.set_scorer_state(ctx, kind, split) was not called "
                               "before the 'partura' fitness kind was used")
        self._warmup, self._cut = int(warmup), int(cut)
        trimmed = np.asarray(target)[self._warmup:]
        if trimmed.shape != _ctx.tgt.shape or not np.array_equal(np.isfinite(trimmed), np.isfinite(_ctx.tgt)):
            raise RuntimeError(f"the GP's label grid {trimmed.shape} (target sans {self._warmup} warm-up "
                               f"row(s)) is not Partura's {_ctx.tgt.shape}: the reward context would be "
                               f"misaligned")
        self.base = asc.PanelScorer(trimmed, kind="rank_ic", turnover_penalty=0.0,
                                    min_coverage=kw.get("min_coverage", 0.5),
                                    min_scored_days=kw.get("min_scored_days", 0.5))
        self.target_t64, self.target_ranks_t = self.base.target_t64, self.base.target_ranks_t
        self.n = self.gate = self.rho_rejected = 0
        self.seconds = 0.0
        SCORERS.append(self)

    def score(self, panel: np.ndarray, gated: bool = True) -> Dict[str, float]:
        t = time.time()
        self.n += 1
        panel = np.asarray(panel)[self._warmup:]
        out = {**self.base.score(panel, gated=gated), **{c: float("nan") for c in self.columns}}
        if np.isfinite(out["fit"]):
            dist = dg.distinct_fraction(panel)
            out["p_dist"] = dist
            if gated and not dist >= 0.5:
                out["fit"] = -np.inf
        if not np.isfinite(out["fit"]):
            self.gate += 1
            self.seconds += time.time() - t
            return out
        r = steer_reward(panel, _ctx, _kind)
        z = dg._zrank(r["sign"] * np.asarray(panel[:self._cut:5], np.float64))
        k = (_ctx.base if _known is None else _known)[:self._cut:5]
        ok = np.isfinite(z) & np.isfinite(k)
        zc, kc = np.where(ok, z, 0.0), np.where(ok, k, 0.0)
        n = np.maximum(ok.sum(1), 1)
        with np.errstate(invalid="ignore", divide="ignore"):
            c = ((zc * kc).sum(1) - zc.sum(1) * kc.sum(1) / n) / np.sqrt(
                ((zc ** 2).sum(1) - zc.sum(1) ** 2 / n) * ((kc ** 2).sum(1) - kc.sum(1) ** 2 / n))
        rho_known = float(np.nanmean(c))
        rej = RHO_REJECT is not None and np.isfinite(rho_known) and abs(rho_known) >= RHO_REJECT
        if rej:
            self.rho_rejected += 1
        out.update(fit=0.03 * r["score"] if (np.isfinite(r["score"]) and not rej) else -np.inf, p_score=r["score"],
                   p_s_train=r["score_train"], p_s_valid=r["score_valid"],
                   p_share=r.get("screened_share", float("nan")), p_sign=r["sign"], p_hl=r["hl"],
                   p_train_sharpe=r["train"]["long_sharpe"], p_valid_sharpe=r["valid"]["long_sharpe"],
                   p_train_ann=r["train"]["long_ann"], p_valid_ann=r["valid"]["long_ann"],
                   p_turnover=r["train"]["long_turnover"], p_rho_known=float(np.nanmean(c)),
                   **{f"p_{k_}": float(r.get(k_, float("nan"))) for k_ in ("ir_train", "ir_valid", "dann_train", "dann_valid")})
        self.seconds += time.time() - t
        return out

    def score_combined(self, panel: np.ndarray) -> Dict[str, float]:
        """No per-candidate gates (coverage / scored-days) -- the pool's own
        combined signal already cleared them member by member."""
        return self.score(panel, gated=False)


def _partura_scorer_factory(target: np.ndarray, *, dates=None, warmup: int = 0, **kw) -> ParturaScorer:
    """Registered under ``"partura"`` (see :func:`register`); called by
    ``alphacube.mining.scoring.make_scorer`` exactly as every other factory is
    -- see that function's docstring for the full keyword set, absorbed here
    through ``**kw`` and forwarded into :class:`ParturaScorer`.

    ``dates`` INCLUDES GPMiner's own lead-in warm-up rows; ``dates[warmup]`` is
    the first day actually evaluated.  ``target`` (and every panel this
    scorer's ``.score`` is later called with) carries those same rows, so both
    are sliced ``[warmup:]`` before anything else -- which is what makes them
    land in the same row space as Partura's own ``ctx`` (built from
    ``PanelSet``, which already drops its view's own lead-in).  With
    ``warmup=0`` (today's one caller, ``scripts/idea_search.py``, whose
    ``start`` is the store's first date so its view's lead-in is empty anyway)
    this slice is a no-op and the split below lands on exactly the cut
    ``scripts/idea_search.py`` used to compute itself from a closed-over
    ``cut``."""
    if dates is None:
        raise ValueError("the 'partura' scorer needs dates (alphacube.mining.gp.GPMiner always supplies them)")
    if _split is None:
        raise RuntimeError("partura.ac_plugin.set_scorer_state(ctx, kind, split) was not called before "
                           "the 'partura' fitness kind was used")
    d = np.asarray(dates)
    warmup = int(warmup)
    if not (0 <= warmup < len(d)):
        raise ValueError(f"warmup ({warmup}) must be within [0, {len(d)}) for {len(d)} dates")
    cut = int(np.searchsorted(d[warmup:], _split))
    return ParturaScorer(target, warmup, cut, **kw)


def register() -> None:
    """Called by ``alphacube.plugins.load_plugins(["partura.ac_plugin"])``
    before the registry is (re)built -- see that function's docstring for why
    it is safe (and required) to call more than once in one process.

    What it does by default is exactly what ``main``'s ``ops_ext.install()``
    did for the search: Partura's kernels reach the legacy name tables, and the
    ``"partura"`` fitness kind exists.  (The nine kernels the registry's smoke
    test mis-flags as boolean are real-valued at their own ``@op`` now.)  The
    declaration of AlphaCube's own ``in_sustain_*`` trio is made only with the
    ``in_sustain`` fix on (:func:`fixes`): it enlarges the search vocabulary."""
    ops_ext.install_kernels()
    if "in_sustain" in fixes():
        declare_real_valued(*_AC_REAL_VALUED)
    register_scorer("partura", _partura_scorer_factory)


def partura_operator_names() -> FrozenSet[str]:
    """Every operator name ``partura/ops_ext.py`` adds to the registry: the
    kernels themselves plus the ``nt_`` twin each shared / nd one also
    registers under.  The one definition of "Partura's own operators", shared
    by :func:`arm_hooks` and by ``scripts/idea_search.py``'s own reporting."""
    names = frozenset(ops_ext.NEW_OPERATORS)
    return names | frozenset("nt_" + name for name in names)


def set_search_hooks(hooks: Optional[SearchHooks]) -> None:
    """Set (or, with ``None``, clear) the :class:`SearchHooks`
    :func:`search_hooks` hands back -- the generator-side counterpart of
    :func:`set_scorer_state`, and the ONLY way this plugin ever steers
    sampling or acceptance.

    Call it before ``run_mining`` / ``GPMiner``; ``scripts/idea_search.py``
    calls it once per arm with that arm's :func:`arm_hooks`.  A caller that
    never calls it (``--plugin partura.ac_plugin`` on AlphaCube's own CLI, say,
    loaded for Partura's 45 operators and the ``"partura"`` fitness kind) gets
    an empty bundle and therefore an unsteered run."""
    global _hooks
    if hooks is not None and not isinstance(hooks, SearchHooks):
        raise TypeError(f"search hooks must be an alphacube.plugins.SearchHooks or None, not "
                        f"{type(hooks).__name__}")
    _hooks = hooks


def search_hooks() -> SearchHooks:
    """Whatever :func:`set_search_hooks` was last given, else an EMPTY
    ``SearchHooks()``.  Read with no arguments by the CLI's ``--plugin`` /
    ``$ALPHACUBE_PLUGINS`` through ``alphacube.plugins.search_hooks_from``, and
    by ``scripts/idea_search.py`` per arm.

    Empty is the load-bearing default, not a stub.  ``SearchHooks()``'s fields
    are each exactly ``TypedTreeGenerator``'s own default, so ``GPMiner(
    hooks=SearchHooks())`` builds a byte-identical generator to ``hooks=None``
    -- i.e. ``alphacube mine --plugin partura.ac_plugin --seed 7``, run only to
    get Partura's operators and reward, stays comparable to the same command
    without ``--plugin``.  An opinion here would not be: even one that assigns
    weight 1.0 to every operator routes ``_pick`` through ``_pick_weighted``
    (``random.choices`` rather than ``random.choice``), which moves the draw
    sequence from index 0 on.  Measured (``alphacube.plugins.search_hooks_from
    (["partura.ac_plugin"])`` against a live ``default_registry()``): an
    op_weight zeroing the resource-risk operators outside ``ops_ext`` silently
    cancelled ``--allow-resource-risk`` for exactly 4 of the 281 searchable
    specs with no opt-out, and under the CLI's default
    ``allow_resource_risk=False`` zeroed none of the 277 yet still diverged
    ``generate_population(30)`` at index 0.  Both are pinned by
    tests/test_ac_plugin.py.

    ``scripts/idea_search.py``'s own arms are built by :func:`arm_hooks` and
    then set here: the steer arm's ``accept`` hook needs that run's guidance
    and idea, which this function -- called with no arguments -- cannot know."""
    return _hooks if _hooks is not None else SearchHooks()


ARM_PARTS = ("seeds", "hood", "priors")           # what a steer arm can be made of (--parts)


def env_operator_weights() -> Dict[str, float]:
    """The ENVIRONMENT's operator weights, applied to BOTH arms (C02, research/coldstart_C02/PLAN.md): read from
    ``$PARTURA_ENV_OPW`` as ``name=w,prefix*=w`` (e.g. ``ts_spearman=0,nt_*=0``).  Unset = {} = every weight 1.0,
    i.e. exactly the behaviour of every earlier episode."""
    out: Dict[str, float] = {}
    for item in (os.environ.get("PARTURA_ENV_OPW") or "").split(","):
        if "=" in item:
            k, v = item.split("=", 1)
            out[k.strip()] = float(v)
    return out


def env_weight(env: Mapping[str, float], name: str) -> float:
    if not env:
        return 1.0
    if name in env:
        return float(env[name])
    for k, v in env.items():
        if k.endswith("*") and name.startswith(k[:-1]):
            return float(v)
    return 1.0


def arm_hooks(arm: str, *, parts: Optional[Iterable[str]] = None, risky: Optional[Iterable[str]] = None,
              ext: Optional[Iterable[str]] = None, opw: Optional[Mapping[str, float]] = None,
              idea_ops: Iterable[str] = (), boost: float = 1.0, accept: Optional[Callable] = None,
              nt_twins: bool = False) -> SearchHooks:
    """The :class:`SearchHooks` for one arm of ``scripts/idea_search.py``'s A/B
    -- the single home of the operator-weight formula both arms share, so the
    arms cannot drift apart (and cannot be swapped) without this function
    saying so.  Pure: no module state, no registry, no I/O.

    * ``"control"`` -- ``op_weight`` is the base library filter ALONE (every
      AlphaCube resource-risk operator that is not one of Partura's own weighs
      0, everything else 1.0) and ``accept`` is ``None``.  ``parts``, ``opw``,
      ``idea_ops``, ``boost``, ``accept`` and ``nt_twins`` are accepted and
      deliberately IGNORED, so one call site can pass the same keywords for
      both arms.
    * ``"steer"`` -- that same base weight times the guidance's own
      per-operator weight (``opw``, default 1.0) times ``boost`` for an
      operator of the idea, plus ``accept`` as the acceptance hook -- each of
      the three only when the matching part is in ``parts``.

    ``parts`` is what the steer arm is made of (``--parts``; ``None`` = all
    three): ``"priors"`` switches the guidance on (its operator weights, and
    ``accept``'s bans / thinning / equivalence / siblings), ``"hood"`` the
    idea's neighbourhood (the ``boost`` of its operators, and ``accept``'s
    must-contain test), ``"seeds"`` the idea's seeds -- which are the caller's
    ``initial_population``, so they change nothing here.  With neither
    ``"priors"`` nor ``"hood"`` the steer arm is handed no ``accept`` and plain
    weights: it is the control to the last draw (``--parts none`` is the
    ablation that says so).

    So the two arms differ in exactly the two fields the design says they may
    (``op_weight``, ``accept``): the boost and the guidance are the steer arm's
    and only the steer arm's.  ``risky`` defaults to reading ``spec
    .resource_risk`` off each spec; pass the name set from the run's own
    registry (``{s.name for s in reg.list_all() if s.resource_risk}``) to keep
    the formula textually identical to the pre-WP11 script's.

    ``opw`` and ``idea_ops`` are matched by ``spec.name`` -- exactly as the
    monkeypatching ``pick`` of ``main`` did.  An ND-face kernel is in the
    registry TWICE, as ``X`` and as ``nt_X``, and both sets are written in
    ND-face spelling (``opw`` from ``steer.Guidance.operator_weights()``, whose
    keys are the heads of hand-written rule patterns; ``idea_ops`` from
    scraping the idea's own expression text), so by name alone the ``nt_`` twin
    keeps weight 1.0: measured on AlphaCube over 400 seeds x
    ``generate_population(25)``, zeroing one nd-face name took its ND-face
    draws 148 -> 0 and left the twin's at 17 -> 17.  ``nt_twins=True`` closes
    that half (the twin inherits the ND name's entry unless it has one of its
    own, ``alphacube.mining.generator.nd_twin_base``) -- the fix the WP11
    branch carried.  It is OFF by default because it changes which operators
    the steer arm draws, so a run with it on is a different experiment from
    every stored episode.  ``ext`` already expanded the twins itself
    (:func:`partura_operator_names`)."""
    if arm not in ARMS:
        raise ValueError(f"arm must be one of {ARMS}, not {arm!r}")
    made_of = frozenset(ARM_PARTS if parts is None else parts)
    if made_of - set(ARM_PARTS):
        raise ValueError(f"parts takes {ARM_PARTS}; got {sorted(made_of - set(ARM_PARTS))}")
    risk_names = None if risky is None else frozenset(risky)
    ext_names = partura_operator_names() if ext is None else frozenset(ext)
    boost = float(boost)
    if not math.isfinite(boost) or boost < 0:
        raise ValueError(f"boost must be a finite float >= 0, not {boost!r}")

    env = env_operator_weights()

    def base_weight(spec) -> float:
        risk = spec.resource_risk if risk_names is None else (spec.name in risk_names)
        if risk and spec.name not in ext_names:
            return 0.0
        return env_weight(env, spec.name)

    # C04: the environment's daily leaves (both arms; $PARTURA_DAILY_FIELDS, $PARTURA_DAILY_LEAF_PROB); unset = none
    dfields = tuple(x for x in (os.environ.get("PARTURA_DAILY_FIELDS") or "").split(",") if x)
    dprob = float(os.environ.get("PARTURA_DAILY_LEAF_PROB", "0")) if dfields else 0.0
    dkw = {"daily_fields": dfields, "daily_leaf_prob": dprob} if dfields else {}

    if arm == "control":
        return SearchHooks(op_weight=base_weight, **dkw)

    weights = dict(opw or {}) if "priors" in made_of else {}
    idea = frozenset(idea_ops) if "hood" in made_of else frozenset()
    judge = accept if made_of & {"hood", "priors"} else None

    def weighted(spec) -> float:
        twin = nd_twin_base(spec) if nt_twins else None   # the ND-face name an nt_ spec is the twin of, else None
        w = weights.get(spec.name)
        if w is None:
            w = 1.0 if twin is None else weights.get(twin, 1.0)
        in_idea = spec.name in idea or (twin is not None and twin in idea)
        return base_weight(spec) * float(w) * (boost if in_idea else 1.0)

    return SearchHooks(op_weight=weighted, accept=judge, **dkw)


def asked_from(*methods: str) -> bool:
    """Is the ``accept`` hook that is running now being asked for the child of one
    of the ``TypedTreeGenerator`` methods named in ``methods``?

    ``SearchHooks.accept`` is called ``accept(tree)`` from the generator's
    ``acceptable()`` and says nothing about WHO asked.  One counter of the
    evidence (``sampling["mutation_refused"]``: a window or a constant mutation
    whose child the guidance turned down) needs exactly that, and the
    monkeypatching script got it for free by wrapping those two methods.  So the
    hook looks one frame up the stack for ``acceptable`` and reads the name of
    its caller.  Only called on a refusal, so the cost is nil; ``False`` when
    the hook is called some other way (a unit test, a tool).  The coupling to
    AlphaCube's method names is pinned by
    ``tests/test_ac_plugin.py::test_asked_from_sees_the_mutator_that_asked``."""
    f = sys._getframe(1)
    while f is not None:
        if f.f_code.co_name == "acceptable" and f.f_code.co_filename.replace("\\", "/").endswith("mining/generator.py"):
            caller = f.f_back
            return caller is not None and caller.f_code.co_name in methods
        f = f.f_back
    return False


__all__ = ["ARMS", "ARM_PARTS", "KNOWN_FIXES", "SCORERS", "ParturaScorer", "arm_hooks", "asked_from", "fixes",
           "partura_operator_names", "register", "search_hooks", "set_fixes", "set_scorer_state", "set_search_hooks"]
