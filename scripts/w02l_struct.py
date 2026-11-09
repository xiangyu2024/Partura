"""W02L step 1: structural batches of AlphaCube's two champion libraries -- the handwritten library L (legacy, 1392 scored)
and the mined library X (allfac_buyable, 4206) -- by expression structure only.  Laptop; no data read beyond the in-sample
(train = 2018-01-02 ~ 2023-08-07) statistics that research/prod_W02L/inputs/libs_train.csv carries for the batch tables.

    ~/.venvs/alphacube/bin/python scripts/w02l_struct.py [--cut 0.6] [--max 60] [--min 8] [--join 0.3] [--loose-cut 0.85]
                                                          [--theme-cut 0.85] [--theme-max 8]

What "structure" is here.  Every expression is parsed with AlphaCube's own parser; each operator node contributes
  - its subtree's skeleton (AlphaCube's skeleton_key -- fields as F, constants and windows dropped: the GP library ban's key),
    weighted by log2(1 + size of the subtree): a large shared substructure says more than a shared day_std(F);
  - for an operator whose operands are all leaves, the operator with its fields kept (day_std(Amt) is not day_std(Ret)),
    windows dropped;
each token weighted by its inverse document frequency over the 5598 expressions; a token only one expression has is dropped.  Cosine similarity of these vectors,
average-linkage clustering cut at --cut, then clusters above --max split along their own dendrogram and clusters below
--min merged into the most similar batch (by centroid) -- or, when nothing is similar enough, into one "residue" batch per
root operator.  The batches are a partition: every parsed expression is in exactly one.

Out: research/prod_W02L/struct/members.csv (one row per expression: batch, skeleton, leaf fields, flags),
     research/prod_W02L/struct/batches.json and BATCHES.md (one row per batch: size, L / X split, champion-family
     membership, shared substructures, medoid, in-sample statistics).
"""
import json
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from partura import bridge  # noqa: E402

bridge.ensure_alphacube_on_path()
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from alphacube.mining.clustering import skeleton_key  # noqa: E402
from alphacube.parser import parse  # noqa: E402
from alphacube.plugins import load_plugins  # noqa: E402
from scipy.cluster.hierarchy import fcluster, linkage, to_tree  # noqa: E402
from scipy.spatial.distance import squareform  # noqa: E402

load_plugins(["partura.ac_plugin"])


def opt(name, default):
    return type(default)(sys.argv[sys.argv.index(name) + 1]) if name in sys.argv else default


CUT, MAX, MIN = opt("--cut", 0.6), opt("--max", 60), opt("--min", 8)
JOIN, LOOSE_CUT = opt("--join", 0.3), opt("--loose-cut", 0.85)
THEME_CUT, THEME_MAX = opt("--theme-cut", 0.85), opt("--theme-max", 8)
OUT = ROOT / "research/prod_W02L/struct"
OUT.mkdir(parents=True, exist_ok=True)
BANNED = re.compile(r"\b(nt_\w+|ts_spearman)\(")      # not in the current GP vocabulary (research/prod_W01/rules.md §1)
VOLUME_LEAVES = {"Amt", "Volume"}


def skel(n):
    return re.sub(r"@[\d.]+", "", skeleton_key(n))


def leaf_token(n):
    return re.sub(r",\s*-?\d+(\.\d+)?", "", repr(n))


def tokens(t):
    out = {}
    for n in t.nodes():
        if not n.operands:
            continue
        size = sum(1 for _ in n.nodes())
        k = "S:" + skel(n)
        out[k] = max(out.get(k, 0.0), math.log2(1 + size))
        if all(not o.operands for o in n.operands):
            out["L:" + leaf_token(n)] = 1.0
    return out


