#!/bin/bash
# C08 (PLAN §5), laptop side: before the final read, copy what the old host holds for seeds 801, 803, 804, 805 to the new host --
# evidence, the run logs (c05_lib.finished reads them), the arm files and locate outputs.  No panels, no values.
set -e
SP=${SCRATCH:-/tmp}
OLD="ssh -o ConnectTimeout=15 -p 29982 root@connect.westd.seetacloud.com"
NEW="ssh root@100.111.77.69"
OR=/root/autodl-tmp/Partura; NR=/var/snap/docker/common/var-lib-docker/c02_partura/Partura
for i in 1 2 3 4 5 6; do
  $OLD "cd $OR && for s in 801 803 804 805; do [ -e research/coldstart_C08/arms/s\$s.ALLDONE ] || { echo \"s\$s not finished\" >&2; exit 3; }; done;
        tar czf - \$(ls -d episodes/c08s80[1345]*/evidence.json episodes/c08s80[1345]*/*/checkpoints/archive_gen*.csv logs/_idea_c08s80[1345]*.log \
                         research/coldstart_C08/arms/*s80[1345]_* research/coldstart_C08/arms/s80[1345].ALLDONE research/coldstart_C08/loc/s80[1345]_* research/coldstart_C08/guidance/s80[1345]_* \
                         2>/dev/null)" > $SP/c08_gather.tgz \
    && tar tzf $SP/c08_gather.tgz > $SP/c08_gather.list && break
  sleep 15
done
n=$(grep -c "evidence.json" $SP/c08_gather.list)
echo "packed $(wc -l < $SP/c08_gather.list) files, $n evidence files (expected 4 seeds x 3 rounds x 2 slots = 24)"
grep -q "s80[2678]" $SP/c08_gather.list && { echo "refusing: new-host seeds in the bundle"; exit 4; }
$NEW "cd $NR && tar xzf - && ls episodes | grep -c '^c08s80[1-8]'" < $SP/c08_gather.tgz
