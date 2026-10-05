"""The test-period read for a batch sweep -- by a rule written before looking, with no judgement in it.

From ``runs/<fid>/sweep_<tag>.json`` (train / valid only) it picks, mechanically:

* ``v_base`` (the original) and ``k_known`` (the known-family benchmark), always;
* the best variant of each of the 3 best KINDS (structure / leaf / memory / shape / neutral /
  hypothesis ...), ranked by pure-long Sharpe on the user's training period, among variants that
  pass the gates (cov >= 0.95, dist >= 0.5) and whose long leg is positive on BOTH train and valid;
* the two best candidates BUILT ON the known family (overlays, screens, or any hypothesis that contains
  it) -- reported apart, because they are the known family plus a tilt or minus a screen;
* ``k_known_xfrozen``, the generic screen (known family, never the frozen-quote names), as their benchmark.

Only these are scored on the holdout (the user's test period), in the user's convention: half-life fitted on
the user's training period, pure long book net of 15 bp.  The sign of the original and of the benchmarks is the
sign of their rank IC on the user's training period (the user's rule); a picked candidate keeps the sign it was
picked under (``sign_flip`` marks the rare weak signal whose rank IC changes sign once valid is added).  The read
is ledgered.

    python scripts/sweep_final.py <factor_id> [--sweep s1] [--per-kind 1] [--kinds 3] [--ids a,b]
"""
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.guard import MemoryGuard, limit_threads, slot  # noqa: E402

limit_threads(4)
import numpy as np  # noqa: E402
import yaml  # noqa: E402

from partura import books as bk  # noqa: E402
from partura import diagnose as dg  # noqa: E402
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.panels import SHARED_CACHE, PanelSet  # noqa: E402
from partura.splits import SPLITS, Ledger  # noqa: E402

argv = sys.argv[1:]
fid = argv[0]


def opt(name, default=None):
    return argv[argv.index(name) + 1] if name in argv else default


SW = opt("--sweep", "s1")
NK = int(opt("--kinds", 3))
cfg = yaml.safe_load((PARTURA_ROOT / "configs" / f"{fid}.yaml").read_text(encoding="utf-8"))
for k, v in cfg["splits"].items():
    SPLITS[k] = (str(v[0]), str(v[1]))
R = json.loads((PARTURA_ROOT / "runs" / fid / f"sweep_{SW}.json").read_text(encoding="utf-8"))["results"]


def shp(k):
    x = R[k].get("utrain_long", {}).get("long_sharpe")
    return x if x is not None and x == x else -9.0


ok = [k for k, v in R.items() if not v.get("dead") and v["cov"] >= 0.95 and v["dist"] >= 0.5
      and v["kind"] not in ("bench", "base")
      and (v["train_long"]["long_ann"] or -1) > 0 and (v["valid_long"]["long_ann"] or -1) > 0]
ok.sort(key=lambda k: -shp(k))
ON_KNOWN = ("overlay", "screen")          # these are the known family plus a tilt / minus a screen: reported apart


def uses_known(k):
    return R[k]["kind"] in ON_KNOWN or "day_std(Amt)" in R[k]["expr"]


picks, kinds = [], []
for k in ok:
    kind = R[k]["kind"]
    if uses_known(k) or kind in kinds:
        continue
    picks.append(k)
    kinds.append(kind)
    if len(kinds) >= NK:
        break
ov = [k for k in ok if uses_known(k)][:2]
extra = [k for k in (opt("--ids") or "").split(",") if k in R]
ids = [k for k in dict.fromkeys(["v_base", "k_known", "k_known_xfrozen"] + picks + ov + extra) if k in R and not R[k].get("dead")]
print(f"[final] {fid}: rule picks {picks} overlay {ov} extra {extra}", flush=True)

