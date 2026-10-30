"""C08: the read (research/coldstart_C08/PLAN.md §3) under C07's rule (rank first, EMA, residual on the 16-column non-linear basis --
source tmp/c08_env.sh).  New server, after every seed's rounds have ended and the old server's C08 runs have been copied here.

Libraries: M = C07's M batches 1..4; A = C07's M then C07's A rounds 1..3; P = C07's M heads (with P's R replacements, chains followed)
then P's extra heads of rounds 1..3 (each round's R additions after its missions).  Greedy dedup as C05 §3; the fused book is
neutralised once more like every single head (PLAN §3).  PRIMARY: P against A over the 8 paired seeds, one-sided Wilcoxon (alpha 0.05).
The test period is a development set (PLAN §4): nothing here is ledgered as a confirmatory read; --confirm reads data after 2026-09-16.

    python scripts/c08_final.py [--dry-run] [--gpu-fraction 0.9]     -> research/coldstart_C08/final.json (final_dry.json)
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
D7, D, EP = PARTURA_ROOT / "research" / "coldstart_C07", PARTURA_ROOT / "research" / "coldstart_C08", PARTURA_ROOT / "episodes"
LEDGER = D / "ledger_c08.json"
SEEDS, XS = [int(x) for x in os.environ.get("C08_SEEDS", "801,802,803,804,805,806,807,808").split(",")], ("A", "P")
if not steer.rank_first() or os.environ.get("PARTURA_NEUTRAL_POWERS") != "1,2,3":
    raise SystemExit("C08 is read under C07's rule: source tmp/c08_env.sh")
if not DRY and len(SEEDS) != 8:
    raise SystemExit("the real read covers all 8 seeds")
T_LINE, RHO_KNOWN, RHO_HEAD, RHO_ANTI = 2.0, 0.5, 0.7, -0.5
STORE = os.environ.get("PARTURA_STORE", "/root/autodl-tmp/qmt_daily_data/fast_factor_compute")
MIRROR = os.environ.get("PARTURA_MIRROR", "/root/autodl-tmp/AlphaCube/mirror")
MIRROR = MIRROR if MIRROR and os.path.isdir(MIRROR) else None
DEV = argv[argv.index("--dev") + 1] if "--dev" in argv else None
FUSE_NEUTRAL = "--no-fuse-neutral" not in argv              # C08 PLAN §3: the fused book is neutralised by default   # PLAN revision 1: the test period as a development set -- a library
# from research/coldstart_C07/<DEV>/s<seed>_train.yaml stands in for V_tr; nothing is ledgered, the official verdict is untouched
if DEV and DRY:
    raise SystemExit("--dev reads the test period as a development set; it does not combine with --dry-run")
if not DRY and not DEV and Ledger(LEDGER).summary().get("holdout"):
    raise SystemExit(f"C08's read has already been made ({LEDGER}); it happens once")


LIB, GPUSEC, EVALS, DROP = {}, {"M": 0.0, "A": 0.0, "P": 0.0}, {"M": 0, "A": 0, "P": 0}, {}
MISS = []
for S in SEEDS:
    m_eps = [EP / f"c07s{S}M{e}_I0_open_search" for e in range(1, 5)]
    a_eps = [Path(p) for k in (1, 2, 3) for p in sorted(glob.glob(str(EP / f"c07s{S}Ar{k}[ab]_*")))]
    for X, eps in (("M", m_eps), ("A", a_eps)):
        for ep in eps:
            for A_ in c05_lib.evidence(ep)["arms"].values():
                GPUSEC[X] += A_["seconds"]
                EVALS[X] += A_["scored"]
    LIB[(S, "M")] = [{**h, "role": "M"} for h in c05_lib.heads(m_eps)]
    cand, seen = [], set()
    for h in c05_lib.heads(m_eps) + c05_lib.heads(a_eps):
        if h["expr"] not in seen:
            seen.add(h["expr"])
            cand.append({**h, "role": "M" if "M" in h["src"].split("_")[0][-2:] else "A"})
    LIB[(S, "A")] = cand
    rep_, extra = {}, []
    for k in (1, 2, 3):
        f = D / "arms" / f"s{S}_P_r{k}_R.json"
        adds = []
        if f.is_file():
            R = json.loads(f.read_text(encoding="utf-8"))
            rep_.update({r["head"]: r for r in R["replacements"]})
            adds = [{**x, "role": "R+", "mission": f.name, "round": k} for x in R.get("additions", [])]
            EVALS["P"] += R["paid"]
        plan = yaml.safe_load((D / "arms" / f"s{S}_P_r{k}.yaml").read_text(encoding="utf-8")) if (D / "arms" / f"s{S}_P_r{k}.yaml").is_file() else {"slots": []}
        types = {j: "N0" if sl.get("audit_failed") else sl["type"] for j, sl in zip("ab", plan["slots"])}
        for pth in sorted(glob.glob(str(EP / f"c08s{S}Pr{k}[ab]_*"))):
            ep = Path(pth)
            j = ep.name.split("_")[0][-1]
            if not (ep / "evidence.json").is_file():
                MISS.append({"seed": S, "round": k, "slot": j, "type": "failed", "scored": 0, "heads": 0})
                continue
            for A_ in c05_lib.evidence(ep)["arms"].values():
                GPUSEC["P"] += A_["seconds"]
                EVALS["P"] += A_["scored"]
                MISS.append({"seed": S, "round": k, "slot": j, "type": types.get(j, "?"), "scored": A_["scored"], "heads": len(A_.get("heads", []))})
            extra += [{**h, "role": types.get(j, "?"), "mission": ep.name, "round": k} for h in c05_lib.heads([ep])]
        extra += adds
        lf = D / "loc" / f"s{S}_P_r{k}.json"
        if lf.is_file():
            EVALS["P"] += json.loads(lf.read_text(encoding="utf-8"))["paid"]
    base = []
    for h in LIB[(S, "M")] + extra:
        if h["expr"] in rep_:
            r, seen_ = rep_[h["expr"]], {h["expr"]}
            while r["expr"] in rep_ and r["expr"] not in seen_:
                seen_.add(r["expr"])
                r = rep_[r["expr"]]
            h = {**h, **{k_: r[k_] for k_ in ("expr", "sign", "hl", "score", "train", "valid")}, "replaced": h["expr"], "role": h["role"] + "+R"}
        base.append(h)
    LIB[(S, "P")] = base
uniq = sorted({h["expr"] for v in LIB.values() for h in v})
print(f"[c08] libraries: {', '.join(f'{X} {sum(len(LIB[(S, X)]) for S in SEEDS)}' for X in ('M',) + XS)}; {len(uniq)} distinct expressions; "
      f"evaluations {EVALS}", flush=True)

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
    print(f"[c08] view {dates[0]}..{END}: test {ho.stop - ho.start} days ({years_ho:.2f} y), forward {fw.stop - fw.start} ({years_fw:.2f} y)", flush=True)

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
                print(f"[c08] does not compute on the full view: {e}", flush=True)
                continue
            sg, hl = sign_hl[e]
            sm = steer.neutral_residual(sg * bk.smoothed(steer.signal_input(P[f"c{j}"]), hl), QF)
            SM[e], Z[e] = sm.astype(np.float32), dg._zrank(sm)[:tr.stop:5]
        print(f"[c08] rebuilt {min(i + 16, len(uniq))}/{len(uniq)} ({time.time() - t0:.0f}s)", flush=True)
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
            out_ = np.where(cnt > 0, acc / np.maximum(cnt, 1), np.nan)
        if FUSE_NEUTRAL:                                   # development: the fused book neutralised like every single head
            out_ = steer.neutral_residual(out_, QF)
        return out_

    def book(fz, sl):
        if fz is None:
            return {"long_sharpe": 0.0, "long_ann": 0.0}
        r = bk.book_row(fz, tgt, sl)
        return {"long_sharpe": float(np.nan_to_num(r["long_sharpe"])), "long_ann": float(np.nan_to_num(r["long_ann"]))}

    out = {"plan": "research/coldstart_C08/PLAN.md", "missions": MISS, "dry_run": DRY, "view": [str(dates[0]), END], "years_test": years_ho, "years_forward": years_fw,
           "evaluations": EVALS, "gpu_seconds": GPUSEC, "libraries": {}, "per_seed": {},
           "fuse_neutral": FUSE_NEUTRAL}
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
    print(f"[c08] reproduce: {sum(h['reproduces'] for v in KEPT.values() for h in v)}/{sum(len(v) for v in KEPT.values())}", flush=True)

    if not DRY:
        n = len({h["expr"] for v in KEPT.values() for h in v})
        if not DEV:
            Ledger(LEDGER).record("holdout", n, "C07 libraries of M, A, V_tr, V_all: test period 20230808..20251231, by PLAN.md §3", "c07_final")
            Ledger(LEDGER).record("forward", n, f"C07 libraries: forward column 20260101..{END} (reported, not judged)", "c07_final")
        from scipy.stats import wilcoxon

        def compare(x, y, sl="test"):
            d = [out["per_seed"][str(S)][x][sl]["long_sharpe"] - out["per_seed"][str(S)][y][sl]["long_sharpe"] for S in SEEDS]
            nz = [v for v in d if v != 0]
            up = float(wilcoxon(nz, alternative="greater").pvalue) if len(nz) >= 5 else float("nan")
            dn = float(wilcoxon(nz, alternative="less").pvalue) if len(nz) >= 5 else float("nan")
            return {"diffs": d, "median": float(np.median(d)), "p_better": up, "p_worse": dn, "wins": sum(v > 0 for v in d), "losses": sum(v < 0 for v in d)}

        out["primary"] = p = compare("P", "A")
        out["verdict_primary"] = "P 更好" if (p["p_better"] < 0.05 and p["median"] > 0) else "P 更差" if (p["p_worse"] < 0.05 and p["median"] < 0) else "分不出"
        out["secondary"] = {"P_vs_A_forward": compare("P", "A", "forward"), "A_vs_M": compare("A", "M"), "P_vs_M": compare("P", "M")}
        heads = []                                              # P's added heads (extra, R replacements, R additions), each on its own
        for S in SEEDS:
            for h in LIB[(S, "P")]:
                if (h["role"] in ("M",) and not h.get("replaced")) or h["expr"] not in SM:
                    continue
                sm = SM[h["expr"]].astype(np.float64)
                r, rf = bk.book_row(sm, tgt, ho), bk.book_row(sm, tgt, fw)
                heads.append({"seed": S, "role": h["role"], "mission": h.get("mission"), "round": h.get("round"), "expr": h["expr"], "train": h["train"],
                              "valid": h["valid"], "test_sharpe": float(np.nan_to_num(r["long_sharpe"])), "forward_sharpe": float(np.nan_to_num(rf["long_sharpe"]))})
        out["extra_heads"] = heads
        print(f"PRIMARY: median P-A {p['median']:+.2f}, p(P better) {p['p_better']:.3f}, p(P worse) {p['p_worse']:.3f} -> {out['verdict_primary']}", flush=True)
    mem.stop()

out["seconds"] = time.time() - t0
(D / ("final_dry.json" if DRY else f"final_dev_{DEV}{'_fn' if FUSE_NEUTRAL else ''}.json" if DEV else "final.json")).write_text(json.dumps(out, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
for S in SEEDS:
    r = out["per_seed"][str(S)]
    print(f"  s{S}: " + "  ".join(f"{X} {r[X]['heads']}h tr {r[X]['train']['long_sharpe']:+.2f} va {r[X]['valid']['long_sharpe']:+.2f}"
                                    + ("" if DRY else f" te {r[X]['test']['long_sharpe']:+.2f}") for X in ("M",) + XS))
print(f"wrote {D / ('final_dry.json' if DRY else f'final_dev_{DEV}' + ('_fn' if FUSE_NEUTRAL else '') + '.json' if DEV else 'final.json')} ({out['seconds']:.0f}s)")
