"""Expression -> readable computational tree, with per-node measured facts.

The output is SSA-style: every internal node becomes a named intermediate
(A, B, C, ...) so the expression can be read as a short program instead of a
nest of parentheses.  Each step carries what the registry declares about its
operator and what the probes in ``semantics`` measured, plus a structural role
tag used to summarise the factor's "grammar" (event -> memory -> gate ->
amplification -> persistence).

Role tags are derived from measured properties, never from operator names.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .bridge import ensure_alphacube_on_path
from .semantics import Dossier, dossier

ensure_alphacube_on_path()

from alphacube.expression import Expression, Feature, Constant, max_window  # noqa: E402
from alphacube.parser import parse  # noqa: E402

_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


@dataclass
class Step:
    var: str
    op: str
    window: Optional[int]
    args: List[str]
    expr: str                 # full sub-expression text
    inline: str               # this step written in terms of earlier vars
    axis: str                 # which axis the operator computes over
    shape: str
    role: str
    notes: List[str] = field(default_factory=list)


@dataclass
class Decomposition:
    expression: str
    steps: List[Step]
    dossiers: Dict[str, Dossier]
    fields: List[str]
    depth: int
    n_nodes: int
    max_day_window: int
    path_day_lookback: int

    def grammar(self) -> List[str]:
        return [f"{s.var}: {s.role}" for s in self.steps]

    def render_markdown(self) -> str:
        lines = ["```", *(f"{s.var} = {s.inline}" for s in self.steps), "```", "",
                 "| 变量 | 算子 | 计算轴 | 窗口 | 输出形状 | 结构角色 |", "|---|---|---|---|---|---|"]
        for s in self.steps:
            lines.append(f"| `{s.var}` | `{s.op}` | {s.axis} | {s.window if s.window else '—'} "
                         f"| {s.shape} | {s.role} |")
        lines += ["", f"- 节点数 {self.n_nodes}(含叶子),深度 {self.depth},用到的字段:"
                      f" {', '.join(self.fields)}",
                  f"- 日轴最大单窗口 {self.max_day_window} 天;**沿路径累计的真实回看 {self.path_day_lookback} 天**"
                  f"(AlphaCube 的 `max_window` 取最大值而不是路径累加,预热行数按它算)"]
        return "\n".join(lines)


def _axis_label(d: Optional[Dossier]) -> str:
    if d is None:
        return "—"
    ax = d.declared.get("compute_axis")
    if ax == "M":
        return "日内分钟轴 (M)"
    if ax == "D":
        return "交易日轴 (D)"
    if ax == "S":
        return "截面 (S)"
    return "逐元素"


def _shape_label(e: Expression) -> str:
    s = e.shape
    if s.width == 1 or s.collapsed:
        return "每股票-日一个值"
    if s.degenerate:
        return "日频值铺满分钟轴"
    return "每股票-日-分钟一个值"


def _role(e: Expression, d: Optional[Dossier]) -> str:
    if d is None:
        return "字段/常数"
    dc, mc = d.declared, d.measured
    hom = mc.get("homogeneity_degree")
    if dc.get("reduces_m"):
        path = mc.get("order_dependent_on_minutes")
        kind = "日内路径统计量" if path else "日内分布统计量"
        scale = "尺度不变" if hom == 0 else (f"齐次度 {hom}" if hom is not None else "尺度行为未定")
        return f"日内事件提取({kind},{scale})"
    if dc.get("compute_axis") == "D" and e.window:
        return f"{e.window} 日记忆(日轴滚动,因果={mc.get('causal_on_day_axis')})"
    if dc.get("category") == "binary" and dc.get("compute_axis") is None:
        return "两路信号交互(乘性:可能是调制/门控)"
    if dc.get("category") == "unary" and dc.get("compute_axis") is None:
        mono = mc.get("rank_preserving")
        return f"非线性放大(保序={mono},齐次度 {hom})"
    if dc.get("compute_axis") == "S":
        return "截面变换"
    return "变换"


def _path_lookback(e: Expression) -> int:
    """Real day-axis lookback: rolling windows COMPOSE along a path
    (cross_max(cross_max(x, 9), 5) sees 13 days), which is what a warm-up
    length should be built from."""
    if isinstance(e, (Feature, Constant)):
        return 1
    child = max((_path_lookback(c) for c in e.operands), default=1)
    w = e.window if (e.spec is not None and e.spec.compute_axis == "D" and e.window) else 1
    return child + w - 1


def decompose(src: str, n_minutes: int = 241) -> Decomposition:
    root = parse(src, strict=False, coerce_daily=True, n_minutes=n_minutes, allow_general=True)
    steps: List[Step] = []
    dossiers: Dict[str, Dossier] = {}
    var_of: Dict[str, str] = {}
    fields: List[str] = []

    def visit(e: Expression) -> str:
        if isinstance(e, Feature):
            if e.field not in fields:
                fields.append(e.field)
            return e.field
        if isinstance(e, Constant):
            return repr(e)
        key = e.key()
        if key in var_of:
            return var_of[key]
        arg_vars = [visit(c) for c in e.operands]
        name = e.spec.name if e.spec is not None else type(e).__name__
        if name not in dossiers:
            dossiers[name] = dossier(name, window=e.window)
        d = dossiers[name]
        var = _LETTERS[len(steps)] if len(steps) < len(_LETTERS) else f"V{len(steps)}"
        inline_args = list(arg_vars) + ([str(e.window)] if e.window is not None else [])
        steps.append(Step(var=var, op=name, window=e.window, args=arg_vars, expr=repr(e),
                          inline=f"{name}({', '.join(inline_args)})",
                          axis=_axis_label(d), shape=_shape_label(e), role=_role(e, d)))
        var_of[key] = var
        return var

    visit(root)
    return Decomposition(expression=repr(root), steps=steps, dossiers=dossiers, fields=fields,
                         depth=root.depth(), n_nodes=len(root.nodes()),
                         max_day_window=max_window(root, "D"), path_day_lookback=_path_lookback(root))


__all__ = ["Step", "Decomposition", "decompose"]
