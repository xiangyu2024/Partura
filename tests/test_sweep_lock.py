"""K002 tooling, item F: the per-hypothesis direction lock of ``scripts/sweep.py`` (``lock: true`` on an --extra entry) and
``scripts/check_hypo.py`` with the extra key.  The REAL scripts run, against a small synthetic world and a PanelSet stand-in
(tests/k002_helpers.py).
"""
import json
import sys
from pathlib import Path

import numpy as np
import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import k002_helpers as H  # noqa: E402

from partura.hypo import lock_of  # noqa: E402


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


def _lock_world(tmp_path):
    """One panel the label leans on NEGATIVELY: the way it is written (+1) loses on the training period, minus one wins."""
    w = _world(tmp_path)
    bad = -(w.x + 0.3 * w.noise())
    w.set("neg(LogFloatCap)", bad)
    w.set("mul(neg(LogFloatCap), 1)", bad)                       # another expression, the very same panel
    w.set("neg(LogTotalCap)", bad)
    return w


def test_a_locked_hypothesis_keeps_the_direction_it_is_written_in_and_an_unlocked_one_flips(monkeypatch, tmp_path):
    w = _lock_world(tmp_path)
    ent = {"a_locked": {"expr": "neg(LogFloatCap)", "why": "ruler", "lock": True},
           "h_free": {"expr": "mul(neg(LogFloatCap), 1)", "why": "same panel, not locked"},
           "h_false": {"expr": "neg(LogTotalCap)", "lock": False}}
    ns, out = _sweep(monkeypatch, tmp_path, w, ["--extra", _hypo(tmp_path, ent), "--only-extra"])
    r = out["results"]
    # the locked one: pinned at +1 although its training-period long book wants -1; reported as locked; the rank IC's choice recorded
    assert r["a_locked"]["sign"] == 1.0 and r["a_locked"]["sign_locked"] is True and r["a_locked"]["sign_by"] == "locked"
    assert r["a_locked"]["sign_ic"] == -1.0
    # the same panel, unlocked: flips, exactly as today
    assert r["h_free"]["sign"] == -1.0 and r["h_free"]["sign_locked"] is False and r["h_free"]["sign_by"] == "long_book"
    assert r["h_free"]["sign_ic"] == -1.0
    # `lock: false` is the same as no key at all
    assert r["h_false"]["sign"] == -1.0 and r["h_false"]["sign_locked"] is False and r["h_false"]["sign_by"] == "long_book"
    # the premise of the test: on the training period the opposite direction really has the better long book
    assert r["a_locked"]["train_long"]["long_sharpe"] < r["h_free"]["train_long"]["long_sharpe"]
    assert ns["LOCKS"] == {"a_locked"}


def test_a_locked_book_is_the_book_of_the_expression_as_written(monkeypatch, tmp_path):
    from partura import books as bk
    w = _lock_world(tmp_path)
    ent = {"a_locked": {"expr": "neg(LogFloatCap)", "lock": True}}
    _, out = _sweep(monkeypatch, tmp_path, w, ["--extra", _hypo(tmp_path, ent), "--only-extra"])
    r = out["results"]["a_locked"]
    us = slice(0, w.cut["valid_end"])
    raw = w.panels["neg(LogFloatCap)"].astype(np.float64)
    tgt = w.target[: w.cut["holdout_end"]]
    books = bk.books(raw[: w.cut["holdout_end"]], tgt, us, {"utrain": us})            # +1 x panel, nothing else
    assert r["hl_long_u"] == books["hl_long"]
    assert r["utrain_long"]["long_ann"] == pytest.approx(books["by_rank"]["long"]["splits"]["utrain"]["long_ann"], abs=1e-12)


def test_entries_without_the_key_are_scored_as_before_and_a_root_screen_is_still_locked(monkeypatch, tmp_path):
    w = _lock_world(tmp_path)
    screen = "cs_last_high20(neg(cross_mean(day_std(Amt), 20)), cross_max(day_zero_ratio(Ret), 15))"
    w.set(screen, -(w.x + 0.3 * w.noise()))
    ent = {"h_free": {"expr": "mul(neg(LogFloatCap), 1)"}, "h_bare": "neg(LogTotalCap)", "h_screen": {"expr": screen}}
    ns, out = _sweep(monkeypatch, tmp_path, w, ["--extra", _hypo(tmp_path, ent), "--only-extra"])
    r = out["results"]
    assert ns["LOCKS"] == set()
    assert r["h_free"]["sign"] == -1.0 and r["h_bare"]["sign"] == -1.0 and r["h_free"]["sign_by"] == r["h_bare"]["sign_by"] == "long_book"
    assert r["h_screen"]["sign"] == 1.0 and r["h_screen"]["sign_locked"] is True and r["h_screen"]["sign_by"] == "locked"


def test_a_lock_must_be_a_real_boolean(monkeypatch, tmp_path):
    w = _lock_world(tmp_path)
    H.stub_propose(monkeypatch)
    for bad in ("false", "true", 1, None):
        ent = {"a_x": {"expr": "neg(LogFloatCap)", "lock": bad}}
        with pytest.raises(SystemExit, match="lock must be true or false"):
            H.run_script(monkeypatch, tmp_path, "sweep.py", ["T001", "--extra", _hypo(tmp_path, ent), "--only-extra"], H.fake_panelset(w))
    assert lock_of("x", "neg(LogFloatCap)") is False and lock_of("x", {"expr": "e"}) is False
    assert lock_of("x", {"expr": "e", "lock": True}) is True and lock_of("x", {"expr": "e", "lock": False}) is False


