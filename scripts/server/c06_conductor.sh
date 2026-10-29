#!/bin/bash
# C06 (research/coldstart_C06/PLAN.md §2.1, §2.4): one seed's rounds 1..3 of arm C on this host.  M is C05's and has finished.
#   round k:  locate (round 1: C05's B round-1 output, copied in beforehand -- the snapshot is the same: M batch 1 only)
#             -> loc/s<seed>_C_r<k>.READY  ->  wait for arms/s<seed>_C_r<k>.yaml (the audited plan, pushed from the laptop)  ->  missions
#   source tmp/c06_env.sh; scripts/server/c06_conductor.sh <seed>
S=${1:?seed}
cd ${PARTURA_HOME:?}
[ "$PARTURA_C0X" = C06 ] || { echo "source tmp/c06_env.sh first"; exit 2; }
D=research/coldstart_C06; mkdir -p $D/loc $D/arms logs
LOG=$D/conductor_s$S.log
say() { echo "[c06 s$S] $* $(date +%F_%T)" >> $LOG; }
waitfor() { while [ ! -e "$1" ]; do sleep 30; done; }
for k in 1 2 3; do
  if [ ! -e $D/loc/s${S}_C_r$k.READY ]; then
    if [ $k -eq 1 ]; then
      [ -s $D/loc/s${S}_C_r1.json ] && [ -s $D/loc/s${S}_C_r1.md ] || { say "round 1: C05's locate output was not copied in"; exit 3; }
    else
      $PY -u scripts/c05_locate.py locate $S C $k > logs/_c06loc_s${S}_C_r$k.log 2>&1 || { say "round $k: locate failed"; exit 4; }
    fi
    touch $D/loc/s${S}_C_r$k.READY
  fi
  say "round $k: located; waiting for Partura's plan"
  [ -e $D/arms/s${S}_C_r$k.DONE ] && continue                 # a restart: this round is done
  waitfor $D/arms/s${S}_C_r$k.yaml
  $PY scripts/c05_round.py mission $S C $k > logs/_c06mis_s${S}_C_r$k.log 2>&1
  [ -e $D/arms/s${S}_C_r$k.DONE ] || { say "round $k: the mission runner died"; exit 6; }
  say "round $k: missions ended"
done
touch $D/arms/s$S.ALLDONE
say "all rounds ended"
