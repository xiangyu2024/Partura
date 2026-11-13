#!/bin/bash
cd /var/snap/docker/common/var-lib-docker/c02_partura/Partura
source tmp/w02l_env.sh
set -e
echo "start $(date +%F_%T)"
$PY -u scripts/w02l_combo.py prep
$PY -u scripts/w02l_combo.py build
$PY -u scripts/w02l_combo.py describe
echo "combo done $(date +%F_%T)"
