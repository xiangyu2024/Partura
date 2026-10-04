"""F109 x2: for a long-only user, does this tree add anything to the known amount-
volatility family (R1, group B)?  x1 only did a crude rank-add (no pairing, no
standard error), so "+1 point" could not be told from noise.  This script adds
pairing.  Only train / valid are read.

  1. BASE / REG / EVT / FAM30 / FAM9 each on their own: long-leg net excess and
     pure-long Sharpe, train/valid.  (self-check: must land near the already-known
     x1 / S0 numbers; this gate is checked at runtime once connected to real data.)
  2. BASE / REG / EVT, each rank-neutralised against FAM30 (daily cross-sectional
     OLS in rank space -- no look-ahead, each day uses only that day's cross-
     section): R^2, residual long-leg net excess and Sharpe, train/valid, with the
     residual re-signed and re-half-lifed from scratch (the study's usual
     convention: nothing is fit on the original tree's choices).
  3. rank(FAM30) + w*rank(candidate) for w in {0.1, 0.3, 1.0}, candidate in
     {BASE, REG, EVT} -- 9 combinations.  Long-leg net excess and Sharpe, plus the
     PAIRED daily difference (combo's long-leg day return minus FAM30's own) and
     its t-statistic, train and valid separately.
  4. FAM30's own long decile: what share of its stock-days are flagged by
     EVTFLAG (a stock was at a degenerate quantile day at least once in the
     trailing 20 days), and the long-leg net excess / Sharpe before and after
     dropping those names from the decile (next-ranked names promoted in,
     FAM30's own ranking order) -- plus the paired t-statistic of that swap.

``X2_SELFTEST_ONLY=1`` runs only ``_selftest()`` (no Study, no server) -- for
shaking the new helpers out before spending a server run.
"""
import os
import warnings

import numpy as np

from partura.study_tools import Study, bk, dg

warnings.simplefilter("ignore", RuntimeWarning)
np.set_printoptions(linewidth=200)
FID = "F109_erm_mag_gap_5m_tsm20"
COST, TOP = 0.0015, 0.10

# ---- copied verbatim from studies/F109_erm_mag_gap_5m_tsm20/x1_anatomy.py -------
# (same day-level parts as the original tree; do not re-derive, do not re-run x1)
R5 = "sub(div(Close, in_delay(Close, 5)), create_like(Close, 1))"
Q95, Q05 = "day_quantile(Ret, 0.95)", "day_quantile(Ret, 0.05)"
E95, E05 = f"create_like({Q95}, 1e-06)", f"create_like({Q05}, 1e-06)"
UPC = f"add(day_sum(is_gt({R5}, {Q95})), {E95})"
DNC = f"add(day_sum(is_lt({R5}, {Q05})), {E05})"
UPM = f"div(day_sum(select_where(is_gt({R5}, {Q95}), {R5}, create_like(Close, 0))), {UPC})"
DNM = f"div(day_sum(select_where(is_lt({R5}, {Q05}), abs_({R5}), create_like(Close, 0))), {DNC})"
EXPRS = {"q95": Q95, "q05": Q05, "upm": UPM, "dnm": DNM}
THR = 1e-4            # x1's "degenerate" floor: a quantile below this in |.| is treated as 0
BIG = 20.0            # x1's "blow-up day" floor: |gap_d| above this is an event day


def roll_sum(x, d):
    xf = np.where(np.isfinite(x), x, 0.0)
    cs = np.cumsum(xf, axis=0)
    out = cs.copy()
    out[d:] = cs[d:] - cs[:-d]
    return out


def roll_mean(x, d):
    n = roll_sum(np.isfinite(x).astype(np.float64), d)
    return np.where(n > 0, roll_sum(x, d) / np.maximum(n, 1), np.nan)


def pct(x):
    r = dg.rank_rows(np.asarray(x, dtype=np.float64))
    n = np.isfinite(r).sum(1, keepdims=True)
    return (r - 0.5) / np.maximum(n, 1)


