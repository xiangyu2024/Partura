"""Member factors of two-level champions on the EXTENDED view (2018-01-02 .. the store's last day).

Server.  A champion is fitted on the training period only, but to carry it into the forward segment its member
factors must exist there.  This computes -- factor VALUES only, no returns, no fitting -- every member expression
of the given champions on the extended view and leaves the panels in Partura's panel cache, so that the later step
(refit on the first 1359 days with AlphaCube's own functions, check against the stored signal on the overlap, read
the forward segment by research/two_level/PLAN.md) is quick.

    extend_members.py name=<pool dir>:<families.json> [name=... ...] [--dry] [--out runs/_forward/members_<end>.json]

A champion's families.json is what build_champion.py writes next to its signal: [{"members": [i, ...], ...}, ...],
with i = the row index in the pool's metrics.csv (whose ``expression`` column is evaluated here).
"""
import csv
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.guard import MemoryGuard, limit_threads, slot  # noqa: E402

limit_threads(8)
from partura import ops_ext  # noqa: E402,F401
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.panels import SHARED_CACHE, PanelSet, parse_research  # noqa: E402

argv = sys.argv[1:]


def opt(name, default=None):
    return argv[argv.index(name) + 1] if name in argv else default


STORE, MIRROR = "/root/autodl-tmp/qmt_daily_data/fast_factor_compute", "/root/autodl-tmp/AlphaCube/mirror"
champs = dict(a.split("=", 1) for a in argv if "=" in a and not a.startswith("-"))
csv.field_size_limit(10 ** 9)
with slot():
    mem = MemoryGuard(self_limit_gb=30, cgroup_limit_gb=70).start()
    t0 = time.time()
    from alphacube.store import open_cube_store
    END = opt("--end") or str(open_cube_store(STORE, mirror_root=MIRROR).dates[-1])
    ps = PanelSet(STORE, "20180102", END, warmup=60, device="cuda", gpu_fraction=0, cache_dir=str(SHARED_CACHE), mirror_root=MIRROR,
                  workdir=str(PARTURA_ROOT / "tmp"), label_kind="open_vwap15", label_buyable=True, batch=16)
    out = {"end": END, "view_id": ps.view_id, "champions": {}, "expressions": {}}
    todo = {}
    for name, spec in champs.items():
        pool, fam = spec.split(":", 1)
        if not Path(fam).is_file():
            print(f"[members] {name}: no {fam} -- skipped", flush=True)
            continue
        expr_of = {int(r["i"]): r["expression"] for r in csv.DictReader(open(Path(pool) / "metrics.csv", encoding="utf-8"))}
        fams = json.loads(Path(fam).read_text(encoding="utf-8"))
        rec, n = [], 0
        for f in fams:
            ms = []
            for i in f["members"]:
                e = expr_of[int(i)]
                k = e.replace(" ", "")
                todo.setdefault(k, e)
                ms.append({"i": int(i), "key": k})
                n += 1
            rec.append(ms)
        out["champions"][name] = {"pool": pool, "families_json": fam, "families": rec, "members": n}
        print(f"[members] {name}: {len(fams)} families, {n} members", flush=True)
    bad, keys = {}, {}
    for k, e in todo.items():
        try:
            keys[k] = parse_research(e, n_minutes=ps.store.n_minutes).key()
        except Exception as exc:                              # noqa: BLE001
            bad[k] = f"parse: {type(exc).__name__}: {str(exc)[:120]}"
    cached = [k for k in keys if (ps._cache_path(keys[k]) is not None and ps._cache_path(keys[k]).is_file())]
    miss = [k for k in keys if k not in set(cached)]
    print(f"[members] {len(todo)} distinct member expressions on the view to {END}: {len(cached)} cached, {len(miss)} to compute, {len(bad)} do not parse", flush=True)
    if "--dry" not in argv:
        for a in range(0, len(miss), 48):
            chunk = miss[a:a + 48]
            ps.compute({k: todo[k] for k in chunk})
            ps._mem.clear()
            for k in chunk:
                if k in ps.errors:
                    bad[k] = str(ps.errors[k])[:200]
            print(f"[members] {min(a + 48, len(miss))}/{len(miss)} computed, {len(bad)} failed so far ({time.time() - t0:.0f}s)", flush=True)
            (PARTURA_ROOT / "runs" / "_forward").mkdir(parents=True, exist_ok=True)
    for k, e in todo.items():
        p = ps._cache_path(keys[k]) if k in keys else None
        out["expressions"][k] = {"expr": e, "path": str(p) if p is not None and p.is_file() else None, "error": bad.get(k)}
    mem.stop()
p = PARTURA_ROOT / (opt("--out") or f"runs/_forward/members_{out['end']}.json")
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")
ok = sum(1 for v in out["expressions"].values() if v["path"])
print(f"[members] wrote {p}: {ok} of {len(out['expressions'])} member panels available ({time.time() - t0:.0f}s)")
for k, v in list(bad.items())[:12]:
    print(f"   failed: {v[:120]} | {todo[k][:90]}")
