# 结构解剖:种子 807,C 组,第 3 轮

材料:`r3/loc.md` / `r3/loc.json`(快照 = `c05s807M1/M2/M3_I0_open_search` + `c06s807Cr1a_Ea`、`c06s807Cr1b_Nb`、`c06s807Cr2a_Na`、`c06s807Cr2b_Nb`;**24 个 head**,526 个已评分存档候选,拆解花 32 次评估,已生效的 R 替换 1 个);`r3/R_prev.json`;`r1/`、`r2/` 的 `analysis.md`、`lit.md`、`missions_final.yaml`、`audit_1.yaml`、`audit_2.yaml`、`audit_record.json`、`corr_*.md`;`notebook.md`。
算子与奖励源码:`/Users/wxy/Desktop/AlphaCube/src/alphacube/operators/{dt_cross.py,dt_day.py,dt_in.py,nd_cs.py,nd_ts.py,common.py}`、`src/alphacube/axes.py`、`/Users/wxy/Desktop/Partura/partura/{ops_ext.py,steer.py,books.py}`、`scripts/c05_locate.py`。

**本轮一句话**:M 第 3 批把库从 8 个 head 扩到 24 个,新增的 14 个(库的 58%)全是同一个骨架 ——
`cross_regbeta(<成交量/价格的离散度>, <cs_* 包装的 day_distinct_ratio(Volume)>, 10–15)`。
这一族的**两条腿单独都不是因子**(x 腿的 `rho_known` 是 0.57 / 0.62,本身就是已知族;y 腿只有几百个取值,`distinct` 0.030–0.053,过不了门槛),alpha 只出现在"比值"里;而且同一骨架的 14 个 head 里 **7 个方向 +1、7 个方向 −1**,最干净的一对只差 y 的一层包装、方向相反。
与此同时,r2 的 R 把一个与波动控制 |ρ| = 0.56 的空对照**替换进了库**(审计员两轮都建议删掉它),而本种子唯一一个"去掉波动尺度之后 train 和 valid 都 ≥ 1.0、与两个控制都 ≤ 0.18"的量(日度波动的 60 日变异系数,+1.04 / +1.11)**因为差 0.33 分而被丢掉,并且从此被库禁令挡在门外**。

---

## 0. 本轮新读出来的实现事实(全部有源码位置,不是推测)

**(0a) `cross_regbeta(x, y, d)` 是「每只股票自己的 d 日时序回归的斜率」,`β = cov_d(x, y) / var_d(x)`。**
`dt_cross.py`:`cross_regbeta(x, y, d) = rolling_ols(x, y, d, axis=0)["beta"]`;`common.py` 的 `rolling_ols` 注释写明模型是 `y ~ alpha + beta*x`,`beta = torch.where(var_x > EPS, cov / var_x, nan)`。
`axes.py` 的面表:`dt/cross` 是「固定分钟、沿日轴滚动」。所有 `day_*` 把分钟轴压成 1 列,所以这里的 `cross_*` 就是**逐股票的日轴滚动**,和截面无关(r2 §0c 已记过;本轮的 `cross_regbeta` 同理)。
两个推论,后面整节都要用:
- `β = corr_d(x,y) · σ_d(y) / σ_d(x)`。y 若有界(robust-z / 掩码后量级 O(1)),**|β| 与 x 的尺度成反比**;
- 分母 `var_d(x)` 只有 `> EPS` 的保护,**x 在窗口里几乎不动的股票 β 会爆**。这是一个极点,不是一个旋钮。

**(0b) `day_distinct_ratio(x)` 是一个离散网格量,单独永远过不了门槛。**
`ops_ext.py`:`k / n`,k = 当日有限分钟里不同取值的个数,n = 有限分钟数(≈241)。docstring 原文:「On a price: how many price levels the day visited -- coarse for low-priced stocks on a one-tick grid」。
用在 `Volume` 上,它量的是「这一天有多少分钟的成交量取值彼此不同」——低值 = 大量零成交 / 重复成交的分钟 = **分钟级交易不连续**。
门槛是 `coverage ≥ 0.9 且 distinct ≥ 0.5`(`c05_locate.py` 第 161–162 行),`distinct` = 抽样日上「不同取值数 / 有值股票数」的中位数。实测:

| 表达式 | distinct | gate |
|---|---|---|
| `day_distinct_ratio(Volume)` | 0.0532 | 废 |
| `cs_robust_z(day_distinct_ratio(Volume))` | 0.0532 | 废 |
| `cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume)))` | 0.0366 | 废 |
| `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume))))` | 0.0303 | 废 |
| `day_distinct_ratio(in_sum_rolling(Volume, 10))` | 0.0316 | 废 |
| `inv(cs_demean(day_distinct_ratio(in_sum_rolling(Volume, 10))))` | 0.0316 | 废 |

注意第 5 行比第 1 行还低:10 分钟滚动和几乎处处不同,`k/n` 在大多数股票上**饱和在 1.0**,截面上的取值更少。所以「把分钟聚粗」让这个变量作为截面变量**更差**,不是更好。
head 19 的 y 腿叶子是 `day_argmax(Volume)`(当日成交量最大那一分钟的序号,整数 0..240),同样是几百个取值的离散量。**14 个 F3 head 的 y 腿,无一例外都是离散量。**

**(0c) `cs_mask_top_replace_mean_neg(x)`:把每日截面最低的 10% 换成当日截面均值。**
`nd_cs.py`:`cs_mask_top_replace_mean_neg(x) = -cs_mask_top_replace_mean(-x)`,`top_ratio = 0.1`,`n_top = ceil(count * 0.1)`,被选中的位置换成**当日有效值的均值**。两个后果:
- (i) 被换掉的那 ~500 只股票,当天的 y 变成**同一个值**,而且这个值是一条市场级时间序列 `m_t`;
- (ii) 它**不是单调变换**:最低的一段被搬到分布中间。

**(0d) `inv(cs_demean(d))` 有极点,而且是 d 的非单调函数。**
`common.py`:`inv(x) = 1.0 / x`,**没有任何截断**;`cs_demean` 逐日去截面均值。所以 `d ≈ 当日截面均值` 的股票 y 爆成任意大,均值两侧符号相反。

**(0e) `cs_robust_z` 放在滚动回归里不是单调变换,是「给窗口里的每一天重新加权」。**
`ops_ext.py`:`(x − median_t) / (1.4826·MAD_t + EPS)`,除的是**逐日**的截面尺度。它在当日截面上是保序的,但 `cov_d(x, y)` 是跨 15 天求和,逐日的缩放因子**提不出来**,结果是 MAD 小的日子在协方差里权重更大。
这与 F1 族的凸度旋钮是同一类东西:**改"日与日怎么混",不加当日截面信息**(r2 §0b 的 `MONOTONE_NONNEG` 注释:「changes nothing a rank-based book sees on the day -- only how the days mix under the EMA」)。这解释了为什么它的必要性在两个 head 上一个是 **−0.09**、一个是 **+0.78**:它不是信息部件。

**(0f) `cs_sum(x)` 逐日截面求和再广播 ⟹ 截面上处处相同。**
head +0.58 `cross_regbeta(day_last(in_sum_rolling(Volume, 5)), cross_regbeta(cs_normalize(day_std(High)), cs_sum(day_distinct_ratio(Volume)), 15), 10)` 的内层 y 就是它。于是内层 β 里唯一的股票特异内容是 `1/var(x_i)` 与「对一条市场序列的敏感度」。这不是规则 §4 陷阱 2 的原话(没有经过 `_pct_rank` 的 `cs_*`),但是同一种性质:**用一个与股票本身无关的量去构造截面排序**。

**(0g) 方向与半衰期按 train 的纯多头 Sharpe 取最大,成本 15 bp / 单位换手。**
`steer.py` 的 `reward`:`for hl ... for sign in (1.0, -1.0): ... key = long_sharpe(train); if key > best`。`books.py`:`COST = 0.0015`,`long_book` = 顶十分位等权、净扣成本、对「有信号且有标签的名字的等权」取超额。两个后果:
- (i) **「x 单独 = −2.01」不等于「反过来就是 +2.01」**。两个方向都可能被换手成本压成负的。`day_std(Ret)` 单独 −2.56 / `day_std(Volume)` 单独 −1.60 / `day_last(in_sum_rolling(Volume, 10))` 单独 −2.01 —— 这些很负的数主要量的是**换手**,不是「信息在反方向」。以后不要从负分推反方向。
- (ii) 同一族里方向不一致,说明**方向没有被数据识别**,是在 train 上挑出来的。

**(0h) `ts_sum(·, 1)` 是恒等算子(r2 §0c)本轮被直接证实。**
head 3 `ts_sum(cross_stddev(day_std(Ret), 60), 1)` 的 sufficiency 行 `cross_stddev(day_std(Ret), 60)`:score / train / valid / distinct **完全相同**(+1.2668 / +1.2668 / +2.249 / 0.9997)。

**(0i) 共性表的"均值差"主要量的是"这个子树出现在存档的精英一侧",不是增量。**
40 行里每一行的 `mean_without` 都在 **−0.76 ~ −0.88**(存档 526 个候选绝大多数是负分)。有信息的是 `mean_with` 这一列:

