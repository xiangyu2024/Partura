# 结构解剖:种子 803,B 组,第 2 轮

读的东西:`r2/loc.md`、`r2/loc.json`、`r2/R_prev.json`、`r1/loc.md`、`r1/analysis.md`、`r1/lit.md`、`r1/missions.yaml`、`notebook.md`、`PLAN.md`(含 7 条修订);
代码:`scripts/c05_locate.py`、`scripts/c05_round.py`、`scripts/c05_check.py`、`scripts/idea_search.py`、`partura/steer.py`(reward / neutral_basis / neutral_residual)、`partura/diagnose.py`、`partura/ops_ext.py`、`partura/probes.py`、`partura/lab.py`、
`$HOME/Desktop/AlphaCube-steering/src/alphacube/operators/{common,dt_day,dt_cross,dt_in,nd_ts}.py`、`catalog.py`。
**没有读**:其他种子目录、A / B0 组的任何东西、C01–C04、`guidance/C0*`(含 `C05_base.yaml`)、`runs/ lab/ notes/ studies/ handoff/ batches/ docs/ episodes/`、任何测试段数字。

证据分四类:**(定位)**= 定位工具/R 真给出的数;**(源码)**= 读代码确认的语义;**(算术)**= 我在本机用随机张量对算子本身做的数值验证(不碰任何数据,脚本在 scratchpad);**(推断)**= 未经付费评估检验。

---

## 0. 本轮的信息量,和一句先说的话

(定位)快照 4 个运行、6 个 heads、210 个已评分存档候选;共性表 13 行;拆解 18 次付费评估(预算 48,又作废 30);R 的 16 行全部回来了,0 个替换。

本轮和第 1 轮最大的不同:**第 1 轮什么都没测到,第 2 轮三件事被真正测死了**——
(1) `day_kurt(Ret)` 的来源被 16 个换件钉住了(§1.3);
(2) M 第 2 批给出一个四条轴全部站得住的核心(§1.1),而且它的「新信息」在构造上不可能是波动、成交额或市值的改写;
(3) 库里分数最高的那个 head 有一个**制造出来的、约 12.8% 的格子的假值块**(§1.1.4、§2.1),这是本轮最硬的一条「烂部件」。

同时有一条工具层面的警告必须先说:**本轮的共性表不能当证据用**(§1.5)。

---

## 1. alpha 的来源

### 1.1 核心 A:`ts_skew(day_durbin_watson(Open), 50)` —— 本种子目前唯一四条轴都站得住的真来源

(定位)四条轴:

| 轴 | 证据 |
|---|---|
| 共性 | 均值差 +2.35,p 0.000,11 个候选含它(父结构 `day_durbin_watson(Open)` 25 个,p 0.000)——**但见 §1.5,这一列本轮不可信** |
| 充分性 | 它单独当因子 score **+1.18**(train 1.1787 / valid 2.2607),是所在 head(1.56)的 **75%**;它自己也是快照里第 2 高的 head(1.23) |
| 必要性 | 去掉外层 `ts_skew` 只剩 `day_durbin_watson(Open)`:score **−2.13**(train −2.1281 / valid −0.1089)。**外层不是装饰,是全部** |
| 敏感性 | 窗口 50→25:+1.06;50→100:+1.28;字段 Open→Close:+1.43。三个方向都不崩,**没有刀锋** |

#### 1.1.1 它到底在算什么:`day_durbin_watson` 在价格上不是自相关,是已实现方差

(源码)`day_durbin_watson` 的分母是 **Σx²,不是去均值平方和**(`dt_day.py:273`)。`partura/probes.py` 的开头把这件事写成了它存在的理由:「the answer (it divides by sum-of-squares, not by the variance) is what turns it from *an autocorrelation test* into *realized variance*」;`partura/lab.py` 的开头把「`day_durbin_watson` on a price level is realized variance」列为跨研究必须带走的结论之一。

(算术,本机 2000×241 随机价格路径)我自己验了一遍:

- `day_durbin_watson(P) / mean(分钟收益²)` = **0.9959 ± 0.0012**,秩相关 **1.0000**;
- `day_durbin_watson(P) / day_std(Ret)²` = **0.9996**;
- `day_durbin_watson(100·P) / day_durbin_watson(P)` = **1.000000**(乘性标度不变 → **后复权因子被约掉**,它读的是相对波动,不是价格水平);
- 加常数会变(非位置不变)。

所以 **`day_durbin_watson(Open) ≡ day_var(Ret)`,误差 0.4%**。裸用它 score −2.13 完全合理:它就是日内方差,而控制里有 `cross_mean(day_std(Ret), 20)`。

> **真正的新信息 100% 在 `ts_skew(·, 50)` 这一层**:这只股票**自己**过去 50 天的日内方差序列**偏不偏**。方向 −1 = 做多偏度最低的一端 = 过去两个半月里**没有出现过孤立的爆波动日**、方差天天差不多的股票。

#### 1.1.2 为什么它在构造上不可能是波动 / 成交额 / 市值的改写

(算术)`ts_skew` 对窗口内的仿射变换不变:`ts_skew(a + b·X, 50) − ts_skew(X, 50)` 的平均绝对差 = **5.1e−7**。
所以**任何按个股固定的乘性标度(平均波动水平、平均成交额水平、价格水平、后复权因子、股本)都被这一层整除掉了**。这正是「裸 DW −2.13 → 包一层 +1.18」的机制:控制拿掉的是水平,`ts_skew` 读的是**形状**,两者在构造上正交。

(定位)配套的数:`rho_known` 只有 **0.1886**(已知族 `cross_mean(day_std(Amt), 30)`),远低于 0.5 的不合格线。

这比 `day_kurt(Ret)` 干净得多:`day_kurt(Ret)` 躲波动控制靠的是「自己把尺度除掉了」,但它的**形状本身**被零收益质量污染(§1.3);`ts_skew(DW, 50)` 的形状是在**日这条轴**上取的,日内的零质量只影响每一天的水平,被仿射不变性吃掉一大半。

#### 1.1.3 还没排除的混淆(两条,都该在本轮买掉)

1. **名义价格 / 价格网格**。价格网格是**形状**(0 上的点质量),不是标度,所以仿射不变性救不了。(推断)低价股的分钟价差量化粗 → 日内方差由少数几跳构成 → 它的 50 日方差分布更偏。这条轴本轮在三个地方同时冒头(§1.4 的 `neg(LogFloatShares)`、r1 的 R 第 12 行、这里),是本种子最该一次性测死的混淆。
2. **上市年龄 / 燃烧期**。`ts_skew(·,50)` 需要 50 天历史,`nanskew_last` 跳 NaN,所以次新股与复牌股拿到的是**少数几个点算出来的偏度**,噪声极大且更容易取极值。控制里**没有** `ListAge`。head 2 的 coverage 0.9983,问题不大;但它的父结构把这件事放大成了一个假值块(下一条)。

