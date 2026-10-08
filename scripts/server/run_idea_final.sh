#!/bin/bash
# Server side: the rule-based out-of-sample read of what idea searches found (scripts/idea_final.py), with the forward column.
#   WAIT_FOR=<screen> screen -dmS ifin scripts/server/run_idea_final.sh <episode> [<episode> ...] [--top 1]
# Log: logs/_idea_final.log.  Run `./scripts/study.sh code` on the Mac first.
cd /root/autodl-tmp/Partura
export PYTHONPATH=/root/autodl-tmp/AlphaCube/src:/root/autodl-tmp/Partura ALPHACUBE_ROOT=/root/autodl-tmp/AlphaCube OMP_NUM_THREADS=8 MKL_NUM_THREADS=8 \
       PARTURA_RANK_DEVICE=cuda PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True PARTURA_SLOTS=4 PARTURA_GPU_WAYS=2 PARTURA_MEM_WAIT_S=10800
PY=/root/miniconda3/envs/quant/bin/python
if [ -n "$WAIT_FOR" ]; then while screen -ls | grep -q "\.${WAIT_FOR}[[:space:]]"; do sleep 20; done; fi
$PY -u scripts/idea_final.py "$@" > logs/_idea_final.log 2>&1
echo "[partura exit $? $(date +%F_%T)]" >> logs/_idea_final.log
