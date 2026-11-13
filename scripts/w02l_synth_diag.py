"""W02L synth: where S's drawdown sits and how small its long book is, vs C_LX (cut view, nothing of 2026)."""
import os, sys, json
sys.path.insert(0, os.getcwd())
from partura.guard import limit_threads
limit_threads(16)
import numpy as np
from partura import books as bk, diagnose as dg
from alphacube.research import warmed_view
from alphacube.store import open_cube_store
from alphacube.label import Label, open_vwap15
from alphacube.metrics import long_short_weights, zscore_rows
W = "runs/prod_W02L/two_level"
view, _ = warmed_view(open_cube_store("/root/autodl-tmp/qmt_daily_data/fast_factor_compute"), "20180102", "20251231", warmup=60)
dates = np.asarray([str(d) for d in view.dates]); n = len(dates)
tgt = Label("open_vwap15", 1, buyable=True).compute(view, price=open_vwap15(view)).astype(np.float64)
from alphacube.plugins import load_plugins; load_plugins(["partura.ac_plugin"])
from partura.panels import SHARED_CACHE, PanelSet
ps = PanelSet("/root/autodl-tmp/qmt_daily_data/fast_factor_compute", "20180102", "20251231", warmup=60, device="cpu", cache_dir=str(SHARED_CACHE), mirror_root=os.environ.get("PARTURA_MIRROR"), workdir="tmp", daily_root=os.environ.get("PARTURA_DAILY_ROOT") or None)
P_ = ps.compute({"c": "LogFloatCap"}); print("cap err", ps.errors.get("c")) if "c" not in P_ else None; cap = np.asarray(P_["c"], np.float64)[:n]
capr = dg.rank_rows(cap); capr = capr / np.isfinite(capr).sum(1, keepdims=True)
va = int(np.searchsorted(dates, "20230808"))
for nm, hl in (("C_LX", 60), ("S", 5), ("S_nested", 10)):
    s = np.load(f"{W}/{nm}.npy")[:n].astype(np.float64)
    sm = bk.smoothed(s, hl)
    w = long_short_weights(sm, bk.TOP_FRAC)
    lw = np.where(w > 0, w, 0.0)
    ex = bk.long_book(w, sm, tgt)[0]
    sz = np.nansum(lw * np.nan_to_num(capr), 1) / np.maximum(lw.sum(1), 1e-12)
    eq = np.nancumsum(np.nan_to_num(ex)); peak = np.maximum.accumulate(eq); dd = eq - peak
    t = int(np.argmin(dd)); p = int(np.argmax(eq[:t + 1]))
    worst = sorted(range(va, n), key=lambda i: np.nan_to_num(ex[i]))[:3]
    print(f"{nm:9s} hl {hl:>2}: long-book mean size pct all {np.nanmean(sz):.3f} valid {np.nanmean(sz[va:]):.3f} | "
          f"max dd {dd[t]:+.1%} from {dates[p]} to {dates[t]} | worst valid days " + ", ".join(f"{dates[i]} {ex[i]:+.1%}" for i in worst), flush=True)
