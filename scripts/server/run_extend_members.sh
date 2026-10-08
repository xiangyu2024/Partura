#!/bin/bash
# Server side: member factors of the champions on the extended view (scripts/extend_members.py) -- values only, hours of GPU.
#   WAIT_FOR="e7c e7b e7l" screen -dmS ext1 scripts/server/run_extend_members.sh base
#   WAIT_FOR="tl1 ext1"    screen -dmS ext2 scripts/server/run_extend_members.sh new
# Waits until every screen named in WAIT_FOR is gone.  Log: logs/_extend_members_<set>.log.  `./scripts/study.sh code` first.
cd /root/autodl-tmp/Partura
export PYTHONPATH=/root/autodl-tmp/AlphaCube/src:/root/autodl-tmp/Partura ALPHACUBE_ROOT=/root/autodl-tmp/AlphaCube OMP_NUM_THREADS=8 MKL_NUM_THREADS=8 \
       PARTURA_RANK_DEVICE=cuda PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True PARTURA_SLOTS=4 PARTURA_GPU_WAYS=2 PARTURA_MEM_WAIT_S=10800 \
       PARTURA_GPU_MAX_FRAC=0.85      # the card is ours once the searches are done: heavy hand-written members need more than the shared 45%
PY=/root/miniconda3/envs/quant/bin/python
for s in $WAIT_FOR; do while screen -ls | grep -q "\.${s}[[:space:]]"; do sleep 30; done; done
B=/root/autodl-tmp/AlphaCube/_bench/trainto
P=/root/autodl-tmp/Partura/pools
# $1 = which set: "base" (the two existing champions; needs nothing from stage 1) or "new" (the five stage-1 signals plus the two)
SET=${1:-new}
LOG=logs/_extend_members_${SET}.log
BASE="手写库冠军=$B/legacy:$B/legacy_signal.families.json 挖掘冠军=$B/allfac_buyable:$B/champion_signal_buyable.families.json"
NEW="C_Q=$P/Q:$P/signals/C_Q.families.json C_LQ=$P/LQ:$P/signals/C_LQ.families.json C_MQ=$P/MQ:$P/signals/C_MQ.families.json C_LM=$P/LM:$P/signals/C_LM.families.json C_LMQ=$P/LMQ:$P/signals/C_LMQ.families.json"
echo "[ext $(date +%F_%T)] start $SET" > $LOG
if [ "$SET" = base ]; then
  $PY -u scripts/extend_members.py $BASE --out runs/_forward/members_base.json >> $LOG 2>&1
else
  $PY -u scripts/extend_members.py $BASE $NEW >> $LOG 2>&1
fi
echo "[ext $(date +%F_%T)] exit $?" >> $LOG
