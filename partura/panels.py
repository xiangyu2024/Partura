"""Evaluate expressions on the AlphaCube cube, once, with a disk cache.

Everything downstream (metrics, ablations, conditional ICs, neutralisation)
reads panels from here.  Three deliberate choices:

* **One warmed view over the whole period, sliced afterwards.**  A split is a
  row range of the same panel, so train / valid / holdout numbers are
  guaranteed to come from identical computation, and no split costs an extra
  engine call.
* **One engine call per batch.**  The engine does common-subexpression
  elimination inside a call, and ablation variants share almost all of their
  subtrees, so a batch of 30 variants costs far less than 30 evaluations.
* **A content-addressed disk cache.**  The key is the parsed expression's
  structural key plus the view identity, so a re-run of a report costs no
  compute, and a changed view can never silently reuse an old panel.
"""

from __future__ import annotations

import hashlib
import json
import os
import time
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

from .bridge import ensure_alphacube_on_path

ensure_alphacube_on_path()

import numpy as np  # noqa: E402
import torch  # noqa: E402

from alphacube.engine.engine import CubeEngine  # noqa: E402
from alphacube.label import Label  # noqa: E402
from alphacube.parser import ParseError, parse  # noqa: E402
from alphacube.research import warmed_view  # noqa: E402
from alphacube.store import open_cube_store  # noqa: E402


def parse_research(src: str, n_minutes: int = 241):
    """Research parsing rules (same as ``alphacube.research.parse_many``):
    lenient operands, daily coercion for minute-free expressions, full catalog."""
    return parse(src, strict=False, coerce_daily=True, n_minutes=n_minutes, allow_general=True)


def _drop_page_cache(path: Path) -> None:
    """Tell the kernel we are done with this file (the server's page cache is
    the scarce resource; AlphaCube's own eval scripts do the same)."""
    try:
        fd = os.open(str(path), os.O_RDONLY)
        try:
            os.posix_fadvise(fd, 0, 0, os.POSIX_FADV_DONTNEED)
        finally:
            os.close(fd)
    except (OSError, AttributeError):
        pass


