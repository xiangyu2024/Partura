# F109_erm_mag_gap_5m_tsm20 — 交接状态

_自动生成于 2026-10-05 11:13(`python scripts/recorder.py --brief F109_erm_mag_gap_5m_tsm20` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:手写 erm_mag_gap_5m_tsm20(批次 B01_single_factors)
- 表达式:`ts_mean(sub(div(div(day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95)), sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), create_like(Close, 0))), add(day_sum(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95))), create_like(day_quantile(Ret, 0.95), 1e-06))), add(day_quantile(Ret, 0.95), create_like(day_quantile(Ret, 0.95), 1e-06))), div(div(day_sum(select_where(is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05)), abs_(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1))), create_like(Close, 0))), add(day_sum(is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05))), create_like(day_quantile(Ret, 0.05), 1e-06))), add(abs_(day_quantile(Ret, 0.05)), create_like(day_quantile(Ret, 0.05), 1e-06)))), 20)`

## 现在到哪一步

- **阶段:全部完成**
- **留出段已经读过 1 次**(10-04 15:19)—— **不许再读**。候选在留出段上的数全在 `runs/F109_erm_mag_gap_5m_tsm20/final.json`(`./scripts/study.sh digest F109_erm_mag_gap_5m_tsm20 final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `study:F109_erm_mag_gap_5m_tsm20`:已返回结果,最后动作 10-05 00:00 → `handoff/F109_erm_mag_gap_5m_tsm20/agents/study_aa16cdd06605b6095.md`
  - `audit-numbers:F109_erm_mag_gap_5m_tsm20`:已返回结果,最后动作 10-05 00:14 → `handoff/F109_erm_mag_gap_5m_tsm20/agents/audit-numbers_ae5d6ae4559cdb8a5.md`
  - `synth:F109_erm_mag_gap_5m_tsm20`:还在跑(多半就是你自己)

**接手的人该做什么:** 这条因子做完了。最终结论在 `handoff/F109_erm_mag_gap_5m_tsm20/results/` 里最新的那个(revised.json 优先,否则 study.json)。

## 研究现状(`notes/F109_erm_mag_gap_5m_tsm20/state.md`,10-04 23:56 更新)—— **先读这个文件**

# F109_erm_mag_gap_5m_tsm20 — 研究现状(主研第 6 轮覆盖重写,2026-10-04)

> **研究已完成并交出结构化结果。结论:分辨。** 本轮(第 6 轮)无新实验、0 次服务器运行、没有读留出段,
> 只做三件事:(a) 通读 R3 结果卡,把执行报上来的 2 条数字不一致**直接改在 notes 里**;
> (b) 重出报告;(c) 填结构化结果。**候选没改、推荐没换**(留出段的规矩)。

## 1. 一句话现状

**`status: done`。结论 = 分辨;`recommended_kind = known_family`,推荐 = 用户已有的 `cross_mean(day_std(Amt), 30)`(变体 id `f_fam30`),
本因子没有任何提纯 / 升华产物。** 14 条假设全部有结论,留出段已读(1 次,tag `S_final`),01~12 全部成文,
报告在 `research/alpha_distillation/F109_erm_mag_gap_5m_tsm20.md`。
**接手者不需要再做任何事** —— 除了 `12_next.md` 第 1 条(那是**另一条研究**,不挂在 F109 上)。

(…全文 7392 字符,读 `notes/F109_erm_mag_gap_5m_tsm20/state.md`)

## 研究日志(`notes/F109_erm_mag_gap_5m_tsm20/journal.md`:19 条,其中研究员自己写的 11 条)

最近的 5 条(更早的和全文看文件):

### 2026-10-04 23:22 [主研] 第 5 轮:裁决判据 A~G,结论维持分辨;发现并修正多空口径标签错误;写完全部判断类 notes,下 writeup 工单 R3

我是第 5 轮主研(新工作流第 3 轮)。留出段已读、R2 有结果卡 → 本轮做 (c) 成文,没有开任何新实验、没有跑服务器。

看到了什么(逐条裁决写进 10_distilled.md「读完留出段之后」):
1. **七条判据五条过,没有一条触发推翻主结论的否定条件。** 判据 B(可信性锚)f_fam30 holdout +14.10%/1.509,
   落在事前写的 +10%~+18% / ≥1.1 里,整张表可比。判据 C 压倒性通过:三条结构候选比家族低 16.43 / 11.16 / 15.32 个点,
   其中 f_sig、f_lvl 在留出段直接翻负(−2.33% / −1.22%)。判据 E 通过(f_lvl −1.22%,valid 的 +12.0% 确是 2022–23 风格)。
2. **判据 D 干净到极点,把 H11 钉死了**:sub→add 在样本内值 +6.57pp(utrain +3.36% vs −3.21%),
   在留出段只值 +0.06pp(+2.95% vs +2.88%)。两种写法在留出段收敛到同一个数 —— 「减法是缺陷」只在样本内成立。
3. **判据 A 保住了主结论,但预测的夏普那一半失手 0.21**(事前写 <0.5,实际 +0.713),而且原式多头腿
   从 utrain −3.21% 变成 holdout +2.88%,是符号翻转(2024 +4.65%、2025 +3.32%,而 train 六年全负)。
   我没有事后改口:否定条件(≥+10% 且 ≥1.0)远未触及,+2.88% 在噪声带(±3 点)内与 0 不可区分、比家族低 11.2 个点,
   所以主张从「多头腿不可用」软化为「多头腿不具备竞争力」,符号翻转本身写进 09_diagnosis.md 的「未决」。
4. **判据 F 后半在 2024 年被否定**(事前写三条结构候选两年都 <+5%,实际 2024 是 +8.84%/+9.99%/+11.06%,
   两条还高于家族自己的 +9.17%;2025 年则全部 −1.92%~−12.66%)。按判据 F 原文的要求写进 11_risks.md 第 6 条。

5. **本轮最重要的一条新事实**:原式的空头腿在留出段毫发无损 —— 空头腿毛超额 utrain +32.71%
…(这条日志还有后文,读 journal.md)

### 2026-10-04 23:42 [执行] R3:补齐01_expression.md,14组(88条细项)数字核对完成(2条不一致),R2第3节hlL/hlS标签更正已追加,报告重出并通读,0次服务器运行

结果卡 notes/F109_erm_mag_gap_5m_tsm20/results/R3.md。

核对结论:88条细项里86条一致,2条不一致(均只报告,未改判断类notes):
1) f_orig 正年数:工单写2/8,diagnostics.by_year读出3/8(2022 +0.38%、2024 +4.65%、2025 +3.32%三年为正)。
2) f_fam30"固定hl20下+12.6%":sweep表hl=20的真实值是+8.39%/夏普1.209;+12.6%/夏普1.78精确等于hl=0那一行
   (=f_fam30自己选中的hl_used)。检索过08_variants/09_diagnosis/10_distilled/state/journal里全部出现处,
   笔记本身从未把+12.6%字面标成hl20,只是本工单第2节的表头把它和a_sig/a_sum/v_base并列在"固定hl20下"造成歧义。

其余14组(含判据C/D差值、hlS权威多空表、八年均值、holdout rIC、固定半衰期表、f_lvl两口径hl、sign、cov/dist门槛、
rank_corr_train)逐一核对后数字均对得上(JSON原始值与工单一致,或差在0.01~0.04pp的正常舍入内)。

报告:research/alpha_distillation/F109_erm_mag_gap_5m_tsm20.md,1910行/112918字符/46张表。01~12全部进了报告(含
新建的01_expression.md);S2_family 4条无数据处有完整说明文字,无静默空表格;结论"分辨"5处一致,f_fam30两处
均标注"不是这条因子的产物"。

新建:01_expression.md(37行,表达式与yaml逐字节校验一致)。追加(未删改原表):results/R2.md 第3节后的
"更正"小节,把hlL/hlS标签错误列清楚。一次性核对脚本未进Partura仓库。

### 2026-10-04 23:57 [主研] 研究完成:推荐 f_fam30(= 已知家族 cross_mean(day_std(Amt),30)),结论 分辨;本轮核对改正 2 处笔记数字、重出报告、交结构化结果

我是第 6 轮主研(成文后的最后一道核对)。0 次服务器运行、没有读留出段、没有动候选与推荐。

做了三件事:
1) 通读 results/R3.md(88 条细项、2 条不一致),判定两条都是**笔记里的数字标签错、不是结论错**,按规矩直接改 notes:
   (a) f_orig 正年数 2/8 → **3/8**(by_year 读出 2022 +0.38%、2024 +4.65%、2025 +3.32%;原来漏数了 2022 那个 +0.38%)。
       改了 09_diagnosis.md 一.4 与三.1、11_risks.md §6、state.md §2。实质不变:+0.38% 在噪声带内,
       「多头腿不具备竞争力」的措辞不受影响。
   (b) 「固定 hl20 下家族 +12.6%(1.78)」是口径张冠李戴:sweep 表 hl=20 上家族是 **+8.4%(1.21)**,
       +12.6%/1.78 是 hl=0(家族自己的 hlL)那一行。改了 09_diagnosis.md 一.6、05_hypotheses.md H9 行、state.md §2。
       结论方向不变(固定 hl20 下 a_sig +2.3% vs 家族 +8.4%,仍差 6 个点;家族自选口径则差 10 个点)。
       执行说「笔记从未字面标成 hl20」这点我不接受:state.md/09/05 这三处确实把家族的数字摆在「固定 hl20 下」这句话里,
       属于审查点名的「把平滑的功劳写成结构的 / 数字张冠李戴」,所以照改。
   **10_distilled.md 一个字没动** —— 事前预注册 + 事后裁决是冻结件,而且它写的是「第二条基准(已知家族)」,
   指家族自己的 hlL=0,按用户定的基准口径本来就对。
2) 重跑 ./scripts/study.sh report(1914 行),核对两处改正都已进报告(1432/1744/1438 行,与第 853 行的固定半衰期表一致)。
3) 填结构化结果:verdict 分辨,recommended_kind = known_family,recommended_id = f_fam30
   (留出段多头腿净
…(这条日志还有后文,读 journal.md)

### 2026-10-05 00:12 [审查-数字与流程] 10_distilled.md 第14行「第二条基准(已知家族)是+12.6%/1.78」紧跟在「同一半衰期hl20下a_sig+2.3%」之后未重新声明口径,与09_diagnosis/05_hypotheses/state.md三处已改正的同一错误(该数字实为家族自选hl0,固定hl20上家族是+8.4%/1.21)同源但未同步修正;研究员以「10_distilled.md是冻结的事前预注册件」为由未改。定性:minor——不影响结论,报告正文H9表与09_diagnosis对应段落(行488、1438-1440)已正确双标注并带⚠更正说明,只有10_distilled.md的冻结段落和报告中对它的逐字复现(约行1538)留有歧义措辞。

对比:
- notes/F109_erm_mag_gap_5m_tsm20/10_distilled.md 第12-14行(读留出段之前,写于主研第4轮,未改动):
  "10 个结构变体在同一半衰期 hl 20 下最好的是 a_sig +2.3%(夏普 0.31)...第二条基准(已知家族)是 +12.6% / 1.78。"
  —— 第三句未重申"已知家族"在哪个hl上,紧接在"hl20"语境后易被读成"同一hl20下家族是+12.6%"。
- runs/F109_erm_mag_gap_5m_tsm20/S_final.json sweep: f_fam30 在 hl20 上 Lnet=+8.4%、Lshp=1.21(非 +12.6%/1.78,
  后者是 hl0 = f_fam30 自己的 hlL)。
- 对照三处已修正的同一错误(study.json tooling_problems 第1条、journal.md 10-04 23:57 条目):
  09_diagnosis.md 一.6、05_hypotheses.md H9 行、state.md §2 均已把"固定hl20下家族+12.6%"改成"+8.4%(1.21);
  家族自选hl0则是+12.6%/1.78"。10_distilled.md 原文一字未动。
- 报告正文已修正且清晰双标:research/alpha_distillation/F109_erm_mag_gap_5m_tsm20.md 行488
  "固定 hl20 下最好的结构变体 +2.3%(夏普 0.31)vs 同一 hl20 上的家族 +8.4%(1.21)(家族自选 hl0 则是 +12.6%/1.78;
…(这条日志还有后文,读 journal.md)

### 2026-10-05 00:13 [审查-数字与流程] 审查完成:核对 40+ 个数字(S_final/S1_lvl/S0_baseline的books_user/by_rank/diagnostics.by_year原始JSON、x1_anatomy.log、x2_incremental.log逐一核对)全部精确对上;留出段只读1次(ledger确认)、S_final 5候选含原式与已知家族、10_distilled.md预注册时间戳(15:01)早于holdout读取(15:14)、推荐全程未变;S0复现published表在容差内;S_final全部候选cov/dist=1.00/1.00;自写脚本未触碰holdout;git status在partura/scripts/lab/docs下干净。仅1条minor(见上一条日志,10_distilled.md残留口径歧义措辞,不影响结论)。未发现critical/major问题。

方法:逐条对照 journal.md/09_diagnosis/10_distilled/11_risks/08_variants/state.md/study.json 里引用的数字与
runs/F109_erm_mag_gap_5m_tsm20/{S0_baseline,S1_lvl,S_final}.json 的原始字段(books/books_user 的 splits 与
by_rank['ls']、diagnostics.by_year)、ledger.json、logs/*_x1_anatomy.log、logs/*_x2_incremental.log 逐一核对,
并手算 f_orig/f_fam30/f_sig/f_sum/f_lvl 的八年算术均值复核笔记里的汇总数。

## 工单与结果卡(`notes/F109_erm_mag_gap_5m_tsm20/orders/`、`notes/F109_erm_mag_gap_5m_tsm20/results/`)

- R1:工单 有,结果卡 有
- R2:工单 有,结果卡 有
- R3:工单 有,结果卡 有

## 配置里的实验计划(`configs/F109_erm_mag_gap_5m_tsm20.yaml`)

- 标题:5 分钟收益的上尾 / 下尾超阈均值比之差的 20 日均值;分母上的 1e-6 把涨跌停封板日变成事件记忆
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base
- **S1_nodes**(8 个变体):两本书各自由哪个节点决定:分母上的 ε(封板日的爆炸)、减法、上侧还是下侧、5 分钟对 1 分钟的尺度?
  a_eps3、a_sum、a_up、a_dn、a_1m、a_q5、a_evt、a_sig
- **S2_family**(4 个变体):规则区间是不是「偏度 / 彩票 / 低价」的另一种写法?多头腿在两侧的水平里还是在两侧的差里?
  b_skew1、b_skew5、b_max20、b_sig60
- **S2_level**(2 个变体):「水平」(上下两侧超阈均值之和)的多头腿是不是就是低价股效应?
  b_lvl、b_lvlq
- **S_final**(5 个变体):留出段:5 条最终候选(排序与判据见 notes/F109_erm_mag_gap_5m_tsm20/10_distilled.md「读留出段之前」)
  f_fam30、f_sig、f_orig、f_sum、f_lvl

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F109_erm_mag_gap_5m_tsm20`)

- `S0_baseline`  10-04 11:54  1 个变体  → `./scripts/study.sh digest F109_erm_mag_gap_5m_tsm20 S0_baseline`
- `S1_lvl`  10-04 14:06  10 个变体  → `./scripts/study.sh digest F109_erm_mag_gap_5m_tsm20 S1_lvl`
- `S_final`  10-04 15:19  5 个变体  → `./scripts/study.sh digest F109_erm_mag_gap_5m_tsm20 S_final`
- `sweep_s1`  10-05 11:05  193 个变体  → `./scripts/study.sh digest F109_erm_mag_gap_5m_tsm20 sweep_s1`
- `anatomy_s1`  10-05 11:09  0 个变体  → `./scripts/study.sh digest F109_erm_mag_gap_5m_tsm20 anatomy_s1`
- `x1_anatomy`(自写脚本的输出)  10-04 12:36  exit 0  → `logs/F109_erm_mag_gap_5m_tsm20_x1_anatomy.log`
- `S1_S2`(自写脚本的输出)  10-04 13:19  exit 97  → `logs/F109_erm_mag_gap_5m_tsm20_S1_S2.log`
- `x2_incremental`(自写脚本的输出)  10-04 14:22  exit 0  → `logs/F109_erm_mag_gap_5m_tsm20_x2_incremental.log`

## 已写的 notes(`notes/F109_erm_mag_gap_5m_tsm20/`)

`01_expression.md`(2K)、`02_operators.md`(2K)、`03_decomposition.md`(2K)、`04_grammar.md`(1K)、`05_hypotheses.md`(23K)、`06_baseline.md`(3K)、`07_S1_nodes.md`(7K)、`07_S2_level.md`(5K)、`07_neutralise.md`(4K)、`07x_1_anatomy.md`(10K)、`07x_2_incremental.md`(6K)、`08_variants.md`(7K)、`09_diagnosis.md`(8K)、`10_distilled.md`(14K)、`11_risks.md`(6K)、`12_next.md`(5K)、`journal.md`(30K)、`state.md`(11K)

## 自写的探针与分析脚本(`studies/F109_erm_mag_gap_5m_tsm20/`)

- `x1_anatomy.py`  10-04 12:17  F109 x1: what the tree is really ranking -- the epsilon blow-up anatomy.
- `x2_incremental.py`  10-04 14:19  F109 x2: for a long-only user, does this tree add anything to the known amount-

## 结构化结果(`handoff/F109_erm_mag_gap_5m_tsm20/results/`)

- `audit-numbers.json`
- `study.json`

报告:`research/alpha_distillation/F109_erm_mag_gap_5m_tsm20.md`(10-04 23:56 生成)
