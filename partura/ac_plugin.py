"""The AlphaCube plugin AlphaCube loads back: ``--plugin partura.ac_plugin`` /
``alphacube.plugins.load_plugins(["partura.ac_plugin"])``.

AlphaCube never imports Partura on its own -- a caller always names this module
itself.  Importing it is what used to require ``ops_ext.install()``'s
``catalog.build_registry`` monkeypatch and a bespoke ``install(arm)`` that
rebound ``TypedTreeGenerator._pick`` / ``.acceptable`` inside
``scripts/idea_search.py``; both are gone (WP11).  What is left:

* :func:`register` -- called once by ``load_plugins`` before the registry is
  (re)built: wires ``ops_ext``'s legacy-table entries, declares AlphaCube's own
  three ``in_sustain_*`` kernels real-valued, and registers the ``"partura"``
  fitness kind (see ``alphacube.mining.scoring.register_scorer``).
* :func:`search_hooks` -- the plugin's base, idea-independent steering opinion,
  read by the CLI / ``alphacube.plugins.search_hooks_from``.
* :class:`ParturaScorer` / :func:`_partura_scorer_factory` -- the reward
  ``scripts/idea_search.py`` used to define inline, with its ``ctx`` / ``KIND``
  closure replaced by :func:`set_scorer_state` (module state the caller sets
  once, before ``run_mining``) and its train/valid split recomputed from the
  ``dates`` / ``warmup`` the factory itself receives rather than from a
  script-level global.

See docs/alphacube_steering_design.md, "丙 Migration" and "### WP11"."""
from __future__ import annotations

import time
from typing import Dict, List, Optional

import numpy as np

from .bridge import ensure_alphacube_on_path

ensure_alphacube_on_path()

from alphacube.mining import scoring as asc  # noqa: E402
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

# -- module state a caller sets once, before run_mining, in place of the
# ctx/KIND closure scripts/idea_search.py used to build ParturaScorer with
# inline.  Every arm of one run shares the same reward, context and split.
_ctx: Optional[RewardContext] = None
_kind: Optional[str] = None
_split: Optional[str] = None

# Every ParturaScorer ever constructed, in construction order -- the caller
# slices this by its own high-water mark (``n0 = len(SCORERS)`` before an
# arm's run) to read back .n / .gate / .seconds for just that arm; nothing
# here ever clears it.
SCORERS: List["ParturaScorer"] = []


def set_scorer_state(ctx: RewardContext, kind: str, split: str) -> None:
    """Tell :func:`_partura_scorer_factory` what reward context, reward kind
    and train/valid split date to score with.  ``ctx`` must be built over the
    SAME view GPMiner itself mines on (its ``tgt`` / ``untradable`` / ``liq`` /
    ``pool`` / ``base`` planes are taken as already correctly trimmed of
    whatever lead-in warm-up rows that view carries -- see
    :func:`_partura_scorer_factory`).  Call this once per run, before
    ``run_mining``; it is the same for every arm of one run."""
    global _ctx, _kind, _split
    _ctx, _kind, _split = ctx, str(kind), str(split)


class ParturaScorer:
    """Partura's pure-long reward (``partura.steer.reward``) as an AlphaCube
    scorer, plus the ``p_*`` archive columns ``scripts/idea_search.py`` reads
    back out of the GP archive.  Registered under the fitness kind
    ``"partura"`` by :func:`register`; built by :func:`_partura_scorer_factory`,
    not directly, so its train/valid split is always derived from the
    ``dates`` / ``warmup`` the factory was given."""

    columns = ("p_score", "p_sign", "p_hl", "p_train_sharpe", "p_valid_sharpe", "p_train_ann",
               "p_valid_ann", "p_turnover", "p_dist", "p_rho_known")

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
        self.n = self.gate = 0
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
        k = _ctx.base[:self._cut:5]
        ok = np.isfinite(z) & np.isfinite(k)
        zc, kc = np.where(ok, z, 0.0), np.where(ok, k, 0.0)
        n = np.maximum(ok.sum(1), 1)
        with np.errstate(invalid="ignore", divide="ignore"):
            c = ((zc * kc).sum(1) - zc.sum(1) * kc.sum(1) / n) / np.sqrt(
                ((zc ** 2).sum(1) - zc.sum(1) ** 2 / n) * ((kc ** 2).sum(1) - kc.sum(1) ** 2 / n))
        out.update(fit=0.03 * r["score"] if np.isfinite(r["score"]) else -np.inf, p_score=r["score"],
                   p_sign=r["sign"], p_hl=r["hl"], p_train_sharpe=r["train"]["long_sharpe"],
                   p_valid_sharpe=r["valid"]["long_sharpe"], p_train_ann=r["train"]["long_ann"],
                   p_valid_ann=r["valid"]["long_ann"], p_turnover=r["train"]["long_turnover"],
                   p_rho_known=float(np.nanmean(c)))
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
    it is safe (and required) to call more than once in one process."""
    ops_ext.install_kernels()
    declare_real_valued(*_AC_REAL_VALUED)
    register_scorer("partura", _partura_scorer_factory)


def search_hooks() -> SearchHooks:
    """The plugin's base steering opinion with no further configuration: weight
    every AlphaCube resource-risk operator that is not one of Partura's own
    ``ops_ext`` kernels to 0 (a full-market search should not pay for an
    operator Partura does not already rely on), and leave sampling and
    acceptance otherwise exactly as today.  Read by the CLI's ``--plugin`` /
    ``alphacube.plugins.search_hooks_from`` for a run with no further
    Python-level configuration.

    ``scripts/idea_search.py`` builds its own, idea-specific ``SearchHooks``
    instead of calling this directly: the steer arm's ``accept`` hook needs
    that run's guidance and idea, which this function -- called with no
    arguments -- has no way to know."""
    ext = set(ops_ext.NEW_OPERATORS) | {"nt_" + name for name in ops_ext.NEW_OPERATORS}

    def op_weight(spec) -> float:
        return 0.0 if (spec.resource_risk and spec.name not in ext) else 1.0

    return SearchHooks(op_weight=op_weight)


__all__ = ["SCORERS", "ParturaScorer", "set_scorer_state", "register", "search_hooks"]
