"""The forward segment (2026-01 onward): one ledgered read of objects that were all fixed before it.

Server.  The rule is research/forward_2026/PLAN.md, written before any 2026 number was computed.  Everything read
here was defined earlier and is rebuilt WITHOUT refitting anything -- members, signs, half-lives, fusion weights come
from the stored results:

    L1/L2/L4  runs/_batch_<B>/fuse_<tag>.json      benchmarks, the six fusions, the originals and the members
    L5        runs/K001_known_screens/sweepfinal_s1.json   the screens on the known family
    L6        episodes/e4k1_e4k2_e4k3_final.json   the top finds of the e4 idea searches (screens)
    L7        the three conventions (user's / tradable universe / inside liquidity buckets) for the known family and
              the fusions O and A

Phase 1 is a REPRODUCTION CHECK that uses data up to 2025-12-31 only: every object is recomputed on the extended
view and its in-sample and old-test-period numbers must match the stored ones (the two last days of 2025 have a
label now; they are masked for the check).  If anything does not reproduce, the script stops before a single forward
number exists.  Phase 2 computes the forward segment and the combined out-of-sample period with the same functions.

    python scripts/forward_read.py [--batch B01] [--tag s4] [--end 20260916] [--check-only]
"""
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.guard import MemoryGuard, limit_threads, slot  # noqa: E402

limit_threads(8)
import math  # noqa: E402

import numpy as np  # noqa: E402

from partura import books as bk  # noqa: E402
from partura import diagnose as dg  # noqa: E402
from partura import ops_ext  # noqa: E402,F401
from partura import steer  # noqa: E402
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.panels import SHARED_CACHE, PanelSet  # noqa: E402
from partura.splits import Ledger  # noqa: E402

argv = sys.argv[1:]


def opt(name, default=None):
    return argv[argv.index(name) + 1] if name in argv else default


BATCH, TAG = opt("--batch", "B01"), opt("--tag", "s4")
STORE, MIRROR = "/root/autodl-tmp/qmt_daily_data/fast_factor_compute", "/root/autodl-tmp/AlphaCube/mirror"
from alphacube.store import open_cube_store  # noqa: E402

END = opt("--end") or str(open_cube_store(STORE, mirror_root=MIRROR).dates[-1])       # default: the last day the store has (base + increments)
CHECK_ONLY = "--check-only" in argv
START, US_END, HO_START, HO_END, FW_START = "20180102", "20230807", "20230808", "20251231", "20260101"
TRAIN_END = "20211231"                                        # train / valid inside the in-sample period (the search's split)
J = json.loads((PARTURA_ROOT / "runs" / f"_batch_{BATCH}" / f"fuse_{TAG}.json").read_text(encoding="utf-8"))
K1 = json.loads((PARTURA_ROOT / "runs" / "K001_known_screens" / "sweepfinal_s1.json").read_text(encoding="utf-8"))["results"]
E4 = json.loads((PARTURA_ROOT / "episodes" / "e4k1_e4k2_e4k3_final.json").read_text(encoding="utf-8"))["results"]
from alphacube.metrics import long_short_weights  # noqa: E402

exprs = {"aux:frozen": "cross_max(day_zero_ratio(Ret), 15)", "aux:age": "cross_valid_count(day_last(Close), 241)", "aux:liq": "cross_mean(day_sum(Amt), 30)"}
exprs.update({f"m:{k}": v["expr"] for k, v in J["members"].items()})
exprs.update({f"k:{k}": v["expr"] for k, v in K1.items()})
exprs.update({f"e:{i}": r["expr"] for i, r in enumerate(E4)})

