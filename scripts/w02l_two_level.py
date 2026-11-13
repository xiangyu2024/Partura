"""PROD W02L: the library and the one 2026 read of PLAN section 7, done as research/prod_W02L/LIBRARY_PLAN.md says (written before
any of this ran).  Server; `source tmp/w02l_env.sh` first.

    python scripts/w02l_two_level.py signals [--pool LX|W] [--shard k/n] [--device cuda|cpu] [--cached-only] [--reverse]
        pools LX (struct/members.csv, the 5583 parseable members of the two libraries) and W (library/heads_D.json, every D-head,
        from scripts/w02l_report.py --heads-json); each expression's daily z-rank signal (steer.signal_input) on the whole view
        2018-01-02 ~ 2026-09-16 -> runs/prod_W02L/two_level/_signals/<sha1>.npy, plus a copy cut at 2025-12-31 for the scorer.
    python scripts/w02l_two_level.py score [--workers N] [--pools W,LX,LX2] [--allow-missing]
        AlphaCube's scorer, unmodified (score_all_factors.py --buyable), on the view cut at 2025-12-31 (its label never sees 2026):
        score_LX/ and score_W/ -> metrics.csv.  Then the cut copies are deleted.
    python scripts/w02l_two_level.py build [--pools LX,LXW,W] [--variants as_is,_ng] [--allow-missing]
        W deduplicated (by D, best first; |rho| >= 0.7 on the training fingerprints drops the later one) -> library/W_dedup.json;
        pools LX, LXW = LX + W, W with the full-length signals and the scorer's rows; AlphaCube's pick_families (as is = main,
        and without the small-family gate = description) and build (ridge inside a family, lstsq across) fitted on the label up
        to 2025-12-31 (computed on the cut view) -> C_<pool>{,_ng}.npy.  Nothing after 2025-12-31 enters any fit or choice.
    python scripts/w02l_two_level.py read [--dry]
        (--dry: a code check on the view cut at 2025-12-31, no ledger, nothing of 2026)
        THE ONE READ OF 2026 (ledgered in research/prod_W02L/ledger_prod.json; refuses to run twice): the books of every signal,
        the paired daily differences of PLAN section 7, the overlay on the two champions; -> research/prod_W02L/two_level.{json,md}.
"""
import csv
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.guard import MemoryGuard, limit_threads, slot  # noqa: E402

limit_threads(int(os.environ.get("PARTURA_THREADS", 8)))
import numpy as np  # noqa: E402

from partura import books as bk  # noqa: E402
from partura import diagnose as dg  # noqa: E402
from partura import ops_ext  # noqa: E402,F401
from partura import steer  # noqa: E402
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.panels import SHARED_CACHE, PanelSet  # noqa: E402
from partura.splits import Ledger  # noqa: E402

argv = sys.argv[1:]
MODE = argv[0] if argv else ""
if MODE not in ("signals", "score", "build", "read"):
    raise SystemExit(__doc__)
assert os.environ.get("PARTURA_RANK_FIRST") == "1" and os.environ.get("PARTURA_STUDY_DIR") == "prod_W02L", "source tmp/w02l_env.sh first"
AC = Path(os.environ.get("ALPHACUBE_ROOT", "/root/autodl-tmp/AlphaCube"))
sys.path.insert(0, str(AC / "scripts"))
D = PARTURA_ROOT / "research" / "prod_W02L"
W = PARTURA_ROOT / "runs" / "prod_W02L" / "two_level"
LIB = D / "library"
LEDGER = D / "ledger_prod.json"
STORE = os.environ.get("PARTURA_STORE", "/root/autodl-tmp/qmt_daily_data/fast_factor_compute")
MIRROR = os.environ.get("PARTURA_MIRROR")
MIRROR = MIRROR if MIRROR and os.path.isdir(MIRROR) else None
PY = os.environ.get("PY", sys.executable)
START, END, LAST, VALID = "20180102", "20260916", "20251231", "20230808"   # the view (= stage 0's); fits end at LAST
FP_DAYS, FP_SYMBOLS = 250, 512
CHAMPS = ("手写库冠军", "挖掘冠军")
CHAMP_DIR = PARTURA_ROOT / "runs" / "prod_W01" / "two_level" / "champions"


