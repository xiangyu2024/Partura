#!/bin/bash
# PROD (research/prod_W01/PLAN.md), laptop side: move one round's files between the servers and this work tree
# (as scripts/c06_sync.sh does for C05-C08: same commands, same retries, atomic md5-checked pushes).  Which seed lives on which
# host comes from research/prod_W01/hosts.json (scripts/prod_hosts.py); nothing is hard-coded here.
#   scripts/prod_sync.sh ready <k> [seeds]      -> which seeds have loc/s<seed>_P_r<k>.READY
#   scripts/prod_sync.sh fetch <k> [seeds]      -> partura/s<seed>/r<k>/loc.json, loc.md (the locate output), R_prev.json (R of round k-1)
#                                                  refuses (exit 1) a seed whose locate has not finished (no READY)
#   scripts/prod_sync.sh push <k> [seeds]       -> arms/s<seed>_P_r<k>.yaml on the seed's server (= partura/s<seed>/r<k>/missions_final.yaml)
#                                                  refuses to replace a DIFFERENT plan that is already there (FORCE=1 to do it anyway)
#   scripts/prod_sync.sh corr <k> <seed> <n>    -> partura/s<seed>/r<k>/corr_<n>.json / .md: the auditor's correlation table for the
#                                                  expressions of partura/s<seed>/r<k>/missions.yaml (cores, seeds, R variants).
#                                                  exit 3 = still running (run the same command again), 1 = failed, 0 = written
#   scripts/prod_sync.sh status [seeds]         -> per seed: M batches complete, round markers (READY / plan / DONE), ALLDONE
# [seeds] = a quoted, space separated list ("901 902"); default: every seed of the mapping.  Exit status of ready / fetch / push:
# 0 only if every named seed succeeded.
# Knobs (tests): PROD_HOSTS (another hosts.json), PROD_SYNC_SLEEP (seconds between retries, default 10), PYL (a python with PyYAML).
CMD=${1:?ready|fetch|push|corr|status}
REPO=$(cd "$(dirname "$0")/.." && pwd)
PYL=${PYL:-/Users/wxy/.venvs/alphacube/bin/python}; [ -x "$PYL" ] || PYL=python3
HOSTS="$PYL $REPO/scripts/prod_hosts.py"
DIR=$($HOSTS dir) || exit 1                        # prod_W01
L=$REPO/research/$DIR; ARM=P; EV=prod; SL=${PROD_SYNC_SLEEP:-10}
# every remote call is retried (the old server's ssh gateway drops connections now and then); a fetched file must be non-empty
rsh() { local H="$1"; shift; for i in 1 2 3 4 5; do $H "$@" && return 0; sleep $SL; done; return 1; }
host() { $HOSTS ssh "$1"; }
home() { $HOSTS home "$1"; }

if [ "$CMD" = status ]; then
  SEEDS=${2:-$($HOSTS seeds)}; RC=0; SCR=$(mktemp)
  cat > $SCR <<'EOF'
cd "$1" && D=research/$2 && shift 2 || exit 1
for s in "$@"; do
  m=""; for e in 1 2 3 4; do grep -q '"complete": true' episodes/prods${s}M${e}_I0_open_search/evidence.json 2>/dev/null && m="$m$e"; done
  r=""; for k in 1 2 3; do
    [ -e $D/loc/s${s}_P_r$k.READY ] && r="$r r$k:ready"; [ -e $D/arms/s${s}_P_r$k.yaml ] && r="$r+plan"; [ -e $D/arms/s${s}_P_r$k.DONE ] && r="$r+done"
  done
  echo "s$s  M batches done [${m:--}]${r}$([ -e $D/arms/s$s.ALLDONE ] && echo '  ALLDONE')"
