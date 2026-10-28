"""C02: evaluate Partura's hypotheses DIRECTLY -- every variant scored once, no GP (research/coldstart_C02/PLAN.md §2.4).

Server.  Reads research/coldstart_C02/hypotheses_r<k>.yaml (hypotheses -> variants), scores every variant on the search
view with the same reward and the same environment rules as the GP (scripts/idea_search.py + partura/ac_plugin.py):
reward ``long`` (score = the worse of train / valid pure-long Sharpe, direction and half-life chosen on train), the gates
(coverage of labelled cells >= 0.9, distinct fraction >= 0.5), and the rejection by measured correlation with the known
family (|rho| >= $PARTURA_RHO_REJECT, the scorer's own measure).  Each variant is one paid evaluation of arm B.

    python scripts/c02_direct.py <k>     -> research/coldstart_C02/direct_r<k>.json and .md
"""
import json
import math
import os
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
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.panels import SHARED_CACHE, PanelSet  # noqa: E402
from partura.steer import Guidance, RewardContext  # noqa: E402
from partura.steer import reward as steer_reward  # noqa: E402

K = int(sys.argv[1])
D = PARTURA_ROOT / "research" / os.environ.get("PARTURA_STUDY_DIR", "coldstart_C02")
KIND = os.environ.get("PARTURA_REWARD_KIND", "long")
H = yaml.safe_load((D / f"hypotheses_r{K}.yaml").read_text(encoding="utf-8"))
START, END, SPLIT = "20180102", "20230807", "20220101"
STORE = os.environ.get("PARTURA_STORE", "/root/autodl-tmp/qmt_daily_data/fast_factor_compute")
MIRROR = os.environ.get("PARTURA_MIRROR", "/root/autodl-tmp/AlphaCube/mirror")
MIRROR = MIRROR if MIRROR and os.path.isdir(MIRROR) else None      # a host without the D-major mirror reads the store itself
THR = float(os.environ.get("PARTURA_THRESHOLD", 0.7))
RHO = float(os.environ.get("PARTURA_RHO_REJECT", "0.5"))
G = Guidance.load(PARTURA_ROOT / "guidance" / os.environ.get("PARTURA_BASE_GUIDANCE", "C02_base.yaml"))

rows = []
for h in H["hypotheses"]:
    for v in h["variants"]:
        rows.append({"hypothesis": h["id"], "variant": v["id"], "role": v.get("role", "core"), "expr": v["expr"], "predicts": v.get("predicts", "")})
print(f"[direct] {len(H['hypotheses'])} hypotheses, {len(rows)} variants = {len(rows)} paid evaluations of arm B", flush=True)