| mean_with | n | 子树 |
|---|---|---|
| +0.86 / +0.84 | 7 / 16 | `pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1))` / `ts_sum(pow_3(day_durbin_watson(High)), 1)` |
| +0.67 | 4 | `pow_2(pow_2(day_wmean(Ret, Ret)))` |
| +0.62 | 30 | `pow_3(day_durbin_watson(High))` |
| +0.47 | 12 | `pow_2_5(LogFloatShares)` |
| +0.29 | 57 | `day_durbin_watson(High)` |
| **+0.145** | 17 | `cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume)))` ← F3 最高的一行 |
| **−0.17** | 62 | `day_distinct_ratio(Volume)` |
| −0.06 | 31 | `day_last(in_sum_rolling(Volume, 5))` |

**F3 没有任何一个子树的 `mean_with` 超过 +0.15,而 DW / W / LogFloatShares 有 5 个在 +0.47 以上;F3 却贡献了 24 个 head 里的 14 个。** 这是「一个很宽的噪声区域 + 一条正的右尾」的签名,也就是选择效应,不是信号强度。(`day_distinct_ratio(Volume)` n=62 与 `day_durbin_watson(High)` n=57 可比,所以这不是样本量的问题。)

---

## 1. alpha 的来源

### 1.1 24 个 head 的家族分解

| 族 | 个数 | 代表表达式 | 方向 | train vs valid |
|---|---|---|---|---|
| **F1** 日内已实现方差的月内凸尾 | 6 | `ts_sum(pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1)), 1)`、`pow_2(pow_2(day_wmean(Ret, Ret)))`、`ts_mean(pow_2(mul(pow_2(day_wmean(Ret, Ret)), day_var(Ret))), 30)` | 全 −1 | **6/6 valid > train** |
| **F2** 日度波动的 60 日离散度 | 1 | `ts_sum(cross_stddev(day_std(Ret), 60), 1)`(**r2 的 R 替换进来的**) | −1 | valid > train |
| **F3** `cross_regbeta` 比值族 | **14** | `cross_regbeta(day_std(Volume), cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume))), 15)` | **7 个 +1,7 个 −1** | **10/14 train > valid**,valid/train 中位数 ≈ **0.74** |
| **F4** 名义价格 + 底部十分位搬中 | 2 | `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(day_quantile(Open)))` | 全 +1 | 1 个 valid≫train,1 个反 |
| **F5** 股本水平 | 1 | `ts_sum(LogFloatShares, 30)` | +1 | valid > train |

F3 内部再分三支:
- **inv 支(5 个,方向全 +1)**:y = `inv(cs_demean(day_distinct_ratio(...)))`,x = `day_last(in_sum_rolling(Volume, k))` 或 `day_last(Volume)`,窗口 10;
- **mask 支(7 个,6 个 −1、1 个 +1)**:y = `cs_mask_top_replace_mean_neg^{1..2}(cs_robust_z(day_distinct_ratio(Volume)))` 或去掉 `cs_robust_z` 的版本,x = `day_std(Volume)` / `cs_normalize(day_std(Volume))` / `cs_normalize(day_std(High))` / `cs_normalize(day_last(in_sum_rolling(Volume,5)))` / `day_last(Volume)`,窗口 15;
- **嵌套支(2 个)**:y 本身是另一个 `cross_regbeta`,一个内层用 `cs_demean`(+1),一个用 `cs_sum`(−1,见 §0f)。

### 1.2 F3 是「比值造出来的」:四条证据

**(1) 两条腿单独都不是因子,而且 x 腿本身就是控制族。**

| 子树(单独当因子) | score | train | valid | `rho_known` | 判 |
|---|---|---|---|---|---|
| `day_std(Volume)` | −1.60 | +0.17 | −1.60 | **0.5746** | 与已知族 ≥ 0.5,本身不合格 |
| `day_last(in_sum_rolling(Volume, 10))` | −2.01 | +0.07 | −2.01 | **0.6191** | 同上 |
| `cs_normalize(day_std(Volume))` | −1.58 | +0.15 | −1.58 | 0.5746 | 同上 |
| 所有 y 腿 | — | — | — | — | 门槛废品(§0b) |

(train 的 +0.07 ~ +0.17 与 valid 的 −1.6 ~ −2.0 之间的巨大落差,按 §0g 主要是换手成本,不要读成「反方向有信息」。)

**(2) 必要性集中在「让 y 退化 / 非单调」的部件上,单调部件的必要性不稳定。**

| head | 去掉的部件 | 变体 score | 必要性 | 读法 |
|---|---|---|---|---|
| +1.215 | `inv(·)` | +0.089 | **+1.13** | 极点是信号 |
| +1.215 | `cs_demean(·)`(留着 `inv`) | +0.101 | **+1.11** | 极点是信号 —— **两者缺一不可**,只有「1/(与当日截面均值之差)」这个组合才有分 |
| +1.199 | `cs_mask_top_replace_mean_neg(·)` | −0.256 | **+1.46** | 掩码是信号 |
| +1.199 | `cs_robust_z(·)` | +1.291 | **−0.09** | 日加权旋钮,不是信息 |
| +1.094 | `cs_robust_z(·)` | +0.313 | **+0.78** | 同一个部件,必要性相差 0.87 ⟹ 它量的是「哪些天进协方差」 |
| +1.094 | 外层 `cs_mask_top_replace_mean_neg(·)` | +1.047 | **+0.05** | 第二层掩码冗余 |
| +1.094 | `cs_normalize(·)`(x 回到裸尺度) | +0.767 | **+0.33** | 去掉 x 的绝对尺度**更好** |

**(3) 方向没有被识别。** 这是本轮最便宜、最硬的一条证据,不用任何新评估:

- 14 个同骨架 head 里 **7 个 +1、7 个 −1**;
- 最干净的一对(x 与窗口一字不差,只差 y 的一层包装):
  `cross_regbeta(cs_normalize(day_std(High)), cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume))), 15)` → **方向 −1**,+0.75(train 0.75 / valid 1.01)
  `cross_regbeta(cs_normalize(day_std(High)), cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(day_distinct_ratio(Volume))), 15)` → **方向 +1**,+0.71(train 0.71 / valid 2.10)
  两者都是「把同一个离散量的最低十分位搬到均值」,方向相反,分数相当;
- 拆解里 head +1.215 做 `Volume→Amt` 的字段替换后,**方向从 +1 翻到 −1**,score 仍然 +0.64(train 0.64 / valid 2.24);同一个 head 的窗口 10→5 也翻过一次方向。

一个真实的经济机制不会因为多套一层「底部十分位搬中」或者把股数换成成交额就反向。

**(4) 尺度分析给出一个与(1)–(3)一致的机制。**
`β = corr · σ_y/σ_x`(§0a)。σ_y 有界,σ_x ∝ 成交量尺度 ⟹ **|β| ∝ 1/流动性尺度**,而 `corr` 的符号两侧都有 ⟹ **β 的截面排序是流动性的非单调函数**:两条尾巴都是不流动的股票,中间是流动的。线性中性化按定义只能去掉线性部分,所以 `rho_known` 可以只有 0.2–0.3,而因子的内容仍然是流动性 —— 这就是规则 §4 **陷阱 3** 的新外衣(「流动性的非线性函数,线性中性化只去掉线性部分」)。
`cs_normalize` 版把 x 的**绝对**尺度去掉了(必要性 +0.33,去掉反而更好),但 `1/var_d(x)` 这个极点还在:z 单位下 `var` 小 = **这只股票在截面排名里 15 天几乎没动**。

**掩码那一支还有一个可检验的机制读法**:`cs_mask_top_replace_mean_neg` 把最低 10% 的 y 换成当日截面均值 `m_t`(§0c)。于是对**长期处在最低十分位的股票**,y 恒等于市场序列 `m_t`,它的 `β_i = cov(x_i, m)/var(x_i)` = 「市场级交易粒度对自己成交离散度的敏感度 / 自己的方差」;而留在上面 90% 的股票的 β 是自己的 idiosyncratic 量。**同一个因子在不同股票上量的是两件不同的事,分界线是第 10 百分位。** 这同时解释了方向不唯一、以及 train(2018–2021)→ valid(2022–2023.8)的系统性衰减。

**F3 的 train/valid 衰减值得单列**:F1 + F2 共 7 个 head **全部** valid > train;F3 的 14 个里 **10 个** train > valid,最极端的是 `cross_regbeta(day_last(in_sum_rolling(Volume, 3)), inv(cs_demean(day_distinct_ratio(in_sum_rolling(Volume, 3)))), 10)`(train 1.61 → valid 0.54)和 `cross_regbeta(day_std(Volume), cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume))), 15)`(train 2.03 → valid 1.20)。方向与 hl 是在 train 上挑的,所以 train 本来就有选择偏差;**valid 是诚实的那一半,而库的 58% 在诚实的那一半上已经在往下走**。最终比的是 2023-08-08 之后,这不是好兆头。

### 1.3 F3 里真正可能是「真来源」的东西:`day_distinct_ratio(Volume)` 这个**输入**

必须把「输入」和「用法」分开 —— 这是本轮与前两轮最不同的一点:

