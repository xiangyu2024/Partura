"""Batch sweep: one run, one factor, a couple of hundred hypotheses, one backtest table.

Instead of testing a handful of variants per round, generate every cheap hypothesis
about the tree at once and read them side by side:

* structure  -- ablate / isolate / substitute every node, sweep windows, swap fields
                (``partura.propose``: substitutes are siblings by MEASURED properties)
* leaves     -- swap the smallest sub-structures: Ret <-> the change rate of Volume /
                Amt (``in_pct``), prices among themselves, Volume <-> Amt
* memory     -- wrap the tree in day-axis memory (mean / max / min / EMA / std / z-score)
* shape      -- fold it, rank it inside liquidity buckets, residualise it on the known
                family, overlay it on the known family with small weights
* yours      -- any extra hypotheses in a YAML file (``--extra``): {id: {expr, why}}

Every variant gets the user's books (both conventions, half-life fitted on the fit
split), gates, and its rank correlation with the original and with the known family.
Nothing here reads the holdout.

    python scripts/sweep.py <factor_id> [--tag s1] [--extra studies/<fid>/hypo.yaml] [--max 260] [--jobs 12]
"""
import json
import os
import re
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.guard import MemoryGuard, limit_threads, slot  # noqa: E402

limit_threads(2)
import numpy as np  # noqa: E402
import yaml  # noqa: E402

from partura import books as bk  # noqa: E402
from partura import diagnose as dg  # noqa: E402
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.panels import SHARED_CACHE, PanelSet, parse_research  # noqa: E402
from partura.propose import propose  # noqa: E402
from partura.splits import SPLITS  # noqa: E402

argv = sys.argv[1:]
fid = argv[0]


def opt(name, default=None):
    return argv[argv.index(name) + 1] if name in argv else default


TAG = opt("--tag", "s1")
MAXV = int(opt("--max", 260))
JOBS = int(opt("--jobs", 12))
cfg = yaml.safe_load((PARTURA_ROOT / "configs" / f"{fid}.yaml").read_text(encoding="utf-8"))
for k, v in cfg["splits"].items():
    SPLITS[k] = (str(v[0]), str(v[1]))
SRC = cfg["expression"]
KNOWN = "cross_mean(day_std(Amt), 30)"
LIQ = "cross_mean(day_sum(Amt), 30)"
DT_WINDOWS = (5, 10, 30, 60)


def variants() -> dict:
    """id -> (expr, kind, why).  Everything that does not parse is dropped silently by the caller."""
    V = {"v_base": (SRC, "base", "原式"), "k_known": (KNOWN, "bench", "已知成交额族基准")}

    def add(i, e, kind, why):
        if i not in V:
            V[i] = (e, kind, why)

    try:
        for c in propose(SRC, max_substitutes=8, max_fields=8, max_nodes=40):
            add(c.id, c.expr, c.kind, c.why)
    except Exception as exc:  # noqa: BLE001
        print(f"[sweep] propose failed: {type(exc).__name__}: {exc}", flush=True)

    # the smallest sub-structures: a minute return and a minute volume change are the same kind of object
    leaf = {"Ret": [("volchg", "in_pct(Volume, 1)"), ("amtchg", "in_pct(Amt, 1)"), ("ret5", "in_pct(Close, 5)"),
                    ("vwapchg", "in_pct(Vwap, 1)"), ("logvol", "in_logchg(Volume, 1)")],
            "Volume": [("amt", "Amt"), ("volchg", "in_pct(Volume, 1)")],
            "Amt": [("vol", "Volume"), ("amtchg", "in_pct(Amt, 1)")],
            "Close": [("vwap", "Vwap"), ("high", "High"), ("low", "Low"), ("open", "Open")],
            "Low": [("close", "Close"), ("high", "High"), ("vwap", "Vwap")],
            "High": [("close", "Close"), ("low", "Low"), ("vwap", "Vwap")],
            "Open": [("close", "Close"), ("vwap", "Vwap")]}
    for field, subs in leaf.items():
        if re.search(rf"\b{field}\b", SRC):
            for name, rep in subs:
                add(f"leaf_{field}_{name}", re.sub(rf"\b{field}\b", rep, SRC), "leaf",
                    f"叶子 {field} 换成 {rep}")

    X = SRC
    for d in DT_WINDOWS:
        for op in ("cross_mean", "cross_max", "cross_min", "cross_ema", "cross_stddev", "cross_zscore", "cross_decay_linear"):
            add(f"mem_{op[6:]}{d}", f"{op}({X}, {d})", "memory", f"日轴记忆 {op}({d})")
    add("fold_mean", f"abs_(cs_demean({X}))", "shape", "截面均值折叠")
    add("fold_rank", f"abs_(cs_demean(cs_rank({X})))", "shape", "截面排名折叠")
    add("fold_sq", f"pow_2(cs_demean({X}))", "shape", "截面均值平方折叠")
    add("win", f"cs_winsor({X})", "shape", "截面缩尾(EMA 之前)")
    add("rk", f"cs_rank({X})", "shape", "先排名(EMA 之前):去掉幅度信息")
    add("z60", f"cross_zscore({X}, 60)", "shape", "相对自身 60 日的偏离")
    add("rel60", f"div({X}, cross_mean({X}, 60))", "shape", "相对自身 60 日均值的比值")
    add("bk_liq", f"cs_bucket_rank({X}, {LIQ})", "neutral", "成交额十分桶内排名(分桶中性)")
    add("bk_known", f"cs_bucket_rank({X}, {KNOWN})", "neutral", "已知族十分桶内排名")
    add("res_known", f"cs_regres(cs_rank({X}), cs_rank({KNOWN}))", "neutral", "对已知族的秩残差")
    add("res_liq", f"cs_regres(cs_rank({X}), cs_rank({LIQ}))", "neutral", "对成交额水平的秩残差")
    for w in (0.25, 0.5, 1.0):
        for s, sg in (("p", ""), ("m", "-")):
            add(f"ov_{s}{str(w).replace('.', '')}", f"add(cs_rank({KNOWN}), mul(cs_rank({X}), {sg}{w}))", "overlay",
                f"叠在已知族上,权重 {sg}{w}")
    extra = opt("--extra")
    if extra and Path(extra).is_file():
        for i, v in (yaml.safe_load(Path(extra).read_text(encoding="utf-8")) or {}).items():
            add(str(i), v["expr"] if isinstance(v, dict) else str(v), "hypo", (v.get("why", "") if isinstance(v, dict) else ""))
    return V