done
EOF
  for HN in $(for s in $SEEDS; do $HOSTS host $s; done | sort -u); do
    mine=""; for s in $SEEDS; do [ "$($HOSTS host $s)" = "$HN" ] && mine="$mine $s"; done
    echo "== $HN"
    ok=""; for i in 1 2 3; do $($HOSTS hostssh $HN) "bash -s -- $($HOSTS hosthome $HN) $DIR $mine" < $SCR && { ok=1; break; }; sleep $SL; done
    [ -n "$ok" ] || { echo "$HN: unreachable"; RC=1; }
  done
  rm -f $SCR; exit $RC
fi

K=${2:?round}
if [ "$CMD" = corr ]; then
  S=${3:?seed}; N=${4:?attempt}; H=$(host $S) && RH=$(home $S) || exit 1
  R=$RH/research/$DIR; P=$L/partura/s$S/r$K
  $PYL - "$P/missions.yaml" > $P/corr_$N.request.json <<'EOF' || { echo "CORR FAILED: cannot read missions.yaml"; exit 1; }
import json, sys, yaml
M = yaml.safe_load(open(sys.argv[1], encoding="utf-8")) or {}
out = []
for s, j in zip(M.get("slots") or [], "ab"):
    if s.get("core"):
        out.append({"where": f"slot {j} core", "expr": s["core"]})
    out += [{"where": f"slot {j} seed {i + 1}", "expr": e} for i, e in enumerate(s.get("seeds") or [])]
for i, r in enumerate(M.get("R") or []):
    out += [{"where": f"R {i + 1} variant {k + 1}", "expr": e} for k, e in enumerate(r.get("variants") or [])]
print(json.dumps(out, ensure_ascii=False))
EOF
  want=$(md5 -q $P/corr_$N.request.json); ok=""
  # the job is named after the request's md5: a rewritten missions.yaml is a new job (a finished job's table is never reused for it)
  Q=s${S}_r${K}_q${N}_${want:0:8}
  for i in 1 2 3 4 5; do
    $H "mkdir -p $R/audit && cat > $R/audit/.$Q.json.part && [ \$(md5sum < $R/audit/.$Q.json.part | cut -c1-32) = $want ] && mv $R/audit/.$Q.json.part $R/audit/$Q.json" < $P/corr_$N.request.json && { ok=1; break; }
    sleep $SL
  done
  [ -n "$ok" ] || { echo "CORR FAILED: could not send the request"; exit 1; }
  # resumable: a finished job is only fetched, a running one only waited for ([c]... keeps pgrep from matching this very command)
  st=$($H "grep -ao '\[corr exit [0-9]*\]' $RH/logs/_${EV}corr_$Q.log 2>/dev/null | tail -1")
  if [ -z "$st" ] && ! $H "pgrep -f '[c]05_locate.py corr $S $ARM $K research/$DIR/audit/$Q.json' > /dev/null"; then
    rsh "$H" "cd $RH && rm -f $R/audit/${Q}_corr.json $R/audit/${Q}_corr.md && source tmp/${EV}_env.sh && \
              nohup bash -c '\$PY -u scripts/c05_locate.py corr $S $ARM $K research/$DIR/audit/$Q.json > logs/_${EV}corr_$Q.log 2>&1; echo \"[corr exit \$?]\" >> logs/_${EV}corr_$Q.log' > /dev/null 2>&1 < /dev/null &"
    echo "started the correlation job on $(echo $H | awk '{print $NF}')"
  fi
  for t in $(seq 1 ${PROD_CORR_POLLS:-20}); do        # ~5-6 minutes per call (ssh included), well inside a 10-minute tool limit
    st=$($H "grep -ao '\[corr exit [0-9]*\]' $RH/logs/_${EV}corr_$Q.log 2>/dev/null | tail -1")
    [ -n "$st" ] && break
    sleep ${PROD_CORR_POLL_S:-15}
  done
  [ -n "$st" ] || { echo "STILL RUNNING: run the same command again to keep waiting ($($H "grep -a '\[corr\]\|guard' $RH/logs/_${EV}corr_$Q.log | tail -1"))"; exit 3; }
  [ "$st" = "[corr exit 0]" ] || { echo "CORR FAILED: $st"; rsh "$H" "grep -av 'FutureWarning\|return vmap' $RH/logs/_${EV}corr_$Q.log | tail -5"; exit 1; }
  rsh "$H" "cat $R/audit/${Q}_corr.json" > $P/corr_$N.json && rsh "$H" "cat $R/audit/${Q}_corr.md" > $P/corr_$N.md
  [ -s $P/corr_$N.json ] && [ -s $P/corr_$N.md ] || { echo "CORR FAILED: empty fetch"; exit 1; }
  echo "corr_$N.md written: $(grep -c '^| slot\|^| R' $P/corr_$N.md) rows -> $P/corr_$N.md"
  exit 0
