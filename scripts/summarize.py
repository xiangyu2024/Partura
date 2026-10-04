"""Console digest of Partura run JSON(s): the numbers a decision actually turns on.

    python scripts/summarize.py runs/<factor_id>/<tag>.json [more.json ...] [--base v_base]

Selection is by the LONG leg (A-shares: only the long book can be held):

  hlL    half-life fitted on the fit split by the pure long book's after-cost excess Sharpe
  Lnet   long-leg NET annual excess (after 15 bp per unit turnover) at hlL      <- the headline
  Lshp   pure-long Sharpe at hlL
  Lgross long-leg gross annual excess at hlL
  LTO    long book daily turnover at hlL

and, for comparability with the user's first table (which fitted the half-life by L/S Sharpe):

  hlS    half-life fitted by the decile long/short book's after-cost Sharpe
  LS     decile L/S Sharpe after cost at hlS;  short = short-leg gross annual excess at hlS
"""
import json
import sys
from pathlib import Path

args = [a for a in sys.argv[1:] if not a.startswith("--")]
base = "v_base"
if "--base" in sys.argv:
    base = sys.argv[sys.argv.index("--base") + 1]
    args = [a for a in args if a != base]


def f(v, nd=2, pct=False):
    try:
        x = float(v)
    except (TypeError, ValueError):
        return "—"
    if x != x:
        return "NaN"
    return f"{x:+.1%}" if pct else f"{x:+.{nd}f}"


def views(b):
    """{"ls": {hl, splits}, "long": {hl, splits}} for a books result of any vintage."""
    if "by_rank" in b:
        return b["by_rank"]
    return {"ls": {"hl": b["hl_ls"], "splits": b["splits"]},
            "long": {"hl": b["hl_long"], "splits": b.get("splits_at_hl_long") or b["splits"]}}


def book_table(rows, a, b, la, lb):
    """rows: [(vid, sign, books, extra_cols)]"""
    print(f"{'variant':<20}{'sgn':>4} |{'hlL':>4}{'Lnet ' + la:>10}{'Lnet ' + lb:>10}{'Lshp ' + la:>9}{'Lshp ' + lb:>9}"
          f"{'Lgross ' + la:>11}{'Lgross ' + lb:>11}{'LTO':>6} |{'hlS':>4}{'LS ' + la:>8}{'LS ' + lb:>8}{'short ' + la:>10}")
    for vid, sign, bks in rows:
        v = views(bks)
        lo, ls = v["long"], v["ls"]
        x, y = lo["splits"].get(a, {}), lo["splits"].get(b, {})
        p, q = ls["splits"].get(a, {}), ls["splits"].get(b, {})
        print(f"{vid:<20}{'+' if sign > 0 else '-':>4} |{lo['hl']:>4g}"
              f"{f(x.get('long_ann'), pct=True):>10}{f(y.get('long_ann'), pct=True):>10}"
              f"{f(x.get('long_sharpe')):>9}{f(y.get('long_sharpe')):>9}"
              f"{f(x.get('long_gross_ann'), pct=True):>11}{f(y.get('long_gross_ann'), pct=True):>11}"
              f"{x.get('long_turnover', float('nan')):>6.1%} |{ls['hl']:>4g}"
              f"{f(p.get('ls_sharpe')):>8}{f(q.get('ls_sharpe')):>8}{f(p.get('short_gross_ann'), pct=True):>10}")


