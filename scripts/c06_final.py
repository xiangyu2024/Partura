"""C06: the one out-of-sample read, by the rule written before any run (research/coldstart_C06/PLAN.md §3).  New server, after every
seed's rounds have ended and the old server's C06 files have been copied here (scripts/c06_gather.sh).

Libraries, exactly as C05 (research/coldstart_C05/PLAN.md §3): L_X(s) = M's heads of batches 1..4 (with X's R replacements, chains
followed) then X's extra heads of rounds 1..3 (in round, then slot order; C06's R additions after their round's missions); greedy
dedup (|rho known| >= 0.5, rho >= 0.7 or <= -0.5 with a head kept); every head rebuilt on the full view as its reward traded it.
Arms: M, A and B5 are C05's runs (M batches c05s<seed>M<e>, A c05s<seed>Ar..., B5 = C05's B c05s<seed>Br... with C05's R files);
C is C06's (c06s<seed>Cr..., research/coldstart_C06/arms).  PRIMARY: C against A over the 8 paired seeds, one-sided Wilcoxon
(alpha 0.05) on the test-period net Sharpe of the fused book.  Secondary: C vs B5; forward; C's added heads by mission type;
the auditor's calibration (research/coldstart_C06/calib.json: accepted against rejected seed expressions, each read as a factor of
its own with its direction and half-life chosen in sample).

    python scripts/c06_final.py [--dry-run] [--gpu-fraction 0.9]     -> research/coldstart_C06/final.json (final_dry.json)
--dry-run: libraries, in-sample books, the reproduction check and the calibration's in-sample choices only; nothing out of sample.
"""
import glob
import json
import math
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.guard import MemoryGuard, limit_threads, slot  # noqa: E402

limit_threads(8)
import numpy as np  # noqa: E402
import yaml  # noqa: E402

from partura import books as bk  # noqa: E402
from partura import diagnose as dg  # noqa: E402
from partura import ops_ext  # noqa: E402,F401
from partura import steer  # noqa: E402
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.panels import SHARED_CACHE, PanelSet  # noqa: E402
from partura.splits import Ledger  # noqa: E402

sys.path.insert(0, str(PARTURA_ROOT / "scripts"))
import c05_lib  # noqa: E402

argv = sys.argv[1:]
DRY = "--dry-run" in argv
os.environ.setdefault("PARTURA_REPROMOTE", "1")                # PLAN revision 7
GPU = float(argv[argv.index("--gpu-fraction") + 1]) if "--gpu-fraction" in argv else 0.4
D5, D, EP = PARTURA_ROOT / "research" / "coldstart_C05", PARTURA_ROOT / "research" / "coldstart_C06", PARTURA_ROOT / "episodes"
LEDGER = D / "ledger_c06.json"
SEEDS, XS = [int(x) for x in os.environ.get("C06_SEEDS", "801,802,803,804,805,806,807,808").split(",")], ("A", "B5", "C")
SRC = {"A": (D5, "c05", "A"), "B5": (D5, "c05", "B"), "C": (D, "c06", "C")}    # where each arm's files and runs are
if not DRY and len(SEEDS) != 8:
    raise SystemExit("the real read covers all 8 seeds")
T_LINE, RHO_KNOWN, RHO_HEAD, RHO_ANTI = 2.0, 0.5, 0.7, -0.5
STORE = os.environ.get("PARTURA_STORE", "/root/autodl-tmp/qmt_daily_data/fast_factor_compute")
MIRROR = os.environ.get("PARTURA_MIRROR", "/root/autodl-tmp/AlphaCube/mirror")
MIRROR = MIRROR if MIRROR and os.path.isdir(MIRROR) else None
if not DRY and Ledger(LEDGER).summary().get("holdout"):
    raise SystemExit(f"the test period of C06 has already been read ({LEDGER}); this read happens once")


def slot_types(S, X, k):
    if X == "A":
        return {"a": "A", "b": "A"}
    d, _, x = SRC[X]
    f = d / "arms" / f"s{S}_{x}_r{k}.yaml"
    plan = yaml.safe_load(f.read_text(encoding="utf-8")) if f.is_file() else {"slots": []}
    if X == "C":                                               # a slot the audit turned into a plain GP is N0 (C06 PLAN §2.5)
        return {j: "N0" if s.get("audit_failed") else s["type"] for j, s in zip("ab", plan["slots"])}
    return {j: s["type"] for j, s in zip("ab", plan["slots"])}


