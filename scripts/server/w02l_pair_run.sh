#!/bin/bash
cd /var/snap/docker/common/var-lib-docker/c02_partura/Partura
source tmp/w02l_env.sh
echo "start $(date +%F_%T)"
$PY -u scripts/w02l_pair.py && echo "pair done $(date +%F_%T)" || echo "pair FAILED $(date +%F_%T)"
