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
#   study.sh list <fid>                    what has ALREADY run for this study on the server (tags, exit codes)
#   study.sh status                        what Partura jobs are on the server right now
#   study.sh table <fid> [tag]             the BATCH SWEEP table (hundreds of variants side by side) + the market anatomy
#   study.sh hypo <fid>                    check that studies/<fid>/hypo.yaml (hypotheses for the next sweep) parses
#   study.sh brief <fid>                   the HANDOFF briefing: where this study stands, its journal, what exists -- read it first
#   study.sh note <fid> "<title>" [<<EOF]  append an entry to the research journal notes/<fid>/journal.md (body on stdin)
#
# The journal is how a study survives its researcher: a study can be cut off at any moment and continued by
# someone else (another model), and only what was written down carries over.  run/final/exec/wait add their own
# one-line entries; what a result MEANS is yours to add with `note` before you start the next thing.
set -u
cd "$(dirname "$0")/.."
PY=${PY:-$HOME/.venvs/alphacube/bin/python}
HOST=root@connect.westd.seetacloud.com
SSH="ssh -o BatchMode=yes -o ControlPath=none -o ConnectTimeout=30 -o ServerAliveInterval=15 -o ServerAliveCountMax=4 -p 29982"
RS="rsync -a --exclude __pycache__ -e"
R=/root/autodl-tmp/Partura
ENV="cd $R && export PYTHONPATH=/root/autodl-tmp/AlphaCube/src:$R ALPHACUBE_ROOT=/root/autodl-tmp/AlphaCube OMP_NUM_THREADS=2 MKL_NUM_THREADS=2 PARTURA_RANK_DEVICE=cuda PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True PARTURA_SLOTS=\${PARTURA_SLOTS:-6} PARTURA_MEM_WAIT_S=\${PARTURA_MEM_WAIT_S:-10800}"
RPY=/root/miniconda3/envs/quant/bin/python
cmd=${1:-}; shift || true

