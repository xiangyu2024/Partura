#!/bin/bash
# C08 (research/coldstart_C08/PLAN.md): one seed's rounds 1..3 of arm P on this host.  M and A are C07's (the new rule), finished.
#   round k:  locate -> loc/s<seed>_P_r<k>.READY  ->  wait for arms/s<seed>_P_r<k>.yaml (the audited plan, pushed from the laptop)  ->  missions
#   source tmp/c08_env.sh; scripts/server/c08_conductor.sh <seed>
S=${1:?seed}
cd ${PARTURA_HOME:?}
[ "$PARTURA_C0X" = C08 ] && [ "$PARTURA_RANK_FIRST" = 1 ] || { echo "source tmp/c08_env.sh first"; exit 2; }
D=research/coldstart_C08; mkdir -p $D/loc $D/arms logs
LOG=$D/conductor_s$S.log
say() { echo "[c08 s$S] $* $(date +%F_%T)" >> $LOG; }
waitfor() { while [ ! -e "$1" ]; do sleep 30; done; }
for k in 1 2 3; do
  if [ ! -e $D/loc/s${S}_P_r$k.READY ]; then
    $PY -u scripts/c05_locate.py locate $S P $k > logs/_c08loc_s${S}_P_r$k.log 2>&1 || { say "round $k: locate failed"; exit 4; }
    touch $D/loc/s${S}_P_r$k.READY
  fi
  say "round $k: located; waiting for Partura's plan"
  [ -e $D/arms/s${S}_P_r$k.DONE ] && continue
  waitfor $D/arms/s${S}_P_r$k.yaml
  $PY scripts/c05_round.py mission $S P $k > logs/_c08mis_s${S}_P_r$k.log 2>&1
  [ -e $D/arms/s${S}_P_r$k.DONE ] || { say "round $k: the mission runner died"; exit 6; }
  say "round $k: missions ended"
done
touch $D/arms/s$S.ALLDONE
say "all rounds ended"
