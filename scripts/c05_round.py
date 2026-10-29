"""C05 round runner (research/coldstart_C05/PLAN.md §2.2-2.5).  Server.

    python scripts/c05_round.py A <seed> <round>                 A: two plain GP runs (population 32, budget 128 each)
    python scripts/c05_round.py b0plan <seed> <round>            B0's plan, following B's: as many E / N slots and R variants as
                                                                 arms/s<seed>_B_r<round>.yaml, chosen by the mechanical rules
    python scripts/c05_round.py mission <seed> <B|B0> <round>    the plan arms/s<seed>_<arm>_r<round>.yaml: two GP slots (E / N,
                                                                 population 32, budget 96 each) and the R variants (direct)
Each writes arms/s<seed>_<arm>_r<round>.DONE ("<tag> <exit code>" per job) when every job has ended.
Every GP run is banned from the arm's library: M batches 1..round + the arm's own earlier missions (rank |rho| >= 0.7, same skeleton).
"""
import glob
import json
import os
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import c05_lib  # noqa: E402

D, EP = ROOT / "research" / "coldstart_C05", ROOT / "episodes"
ARMS = D / "arms"
PY = os.environ.get("PY", sys.executable)
MODE = sys.argv[1]


def snapshot(S, X, K):
    """M batches 1..K, then the arm's missions of rounds < K.  A mission whose round has ended (its .DONE exists) but that left no
    evidence failed twice: it spent its budget and produced nothing, so it is left out (PLAN revision 6)."""
    eps = [EP / f"c05s{S}M{e}_I0_open_search" for e in range(1, K + 1)]
    for k in range(1, K):
        eps += [Path(p) for p in sorted(glob.glob(str(EP / f"c05s{S}{X}r{k}[ab]_*")))
                if (Path(p) / "evidence.json").is_file() or not (ARMS / f"s{S}_{X}_r{k}.DONE").is_file()]
    return eps


def library(S, X, K):
    """The arm's library for round K (heads, with the arm's R replacements of earlier rounds added as members too)."""
    lib = c05_lib.heads(snapshot(S, X, K))
    for k in range(1, K):
        f = ARMS / f"s{S}_{X}_r{k}_R.json"
        if f.is_file():
            lib += [{**r, "src": f.name} for r in json.loads(f.read_text(encoding="utf-8"))["replacements"]]
    f = ARMS / f"lib_s{S}_{X}_r{K}.json"
    f.write_text(json.dumps(lib, ensure_ascii=False, indent=1), encoding="utf-8")
    return f, lib


class Done:
    """A job that already ended well (resumable runner, PLAN revision 7): nothing to wait for."""
    def wait(self):
        return 0


class Adopted:
    """A job of the same name still running from an earlier runner (PLAN revision 7): wait for it instead of starting a twin."""
    def __init__(self, pattern, ep_glob=None):
        self.pattern, self.ep_glob = pattern, ep_glob

    def wait(self):
        import time as _t
        while running(self.pattern):
            _t.sleep(30)
        if self.ep_glob is None:
            return 0
        eps = glob.glob(self.ep_glob)
        return 0 if eps and c05_lib.finished(eps[0]) else 1


def running(pattern):
    """Is a process whose command line contains ``pattern`` alive (other than this one)?"""
    me = os.getpid()
    for d in os.listdir("/proc"):
        if d.isdigit() and int(d) != me:
            try:
                cmd = open(f"/proc/{d}/cmdline", "rb").read().replace(b"\0", b" ").decode(errors="replace")
            except OSError:
                continue
            if pattern in cmd and "timeout" not in cmd.split()[0]:
                return True
    return False


def gp(tag, idea, guidance, arm, seed, budget, extra):
    log = ROOT / "logs" / f"_idea_{tag}.log"
    cmd = ["timeout", "--signal=TERM", "--kill-after=60", f"{os.environ.get('C05_JOB_MINUTES', 720)}m", PY, "-u", "scripts/idea_search.py", idea,
           "--guidance", guidance, "--arms", arm, "--seed", str(seed), "--tag", tag, "--budget", str(budget), "--population", "32",
           "--threshold", "0.5", *extra]
    # scheduling only (PLAN revisions 2, 6): two GPU ways, four run slots, a panel cache of at most 24 GB
    env = {**os.environ, "PARTURA_GPU_WAYS": "2", "PARTURA_SLOTS": "4",
           "PARTURA_PANEL_CACHE_GB": str(min(24.0, float(os.environ.get("PARTURA_PANEL_CACHE_GB", 6))))}
    CMDS[tag] = (cmd, env, budget)
    eps = glob.glob(str(EP / f"{tag}_*"))
    if eps and c05_lib.finished(eps[0]) and not broken_ep(eps[0], budget):     # resumable runner (PLAN revision 7)
        print(f"{tag}: already finished, not rerun", flush=True)
        return tag, Done()
    if running(f"--tag {tag} "):
        print(f"{tag}: still running from an earlier runner, adopted", flush=True)
        return tag, Adopted(f"--tag {tag} ", str(EP / f"{tag}_*"))
    return tag, subprocess.Popen(cmd, cwd=ROOT, stdout=log.open("w"), stderr=subprocess.STDOUT, env=env)


