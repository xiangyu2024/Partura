#!/bin/bash
# C05, laptop side (research/coldstart_C05/PLAN.md §2.6): move one round's files between the servers and Partura's directories.
#   scripts/c05_sync.sh ready <k>   -> which seeds have loc/s<seed>_r<k>.READY
#   scripts/c05_sync.sh fetch <k>   -> partura/s<seed>/r<k>/loc.json, loc.md (B's locate output), R_prev.json (B's R of round k-1)
#   scripts/c05_sync.sh push <k>    -> arms/s<seed>_B_r<k>.yaml on the seed's server (= partura/s<seed>/r<k>/missions.yaml)
# Only arm B's files ever come to the laptop before the final read: Partura never sees A or B0.
K=${2:?round}
L=/Users/wxy/Desktop/Partura/research/coldstart_C05
# every remote call is retried (the old server's ssh gateway drops connections now and then); a fetched file must be non-empty
rsh() { local H="$1"; shift; for i in 1 2 3 4 5; do $H "$@" && return 0; sleep 10; done; return 1; }
# PLAN revision 11: seed 802 from round 3 on lives on the new host
host() { if [ $1 -le 804 ] && ! { [ $1 = 802 ] && [ $K -ge 3 ]; }; then echo "ssh -p 29982 root@connect.westd.seetacloud.com"; else echo "ssh root@100.111.77.69"; fi; }
dir() { if [ $1 -le 804 ] && ! { [ $1 = 802 ] && [ $K -ge 3 ]; }; then echo /root/autodl-tmp/Partura/research/coldstart_C05; else echo /var/snap/docker/common/var-lib-docker/c02_partura/Partura/research/coldstart_C05; fi; }
for S in ${3:-801 802 803 804 805 806 807 808}; do
  H=$(host $S); R=$(dir $S); P=$L/partura/s$S/r$K
  case $1 in
    ready) rsh "$H" "test -e $R/loc/s${S}_r$K.READY" && echo "$S ready" || echo "$S waiting" ;;
    fetch) mkdir -p $P
           rsh "$H" "cat $R/loc/s${S}_B_r$K.json" > $P/loc.json && rsh "$H" "cat $R/loc/s${S}_B_r$K.md" > $P/loc.md
           [ -s $P/loc.json ] && [ -s $P/loc.md ] || { echo "$S: FETCH FAILED (empty)"; rm -f $P/loc.json $P/loc.md; continue; }
           [ $K -gt 1 ] && rsh "$H" "test -e $R/arms/s${S}_B_r$((K - 1))_R.json && cat $R/arms/s${S}_B_r$((K - 1))_R.json" > $P/R_prev.json
           [ -s $P/R_prev.json ] || rm -f $P/R_prev.json
           echo "$S: $(wc -c < $P/loc.json) bytes of locate output" ;;
    push)  ok=""                                        # atomic (temp name, then mv); each try re-reads the file; md5 checked
           want=$(md5 -q $P/missions.yaml)
           for i in 1 2 3 4 5; do
             $H "cat > $R/arms/.s${S}_B_r$K.yaml.part && [ \$(md5sum < $R/arms/.s${S}_B_r$K.yaml.part | cut -c1-32) = $want ] && mv $R/arms/.s${S}_B_r$K.yaml.part $R/arms/s${S}_B_r$K.yaml" < $P/missions.yaml && { ok=1; break; }
             sleep 10
           done
           [ -n "$ok" ] && echo "$S pushed ($want)" || echo "$S: PUSH FAILED" ;;
  esac
done