with slot():
    mem = MemoryGuard(self_limit_gb=40, cgroup_limit_gb=70).start()
    t0 = time.time()
    ps = PanelSet(STORE, START, END, warmup=60, device="cuda", gpu_fraction=0,
                  cache_dir=str(SHARED_CACHE), mirror_root=MIRROR, workdir=str(PARTURA_ROOT / "tmp"),
                  label_kind="open_vwap15", label_buyable=True, batch=32)
    dates = np.asarray(ps.dates).astype(str)
    last = str(dates[-1])
    P = ps.compute(exprs)
    if ps.errors:
        raise SystemExit(f"[forward] expressions that did not evaluate on the extended view: {dict(ps.errors)}")
    tgt = np.asarray(ps.target(1), dtype=np.float64)
    ix = lambda d: int(np.searchsorted(dates, d))             # noqa: E731
    us, ho, fw = slice(0, ix(HO_START)), slice(ix(HO_START), ix(FW_START)), slice(ix(FW_START), len(dates))
    tr, va, oos = slice(0, ix("20220101")), slice(ix("20220101"), ix(HO_START)), slice(ix(HO_START), len(dates))
    if str(dates[us.stop - 1]) != US_END or str(dates[ho.stop - 1]) != HO_END:
        raise SystemExit(f"[forward] unexpected calendar: in-sample ends {dates[us.stop - 1]}, old test period ends {dates[ho.stop - 1]}")
    # the label of the two last days of 2025 did not exist when the stored numbers were made: mask them for the check
    tgt_old = tgt.copy()
    tgt_old[ho.stop - 2:] = np.nan
    print(f"[forward] view {dates[0]} .. {last}: {len(dates)} days x {tgt.shape[1]} names; in-sample {us.stop} days, old test period {ho.stop - ho.start}, "
          f"forward {fw.stop - fw.start} days ({dates[fw.start]} .. {last}; {int(np.isfinite(tgt[fw]).any(1).sum())} with a label)", flush=True)

    KEEP = ("long_ann", "long_sharpe", "long_mdd", "long_turnover")

    def row(sm, sl, target):
        r = bk.book_row(sm, target, sl)
        return {k: float(r[k]) for k in KEEP}

    def daily(sm, target):
        """One continuous pure long book over the whole view (scripts/batch_fuse.py: daily)."""
        return bk.long_book(long_short_weights(sm, bk.TOP_FRAC), sm, target)[0]

    def seg_net(sm, sl, target):
        """The book of one segment, started empty (scripts/sweep_final.py: the paired series)."""
        return bk.long_book(long_short_weights(sm[sl], bk.TOP_FRAC), sm[sl], target[sl])[0]

    def stats(d):
        f = d[np.isfinite(d)]
        if f.size < 20 or not f.std() > 0:
            return {"ann": float("nan"), "ir": float("nan"), "t": float("nan"), "n": int(f.size)}
        return {"ann": float(f.mean() * 252), "ir": float(f.mean() / f.std() * np.sqrt(252)), "t": float(f.mean() / f.std() * np.sqrt(f.size)), "n": int(f.size)}

    # ------------------------------------------------------------------ rebuild every object (signals only)
    SM, Zs = {}, {}
    for k, v in J["members"].items():
        raw = float(v["sign"]) * np.asarray(P[f"m:{k}"], dtype=np.float64)
        SM[f"m:{k}"] = bk.smoothed(raw, float(v["hl"]))
        Zs[k] = dg._zrank(SM[f"m:{k}"]).astype(np.float32)
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
    for name, fn in build.items():
        SM[f"f:{name}"] = bk.smoothed(fn(), float(J["fusions"][name]["methods"]["each"]["chosen_hl"]))
    for k, r in K1.items():
        SM[f"k:{k}"] = bk.smoothed(float(r["sign_user"]) * np.asarray(P[f"k:{k}"], dtype=np.float64), float(r["books_user"]["by_rank"]["long"]["hl"]))
    known_z = dg._zrank(float(J["members"]["known"]["sign"]) * np.asarray(P["m:known"], dtype=np.float64))     # the screens' base (hl 0)
    fin_k = np.isfinite(known_z)
    for i, r in enumerate(E4):
        sm0 = bk.smoothed(np.asarray(P[f"e:{i}"], dtype=np.float64), float(r["hl"]))
        band = steer._top_band(np.where(fin_k, float(r["sign"]) * sm0, np.nan))
        SM[f"e:{i}"] = np.where(fin_k, np.where(band, known_z - 2.0, known_z), np.nan)

    # ------------------------------------------------------------------ phase 1: does everything reproduce? (data to 2025-12-31 only)
    bad, worst = [], {"train_ann": 0.0, "train_sharpe": 0.0, "test_ann": 0.0, "test_sharpe": 0.0}
    # One documented exception (research/forward_2026/PLAN.md, amendment of 2026-10-06 23:36; evidence in
    # runs/_forward/view_consistency_20251231_20260916.json): F113's original adds 5 to a quantity of order 1e-3 and
    # then removes the cross-sectional mean, so in float32 its values carry only three or four digits and move by
    # about 1e-3 with the engine's chunking -- on every day of the history alike (rank correlation 0.99994-0.99999
    # each year, top decile 99.6-100% the same names), not towards the end: numerical fragility, not look-ahead.
    # Its book is weak (+0.6% a year) and moved by 0.08 points.  Every other object keeps the tight tolerance.
    TOL = {"member F113.orig": (2e-3, 0.05)}
    exceptions = []

    def check(name, got_tr, got_te, want_tr, want_te):
        ta, ts_ = TOL.get(name, (5e-4, 0.02))
        for seg, g, w in (("train", got_tr, want_tr), ("test", got_te, want_te)):
            if w is None:
                continue
            da, ds = abs(g["long_ann"] - w["long_ann"]), abs(g["long_sharpe"] - w["long_sharpe"])
            if name in TOL:
                exceptions.append(f"{name} {seg}: ann {g['long_ann']:+.4f} vs stored {w['long_ann']:+.4f}, sharpe {g['long_sharpe']:.3f} vs {w['long_sharpe']:.3f}")
                if da <= ta and ds <= ts_:
                    continue
            else:
                worst[f"{seg}_ann"], worst[f"{seg}_sharpe"] = max(worst[f"{seg}_ann"], da), max(worst[f"{seg}_sharpe"], ds)
            if not (da <= ta and ds <= ts_):
                bad.append(f"{name} {seg}: ann {g['long_ann']:+.4f} vs stored {w['long_ann']:+.4f}, sharpe {g['long_sharpe']:.3f} vs {w['long_sharpe']:.3f}")

    for k, v in J["members"].items():
        check(f"member {k}", row(SM[f"m:{k}"], us, tgt_old), row(SM[f"m:{k}"], ho, tgt_old), v["rows"]["train"], v["rows"]["test"])
    for name in build:
        M = J["fusions"][name]["methods"]["each"]
        g = next(x for x in M["grid"] if x["hl"] == M["chosen_hl"])
        check(f"fusion {name}", row(SM[f"f:{name}"], us, tgt_old), row(SM[f"f:{name}"], ho, tgt_old), g["train"], g["test"])
    for k, r in K1.items():
        sp = r["books_user"]["by_rank"]["long"]["splits"]
        check(f"K001 {k}", row(SM[f"k:{k}"], us, tgt_old), row(SM[f"k:{k}"], ho, tgt_old), sp["utrain"], sp["holdout"])
    for i, r in enumerate(E4):                                    # stored as paired differences against the base book
        for seg, sl in (("utrain", us), ("holdout", ho)):
            got = stats(seg_net(SM[f"e:{i}"], sl, tgt_old) - seg_net(known_z, sl, tgt_old))["ann"]
            if abs(got - r["paired"][seg]["ann"]) > 5e-4:
                bad.append(f"e4 find {i} ({r['episode']}/{r['arm']}) {seg}: paired ann {got:+.4f} vs stored {r['paired'][seg]['ann']:+.4f}")
    n_obj = len(J["members"]) + len(build) + len(K1) + len(E4)
    print(f"[forward] reproduction check on {n_obj} objects (data to {HO_END} only): largest deviation  in-sample ann {worst['train_ann']:.1e}, sharpe {worst['train_sharpe']:.1e};  "
          f"old test period ann {worst['test_ann']:.1e}, sharpe {worst['test_sharpe']:.1e}  ->  {'PASS' if not bad else 'FAIL'}", flush=True)
    out_dir = PARTURA_ROOT / "runs" / "_forward"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / f"check_{last}.json").write_text(json.dumps({"end": last, "objects": n_obj, "worst": worst, "failed": bad, "documented_exceptions": exceptions}, ensure_ascii=False, indent=1), encoding="utf-8")
    for x in exceptions:
        print("   documented exception (wider tolerance): " + x, flush=True)
    if bad:
        for b in bad[:20]:
            print("   " + b, flush=True)
        raise SystemExit("[forward] the stored numbers do not reproduce on the extended view: nothing of the forward segment was computed")
    if CHECK_ONLY:
        mem.stop()
        raise SystemExit(0)

    # ------------------------------------------------------------------ phase 2: the forward segment
    Ledger(out_dir / "ledger.json").record(
        "forward", n_obj, f"first read of the forward segment {dates[fw.start]}..{last} by research/forward_2026/PLAN.md: benchmarks, the six {TAG} fusions and their members, "
        f"the K001 screens, the e4 finds, the three conventions", f"forward_read_{last}")
    SEG = {"insample": us, "test": ho, "forward": fw, "oos": oos}

    def level(sm):
        return {nm: row(sm, sl, tgt) for nm, sl in SEG.items()}

    def paired_cont(a, b):                                        # continuous books (fusions and benchmarks)
        d = daily(a, tgt) - daily(b, tgt)
        return {nm: stats(d[sl]) for nm, sl in SEG.items()}

    def paired_seg(a, b):                                         # per-segment books (the screens, as they were stored)
        out = {nm: stats(seg_net(a, sl, tgt) - seg_net(b, sl, tgt)) for nm, sl in (("insample", us), ("test", ho), ("forward", fw))}
        out["oos"] = stats(np.concatenate([seg_net(a, ho, tgt) - seg_net(b, ho, tgt), seg_net(a, fw, tgt) - seg_net(b, fw, tgt)]))
        return out

    yrs = np.asarray([d[:4] for d in dates])

    def by_year(sm):
        d = daily(sm, tgt)
        return {y: float(np.nanmean(d[yrs == y]) * 252) for y in sorted(set(yrs))}

    res = {"end": last, "forward": [str(dates[fw.start]), last, int(np.isfinite(tgt[fw]).any(1).sum())], "years_oos": float(np.isfinite(tgt[oos]).any(1).sum()) / 252.0,
           "check": {"objects": n_obj, "worst": worst, "documented_exceptions": exceptions}, "benchmarks": {}, "fusions": {}, "paired": {}, "members": {}, "k001": {}, "e4": [], "conventions": {}, "daily": {}}
    for k in ("known", "known_xfrozen"):
        res["benchmarks"][k] = {"expr": J["members"][k]["expr"], "sign": J["members"][k]["sign"], "hl": J["members"][k]["hl"], "level": level(SM[f"m:{k}"]), "by_year": by_year(SM[f"m:{k}"])}
    for name in build:
        res["fusions"][name] = {"label": J["fusions"][name]["label"], "n_members": len(J["fusions"][name]["members"]), "hl": J["fusions"][name]["methods"]["each"]["chosen_hl"],
                                "level": level(SM[f"f:{name}"]), "by_year": by_year(SM[f"f:{name}"])}
    for a, b in (("f:A", "m:known"), ("f:C", "m:known"), ("f:B", "m:known"), ("f:O", "m:known"), ("f:A", "f:O"), ("f:U", "f:O"), ("m:known_xfrozen", "m:known"), ("f:A", "m:known_xfrozen")):
        res["paired"][f"{a[2:]}-{b[2:]}"] = paired_cont(SM[a], SM[b])
    for k, v in J["members"].items():
        if k in ("known", "known_xfrozen"):
            continue
        res["members"][k] = {"expr": v["expr"], "sign": v["sign"], "hl": v["hl"], "group": [g for g in ("orig", "upg", "indep") if k in G[g]] + (["known_head"] if k == "known_head" else []),
                             "level": level(SM[f"m:{k}"])}
    for k, r in K1.items():
        if r["kind"] in ("base",):
            continue
        res["k001"][k] = {"expr": r["expr"], "level": level(SM[f"k:{k}"]), "paired_vs_known": paired_seg(SM[f"k:{k}"], SM["k:k_known"])}
    for i, r in enumerate(E4):
        res["e4"].append({"episode": r["episode"], "arm": r["arm"], "expr": r["expr"], "sign": r["sign"], "hl": r["hl"], "paired_vs_known": paired_seg(SM[f"e:{i}"], known_z),
                          "level": level(SM[f"e:{i}"])})
    # ---- which money: the user's convention / the tradable universe / inside liquidity buckets
    frozen = np.asarray(P["aux:frozen"], np.float64)
    possible = np.minimum(241, np.arange(1, len(dates) + 1))[:, None]
    untradable = ((dg._zrank(frozen) + 0.5) > 0.8) | (np.asarray(P["aux:age"], np.float64) < 0.9 * possible) | ~np.isfinite(frozen)
    ctx = steer.RewardContext(tgt, us, ho, untradable=untradable, liq=np.asarray(P["aux:liq"], np.float64), pool=known_z, base=known_z)
    SEG4 = {"train": tr, "valid": va, "test": ho, "forward": fw}
    for nm, key in (("known", "m:known"), ("O", "f:O"), ("A", "f:A")):
        sm = SM[key]
        cut = np.where(untradable, np.nan, sm)
        buck = steer._bucket_rank(cut, ctx.bucket())
        res["conventions"][nm] = {c: {s: row(x, sl, tgt) for s, sl in SEG4.items()} for c, x in (("user", sm), ("tradable", cut), ("bucket", buck))}
    for nm, key in (("known", "m:known"), ("known_xfrozen", "m:known_xfrozen"), ("O", "f:O"), ("U", "f:U"), ("A", "f:A"), ("C", "f:C")):
        res["daily"][nm] = [None if x != x else round(float(x), 7) for x in daily(SM[key], tgt)]
    # L8 (PLAN, amended before the read): the same objects as a decile long/short book, and the pure long book's TOTAL
    # return (net excess + the equal-weight return of the names with a signal and a label).  Descriptive.
    from alphacube.metrics import portfolio_returns
    LSK = ("ls_ann", "ls_sharpe", "ls_mdd", "ls_turnover")
    r5 = lambda a: [None if x != x else round(float(x), 7) for x in a]    # noqa: E731
    res["ls"], res["series"] = {}, {}
    for nm, key in (("known", "m:known"), ("known_xfrozen", "m:known_xfrozen"), ("O", "f:O"), ("U", "f:U"), ("A", "f:A"), ("B", "f:B"), ("C", "f:C"), ("D", "f:D")):
        sm = SM[key]
        res["ls"][nm] = {s: {k: float(v) for k, v in bk.book_row(sm, tgt, sl).items() if k in LSK} for s, sl in SEG.items()}
        w = long_short_weights(sm, bk.TOP_FRAC)
        ok = np.isfinite(sm) & np.isfinite(tgt)
        cnt = ok.sum(1)
        ew = np.where(cnt > 0, np.where(ok, tgt, 0.0).sum(1) / np.maximum(cnt, 1), np.nan)
        net = bk.long_book(w, sm, tgt)[0]
        res["series"][nm] = {"ls": r5(portfolio_returns(w, tgt, bk.COST)[0]), "excess": r5(net), "bench": r5(ew), "total": r5(net + ew)}
    res["dates"] = [str(d) for d in dates]
    mem.stop()

