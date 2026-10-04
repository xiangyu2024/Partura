#!/bin/bash
# One study's lifeline to the server.  Run from the Mac, in ~/Desktop/Partura.
# Each subcommand touches ONLY this study's files (configs/<fid>.yaml, studies/<fid>/, notes/<fid>/,
# runs/<fid>/), so several studies can run side by side without stepping on each other.
#
#   study.sh ops [regex]                   list operators (name, face/family/category, windows) — the vocabulary
#   study.sh src <operator> [...]          print the server's kernel source of an operator (the source of truth)
#   study.sh check <fid>                   parse every expression of the config on the server (do this before `run`)
#   study.sh decompose <fid>               operator dossiers + SSA decomposition + lab priors, on the server
#   study.sh propose <fid>                 candidate experiments derived from the tree (a DRAFT to curate)
#   study.sh run <fid> <tag> <stage...>    push config, start the stages on the server (returns at once)
#   study.sh final <fid> <tag> <stage>     same, but reads the HOLDOUT (once per study -- it is ledgered)
#   study.sh exec <fid> <tag> <script.py>  run studies/<fid>/<script.py> on the server (returns at once)
#   study.sh wait <fid> <tag> [seconds]    wait (default 540 s) for that job; on completion pull + print the digest
#   study.sh digest <fid> <tag> [base_id]  re-print the digest of a finished run
#   study.sh report <fid>                  push notes, build the report on the server, pull the .md back
#   study.sh status                        what Partura jobs are on the server right now
set -u
cd "$(dirname "$0")/.."
PY=${PY:-$HOME/.venvs/alphacube/bin/python}
HOST=root@connect.westd.seetacloud.com
SSH="ssh -o BatchMode=yes -o ControlPath=none -o ConnectTimeout=30 -p 29982"
RS="rsync -a --exclude __pycache__ -e"
R=/root/autodl-tmp/Partura
ENV="cd $R && export PYTHONPATH=/root/autodl-tmp/AlphaCube/src:$R ALPHACUBE_ROOT=/root/autodl-tmp/AlphaCube OMP_NUM_THREADS=2 MKL_NUM_THREADS=2 PARTURA_RANK_DEVICE=cuda PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True PARTURA_SLOTS=\${PARTURA_SLOTS:-2}"
RPY=/root/miniconda3/envs/quant/bin/python
cmd=${1:-}; shift || true

push() {   # this study's inputs only
  local fid=$1
  $RS "$SSH" "configs/$fid.yaml" "$HOST:$R/configs/" || return 1
  [ -d "studies/$fid" ] && { $SSH $HOST "mkdir -p $R/studies/$fid"; $RS "$SSH" "studies/$fid/" "$HOST:$R/studies/$fid/"; }
  [ -d "notes/$fid" ] && { $SSH $HOST "mkdir -p $R/notes/$fid"; $RS "$SSH" "notes/$fid/" "$HOST:$R/notes/$fid/"; }
  return 0
}

