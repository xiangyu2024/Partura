"""scripts/plugin_acceptance.py: identical evidence says "identical"; every kind of difference is found, first.

    ALPHACUBE_ROOT=~/Desktop/AlphaCube-steering PYTHONPATH=~/Desktop/AlphaCube-steering/src:. \
        python -m pytest tests/test_plugin_acceptance.py -q
"""
import copy
import importlib.util
import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("plugin_acceptance", ROOT / "scripts" / "plugin_acceptance.py")
pa = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pa)


def cand(i, score=1.0):
    return {"expr": f"day_std(Ret_{i})", "fit": 0.03 * score, "score": score, "s_train": score + 0.5, "s_valid": score,
            "share": float("nan"), "train": 1.5, "valid": 1.0, "hl": 5.0, "sign": 1.0, "rho_known": 0.1 * i,
            "ir_train": float("nan"), "dann_valid": 0.123456789012345}


def arm(n=5, sampling=None):
    return {"error": None, "checkpoints": 4, "seconds": 600.1, "scored": 143, "gate_fail": 38, "scoring_seconds": 135.0, "archive": 105,
            "live": 105, "passers": 26, "sampling": sampling if sampling is not None else {"proposed": 521, "accepted": 237, "thinned": 277},
            "candidates": [cand(i, 2.0 - 0.1 * i) for i in range(n)], "independent_distinct": 1, "efficiency_per_100": 0.7,
            "heads": [dict(cand(0), rho_pool=0.2, rho_known_traded=0.3)]}


def evidence(**arms):
    return {"idea": {"id": "I5"}, "reward": "long", "threshold": 1.0, "screen_base": "pool", "score_scale": "long_sharpe",
            "code": {"scripts/idea_search.py": "aaaaaaaaaaaa", "partura/steer.py": "bbbbbbbbbbbb", "guidance/B01.yaml": "cccccccccccc"},
            "reward_device": "cuda", "budget": 192, "population": 48, "seed": 1, "boost": 8.0, "period": ["a", "b", "c"],
            "guidance": "guidance/B01.yaml", "parts": ["priors"], "halflives": [0.0, 5.0, 20.0], "arms": arms or {"steer": arm()}}


def test_identical_evidence_is_identical_and_timings_are_ignored():
    a, b = evidence(), evidence()
    b["arms"]["steer"]["seconds"] = 9999.0
    b["arms"]["steer"]["scoring_seconds"] = 1.0
    b["code"]["scripts/idea_search.py"] = "different"          # the code fingerprints differ by construction
    lines, ok = pa.compare(a, b)
    assert ok and lines[-1].startswith("arm steer: identical")


@pytest.mark.parametrize("edit,needle", [
    (lambda e: e["arms"]["steer"]["candidates"][3].update(score=2.0000000001), "candidate #3"),
    (lambda e: e["arms"]["steer"]["candidates"][2].update(expr="other"), "candidate #2: expression"),
    (lambda e: e["arms"]["steer"]["sampling"].update(thinned=278), "sampling['thinned']"),
    (lambda e: e["arms"]["steer"]["sampling"].update(mutation_refused=1), "sampling['mutation_refused']"),
    (lambda e: e["arms"]["steer"].update(scored=144), "scored"),
    (lambda e: e["arms"]["steer"].update(gate_fail=39), "gate_fail"),
    (lambda e: e["arms"]["steer"]["candidates"].pop(), "candidates: fresh lists 4"),
    (lambda e: e["arms"]["steer"]["candidates"][0].update(dann_valid=0.123456789012346), "dann_valid"),
    (lambda e: e["arms"]["steer"]["heads"][0].update(rho_pool=0.21), "head #0"),
    (lambda e: e["arms"]["steer"].update(independent_distinct=2), "independent_distinct"),
])
def test_every_kind_of_difference_is_found_and_named(edit, needle):
    fresh, stored = evidence(), evidence()
    edit(fresh)
    lines, ok = pa.compare(fresh, stored)
    assert not ok
    assert any("DIFFERENT" in l and needle in l for l in lines), lines


def test_the_first_difference_is_the_one_reported():
    fresh, stored = evidence(), evidence()
    fresh["arms"]["steer"]["candidates"][4].update(score=0.0)
    fresh["arms"]["steer"]["candidates"][1].update(score=0.0)
    (line,) = [l for l in pa.compare(fresh, stored)[0] if "DIFFERENT" in l]
    assert "candidate #1" in line


def test_nan_equals_nan_and_nothing_else_does():
    assert pa.same(float("nan"), float("nan"))[0]
    assert not pa.same(float("nan"), 0.0)[0] and not pa.same(0.0, float("nan"))[0]
    assert pa.same(1, 1.0)[0] and not pa.same(True, 2)[0]


