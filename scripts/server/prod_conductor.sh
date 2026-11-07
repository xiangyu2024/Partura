#!/bin/bash
# PROD W01 (research/prod_W01/PLAN.md), one seed on this host: its main AlphaCube M (batches 1..4, scripts/server/prod_m.sh, started
# in the background, as C07's conductor does) and Partura's rounds 1..3 (as C08's conductor: arm P, scripts/c05_locate.py / c05_round.py).
#   round k:  wait for M batch k (complete evidence)  ->  locate  ->  loc/s<seed>_P_r<k>.READY
#             ->  wait for arms/s<seed>_P_r<k>.yaml (the audited plan, pushed from the laptop)  ->  missions
#   then: wait for the M chain to finish (m/s<seed>.DONE)  ->  touch arms/s<seed>.ALLDONE
# Restart-safe like C07's / C08's: finished pieces are skipped, running ones adopted (c05_round.py).  One difference from C07's conductor:
# if the M chain dies while this script is waiting (a disk-guard kill, a timeout, a reboot), it is started again here -- at most
# PROD_M_STARTS times (default 6 = the first start and 5 restarts, the keeper's limit), counted in m/s<seed>.starts (delete the file to
# allow more).  Without this a dead M chain would leave the seed waiting for ever with its conductor "alive".
#   source tmp/prod_env.sh; scripts/server/prod_conductor.sh <seed>
S=${1:?seed}
cd ${PARTURA_HOME:?}
[ "$PARTURA_C0X" = PROD ] && [ -n "$PARTURA_STUDY_DIR" ] && [ "$PARTURA_RANK_FIRST" = 1 ] && [ "$PARTURA_NEUTRAL_POWERS" = 1,2,3 ] || { echo "source tmp/prod_env.sh first"; exit 2; }
D=research/$PARTURA_STUDY_DIR; mkdir -p $D/m $D/loc $D/arms logs
LOG=$D/conductor_s$S.log
say() { echo "[prod s$S] $* $(date +%F_%T)" >> $LOG; }
POLL=${PROD_POLL_S:-30}; POLL_M=${PROD_POLL_M_S:-60}            # (seconds; the tests shorten them)
m_alive() { pgrep -f "[p]rod_m.sh $S\$" > /dev/null; }
ensure_m() {                                                    # 0 = the M chain is done or running; 1 = gave up
  [ -e $D/m/s$S.DONE ] && return 0
  m_alive && return 0
  n=$(cat $D/m/s$S.starts 2>/dev/null || echo 0)
  if [ "$n" -ge "${PROD_M_STARTS:-6}" ]; then say "M chain: not running, not finished, and already started $n times -- giving up"; return 1; fi
  echo $((n + 1)) > $D/m/s$S.starts
  nohup bash scripts/server/prod_m.sh $S >> $D/m/s$S.out 2>&1 < /dev/null &
  say "M chain started (start $((n + 1)))"
  return 0
}
waitfor() { while [ ! -e "$1" ]; do ensure_m || exit 7; sleep $POLL; done; }
m_batch_done() { grep -q '"complete": true' episodes/prods${S}M${1}_I0_open_search/evidence.json 2>/dev/null; }
ensure_m || exit 7
for k in 1 2 3; do
  [ -e $D/arms/s${S}_P_r$k.DONE ] && { say "round $k: done earlier"; continue; }          # a restart: this round is over
  until m_batch_done $k; do ensure_m || exit 7; sleep $POLL_M; done
  say "round $k: M batch $k ready"
  if [ ! -e $D/loc/s${S}_P_r$k.READY ]; then
    $PY -u scripts/c05_locate.py locate $S P $k > logs/_prodloc_s${S}_P_r$k.log 2>&1 || { say "round $k: locate failed"; exit 4; }
    touch $D/loc/s${S}_P_r$k.READY
  fi
  say "round $k: located; waiting for Partura's plan"
  waitfor $D/arms/s${S}_P_r$k.yaml
  $PY scripts/c05_round.py mission $S P $k > logs/_prodmis_s${S}_P_r$k.log 2>&1
  [ -e $D/arms/s${S}_P_r$k.DONE ] || { say "round $k: the mission runner died"; exit 6; }
  say "round $k: missions ended"
done
while [ ! -e $D/m/s$S.DONE ]; do ensure_m || exit 7; sleep $POLL_M; done
touch $D/arms/s$S.ALLDONE
say "all done"