# ---- new for x2 (each piece self-tested below) ----------------------------------
def paired_tstat(net_a, net_b):
    """Daily difference (a - b) on the days both are finite: annualised mean,
    annualised std, t-stat (mean / (std/sqrt(n))), and n (shared finite days)."""
    a, b = np.asarray(net_a, dtype=np.float64), np.asarray(net_b, dtype=np.float64)
    ok = np.isfinite(a) & np.isfinite(b)
    d = (a - b)[ok]
    n = int(d.size)
    if n < 3 or d.std() == 0:
        return {"n_days": n, "ann_mean": float("nan"), "ann_std": float("nan"), "t": float("nan")}
    return {"n_days": n, "ann_mean": float(d.mean() * 252), "ann_std": float(d.std(ddof=0) * np.sqrt(252)),
            "t": float(d.mean() / d.std(ddof=0) * np.sqrt(n))}


def excluded_long_weights(sm, flag, top_frac):
    """Same long-side membership rule as ``alphacube.metrics.long_short_weights``
    (stable sort, k = max(1, floor(n*top_frac))), except a day-name with
    ``flag`` true is skipped and the next-ranked (by ``sm``) non-flagged name is
    promoted in, so the slot count and the 0.5/k weight are unchanged.  The short
    side is left at 0 -- unused by ``bk.long_book``, which only reads the clipped
    positive part. Returns (weights, k_used_per_day)."""
    sm = np.asarray(sm, dtype=np.float64)
    flag = np.asarray(flag, dtype=bool)
    D, S = sm.shape
    w = np.zeros((D, S), dtype=np.float64)
    k_used = np.zeros(D, dtype=np.int64)
    for t in range(D):
        row = sm[t]
        fin = np.isfinite(row)
        n = int(fin.sum())
        if n < 2:
            continue
        k = max(1, int(np.floor(n * top_frac)))
        order = np.argsort(np.where(fin, row, np.inf), kind="stable")
        best_to_worst = order[:n][::-1]
        ft = flag[t]
        chosen = []
        for idx in best_to_worst:
            if not ft[idx]:
                chosen.append(idx)
                if len(chosen) == k:
                    break
        if chosen:
            w[t, np.asarray(chosen)] = 0.5 / len(chosen)
            k_used[t] = len(chosen)
    return w, k_used


def decile_flag_rate(sm, flag, top_frac, days):
    """Share of (day, name) slots in the ORIGINAL (un-backfilled) long decile of
    ``sm`` over ``days`` for which ``flag`` is true, and the total slot count."""
    sm_s, flag_s = np.asarray(sm[days], dtype=np.float64), np.asarray(flag[days], dtype=bool)
    D, S = sm_s.shape
    total_k, total_flagged = 0, 0
    for t in range(D):
        row = sm_s[t]
        fin = np.isfinite(row)
        n = int(fin.sum())
        if n < 2:
            continue
        k = max(1, int(np.floor(n * top_frac)))
        order = np.argsort(np.where(fin, row, np.inf), kind="stable")
        top_idx = order[n - k:n]
        total_k += k
        total_flagged += int(flag_s[t, top_idx].sum())
    return (total_flagged / total_k if total_k else float("nan")), total_k


def fit_eval(panel_full, target_full, tr, spl, cost, top_frac, sign=None):
    """The study's usual convention: sign (if not given) and half-life fit on
    ``tr`` by the long book, evaluated on every split in ``spl``."""
    p = np.asarray(panel_full, dtype=np.float64)
    sg = dg.sign_from(p[tr], target_full[tr]) if sign is None else float(sign)
    b = bk.books(sg * p, target_full, tr, spl, cost=cost, top_frac=top_frac, rank_by="long")
    return {"sign": sg, "hlL": b["by_rank"]["long"]["hl"], "hlS": b["by_rank"]["ls"]["hl"],
            "books": b, "signed_panel": sg * p}


def net_series(fit, target_full, days, cost, top_frac):
    """The long book's own daily net-excess series on ``days``, at the half-life
    ``fit_eval`` chose for the LONG book (this study's ``rank_by: long``)."""
    sm = bk.smoothed(fit["signed_panel"], fit["hlL"])
    w = bk.long_short_weights(sm[days], top_frac)
    net, _, _ = bk.long_book(w, sm[days], target_full[days], cost)
    return net


def fmt_row(name, b):
    L, Sv = b["by_rank"]["long"], b["by_rank"]["ls"]
    lt, lv = L["splits"]["train"], L["splits"]["valid"]
    st_, sv_ = Sv["splits"]["train"], Sv["splits"]["valid"]
    return (f"{name:<10} hlL {L['hl']:>4g} Lnet {lt['long_ann']*100:+6.1f}% {lv['long_ann']*100:+6.1f}% "
            f"Lshp {lt['long_sharpe']:+5.2f} {lv['long_sharpe']:+5.2f} Lgross {lt['long_gross_ann']*100:+6.1f}% "
            f"{lv['long_gross_ann']*100:+6.1f}% | hlS {Sv['hl']:>4g} LS {st_['ls_sharpe']:+5.2f} {sv_['ls_sharpe']:+5.2f}")


