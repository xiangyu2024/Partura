"""x2 -- the section x1 lost to the memory guard: does F108 give a pure-long user
anything ON TOP of the known turnover-level family (order R1).

Reuses x1's already-computed panels only (base, jmax) and the config's existing
controls/gates -- no new NT-face expression.  Only train / valid are read.

  0.  utrain @ fixed half-life 10 (vs the published +5.6%); the two LTO readings
      R0 found in two different tables (quoted from notes, not re-derived)
  A1. the known family alone (K1 = known_stdamt_mean30, K2 = known_stdamt_max9) --
      the baseline every combination below must beat
  A2. removal screens on the family's long pool (quintile/decile), vs a
      SAME-SIZE family-only control (the core measurement of this order)
  A3. rank-space asymmetric overlay  rk + w * rD**p
  A4. neutralisation, both directions (D on K, and K on D_m30)
  B1. H14 -- one-sided exclusion vs full decile ranking vs the equal-weight
      universe (ladder of 03/05/10/20%)
  B2. H9 -- within-bucket ranking using language-available proxies for size
  C.  same-tail comparison: F108's alert vs each control's own tail, matched
      by day-count, not by threshold
"""
import gc
import warnings

import numpy as np

warnings.filterwarnings("ignore")

from partura.study_tools import Study, bk, dg  # noqa: E402

FID = "F108_max_ntkurt_close"
K_EXPR = "nt_ts_kurt(Close, 30)"
EX = {
    "base": f"day_max(pow_1_5(pow_2({K_EXPR})))",
    "jmax": "day_max(abs_(Ret))",
}
CTL = ["ctl_amt", "ctl_price", "ctl_cap", "ctl_ivol", "ctl_dvol20", "ctl_turnrate",
       "known_stdamt_mean30", "known_stdamt_max9", "known_ivol_max9"]
COST = 0.0015


# ============================================================ copied verbatim from x1_anatomy.py
def hdr(s):
    print("\n" + "=" * 8 + " " + s + " " + "=" * 8, flush=True)


def pct_rank(a):
    r = dg.rank_rows(np.asarray(a, dtype=np.float64))
    n = np.isfinite(r).sum(1, keepdims=True)
    return (r - 0.5) / np.maximum(n, 1)


def bucket(pr, n):
    return np.where(np.isfinite(pr), np.minimum(np.floor(pr * n), n - 1), np.nan)


def excess(t, universe):
    """label minus the equal-weight mean of the labelled cells of `universe` (NaN elsewhere)."""
    r = np.where(universe & np.isfinite(t), t, np.nan)
    return r - np.nanmean(r, axis=1, keepdims=True)


def cell_ann(ex, sel):
    """annualised mean (%) of the daily equal-weight excess of the cells in sel; mean names a day."""
    sel = sel & np.isfinite(ex)
    m = sel.sum(1)
    daily = np.where(m > 0, np.where(sel, ex, 0.0).sum(1) / np.maximum(m, 1), np.nan)
    return float(np.nanmean(daily) * 252 * 100), float(m.mean())


def roll_mean(x, d):
    x = np.asarray(x, dtype=np.float64)
    fin = np.isfinite(x)
    cs = np.cumsum(np.where(fin, x, 0.0), axis=0)
    cn = np.cumsum(fin, axis=0).astype(np.float64)
    s, n = cs.copy(), cn.copy()
    s[d:] -= cs[:-d]
    n[d:] -= cn[:-d]
    return np.where(n > 0, s / np.maximum(n, 1), np.nan)


