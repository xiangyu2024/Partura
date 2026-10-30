#!/bin/bash
# C07 (research/coldstart_C07/PLAN.md §2): one seed on this host -- its main AlphaCube M (batches 1..4, scripts/server/c07_m.sh,
# in the background) and arm A's rounds 1..3 (round k after M batch k and after A's round k-1; c05_round.py A with $PARTURA_C0X=C07).
# Restart-safe: finished pieces are skipped (c05_round.py adopts or skips its own runs).
#   source tmp/c07_env.sh; scripts/server/c07_conductor.sh <seed>
S=${1:?seed}
cd ${PARTURA_HOME:?}
[ "$PARTURA_C0X" = C07 ] && [ "$PARTURA_RANK_FIRST" = 1 ] || { echo "source tmp/c07_env.sh first"; exit 2; }
D=research/coldstart_C07; mkdir -p $D/m $D/arms logs
LOG=$D/conductor_s$S.log
say() { echo "[c07 s$S] $* $(date +%F_%T)" >> $LOG; }
if [ ! -e $D/m/s$S.DONE ] && ! pgrep -f "[c]07_m.sh $S\$" > /dev/null; then
  nohup bash scripts/server/c07_m.sh $S >> $D/m/s$S.out 2>&1 < /dev/null &
  say "M chain started"
fi
for k in 1 2 3; do
  until grep -q '"complete": true' episodes/c07s${S}M${k}_I0_open_search/evidence.json 2>/dev/null; do sleep 60; done
  say "round $k: M batch $k ready"
  [ -e $D/arms/s${S}_A_r$k.DONE ] || $PY scripts/c05_round.py A $S $k > logs/_c07A_s${S}_r$k.log 2>&1
  [ -e $D/arms/s${S}_A_r$k.DONE ] || { say "round $k: A runner died"; exit 6; }
  say "round $k: A ended"
done
while [ ! -e $D/m/s$S.DONE ]; do sleep 60; done
touch $D/arms/s$S.ALLDONE
say "all done"
