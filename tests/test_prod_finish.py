"""PROD W01: the structural check of a finalized plan (scripts/prod_finish.py check_final) -- what is about to run on a server."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import prod_finish  # noqa: E402

E = ["e%d" % i for i in range(8)]


def good():
    plan = {"seed": 901, "round": 1, "slots": [{"type": "E", "core": "c", "hypothesis": "h", "seeds": E[:5]},
                                              {"type": "N", "note": "audit did not pass", "audit_failed": True, "proposed_type": "N"}],
            "R": [{"head": "h", "variants": ["v1", "v2"]}], "audit": {"attempts": 1}}
    return plan, {"slots": [{}, {}], "R": []}


def test_a_good_plan_passes():
    plan, rec = good()
    assert prod_finish.check_final(plan, rec, 901, 1) == []


def test_each_defect_is_reported():
    def issues(mut):
        plan, rec = good()
        mut(plan, rec)
        return prod_finish.check_final(plan, rec, 901, 1)
    assert any("expected 901" in x for x in issues(lambda p, r: p.update(seed=902)))
    assert any("expected 2" in x for x in issues(lambda p, r: p["slots"].pop()))
    assert any("3 seeds" in x for x in issues(lambda p, r: p["slots"][0].update(seeds=E[:3])))
    assert any("17 seeds" in x for x in issues(lambda p, r: p["slots"][0].update(seeds=["s%d" % i for i in range(17)])))
    assert any("without a core" in x for x in issues(lambda p, r: p["slots"][0].update(core="")))
    assert any("plain-GP" in x for x in issues(lambda p, r: p["slots"][1].update(seeds=["x"])))
    assert any("banned operator" in x for x in issues(lambda p, r: p["slots"][0].update(seeds=E[:4] + ["ts_spearman(a, b, 10)"])))
    assert any("banned operator" in x for x in issues(lambda p, r: p["R"][0].update(variants=["nt_foo(x)"])))
    assert any("at most 16" in x for x in issues(lambda p, r: p.update(R=[{"head": "h", "variants": ["v%d" % i for i in range(17)]}])))
    assert any("no head or no variants" in x for x in issues(lambda p, r: p.update(R=[{"head": "h", "variants": []}])))
    assert any("audit_record" in x for x in issues(lambda p, r: r.update(slots=[{}])))
    assert any("type" in x for x in issues(lambda p, r: p["slots"][0].update(type="X")))


def test_a_plan_with_no_R_and_two_gp_slots_is_fine():
    plan = {"seed": 901, "round": 3, "slots": [{"type": "N", "hypothesis": "h", "seeds": E[:4]}, {"type": "N", "hypothesis": "g", "seeds": E[4:8]}]}
    assert prod_finish.check_final(plan, {"slots": [{}, {}]}, 901, 3) == []
