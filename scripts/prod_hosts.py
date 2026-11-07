"""PROD (research/prod_W01/PLAN.md section 3): which seed runs on which host -- the one place that says so.

The mapping is research/prod_W01/hosts.json (override: $PROD_HOSTS):
    {"study": "PROD", "dir": "prod_W01",
     "hosts": {"new": {"ssh": "<ssh command>", "home": "<Partura home on that host>"}, "old": {...}},
     "seeds": {"901": "new", ..., "909": "old", ...}}
Every laptop-side PROD script (prod_sync.sh, prod_gather.sh, prod_final.py's seed list) reads it through this module.

    python scripts/prod_hosts.py seeds [host]     -> the seeds (of one host), space separated, ascending
    python scripts/prod_hosts.py host <seed>      -> new | old
    python scripts/prod_hosts.py ssh <seed>       -> the ssh command of the seed's host
    python scripts/prod_hosts.py home <seed>      -> the Partura home on the seed's host
    python scripts/prod_hosts.py dir              -> prod_W01
    python scripts/prod_hosts.py hostssh <host>   -> the ssh command of a host (new | old)
    python scripts/prod_hosts.py hosthome <host>  -> the Partura home of a host
Stdlib only.  Unknown seeds / hosts exit non-zero with a message on stderr (a script must never guess a host).
"""
import json
import os
import sys
from pathlib import Path

DEFAULT = Path(__file__).resolve().parents[1] / "research" / "prod_W01" / "hosts.json"


def load(path=None):
    p = Path(path or os.environ.get("PROD_HOSTS") or DEFAULT)
    cfg = json.loads(p.read_text(encoding="utf-8"))
    problems = []
    for k in ("study", "dir", "hosts", "seeds"):
        if k not in cfg:
            problems.append(f"missing key {k!r}")
    if not problems:
        for h, v in cfg["hosts"].items():
            for k in ("ssh", "home"):
                if not str(v.get(k, "")).strip():
                    problems.append(f"host {h}: no {k}")
            if str(v.get("home", "")).strip() in ("", "/"):
                problems.append(f"host {h}: home must be a real directory")
        for s, h in cfg["seeds"].items():
            if not s.isdigit():
                problems.append(f"seed {s!r} is not a number")
            if h not in cfg["hosts"]:
                problems.append(f"seed {s}: host {h!r} is not defined")
    if problems:
        raise SystemExit(f"{p}: " + "; ".join(problems))
    return cfg


def seeds(cfg, host=None):
    return sorted(int(s) for s, h in cfg["seeds"].items() if host in (None, h))


def host_of(cfg, seed):
    h = cfg["seeds"].get(str(int(seed)))
    if h is None:
        raise SystemExit(f"seed {seed} is not in the host mapping ({sorted(cfg['seeds'])})")
    return h


def main(argv):
    cfg = load()
    cmd, arg = argv[0], (argv[1] if len(argv) > 1 else None)
    if cmd == "seeds":
        print(" ".join(map(str, seeds(cfg, arg))))
    elif cmd == "host":
        print(host_of(cfg, arg))
    elif cmd == "ssh":
        print(cfg["hosts"][host_of(cfg, arg)]["ssh"])
    elif cmd == "home":
        print(cfg["hosts"][host_of(cfg, arg)]["home"])
    elif cmd == "dir":
        print(cfg["dir"])
    elif cmd in ("hostssh", "hosthome"):
        if arg not in cfg["hosts"]:
            raise SystemExit(f"unknown host {arg!r} ({sorted(cfg['hosts'])})")
        print(cfg["hosts"][arg]["ssh" if cmd == "hostssh" else "home"])
    else:
        raise SystemExit(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
