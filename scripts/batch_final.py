"""分辨, at the end of a batch: are the picks of the studies N factors or one?

Every study of a batch ends with a recommended candidate.  A long-only user
who adds them to a book wants to know which of those are the same thing
twice, and which add something to what is already known.  This takes, for
every factor of the batch, the ORIGINAL and the PICK (plus the known-family
benchmarks), builds the signal that would be traded under the selection
convention -- sign x panel, causal EMA at the half-life the pure long book
prefers on the user's training period -- and reports, on that training
period only (the holdout is not touched):

* the daily cross-sectional rank correlation of every pair,
* the overlap of their long books (share of the top decile two signals share),
* what the pure long book of each earns, net, on train / valid / both,
* what is left of each pick's long book once the known family is taken out of
  the signal (rank-space residual), and what a 50/50 rank blend with the known
  family earns compared with the known family alone.

All panels come out of the shared content-addressed cache the studies filled;
only a pick nobody evaluated is computed.

    python scripts/batch_final.py batches/B01_picks.yaml
"""
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.guard import MemoryGuard, limit_threads, slot  # noqa: E402

limit_threads(2)
import numpy as np  # noqa: E402
import yaml  # noqa: E402

from partura import books as bk  # noqa: E402
from partura import diagnose as dg  # noqa: E402
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.panels import SHARED_CACHE, PanelSet  # noqa: E402
from partura.splits import SPLITS  # noqa: E402

picks = yaml.safe_load(open(sys.argv[1], encoding="utf-8"))
batch = yaml.safe_load(open(PARTURA_ROOT / "batches" / f"{picks['batch']}.yaml", encoding="utf-8"))
first = yaml.safe_load(open(PARTURA_ROOT / "configs" / f"{batch['factors'][0]['id']}.yaml", encoding="utf-8"))
for k, v in first["splits"].items():
    SPLITS[k] = (str(v[0]), str(v[1]))
KNOWN = picks.get("known", "known_stdamt_mean30")

