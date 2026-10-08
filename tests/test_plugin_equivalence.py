"""The plugin route against ``main``'s monkeypatching route: same weights, same filter, same counters, same reward.

``scripts/idea_search.py`` of ``main`` (frozen at commit 980a24e) rebound ``TypedTreeGenerator._pick`` /
``.acceptable`` / the window and constant mutations and wrapped ``make_scorer``.  The merged script reaches the same
places through ``alphacube.plugins`` (``SearchHooks`` + a registered scorer).  These tests re-create the old route
on AlphaCube-steering's own generator -- as a subclass, in the test, from a transcription of ``main``'s code -- and
check, draw for draw, that the plugin route does what it did.  The baseline AlphaCube cannot be imported next to
the steering one, so the end-to-end proof (the real scripts, the real baseline, a synthetic store) is a run outside
the suite; ``scripts/plugin_acceptance.py`` is its check against the stored server episodes.

    ALPHACUBE_ROOT=~/Desktop/AlphaCube-steering PYTHONPATH=~/Desktop/AlphaCube-steering/src:. \
        python -m pytest tests/test_plugin_equivalence.py -q
"""
import ast
import random
import re
import sys
from collections import Counter
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from partura import ac_plugin, diagnose as dg
from partura.bridge import ensure_alphacube_on_path
from partura.steer import REWARDS, Guidance, RewardContext

ensure_alphacube_on_path()

import alphacube.catalog as catalog  # noqa: E402
from alphacube.catalog import default_registry  # noqa: E402
from alphacube.expression import is_valid_root  # noqa: E402
from alphacube.mining import scoring as asc  # noqa: E402
from alphacube.mining.generator import TypedTreeGenerator  # noqa: E402
from alphacube.parser import parse  # noqa: E402
from alphacube.plugins import load_plugins  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "idea_search.py"
G = Guidance.load(ROOT / "guidance" / "B01.yaml")
IDEA = next(i for i in G.spec["ideas"] if i["id"] == "I1_frozen_state")
BOOST = 8.0


@pytest.fixture(scope="module")
def reg():
    """The registry the script searches: plugin loaded, no opt-in fix."""
    ac_plugin.set_fixes(None)
    assert not ac_plugin.fixes(), "run this file without $PARTURA_AC_FIXES"
    catalog.REAL_VALUED_OVERRIDES.difference_update(ac_plugin._AC_REAL_VALUED)
    catalog._DEFAULT = None
    load_plugins(["partura.ac_plugin"])
    return default_registry()


def idea_sets(idea):
    """IDEA_OPS and MUST, computed as the script computes them."""
    gram = idea.get("grammar") or {}
    ops = set()
    for key in ("day_ops", "memory_ops", "convex", "fold", "inner", "ops"):
        for x in gram.get(key, []):
            ops.update(re.findall(r"[A-Za-z_][A-Za-z_0-9]*(?=\()", x) or [x])
    for s in idea.get("seeds", []):
        ops.update(re.findall(r"[A-Za-z_][A-Za-z_0-9]*(?=\()", s))
    return ops, set(gram.get("day_ops", []))


IDEA_OPS, MUST = idea_sets(IDEA)
OPW = G.operator_weights()
PARTS_GRID = [("seeds", "hood", "priors"), ("priors",), ("hood",), ("seeds",), ("seeds", "priors"), ("hood", "priors"), ()]


def risky_of(reg):
    return {s.name for s in reg.list_all() if getattr(s, "resource_risk", False)}


# ------------------------------------------------------------------------------------------ main's code, transcribed
def main_weight(s, arm, parts, risky, ext, opw, idea_ops, boost):
    """``base_weight`` and the steer arm's factor in ``pick``, scripts/idea_search.py of main@980a24e."""
    w = 0.0 if (s.name in risky and s.name not in ext) else 1.0
    if arm == "steer":
        w *= (opw.get(s.name, 1.0) if "priors" in parts else 1.0) * (boost if ("hood" in parts and s.name in idea_ops) else 1.0)
    return w


