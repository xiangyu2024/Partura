# F106_erm_mag_gap_1m — 研究现状(**自动汇编**,2026-10-04 13:10)

> 这一页不是研究员写的。上一位研究员(Opus 5.5,工作流 agent `study:F106_erm_mag_gap_1m`)在写下现状之前就被换下了;
> 协调者用脚本(`scripts/autostate.py`,不经过任何模型)把磁盘上**它写过的和做过的**汇编成这一页。
> 它当时怎么想的没有留下 —— 假设的最新状态、对结果的解读,需要接手的主研读下面列出的材料后**重写这一页**。

## 1. 一句话现状

- 配置里的一句话(研究员读完这棵树之后写的):分钟收益右尾 ES/VaR 减左尾 ES/VaR;分母 +1e-6 在「上涨(下跌)分钟不足 5%」的日子塌掉,截面两端由这些日子决定
- 已写 notes:01_expression.md、02_operators.md、03_decomposition.md、04_grammar.md、05_hypotheses.md、06_baseline.md、07x_1_anatomy.md
- 已拉回本地的运行:S0_baseline;已启动但**结果还没人读**的:S1_regime
- 留出段:未读

## 2. 中间结果(事实在这些文件里,还没有汇总)

- 运行 `S0_baseline`(10-04 11:50):`./scripts/study.sh digest F106_erm_mag_gap_1m S0_baseline`
- 自写分析 `x1` 的输出:`logs/F106_erm_mag_gap_1m_x1.log`

### 基线读数(原文照录 `notes/F106_erm_mag_gap_1m/06_baseline.md`)

**复现**:用户训练段(utrain)上 S0 给出方向 −、半衰期 20、扣费多空夏普 +2.91、多头腿毛超额 −4.2%,与公布的那一行(2.91 / −4.2%)一致。
两种口径选到的半衰期相同(多头口径 20、多空口径 20),所以这条因子**没有「换成多头最优半衰期」这条免费的改进** ——
「原式 + 多头最优半衰期」就是公布的那一行本身。

**多头腿(选拔口径)是负的,而且在每一个半衰期下都是负的**:

| 半衰期(train) | 0 | 2 | 5 | 10 | 20 |
|---|---|---|---|---|---|
| 多头腿净超额 | −67.2% | −32.5% | −18.5% | −10.6% | −6.9% |
| 纯多头夏普 | −19.51 | −9.93 | −5.82 | −3.26 | −2.15 |
| 多头日换手 | 88% | 37% | 17% | 7% | 2% |

决策口径下:多头腿净超额 train −6.9% / valid −3.2%,纯多头夏普 −2.15 / −1.23,多头腿**毛**超额也是负的(−5.1% / −1.8%)。
所以负的多头腿不是成本问题:把换手压到 2.4% 之后它仍然跑输等权。半衰期从 0 拉到 20 只是把亏损从「成本 + 选股」缩到「选股」。
半衰期 20 是网格的上边界,扫描在边界上仍在改善(−10.6% → −6.9%)—— 最优的记忆长度很可能在 20 以外。

**钱全在空头腿**:train 空头腿毛超额 +27.9%(valid +22.4%),多头腿毛超额 −5.1%(valid −1.8%);扣费多空夏普 +2.82 / +3.24 完全由空头腿撑起。

**分位剖面是倒 U,而且极不对称**(Q1 = 空头端 = X 的 EMA 最大的一档;Q10 = 多头端):

| | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 |
|---|---|---|---|---|---|---|---|---|---|---|
| train | −28.4% | +0.1% | +3.5% | +2.0% | +4.7% | +6.6% | +7.9% | +5.9% | +3.2% | −5.3% |
| valid | −22.7% | +3.5% | +10.2% | +2.6% | +2.6% | +5.4% | +1.3% | −1.2% | +0.1% | −1.8% |

一档(Q1)独自跑输 23~28 个点,其余九档里八档在 0~+10% 之间、多头端一档为负。这不是一个「信号越大越好」的排序:
它是「有一档很坏」。中间几档的正超额大体上只是「全市场均值扣掉那一档坏股票」之后的算术结果(九档平均 ≈ +3%)。

**Pearson IC 远大于 rank IC**:原始日频面板 train 的 Pearson IC 0.0316(ICIR 0.59),rank IC 只有 0.0067。预测力在取值的**量级**里
(也就是那些 10³ 以上的塌缩值),不在排序的中段 —— 与 `03_decomposition.md` 里「两端由塌缩日决定」的推断一致。
平滑之后实际交易信号的 rank IC 是 0.0165 / 0.0086(train / valid)。

**逐年**(utrain 内,多空口径):2018 +1.82、2019 +4.17、2020 +3.25、2021 +2.33、2022 +3.22、2023 +3.31,年年为正;
多头腿净超额年年为负(−9.2%、−6.2%、−8.6%、−4.1%、−0.8%、−7.4%)。

**衰减**:rank IC 随持有期上升(h1 0.0165 → h5 0.0247 → h20 0.0338)。信号是一个慢变量:今天排在空头端的股票,二十天后还在跑输。

**条件 IC**:按成交额分桶,IC 随成交额上升(0.0039 → 0.0330);按市值分桶,小市值里更高(0.0214 → 0.0082)。
即「成交活跃的小票」里最有效 —— 与「空头端是被炒作的票」的读法相容,但这两个分桶变量与因子本身的关系要另量(`07x_1_anatomy.md`)。

**门槛**:cov 1.00、dist 0.99,两道都过。


### 已写的阶段结论(原文照录 `notes/F106_erm_mag_gap_1m/07x_1_anatomy.md`)

### x1:这棵树在真实数据上读到的是什么(`studies/F106_erm_mag_gap_1m/x1_anatomy.py`,tag `x1`;只用 utrain)

脚本先做了三个自检:探针在服务器内核上全部通过;用零件重算的 R − L 与整棵树的最大相对差 9.8e-4;
原式的方向 −、多头半衰期 20、train 多头腿净超额 −6.9%,与 S0 一致。

**A. `Ret` 是什么**(决定 H5 的生死)

