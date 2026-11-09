#!/bin/bash
# PROD W02L, server side: pick up a changed tmp/w02l_env.sh in the round machinery without losing work.  Stops the autobuilder,
# every keeper and every conductor (bash only), and the locates (minutes of work; their panels stay in the cache); GP missions
# (c05_round.py and its searches) keep running.  Then starts one keeper for every built stream and the autobuilder, both with
# the current env: a keeper restarts a stream's conductor once none of its runners is alive, and the conductor resumes.
#   bash scripts/server/w02l_restart_rounds.sh
cd /var/snap/docker/common/var-lib-docker/c02_partura/Partura
PYB=/home/user/anaconda3/envs/quant/bin/python
for p in $(pgrep -f "^bash scripts/server/w02l_autobuild.sh"); do kill $p; done
for p in $(pgrep -f "^bash scripts/server/prod_keeper.sh 20"); do kill $p; done
sleep 1
for p in $(pgrep -f "^bash scripts/server/prod_conductor.sh 20"); do kill $p; done
for p in $(pgrep -f "^$PYB -u scripts/c05_locate.py locate 20"); do kill $p; done
sleep 3
SEEDS=$(python3 -c "import json;print(' '.join(str(x['seed']) for x in json.load(open('research/prod_W02L/streams.json'))['streams']))")
(source tmp/w02l_env.sh && nohup bash scripts/server/prod_keeper.sh $SEEDS >> research/prod_W02L/keeper.out 2>&1 < /dev/null &)
(source tmp/w02l_env.sh && nohup bash scripts/server/w02l_autobuild.sh >> research/prod_W02L/autobuild.log 2>&1 < /dev/null &)
echo "restarted: keeper for $(echo $SEEDS | wc -w) streams, autobuild; missions running: $(pgrep -fc '[c]05_round.py mission')"
