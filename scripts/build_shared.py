"""Panels every study in a batch shares, built once.

* ``log_float_cap.npy``  log of the circulating market value on the decision day
* ``log_total_cap.npy``  log of the total market value
* ``log_turnover_rate.npy``  log(day amount) - log(float cap): how fast the float trades

F001 could not tell "low turnover" from "small cap" because the cube only has
Amt.  The daily capital files the tradable backtest already reads close that
gap: with cap and turnover rate as separate controls, a factor that loads on
trading activity can be told apart from one that loads on size.

All three use information available at the close of day t (the factor's own
information set); the label starts at t+1.

    python scripts/build_shared.py            # on the server
"""
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.guard import limit_threads  # noqa: E402

limit_threads(2)
import numpy as np  # noqa: E402

from partura.bridge import PARTURA_ROOT, alphacube_root, ensure_alphacube_on_path  # noqa: E402

ensure_alphacube_on_path()
sys.path.insert(0, str(alphacube_root() / "scripts"))
from alphacube.research import warmed_view  # noqa: E402
from alphacube.store import open_cube_store  # noqa: E402
from tearsheet import load_caps  # noqa: E402  (the other session's loader, read-only)

STORE = "/root/autodl-tmp/qmt_daily_data/fast_factor_compute"
CAP_DIR = "/root/autodl-tmp/qmt_daily_data/daily_capital"
AMOUNT = alphacube_root() / "_bench/tradable/amount_day.npy"
out = PARTURA_ROOT / "shared"
out.mkdir(exist_ok=True)

view, trim = warmed_view(open_cube_store(STORE, mirror_root=str(alphacube_root() / "mirror")),
                         "20180102", "20251231", warmup=60)
dates, symbols = list(view.dates[trim:]), list(view.symbols)
t0 = time.time()
cmv, tmv = load_caps(CAP_DIR, dates, symbols)
print(f"caps {cmv.shape} in {time.time() - t0:.0f}s; float cap finite {np.isfinite(cmv).mean():.3f}", flush=True)
with np.errstate(invalid="ignore", divide="ignore"):
    lf = np.where(cmv > 0, np.log(cmv), np.nan).astype(np.float32)
    lt = np.where(tmv > 0, np.log(tmv), np.nan).astype(np.float32)
np.save(out / "log_float_cap.npy", lf)
np.save(out / "log_total_cap.npy", lt)
if AMOUNT.is_file():
    amt = np.load(AMOUNT, mmap_mode="r")
    if amt.shape == cmv.shape:
        with np.errstate(invalid="ignore", divide="ignore"):
            tr = np.where((np.asarray(amt) > 0) & (cmv > 0), np.log(np.asarray(amt, dtype=np.float64) / cmv), np.nan)
        np.save(out / "log_turnover_rate.npy", tr.astype(np.float32))
        print(f"turnover rate finite {np.isfinite(tr).mean():.3f}", flush=True)
    else:
        print(f"amount_day shape {amt.shape} != {cmv.shape}; turnover rate not built", flush=True)
(out / "README.txt").write_text(
    f"built {time.strftime('%F %T')} from {CAP_DIR}; view {dates[0]}..{dates[-1]} x {len(symbols)} symbols\n",
    encoding="utf-8")
print("wrote", sorted(p.name for p in out.glob('*.npy')), flush=True)
