#!/bin/bash
# W02L: ruler D for the GP makeup's 110 candidates in 3 shards (the single process from w02l_makeup_r.sh is stopped after the
# shards start, so the after-makeup pipeline never sees a moment with no D process).  Lines of a chunk go out in one append.
cd /var/snap/docker/common/var-lib-docker/c02_partura/Partura
source tmp/w02l_env.sh
old=$(pgrep -f "^$PY -u scripts/w02l_backtest.py tmp/w2tl/d_makeup1.txt")
$PY - <<'PYEOF'
L = [x for x in open("tmp/w2tl/d_makeup1.txt", encoding="utf-8") if x.strip()]
for k in range(3):
    open(f"tmp/w2tl/d_makeup1_s{k}.txt", "w", encoding="utf-8").write("".join(L[k::3]))
PYEOF
for k in 0 1 2; do
  nohup $PY -u scripts/w02l_backtest.py tmp/w2tl/d_makeup1_s$k.txt --d-jsonl research/prod_W02L/d_scores.jsonl > tmp/w2tl/d_makeup1_s$k.log 2>&1 < /dev/null &
done
sleep 5
for p in $old; do echo "stop the single D process $p"; kill $p; done
