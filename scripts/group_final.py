"""The K002 reading rule, mechanically: the out-of-sample read of a hand-written batch (studies/K002_daily_fields/README.md, "现行规则").

From ``runs/<fid>/sweep_<tag>.json`` -- which holds train / valid numbers only -- this fixes, by a rule written before any
out-of-sample number exists, WHAT is read, and then reads each object once.

Objects and their roles (the sweep carries ``base`` / ``lock`` from the hypotheses file):
* rulers, always read, never selected: ``v_base``, ``k_known``, ``k_known_xfrozen`` and ``--always`` (default: the K002 list of
  ``DEFAULT_RULERS``);
* standalone hypotheses: id starts with a group prefix (``--groups``, default ``b_,c_,d_,e_``), no ``base``;
* modification hypotheses: the same, WITH ``base: <id>`` -- a screen / penalty / "only inside this board" on a carrier;
* twins (``<parent>_twin``) and carriers (``x_...``): never selected; read along with the hypothesis that needs them.

Selection, per group, in-sample only (train + valid); gates for every type: coverage >= 0.95, distinctness >= 0.5:
* standalone: long-leg net excess positive on BOTH train and valid; rank by the pure-long Sharpe of the user's training period,
  best first; keep a candidate only if the rank correlation of its TRADED signal (direction x EMA at its fitted half-life) with
  every standalone already kept in the group is below ``--distinct``; at most ``--per-group``;
* modification: the mean of its daily paired difference against its own base (pure-long net excess of the hypothesis minus that
  of its base, the same day) positive on BOTH train and valid, and not identically zero; rank by the information ratio of that
  difference over the training period; keep one only if its difference series correlates below ``--distinct`` (in-sample days)
  with those of the modifications already kept; at most ``--per-group``.
  The two difference series are built here from the panels, each book at its own direction and fitted half-life, as the
  out-of-sample read builds them -- nothing is approximated from summary statistics.

Read once: the rulers, every selected hypothesis, the base of every selected modification, the twin of every selected hypothesis,
each in the user's convention (half-life fitted on the user's training period; decile pure-long book net of 15 bp against the
equal-weight universe) and in the direction the sweep recorded for it -- for EVERY object, so a ruler locked with ``lock: true``
is read as written.  Periods: in-sample, the test period (the config's ``holdout``), the forward segment (the day after the
holdout ends .. the store's last day, or ``--end``) and the two out-of-sample periods together ("oos"); each repeated at a fixed
half-life (``--fixed-hl``).

Verdicts (paired daily differences, combined period's t, in-sample difference of the same sign; t >= 2 established, 1-2 right
direction not enough, 0-1 none, negative worse): a standalone against ``k_known``; a modification against its own base (with its
difference against ``k_known`` reported as a description); a twin: "parent minus twin", the daily field contributes only at
t >= 2.  "Is it size" is an EXPOSURE read, in-sample: the rank correlation of the traded signal with ``a_size``'s and the mean
overlap of the top-decile book with ``a_size``'s book; ``就是市值`` when the first is >= 0.7 or the second >= 0.5 (both are
reported for every object read); the paired difference against ``a_size`` is kept as "有没有赢过小市值", a description.  The level
criterion (combined-period net excess positive and Sharpe >= 1) is asked of group-B standalone picks and ``a_known_in_size``.
For a selected modification the share of its base's top-decile book it changes is reported (in-sample, combined period).
A final pass over all verdicts applies the multiplicity rule (``apply_multiplicity``).  When the fitted and the fixed half-life
disagree the fixed one wins and the disagreement is written out; the forward segment alone never decides.

Before a single out-of-sample number exists the script (1) refuses a second read of the same sweep tag (``--again`` to
override; the rule says the read happens once) and (2) recomputes the in-sample books of every object it is about to read on
the (extended) view and checks them against the sweep's own record (``--tol-ann`` / ``--tol-sharpe``; the check of
``scripts/forward_read.py``) -- a failure stops it with nothing ledgered.  The read is ledgered: ``runs/<fid>/ledger.json``
(test period) and ``runs/_forward/ledger.json`` (forward segment).  ``--dry-run`` does the selection and the check, prints
them and keeps them in ``runs/<fid>/group_select_<tag>.json``; it reads nothing out of sample, writes no ledger entry and no
result file (and a real read warns if its selection differs from that file's).

    python scripts/group_final.py <factor_id> [--sweep s1] [--groups b_,c_,d_,e_] [--per-group 3] [--always <ids>]
        [--distinct 0.7] [--fixed-hl 10] [--pair k_known,a_size] [--end <YYYYMMDD>] [--dry-run] [--again]

Writes ``runs/<fid>/group_final_<tag>.json`` (everything, including each read object's per-day series) and prints markdown
tables.  ``$PARTURA_STORE`` / ``$PARTURA_MIRROR`` move the minute store (default: the server's); the config's
``daily_fields: <dir>`` attaches the daily-field store.
"""
import argparse
import hashlib
import json
import math
import sys
import time
import warnings
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.guard import MemoryGuard, limit_threads, slot  # noqa: E402

if __name__ == "__main__":          # before numpy / torch start their pools (and not as a side effect of importing this file)
    limit_threads(8)
import numpy as np  # noqa: E402
import yaml  # noqa: E402

from partura import books as bk  # noqa: E402
from partura import diagnose as dg  # noqa: E402
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.panels import SHARED_CACHE, PanelSet, config_daily_root, default_mirror, default_store  # noqa: E402
from partura.splits import SPLITS, Ledger  # noqa: E402

from alphacube.metrics import cs_pearson, long_short_weights, nanmean_quiet  # noqa: E402

# ---------------------------------------------------------------------------------------------------------- constants
COV_MIN, DIST_MIN = 0.95, 0.5                       # the gates of scripts/sweep_final.py
BASE_IDS = ("v_base", "k_known", "k_known_xfrozen")
KNOWN_ID, SIZE_ID = "k_known", "a_size"             # the references: the known family; small float cap
DEFAULT_RULERS = BASE_IDS + ("a_size", "a_tsize", "a_turn20", "a_amt20", "a_known_in_size", "a_size_in_known", "a_known_in_turn",
                             "a_size_plus_known", "e_main_only", "e_wide_only", "e_xage1y")          # README, 现行规则: the rulers
GROUP_PREFIXES = ("b_", "c_", "d_", "e_")
GROUP_TITLES = {"b_": "B 拿掉市值之后还剩什么", "c_": "C 写法替换", "d_": "D 新信息", "e_": "E 筛子"}
LEVEL_GROUP, LEVEL_IDS = "b_", ("a_known_in_size",)  # "拿掉市值之后还剩东西" is asked of group-B standalone picks and of this ruler
LEVEL_SHARPE = 1.0                                  # ... = the combined period's pure-long net excess > 0 and Sharpe >= 1
NOISE_ANN, NOISE_SHARPE = 0.03, 0.3                 # the README's noise band of a level reading (+-3 points / +-0.3 Sharpe)
SIZE_RANK_CORR, SIZE_OVERLAP = 0.7, 0.5             # "就是市值": signal rank correlation with a_size >= 0.7, or top-decile book overlap >= 0.5
T_ESTABLISHED, T_RIGHT, T_OUTRIGHT = 2.0, 1.0, 3.0  # paired t: established / right direction / established beyond a multiplicity doubt
NOOP_TOL = 1e-12                                    # a daily difference this small on every day is "identically zero"
FWD_MIN_DAYS = 20                                   # as scripts/idea_final.py: fewer days than this is no forward segment
PERIODS = ("utrain", "holdout", "forward", "oos")
CONVS = ("fitted", "fixed")
NA = "无读数"
TWIN_OK = "日频字段有贡献"

# ------------------------------------------------------------------------------------------------------------ the pick


def _pos(x) -> bool:
    return x is not None and x == x and x > 0


def gate_failures(v: dict, legs: bool = True) -> list:
    """Why a sweep result may not be picked (empty list = it may).  The fields and thresholds are those of
    ``scripts/sweep_final.py``: not dead, coverage >= 0.95, distinctness >= 0.5, not a benchmark and -- ``legs=True``, for a
    standalone -- long-leg net excess positive on train AND on valid.  (A modification is judged on its difference against its
    base instead: ``legs=False``.)"""
    if v.get("dead"):
        return ["dead (no rank IC on train)"]
    out = []
    if v.get("kind") in ("bench", "base"):
        out.append(f"kind {v['kind']}")
    if not v["cov"] >= COV_MIN:
        out.append(f"coverage {v['cov']:.2f} < {COV_MIN}")
    if not v["dist"] >= DIST_MIN:
        out.append(f"distinctness {v['dist']:.2f} < {DIST_MIN}")
    if legs:
        if not _pos(v["train_long"]["long_ann"]):
            out.append("long-leg net excess on train not positive")
        if not _pos(v["valid_long"]["long_ann"]):
            out.append("long-leg net excess on valid not positive")
    return out