df = pd.read_csv(ROOT / "research/prod_W02L/inputs/libs_train.csv")
rows, toks, fails = [], [], []
for r in df.itertuples(index=False):
    try:
        t = parse(r.expression, strict=True, coerce_daily=True, n_minutes=241, allow_general=True)
    except Exception as exc:                                  # noqa: BLE001
        fails.append({"lib": r.lib, "i": int(r.i), "expression": r.expression, "error": f"{type(exc).__name__}: {str(exc)[:120]}"})
        continue
    leaves = sorted({repr(n) for n in t.nodes() if not n.operands and re.fullmatch(r"[A-Za-z_]\w*", repr(n))})
    rows.append({"lib": r.lib, "i": int(r.i), "expression": r.expression, "skeleton": skel(t), "root": t.name,
                 "size": sum(1 for _ in t.nodes()), "leaves": " ".join(leaves),
                 "volume_leaf": bool(VOLUME_LEAVES & set(leaves)), "banned_op": bool(BANNED.search(r.expression)),
                 "healthy": bool(r.healthy), "champ_family": int(r.champ_family),
                 "rank_ic_train": float(r.rank_ic_train), "turnover_train": float(r.turnover_train),
                 "net_sharpe_train": float(r.net_sharpe_train)})
    toks.append(tokens(t))
M = pd.DataFrame(rows)
print(f"parsed {len(M)} of {len(df)}; failed {len(fails)}", flush=True)

# ---- vectors: idf-weighted structural tokens, L2-normalised
dfreq = Counter(k for d in toks for k in d)
# a token only one expression has says nothing about what it shares (and, being the whole tree, it would dominate the norm)
toks = [{k: w for k, w in d.items() if dfreq[k] > 1} or d for d in toks]
vocab = {}
for d in toks:
    for k in d:
        vocab.setdefault(k, len(vocab))
N = len(toks)
idf = {k: math.log(N / c) for k, c in dfreq.items()}
X = np.zeros((N, len(vocab)), np.float32)
for i, d in enumerate(toks):
    for k, w in d.items():
        X[i, vocab[k]] = w * idf[k]
X /= np.maximum(np.linalg.norm(X, axis=1, keepdims=True), 1e-12)
S = np.clip(X @ X.T, -1.0, 1.0)
D = 1.0 - S
np.fill_diagonal(D, 0.0)


def split(ids, cap):
    """Split ids (> cap) along their own average-linkage dendrogram into pieces of at most cap."""
    if len(ids) <= cap:
        return [list(ids)]
    tr = to_tree(linkage(squareform(D[np.ix_(ids, ids)], checks=False), method="average"))
    out, stack = [], [tr]
    while stack:
        nd = stack.pop()
        if nd.get_count() <= cap or nd.is_leaf():
            out.append([ids[j] for j in nd.pre_order()])
        else:
            stack += [nd.get_left(), nd.get_right()]
    return out


def centroids(groups):
    c = np.stack([X[g].mean(0) for g in groups])
    return c / np.maximum(np.linalg.norm(c, axis=1, keepdims=True), 1e-12)


# ---- 1. fine structural clusters, cut at CUT, split above MAX
lab = fcluster(linkage(squareform(D, checks=False), method="average"), t=CUT, criterion="distance")
groups = defaultdict(list)
for i, l in enumerate(lab):
    groups[l].append(i)
parts = [q for g in groups.values() for q in split(g, MAX)]
big = [p for p in parts if len(p) >= MIN]
small = [i for p in parts if len(p) < MIN for i in p]
# ---- 2. a small piece joins the batch it is most similar to (centroid cosine >= JOIN); a batch pushed over MAX is re-split
#         and any piece the split leaves under MIN goes back into the pool -- three passes, then what is left is "loose"
for _ in range(3):
    if not small:
        break
    cent = centroids(big)
    loose = []
    for i in small:
        sim = cent @ X[i]
        j = int(np.argmax(sim))
        (big[j].append(i) if sim[j] >= JOIN else loose.append(i))
    nb, small = [], list(loose)
    for b in big:
        for q in split(b, MAX):
            (nb.append(q) if len(q) >= MIN else small.extend(q))
    big = nb
# ---- 3. the loose ones: clustered among themselves at a looser cut; pieces still under MIN pooled into chunks of <= MAX
residue = []
if small:
    if len(small) > 1:
        sub = squareform(D[np.ix_(small, small)], checks=False)
        l2 = fcluster(linkage(sub, method="average"), t=LOOSE_CUT, criterion="distance")
    else:
        l2 = [1]
    g2 = defaultdict(list)
    for i, l in zip(small, l2):
        g2[l].append(i)
    pool = []
    for g in g2.values():
        for q in split(g, MAX):
            (residue.append(q) if len(q) >= MIN else pool.extend(q))
    pool.sort(key=lambda i: (M.root[i], M.skeleton[i]))
    residue += [pool[k:k + MAX] for k in range(0, len(pool), MAX)]