- 每个有值的股票-日都是 241 个有效分钟(100.00%),所以分位数永远恰好是一个顺序统计量,没有插值造成的过渡区间。
- **第一个分钟的 `Ret` 在 100% 的股票-日上恰好是 0** —— `Ret` 不含隔夜跳空。`day_sum(Ret)` 与「收盘/开盘 − 1」的相关 0.9989、
  中位绝对差 0.027%;与「收盘/昨收 − 1」的相关只有 0.8985、中位绝对差 0.42%。
- 去掉第一个分钟重算整棵树,在常规日上与原式的日截面 rank 相关 0.999。
- **H5(常规区间读的是隔夜跳空)被杀死**:第一分钟不可能落在尾部。这棵树是纯日内的。

**B. 三个区间在真实数据上各占多少、各是什么日子**

| | 占全部股票-日 | 涨停收盘占比 | 跌停收盘占比 | 收盘价 < 3 元 | 成交额排名后 20% |
|---|---|---|---|---|---|
| 两侧都常规 | 99.40% | 1.2% | 0.6% | — | — |
| 右侧塌缩为主(X ≥ +500) | 0.32%(17,013 个) | **86.3%** | 6.6% | 0.2% | 10.8% |
| 左侧塌缩为主(X ≤ −500) | 0.14%(7,622 个) | **77.8%** | 16.0% | 0.2% | 10.1% |
| 边缘(5 ≤ \|X\| < 500) | 0.06%(2,957 个) | 56.2% | 24.6% | 0.1% | 18.6% |
| 全部股票-日的基准率 | | 1.59% | 0.67% | | 20% |

- X 的分位数:0.1% −3192、1% −1.18、5% −0.62、25% −0.149、中位 +0.056、75% +0.29、95% +0.82、99% +1.63、99.9% **+13814**。
  常规区间里 R 的中位数 1.573、L 的中位数 1.506(比高斯的 1.254 重尾),X 的四分位距只有 0.44。
- **塌缩日就是封板日**:八成左右是涨停收盘(基准率 1.6%,富集 50 倍),其余主要是跌停收盘。**H3 被支持**。
- **塌缩日不是低价/不活跃股票**:收盘价低于 3 元的只占 0.2%,成交额排名在后 20% 的只占 10% 上下(比随机的 20% 还少)。
  探针里「2~3 元的股票因为 tick 太粗而塌缩」在真实数据上基本不发生。**H4 被杀死**。
- 一字板(全天价格不动)**不在**塌缩日里:`Ret` 全为 0,两侧尾部集合都是空的,X 读 0,被归进「常规」。
  原式看不见一字板本身,只看得见「大部分时间封死、但有几分钟在动」的板。
- X 在封板日的符号取决于板是怎么封上的:几分钟拉到涨停然后封死(上涨分钟 ≤ 12 个)→ 右侧塌缩 → X ≈ +10⁴;
  一路缓涨到涨停、下跌分钟很少 → 左侧塌缩 → X ≈ −10³~−10⁴。两种都是涨停日。
- 塌缩日之后一天的表现(这些格子的次日超额,年化;可买入标签 / 不过滤的标签 / 次日开盘买不进的比例):
  只有右侧塌缩 −565% / −187% / 23.4%;两侧都塌缩 −332% / −264% / 8.0%;只有左侧塌缩 −201% / −184% / 5.3%;
  两侧常规 +1.8% / +1.4% / 2.0%。也就是 **封板日次日(能买进的那部分)每天跑输 0.8~2.2 个点**,不分 X 的正负。

**C. 实际交易的信号(EMA-20 的 −X)里,每一档是谁**(train)

- 28.5% 的格子 \|信号\| ≥ 5(仍被某个塌缩日统治);39.0% 的格子所属股票**从未**出现过塌缩日;最近一次塌缩日在 20 / 60 / 250 天以内的各占 8.3% / 19.6% / 46.2%。

| 档 | 信号中位数 | \|信号\|≥5 | 距上次塌缩日(中位,天) | 近 20 日有涨停 | 近 60 日有涨停 | 上市不满 250 日 | 市值秩 | 换手率秩 | 次日超额(可买入) | 次日超额(不过滤) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1(空头端) | −327.9 | 97.5% | 23 | 55.3% | 87.1% | 26.8% | 0.33 | 0.71 | **−28.5%** | −13.0% |
| 2 | −36.8 | 92.2% | 64 | 26.5% | 63.5% | 6.5% | 0.41 | 0.56 | −0.2% | −1.2% |
| 3 | −2.7 | 31.4% | 139 | 16.5% | 38.8% | 2.5% | 0.44 | 0.51 | +3.7% | +2.3% |
| 4~9 | −0.21~+0.03 | 0% | 从未(4 档:325) | 10~13% | 24~31% | 5~7% | 0.48~0.61 | 0.40~0.49 | +1.7%~+7.9% | −0.5%~+5.8% |
| 10(多头端) | +13.0 | 64.4% | 61 | 32.6% | 62.6% | 3.6% | 0.48 | 0.54 | **−5.2%** | −6.3% |
| 全市场 | | | | 19.7% | 41.1% | 7.4% | | | | |

- **两端都是「近期封过板的股票」**:空头端是最近(中位 23 天前)出现过「秒板」的小市值、高换手股票,其中四分之一是上市不到一年的新股;
  多头端是两个月前出现过「缓涨封板」的股票。中间六档是一年内没有任何塌缩日的股票,它们之间才是按常规区间的尾部不对称排的序。
- 把空头端再切细:信号最低的 1% 里 **95.2% 是上市不满 250 日的新股**(连续涨停期的 ES 把 EMA 顶到 −3.5 万),
  这一组用可买入标签是 −52.5%、用不过滤的标签是 **+86.4%**,7.9% 的格子次日买不进 —— 完全是口径造成的;
  1%~2% 一组 −55.6% / −51.1%,2%~5% 一组 −41.2% / −36.9%,5%~10% 一组 −11.1% / −10.7%,10%~20% 一组 −0.2%。
  多头端最高的 2% 是 −22.2% / −21.4%(其中 66.5% 近 20 日有过涨停),95%~98% 一组 −1.7%。