# ------------------------------------------------------------------------ self-test
def _selftest():
    rng = np.random.default_rng(0)
    x = rng.normal(size=(40, 6))
    x[rng.random(x.shape) < 0.1] = np.nan
    ref = np.full_like(x, np.nan)
    for t in range(40):
        w = x[max(0, t - 4): t + 1]
        ok = np.isfinite(w)
        ref[t] = np.where(ok.sum(0) > 0, np.where(ok, w, 0).sum(0) / np.maximum(ok.sum(0), 1), np.nan)
    assert np.allclose(roll_mean(x, 5), ref, equal_nan=True), "roll_mean"

    # dg.neutralise (rank-space day-by-day OLS) needs >= 50 valid pairs/day (its own floor) to
    # attempt a day at all, so these checks use 60 names/day, not the 5-name toy size used below.
    x0 = np.arange(2.0, 122.0, 2.0).reshape(1, -1)       # 1 day, 60 names, strictly increasing
    y_inc = np.arange(1.0, 61.0).reshape(1, -1)          # same rank order as x0
    _, info_inc = dg.neutralise(y_inc, {"x": x0}, space="rank")
    assert info_inc["mean_r2"] > 0.999, f"identical rank order should give R2~1, got {info_inc['mean_r2']}"
    y_dec = y_inc[:, ::-1].copy()                        # exact reverse order of x0
    _, info_dec = dg.neutralise(y_dec, {"x": x0}, space="rank")
    assert info_dec["mean_r2"] > 0.999, f"reversed rank order should also give R2~1, got {info_dec['mean_r2']}"
    rng2 = np.random.default_rng(3)
    xN, yN = rng2.normal(size=(300, 60)), rng2.normal(size=(300, 60))      # independent, 60 names/day
    _, infoN = dg.neutralise(yN, {"x": xN}, space="rank")
    assert infoN["mean_r2"] < 0.15, f"independent panels should not show a strong rank-R2, got {infoN['mean_r2']}"

    # paired_tstat: hand-worked case, one NaN day dropped
    a = np.array([0.02, 0.03, 0.01, 0.04, np.nan])
    b = np.array([0.01, 0.01, 0.01, 0.01, 0.01])
    pt = paired_tstat(a, b)
    d = np.array([0.01, 0.02, 0.00, 0.03])
    assert pt["n_days"] == 4
    assert abs(pt["ann_mean"] - d.mean() * 252) < 1e-9
    assert abs(pt["t"] - d.mean() / d.std() * np.sqrt(4)) < 1e-9

    # excluded_long_weights: n=5, top_frac=0.4 -> k=2; flag the single best name
    sm_day = np.array([[1.0, 5.0, 4.0, 3.0, 2.0]])              # best..worst: idx1>idx2>idx3>idx4>idx0
    flag_day = np.array([[False, True, False, False, False]])   # best name (idx1) flagged
    w, k_used = excluded_long_weights(sm_day, flag_day, top_frac=0.4)
    assert k_used[0] == 2
    assert w[0, 1] == 0.0, "the flagged (best) name must be excluded"
    assert abs(w[0, 2] - 0.25) < 1e-9 and abs(w[0, 3] - 0.25) < 1e-9, "2nd/3rd best promoted in at 0.5/k each"
    assert w[0, 0] == 0.0 and w[0, 4] == 0.0
    w_noflag, k_noflag = excluded_long_weights(sm_day, np.zeros_like(flag_day, dtype=bool), 0.4)
    w0 = bk.long_short_weights(sm_day, 0.4)
    assert np.allclose(w_noflag, np.clip(w0, 0.0, None)), "no flags -> must match long_short_weights' long side exactly"

    # decile_flag_rate on the same tiny day: original top-2 = {idx1, idx2}; only idx1 flagged -> rate 1/2
    rate, k = decile_flag_rate(sm_day, flag_day, 0.4, slice(0, 1))
    assert k == 2 and abs(rate - 0.5) < 1e-12

    print("[selftest] roll_mean / neutralise(rank) / paired_tstat / excluded_long_weights / "
          "decile_flag_rate ok", flush=True)


