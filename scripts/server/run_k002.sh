#!/bin/bash
# Server side: the K002 batch (studies/K002_daily_fields) -- the sweep of its hand-written hypotheses, then the DRY RUN of the
# reading rule.  The real out-of-sample read is NOT queued here: it happens once, by hand, after the dry run has been looked at
# (see the end of this file).
#   WAIT_FOR=<screen> TAG=s1 screen -dmS k002 scripts/server/run_k002.sh
# Steps (each stops the chain if it fails):
#   1. scripts/check_hypo.py studies/K002_daily_fields/hypo.yaml      -> logs/K002_daily_fields_<tag>_hypo.log
#   2. scripts/sweep.py K002_daily_fields --only-extra --max 400      -> logs/K002_daily_fields_<tag>.log, runs/K002_daily_fields/sweep_<tag>.json
#   3. scripts/group_final.py K002_daily_fields --dry-run             -> logs/K002_daily_fields_<tag>_dry.log, runs/K002_daily_fields/group_select_<tag>.json
# The logs end with the "[partura exit N ...]" line `study.sh wait` / `study.sh list` look for, so
#   ./scripts/study.sh wait K002_daily_fields s1        and        ./scripts/study.sh wait K002_daily_fields s1_dry
# work.  Run `./scripts/study.sh code` on the Mac first (it syncs partura/, scripts/, configs/); studies/K002_daily_fields/ goes up
# with `./scripts/study.sh hypo K002_daily_fields`.
#
# The dry run picks from the sweep by the README's rule using in-sample days only, checks that the in-sample books reproduce on the
# extended view, and PRINTS the selection; it reads nothing out of sample and writes no ledger entry.  It does compute the picked
# and candidate expressions on the view to the store's last day (values only), so the real read afterwards is cache hits.  The real read:
#   cd /root/autodl-tmp/Partura && <the environment below> /root/miniconda3/envs/quant/bin/python -u scripts/group_final.py K002_daily_fields --sweep s1 \
#       > logs/K002_daily_fields_s1_read.log 2>&1       # refuses a second time for the same tag (--again to override)
cd /root/autodl-tmp/Partura
export PYTHONPATH=${PARTURA_AC:-/root/autodl-tmp/Partura/vendor/AlphaCube-steering}/src:/root/autodl-tmp/Partura ALPHACUBE_ROOT=${PARTURA_AC:-/root/autodl-tmp/Partura/vendor/AlphaCube-steering} \
       PARTURA_RANK_DEVICE=cuda PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True PARTURA_SLOTS=${PARTURA_SLOTS:-4} PARTURA_GPU_WAYS=${PARTURA_GPU_WAYS:-2} PARTURA_MEM_WAIT_S=10800
PY=/root/miniconda3/envs/quant/bin/python
FID=K002_daily_fields
TAG=${TAG:-s1}
HYPO=studies/$FID/hypo.yaml
mkdir -p logs
if [ -n "$WAIT_FOR" ]; then while screen -ls | grep -q "\.${WAIT_FOR}[[:space:]]"; do sleep 20; done; fi

# 1. the hypotheses parse (a sweep that drops a ruler silently is worse than one that does not start)
$PY scripts/check_hypo.py $HYPO > logs/${FID}_${TAG}_hypo.log 2>&1
code=$?; echo "[partura exit $code $(date +%F_%T)]" >> logs/${FID}_${TAG}_hypo.log
[ $code -eq 0 ] || exit $code

# 2. the sweep: the three benchmarks plus the hypotheses, nothing generated; two threads per worker, as study.sh runs sweeps.
#    --max 400: the file has 189 entries and the default cap (260) would also do, but --only-extra stops with an error if a cap would ever drop one
OMP_NUM_THREADS=2 MKL_NUM_THREADS=2 nice -n 5 $PY -u scripts/sweep.py $FID --tag $TAG --extra $HYPO --only-extra --max 400 > logs/${FID}_${TAG}.log 2>&1
code=$?; echo "[partura exit $code $(date +%F_%T)]" >> logs/${FID}_${TAG}.log
[ $code -eq 0 ] || exit $code

# 3. the dry run of the reading rule (selection + reproduction check, in-sample only)
OMP_NUM_THREADS=8 MKL_NUM_THREADS=8 $PY -u scripts/group_final.py $FID --sweep $TAG --dry-run > logs/${FID}_${TAG}_dry.log 2>&1
code=$?; echo "[partura exit $code $(date +%F_%T)]" >> logs/${FID}_${TAG}_dry.log
exit $code
