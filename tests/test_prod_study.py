"""PROD W01: study resolution (partura/study.py) -- the legacy studies resolve exactly as the scripts used to spell it out inline,
PROD resolves to C08's behaviour at every switch except the documented ones, and the scripts really go through the module."""
import json
import os
import re
import shutil
import subprocess
import sys
import uuid
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from partura import study  # noqa: E402

LEGACY = ["C05", "C06", "C07", "C08"]


# ---- what the scripts spelled out inline before partura/study.py existed (copied from the old source, not from the module)
def old_dir(s):
    return f"coldstart_{s}"


def old_mpfx(s):
    return "c07" if s in ("C07", "C08") else "c05"


@pytest.mark.parametrize("s", LEGACY)
def test_legacy_studies_resolve_as_before(s):
    junk = {"PARTURA_STUDY_DIR": "something_else", "PARTURA_R_ADDITIONS": "0", "PARTURA_C0X": s}
    assert study.name("C05", junk) == s
    assert study.dirname(s, junk) == old_dir(s)                       # PARTURA_STUDY_DIR is not read for a legacy study
    assert study.prefix(s) == s.lower()
    assert study.m_prefix(s) == old_mpfx(s)
    assert study.neutral_extra(s) == (s == "C05")
    assert study.r_additions(s, junk) == (s == "C06")                 # the old gate: `if STUDY == "C06"` (so NOT C08)
    assert study.ctrl_strike_default(s) == "0.5"                      # c06_check.py's old default; C08 passed 0.8 in the environment
    assert study.follows(s) == s


def test_name_defaults_are_the_scripts_own():
    assert study.name("C05", {}) == "C05" and study.name("C06", {}) == "C06"
    assert study.name("C06", {"PARTURA_C0X": ""}) == "C06"
    assert study.name("C06", {"PARTURA_C0X": "PROD"}) == "PROD"


def test_old_scheduling_list_is_unchanged():
    for d in ("coldstart_C05", "coldstart_C06", "coldstart_C07"):
        assert study.scheduling_env({"PARTURA_STUDY_DIR": d}) is True
    for d in ("coldstart_C08", "coldstart_C04", "other", ""):
        assert study.scheduling_env({"PARTURA_STUDY_DIR": d}) is False
    assert study.scheduling_env({}) is False


def test_prod_directory_comes_from_the_environment():
    assert study.dirname("PROD", {"PARTURA_STUDY_DIR": "prod_W01"}) == "prod_W01"
    with pytest.raises(SystemExit):
        study.dirname("PROD", {})
    for bad in ("../x", "a/b", ".hidden"):
        with pytest.raises(SystemExit):
            study.dirname("PROD", {"PARTURA_STUDY_DIR": bad})


def test_prod_names_and_prefixes():
    assert study.prefix("PROD") == "prod"
    assert study.m_prefix("PROD") == "prod"                          # PROD runs its own main AlphaCube: prods901M1_I0_open_search
    assert study.follows("PROD") == "C08"
    assert not study.is_legacy("PROD")


def test_prod_follows_c08_at_every_switch_except_the_documented_ones():
    """Every switch in partura/study.py, evaluated for PROD and for C08: equal, unless listed here with the reason."""
    env = {"PARTURA_STUDY_DIR": "prod_W01", "PARTURA_C0X": "PROD"}
    switches = {
        "neutral_extra": lambda s: study.neutral_extra(s),
        "r_additions": lambda s: study.r_additions(s, env),
        "ctrl_strike_default": lambda s: study.ctrl_strike_default(s),
        "scheduling_env": lambda s: study.scheduling_env({"PARTURA_STUDY_DIR": study.dirname(s, env), "PARTURA_C0X": s}),
        "dirname": lambda s: study.dirname(s, env),
        "prefix": lambda s: study.prefix(s),
        "m_prefix": lambda s: study.m_prefix(s),
    }
    documented = {
        "r_additions": "PLAN/rules.md say accessions; C08's code gate (STUDY == 'C06') never let C08 have them",
        "ctrl_strike_default": "C08 passed 0.8 in the environment; PROD makes it the default",
        "scheduling_env": "scheduling only (REPROMOTE etc.); PROD's M is C07's M run again, which had it",
        "dirname": "its own directory", "prefix": "its own tags", "m_prefix": "its own main AlphaCube",
    }
    assert set(documented) <= set(switches)
    for name, f in switches.items():
        if name not in documented:
            assert f("PROD") == f("C08"), name
    # and the documented differences are exactly these values
    assert switches["r_additions"]("PROD") is True and switches["r_additions"]("C08") is False
    assert switches["ctrl_strike_default"]("PROD") == "0.8"
    assert switches["scheduling_env"]("PROD") is True and switches["scheduling_env"]("C08") is False


def test_prod_r_additions_can_be_switched_off_for_c08_as_it_ran():
    assert study.r_additions("PROD", {"PARTURA_R_ADDITIONS": "0"}) is False
    assert study.r_additions("PROD", {"PARTURA_R_ADDITIONS": "1"}) is True
    assert study.r_additions("PROD", {}) is True


# ---- the scripts really use the module (no inline study literals left in the four switch points)
SWITCH_SCRIPTS = ["scripts/c05_round.py", "scripts/c05_locate.py", "scripts/c06_check.py", "scripts/idea_search.py"]