class MainRoute(TypedTreeGenerator):
    """``main``'s ``install(arm)`` re-created on AlphaCube-steering's generator: its ``pick`` as ``_pick``, its
    ``acceptable`` (the baseline's legal-root + ban test, then the steering filter), its ``guarded`` window / constant
    mutations, and the baseline's ``generate()`` whose fallback does not ask ``acceptable``.  ``mutation_checks_bans
    =False`` gives back the baseline's window / constant mutations (``is_valid_root`` only), which is what ``main``'s
    route started from."""

    def __init__(self, registry, *, arm, parts, weight, filter_state, **kw):
        super().__init__(registry, mutation_checks_bans=False, **kw)
        self.arm, self.parts, self.weight = arm, frozenset(parts), weight
        self.stats, self.first_form, self.family_first, self.hook_rng, self.seeds_repr = filter_state
        self.fallbacks = 0

    def _pick(self, specs):                       # main's `pick`
        faces = {}
        for s in specs:
            w = self.weight(s)
            if w > 0:
                faces.setdefault(s.face, []).append((s, w))
        if not faces:
            return TypedTreeGenerator._pick(self, specs)
        names = sorted(faces)
        f = self._rng.choices(names, weights=[sum(w for _, w in faces[n]) / len(faces[n]) for n in names])[0]
        return self._rng.choices([s for s, _ in faces[f]], weights=[w for _, w in faces[f]])[0]

    def acceptable(self, tree):                   # main's `acceptable`
        if not (is_valid_root(tree) and self._ban_ok(tree)):
            return False
        if self.arm != "steer" or not (self.parts & {"hood", "priors"}):
            return True
        stats, parts = self.stats, self.parts
        e = repr(tree)
        if e in self.seeds_repr and "seeds" in parts:
            return True
        stats["proposed"] += 1
        priors = "priors" in parts
        try:
            key = G.dedup_key(e)
            if priors and self.first_form.setdefault(key, e) != e:
                stats["equivalent"] += 1
                return False
            if priors and G.banned(e):
                stats["banned"] += 1
                return False
            if "hood" in parts and MUST and not (MUST & set(re.findall(r"[A-Za-z_][A-Za-z_0-9]*", e))):
                stats["outside"] += 1
                return False
            if priors and not G.accept(e, u=self.hook_rng.random()):
                stats["thinned"] += 1
                return False
            fam = G.family_key(e)
            if priors and self.family_first.setdefault(fam, key) != key and self.hook_rng.random() >= G.family_weight:
                stats["sibling"] += 1
                return False
        except ValueError:
            stats["unread"] += 1
        stats["accepted"] += 1
        return True

    def _guarded(self, child):
        if self.arm == "steer" and self.parts & {"hood", "priors"}:
            if child is None or self.acceptable(child):
                return child
            self.stats["mutation_refused"] += 1
            return None
        return child

    def mutate_window(self, expr):
        return self._guarded(super().mutate_window(expr))

    def mutate_constant(self, expr):
        return self._guarded(super().mutate_constant(expr))

    def generate(self, depth=None):               # the baseline's: the fallback tree is returned without asking
        d = depth if depth is not None else self._rng.randint(self.min_depth, self.max_depth)
        from alphacube.expression import ShapeError
        for _ in range(self.max_retries * 4):
            try:
                tree = self._gen("daily", d, full=self._rng.random() < 0.5, root=True)
            except ShapeError:
                continue
            if self.acceptable(tree):
                return tree
        self.fallbacks += 1
        return self._collapse_leaf(self._pick(self._root_ops_of("reduce")))


def script_filter(parts, seeds_repr, seed):
    """The script's own ``refused`` / ``guidance_accept``, cut out of ``scripts/idea_search.py`` and bound to a fresh
    namespace -- so what is tested is the code that runs, not a copy of it."""
    tree = ast.parse(SCRIPT.read_text(encoding="utf-8"))
    fns = sorted((n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name in ("refused", "guidance_accept")),
                 key=lambda n: n.lineno)
    assert [f.name for f in fns] == ["refused", "guidance_accept"]
    stats, first_form, family_first = Counter(), {}, {}
    hook_rng = random.Random((seed * 2654435761) & 0xFFFFFFFF)
    ns = dict(ac_plugin=ac_plugin, stats=stats, first_form=first_form, family_first=family_first, hook_rng=hook_rng,
              seeds_repr=seeds_repr, PARTS=frozenset(parts), G=G, MUST=MUST, re=re)
    exec(compile(ast.fix_missing_locations(ast.Module(body=fns, type_ignores=[])), str(SCRIPT), "exec"), ns)
    return ns["guidance_accept"], stats, hook_rng


