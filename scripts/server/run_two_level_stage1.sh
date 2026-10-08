#!/bin/bash
# Server side: stage 1 of research/two_level/PLAN.md -- the two-level method on pools that contain Partura's signals.
# CPU only (every panel is cached).  Run `./scripts/study.sh code` on the Mac first.  Log: logs/_two_level_stage1.log
cd /root/autodl-tmp/Partura
export PYTHONPATH=${PARTURA_AC:-/root/autodl-tmp/Partura/vendor/AlphaCube-steering}/src:/root/autodl-tmp/Partura ALPHACUBE_ROOT=${PARTURA_AC:-/root/autodl-tmp/Partura/vendor/AlphaCube-steering} OMP_NUM_THREADS=8 MKL_NUM_THREADS=8 PARTURA_RANK_DEVICE=cpu PARTURA_SLOTS=4 PARTURA_GPU_WAYS=2
PY=/root/miniconda3/envs/quant/bin/python
B=/root/autodl-tmp/AlphaCube/_bench
L=logs/_two_level_stage1.log
say() { echo "[stage1 $(date +%T)] $*" >> $L; }
: > $L
say "export Q";  $PY -u scripts/two_level.py export Q studies/_pools/Q_s4_candidates.json >> $L 2>&1 || { say "export failed"; exit 1; }
say "score Q";   $PY -u scripts/two_level.py score Q >> $L 2>&1 || { say "score failed"; exit 1; }
say "merge";     $PY -u scripts/two_level.py merge LQ  $B/trainto/legacy Q >> $L 2>&1 \
              && $PY -u scripts/two_level.py merge MQ  $B/trainto/allfac_buyable Q >> $L 2>&1 \
              && $PY -u scripts/two_level.py merge LM  $B/trainto/legacy $B/trainto/allfac_buyable >> $L 2>&1 \
              && $PY -u scripts/two_level.py merge LMQ $B/trainto/legacy $B/trainto/allfac_buyable Q >> $L 2>&1 || { say "merge failed"; exit 1; }
for job in "Q C_Q" "LQ C_LQ" "MQ C_MQ" "LM C_LM" "LMQ C_LMQ"; do
  set -- $job
  say "build $2 from pool $1"
  $PY -u scripts/two_level.py build $1 $2 --compare 手写库冠军=$B/trainto/legacy_signal.npy --compare 挖掘冠军=$B/trainto/champion_signal_buyable.npy >> $L 2>&1 || say "build $2 FAILED"
done
say "evaluate"
$PY -u scripts/signal_books.py 手写库冠军=$B/trainto/legacy_signal.npy 挖掘冠军=$B/trainto/champion_signal_buyable.npy C_Q=pools/signals/C_Q.npy C_LQ=pools/signals/C_LQ.npy \
    C_MQ=pools/signals/C_MQ.npy C_LM=pools/signals/C_LM.npy C_LMQ=pools/signals/C_LMQ.npy --out runs/_batch_B01/two_level_stage1.json >> $L 2>&1
say "done exit $?"
