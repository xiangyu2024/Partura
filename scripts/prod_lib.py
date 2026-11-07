"""PROD W01: the library construction of scripts/c08_final.py, as functions (research/prod_W01/PLAN.md section 1).

No GPU, no engine, no panels: evidence files in, lists of heads out; the numeric steps (rank correlation, z-rank, neutralisation) are
passed in, so the logic is testable on small synthetic inputs.  c08_final.py is NOT changed and does not import this; the logic here is
the same, line for line, with three differences that come from the design of PROD:
  * the main AlphaCube is the study's own (episodes ``prods<seed>M<batch>``), missions are ``prods<seed>Pr<round><a|b>``;
  * there is no A arm;
  * the whole wave gets a library too (:func:`wave_library`).

Library of a seed (c08_final.py / C05 PLAN section 3):
    M   = the heads of M batches 1..4
    P   = M's heads and Partura's extra heads (missions of rounds 1..3 in round, then slot order; each round's R accessions after its
          missions), every head an R replacement stands in for replaced by the END of its replacement chain (role + "+R")
    both greedily deduplicated in that order: dropped when |rho| with the known family >= 0.5, or rho >= 0.7 / <= -0.5 with a head already
    kept, or the same expression twice.
"""
import glob
import json
from pathlib import Path

import yaml

RHO_KNOWN, RHO_HEAD, RHO_ANTI = 0.5, 0.7, -0.5
ROUNDS = (1, 2, 3)
BATCHES = (1, 2, 3, 4)


def chain_end(rep, expr):
    """The replacement row at the end of the chain expr -> v1 -> v2 ... (PLAN revision 13 of C05); None if expr is not replaced."""
    if expr not in rep:
        return None
    r, seen = rep[expr], {expr}
    while r["expr"] in rep and r["expr"] not in seen:
        seen.add(r["expr"])
        r = rep[r["expr"]]
    return r


def apply_replacements(heads, rep):
    """Replace every head that has a replacement by the end of its chain (keys of the replacement row override; role gets "+R")."""
    out = []
    for h in heads:
        r = chain_end(rep, h["expr"])
        if r is not None:
            h = {**h, **{k: r[k] for k in ("expr", "sign", "hl", "score", "train", "valid")}, "replaced": h["expr"], "role": h["role"] + "+R"}
        out.append(h)
    return out


def slot_types(plan):
    """{"a": type, "b": type} of a round's plan; a slot the audit turned into plain GP is "N0"."""
    return {j: "N0" if sl.get("audit_failed") else sl["type"] for j, sl in zip("ab", (plan or {}).get("slots", []))}


