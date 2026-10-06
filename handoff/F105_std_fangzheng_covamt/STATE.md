# F105_std_fangzheng_covamt — 交接状态

_自动生成于 2026-10-05 19:23(`python scripts/recorder.py --brief F105_std_fangzheng_covamt` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #25(批次 B01_single_factors)
- 表达式:`ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5)`

## 现在到哪一步

- **阶段:全部完成**
- **留出段已经读过 2 次**(10-03 23:11, 10-05 11:58)—— **不许再读**。候选在留出段上的数全在 `runs/F105_std_fangzheng_covamt/final.json`(`./scripts/study.sh digest F105_std_fangzheng_covamt final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `synth:F105_std_fangzheng_covamt`:已返回结果,最后动作 10-05 11:21 → `handoff/F105_std_fangzheng_covamt/agents/synth_a1530a507fb533732.md`
  - `verdict:F105_std_fangzheng_covamt`:中断,最后动作 10-05 13:53 → `handoff/F105_std_fangzheng_covamt/agents/verdict_a769b59a5d9769c01.md`
  - `verdict:F105_std_fangzheng_covamt`:已返回结果,最后动作 10-05 15:18 → `handoff/F105_std_fangzheng_covamt/agents/verdict_abf3a5599890322c7.md`

**接手的人该做什么:** 这条因子做完了。最终结论在 `handoff/F105_std_fangzheng_covamt/results/` 里最新的那个(revised.json 优先,否则 study.json)。

## 研究现状(`notes/F105_std_fangzheng_covamt/state.md`,10-05 15:10 更新)—— **先读这个文件**

# F105_std_fangzheng_covamt —— 状态(主研,2026-10-05,基于批量扫描 s2 的 132 个变体 + 市场解剖)

原式:`ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5)`(挖掘库 #25)
口径:多头腿扣 15bp 净超额 Lnet / 纯多头夏普 Lshp(半衰期按纯多头书选)。噪声 ±3 点 / ±0.3 夏普。门槛 cov ≥ 0.95、dist ≥ 0.5。
基准:`k_known` = `cross_mean(day_std(Amt), 30)` = ut +15.4,Lshp 2.22;
**`k_known_xfrozen`**(已知族剔掉近 15 日冻结盘口最重的 20%)= ut **+18.5**,Lshp **3.15** ← 真正的标尺。
**测试段一次都没读过**(`sweepfinal_*.json` 未打开),也不该读。

## 1. 现状

**定论:只是已知族,而且是劣化写法。否掉。**
v_base = +9.3 / +18.2(ut +11.8),Lshp 1.96,ρk 0.72。三条路全是零增量:
信号(输 k_known 3.6 点)、筛子(`scr_xhi_p` +15.2 / 2.21 vs k_known +15.4 / 2.22 = 一点没涨)、
叠加(`ov_p025/05/10` = +15.0 / +14.6 / +14.5,全部 ≤ k_known)。
不是提纯:最强的 `iso_A = day_cov(Amt,Amt)` ≡ `day_var(Amt)` 虽然 ut +17.8 / 2.59,但 **ρk 0.97 = 同一条因子**。
不是升华:没有任何版本给出已知族之外的新内容(autocorr 线索已按预先登记的判据作废)。
已交付:`synthesis.md`(+ §「第二轮(s2)对账与结论」)、`hypo.yaml`(34 条)、`hypo3.yaml`(25 条,25/25 parse)。

(…全文 6326 字符,读 `notes/F105_std_fangzheng_covamt/state.md`)

## 研究日志(`notes/F105_std_fangzheng_covamt/journal.md`:3 条,其中研究员自己写的 3 条)

最近的 5 条(更早的和全文看文件):

### 2026-10-05 11:16 [主研] 批量扫描 s1 的综合

- 它是什么:day_cov(Amt,Amt) 按定义就是 day_var(Amt)(假协方差);cross_fangzheng = 近一年 mean+std 的上轨(不是正规化);
  根 ts_stddev(·,5) 读的是"这条年度上轨上周动了多少"。整棵树 = 一条绕了四层的成交额水平读数,sg=-1 买低流动性。
- 提纯:isolate 阶梯单调下坡 iso_A +17.8/2.59 → iso_B +17.2 → iso_C +12.3 → v_base +11.8;abl_B/abl_C 删节点反而 +1.4/+2.1。
  承重只有两件:Amt 必须以水平进来(rel60 +5.3、mem_zscore 全负、leaf in_pct -0.1% 且 sg 翻号),根必须是幅度型归约。
  三条窗口梯子全在 ±1 噪声内 = 纯水平代理的签名。叶子不可换:Amt→Volume 只剩 +6.9%(valid +3.8%),价这一维值约一半。
- 增量 = 0:ρk 0.72,res_known +2.3%/0.51、bk_known +2.4%/0.50,三条正权重 overlay 全 ≤ k_known 单独的 +15.4/2.22。按口径应否掉。
- 市场:钱全在"买低成交额这一段"的倾斜(最低桶超配 +55.2pp、段等权超额 +15.1%),段内净超额 -4.7/-2.9/-0.0/+4.2/+1.2。
  市值桶段内处处为正(+3~+9%)→ 真实内容是"同市值内选低换手",要中性化的是市值而立方体没有这个字段。
- 结构性缺陷:含 ts_stddev(·,5) 的变体在次新(-23.2% vs iso_A +6.1%)、科创板(-15.7% vs +4.9%)、封板(-11.5% vs +10.4%)
  全崩,不含的全不崩(7比7/3比3);abl_C 没有 241 窗口却最差,所以罪魁是根这个"抖动"读法,不是年窗口。
- 唯一线索:sub_D_ts_autocorr_s1 Lshp 2.46、空头腿只 +11.7/+13.2(全表唯一钱在多头腿的行),但 dist 0.46 ✗。已写成 F 组 5 条假设。

### 2026-10-05 13:51 [主研] 批量扫描 s2 对账与结论

对账(132 变体):原子被钉死 —— h_atom_var_m30 / h_atom_std_max3 / h_atom_log_m30 的 ρk 全是 0.99,day_cov(Amt,Amt) ≡ day_var(Amt),"covamt" 作废。机制证实:解剖次新段内 iso_A +6.1% vs v_base −23.2% = 29.3pp,与上一轮预言的 ~30pp 一致。段内(同流动性桶内日内形状)= 零(四条 +2.6 ~ −7.9,dist 已修好)。autocorr 线索按预先登记判据作废(h_ac_atom5/10 dist 0.08 / 0.04 ✗;搬到 log 成交额与日内波动 −11.8 / −10.7 = 不迁移)。
两条被推翻的上一轮结论:(1)"去尺度一律死"错了 —— h_leaf_logchg_var(无尺度)+10.3% / ρk 0.82,死的是 in_pct 这个算子;(2) 三条门控假设全是写法 bug —— cs_last_high20 把筛出的票压到排序最后,y 必须套 neg() 让 sg = +1,漏了就变成专买被筛掉的票(seg_xfrozen_p +1.7 vs seg_xfrozen_m +13.3),外加 cross_valid_count(·,241) 93% 饱和。
定论:**只是已知族,劣化写法,否掉。** 信号输 k_known 3.6 点;筛子 scr_xhi_p +15.2 / 2.21 ≈ k_known +15.4 / 2.22(零增益);所有 overlay ≤ k_known。自家最好 seg_xfrozen_m(ut +13.3 / 2.75、ρk 0.37)与 h_root_tail75_241(+12.5 / 1.97、LTO 仅 1.5%)都输给新标尺 k_known_xfrozen(+18.5 / 3.15)——全表唯一真赚钱的东西是**通用冻结盘口筛子**,与本因子无关。
第三批 25 条已落盘(hypo3.yaml,25/25 parse):cross_age 重做年龄门与段内方向反转对、cs_bucket_zscore × 价格桶(唯一不由 Amt 构成的规模代理)、day_at_max/min_ratio + cross_flat_ratio 拆开冻结筛子并首次扫宽度、cross_semistd_pos/neg 拆根的符号、cross_madz 分清"去水平不对 vs 估计量脆"、
…(这条日志还有后文,读 journal.md)

### 2026-10-05 15:10 [主研] 批量扫描 s2 对账与结论(复核与补遗)

复核了 s2 全表(132 变体 + 解剖十列)与已落盘的两份文字,每个数字逐行对上,结论不变:**只是已知族,劣化写法,否掉**。hypo3.yaml 重跑 25/25 parse。测试段仍未读。
新发现一条读表陷阱(已写进 state.md §8):解剖表的"段内净超额"在**持仓被清空的段**里是退化读数,不能当业绩看 —— seg_xfrozen_m 在冻结段 −153.6%、seg_new_p 在次新段 −60.7%,而两者括号里的超配恰好 ≈ −(该段占比) → 持仓 0。判别只看括号,不看百分数。这解释了为什么 s2 里几条筛子变体的段内列看着像灾难。
回答用户关心的"融合 + 平滑":对本因子两条路都已有现成读数,不需要新算。**融合**(与已知族按秩叠加)ov_p025 / ov_p05 / ov_p10 = ut +15.0 / +14.6 / +14.5、Lshp 2.20 / 2.18 / 2.19,全部 ≤ k_known 单独的 +15.4 / 2.22,且权重越大越差;负权重 −4.5 ~ +10.3。**平滑**(memory 一族 5/10/30/60 日)最好 mem_max30 ut +12.8 / 2.17 vs v_base +11.8 / 1.96,只 +1.0 点 / +0.2 夏普 = 噪声内,且 cross_min 那一支崩掉(+6.9 ~ −3.4)。
结论:融合与平滑都救不了这条因子;本因子唯一能让人赚到钱的用法是把**通用冻结盘口筛子**套上去(seg_xfrozen_m ut +13.3 / 2.75、ρk 0.37),而同一个筛子给已知族更多(k_known_xfrozen ut +18.5 / 3.15)—— 所以赚的是筛子,不是 F105。
样本内外一致性(train 2018–2021 / valid 2022–202308):v_base +9.3% → +18.2%、k_known +12.6% → +22.3%、k_known_xfrozen +16.4% → +23.2%、seg_xfrozen_m +11.4% → +16.5%。排序在两段上完全不变,没有样本内外翻转,只是 valid 段整体更肥(2022 微盘年)。

## 配置里的实验计划(`configs/F105_std_fangzheng_covamt.yaml`)

- 标题:分钟成交额方差的一年期 mean+std 水平在最近 5 天的变化量 —— 带成交额平方尺度的「放量事件进入/滑出一年窗口」探测器
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base
- **S1_what**(3 个变体):原式的预测力在哪一样东西里:成交额尺度(水平)、还是事件的方向?它和已知家族 cross_max(day_std(Amt),9) 比怎么样?
  s1_level、s1_signed、s1_known_stdamt9
- **S1b_events**(3 个变体):把成交额尺度除掉之后,「事件」这一半自己还剩多少?硬窗口的周年回声、一年窗口本身,是在挣钱还是在稀释?
  s1_relchg、s1_noecho、s1_recent
- **S2_nodes**(10 个变体):树里哪些节点是多余的:3 日极值、fangzheng 的 mean 项 / std 项、日内方差这个字段、241 和 5 这两个窗口?把外层 std 换成 |5 日差分| 能不能去掉上市首日的伪影?
  s2_dtface_check、s2_no_max3、s2_mid_std、s2_mid_mean、s2_min3、s2_field_std、s2_field_sum、s2_w60、s2_out20、s2_absdelta
- **S3_family**(6 个变体):原式的水平部分 C 近似一年最大值(07x:scale-free rank 相关 0.984),已知家族是 9 日最大值:cross_max(day_std(Amt), d) 这一族里,多头腿净超额在哪个 d 上最好?长窗口下 max 还比 mean 好吗?
  s3_max241、s3_max20、s3_max60、s3_max120、s3_mean60、s3_mean241
- **S4_longleg**(6 个变体):已知家族 cross_max(day_std(Amt), d) 的多头腿在 d=20~60 上是稳定的平台,还是两个点的运气?多头腿要的是「没爆过量」(极值)还是「平时成交少」(中位数/均值)?原式的「事件」那一半写干净之后有没有多头腿?
  s4_max15、s4_max30、s4_mean20、s4_med60、s4_summax30、s4_pos
- **S_final**(5 个变体):只凭 train/valid 选出来的结论 ——「原式 = 已知家族的一个更吵的写法;换成 cross_max(day_std(Amt), 30) 多头腿更好」—— 在用户的测试段(20230808–20251231)上站不站得住?
  f_orig、f_min3、f_max15、f_max30、f_max60

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F105_std_fangzheng_covamt`)

