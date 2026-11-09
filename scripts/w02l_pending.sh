#!/bin/bash
# PROD W02L, laptop side: which streams wait for the coordinator.  Prints "<k> <seeds...>" per round k: the streams whose locate of
# round k is READY on the server and whose plan for round k has not been pushed yet; then one summary line.
#   bash scripts/w02l_pending.sh
H="ssh -o ConnectTimeout=15 root@100.111.77.69"
R=/var/snap/docker/common/var-lib-docker/c02_partura/Partura/research/prod_W02L
$H "cd $R 2>/dev/null && for k in 1 2 3; do s=''; for f in \$(ls loc/*_P_r\$k.READY 2>/dev/null); do b=\$(basename \$f .READY); seed=\${b#s}; seed=\${seed%%_*}; [ -e arms/s\${seed}_P_r\$k.yaml ] || s=\"\$s \$seed\"; done; [ -n \"\$s\" ] && echo \"\$k\$s\"; done; echo \"built \$(python3 -c \"import json;print(len(json.load(open('streams.json'))['streams']))\" 2>/dev/null) alldone \$(ls arms/*.ALLDONE 2>/dev/null | wc -l) running_missions \$(pgrep -fc '[c]05_round.py mission')\""
