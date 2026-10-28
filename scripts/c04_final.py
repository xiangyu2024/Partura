"""C04: the one out-of-sample read of both arms, by the rule written before any run (research/coldstart_C04/PLAN.md §3).
Derived from scripts/c03_final.py; differences: size (LogFloatCap) is a fifth control of the residual, the daily-field store
is opened ($PARTURA_DAILY_ROOT), a head must be |rho| < 0.7 from every C01-C03 head, and the PRIMARY metric is continuous:
per seed, the equal-weight fusion of that run's own heads (same dedup rules) traded as a residual book on the test period
(a seed without heads holds cash: 0), compared across the 16 paired seeds with a one-sided Wilcoxon signed-rank test.
Derived from scripts/c02_final.py; differences: every rebuilt signal is the RESIDUAL on the style controls (liquidity,
volatility, 20-day reversal, the known family -- partura.steer.neutral_residual, the reward's own transform), so the
dedup, the heads, the reproduction check and the out-of-sample books are all on what the reward traded; a head must be
|rho| < 0.7 from every C01 AND C02 head; 16 seeds (601-616).
Derived from scripts/c01_final.py (same rebuild, dedup, reads, memory handling); differences: one round (seeds 401-408),
arm B's discoveries include its direct tests (research/coldstart_C02/direct_r1.json), the admission line is the runs' own
--threshold (0.7), and a head must also be |rho| < 0.7 from every C01 head (only NEW signals count).

Server.  For each arm -- A (AlphaCube alone: the round-1 runs and the A jobs of rounds 2-3) and B (AlphaCube + Partura:
the same round-1 runs and the B jobs) -- every discovery (steer.is_discovery, score >= 1.0) of every run, highest score
first, is rebuilt on the full view exactly as the reward scored it (direction x EMA at the chosen half-life) and kept as
a HEAD when its daily cross-sectional rank correlation (train, every 5th day, as scripts/idea_search.py measures it) is
below 0.5 with the known family and the pool and below 0.7 with every head already kept.  Each head is then read ONCE on
the test period (20230808..20251231: its pure long book, top decile, net of 15 bp, against the equal weight; VALID =
annualised net excess > 0 and t = Sharpe x sqrt(years) >= 2.0), on the forward segment (2026 onward: reported, not
judged), and after a daily cross-sectional neutralisation on liquidity, volatility and 20-day reversal.  Both reads are
ledgered (runs/_c04/ledger.json) and refused a second time.

    python scripts/c04_final.py [--dry-run] [--gpu-fraction 0.4]      -> research/coldstart_C04/final.json
--dry-run: heads and the in-sample reproduction check only; nothing out of sample is computed or ledgered.
--fix-rerun '<reason>': PLAN revision 3 -- the same read again after an implementation error was fixed; ledgered with the reason -> final_fix.json.
"""
import json
import math
import os
import re
import sys
import time
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.guard import MemoryGuard, limit_threads, slot  # noqa: E402

limit_threads(8)
import numpy as np  # noqa: E402

from partura import books as bk  # noqa: E402
from partura import diagnose as dg  # noqa: E402
from partura import ops_ext  # noqa: E402,F401
from partura import steer  # noqa: E402
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.panels import SHARED_CACHE, PanelSet  # noqa: E402
from partura.splits import Ledger  # noqa: E402

argv = sys.argv[1:]
DRY = "--dry-run" in argv
GPU = float(argv[argv.index("--gpu-fraction") + 1]) if "--gpu-fraction" in argv else 0.4
D = PARTURA_ROOT / "research" / "coldstart_C04"
EP = PARTURA_ROOT / "episodes"
LEDGER = PARTURA_ROOT / "runs" / "_c04" / "ledger.json"
LEDGER.parent.mkdir(parents=True, exist_ok=True)
T_LINE, RHO_KNOWN, RHO_HEAD = 2.0, 0.5, 0.7
STORE, MIRROR = "/root/autodl-tmp/qmt_daily_data/fast_factor_compute", "/root/autodl-tmp/AlphaCube/mirror"


