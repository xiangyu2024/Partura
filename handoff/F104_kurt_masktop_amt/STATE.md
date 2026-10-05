# F104_kurt_masktop_amt — 交接状态

_自动生成于 2026-10-05 13:33(`python scripts/recorder.py --brief F104_kurt_masktop_amt` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #4190(批次 B01_single_factors)
- 表达式:`day_kurt(nt_cs_mask_top_replace_mean_neg(abs_(Amt)))`

## 现在到哪一步

- **阶段:全部完成**
- **留出段已经读过 2 次**(10-03 23:33, 10-05 12:12)—— **不许再读**。候选在留出段上的数全在 `runs/F104_kurt_masktop_amt/final.json`(`./scripts/study.sh digest F104_kurt_masktop_amt final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `revise:F104_kurt_masktop_amt#2`:失败,几乎没做事
  - `revise:F104_kurt_masktop_amt`:已返回结果,最后动作 10-04 13:06 → `handoff/F104_kurt_masktop_amt/agents/revise_a1835fbf9371d0c2b.md`
  - `synth:F104_kurt_masktop_amt`:已返回结果,最后动作 10-05 11:21 → `handoff/F104_kurt_masktop_amt/agents/synth_accae2715d8c6687c.md`

**接手的人该做什么:** 这条因子做完了。最终结论在 `handoff/F104_kurt_masktop_amt/results/` 里最新的那个(revised.json 优先,否则 study.json)。

## 研究现状(`notes/F104_kurt_masktop_amt/state.md`,10-05 11:19 更新)—— **先读这个文件**

# F104_kurt_masktop_amt — 研究现状(2026-10-05 主研重写;接手者先读这一页)

## 1. 现状

批量扫描 s1(70 个变体)+ 市场解剖已跑完并读完。综合写在 `notes/F104_kurt_masktop_amt/synthesis.md`(每个论断带变体 id 和数字),
第二批 38 条假设写在 `studies/F104_kurt_masktop_amt/hypo.yaml`(`study.sh hypo` 38/38 通过,尚未回测)。
**留出段(holdout)在 2026-10-04 已经读过一次(tag `final`),绝不能再读。**

结论分两层:
- **原式**(`day_kurt(nt_cs_mask_top_replace_mean_neg(abs_(Amt)))`):对只做多的用户 **none_robust** —— 相对已知成交额族没有增量。
  (与 2026-10-04 修订版一致,但这次是在 70 个变体的大表上确认的,不再依赖小样本逐轮实验。)
- **新的东西**:这棵树里的 **mask 是一个真的、可交易的「流动性下限」**。
  候选 `sub_C_day_std` = `day_std(nt_cs_mask_top_replace_mean_neg(abs_(Amt)))`,
  **纯多头夏普两段都显著高于已知族基准**。它 ρk = 0.85,必须按**已知成交额族的改良成员**上报,不是新因子。

## 2. 中间结果(口径:多头腿扣 15bp 净超额 / 纯多头夏普,train 2018–2021 / valid 20220101–20230807 / utrain 合并)

基准 `k_known = cross_mean(day_std(Amt), 30)`:+12.6% / +22.3% / +15.4%,Lshp 1.78 / 3.46 / 2.22,LTO 3.4%。

| 变体 | 表达式 | Lnet tr/va/ut | Lshp tr/va/ut | LTO | ρo | ρk |
|---|---|---|---|---|---|---|
| v_base | 原式 | +4.8 / −5.8 / +1.8% | 1.00 / −1.24 / 0.38 | 7.0% | 1.00 | 0.26 |
| **sub_C_day_std** | day_std(mask(abs_(Amt))) | +12.0 / +15.5 / **+13.0%** | 2.49 / 3.98 / **2.85** | 4.1% | 0.12 | 0.85 |
| sub_A_sqrt(=pow_05) | day_kurt(mask(sqrt(Amt))) | +12.2 / +18.8 / +14.1% | 1.81 / 3.29 / 2.18 | 4.0% | 0.84 | 0.60 |
| sub_C_day_ar1 | ar1(mask(abs_(Amt))) | +9.0 / +16.5 / +11.2% | 1.47 / 3.05 / 1.88 | 6.5% | 0.04 | 0.78 |
| sub_A_log | day_kurt(mask(log(Amt))) | +8.7 / +13.0 / +10.0% | 1.46 / 2.23 / 1.68 | 4.7% | 0.24 | 0.82 |
| mem_min10 | cross_min(原式, 10) | +6.0 / +8.1 / +6.6% | 1.05 / 2.25 / 1.27 | 2.9% | 0.66 | 0.38 |

坏的一端:abl_B(删 mask)ut −5.0% / ρk **−0.35**;nt_cs_rank 替代 −16.7%;nt_cs_quantile_q50 −28.1%;
pow_1_5(凸变换)−50.6%(cov 0.23 ✗);cross_zscore 5/10/30/60 全崩 −28.6~−10.8%(换手 12~33%)。
overlay 六条(已知族 + λ·原式,λ = ±0.25/±0.5/±1.0)ut = 13.1 / 12.4 / 11.5 / 10.8 / 9.0 / 3.7,**全部严格低于 15.4**;
res_known −0.4%、res_liq +0.9%、bk_known −2.0% ✗、bk_liq −1.2% ✗。

解剖(utrain 全市场多头书;段内 = 只在该段建书):
原式只在 **6.5% 的冻结盘口段**(段等权 −67.4%)段内 **+12.1%**,在无冻结的 93.5% 段 **−0.3%**;
成交额五档段内 −4.0 / −6.8 / −6.9 / −3.6 / **+7.4%**(书却超配最低档 +25.1pp,该档段等权 +15.1%、最高档 −17.8%);
主板 +4.9 / +6.9,创业板 −3.5、科创板 −6.9;次新(7.1%)−9.7%;逐年 +5.5/+6.4/+1.4/+5.8/**−3.9/−8.7**;缩量日 +4.7% vs 放量日 −1.7%。
候选 sub_C_day_std:四板块全正(+8.5/+14.5/+18.7/+8.8),成交额五档段内 −1.5/+1.6/+0.3/+0.3/+1.9(**唯一不为负的一列**,基准是 −4.1/−5.3/−8.2/−5.2/+2.5),
书落在第二档(+43.9pp,最低档只 +5.9pp),逐年 18.6/13.7/6.2/9.4/16.8/13.6 全正。

## 3. 过程与逻辑

读算子定义 → 发现 `nt_cs_mask_top_replace_mean_neg` 名字三处骗人(遮的是**最低** 10%,沿**股票轴**,替换值是**市场级**截面均值 M[d,m],
比被遮票自身大 10~100 倍)→ 由此推出 day_kurt(masked) 是流动性的**驼峰型**函数、书是杠铃(解剖里得到证实:成交额档超配 +25.1 / −7~−13 / +6.1pp)
→ 再看三类变体:删 mask 翻号(mask 定符号)、换 reader 时「保尺度 / 持续性」赢而「标准化高阶矩」输、前置凹变换单调改善
→ 统一解释:**多头腿的钱全在 mask 漏进来的成交额水平里,而 day_kurt 的工作恰恰是把它除掉** → overlay/残差全败,确认原式无增量;
但 `day_std(masked)` 把最死的票挤出书(它们大半分钟写着 M),等于一个可交易的流动性下限,夏普优于基准 → 这才是研究产物。

## 4. 假设表(第二批,38 条,`studies/F104_kurt_masktop_amt/hypo.yaml`,未回测)

A 连续无漂移的底十分位标记(6):`nt_cs_rank(Amt)` 的 day_mean / q25 / min,`day_pos_ratio(nt_cs_quantile_q75(Amt))`(修 sub_B 的 dist ✗)。
B 死分钟直读(5):day_zero_ratio / day_flat_ratio / day_flat_run_max + cross_mean/cross_max;Ret 与 Amt 零占比之差 = 封板排队。
C 保 mask 换 reader(6):day_mean / day_quantile_q25 / day_centroid;候选 + 30 日均值 / 低尾均值;遮最高一成的镜像。
D 压缩杠杆(4):Amt^0.25、sqrt×day_std、sqrt×ar1、log×day_std。
E 新叶子(4):\|Ret\| × kurt / std、sqrt(Volume)、5 分钟量变化率 × day_std。
F 分段写进表达式(6):已知族 + 剔最清淡 20% / 剔死分钟 / 剔封板 / 剔次新;原式关进最活跃 40% 与最清淡 40%。
G 状态与新算子(7):个股放缩量比做段;in_madz 的自身历史门槛;day_gini;day_signed_ratio;cross_tail_mean_q25。

## 5. 候选

1. **`day_std(nt_cs_mask_top_replace_mean_neg(abs_(Amt)))`**(sub_C_day_std)—— 第一推荐,按已知族改良成员报。
   判据:夏普 2.85 vs 2.22(两段都高、超 ±0.3 噪声);净超额 13.0 vs 15.4(valid 低 6.8 点,是它的弱点);ρk 0.85。
2. `day_kurt(nt_cs_mask_top_replace_mean_neg(sqrt(Amt)))`(sub_A_sqrt)—— ρo 0.84 还保着原式的序,ut +14.1%;多空 LS 4.79/5.04 是全表最好,但那不是用户的口径。
3. `cross_min(原式, 10)`(mem_min10)—— 若一定要交易原式:换手只有 2.9%、valid 为正(+8.1%),但 +6.6% 远低于基准,不值得。
原式本身 **不是候选**。

## 6. 后面的思路

- 先跑第 4 节的 38 条;最该先看的是 F 组(h_known_nofloor / h_known_nofrozen):若显式下限就追平了候选,mask 可以整条删掉,结论变成「已知族 + 一个剔除器」。
- 其次是 C 组 h_mask_mean 与 h_mask_std_m30:把「下限」「二阶矩」「一天 vs 一个月」三件事拆开。
- 若 A 组(nt_cs_rank 一族)能达到候选的水平,整棵树都可以用一个有界、无尖峰、不随市场量漂移的量替代 —— 那是更干净的产物。
- 候选若要上报,还需要:(i) 它与 F001 成员 `cross_max(day_std(Amt), 9)` 的相关与对比(本次大表没放这条基准);(ii) 多头腿最大回撤(大表不出这一列)。

## 7. 留出段

**已用掉(2026-10-04,tag `final`,5 条候选)。不得再读。** 本轮所有数字都来自 train / valid,没有碰 holdout。
若要为候选 sub_C_day_std 申请第二次留出段,必须先由用户同意,并在读之前把排序与判据写进 `10_distilled.md`。

## 8. 给接手者的提醒

- **算子按定义理解,不要按名字**:`nt_cs_mask_top_replace_mean_neg` 遮的是最低 10%、替换值是市场级截面均值;
  `cs_regres(Y, X)` 返回残差不是系数;`cs_quantile_qXX` flag 的是**上** XX% 的带;`cross_*` 滚交易日轴;`in_slice(x,a,b)` 是闭区间。
- `sqrt` 与 `pow_05` 是同一个算子,大表里占了两行(sub_A_sqrt / sub_A_pow_05 数字完全相同)。
- 大表的多头半衰期网格封在 **hlL = 20**,很多变体正好取到上限;旧版 state 的 rev2 网格外实验显示 train 最优在 30~40。
  比较「水平类」变体时要记得这个截断。
- `cs_bucket_rank` 在这条因子上即使修了并列也过不了 dist(bk_liq 0.20、bk_known 0.20 ✗),别再用它做中性化;用 `cs_first_*/cs_last_*`。
- 用 `cs_first_*` / `cs_last_*` 时,y 必须写成「高 = 该买」(已知族要加 `neg`),否则 sg 取 −1 会把哪一段在书顶整个翻掉。
- 布尔输出 + day_kurt 会因为取值太少被 cov/dist 误杀(sub_B_q75:ut +7.9% / Lshp 1.73 却 cov 0.79 / dist 0.15 ✗);要连续化(day_pos_ratio / day_mean)。
- 旧 notes(01~12、07x_*)是 2026-10-03/04 那一轮的,口径与结论**以本页和 synthesis.md 为准**。

## 研究日志(`notes/F104_kurt_masktop_amt/journal.md`:5 条,其中研究员自己写的 4 条)

最近的 5 条(更早的和全文看文件):

### 2026-10-04 12:39 [auto] rev2 跑完(exit 0);重看结果:logs/F104_kurt_masktop_amt_rev2.log

### 2026-10-04 12:41 修订接手(第三次):口径改为多头腿;rev2(rev2_long.py)跑完 —— 这条因子对只能做多的人相对已知家族没有增量

接手时的状态:原研究 + 两路审查完成(5 条 major);上一位修订者跑了 rev1(exit 97,但 A/B/D 全、C 大半有结果)并改了 05/06/07_S2/S3/S4/07x_*/08/11,没改 01/09/10/12,也没返回结果。
用户 2026-10-04 把选拔口径定为「多头腿净超额 + 纯多头夏普,半衰期按纯多头书选」。按这个口径重读 final.json(没有再读留出段),用户口径 训练/测试:
  原式 hlL 20(=hlS,网格上界):+1.8% / -2.1%,纯多头夏普 0.38 / -0.39
  f_kurt30 hlL 2:+4.4% / +3.9%,0.89 / 0.79      f_cv30 hlL 1:+3.7% / -1.2%,0.82 / -0.19
  f_exclcv hlL 1:+16.2% / +12.1%,2.78 / 1.24      f_std30(已知家族基准)hlL 0:+15.4% / +14.1%,2.22 / 1.51
rev2(exec,只切 train/valid,自检全部对上阶段表与 rev1 日志)量到的:
  H 半衰期放到网格外:原式 train 净超额在 hl 40 见顶 +5.8%(夏普 1.21),valid 在 hl 20/40/60/120 是 -5.8/-2.8/-2.8/-1.1%,毛超额始终在 0 上下 —— 延长半衰期只省成本,省不出正数。
    f_kurt30 再平滑 valid 变差(hl 20:-5.0%);已知家族 F001 成员 cross_max(day_std(Amt),9) 在 hl 5 是 +13.7% / +22.2%(hl 0 是 +9.3% / +18.5%)。
  P 日度配对差:f_exclcv - f_std30 = train +2.4 点(t 1.3)、valid -3.2 点(t -1.4);逐年 2018~2020 为 +6.5/+4.6/+3.3,2021~2023 为 -4.8/-3.1/-3.5。
  X 排除式叠加(在已知家族多头十分位里剔除本因子最差的 10%/20%,扣换手成本):train +0.2~+1.6 点(t 2~4.7),valid -0.8~+0.2 点;逐年只有 2018、2020 为正。原式的最差 20% 只
…(这条日志还有后文,读 journal.md)

### 2026-10-04 12:53 notes 进度:07x_rev2、06/07_* 的多头口径读法、09、10 已写;还差 01/05/08/11/12 与配置注释

已落盘:state.md(现状 8 节)、07x_rev2.md(rev2 五节,数字逐项对过日志)、07_S1~S4 / 07_S_final / 07_controls / 07_neutralise / 07_conditional 各加了「按选拔口径(多头腿)读」的一段(原文保留)、
06_baseline.md 加了多头口径的基线读法、09_diagnosis.md 重写(A 多头腿 7 条 + B 机制 5 条 + 修订记录表)、10_distilled.md 改成三段(读前原文逐字保留 36 行,已用脚本核对;新写「按多头口径读」;原读后结论存档)。
结论:none_robust;recommended 填已知家族基准 f_std30;f_exclcv 不记为升华。
还没做:01_expression.md 末段、05_hypotheses.md 补 H17~H20 与表头说明、08_variants.md 重写、11_risks.md、12_next.md、07x_longleg.md 加口径说明、配置 rank_by 注释;然后 report、通读、最终日志、返回结构化结果。
不再跑服务器(rev3 不用)。

### 2026-10-04 13:00 研究完成(修订):none_robust —— 这条因子没有属于自己的稳健多头版本;纯多头直接用已知家族 cross_mean(day_std(Amt),30)(半衰期 0)

推荐与理由(用户口径,训练/测试;数字全部取自 final.json,没有再读留出段):
  recommended 栏填已知家族基准 f_std30 = cross_mean(day_std(Amt), 30),多头口径半衰期 0:多头腿净超额 +15.4% / +14.1%,纯多头夏普 2.22 / 1.51;类型 none_robust —— 它不是这条因子的提纯或升华。
  原式(多头最优半衰期 20 = 多空口径 = 网格上界):+1.8% / -2.1%,0.38 / -0.39 → 不可用,original_at_long_halflife_is_enough = false。
  事前第一推荐 f_exclcv(半衰期 1):+16.2% / +12.1%,2.78 / 1.24 —— 相对原式好 14 个点,但它是流动性家族(与基准秩相关 0.84、与原式 0.35),相对已知家族没有增量(留出段低 2.0 点;train +2.4 点 t 1.3,valid -3.2 点 t -1.4;2021~2025 每年都低)→ 不记为升华。
  f_kurt30(半衰期 2):+4.4% / +3.9%,0.89 / 0.79;比原式好 6 点,valid 上拆开是流动性位置 +5.7、成本 +2.0、桶内选择 -1.7,不是更好的读数;valid 多头腿 +0.1%。
五条审查意见:① ② elevated 标签 → 已改(none_robust)+ rev2 补实验;③ 标签口径抬高空头腿 → rev1 已量、各节已注;④ 线性正交 ≠ 尾部中性 → rev1 分桶中性 + 措辞已改;⑤ 条件化只替代空头腿 → rev1 加分桶哑变量,残差 IC 不消失,措辞降级,那块成分列未决。
已交付:notes 全部按多头口径改完(原文保留),报告 research/alpha_distillation/F104_kurt_masktop_amt.md 已重出并通读(2173 行;生成表与 notes 的数字逐项对过;唯一的表格问题是条件 IC 表行首的竖线没转义,属于 report.py)。
未决:原式里提纯式张不成的那块 rank IC 是什么(rev2_split.py 写好没跑);集中度对流动性多头书的增量为什么 2021 年后消失
…(这条日志还有后文,读 journal.md)

### 2026-10-05 11:17 [主研] 批量扫描 s1 的综合

- 机制定稿:nt_cs_mask_top_replace_mean_neg 是「带巨型旗标的指示函数」—— 每(日,分钟)沿股票轴把最低 10% 换成市场级截面均值 M[d,m](比被遮票自身大 10~100 倍);day_kurt 再把成交额水平除掉,于是因子成为流动性的驼峰型函数,书是成交额上的杠铃(最低档 +25.1pp / 最高档 +6.1pp / 中间三档 −7~−13pp)。abs_ 是空操作(abl_A 逐位相同)。
- 多头腿的钱全在 mask 漏进来的「水平」里:换保尺度 reader(day_std ut +13.0% / Lshp 2.85)或持续性 reader(ar1 +11.2%、autocorr +11.1%)是原式(+1.8% / 0.38)的 3~7 倍,而它们 ρo 只有 +0.04~+0.12、ρk 0.60~0.85 —— 不是同一条因子。前置凹变换同理:Amt +1.8% → sqrt +14.1% → log +10.0%,凸的 pow_1_5 −50.6%(cov ✗)。
- 原式对纯多头没有增量,确认 none_robust:六条 overlay 全部严格差于已知族(ut 13.1/12.4/11.5/10.8/9.0/3.7 对 15.4),res_known −0.4%、bk_known −2.0% ✗,表里没有任何筛子形态。
- 解剖:选股力只剩 6.5% 冻结盘口段(段内 +12.1%,无冻结的 93.5% 段 −0.3%)与成交额最高档(+7.4%,段等权 −17.8%);它超配的清淡档段内是 −4.0%;主板专属(创业板 −3.5% / 科创板 −6.9%);次新 −9.7%;2022 起转负;只在缩量日有效(+4.7% vs 放量 −1.7%)—— 因为 mask 的门槛是截面相对的,随市场总量漂移。
- 候选(按已知族的改良成员报,不是新因子):sub_C_day_std = day_std(nt_cs_mask_top_replace_mean_neg(abs_(Amt))),Lnet +12.0/+15.5/+13.0、Lshp 2.49/3.98/2.85(基准 1.78/3.46/2.22,两段都高且超噪声),ρk 0.85,逐年全正;mask 在它身上起的是「可交易的流动性下限」作用,把书从成交额最低档推到第二档。
- 第二批 38 条假设已落盘并全部通过解析(studies/F104_kurt_masktop
…(这条日志还有后文,读 journal.md)

## 配置里的实验计划(`configs/F104_kurt_masktop_amt.yaml`)

- 标题:成交额的日内脉冲集中度(峰度),但先把不活跃股票的安静分钟垫到全市场均值水平
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base
- **S1_mask**(7 个变体):nt_cs_mask_top_replace_mean_neg 在这棵树里做的是什么:旁观者、被替换分钟数的计数器,还是一个把不活跃股票的安静分钟垫到市场水平的地板?
  p_noabs、p_nat、p_kfrac、p_mirror、f_addmean、f_addmed、f_floormed
- **S2_resid**(7 个变体):mask 节点做的事,是不是等价于「把自身成交额峰度对流动性水平做截面残差」?如果是,干净的写法(不要 NT 面、不要排名阈值)在 train 和 valid 上应该都不输原式。
  q_ref、q_nat_ramt、q_nat_m30、q_nat_ramt30、q_base_ramt30、q_nat_rk30、q_addmed_m30
- **S3_reader**(12 个变体):条件化之后,读数的哪些性质是必需的:统计量(峰度 / 最大一分钟占比 / 变异系数)、记忆(原值均值 / 极值 / 秩均值)、窗口、时段(开盘 / 盘中)、方向(上涨分钟的脉冲 / 下跌分钟的脉冲)?
  r_ref30、r_base_m30、r_maxsh30、r_cv30、r_kurt_max30、r_rankavg30、r_kurt15、r_kurt60、r_kurt_noopen30、r_addmed_ramt30、r_up30、r_dn30
- **S4_long**(9 个变体):「同等流动性下成交不集中」这个条件,能不能改善一本低流动性多头书 —— 而且是超出已知的 F001 家族(成交额水平、成交额的日内标准差)已经给出的那部分?
  l_amt30、l_f001、l_std30、l_stdres30、l_add、l_add2、l_addcv、l_gate、l_excl
- **S_final**(5 个变体):样本外(用户的测试段 20230808–20251231):(1) 把 mask 换成显式条件化的提纯式站不站得住;(2) 读数换成变异系数有没有差别;(3) 排除式合成的多头腿是不是好于原式;(4) 它有没有超出已知的流动性家族?
  f_orig、f_kurt30、f_cv30、f_exclcv、f_std30

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F104_kurt_masktop_amt`)

- `S0_baseline`  10-03 17:43  1 个变体  → `./scripts/study.sh digest F104_kurt_masktop_amt S0_baseline`
- `S1_mask`  10-03 19:44  7 个变体  → `./scripts/study.sh digest F104_kurt_masktop_amt S1_mask`
- `S2_resid`  10-03 19:57  7 个变体  → `./scripts/study.sh digest F104_kurt_masktop_amt S2_resid`
- `S3_reader`  10-03 22:55  12 个变体  → `./scripts/study.sh digest F104_kurt_masktop_amt S3_reader`
- `S4_long`  10-03 23:12  9 个变体  → `./scripts/study.sh digest F104_kurt_masktop_amt S4_long`
- `final`  10-03 23:33  5 个变体  → `./scripts/study.sh digest F104_kurt_masktop_amt final`
- `sweep_s1`  10-05 10:55  74 个变体  → `./scripts/study.sh digest F104_kurt_masktop_amt sweep_s1`
- `anatomy_s1`  10-05 11:02  0 个变体  → `./scripts/study.sh digest F104_kurt_masktop_amt anatomy_s1`
- `sweep_s2`  10-05 11:39  121 个变体  → `./scripts/study.sh digest F104_kurt_masktop_amt sweep_s2`
- `anatomy_s2`  10-05 12:02  0 个变体  → `./scripts/study.sh digest F104_kurt_masktop_amt anatomy_s2`
- `sweepfinal_s2`  10-05 12:14  8 个变体  → `./scripts/study.sh digest F104_kurt_masktop_amt sweepfinal_s2`
- `x1`(自写脚本的输出)  10-03 19:33  exit 0  → `logs/F104_kurt_masktop_amt_x1.log`
- `x2`(自写脚本的输出)  10-03 23:20  exit 0  → `logs/F104_kurt_masktop_amt_x2.log`
- `audit1`(自写脚本的输出)  10-03 23:56  exit 0  → `logs/F104_kurt_masktop_amt_audit1.log`
- `rev1`(自写脚本的输出)  10-04 00:28  exit 97  → `logs/F104_kurt_masktop_amt_rev1.log`
- `rev2`(自写脚本的输出)  10-04 12:38  exit 0  → `logs/F104_kurt_masktop_amt_rev2.log`

## 已写的 notes(`notes/F104_kurt_masktop_amt/`)

`01_expression.md`(3K)、`02_operators.md`(5K)、`03_decomposition.md`(2K)、`04_grammar.md`(1K)、`05_hypotheses.md`(15K)、`06_baseline.md`(5K)、`07_S1_mask.md`(5K)、`07_S2_resid.md`(6K)、`07_S3_reader.md`(8K)、`07_S4_long.md`(8K)、`07_SA_audit.md`(1K)、`07_S_final.md`(2K)、`07_conditional.md`(2K)、`07_controls.md`(2K)、`07_neutralise.md`(5K)、`07x_anatomy.md`(7K)、`07x_audit.md`(5K)、`07x_longleg.md`(9K)、`07x_rev1.md`(14K)、`07x_rev2.md`(17K)、`08_variants.md`(6K)、`09_diagnosis.md`(10K)、`10_distilled.md`(19K)、`11_risks.md`(5K)、`12_next.md`(3K)、`journal.md`(8K)、`state.md`(7K)、`synthesis.md`(11K)

## 自写的探针与分析脚本(`studies/F104_kurt_masktop_amt/`)

- `audit_span.py`  10-03 23:50  audit_span -- reviewer's refutation attempt (mechanism / overfitting lens).  train / valid rows only.
- `probes.py`  10-03 18:37  Probes this tree needs:  day_kurt(nt_cs_mask_top_replace_mean_neg(abs_(Amt))).
- `rev1_review.py`  10-04 00:15  rev1 -- the experiments the two reviews asked for.  train / valid rows only; the holdout is never sliced.
- `rev2_long.py`  10-04 12:19  rev2 -- what the LONG-ONLY selection criterion asks of this study.  train / valid rows only; the holdout is ne
- `rev2_split.py`  10-04 00:56  rev2 -- what rev1 could not finish, and the one new question rev1 raised.  train / valid rows only.
- `x1_anatomy.py`  10-03 19:07  x1 -- what  day_kurt(nt_cs_mask_top_replace_mean_neg(abs_(Amt)))  reads on REAL data.
- `x2_longleg.py`  10-03 23:17  x2 -- what S3/S4 left open, and no stage table answers.  Only train / valid rows are touched.

## 结构化结果(`handoff/F104_kurt_masktop_amt/results/`)

- `audit-mechanism.json`
- `audit-numbers.json`
- `revised.json`
- `study.json`
- `synthesis.json`

报告:`research/alpha_distillation/F104_kurt_masktop_amt.md`(10-04 13:03 生成)
