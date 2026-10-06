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
IDEMPOTENT_OPS = frozenset("abs_ cs_demean cs_rank".split())     # exactly f(f(x)) = f(x); nothing "nearly" idempotent belongs here


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
        """The canonical form: two candidates with the same key are the same experiment -- exactly, by the rewrite
        rules -- and only one of them should be scored.  Nothing that is merely "usually similar" is merged here."""
        return re.sub(r"\s+", "", self.canonical(expr))

    def family_key(self, expr: str) -> str:
        """The canonical form with the leaves of each ``family`` rule relabelled by order of first appearance
        (the k-th distinct price field met becomes @P<k>).  Two candidates with the same family key differ only
        by a renaming of those fields: ``day_std(Low)`` and ``day_std(Close)``, but NOT ``sub(High, Low)`` and
        ``sub(Close, Open)`` -- and not a tree and the tree with one of two leaves swapped.  Such siblings are
        usually close (median rank correlation 0.96-0.98 in the batch) and sometimes not (0.45), so a family is
        a reason to sample a sibling less often (``family_weight``), never to refuse it."""
        kinds = {r.pattern.tree.name: r for r in self.rules if r.action == "family" and r.pattern.tree.name in LEAF_KINDS}
        if not kinds:
            return self.dedup_key(expr)
        seen: Dict[str, Dict[str, str]] = {k: {} for k in kinds}

        def relabel(n: Node) -> Node:
            if n.args is None:
                for k in kinds:
                    if n.name in LEAF_KINDS[k]:
                        m = seen[k]
                        return Node(m.setdefault(n.name, f"{k[:2].upper()}{len(m) + 1}"))
                return n
            return Node(n.name, tuple(relabel(a) for a in n.args))

        return re.sub(r"\s+", "", str(relabel(parse_expr(self.canonical(expr)))))

    @property
    def family_weight(self) -> float:
        ws = [r.w for r in self.rules if r.action == "family"]
        return min(ws) if ws else 1.0

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
        every rule that says "this operator, whatever its operands, wherever it sits".  A rule with any context --
        anchored at the root, with a specific operand, an exception or a nesting depth -- is NOT folded in: a
        root-only ban turned into a vocabulary ban removed five operators from the steered arm that the rule
        never meant to touch.  Context is what ``accept`` enforces; this is the fallback, not the mechanism."""
        out: Dict[str, float] = {}
        for r in self.rules:
            if r.action not in ("ban", "weight"):
                continue
            head = r.pattern.tree.name
            names = [x.strip() for x in head[1:-1].split("|")] if head.startswith("{") else [head]
            generic = all(a.name in ("_", "$w") or re.fullmatch(r"_\d+", a.name or "") for a in r.pattern.tree.args or ())
            if not generic or r.unless is not None or r.depth_ge or r.pattern.root:
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


PAIRED = ("long_marginal", "long_screen")     # rewards that are a DIFFERENCE between two books on one universe
PAIRED_FLOOR = -1.0                             # a paired information ratio below this in either period is a rejection


def _daily_long_net(sm, tgt, days):
    """Daily net excess of the pure long book of ``sm`` over ``days`` (the book starts empty)."""
    from alphacube.metrics import long_short_weights

    from . import books as bk
    s, t = sm[days], tgt[days]
    return bk.long_book(long_short_weights(s, bk.TOP_FRAC), s, t)[0]


def _ir(d) -> float:
    import numpy as np
    f = d[np.isfinite(d)]
    if f.size < 30 or not f.std() > 0:
        return float("nan")
    return float(f.mean() / f.std() * np.sqrt(252))


def _top_band(x, frac: float = 0.2):
    """Boolean (days, stocks): the names whose whole TIE BLOCK lies in the top ``frac`` of the day's finite values.
    A block that straddles the cut is left out as a whole, so the band is at most ``frac`` wide, never decided by
    the order of the stocks, and a saturating panel (a share with most names at its floor) cannot screen 27% on
    one half-life and 20% on another."""
    import numpy as np
    import torch
    t = torch.from_numpy(np.ascontiguousarray(x, dtype=np.float64))
    ok = torch.isfinite(t)
    v = torch.where(ok, t, torch.full_like(t, float("-inf")))
    s_, order = torch.sort(v, dim=-1, stable=True)
    s_ = s_.contiguous()
    first = torch.searchsorted(s_, s_, right=False)
    n = ok.sum(-1, keepdim=True)
    below = (first - (t.shape[-1] - n)).to(torch.float64) / n.clamp(min=1).to(torch.float64)   # share of names strictly below the block
    band = torch.zeros_like(ok).scatter_(-1, order, below >= (1.0 - frac) - 1e-12) & ok
    return band.numpy()


def reward(panel, ctx: RewardContext, kind: str = "long", *, both_periods: bool = True) -> Dict[str, object]:
    """Score one raw (days, stocks) panel.  Direction and half-life are chosen on the TRAINING period only.

    Level rewards -- ``long`` / ``long_tradable`` / ``long_bucket``: the signal (direction x EMA) is, for the last
    two, cut to the tradable universe AFTER smoothing (the EMA sees the whole history; the universe only decides
    who can be ranked today), for the last one ranked inside liquidity buckets; its pure long book (top decile,
    equal weight, net of 15 bp, against the equal weight of the names with a signal and a label) is scored and
    the best (direction, half-life) by train Sharpe is kept.  ``score`` = pure-long Sharpe, the worse of train
    and valid.

    Paired rewards -- a candidate judged by what it does to another book ON THE SAME CELLS:
    ``long_marginal``  the 50/50 rank blend of candidate and pool, against the pool on exactly the cells where
                       the blend exists (a candidate's own missing values would otherwise move its benchmark);
    ``long_screen``    the base signal with the candidate's top fifth (whole tie blocks) sent below everything,
                       against the base itself.
    Their ``score`` is the information ratio of the PAIRED DAILY DIFFERENCE of the two books' net excess over
    train + valid together, unless the ratio of either period alone is below ``PAIRED_FLOOR`` (then that one):
    a Sharpe difference required in both periods cannot be met in a period where the pool's own Sharpe is 3.5
    (episode e2_I2), a paired difference says whether the candidate adds return reliably.  A candidate that
    changes nothing in the book (difference identically zero) is rejected, not scored 0."""
    import numpy as np

    from . import books as bk
    from . import diagnose as dg

    if kind not in REWARDS:
        raise ValueError(f"unknown reward {kind!r}; choose from {REWARDS}")
    raw = np.asarray(panel, dtype=np.float64)
    mask = ctx.untradable if (ctx.untradable is not None and kind in ("long_tradable", "long_bucket", "long_marginal")) else None
    keep = ("long_ann", "long_sharpe", "long_turnover", "long_mdd")
    best, extra = None, {}

    if kind not in PAIRED:
        for hl in ctx.halflives:
            sm0 = bk.smoothed(raw, hl)                       # the EMA is linear: one pass serves both directions
            if mask is not None:
                sm0 = np.where(mask, np.nan, sm0)
            for sign in (1.0, -1.0):
                sm = sign * sm0
                if kind == "long_bucket":
                    sm = _bucket_rank(sm, ctx.bucket())
                r = bk.book_row(sm, ctx.tgt, ctx.train)
                key = float(np.nan_to_num(r["long_sharpe"], nan=-9e9))
                if best is None or key > best[0]:
                    best = (key, sign, float(hl), sm, r)
        _, sign, hl, sm, tr = best
        va = bk.book_row(sm, ctx.tgt, ctx.valid)
        s_tr, s_va = tr["long_sharpe"], va["long_sharpe"]
        score = min(s_tr, s_va) if both_periods else s_tr
    else:
        if kind == "long_marginal":
            pu = ctx.pool_in_universe()
            cells = np.isfinite(raw) & np.isfinite(pu) if mask is None else np.isfinite(raw) & np.isfinite(pu) & ~mask
            ref = np.where(cells, pu, np.nan)                # the pool, on exactly the cells the blend can use
            ref_tr, ref_va = _daily_long_net(ref, ctx.tgt, ctx.train), _daily_long_net(ref, ctx.tgt, ctx.valid)
        else:
            ref = ctx.base
            if ctx._base_rows is None:
                ctx._base_rows = (_daily_long_net(ref, ctx.tgt, ctx.train), _daily_long_net(ref, ctx.tgt, ctx.valid))
            ref_tr, ref_va = ctx._base_rows
        for hl in ctx.halflives:
            sm0 = bk.smoothed(raw, hl)
            z0 = dg._zrank(np.where(cells, sm0, np.nan)) if kind == "long_marginal" else None
            for sign in (1.0, -1.0):
                if kind == "long_marginal":
                    sm = np.where(cells, 0.5 * sign * z0 + 0.5 * pu, np.nan)       # rank(-x) = -rank(x): one ranking per half-life
                    share = float("nan")
                else:
                    band = _top_band(np.where(np.isfinite(ref), sign * sm0, np.nan))
                    sm = np.where(np.isfinite(ref), np.where(band, ref - 2.0, ref), np.nan)   # below every unscreened name, order kept
                    share = float(band[ctx.train].sum() / max(np.isfinite(ref[ctx.train]).sum(), 1))
                with np.errstate(invalid="ignore"):
                    spread = np.nanmedian(np.nanstd(sm[ctx.train], axis=1))
                if not spread > 1e-12:                       # a signal with no cross-section (the pool blended with minus
                    continue                                 # itself) has no book: its "book" is the order of the columns
                ir = _ir(_daily_long_net(sm, ctx.tgt, ctx.train) - ref_tr)
                key = 0.0 if ir != ir else ir                # NaN = the book IS the reference book: worth exactly nothing,
                if best is None or key > best[0]:            # which still beats a direction that makes the book worse
                    best = (key, sign, float(hl), sm, ir, share)
        if best is None or best[4] != best[4]:               # the best this candidate can do is to change nothing
            nanrow = {k: float("nan") for k in keep}
            return {"score": float("-inf"), "sign": 1.0, "hl": float(ctx.halflives[0]), "kind": kind, "score_train": float("nan"),
                    "score_valid": float("nan"), "score_all": float("nan"), "no_effect": True, "train": nanrow, "valid": nanrow}
        _, sign, hl, sm, s_tr, share = best
        d_tr = _daily_long_net(sm, ctx.tgt, ctx.train) - ref_tr
        d_va = _daily_long_net(sm, ctx.tgt, ctx.valid) - ref_va
        s_va, s_all = _ir(d_va), _ir(np.concatenate([d_tr, d_va]))
        worst = min(s_tr, s_va) if (s_tr == s_tr and s_va == s_va) else float("nan")
        score = worst if not worst >= PAIRED_FLOOR else s_all            # NaN (a no-op) falls through to -inf below
        if not both_periods:
            score = s_tr
        tr, va = bk.book_row(sm, ctx.tgt, ctx.train), bk.book_row(sm, ctx.tgt, ctx.valid)
        extra = {"score_all": float(s_all), "screened_share": share} if kind == "long_screen" else {"score_all": float(s_all)}
    return {"score": float(score) if score == score else float("-inf"), "sign": sign, "hl": hl, "kind": kind,
            "score_train": float(s_tr), "score_valid": float(s_va), **extra,
            "train": {k: tr[k] for k in keep}, "valid": {k: va[k] for k in keep}}


__all__ = ["Node", "parse_expr", "walk", "operators", "leaves", "Pattern", "nesting", "nonneg", "simplify", "Rule", "Guidance",
           "RewardContext", "reward", "REWARDS", "PAIRED", "PAIRED_FLOOR", "LEAF_KINDS"]
