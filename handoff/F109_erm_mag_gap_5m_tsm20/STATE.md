# F109_erm_mag_gap_5m_tsm20 — 交接状态

_自动生成于 2026-10-05 13:33(`python scripts/recorder.py --brief F109_erm_mag_gap_5m_tsm20` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:手写 erm_mag_gap_5m_tsm20(批次 B01_single_factors)
- 表达式:`ts_mean(sub(div(div(day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95)), sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), create_like(Close, 0))), add(day_sum(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95))), create_like(day_quantile(Ret, 0.95), 1e-06))), add(day_quantile(Ret, 0.95), create_like(day_quantile(Ret, 0.95), 1e-06))), div(div(day_sum(select_where(is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05)), abs_(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1))), create_like(Close, 0))), add(day_sum(is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05))), create_like(day_quantile(Ret, 0.05), 1e-06))), add(abs_(day_quantile(Ret, 0.05)), create_like(day_quantile(Ret, 0.05), 1e-06)))), 20)`

## 现在到哪一步

- **阶段:全部完成**
- **留出段已经读过 2 次**(10-04 15:19, 10-05 12:20)—— **不许再读**。候选在留出段上的数全在 `runs/F109_erm_mag_gap_5m_tsm20/final.json`(`./scripts/study.sh digest F109_erm_mag_gap_5m_tsm20 final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `study:F109_erm_mag_gap_5m_tsm20`:已返回结果,最后动作 10-05 00:00 → `handoff/F109_erm_mag_gap_5m_tsm20/agents/study_aa16cdd06605b6095.md`
  - `audit-numbers:F109_erm_mag_gap_5m_tsm20`:已返回结果,最后动作 10-05 00:14 → `handoff/F109_erm_mag_gap_5m_tsm20/agents/audit-numbers_ae5d6ae4559cdb8a5.md`
  - `synth:F109_erm_mag_gap_5m_tsm20`:已返回结果,最后动作 10-05 11:32 → `handoff/F109_erm_mag_gap_5m_tsm20/agents/synth_aa3609845243aa6a4.md`

**接手的人该做什么:** 这条因子做完了。最终结论在 `handoff/F109_erm_mag_gap_5m_tsm20/results/` 里最新的那个(revised.json 优先,否则 study.json)。

## 研究现状(`notes/F109_erm_mag_gap_5m_tsm20/state.md`,10-05 11:30 更新)—— **先读这个文件**

# F109_erm_mag_gap_5m_tsm20 — 研究现状(主研第 7 轮覆盖重写,2026-10-05)

> 本轮 = **批量扫描 s1(190 变体)+ 市场解剖的一次性综合**。0 次服务器计算(只用了 `table` / `src` / `ops` / `hypo` 四个只读命令),
> 没有读留出段,没有改候选、没有换推荐。产出两件:`notes/.../synthesis.md`(118 行)与 `studies/.../hypo.yaml`(40 条,全部 parse 通过)。

## 1. 现状

`status: done`(上一位研究员已交出结构化结果,结论 = **分辨**;推荐仍是用户已有的 `cross_mean(day_std(Amt), 30)`)。
本轮**没有推翻这个结论**,但把原因从「它是一条空头腿因子」细化成:

**这棵树里有两件被 `1e-6` 焊在一起的东西。**
(a) 一个「近 20 日有没有封板 / 冻结盘口」的**事件标记**(钱在空头腿、买不进,而且它住在已知族亏钱的那 6.5% 里);
(b) 一个「日内被资金推着走 → 回吐」的**活跃小盘反转信号**(去掉爆炸后多头腿 +4.5~5.1%、LTO 仅 1.7%,
但与已知族的活跃度倾斜共线,桶内中性后只剩 +0.4%)。
第二批 40 条假设就是去分别钉死这两件东西能不能各自站住。**留出段仍然只读过 1 次,绝对不许再读。**

(…全文 6128 字符,读 `notes/F109_erm_mag_gap_5m_tsm20/state.md`)

## 研究日志(`notes/F109_erm_mag_gap_5m_tsm20/journal.md`:20 条,其中研究员自己写的 12 条)

最近的 5 条(更早的和全文看文件):

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

### 2026-10-05 11:27 [主研] 批量扫描 s1 的综合

- 节点记号本地重建(后序 SSA,A..AC),与 R1_propose_draft.txt 对齐:承重 = D/H(5分钟收益+掩码,abl_D -17.4%)与 N 上的 1e-6(sub_N_sub -19.1%);
  惰性 = L/W 的 1e-6(sub_L_sub/sub_W_sub 与原式逐位同分 ρo 1.00)。名字骗人四处:5m 只在被测量、mag 只在下侧、两个 ε 不同质、ts_mean 是记忆不是平滑(窗口 5→40 全平)。
- 全表最大的一次结构收益 = 去掉上侧计数归一化:only_L_R / sub_J_day_first +5.1%(valid +14.0%)、sub_L_mul +4.9%、sub_W_div +4.5%(原式 -3.2%);
  整条下侧分支是损害(abl_AA/only_AA_R/sub_AA_* 五条同为 +2.6~2.7%);sub_Y_log +4.9% 之所以赚是 log 把 q05=0 的爆炸日变 NaN 丢掉。
- 解剖:原式只在「近15日有冻结盘口」(6.5%、段等权 -67.4%)+14.3% 与「上市不足250日」(7.1%)+5.0% 为正,其余所有段为负,且超配冻结段 +2.3pp —— 这就是 -3.2% 的来源。
- 去掉爆炸后的变体换了一片市场:创业板 +9~11.6%、小市值 +9.8~12.0%、成交额最高20% +10.8%(最低20% -6.2%),低波 +9.4% vs 高波 +0.4%,市场上涨 +8.2~13.1% vs 下跌 -4.6~0.4%;
  已知族恰好相反(持仓 +80.3pp 压在成交额最低20%、高波更强)。机制推断 = 活跃小盘的「日内被资金推着走 → 回吐」反转。
- 增量仍然没有:res_known -0.3%、bk_known/bk_liq +0.4%(且 dist 0.20 ✗)、overlay 六档全部低于家族 +15.4%。但 overlay 叠的全是多头腿为负的原式,对结构变体不公平 → 第二批补。
- 落盘:notes/synthesis.md(140 行)、studies/hypo.yaml 40 条全部 parse 通过(A 去归一化 / B 冻结状态 / C 错配 / D 拉升机制 / E 桶内与分段 / F 市场状态 / G 当筛子 / H 低相关新结构)。

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
- `sweep_s2`  10-05 12:16  243 个变体  → `./scripts/study.sh digest F109_erm_mag_gap_5m_tsm20 sweep_s2`
- `anatomy_s2`  10-05 12:20  0 个变体  → `./scripts/study.sh digest F109_erm_mag_gap_5m_tsm20 anatomy_s2`
- `sweepfinal_s2`  10-05 12:22  8 个变体  → `./scripts/study.sh digest F109_erm_mag_gap_5m_tsm20 sweepfinal_s2`
- `x1_anatomy`(自写脚本的输出)  10-04 12:36  exit 0  → `logs/F109_erm_mag_gap_5m_tsm20_x1_anatomy.log`
- `S1_S2`(自写脚本的输出)  10-04 13:19  exit 97  → `logs/F109_erm_mag_gap_5m_tsm20_S1_S2.log`
- `x2_incremental`(自写脚本的输出)  10-04 14:22  exit 0  → `logs/F109_erm_mag_gap_5m_tsm20_x2_incremental.log`

## 已写的 notes(`notes/F109_erm_mag_gap_5m_tsm20/`)

`01_expression.md`(2K)、`02_operators.md`(2K)、`03_decomposition.md`(2K)、`04_grammar.md`(1K)、`05_hypotheses.md`(23K)、`06_baseline.md`(3K)、`07_S1_nodes.md`(7K)、`07_S2_level.md`(5K)、`07_neutralise.md`(4K)、`07x_1_anatomy.md`(10K)、`07x_2_incremental.md`(6K)、`08_variants.md`(7K)、`09_diagnosis.md`(8K)、`10_distilled.md`(14K)、`11_risks.md`(6K)、`12_next.md`(5K)、`journal.md`(32K)、`state.md`(9K)、`synthesis.md`(9K)

## 自写的探针与分析脚本(`studies/F109_erm_mag_gap_5m_tsm20/`)

- `x1_anatomy.py`  10-04 12:17  F109 x1: what the tree is really ranking -- the epsilon blow-up anatomy.
- `x2_incremental.py`  10-04 14:19  F109 x2: for a long-only user, does this tree add anything to the known amount-

## 结构化结果(`handoff/F109_erm_mag_gap_5m_tsm20/results/`)

- `audit-numbers.json`
- `study.json`
- `synthesis.json`

报告:`research/alpha_distillation/F109_erm_mag_gap_5m_tsm20.md`(10-04 23:56 生成)
