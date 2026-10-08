"""The accelerated reward against the reference, on real panels and on the search's own grid: same numbers? how much faster?

Server.  Builds the reward context exactly as scripts/idea_search.py does (the search's view, 2018-01 ~ 2023-08-07),
takes a handful of real factor panels (cached ones cost nothing) and scores each under every reward twice:
``partura.steer.reward`` with PARTURA_REWARD_DEVICE unset (the numpy reference) and ``partura.steer_fast.reward_fast``
on the GPU.  Prints the largest difference and the time per call.  Reads train / valid only.

    python scripts/reward_bench.py [--n 8] [--device cuda]
"""
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.guard import MemoryGuard, limit_threads, slot  # noqa: E402

limit_threads(8)
import math  # noqa: E402

import numpy as np  # noqa: E402

from partura import books as bk  # noqa: E402
from partura import diagnose as dg  # noqa: E402
from partura import ops_ext  # noqa: E402,F401
from partura import steer, steer_fast  # noqa: E402
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.panels import SHARED_CACHE, PanelSet  # noqa: E402

argv = sys.argv[1:]
N = int(argv[argv.index("--n") + 1]) if "--n" in argv else 8
DEV = argv[argv.index("--device") + 1] if "--device" in argv else "cuda"
START, END, SPLIT = "20180102", "20230807", "20220101"
EXPRS = ["cross_mean(day_std(Amt), 30)", "cross_max(day_zero_ratio(Ret), 15)", "cross_mean(day_at_max_ratio(Vwap), 15)",
         "abs_(cs_demean(day_std(Ret)))", "cross_mean(day_gini(Ret), 30)", "ts_std(day_topw_mean(Volume, Close), 20)",
         "day_zero_ratio(Ret)", "cs_bucket_rank(cross_mean(day_gini(Ret), 5), cross_mean(day_sum(Amt), 30))",
         "day_min(nt_ts_delta(Amt, 3))", "cross_mean(day_sum(Amt), 30)", "ts_spearman(day_quantile(Close), 10)", "day_skew(Low)"][:N]

with slot():
    mem = MemoryGuard(self_limit_gb=34, cgroup_limit_gb=70).start()
    G = steer.Guidance.load(PARTURA_ROOT / "guidance" / "B01.yaml")
    ps = PanelSet("/root/autodl-tmp/qmt_daily_data/fast_factor_compute", START, END, warmup=60, device="cuda", gpu_fraction=0,
                  cache_dir=str(SHARED_CACHE), mirror_root="/root/autodl-tmp/AlphaCube/mirror", workdir=str(PARTURA_ROOT / "tmp"),
                  label_kind="open_vwap15", label_buyable=True, batch=8)
    pool_spec = G.spec["pool"][-1]
    aux = ps.compute({"frozen": "cross_max(day_zero_ratio(Ret), 15)", "age": "cross_valid_count(day_last(Close), 241)",
                      "liq": "cross_mean(day_sum(Amt), 30)", "pool": pool_spec["expr"], "known": G.spec["pool"][0]["expr"]})
    tgt = ps.target(1)
    dates = np.asarray(ps.dates)
    cut = int(np.searchsorted(dates, SPLIT))
    frozen = np.asarray(aux["frozen"], np.float64)
    possible = np.minimum(241, np.arange(1, len(dates) + 1))[:, None]
    untradable = ((dg._zrank(frozen) + 0.5) > 0.8) | (np.asarray(aux["age"], np.float64) < 0.9 * possible) | ~np.isfinite(frozen)
    pool_sig = dg._zrank(bk.smoothed(float(pool_spec["sign"]) * np.asarray(aux["pool"], np.float64), float(pool_spec["hl"])))

    def ctx():
        return steer.RewardContext(tgt, slice(0, cut), slice(cut, len(dates)), untradable=untradable, liq=np.asarray(aux["liq"], np.float64),
                                   pool=pool_sig, base=pool_sig, halflives=(0.0, 5, 20))

    P = ps.compute({f"p{i}": e for i, e in enumerate(EXPRS)})
    os.environ.pop("PARTURA_REWARD_DEVICE", None)

    def diff(a, b):
        if isinstance(a, dict):
            return max([diff(a[k], b[k]) for k in a] + [0.0 if set(a) == set(b) else float("inf")])
        if isinstance(a, (bool, str)):
            return 0.0 if a == b else float("inf")
        if a != a or b != b:
            return 0.0 if (a != a and b != b) else float("inf")
        if math.isinf(a) or math.isinf(b):
            return 0.0 if a == b else float("inf")
        return abs(a - b) / max(1.0, abs(a), abs(b))

    cr, cf = ctx(), ctx()
    steer_fast.reward_fast(P["p0"], cf, "long", device=DEV)             # warm the device and the context tensors
    print(f"{len(dates)} days x {tgt.shape[1]} names; {len(P)} panels; device {DEV}\n{'reward':14s} {'reference':>10s} {'fast':>8s} {'x':>6s}  max rel diff   (score of each panel, fast path)")
    worst = 0.0
    for kind in steer.REWARDS:
        tr = tf = 0.0
        dmax, scores = 0.0, []
        for k, p in P.items():
            t = time.time(); a = steer.reward(p, cr, kind); tr += time.time() - t
            t = time.time(); b = steer_fast.reward_fast(p, cf, kind, device=DEV); tf += time.time() - t
            dmax = max(dmax, diff(a, b))
            scores.append(b["score"])
        worst = max(worst, dmax)
        print(f"{kind:14s} {tr / len(P):9.2f}s {tf / len(P):7.2f}s {tr / max(tf, 1e-9):5.1f}x  {dmax:.2e}      " + " ".join(f"{s:+.2f}" for s in scores), flush=True)
    print(f"\nlargest relative difference over every number returned: {worst:.2e}  ->  {'SAME' if worst < 1e-9 else 'DIFFERENT'}")
    mem.stop()