def runs_of(arm):
    """(round, seed, episode dir, arm name in the evidence, idea) of every run of an arm."""
    out = [(1, p) for p in sorted(EP.glob(f"c04r1s*{arm}_*/evidence.json"))]
    rows = []
    for k, p in out:
        E = json.loads(p.read_text(encoding="utf-8"))
        name = "control" if arm == "A" else "steer"
        if name in E["arms"]:
            rows.append({"round": k, "seed": E["seed"], "episode": p.parent.name, "evidence": E, "arm": name, "idea": E["idea"]})
    return rows


ARMS = {a: runs_of(a) for a in ("A", "B")}
for a, rs in ARMS.items():
    print(f"[c04] arm {a}: {len(rs)} runs ({Counter(r['round'] for r in rs)})", flush=True)
AFTER_ABORT = argv[argv.index("--after-abort") + 1] if "--after-abort" in argv else ""
FIX = argv[argv.index("--fix-rerun") + 1] if "--fix-rerun" in argv else ""   # PLAN revision 3: re-run after an implementation error, ledgered, -> final_fix.json
if not DRY and Ledger(LEDGER).summary().get("holdout") and not AFTER_ABORT and not FIX:
    raise SystemExit(f"the test period of C04 has already been read ({LEDGER}); this read happens once "
                     f"(--after-abort '<reason>' only when the previous read stopped before producing any result)")

passers, EXCLUDED = {}, {}
EXCLUDE_OPS = ("ts_spearman",)
for a, rs in ARMS.items():
    lst = []
    for r in rs:
        E, A = r["evidence"], r["evidence"]["arms"][r["arm"]]
        for c in A["candidates"]:
            if steer.is_discovery(E["reward"], c.get("score"), c.get("s_train"), c.get("s_valid"), float(E.get("threshold", 1.0))):
                lst.append({**{k: c.get(k) for k in ("expr", "score", "train", "valid", "hl", "sign", "turnover", "rho_known")},
                            "round": r["round"], "seed": r["seed"], "episode": r["episode"], "idea": r["idea"]["id"],
                            "hood": sorted(set((r["idea"].get("grammar") or {}).get("day_ops", [])))})
    lst.sort(key=lambda c: -c["score"])
    # PLAN §6 revision 4: every expression with ts_spearman is left out of BOTH arms (a per-stock Python loop that cannot be
    # rebuilt on the full view in reasonable time); 90 of arm A's discoveries and 1 of arm B's.  This favours arm B.
    EXCLUDED[a] = sum(1 for c in lst if any(op in c["expr"] for op in EXCLUDE_OPS))
    passers[a] = [c for c in lst if not any(op in c["expr"] for op in EXCLUDE_OPS)]
# arm B's direct tests (research/coldstart_C02/PLAN.md §2.4): every variant that was a discovery there is one of B's discoveries
DIRECT = json.loads((D / "direct_r1.json").read_text(encoding="utf-8")) if (D / "direct_r1.json").is_file() else {"rows": []}
for r in DIRECT["rows"]:
    if r.get("discovery"):
        passers["B"].append({**{k: r.get(k) for k in ("expr", "score", "train", "valid", "hl", "sign", "turnover", "rho_known")},
                             "round": 1, "seed": None, "episode": "direct_r1", "idea": r["hypothesis"], "hood": []})
passers["B"].sort(key=lambda c: -c["score"])
# every C01 head (research/coldstart_C01/final.json, both arms): a C02 head must be |rho| < 0.7 from all of them
C01H = {}                                                      # every C01 AND C02 head (the prior knowledge of both arms)
for study in ("coldstart_C01", "coldstart_C02", "coldstart_C03"):
    for A_ in json.loads((PARTURA_ROOT / "research" / study / "final.json").read_text(encoding="utf-8"))["arms"].values():
        for h in A_["heads"]:
            C01H.setdefault(h["expr"], (float(h["sign"]), float(h["hl"])))
# C01 PLAN §6 revision 3 (kept): a discovery that is the known family by the search's own measurement (max(|rho_pool|, |rho_known_traded|)
# >= 0.5, the same train days, smoothing and direction as below) can never be a head -- it is not rebuilt; a random 20 of
# them are rebuilt anyway and both measurements are reported, so the shortcut is checked, not assumed.
def known_by_search(c):
    r = [abs(c[k]) for k in ("rho_pool", "rho_known_traded") if isinstance(c.get(k), (int, float)) and c[k] == c[k]]
    return bool(r) and max(r) >= RHO_KNOWN


