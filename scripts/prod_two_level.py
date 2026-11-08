"""PROD W01 re-tested with AlphaCube's two-level champion synthesis (research/prod_W01/TWO_LEVEL_PLAN.md).  New server, after
prod_final.py.  Source tmp/prod_env.sh first.

    python scripts/prod_two_level.py build
        pools WM (every M head of every seed, before dedup) and WP (every P head), as daily z-ranks of each head's raw panel
        -> AlphaCube's scorer (score_all_factors.py --buyable, split at the 1359th day = 2023-08-07) -> training fingerprints ->
        pick_families -> build (ridge inside a family, lstsq across, fitted on the first 1359 days) -> C_WM / C_WP.
        Nothing after 2023-08-07 selects or fits anything.  -> runs/prod_W01/two_level/{WM,WP}/, C_W{M,P}.npy (+ .families.json)
    python scripts/prod_two_level.py read [--again]
        the two existing champions (copied from the old host into runs/prod_W01/two_level/champions/) are checked against
        their recorded books first; then in-sample / test / forward / combined books of every signal and the paired daily
        differences the plan names.  Ledgered (research/prod_W01/ledger_prod.json).  -> research/prod_W01/two_level.{json,md}
    python scripts/prod_two_level.py overlay [--again]
        research/prod_W01/OVERLAY_PLAN.md: each champion and C_WP_ng as two "family factors" (daily z-scores, oriented on the
        training period), weighted by AlphaCube's between-family lstsq on the first 1359 days; paired with the champion
        itself.  Ledgered.  -> research/prod_W01/overlay.{json,md}

AlphaCube's scripts are used unmodified ($ALPHACUBE_ROOT/scripts).  The book convention is research/two_level's
(partura.books.books, scripts/two_level_forward.py).
"""
import csv
import hashlib
import json
import os
import subprocess
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
from partura import steer  # noqa: E402
from partura import study  # noqa: E402
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.panels import SHARED_CACHE, PanelSet  # noqa: E402
from partura.splits import Ledger  # noqa: E402

sys.path.insert(0, str(PARTURA_ROOT / "scripts"))
import c05_lib  # noqa: E402
import prod_hosts  # noqa: E402
import prod_lib  # noqa: E402

argv = sys.argv[1:]
MODE = argv[0] if argv else ""
if MODE not in ("build", "read", "overlay"):
    raise SystemExit(__doc__)
if study.name("") != "PROD" or not steer.rank_first():
    raise SystemExit("source tmp/prod_env.sh first (PARTURA_C0X=PROD, rank first)")
AC = Path(os.environ.get("ALPHACUBE_ROOT", "/root/autodl-tmp/AlphaCube"))
sys.path.insert(0, str(AC / "scripts"))
DIRNAME = study.dirname("PROD")
D, EP = PARTURA_ROOT / "research" / DIRNAME, PARTURA_ROOT / "episodes"
W = PARTURA_ROOT / "runs" / DIRNAME / "two_level"
LEDGER = D / "ledger_prod.json"
STORE = os.environ.get("PARTURA_STORE", "/root/autodl-tmp/qmt_daily_data/fast_factor_compute")
MIRROR = os.environ.get("PARTURA_MIRROR", "/root/autodl-tmp/AlphaCube/mirror")
MIRROR = MIRROR if MIRROR and os.path.isdir(MIRROR) else None
PY = os.environ.get("PY", sys.executable)
SPLIT = 1359                                   # the first 1359 days = 2018-01-02 .. 2023-08-07 (AlphaCube's training period)
FP_DAYS, FP_SYMBOLS = 250, 512                 # build_champion.py's training fingerprints
CHAMPS = ("手写库冠军", "挖掘冠军")
POOLS = ("WM", "WP")
VARIANTS = ("_ng", "")          # TWO_LEVEL_PLAN.md correction 3: _ng = no small-family gate (the main criterion); "" = AlphaCube as is
MAIN, LITERAL = ("C_WP_ng", "C_WM_ng"), ("C_WP", "C_WM")


def pick_families_no_gate(rows, fp, cluster, max_families, max_members):
    """build_champion.pick_families without the small-family quality gate (TWO_LEVEL_PLAN.md correction 3); everything else
    as there: clusters on the training fingerprints, members by training fitness, families by their best member's."""
    from select_factors import cluster_by_correlation, fitness, pairwise_abs_corr
    labels = cluster_by_correlation(pairwise_abs_corr(fp), cluster)
    fams = []
    for fam in np.unique(labels):
        idx = sorted(np.flatnonzero(labels == fam).tolist(), key=lambda j: -fitness(rows[j]))
        fams.append((idx[:max_members], fitness(rows[idx[0]])))
    fams.sort(key=lambda t: -t[1])
    print(f"{len(rows)} 个健康因子 -> {labels.max() + 1} 族,不设小族门槛,取前 {max_families}", flush=True)
    return [f[0] for f in fams[:max_families]]


