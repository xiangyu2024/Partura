"""Derive the experiment plan FROM the expression.

A factor study is not a template to fill in.  The questions worth asking about
``cross_max(mul(cross_max(day_cov(Amt,Low),9), pow_3(dw(Open))),5)`` are not
the questions worth asking about the next tree, because they follow from which
nodes that tree has and what those nodes measurably do.  So the plan is
generated here, from the parsed tree plus the probe signatures of the
operators in it, and then CURATED BY THE AGENT: this module proposes, it does
not decide.

Five families of candidate, all derived structurally:

* **ablate**     -- delete a node (splice its operand through).  Does it carry anything?
* **isolate**    -- run a subtree as a factor on its own.  Where does the signal live?
* **substitute** -- swap an operator for a registry sibling that differs in
  exactly ONE measured property (``cross_max`` -> ``cross_mean`` differs in
  ``sign_sensitivity`` and ``monotone_in_window``; -> ``cross_med`` differs in
  fewer).  This is the part that cannot be written in advance: the neighbours
  are chosen by running the probes, so a tree made of operators nobody has
  looked at still gets a sensible list.
* **window**     -- neighbouring windows for every rolling node, from the
  registry's own window pool.  A real effect has a neighbourhood.
* **field**      -- swap a leaf for a field of the same kind.
* plus targeted **rankify / magnitude / interaction** candidates that only
  appear when the probes say they are relevant (a node with homogeneity
  degree != 0 gets a scale-free counterpart; an extremum over a sign-carrying
  operand gets an ``abs_`` test; a binary elementwise node gets its branches
  measured alone, added instead of multiplied, and rank-normalised).

Nothing here decides what matters.  The output is a draft YAML the agent edits:
delete what is uninformative, add what only a human reading of THIS tree
suggests, and write the `why` for each survivor.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Dict, List, Optional, Sequence, Tuple

from .bridge import ensure_alphacube_on_path
from . import probes as P

ensure_alphacube_on_path()

from alphacube.catalog import default_registry  # noqa: E402
from alphacube.expression import (Constant, Expression, Feature, GeneralCall, ShapeError,  # noqa: E402
                                  is_valid_root, make_node, replace)
from alphacube.parser import ParseError, parse  # noqa: E402

# Field kinds are a heuristic starting point, not a fact about the data: the
# agent should check them against the store (in the production cube Amt and
# Volume are raw while the price fields are back-adjusted, so they are not
# interchangeable in every context).
FIELD_KINDS: Dict[str, str] = {
    "Open": "price", "High": "price", "Low": "price", "Close": "price", "Vwap": "price",
    "Amt": "flow", "Volume": "flow", "Ret": "return",
}

SIGNATURE_KEYS = ("shift_invariant", "homogeneity_degree", "sign_sensitivity",
                  "order_dependent_on_minutes", "monotone_in_window", "rank_preserving",
                  "causal_on_day_axis")

_SIG_CACHE: Dict[Tuple[str, Optional[int]], Dict[str, object]] = {}


@dataclass
class Candidate:
    id: str
    expr: str
    kind: str
    node: str
    why: str


def signature(name: str, window: Optional[int] = None) -> Dict[str, object]:
    key = (name, window)
    if key not in _SIG_CACHE:
        spec = default_registry().get(name)
        res = P.run_probes(spec, window=window, only=SIGNATURE_KEYS)
        _SIG_CACHE[key] = {k: v.get("value") for k, v in res.items() if v.get("applicable")}
    return _SIG_CACHE[key]


def siblings(spec) -> List[str]:
    """Operators the grammar could put in the same slot."""
    reg = default_registry()
    return [n for n, s in reg._ops.items()
            if n != spec.name and s.face == spec.face and s.family == spec.family
            and s.category == spec.category and s.arity == spec.arity
            and s.requires_window == spec.requires_window
            and not (s.lookahead or s.trivial_boolean or s.resource_risk or s.coarse_output)]


def neighbours(spec, window: Optional[int], n: int = 4) -> List[Tuple[str, List[str]]]:
    """Siblings ranked by how FEW measured properties they differ in, so a
    substitution changes one thing at a time."""
    base = signature(spec.name, window)
    scored = []
    for cand in siblings(spec):
        try:
            sig = signature(cand, window)
        except Exception:
            continue
        diff = [k for k in base if k in sig and sig[k] != base[k]]
        if not diff:                       # measurably identical: nothing to learn
            continue
        scored.append((len(diff), cand, diff))
    scored.sort(key=lambda t: (t[0], t[1]))
    return [(c, d) for _, c, d in scored[:n]]


def scale_free_siblings(spec, window: Optional[int], n: int = 2) -> List[str]:
    """Siblings whose homogeneity degree is 0 -- the scale-contamination test
    for THIS node, found by measurement rather than by remembering that
    covariance has a correlation twin."""
    base = signature(spec.name, window)
    if base.get("homogeneity_degree") in (None, 0.0):
        return []
    scored = []
    for cand in siblings(spec):
        try:
            sig = signature(cand, window)
        except Exception:
            continue
        if sig.get("homogeneity_degree") != 0.0:
            continue
        # Prefer a twin that changes ONLY the scale behaviour: cross_argmax is
        # also degree 0, but it is a position index, not a scale-free version of
        # a maximum, and its other probe values say so.
        other = sum(1 for k in base if k != "homogeneity_degree" and k in sig and sig[k] != base[k])
        scored.append((other, cand))
    scored.sort()
    return [c for _, c in scored[:n]]


def _sub(root: Expression, node: Expression, new: Expression) -> Optional[str]:
    try:
        out = replace(root, node, new)
    except (ShapeError, TypeError, ValueError):
        return None
    return repr(out) if is_valid_root(out) else None


def _retyped(spec_name: str, node: Expression) -> Optional[Expression]:
    try:
        return make_node(default_registry().get(spec_name), node.operands, node.window, strict=False)
    except (ShapeError, TypeError, ValueError, KeyError):
        return None


def _label(node: Expression, var_of: Dict[str, str]) -> str:
    return var_of.get(node.key(), node.name)


def propose(src: str, *, n_minutes: int = 241, max_substitutes: int = 3,
            max_fields: int = 3, max_nodes: int = 14) -> List[Candidate]:
    from .decompose import decompose
    from .panels import parse_research
    root = parse_research(src, n_minutes=n_minutes)
    dec = decompose(src, n_minutes=n_minutes)
    var_of = dec.var_of_key()

    out: List[Candidate] = []
    base_key = root.key()

    def add(cid: str, expr: Optional[str], kind: str, node: str, why: str):
        if expr and expr != src:
            try:
                if parse_research(expr, n_minutes=n_minutes).key() == base_key:
                    return                              # a rewrite of the same tree
            except (ParseError, ValueError, TypeError):
                return
            if all(c.expr != expr for c in out):
                out.append(Candidate(id=cid, expr=expr, kind=kind, node=node, why=why))

    # Unique internal nodes, outermost first.  A hand-written factor can have 90
    # nodes; proposing around every one of them is noise, so only the nodes
    # nearest the root get the full treatment and the rest are left to whoever
    # reads the tree (the shared sub-trees are listed by `decompose`).
    seen, nodes = set(), []
    frontier = [root]
    while frontier:
        nxt = []
        for n in frontier:
            if n.spec is None or n.key() in seen:
                continue
            seen.add(n.key())
            nodes.append(n)
            nxt.extend(n.operands)
        frontier = nxt
    deep = nodes[max_nodes:]
    nodes = nodes[:max_nodes]

    for node in nodes:
        v = _label(node, var_of)
        spec = node.spec
        general = isinstance(node, GeneralCall)

        # ---- isolate: is the signal already here?
        if is_valid_root(node) and node is not root:
            add(f"iso_{v}", repr(node), "isolate", v,
                f"单独跑 {v} = {spec.name}(...):预测力是不是已经在这一层")

        # ---- ablate: splice the first tensor operand through
        if node is not root and node.operands:
            child = node.operands[0]
            if not isinstance(child, Constant):
                add(f"abl_{v}", _sub(root, node, child), "ablate", v,
                    f"删掉 {v} = {spec.name},其余不变:这个节点贡献了什么")
        if general:
            continue                                   # no registry siblings for a call with literals

        try:
            sig = signature(spec.name, node.window)
        except Exception:
            continue

        # ---- substitute: siblings that differ in exactly one measured property
        for cand, diff in neighbours(spec, node.window, max_substitutes):
            new = _retyped(cand, node)
            if new is None:
                continue
            add(f"sub_{v}_{cand}", _sub(root, node, new), "substitute", v,
                f"{spec.name} → {cand}:实测只差 {', '.join(diff)}")

        # ---- scale-free counterpart, only where the node carries scale
        for cand in scale_free_siblings(spec, node.window):
            new = _retyped(cand, node)
            if new is None:
                continue
            add(f"nosc_{v}_{cand}", _sub(root, node, new), "substitute", v,
                f"{spec.name}(齐次度 {sig.get('homogeneity_degree')}) → {cand}(齐次度 0):"
                f"尺度是不是必需的")

        # ---- window neighbourhood
        if node.window is not None:
            pool = sorted(set(spec.windows) | {node.window})
            i = pool.index(node.window)
            for w in sorted({pool[max(0, i - 1)], pool[min(len(pool) - 1, i + 1)],
                             pool[max(0, i - 2)], pool[min(len(pool) - 1, i + 2)]} - {node.window}):
                try:
                    new = make_node(spec, node.operands, w, strict=False)
                except (ShapeError, TypeError, ValueError):
                    continue
                add(f"win_{v}_{w}", _sub(root, node, new), "window", v,
                    f"{v} 的窗口 {node.window} → {w}:真效应应该有邻域")

        # ---- magnitude: an extremum over an operand that carries sign
        if sig.get("monotone_in_window") == "non_decreasing" and node.operands:
            child = node.operands[0]
            try:
                child_sign = signature(child.spec.name, child.window).get("sign_sensitivity") \
                    if child.spec is not None and not isinstance(child, GeneralCall) else None
            except Exception:
                child_sign = None
            if child_sign == "odd":
                try:
                    absed = make_node(default_registry().get("abs_"), (child,), None, strict=False)
                    add(f"mag_{v}", _sub(root, child, absed), "magnitude", v,
                        f"在 {v} 的操作数外面套 abs_:取极值是不是只是在取幅度")
                except (ShapeError, KeyError, TypeError, ValueError):
                    pass

        # ---- interaction: a binary elementwise node is a claim about a mechanism
        if spec.category == "binary" and spec.compute_axis is None and len(node.operands) == 2:
            a, b = node.operands
            for side, sub in (("左", a), ("右", b)):
                if is_valid_root(sub):
                    add(f"only_{v}_{'L' if side == '左' else 'R'}", _sub(root, node, sub),
                        "interaction", v, f"只留 {v} 的{side}支:这次组合是不是真的带来了东西")
            alt = {"mul": "add", "add": "mul", "div": "sub", "sub": "div"}.get(spec.name)
            if alt:
                new = _retyped(alt, node)
                add(f"alt_{v}_{alt}", _sub(root, node, new) if new is not None else None, "interaction", v,
                    f"{spec.name} → {alt}:交互形式换一种,预测力变不变")
            if a.shape.daily and b.shape.daily:
                try:
                    rk = default_registry().get("cs_rank")
                    ra = make_node(rk, (a,), None, strict=False)
                    rb = make_node(rk, (b,), None, strict=False)
                    add(f"rank_{v}", _sub(root, node, make_node(spec, (ra, rb), None, strict=False)),
                        "interaction", v, f"{v} 的两支先各自截面排名再 {spec.name}:抹掉尺度后交互还在不在")
                except (ShapeError, KeyError, TypeError, ValueError):
                    pass

    if deep:
        out.append(Candidate(id="_note_deep", expr=src, kind="note", node="",
                             why=f"还有 {len(deep)} 个更深的节点没有自动提议(树太大);"
                                 f"它们要靠读 decompose 里被重复使用的中间量来决定动哪一个"))

    # ---- field swaps
    fields = [n for n in root.nodes() if isinstance(n, Feature)]
    reg_fields = list(default_registry().fields)
    for f in {n.field for n in fields}:
        kind = FIELD_KINDS.get(f)
        alts = [g for g in reg_fields if g != f and FIELD_KINDS.get(g) == kind][:max_fields]
        for g in alts:
            node = next(n for n in fields if n.field == f)
            add(f"fld_{f}_{g}", _sub(root, node, Feature(g)), "field", f,
                f"字段 {f} → {g}(同为 {kind}):这条 alpha 依不依赖这个字段的身份")
    return out


def to_yaml(src: str, factor_id: str, cands: Sequence[Candidate], title: str = "") -> str:
    """A draft config.  Everything in it is a PROPOSAL -- prune it, reorder it,
    and write a real `why` before running anything."""
    kinds = ["isolate", "ablate", "substitute", "window", "magnitude", "interaction", "field"]
    head = [f"factor_id: {factor_id}",
            f'title: "{title or "(填一句这棵树是什么)"}"',
            f'expression: "{src}"',
            "",
            "label: {kind: open_vwap15, horizon: 1}",
            "cost_per_side: 0.0015",
            "turnover_cap: 0.30",
            "top_frac: 0.10",
            "horizons: [1, 2, 3, 5, 10, 20]",
            "warmup: 60",
            "",
            "# 控制变量按这棵树的嫌疑来挑,不要照抄别的因子的清单。",
            "controls: {}",
            "gates: {}",
            "diagnostics: {}",
            "",
            "# ↓↓↓ 以下全部是 propose 生成的**候选**,不是计划。删掉没有信息量的,",
            "#     补上只有读了这棵树才想得到的,并把 why 写成一句可证伪的话。",
            "stages:"]
    body: List[str] = []
    for c in cands:
        if c.kind == "note":
            head.insert(-1, f"# 注意: {c.why}")
    for k in kinds:
        group = [c for c in cands if c.kind == k]
        if not group:
            continue
        body.append(f"  - id: S_{k}")
        body.append(f'    question: "(这一组在回答什么问题?)"')
        body.append("    variants:")
        for c in group:
            body.append(f'      - {{id: {c.id}, group: {c.kind}, expr: "{c.expr}", why: "{c.why}"}}')
    return "\n".join(head + body) + "\n"


__all__ = ["Candidate", "propose", "to_yaml", "signature", "neighbours", "scale_free_siblings",
           "siblings", "FIELD_KINDS", "SIGNATURE_KEYS"]
