"""PROD W01: the library construction of scripts/prod_lib.py (the logic of scripts/c08_final.py) on small synthetic evidence / panels."""
import json
import sys
from pathlib import Path

import numpy as np
import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT))
import c05_lib  # noqa: E402
import prod_lib  # noqa: E402


def head(expr, score=0.8, sign=1.0, hl=5.0):
    return {"expr": expr, "sign": sign, "hl": hl, "score": score, "train": score + 0.1, "valid": score}


def write_episode(ep_dir, name, heads, scored=100, seconds=10.0, complete=True):
    d = Path(ep_dir) / name
    d.mkdir(parents=True)
    ev = {"arms": {"control": {"heads": heads, "scored": scored, "seconds": seconds, "passers": len(heads)}}}
    if complete:
        ev["complete"] = True
    (d / "evidence.json").write_text(json.dumps(ev))
    return d


@pytest.fixture
def study_dir(tmp_path):
    ep, D = tmp_path / "episodes", tmp_path / "research" / "prod_W01"
    ep.mkdir()
    (D / "arms").mkdir(parents=True)
    (D / "loc").mkdir()
    return ep, D


def build(ep, S=901, m=None):
    m = m or {1: [head("m1a"), head("m1b")], 2: [head("m2a")], 3: [], 4: [head("m4a")]}
    for e, hs in m.items():
        write_episode(ep, f"prods{S}M{e}_I0_open_search", hs, scored=192, seconds=100.0)


def test_seed_library_orders_m_then_missions_then_accessions_per_round(study_dir):
    ep, D = study_dir
    build(ep)
    write_episode(ep, "prods901Pr1a_I0_open_search", [head("e1")], scored=96, seconds=5.0)
    write_episode(ep, "prods901Pr1b_I0_open_search", [head("n1")], scored=96, seconds=6.0)
    write_episode(ep, "prods901Pr2a_I0_open_search", [head("e2")], scored=96)
    (D / "arms" / "s901_P_r1.yaml").write_text(yaml.safe_dump({"slots": [{"type": "E", "core": "c"}, {"type": "N", "seeds": ["x"]}]}))
    (D / "arms" / "s901_P_r2.yaml").write_text(yaml.safe_dump({"slots": [{"type": "N", "audit_failed": True}, {"type": "N", "seeds": ["x"]}]}))
    (D / "arms" / "s901_P_r1_R.json").write_text(json.dumps({"paid": 12, "replacements": [], "additions": [head("acc1")]}))
    (D / "loc" / "s901_P_r1.json").write_text(json.dumps({"paid": 40}))
    r = prod_lib.seed_library(901, ep, D, c05_lib)
    assert [h["expr"] for h in r["M"]] == ["m1a", "m1b", "m2a", "m4a"] and {h["role"] for h in r["M"]} == {"M"}
    assert [(h["expr"], h["role"]) for h in r["P"]] == [("m1a", "M"), ("m1b", "M"), ("m2a", "M"), ("m4a", "M"),
                                                          ("e1", "E"), ("n1", "N"), ("acc1", "R+"), ("e2", "N0")]
    assert r["evals"] == {"M": 4 * 192, "P": 96 * 3 + 12 + 40}
    assert r["gpu_seconds"]["P"] == 5.0 + 6.0 + 10.0 and r["gpu_seconds"]["M"] == 400.0
    assert [m["type"] for m in r["missions"]] == ["E", "N", "N0"] and r["missions"][0]["heads"] == 1
    assert next(h for h in r["P"] if h["expr"] == "acc1")["round"] == 1


def test_failed_mission_without_evidence_is_listed_not_fatal(study_dir):
    ep, D = study_dir
    build(ep)
    (ep / "prods901Pr3a_I0_open_search").mkdir()
    r = prod_lib.seed_library(901, ep, D, c05_lib)
    assert r["missions"] == [{"seed": 901, "round": 3, "slot": "a", "type": "failed", "scored": 0, "heads": 0}]


def test_unfinished_m_batch_is_an_error(study_dir):
    ep, D = study_dir
    build(ep, m={1: [head("a")], 2: [], 3: []})
    write_episode(ep, "prods901M4_I0_open_search", [head("zz")], complete=False)           # evidence written once, not final; no log
    with pytest.raises(SystemExit):
        prod_lib.seed_library(901, ep, D, c05_lib)


