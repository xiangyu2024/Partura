"""W02L stage 0 (research/prod_W02L/PLAN.md): every expression of the two champion libraries computed on the new host from its
expression, over the whole history 2018-01-02 ~ 2026-09-16 (the panel goes to the shared panel cache: the 2026 test will need
it), and scored in sample under the user's split of 2026-11-08 -- train 2018-01-02 ~ 2023-08-07, valid 2023-08-08 ~ 2025-12-31.
The label after 2025-12-31 is blanked before anything is scored: no statistic of 2026 is computed here.

    source tmp/prod_env.sh
    python scripts/w02l_stage0.py <members.csv> <outdir> [--device cuda|cpu] [--batch 8] [--steal-min M] [--defer-spearman | --spearman-only]

--defer-spearman: a chunk is scored without its members that use ts_spearman (30 of 5583, all mined; on this host they do not fit
on the card and take hours each on the CPU, holding up whole batches -- and they can never be a head or material anyway);
--spearman-only: one expression per job, every ts_spearman member not in any chunk file yet -> <outdir>/chunks/sp<k>.jsonl.

Workers share one queue: chunk k (8 expressions, in members.csv order) is claimed by creating <outdir>/claims/<k> (atomic),
written to <outdir>/chunks/<k>.jsonl when done; a claim whose worker is no longer alive is released at start, so any number
of GPU and CPU workers can be started and restarted.  A CPU worker takes no GPU way (partura/panels.py) and no card memory.

Two rulers per expression, both the production reward (`partura.steer.reward(..., "long_neutral")`: rank first, EMA 0 / 5 / 20,
direction and half-life by train pure-long net Sharpe, score = the worse of train and valid):
  A  residual on the five controls (liquidity, volatility, 20-day reversal, the known Amt family, LogFloatCap), powers 1 / 2 / 3
  B  the same plus the two champions' signals (handwritten, mined) as controls -- what the champions do not already have
plus |rho| of the traded signal's daily ranks (train, every 5th day) with the known family and with each champion.
"""
import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.guard import MemoryGuard, limit_threads, slot  # noqa: E402

DEV = sys.argv[sys.argv.index("--device") + 1] if "--device" in sys.argv else "cuda"
if DEV == "cpu":                                              # never initialise the card from a CPU worker
    os.environ.pop("PARTURA_RANK_DEVICE", None)
    os.environ.pop("PARTURA_REWARD_DEVICE", None)
limit_threads(int(os.environ.get("PARTURA_THREADS", 8)))
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from partura import books as bk  # noqa: E402
from partura import diagnose as dg  # noqa: E402
from partura import ops_ext  # noqa: E402,F401
from partura import study  # noqa: E402
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.panels import SHARED_CACHE, PanelSet  # noqa: E402
from partura.steer import Guidance, RewardContext, neutral_basis  # noqa: E402
from partura.steer import reward as steer_reward  # noqa: E402

assert os.environ.get("PARTURA_RANK_FIRST") == "1" and os.environ.get("PARTURA_NEUTRAL_POWERS") == "1,2,3", "source tmp/prod_env.sh first"
IN, OUT = Path(sys.argv[1]), Path(sys.argv[2])
BATCH = int(sys.argv[sys.argv.index("--batch") + 1]) if "--batch" in sys.argv else 8
START, END = "20180102", "20260916"                           # the panel: whole history (the test will need 2026)
SPLIT, LAST = "20230808", "20251231"                          # valid from SPLIT; nothing after LAST is scored
CHAMPS = {"H": "runs/prod_W01/two_level/champions/signal_手写库冠军_20260916.npy",
          "X": "runs/prod_W01/two_level/champions/signal_挖掘冠军_20260916.npy"}