#### 1.1.4 head 1 比 head 2 多出来的 +0.38,是训练段的,而且带一个 12.8% 的假值块

head 1 = `cross_autocorr_s1(ts_skew(ts_skew(day_durbin_watson(Open), 50), 50), 3)`,1.56。两件事:

**(a) 里面那层重复的 `ts_skew` 完全无用。**(定位)knockout 掉它 → `cross_autocorr_s1(ts_skew(day_durbin_watson(Open), 50), 3)` score **1.5565**,必要性 **+0.0065**。而且 `ts_skew(ts_skew(day_durbin_watson(Open), 50), 50)` 自己 **coverage 0.8708,门槛废品**(100 天燃烧期)——一个连自己都求不出值的子树。

**(b) 那 13% 求不出值的格子没有变成 NaN,变成了精确的 0.0。**(源码 + 算术)`cross_corr` 里 `count.clamp(min=1)` 加 `cov/(sqrt(var_x·var_y)+EPS)`:窗口里**有效对 ≤ 1 时输出恰好 0.0**,**= 2 时输出恰好 ±1**。我在本机用一个前 12 天为 NaN 的列验过:`cross_autocorr_s1(x, 3)` 给出 `nan, 0, 0, 0, …, 0, +1, −0.02, …`——**13 个连续的 0.0**;`cross_autocorr_s1(x, 2)` 的全panel取值集合**就是 {−1, 0, +1}**。

对得上定位里的三个数:head 1 的 coverage **0.9987** 对输入的 **0.8708**,差 **0.1279**;两个窗口变体的 distinct 分别是 **0.8904**(d=2)和 **0.9041**(d=6),即约 **10–11% 的并列**;而 knockout 版(输入 coverage 0.9983)的 distinct 是 **0.9979**,几乎没有并列。

> 结论:**head 1 有约 12.8% 的格子(历史不足 100 天的次新股 / 复牌股)被填成常数 0 或 ±1**,这不是数据,是 `cross_autocorr` 的 NaN 处理造出来的。knockout 版把假值块压到 0.2% 而 score 不变(1.5565 vs 1.5630,差 0.0065,见 §1.6 的复现噪声 ≈0.05),所以**这个块对 score 的贡献 ≈ 0,它纯粹是脏**。

**(c) 多出来的 +0.38 是训练段的。** 把整个家族的 train / valid 并排看(定位):

| 表达式 | train | valid |
|---|---|---|
| `ts_skew(day_durbin_watson(Open), 25)` | 1.06 | 1.64 |
| `ts_skew(day_durbin_watson(Open), 50)` | 1.18 / 1.23 | 2.26 / 2.29 |
| `ts_skew(day_durbin_watson(Open), 100)` | 1.28 | **2.47** |
| `ts_skew(day_durbin_watson(Close), 50)` | 1.43 | 2.23 |
| `cross_autocorr_s1(ts_skew(·,50), 3)`(knockout) | 1.56 | 2.06 |
| head 1(双 `ts_skew`) | 1.56 | 2.07 |
| head 1 的 Close 版 | 1.33 | **2.39** |
| head 1 窗口 2 / 窗口 6 | 1.44 / 1.61 | 2.01 / 2.17 |

**valid 全家族都在 2.0–2.5,train 在 1.06–1.61。score = min(·) 永远被 train 卡住,所以族内的一切分差都是 train 侧的抖动。**
`cross_autocorr_s1` 那一层把 train 从 1.18 推到 1.56,valid 却从 2.26 掉到 2.07 —— **它买的是训练段**。

**这条对整个判读很重要:核心 A 这个族在 valid 上非常稳(2.0–2.5),族内的排序不稳。所以不要花钱在族内微调上(包括 Open↔Close),要花钱在「核心之外有没有别的东西」和「混淆排掉之后还剩多少」上。**

### 1.2 核心 B:`sub(day_centroid(Amt), day_centroid(Ret))` —— 第二个真来源,是「时点」这条全新的轴

(定位)充分性:`day_centroid(Amt)` 单独 **−0.0846**(valid 0.5839),`day_centroid(Ret)` 单独 **−1.3836**(方向 +1,valid −0.4808);head 本身 **0.904**。
敏感性:`Amt→Volume` → **0.884**(差 0.02,噪声内)。没有窗口、没有可跳的算子,所以必要性与窗口两列是空的(不是 ≤0)。

> **两半单独都是废的,差值 0.90。这是本种子最干净的「交互才有信息」的例子**,也是全库唯一不读「波动形状」的 head。

(源码)`day_centroid(x)` = `Σ(t·|x|)/Σ|x|/(T−1)` ∈ [0,1],是 |x| 在分钟轴上的**重心**;文档串自己点明用在 Volume / Amt 上读的是「*when* in the day the trading happened -- information that every order-free statistic (std, kurt, gini) throws away」。
所以 head = **成交的时点 减 波动的时点**,方向 −1 = 做多「成交偏早、而波动偏晚」的股票。五个控制(成交额水平、日内波动、20 日反转、已知族、市值)**一个都不含日内时点**,`rho_known` −0.1943。它不是代理。

(推断)两条没测的风险:(a) 241 根分钟的最后一根含**收盘集合竞价**,`day_centroid(Amt)` 很可能主要被这一根驱动(指数成分 / ETF 标的的尾盘量占比),那它就更像一个「尾盘量占比」因子;(b) `day_centroid(Ret)` 用 |Ret|,可能被一根大打印主宰(`day_gini` 的文档串警告过 `day_kurt` / max-share 的同类毛病)。两条都有现成的 R 测法(§4.2)。

### 1.3 `day_kurt(Ret)`:16 个换件把它判成「一分钟吃掉全天、其余时间躺平」,是半代理

(定位,R_prev)16 行全部过门槛(r1 预测的 0–2 个门槛废品 → **实际 0 个**,`cross_ema` 包装 k/241 型比例以过 distinct 的办法奏效:`cross_ema(day_zero_ratio(Ret), 10)` distinct 0.9998)。按信息量排:

