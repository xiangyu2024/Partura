#!/bin/bash
# C06, laptop side (research/coldstart_C06/PLAN.md §2.4-2.5): move one round's files between the servers and Partura's directories.
#   scripts/c06_sync.sh ready <k> [seeds]      -> which seeds have loc/s<seed>_C_r<k>.READY
#   scripts/c06_sync.sh fetch <k> [seeds]      -> partura/s<seed>/r<k>/loc.json, loc.md (C's locate output), R_prev.json (C's R of round k-1)
#   scripts/c06_sync.sh push <k> [seeds]       -> arms/s<seed>_C_r<k>.yaml on the seed's server (= partura/s<seed>/r<k>/missions_final.yaml)
#   scripts/c06_sync.sh corr <k> <seed> <n>    -> partura/s<seed>/r<k>/corr_<n>.json / .md: the auditor's correlation table for the
#                                                 expressions of partura/s<seed>/r<k>/missions.yaml (cores, seeds, R variants)
# Seeds 801, 803, 804, 805 live on the old server, 802, 806, 807, 808 on the new one (PLAN §5).
CMD=$1; K=${2:?round}
L=/Users/wxy/Desktop/Partura/research/coldstart_C06
OLDH="ssh -o ConnectTimeout=15 -o ServerAliveInterval=30 -p 29982 root@connect.westd.seetacloud.com"; OLDR=/root/autodl-tmp/Partura
NEWH="ssh -o ConnectTimeout=15 -o ServerAliveInterval=30 root@100.111.77.69"; NEWR=/var/snap/docker/common/var-lib-docker/c02_partura/Partura
# every remote call is retried (the old server's ssh gateway drops connections now and then); a fetched file must be non-empty
rsh() { local H="$1"; shift; for i in 1 2 3 4 5; do $H "$@" && return 0; sleep 10; done; return 1; }
host() { case $1 in 801|803|804|805) echo "$OLDH" ;; *) echo "$NEWH" ;; esac; }
home() { case $1 in 801|803|804|805) echo $OLDR ;; *) echo $NEWR ;; esac; }

if [ "$CMD" = corr ]; then
  S=${3:?seed}; N=${4:?attempt}; H=$(host $S); RH=$(home $S); R=$RH/research/coldstart_C06; P=$L/partura/s$S/r$K
  Q=s${S}_r${K}_q$N
  /Users/wxy/.venvs/alphacube/bin/python - "$P/missions.yaml" > $P/corr_$N.request.json <<'EOF' || { echo "CORR FAILED: cannot read missions.yaml"; exit 1; }
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
  for i in 1 2 3 4 5; do
    $H "mkdir -p $R/audit && cat > $R/audit/.$Q.json.part && [ \$(md5sum < $R/audit/.$Q.json.part | cut -c1-32) = $want ] && mv $R/audit/.$Q.json.part $R/audit/$Q.json" < $P/corr_$N.request.json && { ok=1; break; }
    sleep 10
  done
  [ -n "$ok" ] || { echo "CORR FAILED: could not send the request"; exit 1; }
  # resumable: a finished job is only fetched, a running one only waited for ([c]... keeps pgrep from matching this very command)
  st=$($H "grep -ao '\[corr exit [0-9]*\]' $RH/logs/_c06corr_$Q.log 2>/dev/null | tail -1")
  if [ -z "$st" ] && ! $H "pgrep -f '[c]05_locate.py corr $S C $K research/coldstart_C06/audit/$Q.json' > /dev/null"; then
    rsh "$H" "cd $RH && rm -f $R/audit/${Q}_corr.json $R/audit/${Q}_corr.md && source tmp/c06_env.sh && \
              nohup bash -c '\$PY -u scripts/c05_locate.py corr $S C $K research/coldstart_C06/audit/$Q.json > logs/_c06corr_$Q.log 2>&1; echo \"[corr exit \$?]\" >> logs/_c06corr_$Q.log' > /dev/null 2>&1 < /dev/null &"
    echo "started the correlation job on $(echo $H | awk '{print $NF}')"
  fi
  for t in $(seq 1 20); do                      # ~5-6 minutes per call (ssh included), well inside a 10-minute tool limit
    st=$($H "grep -ao '\[corr exit [0-9]*\]' $RH/logs/_c06corr_$Q.log 2>/dev/null | tail -1")
    [ -n "$st" ] && break
    sleep 15
  done
  [ -n "$st" ] || { echo "STILL RUNNING: run the same command again to keep waiting ($($H "grep -a '\[corr\]\|guard' $RH/logs/_c06corr_$Q.log | tail -1"))"; exit 3; }
  [ "$st" = "[corr exit 0]" ] || { echo "CORR FAILED: $st"; rsh "$H" "grep -av 'FutureWarning\|return vmap' $RH/logs/_c06corr_$Q.log | tail -5"; exit 1; }
  rsh "$H" "cat $R/audit/${Q}_corr.json" > $P/corr_$N.json && rsh "$H" "cat $R/audit/${Q}_corr.md" > $P/corr_$N.md
  [ -s $P/corr_$N.json ] && [ -s $P/corr_$N.md ] || { echo "CORR FAILED: empty fetch"; exit 1; }
  echo "corr_$N.md written: $(grep -c '^| slot\|^| R' $P/corr_$N.md) rows -> $P/corr_$N.md"
  exit 0
fi

for S in ${3:-801 802 803 804 805 806 807 808}; do
  H=$(host $S); R=$(home $S)/research/coldstart_C06; P=$L/partura/s$S/r$K
  case $CMD in
    ready) rsh "$H" "test -e $R/loc/s${S}_C_r$K.READY" && echo "$S ready" || echo "$S waiting" ;;
    fetch) mkdir -p $P
           rsh "$H" "cat $R/loc/s${S}_C_r$K.json" > $P/loc.json && rsh "$H" "cat $R/loc/s${S}_C_r$K.md" > $P/loc.md
           [ -s $P/loc.json ] && [ -s $P/loc.md ] || { echo "$S: FETCH FAILED (empty)"; rm -f $P/loc.json $P/loc.md; continue; }
           [ $K -gt 1 ] && rsh "$H" "test -e $R/arms/s${S}_C_r$((K - 1))_R.json && cat $R/arms/s${S}_C_r$((K - 1))_R.json" > $P/R_prev.json
           [ -s $P/R_prev.json ] || rm -f $P/R_prev.json
           echo "$S: $(wc -c < $P/loc.json) bytes of locate output" ;;
    push)  ok=""                                        # atomic (temp name, then mv); each try re-reads the file; md5 checked
           [ -s $P/missions_final.yaml ] || { echo "$S: no missions_final.yaml"; continue; }
           want=$(md5 -q $P/missions_final.yaml)
           for i in 1 2 3 4 5; do
             $H "mkdir -p $R/arms && cat > $R/arms/.s${S}_C_r$K.yaml.part && [ \$(md5sum < $R/arms/.s${S}_C_r$K.yaml.part | cut -c1-32) = $want ] && mv $R/arms/.s${S}_C_r$K.yaml.part $R/arms/s${S}_C_r$K.yaml" < $P/missions_final.yaml && { ok=1; break; }
             sleep 10
           done
           [ -n "$ok" ] && echo "$S pushed ($want)" || echo "$S: PUSH FAILED" ;;
  esac
done