CHAMP_DATES = "runs/prod_W01/two_level/champions/two_level_forward_20260916.json"
STORE = os.environ.get("PARTURA_STORE", "/root/autodl-tmp/qmt_daily_data/fast_factor_compute")
MIRROR = os.environ.get("PARTURA_MIRROR")
MIRROR = MIRROR if MIRROR and os.path.isdir(MIRROR) else None
RHO, THR = 0.5, 0.5
G = Guidance.load(PARTURA_ROOT / "guidance" / "C05_base.yaml")
_caps = study.host_caps()
os.environ.update(PARTURA_SLOTS=_caps["PARTURA_SLOTS"], PARTURA_GPU_WAYS=_caps["PARTURA_GPU_WAYS"], PARTURA_REPROMOTE="1")

rows = pd.read_csv(IN)[["lib", "i", "expression", "batch"]].sort_values(["batch", "lib", "i"], kind="stable").reset_index(drop=True)
chunks = [rows.iloc[k:k + BATCH] for k in range(0, len(rows), BATCH)]
SP_DEFER, SP_ONLY = "--defer-spearman" in sys.argv, "--spearman-only" in sys.argv
is_sp = rows.expression.str.contains("ts_spearman", regex=False)
if SP_ONLY:                                                   # the deferred members, one per job, unless a chunk file has them
    have = {(x["lib"], int(x["i"])) for f in (OUT / "chunks").glob("*.jsonl")
            for x in (json.loads(ln) for ln in open(f, encoding="utf-8") if ln.strip())}
    sp = rows[is_sp & ~rows.apply(lambda r: (r.lib, int(r.i)) in have, axis=1)]
    chunks = [sp.iloc[[j]] for j in range(len(sp))]


def tag(k):
    return f"sp{k}" if SP_ONLY else str(k)
(OUT / "claims").mkdir(parents=True, exist_ok=True)
(OUT / "chunks").mkdir(parents=True, exist_ok=True)
for c in (OUT / "claims").iterdir():                          # release the claims of workers that are gone
    try:
        pid = int(c.read_text().split()[0])
        os.kill(pid, 0)
    except (ValueError, IndexError, ProcessLookupError, FileNotFoundError):
        if not (OUT / "chunks" / f"{c.name}.jsonl").is_file():
            c.unlink(missing_ok=True)
    except PermissionError:
        pass


STEAL = float(sys.argv[sys.argv.index("--steal-min") + 1]) if "--steal-min" in sys.argv else 0.0