| 换件 | score | rho_head | 读出什么 |
|---|---|---|---|
| `day_kurt(in_pct(Close, 1))` | **0.9685** | **1.0000** | `Ret` ≡ 日内 1 分钟 Close 收益。**r1 怀疑的「首根 bar / 隔夜跳空」被证伪,这条可以销案** |
| `day_kurt(in_logchg(Vwap, 1))` | **0.0241** | 0.8065 | 只在**真的成交过的分钟**上算同一个统计量 → **alpha 从 0.97 掉到 0.02**。零收益质量是**必要**的 |
| `day_kurt(in_pct(Close, 5))` | 0.3786 | 0.7943 | 聚合到 5 分钟、零质量变少 → alpha 也跟着少。同一方向 |
| `div(day_max(Ret), day_std(Ret))` | 0.3998 | **0.8729** | 尺度无关的 MAX 和它 **87% 同号** → 它很大程度上就是「最大一跳 / 当日波动」 |
| `cs_rank(day_kurt(Ret))` | 0.5364 | 0.8598 | 先截面秩再给奖励做 EMA → 掉 0.43 |
| `log(add(day_kurt(Ret), 5))` | 0.8262 | 0.9350 | 压尾 → 掉 0.14 |
| `cross_med(day_kurt(Ret), 20)` | 0.4982 | 0.8420 | 20 日中位数(抹掉尖峰日)→ 掉 0.47 |
| `cross_ema(day_zero_ratio(Ret), 10)` | −2.2809 | **−0.4375** | 零收益比例**自己**是废的,而且和它**反号**相关、|ρ|<0.5 |
| `log(div(day_sum(Amt), day_sum(Volume)))` | −2.0600 | **−0.5115** | 名义价格自己是废的(方向 +1 = 做多高价),|ρ| 刚过 0.5 |
| `day_gini(Ret)` | −0.2743 | 0.2074 | 有界集中度只和它 21% 相关,而且 **`rho_known` = −0.626**:gini(Ret) 本身就是已知族的另一种写法 |
| `day_es_ratio_hi/lo`、`day_skew(Ret)` | −0.63 / −0.57 / −1.96 | 0.43 / 0.45 / 0.42 | 单侧尾部、三阶矩都不是它 |
| `cross_ema(day_at_max_ratio(Close), 10)` | −2.3294 | −0.2111 | 封板频率不是它(H3 的封板分支否) |
| `day_kurt(Amt)` | −4.9558 | 0.1279 | 成交额的形状和它无关,而且有害 |
| `cross_ema(day_flat_run_max(Ret), 10)` | −3.5073 | −0.1399 | 最长静止段也不是它 |

**把 r1 笔记里的四个假设重新定权(定位证据,不是先验):**

- **零质量是必要条件,但零质量的任何单一代理都不是它**:拿掉零分钟 → 0.02(必要);而 `day_zero_ratio`、名义价格、`day_flat_run_max`、`day_at_max_ratio` 四个代理的 |rho_head| 全 ≤ 0.52、score 全为大负数(不充分)。所以「H1 成交稀疏」「H4 价格网格」**不能**说「这个 head 就是那个原子的改写」。
- **「峰值记忆」是好部件,不是烂部件**:r1 预测 `cs_rank` / `log(kurt+5)` / `cross_med` 至少一个会**高于** 0.97,实际**三个全低**(0.54 / 0.83 / 0.50)。按 r1 自己写下的判读条件,这说明 **alpha 就在「出没出现过尖峰日」这件事上**,而且原始重尾值在 EMA 之前必须保留。
- **最接近它的单一改写是尺度无关的 MAX(rho_head 0.87)**:所以它读的是「一分钟吃掉全天的跳 + 其余时间躺平」这个**复合**,两个成分分别对应 H3(彩票 / 跳)和 H1/H4(躺平 = 零质量),**单独任何一个都复现不出来**。
- **H2(与零质量无关的真尾部形状)基本死了**:gini、es_ratio_hi/lo、skew 全废。

> 判定:**半代理**。它不是流动性或彩票因子的直接改写(没有一个代理能替代它),但它的两个成分都是最老的两个摩擦。库里留着它合适;**不建议把它第 2 个 E 位用掉**(§4.1)。

### 1.4 代理与伪来源(不要当核心)

- **`neg(LogFloatShares)`(机械核心卡第 3,均值差 +2.10,p 0.0046,n=4)—— 代理。**(源码 + 推断)定义上 `FloatCap = 价格 × FloatShares`,而控制里有 `LogFloatCap`。所以 `LogFloatShares` 对控制取残差后 ≈ **−log(名义价格)**。它不是新信息,是「给定市值之后的价格水平」这条**没被控制的轴**;r1 的 R 第 12 行(名义价格,|rho_head| 0.51)指的是同一条轴。
  → **别给它 E 位**;把它当**条件变量 / 混淆项**去测(§4.2 的 `sub(LogFloatCap, LogFloatShares)` 就是精确的 log 名义价格,只用允许的日频叶子就能写出来)。
  这也顺手解释了 `sub(day_centroid(Amt), LogFloatShares)`(0.53):它 ≈ 「成交时点 + 低价」,是核心 B 掺了一条价格轴,不是第三个结构。
- **`day_durbin_watson(Open)` 裸用(机械核心卡第 4,n=25,p 0.000)—— 伪来源**:−2.13,就是日内方差(§1.1.1)。它进核心卡只是因为共性表按均值差排,而它是 M2 那一批的共同前缀。
- **`day_gini(Ret)` —— 已知族的改写**:`rho_known` −0.626,|ρ| ≥ 0.5 **本身就不合格**。它是 r1 E 任务产出那个 head 的第二个成分(§2.3)。
- **`day_kurt(Amt)`、`day_sum(Amt)`、`day_argmin(High)`** 在共性表里都是负的——但见下一节,这些负号本身不可信。

### 1.5 工具警告:本轮的共性表被「运行身份」混淆了,p 值不能用

(源码,`c05_locate.py` 第 203–233 行)共性把**快照里 4 个运行的存档合并成一个 210 条的池子**,然后比较「含某子树」与「不含」的 score 均值,附 Mann–Whitney p。问题是这 4 个运行**不是同一个实验**:

- `c05s803Br1a_Ea` 是 E 任务:**它存档里 100% 的候选都含 `day_kurt(Ret)`**(`--must-contain`),而且它的奖励**多一个控制向量**(核心的家族进了 `--neutral-extra`),所以它的候选在构造上就比别人低一截。
- `c05s803Br1b_Nb` 是 N 任务(种子占一半),M1 / M2 是普通 GP。

对得上的数:`day_kurt(Ret)` 的 n_with = **55**,均值差 **−0.83**,p **0.9948** —— 这几乎就是「Ea 那一批的存档(mean −2.19)比另外三批(mean −1.36)差」,**不是「含 `day_kurt(Ret)` 的候选更差」**。同一个机制让 `cross_fangzheng(day_kurt(Ret), 15)`、`day_argmin(High)`、`div(day_argmin(High), day_kurt(Ret))` 全部带上负号(它们都是 Ea 的东西),也让 `ts_skew(day_durbin_watson(Open), 50)`(M2)和 `day_centroid(Amt)` / `neg(LogFloatShares)`(Nb)的正号被抬高。

> **共性表这一轮只能当「哪个运行分数高」读,不能当「哪个子树好」读。** 幸运的是:核心 A 的判定**不依赖**共性表——它靠的是拆解的充分性(+1.18)、必要性(−2.13)和三个方向的敏感性,这三样都是**同一个运行内**的对照。写任务时请把论据挂在拆解上,不要挂在 p 值上。
> (另外,E 任务的存档会机械地把它的核心推上共性表,**这会让 B 组每一轮都倾向于再深挖上一轮的核心**——一个该记在判读局限里的自我强化回路。)