G = {}          # shared with the forked workers


def score(vid):
    p = G["panels"][vid]
    tgt, tr, va, us = G["tgt"], G["tr"], G["va"], G["us"]
    raw = np.asarray(p, dtype=np.float64)
    ic = dg.ic_row(p[tr], tgt[tr], target_ranks=G["tr_ranks"])
    sign = 1.0 if not np.isfinite(ic["rank_ic"]) or ic["rank_ic"] >= 0 else -1.0
    out = {"sign": sign, "rank_ic_train": abs(ic["rank_ic"]), "cov": ic["coverage_labelled"],
           "dist": dg.distinct_fraction(p[tr])}
    if not np.isfinite(ic["rank_ic"]):
        return vid, {**out, "dead": True}
    b = bk.books(sign * raw, tgt, tr, {"train": tr, "valid": va})
    u = bk.books(sign * raw, tgt, us, {"utrain": us})
    for name, src in (("train", b), ("valid", b), ("utrain", u)):
        for rk in ("long", "ls"):
            r = src["by_rank"][rk]["splits"][name]
            out[f"{name}_{rk}"] = {k: r[k] for k in ("long_ann", "long_sharpe", "long_gross_ann", "long_turnover",
                                                     "ls_sharpe", "short_gross_ann", "long_mdd")}
    out["hl_long"], out["hl_ls"], out["hl_long_u"] = b["hl_long"], b["hl_ls"], u["hl_long"]
    out["hl_train"] = {str(int(s["halflife"])): [s["long_ann"], s["long_sharpe"], s["ls_sharpe"]] for s in b["sweep"]}
    r = dg.rank_rows(bk.smoothed(sign * raw, b["hl_long"])[tr])
    from alphacube.metrics import cs_pearson, nanmean_quiet
    out["corr_orig"] = float(nanmean_quiet(cs_pearson(r, G["r_orig"])))
    out["corr_known"] = float(nanmean_quiet(cs_pearson(r, G["r_known"])))
    return vid, out


def fmt(x, pct=True):
    return "   —  " if x is None or x != x else (f"{x:+6.1%}" if pct else f"{x:+5.2f}")


