"""Steering the search: Partura's conclusions as interventions on AlphaCube.

Partura is not downstream of AlphaCube.  AlphaCube does the high-entropy empirical discovery; Partura studies
what was found (and what failed), forms beliefs, and turns them back into the search: a different reward, a
different way of evaluating a candidate, a different probability for an action or a sub-structure, and ideas
that are handed to the search as a neighbourhood to brute-force for a short while.  This module is that
return path.  A guidance file (``guidance/<batch>.yaml``) holds the interventions with their evidence; here are

* the expression patterns the rules are written in, and a matcher over expression STRINGS (so a rule can be
  applied to anything that prints an expression: a GP archive, an RL trajectory, a sweep table);
* ``Guidance``: canonical form (rewrites that are equivalent under the selection convention), a de-duplication
  key, the weight of an expression (product of the matching rules; a ban is 0) and a deterministic
  accept / reject that turns a proposal distribution P into P x weight -- usable as a filter in front of ANY
  generator, whether or not the generator exposes operator probabilities;
* the rewards of the guidance, as functions of a raw (days, stocks) panel -- the long-leg conventions of
  ``partura.books`` plus the three changes the batch argued for (tradable universe, within-liquidity-bucket,
  marginal over the known pool), direction chosen by the long leg, half-life by the long book, and the worse of
  train / valid as the score.

Pattern syntax -- an expression, with
    _            any sub-tree              _1 _2 ...   any sub-tree, the same one wherever the name repeats
    $w           any number                {a|b|c}     any of these operator / leaf names
    @price @flow @any                      a leaf of that kind
    root: ...                              match the whole expression only (default: anywhere in the tree)
"""

from __future__ import annotations

import hashlib
import math
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterator, List, Optional, Sequence, Tuple

LEAF_KINDS = {"@price": ("Close", "Open", "High", "Low", "Vwap"), "@flow": ("Amt", "Volume"),
              "@any": ("Close", "Open", "High", "Low", "Vwap", "Amt", "Volume", "Ret")}
POWERS = {"sqrt": 0.5, "pow_05": 0.5, "pow_1_5": 1.5, "pow_2": 2.0, "pow_2_5": 2.5, "pow_3": 3.0}


# ------------------------------------------------------------------ trees over strings
@dataclass(frozen=True)
class Node:
    name: str                                  # operator / leaf name, or the literal text of a number
    args: Optional[Tuple["Node", ...]] = None  # None = leaf or number

    @property
    def is_number(self) -> bool:
        return self.args is None and bool(re.fullmatch(r"[-+]?(\d+\.?\d*|\.\d+)([eE][-+]?\d+)?", self.name))

    def __str__(self) -> str:
        return self.name if self.args is None else f"{self.name}({', '.join(map(str, self.args))})"


_TOKEN = re.compile(r"\s*([A-Za-z_@$][A-Za-z_0-9]*|\{[^{}]*\}|[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?|[(),])")


def parse_expr(src: str) -> Node:
    """``name(arg, ...)`` / leaf / number -> Node.  Raises ValueError on anything else."""
    toks = _TOKEN.findall(src)
    if "".join(toks) != re.sub(r"\s+", "", src):
        raise ValueError(f"cannot tokenise: {src[:80]}")
    pos = 0

    def node() -> Node:
        nonlocal pos
        if pos >= len(toks) or toks[pos] in "(),":
            raise ValueError(f"unexpected token at {pos} in {src[:80]}")
        name = toks[pos]
        pos += 1
        if pos < len(toks) and toks[pos] == "(":
            pos += 1
            args: List[Node] = []
            if toks[pos] == ")":
                pos += 1
                return Node(name, ())
            while True:
                args.append(node())
                if pos >= len(toks):
                    raise ValueError(f"unbalanced: {src[:80]}")
                if toks[pos] == ",":
                    pos += 1
                    continue
                if toks[pos] == ")":
                    pos += 1
                    return Node(name, tuple(args))
                raise ValueError(f"unexpected {toks[pos]!r} in {src[:80]}")
        return Node(name)

    out = node()
    if pos != len(toks):
        raise ValueError(f"trailing tokens in {src[:80]}")
    return out


def walk(n: Node, depth: int = 0) -> Iterator[Tuple[Node, int]]:
    yield n, depth
    for a in n.args or ():
        yield from walk(a, depth + 1)


def operators(n: Node) -> List[str]:
    return [x.name for x, _ in walk(n) if x.args is not None]


