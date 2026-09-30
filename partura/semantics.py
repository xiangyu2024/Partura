"""Operator dossiers: what an AlphaCube operator ACTUALLY does.

Rule of the house (inherited from AlphaCube): never infer an operator's
meaning from its name.  A dossier therefore has two halves:

1. **Declared** -- what the registry says (face, family, compute axis, arity,
   window requirement, the flags the catalog's own probes set) plus the real
   source file, line and body of the kernel.
2. **Measured** -- what the kernel does to tensors, established here by
   running it:

   * ``causal``            does an output row depend on later input rows?
   * ``order_dependence``  does permuting the reduced axis change the output?
     (a path statistic vs a distributional one)
   * ``shift``             is f(x + c) = f(x)?  (location invariance)
   * ``homogeneity``       fitted k in f(c*x) = c^k f(x)  (scale exposure)
   * ``rank_preserving``   does f keep the order of its input?
   * ``nan``               what a partially / fully missing input produces

The scale and shift probes are the ones that decide contamination
hypotheses: an operator with homogeneity degree 1 in ``Amt`` carries the
liquidity level into the factor whether or not anybody intended it.
"""

from __future__ import annotations

import inspect
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Sequence, Tuple

from .bridge import ensure_alphacube_on_path

ensure_alphacube_on_path()

import numpy as np  # noqa: E402
import torch  # noqa: E402

from alphacube.catalog import default_registry  # noqa: E402

_TOL = 1e-4


def _finite_close(a: torch.Tensor, b: torch.Tensor, tol: float = _TOL) -> bool:
    a, b = a.double(), b.double()
    m = torch.isfinite(a) & torch.isfinite(b)
    if m.sum() == 0:
        return bool((torch.isnan(a) == torch.isnan(b)).all())
    scale = torch.maximum(a[m].abs(), b[m].abs()).clamp(min=1.0)
    return bool(((a[m] - b[m]).abs() / scale).max() < tol)


def _call(spec, args: Sequence[torch.Tensor], window: Optional[int]):
    if spec.requires_window:
        return spec.fn(*args, window)
    return spec.fn(*args)


def _sample(shape: Tuple[int, int], seed: int, positive: bool) -> torch.Tensor:
    g = torch.Generator().manual_seed(seed)
    x = torch.randn(shape, generator=g, dtype=torch.float64)
    return x.abs() + 1.0 if positive else x


@dataclass
class Dossier:
    name: str
    declared: Dict[str, object] = field(default_factory=dict)
    measured: Dict[str, object] = field(default_factory=dict)
    source_file: str = ""
    source_line: int = 0
    doc: str = ""
    source: str = ""

    def to_dict(self) -> Dict[str, object]:
        return {"name": self.name, "declared": self.declared, "measured": self.measured,
                "source_file": self.source_file, "source_line": self.source_line, "doc": self.doc}


def _probe_causal(spec, window: Optional[int], shape: Tuple[int, int]) -> Optional[bool]:
    """Perturb the second half of the DAY axis; if any earlier output row moves,
    the operator reads the future.  Only meaningful for day-axis operators."""
    if spec.compute_axis != "D":
        return None
    D = shape[0]
    cut = D // 2
    xs = [_sample(shape, 11 + i, positive=True) for i in range(spec.arity)]
    base = _call(spec, xs, window)
    pert = [x.clone() for x in xs]
    for p in pert:
        p[cut:] += 7.0
    out = _call(spec, pert, window)
    return _finite_close(base[:cut], out[:cut])


def _probe_order(spec, window: Optional[int], shape: Tuple[int, int]) -> Optional[bool]:
    """Permute the minute axis (jointly for pair operators).  True = the output
    depends on the ORDER of the row, i.e. it is a path statistic."""
    if not (spec.face == "dt" and spec.family in ("day", "in")):
        return None
    xs = [_sample(shape, 21 + i, positive=True) for i in range(spec.arity)]
    base = _call(spec, xs, window)
    g = torch.Generator().manual_seed(7)
    perm = torch.randperm(shape[1], generator=g)
    out = _call(spec, [x[:, perm] for x in xs], window)
    return not _finite_close(base, out)


def _probe_shift(spec, window: Optional[int], shape: Tuple[int, int]) -> Optional[bool]:
    """True = f(x + c) == f(x) for every operand (location invariant)."""
    xs = [_sample(shape, 31 + i, positive=True) for i in range(spec.arity)]
    base = _call(spec, xs, window)
    out = _call(spec, [x + 3.0 for x in xs], window)
    return _finite_close(base, out)


def _probe_homogeneity(spec, window: Optional[int], shape: Tuple[int, int]) -> Optional[float]:
    """Fit k in f(c*x) = c^k * f(x) over c in {2, 4, 8}; None if no single k fits."""
    xs = [_sample(shape, 41 + i, positive=True) for i in range(spec.arity)]
    base = _call(spec, xs, window).double()
    m = torch.isfinite(base) & (base.abs() > 1e-12)
    if m.sum() < 10:
        return None
    ks: List[float] = []
    for c in (2.0, 4.0, 8.0):
        out = _call(spec, [x * c for x in xs], window).double()
        mm = m & torch.isfinite(out) & (out.abs() > 1e-12)
        if mm.sum() < 10:
            return None
        k = (torch.log(out[mm].abs()) - torch.log(base[mm].abs())) / np.log(c)
        if float(k.std()) > 1e-3:
            return None
        ks.append(float(k.mean()))
    return round(float(np.mean(ks)), 4) if max(ks) - min(ks) < 1e-3 else None