### 1.6 两条给 PI 的标尺(本轮才第一次能量出来)

1. **`score` 的复现噪声 ≈ 0.05。** 同一个表达式 `ts_skew(day_durbin_watson(Open), 50)` 在 M2 挖掘里是 **1.2257**,在 locate 里重算是 **1.1787**,差 **0.047**(两处都是 train 卡住,同一奖励、同一时段)。R 的 +0.1 替换线只有这个差的 2 倍 —— **任何 0.05–0.15 的「改进」都要当噪声看**。
2. **rho_head 0.8–0.94 完全保不住 score。** 同一个 head 的改写里:rho_head 1.00 → 0.97;0.935 → 0.83;0.873 → 0.40;0.860 → 0.54;0.842 → 0.50;0.807 → **0.02**。
   → 在这个环境里「高度相关的改写」照样可以掉 0.5–0.95 分。所以 (a) 换件实验必须看 score 不能只看 ρ;(b) 反过来,**库里 ρ<0.7 的两个 head 可以是同一个经济机制的两种写法**,判读时不要以为去重就等于独立。

---

## 2. 烂部件

### 2.1 已证明的烂部件:head 1 里面那层 `ts_skew`(必要性 +0.0065,且制造 12.8% 的假值)

(定位 + 源码 + 算术,见 §1.1.4)这是本轮唯一**必要性 ≈ 0 而且有明确机制说它有害**的部件:它把输入的 coverage 从 0.9983 压到 0.8708,逼 `cross_autocorr_s1` 用 `count.clamp(min=1)` 把 12.8% 的格子填成常数 0.0 / ±1(distinct 0.89 vs knockout 的 0.998),而 score 一点没变。
**R 动作**:`cross_autocorr_s1(ts_skew(day_durbin_watson(Open), 50), 3)` 已经测过(1.5565),**不要再付钱**;值得付的是 knockout + 最好窗口的组合 `cross_autocorr_s1(ts_skew(day_durbin_watson(Open), 50), 6)`(未测;窗口 3→6 在双层版上值 +0.049)。
**诚实提醒**:按 §1.6 的标尺,它大概**到不了 +0.1 的替换线**(估计 +0.05)。所以这一条的价值主要是**判读与归因**(库里最高分的 head 有 1/8 的格子是假的),不是真能换掉它。

### 2.2 换掉反而更好、但我判为噪声:head 2 的 `Open`

(定位)`ts_skew(day_durbin_watson(Close), 50)` = **1.4328**,比 head 的 1.2257 好 **+0.207**,rho_head **0.9424**,|rho_known| 0.1933 —— **按 §2.5 的规则完全够资格替换**,而且它已经在 `r2/loc.md` 的 R 候选表里。
但两条反证:(a) **同一个字段换在 head 1 上是 −0.23**(1.3334 vs 1.5630);(b) valid 基本不动(2.2295 vs 2.2607,略差)。所以 Open↔Close 的差是 §1.1.4 说的 train 侧抖动。
**建议**:`r_candidates` 里的东西**不会自动生效**(源码:替换只在 `direct` 模式里写出),要生效必须在 `missions.yaml` 的 R 里再列一次、花掉 16 次中的 1 次。花 1 次把规则认可的 +0.21 落袋**风险低、收益也低**(rho 0.94,对最终融合几乎没有影响),由 PI 定;我不会把它排在 §4.2 的前三。

### 2.3 结构上就弱的 head:`cross_corr(day_kurt(Ret), day_gini(Ret), 241)`(r1 的 E 产出)

(定位)三条都不好看:
- **窗口是刀锋**:241→120 变 **−0.227**(valid 仍 2.298,train 塌了),241→482 变 **−1.137**,方向还翻了号。**只有 241 这一个值能工作**,而 241 ≈ 一年。
- **它的两个成分**:`day_kurt(Ret)` 单独 0.967(**比 head 本身的 0.726 高**),`day_gini(Ret)` 单独 −0.274 且 `rho_known` −0.626(§1.4:本身就是已知族的改写)。
- 它在快照里的 score 0.726 是 6 个 head 里第 5 低。

> 判定:**这是库里最该被换掉的一个 head**。它不是一个「部件烂」的问题,是整棵树靠一个训练段窗口常数站着。好消息是它的分数低(0.726),所以 +0.1 的替换线相对好过——R 在这里的期望收益最高(§4.2)。

### 2.4 不是烂部件(本轮排除掉的)

- `day_centroid(Ret)`:单独 −1.38,但去掉它(= `day_centroid(Amt)` 单独,−0.085)把 head 从 0.90 打到 −0.08。**两半都必要**。
- `day_kurt(Ret)` 的「峰值记忆」:三个去掉它的换件全部更差(§1.3)。**好部件**。
- `day_kurt(Ret)` 的输入 `Ret`:`day_kurt(in_pct(Close, 1))` rho_head 1.00、score 0.9685。**r1 对「首根 bar / 隔夜跳空」的怀疑销案**。

---

## 3. 之前的任务,和第 1 轮的预测对不对

### 3.1 E 位 `c05s803Br1a_Ea`(核心 `day_kurt(Ret)`,用掉它 2 个 E 位中的 1 个)

(定位)评分 80、过线 1、入 heads 1;采样计数 `{c05_no_core: 1322, c05_skeleton: 30}`,**`c05_periphery_seen` 根本没出现(= 0 次拒绝)**。

**试了什么外围、出了什么**:PI 写的 16 个种子分三类(拿掉疑似混淆的分桶 / 截面回归、改时间轴聚合、与成交的共动)。前 5 名里:
- 唯一过线:`cross_corr(day_kurt(Ret), day_gini(Ret), 241)` 0.726 —— **形状来自 PI 的种子 8 / 9**(`cross_corr(day_kurt(Ret), day_sum(Amt), 20)`、`cross_corr(day_kurt(Ret), day_kurt(Amt), 20)`),但**搭档和窗口是 GP 自己选的**(换成 `day_gini(Ret)`、窗口从 20 吹到 241)。hl = 5。
- 其余 4 名全是负分,而且 3 个是 `div(…, day_kurt(Ret))` 或 `div(day_argmin(·), …)` 这种「核心除以 / 被除以一条无关分支」的漂移;**分桶 / 截面回归那一类(种子 1、2、3、13、16)一个都没进前 5**。

