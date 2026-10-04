"""Small read-only helpers a study runs ON THE SERVER (through scripts/study.sh).

The server's AlphaCube checkout is the source of truth for what an operator
does -- the local copy may be a different commit with uncommitted edits -- so
"what operators exist", "what is this kernel's source" and "does this
expression parse" are always asked there.

    python -m partura.remote_tools ops '<regex>'
    python -m partura.remote_tools src <operator> [...]
    python -m partura.remote_tools check <factor_id>
    python -m partura.remote_tools propose <factor_id>
"""

from __future__ import annotations

import inspect
import re
import sys

import yaml

from .bridge import PARTURA_ROOT, ensure_alphacube_on_path

ensure_alphacube_on_path()


def _catalogs():
    from alphacube.catalog import default_registry
    from alphacube.fullcatalog import default_full_catalog
    return default_registry(), default_full_catalog()


def ops(pattern: str = ".") -> int:
    reg, cat = _catalogs()
    pat = re.compile(pattern)
    print("# 搜索语法内的注册表算子(带 win 的需要窗口参数,写在最后一个位置):")
    for n, sp in sorted(reg._ops.items()):
        if not pat.search(n):
            continue
        flags = ",".join(k for k in ("lookahead", "boolean_output", "trivial_boolean", "resource_risk",
                                     "coarse_output") if getattr(sp, k))
        win = f" win {list(sp.windows)}" if sp.requires_window else ""
        print(f"  {n:<34} {sp.face}/{sp.family}/{sp.category:<12} arity {sp.arity} axis {sp.compute_axis}{win}"
              f"{'  [' + flags + ']' if flags else ''}")
    print("# 只在完整库里的通用调用(手写因子用的;参数含字面量,签名看 src):")
    for n, sp in sorted(cat.entries.items()):
        if pat.search(n) and n not in reg._ops:
            print(f"  {n:<34} {sp.face}/{sp.family}  axis {sp.compute_axis} reduces_m {sp.reduces_m}")
    return 0


def src(names) -> int:
    reg, cat = _catalogs()
    for name in names:
        spec = reg._ops.get(name) or cat.get(name)
        if spec is None:
            print(f"### {name}: not found (ambiguous in the full catalog: {name in cat.ambiguous})")
            continue
        fn = inspect.unwrap(spec.fn)
        try:
            f, (lines, line) = inspect.getsourcefile(fn), inspect.getsourcelines(fn)
            print(f"### {name}  face={spec.face} family={spec.family} category={spec.category} "
                  f"axis={spec.compute_axis} reduces_m={spec.reduces_m} lookahead={spec.lookahead} "
                  f"kernel={spec.kernel_id}\n# {f}:{line}")
            print("".join(lines))
        except (OSError, TypeError) as exc:
            print(f"### {name}: {spec.kernel_id}: source unavailable ({exc})")
            lines = []
        # A baked variant (nt_ts_autocorr_s1, pow_3, cross_quantile_q25) or an nt_ twin is a
        # one-line wrapper: what it DOES is in the kernel the registry names, and in the
        # module-level helpers that kernel calls.
        _show_kernel(spec, name, shown="".join(lines))
    return 0


def _show_kernel(spec, name: str, shown: str = "", depth: int = 2) -> None:
    import importlib
    mod_name, _, fn_name = str(spec.kernel_id).partition(".")
    try:
        mod = importlib.import_module(f"alphacube.operators.{mod_name}")
    except ImportError:
        return
    seen = set()

    def emit(obj, why: str, level: int) -> None:
        if not inspect.isfunction(obj) or obj in seen:
            return
        seen.add(obj)
        try:
            src = inspect.getsource(inspect.unwrap(obj))
        except (OSError, TypeError):
            return
        if src.strip() and src.strip() not in shown:
            print(f"# --- {why}: {obj.__module__.split('.')[-1]}.{obj.__name__}")
            print(src)
        if level <= 0:
            return
        g = getattr(inspect.unwrap(obj), "__globals__", {})
        for called in sorted(set(re.findall(r"\b([A-Za-z_][A-Za-z0-9_]*)\(", src))):
            h = g.get(called)
            if called in ("op", "deco"):                 # the registration decorator, not part of the maths
                continue
            if inspect.isfunction(h) and h.__module__.startswith("alphacube.operators") and h is not obj:
                emit(h, f"{obj.__name__} 调用的", level - 1)

    base = getattr(mod, fn_name, None)
    if base is not None:
        emit(base, f"{name} 背后的内核", depth)


def _config(fid: str) -> dict:
    return yaml.safe_load((PARTURA_ROOT / "configs" / f"{fid}.yaml").read_text(encoding="utf-8"))


def check(fid: str) -> int:
    from alphacube.expression import contains_lookahead, is_valid_root
    from .panels import parse_research
    cfg = _config(fid)
    items = {**(cfg.get("controls") or {}), **(cfg.get("gates") or {})}
    ids = set()
    bad = 0
    for st in cfg["stages"]:
        for v in st["variants"]:
            if v["id"] in ids:
                bad += 1
                print(f"DUPLICATE id {v['id']} (stage {st['id']}) — a later one silently replaces the earlier")
            ids.add(v["id"])
            items[f"{st['id']}/{v['id']}"] = v["expr"]
    keys = {}
    for k, s in items.items():
        try:
            e = parse_research(s)
        except Exception as exc:
            bad += 1
            print(f"PARSE FAIL {k}: {type(exc).__name__}: {str(exc)[:220]}")
            continue
        notes = []
        if not is_valid_root(e):
            notes.append("NOT A VALID ROOT (must be one value per stock-day and not boolean)")
        if contains_lookahead(e):
            notes.append("contains a LOOKAHEAD operator")
        if notes:
            bad += 1
            print(f"PROBLEM {k}: " + "; ".join(notes))
        if e.key() in keys and "/" in k and "/" in keys[e.key()]:
            print(f"note: {k} is the same tree as {keys[e.key()]} (evaluated once)")
        keys.setdefault(e.key(), k)
    for sec in ("decay", "by_year", "neutralise", "profile"):
        for vid in (cfg.get("diagnostics") or {}).get(sec) or []:
            if vid not in ids:
                print(f"note: diagnostics.{sec} names '{vid}', which is not a variant id")
    print(f"{len(items) - bad}/{len(items)} OK" + ("" if bad else " — safe to run"))
    return 1 if bad else 0


def propose_cmd(fid: str) -> int:
    from .probes import load_study_probes
    from .propose import propose
    cfg = _config(fid)
    for pf in cfg.get("probes") or []:
        load_study_probes(PARTURA_ROOT / pf)
    for c in propose(cfg["expression"]):
        if c.kind == "note":
            print(f"# {c.why}")
            continue
        print(f"[{c.kind:<11}] {c.id:<28} {c.why}\n              {c.expr}")
    return 0


def main(argv=None) -> int:
    a = list(sys.argv[1:] if argv is None else argv)
    if not a:
        print(__doc__)
        return 2
    cmd, rest = a[0], a[1:]
    if cmd == "ops":
        return ops(rest[0] if rest else ".")
    if cmd == "src":
        return src(rest)
    if cmd == "check":
        return check(rest[0])
    if cmd == "propose":
        return propose_cmd(rest[0])
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())
