#!/bin/bash
# PROD W01: keep every seed's conductor alive (as c08_keeper.sh, itself C05's c05_keeper.sh, PLAN revision 7 there).  Every 60 s, for
# each seed that is not finished: if its conductor is not running AND none of its runners (mission, locate) is, start the conductor
# again (it resumes).  At most 5 restarts per seed, then it gives up and says so.  The M chain (prod_m.sh) is NOT counted as a
# runner: unlike C08 the conductor has work to do while M runs (locate after every M batch), so a dead conductor is restarted even
# with M alive (the restarted conductor sees M alive and does not start a second one).
#   source tmp/prod_env.sh; scripts/server/prod_keeper.sh 901 902 ... 908        (in its own screen / tmux session, one per host)
cd ${PARTURA_HOME:?}
[ "$PARTURA_C0X" = PROD ] && [ -n "$PARTURA_STUDY_DIR" ] || { echo "source tmp/prod_env.sh first"; exit 2; }
D=research/$PARTURA_STUDY_DIR
LOG=$D/keeper.log
declare -A N
echo "[keeper] started for $* $(date +%F_%T)" >> $LOG
while true; do
  all=1
  for S in "$@"; do
    [ -e $D/arms/s$S.ALLDONE ] && continue
    all=0
    pgrep -f "[p]rod_conductor.sh $S\$" >/dev/null && continue
    pgrep -f "[c]05_round.py mission $S P " >/dev/null && continue
    pgrep -f "[c]05_locate.py locate $S P " >/dev/null && continue
    n=${N[$S]:-0}
    if [ $n -ge 5 ]; then
      [ $n -eq 5 ] && echo "[keeper] s$S: GAVE UP after 5 restarts $(date +%F_%T)" >> $LOG
      N[$S]=6; continue
    fi
    N[$S]=$((n + 1))
    echo "[keeper] s$S: conductor not running, no runner alive -> restart $((n + 1)) $(date +%F_%T)" >> $LOG
    nohup bash scripts/server/prod_conductor.sh $S >> $D/conductor_s$S.out 2>&1 &
  done
  [ $all = 1 ] && { echo "[keeper] all seeds finished $(date +%F_%T)" >> $LOG; exit 0; }
  sleep 60
done
