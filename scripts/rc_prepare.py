"""Risk control (research/risk_control/PLAN.md), step 1: the inputs, on the extended view (2018-01-02 .. 2026-09-16).

Server.  Writes runs/_risk/:

* ``base.json``            dates, symbols, the segment boundaries
* ``target.npy``           the label every champion was fitted on (open_vwap15, buyable), float64
* ``px_*.npy``             daily panels the risk side needs (close, amount, high, low, log caps, limit width, industry code)
* ``fam_<champion>.npy``   the champion's family factors (n_fam, D, S) float32 -- AlphaCube's ``build_champion.build`` step by step
  (z-score per day, direction by the training-period IC, ridge inside a family), kept so the pre-fusion side can re-weight them
* ``famw_<champion>.npy``  the across-family least-squares weights (training period only)

and checks that sum_k w_k fam_k is the stored signal ``runs/_forward/signal_<champion>_20260916.npy``.

    rc_prepare.py [--only 手写库冠军,挖掘冠军] [--skip-families]
"""
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.guard import MemoryGuard, limit_threads, slot  # noqa: E402

limit_threads(8)
import numpy as np  # noqa: E402

from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.panels import SHARED_CACHE, PanelSet  # noqa: E402

AC = Path("/root/autodl-tmp/AlphaCube")
sys.path.insert(0, str(AC / "scripts"))
argv = sys.argv[1:]


def opt(name, default=None):
    return argv[argv.index(name) + 1] if name in argv else default


STORE = "/root/autodl-tmp/qmt_daily_data/fast_factor_compute"
END = "20260916"
OUT = PARTURA_ROOT / "runs" / "_risk"
OUT.mkdir(parents=True, exist_ok=True)
names = [n for n in (opt("--only") or "手写库冠军,挖掘冠军").split(",") if n]
M = json.loads((PARTURA_ROOT / "runs" / "_forward" / f"members_{END}.json").read_text(encoding="utf-8"))
EXPR = {"close": "day_last(Close)", "amt": "day_sum(Amt)", "high": "day_max(High)", "low": "day_min(Low)",
        "ltc": "neg(LogTotalCap)", "lfc": "neg(LogFloatCap)", "lfs": "neg(LogFloatShares)"}

