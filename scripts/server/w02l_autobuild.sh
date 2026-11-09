#!/bin/bash
# PROD W02L (research/prod_W02L/PLAN.md revision 1), server side: every 10 minutes build the streams whose three batches stage 0
# has finished (scripts/w02l_lib.py build) and start one keeper (scripts/server/prod_keeper.sh) for the streams just built --
# the keeper keeps their conductors alive, the conductor runs locate -> waits for the plan -> missions, round by round.
# Stops when every stream is built.
#   source tmp/w02l_env.sh; nohup bash scripts/server/w02l_autobuild.sh >> research/prod_W02L/autobuild.log 2>&1 &
cd ${PARTURA_HOME:?}
[ "$PARTURA_STUDY_DIR" = prod_W02L ] && [ "$PARTURA_VIEW" = w02 ] || { echo "source tmp/w02l_env.sh first"; exit 2; }
D=research/$PARTURA_STUDY_DIR
built() { python3 -c "import json;print(' '.join(str(x['seed']) for x in json.load(open('$D/streams.json'))['streams']))" 2>/dev/null; }
N=$(python3 -c "import json;print(-(-len(json.load(open('$D/struct/batches.json'))['batches'])//3))")
while true; do
  before=" $(built) "
  echo "[autobuild] $(date +%F_%T) $($PY scripts/w02l_lib.py build --ruler B 2>&1 | tail -n 1)"
  new=""; for s in $(built); do case "$before" in *" $s "*) ;; *) new="$new $s";; esac; done
  if [ -n "$new" ]; then
    nohup bash scripts/server/prod_keeper.sh $new >> $D/keeper.out 2>&1 < /dev/null &
    echo "[autobuild] keeper started for$new"
  fi
  [ "$(built | wc -w)" -ge "$N" ] && { echo "[autobuild] all $N streams built"; break; }
  sleep ${W02L_BUILD_EVERY_S:-600}
done