def parsed_seeds():
    out = []
    for s in IDEA.get("seeds", []):
        try:
            out.append(parse(G.canonical(s), strict=True, coerce_daily=True, n_minutes=241, allow_general=True))
        except Exception:                                                  # noqa: BLE001  (the script drops these too)
            pass
    return out


def mutate(gen, expr):                            # GPMiner._mutate
    kinds = ["subtree", "operator", "hoist", "window", "constant"]
    gen._rng.shuffle(kinds)
    for k in kinds:
        child = {"subtree": gen.mutate_subtree, "operator": gen.mutate_operator, "hoist": gen.mutate_hoist,
                 "window": gen.mutate_window, "constant": gen.mutate_constant}[k](expr)
        if child is not None:
            return child
    return gen.generate()


def drive(gen, seeds, size=40, rounds=5):
    """GPMiner's breeding loop without the fitness: the seeds are offered to ``acceptable`` first (as GPMiner's
    constructor does), a first population, then ``rounds`` generations of crossover / mutation of random parents.
    Returns every tree's key, in order."""
    ok_seeds = [e for e in seeds if gen.acceptable(e)]
    pop = ok_seeds[: size // 4] + gen.generate_population(size - len(ok_seeds[: size // 4]))
    out = [e.key() for e in pop]
    for _ in range(rounds):
        nxt = []
        while len(nxt) < size:
            if gen._rng.random() < 0.7:
                a, b = gen._rng.choice(pop), gen._rng.choice(pop)
                child = gen.crossover(a, b) or a
            else:
                child = gen._rng.choice(pop)
            if gen._rng.random() < 0.9:
                child = mutate(gen, child)
            if not is_valid_root(child):
                child = gen.generate()
            nxt.append(child)
        pop = nxt
        out.extend(e.key() for e in pop)
    return out


# ------------------------------------------------------------------------------------------------------- the weights
@pytest.mark.parametrize("arm", ["control", "steer"])
@pytest.mark.parametrize("parts", PARTS_GRID)
def test_every_operator_weight_is_mains(reg, arm, parts):
    """``arm_hooks`` as the script calls it gives every registered operator -- both faces -- exactly the weight
    ``main``'s ``pick`` computed, for each subset of ``--parts``."""
    risky, ext = risky_of(reg), ac_plugin.partura_operator_names()
    hooks = ac_plugin.arm_hooks(arm, parts=parts, risky=risky, ext=ext, opw=OPW, idea_ops=IDEA_OPS, boost=BOOST,
                                accept=lambda tree: True)
    for s in reg.list_all():
        assert hooks.op_weight(s) == main_weight(s, arm, parts, risky, ext, OPW, IDEA_OPS, BOOST), s.name
    # the accept hook is attached to the steer arm made of hood and/or priors, and to nothing else
    assert (hooks.accept is not None) == (arm == "steer" and bool(set(parts) & {"hood", "priors"}))


def test_the_default_guidance_really_does_steer_the_operators_it_is_tested_on(reg):
    """(a test that cannot fail is worth nothing: with the real guidance and idea the weights are not all 1.0)"""
    hooks = ac_plugin.arm_hooks("steer", risky=risky_of(reg), ext=ac_plugin.partura_operator_names(), opw=OPW,
                                idea_ops=IDEA_OPS, boost=BOOST, accept=lambda tree: True)
    ws = Counter(hooks.op_weight(s) for s in reg.list_all())
    assert BOOST in ws and 0.0 in ws and any(0.0 < w < 1.0 for w in ws)


# ------------------------------------------------------------------------- the filter, the picks, the mutations
@pytest.mark.parametrize("seed", [1, 7])
@pytest.mark.parametrize("arm,parts", [("control", ("seeds", "hood", "priors"))] + [("steer", p) for p in PARTS_GRID])
def test_generation_breeding_and_counters_are_draw_for_draw_mains(reg, arm, parts, seed):
    """The whole chain at once: ``_pick``'s two draws, ``acceptable`` at every acceptance point, the guidance's own
    stream, the window / constant mutations the old script wrapped -- same trees in the same order, same counters,
    same position in both random streams."""
    risky, ext = risky_of(reg), ac_plugin.partura_operator_names()
    seeds = parsed_seeds()
    seeds_repr = {repr(e) for e in seeds}
    kw = dict(allow_resource_risk=True, min_depth=2, max_depth=4)

    old_state = (Counter(), {}, {}, random.Random((seed * 2654435761) & 0xFFFFFFFF), seeds_repr)
    old = MainRoute(reg, arm=arm, parts=parts, filter_state=old_state, rng=random.Random(seed),
                    weight=lambda s: main_weight(s, arm, frozenset(parts), risky, ext, OPW, IDEA_OPS, BOOST), **kw)
    offered = seeds if (arm == "steer" and "seeds" in parts) else []          # the script hands the GP seeds for exactly that arm
    old_keys = drive(old, offered)

    accept, stats, hook_rng = script_filter(parts, seeds_repr, seed)
    hooks = ac_plugin.arm_hooks(arm, parts=parts, risky=risky, ext=ext, opw=OPW, idea_ops=IDEA_OPS, boost=BOOST, accept=accept)
    new = TypedTreeGenerator(reg, rng=random.Random(seed), op_weight=hooks.op_weight, accept=hooks.accept, **kw)
    new_keys = drive(new, offered)

    assert old.fallbacks == 0, "the run reached generate()'s fallback, the one place the two routes differ by design"
    assert new_keys == old_keys
    assert new._rng.getstate() == old._rng.getstate()                       # the miner's own stream: same position
    assert dict(stats) == dict(old.stats) and list(stats) == list(old.stats)
    assert hook_rng.getstate() == old.hook_rng.getstate()                   # the guidance's stream: same position
    if arm == "steer" and set(parts) & {"hood", "priors"}:
        assert stats["proposed"] > 100 and stats["accepted"] > 20
    if arm == "steer" and "priors" in parts:
        assert stats["thinned"] > 0                                         # the filter drew
    if arm == "control" or not set(parts) & {"hood", "priors"}:
        assert not stats                                                   # the control arm is not touched by any hook


def test_mutation_refused_matches_mains_count_when_the_guidance_does_refuse_mutations(reg):
    """A directed case with a long run, so that the counter is not trivially 0 == 0 (the grid above is only as
    strong as its counters are non-zero)."""
    risky, ext = risky_of(reg), ac_plugin.partura_operator_names()
    parts, seed = ("priors",), 5
    kw = dict(allow_resource_risk=True, min_depth=2, max_depth=4)
    old_state = (Counter(), {}, {}, random.Random((seed * 2654435761) & 0xFFFFFFFF), set())
    old = MainRoute(reg, arm="steer", parts=parts, filter_state=old_state, rng=random.Random(seed),
                    weight=lambda s: main_weight(s, "steer", frozenset(parts), risky, ext, OPW, IDEA_OPS, BOOST), **kw)
    old_keys = drive(old, [], size=48, rounds=40)
    accept, stats, _ = script_filter(parts, set(), seed)
    hooks = ac_plugin.arm_hooks("steer", parts=parts, risky=risky, ext=ext, opw=OPW, idea_ops=IDEA_OPS, boost=BOOST, accept=accept)
    new = TypedTreeGenerator(reg, rng=random.Random(seed), op_weight=hooks.op_weight, accept=hooks.accept, **kw)
    assert drive(new, [], size=48, rounds=40) == old_keys
    assert old.fallbacks == 0
    assert old.stats["mutation_refused"] > 0
    assert dict(stats) == dict(old.stats)


def test_mutation_refused_is_counted_on_window_and_constant_mutations_only(reg):
    """The one counter the hook signature cannot see on its own.  Across the grid above it matches ``main``'s; this
    pins that it is the mutator that decides, with a hook that refuses everything."""
    seen = []
    gen = TypedTreeGenerator(reg, rng=random.Random(3), allow_resource_risk=True,
                             accept=lambda tree: seen.append(ac_plugin.asked_from("mutate_window", "mutate_constant")) or True)
    base = gen.generate_population(30)
    seen.clear()
    windowed = next(e for e in base if any(n.window is not None and not n.spec.restores_m for n in e.nodes()))
    for _ in range(40):
        gen.mutate_window(windowed)
    assert seen and all(seen)                                  # every acceptable() it caused came from mutate_window
    seen.clear()
    for e in base:
        gen.mutate_subtree(e), gen.mutate_operator(e), gen.mutate_hoist(e)
        gen.crossover(e, base[0])
    gen.generate()
    assert seen and not any(seen)                              # none of those is a window / constant mutation
    assert ac_plugin.asked_from("mutate_window") is False      # called from outside a generator: no


def test_asked_from_sees_the_mutator_that_asked(reg):
    calls = []
    gen = TypedTreeGenerator(reg, rng=random.Random(5), allow_resource_risk=True,
                             accept=lambda tree: calls.append(ac_plugin.asked_from("mutate_constant")) or True)
    consts = [e for e in gen.generate_population(80) if any(type(n).__name__ == "Constant" for n in e.nodes())]
    assert consts, "no tree with a constant among 80"
    calls.clear()
    for e in consts:
        gen.mutate_constant(e)
    assert calls and all(calls)


def test_generate_fallback_is_the_one_place_the_routes_differ_by_design(reg):
    """Documented, not hidden: when ``generate()`` runs out of its 64 tries, the baseline AlphaCube returns the
    minimal ``day_*`` tree WITHOUT asking ``acceptable`` (``main``'s route inherited that), while AlphaCube-steering
    asks it -- up to 64 more times when a hook is installed -- so the hook's counters and streams, and the miner's own
    stream, move differently.  The tree RETURNED is the same first minimal tree.  It needs 64 refusals in a row: at the
    lowest per-try acceptance of any stored steer arm (0.17, e2_I2) that is 5e-6 per ``generate()`` call; the grid above
    never reached it.  If AlphaCube changes this, this test says so."""
    class Baseline(TypedTreeGenerator):
        fallbacks = 0

        def acceptable(self, tree):
            return False                                          # the guidance turns everything down

        def generate(self, depth=None):                          # the baseline's generate()
            from alphacube.expression import ShapeError
            d = depth if depth is not None else self._rng.randint(self.min_depth, self.max_depth)
            for _ in range(self.max_retries * 4):
                try:
                    tree = self._gen("daily", d, full=self._rng.random() < 0.5, root=True)
                except ShapeError:
                    continue
                if self.acceptable(tree):
                    return tree
            self.fallbacks += 1
            return self._collapse_leaf(self._pick(self._root_ops_of("reduce")))

    calls = []
    old = Baseline(reg, rng=random.Random(11), allow_resource_risk=True)
    new = TypedTreeGenerator(reg, rng=random.Random(11), allow_resource_risk=True, accept=lambda tree: calls.append(1) and False)
    a, b = old.generate(3), new.generate(3)
    assert old.fallbacks == 1
    assert repr(a) == repr(b)                                     # the same first minimal tree ...
    assert new.unaccepted_fallbacks == 1 and 64 < len(calls) <= 64 + 64     # ... after up to 64 asks in the main loop and 64 in the fallback
    assert old._rng.getstate() != new._rng.getstate()             # ... but the miner's stream is no longer in step


# ---------------------------------------------------------------------------------------------------------- the reward
def _world(seed=0, D=260, S=120):
    rng = np.random.default_rng(seed)
    alpha = np.cumsum(rng.normal(size=(D, S)), axis=0) / np.sqrt(np.arange(1, D + 1))[:, None]
    liq = rng.normal(size=(1, S)) + 0.1 * rng.normal(size=(D, S))
    tgt = 0.002 * alpha - 0.001 * liq + 0.02 * rng.normal(size=(D, S))
    tgt[rng.random((D, S)) < 0.02] = np.nan
    frozen = rng.random((D, S)) < 0.1
    pool = dg._zrank(-liq + 0.3 * rng.normal(size=(D, S)))
    return alpha, liq, tgt, frozen, pool


class MainScorer:
    """``ParturaScorer`` of scripts/idea_search.py of main@980a24e, its closure variables made arguments."""
    columns = ("p_score", "p_s_train", "p_s_valid", "p_share", "p_sign", "p_hl", "p_train_sharpe", "p_valid_sharpe", "p_train_ann",
               "p_valid_ann", "p_turnover", "p_dist", "p_rho_known", "p_ir_train", "p_ir_valid", "p_dann_train", "p_dann_valid")

    def __init__(self, target, ctx, KIND, known_z, cut, **kw):
        self.base = asc.PanelScorer(target, kind="rank_ic", turnover_penalty=0.0, min_coverage=kw.get("min_coverage", 0.5),
                                    min_scored_days=kw.get("min_scored_days", 0.5))
        self.ctx, self.KIND, self.known_z, self.cut = ctx, KIND, known_z, cut
        self.n = self.gate = 0

    def score(self, panel, gated=True):
        from partura.steer import reward as steer_reward
        ctx, KIND, known_z, cut = self.ctx, self.KIND, self.known_z, self.cut
        self.n += 1
        out = {**self.base.score(panel, gated=gated), **{c: float("nan") for c in self.columns}}
        if np.isfinite(out["fit"]):
            dist = dg.distinct_fraction(panel)
            out["p_dist"] = dist
            if gated and not dist >= 0.5:
                out["fit"] = -np.inf
        if not np.isfinite(out["fit"]):
            self.gate += 1
            return out
        r = steer_reward(panel, ctx, KIND)
        z = dg._zrank(r["sign"] * np.asarray(panel[:cut:5], np.float64))
        k = known_z[:cut:5]
        ok = np.isfinite(z) & np.isfinite(k)
        zc, kc = np.where(ok, z, 0.0), np.where(ok, k, 0.0)
        n = np.maximum(ok.sum(1), 1)
        with np.errstate(invalid="ignore", divide="ignore"):
            c = ((zc * kc).sum(1) - zc.sum(1) * kc.sum(1) / n) / np.sqrt(((zc ** 2).sum(1) - zc.sum(1) ** 2 / n) * ((kc ** 2).sum(1) - kc.sum(1) ** 2 / n))
        out.update(fit=0.03 * r["score"] if np.isfinite(r["score"]) else -np.inf, p_score=r["score"], p_s_train=r["score_train"],
                   p_s_valid=r["score_valid"], p_share=r.get("screened_share", float("nan")), p_sign=r["sign"], p_hl=r["hl"],
                   p_train_sharpe=r["train"]["long_sharpe"], p_valid_sharpe=r["valid"]["long_sharpe"], p_train_ann=r["train"]["long_ann"],
                   p_valid_ann=r["valid"]["long_ann"], p_turnover=r["train"]["long_turnover"], p_rho_known=float(np.nanmean(c)),
                   **{f"p_{k}": float(r.get(k, float("nan"))) for k in ("ir_train", "ir_valid", "dann_train", "dann_valid")})
        return out


def _same(a, b):
    return a.keys() == b.keys() and all(a[k] == b[k] or (a[k] != a[k] and b[k] != b[k]) for k in a)


@pytest.mark.parametrize("kind", REWARDS)
def test_the_registered_scorer_scores_and_records_exactly_what_mains_inline_one_did(kind):
    alpha, liq, tgt, frozen, pool = _world(3)
    D = tgt.shape[0]
    cut = 180
    known = dg._zrank(np.random.default_rng(9).normal(size=tgt.shape))            # NOT ctx.base: --screen-base pool
    ctx = RewardContext(tgt, slice(0, cut), slice(cut, D), untradable=frozen, liq=liq, pool=pool, base=pool, halflives=(0.0, 5, 20))
    dates = [f"{20200101 + i}" for i in range(D)]
    ac_plugin.set_scorer_state(ctx, kind, dates[cut], known=known)
    new = ac_plugin._partura_scorer_factory(tgt, dates=dates, warmup=0, min_coverage=0.5, min_scored_days=0.5)
    old = MainScorer(tgt, ctx, kind, known, cut, min_coverage=0.5, min_scored_days=0.5)
    assert tuple(ac_plugin.ParturaScorer.columns) == MainScorer.columns
    rng = np.random.default_rng(1)
    panels = [alpha, -alpha, alpha + 0.5 * rng.normal(size=alpha.shape), rng.normal(size=alpha.shape),
              np.where(rng.random(alpha.shape) < 0.7, np.nan, alpha),               # mostly missing: the coverage gate
              np.round(alpha * 2) / 2,                                              # few distinct values: the p_dist gate
              np.ones_like(alpha)]                                                   # constant
    for p in panels:
        for gated in (True, False):
            assert _same(new.score(p, gated=gated), old.score(p, gated=gated)), (kind, gated)
    assert (new.n, new.gate) == (old.n, old.gate)
    assert new.n == 2 * len(panels)


def test_p_rho_known_is_measured_against_the_known_family_not_the_screen_base():
    """The earlier plugin API read ``ctx.base``; with ``--screen-base pool`` that is another plane."""
    alpha, liq, tgt, frozen, pool = _world(5)
    cut = 180
    known = dg._zrank(np.random.default_rng(2).normal(size=tgt.shape))
    ctx = RewardContext(tgt, slice(0, cut), slice(cut, tgt.shape[0]), untradable=frozen, liq=liq, pool=pool, base=pool, halflives=(0.0,))
    dates = [f"{20200101 + i}" for i in range(tgt.shape[0])]
    out = {}
    for label, k in (("known", known), ("default", None)):
        ac_plugin.set_scorer_state(ctx, "long", dates[cut], known=k)
        out[label] = ac_plugin._partura_scorer_factory(tgt, dates=dates, warmup=0, min_coverage=0.0, min_scored_days=0.0).score(alpha)["p_rho_known"]
    assert out["known"] != out["default"] and np.isfinite(out["known"]) and np.isfinite(out["default"])


# ----------------------------------------------------------------------------------- what main's script offers
def _script_tree():
    return ast.parse(SCRIPT.read_text(encoding="utf-8"))


def test_the_script_keeps_every_option_and_evidence_key_of_main():
    tree = _script_tree()
    opts = {c.args[0].value for c in ast.walk(tree) if isinstance(c, ast.Call) and isinstance(c.func, ast.Name) and c.func.id == "opt"
            and c.args and isinstance(c.args[0], ast.Constant)}
    assert opts >= {"--guidance", "--budget", "--population", "--arms", "--seed", "--boost", "--tag", "--reward", "--parts",
                    "--halflives", "--threshold", "--screen-base"}

    def keys_of(dict_node):
        return {k.value for k in dict_node.keys if isinstance(k, ast.Constant)}

    header = next(n.value for n in ast.walk(tree) if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "evidence" for t in n.targets))
    assert keys_of(header) >= {"idea", "reward", "threshold", "screen_base", "score_scale", "code", "reward_device", "budget", "population",
                               "seed", "boost", "period", "guidance", "parts", "halflives", "arms"}
    arm_dict = next(n.value for n in ast.walk(tree) if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Subscript)
                    and isinstance(n.value, ast.Dict) and "passers" in keys_of(n.value))
    assert keys_of(arm_dict) >= {"error", "checkpoints", "seconds", "scored", "gate_fail", "scoring_seconds", "archive", "live", "passers",
                                 "sampling", "candidates"}
    src = SCRIPT.read_text(encoding="utf-8")
    for counter in ("proposed", "accepted", "thinned", "banned", "sibling", "equivalent", "mutation_refused", "outside", "unread"):
        assert f'stats["{counter}"] += 1' in src, counter
    for token in ("independent_distinct", "efficiency_per_100", "rho_pool", "rho_known_traded", "heads", "is_discovery", "PARTURA_REWARD_DEVICE",
                  "DISCOVERY_MIN_PERIOD", "shutil.rmtree(ep_dir / arm", "family_first", "G.family_weight", "G.dedup_key", "G.family_key"):
        assert token in src, token
    # the candidate record the evidence carries
    cand = next(n.value for n in ast.walk(tree) if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "cand" for t in n.targets))
    cand_keys = keys_of(cand.elt)
    assert cand_keys >= {"expr", "fit", "score", "s_train", "s_valid", "share", "train", "valid", "train_ann", "valid_ann", "hl", "sign",
                         "turnover", "rho_known"}


