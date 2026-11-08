"""PROD W01: the server-side scripts (scripts/server/prod_*.sh), run on this machine with a fake python ($PY) that stands in for the engine:
a Partura home in a temp directory, M batches that take a moment, locate / mission steps that only check their preconditions and write the
files the real ones write.  Checks the ordering the plan asks for (round k needs M batch k AND the pushed plan), restart safety, the M-chain
restart limit, ALLDONE.  The keeper (bash 4 associative array) and the health check are only syntax-checked here."""
import os
import shutil
import stat
import subprocess
import time
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SERVER = ROOT / "scripts" / "server"

FAKE_PY = r'''#!/bin/bash
H="$PARTURA_HOME"; D="$H/research/$PARTURA_STUDY_DIR"; LOGF="$H/calls.log"
case "$*" in
  *c05_lib.py*heads*) echo '[]' > "$3"; exit 0 ;;
  *idea_search.py*)
    tag=""; prev=""; for x in "$@"; do [ "$prev" = "--tag" ] && tag="$x"; prev="$x"; done
    [ -e "$H/failonce_$tag" ] && { rm -f "$H/failonce_$tag"; echo "FAIL $tag" >> "$LOGF"; exit 1; }
    [ -e "$H/failalways_$tag" ] && { echo "FAIL $tag" >> "$LOGF"; exit 1; }
    case "$tag" in *M2) sleep 1.2 ;; *M4) sleep 1.6 ;; *) sleep 0.2 ;; esac
    mkdir -p "$H/episodes/${tag}_I0_open_search"
    echo '{"complete": true, "arms": {"control": {"heads": [], "scored": 1, "seconds": 1}}}' > "$H/episodes/${tag}_I0_open_search/evidence.json"
    echo "Mdone $tag" >> "$LOGF"; exit 0 ;;
  *c05_locate.py*locate*)
    S=$4; K=$6
    [ -e "$H/episodes/prods${S}M${K}_I0_open_search/evidence.json" ] || echo "VIOLATION locate $S $K before M batch $K" >> "$LOGF"
    mkdir -p "$D/loc"; echo '{}' > "$D/loc/s${S}_P_r$K.json"; echo '# loc' > "$D/loc/s${S}_P_r$K.md"
    echo "locate $S $K" >> "$LOGF"; exit 0 ;;
  *c05_round.py*mission*)
    S=$3; K=$5
    [ -e "$D/arms/s${S}_P_r$K.yaml" ] || echo "VIOLATION mission $S $K without a plan" >> "$LOGF"
    [ -e "$H/episodes/prods${S}M${K}_I0_open_search/evidence.json" ] || echo "VIOLATION mission $S $K before M batch $K" >> "$LOGF"
    echo "mission $S $K" >> "$LOGF"; sleep 0.1; echo "$S $K 0" > "$D/arms/s${S}_P_r$K.DONE"; exit 0 ;;
esac
echo "UNEXPECTED $*" >> "$LOGF"; exit 9
'''
FAKE_TIMEOUT = '#!/bin/bash\nwhile [[ "$1" == --* ]]; do shift; done\nshift\nexec "$@"\n'      # timeout --signal=TERM --kill-after=60 720m cmd...


def _exe(path, text):
    path.write_text(text)
    path.chmod(path.stat().st_mode | stat.S_IEXEC)


@pytest.fixture
def home(tmp_path):
    h = tmp_path / "home"
    (h / "research" / "prod_test").mkdir(parents=True)
    os.symlink(ROOT / "scripts", h / "scripts")
    bindir = tmp_path / "bin"
    bindir.mkdir()
    _exe(bindir / "timeout", FAKE_TIMEOUT)
    _exe(bindir / "fakepy", FAKE_PY)
    (h / "calls.log").write_text("")
    env = {**os.environ, "PATH": f"{bindir}:{os.environ['PATH']}", "PARTURA_HOME": str(h), "PY": str(bindir / "fakepy"), "PARTURA_C0X": "PROD",
           "PARTURA_STUDY_DIR": "prod_test", "PARTURA_RANK_FIRST": "1", "PARTURA_NEUTRAL_POWERS": "1,2,3", "PROD_POLL_S": "0.1", "PROD_POLL_M_S": "0.1"}
    procs = []
    yield h, env, procs
    for p in procs:
        if p.poll() is None:
            p.kill()
    subprocess.run(["pkill", "-f", "prod_m.sh 95"], capture_output=True)