for lst in passers.values():
    for c in lst:
        src = next((x for r in ARMS["A"] + ARMS["B"] if r["episode"] == c["episode"] for x in r["evidence"]["arms"][r["arm"]]["candidates"] if x["expr"] == c["expr"]), {})
        c["rho_pool"], c["rho_known_traded"] = src.get("rho_pool"), src.get("rho_known_traded")
prefiltered = sorted({c["expr"] for lst in passers.values() for c in lst if known_by_search(c)}
                     - {c["expr"] for lst in passers.values() for c in lst if not known_by_search(c)})
_ck = [e for e in prefiltered if "nt_" not in e]               # the check itself must not be the minute-level spill it avoids
check_known = [_ck[j] for j in sorted(set(int(k * len(_ck) / 20) for k in range(20)))] if _ck else []
uniq = sorted({c["expr"] for lst in passers.values() for c in lst} - set(prefiltered)) + check_known
uniq += [e for e in sorted(C01H) if e not in uniq]
print(f"[c04] known family by the search's own measurement, not rebuilt: {len(prefiltered)} (rebuilt anyway as a check: {len(check_known)})", flush=True)
print(f"[c04] discoveries: A {len(passers['A'])}, B {len(passers['B'])} (left out by revision 4: {EXCLUDED}); {len(uniq)} distinct expressions to rebuild", flush=True)