def test_the_script_wires_mains_guidance_stream_and_the_arguments_the_plugin_needs():
    """What the extracted filter functions cannot show: how the script seeds the guidance's stream, and that it hands
    the plugin everything ``main``'s version captured in closures."""
    tree = _script_tree()
    want = ast.dump(ast.parse("(SEED * 2654435761) & 0xFFFFFFFF", mode="eval").body)
    made = [c for c in ast.walk(tree) if isinstance(c, ast.Call) and ast.unparse(c.func) == "random.Random"]
    assert len(made) == 1 and ast.dump(made[0].args[0]) == want                    # hook_rng = random.Random(<main's seed>)
    reseeds = [c for c in ast.walk(tree) if isinstance(c, ast.Call) and ast.unparse(c.func) == "hook_rng.seed"]
    assert len(reseeds) == 1 and ast.dump(reseeds[0].args[0]) == want              # ... reseeded at the start of every arm
    (state,) = [c for c in ast.walk(tree) if isinstance(c, ast.Call) and ast.unparse(c.func) == "ac_plugin.set_scorer_state"]
    assert [ast.unparse(a) for a in state.args] == ["ctx", "KIND", "SPLIT"] and {k.arg: ast.unparse(k.value) for k in state.keywords} == {"known": "known_z"}
    (arm_call,) = [c for c in ast.walk(tree) if isinstance(c, ast.Call) and ast.unparse(c.func) == "ac_plugin.arm_hooks"]
    assert {k.arg: ast.unparse(k.value) for k in arm_call.keywords} == {
        "parts": "PARTS", "risky": "risky", "ext": "EXT", "opw": "OPW", "idea_ops": "IDEA_OPS", "boost": "BOOST",
        "accept": "guidance_accept", "nt_twins": "'nt_twins' in FIXES"}
    src = SCRIPT.read_text(encoding="utf-8")
    assert 'fitness_kind="partura"' in src and "hooks=ac_plugin.search_hooks()" in src
    assert 'if arm == "steer" and seeds and "seeds" in PARTS:' in src                  # seeds are the steer arm's, and only with the part
    assert "ac_plugin.set_search_hooks(None)" in src                                   # nothing of an arm's opinion outlives it