- **输入可能是真的**:`day_distinct_ratio(Volume)` 是本种子第一个既不是「分钟收益的二阶量」也不是「价格水平 / 股本」的输入。它量的是分钟级的交易是否连续(零成交 / 重复成交的分钟占比),与波动、与市值都没有机械恒等式。共性表 n=62、p 0.000;它的两个 `cs_*` 包装 n=17 / 18、p 0.001 / 0.0008。
  更值得注意的是:`ops_ext.py` 里还有一整族**同类而且更干净**的原子,库里 24 个 head 一个都没用过 ——
  `day_zero_ratio`(「当日有限分钟里 x 恰好为 0 的比例」,在 Volume 上就是零成交分钟占比)、`day_flat_ratio`(与前一分钟相等的比例)、`day_flat_run_max`(最长「不动」连续段 / 分钟数)、`day_at_max_ratio` / `day_at_min_ratio`(钉在当日最高 / 最低价的分钟占比 —— 一字板)、`day_centroid`(成交的时间重心,**连续量**)、`day_gini`(当日成交分布的基尼,**连续量**)、`cross_flat_ratio`、`cross_valid_count`。
  M 第 3 批摸到了这一族,但只摸到最粗的一个,并且用在最糟的位置上(退化回归的被解释变量)。
- **现在的用法是代理 / 构造假象**:见 §1.2。

所以「真来源 vs 代理」在这一族里**不在子树层面,而在"同一个子树被怎么用"上**。判它只需要 §4.2 的 R1–R6。

### 1.4 F2:r2 的 R 替换让库变坏了,而本种子唯一一条去尺度后还活着的线索被挡在门外

把 `r2/R_prev.json` 与 `r2/corr_2.md` 摊开:

| r2 的 R 变体 | score | train | valid | 与波动控制 \|ρ\| | 与原 head \|ρ\| | 结果 |
|---|---|---|---|---|---|---|
| `ts_sum(cross_stddev(day_std(Ret), 60), 1)`(**明写波动的空对照**) | **+1.267** | 1.267 | 2.249 | **0.56** | 0.869 | **替换了 head 4** |
| `ts_sum(div(cross_stddev(day_std(Ret), 60), cross_mean(day_std(Ret), 60)), 1)`(**变异系数,去尺度**) | **+1.040** | 1.040 | 1.113 | **0.18** | 0.762 | 差 0.33 分,丢掉 |
| `ts_sum(div(cross_stddev(day_durbin_watson(High), 60), cross_mean(day_durbin_watson(High), 60)), 1)` | −0.300 | 1.145 | −0.300 | 0.09 | 0.828 | 丢掉 |

三件事必须写进 notebook:

**(a) 审计员说对了,代价已经发生。** `r2/audit_1.yaml` 与 `audit_2.yaml` 两次都写:「变体 3(未去尺度的版本)…… 若 ≥ head + 0.1 会替换 head 4,把一个明写的波动非线性函数放进库(陷阱 3),诊断用不着走替换通道,建议删掉」。PI 两次都按「通过的部分原样保留」没有动。它真的胜出了。
现在库里 head 3 与波动控制的 |ρ| = **0.56**:**它作为 E 位的核心会被规则 §3 直接挡掉(核心与每个控制 |ρ| < 0.5),却可以作为 head 留在库里参加样本外评比。** 规则漏洞(R 的替换 / 收录只查已知族 |ρ| < 0.5,不查 5 个控制)已经被实际触发一次 —— 这是三轮里审计员唯一一次被忽略且事后证明有实际损失的意见。

**(b) r2 的信念「head 4 就是 RV 水平、没有 vol-of-vol」只对了一半。** DW 口径的变异系数塌了(−0.30),`day_std(Ret)` 口径的**没塌**(+1.04,train 1.04 / valid 1.11,与波动控制 0.18、与已知族 0.085)。这是本种子**唯一**一个「去掉波动尺度之后 train 和 valid 都 ≥ 1.0、与两个控制都 ≤ 0.18」的量。

**(c) 但它现在进不了库。** R 收录要 ≥ 挂靠 head + 0.1(head 3 = 1.267 ⟹ 需要 ≥ 1.367);作为 N 的种子,它与 head 3 同分子、同窗口,日度秩 |ρ| 大概率 ≥ 0.7(对**旧** head 4 已经是 0.762),相关度表会按规则直接划掉。**要救它,只能换一个与 head 3 秩相关 < 0.7 的 vol-of-vol 写法** —— 见 §4.2 的 R9/R10 与 §4.3 的 N-α。

### 1.5 F4(r2b 产出的 2 个 head):名义价格 + 把最便宜的 10% 搬到中间

`day_quantile(x)` 默认 `q = 0.5`(`dt_day.py`),所以 `day_quantile(Open)` = **当日分钟开盘价的中位数 = 价格水平**。阶梯:

| 表达式 | score | train | valid |
|---|---|---|---|
| `cs_mask_top_replace_mean_neg(day_quantile(Open))` | +0.442 | 0.442 | 1.083 |
| `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(day_quantile(Open)))` | **+0.934** | 0.934 | 2.297 |
| `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(day_quantile(Open))))` | +0.698 | 1.006 | 0.698 |
| `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(day_min(Open)))` | +0.799 | 0.799 | 2.185 |
| `cs_mask_top_replace_mean_neg(cs_scale(day_quantile(Open)))` | +0.432 | 0.432 | 1.025 |

读法:掩码把**最便宜的 10%** 设成当日均价(§0c)。中性化的控制里有 `LogFloatCap`,这些股票的拟合值低,残差 = 均价 − 低拟合 = **高** ⟹ 方向 +1 的多头十分位里会出现「最便宜 + 最小市值」的那一块。也就是一个**市值 / 名义价格的非单调重写(陷阱 3)**,与 head 24 `ts_sum(LogFloatShares, 30)`(= −log 价格,r2 §1.6)、r1 的 `day_median(Vwap)` 是同一条线,只是这次用非单调算子藏得更深。valid +2.30 ≫ train +0.93 与 2022–23 的低价 / 小市值行情一致。
另外,共性表这两行 n = 4、p 0.038 / 0.127,而这 4 个候选就是 r2b 那 3 个过线者的近亲 —— **血缘固定块,不是独立证据**。同一张表已经示范过一次这种塌陷:`ts_cov(day_median(Vwap), day_var(Ret), 20)` 在 r1(66 个候选)是 +0.62 / p 0.021,r2(301 个)+0.08 / p 0.570,r3(526 个)**+0.19 / p 0.412,`mean_with` −0.57**。

### 1.6 F1 / F5:结论不变,但 r2 的一条信念被证伪

r2 的信念 2(「head 1 的 +1.78 有一部分来自 float32 下溢造成的并列,多头腿成员由控制投影决定」,置信度 0.85)**被证伪**:

| 表达式 | distinct | score | train | valid | 与波动控制 \|ρ\| |
|---|---|---|---|---|---|
| `ts_sum(pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1)), 1)`(head 1) | 0.5523 | +1.7753 | 1.775 | 2.691 | 0.68 |
| `ts_sum(pow_2_5(ts_sum(pow_3(mul(day_durbin_watson(High), 1000.0)), 1)), 1)` | **0.9997** | **+1.7741** | 1.774 | 2.671 | 0.68 |
| `ts_sum(pow_2_5(ts_sum(pow_3(day_std(Ret)), 1)), 1)`(= σ^7.5 空对照) | 0.9976 | +1.4707 | 1.471 | 3.321 | 0.72 |

下溢**确实**发生了(distinct 0.55 → 1.00 一个乘法就解决),但**并列一点都不承重**(score 差 0.0012)。所以 head 1 的分数就是「日内已实现方差的月内凸尾」本身,与波动控制 |ρ| 0.68 —— 干净的**陷阱 1**,不是数值假象。σ^7.5 的空对照 +1.47 / 与波动控制 0.72 再确认一次:同样的凸化套在奖励自己声明的波动度量上,一样能跑出高分。
F1 的真来源判定不变:低波动异象的多头腿。F5 不变:`LogFloatShares` 对 `LogFloatCap` 取残差 ≈ −log 价格。

### 1.7 三栏判定

| 判定 | 内容 |
|---|---|
| **真来源**(样本内还活着,**且**去掉波动尺度后还活着) | 只有一个候选:**日度波动的 60 日变异系数**(去尺度的 vol-of-vol / 风险不确定性),`ts_sum(div(cross_stddev(day_std(Ret), 60), cross_mean(day_std(Ret), 60)), 1)`,+1.04 / +1.11,vol 0.18、known 0.085。**它不在库里。** |
| **可能是真输入,但现在被错用** | `day_distinct_ratio(Volume)`(分钟级交易不连续度)及其整族更干净的兄弟(`day_zero_ratio`、`day_flat_ratio`、`day_flat_run_max`、`day_centroid`、`day_gini`) |
| **代理** | F1 = 波动(\|ρ\| 0.68);F2 现在的写法 = 波动(\|ρ\| 0.56);F4 / F5 = 市值 / 名义价格 |
| **数值 / 构造假象** | F3 的 `inv(cs_demean(·))` 极点(必要性 +1.13 与 +1.11,缺一不可);`1/var_d(x)` 尺度与极点;`cs_sum` 的截面常数 y;`cs_mask_top_replace_mean_neg` 的「底部十分位搬中」(F3 必要性 +1.46,F4 的 +0.49 增量) |

**到现在为止,库里没有一个 head 的分数能在既去掉波动尺度、又去掉流动性尺度之后存活。** 这是 r2 那条信念的正确写法,它仍然成立。