**预测核对**:
1. 「产出 heads 概率 40%,若有 1–2 个」→ **1 个,对**。「最可能来自 cross_madz / cross_regres 对自身波动或成交额的残差」→ **错**(来自 cross_corr 共动一支)。「选中的半衰期是 0 或 5,不是 20」→ **对**(hl 5)。
2. 「分桶 / 截面回归类 score 大多 < 0.3」→ **对**(前 5 名里一个都没有,全部 ≤ −0.16)。「若其中某个 ≥ 0.5 说明 H2 有独立 alpha」→ 没有发生,与 §1.3 里 H2 被 R 判死一致。
3. 「GP 会往『核心 + 一条无关的好分支』漂」→ **对**(漂成了 `div`,不是 add / sub,且都没过线)。
4. 「`c05_periphery_seen` < 5,`c05_no_core` 高得多」→ **对,而且极端**(0 对 1322)。

### 3.2 N 位 `c05s803Br1b_Nb`

(定位)评分 65、过线 6、入 heads 2。过线的 6 个里有 3 个是**同一个因子的符号孪生**(`sub(…)`、`neg(sub(…))`、`neg(neg(sub(…)))`,score 全是 0.903975),库的去重只收了 2 个。**所以 N 位实际产出 2 个不同的东西**:`sub(day_centroid(Amt), day_centroid(Ret))` 0.90 和 `sub(day_centroid(Amt), LogFloatShares)` 0.53(后者 ≈ 前者掺了一条价格轴,§1.4)。
(推断,给 PI 的实务提醒:奖励自己选方向,所以 `neg(·)` 包装是纯浪费;N 的种子里不要出现只差一个 `neg` 的写法,也别指望 GP 不去生成它们。)

**预测核对**:
1. 「概率 65%,1–3 个」→ **2 个,对**。「最可能来自量价相关一支(`day_corr(Ret, Amt)`、`cross_mean(day_corr(Close, Volume), 20)`)和带方向的成交额占比」→ **错**。赢家是**成交钟时点**那一支(`day_centroid`),文献依据是 r1/lit.md 的 [S18][S19](Clark 1973 / Oomen 2006,「用成交额当钟」)那一条,不是量价相关那一条。
2. 「自相关一支(ar1 / DW / Hurst)单独过线的可能小」→ **对**(`day_ar1_coefficient(Ret)`、`day_durbin_watson(Ret)`、`cross_mean(day_hurst(Ret), 20)` 都没进前 5)。
3. 「若量价相关出 head,则与 `day_kurt(Ret)` 的 |ρ| < 0.3」→ 无从检验。

**但这里有本轮最值得记住的一条反讽**(源码 + 定位):N 位按**算子名字**理解 `day_durbin_watson`,把它用在 `Ret` 上当「买卖价差反弹 / 自相关」读 —— 在 `Ret` 上它确实是真的 DW(≈ 2(1−ρ₁)),而 PI 预测它「和流动性控制同源、剩不下多少」,**结果正确**。与此同时 **M 第 2 批把同一个算子用在价格水平 `Open` 上,那里它是已实现方差**,再套一层 50 日偏度,拿到 1.23 和 1.56。
> **同一个算子,换一个输入就换一门学科。本种子两个最高分 head 的来源,是 N 位按名字判定「没戏」的那个算子。** 这件事该写进 notebook:**任何以算子名字为依据的先验判断都要先过一遍「它在这个输入上到底算什么」**(`partura/probes.py` 的全部存在理由)。

### 3.3 R(16 次直接评估,0 个替换)

逐条核对 r1 的 8 条预测:

| # | 预测 | 实际 | 判 |
|---|---|---|---|
| 1 | `cross_ema(day_zero_ratio(Ret), 10)` rho_head ≥ 0.5(押 0.5–0.8) | **−0.4375** | **错**(符号与幅度都错) |
| 2 | 名义价格 rho_head 0.3–0.6、方向做多高价、score 五五开 | rho_head **−0.5115**、sign **+1** ✓、score −2.06 | **部分对**(幅度与方向对,符号错) |
| 3 | `day_kurt(in_logchg(Vwap, 1))` < 0.6;`in_pct(Close, 5)` < 0.7 | **0.0241**;**0.3786** | **对**(而且是戏剧性的) |
| 4 | `cs_rank` / `log(kurt+5)` / `cross_med` 至少一个 **高于** 0.97 | 0.5364 / 0.8262 / 0.4982,**全低** | **错**(按 PI 自己写的备选读法:alpha 在「出没出现过尖峰日」上) |
| 5 | `day_gini(Ret)` 过门槛 ✓、rho_head ≥ 0.5、不够 +0.1 ✓ | 过门槛 ✓、rho_head **0.2074**、−0.27 | **部分对**(相关度错;额外发现 rho_known −0.626) |
| 6 | 封板占比与尺度无关 MAX 的 rho_head < 0.5 | −0.2111 ✓;**0.8729** ✗ | **半对**(MAX 恰恰是最像它的那一个) |
| 7 | 0–2 个栽在门槛上 | **0 个** | **对**(k/241 比例套 `cross_ema` 的办法有效) |
| 8 | 本轮替换数 0 或 1 | **0** | **对** |

(第 1 轮笔记 §「留给第 2、3 轮的规则」里的另两条:预测 5「第 2 轮共性表仍然很可能是空的或极少几行」→ **错,13 行**,原因是 E 任务的存档机械地把核心推上表(§1.5),这比笔记预想的 85 条池子大得多;预测 6「M 第 2 批带窗口或 SWAP 字段则拆解会真花钱」→ **对**,花了 18 次。)

**结构性损失记账**(笔记要求跟踪):拆解预算 r1 用 0 / 48、r2 用 18 / 48,两轮作废 **78 次**。不是笔记担心的「连续两轮为 0」,但 B 组在本种子上确实已经扔掉了一半以上的诊断预算。

---

## 4. 本轮候选

### 4.0 先说两条机制约束(选核心时直接影响成败)

1. **家族控制变大了。**(源码,`c05_round.py` 第 143–150 行)E 的家族 = 库里**含该核心**的 heads 前 ≤6 个,全部以 `sign × EMA_hl` 进控制基。
   - 核心 A:家族 = **两个**(1.56 和 1.23)→ 控制基 1 + 5 + 2 = **8** 维。只奖励「这两个 head 之外的新东西」,很硬,但也最诚实。
   - 核心 B(`day_centroid(Amt)`):家族 = **两个**(0.90 和 0.53)。
   - 核心 `day_kurt(Ret)`:家族 = **两个**(0.97 和 0.726,后者含它)。
