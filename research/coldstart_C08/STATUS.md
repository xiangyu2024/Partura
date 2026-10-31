# C08 现状与收尾步骤(2026-10-31 写;研究负责人的额度将用完,别人或别的 AI 照这里接手)

设计见 `PLAN.md`(含修订 1:第 2、3 轮降成本)。规则见 `rules.md`(宽松审计)、`rules_strict.md`(旁听,只用于第 1 轮的 3 个种子)。

## 已完成

| 轮 | 种子 | 流程 | 状态 |
|---|---|---|---|
| 1 | 801–807 | 完整:解剖 Opus 5 → 文献 Sonnet 5 → PI Opus 5.5 → 相关度表 → 宽松审计 Opus 5.5 | 定稿已推送;任务已在服务器跑完 |
| 1 | 801、803、805 | 严格审计员旁听(`partura/s80X/r1/shadow.yaml`) | 有;其余 5 个种子按修订 1 不再做 |
| 1 | 808 | 精简:PI Sonnet 5 → 相关度表 → 审计 Sonnet 5(1 次) | 定稿已推送 |
| 2 | 801–808 | 精简 | 定稿已推送 |
| 3 | 801–807 | 精简 | 写本文件时 workflow 正在跑(run `wf_5510653c-5d3`);跑完要推送 |
| 3 | 808 | 精简 | 等服务器上第 3 轮的定位输出 |

各种子各轮的审计结果都在 `partura/s80X/rK/audit_record.json`。到写本文件时,所有任务位都通过了审计,没有改成普通 GP 的。

## 还要做的(按顺序)

笔记本在 `/Users/wxy/Desktop/Partura`。服务器与目录:
- 原服务器:`ssh -p 29982 root@connect.westd.seetacloud.com`,目录 `/root/autodl-tmp/Partura`,种子 801、803、804、805;
- 新服务器:`ssh root@100.111.77.69`,目录 `/var/snap/docker/common/var-lib-docker/c02_partura/Partura`,种子 802、806、807、808。

服务器上的命令都要先 `source tmp/c08_env.sh`。调度与守护(`scripts/server/c08_conductor.sh`、`c08_keeper.sh`)在两台服务器上一直在跑:计划推上去就开跑任务,跑完自动算下一轮的定位。

1. **第 3 轮的计划**
   - 801–807:workflow 跑完后,在笔记本上推送:
     ```
     STUDY=C08 ARM=P bash scripts/c06_sync.sh push 3 "801 802 803 804 805 806 807"
     ```
   - 808:第 3 轮的定位出来后,先拉取,再跑 workflow,最后推送。
     - 拉取:`STUDY=C08 ARM=P bash scripts/c06_sync.sh fetch 3 808`
     - workflow:Claude Code 的 Workflow 工具,脚本 `workflows/c06_round.js`,参数 `{"round": 3, "seeds": [808], "study": "C08", "arm": "P", "ctrl_strike": 0.8, "lean": true}`
     - 推送:`STUDY=C08 ARM=P bash scripts/c06_sync.sh push 3 808`
   - **没有 Claude 时**:可以让别的 LLM 按 `rules.md` 手写 `partura/s808/r3/missions.yaml` 与审计,再用下面的命令定稿,然后推送。这一步要在 PLAN 里记一条修订。
     ```
     PARTURA_C0X=C08 C06_CTRL_STRIKE=0.8 python scripts/c06_check.py 808 3 --finalize
     ```
2. **等全部跑完**:两台服务器上 `research/coldstart_C08/arms/s<种子>.ALLDONE` 都出现。
3. **汇总**:笔记本上 `bash scripts/c08_gather.sh`,把原服务器的 4 个种子复制到新服务器。
4. **样本内试跑**:新服务器上
   ```
   PARTURA_SELF_LIMIT_GB=200 PARTURA_CGROUP_LIMIT_GB=600 $PY scripts/c08_final.py --dry-run --gpu-fraction 0.9
   ```
   看复现率与库大小。
5. **读开发集(测试段)**:同上去掉 `--dry-run`,得到 `research/coldstart_C08/final.json`,主判定在 `PRIMARY:` 一行(P 对 A)。
   - 融合书默认再中性化;要不中性化的版本,加 `--no-fuse-neutral`(输出名会不同,先改脚本里的文件名,免得覆盖)。
6. **写 RESULT.md**:格式同 C07。
   - P 的额外 head 按轮次分开:第 1 轮完整流程,第 2、3 轮精简流程;
   - 第 1 轮 801、803、805 按旁听严格审计员的判断分组,只作描述;
   - 测试段是开发集,确认要等 2026-09-16 之后的新数据。

## 额度

- 第 1 轮完整流程约占计划的三分之一。
- 第 2 轮精简流程:7 个种子约 420 万子 agent token,808 约 70 万。
- 第 3 轮应与第 2 轮相当。
