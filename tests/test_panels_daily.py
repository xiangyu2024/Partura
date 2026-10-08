"""K002 tooling, part A: panels that know about the daily store.

* ``PanelSet(daily_root=...)`` and the per-EXPRESSION cache identity: an expression without a ``DF:`` leaf keeps the
  daily-free cache file when a daily store is attached (the shared cache holds hundreds of GB of such panels), an expression
  with one gets the daily-aware key;
* the study config's ``daily_fields`` key and ``$PARTURA_STORE`` / ``$PARTURA_MIRROR`` reach ``PanelSet`` from every script
  that builds one from a config (sweep.py, sweep_final.py, anatomy.py, group_final.py).
"""
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import k002_helpers as H  # noqa: E402

from partura.panels import (DEFAULT_MIRROR, DEFAULT_STORE, PanelSet, config_daily_root, default_mirror, default_store,  # noqa: E402
                            parse_research, uses_daily_leaf)

from alphacube.synthetic import write_daily_fields, write_synthetic_store  # noqa: E402


@pytest.fixture(autouse=True)
def _restore_splits():
    from partura.splits import SPLITS
    saved = dict(SPLITS)
    yield
    SPLITS.clear()
    SPLITS.update(saved)


@pytest.fixture(autouse=True)
def _no_ambient_daily_store(monkeypatch):
    monkeypatch.delenv("ALPHACUBE_DAILY_FIELDS", raising=False)


def _store(tmp_path):
    return write_synthetic_store(tmp_path / "cube", n_symbols=12, n_days=70, n_minutes=8, seed=5)


def _daily(tmp_path, store, name="daily", fields=("FloatCap",), scale=1.0):
    cap = scale * (1e9 * (np.arange(store.n_symbols, dtype=np.float64)[:, None] + 1.0) + 1e6 * np.arange(store.n_days, dtype=np.float64)[None, :])
    return write_daily_fields(tmp_path / name, {f: cap for f in fields}, store.symbols, store.dates)


def _ps(store, cache, **kw):
    return PanelSet(str(store.directory), store.dates[0], store.dates[-1], warmup=0, device="cpu", cache_dir=str(cache), quiet=True, **kw)


# ------------------------------------------------------------------------------------------- the key test
@pytest.mark.parametrize("key,expected", [
    ("DF:LogFloatCap", True),
    ("O:neg(DF:LogFloatCap)", True),
    ("O:cs_bucket_rank(O:neg(O:cross_mean(O:day_std(F:Amt))|w30),DF:LogFloatCap)", True),
    ("O:add(C:1.0,DF:FloatCap)", True),
    ("G:in_slice(DF:FloatCap,L:10,L:229)", True),
    ("G:foo([DF:FloatCap,F:Close],L:3)", True),
    ("O:cross_mean(O:day_std(F:Amt))|w30", False),
    ("F:Amt", False),
    ("C:5.0", False),
    ("__label__|open_vwap15|h1|buyable1", False),
    ("O:cs_last_high20(O:neg(O:cross_mean(O:day_std(F:Amt))|w30),O:cross_max(O:day_zero_ratio(F:Ret))|w15)", False),
    ("O:fooDF(F:ADF)", False),                 # names that merely end in "DF" are not daily leaves
    ("O:x(F:fooDF:bar)", False),
])
def test_uses_daily_leaf_reads_the_df_tag_of_a_key(key, expected):
    assert uses_daily_leaf(key) is expected


def test_real_parsed_keys_of_the_k002_expressions():
    assert uses_daily_leaf(parse_research("neg(LogFloatCap)").key())
    assert uses_daily_leaf(parse_research("cs_bucket_rank(neg(cross_mean(day_std(Amt), 30)), LogFloatCap)").key())
    assert uses_daily_leaf(parse_research("ListAge").key())
    assert not uses_daily_leaf(parse_research("cross_mean(day_std(Amt), 30)").key())
    assert not uses_daily_leaf(parse_research("cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Ret), 15))").key())


