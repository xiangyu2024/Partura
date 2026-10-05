# F111_spearman_qclose — 交接状态

_自动生成于 2026-10-05 11:06(`python scripts/recorder.py --brief F111_spearman_qclose` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #953(批次 B01_single_factors)
- 表达式:`ts_spearman(day_quantile(Close), 10)`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- 留出段:**还没读过**(只能读一次;读之前要在 `10_distilled.md` 里写下候选排序和判据)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `lead:F111_spearman_qclose#1`:已返回结果,最后动作 10-04 23:23 → `handoff/F111_spearman_qclose/agents/lead_R1_a9fca7853ab5edfd4.md`
  - `work:F111_spearman_qclose#1`:已返回结果,最后动作 10-05 00:09 → `handoff/F111_spearman_qclose/agents/work_R1_aae62ed0fb3b82fe7.md`
  - `lead:F111_spearman_qclose#2`:中断,最后动作 10-05 00:20 → `handoff/F111_spearman_qclose/agents/lead_R2_aeedf79bbeec0a00f.md`

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F111_spearman_qclose` 看服务器上的 tag,`./scripts/study.sh digest F111_spearman_qclose <tag>` 重看结果)。

## 研究现状(`notes/F111_spearman_qclose/state.md`,10-04 23:22 更新)—— **先读这个文件**

# F111_spearman_qclose 研究现状

> 主研每轮**覆盖重写**。最后更新:**第 3 轮主研(工作流计数第 1 轮),2026-10-04**。
> `ts_spearman(day_quantile(Close), 10)`,挖掘库 / #953。**只放结论和指针**:每条的推导、长表、
> 逐条裁决在 `04_grammar.md`、`05_hypotheses.md`(全部假设全文)、`06_baseline.md`(S0 全部数字)、
> `07_S1_whatis.md`、`07x_1_identity.md`(x1 全部数字)、`results/R1.md`。
> (本轮从 34 KB 压到 13.5 KB / 156 行,**仍略超 10 KB 的指导线**:§2 的数字是裁决 H4/H12 的直接依据,
> 删掉下一个人每轮要多开三个文件才能判。真要再瘦,先砍 §2.2 / §2.4 / §2.8 —— 它们已经定案、
> 且**不在** H4 的裁决路径上。)

## 1. 一句话现状

身份已定清、提纯已做完,只剩 **H4(相对已知家族有没有增量)** 和 **H12(窗口 `d`)** 两问。
R2 工单第 2 轮就写好了,但**上一轮执行被打断、没有结果卡**:`S2_window` 连挂两次 `exit 97`
(`w_last_50` 撑爆内存,§2.11)。本轮**没下新工单**,只给 R2 加了「修订 R2-a」(删 `w_last_50`、
block 优先级改 **B>A**、`F2` 变可选、第 1 项只许跑一次),按规矩把 **R2 原样交回执行**。
**下一轮(第 4 轮主研)**:读 `results/R2.md` → 裁决 H12/H4 → **直接进「读留出段」**(已可收口)。

(…全文 8456 字符,读 `notes/F111_spearman_qclose/state.md`)

## 研究日志(`notes/F111_spearman_qclose/journal.md`:19 条,其中研究员自己写的 9 条)

最近的 5 条(更早的和全文看文件):

### 2026-10-04 23:29 [auto] 启动 run S2_window:阶段 S2_window

### 2026-10-04 23:52 [auto] 启动 exec x2_increment:studies/F111_spearman_qclose/x2_increment.py

### 2026-10-04 23:58 [auto] x2_increment 跑完(exit 0);重看结果:logs/F111_spearman_qclose_x2_increment.log

### 2026-10-05 00:06 [执行] R2:S2_window(删w_last_50后7个变体)和x2_increment(block A-E)都exit 0,结果卡见results/R2.md

第1项 S2_window:按修订R2-a删掉w_last_50(4处:variants/corr_ids/neutralise/profile)后reran,
exit 0,290.2s,peak anon 5.36GiB(此前两次exit 97的w_last_50已彻底移除)。BESTW按改动2规则选出
p_last_30(=ts_pearson(day_last(Close),30)),hlL=3,Lnet train+11.6%,5个候选里最高。

第2项 x2_increment.py(新写):F1=ts_spearman(day_last(Close),10)固定,F2=BESTW=p_last_30。
block A组合书30行:w=1时3条known家族逐位一致(F1 Lnet_tr+10.38%,F2 Lnet_tr+12.41%,PASS);
w=0行与R1数字14接近但不逐位相等,差值量级(Lnet -0.57~-0.67pp,Lshp -0.08~-0.09)落在R1自己
记录的0.3~0.9pp区间内,known_stdamt_max9这条hlL从5变2、LTO差1.6~1.9pp,比另两条家族明显大。
block B双重排序5本书:30%池覆盖率约0.29~0.30、多头端中位105~140只;10%池覆盖率约0.097、
中位35~46只,F1在两条known家族上单侧LTO都偏高(14.75%~19.44%)。block C残差(6行,主口径①):
F1对3条known家族R²=0.066/0.111/0.101(与R1的v_base版0.068/0.109/0.101高度吻合),F2对应R²=
0.127/0.126/0.129——F2的原始面板R²比F1高,但S2_window的rank_corr_train(平滑交易信号口径)显示
F1对known家族的|相关|反而比F2高(0.35~0.41 vs 0.30~0.35),两个口径排名相反,已写进结果卡"值得
注意"。block D:F1多头端(Q10)在ctl_amt/ctl_cap/ctl_ivol/ctl_dvol20/known_stdamt_mean30上全部
单调降到最低百分位(0.28~0.42),即多头端是"更不活跃更小更低波动"的票。block E:
…(这条日志还有后文,读 journal.md)

### 2026-10-05 00:07 [执行] R2 勘误:上一条日志的服务器运行计数写错了,更正如下

上一条[执行]日志里"全研究累计6次...还剩4次"这句话前后口径不一致,混用了两种计数方式,更正:

playbook §4 原文:"全研究的服务器运行控制在 8 次以内(含 final；不含预先跑好的 S0)"。按这个口径(不算
S0,S2_window 两次 exit 97 的中断重试按同一个 tag 只算一次,不是三次),已用的是:S1_whatis(1)+
x1_identity(2)+S2_window(3,本轮跑成)+x2_increment(4)= 4 次,与工单原文"都 exit 0 之后全研究还剩
4 次(含最后的 final)"的说法一致(8-4=4)。上一条日志里把 S0 和 S2_window 的两次 exit 97 也计入
"累计6次"是我自己多算的,不是这项研究的计数口径,后面不要沿用那句话里的"6次"。

## 工单与结果卡(`notes/F111_spearman_qclose/orders/`、`notes/F111_spearman_qclose/results/`)

- R0:工单 —,结果卡 有
- R1:工单 有,结果卡 有
- R2:工单 有,结果卡 有

## 配置里的实验计划(`configs/F111_spearman_qclose.yaml`)

- 标题:(读完这棵树之后,用一句话写它是什么)
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base
- **S1_whatis**(6 个变体):ts_spearman 的全市场两两配对平均,等价于什么更简单的东西?预测力的载体是价格路径、活跃度,还是实现细节?
  m_mktcorr、s_pearson、l_mean、l_last、l_amt、t_tsrank
- **S2_window**(7 个变体):窗口 d 这根轴上有东西吗?10 天只是任意选择,还是 5~50 里有一个明显更好的频段?
  a_last_10、w_last_5、w_last_20、w_last_30、w_q_30、pl_last_10、p_last_30

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F111_spearman_qclose`)

