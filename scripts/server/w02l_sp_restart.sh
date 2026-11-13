#!/bin/bash
# W02L: release the ts_spearman claims of dead GPU workers, then start one stealing GPU worker once at most 1 GP search is alive.
cd /var/snap/docker/common/var-lib-docker/c02_partura/Partura
source tmp/w02l_env.sh
O=research/prod_W02L/stage0
for c in $O/claims/sp*; do
  k=$(basename $c); [ -f $O/chunks/$k.jsonl ] && continue
  who=$(cat $c); pid=${who%% *}
  case "$who" in *cuda*) kill -0 $pid 2>/dev/null || { echo "release $k ($who)"; mv $c $O/claims/.released_$k; };; esac
done
echo "claims now: $(ls $O/claims | grep -c '^sp'), chunks done: $(ls $O/chunks | grep -c '^sp')"
until [ "$(pgrep -fc "^$PY -u scripts/idea_search.py")" -le 1 ]; do sleep 60; done
echo "[sp] GP at <=1 search, GPU spearman worker starts $(date +%F_%T)"
export PARTURA_GPU_LOCK=gpus0 PARTURA_GPUS0_WAYS=1
exec $PY -u scripts/w02l_stage0.py research/prod_W02L/struct/members.csv research/prod_W02L/stage0 --device cuda --spearman-only --steal-min 30
