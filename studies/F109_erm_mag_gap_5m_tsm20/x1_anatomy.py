"""F109 x1: what the tree is really ranking -- the epsilon blow-up anatomy.

The tree is   gap_d = up_mean / (q95 + 1e-6) - dn_mean / (|q05| + 1e-6),   factor = nanmean_20d(gap_d)
with q95 / q05 the 95% / 5% quantile of the 1-MINUTE returns of the day and up_mean / dn_mean the mean
5-MINUTE return beyond those thresholds.  When fewer than ~5% of the minutes move up (down), q95 (q05)
is exactly 0 and that side of the ratio jumps from O(1) to O(1e2..1e4).  No stock diagnostic can say
how often that happens or who it is.  This script measures, on train / valid only:

  S0  did I read the tree right?  (rebuild the panel from its day-level parts; reproduce the S0 row)
  S1  what is `Ret` on the first bar of the day?  (overnight / open-to-close / NaN)
  S2  census: how often is a denominator exactly 0, how big is gap_d then, how many names have a
      blow-up day inside their 20-day window, and does one day dominate the 20-day mean?      (H1, H10)
  S3  who sits in each decile of the traded signal: blow-up regime in window, limit-lock days,
      unbuyable labels, price / size / turnover / vol ranks; event study of the window flags   (H2, H3, H5)
  S4  the short leg with and without the "could not be bought" filter                          (H3)
  S5  rebuilt variants, each tied to one hypothesis: floor the epsilon, drop / keep only the blow-up
      days, per-day rank, sides, counts, sigma-normalised gap, skew, event memory, windows    (H1 H2 H6 H8 H9)
  S6  neutralising the traded signal on event-type controls                                    (H2, H4)
  S7  first look at "does it add to the amount-level family for a long-only book"              (H9)

Only train / valid are read.  X1_FAKE=1 runs the whole thing on random arrays (shape / NaN shake-out).
"""
import os
import warnings

import numpy as np

from partura.study_tools import Study, bk, dg

warnings.simplefilter("ignore", RuntimeWarning)
np.set_printoptions(linewidth=200)
FID = "F109_erm_mag_gap_5m_tsm20"
FAKE = bool(os.environ.get("X1_FAKE"))

R5 = "sub(div(Close, in_delay(Close, 5)), create_like(Close, 1))"
Q95, Q05 = "day_quantile(Ret, 0.95)", "day_quantile(Ret, 0.05)"
E95, E05 = f"create_like({Q95}, 1e-06)", f"create_like({Q05}, 1e-06)"
UPC = f"add(day_sum(is_gt({R5}, {Q95})), {E95})"
DNC = f"add(day_sum(is_lt({R5}, {Q05})), {E05})"
UPM = f"div(day_sum(select_where(is_gt({R5}, {Q95}), {R5}, create_like(Close, 0))), {UPC})"
DNM = f"div(day_sum(select_where(is_lt({R5}, {Q05}), abs_({R5}), create_like(Close, 0))), {DNC})"
GAP = f"sub(div({UPM}, add({Q95}, {E95})), div({DNM}, add(abs_({Q05}), {E05})))"
BASE = f"ts_mean({GAP}, 20)"

EXPRS = {
    "base": BASE, "gap": GAP, "q95": Q95, "q05": Q05, "upm": UPM, "dnm": DNM, "upc": UPC, "dnc": DNC,
    "npos": f"add(day_sum(is_gt(Ret, create_like(Ret, 0))), {E95})",
    "nneg": f"add(day_sum(is_lt(Ret, create_like(Ret, 0))), {E05})",
    "skew": "day_skew(Ret)",
    "ret0": "day_first(Ret)", "c0": "day_first(Close)", "o0": "day_first(Open)",
    "cl": "day_last(Close)", "hi": "day_max(High)", "lo": "day_min(Low)",
}
CTLS = ["ctl_rev1", "ctl_amt", "ctl_price", "ctl_ivol", "ctl_dvol20", "ctl_mom20", "ctl_cap", "ctl_turnrate",
        "known_stdamt_mean30"]
THR = 1e-4            # a quantile below this is "degenerate" (a real tick return is >= ~1e-4 except for 100+ yuan names)
BIG = 20.0            # |gap_d| above this is a "blow-up day" (a regular day is O(1))


# ------------------------------------------------------------------ helpers (pure numpy; self-tested below)
def roll_sum(x, d):
    xf = np.where(np.isfinite(x), x, 0.0)
    cs = np.cumsum(xf, axis=0)
    out = cs.copy()
    out[d:] = cs[d:] - cs[:-d]
    return out


def roll_mean(x, d):
    n = roll_sum(np.isfinite(x).astype(np.float64), d)
    return np.where(n > 0, roll_sum(x, d) / np.maximum(n, 1), np.nan)


