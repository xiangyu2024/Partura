"""PROD W01: scripts/prod_final.py end to end on synthetic data -- a copy of the code in a temp "Partura home", evidence files written by the
test, and the data layer (PanelSet, the cube store) replaced by a fake that makes panels out of the expression text.  Checks what the real run
must do: libraries (replacement chain, accessions, dedup within and across seeds), fused books, dry run = in-sample only and nothing ledgered /
saved, real run = description-only periods ledgered, the wave panel saved, a second real read refused."""
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np
import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
ALPHACUBE = Path(os.environ.get("ALPHACUBE_ROOT", Path.home() / "Desktop" / "AlphaCube-steering"))
pytestmark = pytest.mark.skipif(not (ALPHACUBE / "src" / "alphacube").is_dir(), reason="AlphaCube checkout not available")

WRAPPER = r'''
import hashlib, runpy, sys
root = sys.argv[1]
sys.path.insert(0, root)
import numpy as np
from partura import books  # puts AlphaCube on sys.path
import alphacube.store
import partura.panels as P
import partura.guard as G


class FakeStore:
    dates = ["20260916"]


class FakePanelSet:
    def __init__(self, store, start, end, **kw):
        d = np.arange(np.datetime64("2018-01-02"), np.datetime64("2026-09-17"), 4)
        self.dates = [str(x).replace("-", "") for x in d]
        self.symbols = [f"S{i:03d}" for i in range(50)]
        self.shape = (len(self.dates), 50)

    def target(self, h=1):
        rng = np.random.default_rng(7)
        t = rng.normal(0, 0.02, self.shape)
        t[rng.random(self.shape) < 0.05] = np.nan
        return t

    def compute(self, exprs):
        out = {}
        for k, e in exprs.items():
            rng = np.random.default_rng(int(hashlib.md5(e.split("~dup")[0].encode()).hexdigest()[:8], 16))
            a = rng.normal(size=self.shape)
            if "~dup" in e:
                a = a + 0.01 * np.random.default_rng(1).normal(size=a.shape)
            out[k] = a
        return out


class FakeGuard:
    def __init__(self, *a, **k): pass
    def start(self): return self
    def stop(self): pass


P.PanelSet = FakePanelSet
alphacube.store.open_cube_store = lambda *a, **k: FakeStore()
G.MemoryGuard = FakeGuard
sys.argv = ["prod_final.py"] + sys.argv[2:]
runpy.run_path(root + "/scripts/prod_final.py", run_name="__main__")
'''


def head(expr, score=0.8, sign=1.0, hl=5.0):
    return {"expr": expr, "sign": sign, "hl": hl, "score": score, "train": score + 0.1, "valid": score}


def episode(root, name, heads, scored=100):
    d = root / "episodes" / name
    d.mkdir(parents=True)
    (d / "evidence.json").write_text(json.dumps({"complete": True, "arms": {"control": {"heads": heads, "scored": scored, "seconds": 10.0, "passers": len(heads)}}}))


