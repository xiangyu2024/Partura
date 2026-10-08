#!/bin/bash
# Server side: one idea search per seed, one after another, on one GPU way.  Lives in the repo so that
# `./scripts/study.sh code` puts the launcher and the code it starts on the server in the same sync.
#
#   screen -dmS <name> scripts/server/run_idea_seeds.sh <idea> <tag-prefix> "<seeds>" [idea_search options ...]
#   e.g.  screen -dmS e6a scripts/server/run_idea_seeds.sh I7_beyond_liquidity e6b "1 3" --budget 384 --population 48 --halflives 0,5,20,60 --threshold 0.75
#
# Each run writes episodes/<prefix><seed>_<idea>/ and logs/_idea_<prefix><seed>_<idea>.log; a line per finished run goes to logs/_<prefix>.log.
# WAIT_FOR=<screen name> makes it wait until that screen is gone before starting (to queue behind another launcher).
cd /root/autodl-tmp/Partura
export PYTHONPATH=/root/autodl-tmp/AlphaCube/src:/root/autodl-tmp/Partura ALPHACUBE_ROOT=/root/autodl-tmp/AlphaCube OMP_NUM_THREADS=8 MKL_NUM_THREADS=8 \
       PARTURA_RANK_DEVICE=cuda PARTURA_REWARD_DEVICE=cuda PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True PARTURA_SLOTS=4 PARTURA_GPU_WAYS=2 PARTURA_MEM_WAIT_S=10800
PY=/root/miniconda3/envs/quant/bin/python
idea=$1; prefix=$2; seeds=$3; shift 3
if [ -n "$WAIT_FOR" ]; then while screen -ls | grep -q "\.${WAIT_FOR}[[:space:]]"; do sleep 30; done; fi
for seed in $seeds; do
  $PY -u scripts/idea_search.py "$idea" --tag "${prefix}${seed}" --seed "$seed" "$@" > "logs/_idea_${prefix}${seed}_${idea}.log" 2>&1
  echo "[$prefix] ${prefix}${seed} exit $? $(date +%F_%T)" >> "logs/_${prefix}.log"
done