LIB, MISS, GPUSEC, EVALS = {}, [], {}, {}
for S in SEEDS:
    m_eps = [EP / f"c05s{S}M{e}_I0_open_search" for e in range(1, 5)]
    LIB[(S, "M")] = [{**h, "role": "M"} for h in c05_lib.heads(m_eps)]
    for X in XS:
        rep, extra = {}, []
        d, pfx, x = SRC[X]
        for k in (1, 2, 3):
            f = d / "arms" / f"s{S}_{x}_r{k}_R.json"
            adds = []
            if f.is_file():
                R = json.loads(f.read_text(encoding="utf-8"))
                rep.update({r["head"]: r for r in R["replacements"]})
                adds = [{**a, "role": "R+", "mission": f.name, "round": k} for a in R.get("additions", [])]
                EVALS[X] = EVALS.get(X, 0) + R["paid"]
            types = slot_types(S, X, k)
            for p in sorted(glob.glob(str(EP / f"{pfx}s{S}{x}r{k}[ab]_*"))):
                ep = Path(p)
                if not (ep / "evidence.json").is_file():          # failed twice: budget spent, nothing produced (PLAN revision 6)
                    MISS.append({"seed": S, "arm": X, "round": k, "slot": ep.name.split("_")[0][-1], "type": "failed", "scored": 0, "heads": 0})
                    continue
                j = ep.name.split("_")[0][-1]
                E = c05_lib.evidence(ep)
                for arm, A_ in E["arms"].items():
                    GPUSEC[X] = GPUSEC.get(X, 0.0) + A_["seconds"]
                    EVALS[X] = EVALS.get(X, 0) + A_["scored"]
                    MISS.append({"seed": S, "arm": X, "round": k, "slot": j, "type": types.get(j, "?"), "core": (E.get("c05") or {}).get("core"),
                                 "scored": A_["scored"], "heads": len(A_.get("heads", [])), "sampling": A_.get("sampling")})
                extra += [{**h, "role": types.get(j, "?"), "mission": ep.name, "round": k} for h in c05_lib.heads([ep])]
            extra += adds
            lf = d / "loc" / f"s{S}_{x}_r{k}.json"
            if X != "A" and lf.is_file():
                EVALS[X] = EVALS.get(X, 0) + json.loads(lf.read_text(encoding="utf-8"))["paid"]
        base = []
        for h in LIB[(S, "M")] + extra:
            if h["expr"] in rep:
                r, seen = rep[h["expr"]], {h["expr"]}
                while r["expr"] in rep and r["expr"] not in seen:     # PLAN revision 13: a chain of replacements ends at its last link
                    seen.add(r["expr"])
                    r = rep[r["expr"]]
                h = {**h, **{k_: r[k_] for k_ in ("expr", "sign", "hl", "score", "train", "valid")}, "replaced": h["expr"], "role": h["role"] + "+R"}
            base.append(h)
        LIB[(S, X)] = base
for S in SEEDS:
    GPUSEC["M"] = GPUSEC.get("M", 0.0) + sum(c05_lib.evidence(EP / f"c05s{S}M{e}_I0_open_search")["arms"]["control"]["seconds"] for e in range(1, 5))
uniq = sorted({h["expr"] for v in LIB.values() for h in v})
CAL = json.loads((D / "calib.json").read_text(encoding="utf-8")) if (D / "calib.json").is_file() else []
cal_exprs = sorted({c["expr"] for c in CAL} - set(uniq))
print(f"[c06] libraries: {', '.join(f'{X} {sum(len(LIB[(S, X)]) for S in SEEDS)}' for X in ('M',) + XS)}; {len(uniq)} distinct expressions; "
      f"evaluations {EVALS}; calibration {len(CAL)} rows ({len(cal_exprs)} more expressions)", flush=True)