for path in args:
    d = json.loads(Path(path).read_text(encoding="utf-8"))
    res, diag = d["results"], d.get("diagnostics", {})
    v = d["view"]
    print(f"\n===== {d['factor_id']}  [{Path(path).name}]  {v['days']}d x {v['symbols']}s  "
          f"splits {d['splits_used']}  fit={d.get('fit_split')}  device={d.get('device', '?')}  "
          f"{d.get('seconds')}s  peak anon {d.get('peak_anon_gb')}G =====")
    for k, e in (d.get("errors") or {}).items():
        print(f"  ERROR {k}: {str(e)[:170]}")
    good = [(vid, r) for vid, r in res.items() if "error" not in r]
    for vid, r in res.items():
        if "error" in r:
            print(f"  求值失败 {vid}: {str(r['error'])[:150]}")

    print("\n决策口径(方向/半衰期在 train 上定; valid 没见过)—— 按多头腿选:")
    book_table([(vid, r["sign"], r["books"]) for vid, r in good], "train", "valid", "tr", "va")
    print(f"\n{'variant':<20}{'rIC tr':>9}{'rIC va':>9}{'rICtraded tr':>14}{'rICtraded va':>14}{'cov':>7}{'dist':>7}")
    for vid, r in good:
        s = r["splits"]
        print(f"{vid:<20}{f(s['train'].get('rank_ic'), 4):>9}{f(s.get('valid', {}).get('rank_ic'), 4):>9}"
              f"{f(s['train'].get('rank_ic_traded'), 4):>14}{f(s.get('valid', {}).get('rank_ic_traded'), 4):>14}"
              f"{s['train'].get('coverage_labelled', float('nan')):>7.2f}{r.get('distinct', float('nan')):>7.2f}")
    print("  (rIC = 原始日频面板的 rank IC; rICtraded = 平滑后实际交易信号的; cov ≥ 0.95、dist ≥ 0.5 是用户的两道门槛)")

    sw_rows = [(vid, r) for vid, r in good if r["books"].get("sweep")]
    if sw_rows:
        print("\n固定半衰期下的 train 表现(结构之间先在同一半衰期下比;Lnet = 多头腿净超额, Lshp = 纯多头夏普):")
        hs = (0.0, 2.0, 5.0, 10.0, 20.0)
        print(f"{'variant':<20}" + "".join(f"{'hl' + format(h, 'g') + ' Lnet':>11}{'Lshp':>7}{'LTO':>5}" for h in hs))
        for vid, r in sw_rows:
            sw = {x["halflife"]: x for x in r["books"]["sweep"]}
            print(f"{vid:<20}" + "".join(
                f"{f(sw[h]['long_ann'], pct=True):>11}{f(sw[h]['long_sharpe']):>7}{sw[h]['long_turnover']:>5.0%}"
                if h in sw else f"{'—':>23}" for h in hs))

    users = [(vid, r) for vid, r in good if "books_user" in r]
    if users:
        us = d.get("user_split", "utrain")
        has_ho = any("holdout" in r["books_user"]["splits"] for _, r in users)
        print(f"\n与用户表同口径(方向/半衰期在 {us} = 用户训练段上定"
              f"{'; ho = holdout = 用户测试段' if has_ho else '; 留出段未读'}):")
        book_table([(vid, r.get("sign_user", r["sign"]), r["books_user"]) for vid, r in users], us, "holdout", "utr", "ho")

    for vid, r in good:
        if r.get("profile"):
            for sname, rows in r["profile"].items():
                print(f"分位超额 {vid} [{sname}] Q1..Q{len(rows)}(Q{len(rows)} = 多头端): " +
                      " ".join(f(x['excess_ann'], pct=True) for x in rows))

    for vid, entry in (diag.get("neutralise") or {}).items():
        b = entry.get("_traded_signal", {})
        print(f"\n中性化 {vid}(fit 段;对象 = 实际交易的信号;残差不再平滑 → 残差换手更高,净值类指标可能只因成本而塌,"
              f"alpha 还在不在看 rIC / 毛超额):")
        print(f"  {'(未中性化)':<14} R2   —    rIC {f(b.get('rank_ic'), 4)}  Lgross {f(b.get('long_gross_ann'), pct=True)}  "
              f"Lnet {f(b.get('long_ann'), pct=True)}  short {f(b.get('short_gross_ann'), pct=True)}  "
              f"LSgross {f(b.get('ls_gross_sharpe'))}  LS {f(b.get('ls_sharpe'))}  TO {b.get('ls_turnover', float('nan')):.1%}")
        for ctl, rec in entry.items():
            if ctl == "_traded_signal":
                continue
            extra = f"  (原始日频面板上的 R2: {rec['r2_raw_panel']:.3f})" if "r2_raw_panel" in rec else ""
            print(f"  {ctl:<14} R2 {rec['r2']:.3f}  残差 rIC {f(rec['rank_ic'], 4)}  Lgross {f(rec['long_gross_ann'], pct=True)}  "
                  f"Lnet {f(rec.get('long_ann'), pct=True)}  short {f(rec.get('short_gross_ann'), pct=True)}  "
                  f"LSgross {f(rec.get('ls_gross_sharpe'))}  LS {f(rec['ls_sharpe'])}  TO {rec['ls_turnover']:.1%}{extra}")
    for key, rows in (diag.get("conditional") or {}).items():
        print(f"条件 IC {key}(分桶变量从低到高): " + "  ".join(f"Q{r['bucket'] + 1} {f(r['rank_ic'], 4)}" for r in rows))
    if diag.get("controls"):
        print("\n控制变量 / 已知家族自己当因子(同口径, train/valid):")
        for k, m in diag["controls"].items():
            print(f"  {k:<20}{'+' if m['sign'] > 0 else '-'} rIC {f(m['rank_ic'], 4)} hl {m['hl']:g}  "
                  f"Lnet {f(m.get('train_long_ann'), pct=True)}/{f(m.get('valid_long_ann'), pct=True)}  "
                  f"Lshp {f(m.get('train_long_sharpe'))}/{f(m.get('valid_long_sharpe'))}  "
                  f"LS {f(m.get('train_ls_sharpe'))}/{f(m.get('valid_ls_sharpe'))}  "
                  f"LTO {m.get('train_long_turnover', m.get('train_ls_turnover', float('nan'))):.1%}")
    m = diag.get("rank_corr_train")
    if m:
        on = "实际交易信号" if diag.get("rank_corr_on") else "原始面板"
        for anchor in dict.fromkeys([base] + [k for k in m if k in res]):
            if anchor in m:
                print(f"\n与 {anchor} 的日截面 rank 相关(fit 段, {on}; |.|>=0.95 = 同一因子族): " +
                      "  ".join(f"{k} {val:+.2f}" for k, val in sorted(m[anchor].items(), key=lambda kv: -abs(kv[1]))
                                if k != anchor))
                break
    for vid, rows in (diag.get("by_year") or {}).items():
        print(f"逐年 {vid}: " + "  ".join(
            f"{r['year']} Lnet {f(r['long_ann'], pct=True)} LS {f(r['ls_sharpe'])}" for r in rows))
    for vid, rows in (diag.get("decay") or {}).items():
        print(f"衰减 {vid} rank IC: " + "  ".join(f"h{r['horizon']} {f(r['rank_ic'], 4)}" for r in rows))
