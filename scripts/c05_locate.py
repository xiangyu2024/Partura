"""C05 locate tools (research/coldstart_C05/PLAN.md §2.4) and the R direct evaluation (§2.5).  Server; train + valid only.

    python scripts/c05_locate.py locate <seed> <arm> <round>
        snapshot = M batches 1..round of the seed + the arm's missions of earlier rounds (+ its R replacements);
        -> research/coldstart_C05/loc/s<seed>_<arm>_r<round>.json and .md:
           heads table, enrichment (subtrees over every archived candidate), ablation of <= 4 not-yet-ablated heads
           (<= 12 variants each, <= 48 paid evaluations), the mechanical core cards and R candidates
    python scripts/c05_locate.py direct <seed> <arm> <round> <requests.json>
        requests = [{"head": <expr of a snapshot head>, "variants": [<expr>, ...]}, ...] (<= 16 variants in all)
        -> research/coldstart_C05/arms/s<seed>_<arm>_r<round>_R.json: every variant scored, and the replacements (§2.5 rule)
"""
import glob
import json
import math
import os
import random
import re
import sys
import time
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.guard import MemoryGuard, limit_threads, slot  # noqa: E402

limit_threads(int(os.environ.get("PARTURA_THREADS", 8)))
import numpy as np  # noqa: E402

from partura import books as bk  # noqa: E402
from partura import diagnose as dg  # noqa: E402
from partura import ops_ext  # noqa: E402,F401
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.panels import SHARED_CACHE, PanelSet  # noqa: E402
from partura.steer import Guidance, RewardContext, neutral_basis, neutral_residual  # noqa: E402
from partura.steer import reward as steer_reward  # noqa: E402

MODE, S, ARM, K = sys.argv[1], int(sys.argv[2]), sys.argv[3], int(sys.argv[4])
os.environ.update(PARTURA_SLOTS="4", PARTURA_GPU_WAYS="2", PARTURA_REPROMOTE="1")      # scheduling only (PLAN revision 2: a GP run holds up to ~13 GB of the card)
D = PARTURA_ROOT / "research" / "coldstart_C05"
EP = PARTURA_ROOT / "episodes"
START, END, SPLIT = "20180102", "20230807", "20220101"
STORE = os.environ.get("PARTURA_STORE", "/root/autodl-tmp/qmt_daily_data/fast_factor_compute")
MIRROR = os.environ.get("PARTURA_MIRROR", "/root/autodl-tmp/AlphaCube/mirror")
MIRROR = MIRROR if MIRROR and os.path.isdir(MIRROR) else None
RHO = float(os.environ.get("PARTURA_RHO_REJECT", "0.5"))
THR, MAX_HEADS, MAX_VAR, MAX_R = 0.5, 4, 12, 16
SWAP = {"Close": "Vwap", "Vwap": "Close", "Open": "Close", "High": "Low", "Low": "High", "Volume": "Amt", "Amt": "Volume"}
G = Guidance.load(PARTURA_ROOT / "guidance" / "C05_base.yaml")


def snapshot_episodes():
    """M batches 1..K, then this arm's missions of rounds < K, in that order."""
    eps = [EP / f"c05s{S}M{e}_I0_open_search" for e in range(1, K + 1)]
    for k in range(1, K):                                 # a mission that ended without evidence produced nothing (PLAN revision 6)
        done = (D / "arms" / f"s{S}_{ARM}_r{k}.DONE").is_file()
        eps += [Path(p) for p in sorted(glob.glob(str(EP / f"c05s{S}{ARM}r{k}[ab]_*"))) if (Path(p) / "evidence.json").is_file() or not done]
    missing = [p for p in eps if not (p / "evidence.json").is_file()]
    if missing:
        raise SystemExit(f"snapshot incomplete: {[p.name for p in missing]}")
    return eps


def replacements():
    """{original head expr: replacing variant row} from this arm's R files of rounds < K."""
    out = {}
    for k in range(1, K):
        f = D / "arms" / f"s{S}_{ARM}_r{k}_R.json"
        if f.is_file():
            for r in json.loads(f.read_text(encoding="utf-8"))["replacements"]:
                out[r["head"]] = r
    return out


sys.path.insert(0, str(PARTURA_ROOT / "scripts"))
import c05_lib  # noqa: E402