def test_r_replacement_chain_is_followed_to_its_end_and_marks_the_role(study_dir):
    ep, D = study_dir
    build(ep, m={1: [head("m1a", 0.6)], 2: [], 3: [], 4: []})
    write_episode(ep, "prods901Pr1a_I0_open_search", [head("e1", 0.7)])
    (D / "arms" / "s901_P_r1.yaml").write_text(yaml.safe_dump({"slots": [{"type": "E", "core": "c"}, {"type": "N", "seeds": ["x"]}]}))
    # round 1 replaces m1a by v1 and e1 by w1; round 2 replaces v1 by v2 (the chain of C05 revision 13)
    (D / "arms" / "s901_P_r1_R.json").write_text(json.dumps({"paid": 5, "replacements": [{"head": "m1a", **head("v1", 0.9)}, {"head": "e1", **head("w1", 0.95)}]}))
    (D / "arms" / "s901_P_r2_R.json").write_text(json.dumps({"paid": 5, "replacements": [{"head": "v1", **head("v2", 1.2)}]}))
    r = prod_lib.seed_library(901, ep, D, c05_lib)
    got = {h["expr"]: h for h in r["P"]}
    assert set(got) == {"v2", "w1"}
    assert got["v2"]["replaced"] == "m1a" and got["v2"]["role"] == "M+R" and got["v2"]["score"] == 1.2
    assert got["w1"]["replaced"] == "e1" and got["w1"]["role"] == "E+R"
    assert [h["expr"] for h in r["M"]] == ["m1a"]                                         # the M library itself is not touched by Partura's R


def test_chain_end_handles_cycles():
    rep = {"a": {"expr": "b", **head("b")}, "b": {"expr": "a", **head("a")}}
    assert prod_lib.chain_end(rep, "a")["expr"] in ("a", "b")                                       # terminates
    assert prod_lib.chain_end(rep, "zzz") is None


def test_dedup_rules():
    rng = np.random.default_rng(0)
    base = rng.normal(size=(40, 30))
    Z = {"a": base, "b": base + 0.01 * rng.normal(size=base.shape), "c": rng.normal(size=base.shape), "anti": -base + 0.01 * rng.normal(size=base.shape),
         "known": rng.normal(size=base.shape)}
    RK = {"a": 0.0, "b": 0.0, "c": 0.1, "anti": 0.0, "known": 0.6}

    def rho(x, y):
        return float(np.mean([np.corrcoef(x[i], y[i])[0, 1] for i in range(len(x))]))
    lst = [{"expr": e} for e in ["a", "b", "c", "anti", "known", "c", "missing"]]
    kept = [h["expr"] for h in prod_lib.dedup(lst, Z, RK, rho)]
    assert kept == ["a", "c"]                      # b >= 0.7 with a, anti <= -0.5 with a, known >= 0.5 with the known family, c twice, missing has no panel
    # order matters: greedy, first come first kept
    assert [h["expr"] for h in prod_lib.dedup([{"expr": "b"}, {"expr": "a"}], Z, RK, rho)] == ["b"]


def test_wave_library_dedups_across_seeds_by_score_and_keeps_the_seed():
    rng = np.random.default_rng(1)
    x = rng.normal(size=(30, 20))
    Z = {"p": x, "q": x + 0.01 * rng.normal(size=x.shape), "r": rng.normal(size=x.shape)}
    RK = {k: 0.0 for k in Z}

    def rho(a, b):
        return float(np.mean([np.corrcoef(a[i], b[i])[0, 1] for i in range(len(a))]))
    per_seed = {902: [head("q", 0.9)], 901: [head("p", 0.7), head("r", 0.6)]}
    w = prod_lib.wave_library(per_seed, Z, RK, rho)
    assert [(h["expr"], h["seed"]) for h in w] == [("q", 902), ("r", 901)]                           # q (0.9) beats its twin p (0.7); r is independent
    assert per_seed[901][0].get("seed") is None                                                      # inputs are not modified


def test_fuse_is_an_equal_weight_zrank_mean_over_the_names_each_head_has():
    nan = np.nan
    SM = {"a": np.array([[1.0, 2.0, 3.0], [1.0, 2.0, 3.0]], np.float32), "b": np.array([[3.0, 2.0, nan], [1.0, 2.0, 3.0]], np.float32)}

    def zrank(x):
        out = np.full(x.shape, np.nan)
        for i, row in enumerate(x):
            ok = np.isfinite(row)
            r = row[ok].argsort().argsort()
            out[i, ok] = (r + 0.5) / ok.sum() - 0.5
        return out
    f = prod_lib.fuse(["a", "b"], SM, zrank)
    za, zb = zrank(SM["a"].astype(float)), zrank(SM["b"].astype(float))
    assert np.allclose(f[1], (za[1] + zb[1]) / 2)
    assert np.isclose(f[0, 2], za[0, 2])                                                             # b is missing there: a alone
    assert prod_lib.fuse([], SM, zrank) is None
    g = prod_lib.fuse(["a"], SM, zrank, neutralize=lambda a: a * 0 + 7)
    assert np.all(g == 7)


def test_head_row_has_in_sample_fields_only():
    row = prod_lib.head_row({**head("e"), "seed": 901, "role": "E", "test_sharpe": 1.0, "forward_sharpe": 2.0})
    assert "test_sharpe" not in row and "forward_sharpe" not in row and row["seed"] == 901 and row["expr"] == "e"
