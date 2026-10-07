"""Stage 2 of research/two_level/PLAN.md: carry two-level champions into the forward segment, then read it once.

Server.  For every champion (AlphaCube's two existing ones and the stage-1 signals built on pools with Partura's
signals) this

1. takes the champion's OWN families (its ``.families.json``: nothing is re-selected) and its members' panels on the
   extended view (2018-01-02 .. the store's last day; ``scripts/extend_members.py`` computed them),
2. rebuilds the signal with AlphaCube's own code -- ``build_champion.build``: z-score per day, direction by the
   training-period IC, ridge inside a family, least squares across families -- with the training period cut BY DATE
   at 2023-08-07 (the first 1359 days), exactly where the stored signal was fitted,
3. checks, on data up to 2025-12-31 only, that the rebuilt signal is the stored one (daily rank correlation, and the
   books of the old test period),
4. and only for signals that pass, reads the forward segment and the combined out-of-sample period in the book
   convention of ``partura.books.books`` (the convention of research/alpha_distillation/ALL_best_books.md), with the
   paired daily differences the plan names.  The read is ledgered.

    two_level_forward.py [--only C_LQ,手写库冠军] [--check-only] [--members runs/_forward/members_<end>.json]
"""
import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.guard import MemoryGuard, limit_threads, slot  # noqa: E402

limit_threads(8)
import numpy as np  # noqa: E402

from partura import books as bk  # noqa: E402
from partura import diagnose as dg  # noqa: E402
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.splits import Ledger  # noqa: E402

AC = Path("/root/autodl-tmp/AlphaCube")
sys.path.insert(0, str(AC / "scripts"))
argv = sys.argv[1:]


def opt(name, default=None):
    return argv[argv.index(name) + 1] if name in argv else default


STORE = "/root/autodl-tmp/qmt_daily_data/fast_factor_compute"
B, P = AC / "_bench" / "trainto", PARTURA_ROOT / "pools"
STORED = {"手写库冠军": B / "legacy_signal.npy", "挖掘冠军": B / "champion_signal_buyable.npy",
          **{n: P / "signals" / f"{n}.npy" for n in ("C_Q", "C_LQ", "C_MQ", "C_LM", "C_LMQ")}}
PAIRS = [("C_LQ", "手写库冠军"), ("C_MQ", "挖掘冠军"), ("C_LMQ", "C_LM"),                    # the plan's main comparisons
         ("C_Q", "手写库冠军"), ("C_Q", "挖掘冠军"), ("C_LM", "手写库冠军"), ("C_LM", "挖掘冠军"), ("C_LMQ", "挖掘冠军"), ("C_LMQ", "手写库冠军"),
         ("挖掘冠军", "手写库冠军")]
mfile = opt("--members")
if not mfile:
    c = sorted((PARTURA_ROOT / "runs" / "_forward").glob("members_2*.json"))
    mfile = str(c[-1]) if c else str(PARTURA_ROOT / "runs" / "_forward" / "members_base.json")
M = json.loads(Path(mfile).read_text(encoding="utf-8"))
only = set((opt("--only") or "").split(",")) - {""}
names = [n for n in M["champions"] if (not only or n in only) and STORED.get(n) is not None and STORED[n].is_file()]
END = M["end"]
out_dir = PARTURA_ROOT / "runs" / "_forward"
work = PARTURA_ROOT / "pools" / "_ext"

