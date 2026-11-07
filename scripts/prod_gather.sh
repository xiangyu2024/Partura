#!/bin/bash
# PROD W01, laptop side (as scripts/c08_gather.sh): before the final read, copy what the OLD host holds for its seeds (909-912 in
# research/prod_W01/hosts.json) to the NEW host -- evidence, the run logs (c05_lib.finished reads them), the archives of the last
# checkpoints (c05_lib.archive), the arm files, the locate outputs, the M chains' ban libraries.  No panels, no values.
# Refuses unless every one of those seeds has arms/s<seed>.ALLDONE on the old host, and never ships a new-host seed.
# The tar stream passes through this machine ($SCRATCH, default /tmp) and is unpacked INSIDE the new host's Partura home only.
#   scripts/prod_gather.sh
set -e
REPO=$(cd "$(dirname "$0")/.." && pwd)
PYL=${PYL:-/Users/wxy/.venvs/alphacube/bin/python}; [ -x "$PYL" ] || PYL=python3
HOSTS="$PYL $REPO/scripts/prod_hosts.py"
DIR=$($HOSTS dir)
SP=${SCRATCH:-/tmp}
OLDSEEDS="$($HOSTS seeds old)"; NEWSEEDS="$($HOSTS seeds new)"
OLD="$($HOSTS hostssh old)"; NEW="$($HOSTS hostssh new)"
OR="$($HOSTS hosthome old)"; NR="$($HOSTS hosthome new)"
[ -n "$OLDSEEDS" ] || { echo "no seeds on the old host"; exit 1; }
for i in 1 2 3 4 5 6; do
  $OLD "cd $OR && for s in $OLDSEEDS; do [ -e research/$DIR/arms/s\$s.ALLDONE ] || { echo \"s\$s not finished\" >&2; exit 3; }; done;
        for s in $OLDSEEDS; do ls -d episodes/prods\${s}*/evidence.json episodes/prods\${s}*/*/checkpoints/archive_gen*.csv logs/_idea_prods\${s}*.log \
                         research/$DIR/arms/*s\${s}_* research/$DIR/arms/s\${s}.ALLDONE research/$DIR/loc/s\${s}_* research/$DIR/guidance/s\${s}_* \
                         research/$DIR/m/lib_s\${s}_* research/$DIR/m/s\${s}.DONE 2>/dev/null; done | sort -u | tar czf - -T -" > $SP/prod_gather.tgz \
    && tar tzf $SP/prod_gather.tgz > $SP/prod_gather.list && break
  sleep 15
done
n=$(grep -c "evidence.json" $SP/prod_gather.list || true)
want=$(( $(echo $OLDSEEDS | wc -w) * 10 ))
echo "packed $(wc -l < $SP/prod_gather.list) files, $n evidence files (expected $(echo $OLDSEEDS | wc -w) seeds x (4 M + 3 rounds x 2 slots) = $want)"
[ "$n" -eq "$want" ] || echo "NOTE: $n evidence files, expected $want -- fine only if the missing ones are missions that failed twice (no evidence; prod_final.py lists them)"
for s in $NEWSEEDS; do grep -q "prods${s}\|[_/]s${s}[_.]" $SP/prod_gather.list && { echo "refusing: new-host seed $s in the bundle"; exit 4; }; done
$NEW "cd $NR && tar xzf - && for s in $OLDSEEDS; do echo \"s\$s: \$(ls -d episodes/prods\${s}*/ | wc -l) episode dirs\"; done" < $SP/prod_gather.tgz
