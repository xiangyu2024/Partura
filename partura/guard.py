"""Being a good neighbour on a shared server.

Partura studies run next to whatever else the user has going (a mining run, a
scoring job with twenty workers).  Three things can hurt that other job, and
each has bitten this project before:

* **Memory.**  The container's practical anon ceiling is about 40 GB, and a
  CPU-engine evaluation of a hand-written factor has been measured at 40 GB on
  its own.  A blown ceiling does not raise in the offender -- it kills whoever
  the kernel picks.  ``MemoryGuard`` watches this process's anonymous RSS and
  the cgroup's total and exits the *Partura* process before either limit is
  reached.
* **GPU memory.**  A CUDA OOM inside the engine is swallowed per node and
  silently fails a tree in whichever job hits it.  Partura caps its own share
  (``--gpu-fraction``) and holds an exclusive file lock around every engine
  call, so at most one Partura evaluation is on the card at a time.
* **CPU.**  The quota is 25 cores and the neighbour may be using 20.  Partura
  runs with a couple of threads and at most ``PARTURA_SLOTS`` processes.

All locks are ``flock`` on files under ``$PARTURA_LOCK_DIR`` (default
``<partura>/tmp/locks``), so they vanish with the process even on SIGKILL.
"""

from __future__ import annotations

import contextlib
import fcntl
import os
import threading
import time
from pathlib import Path
from typing import Iterator, Optional

from .bridge import PARTURA_ROOT

GIB = 1 << 30


def lock_dir() -> Path:
    d = Path(os.environ.get("PARTURA_LOCK_DIR", PARTURA_ROOT / "tmp" / "locks"))
    d.mkdir(parents=True, exist_ok=True)
    return d


@contextlib.contextmanager
def exclusive(name: str, poll: float = 2.0, announce: bool = True) -> Iterator[None]:
    """Block until this process holds ``name``; release on exit."""
    path = lock_dir() / f"{name}.lock"
    fh = open(path, "a+")
    waited, said = 0.0, False
    try:
        while True:
            try:
                fcntl.flock(fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except BlockingIOError:
                if announce and not said:
                    print(f"[guard] waiting for lock '{name}' ...", flush=True)
                    said = True
                time.sleep(poll)
                waited += poll
        if said:
            print(f"[guard] got lock '{name}' after {waited:.0f}s", flush=True)
        yield
    finally:
        try:
            fcntl.flock(fh, fcntl.LOCK_UN)
        finally:
            fh.close()


@contextlib.contextmanager
def slot(n_slots: Optional[int] = None, poll: float = 3.0) -> Iterator[int]:
    """One of N process slots: bounds how many Partura runs exist at once."""
    n = int(n_slots or os.environ.get("PARTURA_SLOTS", 2))
    files = [open(lock_dir() / f"slot{i}.lock", "a+") for i in range(n)]
    got, said, waited = None, False, 0.0
    try:
        while got is None:
            for i, fh in enumerate(files):
                try:
                    fcntl.flock(fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
                    got = i
                    break
                except BlockingIOError:
                    continue
            if got is None:
                if not said:
                    print(f"[guard] all {n} run slots busy, waiting ...", flush=True)
                    said = True
                time.sleep(poll)
                waited += poll
        if said:
            print(f"[guard] got run slot {got} after {waited:.0f}s", flush=True)
        yield got
    finally:
        for fh in files:
            try:
                fcntl.flock(fh, fcntl.LOCK_UN)
            except OSError:
                pass
            fh.close()


def self_anon_gb() -> float:
    try:
        for line in open("/proc/self/status"):
            if line.startswith("RssAnon:"):
                return int(line.split()[1]) * 1024 / GIB
    except OSError:
        pass
    return float("nan")


def cgroup_anon_gb() -> float:
    try:
        for line in open("/sys/fs/cgroup/memory.stat"):
            if line.startswith("anon "):
                return int(line.split()[1]) / GIB
    except OSError:
        pass
    return float("nan")


class MemoryGuard:
    """Exit THIS process before memory becomes somebody else's problem."""

    def __init__(self, self_limit_gb: float = 14.0, cgroup_limit_gb: float = 34.0, every: float = 2.0) -> None:
        self.self_limit, self.cgroup_limit, self.every = self_limit_gb, cgroup_limit_gb, every
        self.peak = 0.0
        self._stop = threading.Event()
        self._t = threading.Thread(target=self._run, daemon=True)

    def start(self) -> "MemoryGuard":
        me, cg = self_anon_gb(), cgroup_anon_gb()
        if cg == cg and cg > self.cgroup_limit - 4.0:
            raise SystemExit(f"[guard] container anon is already {cg:.1f} GiB (limit {self.cgroup_limit}); "
                             f"not starting a Partura run on top of it")
        if me == me:                                   # /proc exists: we are on Linux
            self._t.start()
        return self

    def _run(self) -> None:
        while not self._stop.wait(self.every):
            me, cg = self_anon_gb(), cgroup_anon_gb()
            if me == me:
                self.peak = max(self.peak, me)
            if (me == me and me > self.self_limit) or (cg == cg and cg > self.cgroup_limit):
                print(f"[guard] ABORT: this process anon {me:.1f} GiB (limit {self.self_limit}), "
                      f"container anon {cg:.1f} GiB (limit {self.cgroup_limit}). "
                      f"Exiting so the neighbouring job is not the one that gets killed.", flush=True)
                os._exit(97)

    def stop(self) -> None:
        self._stop.set()


def limit_threads(n: int = 2) -> None:
    """Call before numpy/torch spin up their pools."""
    for k in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
        os.environ.setdefault(k, str(n))
    try:
        import torch
        torch.set_num_threads(n)
    except Exception:
        pass


__all__ = ["exclusive", "slot", "MemoryGuard", "limit_threads", "self_anon_gb", "cgroup_anon_gb", "lock_dir"]