def leaves(n: Node) -> List[str]:
    return [x.name for x, _ in walk(n) if x.args is None and not x.is_number]


# ------------------------------------------------------------------ patterns
@dataclass
class Pattern:
    text: str
    root: bool
    tree: Node

    @classmethod
    def compile(cls, text: str) -> "Pattern":
        t = text.strip()
        root = t.startswith("root:")
        return cls(text, root, parse_expr(t[5:].strip() if root else t))

    @staticmethod
    def _name_ok(pat: str, name: str) -> bool:
        if pat.startswith("{"):
            names: List[str] = []
            for x in pat[1:-1].split("|"):
                names.extend(LEAF_KINDS.get(x.strip(), (x.strip(),)))
            return name in names
        return pat == name

    def _match(self, p: Node, n: Node, binds: Dict[str, str]) -> bool:
        if p.args is None:                                   # a leaf of the pattern
            if p.name == "_":
                return True
            if re.fullmatch(r"_\d+", p.name):
                s = str(n)
                return binds.setdefault(p.name, s) == s
            if p.name == "$w":
                return n.is_number
            if p.name in LEAF_KINDS:
                return n.args is None and n.name in LEAF_KINDS[p.name]
            if p.name.startswith("{"):
                return n.args is None and self._name_ok(p.name, n.name)
            if p.is_number:
                return n.is_number and float(n.name) == float(p.name)
            return n.args is None and n.name == p.name
        if n.args is None or len(n.args) != len(p.args) or not self._name_ok(p.name, n.name):
            return False
        return all(self._match(a, b, binds) for a, b in zip(p.args, n.args))

    def find(self, n: Node) -> List[Tuple[Node, int]]:
        if self.root:
            return [(n, 0)] if self._match(self.tree, n, {}) else []
        return [(x, d) for x, d in walk(n) if self._match(self.tree, x, {})]

    def matches(self, n: Node) -> bool:
        return bool(self.find(n))


# Operators whose output is never negative, and operators that keep "never negative" when every tensor operand is.
# Used by the canonical form: abs_ of such a sub-tree is the sub-tree (a GP breeds these wrappers for free and each
# one costs an evaluation).  A name missing from the lists only means a rewrite is not made -- never a wrong one.
NONNEG_OPS = frozenset("""abs_ pow_2 sqrt sigmoid day_std day_var day_gini day_zero_ratio day_flat_ratio day_distinct_ratio
    day_at_max_ratio day_at_min_ratio day_flat_run_max day_pos_ratio day_wstd cross_stddev ts_stddev cross_valid_count cross_age
    cross_flat_ratio cross_semistd_neg cross_semistd_pos cs_rank in_stddev_rolling in_stddev_full nt_ts_std nt_ts_var""".split())
SIGN_KEEPING_OPS = frozenset("""cross_ema cross_mean cross_max cross_min cross_med cross_sum cross_decay_linear cross_fangzheng
    cross_tail_mean_q25 cross_tail_mean_q75 cross_quantile_q25 cross_quantile_q75 ts_mean ts_max ts_min ts_sum ts_med ts_decay_linear
    day_mean day_sum day_max day_min day_median day_quantile day_first day_last day_close day_open in_slice in_delay in_local_mean
    in_mean_full add mul div cs_winsor pow_05 pow_1_5 pow_2_5 pow_3 signedpower""".split())
IDEMPOTENT_OPS = frozenset("abs_ cs_demean cs_rank cs_winsor cs_normalize cs_robust_z neg_abs".split())


def nonneg(n: Node) -> bool:
    """True when the sub-tree can be shown never to be negative (conservative: False when unsure)."""
    if n.args is None:
        if n.is_number:
            return float(n.name) >= 0
        return n.name in LEAF_KINDS["@price"] or n.name in LEAF_KINDS["@flow"]
    if n.name in NONNEG_OPS:
        return True
    if n.name in SIGN_KEEPING_OPS:
        return all(nonneg(a) for a in n.args)
    return False


def simplify(n: Node) -> Node:
    """Rewrites that hold for every input: f(f(x)) = f(x) for idempotent f; abs_(x) = x when x is never negative."""
    if n.args is None:
        return n
    n = Node(n.name, tuple(simplify(a) for a in n.args))
    if len(n.args) == 1:
        a = n.args[0]
        if n.name in IDEMPOTENT_OPS and a.args is not None and a.name == n.name:
            return a
        if n.name == "abs_" and nonneg(a):
            return a
    return n


