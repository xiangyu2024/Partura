"""C07 (research/coldstart_C07/PLAN.md §2.3): the verifier's material for every seed -- in sample only.  Server, after every seed's
M and A runs have ended (and the old server's runs have been copied here).

L_A(s) = M batches 1..4 then A rounds 1..3 (c05_lib.heads, in that order).  For every head: expression, direction, half-life,
train (and valid) net Sharpe as recorded by its run, its daily-rank |rho| with every other head (top 3) and with the five controls
(train, every 5th day).  -> research/coldstart_C07/screen/s<seed>.json, s<seed>_train.md (V_tr), s<seed>_all.md (V_all)

    python scripts/c07_screen_prep.py [seeds]
"""
import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.guard import MemoryGuard, limit_threads, slot  # noqa: E402

limit_threads(8)
import numpy as np  # noqa: E402

from partura import diagnose as dg  # noqa: E402
from partura import ops_ext  # noqa: E402,F401
from partura import steer  # noqa: E402
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.panels import SHARED_CACHE, PanelSet  # noqa: E402

sys.path.insert(0, str(PARTURA_ROOT / "scripts"))
import c05_lib  # noqa: E402

D, EP = PARTURA_ROOT / "research" / "coldstart_C07", PARTURA_ROOT / "episodes"
OUT = D / "screen"
OUT.mkdir(parents=True, exist_ok=True)
SEEDS = [int(x) for x in (sys.argv[1:] or "801 802 803 804 805 806 807 808".split())]
STORE = os.environ.get("PARTURA_STORE", "/root/autodl-tmp/qmt_daily_data/fast_factor_compute")
MIRROR = os.environ.get("PARTURA_MIRROR", "/root/autodl-tmp/AlphaCube/mirror")
MIRROR = MIRROR if MIRROR and os.path.isdir(MIRROR) else None

with slot():
    mem = MemoryGuard(self_limit_gb=int(os.environ.get("PARTURA_SELF_LIMIT_GB", 60)), cgroup_limit_gb=int(os.environ.get("PARTURA_CGROUP_LIMIT_GB", 80))).start()
    t0 = time.time()
    from alphacube.plugins import load_plugins
    load_plugins(["partura.ac_plugin"])
    ps = PanelSet(STORE, "20180102", "20230807", warmup=60, device="cuda", gpu_fraction=0.9, cache_dir=str(SHARED_CACHE), mirror_root=MIRROR,
                  workdir=str(PARTURA_ROOT / "tmp"), label_kind="open_vwap15", label_buyable=True, batch=8,
                  daily_root=os.environ.get("PARTURA_DAILY_ROOT") or None)
    G = steer.Guidance.load(PARTURA_ROOT / "guidance" / "C05_base.yaml")
    CTRL = {"liquidity": "cross_mean(day_sum(Amt), 30)", "volatility": "cross_mean(day_std(Ret), 20)",
            "reversal": "div(day_last(Close), ts_delay(day_last(Close), 20))", "known": G.spec["pool"][0]["expr"], "size": "LogFloatCap"}
    aux = ps.compute(CTRL)
    dates = np.asarray(ps.dates).astype(str)
    cut = int(np.searchsorted(dates, "20220101"))
    CZ = {k: dg._zrank(np.asarray(v, np.float64))[:cut:5] for k, v in aux.items()}

    def rho(a, b):
        ok = np.isfinite(a) & np.isfinite(b)
        x, y = np.where(ok, a, 0.0), np.where(ok, b, 0.0)
        n = np.maximum(ok.sum(1), 1)
        with np.errstate(invalid="ignore", divide="ignore"):
            c = ((x * y).sum(1) - x.sum(1) * y.sum(1) / n) / np.sqrt(((x ** 2).sum(1) - x.sum(1) ** 2 / n) * ((y ** 2).sum(1) - y.sum(1) ** 2 / n))
        return float(np.nan_to_num(np.nanmean(c)))

    for S in SEEDS:
        eps = [EP / f"c07s{S}M{e}_I0_open_search" for e in range(1, 5)]
        for k in (1, 2, 3):
            eps += sorted(Path(p) for p in __import__("glob").glob(str(EP / f"c07s{S}Ar{k}[ab]_*")) if (Path(p) / "evidence.json").is_file())
        heads, seen = [], set()
        for h in c05_lib.heads(eps):
            if h["expr"] not in seen:
                seen.add(h["expr"])
                heads.append(h)
        Z = {}
        for i in range(0, len(heads), 16):
            chunk = heads[i:i + 16]
            P = ps.compute({f"h{j}": h["expr"] for j, h in enumerate(chunk)})
            for j, h in enumerate(chunk):
                if f"h{j}" in P:
                    Z[h["expr"]] = dg._zrank(np.asarray(P[f"h{j}"], np.float64))[:cut:5]
        rows = []
        for n, h in enumerate(heads, 1):
            z = Z.get(h["expr"])
            others = sorted(((abs(rho(z, Z[g["expr"]])), m) for m, g in enumerate(heads, 1) if g["expr"] != h["expr"] and g["expr"] in Z), reverse=True)[:3] if z is not None else []
            rows.append({"id": n, "expr": h["expr"], "src": h["src"], "sign": h["sign"], "hl": h["hl"], "train": h["train"], "valid": h["valid"],
                         "top_heads": [[round(r, 3), m] for r, m in others],
                         "controls": {k: round(abs(rho(z, cz)), 3) for k, cz in CZ.items()} if z is not None else None})
        (OUT / f"s{S}.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
        for variant in ("train", "all"):
            L = [f"# 验证材料:种子 {S}({'只含 train' if variant == 'train' else 'train 与 valid'})", "",
                 f"候选因子库 {len(rows)} 个 head(主搜索第 1–4 批,然后补充搜索第 1–3 轮)。秩相关 |ρ| 用 train,每 5 天一天,不分方向。", "",
                 "| # | 来源 | 方向 | 半衰期 | train 夏普 |" + (" valid 夏普 |" if variant == "all" else "") + " 最像的其他 head(\\|ρ\\|, #) | 流动性 | 波动 | 反转 | 已知族 | 市值 | 表达式 |",
                 "|---|---|---|---|---|" + ("---|" if variant == "all" else "") + "---|---|---|---|---|---|---|"]
            for r in rows:
                c = r["controls"] or {}
                th = ", ".join(f"{v:.2f} (#{m})" for v, m in r["top_heads"]) or "—"
                cs = " | ".join(f"{c.get(k, float('nan')):.2f}" for k in ("liquidity", "volatility", "reversal", "known", "size"))
                L.append(f"| {r['id']} | {r['src'].split('_')[0]} | {r['sign']:+.0f} | {r['hl']:g} | {r['train']:+.2f} |"
                         + (f" {r['valid']:+.2f} |" if variant == "all" else "") + f" {th} | {cs} | `{r['expr']}` |")
            (OUT / f"s{S}_{variant}.md").write_text("\n".join(L) + "\n", encoding="utf-8")
        print(f"[screen] s{S}: {len(rows)} heads ({time.time() - t0:.0f}s)", flush=True)
    mem.stop()
