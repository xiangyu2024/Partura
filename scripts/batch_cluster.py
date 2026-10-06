"""分辨 at the end of a batch (batch method): are the rule-picked candidates of 15 factors N things, or a few?

Reads every factor's ``runs/<fid>/sweepfinal_<tag>.json`` (the candidates a fixed rule picked on train / valid),
builds the signal each would be traded with (sign x panel, EMA at the half-life its pure long book prefers on the
user's training period) and, on the user's TRAINING period only, reports

* the daily cross-sectional rank correlation of every pair, and the overlap of their long books
  (share of the top decile two signals hold in common);
* clusters.  Candidates are taken in the order of their pure-long Sharpe; one joins an earlier cluster head when
  their rank correlation is >= 0.7 OR their long books share >= 50% of the names, otherwise it starts a cluster
  of its own.  (The overlap matters: a screen pushes a fifth of the names to the bottom, which lowers the rank
  correlation a lot and changes the book that is held very little.)  A cluster belongs to the KNOWN FAMILY when
  it holds a benchmark, or when its head is built on ``day_std(Amt)`` or is that close to a benchmark; the
  others are independent;
* combination books, by a rule written before looking -- the mean of the members' z-ranks:

    ``known_head``  the head of the best known-family cluster, alone
    ``indep_eq``    every independent head whose training pure-long Sharpe is >= 2.0, equal weights
    ``indep_top3``  the best three of them
    ``all_eq``      those heads plus the known head, equal weights
    ``half_half``   half the known head, half the mean of the independent heads

  and, still on the training period, ``indep_eq`` with each head left out in turn (what does each one carry?).

``--read-holdout`` also scores the five combination books on the test period: one read, ledgered.

    python scripts/batch_cluster.py batches/B01_single_factors.yaml [--tag s2] [--read-holdout]
"""
import json
import math
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.guard import MemoryGuard, limit_threads, slot  # noqa: E402

limit_threads(4)
import numpy as np  # noqa: E402
import yaml  # noqa: E402

from partura import books as bk  # noqa: E402
from partura import diagnose as dg  # noqa: E402
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.panels import SHARED_CACHE, PanelSet  # noqa: E402
from partura.splits import SPLITS, Ledger  # noqa: E402

argv = sys.argv[1:]


def opt(name, default=None):
    return argv[argv.index(name) + 1] if name in argv else default


TAG = opt("--tag", "s2")
READ = "--read-holdout" in argv
RHO, OVL, SH_MIN = float(opt("--rho", 0.7)), float(opt("--overlap", 0.5)), float(opt("--min-sharpe", 2.0))
batch = yaml.safe_load(open(PARTURA_ROOT / argv[0], encoding="utf-8"))
bname = Path(argv[0]).stem.split("_")[0]
first = yaml.safe_load(open(PARTURA_ROOT / "configs" / f"{batch['factors'][0]['id']}.yaml", encoding="utf-8"))
for k, v in first["splits"].items():
    SPLITS[k] = (str(v[0]), str(v[1]))

spec, by_expr = {}, {}          # key -> what it is; an expression several factors picked is kept once


def add(key, r, role, fid, cid):
    e = r["expr"].replace(" ", "")
    if e in by_expr:
        spec[by_expr[e]]["also"].append(key)
        return
    by_expr[e] = key
    v = r["books_user"]["by_rank"]["long"]
    spec[key] = {"expr": r["expr"], "sign": float(r["sign_user"]), "hl": float(v["hl"]), "kind": r["kind"], "role": role,
                 "fid": fid, "cid": cid, "also": [], "why": r.get("why", "")}


