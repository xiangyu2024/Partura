"""PROD W02L: the W02L heads + the two champion signals, synthesised by AlphaCube as is (research/prod_W02L/COMBO_PLAN.md,
written before any of this ran).  Server; `source tmp/w02l_env.sh` first.

    python scripts/w02l_combo.py prep
        the two champion signals (runs/prod_W01/two_level/champions) as daily z-ranks -> runs/prod_W02L/two_level/_champ/<sha1>.npy
        (full view) and a copy cut at 2025-12-31; AlphaCube's scorer on the cut copies (same arguments as the W pool) -> score_K/
    python scripts/w02l_combo.py build
        pools WK = the 244 D-heads + the two champions, K = the two champions; pick_families(0.7, 100, 60) (as is) and without the
        small-family gate (_ng, WK only); ridge inside a family, lstsq across, fitted to 2025-12-31 -> C_WK, C_WK_ng, C_K; the same
        families with both layers fitted to 2023-08-07 -> C_WK_nested, C_K_nested.  Nothing after 2025-12-31 enters a fit.
    python scripts/w02l_combo.py describe
        books on the view cut at 2025-12-31 only (nothing of 2026) -> research/prod_W02L/combo.{json,md}
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

limit_threads(int(os.environ.get("PARTURA_THREADS", 16)))
import numpy as np  # noqa: E402

from partura import books as bk  # noqa: E402
from partura import diagnose as dg  # noqa: E402
from partura.bridge import PARTURA_ROOT  # noqa: E402

argv = sys.argv[1:]
MODE = argv[0] if argv else ""
if MODE not in ("prep", "build", "describe"):
    raise SystemExit(__doc__)
assert os.environ.get("PARTURA_RANK_FIRST") == "1" and os.environ.get("PARTURA_STUDY_DIR") == "prod_W02L", "source tmp/w02l_env.sh first"
AC = Path(os.environ.get("ALPHACUBE_ROOT", "/root/autodl-tmp/AlphaCube"))
sys.path.insert(0, str(AC / "scripts"))
D = PARTURA_ROOT / "research" / "prod_W02L"
W = PARTURA_ROOT / "runs" / "prod_W02L" / "two_level"
CH = W / "_champ"
STORE = os.environ.get("PARTURA_STORE", "/root/autodl-tmp/qmt_daily_data/fast_factor_compute")
PY = os.environ.get("PY", sys.executable)
START, END, LAST, VALID = "20180102", "20260916", "20251231", "20230808"
FP_DAYS, FP_SYMBOLS = 250, 512
CHAMP_DIR = PARTURA_ROOT / "runs" / "prod_W01" / "two_level" / "champions"
CHAMPS = ("手写库冠军", "挖掘冠军")
KEXPR = {c: f"CHAMPION:{c}" for c in CHAMPS}                         # the champions' names in the pools' manifests


def key(e):
    return hashlib.sha1(e.encode()).hexdigest()[:20]


def view_dates(end):
    from alphacube.research import warmed_view
    from alphacube.store import open_cube_store
    view, _ = warmed_view(open_cube_store(STORE), START, end, warmup=60)
    return view, np.asarray([str(d) for d in view.dates])


def label(view):
    from alphacube.label import Label, open_vwap15
    return Label("open_vwap15", 1, buyable=True).compute(view, price=open_vwap15(view)).astype(np.float64)


def src_of(e):
    """where an expression's full-length z-rank signal lives"""
    return (CH if e.startswith("CHAMPION:") else W / "_signals") / f"{key(e)}.npy"


def write_pool(d, exprs, dates, cut=False):
    """d/panels/<i>.npy (hard links), manifest.csv, dates.npy; drops a stale fingerprint cache (see w02l_two_level.write_pool)."""
    if d.exists():
        shutil.rmtree(d)
    (d / "panels").mkdir(parents=True)
    with open(d / "manifest.csv", "w", newline="", encoding="utf-8") as fh:
        wr = csv.DictWriter(fh, fieldnames=["i", "run", "expression"])
        wr.writeheader()
        for i, e in enumerate(exprs):
            s = src_of(e) if not cut else CH / "cut" / f"{key(e)}.npy"
            os.link(s, d / "panels" / f"{i:05d}.npy")
            wr.writerow({"i": i, "run": "prod_W02L", "expression": e})
    np.save(d / "dates.npy", dates)