with slot():
    mem = MemoryGuard(self_limit_gb=34, cgroup_limit_gb=70).start()
    t0 = time.time()
    from alphacube.plugins import load_plugins
    load_plugins(["partura.ac_plugin"])
    ps = PanelSet(STORE, START, END, warmup=60, device="cuda", gpu_fraction=0.4, cache_dir=str(SHARED_CACHE), mirror_root=MIRROR,
                  workdir=str(PARTURA_ROOT / "tmp"), label_kind="open_vwap15", label_buyable=True, batch=8)
    pool_spec, known_spec = G.spec["pool"][-1], G.spec["pool"][0]
    aux = ps.compute({"frozen": "cross_max(day_zero_ratio(Ret), 15)", "age": "cross_valid_count(day_last(Close), 241)",
                      "liq": "cross_mean(day_sum(Amt), 30)", "pool": pool_spec["expr"], "known": known_spec["expr"]})
    tgt = ps.target(1)
    dates = np.asarray(ps.dates)
    cut = int(np.searchsorted(dates, SPLIT))
    tr, va = slice(0, cut), slice(cut, len(dates))
    frozen = np.asarray(aux["frozen"], np.float64)
    possible = np.minimum(241, np.arange(1, len(dates) + 1))[:, None]
    untradable = ((dg._zrank(frozen) + 0.5) > 0.8) | (np.asarray(aux["age"], np.float64) < 0.9 * possible) | ~np.isfinite(frozen)
    pool_sig = dg._zrank(bk.smoothed(float(pool_spec["sign"]) * np.asarray(aux["pool"], np.float64), float(pool_spec["hl"])))
    known_z = dg._zrank(float(known_spec["sign"]) * np.asarray(aux["known"], np.float64))
    ctx = RewardContext(tgt, tr, va, untradable=untradable, liq=np.asarray(aux["liq"], np.float64), pool=pool_sig, base=pool_sig, halflives=(0.0, 5.0, 20.0))
    if KIND == "long_neutral":
        from partura.steer import neutral_basis
        nq = ps.compute({"n_vol": "cross_mean(day_std(Ret), 20)", "n_rev": "div(day_last(Close), ts_delay(day_last(Close), 20))"})
        ctx.neutral_Q = neutral_basis([aux["liq"], nq["n_vol"], nq["n_rev"], aux["known"]])
    labelled = np.isfinite(tgt)
    kz = known_z[:cut:5]

    def rho_known(panel, sign):
        """The scorer's own measure (partura/ac_plugin.py ParturaScorer.score)."""
        z = dg._zrank(sign * np.asarray(panel[:cut:5], np.float64))
        ok = np.isfinite(z) & np.isfinite(kz)
        zc, kc = np.where(ok, z, 0.0), np.where(ok, kz, 0.0)
        n = np.maximum(ok.sum(1), 1)
        with np.errstate(invalid="ignore", divide="ignore"):
            c = ((zc * kc).sum(1) - zc.sum(1) * kc.sum(1) / n) / np.sqrt(((zc ** 2).sum(1) - zc.sum(1) ** 2 / n) * ((kc ** 2).sum(1) - kc.sum(1) ** 2 / n))
        return float(np.nanmean(c))

    for i in range(0, len(rows), 8):
        chunk = rows[i:i + 8]
        try:
            P = ps.compute({f"v{j}": r["expr"] for j, r in enumerate(chunk)})
        except Exception as exc:                              # noqa: BLE001  (one bad batch must not lose the others)
            P = {}
            for j, r in enumerate(chunk):
                try:
                    P.update({f"v{j}": ps.compute({"x": r["expr"]})["x"]})
                except Exception as e2:                       # noqa: BLE001
                    r["error"] = f"{type(e2).__name__}: {str(e2)[:160]}"
        for j, r in enumerate(chunk):
            if f"v{j}" not in P:
                r.setdefault("error", "did not compute")
                continue
            panel = np.asarray(P[f"v{j}"], np.float64)
            cov = float(np.isfinite(panel[labelled]).mean())
            dist = dg.distinct_fraction(panel)
            r.update(coverage=cov, distinct=dist, gate=bool(cov >= 0.9 and dist >= 0.5))
            if not r["gate"]:
                continue
            rw = steer_reward(panel, ctx, KIND)
            r.update(score=rw["score"], s_train=rw["score_train"], s_valid=rw["score_valid"], sign=rw["sign"], hl=rw["hl"],
                     train=rw["train"]["long_sharpe"], valid=rw["valid"]["long_sharpe"], train_ann=rw["train"]["long_ann"],
                     valid_ann=rw["valid"]["long_ann"], turnover=rw["train"]["long_turnover"], rho_known=rho_known(panel, rw["sign"]))
            r["rejected"] = bool(math.isfinite(r["rho_known"]) and abs(r["rho_known"]) >= RHO)
            r["discovery"] = bool(math.isfinite(r["score"]) and r["score"] >= THR and not r["rejected"])
        print(f"[direct] {min(i + 8, len(rows))}/{len(rows)} ({time.time() - t0:.0f}s)", flush=True)
    mem.stop()

out = {"round": K, "n_paid": len(rows), "threshold": THR, "rho_reject": RHO, "rows": rows, "seconds": time.time() - t0}
(D / f"direct_r{K}.json").write_text(json.dumps(out, ensure_ascii=False, indent=1, default=float), encoding="utf-8")


def f(x, nd=2):
    return f"{x:+.{nd}f}" if isinstance(x, (int, float)) and math.isfinite(x) else "—"


L = [f"# C02 直接检验(第 {K} 轮):{len(H['hypotheses'])} 个假设、{len(rows)} 个变体(= B 组 {len(rows)} 次付费评估)", "",
     f"score = 纯多头十分位书扣 15bp 的 train 与 valid 夏普中较差的;发现 = score ≥ {THR} 且未被相关度拒绝(|ρ已知| ≥ {RHO});门槛:覆盖率 ≥ 0.9、取值离散度 ≥ 0.5。", ""]
for h in H["hypotheses"]:
    L += [f"## {h['id']}", "", f"> {str(h.get('thesis', {}).get('mechanism', h.get('hypothesis', '')))[:400]}", "",
          "| 变体 | 角色 | score | train | valid | 方向 | 半衰期 | 换手 | ρ已知 | 结果 | 表达式 |", "|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in [x for x in rows if x["hypothesis"] == h["id"]]:
        res = ("错误" if r.get("error") else "门槛废品" if not r.get("gate") else "被相关度拒绝" if r.get("rejected") else "**发现**" if r.get("discovery") else "未过线")
        L.append(f"| {r['variant']} | {r['role']} | {f(r.get('score'))} | {f(r.get('train'))} | {f(r.get('valid'))} | {r.get('sign', '—')} | {r.get('hl', '—')} | "
                 f"{f(r.get('turnover'), 3)} | {f(r.get('rho_known'))} | {res} | `{r['expr']}` |")
    L.append("")
(D / f"direct_r{K}.md").write_text("\n".join(L) + "\n", encoding="utf-8")
print(f"wrote {D / f'direct_r{K}.md'}: {sum(r.get('discovery', False) for r in rows)} discoveries of {len(rows)} ({time.time() - t0:.0f}s)")