def nesting(n: Node, name: str) -> int:
    """Deepest chain of ``name`` nodes along one root-to-leaf path."""
    here = 1 if n.args is not None and n.name == name else 0
    return here + max((nesting(a, name) for a in n.args or ()), default=0)


# ------------------------------------------------------------------ guidance
@dataclass
class Rule:
    id: str
    action: str                       # ban | weight | rewrite | dedup_key
    pattern: Pattern
    w: float = 1.0
    to: str = ""
    unless: Optional[Pattern] = None
    depth_ge: int = 0
    why: str = ""
    evidence: Sequence[str] = field(default_factory=tuple)

    def hits(self, n: Node) -> bool:
        if not self.pattern.matches(n):
            return False
        if self.unless is not None and self.unless.matches(n):
            return False
        if self.depth_ge and nesting(n, self.pattern.tree.name) < self.depth_ge:
            return False
        return True


class Guidance:
    def __init__(self, spec: dict) -> None:
        self.spec = spec
        self.rules: List[Rule] = []
        for r in spec.get("priors", []):
            self.rules.append(Rule(r["id"], r["action"], Pattern.compile(r["pattern"]), float(r.get("w", 0.0 if r["action"] == "ban" else 1.0)),
                                   str(r.get("to", "")), Pattern.compile(r["unless"]) if r.get("unless") else None, int(r.get("depth_ge", 0)),
                                   r.get("why", ""), tuple(map(str, r.get("evidence", [])))))
        self.w_ref = max([1.0] + [r.w for r in self.rules if r.action == "weight"])

    @classmethod
    def load(cls, path) -> "Guidance":
        import yaml
        return cls(yaml.safe_load(Path(path).read_text(encoding="utf-8")))

    # -- rewrites: equivalent (or measured-equivalent) under the selection convention
    def _rewrite_once(self, n: Node) -> Node:
        if n.args is not None:
            n = Node(n.name, tuple(self._rewrite_once(a) for a in n.args))
        return n

    def _apply(self, rule: Rule, n: Node, top: bool) -> Node:
        if n.args is not None:
            n = Node(n.name, tuple(self._apply(rule, a, False) for a in n.args))
        if rule.pattern.root and not top:
            return n
        binds: Dict[str, str] = {}
        if not rule.pattern._match(rule.pattern.tree, n, binds):
            return n
        if rule.to == "operand":
            return n.args[0]
        if rule.to == "single_power":
            return n
        if rule.to:
            out = rule.to
            for k, v in binds.items():
                out = out.replace(k, v)
            return parse_expr(out)
        return n

    def canonical(self, expr: str) -> str:
        """The expression with every rewrite rule applied until nothing changes."""
        n = parse_expr(expr)
        for _ in range(8):
            before = str(n)
            n = simplify(n)
            for r in self.rules:
                if r.action == "rewrite":
                    n = self._apply(r, n, True)
            if str(n) == before:
                break
        return str(n)

    def dedup_key(self, expr: str) -> str:
        """Canonical form with every leaf family collapsed to its representative: two candidates with the same
        key are the same experiment and only one of them should be scored."""
        s = self.canonical(expr)
        for r in self.rules:
            if r.action == "dedup_key" and r.pattern.tree.name in LEAF_KINDS:
                s = re.sub(r"\b(" + "|".join(LEAF_KINDS[r.pattern.tree.name]) + r")\b", r.to, s)
        return re.sub(r"\s+", "", s)

    # -- weights
    def explain(self, expr: str) -> List[Rule]:
        n = parse_expr(self.canonical(expr))
        return [r for r in self.rules if r.action in ("ban", "weight") and r.hits(n)]

    def weight(self, expr: str) -> float:
        w = 1.0
        for r in self.explain(expr):
            w *= r.w
        return w

    def accept(self, expr: str, u: Optional[float] = None, salt: str = "") -> bool:
        """Accept / reject so that a generator with proposal P ends up sampling from P x weight (capped at
        w_ref): a banned expression never passes; any other passes with probability min(1, weight / w_ref).

        Inside a search pass ``u`` = a uniform draw from the SEARCH's own seeded generator: the thinning is then
        per draw (an expression rejected once can be proposed again and pass), and the run stays reproducible.
        Without ``u`` the decision is a hash of the canonical form -- for thinning a FIXED list of proposals,
        where the same list must always give the same subset."""
        w = self.weight(expr)
        if w <= 0:
            return False
        if u is None:
            u = int(hashlib.sha1((salt + self.dedup_key(expr)).encode()).hexdigest()[:12], 16) / float(16 ** 12)
        return u < min(1.0, w / self.w_ref)

    def banned(self, expr: str) -> bool:
        return self.weight(expr) <= 0

    def ban_patterns(self) -> List[str]:
        return [r.pattern.text for r in self.rules if r.action == "ban"]

    def operator_weights(self) -> Dict[str, float]:
        """A coarse per-operator multiplier for generators that only take one number per operator: the weight of
        every rule whose pattern is led by that operator at the root or anywhere.  Structure-specific rules lose
        their context here (that is what ``accept`` is for); this is the fallback, not the mechanism."""
        out: Dict[str, float] = {}
        for r in self.rules:
            if r.action not in ("ban", "weight"):
                continue
            head = r.pattern.tree.name
            names = [x.strip() for x in head[1:-1].split("|")] if head.startswith("{") else [head]
            generic = all(a.name in ("_", "$w") or re.fullmatch(r"_\d+", a.name or "") for a in r.pattern.tree.args or ())
            if not generic or r.unless is not None or r.depth_ge:
                continue
            for nm in names:
                out[nm] = out.get(nm, 1.0) * (r.w if r.action == "weight" else 0.0)
        return out