def opt(name, default=None):
    return argv[argv.index(name) + 1] if name in argv else default


def view_and_label():
    from alphacube.label import Label, open_vwap15
    from alphacube.research import warmed_view
    from alphacube.store import open_cube_store
    end = str(open_cube_store(STORE).dates[-1])
    view, _ = warmed_view(open_cube_store(STORE), "20180102", end, warmup=60)
    dates = np.asarray([str(d) for d in view.dates])
    if str(dates[SPLIT - 1]) != "20230807" or str(dates[SPLIT]) != "20230808":
        raise SystemExit(f"unexpected calendar: day {SPLIT} is {dates[SPLIT - 1]}")
    tgt = Label("open_vwap15", 1, buyable=True).compute(view, price=open_vwap15(view)).astype(np.float64)
    return view, dates, end, tgt


def build():
    seeds = prod_hosts.seeds(prod_hosts.load(D / "hosts.json"))
    unfinished = [s for s in seeds if not (D / "arms" / f"s{s}.ALLDONE").is_file()]
    if unfinished:
        raise SystemExit(f"seeds {unfinished} are not finished")
    pool = {"WM": [], "WP": []}
    for S in seeds:
        r = prod_lib.seed_library(S, EP, D, c05_lib, pfx=study.prefix("PROD"))
        for X, name in (("M", "WM"), ("P", "WP")):
            pool[name] += [h["expr"] for h in r[X]]
    n_heads = {k: len(v) for k, v in pool.items()}
    pool = {k: list(dict.fromkeys(v)) for k, v in pool.items()}             # exact duplicates once, first seen first
    print(f"[tl] pools (heads before dedup -> distinct): WM {n_heads['WM']} -> {len(pool['WM'])}, WP {n_heads['WP']} -> {len(pool['WP'])}", flush=True)

    from alphacube.plugins import load_plugins
    load_plugins(["partura.ac_plugin"])
    t0 = time.time()
    view, dates, end, tgt = view_and_label()
    ps = PanelSet(STORE, "20180102", end, warmup=60, device="cuda", gpu_fraction=float(opt("--gpu-fraction", 0.4)), cache_dir=str(SHARED_CACHE),
                  mirror_root=MIRROR, workdir=str(PARTURA_ROOT / "tmp"), label_kind="open_vwap15", label_buyable=True, batch=8,
                  daily_root=os.environ.get("PARTURA_DAILY_ROOT") or None)
    if list(ps.dates) != list(dates):
        raise SystemExit("the panel view and AlphaCube's view differ")
    # every head's signal as AlphaCube's scorer wants it: one (D, S) float32 file per expression, shared by both pools
    store_dir = W / "_signals"
    store_dir.mkdir(parents=True, exist_ok=True)
    path = {e: store_dir / (hashlib.sha1(e.encode()).hexdigest()[:20] + ".npy") for e in pool["WP"] + pool["WM"]}
    todo = [e for e in dict.fromkeys(pool["WP"] + pool["WM"]) if not path[e].is_file()]
    bad = []
    for i in range(0, len(todo), 16):
        chunk = todo[i:i + 16]
        P = ps.compute({f"c{j}": e for j, e in enumerate(chunk)})
        for j, e in enumerate(chunk):
            if f"c{j}" not in P:
                bad.append(e)
                continue
            np.save(path[e], steer.signal_input(P[f"c{j}"]).astype(np.float32))
        print(f"[tl] signals {min(i + 16, len(todo))}/{len(todo)} ({time.time() - t0:.0f}s)", flush=True)
    summary = {"plan": f"research/{DIRNAME}/TWO_LEVEL_PLAN.md", "view": [str(dates[0]), end], "split_day": str(dates[SPLIT - 1]),
               "heads_before_dedup": n_heads, "distinct": {k: len(v) for k, v in pool.items()}, "not_computed": bad, "pools": {}}

    from build_champion import build as ac_build, healthy_rows, pick_families
    from select_factors import build_train_fingerprints
    fit_target = tgt.copy()
    fit_target[SPLIT:] = np.nan                     # build() fits on target[:SPLIT] only; nothing later is even passed in
    for name in POOLS:
        d = W / name
        (d / "panels").mkdir(parents=True, exist_ok=True)
        exprs = [e for e in pool[name] if e not in bad]
        with open(d / "manifest.csv", "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=["i", "run", "expression"])
            w.writeheader()
            for i, e in enumerate(exprs):
                dst = d / "panels" / f"{i:05d}.npy"
                if dst.exists():
                    dst.unlink()
                os.link(path[e], dst)
                w.writerow({"i": i, "run": "prod_W01", "expression": e})
        np.save(d / "dates.npy", dates)
        frac = (SPLIT + 0.5) / len(dates)              # int(D * frac) == SPLIT exactly
        if int(len(dates) * frac) != SPLIT:
            raise SystemExit("train-frac does not land on the split")
        if not (d / "metrics.csv").is_file() or "--rescore" in argv:
            cmd = [PY, "-u", str(AC / "scripts" / "score_all_factors.py"), str(d), "--store", STORE, "--start", "20180102", "--end", end,
                   "--buyable", "--train-frac", repr(frac), "--workers", opt("--workers", "8"), "--no-rows"]
            print(f"[tl] {name}: scoring {len(exprs)} signals with AlphaCube's scorer", flush=True)
            r = subprocess.run(cmd, cwd=str(AC))
            if r.returncode:
                raise SystemExit(f"scorer failed on {name} ({r.returncode})")
        rows = healthy_rows(d)
        S_ = tgt.shape[1]
        cols = np.linspace(0, S_ - 1, num=min(FP_SYMBOLS, S_)).astype(int)
        fp = np.asarray(build_train_fingerprints(d / "panels", [int(r_["i"]) for r_ in rows], slice(SPLIT - FP_DAYS, SPLIT), cols,
                                                 d / f"fp_train_{FP_DAYS}x{FP_SYMBOLS}.npy"))
        for v in VARIANTS:
            fams = pick_families_no_gate(rows, fp, 0.7, 100, 60) if v == "_ng" else pick_families(rows, fp, 0.7, 100, 60)
            t1 = time.time()
            sig = ac_build(d, rows, fams, fit_target, slice(0, SPLIT))
            np.save(W / f"C_{name}{v}.npy", sig.astype(np.float32))
            fam_rows = [{"members": [int(rows[j]["i"]) for j in idx], "expressions": [rows[j]["expression"] for j in idx],
                         "fitness_best": float(abs(float(rows[idx[0]]["rank_ic_train"])) - 0.14 * float(rows[idx[0]]["turnover_train"]))} for idx in fams]
            (W / f"C_{name}{v}.families.json").write_text(json.dumps(fam_rows, ensure_ascii=False, indent=1), encoding="utf-8")
            summary["pools"][name + v] = {"signals": len(exprs), "healthy": len(rows), "families": len(fams), "members": sum(len(f) for f in fams),
                                          "largest_family": max((len(f) for f in fams), default=0), "seconds_build": time.time() - t1}
            print(f"[tl] C_{name}{v}: {len(exprs)} signals, {len(rows)} healthy, {len(fams)} families, {summary['pools'][name + v]['members']} members "
                  f"({time.time() - t1:.0f}s)", flush=True)
    (W / "build.json").write_text(json.dumps(summary, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"[tl] built ({time.time() - t0:.0f}s) -> {W}", flush=True)


def read():
    out_json, out_md = D / "two_level.json", D / "two_level.md"
    if out_json.is_file() and "--again" not in argv:
        raise SystemExit(f"{out_json} exists: the two-level read has been done; --again to read once more (ledgered again)")
    from alphacube.metrics import long_short_weights, portfolio_returns
    view, dates, end, tgt = view_and_label()
    ix = lambda d: int(np.searchsorted(dates, d))             # noqa: E731
    us, ho, fw, oos = slice(0, SPLIT), slice(SPLIT, ix("20260101")), slice(ix("20260101"), len(dates)), slice(SPLIT, len(dates))
    SEG = {"insample": us, "test": ho, "forward": fw, "oos": oos}
    ref = json.loads((W / "champions" / "two_level_forward_20260916.json").read_text(encoding="utf-8"))

    def oriented(sig):
        ic = dg.ic_row(sig[us], tgt[us], target_ranks=dg.rank_rows(tgt[us]))
        return (1.0 if not np.isfinite(ic["rank_ic"]) or ic["rank_ic"] >= 0 else -1.0) * sig

    def daily(sig, hl_lo, hl_ls):
        sm_lo, sm_ls = bk.smoothed(sig, hl_lo), bk.smoothed(sig, hl_ls)
        return {"excess": bk.long_book(long_short_weights(sm_lo, bk.TOP_FRAC), sm_lo, tgt)[0],
                "ls": portfolio_returns(long_short_weights(sm_ls, bk.TOP_FRAC), tgt, bk.COST)[0]}

    def stats(x):
        f = x[np.isfinite(x)]
        if f.size < 20 or not f.std() > 0:
            return {"ann": float("nan"), "ir": float("nan"), "t": float("nan"), "n": int(f.size)}
        return {"ann": float(f.mean() * 252), "ir": float(f.mean() / f.std() * np.sqrt(252)), "t": float(f.mean() / f.std() * np.sqrt(f.size)), "n": int(f.size)}

    res = {"plan": f"research/{DIRNAME}/TWO_LEVEL_PLAN.md", "view": [str(dates[0]), end], "segments": {k: [str(dates[v.start]), str(dates[v.stop - 1])] for k, v in SEG.items()},
           "build": json.loads((W / "build.json").read_text(encoding="utf-8")), "check": {}, "signals": {}, "paired": {}, "fixed_hl": {}}
    SIG = {f"C_{n}{v}": oriented(np.load(W / f"C_{n}{v}.npy").astype(np.float64)) for v in VARIANTS for n in POOLS}
    with slot():
        mem = MemoryGuard(self_limit_gb=int(os.environ.get("PARTURA_SELF_LIMIT_GB", 60)), cgroup_limit_gb=int(os.environ.get("PARTURA_CGROUP_LIMIT_GB", 80))).start()
        # ---- the champions: are they, on this host's label, the signals research/two_level read?  (their numbers are known already)
        for c in CHAMPS:
            f = W / "champions" / f"signal_{c}_20260916.npy"
            s = np.load(f).astype(np.float64)
            if s.shape != tgt.shape:
                res["check"][c] = {"pass": False, "why": f"shape {s.shape} != {tgt.shape}"}
                continue
            s = oriented(s)
            b = bk.books(s, tgt, us, {"test": ho, "forward": fw})["by_rank"]["long"]
            rec = ref["signals"][c]
            got = {k: float(b["splits"][k]["long_ann"]) for k in ("test", "forward")}
            want = {k: float(rec["long"][k]["long_ann"]) for k in ("test", "forward")}
            ok = bool(b["hl"] == rec["hl_long"] and all(abs(got[k] - want[k]) <= 0.005 for k in got))
            res["check"][c] = {"pass": ok, "hl": [b["hl"], rec["hl_long"]], "long_ann": {k: [got[k], want[k]] for k in got}}
            print(f"[tl] check {c}: hl {b['hl']} vs {rec['hl_long']}; test {got['test']:+.1%} vs {want['test']:+.1%}; "
                  f"forward {got['forward']:+.1%} vs {want['forward']:+.1%} -> {'PASS' if ok else 'FAIL'}", flush=True)
            if ok:
                SIG[c] = s
        Ledger(LEDGER).record("holdout", 4, f"PROD {DIRNAME} two-level C_WM / C_WP, with and without the small-family gate (TWO_LEVEL_PLAN.md): test 20230808..20251231, description + the plan's paired rule", "prod_two_level")
        Ledger(LEDGER).record("forward", 4, f"PROD {DIRNAME} two-level C_WM / C_WP (_ng and as is): forward 20260101..{end}", "prod_two_level")
        KEEP = ("long_ann", "long_sharpe", "long_mdd", "long_turnover", "ls_ann", "ls_sharpe", "ls_mdd")
        DAILY = {}
        for name, sig in SIG.items():
            b = bk.books(sig, tgt, us, SEG)
            L, S_ = b["by_rank"]["long"], b["by_rank"]["ls"]
            res["signals"][name] = {"hl_long": L["hl"], "hl_ls": S_["hl"],
                                    "long": {k: {m: float(v[m]) for m in KEEP if m.startswith("long")} for k, v in L["splits"].items()},
                                    "ls": {k: {m: float(v[m]) for m in KEEP if m.startswith("ls")} for k, v in S_["splits"].items()}}
            DAILY[name] = daily(sig, L["hl"], S_["hl"])
            x = res["signals"][name]["long"]
            print(f"[tl] {name:6s} 纯多头 净超额 / 夏普(hl {L['hl']:g}): 样本内 {x['insample']['long_ann']:+.1%} / {x['insample']['long_sharpe']:.2f} | "
                  f"测试 {x['test']['long_ann']:+.1%} / {x['test']['long_sharpe']:.2f} | 前推 {x['forward']['long_ann']:+.1%} / {x['forward']['long_sharpe']:.2f} | "
                  f"合并 {x['oos']['long_ann']:+.1%} / {x['oos']['long_sharpe']:.2f}", flush=True)
        pairs = [MAIN, LITERAL] + [(a, c) for a in MAIN + LITERAL for c in CHAMPS]
        for a, c in pairs:
            if a in DAILY and c in DAILY:
                res["paired"][f"{a}-{c}"] = {k: {s: stats((DAILY[a][k] - DAILY[c][k])[sl]) for s, sl in SEG.items() if s != "insample"} for k in ("excess", "ls")}
        for hl in (5, 10, 20):                                                        # the plan's robustness line: one common half-life
            da, dm = daily(SIG[MAIN[0]], hl, hl), daily(SIG[MAIN[1]], hl, hl)
            res["fixed_hl"][str(hl)] = {s: stats((da["excess"] - dm["excess"])[sl]) for s, sl in SEG.items() if s != "insample"}
        mem.stop()
    def verdict(pair):
        q_ = res["paired"]["-".join(pair)]["excess"]
        t_, f_ = q_["oos"]["t"], q_["forward"]["ann"]
        return "成立" if t_ >= 2 else "方向一致、证据不够" if f_ > 0 and t_ >= 1 else "没有延续" if f_ < 0 else "证据弱"
    q = res["paired"]["-".join(MAIN)]["excess"]
    t_oos, fw_ann = q["oos"]["t"], q["forward"]["ann"]
    res["verdict"], res["verdict_literal"] = verdict(MAIN), verdict(LITERAL)
    out_json.write_text(json.dumps(res, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
    out_md.write_text(report(res), encoding="utf-8")
    print(f"[tl] {MAIN[0]} − {MAIN[1]}: test {q['test']['ann']:+.1%} (t {q['test']['t']:+.1f}) | forward {fw_ann:+.1%} (t {q['forward']['t']:+.1f}) | "
          f"combined {q['oos']['ann']:+.1%} (t {t_oos:+.1f}) -> {res['verdict']}", flush=True)
    print(f"[tl] wrote {out_json}, {out_md}", flush=True)

def overlay():
    out_json, out_md = D / "overlay.json", D / "overlay.md"
    if out_json.is_file() and "--again" not in argv:
        raise SystemExit(f"{out_json} exists: the overlay read has been done; --again to read once more (ledgered again)")
    from alphacube.metrics import long_short_weights, portfolio_returns, zscore_rows
    from combine_two_level import blend, fit_weights
    view, dates, end, tgt = view_and_label()
    ix = lambda d: int(np.searchsorted(dates, d))             # noqa: E731
    us, ho, fw, oos = slice(0, SPLIT), slice(SPLIT, ix("20260101")), slice(ix("20260101"), len(dates)), slice(SPLIT, len(dates))
    SEG = {"insample": us, "test": ho, "forward": fw, "oos": oos}
    fit_target = tgt.copy()
    fit_target[SPLIT:] = np.nan

    def oriented(sig):
        ic = dg.ic_row(sig[us], tgt[us], target_ranks=dg.rank_rows(tgt[us]))
        return (1.0 if not np.isfinite(ic["rank_ic"]) or ic["rank_ic"] >= 0 else -1.0) * sig

    def daily(sig, hl_lo, hl_ls):
        sm_lo, sm_ls = bk.smoothed(sig, hl_lo), bk.smoothed(sig, hl_ls)
        return {"excess": bk.long_book(long_short_weights(sm_lo, bk.TOP_FRAC), sm_lo, tgt)[0],
                "ls": portfolio_returns(long_short_weights(sm_ls, bk.TOP_FRAC), tgt, bk.COST)[0]}

    def stats(x):
        f = x[np.isfinite(x)]
        if f.size < 20 or not f.std() > 0:
            return {"ann": float("nan"), "ir": float("nan"), "t": float("nan"), "n": int(f.size)}
        return {"ann": float(f.mean() * 252), "ir": float(f.mean() / f.std() * np.sqrt(252)), "t": float(f.mean() / f.std() * np.sqrt(f.size)), "n": int(f.size)}

    def rankcorr(a, b, sl, step=5):
        cs = []
        for d in range(sl.start, sl.stop, step):
            m = np.isfinite(a[d]) & np.isfinite(b[d])
            if m.sum() > 100:
                cs.append(np.corrcoef(np.argsort(np.argsort(a[d, m])), np.argsort(np.argsort(b[d, m])))[0, 1])
        return float(np.mean(cs))

    zw = zscore_rows(oriented(np.load(W / "C_WP_ng.npy").astype(np.float64)))
    res = {"plan": f"research/{DIRNAME}/OVERLAY_PLAN.md", "view": [str(dates[0]), end], "segments": {k: [str(dates[v.start]), str(dates[v.stop - 1])] for k, v in SEG.items()},
           "insample": {}, "signals": {}, "paired": {}, "own_hl": {}, "fixed_ratio": {}}
    SIG, OWN_HL = {"W": zw}, {"手写库冠军": 20.0, "挖掘冠军": 10.0}
    with slot():
        mem = MemoryGuard(self_limit_gb=int(os.environ.get("PARTURA_SELF_LIMIT_GB", 60)), cgroup_limit_gb=int(os.environ.get("PARTURA_CGROUP_LIMIT_GB", 80))).start()
        for c, tag in (("手写库冠军", "O_H"), ("挖掘冠军", "O_X")):
            zc = zscore_rows(oriented(np.load(W / "champions" / f"signal_{c}_20260916.npy").astype(np.float64)))
            if zc.shape != zw.shape:
                raise SystemExit(f"{c}: shape {zc.shape} != {zw.shape}")
            w = fit_weights([zc, zw], fit_target, us, "lstsq")                  # the between-family layer, training period only
            SIG[c], SIG[tag] = zc, blend([zc, zw], w)
            res["insample"][tag] = {"weights": [float(w[0]), float(w[1])], "w_ratio": float(w[1] / w[0]) if w[0] else float("nan"),
                                    "rank_corr_W_champion": rankcorr(zw, zc, us)}
            for r in (0.25, 0.5, 1.0):
                SIG[f"{tag}@{r:g}"] = blend([zc, zw], np.array([1.0, r]))
            print(f"[ov] {tag}: weights {c} {w[0]:.4g}, W {w[1]:.4g} (W / champion {res['insample'][tag]['w_ratio']:.3f}); "
                  f"in-sample daily rank corr W vs {c} {res['insample'][tag]['rank_corr_W_champion']:.3f}", flush=True)
        Ledger(LEDGER).record("holdout", 2, f"PROD {DIRNAME} overlay O_H / O_X = champion + C_WP_ng (OVERLAY_PLAN.md): test 20230808..20251231", "prod_two_level overlay")
        Ledger(LEDGER).record("forward", 2, f"PROD {DIRNAME} overlay O_H / O_X: forward 20260101..{end}", "prod_two_level overlay")
        KEEP = ("long_ann", "long_sharpe", "long_mdd", "long_turnover", "ls_ann", "ls_sharpe", "ls_mdd")
        DAILY = {}
        for name in ("手写库冠军", "O_H", "挖掘冠军", "O_X", "W"):
            b = bk.books(SIG[name], tgt, us, SEG)
            L, S_ = b["by_rank"]["long"], b["by_rank"]["ls"]
            res["signals"][name] = {"hl_long": L["hl"], "hl_ls": S_["hl"],
                                    "long": {k: {m: float(v[m]) for m in KEEP if m.startswith("long")} for k, v in L["splits"].items()},
                                    "ls": {k: {m: float(v[m]) for m in KEEP if m.startswith("ls")} for k, v in S_["splits"].items()}}
            DAILY[name] = daily(SIG[name], L["hl"], S_["hl"])
            x = res["signals"][name]["long"]
            print(f"[ov] {name:6s} 纯多头 净超额 / 夏普(hl {L['hl']:g}): 样本内 {x['insample']['long_ann']:+.1%} / {x['insample']['long_sharpe']:.2f} | "
                  f"测试 {x['test']['long_ann']:+.1%} / {x['test']['long_sharpe']:.2f} | 前推 {x['forward']['long_ann']:+.1%} / {x['forward']['long_sharpe']:.2f} | "
                  f"合并 {x['oos']['long_ann']:+.1%} / {x['oos']['long_sharpe']:.2f}", flush=True)
        for tag, c in (("O_H", "手写库冠军"), ("O_X", "挖掘冠军")):
            res["paired"][f"{tag}-{c}"] = {k: {s: stats((DAILY[tag][k] - DAILY[c][k])[sl]) for s, sl in SEG.items() if s != "insample"} for k in ("excess", "ls")}
            hl = OWN_HL[c]                                                           # robustness: the champion's own half-life for both
            do, dc = daily(SIG[tag], hl, hl), daily(SIG[c], hl, hl)
            res["own_hl"][f"{tag}-{c}"] = {"hl": hl, **{s: stats((do["excess"] - dc["excess"])[sl]) for s, sl in SEG.items() if s != "insample"}}
            for r in (0.25, 0.5, 1.0):
                dr = daily(SIG[f"{tag}@{r:g}"], hl, hl)
                res["fixed_ratio"][f"{tag}@{r:g}-{c}"] = {"hl": hl, **{s: stats((dr["excess"] - dc["excess"])[sl]) for s, sl in SEG.items() if s != "insample"}}
        mem.stop()

    def verdict(key):
        q_ = res["paired"][key]["excess"]
        t_, f_ = q_["oos"]["t"], q_["forward"]["ann"]
        return "成立" if t_ >= 2 else "方向一致、证据不够" if f_ > 0 and t_ >= 1 else "没有延续" if f_ < 0 else "证据弱"
    res["verdict"] = {k: verdict(k) for k in res["paired"]}
    out_json.write_text(json.dumps(res, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
    out_md.write_text(overlay_report(res), encoding="utf-8")
    for k, v in res["paired"].items():
        q = v["excess"]
        print(f"[ov] {k}: test {q['test']['ann']:+.1%} (t {q['test']['t']:+.1f}) | forward {q['forward']['ann']:+.1%} (t {q['forward']['t']:+.1f}) | "
              f"combined {q['oos']['ann']:+.1%} (t {q['oos']['t']:+.1f}) -> {res['verdict'][k]}", flush=True)
    print(f"[ov] wrote {out_json}, {out_md}", flush=True)


def overlay_report(res):
    p = lambda x: "—" if x is None or x != x else f"{x:+.1%}"            # noqa: E731
    f2 = lambda x: "—" if x is None or x != x else f"{x:.2f}"             # noqa: E731
    t1 = lambda q: f"{p(q['ann'])}(t {q['t']:+.1f})"                      # noqa: E731
    L = [f"# PROD W01:W01 的两层合成信号叠加到现成冠军上(规则见 `{res['plan']}`)", "",
         f"W = C_WP_ng;O_H = 手写库冠军 ⊕ W,O_X = 挖掘冠军 ⊕ W(逐日 z 分数,族间 lstsq 权重只在 {res['segments']['insample'][0]} ~ {res['segments']['insample'][1]} 拟合)。", "",
         "## 样本内的事实(描述)", "", "| 叠加 | 冠军权重 | W 权重 | W / 冠军 | W 与冠军逐日秩相关(样本内) |", "|---|---|---|---|---|"]
    for k, x in res["insample"].items():
        L.append(f"| {k} | {x['weights'][0]:.4g} | {x['weights'][1]:.4g} | {x['w_ratio']:.3f} | {x['rank_corr_W_champion']:.3f} |")
    L += ["", "## 各信号(纯多头 = 净超额 / 超额夏普)", "", "| 信号 | hl | 样本内 | 测试段 | 前推段 | 合并段 | 合并段超额回撤 | 多空夏普 合并段 |", "|---|---|---|---|---|---|---|---|"]
    for n, x in res["signals"].items():
        lo = x["long"]
        L.append(f"| {n} | {x['hl_long']:g} | {p(lo['insample']['long_ann'])} / {f2(lo['insample']['long_sharpe'])} | {p(lo['test']['long_ann'])} / {f2(lo['test']['long_sharpe'])} | "
                 f"{p(lo['forward']['long_ann'])} / {f2(lo['forward']['long_sharpe'])} | {p(lo['oos']['long_ann'])} / {f2(lo['oos']['long_sharpe'])} | {p(lo['oos']['long_mdd'])} | {f2(x['ls']['oos']['ls_sharpe'])} |")
    L += ["", "## 主判据:叠加 − 冠军(纯多头逐日净超额,同一天相减)", "", "| 比较 | 测试段 | 前推段 | 合并段 | 多空 合并段 | 按规则 |", "|---|---|---|---|---|---|"]
    for k, v in res["paired"].items():
        L.append(f"| **{k}** | {t1(v['excess']['test'])} | {t1(v['excess']['forward'])} | {t1(v['excess']['oos'])} | {t1(v['ls']['oos'])} | {res['verdict'][k]} |")
    L += ["", "稳健性(描述):两边都用冠军自己的半衰期;以及固定权重比 W : 冠军。", "", "| 比较 | hl | 测试段 | 前推段 | 合并段 |", "|---|---|---|---|---|"]
    for k, v in list(res["own_hl"].items()) + list(res["fixed_ratio"].items()):
        L.append(f"| {k} | {v['hl']:g} | {t1(v['test'])} | {t1(v['forward'])} | {t1(v['oos'])} |")
    return "\n".join(L) + "\n"


def report(res):
    p = lambda x: "—" if x is None or x != x else f"{x:+.1%}"            # noqa: E731
    f2 = lambda x: "—" if x is None or x != x else f"{x:.2f}"             # noqa: E731
    b = res["build"]
    L = [f"# PROD W01:两层合成重测(规则见 `{res['plan']}`)", "",
         f"视窗 {res['view'][0]} ~ {res['view'][1]};训练段切在 {b['split_day']}(选族、权重、方向、半衰期都只用它)。"
         f"测试段 {res['segments']['test'][0]} ~ {res['segments']['test'][1]},前推段 {res['segments']['forward'][0]} ~ {res['segments']['forward'][1]}。", "",
         "| 信号 | head(去重前) | 不同表达式 | 健康 | 族 | 入选成员 | 最大族 |", "|---|---|---|---|---|---|---|"]
    for v in VARIANTS:
        for n in POOLS:
            x = b["pools"].get(n + v, {})
            L.append(f"| C_{n}{v}{'(无小族门槛)' if v else '(原样)'} | {b['heads_before_dedup'][n]} | {b['distinct'][n]} | {x.get('healthy')} | {x.get('families')} | {x.get('members')} | {x.get('largest_family')} |")
    if b["not_computed"]:
        L.append(f"\n在全视窗上算不出来、没进池子的表达式:{len(b['not_computed'])} 个。")
    L += ["", "## 冠军核对(过了才和冠军比)", "", "| 冠军 | 半衰期 本机 / 记录 | 测试段 本机 / 记录 | 前推段 本机 / 记录 | 结果 |", "|---|---|---|---|---|"]
    for c, x in res["check"].items():
        if "long_ann" in x:
            L.append(f"| {c} | {x['hl'][0]:g} / {x['hl'][1]:g} | {p(x['long_ann']['test'][0])} / {p(x['long_ann']['test'][1])} | "
                     f"{p(x['long_ann']['forward'][0])} / {p(x['long_ann']['forward'][1])} | {'过' if x['pass'] else '不过'} |")
        else:
            L.append(f"| {c} | — | — | — | 不过({x['why']}) |")
    L += ["", "## 各信号(纯多头 = 净超额 / 超额夏普;多空 = 净夏普)", "",
          "| 信号 | hl | 样本内(拟合值) | 测试段 | 前推段 | 合并段 | 合并段超额回撤 | 多空 测试 / 前推 / 合并 |", "|---|---|---|---|---|---|---|---|"]
    for n, x in res["signals"].items():
        lo, ls = x["long"], x["ls"]
        L.append(f"| {n} | {x['hl_long']:g} | {p(lo['insample']['long_ann'])} / {f2(lo['insample']['long_sharpe'])} | {p(lo['test']['long_ann'])} / {f2(lo['test']['long_sharpe'])} | "
                 f"{p(lo['forward']['long_ann'])} / {f2(lo['forward']['long_sharpe'])} | {p(lo['oos']['long_ann'])} / {f2(lo['oos']['long_sharpe'])} | {p(lo['oos']['long_mdd'])} | "
                 f"{f2(ls['test']['ls_sharpe'])} / {f2(ls['forward']['ls_sharpe'])} / {f2(ls['oos']['ls_sharpe'])} |")
    L += ["", "## 成对差(同一天相减;纯多头看逐日净超额)", "", "| 比较 | 测试段 | 前推段 | 合并段 | 多空 合并段 |", "|---|---|---|---|---|"]
    for k, v in res["paired"].items():
        e, s = v["excess"], v["ls"]
        L.append(f"| {'**' + k + '**(主判据)' if k == '-'.join(MAIN) else k + '(原样,对照)' if k == '-'.join(LITERAL) else k} | {p(e['test']['ann'])}(t {e['test']['t']:+.1f}) | {p(e['forward']['ann'])}(t {e['forward']['t']:+.1f}) | "
                 f"{p(e['oos']['ann'])}(t {e['oos']['t']:+.1f}) | {p(s['oos']['ann'])}(t {s['oos']['t']:+.1f}) |")
    L += ["", f"固定同一个半衰期时的 {MAIN[0]} − {MAIN[1]}(描述):", "", "| hl | 测试段 | 前推段 | 合并段 |", "|---|---|---|---|"]
    for hl, v in res["fixed_hl"].items():
        L.append(f"| {hl} | {p(v['test']['ann'])}(t {v['test']['t']:+.1f}) | {p(v['forward']['ann'])}(t {v['forward']['t']:+.1f}) | {p(v['oos']['ann'])}(t {v['oos']['t']:+.1f}) |")
    L += ["", f"**按事先的规则(主判据 {MAIN[0]} − {MAIN[1]}):{res['verdict']}。** 原样版本({LITERAL[0]} − {LITERAL[1]}):{res['verdict_literal']}。"]
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    {"build": build, "read": read, "overlay": overlay}[MODE]()
