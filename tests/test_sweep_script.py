"""K002 tooling, part B: ``scripts/sweep.py --only-extra`` (and that nothing changes without it).  The REAL script runs,
against a small synthetic world and a PanelSet stand-in (tests/k002_helpers.py).  The per-hypothesis direction lock
(``lock: true``) is in tests/test_sweep_lock.py.
"""
import json
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import k002_helpers as H  # noqa: E402


@pytest.fixture(autouse=True)
def _isolation():
    from partura.splits import SPLITS
    saved = dict(SPLITS)
    import torch
    threads = torch.get_num_threads()
    yield
    SPLITS.clear()
    SPLITS.update(saved)
    torch.set_num_threads(threads)


def _hypo(tmp_path, entries, name="hypo.yaml"):
    p = tmp_path / name
    p.write_text(yaml.safe_dump(entries, allow_unicode=True), encoding="utf-8")
    return str(p)


def _world(tmp_path):
    w = H.World(n_days=300, n_names=50)
    H.write_config(tmp_path, "T001", w)
    w.set(H.KNOWN, -(0.8 * w.x + 0.6 * w.noise()))
    w.set(H.XFROZEN, 0.7 * w.x + 0.7 * w.noise())
    return w


def _sweep(monkeypatch, tmp_path, w, argv, propose_calls=None):
    H.stub_propose(monkeypatch, propose_calls)
    ns = H.run_script(monkeypatch, tmp_path, "sweep.py", ["T001"] + list(argv), H.fake_panelset(w))
    return ns, json.loads((tmp_path / "runs" / "T001" / "sweep_s1.json").read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------------------------- --only-extra
EXTRA = {"h_a": {"expr": "cross_mean(day_sum(Amt), 20)", "why": "first"},
         "h_b": "cross_mean(div(day_sum(Amt), FloatCap), 20)",
         "h_c": {"expr": "neg(LogFloatCap)", "why": "third"}}


def test_only_extra_scores_the_benchmarks_and_the_extra_hypotheses_and_nothing_else(monkeypatch, tmp_path):
    w = _world(tmp_path)
    calls = []
    _, out = _sweep(monkeypatch, tmp_path, w, ["--extra", _hypo(tmp_path, EXTRA), "--only-extra"], calls)
    assert list(out["results"]) == ["v_base", "k_known", "k_known_xfrozen", "h_a", "h_b", "h_c"]
    assert {v["kind"] for v in out["results"].values()} == {"base", "bench", "hypo"}
    assert [out["results"][k]["kind"] for k in ("v_base", "k_known", "k_known_xfrozen")] == ["base", "bench", "bench"]
    assert calls == []                                               # propose() is never called
    assert out["only_extra"] is True


def test_only_extra_with_several_extra_files(monkeypatch, tmp_path):
    w = _world(tmp_path)
    f1 = _hypo(tmp_path, {"h_a": EXTRA["h_a"]}, "one.yaml")
    f2 = _hypo(tmp_path, {"h_c": EXTRA["h_c"]}, "two.yaml")
    _, out = _sweep(monkeypatch, tmp_path, w, ["--extra", f"{f1},{f2}", "--only-extra"])
    assert list(out["results"]) == ["v_base", "k_known", "k_known_xfrozen", "h_a", "h_c"]


def test_only_extra_needs_hypotheses(monkeypatch, tmp_path):
    w = _world(tmp_path)
    H.stub_propose(monkeypatch)
    for extra in ([], ["--extra", str(tmp_path / "typo.yaml")], ["--extra", _hypo(tmp_path, {}, "empty.yaml")]):
        with pytest.raises(SystemExit, match="only-extra"):
            H.run_script(monkeypatch, tmp_path, "sweep.py", ["T001", "--only-extra"] + extra, H.fake_panelset(w))


# Golden values: scripts/sweep.py of main (cd926a3) on this source, with propose() returning nothing.  Without the flag the
# generated variants (ids, expressions, kinds, explanations, order) must be exactly these.
GOLDEN_IDS = ["v_base", "k_known", "k_known_xfrozen", "leaf_Amt_vol", "leaf_Amt_amtchg"] + \
    [f"mem_{op}{d}" for d in (5, 10, 30, 60) for op in ("mean", "max", "min", "ema", "stddev", "zscore", "decay_linear")] + \
    ["fold_mean", "fold_rank", "fold_sq", "win", "rk", "z60", "rel60", "bk_liq", "bk_known", "res_known", "res_liq"] + \
    [f"ov_{s}{w}" for w in ("025", "05", "10") for s in ("p", "m")] + \
    [f"{p}_{s}" for s in ("p", "m") for p in ("scr_xhi", "seg_lowliq", "seg_hiliq", "seg_new", "seg_xfrozen")]
GOLDEN_DIGEST = "64a27aeabfad1bfe45044f56784b84b3f31edd61"


def test_without_the_flag_the_generated_variants_are_exactly_what_main_generated(monkeypatch, tmp_path):
    import ast
    import hashlib
    import re
    w = _world(tmp_path)
    ns = {"re": re, "yaml": yaml, "Path": Path}
    tree = ast.parse((H.SCRIPTS / "sweep.py").read_text(encoding="utf-8"))
    fn = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "variants")
    ns.update(SRC=H.KNOWN, KNOWN=H.KNOWN, LIQ="cross_mean(day_sum(Amt), 30)", DT_WINDOWS=(5, 10, 30, 60), propose=lambda *a, **k: [],
              opt=lambda name, default=None: default, ONLY_EXTRA=False, LOCKS=set(), lock_of=lambda entry_id, entry: False)
    exec(compile(ast.Module(body=[fn], type_ignores=[]), "sweep.py", "exec"), ns)
    got = ns["variants"]()
    assert len(got) == 60
    assert sorted(got) == sorted(GOLDEN_IDS)
    digest = hashlib.sha1(json.dumps([[k, list(v)] for k, v in got.items()], ensure_ascii=False).encode()).hexdigest()
    assert digest == GOLDEN_DIGEST
    # and through the whole script: the kinds that ended up scored, propose() consulted exactly once
    calls = []
    _, out = _sweep(monkeypatch, tmp_path, w, ["--extra", _hypo(tmp_path, EXTRA)], calls)
    assert len(calls) == 1 and calls[0][0] == H.KNOWN
    kinds = {v["kind"] for v in out["results"].values()}
    assert kinds == {"base", "bench", "leaf", "memory", "shape", "neutral", "overlay", "screen", "segment", "hypo"}
    # two generated variants are the very same tree as an earlier one (seg_xfrozen_m = the xfrozen benchmark, z60 = mem_zscore60):
    # the script's dedupe by tree drops them, as it always did
    assert set(out["results"]) == (set(GOLDEN_IDS) - {"seg_xfrozen_m", "z60"}) | {"h_a", "h_b", "h_c"}
    assert "only_extra" not in out and "daily_fields" not in out and not any(v["sign_locked"] and v["kind"] == "hypo" for v in out["results"].values())