---

## 2. 烂部件

**(A) 必要性 ≤ 0 或接近 0 的(数已经在 `loc.json` 里,不要再花 R 额度去买)**

| head | 部件 | 变体 | 变体 score | 必要性 |
|---|---|---|---|---|
| `cross_regbeta(day_std(Volume), cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume))), 15)` +1.199 | `cs_robust_z` | `cross_regbeta(day_std(Volume), cs_mask_top_replace_mean_neg(day_distinct_ratio(Volume)), 15)` | +1.291 | **−0.09** |
| `cross_regbeta(cs_normalize(day_std(Volume)), cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume)))), 15)` +1.094 | 外层 `cs_mask_top_replace_mean_neg` | 去掉一层 | +1.047 | **+0.05** |

第一条差 0.009 就到替换线(1.291 vs 1.199 + 0.1 = 1.2995),**丢进 R 也不会触发替换**;两条都是已知数,买不到新信息。

**(B) 换掉反而更好的(≥ head + 0.1,会触发替换)—— 注意 `loc` 的 `r_candidates` 漏了一个**

| 增益 | 变体 | score | `loc` 列了吗 |
|---|---|---|---|
| **+0.277** | `cross_regbeta(cs_normalize(day_std(Amt)), cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Amt)))), 15)`(swap `Volume→Amt`) | **+1.371** | **没有** |
| +0.184 | `cross_regbeta(cs_normalize(day_std(Volume)), cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume)))), 30)`(window 15→30) | +1.278 | 有(唯一一条) |

两个都挂在 head +1.094 下,与它的秩相关必然很高 ⟹ 都会**替换**。`loc` 只机械列了 window 那一条,PI 如果只看 `loc.md` 的最后一节会漏掉更高的那个。**是否要花额度,见 §4.2 的 R11 与那里的保留意见。**

**(C) 真正该打的靶子(必要性 > 0,但那部分必要性里没有新信息)**

| 族 | 部件 | 必要性 | 为什么是烂的 | 依据 |
|---|---|---|---|---|
| F3 | `inv` + `cs_demean` 的组合 | +1.13 / +1.11 | 它是一个**没有截断的极点**,而且两者缺一不可 —— 说明分数来自「1/(与当日截面均值之差)」这个爆炸项,不是来自粒度信息 | §0d + 拆解 |
| F3 | `cross_regbeta` 的分母 `var_d(x)` | 整族 | `β = corr·σ_y/σ_x`,把一个有界的共动量变成「÷ 流动性尺度」「÷ 截面位置的稳定度」,是陷阱 3 的形状;`cs_normalize` 的必要性 +0.33(去掉绝对尺度反而更好)已经指向这里 | §0a、§1.2(4) |
| F3 | `cs_mask_top_replace_mean_neg`(1–2 层) | +1.46 / +0.05 | 非单调,而且把最低十分位的 y 变成一条**市场序列**,使因子在不同股票上量不同的东西 | §0c、§1.2(4) |
| F3 | `cs_robust_z` | −0.09 / +0.78 | 同一个部件必要性相差 0.87 ⟹ 它是日加权旋钮,不是信息(与 F1 的凸度旋钮同类) | §0e |
| F4 | `cs_mask_top_replace_mean_neg`(2 层) | +0.49(0.44→0.93) | 保序的极值处理不会有这个增量;它靠的是把最便宜的十分位搬到中间,再由市值控制把它们推回多头腿 | §1.5 |
| F2 | 「未去尺度」 | — | 已判:去尺度版 +1.04 存在,与波动控制从 0.56 降到 0.18 | §1.4 |

**明确不是烂部件、不要动的**:F1 里 W 的内层 `pow_2`(把带符号的 W 折成 W²,r1 必要性 +1.08;`day_wmean(Ret, Ret)` 单独 −0.19);F2 的 `cross_stddev` 这个算子本身(必要性 **+3.82**,拆掉就从 +1.27 掉到 −2.56)。

---

## 3. 之前的任务

### 3.1 r2 a 位(N,隔夜 vs 日内的收益归属):100 次评分,**0 过线,0 head**

最好的 5 个 score −0.02 ~ −0.28,全部带种子血缘(都含 `log(div(day_first(Open), ts_delay(day_last(Close), 1)))` 结构)。
- 主预测「产出 ≥ 1 个 head,0.30」:**没发生**;
- 次要预测「最好的 5 个里至少 3 个带种子血缘,0.5」:**对**(5/5;r1 的 N 位是 0/5)。
尸检:526 个候选的共性表里,ON / ID 的任何子树**一个都没进前 40**。连 `cross_mean(log(div(...)))` 这类子树都没有出现在正端 ⟹ 和 r1 的资金流一样,**这条通道在这个奖励下没有分,不是"没调好"**。PI 自己记下的制度原因仍然是最可能的:标签从次日 09:31–09:45 VWAP 起算,**次日的隔夜段不在标签里**,LPS 的「隔夜持续性」那一半吃不到。

### 3.2 r2 b 位(N,净派现 / 复合发行,第 2 稿):53 次评分,3 过线,**2 个入 head —— 但两个 head 与这个 idea 毫无关系**

两个 head 都是 `cs_mask_top_replace_mean_neg^k(day_quantile(Open))`,来自 GP 自己那一半随机树(§1.5)。
- 「产出 ≥ 1 个 head,0.25」:字面上**对**,实质上**错**;
- 「若有,是 241 日累积版、方向 −1」:**错**;
- 新增的门槛预测「8 个种子至少 6 个过门槛,0.75」:**对**(审计员记录 8/8 过,distinct 0.715–0.917,coverage 0.998)。
另外值得记:这一位 96 次付费评估只换到 **53 次评分**(r2 a 位 100、r1 两位 84 / 85)—— 种子那 20–30% 的并列块和库禁令吃掉了一部分预算。

**两轮 4 个 N 位的总账:按 idea 产出 head 的次数是 0。** 唯一的 2 个 head 来自「另一半随机树」。N 位的一半初代是 GP 的随机树,这件事在事前预测里必须算进去。

### 3.3 R:6 个变体,**1 个替换,0 个收录**

逐条对 notebook 的预测:

| 预测(r2) | 实际 | 判 |
|---|---|---|
| head 1 组变体 1(×1000)distinct ≥ 0.95(0.85) | 0.9997 | **对** |
| 同上,score 与 +1.78 相差 ≥ 0.3(0.55) | 差 0.0012 | **错** —— 并列不承重,信念 2 证伪(§1.6) |
| 同上,触发替换(0.25) | 没有(与 head 差 −0.001) | 对 |
| head 1 组变体 2(σ^7.5)score ≥ +0.9(0.60) | +1.471 | **对** |
| head 4 组变体 1、2(两个变异系数)都 < +0.5(0.50) | −0.300 / **+1.040** | **半对,而且错的那一半是本轮最重要的信息**(§1.4) |
| head 4 组变体 3(未去尺度空对照)≥ +0.8(0.50) | +1.267,**并替换 head 4** | 对 |
| head 2 组(`mul`→`div`)比 head 2 低 ≥ 0.8(0.65) | 低 0.822 | 对(擦边) |
| 全部 R 合计替换 + 收录 ≤ 2(0.85) | 1 | 对 |
| head 8 组 3 个变体(含 P5 的 log 价格、P9 的 `ts_delta(LogFloatShares, 241)` 门槛) | **未评**(R3 组被 PI 删掉,没有重写) | 悬空 |
| r2/analysis §6 的 P7(核心 A 的第 2 个 E 位) | **未立位**(PI 改成 N+N) | 悬空 |
| r2/analysis §6 的 P3(`day_durbin_watson(High)` 与波动控制 \|ρ\| ≥ 0.5,0.70) | 0.68(×1000 版同秩,corr_2) | **对** |
| r2/analysis §6 的 P4 后半(变异系数版 < +0.5) | DW 口径 −0.30 **对**;`day_std(Ret)` 口径 +1.04 **错** | 半对 |

### 3.4 审计员挡掉了什么、为什么、事后看对不对

| 审计意见 | 事后看 |
|---|---|
| **第 1 稿 b 位合理度 2,划掉全部 10 个种子**:`ts_delta(x, d)` 要求恰好 d 行之前有值 ⟹ 120 / 241 日版覆盖率 0.89 / 0.786–0.788;60 日版 distinct 只有 0.334(「无事件股只剩 float32 舍入,落在少数格点上」) | **对,而且是三轮里质量最高的一次干预**。PI 按意见把 `ts_delta(x, 241)` 换成 `ts_sum(ts_delta(x, 1), 241)`,第 2 稿 8/8 过门槛。审计员把一个会退化成随机 GP 的位救回来了 |
| **第 1、2 稿都建议删掉 R1 变体 2、R2 变体 3**(明写波动的空对照):「它若胜出会把陷阱 3 因子换进库,诊断用不着走替换通道」 | **对,代价已经发生**:R2 变体 3 胜出并替换了 head 4,库里现在有一个与波动控制 \|ρ\| 0.56 的 head(§1.4)。PI 两次都以「通过的部分原样保留」为由没动 |
| 划掉 a 位种子 1(与反转控制 \|ρ\| 0.528) | 对(表规则也会划) |
| 方法学更正:`cov(ON−ID, ON+ID) = var(ON) − var(ID)`,**取差不等于把总收益剥掉**;真正正交的是 `cross_corr` / `cross_regbeta` 版 | 对;PI 两稿都没改这句话。事后 a 位 0 产出,无法进一步分辨 |
| 第 2 稿自己收回一条:`cs_regres` 版并没有剥掉总收益,种子 10 与单腿 ON(种子 5)逐列几乎相同 ⟹ 它只是种子 1 的复本 | 收回是对的(数对得上);a 位 0 产出,无法检验 |
| 第 2 稿提示的风险:送转 / 配股的时点错位会在 x 上造成 −log(1+送转比例) 的负尖刺,方向 −1 时直接进多头书 | **未检验**(b 位的 head 与 idea 无关)。如果以后再碰公司行为,这条要先查 |