class PanelSet:
    def __init__(self, store_path: str, start: str, end: str, *, warmup: int = 60,
                 device: str = "cpu", chunk_symbols: Optional[int] = None, chunk_days: Optional[int] = None,
                 cache_dir: Optional[str] = None, mirror_root: Optional[str] = None,
                 max_symbols: Optional[int] = None, gpu_fraction: Optional[float] = None,
                 torch_threads: Optional[int] = None, workdir: Optional[str] = None,
                 label_kind: str = "open_vwap15", quiet: bool = False) -> None:
        if gpu_fraction and device.startswith("cuda"):
            torch.cuda.set_per_process_memory_fraction(float(gpu_fraction))
        self.store_path = store_path
        self.store = open_cube_store(store_path, mirror_root=mirror_root)
        self.view, self.trim = warmed_view(self.store, start, end, warmup, max_symbols=max_symbols)
        self.start, self.end, self.warmup = start, end, warmup
        self.device, self.chunk_symbols, self.chunk_days = device, chunk_symbols, chunk_days
        self.torch_threads, self.workdir = torch_threads, workdir
        self.label_kind = label_kind
        self.quiet = quiet
        self.dates: List[str] = list(self.view.dates[self.trim:])
        self.symbols: List[str] = list(self.view.symbols)
        self.years = np.asarray([d[:4] for d in self.dates])
        self.cache_dir = Path(cache_dir) if cache_dir else None
        if self.cache_dir:
            self.cache_dir.mkdir(parents=True, exist_ok=True)
        self._targets: Dict[int, np.ndarray] = {}
        self._mem: Dict[str, np.ndarray] = {}
        self._price: Optional[np.ndarray] = None
        self.errors: Dict[str, str] = {}

    # -- identity ---------------------------------------------------------
    @property
    def view_id(self) -> str:
        raw = f"{self.store_path}|{self.start}|{self.end}|{len(self.symbols)}|{self.dates[0]}|{self.dates[-1]}"
        return hashlib.sha1(raw.encode()).hexdigest()[:10]

    def _cache_path(self, expr_key: str) -> Optional[Path]:
        if not self.cache_dir:
            return None
        h = hashlib.sha1(f"{self.view_id}|{expr_key}".encode()).hexdigest()[:16]
        return self.cache_dir / f"{h}.npy"

    # -- labels -----------------------------------------------------------
    def target(self, horizon: int = 1) -> np.ndarray:
        if horizon not in self._targets:
            if self._price is None:
                self._price = Label(self.label_kind, 1).price(self.view)
            t = Label(self.label_kind, horizon).compute(self.view, price=self._price)
            self._targets[horizon] = np.asarray(t[self.trim:], dtype=np.float64)
        return self._targets[horizon]

    # -- evaluation -------------------------------------------------------
    def compute(self, expressions: Dict[str, str]) -> Dict[str, np.ndarray]:
        """name -> (n_days, n_symbols) float32 panel over the trimmed range."""
        parsed, keys = {}, {}
        for name, src in expressions.items():
            try:
                e = parse_research(src, n_minutes=self.store.n_minutes)
            except (ParseError, ValueError, TypeError) as exc:
                self.errors[name] = f"parse: {exc}"
                continue
            parsed[name], keys[name] = e, e.key()

        out: Dict[str, np.ndarray] = {}
        todo: Dict[str, object] = {}
        for name, e in parsed.items():
            if keys[name] in self._mem:
                out[name] = self._mem[keys[name]]
                continue
            p = self._cache_path(keys[name])
            if p is not None and p.is_file():
                arr = np.load(p)
                _drop_page_cache(p)
                self._mem[keys[name]] = arr
                out[name] = arr
                continue
            todo[name] = e
        if not todo:
            return out

        names = list(todo)
        exprs = [todo[n] for n in names]
        kw = {}
        if self.chunk_symbols:
            kw["chunk_symbols"] = self.chunk_symbols
        if self.chunk_days:
            kw["chunk_days"] = self.chunk_days
        if self.torch_threads:
            kw["torch_threads"] = self.torch_threads
        if self.workdir:
            kw["workdir"] = self.workdir
        engine = CubeEngine(self.view, device=self.device, **kw)
        t0 = time.perf_counter()
        if not self.quiet:
            print(f"[panels] evaluating {len(exprs)} expression(s) on "
                  f"{self.view.n_days - self.trim}d x {self.view.n_symbols}s "
                  f"(+{self.trim} warm-up), device={self.device}", flush=True)
        res = engine.evaluate(exprs, tolerant=True)
        for i, name in enumerate(names):
            err = res.errors.get(i)
            if err or res.panels[i] is None:
                self.errors[name] = f"evaluate: {err}"
                continue
            arr = np.asarray(res.panels[i][self.trim:], dtype=np.float32)
            self._mem[keys[name]] = arr
            out[name] = arr
            p = self._cache_path(keys[name])
            if p is not None:
                np.save(p, arr)
                _drop_page_cache(p)
                idx = self.cache_dir / "index.json"
                book = json.loads(idx.read_text()) if idx.is_file() else {}
                book[p.name] = {"expression": repr(todo[name]), "key": keys[name],
                                "view_id": self.view_id, "name": name}
                idx.write_text(json.dumps(book, ensure_ascii=False, indent=1), encoding="utf-8")
        if not self.quiet:
            print(f"[panels] done in {time.perf_counter() - t0:.0f}s"
                  f"{'; failed: ' + ', '.join(n for n in names if n in self.errors) if self.errors else ''}",
                  flush=True)
        return out

    # -- split slicing ----------------------------------------------------
    def split_slice(self, split: str) -> slice:
        from .splits import SPLITS
        a, b = SPLITS[split]
        d = np.asarray(self.dates)
        idx = np.nonzero((d >= a) & (d <= b))[0]
        if idx.size == 0:
            raise ValueError(f"split {split} ({a}..{b}) is empty in this view")
        return slice(int(idx[0]), int(idx[-1]) + 1)


__all__ = ["PanelSet", "parse_research"]
