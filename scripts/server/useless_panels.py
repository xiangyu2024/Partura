"""Which stored factor panels of the mined library were judged useless as soon as they were scored -- and how much disk
deleting them would free.  Server, read-only: it writes a list and a removal script, it removes nothing.

A panel (AlphaCube/_bench/allfac/panels/<i>.npy, one mined factor's values on 2018-2025) is a candidate when, using
TRAINING-PERIOD numbers only (nothing from the test period):
  * the factor is unhealthy, or its decile long-short net Sharpe on the training period (in the direction chosen on
    the training period, 15 bp) is <= 0 under the original label AND under the buyable label; and
  * it is a member of no champion family (champion_signal_{buyable,hs300}.families.json, _bench/ and _bench/trainto/).
The same file is hard-linked into other folders (allfac_buyable, allfac_hs300, Partura/pools/*): disk is freed only when
every link goes, so links are mapped by inode.  Two tiers:
  tier 1  every link is inside AlphaCube/_bench/allfac* -- no Partura pool uses the file;
  tier 2  some link is in Partura/pools/* (the two-level pools LM / LMQ / MQ): removing it breaks an exact rerun of
          those pools until the panel is recomputed from its expression (manifest.csv keeps every expression).

    python useless_panels.py      -> AlphaCube/_bench/useless_panels.csv, useless_panels_tier1.sh, useless_panels_tier2.sh
"""
import json
import os
from collections import defaultdict
from pathlib import Path

import pandas as pd

ROOT = Path("/root/autodl-tmp")
B = ROOT / "AlphaCube" / "_bench"
x = pd.read_csv(B / "allfac" / "metrics.csv").set_index("i")
b = pd.read_csv(B / "allfac_buyable" / "metrics.csv").set_index("i")
champ = set()
for f in ("champion_signal_buyable.families.json", "champion_signal_hs300.families.json",
          "trainto/champion_signal_buyable.families.json", "trainto/champion_signal_hs300.families.json"):
    for fam in json.loads((B / f).read_text()):
        champ |= set(int(m) for m in fam["members"])
bad = (x.healthy != True) | ((x.net_sharpe_train <= 0) & (b.net_sharpe_train.reindex(x.index) <= 0))   # noqa: E712
cand = [int(i) for i in x.index[bad] if int(i) not in champ]

links = defaultdict(list)                                   # inode -> every path of that file under the two trees
for top in (B, ROOT / "Partura" / "pools"):
    for dp, _, fs in os.walk(top):
        for f in fs:
            if f.endswith(".npy"):
                p = os.path.join(dp, f)
                st = os.stat(p)
                if st.st_size > 10_000_000:
                    links[st.st_ino].append(p)

rows, seen = [], set()
for i in cand:
    for folder in ("allfac", "allfac_buyable", "allfac_hs300"):
        p = B / folder / "panels" / f"{i:05d}.npy"
        if not p.exists():
            continue
        st = os.stat(p)
        if st.st_ino in seen:
            continue
        seen.add(st.st_ino)
        paths = links[st.st_ino]
        tier = 2 if any("/Partura/pools/" in q for q in paths) else 1
        rows.append({"i": i, "folder": folder, "tier": tier, "bytes": st.st_size, "nlink": st.st_nlink, "links_found": len(paths),
                     "healthy": bool(x.loc[i, "healthy"]), "net_sharpe_train": float(x.loc[i, "net_sharpe_train"]),
                     "net_sharpe_train_buyable": float(b.loc[i, "net_sharpe_train"]), "expression": x.loc[i, "expression"],
                     "paths": " ".join(paths)})
R = pd.DataFrame(rows)
R.to_csv(B / "useless_panels.csv", index=False)
for t in (1, 2):
    S = R[R.tier == t]
    lines = ["#!/bin/bash", f"# removes tier-{t} panels listed in useless_panels.csv ({len(S)} files, {S.bytes.sum() / 1e9:.1f} GB freed); every hard link of each file",
             "set -e"] + [f"rm -f {p}" for ps in S.paths for p in ps.split()]
    (B / f"useless_panels_tier{t}.sh").write_text("\n".join(lines) + "\n")
complete = R[R.nlink == R.links_found]
print(f"factors in the mined library: {len(x)}; champion members: {len(champ)}; candidates: {len(cand)}")
for t in (1, 2):
    S = R[R.tier == t]
    print(f"tier {t}: {len(S)} files, {S.bytes.sum() / 1e9:.1f} GB freed if removed "
          f"(every link found for {int((S.nlink == S.links_found).sum())} of them)")
print("by folder:", R.groupby(["folder", "tier"]).bytes.agg(["count", "sum"]).assign(GB=lambda d: d["sum"] / 1e9)[["count", "GB"]].to_dict("index"))
print(f"wrote {B / 'useless_panels.csv'} and useless_panels_tier1.sh / tier2.sh (nothing removed)")
