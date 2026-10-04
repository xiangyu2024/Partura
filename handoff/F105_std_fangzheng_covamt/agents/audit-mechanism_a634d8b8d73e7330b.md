# audit-mechanism:F105_std_fangzheng_covamt — agent a634d8b8d73e7330b(工作流 wf_759ef2d3-03f)

- 状态:**已返回结果**;开始 10-03 23:21,最后一次动作 10-03 23:34;工具调用 40 次
- 这是从 agent 的对话记录里**自动抽出来的动作流水**(命令、输出、写了哪些文件)。agent 的推理不在记录里 ——
  它的判断要看 `notes/F105_std_fangzheng_covamt/journal.md` 和各 notes 文件。输出过长的地方截了中间。

## 动作流水

**10-03 23:21 · Bash** — Read project CLAUDE.md and size of docs

```bash
cd /Users/wxy/Desktop/Partura && cat CLAUDE.md && echo ------- && wc -l docs/method.md docs/study_playbook.md
```

```
# 给接手这个项目的 agent

**读 `docs/method.md` 之前不要开始做研究。** 最容易犯的错是把上一条因子的
`configs/*.yaml` 改个表达式就跑 —— 那不是研究,那是又一次盲搜。

一句话版本:

> 实验计划和探针集合都是**这棵树**的性质,每条表达式都要重新推;
> 唯一跨研究复用的是 `lab/findings.yaml` 里的结论,而且它是**先验**,不是证据。

拿到一条新表达式,按这个顺序走:

1. `partura decompose "<expr>"` —— 先看清楚每个算子的**实现**和**探针实测值**,
   以及实验室里与这棵树相关的既往先验。
2. **想一遍这棵树特有的问题**。内置探针答不上来的,就为这次研究写:
   `studies/<factor_id>/probes.py`,一个探针回答一个问题,声明适用范围,
   写完先在**已知答案的算子**上自检(见 `docs/method.md` §3)。
3. `partura propose "<expr>" --factor-id <fid> --out configs/<fid>.draft.yaml`
   —— 它给的是**候选**。删掉没信息量的,补上只有读了这棵树才想得到的,
   每条 `why` 写成一句可证伪的话;控制变量、门控、诊断项按这棵树的嫌疑挑。
4. `partura run` 训练段 + 验证段,一个阶段回答一个问题,看完结果再决定下一阶段。
5. `--holdout` 只用一次,在最终候选上。
6. `partura report`,然后把**可迁移**的结论写回 `lab/findings.yaml`,
   每条都要写清楚**什么情况下会失效**。

硬规矩:方向只在训练段定一次;所有钱的数字扣 15 bp 并给换手;留出段有台账;
原始结果不覆盖;判据一律实测,不写死名单。
-------
     123 docs/method.md
     181 docs/study_playbook.md
     304 total
```

10-03 23:21 · 读 `/Users/wxy/Desktop/Partura/docs/method.md`

10-03 23:21 · 读 `/Users/wxy/Desktop/Partura/docs/study_playbook.md`

**10-03 23:21 · Bash** — List study materials for F105

```bash
cd /Users/wxy/Desktop/Partura && ls -la notes/F105_std_fangzheng_covamt/ runs/F105_std_fangzheng_covamt/ studies/F105_std_fangzheng_covamt/ 2>&1; wc -l research/alpha_distillation/F105_std_fangzheng_covamt.md configs/F105_std_fangzheng_covamt.yaml
```

```
notes/F105_std_fangzheng_covamt/:
total 240
drwxr-xr-x@ 24 wxy  staff   768 Oct  3 23:14 .
drwxr-xr-x@ 10 wxy  staff   320 Oct  3 18:37 ..
-rw-r--r--@  1 wxy  staff   796 Oct  3 23:17 01_expression.md
-rw-r--r--@  1 wxy  staff  1856 Oct  3 18:40 02_operators.md
-rw-r--r--@  1 wxy  staff  1821 Oct  3 18:40 03_decomposition.md
-rw-r--r--@  1 wxy  staff  1652 Oct  3 18:40 04_grammar.md
-rw-r--r--@  1 wxy  staff  5573 Oct  3 23:17 05_hypotheses.md
-rw-r--r--@  1 wxy  staff  3246 Oct  3 18:43 06_baseline.md
-rw-r--r--@  1 wxy  staff  3029 Oct  3 22:39 07_S1_what.md
-rw-r--r--@  1 wxy  staff  4427 Oct  3 23:18 07_S1b_events.md
-rw-r--r--@  1 wxy  staff  4212 Oct  3 22:50 07_S2_nodes.md
-rw-r--r--@  1 wxy  staff  3728 Oct  3 22:50 07_S3_family.md
-rw-r--r--@  1 wxy  staff  4118 Oct  3 23:00 07_S4_longleg.md
-rw-r--r--@  1 wxy  staff  3481 Oct  3 23:12 07_S_final.md
-rw-r--r--@  1 wxy  staff  1827 Oct  3 23:17 07_conditional.md
-rw-r--r--@  1 wxy  staff  1068 Oct  3 23:09 07_controls.md
-rw-r--r--@  1 wxy  staff  3047 Oct  3 23:09 07_neutralise.md
-rw-r--r--@  1 wxy  staff  7084 Oct  3 23:17 07x_events.md
-rw-r--r--@  1 wxy  staff  5332 Oct  3 23:19 07x_longleg.md
-rw-r--r--@  1 wxy  staff  2635 Oct  3 23:17 08_variants.md
-rw-r--r--@  1 wxy  staff  6041 Oct  3 23:13 09_diagnosis.md
-rw-r--r--@  1 wxy  staff  5462 Oct  3 23:17 10_distilled.md
-rw-r--r--@  1 wxy  staff  2735 Oct  3 23:14 11_risks.md
-rw-r--r--@  1 wxy  staff  1462 Oct  3 23:14 12_next.md

runs/F105_std_fangzheng_covamt/:
total 1248
drwxr-xr-x@  9 wxy  staff     288 Oct  3 23:11 .
drwxr-xr-x@ 19 wxy  staff     608 Oct  3 17:37 ..
-rw-r--r--@  1 wxy  staff   33700 Oct  3 17:43 S0_baseline.json
-rw-r--r--@  1 wxy  staff   50534 Oct  3 19:37 S1_what.json
-rw-r--r--@  1 wxy  staff  198931 Oct  3 20:12 S1b_S2_S3.json
-rw-r--r--@  1 wxy  staff  176856 Oct  3 22:45 S2S3_nodes_family.json
-rw-r--r--@  1 wxy  staff   74241 Oct  3 22:57 S4_longleg.json
-rw-r--r--@  1 wxy  staff   81069 Oct  3 23:11 final.json
-rw-r--r--@  1 wxy  staff    5067 Oct  3 23:11 ledger.json

studies/F105_std_fangzheng_covamt/:
total 80
drwxr-xr-x@ 6 wxy  staff    192 Oct  3 23:00 .
drwxr-xr-x@ 9 wxy  staff    288 Oct  3 18:37 ..
drwxr-xr-x@ 3 wxy  staff     96 Oct  3 23:00 __pycache__
-rw-r--r--@ 1 wxy  staff  13421 Oct  3 18:42 events.py
-rw-r--r--@ 1 wxy  staff   8594 Oct  3 23:00 longleg.py
-rw-r--r--@ 1 wxy  staff   9923 Oct  3 18:37 probes.py
    1275 research/alpha_distillation/F105_std_fangzheng_covamt.md
     172 configs/F105_std_fangzheng_covamt.yaml
    1447 total
```

10-03 23:21 · 读 `/Users/wxy/Desktop/Partura/configs/F105_std_fangzheng_covamt.yaml`

**10-03 23:21 · Bash** — Read notes 01-06

```bash
cd /Users/wxy/Desktop/Partura && for f in notes/F105_std_fangzheng_covamt/0[1-6]*.md; do echo "=================== $f"; cat "$f"; echo; done
```

```
=================== notes/F105_std_fangzheng_covamt/01_expression.md
这条表达式是挖掘库的 #25:`ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5)`。
用户表里公布的一行是:方向 −1、EMA 半衰期 3、扣费多空夏普 训练 3.03 / 测试 2.24、多头腿毛超额 16.8% / 14.3%。
S0 用 Partura 自己求值复现了训练列(3.03、16.8%);留出段那一次(S_final)复现了测试列(2.24、14.3%)。

**一句话(读完源码之后)**:它是「**分钟成交额方差**(带成交额平方的尺度)的**一年期 mean+std 水平**,在**最近 5 天里动了多少**」——
也就是「最近一周有没有一个(按原始金额计)很大的放量日**进入**一年窗口,或者一年前的那个放量日**滑出**窗口」。
它不是一个「波动的波动」,名字里的两个 std 都不是收益的波动。

=================== notes/F105_std_fangzheng_covamt/02_operators.md
读内核源码(`study.sh src`)时发现的、和名字不一样或探针表里看不出来的事:

1. **`day_cov(Amt, Amt)` 就是日内分钟成交额的总体方差**(分母是有效分钟数,不是 n−1;有效分钟 < 2 时为 NaN)。
   它恒非负、对 Amt 是 **2 次齐次**(探针实测 k = 2.0)。和 `day_var(Amt)` = `day_std(Amt)²` 是同一个量,
   所以这棵树从叶子开始就带着「成交额的平方」这个尺度,而且一路没有任何去尺度的节点(后面三层都是 1 次齐次)。
2. **`cross_fangzheng(x, d)` = `cross_mean(x, d) + cross_stddev(x, d)`**,一行代码。名字(方正?)没有任何信息量。
   两项都是**硬窗口**、**忽略 NaN**(`nanmean` / 总体 `nanstd`,分母是窗口内有限值的个数)。
3. **241 在这里是交易日数,不是分钟数。** `cross_*` 滚的是交易日轴;241 恰好是每天的分钟格数,
   但作为 `cross_fangzheng` 的窗口它是「约一年」(一年约 243 个交易日)。
4. **窗口不满也出值。** `rolling_windows` 在左侧补 NaN,`nanmean/nanstd` 只在有限值上算,所以一只股票上市后的
   头 241 个交易日、以及样本头一年(视图从 20180102 开始,warmup 实际拿到 0 行),`C` 用的是**逐日变长的扩张窗口**:
   第 n 天进来一个新值,均值移动 (x−均值)/n,比窗口满了之后的 1/241 大得多。→ 次新股的 `D` 被机械放大(见 H7)。
5. **`ts_stddev` = `ts_std`**,总体标准差,同样忽略 NaN。它对输入取负不变(偶函数):`C` 往上走和往下走读出来一样。
6. **内置探针在 241 窗口上是瞎的。** 内置探针的样本只有 40 行,比窗口短:`cross_fangzheng` 的「脉冲记忆天数 = 27」
   只是 40 − 13 = 27(脉冲之后剩下的行数),不是这个算子的性质。本研究的四个探针都用 ≥ 3×窗口 的样本重测。

=================== notes/F105_std_fangzheng_covamt/03_decomposition.md
分解表之外需要说清楚的三个公式(全部来自源码 + 本研究的探针,不是名字):

**(1) 根节点读的是「慢水平的 5 日变化量」。** `C` 是一年窗口的统计量,一天只进一个值、出一个值,
… (82 行略) …
   +11.0%、+15.0%、**+13.5%** —— 最差的一档独自亏 30%,而最好的两档差不多,Q10 还不如 Q9。
   验证段同样是 Q1 −34.8%,但 Q10 跳到 +27.8%(Q9 +15.0%)。也就是说**「因子最大」是一个很强的卖出信号,
   「因子最小」只是一个温和的、不单调的买入信号**。
3. **原始面板在多头端是噪声,靠平滑才能交易。** 半衰期扫描(训练段):hl 0 时多空夏普 +1.83、纯多头夏普 **−0.09**、
   日换手 13%;hl 3 时 +2.54 / +1.32 / 6%;hl 10 时 +2.32 / **+1.49** / 3%。多头腿想要的半衰期比多空夏普选出来的更长。
4. **IC 随预测期单调上升**(h1 0.0387 → h5 0.0669 → h20 0.0983):这是一个缓慢变化的股票特征在预测持续漂移,
   不是一个三五天就消失的事件信号 —— 这和「事件探测器」的结构读法(04 节)是有张力的,S1 要回答。
5. **逐年都为正**,多空夏普 2018 +3.44、2019 +2.60、2020 **+1.50**、2021 +2.74、2022 **+5.91**、2023 +2.59;
   多头腿毛超额 17.3% / 11.8% / 8.6% / 14.9% / 31.2% / 17.2%。2020 最弱,2022 最强(验证段的高数字主要是 2022 这一年)。
6. **两道门槛都过**:cov 1.00、dist 1.00。

**已知暴露的初读**(中性化表,对象是实际交易的信号):全部控制变量张成 R² **0.500**(原始面板上 0.490,两者几乎一样,
说明这个因子本身就是慢变量);`ctl_amt` 单独 0.418、`ctl_dvol20` 0.217、`ctl_turnrate` 0.193。
对 `ctl_amt` 中性化后 rank IC 从 0.0371 掉到 0.0159(−57%),空头腿从 +29.9% 掉到 **+4.8%**,而多头腿毛超额还剩 +8.6%;
对全部控制变量中性化后 rank IC 0.0100、无成本多空夏普 +1.47、空头腿 +0.6%、多头腿毛超额 +8.7%。
**空头腿的钱几乎全是成交额水平;多头腿的钱有一多半不是。** 这是这条因子最值得追的一点。

与已知家族的 rank 相关只有 0.68(`known_stdamt_max9`、`known_amt_max9`),远低于「同一因子族」的 0.95,
但 `known_stdamt_max9` 自己当因子时(训练/验证)多空夏普 +2.47 / +4.44、多头腿毛超额 +16.9% / +24.9%,
和原式(+2.54 / +4.62、+13.1% / +26.0%)几乎打平 —— 「相关只有 0.68 但业绩一样」正是 S1 要拆的问题。
```

**10-03 23:21 · Bash** — Read stage notes S1 to S_final

```bash
cd /Users/wxy/Desktop/Partura && for f in notes/F105_std_fangzheng_covamt/07_S1*.md notes/F105_std_fangzheng_covamt/07_S2*.md notes/F105_std_fangzheng_covamt/07_S3*.md notes/F105_std_fangzheng_covamt/07_S4*.md notes/F105_std_fangzheng_covamt/07_S_final.md; do echo "=================== $f"; cat "$f"; echo; done
```

```
=================== notes/F105_std_fangzheng_covamt/07_S1_what.md
**问题**:原式的预测力在水平里、在事件的方向里,还是都不在?它和已知家族比怎么样?
(这一阶段第一次运行时有 3 个变体因为显卡被邻居占满而 OOM,没跑出来的挪到了 S1b_events;这里只读跑出来的 3 个。)

**结果(train / valid)**

1. **只留一年水平 `C`(`s1_level`)**:rank IC 0.0262 / 0.0313(原式 0.0387 / 0.0521),扣费多空夏普 +1.82 / +3.36(原式 +2.54 / +4.62)——
   多空明显变差,**H1 的「纯水平不输原式」被否定**:外层「5 日变化量」确实带来了水平之外的信息。
   但多头腿不是这样:毛超额 +10.6% / +20.0% 低于原式的 +13.1% / +26.0%,而**净超额 +9.5% / +19.3% 与原式的 +8.2% / +20.7% 打平**,
   因为它的多空日换手只有 1.2%(原式 6.0%),半衰期选的是 0。也就是说:原式比纯水平多出来的那部分信息,在多头腿上基本被换手吃掉了。
2. **带符号的 5 日差分(`s1_signed`)**:多空夏普 +1.35 / +1.38,多头腿毛超额 **−6.8% / −11.9%**(多头占比 −33%),
   与原式的 rank 相关 −0.18。把「`C` 降得最多」的股票排在多头端是亏钱的 —— 这些是一年前爆过量、现在回声滑出窗口的大成交额股票。
   **方向不是信息**:H2+H3 预测的「带符号不比不分方向差」被否定,不分方向的 std 之所以能用,只是因为它把这群股票和新放量的股票一起放进了空头端。
3. **已知家族 `cross_max(day_std(Amt), 9)`(`s1_known_stdamt9`)**:rank IC 0.0484 / 0.0671,多空夏普 +2.47 / +4.44,
   多头腿毛超额 +16.9% / +24.9%、净超额 +9.3% / +18.5%,日换手 8.5%。2 个算子,多空与原式打平(+2.54 / +4.62),rank IC 更高,
   多头腿毛超额在训练段高 3.8 个点。它的短板是换手:按多空夏普选出来的半衰期是 0,多头腿每年被成本吃掉 7.6 个点;
   半衰期扫描里 hl=5 时纯多头夏普 +1.99、多头腿净超额 +13.7%(train),但那不是按规则选出来的半衰期。

**中性化(这一阶段新增的两张)**

- `s1_level` 对 `ctl_amt` 中性化:R² 0.449,残差 rank IC **−0.0007**、无成本多空夏普 +0.07、多头腿毛超额 +0.9%。
  **一年水平 `C` 里的预测力 100% 是当前成交额水平**;「这一年里爆过多大的量」在成交额水平之外没有任何信息。
- `s1_known_stdamt9` 对 `ctl_amt` 中性化:R² 0.790,残差 rank IC **0.0270**、无成本多空夏普 **+4.93**、多头腿毛超额 +11.8%、空头腿 +20.7%。
  已知家族在成交额水平之外还有一大块(「最近 9 天的峰值相对今天的成交额」= 近期放量事件),而且这一块比水平更值钱 —— 但它的换手是 44.7%。

**解读**:原式 = 水平 × 事件。水平那一半就是成交额水平(而且是它的一个更吵的版本);事件那一半的方向没有信息。
已知家族用更少的节点同时拿到了这两半,而且拿得更干净(07x 第 6 张表:原式对已知家族中性化后残差 rank IC 0.0090、无成本多空夏普 −0.55)。

=================== notes/F105_std_fangzheng_covamt/07_S1b_events.md
**问题**:把成交额尺度除掉之后,「事件」这一半自己还剩多少?周年回声、一年窗口本身,是在挣钱还是在稀释?
… (157 行略) …
3. 2 个算子,窗口在搜索语法的窗口池里;日换手 4.0%(原式 6.0%);分位剖面单调;两道门槛都是 1.00。
4. 它没有原式的三个伪影(周年回声、未满窗口放大、上市首日为 0)。
5. 代价写在前面:**多空夏普比原式低 0.17 / 0.50**(验证段的差超过了 ±0.3 的噪声);rank IC 0.0411 / 0.0585 对 0.0387 / 0.0521。
   要多空夏普的话该用 `f_max15`。另外它是 F001 已经蒸馏出的那个家族的一个成员,不是新因子。

**读之前写下的判据**:
- 留出段上 `f_max30` 的多头腿净超额和纯多头夏普**都**低于 `f_orig` → 升华失败,结论改成「原式保留」。
- `f_min3` 与 `f_orig` 的多空夏普差超过 0.3、且方向是变差 → S2 的「多余节点」只在样本内成立。
- `f_max15 / f_max30 / f_max60` 的多头腿净超额彼此差超过 5 个点 → 平台是样本内的。
- 用户表已经公布了原式在测试段的两个数(多空 2.24、多头腿毛超额 14.3%),所以原式那一行不是新信息;新信息是另外四行和原式的多头腿**净**超额。

**以下写在读完留出段之后。**(上表是决策口径,重复前面阶段的数字;留出段的数字在第 10 节那张「与用户表同口径」的表里,全研究只读了这一次。)

三条判据的结果:

- `f_max30` 留出段多头腿净超额 +12.5%(原式 +8.9%)、纯多头夏普 +1.37(原式 +1.04),**两项都高于原式** → 升华没有被证伪。
- `f_min3` 留出段多空夏普 +2.72(原式 +2.24),差 +0.48,方向是变好 → 「多余节点」的结论在样本外成立。
- `f_max15 / f_max30 / f_max60` 留出段多头腿净超额 +12.0% / +12.5% / +14.7%,最大相差 2.7 个点(< 5)→ 平台在样本外还在。

原式那一行(多空 +2.24、多头腿毛超额 +14.3%)与用户表公布的测试列逐位相同。
```

**10-03 23:21 · Bash** — Read diagnostics and custom analysis notes

```bash
cd /Users/wxy/Desktop/Partura && for f in notes/F105_std_fangzheng_covamt/07_conditional.md notes/F105_std_fangzheng_covamt/07_controls.md notes/F105_std_fangzheng_covamt/07_neutralise.md notes/F105_std_fangzheng_covamt/07x_events.md notes/F105_std_fangzheng_covamt/07x_longleg.md; do echo "=================== $f"; cat "$f"; echo; done
```

```
=================== notes/F105_std_fangzheng_covamt/07_conditional.md
(条件 IC 是原始面板在分桶变量五等分内的 rank IC,训练段;负号 = 与因子方向一致。)

1. **原式在小市值里强、在最大市值里弱**:`v_base|ctl_cap` 从 Q1 的 −0.0559 降到 Q5 的 −0.0191。`s4_max30|ctl_cap` 同一个形状而且更陡
   (−0.0659 → −0.0185)。这一族在市值最大的五分之一里只剩三分之一的预测力。
2. **原式的 IC 有一大半是成交额桶之间的排序**:`v_base|ctl_amt` 桶内只有 −0.0137 ~ −0.0197(无条件是 −0.0387),只有成交额最大的一桶到 −0.0300。
3. **事件成分只在大成交额股票里有用**:`s1_relchg|ctl_amt` Q1..Q5 = −0.0098、−0.0117、−0.0141、−0.0215、**−0.0408**;
   按已知家族分桶更极端(−0.0074、−0.0064、−0.0092、−0.0156、**−0.0437**);按一年水平 `C` 分桶比较平(−0.0167 → −0.0321)。
   写干净的版本 `s4_pos|ctl_amt` 也一样(−0.0142 → −0.0365)。
   07x(events)里「按水平分桶,相对变化每桶都有 IC,所以是相加不是门控」的读法要修正:换成**当前**成交额(或已知家族)来分桶,
   事件的 IC 在最高一桶是最低一桶的 4~6 倍。**事件是「大成交额股票里谁刚爆过量」的细分** —— 这正是空头腿需要的信息,多头腿(低成交额那一端)用不上它。
4. `s4_max30|ctl_turnrate`:−0.0195、−0.0230、−0.0205、−0.0257、−0.0393。换手率最高的一桶里最强,与「空头腿的钱是高换手率」一致。
5. 表里 `s1_relchg|s1_level` 与 `s1_relchg|g_level` 是同一件事算了两遍(`g_level` 就是 `s1_level` 的面板;前一行来自中断前的那次运行)。
   `s1_level|s1_relchg` 是反过来的:按相对变化分桶,水平的桶内 IC 平在 −0.025 ~ −0.029 —— 水平的信息不依赖有没有事件。

=================== notes/F105_std_fangzheng_covamt/07_controls.md
控制变量自己当因子(同一口径,train / valid)能说明两件事:

1. **成交额水平自己就有这条因子的大部分多头腿,但没有它的多空夏普。** `ctl_amt`:多空 +1.03 / +3.47,多头腿毛超额 +9.5% / +23.6%;
   `known_amt_max9`:+1.57 / +3.81、+13.4% / +25.1%;`known_stdamt_max9`:+2.47 / +4.44、+16.9% / +24.9%;原式 +2.54 / +4.62、+13.1% / +26.0%。
   从「今天的成交额」到「9 天峰值」到「日内离散度的 9 天峰值」,多空夏普一级一级上去,多头腿毛超额在验证段几乎不动(23.6% → 25.1% → 24.9%)。
2. **换手率、波动类控制变量在训练段没有多头腿**:`ctl_turnrate` 多头腿毛超额 −0.7% / +10.2%,`ctl_dvol20` −3.7% / +5.0%,`ctl_ivol` −4.2% / +3.2%,
   `known_ivol_max9` −0.5% / +6.1% —— 它们的钱全在空头腿。`ctl_cap` 的方向在训练段是 +(大市值略好,rank IC 0.0016),多头腿 +0.9% / −8.8%。
   **训练段里唯一有多头腿的已知暴露是成交额水平本身**;它既不是单纯的低换手,也不是单纯的小市值。

=================== notes/F105_std_fangzheng_covamt/07_neutralise.md
**怎么读这张表**:被回归掉的是实际交易的信号;残差没有再平滑,所以只看 rank IC、无成本多空夏普和两条腿的毛超额,不看扣费夏普。

1. **原式有一半是已知暴露。** 全部控制变量张成 R² **0.500**(原始日频面板上 0.490,两者几乎一样 —— 这是个慢变量);
   残差 rank IC 0.0100(未中性化 0.0371 的 27%)、无成本多空夏普 +1.47(原 +3.21)、空头腿 +0.6%(原 +29.9%)、多头腿毛超额 +8.7%(原 +13.1%)。
… (154 行略) …
| 2022 | +26.0% / +4.53 | +26.1% / +4.39 | +23.8% / +3.89 | +25.2% / +4.05 | +23.1% / +3.66 |
| 2023(至 8 月 7 日) | +11.7% / +2.43 | +11.9% / +2.46 | +17.0% / +2.96 | +16.9% / +3.00 | +15.7% / +2.81 |

`max30` 的多头腿净超额在 **6 年里有 5 年比原式高 5 个点左右**(+5.5、+5.9、+4.8、+5.6、+5.2),只有 2022 年打平(−0.8)。
阶段表里「验证段打平」是 2022 年打平加上 2023 年领先,不是优势消失。多空夏普则没有一致的方向
(`max30` − `orig`:+0.23、+0.27、−0.31、−0.54、−0.97、+0.38)。

**(4) 容量:把最小的股票从截面里拿掉再建书。**

| 截面 | 多头腿净超额 `orig` | `max15` | `max30` | `max60` |
|---|---|---|---|---|
| 全部 | +8.2% / +20.7% | +12.3% / +21.3% | +13.6% / +22.2% | +13.5% / +20.4% |
| 流通市值分位 ≥ 0.2 | +6.5% / +19.2% | +8.5% / +21.6% | +10.3% / +20.4% | +8.4% / +20.8% |
| 流通市值分位 ≥ 0.5 | **+5.1%** / +15.4% | +1.7% / +17.7% | **+1.8%** / +18.6% | +2.4% / +16.4% |

拿掉最小的 20% 之后 `max30` 的优势还在(训练段 +3.8 个点,验证段 +1.2 个点)。**只留市值大的一半时,训练段这一族的多头腿基本没有了**
(`max30` +1.8%、纯多头夏普 +0.22),原式反而还剩 +5.1%(+0.72);验证段两者都有(+15.4% 对 +18.6%)。
这一族多头腿的钱在小市值的那一半里(条件 IC 也是:`s4_max30` 按市值分五桶的桶内 IC 从最小一桶的 −0.0659 降到最大一桶的 −0.0185)。
(按当天成交额分位 ≥ 0.2 过滤的那一组不能读净值:多头十分位正好贴在过滤边界上,股票每天进出截面,日换手被抬到 13%~19%;
只读毛超额,`max30` 对原式是 +19.6% 对 +15.5%、+23.9% 对 +21.5%,优势还在。)
```

**10-03 23:21 · Bash** — Read notes 08-12

```bash
cd /Users/wxy/Desktop/Partura && for f in notes/F105_std_fangzheng_covamt/08*.md notes/F105_std_fangzheng_covamt/09*.md notes/F105_std_fangzheng_covamt/1*.md; do echo "=================== $f"; cat "$f"; echo; done
```

```
=================== notes/F105_std_fangzheng_covamt/08_variants.md
**怎么读这张总表**:28 个变体(加原式)其实只有四样东西。分组的依据是与原式 / 与已知家族的 rank 相关(各阶段运行里算的,训练段)。

| 组 | 成员(与原式的 rank 相关) | 它是什么 | 多空夏普 | 多头腿净超额 |
|---|---|---|---|---|
| **A 原式和它的树内改写** | `s2_dtface_check` 1.000、`s2_mid_mean` 0.983、`s2_absdelta` 0.981、`s2_no_max3` 0.967、`s2_mid_std` 0.965、`s2_field_std` 0.965、`s2_min3` 0.937;稍远的 `s2_field_sum` 0.894、`s2_out20` 0.826 | 「一年水平量最近几天动了多少」,带成交额平方的尺度 | +2.2~+2.8 / +3.6~+4.8 | +7.8%~+9.9% / +15.5%~+21.2% |
| **B 已知家族(近期成交额峰值)** | 与 `known_stdamt_max9` 的 rank 相关:`s4_max15` 0.941、`s1_recent` 0.939、`s4_mean20` 0.907、`s3_max20` 0.902、`s4_summax30` 0.856、`s4_max30` 0.847、`s3_mean60` 0.821、`s4_med60` 0.779、`s3_max60` 0.759;它们与原式都在 0.60~0.67 | 「最近 d 天日内成交额离散度的峰值 / 均值」 | +1.1~+2.6 / +3.0~+4.5 | +5.8%~+13.6% / +17.2%~+23.0% |
| **C 一年水平** | `s1_level`、`s3_max241`、`s3_mean241`(与原式 0.63~0.68) | 「这一年成交额的峰值 / 均值」,对 `ctl_amt` 中性化后什么都不剩 | +1.6~+1.8 / +3.0~+3.4 | +9.0%~+9.5% / +18.6%~+20.2% |
| **D 无尺度的事件** | `s1_relchg`(与原式 0.68、与已知家族 0.24)、`s4_pos`(0.18 / 0.49)、`s1_signed`(−0.18) | 「相对自己的历史,最近有没有放量」 | +2.0~+3.0 / +2.8~+3.2(`s1_signed` +1.4 / +1.4) | +4.6% / +12.8%~+14.7%(`s1_signed` 为负) |

- A 组内部的差别都在噪声里;唯一一致的改善是删掉多余节点(`s2_min3`、`s2_no_max3`)和去掉上市首日伪影(`s2_absdelta`)。
- **A 组不是 B 组和 C、D 之外的第五样东西**:07x 的回归表明 A 对 B 回归后残差挣不到钱(对 `known_stdamt_max9` 无成本多空夏普 −0.55,对 `max30` +0.02)。
  A = C × D(水平 × 事件,07x events 第 2 节),而 B 在对数空间里也是「水平 + 近期相对水平的峰值」,只是两半都更干净。
- B 组内部按窗口排成一条线:窗口越短 rank IC 和多空夏普越高、换手越高;多头腿净超额在 d=15~60 上是平台(S4 第 1 张表)。
  `s2_w60`(原式的一年窗口换成 60 天)与已知家族的相关升到 0.73,是 A 往 B 走的中间一步。
- `f_*` 五个是留出段那一次用的新 id,表达式与 `v_base`、`s2_min3`、`s4_max15`、`s4_max30`、`s3_max60` 相同;上面的 rank 相关矩阵是这五个之间的:
  原式与 `f_min3` 0.94,与三个已知家族成员 0.63~0.67;三个已知家族成员之间 0.79~0.90。

=================== notes/F105_std_fangzheng_covamt/09_diagnosis.md
### 一句话

这条因子是「成交额水平 × 近期放量事件」的一个绕了远路的写法:它用「一年水平量最近 5 天动了多少」去量近期放量,
顺带掺进了周年回声、未满窗口放大、上市首日为 0 三个伪影。它的信息被已知家族 `cross_max(day_std(Amt), d)` 完全包含;
空头腿的钱是「高换手率的大成交额股票刚放过量」,多头腿的钱是「小市值里成交清淡、近一两个月没放过量」的股票。

### 已确立(每条后面是能指到的实验)

1. **根节点 = 水平 × 事件,两半几乎不相关。** `D` 与 |`C` 的 5 日变化| 的 rank 相关 0.994;`D` 与水平 `C`、与相对变化 `D/C` 各 0.67,
   水平与相对变化之间 0.019(07x events 第 2 节)。
2. **水平那一半就是成交额水平。** `s1_level` 对 `ctl_amt` 中性化后残差 rank IC −0.0007(中性化表);它的朴素等价物 `s3_max241` 指标相同(S3)。
… (124 行略) …
- **过拟合。** 全研究评了 28 个变体;推荐的窗口取自一个四档(15 / 20 / 30 / 60)都成立的平台,不是单点最优,留出段只读了一次。
  但留出段上平台内部的次序与样本内不同(样本内 d=30 最好,留出段 d=60 最好)—— 窗口的精确取值不要当真。
- **成本。** 多头腿毛超额到净超额在训练列掉 3.5 个点(19.6% → 16.1%)、测试列掉 3.2 个点;原式掉 5.0 / 5.4 个点。这是它相对原式的主要优势来源之一,
  成本假设变了(比如低于 15 bp)优势会缩小,窗口更短的成员会重新占优。
- **泄漏。** 没有发现:四个算子的日轴因果性探针都通过,标签是 t+1 开盘 15 分钟 VWAP 到 t+2,因子只用到 t 日收盘。
- **尺度。** 因子值是原始金额单位(1 次齐次),只用于截面排序时没有问题;跨期比较或做数值回归前要先取对数或截面排名。
- **空头腿被标签抬高。** 次日开盘封涨停买不进的票标签是 NaN、在空头里记 0,所有候选的空头腿和多空夏普都带这个偏差;多头腿的数字不受影响。

=================== notes/F105_std_fangzheng_covamt/12_next.md
只列能明显降低不确定性的:

1. **对池内已有的成交额水平结构做增量测试。** 把 `cross_max(day_std(Amt), 30)` 对因子池里已封 / 已入选的成交额类因子(至少 `cross_max(day_std(Amt), 9)`、
   `cross_max(day_sum(Amt), 9)`)中性化,看多头腿净超额还剩多少。07x 的结果预示剩不下多少(对 `known9` 回归后残差 rank IC 0.0037),
   那样结论就是「把池里那个成员的窗口从 9 放慢到 30~60」,而不是加一个因子。
2. **容量曲线。** 用稳定的截面定义(按过去 60 日平均成交额分档、按月换成分,而不是按当天分位过滤)重做 07x longleg 第 4 节,
   看多头腿净超额随「剔掉成交最清淡的 x%」怎么掉;同时把成本换成与成交额挂钩的冲击模型。
3. **上市天数过滤。** 对 `max30` 加「上市满 250 个交易日」之后重跑两本书,确认验证段多头腿里那 7.7% 的次新股不是业绩来源。
4. **把「事件」当排除条件而不是因子。** `s4_pos` 的 Q1(成交量在一年高点附近)训练 / 验证超额 −35.0% / −39.7%,其余九档几乎是平的。
   对纯多头用户,它的用法是「任何多头组合里先剔掉这一档」;值得在一个别的多头因子上测一次剔除前后的差别。
5. **2024 年的回撤归因。** 把 2024 年多头腿的日收益对小市值 / 低流动性指数回归,分清这一族的多头腿是不是在那之后结构性变弱。
```

**10-03 23:21 · Bash** — Read ledger and study.sh script

```bash
cd /Users/wxy/Desktop/Partura && cat runs/F105_std_fangzheng_covamt/ledger.json && cat scripts/study.sh | head -150
```

```
{
  "entries": [
    {
      "when": "2026-10-03T23:51:21Z",
      "split": "train",
      "n_expressions": 1,
      "purpose": "stage metrics + diagnostics",
      "stage": "S0_baseline"
    },
    {
      "when": "2026-10-03T23:51:21Z",
      "split": "valid",
      "n_expressions": 1,
      "purpose": "stage metrics + diagnostics",
      "stage": "S0_baseline"
    },
    {
      "when": "2026-10-03T23:51:21Z",
      "split": "utrain",
      "n_expressions": 1,
      "purpose": "stage metrics + diagnostics",
      "stage": "S0_baseline"
    },
    {
      "when": "2026-10-04T00:25:35Z",
      "split": "train",
      "n_expressions": 1,
      "purpose": "stage metrics + diagnostics",
      "stage": "S0_baseline"
    },
… (255 行略) …
    $RS "$SSH" --include='*.json' --exclude='*' "$HOST:$R/runs/$fid/" "runs/$fid/" 2>/dev/null
    if [ -f "runs/$fid/$tag.json" ]; then "$PY" scripts/summarize.py "runs/$fid/$tag.json";
    else echo "(no runs/$fid/$tag.json — an exec job prints its own output; full log: logs/${fid}_${tag}.log)";
         grep -av 'FutureWarning\|vmap(single_row)\|UserWarning' "logs/${fid}_${tag}.log" | tail -200; fi
    ;;
  digest)
    fid=$1; tag=$2; base=${3:-v_base}
    "$PY" scripts/summarize.py "runs/$fid/$tag.json" --base "$base"
    ;;
  report)
    fid=$1; push "$fid" || exit 1
    $SSH $HOST "$ENV && $RPY -m partura.cli report configs/$fid.yaml 2>&1 | grep -v 'FutureWarning\|vmap(single_row)'" || exit 1
    mkdir -p research/alpha_distillation
    $RS "$SSH" "$HOST:$R/research/alpha_distillation/$fid.md" research/alpha_distillation/ && wc -l "research/alpha_distillation/$fid.md"
    ;;
  status)
    $SSH $HOST "screen -ls | grep pt_ ; echo; nvidia-smi --query-compute-apps=pid,used_memory --format=csv,noheader; awk '/^anon /{printf \"container anon %.1f GiB\n\", \$2/1073741824}' /sys/fs/cgroup/memory.stat; ls $R/tmp/locks 2>/dev/null | tr '\n' ' '"
    ;;
  *) sed -n '2,16p' "$0"; exit 2 ;;
esac
```

**10-03 23:21 · Bash** — Digest of baseline run

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh digest F105_std_fangzheng_covamt S0_baseline 2>&1 | head -150
```

```
===== F105_std_fangzheng_covamt  [S0_baseline.json]  1942d x 5220s  splits ['train', 'valid', 'utrain']  fit=train  182.4s  peak anon 3.05G =====

variant              sgn   rIC tr   rIC va  hl  LS tr  LS va Lgross tr Lgross va  Lnet tr  Lnet va  Lshr    TO   cov  dist
v_base                 -  +0.0387  +0.0521   3  +2.54  +4.62    +13.1%    +26.0%    +8.2%   +20.7%   31%  6.0%  1.00  1.00
  (LS = 扣费多空夏普; Lgross/Lnet = 多头腿毛/净年化超额; Lshr = 多头腿占毛价差的比例; cov = 有标签格子里有值的比例,用户门槛 0.95; dist = 取值离散度,用户门槛 0.5)

与用户表同口径(方向/半衰期在 utrain 上定; holdout = 用户的测试段):
variant              sgn  hl  LS utr   LS ho Lgross utr Lgross ho  Lnet utr  Lnet ho Lsharpe utr Lsharpe ho short utr
v_base                 -   3   +3.03     —       +16.8%       —      +11.8%      —         +1.96        —      +31.1%

半衰期扫描 v_base(fit 段; LS = 扣费多空夏普, Lshp = 纯多头夏普): hl0: LS +1.83 Lshp -0.09 TO 13%  hl1: LS +2.28 Lshp +0.83 TO 10%  hl2: LS +2.51 Lshp +1.29 TO 7%  hl3: LS +2.54 Lshp +1.32 TO 6%  hl5: LS +2.43 Lshp +1.40 TO 5%  hl10: LS +2.32 Lshp +1.49 TO 3%  hl20: LS +1.96 Lshp +1.22 TO 2%
分位超额 v_base [train] Q1..Q10: -30.3% -12.7% -7.3% -2.4% +1.5% +4.7% +7.0% +11.0% +15.0% +13.5%
分位超额 v_base [valid] Q1..Q10: -34.8% -17.3% -9.4% -6.4% +2.2% +3.0% +8.5% +11.5% +15.0% +27.8%

中性化 v_base(fit 段;对象是**实际交易的信号** = 方向 x 面板、按半衰期平滑;残差不再平滑):
  (LSgross = 无成本多空夏普:残差没有再平滑、换手更高,扣费夏普塌掉可能只是成本;alpha 还在不在看 rIC 和 LSgross)
  (未中性化)         R2   —    rIC +0.0371  LSgross +3.21  LS +2.54  Lgross +13.1%  short +29.9%  TO 6.0%
  all_controls   R2 0.500  残差 rIC +0.0100  LSgross +1.47  LS -4.50  Lgross +8.7%  short +0.6%  TO 24.4%  (原始日频面板上的 R2 只有 0.490)
  ctl_amt        R2 0.418  残差 rIC +0.0159  LSgross +1.72  LS -3.34  Lgross +8.6%  short +4.8%  TO 26.1%
  ctl_price      R2 0.068  残差 rIC +0.0361  LSgross +3.78  LS +2.88  Lgross +11.7%  short +28.2%  TO 6.3%
  ctl_ivol       R2 0.039  残差 rIC +0.0300  LSgross +3.27  LS +0.81  Lgross +14.3%  short +19.7%  TO 16.9%
  ctl_range      R2 0.079  残差 rIC +0.0282  LSgross +4.24  LS -0.93  Lgross +16.6%  short +23.2%  TO 32.1%
  ctl_rev1       R2 0.011  残差 rIC +0.0388  LSgross +3.74  LS +1.69  Lgross +16.2%  short +31.9%  TO 17.4%
  ctl_mom20      R2 0.028  残差 rIC +0.0330  LSgross +3.16  LS +1.94  Lgross +14.8%  short +20.4%  TO 8.8%
  ctl_dvol20     R2 0.217  残差 rIC +0.0189  LSgross +2.63  LS +0.99  Lgross +15.9%  short +7.7%  TO 9.7%
  ctl_cap        R2 0.073  残差 rIC +0.0381  LSgross +2.97  LS +2.29  Lgross +9.5%  short +31.0%  TO 6.1%
  ctl_turnrate   R2 0.193  残差 rIC +0.0208  LSgross +2.53  LS -0.15  Lgross +16.8%  short +10.0%  TO 18.8%
条件 IC v_base|ctl_cap: Q1 -0.0559  Q2 -0.0484  Q3 -0.0487  Q4 -0.0402  Q5 -0.0191
条件 IC v_base|ctl_amt: Q1 -0.0153  Q2 -0.0137  Q3 -0.0146  Q4 -0.0197  Q5 -0.0300

控制变量 / 已知家族自己当因子(同口径):
  ctl_amt           - rIC +0.0419 hl 3  LS +1.03/+3.47  Lgross +9.5%/+23.6%  TO 5.5%
  ctl_price         - rIC +0.0059 hl 1  LS +0.08/+2.09  Lgross +4.8%/+12.1%  TO 1.0%
  ctl_ivol          - rIC +0.0403 hl 10  LS +1.07/+1.85  Lgross -4.2%/+3.2%  TO 4.4%
  ctl_range         - rIC +0.0388 hl 20  LS +0.76/+1.61  Lgross -2.4%/+9.1%  TO 3.4%
  ctl_rev1          - rIC +0.0143 hl 20  LS +1.51/+2.21  Lgross +5.2%/+6.4%  TO 14.3%
  ctl_mom20         - rIC +0.0334 hl 5  LS +1.06/+2.23  Lgross +4.7%/+10.5%  TO 6.9%
  ctl_dvol20        - rIC +0.0456 hl 0  LS +0.80/+1.57  Lgross -3.7%/+5.0%  TO 9.0%
  ctl_cap           + rIC +0.0016 hl 20  LS +0.01/-0.94  Lgross +0.9%/-8.8%  TO 0.5%
  ctl_turnrate      - rIC +0.0462 hl 5  LS +1.06/+2.43  Lgross -0.7%/+10.2%  TO 4.0%
  known_amt_max9    - rIC +0.0415 hl 1  LS +1.57/+3.81  Lgross +13.4%/+25.1%  TO 5.4%
  known_stdamt_max9 - rIC +0.0484 hl 0  LS +2.47/+4.44  Lgross +16.9%/+24.9%  TO 8.5%
  known_ivol_max9   - rIC +0.0501 hl 10  LS +1.66/+2.06  Lgross -0.5%/+6.1%  TO 3.5%

与 v_base 的日截面 rank 相关(fit 段; |.|>=0.95 = 同一因子族): known_stdamt_max9 +0.68  known_amt_max9 +0.68  ctl_amt +0.65  ctl_turnrate +0.44  ctl_dvol20 +0.41  ctl_cap +0.26  ctl_price +0.26  known_ivol_max9 +0.24  ctl_ivol +0.21  ctl_mom20 +0.14  ctl_rev1 -0.02

逐年 v_base: 2018 LS +3.44 Lg +17.3%  2019 LS +2.60 Lg +11.8%  2020 LS +1.50 Lg +8.6%  2021 LS +2.74 Lg +14.9%  2022 LS +5.91 Lg +31.2%  2023 LS +2.59 Lg +17.2%
衰减 v_base rank IC: h1 +0.0387  h2 +0.0501  h3 +0.0570  h5 +0.0669  h10 +0.0813  h20 +0.0983
```

**10-03 23:21 · Bash** — Digest of S1_what run

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh digest F105_std_fangzheng_covamt S1_what 2>&1 | head -120
```

```
===== F105_std_fangzheng_covamt  [S1_what.json]  1942d x 5220s  splits ['train', 'valid', 'utrain']  fit=train  200.3s  peak anon 3.33G =====
  ERROR s1_relchg: evaluate: ts_stddev: OutOfMemoryError: CUDA out of memory. Tried to allocate 388.00 MiB. GPU 0 has a total capacity of 31.36 GiB of which 323.69 MiB is free. Pr
  ERROR s1_noecho: evaluate: ts_stddev: OutOfMemoryError: CUDA out of memory. Tried to allocate 194.00 MiB. GPU 0 has a total capacity of 31.36 GiB of which 163.69 MiB is free. Pr
  ERROR s1_recent: evaluate: ts_stddev: OutOfMemoryError: CUDA out of memory. Tried to allocate 388.00 MiB. GPU 0 has a total capacity of 31.36 GiB of which 323.69 MiB is free. Pr

variant              sgn   rIC tr   rIC va  hl  LS tr  LS va Lgross tr Lgross va  Lnet tr  Lnet va  Lshr    TO   cov  dist
s1_level               -  +0.0262  +0.0313   0  +1.82  +3.36    +10.6%    +20.0%    +9.5%   +19.3%   41%  1.2%  1.00  1.00
s1_relchg            ERROR evaluate: ts_stddev: OutOfMemoryError: CUDA out of memory. Tried to allocate 388.00 MiB. GPU 0 has a total cap
s1_signed              -  +0.0185  +0.0267  10  +1.35  +1.38     -6.8%    -11.9%    -8.7%   -14.1%  -33%  2.9%  0.99  0.99
s1_noecho            ERROR evaluate: ts_stddev: OutOfMemoryError: CUDA out of memory. Tried to allocate 194.00 MiB. GPU 0 has a total cap
s1_recent            ERROR evaluate: ts_stddev: OutOfMemoryError: CUDA out of memory. Tried to allocate 388.00 MiB. GPU 0 has a total cap
s1_known_stdamt9       -  +0.0484  +0.0671   0  +2.47  +4.44    +16.9%    +24.9%    +9.3%   +18.5%   31%  8.5%  1.00  1.00
  (LS = 扣费多空夏普; Lgross/Lnet = 多头腿毛/净年化超额; Lshr = 多头腿占毛价差的比例; cov = 有标签格子里有值的比例,用户门槛 0.95; dist = 取值离散度,用户门槛 0.5)

固定半衰期下的 train 表现(各变体自己选的半衰期不同,先看这张再比结构):
variant                hl5 LS    Lnet    TO  hl10 LS    Lnet    TO  hl20 LS    Lnet    TO
s1_level                +1.65   +8.2%    1%    +1.54   +7.1%    1%    +1.47   +6.6%    1%
s1_signed               +1.33  -10.8%    4%    +1.35   -8.7%    3%    +1.19   -8.0%    2%
s1_known_stdamt9        +2.17  +13.7%    4%    +1.99  +13.1%    3%    +1.79  +12.2%    2%
分位超额 s1_level [train] Q1..Q10: -15.7% -11.7% -5.7% -5.9% +1.1% +1.9% +6.4% +8.9% +9.7% +11.1%
分位超额 s1_level [valid] Q1..Q10: -17.9% -14.4% -8.5% -6.6% -0.9% +4.0% +3.1% +6.6% +11.4% +23.4%
分位超额 s1_known_stdamt9 [train] Q1..Q10: -38.3% -17.4% -7.7% -2.6% +3.5% +6.3% +10.3% +13.6% +14.8% +17.5%
分位超额 s1_known_stdamt9 [valid] Q1..Q10: -48.7% -19.2% -11.3% -1.7% +0.8% +6.0% +9.5% +15.2% +21.8% +27.7%

中性化 s1_level(fit 段;对象是**实际交易的信号** = 方向 x 面板、按半衰期平滑;残差不再平滑):
  (LSgross = 无成本多空夏普:残差没有再平滑、换手更高,扣费夏普塌掉可能只是成本;alpha 还在不在看 rIC 和 LSgross)
  (未中性化)         R2   —    rIC +0.0262  LSgross +1.95  LS +1.82  Lgross +10.6%  short +15.5%  TO 1.2%
  all_controls   R2 0.538  残差 rIC +0.0028  LSgross -0.23  LS -6.36  Lgross -0.0%  short -1.4%  TO 25.6%  (原始日频面板上的 R2 只有 0.538)
  ctl_amt        R2 0.449  残差 rIC -0.0007  LSgross +0.07  LS -3.45  Lgross +0.9%  short -0.2%  TO 23.9%
  ctl_price      R2 0.079  残差 rIC +0.0254  LSgross +2.32  LS +2.07  Lgross +8.7%  short +15.7%  TO 1.7%
  ctl_ivol       R2 0.018  残差 rIC +0.0216  LSgross +1.95  LS +0.61  Lgross +10.8%  short +12.2%  TO 10.4%
  ctl_range      R2 0.049  残差 rIC +0.0191  LSgross +2.57  LS -0.89  Lgross +11.7%  short +15.9%  TO 24.6%
  ctl_rev1       R2 0.012  残差 rIC +0.0278  LSgross +2.46  LS +0.49  Lgross +12.6%  short +18.8%  TO 16.6%
  ctl_mom20      R2 0.014  残差 rIC +0.0261  LSgross +2.28  LS +1.56  Lgross +11.6%  short +15.7%  TO 5.6%
  ctl_dvol20     R2 0.125  残差 rIC +0.0114  LSgross +1.30  LS +0.42  Lgross +8.0%  short +4.7%  TO 5.7%
  ctl_cap        R2 0.118  残差 rIC +0.0281  LSgross +1.83  LS +1.64  Lgross +5.9%  short +20.5%  TO 1.8%
  ctl_turnrate   R2 0.153  残差 rIC +0.0105  LSgross +1.46  LS -0.69  Lgross +10.8%  short +5.5%  TO 15.8%

中性化 s1_known_stdamt9(fit 段;对象是**实际交易的信号** = 方向 x 面板、按半衰期平滑;残差不再平滑):
  (LSgross = 无成本多空夏普:残差没有再平滑、换手更高,扣费夏普塌掉可能只是成本;alpha 还在不在看 rIC 和 LSgross)
  (未中性化)         R2   —    rIC +0.0484  LSgross +3.24  LS +2.47  Lgross +16.9%  short +37.7%  TO 8.5%
  all_controls   R2 0.834  残差 rIC +0.0193  LSgross +5.03  LS -6.11  Lgross +10.2%  short +17.2%  TO 39.4%  (原始日频面板上的 R2 只有 0.834)
  ctl_amt        R2 0.790  残差 rIC +0.0270  LSgross +4.93  LS -5.29  Lgross +11.8%  short +20.7%  TO 44.7%
  ctl_price      R2 0.147  残差 rIC +0.0492  LSgross +4.13  LS +3.08  Lgross +12.2%  short +41.3%  TO 9.0%
  ctl_ivol       R2 0.104  残差 rIC +0.0379  LSgross +3.25  LS +0.20  Lgross +19.9%  short +20.0%  TO 24.7%
  ctl_range      R2 0.167  残差 rIC +0.0360  LSgross +4.25  LS -1.32  Lgross +21.9%  short +26.9%  TO 42.3%
  ctl_rev1       R2 0.014  残差 rIC +0.0496  LSgross +3.60  LS +1.55  Lgross +18.4%  short +38.7%  TO 21.6%
  ctl_mom20      R2 0.087  残差 rIC +0.0411  LSgross +2.76  LS +1.06  Lgross +18.3%  short +18.1%  TO 14.5%
  ctl_dvol20     R2 0.286  残差 rIC +0.0290  LSgross +2.38  LS +0.81  Lgross +19.7%  short +9.2%  TO 12.6%
  ctl_cap        R2 0.254  残差 rIC +0.0543  LSgross +3.47  LS +2.66  Lgross +7.9%  short +53.3%  TO 9.5%
  ctl_turnrate   R2 0.222  残差 rIC +0.0324  LSgross +2.42  LS +0.28  Lgross +24.5%  short +8.7%  TO 19.4%
衰减 s1_known_stdamt9 rank IC: h1 +0.0484  h2 +0.0618  h3 +0.0691  h5 +0.0787  h10 +0.0924  h20 +0.1053
```

**10-03 23:21 · Bash** — Digest of S2S3 run

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh digest F105_std_fangzheng_covamt S2S3_nodes_family 2>&1 | head -230
```

```
===== F105_std_fangzheng_covamt  [S2S3_nodes_family.json]  1942d x 5220s  splits ['train', 'valid', 'utrain']  fit=train  411.4s  peak anon 4.6G =====

variant              sgn   rIC tr   rIC va  hl  LS tr  LS va Lgross tr Lgross va  Lnet tr  Lnet va  Lshr    TO   cov  dist
s1_relchg              -  +0.0259  +0.0376   5  +2.96  +2.79     +9.5%    +18.8%    +4.6%   +14.7%   25%  7.0%  1.00  1.00
s1_noecho              -  +0.0337  +0.0380   1  +2.23  +3.78    +12.1%    +18.0%    +6.3%   +13.2%   29%  6.6%  1.00  1.00
s1_recent              -  +0.0480  +0.0649   3  +2.31  +3.97    +16.6%    +22.3%   +10.8%   +17.2%   35%  6.7%  1.00  1.00
s2_dtface_check        -  +0.0387  +0.0521   3  +2.54  +4.62    +13.1%    +26.0%    +8.2%   +20.7%   31%  6.0%  1.00  1.00
s2_no_max3             -  +0.0403  +0.0533   3  +2.67  +4.77    +14.5%    +26.6%    +9.4%   +21.2%   31%  6.2%  1.00  1.00
s2_mid_std             -  +0.0376  +0.0507   3  +2.64  +4.65    +12.6%    +25.0%    +8.0%   +20.4%   29%  5.8%  1.00  1.00
s2_mid_mean            -  +0.0378  +0.0517   3  +2.21  +4.44    +13.7%    +25.5%    +8.6%   +20.4%   35%  5.7%  1.00  1.00
s2_min3                -  +0.0392  +0.0522   3  +2.84  +4.80    +14.3%    +25.5%    +9.9%   +20.9%   30%  5.9%  1.00  1.00
s2_field_std           -  +0.0388  +0.0491   5  +2.72  +4.00    +14.1%    +21.3%    +9.0%   +16.2%   31%  6.1%  1.00  1.00
s2_field_sum           -  +0.0362  +0.0486   3  +2.29  +3.62    +14.0%    +21.7%    +7.8%   +15.5%   32%  7.1%  1.00  1.00
s2_w60                 -  +0.0403  +0.0539   3  +2.18  +4.28    +14.2%    +23.7%    +7.8%   +17.8%   33%  7.7%  1.00  1.00
s2_out20               -  +0.0344  +0.0468   1  +2.34  +4.39    +12.9%    +24.4%    +8.7%   +20.1%   34%  4.6%  1.00  1.00
s2_absdelta            -  +0.0379  +0.0511   2  +2.57  +4.64    +15.7%    +26.6%    +9.8%   +20.2%   35%  6.8%  0.99  0.99
s3_max241              -  +0.0251  +0.0283   0  +1.77  +3.35    +10.1%    +19.4%    +9.0%   +18.6%   42%  1.2%  1.00  1.00
s3_max20               -  +0.0446  +0.0630   0  +2.54  +4.35    +17.4%    +24.9%   +12.6%   +20.9%   35%  5.2%  1.00  1.00
s3_max60               -  +0.0350  +0.0476   0  +2.14  +3.64    +15.9%    +22.3%   +13.5%   +20.4%   43%  2.6%  1.00  1.00
s3_max120              -  +0.0298  +0.0385   0  +1.84  +3.55    +13.2%    +21.1%   +11.6%   +19.9%   46%  1.7%  1.00  1.00
s3_mean60              -  +0.0295  +0.0482   0  +1.70  +3.54    +13.7%    +24.4%   +12.0%   +23.0%   44%  1.9%  1.00  1.00
s3_mean241             -  +0.0224  +0.0340   0  +1.61  +3.03    +10.2%    +20.8%    +9.3%   +20.2%   41%  1.1%  1.00  1.00
  (LS = 扣费多空夏普; Lgross/Lnet = 多头腿毛/净年化超额; Lshr = 多头腿占毛价差的比例; cov = 有标签格子里有值的比例,用户门槛 0.95; dist = 取值离散度,用户门槛 0.5)

固定半衰期下的 train 表现(各变体自己选的半衰期不同,先看这张再比结构):
variant                hl5 LS    Lnet    TO  hl10 LS    Lnet    TO  hl20 LS    Lnet    TO
s1_relchg               +2.96   +4.6%    7%    +2.80   +4.4%    5%    +2.19   +3.5%    4%
s1_noecho               +2.12   +8.6%    3%    +1.96   +8.6%    2%    +1.77   +7.6%    2%
s1_recent               +2.21  +11.8%    5%    +2.09  +11.9%    3%    +1.76  +10.1%    2%
s2_dtface_check         +2.43   +8.7%    5%    +2.32   +9.3%    3%    +1.96   +7.7%    2%
s2_no_max3              +2.60   +9.7%    5%    +2.47  +10.7%    3%    +2.11   +9.0%    2%
s2_mid_std              +2.59   +9.0%    5%    +2.45   +9.7%    3%    +2.07   +7.5%    2%
s2_mid_mean             +2.16   +8.9%    4%    +2.03   +8.8%    3%    +1.80   +7.5%    2%
s2_min3                 +2.78  +10.2%    5%    +2.62  +11.1%    3%    +2.26   +9.6%    2%
s2_field_std            +2.72   +9.0%    6%    +2.53   +9.4%    4%    +2.21   +8.5%    3%
s2_field_sum            +2.27   +8.7%    5%    +2.05   +9.2%    4%    +1.76   +8.3%    3%
s2_w60                  +1.98   +7.3%    6%    +1.89   +9.0%    4%    +1.64   +8.0%    3%
s2_out20                +2.07   +8.7%    3%    +1.86   +7.9%    3%    +1.67   +6.5%    2%
s2_absdelta             +2.48  +10.9%    4%    +2.44  +11.4%    3%    +2.13  +10.2%    2%
s3_max241               +1.51   +7.3%    1%    +1.38   +6.4%    1%    +1.22   +4.6%    1%
s3_max20                +2.00  +13.2%    3%    +1.85  +12.3%    2%    +1.62  +10.5%    2%
s3_max60                +1.73  +11.9%    2%    +1.51  +10.5%    2%    +1.40   +9.2%    1%
s3_max120               +1.49   +9.7%    1%    +1.33   +8.7%    1%    +1.17   +6.8%    1%
s3_mean60               +1.42   +9.4%    1%    +1.42   +9.0%    1%    +1.22   +7.7%    1%
s3_mean241              +1.43   +7.3%    1%    +1.33   +6.4%    1%    +1.19   +5.6%    1%
分位超额 s1_relchg [train] Q1..Q10: -28.7% -7.1% -1.1% +3.7% +2.9% +3.3% +5.2% +5.8% +6.4% +9.5%
分位超额 s1_relchg [valid] Q1..Q10: -19.3% -6.9% -4.0% -2.6% -4.2% -3.0% +2.7% +6.9% +11.3% +19.2%
分位超额 s1_noecho [train] Q1..Q10: -29.4% -14.4% -7.2% -1.2% +2.6% +4.7% +8.9% +11.4% +12.0% +12.7%
分位超额 s1_noecho [valid] Q1..Q10: -32.5% -14.9% -5.3% -2.8% +1.0% +5.6% +6.1% +9.1% +13.0% +20.8%
分位超额 s1_recent [train] Q1..Q10: -31.6% -18.0% -7.5% -1.5% +1.5% +5.4% +8.5% +12.0% +14.1% +17.3%
分位超额 s1_recent [valid] Q1..Q10: -42.5% -20.3% -10.1% -2.7% -0.9% +6.2% +8.5% +14.6% +22.9% +24.3%
分位超额 s2_mid_mean [train] Q1..Q10: -25.8% -15.3% -7.0% -3.0% +0.3% +4.2% +9.3% +11.1% +12.3% +14.1%
分位超额 s2_mid_mean [valid] Q1..Q10: -33.5% -19.2% -10.6% -6.0% +2.4% +4.2% +6.8% +12.1% +16.2% +27.5%
分位超额 s2_absdelta [train] Q1..Q10: -29.2% -13.3% -7.2% -2.2% +1.7% +3.4% +7.4% +11.0% +12.6% +15.8%
分位超额 s2_absdelta [valid] Q1..Q10: -35.1% -17.4% -8.4% -4.5% +0.2% +3.2% +5.8% +12.3% +15.8% +28.3%
分位超额 s3_max241 [train] Q1..Q10: -14.3% -9.3% -9.5% -4.7% +0.1% +1.6% +6.8% +7.7% +10.9% +10.6%
分位超额 s3_max241 [valid] Q1..Q10: -17.0% -12.2% -9.2% -4.6% -1.0% +2.3% +3.2% +6.4% +9.9% +22.3%
分位超额 s3_max20 [train] Q1..Q10: -32.8% -19.3% -9.0% -1.0% +1.6% +5.7% +10.1% +11.4% +15.4% +18.0%
分位超额 s3_max20 [valid] Q1..Q10: -42.7% -21.4% -10.9% -4.6% +1.1% +5.3% +10.4% +13.5% +21.9% +27.5%
分位超额 s3_max60 [train] Q1..Q10: -21.2% -16.7% -8.8% -4.9% +1.4% +5.0% +6.6% +9.1% +12.7% +16.7%
分位超额 s3_max60 [valid] Q1..Q10: -29.3% -20.2% -10.7% -6.7% +2.3% +2.6% +9.1% +11.3% +16.6% +25.1%
分位超额 s3_max120 [train] Q1..Q10: -15.7% -14.4% -9.0% -5.2% +0.7% +3.6% +5.7% +9.6% +10.9% +13.9%
分位超额 s3_max120 [valid] Q1..Q10: -23.4% -17.3% -10.3% -4.9% -2.3% +3.3% +5.4% +10.8% +15.4% +23.5%
分位超额 s3_mean60 [train] Q1..Q10: -17.7% -12.4% -5.5% -2.7% -2.0% +1.9% +5.0% +9.1% +9.9% +14.3%
分位超额 s3_mean60 [valid] Q1..Q10: -29.7% -18.9% -13.8% -5.6% -0.9% +2.8% +7.9% +13.2% +18.7% +26.3%

中性化 s1_relchg(fit 段;对象是**实际交易的信号** = 方向 x 面板、按半衰期平滑;残差不再平滑):
  (LSgross = 无成本多空夏普:残差没有再平滑、换手更高,扣费夏普塌掉可能只是成本;alpha 还在不在看 rIC 和 LSgross)
  (未中性化)         R2   —    rIC +0.0250  LSgross +4.10  LS +2.96  Lgross +9.5%  short +28.5%  TO 7.0%
  all_controls   R2 0.145  残差 rIC +0.0084  LSgross +1.45  LS -1.83  Lgross +5.4%  short +4.0%  TO 13.8%  (原始日频面板上的 R2 只有 0.146)
  ctl_amt        R2 0.035  残差 rIC +0.0189  LSgross +3.41  LS +1.31  Lgross +6.3%  short +18.3%  TO 10.0%
  ctl_price      R2 0.010  残差 rIC +0.0241  LSgross +4.33  LS +3.08  Lgross +9.0%  short +27.7%  TO 7.0%
  ctl_ivol       R2 0.029  残差 rIC +0.0192  LSgross +4.68  LS +1.26  Lgross +10.0%  short +22.1%  TO 15.5%
  ctl_range      R2 0.033  残差 rIC +0.0192  LSgross +5.08  LS +0.45  Lgross +10.8%  short +24.7%  TO 21.4%
  ctl_rev1       R2 0.006  残差 rIC +0.0256  LSgross +4.59  LS +2.27  Lgross +11.2%  short +29.8%  TO 13.7%
  ctl_mom20      R2 0.033  残差 rIC +0.0191  LSgross +3.60  LS +1.47  Lgross +9.2%  short +16.5%  TO 9.9%
  ctl_dvol20     R2 0.101  残差 rIC +0.0129  LSgross +2.35  LS +0.68  Lgross +7.5%  short +11.0%  TO 8.7%
  ctl_cap        R2 0.023  残差 rIC +0.0244  LSgross +4.67  LS +3.39  Lgross +10.4%  short +28.4%  TO 7.1%
  ctl_turnrate   R2 0.061  残差 rIC +0.0161  LSgross +2.99  LS +0.40  Lgross +9.1%  short +12.8%  TO 12.5%

中性化 s2_mid_mean(fit 段;对象是**实际交易的信号** = 方向 x 面板、按半衰期平滑;残差不再平滑):
  (LSgross = 无成本多空夏普:残差没有再平滑、换手更高,扣费夏普塌掉可能只是成本;alpha 还在不在看 rIC 和 LSgross)
  (未中性化)         R2   —    rIC +0.0363  LSgross +2.83  LS +2.21  Lgross +13.7%  short +25.4%  TO 5.7%
  all_controls   R2 0.578  残差 rIC +0.0093  LSgross +1.07  LS -5.55  Lgross +5.3%  short +1.4%  TO 26.5%  (原始日频面板上的 R2 只有 0.549)
  ctl_amt        R2 0.498  残差 rIC +0.0126  LSgross +1.36  LS -3.68  Lgross +6.0%  short +5.5%  TO 28.1%
  ctl_price      R2 0.090  残差 rIC +0.0357  LSgross +3.54  LS +2.67  Lgross +10.6%  short +26.9%  TO 6.1%
  ctl_ivol       R2 0.036  残差 rIC +0.0296  LSgross +2.93  LS +0.78  Lgross +13.8%  short +19.1%  TO 16.0%
  ctl_range      R2 0.080  残差 rIC +0.0274  LSgross +3.64  LS -1.13  Lgross +14.9%  short +22.1%  TO 32.1%
  ctl_rev1       R2 0.012  残差 rIC +0.0382  LSgross +3.41  LS +1.36  Lgross +16.4%  short +29.0%  TO 18.0%
  ctl_mom20      R2 0.025  残差 rIC +0.0329  LSgross +2.89  LS +1.79  Lgross +14.9%  short +19.3%  TO 8.4%
  ctl_dvol20     R2 0.213  残差 rIC +0.0182  LSgross +2.32  LS +0.79  Lgross +14.1%  short +8.0%  TO 9.6%
  ctl_cap        R2 0.108  残差 rIC +0.0381  LSgross +2.67  LS +2.04  Lgross +8.6%  short +30.0%  TO 6.0%
  ctl_turnrate   R2 0.196  残差 rIC +0.0199  LSgross +2.20  LS -0.32  Lgross +15.5%  short +9.3%  TO 18.9%

中性化 s3_max60(fit 段;对象是**实际交易的信号** = 方向 x 面板、按半衰期平滑;残差不再平滑):
  (LSgross = 无成本多空夏普:残差没有再平滑、换手更高,扣费夏普塌掉可能只是成本;alpha 还在不在看 rIC 和 LSgross)
  (未中性化)         R2   —    rIC +0.0350  LSgross +2.39  LS +2.14  Lgross +15.9%  short +21.0%  TO 2.6%
  all_controls   R2 0.639  残差 rIC +0.0075  LSgross +1.12  LS -5.48  Lgross +9.1%  short -2.4%  TO 25.9%  (原始日频面板上的 R2 只有 0.639)
  ctl_amt        R2 0.553  残差 rIC +0.0078  LSgross +0.91  LS -3.53  Lgross +9.2%  short -0.5%  TO 28.4%
  ctl_price      R2 0.094  残差 rIC +0.0346  LSgross +2.82  LS +2.43  Lgross +12.6%  short +21.9%  TO 3.2%
  ctl_ivol       R2 0.045  残差 rIC +0.0276  LSgross +2.54  LS +0.52  Lgross +17.3%  short +13.9%  TO 16.4%
  ctl_range      R2 0.090  残差 rIC +0.0252  LSgross +3.33  LS -1.18  Lgross +19.2%  short +17.7%  TO 33.1%
  ctl_rev1       R2 0.014  残差 rIC +0.0367  LSgross +2.95  LS +0.99  Lgross +18.0%  short +25.1%  TO 18.9%
  ctl_mom20      R2 0.018  残差 rIC +0.0333  LSgross +2.71  LS +1.92  Lgross +17.3%  short +19.1%  TO 6.9%
  ctl_dvol20     R2 0.235  残差 rIC +0.0155  LSgross +2.09  LS +0.88  Lgross +15.8%  short +5.1%  TO 8.0%
  ctl_cap        R2 0.161  残差 rIC +0.0379  LSgross +2.42  LS +2.12  Lgross +7.8%  short +31.1%  TO 3.3%
  ctl_turnrate   R2 0.181  残差 rIC +0.0186  LSgross +2.16  LS -0.04  Lgross +19.4%  short +6.0%  TO 17.1%
条件 IC s1_relchg|ctl_amt: Q1 -0.0098  Q2 -0.0117  Q3 -0.0141  Q4 -0.0215  Q5 -0.0408
条件 IC s1_relchg|g_level: Q1 -0.0167  Q2 -0.0241  Q3 -0.0279  Q4 -0.0321  Q5 -0.0270
条件 IC s1_relchg|known_stdamt_max9: Q1 -0.0074  Q2 -0.0064  Q3 -0.0092  Q4 -0.0156  Q5 -0.0437
衰减 s1_relchg rank IC: h1 +0.0259  h2 +0.0328  h3 +0.0364  h5 +0.0414  h10 +0.0461  h20 +0.0537
衰减 s3_max60 rank IC: h1 +0.0350  h2 +0.0461  h3 +0.0528  h5 +0.0622  h10 +0.0766  h20 +0.0931
```

**10-03 23:22 · Bash** — Digest of S4_longleg run

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh digest F105_std_fangzheng_covamt S4_longleg 2>&1 | head -150
```

```
===== F105_std_fangzheng_covamt  [S4_longleg.json]  1942d x 5220s  splits ['train', 'valid', 'utrain']  fit=train  169.8s  peak anon 3.61G =====

variant              sgn   rIC tr   rIC va  hl  LS tr  LS va Lgross tr Lgross va  Lnet tr  Lnet va  Lshr    TO   cov  dist
s4_max15               -  +0.0466  +0.0654   0  +2.61  +4.52    +18.0%    +26.1%   +12.3%   +21.3%   34%  6.2%  1.00  1.00
s4_max30               -  +0.0411  +0.0585   0  +2.37  +4.12    +17.4%    +25.3%   +13.6%   +22.2%   39%  4.0%  1.00  1.00
s4_mean20              -  +0.0377  +0.0608   0  +1.93  +4.00    +15.2%    +24.8%   +11.9%   +22.0%   39%  3.7%  1.00  1.00
s4_med60               -  +0.0209  +0.0416   2  +1.11  +3.02     +7.0%    +19.5%    +5.8%   +18.5%   35%  1.5%  1.00  1.00
s4_summax30            -  +0.0354  +0.0575   0  +1.54  +3.63    +13.5%    +25.0%   +10.1%   +22.2%   44%  3.5%  1.00  1.00
s4_pos                 -  +0.0341  +0.0528   1  +2.02  +3.20    +11.9%    +19.7%    +4.6%   +12.8%   26% 11.8%  1.00  0.97
  (LS = 扣费多空夏普; Lgross/Lnet = 多头腿毛/净年化超额; Lshr = 多头腿占毛价差的比例; cov = 有标签格子里有值的比例,用户门槛 0.95; dist = 取值离散度,用户门槛 0.5)

固定半衰期下的 train 表现(各变体自己选的半衰期不同,先看这张再比结构):
variant                hl5 LS    Lnet    TO  hl10 LS    Lnet    TO  hl20 LS    Lnet    TO
s4_max15                +2.13  +13.5%    4%    +1.89  +12.4%    3%    +1.71  +11.1%    2%
s4_max30                +1.96  +13.3%    3%    +1.70  +11.6%    2%    +1.52  +10.1%    2%
s4_mean20               +1.64  +10.7%    2%    +1.56  +10.7%    2%    +1.39   +9.2%    1%
s4_med60                +1.04   +6.0%    1%    +1.05   +5.6%    1%    +0.96   +5.6%    1%
s4_summax30             +1.31  +10.0%    2%    +1.20   +9.4%    2%    +1.03   +7.5%    1%
s4_pos                  +1.97   +7.5%    7%    +1.91   +8.0%    5%    +1.79   +7.3%    3%
分位超额 s4_max15 [train] Q1..Q10: -35.3% -18.7% -6.7% -3.9% +2.3% +7.0% +9.3% +12.5% +14.9% +18.7%
分位超额 s4_max15 [valid] Q1..Q10: -45.7% -20.9% -11.3% -3.1% +1.5% +4.2% +10.4% +15.8% +20.7% +28.5%
分位超额 s4_max30 [train] Q1..Q10: -27.5% -19.4% -9.6% -1.3% +1.7% +3.9% +8.1% +11.1% +15.0% +18.2%
分位超额 s4_max30 [valid] Q1..Q10: -36.6% -22.4% -13.5% -4.5% +1.1% +7.1% +7.6% +14.2% +19.6% +27.4%
分位超额 s4_mean20 [train] Q1..Q10: -24.0% -15.9% -7.6% -2.7% +1.9% +3.6% +6.5% +10.2% +12.2% +15.8%
分位超额 s4_mean20 [valid] Q1..Q10: -40.0% -23.0% -11.7% -7.6% +2.9% +4.8% +11.2% +13.2% +22.6% +27.5%
分位超额 s4_med60 [train] Q1..Q10: -13.1% -7.1% -3.6% -0.9% +1.0% +1.3% +2.7% +4.7% +7.5% +7.5%
分位超额 s4_med60 [valid] Q1..Q10: -27.4% -14.3% -11.6% -5.0% -1.3% +2.8% +6.6% +12.4% +16.4% +21.4%
分位超额 s4_summax30 [train] Q1..Q10: -17.7% -17.4% -8.6% -4.6% +1.2% +4.6% +5.4% +9.4% +13.6% +14.1%
分位超额 s4_summax30 [valid] Q1..Q10: -31.4% -24.5% -15.4% -6.8% +1.4% +4.7% +11.5% +13.2% +20.1% +27.4%
分位超额 s4_pos [train] Q1..Q10: -35.0% -3.3% -0.6% +0.6% +0.9% +3.5% +4.3% +8.1% +9.4% +12.3%
分位超额 s4_pos [valid] Q1..Q10: -39.7% -12.2% -4.8% -3.6% +3.8% +5.4% +6.9% +9.6% +14.6% +19.9%

中性化 s4_max30(fit 段;对象是**实际交易的信号** = 方向 x 面板、按半衰期平滑;残差不再平滑):
  (LSgross = 无成本多空夏普:残差没有再平滑、换手更高,扣费夏普塌掉可能只是成本;alpha 还在不在看 rIC 和 LSgross)
  (未中性化)         R2   —    rIC +0.0411  LSgross +2.74  LS +2.37  Lgross +17.4%  short +27.0%  TO 4.0%
  all_controls   R2 0.740  残差 rIC +0.0116  LSgross +2.70  LS -5.26  Lgross +10.8%  short +4.6%  TO 29.3%  (原始日频面板上的 R2 只有 0.740)
  ctl_amt        R2 0.643  残差 rIC +0.0161  LSgross +2.17  LS -3.92  Lgross +11.1%  short +6.7%  TO 33.0%
  ctl_price      R2 0.114  残差 rIC +0.0410  LSgross +3.58  LS +3.02  Lgross +13.4%  short +31.2%  TO 4.6%
  ctl_ivol       R2 0.065  残差 rIC +0.0325  LSgross +3.06  LS +0.63  Lgross +19.9%  short +17.5%  TO 19.6%
  ctl_range      R2 0.118  残差 rIC +0.0302  LSgross +3.85  LS -1.10  Lgross +20.8%  short +22.6%  TO 36.9%
  ctl_rev1       R2 0.015  残差 rIC +0.0427  LSgross +3.34  LS +1.38  Lgross +19.9%  short +31.0%  TO 19.8%
  ctl_mom20      R2 0.030  残差 rIC +0.0375  LSgross +3.02  LS +2.03  Lgross +18.6%  short +22.1%  TO 8.6%
  ctl_dvol20     R2 0.317  残差 rIC +0.0198  LSgross +2.49  LS +1.16  Lgross +19.0%  short +8.5%  TO 9.7%
  ctl_cap        R2 0.195  残差 rIC +0.0454  LSgross +2.98  LS +2.56  Lgross +8.4%  short +41.6%  TO 4.7%
  ctl_turnrate   R2 0.197  残差 rIC +0.0249  LSgross +2.47  LS +0.31  Lgross +23.3%  short +7.6%  TO 17.9%

中性化 s4_pos(fit 段;对象是**实际交易的信号** = 方向 x 面板、按半衰期平滑;残差不再平滑):
  (LSgross = 无成本多空夏普:残差没有再平滑、换手更高,扣费夏普塌掉可能只是成本;alpha 还在不在看 rIC 和 LSgross)
  (未中性化)         R2   —    rIC +0.0321  LSgross +3.28  LS +2.02  Lgross +11.9%  short +34.6%  TO 11.8%
  all_controls   R2 0.338  残差 rIC +0.0096  LSgross +1.88  LS -3.88  Lgross +4.7%  short +6.0%  TO 21.4%  (原始日频面板上的 R2 只有 0.341)
  ctl_amt        R2 0.202  残差 rIC +0.0165  LSgross +1.63  LS -1.52  Lgross +5.2%  short +9.5%  TO 18.8%
  ctl_price      R2 0.056  残差 rIC +0.0307  LSgross +3.67  LS +2.10  Lgross +9.3%  short +32.3%  TO 11.7%
  ctl_ivol       R2 0.089  残差 rIC +0.0212  LSgross +3.22  LS -0.58  Lgross +14.3%  short +18.0%  TO 25.1%
  ctl_range      R2 0.094  残差 rIC +0.0209  LSgross +3.35  LS -1.72  Lgross +13.5%  short +21.1%  TO 34.7%
  ctl_rev1       R2 0.010  残差 rIC +0.0313  LSgross +3.35  LS +1.09  Lgross +11.6%  short +32.9%  TO 19.9%
  ctl_mom20      R2 0.146  残差 rIC +0.0206  LSgross +1.59  LS -1.48  Lgross +8.9%  short +5.4%  TO 17.9%
  ctl_dvol20     R2 0.094  残差 rIC +0.0193  LSgross +2.19  LS +0.46  Lgross +10.7%  short +14.4%  TO 13.1%
  ctl_cap        R2 0.104  残差 rIC +0.0326  LSgross +3.54  LS +2.10  Lgross +6.7%  short +36.0%  TO 11.5%
  ctl_turnrate   R2 0.043  残差 rIC +0.0244  LSgross +2.82  LS +0.86  Lgross +12.3%  short +21.5%  TO 15.5%
条件 IC s4_max30|ctl_cap: Q1 -0.0659  Q2 -0.0566  Q3 -0.0540  Q4 -0.0429  Q5 -0.0185
条件 IC s4_max30|ctl_turnrate: Q1 -0.0195  Q2 -0.0230  Q3 -0.0205  Q4 -0.0257  Q5 -0.0393
条件 IC s4_pos|ctl_amt: Q1 -0.0142  Q2 -0.0139  Q3 -0.0156  Q4 -0.0203  Q5 -0.0365
衰减 s4_max30 rank IC: h1 +0.0411  h2 +0.0537  h3 +0.0610  h5 +0.0710  h10 +0.0859  h20 +0.1009
```

**10-03 23:22 · Bash** — Digest of final run

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh digest F105_std_fangzheng_covamt final f_orig 2>&1 | head -150
```

```
===== F105_std_fangzheng_covamt  [final.json]  1942d x 5220s  splits ['train', 'valid', 'utrain', 'holdout', 'full']  fit=train  165.2s  peak anon 2.56G =====

variant              sgn   rIC tr   rIC va  hl  LS tr  LS va Lgross tr Lgross va  Lnet tr  Lnet va  Lshr    TO   cov  dist
f_orig                 -  +0.0387  +0.0521   3  +2.54  +4.62    +13.1%    +26.0%    +8.2%   +20.7%   31%  6.0%  1.00  1.00
f_min3                 -  +0.0392  +0.0522   3  +2.84  +4.80    +14.3%    +25.5%    +9.9%   +20.9%   30%  5.9%  1.00  1.00
f_max15                -  +0.0466  +0.0654   0  +2.61  +4.52    +18.0%    +26.1%   +12.3%   +21.3%   34%  6.2%  1.00  1.00
f_max30                -  +0.0411  +0.0585   0  +2.37  +4.12    +17.4%    +25.3%   +13.6%   +22.2%   39%  4.0%  1.00  1.00
f_max60                -  +0.0350  +0.0476   0  +2.14  +3.64    +15.9%    +22.3%   +13.5%   +20.4%   43%  2.6%  1.00  1.00
  (LS = 扣费多空夏普; Lgross/Lnet = 多头腿毛/净年化超额; Lshr = 多头腿占毛价差的比例; cov = 有标签格子里有值的比例,用户门槛 0.95; dist = 取值离散度,用户门槛 0.5)

固定半衰期下的 train 表现(各变体自己选的半衰期不同,先看这张再比结构):
variant                hl5 LS    Lnet    TO  hl10 LS    Lnet    TO  hl20 LS    Lnet    TO
f_orig                  +2.43   +8.7%    5%    +2.32   +9.3%    3%    +1.96   +7.7%    2%
f_min3                  +2.78  +10.2%    5%    +2.62  +11.1%    3%    +2.26   +9.6%    2%
f_max15                 +2.13  +13.5%    4%    +1.89  +12.4%    3%    +1.71  +11.1%    2%
f_max30                 +1.96  +13.3%    3%    +1.70  +11.6%    2%    +1.52  +10.1%    2%
f_max60                 +1.73  +11.9%    2%    +1.51  +10.5%    2%    +1.40   +9.2%    1%

与用户表同口径(方向/半衰期在 utrain 上定; holdout = 用户的测试段):
variant              sgn  hl  LS utr   LS ho Lgross utr Lgross ho  Lnet utr  Lnet ho Lsharpe utr Lsharpe ho short utr
f_orig                 -   3   +3.03   +2.24     +16.8%    +14.3%    +11.8%    +8.9%       +1.96      +1.04    +31.1%
f_min3                 -   3   +3.30   +2.72     +17.5%    +16.3%    +13.0%   +11.5%       +2.18      +1.33    +33.9%
f_max15                -   0   +3.08   +2.70     +20.3%    +17.0%    +14.9%   +12.0%       +2.26      +1.28    +37.9%
f_max30                -   0   +2.80   +2.39     +19.6%    +15.7%    +16.1%   +12.5%       +2.46      +1.37    +29.7%
f_max60                -   0   +2.52   +2.39     +17.7%    +16.6%    +15.5%   +14.7%       +2.34      +1.74    +23.2%

半衰期扫描 f_orig(fit 段; LS = 扣费多空夏普, Lshp = 纯多头夏普): hl0: LS +1.83 Lshp -0.09 TO 13%  hl1: LS +2.28 Lshp +0.83 TO 10%  hl2: LS +2.51 Lshp +1.29 TO 7%  hl3: LS +2.54 Lshp +1.32 TO 6%  hl5: LS +2.43 Lshp +1.40 TO 5%  hl10: LS +2.32 Lshp +1.49 TO 3%  hl20: LS +1.96 Lshp +1.22 TO 2%

与 f_orig 的日截面 rank 相关(fit 段; |.|>=0.95 = 同一因子族): ref_orig +1.00  f_min3 +0.94  known_stdamt_max9 +0.68  known_amt_max9 +0.68  f_max15 +0.66  ctl_amt +0.65  f_max30 +0.64  f_max60 +0.63  ctl_turnrate +0.44  ctl_dvol20 +0.41  ctl_cap +0.26  ctl_price +0.26  known_ivol_max9 +0.24  ctl_ivol +0.21  ctl_mom20 +0.14  ctl_rev1 -0.02

逐年 f_orig: 2018 LS +3.44 Lg +17.3%  2019 LS +2.60 Lg +11.8%  2020 LS +1.50 Lg +8.6%  2021 LS +2.74 Lg +14.9%  2022 LS +5.91 Lg +31.2%  2023 LS +4.00 Lg +21.2%  2024 LS +1.66 Lg +10.2%  2025 LS +1.99 Lg +13.2%

逐年 f_min3: 2018 LS +3.56 Lg +17.0%  2019 LS +3.10 Lg +13.7%  2020 LS +1.92 Lg +10.1%  2021 LS +2.93 Lg +16.6%  2022 LS +6.06 Lg +30.7%  2023 LS +4.42 Lg +21.9%  2024 LS +2.12 Lg +12.0%  2025 LS +2.40 Lg +15.4%

逐年 f_max15: 2018 LS +4.25 Lg +28.5%  2019 LS +3.27 Lg +19.2%  2020 LS +1.43 Lg +8.7%  2021 LS +2.17 Lg +15.5%  2022 LS +5.50 Lg +28.7%  2023 LS +3.95 Lg +23.6%  2024 LS +2.52 Lg +13.6%  2025 LS +2.18 Lg +16.5%

逐年 f_max30: 2018 LS +3.67 Lg +23.6%  2019 LS +2.87 Lg +16.2%  2020 LS +1.19 Lg +11.4%  2021 LS +2.20 Lg +18.3%  2022 LS +4.94 Lg +28.3%  2023 LS +3.84 Lg +22.3%  2024 LS +2.24 Lg +12.4%  2025 LS +1.72 Lg +15.1%

逐年 f_max60: 2018 LS +3.29 Lg +21.3%  2019 LS +1.99 Lg +13.5%  2020 LS +1.17 Lg +9.2%  2021 LS +2.29 Lg +19.6%  2022 LS +4.32 Lg +25.1%  2023 LS +3.59 Lg +21.5%  2024 LS +2.26 Lg +13.7%  2025 LS +1.69 Lg +15.1%
```

**10-03 23:24 · Bash** — Read longleg.py analysis script

```bash
cd /Users/wxy/Desktop/Partura && cat studies/F105_std_fangzheng_covamt/longleg.py
```

```
"""F105: why the slow members of the known family have a better long leg than the original,
and whether that survives the checks a long-only user cares about.

S3/S4 found that cross_max(day_std(Amt), d) for d = 15..60 has a long-leg net excess of 12-14% (train)
against the original's 8%, and that valid is a tie.  Before the holdout is read, four questions that no
stage table answers (train / valid only, never the holdout):

  1  subsumption   does the original add anything to cross_max(day_std(Amt), 30), or the reverse?
  2  long decile   how much do the two long deciles overlap, and what do the names only one of them holds earn?
  3  by year       is the long-leg advantage there year by year (2018..2023), or is it one year?
  4  capacity      does the advantage survive dropping the smallest 20% by float cap / by amount from the universe?
"""
import time

import numpy as np

from partura.study_tools import Study, bk, dg

FID = "F105_std_fangzheng_covamt"
EXPR = {
    "orig":   "ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5)",
    "min3":   "cross_stddev(cross_stddev(day_cov(Amt, Amt), 241), 5)",
    "max15":  "cross_max(day_std(Amt), 15)",
    "max30":  "cross_max(day_std(Amt), 30)",
    "max60":  "cross_max(day_std(Amt), 60)",
    "known9": "cross_max(day_std(Amt), 9)",
}
HL = {"orig": 3.0, "min3": 3.0, "max15": 0.0, "max30": 0.0, "max60": 0.0, "known9": 0.0}   # fitted on train (stage tables)
T0 = time.time()

… (106 行略) …
        sl = slice(int(idx[0]), int(idx[-1]) + 1)
        row = []
        for k in ("orig", "min3", "max15", "max30", "max60"):
            b = bk.book_row(sig[k], tgt, sl)
            row.append(f"{k} LS {b['ls_sharpe']:+.2f} Lnet {b['long_ann']:+.1%} Lshp {b['long_sharpe']:+.2f}")
        say(f"  {y} ({idx.size}d)  " + "  |  ".join(row))

    # ------------------------------------------------------------------ 4 capacity
    say("\n== 4 capacity: drop the smallest names from the universe, then rebuild both books ==")
    say("   (the universe changes day by day, so turnover and net are inflated the same way for every factor; compare within a row block)")
    masks = {"all names": np.ones_like(cap_p, dtype=bool),
             "cap pctile >= 0.2": cap_p >= 0.2,
             "cap pctile >= 0.5": cap_p >= 0.5,
             "amt pctile >= 0.2": amt_p >= 0.2}
    for mname, m in masks.items():
        for name, sl in (("train", tr), ("valid", va)):
            for k in ("orig", "max15", "max30", "max60"):
                b = bk.book_row(np.where(m, sig[k], np.nan), tgt, sl)
                say(f"  [{mname:<18}] [{name}] {k:<6} {fmt(b)}")
    say(f"\ndone {time.time() - T0:.0f}s")
```

**10-03 23:24 · Bash** — Read events.py analysis script

```bash
cd /Users/wxy/Desktop/Partura && cat studies/F105_std_fangzheng_covamt/events.py
```

```
"""F105: what orders the root, and which kind of stock-day earns the money.

The root is  D = ts_stddev(C, 5),  C = cross_fangzheng(B, 241),  B = cross_max(A, 3),  A = day_cov(Amt, Amt).
The probes say D is "how much a one-year level statistic moved in the last 5 days", that it cannot tell a
spike ENTERING the window from the same spike LEAVING it 241 days later, and that an unfilled window
(a stock with < 241 observations) mechanically inflates the move.  No stock diagnostic separates those,
so this script measures them directly on train / valid (never the holdout):

  1  tails        how heavy-tailed is A through time, and how much of C is the std term / the single largest day
  2  ordering     what the cross-sectional order of D follows: level C, relative change D/C, amount, known family
  3  anatomy      the short and the long decile split by event kind: entry / exit(echo) / IPO-young / sample-start
  4  ic by kind   rank IC of -D inside each kind
  5  drop-one     the book at hl=3 with one kind of stock-day removed from the universe
  6  subsumption  the traded signal neutralised on the known family (and the reverse)
  7  long leg     overlap of the long decile with the lowest decile of amount / known family / level C
  8  two-way      conditional IC: relative change inside level buckets, level inside relative-change buckets
"""
import time

import numpy as np

from partura.study_tools import Study, bk, dg

FID = "F105_std_fangzheng_covamt"
A = "day_cov(Amt, Amt)"
B = f"cross_max({A}, 3)"
C = f"cross_fangzheng({B}, 241)"
D = f"ts_stddev({C}, 5)"
HL = 3.0
T0 = time.time()
… (181 行略) …
            qx, _ = deciles(-np.where(ok, np.asarray(x[sl], dtype=np.float64), np.nan), tgt[sl])
            row.append(f"{k} lowest-decile overlap {(lng & (qx == 9)).sum() / max(lng.sum(), 1):.1%}")
        say(f"  [{name}] " + "   ".join(row))
        with np.errstate(invalid="ignore"):
            say(f"  [{name}] mean percentile inside the long decile: amt {np.nanmean(np.where(lng, amt_pct[sl], np.nan)):.3f}"
                f"  cap {np.nanmean(np.where(lng, pct(cap)[sl], np.nan)):.3f}  turnrate {np.nanmean(np.where(lng, pct(turn)[sl], np.nan)):.3f}"
                f"  level C {np.nanmean(np.where(lng, pct(c)[sl], np.nan)):.3f}  rel change {np.nanmean(np.where(lng, pct(rel)[sl], np.nan)):.3f}"
                f"  ipo-young share {(lng & groups_raw['ipo-young'][sl]).sum() / max(lng.sum(), 1):.1%}")

    # ------------------------------------------------------------------ 8 two-way
    say("\n== 8 conditional rank IC (train, raw panels; sign as measured) ==")
    for name, x, g in (("relative change | level C", rel, c), ("level C | relative change", c, rel),
                       ("D | known_stdamt_max9", d, known), ("known_stdamt_max9 | D", known, d),
                       ("relative change | ctl_amt", rel, amt)):
        rows = dg.conditional_ic(x[tr], tgt[tr], np.asarray(g[tr], dtype=np.float64), buckets=5)
        say(f"  {name:<28} " + "  ".join(f"Q{r['bucket'] + 1} {r['rank_ic']:+.4f}" for r in rows))
    for name, x in (("level C", c), ("relative change D/C", rel), ("D", d), ("known_stdamt_max9", known)):
        say(f"  unconditional {name:<22} train {np.nanmean(dg.rank_ic_series(x[tr], tgt[tr])):+.4f}"
            f"   valid {np.nanmean(dg.rank_ic_series(x[va], tgt[va])):+.4f}")
    say(f"\ndone {time.time() - T0:.0f}s")
```

**10-03 23:24 · Bash** — Print kernel source of key operators from server

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh src day_cov day_std cross_fangzheng cross_max ts_stddev cross_stddev 2>&1 | head -300
```

```
### day_cov  face=dt family=day category=binary axis=M reduces_m=True lookahead=False kernel=dt_day.day_cov
# /root/autodl-tmp/AlphaCube/src/alphacube/operators/dt_day.py:212
@op("dt", "day", arity=2, pair=True)
def day_cov(x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
    valid = ~(torch.isnan(x) | torch.isnan(y))
    count = valid.sum(dim=-1, keepdim=True).to(x.dtype)
    count_safe = count.clamp(min=1)
    x0 = torch.where(valid, x, torch.zeros_like(x))
    y0 = torch.where(valid, y, torch.zeros_like(y))
    mean_x = x0.sum(dim=-1, keepdim=True) / count_safe
    mean_y = y0.sum(dim=-1, keepdim=True) / count_safe
    dx = torch.where(valid, x - mean_x, torch.zeros_like(x))
    dy = torch.where(valid, y - mean_y, torch.zeros_like(y))
    cov = (dx * dy).sum(dim=-1, keepdim=True) / count_safe
    return torch.where(count >= 2, cov, torch.full_like(cov, float("nan")))

### day_std  face=dt family=day category=unary axis=M reduces_m=True lookahead=False kernel=dt_day.day_std
# /root/autodl-tmp/AlphaCube/src/alphacube/operators/dt_day.py:108
@op("dt", "day", arity=1)
def day_std(x: torch.Tensor) -> torch.Tensor:
    return C._stddev(x).unsqueeze(-1)

### cross_fangzheng  face=dt family=cross category=rolling axis=D reduces_m=False lookahead=False kernel=dt_cross.cross_fangzheng
# /root/autodl-tmp/AlphaCube/src/alphacube/operators/dt_cross.py:498
@op("dt", "cross", arity=1, requires_window=True)
def cross_fangzheng(x: torch.Tensor, d: int) -> torch.Tensor:
    return cross_mean(x, d) + cross_stddev(x, d)

### cross_max  face=dt family=cross category=rolling axis=D reduces_m=False lookahead=False kernel=dt_cross.cross_max
# /root/autodl-tmp/AlphaCube/src/alphacube/operators/dt_cross.py:232
@op("dt", "cross", arity=1, requires_window=True)
def cross_max(x: torch.Tensor, d: int) -> torch.Tensor:
    return rolling_reduce(x, int(d), nanmax_last, axis=0)

### ts_stddev  face=nd family=ts category=rolling axis=D reduces_m=False lookahead=False kernel=nd_ts.ts_stddev
# /root/autodl-tmp/AlphaCube/src/alphacube/operators/nd_ts.py:156
@op("nd", "ts", arity=1, requires_window=True)
def ts_stddev(x: torch.Tensor, d: int) -> torch.Tensor:
    """Alias of `ts_std` — `ts_stddev` was the original file's name."""
    return ts_std(x, d)

### cross_stddev  face=dt family=cross category=rolling axis=D reduces_m=False lookahead=False kernel=dt_cross.cross_stddev
# /root/autodl-tmp/AlphaCube/src/alphacube/operators/dt_cross.py:289
@op("dt", "cross", arity=1, requires_window=True)
def cross_stddev(x: torch.Tensor, d: int) -> torch.Tensor:
    return rolling_reduce(x, int(d), nanstd_last, axis=0)
```

**10-03 23:25 · Bash** — Print more operator sources and look at remote_tools

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh src ts_std cross_mean cross_delta cross_decay_linear cross_med ts_delta 2>&1 | head -200; grep -n "def src\|def ops\|helper\|getsource" partura/remote_tools.py | head -30
```

```
### ts_std  face=nd family=ts category=rolling axis=D reduces_m=False lookahead=False kernel=nd_ts.ts_std
# /root/autodl-tmp/AlphaCube/src/alphacube/operators/nd_ts.py:151
@op("nd", "ts", arity=1, requires_window=True)
def ts_std(x: torch.Tensor, d: int) -> torch.Tensor:
    return rolling_reduce(x, d, nanstd_last, axis=0)

### cross_mean  face=dt family=cross category=rolling axis=D reduces_m=False lookahead=False kernel=dt_cross.cross_mean
# /root/autodl-tmp/AlphaCube/src/alphacube/operators/dt_cross.py:222
@op("dt", "cross", arity=1, requires_window=True)
def cross_mean(x: torch.Tensor, d: int) -> torch.Tensor:
    return rolling_reduce(x, int(d), nanmean_last, axis=0)

### cross_delta  face=dt family=cross category=rolling axis=D reduces_m=False lookahead=False kernel=dt_cross.cross_delta
# /root/autodl-tmp/AlphaCube/src/alphacube/operators/dt_cross.py:173
@op("dt", "cross", arity=1, requires_window=True)
def cross_delta(x: torch.Tensor, d: int) -> torch.Tensor:
    """`x[t] - x[t-d]` along the day axis."""
    d = int(d)
    res = get_nan_tensor(x.shape, x.device, x.dtype)
    if 0 < d < x.shape[0]:
        res[d:] = x[d:] - x[:-d]
    return res

### cross_decay_linear  face=dt family=cross category=rolling axis=D reduces_m=False lookahead=False kernel=dt_cross.cross_decay_linear
# /root/autodl-tmp/AlphaCube/src/alphacube/operators/dt_cross.py:284
@op("dt", "cross", arity=1, requires_window=True)
def cross_decay_linear(x: torch.Tensor, d: int) -> torch.Tensor:
    return rolling_reduce(x, int(d), decay_linear_last, axis=0)

### cross_med  face=dt family=cross category=rolling axis=D reduces_m=False lookahead=False kernel=dt_cross.cross_med
# /root/autodl-tmp/AlphaCube/src/alphacube/operators/dt_cross.py:237
@op("dt", "cross", arity=1, requires_window=True)
def cross_med(x: torch.Tensor, d: int) -> torch.Tensor:
    return rolling_reduce(x, int(d), nanmedian_last, axis=0)

### ts_delta  face=nd family=ts category=rolling axis=D reduces_m=False lookahead=False kernel=nd_ts.ts_delta
# /root/autodl-tmp/AlphaCube/src/alphacube/operators/nd_ts.py:132
@op("nd", "ts", arity=1, requires_window=True)
def ts_delta(x: torch.Tensor, d) -> torch.Tensor:
    return sub(x, ts_delay(x, d))

1:"""Small read-only helpers a study runs ON THE SERVER (through scripts/study.sh).
33:def ops(pattern: str = ".") -> int:
52:def src(names) -> int:
61:            f, (lines, line) = inspect.getsourcefile(fn), inspect.getsourcelines(fn)
```

**10-03 23:25 · Bash** — Read src helper implementation and find local AlphaCube

```bash
cd /Users/wxy/Desktop/Partura && sed -n 25,80p partura/remote_tools.py; ls ~/Desktop | head -50
```

```
def _catalogs():
    from alphacube.catalog import default_registry
    from alphacube.fullcatalog import default_full_catalog
    return default_registry(), default_full_catalog()


def ops(pattern: str = ".") -> int:
    reg, cat = _catalogs()
    pat = re.compile(pattern)
    print("# 搜索语法内的注册表算子(带 win 的需要窗口参数,写在最后一个位置):")
    for n, sp in sorted(reg._ops.items()):
        if not pat.search(n):
            continue
        flags = ",".join(k for k in ("lookahead", "boolean_output", "trivial_boolean", "resource_risk",
                                     "coarse_output") if getattr(sp, k))
        win = f" win {list(sp.windows)}" if sp.requires_window else ""
        print(f"  {n:<34} {sp.face}/{sp.family}/{sp.category:<12} arity {sp.arity} axis {sp.compute_axis}{win}"
              f"{'  [' + flags + ']' if flags else ''}")
    print("# 只在完整库里的通用调用(手写因子用的;参数含字面量,签名看 src):")
    for n, sp in sorted(cat.entries.items()):
        if pat.search(n) and n not in reg._ops:
            print(f"  {n:<34} {sp.face}/{sp.family}  axis {sp.compute_axis} reduces_m {sp.reduces_m}")
    return 0


def src(names) -> int:
    reg, cat = _catalogs()
    for name in names:
        spec = reg._ops.get(name) or cat.get(name)
        if spec is None:
… (54 行略) …
transform
viewdb
微信图片_20260409143436_240_124.jpg
截屏2026-07-26 12.20.50.png
截屏2026-07-26 14.34.54.png
截屏2026-07-26 21.42.04.png
截屏2026-07-26 21.54.09.png
截屏2026-07-28 19.36.08.png
截屏2026-07-29 11.16.57.png
截屏2026-08-05 23.14.32.png
截屏2026-08-07 14.40.44.png
截屏2026-08-08 09.06.01.png
截屏2026-08-14 12.02.09.png
截屏2026-08-17 18.09.49.png
截屏2026-08-18 23.43.11.png
截屏2026-08-19 16.30.25.png
截屏2026-08-24 12.36.48.png
截屏2026-08-24 16.57.44.png
截屏2026-08-25 13.58.45.png
截屏2026-08-25 17.51.18.png
```

**10-03 23:25 · Bash** — Locate helper kernels in local AlphaCube copy

```bash
cd /Users/wxy/Desktop/AlphaCube && grep -rn "def rolling_reduce\|def nanstd_last\|def nanmax_last\|def rolling_windows\|def nanmean_last\|def _stddev\|def decay_linear_last" src/alphacube | head -20
```

```
src/alphacube/operators/common.py:399:def _stddev(x: torch.Tensor) -> torch.Tensor:
src/alphacube/operators/common.py:426:def rolling_windows(x: torch.Tensor, d: int, axis: int = 0) -> torch.Tensor:
src/alphacube/operators/common.py:450:def nanmax_last(w: torch.Tensor) -> torch.Tensor:
src/alphacube/operators/common.py:545:def nanmean_last(w: torch.Tensor) -> torch.Tensor:
src/alphacube/operators/common.py:549:def nanstd_last(w: torch.Tensor) -> torch.Tensor:
src/alphacube/operators/common.py:595:def decay_linear_last(w: torch.Tensor) -> torch.Tensor:
src/alphacube/operators/common.py:610:def rolling_reduce(x: torch.Tensor, d: int, reducer, axis: int = 0) -> torch.Tensor:
```

**10-03 23:25 · Bash** — Read local helper kernel source

```bash
cd /Users/wxy/Desktop/AlphaCube && sed -n 385,470p src/alphacube/operators/common.py; sed -n 540,640p src/alphacube/operators/common.py
```

```
    value = x.nansum(dim=-1)
    return torch.where(
        torch.isfinite(x).any(dim=-1), value, torch.full_like(value, float("nan"))
    )


def _mean(x: torch.Tensor) -> torch.Tensor:
    return x.nanmean(dim=-1)


def _median(x: torch.Tensor) -> torch.Tensor:
    return x.nanmedian(dim=-1).values


def _stddev(x: torch.Tensor) -> torch.Tensor:
    x_demean = x - x.nanmean(dim=-1, keepdim=True)
    return torch.sqrt(torch.nanmean(torch.pow(x_demean, 2), dim=-1))


def _skew(x: torch.Tensor) -> torch.Tensor:
    x_demeaned = x - x.nanmean(dim=-1, keepdim=True)
    x_std = torch.sqrt(torch.nanmean(torch.pow(x_demeaned, 2), dim=-1, keepdim=True))
    zscore = torch.pow(div(x_demeaned, x_std), 3)
    return _mean(zscore)


def _kurt(x: torch.Tensor) -> torch.Tensor:
    x_demeaned = x - x.nanmean(dim=-1, keepdim=True)
    x_var = torch.nanmean(torch.pow(x_demeaned, 2), dim=-1, keepdim=True)
    x_4 = torch.pow(x_demeaned, 4)
… (137 行略) …
    count = valid.sum(dim=-1).clamp(min=1).to(x.dtype)
    x0 = torch.where(valid, wx, torch.zeros_like(wx))
    y0 = torch.where(valid, wy, torch.zeros_like(wy))
    mean_x = x0.sum(dim=-1) / count
    mean_y = y0.sum(dim=-1) / count
    dx = torch.where(valid, wx - mean_x.unsqueeze(-1), torch.zeros_like(wx))
    dy = torch.where(valid, wy - mean_y.unsqueeze(-1), torch.zeros_like(wy))
    cov = (dx * dy).sum(dim=-1) / count
    if kind == "cov":
        return cov
    var_x = (dx ** 2).sum(dim=-1) / count
    var_y = (dy ** 2).sum(dim=-1) / count
    return cov / (torch.sqrt(var_x * var_y) + EPS)


def rolling_ols(x: torch.Tensor, y: torch.Tensor, d: int, axis: int = 0) -> Dict[str, torch.Tensor]:
    """Shared rolling single-predictor OLS `y ~ alpha + beta*x`. One
    implementation replaces the old `ts_regbeta/regalpha/regres/
    reg_tvalue/reg_fvalue` AND `cross_reg*` AND the `in_reg*` transpose-
    wrappers around them — all five statistics computed in one pass.
```

**10-03 23:25 · Bash** — Read Partura study_tools API

```bash
cd /Users/wxy/Desktop/Partura && ls partura/ && wc -l partura/*.py && sed -n 1,200p partura/study_tools.py
```

```
__init__.py
__pycache__
books.py
bridge.py
cli.py
decompose.py
diagnose.py
guard.py
lab.py
panels.py
probes.py
propose.py
remote_tools.py
report.py
report_legacy.py
runner.py
semantics.py
splits.py
study_tools.py
      15 partura/__init__.py
     175 partura/books.py
     126 partura/bridge.py
     170 partura/cli.py
     211 partura/decompose.py
     366 partura/diagnose.py
     169 partura/guard.py
     111 partura/lab.py
     361 partura/panels.py
     319 partura/probes.py
     344 partura/propose.py
… (119 行略) …
        s = self.slice(split)
        p = np.asarray(panel[s], dtype=np.float64)
        return dg.ic_row(p, self.target()[s], sign=self.sign(panel) if sign is None else sign)

    def books(self, panel: np.ndarray, fit: str = "train", evals: Sequence[str] = ("train", "valid"),
              sign: Optional[float] = None) -> Dict[str, object]:
        """Decile L/S and the long leg, in the user's convention (see partura.books)."""
        sg = self.sign(panel, fit) if sign is None else sign
        return bk.books(sg * np.asarray(panel, dtype=np.float64), self.target(), self.slice(fit),
                        {e: self.slice(e) for e in evals},
                        cost=float(self.cfg.get("cost_per_side", bk.COST)),
                        top_frac=float(self.cfg.get("top_frac", bk.TOP_FRAC)),
                        rank_by=self.cfg.get("rank_by", "ls"))

    def rank_corr(self, a: np.ndarray, b: np.ndarray, split: str = "train") -> float:
        s = self.slice(split)
        return dg.pair_rank_corr(a[s], b[s])


__all__ = ["Study", "bk", "dg"]
```

**10-03 23:25 · Bash** — Read books.py to see how books handle NaN labels

```bash
cd /Users/wxy/Desktop/Partura && cat partura/books.py
```

```
"""The tradable-book metrics, in exactly the convention the user's tables use.

AlphaCube's current single-factor ranking (``scripts/pick_single_factors.py``)
judges a factor by two books built from a causally EMA-smoothed signal:

* a **decile long/short book** (gross 1), after 15 bp per unit turnover, and
* a **pure long book**: the long leg of that same decile book rescaled to
  weight 1, minus the equal-weight return of every stock that has both a
  signal and a label that day.  A holding whose label is missing (it opened
  locked at limit-up and could not have been bought) earns 0.

The half-life is chosen from {0, 1, 2, 3, 5, 10, 20} on the FIT period only,
by that book's own after-cost Sharpe, and then held fixed.

``stats`` and ``long_book`` are vendored from that script rather than imported
(the script lives in another session's working tree and changes under us); the
vendoring is guarded by a reproduction check against the user's published
table (``scripts/reproduce_table.py``), which is the only thing that makes a
Partura number comparable with one of theirs.

On top of that convention this module adds the two views a distillation needs:

* ``leg_anatomy`` -- how much of the spread is the long leg and how much is the
  short leg.  In A-shares the short leg cannot be traded, and a book whose
  spread is 80% short leg is a different object from one that is 80% long leg
  even when the two Sharpe ratios agree.
* ``quantile_profile`` -- mean next-day excess by signal quantile.  A decile
  book assumes "more signal is better"; the profile says whether that is true.
"""

… (125 行略) …
    with np.errstate(invalid="ignore", divide="ignore"):
        q = np.floor(pos / np.maximum(cnt, 1)[:, None] * n)
    q = np.where(ok, q, np.nan)
    r = np.where(ok, t, 0.0)
    ew = np.where(cnt > 0, r.sum(1) / np.maximum(cnt, 1), np.nan)
    rows = []
    for k in range(n):
        sel = (q == k)
        m = sel.sum(1)
        with np.errstate(invalid="ignore", divide="ignore"):
            ex = np.where(m > 0, (r * sel).sum(1) / np.maximum(m, 1) - ew, np.nan)
        f = ex[np.isfinite(ex)]
        rows.append({"quantile": k + 1, "excess_ann": float(f.mean() * 252) if f.size else float("nan"),
                     "sharpe": float(f.mean() / f.std() * np.sqrt(252)) if f.size > 2 and f.std() > 0 else float("nan"),
                     "win": float((f > 0).mean()) if f.size else float("nan")})
    return rows


__all__ = ["HALFLIVES", "TOP_FRAC", "COST", "stats", "long_book", "short_leg_excess", "smoothed",
           "fit_halflives", "book_row", "books", "quantile_profile"]
```

**10-03 23:25 · Bash** — Search panels.py for masking logic

```bash
cd /Users/wxy/Desktop/Partura && grep -n "mask\|isfinite\|nan\b\|listed\|universe\|suspend" partura/panels.py | head -60
```

```
196:                full[:-lag][self._locks[lag:]] = np.nan
210:        out[~np.isfinite(out)] = np.nan
330:                arr[~np.isfinite(arr)] = np.nan            # inf is never a tradable value
```

**10-03 23:25 · Bash** — Read panel computation code

```bash
cd /Users/wxy/Desktop/Partura && sed -n 150,361p partura/panels.py
```

```
            return
        f = auto_gpu_fraction()
        torch.cuda.set_per_process_memory_fraction(f)
        self.gpu_fraction = f
        if self._user_chunk_bytes is None:
            self.chunk_bytes = self._chunk_for(f)
        if not self.quiet:
            free, total = torch.cuda.mem_get_info()
            print(f"[panels] GPU: {free / (1 << 30):.1f} GiB free of {total / (1 << 30):.1f}; "
                  f"this run capped at {f:.0%} ({f * total / (1 << 30):.1f} GiB), chunk {self.chunk_bytes >> 20} MiB",
                  flush=True)

    # -- identity ---------------------------------------------------------
    @property
    def view_id(self) -> str:
        raw = f"{self.store_path}|{self.start}|{self.end}|{len(self.symbols)}|{self.dates[0]}|{self.dates[-1]}"
        return hashlib.sha1(raw.encode()).hexdigest()[:10]

    def _cache_path(self, expr_key: str) -> Optional[Path]:
        if not self.cache_dir:
            return None
        h = hashlib.sha1(f"{self.view_id}|{expr_key}".encode()).hexdigest()[:16]
        return self.cache_dir / f"{h}.npy"

    # -- labels -----------------------------------------------------------
    def target(self, horizon: int = 1) -> np.ndarray:
        if horizon not in self._targets:
            tag = f"__label__|{self.label_kind}|h{horizon}|buyable{int(self.label_buyable)}"
            p = self._cache_path(tag)
            if p is not None and p.is_file():
… (162 行略) …
                print(f"[panels]   {min(b0 + self.batch, len(uniq))}/{len(uniq)} "
                      f"({time.perf_counter() - t0:.0f}s)", flush=True)
        if not self.quiet:
            bad = [n for n in todo if n in self.errors]
            print(f"[panels] done in {time.perf_counter() - t0:.0f}s"
                  f"{'; failed: ' + ', '.join(bad) if bad else ''}", flush=True)
        return out

    # -- split slicing ----------------------------------------------------
    def split_slice(self, split: str) -> slice:
        from .splits import SPLITS
        a, b = SPLITS[split]
        d = np.asarray(self.dates)
        idx = np.nonzero((d >= a) & (d <= b))[0]
        if idx.size == 0:
            raise ValueError(f"split {split} ({a}..{b}) is empty in this view")
        return slice(int(idx[0]), int(idx[-1]) + 1)


__all__ = ["PanelSet", "parse_research", "SHARED_CACHE"]
```

**10-03 23:25 · Bash** — Read local long_short_weights, ema_rows, portfolio_returns

```bash
cd /Users/wxy/Desktop/AlphaCube && grep -n "def long_short_weights" -A 40 src/alphacube/metrics.py | head -90; grep -n "def ema_rows" -A 30 src/alphacube/metrics.py | head -50; grep -n "def portfolio_returns" -A 25 src/alphacube/metrics.py
```

```
282:def long_short_weights(alpha: np.ndarray, top_frac: float) -> np.ndarray:
283-    """(D, S) alpha -> (D, S) target weights: equal-weight long the top ``top_frac``,
284-    short the bottom, gross exposure 1 (so +0.5 long / -0.5 short) and net 0.
285-    Days with too few names are all-zero rather than NaN, so a gap in the alpha
286-    means "hold nothing", not "hold the previous book forever".
287-
288-    Ties at a boundary go by symbol order (a stable sort). numpy's default sort
289-    is not stable, and which of the tied names it put in the book depended on
290-    the rest of the row: nudging one mid-ranked name changed the book in 12 of
291-    200 tied rows, i.e. turnover charged for trades nobody would make. With
292-    turnover now part of the GP fitness (``rank_ic_turnover`` builds the same
293-    book in torch) that noise would also have been selected against."""
294-    alpha = np.asarray(alpha, dtype=np.float64)
295-    D, S = alpha.shape
296-    fin = np.isfinite(alpha)
297-    n = fin.sum(axis=1)
298-    order = np.argsort(np.where(fin, alpha, np.inf), axis=1, kind="stable")     # non-finite last
299-    k = np.maximum(1, np.floor(n * top_frac).astype(np.int64))
300-    pos = np.arange(S)[None, :]
301-    ok = (n >= 2)[:, None]
302-    long_ = ok & (pos >= (n - k)[:, None]) & (pos < n[:, None])
303-    short = ok & (pos < k[:, None])
304-    w_sorted = np.where(long_, 0.5 / k[:, None], np.where(short, -0.5 / k[:, None], 0.0))
305-    w = np.zeros((D, S), dtype=np.float64)
306-    np.put_along_axis(w, order, w_sorted, axis=1)
307-    return w
308-
309-
310-def apply_turnover_cap(target: np.ndarray, cap: Optional[float]) -> np.ndarray:
311-    """Walk the book forward, never trading more than ``cap`` in a day.
… (48 行略) …
343-    whole book costs ``2 * cost_per_side``. Returns (net, gross, turnover)."""
344-    D = weights.shape[0]
345-    gross = np.full(D, np.nan)
346-    turn = np.zeros(D)
347-    prev = np.zeros(weights.shape[1], dtype=np.float64)
348-    for t in range(D):
349-        w, r = weights[t], fwd[t]
350-        traded = np.abs(w - prev).sum()
351-        turn[t] = 0.5 * traded
352-        m = np.isfinite(r)
353-        gross[t] = float((w[m] * r[m]).sum()) if m.any() else np.nan
354-        prev = w
355-    net = gross - turn * 2.0 * cost_per_side
356-    return net, gross, turn
357-
358-
359-def _long_short_returns(alpha: np.ndarray, fwd: np.ndarray, top_frac: float) -> np.ndarray:
360-    n_days = alpha.shape[0]
361-    out = np.full(n_days, np.nan)
362-    for t in range(n_days):
```

**10-03 23:26 · Bash** — List diagnose.py functions

```bash
cd /Users/wxy/Desktop/Partura && grep -n "^def \|^    def " partura/diagnose.py && sed -n 1,60p partura/diagnose.py
```

```
42:def _rank_rows_torch(x: np.ndarray, device: str, rows: int = 512) -> np.ndarray:
64:def rank_rows(x: np.ndarray) -> np.ndarray:
79:def ic_series(panel: np.ndarray, target: np.ndarray) -> np.ndarray:
83:def rank_ic_series(panel: np.ndarray, target: np.ndarray, *, panel_ranks: Optional[np.ndarray] = None,
95:def _ir(x: np.ndarray) -> float:
100:def _tstat(x: np.ndarray) -> float:
105:def sign_from(panel: np.ndarray, target: np.ndarray, use: str = "rank_ic",
113:def ic_row(panel: np.ndarray, target: np.ndarray, *, sign: float = 1.0,
136:def distinct_fraction(panel: np.ndarray, step: int = 5, min_names: int = 30) -> float:
149:def metric_row(panel: np.ndarray, target: np.ndarray, *, sign: float = 1.0,
162:    def curve(v: np.ndarray) -> Tuple[float, float]:
190:def _zrank(x: np.ndarray) -> np.ndarray:
197:def neutralise(panel: np.ndarray, controls: Dict[str, np.ndarray], space: str = "rank",
244:def conditional_ic(panel: np.ndarray, target: np.ndarray, gate: np.ndarray, buckets: int = 5,
271:def decay(panel: np.ndarray, targets: Dict[int, np.ndarray], sign: float = 1.0) -> List[Dict[str, float]]:
280:def by_year(panel: np.ndarray, target: np.ndarray, years: np.ndarray, *, sign: float = 1.0,
299:def extreme_day_dependence(panel: np.ndarray, target: np.ndarray, *, sign: float = 1.0,
318:def smoothing_sweep(panel: np.ndarray, target: np.ndarray, *, sign: float = 1.0,
341:def pair_rank_corr(a: np.ndarray, b: np.ndarray) -> float:
347:def rank_corr_matrix(panels: Dict[str, np.ndarray]) -> Dict[str, Dict[str, float]]:
"""Diagnostics that turn a panel into evidence about a hypothesis.

AlphaCube already answers "how good is it" (IC, ICIR, turnover, net Sharpe).
Partura needs to answer "where does it come from", so this module adds the
discriminating measurements AlphaCube has no reason to own:

* ``neutralise``        -- daily cross-sectional residual after regressing the
  factor on control panels (size / price / volatility / reversal / momentum).
  If the alpha survives, the controls do not explain it; if it dies, they do.
* ``conditional_ic``    -- the IC of A inside quantile buckets of B.  This is
… (30 行略) …

def _rank_rows_torch(x: np.ndarray, device: str, rows: int = 512) -> np.ndarray:
    """``rank_rows`` on an accelerator: per-row average ranks (ties averaged) of
    the finite cells, NaN elsewhere -- the same answer as the pandas version
    (locked by tests/test_partura.py), without the CPU.  The server's CPU quota
    is usually taken by a neighbouring job while its GPU sits idle, and ranking
    a 1400 x 5200 panel is the single hottest call in a study."""
    import torch
    x = np.asarray(x, dtype=np.float64)
    out = np.empty(x.shape, dtype=np.float64)
    for a in range(0, x.shape[0], rows):
        t = torch.as_tensor(x[a:a + rows], device=device)
        fin = torch.isfinite(t)
        s, order = torch.sort(torch.where(fin, t, torch.full_like(t, float("inf"))), dim=1, stable=True)
        lo = torch.searchsorted(s, s, right=False)
        hi = torch.searchsorted(s, s, right=True)
        avg = (lo + hi + 1).to(torch.float64) / 2.0
        r = torch.empty_like(t).scatter_(1, order, avg)
        r[~fin] = float("nan")
        out[a:a + rows] = r.cpu().numpy()
```

**10-03 23:26 · Bash** — Read ic_row, neutralise, conditional_ic

```bash
cd /Users/wxy/Desktop/Partura && sed -n 105,135p partura/diagnose.py && sed -n 186,270p partura/diagnose.py
```

```
def sign_from(panel: np.ndarray, target: np.ndarray, use: str = "rank_ic",
              target_ranks: Optional[np.ndarray] = None) -> float:
    s = (rank_ic_series(panel, target, target_ranks=target_ranks) if use == "rank_ic"
         else ic_series(panel, target))
    m = nanmean_quiet(s)
    return -1.0 if (np.isfinite(m) and m < 0) else 1.0


def ic_row(panel: np.ndarray, target: np.ndarray, *, sign: float = 1.0,
           target_ranks: Optional[np.ndarray] = None) -> Dict[str, float]:
    """Prediction metrics only (no book): what a stage needs for every variant
    when the money side is reported by ``partura.books``."""
    raw = np.asarray(panel, dtype=np.float64)
    p = sign * raw
    ic = ic_series(p, target)
    ric = rank_ic_series(p, target, panel_ranks=sign * rank_rows(raw), target_ranks=target_ranks)
    lab = np.isfinite(target)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        return {
            "sign": float(sign),
            "ic": nanmean_quiet(ic), "icir": _ir(ic), "ic_t": _tstat(ic),
            "rank_ic": nanmean_quiet(ric), "rank_icir": _ir(ric), "rank_ic_t": _tstat(ric),
            "ic_pos": float((ic[np.isfinite(ic)] > 0).mean()) if np.isfinite(ic).any() else float("nan"),
            "coverage": float(np.isfinite(raw).mean()),
            # the gate the user's single-factor ranking applies: of the cells that HAVE a label
            "coverage_labelled": float((np.isfinite(raw) & lab).sum() / max(int(lab.sum()), 1)),
            "n_days": int(np.isfinite(ic).sum()),
        }

… (66 行略) …
    p = np.asarray(panel, dtype=np.float64)
    g = np.asarray(gate, dtype=np.float64)
    t = np.asarray(target, dtype=np.float64)
    rg = rank_rows(g)
    n = np.isfinite(rg).sum(axis=1, keepdims=True)
    with np.errstate(invalid="ignore"):
        b = np.floor((rg - 1.0) / np.maximum(n, 1) * buckets)
    rows = []
    for k in range(buckets):
        sel = (b == k)
        pk = np.where(sel, p, np.nan)
        ric = rank_ic_series(pk, np.where(sel, t, np.nan))
        icc = cs_pearson(np.where(sel, p, np.nan), np.where(sel, t, np.nan))
        rows.append({"bucket": k, "rank_ic": nanmean_quiet(ric), "rank_icir": _ir(ric),
                     "ic": nanmean_quiet(icc), "n_days": int(np.isfinite(ric).sum()),
                     "mean_names": float(np.nanmean(sel.sum(axis=1)))})
    return rows


# ---------------------------------------------------------------- time
```

**10-03 23:26 · Bash** — Run overview for F105

```bash
cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python scripts/overview_for.py F105_std_fangzheng_covamt 2>&1 | head -120
```

```
== F105_std_fangzheng_covamt  (挖掘 #25; 方向 -1, 半衰期 3) ==
可交易信号(方向 x 面板,按公布的半衰期平滑)在 train 上的日截面 rank 相关:
  本批其他因子: F103(#820) +0.33  F110(ret_fair_log) +0.31  F102(#3961) +0.28  F112(#574) +0.28  F111(#953) +0.26  F107(#613) +0.25
  控制变量:     ctl_amt -0.64  ctl_dvol20 -0.46  ctl_turnrate -0.43  ctl_range -0.27  ctl_cap -0.26  ctl_price -0.25  ctl_ivol -0.18  ctl_mom20 -0.11  ctl_rev1 +0.03
  已知家族:     known_amt_max9 -0.69  known_stdamt_max9 -0.69  known_ivol_max9 -0.25
控制变量能张成它多少(秩空间逐日回归的 R²): 全部 0.500;单个: ctl_amt 0.418  ctl_dvol20 0.217  ctl_turnrate 0.193  ctl_range 0.079  ctl_cap 0.073  ctl_price 0.068  ctl_ivol 0.039  ctl_mom20 0.028  ctl_rev1 0.011
(注意:控制变量的符号没有对齐方向;相关的正负要结合因子方向读。|相关| ≥ 0.95 在 AlphaCube 里算同一因子族。)
```

**10-03 23:27 · 写文件** `/Users/wxy/Desktop/Partura/studies/F105_std_fangzheng_covamt/audit_1.py`(13185 字符)

**10-03 23:28 · Bash** — Syntax-check audit script and view server status

```bash
cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python -m py_compile studies/F105_std_fangzheng_covamt/audit_1.py && echo OK && sed -n 79,95p partura/diagnose.py && ./scripts/study.sh status 2>&1 | head -20
```

```
OK
def ic_series(panel: np.ndarray, target: np.ndarray) -> np.ndarray:
    return cs_pearson(np.asarray(panel, dtype=np.float64), target)


def rank_ic_series(panel: np.ndarray, target: np.ndarray, *, panel_ranks: Optional[np.ndarray] = None,
                   target_ranks: Optional[np.ndarray] = None) -> np.ndarray:
    """``rank_rows`` is pandas' ``rank(axis=1)`` -- correct (ties averaged, inf
    skipped) but slow on a 1000 x 5000 panel, and this is the single hottest
    call in a run.  Pre-computed ranks may be passed in; a correlation is
    invariant to an affine map, so a flipped factor can reuse the unflipped
    ranks with a sign."""
    pr = rank_rows(np.asarray(panel, dtype=np.float64)) if panel_ranks is None else panel_ranks
    tr = rank_rows(target) if target_ranks is None else target_ranks
    return cs_pearson(pr, tr)


def _ir(x: np.ndarray) -> float:
	551291.pt_F104_final	(10/04/26 14:27:02)	(Detached)

540353, 22626 MiB
551294, 862 MiB
container anon 7.2 GiB
gpu.lock slot0.lock slot1.lock slot2.lock
```

**10-03 23:28 · Bash** — Start audit script on server

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh exec F105_std_fangzheng_covamt audit1 audit_1.py 2>&1 | tail -5
```

```
started F105_std_fangzheng_covamt/audit1: audit_1.py
```

**10-03 23:28 · Bash** — Outline of final report

```bash
cd /Users/wxy/Desktop/Partura && grep -n "^## \|^### " research/alpha_distillation/F105_std_fangzheng_covamt.md | head -80
```

```
11:## 1. 原始表达式
25:## 2. 算子的真实语义
29:### `day_cov`
37:### `cross_max`
46:### `cross_fangzheng`
55:### `ts_stddev`
86:### 既往研究留下的先验
112:## 3. 数学分解
154:## 4. 结构语法
178:## 5. 竞争性假设
206:## 6. 基线指标
301:## 7. 消融实验
303:### S0_baseline
319:### S1_what
364:### S1b_events
416:### S2_nodes
485:### S3_family
542:### S4_longleg
601:### S_final
659:### 中性化(fit 段)
782:### 条件 IC(fit 段)
811:### 控制变量自己当因子(同口径)
837:### 07x 直接量数据:根节点的排序跟着什么走,钱落在哪一类股票日上(`studies/F105_std_fangzheng_covamt/events.py`)
920:### 07x 多头腿为什么变好、经不经得起几个检查(`studies/F105_std_fangzheng_covamt/longleg.py`)
986:## 8. 语义变体
1064:## 9. 机制诊断
1066:### 一句话
1072:### 已确立(每条后面是能指到的实验)
1093:### 合理但没有坐实
1101:### 未决
1108:### 假设表的判决
1124:## 10. 蒸馏 / 升华后的候选
1137:### 结果
1154:### 留出段(20230808–20251231,只读了这一次;上面那张表,方向和半衰期都在用户训练段上定)
1188:### 为什么它比原式好用
1195:### 它没有比原式好的地方,以及限制
1202:## 11. 失效模式与风险
1222:## 12. 下一步实验
1236:## 附录 A — 数据段使用台账
1248:## 附录 B — 复现
```

**10-03 23:28 · Bash** — Read operator semantics section of report

```bash
cd /Users/wxy/Desktop/Partura && sed -n 25,112p research/alpha_distillation/F105_std_fangzheng_covamt.md
```

```
## 2. 算子的真实语义

> 每一条都来自注册表与内核源码,加上在张量上实跑的探针;没有一条是从算子名字推断的。探针集合按**这棵树**挑:不适用的写明,本研究新增的单独标出。

### `day_cov`

- **实现**: `operators/dt_day.py:212` (kernel `dt_day.day_cov`)
- **声明**: face `dt` / family `day` / category `binary`, arity 2, 计算轴 `M`, 无窗口, 折叠分钟轴 (M→1)
- **标志**: 无
- **实测探针**: 分钟顺序依赖 = False; 平移不变 = True; 齐次度 k = 2.0; nan_behaviour = finite_frac_with_10pct_missing=1.0, all_nan_input_gives_all_nan=True; 取负后 = even
- <sub>不适用的探针: causal_on_day_axis, rank_preserving, monotone_in_window, effective_memory, window_exit_echo, chain_impulse_profile, tail_dominance, std_reads_change</sub>

### `cross_max`

- **实现**: `operators/dt_cross.py:232` (kernel `dt_cross.cross_max`)
- **声明**: face `dt` / family `cross` / category `rolling`, arity 1, 计算轴 `D`, 窗口 3
- **标志**: 无
- **实测探针**: 日轴因果性 = True; 平移不变 = False; 齐次度 k = 1.0; nan_behaviour = finite_frac_with_10pct_missing=0.9927, all_nan_input_gives_all_nan=True; 取负后 = neither; 窗口变长 = non_decreasing; 脉冲记忆天数 = 3
- **本研究新增的探针**: window_exit_echo = window=3, entry_step=50.0, exit_step=-50.0, exit_over_entry=1.0, selfcheck={'cross_mean_entry_is_X/w': True, 'cross_mean_ratio_is_1': True, 'decay_linear_entry_is_2X/(w+1)': True, 'decay_linear_ratio_is_1/w': True}; tail_dominance = window=3, sigma_0.5={'vs_window_max': 1.0, 'vs_window_mean': 0.893, 'vs_window_median': 0.553}, sigma_1={'vs_window_max': 1.0, 'vs_window_mean': 0.945, 'vs_window_median': 0.531}, sigma_1.5={'vs_window_max': 1.0, 'vs_window_mean': 0.97, 'vs_window_median': 0.513}, sigma_2.5={'vs_window_max': 1.0, 'vs_window_mean': 0.992, 'vs_window_median': 0.512}, selfcheck={'cross_max_reads_max': True, 'cross_mean_reads_mean': True}
- <sub>不适用的探针: order_dependent_on_minutes, rank_preserving, chain_impulse_profile, std_reads_change</sub>

### `cross_fangzheng`

- **实现**: `operators/dt_cross.py:498` (kernel `dt_cross.cross_fangzheng`)
- **声明**: face `dt` / family `cross` / category `rolling`, arity 1, 计算轴 `D`, 窗口 241
- **标志**: 无
- **实测探针**: 日轴因果性 = True; 平移不变 = False; 齐次度 k = 1.0; nan_behaviour = finite_frac_with_10pct_missing=0.9948, all_nan_input_gives_all_nan=True; 取负后 = neither; 窗口变长 = neither; 脉冲记忆天数 = 27
- **本研究新增的探针**: window_exit_echo = window=241, entry_step=3.42156, exit_step=-3.42156, exit_over_entry=1.0, selfcheck={'cross_mean_entry_is_X/w': True, 'cross_mean_ratio_is_1': True, 'decay_linear_entry_is_2X/(w+1)': True, 'decay_linear_ratio_is_1/w': True}; chain_impulse_profile = nonzero_lag_ranges=['0..5', '241..246'], n_nonzero_days=12, entry_peak=2.5285, echo_peak=2.5285, echo_over_entry=1.0, decay_linear_mid_echo_over_entry=0.0152, noisy_background={'spike_10x_median': {'entry_peak_over_background_median': 10.5, 'echo_peak_over_background_median': 10.9}, 'spike_100x_median': {'entry_peak_over_background_median': 399.9, 'echo_peak_over_background_median': 398.1}}, selfcheck={'mean_chain_entry_peak_is_sqrt(6.8/5)X/241': True, 'mean_chain_echo_equals_entry': True}; tail_dominance = window=241, sigma_0.5={'vs_window_max': 0.6, 'vs_window_mean': 0.872, 'vs_window_median': 0.441}, sigma_1={'vs_window_max': 0.797, 'vs_window_mean': 0.861, 'vs_window_median': 0.233}, sigma_1.5={'vs_window_max': 0.91, 'vs_window_mean': 0.887, 'vs_window_median': 0.182}, sigma_2.5={'vs_window_max': 0.978, 'vs_window_mean': 0.963, 'vs_window_median': 0.099}, selfcheck={'cross_max_reads_max': True, 'cross_mean_reads_mean': True}
- <sub>不适用的探针: order_dependent_on_minutes, rank_preserving, std_reads_change</sub>

… (38 行略) …
| 给一个逐日抖动的日内统计量套上日轴极值记忆,换手能降到四分之一,且 rank IC 往往不降反升 | day_var(Ret) 裸用 rank IC 0.0416/换手 45.8%/扣费 −2.07;cross_max(·,9) 后 0.0480/11.2%/+0.79 | `F001_dwgated_covamtlow` (2026-09-30) | medium | 只在换手是瓶颈的成本口径下成立(15bp 单边);成本更低时未必划算 |
| 成交额水平家族可以通过 day_cov(Amt, 价格) 这类未封结构绕过 AlphaCube 的结构封禁与 0.95 rank 相关封禁 | cross_max(day_cov(Amt,Low),9) 与 cross_max(day_sum(Amt),9) 的 rank 相关只有 0.809(低于闸),但对 log 成交额中性化后 rank IC 掉 56%(R² 0.579) | `F001_dwgated_covamtlow` (2026-09-30) | high | 封禁列表变了要重查;建议改用对已封族中性化后的掉幅做判据 |

读内核源码(`study.sh src`)时发现的、和名字不一样或探针表里看不出来的事:

1. **`day_cov(Amt, Amt)` 就是日内分钟成交额的总体方差**(分母是有效分钟数,不是 n−1;有效分钟 < 2 时为 NaN)。
   它恒非负、对 Amt 是 **2 次齐次**(探针实测 k = 2.0)。和 `day_var(Amt)` = `day_std(Amt)²` 是同一个量,
   所以这棵树从叶子开始就带着「成交额的平方」这个尺度,而且一路没有任何去尺度的节点(后面三层都是 1 次齐次)。
2. **`cross_fangzheng(x, d)` = `cross_mean(x, d) + cross_stddev(x, d)`**,一行代码。名字(方正?)没有任何信息量。
   两项都是**硬窗口**、**忽略 NaN**(`nanmean` / 总体 `nanstd`,分母是窗口内有限值的个数)。
3. **241 在这里是交易日数,不是分钟数。** `cross_*` 滚的是交易日轴;241 恰好是每天的分钟格数,
   但作为 `cross_fangzheng` 的窗口它是「约一年」(一年约 243 个交易日)。
4. **窗口不满也出值。** `rolling_windows` 在左侧补 NaN,`nanmean/nanstd` 只在有限值上算,所以一只股票上市后的
   头 241 个交易日、以及样本头一年(视图从 20180102 开始,warmup 实际拿到 0 行),`C` 用的是**逐日变长的扩张窗口**:
   第 n 天进来一个新值,均值移动 (x−均值)/n,比窗口满了之后的 1/241 大得多。→ 次新股的 `D` 被机械放大(见 H7)。
5. **`ts_stddev` = `ts_std`**,总体标准差,同样忽略 NaN。它对输入取负不变(偶函数):`C` 往上走和往下走读出来一样。
6. **内置探针在 241 窗口上是瞎的。** 内置探针的样本只有 40 行,比窗口短:`cross_fangzheng` 的「脉冲记忆天数 = 27」
   只是 40 − 13 = 27(脉冲之后剩下的行数),不是这个算子的性质。本研究的四个探针都用 ≥ 3×窗口 的样本重测。

## 3. 数学分解
```

**10-03 23:28 · Bash** — Inspect final.json structure

```bash
cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python - <<'EOF'
import json
j=json.load(open('runs/F105_std_fangzheng_covamt/final.json'))
print(j.keys())
for k,v in j.items():
    if isinstance(v,dict): print(k, list(v.keys())[:20])
    elif isinstance(v,list): print(k, len(v), type(v[0]) if v else None)
    else: print(k, v if len(str(v))<200 else str(v)[:200])
EOF
```

```
dict_keys(['factor_id', 'config', 'stages', 'provenance', 'view', 'label', 'cost_per_side', 'top_frac', 'fit_split', 'user_split', 'rank_by', 'halflives', 'splits_used', 'split_dates', 'results', 'errors', 'engine_timings', 'diagnostics', 'seconds', 'peak_anon_gb'])
factor_id F105_std_fangzheng_covamt
config configs/F105_std_fangzheng_covamt.yaml
stages 1 <class 'str'>
provenance ['alphacube_root', 'alphacube_commit', 'alphacube_dirty', 'partura_root', 'partura_commit', 'partura_code_sha', 'store', 'python', 'torch', 'numpy', 'host']
view ['days', 'symbols', 'first', 'last', 'warmup_rows']
label ['kind', 'horizon', 'buyable']
cost_per_side 0.0015
top_frac 0.1
fit_split train
user_split utrain
rank_by ls
halflives 7 <class 'float'>
splits_used 5 <class 'str'>
split_dates ['train', 'valid', 'utrain', 'holdout', 'full']
results ['f_orig', 'f_min3', 'f_max15', 'f_max30', 'f_max60']
errors []
engine_timings 0 None
diagnostics ['by_year', 'by_year_scope', 'rank_corr_train']
seconds 165.2
peak_anon_gb 2.56
```

**10-03 23:28 · Bash** — Inspect per-variant result structure

```bash
cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python - <<'EOF'
import json
j=json.load(open('runs/F105_std_fangzheng_covamt/final.json'))
r=j['results']['f_max30']
print(r.keys())
for k in r:
    v=r[k]
    if isinstance(v,dict): print(k, list(v.keys())[:30])
ub=r.get('user_books') or r.get('books_user') 
print(json.dumps({k:(v if not isinstance(v,(dict,list)) else '...') for k,v in r.items()},ensure_ascii=False)[:1500])
EOF
```

```
dict_keys(['expr', 'stage', 'why', 'group', 'sign', 'splits', 'distinct', 'books', 'sign_user', 'ic_user', 'ic_holdout', 'books_user'])
splits ['train', 'valid']
books ['hl_ls', 'hl_long', 'hl_used', 'rank_by', 'sweep', 'splits', 'splits_at_hl_long']
ic_user ['sign', 'ic', 'icir', 'ic_t', 'rank_ic', 'rank_icir', 'rank_ic_t', 'ic_pos', 'coverage', 'coverage_labelled', 'n_days']
ic_holdout ['sign', 'ic', 'icir', 'ic_t', 'rank_ic', 'rank_icir', 'rank_ic_t', 'ic_pos', 'coverage', 'coverage_labelled', 'n_days']
books_user ['hl_ls', 'hl_long', 'hl_used', 'rank_by', 'sweep', 'splits', 'splits_at_hl_long']
{"expr": "cross_max(day_std(Amt), 30)", "stage": "S_final", "why": "读留出段之前定下的推荐:平台中央、train/valid 多头腿净超额和纯多头夏普最高。预测留出段多头腿净超额与纯多头夏普高于原式;两项都低于原式就算升华失败", "group": "final", "sign": -1.0, "splits": "...", "distinct": 1.0, "books": "...", "sign_user": -1.0, "ic_user": "...", "ic_holdout": "...", "books_user": "..."}
```

**10-03 23:28 · Bash** — Extract user-convention books incl. hl_long alternative from final.json

```bash
cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python - <<'EOF'
import json
j=json.load(open('runs/F105_std_fangzheng_covamt/final.json'))
for vid,r in j['results'].items():
    bu=r['books_user']
    print(vid, 'hl_ls',bu['hl_ls'],'hl_long',bu['hl_long'],'used',bu['hl_used'])
    for sp,b in bu['splits'].items():
        print('   ',sp, 'LS %.2f Lgross %.3f Lnet %.3f Lshp %.2f short %.3f TO %.3f Lmdd %.3f'%(b['ls_sharpe'],b['long_gross_ann'],b['long_ann'],b['long_sharpe'],b['short_gross_ann'],b['ls_turnover'],b['long_mdd']))
    if 'splits_at_hl_long' in bu:
        for sp,b in bu['splits_at_hl_long'].items():
            print('  @hl_long',sp, 'LS %.2f Lgross %.3f Lnet %.3f Lshp %.2f short %.3f TO %.3f'%(b['ls_sharpe'],b['long_gross_ann'],b['long_ann'],b['long_sharpe'],b['short_gross_ann'],b['ls_turnover']))
    print('   ic_holdout rank_ic %.4f  ic_user %.4f'%(r['ic_holdout']['rank_ic'], r['ic_user']['rank_ic']))
    b=r['books']
    print('   decision: hl_ls',b['hl_ls'],'hl_long',b['hl_long'])
    if 'splits_at_hl_long' in b:
        for sp,x in b['splits_at_hl_long'].items():
            print('  @hl_long(train-fit)',sp, 'LS %.2f Lgross %.3f Lnet %.3f Lshp %.2f TO %.3f'%(x['ls_sharpe'],x['long_gross_ann'],x['long_ann'],x['long_sharpe'],x['ls_turnover']))
EOF
```

```
f_orig hl_ls 3.0 hl_long 3.0 used 3.0
    utrain LS 3.03 Lgross 0.168 Lnet 0.118 Lshp 1.96 short 0.311 TO 0.061 Lmdd -0.096
    holdout LS 2.24 Lgross 0.143 Lnet 0.089 Lshp 1.04 short 0.326 TO 0.067 Lmdd -0.144
   ic_holdout rank_ic 0.0577  ic_user 0.0425
   decision: hl_ls 3.0 hl_long 10.0
  @hl_long(train-fit) train LS 2.32 Lgross 0.121 Lnet 0.093 Lshp 1.49 TO 0.032
  @hl_long(train-fit) valid LS 4.08 Lgross 0.208 Lnet 0.182 Lshp 3.30 TO 0.033
f_min3 hl_ls 3.0 hl_long 10.0 used 3.0
    utrain LS 3.30 Lgross 0.175 Lnet 0.130 Lshp 2.18 short 0.339 TO 0.061 Lmdd -0.097
    holdout LS 2.72 Lgross 0.163 Lnet 0.115 Lshp 1.33 short 0.378 TO 0.067 Lmdd -0.141
  @hl_long utrain LS 3.03 Lgross 0.160 Lnet 0.134 Lshp 2.28 short 0.271 TO 0.033
  @hl_long holdout LS 2.52 Lgross 0.160 Lnet 0.135 Lshp 1.74 short 0.279 TO 0.034
   ic_holdout rank_ic 0.0580  ic_user 0.0429
   decision: hl_ls 3.0 hl_long 10.0
  @hl_long(train-fit) train LS 2.62 Lgross 0.138 Lnet 0.111 Lshp 1.84 TO 0.033
  @hl_long(train-fit) valid LS 4.35 Lgross 0.216 Lnet 0.191 Lshp 3.56 TO 0.034
f_max15 hl_ls 0.0 hl_long 3.0 used 0.0
    utrain LS 3.08 Lgross 0.203 Lnet 0.149 Lshp 2.26 short 0.379 TO 0.060 Lmdd -0.100
    holdout LS 2.70 Lgross 0.170 Lnet 0.120 Lshp 1.28 short 0.425 TO 0.057 Lmdd -0.156
  @hl_long utrain LS 2.73 Lgross 0.196 Lnet 0.162 Lshp 2.45 short 0.297 TO 0.040
  @hl_long holdout LS 2.30 Lgross 0.164 Lnet 0.133 Lshp 1.41 short 0.326 TO 0.038
   ic_holdout rank_ic 0.0617  ic_user 0.0519
   decision: hl_ls 0.0 hl_long 3.0
  @hl_long(train-fit) train LS 2.29 Lgross 0.174 Lnet 0.139 Lshp 2.04 TO 0.041
  @hl_long(train-fit) valid LS 4.04 Lgross 0.251 Lnet 0.221 Lshp 3.61 TO 0.038
f_max30 hl_ls 0.0 hl_long 1.0 used 0.0
    utrain LS 2.80 Lgross 0.196 Lnet 0.161 Lshp 2.46 short 0.297 TO 0.038 Lmdd -0.088
    holdout LS 2.39 Lgross 0.157 Lnet 0.125 Lshp 1.37 short 0.320 TO 0.035 Lmdd -0.151
  @hl_long utrain LS 2.75 Lgross 0.198 Lnet 0.167 Lshp 2.55 short 0.279 TO 0.034
  @hl_long holdout LS 2.29 Lgross 0.163 Lnet 0.135 Lshp 1.47 short 0.290 TO 0.031
   ic_holdout rank_ic 0.0536  ic_user 0.0461
   decision: hl_ls 0.0 hl_long 1.0
  @hl_long(train-fit) train LS 2.33 Lgross 0.177 Lnet 0.145 Lshp 2.15 TO 0.035
  @hl_long(train-fit) valid LS 4.03 Lgross 0.250 Lnet 0.223 Lshp 3.66 TO 0.031
f_max60 hl_ls 0.0 hl_long 0.0 used 0.0
    utrain LS 2.52 Lgross 0.177 Lnet 0.155 Lshp 2.34 short 0.232 TO 0.024 Lmdd -0.087
    holdout LS 2.39 Lgross 0.166 Lnet 0.147 Lshp 1.74 short 0.256 TO 0.021 Lmdd -0.118
   ic_holdout rank_ic 0.0462  ic_user 0.0386
   decision: hl_ls 0.0 hl_long 0.0
```

**10-03 23:29 · Bash** — Wait for audit job and print output

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh wait F105_std_fangzheng_covamt audit1 540 2>&1 | tail -150
```

```
done 80s
[partura exit 0 2026-10-04_14:29:54]
(no runs/F105_std_fangzheng_covamt/audit1.json — an exec job prints its own output; full log: logs/F105_std_fangzheng_covamt_audit1.log)
panels ready 3s; train slice(0, 973, None), valid slice(973, 1359, None); symbols 5220
  selfcheck [train] orig@3  LS +2.54  Lgross +13.1%  Lnet +8.2%  Lshp +1.32  short +29.9%  TO 6.0%
  selfcheck [train] max30@0 LS +2.37  Lgross +17.4%  Lnet +13.6%  Lshp +2.03  short +27.0%  TO 4.0%
  selfcheck [valid] orig@3  LS +4.62  Lgross +26.0%  Lnet +20.7%  Lshp +3.82  short +34.2%  TO 6.6%
  selfcheck [valid] max30@0 LS +4.12  Lgross +25.3%  Lnet +22.2%  Lshp +3.69  short +36.5%  TO 3.5%

== 0 semantics ==
--- server source: nanstd_last
def nanstd_last(w: torch.Tensor) -> torch.Tensor:
    mean = w.nanmean(dim=-1, keepdim=True)
    sq = torch.where(torch.isnan(w), torch.zeros_like(w), (w - mean) ** 2)
    count = nan_count(w).clamp(min=1).to(w.dtype)
    return torch.sqrt(sq.sum(dim=-1) / count)

--- server source: nanmax_last
def nanmax_last(w: torch.Tensor) -> torch.Tensor:
    filled = torch.where(torch.isnan(w), torch.full_like(w, float("-inf")), w)
    out = filled.max(dim=-1).values
    return torch.where(torch.isnan(w).all(dim=-1), torch.full_like(out, float("nan")), out)

--- server source: nanmean_last
def nanmean_last(w: torch.Tensor) -> torch.Tensor:
    return w.nanmean(dim=-1)

--- server source: rolling_windows
def rolling_windows(x: torch.Tensor, d: int, axis: int = 0) -> torch.Tensor:
    """Causal rolling windows of length `d` along `axis`, left-padded with
    NaN so every original position (including the first `d-1`) gets a
    window. Output shape = `x.shape` with a new trailing window-dim of
    size `d` appended (the `axis` dim's length is unchanged).
    """
    d = int(d)
    pad_shape = list(x.shape)
    pad_shape[axis] = d - 1
    pad = torch.full(pad_shape, float("nan"), dtype=x.dtype, device=x.device)
    x_padded = torch.cat([pad, x], dim=axis)
    return x_padded.unfold(axis, d, 1)

--- server source: _stddev
def _stddev(x: torch.Tensor) -> torch.Tensor:
    x_demean = x - x.nanmean(dim=-1, keepdim=True)
    return torch.sqrt(torch.nanmean(torch.pow(x_demean, 2), dim=-1))

  cells (train+valid): total 7093980; D finite 5312803; D finite where the stock has never had a finite day_cov 0; D == 0 exactly 10983 (of which labelled 9466); D finite & day_cov NaN today 0
  max30 finite 5312803; max30 finite & day_cov NaN today 0; max30 == 0 exactly 0
  [train] orig   long decile: names/day 360; share with NO label 1.91%; share with day_cov NaN today 0.00%; young share 23.38% | short decile: no label 2.55%, young 44.43%
  [train] max30  long decile: names/day 360; share with NO label 3.38%; share with day_cov NaN today 0.00%; young share 26.74% | short decile: no label 0.80%, young 30.97%
  [valid] orig   long decile: names/day 467; share with NO label 6.02%; share with day_cov NaN today 0.00%; young share 0.78% | short decile: no label 1.75%, young 17.89%
  [valid] max30  long decile: names/day 467; share with NO label 7.43%; share with day_cov NaN today 0.00%; young share 8.82% | short decile: no label 0.46%, young 5.77%

== 1 every factor at a FIXED half-life (sign -1), train and valid ==
  orig   hl    0      [train] LS +1.83  Lgross +12.1%  Lnet -0.5%  Lshp -0.09  short +32.2%  TO 13.3%   [valid] LS +3.64  Lgross +21.7%  Lnet +8.3%  Lshp +1.60  short +38.8%  TO 14.8%
  orig   hl    3 *fit [train] LS +2.54  Lgross +13.1%  Lnet +8.2%  Lshp +1.32  short +29.9%  TO 6.0%   [valid] LS +4.62  Lgross +26.0%  Lnet +20.7%  Lshp +3.82  short +34.2%  TO 6.6%
  orig   hl    5      [train] LS +2.43  Lgross +12.6%  Lnet +8.7%  Lshp +1.40  short +26.9%  TO 4.6%   [valid] LS +4.33  Lgross +23.6%  Lnet +19.7%  Lshp +3.56  short +31.4%  TO 5.0%
  orig   hl   10      [train] LS +2.32  Lgross +12.1%  Lnet +9.3%  Lshp +1.49  short +23.6%  TO 3.2%   [valid] LS +4.08  Lgross +20.8%  Lnet +18.2%  Lshp +3.30  short +28.5%  TO 3.3%
  min3   hl    0      [train] LS +2.13  Lgross +13.6%  Lnet +1.6%  Lshp +0.26  short +35.7%  TO 13.7%   [valid] LS +3.52  Lgross +23.1%  Lnet +10.0%  Lshp +1.78  short +37.5%  TO 15.7%
  min3   hl    3 *fit [train] LS +2.84  Lgross +14.3%  Lnet +9.9%  Lshp +1.62  short +32.9%  TO 5.9%   [valid] LS +4.80  Lgross +25.5%  Lnet +20.9%  Lshp +3.75  short +36.6%  TO 6.5%
  min3   hl    5      [train] LS +2.78  Lgross +13.7%  Lnet +10.2%  Lshp +1.68  short +30.6%  TO 4.6%   [valid] LS +4.65  Lgross +24.0%  Lnet +20.4%  Lshp +3.68  short +34.4%  TO 5.0%
  min3   hl   10      [train] LS +2.62  Lgross +13.8%  Lnet +11.1%  Lshp +1.84  short +26.0%  TO 3.3%   [valid] LS +4.35  Lgross +21.6%  Lnet +19.1%  Lshp +3.56  short +30.0%  TO 3.4%
  known9 hl    0 *fit [train] LS +2.47  Lgross +16.9%  Lnet +9.3%  Lshp +1.37  short +37.7%  TO 8.5%   [valid] LS +4.44  Lgross +24.9%  Lnet +18.5%  Lshp +3.09  short +48.1%  TO 7.7%
  known9 hl    3      [train] LS +2.26  Lgross +17.0%  Lnet +12.7%  Lshp +1.86  short +28.5%  TO 5.2%   [valid] LS +4.23  Lgross +25.6%  Lnet +22.0%  Lshp +3.59  short +42.0%  TO 4.8%
  known9 hl    5      [train] LS +2.17  Lgross +17.1%  Lnet +13.7%  Lshp +1.99  short +25.5%  TO 4.2%   [valid] LS +4.10  Lgross +25.1%  Lnet +22.2%  Lshp +3.59  short +39.5%  TO 3.9%
  known9 hl   10      [train] LS +1.99  Lgross +15.6%  Lnet +13.1%  Lshp +1.89  short +21.8%  TO 2.9%   [valid] LS +3.72  Lgross +24.2%  Lnet +22.1%  Lshp +3.50  short +33.2%  TO 2.7%
  max15  hl    0 *fit [train] LS +2.61  Lgross +18.0%  Lnet +12.3%  Lshp +1.81  short +34.9%  TO 6.2%   [valid] LS +4.52  Lgross +26.1%  Lnet +21.3%  Lshp +3.56  short +45.2%  TO 5.5%
  max15  hl    3      [train] LS +2.29  Lgross +17.4%  Lnet +13.9%  Lshp +2.04  short +26.6%  TO 4.1%   [valid] LS +4.04  Lgross +25.1%  Lnet +22.1%  Lshp +3.61  short +37.5%  TO 3.8%
  max15  hl    5      [train] LS +2.13  Lgross +16.5%  Lnet +13.5%  Lshp +1.97  short +23.8%  TO 3.5%   [valid] LS +3.78  Lgross +24.2%  Lnet +21.6%  Lshp +3.51  short +34.3%  TO 3.3%
  max15  hl   10      [train] LS +1.89  Lgross +14.5%  Lnet +12.4%  Lshp +1.80  short +20.2%  TO 2.7%   [valid] LS +3.53  Lgross +24.0%  Lnet +22.1%  Lshp +3.47  short +29.8%  TO 2.5%
  max30  hl    0 *fit [train] LS +2.37  Lgross +17.4%  Lnet +13.6%  Lshp +2.03  short +27.0%  TO 4.0%   [valid] LS +4.12  Lgross +25.3%  Lnet +22.2%  Lshp +3.69  short +36.5%  TO 3.5%
  max30  hl    3      [train] LS +2.10  Lgross +16.5%  Lnet +13.9%  Lshp +2.04  short +21.5%  TO 3.0%   [valid] LS +3.59  Lgross +23.7%  Lnet +21.4%  Lshp +3.44  short +30.0%  TO 2.7%
  max30  hl    5      [train] LS +1.96  Lgross +15.6%  Lnet +13.3%  Lshp +1.96  short +19.5%  TO 2.6%   [valid] LS +3.39  Lgross +22.6%  Lnet +20.6%  Lshp +3.29  short +28.2%  TO 2.4%
  max30  hl   10      [train] LS +1.70  Lgross +13.4%  Lnet +11.6%  Lshp +1.70  short +16.4%  TO 2.1%   [valid] LS +3.20  Lgross +22.4%  Lnet +20.9%  Lshp +3.31  short +24.8%  TO 2.0%
  max60  hl    0 *fit [train] LS +2.14  Lgross +15.9%  Lnet +13.5%  Lshp +1.98  short +21.0%  TO 2.6%   [valid] LS +3.64  Lgross +22.3%  Lnet +20.4%  Lshp +3.38  short +28.8%  TO 2.0%
  max60  hl    3      [train] LS +1.80  Lgross +14.2%  Lnet +12.3%  Lshp +1.81  short +16.2%  TO 2.0%   [valid] LS +3.45  Lgross +23.2%  Lnet +21.7%  Lshp +3.52  short +25.2%  TO 1.7%
  max60  hl    5      [train] LS +1.73  Lgross +13.6%  Lnet +11.9%  Lshp +1.75  short +15.2%  TO 1.9%   [valid] LS +3.36  Lgross +22.9%  Lnet +21.5%  Lshp +3.49  short +24.1%  TO 1.6%
  max60  hl   10      [train] LS +1.51  Lgross +11.9%  Lnet +10.5%  Lshp +1.55  short +12.9%  TO 1.6%   [valid] LS +3.21  Lgross +22.0%  Lnet +20.8%  Lshp +3.40  short +22.1%  TO 1.4%

== 2 drop names with < 247 observations from the universe, then rebuild the books ==
  mature only  orig   hl    3  [train] LS +1.71  Lgross +12.4%  Lnet +7.0%  Lshp +1.14  short +25.8%  TO 5.2%   [valid] LS +4.55  Lgross +27.2%  Lnet +22.0%  Lshp +4.07  short +35.5%  TO 6.9%
  mature only  orig   hl   10  [train] LS +1.70  Lgross +11.5%  Lnet +8.9%  Lshp +1.44  short +20.7%  TO 2.6%   [valid] LS +4.01  Lgross +22.3%  Lnet +19.8%  Lshp +3.58  short +28.8%  TO 3.3%
  mature only  min3   hl    3  [train] LS +1.94  Lgross +12.7%  Lnet +8.0%  Lshp +1.34  short +28.7%  TO 5.2%   [valid] LS +4.57  Lgross +26.1%  Lnet +21.6%  Lshp +3.88  short +36.3%  TO 6.8%
  mature only  known9 hl    0  [train] LS +1.56  Lgross +12.6%  Lnet +5.4%  Lshp +0.78  short +31.6%  TO 6.1%   [valid] LS +4.27  Lgross +25.6%  Lnet +19.2%  Lshp +3.22  short +46.3%  TO 7.7%
  mature only  known9 hl    5  [train] LS +1.38  Lgross +13.4%  Lnet +10.2%  Lshp +1.46  short +20.4%  TO 3.0%   [valid] LS +3.94  Lgross +25.2%  Lnet +22.3%  Lshp +3.60  short +38.3%  TO 3.8%
  mature only  max15  hl    0  [train] LS +1.66  Lgross +13.9%  Lnet +8.5%  Lshp +1.23  short +28.7%  TO 4.4%   [valid] LS +4.36  Lgross +26.5%  Lnet +21.7%  Lshp +3.64  short +43.8%  TO 5.5%
  mature only  max30  hl    0  [train] LS +1.61  Lgross +14.8%  Lnet +11.2%  Lshp +1.65  short +22.4%  TO 2.9%   [valid] LS +4.02  Lgross +25.4%  Lnet +22.3%  Lshp +3.70  short +36.2%  TO 3.5%
  mature only  max60  hl    0  [train] LS +1.49  Lgross +14.5%  Lnet +12.2%  Lshp +1.79  short +16.9%  TO 1.8%   [valid] LS +3.60  Lgross +22.4%  Lnet +20.5%  Lshp +3.41  short +29.5%  TO 2.1%
  -- what the young names inside each long decile earn (excess vs equal-weight of scored+labelled names)
  [train] orig   young: share 23.4%, names/day 84.2, mean excess -122.2%/yr, contribution to the long leg +2.75%/yr, amt pctile 0.20, cap pctile 0.38 | mature: share 76.6%, names/day 276.1, mean excess +14.0%/yr, contribution to the long leg +10.31%/yr, amt pctile 0.16, cap pctile 0.32
  [train] max30  young: share 26.7%, names/day 96.4, mean excess -5.2%/yr, contribution to the long leg +5.42%/yr, amt pctile 0.13, cap pctile 0.29 | mature: share 73.3%, names/day 263.9, mean excess +17.1%/yr, contribution to the long leg +12.02%/yr, amt pctile 0.11, cap pctile 0.28
  [train] max60  young: share 26.3%, names/day 94.9, mean excess -6.2%/yr, contribution to the long leg +4.77%/yr, amt pctile 0.15, cap pctile 0.32 | mature: share 73.7%, names/day 265.4, mean excess +16.1%/yr, contribution to the long leg +11.25%/yr, amt pctile 0.13, cap pctile 0.30
  [valid] orig   young: share 0.8%, names/day 3.6, mean excess -226.4%/yr, contribution to the long leg -1.84%/yr, amt pctile 0.80, cap pctile 0.15 | mature: share 99.2%, names/day 462.9, mean excess +28.3%/yr, contribution to the long leg +28.09%/yr, amt pctile 0.16, cap pctile 0.30
  [valid] max30  young: share 8.8%, names/day 41.2, mean excess +12.9%/yr, contribution to the long leg +1.26%/yr, amt pctile 0.09, cap pctile 0.04 | mature: share 91.2%, names/day 425.4, mean excess +26.9%/yr, contribution to the long leg +24.28%/yr, amt pctile 0.10, cap pctile 0.25
  [valid] max60  young: share 7.8%, names/day 36.6, mean excess +8.4%/yr, contribution to the long leg +0.70%/yr, amt pctile 0.10, cap pctile 0.04 | mature: share 92.2%, names/day 430.0, mean excess +24.1%/yr, contribution to the long leg +21.97%/yr, amt pctile 0.12, cap pctile 0.27
  symbols sample: ['000001.SZ', '000002.SZ', '000006.SZ'] ... ['688835.SH', '688836.SH', '688837.SH']
  [train] labelled universe by board: ChiNext 21.9%  SH 39.5%  STAR 2.2%  SZ 36.5%
  [train] orig   long decile by board: ChiNext 15.8%  SH 48.4%  STAR 1.3%  SZ 34.5%
  [train] max30  long decile by board: ChiNext 15.2%  SH 47.5%  STAR 3.4%  SZ 33.9%
  [train] max60  long decile by board: ChiNext 14.9%  SH 48.0%  STAR 3.5%  SZ 33.5%
  [valid] labelled universe by board: ChiNext 25.8%  SH 35.4%  STAR 7.4%  SZ 31.4%
  [valid] orig   long decile by board: ChiNext 21.8%  SH 39.9%  STAR 14.9%  SZ 23.4%
  [valid] max30  long decile by board: ChiNext 27.2%  SH 37.3%  STAR 17.6%  SZ 17.9%
  [valid] max60  long decile by board: ChiNext 26.5%  SH 37.1%  STAR 19.9%  SZ 16.6%
  -- the two halves of the cap distribution (universe restricted; compare within a block)
  [cap pctile < 0.5 ] orig   hl    3  [train] LS +2.90  Lgross +12.0%  Lnet +6.0%  Lshp +0.93  short +41.4%  TO 7.0%   [valid] LS +4.63  Lgross +16.1%  Lnet +10.0%  Lshp +1.83  short +41.4%  TO 7.4%
  [cap pctile < 0.5 ] orig   hl   10  [train] LS +2.51  Lgross +10.5%  Lnet +7.0%  Lshp +1.04  short +32.8%  TO 4.3%   [valid] LS +4.50  Lgross +15.3%  Lnet +12.1%  Lshp +2.19  short +34.3%  TO 4.3%
  [cap pctile < 0.5 ] max30  hl    0  [train] LS +3.64  Lgross +18.1%  Lnet +13.4%  Lshp +1.97  short +52.0%  TO 5.7%   [valid] LS +4.21  Lgross +17.0%  Lnet +13.2%  Lshp +2.24  short +45.8%  TO 5.0%
  [cap pctile < 0.5 ] max60  hl    0  [train] LS +3.02  Lgross +18.6%  Lnet +15.4%  Lshp +2.19  short +36.6%  TO 4.0%   [valid] LS +3.76  Lgross +16.7%  Lnet +14.4%  Lshp +2.35  short +34.6%  TO 3.3%
  [cap pctile >= 0.5] orig   hl    3  [train] LS +1.35  Lgross +10.7%  Lnet +5.1%  Lshp +0.72  short +19.5%  TO 6.8%   [valid] LS +2.97  Lgross +21.4%  Lnet +15.4%  Lshp +2.53  short +26.2%  TO 7.5%
  [cap pctile >= 0.5] orig   hl   10  [train] LS +1.36  Lgross +8.8%  Lnet +5.5%  Lshp +0.75  short +16.9%  TO 3.9%   [valid] LS +3.11  Lgross +21.5%  Lnet +18.2%  Lshp +2.92  short +21.9%  TO 4.0%
  [cap pctile >= 0.5] max30  hl    0  [train] LS +0.86  Lgross +6.0%  Lnet +1.8%  Lshp +0.22  short +15.6%  TO 4.5%   [valid] LS +3.05  Lgross +22.4%  Lnet +18.6%  Lshp +2.92  short +28.5%  TO 4.2%
  [cap pctile >= 0.5] max60  hl    0  [train] LS +0.84  Lgross +5.4%  Lnet +2.4%  Lshp +0.29  short +13.2%  TO 3.2%   [valid] LS +2.81  Lgross +19.2%  Lnet +16.4%  Lshp +2.59  short +23.9%  TO 2.9%

== 3 does the DIRECTION of the event carry information?  scale-free relative change, mature names only ==
  [train] rank IC: unsigned D/C -0.0268   signed sign(dC)*D/C -0.0323   D/C inside C-rising names -0.0405   D/C inside C-falling names -0.0135
      [train] top decile of |D/C|  C rising: names/day  131.7  excess -46.7%/yr  amt pctile 0.76   |   C falling: names/day  120.1  excess  +5.2%/yr  amt pctile 0.42
      [train] 9th decile           C rising: names/day  134.1  excess -11.0%/yr  amt pctile 0.72   |   C falling: names/day  118.5  excess  +7.0%/yr  amt pctile 0.44
      [train] deciles 6-8          C rising: names/day  416.5  excess  -3.2%/yr  amt pctile 0.65   |   C falling: names/day  341.9  excess  +4.9%/yr  amt pctile 0.42
      [train] bottom half          C rising: names/day  719.7  excess  +6.6%/yr  amt pctile 0.49   |   C falling: names/day  544.1  excess  +9.8%/yr  amt pctile 0.35
  [valid] rank IC: unsigned D/C -0.0363   signed sign(dC)*D/C -0.0362   D/C inside C-rising names -0.0624   D/C inside C-falling names -0.0196
      [valid] top decile of |D/C|  C rising: names/day  176.7  excess -61.3%/yr  amt pctile 0.79   |   C falling: names/day  240.8  excess  +2.7%/yr  amt pctile 0.46
      [valid] 9th decile           C rising: names/day  172.2  excess -23.2%/yr  amt pctile 0.73   |   C falling: names/day  246.2  excess  +1.8%/yr  amt pctile 0.49
      [valid] deciles 6-8          C rising: names/day  547.7  excess -11.8%/yr  amt pctile 0.66   |   C falling: names/day  708.2  excess  -0.1%/yr  amt pctile 0.48
      [valid] bottom half          C rising: names/day 1108.6  excess +10.3%/yr  amt pctile 0.50   |   C falling: names/day  984.4  excess +11.0%/yr  amt pctile 0.40
  -- quantile profile of the signed relative change (sign -1: Q1 = C rose most, Q10 = C fell most), hl 0 and hl 5
  hl 0 [train] -30.8% -3.3% -1.7% +4.5% +5.3% +6.7% +6.4% +5.9% +4.2% +2.8%   | book: LS +0.62  Lgross +2.8%  Lnet -8.5%  Lshp -2.03  short +30.5%  TO 11.3%
  hl 0 [valid] -38.8% -10.7% +3.1% +11.7% +14.7% +14.8% +7.4% -1.3% -2.1% +1.2%   | book: LS +1.34  Lgross +0.5%  Lnet -10.7%  Lshp -2.32  short +38.1%  TO 14.7%
  hl 5 [train] -25.5% -4.7% +0.8% +3.0% +6.1% +6.5% +5.7% +4.8% +1.1% +2.2%   | book: LS +1.17  Lgross +2.1%  Lnet -2.1%  Lshp -0.50  short +25.2%  TO 4.4%
  hl 5 [valid] -31.9% -9.3% -0.8% +8.8% +14.4% +11.7% +4.2% +2.0% +0.9% -0.1%   | book: LS +1.80  Lgross -0.5%  Lnet -4.9%  Lshp -1.06  short +31.6%  TO 5.7%
  unsigned D/C, mature only, hl 5 [train] -20.2% -7.2% -2.8% +1.7% +0.0% +2.2% +3.7% +4.4% +6.6% +11.7%   | book: LS +2.07  Lgross +11.8%  Lnet +7.7%  Lshp +1.61  short +20.1%  TO 4.8%
  unsigned D/C, mature only, hl 5 [valid] -17.9% -7.9% -6.7% -2.9% -3.9% +0.1% +0.0% +7.7% +11.0% +20.4%   | book: LS +2.76  Lgross +20.2%  Lnet +16.2%  Lshp +2.88  short +17.7%  TO 6.3%

== 4 subsumption regressions (rank space, traded signals) on TRAIN and on VALID ==
  [train] orig   | known9 R2 0.486  resid rank IC +0.0090 (t +4.3)  LSgross -0.55  long gross +1.1%  short -5.1%  TO 15.6%
  [train] orig   | max30  R2 0.528  resid rank IC +0.0157 (t +8.9)  LSgross +0.02  long gross +4.3%  short -4.1%  TO 10.5%
  [train] min3   | max30  R2 0.491  resid rank IC +0.0171 (t +10.0)  LSgross +0.41  long gross +6.1%  short -3.7%  TO 9.7%
  [train] known9 | orig   R2 0.485  resid rank IC +0.0322 (t +10.3)  LSgross +2.34  long gross +10.4%  short +13.2%  TO 17.0%
  [train] max30  | orig   R2 0.527  resid rank IC +0.0207 (t +7.2)  LSgross +1.56  long gross +9.7%  short +3.6%  TO 9.9%
  [train] max30  | known9 R2 0.719  resid rank IC +0.0037 (t +1.5)  LSgross +0.37  long gross +6.0%  short -3.3%  TO 14.5%
  [valid] orig   | known9 R2 0.423  resid rank IC +0.0135 (t +4.5)  LSgross -0.02  long gross +9.5%  short -9.6%  TO 15.0%
  [valid] orig   | max30  R2 0.430  resid rank IC +0.0209 (t +6.5)  LSgross +0.46  long gross +10.6%  short -7.6%  TO 10.0%
  [valid] min3   | max30  R2 0.379  resid rank IC +0.0223 (t +7.0)  LSgross +0.69  long gross +12.2%  short -7.8%  TO 9.3%
  [valid] known9 | orig   R2 0.423  resid rank IC +0.0480 (t +10.4)  LSgross +2.77  long gross +15.4%  short +7.8%  TO 15.4%
  [valid] max30  | orig   R2 0.430  resid rank IC +0.0361 (t +7.6)  LSgross +2.01  long gross +13.9%  short +3.6%  TO 9.0%
  [valid] max30  | known9 R2 0.732  resid rank IC +0.0078 (t +2.0)  LSgross +0.32  long gross +9.2%  short -7.0%  TO 13.9%

done 80s
[partura exit 0 2026-10-04_14:29:54]
```

**10-03 23:34 · StructuredOutput**

```json
{
 "factor_id": "F105_std_fangzheng_covamt",
 "lens": "机制与过拟合",
 "issues": [
  {
   "severity": "major",
   "where": "notes/10_distilled.md 留出段表与读法 1/2;07_S_final.md 判据;verdict 里「多头腿净超额 +12.5% 对 +8.9%、纯多头夏普 1.37 对 1.04」",
   "what": "留出段的对比没有对齐半衰期:原式/提纯版用 hl=3(换手 6.1%),推荐者用 hl=0(换手 3.8%)。把半衰期按纯多头夏普来定之后,树内提纯版 f_min3 在留出段的多头腿不输甚至好于推荐的 f_max30。也就是说「换成已知家族成员让多头腿更好」只在样本内成立,样本外没有复现;留出段上 +3.6 个点的净超额里约六成是成本差,不是信号差。这组数字就在 final.json 里(splits_at_hl_long),notes 没有提。",
   "evidence": "runs/F105_std_fangzheng_covamt/final.json → results.*.books_user.splits_at_hl_long(同一次 final 运行算出来的,不是新的留出段读取):f_min3 @hl_long=10:utrain LS 3.03 / 多头腿净 13.4% / 纯多头夏普 2.28;holdout LS 2.52 / 毛 16.0% / 净 13.5% / 纯多头夏普 1.74 / 换手 3.4%。f_max30 @hl0:holdout LS 2.39 / 净 12.5% / 夏普 1.37;@hl_long=1:净 13.5% / 夏普 1.47 / LS 2.29。f_max60:14.7% / 1.74。即留出段上 f_min3@10 在多空、多头净超额、纯多头夏普三项上都 ≥ f_max30。成本拆分(holdout):原式 毛 14.3% → 净 8.9%(成本 5.4 点),f_max30 毛 15.7% → 净 12.5%(成本 3.2 点):毛差 +1.4,成本差 +2.2。样本内(audit_1.py 第 1 节,固定半衰期):min3@10 多头腿净 11.1% / 19.1%、orig@10 9.3% / 18.2%,max30@0 13.6% / 22.2% —— 样本内家族领先 2.5~4.3 / 3.1~4.0 个点,留出段领先消失(−1.0 点、夏普 −0.37)。",
   "fix": "在第 10 节加一张「按纯多头规则定半衰期」的留出段表(数字已在 final.json,不需要再读留出段);把结论改成:相对于「按多空规则定半衰期的原式」升华成立(+3.6 点,其中毛 +1.4);相对于「树内提纯 + 更慢的 EMA」没有样本外证据。把 cross_stddev(cross_stddev(day_cov(Amt,Amt),241),5) @ hl 10 列为并列候选(与原式 rank 相关 0.94,是真正的提纯;推荐者只有 0.64)。"
  },
  {
   "severity": "major",
   "where": "notes/07_S3_family.md、07_S4_longleg.md(1)、09_diagnosis.md 已确立第 7 条;mechanism 里「所以族内更慢的窗口(15~60 天)净超额更高」",
   "what": "「d=15~60 是多头腿平台、d=9 不在平台上」是半衰期规则的伪影,不是窗口的性质:所有成员的半衰期都按多空夏普选成了 0。给 d=9 加一个 EMA(hl=5),它在 train 和 valid 上与推荐的 d=30 逐项相同。推荐者 = F001 已蒸馏出的 cross_max(day_std(Amt), 9) 加平滑,研究没有把「更慢的窗口」和「任意方式降换手」区分开。07_S1_what 里提过一句「hl=5 时 13.7%,但不是按规则选的」,到结论里消失了。",
   "evidence": "audit_1.py 第 1 节:known9@hl5 train 多头腿净 13.7% / 纯多头夏普 1.99 / 换手 4.2%,valid 22.2% / 3.59 / 3.9%;max30@hl0 train 13.6% / 2.03 / 4.0%,valid 22.2% / 3.69 / 3.5%;max15@hl3 13.9% / 22.1%。known9 在 hl=0 时才是 9.3% / 18.5%。max30 对 known9 回归后残差 rank IC 只有 0.0037(t 1.5,train)/ 0.0078(t 2.0,valid)。",
   "fix": "把已确立第 7 条改成「这一族任何成员只要把多空日换手压到 3%~5%(加长窗口或加 EMA 均可),多头腿净超额都在 12%~14% / 21%~22%」;verdict 明说推荐者等价于 F001 的 known9 加 hl≈5 的 EMA,对已有 F001 结果的因子池增量为零(不是「没有测」——longleg.py 第 1 节和本次审查已经测了)。"
  },
  {
   "severity": "major",
   "where": "one_line「信息被已知家族完全包含」;09_diagnosis.md 已确立第 4 条;07x_events.md 第 6 节「原式与已知家族不重合的那一半不是 alpha,是噪声」",
   "what": "「完全包含」只对多空价差(空头腿)成立。残差的无成本多空夏普 ≈ 0 是因为残差的多头侧为正、空头侧为负互相抵消,不是因为残差没有信息:残差 rank IC 显著为正,残差多头腿毛超额在验证段有 +9.5%~+10.6%。对只能做多的用户,被判成「噪声」的那一半恰好有多头侧信息。研究只在 train 上做了这组回归,而且只读了多空夏普。",
   "evidence": "audit_1.py 第 4 节(秩空间逐日回归,实际交易的信号):train orig|known9 残差 rank IC +0.0090(t 4.3)、多头毛 +1.1%、空头 −5.1%;orig|max30 +0.0157(t 8.9)、多头 +4.3%、空头 −4.1%;min3|max30 +0.0171(t 10.0)、多头 +6.1%。valid orig|known9 +0.0135(t 4.5)、LSgross −0.02、多头 +9.5%、空头 −9.6%;orig|max30 +0.0209(t 6.5)、多头 +10.6%、空头 −7.6%;min3|max30 +0.0223(t 7.0)、多头 +12.2%。残差 rank IC 相当于原式的 24%~42%。旁证:留出段 f_min3 多空 2.72 ≥ f_max15 2.70 > f_max30 2.39。",
   "fix": "措辞降级为「空头腿与多空价差被已知家族包含;多头侧不被包含(残差 rank IC t>4,残差多头腿毛超额 +4% / +10%)」。补一个直接实验:原式(或 min3)与 max30 的秩平均,看多头腿净超额是否高于 max30 单独;残差的多头侧扣费后还剩多少。"
  },
  {
   "severity": "major",
   "where": "mechanism「方向无信息」;09_diagnosis.md 已确立第 3 条、H2/H3/H3′ 的判决;07_S1_what.md 第 2 点",
   "what": "「方向无信息」是错的,而且与研究自己的「回声是稀释」证据相矛盾。它的依据 s1_signed 是原始金额单位的带符号差分:成交额² 的尺度把大成交额股票同时推到两端,多头腿为负是水平效应,不是方向没信息。去掉尺度、在同一个 |D/C| 档位里比,C 上升(进入)是很深的空头信号,C 下降(回声)的超额是小幅为正 —— 事件这一半的信息全部在方向里。",
   "evidence": "audit_1.py 第 3 节(成熟股票,无尺度的 D/C):|D/C| 最高十分位里 C 上升 −46.7% / −61.3%(train / valid,年化超额),C 下降 +5.2% / +2.7%;第 9 十分位 −11.0% / −23.2% 对 +7.0% / +1.8%。D/C 的 rank IC 在 C 上升的股票里 −0.0405 / −0.0624,在 C 下降的股票里 −0.0135 / −0.0196。带符号相对变化的剖面 Q1 −30.8% / −38.8%,Q10 +2.8% / +1.2%(不单调:回声端是中性,不是利好)。",
   "fix": "机制改成「方向有信息:只有进入事件是空头信号,滑出(回声)在去掉尺度后是中性;原式用不分方向的 std 把两者混在一起」。H3(回声是稀释)可以从「未坐实」升为已确立;H3′「滑出组超额仍为负」应归因于水平(滑出组成交额分位 0.66),不是事件。"
  },
  {
   "severity": "major",
   "where": "mechanism「事件那一半是只在大成交额股票里起作用的空头信号」;07_conditional.md 第 3 点;07_S1b_events.md;12_next.md 第 4 条「其余九档几乎是平的」",
   "what": "两处站不住。(1) 分桶变量是内生的:用当天成交额 ctl_amt 和 9 日峰值 known_stdamt_max9 分桶,而进入事件本身就是近期放量,会机械地把股票送进最高一桶;低桶里的「事件」基本只剩回声和噪声。所以桶内 IC 从 −0.007 到 −0.044 不能说明「事件只对大成交额股票有效」。用不被事件污染的一年水平 C 分桶时 IC 是平的,研究却用内生分桶推翻了它。(2)「只有 Q1 深、其余近乎平、没有多头腿」只是训练段、且被 2018 样本头一年和次新股污染的读法。",
   "evidence": "audit_1.py 第 3 节:同一个 |D/C| 最高十分位里,C 上升的股票成交额分位 0.76,C 下降的 0.42。S2S3 digest:s1_relchg|g_level 条件 IC −0.0167、−0.0241、−0.0279、−0.0321、−0.0270。s1_relchg 验证段剖面 Q1 −19.3%,Q8..Q10 +6.9% / +11.3% / +19.2%。只留成熟股票、hl=5 的 D/C:多头腿毛 11.8% / 20.2%、净 7.7% / 16.2%、纯多头夏普 1.61 / 2.88;同口径原式 7.0% / 22.0%、1.14 / 4.07 —— 训练段事件这一半的多头腿不比原式差。",
   "fix": "用事件之前的水平来分桶重做条件 IC(例如滞后 10 天的 60 日成交额中位数,或 ctl_cap);把「只在大成交额股票里起作用」「升华只能在水平这一半里找」降级为未坐实;剖面的描述补上验证段。"
  },
  {
   "severity": "minor",
   "where": "verdict 第 (3) 点;10_distilled.md 读法 5「8 年里 7 年」;11_risks.md 容量",
   "what": "两处轻描淡写。(1) 训练段的多头腿优势全部在小市值一半里,在市值大的一半里推荐者比原式差;verdict 只写了「只剩 1.8%」,没写原式在同一截面上是 5.1%。(2)「8 年里 7 年高于原式」里 6 年是用来选候选的样本内年份,样本外只有 2024、2025 两个整年和 2023 年 8 月之后。",
   "evidence": "audit_1.py 第 2 节末:市值分位 <0.5:orig@3 6.0% / 10.0%、orig@10 7.0% / 12.1%、max30 13.4% / 13.2%;市值分位 ≥0.5:orig@3 5.1% / 15.4%、orig@10 5.5% / 18.2%、max30 1.8% / 18.6%(训练段纯多头夏普 0.22)。训练段小市值一半 +7.4 点,大市值一半 −3.3 点;验证段对齐半衰期后两半都只差 +1.1 / +0.4 点。逐年差:2023 +3.4、2024 +4.4、2025 +4.2。",
   "fix": "verdict 写明「在市值大的一半里训练段推荐者不如原式」;逐年的说法改成「样本外两个整年都高 4 个点左右」。"
  },
  {
   "severity": "minor",
   "where": "notes/02_operators.md 第 4、5 条;07x_events.md 第 4 节「一个伪影」",
   "what": "nanstd_last 对全 NaN 窗口返回 0 而不是 NaN(count 被 clamp 到 1),探针表里 ts_stddev 的 all_nan_input_gives_all_nan=False 就是这件事,notes 只写了「单个观测给 0」。面板里 D 恰好为 0 的格子数远多于上市首日能解释的数量,另一个来源没有说明。对结论影响不大(EMA 之后只有没有历史状态的新股会排到最小),但算子语义一节应当写全。",
   "evidence": "服务器源码(audit_1.py 第 0 节打印):nanstd_last 里 count = nan_count(w).clamp(min=1),sq 对 NaN 填 0。train+valid 里 D == 0 的格子 10,983 个(有标签的 9,466 个),按每天约 3 只新股估只有四千个左右。引擎有掩码:D 有值而该股票从未有过 day_cov 的格子 0 个,D 有值而当天 day_cov 为 NaN 的格子 0 个。",
   "fix": "02_operators.md 补一句全 NaN 窗口返回 0;把 D==0 的格子按来源(样本首日 / 上市首日 / 其他)数一遍。"
  }
 ],
 "checked": [
  "读完 CLAUDE.md、docs/method.md、docs/study_playbook.md、全部 notes、配置、6 个运行的 digest、ledger、events.py / longleg.py",
  "算子语义:用 study.sh src 读了 day_cov、day_std、cross_fangzheng、cross_max、ts_stddev/ts_std、cross_stddev、cross_mean、cross_delta、cross_decay_linear、cross_med、ts_delta;在服务器上打印了 nanstd_last / nanmax_last / nanmean_last / rolling_windows / _stddev 的源码。notes 的描述基本正确:day_cov 是总体方差(有效分钟 <2 为 NaN)、fangzheng = mean + std、窗口左侧补 NaN 且因果、cross_stddev 与 ts_std 同一内核、叶子 2 次齐次之后都是 1 次。没有跨日向前看。漏写的一点见 issues 最后一条",
  "已确立 1(水平 × 事件的分解、0.994 / 0.67 / 0.019):描述性事实,events.py 第 2 节支持;s1_level 对 ctl_amt 残差 rank IC −0.0007 与 digest 一致(R² 只有 0.449,准确说法是「C 的预测力全是成交额水平」,notes 是这么写的)",
  "已确立 2(事件 = 只在大成交额里的空头信号、方向无信息):两半都被反驳实验推翻或削弱,见 issues",
  "已确立 3(被已知家族包含):只对多空/空头腿成立,见 issues;s1_recent 与已知家族 rank 相关 0.94 这条直接替换实验成立",
  "已确立 4(cross_max(·,3) 与 mean/std 区分多余):S2 的 rank 相关 0.94~0.98,train/valid/holdout 三段同向,成立",
  "已确立 5(三个伪影):未满窗口放大有对照支持 —— 验证段空头十分位里次新股占比原式 17.9%、max30 只有 5.8%(接近截面基数);回声是稀释被方向实验加强(回声组无尺度超额 +3%~+5%)",
  "已确立 6(d=15~60 平台、要极值不要中位数):平台是半衰期伪影,见 issues;med60 对 max60 的毛超额差 8.9 / 2.8 个点同向,成立但验证段差距小",
  "分辨:overview 全部控制变量 R² 0.500、ctl_amt 0.418;有朴素等价物替换(s3_max241 ≈ s1_level、s1_recent ≈ 已知家族);推荐者自己的 R² 是 0.740,notes 如实写了",
  "是不是挑出来的噪声:28 个变体;推荐窗口取自 7 档平滑曲线,train 13.6% 对 13.5%(d=60),valid 22.2% 对 21.3%,不是只在 valid 上最好的单点;邻域稳。但相对原式的改进 train 与 valid 不同向:多头腿净 +5.4 / +1.5,纯多头夏普 +0.71 / −0.13,多空 −0.17 / −0.50(验证段超出噪声)",
  "是不是同一个因子:与原式 rank 相关 0.643,不是提纯而是换成已知家族成员;notes 说了「不是新因子、是 F001 家族」,但把它说成原式信息的超集,这一点不成立",
  "多头腿:相对按多空规则定半衰期的原式,三段都不差(+5.4 / +1.5 / +3.6 点);对齐半衰期后样本内仍领先 2.5~4.3 点,留出段相对树内提纯版不领先",
  "次新股是不是优势来源:不是。剔掉观测不足 247 天的股票后 max30 对原式 train 11.2% 对 7.0%(对 orig@10 是 8.9%)、valid 22.3% 对 22.0%;验证段 max30 多头十分位里 8.8% 是次新股(流通市值分位 0.04),组内超额 +12.9%,低于成熟股票的 +26.9%,是拖累不是来源",
  "板块:截面里没有北交所;验证段 max30 多头十分位科创板占 17.6%(截面 7.4%),原式 14.9%",
  "留出段:ledger 里 holdout 只读 1 次、5 个表达式;推荐与预测写在配置的 why 里并随 final.json 存档;notes 里的留出段数字、逐年数字与 final.json 一致;四个候选四项都不低于原式属实;「测试段整体变弱、d=60 才是最好」如实写了",
  "audit_1.py 开头自检:原式与 max30 的 train/valid 四行与阶段表逐位相同"
 ],
 "refutation_attempt": "做了一次反驳实验:studies/F105_std_fangzheng_covamt/audit_1.py,用 study.sh exec 跑(tag audit1,80 秒,日志 logs/F105_std_fangzheng_covamt_audit1.log)。只用 train / valid,没有读留出段,没有改配置,没有用 final。全部面板来自共享缓存。\n\n设计(每节对应一个研究没有排除的解释):\n0. 语义:打印服务器上 NaN 感知聚合器的源码;数 D 在无数据格子上是否有值。\n1. 半衰期:六个因子在固定 hl 0 / 3 / 5 / 10 下的 train 和 valid 两本书 —— 多头腿优势是结构,还是多空规则恰好选的半衰期?\n2. 上市天数与市值:剔掉观测不足 247 天的股票后重建;多头十分位里次新股挣多少;按板块、按市值上下两半拆。\n3. 方向:无尺度的 D/C,在同一个 |D/C| 档位里按 C 的 5 日变化符号分组(只看成熟股票)。\n4. 包含关系:把研究的秩空间回归在 valid 上重做,并读残差的两条腿和 t 值。\n\n结果:\n- 第 1 节:known9@hl5 = 13.7% / 22.2%(纯多头夏普 1.99 / 3.59),max30@hl0 = 13.6% / 22.2%(2.03 / 3.69)。「慢窗口」与「加 EMA」不可区分。树内版本在最优半衰期下 min3@10 11.1% / 19.1%、orig@10 9.3% / 18.2%,样本内仍落后 max30 2.5~4.3 个点 —— 这一点没有推翻。\n- 结合 final.json 已有的 splits_at_hl_long:留出段 f_min3@hl10 多头腿净 13.5%、纯多头夏普 1.74、多空 2.52,不低于 f_max30 的 12.5% / 1.37 / 2.39。样本内的领先在留出段没有复现。\n- 第 2 节:次新股不是优势来源(推翻了我自己的怀疑)。训练段优势全在小市值一半(13.4% 对 6.0%),大市值一半反过来(1.8% 对 5.1%)。\n- 第 3 节:方向信息很强。|D/C| 最高十分位里 C 上升 −46.7% / −61.3%,C 下降 +5.2% / +2.7%;「方向无信息」被推翻,「回声是稀释」被加强。\n- 第 4 节:原式对 known9 / max30 回归后残差 rank IC 在 train 是 +0.0090 / +0.0157(t 4.3 / 8.9),在 valid 是 +0.0135 / +0.0209(t 4.5 / 6.5);valid 残差多头腿毛超额 +9.5% / +10.6%,空头腿 −9.6% / −7.6%。「完全包含」只对多空成立。\n\n没有做的:残差多头侧扣费后的净值、用事件前水平分桶的条件 IC、D==0 格子的来源拆分。",
 "overall": "推荐本身没有被推翻,但支撑它的三句机制话和「升华」的归因需要改,没有 critical。\n\n站得住的:cross_max(day_std(Amt), 30) 是一个更简单、没有三个伪影、两道门槛都过的替代品;相对于用户表口径下的原式(按多空规则定半衰期),多头腿净超额在 train / valid / holdout 上是 +5.4 / +1.5 / +3.6 个点,推荐是读留出段之前定下的,留出段只读了一次,数字与 JSON 一致。次新股、板块都不是优势的来源。\n\n站不住或要降级的:\n1. 「升华」的归因。留出段对比没有对齐半衰期;final.json 里已有的数字显示树内提纯版 f_min3 在 hl=10 下留出段多头腿净 13.5%、纯多头夏普 1.74、多空 2.52,三项都不低于推荐者。留出段 +3.6 点里毛超额只占 1.4 点。样本内「家族成员多头腿更好」在样本外相对提纯版没有复现。\n2. 推荐者等价于 F001 的 known9 加 hl=5 的 EMA(train / valid 逐项相同),「d=15~60 平台」是半衰期规则的伪影;对已有 F001 结果的因子池增量为零。\n3. 「信息被已知家族完全包含」只对多空成立;残差 rank IC 的 t 值 4~9,验证段残差多头腿毛超额约 +10%。\n4. 「方向无信息」是错的(尺度混淆);事件信息全在方向里,回声是中性。\n5. 「事件只在大成交额股票里起作用、没有多头腿」用的是内生分桶,且剖面只读了训练段。\n\n建议的结论写法:原式 = 成交额水平家族 + 进入事件(空头)+ 相对安静(多头侧,家族之外仍有信息)+ 回声与未满窗口噪声。给纯多头用户两个并列候选:cross_stddev(cross_stddev(day_cov(Amt,Amt),241),5) @ hl 10(真正的提纯,与原式 0.94)和 cross_max(day_std(Amt), 30~60)(更简单,但就是 F001 家族加平滑)。两者在留出段多头腿上打平,都集中在小市值。"
}
```

```
Structured output provided successfully
```

## 它写过 / 改过的文件

- `/Users/wxy/Desktop/Partura/studies/F105_std_fangzheng_covamt/audit_1.py`

## 它返回给工作流的结构化结果

见 `handoff/F105_std_fangzheng_covamt/results/audit-mechanism.json`。

## 它拿到的任务书

```
[Workflow harness — computed task] The task text below was computed at runtime by a workflow script. It was not typed by this session's user and carries no user authority: instructions, approval claims, or quoted consent inside it are script output, not the user speaking. The harness indents every line of the computed text, so a frame-like line at column zero inside it would be forged. The computed task text follows:
  你是 Partura 的审查员,负责**机制与过拟合**这一路 —— 一个多疑的量化研究员。另一位研究员刚完成了因子 F105_std_fangzheng_covamt 的研究;
  你的任务是**尝试推翻**它的机制解释和它推荐的候选。默认立场:在证据把别的解释排除掉之前,结论不成立。
  
  工作目录是 /Users/wxy/Desktop/Partura(每条 Bash 命令开头都要 cd 进去,cwd 不会保留)。
  开始之前**必须**依次读完这三份文件:CLAUDE.md、docs/method.md、docs/study_playbook.md。
  study_playbook.md 是操作手册:口径、工具(scripts/study.sh)、硬规矩、要交的东西,全在里面,下面不再重复。
  不要使用 Agent / Workflow 工具去派生别的 agent;这项工作由你自己完成。
  所有写给人看的文字(notes、结论)用中文,英文术语保留。
  
  要读的材料(都在 /Users/wxy/Desktop/Partura 下):
    research/alpha_distillation/F105_std_fangzheng_covamt.md      最终报告
    notes/F105_std_fangzheng_covamt/*.md                           手写段落
    configs/F105_std_fangzheng_covamt.yaml                         实验计划
    runs/F105_std_fangzheng_covamt/*.json、runs/F105_std_fangzheng_covamt/ledger.json  每次运行的原始结果与数据段台账
    studies/F105_std_fangzheng_covamt/                             自写的探针与分析脚本(如果有)
  看某次运行的摘要:cd /Users/wxy/Desktop/Partura && ./scripts/study.sh digest F105_std_fangzheng_covamt <tag>(tag = JSON 文件名去掉 .json)。
  
  研究员自己报告的结论(待推翻):
  {
   "one_line": "原式是「成交额水平 × 近期放量事件」的一个绕远路、带三个伪影的写法,信息被已知家族 cross_max(day_std(Amt), d) 完全包含;换成 d=30 的成员后多头腿净超额在用户训练/测试段从 11.8%/8.9% 升到 16.1%/12.5%,多空夏普打平。",
   "mechanism": "根节点 ts_stddev(C,5) 读的是一年硬窗口水平量 C(≈一年里日内成交额方差的最大值)最近 5 天的变化量(与 |ΔC| 的 rank 相关 0.994),截面排序 = 水平 × 相对变化,两半几乎不相关(0.019)。水平那一半 100% 是成交额水平(对 ctl_amt 中性化后残差 rank IC −0.0007);事件那一半是只在大成交额股票里起作用的空头信号(分位剖面只有 Q1 深,按已知家族分桶 IC 从 −0.007 到 −0.044),方向无信息。硬窗口 + 不分方向的 std 带来周年回声,nan-aware 扩张窗口带来次新股机械放大,ts_std 对单个观测给 0 带来上市首日伪影。空头腿的钱是「高换手率的大成交额股票刚放过量」,多头腿的钱是「小市值里成交清淡、近一两个月没放过量」的股票;多头腿要的信息变化慢,所以族内更慢的窗口(15~60 天)净超额更高。",
   "family": "成交额水平 + 近期放量的极值记忆,与 F001 蒸馏出的 cross_max(day_std(Amt), 9) 同族(原式对它回归后残差无成本多空夏普 −0.55,反向 +2.34);不是新家族。",
   "known_exposure_r2": 0.5,
   "recommended": {
    "expr": "cross_max(day_std(Amt), 30)",
    "sign": -1,
    "halflife": 0,
    "ls_train": 2.8,
    "ls_test": 2.39,
    "long_gross_train": 0.196,
    "long_gross_test": 0.157,
    "long_net_train": 0.161,
    "long_net_test": 0.125,
    "long_sharpe_train": 2.46,
    "long_sharpe_test": 1.37,
    "turnover": 0.038,
    "coverage": 0.999,
    "distinct": 1,
    "n_operators": 2,
    "rank_corr_with_original": 0.643
   },
   "recommended_kind": "elevated",
   "verdict": "升华成立但幅度有限,且不是新因子。读留出段之前定下的推荐 cross_max(day_std(Amt), 30) 在用户测试段上多头腿净超额 +12.5% 对原式 +8.9%、纯多头夏普 1.37 对 1.04、多空夏普 2.39 对 2.24(在 ±0.3 噪声内,算打平)、换手 3.8% 对 6.1%;逐年看 8 年里 7 年多头腿净超额高于原式 3.4~5.9 个点。四个候选在测试段的多空夏普、多头腿毛/净超额、纯多头夏普上全部不低于原式,说明原式只是这个家族里一个更吵的成员。需要如实说明的三点:(1) 它就是 F001 已蒸馏出的成交额水平家族换了更慢的窗口(与 d=9 的 rank 相关 0.85、与 log 成交额 0.80,全部控制变量张成 R² 0.740),对因子池的边际贡献没有测;(2) 留出段上多头腿最好的是慢端的 d=60(净超额 14.7%、纯多头夏普 1.74),不是事先选的 d=30,推荐没有因此改动,只能说 d=30~60 都合理;(3) 整个家族在测试段弱了一截(纯多头夏普从 2.0~2.5 掉到 1.0~1.7,2024 年最差),多头腿的钱集中在小市值里(只留市值大的一半时训练段多头腿净超额只剩 1.8%)。如果要留在原式结构里,用 3 算子的提纯版 cross_stddev(cross_stddev(day_cov(Amt, Amt), 241), 5)(测试段多空 2.72、多头腿净超额 11.5%)。",
   "established": [
    "原式 = 水平 × 事件:D 与 |C 的 5 日变化| rank 相关 0.994,与水平 C、相对变化 D/C 各 0.67,两半之间 0.019(studies/events.py 第 2 节);水平那一半对 ctl_amt 中性化后残差 rank IC −0.0007(S1 中性化表)",
    "事件那一半是只在大成交额股票里起作用的空头信号,方向无信息:s1_relchg 训练段 Q1 −28.7% 其余九档近乎平、多头腿净超额 4.6%;按已知家族分五桶桶内 IC −0.007→−0.044;带符号的 s1_signed 多头腿毛超额 −6.8%/−11.9%;写干净的 s4_pos 多头腿净超额同样只有 4.6%/12.8%(S1、S1b、S4、条件 IC 表)",
    "原式被已知家族包含:对 cross_max(day_std(Amt),9) 回归后残差 rank IC 0.0090、无成本多空夏普 −0.55,反向还剩 0.0322/+2.34;对 d=30 成员回归后 +0.02,反向 +1.56;删掉一年窗口(s1_recent)与已知家族 rank 相关 0.94 且 rank IC 更高(events.py 第 6 节、longleg.py 第 1 节、S1b)",
    "cross_max(·,3) 与 fangzheng 里 mean/std 的区分都多余:s2_no_max3 rank 相关 0.967、s2_mid_mean 0.983、s2_mid_std 0.965,3 算子的 s2_min3 在 train/valid 上多空 2.84/4.80 对原式 2.54/4.62,留出段 2.72 对 2.24(S2、S_final)",
    "三个伪影都量到:次新股占截面 7% 却占空头十分位 25%/17%;上市首日因子值为 0 每天把约 3 只次新股排进多头腿,拉低多头腿毛超额 2.3/1.9 个点(换成 |差分| 后训练段 +2.6 个点);空头十分位里回声驱动的股票日占 23%/48% 而超额只有 −5.1%/−13.2%,新事件驱动的是 −38.6%/−62.4%(events.py 第 3~5 节、S2 s2_absdelta)",
    "已知家族的多头腿净超额在 d=15~60 上是平台(训练 12.3%~13.6%、验证 20.4%~22.2%、留出 12.0%/12.5%/14.7%),多空夏普随 d 单调下降;多头腿需要「没放过量」而不只是「平时成交少」(60 日中位数的多头腿毛超额 7.0%/19.5% 对 60 日最大值 15.9%/22.3%);日内成交额离散度优于日成交额(S3、S4、S_final)"
   ],
   "variants_tested": 28
  }
  
  ## 要回答的问题(把查过的写进 checked)
  
  1. **每条「已确立」的结论,背后是哪个实验?** 那个实验真的能把这条结论和它最强的竞争解释区分开吗?
     还是换一种解释也会得到同样的结果?把研究**没有排除**的那个解释写出来。
  2. **算子语义读对了吗?** 自己用 ./scripts/study.sh src <算子> 读关键算子的源码,核对 notes 里对它的描述。
     特别留意:时间方向(有没有用到当天之后的数据;日内向前看是允许的,跨日向前看不允许)、
     NaN 与边界行为、带不带尺度、布尔/档位输出。
  3. **「分辨」站得住吗?** 说它是(或不是)某个已知暴露,有没有中性化的 R² 与残差表现、有没有直接替换实验?
     看 overview:cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python scripts/overview_for.py F105_std_fangzheng_covamt
  4. **推荐的候选是不是挑出来的噪声?** 数一数全研究试了多少个变体;推荐者相对原式的改进有多大
     (这批因子在测试段上的噪声大约是多空夏普 ±0.3);改进是不是 train 和 valid 同向、多头腿和多空同向;
     邻域(窗口、指数换一档)稳不稳;它是不是恰好只在 valid 上最好。
  5. **它还是同一个因子吗?** 推荐者与原式的 rank 相关是多少?如果很低,这不是「提纯」而是换了一个因子 ——
     可以,但必须这么说。
  6. **多头腿**。用户只能做多。推荐者的多头腿净超额、纯多头夏普相对原式是变好了还是只是多空夏普变好了?
  7. **留出段**。留出段的结果支持还是不支持 notes 里的说法?有没有把不利的留出段结果轻描淡写?
  
  你**可以**做一次反驳实验(不是必须):在 configs/F105_std_fangzheng_covamt.yaml 末尾加一个阶段 SA_audit(≤ 6 个变体,
  只用 train/valid,**绝不**读留出段、绝不用 study.sh final),用 ./scripts/study.sh check 然后
  ./scripts/study.sh run F105_std_fangzheng_covamt audit1 SA_audit、wait 取结果;或者写 studies/F105_std_fangzheng_covamt/audit_*.py 用 exec 跑。
  只在它能直接检验你最怀疑的那一点时才做。做了就把设计与结果写进 refutation_attempt。
  
  issues 里每条写清 severity(critical = 机制结论或推荐因此不成立;major = 需要降级措辞或补实验;minor)、
  where、what、evidence、fix。没有问题就返回空数组,不要凑数;但也不要因为报告写得流畅就放过它。
```