batches = [(b, "struct") for b in big] + [(b, "residue") for b in residue]


def shared(ids, frac=0.6):
    c = Counter(k for i in ids for k in toks[i])
    need = frac * len(ids)
    return sorted([k for k, v in c.items() if v >= need], key=lambda k: (-(len(k)), k))


summ = []
for b, kind in batches:
    sub = M.iloc[b]
    sims = S[np.ix_(b, b)]
    med = b[int(np.argmax(sims.mean(1)))]
    core = [k[2:] for k in shared(b) if k.startswith("S:")][:3]
    leaf = [k[2:] for k in shared(b, 0.5) if k.startswith("L:")][:4]
    fit = (sub.rank_ic_train.abs() - 0.14 * sub.turnover_train)
    cf = sub.loc[sub.champ_family >= 0]
    summ.append({"kind": kind, "ids": b, "n": len(b), "n_L": int((sub.lib == "L").sum()), "n_X": int((sub.lib == "X").sum()),
                 "healthy": int(sub.healthy.sum()), "in_champ": int(len(cf)),
                 "champ_families": int((cf.lib + cf.champ_family.astype(str)).nunique()),
                 "within_sim": float((sims.sum() - len(b)) / max(1, len(b) * (len(b) - 1))),
                 "volume_leaf": float(sub.volume_leaf.mean()), "banned_op": float(sub.banned_op.mean()),
                 "spearman": int(sub.expression.str.contains("ts_spearman").sum()),
                 "skeletons": int(sub.skeleton.nunique()), "core": core, "leaf_tokens": leaf,
                 "medoid": M.expression[med],
                 "abs_ric_train_med": float(sub.rank_ic_train.abs().median()), "abs_ric_train_max": float(sub.rank_ic_train.abs().max()),
                 "fitness_max": float(fit.max()), "net_sharpe_train_max": float(sub.net_sharpe_train.max()),
                 "turnover_train_med": float(sub.turnover_train.median())})

# ---- 4. themes: structural batches grouped by centroid similarity (average linkage, cut THEME_CUT, <= THEME_MAX batches);
#         residue batches are their own theme ("R")
st = [k for k, s in enumerate(summ) if s["kind"] == "struct"]
C = centroids([summ[k]["ids"] for k in st])
Dc = np.clip(1.0 - C @ C.T, 0.0, 2.0)
np.fill_diagonal(Dc, 0.0)
tl = fcluster(linkage(squareform(Dc, checks=False), method="average"), t=THEME_CUT, criterion="distance") if len(st) > 1 else [1]
tg = defaultdict(list)
for k, l in zip(st, tl):
    tg[l].append(k)
themes = []
for g in tg.values():
    if len(g) <= THEME_MAX:
        themes.append(g)
        continue
    sub = Dc[np.ix_([st.index(k) for k in g], [st.index(k) for k in g])]
    tr = to_tree(linkage(squareform(sub, checks=False), method="average"))
    stack = [tr]
    while stack:
        nd = stack.pop()
        if nd.get_count() <= THEME_MAX or nd.is_leaf():
            themes.append([g[j] for j in nd.pre_order()])
        else:
            stack += [nd.get_left(), nd.get_right()]
themes.sort(key=lambda g: -sum(summ[k]["n"] for k in g))
order = []
for t_i, g in enumerate(themes, 1):
    g.sort(key=lambda k: -summ[k]["n"])
    for k in g:
        summ[k]["theme"] = f"T{t_i:02d}"
        order.append(k)
for k, s in enumerate(summ):
    if s["kind"] == "residue":
        s["theme"] = "R"
        order.append(k)
summ = [summ[k] for k in order]
M["batch"], M["theme"] = "", ""
for k, s in enumerate(summ, 1):
    s["batch"] = f"B{k:03d}"
    M.loc[s["ids"], "batch"] = s["batch"]
    M.loc[s["ids"], "theme"] = s["theme"]