with slot():
    mem = MemoryGuard(self_limit_gb=60, cgroup_limit_gb=80).start()   # PLAN §6 revision 5 (34 GB aborted the first read)
    t0 = time.time()
    import torch
    from alphacube.plugins import load_plugins
    from alphacube.store import open_cube_store
    load_plugins(["partura.ac_plugin"])
    END = str(open_cube_store(STORE, mirror_root=MIRROR).dates[-1])
    ps = PanelSet(STORE, "20180102", END, warmup=60, device="cuda", gpu_fraction=GPU, cache_dir=str(SHARED_CACHE), mirror_root=MIRROR,
                  workdir=str(PARTURA_ROOT / "tmp"), label_kind="open_vwap15", label_buyable=True, batch=8,
                  daily_root=os.environ.get("PARTURA_DAILY_ROOT") or None)
    G = steer.Guidance.load(PARTURA_ROOT / "guidance" / "C00_base.yaml")
    known_spec = G.spec["pool"][0]
    aux = ps.compute({"known": known_spec["expr"], "liq": "cross_mean(day_sum(Amt), 30)", "vol": "cross_mean(day_std(Ret), 20)",
                      "rev": "div(day_last(Close), ts_delay(day_last(Close), 20))", "size": "LogFloatCap"})
    tgt = ps.target(1)
    dates = np.asarray(ps.dates).astype(str)
    ix = lambda d: int(np.searchsorted(dates, d))                       # noqa: E731
    tr, va, us = slice(0, ix("20220101")), slice(ix("20220101"), ix("20230808")), slice(0, ix("20230808"))
    ho, fw = slice(ix("20230808"), ix("20260101")), slice(ix("20260101"), len(dates))
    years_ho = float(np.isfinite(tgt[ho]).any(1).sum()) / 252.0
    years_fw = float(np.isfinite(tgt[fw]).any(1).sum()) / 252.0
    known_z = dg._zrank(float(known_spec["sign"]) * np.asarray(aux["known"], np.float64))
    kz = known_z[:tr.stop:5]
    controls = {k: dg._zrank(np.asarray(aux[k], np.float64)) for k in ("liq", "vol", "rev")}
    QF = steer.neutral_basis([aux["liq"], aux["vol"], aux["rev"], aux["known"], aux["size"]])   # the same controls, in the same order, as the search
    print(f"[c04] view {dates[0]}..{END}: train {tr.stop} days, valid {va.stop - va.start}, test {ho.stop - ho.start} ({years_ho:.2f} y), "
          f"forward {fw.stop - fw.start} ({years_fw:.2f} y); context in {time.time() - t0:.0f}s", flush=True)

    def rho(a, b):
        ok = np.isfinite(a) & np.isfinite(b)
        x, y = np.where(ok, a, 0.0), np.where(ok, b, 0.0)
        n = np.maximum(ok.sum(1), 1)
        with np.errstate(invalid="ignore", divide="ignore"):
            c = ((x * y).sum(1) - x.sum(1) * y.sum(1) / n) / np.sqrt(((x ** 2).sum(1) - x.sum(1) ** 2 / n) * ((y ** 2).sum(1) - y.sum(1) ** 2 / n))
        return float(np.nanmean(c))

    def top_decile(x):
        with np.errstate(invalid="ignore"):
            q = np.nanquantile(np.where(np.isfinite(x), x, np.nan), 1.0 - bk.TOP_FRAC, axis=1, keepdims=True)
            return np.isfinite(x) & (x >= q)

    KNOWN_TOP = top_decile(known_z)

    def overlap(sm, sl):
        """Mean daily share of the head's top decile that is also in the known family's top decile (holdings only)."""
        ht = top_decile(sm[sl])
        n = ht.sum(1)
        with np.errstate(invalid="ignore", divide="ignore"):
            return float(np.nanmean(np.where(n > 0, (ht & KNOWN_TOP[sl]).sum(1) / n, np.nan)))

    # ---- rebuild every discovery once (the same expression found by both arms is one panel)
    SM, Z = {}, {}
    sign_hl = {}
    for lst in passers.values():
        for c in lst:
            sign_hl.setdefault(c["expr"], (float(c["sign"]), float(c["hl"])))
    for e, v in C01H.items():
        sign_hl.setdefault(e, v)
    for i in range(0, len(uniq), 16):
        chunk = uniq[i:i + 16]
        P = ps.compute({f"c{j}": e for j, e in enumerate(chunk)})
        for j, e in enumerate(chunk):
            if f"c{j}" not in P:
                print(f"[c04] does not compute on the full view: {e}", flush=True)
                continue
            sg, hl = sign_hl[e]
            sm = steer.neutral_residual(sg * bk.smoothed(np.asarray(P[f"c{j}"], np.float64), hl), QF)   # what the reward traded
            SM[e] = sm.astype(np.float32)
            Z[e] = dg._zrank(sm)[:tr.stop:5]
        print(f"[c04] rebuilt {min(i + 16, len(uniq))}/{len(uniq)} ({time.time() - t0:.0f}s)", flush=True)

    chk = [{"expr": e, "full_view": rho(Z[e], kz), "search": max(abs(c["rho_known_traded"]) for lst in passers.values() for c in lst if c["expr"] == e)}
           for e in check_known if e in Z]
    if chk:
        print(f"[c04] prefilter check on {len(chk)}: |rho| full view vs search, max abs diff {max(abs(abs(x['full_view']) - x['search']) for x in chk):.4f}; "
              f"would have been heads by the full-view number: {sum(abs(x['full_view']) < RHO_KNOWN for x in chk)}", flush=True)
    out = {"plan": "research/coldstart_C04/PLAN.md", "dry_run": DRY, "prefiltered_known": len(prefiltered), "excluded_ts_spearman": EXCLUDED, "prefilter_check": chk, "view": [str(dates[0]), END], "years_test": years_ho, "years_forward": years_fw,
           "trials": {a: sum(r["evidence"]["arms"][r["arm"]]["scored"] for r in rs) for a, rs in ARMS.items()}, "arms": {}}
    for a, lst in passers.items():
        heads = []
        for c in lst:
            e = c["expr"]
            if e not in Z or e in prefiltered:
                continue
            c["rho_known_full"] = rho(Z[e], kz)
            if abs(c["rho_known_full"]) >= RHO_KNOWN:
                continue
            near = [x for x in C01H if x in Z and abs(rho(Z[e], Z[x])) >= RHO_HEAD]
            if near:                                          # not new: the same signal as a C01 head
                c["near_c01"] = near[0]
                out.setdefault("not_new", {}).setdefault(a, []).append({"expr": e, "score": c["score"], "c01_head": near[0]})
                continue
            if all(abs(rho(Z[e], Z[h["expr"]])) < RHO_HEAD for h in heads):
                heads.append(c)
        for h in heads:                                       # does the rebuilt book reproduce the search's own numbers?
            sm = SM[h["expr"]].astype(np.float64)
            h["re_train"], h["re_valid"] = bk.book_row(sm, tgt, tr)["long_sharpe"], bk.book_row(sm, tgt, va)["long_sharpe"]
            h["reproduces"] = bool(abs(h["re_train"] - h["train"]) < 0.05 and abs(h["re_valid"] - h["valid"]) < 0.05)
            # PLAN §6 (revision 1): a screen can shift a block of ranks and keep |rho| low while the LONG BOOK is still the
            # known family's -- so also the share of the head's top decile that is in the known family's top decile
            h["overlap_known_train"] = overlap(sm, us)
            if not DRY:
                h["overlap_known_test"] = overlap(sm, ho)
        out["arms"][a] = {"discoveries": len(lst), "heads": heads}
        print(f"[c04] arm {a}: {len(lst)} discoveries -> {len(heads)} heads; reproduce {sum(h['reproduces'] for h in heads)}/{len(heads)}", flush=True)

    # ---- PRIMARY (C04 PLAN §3): per seed, the fusion of that run's own heads
    SEEDFUSE = {}
    for a, lst in passers.items():
        for seed in sorted({r["seed"] for r in ARMS[a]}):   # every run of the arm (PLAN §3: a seed without heads holds cash), not only seeds with discoveries
            hs = []
            for c in lst:
                e = c["expr"]
                if c["seed"] != seed or e not in Z or e in prefiltered or c.get("near_c01") or abs(rho(Z[e], kz)) >= RHO_KNOWN:
                    continue
                if all(abs(rho(Z[e], Z[h])) < RHO_HEAD for h in hs):
                    hs.append(e)
            if hs:
                acc = np.zeros(SM[hs[0]].shape, np.float64)
                cnt = np.zeros(SM[hs[0]].shape, np.int32)
                for e in hs:
                    z = dg._zrank(SM[e].astype(np.float64))
                    ok = np.isfinite(z)
                    acc += np.where(ok, z, 0.0)
                    cnt += ok
                with np.errstate(invalid="ignore", divide="ignore"):
                    SEEDFUSE[(a, seed)] = (len(hs), np.where(cnt > 0, acc / np.maximum(cnt, 1), np.nan).astype(np.float32))
            else:
                SEEDFUSE[(a, seed)] = (0, None)
    keep = {h["expr"] for v in out["arms"].values() for h in v["heads"]}
    for e in list(SM):
        if e not in keep:
            del SM[e]
    if not DRY:
        n = sum(len(v["heads"]) for v in out["arms"].values())
        tag = "c04_final" + ("_after_abort" if AFTER_ABORT else "_fix" if FIX else "")
        why = f" -- re-read after an aborted read: {AFTER_ABORT}" if AFTER_ABORT else f" -- re-run to fix an implementation error: {FIX}" if FIX else ""
        Ledger(LEDGER).record("holdout", n, f"C04 heads of both arms, test period 20230808..20251231, by PLAN.md §3{why}", tag)
        Ledger(LEDGER).record("forward", n, f"C04 heads of both arms, forward column 20260101..{END} (reported, not judged){why}", tag)
        for a, A in out["arms"].items():
            fsum, fcnt = None, None
            for h in A["heads"]:
                sm = SM[h["expr"]].astype(np.float64)
                for nm, sl, yrs in (("test", ho, years_ho), ("forward", fw, years_fw)):
                    r = bk.book_row(sm, tgt, sl)
                    h[nm] = {"ann": r["long_ann"], "sharpe": r["long_sharpe"], "t": r["long_sharpe"] * math.sqrt(yrs), "mdd": r["long_mdd"],
                             "turnover": r["long_turnover"], "ls_sharpe": r["ls_sharpe"]}
                res, info = dg.neutralise(sm, controls, controls_ready=True)
                rn = bk.book_row(res, tgt, ho)
                h["test_neutral"] = {"ann": rn["long_ann"], "sharpe": rn["long_sharpe"], "t": rn["long_sharpe"] * math.sqrt(years_ho), "r2": info["mean_r2"]}
                h["valid_oos"] = bool(h["test"]["ann"] > 0 and h["test"]["t"] >= T_LINE)
                h["valid_oos_neutral"] = bool(h["test_neutral"]["ann"] > 0 and h["test_neutral"]["t"] >= T_LINE)
                z = dg._zrank(sm)
                ok = np.isfinite(z)
                if fsum is None:
                    fsum, fcnt = np.zeros_like(z), np.zeros(z.shape, np.int32)
                fsum += np.where(ok, z, 0.0)
                fcnt += ok
                del z, ok, res
            if fsum is not None:
                with np.errstate(invalid="ignore", divide="ignore"):
                    fz = np.where(fcnt > 0, fsum / np.maximum(fcnt, 1), np.nan)
                A["fused"] = {nm: {k: bk.book_row(fz, tgt, sl)[k] for k in ("long_ann", "long_sharpe", "long_turnover", "long_mdd")}
                              for nm, sl in (("train", tr), ("valid", va), ("test", ho), ("forward", fw))}
            A["valid_oos"] = sum(h["valid_oos"] for h in A["heads"])
            A["valid_oos_neutral"] = sum(h["valid_oos_neutral"] for h in A["heads"])
        per = {}
        for (a, seed), (nh, fz) in SEEDFUSE.items():
            if fz is None:
                per[(a, seed)] = {"heads": 0, "test_sharpe": 0.0, "test_ann": 0.0, "forward_sharpe": 0.0}
            else:
                rt, rf = bk.book_row(fz.astype(np.float64), tgt, ho), bk.book_row(fz.astype(np.float64), tgt, fw)
                per[(a, seed)] = {"heads": nh, "test_sharpe": float(np.nan_to_num(rt["long_sharpe"])), "test_ann": float(np.nan_to_num(rt["long_ann"])),
                                  "forward_sharpe": float(np.nan_to_num(rf["long_sharpe"]))}
        seeds = sorted({s_ for (a, s_) in per if a == "A"} & {s_ for (a, s_) in per if a == "B"})
        diffs = [per[("B", s_)]["test_sharpe"] - per[("A", s_)]["test_sharpe"] for s_ in seeds]
        from scipy.stats import wilcoxon
        nz = [d for d in diffs if d != 0]
        p_up = float(wilcoxon(nz, alternative="greater").pvalue) if len(nz) >= 5 else float("nan")
        p_dn = float(wilcoxon(nz, alternative="less").pvalue) if len(nz) >= 5 else float("nan")
        med = float(np.median(diffs)) if diffs else float("nan")
        out["per_seed"] = {"seeds": seeds, "A": [per[("A", s_)] for s_ in seeds], "B": [per[("B", s_)] for s_ in seeds],
                           "diffs": diffs, "median_diff": med, "p_B_better": p_up, "p_B_worse": p_dn}
        out["verdict_primary"] = ("Partura v2 有用" if (p_up < 0.05 and med > 0) else "Partura v2 更差" if (p_dn < 0.05 and med < 0) else "分不出")
        print(f"PRIMARY (per-seed fused residual book, test Sharpe): median B-A {med:+.2f}, p(B better) {p_up:.3f}, p(B worse) {p_dn:.3f} -> {out['verdict_primary']}", flush=True)
        a_, b_ = out["arms"]["A"]["valid_oos"], out["arms"]["B"]["valid_oos"]
        out["verdict"] = ("Partura 有用" if (b_ - a_ >= 2 and b_ >= 2 * max(a_, 1)) else "Partura 更差" if a_ - b_ >= 2 else "分不出")
    mem.stop()

