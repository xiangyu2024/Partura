# PROD W01 运行手册

设计见 `PLAN.md`,规则见 `rules.md`,种子 → 服务器见 `hosts.json`(种子 901–908 在新服务器,909–912 在原服务器)。
笔记本上的命令都在 `/Users/wxy/Desktop/Partura-prod` 里跑(分支 `prod-w01` 或并入后的 `main`);**不要碰 `/Users/wxy/Desktop/Partura`**。

下面的变量和函数先在笔记本的 shell 里设好(zsh 与 bash 都能用;后面的命令都用它们。**不要把 ssh 命令存成变量再不加引号展开**:zsh 不会按空格拆开):

```bash
cd /Users/wxy/Desktop/Partura-prod
NEWHOME=/var/snap/docker/common/var-lib-docker/c02_partura/Partura
OLDHOME=/root/autodl-tmp/Partura
NEWSEEDS="901 902 903 904 905 906 907 908"; OLDSEEDS="909 910 911 912"
nssh() { ssh -o ConnectTimeout=15 -o ServerAliveInterval=30 root@100.111.77.69 "$@"; }
ossh() { ssh -o ConnectTimeout=15 -o ServerAliveInterval=30 -p 29982 root@connect.westd.seetacloud.com "$@"; }
hsh()   { local h=$1; shift; if [ "$h" = new ]; then nssh "$@"; else ossh "$@"; fi; }            # hsh new|old "<remote command>"
hhome() { if [ "$1" = new ]; then echo $NEWHOME; else echo $OLDHOME; fi; }
haddr() { if [ "$1" = new ]; then echo root@100.111.77.69; else echo root@connect.westd.seetacloud.com; fi; }
hrsync(){ local h=$1; shift; if [ "$h" = new ]; then rsync -e "ssh -o ConnectTimeout=15" "$@"; else rsync -e "ssh -p 29982 -o ConnectTimeout=15" "$@"; fi; }
```

(`hosts.json` 里的 ssh 命令与这里一致;`prod_sync.sh` / `prod_gather.sh` 读的是 `hosts.json`,不用这些函数。)

## 0. 硬约束(PLAN §3)

- **新服务器**上还跑着用户的大量其他服务:一律不碰。只写 `$NEWHOME` 下面的目录;**根分区(余约 60 GB)不写**
  (`prod_env.sh` 把 `TMPDIR` 指到 `$NEWHOME/tmp/sys_tmp`;启动前后各看一次 `df -h /`,应当不变)。
  不对不属于本研究的进程发任何信号:`pkill` / `killall` 不用;找进程只用下面这种带脚本名的 `pgrep -af`,杀进程按 pid。
- **原服务器**磁盘余约 123 GB,磁盘守护线 60 GB(`scripts/server/c01_diskguard.sh` 会杀溢出文件最大的作业)。
  **跌到 90 GB 以下**:它那 4 个种子的后续轮次改到新服务器跑(见 §7)。
- 两台服务器的数据都停在 2026-09-16。一切挑选只用样本内(train 2018–2021、valid 2022-01 ~ 2023-08-07);测试段与前推段只作描述(PLAN §4)。
- 只 rsync 代码:`partura/`、`scripts/`、`research/prod_W01/{rules.md,hosts.json}`;`workflows/` 只在笔记本。不 `--delete`。

## 1. 部署(两台各做一次)

### 1.1 先看(只读)

```bash
for H in new old; do
  echo "== $H"; hsh $H "cd $(hhome $H) && df -h / | tail -1; df -h \${GUARD_DISK:-$(hhome $H)} | tail -1; ls tmp/c05_env.sh tmp/c08_env.sh; \
     nvidia-smi --query-gpu=memory.used,memory.total --format=csv,noheader; pgrep -af 'c0[5-8]_(conductor|keeper|m)|prod_(conductor|keeper|m)|idea_search|c05_(round|locate)' | cut -c1-150; md5sum guidance/C05_base.yaml"
done
md5 -q guidance/C05_base.yaml          # 两台的 md5 必须与它相同(guidance 不 rsync)
```

要点:没有残留的 C0X / PROD 进程(有就先弄清是谁的,**不要杀**);`tmp/c05_env.sh` 在。

### 1.2 rsync(先试跑,看清楚只动了哪些文件,再真传)

