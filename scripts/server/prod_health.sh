#!/bin/bash
# PROD W01 health check (as c06_health.sh / c05_health.sh): prints only problems, and one line per seed.
#   source tmp/prod_env.sh; scripts/server/prod_health.sh 901 902 ... 908        (the seeds of THIS host)
# Reads only: disk, the disk guard's log, the GPU, logs of this study's runs, their evidence, the markers.  Never kills or starts anything.
cd ${PARTURA_HOME:?}
[ "$PARTURA_C0X" = PROD ] && [ -n "$PARTURA_STUDY_DIR" ] || { echo "source tmp/prod_env.sh first"; exit 2; }
D=research/$PARTURA_STUDY_DIR
SEEDS=${*:?the seeds of this host}
GDISK=${GUARD_DISK:-/root/autodl-tmp}
avail=$(df -BG --output=avail $GDISK | tail -1 | tr -dc 0-9)
[ "${avail:-0}" -lt 120 ] && echo "DISK: only ${avail}G free on $GDISK (the guard kills a job below 60G)"
[ "${avail:-0}" -lt "${PROD_SWITCH_GB:-90}" ] && [ "$GDISK" = /root/autodl-tmp ] && echo "DISK: below ${PROD_SWITCH_GB:-90}G on the old host -- PLAN section 3: move this host's later rounds to the new host"
screen -ls 2>/dev/null | grep -q "\.c01_guard[[:space:]]" || echo "DISK GUARD: no screen session c01_guard (scripts/server/c01_diskguard.sh)"
grep -a "$(date +%F)" research/coldstart_C01/diskguard.log 2>/dev/null | grep -a killing | sed 's/^/GUARD KILL: /'
read used total <<< "$(nvidia-smi --query-gpu=memory.used,memory.total --format=csv,noheader,nounits | head -1 | tr -d ',')"
[ -n "$total" ] && [ $((used * 100 / total)) -ge 92 ] && echo "GPU: ${used}/${total} MiB in use"
for f in logs/_idea_prods9*.log logs/_prod*.log; do
  [ -e "$f" ] || continue
  case "$f" in *.broken.log) continue ;; esac
  n=$(grep -ac "CUDA error\|CUDA out of memory\|CUBLAS_STATUS" "$f"); t=$(grep -ac "Traceback" "$f")
  x=$(grep -ao "partura exit [0-9]*\|corr exit [0-9]*" "$f" | tail -1 | grep -v "exit 0")
  { [ "$n$t" != "00" ] || [ -n "$x" ]; } && echo "LOG $f: cuda-errors $n, tracebacks $t ${x}"
done
$PY - $D $SEEDS <<'PYEOF'
import glob, json, os, sys, time
D, seeds = sys.argv[1], sys.argv[2:]
for f in sorted(glob.glob("episodes/prods9*/evidence.json")):
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
for s in seeds:
    log = f"{D}/conductor_s{s}.log"
    last = open(log).read().strip().splitlines()[-1] if os.path.exists(log) and os.path.getsize(log) else "(no conductor log yet)"
    age = (now - os.path.getmtime(log)) / 60 if os.path.exists(log) else 0
    m = [e for e in (1, 2, 3, 4) if '"complete": true' in (open(f"episodes/prods{s}M{e}_I0_open_search/evidence.json").read() if os.path.exists(f"episodes/prods{s}M{e}_I0_open_search/evidence.json") else "")]
    rounds = [k for k in (1, 2, 3) if os.path.exists(f"{D}/arms/s{s}_P_r{k}.DONE")]
    starts = open(f"{D}/m/s{s}.starts").read().strip() if os.path.exists(f"{D}/m/s{s}.starts") else "0"
    print(f"s{s}: M batches {m}, M starts {starts}, rounds done {rounds}, conductor: {last[:90]} ({age:.0f} min ago)")
PYEOF
for s in $SEEDS; do
  pgrep -f "[p]rod_conductor.sh $s\$" >/dev/null || [ -e $D/arms/s$s.ALLDONE ] || echo "CONDUCTOR s$s: not running and not finished"
  [ -e $D/m/s$s.DONE ] || pgrep -f "[p]rod_m.sh $s\$" >/dev/null || echo "M CHAIN s$s: not running and not finished"
done
pgrep -f "[p]rod_keeper.sh" >/dev/null || echo "KEEPER: not running"
echo "health check done $(date +%F_%T)"