def utrain_sharpe(v: dict) -> float:
    """The standalone ranking key: pure-long Sharpe on the user's training period (train + valid); a missing one sorts last."""
    x = v.get("utrain_long", {}).get("long_sharpe")
    return x if x is not None and x == x else -9.0


def role_of(k: str, v: dict, rulers, groups) -> str:
    """ruler / twin / carrier / standalone / modification / other -- by the id and the keys the sweep carries from the hypotheses file
    (``base``; ``declared_kind``).  Anything named ``*_twin`` is a twin, whatever keys it carries (some have a ``base``); an object
    that is only somebody's explicit ``twin: <id>`` keeps the role it has by itself."""
    if k in rulers:
        return "ruler"
    if k.endswith("_twin"):
        return "twin"
    if k.startswith("x_") or v.get("declared_kind") == "carrier":
        return "carrier"
    if any(k.startswith(p) for p in groups):
        return "modification" if v.get("base") else "standalone"
    return "other"


def twin_of(R: dict, k: str):
    """The id of ``k``'s twin -- the same structure written without the daily field, or an existing comparison object -- if it has
    one: the explicit ``twin: <id>`` the sweep carried, else ``<k>_twin`` when the sweep has that."""
    t = R[k].get("twin") or f"{k}_twin"
    return t if t in R else None


def base_chain(R: dict, k: str) -> list:
    """The bases of ``k``, nearest first, as far as the chain goes (a base may itself have a base; a cycle stops it)."""
    out, seen = [], {k}
    b = R[k].get("base")
    while b and b in R and b not in seen:
        out.append(b)
        seen.add(b)
        b = R[b].get("base")
    return out


def rank_standalone(R: dict, ids) -> tuple:
    """(eligible ids best-first by the training-period Sharpe, {id: [reasons]} for the rest)."""
    ok, fail = [], {}
    for k in ids:
        f = gate_failures(R[k])
        if f:
            fail[k] = f
        else:
            ok.append(k)
    ok.sort(key=lambda k: (-utrain_sharpe(R[k]), k))
    return ok, fail


def gate_modifications(R: dict, ids) -> tuple:
    """(ids that pass the gates and whose base can be read, {id: [reasons]} for the rest).  Not ranked: that needs the books."""
    ok, fail = [], {}
    for k in ids:
        f = gate_failures(R[k], legs=False)
        b = R[k].get("base")
        if b not in R:
            f.append(f"base {b} is not in the sweep")
        elif R[b].get("dead"):
            f.append(f"base {b} is dead")
        if f:
            fail[k] = f
        else:
            ok.append(k)
    return ok, fail


def diff_stats(d, m_train, m_valid) -> dict:
    """What the selection asks of a modification's daily paired difference ``d`` (in-sample days): its mean on train and on valid
    (``m_train`` / ``m_valid`` are boolean masks over ``d``), its information ratio over the whole in-sample period, and whether it is
    identically zero (a no-op)."""
    d = np.asarray(d, dtype=np.float64)
    f = np.isfinite(d)
    out = {"n": int(f.sum()), "mean_train": float("nan"), "mean_valid": float("nan"), "ir": float("nan"), "ann": float("nan"), "noop": False}
    if not f.any():
        return out
    out["noop"] = bool(np.all(np.abs(d[f]) <= NOOP_TOL))
    if (f & m_train).any():
        out["mean_train"] = float(d[f & m_train].mean())
    if (f & m_valid).any():
        out["mean_valid"] = float(d[f & m_valid].mean())
    out["ann"] = float(d[f].mean() * 252)
    if f.sum() >= 20 and d[f].std() > 0:
        out["ir"] = float(d[f].mean() / d[f].std() * np.sqrt(252))
    return out


def modification_failures(st: dict) -> list:
    """Why a modification whose gates passed is still not eligible, from ``diff_stats``."""
    if st["noop"]:
        return ["the paired difference against its base is identically zero (a no-op)"]
    out = []
    if not _pos(st["mean_train"]):
        out.append("mean paired difference against its base on train not positive")
    if not _pos(st["mean_valid"]):
        out.append("mean paired difference against its base on valid not positive")
    if not st["ir"] == st["ir"] and not out:
        out.append("information ratio of the difference undefined")
    return out


def rank_modifications(ids, stats: dict) -> tuple:
    """(eligible ids best-first by the in-sample information ratio of their difference, {id: [reasons]} for the rest)."""
    ok, fail = [], {}
    for k in ids:
        f = modification_failures(stats[k])
        if f:
            fail[k] = f
        else:
            ok.append(k)
    ok.sort(key=lambda k: (-stats[k]["ir"], k))
    return ok, fail


def mean_daily_rank_corr(ra: np.ndarray, rb: np.ndarray) -> float:
    """Mean over days of the cross-sectional Pearson correlation of two RANK panels (= the mean daily Spearman)."""
    return float(nanmean_quiet(cs_pearson(ra, rb)))


def series_corr(a, b) -> float:
    """Pearson correlation of two daily series over the days both have; undefined (NaN) with fewer than 20 or no variance."""
    a, b = np.asarray(a, dtype=np.float64), np.asarray(b, dtype=np.float64)
    m = np.isfinite(a) & np.isfinite(b)
    if m.sum() < 20:
        return float("nan")
    x, y = a[m] - a[m].mean(), b[m] - b[m].mean()
    den = np.sqrt((x ** 2).sum() * (y ** 2).sum())
    return float((x * y).sum() / den) if den > 0 else float("nan")


def traded_ranks_in_sample(raw_in: np.ndarray, sign: float, hl: float) -> np.ndarray:
    """Rank panel of the signal a variant TRADES -- direction x EMA at its half-life -- over IN-SAMPLE days.
    ``raw_in`` must already be cut to the in-sample rows (the EMA is causal, so the cut changes nothing in them)."""
    return dg.rank_rows(bk.smoothed(sign * np.asarray(raw_in, dtype=np.float64), hl))


def select_group(ranked: list, feature_of, per_group: int, distinct: float, similarity=None):
    """The walk.  ``ranked``: eligible ids, best first.  ``feature_of(id)``: what two candidates are compared by -- the in-sample rank
    panel of a standalone's traded signal (``similarity`` = ``mean_daily_rank_corr``, the default), the in-sample daily difference
    series of a modification (``series_corr``).  Keeps an id only if its similarity with EVERY id already kept is below ``distinct``
    (an undefined one does not count against it); stops once ``per_group`` are kept.  Returns (kept, walk, unexamined), where
    ``walk`` has one entry per id looked at.  This function receives nothing but in-sample features."""
    similarity = similarity or mean_daily_rank_corr
    kept, kept_feat, walk = [], {}, []
    for i, k in enumerate(ranked):
        if len(kept) >= per_group:
            break
        r = feature_of(k)
        rhos = {j: similarity(r, kept_feat[j]) for j in kept}
        finite = {j: x for j, x in rhos.items() if x == x}
        top = max(finite, key=finite.get) if finite else None
        best = finite[top] if top is not None else float("nan")
        dup = best == best and best >= distinct
        walk.append({"id": k, "rank": i + 1, "max_corr": best, "with": top, "corr_with_kept": rhos,
                     "decision": "dropped" if dup else "kept"})
        if not dup:
            kept.append(k)
            kept_feat[k] = r
    return kept, walk, list(ranked[len(walk):])