missing = []
for f in batch["factors"]:
    fid, s = f["id"], f["id"].split("_")[0]
    p = PARTURA_ROOT / "runs" / fid / f"sweepfinal_{TAG}.json"
    if not p.is_file():
        missing.append(s)
        continue
    F = json.loads(p.read_text(encoding="utf-8"))
    R = F["results"]
    for b, key in (("k_known", "known"), ("k_known_xfrozen", "known_xfrozen")):
        if b in R:
            add(key, R[b], "bench", "", b)
    own = [k for k in F["picks"] if k in R]
    for k in own:
        add(f"{s}.{k}", R[k], "own", fid, k)
    for k in R:
        if k not in own and k not in ("v_base", "k_known", "k_known_xfrozen"):
            add(f"{s}.{k}", R[k], "onk", fid, k)
for f in batch["factors"]:      # the originals last: shown in the tables, never a cluster head
    fid, s = f["id"], f["id"].split("_")[0]
    p = PARTURA_ROOT / "runs" / fid / f"sweepfinal_{TAG}.json"
    if p.is_file():
        R = json.loads(p.read_text(encoding="utf-8"))["results"]
        if "v_base" in R:
            add(f"{s}.orig", R["v_base"], "orig", fid, "v_base")
print(f"[cluster] {bname} {TAG}: {len(spec)} distinct signals "
      f"({sum(v['role'] == 'own' for v in spec.values())} own, {sum(v['role'] == 'onk' for v in spec.values())} on-known, "
      f"{sum(v['role'] == 'orig' for v in spec.values())} originals); missing {missing}", flush=True)


def by_year_net(sm, tgt, yrs, last_day):
    """Pure-long net excess per calendar year, each year's book started empty; days after ``last_day`` are not read."""
    from alphacube.metrics import long_short_weights
    out = {}
    for y in sorted(set(yrs[:last_day])):
        d = np.nonzero(yrs[:last_day] == y)[0]
        sl = slice(int(d[0]), int(d[-1]) + 1)
        w = long_short_weights(sm[sl], bk.TOP_FRAC)
        out[str(y)] = float(np.nanmean(bk.long_book(w, sm[sl], tgt[sl])[0]) * 252)
    return out


