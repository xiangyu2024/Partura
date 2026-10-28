#!/bin/bash
# C05 (research/coldstart_C05/PLAN.md §2.1): the main AlphaCube M of one seed -- batches 1..4 in a row, batch e banned from
# the heads of batches 1..e-1 of the same seed (rank correlation >= 0.7, same skeleton) and from nothing else.
# A batch already finished (its evidence has heads) is not rerun, so the chain can be restarted.
#   source tmp/c05_env.sh; scripts/server/c05_m.sh <seed> [batches]
S=${1:?seed}; NB=${2:-4}
cd ${PARTURA_HOME:?}
D=research/coldstart_C05/m; mkdir -p $D logs
for e in $(seq 1 $NB); do
  tag=c05s${S}M$e; ep=episodes/${tag}_I0_open_search
  if grep -q '"independent_distinct"' $ep/evidence.json 2>/dev/null; then continue; fi
  eps=""; for p in $(seq 1 $((e - 1))); do eps="$eps episodes/c05s${S}M${p}_I0_open_search"; done
  lib=""
  if [ $e -gt 1 ]; then
    $PY scripts/c05_lib.py heads $D/lib_s${S}_b$e.json $eps >> $D/s$S.log 2>&1 || { echo "[c05] $tag: library failed" >> $D/s$S.log; exit 3; }
    lib="--ban-library $D/lib_s${S}_b$e.json"
  fi
  timeout --signal=TERM --kill-after=60 ${JOB_MINUTES:-180}m \
    $PY -u scripts/idea_search.py I0_open_search --guidance guidance/C05_base.yaml --arms control --seed $((10 * S + e)) --tag $tag \
      --budget 192 --population 48 --threshold 0.5 $lib > logs/_idea_$tag.log 2>&1
  code=$?
  echo "[partura exit $code $(date +%F_%T)]" >> logs/_idea_$tag.log
  echo "[c05] $tag exit $code $(date +%F_%T)" >> $D/s$S.log
  [ $code -eq 0 ] || exit $code
done
touch $D/s$S.DONE