2. **核心越大越容易被变异打坏。** r1 的核心只有 2 个节点,`c05_no_core` 就被拒了 1322 次;核心 A 有 3 个节点还带窗口 50,(推断)拒绝会更多,PLAN 修订 1 第 5 条那种「退回不含核心的最小树」的计数也会更高(这类候选照样吃预算)。**写 E 种子时请把 16 个位置填满**,别留给机械嫁接。
3. **外围「不得与见过的相同」这一轮开始咬人了。**(源码)`periphery` 是「核心之外**算子名字的集合**」(不含窗口、不含结构、**叶子不算**)。核心 A 在存档里有 11 个含它的候选 → SEEN ≤ 12;核心 B 有 10 个 → SEEN ≤ 11。
   (推断)几乎肯定已在 SEEN 里的:核心 A —— `{ts_skew}`、`{ts_skew, cross_autocorr_s1}`、`{cross_autocorr_s1}`;核心 B —— `{sub}`、`{sub, day_centroid}`、`{neg, sub}`。再加上 GP 最常抽到的单算子集 `{div}`、`{mul}`、`{add}`、`{cross_mean}`、`{cross_ema}`、`{neg}`。
   **建议:外围一律 ≥ 2 个算子,且至少一个是上面没出现过的。**

### 4.1 值得深挖的核心(≤ 3 个,按我的排序)

**① `ts_skew(day_durbin_watson(Open), 50)`(强烈建议本轮用掉一个 E 位)**
理由:§1.1 四条轴全过;新信息在构造上(仿射不变,算术验证 5e−7)不可能是波动 / 成交额 / 市值 / 价格的**水平**;valid 全家族 2.0–2.5;`rho_known` 0.19。
**它周围已经见过的外围写法**(定位输出不打印存档表达式,所以只能从 heads 和共性表反推):
- `{ts_skew}` —— 再套一层 50 日偏度(= head 1 的内层,已证明无用,coverage 0.87 门槛废品);
- `{ts_skew, cross_autocorr_s1}` —— head 1 本身;
- `{cross_autocorr_s1}` —— knockout 版(1.5565,已测);
- 共性表里还有 `ts_skew(day_durbin_watson(Open), 40)`(5 个候选)和裸 `day_durbin_watson(Open)`(25 个候选),说明 M2 在这一族里主要试的是**换窗口和再套同类平滑**;
- **没见过的方向**:条件分组、与第二个结构的秩差、按市场状态调制、与「时点」那条轴的交互。
E 该去问的三个问题(都不是上面任何一个):(i) 把**名义价格 / 零收益比例 / 板块 / 涨跌幅上限**当分组变量,它在组内还剩多少(= §1.1.3 的两条混淆,**这是本轮最该买的信息**);(ii) 它和 `day_kurt(Ret)`(另一个「没有尖峰」的读法)的**秩差**里有没有独立信息;(iii) 它在高成交 / 低成交市场里是不是反向(`cs_flip_by_state` 的文档串自带判决:若只是失效而非反向,翻向版会明显更差)。

**② `day_centroid(Amt)`(第二选择,也可以留给 N)**
理由:§1.2,全库唯一一条「日内时点」的轴,五个控制一个都不碰;它是一个 0.90 的 head 的必要一半;而且它是**Partura 自己(r1 的 N)带来的**,深挖它是 B 组这套架构唯一能自证的地方。
**已见过的外围**:`{sub}`(减 `day_centroid(Ret)` / 减 `LogFloatShares`)、`{sub, day_centroid}`、`{neg, sub}` —— Nb 那一批基本只试了「减掉另一个日频量」。
没见过的:与成交额水平 / 波动的**时序**相关(`cross_corr(day_centroid(Amt), day_sum(Amt), 20)`)、它自己的**异常度**(`cross_madz(·, 60)` = 今天的成交时点比自己平常偏多少)、按板块 / 价格分组、以及(呼应 §1.1 的教训)**它自己 50 日分布的形状**。
风险:收盘集合竞价那一根可能主宰它(§1.2),**这条风险应该先用 R 的 1–2 次测掉,再决定要不要给 E 位**。

**③ `day_durbin_watson(Open)`(备选,不建议本轮)**
它是 25 个候选的共同前缀、核心卡第 4,家族控制会把两个 M2 head 都放进去,所以 E 会被迫去找「日内方差的**另一种**包法」。吸引力在于空间大;问题在于它裸用 −2.13、就是 `day_var(Ret)`,大部分包法会死在波动控制上。**排第三。**

**明确不建议的两个:**
- **`day_kurt(Ret)` 的第 2 个 E 位 —— 不要用。** r1 笔记自己定的条件是「本轮 E 出了 head、**或** R 证明某个换件本身是更干净的核心」。E 出的那个 head 是靠单个窗口常数站着的(§2.3);R 里 **16 个换件没有一个更干净**(最高 0.9685 的那个和它 ρ=1.0,等于没换)。两个条件一个都不硬。把这个 E 位留到第 3 轮,只在 r2 的 R 找出更干净写法时再用。
- **`neg(LogFloatShares)` —— 不要当核心**(§1.4,给定市值的 −log 名义价格)。它该出现在 E 的**分组变量**位置和 R 的诊断位置。

### 4.2 R 目标(≤ 16 次,按期望信息量排;全部已在本机 parse + `is_valid_root` 通过)

**第一优先 —— 把核心 A 的两条混淆测死(4 次,头 = `ts_skew(day_durbin_watson(Open), 50)`)**
1. `ts_skew(day_durbin_watson(Vwap), 50)` —— Vwap 在无成交分钟缺失,DW 的分子只用两端都有效的对,**等于只在成交过的分钟上算已实现方差**。这是对核心 A 做 r1 第 1 号那一刀(当时让 `day_kurt` 从 0.97 掉到 0.02)。还带 alpha ⇒ 核心 A 不吃零质量,比 `day_kurt(Ret)` 干净;掉光 ⇒ 两个核心其实是同一个摩擦的两种写法,判读要改。
2. `ts_skew(day_var(Ret), 50)` —— (算术)DW(Open) 与 day_var(Ret) 差 0.4%,所以这一条**预测与头几乎同分**;若明显不同,说明 `Open` 的零质量 / 首根 bar 另有内容。一次便宜的交叉验证,也是对 §1.1.1 全部论证的检验。
3. `ts_skew(day_std(Ret), 50)` —— 不平方。偏度对单调非线性变换不守恒,平方会放大右尾。若这一条明显差,说明核心 A 要的正是**方差分布的右尾**(= 爆波动日),和 `day_kurt(Ret)` 的「尖峰日」是同一个经济故事(对最终融合的去重是个警告)。
4. `div(cross_tail_mean_q75(day_durbin_watson(Open), 50), cross_mean(day_durbin_watson(Open), 50))` —— 「最差那几天比平常差多少」,尺度无关、不吃三阶矩的噪声。这是 `ts_skew` 这个部件**最有希望的真替换件**。

**第二优先 —— 换掉 §2.3 那个结构上就弱的 head(3 次,头 = `cross_corr(day_kurt(Ret), day_gini(Ret), 241)`,它只有 0.726,+0.1 的线最好过)**
5. `cross_corr(day_kurt(Ret), day_zero_ratio(Ret), 241)` —— 既是替换件又是诊断:这个 head 是不是在读「尖峰到底是不是躺平造出来的」。
6. `cross_corr(day_kurt(Ret), day_sum(Amt), 241)` —— 用成交额替掉那个本身就 `rho_known` −0.63 的 `day_gini(Ret)`。
7. `cross_corr(day_kurt(Ret), day_gini(Amt), 241)` —— 同上,换成成交额的集中度。