with slot():
    mem = MemoryGuard(self_limit_gb=34, cgroup_limit_gb=70).start()
    t0 = time.time()
    ps = PanelSet("/root/autodl-tmp/qmt_daily_data/fast_factor_compute", SPLITS["full"][0], SPLITS["full"][1],
                  warmup=int(first.get("warmup", 60)), device="cuda", gpu_fraction=0, cache_dir=str(SHARED_CACHE),
                  mirror_root="/root/autodl-tmp/AlphaCube/mirror", workdir=str(PARTURA_ROOT / "tmp"),
                  label_kind="open_vwap15", label_buyable=True, batch=8)
    P = ps.compute({k: v["expr"] for k, v in spec.items()})
    tgt = ps.target(1)
    tr, va, us, ho = (ps.split_slice(x) for x in ("train", "valid", "utrain", "holdout"))
    last = len(ps.dates) if READ else us.stop
    from alphacube.metrics import long_short_weights

    Z, held = {}, {}
    for k, v in list(spec.items()):
        p = P.get(k)
        if p is None:
            print(f"  {k}: no panel ({ps.errors.get(k)})", flush=True)
            del spec[k]
            continue
        sm = bk.smoothed(v["sign"] * np.asarray(p, dtype=np.float64), v["hl"])
        v["books"] = {n: bk.book_row(sm, tgt, d) for n, d in (("train", tr), ("valid", va), ("utrain", us))}
        Z[k] = dg._zrank(sm).astype(np.float32)                    # full period; only utrain is used unless --read-holdout
        held[k] = long_short_weights(sm[us], bk.TOP_FRAC) > 0
    names = list(Z)
    N, D = len(names), us.stop - us.start
    print(f"[cluster] {N} signals ready in {time.time() - t0:.0f}s", flush=True)

    # pairwise, day by day, over each pair's common support (z-ranks are not re-ranked on it: coverage is >= 0.95)
    cs, cn, osum, on = np.zeros((N, N)), np.zeros((N, N)), np.zeros((N, N)), np.zeros((N, N))
    for d in range(D):
        X = np.stack([Z[k][us.start + d] for k in names]).astype(np.float64)
        m = np.isfinite(X)
        X = np.where(m, X, 0.0)
        mf = m.astype(np.float64)
        n = mf @ mf.T
        sx = X @ mf.T
        sxx = (X * X) @ mf.T
        with np.errstate(invalid="ignore", divide="ignore"):
            c = (X @ X.T - sx * sx.T / n) / np.sqrt((sxx - sx ** 2 / n) * (sxx - sx ** 2 / n).T)
        ok = np.isfinite(c) & (n >= 30)
        cs[ok] += c[ok]
        cn[ok] += 1
        H = np.stack([held[k][d] for k in names]).astype(np.float64)
        both = H @ H.T
        na = np.diag(both)
        with np.errstate(invalid="ignore", divide="ignore"):
            o = both / (0.5 * (na[:, None] + na[None, :]))
        ok = np.isfinite(o) & (na[:, None] > 0) & (na[None, :] > 0)
        osum[ok] += o[ok]
        on[ok] += 1
    with np.errstate(invalid="ignore", divide="ignore"):
        C, O = cs / cn, osum / on
    ix = {k: i for i, k in enumerate(names)}
    print(f"[cluster] pairwise correlation / overlap in {time.time() - t0:.0f}s", flush=True)

    def shp(k):
        x = spec[k]["books"]["utrain"]["long_sharpe"]
        return x if x == x else -9.0

    def similar(a, b):
        return C[ix[a], ix[b]] >= RHO or O[ix[a], ix[b]] >= OVL

    KN = [k for k in ("known", "known_xfrozen") if k in ix]

    def is_known(k):
        """Is THIS candidate the known family?  Built on it; or close to the plain benchmark (rank correlation or
        long-book overlap); or holding the same book as the screened benchmark.  For the screened benchmark only
        the overlap is read: two signals that share the screen share the fifth of the names it sends to the bottom,
        which lifts their rank correlation whatever is above it."""
        if "day_std(Amt)" in spec[k]["expr"]:
            return True
        if "known" in ix and similar(k, "known"):
            return True
        return "known_xfrozen" in ix and O[ix[k], ix["known_xfrozen"]] >= OVL

    for k in names:
        spec[k]["known_like"] = bool(is_known(k))
        for b in KN:
            spec[k][f"rho_{b}"], spec[k][f"ovl_{b}"] = float(C[ix[k], ix[b]]), float(O[ix[k], ix[b]])

    elig = sorted([k for k in names if spec[k]["role"] != "orig"], key=lambda k: -shp(k))
    heads, member_of = [], {}
    for k in elig:
        near = [h for h in heads if similar(k, h)]
        if near:
            member_of[k] = max(near, key=lambda h: C[ix[k], ix[h]])
        else:
            heads.append(k)
            member_of[k] = k
    clusters = []
    for h in heads:
        mem_ = [k for k in elig if member_of[k] == h]
        clusters.append({"head": h, "members": mem_, "known_family": bool(spec[h]["known_like"] or any(spec[k]["role"] == "bench" for k in mem_)),
                         "known_like_members": [k for k in mem_ if spec[k]["known_like"]]})
    for k in names:                                              # where does each original fall?
        if spec[k]["role"] == "orig":
            near = [h for h in heads if similar(k, h)]
            spec[k]["nearest_head"] = max(heads, key=lambda h: C[ix[k], ix[h]])
            spec[k]["in_cluster"] = max(near, key=lambda h: C[ix[k], ix[h]]) if near else None
    kn_heads = [c["head"] for c in clusters if c["known_family"]]
    known_head = kn_heads[0] if kn_heads else None               # heads are in Sharpe order
    indep = [c["head"] for c in clusters if not spec[c["head"]]["known_like"] and not c["known_family"] and shp(c["head"]) >= SH_MIN]
    print(f"[cluster] {len(clusters)} clusters; known head {known_head}; independent heads (Sharpe >= {SH_MIN:g}): {indep}", flush=True)

    def mix(keys, weights=None):
        z = np.stack([Z[k][:last] for k in keys]).astype(np.float64)
        w = np.asarray(weights if weights is not None else [1.0] * len(keys), dtype=np.float64)[:, None, None]
        fin = np.isfinite(z)
        with np.errstate(invalid="ignore", divide="ignore"):
            out = (np.where(fin, z, 0.0) * w).sum(0) / (fin * w).sum(0)
        return np.where(fin.sum(0) >= math.ceil(len(keys) / 2), out, np.nan)

    T = tgt[:last]
    evals = {"train": tr, "valid": va, "utrain": us, **({"holdout": ho} if READ else {})}

    def score(sig):
        b = bk.books(sig, T, us, evals)
        v = b["by_rank"]["long"]
        return {"hl": v["hl"], "splits": v["splits"], "by_year_long_net": by_year_net(bk.smoothed(sig, v["hl"]), T, ps.years, last)}

    combos = {}
    if known_head:
        combos["known_head"] = {"members": [known_head], **score(Z[known_head][:last].astype(np.float64))}
    if indep:
        combos["indep_eq"] = {"members": indep, **score(mix(indep))}
        if len(indep) > 3:
            combos["indep_top3"] = {"members": indep[:3], **score(mix(indep[:3]))}
        if known_head:
            combos["all_eq"] = {"members": indep + [known_head], **score(mix(indep + [known_head]))}
            ind = mix(indep)
            kz = Z[known_head][:last].astype(np.float64)
            combos["half_half"] = {"members": [known_head] + indep, "weights": "0.5 known head + 0.5 mean(independent heads)",
                                   **score(np.where(np.isfinite(ind) & np.isfinite(kz), 0.5 * ind + 0.5 * kz, np.nan))}
    if READ:
        Ledger(PARTURA_ROOT / "runs" / f"_batch_{bname}" / "ledger.json").record(
            "holdout", len(combos), f"batch cluster {TAG}: combination books defined by a fixed rule on utrain ({', '.join(combos)})",
            f"batch_cluster_{TAG}")
    loo = {}
    if len(indep) > 1:                                           # training period only
        base = bk.book_row(bk.smoothed(mix(indep), combos["indep_eq"]["hl"]), T, us)
        for h in indep:
            rest = [k for k in indep if k != h]
            sig = mix(rest)
            hl = bk.fit_halflives(sig, T, us)["hl_long"]
            r = bk.book_row(bk.smoothed(sig, hl), T, us)
            loo[h] = {"without_long_ann": r["long_ann"], "without_long_sharpe": r["long_sharpe"],
                      "d_long_ann": base["long_ann"] - r["long_ann"], "d_long_sharpe": base["long_sharpe"] - r["long_sharpe"]}
    pair = {}
    if known_head:                                               # each independent head half-and-half with the known head
        kz = Z[known_head][:us.stop].astype(np.float64)
        for h in indep:
            sig = 0.5 * kz + 0.5 * Z[h][:us.stop].astype(np.float64)
            hl = bk.fit_halflives(sig, tgt[:us.stop], us)["hl_long"]
            r = bk.book_row(bk.smoothed(sig, hl), tgt[:us.stop], us)
            pair[h] = {"hl": hl, "long_ann": r["long_ann"], "long_sharpe": r["long_sharpe"], "long_turnover": r["long_turnover"]}
    mem.stop()

