"""Expression -> readable computational tree, with per-node measured facts.

The output is SSA-style: every internal node becomes a named intermediate
(A, B, C, ...) so the expression can be read as a short program instead of a
nest of parentheses.  Shared sub-trees get ONE name -- a hand-written factor
that repeats ``sub(in_slice(Volume, 2, 237), in_delay(...))`` four times reads
as one definition used four times, which is usually the first thing one needs
to see about it.

Each step carries what the registry declares about its operator and what the
probes in ``partura.probes`` measured, plus a structural role tag.  Role tags
are derived from measured properties, never from operator names.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .bridge import ensure_alphacube_on_path
from .semantics import Dossier, dossier_for_node, usage_name

ensure_alphacube_on_path()

from alphacube.expression import Constant, Expression, Feature, GeneralCall, max_window  # noqa: E402

_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def _var(i: int) -> str:
    return _LETTERS[i] if i < len(_LETTERS) else f"{_LETTERS[i // 26 - 1]}{_LETTERS[i % 26]}"


@dataclass
class Step:
    var: str
    op: str                   # usage name (general calls keep their literals)
    window: Optional[int]
    args: List[str]
    expr: str                 # full sub-expression text
    inline: str               # this step written in terms of earlier vars
    axis: str
    shape: str
    role: str
    uses: int = 1             # how many times the tree reads this intermediate
    key: str = ""
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

    def var_of_key(self) -> Dict[str, str]:
        return {s.key: s.var for s in self.steps}

    def grammar(self) -> List[str]:
        return [f"{s.var}: {s.role}" for s in self.steps]

    def render_markdown(self) -> str:
        lines = ["```", *(f"{s.var} = {s.inline}" for s in self.steps), "```", "",
                 "| 变量 | 算子 | 计算轴 | 窗口 | 输出形状 | 被引用 | 结构角色 |", "|---|---|---|---|---|---|---|"]
        for s in self.steps:
            lines.append(f"| `{s.var}` | `{s.op}` | {s.axis} | {s.window if s.window else '—'} "
                         f"| {s.shape} | {s.uses}× | {s.role} |")
        shared = [s for s in self.steps if s.uses > 1]
        lines += ["", f"- 节点数 {self.n_nodes}(含叶子),去重后 {len(self.steps)} 个中间量,深度 {self.depth},"
                      f"用到的字段: {', '.join(self.fields)}",
                  f"- 日轴最大单窗口 {self.max_day_window} 天;**沿路径累计的真实回看 {self.path_day_lookback} 天**"
                  f"(AlphaCube 的 `max_window` 取最大值而不是路径累加,预热行数按它算)"]
        if shared:
            lines.append(f"- 被重复使用的中间量:{', '.join(f'`{s.var}`×{s.uses}' for s in shared)}"
                         f" —— 整棵树其实是围绕它们写的")
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
    if s.width:
        return f"每股票-日 {s.width} 个分钟"
    return "每股票-日-分钟一个值"


def _role(e: Expression, d: Optional[Dossier]) -> str:
    if d is None:
        return "字段/常数"
    dc, mc = d.declared, d.measured
    hom = mc.get("homogeneity_degree")
    face, fam = dc.get("face"), dc.get("family")
    if dc.get("boolean_output") or e.spec.name in ("is_gt", "is_lt", "eq", "greater", "less"):
        return "事件判定(0/1 掩码)"
    if dc.get("reduces_m"):
        path = mc.get("order_dependent_on_minutes")
        kind = "日内路径统计量" if path else ("日内分布统计量" if path is False else "日内折叠")
        scale = "尺度不变" if hom == 0 else (f"齐次度 {hom}" if hom is not None else "尺度行为未定")
        return f"日内事件提取({kind},{scale})"
    if face == "nt":
        return "逐分钟的截面/日轴变换(NT 面:每分钟跨股票或跨日)"
    if face == "dt" and fam == "in":
        return "日内分钟轴上的变换(仍是分钟级)"
    if dc.get("compute_axis") == "D" and e.window:
        return f"{e.window} 日记忆(日轴滚动,因果={mc.get('causal_on_day_axis')})"
    if dc.get("compute_axis") == "S":
        return "截面变换(当天所有股票之间)"
    if len(e.operands) >= 2 and dc.get("compute_axis") is None:
        return "多路信号逐元素组合"
    if len(e.operands) == 1 and dc.get("compute_axis") is None:
        mono = mc.get("rank_preserving")
        return f"逐元素变换(保序={mono},齐次度 {hom})"
    return "变换"


def _path_lookback(e: Expression) -> int:
    """Real day-axis lookback: rolling windows COMPOSE along a path
    (cross_max(cross_max(x, 9), 5) sees 13 days)."""
    if isinstance(e, (Feature, Constant)):
        return 1
    child = max((_path_lookback(c) for c in e.operands), default=1)
    w = e.window if (e.spec is not None and e.spec.compute_axis == "D" and e.window) else 1
    return child + w - 1


def decompose(src: str, n_minutes: int = 241) -> Decomposition:
    from .panels import parse_research
    root = parse_research(src, n_minutes=n_minutes)
    steps: List[Step] = []
    dossiers: Dict[str, Dossier] = {}
    var_of: Dict[str, str] = {}
    by_key: Dict[str, Step] = {}
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
            by_key[key].uses += 1
            return var_of[key]
        if isinstance(e, GeneralCall):
            rendered, arg_vars = [], []
            for a in e.args:
                if isinstance(a, tuple):
                    vs = [visit(x) for x in a]
                    arg_vars += vs
                    rendered.append("[" + ", ".join(vs) + "]")
                elif isinstance(a, Expression):
                    v = visit(a)
                    arg_vars.append(v)
                    rendered.append(v)
                else:
                    rendered.append(repr(a))
            inline = f"{e.spec.name}({', '.join(rendered)})"
        else:
            arg_vars = [visit(c) for c in e.operands]
            inline_args = list(arg_vars) + ([str(e.window)] if e.window is not None else [])
            inline = f"{e.spec.name}({', '.join(inline_args)})"
        uname = usage_name(e)
        if uname not in dossiers:
            try:
                dossiers[uname] = dossier_for_node(e)
            except Exception as exc:
                dossiers[uname] = Dossier(name=uname, declared={
                    "face": e.spec.face, "family": e.spec.family, "category": e.spec.category,
                    "arity": len(e.operands), "requires_window": e.spec.requires_window,
                    "compute_axis": e.spec.compute_axis, "reduces_m": e.spec.reduces_m,
                    "kernel_id": e.spec.kernel_id, "window_probed": e.window},
                    probes={"_dossier": {"applicable": True, "error": f"{type(exc).__name__}: {exc}",
                                         "question": "", "origin": "builtin"}})
        d = dossiers[uname]
        st = Step(var=_var(len(steps)), op=uname, window=e.window, args=arg_vars, expr=repr(e),
                  inline=inline, axis=_axis_label(d), shape=_shape_label(e), role=_role(e, d), key=key)
        steps.append(st)
        var_of[key] = st.var
        by_key[key] = st
        return st.var

    visit(root)
    return Decomposition(expression=repr(root), steps=steps, dossiers=dossiers, fields=fields,
                         depth=root.depth(), n_nodes=len(root.nodes()),
                         max_day_window=max_window(root, "D"), path_day_lookback=_path_lookback(root))


__all__ = ["Step", "Decomposition", "decompose"]