jfile() { echo "notes/$1/journal.md"; }
jinit() {   # create the journal with its header
  local f; f=$(jfile "$1"); mkdir -p "notes/$1"
  [ -f "$f" ] || printf '# %s 研究日志\n\n只追加、不改写。[auto] 是工具自己记的(启动了什么、什么时候跑完);其余是研究员写的:\n每看完一个结果,写下它说明了什么、哪条假设变了、下一步做什么。接手的人先读这里(`./scripts/study.sh brief %s`)。\n' "$1" "$1" > "$f"
}
jlog() {    # jlog <fid> <text>: one automatic line
  jinit "$1"; printf '\n### %s [auto] %s\n' "$(date '+%Y-%m-%d %H:%M')" "$2" >> "$(jfile "$1")"
}
notice() {  # a standing notice from the coordinator to whoever is working on this study (handoff/NOTICE.md);
            # it stops appearing for a study once that study's notes/<fid>/state.md is newer than the notice
  local f="handoff/NOTICE.md" s="notes/${1:-}/state.md"
  [ -n "${1:-}" ] && [ -f "$f" ] || return 0
  [ -f handoff/NOTICE.fids ] && ! grep -qx "$1" handoff/NOTICE.fids && return 0   # addressed to listed studies only
  [ -f "$s" ] && [ "$s" -nt "$f" ] && return 0
  echo; sed "s/<fid>/$1/g" "$f"
}
trap 'notice "${fid:-}"' EXIT
remind() {  # what every finished result ends with
  echo
  echo "📝 往下做之前先记日志(研究随时可能中断、换人或换模型接手;没落盘的判断会丢):"
  echo "   ./scripts/study.sh note $1 \"<一句话:这次看到了什么>\" <<'EOF'"
  echo "   这次结果说明什么(带关键数字)/ 哪条假设因此变了 / 下一步打算做什么、为什么"
  echo "   EOF"
  echo "   并更新 notes/$1/state.md(研究现状:中间结果 / 逻辑 / 假设表 / 候选 / 后面的思路;格式见 docs/study_playbook.md §7)。"
}

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
    $SSH $HOST "$ENV && mkdir -p logs && rm -f logs/${fid}_${tag}.log && screen -dmS pt_${fid:0:4}_${tag} bash -c 'EXTRA=\"$extra --tag $tag\" PARTURA_SLOTS=\${PARTURA_SLOTS:-6} ./scripts/run_server.sh configs/$fid.yaml $* > logs/${fid}_${tag}.log 2>&1' && echo 'started $fid/$tag: stages $* $extra'" || exit 1
    if [ "$cmd" = final ]; then jlog "$fid" "⚠ 读留出段:final $tag,阶段 $*(留出段只能读这一次;候选与判据应当已经写在 10_distilled.md 里)"
    else jlog "$fid" "启动 run $tag:阶段 $*"; fi
    ;;
  exec)
    fid=$1; tag=$2; script=$3; shift 3
    push "$fid" || exit 1
    $SSH $HOST "$ENV && mkdir -p logs && rm -f logs/${fid}_${tag}.log && screen -dmS pt_${fid:0:4}_${tag} bash -c '$ENV; nice -n 5 $RPY -u studies/$fid/$script $* > logs/${fid}_${tag}.log 2>&1; echo \"[partura exit \$? \$(date +%F_%T)]\" >> logs/${fid}_${tag}.log' && echo 'started $fid/$tag: $script'" || exit 1
    jlog "$fid" "启动 exec $tag:studies/$fid/$script $*"
    ;;
  list)
    fid=$1
    $SSH $HOST "cd $R; echo '# 已有的运行(tag = 日志名去掉前缀;exit 0 = 成功,97 = 内存守卫让路,其他 = 出错):'; for f in logs/${fid}_*.log; do [ -f \"\$f\" ] || continue; t=\$(basename \$f .log); t=\${t#${fid}_}; e=\$(grep -a 'partura exit' \$f | tail -1); j=''; [ -f runs/$fid/\$t.json ] && j='  [有 JSON]'; printf '  %-22s %s%s\n' \"\$t\" \"\${e:-(还在跑 / 没有退出行)}\" \"\$j\"; done; echo '# 正在跑的:'; screen -ls | grep 'pt_${fid:0:4}_' || echo '  (无)'"
    mkdir -p "runs/$fid"
    $RS "$SSH" --include='*.json' --exclude='*' "$HOST:$R/runs/$fid/" "runs/$fid/" 2>/dev/null && echo "# 已把服务器上的 runs/$fid/*.json 拉回本地"
    ;;
  wait)
    fid=$1; tag=$2; secs=${3:-540}
    if ! $SSH $HOST "[ -f $R/logs/${fid}_${tag}.log ]" 2>/dev/null; then
      echo "没有这个任务:服务器上不存在 logs/${fid}_${tag}.log(tag 写错了,或者还没 run)。用 'study.sh list $fid' 看已有的运行。"; exit 4
    fi
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
    ex=$(grep -a 'partura exit' "logs/${fid}_${tag}.log" 2>/dev/null | tail -1 | sed 's/.*partura exit \([0-9]*\).*/\1/')
    if [ -f "runs/$fid/$tag.json" ]; then "$PY" scripts/summarize.py "runs/$fid/$tag.json"; see="./scripts/study.sh digest $fid $tag";
    else echo "(no runs/$fid/$tag.json — an exec job prints its own output; full log: logs/${fid}_${tag}.log)";
         grep -av 'FutureWarning\|vmap(single_row)\|UserWarning' "logs/${fid}_${tag}.log" | tail -200; see="logs/${fid}_${tag}.log"; fi
    grep -qs "\[auto\] $tag 跑完" "$(jfile "$fid")" || jlog "$fid" "$tag 跑完(exit ${ex:-?});重看结果:$see"
    remind "$fid"
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
  hypo)      # do the hypotheses in studies/<fid>/hypo.yaml parse?  (they go into the next batch sweep)
    fid=$1; push "$fid" || exit 1
    $SSH $HOST "$ENV && $RPY scripts/check_hypo.py studies/$fid/hypo.yaml 2>&1 | grep -v 'FutureWarning\|vmap(single_row)\|UserWarning'"
    ;;
  table)     # the batch-sweep backtest table and the market anatomy of this factor (tag defaults to s1; --all = every variant)
    fid=$1; tag=${2:-s1}
    mkdir -p "runs/$fid"
    $RS "$SSH" --include='*.json' --exclude='*' "$HOST:$R/runs/$fid/" "runs/$fid/" 2>/dev/null
    "$PY" scripts/sweep_table.py "$fid" "$tag" ${3:-}
    ;;
  brief)
    fid=$1
    "$PY" scripts/recorder.py --brief "$fid"
    ;;
  note)
    fid=$1; shift
    title="$*"; body=""
    if [ -p /dev/stdin ] || [ -f /dev/stdin ]; then body=$(cat); fi
    [ -n "$title$body" ] || { echo "用法:study.sh note <fid> \"<一句话>\" <<'EOF' … EOF"; exit 2; }
    jinit "$fid"
    { printf '\n### %s %s\n' "$(date '+%Y-%m-%d %H:%M')" "${title:-(无标题)}"; [ -n "$body" ] && printf '\n%s\n' "$body"; } >> "$(jfile "$fid")"
    echo "已记入 $(jfile "$fid")($(grep -c '^### ' "$(jfile "$fid")") 条)"
    ;;
  status)
    $SSH $HOST "screen -ls | grep pt_ ; echo; nvidia-smi --query-compute-apps=pid,used_memory --format=csv,noheader; awk '/^anon /{printf \"container anon %.1f GiB\n\", \$2/1073741824}' /sys/fs/cgroup/memory.stat; ls $R/tmp/locks 2>/dev/null | tr '\n' ' '"
    ;;
  *) sed -n '2,24p' "$0"; exit 2 ;;
esac