```bash
# 试跑:每台一遍,只列要改的文件
for H in new old; do for d in partura/ scripts/; do
  hrsync $H -avn --itemize-changes --exclude __pycache__ --exclude '*.pyc' $d $(haddr $H):$(hhome $H)/$d; done; done
#   预期被改 / 新增的只有:partura/study.py、scripts/c05_round.py、c05_locate.py、c06_check.py、idea_search.py、scripts/prod_*、scripts/server/prod_*
#   (若列出别的文件,先弄清为什么服务器上的版本和仓库不同,再决定;不要盲目覆盖)
# 真传
for H in new old; do
  for d in partura/ scripts/; do hrsync $H -av --exclude __pycache__ --exclude '*.pyc' $d $(haddr $H):$(hhome $H)/$d; done
  hsh $H "mkdir -p $(hhome $H)/research/prod_W01"
  hrsync $H -av research/prod_W01/rules.md research/prod_W01/hosts.json $(haddr $H):$(hhome $H)/research/prod_W01/
  hrsync $H -av scripts/server/prod_env.sh $(haddr $H):$(hhome $H)/tmp/prod_env.sh          # 模板放到 <home>/tmp/ 下
done
```

`prod_env.sh` 先 `source` 该服务器自己的 `tmp/c05_env.sh`(路径、python、GPU / 内存设置、日频叶子),再设:
`PARTURA_C0X=PROD`、`PARTURA_STUDY_DIR=prod_W01`、`PARTURA_RANK_FIRST=1`、`PARTURA_NEUTRAL_POWERS=1,2,3`、`C06_CTRL_STRIKE=0.8`、`PARTURA_R_ADDITIONS=0`(PLAN 修订 1)、`TMPDIR`。
**两台之间不得有别的差别。**

### 1.3 验证(只读)

```bash
for H in new old; do hsh $H "cd $(hhome $H) && source tmp/prod_env.sh && env | grep -E '^(PARTURA_(C0X|STUDY_DIR|RANK_FIRST|NEUTRAL_POWERS|R_ADDITIONS)|C06_CTRL_STRIKE|TMPDIR)=' && \
        \$PY -c 'from partura import study; print(study.dirname(\"PROD\"), study.prefix(\"PROD\"), study.m_prefix(\"PROD\"), study.r_additions(\"PROD\"))' && \
        bash -n scripts/server/prod_conductor.sh && bash -n scripts/server/prod_m.sh && bash -n scripts/server/prod_keeper.sh && echo scripts parse"; done
```
期望:`prod_W01 prod prod True` 与 `scripts parse`。

### 1.4 磁盘守护

```bash
for H in new old; do hsh $H "cd $(hhome $H) && screen -ls | grep c01_guard; ls research/coldstart_C01/guard.stop 2>&1 | tail -1"; done
```
没有 `c01_guard` 会话就起(有 `guard.stop` 说明有人特意停过它,先弄清再删):

```bash
for H in new old; do hsh $H "cd $(hhome $H) && source tmp/prod_env.sh && screen -dmS c01_guard scripts/server/c01_diskguard.sh"; done
#   监控的盘:新服务器由 c05_env.sh 的 GUARD_DISK 指到 docker 数据盘(不是根分区);原服务器默认 /root/autodl-tmp。线 60 GB(MIN_FREE_GB)
```
守护只会杀 `Partura/tmp/alphacube_*` 溢出目录的持有进程(本研究的作业),被杀的 M 批由调度自动重启、P 任务由执行器自动重跑一次。

## 2. 开跑(每台一次)

先手工起各种子的调度(这样守护的 5 次重启额度不被首次启动占掉),再起守护(各开一个 screen 会话,没有 screen 就用 `nohup setsid`):

```bash
hsh new "cd $NEWHOME && source tmp/prod_env.sh && mkdir -p research/prod_W01 logs && \
  for s in $NEWSEEDS; do nohup bash scripts/server/prod_conductor.sh \$s >> research/prod_W01/conductor_s\$s.out 2>&1 < /dev/null & done; sleep 3; \
  screen -dmS prod_keeper bash -c 'cd $NEWHOME && source tmp/prod_env.sh && scripts/server/prod_keeper.sh $NEWSEEDS'; screen -ls | grep prod_keeper"
hsh old "cd $OLDHOME && source tmp/prod_env.sh && mkdir -p research/prod_W01 logs && \
  for s in $OLDSEEDS; do nohup bash scripts/server/prod_conductor.sh \$s >> research/prod_W01/conductor_s\$s.out 2>&1 < /dev/null & done; sleep 3; \
  screen -dmS prod_keeper bash -c 'cd $OLDHOME && source tmp/prod_env.sh && scripts/server/prod_keeper.sh $OLDSEEDS'; screen -ls | grep prod_keeper"
```

