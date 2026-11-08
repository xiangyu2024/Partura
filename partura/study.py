"""Which study a script belongs to, where its files live, and whose behaviour it follows.

The C05-C08 scripts switched on ``$PARTURA_C0X`` ("C05" .. "C08", unset = the script's own default) and wrote under
``research/coldstart_<C0X>``.  Every such switch now goes through this module, so that a production study (``PROD``,
research/prod_W01) is one more row in one table instead of a new string literal in every script.

Rules (the history is not touched):

* A legacy study (C05-C08) resolves exactly as before: directory ``coldstart_<C0X>`` -- ``$PARTURA_STUDY_DIR`` is NOT read for
  it (the scripts never read it for these studies) -- and the same prefixes / switches the scripts spelled out inline.
* ``PROD`` takes its directory from ``$PARTURA_STUDY_DIR`` (required; ``prod_W01`` for wave 1), runs its own main AlphaCube
  (episodes ``prods<seed>M<batch>``), its Partura missions are named ``prods<seed>Pr<round><a|b>``, and everywhere else it
  behaves as C08's P arm (:data:`FOLLOWS`).  The one place where it is *not* C08-as-it-ran is R accessions, see
  :func:`r_additions`.

Pure stdlib: importable on the laptop, on the servers and in the tests without the engine.
"""
from __future__ import annotations

import os
from typing import Dict, Mapping, Optional

LEGACY = ("C05", "C06", "C07", "C08")                  # the studies whose scripts predate this module
FOLLOWS = {"PROD": "C08"}                              # whose behaviour a non-legacy study copies at every switch
# whose main AlphaCube (M) a study reads: C06 reuses C05's, C08 reuses C07's, PROD runs its own (prefix = its own, see m_prefix)
_M_PREFIX = {"C05": "c05", "C06": "c05", "C07": "c07", "C08": "c07"}


def name(default: str = "C05", env: Optional[Mapping[str, str]] = None) -> str:
    """The study ($PARTURA_C0X); ``default`` is the script's own default (C05 for the server tools, C06 for the laptop check)."""
    env = os.environ if env is None else env
    return env.get("PARTURA_C0X") or default


def follows(study: str) -> str:
    """The legacy study whose behaviour ``study`` copies (itself for a legacy study)."""
    return FOLLOWS.get(study, study)


def is_legacy(study: str) -> bool:
    return study in LEGACY


def dirname(study: str, env: Optional[Mapping[str, str]] = None) -> str:
    """The study's directory under research/: ``coldstart_<C0X>`` for a legacy study, ``$PARTURA_STUDY_DIR`` otherwise."""
    if is_legacy(study):
        return f"coldstart_{study}"
    env = os.environ if env is None else env
    d = env.get("PARTURA_STUDY_DIR")
    if not d:
        raise SystemExit(f"study {study}: set PARTURA_STUDY_DIR (the directory under research/), e.g. prod_W01")
    if "/" in d or d.startswith("."):
        raise SystemExit(f"PARTURA_STUDY_DIR must be a plain directory name under research/, got {d!r}")
    return d


def prefix(study: str) -> str:
    """Prefix of the study's own episode tags: C08 -> c08 (c08s801Pr1a), PROD -> prod (prods901Pr1a)."""
    return study.lower()


def m_prefix(study: str) -> str:
    """Prefix of the main AlphaCube episodes the study reads (``<prefix>s<seed>M<batch>_I0_open_search``)."""
    return _M_PREFIX.get(study) or prefix(study)


def neutral_extra(study: str) -> bool:
    """C05 only: an E mission's reward adds the core's family to the controls (C06 PLAN 2.3 removed it; C08 and PROD never had it)."""
    return study == "C05"


def r_additions(study: str, env: Optional[Mapping[str, str]] = None) -> bool:
    """Does the R direct evaluation take a better-but-different variant in as a head of its own ("accession")?

    Legacy: ``study == "C06"`` -- literally what c05_locate.py did.  NB that is *only* C06: C08's PLAN and rules.md describe
    accessions, but the code gate never opened for C08, so C08 ran with replacements only (its final.json has no "R+" head).
    PROD follows its PLAN / rules.md (accessions on); ``$PARTURA_R_ADDITIONS=0`` switches them off, i.e. C08-as-it-ran.
    """
    if is_legacy(study):
        return study == "C06"
    env = os.environ if env is None else env
    return env.get("PARTURA_R_ADDITIONS", "1") != "0"


def ctrl_strike_default(study: str) -> str:
    """Default of $C06_CTRL_STRIKE in c06_check.py: a seed is struck when its |rho| with a control reaches this.
    Legacy default 0.5 (C08 passed 0.8 in the environment); PROD follows C08's permissive audit: 0.8 by default."""
    return "0.5" if is_legacy(study) else "0.8"


def scheduling_env(env: Optional[Mapping[str, str]] = None) -> bool:
    """idea_search.py: apply the C05 scheduling settings (4 run slots, 2 GPU ways, GPU re-promotion, panel cache <= 24 GB)?
    Scheduling only, no numbers.  True for the research directories coldstart_C05 / C06 / C07 (as before; C08 is not on the
    list) and for PROD, whose main AlphaCube is C07's M run again."""
    env = os.environ if env is None else env
    return env.get("PARTURA_STUDY_DIR") in ("coldstart_C05", "coldstart_C06", "coldstart_C07") or env.get("PARTURA_C0X") == "PROD"


def host_caps(env: Optional[Mapping[str, str]] = None) -> Dict[str, str]:
    """The C05 scheduling numbers (4 run slots, 2 GPU ways, a panel cache of at most 24 GB), with a host's own override.
    Scheduling only, no numbers: the slots and the GPU ways decide what waits, the in-memory panel cache only saves
    recomputation.  A host with more memory than the first server (the second server: 1 TB) sets $PARTURA_HOST_SLOTS /
    $PARTURA_HOST_GPU_WAYS / $PARTURA_HOST_PANEL_CACHE_GB in its own tmp/ env; unset = exactly the old values.  The
    panel cache is still min(cap, $PARTURA_PANEL_CACHE_GB or 6), as before."""
    env = os.environ if env is None else env
    cap = float(env.get("PARTURA_HOST_PANEL_CACHE_GB") or 24.0)
    return {"PARTURA_SLOTS": env.get("PARTURA_HOST_SLOTS") or "4", "PARTURA_GPU_WAYS": env.get("PARTURA_HOST_GPU_WAYS") or "2",
            "PARTURA_PANEL_CACHE_GB": str(min(cap, float(env.get("PARTURA_PANEL_CACHE_GB", 6))))}


__all__ = ["LEGACY", "FOLLOWS", "name", "follows", "is_legacy", "dirname", "prefix", "m_prefix", "neutral_extra", "r_additions",
           "ctrl_strike_default", "scheduling_env", "host_caps"]