- 所以 **真正的跑输集中在信号两头各 2%~5% 的股票上,它们都是近期封板股**;倒 U 的两臂是同一类股票。**H6 被支持**。

**D. 事件时间:塌缩日之后第 k 天的超额(可买入标签,bp/天)**

| 事件 | 个数 | k=0 | 1 | 2 | 5 | 10 | 20 | 40 | 60 |
|---|---|---|---|---|---|---|---|---|---|
| 右侧塌缩且涨停收盘 | 14,680 | −172.2 | −56.0 | −47.4 | −19.5 | −10.3 | −8.2 | −0.1 | +0.1 |
| 右侧塌缩、非涨停 | 2,169 | −118.8 | −72.5 | −30.3 | −48.2 | +1.7 | +5.5 | +3.0 | +6.9 |
| 左侧塌缩且跌停收盘 | 1,221 | −90.9 | −61.1 | −47.2 | −2.2 | −6.0 | −3.7 | +1.2 | +2.0 |
| 左侧塌缩、非跌停 | 6,333 | −91.8 | −20.2 | −24.1 | −10.4 | −6.7 | +3.0 | −2.3 | +0.7 |
| **涨停收盘但 X 常规** | 62,438 | −69.2 | −29.2 | −29.9 | −16.5 | −11.1 | −10.0 | −4.5 | −1.9 |
| 跌停收盘但 X 常规 | 32,465 | −38.2 | −22.0 | −4.3 | −6.6 | +0.1 | +1.6 | −5.7 | +1.3 |

- 封板之后的跑输持续约 20 个交易日,40 天之后归零。而 EMA-20 把一个 10⁴ 的读数记上一年 —— **记忆长度比效应长一个数量级**,
  这就是 Q2、Q3、Q10 这些「几个月前封过板」的档位收益平平的原因。
- **没塌缩的涨停日事后同样跑输**(−69 bp、之后二十天每天 −10~−30 bp),而它们的数量是塌缩涨停日的四倍多(62,438 对 14,680)。
  原式只抓到了涨停日里「封得死」的那五分之一。

**E. 各种构造的两本书(numpy 版,fit = train;train / valid)**

| 构造 | 方向 | hlL | 多头腿净超额 | 纯多头夏普 | hlS | 多空夏普 | 空头腿(train) | 日频 rank IC | 与原式信号的秩相关 |
|---|---|---|---|---|---|---|---|---|---|
| 原式 X | − | 20 | −6.9% / −3.2% | −2.15 / −1.23 | 20 | +2.82 / +3.24 | +27.9% | 0.0067 / 0.0027 | 1.00 |
| 只留常规日(塌缩日置 0) | − | 20 | −12.0% / −9.7% | −2.49 / −2.45 | 20 | **−1.45 / −2.11** | +9.8% | 0.0036 / 0.0006 | 0.41 |
| 先截面排序再 EMA | − | 20 | −12.8% / −13.2% | −2.17 / −2.49 | 20 | **−0.93 / −1.40** | +14.7% | 0.0067 / 0.0027 | 0.48 |
| clip(X, ±3) | − | 20 | −10.7% / −9.3% | −2.28 / −2.37 | 20 | +0.80 / +0.13 | +25.6% | 0.0067 / 0.0027 | 0.61 |
| 只留右侧 R | − | 20 | −4.2% / −4.0% | −0.65 / −0.60 | 20 | +2.10 / +1.78 | +32.1% | 0.0135 / 0.0104 | 0.63 |
| 只留左侧 L | **−** | 20 | −8.2% / −3.4% | −1.60 / −0.60 | 20 | +1.61 / +1.76 | +27.5% | 0.0083 / 0.0087 | 0.19 |
| 任一侧塌缩的 0/1 标记 | − | 1 | +2.7% / +3.5% | +0.42 / +0.44 | 5 | +3.40 / +2.66 | +38.6% | 0.0320 / 0.0236 | 0.38 |
| 日线涨停标记(5/10/20% 板) | − | 0 | +2.1% / +1.9% | +0.33 / +0.19 | 1 | +3.09 / +3.73 | +51.2% | 0.0424 / 0.0319 | 0.06 |
| 多头 = \|EMA20(X)\| 最小 | (强制) | 20 | +2.4% / −6.0% | +0.34 / −0.88 | 2 | +2.07 / +1.05 | +26.8% | — | 0.56 |

- **去掉塌缩日(或抹掉量级),多空夏普从 +2.82 / +3.24 变成负的** → 常规区间的尾部形状不对称没有可交易的信号。**H1 被支持、H2 被杀死**。
- **L 单独用的方向也是 −**(L 越大越差),与 R 同向 → 「右减左」是在让两个同向的读数互相抵消。**H8 被支持**(两侧不是镜像)。
- 一个不带任何幅度的塌缩标记、乃至一个朴素的日线涨停标记,多空夏普就与原式相当或更高,日频 rank IC 是原式的 5~6 倍。
  (这些 0/1 构造的「多头腿」是并列里按股票代码顺序取的 10%,没有意义;它们过不了 dist 门槛,只用来分辨。)
- 上涨/下跌/零收益分钟占比这类「活跃度」读数的多头腿在 train 为负、valid 为正(−8.5% / +5.5% 等),是换手率/波动家族的制度性表现,不是这棵树的东西。
- 所有从这棵树派生出来的连续构造,**多头腿净超额在 train 和 valid 上没有一个同时为正**。

**F. 空头腿里有多少是「买不进的票」撑的**(原式信号,半衰期 20)

| | 空头腿(可买入标签) | 多空夏普 | 空头腿(不过滤标签) | 多空夏普 |
|---|---|---|---|---|
| train | +27.9% | +2.82 | **+12.5%** | **+0.42** |
| valid | +22.4% | +3.24 | +16.8% | +2.26 |

train 上空头腿 27.9 个点里有 15.4 个点来自「次日开盘封涨停、标签缺失、在空头里记 0」的票(主要是连板新股);
换成不过滤的标签,多空夏普从 2.82 掉到 0.42。valid 上掉 5.6 个点、夏普从 3.24 到 2.26。
**公布的多空夏普有一半以上(train)是口径造成的**;多头腿不受这个影响(不过滤标签下 train −6.1%、valid −1.4%,仍然为负)。