# ---- secondary (in-sample, from the evidence): paired seeds of rounds 2-3 and the expressions themselves
pairs = []
for k in (1,):
    for ra in [r for r in ARMS["A"] if r["round"] == k]:
        rb = next((r for r in ARMS["B"] if r["round"] == k and r["seed"] == ra["seed"]), None)
        ha = ra["evidence"]["arms"]["control"].get("independent_distinct", 0)
        ga = ra["evidence"]["arms"]["control"]["gate_fail"] / max(ra["evidence"]["arms"]["control"]["scored"], 1)
        if rb:
            hb = rb["evidence"]["arms"]["steer"].get("independent_distinct", 0)
            gb = rb["evidence"]["arms"]["steer"]["gate_fail"] / max(rb["evidence"]["arms"]["steer"]["scored"], 1)
            pb = rb["evidence"]["arms"]["steer"]["passers"]
        else:                                                 # PLAN §6 revision 2: a B run that failed twice counts as 0
            hb, gb, pb = 0, float("nan"), 0
        pairs.append({"round": k, "seed": ra["seed"], "heads_A": ha, "heads_B": hb, "gate_A": ga, "gate_B": gb, "B_failed": rb is None,
                      "passers_A": ra["evidence"]["arms"]["control"]["passers"], "passers_B": pb})
