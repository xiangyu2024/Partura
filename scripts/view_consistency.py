"""Are panels computed on two views of different length the same on the days they share?

Server.  A causal expression evaluated on 2018-01 ~ 2025-12 and on 2018-01 ~ 2026-09 must agree on every day up to
2025-12: a difference means either look-ahead (an operator that uses data after the day) or numerical noise (chunk
boundaries, summation order).  This loads both cached panels of every expression of the forward read and compares
them on the overlap -- values only, no returns, nothing after the shorter view's last day.

    python scripts/view_consistency.py [--short 20251231] [--long 20260916] [--only F113.orig,...]
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.guard import limit_threads, slot  # noqa: E402

limit_threads(8)
import numpy as np  # noqa: E402

from partura import ops_ext  # noqa: E402,F401
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.panels import SHARED_CACHE, PanelSet  # noqa: E402

argv = sys.argv[1:]


def opt(name, default=None):
    return argv[argv.index(name) + 1] if name in argv else default


SHORT, LONG = opt("--short", "20251231"), opt("--long", "20260916")
J = json.loads((PARTURA_ROOT / "runs" / "_batch_B01" / "fuse_s4.json").read_text(encoding="utf-8"))
K1 = json.loads((PARTURA_ROOT / "runs" / "K001_known_screens" / "sweepfinal_s1.json").read_text(encoding="utf-8"))["results"]
E4 = json.loads((PARTURA_ROOT / "episodes" / "e4k1_e4k2_e4k3_final.json").read_text(encoding="utf-8"))["results"]
exprs = {"aux:frozen": "cross_max(day_zero_ratio(Ret), 15)", "aux:age": "cross_valid_count(day_last(Close), 241)", "aux:liq": "cross_mean(day_sum(Amt), 30)"}
exprs.update({f"m:{k}": v["expr"] for k, v in J["members"].items()})
exprs.update({f"k:{k}": v["expr"] for k, v in K1.items()})
exprs.update({f"e:{i}": r["expr"] for i, r in enumerate(E4)})
only = set((opt("--only") or "").split(",")) - {""}
if only:
    exprs = {k: v for k, v in exprs.items() if k.split(":", 1)[1] in only}

with slot():
    kw = dict(warmup=60, device="cuda", gpu_fraction=0, cache_dir=str(SHARED_CACHE), mirror_root="/root/autodl-tmp/AlphaCube/mirror",
              workdir=str(PARTURA_ROOT / "tmp"), label_kind="open_vwap15", label_buyable=True, batch=32)
    a = PanelSet("/root/autodl-tmp/qmt_daily_data/fast_factor_compute", "20180102", SHORT, **kw)
    b = PanelSet("/root/autodl-tmp/qmt_daily_data/fast_factor_compute", "20180102", LONG, **kw)
    PA, PB = a.compute(exprs), b.compute(exprs)
    n = len(a.dates)
    assert list(a.dates) == list(b.dates)[:n], "the two views do not share their first days"
    print(f"{len(exprs)} expressions; overlap {n} days ({a.dates[0]} .. {a.dates[-1]}); columns {PA[next(iter(PA))].shape[1]} / {PB[next(iter(PB))].shape[1]}")
    print(f"{'name':34s} {'cells differing':>16s} {'nan pattern differs':>20s} {'max |rel diff|':>15s} {'days touched':>13s} {'first / last day touched':>26s} {'mean daily rank corr':>21s}")
    out = {}
    for k in exprs:
        x, y = np.asarray(PA[k], np.float64), np.asarray(PB[k][:n], np.float64)
        fx, fy = np.isfinite(x), np.isfinite(y)
        both = fx & fy
        with np.errstate(invalid="ignore", divide="ignore"):
            rel = np.where(both, np.abs(x - y) / np.maximum(np.maximum(np.abs(x), np.abs(y)), 1e-300), 0.0)
        diff = both & (x != y)
        nanp = int((fx != fy).sum())
        days = np.nonzero(diff.any(1) | (fx != fy).any(1))[0]
        if days.size:
            # rank correlation per day on the cells both have (how much the ORDER moved)
            rc = []
            for d in days[:: max(1, days.size // 60)]:
                m = both[d]
                if m.sum() > 50:
                    rx, ry = np.argsort(np.argsort(x[d, m])), np.argsort(np.argsort(y[d, m]))
                    rc.append(np.corrcoef(rx, ry)[0, 1])
            rcm = float(np.mean(rc)) if rc else float("nan")
        else:
            rcm = 1.0
        out[k] = {"cells_differing": int(diff.sum()), "share": float(diff.sum() / max(both.sum(), 1)), "nan_pattern": nanp, "max_rel": float(rel.max()),
                  "days": int(days.size), "first": str(a.dates[days[0]]) if days.size else None, "last": str(a.dates[days[-1]]) if days.size else None, "rank_corr": rcm}
        o = out[k]
        if o["cells_differing"] or o["nan_pattern"]:
            print(f"{k[:34]:34s} {o['cells_differing']:>9d} ({o['share']:.2%}) {o['nan_pattern']:>20d} {o['max_rel']:>15.2e} {o['days']:>13d} {str(o['first']) + ' / ' + str(o['last']):>26s} {o['rank_corr']:>21.6f}")
    same = [k for k, o in out.items() if not o["cells_differing"] and not o["nan_pattern"]]
    print(f"\nbit-identical on the overlap: {len(same)} of {len(out)} expressions")
(PARTURA_ROOT / "runs" / "_forward").mkdir(parents=True, exist_ok=True)
(PARTURA_ROOT / "runs" / "_forward" / f"view_consistency_{SHORT}_{LONG}.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
