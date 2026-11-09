#!/bin/bash
# PROD W01 (research/prod_W01/PLAN.md 修订 2), laptop side: the deterministic steps of one round for many seeds at once,
# run by the coordinator instead of one Haiku agent per seed and step (~50k tokens each, for one command).
#   scripts/prod_round.sh fetch  <k> "<seeds>"   -> prod_sync.sh fetch <k> <seed> (one retry)
#   scripts/prod_round.sh corr   <k> "<seeds>"   -> prod_sync.sh corr <k> <seed> 1, all seeds in parallel; re-run while it says
#                                                   STILL RUNNING (exit 3), at most 12 times; one more try after a failure
#   scripts/prod_round.sh finish <k> "<seeds>"   -> scripts/prod_finish.py <k> <seed> (finalize, check, push), no retry
# One line per seed at the end: "<seed> OK <stage>" / "<seed> FAILED <stage>: <last line>"; per-seed logs in tmp/prod_round/.
# Exit 0 only if every seed is OK.  The workflow (workflows/prod_round.js, args.stage) runs only the PI and the auditor.
STAGE=${1:?fetch|corr|finish}; K=${2:?round}; SEEDS=${3:?seeds}
REPO=$(cd "$(dirname "$0")/.." && pwd); cd "$REPO" || exit 1
PY=/Users/wxy/.venvs/alphacube/bin/python
export PARTURA_C0X=PROD PARTURA_STUDY_DIR=$($PY scripts/prod_hosts.py dir) C06_CTRL_STRIKE=0.8   # prod_W01 unless $PROD_HOSTS says otherwise ALPHACUBE_ROOT=$HOME/Desktop/AlphaCube-steering
export PYTHONPATH=$HOME/Desktop/AlphaCube-steering/src:$REPO
LOG=$REPO/tmp/prod_round; mkdir -p $LOG

one() {   # <seed> -> exit status of the stage; output in $LOG/r<k>_s<seed>_<stage>.log
  local S=$1 f=$LOG/r${K}_s$1_$STAGE.log rc
  case $STAGE in
    fetch)  bash scripts/prod_sync.sh fetch $K "$S" > $f 2>&1 || bash scripts/prod_sync.sh fetch $K "$S" >> $f 2>&1 ;;
    corr)   : > $f
            for try in 1 2; do
              for i in $(seq 1 12); do bash scripts/prod_sync.sh corr $K $S 1 >> $f 2>&1; rc=$?; [ $rc -ne 3 ] && break; done
              [ $rc -eq 0 ] && return 0
            done
            return 1 ;;
    finish) $PY scripts/prod_finish.py $K $S > $f 2>&1 ;;
    *)      echo "unknown stage $STAGE"; return 2 ;;
  esac
}

for S in $SEEDS; do ( one $S; echo $? > $LOG/r${K}_s${S}_$STAGE.rc ) & done
wait
RC=0
for S in $SEEDS; do
  f=$LOG/r${K}_s${S}_$STAGE
  if [ "$(cat $f.rc 2>/dev/null)" = 0 ]; then echo "$S OK $STAGE  $(grep -a '^FINALIZED\|bytes of locate\|^PUSHED' $f.log | tr '\n' ' ' | cut -c1-220)"
  else echo "$S FAILED $STAGE: $(tail -1 $f.log)"; RC=1; fi
done
exit $RC
