#!/bin/bash
# Server side: one batch of C02 jobs (research/coldstart_C02/PLAN.md) -- every job of research/coldstart_C02/jobs_<name>.tsv,
# two at a time, detached.  Same as c01_queue.sh, plus: the environment rules of BOTH arms (PARTURA_RHO_REJECT, PARTURA_ENV_OPW),
# the budget / population / threshold in each job line (A and B differ in budget), and the host paths as variables
# (PARTURA_HOME, PY, PARTURA_STORE, PARTURA_MIRROR) so the same script runs on either server.
#   screen -dmS c02_<name> scripts/server/c02_queue.sh <name>
# jobs file: <tag> <idea_id> <guidance> <arms> <seed> [idea_search args: --budget N --population 48 --threshold 0.7 ...]
ROUND=${1:?jobs-file name, e.g. r1}
JOB_MINUTES=${JOB_MINUTES:-180}     # PLAN §6 revision 2: a job still running after this many minutes is stopped and recorded as failed
PARTURA_HOME=${PARTURA_HOME:-/root/autodl-tmp/Partura}
cd $PARTURA_HOME
export PYTHONPATH=${PARTURA_AC:-$PARTURA_HOME/vendor/AlphaCube-steering}/src:$PARTURA_HOME ALPHACUBE_ROOT=${PARTURA_AC:-$PARTURA_HOME/vendor/AlphaCube-steering} \
       PARTURA_RANK_DEVICE=cuda PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True PARTURA_SLOTS=${PARTURA_SLOTS:-4} PARTURA_GPU_WAYS=${PARTURA_GPU_WAYS:-2} \
       PARTURA_MEM_WAIT_S=10800 PARTURA_REWARD_DEVICE=${PARTURA_REWARD_DEVICE-cuda} OMP_NUM_THREADS=8 MKL_NUM_THREADS=8 PARTURA_RHO_REJECT=${PARTURA_RHO_REJECT:-0.5} PARTURA_ENV_OPW=${PARTURA_ENV_OPW:-ts_spearman=0,nt_*=0}
PY=${PY:-/root/miniconda3/envs/quant/bin/python}
D=research/coldstart_C02
JOBS=$D/jobs_$ROUND.tsv
[ -f "$JOBS" ] || { echo "no $JOBS"; exit 2; }
mkdir -p logs
rm -f $D/$ROUND.DONE $D/$ROUND.exit
echo "[c02] round $ROUND started $(date +%F_%T); $(grep -cv '^\s*\(#\|$\)' $JOBS) jobs" > $D/$ROUND.log

run_one() {   # <tag> <idea> <guidance> <arms> <seed> [extra...]
  local tag=$1 idea=$2 g=$3 arms=$4 seed=$5; shift 5
  local log=logs/_idea_$tag.log
  timeout --signal=TERM --kill-after=60 ${JOB_MINUTES}m \
    $PY -u scripts/idea_search.py "$idea" --guidance "$g" --arms "$arms" --seed "$seed" --tag "$tag" "$@" > "$log" 2>&1
  local code=$?
  echo "[partura exit $code $(date +%F_%T)]" >> "$log"
  echo "$tag $code" >> research/coldstart_C02/$ROUND.exit
  echo "[c02] $tag exit $code $(date +%F_%T)" >> research/coldstart_C02/$ROUND.log
}
export -f run_one
export ROUND PY JOB_MINUTES PARTURA_HOME
# the disk guard (C01 PLAN §6 revision 2) must be running whenever jobs are
GUARD="env PARTURA_HOME=$PARTURA_HOME GUARD_DISK=${GUARD_DISK:-/root/autodl-tmp} scripts/server/c01_diskguard.sh"
if command -v screen >/dev/null; then
  screen -ls | grep -q "\.c01_guard[[:space:]]" || { rm -f research/coldstart_C01/guard.stop; screen -dmS c01_guard $GUARD; }
else                                   # a host without screen (the second server): tmux
  tmux has-session -t c01_guard 2>/dev/null || { mkdir -p research/coldstart_C01; rm -f research/coldstart_C01/guard.stop; tmux new-session -d -s c01_guard "$GUARD"; }
fi

grep -v '^\s*\(#\|$\)' $JOBS | xargs -P 2 -L 1 bash -c 'run_one "$@"' _
cp $D/$ROUND.exit $D/$ROUND.DONE
echo "[c02] round $ROUND finished $(date +%F_%T)" >> $D/$ROUND.log