def _probe_rank_preserving(spec, window: Optional[int]) -> Optional[bool]:
    """Elementwise only: does f keep the order of its input?"""
    if spec.category != "unary" or spec.compute_axis is not None:
        return None
    x = torch.linspace(-5, 5, 401, dtype=torch.float64).reshape(1, -1)
    try:
        y = spec.fn(x)
    except Exception:
        return None
    y = y.flatten()
    fin = torch.isfinite(y)
    return bool((y[fin][1:] - y[fin][:-1] >= -1e-12).all())


def _probe_nan(spec, window: Optional[int], shape: Tuple[int, int]) -> Dict[str, object]:
    xs = [_sample(shape, 51 + i, positive=True) for i in range(spec.arity)]
    g = torch.Generator().manual_seed(3)
    holes = torch.rand(shape, generator=g) < 0.1
    part = [torch.where(holes, torch.full_like(x, float("nan")), x) for x in xs]
    out_part = _call(spec, part, window)
    dead = [torch.full(shape, float("nan"), dtype=torch.float64) for _ in xs]
    out_dead = _call(spec, dead, window)
    return {"finite_frac_with_10pct_missing": round(float(torch.isfinite(out_part).double().mean()), 4),
            "all_nan_input_gives_all_nan": bool(torch.isnan(out_dead).all())}


def dossier(name: str, window: Optional[int] = None, shape: Tuple[int, int] = (40, 24)) -> Dossier:
    spec = default_registry().get(name)
    w = window if window is not None else (spec.windows[0] if spec.requires_window and spec.windows else 5)
    w = w if spec.requires_window else None
    fn = inspect.unwrap(spec.fn)
    try:
        src_file, src_line = inspect.getsourcefile(fn) or "", inspect.getsourcelines(fn)[1]
        src = inspect.getsource(fn)
    except (OSError, TypeError):
        src_file, src_line, src = "", 0, ""
    d = Dossier(
        name=name,
        declared={
            "face": spec.face, "family": spec.family, "category": spec.category, "arity": spec.arity,
            "requires_window": spec.requires_window, "compute_axis": spec.compute_axis,
            "reduces_m": spec.reduces_m, "restores_m": spec.restores_m, "kernel_id": spec.kernel_id,
            "lookahead_flag": spec.lookahead, "boolean_output": spec.boolean_output,
            "trivial_boolean": spec.trivial_boolean, "resource_risk": spec.resource_risk,
            "coarse_output": spec.coarse_output, "windows": list(spec.windows),
        },
        source_file=src_file, source_line=src_line,
        doc=inspect.getdoc(fn) or "", source=src,
    )
    probes: Dict[str, object] = {"probe_window": w, "probe_shape": list(shape)}
    for key, f in (("causal_on_day_axis", lambda: _probe_causal(spec, w, shape)),
                   ("order_dependent_on_minutes", lambda: _probe_order(spec, w, shape)),
                   ("shift_invariant", lambda: _probe_shift(spec, w, shape)),
                   ("homogeneity_degree", lambda: _probe_homogeneity(spec, w, shape)),
                   ("rank_preserving", lambda: _probe_rank_preserving(spec, w)),
                   ("nan", lambda: _probe_nan(spec, w, shape))):
        try:
            probes[key] = f()
        except Exception as exc:                       # a probe that cannot run says so; it never guesses
            probes[key] = f"probe failed: {type(exc).__name__}: {exc}"
    d.measured = probes
    return d


def dossiers_for(expr) -> Dict[str, Dossier]:
    """Every operator used in a parsed expression, with the window it is used at."""
    out: Dict[str, Dossier] = {}
    for n in expr.nodes():
        if n.spec is None or n.spec.name in out:
            continue
        out[n.spec.name] = dossier(n.spec.name, window=n.window)
    return out


def render_markdown(ds: Dict[str, Dossier]) -> str:
    lines: List[str] = []
    for name, d in ds.items():
        dc, mc = d.declared, d.measured
        loc = f"{d.source_file.split('alphacube/')[-1]}:{d.source_line}" if d.source_file else "?"
        lines.append(f"### `{name}`\n")
        lines.append(f"- **实现**: `{loc}` (kernel `{dc['kernel_id']}`)")
        lines.append(f"- **声明**: face `{dc['face']}` / family `{dc['family']}` / category `{dc['category']}`, "
                     f"arity {dc['arity']}, 计算轴 `{dc['compute_axis']}`, "
                     f"{'需要窗口' if dc['requires_window'] else '无窗口'}"
                     f"{', 折叠分钟轴 (M→1)' if dc['reduces_m'] else ''}")
        flags = [k for k in ("lookahead_flag", "boolean_output", "trivial_boolean", "resource_risk",
                             "coarse_output") if dc.get(k)]
        lines.append(f"- **标志**: {', '.join(flags) if flags else '无'}")
        probe_bits = []
        if mc.get("causal_on_day_axis") is not None:
            probe_bits.append(f"日轴因果性 = {mc['causal_on_day_axis']}")
        if mc.get("order_dependent_on_minutes") is not None:
            probe_bits.append(f"分钟顺序依赖 = {mc['order_dependent_on_minutes']}")
        probe_bits.append(f"平移不变 = {mc.get('shift_invariant')}")
        probe_bits.append(f"齐次度 k = {mc.get('homogeneity_degree')}")
        if mc.get("rank_preserving") is not None:
            probe_bits.append(f"保序 = {mc['rank_preserving']}")
        nan = mc.get("nan") or {}
        if isinstance(nan, dict):
            probe_bits.append(f"10% 缺失后有限值占比 = {nan.get('finite_frac_with_10pct_missing')}")
        lines.append(f"- **实测探针**: {'; '.join(probe_bits)}")
        if d.doc:
            lines.append(f"- **docstring**: {d.doc.splitlines()[0]}")
        lines.append("")
    return "\n".join(lines)


__all__ = ["Dossier", "dossier", "dossiers_for", "render_markdown"]