def main():
    _selftest()
    if os.environ.get("X2_SELFTEST_ONLY"):
        print("[X2_SELFTEST_ONLY] selftest passed, not connecting to Study", flush=True)
        return
    with Study(FID) as st:
        tgt = np.asarray(st.target(), dtype=np.float64)
        tr, va = st.slice("train"), st.slice("valid")
        SPL = {"train": tr, "valid": va}
        print(f"[shape] train {tr}, valid {va}", flush=True)

        P = {k: np.asarray(v, dtype=np.float64) for k, v in st.panels(EXPRS).items()}
        print("[panels] got", sorted(P), "missing", [k for k in EXPRS if k not in P], flush=True)
        q95, q05, upm, dnm = P["q95"], P["q05"], P["upm"], P["dnm"]
        gap = upm / (q95 + 1e-6) - dnm / (np.abs(q05) + 1e-6)
        gfin = np.isfinite(gap)
        blow = np.abs(gap) > BIG
        z95 = (q95 < THR) & np.isfinite(q95)
        z05 = (q05 > -THR) & np.isfinite(q05)
        regd = (q95 >= THR) & (q05 <= -THR)

        BASE = roll_mean(gap, 20)
        REG = roll_mean(np.where(regd, gap, np.nan), 20)
        EVT = roll_mean(np.where(gfin, np.where(blow, gap, 0.0), np.nan), 20)
        FAM30 = np.asarray(st.control("known_stdamt_mean30"), dtype=np.float64)
        FAM9 = np.asarray(st.control("known_stdamt_max9"), dtype=np.float64)
        EVTFLAG = roll_sum((z95 | z05).astype(np.float64), 20) > 0
        D, S = BASE.shape
        print(f"[panels] gap/BASE/REG/EVT/FAM30/FAM9/EVTFLAG built, shape {D}x{S}", flush=True)

        # ============================================================ item 1
        print("\n=== 1. 五个面板各自的两本书(train/valid) ===", flush=True)
        FITS = {}
        for name, panel in (("BASE", BASE), ("REG", REG), ("EVT", EVT), ("FAM30", FAM30), ("FAM9", FAM9)):
            FITS[name] = fit_eval(panel, tgt, tr, SPL, COST, TOP)
            print(fmt_row(name, FITS[name]["books"]), flush=True)

        b = FITS["BASE"]["books"]["by_rank"]["long"]["splits"]
        f30 = FITS["FAM30"]["books"]["by_rank"]["long"]["splits"]
        base_tr_pct, base_va_pct = b["train"]["long_ann"] * 100, b["valid"]["long_ann"] * 100
        fam_tr_pct, fam_va_pct = f30["train"]["long_ann"] * 100, f30["valid"]["long_ann"] * 100
        print(f"\n[check] BASE Lnet train/valid = {base_tr_pct:+.1f}%/{base_va_pct:+.1f}% "
              f"(期望附近 -4.7%/+0.3%); FAM30 Lnet train/valid = {fam_tr_pct:+.1f}%/{fam_va_pct:+.1f}% "
              f"(期望附近 +12.6%/+22.3%)", flush=True)
        assert abs(base_tr_pct - (-4.7)) < 5 and abs(base_va_pct - 0.3) < 5, \
            f"BASE 与 x1/S0 的已知答案差太远(train {base_tr_pct:+.1f}% valid {base_va_pct:+.1f}%),先停下来核对口径"
        assert abs(fam_tr_pct - 12.6) < 3 and abs(fam_va_pct - 22.3) < 3, \
            f"FAM30 与 S0 已有的 known_stdamt_mean30 数字差太远(train {fam_tr_pct:+.1f}% valid {fam_va_pct:+.1f}%),先停下来核对口径"
        print("[check] 自检通过,继续往下算", flush=True)

        # ============================================================ item 2
        print("\n=== 2. BASE/REG/EVT 对 FAM30 的秩空间残差(重新定方向半衰期)===", flush=True)
        for name, panel in (("BASE", BASE), ("REG", REG), ("EVT", EVT)):
            resid = np.full((D, S), np.nan)
            r2 = {}
            for split_name, sl in (("train", tr), ("valid", va)):
                res, info = dg.neutralise(panel[sl], {"FAM30": FAM30[sl]}, space="rank")
                resid[sl] = res
                r2[split_name] = info["mean_r2"]
            fit_r = fit_eval(resid, tgt, tr, SPL, COST, TOP)
            rb = fit_r["books"]["by_rank"]["long"]["splits"]
            print(f"{name:<6} vs FAM30: R2 train {r2['train']:.3f} valid {r2['valid']:.3f} | "
                  f"残差 sign {fit_r['sign']:+.0f} hlL {fit_r['hlL']:g} "
                  f"Lnet {rb['train']['long_ann']*100:+6.1f}% {rb['valid']['long_ann']*100:+6.1f}% "
                  f"Lshp {rb['train']['long_sharpe']:+5.2f} {rb['valid']['long_sharpe']:+5.2f}", flush=True)

        # ============================================================ item 3
        print("\n=== 3. rank(FAM30) + w*rank(候选):多头腿 + 对 FAM30 的配对差 ===", flush=True)
        net_fam_tr = net_series(FITS["FAM30"], tgt, tr, COST, TOP)
        net_fam_va = net_series(FITS["FAM30"], tgt, va, COST, TOP)
        ks = pct(FITS["FAM30"]["sign"] * FAM30)
        for cand in ("BASE", "REG", "EVT"):
            cs_ = pct(FITS[cand]["sign"] * (BASE if cand == "BASE" else REG if cand == "REG" else EVT))
            for w in (0.1, 0.3, 1.0):
                combo = ks + w * cs_
                fit_c = fit_eval(combo, tgt, tr, SPL, COST, TOP, sign=1.0)
                cb = fit_c["books"]["by_rank"]["long"]["splits"]
                net_c_tr = net_series(fit_c, tgt, tr, COST, TOP)
                net_c_va = net_series(fit_c, tgt, va, COST, TOP)
                pt_tr = paired_tstat(net_c_tr, net_fam_tr)
                pt_va = paired_tstat(net_c_va, net_fam_va)
                print(f"FAM30+{w:g}*{cand:<4} hlL {fit_c['hlL']:g} "
                      f"Lnet {cb['train']['long_ann']*100:+6.1f}% {cb['valid']['long_ann']*100:+6.1f}% "
                      f"Lshp {cb['train']['long_sharpe']:+5.2f} {cb['valid']['long_sharpe']:+5.2f} | "
                      f"配对差(vs FAM30) train ann {pt_tr['ann_mean']*100:+5.1f}% t {pt_tr['t']:+5.2f} n {pt_tr['n_days']} | "
                      f"valid ann {pt_va['ann_mean']*100:+5.1f}% t {pt_va['t']:+5.2f} n {pt_va['n_days']}", flush=True)

        # ============================================================ item 4
        print("\n=== 4. FAM30 多头十分位:EVTFLAG 占比 + 剔除再补位 ===", flush=True)
        sm_fam_full = bk.smoothed(FITS["FAM30"]["signed_panel"], FITS["FAM30"]["hlL"])
        for split_name, sl in (("train", tr), ("valid", va)):
            rate, k = decile_flag_rate(sm_fam_full, EVTFLAG, TOP, sl)
            print(f"[{split_name}] FAM30 多头十分位里 EVTFLAG 占比 {rate*100:.2f}% (decile 总格数 {k})", flush=True)

        net_fam = {"train": net_fam_tr, "valid": net_fam_va}
        for split_name, sl in (("train", tr), ("valid", va)):
            w_excl, k_used = excluded_long_weights(sm_fam_full[sl], EVTFLAG[sl], TOP)
            net_excl, _, _ = bk.long_book(w_excl, sm_fam_full[sl], tgt[sl], COST)
            before, after = bk.stats(net_fam[split_name]), bk.stats(net_excl)
            pt = paired_tstat(net_excl, net_fam[split_name])
            print(f"[{split_name}] 剔除前 Lnet {before['ann']*100:+.1f}% Lshp {before['sharpe']:+.2f} | "
                  f"剔除后 Lnet {after['ann']*100:+.1f}% Lshp {after['sharpe']:+.2f} | "
                  f"配对差 ann {pt['ann_mean']*100:+.1f}% t {pt['t']:+.2f} n {pt['n_days']} "
                  f"(k_used 均值 {k_used.mean():.2f}, 最小 {k_used.min()})", flush=True)

        print("\n[done]", flush=True)


if __name__ == "__main__":
    main()
