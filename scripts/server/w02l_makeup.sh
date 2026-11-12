#!/bin/bash
# PROD W02L makeup (research/prod_W02L/MAKEUP.md): re-run the GP slots that ended "(rerun) 98" -- infrastructure failures (GPU
# oversubscription 11-09, killed after 12 h in the queue, old/new code mixed on 11-10), not search outcomes -- each with its round's
# own pushed plan (arms/s<S>_P_r<K>.yaml), by running that round's mission again: c05_round.py skips every slot whose episode finished
# cleanly and the R evaluation that already exists, so only the broken slots search again.
#
# Fills idle capacity only (2026-11-12): a round is started when fewer than $MAKEUP_IDLE_BELOW (default 3 = the GP ways) GP searches
# are alive on the host (so nothing is queued for the card) and fewer than $MAKEUP_MAX (default 2) makeup searches are, so the tail of
# the regular rounds always keeps a way.
#
# Before a round is re-run: its arms files and guidance are copied to research/prod_W02L/makeup_orig/s<S>_r<K>/ (the mission rewrites
# seen / fam / guidance / DONE), the broken episodes move to episodes/_broken98/, their logs to logs/_idea_<tag>.broken98.log.
# Differences from the original run, by construction: the wave ban (PARTURA_WAVE_BAN) now holds every stream's heads found since.
#   source tmp/w02l_env.sh; nohup bash scripts/server/w02l_makeup.sh research/prod_W02L/makeup_list.txt > /dev/null 2>&1 < /dev/null &
#   list lines: "<seed> <round> <slot> [<slot>]"
LIST=${1:?list}
cd ${PARTURA_HOME:?}
[ -n "$PY" ] && [ "$PARTURA_STUDY_DIR" = prod_W02L ] || { echo "source tmp/w02l_env.sh first"; exit 2; }
D=research/prod_W02L; LOG=$D/makeup.log; ORIG=$D/makeup_orig; mkdir -p $ORIG episodes/_broken98
say() { echo "[makeup] $* $(date +%F_%T)" >> $LOG; }
gp_alive() { pgrep -fc "^$PY -u scripts/idea_search.py"; }
LAUNCHED=""
mk_alive() { local m=0 t; for t in $LAUNCHED; do pgrep -f "^$PY -u scripts/idea_search.py .*--tag $t " > /dev/null && m=$((m + 1)); done; echo $m; }
say "started: $(wc -l < $LIST) rounds, $(awk '{n += NF - 2} END {print n}' $LIST) slots"
while read -r S K SLOTS <&3; do
  [ -z "$S" ] && continue
  if grep -q "^s$S r$K started" $D/makeup_started.txt 2>/dev/null; then say "s$S r$K: started earlier, skipped"; continue; fi
  until [ "$(gp_alive)" -lt "${MAKEUP_IDLE_BELOW:-3}" ] && [ "$(mk_alive)" -lt "${MAKEUP_MAX:-2}" ]; do sleep 120; done
  while pgrep -f "[c]05_round.py mission $S P $K\$" > /dev/null; do sleep 120; done      # never beside a runner of the same round
  mkdir -p $ORIG/s${S}_r$K
  cp -p $D/arms/*s${S}_P_r${K}* $ORIG/s${S}_r$K/ 2>/dev/null
  cp -p $D/guidance/s${S}_P_r$K.yaml $ORIG/s${S}_r$K/ 2>/dev/null
  for j in $SLOTS; do
    t=prods${S}Pr${K}$j
    for ep in episodes/${t}_*; do [ -d "$ep" ] && mv "$ep" episodes/_broken98/; done
    [ -f logs/_idea_$t.log ] && mv logs/_idea_$t.log logs/_idea_$t.broken98.log
    LAUNCHED="$LAUNCHED $t"
  done
  nohup $PY -u scripts/c05_round.py mission $S P $K > logs/_prodmakeup_s${S}_P_r$K.log 2>&1 < /dev/null &
  echo "s$S r$K started $(date +%F_%T)" >> $D/makeup_started.txt
  say "s$S r$K: started (slots $SLOTS; GP alive $(gp_alive))"
  sleep 300                                                                   # let its searches show up before the next count
done 3< $LIST
say "all rounds started; waiting for the last ones"
while [ "$(mk_alive)" -gt 0 ]; do sleep 300; done
say "all makeup searches ended"
