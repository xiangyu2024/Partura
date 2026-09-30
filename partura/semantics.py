"""Operator dossiers: what an AlphaCube operator ACTUALLY does.

A dossier has two halves:

1. **Declared** -- what the registry says (face, family, compute axis, arity,
   window, the flags the catalog's own probes set) plus the real source file,
   line and body of the kernel.
2. **Measured** -- the output of every probe in ``partura.probes`` that
   declares itself applicable to this operator, INCLUDING any probe the
   current study added for this expression.

Which probes are worth running is a property of the expression under study,
not of Partura, so this module never hardcodes a probe list: it asks the
registry.  A study that needs a question the built-ins do not ask writes it in
``studies/<factor_id>/probes.py`` and it appears here automatically, tagged
with the file it came from.
"""

from __future__ import annotations

import inspect
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Sequence, Tuple

from .bridge import ensure_alphacube_on_path
from . import probes as P

ensure_alphacube_on_path()

from alphacube.catalog import default_registry  # noqa: E402


@dataclass
class Dossier:
    name: str
    declared: Dict[str, object] = field(default_factory=dict)
    probes: Dict[str, dict] = field(default_factory=dict)      # full records incl. skipped
    source_file: str = ""
    source_line: int = 0
    doc: str = ""
    source: str = ""

    @property
    def measured(self) -> Dict[str, object]:
        return P.values(self.probes)

    def to_dict(self) -> Dict[str, object]:
        return {"name": self.name, "declared": self.declared, "probes": self.probes,
                "source_file": self.source_file, "source_line": self.source_line, "doc": self.doc}


def dossier(name: str, window: Optional[int] = None, shape: Tuple[int, int] = (40, 24),
            only: Optional[Sequence[str]] = None) -> Dossier:
    spec = default_registry().get(name)
    fn = inspect.unwrap(spec.fn)
    try:
        src_file, src_line = inspect.getsourcefile(fn) or "", inspect.getsourcelines(fn)[1]
        src = inspect.getsource(fn)
    except (OSError, TypeError):
        src_file, src_line, src = "", 0, ""
    return Dossier(
        name=name,
        declared={
            "face": spec.face, "family": spec.family, "category": spec.category, "arity": spec.arity,
            "requires_window": spec.requires_window, "compute_axis": spec.compute_axis,
            "reduces_m": spec.reduces_m, "restores_m": spec.restores_m, "kernel_id": spec.kernel_id,
            "lookahead_flag": spec.lookahead, "boolean_output": spec.boolean_output,
            "trivial_boolean": spec.trivial_boolean, "resource_risk": spec.resource_risk,
            "coarse_output": spec.coarse_output, "windows": list(spec.windows),
            "window_probed": window,
        },
        probes=P.run_probes(spec, window=window, shape=shape, only=only),
        source_file=src_file, source_line=src_line, doc=inspect.getdoc(fn) or "", source=src,
    )


def dossiers_for(expr, **kw) -> Dict[str, Dossier]:
    """Every operator used in a parsed expression, probed at the window it is
    used at (a rolling operator behaves differently at 3 days and at 60)."""
    out: Dict[str, Dossier] = {}
    for n in expr.nodes():
        if n.spec is None or n.spec.name in out:
            continue
        out[n.spec.name] = dossier(n.spec.name, window=n.window, **kw)
    return out


_LABELS = {
    "causal_on_day_axis": "日轴因果性",
    "order_dependent_on_minutes": "分钟顺序依赖",
    "shift_invariant": "平移不变",
    "homogeneity_degree": "齐次度 k",
    "rank_preserving": "保序",
    "sign_sensitivity": "取负后",
    "monotone_in_window": "窗口变长",
    "effective_memory": "脉冲记忆天数",
}


def render_markdown(ds: Dict[str, Dossier], show_questions: bool = False) -> str:
    lines: List[str] = []
    study_probes = sorted({r["origin"] for d in ds.values() for r in d.probes.values()
                           if r.get("origin", "builtin") != "builtin"})
    for name, d in ds.items():
        dc = d.declared
        loc = f"{d.source_file.split('alphacube/')[-1]}:{d.source_line}" if d.source_file else "?"
        lines.append(f"### `{name}`\n")
        lines.append(f"- **实现**: `{loc}` (kernel `{dc['kernel_id']}`)")
        w = dc.get("window_probed")
        lines.append(f"- **声明**: face `{dc['face']}` / family `{dc['family']}` / category `{dc['category']}`, "
                     f"arity {dc['arity']}, 计算轴 `{dc['compute_axis']}`, "
                     f"{f'窗口 {w}' if dc['requires_window'] else '无窗口'}"
                     f"{', 折叠分钟轴 (M→1)' if dc['reduces_m'] else ''}")
        flags = [k for k in ("lookahead_flag", "boolean_output", "trivial_boolean", "resource_risk",
                             "coarse_output") if dc.get(k)]
        lines.append(f"- **标志**: {', '.join(flags) if flags else '无'}")
        bits, extra = [], []
        for k, rec in d.probes.items():
            if not rec.get("applicable") or "value" not in rec:
                continue
            label = _LABELS.get(k, k)
            v = rec["value"]
            if isinstance(v, dict):
                v = ", ".join(f"{a}={b}" for a, b in v.items())
            item = f"{label} = {v}"
            (extra if rec.get("origin", "builtin") != "builtin" else bits).append(item)
        lines.append(f"- **实测探针**: {'; '.join(bits) if bits else '(无适用探针)'}")
        if extra:
            lines.append(f"- **本研究新增的探针**: {'; '.join(extra)}")
        skipped = [k for k, r in d.probes.items() if not r.get("applicable")]
        if skipped:
            lines.append(f"- <sub>不适用的探针: {', '.join(skipped)}</sub>")
        failed = {k: r["error"] for k, r in d.probes.items() if "error" in r}
        if failed:
            lines.append(f"- **探针报错**: {failed}")
        if d.doc:
            lines.append(f"- **docstring**: {d.doc.splitlines()[0]}")
        lines.append("")
    if show_questions:
        lines += ["<details><summary>每个探针在问什么</summary>", ""]
        seen = {}
        for d in ds.values():
            for k, r in d.probes.items():
                seen.setdefault(k, (r.get("question", ""), r.get("origin", "builtin")))
        for k, (q, origin) in sorted(seen.items()):
            tag = "" if origin == "builtin" else f"  _(本研究新增,来自 `{origin.split('/')[-1]}`)_"
            lines.append(f"- `{k}` — {q}{tag}")
        lines += ["", "</details>", ""]
    if study_probes:
        lines.append(f"> 本研究额外加载了探针文件:{', '.join(f'`{s}`' for s in study_probes)}")
        lines.append("")
    return "\n".join(lines)


__all__ = ["Dossier", "dossier", "dossiers_for", "render_markdown"]