**G. 折叠之后是不是已知暴露**(train,日截面 rank 相关 / 秩空间 R²)

信号到截面中位的距离(折叠量)与「近 20 日塌缩日密度(EMA)」的 rank 相关 +0.615,单变量 R² 0.384;
与价格、成交额、市值、换手率、日内波动五个控制变量合起来的 R² 只有 0.068(加上塌缩密度后 0.398)。
带符号的信号对塌缩密度的 R² 是 0.166。也就是说:折叠量的近四成就是「最近封过板没有」,它不是成交额/规模/波动/换手这些水平型暴露。


## 3. 研究过程与逻辑(从对话记录里抽的动作时间线;每条是研究员给自己那条命令写的说明)

- 10-04 12:03 [看] List project files and count doc lines
- 10-04 12:03 [看] Inspect existing config, notes, studies, runs for F106
- 10-04 12:03 [跑] List server-side tags already run for F106  〔study.sh list F106_erm_mag_gap_1m 2〕
- 10-04 12:03 [跑] Show baseline digest for F106  〔study.sh digest F106_erm_mag_gap_1m S0_baseline 2〕
- 10-04 12:04 [看] Show overview of F106 relative to batch and known families
- 10-04 12:04 [跑] Decompose F106 expression into operator profiles and SSA  〔study.sh decompose F106_erm_mag_gap_1m 2〕
- 10-04 12:04 [跑] Read kernel source for all operators in the expression  〔study.sh src day_quantile is_gt is_lt select_where create_like day_sum add div abs_〕
- 10-04 12:05 [看] Read study.sh wrapper and list project dirs
- 10-04 12:05 [看] List function signatures in diagnose, panels, guard
- 10-04 12:05 [看] List prior study scripts and notes for reference
- 10-04 12:05 [看] Read lab findings and one example analysis script
- 10-04 12:06 [看] List available operators (day_, is_, select, in_ families)
- 10-04 12:06 [看] List cross_, cs_, ts_, elementwise operators
- 10-04 12:06 [跑] Read kernel sources for auxiliary operators  〔study.sh src eq is_gt0 is_lt0 sign fillna in_slice day_mean day_first day_max day_m〕
- 10-04 12:07 [看] Read example probes file and probes API signatures
- 10-04 12:07 [看] Read probes API implementation
- 10-04 12:08 [看] Read bridge and remote tools to learn local test options
- 10-04 12:08 [看] Find how the Ret field is defined in local AlphaCube
- 10-04 12:08 [看] Search local AlphaCube source for Ret field definition
- 10-04 12:08 [看] Search for Ret field semantics in store and docs
- 10-04 12:09 [跑] Read cross_delay source and local ema_rows, long_short_weights  〔study.sh src cross_delay day_last create_valid_mask in_slice_from_start 2〕
- 10-04 12:10 [看] Check op decorator and _sum/_mean helpers in local AlphaCube
- 10-04 12:10 [看] Read built-in probes and how study probes are loaded
- 10-04 12:10 [看] Create study dirs and look at F104 probe self-check style
- 10-04 12:11 [写] studies/F106_erm_mag_gap_1m/probes.py
- 10-04 12:11 [看] Run the new probes locally as a syntax and self-check test
- 10-04 12:12 [看] Debug why the oddness self-check fails locally
- 10-04 12:13 [看] Fix oddness self-check in probes and rerun locally
- 10-04 12:13 [跑] Add probes to config and run decompose on server  〔study.sh decompose F106_erm_mag_gap_1m 2〕
- 10-04 12:14 [写] notes/F106_erm_mag_gap_1m/01_expression.md
- 10-04 12:14 [写] notes/F106_erm_mag_gap_1m/02_operators.md
- 10-04 12:14 [写] notes/F106_erm_mag_gap_1m/03_decomposition.md
- 10-04 12:15 [写] notes/F106_erm_mag_gap_1m/04_grammar.md
- 10-04 12:15 [写] notes/F106_erm_mag_gap_1m/05_hypotheses.md
- 10-04 12:15 [看] Read remote_tools check and propose implementation
- 10-04 12:15 [跑] Get candidate experiments draft from propose  〔study.sh propose F106_erm_mag_gap_1m 2〕
- 10-04 12:19 [写] studies/F106_erm_mag_gap_1m/x1_anatomy.py
- 10-04 12:19 [看] Run anatomy selftest and parse-check expressions locally
- 10-04 12:19 [跑] Check server status and launch anatomy script  〔study.sh exec F106_erm_mag_gap_1m x1 x1_anatomy.py 2〕
- 10-04 12:20 [看] Inspect structure of S0 baseline JSON
- 10-04 12:20 [看] Extract baseline sweep, by-year, and profile details from S0 JSON
- 10-04 12:20 [写] notes/F106_erm_mag_gap_1m/06_baseline.md
- 10-04 12:20 [跑] Wait for anatomy job x1 to finish  〔study.sh wait F106_erm_mag_gap_1m x1 520 2〕
- 10-04 12:29 [跑] Wait for x1 completion and save output  〔study.sh wait F106_erm_mag_gap_1m x1 300〕
- 10-04 12:30 [看] Read first part of x1 anatomy log
- 10-04 12:31 [看] Read rest of x1 anatomy log
- 10-04 12:34 [看] Look at a prior study config for stage and diagnostics syntax
- 10-04 12:35 [跑] Check for elementwise min/max/clip operators  〔study.sh src pairwise_max signedpower 2〕
- 10-04 12:35 [看] Add S1 stage, gates, and diagnostics to F106 config
- 10-04 12:36 [跑] Rename gate and check config expressions on server  〔study.sh check F106_erm_mag_gap_1m 2〕
- 10-04 12:36 [跑] View full check output and see whether study.sh changed  〔study.sh check F106_erm_mag_gap_1m〕
- 10-04 12:37 [看] Check whether the playbook and docs changed on disk
- 10-04 12:37 [看] Read updated playbook sections on tools, rules, and handoff
- 10-04 12:39 [看] Read updated study.sh sections to see behavior changes
- 10-04 12:40 [跑] Launch stage S1_regime on the server  〔study.sh run F106_erm_mag_gap_1m S1_regime S1_regime 2〕
- 10-04 12:41 [写] notes/F106_erm_mag_gap_1m/07x_1_anatomy.md
- 10-04 12:42 [跑] Wait for S1 stage and print digest  〔study.sh wait F106_erm_mag_gap_1m S1_regime 540〕
- 10-04 12:51 [跑] Wait again for S1 stage and print digest  〔study.sh wait F106_erm_mag_gap_1m S1_regime 540〕
- 10-04 13:01 [看] Check server job queue status
- 10-04 13:02 [写] studies/F106_erm_mag_gap_1m/x2_longonly.py
- 10-04 13:02 [看] Run x2 selftest locally and lint both scripts
- 10-04 13:02 [跑] Check x2 for undefined names, then wait for S1  〔study.sh wait F106_erm_mag_gap_1m S1_regime 420〕
- 10-04 13:09 [跑] Wait for S1 metrics and print digest  〔study.sh wait F106_erm_mag_gap_1m S1_regime 540〕

