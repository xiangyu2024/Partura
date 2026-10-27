#!/bin/bash
# Server side: one round of the C01 cold-start comparison (research/coldstart_C01/PLAN.md) -- every job of
# research/coldstart_C01/jobs_r<k>.tsv, two at a time, detached from the Mac (a locked or sleeping laptop does not stop it).
#   screen -dmS c01_r1 scripts/server/c01_queue.sh 1
# jobs file, one job per line (tab or spaces):  <tag> <idea_id> <guidance> <arms> <seed> [extra idea_search args...]
# Each job logs to logs/_idea_<tag>.log (ending with the "[partura exit N ...]" line) and writes episodes/<tag>_<idea>/evidence.json.
# When every job has ended: research/coldstart_C01/r<k>.DONE lists each tag with its exit code.
# Run `./scripts/study.sh code` on the Mac first (it syncs partura/, scripts/, guidance/, configs/).
ROUND=${1:?round number (or a jobs-file suffix, e.g. 2rerun)}
JOB_MINUTES=${JOB_MINUTES:-180}     # PLAN §6 revision 2: a job still running after this many minutes is stopped and recorded as failed
cd /root/autodl-tmp/Partura
export PYTHONPATH=${PARTURA_AC:-/root/autodl-tmp/Partura/vendor/AlphaCube-steering}/src:/root/autodl-tmp/Partura ALPHACUBE_ROOT=${PARTURA_AC:-/root/autodl-tmp/Partura/vendor/AlphaCube-steering} \
       PARTURA_RANK_DEVICE=cuda PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True PARTURA_SLOTS=${PARTURA_SLOTS:-4} PARTURA_GPU_WAYS=${PARTURA_GPU_WAYS:-2} \
       PARTURA_MEM_WAIT_S=10800 PARTURA_REWARD_DEVICE=${PARTURA_REWARD_DEVICE-cuda} OMP_NUM_THREADS=8 MKL_NUM_THREADS=8
PY=/root/miniconda3/envs/quant/bin/python
D=research/coldstart_C01
JOBS=$D/jobs_r$ROUND.tsv
[ -f "$JOBS" ] || { echo "no $JOBS"; exit 2; }
mkdir -p logs
rm -f $D/r$ROUND.DONE $D/r$ROUND.exit
echo "[c01] round $ROUND started $(date +%F_%T); $(grep -cv '^\s*\(#\|$\)' $JOBS) jobs" > $D/r$ROUND.log

run_one() {   # <tag> <idea> <guidance> <arms> <seed> [extra...]
  local tag=$1 idea=$2 g=$3 arms=$4 seed=$5; shift 5
  local log=logs/_idea_$tag.log
  timeout --signal=TERM --kill-after=60 ${JOB_MINUTES}m \
    $PY -u scripts/idea_search.py "$idea" --guidance "$g" --arms "$arms" --seed "$seed" --tag "$tag" --budget 192 --population 48 "$@" > "$log" 2>&1
  local code=$?
  echo "[partura exit $code $(date +%F_%T)]" >> "$log"
  echo "$tag $code" >> research/coldstart_C01/r$ROUND.exit
  echo "[c01] $tag exit $code $(date +%F_%T)" >> research/coldstart_C01/r$ROUND.log
}
export -f run_one
export ROUND PY JOB_MINUTES
# the disk guard (PLAN §6 revision 2) must be running whenever C01 jobs are
screen -ls | grep -q "\.c01_guard[[:space:]]" || { rm -f $D/guard.stop; screen -dmS c01_guard scripts/server/c01_diskguard.sh; }

grep -v '^\s*\(#\|$\)' $JOBS | xargs -P 2 -L 1 bash -c 'run_one "$@"' _
cp $D/r$ROUND.exit $D/r$ROUND.DONE
echo "[c01] round $ROUND finished $(date +%F_%T)" >> $D/r$ROUND.log