# ---------------------------------------------------------------------------------------------------------------- prep
def prep():
    _, dates = view_dates(END)
    _, cut_dates = view_dates(LAST)
    split = len(cut_dates)
    assert list(cut_dates) == list(dates[:split]), "the cut view is not the first part of the full view"
    (CH / "cut").mkdir(parents=True, exist_ok=True)
    for c in CHAMPS:
        raw = np.load(CHAMP_DIR / f"signal_{c}_20260916.npy").astype(np.float64)
        assert raw.shape[0] == len(dates), (c, raw.shape, len(dates))
        z = dg._zrank(raw).astype(np.float32)
        np.save(CH / f"{key(KEXPR[c])}.npy", z)
        np.save(CH / "cut" / f"{key(KEXPR[c])}.npy", np.ascontiguousarray(z[:split]))
        print(f"[combo] {c}: z-rank {z.shape}", flush=True)
    d = W / "score_K"
    write_pool(d, [KEXPR[c] for c in CHAMPS], cut_dates, cut=True)
    frac = (split - 20 + 0.5) / split                                    # = w02l_two_level.score: train = all but the last 20 days
    cmd = [PY, "-u", str(AC / "scripts" / "score_all_factors.py"), str(d), "--store", STORE, "--start", START, "--end", LAST,
           "--buyable", "--train-frac", repr(frac), "--workers", "2", "--no-rows"]
    r = subprocess.run(cmd, cwd=str(AC))
    if r.returncode:
        raise SystemExit(f"scorer failed ({r.returncode})")
    shutil.rmtree(d / "panels")
    for r_ in csv.DictReader(open(d / "metrics.csv", encoding="utf-8")):
        print(f"[combo] scored {r_['expression']}: rank_ic_train {float(r_['rank_ic_train']):+.4f}, turnover_train "
              f"{float(r_['turnover_train']):.3f}, healthy {r_['healthy']}", flush=True)