### 研究员对这棵树的理解(原文照录 `notes/F106_erm_mag_gap_1m/02_operators.md`)

读了每个算子的服务器内核源码(`study.sh src`),和名字不一样、或者探针表里看不出来的地方:

1. **`day_quantile(x, q)` = `torch.nanquantile(x, q, dim=-1)`,线性插值**。241 个分钟全有值时,q=0.95 的位置是 0.95×240 = 228.0,
   恰好是一个顺序统计量(从小到大第 229 个 = 第 13 大),不插值;少一个分钟(240 个有效值)位置就是 227.05,变成两个相邻顺序统计量的
   5%/95% 加权(探针 `quantile_order_statistic`:斜坡 0..240 上读 228.0;缺第一分钟读 228.05)。
   所以「95% 分位数恰好为 0」的条件是:**上涨分钟 ≤ 12 个**(241 个有效分钟时)。
2. **`is_gt` / `is_lt` 是严格不等号,而且 NaN 比较为假 → 输出 0(不是 NaN)**。两个后果:
   (a) 与分位数并列的分钟不进尾部 —— 分钟收益里并列极多(同一个 tick 的涨跌、0),尾部集合可以远少于 12 个、甚至是空集;
   (b) 缺失分钟在 `select_where` 之后变成 0 而不是 NaN,所以求和、计数都只数有效分钟,整棵树对「部分分钟缺失」没有 NaN 传播;
   只有整天缺失(分位数是 NaN)才输出 NaN —— 这就是 cov = 1.00 的原因。
3. **`create_like(x, 0)` 用的是整数 0 → 张量 dtype 是 int64**;`create_like(x, 1e-06)` 是 float32。`select_where` 里 float32 与 int64
   混用靠 `torch.where` 的类型提升,结果是 float32,数值上没有问题,只是占内存。
4. **计数分母上的 `+1e-6` 只在尾部集合为空时起作用**(求和也是 0,结果 0/1e-6 = 0),是纯粹的除零保护,不改变任何非空情形的值。
   **分位数分母上的 `+1e-6` 才是这棵树的要害**:它是一个带量纲的常数(收益单位),比一个 tick 的收益(10⁻³ 量级)小三个数量级,
   所以分位数为 0 时比值被放大 10⁶ 倍。
5. **右侧分母是 `q95 + 1e-6`(没有绝对值),左侧是 `|q05| + 1e-6`**。q95 理论上可以是负的(全天 95% 的分钟都在跌),
   那时右侧比值会变号甚至再次接近除零;实际上这种日子极少(需要 >229 个分钟为负)。
6. **整棵树在服务器上关于 Ret 是精确的奇函数**(探针:`max|tree(r)+tree(−r)|` = 0.0,两侧尾部各 12 个分钟)。
   本机那份 torch 把 0.95×240 算成比 228 略小,右尾会多收进分位数本身那一个分钟(13 对 12)—— 这是「本机不是事实来源」的一个实例,
   以服务器为准。
7. `day_sum` = `nansum`,整行全 NaN 才给 NaN。`abs_`、`add`、`sub`、`div` 就是 torch 的逐元素运算,没有 NaN 填充(`fill_nan_with_zero` 默认关)。

**这棵树里没有任何日轴算子**:它是纯粹的「当天 241 个分钟 → 一个数」,真实回看 1 天。全部的时间结构来自口径里的因果 EMA(半衰期)。


### 研究员对这棵树的理解(原文照录 `notes/F106_erm_mag_gap_1m/03_decomposition.md`)

记当天有效分钟收益为 r₁…rₙ,q⁺ = Q₀.₉₅(r),q⁻ = Q₀.₀₅(r),U = {r > q⁺},D = {r < q⁻}(严格不等):

```
ES⁺ = Σ_U r / (|U| + 1e-6)          ES⁻ = Σ_D |r| / (|D| + 1e-6)
R   = ES⁺ / (q⁺ + 1e-6)             L   = ES⁻ / (|q⁻| + 1e-6)
X   = R − L
```

SSA 表里 24 个中间量其实只有 4 个量:两个分位数(各被引用 3 次)、两个尾内均值。**它有三个取值区间,量级差三到五个数量级**
(探针 `tail_ratio_knot`,用服务器内核、float32):

| 区间 | 条件(241 个有效分钟) | R(或 L)读数 | 含义 |
|---|---|---|---|
| 常规 | 上涨分钟 ≥ 13 个且幅度有差异 | 1.0~3(高斯分钟收益:右 1.262、左 1.260,理论值 1.254) | 尾部形状:ES/VaR |
| 并列 | 上涨分钟 ≥ 13 个但都是同一个 tick | ≈ 1.04~1.06(尾内均值 ≈ 分位数) | 价格网格,不是形状 |
| 塌缩 | 上涨分钟 ≤ 12 个 | **ES⁺ × 10⁶**(一个 0.2% 的 tick → 2000~2110) | 「这一侧几乎没动」× 那几下的幅度 |
| (边缘) | 240 个有效分钟且恰好 12 个上涨分钟 | ≈ 20.9(分位数是 5% × 最小上涨幅度) | 插值造成的过渡 |

