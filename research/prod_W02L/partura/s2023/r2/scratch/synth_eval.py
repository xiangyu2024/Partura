"""Mechanical check on a SYNTHETIC cube only (no real data): does each seed evaluate, what coverage / distinct share."""
import os, sys, warnings, tempfile, time
warnings.filterwarnings("ignore")
ROOT = "/Users/wxy/Desktop/Partura-prod"
os.environ.setdefault("ALPHACUBE_ROOT", os.path.expanduser("~/Desktop/AlphaCube-steering"))
sys.path.insert(0, ROOT); sys.path.insert(0, os.path.join(os.environ["ALPHACUBE_ROOT"], "src"))
import numpy as np
from partura import ops_ext  # noqa
from partura.steer import Guidance
from alphacube.parser import parse
from alphacube.plugins import load_plugins
from alphacube.store import CubeStore
from alphacube.synthetic import make_synthetic_cube, write_synthetic_store, write_daily_fields
from alphacube.engine.engine import CubeEngine
load_plugins(["partura.ac_plugin"])
G0 = Guidance.load(os.path.join(ROOT, "guidance", "C05_base.yaml"))
tmp = tempfile.mkdtemp(prefix="synth_")
NS, ND = 80, 320
cubes, symbols, dates, status, planes = make_synthetic_cube(n_symbols=NS, n_days=ND, n_minutes=241, seed=3, suspended_frac=0.03, unlisted_days=0, daily_fields=("FloatCap", "TotalCap", "FloatShares"))
store = write_synthetic_store(os.path.join(tmp, "cube"), n_symbols=NS, n_days=ND, n_minutes=241, seed=3, suspended_frac=0.03, unlisted_days=0)
droot = write_daily_fields(os.path.join(tmp, "daily"), planes, store.symbols, store.dates)
view = CubeStore(store.directory, daily_root=droot).view()
eng = CubeEngine(view, device="cpu")
exprs = [l.strip() for l in open(sys.argv[1]).read().splitlines() if l.strip() and not l.startswith("#")]
for e in exprs:
    try:
        t = parse(G0.canonical(e), strict=True, coerce_daily=True, n_minutes=241, allow_general=True)
        t0 = time.time()
        res = eng.evaluate([t])
        if res.errors: print("ERR", res.errors, "|", e[:110]); continue
        p = res.panels[0]  # (D, S)
        fin = np.isfinite(p)
        cov = fin.mean(); late = fin[250:].mean()
        v = p[250:][np.isfinite(p[250:])]
        dist = len(np.unique(v)) / max(len(v), 1)
        print(f"cov {cov:.2f} late-cov {late:.2f} distinct {dist:.2f} [{time.time()-t0:.1f}s] {e[:115]}")
    except Exception as exc:
        print("EXC", type(exc).__name__, str(exc)[:100], "|", e[:110])