### 3.5 r2 五条信念的重新打分

| 信念 | r2 的置信度 | 现在 |
|---|---|---|
| 1. 所有正分都来自「日内已实现方差的月内凸尾」 | 0.9 | **0.55**。F1 / F2 仍是,但 F3 的 14 个 head 不是波动凸尾(是比值 / 极点),F4 是名义价格。正确的写法是 §1.7 最后那句:**没有一个 head 能在同时去掉波动尺度和流动性尺度后存活** |
| 2. head 1 的 +1.78 有一部分来自 float32 并列 | 0.85 | **证伪**(×1000 测试,§1.6) |
| 3. head 4 里可能还有去尺度后仍在的 vol-of-vol | 0.5 | **证实但只在一个口径上**:`day_std(Ret)` 的变异系数 +1.04;DW 口径 −0.30。升到 0.8,并降级为"必须换写法才能进库"(§1.4c) |
| 4. head 8 的信息在股本**变化**里不在水平里 | 0.65 | **未检验**(R3 组删了、b 位产出与 idea 无关),维持 0.65 |
| 5. 资金流失衡通道在这个奖励下是负的 | 0.8 | **维持 0.85**:526 个候选的共性表里这条线仍在负端(`div(pow_2(day_wmean(Ret, Ret)), pow_2(day_wmean(abs_(Ret), Ret)))` `mean_with` −0.58,`day_wmean(abs_(Ret), Ret)` −0.58) |

---

## 4. 本轮候选

### 4.1 值得深挖的核心(≤ 3)

**先说明确反对的四类,附已测数字:**

1. **整个 F1(W 与 DW)族 —— W 核心最后 1 个 E 额度建议作废。** 它的信息已经被量清(是波动尺度:r1 的四种去尺度写法 +0.18 / +0.17 / −0.71 / −0.75;本轮 σ^7.5 空对照 +1.47 再确认),第 2 个 E 位只会产出同机制的下一个日轴聚合写法(r1 已经示范过 4 个)。DW 子族的核心与波动控制 |ρ| = **0.68**(已测),规则 §3「核心与每个控制 |ρ| < 0.5」直接挡掉。
2. **F2 的 `cross_stddev(day_std(Ret), 60)`**:与波动控制 **0.56**,E 位被规则挡掉。
3. **F4 的 `cs_mask_top_replace_mean_neg(day_quantile(Open))`**(核心卡 13):价格水平的非单调重写,合理度拿不到 3;n = 4 还是血缘块。
4. **F3 里任何含 `day_std(Volume)` / `day_last(in_sum_rolling(Volume, k))` / `cs_normalize(day_std(Volume))` 的子树**(核心卡 20、23、25):它们单独的 `rho_known` 是 0.57 / 0.62 / 0.57,**已经 ≥ 0.5**,E 位核心必被挡。

---

**核心 A(推荐,本轮唯一的 E 核心):`day_distinct_ratio(Volume)`**(核心卡 22,共性 +0.66,p 0.000,n = 62)

- **为什么**:库里 24 个 head 的输入只有三类 —— 分钟收益的二阶量、价格水平 / 股本、成交量的水平与离散度。它是第一个「分钟级交易是否连续」的输入(§1.3),与波动、与市值都没有机械恒等式;而 M 把它用在了最糟的位置上。E 位的价值正在于「把同一个新输入从退化的用法里拿出来」。
- **这个核心周围已经见过的外围(全部,14 个 head + 3 张核心卡,共 62 个存档候选)**:只有一种形态 ——
  做 10 / 15 / 30 日滚动 OLS 的**被解释变量**,x ∈ {`day_std(Volume)`、`cs_normalize(day_std(Volume))`、`cs_normalize(day_std(High))`、`day_last(Volume)`、`day_last(in_sum_rolling(Volume, 3/5/10))`、`cs_normalize(day_last(in_sum_rolling(Volume, 5)))`},包装只有 `cs_robust_z`、`cs_mask_top_replace_mean_neg`(1–3 层)、`cs_demean`、`inv(cs_demean(·))`、`cs_sum`、`cs_normalize`,外层偶尔再套一次 `cross_regbeta`。**没有任何一个候选对它做过自身历史的归一化、份额化、或者用相关系数而不是斜率。**
- **本轮要长的外围(与上面没有一处重合)**:
  (i) **自身历史标准化**:`cross_zscore(·, 60)`(ops_ext docstring 原文:「Turns a level into 'unusual for THIS stock', removing the persistent cross-sectional level」)、`div(·, cross_mean(·, 60))`、`cross_delta(·, 20)` ——「这只股票最近的交易连续性相对它自己变差了多少」;
  (ii) **份额 / 无量纲比**:与 `day_distinct_ratio(in_sum_rolling(Volume, k))` 的比(两个量的饱和程度完全不同,比值是一个真实的形状度量,见 §0b);
  (iii) **共动用相关系数不用斜率**:`cross_corr(·, ·, 60)`,把 §0a 的 `1/var` 极点从外围里排除掉;
  (iv) **月内极端日 vs 典型日**:`cross_min` / `cross_tail_mean_q25` / `cross_quantile_q25`(「最不连续的那几天」比「平均」更像一个事件);
  (v) **与同族更干净的原子对照**:`day_zero_ratio(Volume)`、`day_flat_ratio(Volume)`、`day_flat_run_max(Volume)`、`day_centroid(Amt)`、`day_gini(Amt)` 作为伙伴 —— **这五个算子在 526 个候选里一次都没出现过**。
- **两个必须先处理的风险**:
  - **门槛**:核心是离散网格(distinct 0.053),单独过不了门槛,**外围必须连续化**。可靠的连续化只有「跨日聚合」(`cross_mean` / `cross_zscore` / `cross_stddev`,窗口 ≥ 20)和「与连续量相除 / 相关」。**不要**指望 `cs_bucket_rank` 救它:它的输出是「桶内百分位 + 1e-4 × 全局百分位」,离散输入进去出来还是离散,取值数约 10 × 241 ≈ 2400 / 4700 ≈ **0.51**,擦着门槛,不稳。16 个种子里**一个都不要放「核心 + 一层逐日单调包装」的写法**,那是门槛废品,会白烧初代一半名额(r2b 第 1 稿的教训)。
  - **控制列未知**:核心与流动性控制 `cross_mean(day_sum(Amt), 30)` / 已知族 `cross_mean(day_std(Amt), 30)` 的原始日度秩 |ρ| **没有人量过**(它是门槛废品,`loc` 不给它打分,也就没有 `rho_known`)。它是一个交易活跃度量,**有可能 ≥ 0.5 直接把这个位废掉**。**请 PI 先让流水线把这一列算出来再决定写不写** —— r2 对 DW 核心做过同样的事,事后(0.68)证明是对的。
- **创新度预期**:3–4(同一类输入,机制不同:从「比值里的极点」换成「自身历史的变化 + 无量纲份额」;E 位的创新度评的是**外围**,而这个核心已有的外围只有一种形态,对比很清楚)。**合理度**:3,拿到 §5 的 L1 文献后 4。

**核心 B(备选,只在核心 A 的控制列 ≥ 0.5 时启用):`cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume)))`**(核心卡 14,共性 +0.93 / p 0.0009 / n = 17,是 F3 里 `mean_with` 最高的子树 +0.145)

- 好处:出现在 17 个候选、6 个 head 里,E 的候选更容易过线;而且它的掩码在当日截面上保序,所以核心的日度秩 ≈ `day_distinct_ratio(Volume)` 的秩,控制列与核心 A 基本同命。
- 坏处:把我判为构造假象的那一层(§0c)**锁进每一个候选**,等于把 §1.2 的问题固定下来。**只在 A 被控制列挡掉时用**,外围要求同 A。

**不提核心 C。** 剩下的核心卡要么是 F1 / F2 / F4(上面已反对),要么是 x 腿(`rho_known` ≥ 0.5)。

**一条要提前讲清的事**:库禁令(与任一 head 日度秩 |ρ| ≥ 0.7 或**算子骨架完全相同**)**不能保护这个 E 位**。骨架禁令只挡精确重现;而 14 个 F3 head 彼此都在 |ρ| < 0.7 内共存,说明这一族内部的秩相关很松,GP 只要多套一层包装就能重新长回 `cross_regbeta` / `inv` / `div` 的极点结构。r1 的教训(「E 位没有家族控制,GP 会往奖励最喜欢的机制上长」)在这里**会重演**。唯一的抓手是 16 个种子全部无极点,并在事前预测里承认这个漂移概率(§6 的 P7)。