CMDS = {}


def broken_ep(ep, budget):
    for A in json.loads((Path(ep) / "evidence.json").read_text(encoding="utf-8"))["arms"].values():
        if A.get("live", 0) == 0 or A.get("scored", 0) < 0.25 * budget:
            return True
    return False


def broken(tag):
    """PLAN revision 6: a GP run whose evaluations failed in the engine (no GPU memory left) -- empty archive, or fewer
    scored candidates than a quarter of its budget -- is an infrastructure failure, not a search outcome."""
    eps = glob.glob(str(EP / f"{tag}_*" / "evidence.json"))
    if not eps:
        return True
    for A in json.loads(Path(eps[0]).read_text(encoding="utf-8"))["arms"].values():
        if A.get("live", 0) == 0 or A.get("scored", 0) < 0.25 * CMDS[tag][2]:
            return True
    return False


def finish(S, X, K, procs):
    lines = []
    for tag, p in procs:
        code = p.wait()
        if tag in CMDS and (code != 0 or broken(tag)):      # one rerun, by itself (PLAN revision 6)
            log = ROOT / "logs" / f"_idea_{tag}.log"
            log.rename(log.with_suffix(".broken.log"))
            for ep in glob.glob(str(EP / f"{tag}_*" / "evidence.json")):
                Path(ep).rename(Path(ep).with_suffix(".broken.json"))
            cmd, env, _ = CMDS[tag]
            code = subprocess.run(cmd, cwd=ROOT, stdout=log.open("w"), stderr=subprocess.STDOUT, env=env).returncode
            code = code if not broken(tag) else 98
            tag = tag + " (rerun)"
        lines.append(f"{tag} {code}")
        if tag.startswith("c05s") and isinstance(p, subprocess.Popen) or tag.endswith("(rerun)"):
            with (ROOT / "logs" / f"_idea_{tag.split()[0]}.log").open("a") as fh:
                fh.write(f"[partura exit {code}]\n")
    (ARMS / f"s{S}_{X}_r{K}.DONE").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


def contains(expr, core_key, P_):
    try:
        return any(n.key() == core_key for n in P_(expr).nodes())
    except Exception:                                        # noqa: BLE001
        return False


ARMS.mkdir(parents=True, exist_ok=True)
(ROOT / "logs").mkdir(exist_ok=True)

if MODE == "A":
    S, K = int(sys.argv[2]), int(sys.argv[3])
    lf, lib = library(S, "A", K)
    procs = [gp(f"c05s{S}Ar{K}{j}", "I0_open_search", "guidance/C05_base.yaml", "control", 1000 * S + 10 * K + i, 128, ["--ban-library", str(lf)])
             for i, j in ((1, "a"), (2, "b"))]
    finish(S, "A", K, procs)

elif MODE == "b0plan":
    S, K = int(sys.argv[2]), int(sys.argv[3])
    B = yaml.safe_load((ARMS / f"s{S}_B_r{K}.yaml").read_text(encoding="utf-8"))
    loc = json.loads((D / "loc" / f"s{S}_B0_r{K}.json").read_text(encoding="utf-8"))
    used = {}
    for k in range(1, K):
        for s in (yaml.safe_load((ARMS / f"s{S}_B0_r{k}.yaml").read_text(encoding="utf-8")) or {}).get("slots", []):
            if s["type"] == "E":
                used[s["core"]] = used.get(s["core"], 0) + 1
    slots = []
    cards = [c["core"] for c in loc["core_cards"]]
    cards += [h["expr"] for h in loc["heads"] if h["expr"] not in cards]   # PLAN revision 3: then the whole heads, by score
    for s in B["slots"]:
        if s["type"] == "E":
            core = next((c for c in cards if used.get(c, 0) < 2 and c not in [x.get("core") for x in slots]), None)
            if core is not None:
                slots.append({"type": "E", "core": core, "seeds": []})
                used[core] = used.get(core, 0) + 1
                continue
            slots.append({"type": "N", "note": "no core card left: plain GP"})
        else:
            slots.append({"type": "N"})
    n_r = sum(len(r.get("variants", [])) for r in (B.get("R") or []))
    req = {}
    for r in loc["r_candidates"][:min(n_r, 16)]:
        req.setdefault(r["head"], []).append(r["variant"])
    plan = {"seed": S, "round": K, "rule": "PLAN §2.5 (B0 follows B's slot counts)", "slots": slots,
            "R": [{"head": h, "variants": v} for h, v in req.items()]}
    (ARMS / f"s{S}_B0_r{K}.yaml").write_text(yaml.safe_dump(plan, allow_unicode=True, sort_keys=False), encoding="utf-8")
    print(f"B0 plan s{S} r{K}: {[s['type'] for s in slots]}, R {sum(len(v) for v in req.values())}")

