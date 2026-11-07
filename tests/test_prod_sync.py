"""PROD W01: the seed -> host mapping (research/prod_W01/hosts.json, scripts/prod_hosts.py) and the laptop-side mover scripts/prod_sync.sh,
run against a fake "ssh" that executes the remote command in a local directory standing in for the server's Partura home."""
import json
import os
import shutil
import stat
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import prod_hosts  # noqa: E402

PY = sys.executable
HAS_YAML = subprocess.run([PY, "-c", "import yaml"], capture_output=True).returncode == 0


# ------------------------------------------------------------------ the real mapping
def test_real_mapping_is_the_plan():
    cfg = prod_hosts.load(ROOT / "research" / "prod_W01" / "hosts.json")
    assert cfg["study"] == "PROD" and cfg["dir"] == "prod_W01"
    assert prod_hosts.seeds(cfg) == list(range(901, 913))
    assert prod_hosts.seeds(cfg, "new") == list(range(901, 909))                  # PLAN section 3: 901-908 on the new server
    assert prod_hosts.seeds(cfg, "old") == [909, 910, 911, 912]
    new, old = cfg["hosts"]["new"], cfg["hosts"]["old"]
    assert new["ssh"].endswith("root@100.111.77.69") and "-p" not in new["ssh"].split()
    assert "-p 29982" in old["ssh"] and old["ssh"].endswith("root@connect.westd.seetacloud.com")
    assert new["home"] == "/var/snap/docker/common/var-lib-docker/c02_partura/Partura"
    assert old["home"] == "/root/autodl-tmp/Partura"
    assert prod_hosts.host_of(cfg, 905) == "new" and prod_hosts.host_of(cfg, 910) == "old"
    with pytest.raises(SystemExit):
        prod_hosts.host_of(cfg, 913)
    with pytest.raises(SystemExit):
        prod_hosts.host_of(cfg, 801)                                                  # the C08 seeds are not PROD's


def test_load_rejects_a_broken_mapping(tmp_path):
    f = tmp_path / "h.json"
    f.write_text(json.dumps({"study": "PROD", "dir": "x", "hosts": {"new": {"ssh": "ssh a", "home": "/h"}}, "seeds": {"901": "old"}}))
    with pytest.raises(SystemExit):
        prod_hosts.load(f)
    f.write_text(json.dumps({"study": "PROD", "dir": "x", "hosts": {"new": {"ssh": "", "home": "/"}}, "seeds": {"901": "new"}}))
    with pytest.raises(SystemExit):
        prod_hosts.load(f)


def test_cli():
    def run(*a, hosts=None):
        env = {**os.environ, **({"PROD_HOSTS": str(hosts)} if hosts else {})}
        return subprocess.run([PY, str(ROOT / "scripts" / "prod_hosts.py"), *a], capture_output=True, text=True, env=env)
    assert run("seeds", "old").stdout.split() == ["909", "910", "911", "912"]
    assert run("host", "901").stdout.strip() == "new"
    assert run("home", "912").stdout.strip() == "/root/autodl-tmp/Partura"
    assert run("dir").stdout.strip() == "prod_W01"
    assert run("host", "999").returncode != 0


