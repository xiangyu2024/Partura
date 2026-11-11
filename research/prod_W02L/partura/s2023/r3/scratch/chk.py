"""Seed checker (PI s2023 r1): parse, validity, skeleton vs the 5583-library skeletons, banned ops. Reads expressions from a file (one per line)."""
import os, re, sys, warnings
warnings.filterwarnings("ignore")
ROOT = "/Users/wxy/Desktop/Partura-prod"
os.environ.setdefault("ALPHACUBE_ROOT", os.path.expanduser("~/Desktop/AlphaCube-steering"))
sys.path.insert(0, ROOT); sys.path.insert(0, os.path.join(os.environ["ALPHACUBE_ROOT"], "src"))
from partura import ops_ext  # noqa
from partura.steer import Guidance
from alphacube.expression import is_valid_root
from alphacube.parser import parse
from alphacube.plugins import load_plugins
from alphacube.mining.clustering import skeleton_key
import csv
load_plugins(["partura.ac_plugin"])
G0 = Guidance.load(os.path.join(ROOT, "guidance", "C05_base.yaml"))
LIB = {}
for r in csv.DictReader(open(os.path.join(ROOT, "research/prod_W02L/struct/members.csv"))):
    LIB.setdefault(r["skeleton"], []).append((r["lib"], r["i"], r["expression"]))
BANNED = re.compile(r"\b(ts_spearman|nt_[A-Za-z0-9_]+)\s*\(")
def skel(n): return re.sub(r"@[\d.]+", "", skeleton_key(n))
def check(e):
    try:
        t = parse(G0.canonical(e), strict=True, coerce_daily=True, n_minutes=241, allow_general=True)
    except Exception as exc:
        return None, f"PARSE-FAIL {type(exc).__name__}: {str(exc)[:100]}"
    if not is_valid_root(t): return t, "NOT-VALID-ROOT"
    if BANNED.search(e): return t, "BANNED-OP"
    s = skel(t)
    if s in LIB: return t, "LIB-SKELETON " + str(LIB[s][:2])
    return t, "ok " + s
if __name__ == "__main__":
    core = None
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    for a in sys.argv[1:]:
        if a.startswith("--core="): core = a[7:]
    ct = None
    if core:
        ct = parse(G0.canonical(core), strict=True, coerce_daily=True, n_minutes=241, allow_general=True)
    for i, line in enumerate(open(args[0]).read().splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"): continue
        t, msg = check(line)
        extra = ""
        if ct is not None and t is not None:
            extra = " core=" + ("Y" if any(n.key() == ct.key() for n in t.nodes()) else "N")
        print(f"{i:2d} {msg[:150]}{extra}\n     {line[:140]}")