def test_hood_and_priors_are_a_property_of_the_arm_not_of_a_global():
    """``--parts none`` has to make the steer arm the control to the last draw: no weights of its own, no accept."""
    risky, ext = {"x"}, frozenset()
    steer = ac_plugin.arm_hooks("steer", parts=(), risky=risky, ext=ext, opw={"a": 0.0}, idea_ops={"b"}, boost=9.0, accept=lambda t: True)
    control = ac_plugin.arm_hooks("control", risky=risky, ext=ext)

    class S:
        def __init__(self, name):
            self.name, self.resource_risk = name, name == "x"
    for n in ("a", "b", "x", "c"):
        assert steer.op_weight(S(n)) == control.op_weight(S(n))
    assert steer.accept is None and control.accept is None
    with pytest.raises(ValueError):
        ac_plugin.arm_hooks("steer", parts=("seeds", "typo"))


# ------------------------------------------------------------------------------------------- the opt-in switches
def test_fixes_are_off_by_default_and_read_from_the_environment(monkeypatch):
    ac_plugin.set_fixes(None)
    monkeypatch.delenv("PARTURA_AC_FIXES", raising=False)
    assert ac_plugin.fixes() == frozenset()
    monkeypatch.setenv("PARTURA_AC_FIXES", "in_sustain, nt_twins")
    assert ac_plugin.fixes() == {"in_sustain", "nt_twins"}
    ac_plugin.set_fixes(["nt_twins"])                       # an explicit call wins over the environment
    try:
        assert ac_plugin.fixes() == {"nt_twins"}
    finally:
        ac_plugin.set_fixes(None)
    monkeypatch.setenv("PARTURA_AC_FIXES", "in_sustian")
    with pytest.raises(ValueError):
        ac_plugin.fixes()


def test_register_declares_in_sustain_only_with_the_fix(monkeypatch):
    monkeypatch.delenv("PARTURA_AC_FIXES", raising=False)
    ac_plugin.set_fixes(None)
    names = set(ac_plugin._AC_REAL_VALUED)
    catalog.REAL_VALUED_OVERRIDES.difference_update(names)
    ac_plugin.register()
    assert not (names & catalog.REAL_VALUED_OVERRIDES)
    monkeypatch.setenv("PARTURA_AC_FIXES", "in_sustain")
    try:
        ac_plugin.register()
        assert names <= catalog.REAL_VALUED_OVERRIDES
    finally:
        catalog.REAL_VALUED_OVERRIDES.difference_update(names)
        catalog._DEFAULT = None