def roll_ext(x, d, fn=np.fmax):
    out = x.copy()
    for k in range(1, d):
        sh = np.full_like(x, np.nan)
        sh[k:] = x[:-k]
        out = fn(out, sh)
    return out


def pct(x):
    r = dg.rank_rows(np.asarray(x, dtype=np.float64))
    n = np.isfinite(r).sum(1, keepdims=True)
    return (r - 0.5) / np.maximum(n, 1)


def qs(x, ps=(0.1, 1, 5, 25, 50, 75, 95, 99, 99.9)):
    f = x[np.isfinite(x)]
    if f.size == 0:
        return "empty"
    return " ".join(f"p{p:g}={np.percentile(f, p):+.4g}" for p in ps)


def _selftest():
    rng = np.random.default_rng(0)
    x = rng.normal(size=(50, 7))
    x[rng.random(x.shape) < 0.1] = np.nan
    ref = np.full_like(x, np.nan)
    refmax = np.full_like(x, np.nan)
    for t in range(50):
        w = x[max(0, t - 4): t + 1]
        ok = np.isfinite(w)
        ref[t] = np.where(ok.sum(0) > 0, np.where(ok, w, 0).sum(0) / np.maximum(ok.sum(0), 1), np.nan)
        refmax[t] = np.where(ok.sum(0) > 0, np.where(ok, w, -np.inf).max(0), np.nan)
    assert np.allclose(roll_mean(x, 5), ref, equal_nan=True), "roll_mean"
    assert np.allclose(roll_ext(x, 5, np.fmax), refmax, equal_nan=True), "roll_ext"
    p = pct(np.array([[3.0, 1.0, np.nan, 2.0]]))
    assert np.allclose(p[0, [0, 1, 3]], [2.5 / 3, 0.5 / 3, 1.5 / 3]) and np.isnan(p[0, 2]), "pct"
    print("[selftest] roll_mean / roll_ext / pct ok", flush=True)


class FakeStudy:
    """Random arrays, so the script can be shaken out off-server."""
    def __init__(self):
        self.cfg = {"cost_per_side": 0.0015, "top_frac": 0.1, "rank_by": "long", "expression": BASE}
        self.D, self.S = 420, 300
        self.rng = np.random.default_rng(1)

    def __enter__(self):
        return self

    def __exit__(self, *a):
        pass

    def _r(self, scale=1.0, loc=0.0):
        x = self.rng.normal(loc, scale, size=(self.D, self.S)).astype(np.float32)
        x[self.rng.random(x.shape) < 0.03] = np.nan
        return x

    def panels(self, ex):
        out = {}
        for k in ex:
            if k == "q95":
                x = np.abs(self._r(1e-3)); x[self.rng.random(x.shape) < 0.1] = 0.0
            elif k == "q05":
                x = -np.abs(self._r(1e-3)); x[self.rng.random(x.shape) < 0.1] = 0.0
            elif k in ("upm", "dnm"):
                x = np.abs(self._r(3e-3))
            elif k in ("upc", "dnc", "npos", "nneg"):
                x = np.abs(self._r(30)) + 1e-6
            elif k in ("c0", "o0", "cl", "hi", "lo"):
                x = np.abs(self._r(1.0, 10.0)) + 1
            else:
                x = self._r()
            out[k] = x
        if "gap" in out and "upm" in out:
            out["gap"] = (out["upm"] / (out["q95"] + 1e-6) - out["dnm"] / (np.abs(out["q05"]) + 1e-6)).astype(np.float32)
            out["base"] = roll_mean(out["gap"].astype(np.float64), 20).astype(np.float32)
        return out

    def control(self, name):
        if name == "ctl_rev1":
            return (1 + self._r(0.03)).astype(np.float32)
        return self._r()

    def target(self, horizon=1, buyable=None):
        t = np.random.default_rng(7).normal(0, 0.02, size=(self.D, self.S))
        t[np.random.default_rng(6).random(t.shape) < 0.03] = np.nan
        if buyable is None or buyable:
            t[np.random.default_rng(8).random(t.shape) < 0.02] = np.nan
        return t

    def slice(self, split):
        return {"train": slice(0, 280), "valid": slice(280, 420)}[split]


