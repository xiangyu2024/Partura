#!/bin/bash
# W02L SYNTH_PLAN.md: build S (fit to 2025-12-31) and S_nested (fit to 2023-08-07) side by side, then the in-sample description.
cd /var/snap/docker/common/var-lib-docker/c02_partura/Partura
source tmp/w02l_env.sh
export PARTURA_THREADS=16
$PY -u scripts/w02l_synth.py build --fit-end 20251231 > tmp/w2tl/synth_S.log 2>&1 &
$PY -u scripts/w02l_synth.py build --fit-end 20230807 > tmp/w2tl/synth_S_nested.log 2>&1 &
wait
$PY -u scripts/w02l_synth.py describe > tmp/w2tl/synth_describe.log 2>&1
echo "synth done $(date +%F_%T)" >> tmp/w2tl/synth_describe.log