### 4.2 R 目标(16 个额度,我提 11 个,按信息价值排序)

**优先级 1 —— 判 F3(库的 58%)。3 个变体,每个都是严格的单部件替换,全部挂在 `cross_regbeta(day_std(Volume), cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume))), 15)`(+1.199)下。**

- **R1** `cross_corr(day_std(Volume), cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume))), 15)`
  换掉的部件:`cross_regbeta` → `cross_corr`,即把 `β = cov/var_x` 换成相关系数。**只去掉 `σ_y/σ_x` 这个尺度 / 极点项,共动信息一字不改。**
  依据:§0a + §1.2(4) + `cs_normalize` 的必要性 +0.33。
  判据:score < +0.5 ⟹ F3 的分数就是「1/流动性尺度」(陷阱 3),整族应当被当成代理;score ≥ +1.1 ⟹ 共动本身有信息,F3 要重新评价。
  (`cross_reg_tvalue` 不必另花一次:满窗口下 `t = r·√((n−2)/(1−r²))`,与 `cross_corr` 是单调同构。)
- **R2** `cross_cov(day_std(Volume), cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume))), 15)`
  镜像对照:把「÷ 尺度」换成「× 尺度」。R1 + R2 把 `β = corr · σ_y / σ_x` 的三个因子分开,两次评估定位分数在哪一项上。
- **R3** `cross_regbeta(cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume))), day_std(Volume), 15)`
  只把两个参数对调:分母从 `var(day_std(Volume))`(无界、∝ 成交量²)变成 `var(有界的 y)`。不引入新算子,判据同 R1。

**优先级 2 —— 判 F3 的 y 腿构造(极点)。2 个变体,挂在 `cross_regbeta(day_last(in_sum_rolling(Volume, 10)), inv(cs_demean(day_distinct_ratio(in_sum_rolling(Volume, 10)))), 10)`(+1.215)下。**

- **R4** `cross_regbeta(day_last(in_sum_rolling(Volume, 10)), cs_winsor(inv(cs_demean(day_distinct_ratio(in_sum_rolling(Volume, 10))))), 10)`
  换掉的部件:在 y 的最外层加 `cs_winsor`(逐日截面截到 1% / 99%,`ops_ext.py`)。**它只砍掉极点的爆炸值,保序、不动任何别的东西。** 拆解已经证明 `inv` 与 `cs_demean` 缺一不可(+1.13 / +1.11),这一条直接问「是不是极点本身」。
- **R5** `cross_regbeta(day_last(in_sum_rolling(Volume, 10)), cs_robust_z(day_distinct_ratio(in_sum_rolling(Volume, 10))), 10)`
  把非单调的 y 换成**单调、同信息、同量级**的 y(与拆解里的 `cs_demean` knockout 不同:那个没有逐日尺度归一,量级不可比)。R4 + R5 两次把「极点」判死或判活。

**优先级 3 —— F3 里一个有机制的字段替换。1 个变体,挂在 +1.199 下。**

- **R6** `cross_regbeta(day_std(Amt), cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume))), 15)`
  **只换 x 的字段,y 不动**(`loc` 的 `swap Volume→Amt` 把两条腿一起换了,不是单部件)。
  机制依据:`Volume` 是股数,`Amt = Volume × 价格`,所以 `1/σ(Volume) ≈ 价格 / σ(Amt)` —— **股数口径的分母里藏着一个名义价格因子**,正是 F4 / F5 那条线。拆解里 `Volume→Amt`(两腿同换)在三个 head 上分别是 1.199→0.989、1.215→0.638、1.094→**1.371**:不一致,正说明价格项在其中承重。
  判据:score 明显下降 ⟹ F3 的一部分分数来自名义价格(与 F4 / F5 重复);上升 ⟹ 库里换上一个不含价格项的版本。

**优先级 4 —— 判 F4。2 个变体,挂在 `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(day_quantile(Open)))`(+0.934)下。**

- **R7** `day_quantile(Open)`(裸价格水平)。1 次评估就知道两层掩码到底加了多少(单层 +0.442 / 双层 +0.934 已知)。
- **R8** `cs_winsor(day_quantile(Open))`。同样处理极端值,但**保序**(截到 1% / 99%,不把最便宜的 10% 搬到均值)。
  判据:R7、R8 都明显低于 +0.934 ⟹ F4 的分数来自「非单调地把最便宜的十分位搬到分布中间,再由 `LogFloatCap` 控制把它们推回多头腿」,即市值 / 价格控制的非线性重写(陷阱 3),这一族不值得再长。

**优先级 5 —— 救 vol-of-vol(本轮唯一可能"赢了也对库有好处"的两条)。挂在 `ts_sum(cross_stddev(day_std(Ret), 60), 1)`(+1.267)下。**

- **R9** `ts_sum(cross_stddev(log(day_std(Ret)), 60), 1)`
  换掉的部件:在 `cross_stddev` 的输入上加 `log`,即把「水平空间的离散度」换成「对数空间的离散度」。
  依据:`d log σ ≈ dσ/σ`,所以它近似就是那个 +1.04 的变异系数,但**它不是 head 3 的单调函数**(`cross_stddev` 在 `log` 前后不同构),日度秩与 head 3 的 |ρ| 有机会 < 0.7(变异系数对**旧** head 4 已经是 0.762)。`log()` 是 `log|x|`(|x| ≤ 1e-9 给 NaN),`day_std(Ret) > 0`,安全。
  赢的条件:score ≥ 1.367 且与 head 3 的 ρ < 0.5 ⟹ **收录**,库里第一次出现一个去尺度的风险不确定性因子;ρ ≥ 0.5 则替换,库里换上一个与波动控制从 0.56 降下来的版本。两种结果都比现状好。
- **R10** `ts_sum(cross_autocorr(day_std(Ret), 60, 1), 1)`(或 `ts_sum(cross_hurst(day_std(Ret), 60), 1)`)
  波动的**持续性**而不是波动的**离散度**:同一个「风险不确定性」机制的第二种写法,与 head 3 的秩相关应当远低于变异系数。`cross_autocorr(x, d, shift)` 是三参数(`dt_cross.py`),写的时候别漏 `shift`。

**优先级 6 —— 可选,纯为库的分数。**

- **R11** `cross_regbeta(cs_normalize(day_std(Amt)), cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Amt)))), 15)` = §2(B) 里 `loc` 漏掉的那个 **+1.371**,挂 head +1.094 ⟹ 几乎必然替换。
  **请在 `missions.yaml` 里明写它是"分数操作"而不是"去烂部件"**(r2/analysis §2 立过这个规矩;审计员评 R 的合理度看的是「去掉或替换的部件是否**真是**烂的」):它只是把一个 F3 head 换成同族分数更高的写法,对库的**样本外**帮助可疑。**如果 R1–R3 判定 F3 是尺度假象,这一条应当撤掉。** 同族的 window 15→30(+1.278)不要再花一个额度。

**不建议花额度的**:§2(A) 的两条(数已知,且第一条差 0.009 到不了替换线)。

### 4.3 N 的灵感

**N-α(推荐):风险的不确定性,去尺度写法(vol-of-vol)。**
- 为什么现在提:它是本种子**唯一**一个已经在 train + valid 两边都 ≥ 1.0、与波动控制 0.18、与已知族 0.085 的量(+1.04 / +1.11),而且它是被 R 的替换规则**挤出**库的(§1.4),不是被数据否掉的。
- 种子方向:60 日变异系数的多种口径(`day_std(Ret)`、`day_wstd(Ret, Amt)`、上行 / 下行半方差分别算);对数空间的离散度;波动的自相关 / Hurst;短窗 / 长窗波动比的离散度;**以及一个不同族的口径 —— 当日内部分段 RV 之间的离散度**(例如 `day_gini` 或 `day_std` 作用在 `in_sum_rolling(pow_2(Ret), 30)` 上,「日内的 vol-of-vol」),它是当日量而不是 60 日时序量,与 head 3 的秩相关最有机会低。
- **必须先解决的硬约束**:与 head 3 `ts_sum(cross_stddev(day_std(Ret), 60), 1)` 的日度秩 |ρ| ≥ 0.7 的种子会被相关度表**直接划掉**,而那个 +1.04 的变异系数本人大概率就在这条线上。**请让流水线先算这一列**,只留 < 0.7 的;日内分段口径与「持续性」口径最有机会。
- 文献:`r2/lit.md` L3-2 已核实 Baltussen 等 2018(JFQA 53(4))—— 但那是**隐含波动率**口径,A 股 + **已实现**波动率口径是明确的检索空白(L3 的空白清单)。所以合理度最多 4(train 证据 + 机制 + 他口径的文献),**不要写成 5**。
- 事前预期:创新度 3(同一类输入即波动,但机制不同:不确定性而非水平 / 极值),合理度 4。