# ------------------------------------------------------------------------------------- the cache identity
def test_with_no_daily_store_every_cache_key_is_what_it_was_on_main(tmp_path):
    store = _store(tmp_path)
    ps = _ps(store, tmp_path / "cache")
    assert ps.store.daily is None and ps.daily_root is None
    raw = f"{ps.store_path}|{ps.start}|{ps.end}|{len(ps.symbols)}|{ps.dates[0]}|{ps.dates[-1]}"
    main_view_id = hashlib.sha1(raw.encode()).hexdigest()[:10]
    assert ps.view_id == ps.plain_view_id == main_view_id
    for key in ("O:cross_mean(O:day_std(F:Amt))|w30", "O:neg(DF:LogFloatCap)", "DF:ListAge", "__label__|open_vwap15|h1|buyable1"):
        main_name = hashlib.sha1(f"{main_view_id}|{key}".encode()).hexdigest()[:16] + ".npy"
        assert ps._cache_path(key).name == main_name        # also for a DF key: nothing is attached, nothing moves


def test_a_non_daily_expression_resolves_to_the_same_cache_file_with_and_without_a_daily_store(tmp_path):
    store = _store(tmp_path)
    cache = tmp_path / "cache"
    plain = _ps(store, cache)
    with_daily = _ps(store, cache, daily_root=str(_daily(tmp_path, store)))
    assert plain.store.daily is None and with_daily.store.daily is not None
    assert with_daily.view_id != plain.view_id              # the view as a whole is another one ...
    assert with_daily.plain_view_id == plain.view_id
    src = "cross_mean(day_std(Amt), 5)"
    key = parse_research(src).key()
    assert with_daily._cache_path(key) == plain._cache_path(key)        # ... this expression's file is not
    # the label has no leaf at all
    tag = "__label__|open_vwap15|h1|buyable0"
    assert with_daily._cache_path(tag) == plain._cache_path(tag)
    # and it really is shared: computed by one view, served to the other without evaluating anything
    a = plain.compute({"x": src})["x"]
    files = sorted(p.name for p in cache.glob("*"))
    boom = AssertionError("a cache hit must not evaluate")

    def refuse(*args, **kw):
        raise boom
    with_daily._evaluate = refuse
    b = with_daily.compute({"x": src})["x"]
    assert np.array_equal(a, b, equal_nan=True)
    assert sorted(p.name for p in cache.glob("*")) == files             # nothing duplicated, nothing orphaned
    # and the other way round: the daily view writes it first, the plain one reads it
    cache2 = tmp_path / "cache2"
    first = _ps(store, cache2, daily_root=str(_daily(tmp_path, store, "daily2")))
    first.compute({"x": src})
    second = _ps(store, cache2)
    second._evaluate = refuse
    assert np.array_equal(second.compute({"x": src})["x"], a, equal_nan=True)


def test_an_expression_with_a_daily_leaf_gets_the_daily_aware_key(tmp_path):
    store = _store(tmp_path)
    cache = tmp_path / "cache"
    plain = _ps(store, cache)
    a = _ps(store, cache, daily_root=str(_daily(tmp_path, store, "daily_a")))
    b = _ps(store, cache, daily_root=str(_daily(tmp_path, store, "daily_b", fields=("FloatCap", "TotalCap"))))
    src = "div(day_sum(Amt), FloatCap)"
    key = parse_research(src).key()
    assert uses_daily_leaf(key)
    assert a._cache_path(key) != plain._cache_path(key)
    assert a._cache_path(key).name == hashlib.sha1(f"{a.view_id}|{key}".encode()).hexdigest()[:16] + ".npy"
    assert b._cache_path(key) != a._cache_path(key)                    # a rebuilt daily directory is never served a stale panel
    # stable: the same store opened twice is the same file
    assert _ps(store, cache, daily_root=str(a.daily_root))._cache_path(key) == a._cache_path(key)
    # the daily-aware panel is computed from the store, written under the daily-aware name, and the plain view cannot read it
    arr = a.compute({"x": src})["x"]
    assert a._cache_path(key).is_file() and not plain._cache_path(key).is_file()
    assert np.isfinite(arr).any()
    again = _ps(store, cache, daily_root=str(a.daily_root))
    again._evaluate = lambda *args, **kw: (_ for _ in ()).throw(AssertionError("must be a cache hit"))
    assert np.array_equal(again.compute({"x": src})["x"], arr, equal_nan=True)