调度对每个种子:在后台起主 AlphaCube(`prod_m.sh`:4 批,每批只按本种子自己的历史禁;已完成的批不重跑);
第 k 轮 **等 M 第 k 批完成** → 定位(`loc/s<seed>_P_r<k>.READY`)→ **等计划文件 `arms/s<seed>_P_r<k>.yaml`** → 执行任务 → `arms/s<seed>_P_r<k>.DONE`;
三轮之后等 M 链 `m/s<seed>.DONE`,然后 `arms/s<seed>.ALLDONE`。M 链中途死掉(磁盘守护、超时、重启),调度会在等待时重新起它,最多 6 次(`m/s<seed>.starts`)。


> **2026-11-07 实际开跑时的修正(总领)**:新服务器**没有 `screen`**,守护改用 tmux:
> `tmux new-session -d -s prod_keeper "cd $NEWHOME && source tmp/prod_env.sh && scripts/server/prod_keeper.sh $NEWSEEDS"`(原服务器照用 screen)。
> 两台的磁盘守护分别是原服务器的 screen `c01_guard`、新服务器的 tmux `c01_guard`。

## 3. 每一轮(k = 1, 2, 3)

M 的第 k 批和上一轮的任务都完成后,服务器才会算第 k 轮的定位。种子之间不同步:谁 READY 就先跑谁。

```bash
bash scripts/prod_sync.sh status            # 每个种子:M 已完成的批、r<k>:ready / +plan / +done、ALLDONE
bash scripts/prod_sync.sh ready 1           # 第 1 轮哪些种子的定位输出已经 READY(退出码 1 = 还有没好的)
```

对 READY 的种子,在 Claude Code 里跑 Workflow(脚本 `workflows/prod_round.js`):

```
Workflow({scriptPath: "/Users/wxy/Desktop/Partura-prod/workflows/prod_round.js", args: {"round": 1, "seeds": [901, 902, 903]}})
```

每个种子一路做完:取定位输出(`prod_sync.sh fetch`)→ PI(Sonnet 5.5,写 `missions.yaml` 与笔记)→ 相关度表(`prod_sync.sh corr`,服务器上算,约 5–10 分钟)→ 审计(Haiku 5.5,1 次)→
`prod_finish.py`(定稿 → 检查 → 推送到种子所在服务器)。结果里每个种子有 `pushed: true`;`failed` 写明停在哪一步。
推送之后服务器上调度立刻开跑任务。

续跑(某个环节失败,前面各步的文件还在磁盘上):

```
Workflow({scriptPath: ".../workflows/prod_round.js", args: {"round": 1, "seeds": [903], "from": {"903": "corr"}}})      # from: fetch | pi | corr | audit | finish
```

没有 Claude 时手工做:`bash scripts/prod_sync.sh fetch K S` → 按 `rules.md` 手写 `research/prod_W01/partura/s<S>/r<K>/missions.yaml` →
`PARTURA_C0X=PROD PARTURA_STUDY_DIR=prod_W01 C06_CTRL_STRIKE=0.8 ~/.venvs/alphacube/bin/python scripts/c06_check.py S K` →
`bash scripts/prod_sync.sh corr K S 1`(退出码 3 = 还在算,再跑同一条)→ 手写 `audit_1.yaml`(格式见 `workflows/prod_round.js` 的审计提示)→
`~/.venvs/alphacube/bin/python scripts/prod_finish.py K S`。

每轮做完,把笔记本上的工作文件提交:`git add research/prod_W01/partura && git commit`。

预算(PLAN §2):每种子每轮 ≤ 30 万 token(PI ≤ 20 万,其余 ≤ 10 万);W01 合计 ≤ 1,100 万,超出就停下看原因。

## 4. 监控

服务器上(`cd <home> && source tmp/prod_env.sh`):

```bash
scripts/server/prod_health.sh 901 902 903 904 905 906 907 908       # 本机的种子;只打印问题和每个种子一行
```

| 看什么 | 在哪里(`<home>/research/prod_W01/` 下,日志在 `<home>/logs/`) |
|---|---|
| 每个种子的进度 | `conductor_s<seed>.log`(每轮一行)、`conductor_s<seed>.out` |
| 守护 | `keeper.log`(`restart n` / `GAVE UP`) |
| M 链 | `m/s<seed>.log`(每批一行退出码)、`m/s<seed>.starts`(已起几次)、`m/s<seed>.DONE`、`logs/_idea_prods<seed>M<批>.log` |
| 定位 | `loc/s<seed>_P_r<k>.json` `.md` `.READY`;`logs/_prodloc_s<seed>_P_r<k>.log` |
| 计划已到 | `arms/s<seed>_P_r<k>.yaml` |
| 任务位 | `logs/_idea_prods<seed>Pr<k>a.log`、`…b.log`;`arms/s<seed>_P_r<k>.DONE`(每行 `<标签> <退出码>`,非 0 要看) |
| R 直接评估 | `logs/_prodR_s<seed>_P_r<k>.log`、`arms/s<seed>_P_r<k>_R.json` |
| 相关度表 | `logs/_prodcorr_s<seed>_r<k>_q1_<请求 md5 前 8 位>.log`、`audit/` |
| 全部完成 | `arms/s<seed>.ALLDONE` |
| 磁盘守护 | `<home>/research/coldstart_C01/diskguard.log`(`killing`) |

