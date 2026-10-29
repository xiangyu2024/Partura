#!/bin/bash
# C05 health check (research/coldstart_C05/PLAN.md revision 6): everything that has gone wrong, or could, in one pass.
#   source tmp/c05_env.sh; scripts/server/c05_health.sh <seeds...>
# Prints only problems (and a one-line summary per seed); exit 0 always.
cd ${PARTURA_HOME:?}
D=research/coldstart_C05
SEEDS=${*:-801 802 803 804 805 806 807 808}
GDISK=${GUARD_DISK:-/root/autodl-tmp}
avail=$(df -BG --output=avail $GDISK | tail -1 | tr -dc 0-9)
[ "${avail:-0}" -lt 120 ] && echo "DISK: only ${avail}G free on $GDISK (the guard kills a job below 60G)"
grep -a "2026-10-29\|2026-10-3" research/coldstart_C01/diskguard.log 2>/dev/null | grep -a killing | sed 's/^/GUARD KILL: /'
read used total <<< "$(nvidia-smi --query-gpu=memory.used,memory.total --format=csv,noheader,nounits | tr -d ',')"
[ $((used * 100 / total)) -ge 92 ] && echo "GPU: ${used}/${total} MiB in use"
for f in logs/_idea_c05s8*.log logs/_c05*.log; do
  [ -e "$f" ] || continue
  case "$f" in *.broken.log) continue ;; esac
  n=$(grep -ac "CUDA error\|CUDA out of memory\|CUBLAS_STATUS" "$f")
  t=$(grep -ac "Traceback" "$f")
  x=$(grep -ao "partura exit [0-9]*" "$f" | tail -1 | grep -v "exit 0")
  r=$(grep -ac "run_mining ended with" "$f")
  [ "$n$t$r" != "000" ] || [ -n "$x" ] && echo "LOG $f: cuda-errors $n, tracebacks $t, run_mining-errors $r ${x}"
done
$PY - $SEEDS <<'EOF'
import glob, json, os, re, sys, time
D = "research/coldstart_C05"
for f in sorted(glob.glob("episodes/c05s8*/evidence.json")):
    E = json.load(open(f))
    for arm, A in E["arms"].items():
        bad = []
        if A.get("error"):
            bad.append(f"error {A['error'][:80]}")
        if "independent_distinct" not in A:
            bad.append("no heads field")
        if A.get("live", 0) == 0 or A.get("scored", 0) < 0.25 * E.get("budget", 0):
            bad.append(f"scored {A.get('scored')} live {A.get('live')} of budget {E.get('budget')}")
        if bad:
            print(f"EVIDENCE {f}: {'; '.join(bad)}")
for f in sorted(glob.glob(f"{D}/arms/*.DONE")):
    for line in open(f):
        p = line.split()
        if len(p) >= 2 and p[-1] != "0":
            print(f"DONE {os.path.basename(f)}: {line.strip()}")
now = time.time()
for s in sys.argv[1:]:
    m = sum(1 for e in range(1, 5) if os.path.exists(f"episodes/c05s{s}M{e}_I0_open_search/evidence.json"))
    log = f"{D}/conductor_s{s}.log"
    last = open(log).read().strip().splitlines()[-1] if os.path.exists(log) and os.path.getsize(log) else "(no conductor log yet)"
    age = (now - os.path.getmtime(log)) / 60 if os.path.exists(log) else 0
    rounds = [k for k in (1, 2, 3) if all(os.path.exists(f"{D}/arms/s{s}_{x}_r{k}.DONE") for x in ("A", "B", "B0"))]
    print(f"s{s}: M {m}/4, rounds done {rounds}, conductor: {last[:90]} ({age:.0f} min ago)")
EOF
for s in $SEEDS; do
  pgrep -f "c05_conductor.sh $s\$" >/dev/null || [ -e $D/arms/s$s.ALLDONE ] || echo "CONDUCTOR s$s: not running and not finished (the keeper restarts it once no runner is alive)"
  pgrep -f "c05_m.sh $s\$" >/dev/null || [ -e $D/m/s$s.DONE ] || echo "M CHAIN s$s: not running and not finished"
  for p in $(pgrep -f "idea_search.py|c05_locate.py|c05_final.py"); do
    a=$(tr "\0" " " < /proc/$p/cmdline 2>/dev/null); case "$a" in timeout*|bash*) continue ;; esac
    t=$(echo "$a" | grep -o "c05s$s[A-Za-z0-9]*\|locate.py [a-z]* $s [A-Z0-9]* [0-9]"); [ -z "$t" ] && continue
    l=$(ls -t logs/_idea_${t}.log logs/_c05R_s${s}_*.log logs/_c05loc_s${s}_*.log 2>/dev/null | head -1)
    grep -aq "device=cpu" "$l" 2>/dev/null && [ "$(ps -o pcpu= -p $p | cut -d. -f1)" -gt 100 ] && echo "CPU-BOUND $t (pid $p): a panel view on the CPU"
  done
done
pgrep -f "c05_keeper.sh" >/dev/null || echo "KEEPER: not running"
echo "health check done $(date +%F_%T)"