def book_line(st, name, panel, sign=None):
    b = st.books(panel, fit="train", evals=("train", "valid"), sign=sign)
    lo, ls = b["by_rank"]["long"], b["by_rank"]["ls"]
    tr, va = lo["splits"]["train"], lo["splits"]["valid"]
    str_, sva = ls["splits"]["train"], ls["splits"]["valid"]
    sg = st.sign(panel, "train") if sign is None else sign
    print(f"{name:<24} sgn {sg:+.0f} | hlL {lo['hl']:>3g}  Lnet {tr['long_ann'] * 100:+6.1f}%/{va['long_ann'] * 100:+6.1f}%  "
          f"Lshp {tr['long_sharpe']:+5.2f}/{va['long_sharpe']:+5.2f}  Lgross {tr['long_gross_ann'] * 100:+6.1f}%/"
          f"{va['long_gross_ann'] * 100:+6.1f}%  LTO {tr['long_turnover'] * 100:4.1f}% | hlS {ls['hl']:>3g}  "
          f"LS {str_['ls_sharpe']:+5.2f}/{sva['ls_sharpe']:+5.2f}  short {str_['short_gross_ann'] * 100:+6.1f}%/"
          f"{sva['short_gross_ann'] * 100:+6.1f}%", flush=True)
    return b


def fixed_line(st, name, panel, tgt, tr, va, sign, hls=(0, 5, 20)):
    p = sign * np.asarray(panel, dtype=np.float64)
    bits = []
    for hl in hls:
        sm = bk.smoothed(p, hl)
        a, b = bk.book_row(sm, tgt, tr), bk.book_row(sm, tgt, va)
        bits.append(f"hl{hl:<2} Lnet {a['long_ann'] * 100:+6.1f}%/{b['long_ann'] * 100:+6.1f}% Lgross "
                    f"{a['long_gross_ann'] * 100:+5.1f}%/{b['long_gross_ann'] * 100:+5.1f}% LTO {a['long_turnover'] * 100:4.1f}%")
    print(f"{name:<24} " + "  |  ".join(bits), flush=True)


def safe(fn, label):
    try:
        fn()
    except Exception as exc:                                    # one broken section must not waste the run
        import traceback
        print(f"[section {label} FAILED] {type(exc).__name__}: {exc}", flush=True)
        traceback.print_exc()


# ============================================================ new for x2
def mem_mark(label):
    try:
        from partura import guard
        print(f"[mem] {label}: process anon ~ {guard.self_anon_gb():.2f} GiB", flush=True)
    except Exception:
        pass


def screened_book(held, ok, target, cost=COST):
    """Pure long book of an equal-weight basket (`held`, bool, per day), excess
    vs the equal-weight return of every `ok` (available & labelled) name that
    day.  Built by handing partura.books.long_book exactly the weight vector it
    expects, so the cost/turnover convention is identical to every other book
    in this report.  Returns (net, gross, one-sided turnover, n_held/day)."""
    held = held & ok
    n = held.sum(1).astype(np.float64)
    w_half = np.where(held, 0.5 / np.maximum(n, 1)[:, None], 0.0)   # clip(.,0,None)*2 -> 1/n for held
    sig_dummy = np.where(ok, 1.0, np.nan)                       # only its isfinite pattern is used
    net, gross, turn = bk.long_book(w_half, sig_dummy, target, cost)
    return net, gross, turn, n


def layered_pct_rank(x_masked, bucket_id, nbuckets):
    """percentile rank of x WITHIN each day's bucket group (0..nbuckets-1); x_masked
    should already be NaN outside the universe the caller wants ranked."""
    out = np.full(x_masked.shape, np.nan)
    for q in range(nbuckets):
        m = bucket_id == q
        pr = pct_rank(np.where(m, x_masked, np.nan))
        out = np.where(m, pr, out)
    return out


def book_stats_row(net, gross, turn, n):
    ln, lg = bk.stats(net), bk.stats(gross)
    return {"Lnet": ln["ann"] * 100, "Lgross": lg["ann"] * 100, "Lshp": ln["sharpe"],
            "LTO": float(np.nanmean(turn)) * 100, "N": float(np.nanmean(n))}


def fmt_row(r):
    return f"Lnet {r['Lnet']:+6.1f}% Lgross {r['Lgross']:+6.1f}% Lshp {r['Lshp']:+5.2f} LTO {r['LTO']:4.1f}% N {r['N']:5.0f}"