def test_the_manifest_beside_a_panel_records_the_id_its_key_was_built_from(tmp_path):
    store = _store(tmp_path)
    cache = tmp_path / "cache"
    ps = _ps(store, cache, daily_root=str(_daily(tmp_path, store)))
    ps.compute({"plain": "cross_mean(day_std(Amt), 5)", "daily": "div(day_sum(Amt), FloatCap)"})
    for name, want in (("plain", ps.plain_view_id), ("daily", ps.view_id)):
        key = parse_research({"plain": "cross_mean(day_std(Amt), 5)", "daily": "div(day_sum(Amt), FloatCap)"}[name]).key()
        meta = json.loads(ps._cache_path(key).with_suffix(".json").read_text(encoding="utf-8"))
        assert meta["key"] == key and meta["view_id"] == want and meta["name"] == name
    assert ps.plain_view_id != ps.view_id


def test_the_label_is_cached_under_the_daily_free_name(tmp_path):
    store = _store(tmp_path)
    cache = tmp_path / "cache"
    plain = _ps(store, cache, label_kind="close")
    t1 = plain.target(1)
    n_files = len(list(cache.glob("*.npy")))
    with_daily = _ps(store, cache, label_kind="close", daily_root=str(_daily(tmp_path, store)))
    t2 = with_daily.target(1)
    assert np.array_equal(t1, t2, equal_nan=True)
    assert len(list(cache.glob("*.npy"))) == n_files                  # served from the plain file, no second copy


# ------------------------------------------------------------------------- daily_root reaches the store
def test_daily_root_is_passed_to_open_cube_store_and_none_keeps_the_environment_default(tmp_path, monkeypatch):
    store = _store(tmp_path)
    root = _daily(tmp_path, store)
    assert _ps(store, None).store.daily is None
    ps = _ps(store, None, daily_root=str(root))
    assert ps.store.daily is not None and Path(ps.store.daily.root) == Path(root) and ps.daily_root == str(root)
    # unchanged behaviour: with daily_root=None the environment variable still attaches a store
    monkeypatch.setenv("ALPHACUBE_DAILY_FIELDS", str(root))
    assert _ps(store, None).store.daily is not None
    # and an explicit argument beats the environment
    other = _daily(tmp_path, store, "other", fields=("FloatCap", "TotalCap"))
    assert Path(_ps(store, None, daily_root=str(other)).store.daily.root) == Path(other)


def test_default_store_mirror_and_the_configs_daily_key(monkeypatch):
    monkeypatch.delenv("PARTURA_STORE", raising=False)
    monkeypatch.delenv("PARTURA_MIRROR", raising=False)
    assert default_store() == DEFAULT_STORE == "/root/autodl-tmp/qmt_daily_data/fast_factor_compute"
    assert default_mirror() == DEFAULT_MIRROR == "/root/autodl-tmp/AlphaCube/mirror"
    monkeypatch.setenv("PARTURA_STORE", "/tmp/cube")
    monkeypatch.setenv("PARTURA_MIRROR", "/tmp/mirror")
    assert default_store() == "/tmp/cube" and default_mirror() == "/tmp/mirror"
    monkeypatch.setenv("PARTURA_STORE", "")
    assert default_store() == DEFAULT_STORE                                # an empty variable is no variable
    assert config_daily_root({"daily_fields": "/x/daily"}) == "/x/daily"
    assert config_daily_root({}) is None and config_daily_root({"daily_fields": None}) is None and config_daily_root({"daily_fields": ""}) is None
    assert config_daily_root(None) is None


def test_the_k002_config_names_the_daily_store_and_k001_does_not():
    import yaml
    root = Path(__file__).resolve().parents[1]
    k2 = yaml.safe_load((root / "configs" / "K002_daily_fields.yaml").read_text(encoding="utf-8"))
    k1 = yaml.safe_load((root / "configs" / "K001_known_screens.yaml").read_text(encoding="utf-8"))
    assert k2["factor_id"] == "K002_daily_fields" and k2["daily_fields"] == "/root/autodl-tmp/Partura/daily_fields"
    assert "daily_fields" not in k1
    for key in ("expression", "label", "cost_per_side", "top_frac", "rank_by", "warmup", "splits", "gates", "controls", "fit_split", "user_split"):
        assert k2[key] == k1[key], key
    assert k2["stages"] == [] and "corr_ids" not in k2 and "diagnostics" not in k2


