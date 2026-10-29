#!/bin/bash
# C06 health check (as C05's c05_health.sh): prints only problems, and one line per seed.
#   source tmp/c06_env.sh; scripts/server/c06_health.sh <seeds...>
cd ${PARTURA_HOME:?}
D=research/coldstart_C06
SEEDS=${*:-801 802 803 804 805 806 807 808}
GDISK=${GUARD_DISK:-/root/autodl-tmp}
avail=$(df -BG --output=avail $GDISK | tail -1 | tr -dc 0-9)
[ "${avail:-0}" -lt 120 ] && echo "DISK: only ${avail}G free on $GDISK (the guard kills a job below 60G)"
grep -a "$(date +%F)" research/coldstart_C01/diskguard.log 2>/dev/null | grep -a killing | sed 's/^/GUARD KILL: /'
read used total <<< "$(nvidia-smi --query-gpu=memory.used,memory.total --format=csv,noheader,nounits | tr -d ',')"
[ $((used * 100 / total)) -ge 92 ] && echo "GPU: ${used}/${total} MiB in use"
for f in logs/_idea_c06s8*.log logs/_c06*.log; do
  [ -e "$f" ] || continue
  case "$f" in *.broken.log) continue ;; esac
  n=$(grep -ac "CUDA error\|CUDA out of memory\|CUBLAS_STATUS" "$f"); t=$(grep -ac "Traceback" "$f")
  x=$(grep -ao "partura exit [0-9]*\|corr exit [0-9]*" "$f" | tail -1 | grep -v "exit 0")
  [ "$n$t" != "00" ] || [ -n "$x" ] && echo "LOG $f: cuda-errors $n, tracebacks $t ${x}"
done
$PY - $SEEDS <<'PYEOF'
import glob, json, os, sys, time
D = "research/coldstart_C06"
for f in sorted(glob.glob("episodes/c06s8*/evidence.json")):
    E = json.load(open(f))
    for arm, A in E["arms"].items():
        if A.get("error") or A.get("live", 0) == 0 or A.get("scored", 0) < 0.25 * E.get("budget", 0):
            print(f"EVIDENCE {f}: error {str(A.get('error'))[:60]}, scored {A.get('scored')} live {A.get('live')} of budget {E.get('budget')}")
for f in sorted(glob.glob(f"{D}/arms/*.DONE")):
    for line in open(f):
        p = line.split()
        if len(p) >= 2 and p[-1] != "0":
            print(f"DONE {os.path.basename(f)}: {line.strip()}")
now = time.time()
for s in sys.argv[1:]:
    log = f"{D}/conductor_s{s}.log"
    last = open(log).read().strip().splitlines()[-1] if os.path.exists(log) and os.path.getsize(log) else "(no conductor log yet)"
    age = (now - os.path.getmtime(log)) / 60 if os.path.exists(log) else 0
    rounds = [k for k in (1, 2, 3) if os.path.exists(f"{D}/arms/s{s}_C_r{k}.DONE")]
    print(f"s{s}: rounds done {rounds}, conductor: {last[:90]} ({age:.0f} min ago)")
PYEOF
for s in $SEEDS; do
  pgrep -f "[c]06_conductor.sh $s\$" >/dev/null || [ -e $D/arms/s$s.ALLDONE ] || echo "CONDUCTOR s$s: not running and not finished"
done
pgrep -f "[c]06_keeper.sh" >/dev/null || echo "KEEPER: not running"
echo "health check done $(date +%F_%T)"
