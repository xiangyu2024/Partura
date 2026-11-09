#!/bin/bash
# PROD W02L: one screen of progress (server).  bash scripts/w02l_status.sh
cd "$(dirname "$0")/.." || exit 1
S=research/prod_W02L/stage0
n=$(ls $S/chunks 2>/dev/null | grep -c '\.jsonl$'); tot=$(( ($(wc -l < research/prod_W02L/struct/members.csv) - 1 + 7) / 8 ))
echo "stage0: $n / $tot chunks ($(( 100 * n / tot ))%), workers $(pgrep -fc '^/home/user/anaconda3/envs/quant/bin/python -u scripts/w02l_stage0.py')"
for f in logs/_w02l_s0_*.log; do echo "  $(basename $f .log): $(grep -c '^\[s0\] chunk' $f) chunks; $(grep '^\[s0\]' $f | tail -n 1 | cut -c1-90)"; done
cat $S/chunks/*.jsonl 2>/dev/null | python3 -c "
import sys, json
r=[json.loads(x) for x in sys.stdin if x.strip()]
g=[x for x in r if x.get('gate')]
print(f'  scored {len(r)}: errors {sum(\"error\" in x for x in r)}, gate {len(g)}, heads A {sum(x.get(\"discovery_A\",False) for x in g)}, B {sum(x.get(\"discovery_B\",False) for x in g)}')"
free -g | awk 'NR==2{print "  mem used "$3" GB, available "$7" GB"}'; nvidia-smi --query-gpu=memory.used,utilization.gpu --format=csv,noheader | sed 's/^/  gpu /'
