"""Shared fixtures of the K002 tooling tests: a small synthetic "world" (calendar, names, a planted label, a panel for each
expression the tests use) and a PanelSet stand-in that serves slices of it -- so the REAL scripts (scripts/sweep.py,
sweep_final.py, anatomy.py, group_final.py) run to completion without an engine, a store or a GPU, against a temporary
Partura root of their own (configs/, runs/, locks).
"""
import concurrent.futures
import runpy
import sys
import zlib
from pathlib import Path

import numpy as np
import yaml

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(ROOT))

from partura.bridge import ensure_alphacube_on_path  # noqa: E402

ensure_alphacube_on_path()
from alphacube.synthetic import trading_dates  # noqa: E402

KNOWN = "cross_mean(day_std(Amt), 30)"
XFROZEN = f"cs_last_high20(neg({KNOWN}), cross_max(day_zero_ratio(Ret), 15))"


def ar1(rng, d, s, rho):
    """Unit-variance AR(1) along days, independently per name: a slow signal (small turnover)."""
    e = rng.normal(size=(d, s))
    x = np.empty((d, s))
    x[0] = e[0]
    for t in range(1, d):
        x[t] = rho * x[t - 1] + np.sqrt(1 - rho ** 2) * e[t]
    return x


class Stop(Exception):
    """Raised by the stand-in PanelSet to end a script right where it builds one; carries what it was called with."""


class World:
    """Calendar + names + label + panels by expression.  ``x``, ``x2`` and ``x3`` are hidden persistent signals the label leans on; a panel
    is whatever array a test registers for an expression string (an expression with none gets reproducible noise)."""

    def __init__(self, n_days=420, n_names=80, seed=3, slope=8e-4, noise=0.015, rho=0.95):
        self.dates = trading_dates(n_days)
        self.symbols = [f"{600000 + i}.SH" for i in range(n_names)]
        self.rng = np.random.default_rng(seed)
        self.x = ar1(self.rng, n_days, n_names, rho)
        self.x2 = ar1(self.rng, n_days, n_names, rho)                   # a second, independent slow signal the label also leans on
        self.x3 = ar1(np.random.default_rng(seed + 1000), n_days, n_names, rho)       # a third, from a stream of its own (the others keep theirs)
        tgt = slope * (0.99 * self.x + 1.5 * self.x2 + 1.2 * self.x3) + noise * self.rng.normal(size=(n_days, n_names))
        self.dead = self.rng.random((n_days, n_names)) < 0.02          # suspended cells: no label, no signal
        tgt[self.dead] = np.nan
        tgt[-2:] = np.nan                                              # the last days have no label yet
        self.target = tgt
        self.panels = {}
        n = n_days
        # in-sample = days [0, a), test = [a, b), forward = [b, n)
        self.cut = {"train_end": int(n * 0.48), "valid_end": int(n * 0.67), "holdout_end": int(n * 0.86)}

    def noise(self):
        return self.rng.normal(size=self.x.shape)

    def set(self, expr, arr):
        a = np.asarray(arr, dtype=np.float64).copy()
        a[self.dead] = np.nan
        self.panels[expr] = a.astype(np.float32)
        return expr

    def panel(self, expr):
        if expr not in self.panels:
            rng = np.random.default_rng(zlib.crc32(expr.encode()))
            self.set(expr, rng.normal(size=self.x.shape))
        return self.panels[expr]

    def splits(self):
        d, c = self.dates, self.cut
        return {"train": [d[0], d[c["train_end"] - 1]], "valid": [d[c["train_end"]], d[c["valid_end"] - 1]],
                "utrain": [d[0], d[c["valid_end"] - 1]], "holdout": [d[c["valid_end"]], d[c["holdout_end"] - 1]],
                "full": [d[0], d[c["holdout_end"] - 1]]}


def fake_panelset(world, calls=None, stop_at_init=False, compute_log=None):
    """A PanelSet stand-in serving ``world``.  ``calls`` collects the constructor's arguments."""
    from partura.splits import SPLITS

    class FakePanelSet:
        def __init__(self, store_path, start, end, **kw):
            rec = {"store_path": store_path, "start": start, "end": end, **kw}
            if calls is not None:
                calls.append(rec)
            if stop_at_init:
                raise Stop(rec)
            self.rows = [i for i, d in enumerate(world.dates) if start <= d <= end]
            self.sl = slice(self.rows[0], self.rows[-1] + 1)
            self.dates = [world.dates[i] for i in self.rows]
            self.symbols = list(world.symbols)
            self.years = np.asarray([d[:4] for d in self.dates])
            self.errors = {}

        def compute(self, exprs):
            if compute_log is not None:
                compute_log.append(dict(exprs))
            return {n: world.panel(e)[self.sl].copy() for n, e in exprs.items()}

        def target(self, horizon=1):
            return world.target[self.sl].copy()

        def split_slice(self, split):
            a, b = SPLITS[split]
            d = np.asarray(self.dates)
            idx = np.nonzero((d >= a) & (d <= b))[0]
            if idx.size == 0:
                raise ValueError(f"split {split} ({a}..{b}) is empty in this view")
            return slice(int(idx[0]), int(idx[-1]) + 1)

    return FakePanelSet


def write_config(root, fid, world, expression=KNOWN, extra=None):
    cfg = {"factor_id": fid, "expression": expression, "label": {"kind": "open_vwap15", "horizon": 1, "buyable": True}, "warmup": 60,
           "splits": world.splits(), "stages": [], **(extra or {})}
    (root / "configs").mkdir(parents=True, exist_ok=True)
    (root / "configs" / f"{fid}.yaml").write_text(yaml.safe_dump(cfg, allow_unicode=True), encoding="utf-8")
    return cfg


def run_script(monkeypatch, root, script, argv, panelset_cls):
    """Run scripts/<script> as ``__main__`` against the temporary root ``root`` and the stand-in PanelSet.  Worker processes
    become threads (the scripts hand their workers a module global; threads see it as forks do)."""
    monkeypatch.setattr("partura.bridge.PARTURA_ROOT", root)
    monkeypatch.setattr("partura.panels.PanelSet", panelset_cls)
    monkeypatch.setattr(concurrent.futures, "ProcessPoolExecutor", concurrent.futures.ThreadPoolExecutor)
    monkeypatch.setattr(sys, "argv", [script] + list(argv))
    monkeypatch.setenv("PARTURA_LOCK_DIR", str(root / "locks"))
    monkeypatch.setenv("PARTURA_RANK_DEVICE", "")
    return runpy.run_path(str(SCRIPTS / script), run_name="__main__")


def stub_propose(monkeypatch, calls=None):
    """scripts/sweep.py's tree-derived candidates need the probe machinery; the tests stand a spy in its place."""
    def propose(src, **kw):
        if calls is not None:
            calls.append((src, kw))
        return []
    monkeypatch.setattr("partura.propose.propose", propose)
    return propose