def main():
    _selftest()
    with (FakeStudy() if FAKE else Study(FID)) as st:
        assert BASE == st.cfg["expression"], "my sub-strings do not rebuild the config expression"
        print("[check] the sub-strings rebuild the config expression exactly", flush=True)
        COST, TOP = float(st.cfg.get("cost_per_side", 0.0015)), float(st.cfg.get("top_frac", 0.10))
        P = {k: np.asarray(v, dtype=np.float64) for k, v in st.panels(EXPRS).items()}
        print("[panels] got", sorted(P), "missing", [k for k in EXPRS if k not in P], flush=True)
        C = {k: np.asarray(st.control(k), dtype=np.float64) for k in CTLS}
        tgt = np.asarray(st.target(), dtype=np.float64)
        raw = np.asarray(st.target(buyable=False), dtype=np.float64)
        tr, va = st.slice("train"), st.slice("valid")
        SPL = {"train": tr, "valid": va}
        TRK = {k: dg.rank_rows(tgt[s]) for k, s in SPL.items()}
        base, gap, q95, q05 = P["base"], P["gap"], P["q95"], P["q05"]
        upm, dnm, upc, dnc = P["upm"], P["dnm"], P["upc"], P["dnc"]
        D, S = base.shape
        print(f"[shape] {D} days x {S} names; train {tr}, valid {va}", flush=True)
        tv = slice(tr.start, va.stop)          # train + valid (never beyond)

        # ---------------------------------------------------------------- S0 reading check
        print("\n=== S0 读树自检 ===")
        upr = upm / (q95 + 1e-6)
        dnr = dnm / (np.abs(q05) + 1e-6)
        gap_np = upr - dnr
        both = np.isfinite(gap[tv]) & np.isfinite(gap_np[tv])
        rel = np.abs(gap[tv] - gap_np[tv])[both] / (1.0 + np.abs(gap[tv])[both])
        print(f"gap(引擎) vs up_ratio - dn_ratio(numpy): 共同有值 {both.mean():.4f}; 相对差 p50 {np.median(rel):.2e} p99 {np.percentile(rel, 99):.2e} max {rel.max():.2e}")
        rec = roll_mean(gap, 20)
        s2 = slice(tr.start + 25, va.stop)
        print(f"base vs nanmean20(gap): rank 相关 {dg.pair_rank_corr(base[s2], rec[s2]):+.4f}; "
              f"base 有值 {np.isfinite(base[tv]).mean():.4f}, 重构有值 {np.isfinite(rec[tv]).mean():.4f}", flush=True)
        REFR = {}

        def line(name, panel, sign=None, target=None, keep=False):
            t = tgt if target is None else target
            p = np.asarray(panel, dtype=np.float64)
            sg = dg.sign_from(p[tr], t[tr]) if sign is None else sign
            b = bk.books(sg * p, t, tr, SPL, cost=COST, top_frac=TOP, rank_by="long")
            L, Sv = b["by_rank"]["long"], b["by_rank"]["ls"]
            lt, lv, st_, sv_ = L["splits"]["train"], L["splits"]["valid"], Sv["splits"]["train"], Sv["splits"]["valid"]
            ric = [dg.nanmean_quiet(dg.cs_pearson(sg * dg.rank_rows(p[s]), TRK[k])) if target is None else
                   dg.nanmean_quiet(dg.rank_ic_series(sg * p[s], t[s])) for k, s in SPL.items()]
            sm = bk.smoothed(sg * p, L["hl"])
            smr = dg.rank_rows(sm[tr])
            cb = dg.nanmean_quiet(dg.cs_pearson(smr, REFR["base"])) if "base" in REFR else float("nan")
            ck = dg.nanmean_quiet(dg.cs_pearson(smr, REFR["known"])) if "known" in REFR else float("nan")
            cov = (np.isfinite(p[tr]) & np.isfinite(t[tr])).sum() / max(int(np.isfinite(t[tr]).sum()), 1)
            dist = dg.distinct_fraction(p[tr])
            print(f"{name:<24}{'+' if sg > 0 else '-'} | hlL {L['hl']:>4g} Lnet {lt['long_ann']*100:+6.1f}% {lv['long_ann']*100:+6.1f}% "
                  f"Lshp {lt['long_sharpe']:+5.2f} {lv['long_sharpe']:+5.2f} Lgross {lt['long_gross_ann']*100:+6.1f}% {lv['long_gross_ann']*100:+6.1f}% "
                  f"LTO {lt['long_turnover']*100:4.1f}% | hlS {Sv['hl']:>4g} LS {st_['ls_sharpe']:+5.2f} {sv_['ls_sharpe']:+5.2f} "
                  f"short {st_['short_gross_ann']*100:+6.1f}% {sv_['short_gross_ann']*100:+6.1f}% | rIC {ric[0]:+.4f} {ric[1]:+.4f} "
                  f"| r(base) {cb:+.2f} r(known) {ck:+.2f} | cov {cov:.2f} dist {dist:.2f}", flush=True)
            out = {"sign": sg, "hlL": L["hl"], "hlS": Sv["hl"], "smr": smr}
            if keep:
                out["sm"] = sm
            return out

        print("\n列: 名称 方向 | 多头口径半衰期 多头腿净超额 tr va 纯多头夏普 tr va 多头腿毛超额 tr va 多头日换手 | 多空口径半衰期 多空夏普 tr va "
              "空头腿毛超额 tr va | 原始面板 rank IC tr va | 与原式/已知家族的 rank 相关(多头口径信号, train) | cov dist")
        b0 = line("base(引擎)", base, keep=True)
        known = C["known_stdamt_mean30"]
        k0 = line("known_stdamt_mean30", known)
        REFR.update({"base": b0["smr"], "known": k0["smr"]})
        line("base 重构", rec)

        # ---------------------------------------------------------------- S1 first bar of Ret
        print("\n=== S1 `Ret` 的第一根 ===")
        if all(k in P for k in ("ret0", "c0", "o0", "cl")):
            ret0, c0, o0, cl = P["ret0"], P["c0"], P["o0"], P["cl"]
            pc = np.full_like(cl, np.nan)
            pc[1:] = cl[:-1]
            a = ret0[tv]
            print(f"day_first(Ret): 有值 {np.isfinite(a).mean():.4f}  恰为 0 的比例 {(a == 0).sum() / max(np.isfinite(a).sum(), 1):.4f}  {qs(a, (1, 25, 50, 75, 99))}")
            for nm, ref_ in (("首根收盘/昨收-1(含隔夜)", c0 / pc - 1.0), ("首根收盘/首根开盘-1", c0 / o0 - 1.0)):
                d = np.abs(a - ref_[tv])
                d = d[np.isfinite(d)]
                if d.size:
                    print(f"  |day_first(Ret) - {nm}|: p50 {np.median(d):.2e} p90 {np.percentile(d, 90):.2e}  (越接近 0 越说明就是它)")
        else:
            print("  (缺面板,跳过)")

        # ---------------------------------------------------------------- S2 census
        print("\n=== S2 分母爆炸的普查(train+valid 的股票-日)===")
        g = gap[tv]
        fin = np.isfinite(g)
        z95 = (q95 < THR) & np.isfinite(q95)
        z05 = (q05 > -THR) & np.isfinite(q05)
        regd = (q95 >= THR) & (q05 <= -THR)
        n = fin.sum()
        print(f"有值的股票-日 {n:,}(占 {fin.mean():.4f})")
        print(f"q95 的分布: {qs(q95[tv])}")
        print(f"q05 的分布: {qs(q05[tv])}")
        for nm, m in (("q95 == 0", np.abs(q95) < 1e-9), ("q05 == 0", np.abs(q05) < 1e-9), ("两个都 == 0", (np.abs(q95) < 1e-9) & (np.abs(q05) < 1e-9)),
                      ("0 < q95 < 1e-5", (q95 > 1e-9) & (q95 < 1e-5)), ("1e-5 <= q95 < 1e-4", (q95 >= 1e-5) & (q95 < 1e-4)),
                      ("1e-4 <= q95 < 3e-4", (q95 >= 1e-4) & (q95 < 3e-4)),
                      ("0 < |q05| < 1e-5", (q05 < -1e-9) & (q05 > -1e-5)), ("1e-5 <= |q05| < 1e-4", (q05 <= -1e-5) & (q05 > -1e-4)),
                      ("q95 < 0", q95 < -1e-9), ("q05 > 0", q05 > 1e-9),
                      (f"退化: q95 < {THR:g}", z95), (f"退化: |q05| < {THR:g}", z05), ("两侧都退化", z95 & z05),
                      ("只有上侧退化", z95 & ~z05), ("只有下侧退化", z05 & ~z95)):
            print(f"  {nm:<22} {(m[tv] & fin).sum() / n:.4f}")
        for thr in (5, 20, 100, 1000, 10000):
            print(f"  |gap_d| > {thr:<6} {(np.abs(g) > thr).sum() / n:.4f}   其中为正的占 {((g > thr).sum() / max((np.abs(g) > thr).sum(), 1)):.3f}")
        print(f"  规则日里 |gap_d| > {BIG:g} 的比例 {(np.abs(g) > BIG)[regd[tv] & fin].mean():.5f};退化日里 |gap_d| > {BIG:g} 的比例 {(np.abs(g) > BIG)[(z95 | z05)[tv] & fin].mean():.4f}")
        print(f"gap_d 全体: {qs(g)}")
        print(f"gap_d 规则日: {qs(g[regd[tv] & fin])}")
        print(f"up_ratio 规则日: {qs(upr[tv][regd[tv] & fin], (1, 25, 50, 75, 99))}")
        print(f"dn_ratio 规则日: {qs(dnr[tv][regd[tv] & fin], (1, 25, 50, 75, 99))}")
        for nm, m in (("只有上侧退化", z95 & ~z05), ("只有下侧退化", z05 & ~z95), ("两侧都退化", z95 & z05)):
            mm = m[tv] & fin
            if mm.sum():
                print(f"gap_d [{nm}]: 为正的占 {(g[mm] > 0).mean():.3f}; {qs(g[mm], (1, 25, 50, 75, 99))}")
        print(f"超过阈值的分钟数(+1e-6): up {qs(upc[tv], (1, 25, 50, 75, 99))} | dn {qs(dnc[tv], (1, 25, 50, 75, 99))}")
        print(f"  一次都没超过(计数 < 0.5)的股票-日: up {(upc[tv] < 0.5).sum() / n:.4f}  dn {(dnc[tv] < 0.5).sum() / n:.4f}  (H10: 计数上的 1e-6 只在这些日子起作用)")
        npos, nneg = P.get("npos"), P.get("nneg")
        if npos is not None and nneg is not None:
            print(f"上涨分钟数: {qs(npos[tv], (1, 5, 25, 50, 75, 99))} | 下跌分钟数: {qs(nneg[tv], (1, 5, 25, 50, 75, 99))}")
        blow = np.abs(gap) > BIG
        gfin = np.isfinite(gap)
        wpos = roll_sum(gfin & (gap > BIG), 20) > 0
        wneg = roll_sum(gfin & (gap < -BIG), 20) > 0
        wblow = wpos | wneg
        fb_ = np.isfinite(base)
        print(f"20 日窗口里至少有一个爆炸日(|gap_d| > {BIG:g})的股票-日: {(wblow[tv] & fb_[tv]).sum() / fb_[tv].sum():.4f}"
              f"(有正爆炸 {(wpos[tv] & fb_[tv]).sum() / fb_[tv].sum():.4f}, 有负爆炸 {(wneg[tv] & fb_[tv]).sum() / fb_[tv].sum():.4f})")
        amax = roll_ext(np.abs(gap), 20, np.fmax)
        asum = roll_sum(np.abs(gap), 20)
        dom = (amax / np.maximum(asum, 1e-12))[tv]
        print(f"窗口内最大一天占 Σ|gap_d| 的比例: 有爆炸日的窗口 {qs(dom[wblow[tv] & fb_[tv]], (5, 25, 50, 75))} | 没有的 {qs(dom[~wblow[tv] & fb_[tv]], (5, 25, 50, 75))}")
        del amax, asum, dom
        print(f"|base| 的分布: {qs(np.abs(base[tv]), (10, 25, 50, 75, 90, 99))}")
        rev1 = C["ctl_rev1"]
        lockup = z95 & z05 & (rev1 >= 1.04)
        lockdn = z95 & z05 & (rev1 <= 0.96)
        bigup, bigdn = rev1 >= 1.095, rev1 <= 0.905
        for nm, m in (("封涨停型(两侧退化且当日涨幅≥4%)", lockup), ("封跌停型(两侧退化且当日跌幅≥4%)", lockdn),
                      ("当日涨幅 ≥ 9.5%", bigup), ("当日跌幅 ≥ 9.5%", bigdn)):
            mm = m[tv] & fin
            if mm.sum():
                print(f"  {nm:<30} 占全部股票-日 {mm.sum() / n:.4f}; 其中 |gap_d| > {BIG:g} 的占 {(np.abs(g[mm]) > BIG).mean():.3f}, gap_d 中位数 {np.median(g[mm]):+.4g}")
        bl = blow[tv] & fin
        msg = (f"爆炸日里: 封涨停型 {(lockup[tv] & bl).sum() / bl.sum():.3f} 封跌停型 {(lockdn[tv] & bl).sum() / bl.sum():.3f} "
               f"当日涨幅≥9.5% {(bigup[tv] & bl).sum() / bl.sum():.3f} 当日跌幅≥9.5% {(bigdn[tv] & bl).sum() / bl.sum():.3f}")
        if all(k in P for k in ("cl", "hi", "lo")):
            athigh, atlow = np.abs(P["cl"] - P["hi"]) < 1e-6, np.abs(P["cl"] - P["lo"]) < 1e-6
            msg += f" 收在最高 {(athigh[tv] & bl).sum() / bl.sum():.3f} 收在最低 {(atlow[tv] & bl).sum() / bl.sum():.3f}"
        print(msg)
        PR = {k: pct(C[k]) for k in ("ctl_price", "ctl_cap", "ctl_amt", "ctl_turnrate", "ctl_ivol", "ctl_dvol20", "ctl_mom20")}
        for nm, m in (("规则日", regd & gfin), ("爆炸日 gap>20", gap > BIG), ("爆炸日 gap<-20", gap < -BIG),
                      ("非封板爆炸 gap>20", (gap > BIG) & ~lockup & ~lockdn), ("非封板爆炸 gap<-20", (gap < -BIG) & ~lockup & ~lockdn),
                      ("封涨停型", lockup & gfin), ("封跌停型", lockdn & gfin)):
            mm = m[tv]
            if mm.sum():
                print(f"  [{nm:<16}] 占 {mm.sum() / n:.4f} 平均分位: " + " ".join(f"{k[4:]} {np.nanmean(PR[k][tv][mm]):.2f}" for k in PR)
                      + f" | 当日收益中位数 {np.nanmedian(rev1[tv][mm]) - 1:+.4f}")

        # ---------------------------------------------------------------- S3 decile anatomy
        print("\n=== S3 十分位画像(实际交易的信号;Q1 = 空头端, Q10 = 多头端)===", flush=True)
        W = {"窗内有正爆炸": wpos, "窗内有负爆炸": wneg,
             "窗内有封涨停": roll_sum(lockup, 20) > 0, "窗内有封跌停": roll_sum(lockdn, 20) > 0,
             "窗内有≥9.5%大涨": roll_sum(bigup, 20) > 0, "窗内有≥9.5%大跌": roll_sum(bigdn, 20) > 0,
             "窗内无爆炸": ~wblow}
        unbuy = np.isfinite(raw) & ~np.isfinite(tgt)

        def anatomy(tag, sm, days, full=True):
            s = sm[days]
            ok = np.isfinite(s) & np.isfinite(raw[days])
            order = np.argsort(np.where(ok, s, np.inf), axis=1, kind="stable")
            cnt = ok.sum(1)
            pos = np.empty_like(order)
            np.put_along_axis(pos, order, np.arange(s.shape[1])[None, :].repeat(s.shape[0], 0), axis=1)
            q = np.where(ok, np.floor(pos / np.maximum(cnt, 1)[:, None] * 10), np.nan)
            prof_b = bk.quantile_profile(sm, tgt, days, n=10)
            prof_r = bk.quantile_profile(sm, raw, days, n=10)
            print(f"-- {tag}")
            print(" " * 18 + " ".join(f"{'Q' + str(k + 1):>7}" for k in range(10)))
            print(f"{'超额(可买入标签)%':<12}" + " ".join(f"{r['excess_ann'] * 100:+7.1f}" for r in prof_b))
            print(f"{'超额(原始标签)%':<13}" + " ".join(f"{r['excess_ann'] * 100:+7.1f}" for r in prof_r))
            rows = [("买不进占比%", unbuy)] + [(k + "%", v) for k, v in W.items()]
            for nm, f in rows:
                fd = f[days]
                print(f"{nm:<14}" + " ".join(f"{100 * (fd & (q == k)).sum() / max((q == k).sum(), 1):7.1f}" for k in range(10)))
            if full:
                for k_, v in PR.items():
                    vd = v[days]
                    print(f"{k_[4:] + ' 分位':<14}" + " ".join(f"{np.nanmean(vd[q == k]):7.2f}" for k in range(10)))
                bd = base[days]
                print(f"{'base 中位数':<14}" + " ".join(f"{np.nanmedian(bd[q == k]):+7.3g}" for k in range(10)))
            print("", flush=True)

        sm_long = b0["sm"]                                   # hl fitted for the long book
        sm_ls = bk.smoothed(b0["sign"] * base, b0["hlS"])    # hl fitted for the L/S book
        anatomy(f"train, 多头口径 hl {b0['hlL']:g}", sm_long, tr)
        anatomy(f"valid, 多头口径 hl {b0['hlL']:g}", sm_long, va)
        anatomy(f"train, 多空口径 hl {b0['hlS']:g}", sm_ls, tr)
        anatomy(f"valid, 多空口径 hl {b0['hlS']:g}", sm_ls, va, full=False)
        for k, s in SPL.items():
            pr_ = bk.quantile_profile(sm_long, tgt, s, n=20)
            print(f"base 20 分位剖面 [{k}, 多头口径] " + " ".join(f"{r['excess_ann'] * 100:+.0f}" for r in pr_))
        print("全市场基准率(train): " + " ".join(f"{k} {100 * (v[tr] & fb_[tr]).sum() / fb_[tr].sum():.1f}%" for k, v in W.items())
              + f" 买不进 {100 * unbuy[tr].sum() / np.isfinite(raw[tr]).sum():.2f}%")
        print("-- 事件研究: 窗口旗标下的股票次日超额(年化%, 相对同日有信号有标签的等权) [train 可买入 | train 原始 | valid 可买入 | valid 原始], 平均只数占比")
        for k, f in W.items():
            cells = []
            for s in (tr, va):
                for t in (tgt, raw):
                    ok = fb_[s] & np.isfinite(t[s])
                    r = np.where(ok, t[s], 0.0)
                    ew = r.sum(1) / np.maximum(ok.sum(1), 1)
                    sel = f[s] & ok
                    m = sel.sum(1)
                    ex = np.where(m > 0, (r * sel).sum(1) / np.maximum(m, 1) - ew, np.nan)
                    cells.append(f"{np.nanmean(ex) * 252 * 100:+6.1f}")
            print(f"  {k:<14} " + " | ".join(cells) + f"   占比 {100 * (f[tr] & fb_[tr]).sum() / fb_[tr].sum():.1f}%", flush=True)

        # ---------------------------------------------------------------- S4 unbuyable inflation
        print("\n=== S4 空头腿里有多少是「买不进」撑的(同一信号,换成不带过滤的标签)===")
        line("base / 可买入标签", base, sign=b0["sign"])
        line("base / 原始标签", base, sign=b0["sign"], target=raw)

        # ---------------------------------------------------------------- S5 rebuilt variants
        print("\n=== S5 重构变体(numpy;方向与半衰期都在 train 上定)===", flush=True)
        ivol = C["ctl_ivol"]

        def gap_eps(e):
            return upm / (q95 + e) - dnm / (np.abs(q05) + e)

        gap_reg = np.where(regd, gap, np.nan)
        skew = P.get("skew")
        V = [
            ("H1 eps=1e-5", lambda: roll_mean(gap_eps(1e-5), 20)),
            ("H1 eps=1e-4", lambda: roll_mean(gap_eps(1e-4), 20)),
            ("H1 eps=1e-3", lambda: roll_mean(gap_eps(1e-3), 20)),
            ("H1 去掉退化日", lambda: roll_mean(gap_reg, 20)),
            ("H1 逐日截尾±5", lambda: roll_mean(np.clip(gap, -5, 5), 20)),
            ("H1 逐日截面秩", lambda: roll_mean(pct(gap) - 0.5, 20)),
            ("H1 只留符号", lambda: roll_mean(np.sign(gap), 20)),
            ("H1 只留爆炸日", lambda: roll_mean(np.where(gfin, np.where(blow, gap, 0.0), np.nan), 20)),
            ("H1 sign*log1p", lambda: roll_mean(np.sign(gap) * np.log1p(np.abs(gap)), 20)),
            ("H8 max20+min20", lambda: roll_ext(gap, 20, np.fmax) + roll_ext(gap, 20, np.fmin)),
            ("H2 20日最大涨幅", lambda: roll_ext(rev1, 20, np.fmax)),
            ("H2 20日最小涨幅", lambda: roll_ext(rev1, 20, np.fmin)),
            ("H2 上侧退化-下侧退化 天数", lambda: roll_mean(np.where(gfin, z95.astype(float) - z05.astype(float), np.nan), 20)),
            ("H2 退化天数", lambda: roll_mean(np.where(gfin, (z95 | z05).astype(float), np.nan), 20)),
            ("侧 up_ratio 原", lambda: roll_mean(upr, 20)),
            ("侧 dn_ratio 原", lambda: roll_mean(dnr, 20)),
            ("侧 up_ratio 规则", lambda: roll_mean(np.where(regd, upr, np.nan), 20)),
            ("侧 dn_ratio 规则", lambda: roll_mean(np.where(regd, dnr, np.nan), 20)),
            ("侧 up+dn 规则", lambda: roll_mean(np.where(regd, upr + dnr, np.nan), 20)),
            ("计数 up-dn", lambda: roll_mean((upc - dnc) / 236.0, 20)),
            ("计数 up+dn", lambda: roll_mean((upc + dnc) / 236.0, 20)),
            ("σ归一 (upm-dnm)/σ", lambda: roll_mean(np.where(ivol > 0, (upm - dnm) / ivol, np.nan), 20)),
            ("差 (upm-q95)-(dnm-|q05|)", lambda: roll_mean((upm - q95) - (dnm - np.abs(q05)), 20)),
            ("折叠 -|pct(base)-.5|", lambda: -np.abs(pct(base) - 0.5)),
            ("折叠 -|pct(规则)-.5|", lambda: -np.abs(pct(roll_mean(gap_reg, 20)) - 0.5)),
        ]
        if skew is not None:
            V.append(("H6 day_skew 20日", lambda: roll_mean(skew, 20)))
        if npos is not None and nneg is not None:
            V.append(("活跃度 (npos+nneg)/241", lambda: roll_mean((npos + nneg) / 241.0, 20)))
            V.append(("方向 (npos-nneg)/(·+1)", lambda: roll_mean((npos - nneg) / (npos + nneg + 1.0), 20)))
        for d in (5, 10, 40, 60):
            V.append((f"H8 原式窗口 {d}", lambda d=d: roll_mean(gap, d)))
        for d in (5, 10, 40, 60):
            V.append((f"H8 去退化 窗口 {d}", lambda d=d: roll_mean(gap_reg, d)))
        KEEP = {"H1 去掉退化日", "H1 只留爆炸日", "H1 eps=1e-3", "H1 逐日截面秩", "H6 day_skew 20日", "H2 20日最大涨幅",
                "H2 上侧退化-下侧退化 天数", "σ归一 (upm-dnm)/σ", "计数 up-dn"}
        OUT, VP = {}, {}
        for nm, fn in V:
            try:
                p = fn()
                OUT[nm] = line(nm, p, keep=nm in KEEP)
                if nm in KEEP:
                    VP[nm] = p
                del p
            except Exception as exc:                       # one broken variant must not cost the run
                print(f"{nm:<24} FAILED {type(exc).__name__}: {exc}", flush=True)

        print("\n-- 关键面板之间的 rank 相关(原始日频面板, train)")
        M = {"base": base, **VP, "turnrate": C["ctl_turnrate"], "dvol20": C["ctl_dvol20"], "price": C["ctl_price"],
             "cap": C["ctl_cap"], "known30": known}
        rk = {k: dg.rank_rows(v[tr]) for k, v in M.items()}
        names = list(M)
        print(" " * 26 + " ".join(f"{k[:8]:>8}" for k in names))
        for a_ in names:
            print(f"{a_[:26]:<26}" + " ".join(f"{dg.nanmean_quiet(dg.cs_pearson(rk[a_], rk[b_])):+8.2f}" for b_ in names), flush=True)
        del rk

        print("\n-- 分位剖面(各自的多头口径信号; Q10 = 多头端)")
        for nm in KEEP:
            if nm in OUT and "sm" in OUT[nm]:
                for k, s in SPL.items():
                    pr_ = bk.quantile_profile(OUT[nm]["sm"], tgt, s, n=10)
                    print(f"{nm:<24}[{k}] " + " ".join(f"{r['excess_ann'] * 100:+6.1f}" for r in pr_), flush=True)

        # ---------------------------------------------------------------- S6 neutralise on event controls
        print("\n=== S6 实际交易信号(多头口径)对事件型控制取秩残差(train) ===", flush=True)
        EV = {"20日最大涨幅": roll_ext(rev1, 20, np.fmax), "20日最小涨幅": roll_ext(rev1, 20, np.fmin),
              "上侧退化天数": roll_mean(np.where(gfin, z95.astype(float), np.nan), 20),
              "下侧退化天数": roll_mean(np.where(gfin, z05.astype(float), np.nan), 20),
              "turnrate": C["ctl_turnrate"], "dvol20": C["ctl_dvol20"], "price": C["ctl_price"], "cap": C["ctl_cap"]}
        sets = {"20日最大涨幅": ["20日最大涨幅"], "上/下侧退化天数": ["上侧退化天数", "下侧退化天数"], "turnrate": ["turnrate"],
                "最大/最小涨幅+退化天数": ["20日最大涨幅", "20日最小涨幅", "上侧退化天数", "下侧退化天数"],
                "全部事件型+turnrate+dvol20+price+cap": list(EV)}
        sig = b0["sm"]

        def resid_row(nm, res, r2):
            full = np.full_like(sig, np.nan)
            full[tr] = res
            ric = dg.nanmean_quiet(dg.rank_ic_series(res, tgt[tr]))
            br = bk.book_row(full, tgt, tr, COST, TOP)
            print(f"  [{nm}] R2 {r2:.3f} 残差 rIC {ric:+.4f} Lgross {br['long_gross_ann'] * 100:+.1f}% Lnet {br['long_ann'] * 100:+.1f}% "
                  f"short {br['short_gross_ann'] * 100:+.1f}% LSgross {br['ls_gross_sharpe']:+.2f} LS {br['ls_sharpe']:+.2f} TO {br['ls_turnover'] * 100:.1f}%", flush=True)

        resid_row("未中性化", sig[tr], 0.0)
        for nm, ks in sets.items():
            res, info = dg.neutralise(sig[tr], {k: EV[k][tr] for k in ks}, space="rank")
            resid_row(nm, res, info["mean_r2"])
        del EV

        # ---------------------------------------------------------------- S7 increment over the known family (first look)
        print("\n=== S7 对只能做多的人:与已知家族秩相加(权重 w 加在候选上;第一行是已知家族自己)===", flush=True)
        ks = pct(k0["sign"] * known)
        line("known 自己(秩)", ks, sign=1.0)
        for nm, p_, sg_ in (("base", base, b0["sign"]),) + tuple((k, VP[k], OUT[k]["sign"]) for k in
                                                               ("H1 去掉退化日", "H1 只留爆炸日", "H1 eps=1e-3", "H1 逐日截面秩") if k in VP):
            cs_ = pct(sg_ * p_)
            for w in (0.3, 1.0):
                line(f"known+{w:g}*{nm}"[:24], ks + w * cs_, sign=1.0)
        print("\n[done]", flush=True)


if __name__ == "__main__":
    main()