- `S0_baseline`  10-03 17:43  1 个变体  → `./scripts/study.sh digest F105_std_fangzheng_covamt S0_baseline`
- `S1_what`  10-03 19:37  6 个变体  → `./scripts/study.sh digest F105_std_fangzheng_covamt S1_what`
- `S1b_S2_S3`  10-03 20:12  21 个变体  → `./scripts/study.sh digest F105_std_fangzheng_covamt S1b_S2_S3`
- `S2S3_nodes_family`  10-03 22:45  19 个变体  → `./scripts/study.sh digest F105_std_fangzheng_covamt S2S3_nodes_family`
- `S4_longleg`  10-03 22:57  6 个变体  → `./scripts/study.sh digest F105_std_fangzheng_covamt S4_longleg`
- `final`  10-03 23:11  5 个变体  → `./scripts/study.sh digest F105_std_fangzheng_covamt final`
- `sweep_s1`  10-05 10:47  91 个变体  → `./scripts/study.sh digest F105_std_fangzheng_covamt sweep_s1`
- `anatomy_s1`  10-05 10:52  0 个变体  → `./scripts/study.sh digest F105_std_fangzheng_covamt anatomy_s1`
- `sweep_s2`  10-05 11:46  134 个变体  → `./scripts/study.sh digest F105_std_fangzheng_covamt sweep_s2`
- `anatomy_s2`  10-05 11:57  0 个变体  → `./scripts/study.sh digest F105_std_fangzheng_covamt anatomy_s2`
- `sweepfinal_s2`  10-05 11:59  8 个变体  → `./scripts/study.sh digest F105_std_fangzheng_covamt sweepfinal_s2`
- `sweep_s3`  10-05 17:38  161 个变体  → `./scripts/study.sh digest F105_std_fangzheng_covamt sweep_s3`
- `anatomy_s3`  10-05 17:49  0 个变体  → `./scripts/study.sh digest F105_std_fangzheng_covamt anatomy_s3`
- `sweepfinal_s3`  10-05 17:59  8 个变体  → `./scripts/study.sh digest F105_std_fangzheng_covamt sweepfinal_s3`
- `x1_events`(自写脚本的输出)  10-03 19:28  exit 0  → `logs/F105_std_fangzheng_covamt_x1_events.log`
- `x2_longleg`(自写脚本的输出)  10-03 23:05  exit 0  → `logs/F105_std_fangzheng_covamt_x2_longleg.log`
- `audit1`(自写脚本的输出)  10-03 23:29  exit 0  → `logs/F105_std_fangzheng_covamt_audit1.log`
- `rev1`(自写脚本的输出)  10-03 23:51  exit 0  → `logs/F105_std_fangzheng_covamt_rev1.log`
- `rev2`(自写脚本的输出)  10-03 23:59  exit 97  → `logs/F105_std_fangzheng_covamt_rev2.log`

