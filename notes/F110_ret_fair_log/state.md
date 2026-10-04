# F110_ret_fair_log — 研究现状(**自动汇编**,2026-10-04 13:10)

> 这一页不是研究员写的。上一位研究员(Opus 5.5,工作流 agent `study:F110_ret_fair_log`)在写下现状之前就被换下了;
> 协调者用脚本(`scripts/autostate.py`,不经过任何模型)把磁盘上**它写过的和做过的**汇编成这一页。
> 它当时怎么想的没有留下 —— 假设的最新状态、对结果的解读,需要接手的主研读下面列出的材料后**重写这一页**。

## 1. 一句话现状

- 配置里的一句话(研究员读完这棵树之后写的):日内收益 × |放量后波动 − 缩量后波动|:按『成交量跳变处的价格冲击』加权的日内收益累积(方向为负 = 加权的月度日内反转)
- 已写 notes:01_expression.md、02_operators.md、03_decomposition.md、04_grammar.md、05_hypotheses.md、06_baseline.md
- 已拉回本地的运行:S0_baseline;已启动但**结果还没人读**的:x1b
- 留出段:未读

## 2. 中间结果(事实在这些文件里,还没有汇总)

- 运行 `S0_baseline`(10-04 11:53):`./scripts/study.sh digest F110_ret_fair_log S0_baseline`
- 自写分析 `x1` 的输出:`logs/F110_ret_fair_log_x1.log`

### 基线读数(原文照录 `notes/F110_ret_fair_log/06_baseline.md`)

基线(S0,方向与半衰期在 train 上定,valid 没见过)怎么读:

**1. 多头腿扣费之后是零 —— 这是起点。** 多头口径和多空口径选到的是同一个半衰期(20,网格上限),所以这条因子没有
「换成多头最优半衰期就白捡几个点」的余地:**「原式 + 多头最优半衰期」就是表里这一行本身**。

| | train | valid | utrain(用户口径) |
|---|---|---|---|
| 多头腿净超额 / 纯多头夏普 | −0.0% / −0.00 | −0.6% / −0.10 | −0.2% / −0.03 |
| 多头腿毛超额 / 多头日换手 | +8.0% / 10.6% | +7.4% / 10.5% | +7.8% / 10.5% |
| 扣费多空夏普 / 空头腿毛超额 | +2.77 / +43.3% | +2.74 / +46.8% | +2.76 / +44.3% |

毛超额 8 个点,10.6% 的日换手按双边 15 bp 正好吃掉 8 个点。两道门槛都过(cov 1.00、dist 0.97)。

**2. 半衰期越长越好,而且到网格尽头还没有见顶。** train 上的扫描:

| 半衰期 | 0 | 1 | 2 | 3 | 5 | 10 | 20 |
|---|---|---|---|---|---|---|---|
| 多头腿净超额 | −62.3% | −35.7% | −24.3% | −19.1% | −13.5% | −5.9% | −0.0% |
| 多头日换手 | 85.5% | 53.4% | 38.5% | 31.1% | 23.6% | 16.0% | 10.6% |
| 扣费多空夏普 | −6.57 | −1.89 | +0.08 | +0.91 | +1.64 | +2.33 | +2.77 |

不平滑时它是一条日换手 85% 的信号(今天的日内收益 × 今天的 `S`),没法交易。每把半衰期翻一倍,多头腿净超额多 6~8 个点。
这说明两件事:(a)预测力在**慢**的成分里(「过去一两个月累计」而不是「昨天」);(b)20 很可能不是最优,只是网格到头了 —— H9。
衰减表是同一件事的另一面:实际交易信号的 rank IC 从 h1 的 +0.044 一路升到 h20 的 +0.106,持有期越长越准。

**3. 钱几乎全在空头腿。** 空头腿毛超额 +43.3% / +46.8%,多头腿 +8.0% / +7.4%,多头腿只占毛价差的 16% / 14%。
这批因子普遍七八成在空头腿,这一条是八成五。对只能做多的用户,多空夏普 2.77 里能拿到手的部分是零。

**4. 分位剖面不是单调的,是「一道悬崖 + 一块平台」。**

| | Q1(空头端) | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10(多头端) |
|---|---|---|---|---|---|---|---|---|---|---|
| train | −43.5% | −11.4% | +0.4% | +4.8% | +4.9% | +8.9% | +9.6% | +7.6% | +10.1% | +8.6% |
| valid | −47.8% | −13.4% | −2.7% | +4.2% | +7.5% | +8.7% | +10.7% | +12.3% | +12.0% | +8.6% |

