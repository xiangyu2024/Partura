# F104_kurt_masktop_amt — 交接状态

_自动生成于 2026-10-05 15:16(`python scripts/recorder.py --brief F104_kurt_masktop_amt` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #4190(批次 B01_single_factors)
- 表达式:`day_kurt(nt_cs_mask_top_replace_mean_neg(abs_(Amt)))`

## 现在到哪一步

- **阶段:全部完成**
- **留出段已经读过 2 次**(10-03 23:33, 10-05 12:12)—— **不许再读**。候选在留出段上的数全在 `runs/F104_kurt_masktop_amt/final.json`(`./scripts/study.sh digest F104_kurt_masktop_amt final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `synth:F104_kurt_masktop_amt`:已返回结果,最后动作 10-05 11:21 → `handoff/F104_kurt_masktop_amt/agents/synth_accae2715d8c6687c.md`
  - `verdict:F104_kurt_masktop_amt`:中断,最后动作 10-05 13:53 → `handoff/F104_kurt_masktop_amt/agents/verdict_a41b25b16372b7086.md`
  - `verdict:F104_kurt_masktop_amt`:还在跑(多半就是你自己)

**接手的人该做什么:** 这条因子做完了。最终结论在 `handoff/F104_kurt_masktop_amt/results/` 里最新的那个(revised.json 优先,否则 study.json)。

## 研究现状(`notes/F104_kurt_masktop_amt/state.md`,10-05 15:16 更新)—— **先读这个文件**

# F104_kurt_masktop_amt — 研究现状(2026-10-05 第二轮主研重写;接手者先读这一页)

因子:`day_kurt(nt_cs_mask_top_replace_mean_neg(abs_(Amt)))`(挖掘库 #4190)。
口径:A 股纯多头,多头腿扣 15bp 净超额 Lnet / 纯多头夏普 Lshp,半衰期按纯多头书选;train 2018–2021 / valid 20220101–20230807 / utrain 合并。
噪声 ±3 点、±0.3 夏普;门槛 cov ≥ 0.95、dist ≥ 0.5。

## 1. 现状

两轮批量扫描都已读完:s1(70 变体)、**s2(117 变体 + 10 列市场解剖)**。
综合(含完整对账表)在 `notes/F104_kurt_masktop_amt/synthesis.md`,末节 =「## 第二轮(s2)对账与结论」。
第三批 25 条假设在 `studies/F104_kurt_masktop_amt/hypo3.yaml`(`study.sh hypo3` **25/25 通过**,尚未回测;
2026-10-05 复核时把最弱的一条 h3_semistd_dryup 换成了 **h3_cand_xfrozen** = 候选 × 通用冻结筛子,见 §6)。
**留出段已在 2026-10-04 用掉(tag `final`),绝不能再读;`runs/.../sweepfinal_*.json` 是测试段读数,不许打开。**
本页所有数字来自 train / valid。

结论(两轮一致、这一轮在 117 个变体上确认):
- **原式对纯多头不可用**。ut +1.8% / 0.38,valid **−5.8% / −1.24**;全部多头价值在那 6.5% 冻结盘口段里,剔掉就倒挂到 ut **−2.0%**。
- **树里唯一有价值的子结构是 mask** = 可交易的「流动性下限」。配保尺度 reader 得 ut +13.0~15.1% / Lshp 2.71~2.87,
  但 ρk 0.83~0.93 ⇒ **是已知成交额族里形状更好的成员,不是新因子**(提纯,不是升华)。
- **建在已知族之上本因子没有净增量**:overlay 六条、本因子当筛子两条、残差、分桶全部严格劣于 k_known。

(…全文 6931 字符,读 `notes/F104_kurt_masktop_amt/state.md`)

## 研究日志(`notes/F104_kurt_masktop_amt/journal.md`:6 条,其中研究员自己写的 5 条)

最近的 5 条(更早的和全文看文件):

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

### 2026-10-05 13:49 [主研] 批量扫描 s2 对账与结论

s2(117 变体 + 10 列解剖)读完。对账:上一轮五条推论里 (b)(d) 支持、(a)(c) 半支持(绝对死分钟口径当排序一律 ≈0 且 dist ✗,当筛子则赢基准)、(e) 否定(day_centroid 不是零信息而是 ut −22.4%)。
定论:原式对纯多头不可用(ut +1.8% / 0.38,valid −5.8%;剔掉 6.5% 冻结段后 ut −2.0%,全部价值就在那一段)。best_own 三条都是 mask + 保尺度 reader:h_sqrt_std +15.1% / 2.87、h_mask_mean +13.7% / 2.71(LTO 3.4%、ρo 0.00)、sub_C_day_std +13.0% / 2.85;ρk 0.83~0.93 ⇒ 已知成交额族的改良成员,是提纯不是升华。
新判决:压缩与 reader 是两条独立杠杆(sqrt 各加 ≈2 点);二阶矩多余(day_mean 就够);外层 30 日记忆多余(13.0→11.6);day_std(log) 反而 −6.7%,证实值在尺度本身。
best_on_known:没有净增量。最强的 h_known_nofrozen +18.5% / 3.15 与通用筛子 k_known_xfrozen 逐位同级(ρk 0.56 相同),不是本因子的功劳;h_known_nofloor(剔最清淡 20%)只 +8.6%,所以候选的夏普优势不等于「别买清淡」。
隐患:h_sqrt_std 的钱几乎全是「买清淡」的段暴露(五档段内 +0.3/−1.0/−5.0/−5.7/−12.0%、书 36.6pp 在最清淡档),而 sub_C_day_std 是全解剖唯一段内都不为负的一列。
第三批 25 条已写入 studies/F104_kurt_masktop_amt/hypo3.yaml(hypo3 25/25 通过),核心是 cs_bucket_demean 裁决「段溢价 vs 段内选股」、day_at_max/min_ratio 把封顶与封底分开、day_es_ratio_hi/lo 替代 day_kurt、cs_flip_by_state 验「只在缩量日有效」、以及 Amt^0.25 × day_std 这个唯一没试的格点。

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

`01_expression.md`(3K)、`02_operators.md`(5K)、`03_decomposition.md`(2K)、`04_grammar.md`(1K)、`05_hypotheses.md`(15K)、`06_baseline.md`(5K)、`07_S1_mask.md`(5K)、`07_S2_resid.md`(6K)、`07_S3_reader.md`(8K)、`07_S4_long.md`(8K)、`07_SA_audit.md`(1K)、`07_S_final.md`(2K)、`07_conditional.md`(2K)、`07_controls.md`(2K)、`07_neutralise.md`(5K)、`07x_anatomy.md`(7K)、`07x_audit.md`(5K)、`07x_longleg.md`(9K)、`07x_rev1.md`(14K)、`07x_rev2.md`(17K)、`08_variants.md`(6K)、`09_diagnosis.md`(10K)、`10_distilled.md`(19K)、`11_risks.md`(5K)、`12_next.md`(3K)、`journal.md`(10K)、`state.md`(10K)、`synthesis.md`(19K)

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
