"""PROD W01: workflows/prod_round.js against a mock of the Workflow runtime (tests/prod_round_harness.js): stage order, models, what each
prompt may and may not say, resuming, failure handling.  Needs node; skipped without it.  (The real runtime is not available here.)"""
import json
import re
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
NODE = shutil.which("node")
pytestmark = pytest.mark.skipif(NODE is None, reason="node not installed")
SCRIPT = ROOT / "workflows" / "prod_round.js"


def run(args, beh=None):
    r = subprocess.run([NODE, str(ROOT / "tests" / "prod_round_harness.js"), str(SCRIPT), json.dumps(args), json.dumps(beh or {})], capture_output=True, text=True, timeout=60)
    assert r.returncode == 0, r.stderr
    return json.loads(r.stdout)


def stages(d, seed):
    return [c["label"].split(":")[1] for c in d["calls"] if f"s{seed}:" in c["label"]]


def test_script_parses_without_the_meta_line():
    """The syntax check asked for: the body (meta removed) is valid as the body of an async function."""
    src = SCRIPT.read_text(encoding="utf-8")
    body = re.sub(r"^export const meta = \{[\s\S]*?\n\}\n", "", src, count=1, flags=re.M)
    assert "export const meta" not in body
    tmp = ROOT / "tmp" / "prod_round_check.js"
    tmp.parent.mkdir(exist_ok=True)
    tmp.write_text("(async (args, agent, parallel, log, phase, budget) => {\n" + body + "\n})\n", encoding="utf-8")
    r = subprocess.run([NODE, "--check", str(tmp)], capture_output=True, text=True)
    tmp.unlink()
    assert r.returncode == 0, r.stderr


def test_meta_is_a_pure_literal_with_the_four_phases():
    src = SCRIPT.read_text(encoding="utf-8")
    meta = re.search(r"^export const meta = \{[\s\S]*?\n\}\n", src, flags=re.M).group(0)
    assert "${" not in meta and "`" not in meta
    for t in ("Fetch", "Plan", "Audit", "Finish"):
        assert f"title: '{t}'" in meta


def test_each_seed_runs_fetch_pi_corr_audit_finish_once_with_the_right_models():
    d = run({"round": 2, "seeds": [901, 909]})
    assert d.get("error") is None
    for s in (901, 909):
        assert stages(d, s) == ["fetch", "pi", "corr", "audit", "finish"]
    model = {c["label"].split(":")[1]: c["model"] for c in d["calls"]}
    assert model == {"fetch": "claude-haiku-5-5", "pi": "claude-sonnet-5-5", "corr": "claude-haiku-5-5", "audit": "claude-haiku-5-5", "finish": "claude-haiku-5-5"}
    assert all(c["schema"] for c in d["calls"])
    assert [r["pushed"] for r in d["result"]["results"]] == [True, True] and d["result"]["round"] == 2
    assert not any("opus" in (c["model"] or "").lower() for c in d["calls"])


def test_commands_use_prod_scripts_and_the_prod_work_tree():
    d = run({"round": 3, "seeds": [905]})
    prompts = {c["label"].split(":")[1]: c["prompt"] for c in d["calls"]}
    assert 'prod_sync.sh fetch 3 "905"' in prompts["fetch"]
    assert "prod_sync.sh corr 3 905 1" in prompts["corr"]
    assert "scripts/prod_finish.py 3 905" in prompts["finish"]
    assert "PARTURA_C0X=PROD" in prompts["finish"] and "PARTURA_STUDY_DIR=prod_W01" in prompts["finish"] and "C06_CTRL_STRIKE=0.8" in prompts["finish"]
    for p in prompts.values():
        assert "/Users/wxy/Desktop/Partura/" not in p.replace("/Users/wxy/Desktop/Partura-prod/", "")      # never the other work tree
        assert "coldstart_" not in p and "c06_sync" not in p
    assert "/Users/wxy/Desktop/Partura-prod/research/prod_W01/rules.md" in prompts["pi"] and "partura/s905/r3/missions.yaml" in prompts["pi"]
    assert "audit_1.yaml" in prompts["audit"] and "corr_1.md" in prompts["audit"]