Q4 到 Q10 是平的,多头端 Q10 两段都**不高于** Q7~Q9。也就是说这条因子在多头一侧没有排序能力:多头十分位的 +8% 和
「随便拿一只不在最差两成里的票」差不多 —— 这 +8% 是相对全市场等权的超额,而全市场等权被 Q1、Q2 拖低了 5.5 个点。
多头十分位既然不比平台好,它的高换手(信号最极端的一端,成员换得最勤)就纯是成本。H6、H10 从这里来。

**5. 逐年**(多头腿净超额 / 扣费多空夏普):2018 −1.8% / +2.67,2019 +6.5% / +4.75,2020 −1.1% / +2.12,2021 −4.1% / +2.14,
2022 +3.2% / +3.90,2023(到 8 月 7 日)−7.1% / +1.27。多空每年都是正的;多头腿六年里四年为负,没有哪一段是稳定为正的。

**6. 已知暴露。** 9 个线性控制变量在秩空间张成实际交易信号的 34.9%(原始日频面板上是 62.4% —— 当天的 `T` 和当天收益 `ctl_rev1` 高度同序,
平滑之后这层关系被稀释,所以这个 R² 低估了「它是不是反转 / 动量的另一种写法」,要用同样平滑过的对照去量,H8)。
单个控制里 R² 最高的是 20 日波动(0.229)和换手率(0.217);对全部控制中性化之后,残差 rank IC 从 +0.0444 掉到 +0.0173,
**空头腿从 +43.3% 掉到 +5.1%,多头腿毛超额还剩 +6.2%**。空头腿基本就是「高波动 / 高换手的票之后跑输」这个已知事实;多头腿那一点毛超额反而不靠这些控制。
与已知家族的 rank 相关:成交额水平三条 −0.35 ~ −0.36,日内波动极值记忆 −0.39 —— 相关但远不到同族(0.95)的程度。

**7. 条件 IC。** 按流通市值分桶 +0.052 / +0.051 / +0.052 / +0.043 / +0.026(小票里更强,最大一档减半);
按当天成交额分桶 +0.022 / +0.025 / +0.031 / +0.041 / +0.055(成交越活跃越强)。两条合起来:它在「小而活跃」的票里最强 ——
正是被炒作的那一类。(当天成交额这个分桶变量对一条 20 日平滑的信号不算内生,但它和信号空头端的高换手正相关,读的时候要记得。)


## 3. 研究过程与逻辑(从对话记录里抽的动作时间线;每条是研究员给自己那条命令写的说明)