def make_plan(R: dict, groups: list, always_arg, pair_ids: list) -> dict:
    """Everything that can be decided from the sweep file alone: the rulers, and per group the standalone hypotheses (gates, long
    legs, ranked) and the modification hypotheses (gates, base readable; ranked later, by their difference series).  No panel,
    no return."""
    base_missing = [k for k in BASE_IDS if k not in R]
    if base_missing:
        raise SystemExit(f"[group_final] the sweep has no {base_missing} (it always carries them -- is this a sweep file?)")
    extra = list(DEFAULT_RULERS[len(BASE_IDS):]) if always_arg is None else [k for k in always_arg if k]
    wanted = list(dict.fromkeys(list(BASE_IDS) + extra + list(pair_ids)))
    unknown = [k for k in wanted if k not in R]
    if unknown:
        raise SystemExit(f"[group_final] ids not in the sweep: {unknown}")
    dead = {k: "dead in the sweep (no rank IC on train): not read" for k in wanted if R[k].get("dead")}
    for k in list(BASE_IDS) + list(pair_ids):
        if k in dead:
            raise SystemExit(f"[group_final] {k} is dead in the sweep; it is a reference of the rule and cannot be read around")
    rulers = set(wanted)
    out = {"always": [k for k in wanted if k not in dead], "unread": dead, "groups": {}}
    for pfx in groups:
        mine = [k for k, v in R.items() if k.startswith(pfx) and role_of(k, v, rulers, groups) in ("standalone", "modification")]
        stand, mods = [k for k in mine if not R[k].get("base")], [k for k in mine if R[k].get("base")]
        s_ok, s_fail = rank_standalone(R, stand)
        m_ok, m_fail = gate_modifications(R, mods)
        out["groups"][pfx] = {"prefix": pfx, "title": GROUP_TITLES.get(pfx, pfx), "n_standalone": len(stand), "n_modification": len(mods),
                              "standalone": {"eligible": s_ok, "gate_fail": s_fail}, "modification": {"gated": m_ok, "gate_fail": m_fail}}
    return out


# ----------------------------------------------------------------------------------------------------- the statistics


def paired_stats(a: np.ndarray, b: np.ndarray) -> dict:
    """Paired daily difference ``a - b`` (the same day, net excess of two pure-long books): annualised difference,
    information ratio, t = ir x sqrt(years).  The formulas of ``scripts/sweep_final.py: paired``."""
    d = np.asarray(a, dtype=np.float64) - np.asarray(b, dtype=np.float64)
    d = d[np.isfinite(d)]
    if d.size < 20 or not d.std() > 0:
        return {"ann": float("nan"), "ir": float("nan"), "t": float("nan"), "n": int(d.size)}
    return {"ann": float(d.mean() * 252), "ir": float(d.mean() / d.std() * np.sqrt(252)),
            "t": float(d.mean() / d.std() * np.sqrt(d.size)), "n": int(d.size)}


def long_mask(sm: np.ndarray) -> np.ndarray:
    """The names the decile pure-long book holds each day (a boolean days x names panel)."""
    return long_short_weights(sm, bk.TOP_FRAC) > 0


def book_overlap_by_day(held_a: np.ndarray, held_b: np.ndarray) -> np.ndarray:
    """Per day, the share of capital two equal-weight top-decile books hold in the same names (``common / max(size_a, size_b)``;
    the same as sum(min(w_a, w_b)) of the two long legs); undefined where either holds nothing."""
    ka, kb = held_a.sum(1), held_b.sum(1)
    inter = (held_a & held_b).sum(1)
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.where((ka > 0) & (kb > 0), inter / np.maximum(ka, kb), np.nan)


def is_size_exposure(rank_corr: float, overlap: float) -> bool:
    """"就是市值": the traded signal's rank correlation with a_size's is >= 0.7, or the top-decile book's overlap with a_size's is >= 0.5."""
    return bool((rank_corr == rank_corr and rank_corr >= SIZE_RANK_CORR) or (overlap == overlap and overlap >= SIZE_OVERLAP))


def classify(t: float, ann_in: float) -> str:
    """README 判读.  Established = the combined period's paired t >= 2 AND the in-sample difference has the same
    (positive) sign; 1 <= t < 2, or t >= 2 with an in-sample difference of the other sign = right direction, not enough;
    0 <= t < 1 = none; t < 0 = worse."""
    if t is None or t != t:
        return NA
    if t >= T_ESTABLISHED and ann_in is not None and ann_in == ann_in and ann_in > 0:
        return "成立"
    if t >= T_RIGHT:
        return "方向对、证据不够"
    if t >= 0:
        return "没有"
    return "更差"


classify_vs_known = classify


def needs_level(obj_id: str, role: str) -> bool:
    return (role == "standalone" and obj_id.startswith(LEVEL_GROUP)) or obj_id in LEVEL_IDS


def level_reading(row_oos: dict) -> dict:
    """"拿掉市值之后还剩东西": the object's own combined-period pure-long net excess is positive and its Sharpe >= 1.
    A level reading, not paired; ``edge`` marks one inside the README's noise band of either threshold."""
    ann, sh = row_oos["long_ann"], row_oos["long_sharpe"]
    ok = ann == ann and sh == sh
    return {"remains": bool(ok and ann > 0 and sh >= LEVEL_SHARPE), "ann": ann, "sharpe": sh,
            "edge": bool(ok and (abs(ann) <= NOISE_ANN or abs(sh - LEVEL_SHARPE) <= NOISE_SHARPE))}


def _summary(p):
    """A paired result reduced to what a verdict looks at: combined-period t and difference, the in-sample difference, the label."""
    if not p:
        return None
    return {"label": classify(p["oos"]["t"], p["utrain"]["ann"]), "t_oos": p["oos"]["t"], "ann_oos": p["oos"]["ann"], "ann_in": p["utrain"]["ann"], "n_oos": p["oos"]["n"]}


def judge_convention(obj_id: str, role: str, ref_id, pair_ref, pair_known, pair_size, row_oos: dict, is_size: bool = False, pair_twin=None) -> dict:
    """The verdict of one object under one half-life convention.

    ``pair_ref``: {period: paired_stats} against the verdict's reference -- ``k_known`` for a standalone (and, as a description, for
    a ruler), the object's own base for a modification; ``pair_known`` / ``pair_size``: against ``k_known`` (a description) and
    against ``a_size`` ("有没有赢过小市值", a description); ``pair_twin``: parent minus twin.  ``is_size``: the in-sample exposure
    read (see ``is_size_exposure``).  A carrier or a twin is only read along: no verdict."""
    out = {"role": role, "ref": ref_id, "label": NA, "label_paired": NA, "vs_ref": _summary(pair_ref), "vs_known": _summary(pair_known),
           "vs_size": _summary(pair_size), "twin": None, "note": "", "level": None}
    if obj_id == KNOWN_ID:
        out["label"] = out["label_paired"] = "基准"
        return out
    if role in ("carrier", "twin"):
        out["label"] = out["label_paired"] = "一起读"
        return out
    if pair_twin:
        tw = _summary(pair_twin)
        out["twin"] = {**tw, "label": TWIN_OK if tw["label"] == "成立" else tw["label"]}
    if pair_ref:
        t, ann_in = out["vs_ref"]["t_oos"], out["vs_ref"]["ann_in"]
        out["label_paired"] = base = out["vs_ref"]["label"]
        out["label"] = "就是市值" if (role in ("standalone", "modification") and base == "成立" and is_size) else base
        if t == t and t >= T_ESTABLISHED and not (ann_in == ann_in and ann_in > 0):
            out["note"] = "合并段 t >= 2,但样本内差为负或无读数"
        if t != t and pair_ref["oos"]["n"] >= 20:
            out["note"] = f"和 {ref_id} 逐日相同(成对差为零),没有可读的差"
    if needs_level(obj_id, role):
        out["level"] = level_reading(row_oos)
    return out


def combine_conventions(fit: dict, fix: dict, hl_fit: float, hl_fix: float) -> dict:
    """The final verdict of one object: the fixed half-life's.  When the two reads disagree, say so."""
    notes = []
    agree = fit["label"] == fix["label"]
    if not agree:
        notes.append(f"两种读法不一致:拟合半衰期 {hl_fit:g} 读「{fit['label']}」,固定半衰期 {hl_fix:g} 读「{fix['label']}」;以固定半衰期的为准")
    lf, lx = fit["level"], fix["level"]
    agree_level = (lf is None and lx is None) or (lf is not None and lx is not None and lf["remains"] == lx["remains"])
    if not agree_level:
        notes.append(f"水平读数两种读法不一致:拟合半衰期 {hl_fit:g} 读「{'有' if lf['remains'] else '无'}」,"
                     f"固定半衰期 {hl_fix:g} 读「{'有' if lx['remains'] else '无'}」;以固定半衰期的为准")
    tf, tx = fit["twin"], fix["twin"]
    agree_twin = (tf is None and tx is None) or (tf is not None and tx is not None and tf["label"] == tx["label"])
    if not agree_twin:
        notes.append(f"孪生的读法两种半衰期不一致:拟合半衰期 {hl_fit:g} 读「{tf and tf['label']}」,固定半衰期 {hl_fix:g} 读「{tx and tx['label']}」;以固定半衰期的为准")
    return {"fitted": fit, "fixed": fix, "role": fix["role"], "ref": fix["ref"], "final_paired": fix["label"], "final": fix["label"],
            "final_level": fix["level"], "final_twin": tx, "agree": bool(agree and agree_level and agree_twin),
            "notes": notes + [n for n in (fix["note"],) if n]}