with slot():
    mem = MemoryGuard(self_limit_gb=int(os.environ.get("PARTURA_SELF_LIMIT_GB", 34)), cgroup_limit_gb=int(os.environ.get("PARTURA_CGROUP_LIMIT_GB", 70))).start()
    t0 = time.time()
    from alphacube.plugins import load_plugins
    load_plugins(["partura.ac_plugin"])
    from alphacube.expression import Feature, ShapeError, is_valid_root, make_node
    from alphacube.expression import replace as ex_replace
    from alphacube.parser import parse

    def P_(s):
        return parse(s, strict=True, coerce_daily=True, n_minutes=241, allow_general=True)

    ps = PanelSet(STORE, START, END, warmup=60, device="cuda", gpu_fraction=0.3, cache_dir=str(SHARED_CACHE), mirror_root=MIRROR,
                  workdir=str(PARTURA_ROOT / "tmp"), label_kind="open_vwap15", label_buyable=True, batch=8,
                  daily_root=os.environ.get("PARTURA_DAILY_ROOT") or None)
    pool_spec, known_spec = G.spec["pool"][-1], G.spec["pool"][0]
    aux = ps.compute({"frozen": "cross_max(day_zero_ratio(Ret), 15)", "age": "cross_valid_count(day_last(Close), 241)",
                      "liq": "cross_mean(day_sum(Amt), 30)", "pool": pool_spec["expr"], "known": known_spec["expr"],
                      "n_vol": "cross_mean(day_std(Ret), 20)", "n_rev": "div(day_last(Close), ts_delay(day_last(Close), 20))", "n_size": "LogFloatCap"})
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
    ctx.neutral_Q = QF = neutral_basis([aux["liq"], aux["n_vol"], aux["n_rev"], aux["known"], aux["n_size"]])
    labelled = np.isfinite(tgt)
    kz = known_z[:cut:5]

    def corr(a, b):
        ok = np.isfinite(a) & np.isfinite(b)
        x, y = np.where(ok, a, 0.0), np.where(ok, b, 0.0)
        n = np.maximum(ok.sum(1), 1)
        with np.errstate(invalid="ignore", divide="ignore"):
            c = ((x * y).sum(1) - x.sum(1) * y.sum(1) / n) / np.sqrt(((x ** 2).sum(1) - x.sum(1) ** 2 / n) * ((y ** 2).sum(1) - y.sum(1) ** 2 / n))
        return float(np.nanmean(c))

    def evaluate(exprs):
        """{expr: row} -- the reward of idea_search / c02_direct on each expression; paid evaluations."""
        out = {}
        exprs = list(dict.fromkeys(exprs))
        for i in range(0, len(exprs), 8):
            chunk = exprs[i:i + 8]
            P = {}
            try:
                P = ps.compute({f"v{j}": e for j, e in enumerate(chunk)})
            except Exception:                                 # noqa: BLE001
                for j, e in enumerate(chunk):
                    try:
                        P[f"v{j}"] = ps.compute({"x": e})["x"]
                    except Exception as exc:                  # noqa: BLE001
                        out[e] = {"expr": e, "error": f"{type(exc).__name__}: {str(exc)[:120]}"}
            for j, e in enumerate(chunk):
                if f"v{j}" not in P:
                    out.setdefault(e, {"expr": e, "error": "did not compute"})
                    continue
                panel = np.asarray(P[f"v{j}"], np.float64)
                r = {"expr": e, "coverage": float(np.isfinite(panel[labelled]).mean()), "distinct": dg.distinct_fraction(panel)}
                r["gate"] = bool(r["coverage"] >= 0.9 and r["distinct"] >= 0.5)
                if r["gate"]:
                    rw = steer_reward(panel, ctx, "long_neutral")
                    z = dg._zrank(rw["sign"] * panel[:cut:5])
                    r.update(score=rw["score"], sign=rw["sign"], hl=rw["hl"], train=rw["train"]["long_sharpe"], valid=rw["valid"]["long_sharpe"],
                             rho_known=corr(z, kz))
                    r["_traded"] = neutral_residual(bk.smoothed(rw["sign"] * panel, rw["hl"]), QF)
                out[e] = r
        return out

    def traded(h):
        p = ps.compute({"x": h["expr"]})["x"]
        return neutral_residual(bk.smoothed(float(h["sign"]) * np.asarray(p, np.float64), float(h["hl"])), QF)

    def clean(r):
        return {k: (round(v, 4) if isinstance(v, float) and math.isfinite(v) else (None if isinstance(v, float) else v))
                for k, v in r.items() if not k.startswith("_")}

    eps = snapshot_episodes()
    rep = replacements()
    heads = []
    for h in c05_lib.heads(eps):
        if h["expr"] in rep:                                  # an R replacement of an earlier round stands in for its head
            r, seen = rep[h["expr"]], {h["expr"]}
            while r["expr"] in rep and r["expr"] not in seen:     # PLAN revision 13: follow a chain of replacements to its end
                seen.add(r["expr"])
                r = rep[r["expr"]]
            h = {**h, **{k: r[k] for k in ("expr", "sign", "hl", "score", "train", "valid")}, "replaces": h["expr"]}
        heads.append(h)

    prev = []                                                 # what the arm's earlier missions did (train / valid only)
    for ep in eps:
        if ep.name.startswith(f"c05s{S}M"):
            continue
        E = c05_lib.evidence(ep)
        for arm_, A in E["arms"].items():
            prev.append({"mission": ep.name, "core": (E.get("c05") or {}).get("core"), "scored": A.get("scored"), "passers": A.get("passers"),
                         "heads": len(A.get("heads", [])), "sampling": A.get("sampling"),
                         "best": [{k: c.get(k) for k in ("expr", "score", "train", "valid", "sign", "hl")} for c in A.get("candidates", [])[:5]]})

    if MODE == "direct":
        req = json.loads(Path(sys.argv[5]).read_text(encoding="utf-8"))
        byexpr = {h["expr"]: h for h in heads}
        todo = [(q["head"], v) for q in req for v in q["variants"]][:MAX_R]
        bad = [hd for hd, _ in todo if hd not in byexpr]
        if bad:
            raise SystemExit(f"R requests name heads outside the snapshot: {bad[:3]}")
        res = evaluate([v for _, v in todo])
        out, repl = [], []
        for hd, v in todo:
            r, h = res[v], byexpr[hd]
            row = {"head": hd, "head_score": h["score"], **clean(r)}
            if r.get("gate") and math.isfinite(r.get("score", float("nan"))):
                row["rho_head"] = round(corr(r["_traded"][:cut:5], traded(h)[:cut:5]), 4)
                row["replaces"] = bool(r["score"] >= h["score"] + 0.1 and row["rho_head"] >= 0.5 and abs(r["rho_known"]) < RHO)
            out.append(row)
        for hd in dict.fromkeys(hd for hd, _ in todo):         # one replacement per head: the best variant that qualifies
            ok = [r for r in out if r["head"] == hd and r.get("replaces")]
            if ok:
                b = max(ok, key=lambda r: r["score"])
                repl.append({"head": hd, **{k: b[k] for k in ("expr", "sign", "hl", "score", "train", "valid")}})
        f = D / "arms" / f"s{S}_{ARM}_r{K}_R.json"
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(json.dumps({"seed": S, "arm": ARM, "round": K, "paid": len(todo), "rows": out, "replacements": repl}, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"wrote {f}: {len(todo)} variants, {len(repl)} replacements ({time.time() - t0:.0f}s)")
        mem.stop()
        sys.exit(0)

    # ---------------------------------------------------------------- enrichment over every archived candidate
    arch = c05_lib.archive(eps)
    cand = []
    for a in arch:
        if a["score"] is None:
            continue
        try:
            t = P_(a["expr"])
        except Exception:                                    # noqa: BLE001
            continue
        subs = {repr(n) for n in t.nodes()[1:] if n.operands and n.shape.collapsed and n.shape.degenerate}
        cand.append((a["score"], subs))
    count = defaultdict(int)
    for _, subs in cand:
        for s in subs:
            count[s] += 1
    try:
        from scipy.stats import mannwhitneyu
    except Exception:                                        # noqa: BLE001
        mannwhitneyu = None
    enrich = []
    for s, n in count.items():
        if n < 4 or n > 0.7 * len(cand):
            continue
        w = [sc for sc, subs in cand if s in subs]
        wo = [sc for sc, subs in cand if s not in subs]
        eff = float(np.mean(w) - np.mean(wo))
        p = float(mannwhitneyu(w, wo, alternative="greater").pvalue) if mannwhitneyu else float("nan")
        enrich.append({"subtree": s, "n_with": n, "mean_with": round(float(np.mean(w)), 4), "mean_without": round(float(np.mean(wo)), 4),
                       "effect": round(eff, 4), "p": round(p, 4)})
    enrich.sort(key=lambda r: -r["effect"])

    # ---------------------------------------------------------------- ablation of <= 4 heads not ablated before
    done = set()
    for k in range(1, K):
        f = D / "loc" / f"s{S}_{ARM}_r{k}.json"
        if f.is_file():
            done |= {a["head"] for a in json.loads(f.read_text(encoding="utf-8"))["ablation"]}
    todo = [h for h in sorted(heads, key=lambda h: -h["score"]) if h["expr"] not in done][:MAX_HEADS]
    plans = []
    for h in todo:
        t = P_(h["expr"])
        nodes = t.nodes()
        bfs = sorted(nodes[1:], key=lambda n: (n.depth() * -1))   # bigger subtrees first
        subs = [n for n in bfs if n.operands and n.shape.collapsed and n.shape.degenerate and is_valid_root(n)]
        var = []
        for n in subs[:4]:
            var.append(("sufficiency", repr(n), repr(n)))
        ko = 0
        for n in bfs:
            if ko >= 4 or not n.operands:
                continue
            kid = next((c for c in n.operands if c.shape.collapsed and c.shape.degenerate), None)
            if kid is None:
                continue
            try:
                v = ex_replace(t, n, kid)
            except ShapeError:
                continue
            if is_valid_root(v) and repr(v) != h["expr"]:
                var.append(("knockout", repr(n), repr(v)))
                ko += 1
        fields = list(dict.fromkeys(n.field for n in nodes if isinstance(n, Feature) and n.field in SWAP))
        for fld in fields[:2]:
            v = re.sub(rf"\b{fld}\b", SWAP[fld], h["expr"])
            if v != h["expr"]:
                var.append(("swap", f"{fld}->{SWAP[fld]}", v))
        wn = next((n for n in nodes if n.window), None)
        if wn is not None:
            for w in (max(2, wn.window // 2), wn.window * 2):
                try:
                    v = repr(ex_replace(t, wn, make_node(wn.spec, wn.operands, w)))
                    var.append(("window", f"{wn.name}@{wn.window}->{w}", v))
                except Exception:                            # noqa: BLE001
                    pass
        seen, uniq = set(), []
        for kind, what, v in var:
            if v not in seen:
                seen.add(v)
                uniq.append((kind, what, v))
        plans.append((h, uniq[:MAX_VAR]))
    res = evaluate([v for _, vs in plans for _, _, v in vs])
    ablation, cards, rcands = [], [], []
    for h, vs in plans:
        rows = []
        for kind, what, v in vs:
            r = res.get(v, {"expr": v, "error": "missing"})
            row = {"kind": kind, "what": what, **clean(r)}
            if kind == "knockout" and r.get("gate"):
                row["necessity"] = round(h["score"] - r["score"], 4)
            if kind != "sufficiency" and r.get("gate") and math.isfinite(r.get("score", float("nan"))) and r["score"] >= h["score"] + 0.1 \
                    and abs(r["rho_known"]) < RHO:
                rho_h = corr(r["_traded"][:cut:5], traded(h)[:cut:5])
                row["rho_head"] = round(rho_h, 4)
                if rho_h >= 0.5:
                    rcands.append({"head": h["expr"], "head_score": h["score"], "variant": v, "kind": kind, "what": what,
                                   "score": round(r["score"], 4), "gain": round(r["score"] - h["score"], 4)})
            if kind == "sufficiency" and r.get("gate") and r["score"] >= THR and r["score"] >= 0.6 * h["score"]:
                cards.append({"core": v, "source": "ablation", "own_score": round(r["score"], 4), "head": h["expr"], "head_score": h["score"]})
            rows.append(row)
        ablation.append({"head": h["expr"], "head_score": h["score"], "src": h["src"], "variants": rows})
    cards.sort(key=lambda c: -c["own_score"])
    cards += [{"core": e["subtree"], "source": "enrichment", "effect": e["effect"], "p": e["p"], "n_with": e["n_with"]}
              for e in enrich if e["effect"] > 0 and e["p"] < 0.1 and is_valid_root(P_(e["subtree"]))]
    uniq, seen = [], set()
    for c in cards:
        if c["core"] not in seen:
            seen.add(c["core"])
            uniq.append(c)
    rcands.sort(key=lambda r: -r["gain"])
    mem.stop()

out = {"seed": S, "arm": ARM, "round": K, "snapshot": [p.name for p in eps], "replacements_in_force": len(rep),
       "heads": sorted(heads, key=lambda h: -h["score"]), "n_archived": len(cand), "enrichment": enrich[:40],
       "ablation": ablation, "paid": sum(len(vs) for _, vs in plans), "core_cards": uniq, "r_candidates": rcands, "missions_before": prev,
       "seconds": round(time.time() - t0)}
(D / "loc").mkdir(parents=True, exist_ok=True)
f = D / "loc" / f"s{S}_{ARM}_r{K}.json"
f.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")


def g(x):
    return "—" if x is None else f"{x:+.2f}" if isinstance(x, (int, float)) else str(x)


L = [f"# 定位:种子 {S},{ARM} 组,第 {K} 轮(只含 train / valid)", "",
     f"快照:{', '.join(out['snapshot'])};已生效的 R 替换 {len(rep)} 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。", "",
     f"## heads({len(heads)} 个)", "", "| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |", "|---|---|---|---|---|---|---|"]
L += [f"| {g(h['score'])} | {g(h['train'])} | {g(h['valid'])} | {h['sign']:+.0f} | {h['hl']:g} | {h['src']} | `{h['expr']}` |" for h in out["heads"]]
L += ["", f"## 共性:{len(cand)} 个已评分候选里的子树(按均值差排,前 20)", "", "| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |", "|---|---|---|---|---|"]
L += [f"| {g(e['effect'])} | {e['p']:.3f} | {e['n_with']} | {g(e['mean_with'])} / {g(e['mean_without'])} | `{e['subtree']}` |" for e in enrich[:20]]
L += ["", f"## 拆解({out['paid']} 次评估)"]
for a in ablation:
    L += ["", f"### head score {g(a['head_score'])}:`{a['head']}`", "", "| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |", "|---|---|---|---|---|---|---|"]
    L += [f"| {r['kind']} | `{r['what']}` | {g(r.get('score'))} | {g(r.get('train'))} | {g(r.get('valid'))} | {g(r.get('necessity'))} | "
          f"{'`' + r['expr'] + '`' if r['kind'] != 'sufficiency' else ('门槛废品' if not r.get('gate') else '(子树本身)')} |" for r in a["variants"]]
L += ["", "## 机械核心卡(B0 按这个顺序取)", ""]
L += [f"{i + 1}. `{c['core']}` — {c['source']}" + (f",自身 score {g(c['own_score'])}(所在 head {g(c['head_score'])})" if c["source"] == "ablation" else f",均值差 {g(c['effect'])},p {c['p']:.3f}") for i, c in enumerate(uniq)]
L += ["", "## 本组之前各轮的任务", ""]
for m in prev:
    L += [f"- `{m['mission']}`:核心 `{m['core'] or '—'}`;评分 {m['scored']},过线 {m['passers']},入 heads {m['heads']};采样计数 {m['sampling']}"]
    L += [f"  - score {g(c['score'])}(train {g(c['train'])} valid {g(c['valid'])}):`{c['expr']}`" for c in m["best"]]
if not prev:
    L.append("(第 1 轮,还没有)")
L += ["", "## 比原 head 好的拆解变体(R 候选)", ""]
L += [f"- 增益 {g(r['gain'])}({r['kind']} {r['what']}):`{r['variant']}`" for r in rcands] or ["(没有)"]
f.with_suffix(".md").write_text("\n".join(L) + "\n", encoding="utf-8")
print(f"wrote {f} (+ .md): {len(heads)} heads, {len(cand)} archived, {len(enrich)} enriched subtrees, {out['paid']} ablation evaluations, "
      f"{len(uniq)} core cards, {len(rcands)} R candidates ({out['seconds']}s)")
