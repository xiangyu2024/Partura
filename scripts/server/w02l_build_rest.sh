#!/bin/bash
# W02L: the rest of after_makeup.sh once the stale fingerprint caches are dropped on pool rewrite -- C_LXW, C_W (as is), then
# their _ng on the same pools, then a --dry read with the real syntheses (nothing of 2026).
cd /var/snap/docker/common/var-lib-docker/c02_partura/Partura
source tmp/w02l_env.sh
L=tmp/w2tl/after_makeup.log
say() { echo "[after] $* $(date +%F_%T)" >> $L; }
fail() { say "FAILED: $*"; exit 1; }
say "restart: building C_LXW, C_W (as is) with fresh fingerprints"
$PY -u scripts/w02l_two_level.py build --pools LXW,W --variants as_is --allow-missing > tmp/w2tl/build_LXW_as_is.log 2>&1 || fail "build as is"
say "building C_LXW_ng, C_W_ng"
$PY -u scripts/w02l_two_level.py build --pools LXW,W --variants _ng --allow-missing --reuse-pool > tmp/w2tl/build_LXW__ng.log 2>&1 || fail "build _ng"
say "ALL BUILT; read --dry"
$PY -u scripts/w02l_two_level.py read --dry > tmp/w2tl/read_dry2.log 2>&1 || fail "read --dry"
say "DRY OK"