def test_prompts_do_not_mention_what_production_does_not_have():
    d = run({"round": 1, "seeds": [901]})
    forbidden = ["文献", "解剖", "Opus", "opus", "anatom", "literature", "对照", "旁听", "C05", "C06 ", "C07", "C08", "A 组", "B0", "shadow", "严格审计"]
    for c in d["calls"]:
        for w in forbidden:
            assert w not in c["prompt"], (c["label"], w)


def test_the_pi_does_not_read_what_the_audit_must_not_and_the_auditor_does_not_read_the_notebook():
    d = run({"round": 1, "seeds": [901]})
    pi = next(c["prompt"] for c in d["calls"] if c["label"].endswith(":pi"))
    au = next(c["prompt"] for c in d["calls"] if c["label"].endswith(":audit"))
    assert "notebook.md" in pi and "audit_1.yaml" not in pi
    assert "不读** " in au and "notebook.md" in au.split("你要读")[0]
    assert "sed -n '1,/^## 共性/p'" in au                                                                # only the heads table of loc.md


def test_resume_starts_at_the_named_stage():
    assert stages(run({"round": 1, "seeds": [901], "from": {"901": "pi"}}), 901) == ["pi", "corr", "audit", "finish"]
    assert stages(run({"round": 1, "seeds": [901], "from": {"901": "corr"}}), 901) == ["corr", "audit", "finish"]
    assert stages(run({"round": 1, "seeds": [901], "from": {"901": "audit"}}), 901) == ["audit", "finish"]
    d = run({"round": 1, "seeds": [901, 902], "from": {"902": "finish"}})
    assert stages(d, 902) == ["finish"] and stages(d, 901)[0] == "fetch"


def test_failures_stop_that_seed_only_and_say_where():
    d = run({"round": 1, "seeds": [901, 902]}, {"fetch": {"exit_code": 1, "output": "NOT READY"}})
    assert [r.get("failed") for r in d["result"]["results"]] == ["fetch", "fetch"]
    d = run({"round": 1, "seeds": [901]}, {"pi": {"path": "x", "slots": [], "n_R": 0, "check_exit_code": 1, "summary": "not admissible"}})
    assert d["result"]["results"][0]["failed"] == "pi-check" and stages(d, 901) == ["fetch", "pi"]
    d = run({"round": 1, "seeds": [901]}, {"pi": None})
    assert d["result"]["results"][0]["failed"] == "pi"
    d = run({"round": 1, "seeds": [901]}, {"audit": None})
    assert d["result"]["results"][0]["failed"] == "audit" and "finish" not in stages(d, 901)
    d = run({"round": 1, "seeds": [901]}, {"finish": {"exit_code": 1, "output": "NOT PUSHED: finalize failed (exit 1)"}})
    r = d["result"]["results"][0]
    assert r["failed"] == "finish" and r["pushed"] is False and "NOT PUSHED" in r["detail"]


def test_corr_is_retried_once():
    ok = {"exit_code": 0, "output": "corr_1.md written"}
    d = run({"round": 1, "seeds": [901]}, {"__seq:corr": [{"exit_code": 1, "output": "CORR FAILED"}, ok]})
    assert stages(d, 901) == ["fetch", "pi", "corr", "corr-retry", "audit", "finish"]
    assert d["result"]["results"][0]["pushed"] is True
    d = run({"round": 1, "seeds": [901]}, {"corr": {"exit_code": 1, "output": "CORR FAILED"}})
    assert d["result"]["results"][0]["failed"] == "corr" and stages(d, 901) == ["fetch", "pi", "corr", "corr-retry"]


def test_bad_arguments_are_refused():
    assert "round" in run({"round": 4, "seeds": [901]})["error"]
    assert "seeds" in run({"round": 1, "seeds": [801]})["error"]
    assert "seeds" in run({"round": 1, "seeds": []})["error"]
    assert "from" in run({"round": 1, "seeds": [901], "from": {"901": "nope"}})["error"]