def claim(k):
    if (OUT / "chunks" / f"{tag(k)}.jsonl").is_file():
        return False
    try:
        fd = os.open(OUT / "claims" / tag(k), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        # --steal-min M (a GPU worker): a chunk a CPU worker has held for more than M minutes is computed here as well -- the
        # straggler that keeps a whole stream waiting; whichever finishes first writes the (identical) result, the other one
        # finds the output there and its work is wasted, nothing else
        c = OUT / "claims" / tag(k)
        try:
            held_by_cpu = c.read_text().split()[1] == "cpu"
            age_min = (time.time() - c.stat().st_mtime) / 60
        except (OSError, IndexError):
            return False
        if not (STEAL and DEV.startswith("cuda") and held_by_cpu and age_min > STEAL):
            return False
        c.write_text(f"{os.getpid()} {DEV} stolen\n")
        return True
    os.write(fd, f"{os.getpid()} {DEV}\n".encode())
    os.close(fd)
    return True


def zr(a):
    return dg._zrank(np.asarray(a, np.float64))


def corr_rows(a, b):
    ok = np.isfinite(a) & np.isfinite(b)
    x, y = np.where(ok, a, 0.0), np.where(ok, b, 0.0)
    n = np.maximum(ok.sum(1), 1)
    with np.errstate(invalid="ignore", divide="ignore"):
        c = ((x * y).sum(1) - x.sum(1) * y.sum(1) / n) / np.sqrt(((x ** 2).sum(1) - x.sum(1) ** 2 / n) * ((y ** 2).sum(1) - y.sum(1) ** 2 / n))
    return float(np.nanmean(c))


with slot(name="slot"):                                       # its own slots: the rounds use $PARTURA_SLOT_NAME
    mem = MemoryGuard(self_limit_gb=float(os.environ.get("PARTURA_SELF_LIMIT_GB", 150)),
                      cgroup_limit_gb=float(os.environ.get("PARTURA_CGROUP_LIMIT_GB", 850))).start()
    t0 = time.time()
    from alphacube.plugins import load_plugins
    load_plugins(["partura.ac_plugin"])
    ps = PanelSet(STORE, START, END, warmup=60, device=DEV, gpu_fraction=0.4 if DEV.startswith("cuda") else None,
                  cache_dir=str(SHARED_CACHE), mirror_root=MIRROR, workdir=str(PARTURA_ROOT / "tmp"), label_kind="open_vwap15",
                  label_buyable=True, batch=BATCH, daily_root=os.environ.get("PARTURA_DAILY_ROOT") or None)
    dates = np.asarray([str(d) for d in ps.dates])
    cut, vend = int(np.searchsorted(dates, SPLIT)), int(np.searchsorted(dates, LAST, side="right"))
    assert dates[cut - 1] == "20230807" and dates[vend - 1] <= LAST < (dates[vend] if vend < len(dates) else "99999999")
    tgt = np.array(ps.target(1), np.float64)
    tgt[vend:] = np.nan                                       # 2026 is the test: its label never enters a number here
    tr, va = slice(0, cut), slice(cut, vend)
    pool_spec, known_spec = G.spec["pool"][-1], G.spec["pool"][0]
    aux = ps.compute({"frozen": "cross_max(day_zero_ratio(Ret), 15)", "age": "cross_valid_count(day_last(Close), 241)",
                      "liq": "cross_mean(day_sum(Amt), 30)", "pool": pool_spec["expr"], "known": known_spec["expr"],
                      "n_vol": "cross_mean(day_std(Ret), 20)", "n_rev": "div(day_last(Close), ts_delay(day_last(Close), 20))", "n_size": "LogFloatCap"})
    cd = [str(d) for d in json.loads((PARTURA_ROOT / CHAMP_DATES).read_text(encoding="utf-8"))["dates"]]
    pos = {d: j for j, d in enumerate(cd)}
    assert all(d in pos for d in dates), "champion dates do not cover the view"
    take = np.array([pos[d] for d in dates])
    champ = {k: np.asarray(np.load(PARTURA_ROOT / f, mmap_mode="r"), np.float64)[take] for k, f in CHAMPS.items()}
    frozen = np.asarray(aux["frozen"], np.float64)
    possible = np.minimum(241, np.arange(1, len(dates) + 1))[:, None]
    untradable = ((dg._zrank(frozen) + 0.5) > 0.8) | (np.asarray(aux["age"], np.float64) < 0.9 * possible) | ~np.isfinite(frozen)
    pool_sig = dg._zrank(bk.smoothed(float(pool_spec["sign"]) * np.asarray(aux["pool"], np.float64), float(pool_spec["hl"])))
    ctl5 = [aux["liq"], aux["n_vol"], aux["n_rev"], aux["known"], aux["n_size"]]
    ctx = {}
    for name, ctls in (("A", ctl5), ("B", ctl5 + [champ["H"], champ["X"]])):
        c = RewardContext(tgt, tr, va, untradable=untradable, liq=np.asarray(aux["liq"], np.float64), pool=pool_sig, base=pool_sig,
                          halflives=(0.0, 5.0, 20.0))
        c.neutral_Q = neutral_basis(ctls)
        ctx[name] = c
    ref = {"known": zr(float(known_spec["sign"]) * np.asarray(aux["known"], np.float64))[:cut:5],
           "H": zr(champ["H"])[:cut:5], "X": zr(champ["X"])[:cut:5]}
    labelled = np.isfinite(tgt)
    print(f"[s0] {DEV} worker ready in {time.time() - t0:.0f}s: {len(dates)} days x {tgt.shape[1]} names ({dates[0]} ~ {dates[-1]}); "
          f"train {cut}, valid {vend - cut} days (to {dates[vend - 1]}); {len(chunks)} chunks", flush=True)

    n_done = 0

    def next_chunk():
        """The first chunk this worker may take (scanning from the start every time, so a stealing worker always takes the
        earliest straggler); None when there is nothing to take now."""
        for k in range(len(chunks)):
            if claim(k):
                return k
        return None

    while True:
        k = next_chunk()
        if k is None:
            if not STEAL or all((OUT / "chunks" / f"{tag(j)}.jsonl").is_file() for j in range(len(chunks))):
                break
            time.sleep(60)                                    # a stealing worker waits for a chunk to become stale
            continue
        ch = chunks[k]
        if SP_DEFER:
            ch = ch[~ch.expression.str.contains("ts_spearman", regex=False)]
        t1 = time.time()
        exprs = list(ch.expression)
        P, err = {}, {}
        try:
            P = ps.compute({f"v{j}": e for j, e in enumerate(exprs)})
        except Exception:                                     # noqa: BLE001
            for j, e in enumerate(exprs):
                try:
                    P[f"v{j}"] = ps.compute({"x": e})["x"]
                except Exception as exc:                      # noqa: BLE001
                    err[j] = f"{type(exc).__name__}: {str(exc)[:160]}"
        lines = []
        for j, r in enumerate(ch.itertuples(index=False)):
            out = {"lib": r.lib, "i": int(r.i), "expression": r.expression, "batch": r.batch}
            if f"v{j}" not in P:
                out["error"] = err.get(j, "did not compute")
                lines.append(out)
                continue
            panel = np.asarray(P[f"v{j}"], np.float64)
            out.update(coverage=float(np.isfinite(panel[labelled]).mean()), distinct=float(dg.distinct_fraction(panel[:vend])))
            out["gate"] = bool(out["coverage"] >= 0.9 and out["distinct"] >= 0.5)
            if out["gate"]:
                for name, c in ctx.items():
                    rw = steer_reward(panel, c, "long_neutral")
                    out[name] = {"score": float(rw["score"]), "sign": float(rw["sign"]), "hl": float(rw["hl"]),
                                 "train": float(rw["train"]["long_sharpe"]), "valid": float(rw["valid"]["long_sharpe"]),
                                 "train_ann": float(rw["train"]["long_ann"]), "valid_ann": float(rw["valid"]["long_ann"]),
                                 "turnover": float(rw["train"]["long_turnover"])}
                z = zr(out["A"]["sign"] * panel[:cut:5])
                out["rho"] = {k2: corr_rows(z, v) for k2, v in ref.items()}
                out["discovery_A"] = bool(out["A"]["score"] >= THR and abs(out["rho"]["known"]) < RHO)
                out["discovery_B"] = bool(out["B"]["score"] >= THR and abs(out["rho"]["known"]) < RHO)
            lines.append(out)
        ps._mem.clear()                                       # PanelSet keeps every panel it computed in memory (44 MB each); they
        del P                                                 # are on disk in the panel cache already -- a worker would grow by ~40 GB
        if (OUT / "chunks" / f"{tag(k)}.jsonl").is_file():      # the other worker finished first (a stolen chunk)
            continue
        tmp = OUT / "chunks" / f".{tag(k)}.{os.getpid()}.jsonl.tmp"
        tmp.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in lines), encoding="utf-8")
        tmp.rename(OUT / "chunks" / f"{tag(k)}.jsonl")
        n_done += 1
        print(f"[s0] chunk {k} ({len(lines)} expr, {time.time() - t1:.0f}s); this worker {n_done} chunks in {time.time() - t0:.0f}s", flush=True)
print("[s0] queue empty", flush=True)