整棵树在四个角上的读数(同一个探针):只有上涨稀少 → **+2039**;只有下跌稀少 → **−2039**;两边都稀少且幅度相同 → 0;
两边都不稀少 → 0;价格全天不动 → 0。也就是说:

- **X 的截面两端一定是塌缩日**。常规区间里 X 的标准差只有约 0.10(高斯)到 0.3,塌缩日是 ±10³ 以上。
- **塌缩区间里 X 不再是无量纲的**:探针 `scale_degree_by_regime` —— 常规区间把收益放大 2 倍,X 变化 < 0.0003(齐次度 0);
  塌缩区间放大 2 倍,X 变成 2.0005 倍(齐次度 1)。在塌缩区间里它读的是「那几个分钟平均跳了多大」。
- **口径是先 EMA 再排序**。半衰期 20 的 EMA 里,一个 +2000 的塌缩日要过 20×log₂(2000/0.3) ≈ 250 个交易日才会衰减到常规量级以下。
  所以实际交易的信号 ≈ 「这只股票过去一年里塌缩日的带符号、按幅度加权的累计」,常规区间的尾部形状信息基本被淹没。
  (这是从公式推出来的预期,要在真实数据上量 —— 见 `07x_1_anatomy.md`。)

**价格网格本身能不能造出塌缩日**(探针 `tick_grid_regime_share`,0.01 元 tick 的几何随机游走):
日波动约 1.2% 时,2 元股 24% 的日子右侧塌缩,3 元股 0.5%,5 元以上 0;日波动约 0.6% 时,2 元股 92%、3 元股 66%、5 元股 4%、10 元以上 0。
所以纯粹由 tick 造成的塌缩只发生在 **3 元以下(或 5 元以下且极不活跃)** 的股票上;更高价位的股票要进塌缩区间,得靠别的机制
(封板、停牌前后、全天只有零星成交)。

**一个分钟的离群收益的杠杆**(探针 `single_minute_leverage`):常规区间里把第一个分钟换成 10 倍分钟波动的跳空,X 平均移动 +0.39
(无跳空时 X 的标准差是 0.107);20 倍 → +0.90;−10 倍 → −0.39。一阶近似 (g − 2.06σ)/(12 × 1.645σ) 给出 0.40 / 0.91,对得上。
如果 `Ret` 的第一个分钟带着隔夜跳空,常规区间里的 X 就在很大程度上是「带符号的跳空 ÷ 分钟波动」—— 这要在真实数据上核对。


### 研究员对这棵树的理解(原文照录 `notes/F106_erm_mag_gap_1m/04_grammar.md`)

结构语法(从里到外):

```
分钟收益 Ret
  → 日内分位数(q95 / q05)                    —— 阈值,各自既当「尾部的门槛」又当「归一化的分母」
  → 严格越过阈值的分钟(0/1 掩码)             —— 事件判定
  → 掩码内的均值(ES)                          —— 尾内幅度
  → ÷ (阈值 + 1e-6)                             —— 归一化;阈值为 0 时变成 ×10⁶
  → 右侧 − 左侧                                  —— 带符号的不对称
(口径)→ 因果 EMA,半衰期 20                    —— 唯一的时间结构;把稀疏的大数变成缓慢衰减的状态
```

和已经研究过的几条都不同:**没有日轴算子、没有成交额字段、没有逐元素乘法(门控)**。所以 F001 的「极值记忆」、
F002 的「成对协方差」、F104 的「截面掩码」这些问题在这里都不存在。这棵树特有的问题是:

1. 阈值兼做分母 → 阈值为 0 时的行为决定了截面两端是谁(`+1e-6` 是一个带量纲的常数)。
2. 输出是一个**混合分布**(常规 O(1) + 塌缩 O(10³~10⁵)),再喂给一个**线性**的 EMA → 排序由大数决定。
   「先排序再平滑」与「先平滑再排序」在这里不是小差别,而是两条不同的因子。
3. 右减左:两侧各自是不是都有预测力、符号相反?还是只有一侧有用、另一侧只是噪声/抵消项?
4. 只用到 `Ret`:第一个分钟的收益里有没有隔夜跳空,决定了常规区间读的是「日内尾部形状」还是「跳空」。


## 4. 假设表

下面是研究员在跑实验**之前**写的假设表(原文照录 `notes/F106_erm_mag_gap_1m/05_hypotheses.md`)。**其后的实验结果没有回填**:
每条假设现在是「未验证 / 被支持 / 被否定」,要对照第 2 节列出的运行结果重新判定。

写于任何实验之前(手里只有 S0 基线、源码和探针)。每条写它预测什么、什么结果能杀死它。结论见 `09_diagnosis.md`。