@pytest.mark.parametrize("rel", SWITCH_SCRIPTS)
def test_switch_scripts_go_through_the_study_module(rel):
    src = (ROOT / rel).read_text(encoding="utf-8")
    assert "from partura import study" in src
    code = "\n".join(l.split("#")[0] for l in src.splitlines())             # comments may still talk about C06 / C08
    assert not re.search(r'coldstart_\{', code), "inline research/coldstart_<study> path"
    assert not re.search(r'STUDY\s*(==|in|!=)\s*[\(\"\']', code), "inline comparison of the study with a literal"
    assert '"coldstart_C0' not in code


# ---- c06_check.py end to end, for PROD, in a throw-away directory under research/
GOOD = ["cross_mean(day_std(Amt), 30)", "cross_mean(day_std(Amt), 20)", "cross_mean(day_std(Amt), 10)", "cross_mean(day_std(Ret), 20)",
        "cross_mean(day_sum(Amt), 30)", "cross_mean(day_sum(Volume), 30)", "cross_mean(day_std(Volume), 30)", "cross_mean(day_std(Close), 30)",
        "cross_mean(day_std(Vwap), 30)"]
ALPHACUBE = Path(os.environ.get("ALPHACUBE_ROOT", Path.home() / "Desktop" / "AlphaCube-steering"))


@pytest.fixture
def seed_dir():
    name = f"prod_test_{uuid.uuid4().hex[:8]}"
    base = ROOT / "research" / name
    r1 = base / "partura" / "s999" / "r1"
    r1.mkdir(parents=True)
    yield name, r1
    shutil.rmtree(base, ignore_errors=True)


def _write_round(r1, control_rho):
    import yaml
    a, b = GOOD[:4], GOOD[4:8]
    (r1 / "missions.yaml").write_text(yaml.safe_dump({"seed": 999, "round": 1, "slots": [
        {"type": "N", "hypothesis": "h1", "seeds": a}, {"type": "N", "hypothesis": "h2", "seeds": b}]}), encoding="utf-8")
    (r1 / "loc.json").write_text(json.dumps({"heads": [{"expr": GOOD[8]}], "enrichment": [], "core_cards": []}), encoding="utf-8")
    (r1 / "audit_1.yaml").write_text(yaml.safe_dump({"attempt": 1, "slots": [
        {"slot": "a", "novelty": 4, "soundness": 4, "struck_seeds": []}, {"slot": "b", "novelty": 3, "soundness": 3, "struck_seeds": []}], "R": []}), encoding="utf-8")
    rows = []
    for i, e in enumerate(a + b):
        c = {"liq": 0.1, "vol": 0.1, "rev": 0.1, "known": control_rho if i == 0 else 0.1, "size": 0.1}      # seed 1 of slot a sits at control_rho with a control
        rows.append({"where": f"slot x seed {i}", "expr": e, "gate": True, "max_head": 0.2, "controls": c})
    (r1 / "corr_1.json").write_text(json.dumps({"heads": 1, "rows": rows}), encoding="utf-8")


def _finalize(name, extra_env):
    env = {**os.environ, "PARTURA_C0X": "PROD", "PARTURA_STUDY_DIR": name, "ALPHACUBE_ROOT": str(ALPHACUBE)}
    env.pop("C06_CTRL_STRIKE", None)
    env.update(extra_env)
    return subprocess.run([sys.executable, str(ROOT / "scripts" / "c06_check.py"), "999", "1", "--finalize"], cwd=ROOT, env=env, capture_output=True, text=True)


@pytest.mark.skipif(not (ALPHACUBE / "src" / "alphacube").is_dir(), reason="AlphaCube checkout not available")
def test_c06_check_for_prod_reads_its_directory_and_strikes_at_0_8(seed_dir):
    name, r1 = seed_dir
    _write_round(r1, control_rho=0.6)              # between C06's 0.5 and C08's 0.8
    r = _finalize(name, {})
    assert r.returncode == 0, r.stdout + r.stderr
    assert "FINALIZED after 1 audit" in r.stdout
    final = (r1 / "missions_final.yaml").read_text(encoding="utf-8")
    assert "audit_failed" not in final, "0.6 against a control must not strike a seed at PROD's default (0.8)"
    rec = json.loads((r1 / "audit_record.json").read_text(encoding="utf-8"))
    assert [s["kept"] for s in rec["slots"]] == [4, 4] and all(s["pass"] for s in rec["slots"])


@pytest.mark.skipif(not (ALPHACUBE / "src" / "alphacube").is_dir(), reason="AlphaCube checkout not available")
def test_c06_check_strike_line_env_still_overrides(seed_dir):
    name, r1 = seed_dir
    _write_round(r1, control_rho=0.6)
    r = _finalize(name, {"C06_CTRL_STRIKE": "0.5"})              # C06's line: the seed is struck, slot a keeps 3 < 4 seeds -> plain GP
    assert r.returncode == 0, r.stdout + r.stderr
    rec = json.loads((r1 / "audit_record.json").read_text(encoding="utf-8"))
    assert rec["slots"][0]["kept"] == 3 and rec["slots"][0]["pass"] is False and rec["slots"][1]["pass"] is True


@pytest.mark.skipif(not (ALPHACUBE / "src" / "alphacube").is_dir(), reason="AlphaCube checkout not available")
def test_c06_check_for_prod_needs_the_directory_setting(seed_dir):
    name, r1 = seed_dir
    _write_round(r1, control_rho=0.1)
    env = {**os.environ, "PARTURA_C0X": "PROD", "ALPHACUBE_ROOT": str(ALPHACUBE)}
    env.pop("PARTURA_STUDY_DIR", None)
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / "c06_check.py"), "999", "1"], cwd=ROOT, env=env, capture_output=True, text=True)
    assert r.returncode != 0 and "PARTURA_STUDY_DIR" in (r.stdout + r.stderr)
