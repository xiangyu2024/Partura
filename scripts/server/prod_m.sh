#!/bin/bash
# PROD (research/prod_W01/PLAN.md section 1), as scripts/server/c07_m.sh with the study taken from the environment: the main
# AlphaCube M of one seed -- batches 1..4 in a row, batch e banned from the heads of batches 1..e-1 of the same seed (rank
# correlation >= 0.7, same skeleton) and from nothing else (not from Partura's heads).  Same search settings as C07's M
# (budget 192, population 48, threshold 0.5, seed 10 * seed + batch, the C05 base guidance, 720-minute timeout incl. queueing).
# A batch already finished (its evidence says "complete") is not rerun, so the chain can be restarted.
#   source tmp/prod_env.sh; scripts/server/prod_m.sh <seed> [batches]
# Episodes: episodes/prods<seed>M<batch>_I0_open_search; logs logs/_idea_prods<seed>M<batch>.log; chain log, DONE marker and the
# libraries it bans from: research/prod_W01/m/.
S=${1:?seed}; NB=${2:-4}
cd ${PARTURA_HOME:?}
[ "$PARTURA_C0X" = PROD ] && [ -n "$PARTURA_STUDY_DIR" ] && [ "$PARTURA_RANK_FIRST" = 1 ] && [ "$PARTURA_NEUTRAL_POWERS" = 1,2,3 ] || { echo "source tmp/prod_env.sh first"; exit 2; }
D=research/$PARTURA_STUDY_DIR/m; mkdir -p $D logs
for e in $(seq 1 $NB); do
  tag=prods${S}M$e; ep=episodes/${tag}_I0_open_search
  if grep -q '"complete": true' $ep/evidence.json 2>/dev/null; then continue; fi
  eps=""; for p in $(seq 1 $((e - 1))); do eps="$eps episodes/prods${S}M${p}_I0_open_search"; done
  lib=""
  if [ $e -gt 1 ]; then
    $PY scripts/c05_lib.py heads $D/lib_s${S}_b$e.json $eps >> $D/s$S.log 2>&1 || { echo "[prod] $tag: library failed" >> $D/s$S.log; exit 3; }
    lib="--ban-library $D/lib_s${S}_b$e.json"
  fi
  timeout --signal=TERM --kill-after=60 ${JOB_MINUTES:-720}m \
    $PY -u scripts/idea_search.py I0_open_search --guidance guidance/C05_base.yaml --arms control --seed $((10 * S + e)) --tag $tag \
      --budget 192 --population 48 --threshold 0.5 $lib > logs/_idea_$tag.log 2>&1
  code=$?
  echo "[partura exit $code $(date +%F_%T)]" >> logs/_idea_$tag.log
  echo "[prod] $tag exit $code $(date +%F_%T)" >> $D/s$S.log
  [ $code -eq 0 ] || exit $code
done
touch $D/s$S.DONE