**N-β(备选):尾盘成交份额(收盘集中度)。**
- 为什么:F3 的 x 腿有 6 个 head 用 `day_last(in_sum_rolling(Volume, k))` = **当日最后 k 分钟的成交量**(k = 3 / 5 / 10),但 **14 个 head 里没有一个把它除以当日总量**。水平 = 已知族(`rho_known` 0.62);份额 `div(day_last(in_sum_rolling(Volume, 30)), day_sum(Volume))` 是无量纲的,机制(收盘集合竞价、指数再平衡、被动资金、隔夜约束下的收盘前平仓)与波动水平和流动性水平都不同。这是「GP 找对了输入、用错了归一化」在本批里最干净的一次机会。
- 文献已有一半(都在 `r2/lit.md` 里核实过):Bogousslavsky 2021(JFE 141(1),L4-2)—— 小盘 / 低流动性股票尾盘 30 分钟收益高、隔夜收益大幅为负,**方向需按规模 / 流动性分组**;Heston–Korajczyk–Sadka 2010(JF 65(4),L4-1)—— 量、价差、波动的日内模式**解释不了**收益的日内模式,正面支持「时点 / 份额不是波动的马甲」。
- 制度风险必须写进假设:上交所自 2018-08-20 起才用收盘集合竞价产生收盘价,train 从 2018-01-02 开始,**跨过一个制度断点**(`r2/lit.md` L4-4;这是制度公告不是同行评审文献,只能当背景)。窗口 ≥ 60 日的版本会把断点摊开,但 2018 年上半年的值与之后不同质。
- 为什么排在 N-α 后面:方向按文献要分组才稳(纯多头 + 15 bp 下尤其吃亏);而且它与 F3 的 x 腿共用叶子,相关度表可能出现 ≥ 0.5 的控制列。

**明确不推荐的一条(写出来免得 GP 或 PI 捡回去)**:`day_distinct_ratio` 用在**价格**上的「价格网格」读法。算子自己的 docstring 就说它「coarse for low-priced stocks on a one-tick grid」,所以它基本是 1/价格 的代理,等于 F4 / F5 那条线。要用必须先除掉价格水平(顺便记一个可用的恒等式:`sub(LogFloatCap, LogFloatShares) = log(未复权价)`,价格字段本身是后复权的),复杂度高、收益低。

### 4.4 配置建议

**1 个 E(核心 A,条件:控制列 < 0.5)+ 1 个 N(N-α)+ 11 个 R。**
- 如果核心 A / B 被控制列挡掉:改成 **N-α + N-β 两个 N 位**,E 额度留空(规则没有要求每轮必须有 E),R 不变。
- 规则提醒:「3 轮里至少要有 1 个 N 位通过审计」这一条**已经满足**(r1 b、r2 a、r2 b 都通过了),所以第 3 轮可以纯按「对库的样本外最有用」来选,不必为凑 N 位而写。
- 还有一条值得 PI 自己权衡:最终比的是**库**在样本外的表现,而库现在有 14 个 F3 head、7 个波动 head。C 组这一轮的边际价值不在「再加一个高分 head」,而在 (i) 用 R 把 F3 判清并留下记录,(ii) 把唯一一个去尺度后还活着的机制(vol-of-vol)用一个 ρ < 0.7 的写法送进库。

---

## 5. 文献题目(4 个,交文献员;只用 2023-08-08 之前发表的文献)

**L1 —— 对准核心 A:分钟级「零成交 / 重复成交 / 不动」型不流动度量**
把「一天里有多少分钟根本没有成交、或者成交量取值重复」做成横截面特征,文献里是怎么度量、怎么处理的?具体请找:(a) 度量族 —— 零收益天数比例、零成交天数比例、分钟 / 日内频率上的「不动」比例,各自的原始定义与标准化方式(是否除以换手、是否取 log、是否按市值分组);(b) 它与 **Amihud 非流动性、换手率、成交额水平**的关系 —— 文献有没有做过「控制住成交额水平之后零成交比例还剩多少」这类检验,结论是什么;(c) 符号与持续性 —— 这类度量高的股票未来收益更高还是更低,回看窗口多长、半衰期多长,**纯多头一侧**单独有没有报过;(d) 用**日内 / 分钟**数据(而不是日度)做这类度量的先例,以及「取值重复 / 价格网格填充程度」这种更细的版本有没有人用过;(e) **A 股**上的证据(涨跌停一字板、停牌、T+1 对「零成交分钟」的影响)。
关键词:zero volume days liquidity measure; zero return proportion Lesmond Ogden Trzcinka; Liu 2006 standardized turnover-adjusted number of zero trading volumes; FHT liquidity proxy Fong Holden Trzcinka; Goyenko Holden Trzcinka liquidity proxy horse race; illiquidity and expected returns Amihud; intraday zero-trade minutes /
零成交;零收益率比例;非流动性度量;分钟级流动性代理;换手率调整的零成交天数;停牌与涨跌停对流动性度量的影响;A 股流动性溢价

**L2 —— 对准 N-α:已实现波动率口径、去尺度的 vol-of-vol / 风险不确定性**
「风险的不确定性」除了用期权隐含波动率的波动率(Baltussen 等 2018,已核实)之外,有没有人用**已实现 / 高频波动率**做过同一件事,并且**把波动水平的尺度去掉**?具体请找:(a) 构造 —— 已实现方差的滚动标准差、**变异系数(std/mean)**、对数空间的标准差、HAR 残差的离散度、波动的自相关 / 持续性,哪些有同行评审的横截面证据,分别用了什么窗口;(b) **去尺度**这一步 —— 文献有没有明确讨论「未去尺度的 std 在乘性尺度下约等于波动水平本身」这个共线性,怎么处理;(c) 增量 —— 控制住 IVOL / 已实现方差水平 / MAX 之后还剩多少,是否只在空头腿;(d) **A 股**上有没有做过已实现波动率口径的 vol-of-vol 定价检验;(e) 「波动的持续性 / Hurst」作为独立横截面特征的证据(与离散度是不是同一件事)。
关键词:volatility of volatility realized measures cross-section; uncertainty about risk stock returns; coefficient of variation of realized variance; vol-of-vol high frequency; persistence of idiosyncratic volatility cross-section; HAR model residual dispersion pricing /
波动率的波动;已实现波动率的不确定性;风险不确定性与股票收益;变异系数去尺度;波动率持续性;A 股已实现波动率定价

**L3 —— 对准 F3 的方法学(库的 58%):把「滚动回归斜率」当横截面特征时,尺度与估计误差怎么处理**
文献里把「A 对 B 的 N 日滚动回归斜率 / beta」做成个股横截面特征时,标准做法是什么?具体请找:(a) **尺度** —— 斜率 `cov/var` 的量纲由解释变量决定,文献是先把两边标准化(z 分数 / 秩 / 对数),还是直接用相关系数 / t 值替代斜率?有没有明确记录过「不标准化会让 beta 的截面排序由 1/var(x) 主导」这件事;(b) **估计误差** —— 短窗口 beta 的测量误差与截面排序的关系,收缩(shrinkage)、分组估计、用 t 值或 R² 代替 beta 的做法与各自的理由;(c) **方向的可识别性** —— 有没有讨论过「beta 型特征在不同实现下符号翻转」的诊断与处理;(d) 以**流动性 / 成交量**作为解释变量的 beta 型特征(liquidity beta、流动性风险暴露)的构造规范,以及它与流动性**水平**怎么分开;(e) 用**离散 / 粗网格**变量(只有几十到几百个取值)做回归一边时,文献有没有讨论过并列与量化误差的后果。
关键词:rolling beta as a cross-sectional characteristic; liquidity beta estimation error shrinkage; correlation versus regression slope characteristic; measurement error in estimated betas portfolio sorts; Vasicek shrinkage beta; standardizing regressors rolling window factor construction /
滚动回归斜率作为横截面特征;估计误差与贝塔收缩;用相关系数替代回归斜率;流动性风险暴露的构造;量纲与标准化;离散变量回归的并列问题

**L4 —— 对准 N-β:尾盘 / 收盘集合竞价的成交份额(不是水平)**
「当日最后 X 分钟(或收盘集合竞价)的成交量占全天成交量的比例」作为个股横截面特征,文献里怎么构造、什么符号?具体请找:(a) 构造 —— 用最后 30 分钟 / 最后 10 分钟 / 收盘竞价本身?分母用全天成交量还是过去 N 日平均?有没有做自身历史标准化;(b) 机制与符号 —— 指数再平衡与被动资金、收盘定价需求、做市商 / 套利者在收盘前平仓(隔夜持仓成本),这些机制各自预测什么符号,证据是否按规模 / 流动性分组才稳定;(c) 持续性与成本 —— 这类份额特征的半衰期,月度聚合后还剩多少,换手与交易成本怎么报;(d) **收盘集合竞价制度**本身的研究(引入 / 延长对价格发现与收盘前成交分布的影响),尤其是**中国 2018 年收盘集合竞价改革**前后的实证;(e) 「谁在收盘交易」这条线(散户 vs 机构 vs 被动)有没有同行评审的横截面收益证据。
关键词:closing auction volume share cross-section; who trades at the close; end-of-day volume concentration returns; index rebalancing closing auction; last half hour volume share predictability; call auction market design price discovery /
收盘集合竞价;尾盘成交占比;收盘前成交集中度;指数再平衡与收盘成交;2018 收盘集合竞价改革;日内成交分布与横截面收益

---

## 6. 可核对的预测(供事后打分)

