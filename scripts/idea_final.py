"""The test-period read of what an idea search found -- the SAME object the search selected, by a rule written before.

Server.  For every given episode (episodes/<name>/evidence.json) and each arm, takes the find with the highest
score (partura.steer.is_discovery; an arm without a find is not read) and rebuilds, on the full period, exactly the
book the reward scored.  ``long_screen``: the base signal with the candidate's top fifth (whole tie blocks, at the
direction and half-life the search chose) sent below everything; reported as the paired daily difference against the
base book (annualised, information ratio, t).  Level rewards (``long`` / ``long_tradable`` / ``long_bucket``): the
signal the reward ranked (direction x EMA, cut to the tradable universe / ranked inside liquidity buckets); reported
as the book's own net excess and Sharpe (t = Sharpe x sqrt(years of holdout)), plus the same expression in the
user's convention and its paired difference against the known family.  Either way it first checks that the rebuilt
book reproduces the search's own numbers on train and on valid.  The read is ledgered.  Since 2026-10-06 the view
runs to the store's last day and the forward segment (2026-01 onward) is reported in a column of its own, with its
own ledger entry; verdicts stay on the period their plan named.

    python scripts/idea_final.py <episode> [<episode> ...] [--top 1] [--out episodes/<name>.json]
"""
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.guard import MemoryGuard, limit_threads, slot  # noqa: E402

limit_threads(8)
import numpy as np  # noqa: E402
import yaml  # noqa: E402

from partura import books as bk  # noqa: E402
from partura import diagnose as dg  # noqa: E402
from partura import ops_ext  # noqa: E402,F401
from partura import steer  # noqa: E402
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.panels import SHARED_CACHE, PanelSet  # noqa: E402
from partura.splits import SPLITS, Ledger  # noqa: E402

argv = sys.argv[1:]


def opt(name, default=None):
    return argv[argv.index(name) + 1] if name in argv else default


names = [a for i, a in enumerate(argv) if not a.startswith("-") and (i == 0 or argv[i - 1] not in ("--top", "--out"))]
TOP = int(opt("--top", 1))
cfg = yaml.safe_load((PARTURA_ROOT / "configs" / "K001_known_screens.yaml").read_text(encoding="utf-8"))     # the batch's splits
for k, v in cfg["splits"].items():
    SPLITS[k] = (str(v[0]), str(v[1]))

picks = []
for name in names:
    E = json.loads((PARTURA_ROOT / "episodes" / name / "evidence.json").read_text(encoding="utf-8"))
    if E["reward"] == "long_marginal":
        raise SystemExit(f"{name}: reward {E['reward']} -- the blend with the pool is not rebuilt here yet")
    G = steer.Guidance.load(PARTURA_ROOT / E.get("guidance", "guidance/B01.yaml"))
    for arm, A in E["arms"].items():
        cs = sorted([c for c in A["candidates"] if steer.is_discovery(E["reward"], c.get("score"), c.get("s_train"), c.get("s_valid"), float(E.get("threshold", 1.0)))],
                    key=lambda c: -c["score"])
        seen = set()
        for c in cs:
            f = G.family_key(c["expr"])
            if f in seen:
                continue
            seen.add(f)
            picks.append({"episode": name, "arm": arm, "reward": E["reward"], "base": E.get("screen_base") or "known", "split": E["period"][2], **{k: c.get(k) for k in
                          ("expr", "sign", "hl", "score", "s_train", "s_valid", "dann_train", "dann_valid", "ir_train", "ir_valid", "share", "train", "valid")}})
            if len(seen) >= TOP:
                break
print(f"[idea-final] {len(picks)} finds to read (top {TOP} per arm and run): " + ", ".join(f"{p['episode'].split('_')[0]}/{p['arm']}" for p in picks), flush=True)
if not picks:
    raise SystemExit(0)

