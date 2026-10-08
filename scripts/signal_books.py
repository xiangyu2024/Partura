"""Stored signal arrays (AlphaCube's champions, blends, rolling fits ...) under Partura's book convention.

Server.  Every (days, stocks) array on the production view (2018-01-02 ~ 2025-12-31, 5220 names) is treated like any
other signal: direction by the sign of its in-sample rank IC, half-life from the grid by the in-sample Sharpe of the
book it is judged by (the long/short book for the long/short view, the pure long book for the long view), decile
books, 15 bp.  That is exactly ``partura.books.books`` -- the function every Partura candidate went through -- so
the numbers are comparable with runs/*/sweepfinal_*.json and runs/_batch_*/fuse_*.json.

    python scripts/signal_books.py name=path [name=path ...] [--out runs/_batch_B01/signal_books.json]
    python scripts/signal_books.py --preset alphacube

Writes the table and, per signal, the daily series (long/short net; pure long TOTAL return; the equal-weight
universe; excess) in the format of scripts/book_series.py.  In-sample = to 2023-08-07; the rest is the old test
period.  A fitted combination's in-sample numbers are FITTED (its weights were estimated there).
"""
import glob
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.guard import MemoryGuard, limit_threads, slot  # noqa: E402

limit_threads(8)
import numpy as np  # noqa: E402

from partura import books as bk  # noqa: E402
from partura import diagnose as dg  # noqa: E402
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.panels import SHARED_CACHE, PanelSet  # noqa: E402

argv = sys.argv[1:]


def opt(name, default=None):
    return argv[argv.index(name) + 1] if name in argv else default


AC = Path("/root/autodl-tmp/AlphaCube")
items = dict(a.split("=", 1) for a in argv if "=" in a and not a.startswith("-"))
if opt("--preset") == "alphacube":
    B = AC / "_bench"
    for p in ([B / "champion_signal.npy", B / "champion_signal_buyable.npy", B / "legacy_signal.npy", B / "blend_legacy_mined.npy", B / "trainto" / "champion_signal_buyable.npy",
               B / "trainto" / "legacy_signal.npy"] + sorted(B.glob("sig_*.npy")) + sorted((B / "long_side").glob("*.npy")) + sorted((B / "universe").glob("oos_*_full_*.npy"))
              + sorted((B / "universe").glob("oos_mined_full_*.npy")) + [AC / "mining_runs" / r / "combined.npy" for r in ("gpu12", "gpu15", "gpu16", "rl1")]):
        if p.is_file():
            items.setdefault(str(p.relative_to(AC)).replace("_bench/", "").replace(".npy", ""), str(p))

with slot():
    mem = MemoryGuard(self_limit_gb=34, cgroup_limit_gb=70).start()
    t0 = time.time()
    ps = PanelSet("/root/autodl-tmp/qmt_daily_data/fast_factor_compute", "20180102", "20251231", warmup=60, device="cuda", gpu_fraction=0,
                  cache_dir=str(SHARED_CACHE), mirror_root="/root/autodl-tmp/AlphaCube/mirror", workdir=str(PARTURA_ROOT / "tmp"),
                  label_kind="open_vwap15", label_buyable=True, batch=8)
    tgt = np.asarray(ps.target(1), dtype=np.float64)
    dates = [str(d) for d in ps.dates]
    us, ho = ps.split_slice("utrain") if False else (slice(0, int(np.searchsorted(np.asarray(dates), "20230808"))), slice(int(np.searchsorted(np.asarray(dates), "20230808")), len(dates)))
    us_ranks = dg.rank_rows(tgt[us])
    from alphacube.metrics import long_short_weights, portfolio_returns
    r5 = lambda a: [None if x != x else round(float(x), 7) for x in a]      # noqa: E731
    out = {"end": dates[-1], "dates": dates, "objects": {}}
    print(f"{len(items)} signals on {len(dates)} days x {tgt.shape[1]} names (in-sample {us.stop} days, test {ho.stop - ho.start})")
    print(f"{'signal':52s} sg | 多空: hl 样本内 → 测试 夏普(年化)          | 纯多头: hl 样本内 → 测试 超额夏普(年化超额)   | 测试段换手")
    for name, path in items.items():
        a = np.load(path, mmap_mode="r")
        if a.shape != tgt.shape:
            print(f"{name[:52]:52s} skipped: shape {a.shape}")
            continue
        raw = np.asarray(a, dtype=np.float64)
        raw[~np.isfinite(raw)] = np.nan
        ic = dg.ic_row(raw[us], tgt[us], target_ranks=us_ranks)
        sign = 1.0 if not np.isfinite(ic["rank_ic"]) or ic["rank_ic"] >= 0 else -1.0
        b = bk.books(sign * raw, tgt, us, {"utrain": us, "holdout": ho})
        v = b["by_rank"]
        L, S = v["long"], v["ls"]
        o = {"kind": "array", "path": path, "sign": sign, "rank_ic_insample": float(ic["rank_ic"]), "hl_ls": float(S["hl"]), "hl": float(L["hl"]),
             "rows_ls": S["splits"], "rows_long": L["splits"]}
        sm_ls, sm_lo = bk.smoothed(sign * raw, S["hl"]), bk.smoothed(sign * raw, L["hl"])
        o["ls"] = r5(portfolio_returns(long_short_weights(sm_ls, bk.TOP_FRAC), tgt, bk.COST)[0])
        w = long_short_weights(sm_lo, bk.TOP_FRAC)
        net, _, turn = bk.long_book(w, sm_lo, tgt)
        ok = np.isfinite(sm_lo) & np.isfinite(tgt)
        cnt = ok.sum(1)
        ew = np.where(cnt > 0, np.where(ok, tgt, 0.0).sum(1) / np.maximum(cnt, 1), np.nan)
        held = (w > 0).sum(1)
        o.update(excess=r5(net), bench=r5(ew), total=r5(net + ew), long_turnover=float(np.nanmean(turn)),
                 ls_turnover=float(S["splits"]["utrain"]["ls_turnover"]), names_held=float(np.mean(held[held > 0])), universe=float(np.mean(cnt[cnt > 0])))
        out["objects"][name] = o
        a_, h_ = S["splits"]["utrain"], S["splits"]["holdout"]
        la, lh = L["splits"]["utrain"], L["splits"]["holdout"]
        print(f"{name[:52]:52s} {int(sign):+d} | {S['hl']:>3g} {a_['ls_sharpe']:5.2f} → {h_['ls_sharpe']:5.2f} ({a_['ls_ann']:+.1%} → {h_['ls_ann']:+.1%}) | "
              f"{L['hl']:>3g} {la['long_sharpe']:5.2f} → {lh['long_sharpe']:5.2f} ({la['long_ann']:+.1%} → {lh['long_ann']:+.1%}) | {lh['long_turnover']:.1%}", flush=True)
    mem.stop()
p = PARTURA_ROOT / (opt("--out") or "runs/_batch_B01/signal_books.json")
p.write_text(json.dumps(out, ensure_ascii=False, default=float), encoding="utf-8")
print(f"wrote {p} ({time.time() - t0:.0f}s)")
