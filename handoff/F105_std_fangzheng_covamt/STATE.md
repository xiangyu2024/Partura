# F105_std_fangzheng_covamt — 交接状态

_自动生成于 2026-10-05 11:23(`python scripts/recorder.py --brief F105_std_fangzheng_covamt` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #25(批次 B01_single_factors)
- 表达式:`ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5)`

## 现在到哪一步

- **阶段:全部完成**
- **留出段已经读过 1 次**(10-03 23:11)—— **不许再读**。候选在留出段上的数全在 `runs/F105_std_fangzheng_covamt/final.json`(`./scripts/study.sh digest F105_std_fangzheng_covamt final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `audit-mechanism:F105_std_fangzheng_covamt`:已返回结果,最后动作 10-03 23:34 → `handoff/F105_std_fangzheng_covamt/agents/audit-mechanism_a634d8b8d73e7330b.md`
  - `revise:F105_std_fangzheng_covamt`:已返回结果,最后动作 10-04 00:19 → `handoff/F105_std_fangzheng_covamt/agents/revise_a05e6538df5a93b1b.md`
  - `synth:F105_std_fangzheng_covamt`:已返回结果,最后动作 10-05 11:21 → `handoff/F105_std_fangzheng_covamt/agents/synth_a1530a507fb533732.md`

**接手的人该做什么:** 这条因子做完了。最终结论在 `handoff/F105_std_fangzheng_covamt/results/` 里最新的那个(revised.json 优先,否则 study.json)。

## 研究现状(`notes/F105_std_fangzheng_covamt/state.md`,10-05 11:17 更新)—— **先读这个文件**

# F105_std_fangzheng_covamt —— 状态(主研,2026-10-05,基于批量扫描 s1 的 89 个变体 + 市场解剖)

原式:`ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5)`(挖掘库 #25)
口径:多头腿扣 15bp 净超额 / 纯多头夏普,半衰期按纯多头书选。噪声 ±3 点 / ±0.3 夏普。门槛 cov ≥ 0.95、dist ≥ 0.5。
基准 k_known = `cross_mean(day_std(Amt), 30)`:train/valid/utrain = +12.6% / +22.3% / +15.4%,Lshp +2.22。

## 1. 现状

**初步结论:否定 —— 就是已知成交额族,而且是它被四层包装削弱后的一个读法。**
v_base = +9.3% / +18.2% / +11.8%,Lshp +1.96,在两段、两条腿、两个分段维度上全面输给 k_known。
ρk = 0.72;正交部分 res_known +2.3% / Lshp 0.51、bk_known +2.4% / 0.50(dist 0.20 ✗);
三条正权重 overlay(+15.0 / +14.6 / +14.5)全部 ≤ k_known 单独的 +15.4,负权重更差。**增量为零。**
已交付:`notes/F105_std_fangzheng_covamt/synthesis.md`(≤150 行)、
`studies/F105_std_fangzheng_covamt/hypo.yaml`(34 条,34/34 parse)。

## 2. 中间结果(表里的数字,按 utrain 口径)

- isolate 阶梯单调下坡:`iso_A` day_cov 单独 **+17.8% / 2.59**(全表第一)→ `iso_B` +17.2 / 2.52 →
  `iso_C` +12.3 / 1.98(LTO 只 1.4%)→ `v_base` +11.8 / 1.96。
- ablate 删节点反而更好:`abl_B`(删 cross_max3)+13.2 / 2.15;`abl_C`(删 fangzheng241)+13.9 / 2.13。
- B 槽所有保尺度的替代都在 ±1:cross_sum 12.8 / fangzheng 12.4 / decay_linear 12.6 / q75 12.4 / q25 11.8 /
  med 11.1 / min 11.1;返回下标的 argmax / argmin 打死(−8.3 / −4.4)。
- C 槽:`sub_C_cross_mean` +12.3 ≈ 原式 → 方正的 `+cross_stddev` 那一半零贡献。
- D 槽:ts_var +12.0(单调孪生 ρo 0.99);ts_delta −9.1、ts_kurt −14.9(cov 0.39 ✗)、ts_hurst −17.6、
  ts_pearson/spearman ≈ 0 → 根必须是幅度型归约。
- 去尺度一族全死:rel60 +5.3(ρo 0.36 / ρk 0.19)、mem_zscore 5/10/30/60 = −4.5 / −3.0 / −2.1 / −0.1、
  **leaf_Amt_amtchg(in_pct)−0.1% 且 sg 翻成 +1**。
- 叶子:Volume 版 +6.9%(valid 只 +3.8%)、day_cov(Volume, Amt) +9.9% → Amt 里"价"这一维值约一半。
- 窗口三条梯子:win_D 5/10/20 = 11.8 / 11.6 / 12.0;win_B 3/5/10 = 11.8 / 11.1 / 10.9;
  win_C 241/60/30 = 11.8 / 11.4 / **12.5**(ρk 0.72→0.83)。全在噪声内 = 没有平台。
- memory:最好的 mem_max30 +12.8 / 2.17(hlL 10→1);cross_min 一支崩(+6.9 / +5.5 / −1.0 / −3.4)。
- `cs_winsor` no-op(+11.9)。`cs_rank` 略差(+11.0,LTO 7.6%)。

## 3. 过程与逻辑

按算子源码逐层读出:`day_cov(x,x)` = Σ(x−mean)²/count = **day_var**(名字里的协方差是假的);
`cross_fangzheng(X,241)` = `cross_mean + cross_stddev` = 近一年上轨(**不是正规化**);
`ts_stddev(·,5)` 与 `cross_stddev` 同一内核,读的是"年度上轨上周动了多少"。
整棵树因此是一条四重衰减的**成交额水平**读数,sg = −1 → 买低流动性。
解剖证实:多头书在成交额最低桶超配 **+55.2pp**,该段等权超额 **+15.1%/年**,
而**段内**净超额 = −4.7 / −2.9 / −0.0 / +4.2 / +1.2 → **钱全在段倾斜,段内排序是负贡献**(k_known、iso_A 同)。
市值桶段内却处处为正(+2.9 ~ +9.0,超配 +15.4pp → −17.7pp)→ 两个效应叠加:小市值倾斜 + 同市值内选低换手。
**真实身份:一条披着流动性外衣的换手率水平因子。**

结构性缺陷(最有价值的一条):十个被解剖的变体里,次新 / 科创板 / 封板三段的损伤与
**是否含 `ts_stddev(·,5)`** 完全对应 —— 含它的 7 个全崩([0] 次新 −23.2% / 科创 −15.7%,[4]…[9] 同向),
不含的 3 个全不崩([1] +8.6 / +1.4,[2] +6.1 / +4.9,[3] +6.1 / +6.9)。
`abl_C` 根本没有 241 窗口却在科创板最差(−22.2%)→ **罪魁是根这个"抖动"读法,不是年窗口。**
机制:次新 / 科创 / 刚封板的票日成交额方差序列本身就抖,抖动大在这些段里恰恰是"正在被炒"的标志,
所以段内抖动与水平的排序方向相反;叠加 `rolling_windows` 补 NaN 让短历史的年度上轨每天因重新估计而跳。

时间维度**不要再碰**:年份 / 涨跌 / 波动 / 离散 / 放量五组分布,k_known 与原式形状一模一样
(2020 +3.2 vs +6.7、2022 +26.1 vs +24.7;涨 +18.0 vs +23.0 / 跌 +4.2 vs +6.0)→ 择时属于小盘溢价,不属于这条因子。

## 4. 假设表(第二批,34 条,studies/F105_std_fangzheng_covamt/hypo.yaml,34/34 parse)

| 组 | 条数 | 在检验什么 |
|---|---|---|
| A 钉死原子 | 4 | day_var / day_std / log / 变异系数 —— 假协方差、水平 vs 尖峰记忆 |
| B 最小修补 | 5 | 根窗口下沿 3;方正 → q75 / cross_tail_mean_q75 / q25;两条尾巴的比值(无尺度) |
| C 承重否定测试 | 3 | in_logchg 替 in_pct(排除不对称这个替代解释)、day_var(Ret)、day_var(Close) |
| D 补 §3 的洞 | 6 | cross_valid_count / day_zero_ratio 做剔除器与段内倾斜,**含对照组 h_gate_both_atom** |
| E 段内有没有东西 | 6 | day_gini / day_centroid / day_signed_ratio / day_flat_run_max 的桶内排名 + cs_first_low40 孪生 |
| F 救活 autocorr | 5 | 换不那么平滑的内层、加水平 tie-break 补 dist、搬到 log 成交额与日内波动上 |
| G 大胆换原子 | 5 | day_gini / day_centroid / day_wmean(Ret,Amt) / in_madz —— 无尺度的日内形状 |

读第二批时的判据(先写下来):
- D 组 h_gate_newlist 若 **< +1 点**,§3 的机制说法被否;若 ≈ +2 点而对照组 h_gate_both_atom ≈ 0,机制成立。
- F 组 h_ac_atom5 / h_ac_atom10 若 dist 仍 < 0.5,autocorr 这条线索作废(它只是并列的伪影)。
- E / G 两组多数预期会死(rel60 / mem_zscore 已预言);**死也是结论**,不要重跑、不要加窗口。

## 5. 候选

**目前没有可推荐的候选。** 全表唯一值得记一笔的两行:
- `iso_A = day_cov(Amt, Amt)` ≡ `day_var(Amt)` = `day_std(Amt)²`:+15.6 / +23.3 / **+17.8%**,Lshp **+2.59**,
  LTO 3.8% —— 全表最好,比 k_known 高 2.4 点(**在 ±3 噪声内,不是改进**),但 **ρk = 0.97 = 同一条因子**。
- `sub_D_ts_autocorr_s1`:+11.3 / +13.4 / +12.0%,Lshp **+2.46**,LTO 9.6%,
  空头腿只 **+11.7 / +13.2**(原式 +23.6 / +28.5)—— **全表唯一钱在多头腿而不在空头腿的一行**,ρk 0.63,
  **但 dist 0.46 ✗**(年度上轨太平滑,自相关堆在 +1)。F 组 5 条就是去救它。

## 6. 后面的思路

1. 先看 D 组(6 条)—— 它是唯一一组"机制成立就能直接换来点数"的实验,而且自带对照组。
2. 再看 F 组 —— 唯一可能长出一条**新**因子的线索;若 h_ac_atom5/10 的 dist 还是不过,整条线作废。
3. E / G 两组是对"日内成交额形状里有没有信息"的一次性结算,看完就下结论,不要迭代。
4. A / B / C 三组是提纯与否定测试,主要产出是把 §1、§2 的论断钉死,不指望出候选。
5. **不要做的**:市场状态门控(§3 已证明择时属于小盘溢价)、再扫窗口(三条梯子全在噪声内)、
   任何试图把原式"修回来"的尝试(isolate 阶梯说上面每一层都在扣分,修的方向只有一个 —— 删)。

## 7. 留出段

**还没有碰测试段,也不该碰。** 按现在的证据这条因子应当被否掉(增量为零),没有值得花留出段的候选。
若第二批里 D 组或 F 组真的长出东西,`S_final` 只放 ≤ 5 条,必须含原式(新 id)+ k_known +(建议)iso_A 作第三条基准,
判据在跑之前写进 `notes/F105_std_fangzheng_covamt/10_distilled.md`。

## 8. 给接手者的提醒

- **先读 `synthesis.md`,再读 hypo.yaml 的头部注释**;两份里的每个数字都标了变体 id,不要重新跑大表。
- 工具问题三条(跑第二批时会再撞上):
  (1) **`cs_bucket_rank` 的 dist 还是塌**:bk_liq 0.20、bk_known 0.20,与 new_operators.md 说"已用全局秩 ×1e-4
      打破并列"不符 —— 要么 sweep 跑在修复之前,要么修复没生效。E 组 4 条 `h_bk_*` 可能整体被门槛误杀,
      所以我同时写了 `cs_first_low40` 的孪生(h_tilt_gini / h_tilt_lowvol)。**先确认这个再读 E 组。**
  (2) **`cross_ema` 在小 d 上会毁掉覆盖**:mem_ema5 cov 0.49 且 valid Lnet −92.4%(不可能是真实策略收益),
      mem_ema10 cov 0.90,mem_ema30/60 才 cov 1.00。小半衰期的 cross_ema 在这类重尾正数上有 bug。
  (3) **退化组合浪费了变体名额**:`day_corr(Amt, Amt)` ≡ 1(dist 0.00、全段 0.0%)、
      `cross_product(·,3)` cov 0.49(三个 ~1e12 相乘 float32 溢出)、`cross_max(·,241)` 后再取 5 日 std 的
      dist 0.04(年度滚动最大值几乎不动)。生成器应当预筛掉同参数的 corr/cov 与会溢出的 product。
- **立方体没有流通市值**,这是本因子分析里最大的一处手被绑住:全部分析指向"同市值内选低换手",
  而对成交额中性化(res/bk_liq、res/bk_known)四行全是 +2.3~+3.8% —— 不是因子没内容,是中性化错了对象。
  已把"加 FloatMV / Shares 字段"写进 new_operator_requests,这是优先级最高的一条。
- 口径提醒:`ts_stddev(x, d)` 与 `cross_stddev(x, d)` 对"每股票-日一个值"是同一个内核、逐位相同,
  但窗口池不同(ts: 1/5/10/20/30/40/50;cross: 3/5/10/15/30/60/241)。想要 3 或 15 就写 cross_*(playbook 也建议)。

## 研究日志(`notes/F105_std_fangzheng_covamt/journal.md`:1 条,其中研究员自己写的 1 条)

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
- `x1_events`(自写脚本的输出)  10-03 19:28  exit 0  → `logs/F105_std_fangzheng_covamt_x1_events.log`
- `x2_longleg`(自写脚本的输出)  10-03 23:05  exit 0  → `logs/F105_std_fangzheng_covamt_x2_longleg.log`
- `audit1`(自写脚本的输出)  10-03 23:29  exit 0  → `logs/F105_std_fangzheng_covamt_audit1.log`
- `rev1`(自写脚本的输出)  10-03 23:51  exit 0  → `logs/F105_std_fangzheng_covamt_rev1.log`
- `rev2`(自写脚本的输出)  10-03 23:59  exit 97  → `logs/F105_std_fangzheng_covamt_rev2.log`

## 已写的 notes(`notes/F105_std_fangzheng_covamt/`)

`01_expression.md`(1K)、`02_operators.md`(1K)、`03_decomposition.md`(1K)、`04_grammar.md`(1K)、`05_hypotheses.md`(5K)、`06_baseline.md`(3K)、`07_S1_what.md`(4K)、`07_S1b_events.md`(6K)、`07_S2_nodes.md`(4K)、`07_S3_family.md`(4K)、`07_S4_longleg.md`(6K)、`07_S_final.md`(6K)、`07_conditional.md`(3K)、`07_controls.md`(1K)、`07_neutralise.md`(2K)、`07x_events.md`(8K)、`07x_longleg.md`(5K)、`07x_review_audit.md`(8K)、`07x_revision.md`(19K)、`08_variants.md`(3K)、`09_diagnosis.md`(11K)、`10_distilled.md`(13K)、`11_risks.md`(4K)、`12_next.md`(2K)、`journal.md`(1K)、`state.md`(9K)、`synthesis.md`(11K)

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

报告:`research/alpha_distillation/F105_std_fangzheng_covamt.md`(10-04 12:08 生成)
