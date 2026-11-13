#!/bin/bash
# W02L: a ts_spearman tree needs most of the card (it did not fit beside 2 GP searches), so: stop the GPU spearman worker,
# release its claims, and start it again once all 240 rounds have ended and no GP search is alive (before the makeup starts).
cd /var/snap/docker/common/var-lib-docker/c02_partura/Partura
source tmp/w02l_env.sh
O=research/prod_W02L/stage0
for p in $(pgrep -f "^$PY -u scripts/w02l_stage0.py .*--device cuda"); do echo "stop GPU worker $p"; kill -9 $p; done
sleep 1
for c in $O/claims/sp*; do
  k=$(basename $c); [ -f $O/chunks/$k.jsonl ] && continue
  who=$(cat $c); pid=${who%% *}
  case "$who" in *cuda*) kill -0 $pid 2>/dev/null || { echo "release $k ($who)"; mv $c $O/claims/.released2_$k; };; esac
done
until [ "$(ls research/prod_W02L/arms/s*_P_r?.DONE | wc -l)" -ge 240 ] && [ "$(pgrep -fc "^$PY -u scripts/idea_search.py")" -eq 0 ]; do sleep 60; done
echo "[sp] all 240 rounds ended and no GP search alive; GPU spearman worker starts $(date +%F_%T)"
export PARTURA_GPU_LOCK=gpus0 PARTURA_GPUS0_WAYS=1
exec $PY -u scripts/w02l_stage0.py research/prod_W02L/struct/members.csv research/prod_W02L/stage0 --device cuda --spearman-only --steal-min 30
