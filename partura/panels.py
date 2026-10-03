"""Evaluate expressions on the AlphaCube cube, once, with a disk cache.

Everything downstream (metrics, ablations, conditional ICs, neutralisation)
reads panels from here.  Deliberate choices:

* **One warmed view over the whole period, sliced afterwards.**  A split is a
  row range of the same panel, so train / valid / holdout numbers are
  guaranteed to come from identical computation.
* **A content-addressed disk cache**, shared by every study (``runs/_panels``).
  The key is the parsed expression's structural key plus the view identity, so
  a control or a sub-tree computed for one factor is free for the next, and a
  changed view can never silently reuse an old panel.  Writes are atomic
  (temp file + rename) because several studies run at once.
* **Small batches, one GPU job at a time.**  Heavy operators evaluated together
  blow GPU memory (the other session's ``pick_single_factors --verify``
  evaluates one expression at a time for the same reason), so expressions go
  to the engine in batches of ``batch`` under an exclusive file lock.  An
  expression that still fails on memory is retried alone with a smaller chunk.
* **No silent CPU fallback.**  A CPU-engine evaluation of a hand-written factor
  has been measured at ~40 GB of anonymous memory, which is the whole
  container.  It has to be asked for (``cpu_fallback=True``).
"""

from __future__ import annotations

import hashlib
import json
import os
import time
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

from .bridge import PARTURA_ROOT, ensure_alphacube_on_path
from . import guard

ensure_alphacube_on_path()

import numpy as np  # noqa: E402
import torch  # noqa: E402

from alphacube.engine.engine import CubeEngine  # noqa: E402
from alphacube.label import Label  # noqa: E402
from alphacube.parser import ParseError, parse  # noqa: E402
from alphacube.research import warmed_view  # noqa: E402
from alphacube.store import open_cube_store  # noqa: E402

SHARED_CACHE = PARTURA_ROOT / "runs" / "_panels"


def parse_research(src: str, n_minutes: int = 241):
    """Strict first (the search grammar), then the research relaxations -- the
    same order ``pick_single_factors.reevaluate`` uses, so a string means the
    same tree here as in the library it came from."""
    try:
        return parse(src)
    except (ParseError, ValueError, TypeError):
        return parse(src, strict=False, coerce_daily=True, n_minutes=n_minutes, allow_general=True)


def _drop_page_cache(path: Path) -> None:
    try:
        fd = os.open(str(path), os.O_RDONLY)
        try:
            os.posix_fadvise(fd, 0, 0, os.POSIX_FADV_DONTNEED)
        finally:
            os.close(fd)
    except (OSError, AttributeError):
        pass


def _atomic_save(path: Path, arr: np.ndarray) -> None:
    tmp = path.with_suffix(f".{os.getpid()}.tmp.npy")
    np.save(tmp, arr)
    os.replace(tmp, path)


def _is_oom(msg: Optional[str]) -> bool:
    return bool(msg) and ("out of memory" in msg.lower() or "outofmemory" in msg.lower())