with slot():
    mem = MemoryGuard(self_limit_gb=40, cgroup_limit_gb=70).start()
    t0 = time.time()
    V = {}
    for i, (e, kind, why) in variants().items():
        try:
            key = parse_research(e).key()
        except Exception:  # noqa: BLE001 - a wrapper that does not type-check on this tree is simply not a hypothesis
            continue
        if key not in {v[3] for v in V.values()} or i in ("v_base", "k_known"):
            V[i] = (e, kind, why, key)
        if len(V) >= MAXV:
            break
    print(f"[sweep] {fid}: {len(V)} variants ({', '.join(f'{k} {sum(1 for v in V.values() if v[1] == k)}' for k in dict.fromkeys(v[1] for v in V.values()))})", flush=True)
    lab = cfg.get("label") or {}
    ps = PanelSet("/root/autodl-tmp/qmt_daily_data/fast_factor_compute", SPLITS["full"][0], SPLITS["full"][1],
                  warmup=int(cfg.get("warmup", 60)), device="cuda", gpu_fraction=0, cache_dir=str(SHARED_CACHE),
                  mirror_root="/root/autodl-tmp/AlphaCube/mirror", workdir=str(PARTURA_ROOT / "tmp"),
                  label_kind=lab.get("kind", "open_vwap15"), label_buyable=bool(lab.get("buyable", True)), batch=8)
    panels = ps.compute({i: v[0] for i, v in V.items()})
    print(f"[sweep] panels: {len(panels)}/{len(V)} in {time.time() - t0:.0f}s; failed: {sorted(set(V) - set(panels))[:12]}", flush=True)
    tgt = ps.target(1)
    tr, va, us = ps.split_slice("train"), ps.split_slice("valid"), ps.split_slice("utrain")
    os.environ["PARTURA_RANK_DEVICE"] = ""           # workers are forked: CPU ranking only
    G.update(panels=panels, tgt=tgt, tr=tr, va=va, us=us, tr_ranks=dg.rank_rows(tgt[tr]))
    for name, key in (("r_orig", "v_base"), ("r_known", "k_known")):
        p = np.asarray(panels[key], dtype=np.float64)
        s0 = np.sign(dg.ic_row(panels[key][tr], tgt[tr], target_ranks=G["tr_ranks"])["rank_ic"]) or 1.0
        hl = bk.fit_halflives(s0 * p, tgt, tr)["hl_long"]
        G[name] = dg.rank_rows(bk.smoothed(s0 * p, hl)[tr])
    t1 = time.time()
    res = {}
    with ProcessPoolExecutor(max_workers=JOBS) as ex:
        for vid, out in ex.map(score, list(panels), chunksize=2):
            res[vid] = {"expr": V[vid][0], "kind": V[vid][1], "why": V[vid][2], **out}
    print(f"[sweep] scored {len(res)} variants in {time.time() - t1:.0f}s", flush=True)
    mem.stop()

out_p = PARTURA_ROOT / "runs" / fid / f"sweep_{TAG}.json"
out_p.parent.mkdir(parents=True, exist_ok=True)
out_p.write_text(json.dumps({"factor_id": fid, "tag": TAG, "expression": SRC, "known": KNOWN, "fit_split": "train",
                             "splits": {k: list(SPLITS[k]) for k in ("train", "valid", "utrain")},
                             "errors": {k: str(v)[:300] for k, v in ps.errors.items()}, "results": res},
                            ensure_ascii=False, indent=1, default=float), encoding="utf-8")

live = {k: v for k, v in res.items() if not v.get("dead")}
order = sorted(live, key=lambda k: -(live[k]["utrain_long"]["long_sharpe"] if live[k]["utrain_long"]["long_sharpe"] == live[k]["utrain_long"]["long_sharpe"] else -9))
print(f"\n== {fid}  批量扫描 {TAG}:{len(live)} 个变体(只用 train / valid;半衰期按纯多头书在 train 上选)==")
print("多头腿净超额 Lnet 与纯多头夏普 Lshp:train | valid(train 上定方向和半衰期)| utrain(用户训练段);ρo / ρk = 与原式 / 已知族的交易信号 rank 相关")
print("底腿 = 最低十分位相对等权的毛超额(为正说明把方向反过来,多头腿是它);方向 sg 按 train 的 rank IC 定")
hdr = f"{'id':22s} {'kind':8s} sg hlL | Lnet tr     va     ut   | Lshp tr    va    ut  | LTO   | LS tr   va  | 底腿 tr    va   |  ρo    ρk  | cov  dist | expr"
print(hdr)


def line(k):
    v = live[k]
    a, b, c = v["train_long"], v["valid_long"], v["utrain_long"]
    gate = "" if (v["cov"] >= 0.95 and v["dist"] >= 0.5) else " ✗门槛"
    return (f"{k[:22]:22s} {v['kind'][:8]:8s} {int(v['sign']):+d} {v['hl_long']:>3g} | {fmt(a['long_ann'])} {fmt(b['long_ann'])} {fmt(c['long_ann'])} "
            f"| {fmt(a['long_sharpe'], 0)} {fmt(b['long_sharpe'], 0)} {fmt(c['long_sharpe'], 0)} | {a['long_turnover']:5.1%} "
            f"| {fmt(v['train_ls']['ls_sharpe'], 0)} {fmt(v['valid_ls']['ls_sharpe'], 0)} "
            f"| {fmt(-a['short_gross_ann'])} {fmt(-b['short_gross_ann'])} | {v['corr_orig']:+.2f} {v['corr_known']:+.2f} "
            f"| {v['cov']:.2f} {v['dist']:.2f}{gate} | {v['expr'][:120]}")


for k in ("v_base", "k_known"):
    if k in live:
        print(line(k))
print("-" * 60 + " 按 utrain 纯多头夏普排序的前 45 个")
for k in order[:45]:
    print(line(k))
print("-" * 60 + " 每一类里最好的 3 个(按 utrain 纯多头夏普)")
for kind in dict.fromkeys(v["kind"] for v in live.values()):
    for k in [x for x in order if live[x]["kind"] == kind][:3]:
        print(line(k))
print("-" * 60 + " 垫底的 8 个(方向反过来也是信息)")
for k in order[-8:]:
    print(line(k))
print(f"\nwrote {out_p}  ({time.time() - t0:.0f}s total)")