wins = sum(p["heads_B"] > p["heads_A"] for p in pairs)
loss = sum(p["heads_B"] < p["heads_A"] for p in pairs)
nn = wins + loss
p_sign = sum(math.comb(nn, j) for j in range(wins, nn + 1)) / 2 ** nn if nn else float("nan")
out["paired_seeds"] = {"pairs": pairs, "B_wins": wins, "B_losses": loss, "ties": len(pairs) - nn, "p_one_sided": p_sign}
out["bad_rounds"] = [k for k in (1,) if sum(p["heads_B"] < p["heads_A"] for p in pairs if p["round"] == k) >= 5]

FACES = ("day_", "cross_", "cs_", "ts_", "in_", "nt_")


def anatomy(lst):
    ops, leaves, faces, depth, size = Counter(), Counter(), Counter(), [], []
    for c in lst:
        e = c["expr"]
        o = re.findall(r"[A-Za-z_][A-Za-z_0-9]*(?=\()", e)
        ops.update(set(o))
        leaves.update(set(t for t in re.findall(r"[A-Za-z_]+", e) if t in ("Open", "High", "Low", "Close", "Vwap", "Volume", "Amt", "Ret")))
        faces.update(set(next((f for f in FACES if x.startswith(f)), "other") for x in o))
        try:
            n = steer.parse_expr(e)
            size.append(sum(1 for _ in steer.walk(n)))
            depth.append(max(d for _, d in steer.walk(n)) + 1)
        except Exception:                                      # noqa: BLE001
            pass
    n = max(len(lst), 1)
    return {"n": len(lst), "ops": {k: v / n for k, v in ops.most_common(25)}, "leaves": {k: v / n for k, v in leaves.most_common()},
            "faces": {k: v / n for k, v in faces.most_common()}, "depth_mean": float(np.mean(depth)) if depth else None,
            "size_mean": float(np.mean(size)) if size else None}