## 已写的 notes(`notes/F105_std_fangzheng_covamt/`)

`01_expression.md`(1K)、`02_operators.md`(1K)、`03_decomposition.md`(1K)、`04_grammar.md`(1K)、`05_hypotheses.md`(5K)、`06_baseline.md`(3K)、`07_S1_what.md`(4K)、`07_S1b_events.md`(6K)、`07_S2_nodes.md`(4K)、`07_S3_family.md`(4K)、`07_S4_longleg.md`(6K)、`07_S_final.md`(6K)、`07_conditional.md`(3K)、`07_controls.md`(1K)、`07_neutralise.md`(2K)、`07x_events.md`(8K)、`07x_longleg.md`(5K)、`07x_review_audit.md`(8K)、`07x_revision.md`(19K)、`08_variants.md`(3K)、`09_diagnosis.md`(11K)、`10_distilled.md`(13K)、`11_risks.md`(4K)、`12_next.md`(2K)、`journal.md`(5K)、`state.md`(9K)、`synthesis.md`(18K)

## 自写的探针与分析脚本(`studies/F105_std_fangzheng_covamt/`)

- `audit_1.py`  10-03 23:27  F105 audit (reviewer, mechanism / overfitting lens).  train / valid only -- never the holdout.
- `events.py`  10-03 18:42  F105: what orders the root, and which kind of stock-day earns the money.
- `longleg.py`  10-03 23:00  F105: why the slow members of the known family have a better long leg than the original,
- `probes.py`  10-03 18:37  Probes this tree needs: ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5).
- `rev1.py`  10-03 23:42  F105 revision 1 -- the researcher's follow-up to the two reviews.  train / valid only: every panel is cut at
- `rev2.py`  10-03 23:57  F105 revision 2 -- is the "entry event" result manufactured by the label's buyable filter?

## 结构化结果(`handoff/F105_std_fangzheng_covamt/results/`)

- `audit-mechanism.json`
- `audit-numbers.json`
- `revised.json`
- `study.json`
- `synthesis.json`
- `verdict.json`

报告:`research/alpha_distillation/F105_std_fangzheng_covamt.md`(10-04 12:08 生成)