p = out_dir / f"forward_read_{last}.json"
p.write_text(json.dumps(res, ensure_ascii=False, default=float), encoding="utf-8")
pc = lambda x: f"{x:+6.1%}"                                    # noqa: E731
print(f"\n== 前推段 {res['forward'][0]} ~ {res['forward'][1]}({res['forward'][2]} 个有标签的交易日);样本外合并段约 {res['years_oos']:.2f} 年")
print(f"{'':34s} | 样本内 净超额 / 夏普 | 原测试段          | 前推段            | 合并段")
for nm, o in list(res["benchmarks"].items()) + [(f"融合 {k}", v) for k, v in res["fusions"].items()]:
    L = o["level"]
    print(f"{nm[:34]:34s} | " + " | ".join(f"{pc(L[s]['long_ann'])} / {L[s]['long_sharpe']:5.2f}    " for s in ("insample", "test", "forward", "oos")))
print(f"\n{'成对差(同一天相减)':30s} | 样本内 年化 / t   | 原测试段 年化 / t  | 前推段 年化 / t    | 合并段 年化 / IR / t")
for k, o in res["paired"].items():
    print(f"{k[:30]:30s} | " + " | ".join(f"{pc(o[s]['ann'])} / {o[s]['t']:+5.1f}    " for s in ("insample", "test", "forward")) + f" | {pc(o['oos']['ann'])} / {o['oos']['ir']:+.2f} / {o['oos']['t']:+.1f}")
print(f"\nwrote {p} ({time.time() - t0:.0f}s)")