with slot():
    mem = MemoryGuard(self_limit_gb=30, cgroup_limit_gb=70).start()
    t0 = time.time()
    lab = cfg.get("label") or {}
    ps = PanelSet("/root/autodl-tmp/qmt_daily_data/fast_factor_compute", SPLITS["full"][0], SPLITS["full"][1],
                  warmup=int(cfg.get("warmup", 60)), device="cuda", gpu_fraction=0, cache_dir=str(SHARED_CACHE),
                  mirror_root="/root/autodl-tmp/AlphaCube/mirror", workdir=str(PARTURA_ROOT / "tmp"),
                  label_kind=lab.get("kind", "open_vwap15"), label_buyable=bool(lab.get("buyable", True)), batch=8)
    P = ps.compute({k: R[k]["expr"] for k in ids})
    tgt = ps.target(1)
    us, ho = ps.split_slice("utrain"), ps.split_slice("holdout")
    us_ranks = dg.rank_rows(tgt[us])
    Ledger(PARTURA_ROOT / "runs" / fid / "ledger.json").record(
        "holdout", len(ids), f"batch sweep {SW}: candidates picked by a fixed rule on train/valid ({', '.join(ids)})", f"sweep_final_{SW}")
    out = {"factor_id": fid, "sweep": SW, "rule": __doc__.split("    python")[0].strip(), "picks": picks, "overlay": ov, "results": {}}
    yrs = ps.years
    for k in ids:
        raw = np.asarray(P[k], dtype=np.float64)
        ic = dg.ic_row(P[k][us], tgt[us], target_ranks=us_ranks)
        sign_ic = 1.0 if not np.isfinite(ic["rank_ic"]) or ic["rank_ic"] >= 0 else -1.0
        # The original and the benchmarks are read in the user's convention (sign of the rank IC on their training
        # period).  A picked candidate is read with the sign it was PICKED under (the sweep's, fitted on train): a weak
        # signal's rank IC can change sign between train and train+valid, and the book that was selected is the one
        # whose test period must be read -- not its mirror image.
        sign = sign_ic if R[k]["kind"] in ("base", "bench") else float(R[k]["sign"])
        b = bk.books(sign * raw, tgt, us, {"utrain": us, "holdout": ho})
        sm = bk.smoothed(sign * raw, b["hl_long"])
        from alphacube.metrics import long_short_weights
        by = {}
        for y in sorted(set(yrs)):
            d = np.nonzero(yrs == y)[0]
            sl = slice(int(d[0]), int(d[-1]) + 1)
            w = long_short_weights(sm[sl], bk.TOP_FRAC)
            net = bk.long_book(w, sm[sl], tgt[sl])[0]
            by[str(y)] = float(np.nanmean(net) * 252)
        out["results"][k] = {"expr": R[k]["expr"], "kind": R[k]["kind"], "why": R[k]["why"], "sign_user": sign,
                             "sign_ic_utrain": sign_ic, "sign_flip": bool(sign != sign_ic),
                             "corr_orig": R[k].get("corr_orig"), "corr_known": R[k].get("corr_known"),
                             "books_user": b, "by_year_long_net": by}
    mem.stop()

p = PARTURA_ROOT / "runs" / fid / f"sweepfinal_{SW}.json"
p.write_text(json.dumps(out, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
print(f"\n== {fid} 测试段读数(批量扫描 {SW};候选按写死的规则只用 train/valid 选出)==")
print(f"{'id':22s} {'kind':8s} sg hlL | 多头净超额 训练/测试 | 纯多头夏普 训练/测试 | 换手  | 多空夏普 训/测 |  ρo    ρk  | 逐年多头净超额 2018..2025")
for k in ids:
    r = out["results"][k]
    v = r["books_user"]["by_rank"]
    a, h = v["long"]["splits"]["utrain"], v["long"]["splits"]["holdout"]
    la, lh = v["ls"]["splits"]["utrain"], v["ls"]["splits"]["holdout"]
    print(f"{k[:22]:22s} {r['kind'][:8]:8s} {int(r['sign_user']):+d} {v['long']['hl']:>3g} | {a['long_ann']:+6.1%} / {h['long_ann']:+6.1%}   | "
          f"{a['long_sharpe']:+5.2f} / {h['long_sharpe']:+5.2f}     | {a['long_turnover']:4.1%} | {la['ls_sharpe']:+5.2f} / {lh['ls_sharpe']:+5.2f} | "
          f"{(r['corr_orig'] or 0):+.2f} {(r['corr_known'] or 0):+.2f} | " + " ".join(f"{x:+5.1%}" for x in r["by_year_long_net"].values()))
    print(f"{'':22s} {r['expr'][:170]}")
print(f"\nwrote {p} ({time.time() - t0:.0f}s)")
