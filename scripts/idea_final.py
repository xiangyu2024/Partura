"""The test-period read of what an idea search found -- the SAME object the search selected, by a rule written before.

Server.  For every given episode (episodes/<name>/evidence.json) and each arm, takes the find with the highest
score (partura.steer.is_discovery; an arm without a find is not read) and rebuilds, on the full period, exactly the
book the reward scored: for ``long_screen`` the base signal with the candidate's top fifth (whole tie blocks, at the
direction and half-life the search chose) sent below everything.  It first checks that this book reproduces the
search's own numbers on train and on valid, then reports the paired daily difference against the base book in
sample and on the holdout (annualised, information ratio, t).  The read is ledgered.

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
    if E["reward"] != "long_screen":
        raise SystemExit(f"{name}: reward {E['reward']} -- only the screen reward is rebuilt here")
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
            picks.append({"episode": name, "arm": arm, "base": E.get("screen_base") or "known", "split": E["period"][2], **{k: c.get(k) for k in
                          ("expr", "sign", "hl", "score", "s_train", "s_valid", "dann_train", "dann_valid", "ir_train", "ir_valid", "share")}})
            if len(seen) >= TOP:
                break
print(f"[idea-final] {len(picks)} finds to read (top {TOP} per arm and run): " + ", ".join(f"{p['episode'].split('_')[0]}/{p['arm']}" for p in picks), flush=True)
if not picks:
    raise SystemExit(0)

with slot():
    mem = MemoryGuard(self_limit_gb=34, cgroup_limit_gb=70).start()
    t0 = time.time()
    ps = PanelSet("/root/autodl-tmp/qmt_daily_data/fast_factor_compute", SPLITS["full"][0], SPLITS["full"][1], warmup=int(cfg.get("warmup", 60)),
                  device="cuda", gpu_fraction=0, cache_dir=str(SHARED_CACHE), mirror_root="/root/autodl-tmp/AlphaCube/mirror",
                  workdir=str(PARTURA_ROOT / "tmp"), label_kind="open_vwap15", label_buyable=True, batch=8)
    G = steer.Guidance.load(PARTURA_ROOT / "guidance" / "B01.yaml")
    pool_spec, known_spec = G.spec["pool"][-1], G.spec["pool"][0]
    P = ps.compute({"known": known_spec["expr"], "pool": pool_spec["expr"], **{f"c{i}": p["expr"] for i, p in enumerate(picks)}})
    tgt = ps.target(1)
    dates = np.asarray(ps.dates)
    us, ho = ps.split_slice("utrain"), ps.split_slice("holdout")
    bases = {"known": dg._zrank(float(known_spec["sign"]) * np.asarray(P["known"], np.float64)),
             "pool": dg._zrank(bk.smoothed(float(pool_spec["sign"]) * np.asarray(P["pool"], np.float64), float(pool_spec["hl"])))}

    def stats(d):
        f = d[np.isfinite(d)]
        if f.size < 20 or not f.std() > 0:
            return {"ann": float("nan"), "ir": float("nan"), "t": float("nan"), "n": int(f.size)}
        return {"ann": float(f.mean() * 252), "ir": float(f.mean() / f.std() * np.sqrt(252)), "t": float(f.mean() / f.std() * np.sqrt(f.size)), "n": int(f.size)}

    Ledger(PARTURA_ROOT / "runs" / "_ideas" / "ledger.json").record(
        "holdout", len(picks), "idea searches: the top find of each arm and run, rebuilt exactly as scored (" + ", ".join(f"{p['episode']}/{p['arm']}" for p in picks) + ")",
        "idea_final_" + "_".join(sorted({p["episode"].split("_")[0] for p in picks})))
    out = []
    for i, p in enumerate(picks):
        ref = bases[p["base"]]
        fin = np.isfinite(ref)
        cut = int(np.searchsorted(dates, p["split"]))
        tr, va = slice(us.start, cut), slice(cut, us.stop)
        sm0 = bk.smoothed(np.asarray(P[f"c{i}"], np.float64), float(p["hl"]))
        band = steer._top_band(np.where(fin, float(p["sign"]) * sm0, np.nan))
        scr = np.where(fin, np.where(band, ref - 2.0, ref), np.nan)
        d = {nm: steer._daily_long_net(scr, tgt, sl) - steer._daily_long_net(ref, tgt, sl) for nm, sl in (("train", tr), ("valid", va), ("utrain", us), ("holdout", ho))}
        S = {nm: stats(x) for nm, x in d.items()}
        rep = abs(S["train"]["ann"] - p["dann_train"]) < 2e-3 and abs(S["valid"]["ann"] - p["dann_valid"]) < 3e-3        # the search's last days have no label yet
        books = {nm: bk.book_row(scr, tgt, sl) for nm, sl in (("utrain", us), ("holdout", ho))}
        refb = {nm: bk.book_row(ref, tgt, sl) for nm, sl in (("utrain", us), ("holdout", ho))}
        yrs = np.asarray(ps.years)
        by = {str(y): float(np.nanmean((steer._daily_long_net(scr, tgt, slice(0, len(dates))) - steer._daily_long_net(ref, tgt, slice(0, len(dates))))[yrs == y]) * 252) for y in sorted(set(yrs))}
        t = S["holdout"]["t"]
        verdict = "成立" if (t >= 2 and S["utrain"]["ann"] > 0) else "方向对、证据不够" if t >= 1 else "没有"
        out.append({**p, "paired": S, "reproduces_search": bool(rep), "book": {k: {x: v[x] for x in ("long_ann", "long_sharpe", "long_mdd", "long_turnover")} for k, v in books.items()},
                    "reference_book": {k: {x: v[x] for x in ("long_ann", "long_sharpe")} for k, v in refb.items()}, "by_year_diff": by, "verdict": verdict,
                    "screened_share_holdout": float(band[ho].sum() / max(fin[ho].sum(), 1))})
    mem.stop()

p_out = PARTURA_ROOT / (opt("--out") or f"episodes/{'_'.join(sorted({p['episode'].split('_')[0] for p in picks}))}_final.json")
p_out.write_text(json.dumps({"rule": __doc__.split("    python")[0].strip(), "splits": {k: list(SPLITS[k]) for k in ("utrain", "holdout")}, "results": out}, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
print(f"\n{'run/arm':16s} sg hl | 复现搜索 | 账面每年多赚 train / valid | 样本内 多赚 / IR | 样本外 多赚 / IR / t | 判读 | 筛过的书 样本外 净超额 / 夏普(参照) | 逐年差")
for r in out:
    S = r["paired"]
    print(f"{r['episode'].split('_')[0] + '/' + r['arm']:16s} {int(r['sign']):+d} {r['hl']:>2g} | {'是' if r['reproduces_search'] else '否!'}      | {S['train']['ann']:+.1%} / {S['valid']['ann']:+.1%} (搜索记的 {r['dann_train']:+.1%} / {r['dann_valid']:+.1%}) | "
          f"{S['utrain']['ann']:+.1%} / {S['utrain']['ir']:+.2f} | {S['holdout']['ann']:+.1%} / {S['holdout']['ir']:+.2f} / t {S['holdout']['t']:+.1f} | {r['verdict']} | "
          f"{r['book']['holdout']['long_ann']:+.1%} / {r['book']['holdout']['long_sharpe']:.2f} ({r['reference_book']['holdout']['long_ann']:+.1%} / {r['reference_book']['holdout']['long_sharpe']:.2f}) | "
          + " ".join(f"{v:+.1%}" for v in r["by_year_diff"].values()))
    print(f"{'':16s} {r['expr'][:170]}")
print(f"\nwrote {p_out} ({time.time() - t0:.0f}s)")
