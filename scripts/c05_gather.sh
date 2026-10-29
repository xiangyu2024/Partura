#!/bin/bash
# C05 (PLAN revision 9 / 11), laptop side: before the final read, copy what the old host holds for seeds 801, 803, 804 to the new host.
# 802 is NOT copied: from round 3 on it lives on the new host, whose copies of its round-2 files carry the R reruns (PLAN revision 11);
# the old host's copies are stale.  Only evidence, the run logs (c05_lib.finished reads them), the arm files, locate outputs and the
# mission guidance travel -- no panels, no values.
set -e
SP=${SCRATCH:-/tmp}
OLD="ssh -o ConnectTimeout=15 -p 29982 root@connect.westd.seetacloud.com"
NEW="ssh root@100.111.77.69"
OR=/root/autodl-tmp/Partura; NR=/var/snap/docker/common/var-lib-docker/c02_partura/Partura
for i in 1 2 3 4 5 6; do
  $OLD "cd $OR && for s in 801 803 804; do [ -e research/coldstart_C05/arms/s\$s.ALLDONE ] || { echo \"s\$s not finished\" >&2; exit 3; }; done;
        tar czf - \$(ls -d episodes/c05s80[134]*/evidence.json episodes/c05s80[134]*/*/checkpoints/archive_gen*.csv logs/_idea_c05s80[134]*.log \
                         research/coldstart_C05/arms/*s80[134]_* research/coldstart_C05/arms/s80[134].ALLDONE research/coldstart_C05/loc/s80[134]_* \
                         research/coldstart_C05/guidance/s80[134]_* research/coldstart_C05/m/lib_s80[134]_* 2>/dev/null)" > $SP/c05_gather.tgz \
    && tar tzf $SP/c05_gather.tgz > $SP/c05_gather.list && break
  sleep 15
done
n=$(grep -c "evidence.json" $SP/c05_gather.list)
echo "packed $(wc -l < $SP/c05_gather.list) files, $n evidence files (expected 3 seeds x (4 M + 3 rounds x 6 jobs) = 66)"
grep -q "s802" $SP/c05_gather.list && { echo "refusing: 802 files in the bundle"; exit 4; }
$NEW "cd $NR && tar xzf - && ls episodes | grep -c '^c05s80[1-8][MAB]'" < $SP/c05_gather.tgz
