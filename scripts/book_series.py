"""Daily return series of a few named books, for plotting: the decile long/short book, the pure long book's TOTAL
return, and the equal-weight universe it is measured against.

Server.  Objects are rebuilt from stored results without refitting anything:
    fusion:<X>           a fusion of runs/_batch_<B>/fuse_<tag>.json (members, signs, half-lives and the fusion's
                         own half-life as stored)
    <fid>.<cid>@<view>   a candidate of runs/<fid>*/sweepfinal_<tag>.json at the half-life of the given convention
                         (view = ls | long)
The view ends at --end (default 20251231: nothing after the old test period is read here; the forward segment is
read by scripts/forward_read.py and its plan).

    python scripts/book_series.py fusion:A fusion:C F104.sub_A_sqrt@ls [--batch B01] [--tag s4] [--end 20251231] [--out runs/_batch_B01/book_series.json]

Per object and day:  ls = net return of the decile long/short book (gross 1, 15 bp per unit traded);
total = net return of the pure long book (top decile, equal weight, 15 bp);  bench = equal-weight return of the
names that have a signal and a label that day;  excess = total - bench.
"""
import glob
import json
import math
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.guard import MemoryGuard, limit_threads, slot  # noqa: E402

limit_threads(8)
import numpy as np  # noqa: E402

from partura import books as bk  # noqa: E402
from partura import diagnose as dg  # noqa: E402
from partura import ops_ext  # noqa: E402,F401
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.panels import SHARED_CACHE, PanelSet  # noqa: E402

argv = sys.argv[1:]


def opt(name, default=None):
    return argv[argv.index(name) + 1] if name in argv else default


BATCH, TAG, END = opt("--batch", "B01"), opt("--tag", "s4"), opt("--end", "20251231")
objs = [a for i, a in enumerate(argv) if not a.startswith("-") and (i == 0 or argv[i - 1] not in ("--batch", "--tag", "--end", "--out"))]
J = json.loads((PARTURA_ROOT / "runs" / f"_batch_{BATCH}" / f"fuse_{TAG}.json").read_text(encoding="utf-8"))
exprs, spec = {}, {}
for o in objs:
    if o.startswith("fusion:"):
        name = o.split(":")[1]
        keys = J["fusions"][name]["members"]
        for k in set(keys) | {"known_head"}:
            exprs[f"m:{k}"] = J["members"][k]["expr"]
        spec[o] = {"kind": "fusion", "name": name, "label": J["fusions"][name]["label"], "hl": float(J["fusions"][name]["methods"]["each"]["chosen_hl"])}
    else:
        cand, view = o.split("@")
        fid, cid = cand.split(".", 1)
        p = sorted(glob.glob(str(PARTURA_ROOT / "runs" / f"{fid}_*" / f"sweepfinal_{TAG}.json")))[0]
        r = json.loads(Path(p).read_text(encoding="utf-8"))["results"][cid]
        exprs[f"c:{o}"] = r["expr"]
        spec[o] = {"kind": "single", "expr": r["expr"], "sign": float(r["sign_user"]), "hl": float(r["books_user"]["by_rank"][view]["hl"]), "view": view}

with slot():
    mem = MemoryGuard(self_limit_gb=34, cgroup_limit_gb=70).start()
    t0 = time.time()
    ps = PanelSet("/root/autodl-tmp/qmt_daily_data/fast_factor_compute", "20180102", END, warmup=60, device="cuda", gpu_fraction=0,
                  cache_dir=str(SHARED_CACHE), mirror_root="/root/autodl-tmp/AlphaCube/mirror", workdir=str(PARTURA_ROOT / "tmp"),
                  label_kind="open_vwap15", label_buyable=True, batch=32)
    P = ps.compute(exprs)
    if ps.errors:
        raise SystemExit(f"did not evaluate: {dict(ps.errors)}")
    tgt = np.asarray(ps.target(1), dtype=np.float64)
    dates = [str(d) for d in ps.dates]
    from alphacube.metrics import long_short_weights, portfolio_returns
    Zs = {k[2:]: dg._zrank(bk.smoothed(float(J["members"][k[2:]]["sign"]) * np.asarray(P[k], np.float64), float(J["members"][k[2:]]["hl"]))).astype(np.float32)
          for k in exprs if k.startswith("m:")}
    G = J["groups"]

    def fuse(keys):
        z = np.stack([Zs[k] for k in keys]).astype(np.float64)
        fin = np.isfinite(z)
        with np.errstate(invalid="ignore", divide="ignore"):
            out = np.where(fin, z, 0.0).sum(0) / fin.sum(0)
        return np.where(fin.sum(0) >= math.ceil(len(keys) / 2), out, np.nan)

    def half(keys):
        a, b = fuse(keys), Zs["known_head"].astype(np.float64)
        return np.where(np.isfinite(a) & np.isfinite(b), 0.5 * a + 0.5 * b, np.nan)

    build = {"O": lambda: fuse(G["orig"]), "U": lambda: fuse(G["upg"]), "A": lambda: fuse(G["indep"]), "B": lambda: Zs["known_head"].astype(np.float64),
             "C": lambda: fuse(G["indep"] + ["known_head"]), "D": lambda: half(G["indep"])}
    r5 = lambda a: [None if x != x else round(float(x), 7) for x in a]      # noqa: E731
    out = {"end": dates[-1], "dates": dates, "objects": {}}
    for o, s in spec.items():
        sm = bk.smoothed(build[s["name"]](), s["hl"]) if s["kind"] == "fusion" else bk.smoothed(s["sign"] * np.asarray(P[f"c:{o}"], np.float64), s["hl"])
        w = long_short_weights(sm, bk.TOP_FRAC)
        ls_net, _, ls_turn = portfolio_returns(w, tgt, bk.COST)
        net, gross, turn = bk.long_book(w, sm, tgt)
        ok = np.isfinite(sm) & np.isfinite(tgt)
        cnt = ok.sum(1)
        ew = np.where(cnt > 0, np.where(ok, tgt, 0.0).sum(1) / np.maximum(cnt, 1), np.nan)
        held = (w > 0).sum(1)
        out["objects"][o] = {**s, "ls": r5(ls_net), "excess": r5(net), "bench": r5(ew), "total": r5(net + ew), "long_turnover": float(np.nanmean(turn)), "ls_turnover": float(np.nanmean(ls_turn)),
                             "names_held": float(np.mean(held[held > 0])), "universe": float(np.mean(cnt[cnt > 0]))}
        print(f"{o}: {len(dates)} days; long book holds {out['objects'][o]['names_held']:.0f} names of {out['objects'][o]['universe']:.0f}", flush=True)
    mem.stop()
p = PARTURA_ROOT / (opt("--out") or f"runs/_batch_{BATCH}/book_series_{TAG}.json")
p.write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")
print(f"wrote {p} ({time.time() - t0:.0f}s)")