def seed_library(S, ep_dir, study_dir, c05_lib, pfx="prod"):
    """One seed's M and P libraries (before dedup) and the bookkeeping of the read.

    ep_dir = episodes/, study_dir = research/<study>/ (arms/, loc/).  c05_lib = scripts/c05_lib.py (heads / evidence of a finished run).
    -> {"M": [...], "P": [...], "missions": [...], "evals": {"M", "P"}, "gpu_seconds": {"M", "P"}, "replacements": {head: row}}
    """
    ep_dir, D = Path(ep_dir), Path(study_dir)
    m_eps = [ep_dir / f"{pfx}s{S}M{e}_I0_open_search" for e in BATCHES]
    evals, gpu, miss = {"M": 0, "P": 0}, {"M": 0.0, "P": 0.0}, []
    for ep in m_eps:
        for A in c05_lib.evidence(ep)["arms"].values():
            gpu["M"] += A["seconds"]
            evals["M"] += A["scored"]
    m_lib = [{**h, "role": "M"} for h in c05_lib.heads(m_eps)]
    rep, extra = {}, []
    for k in ROUNDS:
        f = D / "arms" / f"s{S}_P_r{k}_R.json"
        adds = []
        if f.is_file():
            R = json.loads(f.read_text(encoding="utf-8"))
            rep.update({r["head"]: r for r in R["replacements"]})
            adds = [{**x, "role": "R+", "mission": f.name, "round": k} for x in R.get("additions", [])]
            evals["P"] += R["paid"]
        pf = D / "arms" / f"s{S}_P_r{k}.yaml"
        types = slot_types(yaml.safe_load(pf.read_text(encoding="utf-8")) if pf.is_file() else {"slots": []})
        for pth in sorted(glob.glob(str(ep_dir / f"{pfx}s{S}Pr{k}[ab]_*"))):
            ep = Path(pth)
            j = ep.name.split("_")[0][-1]
            if not (ep / "evidence.json").is_file():
                miss.append({"seed": S, "round": k, "slot": j, "type": "failed", "scored": 0, "heads": 0})
                continue
            for A in c05_lib.evidence(ep)["arms"].values():
                gpu["P"] += A["seconds"]
                evals["P"] += A["scored"]
                miss.append({"seed": S, "round": k, "slot": j, "type": types.get(j, "?"), "scored": A["scored"], "heads": len(A.get("heads", []))})
            extra += [{**h, "role": types.get(j, "?"), "mission": ep.name, "round": k} for h in c05_lib.heads([ep])]
        extra += adds
        lf = D / "loc" / f"s{S}_P_r{k}.json"
        if lf.is_file():
            evals["P"] += json.loads(lf.read_text(encoding="utf-8"))["paid"]
    p_lib = apply_replacements(m_lib + extra, rep)
    return {"M": m_lib, "P": p_lib, "missions": miss, "evals": evals, "gpu_seconds": gpu, "replacements": rep}


def dedup(lst, Z, RK, rho, rho_known=RHO_KNOWN, rho_head=RHO_HEAD, rho_anti=RHO_ANTI):
    """Greedy, in order (C05 PLAN section 3).  Z[expr] = the head's traded residual ranks (train, every 5th day), RK[expr] = its rank
    correlation with the known family, rho(a, b) = mean daily rank correlation.  Expressions without a panel (not in Z) are dropped."""
    kept = []
    for h in lst:
        e = h["expr"]
        if e not in Z or abs(RK[e]) >= rho_known or any(x["expr"] == e for x in kept):
            continue
        rs = [rho(Z[e], Z[x["expr"]]) for x in kept]
        if all(rho_anti < r < rho_head for r in rs):
            kept.append(h)
    return kept


def wave_library(per_seed, Z, RK, rho, **kw):
    """The whole wave's library: the per-seed libraries (already deduplicated within a seed) pooled and deduplicated again ACROSS seeds,
    greedily in descending in-sample score (ties: seed, then expression) -- the order uses only train / valid numbers.  Every head
    keeps its seed.  per_seed = {seed: [head, ...]}."""
    pool = [{**h, "seed": S} for S in sorted(per_seed) for h in per_seed[S]]
    pool.sort(key=lambda h: (-(h["score"] if h.get("score") is not None else float("-inf")), h["seed"], h["expr"]))
    return dedup(pool, Z, RK, rho, **kw)


def fuse(exprs, SM, zrank, neutralize=None):
    """Equal-weight z-rank fusion of the traded signals SM[expr] (days x stocks), averaged over the heads that have a value that day,
    then (if ``neutralize``) neutralised once more like every single head (C08 PLAN section 3).  None for an empty library."""
    import numpy as np
    if not exprs:
        return None
    acc = np.zeros(SM[exprs[0]].shape, np.float64)
    cnt = np.zeros(acc.shape, np.int32)
    for e in exprs:
        z = zrank(SM[e].astype(np.float64))
        ok = np.isfinite(z)
        acc += np.where(ok, z, 0.0)
        cnt += ok
    with np.errstate(invalid="ignore", divide="ignore"):
        out = np.where(cnt > 0, acc / np.maximum(cnt, 1), np.nan)
    if neutralize is not None:
        out = neutralize(out)
    return out


def head_row(h):
    """The fields of a head that go to library.json (in-sample numbers only)."""
    return {k: h.get(k) for k in ("seed", "expr", "role", "mission", "round", "score", "train", "valid", "sign", "hl", "replaced", "reproduces", "rho_known")}