- 10-04 12:03 [看] Check sizes of required docs and list project root
- 10-04 12:03 [看] Inspect existing study state for F110
- 10-04 12:03 [跑] List tags already run on the server for F110  〔study.sh list F110_ret_fair_log 2〕
- 10-04 12:03 [跑] Print baseline digest for F110  〔study.sh digest F110_ret_fair_log S0_baseline 2〕
- 10-04 12:03 [看] Show F110 relations to other batch factors and known families
- 10-04 12:04 [跑] Run decompose for F110 and save output to scratchpad  〔study.sh decompose F110_ret_fair_log 2〕
- 10-04 12:04 [跑] Read kernel source for intraday and comparison operators  〔study.sh src in_sustain_stddev in_forward_valid_part in_mean_full in_stddev_full is〕
- 10-04 12:05 [跑] Read kernel source for elementwise and day-fold operators  〔study.sh src mul sub div add abs_ log day_last day_first day_mean day_std 2〕
- 10-04 12:05 [看] List existing studies, notes, reports and configs
- 10-04 12:05 [看] Read lab findings, study.sh, and study_tools
- 10-04 12:05 [看] Read study.sh and study_tools source
- 10-04 12:05 [看] List partura module sizes and prior study files
- 10-04 12:05 [看] Find prior uses of trigger operators and list batch expressions
- 10-04 12:05 [看] Read F101 notes on the closely related trigger operator
- 10-04 12:06 [看] Read F101 mechanism diagnosis
- 10-04 12:06 [看] List local logs and run directories of prior studies
- 10-04 12:07 [看] Read remote_tools and F101's custom probes
- 10-04 12:07 [看] Dump operator vocabulary and show cross_/cs_ operators
- 10-04 12:07 [看] Show non-cross/cs/nt operators
- 10-04 12:07 [看] Search notes for field/grid conventions (overnight, auction, 241 grid)
- 10-04 12:08 [看] Check server status and inspect S0 baseline JSON structure
- 10-04 12:08 [看] Extract half-life sweep and book rows from S0 baseline
- 10-04 12:09 [跑] Read source of candidate operators for variants  〔study.sh src signedpower sign neg cross_mean cross_sum cross_decay_linear cross_del〕
- 10-04 12:09 [跑] Read bridge path setup and a few more operator sources  〔study.sh src in_sustain_mean in_stddev_rolling in_delay day_sum 2〕
- 10-04 12:09 [看] Read local AlphaCube metrics for EMA and weight definitions
- 10-04 12:11 [看] Find definition of the Ret field in local AlphaCube
- 10-04 12:11 [看] Search AlphaCube docs for Ret field semantics
- 10-04 12:11 [看] Look for the definition of minute Ret in docs and code
- 10-04 12:11 [看] Check local torch/alphacube availability and read decompose module head
- 10-04 12:12 [看] Read semantics module (dossier construction and probe invocation)
- 10-04 12:12 [看] Create study dirs and view an example probes file header and config hook
- 10-04 12:13 [写] studies/F110_ret_fair_log/probes.py
- 10-04 12:13 [看] Smoke-test the custom probes locally against local kernels
- 10-04 12:14 [跑] Register probes in config and run decompose on server for authoritative probe readings  〔study.sh decompose F110_ret_fair_log 2〕
- 10-04 12:14 [跑] Get proposed candidate experiments draft for F110  〔study.sh propose F110_ret_fair_log 2〕
- 10-04 12:16 [跑] Read in_slice source and the nan-handling of row mean/std helpers  〔study.sh src in_slice 2〕
- 10-04 12:16 [写] notes/F110_ret_fair_log/01_expression.md
- 10-04 12:17 [写] notes/F110_ret_fair_log/02_operators.md
- 10-04 12:17 [写] notes/F110_ret_fair_log/03_decomposition.md
- 10-04 12:17 [写] notes/F110_ret_fair_log/04_grammar.md
- 10-04 12:18 [写] notes/F110_ret_fair_log/05_hypotheses.md
- 10-04 12:21 [写] studies/F110_ret_fair_log/x1_anatomy.py
- 10-04 12:21 [看] Smoke-test the anatomy script locally against a mock Study with random panels
- 10-04 12:22 [看] Check tail of mock run for sections H and I
- 10-04 12:23 [看] Patch anatomy script with lag profile and extras, re-run mock test
- 10-04 12:23 [跑] Launch anatomy script x1 on the server and check status  〔study.sh exec F110_ret_fair_log x1 x1_anatomy.py 2〕
- 10-04 12:25 [写] notes/F110_ret_fair_log/06_baseline.md
- 10-04 12:25 [跑] Wait for anatomy job x1 and print output  〔study.sh wait F110_ret_fair_log x1 540 2〕
- 10-04 12:35 [跑] Wait again for anatomy job x1  〔study.sh wait F110_ret_fair_log x1 540 2〕
- 10-04 12:44 [看] Read F105's distilled note for pre-registration format
- 10-04 12:44 [跑] Wait again for anatomy job x1  〔study.sh wait F110_ret_fair_log x1 540 2〕
- 10-04 12:54 [看] Check whether project tooling or docs mention the handoff notice
- 10-04 12:55 [看] Inspect modification times and the updated study.sh header
- 10-04 12:55 [看] Read the rest of the updated study.sh
- 10-04 12:55 [看] Read the changed parts of CLAUDE.md and the playbook, and handoff dir
- 10-04 12:56 [跑] Wait for anatomy job x1 and print results (first part)  〔study.sh wait F110_ret_fair_log x1 540 2〕
- 10-04 13:05 [跑] Wait for x1 and save output to scratchpad  〔study.sh wait F110_ret_fair_log x1 540〕
- 10-04 13:08 [看] Read the partial x1 log
- 10-04 13:09 [跑] Patch x1 script: lazy candidates and list section markers  〔study.sh exec F110_ret_fair_log x1b x1_anatomy.py C D E      (section C is always co〕
- 10-04 13:09 [看] Wrap script sections in selectable blocks and syntax-check
- 10-04 13:09 [看] Re-run mock test of the restructured script (all sections and a subset)

### 研究员对这棵树的理解(原文照录 `notes/F110_ret_fair_log/02_operators.md`)

读内核源码(`study.sh src`,服务器上的 AlphaCube 1698296)和为这棵树写的五个探针(`studies/F110_ret_fair_log/probes.py`,
每个都带已知答案的自检,在服务器内核上跑过)之后,和名字不一样、或者内置探针表里看不出来的地方:

1. **`in_forward_valid_part(x)` 不是前向填充,是「上一有效分钟的值」**(`prev_valid_lookup`:只读 `j−1`;`j−1` 是 0 或 NaN 时
   **跳到 `j−2`**;第一分钟是 NaN。自检:`in_delay(x, 1)` 同样只读 `j−1`,但遇到 0 原样返回、遇到 NaN 给 NaN —— 对上了)。
   「有效」的判据是**非零且非 NaN**,而它吃的是 `log(Volume)`,所以被跳过的是「零成交分钟」(`log` 给 NaN)和「成交量恰好为 1 的分钟」(`log 1 = 0`)。
   于是 `G_j = log V_j − log V_{上一有成交分钟}`:零成交的缺口被跨过去,缺口之后第一笔成交是和缺口**之前**的量比(探针:缺口后 `drop` 在 `j+3` 触发)。
2. **`log(0)` 是 NaN 不是 −inf**(`unary_domain`:`f(0) = nan`、`f(−e) = 1`、输入小到 1e-9 以下也是 NaN;源码是 `log|x|`,`|x| ≤ EPS` 给 NaN)。
   所以零成交分钟的 `G` 是 NaN,**不触发**任何一侧(`is_gt` / `is_lt` 遇 NaN 给 0,`comparison_semantics`)。
3. **`in_mean_full` / `in_stddev_full` 是整行统计量铺满整行**(`prev_valid_lookup` 读数:第 `j` 分钟的输出依赖全天 24/24 个分钟,含之后的)。
   阈值 `mean(G) ± 1·std(G)`(总体 std,NaN 跳过)是**事后**的:一分钟算不算放量 / 缩量要到收盘才知道。对收盘后才用的日频因子不是泄漏。
4. **`in_sustain_stddev(mask, Ret, 5)` 是触发型算子**(内置探针喂的是随机浮点,`mask == 1` 永不成立,内置读数全是空的)。`trigger_window` 实测:
   只在 `mask == 1` 处有值;窗口是**触发分钟自己 + 之后 4 分钟**(`offsets_read = [0,1,2,3,4]`);**总体** std(斜坡读数 1.4142);
   窗口跑出行尾就截短(剩 4/3/2/1 分钟读 1.118 / 0.8165 / 0.5 / **0.0**);窗口里的 NaN 被跳过;没有触发的分钟是 NaN,整行没有触发就整行 NaN。
   (F101 的 notes 里有同样的读数;这里是在本研究里重新测的,不是引用。)
5. **`is_gt(a, b)` / `is_lt(a, b)` 输出 int32**,NaN 和相等都给 0。
6. **`day_first(Open)` / `day_last(Close)` 取的是当天第一个 / 最后一个非 NaN 值**,所以 `D` 是「开盘价 → 收盘价」的日内收益,不含隔夜跳空。
7. **`abs_`、`mul`、`sub`、`div` 就是名字说的那样**;`sub(·, 1)` 里的常数是「铺满分钟轴的退化值」,所以原式的根在引擎里是「日频值铺满分钟轴」。
   想在外面再套日轴算子(`cross_mean` 等)时,要把 `D` 改写成不含常数的 `(Close − Open) / Open`(数值相同)。

**整棵树的组合性质**(`spike_composite`:用真实内核把 `S` 搭出来,喂答案可解析的合成日):

| 合成情形 | 读数 | 含义 |
|---|---|---|
| 孤立的一分钟放量(第 `j` 分钟量 ×10) | 放量在 `j` 触发,**缩量在 `j+1` 触发**;`S = 0.4·\|\|r_j\| − \|r_{j+5}\|\|`(实测 / 解析 = 1.0) | 一次量的脉冲同时喂给两侧,两个 5 分钟窗口重叠 4 分钟;`M − Q` 只剩「脉冲那一分钟的收益」对「5 分钟后那一分钟的收益」 |
| `Ret × 3` | `S × 3.0` | `S` 对收益齐次度 1 —— **带波动尺度** |
| `Volume × 7` | `S × 1.0` | 对成交量齐次度 0 —— **不带成交额尺度**(阈值按当天自己的 σ 定) |
| 放量 / 缩量两个掩码对调 | `S × 1.0` | `abs_` 让 `S` 对两侧对称:它量的是「两侧差多少」,不分谁大 |
| 量永久上一个台阶(只有放量、没有缩量) | `S = NaN` | 任何一侧没有触发,当天因子就是 NaN |
| 尾盘两分钟零成交 + 最后一格大量(收盘集合竞价的样子) | 最后一格触发放量;`M` 变成原来的 **0.5** | 最后一格的窗口只剩 1 分钟,std = 0,往 `M` 里掺一个 0 |

最后一行是这棵树特有的嫌疑(H13):241 网格的最后一格是收盘集合竞价,前两格(14:58、14:59)在深市没有成交,
所以几乎每天都可能在最后一格触发一次「放量」并贡献一个 0。`M` 被系统性地压低,而 `S` 是两个相近的量之差,对这种偏移敏感。实际占比在 X1 里量。


### 研究员对这棵树的理解(原文照录 `notes/F110_ret_fair_log/03_decomposition.md`)

分解表之外需要说明的。

**关键公式**(记 `v_j`、`r_j` 为第 `j` 分钟的成交量与收益,`j = 0..240`;`p(j)` 是 `j` 之前最近一个有成交的分钟):

```
g_j   = log v_j − log v_{p(j)}                    (v_j = 0 或 j 是当天第一分钟 → NaN,不触发)
放量集 U = { j : g_j > mean(g) + std(g) }          缩量集 L = { j : g_j < mean(g) − std(g) }     (全天的均值与总体 std)
σ5(j) = 总体 std( r_j, r_{j+1}, …, r_{j+4} )       (跑出行尾则截短;只剩 1 分钟时为 0)
M     = (1/|U|) Σ_{j∈U} σ5(j)                      Q = (1/|L|) Σ_{j∈L} σ5(j)
S     = | M − Q |
D     = Close_收盘 / Open_开盘 − 1
因子 T = D · S                                      实际交易的信号 = − EMA_{半衰期 20}(T)
```

**容易被名字骗的地方**

- 「放量后的波动」与「缩量后的波动」**不是两个独立的量**。量的脉冲是「上去再下来」:第 `j` 分钟放量,第 `j+1` 分钟多半就是缩量
  (探针 `spike_composite`:孤立脉冲下一个在 `j`、一个在 `j+1`)。两个窗口重叠 4/5,`M − Q` 里重叠的部分消掉,剩下的是
  **「放量那一分钟自己的收益幅度」对「5 分钟之后那一分钟的收益幅度」** —— 更接近「成交量脉冲处的价格冲击」,而不是字面上的「放量后与缩量后的波动差」。
  真实数据里两侧有多大比例是这样首尾相接的,在 X1 里量。
- `S` 是两个相近的正数之差再取绝对值。它的**量纲是波动**(对 `Ret` 齐次度 1),但它不是波动水平本身:`M ≈ Q` 的票 `S ≈ 0`,
  不管它波动多大。`M − Q` 是恒正(那 `abs_` 就是 no-op)还是正负都有(那 `abs_` 是一次折叠),决定了 `S` 到底是「冲击幅度」还是「两侧谁大都算」。
- `T = D·S` 是**两个带收益尺度的量相乘**(整体对收益齐次度 2):波动大的票 `|D|` 大、`S` 也大,所以 `T` 的两个尾巴都是高波动的票;
  排序上它近似「带符号的凸化」—— 大的日内涨跌被放大,小的被压扁。
- **整棵树没有任何日轴算子**(沿路径累计的回看是 1 天)。裸的 `T` 就是「今天的日内收益 × 今天的 `S`」,日换手 85%;
  它之所以能交易,全靠回测口径里那个半衰期 20 的 EMA。所以**平滑不是这条因子的外加参数,而是它的另一半**:
  实际的信号是 `Σ_k 0.966^k · D_{t−k}·S_{t−k}`,一个按 `S` 加权的日内收益累积。恒等式 `EMA(D·S) = EMA(D)·EMA(S) + Cov_EMA(D, S)`
  把它拆成「平均日内收益 × 平均 `S`」和「`S` 大的日子偏涨还是偏跌」两块。
- 用到的字段:`Close`、`Open`(定 `D`)、`Volume`(只定时刻)、`Ret`(定 `S` 的数值)。**没有成交额尺度**混进来(探针:`Volume × 7` 不改变 `S`)。
  所以 F001 那种「成交额水平换了写法」的嫌疑在结构上不成立;嫌疑在「波动 / 换手 / 动量反转」这一侧(基线的 rank 相关:20 日波动 −0.47、换手率 −0.46)。

**重复使用的中间量**:`log(Volume)` ×2、`g`(对数量差)×4、它的全天均值与 std 各 ×2。整棵树 60 个节点里,
`E..K`、`N..O` 都只是为了造两个掩码;取数的只有 `in_sustain_stddev(·, Ret, 5)` 两次、`day_mean` 两次。
所以它可以读成 `D × fold( stat_at(掩码₊, Ret) − stat_at(掩码₋, Ret) )`,可以独立替换的零件是:
**符号载体 `D`、权重 `S`(及其内部的掩码 / 统计量 / 折叠)、乘法、以及口径里的 EMA**。实验按这四个零件拆。


### 研究员对这棵树的理解(原文照录 `notes/F110_ret_fair_log/04_grammar.md`)

把分解表的结构角色串起来,这棵树的语法是:

```
符号载体(A..D):   当天开盘 → 收盘的日内收益                                   —— 每股票-日一个带符号的数,带收益尺度
事件掩码 ×2(E..K, N..O): 对数成交量比上一有成交分钟 高 / 低 出当天 1σ          —— 每股票-日两串 0/1,不带任何尺度
    -> 挂在事件上的短窗统计量 ×2(L, P): 触发分钟起 5 分钟(含自己)的收益总体 std   —— 只在触发分钟有值
        -> 日内折叠 ×2(M, Q): 当天所有触发点的等权均值                          —— 两个正数,量纲是波动
            -> 作差再取绝对值(R, S): |放量侧 − 缩量侧|                          —— 非负权重,量纲仍是波动
乘法(T):           符号载体 × 非负权重                                         —— 带符号、对收益齐次度 2
    -> (回测口径)因果 EMA,半衰期 20 天;方向取负                               —— 「按 S 加权的日内收益累积」的反转
```

三点是这棵树特有的:

1. **符号和幅度来自两条互不相干的支路**。`D` 决定排在哪一头,`S` 只决定当天这一笔算多重。所以要问的不是「门控还是两个信号」
   (`S` 恒非负,单独拿出来不带方向),而是:**权重 `S` 换成最朴素的波动水平、换成 1(不加权)、换成 `|D|` 自己,还是不是同一条因子**。
2. **权重是「两个高度重叠的量之差的绝对值」**。差的符号被 `abs_` 抹掉了,差的大小混着三样东西:波动水平、成交量脉冲处的价格冲击、
   以及两个均值各自的抽样噪声。哪一样在起作用,要靠替换实验分开。
3. **没有日轴记忆,记忆全在口径的 EMA 里**,而且基线的半衰期扫描在网格上限(20)处还在单调改善。
   对只能做多的用户,「再平滑一点」是不是还能把多头腿净超额从零往上抬,是这棵树上第一个要回答的升华问题;
   它需要把平滑写进表达式(`cross_mean` 等),因为口径的半衰期网格到 20 为止。


## 4. 假设表

下面是研究员在跑实验**之前**写的假设表(原文照录 `notes/F110_ret_fair_log/05_hypotheses.md`)。**其后的实验结果没有回填**:
每条假设现在是「未验证 / 被支持 / 被否定」,要对照第 2 节列出的运行结果重新判定。

**写在任何实验之前**(此时手里只有 S0 基线、源码和探针读数)。每条写「它预测什么」「哪个实验能杀死它」。
判据里的噪声尺度按手册:多头腿净超额 ±3 个点、纯多头夏普 ±0.3、多空夏普 ±0.3;「同一半衰期下比」指固定半衰期 20。

基线给的四个事实是这些假设的出发点:(a)多头腿净超额 −0.0% / −0.6%(train / valid),毛超额 +8.0% / +7.4%,全被 10.6% 的日换手吃掉;
(b)空头腿毛超额 +43.3% / +46.8%,多头腿只占毛价差的 16% / 14%;(c)分位剖面是「Q1 悬崖(−43.5%)+ Q4~Q10 一块平台」,多头端 Q10 不高于 Q7~Q9;
(d)半衰期扫描从 0 到 20 单调改善,20 是网格上限;rank IC 随持有期一路升到 h20 的 +0.106。

| # | 假设 | 它预测什么 | 哪个实验能杀死它 |
|---|---|---|---|
| **H1** | **权重 `S` 只是日内波动水平的含噪代理** | `S` 与 `day_std(Ret)` 的日截面 rank 相关高(> 0.7);把 `S` 换成 `day_std(Ret)`,交易信号与原式 rank 相关 ≥ 0.9,同一半衰期下 rank IC、两本书都不差 | X1-C / S1:`D × day_std(Ret)` 与原式相关 < 0.8,或两段数据上多空夏普都低 0.3 以上、多头腿毛超额都低 3 个点以上 |
| **H2** | **放量 / 缩量事件机器不携带信息**(F101 的先验:放量掩码对多头腿没有贡献,换成不用 Volume 的版本分不开) | `D×M`、`D×Q`、`D×(全部分钟的 5 分钟滚动 std)` 与原式等价;去掉波动水平之后的「纯不对称」`S/σ` 当权重反而更差 | X1-C:`D×(S/σ)` 好于 `D×σ`(说明 `S` 里超出波动水平的那部分有用);或 `D×M` 明显不同于 `D×S` |
| **H3** | **`abs_` 是 no-op**:放量侧波动几乎总是大于缩量侧(`M − Q > 0`) | `M < Q` 的股票-日占比 < 5%;`D×(M−Q)` 与原式 rank 相关 > 0.98 | X1-B:`M < Q` 占比 > 15%;X1-C / S1:`D×(M−Q)` 与原式不同 —— 那样 `abs_` 就是一次真的折叠,`S` 量的是「两侧差多少」而不是「放量侧多出多少」 |
| **H4** | **乘法是带符号的凸化**:`D·S ≈ sign(D)·D²`,大的日内涨跌被放大。因子 ≈ 「过去一两个月最大的几次日内涨跌的带符号和」 | `D×\|D\|` 与原式等价(相关 ≥ 0.9、书相同);不加权的 `D` 弱于它们(凸化有用) | X1-C / S1:`D` 单独不弱于原式(凸化多余,它就是普通的日内反转);或 `D×\|D\|` 明显差于 `D×S`(`S` 带了 `\|D\|` 没有的东西) |
| **H5** | **起作用的是「日内」这个分量**(A 股 T+1 下的日内 / 隔夜拔河),不是普通的收盘到收盘反转 | 把 `D` 换成收盘到收盘收益,rank IC 和空头腿明显变弱;换成隔夜收益,方向反过来或没有预测力 | X1-C / S1:`收盘到收盘收益 × S` 不弱于原式 —— 那它就是「20 日反转 × 波动」,落在 `ctl_mom20` / `ctl_dvol20` 上 |
| **H6** | **钱在空头腿 = 近期被日内拉高的高波动票回落;多头腿没有独立的选股信息** | 把 `T` 拆成正部 `T⁺` 和负部 `T⁻`:rank IC 与空头腿几乎全在 `−EMA(T⁺)` 上;多头十分位的毛超额不高于 Q4~Q9 的平均;只用 `T⁻` 排出来的多头腿不比平台好 | X1-C / X1-E:`−EMA(T⁻)` 单独的多头十分位毛超额在 train 和 valid 上都比 Q4~Q9 平台高 3 个点以上,且 20 分位剖面在多头端单调 |
| **H7** | **空头腿被「买不进的票」抬高**:空头端是日内大涨的票,其中次日开盘封板的标签是 NaN、在空头里记 0 | 换成不带可买入过滤的标签,空头腿毛超额掉 5 个点以上、多空夏普掉 0.5 以上 | X1-F:掉幅 < 2 个点、< 0.2(这只影响多空口径,不影响多头腿) |
| **H8** | **它是已知暴露(换手率 / 20 日波动 / 动量反转)的平滑、非线性写法** | 基线 9 个线性控制 R² 只有 0.349,但控制变量没有按同样的方式平滑、也没有「带符号 × 波动」这种形状;用**同口径**的对照(`−EMA20(D)`、`−EMA20(D×σ)`、平滑后的波动)去张,R² 升到 0.7 以上,残差 rank IC 与多头腿毛超额归零 | X1-G:同口径对照下 R² 仍 < 0.5,且残差 rank IC > +0.02、残差多头腿毛超额 > +4%(两段都是) |
| **H9** | **半衰期 20 是网格上限而不是最优;更长的平滑继续抬高多头腿净超额** | 半衰期 30 / 40 / 60 下多头腿净超额在 train 和 valid 上都单调上升(毛超额掉得比换手慢) | X1-D:半衰期 40 或 60 的多头腿净超额在 train 或 valid 上不高于半衰期 20 |
| **H10** | **多头端不单调(Q10 < Q7~Q9)是因为「高波动的暴跌票」被 `S` 的波动尺度推到了最顶上**;去掉尺度(截面排名后再乘、或 `D` 不加权)能把多头端修平 | 去尺度版本在同一半衰期下多头十分位毛超额更高、20 分位剖面多头端单调 | X1-C / X1-E:去尺度版本的多头腿在两段上都不好于原式 |
| **H11** | **对只能做多的用户,它相对已知的成交额水平家族没有增量** | 对 `cross_mean(day_std(Amt), 30)` 中性化后的残差多头腿毛超额 ≤ +2%;与它相加之后多头腿净超额不比它单独高出噪声(3 个点 / 0.3 夏普) | X1-H:相加之后的多头腿净超额在 train 和 valid 上都高 3 个点以上,或残差多头腿毛超额两段都 > +5% |
| **H12** | **幸运参数**:5 分钟窗口、1σ 阈值是调出来的 | 窗口换成 3 / 10 / 15 明显变差 | S1:邻域里各档与原式在噪声内 → H12 死 |
| **H13** | **收盘集合竞价那一格污染了 `M`**(探针:最后一格触发放量时窗口只剩 1 分钟、std = 0) | 绝大多数股票-日最后一格都触发放量;把最后几格切掉,`M − Q` 的符号分布变了,但因子表现不变 | X1-B / S1:切掉之后表现明显变了 —— 那这条因子的内容就依赖 241 网格的版式(沪市 2018-08-20 之前没有收盘集合竞价),是制度伪影 |

**事前的主猜想**(写下来以便事后对照,不是结论):H4 + H5 + H6 成立 —— 它是「凸化的日内反转」,预测力在空头端的拉升票上,
`S` 的事件机器可以整个换成 `day_std(Ret)` 甚至 `|D|`(H1、H2),多头腿只是「不在被拉升的那 20% 里」。
如果是这样,提纯的结果是一个 4~6 个算子的式子;升华的空间主要在平滑(H9)和「对已知家族有没有增量」(H11)上,而不在结构上。

**实验安排**(服务器运行不超过 8 次,含 final):

1. `x1_anatomy.py`(exec):在 numpy 里把 `D`、`M`、`Q`、`σ` 四个基础面板自由组合 —— 一次回答 H1~H11、H13 的大部分(同一半衰期下比结构、延长半衰期、拆正负部、腿的构成、同口径中性化、对已知家族的增量)。
2. `S1`(run):把 X1 里起决定作用的替换写成表达式,进正式的阶段表(连同窗口邻域 H12、切掉首尾格 H13)。
3. `S2`(run):提纯出来的结构 + 写进表达式的平滑 + 多头腿候选;必要时再跟一个 exec 量它们对已知家族的增量。
4. `S_final`(final):≤ 5 个候选,含原式与一条已知家族基准;读之前把排序和判据写进 `10_distilled.md`。

## 5. 当前的候选(提纯 / 升华)

(没有留下。研究还没进行到选候选的阶段,或者候选只在研究员脑子里。)

## 6. 后面的研究思路(研究员已经写进配置和脚本、但还没做完的)

- 阶段 **S0_baseline**(已有结果):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
    - `v_base` = `mul(sub(div(day_last(Close), day_first(Open)), 1), abs_(sub(day_mean(in_sustain_stddev(is_gt(sub(log(Volume), in_forward_valid_part(log(Volume))), add` —— 原始表达式
- 脚本 `studies/F110_ret_fair_log/probes.py`:Probes this tree needs:  D * | M - Q |

    D = Close_last / Open_first - 1
    G = log(Volume) - in_forward_valid_part(log(Volume))          (minute log-volume change)
    M = day_mean(in_sustain_stddev(G > mean(G) + std(G), Ret, 5)) (5-min return std hanging off volume SURGES)
    Q = day_mean(in_sustain_stddev(G < mean(G) - std(G), Ret, 5)) (the same hanging off volume DROPS)

The built-in probes are blind here for three reasons: the trigger kernel is fed random floats (mask == 1
never holds, so every built-in reading on `in_sustain_stddev` is vacuous), `in_forward_valid_part` is a
LOOKUP w
- 脚本 `studies/F110_ret_fair_log/x1_anatomy.py`:F110 X1: anatomy of  T = D * |M - Q|  and of the signal that is actually traded, -EMA20(T).

The tree has no day-axis operator: everything that makes it tradable is the EMA of the convention.  So the
structural questions can be asked in numpy on four base panels (D, M, Q, sigma = day_std(Ret)), at ONE fixed
half-life, which is the only clean way to separate "structure" from "smoothing":

  0  self-checks     T == D*|M-Q| ?  does the helper reproduce the S0 table row?
  B  what is S       sign of M-Q (is abs_ a no-op?), trigger counts, surge->drop adjacency, the closing-auction
                

## 7. 留出段

未读。读之前要先在 `10_distilled.md` 里写下候选排序和判据。

## 8. 给接手者的提醒

- `x1b`(10-04 13:09 用 exec 启动)在服务器上跑着或已跑完,**结果没人读过**:`./scripts/study.sh wait F110_ret_fair_log x1b` 拉回来看。
- 上一位研究员的完整动作流水(含每条命令的输出):`handoff/F110_ret_fair_log/agents/`。
- 这一页是自动汇编的;你读完材料、形成判断之后,**按 playbook §7 的 8 节把它整个重写**。