out = {"batch": bname, "tag": TAG, "rule": __doc__.split("    python")[0].strip(), "thresholds": {"rho": RHO, "overlap": OVL, "min_sharpe": SH_MIN},
       "holdout_read": READ, "split": list(SPLITS["utrain"]), "names": names, "known_head": known_head, "independent_heads": indep,
       "info": {k: {x: spec[k].get(x) for x in ("expr", "sign", "hl", "kind", "role", "fid", "cid", "also", "books", "nearest_head", "in_cluster", "known_like",
                                               "rho_known", "ovl_known", "rho_known_xfrozen", "ovl_known_xfrozen")} for k in names},
       "corr": {a: {b: float(C[ix[a], ix[b]]) for b in names} for a in names},
       "overlap": {a: {b: float(O[ix[a], ix[b]]) for b in names} for a in names},
       "clusters": clusters, "combos": combos, "leave_one_out": loo, "pair_with_known_head": pair}
od = PARTURA_ROOT / "runs" / f"_batch_{bname}"
od.mkdir(parents=True, exist_ok=True)
p = od / f"cluster_{TAG}.json"
p.write_text(json.dumps(out, ensure_ascii=False, indent=1, default=float), encoding="utf-8")


def pc(x):
    return "   — " if x is None or x != x else f"{x:+5.1%}"


