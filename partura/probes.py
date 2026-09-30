"""An extensible registry of operator probes.

The point of a probe is to answer ONE question about a kernel by running it,
because the name of an operator is not evidence.  Which questions are worth
asking depends entirely on the expression being studied:

* ``day_durbin_watson`` needed a *location-invariance* probe, because the
  answer (it divides by sum-of-squares, not by the variance) is what turns it
  from "an autocorrelation test" into "realized variance".
* An operator with a hard threshold needs a probe that finds the knot.
* A rank-based operator needs a probe for invariance to monotone maps.
* A two-window operator needs a probe for which window actually moves it.

So this module ships a small set of *generally useful* probes and makes it
cheap to add study-specific ones: write a function in
``studies/<factor_id>/probes.py``, decorate it, and it runs alongside the
built-ins for the operators it declares itself applicable to.  A probe that
does not apply says so instead of returning a misleading value, and a probe
that cannot run reports the exception rather than guessing.

    @probe("knot", question="Where does the output jump?",
           applies=lambda s: s.category == "unary" and s.compute_axis is None)
    def _knot(ctx):
        x = torch.linspace(-5, 5, 2001, dtype=torch.float64).reshape(1, -1)
        y = ctx.call([x])
        return float(x.flatten()[y.flatten().diff().abs().argmax()])
"""

from __future__ import annotations

import importlib.util
import inspect
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Dict, List, Optional, Sequence, Tuple

from .bridge import ensure_alphacube_on_path

ensure_alphacube_on_path()

import numpy as np  # noqa: E402
import torch  # noqa: E402

TOL = 1e-4


# ---------------------------------------------------------------- context
@dataclass
class ProbeContext:
    """What a probe gets to work with: the kernel, how to call it, and helpers
    that keep every probe's numerical conventions the same."""

    spec: object                      # alphacube.axes.OpSpec
    window: Optional[int]
    shape: Tuple[int, int]            # the (rows, cols) 2-D view the face sees

    def call(self, args: Sequence[torch.Tensor], window: Optional[int] = None) -> torch.Tensor:
        w = self.window if window is None else window
        if self.spec.requires_window:
            return self.spec.fn(*args, w)
        return self.spec.fn(*args)

    def sample(self, seed: int = 0, positive: bool = True,
               shape: Optional[Tuple[int, int]] = None) -> torch.Tensor:
        g = torch.Generator().manual_seed(seed)
        x = torch.randn(shape or self.shape, generator=g, dtype=torch.float64)
        return x.abs() + 1.0 if positive else x

    def operands(self, seed: int = 0, positive: bool = True) -> List[torch.Tensor]:
        return [self.sample(seed + i, positive) for i in range(self.spec.arity)]

    @staticmethod
    def close(a: torch.Tensor, b: torch.Tensor, tol: float = TOL) -> bool:
        a, b = a.double(), b.double()
        m = torch.isfinite(a) & torch.isfinite(b)
        if m.sum() == 0:
            return bool((torch.isnan(a) == torch.isnan(b)).all())
        scale = torch.maximum(a[m].abs(), b[m].abs()).clamp(min=1.0)
        return bool(((a[m] - b[m]).abs() / scale).max() < tol)

    @staticmethod
    def spearman(a: torch.Tensor, b: torch.Tensor) -> float:
        """Rank correlation over the cells finite in both -- the right measure
        whenever the question is "same ordering?" rather than "same value?"."""
        a, b = a.flatten().double(), b.flatten().double()
        m = torch.isfinite(a) & torch.isfinite(b)
        if m.sum() < 3:
            return float("nan")
        ra = torch.argsort(torch.argsort(a[m], stable=True)).double()
        rb = torch.argsort(torch.argsort(b[m], stable=True)).double()
        ra, rb = ra - ra.mean(), rb - rb.mean()
        d = (ra.norm() * rb.norm())
        return float((ra @ rb / d)) if d > 0 else float("nan")


# ---------------------------------------------------------------- registry
@dataclass
class Probe:
    name: str
    question: str
    fn: Callable[[ProbeContext], object]
    applies: Callable[[object], bool]
    origin: str = "builtin"

    def source(self) -> str:
        try:
            return inspect.getsource(self.fn)
        except (OSError, TypeError):
            return ""