with slot():
    mem = MemoryGuard(self_limit_gb=60, cgroup_limit_gb=80).start()
    t0 = time.time()
    ps = PanelSet(STORE, "20180102", END, warmup=60, device="cuda", gpu_fraction=0, cache_dir=str(SHARED_CACHE),
                  mirror_root="/root/autodl-tmp/AlphaCube/mirror", workdir=str(PARTURA_ROOT / "tmp"),
                  label_kind="open_vwap15", label_buyable=True, batch=8, daily_root=str(PARTURA_ROOT / "daily_fields"))
    dates = np.asarray(ps.dates).astype(str)
    syms = list(ps.symbols)
    ix = lambda d: int(np.searchsorted(dates, d))             # noqa: E731
    us, n_old = slice(0, ix("20230808")), ix("20260101")
    if us.stop != 1359 or str(dates[n_old - 1]) != "20251231" or str(dates[-1]) != END:
        raise SystemExit(f"unexpected calendar: {us.stop} training days, old view ends {dates[n_old - 1]}, view ends {dates[-1]}")
    tgt = np.asarray(ps.target(1), dtype=np.float64)
    np.save(OUT / "target.npy", tgt)
    P = ps.compute(EXPR)
    if ps.errors:
        raise SystemExit(f"[rc] expressions that did not evaluate: {dict(ps.errors)}")
    for k in ("ltc", "lfc", "lfs"):
        P[k] = -np.asarray(P[k], dtype=np.float64)
    for k, v in P.items():
        np.save(OUT / f"px_{k}.npy", np.asarray(v, dtype=np.float32))
    from alphacube.tradability import board_limit
    np.save(OUT / "px_limit.npy", board_limit(syms, list(dates)).astype(np.float32))
    # industry: the only Shenwan level-1 table on the server is a 2026-08/09 snapshot -> back-filled (PLAN section 5)
    import pandas as pd
    snap = sorted(Path("/root/autodl-tmp/qmt_stock_data/processed/reference/sw_l1_mapping").glob("*.parquet"))[-1]
    df = pd.read_parquet(snap)
    code = dict(zip(df["symbol"], df["sw_l1_code"]))
    ind = np.asarray([int(code.get(s, -1)) for s in syms], dtype=np.int16)
    np.save(OUT / "px_industry.npy", ind)
    raw_px = np.exp(P["lfc"] - P["lfs"])                       # float cap / float shares = unadjusted price (unit check below)
    np.save(OUT / "px_rawprice.npy", raw_px.astype(np.float32))
    print(f"[rc] view {dates[0]}..{dates[-1]}: {len(dates)} x {len(syms)}; industry from {snap.name}: {int((ind >= 0).sum())} mapped, {len(set(ind[ind >= 0]))} industries; "
          f"raw price median {np.nanmedian(raw_px[-1]):.3f} (last day), {np.nanmedian(raw_px[0]):.3f} (first day); total cap median {np.exp(np.nanmedian(P['ltc'][-1])):.3g} ({time.time() - t0:.0f}s)", flush=True)
    (OUT / "base.json").write_text(json.dumps({"dates": [str(d) for d in dates], "symbols": syms, "train_stop": us.stop, "old_stop": n_old, "end": END,
                                                "industry_snapshot": snap.name}, ensure_ascii=False), encoding="utf-8")

    if "--skip-families" not in argv:
        from combine_two_level import blend, fit_weights
        from alphacube.metrics import cs_pearson, nanmean_quiet, zscore_rows
        tgt_old = tgt.copy()
        tgt_old[n_old - 2:] = np.nan                           # the label the stored signals saw
        check = {}
        for name in names:
            C, d = M["champions"][name], PARTURA_ROOT / "pools" / "_ext" / name / "panels"
            fams, n = [], 0
            for f in C["families"]:                            # the same numbering scripts/two_level_forward.py gave the hard links
                idx = []
                for m_ in f:
                    e = M["expressions"][m_["key"]]
                    if e.get("path") and Path(e["path"]).is_file():
                        idx.append(n)
                        n += 1
                if idx:
                    fams.append(idx)
            keep = np.lib.format.open_memmap(OUT / f"fam_{name}.npy", mode="w+", dtype=np.float32, shape=(len(fams),) + tgt.shape)
            t1 = time.time()
            for k, idx in enumerate(fams):
                cols = []
                for j in idx:
                    z = zscore_rows(np.load(d / f"{j:05d}.npy").astype(np.float64))
                    if nanmean_quiet(cs_pearson(z[us], tgt_old[us])) < 0:
                        z = -z
                    cols.append(z)
                keep[k] = blend(cols, fit_weights(cols, tgt_old, us, "ridge")).astype(np.float32)
                del cols
                if (k + 1) % 25 == 0:
                    print(f"[rc] {name}: family {k + 1}/{len(fams)} ({time.time() - t1:.0f}s)", flush=True)
            keep.flush()
            comp = [np.asarray(keep[k], dtype=np.float64) for k in range(len(fams))]
            w = fit_weights(comp, tgt_old, us, "lstsq")
            np.save(OUT / f"famw_{name}.npy", w)
            sig = blend(comp, w)
            stored = np.load(PARTURA_ROOT / "runs" / "_forward" / f"signal_{name}_{END}.npy").astype(np.float64)
            both = np.isfinite(sig) & np.isfinite(stored)
            err = float(np.max(np.abs(sig[both] - stored[both]) / (np.abs(stored[both]) + 1e-6)))
            check[name] = {"families": len(fams), "members": n, "negative_weights": int((w < 0).sum()), "max_rel_err_vs_stored": err,
                           "nan_pattern_equal": bool((np.isfinite(sig) == np.isfinite(stored)).all())}
            print(f"[rc] {name}: {len(fams)} families / {n} members; {int((w < 0).sum())} negative across-family weights; rebuilt vs stored max rel err {err:.2e}, "
                  f"NaN pattern equal {check[name]['nan_pattern_equal']} ({time.time() - t1:.0f}s)", flush=True)
            del comp, keep, sig, stored
        (OUT / "prepare_check.json").write_text(json.dumps(check, ensure_ascii=False, indent=1), encoding="utf-8")
    mem.stop()
print(f"[rc] prepare done ({time.time() - t0:.0f}s)")