with slot():
    mem = MemoryGuard().start()
    ps = PanelSet("/root/autodl-tmp/qmt_daily_data/fast_factor_compute", SPLITS["full"][0], SPLITS["full"][1],
                  warmup=60, device="cuda", gpu_fraction=0, cache_dir=str(SHARED_CACHE),
                  mirror_root="/root/autodl-tmp/AlphaCube/mirror", workdir=str(PARTURA_ROOT / "tmp"),
                  label_kind="open_vwap15", label_buyable=True, batch=2)
    spec = {}                                   # key -> (expr, sign, label)
    for f in batch["factors"]:
        short = f["id"].split("_")[0]
        spec[f"{short}.orig"] = (f["expr"], float(f["sign"]), f["name"])
        p = picks["picks"].get(f["id"])
        if p and p.get("expr") and p["expr"].replace(" ", "") != f["expr"].replace(" ", ""):
            spec[f"{short}.pick"] = (p["expr"], float(p["sign"]), p.get("kind", ""))
    for k, b in picks.get("benchmarks", {}).items():
        spec[k] = (b["expr"], float(b["sign"]), "benchmark")
    panels = ps.compute({k: v[0] for k, v in spec.items()})
    tgt = ps.target(1)
    tr, va, us = ps.split_slice("train"), ps.split_slice("valid"), ps.split_slice("utrain")
    t0 = time.time()

    sig, info = {}, {}
    for k, (expr, sign, label) in spec.items():
        p = panels.get(k)
        if p is None:
            print(f"{k}: no panel ({ps.errors.get(k)})", flush=True)
            continue
        s = sign * np.asarray(p, dtype=np.float64)
        hl = bk.fit_halflives(s, tgt, us)["hl_long"]
        sm = bk.smoothed(s, hl)
        rows = {name: bk.book_row(sm, tgt, d) for name, d in (("train", tr), ("valid", va), ("utrain", us))}
        sig[k] = sm[us]
        info[k] = {"expr": expr, "sign": sign, "label": label, "hl_long": hl,
                   **{f"{name}_{m}": rows[name][m] for name in rows
                      for m in ("long_ann", "long_sharpe", "long_gross_ann", "long_turnover", "ls_sharpe")}}
        print(f"{k:24s} hl {hl:>4g}  long net utrain {rows['utrain']['long_ann']:+.1%} "
              f"(train {rows['train']['long_ann']:+.1%}, valid {rows['valid']['long_ann']:+.1%})  "
              f"Sharpe {rows['utrain']['long_sharpe']:+.2f}", flush=True)
    names = list(sig)
    t_us = tgt[us]

    ranks = {k: dg.rank_rows(v) for k, v in sig.items()}
    from alphacube.metrics import cs_pearson, long_short_weights, nanmean_quiet
    corr = {a: {} for a in names}
    for i, a in enumerate(names):
        for b in names[i:]:
            c = nanmean_quiet(cs_pearson(ranks[a], ranks[b]))
            corr[a][b] = corr[b][a] = c
    print(f"rank correlations in {time.time() - t0:.0f}s", flush=True)

    # overlap of the long books: of the names one signal holds, the share the other holds too
    held = {k: long_short_weights(v, bk.TOP_FRAC) > 0 for k, v in sig.items()}
    overlap = {a: {} for a in names}
    for i, a in enumerate(names):
        na = held[a].sum(1)
        for b in names[i:]:
            both = (held[a] & held[b]).sum(1)
            with np.errstate(invalid="ignore", divide="ignore"):
                o = float(np.nanmean(np.where(na > 0, both / np.maximum(na, 1), np.nan)))
            overlap[a][b] = overlap[b][a] = o

    # what each signal adds to the known family, as a long-only book
    marg = {}
    if KNOWN in sig:
        kz = dg._zrank(sig[KNOWN])
        base = bk.book_row(sig[KNOWN], t_us, slice(None))
        for k in names:
            if k == KNOWN:
                continue
            y = dg._zrank(sig[k])
            res, i1 = dg.neutralise(y, {KNOWN: kz}, panel_ready=True, controls_ready=True)
            rr = bk.book_row(res, t_us, slice(None))
            blend = bk.book_row(0.5 * y + 0.5 * kz, t_us, slice(None))
            marg[k] = {"r2_by_known": i1["mean_r2"], "resid_long_ann": rr["long_ann"],
                       "resid_long_sharpe": rr["long_sharpe"], "resid_long_gross_ann": rr["long_gross_ann"],
                       "blend_long_ann": blend["long_ann"], "blend_long_sharpe": blend["long_sharpe"],
                       "known_long_ann": base["long_ann"], "known_long_sharpe": base["long_sharpe"]}
            print(f"{k:24s} R2 by {KNOWN} {i1['mean_r2']:.3f}  residual long net {rr['long_ann']:+.1%} "
                  f"(Sharpe {rr['long_sharpe']:+.2f})  blend {blend['long_ann']:+.1%} / {blend['long_sharpe']:+.2f} "
                  f"vs known alone {base['long_ann']:+.1%} / {base['long_sharpe']:+.2f}", flush=True)
    mem.stop()

out_dir = PARTURA_ROOT / "runs" / f"_batch_{picks['batch'].split('_')[0]}"
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "final_overview.json").write_text(json.dumps(
    {"info": info, "corr": corr, "overlap": overlap, "marginal": marg, "known": KNOWN,
     "split": list(SPLITS["utrain"]),
     "note": "signals are sign x panel, EMA-smoothed at the half-life the pure long book prefers on utrain; "
             "everything here is measured on utrain (train+valid) only -- the holdout is not read"},
    ensure_ascii=False, indent=1, default=float), encoding="utf-8")
print("wrote", out_dir / "final_overview.json", flush=True)
