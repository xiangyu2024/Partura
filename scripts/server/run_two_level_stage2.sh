#!/bin/bash
# Server side: stage 2 of research/two_level/PLAN.md (scripts/two_level_forward.py): rebuild the champions on the extended
# view from their own families, check them against the stored signals, read the forward segment for those that pass.
#   WAIT_FOR="ext2" screen -dmS tl2 scripts/server/run_two_level_stage2.sh
# CPU only.  Log: logs/_two_level_stage2.log.  `./scripts/study.sh code` first.
cd /root/autodl-tmp/Partura
export PYTHONPATH=/root/autodl-tmp/AlphaCube/src:/root/autodl-tmp/Partura ALPHACUBE_ROOT=/root/autodl-tmp/AlphaCube OMP_NUM_THREADS=8 MKL_NUM_THREADS=8 PARTURA_RANK_DEVICE=cpu PARTURA_SLOTS=4 PARTURA_GPU_WAYS=2
PY=/root/miniconda3/envs/quant/bin/python
for s in $WAIT_FOR; do while screen -ls | grep -q "\.${s}[[:space:]]"; do sleep 30; done; done
echo "[tl2 $(date +%F_%T)] start" > logs/_two_level_stage2.log
$PY -u scripts/two_level_forward.py "$@" >> logs/_two_level_stage2.log 2>&1
echo "[tl2 $(date +%F_%T)] exit $?" >> logs/_two_level_stage2.log
