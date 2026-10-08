"""Hand-written hypotheses (``studies/<fid>/hypo.yaml``, read by ``scripts/sweep.py --extra`` and checked by
``scripts/check_hypo.py``): ``{id: {expr: "...", why: "...", lock: true}}`` or just ``{id: "expr"}``.

``lock: true`` pins the direction of a hypothesis to the way its expression is written (+1: the high end of the expression
is what is held).  Without it the sweep gives a hypothesis the direction whose pure long book is better on the training
period -- right for a search, wrong for a ruler whose meaning is its direction ("small float cap" must not turn into "large
float cap" because large caps happened to win on the training years).  A root screen (``cs_first_*`` / ``cs_last_*``) is
pinned the same way without being asked.

``base: <id>`` marks a MODIFICATION of another object (a screen, a penalty, "only inside this board"): the study's reading rule
judges it against that carrier (``scripts/group_final.py``), and the sweep carries the key into ``sweep_<tag>.json``.
``twin: <id>`` names the comparison object of a hypothesis whose twin is an existing object (a twin by name needs no key);
``kind: carrier`` marks an object that exists to be some modification's base.
"""

from __future__ import annotations


def lock_of(entry_id: str, entry) -> bool:
    """Is this hypothesis's direction pinned (``lock: true``)?  An entry without the key, or a bare expression string,
    is not.  The value must be a real boolean: a quoted "false" is truthy in Python and would pin the hypothesis."""
    if not isinstance(entry, dict) or "lock" not in entry:
        return False
    lock = entry["lock"]
    if not isinstance(lock, bool):
        raise ValueError(f"hypothesis {entry_id}: lock must be true or false (no quotes), got {lock!r}")
    return lock


def base_of(entry_id: str, entry):
    """The id of the carrier a hypothesis MODIFIES (``base: <id>``), or None for a standalone hypothesis.  A modification (a screen,
    a penalty, "buy only inside this board") is judged against its carrier, not against the known family; the id names another
    object of the sweep -- ``k_known``, ``k_known_xfrozen``, ``v_base``, a ruler, another hypothesis or an ``x_`` carrier.
    Whether that object exists is checked where the whole file (``scripts/check_hypo.py``) or the whole sweep is in view."""
    if not isinstance(entry, dict) or entry.get("base") is None:
        return None
    base = entry["base"]
    if not isinstance(base, str) or not base.strip():
        raise ValueError(f"hypothesis {entry_id}: base must be the id of another object (a non-empty string), got {base!r}")
    if base.strip() == entry_id:
        raise ValueError(f"hypothesis {entry_id}: base is itself")
    return base.strip()


def twin_key_of(entry_id: str, entry):
    """The id an entry names as its comparison object with ``twin: <id>`` (the same structure written without the daily field),
    or None.  The other way to declare a twin is by name: ``<parent>_twin`` is the twin of ``<parent>`` -- no key needed."""
    if not isinstance(entry, dict) or entry.get("twin") is None:
        return None
    twin = entry["twin"]
    if not isinstance(twin, str) or not twin.strip():
        raise ValueError(f"hypothesis {entry_id}: twin must be the id of another object (a non-empty string), got {twin!r}")
    if twin.strip() == entry_id:
        raise ValueError(f"hypothesis {entry_id}: twin is itself")
    return twin.strip()


def kind_of(entry_id: str, entry):
    """The declared kind of an entry (``kind: carrier``: an object that exists to be some modification's base), or None."""
    if not isinstance(entry, dict) or entry.get("kind") is None:
        return None
    kind = entry["kind"]
    if not isinstance(kind, str) or not kind.strip():
        raise ValueError(f"hypothesis {entry_id}: kind must be a non-empty string, got {kind!r}")
    return kind.strip()


BENCHMARK_IDS = ("v_base", "k_known", "k_known_xfrozen")        # always in a sweep, so always valid as a base or a twin


__all__ = ["lock_of", "base_of", "twin_key_of", "kind_of", "BENCHMARK_IDS"]
