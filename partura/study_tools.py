"""What a study's own analysis script needs, in one import.

A study often has a question no stock diagnostic answers -- "is the signal
only there on days the stock hit its limit?", "does the long leg survive if
the top 1% of names is dropped?".  Those analyses live in
``studies/<factor_id>/*.py`` and run on the server through
``scripts/study.sh exec``.  This module gives them the same panels, label,
splits and safety rails the runner uses, so a bespoke number is comparable
with a table number and cannot take the server down:

    from partura.study_tools import Study
    with Study("F107_abs_demean_skew_low") as st:
        p = st.panels({"x": "day_skew(Low)"})["x"]            # cached, GPU-locked
        tr = st.slice("train")
        print(st.books(p, fit="train", evals=("train", "valid")))

Never read ``holdout`` here: the holdout is read once, by the runner, with
``--holdout``, and that read is ledgered.  ``Study.slice("holdout")`` refuses.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Dict, Optional, Sequence

from . import guard

guard.limit_threads(2)

import numpy as np  # noqa: E402
import yaml  # noqa: E402

from . import books as bk  # noqa: E402
from . import diagnose as dg  # noqa: E402
from .bridge import PARTURA_ROOT  # noqa: E402
from .panels import SHARED_CACHE, PanelSet  # noqa: E402
from .splits import SPLITS  # noqa: E402

STORE = os.environ.get("PARTURA_STORE", "/root/autodl-tmp/qmt_daily_data/fast_factor_compute")
MIRROR = os.environ.get("PARTURA_MIRROR", "/root/autodl-tmp/AlphaCube/mirror")


class Study:
    def __init__(self, factor_id: str, device: str = "cuda", gpu_fraction: float = 0.0) -> None:
        self.fid = factor_id
        self.cfg = yaml.safe_load((PARTURA_ROOT / "configs" / f"{factor_id}.yaml").read_text(encoding="utf-8"))
        for k, v in (self.cfg.get("splits") or {}).items():
            SPLITS[k] = (str(v[0]), str(v[1]))
        self._device, self._frac = device, gpu_fraction
        self._slot = None
        self._mem: Optional[guard.MemoryGuard] = None
        self.ps: Optional[PanelSet] = None

    def __enter__(self) -> "Study":
        self._slot = guard.slot()
        self._slot.__enter__()
        self._mem = guard.MemoryGuard(self_limit_gb=float(os.environ.get("PARTURA_SELF_GB", 14)),
                                      cgroup_limit_gb=float(os.environ.get("PARTURA_CGROUP_GB", 34))).start()
        lab = self.cfg.get("label") or {}
        self.ps = PanelSet(STORE, SPLITS["full"][0], SPLITS["full"][1], warmup=int(self.cfg.get("warmup", 60)),
                           device=self._device, gpu_fraction=self._frac, cache_dir=str(SHARED_CACHE),
                           mirror_root=MIRROR, workdir=str(PARTURA_ROOT / "tmp"),
                           label_kind=lab.get("kind", "open_vwap15"), label_buyable=bool(lab.get("buyable", False)),
                           batch=3)
        return self

    def __exit__(self, *exc) -> None:
        if self._mem:
            self._mem.stop()
        if self._slot:
            self._slot.__exit__(*exc)

    # -- data -------------------------------------------------------------
    def panels(self, expressions: Dict[str, str]) -> Dict[str, np.ndarray]:
        out = self.ps.compute(expressions)
        for k, e in self.ps.errors.items():
            if k in expressions:
                print(f"[study] {k} failed: {e}", flush=True)
        return out

    def control(self, name: str) -> np.ndarray:
        """A control / known-family panel of this study's config, by name."""
        cfg = self.cfg
        if name in (cfg.get("external_controls") or {}):
            return self.ps.external(cfg["external_controls"][name])
        src = {**(cfg.get("controls") or {}), **(cfg.get("gates") or {})}[name]
        return self.panels({name: src})[name]

    def target(self, horizon: int = 1) -> np.ndarray:
        return self.ps.target(horizon)

    def slice(self, split: str) -> slice:
        if split in ("holdout", "full"):
            raise PermissionError("the holdout is read once, by `partura run --holdout`; not from an analysis script")
        return self.ps.split_slice(split)

    @property
    def dates(self):
        return self.ps.dates

    @property
    def symbols(self):
        return self.ps.symbols

    # -- the same numbers the tables print ---------------------------------
    def sign(self, panel: np.ndarray, split: str = "train") -> float:
        s = self.slice(split)
        return dg.sign_from(np.asarray(panel[s], dtype=np.float64), self.target()[s])

    def ic(self, panel: np.ndarray, split: str = "train", sign: Optional[float] = None) -> Dict[str, float]:
        s = self.slice(split)
        p = np.asarray(panel[s], dtype=np.float64)
        return dg.ic_row(p, self.target()[s], sign=self.sign(panel) if sign is None else sign)

    def books(self, panel: np.ndarray, fit: str = "train", evals: Sequence[str] = ("train", "valid"),
              sign: Optional[float] = None) -> Dict[str, object]:
        """Decile L/S and the long leg, in the user's convention (see partura.books)."""
        sg = self.sign(panel, fit) if sign is None else sign
        return bk.books(sg * np.asarray(panel, dtype=np.float64), self.target(), self.slice(fit),
                        {e: self.slice(e) for e in evals},
                        cost=float(self.cfg.get("cost_per_side", bk.COST)),
                        top_frac=float(self.cfg.get("top_frac", bk.TOP_FRAC)),
                        rank_by=self.cfg.get("rank_by", "ls"))

    def rank_corr(self, a: np.ndarray, b: np.ndarray, split: str = "train") -> float:
        s = self.slice(split)
        return dg.pair_rank_corr(a[s], b[s])


__all__ = ["Study", "bk", "dg"]