def test_rtol_turns_a_last_digit_into_identical_within_tolerance_but_never_by_default():
    fresh, stored = evidence(), evidence()
    fresh["arms"]["steer"]["candidates"][0]["score"] *= 1 + 1e-12
    assert not pa.compare(fresh, stored)[1]
    lines, ok = pa.compare(fresh, stored, rtol=1e-9)
    assert ok and "within rtol" in lines[-1]
    fresh["arms"]["steer"]["candidates"][0]["score"] *= 1 + 1e-3
    assert not pa.compare(fresh, stored, rtol=1e-9)[1]


def test_runs_of_different_experiments_are_not_compared_as_if_they_were_the_same():
    for key, value in (("seed", 2), ("budget", 384), ("parts", ["priors", "hood"]), ("halflives", [0.0, 5.0]), ("reward", "long_screen")):
        fresh, stored = evidence(), evidence()
        fresh[key] = value
        lines, ok = pa.compare(fresh, stored)
        assert not ok and any("NOT THE SAME EXPERIMENT" in l and key in l for l in lines), key
    fresh, stored = evidence(), evidence()
    fresh["idea"] = {"id": "I1"}
    assert not pa.compare(fresh, stored)[1]


def test_a_key_only_one_side_recorded_is_not_a_difference():
    fresh, stored = evidence(), evidence()
    del stored["screen_base"], stored["score_scale"]                # older evidence
    for a in stored["arms"].values():
        del a["checkpoints"], a["error"]
    assert pa.compare(fresh, stored)[1]


def test_opt_in_plugin_fixes_in_the_fresh_run_are_flagged():
    fresh, stored = evidence(), evidence()
    fresh["plugin_fixes"] = ["nt_twins"]
    lines, ok = pa.compare(fresh, stored)
    assert not ok and any("opt-in plugin fixes" in l for l in lines)
    fresh["plugin_fixes"] = []
    assert pa.compare(fresh, stored)[1]


def test_arms_present_on_one_side_only_are_reported_not_compared_and_no_common_arm_is_not_a_pass():
    fresh, stored = evidence(steer=arm(), control=arm(sampling={})), evidence(steer=arm())
    lines, ok = pa.compare(fresh, stored)
    assert ok and any("arm control: only in the fresh" in l for l in lines)
    lines, ok = pa.compare(evidence(control=arm(sampling={})), evidence(steer=arm()))
    assert not ok and any("nothing to compare" in l for l in lines)


def test_a_guidance_file_under_another_name_is_compared_by_its_fingerprint():
    fresh, stored = evidence(), evidence()
    fresh["code"]["guidance/B01_e7.yaml"] = fresh["code"].pop("guidance/B01.yaml")
    assert pa.guidance_fingerprint(fresh["code"]) == pa.guidance_fingerprint(stored["code"])
    assert pa.compare(fresh, stored)[1]


def test_reward_code_that_differs_from_the_stored_runs_is_called_out():
    fresh, stored = evidence(), evidence()
    fresh["code"]["partura/steer.py"] = "zzzzzzzzzzzz"
    lines, ok = pa.compare(fresh, stored)
    assert ok and any("partura/steer.py differs" in l for l in lines)       # a note: the comparison itself still stands


def test_main_reads_files_directories_and_exit_codes(tmp_path, capsys):
    d1, d2 = tmp_path / "e_new", tmp_path / "e_old"
    for d in (d1, d2):
        d.mkdir()
        (d / "evidence.json").write_text(json.dumps(evidence(), default=float))
    assert pa.main([str(d1), str(d2 / "evidence.json")]) == 0
    assert "identical" in capsys.readouterr().out
    bad = evidence()
    bad["arms"]["steer"]["candidates"][0]["score"] = math.nan
    (d1 / "evidence.json").write_text(json.dumps(bad, default=float))
    assert pa.main([str(d1), str(d2)]) == 1
    out = capsys.readouterr().out
    assert "NOT identical" in out and "candidate #0" in out


def test_the_header_of_the_script_names_the_two_stored_runs_and_their_exact_commands():
    head = (ROOT / "scripts" / "plugin_acceptance.py").read_text(encoding="utf-8").split('"""')[1]
    for needle in ("I5_within_bucket_anything e7cx \"1\" --reward long --arms control --budget 192 --population 48",
                   "I5_within_bucket_anything e7bx \"1\" --reward long --parts priors --arms steer --budget 192 --population 48",
                   "--tag e7cx1 --seed 1 --reward long --arms control --budget 192 --population 48",
                   "--tag e7bx1 --seed 1 --reward long --parts priors --arms steer --budget 192 --population 48",
                   "e7c1_I5_within_bucket_anything", "e7b1_I5_within_bucket_anything", "acc7c1_I5_within_bucket_anything", "vendor/AlphaCube-steering"):
        assert needle in head, needle