**第三优先 —— 核心 B 的收盘集合竞价风险(2 次,头 = `sub(day_centroid(Amt), day_centroid(Ret))`)**
8. `sub(day_centroid(in_slice(Amt, 0, 230)), day_centroid(in_slice(Ret, 0, 230)))` —— 砍掉当日最后 10 分钟(含收盘集合竞价)。掉光 ⇒ 这个 head 是「尾盘量占比」;不掉 ⇒ 它真的是全天的时点错位,可以放心给 E 位。
9. `sub(day_centroid(Amt), day_centroid(mul(Ret, Ret)))` —— 用平方代替 |Ret| 定义「波动时点」,检验它是否被一根大打印主宰。

**第四优先 —— 名义价格这条反复冒头的轴(1 次,头随意挂一个,我建议挂 `day_kurt(Ret)`)**
10. `sub(LogFloatCap, LogFloatShares)` —— **精确的 log 名义价格**,只用两个允许的日频叶子。它的 `rho_head`、`rho_known` 和自身 score 一次性把 §1.4 的代理判定、r1 第 12 行(用 `Amt/Volume` 近似)和核心卡第 3 条全部钉住。

**第五优先 —— 其余(按此序凑满)**
11. `ts_kurt(day_durbin_watson(Open), 50)` —— 是「偏」还是「尾」(替换 `ts_skew` 部件)。
12. `div(cross_semistd_pos(day_durbin_watson(Open), 50), cross_semistd_neg(day_durbin_watson(Open), 50))` —— 上下行半偏差之比,另一种尺度无关的不对称。
13. `cross_autocorr_s1(ts_skew(day_durbin_watson(Open), 50), 6)` —— §2.1:knockout + 最好窗口,把 12.8% 的假值块清掉。(估计 +0.05,**大概不够 +0.1**;只在还有余额时放。)
14. `ts_skew(day_durbin_watson(Ret), 50)` —— DW 在 `Ret` 上是**真的**自相关(≈2(1−ρ₁))。预测明显差;它的作用是把 §3.2 那条反讽变成一个数。
15. `ts_skew(day_durbin_watson(Close), 50)` —— §2.2,规则认可的 +0.207,纯落袋,我判为噪声,排在这里。
16. `cross_madz(day_durbin_watson(Open), 50)` —— 「今天的日内方差比自己平常高多少」,与偏度正交的另一种形状读法。

**不建议放进 R 的**:`cross_autocorr_s1(ts_skew(day_durbin_watson(Open), 50), 3)`(**已测 1.5565,再付就是白花**);任何「在核心外面加分组 / 加状态」的写法(那是 E 的地盘,§2.5 的 R 只认「去掉或替换部件」)。

### 4.3 N 的灵感

**N-A(首选)「控制里只有水平,形状全是空的」。** 本轮唯一真正被数据证实的教训是:M2 的 1.56 和 1.23 不是靠一个新原子,而是靠把一个**旧日频量**换成**它自己 50 日分布的形状**(§1.1)。而五个控制全部是**水平**:`cross_mean(day_sum(Amt), 30)`、`cross_mean(day_std(Ret), 20)`、20 日反转、`cross_mean(day_std(Amt), 30)`、`LogFloatCap`。
→ 系统地把「水平」换成「形状」:`ts_skew(day_sum(Amt), 50)`(成交额爆量的不对称)、`ts_skew(div(day_last(Close), ts_delay(day_last(Close), 1)), 50)`(日收益偏度 = 经典的 idiosyncratic skewness / 彩票,文献上有现成对照)、`ts_skew(day_zero_ratio(Ret), 50)`、`ts_skew(day_centroid(Amt), 50)`、`ts_skew(day_kurt(Ret), 50)`,以及尺度无关的比值版 `div(cross_tail_mean_q75(day_std(Ret), 60), cross_mean(day_std(Ret), 60))`、`div(cross_semistd_pos(·, 60), cross_semistd_neg(·, 60))`。
优点:(a) 直接长在本轮唯一被证实的机制上;(b) 仿射不变 ⇒ 构造上躲开所有水平控制;(c) 和库里两个「没有尖峰」的 head 读的是不同的日频量,ρ 不容易撞线;(d) 便宜,16 个种子一个模板就写满。

**N-B(备选)「时点」这条轴的扩张**,若核心 B 没拿到 E 位就放这里:成交时点 vs 波动时点 vs **带方向**的成交时点(`day_signed_ratio(Ret, Amt)` 的时点版)、`day_wstd(Ret, Amt)/day_std(Ret)`(成交钟 vs 钟表钟,r1/lit.md [S18][S19] 有理论支撑且文献空白)、尾盘量占比。注意**不要和 §4.2 第 8、9 条重复花钱**。

**不建议**:再去做日内自相关 / Hurst(r1 的 N 已经测过,没过线;r1/lit.md [S20] 本来就是警告)。

---

## 5. 文献题目(给文献员,4 个;只要 2023-08-08 之前发表的,每条注年份)

r1 已经问过的四题(日内高阶矩与「不交易」、尾部统计量的稳健化、条件分组与 A 股涨跌停、顺序信息与成交钟)**不要重复**;下面四题换的是轴。

**L1 —— 对准核心 A:一只股票**自己的已实现方差序列的形状**(不是水平)在截面上值钱吗?**
文献里怎么用「波动的波动 / 已实现方差的偏度 / 爆波动日的频率与严重度」预测个股截面收益:用的是**滚动偏度**、**上下行半方差之比**、**尾部条件均值 ÷ 中位数**,还是**跳跃计数**?窗口取多长(一个月?一季度?)?有没有先**除掉自己的波动水平**(因为偏度本身对仿射变换不变,这一步可能是多余的)?结论方向是「波动不稳 → 未来收益低」还是相反?以及最关键的一条:**这个量在控制了特质波动水平、流动性、市值之后还剩不剩**,文献怎么证明它不是特质波动或彩票偏好的另一种写法。
EN:`volatility of volatility cross-section of stock returns`;`vol-of-vol anomaly idiosyncratic`;`realized variance skewness predicts returns`;`upside downside semivariance ratio cross-section`;`volatility jumps frequency individual stocks returns`;`realized volatility uncertainty expected returns`;`higher moments of realized variance time series`
ZH:`波动率的波动率 截面收益`;`已实现方差 偏度 预测 个股`;`上行 下行 半方差 比率 选股`;`波动跳跃 频率 个股收益`;`特质波动率 不确定性 异象`

