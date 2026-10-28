#!/bin/bash
# C05 (research/coldstart_C05/PLAN.md §2.2): one seed's rounds 1..3 on this host, after its M chain has been started.
#   round k:  wait for M batch k  ->  A's two runs (in the background; after A's round k-1)
#             locate for B and B0 (round 1: one snapshot, so B0's is a copy of B's)  ->  loc/s<seed>_r<k>.READY
#             wait for arms/s<seed>_B_r<k>.yaml (Partura's plan, pushed from the laptop)  ->  B0's plan  ->  both arms' missions
#   source tmp/c05_env.sh; scripts/server/c05_conductor.sh <seed>
S=${1:?seed}
cd ${PARTURA_HOME:?}
D=research/coldstart_C05; mkdir -p $D/loc $D/arms logs
LOG=$D/conductor_s$S.log
say() { echo "[c05 s$S] $* $(date +%F_%T)" >> $LOG; }
waitfor() { while [ ! -e "$1" ]; do sleep 30; done; }
for k in 1 2 3; do
  until grep -q '"independent_distinct"' episodes/c05s${S}M${k}_I0_open_search/evidence.json 2>/dev/null; do sleep 30; done
  say "round $k: M batch $k ready"
  ( [ $k -eq 1 ] || waitfor $D/arms/s${S}_A_r$((k - 1)).DONE
    $PY scripts/c05_round.py A $S $k > logs/_c05A_s${S}_r$k.log 2>&1; say "A round $k ended" ) &
  if [ ! -e $D/loc/s${S}_r$k.READY ]; then
    $PY -u scripts/c05_locate.py locate $S B $k > logs/_c05loc_s${S}_B_r$k.log 2>&1 || { say "locate B failed"; exit 4; }
    if [ $k -eq 1 ]; then
      cp $D/loc/s${S}_B_r1.json $D/loc/s${S}_B0_r1.json; cp $D/loc/s${S}_B_r1.md $D/loc/s${S}_B0_r1.md
    else
      $PY -u scripts/c05_locate.py locate $S B0 $k > logs/_c05loc_s${S}_B0_r$k.log 2>&1 || { say "locate B0 failed"; exit 4; }
    fi
    touch $D/loc/s${S}_r$k.READY
  fi
  say "round $k: located; waiting for Partura's plan"
  waitfor $D/arms/s${S}_B_r$k.yaml
  $PY scripts/c05_round.py b0plan $S $k >> $LOG 2>&1 || { say "b0plan failed"; exit 5; }
  $PY scripts/c05_round.py mission $S B $k > logs/_c05mis_s${S}_B_r$k.log 2>&1 & p1=$!
  $PY scripts/c05_round.py mission $S B0 $k > logs/_c05mis_s${S}_B0_r$k.log 2>&1 & p2=$!
  wait $p1 $p2
  [ -e $D/arms/s${S}_B_r$k.DONE ] && [ -e $D/arms/s${S}_B0_r$k.DONE ] || { say "round $k: a mission runner died"; exit 6; }
  say "round $k: missions ended"
done
waitfor $D/arms/s${S}_A_r3.DONE
touch $D/arms/s$S.ALLDONE
say "all rounds ended"