def apply_multiplicity(picks: dict, distinct) -> dict:
    """The multiplicity pass over all verdicts (README, 现行规则).  ``picks``: {id: {"group", "label", "t"}} for the SELECTED
    hypotheses (rulers are descriptions and carriers / twins have no verdict) with their final label before this pass and the
    combined-period t of the paired difference it rests on; ``distinct(a, b)``: are two picks of the same group mutually distinct?

    A pick labelled 成立 stays 成立 if its t is >= 3, or if another 成立 pick of the SAME group is distinct from it (two independent
    confirmations of one idea); otherwise it is 候选成立 -- a lone t between 2 and 3 among some twenty tests is what chance
    produces about four times in ten.  (Two 成立 picks in different groups do not confirm each other: each stays a candidate.  The
    README's first sentence alone would leave them 成立; the second sentence, "only t >= 3 or a same-group pair is written
    directly as 成立", is the stricter reading and the one implemented.)  Returns {id: {"label", "note"}} for every pick."""
    out = {k: {"label": p["label"], "note": ""} for k, p in picks.items()}
    est = [k for k, p in picks.items() if p["label"] == "成立"]
    for k in est:
        p = picks[k]
        if p["t"] >= T_OUTRIGHT:
            continue
        if any(j != k and picks[j]["group"] == p["group"] and distinct(k, j) for j in est):
            continue
        n = len(est)
        out[k] = {"label": "候选成立", "note": "多重比较:" + ("整轮只有这一个成立" if n == 1 else f"整轮有 {n} 个成立,但同组里没有第二个互不相关的")
                  + f",t = {p['t']:.2f} 在 2 ~ 3 之间,记候选,等前推段变长再确认"}
    return out


# --------------------------------------------------------------------------------------------------------- the guard


def prior_reads(root: Path, fid: str, tag: str) -> list:
    """What shows that this sweep tag has already been read: a ledger entry of its stage, or its result file."""
    stage, found = f"group_final_{tag}", []
    lp = root / "runs" / fid / "ledger.json"
    if lp.is_file():
        found += [f"ledger entry {e.when} ({e.split}, {e.n_expressions} objects) in {lp}" for e in Ledger(lp).entries if e.stage == stage]
    op = root / "runs" / fid / f"group_final_{tag}.json"
    if op.is_file():
        found.append(f"result file {op}")
    return found


# ------------------------------------------------------------------------------------------------------ formatting