elif MODE == "mission":
    S, X, K = int(sys.argv[2]), sys.argv[3], int(sys.argv[4])
    plan = yaml.safe_load((ARMS / f"s{S}_{X}_r{K}.yaml").read_text(encoding="utf-8"))
    sys.path.insert(0, str(ROOT))
    from partura.bridge import ensure_alphacube_on_path
    ensure_alphacube_on_path()
    from alphacube.plugins import load_plugins
    load_plugins(["partura.ac_plugin"])
    from alphacube.parser import parse

    def P_(s):
        return parse(s, strict=True, coerce_daily=True, n_minutes=241, allow_general=True)

    lf, lib = library(S, X, K)
    seen = ARMS / f"seen_s{S}_{X}_r{K}.json"
    seen.write_text(json.dumps([a["expr"] for a in c05_lib.archive(snapshot(S, X, K))]), encoding="utf-8")
    base = yaml.safe_load((ROOT / "guidance" / "C05_base.yaml").read_text(encoding="utf-8"))
    base["batch"] = f"C05_s{S}_{X}_r{K}"
    base["ideas"] = list(base["ideas"])
    jobs = []
    for i, (s, j) in enumerate(zip(plan["slots"], "ab")):
        seed, tag = 1000 * S + 10 * K + i + 1, f"c05s{S}{X}r{K}{j}"
        if s["type"] == "E":
            core = s["core"]
            ck = P_(core).key()
            fam = sorted([h for h in lib if contains(h["expr"], ck, P_)], key=lambda h: -h["score"])[:6]
            ff = ARMS / f"fam_s{S}_{X}_r{K}{j}.json"
            ff.write_text(json.dumps([{"expr": h["expr"], "sign": h["sign"], "hl": h["hl"]} for h in fam]), encoding="utf-8")
            iid = f"E{j}"
            base["ideas"].append({"id": iid, "hypothesis": s.get("hypothesis", "B0: mechanical core"), "seeds": list(s.get("seeds") or [])[:16],
                                  "grammar": {}, "reward": "long_neutral"})
            jobs.append((tag, iid, "steer", seed, ["--parts", "seeds", "--seed-share", "1.0", "--must-contain", core, "--periphery-seen", str(seen),
                                                    "--neutral-extra", str(ff), "--graft-fill", "32", "--ban-library", str(lf)]))
        elif s.get("seeds"):
            iid = f"N{j}"
            base["ideas"].append({"id": iid, "hypothesis": s.get("hypothesis", ""), "seeds": list(s["seeds"])[:16], "grammar": {}, "reward": "long_neutral"})
            jobs.append((tag, iid, "steer", seed, ["--parts", "seeds", "--seed-share", "0.5", "--ban-library", str(lf)]))
        else:
            jobs.append((tag, "I0_open_search", "control", seed, ["--ban-library", str(lf)]))
    gpath = D / "guidance" / f"s{S}_{X}_r{K}.yaml"
    gpath.parent.mkdir(parents=True, exist_ok=True)
    gpath.write_text(yaml.safe_dump(base, allow_unicode=True, sort_keys=False), encoding="utf-8")
    procs = [gp(tag, iid, str(gpath.relative_to(ROOT)), arm, seed, 96, extra) for tag, iid, arm, seed, extra in jobs]
    if plan.get("R") and (ARMS / f"s{S}_{X}_r{K}_R.json").is_file():
        print(f"R s{S} {X} r{K}: already evaluated, not rerun", flush=True)
    elif plan.get("R") and running(f"c05_locate.py direct {S} {X} {K} "):
        print(f"R s{S} {X} r{K}: still running from an earlier runner, adopted", flush=True)
        procs.append((f"R_s{S}_{X}_r{K}", Adopted(f"c05_locate.py direct {S} {X} {K} ")))
    elif plan.get("R"):
        rq = ARMS / f"rreq_s{S}_{X}_r{K}.json"
        rq.write_text(json.dumps(plan["R"], ensure_ascii=False), encoding="utf-8")
        log = ROOT / "logs" / f"_c05R_s{S}_{X}_r{K}.log"
        procs.append((f"R_s{S}_{X}_r{K}", subprocess.Popen([PY, "-u", "scripts/c05_locate.py", "direct", str(S), X, str(K), str(rq)], cwd=ROOT,
                                                            stdout=log.open("w"), stderr=subprocess.STDOUT,
                                                            env={**os.environ, "PARTURA_GPU_WAYS": "2"})))   # the same two ways as the GP runs (PLAN revision 2)
    finish(S, X, K, procs)
else:
    raise SystemExit(f"unknown mode {MODE}")