# ------------------------------------------------------------------ prod_sync.sh against a fake ssh
@pytest.fixture
def world(tmp_path):
    """A copy of scripts/ in tmp_path/repo (so the laptop-side files land there, not in this work tree), two fake server homes, a hosts.json."""
    repo = tmp_path / "repo"
    (repo / "scripts").mkdir(parents=True)
    for f in ("prod_sync.sh", "prod_hosts.py"):
        shutil.copy(ROOT / "scripts" / f, repo / "scripts" / f)
    fake = tmp_path / "fakessh"
    fake.write_text('#!/bin/bash\nexec bash -c "$*"\n')                          # ssh concatenates its arguments for the remote shell
    fake.chmod(fake.stat().st_mode | stat.S_IEXEC)
    homes = {"new": tmp_path / "newhome", "old": tmp_path / "oldhome"}
    for h in homes.values():
        (h / "research" / "prod_W01" / "loc").mkdir(parents=True)
        (h / "research" / "prod_W01" / "arms").mkdir(parents=True)
        (h / "logs").mkdir()
        (h / "tmp").mkdir()
    hosts = {"study": "PROD", "dir": "prod_W01", "hosts": {k: {"ssh": str(fake), "home": str(v)} for k, v in homes.items()},
             "seeds": {"901": "new", "909": "old"}}
    (tmp_path / "hosts.json").write_text(json.dumps(hosts))
    # the stand-in for `$PY scripts/c05_locate.py corr <seed> P <k> <request.json>`: writes <request>_corr.json / .md
    stub = tmp_path / "pystub"
    stub.write_text('#!/bin/bash\nreq="${@: -1}"; b="${req%.json}"; sleep 0.3\n'
                    'echo \'{"heads": 2, "rows": []}\' > ${b}_corr.json; echo "| slot a seed 1 | row |" > ${b}_corr.md\n'
                    'echo "$@" >> "$(dirname "$0")/stub_calls.txt"\n')
    stub.chmod(stub.stat().st_mode | stat.S_IEXEC)
    for h in homes.values():
        (h / "tmp" / "prod_env.sh").write_text(f'export PY={stub}\n')
    env = {**os.environ, "PROD_HOSTS": str(tmp_path / "hosts.json"), "PROD_SYNC_SLEEP": "0", "PROD_CORR_POLL_S": "0.2", "PROD_CORR_POLLS": "40", "PYL": PY}
    env.pop("FORCE", None)

    def sync(*a, **kw):
        return subprocess.run(["bash", str(repo / "scripts" / "prod_sync.sh"), *a], capture_output=True, text=True, env={**env, **kw.get("env", {})}, timeout=120)
    return {"repo": repo, "homes": homes, "sync": sync, "tmp": tmp_path, "L": repo / "research" / "prod_W01"}


def _locate_ready(home, seed, k, body="LOC"):
    d = home / "research" / "prod_W01" / "loc"
    (d / f"s{seed}_P_r{k}.json").write_text(json.dumps({"heads": body}))
    (d / f"s{seed}_P_r{k}.md").write_text(f"# loc {body}\n")
    (d / f"s{seed}_P_r{k}.READY").write_text("")


def test_ready_and_fetch(world):
    s, h, L = world["sync"], world["homes"], world["L"]
    r = s("ready", "1", "901 909")
    assert "901 waiting" in r.stdout and "909 waiting" in r.stdout and r.returncode == 1
    _locate_ready(h["new"], 901, 1)
    r = s("ready", "1", "901 909")
    assert "901 ready" in r.stdout and "909 waiting" in r.stdout
    # a locate that has not finished (no READY) is not fetched
    (h["old"] / "research/prod_W01/loc/s909_P_r1.json").write_text("{}")
    r = s("fetch", "1", "909")
    assert "NOT READY" in r.stdout and r.returncode == 1 and not (L / "partura/s909/r1/loc.json").exists()
    r = s("fetch", "1", "901")
    assert r.returncode == 0 and "bytes of locate output" in r.stdout
    assert json.loads((L / "partura/s901/r1/loc.json").read_text()) == {"heads": "LOC"}
    assert (L / "partura/s901/r1/loc.md").read_text() == "# loc LOC\n"
    assert not (L / "partura/s901/r1/R_prev.json").exists()


def test_fetch_round_two_takes_the_previous_R_file_if_there_is_one(world):
    s, h, L = world["sync"], world["homes"], world["L"]
    _locate_ready(h["new"], 901, 2)
    r = s("fetch", "2", "901")
    assert r.returncode == 0 and not (L / "partura/s901/r2/R_prev.json").exists()                 # absent is not an error
    (h["new"] / "research/prod_W01/arms/s901_P_r1_R.json").write_text('{"replacements": []}')
    r = s("fetch", "2", "901")
    assert r.returncode == 0 and json.loads((L / "partura/s901/r2/R_prev.json").read_text()) == {"replacements": []}


def test_hosts_are_taken_from_the_mapping(world):
    s, h, L = world["sync"], world["homes"], world["L"]
    _locate_ready(h["old"], 909, 1, "OLD")
    r = s("fetch", "1", "909")
    assert r.returncode == 0 and json.loads((L / "partura/s909/r1/loc.json").read_text()) == {"heads": "OLD"}
    r = s("fetch", "1", "905")                                                                      # not in the mapping: never guessed
    assert r.returncode == 1 and "not in the host mapping" in r.stdout