| # | 预测 | 置信度 |
|---|---|---|
| **P1** | R1(`cross_corr` 版)的 score < +0.5 —— F3 的分数主要来自 `1/var_d(x)` 这个尺度 / 极点项,不是共动信息 | **0.60** |
| **P2** | R1 与 R2(`cross_cov` 版)**都** < +0.8 —— 去尺度和乘尺度两种写法都到不了 head 的量级,分数是「除以一个会变小的分母」造出来的 | 0.50 |
| **P3** | R4(`cs_winsor(inv(cs_demean(·)))`)的 score 比 head +1.215 低 ≥ 0.5 —— 极点本身就是信号 | **0.65** |
| **P4** | R7(裸 `day_quantile(Open)`)< +0.5,**且** R8(保序的 `cs_winsor` 版)< +0.6 —— F4 的 +0.93 来自非单调的「底部十分位搬中」 | 0.60 |
| **P5** | R9(`cross_stddev(log(day_std(Ret)), 60)` 版)的 score ≥ +0.9;但它与 head 3 的日度秩 \|ρ\| ≥ 0.7(所以只能走替换、进不了"收录") | 0.55 / 0.60 |
| **P6** | 相关度表里核心 A `day_distinct_ratio(Volume)` 与流动性控制 `cross_mean(day_sum(Amt), 30)` 的原始日度秩 \|ρ\| ≥ 0.5(即 E 位会被规则 §3 挡掉) | 0.45 |
| **P7** | 若 E 位立起来:产出 ≥ 1 个 head 的概率 **0.55**;但最好的 5 个产出里**至少 3 个**会重新含有 `cross_regbeta` / `inv` / `div` 型的比值-极点结构(即 GP 漂回 F3 的机制) | 0.55 |
| **P8** | R11(`loc` 漏掉的 Amt 版,已量到 +1.371)若提交,触发替换的概率 0.95;但它与被替换的 head +1.094 在交易信号上几乎同一条线,库的样本外不会因此变好 | 0.95 |
| **P9** | 本轮 R 合计替换 + 收录 ≤ 2 | 0.75 |
| **P10** | N-α 的种子里至少一半与 head 3 的 \|ρ\| ≥ 0.7 被相关度表划掉,除非用「日内分段 RV 的离散度」这种当日口径 | 0.55 |
| **P11** | 第 4 批(本轮看不到)如果再出一族,它仍然会是「两条腿单独不是因子、比值才是因子」的形状(比值 / 极点 / 掩码),而不是一个新的经济输入 | 0.50 |

---

## 7. 方法学提醒(请 PI 写进 notebook;前两轮的仍然有效)

1. **不要从很负的分数推「反方向有信息」。** 方向与 hl 按 train 的纯多头 Sharpe 取最大,成本 15 bp / 单位换手(§0g)。`day_std(Volume)` 单独 −1.60、`day_last(in_sum_rolling(Volume, 10))` 单独 −2.01,量的主要是换手。
2. **同族表达式方向不一致 = 方向没有被数据识别。** 这是一个免费的、不花评估的诊断,本轮直接把 F3 判了一半(§1.2(3))。以后看到一批 head 骨架相同、符号一半一半,先怀疑构造。
3. **共性表要看 `mean_with` 这一列,不要只看「均值差」。** 每一行的 `mean_without` 都在 −0.76 ~ −0.88,所以「均值差」大部分只是「它出现在存档的精英一侧」(§0i)。n = 4 的行基本都是血缘固定块(`ts_cov(day_median(Vwap), day_var(Ret), 20)` 从 +0.62/p 0.021 塌到 +0.19/p 0.41 已经示范过两次)。
4. **R 的替换 / 收录只查已知族 \|ρ\| < 0.5,不查 5 个控制 —— 这个漏洞已经被实际触发一次**(§1.4a)。凡是「明写控制变量的空对照」,要么不提交,要么在计划里声明为诊断并接受替换的后果;审计员已经提醒过两次。
5. **`distinct` 和 `coverage` 不只是门槛,是诊断。** 本轮靠它判出「F3 的 y 腿全是只有几百个取值的离散量」;而「把分钟聚粗」(`in_sum_rolling`)让离散度更差不是更好(§0b 的饱和)。离散核心的连续化只能靠跨日聚合或与连续量相除,`cs_bucket_rank` 救不了(§4.1)。
6. **逐日的截面缩放(`cs_robust_z`、`cs_normalize`、`cs_mask_*`)放进滚动窗口算子里就不再是单调变换**,而是「给窗口里的每一天重新加权」(§0e)。看到它们出现在 `cross_*` / `ts_*` 的参数里,要按「日加权旋钮」而不是「截面变换」来读。
7. **N 位有一半初代是 GP 的随机树。** 两轮 4 个 N 位,「按 idea 产出 head」的次数是 0;唯一的 2 个 head 来自那一半随机树(§3.2)。事前预测 N 位时应当分开写「idea 产出」和「这一位产出」两个概率。

---

## 8. 一页总结

- **M 第 3 批把库从 8 个 head 扩到 24 个,新增的 14 个全是一个骨架**:`cross_regbeta(<成交量/价格离散度>, <cs_* 包装的 day_distinct_ratio(Volume)>, 10–15)`。
- **这一族的两条腿单独都不是因子**:x 腿的 `rho_known` 是 0.57 / 0.62(本身就是已知族,单独 score −1.6 ~ −2.0),y 腿只有几百个取值(`distinct` 0.030–0.053,门槛废品)。**alpha 只出现在比值里。**
- **必要性集中在「让 y 退化」的部件上**:`inv` 与 `cs_demean` 各 +1.13 / +1.11 且**缺一不可**(没有截断的极点就是信号);掩码 +1.46;而单调的 `cs_robust_z` 一个 head 上 −0.09、另一个上 +0.78(日加权旋钮,不是信息)。
- **方向没有被识别**:14 个同骨架 head 里 7 个 +1、7 个 −1;最干净的一对只差 y 的一层包装、方向相反(`cross_regbeta(cs_normalize(day_std(High)), cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume))), 15)` = −1 / +0.75 与 `cross_regbeta(cs_normalize(day_std(High)), cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(day_distinct_ratio(Volume))), 15)` = +1 / +0.71);字段 `Volume→Amt` 一换,head +1.215 的方向就从 +1 翻到 −1。
- **尺度分析与之一致**:`β = corr·σ_y/σ_x`,σ_y 有界而 σ_x ∝ 成交量尺度 ⟹ β 的截面排序是流动性的**非单调**函数,线性中性化按定义去不掉 —— 陷阱 3 的新外衣;`cs_normalize`(去掉 x 的绝对尺度)的必要性只有 +0.33,去掉反而更好。
- **衰减方向也不一样**:F1 + F2 的 7 个 head **全部** valid > train;F3 的 14 个里 **10 个** train > valid(2.03→1.20、1.61→0.54),valid/train 中位数 ≈ 0.74。库的 58% 在样本内的诚实那一半上已经在往下走。
- **r2 的 R 让库变坏了一次**:审计员两轮都建议删掉的「明写波动的空对照」`ts_sum(cross_stddev(day_std(Ret), 60), 1)` 胜出并替换了 head 4,它与波动控制 \|ρ\| = **0.56**(作为 E 核心会被规则直接挡掉,作为 head 却能留在库里);而同组真正有意思的**变异系数**版 `ts_sum(div(cross_stddev(day_std(Ret), 60), cross_mean(day_std(Ret), 60)), 1)`(+1.04 / +1.11,与波动控制 0.18、与已知族 0.085)差 0.33 分被丢掉,**现在还被库禁令挡在门外**。它是本种子唯一一个「去掉波动尺度后 train 和 valid 都 ≥ 1.0」的量。
- **r2 的信念 2 被证伪**:head 1 的 float32 并列**不承重** —— ×1000 的恒等变换把 `distinct` 从 0.5523 抬到 0.9997,score 1.7741 vs 1.7753。head 1 就是干净的陷阱 1(与波动控制 0.68)。
- **r2b 的两个 head 与它的 idea 无关**:`cs_mask_top_replace_mean_neg^2(day_quantile(Open))` 是「价格水平 + 把最便宜的 10% 搬到均值」,经市值控制的残差把它们推回多头腿 = 市值 / 名义价格的非单调重写;两轮 4 个 N 位「按 idea 产出 head」的次数是 **0**。
- **本轮建议**:**1 个 E**(核心 `day_distinct_ratio(Volume)`,**先要控制列**;外围只长自身历史标准化 / 份额 / 相关系数 / 同族更干净的原子 `day_zero_ratio`、`day_flat_ratio`、`day_flat_run_max`、`day_centroid`、`day_gini` —— 这五个在 526 个候选里一次都没出现过)+ **1 个 N**(去尺度的 vol-of-vol,先要它与 head 3 的 ρ 列)+ **11 个 R**(R1–R3 判 F3 的分母,R4–R5 判极点,R6 判名义价格项,R7–R8 判 F4 的掩码,R9–R10 救 vol-of-vol,R11 可选且须声明是分数操作)。
- **一个额外发现**:`loc` 的 `r_candidates` 只列了 window 15→30(+1.278),**漏了同一个 head 下更高的 `Volume→Amt`(+1.371)**;PI 如果只读 `loc.md` 最后一节会漏掉它。
- **一条要提前认账的风险**:库禁令保护不了 E 位。骨架禁令只挡精确重现,而 14 个 F3 head 彼此 \|ρ\| < 0.7 共存,说明这一族内部的秩相关很松 —— GP 多套一层包装就能长回极点结构(P7:0.55)。