# ------------------------------------------------------------- every script that builds a PanelSet from a config
def _gf():
    spec = importlib.util.spec_from_file_location("group_final_under_test", H.SCRIPTS / "group_final.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _prepare(tmp_path, with_key):
    w = H.World(n_days=140, n_names=20)
    H.write_config(tmp_path, "T001", w, extra={"daily_fields": "/x/daily"} if with_key else None)
    (tmp_path / "runs" / "T001").mkdir(parents=True)
    # the minimum the scripts read before they build their PanelSet: no variants, nothing to pick
    (tmp_path / "runs" / "T001" / "sweep_s1.json").write_text(json.dumps({"results": {}}), encoding="utf-8")
    return w


@pytest.mark.parametrize("script", ["sweep.py", "sweep_final.py", "anatomy.py"])
@pytest.mark.parametrize("with_key", [True, False])
def test_scripts_hand_the_configs_daily_fields_and_the_env_paths_to_panelset(script, with_key, tmp_path, monkeypatch):
    w = _prepare(tmp_path, with_key)
    H.stub_propose(monkeypatch)
    monkeypatch.setenv("PARTURA_STORE", "/laptop/cube")
    monkeypatch.setenv("PARTURA_MIRROR", "/laptop/mirror")
    calls = []
    with pytest.raises(H.Stop) as stop:
        H.run_script(monkeypatch, tmp_path, script, ["T001"], H.fake_panelset(w, calls, stop_at_init=True))
    kw = stop.value.args[0]
    assert kw["daily_root"] == ("/x/daily" if with_key else None)
    assert kw["store_path"] == "/laptop/cube" and kw["mirror_root"] == "/laptop/mirror"
    assert kw["device"] == "cuda"                                         # untouched: the scripts' defaults stay the server's


@pytest.mark.parametrize("script", ["sweep.py", "sweep_final.py", "anatomy.py"])
def test_scripts_default_to_the_servers_paths_without_the_env(script, tmp_path, monkeypatch):
    w = _prepare(tmp_path, False)
    H.stub_propose(monkeypatch)
    monkeypatch.delenv("PARTURA_STORE", raising=False)
    monkeypatch.delenv("PARTURA_MIRROR", raising=False)
    with pytest.raises(H.Stop) as stop:
        H.run_script(monkeypatch, tmp_path, script, ["T001"], H.fake_panelset(w, stop_at_init=True))
    kw = stop.value.args[0]
    assert kw["store_path"] == "/root/autodl-tmp/qmt_daily_data/fast_factor_compute" and kw["mirror_root"] == "/root/autodl-tmp/AlphaCube/mirror"
    assert kw["daily_root"] is None


@pytest.mark.parametrize("with_key", [True, False])
def test_group_final_hands_the_configs_daily_fields_and_the_env_paths_to_panelset(with_key, tmp_path, monkeypatch):
    gf = _gf()
    w = _prepare(tmp_path, with_key)
    # a sweep with just the rulers, so that make_plan is satisfied
    row = {"kind": "bench", "sign": 1.0, "expr": "x", "cov": 1.0, "dist": 1.0, "hl_long_u": 5.0}
    (tmp_path / "runs" / "T001" / "sweep_s1.json").write_text(json.dumps({"results": {k: row for k in gf.DEFAULT_RULERS}}), encoding="utf-8")
    monkeypatch.setenv("PARTURA_STORE", "/laptop/cube")
    monkeypatch.setenv("PARTURA_MIRROR", "/laptop/mirror")
    monkeypatch.setenv("PARTURA_LOCK_DIR", str(tmp_path / "locks"))
    monkeypatch.setattr(gf, "PARTURA_ROOT", tmp_path)
    monkeypatch.setattr(gf, "PanelSet", H.fake_panelset(w, stop_at_init=True))
    with pytest.raises(H.Stop) as stop:
        gf.main(["T001", "--end", w.dates[-1], "--dry-run", "--pair", "k_known"])
    kw = stop.value.args[0]
    assert kw["daily_root"] == ("/x/daily" if with_key else None)
    assert kw["store_path"] == "/laptop/cube" and kw["mirror_root"] == "/laptop/mirror"