def test_push_is_atomic_checked_and_does_not_overwrite_a_different_plan(world):
    s, h, L = world["sync"], world["homes"], world["L"]
    p = L / "partura/s901/r1"
    p.mkdir(parents=True)
    arms = h["new"] / "research/prod_W01/arms"
    r = s("push", "1", "901")
    assert r.returncode == 1 and "no missions_final.yaml" in r.stdout
    (p / "missions_final.yaml").write_text("seed: 901\nround: 1\nslots: []\n")
    r = s("push", "1", "901")
    assert r.returncode == 0 and "901 pushed" in r.stdout
    assert (arms / "s901_P_r1.yaml").read_text() == "seed: 901\nround: 1\nslots: []\n"
    assert not list(arms.glob(".s901*part"))
    r = s("push", "1", "901")                                                                       # the same plan again: nothing to do
    assert r.returncode == 0 and "already on the server" in r.stdout
    (p / "missions_final.yaml").write_text("seed: 901\nround: 1\nslots: [x]\n")
    r = s("push", "1", "901")
    assert r.returncode == 1 and "REFUSING" in r.stdout
    assert (arms / "s901_P_r1.yaml").read_text() == "seed: 901\nround: 1\nslots: []\n"
    r = s("push", "1", "901", env={"FORCE": "1"})
    assert r.returncode == 0 and (arms / "s901_P_r1.yaml").read_text().endswith("[x]\n")


@pytest.mark.skipif(not HAS_YAML, reason="PyYAML missing")
def test_corr_sends_the_request_runs_the_job_and_fetches_the_table(world):
    s, h, L = world["sync"], world["homes"], world["L"]
    p = L / "partura/s901/r1"
    p.mkdir(parents=True)
    (p / "missions.yaml").write_text("seed: 901\nround: 1\nslots:\n- type: E\n  core: cA\n  seeds: [e1, e2]\n- type: N\n  seeds: [e3]\nR:\n- head: hh\n  variants: [v1]\n")
    r = s("corr", "1", "901", "1")
    assert r.returncode == 0, r.stdout + r.stderr
    assert "corr_1.md written" in r.stdout
    req = json.loads((p / "corr_1.request.json").read_text())
    assert [q["expr"] for q in req] == ["cA", "e1", "e2", "e3", "v1"]
    assert (p / "corr_1.json").read_text().strip() == '{"heads": 2, "rows": []}' and (p / "corr_1.md").exists()
    jobs = sorted((h["new"] / "research/prod_W01/audit").glob("*_corr.json"))
    assert len(jobs) == 1 and jobs[0].name.startswith("s901_r1_q1_")
    # same request again: the finished job is fetched, not run a second time
    n_calls = (world["tmp"] / "stub_calls.txt").read_text().count("\n")
    r = s("corr", "1", "901", "1")
    assert r.returncode == 0 and "started the correlation job" not in r.stdout
    assert (world["tmp"] / "stub_calls.txt").read_text().count("\n") == n_calls
    # a rewritten plan is a NEW job (its name carries the request's md5): the old table is never reused for it
    (p / "missions.yaml").write_text("seed: 901\nround: 1\nslots:\n- type: N\n  seeds: [e9]\n")
    r = s("corr", "1", "901", "1")
    assert r.returncode == 0 and "started the correlation job" in r.stdout
    assert len(sorted((h["new"] / "research/prod_W01/audit").glob("*_corr.json"))) == 2
    assert (world["tmp"] / "stub_calls.txt").read_text().count("\n") == n_calls + 1


def test_status_one_line_per_seed(world):
    s, h = world["sync"], world["homes"]
    _locate_ready(h["new"], 901, 1)
    ep = h["new"] / "episodes" / "prods901M1_I0_open_search"
    ep.mkdir(parents=True)
    (ep / "evidence.json").write_text('{"complete": true}')
    (h["new"] / "research/prod_W01/arms/s901_P_r1.yaml").write_text("x")
    r = s("status")
    assert r.returncode == 0, r.stderr
    assert "== new" in r.stdout and "== old" in r.stdout
    line901 = next(l for l in r.stdout.splitlines() if l.startswith("s901"))
    assert "[1]" in line901 and "r1:ready+plan" in line901 and "ALLDONE" not in line901
    assert "[-]" in next(l for l in r.stdout.splitlines() if l.startswith("s909"))
