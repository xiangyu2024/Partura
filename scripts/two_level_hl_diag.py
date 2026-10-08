"""Why does a rebuilt two-level signal miss (or nearly miss) the stage-2 reproduction check?

Server side.  Uses data up to 2025-12-31 only: the stored signal (pools/signals/<name>.npy) and the first 1942 days
of the rebuilt one (runs/_forward/signal_<name>_<end>.npy), both scored against the pool's own stored label.

For each signal and each version: the half-life the in-sample fit picks for the pure long book, the in-sample long
Sharpe at each half-life (how close the tie is), and the test-period pure-long net excess at half-lives 5 / 10 / 20.
The last line per signal compares the two versions AT THE SAME half-life, which is the question the check meant to ask.

    python scripts/two_level_hl_diag.py [--end 20260916]      -> runs/_forward/two_level_hl_diag_<end>.json
"""
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura import books as bk  # noqa: E402

P = Path(__file__).resolve().parents[1]
argv = sys.argv[1:]
END = argv[argv.index("--end") + 1] if "--end" in argv else "20260916"
us, ho = slice(0, 1359), slice(1359, 1942)
out = {}
for name in ("C_Q", "C_LQ", "C_MQ", "C_LM", "C_LMQ"):
    tgt = np.load(P / "pools" / name[2:] / "_target.npy").astype(np.float64)
    vers = {"stored": np.load(P / "pools" / "signals" / f"{name}.npy").astype(np.float64),
            "rebuilt": np.load(P / "runs" / "_forward" / f"signal_{name}_{END}.npy")[:tgt.shape[0]].astype(np.float64)}
    out[name] = {}
    for nm, s in vers.items():
        assert s.shape == tgt.shape, (name, nm, s.shape, tgt.shape)
        f = bk.fit_halflives(s, tgt, us)
        test = {}
        for hl in (5, 10, 20):
            r = bk.book_row(bk.smoothed(s, hl), tgt, ho)
            test[str(hl)] = {"long_ann": r["long_ann"], "long_sharpe": r["long_sharpe"]}
        out[name][nm] = {"hl_long": f["hl_long"], "hl_ls": f["hl_ls"], "insample_long_sharpe": {str(int(r["halflife"])): r["long_sharpe"] for r in f["sweep"]}, "test": test}
    a, b = out[name]["stored"], out[name]["rebuilt"]
    out[name]["same_hl_diff_points"] = {k: 100 * (b["test"][k]["long_ann"] - a["test"][k]["long_ann"]) for k in a["test"]}
    print(f"== {name}: stored picks hl {a['hl_long']:g}, rebuilt picks hl {b['hl_long']:g}")
    for nm in ("stored", "rebuilt"):
        v = out[name][nm]
        print(f"  {nm:7s} in-sample long Sharpe by hl: " + " ".join(f"{k}:{x:.3f}" for k, x in v["insample_long_sharpe"].items() if k in ("3", "5", "10", "20", "40"))
              + " | test long ann/Sharpe: " + " ".join(f"hl{k}:{x['long_ann'] * 100:+.2f}%/{x['long_sharpe']:.2f}" for k, x in v["test"].items()))
    print("  same half-life, rebuilt minus stored (test long ann, points): " + " ".join(f"hl{k}:{x:+.2f}" for k, x in out[name]["same_hl_diff_points"].items()))
dst = P / "runs" / "_forward" / f"two_level_hl_diag_{END}.json"
dst.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"wrote {dst}")
