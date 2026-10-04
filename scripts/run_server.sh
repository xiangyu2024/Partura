#!/bin/bash
# Run Partura stages on the AutoDL server, as a good neighbour:
#   - one engine evaluation on the GPU at a time (file lock); its share of the card follows what is
#     free at that moment and always leaves 4 GiB for the neighbours (GPU_FRAC=0 = auto)
#   - at most PARTURA_SLOTS Partura processes at once (default 2), two threads each
#   - ranks on the GPU (the CPU quota is usually taken by another job)
#   - the process exits by itself before memory becomes somebody else's problem
# usage:  scripts/run_server.sh <config.yaml> <stage> [<stage> ...]
#         EXTRA=--holdout scripts/run_server.sh <config.yaml> S_final      # the ONE holdout read
set -u
cd /root/autodl-tmp/Partura
export PYTHONPATH=/root/autodl-tmp/AlphaCube/src:/root/autodl-tmp/Partura
export ALPHACUBE_ROOT=/root/autodl-tmp/AlphaCube
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
export PARTURA_RANK_DEVICE=${PARTURA_RANK_DEVICE:-cuda}
export PARTURA_SLOTS=${PARTURA_SLOTS:-2}
export PARTURA_SELF_GB=${PARTURA_SELF_GB:-14}
export PARTURA_CGROUP_GB=${PARTURA_CGROUP_GB:-34}
export OMP_NUM_THREADS=2 MKL_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2
STORE=/root/autodl-tmp/qmt_daily_data/fast_factor_compute
MIRROR=/root/autodl-tmp/AlphaCube/mirror
CFG=$1; shift
nice -n 5 /root/miniconda3/envs/quant/bin/python -u -m partura.cli run "$CFG" \
  --store "$STORE" --mirror-root "$MIRROR" --device "${DEV:-cuda}" --gpu-fraction "${GPU_FRAC:-0}" \
  --batch "${BATCH:-3}" --torch-threads 2 \
  --workdir /root/autodl-tmp/Partura/tmp --out-root /root/autodl-tmp/Partura/runs \
  --stages "$@" ${EXTRA:-}
code=$?
echo "[partura exit $code $(date +%F_%T)]"
exit $code
