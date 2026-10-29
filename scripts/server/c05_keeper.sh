#!/bin/bash
# C05 (PLAN revision 7): keep every seed's conductor alive.  Every 60 s, for each seed that is not finished: if its conductor is
# not running AND none of its runners (c05_round.py) is running, start the conductor again (it resumes: finished pieces are
# skipped, jobs still running are adopted, never started twice).  At most 5 restarts per seed; after that it gives up and says so.
#   source tmp/c05_env.sh; scripts/server/c05_keeper.sh 801 802 803 804        (in its own tmux / screen session)
cd ${PARTURA_HOME:?}
D=research/coldstart_C05
LOG=$D/keeper.log
declare -A N
echo "[keeper] started for $* $(date +%F_%T)" >> $LOG
while true; do
  all=1
  for S in "$@"; do
    [ -e $D/arms/s$S.ALLDONE ] && continue
    all=0
    pgrep -f "c05_conductor.sh $S\$" >/dev/null && continue
    pgrep -f "c05_round.py [A-Za-z0-9]* $S " >/dev/null && continue
    n=${N[$S]:-0}
    if [ $n -ge 5 ]; then
      [ $n -eq 5 ] && echo "[keeper] s$S: GAVE UP after 5 restarts $(date +%F_%T)" >> $LOG
      N[$S]=6; continue
    fi
    N[$S]=$((n + 1))
    echo "[keeper] s$S: conductor not running, no runner alive -> restart $((n + 1)) $(date +%F_%T)" >> $LOG
    nohup bash scripts/server/c05_conductor.sh $S >> $D/conductor_s$S.out 2>&1 &
  done
  [ $all = 1 ] && { echo "[keeper] all seeds finished $(date +%F_%T)" >> $LOG; exit 0; }
  sleep 60
done
