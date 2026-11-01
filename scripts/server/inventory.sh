#!/bin/bash
# 只读盘点(在笔记本上跑):两台服务器上的 Partura / AlphaCube 目录、git 状态、大小、在跑的进程。不改、不杀、不写任何东西。
#   bash scripts/server/inventory.sh > /tmp/inventory.txt 2>&1
probe='
echo "### $(hostname)  $(date "+%F %T")"
nproc; free -g | head -2; df -h 2>/dev/null | grep -E "autodl|docker|/$" | head -5
nvidia-smi --query-gpu=name,memory.used,memory.total,utilization.gpu --format=csv,noheader 2>/dev/null
echo "--- screen / tmux"; screen -ls 2>/dev/null | head -20; tmux ls 2>/dev/null | head
echo "--- python / bash 进程(最老的在前)"
ps -eo pid,user,etimes,rss,args --sort=-etimes | grep -E "python|bash scripts|conductor|keeper" | grep -v grep | cut -c1-220 | head -40
for d in $DIRS; do
  [ -d "$d" ] || continue
  echo; echo "=== $d"
  cd "$d" || continue
  if [ -e .git ]; then
    git -c safe.directory="*" log --oneline -3 2>&1 | head -3
    git -c safe.directory="*" status -sb 2>&1 | head -1
    echo "未提交的文件数: $(git -c safe.directory="*" status --porcelain 2>/dev/null | wc -l)"
  else
    echo "不是 git 仓库"; ls VERSION 2>/dev/null && cat VERSION
  fi
  echo "最近 2 天改过的文件数(不含 .git): $(timeout 120 find . -path ./.git -prune -o -type f -mtime -2 -print 2>/dev/null | wc -l)"
  echo "--- 顶层各目录大小"; timeout 180 du -sh -- * 2>/dev/null | sort -rh | head -15
done
'
echo "########## 老服务器"
ssh -o ConnectTimeout=20 -o BatchMode=yes -p 29982 root@connect.westd.seetacloud.com \
  "DIRS='/root/autodl-tmp/Partura /root/autodl-tmp/Partura/vendor/AlphaCube-steering /root/autodl-tmp/AlphaCube'; $probe"
echo; echo "########## 新服务器"
ssh -o ConnectTimeout=20 -o BatchMode=yes root@100.111.77.69 \
  "N=/var/snap/docker/common/var-lib-docker/c02_partura; ls -la \$N 2>/dev/null | head -20;
   DIRS=\"\$N/Partura \$N/Partura/vendor/AlphaCube-steering \$(ls -d \$N/AlphaCube* /root/AlphaCube* /root/autodl-tmp/AlphaCube* 2>/dev/null | tr '\n' ' ')\"; $probe"