def test_a_locked_hypothesis_that_is_lost_is_said_so(monkeypatch, tmp_path, capsys):
    w = _lock_world(tmp_path)
    # the same tree as the benchmark: dropped as a duplicate, and the lock with it -- the sweep must not do that silently
    ent = {"a_dup": {"expr": H.KNOWN, "lock": True}, "a_bad": {"expr": "neg(NoSuchField)", "lock": True}}
    _, out = _sweep(monkeypatch, tmp_path, w, ["--extra", _hypo(tmp_path, ent), "--only-extra"])
    text = capsys.readouterr().out
    assert "locked hypothesis a_dup has the same tree as" in text and "locked hypothesis a_bad does not parse" in text
    assert "a_dup" not in out["results"] and "a_bad" not in out["results"]


def test_a_locked_id_that_is_taken_is_said_so(monkeypatch, tmp_path, capsys):
    w = _lock_world(tmp_path)
    ent = {"mem_mean5": {"expr": "neg(LogFloatCap)", "lock": True}}
    _sweep(monkeypatch, tmp_path, w, ["--extra", _hypo(tmp_path, ent), "--max", "4"])        # --max: the warning comes before any scoring
    assert "hypothesis mem_mean5 is locked but its id is already taken" in capsys.readouterr().out


# ------------------------------------------------------------------------------- check_hypo.py keeps accepting
def _check(monkeypatch, tmp_path, entries):
    import runpy
    monkeypatch.setattr(sys, "argv", ["check_hypo.py", _hypo(tmp_path, entries, "chk.yaml")])
    with pytest.raises(SystemExit) as e:
        runpy.run_path(str(H.SCRIPTS / "check_hypo.py"), run_name="__main__")
    return e.value.code


def test_check_hypo_accepts_entries_with_the_lock_key(monkeypatch, tmp_path, capsys):
    ent = {"a_size": {"expr": "neg(LogFloatCap)", "why": "small float cap", "lock": True},
           "a_amt20": {"expr": "cross_mean(day_sum(Amt), 20)", "why": "unlocked", "lock": False},
           "b_x": {"expr": "cross_mean(div(day_sum(Amt), FloatCap), 20)", "why": "no key"},
           "c_y": "cross_mean(day_std(Amt), 10)"}
    code = _check(monkeypatch, tmp_path, ent)
    text = capsys.readouterr().out
    assert code == 0 and "4/4 parse" in text
    assert "OK    a_size  [lock: direction as written]" in text
    assert "OK    a_amt20\n" in text and "OK    b_x\n" in text and "OK    c_y\n" in text      # the old lines, unchanged


def test_check_hypo_rejects_a_lock_that_is_not_a_boolean(monkeypatch, tmp_path, capsys):
    code = _check(monkeypatch, tmp_path, {"a_size": {"expr": "neg(LogFloatCap)", "lock": "true"}})
    text = capsys.readouterr().out
    assert code == 1 and "FAIL  a_size: ValueError: hypothesis a_size: lock must be true or false" in text


# --------------------------------------------------- check_hypo.py and the base / twin / kind keys of the amended rule
def test_check_hypo_accepts_base_twin_and_kind_and_prints_them(monkeypatch, tmp_path, capsys):
    ent = {"x_car": {"expr": "cross_mean(day_sum(Amt), 30)", "kind": "carrier", "lock": True},
           "d_mod": {"expr": "cross_mean(day_sum(Amt), 31)", "base": "x_car", "why": "modification of a carrier of this file"},
           "d_mod_k": {"expr": "cross_mean(day_sum(Amt), 32)", "base": "k_known"},
           "d_mod_kx": {"expr": "cross_mean(day_sum(Amt), 33)", "base": "k_known_xfrozen"},
           "d_mod_v": {"expr": "cross_mean(day_sum(Amt), 34)", "base": "v_base"},
           "c_par": {"expr": "cross_mean(day_sum(Amt), 35)", "twin": "k_known"},
           "c_par2": {"expr": "cross_mean(day_sum(Amt), 36)", "twin": "x_car"},
           "c_par_twin": {"expr": "cross_mean(day_sum(Amt), 37)", "base": "d_mod"}}
    code = _check(monkeypatch, tmp_path, ent)
    text = capsys.readouterr().out
    assert code == 0 and "8/8 parse" in text
    assert "OK    x_car  [lock: direction as written]  [kind: carrier]" in text and "OK    d_mod  [base: x_car]" in text
    assert "OK    c_par  [twin: k_known]" in text and "OK    c_par_twin  [base: d_mod]" in text


@pytest.mark.parametrize("entry,message", [
    ({"expr": "cross_mean(day_sum(Amt), 31)", "base": "nowhere"}, "base 'nowhere' is neither an entry of this file nor one of"),
    ({"expr": "cross_mean(day_sum(Amt), 31)", "twin": "nowhere"}, "twin 'nowhere' is neither an entry of this file nor one of"),
    ({"expr": "cross_mean(day_sum(Amt), 31)", "base": "h_x"}, "base is itself"),
    ({"expr": "cross_mean(day_sum(Amt), 31)", "twin": "h_x"}, "twin is itself"),
    ({"expr": "cross_mean(day_sum(Amt), 31)", "base": 3}, "base must be the id of another object"),
    ({"expr": "cross_mean(day_sum(Amt), 31)", "twin": ""}, "twin must be the id of another object"),
    ({"expr": "cross_mean(day_sum(Amt), 31)", "kind": 7}, "kind must be a non-empty string")])
def test_check_hypo_rejects_a_base_twin_or_kind_that_makes_no_sense(monkeypatch, tmp_path, capsys, entry, message):
    code = _check(monkeypatch, tmp_path, {"h_x": entry})
    text = capsys.readouterr().out
    assert code == 1 and "FAIL  h_x: ValueError" in text and message in text