# ---------------------------------------------------------------------------------------------------------------- build
def build():
    from build_champion import build as ac_build, pick_families
    from select_factors import build_train_fingerprints, cluster_by_correlation, fitness, pairwise_abs_corr, selectable_rows
    _, dates = view_dates(END)
    cut_view, cut_dates = view_dates(LAST)
    split = len(cut_dates)
    tgt_cut = label(cut_view)
    fit = np.full((len(dates), tgt_cut.shape[1]), np.nan)
    fit[:split] = tgt_cut
    n_tr = int(np.searchsorted(dates, VALID))                            # [0, n_tr) = 2018-01-02 .. 2023-08-07
    cols = np.linspace(0, fit.shape[1] - 1, num=min(FP_SYMBOLS, fit.shape[1])).astype(int)
    fp_days = slice(split - FP_DAYS, split)

    heads = [h["expr"] for h in json.loads((D / "library" / "heads_D.json").read_text(encoding="utf-8"))]
    by = {r["expression"]: r for r in csv.DictReader(open(W / "score_W" / "metrics.csv", encoding="utf-8"))}
    by.update({r["expression"]: r for r in csv.DictReader(open(W / "score_K" / "metrics.csv", encoding="utf-8"))})
    missing = [e for e in heads if e not in by or not src_of(e).is_file()]
    if missing:
        raise SystemExit(f"{len(missing)} D-heads have no score row or signal: {missing[:3]}")
    summary = {"plan": "research/prod_W02L/COMBO_PLAN.md", "fit_until": str(dates[split - 1]), "nested_until": str(dates[n_tr - 1]),
               "heads": len(heads), "pools": {}}
    for name, exprs in (("WK", heads + [KEXPR[c] for c in CHAMPS]), ("K", [KEXPR[c] for c in CHAMPS])):
        d = W / f"pool_{name}"
        write_pool(d, exprs, dates)
        src = [by[e] for e in exprs]
        with open(d / "metrics.csv", "w", newline="", encoding="utf-8") as fh:
            wr = csv.DictWriter(fh, fieldnames=list(src[0].keys()))
            wr.writeheader()
            for i, r in enumerate(src):
                wr.writerow({**r, "i": i})
        rows = selectable_rows(d / "metrics.csv")
        fp = np.asarray(build_train_fingerprints(d / "panels", [int(r["i"]) for r in rows], fp_days, cols, d / f"fp_{FP_DAYS}x{FP_SYMBOLS}.npy"))
        for v in (("", "_ng") if name == "WK" else ("",)):
            if v == "":
                fams = pick_families(rows, fp, 0.7, 100, 60)
            else:
                labels = cluster_by_correlation(pairwise_abs_corr(fp), 0.7)
                fl = []
                for f in np.unique(labels):
                    idx = sorted(np.flatnonzero(labels == f).tolist(), key=lambda j: -fitness(rows[j]))
                    fl.append((idx[:60], fitness(rows[idx[0]])))
                fams = [f[0] for f in sorted(fl, key=lambda t: -t[1])[:100]]
            fam_rows = [{"expressions": [rows[j]["expression"] for j in idx], "fitness_best": float(fitness(rows[idx[0]]))} for idx in fams]
            n_champ_fams = sum(any(e.startswith("CHAMPION:") for e in f["expressions"]) for f in fam_rows)
            for tag, tr in (("", slice(0, split)), ("_nested", slice(0, n_tr))):
                if v == "_ng" and tag:
                    continue
                t1 = time.time()
                sig = ac_build(d, rows, fams, fit, tr)
                np.save(W / f"C_{name}{v}{tag}.npy", sig.astype(np.float32))
                print(f"[combo] C_{name}{v}{tag}: {len(rows)} healthy of {len(exprs)}, {len(fams)} families "
                      f"({n_champ_fams} with a champion), {sum(len(f) for f in fams)} members ({time.time() - t1:.0f}s)", flush=True)
            (W / f"C_{name}{v}.families.json").write_text(json.dumps(fam_rows, ensure_ascii=False, indent=1), encoding="utf-8")
            summary["pools"][name + v] = {"signals": len(exprs), "healthy": len(rows), "families": len(fams),
                                          "members": sum(len(f) for f in fams), "champion_families": n_champ_fams,
                                          "champion_members": sorted({e for f in fam_rows for e in f["expressions"] if e.startswith("CHAMPION:")})}
    (W / "combo_build.json").write_text(json.dumps(summary, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"[combo] built: {json.dumps(summary['pools'], ensure_ascii=False)}", flush=True)


# ---------------------------------------------------------------------------------------------------------------- describe
def describe():
    from alphacube.metrics import long_short_weights, portfolio_returns, rank_rows, zscore_rows
    cut_view, cut_dates = view_dates(LAST)
    tgt = label(cut_view)
    n = len(cut_dates)
    n_tr = int(np.searchsorted(cut_dates, VALID))
    tr, va = slice(0, n_tr), slice(n_tr, n)

    def stats(x):
        f = x[np.isfinite(x)]
        if f.size < 20 or not f.std() > 0:
            return {"ann": float("nan"), "t": float("nan"), "n": int(f.size)}
        return {"ann": float(f.mean() * 252), "t": float(f.mean() / f.std() * np.sqrt(f.size)), "n": int(f.size)}

    def load(nm):
        if nm in CHAMPS:
            return np.load(CHAMP_DIR / f"signal_{nm}_20260916.npy", mmap_mode="r")[:n].astype(np.float64)
        return np.load(W / f"{nm}.npy", mmap_mode="r")[:n].astype(np.float64)

    def books_of(names):
        res, daily = {}, {}
        for nm in names:
            sig = load(nm)
            ic = dg.ic_row(sig[tr], tgt[tr], target_ranks=dg.rank_rows(tgt[tr]))
            sig = (-1.0 if np.isfinite(ic["rank_ic"]) and ic["rank_ic"] < 0 else 1.0) * sig
            b = bk.books(sig, tgt, tr, {"train": tr, "valid": va})
            L, S_ = b["by_rank"]["long"], b["by_rank"]["ls"]
            res[nm] = {"hl_long": L["hl"], "hl_ls": S_["hl"],
                       "long": {k: {m: float(v[m]) for m in ("long_ann", "long_sharpe", "long_mdd", "long_turnover")} for k, v in L["splits"].items()},
                       "ls": {k: {m: float(v[m]) for m in ("ls_ann", "ls_sharpe")} for k, v in S_["splits"].items()}}
            sm_lo, sm_ls = bk.smoothed(sig, L["hl"]), bk.smoothed(sig, S_["hl"])
            daily[nm] = {"excess": bk.long_book(long_short_weights(sm_lo, bk.TOP_FRAC), sm_lo, tgt)[0],
                         "ls": portfolio_returns(long_short_weights(sm_ls, bk.TOP_FRAC), tgt, bk.COST)[0]}
            print(f"[combo] {nm}: hl {L['hl']:g}, valid {L['splits']['valid']['long_ann']:+.1%} / {L['splits']['valid']['long_sharpe']:.2f}", flush=True)
        return res, daily

    def cs_corr(a, b, sl):
        za, zb_ = zscore_rows(rank_rows(load(a)[sl])), zscore_rows(rank_rows(load(b)[sl]))
        r = np.nanmean(za * zb_, axis=1)
        return float(np.nanmean(r))

    out = {"plan": "research/prod_W02L/COMBO_PLAN.md", "note": "description only; nothing of 2026",
           "build": json.loads((W / "combo_build.json").read_text(encoding="utf-8"))}
    with slot():
        mem = MemoryGuard(self_limit_gb=200, cgroup_limit_gb=850).start()
        full = ["C_WK", "C_WK_ng", "C_K", "C_LX", "C_W_ng", *CHAMPS]
        nested = ["C_WK_nested", "C_K_nested"]
        res, daily = books_of(full + nested)
        pairs = [("C_WK_nested", "C_K_nested"), ("C_WK_nested", "手写库冠军"), ("C_WK_nested", "挖掘冠军"), ("C_WK_nested", "C_LX"),
                 ("C_WK", "C_K"), ("C_WK_ng", "C_K"), ("C_WK", "C_LX")]
        out["books"] = res
        out["paired"] = {f"{a}-{b}": {k: {"train": stats((daily[a][k] - daily[b][k])[tr]), "valid": stats((daily[a][k] - daily[b][k])[va])}
                                       for k in ("excess", "ls")} for a, b in pairs}
        out["corr_valid"] = {f"{a}~{b}": cs_corr(a, b, va) for a, b in (("C_WK", "C_K"), ("C_WK_nested", "C_K_nested"), ("C_K", "手写库冠军"),
                                                                       ("C_K", "挖掘冠军"), ("手写库冠军", "挖掘冠军"), ("C_WK", "C_LX"))}
        mem.stop()
    (D / "combo.json").write_text(json.dumps(out, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
    (D / "combo.md").write_text(report(out), encoding="utf-8")
    print((D / "combo.md").read_text(encoding="utf-8"))


def report(out):
    b = out["build"]["pools"]
    L = ["# W02L 因子 + 两个冠军信号的合成：样本内描述(2026 未读)\n",
         "做法见 COMBO_PLAN.md。下面全是描述，不是检验。nested 版两层权重只拟合到 2023-08-07,valid 段对冠军和权重是样本外，但 W02L 的 head 是按 train + valid 挑的。\n",
         "## 建出来的合成\n", "| 合成 | 池子 | 健康 | 族 | 成员 | 含冠军的族 |", "|---|---|---|---|---|---|"]
    for k, v in b.items():
        L.append(f"| C_{k} | {v['signals']} | {v['healthy']} | {v['families']} | {v['members']} | {v['champion_families']} |")
    L += ["\n## 书(纯多头十分位净超额，扣 15 bp,减全市场等权;方向和 hl 在 2018 ~ 2023-08-07 上定)\n",
          "| 信号 | hl | train 2018 ~ 2023-08 | valid 2023-08 ~ 2025 | valid 回撤 |", "|---|---|---|---|---|"]
    for nm, r in out["books"].items():
        t_, v_ = r["long"]["train"], r["long"]["valid"]
        L.append(f"| {nm} | {r['hl_long']:g} | {t_['long_ann']:+.1%} / {t_['long_sharpe']:.2f} | {v_['long_ann']:+.1%} / {v_['long_sharpe']:.2f} | {v_['long_mdd']:.1%} |")
    L += ["\n## 成对差(逐日，年化;valid 段)\n", "| 比较 | 纯多头净超额 | 多空 |", "|---|---|---|"]
    for k, v in out["paired"].items():
        e, s = v["excess"]["valid"], v["ls"]["valid"]
        L.append(f"| {k} | {e['ann']:+.2%}(t {e['t']:+.2f}) | {s['ann']:+.2%}(t {s['t']:+.2f}) |")
    L += ["\n## valid 段逐日截面秩相关\n"] + [f"- {k}:{v:.3f}" for k, v in out["corr_valid"].items()]
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    {"prep": prep, "build": build, "describe": describe}[MODE]()