| # | 假设 | 它预测什么 | 哪个实验能杀死它 |
|---|---|---|---|
| H1 | **塌缩日决定一切**:截面两端、乃至整个排序,由「分位数 = 0 → ×10⁶」的日子决定,尾部形状不起作用 | \|X\| 双峰(O(1) 与 O(10³+));EMA 后绝大多数股票的信号由塌缩日主导;只保留「哪一侧塌了」的指示量(不要幅度、不要 ES/VaR)就能复现多空夏普;把 1e-6 换成与收益同量级的常数(塌缩消失)之后与原式的 rank 相关很低、空头腿收益消失 | 去掉塌缩日(或把 ε 调大)之后与原式 rank 相关仍 > 0.8 且多空夏普不变 → H1 死 |
| H2 | **常规区间的尾部形状不对称才是信号**,塌缩只是噪声 | 只在常规日上计算的 X(塌缩日置空/置 0)rank IC 不低于原式;先截面排序再平滑(消掉量级)不伤表现 | 常规版 rank IC ≈ 0 或多空夏普塌掉 → H2 死 |
| H3 | **塌缩日 = 封板日**:上涨稀少且幅度大 = 早盘拉到涨停后封死(或一字板/T 字板);下跌稀少且幅度大 = 跌停板 | 信号空头端(X 最大)的股票,近期涨停日占比远高于全市场;多头端(X 最小)近期跌停日占比高;空头腿收益里有一大块来自「次日开盘买不进」的票(标签 NaN 记 0);把 `buyable=False` 的标签换上,空头腿明显变小 | 两端的涨跌停占比与全市场无差别;换标签后空头腿不变 → H3 死 |
| H4 | **塌缩日 = 低价/不活跃**:tick 相对价格太粗,或全天成交稀疏 → 是价格水平 / 换手率 / 成交额水平的另一种写法 | 塌缩日集中在 3 元以下或成交额最低的股票;信号的折叠量(到截面中位的距离)与 log 价格、换手率、「零收益分钟占比」的 rank 相关很高;对这些变量(及其折叠)中性化后空头腿消失 | 塌缩日在价格/成交额各档均匀分布 → H4 死。注意:S0 的秩空间线性 R² 只有 0.103,但两端都是塌缩日(非单调),线性中性化看不见,要用折叠量去量 |
| H5 | **常规区间读的是隔夜跳空**:如果 `Ret` 的第一个分钟是「开盘价 ÷ 昨收」,它几乎必然落在尾部,X ≈ 带符号的跳空 ÷ 分钟波动 | `day_first(Ret)` 与 开盘/昨收 高度相关且量级是其余分钟的数倍;去掉第一个分钟重算的 X 与原式(常规日)rank 相关明显 < 1;隔夜收益的 EMA 能解释常规区间的 X | `day_first(Ret)` 是 NaN 或量级与其他分钟相同;去掉第一分钟后 rank 相关 ≈ 1 → H5 死 |
| H6 | **钱在空头腿,是因为空头端是「彩票/打板」类股票**(近期涨停、次新、题材股),它们在可买入口径下次日起持续跑输;多头端是它的镜像(跌停/阴跌股),同样跑输 → 分位剖面是倒 U,没有「好的一端」 | 分位剖面两端都负(S0:训练 Q1 −28.4%、Q10 −5.3%,已经符合);把 X 折叠(取 −\|X\| 或只做「没有塌缩日」的那一端)多头腿转正但幅度小(只是「避开坏股票」);多头腿净超额的上限 ≈ 中间几档的平均超额(训练 +3%~+8%) | 存在某个单调变换使多头端十分位稳定为正且 > +10% → H6 的「没有好的一端」部分死 |
| H7 | **平滑在起主要作用,而且半衰期 20 是网格的边界解**:hl 0 → 20 多头腿净超额从 −67% 单调升到 −6.9%,衰减表 rank IC 随持有期上升(h1 0.0165 → h20 0.0338),说明它是一个慢状态变量 | 用显式的更长记忆(`cross_mean`/`cross_sum` 30、60 日,或「过去 N 日塌缩日计数」)替代 EMA-20,rank IC 与多空夏普不降;日换手再降 | 更长窗口使 rank IC 明显下降 → 记忆长度不是越长越好,H7 的「边界解」部分死 |
| H8 | **两侧不对等**:右侧(R)与左侧(L)不是同一个机制的镜像 —— 上涨稀少的塌缩(R 大)对应「阴跌/无人问津」或「封涨停」,下跌稀少(L 大)对应「封跌停」或「缓涨」,各自的后续收益方向未必相反 | 单独的 R 与单独的 L 各自的方向、分位剖面不同;「右减左」里可能有一侧是在抵消另一侧 | R 与 −L 的 rank IC 相同、剖面互为镜像 → H8 死 |
| H9 | **多余节点**:左支的 `abs_`、计数上的 `+1e-6`、`create_like(·,0)` 都不改变排序;真正有内容的只有「分位数作分母 + 1e-6」 | 把 ES/VaR 换成不除分位数的写法(如 ES − VaR、或尾部计数)会变成另一条因子;而去掉计数 ε 完全等价 | (读源码已基本确立,不单独花服务器轮次) |

**对只能做多的用户,事前判断**:这条因子公布的多头腿是负的(训练 −4.2% 毛、S0 净 −5.8%),空头腿 +26.3%。
如果 H3/H6 成立,它本质上是一个「该避开谁」的清单,不是一个「该买谁」的排序;升华的空间只有两条路:
(a) 把「避开」变成一个单调的多头排序(折叠、或只用「干净」的一端);(b) 承认它没有多头腿,结论写「对纯多头无用,相对已知家族无增量」。
两条路都要和 `cross_mean(day_std(Amt), 30)` / `cross_max(day_std(Amt), 9)` 比。

## 5. 当前的候选(提纯 / 升华)

(没有留下。研究还没进行到选候选的阶段,或者候选只在研究员脑子里。)

## 6. 后面的研究思路(研究员已经写进配置和脚本、但还没做完的)

- 阶段 **S0_baseline**(已有结果):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
    - `v_base` = `sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Ret, 0))), add(day_sum(is_gt(Ret, day_quantile(Ret, 0.95))), cr` —— 原始表达式