with slot():
    mem = MemoryGuard(self_limit_gb=int(os.environ.get("PARTURA_SELF_LIMIT_GB", 60)), cgroup_limit_gb=int(os.environ.get("PARTURA_CGROUP_LIMIT_GB", 80))).start()
    t0 = time.time()
    from alphacube.plugins import load_plugins
    from alphacube.store import open_cube_store
    load_plugins(["partura.ac_plugin"])
    END = str(open_cube_store(STORE, mirror_root=MIRROR).dates[-1])
    ps = PanelSet(STORE, "20180102", END, warmup=60, device="cuda", gpu_fraction=GPU, cache_dir=str(SHARED_CACHE), mirror_root=MIRROR,
                  workdir=str(PARTURA_ROOT / "tmp"), label_kind="open_vwap15", label_buyable=True, batch=8,
                  daily_root=os.environ.get("PARTURA_DAILY_ROOT") or None)
    G = steer.Guidance.load(PARTURA_ROOT / "guidance" / "C05_base.yaml")
    known_spec = G.spec["pool"][0]
    aux = ps.compute({"known": known_spec["expr"], "liq": "cross_mean(day_sum(Amt), 30)", "vol": "cross_mean(day_std(Ret), 20)",
                      "rev": "div(day_last(Close), ts_delay(day_last(Close), 20))", "size": "LogFloatCap"})
    tgt = ps.target(1)
    dates = np.asarray(ps.dates).astype(str)
    ix = lambda d: int(np.searchsorted(dates, d))                       # noqa: E731
    tr, va = slice(0, ix("20220101")), slice(ix("20220101"), ix("20230808"))
    ho, fw = slice(ix("20230808"), ix("20260101")), slice(ix("20260101"), len(dates))
    years_ho = float(np.isfinite(tgt[ho]).any(1).sum()) / 252.0
    years_fw = float(np.isfinite(tgt[fw]).any(1).sum()) / 252.0
    kz = dg._zrank(float(known_spec["sign"]) * np.asarray(aux["known"], np.float64))[:tr.stop:5]
    QF = steer.neutral_basis([aux["liq"], aux["vol"], aux["rev"], aux["known"], aux["size"]])
    print(f"[c06] view {dates[0]}..{END}: test {ho.stop - ho.start} days ({years_ho:.2f} y), forward {fw.stop - fw.start} ({years_fw:.2f} y)", flush=True)

    def rho(a, b):
        ok = np.isfinite(a) & np.isfinite(b)
        x, y = np.where(ok, a, 0.0), np.where(ok, b, 0.0)
        n = np.maximum(ok.sum(1), 1)
        with np.errstate(invalid="ignore", divide="ignore"):
            c = ((x * y).sum(1) - x.sum(1) * y.sum(1) / n) / np.sqrt(((x ** 2).sum(1) - x.sum(1) ** 2 / n) * ((y ** 2).sum(1) - y.sum(1) ** 2 / n))
        return float(np.nanmean(c))

    sign_hl = {}
    for v in LIB.values():
        for h in v:
            sign_hl.setdefault(h["expr"], (float(h["sign"]), float(h["hl"])))
    SM, Z = {}, {}
    for i in range(0, len(uniq), 16):
        chunk = uniq[i:i + 16]
        P = ps.compute({f"c{j}": e for j, e in enumerate(chunk)})
        for j, e in enumerate(chunk):
            if f"c{j}" not in P:
                print(f"[c06] does not compute on the full view: {e}", flush=True)
                continue
            sg, hl = sign_hl[e]
            sm = steer.neutral_residual(sg * bk.smoothed(np.asarray(P[f"c{j}"], np.float64), hl), QF)
            SM[e], Z[e] = sm.astype(np.float32), dg._zrank(sm)[:tr.stop:5]
        print(f"[c06] rebuilt {min(i + 16, len(uniq))}/{len(uniq)} ({time.time() - t0:.0f}s)", flush=True)
    RK = {e: rho(Z[e], kz) for e in Z}

    def dedup(lst):
        kept = []
        for h in lst:
            e = h["expr"]
            if e not in Z or abs(RK[e]) >= RHO_KNOWN or any(x["expr"] == e for x in kept):
                continue
            rs = [rho(Z[e], Z[x["expr"]]) for x in kept]
            if all(RHO_ANTI < r < RHO_HEAD for r in rs):
                kept.append(h)
        return kept

    def fuse(lst):
        if not lst:
            return None
        acc = np.zeros(SM[lst[0]["expr"]].shape, np.float64)
        cnt = np.zeros(acc.shape, np.int32)
        for h in lst:
            z = dg._zrank(SM[h["expr"]].astype(np.float64))
            ok = np.isfinite(z)
            acc += np.where(ok, z, 0.0)
            cnt += ok
        with np.errstate(invalid="ignore", divide="ignore"):
            return np.where(cnt > 0, acc / np.maximum(cnt, 1), np.nan)

    def book(fz, sl):
        if fz is None:
            return {"long_sharpe": 0.0, "long_ann": 0.0}
        r = bk.book_row(fz, tgt, sl)
        return {"long_sharpe": float(np.nan_to_num(r["long_sharpe"])), "long_ann": float(np.nan_to_num(r["long_ann"]))}

    out = {"plan": "research/coldstart_C05/PLAN.md", "dry_run": DRY, "view": [str(dates[0]), END], "years_test": years_ho, "years_forward": years_fw,
           "evaluations": EVALS, "gpu_seconds": GPUSEC, "missions": MISS, "libraries": {}, "per_seed": {}}
    KEPT = {}
    for (S, X), lst in LIB.items():
        kept = dedup(lst)
        KEPT[(S, X)] = kept
        for h in kept:
            h["reproduces"] = bool(abs(bk.book_row(SM[h["expr"]].astype(np.float64), tgt, tr)["long_sharpe"] - h["train"]) < 0.05)
        fz = fuse(kept)
        row = {"heads": len(kept), "train": book(fz, tr), "valid": book(fz, va)}
        if not DRY:
            row.update(test=book(fz, ho), forward=book(fz, fw))
        out["per_seed"].setdefault(str(S), {})[X] = row
        out["libraries"].setdefault(str(S), {})[X] = [{k: h.get(k) for k in ("expr", "role", "mission", "round", "score", "train", "valid", "sign", "hl", "replaced", "reproduces")} for h in kept]
    print(f"[c06] reproduce: {sum(h['reproduces'] for v in KEPT.values() for h in v)}/{sum(len(v) for v in KEPT.values())}", flush=True)

    # the auditor's calibration (C06 PLAN §3): every accepted / rejected seed expression read as a factor of its own; direction and
    # half-life chosen in sample (the best min(train, valid) of the residual long book over sign +-1 and half-life 0 / 5 / 20)
    calib = []
    for i in range(0, len(cal_exprs), 16):
        chunk = cal_exprs[i:i + 16]
        P = ps.compute({f"q{j}": e for j, e in enumerate(chunk)})
        for j, e in enumerate(chunk):
            if f"q{j}" not in P:
                continue
            raw = np.asarray(P[f"q{j}"], np.float64)
            best = None
            for hl in (0.0, 5.0, 20.0):
                for sg in (1.0, -1.0):
                    sm = steer.neutral_residual(sg * bk.smoothed(raw, hl), QF)
                    tr_, va_ = book(sm, tr)["long_sharpe"], book(sm, va)["long_sharpe"]
                    if best is None or min(tr_, va_) > best[0]:
                        best = (min(tr_, va_), sg, hl, tr_, va_, sm)
            row = {"expr": e, "insample": best[0], "sign": best[1], "hl": best[2], "train": best[3], "valid": best[4]}
            if not DRY:
                row.update(test=book(best[5], ho)["long_sharpe"], forward=book(best[5], fw)["long_sharpe"])
            calib.append(row)
        print(f"[c06] calibration {min(i + 16, len(cal_exprs))}/{len(cal_exprs)} ({time.time() - t0:.0f}s)", flush=True)
    cal_by = {r["expr"]: r for r in calib}

    if not DRY:
        n = len({h["expr"] for v in KEPT.values() for h in v})
        Ledger(LEDGER).record("holdout", n, "C05 libraries of M, A, B0, B: test period 20230808..20251231, by PLAN.md §3", "c05_final")
        Ledger(LEDGER).record("forward", n, f"C05 libraries: forward column 20260101..{END} (reported, not judged)", "c05_final")
        from scipy.stats import wilcoxon

        def compare(x, y, sl="test"):
            d = [out["per_seed"][str(S)][x][sl]["long_sharpe"] - out["per_seed"][str(S)][y][sl]["long_sharpe"] for S in SEEDS]
            nz = [v for v in d if v != 0]
            up = float(wilcoxon(nz, alternative="greater").pvalue) if len(nz) >= 5 else float("nan")
            dn = float(wilcoxon(nz, alternative="less").pvalue) if len(nz) >= 5 else float("nan")
            return {"diffs": d, "median": float(np.median(d)), "p_better": up, "p_worse": dn, "wins": sum(v > 0 for v in d), "losses": sum(v < 0 for v in d)}

        out["primary"] = compare("C", "A")
        p = out["primary"]
        out["verdict_primary"] = "C 更好" if (p["p_better"] < 0.05 and p["median"] > 0) else "C 更差" if (p["p_worse"] < 0.05 and p["median"] < 0) else "分不出"
        out["secondary"] = {"C_vs_B5": compare("C", "B5"), "C_vs_A_forward": compare("C", "A", "forward"), "C_vs_B5_forward": compare("C", "B5", "forward"),
                            "delta": {X: [out["per_seed"][str(S)][X]["test"]["long_sharpe"] - out["per_seed"][str(S)]["M"]["test"]["long_sharpe"] for S in SEEDS] for X in XS}}
        heads = {}
        for (S, X), kept in KEPT.items():
            if X == "M":
                continue
            for h in kept:
                if h["role"] in ("M", "M+R") and not h.get("replaced"):
                    continue                                  # only what the arm added: extra heads and R replacements
                sm = SM[h["expr"]].astype(np.float64)
                r, rf = bk.book_row(sm, tgt, ho), bk.book_row(sm, tgt, fw)
                heads.setdefault(X, []).append({"seed": S, "role": h["role"], "mission": h.get("mission"), "expr": h["expr"], "score": h["score"],
                                                "test_ann": r["long_ann"], "test_sharpe": r["long_sharpe"], "test_t": r["long_sharpe"] * math.sqrt(years_ho),
                                                "forward_sharpe": rf["long_sharpe"],
                                                "valid_oos": bool(r["long_ann"] > 0 and r["long_sharpe"] * math.sqrt(years_ho) >= T_LINE)})
        out["extra_heads"] = heads
        out["valid_oos"] = {X: sum(h["valid_oos"] for h in v) for X, v in heads.items()}
        out["by_role"] = {X: {role: {"heads": sum(h["role"] == role for h in v), "valid_oos": sum(h["valid_oos"] for h in v if h["role"] == role),
                                     "mean_test_sharpe": float(np.mean([h["test_sharpe"] for h in v if h["role"] == role])) if any(h["role"] == role for h in v) else None}
                              for role in sorted({h["role"] for h in v})} for X, v in heads.items()}
        print(f"PRIMARY: median C-A {p['median']:+.2f}, p(C better) {p['p_better']:.3f}, p(C worse) {p['p_worse']:.3f} -> {out['verdict_primary']}", flush=True)
    out["calibration"] = [{**c, **{k: v for k, v in cal_by.get(c["expr"], {}).items() if k != "expr"}} for c in CAL]
    mem.stop()

out["seconds"] = time.time() - t0
(D / ("final_dry.json" if DRY else "final.json")).write_text(json.dumps(out, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
for S in SEEDS:
    r = out["per_seed"][str(S)]
    print(f"  s{S}: " + "  ".join(f"{X} {r[X]['heads']}h tr {r[X]['train']['long_sharpe']:+.2f} va {r[X]['valid']['long_sharpe']:+.2f}"
                                    + ("" if DRY else f" te {r[X]['test']['long_sharpe']:+.2f}") for X in ("M",) + XS))
print(f"wrote {D / ('final_dry.json' if DRY else 'final.json')} ({out['seconds']:.0f}s)")
