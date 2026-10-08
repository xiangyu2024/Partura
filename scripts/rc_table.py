"""Print the risk-control table (runs/_risk/risk_control_<tag>.json).   rc_table.py [tag] [--all] [--md]

One row per book: total-return Sharpe / annual / max drawdown / Calmar in-sample and out-of-sample, average exposure, the
paired reading against the baseline (annual difference, t, the 90 % bootstrap interval of the Sharpe difference), the
2024-01/02 stampede window, and the verdict by the rule of research/risk_control/PLAN.md.  Default: the baseline, each
method family's in-sample pick, and the stacks; --all lists every grid cell.
"""
import json
import sys
from pathlib import Path

args = [a for a in sys.argv[1:] if not a.startswith("--")]
tag = args[0] if args else "r1"
J = json.loads((Path(__file__).resolve().parents[1] / "runs" / "_risk" / f"risk_control_{tag}.json").read_text(encoding="utf-8"))
ALL, MD = "--all" in sys.argv, "--md" in sys.argv
f = lambda x, p="{:+.1%}": "  nan" if x is None or x != x else p.format(x)       # noqa: E731


def rows(name):
    C = J["champions"][name]
    B = C["books"]
    picked = {p["key"]: p for p in C["picks"].values()}
    order = ["base"] + [k for k in B if k != "base" and (ALL or k in picked or k.startswith("C") or "尺子" in B[k]["family"])]
    out = []
    for k in order:
        v = B[k]
        i, o, st = v["stats"]["insample"], v["stats"]["oos"], v["stats"].get("stampede") or {}
        p = v.get("paired", {}).get("oos", {})
        ci = v.get("dsharpe_oos_ci90") or [float("nan")] * 3
        mark = "*" if k in picked else " "
        if k in picked and not picked[k]["passes_insample"]:
            mark = "x"
        out.append([mark + k, v["family"], f(i["sharpe"], "{:.2f}"), f(i["ann"]), f(i["mdd"]), f(i["calmar"], "{:.2f}"),
                    f(o["sharpe"], "{:.2f}"), f(o["ann"]), f(o["mdd"]), f(o["calmar"], "{:.2f}"), f(o["ex_ann"]), f(o["ex_sharpe"], "{:.2f}"), f(o.get("ex_mdd")), f(o["expo"], "{:.0%}"), f(o["turn"], "{:.1%}"),
                    f(p.get("ann")), f(p.get("t"), "{:+.1f}"), f"[{ci[0]:+.2f}, {ci[2]:+.2f}]", f(st.get("total")), f(v["stats"]["forward"]["sharpe"], "{:.2f}"), f(v["stats"]["forward"]["mdd"]), v.get("verdict", "")])
    return out


HEAD = ["book", "方法", "内夏普", "内年化", "内回撤", "内Calmar", "外夏普", "外年化", "外回撤", "外Calmar", "外超额", "超额夏普", "超额回撤", "仓位", "换手", "对基线年化差", "t", "夏普差90%区间", "踩踏段", "2026夏普", "2026回撤", "判读"]
for name in J["champions"]:
    R_ = rows(name)
    print(f"\n## {name}(半衰期 {J['champions'][name]['halflife']:g};* = 该方法族样本内选中的格子,x = 样本内就不如基线;外 = {J['segments']['oos'][0]} ~ {J['segments']['oos'][1]})")
    if MD:
        print("| " + " | ".join(HEAD) + " |\n|" + "---|" * len(HEAD))
        for r_ in R_:
            print("| " + " | ".join(r_) + " |")
    else:
        wd = [max(len(str(x)) + sum(1 for ch in str(x) if ord(ch) > 255) for x in col) for col in zip(HEAD, *R_)]
        pad = lambda s, n: str(s) + " " * (n - len(str(s)) - sum(1 for ch in str(s) if ord(ch) > 255))     # noqa: E731
        print("  ".join(pad(h, n) for h, n in zip(HEAD, wd)))
        for r_ in R_:
            print("  ".join(pad(x, n) for x, n in zip(r_, wd)))
    print("stacks:", json.dumps(J["champions"][name]["stacks"], ensure_ascii=False))