@pytest.fixture
def home(tmp_path):
    root = tmp_path / "home"
    (root / "scripts").mkdir(parents=True)
    shutil.copytree(ROOT / "partura", root / "partura", ignore=shutil.ignore_patterns("__pycache__"))
    for f in ("c05_lib.py", "prod_lib.py", "prod_hosts.py", "prod_final.py"):
        shutil.copy(ROOT / "scripts" / f, root / "scripts" / f)
    (root / "guidance").mkdir()
    shutil.copy(ROOT / "guidance" / "C05_base.yaml", root / "guidance" / "C05_base.yaml")
    D = root / "research" / "prod_W01"
    (D / "arms").mkdir(parents=True)
    (D / "loc").mkdir()
    (D / "hosts.json").write_text(json.dumps({"study": "PROD", "dir": "prod_W01", "hosts": {"new": {"ssh": "ssh x", "home": "/h"}}, "seeds": {"901": "new", "902": "new"}}))
    (root / "tmp").mkdir()
    # seed 901: M heads a1 and its twin a1~dup, b1, m4 (replaced twice: r1 m4 -> v1, r2 v1 -> v2); Partura: e1, twins of a1 (dropped), e2, accession acc1
    for S, m in ((901, {1: ["a1", "a1~dup"], 2: ["b1"], 3: [], 4: ["m4"]}), (902, {1: ["a1~dup4", "c1"], 2: [], 3: ["c2"], 4: []})):
        for e, hs in m.items():
            episode(root, f"prods{S}M{e}_I0_open_search", [head(h, 0.6 + 0.01 * i) for i, h in enumerate(hs)], scored=192)
        for k in (1, 2, 3):
            (D / "arms" / f"s{S}_P_r{k}.yaml").write_text(yaml.safe_dump({"slots": [{"type": "E", "core": "c"}, {"type": "N", "seeds": ["x"]}]}))
            (D / "loc" / f"s{S}_P_r{k}.json").write_text(json.dumps({"paid": 10}))
        (D / "arms" / f"s{S}.ALLDONE").write_text("")
    episode(root, "prods901Pr1a_I0_open_search", [head("e1", 0.9)], 96)
    episode(root, "prods901Pr1b_I0_open_search", [head("a1~dup2", 0.7)], 96)
    episode(root, "prods901Pr2a_I0_open_search", [head("a1~dup3", 0.7), head("e2", 0.75)], 96)
    episode(root, "prods902Pr1a_I0_open_search", [head("f1", 0.85)], 96)
    (D / "arms" / "s901_P_r1_R.json").write_text(json.dumps({"paid": 8, "replacements": [{"head": "m4", **head("v1", 0.9)}], "additions": [head("acc1", 0.8)]}))
    (D / "arms" / "s901_P_r2_R.json").write_text(json.dumps({"paid": 8, "replacements": [{"head": "v1", **head("v2", 1.0)}], "additions": []}))
    return root


def run(root, *args, expect=0):
    env = {**os.environ, "ALPHACUBE_ROOT": str(ALPHACUBE), "PARTURA_C0X": "PROD", "PARTURA_STUDY_DIR": "prod_W01", "PARTURA_RANK_FIRST": "1",
           "PARTURA_NEUTRAL_POWERS": "1,2,3", "PARTURA_STORE": "/nonexistent", "PARTURA_SELF_LIMIT_GB": "60"}
    (root / "wrap.py").write_text(WRAPPER)
    r = subprocess.run([sys.executable, str(root / "wrap.py"), str(root), *args], cwd=root, env=env, capture_output=True, text=True, timeout=600)
    if expect == 0:
        assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-3000:]
    else:
        assert r.returncode != 0
    return r


def libs(root, name="library"):
    return json.loads((root / "research" / "prod_W01" / f"{name}.json").read_text())


def test_dry_run_is_in_sample_only(home):
    r = run(home, "--dry-run")
    D = home / "research" / "prod_W01"
    fin, lib = json.loads((D / "final_dry.json").read_text()), libs(home, "library_dry")
    assert fin["dry_run"] is True and (D / "final_dry.md").exists()
    assert not (D / "final.json").exists() and not (D / "library.json").exists() and not (D / "ledger_prod.json").exists()
    assert not (home / "runs").exists(), "a dry run saves no panel"
    for S in ("901", "902"):
        for X in ("M", "P"):
            assert set(fin["per_seed"][S][X]) == {"heads", "train", "valid"}, "no out-of-sample key in a dry run"
    assert "years_test" not in fin and "extra_heads" not in fin
    # libraries: seed 901 M = a1, b1, m4 (a1~dup is a1's twin); P = M with m4 -> v2 (chain), + e1, acc1, e2; the other twins of a1 are out
    p901 = [h["expr"] for h in lib["per_seed"]["901"]["P"]]
    assert [h["expr"] for h in lib["per_seed"]["901"]["M"]] == ["a1", "b1", "m4"]
    assert p901 == ["a1", "b1", "v2", "e1", "acc1", "e2"]
    roles = {h["expr"]: h["role"] for h in lib["per_seed"]["901"]["P"]}
    assert roles["v2"] == "M+R" and roles["acc1"] == "R+" and roles["e1"] == "E" and roles["e2"] == "E"
    assert [h["expr"] for h in lib["per_seed"]["902"]["P"]] == ["a1~dup4", "c1", "c2", "f1"]
    # the whole wave: seed 902's a1~dup4 is a twin of seed 901's a1 -> only one of them stays (the higher score; ties by seed)
    wave = [(h["seed"], h["expr"]) for h in lib["wave"]["P"]]
    assert sum(1 for _, e in wave if e.split("~")[0] == "a1") == 1
    assert len(lib["wave"]["P"]) == len(lib["per_seed"]["901"]["P"]) + len(lib["per_seed"]["902"]["P"]) - 1
    for h in lib["wave"]["P"]:
        assert "test_sharpe" not in h and h["rho_known"] is not None
    assert fin["libraries"]["wave"]["P"] == len(lib["wave"]["P"])
    assert fin["evaluations"]["P"] > 0 and fin["r_additions"] is True