- 阶段 **S1_regime**(**还没有结果**):公布的多空夏普(和空头腿)是「塌缩日 = 封板事件」做出来的,还是「尾部形状不对称」做出来的?差的符号有没有信息?
    - `a_right` = `div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Ret, 0))), add(day_sum(is_gt(Ret, day_quantile(Ret, 0.95))), create` —— 只留右侧(上涨尾部的 ES/VaR)。H8:如果两侧互为镜像,右侧的方向应为 −、左侧应为 +;x1 里两侧的日频 rank IC 同号(都是「越大越差」),这里用两本书坐实。若同号,「右减左」就是在让两个同向的信号互相抵消
    - `a_left` = `div(div(day_sum(select_where(is_lt(Ret, day_quantile(Ret, 0.05)), abs_(Ret), create_like(Ret, 0))), add(day_sum(is_lt(Ret, day_quantile(Ret, 0.05))), ` —— 只留左侧(下跌尾部的 ES/VaR)。与 a_right 成对读:方向相同 → 差的符号不携带信息
    - `a_sum` = `add(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Ret, 0))), add(day_sum(is_gt(Ret, day_quantile(Ret, 0.95))), cr` —— 把减号换成加号:不带符号的「塌缩事件 + 尾部尖」强度。H1/H3 预测它不输原式(事件不分正负都是封板日);若明显更差,说明差的符号(上跳比下跳尖)才是信号
    - `a_abs` = `abs_(sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Ret, 0))), add(day_sum(is_gt(Ret, day_quantile(Ret, 0.95))` —— 丢掉差的符号、保留量级。和 a_sum 的区别:两侧同时塌缩时 a_sum 是两者之和、a_abs 是两者之差的绝对值。预测:分位剖面从倒 U 变成单调(只有一端是事件股)
    - `a_regular` = `mul(sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Ret, 0))), add(day_sum(is_gt(Ret, day_quantile(Ret, 0.95)))` —— H2 的判决实验:只保留两个分位数都没塌缩的日子(其余置 0)。H2(尾部形状不对称才是信号)预测它保住原式的多空夏普;H1 预测塌掉。x1 的 numpy 版已经塌了(−1.45/−2.11),这里用引擎坐实
    - `a_eps3` = `sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Ret, 0))), add(day_sum(is_gt(Ret, day_quantile(Ret, 0.95))), cr` —— 把两个分位数分母上的 1e-6 换成 1e-3:塌缩日的读数从 ES×10⁶ 降到 ES×10³(比常规日大 10~100 倍而不是 10⁴~10⁵ 倍),EMA 里记住一个事件的时间从约一年缩到约四个月。若表现不变,说明需要的只是「比常规日大」,不需要那六个数量级
    - `a_flag` = `add(less(day_quantile(Ret, 0.95), create_like(day_quantile(Ret, 0.95), 1e-06)), less(abs_(day_quantile(Ret, 0.05)), create_like(day_quantile(Ret, 0.05` —— 只留「塌了几侧」(0/1/2),不要任何幅度。注意它把全天不动的日子(一字板)也算进来了,而原式在那些日子读 0。预测:多空夏普不低于原式(x1 的 numpy 版 +3.40/+2.66)。取值只有三档,dist 门槛过不了 —— 它是诊断变体,不是候选
    - `a_rankfirst` = `cs_rank(sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Ret, 0))), add(day_sum(is_gt(Ret, day_quantile(Ret, 0.9` —— 先截面排序再平滑:量级被抹掉,塌缩日在 EMA 里只相当于一个普通的极端排名。H1 预测塌掉(x1 numpy 版 −0.93/−1.40);若不塌,说明排序本身(而不是量级造成的长记忆)携带信号
    - `a_lockshare` = `day_mean(eq(Close, day_max(High)))` —— 朴素等价物之一:价格钉在当日最高价的分钟占比(封涨停的日子接近 1)。H3 预测它与 a_abs 的秩相关高、空头腿同样大;若无关,塌缩日就不只是「封板」
    - `a_limitup` = `mul(sub(create_like(day_last(Close), 1.0), less(day_last(Close), day_max(High))), greater(div(day_last(Close), cross_delay(day_last(Close), 1)), creat` —— 朴素等价物之二:日线涨停标记(收盘 = 最高价且日涨幅 ≥ 9.5%;ST 的 5% 板不算)。x1 里 86% 的右侧塌缩日是涨停收盘,而未塌缩的涨停日事后同样跑输。预测:多空夏普不低于原式 → 这棵树就是「近期涨停」的一种带噪声的写法。取值只有两档,过不了 dist,是诊断变体
- 脚本 `studies/F106_erm_mag_gap_1m/probes.py`:Probes this tree needs:  ES/VaR of the right tail of minute returns  minus  ES/VaR of the left tail.

    side(q) = [ sum(Ret beyond day_quantile(Ret, q)) / (count + 1e-6) ] / ( |day_quantile(Ret, q)| + 1e-6 )
    X       = side(0.95) - side(0.05)

Every operator in it is elementary (a quantile, a strict comparison, a where, a sum, a
ratio), so the per-operator built-in probes have nothing surprising to say.  What decides
how the tree reads real data is the COMPOSITE, and three things in it that a name cannot tell:

* which order statistic `day_quantile(., 0.95)` actually is on a 241-minute ro
- 脚本 `studies/F106_erm_mag_gap_1m/x1_anatomy.py`:x1 -- what the ES/VaR gap tree reads on REAL data, and who sits at the ends of the traded signal.

No stock diagnostic answers these, and the stage plan depends on the answers:

  0. helper sources / probe self-checks with the SERVER kernels
  A. what is `Ret`?  valid minutes per day; does the first minute carry the overnight gap;
     does day_sum(Ret) add up to close/prev-close or to close/open
  B. the three regimes (regular / edge / blown-up) of each side on real stock-days: how often, how big,
     and what kind of day it is (limit board, one-word board, low price, thin trading)
  C. the 
- 脚本 `studies/F106_erm_mag_gap_1m/x2_longonly.py`:x2 -- for a LONG-ONLY user: does this factor add anything to the known amount-level family?

x1 said the tree is a memory of locked limit-board days and that no construction of it has a positive
long leg.  The one use left for a long-only book is as an EXCLUSION: do not hold the names this factor
flags.  That is only worth something if the book one would hold anyway (the known family,
cross_mean(day_std(Amt), 30) / cross_max(day_std(Amt), 9)) actually contains such names and loses on them.

  1. the known family's long decile: how many of its names are flagged, and how do the flagged ones do
 

## 7. 留出段

未读。读之前要先在 `10_distilled.md` 里写下候选排序和判据。

## 8. 给接手者的提醒

- `S1_regime`(10-04 12:40 用 run 启动)在服务器上跑着或已跑完,**结果没人读过**:`./scripts/study.sh wait F106_erm_mag_gap_1m S1_regime` 拉回来看。
- 上一位研究员的完整动作流水(含每条命令的输出):`handoff/F106_erm_mag_gap_1m/agents/`。
- 这一页是自动汇编的;你读完材料、形成判断之后,**按 playbook §7 的 8 节把它整个重写**。
