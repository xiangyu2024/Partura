#!/bin/bash
# W02L: ts_spearman makeup with member-named chunks (w02l_stage0.py tag() fixed): stop every spearman worker (they number by
# position), drop their claims, start one GPU worker on the near-empty card.
cd /var/snap/docker/common/var-lib-docker/c02_partura/Partura
source tmp/w02l_env.sh
O=research/prod_W02L/stage0
for p in $(pgrep -f "^$PY -u scripts/w02l_stage0.py .*--spearman-only"); do echo "stop spearman worker $p"; kill -9 $p; done
sleep 3
mkdir -p $O/claims_old_sp
for c in $O/claims/sp*; do [ -e "$c" ] && mv "$c" $O/claims_old_sp/; done
echo "[sp] one GPU worker, member-named chunks, PARTURA_S0_GPU_FRACTION=0.9, starts $(date +%F_%T)"
export PARTURA_GPU_LOCK=gpus0 PARTURA_GPUS0_WAYS=1 PARTURA_S0_GPU_FRACTION=0.9
exec $PY -u scripts/w02l_stage0.py research/prod_W02L/struct/members.csv research/prod_W02L/stage0 --device cuda --spearman-only
