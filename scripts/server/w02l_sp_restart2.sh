#!/bin/bash
# W02L: start one stealing GPU ts_spearman worker once the last regular round (2080 r3) has been pushed and at most 2 GP
# searches are alive -- so the tail's locates and correlation tables (which need the card) are not pushed to the CPU.
cd /var/snap/docker/common/var-lib-docker/c02_partura/Partura
source tmp/w02l_env.sh
until [ -e research/prod_W02L/arms/s2080_P_r3.yaml ] && [ "$(pgrep -fc "^$PY -u scripts/idea_search.py")" -le 2 ]; do sleep 60; done
echo "[sp] 2080 r3 pushed and <=2 GP searches alive; GPU spearman worker starts $(date +%F_%T)"
export PARTURA_GPU_LOCK=gpus0 PARTURA_GPUS0_WAYS=1
exec $PY -u scripts/w02l_stage0.py research/prod_W02L/struct/members.csv research/prod_W02L/stage0 --device cuda --spearman-only --steal-min 30