调度的退出码:4 = 定位失败、6 = 任务执行器死了(守护会重启调度,至多 5 次,超过写 `GAVE UP`)、7 = M 链起了 6 次还没跑完。
要给 M 链更多次机会:`rm research/prod_W01/m/s<seed>.starts`,然后让守护重启调度(或手工起)。
笔记本上看全局用 `bash scripts/prod_sync.sh status`。

## 5. 出了问题

- **一个 GP 作业被杀 / 失败**:任务位由执行器自动原样重跑一次(证据 `*.broken.json`、日志 `*.broken.log` 留档);仍失败的记为「花了预算、没有产出」,不卡后面的轮次。M 批由调度重启。
- **推送了错的计划**:`prod_sync.sh push` 不会覆盖服务器上已有的不同计划(要覆盖设 `FORCE=1`,但如果该轮的任务已经开跑,先弄清再动)。
- **相关度表**:作业名带请求的 md5,改了 `missions.yaml` 就是新作业,不会拿到旧表。
- 不确定的时候:停在原地、看日志,不要在新服务器上杀不属于本研究的进程。

## 6. 汇总与定稿(所有种子 ALLDONE 之后)

```bash
bash scripts/prod_sync.sh status                                            # 12 个种子都应有 ALLDONE
bash scripts/prod_gather.sh                                                 # 原服务器 909–912 的证据 / 日志 / 计划 / 定位 → 新服务器(要求它们都 ALLDONE)
nssh "cd $NEWHOME && source tmp/prod_env.sh && \$PY scripts/prod_final.py --dry-run --gpu-fraction 0.9"      # 只含样本内:库大小、复现率
```

试跑看库的大小、复现率(`reproduces`),没有问题再读测试段 / 前推段(**只作描述,会记入 `ledger_prod.json`**):

```bash
nssh "cd $NEWHOME && source tmp/prod_env.sh && \$PY scripts/prod_final.py --gpu-fraction 0.9"
# 产出(都在 $NEWHOME/research/prod_W01/):final.json、library.json、final.md、ledger_prod.json;
# 整波 P 融合信号面板 $NEWHOME/runs/prod_W01/wave_fused.npy(+ .meta.json;路径也写在 final.json 的 wave_signal_panel 里)
for f in final.json library.json final.md ledger_prod.json final_dry.json library_dry.json final_dry.md; do
  nssh "cat $NEWHOME/research/prod_W01/$f" > research/prod_W01/$f 2>/dev/null || rm -f research/prod_W01/$f; done
git add research/prod_W01 && git commit
```

再读一次要加 `--again`(会再记一笔账)。`--seeds` 只配 `--dry-run`(看部分种子)。
数据更新到 2026-09-16 之后的确认性检验(PLAN §4)要用户先更新数据,不在本手册里。

## 7. 原服务器磁盘跌到 90 GB 以下

1. 在原服务器上 `df -h /root/autodl-tmp`,确认;`tail research/coldstart_C01/diskguard.log`。
2. 对受影响的种子(例如 910–912 的下一轮):先让它**当前轮的任务跑完**(`arms/s<seed>_P_r<k>.DONE`),再停那个种子的调度与守护:
   `pgrep -af 'prod_(conductor|m)\.sh 910$'` 找到 pid,按 pid `kill`(守护 `prod_keeper.sh` 是整台的:先停守护,再停调度,再用剩下的种子重起守护)。
3. 把该种子的 `episodes/prods<seed>*`(evidence.json 与 `*/checkpoints/archive_gen*.csv`)、`logs/_idea_prods<seed>*.log`、`research/prod_W01/{arms,loc,guidance,m}/*s<seed>_*` 打包搬到新服务器同样的位置
   (照 `scripts/prod_gather.sh` 的打包清单),在 `hosts.json` 里把该种子改成 `"new"`,rsync 新的 `hosts.json` 到两台。
4. 在新服务器上起该种子的调度(§2 的命令,只对这个种子),把它加进新服务器守护的种子表(重起新服务器的守护)。M 链已完成的批不会重跑。
5. 之后 `prod_sync.sh` 自动按新映射走;`prod_gather.sh` 只搬映射里仍在原服务器的种子。