case "$cmd" in
  ops)
    $SSH $HOST "$ENV && $RPY -m partura.remote_tools ops '${1:-.}' 2>&1 | grep -v 'FutureWarning\|vmap(single_row)'"
    ;;
  src)
    $SSH $HOST "$ENV && $RPY -m partura.remote_tools src $* 2>&1 | grep -v 'FutureWarning\|vmap(single_row)'"
    ;;
  check)
    fid=$1; push "$fid" || exit 1
    $SSH $HOST "$ENV && $RPY -m partura.remote_tools check $fid 2>&1 | grep -v 'FutureWarning\|vmap(single_row)'"
    ;;
  decompose)
    fid=$1; push "$fid" || exit 1
    $SSH $HOST "$ENV && P=''; [ -f studies/$fid/probes.py ] && P='--probes studies/$fid/probes.py'; $RPY -m partura.cli decompose --config configs/$fid.yaml \$P 2>&1 | grep -v 'FutureWarning\|vmap(single_row)'"
    ;;
  propose)
    fid=$1; push "$fid" || exit 1
    $SSH $HOST "$ENV && $RPY -m partura.remote_tools propose $fid 2>&1 | grep -v 'FutureWarning\|vmap(single_row)'"
    ;;
  run|final)
    fid=$1; tag=$2; shift 2
    push "$fid" || exit 1
    extra=""; [ "$cmd" = final ] && extra="--holdout"
    $SSH $HOST "$ENV && mkdir -p logs && rm -f logs/${fid}_${tag}.log && screen -dmS pt_${fid:0:4}_${tag} bash -c 'EXTRA=\"$extra --tag $tag\" PARTURA_SLOTS=\${PARTURA_SLOTS:-2} ./scripts/run_server.sh configs/$fid.yaml $* > logs/${fid}_${tag}.log 2>&1' && echo 'started $fid/$tag: stages $* $extra'"
    ;;
  exec)
    fid=$1; tag=$2; script=$3; shift 3
    push "$fid" || exit 1
    $SSH $HOST "$ENV && mkdir -p logs && rm -f logs/${fid}_${tag}.log && screen -dmS pt_${fid:0:4}_${tag} bash -c '$ENV; nice -n 5 $RPY -u studies/$fid/$script $* > logs/${fid}_${tag}.log 2>&1; echo \"[partura exit \$? \$(date +%F_%T)]\" >> logs/${fid}_${tag}.log' && echo 'started $fid/$tag: $script'"
    ;;
  wait)
    fid=$1; tag=$2; secs=${3:-540}
    end=$(( $(date +%s) + secs ))
    while :; do
      st=$($SSH $HOST "grep -ac 'partura exit' $R/logs/${fid}_${tag}.log 2>/dev/null; grep -av 'FutureWarning\|vmap(single_row)\|UserWarning' $R/logs/${fid}_${tag}.log 2>/dev/null | tail -4" 2>/dev/null)
      [ "$(echo "$st" | head -1)" = "1" ] && break
      [ "$(date +%s)" -ge "$end" ] && { echo "STILL RUNNING after ${secs}s — call 'study.sh wait $fid $tag' again. Last lines:"; echo "$st" | tail -n +2; exit 3; }
      sleep 20
    done
    echo "$st" | tail -n +2
    mkdir -p "runs/$fid" logs
    $RS "$SSH" "$HOST:$R/logs/${fid}_${tag}.log" logs/ 2>/dev/null
    $RS "$SSH" --include='*.json' --exclude='*' "$HOST:$R/runs/$fid/" "runs/$fid/" 2>/dev/null
    if [ -f "runs/$fid/$tag.json" ]; then "$PY" scripts/summarize.py "runs/$fid/$tag.json";
    else echo "(no runs/$fid/$tag.json — an exec job prints its own output; full log: logs/${fid}_${tag}.log)";
         grep -av 'FutureWarning\|vmap(single_row)\|UserWarning' "logs/${fid}_${tag}.log" | tail -200; fi
    ;;
  digest)
    fid=$1; tag=$2; base=${3:-v_base}
    "$PY" scripts/summarize.py "runs/$fid/$tag.json" --base "$base"
    ;;
  report)
    fid=$1; push "$fid" || exit 1
    $SSH $HOST "$ENV && $RPY -m partura.cli report configs/$fid.yaml 2>&1 | grep -v 'FutureWarning\|vmap(single_row)'" || exit 1
    mkdir -p research/alpha_distillation
    $RS "$SSH" "$HOST:$R/research/alpha_distillation/$fid.md" research/alpha_distillation/ && wc -l "research/alpha_distillation/$fid.md"
    ;;
  status)
    $SSH $HOST "screen -ls | grep pt_ ; echo; nvidia-smi --query-compute-apps=pid,used_memory --format=csv,noheader; awk '/^anon /{printf \"container anon %.1f GiB\n\", \$2/1073741824}' /sys/fs/cgroup/memory.stat; ls $R/tmp/locks 2>/dev/null | tr '\n' ' '"
    ;;
  *) sed -n '2,16p' "$0"; exit 2 ;;
esac
