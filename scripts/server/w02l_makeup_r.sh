#!/bin/bash
# W02L MAKEUP.md "补评 R 组": the two R groups the finalize step dropped by mistake, evaluated after every round (and the GP makeup) ended.
# 2075 r3 had no R file; 2067 r3's R file held only the Amt group, so it is rerun with both groups (the old file kept as .pre_makeup).
cd /var/snap/docker/common/var-lib-docker/c02_partura/Partura
source tmp/w02l_env.sh
A=research/prod_W02L/arms
[ -f $A/s2067_P_r3_R.json.pre_makeup ] || cp $A/s2067_P_r3_R.json $A/s2067_P_r3_R.json.pre_makeup
export PARTURA_GPU_WAYS=2
for s in 2075 2067; do
  nohup $PY -u scripts/c05_locate.py direct $s P 3 $A/rreq_makeup_s${s}_P_r3.json > logs/_prodR_makeup_s${s}_P_r3.log 2>&1 < /dev/null &
done
# ruler D for the GP makeup's candidates (the R groups' get theirs in a second pass)
$PY scripts/w02l_report.py --collect-d tmp/w2tl/d_makeup1.txt
wc -l tmp/w2tl/d_makeup1.txt
nohup $PY -u scripts/w02l_backtest.py tmp/w2tl/d_makeup1.txt --d-jsonl research/prod_W02L/d_scores.jsonl > tmp/w2tl/d_makeup1.log 2>&1 < /dev/null &
echo "started $(date +%F_%T)"