with slot():
    mem = MemoryGuard(self_limit_gb=34, cgroup_limit_gb=70).start()
    t0 = time.time()
    # Since 2026-10-06 every rule-based read also reports the FORWARD segment (2026-01 onward; research/forward_2026/PLAN.md):
    # the view runs to the last day the store has, the old test period keeps its dates, the forward segment is ledgered apart.
    from alphacube.store import open_cube_store
    END = opt("--end") or str(open_cube_store("/root/autodl-tmp/qmt_daily_data/fast_factor_compute", mirror_root="/root/autodl-tmp/AlphaCube/mirror").dates[-1])
    ps = PanelSet("/root/autodl-tmp/qmt_daily_data/fast_factor_compute", SPLITS["full"][0], END, warmup=int(cfg.get("warmup", 60)),
                  device="cuda", gpu_fraction=0, cache_dir=str(SHARED_CACHE), mirror_root="/root/autodl-tmp/AlphaCube/mirror",
                  workdir=str(PARTURA_ROOT / "tmp"), label_kind="open_vwap15", label_buyable=True, batch=8)
    G = steer.Guidance.load(PARTURA_ROOT / "guidance" / "B01.yaml")
    pool_spec, known_spec = G.spec["pool"][-1], G.spec["pool"][0]
    P = ps.compute({"known": known_spec["expr"], "pool": pool_spec["expr"], "frozen": "cross_max(day_zero_ratio(Ret), 15)",
                    "age": "cross_valid_count(day_last(Close), 241)", "liq": "cross_mean(day_sum(Amt), 30)", **{f"c{i}": p["expr"] for i, p in enumerate(picks)}})
    tgt = ps.target(1)
    dates = np.asarray(ps.dates)
    _ix = lambda d: int(np.searchsorted(dates.astype(str), d))                # noqa: E731
    us, ho = slice(0, _ix("20230808")), slice(_ix("20230808"), _ix("20260101"))
    fw, oos = slice(ho.stop, len(dates)), slice(ho.start, len(dates))          # forward segment; the two out-of-sample periods together
    HAS_FW = fw.stop - fw.start > 20
    bases = {"known": dg._zrank(float(known_spec["sign"]) * np.asarray(P["known"], np.float64)),
             "pool": dg._zrank(bk.smoothed(float(pool_spec["sign"]) * np.asarray(P["pool"], np.float64), float(pool_spec["hl"])))}
    # the search's universe and liquidity buckets, by the same rule, on the full period (scripts/idea_search.py)
    frozen = np.asarray(P["frozen"], np.float64)
    possible = np.minimum(241, np.arange(1, len(dates) + 1))[:, None]
    untradable = ((dg._zrank(frozen) + 0.5) > 0.8) | (np.asarray(P["age"], np.float64) < 0.9 * possible) | ~np.isfinite(frozen)
    full_ctx = steer.RewardContext(tgt, us, ho, untradable=untradable, liq=np.asarray(P["liq"], np.float64), pool=bases["pool"], base=bases["known"])
    years = float(np.isfinite(tgt[ho]).any(1).sum()) / 252.0
    years_fw, years_oos = float(np.isfinite(tgt[fw]).any(1).sum()) / 252.0, float(np.isfinite(tgt[oos]).any(1).sum()) / 252.0

    def stats(d):
        f = d[np.isfinite(d)]
        if f.size < 20 or not f.std() > 0:
            return {"ann": float("nan"), "ir": float("nan"), "t": float("nan"), "n": int(f.size)}
        return {"ann": float(f.mean() * 252), "ir": float(f.mean() / f.std() * np.sqrt(252)), "t": float(f.mean() / f.std() * np.sqrt(f.size)), "n": int(f.size)}

    Ledger(PARTURA_ROOT / "runs" / "_ideas" / "ledger.json").record(
        "holdout", len(picks), "idea searches: the top find of each arm and run, rebuilt exactly as scored (" + ", ".join(f"{p['episode']}/{p['arm']}" for p in picks) + ")",
        "idea_final_" + "_".join(sorted({p["episode"].split("_")[0] for p in picks})))
    if HAS_FW:
        Ledger(PARTURA_ROOT / "runs" / "_forward" / "ledger.json").record(
            "forward", len(picks), f"idea searches, forward column {dates[fw.start]}..{dates[-1]}: " + ", ".join(f"{p['episode']}/{p['arm']}" for p in picks),
            "idea_final_" + "_".join(sorted({p["episode"].split("_")[0] for p in picks})))
    out = []

    def level(i, p):
        """A find of a level reward: the signal the reward ranked (direction x EMA, cut to the tradable universe and
        ranked inside liquidity buckets as that reward does), its pure long book alone, and against the known family."""
        raw = np.asarray(P[f"c{i}"], np.float64)
        sm = float(p["sign"]) * bk.smoothed(raw, float(p["hl"]))
        if p["reward"] in ("long_tradable", "long_bucket"):
            sm = np.where(untradable, np.nan, sm)
        if p["reward"] == "long_bucket":
            sm = steer._bucket_rank(sm, full_ctx.bucket())
        cut = int(np.searchsorted(dates, p["split"]))
        rows = {nm: bk.book_row(sm, tgt, sl) for nm, sl in (("train", slice(us.start, cut)), ("valid", slice(cut, us.stop)), ("utrain", us), ("holdout", ho))
                + ((("forward", fw), ("oos", oos)) if HAS_FW else ())}
        rep = abs(rows["train"]["long_sharpe"] - p["train"]) < 0.02 and abs(rows["valid"]["long_sharpe"] - p["valid"]) < 0.05
        # the same expression in the user's own convention (whole market, no universe cut, no buckets), for the batch tables
        usr = float(p["sign"]) * bk.smoothed(raw, float(p["hl"]))
        urows = {nm: bk.book_row(usr, tgt, sl) for nm, sl in (("utrain", us), ("holdout", ho)) + ((("forward", fw), ("oos", oos)) if HAS_FW else ())}
        ref = bases["known"]
        d = {nm: steer._daily_long_net(usr, tgt, sl) - steer._daily_long_net(ref, tgt, sl) for nm, sl in (("utrain", us), ("holdout", ho)) + ((("forward", fw),) if HAS_FW else ())}
        if HAS_FW:
            d["oos"] = np.concatenate([d["holdout"], d["forward"]])
        S = {nm: stats(x) for nm, x in d.items()}
        t = rows["holdout"]["long_sharpe"] * np.sqrt(years)                     # the book's own t on the holdout
        verdict = "成立" if (t >= 2 and rows["holdout"]["long_ann"] > 0) else "方向对、证据不够" if t >= 1 else "没有"
        yrs = np.asarray(ps.years)
        net = steer._daily_long_net(sm, tgt, slice(0, len(dates)))
        zk = dg._zrank(usr)
        ok = np.isfinite(zk[::5]) & np.isfinite(ref[::5])
        a, b = np.where(ok, zk[::5], 0.0), np.where(ok, ref[::5], 0.0)
        n = np.maximum(ok.sum(1), 1)
        with np.errstate(invalid="ignore", divide="ignore"):
            rk = float(np.nanmean(((a * b).sum(1) - a.sum(1) * b.sum(1) / n) / np.sqrt(((a ** 2).sum(1) - a.sum(1) ** 2 / n) * ((b ** 2).sum(1) - b.sum(1) ** 2 / n))))
        return {**p, "kind": "level", "reproduces_search": bool(rep), "t_holdout": float(t), "verdict": verdict, "rho_known": rk,
                "t_forward": float(rows["forward"]["long_sharpe"] * np.sqrt(years_fw)) if HAS_FW else None,
                "t_oos": float(rows["oos"]["long_sharpe"] * np.sqrt(years_oos)) if HAS_FW else None,
                "book": {k: {x: v[x] for x in ("long_ann", "long_sharpe", "long_mdd", "long_turnover")} for k, v in rows.items()},
                "book_user_convention": {k: {x: v[x] for x in ("long_ann", "long_sharpe", "long_mdd", "long_turnover")} for k, v in urows.items()},
                "paired_vs_known_user_convention": S, "by_year": {str(y): float(np.nanmean(net[yrs == y]) * 252) for y in sorted(set(yrs))}}

    for i, p in enumerate(picks):
        if p["reward"] != "long_screen":
            out.append(level(i, p))
            continue
        ref = bases[p["base"]]
        fin = np.isfinite(ref)
        cut = int(np.searchsorted(dates, p["split"]))
        tr, va = slice(us.start, cut), slice(cut, us.stop)
        sm0 = bk.smoothed(np.asarray(P[f"c{i}"], np.float64), float(p["hl"]))
        band = steer._top_band(np.where(fin, float(p["sign"]) * sm0, np.nan))
        scr = np.where(fin, np.where(band, ref - 2.0, ref), np.nan)
        d = {nm: steer._daily_long_net(scr, tgt, sl) - steer._daily_long_net(ref, tgt, sl) for nm, sl in (("train", tr), ("valid", va), ("utrain", us), ("holdout", ho)) + ((("forward", fw),) if HAS_FW else ())}
        if HAS_FW:
            d["oos"] = np.concatenate([d["holdout"], d["forward"]])
        S = {nm: stats(x) for nm, x in d.items()}
        rep = abs(S["train"]["ann"] - p["dann_train"]) < 2e-3 and abs(S["valid"]["ann"] - p["dann_valid"]) < 3e-3        # the search's last days have no label yet
        books = {nm: bk.book_row(scr, tgt, sl) for nm, sl in (("utrain", us), ("holdout", ho))}
        refb = {nm: bk.book_row(ref, tgt, sl) for nm, sl in (("utrain", us), ("holdout", ho))}
        yrs = np.asarray(ps.years)
        by = {str(y): float(np.nanmean((steer._daily_long_net(scr, tgt, slice(0, len(dates))) - steer._daily_long_net(ref, tgt, slice(0, len(dates))))[yrs == y]) * 252) for y in sorted(set(yrs))}
        t = S["holdout"]["t"]
        verdict = "成立" if (t >= 2 and S["utrain"]["ann"] > 0) else "方向对、证据不够" if t >= 1 else "没有"
        out.append({**p, "kind": "screen", "paired": S, "reproduces_search": bool(rep), "book": {k: {x: v[x] for x in ("long_ann", "long_sharpe", "long_mdd", "long_turnover")} for k, v in books.items()},
                    "reference_book": {k: {x: v[x] for x in ("long_ann", "long_sharpe")} for k, v in refb.items()}, "by_year_diff": by, "verdict": verdict,
                    "screened_share_holdout": float(band[ho].sum() / max(fin[ho].sum(), 1))})
    mem.stop()

