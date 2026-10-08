"""The synthetic K002 world shared by the group_final tests: the rulers of the reading rule, standalone and modification
hypotheses with a designed correlation structure, twins and a carrier, and the sweep that scores them (the REAL
scripts/sweep.py, --only-extra, with `lock:` and `base:` keys in the hypotheses file)."""
import json
import sys
from pathlib import Path

import numpy as np
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import k002_helpers as H  # noqa: E402

KNOWN = H.KNOWN
KNOWN_NEG = f"neg({KNOWN})"
R_EXPR = {      # the rulers of the amended rule (README, 现行规则), with the K002 expressions
    "a_size": "neg(LogFloatCap)",
    "a_tsize": "neg(LogTotalCap)",
    "a_turn20": "cross_mean(div(day_sum(Amt), FloatCap), 20)",
    "a_amt20": "cross_mean(day_sum(Amt), 20)",
    "a_known_in_size": f"cs_bucket_rank({KNOWN_NEG}, LogFloatCap)",
    "a_size_in_known": f"cs_bucket_rank(neg(LogFloatCap), {KNOWN})",
    "a_known_in_turn": f"cs_bucket_rank({KNOWN_NEG}, cross_mean(div(day_sum(Amt), FloatCap), 20))",
    "a_size_plus_known": f"add(cs_rank(neg(LogFloatCap)), cs_rank({KNOWN_NEG}))",
    "e_main_only": f"cs_first_high40({KNOWN_NEG}, LimitWidth)",
    "e_wide_only": f"cs_first_low40({KNOWN_NEG}, LimitWidth)",
    "e_xage1y": f"cs_last_high20({KNOWN_NEG}, neg(ListAge))",
}
RULER_BASES = {"e_main_only": "k_known", "e_wide_only": "k_known_xfrozen", "e_xage1y": "k_known"}          # in the real file all three are k_known
A_LOCKED = ("a_size", "a_tsize", "a_known_in_size", "a_size_in_known", "a_known_in_turn", "a_size_plus_known")      # README: six rulers pinned
H_EXPR = {      # the hypotheses: id -> expression (the panels are set in build())
    "b_strong": "cross_mean(day_std(Amt), 31)", "b_dup": "cross_mean(day_std(Amt), 32)", "b_alt": "cross_mean(day_std(Amt), 33)",
    "b_lowcov": "cross_mean(day_std(Amt), 34)", "b_coarse": "cross_mean(day_std(Amt), 35)", "b_wrong": "cross_mean(day_std(Amt), 36)",
    "b_alt_twin": "cross_mean(day_std(Amt), 37)",
    "c_solo": "cross_mean(day_std(Amt), 41)", "c_solo_twin": "cross_mean(day_std(Amt), 42)",
    "c_mod": "cross_mean(day_std(Amt), 43)",
    "d_one": "cross_mean(day_sum(Amt), 31)", "d_two": "cross_mean(day_sum(Amt), 32)",
    "d_pen1": "cross_mean(day_sum(Amt), 33)", "d_pen1_twin": "cross_mean(day_sum(Amt), 34)", "d_pen2": "cross_mean(day_sum(Amt), 35)",
    "d_pen3": "cross_mean(day_sum(Amt), 36)", "d_noop": "cross_mean(day_sum(Amt), 37)", "d_bad": "cross_mean(day_sum(Amt), 38)",
    "e_lowcov": "cross_mean(day_sum(Amt), 41)", "e_screen": "cross_mean(day_sum(Amt), 42)", "e_screen_twin": "cross_mean(day_sum(Amt), 43)",
    "x_car": "cross_mean(day_std(Amt), 25)", "x_car2": "cross_mean(day_std(Amt), 26)",
}
TWIN_KEYS = {"b_dup": "k_known", "d_one": "d_two"}          # the explicit way to declare a twin (the by-name way needs no key): an existing object / another hypothesis
CARRIERS = ("x_car", "x_car2")
BASES = {"x_car": "x_car2", "c_mod": "k_known", "d_pen1": "a_known_in_size", "d_pen1_twin": "a_known_in_size", "d_pen2": "a_known_in_size", "d_pen3": "x_car",
         "d_noop": "a_known_in_size", "d_bad": "a_known_in_size", "e_screen": "k_known", "e_screen_twin": "k_known"}
H_LOCKED = ("b_wrong", "d_pen1", "d_pen1_twin", "d_pen2", "d_pen3", "d_noop", "d_bad", "c_mod", "e_screen", "e_screen_twin")