with slot():
    mem = MemoryGuard(self_limit_gb=60, cgroup_limit_gb=80).start()
    t0 = time.time()
    from alphacube.label import Label, open_vwap15
    from alphacube.metrics import long_short_weights, portfolio_returns
    from alphacube.research import warmed_view
    from alphacube.store import open_cube_store
    from build_champion import build

    view, _ = warmed_view(open_cube_store(STORE), "20180102", END, warmup=60)
    dates = np.asarray([str(d) for d in view.dates])
    tgt = Label("open_vwap15", 1, buyable=True).compute(view, price=open_vwap15(view)).astype(np.float64)       # the label the champions were fitted on
    ix = lambda d: int(np.searchsorted(dates, d))             # noqa: E731
    us, ho, fw, oos = slice(0, ix("20230808")), slice(ix("20230808"), ix("20260101")), slice(ix("20260101"), len(dates)), slice(ix("20230808"), len(dates))
    n_old = ho.stop
    if us.stop != 1359 or str(dates[n_old - 1]) != "20251231":
        raise SystemExit(f"unexpected calendar: training period {us.stop} days, old view ends {dates[n_old - 1]}")
    tgt_old = tgt.copy()
    tgt_old[n_old - 2:] = np.nan                               # as the stored signals saw it: no label on the two last days of 2025, nothing after
    print(f"[tl2] view to {END}: {len(dates)} days x {tgt.shape[1]}; training period {us.stop} days; forward {fw.stop - fw.start} days; champions {names}", flush=True)

    def rankcorr(a, b, step=5):
        cs = []
        for d in range(0, a.shape[0], step):
            m = np.isfinite(a[d]) & np.isfinite(b[d])
            if m.sum() > 100:
                ra, rb = np.argsort(np.argsort(a[d, m])), np.argsort(np.argsort(b[d, m]))
                cs.append(np.corrcoef(ra, rb)[0, 1])
        return float(np.mean(cs)), float(np.min(cs))

    def books_of(sig, target, splits):
        ic = dg.ic_row(sig[us], target[us], target_ranks=dg.rank_rows(target[us]))
        sign = 1.0 if not np.isfinite(ic["rank_ic"]) or ic["rank_ic"] >= 0 else -1.0
        return sign, bk.books(sign * sig, target, us, splits)

    def stats(d):
        f = d[np.isfinite(d)]
        if f.size < 20 or not f.std() > 0:
            return {"ann": float("nan"), "ir": float("nan"), "t": float("nan"), "n": int(f.size)}
        return {"ann": float(f.mean() * 252), "ir": float(f.mean() / f.std() * np.sqrt(252)), "t": float(f.mean() / f.std() * np.sqrt(f.size)), "n": int(f.size)}

    KEEP = ("long_ann", "long_sharpe", "long_mdd", "long_turnover", "ls_ann", "ls_sharpe", "ls_mdd")
    res = {"end": END, "members_file": mfile, "check": {}, "signals": {}, "paired": {}, "series": {}, "dates": [str(d) for d in dates]}
    SIG = {}
    for name in names:
        C = M["champions"][name]
        d = work / name
        (d / "panels").mkdir(parents=True, exist_ok=True)
        rows, fams, missing = [], [], 0
        for f in C["families"]:
            idx = []
            for m_ in f:
                e = M["expressions"][m_["key"]]
                if not e.get("path") or not Path(e["path"]).is_file():
                    missing += 1
                    continue
                dst = d / "panels" / f"{len(rows):05d}.npy"
                if dst.exists() or dst.is_symlink():
                    dst.unlink()
                os.link(e["path"], dst)
                idx.append(len(rows))
                rows.append({"i": len(rows)})
            if idx:
                fams.append(idx)
        t1 = time.time()
        sig = build(d, rows, fams, tgt_old, us)                                 # AlphaCube's own fitting; the label it sees stops where the stored one did
        np.save(out_dir / f"signal_{name}_{END}.npy", sig.astype(np.float32))
        # ---- the check: is this the stored signal?  (nothing after 2025-12-31 enters)
        stored = np.load(STORED[name]).astype(np.float64)
        mean_rc, min_rc = rankcorr(sig[:n_old], stored)
        sp = {"utrain": us, "holdout": ho}
        s_new, b_new = books_of(sig, tgt_old, sp)
        s_old, b_old = books_of(np.vstack([stored, np.full((len(dates) - n_old, stored.shape[1]), np.nan)]), tgt_old, sp)
        ln, lo_ = b_new["by_rank"]["long"]["splits"]["holdout"], b_old["by_rank"]["long"]["splits"]["holdout"]
        sn, so = b_new["by_rank"]["ls"]["splits"]["holdout"], b_old["by_rank"]["ls"]["splits"]["holdout"]
        ok = bool(mean_rc >= 0.995 and abs(ln["long_ann"] - lo_["long_ann"]) <= 0.010 and abs(sn["ls_sharpe"] - so["ls_sharpe"]) <= 0.20 and s_new == s_old)
        res["check"][name] = {"families": len(fams), "members": len(rows), "members_missing": missing, "rank_corr_mean": mean_rc, "rank_corr_min": min_rc,
                              "test_long_ann": [ln["long_ann"], lo_["long_ann"]], "test_long_sharpe": [ln["long_sharpe"], lo_["long_sharpe"]],
                              "test_ls_sharpe": [sn["ls_sharpe"], so["ls_sharpe"]], "pass": ok, "seconds": time.time() - t1}
        print(f"[tl2] {name}: {len(fams)} families, {len(rows)} members ({missing} missing); rebuilt vs stored on 2018-2025: daily rank corr {mean_rc:.4f} (min {min_rc:.4f}); "
              f"test long {ln['long_ann']:+.1%} vs {lo_['long_ann']:+.1%}, LS {sn['ls_sharpe']:.2f} vs {so['ls_sharpe']:.2f} -> {'PASS' if ok else 'FAIL'} ({time.time() - t1:.0f}s)", flush=True)
        if ok:
            SIG[name] = sig
        del stored
    (out_dir / f"two_level_check_{END}.json").write_text(json.dumps(res["check"], ensure_ascii=False, indent=1), encoding="utf-8")
    if "--check-only" in argv or not SIG:
        mem.stop()
        raise SystemExit(0 if SIG else 2)

    # ------------------------------------------------------------------ the forward segment (signals that reproduce)
    Ledger(out_dir / "ledger.json").record("forward", len(SIG), f"two-level champions carried to {END} (research/two_level/PLAN.md, stage 2): " + ", ".join(SIG), f"two_level_forward_{END}")
    SEG = {"insample": us, "test": ho, "forward": fw, "oos": oos}
    DAILY = {}
    for name, sig in SIG.items():
        sign, b = books_of(sig, tgt, SEG)
        L, S = b["by_rank"]["long"], b["by_rank"]["ls"]
        res["signals"][name] = {"sign": sign, "hl_long": L["hl"], "hl_ls": S["hl"], "long": {s: {k: float(v[k]) for k in KEEP if k.startswith("long")} for s, v in L["splits"].items()},
                                "ls": {s: {k: float(v[k]) for k in KEEP if k.startswith("ls")} for s, v in S["splits"].items()}}
        sm_lo, sm_ls = bk.smoothed(sign * sig, L["hl"]), bk.smoothed(sign * sig, S["hl"])
        w = long_short_weights(sm_lo, bk.TOP_FRAC)
        net = bk.long_book(w, sm_lo, tgt)[0]
        okc = np.isfinite(sm_lo) & np.isfinite(tgt)
        cnt = okc.sum(1)
        ew = np.where(cnt > 0, np.where(okc, tgt, 0.0).sum(1) / np.maximum(cnt, 1), np.nan)
        ls_net = portfolio_returns(long_short_weights(sm_ls, bk.TOP_FRAC), tgt, bk.COST)[0]
        DAILY[name] = {"excess": net, "ls": ls_net}
        r5 = lambda a: [None if x != x else round(float(x), 7) for x in a]      # noqa: E731
        res["series"][name] = {"ls": r5(ls_net), "excess": r5(net), "bench": r5(ew), "total": r5(net + ew)}
        x = res["signals"][name]
        print(f"[tl2] {name:10s} 纯多头 净超额 / 夏普: 样本内 {x['long']['insample']['long_ann']:+.1%} / {x['long']['insample']['long_sharpe']:.2f} | 测试 {x['long']['test']['long_ann']:+.1%} / {x['long']['test']['long_sharpe']:.2f} | "
              f"前推 {x['long']['forward']['long_ann']:+.1%} / {x['long']['forward']['long_sharpe']:.2f} | 合并 {x['long']['oos']['long_ann']:+.1%} / {x['long']['oos']['long_sharpe']:.2f}   "
              f"多空: 测试 {x['ls']['test']['ls_sharpe']:.2f} 前推 {x['ls']['forward']['ls_sharpe']:.2f} 合并 {x['ls']['oos']['ls_sharpe']:.2f}", flush=True)
    for a, b_ in PAIRS:
        if a in DAILY and b_ in DAILY:
            res["paired"][f"{a}-{b_}"] = {k: {s: stats((DAILY[a][k] - DAILY[b_][k])[sl]) for s, sl in SEG.items()} for k in ("excess", "ls")}
            q = res["paired"][f"{a}-{b_}"]["excess"]
            print(f"[tl2] {a} − {b_}(纯多头净超额,同一天相减): 测试 {q['test']['ann']:+.1%} (t {q['test']['t']:+.1f}) | 前推 {q['forward']['ann']:+.1%} (t {q['forward']['t']:+.1f}) | 合并 {q['oos']['ann']:+.1%} (t {q['oos']['t']:+.1f})", flush=True)
    mem.stop()

p = out_dir / f"two_level_forward_{END}.json"
p.write_text(json.dumps(res, ensure_ascii=False, default=float), encoding="utf-8")
print(f"[tl2] wrote {p} ({time.time() - t0:.0f}s)")