PROBES: Dict[str, Probe] = {}


def probe(name: str, *, question: str, applies: Callable[[object], bool] = lambda s: True,
          origin: str = "builtin"):
    def deco(fn):
        PROBES[name] = Probe(name=name, question=question, fn=fn, applies=applies, origin=origin)
        return fn
    return deco


def load_study_probes(path) -> List[str]:
    """Import a study's own probes.  Anything it registers is marked with the
    file it came from, so the report can show that this study asked a question
    the built-ins do not ask."""
    p = Path(path)
    if not p.is_file():
        return []
    # Identity, not membership: loading the same file twice re-runs the
    # decorator and installs FRESH Probe objects whose origin defaults to
    # "builtin", so a name-based diff silently mislabels them on the second
    # load (and the report then hides that the study added a question).
    before = {n: id(pr) for n, pr in PROBES.items()}
    spec = importlib.util.spec_from_file_location(f"partura_study_probes_{p.stem}", p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    added = [n for n, pr in PROBES.items() if before.get(n) != id(pr)]
    for n in added:
        PROBES[n].origin = str(p)
    return added


def run_probes(spec, window: Optional[int] = None, shape: Tuple[int, int] = (40, 24),
               only: Optional[Sequence[str]] = None) -> Dict[str, dict]:
    """Every applicable probe, plus a record of which ones were skipped and why."""
    w = window if window is not None else (spec.windows[0] if spec.requires_window and spec.windows else 5)
    ctx = ProbeContext(spec=spec, window=w if spec.requires_window else None, shape=shape)
    out: Dict[str, dict] = {}
    for name, pr in PROBES.items():
        if only is not None and name not in only:
            continue
        try:
            ok = bool(pr.applies(spec))
        except Exception:
            ok = False
        if not ok:
            out[name] = {"applicable": False, "question": pr.question, "origin": pr.origin}
            continue
        try:
            val = pr.fn(ctx)
            out[name] = {"applicable": True, "value": val, "question": pr.question, "origin": pr.origin}
        except Exception as exc:
            out[name] = {"applicable": True, "error": f"{type(exc).__name__}: {exc}",
                         "question": pr.question, "origin": pr.origin}
    return out


def values(results: Dict[str, dict]) -> Dict[str, object]:
    """Flatten to name -> value for the probes that ran."""
    return {k: v["value"] for k, v in results.items() if v.get("applicable") and "value" in v}


# ---------------------------------------------------------------- applicability helpers
def is_day_reducer(s) -> bool:            # (.., M) -> (.., 1)
    return bool(getattr(s, "reduces_m", False))


def rolls_days(s) -> bool:                # window along the trading-day axis
    return s.compute_axis == "D"


def is_elementwise(s) -> bool:
    return s.compute_axis is None and s.face == "shared"


def reads_minutes(s) -> bool:
    return s.face == "dt" and s.family in ("day", "in")


def is_cross_sectional(s) -> bool:
    return s.compute_axis == "S"


# ---------------------------------------------------------------- built-in probes
@probe("causal_on_day_axis", question="输出的某一行会不会被后面的行改变?(读未来)", applies=rolls_days)
def _causal(ctx: ProbeContext):
    D = ctx.shape[0]
    cut = D // 2
    xs = ctx.operands(11)
    base = ctx.call(xs)
    pert = [x.clone() for x in xs]
    for p in pert:
        p[cut:] += 7.0
    return ctx.close(base[:cut], ctx.call(pert)[:cut])


@probe("order_dependent_on_minutes", question="打乱分钟顺序会不会改变输出?(路径统计量 vs 分布统计量)",
       applies=reads_minutes)
def _order(ctx: ProbeContext):
    xs = ctx.operands(21)
    base = ctx.call(xs)
    g = torch.Generator().manual_seed(7)
    perm = torch.randperm(ctx.shape[1], generator=g)
    return not ctx.close(base, ctx.call([x[:, perm] for x in xs]))


@probe("shift_invariant", question="f(x + c) 是否等于 f(x)?(是否只看相对位置)")
def _shift(ctx: ProbeContext):
    xs = ctx.operands(31)
    return ctx.close(ctx.call(xs), ctx.call([x + 3.0 for x in xs]))


@probe("homogeneity_degree", question="f(c·x) = c^k·f(x) 里的 k 是多少?(带不带尺度)")
def _homogeneity(ctx: ProbeContext):
    xs = ctx.operands(41)
    base = ctx.call(xs).double()
    m = torch.isfinite(base) & (base.abs() > 1e-12)
    if m.sum() < 10:
        return None
    ks = []
    for c in (2.0, 4.0, 8.0):
        out = ctx.call([x * c for x in xs]).double()
        mm = m & torch.isfinite(out) & (out.abs() > 1e-12)
        if mm.sum() < 10:
            return None
        k = (torch.log(out[mm].abs()) - torch.log(base[mm].abs())) / np.log(c)
        if float(k.std()) > 1e-3:
            return None
        ks.append(float(k.mean()))
    return round(float(np.mean(ks)), 4) if max(ks) - min(ks) < 1e-3 else None


@probe("rank_preserving", question="f 会不会改变输入的顺序?(保序的外层变换对排名型指标无效)",
       applies=lambda s: s.category == "unary" and s.compute_axis is None)
def _rank_preserving(ctx: ProbeContext):
    x = torch.linspace(-5, 5, 401, dtype=torch.float64).reshape(1, -1)
    y = ctx.call([x]).flatten()
    fin = torch.isfinite(y)
    return bool((y[fin][1:] - y[fin][:-1] >= -1e-12).all())


@probe("nan_behaviour", question="10% 缺失下还剩多少有限值?整行缺失会怎样?")
def _nan(ctx: ProbeContext):
    xs = ctx.operands(51)
    g = torch.Generator().manual_seed(3)
    holes = torch.rand(ctx.shape, generator=g) < 0.1
    part = [torch.where(holes, torch.full_like(x, float("nan")), x) for x in xs]
    dead = [torch.full(ctx.shape, float("nan"), dtype=torch.float64) for _ in xs]
    return {"finite_frac_with_10pct_missing": round(float(torch.isfinite(ctx.call(part)).double().mean()), 4),
            "all_nan_input_gives_all_nan": bool(torch.isnan(ctx.call(dead)).all())}


@probe("sign_sensitivity", question="把输入整体取负,输出是跟着变号、不变,还是别的?")
def _sign(ctx: ProbeContext):
    xs = ctx.operands(61, positive=False)
    base = ctx.call(xs)
    flip = ctx.call([-x for x in xs])
    if ctx.close(base, flip):
        return "even"            # |x|-like: sign is discarded
    if ctx.close(-base, flip):
        return "odd"             # sign carried through
    return "neither"


@probe("monotone_in_window", question="窗口变长时输出怎么动?(极值型单调,均值型不单调)",
       applies=lambda s: s.requires_window and s.compute_axis == "D")
def _window_monotone(ctx: ProbeContext):
    xs = ctx.operands(71)
    outs = [ctx.call(xs, window=w).double() for w in (3, 6, 12)]
    m = torch.isfinite(outs[0]) & torch.isfinite(outs[1]) & torch.isfinite(outs[2])
    if m.sum() < 10:
        return None
    up = bool(((outs[1][m] >= outs[0][m] - 1e-9) & (outs[2][m] >= outs[1][m] - 1e-9)).all())
    dn = bool(((outs[1][m] <= outs[0][m] + 1e-9) & (outs[2][m] <= outs[1][m] + 1e-9)).all())
    return "non_decreasing" if up else ("non_increasing" if dn else "neither")


@probe("effective_memory", question="脉冲输入之后,输出还在多少天里记得它?",
       applies=lambda s: s.requires_window and s.compute_axis == "D" and s.arity == 1)
def _memory(ctx: ProbeContext):
    D = ctx.shape[0]
    x = torch.full((D, ctx.shape[1]), 1.0, dtype=torch.float64)
    base = ctx.call([x]).double()
    x2 = x.clone()
    x2[D // 3] += 50.0
    out = ctx.call([x2]).double()
    diff = (out - base).abs().max(dim=1).values
    hit = torch.nonzero(diff > 1e-9).flatten()
    return int(hit.numel())


__all__ = ["Probe", "ProbeContext", "PROBES", "probe", "run_probes", "values", "load_study_probes",
           "is_day_reducer", "rolls_days", "is_elementwise", "reads_minutes", "is_cross_sectional"]