class PanelSet:
    def __init__(self, store_path: str, start: str, end: str, *, warmup: int = 60,
                 device: str = "cpu", chunk_symbols: Optional[int] = None, chunk_days: Optional[int] = None,
                 cache_dir: Optional[str] = None, mirror_root: Optional[str] = None,
                 max_symbols: Optional[int] = None, gpu_fraction: Optional[float] = None,
                 torch_threads: Optional[int] = None, workdir: Optional[str] = None,
                 label_kind: str = "open_vwap15", label_buyable: bool = False,
                 batch: int = 4, cpu_fallback: bool = False, chunk_bytes: Optional[int] = None,
                 quiet: bool = False) -> None:
        self.gpu_fraction = gpu_fraction
        if gpu_fraction and device.startswith("cuda"):
            torch.cuda.set_per_process_memory_fraction(float(gpu_fraction))
        self.store_path = store_path
        self.store = open_cube_store(store_path, mirror_root=mirror_root)
        self.view, self.trim = warmed_view(self.store, start, end, warmup, max_symbols=max_symbols)
        self.start, self.end, self.warmup = start, end, warmup
        self.device, self.chunk_symbols, self.chunk_days = device, chunk_symbols, chunk_days
        self.torch_threads, self.workdir = torch_threads, workdir
        self.label_kind, self.label_buyable = label_kind, bool(label_buyable)
        self.batch, self.cpu_fallback = max(1, int(batch)), bool(cpu_fallback)
        if chunk_bytes is None and gpu_fraction and device.startswith("cuda"):
            total = torch.cuda.get_device_properties(0).total_memory
            chunk_bytes = int(max(128 << 20, min(2 << 30, total * float(gpu_fraction) / 12)))
        self.chunk_bytes = chunk_bytes
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
        self._locks: Optional[np.ndarray] = None
        self.errors: Dict[str, str] = {}
        self.timings: List[dict] = []

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
            tag = f"__label__|{self.label_kind}|h{horizon}|buyable{int(self.label_buyable)}"
            p = self._cache_path(tag)
            if p is not None and p.is_file():
                self._targets[horizon] = np.load(p)
                return self._targets[horizon]
            if self._price is None:
                self._price = Label(self.label_kind, 1).price(self.view)
            full = Label(self.label_kind, horizon).compute(self.view, price=self._price.copy())
            if self.label_buyable:
                # Same rule as Label(buyable=True) -- a name that opens locked at
                # limit-up on the entry day cannot be bought, so its label is
                # dropped -- but the lock table is read once, not once per horizon
                # (it scans the opening window of every day; five extra horizons
                # used to cost five extra scans).  The runner still checks the
                # h=1 result against the user's own label file, cell for cell.
                if self._locks is None:
                    from alphacube.tradability import entry_locks
                    self._locks = entry_locks(self.view)[0]
                lag = 1
                full[:-lag][self._locks[lag:]] = np.nan
            t = np.asarray(full[self.trim:], dtype=np.float64)
            self._targets[horizon] = t
            if p is not None:
                _atomic_save(p, t)
        return self._targets[horizon]

    def external(self, path: str) -> np.ndarray:
        """A (n_days, n_symbols) panel somebody else computed (market cap, a
        library panel).  Shape is checked; alignment is the caller's claim."""
        a = np.load(path, mmap_mode="r")
        if a.shape != (len(self.dates), len(self.symbols)):
            raise ValueError(f"{path}: shape {a.shape} != view {(len(self.dates), len(self.symbols))}")
        out = np.array(a, dtype=np.float32)            # a COPY: a memory-mapped file is read-only
        out[~np.isfinite(out)] = np.nan
        return out

    # -- evaluation -------------------------------------------------------
    def _engine(self, device: str, chunk_bytes: Optional[int] = None) -> CubeEngine:
        kw = {}
        if device.startswith("cuda"):
            if self.chunk_symbols:
                kw["chunk_symbols"] = self.chunk_symbols
            if self.chunk_days:
                kw["chunk_days"] = self.chunk_days
            cb = chunk_bytes or self.chunk_bytes
            if cb:
                kw["chunk_bytes"] = int(cb)
        if self.torch_threads:
            kw["torch_threads"] = self.torch_threads
        if self.workdir:
            kw["workdir"] = self.workdir
        return CubeEngine(self.view, device=device, **kw)

    def _evaluate(self, exprs: List[object], names: List[str]) -> Tuple[List[Optional[np.ndarray]], Dict[int, str]]:
        """One batch on the configured device, with the retry ladder for memory."""
        t0 = time.perf_counter()
        res = self._engine(self.device).evaluate(exprs, tolerant=True)
        panels, errs = list(res.panels), dict(res.errors)
        self.timings.append({"names": list(names), "seconds": round(time.perf_counter() - t0, 1)})
        retry = [i for i in sorted(errs) if _is_oom(errs[i])]
        if retry and str(self.device).startswith("cuda"):
            for i in retry:                           # alone, with a quarter of the chunk
                torch.cuda.empty_cache()
                small = max(64 << 20, int((self.chunk_bytes or (2 << 30)) // 4))
                if not self.quiet:
                    print(f"[panels] {names[i]}: GPU memory; retrying alone with chunk {small >> 20} MiB",
                          flush=True)
                r1 = self._engine(self.device, chunk_bytes=small).evaluate([exprs[i]], tolerant=True)
                if r1.errors.get(0) is None and r1.panels[0] is not None:
                    panels[i] = r1.panels[0]
                    errs.pop(i, None)
                else:
                    errs[i] = f"{errs[i]} | retry alone: {r1.errors.get(0)}"
        left = sorted(errs)
        if left and self.cpu_fallback and not str(self.device).startswith("cpu"):
            if not self.quiet:
                print(f"[panels] CPU fallback for: {', '.join(names[i] for i in left)}", flush=True)
            r2 = CubeEngine(self.view, device="cpu",
                            **({"workdir": self.workdir} if self.workdir else {})
                            ).evaluate([exprs[i] for i in left], tolerant=True)
            for j, i in enumerate(left):
                if r2.errors.get(j) is None and r2.panels[j] is not None:
                    panels[i] = r2.panels[j]
                    errs.pop(i, None)
                else:
                    errs[i] = f"{errs[i]} | cpu: {r2.errors.get(j)}"
        if str(self.device).startswith("cuda"):
            torch.cuda.empty_cache()
        return panels, errs

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

        # identical trees under different names are evaluated once
        by_key: Dict[str, List[str]] = {}
        for name in todo:
            by_key.setdefault(keys[name], []).append(name)
        uniq = [names[0] for names in by_key.values()]
        t0 = time.perf_counter()
        if not self.quiet:
            print(f"[panels] {len(uniq)} new expression(s) on {self.view.n_days - self.trim}d x "
                  f"{self.view.n_symbols}s (+{self.trim} warm-up), device={self.device}, "
                  f"batches of {self.batch}", flush=True)
        for b0 in range(0, len(uniq), self.batch):
            chunk = uniq[b0:b0 + self.batch]
            with guard.exclusive("gpu", announce=not self.quiet):
                # another study may have produced it while we were waiting for the card
                still = []
                for n in chunk:
                    p = self._cache_path(keys[n])
                    if p is not None and p.is_file():
                        arr = np.load(p)
                        self._mem[keys[n]] = arr
                        for alias in by_key[keys[n]]:
                            out[alias] = arr
                    else:
                        still.append(n)
                if not still:
                    continue
                panels, errs = self._evaluate([todo[n] for n in still], still)
            for i, n in enumerate(still):
                if errs.get(i) or panels[i] is None:
                    for alias in by_key[keys[n]]:
                        self.errors[alias] = f"evaluate: {errs.get(i)}"
                    continue
                arr = np.asarray(panels[i][self.trim:], dtype=np.float32)
                arr[~np.isfinite(arr)] = np.nan            # inf is never a tradable value
                self._mem[keys[n]] = arr
                for alias in by_key[keys[n]]:
                    out[alias] = arr
                p = self._cache_path(keys[n])
                if p is not None:
                    _atomic_save(p, arr)
                    _drop_page_cache(p)
                    p.with_suffix(".json").write_text(json.dumps(
                        {"expression": repr(todo[n]), "key": keys[n], "view_id": self.view_id, "name": n},
                        ensure_ascii=False), encoding="utf-8")
            if not self.quiet:
                print(f"[panels]   {min(b0 + self.batch, len(uniq))}/{len(uniq)} "
                      f"({time.perf_counter() - t0:.0f}s)", flush=True)
        if not self.quiet:
            bad = [n for n in todo if n in self.errors]
            print(f"[panels] done in {time.perf_counter() - t0:.0f}s"
                  f"{'; failed: ' + ', '.join(bad) if bad else ''}", flush=True)
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


__all__ = ["PanelSet", "parse_research", "SHARED_CACHE"]