def conductor(h, env, procs, seed):
    p = subprocess.Popen(["bash", "scripts/server/prod_conductor.sh", str(seed)], cwd=h, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    procs.append(p)
    return p


def calls(h):
    return [l for l in (h / "calls.log").read_text().splitlines() if l]


def wait(cond, timeout=30.0):
    t = time.time()
    while time.time() - t < timeout:
        if cond():
            return True
        time.sleep(0.05)
    return False


def push_plan(h, seed, k):
    d = h / "research" / "prod_test" / "arms"
    d.mkdir(exist_ok=True)
    (d / f".s{seed}_P_r{k}.yaml.part").write_text("slots: []\n")
    os.rename(d / f".s{seed}_P_r{k}.yaml.part", d / f"s{seed}_P_r{k}.yaml")


def test_scripts_parse():
    for f in sorted(SERVER.glob("prod_*.sh")) + [ROOT / "scripts" / "prod_sync.sh", ROOT / "scripts" / "prod_gather.sh"]:
        assert subprocess.run(["bash", "-n", str(f)], capture_output=True).returncode == 0, f


def test_environment_is_checked(home):
    h, env, procs = home
    bad = {k: v for k, v in env.items() if k != "PARTURA_RANK_FIRST"}
    for script in ("prod_conductor.sh", "prod_m.sh"):
        r = subprocess.run(["bash", f"scripts/server/{script}", "951"], cwd=h, env=bad, capture_output=True, text=True)
        assert r.returncode == 2 and "prod_env.sh" in r.stdout
    r = subprocess.run(["bash", "scripts/server/prod_conductor.sh", "951"], cwd=h, env={**env, "PARTURA_C0X": "C08"}, capture_output=True, text=True)
    assert r.returncode == 2


def test_round_k_needs_m_batch_k_and_the_plan_then_alldone(home):
    h, env, procs = home
    D = h / "research" / "prod_test"
    for k in (1, 2, 3):                                         # the plans are on the server before M is far: they must still wait for their batch
        push_plan(h, 951, k)
    p = conductor(h, env, procs, 951)
    assert wait(lambda: (D / "arms" / "s951.ALLDONE").exists()), (calls(h), (D / "conductor_s951.log").read_text() if (D / "conductor_s951.log").exists() else "")
    assert p.wait(timeout=10) == 0
    c = calls(h)
    assert not [x for x in c if x.startswith(("VIOLATION", "UNEXPECTED", "FAIL"))], c
    assert [x for x in c if x.split()[0] in ("locate", "mission")] == ["locate 951 1", "mission 951 1", "locate 951 2", "mission 951 2", "locate 951 3", "mission 951 3"]
    assert c.index("Mdone prods951M2") < c.index("locate 951 2")           # round 2 started only after M batch 2
    assert [x for x in c if x.startswith("Mdone")] == [f"Mdone prods951M{e}" for e in (1, 2, 3, 4)]
    assert (D / "m" / "s951.DONE").exists() and (D / "loc" / "s951_P_r3.READY").exists()
    assert (D / "m" / "s951.starts").read_text().strip() == "1"
    log = (D / "conductor_s951.log").read_text()
    assert "M chain started (start 1)" in log and "round 3: missions ended" in log and log.strip().splitlines()[-1].startswith("[prod s951] all done")
    # the M library for batch e is built from the seed's own earlier batches only (prod_m.sh passes episodes/prods951M<p>_...)
    assert (D / "m" / "lib_s951_b4.json").exists() and not (D / "m" / "lib_s951_b1.json").exists()


def test_mission_waits_for_the_plan_and_locate_does_not_wait_for_it(home):
    h, env, procs = home
    D = h / "research" / "prod_test"
    p = conductor(h, env, procs, 952)
    assert wait(lambda: (D / "loc" / "s952_P_r1.READY").exists())
    time.sleep(0.6)
    assert not any(x.startswith("mission") for x in calls(h)) and p.poll() is None            # located, waiting for Partura's plan
    push_plan(h, 952, 1)
    assert wait(lambda: (D / "arms" / "s952_P_r1.DONE").exists())
    assert wait(lambda: (D / "loc" / "s952_P_r2.READY").exists(), 30)                           # round 2: after M batch 2, still no plan
    time.sleep(0.6)
    assert "mission 952 2" not in calls(h)
    for k in (2, 3):
        push_plan(h, 952, k)
        assert wait(lambda k=k: (D / "arms" / f"s952_P_r{k}.DONE").exists(), 30)
    assert wait(lambda: (D / "arms" / "s952.ALLDONE").exists(), 30)
    assert not [x for x in calls(h) if x.startswith(("VIOLATION", "UNEXPECTED"))]


def test_a_dead_m_chain_is_restarted_and_a_restart_does_not_redo_finished_work(home):
    h, env, procs = home
    D = h / "research" / "prod_test"
    (h / "failonce_prods953M2").write_text("")                  # batch 2 dies once (a disk-guard kill, say)
    for k in (1, 2, 3):
        push_plan(h, 953, k)
    p = conductor(h, env, procs, 953)
    assert wait(lambda: (D / "arms" / "s953.ALLDONE").exists(), 40), calls(h)
    c = calls(h)
    assert "FAIL prods953M2" in c and [x for x in c if x.startswith("Mdone")] == [f"Mdone prods953M{e}" for e in (1, 2, 3, 4)]
    assert (D / "m" / "s953.starts").read_text().strip() == "2"
    assert "M chain started (start 2)" in (D / "conductor_s953.log").read_text()
    # a second conductor on a finished seed redoes nothing
    n = len(c)
    q = conductor(h, env, procs, 953)
    assert q.wait(timeout=20) == 0
    assert len(calls(h)) == n and "round 1: done earlier" in (D / "conductor_s953.log").read_text()


def test_the_conductor_gives_up_when_the_m_chain_keeps_dying(home):
    h, env, procs = home
    D = h / "research" / "prod_test"
    (h / "failalways_prods954M1").write_text("")
    p = conductor(h, env, procs, 954)
    assert p.wait(timeout=30) == 7
    assert "giving up" in (D / "conductor_s954.log").read_text() and (D / "m" / "s954.starts").read_text().strip() == "6"
    assert not (D / "arms" / "s954.ALLDONE").exists()


def test_m_chain_only_bans_the_seeds_own_earlier_batches(home):
    h, env, procs = home
    r = subprocess.run(["bash", "scripts/server/prod_m.sh", "955"], cwd=h, env=env, capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    assert (h / "research/prod_test/m/s955.DONE").exists()
    assert [x for x in calls(h) if x.startswith("Mdone")] == [f"Mdone prods955M{e}" for e in (1, 2, 3, 4)]
    # rerun: finished batches are skipped
    n = len(calls(h))
    assert subprocess.run(["bash", "scripts/server/prod_m.sh", "955"], cwd=h, env=env, capture_output=True).returncode == 0
    assert len(calls(h)) == n


def test_prod_env_template_sets_the_study_on_top_of_the_hosts_own_env(tmp_path):
    home = tmp_path / "Partura"
    (home / "tmp").mkdir(parents=True)
    (home / "tmp" / "c05_env.sh").write_text(f"export PARTURA_HOME={home} PY=/x/python PARTURA_STUDY_DIR=coldstart_C05\n")
    shutil.copy(SERVER / "prod_env.sh", home / "tmp" / "prod_env.sh")
    out = subprocess.run(["bash", "-c", f"cd {home} && source tmp/prod_env.sh && env"], capture_output=True, text=True, env={"PATH": os.environ["PATH"]})
    assert out.returncode == 0, out.stderr
    e = dict(l.split("=", 1) for l in out.stdout.splitlines() if "=" in l)
    assert (e["PARTURA_C0X"], e["PARTURA_STUDY_DIR"], e["PARTURA_RANK_FIRST"], e["PARTURA_NEUTRAL_POWERS"]) == ("PROD", "prod_W01", "1", "1,2,3")
    assert e["C06_CTRL_STRIKE"] == "0.8" and e["PARTURA_R_ADDITIONS"] == "0" and e["PY"] == "/x/python"     # the host's own settings survive
    assert e["TMPDIR"] == str(home / "tmp" / "sys_tmp") and (home / "tmp" / "sys_tmp").is_dir()
    # sourced from another directory it still finds the host's c05_env.sh next to it (the template is meant to live in <home>/tmp/)
    out = subprocess.run(["bash", "-c", f"cd / && source {home}/tmp/prod_env.sh && echo $PARTURA_C0X"], capture_output=True, text=True, env={"PATH": os.environ["PATH"]})
    assert out.stdout.strip() == "PROD"
    assert "PARTURA_HOST_SLOTS" not in e                     # no tmp/host_caps.sh: the W01 scheduling numbers


def test_prod_env_picks_up_the_hosts_own_scheduling_caps(tmp_path):
    home = tmp_path / "Partura"
    (home / "tmp").mkdir(parents=True)
    (home / "tmp" / "c05_env.sh").write_text(f"export PARTURA_HOME={home} PY=/x/python\n")
    (home / "tmp" / "host_caps.sh").write_text("export PARTURA_HOST_SLOTS=8 PARTURA_HOST_PANEL_CACHE_GB=32\n")
    shutil.copy(SERVER / "prod_env.sh", home / "tmp" / "prod_env.sh")
    out = subprocess.run(["bash", "-c", f"cd / && source {home}/tmp/prod_env.sh && env"], capture_output=True, text=True, env={"PATH": os.environ["PATH"]})
    assert out.returncode == 0, out.stderr
    e = dict(l.split("=", 1) for l in out.stdout.splitlines() if "=" in l)
    assert (e["PARTURA_HOST_SLOTS"], e["PARTURA_HOST_PANEL_CACHE_GB"], e["PARTURA_C0X"]) == ("8", "32", "PROD")


def test_a_given_up_m_chain_still_lets_the_rounds_with_a_batch_go_on(home):
    h, env, procs = home
    D = h / "research" / "prod_test"
    (h / "failalways_prods956M3").write_text("")                # batches 1 and 2 are fine, batch 3 never comes
    for k in (1, 2, 3):
        push_plan(h, 956, k)
    env = {**env, "PROD_M_STARTS": "3"}
    p = conductor(h, env, procs, 956)
    assert p.wait(timeout=40) == 7
    log = (D / "conductor_s956.log").read_text()
    assert (D / "arms" / "s956_P_r1.DONE").exists() and (D / "arms" / "s956_P_r2.DONE").exists() and not (D / "arms" / "s956_P_r3.DONE").exists()
    assert log.count("giving up") == 1 and not (D / "arms" / "s956.ALLDONE").exists()
