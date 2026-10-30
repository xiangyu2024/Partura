#!/bin/bash
# C08: keep every seed's conductor alive (as C05's c05_keeper.sh, PLAN revision 7 there).  Every 60 s, for each seed that is not
# finished: if its conductor is not running AND none of its runners is, start the conductor again (it resumes).  At most 5 restarts.
#   source tmp/c08_env.sh; scripts/server/c08_keeper.sh 801 803 804 805        (in its own tmux / screen session)
cd ${PARTURA_HOME:?}
[ "$PARTURA_C0X" = C08 ] || { echo "source tmp/c08_env.sh first"; exit 2; }
D=research/coldstart_C08
LOG=$D/keeper.log
declare -A N
echo "[keeper] started for $* $(date +%F_%T)" >> $LOG
while true; do
  all=1
  for S in "$@"; do
    [ -e $D/arms/s$S.ALLDONE ] && continue
    all=0
    pgrep -f "[c]08_conductor.sh $S\$" >/dev/null && continue
    pgrep -f "[c]05_round.py mission $S P " >/dev/null && continue
    pgrep -f "[c]05_locate.py locate $S P " >/dev/null && continue
    n=${N[$S]:-0}
    if [ $n -ge 5 ]; then
      [ $n -eq 5 ] && echo "[keeper] s$S: GAVE UP after 5 restarts $(date +%F_%T)" >> $LOG
      N[$S]=6; continue
    fi
    N[$S]=$((n + 1))
    echo "[keeper] s$S: conductor not running, no runner alive -> restart $((n + 1)) $(date +%F_%T)" >> $LOG
    nohup bash scripts/server/c08_conductor.sh $S >> $D/conductor_s$S.out 2>&1 &
  done
  [ $all = 1 ] && { echo "[keeper] all seeds finished $(date +%F_%T)" >> $LOG; exit 0; }
  sleep 60
done
