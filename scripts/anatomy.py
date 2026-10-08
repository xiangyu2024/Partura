"""Market anatomy: WHERE and WHEN does a signal's long leg earn its excess?

For the original, the known-family benchmark and the best variants of a sweep, on the
user's training period only (no holdout), with the signal that would be traded
(sign x panel, EMA at the half-life the pure long book prefers):

* by stock universe -- board, float-cap quintile, liquidity quintile, price quintile,
  listing age.  Two numbers per segment: the long-leg net excess of a book built
  INSIDE the segment (does it select there?) and how the full-market book is
  allocated to it (does it merely avoid / load on the segment?).
* by time -- each year, and market regimes known at the close of day t: trailing
  20-day market return up / down, trailing market volatility high / low, market
  turnover expanding / contracting.

    python scripts/anatomy.py <factor_id> [--sweep s1] [--top 8] [--ids a,b,c]
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
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.panels import SHARED_CACHE, PanelSet, config_daily_root, default_mirror, default_store  # noqa: E402
from partura.splits import SPLITS  # noqa: E402

argv = sys.argv[1:]
fid = argv[0]


def opt(name, default=None):
    return argv[argv.index(name) + 1] if name in argv else default


SW = opt("--sweep", "s1")
TOP = int(opt("--top", 8))
cfg = yaml.safe_load((PARTURA_ROOT / "configs" / f"{fid}.yaml").read_text(encoding="utf-8"))
for k, v in cfg["splits"].items():
    SPLITS[k] = (str(v[0]), str(v[1]))
sweep = json.loads((PARTURA_ROOT / "runs" / fid / f"sweep_{SW}.json").read_text(encoding="utf-8"))
R = sweep["results"]
live = {k: v for k, v in R.items() if not v.get("dead") and v["cov"] >= 0.95 and v["dist"] >= 0.5}
order = sorted(live, key=lambda k: -(live[k]["utrain_long"]["long_sharpe"] if live[k]["utrain_long"]["long_sharpe"] == live[k]["utrain_long"]["long_sharpe"] else -9))
ids = opt("--ids").split(",") if opt("--ids") else []
picked = []
for k in ["v_base", "k_known"] + ids + [k for k in order if live[k]["kind"] not in ("overlay", "bench")][:TOP]:
    if k in R and k not in picked and not R[k].get("dead"):
        picked.append(k)


def qbucket(x, n=5):
    """Per-day quantile bucket 0..n-1 (NaN where missing)."""
    r = np.full(x.shape, np.nan)
    order_ = np.argsort(np.where(np.isfinite(x), x, np.inf), axis=1, kind="stable")
    cnt = np.isfinite(x).sum(1)
    pos = np.empty_like(order_)
    np.put_along_axis(pos, order_, np.arange(x.shape[1])[None, :].repeat(x.shape[0], 0), axis=1)
    with np.errstate(invalid="ignore", divide="ignore"):
        q = np.floor(pos / np.maximum(cnt, 1)[:, None] * n)
    return np.where(np.isfinite(x), np.minimum(q, n - 1), r)


def board(sym):
    c = sym.split(".")[0][-6:] if "." in sym else sym[-6:]
    if c.startswith(("688", "689")):
        return "科创板"
    if c.startswith(("300", "301")):
        return "创业板"
    if c.startswith(("8", "4", "92")):
        return "北交所"
    if c.startswith("6"):
        return "沪主板"
    return "深主板"


def ann(x):
    f = x[np.isfinite(x)]
    return (float(f.mean() * 252), float(f.mean() / f.std() * np.sqrt(252)) if f.size > 2 and f.std() > 0 else float("nan")) if f.size else (float("nan"), float("nan"))


with slot():
    mem = MemoryGuard(self_limit_gb=30, cgroup_limit_gb=70).start()
    t0 = time.time()
    lab = cfg.get("label") or {}
    ps = PanelSet(default_store(), SPLITS["full"][0], SPLITS["full"][1],
                  warmup=int(cfg.get("warmup", 60)), device="cuda", gpu_fraction=0, cache_dir=str(SHARED_CACHE),
                  mirror_root=default_mirror(), workdir=str(PARTURA_ROOT / "tmp"),
                  label_kind=lab.get("kind", "open_vwap15"), label_buyable=bool(lab.get("buyable", True)), batch=8,
                  daily_root=config_daily_root(cfg))
    aux = {"a_px": "day_last(Close)", "a_amt20": "cross_mean(day_sum(Amt), 20)",
           "a_ret": "div(day_last(Close), ts_delay(day_last(Close), 1))", "a_flat": "day_flat_ratio(Close)"}
    P = ps.compute({**{k: R[k]["expr"] for k in picked}, **aux})
    tgt = ps.target(1)
    us = ps.split_slice("utrain")
    T = tgt[us]
    cap = ps.external("/root/autodl-tmp/Partura/shared/log_float_cap.npy")[us]
    px, amt = np.asarray(P["a_px"], np.float64)[us], np.asarray(P["a_amt20"], np.float64)[us]
    full_px = np.asarray(P["a_px"], np.float64)
    seen = np.cumsum(np.isfinite(full_px), axis=0)                         # trading days with a price so far
    old_name = np.isfinite(full_px[:20]).any(axis=0)                       # already trading when the view starts: not a new listing
    age = np.where(old_name[None, :], 10 ** 6, seen)[us]
    flat = np.asarray(P["a_flat"], np.float64)
    hit = np.zeros_like(flat, dtype=bool)                                  # a (near-)frozen quote in the last 15 days
    fr = np.nan_to_num(flat, nan=0.0) > 0.9
    for lag in range(15):
        hit[lag:] |= fr[: fr.shape[0] - lag] if lag else fr
    hit = hit[us]
    bd = np.array([board(s) for s in ps.symbols])
    seg = {}
    for b in ("沪主板", "深主板", "创业板", "科创板", "北交所"):
        m = np.broadcast_to(bd == b, T.shape)
        if (bd == b).sum() >= 100:
            seg[f"板块:{b}"] = m
    for name, x in (("流通市值", cap), ("成交额(20日)", amt), ("价格", px)):
        q = qbucket(x)
        for i, lbl in enumerate(("最低20%", "20-40%", "40-60%", "60-80%", "最高20%")):
            seg[f"{name}:{lbl}"] = q == i
    seg["上市:不足250日"] = age < 250
    seg["上市:250日以上"] = age >= 250
    seg["近15日有冻结盘口(封板/停牌)"] = hit
    seg["近15日无冻结盘口"] = ~hit
    # market regimes, known at the close of day t
    ret = np.asarray(P["a_ret"], np.float64) - 1.0
    mkt = np.nanmean(ret, axis=1)
    c = np.nancumsum(np.nan_to_num(mkt))
    tr20 = np.r_[np.full(20, np.nan), c[20:] - c[:-20]]
    vol20 = np.array([np.nanstd(mkt[max(0, i - 19): i + 1]) for i in range(mkt.size)])
    disp = np.nanstd(ret, axis=1)                                         # cross-sectional dispersion of the day
    tot = np.nansum(np.asarray(P["a_amt20"], np.float64), axis=1)
    tot60 = np.array([np.nanmean(tot[max(0, i - 59): i + 1]) for i in range(tot.size)])
    yrs = ps.years[us]
    reg = {f"年:{y}": yrs == y for y in sorted(set(yrs))}
    reg.update({"市场近20日:上涨": tr20[us] > 0, "市场近20日:下跌": tr20[us] <= 0,
                "市场波动:高于中位": vol20[us] > np.nanmedian(vol20[us]), "市场波动:低于中位": vol20[us] <= np.nanmedian(vol20[us]),
                "截面离散度:高": disp[us] > np.nanmedian(disp[us]), "截面离散度:低": disp[us] <= np.nanmedian(disp[us]),
                "成交:放量(高于60日均)": tot[us] > tot60[us], "成交:缩量": tot[us] <= tot60[us]})
    uni = np.isfinite(T)
    ew_all = np.where(uni.sum(1) > 0, np.nansum(np.where(uni, T, 0.0), 1) / np.maximum(uni.sum(1), 1), np.nan)
    out = {"factor_id": fid, "sweep": SW, "split": list(SPLITS["utrain"]), "signals": {}, "segments": {}, "ids": picked}
    for name, m in seg.items():
        mm = m & uni
        ew = np.where(mm.sum(1) > 0, np.nansum(np.where(mm, T, 0.0), 1) / np.maximum(mm.sum(1), 1), np.nan)
        out["segments"][name] = {"share": float(mm.sum() / max(uni.sum(), 1)), "ew_excess": ann(ew - ew_all)[0]}
    from alphacube.metrics import long_short_weights
    for k in picked:
        v = R[k]
        sm = bk.smoothed(v["sign"] * np.asarray(P[k], np.float64), v["hl_long_u"])[us]
        w = long_short_weights(sm, bk.TOP_FRAC)
        net, gross, turn = bk.long_book(w, sm, T)
        held = w > 0
        d = {"expr": v["expr"], "sign": v["sign"], "hl": v["hl_long_u"], "all": {"long_ann": ann(net)[0], "long_sharpe": ann(net)[1]},
             "seg": {}, "time": {}}
        for name, m in seg.items():
            s2 = np.where(m, sm, np.nan)
            r = bk.book_row(s2, T, slice(None))
            hs = float((held & m).sum() / max(held.sum(), 1))
            d["seg"][name] = {"in_long_ann": r["long_ann"], "in_long_sharpe": r["long_sharpe"], "held_share": hs,
                              "tilt": hs - out["segments"][name]["share"]}
        for name, dm in reg.items():
            a = ann(net[dm])
            d["time"][name] = {"long_ann": a[0], "long_sharpe": a[1], "days": int(dm.sum())}
        out["signals"][k] = d
    mem.stop()

p = PARTURA_ROOT / "runs" / fid / f"anatomy_{SW}.json"
p.write_text(json.dumps(out, ensure_ascii=False, indent=1, default=float), encoding="utf-8")


def f1(x):
    return "   — " if x is None or x != x else f"{x:+5.1%}"


cols = picked
print(f"\n== {fid} 市场解剖(用户训练段 {SPLITS['utrain'][0]}–{SPLITS['utrain'][1]};交易信号 = 方向×面板,多头口径半衰期)==")
for i, k in enumerate(cols):
    s = out["signals"][k]
    print(f"  [{i}] {k:20s} hl {s['hl']:>3g}  全市场多头净超额 {f1(s['all']['long_ann'])} 夏普 {s['all']['long_sharpe']:+.2f} | {s['expr'][:110]}")
print("\n-- 按股票范围:段内自建多头书的净超额(括号 = 全市场多头书在该段的持仓占比 − 该段占全市场的比例)")
print(f"{'段':26s} {'占比':>5s} {'段等权超额':>8s} | " + " | ".join(f"[{i}]".center(15) for i in range(len(cols))))
for name in seg:
    g = out["segments"][name]
    print(f"{name:26s} {g['share']:5.1%} {f1(g['ew_excess']):>8s} | " +
          " | ".join(f"{f1(out['signals'][k]['seg'][name]['in_long_ann'])} ({out['signals'][k]['seg'][name]['tilt']:+5.1%})" for k in cols))
print("\n-- 按时间 / 市场状态:全市场多头书的净超额(年化)")
print(f"{'时段':26s} {'天数':>5s} | " + " | ".join(f"[{i}]".center(7) for i in range(len(cols))))
for name in reg:
    print(f"{name:26s} {out['signals'][cols[0]]['time'][name]['days']:5d} | " +
          " | ".join(f"{f1(out['signals'][k]['time'][name]['long_ann']):>7s}" for k in cols))
print(f"\nwrote {p} ({time.time() - t0:.0f}s)")