out["anatomy"] = {a: {"discoveries": anatomy(passers[a]), "heads": anatomy(out["arms"].get(a, {}).get("heads", []))} for a in passers}
for k in (1,):
    bk_ = [c for c in passers["B"] if c["round"] == k]
    out["anatomy"].setdefault("B_in_hood", {})[f"r{k}"] = {"discoveries": len(bk_), "in_hood": sum(1 for c in bk_ if c["hood"] and any(op in c["expr"] for op in c["hood"]))}
out["gpu_seconds"] = {a: sum(r["evidence"]["arms"][r["arm"]]["seconds"] for r in rs) for a, rs in ARMS.items()}
out["seconds"] = time.time() - t0
(D / ("final_dry.json" if DRY else "final_fix.json" if FIX else "final.json")).write_text(json.dumps(out, ensure_ascii=False, indent=1, default=float), encoding="utf-8")

for a, A in out["arms"].items():
    print(f"\n== arm {a}: {A['discoveries']} discoveries, {len(A['heads'])} heads" + ("" if DRY else f", valid out of sample {A['valid_oos']} (style-neutral {A['valid_oos_neutral']})"))
    for h in A["heads"][:30]:
        t = "" if DRY else f" | test {h['test']['ann']:+.1%} t {h['test']['t']:+.1f} | neutral t {h['test_neutral']['t']:+.1f} | fwd {h['forward']['ann']:+.1%} t {h['forward']['t']:+.1f}"
        print(f"  R{h['round']} s{h['seed']} score {h['score']:+.2f} (re {h['re_train']:+.2f}/{h['re_valid']:+.2f}{'' if h['reproduces'] else ' !'}) "
              f"rho_known {h['rho_known_full']:+.2f}{t} | {h['expr'][:110]}")
print(f"\npaired seeds: B more heads in {wins}, fewer in {loss}, ties {len(pairs) - nn}; one-sided sign test p = {p_sign:.3f}; bad rounds {out['bad_rounds']}")
if not DRY:
    print(f"VERDICT (PLAN.md §3.3): {out['verdict']}  (A {out['arms']['A']['valid_oos']} vs B {out['arms']['B']['valid_oos']})")