- `S0_baseline`  10-04 11:54  1 个变体  → `./scripts/study.sh digest F111_spearman_qclose S0_baseline`
- `S1_whatis`  10-04 14:05  6 个变体  → `./scripts/study.sh digest F111_spearman_qclose S1_whatis`
- `S2_window`  10-04 23:34  7 个变体  → `./scripts/study.sh digest F111_spearman_qclose S2_window`
- `sweep_s1`  10-05 10:54  73 个变体  → `./scripts/study.sh digest F111_spearman_qclose sweep_s1`
- `anatomy_s1`  10-05 10:58  0 个变体  → `./scripts/study.sh digest F111_spearman_qclose anatomy_s1`
- `x1_identity`(自写脚本的输出)  10-04 14:23  exit 0  → `logs/F111_spearman_qclose_x1_identity.log`
- `x2_increment`(自写脚本的输出)  10-04 23:58  exit 0  → `logs/F111_spearman_qclose_x2_increment.log`

## 已写的 notes(`notes/F111_spearman_qclose/`)

`01_expression.md`(3K)、`02_operators.md`(9K)、`03_decomposition.md`(4K)、`04_grammar.md`(11K)、`05_hypotheses.md`(34K)、`06_baseline.md`(12K)、`07_S1_whatis.md`(7K)、`07x_1_identity.md`(14K)、`journal.md`(32K)、`state.md`(13K)

## 自写的探针与分析脚本(`studies/F111_spearman_qclose/`)

- `x1_identity.py`  10-04 14:17  R1 exec script -- the identity + conditioning + known-family + tie analysis.
- `x2_increment.py`  10-04 23:51  R2 exec script (修订 R2-a) -- block A/B/C/D/E: does F1/F2 give a long-only user

## 结构化结果(`handoff/F111_spearman_qclose/results/`)

(还没有)
