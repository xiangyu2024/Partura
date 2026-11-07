"""PROD W01: the wave's libraries and fused books (research/prod_W01/PLAN.md sections 1, 4, 5).  New server, after every seed's rounds
have ended and the old server's seeds have been copied here (scripts/prod_gather.sh).  Source tmp/prod_env.sh first.

For every seed s (901-912, research/prod_W01/hosts.json):
    M(s) = the heads of the seed's M batches 1..4;  P(s) = M's heads (R replacements followed to the end of the chain) + Partura's extra
    heads of rounds 1..3 + R accessions.  Both greedily deduplicated (C05 PLAN section 3; scripts/prod_lib.py, the logic of c08_final.py),
    one equal-weight z-rank fused book each, neutralised once more on the 16-column basis like every single head.
The whole wave: the pooled P(s) (and M(s)) deduplicated again across seeds, in descending in-sample score, one fused book each; the
P fused signal panel is saved as a .npy (runs/prod_W01/wave_fused.npy, path in final.json).
Every choice here -- which heads, their order, the dedup -- uses train (2018-2021) and valid (2022-01 .. 2023-08-07) only.
The test period (2023-08-08 .. 2025-12-31) and the forward segment (2026-01-01 ..) are computed AFTER the libraries are fixed and are
DESCRIPTION ONLY: they are recorded in research/prod_W01/ledger_prod.json (like C08's ledger) and select nothing.

    python scripts/prod_final.py --dry-run [--seeds 901,902] [--gpu-fraction 0.9]
        in-sample only: libraries, in-sample fused books, reproduction check; nothing out of sample is evaluated, ledgered or saved
        (the panels are computed on the full data view, as c08_final.py's dry run does, so that the real run finds them in the shared
        cache; no statistic of a day after 2023-08-07 is computed).  -> final_dry.json, library_dry.json, final_dry.md
    python scripts/prod_final.py [--again] [--gpu-fraction 0.9]
        all seeds, every seed's arms/s<seed>.ALLDONE required.  -> final.json, library.json, final.md, runs/prod_W01/wave_fused.npy
        A second real run is refused unless --again (it is recorded in the ledger again).
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

from partura import books as bk  # noqa: E402
from partura import diagnose as dg  # noqa: E402
from partura import ops_ext  # noqa: E402,F401
from partura import steer  # noqa: E402
from partura import study  # noqa: E402
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.panels import SHARED_CACHE, PanelSet  # noqa: E402
from partura.splits import Ledger  # noqa: E402

sys.path.insert(0, str(PARTURA_ROOT / "scripts"))
import c05_lib  # noqa: E402
import prod_hosts  # noqa: E402
import prod_lib  # noqa: E402

argv = sys.argv[1:]
DRY = "--dry-run" in argv
AGAIN = "--again" in argv
os.environ.setdefault("PARTURA_REPROMOTE", "1")                # C05 PLAN revision 7
GPU = float(argv[argv.index("--gpu-fraction") + 1]) if "--gpu-fraction" in argv else 0.4
if study.name("") != "PROD":
    raise SystemExit("source tmp/prod_env.sh first (PARTURA_C0X=PROD)")
if not steer.rank_first() or os.environ.get("PARTURA_NEUTRAL_POWERS") != "1,2,3":
    raise SystemExit("PROD is read under the new ruler: source tmp/prod_env.sh")
DIRNAME = study.dirname("PROD")
D, EP = PARTURA_ROOT / "research" / DIRNAME, PARTURA_ROOT / "episodes"
LEDGER = D / "ledger_prod.json"
PFX = study.prefix("PROD")
ALL_SEEDS = prod_hosts.seeds(prod_hosts.load(D / "hosts.json"))
SEEDS = [int(x) for x in argv[argv.index("--seeds") + 1].split(",")] if "--seeds" in argv else ALL_SEEDS
if "--seeds" in argv and not DRY:
    raise SystemExit("--seeds only goes with --dry-run: the real read covers the whole wave")
unknown = [s for s in SEEDS if s not in ALL_SEEDS]
if unknown:
    raise SystemExit(f"seeds {unknown} are not in {D / 'hosts.json'}")
if not DRY:
    unfinished = [s for s in SEEDS if not (D / "arms" / f"s{s}.ALLDONE").is_file()]
    if unfinished:
        raise SystemExit(f"seeds {unfinished} have no arms/s<seed>.ALLDONE: not finished (or not gathered from the old host)")
    if Ledger(LEDGER).summary().get("holdout") and not AGAIN:
        raise SystemExit(f"the test period has already been described by this study ({LEDGER}); --again to do it once more (it is ledgered again)")
STORE = os.environ.get("PARTURA_STORE", "/root/autodl-tmp/qmt_daily_data/fast_factor_compute")
MIRROR = os.environ.get("PARTURA_MIRROR", "/root/autodl-tmp/AlphaCube/mirror")
MIRROR = MIRROR if MIRROR and os.path.isdir(MIRROR) else None
SUFFIX = "_dry" if DRY else ""

# ------------------------------------------------------------------ the libraries (evidence files and R files only)
LIB, MISS = {}, []
EVALS, GPUSEC = {"M": 0, "P": 0}, {"M": 0.0, "P": 0.0}
REPL = {}
for S in SEEDS:
    r = prod_lib.seed_library(S, EP, D, c05_lib, pfx=PFX)
    LIB[(S, "M")], LIB[(S, "P")] = r["M"], r["P"]
    MISS += r["missions"]
    for X in ("M", "P"):
        EVALS[X] += r["evals"][X]
        GPUSEC[X] += r["gpu_seconds"][X]
    REPL[S] = len(r["replacements"])
uniq = sorted({h["expr"] for v in LIB.values() for h in v})
print(f"[prod] {len(SEEDS)} seeds; libraries before dedup: M {sum(len(LIB[(S, 'M')]) for S in SEEDS)}, P {sum(len(LIB[(S, 'P')]) for S in SEEDS)}; "
      f"{len(uniq)} distinct expressions; evaluations {EVALS}; replacements in force {sum(REPL.values())}", flush=True)

with slot():
    mem = MemoryGuard(self_limit_gb=int(os.environ.get("PARTURA_SELF_LIMIT_GB", 60)), cgroup_limit_gb=int(os.environ.get("PARTURA_CGROUP_LIMIT_GB", 80))).start()
    t0 = time.time()
    from alphacube.plugins import load_plugins
    from alphacube.store import open_cube_store
    load_plugins(["partura.ac_plugin"])
    END = str(open_cube_store(STORE, mirror_root=MIRROR).dates[-1])
    ps = PanelSet(STORE, "20180102", END, warmup=60, device="cuda", gpu_fraction=GPU, cache_dir=str(SHARED_CACHE), mirror_root=MIRROR,
                  workdir=str(PARTURA_ROOT / "tmp"), label_kind="open_vwap15", label_buyable=True, batch=8,
                  daily_root=os.environ.get("PARTURA_DAILY_ROOT") or None)
    G = steer.Guidance.load(PARTURA_ROOT / "guidance" / "C05_base.yaml")
    known_spec = G.spec["pool"][0]
    aux = ps.compute({"known": known_spec["expr"], "liq": "cross_mean(day_sum(Amt), 30)", "vol": "cross_mean(day_std(Ret), 20)",
                      "rev": "div(day_last(Close), ts_delay(day_last(Close), 20))", "size": "LogFloatCap"})
    tgt = ps.target(1)
    dates = np.asarray(ps.dates).astype(str)
    ix = lambda d: int(np.searchsorted(dates, d))                       # noqa: E731
    tr, va = slice(0, ix("20220101")), slice(ix("20220101"), ix("20230808"))
    ho, fw = slice(ix("20230808"), ix("20260101")), slice(ix("20260101"), len(dates))
    years_ho = float(np.isfinite(tgt[ho]).any(1).sum()) / 252.0
    years_fw = float(np.isfinite(tgt[fw]).any(1).sum()) / 252.0
    kz = dg._zrank(float(known_spec["sign"]) * np.asarray(aux["known"], np.float64))[:tr.stop:5]
    QF = steer.neutral_basis([aux["liq"], aux["vol"], aux["rev"], aux["known"], aux["size"]])
    print(f"[prod] view {dates[0]}..{END}: test {ho.stop - ho.start} days ({years_ho:.2f} y), forward {fw.stop - fw.start} ({years_fw:.2f} y)", flush=True)

    def rho(a, b):
        ok = np.isfinite(a) & np.isfinite(b)
        x, y = np.where(ok, a, 0.0), np.where(ok, b, 0.0)
        n = np.maximum(ok.sum(1), 1)
        with np.errstate(invalid="ignore", divide="ignore"):
            c = ((x * y).sum(1) - x.sum(1) * y.sum(1) / n) / np.sqrt(((x ** 2).sum(1) - x.sum(1) ** 2 / n) * ((y ** 2).sum(1) - y.sum(1) ** 2 / n))
        return float(np.nanmean(c))

    sign_hl = {}
    for v in LIB.values():
        for h in v:
            sign_hl.setdefault(h["expr"], (float(h["sign"]), float(h["hl"])))
    SM, Z = {}, {}
    for i in range(0, len(uniq), 16):
        chunk = uniq[i:i + 16]
        P = ps.compute({f"c{j}": e for j, e in enumerate(chunk)})
        for j, e in enumerate(chunk):
            if f"c{j}" not in P:
                print(f"[prod] does not compute on the full view: {e}", flush=True)
                continue
            sg, hl = sign_hl[e]
            sm = steer.neutral_residual(sg * bk.smoothed(steer.signal_input(P[f"c{j}"]), hl), QF)
            SM[e], Z[e] = sm.astype(np.float32), dg._zrank(sm)[:tr.stop:5]
        print(f"[prod] rebuilt {min(i + 16, len(uniq))}/{len(uniq)} ({time.time() - t0:.0f}s)", flush=True)
    RK = {e: rho(Z[e], kz) for e in Z}

    def fuse(lst):
        return prod_lib.fuse([h["expr"] for h in lst], SM, dg._zrank, lambda a: steer.neutral_residual(a, QF))

    def book(fz, sl):
        if fz is None:
            return {"long_sharpe": 0.0, "long_ann": 0.0}
        r = bk.book_row(fz, tgt, sl)
        return {"long_sharpe": float(np.nan_to_num(r["long_sharpe"])), "long_ann": float(np.nan_to_num(r["long_ann"]))}

    def rows(fz):
        row = {"train": book(fz, tr), "valid": book(fz, va)}
        return row

    # ---------------------------------------------------------------- libraries: per seed, then the wave
    KEPT = {}
    for key, lst in LIB.items():
        KEPT[key] = prod_lib.dedup(lst, Z, RK, rho)
        for h in KEPT[key]:
            h["reproduces"] = bool(abs(bk.book_row(SM[h["expr"]].astype(np.float64), tgt, tr)["long_sharpe"] - h["train"]) < 0.05)
            h["rho_known"] = float(RK[h["expr"]])
    WAVE = {X: prod_lib.wave_library({S: KEPT[(S, X)] for S in SEEDS}, Z, RK, rho) for X in ("M", "P")}
    for X in ("M", "P"):
        for h in WAVE[X]:
            h["reproduces"] = next((g.get("reproduces") for g in KEPT[(h["seed"], X)] if g["expr"] == h["expr"]), None)
            h["rho_known"] = float(RK[h["expr"]])
    print(f"[prod] libraries after dedup: per seed M {sum(len(KEPT[(S, 'M')]) for S in SEEDS)}, P {sum(len(KEPT[(S, 'P')]) for S in SEEDS)}; "
          f"wave M {len(WAVE['M'])}, P {len(WAVE['P'])}; reproduce {sum(bool(h.get('reproduces')) for v in KEPT.values() for h in v)}/{sum(len(v) for v in KEPT.values())}", flush=True)

    # ---------------------------------------------------------------- fused books: in sample first
    FZ = {key: fuse(lst) for key, lst in KEPT.items()}
    FW = {X: fuse(WAVE[X]) for X in ("M", "P")}
    out = {"plan": f"research/{DIRNAME}/PLAN.md", "dry_run": DRY, "seeds": SEEDS, "view": [str(dates[0]), END],
           "periods": {"train": [str(dates[tr.start]), str(dates[tr.stop - 1])], "valid": [str(dates[va.start]), str(dates[va.stop - 1])],
                       "test": ["20230808", "20251231"], "forward": ["20260101", END]},
           "selection": "train + valid only; test and forward are description only (PLAN section 4)",
           "evaluations": EVALS, "gpu_seconds": GPUSEC, "missions": MISS, "replacements_in_force": REPL,
           "libraries": {"per_seed": {str(S): {X: len(KEPT[(S, X)]) for X in ("M", "P")} for S in SEEDS},
                         "before_dedup": {str(S): {X: len(LIB[(S, X)]) for X in ("M", "P")} for S in SEEDS},
                         "wave": {X: len(WAVE[X]) for X in ("M", "P")}},
           "per_seed": {}, "wave": {}, "r_additions": study.r_additions("PROD")}
    for S in SEEDS:
        out["per_seed"][str(S)] = {X: {"heads": len(KEPT[(S, X)]), **rows(FZ[(S, X)])} for X in ("M", "P")}
    for X in ("M", "P"):
        out["wave"][X] = {"heads": len(WAVE[X]), **rows(FW[X])}
    lib_json = {"plan": out["plan"], "dry_run": DRY, "seeds": SEEDS, "note": "in-sample numbers only (score = the worse of train / valid net Sharpe of the residual pure-long book)",
                "rule": {"known_family_abs_rho": prod_lib.RHO_KNOWN, "head_rho": prod_lib.RHO_HEAD, "head_rho_anti": prod_lib.RHO_ANTI},
                "per_seed": {str(S): {X: [prod_lib.head_row({**h, "seed": S}) for h in KEPT[(S, X)]] for X in ("M", "P")} for S in SEEDS},
                "wave": {X: [prod_lib.head_row(h) for h in WAVE[X]] for X in ("M", "P")}}

    if not DRY:
        # the libraries are fixed: from here on the out-of-sample periods are looked at, described, ledgered; nothing is selected by them
        n = len({h["expr"] for v in KEPT.values() for h in v} | {h["expr"] for X in WAVE for h in WAVE[X]})
        Ledger(LEDGER).record("holdout", n, f"PROD {DIRNAME} libraries (per seed M / P, wave M / P): test period 20230808..20251231, description only", "prod_final")
        Ledger(LEDGER).record("forward", n, f"PROD {DIRNAME} libraries: forward column 20260101..{END}, description only", "prod_final")
        out["years_test"], out["years_forward"] = years_ho, years_fw
        for S in SEEDS:
            for X in ("M", "P"):
                out["per_seed"][str(S)][X].update(test=book(FZ[(S, X)], ho), forward=book(FZ[(S, X)], fw))
        for X in ("M", "P"):
            out["wave"][X].update(test=book(FW[X], ho), forward=book(FW[X], fw))
        extra = []                                             # P's added heads (extra, R replacements, R accessions), each on its own
        for S in SEEDS:
            kept = {h["expr"] for h in KEPT[(S, "P")]}
            for h in LIB[(S, "P")]:
                if (h["role"] in ("M",) and not h.get("replaced")) or h["expr"] not in SM:
                    continue
                sm = SM[h["expr"]].astype(np.float64)
                r, rf = bk.book_row(sm, tgt, ho), bk.book_row(sm, tgt, fw)
                extra.append({"seed": S, "role": h["role"], "mission": h.get("mission"), "round": h.get("round"), "expr": h["expr"], "train": h["train"],
                              "valid": h["valid"], "in_library": h["expr"] in kept, "test_sharpe": float(np.nan_to_num(r["long_sharpe"])),
                              "forward_sharpe": float(np.nan_to_num(rf["long_sharpe"]))})
        out["extra_heads"] = extra
        panel = PARTURA_ROOT / "runs" / DIRNAME / "wave_fused.npy"
        panel.parent.mkdir(parents=True, exist_ok=True)
        if FW["P"] is not None:
            np.save(panel, FW["P"].astype(np.float32))
            panel.with_suffix(".meta.json").write_text(json.dumps({"shape": list(FW["P"].shape), "dtype": "float32", "dates": [str(x) for x in dates], "symbols": list(ps.symbols),
                                                                   "heads": [h["expr"] for h in WAVE["P"]], "note": "equal-weight z-rank fusion of the wave's P library, re-neutralised; rows = dates, columns = symbols"},
                                                                  ensure_ascii=False), encoding="utf-8")
        out["wave_signal_panel"] = {"path": str(panel), "relative": str(panel.relative_to(PARTURA_ROOT)), "meta": str(panel.with_suffix(".meta.json")),
                                    "shape": list(FW["P"].shape) if FW["P"] is not None else None}
    mem.stop()

out["seconds"] = time.time() - t0
(D / f"final{SUFFIX}.json").write_text(json.dumps(out, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
(D / f"library{SUFFIX}.json").write_text(json.dumps(lib_json, ensure_ascii=False, indent=1, default=float), encoding="utf-8")

# ------------------------------------------------------------------ the summary (markdown)
f = lambda r, k: f"{r[k]['long_sharpe']:+.2f}"                                 # noqa: E731
L = [f"# PROD {DIRNAME}:库与融合书" + ("(试跑:只含样本内)" if DRY else ""), "",
     f"- 种子 {len(SEEDS)} 个({SEEDS[0]}–{SEEDS[-1]});数据视图 {out['view'][0]} ~ {out['view'][1]}。",
     "- 一切挑选(哪些 head、去重顺序)只用样本内:train 2018–2021、valid 2022-01 ~ 2023-08-07。",
     "- 夏普 = 融合书(纯多头、残差、扣 15 bp)的净夏普。" + ("" if DRY else "**test(2023-08-08 ~ 2025-12-31)与 forward(2026-01-01 ~)两列只作描述,已记入 ledger_prod.json,不用来选任何东西。**"), "",
     f"- 去重前每个种子的库合计:M {sum(len(LIB[(S, 'M')]) for S in SEEDS)},P {sum(len(LIB[(S, 'P')]) for S in SEEDS)};去重后合计 M {sum(len(KEPT[(S, 'M')]) for S in SEEDS)},P {sum(len(KEPT[(S, 'P')]) for S in SEEDS)};"
     f"整波(跨种子再去重)M {len(WAVE['M'])}、P {len(WAVE['P'])}。",
     "- 整波库 = 各种子的 P(M)库合并后,按样本内 score 从高到低、跨种子再去重(同一条规则:与已知族 |ρ| ≥ 0.5 丢,与已留下的 ρ ≥ 0.7 或 ≤ −0.5 丢)。",
     f"- 复现(重建的 train 夏普与记录相差 < 0.05):{sum(bool(h.get('reproduces')) for v in KEPT.values() for h in v)}/{sum(len(v) for v in KEPT.values())}。",
     f"- 付费评估:M {EVALS['M']},P {EVALS['P']};GPU 秒:M {GPUSEC['M']:.0f},P {GPUSEC['P']:.0f}。R 收录:{'开' if out['r_additions'] else '关'}。", "",
     "## 每个种子", "", "| 种子 | M head | P head | M train | M valid | P train | P valid | P−M train | P−M valid |" + ("" if DRY else " M test | P test | M fwd | P fwd |"),
     "|---|---|---|---|---|---|---|---|---|" + ("" if DRY else "---|---|---|---|")]
for S in SEEDS:
    r = out["per_seed"][str(S)]
    d = lambda sl: f"{r['P'][sl]['long_sharpe'] - r['M'][sl]['long_sharpe']:+.2f}"          # noqa: E731
    L.append(f"| {S} | {r['M']['heads']} | {r['P']['heads']} | {f(r['M'], 'train')} | {f(r['M'], 'valid')} | {f(r['P'], 'train')} | {f(r['P'], 'valid')} | {d('train')} | {d('valid')} |"
             + ("" if DRY else f" {f(r['M'], 'test')} | {f(r['P'], 'test')} | {f(r['M'], 'forward')} | {f(r['P'], 'forward')} |"))
dm = {sl: float(np.median([out["per_seed"][str(S)]["P"][sl]["long_sharpe"] - out["per_seed"][str(S)]["M"][sl]["long_sharpe"] for S in SEEDS])) for sl in ("train", "valid")}
L += ["", f"P−M 的种子中位数(监控,样本内):train {dm['train']:+.2f},valid {dm['valid']:+.2f}。", "", "## 整波", "",
      "| 库 | head | train | valid |" + ("" if DRY else " test | forward |"), "|---|---|---|---|" + ("" if DRY else "---|---|")]
for X, nm in (("M", "M 整波"), ("P", "P 整波")):
    r = out["wave"][X]
    L.append(f"| {nm} | {r['heads']} | {f(r, 'train')} | {f(r, 'valid')} |" + ("" if DRY else f" {f(r, 'test')} | {f(r, 'forward')} |"))
if not DRY:
    L += ["", f"整波 P 融合信号面板:`{out['wave_signal_panel']['relative']}`(形状 {out['wave_signal_panel']['shape']};行 = 日期,列 = 股票,见同名 .meta.json)。"]
    ex = out["extra_heads"]
    if ex:
        L += ["", f"## P 的额外 head 单个看(描述;{len(ex)} 个)", "", "| 分组 | 个数 | test 夏普均值 / 中位 | test 为正 | forward 均值 / 中位 |", "|---|---|---|---|---|"]
        groups = {"全部": ex, **{f"第 {k} 轮": [e for e in ex if e["round"] == k] for k in (1, 2, 3)},
                  **{f"角色 {r_}": [e for e in ex if e["role"] == r_] for r_ in sorted({e["role"] for e in ex})}}
        for nm, g in groups.items():
            if g:
                t, w = [e["test_sharpe"] for e in g], [e["forward_sharpe"] for e in g]
                L.append(f"| {nm} | {len(g)} | {np.mean(t):+.2f} / {np.median(t):+.2f} | {sum(x > 0 for x in t)} | {np.mean(w):+.2f} / {np.median(w):+.2f} |")
mt = {}
for m in MISS:
    k = (m["type"], m["round"])
    a = mt.setdefault(k, [0, 0, 0])
    a[0] += 1
    a[1] += m["scored"]
    a[2] += m["heads"]
L += ["", "## 任务位", "", "| 类型 | 轮 | 个数 | 评分 | 入 heads |", "|---|---|---|---|---|"]
L += [f"| {k[0]} | {k[1]} | {v[0]} | {v[1]} | {v[2]} |" for k, v in sorted(mt.items(), key=lambda kv: (kv[0][1], str(kv[0][0])))]
(D / f"final{SUFFIX}.md").write_text("\n".join(L) + "\n", encoding="utf-8")
print("\n".join(L[:12 + len(SEEDS)]))
print(f"wrote {D / ('final' + SUFFIX + '.json')}, library{SUFFIX}.json, final{SUFFIX}.md ({out['seconds']:.0f}s)")
