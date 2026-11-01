"""C07: the one out-of-sample read (research/coldstart_C07/PLAN.md §3), under the new rule: rank first, then EMA, then the residual on
the 16-column non-linear basis ($PARTURA_RANK_FIRST=1, $PARTURA_NEUTRAL_POWERS=1,2,3 -- source tmp/c07_env.sh).  New server, after every
seed's runs have ended, the old server's runs have been copied here and the verifier's decisions (research/coldstart_C07/verify/) are in.

Libraries: M = M batches 1..4; A = M then A rounds 1..3 (c05_lib.heads order); V_tr / V_all = A's candidates the verifier kept, same
order.  Greedy dedup and fusion as C05 §3.  PRIMARY: V_tr against A over the 8 paired seeds, one-sided Wilcoxon (alpha 0.05).

    python scripts/c07_final.py [--dry-run] [--gpu-fraction 0.9]     -> research/coldstart_C07/final.json (final_dry.json)
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
D, EP = PARTURA_ROOT / "research" / "coldstart_C07", PARTURA_ROOT / "episodes"
LEDGER = D / "ledger_c07.json"
SEEDS, XS = [int(x) for x in os.environ.get("C07_SEEDS", "801,802,803,804,805,806,807,808").split(",")], ("A", "Vtr", "Vall")
if not steer.rank_first() or os.environ.get("PARTURA_NEUTRAL_POWERS") != "1,2,3":
    raise SystemExit("C07 is read under the new rule: source tmp/c07_env.sh")
if not DRY and len(SEEDS) != 8:
    raise SystemExit("the real read covers all 8 seeds")
T_LINE, RHO_KNOWN, RHO_HEAD, RHO_ANTI = 2.0, 0.5, 0.7, -0.5
STORE = os.environ.get("PARTURA_STORE", "/root/autodl-tmp/qmt_daily_data/fast_factor_compute")
MIRROR = os.environ.get("PARTURA_MIRROR", "/root/autodl-tmp/AlphaCube/mirror")
MIRROR = MIRROR if MIRROR and os.path.isdir(MIRROR) else None
DEV = argv[argv.index("--dev") + 1] if "--dev" in argv else None
FUSE_NEUTRAL = "--fuse-neutral" in argv   # PLAN revision 1: the test period as a development set -- a library
# from research/coldstart_C07/<DEV>/s<seed>_train.yaml stands in for V_tr; nothing is ledgered, the official verdict is untouched
if DEV and DRY:
    raise SystemExit("--dev reads the test period as a development set; it does not combine with --dry-run")
if not DRY and not DEV and Ledger(LEDGER).summary().get("holdout"):
    raise SystemExit(f"the test period of C07 has already been read ({LEDGER}); this read happens once")


LIB, GPUSEC, EVALS, DROP = {}, {"M": 0.0, "A": 0.0}, {"M": 0, "A": 0}, {}
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
    for h in c05_lib.heads(m_eps) + c05_lib.heads(a_eps):     # the verifier's candidate list (c07_screen_prep.py): same order, ids from 1
        if h["expr"] not in seen:
            seen.add(h["expr"])
            cand.append({**h, "role": "M" if "M" in h["src"].split("_")[0][-2:] else "A"})
    LIB[(S, "A")] = cand
    for X, v in (("Vtr", "train"), ("Vall", "all")):
        f = D / (DEV if (DEV and X == "Vtr") else "verify") / f"s{S}_{v}.yaml"
        dec = {int(d["id"]): bool(d["keep"]) for d in (yaml.safe_load(f.read_text(encoding="utf-8")) or {}).get("decisions", [])} if f.is_file() else None
        if dec is None or set(dec) != set(range(1, len(cand) + 1)):
            if not DRY:
                raise SystemExit(f"{f}: missing, or its decisions do not cover heads 1..{len(cand)}")
            dec = {i: True for i in range(1, len(cand) + 1)}
        LIB[(S, X)] = [h for i, h in enumerate(cand, 1) if dec[i]]
        DROP[(S, X)] = [h for i, h in enumerate(cand, 1) if not dec[i]]
uniq = sorted({h["expr"] for v in LIB.values() for h in v})
print(f"[c07] libraries: {', '.join(f'{X} {sum(len(LIB[(S, X)]) for S in SEEDS)}' for X in ('M',) + XS)}; {len(uniq)} distinct expressions; "
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
    print(f"[c07] view {dates[0]}..{END}: test {ho.stop - ho.start} days ({years_ho:.2f} y), forward {fw.stop - fw.start} ({years_fw:.2f} y)", flush=True)

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
                print(f"[c07] does not compute on the full view: {e}", flush=True)
                continue
            sg, hl = sign_hl[e]
            sm = steer.neutral_residual(sg * bk.smoothed(steer.signal_input(P[f"c{j}"]), hl), QF)
            SM[e], Z[e] = sm.astype(np.float32), dg._zrank(sm)[:tr.stop:5]
        print(f"[c07] rebuilt {min(i + 16, len(uniq))}/{len(uniq)} ({time.time() - t0:.0f}s)", flush=True)
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

    out = {"plan": "research/coldstart_C07/PLAN.md", "dry_run": DRY, "view": [str(dates[0]), END], "years_test": years_ho, "years_forward": years_fw,
           "evaluations": EVALS, "gpu_seconds": GPUSEC, "libraries": {}, "per_seed": {},
           "dropped": {f"{S}/{X}": [h["expr"] for h in v] for (S, X), v in DROP.items()}}
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
    print(f"[c07] reproduce: {sum(h['reproduces'] for v in KEPT.values() for h in v)}/{sum(len(v) for v in KEPT.values())}", flush=True)

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

        out["primary"] = p = compare("Vtr", "A")
        out["verdict_primary"] = "V 更好" if (p["p_better"] < 0.05 and p["median"] > 0) else "V 更差" if (p["p_worse"] < 0.05 and p["median"] < 0) else "分不出"
        out["secondary"] = {"Vall_vs_A": compare("Vall", "A"), "Vtr_vs_Vall": compare("Vtr", "Vall"), "A_vs_M": compare("A", "M"),
                            "Vtr_vs_A_forward": compare("Vtr", "A", "forward"), "Vall_vs_A_forward": compare("Vall", "A", "forward")}
        heads = {}                                              # every candidate head of A, kept or dropped by each verifier
        for S in SEEDS:
            for h in LIB[(S, "A")]:
                if h["expr"] not in SM:
                    continue
                sm = SM[h["expr"]].astype(np.float64)
                r, rf = bk.book_row(sm, tgt, ho), bk.book_row(sm, tgt, fw)
                heads.setdefault(str(S), []).append({"expr": h["expr"], "role": h["role"], "train": h["train"], "valid": h["valid"],
                                                     "test_sharpe": float(np.nan_to_num(r["long_sharpe"])), "forward_sharpe": float(np.nan_to_num(rf["long_sharpe"])),
                                                     "kept_tr": h["expr"] in {x["expr"] for x in LIB[(S, "Vtr")]},
                                                     "kept_all": h["expr"] in {x["expr"] for x in LIB[(S, "Vall")]}})
        out["candidate_heads"] = heads
        print(f"PRIMARY: median V_tr-A {p['median']:+.2f}, p(V better) {p['p_better']:.3f}, p(V worse) {p['p_worse']:.3f} -> {out['verdict_primary']}", flush=True)
    mem.stop()

out["seconds"] = time.time() - t0
(D / ("final_dry.json" if DRY else f"final_dev_{DEV}{'_fn' if FUSE_NEUTRAL else ''}.json" if DEV else "final.json")).write_text(json.dumps(out, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
for S in SEEDS:
    r = out["per_seed"][str(S)]
    print(f"  s{S}: " + "  ".join(f"{X} {r[X]['heads']}h tr {r[X]['train']['long_sharpe']:+.2f} va {r[X]['valid']['long_sharpe']:+.2f}"
                                    + ("" if DRY else f" te {r[X]['test']['long_sharpe']:+.2f}") for X in ("M",) + XS))
print(f"wrote {D / ('final_dry.json' if DRY else f'final_dev_{DEV}' + ('_fn' if FUSE_NEUTRAL else '') + '.json' if DEV else 'final.json')} ({out['seconds']:.0f}s)")
