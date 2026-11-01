#!/bin/bash
# 把服务器上的 Partura / AlphaCube 目录做成 GitHub 上的快照分支(在笔记本上跑)。服务器只读:只用 rsync 拉,不在服务器上写任何东西。
#   bash scripts/server/snapshot_to_github.sh plan          只看会拉多少(rsync 演练,不落盘、不推)
#   bash scripts/server/snapshot_to_github.sh push          拉到 ~/partura_sync/,再推成 sync/server-<old|new>-<repo>-<日期> 分支
# 不拉:pools/、runs/_panels/、数组与模型文件、单个 > 45 MB 的文件、AlphaCube 的 _bench / mirror / mining_runs;其余再按仓库的 .gitignore 过滤。
# 快照的父提交:Partura 用 origin/claude/charming-babbage-d2h3x4,AlphaCube 用 origin/main;笔记本的工作区与分支都不动。
set -u
MODE=${1:?plan|push}
STAGE=${STAGE:-$HOME/partura_sync}
DATE=$(date +%Y%m%d-%H%M)
OLD="ssh -o ConnectTimeout=20 -o ServerAliveInterval=30 -p 29982"; OLDH=root@connect.westd.seetacloud.com
NEW="ssh -o ConnectTimeout=20 -o ServerAliveInterval=30";          NEWH=root@100.111.77.69
EXCL=(--exclude .git/ --exclude __pycache__/ --exclude pools/ --exclude runs/_panels/ --exclude _bench/ --exclude mirror/
      --exclude mining_runs/ --exclude factor_runs/ --exclude tmp/ --exclude 'shared/'
      --exclude '*.npy' --exclude '*.npz' --exclude '*.pt' --exclude '*.pth' --exclude '*.pkl' --exclude '*.parquet' --exclude '*.feather'
      --exclude '*.h5' --exclude '*.tgz' --exclude '*.tar*' --exclude '*.zip' --max-size=45m)
# 名字  ssh  主机  远端目录  本地仓库  父提交
JOBS=(
  "old-Partura|$OLD|$OLDH|/root/autodl-tmp/Partura|$HOME/Desktop/Partura|origin/claude/charming-babbage-d2h3x4"
  "old-AlphaCube|$OLD|$OLDH|/root/autodl-tmp/AlphaCube|$HOME/Desktop/AlphaCube|origin/main"
  "new-Partura|$NEW|$NEWH|/var/snap/docker/common/var-lib-docker/c02_partura/Partura|$HOME/Desktop/Partura|origin/claude/charming-babbage-d2h3x4"
  "new-AlphaCube|$NEW|$NEWH|/root/autodl-tmp/AlphaCube|$HOME/Desktop/AlphaCube|origin/main"
)
for J in "${JOBS[@]}"; do
  IFS='|' read -r NAME SSH HOST RDIR REPO PARENT <<< "$J"
  echo "========== $NAME  ($HOST:$RDIR)"
  if [ "$MODE" = plan ]; then
    rsync -an --stats -e "$SSH" "${EXCL[@]}" "$HOST:$RDIR/" /tmp/_partura_plan_$NAME/ 2>&1 \
      | grep -E "Number of (regular )?files|Total file size|Total transferred file size" ; continue
  fi
  D=$STAGE/$NAME; mkdir -p "$D"
  for i in 1 2 3; do rsync -a --delete --prune-empty-dirs -e "$SSH" "${EXCL[@]}" "$HOST:$RDIR/" "$D/" && break; sleep 10; done || { echo "rsync failed: $NAME"; continue; }
  ( GD=$(git -C "$REPO" rev-parse --absolute-git-dir) || exit 1
    g() { git --git-dir="$GD" --work-tree="$D" -C "$D" "$@"; }
    g fetch -q origin "${PARENT#origin/}" || exit 1
    export GIT_INDEX_FILE="$(mktemp -d)/index"
    g read-tree "$PARENT"                                     # 以父提交为底
    g add --ignore-removal . 2>/dev/null                      # 服务器上的版本覆盖、新增;按仓库的 .gitignore 过滤;服务器没有的文件不当删除
    N=$(g diff --cached --name-only "$PARENT" | wc -l | tr -d ' ')
    MB=$(g diff --cached --name-only -z "$PARENT" | (cd "$D" && xargs -0 du -k 2>/dev/null) | awk '{s+=$1} END{printf "%d", s/1024}')
    echo "$NAME: 相对 $PARENT 有 $N 个文件不同,约 ${MB:-0} MB"
    [ "$N" = 0 ] && { echo "没有差别,不推"; exit 0; }
    [ "${MB:-0}" -gt 800 ] && { echo "超过 800 MB,没有推;最大的 15 个:"; g diff --cached --name-only -z "$PARENT" | (cd "$D" && xargs -0 du -k 2>/dev/null) | sort -rn | head -15; exit 1; }
    C=$(g commit-tree "$(g write-tree)" -p "$PARENT" -m "服务器快照 $NAME($HOST:$RDIR,$(date '+%F %T')):只读拉取,排除面板、数组与 >45MB 文件")
    g push -q origin "${C}:refs/heads/sync/server-${NAME}-${DATE}" && echo "已推送 -> sync/server-${NAME}-${DATE}" )
done