p_out = PARTURA_ROOT / (opt("--out") or f"episodes/{'_'.join(sorted({p['episode'].split('_')[0] for p in picks}))}_final.json")
p_out.write_text(json.dumps({"rule": __doc__.split("    python")[0].strip(), "splits": {k: list(SPLITS[k]) for k in ("utrain", "holdout")}, "results": out}, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
lv = [r for r in out if r["kind"] == "level"]
if lv:
    print(f"\n{'run/arm':16s} sg hl | 复现搜索 | 奖励口径的书: 样本内 净超额 / 夏普 | 样本外 净超额 / 夏普 / t | 判读 | 用户口径: 样本内 → 样本外(夏普) | 减已知族 样本外 多赚 / t | ρ已知 | 逐年")
    for r in lv:
        b, u, S = r["book"], r["book_user_convention"], r["paired_vs_known_user_convention"]
        print(f"{r['episode'].split('_')[0] + '/' + r['arm']:16s} {int(r['sign']):+d} {r['hl']:>2g} | {'是' if r['reproduces_search'] else '否!'}      | {b['utrain']['long_ann']:+.1%} / {b['utrain']['long_sharpe']:.2f} | "
              f"{b['holdout']['long_ann']:+.1%} / {b['holdout']['long_sharpe']:.2f} / t {r['t_holdout']:+.1f} | {r['verdict']} | {u['utrain']['long_ann']:+.1%} → {u['holdout']['long_ann']:+.1%} ({u['utrain']['long_sharpe']:.2f} → {u['holdout']['long_sharpe']:.2f}) | "
              f"{S['holdout']['ann']:+.1%} / t {S['holdout']['t']:+.1f} | {r['rho_known']:+.2f} | " + " ".join(f"{v:+.0%}" for v in r["by_year"].values()))
        if r.get("t_forward") is not None:
            print(f"{'':16s} 前推段({dates[fw.start]}~{dates[-1]}): 奖励口径 {b['forward']['long_ann']:+.1%} / {b['forward']['long_sharpe']:.2f} / t {r['t_forward']:+.1f};合并段 {b['oos']['long_ann']:+.1%} / {b['oos']['long_sharpe']:.2f} / t {r['t_oos']:+.1f};"
                  f"用户口径 前推段 {u['forward']['long_ann']:+.1%} / {u['forward']['long_sharpe']:.2f};减已知族 前推段 {S['forward']['ann']:+.1%} / t {S['forward']['t']:+.1f},合并段 {S['oos']['ann']:+.1%} / t {S['oos']['t']:+.1f}")
        print(f"{'':16s} {r['expr'][:170]}")
out_screen = [r for r in out if r["kind"] == "screen"]
if out_screen:
    print(f"\n{'run/arm':16s} sg hl | 复现搜索 | 账面每年多赚 train / valid | 样本内 多赚 / IR | 样本外 多赚 / IR / t | 判读 | 筛过的书 样本外 净超额 / 夏普(参照) | 逐年差")
for r in out_screen:
    S = r["paired"]
    print(f"{r['episode'].split('_')[0] + '/' + r['arm']:16s} {int(r['sign']):+d} {r['hl']:>2g} | {'是' if r['reproduces_search'] else '否!'}      | {S['train']['ann']:+.1%} / {S['valid']['ann']:+.1%} (搜索记的 {r['dann_train']:+.1%} / {r['dann_valid']:+.1%}) | "
          f"{S['utrain']['ann']:+.1%} / {S['utrain']['ir']:+.2f} | {S['holdout']['ann']:+.1%} / {S['holdout']['ir']:+.2f} / t {S['holdout']['t']:+.1f} | {r['verdict']} | "
          f"{r['book']['holdout']['long_ann']:+.1%} / {r['book']['holdout']['long_sharpe']:.2f} ({r['reference_book']['holdout']['long_ann']:+.1%} / {r['reference_book']['holdout']['long_sharpe']:.2f}) | "
          + " ".join(f"{v:+.1%}" for v in r["by_year_diff"].values()))
    if "forward" in S:
        print(f"{'':16s} 前推段 多赚 {S['forward']['ann']:+.1%} / IR {S['forward']['ir']:+.2f} / t {S['forward']['t']:+.1f};合并段 {S['oos']['ann']:+.1%} / t {S['oos']['t']:+.1f}")
    print(f"{'':16s} {r['expr'][:170]}")
print(f"\nwrote {p_out} ({time.time() - t0:.0f}s)")