def test_real_run_describes_test_and_forward_ledgers_them_and_saves_the_panel(home):
    D = home / "research" / "prod_W01"
    run(home)
    fin = json.loads((D / "final.json").read_text())
    assert fin["dry_run"] is False and (D / "final.md").exists() and (D / "library.json").exists()
    for S in ("901", "902"):
        for X in ("M", "P"):
            assert {"train", "valid", "test", "forward"} <= set(fin["per_seed"][S][X])
    assert {"test", "forward"} <= set(fin["wave"]["P"]) and fin["selection"].startswith("train + valid only")
    led = json.loads((D / "ledger_prod.json").read_text())
    assert led["summary"]["holdout"]["reads"] == 1 and led["summary"]["forward"]["reads"] == 1
    assert all("description only" in e["purpose"] for e in led["entries"])
    sp = fin["wave_signal_panel"]
    npy = home / sp["relative"]
    assert npy.is_file() and sp["relative"] == "runs/prod_W01/wave_fused.npy"
    a = np.load(npy)
    meta = json.loads(npy.with_suffix(".meta.json").read_text())
    assert list(a.shape) == sp["shape"] == meta["shape"] and a.dtype == np.float32 and len(meta["dates"]) == a.shape[0] and len(meta["symbols"]) == a.shape[1]
    assert np.isfinite(a).mean() > 0.5
    assert len(meta["heads"]) == fin["libraries"]["wave"]["P"]
    ex = fin["extra_heads"]
    assert {e["expr"] for e in ex} >= {"e1", "acc1", "v2", "e2", "f1"} and all("test_sharpe" in e for e in ex)
    # library.json is in-sample only even in a real run
    assert "test_sharpe" not in json.dumps(libs(home))
    # the same expressions give the same in-sample books in the dry run and the real run
    run(home, "--dry-run")
    dry = json.loads((D / "final_dry.json").read_text())
    assert dry["per_seed"]["901"]["P"]["train"] == fin["per_seed"]["901"]["P"]["train"] and dry["wave"]["P"]["valid"] == fin["wave"]["P"]["valid"]


def test_second_real_read_is_refused_unless_again(home):
    D = home / "research" / "prod_W01"
    run(home)
    r = run(home, expect=1)
    assert "already" in (r.stdout + r.stderr)
    run(home, "--again")
    assert json.loads((D / "ledger_prod.json").read_text())["summary"]["holdout"]["reads"] == 2


def test_real_run_needs_every_seed_finished_and_the_whole_wave(home):
    D = home / "research" / "prod_W01"
    (D / "arms" / "s902.ALLDONE").unlink()
    r = run(home, expect=1)
    assert "ALLDONE" in (r.stdout + r.stderr) and not (D / "ledger_prod.json").exists()
    r = run(home, "--seeds", "901", expect=1)
    assert "--dry-run" in (r.stdout + r.stderr)
    run(home, "--dry-run", "--seeds", "901")                                  # a partial wave is fine as a dry run
    assert list(json.loads((D / "final_dry.json").read_text())["per_seed"]) == ["901"]


def test_the_ruler_must_be_the_new_one(home):
    env_bad = {**os.environ, "ALPHACUBE_ROOT": str(ALPHACUBE), "PARTURA_C0X": "PROD", "PARTURA_STUDY_DIR": "prod_W01", "PARTURA_RANK_FIRST": "0", "PARTURA_NEUTRAL_POWERS": "1"}
    (home / "wrap.py").write_text(WRAPPER)
    r = subprocess.run([sys.executable, str(home / "wrap.py"), str(home), "--dry-run"], cwd=home, env=env_bad, capture_output=True, text=True)
    assert r.returncode != 0 and "new ruler" in (r.stdout + r.stderr)