def test_the_sweep_records_the_daily_store_it_ran_with(monkeypatch, tmp_path):
    w = H.World(n_days=300, n_names=50)
    H.write_config(tmp_path, "T001", w, extra={"daily_fields": "/x/daily"})
    _, out = _sweep(monkeypatch, tmp_path, w, ["--extra", _hypo(tmp_path, EXTRA), "--only-extra"])
    assert out["daily_fields"] == "/x/daily"


# ------------------------------------------------------------------------------- --max under --only-extra
def _many(n):
    return {f"h_{i:02d}": {"expr": f"cross_mean(day_sum(Amt), {10 + i})", "why": f"hypothesis {i}"} for i in range(n)}


def test_only_extra_never_truncates_silently_it_stops_and_says_how_many_would_be_lost(monkeypatch, tmp_path):
    w = _world(tmp_path)
    H.stub_propose(monkeypatch)
    hy = _hypo(tmp_path, _many(6))
    # 3 benchmarks + 6 hypotheses = 9 variants: a cap of 9 fits, a cap of 8 loses one, a cap of 6 loses three
    for cap, lost in ((8, 1), (6, 3), (4, 5)):
        with pytest.raises(SystemExit, match=rf"{lost} of the --extra hypotheses would be dropped"):
            H.run_script(monkeypatch, tmp_path, "sweep.py", ["T001", "--only-extra", "--extra", hy, "--max", str(cap)], H.fake_panelset(w))
        assert not (tmp_path / "runs" / "T001" / "sweep_s1.json").exists()           # stopped before anything was scored
    ns = H.run_script(monkeypatch, tmp_path, "sweep.py", ["T001", "--only-extra", "--extra", hy, "--max", "9"], H.fake_panelset(w))
    assert len(ns["V"]) == 9
    # the default cap (260) is unchanged, and a hypothesis lost to a duplicate tree or a parse failure is not a cap casualty
    dup = {**_many(2), "h_dup": {"expr": "cross_mean(day_sum(Amt), 10)"}, "h_bad": {"expr": "neg(NoSuchField)"}}
    ns = H.run_script(monkeypatch, tmp_path, "sweep.py", ["T001", "--only-extra", "--extra", _hypo(tmp_path, dup, "dup.yaml"), "--max", "5"], H.fake_panelset(w))
    assert list(ns["V"]) == ["v_base", "k_known", "k_known_xfrozen", "h_00", "h_01"]


