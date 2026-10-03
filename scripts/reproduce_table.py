"""Does Partura's `books` reproduce the user's published single-factor table?

Reads the base panels the other session already scored (no engine call, no GPU),
runs `partura.books` in the user's convention -- sign from the training-period
rank IC, half-life fitted on the training period, decile L/S and long-leg
excess on train / test -- and prints them next to the published numbers.
Nothing in Partura is comparable with that table until this agrees.

    python scripts/reproduce_table.py batches/B01_single_factors.yaml
"""
import csv
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.guard import limit_threads  # noqa: E402

limit_threads(2)
import numpy as np  # noqa: E402
import yaml  # noqa: E402

from partura.books import books  # noqa: E402

AC = Path("/root/autodl-tmp/AlphaCube")
LIBS = {"手写": AC / "_bench/trainto/legacy", "挖掘": AC / "_bench/trainto/allfac_buyable"}

cfg = yaml.safe_load(open(sys.argv[1], encoding="utf-8"))
split = int(cfg["split_index"])
target = np.asarray(np.load(LIBS["挖掘"] / "_target.npy", mmap_mode="r"), dtype=np.float64)
man = {k: {r["expression"]: r for r in csv.DictReader(open(d / "manifest.csv", encoding="utf-8"))}
       for k, d in LIBS.items()}
met = {k: {r["i"]: r for r in csv.DictReader(open(d / "metrics.csv", encoding="utf-8"))} for k, d in LIBS.items()}

out = []
print(f"{'factor':<28}{'sgn':>4}{'hl':>4} | {'LS tr':>7}{'LS te':>7} | {'long tr':>8}{'long te':>8} || "
      f"published: {'hl':>3}{'LS tr':>7}{'LS te':>7}{'long tr':>8}{'long te':>8}  match", flush=True)
for f in cfg["factors"]:
    t0 = time.time()
    row = man[f["lib"]][f["expr"]]
    i = int(row["i"])
    p = np.asarray(np.load(LIBS[f["lib"]] / "panels" / f"{i:05d}.npy", mmap_mode="r"), dtype=np.float64)
    p[~np.isfinite(p)] = np.nan
    sign = float(np.sign(float(met[f["lib"]][str(i)]["rank_ic_train"])))
    b = books(sign * p, target, slice(0, split), {"train": slice(0, split), "test": slice(split, p.shape[0])},
              rank_by="ls")
    tr, te = b["splits"]["train"], b["splits"]["test"]
    ok = (abs(tr["ls_sharpe"] - f["ls"][0]) < 0.006 and abs(te["ls_sharpe"] - f["ls"][1]) < 0.006
          # the published "多头腿年化超额" is the GROSS long-leg excess at the L/S half-life
          # (established by this very check: the net figure is 6.0% where the table says 13.6%)
          and abs(tr["long_gross_ann"] - f["long"][0]) < 0.0006 and abs(te["long_gross_ann"] - f["long"][1]) < 0.0006
          and b["hl_ls"] == f["hl"] and sign == f["sign"])
    print(f"{f['id']:<28}{sign:>+4.0f}{b['hl_ls']:>4.0f} | {tr['ls_sharpe']:>+7.2f}{te['ls_sharpe']:>+7.2f} | "
          f"{tr['long_gross_ann']:>+8.1%}{te['long_gross_ann']:>+8.1%} || "
          f"           {f['hl']:>3}{f['ls'][0]:>+7.2f}{f['ls'][1]:>+7.2f}{f['long'][0]:>+8.1%}{f['long'][1]:>+8.1%}  "
          f"{'OK' if ok else 'DIFF'}  ({time.time()-t0:.0f}s)", flush=True)
    out.append({"id": f["id"], "lib_i": i, "sign": sign, "ok": bool(ok), "books": b})
dest = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).resolve().parents[1] / "runs" / "_reproduce_B01.json"
dest.parent.mkdir(parents=True, exist_ok=True)
dest.write_text(json.dumps(out, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
print(f"{sum(o['ok'] for o in out)}/{len(out)} rows reproduce the published table; wrote {dest}", flush=True)