def opt(name, default=None):
    return argv[argv.index(name) + 1] if name in argv else default


def key(e):
    return hashlib.sha1(e.encode()).hexdigest()[:20]


def pools():
    lx = list(dict.fromkeys(r["expression"] for r in csv.DictReader(open(D / "struct" / "members.csv", encoding="utf-8"))))
    heads = json.loads((LIB / "heads_D.json").read_text(encoding="utf-8"))
    w = [h["expr"] for h in heads]
    return lx, list(dict.fromkeys(w)), heads


def full_view():
    from alphacube.research import warmed_view
    from alphacube.store import open_cube_store
    view, _ = warmed_view(open_cube_store(STORE), START, END, warmup=60)
    dates = np.asarray([str(d) for d in view.dates])
    split = int(np.searchsorted(dates, LAST, side="right"))           # days [0, split) = 2018-01-02 .. 2025-12-31
    assert dates[split - 1] <= LAST < dates[split], "calendar"
    return view, dates, split


def cut_view_dates():
    from alphacube.research import warmed_view
    from alphacube.store import open_cube_store
    view, _ = warmed_view(open_cube_store(STORE), START, LAST, warmup=60)
    return view, np.asarray([str(d) for d in view.dates])


# ---------------------------------------------------------------------------------------------------------------- signals
def signals():
    lx, w, _ = pools()
    _, dates, split = full_view()
    _, cut_dates = cut_view_dates()
    if list(cut_dates) != list(dates[:split]):
        raise SystemExit("the cut view is not the first part of the full view")
    from alphacube.plugins import load_plugins
    load_plugins(["partura.ac_plugin"])
    dev = opt("--device", "cuda")
    ps = PanelSet(STORE, START, END, warmup=60, device=dev, gpu_fraction=0.4 if dev.startswith("cuda") else None, cache_dir=str(SHARED_CACHE),
                  mirror_root=MIRROR, workdir=str(PARTURA_ROOT / "tmp"), label_kind="open_vwap15", label_buyable=True, batch=8,
                  daily_root=os.environ.get("PARTURA_DAILY_ROOT") or None)
    if list(ps.dates) != list(dates):
        raise SystemExit("the panel view and AlphaCube's view differ")
    sd, cd = W / "_signals", W / "_cut"
    sd.mkdir(parents=True, exist_ok=True)
    cd.mkdir(parents=True, exist_ok=True)
    allx = list(dict.fromkeys(w + lx))                                   # W first: the few that are not cached yet
    if opt("--pool"):                                                    # --pool LX | W: only that pool (LX comes from the cache)
        allx = list(dict.fromkeys({"LX": lx, "W": w}[opt("--pool")]))
    k_, n_ = (int(x) for x in opt("--shard", "0/1").split("/"))         # --shard k/n: this process takes every n-th, from k
    todo = [e for i, e in enumerate(allx) if i % n_ == k_ and (not (sd / f"{key(e)}.npy").is_file() or not (cd / f"{key(e)}.npy").is_file())]
    if "--cached-only" in argv:                                          # only what the shared cache already holds (a helper beside
        from partura.panels import parse_research                       # shards that are busy evaluating uncached trees on the CPU)
        def cached(e):
            try:
                p = ps._cache_path(parse_research(e, n_minutes=ps.store.n_minutes).key())
            except Exception:                                            # noqa: BLE001
                return False
            return p is not None and p.is_file()
        todo = [e for e in todo if cached(e)]
    if "--reverse" in argv:                                              # from the other end, to meet the shards rather than race them
        todo = todo[::-1]
    bad, t0 = {}, time.time()
    with slot():
        mem = MemoryGuard(self_limit_gb=float(os.environ.get("PARTURA_SELF_LIMIT_GB", 150)),
                          cgroup_limit_gb=float(os.environ.get("PARTURA_CGROUP_LIMIT_GB", 850))).start()
        for i in range(0, len(todo), 8):
            chunk = todo[i:i + 8]
            P = ps.compute({f"c{j}": e for j, e in enumerate(chunk)})
            for j, e in enumerate(chunk):
                if f"c{j}" not in P:
                    bad[e] = ps.errors.get(f"c{j}", "missing")
                    continue
                s = steer.signal_input(P[f"c{j}"]).astype(np.float32)
                for dst, arr in ((sd / f"{key(e)}.npy", s), (cd / f"{key(e)}.npy", np.ascontiguousarray(s[:split]))):
                    tmp = dst.with_name(f".{dst.stem}.{os.getpid()}.tmp.npy")   # atomic: two processes may write the same file
                    np.save(tmp, arr)
                    os.replace(tmp, dst)
            ps._mem.clear()
            if (i // 8) % 25 == 0 or i + 8 >= len(todo):
                print(f"[w2] signals {min(i + 8, len(todo))}/{len(todo)} ({time.time() - t0:.0f}s, {len(bad)} failed)", flush=True)
        mem.stop()
    (W / f"signals_{opt('--pool', 'all')}_{k_}of{n_}.json").write_text(json.dumps({"lx": len(lx), "w": len(w), "failed": bad}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"[w2] signals done (shard {k_}/{n_}): failed {len(bad)}", flush=True)


def failed_signals(allow_missing=False):
    """Every shard's failures; and every expression of both pools must have its signal or be listed as failed.  With
    allow_missing (score --allow-missing), the missing ones are returned as {expr: "no signal yet"} instead."""
    bad = {}
    for f in W.glob("signals_*_*of*.json"):
        bad.update(json.loads(f.read_text(encoding="utf-8"))["failed"])
    lx, w, _ = pools()
    missing = [e for e in dict.fromkeys(w + lx) if e not in bad and not (W / "_signals" / f"{key(e)}.npy").is_file()]
    if missing and not allow_missing:
        raise SystemExit(f"{len(missing)} expressions have no signal yet (run every shard of `signals` first)")
    return {**bad, **{e: "no signal yet" for e in missing}}


# ---------------------------------------------------------------------------------------------------------------- score
def write_pool(d, exprs, src, dates):
    """d/panels/<i>.npy (hard links to src/<sha1>.npy), manifest.csv, dates.npy.  A rewritten pool drops its fingerprint cache:
    AlphaCube's build_train_fingerprints loads fp_*.npy whenever it exists (11-13: the W pools kept the dry run's 208 / 68 rows)."""
    (d / "panels").mkdir(parents=True, exist_ok=True)
    for f in d.glob("fp_*.npy"):
        f.unlink()
    with open(d / "manifest.csv", "w", newline="", encoding="utf-8") as fh:
        wr = csv.DictWriter(fh, fieldnames=["i", "run", "expression"])
        wr.writeheader()
        for i, e in enumerate(exprs):
            dst = d / "panels" / f"{i:05d}.npy"
            if dst.exists():
                dst.unlink()
            os.link(src / f"{key(e)}.npy", dst)
            wr.writerow({"i": i, "run": "prod_W02L", "expression": e})
    np.save(d / "dates.npy", dates)


def score():
    lx, w, _ = pools()
    _, cut_dates = cut_view_dates()
    failed = failed_signals(allow_missing="--allow-missing" in argv)
    n = len(cut_dates)
    # the scorer's "test" columns: the last 20 days of 2025 (its health check wants coverage there, and the last two days have no
    # label on the cut view); selection reads training columns only, so train = 2018-01-02 .. the 21st-last day of 2025
    frac = (n - 20 + 0.5) / n                                            # int(n * frac) = n - 20
    scored_lx = set()
    if (W / "score_LX" / "manifest.csv").is_file():
        scored_lx = {r["expression"] for r in csv.DictReader(open(W / "score_LX" / "manifest.csv", encoding="utf-8"))}
    lx2 = [e for e in lx if e not in scored_lx] if scored_lx else []    # LX members whose signals came after score_LX ran
    for name, exprs in (("W", w), ("LX", lx), ("LX2", lx2)):
        d = W / f"score_{name}"
        ex = [e for e in exprs if e not in failed]
        if not ex:
            continue
        if name not in opt("--pools", "W,LX,LX2").split(","):
            continue
        if name == "LX" and scored_lx and "--rescore" not in argv:
            print(f"[w2] score_LX: done earlier ({len(scored_lx)} signals); the rest go to score_LX2", flush=True)
            continue
        if (d / "metrics.csv").is_file() and "--rescore" not in argv:
            have = [r["expression"] for r in csv.DictReader(open(d / "manifest.csv", encoding="utf-8"))]
            if have == ex:
                print(f"[w2] score_{name}: metrics.csv exists for these {len(ex)} signals", flush=True)
                continue
            print(f"[w2] score_{name}: the pool changed ({len(have)} -> {len(ex)}), scoring again", flush=True)
        write_pool(d, ex, W / "_cut", cut_dates)
        cmd = [PY, "-u", str(AC / "scripts" / "score_all_factors.py"), str(d), "--store", STORE, "--start", START, "--end", LAST,
               "--buyable", "--train-frac", repr(frac), "--workers", opt("--workers", "16"), "--no-rows"]
        print(f"[w2] score_{name}: {len(ex)} signals, AlphaCube's scorer on {cut_dates[0]}..{cut_dates[-1]}", flush=True)
        r = subprocess.run(cmd, cwd=str(AC))
        if r.returncode:
            raise SystemExit(f"scorer failed on {name} ({r.returncode})")
        shutil.rmtree(d / "panels")                                      # the cut copies are not needed any more
    if "--keep-cut" not in argv:
        shutil.rmtree(W / "_cut", ignore_errors=True)
    print("[w2] scored", flush=True)


# ---------------------------------------------------------------------------------------------------------------- build
def fit_target(split):
    """The label (open_vwap15, buyable) on the cut view, padded with NaN to the full view: no 2026 price enters any fit."""
    from alphacube.label import Label, open_vwap15
    view, cut_dates = cut_view_dates()
    t = Label("open_vwap15", 1, buyable=True).compute(view, price=open_vwap15(view)).astype(np.float64)
    assert t.shape[0] == split
    return t


def build():
    from build_champion import build as ac_build, pick_families
    from select_factors import build_train_fingerprints, cluster_by_correlation, fitness, pairwise_abs_corr, selectable_rows
    lx, w, heads = pools()
    _, dates, split = full_view()
    failed = failed_signals(allow_missing="--allow-missing" in argv)   # still missing at build time = not computed, listed in build.json
    tgt_cut = fit_target(split)
    S_ = tgt_cut.shape[1]
    fit = np.full((len(dates), S_), np.nan)
    fit[:split] = tgt_cut
    cols = np.linspace(0, S_ - 1, num=min(FP_SYMBOLS, S_)).astype(int)
    fp_days = slice(split - FP_DAYS, split)

    def rows_of(name, exprs):
        by_expr = {}
        for nm in ((name, name + "2") if name == "LX" else (name,)):
            f = W / f"score_{nm}" / "metrics.csv"
            if f.is_file():
                by_expr.update({r["expression"]: r for r in csv.DictReader(open(f, encoding="utf-8"))})
        return [by_expr[e] for e in exprs if e in by_expr]

    # W deduplicated: by D, best first; a head whose |rho| to a kept one is >= 0.7 on the training fingerprints is dropped
    wd = W / "W_all"
    wx = [e for e in w if e not in failed]
    if not ("--reuse-pool" in argv and (wd / "manifest.csv").is_file()):
        write_pool(wd, wx, W / "_signals", dates)
    fpw = np.asarray(build_train_fingerprints(wd / "panels", list(range(len(wx))), fp_days, cols, wd / f"fp_{FP_DAYS}x{FP_SYMBOLS}.npy"))
    C = pairwise_abs_corr(fpw)
    Dsc = {h["expr"]: h["D"] for h in heads}
    order = sorted(range(len(wx)), key=lambda i: -Dsc[wx[i]])
    kept, dropped = [], {}
    for i in order:
        hit = next((k for k in kept if C[i, k] >= 0.7), None)
        if hit is None:
            kept.append(i)
        else:
            dropped[wx[i]] = {"kept": wx[hit], "rho": float(C[i, hit])}
    wk = [wx[i] for i in sorted(kept, key=lambda i: -Dsc[wx[i]])]
    LIB.mkdir(parents=True, exist_ok=True)
    (LIB / "W_dedup.json").write_text(json.dumps({"kept": [{"expr": e, "D": Dsc[e]} for e in wk], "dropped": dropped},
                                                 ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"[w2] W: {len(w)} D-heads, {sum(e in failed for e in w)} failed, {len(wk)} kept after |rho| >= 0.7 dedup", flush=True)

    summary = {"plan": "research/prod_W02L/LIBRARY_PLAN.md", "view": [str(dates[0]), str(dates[-1])], "fit_until": str(dates[split - 1]),
               "W_heads": len(w), "W_kept": len(wk), "failed": failed, "pools": {}}
    lx_rows_all = rows_of("LX", [e for e in lx if e not in failed])
    w_rows_all = rows_of("W", wk)
    only = opt("--pools", "LX,LXW,W").split(",")                         # --pools W: a dry run of one pool (fits only, no 2026)
    for name, exprs, rows_src in (("LX", [r["expression"] for r in lx_rows_all], lx_rows_all),
                                  ("LXW", [r["expression"] for r in lx_rows_all] + [r["expression"] for r in w_rows_all], lx_rows_all + w_rows_all),
                                  ("W", [r["expression"] for r in w_rows_all], w_rows_all)):
        if name not in only:
            continue
        d = W / name
        if "--reuse-pool" in argv and (d / "metrics.csv").is_file():   # a second variant beside a running build: the pool is written
            have = [r["expression"] for r in csv.DictReader(open(d / "manifest.csv", encoding="utf-8"))]
            if have != exprs:
                raise SystemExit(f"{name}: the pool on disk is not this pool")
        else:
            write_pool(d, exprs, W / "_signals", dates)
            with open(d / "metrics.csv", "w", newline="", encoding="utf-8") as fh:  # the scorer's rows, renumbered for this pool
                wr = csv.DictWriter(fh, fieldnames=list(rows_src[0].keys()))
                wr.writeheader()
                for i, r in enumerate(rows_src):
                    wr.writerow({**r, "i": i})
        rows = selectable_rows(d / "metrics.csv")
        fp = np.asarray(build_train_fingerprints(d / "panels", [int(r["i"]) for r in rows], fp_days, cols, d / f"fp_{FP_DAYS}x{FP_SYMBOLS}.npy"))
        for v in opt("--variants", "as_is,_ng").replace("as_is", "").split(","):  # --variants as_is | _ng: one per process
            if v == "":
                fams = pick_families(rows, fp, 0.7, 100, 60)                     # AlphaCube as is: the main criterion
            else:
                labels = cluster_by_correlation(pairwise_abs_corr(fp), 0.7)
                fl = []
                for f in np.unique(labels):
                    idx = sorted(np.flatnonzero(labels == f).tolist(), key=lambda j: -fitness(rows[j]))
                    fl.append((idx[:60], fitness(rows[idx[0]])))
                fams = [f[0] for f in sorted(fl, key=lambda t: -t[1])[:100]]
            t1 = time.time()
            sig = ac_build(d, rows, fams, fit, slice(0, split))
            np.save(W / f"C_{name}{v}.npy", sig.astype(np.float32))
            fam_rows = [{"expressions": [rows[j]["expression"] for j in idx], "fitness_best": float(fitness(rows[idx[0]]))} for idx in fams]
            (W / f"C_{name}{v}.families.json").write_text(json.dumps(fam_rows, ensure_ascii=False, indent=1), encoding="utf-8")
            n_w = sum(1 for f in fam_rows for e in f["expressions"] if e in set(wk)) if name == "LXW" else None
            summary["pools"][name + v] = {"signals": len(exprs), "healthy": len(rows), "families": len(fams), "members": sum(len(f) for f in fams),
                                          "W_members": n_w, "seconds": round(time.time() - t1)}
            print(f"[w2] C_{name}{v}: {len(exprs)} signals, {len(rows)} healthy, {len(fams)} families, "
                  f"{summary['pools'][name + v]['members']} members{'' if n_w is None else f', {n_w} from W'} ({time.time() - t1:.0f}s)", flush=True)
    tag = "_".join(only) + ("" if opt("--variants") is None else "_" + opt("--variants").replace(",", "+"))
    (W / f"build_{tag}.json").write_text(json.dumps(summary, ensure_ascii=False, indent=1), encoding="utf-8")
    merged = {}                                                          # build.json = every partial build, latest wins per pool
    for f in sorted(W.glob("build_*.json"), key=lambda p: p.stat().st_mtime):
        x = json.loads(f.read_text(encoding="utf-8"))
        merged = {**merged, **{k: v for k, v in x.items() if k != "pools"}, "pools": {**merged.get("pools", {}), **x["pools"]}}
    (W / "build.json").write_text(json.dumps(merged, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"[w2] built -> {W}", flush=True)


# ---------------------------------------------------------------------------------------------------------------- read
def read():
    """--dry: a code check of this function that cannot touch 2026 -- the view cut at 2025-12-31, 2023-08-08 ~ 2025-12-31 standing
    in for the test segment (the C_* fits cover it, so its numbers mean nothing), no ledger entry, no started mark, output in
    tmp/w2tl/read_dry.{json,md}."""
    dry = "--dry" in argv
    if dry:
        out_json, out_md = PARTURA_ROOT / "tmp" / "w2tl" / "read_dry.json", PARTURA_ROOT / "tmp" / "w2tl" / "read_dry.md"
    else:
        out_json, out_md = D / "two_level.json", D / "two_level.md"
        if out_json.is_file() or (D / "two_level.started").is_file():
            raise SystemExit("the 2026 read has been done (or started) already: PLAN section 7 allows one read")
        (D / "two_level.started").write_text(time.strftime("%Y-%m-%d %H:%M:%S"), encoding="utf-8")
    from alphacube.label import Label, open_vwap15
    from alphacube.metrics import long_short_weights, portfolio_returns, zscore_rows
    from combine_two_level import blend, fit_weights
    if dry:
        _, dates, split = full_view()                                # the full view's calendar only; the label from the cut view
        dates = dates[:split]
        tgt = fit_target(split)
    else:
        view, dates, split = full_view()
        tgt = Label("open_vwap15", 1, buyable=True).compute(view, price=open_vwap15(view)).astype(np.float64)
    n_days = len(dates)
    ix = lambda d_: int(np.searchsorted(dates, d_))                 # noqa: E731
    if dry:
        fit_end = ix(VALID)
        us, va, te = slice(0, fit_end), slice(ix("20220101"), fit_end), slice(fit_end, n_days)
    else:
        fit_end = split
        us, va, te = slice(0, split), slice(ix(VALID), split), slice(split, n_days)
    fit = tgt.copy()
    fit[fit_end:] = np.nan
    SEG = {"insample": us, "valid": va, "test": te}

    def orient(sig, seg):
        ic = dg.ic_row(sig[seg], tgt[seg], target_ranks=dg.rank_rows(tgt[seg]))
        return (1.0 if not np.isfinite(ic["rank_ic"]) or ic["rank_ic"] >= 0 else -1.0) * sig

    def oriented(sig):
        return orient(sig, us)

    def daily(sig, hl_lo, hl_ls):
        sm_lo, sm_ls = bk.smoothed(sig, hl_lo), bk.smoothed(sig, hl_ls)
        return {"excess": bk.long_book(long_short_weights(sm_lo, bk.TOP_FRAC), sm_lo, tgt)[0],
                "ls": portfolio_returns(long_short_weights(sm_ls, bk.TOP_FRAC), tgt, bk.COST)[0]}

    def stats(x):
        f = x[np.isfinite(x)]
        if f.size < 20 or not f.std() > 0:
            return {"ann": float("nan"), "ir": float("nan"), "t": float("nan"), "n": int(f.size)}
        return {"ann": float(f.mean() * 252), "ir": float(f.mean() / f.std() * np.sqrt(252)), "t": float(f.mean() / f.std() * np.sqrt(f.size)), "n": int(f.size)}

    res = {"plan": "research/prod_W02L/PLAN.md §7 + LIBRARY_PLAN.md", "dry": dry,
           "segments": {k: [str(dates[v.start]), str(dates[v.stop - 1])] for k, v in SEG.items()},
           "build": json.loads((W / "build.json").read_text(encoding="utf-8")), "check": {}, "signals": {}, "paired": {}, "overlay": {}}
    def load_c(n):                                                  # --dry before every C_* is built: stand in C_LX (a code check only)
        f = W / f"{n}.npy"
        if dry and not f.is_file():
            res.setdefault("dry_stand_ins", []).append(n)
            f = W / "C_LX.npy"
        return oriented(np.load(f)[:n_days].astype(np.float64))
    SIG = {n: load_c(n) for n in ("C_LX", "C_LXW", "C_W", "C_LX_ng", "C_LXW_ng", "C_W_ng")}
    with slot():
        mem = MemoryGuard(self_limit_gb=float(os.environ.get("PARTURA_SELF_LIMIT_GB", 150)),
                          cgroup_limit_gb=float(os.environ.get("PARTURA_CGROUP_LIMIT_GB", 850))).start()
        if not dry:
            Ledger(LEDGER).record("test", len(SIG) + 4, "PROD W02L PLAN §7: C(LX ∪ W) − C(LX) two-level (as is = main, _ng = description), "
                                  f"C_W alone, overlay of C_W on the two champions; test {dates[split]}..{dates[-1]}, read once", "w02l_two_level read")
        # the champions (LIBRARY_PLAN §5, as W01): on this host's label, do they reproduce the books research/two_level recorded
        # (in-sample to 2023-08-07; test 2023-08-08 ~ 2025-12-31, forward 2026 -- numbers known before W02L)?  Only then are they used.
        ref = json.loads((CHAMP_DIR / "two_level_forward_20260916.json").read_text(encoding="utf-8"))
        us_old = slice(0, ix(VALID))
        seg_old = {"test": slice(ix(VALID), split)} if dry else {"test": slice(ix(VALID), split), "forward": slice(split, n_days)}
        for c in CHAMPS:
            s = np.load(CHAMP_DIR / f"signal_{c}_20260916.npy")[:n_days].astype(np.float64)
            if s.shape != tgt.shape:
                res["check"][c] = {"pass": False, "why": f"shape {s.shape} != {tgt.shape}"}
                continue
            b = bk.books(orient(s, us_old), tgt, us_old, seg_old)["by_rank"]["long"]
            rec = ref["signals"][c]
            got = {k: float(b["splits"][k]["long_ann"]) for k in seg_old}
            want = {k: float(rec["long"][k]["long_ann"]) for k in seg_old}
            ok = bool(b["hl"] == rec["hl_long"] and all(abs(got[k] - want[k]) <= 0.005 for k in got))
            res["check"][c] = {"pass": ok, "hl": [b["hl"], rec["hl_long"]], "long_ann": {k: [got[k], want[k]] for k in got}}
            print(f"[w2] check {c}: hl {b['hl']} vs {rec['hl_long']}; " + "; ".join(f"{k} {got[k]:+.2%} vs {want[k]:+.2%}" for k in got)
                  + f" -> {'PASS' if ok else 'FAIL'}", flush=True)
            if ok:
                SIG[c] = oriented(s)
        KEEP = ("long_ann", "long_sharpe", "long_mdd", "long_turnover", "ls_ann", "ls_sharpe", "ls_mdd")
        DAILY = {}
        zw = zscore_rows(SIG["C_W"])
        for c, tag in (("手写库冠军", "O_H"), ("挖掘冠军", "O_X")):
            if c not in SIG:
                continue
            zc = zscore_rows(SIG[c])
            wts = fit_weights([zc, zw], fit, us, "lstsq")                # the between-family layer, fitted on the in-sample segment
            SIG[tag] = blend([zc, zw], wts)
            res["overlay"][tag] = {"weights": [float(wts[0]), float(wts[1])]}
        for name, sig in SIG.items():
            b = bk.books(sig, tgt, us, SEG)
            L, S_ = b["by_rank"]["long"], b["by_rank"]["ls"]
            res["signals"][name] = {"hl_long": L["hl"], "hl_ls": S_["hl"],
                                    "long": {k: {m: float(v[m]) for m in KEEP if m.startswith("long")} for k, v in L["splits"].items()},
                                    "ls": {k: {m: float(v[m]) for m in KEEP if m.startswith("ls")} for k, v in S_["splits"].items()}}
            DAILY[name] = daily(sig, L["hl"], S_["hl"])
            x = res["signals"][name]["long"]
            print(f"[w2] {name:9s} 纯多头净超额 / 夏普(hl {L['hl']:g}): 样本内 {x['insample']['long_ann']:+.1%} / {x['insample']['long_sharpe']:.2f} | "
                  f"valid {x['valid']['long_ann']:+.1%} / {x['valid']['long_sharpe']:.2f} | test {x['test']['long_ann']:+.1%} / {x['test']['long_sharpe']:.2f}", flush=True)
        pairs = [("C_LXW", "C_LX"), ("C_LXW_ng", "C_LX_ng")] + [(t, c) for t, c in (("O_H", "手写库冠军"), ("O_X", "挖掘冠军")) if t in DAILY]
        for a, c in pairs:
            res["paired"][f"{a}-{c}"] = {k: {s: stats((DAILY[a][k] - DAILY[c][k])[sl]) for s, sl in SEG.items() if s != "insample"} for k in ("excess", "ls")}
        mem.stop()

    def verdict(k):                                                 # PLAN section 7's table, on the test segment
        q = res["paired"][k]["excess"]["test"]
        return "Partura 让这 5 千多条变好了" if q["t"] >= 2 else "方向一致、证据不够" if q["ann"] > 0 and q["t"] >= 1 else "没有增益" if q["ann"] < 0 else "证据弱"
    res["verdict"] = {k: verdict(k) for k in res["paired"]}
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(res, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
    out_md.write_text(report(res), encoding="utf-8")
    for k, v in res["paired"].items():
        q = v["excess"]
        print(f"[w2] {k}: test {q['test']['ann']:+.2%} (t {q['test']['t']:+.2f}) | valid {q['valid']['ann']:+.2%} (t {q['valid']['t']:+.2f}) -> {res['verdict'][k]}", flush=True)


def report(res):
    seg = res["segments"]
    out = [("# 演练(--dry):只查代码，数字没有意义(测试段被拟合覆盖)\n" if res.get("dry") else "") + "# W02L 建库与 2026 判读(PLAN §7,只读一次)\n",
           f"样本内 {seg['insample'][0]} ~ {seg['insample'][1]}(定方向、半衰期、所有拟合);valid {seg['valid'][0]} ~ {seg['valid'][1]}(只描述);"
           f"**test {seg['test'][0]} ~ {seg['test'][1]}**。\n",
           f"W02L 库:D-head {res['build']['W_heads']} 个，去重后 {res['build']['W_kept']} 个。\n",
           "## 主判据:test 段纯多头逐日净超额的成对差\n", "| 比较 | test 年化差 | t | 判读 | valid 年化差(只描述) | 多空 test 年化差(描述) |", "|---|---|---|---|---|---|"]
    for k, v in res["paired"].items():
        q, l_ = v["excess"], v["ls"]
        out.append(f"| {k} | {q['test']['ann']:+.2%} | {q['test']['t']:+.2f} | {res['verdict'][k]} | {q['valid']['ann']:+.2%} | {l_['test']['ann']:+.2%} |")
    out += ["\n主判据是第一行(`C_LXW − C_LX`,AlphaCube 原样);`_ng` 一行与叠加两行只作描述。\n",
            "## 各信号的书(纯多头净超额 / 夏普)\n", "| 信号 | hl | 样本内 | valid | test |", "|---|---|---|---|---|"]
    for n, s in res["signals"].items():
        x = s["long"]
        out.append(f"| {n} | {s['hl_long']:g} | {x['insample']['long_ann']:+.1%} / {x['insample']['long_sharpe']:.2f} | "
                   f"{x['valid']['long_ann']:+.1%} / {x['valid']['long_sharpe']:.2f} | {x['test']['long_ann']:+.1%} / {x['test']['long_sharpe']:.2f} |")
    out.append("\n## 冠军核对(本机标签上复现 research/two_level 记录的书;不过就不做叠加)\n")
    for c, x in res["check"].items():
        la = "; ".join(f"{k} {v[0]:+.2%} vs 记录 {v[1]:+.2%}" for k, v in (x.get("long_ann") or {}).items())
        out.append(f"- {c}:{'通过' if x.get('pass') else '没通过'}" + (f"(hl {x['hl'][0]:g} vs {x['hl'][1]:g};{la})" if "hl" in x else f"({x.get('why')})"))
    out.append("\n## 建库\n")
    for k, v in res["build"]["pools"].items():
        wm = "" if v.get("W_members") is None else f",其中 W02L {v['W_members']} 个"
        out.append(f"- C_{k}:{v['signals']} 条信号,健康 {v['healthy']},{v['families']} 族 {v['members']} 个成员{wm}")
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    {"signals": signals, "score": score, "build": build, "read": read}[MODE]()