def test_without_the_flag_the_cap_still_truncates_as_it_always_did(monkeypatch, tmp_path):
    w = _world(tmp_path)
    _, out = _sweep(monkeypatch, tmp_path, w, ["--extra", _hypo(tmp_path, _many(3)), "--max", "4"])
    assert len(out["results"]) == 4 and set(out["results"]) <= set(out["results"]) and "h_00" not in out["results"]      # the generated variants came first and used the cap up


def test_only_extra_reports_the_hypotheses_that_did_not_make_it(monkeypatch, tmp_path, capsys):
    w = _world(tmp_path)
    ent = {**_many(2), "h_dup": {"expr": "cross_mean(day_sum(Amt), 10)"}, "h_bad": {"expr": "neg(NoSuchField)"}}
    _sweep(monkeypatch, tmp_path, w, ["--extra", _hypo(tmp_path, ent), "--only-extra"])
    text = capsys.readouterr().out
    assert "did not make it into the sweep" in text and "duplicate tree: h_dup" in text and "does not parse: h_bad" in text


# --------------------------------------------------------------------- base / twin / kind travel into the sweep file
def test_base_twin_and_kind_are_carried_into_the_sweep_file_and_plain_entries_get_no_such_keys(monkeypatch, tmp_path):
    w = _world(tmp_path)
    ent = {"x_car": {"expr": "cross_mean(day_sum(Amt), 30)", "kind": "carrier"},
           "h_mod": {"expr": "cross_mean(day_sum(Amt), 31)", "base": "x_car", "lock": True},
           "h_mod_k": {"expr": "cross_mean(day_sum(Amt), 32)", "base": "k_known"},
           "h_par": {"expr": "cross_mean(day_sum(Amt), 33)", "twin": "k_known"},
           "h_par_twin": {"expr": "cross_mean(day_sum(Amt), 34)", "base": "k_known_xfrozen"},
           "h_plain": {"expr": "cross_mean(day_sum(Amt), 35)", "why": "nothing special"},
           "h_bare": "cross_mean(day_sum(Amt), 36)"}
    _, out = _sweep(monkeypatch, tmp_path, w, ["--extra", _hypo(tmp_path, ent), "--only-extra"])
    r = out["results"]
    assert r["h_mod"]["base"] == "x_car" and r["h_mod"]["lock"] is True and r["h_mod_k"]["base"] == "k_known" and r["h_par_twin"]["base"] == "k_known_xfrozen"
    assert r["h_par"]["twin"] == "k_known" and r["x_car"]["declared_kind"] == "carrier"
    for k in ("h_plain", "h_bare", "v_base", "k_known", "k_known_xfrozen"):
        assert not {"base", "twin", "declared_kind", "lock"} & set(r[k]), k
    assert "base" not in r["x_car"] and "twin" not in r["h_mod"]


def test_a_base_or_twin_that_is_not_among_the_scored_variants_stops_the_sweep(monkeypatch, tmp_path):
    w = _world(tmp_path)
    H.stub_propose(monkeypatch)
    for key, bad in (("base", "nowhere"), ("twin", "nowhere")):
        ent = {"h_x": {"expr": "cross_mean(day_sum(Amt), 31)", key: bad}}
        with pytest.raises(SystemExit, match=rf"hypotheses whose {key} is not among the scored variants"):
            H.run_script(monkeypatch, tmp_path, "sweep.py", ["T001", "--only-extra", "--extra", _hypo(tmp_path, ent)], H.fake_panelset(w))
    # a carrier that the sweep dropped as a duplicate tree of an earlier variant is "not scored" either
    ent = {"x_dup": {"expr": "cross_mean(day_std(Amt), 30)"}, "h_x": {"expr": "cross_mean(day_sum(Amt), 31)", "base": "x_dup"}}
    with pytest.raises(SystemExit, match="dropped as a duplicate tree"):
        H.run_script(monkeypatch, tmp_path, "sweep.py", ["T001", "--only-extra", "--extra", _hypo(tmp_path, ent, "d.yaml")], H.fake_panelset(w))
    # the benchmarks are always there
    ent = {"h_x": {"expr": "cross_mean(day_sum(Amt), 31)", "base": "k_known_xfrozen", "twin": "v_base"}}
    ns = H.run_script(monkeypatch, tmp_path, "sweep.py", ["T001", "--only-extra", "--extra", _hypo(tmp_path, ent, "ok.yaml")], H.fake_panelset(w))
    assert ns["BASES"] == {"h_x": "k_known_xfrozen"} and ns["TWINS"] == {"h_x": "v_base"}
