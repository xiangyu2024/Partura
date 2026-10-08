#!/bin/bash
# Old vs new AlphaCube side by side on the server (nothing in /root/autodl-tmp/AlphaCube is written):
#   base = the AlphaCube the server has been running;  new = <Partura>/vendor/AlphaCube-steering (branch partura-steering)
# Phases: a synthetic cube on $VERIFY_DEVICE (control first: base vs base), then the production store, read-only
# (store identity, the batch's 15 expressions + the known family on a real window, one GP and one RL run each way).
# A copy of the local harness in tmp/impl/verify_defaults, which could only be run on CPU.
#   bash scripts/server/ac_accept/run.sh            -> logs/_ac_accept.log, tmp/ac_accept/out/report_<phase>.json
R=/root/autodl-tmp/Partura
export VERIFY_PY=/root/miniconda3/envs/quant/bin/python
export VERIFY_BASE=${VERIFY_BASE:-/root/autodl-tmp/AlphaCube}
export VERIFY_NEW=${VERIFY_NEW:-$R/vendor/AlphaCube-steering}
export VERIFY_ROOT=$R/tmp/ac_accept
export VERIFY_DEVICE=${VERIFY_DEVICE:-cuda}
export VERIFY_FACTORS=$R/batches/B01_single_factors.yaml
PHASES=${*:-"self cross extra_self extra prod_self prod"}
mkdir -p "$VERIFY_ROOT" "$R/logs"
cd "$R/scripts/server/ac_accept" || exit 2
{
  echo "[accept $(date +%F_%T)] device $VERIFY_DEVICE | base $VERIFY_BASE | new $VERIFY_NEW ($(cat "$VERIFY_NEW/VERSION" 2>/dev/null))"
  [ -d "$VERIFY_ROOT/cube" ] || $VERIFY_PY verify.py build
  for ph in $PHASES; do
    echo "[accept $(date +%T)] phase $ph"
    $VERIFY_PY verify.py "$ph"
    echo "[accept $(date +%T)] phase $ph rc $?"
  done
  echo "[accept $(date +%F_%T)] done"
} > "$R/logs/_ac_accept.log" 2>&1