# ------------------------------------------------------------------ rewards
REWARDS = ("long", "long_tradable", "long_bucket", "long_marginal", "long_screen")


class RewardContext:
    """Everything a reward needs besides the candidate's panel -- built once per search.

    ``tgt`` (days, stocks) labels; ``train`` / ``valid`` slices; ``untradable`` boolean (days, stocks): names the
    reward should neither hold nor count in the benchmark (frozen quote in the last 15 days among the worst fifth,
    or listed too recently); ``liq`` (days, stocks) the liquidity key of the buckets; ``pool`` (days, stocks) the
    z-rank of the known pool's traded signal."""

    def __init__(self, tgt, train: slice, valid: slice, *, untradable=None, liq=None, pool=None, base=None,
                 halflives=(0.0, 2, 5, 10, 20)) -> None:
        self.tgt, self.train, self.valid = tgt, train, valid
        self.untradable, self.liq, self.pool = untradable, liq, pool
        self.base = base                       # z-rank of the signal a "screen" candidate is applied to (the known family, unscreened)
        self._base_rows = None
        self._pool_u = None
        self.halflives = tuple(halflives)
        self._bucket = None
        self._pool_rows = None

    def pool_in_universe(self):
        """The pool re-ranked INSIDE the reward's universe.  The candidate is scored with the untradable names
        removed; a pool left on the full universe keeps the excess it earns by avoiding them (they are in its
        benchmark), so 'blend minus pool' compared two different games and every candidate came out negative
        (episode e1, first run).  Both sides of the difference must live in the same universe."""
        if self._pool_u is None:
            import numpy as np
            from . import diagnose as dg
            p = self.pool if self.untradable is None else np.where(self.untradable, np.nan, self.pool)
            self._pool_u = dg._zrank(p)
        return self._pool_u

    def bucket(self, n: int = 10):
        if self._bucket is None:
            import numpy as np
            x = self.liq
            fin = np.isfinite(x)
            order = np.argsort(np.where(fin, x, np.inf), axis=1, kind="stable")
            pos = np.empty_like(order)
            np.put_along_axis(pos, order, np.arange(x.shape[1])[None, :].repeat(x.shape[0], 0), axis=1)
            cnt = fin.sum(1, keepdims=True)
            self._bucket = np.where(fin, np.minimum(np.floor(pos / np.maximum(cnt, 1) * n), n - 1), -1).astype(np.int8)
        return self._bucket


def _bucket_rank(sm, bucket, n: int = 10):
    """Rank inside each liquidity bucket, mapped to (0, 1]: the long book then holds the best of every bucket.
    One lexicographic sort per day (bucket first, value second) instead of one sort per bucket."""
    import numpy as np
    fin = np.isfinite(sm) & (bucket >= 0)
    b = np.where(fin, bucket, n).astype(np.int64)
    order = np.lexsort((np.where(fin, sm, np.inf), b), axis=1)
    pos = np.empty_like(order)
    np.put_along_axis(pos, order, np.arange(sm.shape[1])[None, :].repeat(sm.shape[0], 0), axis=1)
    cnt = np.stack([(b == k).sum(1) for k in range(n + 1)], axis=1)
    start = np.cumsum(cnt, axis=1) - cnt
    within = pos - np.take_along_axis(start, b, axis=1)
    return np.where(fin, (within + 1.0) / np.maximum(np.take_along_axis(cnt, b, axis=1), 1), np.nan)