def main(st):
    mem_mark("start")
    P = st.panels(EX)
    missing = [k for k in EX if k not in P]
    if missing:
        print("MISSING panels:", missing, flush=True)
    C = {}
    for k in CTL:
        try:
            C[k] = st.control(k)
        except Exception as exc:
            print(f"control {k} unavailable: {exc}", flush=True)
    tr, va = st.slice("train"), st.slice("valid")
    tgt = st.target()
    splits = (("train", tr), ("valid", va))
    mem_mark("after panels+controls")

    base64 = np.asarray(P["base"], dtype=np.float64)
    r_full = np.cbrt(base64)
    sgn = st.sign(P["base"], "train")
    K1 = np.asarray(C["known_stdamt_mean30"], dtype=np.float64) if "known_stdamt_mean30" in C else None
    K2 = np.asarray(C["known_stdamt_max9"], dtype=np.float64) if "known_stdamt_max9" in C else None

    D_ema20 = st.signal(P["base"], sign=sgn, halflife=20.0)         # sign*base EMA'd at hl20; high = good
    m30 = roll_mean(base64, 30)
    D_m30 = sgn * m30                                               # high = good, same scale convention
    del m30
    jmax64 = np.asarray(P["jmax"], dtype=np.float64) if "jmax" in P else None
    gc.collect()
    mem_mark("after setup (base/r/D_ema20/D_m30/K1/K2/jmax)")

    STATE = {}

    # ------------------------------------------------------------ self-check
    def self_check():
        hdr("self-check against already-established numbers (S0 / x1)")
        print("expect: base sgn -1 hlL 20 Lnet +0.3%/+2.5% Lshp +0.05/+0.46 LTO 4.7% | hlS 5 LS +2.83/+2.53")
        book_line(st, "base", P["base"])
        if K1 is not None:
            print("expect (x1 S9b): known_stdamt_mean30 alone sgn -1 hlL 0 Lnet +12.6%/+22.3% Lshp +1.78/+3.46 LTO 3.4%")
            book_line(st, "K1 alone (selfcheck)", K1)
        print(f"sign(base, train) = {sgn:+.0f} (expect -1)")
    safe(self_check, "selfcheck")
    mem_mark("after selfcheck")

    # ------------------------------------------------------------ 0
    def s0():
        hdr("0. utrain @ fixed half-life 10; and the two LTO readings R0 found")
        utr = st.slice("utrain")
        sm10 = bk.smoothed(sgn * base64, 10.0)
        row = bk.book_row(sm10, tgt, utr)
        print(f"utrain, sign {sgn:+.0f}, fixed hl=10: Lnet {row['long_ann'] * 100:+.1f}%  Lgross "
              f"{row['long_gross_ann'] * 100:+.1f}%  Lshp {row['long_sharpe']:+.2f}  LTO {row['long_turnover'] * 100:.1f}%  "
              f"(vs 用户发布值 utrain/hl10 +5.6%)", flush=True)
        print("两处 LTO 读数(R0 异常2;原样抄自 notes/06_baseline.md,未重新推导来源,硬规矩不读 partura/):\n"
              "  digest 头条表(S0_baseline,train,hlL=20自选半衰期): LTO = 4.7%  (06_baseline.md 第1节)\n"
              "  all_controls 中性化表『未中性化』行(同一 hlL=20 信号,train):LTO = 5.2%  (06_baseline.md 第7节)\n"
              "  两张表 Lgross(+3.9%)/Lnet(+0.3%) 逐位相同,只有 LTO 不同。", flush=True)
    safe(s0, "0")
    mem_mark("after 0")

    # ------------------------------------------------------------ A1
    def sA1():
        hdr("A1. the known family alone -- the line every combination below must beat")
        if K1 is not None:
            STATE["bK1"] = book_line(st, "K1 (stdamt_mean30)", K1)
        if K2 is not None:
            STATE["bK2"] = book_line(st, "K2 (stdamt_max9)", K2)
    safe(sA1, "A1")
    mem_mark("after A1")
    hl_K1 = STATE.get("bK1", {}).get("hl_long")
    hl_K2 = STATE.get("bK2", {}).get("hl_long")

    # ------------------------------------------------------------ A2 (core measurement)
    def sA2():
        hdr("A2. removal screens on the family long pool vs a SAME-SIZE family-only control (core measurement)")
        combos = []
        if K1 is not None:
            combos += [("K1", K1, "D_ema20", D_ema20), ("K1", K1, "D_m30", D_m30)]
        if K2 is not None:
            combos += [("K2", K2, "D_ema20", D_ema20), ("K2", K2, "D_m30", D_m30)]
        for kname, Kp, dname, Dp in combos:
            ok_full = np.isfinite(Kp) & np.isfinite(Dp) & np.isfinite(tgt)
            rk_full = pct_rank(np.where(ok_full, -Kp, np.nan))          # high = family long end
            rankK_full = dg.rank_rows(np.where(ok_full, Kp, np.nan))    # rank 1 = smallest K = best
            for pool_name, frac in (("quintile(20%)", 0.8), ("decile(10%)", 0.9)):
                pool = ok_full & (rk_full >= frac)
                prD = pct_rank(np.where(pool, Dp, np.nan))              # within-pool percentile of D
                for x in (10, 20, 30):
                    screened = pool & (prD >= x / 100.0)                # drop worst x% of pool by D
                    n_scr = screened.sum(1).astype(np.float64)
                    matched = ok_full & np.isfinite(rankK_full) & (rankK_full <= n_scr[:, None])
                    for sname, sl in splits:
                        rs = book_stats_row(*screened_book(screened[sl], ok_full[sl], tgt[sl]))
                        rm = book_stats_row(*screened_book(matched[sl], ok_full[sl], tgt[sl]))
                        incr_net, incr_gross = rs["Lnet"] - rm["Lnet"], rs["Lgross"] - rm["Lgross"]
                        print(f"  {kname}x{dname} {pool_name} excl{x:>2}% [{sname}]  screened: {fmt_row(rs)}  |  "
                              f"matched({rm['N']:.0f}): {fmt_row(rm)}  |  incr(net) {incr_net:+5.1f}pp  "
                              f"incr(gross) {incr_gross:+5.1f}pp", flush=True)
            del ok_full, rk_full, rankK_full
            gc.collect()
    safe(sA2, "A2")
    mem_mark("after A2")

    # ------------------------------------------------------------ A3
    def sA3():
        hdr("A3. rank-space asymmetric overlay  rk + w * rD**p  (self-check: (1,1) vs x1's 'add ema20')")
        wp_list = [(1, 1), (1, 3), (1, 6), (0.5, 1), (0.25, 1), (0.5, 3)]
        combos = []
        if K1 is not None:
            combos += [("K1", K1, hl_K1), ]
        if K2 is not None:
            combos += [("K2", K2, hl_K2), ]
        for kname, Kp, hl_fam in combos:
            rk = pct_rank(-Kp)
            for dname, Dp in (("D_ema20", D_ema20), ("D_m30", D_m30)):
                rD = pct_rank(Dp)
                for w, p in wp_list:
                    combo = rk + w * (rD ** p)
                    name = f"{kname}+{w:g}*{dname}^{p}"
                    book_line(st, name, combo, sign=1.0)
                    if hl_fam is not None:
                        fixed_line(st, name + f" @famHL{hl_fam:g}", combo, tgt, tr, va, 1.0, hls=(hl_fam,))
                    del combo
                del rD
                gc.collect()
            del rk
            gc.collect()
    safe(sA3, "A3")
    mem_mark("after A3")

    # ------------------------------------------------------------ A4
    def sA4():
        hdr("A4. neutralisation, both directions (R2, residual rank IC, residual books)")
        def one(name, y_full, x_full):
            for sname, sl in splits:
                y, x = y_full[sl], x_full[sl]
                res, info = dg.neutralise(y, {"x": x})
                ic = dg.ic_row(res, tgt[sl], sign=1.0)
                br = bk.book_row(res, tgt[sl], slice(0, res.shape[0]))
                print(f"  {name} [{sname}]: R2 {info['mean_r2']:.3f}  residual rIC {ic['rank_ic']:+.4f}  "
                      f"Lgross {br['long_gross_ann'] * 100:+.1f}%  Lnet {br['long_ann'] * 100:+.1f}%  "
                      f"Lshp {br['long_sharpe']:+.2f}  LTO {br['long_turnover'] * 100:.1f}%", flush=True)
        hdr("A4a. D neutralised on K (does the known family explain the F108 signal?)")
        for dname, Dp in (("D_ema20", D_ema20), ("D_m30", D_m30)):
            if K1 is not None:
                one(f"{dname} ~ K1", Dp, K1)
            if K2 is not None:
                one(f"{dname} ~ K2", Dp, K2)
        hdr("A4b. K neutralised on D_m30, goodness-oriented (reverse direction: does F108 explain the family?)")
        if K1 is not None:
            sgnK1 = st.sign(K1, "train")
            one("K1(goodness) ~ D_m30", sgnK1 * K1, D_m30)
        if K2 is not None:
            sgnK2 = st.sign(K2, "train")
            one("K2(goodness) ~ D_m30", sgnK2 * K2, D_m30)
    safe(sA4, "A4")
    mem_mark("after A4")

    # ------------------------------------------------------------ B1
    def sB1():
        hdr("B1. H14 -- one-sided exclusion vs full decile ranking vs the equal-weight universe (D_m30)")
        ok = np.isfinite(D_m30) & np.isfinite(tgt)
        for sname, sl in splits:
            okx, Dp, t = ok[sl], D_m30[sl], tgt[sl]
            r = np.where(okx & np.isfinite(t), t, 0.0)
            nu = (okx & np.isfinite(t)).sum(1)
            ew = np.where(nu > 0, r.sum(1) / np.maximum(nu, 1), np.nan)
            s3 = bk.stats(ew)
            print(f"  book3 equal-weight universe [{sname}]: gross_ann {s3['ann'] * 100:+.1f}%  sharpe {s3['sharpe']:+.2f}  "
                  f"avgN {nu.mean():.0f}", flush=True)
            prD_all = pct_rank(np.where(okx, Dp, np.nan))
            for x in (3, 5, 10, 20):
                held = okx & (prD_all >= x / 100.0)
                row = book_stats_row(*screened_book(held, okx, t))
                print(f"  book1 excl worst {x:>2}% [{sname}] (vs book3): {fmt_row(row)}", flush=True)
            dec = okx & (prD_all >= 0.9)
            row2 = book_stats_row(*screened_book(dec, okx, t))
            print(f"  book2 D_m30 decile, full ranking [{sname}]: {fmt_row(row2)}", flush=True)
            del r, ew, prD_all
        gc.collect()
    safe(sB1, "B1")
    mem_mark("after B1")

    # ------------------------------------------------------------ B2
    def sB2():
        hdr("B2. H9 -- within-bucket ranking with language-available proxies for size")
        amt_mean30 = None
        try:
            amt_mean30 = st.panels({"amt_mean30": "cross_mean(day_sum(Amt), 30)"})["amt_mean30"]
        except Exception as exc:
            print(f"amt_mean30 unavailable: {exc}", flush=True)
        Vs = []
        if "ctl_amt" in C:
            Vs.append(("ctl_amt", np.asarray(C["ctl_amt"], dtype=np.float64)))
        if amt_mean30 is not None:
            Vs.append(("cross_mean(day_amt,30)", np.asarray(amt_mean30, dtype=np.float64)))
        if "ctl_price" in C:
            Vs.append(("ctl_price", np.asarray(C["ctl_price"], dtype=np.float64)))
        if "ctl_cap" in C:
            Vs.append(("ctl_cap(ceiling,未落地)", np.asarray(C["ctl_cap"], dtype=np.float64)))
        for vname, V in Vs:
            ok = np.isfinite(V) & np.isfinite(D_m30) & np.isfinite(tgt)
            bucket_id = bucket(pct_rank(np.where(ok, V, np.nan)), 5)
            Dmasked = np.where(ok, D_m30, np.nan)
            layer_pr = layered_pct_rank(Dmasked, bucket_id, 5)
            held_layer = ok & (layer_pr >= 0.9)
            plain_pr = pct_rank(Dmasked)
            held_plain = ok & (plain_pr >= 0.9)
            for sname, sl in splits:
                okx, t = ok[sl], tgt[sl]
                rl = book_stats_row(*screened_book(held_layer[sl], okx, t))
                rp = book_stats_row(*screened_book(held_plain[sl], okx, t))
                print(f"  V={vname} [{sname}]  within-bucket decile: {fmt_row(rl)}  ||  unbucketed D_m30 decile "
                      f"(same universe): {fmt_row(rp)}", flush=True)
            del bucket_id, Dmasked, layer_pr, held_layer, plain_pr, held_plain
            gc.collect()
    safe(sB2, "B2")
    mem_mark("after B2")

    # ------------------------------------------------------------ C
    def sC():
        hdr("C. same-tail comparison: F108's alert vs each control's own tail, matched by day-count")
        Vctl = []
        for name in ("ctl_ivol", "ctl_dvol20", "ctl_turnrate", "ctl_amt", "known_ivol_max9"):
            if name in C:
                Vctl.append((name, np.asarray(C[name], dtype=np.float64)))
        if jmax64 is not None:
            Vctl.append(("jmax", jmax64))
        for thr, thr_name in ((15.0, "r>=15"), (24.9, "r>=24.9")):
            hdr(f"C.{thr_name}")
            for vname, V in Vctl:
                ok = np.isfinite(r_full) & np.isfinite(V) & np.isfinite(tgt)
                ex = excess(tgt, ok)
                F = ok & (r_full >= thr)
                for sname, sl in splits:
                    okx, Fx, Vx, exx = ok[sl], F[sl], V[sl], ex[sl]
                    n_f = Fx.sum(1).astype(np.float64)
                    rank_desc = dg.rank_rows(np.where(okx, -Vx, np.nan))       # rank 1 = highest V
                    Vm = okx & np.isfinite(rank_desc) & (rank_desc <= n_f[:, None])
                    both, onlyF = Fx & Vm, Fx & ~Vm
                    onlyV, neither = okx & ~Fx & Vm, okx & ~Fx & ~Vm
                    pVgF = float(both.sum()) / max(float(Fx.sum()), 1.0)
                    pFgV = float(both.sum()) / max(float(Vm.sum()), 1.0)
                    a_b, _ = cell_ann(exx, both)
                    a_of, _ = cell_ann(exx, onlyF)
                    a_ov, _ = cell_ann(exx, onlyV)
                    a_n, _ = cell_ann(exx, neither)
                    print(f"  {vname:<16} [{sname}] P(V|F)={pVgF:.3f} P(F|V)={pFgV:.3f} | "
                          f"both {a_b:+6.1f}%(n={int(both.sum())})  onlyF {a_of:+6.1f}%(n={int(onlyF.sum())})  "
                          f"onlyV {a_ov:+6.1f}%(n={int(onlyV.sum())})  neither {a_n:+6.1f}%(n={int(neither.sum())})",
                          flush=True)
                del ok, ex, F
            gc.collect()
    safe(sC, "C")
    mem_mark("end")


if __name__ == "__main__":
    with Study(FID) as st_:
        main(st_)
    print("\n[x2_longonly done]", flush=True)