**L2 —— 对准「换掉 `ts_skew` 这个部件」:一条**取正值的时间序列**(方差、成交额)的不对称,文献用什么写法度量,各自修掉什么?**
对正值序列,滚动三阶矩偏度是出名地不稳(被一个观测主宰、对窗口敏感)。文献里的替代写法:**分位数偏度(Bowley / Hinkley)**、**尾部条件均值比(expected-shortfall 型)**、**变异系数**、**上下行半偏差之比**、**超越某倍中位数的天数占比**。每一种相对裸偏度**具体修掉了什么**(单点支配?窗口长度敏感?取对数后还需不需要?),有没有在**截面选股**任务上的直接横向比较?另外:对正值重尾序列,**先取对数再算偏度**和**直接算偏度**在实证上差别有多大。
(注:r1/lit.md 的 L2 已经覆盖了双幂变差 / MedRV / 截断已实现方差这类**日内**稳健估计量,这题问的是**日这条轴上**对一条正值序列取形状的写法,不要重复那一批。)
EN:`quantile based skewness measure robust Bowley`;`coefficient of variation versus skewness heavy tailed positive series`;`expected shortfall ratio tail measure time series`;`robust skewness estimator rolling window finite sample bias`;`log transformation skewness realized variance`;`semideviation ratio asymmetry measure`
ZH:`分位数偏度 稳健 度量`;`变异系数 偏度 正值 重尾`;`滚动偏度 窗口 小样本偏误`;`取对数 已实现方差 偏度`;`半偏差 比率 不对称`

**L3 —— 对准核心 B:日内**成交的时点**与**波动的时点**,以及两者之差,在截面上被怎么处理?**
文献里怎么用「成交量在一天里的重心 / 尾盘(及收盘集合竞价)成交占比 / 开盘段占比」预测个股截面收益:是直接用占比,还是先去掉全市场的 U 型模式再看个股偏离?有没有人做过「**成交时点与波动时点的领先滞后**」(成交先于波动 = 有信息的买盘?波动先于成交 = 跟风?)这种**两个时点之差**的度量?以及一条工程性的:**收盘集合竞价**那一笔会不会主宰这类时点度量,文献用什么办法处理(剔除最后 N 分钟?单独建一个尾盘占比变量?),中国市场 2018 年引入收盘集合竞价之后有没有相关研究。
(注:r1/lit.md 的 L4 已覆盖 Clark / Oomen 的「成交量当时钟」和 Admati–Pfleiderer 的 U 型理论,这题问的是**时点本身当因子**和**两个时点之差**,以及收盘竞价的工程处理。)
EN:`intraday volume timing cross-section of returns`;`closing auction volume share price discovery China`;`late-day trading volume concentration predicts returns`;`volume weighted average time of day factor`;`lead-lag between volume and volatility intraday`;`order imbalance timing intraday informed trading`
ZH:`日内成交时点 截面收益`;`收盘集合竞价 成交占比 价格发现`;`尾盘成交集中 收益预测`;`成交量重心 日内`;`成交与波动 领先滞后 日内`

**L4 —— 对准反复冒头的混淆:**给定市值之后的名义价格水平**(= 相对最小报价单位)。**
文献里「低价股 / 名义股价」在控制了市值之后还是不是一个独立的截面效应(A 股有没有专门研究)?**相对最小报价单位(tick ÷ 价格)**被怎么用:当流动性代理、当交易成本代理,还是当「价格离散度」本身?最关键的一条:**价格离散(价格网格)会不会系统性地污染高频波动 / 高阶矩估计量**(低价股一跳就是 0.2%–0.3%,大于典型分钟波动,很多分钟收益落在 0 上),文献用什么办法分离(按价格分组?用相对 tick 当控制?改用成交量时间抽样?);以及有没有人报告**按名义价格分组后,日内波动类因子的表现差异**。
EN:`nominal share price anomaly controlling for size`;`relative tick size liquidity measure`;`price discreteness bias realized volatility estimation`;`minimum tick size microstructure noise high frequency estimator`;`low priced stocks cross-sectional returns China`;`penny stock effect net of size`;`rounding error volatility estimator bias`
ZH:`名义股价 低价股 效应 控制市值`;`最小报价单位 相对 tick 流动性`;`价格离散 已实现波动率 偏误`;`价格网格 高频 估计偏误`;`A 股 低价股 截面收益`

---

## 6. 建议写进 notebook 的可检验预测(供第 3 轮核对)

1. **R 第 2 条** `ts_skew(day_var(Ret), 50)` 与头的 score 差 **< 0.15**,rho_head **≥ 0.9**(§1.1.1 的算术若成立必然如此)。若差很多,§1.1 整节要重写。
2. **R 第 1 条** `ts_skew(day_durbin_watson(Vwap), 50)` 的 score **≥ 0.8**(我押它掉不到 0.3 以下;即核心 A 不像 `day_kurt(Ret)` 那样依赖零质量)。概率我给 65%。
3. **R 第 3 条** `ts_skew(day_std(Ret), 50)` 明显低于头(押掉 0.3 以上):核心 A 要的是**方差**分布的右尾,不是波动分布的。
4. **R 第 4 条**(尾均值 ÷ 均值)过门槛且 rho_head ≥ 0.6,但**不够 +0.1**(押不够)。
5. **R 第 8 条**(砍掉最后 10 分钟)score 掉 **0.2–0.5**:收盘集合竞价贡献实在但不是全部。若掉到 0 以下,核心 B 就是尾盘量占比,E 位不该给它。
6. **R 第 10 条** `sub(LogFloatCap, LogFloatShares)` 与 `day_kurt(Ret)` 的 |rho_head| 落在 **0.4–0.6**(与 r1 第 12 行用 `Amt/Volume` 近似的 −0.5115 一致),自身 score < 0。
7. **本轮替换数 0 或 1**(最可能是第 15 条的 Close 版,若 PI 把它放进去)。
8. **E(核心 A)产出 heads 的概率约 50%**,若有 1–2 个;**最可能来自条件分组一支**(名义价格 / 板块 / 零收益比例分桶),因为那正是 §1.1.3 两条未排除混淆所在的地方,也是 SEEN 里肯定没有的外围。`c05_no_core` 的拒绝计数 **> 2000**(核心 3 个节点带窗口,比 r1 的 1322 更高),`c05_periphery_seen` **< 20**(SEEN ≤ 12)。
9. **若 N 走 N-A**:产出 heads 概率 **70%**,1–3 个,最可能是 `ts_skew(day_sum(Amt), 50)` 或日收益偏度那一支;它们与核心 A 的交易信号 |ρ| **< 0.5**(读的是不同的日频量)。
10. **第 3 轮的拆解**会落在 `day_kurt(Ret)`(**又是 0 个变体**:根不跳、`Ret` 无同类字段、无窗口)、`sub(day_centroid(Amt), LogFloatShares)` 和 M3 / r2 的新 head 上;所以 48 次预算**还会再作废一部分**,累计作废将超过 90 次。