def reward(panel, ctx: RewardContext, kind: str = "long", *, both_periods: bool = True) -> Dict[str, object]:
    """Score one raw (days, stocks) panel.

    For each direction and each half-life of the grid the signal is smoothed, transformed as the reward says,
    and its pure long book (top decile, equal weight, net of 15 bp, against the equal-weight of the names that
    have a signal and a label) is scored on the training period; the best (direction, half-life) BY THE LONG BOOK
    on train is kept.  ``score`` is the pure-long Sharpe -- the worse of train and valid when ``both_periods``.
    ``long_marginal`` scores the 50/50 blend with the pool minus the pool alone.  ``long_screen`` uses the
    candidate as a SCREEN: the base signal (the known family) with the candidate's top fifth sent to the bottom,
    minus the base alone -- the reward for an idea whose claim is "this marks the names not to hold"."""
    import numpy as np

    from . import books as bk
    from . import diagnose as dg

    raw = np.asarray(panel, dtype=np.float64)
    if ctx.untradable is not None and kind in ("long_tradable", "long_bucket", "long_marginal"):
        raw = np.where(ctx.untradable, np.nan, raw)
    best = None
    for hl in ctx.halflives:
        sm0 = bk.smoothed(raw, hl)                           # the EMA is linear: one pass serves both directions
        for sign in (1.0, -1.0):
            sm = sign * sm0
            if kind == "long_bucket":
                sm = _bucket_rank(sm, ctx.bucket())
            elif kind == "long_marginal":
                z, pu = dg._zrank(sm), ctx.pool_in_universe()
                sm = np.where(np.isfinite(z) & np.isfinite(pu), 0.5 * z + 0.5 * pu, np.nan)
            elif kind == "long_screen":
                z = dg._zrank(sm)                            # [-0.5, 0.5]; the top fifth of the candidate goes below everything
                sm = np.where(np.isfinite(ctx.base), np.where(np.isfinite(z) & (z > 0.3), -1.0 + 0.1 * ctx.base, ctx.base), np.nan)
            r = bk.book_row(sm, ctx.tgt, ctx.train)
            key = float(np.nan_to_num(r["long_sharpe"], nan=-9e9))
            if best is None or key > best[0]:
                best = (key, sign, float(hl), sm, r)
    _, sign, hl, sm, tr = best
    va = bk.book_row(sm, ctx.tgt, ctx.valid)
    base_tr = base_va = 0.0
    if kind == "long_marginal":
        if ctx._pool_rows is None:
            pu = ctx.pool_in_universe()
            ctx._pool_rows = (bk.book_row(pu, ctx.tgt, ctx.train), bk.book_row(pu, ctx.tgt, ctx.valid))
        base_tr, base_va = ctx._pool_rows[0]["long_sharpe"], ctx._pool_rows[1]["long_sharpe"]
    if kind == "long_screen":
        if ctx._base_rows is None:
            ctx._base_rows = (bk.book_row(ctx.base, ctx.tgt, ctx.train), bk.book_row(ctx.base, ctx.tgt, ctx.valid))
        base_tr, base_va = ctx._base_rows[0]["long_sharpe"], ctx._base_rows[1]["long_sharpe"]
    s_tr, s_va = tr["long_sharpe"] - base_tr, va["long_sharpe"] - base_va
    score = min(s_tr, s_va) if both_periods else s_tr
    return {"score": float(score) if score == score else float("-inf"), "sign": sign, "hl": hl, "kind": kind,
            "score_train": float(s_tr), "score_valid": float(s_va),
            "train": {k: tr[k] for k in ("long_ann", "long_sharpe", "long_turnover", "long_mdd")},
            "valid": {k: va[k] for k in ("long_ann", "long_sharpe", "long_turnover", "long_mdd")}}


__all__ = ["Node", "parse_expr", "walk", "operators", "leaves", "Pattern", "nesting", "nonneg", "simplify", "Rule", "Guidance",
           "RewardContext", "reward", "REWARDS", "LEAF_KINDS"]