def clean(o):
    """JSON-safe: numpy -> python, NaN / inf -> null."""
    if isinstance(o, dict):
        return {str(k): clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [clean(v) for v in o]
    if isinstance(o, np.ndarray):
        return [clean(v) for v in o.tolist()]
    if isinstance(o, (np.floating, float)):
        return None if not math.isfinite(float(o)) else float(o)
    if isinstance(o, np.integer):
        return int(o)
    if isinstance(o, np.bool_):
        return bool(o)
    return o


def same_number(a, b, tol: float = 1e-9) -> bool:
    """Equal, or both undefined."""
    return (a != a and b != b) or abs(a - b) <= tol


def _series(x: np.ndarray) -> list:
    return [None if not np.isfinite(v) else round(float(v), 7) for v in x]


def f_pct(x, nd: int = 1) -> str:
    return "—" if x is None or x != x else f"{x:+.{nd}%}"


def f_num(x) -> str:
    return "—" if x is None or x != x else f"{x:+.2f}"


def f_level(row) -> str:
    return "—" if not row else f"{f_pct(row['long_ann'])} / {f_num(row['long_sharpe'])}"


def f_pair(p) -> str:
    return "—" if not p or p["t"] != p["t"] else f"{f_pct(p['ann'])} (t {p['t']:+.1f})"


def f_sum(s) -> str:
    return "—" if not s or s["t_oos"] != s["t_oos"] else f"{f_pct(s['ann_oos'])} (t {s['t_oos']:+.1f})"


def f_hl(x) -> str:
    return f"{x:g}"


def f_level_verdict(lv) -> str:
    if not lv:
        return ""
    return f"水平:{'有' if lv['remains'] else '无'}{'(临界)' if lv['edge'] else ''}"


def md_row(cells) -> str:
    return "| " + " | ".join(str(c) for c in cells) + " |"


ROLE_NAMES = {"ruler": "尺子", "standalone": "独立", "modification": "修改型", "carrier": "载体", "twin": "孪生"}


def render_selection(plan: dict, sel: dict, args, periods: dict, repro: dict, info: dict, prep: dict) -> str:
    L = [f"## 选择(只用样本内 {periods['utrain'][0]}~{periods['utrain'][1]};没有读任何样本外数字)", ""]
    locked = [k for k in info if prep[k]["sign_locked"]]
    L.append(f"尺子(总是读,{len(plan['always'])} 个):{', '.join(k + ('(锁)' if k in locked else '') for k in plan['always'])}")
    if plan["unread"]:
        L.append("没读(扫描里是 dead):" + "; ".join(f"{k} ({why})" for k, why in plan["unread"].items()))
    if locked:
        L.append(f"方向锁定为表达式写的方向(+1,扫描里 sign_locked)的有 {len(locked)} 个:{', '.join(locked)}")
    other_way = [k for k in info if prep[k]["sign"] != prep[k]["sign_ic_utrain"]]
    if other_way:
        L.append(f"读的方向(扫描记的)与用户训练段 rank IC 的符号不同的有 {len(other_way)} 个:{', '.join(other_way)}")
    L.append("")
    for pfx, g in sel.items():
        s, m = g["standalone"], g["modification"]
        L += [f"### {g['title']}  ({pfx})  独立假设 {g['n_standalone']} 个、修改型假设 {g['n_modification']} 个", ""]
        L.append(f"**独立假设**:过门槛且 train、valid 多头腿为正 {len(s['eligible'])} 个;选 {len(s['kept'])} 个(上限 {args.per_group},信号秩相关 < {args.distinct:g})")
        if s["walk"]:
            L += ["", md_row(["排名", "id", "样本内夏普", "train / valid 净超额", "半衰期", "与已选者的最大秩相关", "结果"]), md_row(["---"] * 7)]
            for w in s["walk"]:
                L.append(md_row([w["rank"], w["id"], f_num(w["sharpe"]), f"{f_pct(w['train_ann'])} / {f_pct(w['valid_ann'])}", f_hl(w["hl"]),
                                 "—" if w["with"] is None else f"{w['max_corr']:+.2f} ({w['with']})",
                                 "**选**" if w["decision"] == "kept" else f"去掉(≥ {args.distinct:g})"]))
        if s["unexamined"]:
            L.append(f"没轮到(已选满):{', '.join(s['unexamined'])}")
        if s["gate_fail"]:
            L.append("没过:" + "; ".join(f"{k} [{', '.join(v)}]" for k, v in s["gate_fail"].items()))
        L.append("")
        L.append(f"**修改型假设**:过门槛 {len(m['gated'])} 个,对载体的成对差在 train、valid 的均值都为正 {len(m['eligible'])} 个;选 {len(m['kept'])} 个"
                 f"(上限 {args.per_group},差序列相关 < {args.distinct:g})")
        if m["walk"]:
            L += ["", md_row(["排名", "id", "载体", "样本内信息比", "train / valid 平均日差(年化)", "与已选者的差序列最大相关", "结果"]), md_row(["---"] * 7)]
            for w in m["walk"]:
                L.append(md_row([w["rank"], w["id"], w["base"], f_num(w["ir"]), f"{f_pct(w['ann_train'])} / {f_pct(w['ann_valid'])}",
                                 "—" if w["with"] is None else f"{w['max_corr']:+.2f} ({w['with']})",
                                 "**选**" if w["decision"] == "kept" else f"去掉(≥ {args.distinct:g})"]))
        if m["unexamined"]:
            L.append(f"没轮到(已选满):{', '.join(m['unexamined'])}")
        if m["not_eligible"]:
            L.append("没过:" + "; ".join(f"{k} [{', '.join(v)}]" for k, v in m["not_eligible"].items()))
        L.append("")
    along = [(k, i) for k, i in info.items() if i["role"] in ("carrier", "twin")]
    if along:
        L.append("## 一起读的载体与孪生")
        L.append("; ".join(f"{k}({ROLE_NAMES[i['role']]},为 {', '.join(i['needed_by'])})" for k, i in along))
        L.append("")
    L += ["## 暴露(样本内,和 a_size 比;这两个数对每个读到的对象都报)", "",
          md_row(["id", "角色", "交易信号与 a_size 的秩相关", "多头书与 a_size 多头书的平均重合度", "就是市值?"]), md_row(["---"] * 5)]
    for k, i in info.items():
        e = prep[k]["expo"]
        L.append(md_row([k, ROLE_NAMES[i["role"]], f_num(e["rank_corr_size"]), f_num(e["book_overlap_size"]), "是" if e["is_size"] else "否"]))
    L += ["", f"## 复现检查(样本内,扩展视窗上重算的多头书对扫描记录;容差 年化 {args.tol_ann:g}、夏普 {args.tol_sharpe:g})",
          f"{len(repro['objects'])} 个对象:{'通过' if repro['pass'] else '未通过'};最大偏差 年化 {repro['worst_ann']:.1e},夏普 {repro['worst_sharpe']:.1e}"]
    for b in repro["failed"][:30]:
        L.append("  " + b)
    return "\n".join(L)


def render_block(title: str, ids: list, out: dict) -> list:
    """Two tables for a block of objects: the levels, then the paired differences / exposure / verdict."""
    res, paired, verd, info = out["results"], out["paired"], out["verdicts"], out["roles"]
    L = [f"## {title}", "", md_row(["id", "角色", "方向", "半衰期", "样本内", "测试段", "前推段", "合并段"]), md_row(["---"] * 8)]
    for k in ids:
        r = res[k]
        for conv, name in (("fitted", "拟合"), ("fixed", "固定")):
            b = r["conv"][conv]["books"]
            L.append(md_row([k if conv == "fitted" else "", ROLE_NAMES[info[k]["role"]] if conv == "fitted" else "",
                             (f"{int(r['sign_user']):+d}" + (" 锁" if r["sign_locked"] else "")) if conv == "fitted" else "",
                             f"{name} {f_hl(r['conv'][conv]['hl'])}"] + [f_level(b.get(p)) for p in PERIODS]))
    L += ["", md_row(["id", "半衰期", "对谁", "减它: 测试", "前推", "合并", "减 k_known 合并", "有没有赢过小市值 合并", "秩相关 / 书重合(对 a_size)", "改动载体多大比例 样本内 / 合并", "父 − 孪生 合并", "判读"]),
          md_row(["---"] * 12)]
    for k in ids:
        for conv, name in (("fitted", "拟合"), ("fixed", "固定")):
            jv = verd[k][conv]
            ref = jv["ref"]
            pr = paired.get(ref, {}).get(k, {}).get(conv, {}) if ref and ref != k else {}
            e = res[k]["exposure"]
            ch = res[k].get("changed_share", {}).get(conv)
            tw = jv["twin"]
            final = verd[k]["final"] if conv == "fixed" else jv["label"]
            L.append(md_row([k if conv == "fitted" else "", name, ref if ref and ref != k else "—"]
                            + [f_pair(pr.get(p)) for p in ("holdout", "forward", "oos")]
                            + [f_sum(jv["vs_known"]) if ref != KNOWN_ID else "(同左)", f_sum(jv["vs_size"]),
                               f"{f_num(e['rank_corr_size'])} / {f_num(e['book_overlap_size'])}" if conv == "fitted" else "",
                               "" if not ch else f"{f_pct(ch['in_sample'], 0)} / {f_pct(ch['oos'], 0)}",
                               "—" if not tw else f"{f_sum(tw)} {tw['label']}",
                               final + (" " + f_level_verdict(jv["level"]) if jv["level"] else "")]))
    L.append("")
    for k in ids:
        L.append(f"- `{k}` = `{res[k]['expr']}`" + (f"  — 载体 `{res[k]['base']}`" if res[k].get("base") else "") + (f"  — {res[k]['why']}" if res[k].get("why") else ""))
    L.append("")
    return L


def render_results(out: dict, groups: list) -> str:
    res, verd, info, per = out["results"], out["verdicts"], out["roles"], out["periods"]
    L = [f"# {out['factor_id']} 样本外读数(扫描 {out['sweep']};规则:studies/K002_daily_fields/README.md「现行规则」,读一次)", "",
         f"视窗 {out['view']['start']} ~ {out['view']['end']};样本内 {per['utrain'][0]}~{per['utrain'][1]};测试段 {per['holdout'][0]}~{per['holdout'][1]};"
         + (f"前推段 {per['forward'][0]}~{per['forward'][1]}({out['years']['forward']:.2f} 年);" if per.get("forward") else "没有前推段;")
         + f"合并段约 {out['years']['oos']:.2f} 年。读了 {len(res)} 个对象。固定半衰期 {out['args']['fixed_hl']:g}。", "",
         "格式:多头净超额年化 / 纯多头夏普;成对差 = 同一天的多头净超额相减,年化差 (t);判读看合并段的 t 并要求样本内同号,以固定半衰期的为准。"
         "独立假设对 k_known;修改型假设对自己的载体;尺子只是描述。", ""]
    rulers = [k for k in res if info[k]["role"] == "ruler"]
    L += render_block("尺子(总是读;描述,不拿来挑)", [k for k in BASE_IDS if k in rulers] + [k for k in rulers if k not in BASE_IDS], out)
    along = [k for k in res if info[k]["role"] in ("carrier", "twin") and info[k]["group"] == "ruler"]
    if along:
        L += render_block("尺子的载体", along, out)
    for pfx in groups:
        title = GROUP_TITLES.get(pfx, pfx)
        for role, name in (("standalone", "独立假设"), ("modification", "修改型假设(对自己的载体判)")):
            ids = [k for k in res if info[k]["role"] == role and info[k]["group"] == pfx]
            if ids:
                L += render_block(f"{title} —— {name}", ids, out)
        along = [k for k in res if info[k]["role"] in ("carrier", "twin") and info[k]["group"] == pfx]
        if along:
            L += render_block(f"{title} —— 一起读的载体与孪生", along, out)
    L += ["## 判读汇总(固定半衰期的为准;多重比较已处理)", "",
          md_row(["id", "角色", "组", "对谁", "拟合半衰期读法", "固定半衰期读法", "最终", "就是市值?(秩相关 / 书重合)", "拿掉市值之后还剩东西?(合并段 净超额 / 夏普)", "孪生", "说明"]), md_row(["---"] * 11)]
    for k in res:
        v = verd[k]
        if k == KNOWN_ID or info[k]["role"] in ("carrier", "twin"):
            continue
        lv, tw, e = v["final_level"], v["final_twin"], res[k]["exposure"]
        L.append(md_row([k, ROLE_NAMES[info[k]["role"]], info[k]["group"] if info[k]["role"] != "ruler" else "", v["ref"] or "", v["fitted"]["label"], v["fixed"]["label"],
                         f"**{v['final']}**", f"{'是' if e['is_size'] else '否'}({f_num(e['rank_corr_size'])} / {f_num(e['book_overlap_size'])})",
                         "" if not lv else f"{'有' if lv['remains'] else '无'}{'(临界)' if lv['edge'] else ''}:{f_pct(lv['ann'])} / {f_num(lv['sharpe'])}",
                         "" if not tw else f"{tw['label']}({f_sum(tw)})", ";".join(v["notes"])]))
    L += ["", "前推段只有不到一年,单看它不下结论;成对差的 t = 信息比 × √年数;水平读数的噪声带 ±3 个点 / ±0.3 夏普;尺子的判读只是描述,不进多重比较。"]
    return "\n".join(L)


# ------------------------------------------------------------------------------------------------------------- main


def parse_args(argv):
    p = argparse.ArgumentParser(prog="group_final.py", description=__doc__.split("    python")[0].strip().split("\n")[0])
    p.add_argument("factor_id")
    p.add_argument("--sweep", default="s1", help="the sweep tag (runs/<fid>/sweep_<tag>.json)")
    p.add_argument("--groups", default=",".join(GROUP_PREFIXES), help="group prefixes to pick from")
    p.add_argument("--per-group", type=int, default=3, help="at most this many standalone AND this many modification picks per group")
    p.add_argument("--always", default=None, help="ids always read besides v_base / k_known / k_known_xfrozen (default: the K002 rulers, DEFAULT_RULERS)")
    p.add_argument("--distinct", type=float, default=0.7, help="a candidate whose similarity with one already kept is >= this is dropped")
    p.add_argument("--fixed-hl", type=float, default=10.0)
    p.add_argument("--pair", default=f"{KNOWN_ID},{SIZE_ID}", help="objects the paired differences are taken against")
    p.add_argument("--end", default=None, help="last day of the view (default: the store's last day)")
    p.add_argument("--dry-run", action="store_true", help="select and check only: no out-of-sample read, no ledger entry, no result file")
    p.add_argument("--again", action="store_true", help="read a sweep tag that was already read (ledgered as a repeat)")
    p.add_argument("--tol-ann", type=float, default=5e-4, help="reproduction check: largest in-sample difference in annualised net excess")
    p.add_argument("--tol-sharpe", type=float, default=0.02, help="reproduction check: largest in-sample difference in Sharpe")
    return p.parse_args(argv)


def last_store_day() -> str:
    from alphacube.store import open_cube_store
    return str(open_cube_store(default_store(), mirror_root=default_mirror()).dates[-1])


def split_periods(ps) -> dict:
    """Row slices of the view: in-sample (the config's ``utrain``), the test period (``holdout``), the forward segment (every
    day after the holdout ends, if there are enough of them) and the two out-of-sample periods together."""
    n = len(ps.dates)
    us, ho = ps.split_slice("utrain"), ps.split_slice("holdout")
    fw = slice(ho.stop, n)
    has_fw = fw.stop - fw.start > FWD_MIN_DAYS
    return {"utrain": us, "holdout": ho, "forward": fw if has_fw else None, "oos": slice(ho.start, n) if has_fw else ho}


def main(argv=None) -> int:
    args = parse_args(argv)
    fid, tag = args.factor_id, args.sweep
    root = Path(PARTURA_ROOT)
    cfg = yaml.safe_load((root / "configs" / f"{fid}.yaml").read_text(encoding="utf-8"))
    for k, v in cfg["splits"].items():
        SPLITS[k] = (str(v[0]), str(v[1]))
    daily = config_daily_root(cfg)
    sweep_bytes = (root / "runs" / fid / f"sweep_{tag}.json").read_bytes()
    sweep = json.loads(sweep_bytes)
    R = sweep["results"]
    sweep_sha = hashlib.sha1(sweep_bytes).hexdigest()[:12]
    groups = [g for g in args.groups.split(",") if g]
    pair_ids = [g for g in args.pair.split(",") if g]
    plan = make_plan(R, groups, None if args.always is None else args.always.split(","), pair_ids)
    if not args.dry_run and not args.again:
        prior = prior_reads(root, fid, tag)
        if prior:
            raise SystemExit(f"[group_final] sweep {tag} of {fid} was already read ({'; '.join(prior)}).  The rule says the out-of-sample "
                             f"read happens once; pass --again to read it again (it is ledgered as a repeat).")
    if sweep.get("daily_fields") != daily:
        print(f"[group_final] WARNING: the sweep was run with daily_fields={sweep.get('daily_fields')!r}, the config now says {daily!r}", flush=True)

    with slot():
        mem = MemoryGuard(self_limit_gb=34, cgroup_limit_gb=70).start()
        t0 = time.time()
        end = args.end or last_store_day()
        lab = cfg.get("label") or {}
        ps = PanelSet(default_store(), SPLITS["full"][0], end, warmup=int(cfg.get("warmup", 60)), device="cuda", gpu_fraction=0,
                      cache_dir=str(SHARED_CACHE), mirror_root=default_mirror(), workdir=str(root / "tmp"),
                      label_kind=lab.get("kind", "open_vwap15"), label_buyable=bool(lab.get("buyable", True)), batch=8, daily_root=daily)
        rulers = plan["always"]
        stand_ids = [k for g in plan["groups"].values() for k in g["standalone"]["eligible"]]
        mod_ids = [k for g in plan["groups"].values() for k in g["modification"]["gated"]]
        need = list(dict.fromkeys(rulers + stand_ids + mod_ids + [R[k]["base"] for k in mod_ids]))
        P = ps.compute({k: R[k]["expr"] for k in need})
        failed = [k for k in need if k not in P]
        if failed:
            raise SystemExit(f"[group_final] expressions that did not evaluate on this view: { {k: ps.errors.get(k) for k in failed} }")
        dates = np.asarray(ps.dates).astype(str)
        sl = split_periods(ps)
        us, ho, fw, oos = sl["utrain"], sl["holdout"], sl["forward"], sl["oos"]
        n_in = us.stop
        if us.stop != ho.start:
            print(f"[group_final] WARNING: in-sample ends {dates[us.stop - 1]}, the test period starts {dates[ho.start]}: days between them are in neither", flush=True)
        per = {"utrain": [str(dates[us.start]), str(dates[us.stop - 1])], "holdout": [str(dates[ho.start]), str(dates[ho.stop - 1])],
               "forward": None if fw is None else [str(dates[fw.start]), str(dates[fw.stop - 1])], "oos": [str(dates[oos.start]), str(dates[oos.stop - 1])]}
        print(f"[group_final] view {dates[0]} .. {dates[-1]} ({len(dates)} days x {len(ps.symbols)} names); in-sample {per['utrain'][0]}..{per['utrain'][1]}, "
              f"test {per['holdout'][0]}..{per['holdout'][1]}, forward {per['forward'] and (per['forward'][0] + '..' + per['forward'][1])}", flush=True)

        # ============================== phase 1: IN-SAMPLE ONLY -- the pick and the reproduction check =====================
        # Nothing below this line until the ledger entry sees a row past ``n_in``: panels and labels are cut to the in-sample
        # days here and the cut arrays are all that phase 1 uses.
        tgt_in = np.asarray(ps.target(1), dtype=np.float64)[:n_in]
        panel_in = lambda k: np.asarray(P[k][:n_in], dtype=np.float64)              # noqa: E731
        trs, vas = ps.split_slice("train"), ps.split_slice("valid")
        rows_in = np.arange(us.start, us.stop)
        m_tr, m_va = (rows_in >= trs.start) & (rows_in < trs.stop), (rows_in >= vas.start) & (rows_in < vas.stop)
        nets_in = {}

        def net_in(k):
            """Daily net excess of k's pure-long book over the in-sample period: its direction, its half-life fitted on the user's
            training period (the sweep's record), one continuous book from an empty start -- as the out-of-sample read builds it."""
            if k not in nets_in:
                sm = bk.smoothed(float(R[k]["sign"]) * panel_in(k), float(R[k]["hl_long_u"]))[us]
                nets_in[k] = bk.long_book(long_short_weights(sm, bk.TOP_FRAC), sm, tgt_in[us])[0]
            return nets_in[k]

        diffs = {k: net_in(k) - net_in(R[k]["base"]) for k in mod_ids}
        mod_stats = {k: diff_stats(diffs[k], m_tr, m_va) for k in mod_ids}
        sel = {}
        for pfx, g in plan["groups"].items():
            s_kept, s_walk, s_left = select_group(
                g["standalone"]["eligible"], lambda k: traded_ranks_in_sample(panel_in(k), float(R[k]["sign"]), float(R[k]["hl_long_u"])), args.per_group, args.distinct)
            for w in s_walk:
                v = R[w["id"]]
                w.update(sharpe=utrain_sharpe(v), train_ann=v["train_long"]["long_ann"], valid_ann=v["valid_long"]["long_ann"], hl=float(v["hl_long_u"]))
            m_ranked, m_fail = rank_modifications(g["modification"]["gated"], mod_stats)
            m_kept, m_walk, m_left = select_group(m_ranked, lambda k: diffs[k], args.per_group, args.distinct, similarity=series_corr)
            for w in m_walk:
                st = mod_stats[w["id"]]
                w.update(base=R[w["id"]]["base"], ir=st["ir"], ann_train=st["mean_train"] * 252, ann_valid=st["mean_valid"] * 252)
            sel[pfx] = {"title": g["title"], "n_standalone": g["n_standalone"], "n_modification": g["n_modification"],
                        "standalone": {"eligible": g["standalone"]["eligible"], "gate_fail": g["standalone"]["gate_fail"], "kept": s_kept, "walk": s_walk, "unexamined": s_left},
                        "modification": {"gated": g["modification"]["gated"], "eligible": m_ranked, "not_eligible": {**g["modification"]["gate_fail"], **m_fail},
                                         "kept": m_kept, "walk": m_walk, "unexamined": m_left,
                                         "stats": {k: mod_stats[k] for k in g["modification"]["gated"]}}}

        # who is read, and in what role
        info = {k: {"role": "ruler", "group": "ruler", "needed_by": []} for k in rulers}
        for pfx, g in sel.items():
            for role in ("standalone", "modification"):
                for k in g[role]["kept"]:
                    info.setdefault(k, {"role": role, "group": pfx, "needed_by": []})
        selected = [k for k, i in info.items() if i["role"] in ("standalone", "modification")]
        for k in list(info):                        # the base of everything that has one -- a selected modification, a ruler such as e_main_only -- and its base in turn
            if info[k]["role"] in ("modification", "ruler") and R[k].get("base"):
                child = k
                for b in base_chain(R, k):
                    if R[b].get("dead"):
                        break
                    info.setdefault(b, {"role": "carrier", "group": info[k]["group"], "needed_by": []})["needed_by"].append(child)
                    child = b
        twin_dead = {}
        for k in selected:
            t = twin_of(R, k)
            if t is None:
                continue
            if R[t].get("dead"):
                twin_dead[t] = f"twin of {k} is dead in the sweep: not read"
                continue
            info.setdefault(t, {"role": "twin", "group": info[k]["group"], "needed_by": []})["needed_by"].append(k)
        for t in [t for t, i in info.items() if i["role"] == "twin" and R[t].get("base")]:      # a twin with a base of its own (e_xmicro10_twin: k_known): read it too
            child = t
            for b in base_chain(R, t):
                if R[b].get("dead"):
                    break
                info.setdefault(b, {"role": "carrier", "group": info[t]["group"], "needed_by": []})["needed_by"].append(child)
                child = b
        more = {t: R[t]["expr"] for t in info if t not in P}
        if more:
            P.update(ps.compute(more))
            failed = [t for t in more if t not in P]
            if failed:
                raise SystemExit(f"[group_final] objects read along that did not evaluate on this view: { {k: ps.errors.get(k) for k in failed} }")
        read_ids = list(info)
        group_of = {k: info[k]["group"] for k in read_ids}

        us_ranks = dg.rank_rows(tgt_in[us])
        prep, repro = {}, {"objects": {}, "failed": [], "worst_ann": 0.0, "worst_sharpe": 0.0, "tol_ann": args.tol_ann, "tol_sharpe": args.tol_sharpe}
        for k in read_ids:
            v, raw = R[k], panel_in(k)
            ic = dg.ic_row(raw[us], tgt_in[us], target_ranks=us_ranks)
            sign_ic = 1.0 if not np.isfinite(ic["rank_ic"]) or ic["rank_ic"] >= 0 else -1.0      # what the user's own rule would pick: reported, not used
            sign = float(v["sign"])             # EVERY object is read in the direction the sweep recorded for it (a locked ruler: as written)
            fit = bk.fit_halflives(sign * raw, tgt_in, us)
            row = bk.book_row(bk.smoothed(sign * raw, fit["hl_long"]), tgt_in, us)
            rec = v["utrain_long"]
            d_ann, d_sh = abs(row["long_ann"] - rec["long_ann"]), abs(row["long_sharpe"] - rec["long_sharpe"])
            ok = bool(float(fit["hl_long"]) == float(v["hl_long_u"]) and d_ann <= args.tol_ann and d_sh <= args.tol_sharpe)
            repro["objects"][k] = {"ok": ok, "hl_here": float(fit["hl_long"]), "hl_sweep": float(v["hl_long_u"]), "ann_here": row["long_ann"], "ann_sweep": rec["long_ann"],
                                   "sharpe_here": row["long_sharpe"], "sharpe_sweep": rec["long_sharpe"]}
            repro["worst_ann"], repro["worst_sharpe"] = max(repro["worst_ann"], d_ann), max(repro["worst_sharpe"], d_sh)
            if not ok:
                repro["failed"].append(f"{k}: half-life {fit['hl_long']:g} vs {v['hl_long_u']:g}; ann {row['long_ann']:+.4f} vs {rec['long_ann']:+.4f}; "
                                       f"Sharpe {row['long_sharpe']:.3f} vs {rec['long_sharpe']:.3f}")
            prep[k] = {"sign": sign, "sign_ic_utrain": sign_ic, "sign_locked": bool(v.get("sign_locked")), "sign_by": v.get("sign_by"),
                       "fit": fit, "hl_fit": float(fit["hl_long"]), "utrain_row": row}
        repro["pass"] = not repro["failed"]

        # exposure to small float cap, in-sample, on the traded signal (direction x EMA at the fitted half-life)
        traded_in = lambda k: bk.smoothed(prep[k]["sign"] * panel_in(k), prep[k]["hl_fit"])[us]      # noqa: E731
        if SIZE_ID in prep:
            sm_size = traded_in(SIZE_ID)
            r_size, held_size = dg.rank_rows(sm_size), long_mask(sm_size)
        for k in read_ids:
            if SIZE_ID not in prep:
                rc = ov = float("nan")
            elif k == SIZE_ID:
                rc = ov = 1.0
            else:
                sm = traded_in(k)
                rc = mean_daily_rank_corr(dg.rank_rows(sm), r_size)
                ov = float(nanmean_quiet(book_overlap_by_day(long_mask(sm), held_size)))
            prep[k]["expo"] = {"rank_corr_size": rc, "book_overlap_size": ov, "is_size": is_size_exposure(rc, ov)}

        sweep_ref = {"sweep": tag, "sweep_sha1": sweep_sha, "daily_fields": daily}
        locked_ids = [k for k in read_ids if prep[k]["sign_locked"]]
        selection = {"rulers": plan["always"], "unread": {**plan["unread"], **twin_dead}, "read": read_ids, "locked": locked_ids, "groups": sel,
                     "roles": info, "args": {"per_group": args.per_group, "distinct": args.distinct, "groups": groups, "pair": pair_ids}, **sweep_ref}
        print("\n" + render_selection(plan, sel, args, per, repro, info, prep), flush=True)
        sel_path = root / "runs" / fid / f"group_select_{tag}.json"
        if args.dry_run or not repro["pass"]:
            sel_path.parent.mkdir(parents=True, exist_ok=True)
            sel_path.write_text(json.dumps(clean({"selection": selection, "repro": repro, "periods": per, "exposure": {k: prep[k]["expo"] for k in read_ids}}),
                                           ensure_ascii=False, indent=1), encoding="utf-8")
            mem.stop()
            print(f"\nwrote {sel_path} ({time.time() - t0:.0f}s)" + ("  [dry run: nothing out of sample was read, nothing ledgered]" if args.dry_run else ""))
            if not repro["pass"]:
                print("[group_final] the sweep's in-sample numbers do not reproduce on this view: nothing out of sample was read, nothing ledgered", flush=True)
                return 4
            return 0
        if sel_path.is_file():
            try:
                old = json.loads(sel_path.read_text(encoding="utf-8"))["selection"]
                if old.get("read") != read_ids or old.get("sweep_sha1") != sweep_sha:
                    print(f"[group_final] WARNING: {sel_path.name} (from an earlier dry run) lists {old.get('read')} for sweep {old.get('sweep_sha1')}; "
                          f"this read is {read_ids} for sweep {sweep_sha}", flush=True)
            except (ValueError, KeyError):
                pass

        # ============================== the ledger, then phase 2: the out-of-sample read ==================================
        again = bool(args.again and prior_reads(root, fid, tag))
        what = f"group sweep {tag}{' (AGAIN: a repeat read)' if again else ''}: rulers + per-group picks by the fixed rule on train/valid, with carriers and twins ({', '.join(read_ids)})"
        Ledger(root / "runs" / fid / "ledger.json").record("holdout", len(read_ids), what, f"group_final_{tag}")
        if fw is not None:
            Ledger(root / "runs" / "_forward" / "ledger.json").record(
                "forward", len(read_ids), f"{fid} group sweep {tag}{' (AGAIN)' if again else ''}, forward column {dates[fw.start]}..{dates[fw.stop - 1]}: {', '.join(read_ids)}",
                f"group_final_{fid}_{tag}")
        tgt = np.asarray(ps.target(1), dtype=np.float64)
        years_arr = np.asarray(ps.years)
        yrs = {nm: float(np.isfinite(tgt[s]).any(1).sum()) / 252.0 for nm, s in (("utrain", us), ("holdout", ho), ("oos", oos))}
        yrs["forward"] = None if fw is None else float(np.isfinite(tgt[fw]).any(1).sum()) / 252.0
        span = {"utrain": us, "holdout": ho, "forward": fw, "oos": oos}
        mods_read = [k for k in read_ids if info[k]["role"] == "modification"]
        need_held = set(mods_read) | {R[k]["base"] for k in mods_read}
        held = {conv: {} for conv in CONVS}
        results, series = {}, {}
        for k in read_ids:
            raw, pr, v = np.asarray(P[k], dtype=np.float64), prep[k], R[k]
            entry = {"expr": v["expr"], "kind": v["kind"], "why": v.get("why", ""), "role": info[k]["role"], "group": group_of[k], "sign_user": pr["sign"],
                     "base": v.get("base"), "twin": twin_of(R, k) if k in selected else None, "needed_by": info[k]["needed_by"],
                     "sign_locked": pr["sign_locked"], "sign_by": pr["sign_by"],
                     "sign_ic_utrain": pr["sign_ic_utrain"], "sign_flip": bool(pr["sign"] != pr["sign_ic_utrain"]),
                     "fit": {"hl_long": pr["fit"]["hl_long"], "hl_ls": pr["fit"]["hl_ls"], "grid": pr["fit"]["sweep"]},
                     "exposure": pr["expo"], "corr_orig": v.get("corr_orig"), "corr_known": v.get("corr_known"), "conv": {}}
            series[k] = {}
            for conv, hl in (("fitted", pr["hl_fit"]), ("fixed", float(args.fixed_hl))):
                sm = bk.smoothed(pr["sign"] * raw, hl)
                books = {nm: bk.book_row(sm, tgt, s) for nm, s in span.items() if s is not None}
                nets = {nm: bk.long_book(long_short_weights(sm[s], bk.TOP_FRAC), sm[s], tgt[s])[0] for nm, s in (("utrain", us), ("holdout", ho), ("forward", fw)) if s is not None}
                nets["oos"] = np.concatenate([nets["holdout"], nets["forward"]]) if fw is not None else nets["holdout"]
                by = {}
                for y in sorted(set(years_arr)):
                    d = np.nonzero(years_arr == y)[0]
                    s = slice(int(d[0]), int(d[-1]) + 1)
                    with warnings.catch_warnings():
                        warnings.simplefilter("ignore", RuntimeWarning)
                        by[str(y)] = float(np.nanmean(bk.long_book(long_short_weights(sm[s], bk.TOP_FRAC), sm[s], tgt[s])[0]) * 252)
                if k in need_held:
                    held[conv][k] = long_mask(sm)
                entry["conv"][conv] = {"hl": hl, "books": books, "by_year_long_net": by}
                series[k][conv] = nets
            results[k] = entry
        # in-sample numbers of the read must be the ones phase 1 found (same half-life fit, same book): a cheap internal consistency check
        for k in read_ids:
            a, b = results[k]["conv"]["fitted"]["books"]["utrain"], prep[k]["utrain_row"]
            if not same_number(a["long_ann"], b["long_ann"]) or not same_number(a["long_sharpe"], b["long_sharpe"]):
                raise SystemExit(f"[group_final] internal inconsistency for {k}: in-sample net excess {a['long_ann']} / Sharpe {a['long_sharpe']} (read) "
                                 f"vs {b['long_ann']} / {b['long_sharpe']} (phase 1)")
        # how much of its carrier's top-decile book a modification changes: 1 - the overlap of the two books
        for k in mods_read:
            results[k]["changed_share"] = {}
            for conv in CONVS:
                by_day = book_overlap_by_day(held[conv][k], held[conv][R[k]["base"]])
                results[k]["changed_share"][conv] = {"in_sample": 1.0 - float(nanmean_quiet(by_day[us])), "oos": 1.0 - float(nanmean_quiet(by_day[oos]))}
        # the paired differences: against every --pair object for everything read, against its base for a modification, against its twin for a parent
        refs_of = {k: [] for k in read_ids}
        always_refs = list(dict.fromkeys(list(pair_ids) + [KNOWN_ID] + ([SIZE_ID] if SIZE_ID in info else [])))       # the verdicts are defined against these two, whatever --pair says
        for k in read_ids:
            refs_of[k] += [r for r in always_refs if r != k]
            if info[k]["role"] in ("modification", "ruler") and R[k].get("base"):
                refs_of[k].append(R[k]["base"])
            if k in selected and twin_of(R, k) in info:
                refs_of[k].append(twin_of(R, k))
        paired = {}
        for k, refs in refs_of.items():
            for ref in dict.fromkeys(refs):
                paired.setdefault(ref, {})[k] = {conv: {p: paired_stats(series[k][conv][p], series[ref][conv][p]) for p in PERIODS if p in series[k][conv]} for conv in CONVS}
        verdicts = {}
        for k in read_ids:
            role = info[k]["role"]
            ref = R[k]["base"] if role == "modification" else ((R[k].get("base") or KNOWN_ID) if role in ("standalone", "ruler") else None)
            tw = twin_of(R, k) if k in selected and twin_of(R, k) in info else None
            js = {}
            for conv in CONVS:
                get = lambda r: paired.get(r, {}).get(k, {}).get(conv) if r and r != k else None            # noqa: E731
                js[conv] = judge_convention(k, role, ref, get(ref), get(KNOWN_ID), get(SIZE_ID), results[k]["conv"][conv]["books"]["oos"],
                                            is_size=prep[k]["expo"]["is_size"], pair_twin=get(tw))
            verdicts[k] = combine_conventions(js["fitted"], js["fixed"], results[k]["conv"]["fitted"]["hl"], results[k]["conv"]["fixed"]["hl"])
        # the multiplicity pass over the selected hypotheses' verdicts
        evidence = {k: series[k]["fixed"]["utrain"] - series[verdicts[k]["ref"]]["fixed"]["utrain"] for k in selected}

        def distinct(a, b):
            """Two picks of one group: of the same kind they were both kept by the walk (distinct by its own measure); a standalone and
            a modification are distinct unless the in-sample daily differences their verdicts rest on correlate at >= --distinct."""
            if info[a]["role"] == info[b]["role"]:
                return True
            c = series_corr(evidence[a], evidence[b])
            return not (c == c and c >= args.distinct)

        multi = apply_multiplicity({k: {"group": info[k]["group"], "label": verdicts[k]["final_paired"], "t": verdicts[k]["fixed"]["vs_ref"]["t_oos"]} for k in selected
                                    if verdicts[k]["fixed"]["vs_ref"]}, distinct)
        for k, m in multi.items():
            verdicts[k]["final"] = m["label"]
            if m["note"]:
                verdicts[k]["notes"].append(m["note"])
        mem.stop()

    out = {"factor_id": fid, "sweep": tag, "rule": __doc__.split("    python")[0].strip(), "when": time.strftime("%Y-%m-%dT%H:%M:%S"),
           "args": {"per_group": args.per_group, "distinct": args.distinct, "fixed_hl": args.fixed_hl, "groups": groups, "pair": pair_ids, "again": bool(args.again),
                    "end": end, "tol_ann": args.tol_ann, "tol_sharpe": args.tol_sharpe},
           "sweep_ref": sweep_ref, "view": {"start": str(dates[0]), "end": str(dates[-1]), "n_days": len(dates), "n_symbols": len(ps.symbols)},
           "periods": per, "years": yrs, "selection": selection, "roles": info, "repro": repro, "results": results, "paired": paired, "verdicts": verdicts,
           "dates": {nm: [str(d) for d in dates[s]] for nm, s in (("utrain", us), ("holdout", ho), ("forward", fw)) if s is not None},
           "series": {k: {conv: {p: _series(x) for p, x in nets.items() if p != "oos"} for conv, nets in v.items()} for k, v in series.items()}}
    out_p = root / "runs" / fid / f"group_final_{tag}.json"
    out_p.parent.mkdir(parents=True, exist_ok=True)
    out_p.write_text(json.dumps(clean(out), ensure_ascii=False, indent=1, allow_nan=False), encoding="utf-8")
    print("\n" + render_results(out, groups))
    print(f"\nwrote {out_p} ({time.time() - t0:.0f}s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
