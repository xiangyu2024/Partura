# 交接:怎样在任何时候、用任何模型把研究接着做下去

用户 2026-10-04 的要求:Opus 5.5 容易撞额度,研究必须**随时能被另一个模型接上**。做法是让文件成为唯一的记忆 ——
agent 的对话和推理不落盘(记录里只有命令和输出),所以**没有写进文件的判断等于没有做过**。

## 分工(用户定的)

| 层 | 模型 | 做什么 |
|---|---|---|
| 总领(协调者,主会话) | **Opus 5.5** `claude-opus-5-5` | 搭框架、起工作流、看状态板、批次收尾(分辨 / 总表)、和用户对话 |
| 主研(单条因子的研究思路) | **Opus 5** `claude-opus-5` | 理解表达式、假设与裁决、设计实验(写工单)、选候选、下结论、机制审查 |
| 执行(写代码、跑实验、读结果) | **Sonnet 5** `claude-sonnet-5` | 建档(读源码/基线)、实现工单、跑服务器任务、写结果卡、出报告、核对数字、数字审查 |

主研和执行每一轮都是新的 agent,彼此只靠文件传话。

## 每条因子的记忆在哪

```
notes/<fid>/state.md          研究现状(主研每轮覆盖重写;8 节:现状 / 中间结果 / 过程与逻辑 / 假设表 / 候选 / 后面的思路 / 留出段 / 提醒)
notes/<fid>/journal.md        研究日志(只追加):[auto] 工具记的;[主研] 判断与决定;[执行] 结果卡摘要;[审查] 发现
notes/<fid>/orders/R<n>.md    第 n 张工单(主研 → 执行)
notes/<fid>/results/R<n>.md   第 n 张结果卡(执行 → 主研)
notes/<fid>/NN_*.md           进报告的手写段落
configs/<fid>.yaml  studies/<fid>/  runs/<fid>/*.json  logs/<fid>_*.log
handoff/<fid>/STATE.md        交接页(自动生成):阶段、留出段读没读、state.md 全文、最近的日志、工单/结果卡、已跑的运行、已写的 notes
handoff/<fid>/results/        agent 返回的结构化结果:study.json / audit-numbers.json / audit-mechanism.json / revised.json
handoff/<fid>/agents/         每个 agent 的动作流水(从对话记录里抽的:命令、输出、写了哪些文件)
handoff/STATUS.md             批次状态板
```

`handoff/` 由后台记录器写(`scripts/recorder.py --loop 150`,一个普通的 Python 进程,**不依赖任何模型和额度**;
模型全部停摆时它照样把最后的状态存下来)。它没在跑就起一个:

```bash
cd ~/Desktop/Partura && (nohup ~/.venvs/alphacube/bin/python scripts/recorder.py --loop 150 --hours 36 > logs/_recorder.log 2>&1 &)
```

## 看状态

```bash
cd ~/Desktop/Partura
cat handoff/STATUS.md                                   # 15 条因子各到哪一步
./scripts/study.sh brief <fid>                          # 一条因子的交接页
~/.venvs/alphacube/bin/python scripts/recorder.py --state batches/B01_single_factors.yaml   # 机器可读(重启工作流用)
./scripts/study.sh status                               # 服务器上现在有哪些 Partura 任务
```

阶段只由磁盘决定:`handoff/<fid>/results/` 里没有 `study.json` → 研究没做完;有 `study.json` 没有两份审查 → 待审查;
审查里有 critical/major 且没有 `revised.json` → 待修订;否则完成。

## 接着跑(中断之后;换了模型、换了会话都一样)

1. 确认记录器在跑(上面那条命令),`cat handoff/STATUS.md`。
2. 取状态:`python scripts/recorder.py --state batches/B01_single_factors.yaml`,去掉 `phase == "done"` 的。
3. 起工作流(脚本在仓库里:`workflows/partura_tiered.js`;新会话第一次要把文件内容整个放进 `script` 参数,之后可以用工具返回的 `scriptPath`):

   ```
   Workflow({ script: <workflows/partura_tiered.js 的内容>,
              args: { factors: <第 2 步的 JSON>, chunk: 6,
                      models: { think: "claude-opus-5", work: "claude-sonnet-5" } } })
   ```

   它按每条因子的阶段从磁盘接着做:没建档的先建档 → 主研/执行轮转 → 结论 → 两路审查 → 修订。已经做完的阶段不会重做,
   **不依赖上一次工作流的缓存**,所以不需要 `resumeFromRunId`,换模型也不会把做完的研究重跑一遍。
   想换模型只改 `models`(比如额度紧张时主研也用 Sonnet 5:`think: "claude-sonnet-5"`)。
4. 不用工作流也行:任何 agent 按 `docs/study_playbook.md` §7 开工(`./scripts/study.sh brief <fid>` → 接着做 → 每步落盘)。
   这种情况下 agent 做完一个阶段,由协调者把它返回的结论写到 `handoff/<fid>/results/<study|audit-*|revised>.json`,状态板才会前进。

## 给正在跑的 agent 传话

`handoff/NOTICE.md` 存在时,`scripts/study.sh` 的每条带 `<fid>` 的命令末尾都会打印它(直到那条因子的 `notes/<fid>/state.md`
比通知新)。换班前用它让在跑的 agent 把现状写下来;不需要时删掉这个文件。

## 批次收尾(15 条都完成之后,总领做)

1. `batches/B01_picks.yaml`:每条因子的入选式(`{kind, id(final.json 里的变体 id), run, one_line, family, caveat}`;草稿 `B01_picks_draft.yaml`)。
2. 服务器上 `scripts/batch_final.py batches/B01_picks.yaml`(只用用户训练段:入选式之间的 rank 相关、聚类、对已知成交额族的增量)。
3. 本地 `scripts/batch_summary.py batches/B01_picks.yaml` → `research/alpha_distillation/B01_summary.md`。
4. 各研究 `lab_findings` 合并进 `lab/findings.yaml`;commit;更新记忆。

## 硬规矩(对谁都一样)

- **留出段每条因子只读一次**。`runs/<fid>/ledger.json` 里有 holdout 记录就绝不再读;候选的留出段数字都在 `final.json`。
- 服务器上有别人的任务:不杀不是自己起的进程,不碰 `/root/autodl-tmp/AlphaCube`,计算只通过 `scripts/study.sh`。
- 选拔口径是**多头腿净超额 / 纯多头夏普**(半衰期按纯多头书选);延长半衰期带来的净超额是有效的。
- Mac 要开盖、插电(合盖或过热会断网,所有 agent 一起死)。
