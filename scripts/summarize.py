"""Console digest of Partura run JSON(s): the numbers a decision actually turns on.

    python scripts/summarize.py runs/<factor_id>/<stage>.json [more.json ...] [--base v_base]

Money is in the user's convention (partura.books): decile L/S Sharpe after 15 bp
at the half-life fitted on the fit split, and the long leg as a pure long book
vs the equal-weight universe (gross = the column the user's table publishes;
net = after 15 bp per unit turnover).
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
        return "   —  "
    if x != x:
        return "  NaN "
    return f"{x:+.1%}" if pct else f"{x:+.{nd}f}"


for path in args:
    d = json.loads(Path(path).read_text(encoding="utf-8"))
    res, diag = d["results"], d.get("diagnostics", {})
    v = d["view"]
    print(f"\n===== {d['factor_id']}  [{Path(path).name}]  {v['days']}d x {v['symbols']}s  "
          f"splits {d['splits_used']}  fit={d.get('fit_split')}  {d.get('seconds')}s  "
          f"peak anon {d.get('peak_anon_gb')}G =====")
    if d.get("errors"):
        for k, e in d["errors"].items():
            print(f"  ERROR {k}: {str(e)[:160]}")

    print(f"\n{'variant':<20}{'sgn':>4}{'rIC tr':>9}{'rIC va':>9}{'hl':>4}{'LS tr':>7}{'LS va':>7}"
          f"{'Lgross tr':>10}{'Lgross va':>10}{'Lnet tr':>9}{'Lnet va':>9}{'Lshr':>6}{'TO':>6}{'cov':>6}{'dist':>6}")
    for vid, r in res.items():
        if "error" in r:
            print(f"{vid:<20} ERROR {str(r['error'])[:110]}")
            continue
        s, b = r["splits"], r["books"]["splits"]
        tr, va = b.get("train", {}), b.get("valid", {})
        print(f"{vid:<20}{'+' if r['sign'] > 0 else '-':>4}{f(s['train']['rank_ic'], 4):>9}"
              f"{f(s.get('valid', {}).get('rank_ic'), 4):>9}{r['books']['hl_used']:>4g}"
              f"{f(tr.get('ls_sharpe')):>7}{f(va.get('ls_sharpe')):>7}"
              f"{f(tr.get('long_gross_ann'), pct=True):>10}{f(va.get('long_gross_ann'), pct=True):>10}"
              f"{f(tr.get('long_ann'), pct=True):>9}{f(va.get('long_ann'), pct=True):>9}"
              f"{tr.get('long_share', float('nan')):>6.0%}{tr.get('ls_turnover', float('nan')):>6.1%}"
              f"{s['train'].get('coverage_labelled', float('nan')):>6.2f}{r.get('distinct', float('nan')):>6.2f}")
    print("  (LS = 扣费多空夏普; Lgross/Lnet = 多头腿毛/净年化超额; Lshr = 多头腿占毛价差的比例; "
          "cov = 有标签格子里有值的比例,用户门槛 0.95; dist = 取值离散度,用户门槛 0.5)")
    # Each variant is scored at ITS OWN fitted half-life, so two variants can differ in turnover (and
    # therefore in net long-leg excess) only because one fitted 10 and the other 20.  The same numbers at
    # fixed half-lives separate "different structure" from "different smoothing".
    rows = [(vid, r) for vid, r in res.items() if "books" in r and r["books"].get("sweep")]
    if len(rows) > 1:
        print(f"\n固定半衰期下的 train 表现(各变体自己选的半衰期不同,先看这张再比结构):")
        print(f"{'variant':<20}" + "".join(f"{'hl' + format(h, 'g') + ' LS':>9}{'Lnet':>8}{'TO':>6}" for h in (5, 10, 20)))
        for vid, r in rows:
            sw = {x["halflife"]: x for x in r["books"]["sweep"]}
            print(f"{vid:<20}" + "".join(
                f"{f(sw[h]['ls_sharpe']):>9}{f(sw[h]['long_ann'], pct=True):>8}{sw[h]['ls_turnover']:>6.0%}"
                if h in sw else f"{'—':>23}" for h in (5.0, 10.0, 20.0)))

    users = {k: r for k, r in res.items() if "books_user" in r}
    if users:
        us = d.get("user_split", "utrain")
        print(f"\n与用户表同口径(方向/半衰期在 {us} 上定; holdout = 用户的测试段):")
        print(f"{'variant':<20}{'sgn':>4}{'hl':>4}{'LS utr':>8}{'LS ho':>8}{'Lgross utr':>11}{'Lgross ho':>10}"
              f"{'Lnet utr':>10}{'Lnet ho':>9}{'Lsharpe utr':>12}{'Lsharpe ho':>11}{'short utr':>10}")
        for vid, r in users.items():
            bu = r["books_user"]
            a, h = bu["splits"].get(us, {}), bu["splits"].get("holdout", {})
            print(f"{vid:<20}{'+' if r.get('sign_user', 1) > 0 else '-':>4}{bu['hl_used']:>4g}"
                  f"{f(a.get('ls_sharpe')):>8}{f(h.get('ls_sharpe')):>8}"
                  f"{f(a.get('long_gross_ann'), pct=True):>11}{f(h.get('long_gross_ann'), pct=True):>10}"
                  f"{f(a.get('long_ann'), pct=True):>10}{f(h.get('long_ann'), pct=True):>9}"
                  f"{f(a.get('long_sharpe')):>12}{f(h.get('long_sharpe')):>11}"
                  f"{f(a.get('short_gross_ann'), pct=True):>10}")

    b0 = res.get(base)
    if b0 and "books" in b0:
        print(f"\n半衰期扫描 {base}(fit 段; LS = 扣费多空夏普, Lshp = 纯多头夏普): " + "  ".join(
            f"hl{s['halflife']:g}: LS {f(s['ls_sharpe'])} Lshp {f(s['long_sharpe'])} TO {s['ls_turnover']:.0%}"
            for s in b0["books"]["sweep"]))
    for vid, r in res.items():
        if r.get("profile"):
            for sname, rows in r["profile"].items():
                print(f"分位超额 {vid} [{sname}] Q1..Q{len(rows)}: " +
                      " ".join(f(x['excess_ann'], pct=True) for x in rows))

    for vid, entry in (diag.get("neutralise") or {}).items():
        b = entry.get("_traded_signal", {})
        print(f"\n中性化 {vid}(fit 段;对象是**实际交易的信号** = 方向 x 面板、按半衰期平滑;残差不再平滑):")
        print("  (LSgross = 无成本多空夏普:残差没有再平滑、换手更高,扣费夏普塌掉可能只是成本;"
              "alpha 还在不在看 rIC 和 LSgross)")
        print(f"  {'(未中性化)':<14} R2   —    rIC {f(b.get('rank_ic'), 4)}  LSgross {f(b.get('ls_gross_sharpe'))}  "
              f"LS {f(b.get('ls_sharpe'))}  Lgross {f(b.get('long_gross_ann'), pct=True)}  "
              f"short {f(b.get('short_gross_ann'), pct=True)}  TO {b.get('ls_turnover', float('nan')):.1%}")
        for ctl, rec in entry.items():
            if ctl == "_traded_signal":
                continue
            extra = f"  (原始日频面板上的 R2 只有 {rec['r2_raw_panel']:.3f})" if "r2_raw_panel" in rec else ""
            print(f"  {ctl:<14} R2 {rec['r2']:.3f}  残差 rIC {f(rec['rank_ic'], 4)}  "
                  f"LSgross {f(rec.get('ls_gross_sharpe'))}  LS {f(rec['ls_sharpe'])}  "
                  f"Lgross {f(rec['long_gross_ann'], pct=True)}  short {f(rec.get('short_gross_ann'), pct=True)}  "
                  f"TO {rec['ls_turnover']:.1%}{extra}")
    for key, rows in (diag.get("conditional") or {}).items():
        print(f"条件 IC {key}: " + "  ".join(f"Q{r['bucket'] + 1} {f(r['rank_ic'], 4)}" for r in rows))
    if diag.get("controls"):
        print("\n控制变量 / 已知家族自己当因子(同口径):")
        for k, m in diag["controls"].items():
            print(f"  {k:<18}{'+' if m['sign'] > 0 else '-'} rIC {f(m['rank_ic'], 4)} hl {m['hl']:g}  "
                  f"LS {f(m.get('train_ls_sharpe'))}/{f(m.get('valid_ls_sharpe'))}  "
                  f"Lgross {f(m.get('train_long_gross_ann'), pct=True)}/{f(m.get('valid_long_gross_ann'), pct=True)}  "
                  f"TO {m.get('train_ls_turnover', float('nan')):.1%}")
    m = diag.get("rank_corr_train")
    if m and base in m:
        print(f"\n与 {base} 的日截面 rank 相关(fit 段; |.|>=0.95 = 同一因子族): " +
              "  ".join(f"{k} {val:+.2f}" for k, val in sorted(m[base].items(), key=lambda kv: -abs(kv[1]))
                        if k != base))
    for vid, rows in (diag.get("by_year") or {}).items():
        print(f"\n逐年 {vid}: " + "  ".join(
            f"{r['year']} LS {f(r['ls_sharpe'])} Lg {f(r['long_gross_ann'], pct=True)}" for r in rows))
    for vid, rows in (diag.get("decay") or {}).items():
        print(f"衰减 {vid} rank IC: " + "  ".join(f"h{r['horizon']} {f(r['rank_ic'], 4)}" for r in rows))
