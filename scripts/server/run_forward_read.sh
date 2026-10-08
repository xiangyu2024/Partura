#!/bin/bash
# Server side: the forward-segment read (scripts/forward_read.py; the rule is research/forward_2026/PLAN.md).
#   WAIT_FOR=<screen> screen -dmS fwd scripts/server/run_forward_read.sh [forward_read options]
# Log: logs/_forward_read.log.  Run `./scripts/study.sh code` on the Mac first.
cd /root/autodl-tmp/Partura
export PYTHONPATH=${PARTURA_AC:-/root/autodl-tmp/Partura/vendor/AlphaCube-steering}/src:/root/autodl-tmp/Partura ALPHACUBE_ROOT=${PARTURA_AC:-/root/autodl-tmp/Partura/vendor/AlphaCube-steering} OMP_NUM_THREADS=8 MKL_NUM_THREADS=8 \
       PARTURA_RANK_DEVICE=cuda PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True PARTURA_SLOTS=4 PARTURA_GPU_WAYS=2 PARTURA_MEM_WAIT_S=10800
PY=/root/miniconda3/envs/quant/bin/python
if [ -n "$WAIT_FOR" ]; then while screen -ls | grep -q "\.${WAIT_FOR}[[:space:]]"; do sleep 20; done; fi
$PY -u scripts/forward_read.py "$@" > logs/_forward_read.log 2>&1
echo "[partura exit $? $(date +%F_%T)]" >> logs/_forward_read.log
