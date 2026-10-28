"""C04 smoke (server, seconds): the six daily-field leaves resolve on this host's store, cover the stocks, and are the
same on both hosts (a fingerprint of each panel is printed; compare the two hosts' lines).

    PARTURA_DAILY_ROOT=<dir> python scripts/server/c04_smoke.py
"""
import hashlib
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import numpy as np  # noqa: E402

from partura.panels import SHARED_CACHE, PanelSet  # noqa: E402

STORE = os.environ.get("PARTURA_STORE", "/root/autodl-tmp/qmt_daily_data/fast_factor_compute")
MIRROR = os.environ.get("PARTURA_MIRROR", "/root/autodl-tmp/AlphaCube/mirror")
MIRROR = MIRROR if MIRROR and os.path.isdir(MIRROR) else None
ps = PanelSet(STORE, "20180102", "20230807", warmup=60, device="cuda", gpu_fraction=0, cache_dir=str(SHARED_CACHE), mirror_root=MIRROR,
              workdir=str(Path(__file__).resolve().parents[2] / "tmp"), label_kind="open_vwap15", label_buyable=True, batch=8,
              daily_root=os.environ["PARTURA_DAILY_ROOT"])
exprs = {"cap": "LogFloatCap", "tcap": "LogTotalCap", "sh": "ts_delta(LogFloatShares, 20)", "lim": "LimitWidth", "board": "BoardCode",
         "age": "ListAge", "mix": "cs_rank(div(LogFloatCap, cross_mean(day_sum(Amt), 30)))"}
out = ps.compute(exprs)
ref = np.isfinite(ps.compute({"c": "day_last(Close)"})["c"])
for k, e in exprs.items():
    v = np.asarray(out[k], np.float64)
    fin = np.isfinite(v)
    h = hashlib.md5(np.round(np.where(fin, v, 0), 6).tobytes()).hexdigest()[:10]
    print(f"{k:6s} {e:55s} shape {v.shape} finite|traded {fin[ref].mean():.3f} mean {np.nanmean(v):+.4g} md5 {h}")
