#!/bin/bash
# Server side: keep the SHARED data disk from filling up while C01 jobs run (research/coldstart_C01/PLAN.md §6, revision 2).
# AlphaCube spills whole (stock, day, minute) intermediates of minute-level cross-sectional expressions to
# Partura/tmp/alphacube_*/bound_*.npy (6.8 GB each); one R2 job wrote 253 GB and filled the disk.  Every 20 s: if the
# disk has less than MIN_FREE_GB left, the process that holds the LARGEST spill directory open is killed (its job is
# then recorded as failed by c01_queue.sh) and that directory is removed.  Nothing outside Partura/tmp/alphacube_* is touched.
#   screen -dmS c01_guard scripts/server/c01_diskguard.sh        (stop: touch research/coldstart_C01/guard.stop)
MIN=${MIN_FREE_GB:-60}
cd ${PARTURA_HOME:-/root/autodl-tmp/Partura}
LOG=research/coldstart_C01/diskguard.log
echo "[guard] $(date +%F_%T) started, min free ${MIN}G" >> $LOG
while [ ! -f research/coldstart_C01/guard.stop ]; do
  avail=$(df -BG --output=avail ${GUARD_DISK:-/root/autodl-tmp} | tail -1 | tr -dc 0-9)
  if [ "${avail:-0}" -lt "$MIN" ]; then
    big=$(du -s tmp/alphacube_* 2>/dev/null | sort -rn | head -1 | cut -f2)
    if [ -n "$big" ]; then
      full=$(readlink -f "$big")
      pids=$(for p in /proc/[0-9]*; do { ls -l $p/fd 2>/dev/null; cat $p/maps 2>/dev/null; } | grep -q "$full" && basename $p; done | tr '\n' ' ')
      echo "[guard] $(date +%F_%T) free ${avail}G < ${MIN}G: spill $big ($(du -sh $big | cut -f1)), killing: ${pids:-none}" >> $LOG
      [ -n "$pids" ] && kill -TERM $pids 2>/dev/null; sleep 20
      [ -n "$pids" ] && kill -KILL $pids 2>/dev/null; sleep 5
      rm -rf "$big"
      echo "[guard] $(date +%F_%T) removed $big; free now $(df -BG --output=avail ${GUARD_DISK:-/root/autodl-tmp} | tail -1 | tr -dc 0-9)G" >> $LOG
    fi
  fi
  sleep 20
done
echo "[guard] $(date +%F_%T) stopped" >> $LOG
