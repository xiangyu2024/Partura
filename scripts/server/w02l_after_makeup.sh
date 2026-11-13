#!/bin/bash
# W02L, after the GP makeup (LIBRARY_PLAN.md): wait for the two R groups and the first ruler-D pass, run ruler D on whatever is
# still missing (the R groups' outputs), rewrite report.md and the final D-head list, make the new heads' signals, score W, and
# build C_LXW and C_W (as is, then _ng on the same pools).  Fits only -- nothing of 2026 is read here.
cd /var/snap/docker/common/var-lib-docker/c02_partura/Partura
source tmp/w02l_env.sh
L=tmp/w2tl/after_makeup.log
say() { echo "[after] $* $(date +%F_%T)" >> $L; }
fail() { say "FAILED: $*"; exit 1; }
say "waiting for the R groups and D pass 1"
while pgrep -f "^$PY -u scripts/c05_locate.py direct" > /dev/null || pgrep -f "^$PY -u scripts/w02l_backtest.py" > /dev/null; do sleep 60; done
for s in 2075 2067; do grep -q "^wrote " logs/_prodR_makeup_s${s}_P_r3.log || fail "R group s$s did not write its file"; done
say "R groups and D pass 1 done; D pass 2"
$PY scripts/w02l_report.py --collect-d tmp/w2tl/d_makeup2.txt >> $L 2>&1 || fail "collect-d"
if [ -s tmp/w2tl/d_makeup2.txt ]; then
  $PY -u scripts/w02l_backtest.py tmp/w2tl/d_makeup2.txt --d-jsonl research/prod_W02L/d_scores.jsonl > tmp/w2tl/d_makeup2.log 2>&1 || fail "D pass 2"
fi
$PY scripts/w02l_report.py --collect-d tmp/w2tl/d_left.txt >> $L 2>&1
[ -s tmp/w2tl/d_left.txt ] && fail "candidates still without D: $(wc -l < tmp/w2tl/d_left.txt)"
say "D complete; report and the final D-head list"
$PY scripts/w02l_report.py > research/prod_W02L/report.md.new 2>> $L && mv research/prod_W02L/report.md.new research/prod_W02L/report.md || fail "report"
[ -f research/prod_W02L/library/heads_D_dryrun.json ] || cp research/prod_W02L/library/heads_D.json research/prod_W02L/library/heads_D_dryrun.json
$PY scripts/w02l_report.py --heads-json research/prod_W02L/library/heads_D.json >> $L 2>&1 || fail "heads-json"
say "heads: $($PY -c 'import json;print(len(json.load(open("research/prod_W02L/library/heads_D.json"))))')"
export PARTURA_GPU_LOCK=gpusig PARTURA_GPUSIG_WAYS=1 PARTURA_THREADS=4
for k in 0 1 2 3; do
  $PY -u scripts/w02l_two_level.py signals --pool W --shard $k/4 --device cuda > tmp/w2tl/signals_W2_$k.log 2>&1 &
done
wait
unset PARTURA_GPU_LOCK PARTURA_GPUSIG_WAYS
say "W signals done; scoring W"
$PY -u scripts/w02l_two_level.py score --pools W --allow-missing --keep-cut > tmp/w2tl/score_W.log 2>&1 || fail "score W"
say "building C_LXW, C_W (as is)"
$PY -u scripts/w02l_two_level.py build --pools LXW,W --variants as_is --allow-missing > tmp/w2tl/build_LXW_as_is.log 2>&1 || fail "build as is"
say "building C_LXW_ng, C_W_ng"
$PY -u scripts/w02l_two_level.py build --pools LXW,W --variants _ng --allow-missing --reuse-pool > tmp/w2tl/build_LXW__ng.log 2>&1 || fail "build _ng"
say "ALL BUILT"