def build(n_days=320, n_names=50, seed=11):
    """-> (world, hypo entries).  Designed so that: b_dup is a near copy of b_strong, b_alt a different signal (and b_strong looks
    like small cap, b_alt does not); b_lowcov fails the coverage gate, b_coarse is a coarse copy of b_strong, b_wrong (locked at
    +1 although the label leans the other way) the long-leg gate; c_mod improves k_known with x2; d_pen1 / d_pen2 improve
    a_known_in_size with x2 (d_pen2 a near copy of d_pen1), d_pen3 improves x_car with x3, d_noop is a_known_in_size again (a
    no-op), d_bad makes it worse; e_screen improves k_known with x3; e_lowcov leaves standalone E with nobody."""
    w = H.World(n_days=n_days, n_names=n_names, seed=seed)
    x, x2, x3, nz = w.x, w.x2, w.x3, w.noise
    n_k, n_ki, n_xc = nz(), nz(), nz()
    w.set(KNOWN, -(0.8 * x + 0.6 * n_k))
    w.set(H.XFROZEN, -(0.7 * x + 0.7 * nz()))                  # a root screen is pinned at +1 by the sweep although the label leans on its opposite
    ki_s = 0.8 * x + 0.6 * n_ki
    x_car = 0.9 * x + 0.5 * n_xc
    x_car2 = 0.7 * x + 0.7 * nz()
    r_panel = {"a_size": x + 0.5 * nz(), "a_tsize": -(0.9 * x + 0.5 * nz()), "a_turn20": -(0.6 * x + 0.8 * nz()), "a_amt20": 0.3 * x + nz(),
               "a_known_in_size": ki_s, "a_size_in_known": nz(), "a_known_in_turn": 0.5 * x + nz(), "a_size_plus_known": 0.6 * x + 0.8 * nz(),
               "e_main_only": 0.5 * x + 0.9 * nz(), "e_wide_only": 0.4 * x + nz(), "e_xage1y": 0.6 * x + 0.8 * nz()}
    for k, e in R_EXPR.items():
        w.set(e, r_panel[k])
    strong = x + 0.2 * nz()
    sparse = x + 0.2 * nz()
    sparse[w.rng.random(sparse.shape) < 0.7] = np.nan                       # 70 % of the cells missing: coverage ~0.3
    d_one = x2 + 0.3 * nz()
    d_pen1 = ki_s + 0.9 * x2
    h_panel = {"b_strong": strong, "b_dup": strong + 0.05 * nz(), "b_alt": x2 + 0.3 * nz(), "b_lowcov": sparse, "b_coarse": np.round(x / 1.5), "b_wrong": -(x + 0.2 * nz()),
               "b_alt_twin": 0.5 * x2 + nz(),
               "c_solo": x3 + 0.3 * nz(), "c_solo_twin": 0.4 * x3 + nz(), "c_mod": 0.8 * x + 0.6 * n_k + 0.9 * x2,
               "d_one": d_one, "d_two": d_one + 0.1 * nz(),
               "d_pen1": d_pen1, "d_pen1_twin": ki_s + 0.3 * x2, "d_pen2": d_pen1 + 0.05 * nz(), "d_pen3": x_car + 0.9 * x3, "d_noop": ki_s.copy(), "d_bad": ki_s - 0.9 * x2,
               "e_lowcov": sparse.copy(), "e_screen": 0.8 * x + 0.6 * n_k + 0.9 * x3, "e_screen_twin": 0.8 * x + 0.6 * n_k + 0.3 * x3,
               "x_car": x_car, "x_car2": x_car2}
    for k, e in H_EXPR.items():
        w.set(e, h_panel[k])
    entries = {}
    for k, e in R_EXPR.items():
        entries[k] = {"expr": e, "why": f"ruler {k}", **({"lock": True} if k in A_LOCKED else {}), **({"base": RULER_BASES[k]} if k in RULER_BASES else {})}
    for k, e in H_EXPR.items():
        entries[k] = {"expr": e, "why": f"hypothesis {k}", **({"lock": True} if k in H_LOCKED else {}), **({"base": BASES[k]} if k in BASES else {}),
                      **({"twin": TWIN_KEYS[k]} if k in TWIN_KEYS else {}), **({"kind": "carrier"} if k in CARRIERS else {})}
    return w, entries


def sweep(monkeypatch, root, w, entries, fid="T001", tag="s1", max_=None):
    """Run scripts/sweep.py --only-extra on the world; -> the sweep JSON as a dict."""
    H.write_config(root, fid, w)
    hy = root / "hypo.yaml"
    hy.write_text(yaml.safe_dump(entries, allow_unicode=True, sort_keys=False), encoding="utf-8")
    H.stub_propose(monkeypatch)
    H.run_script(monkeypatch, root, "sweep.py", [fid, "--tag", tag, "--extra", str(hy), "--only-extra"] + (["--max", str(max_)] if max_ else []), H.fake_panelset(w))
    return json.loads((root / "runs" / fid / f"sweep_{tag}.json").read_text(encoding="utf-8"))
