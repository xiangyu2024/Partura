#!/bin/bash
# W02L: the GPU spearman worker with most of the card (the card is empty between the last round and the makeup).
cd /var/snap/docker/common/var-lib-docker/c02_partura/Partura
source tmp/w02l_env.sh
O=research/prod_W02L/stage0
for p in $(pgrep -f "^$PY -u scripts/w02l_stage0.py .*--device cuda"); do echo "stop GPU worker $p"; kill -9 $p; done
sleep 3
for c in $O/claims/sp*; do
  k=$(basename $c); [ -f $O/chunks/$k.jsonl ] && continue
  who=$(cat $c); pid=${who%% *}
  case "$who" in *cuda*) [ -d /proc/$pid ] || { echo "release $k ($who)"; mv $c $O/claims/.released4_$k; };; esac
done
echo "[sp] GPU spearman worker with PARTURA_S0_GPU_FRACTION=0.9 starts $(date +%F_%T)"
export PARTURA_GPU_LOCK=gpus0 PARTURA_GPUS0_WAYS=1 PARTURA_S0_GPU_FRACTION=0.9
exec $PY -u scripts/w02l_stage0.py research/prod_W02L/struct/members.csv research/prod_W02L/stage0 --device cuda --spearman-only --steal-min 30