assert (M.batch != "").all() and M.batch.value_counts().sum() == len(M)
M.to_csv(OUT / "members.csv", index=False)
(OUT / "batches.json").write_text(json.dumps({"params": {"cut": CUT, "max": MAX, "min": MIN, "join": JOIN, "loose_cut": LOOSE_CUT,
                                                         "theme_cut": THEME_CUT, "theme_max": THEME_MAX},
                                              "parsed": len(M), "failed": fails,
                                              "batches": [{k: v for k, v in s.items() if k != "ids"} for s in summ]},
                                             ensure_ascii=False, indent=1), encoding="utf-8")

# ---- report
th = defaultdict(list)
for s in summ:
    th[s["theme"]].append(s)
L = ["# W02L 结构分批(手写库 L + 挖掘库 X;只用表达式结构;表里的统计只用样本内 2018-01-02 ~ 2023-08-07)", "",
     f"参数:细聚类切点余弦距离 {CUT};每批 {MIN} ~ {MAX} 条;小块并入最相似的批要求质心余弦 ≥ {JOIN};剩下的在 {LOOSE_CUT} 上再聚一次;"
     f"主题 = 结构批按质心再聚类(切点 {THEME_CUT},每个主题 ≤ {THEME_MAX} 批)。", "",
     f"解析 {len(M)} / {len(df)} 条(失败 {len(fails)} 条,都是 `day_sum(in_slice(Volume, 1, 1))` 一类在现在的解析器下不合法的手写式)。"
     f"批 {len(summ)} 个:结构批 {sum(s['kind'] == 'struct' for s in summ)} 个({sum(s['n'] for s in summ if s['kind'] == 'struct')} 条),"
     f"残余批 {sum(s['kind'] == 'residue' for s in summ)} 个({sum(s['n'] for s in summ if s['kind'] == 'residue')} 条);主题 {len([t for t in th if t != 'R'])} 个。", "",
     "## 主题", "",
     "| 主题 | 批数 | 条数 | L / X | 冠军族成员 | 量额叶子 | 禁用算子 | 训练 |rank IC| 最大 | 共有子结构(最大那批) |",
     "|---|---|---|---|---|---|---|---|---|"]
for t, ss in th.items():
    n = sum(s["n"] for s in ss)
    L.append(f"| {t} | {len(ss)} | {n} | {sum(s['n_L'] for s in ss)} / {sum(s['n_X'] for s in ss)} | {sum(s['in_champ'] for s in ss)} | "
             f"{sum(s['volume_leaf'] * s['n'] for s in ss) / n:.0%} | {sum(s['banned_op'] * s['n'] for s in ss) / n:.0%} | "
             f"{max(s['abs_ric_train_max'] for s in ss):.3f} | `{(ss[0]['core'][0] if ss[0]['core'] else '—')[:80]}` |")
L += ["", "## 批", "",
      "| 批 | 主题 | 条数 | L / X | 冠军族成员(族数) | 骨架数 | 批内结构相似 | 量额叶子 | 禁用算子 | 训练 |rank IC| 中位 / 最大 | 适应度最大 | 共有子结构 | 代表式 |",
      "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
for s in summ:
    L.append(f"| {s['batch']} | {s['theme']} | {s['n']} | {s['n_L']} / {s['n_X']} | {s['in_champ']}({s['champ_families']}) | "
             f"{s['skeletons']} | {s['within_sim']:.2f} | {s['volume_leaf']:.0%} | {s['banned_op']:.0%} | "
             f"{s['abs_ric_train_med']:.3f} / {s['abs_ric_train_max']:.3f} | {s['fitness_max']:.3f} | "
             f"`{(s['core'][0] if s['core'] else '—')[:70]}` | `{s['medoid'][:90]}` |")
(OUT / "BATCHES.md").write_text("\n".join(L) + "\n", encoding="utf-8")
sz = [s["n"] for s in summ if s["kind"] == "struct"]
print(f"{len(summ)} batches ({len(sz)} structural: sizes min {min(sz)} median {int(np.median(sz))} max {max(sz)}, "
      f"{sum(sz)} expressions; within-sim median {np.median([s['within_sim'] for s in summ if s['kind'] == 'struct']):.2f}); "
      f"residue {sum(s['n'] for s in summ if s['kind'] == 'residue')} in {sum(s['kind'] == 'residue' for s in summ)}; themes {len(th) - ('R' in th)}", flush=True)