print(f"\n== {bname} 跨因子聚类({TAG};用户训练段;同簇 = 秩相关 ≥ {RHO:g} 或多头书重合 ≥ {OVL:.0%})==")
for i, c in enumerate(clusters, 1):
    h = c["head"]
    b = spec[h]["books"]
    kc = f"ρ已知族 {C[ix[h], ix['known']]:+.2f} 重合 {O[ix[h], ix['known']]:.0%}" if "known" in ix else ""
    print(f"[{i:2d}] {'已知族' if c['known_family'] else '独立 '} 簇首 {h:28s} hl {spec[h]['hl']:>3g} 多头净超额 训练/验证 {pc(b['train']['long_ann'])}/{pc(b['valid']['long_ann'])} "
          f"夏普 {shp(h):+.2f} {kc} | {len(c['members'])} 个成员")
    print(f"     {spec[h]['expr'][:160]}")
    for k in c["members"][1:]:
        print(f"       · {k:28s} 夏普 {shp(k):+.2f} ρ簇首 {C[ix[k], ix[h]]:+.2f} 重合 {O[ix[k], ix[h]]:.0%} | {spec[k]['expr'][:90]}")
print("\n原式落在哪个簇:")
for k in names:
    if spec[k]["role"] == "orig":
        h = spec[k]["nearest_head"]
        print(f"  {k:12s} 夏普 {shp(k):+.2f} 最近簇首 {h:28s} ρ {C[ix[k], ix[h]]:+.2f} 重合 {O[ix[k], ix[h]]:.0%} {'(同簇)' if spec[k]['in_cluster'] else '(不属于任何簇)'}")
print(f"\n组合书(成员 z-rank 的均值;半衰期在用户训练段上再定){' —— 含测试段(已记账)' if READ else ' —— 只有训练段'}")
for k, c in combos.items():
    a = c["splits"]["utrain"]
    h = c["splits"].get("holdout")
    print(f"  {k:11s} hl {c['hl']:>3g} | 训练 {pc(a['long_ann'])} 夏普 {a['long_sharpe']:+.2f} 换手 {a['long_turnover']:.1%} 回撤 {pc(a['long_mdd'])}"
          + (f" | 测试 {pc(h['long_ann'])} 夏普 {h['long_sharpe']:+.2f} 回撤 {pc(h['long_mdd'])}" if h else "")
          + " | 逐年 " + " ".join(f"{x:+.0%}" for x in c["by_year_long_net"].values()) + f" | {len(c['members'])} 个:{', '.join(c['members'])}")
if loo:
    print("\nindep_eq 去掉一个簇首之后(训练段;正 = 这个簇首有贡献):")
    for h, r in loo.items():
        print(f"  去掉 {h:28s} 净超额 {pc(r['without_long_ann'])} 夏普 {r['without_long_sharpe']:+.2f}  (贡献 {r['d_long_ann']:+.1%} / {r['d_long_sharpe']:+.2f})")
if pair:
    print("\n每个独立簇首与已知族簇首五五混合(训练段):")
    for h, r in pair.items():
        print(f"  {h:28s} hl {r['hl']:>3g} 净超额 {pc(r['long_ann'])} 夏普 {r['long_sharpe']:+.2f} 换手 {r['long_turnover']:.1%}")
print(f"\nwrote {p} ({time.time() - t0:.0f}s)")
