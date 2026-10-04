# F104_kurt_masktop_amt — 交接状态

_自动生成于 2026-10-04 13:10(`python scripts/recorder.py --brief F104_kurt_masktop_amt` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #4190(批次 B01_single_factors)
- 表达式:`day_kurt(nt_cs_mask_top_replace_mean_neg(abs_(Amt)))`

## 现在到哪一步

- **阶段:全部完成**
- **留出段已经读过 1 次**(10-03 23:33)—— **不许再读**。候选在留出段上的数全在 `runs/F104_kurt_masktop_amt/final.json`(`./scripts/study.sh digest F104_kurt_masktop_amt final`)。
- agent `study:F104_kurt_masktop_amt`(wf_759ef2d3-03f):中断,几乎没做事(不用看)
- agent `study:F104_kurt_masktop_amt`(wf_759ef2d3-03f):中断,几乎没做事(不用看)
- agent `study:F104_kurt_masktop_amt`(wf_759ef2d3-03f):已返回结果,最后动作 10-03 23:43 → `handoff/F104_kurt_masktop_amt/agents/study_ac764477b85d34cee.md`
- agent `audit-numbers:F104_kurt_masktop_amt`(wf_759ef2d3-03f):已返回结果,最后动作 10-03 23:54 → `handoff/F104_kurt_masktop_amt/agents/audit-numbers_aea0b8e1e0bb6aa25.md`
- agent `audit-mechanism:F104_kurt_masktop_amt`(wf_759ef2d3-03f):已返回结果,最后动作 10-04 00:01 → `handoff/F104_kurt_masktop_amt/agents/audit-mechanism_aa46b904b09f48794.md`
- agent `revise:F104_kurt_masktop_amt`(wf_759ef2d3-03f):失败,最后动作 10-04 02:41 → `handoff/F104_kurt_masktop_amt/agents/revise_a2b9539aaad227aac.md`
- agent `revise:F104_kurt_masktop_amt#2`(wf_759ef2d3-03f):失败,几乎没做事(不用看)
- agent `revise:F104_kurt_masktop_amt`(wf_08351f46-81b):已返回结果,最后动作 10-04 13:06 → `handoff/F104_kurt_masktop_amt/agents/revise_a1835fbf9371d0c2b.md`

**接手的人该做什么:** 这条因子做完了。最终结论在 `handoff/F104_kurt_masktop_amt/results/` 里最新的那个(revised.json 优先,否则 study.json)。

## 研究现状(`notes/F104_kurt_masktop_amt/state.md`,10-04 13:03 更新)—— **先读这个文件**

# F104_kurt_masktop_amt — 研究现状(修订中;2026-10-04 写,接手者先读这一页)

## 1. 一句话现状

原研究(S0~S4、x1、x2、final)与两路审查都已完成;留出段**已读过一次**(tag `final`),绝不能再读。现在在做**修订**:
按用户 2026-10-04 定的选拔口径(**只看多头腿扣费后的净超额与纯多头夏普,半衰期按纯多头书选**)重写结论,并逐条处理审查的 5 条 major。
补充实验 rev1(上一位修订者,exit 97 但大部分有结果)和 rev2(本人,`rev2_long.py`,exit 0)都已跑完并读完;**notes 已全部改完,报告已重出并通读(2026-10-04,2175 行),结构化结果已返回 —— 修订完成**。
如果还要接着做,只剩第 12 节列的下一步;不要再动留出段。
修订的结论已定:**none_robust —— 这条因子没有属于自己的稳健多头版本;对只能做多的用户,相对已知成交额水平家族没有增量,直接用已知家族**。

(…全文 7594 字符,读 `notes/F104_kurt_masktop_amt/state.md`)

## 研究日志(`notes/F104_kurt_masktop_amt/journal.md`:4 条,其中研究员自己写的 3 条)

最近的 12 条(完整的看文件):

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
  X 排除式叠加(在已知家族多头十分位里剔除本因子最差的 10%/20%,扣换手成本):train +0.2~+1.6 点(t 2~4.7),valid -0.8~+0.2 点;逐年只有 2018、2020 为正。原式的最差 20% 只碰到已知家族多头书的 4%。
  A 秩相加:加原式 train -0.6~-2.5 点、valid ±2 点(都不显著);加提纯读数 train +0.1~+2.3、valid -2.0~-10.3(t -1.3~-3.0)。
  R 在已知家族二十分位内取秩后的多头腿:train +3.3%~+5.8%,valid -1.3%~-6.5%。
  L 多头腿 = 流动性位置 + 桶内选择(毛):valid 上 f_exclcv 20.5+2.6、f_std30 23.4+1.0、F001 23.0+2.1;桶内选择都不够付各自多头书的成本(4.0/2.1/2.9 点)。
判断:
  - 「原式 + 多头最优半衰期」不够(original_at_long_halflife_is_enough = false):它本来就在 20,延长也没有正的 valid。
  - 事前第一推荐 f_exclcv 相对原式是 +14 个点,但那是换成了流动性家族(与 f_std30 可交易信号秩相关 0.84,与原式 0.35);相对已知家族 train 高、valid 低、留出段低,不同向且都不显著 → 不记为升华。
  - 结论定为 none_robust:这条因子没有属于自己的稳健多头版本;纯多头直接用已知家族(读过留出段的五个候选里,多头口径最好、最简单的就是基准 f_std30)。
下一步:写 state.md;写 07x_rev2.md;重写 01/06/08/09/10/11/12 与 07_controls/neutralise 的口径说明;改配置 rank_by 注释;重出报告并通读。剩 1 次服务器运行(rev3),目前不打算用:rev2 的自检全过,没有需要再问服务器的问题。
决定不做的:上一位修订者写好的 rev2_split.py(把原式逐日面板拆成「格子均值 + 偏离」)—— 它追的是空头侧 / rank IC 的机制细节,对多头口径的结论没有影响,列入未决。

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
未决:原式里提纯式张不成的那块 rank IC 是什么(rev2_split.py 写好没跑);集中度对流动性多头书的增量为什么 2021 年后消失;行业;已知家族多头书的容量;F001 成员配多头半衰期 5 在本研究没读留出段。
修订用了 1 次服务器运行(rev2);rev3 没用。配置 rank_by 已改为 long(旧运行是 ls,JSON 里两种口径都有)。

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
- `x1`(自写脚本的输出)  10-03 19:33  exit 0  → `logs/F104_kurt_masktop_amt_x1.log`
- `x2`(自写脚本的输出)  10-03 23:20  exit 0  → `logs/F104_kurt_masktop_amt_x2.log`
- `audit1`(自写脚本的输出)  10-03 23:56  exit 0  → `logs/F104_kurt_masktop_amt_audit1.log`
- `rev1`(自写脚本的输出)  10-04 00:28  exit 97  → `logs/F104_kurt_masktop_amt_rev1.log`
- `rev2`(自写脚本的输出)  10-04 12:38  exit 0  → `logs/F104_kurt_masktop_amt_rev2.log`

## 已写的 notes(`notes/F104_kurt_masktop_amt/`)

- `01_expression.md`  3141 字节  10-04 12:56
- `02_operators.md`  5500 字节  10-03 23:40
- `03_decomposition.md`  2124 字节  10-03 19:49
- `04_grammar.md`  1652 字节  10-03 19:49
- `05_hypotheses.md`  15553 字节  10-04 12:56
- `06_baseline.md`  5651 字节  10-04 12:47
- `07_S1_mask.md`  5299 字节  10-04 12:23
- `07_S2_resid.md`  6706 字节  10-04 12:23
- `07_S3_reader.md`  9113 字节  10-04 12:24
- `07_S4_long.md`  8635 字节  10-04 12:24
- `07_SA_audit.md`  452 字节  10-04 00:49
- `07_S_final.md`  2772 字节  10-04 12:27
- `07_conditional.md`  2557 字节  10-04 12:48
- `07_controls.md`  2564 字节  10-04 12:48
- `07_neutralise.md`  5554 字节  10-04 12:48
- `07x_anatomy.md`  7264 字节  10-04 00:48
- `07x_audit.md`  5749 字节  10-04 12:47
- `07x_longleg.md`  9266 字节  10-04 12:57
- `07x_rev1.md`  15037 字节  10-04 12:47
- `07x_rev2.md`  18058 字节  10-04 12:54
- `08_variants.md`  6819 字节  10-04 12:54
- `09_diagnosis.md`  10663 字节  10-04 12:54
- `10_distilled.md`  20212 字节  10-04 12:54
- `11_risks.md`  5824 字节  10-04 12:55
- `12_next.md`  3423 字节  10-04 13:02
- `journal.md`  6828 字节  10-04 13:00
- `state.md`  12253 字节  10-04 13:03

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

报告:`research/alpha_distillation/F104_kurt_masktop_amt.md`(10-04 13:03 生成)