fi

RC=0
for S in ${3:-$($HOSTS seeds)}; do
  H=$(host $S) && R=$(home $S)/research/$DIR || { echo "$S: not in the host mapping"; RC=1; continue; }
  P=$L/partura/s$S/r$K
  case $CMD in
    ready) rsh "$H" "test -e $R/loc/s${S}_${ARM}_r$K.READY" && echo "$S ready" || { echo "$S waiting"; RC=1; } ;;
    fetch) mkdir -p $P
           rsh "$H" "test -e $R/loc/s${S}_${ARM}_r$K.READY" || { echo "$S: NOT READY (the locate output of round $K is not finished)"; RC=1; continue; }
           rsh "$H" "cat $R/loc/s${S}_${ARM}_r$K.json" > $P/loc.json && rsh "$H" "cat $R/loc/s${S}_${ARM}_r$K.md" > $P/loc.md
           [ -s $P/loc.json ] && [ -s $P/loc.md ] || { echo "$S: FETCH FAILED (empty)"; rm -f $P/loc.json $P/loc.md; RC=1; continue; }
           # (c06_sync.sh asks `test -e F && cat F` under the retry loop: a missing R file then costs 50 s of retries; here "absent" is not a failure)
           [ $K -gt 1 ] && rsh "$H" "if test -e $R/arms/s${S}_${ARM}_r$((K - 1))_R.json; then cat $R/arms/s${S}_${ARM}_r$((K - 1))_R.json; fi" > $P/R_prev.json
           [ -s $P/R_prev.json ] || rm -f $P/R_prev.json
           echo "$S: $(wc -c < $P/loc.json) bytes of locate output" ;;
    push)  ok=""                                        # atomic (temp name, then mv); each try re-reads the file; md5 checked
           [ -s $P/missions_final.yaml ] || { echo "$S: no missions_final.yaml"; RC=1; continue; }
           want=$(md5 -q $P/missions_final.yaml)
           have=$(rsh "$H" "{ md5sum < $R/arms/s${S}_${ARM}_r$K.yaml; } 2>/dev/null | cut -c1-32; true")   # empty = no plan there yet ({ } so a missing file prints nothing)
           have=$(echo $have | tr -d ' -')
           if [ "$have" = "$want" ]; then echo "$S pushed ($want) (already on the server)"; continue; fi
           if [ -n "$have" ] && [ "$have" != "d41d8cd98f00b204e9800998ecf8427e" ] && [ -z "$FORCE" ]; then
             echo "$S: REFUSING: a different plan is already on the server (md5 $have, this one $want); FORCE=1 to replace it"; RC=1; continue
           fi
           for i in 1 2 3 4 5; do
             $H "mkdir -p $R/arms && cat > $R/arms/.s${S}_${ARM}_r$K.yaml.part && [ \$(md5sum < $R/arms/.s${S}_${ARM}_r$K.yaml.part | cut -c1-32) = $want ] && mv $R/arms/.s${S}_${ARM}_r$K.yaml.part $R/arms/s${S}_${ARM}_r$K.yaml" < $P/missions_final.yaml && { ok=1; break; }
             sleep $SL
           done
           [ -n "$ok" ] && echo "$S pushed ($want)" || { echo "$S: PUSH FAILED"; RC=1; } ;;
    *) echo "unknown command $CMD"; exit 2 ;;
  esac
done
exit $RC
