# 结构解剖:种子 807,C 组,第 2 轮

材料:`r2/loc.md` / `r2/loc.json`(快照 = `c05s807M1_I0_open_search`、`c05s807M2_I0_open_search`、`c06s807Cr1a_Ea`、`c06s807Cr1b_Nb`;8 个 head,301 个已评分存档候选,拆解花 28 次评估);`r2/R_prev.json`;`r1/analysis.md`、`r1/lit.md`、`r1/missions_final.yaml`、`r1/audit_1.yaml`、`r1/audit_record.json`、`r1/corr_1.md`;`notebook.md`;
算子与奖励源码:`/Users/wxy/Desktop/AlphaCube/src/alphacube/operators/dt_day.py`、`dt_cross.py`、`nd_ts.py`、`nd_cs.py`、`common.py`、`src/alphacube/catalog.py`、`src/alphacube/metrics.py`、`src/alphacube/store.py`、`src/alphacube/parser.py`、`/Users/wxy/Desktop/Partura/partura/ops_ext.py`、`partura/steer.py`、`partura/books.py`、`partura/diagnose.py`、`scripts/c05_locate.py`。

**本轮一句话**:第 2 批带来的新东西,机制上只有一个 —— **日内已实现方差的「月内极端日」凸尾**,方向 −1;它是规则 §4 陷阱 1 与陷阱 3 的正面命中,而且最高分那个 head 还踩在 float32 下溢上。本种子到目前为止**没有任何一个 head 的分数能在去掉波动尺度后存活**。

---

## 0. 五条会影响全部判读的实现事实

前两条是对第 1 轮的**更正**,后三条是本轮新读出来的。全部有源码位置,不是推测。

**(0a) 不存在「核心家族控制」—— 更正 r1 §4.1 的一条硬规则。**
规则 §2 写明:E 位「奖励与所有组相同,**不**额外控制核心的家族;不和家族重复,靠的是上面的库禁令」。r1 §4.1/§1.4 里写的「E 的奖励把家族加进控制,所以任何只是核心单调函数的种子都会被打到 0 分」**理由是错的**。
结论本身仍然成立,但换了机制:**库禁令**(§1「与库里任一 head 的日度秩 ≥ 0.7、或算子骨架相同的候选一律拒绝」)会把核心的任何单调重写直接拒掉(日度秩 |ρ| = 1.00)。
这条更正有实际后果:E 位的候选分数**没有被家族残差化**,可以和 head 的分数直接比 —— 这解释了为什么 r1 的 a 位能轻松产出 4 个分数 1.03–1.49 的 head(它们高度依赖核心,只要与已有 head 的秩 ρ < 0.7 就收录)。**E 位本身很容易「产出 head」,但产出的往往是同一机制换一种日轴聚合。** 第 3 条(§3)会看到这正是 r1 发生的事。

**(0b) 源码自己承认:`pow_3` / `pow_2_5` / `pow_2` 作用在非负量上不改当日截面秩,只改「日与日怎么混」。**
`partura/steer.py` 第 175–181 行:

> `MONOTONE_ANY = pow_05 pow_3 signedpower sigmoid`;`MONOTONE_NONNEG = pow_1_5 pow_2 pow_2_5 sqrt abs_`
> 注释原文:「At the ROOT of a candidate such a wrapper changes nothing a rank-based book sees on the day -- only how the days mix under the EMA」。

`day_durbin_watson` 恒 ≥ 0(`dt_day.py` 第 273–299 行,分子分母都是平方和),`pow_(x, e)` 在 `e > 1` 时就是 `x**e`(`common.py` 第 209–218 行)。于是:

> `day_durbin_watson(High)`、`pow_2_5(ts_sum(day_durbin_watson(High), 1))`、`ts_sum(pow_3(day_durbin_watson(High)), 1)`、`ts_sum(pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1)), 1)`
> **这四个表达式每一天的截面秩完全相同**,缺失模式也相同。

奖励的顺序是 `sm0 = bk.smoothed(raw, hl)` → `neutral_residual`(`steer.py` 第 423–440 行;`_zrank` 在 `diagnose.py` 第 190 行是平滑之后才做的),`ema_rows` 作用在**原始数值**上(`metrics.py` 第 215–227 行)。所以这四者 score 的全部差别,**百分之百来自 hl = 20 的 EMA 被不同凸度拉向月内最极端的那一天**,一点当日横截面信息都没有增加。

**(0c) `ts_sum(x, 1)` 是恒等算子;`cross_*` 与 `ts_*` 都是日轴滚动。**
`ts_sum = rolling_reduce(x, d, nansum_last, axis=0)`(`nd_ts.py` 第 142 行),d = 1 时原样返回。`dt_cross.py` 的模块注释:「Every operator here rolls a window of `d` DAYS」。所以:

- head `ts_sum(pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1)), 1)` **精确等于** `day_durbin_watson(High)^7.5`;
- head `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)` 精确等于 `cross_stddev(day_durbin_watson(High), 60)`;
- head `ts_sum(LogFloatShares, 30)` 是 LogFloatShares 的 30 日滚动和(股本不变的股票上 = 30 × 当前值,秩与当前值相同)。
- `cross_fangzheng(x, d) = cross_mean(x, d) + cross_stddev(x, d)`(`dt_cross.py` 第 499–501 行)—— 共性表里的「方正」项是「d 日均值 + d 日标准差」,**它的 std 项是一个「这 d 天里变过没变」的探测器**,这一点在 §1.8 有用。

**(0d) `day_durbin_watson(High)` 就是日内已实现方差(规则 §4 陷阱 1 的原话,源码可证)。**
`dt_day.py` 第 283–290 行:分子 `Σ_t (x_t − x_{t−1})²`,分母 `Σ_t x_t²`,**分母不去均值**。代入 x = 分钟最高价(价格水平 P):

> DW(High) = Σ(ΔP)² / Σ P² ≈ [Σ(ΔP/P̄)²] / T ≈ **分钟收益平方的均值 = 日内已实现方差(每分钟)**。

数量级:分钟相对变动 ~0.1%–0.3% ⟹ DW ≈ 1e-6 ~ 2e-5。`High→Low` 的敏感性检验给 +1.54(vs +1.78)—— 字段换成另一个价格水平,结论几乎不动,正是「它只是价格的二阶变动」的签名。

**(0e) float32 + `distinct` 门槛:`DW^7.5` 在数值上塌掉了一半截面。**
数据立方体是 float32(`store.py` 第 175、177 行 `dtype=np.float32`;`ops_ext.py` 第 650 行注释「The result goes back to the input dtype (float32 in production)」)。float32 的最小非规格数是 1.4e-45。
取 DW ≈ 1.8e-6:`DW^7.5` ≈ **8e-44**,也就是只有 1.4e-45 的 **56 倍**;凡 DW < 9.5e-7(约一半的股票)的 `DW^7.5` **直接下溢成 0**。
这不是推演,`loc.json` 直接量到了:

| 表达式 | distinct | score |
|---|---|---|
| `day_durbin_watson(High)` | 0.9997 | −1.17 |
| `ts_sum(pow_3(day_durbin_watson(High)), 1)` | 0.9996 | +0.96 |
| `pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1))` | **0.5523** | **+1.78** |
| `ts_sum(pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1)), 2)` | **0.6905** | +1.90 |

`distinct_fraction` 的定义(`diagnose.py` 第 136–147 行)是「抽样日上 (不同取值数 / 有值的股票数) 的中位数」,它的 docstring 原文就是:

> 「A factor with a handful of levels makes a decile book whose membership is decided by tie-breaking, i.e. by symbol order.」

一个连续的分钟数据函数,distinct 应该是 1.00(表里其它每一行都是 0.997–1.000)。**只有加上 `pow_2_5` 这一层之后掉到 0.55**,而门槛是 `distinct ≥ 0.5`(`c05_locate.py` 第 162 行)—— **它是擦着门槛过的**。
后果要说清楚:方向是 −1,纯多头书买的是**最小**的那一端,而最小的那一端正是下溢成 0 的那 45%。平滑后这些股票的值仍然相同,`_zrank` 对并列取平均秩(`rank_rows` = pandas `rank(axis=1)`,ties averaged),所以并列块内 z 相同,**中性化之后残差 = 常数 − x′β̂,完全由 5 个控制决定**。也就是说:

> **head +1.78 的多头腿 ≈ 「在日内已实现方差最低的那 45% 名字里,挑控制投影最极端的 10%」。** 它既是陷阱 1(凸化波动),也落进陷阱 2 的形状(并列决定成员),残差里还是陷阱 3(控制自己回来)。

§4.2 的 R1–R2 用 1–2 次评估就能把这条判成或判否(见那里的 `mul(·, 1000.0)` 测试,常数字面量是合法的:`parser.py` 第 112–113 行 `Constant(float(node.value))`)。

---

## 1. alpha 的来源

### 1.1 8 个 head 只有三族,而且前两族是同一个机制

| # | score | train | valid | 来源 | 表达式 | 读法 |
|---|---|---|---|---|---|---|
| 1 | +1.78 | +1.78 | +2.69 | M2 | `ts_sum(pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1)), 1)` | RV^7.5(§0b/0d/0e) |
| 2 | +1.49 | +1.49 | +2.45 | 本组 Ea | `ts_mean(pow_2(mul(pow_2(day_wmean(Ret, Ret)), day_var(Ret))), 30)` | 30 日均 (W⁴·RV²) |
| 3 | +1.18 | +1.18 | +1.35 | M1 | `pow_2(pow_2(day_wmean(Ret, Ret)))` | W⁴ |
| 4 | +1.10 | +1.10 | +2.05 | M2 | `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)` | 60 日 RV 的波动(vol-of-vol) |
| 5 | +0.83 | +0.83 | +1.35 | 本组 Ea | `ts_mean(pow_2(day_wmean(Ret, Ret)), 50)` | 50 日均 W² |
| 6 | +0.59 | +0.59 | +1.83 | 本组 Ea | `cross_mean(cross_min(pow_2(pow_2(day_wmean(Ret, Ret))), 30), 5)` | 30 日 W⁴ 的**最小值** |
| 7 | +0.55 | +0.55 | +0.73 | 本组 Ea | `cross_mean(cs_winsor(pow_2(day_wmean(Ret, Ret))), 10)` | 10 日均的**缩尾**W² |
| 8 | +0.52 | +0.52 | +0.84 | M2 | `ts_sum(LogFloatShares, 30)` | 规模 / 名义价格 |

- **RV 凸尾族**:1、4(DW(High) = 已实现方差)。
- **W 凸尾族**:2、3、5、6、7(W = Σr|r|/Σ|r|,`ops_ext.py` 第 109–119 行;`day_wmean` 用 |w| 加权)。
- **规模/价格族**:8。

第 1 批只有 W 族,第 2 批加进来的是 RV 族和规模族。下面证明 **RV 族和 W 族测的是同一件事**:日内波动的「月内极端日」。

### 1.2 凸度阶梯:当日秩不变,score 单调上升,而且全涨在 train 上

把 `loc.json` 的四行按指数排(四者当日秩完全相同,§0b;四者 hl 都是 20):

| 指数 e | 表达式 | score | train | valid | distinct |
|---|---|---|---|---|---|
| 1 | `day_durbin_watson(High)` | **−1.17** | −1.17 | +0.58 | 0.9997 |
| 2.5 | `ts_sum(pow_2_5(ts_sum(day_durbin_watson(High), 1)), 1)` | **+0.72** | +0.72 | +2.36 | 0.9997 |
| 3 | `ts_sum(pow_3(day_durbin_watson(High)), 1)` | **+0.96** | +0.96 | +2.64 | 0.9996 |
| 7.5 | `ts_sum(pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1)), 1)` | **+1.78** | +1.78 | +2.66 | 0.5523 |

规则 §4 陷阱 1 的原话是「凸度越高 score 越高」。**这是四个点上的单调曲线,不是一个例子。** 并且分解得很干净:

- **valid** 从 e = 2.5 起就饱和在 +2.36 ~ +2.66,凸度再加没有用;
- **train** 一路从 −1.17 爬到 +1.78,**score = min(train, valid) 的瓶颈一直在 train**;
- 所以**凸度买到的东西全部是 train**。而方向与半衰期也只按 train 选(`c05_locate.py` 第 104 行,hl ∈ {0, 5, 20})。

必要性表里对应的三行(head 1.775 减去变体):`pow_2_5` 必要性 **+0.81**,`pow_3` 必要性 **+1.06**,内层 `ts_sum` 必要性 **−0.00**。按 §0b,这「+0.81 / +1.06」一分钱都不是当日截面信息,只是 EMA 的加权方式 —— **head 1 的 2.95 分全部是「月内最波动的那一天权重给多大」这一个旋钮**,外加 e = 7.5 处的数值塌缩(§0e)。

### 1.3 W 族的三组对照:去尺度就死,水平版就死,峰值记忆版就活

这是本轮最有价值的证据,因为它来自 r1 花钱买的 11 个 R 变体(`R_prev.json`)和 a 位 84 次评估的产出,**是直接评估,不是共性统计**。

**(i) 把波动尺度去掉 —— 全部崩掉**(原 head 3 = +1.18):

| 表达式 | score | train | valid | ρ(head) |
|---|---|---|---|---|
| `pow_2(pow_2(div(day_wmean(Ret, Ret), day_wmean(abs_(Ret), Ret))))` = RSJ⁴ | **+0.18** | +0.32 | +0.18 | 0.94 |
| `pow_2(pow_2(div(day_wmean(Ret, Ret), day_std(Ret))))` = (W/σ)⁴ | **+0.17** | +0.17 | +0.42 | 0.95 |
| `pow_2(pow_2(day_signed_ratio(Ret, Ret)))` = (Σr/Σ\|r\|)⁴ 路径效率 | **−0.71** | −0.62 | −0.71 | 0.63 |
| `cs_bucket_rank(pow_2(pow_2(day_wmean(Ret, Ret))), cross_mean(day_std(Ret), 20))` 波动十分位内 | **−0.75** | −0.75 | +0.71 | 0.97 |

**(ii) 把波动尺度乘进去 —— 还能涨**:head 2 的 knockout 行显示,`ts_mean(pow_2(pow_2(day_wmean(Ret, Ret))), 30)` = +1.33,加上 `day_var(Ret)` 变成 `ts_mean(pow_2(mul(pow_2(day_wmean(Ret, Ret)), day_var(Ret))), 30)` = **+1.49**(必要性 +0.17);外层那个凸化 `pow_2` 的必要性 **+0.62**。

**(iii) 把「极端日」换成「水平」—— 崩掉**:

| 表达式 | score | 读法 |
|---|---|---|
| `cross_med(pow_2(day_wmean(Ret, Ret)), 20)` | **−0.18** | 20 日中位数 |
| `cross_quantile_q75(pow_2(day_wmean(Ret, Ret)), 20)` | **−0.11** | 20 日 q75 |
| `cross_mean(cs_winsor(pow_2(day_wmean(Ret, Ret))), 10)` (head 7) | **+0.55** | 缩尾后取水平 |
| `cross_max(pow_2(day_wmean(Ret, Ret)), 20)` | **+0.77** | 20 日最大值 |
| `cross_tail_mean_q75(pow_2(day_wmean(Ret, Ret)), 20)` | **+0.81** | 20 日尾部均值 |
| `pow_1_5(pow_2(day_wmean(Ret, Ret)))` = \|W\|³ | **+1.07** | 隐式凸化 |
| `pow_2(pow_2(day_wmean(Ret, Ret)))` = W⁴ | **+1.18** | 隐式凸化(head) |

`cs_winsor` 的 docstring(`ops_ext.py` 第 260–264 行)自己说得最准:「the EMA of a raw heavy-tailed value is **a peak memory**, the EMA of the clipped value is **a level**」。表里**水平版全部 ≤ +0.55,峰值记忆版 ≥ +1.07**。

**(iv) 自加权权重的敏感性**:`pow_2(pow_2(day_wmean(Ret, Amt)))` = +0.83(train 1.21 / valid 0.83),`pow_2(pow_2(day_mean(Ret)))` = +0.26。换权重掉分,去掉加权掉得更多 —— |r| 加权有作用,但作用的方向也是「放大大波动分钟」。

### 1.4 判定:真来源只有一个,而且规则已经给它命过名

把 §1.2 和 §1.3 合起来:

> **本种子 train+valid 上唯一能产生正分的东西,是「日内已实现方差在约一个月窗口内的凸尾(极端日)」,方向 −1 —— 纯多头腿买的是日内波动极端日最温和的股票。**
> 两条通道(DW(High) 的 RV,W = Σr|r|/Σ|r| 的尺度部分)测的是同一个量;共性表的 `day_var(Ret)`(+0.49,p 0.093)是第三条。
> 规则 §4 陷阱 1 原文:「这是低波动异象的多头腿从奖励的缝里漏回来,**不是新信息**」;陷阱 3 原文:「波动(方差、标准差、已实现方差)的非线性函数,线性中性化只去掉线性部分」。

**「日内单边程度本身有信息」这条假说,在样本内已经被证伪了。** r1 notebook 的信念 3 给它 ~0.55 的权重,§1.3(i) 的四个直接评估(+0.18 / +0.17 / −0.71 / −0.75)把它压到 ~0.1:四种互相独立的去尺度写法(RV 型分母、σ 分母、路径效率、波动十分位内排序)无一过 0.5 线,而且与 head 的**原始日度秩 |ρ| 高达 0.94 / 0.95 / 0.97**。
这最后一点本身是本轮第二重要的方法学发现,单独写在 §5.1。

### 1.5 真来源 vs 代理:head 4 是唯一还没被判死的

`ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)` = **60 日 RV 的时序标准差**,hl = 0(不平滑!),score +1.10 / valid +2.04,必要性 **+2.28**(拆掉 `cross_stddev` 退回原始 DW 就变 −1.18)。High→Low 换字段 +0.92,窗口 1→2 +0.88,都稳。

它和 1/2/3/5 不同:**它不是凸化,它是二阶矩**,而且 hl = 0 说明它本身已经足够平滑。文献里「vol-of-vol / 风险的不确定性」是一个**独立**的横截面特征(见 §7 的 L3)。所以它有可能不是陷阱 —— 但现在**不能下这个结论**,因为:

- RV 的分布近似乘性,`std_60(RV) ≈ c · mean_60(RV)`,所以未去尺度的 std 在秩上和波动水平高度重合;
- `loc.json` 只给 `rho_known`(= 与 `cross_mean(day_std(Amt), 30)` 的相关),这一列对整族都只有 0.07–0.25,**它量不到波动控制**;r1 的相关度表显示,未去尺度的 W² 一经 20 日聚合,与波动控制的原始 |ρ| 就升到 **0.52–0.60**。DW 比 W² 更直接就是 RV,它的 60 日滚动统计量与 `cross_mean(day_std(Ret), 20)` 的 |ρ| 我预计 **0.6–0.85**(预测 P3/P4,§6)。

**判死它或救活它的办法只有一个,而且只要 2 次评估**:把尺度除掉 —— `div(cross_stddev(day_durbin_watson(High), 60), cross_mean(day_durbin_watson(High), 60))`(RV 的变异系数),再加一个空对照 `cross_stddev(day_std(Ret), 60)`(同一个统计量套在**奖励自己声明的波动度量**上)。见 §4.2 的 R4–R6。

### 1.6 head 8:名义价格风格,但它带来了本轮唯一一条新线索

`ts_sum(LogFloatShares, 30)`,方向 **+1**,hl = 0。6 个日频叶子里只有它出现在 head 里。拆开看:

> `LogFloatCap = log(流通股数 × 价格) = LogFloatShares + log(价格)`

市值控制用的是 `LogFloatCap`。所以 LogFloatShares 对控制取残差后 ≈ **−log(价格)**,方向 +1 = **买同市值下的低价股**,也就是 A 股的低价股 / 股本效应。这正是 r1 §1.7 对 `day_median(Vwap)` 的判断,M 用另一个叶子又发现了一次。**它基本是「市值控制的一个换写法 + 一个已知风格」,不是新信息。**

但共性表给了一条**值得追**的东西:

| 均值差 | p | n | 子树 |
|---|---|---|---|
| +1.17 | 0.002 | 12 | `pow_2_5(LogFloatShares)` |
| +1.14 | 0.022 | 6 | `cross_fangzheng(pow_2_5(LogFloatShares), 60)` |
| +1.14 | 0.040 | 4 | `pow_3(pow_2_5(LogFloatShares))` |

`pow_2_5(LogFloatShares)` 与 `LogFloatShares` 当日秩相同(§0b,LogFloatShares > 0),所以**纯凸幂那两项是陷阱 3 的教科书形状**(市值的非线性函数)。有意思的是中间那一项:按 §0c,`cross_fangzheng(x, 60) = cross_mean(x, 60) + cross_stddev(x, 60)`,而 **`cross_stddev(LogFloatShares, 60) > 0` 只会发生在 60 日内流通股数变过的股票上** —— 增发、送转、**限售解禁**。凸幂把这个探测器的幅度按市值放大了,所以它以陷阱的形式被 GP 找到;**但它底下那个「流通股本变动」是一个库里完全没有、与波动无关的事件型信息**。
这条线索我放进 §4.3 的 N-β,并在 §4.2 用 3 个 R 变体以 3 次评估先探它的虚实(挂在 head 8 下做叶子替换)。

### 1.7 代理与血缘假象:r1 的判断被 301 个候选证实了

r1 §1.7 判定三张机械核心卡是「代理 + 血缘固定块」,明确反对给 E 位。存档从 66 个长到 301 个之后:

| 子树 | r1(66 个候选) | r2(301 个候选) | 结论 |
|---|---|---|---|
| `ts_cov(day_median(Vwap), day_var(Ret), 20)` | +0.62,p 0.021 | **+0.08,p 0.570** | 血缘固定块,塌了 |
| `day_median(Vwap)` | +0.44,p 0.047 | **−0.11,p 0.776** | 代理,翻负 |
| `day_var(Ret)` | +0.57,p 0.027 | **+0.49,p 0.093** | 留着,但它就是波动本身 |

**r1 拒绝把 E 位花在这三张卡上,是对的。** 这是 C 组相对于「按核心卡顺序机械取」的做法本轮能摆在桌面上的一处具体收益。
同一张表的负端也要记一笔(它是 r1 的 N 位的尸检):`abs_(day_signed_ratio(Ret, Amt))` 均值差 **−0.79**(p 0.952,n 6),`day_signed_ratio(Ret, Amt)` **−1.02**(p 0.991,n 8)—— **全表最差的两个子树**。资金流失衡这条通道在这个奖励下不只是没信号,是负的(§3.2)。

---

## 2. 烂部件(必要性 ≤ 0,或换掉反而更好)

**先说本轮唯一一个真正量到的「必要性 ≤ 0」**:

| head | 部件 | 必要性 | 变体 | 变体 score |
|---|---|---|---|---|
| 1 | 内层 `ts_sum(·, 1)` | **−0.00** | `ts_sum(pow_2_5(pow_3(day_durbin_watson(High))), 1)` | +1.778 |

这是恒等算子(§0c),必要性为 0 是定义决定的,**不是一个研究结论**,也不适合做 R(替换它什么都不会变)。

**换掉反而更好的(机械 `r_candidates`,2 个)**:

| 增益 | 变体 | score |
|---|---|---|
| **+0.25** | `ts_mean(pow_2(mul(pow_2(day_wmean(Ret, Ret)), day_var(Ret))), 15)`(ts_mean@30→15) | +1.75 |
| **+0.13** | `ts_sum(pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1)), 2)`(ts_sum@1→2) | +1.90 |

两个都 ≥ +0.1,与原 head 的 ρ 必然 ≈ 1,**丢进 R 就会触发替换**,把库里两个 head 换成分数更高的同族写法。
**我建议不要这么花 R 预算**,理由三条:(i) 它们只是窗口参数,「这个窗口是烂部件」在 train 上挑出来的,审计员评 R 的合理度看的是「去掉或替换的部件是否**真是**烂的」,窗口微调拿不到 3 分;(ii) 替换进来的 head 与被替换的那个在交易信号上几乎同一条线,**库在样本外不会因此变好**,而最终比的就是库的样本外表现;(iii) 这两次评估买到的信息量为零(数字已经在 `loc.json` 里了)。
如果 PI 仍然想要这两分,成本是 2 个 R 槽,但请在 `missions.yaml` 里写明它是「分数操作」而非「去烂部件」,让审计员分开评。

**然后是「虽然必要性 > 0,但那部分必要性里没有新信息」的部件 —— 本轮 R 真正该打的靶子**:

| head | 部件 | 必要性 | 为什么是烂的 | 依据 |
|---|---|---|---|---|
| 1 | `pow_2_5`(e: 3 → 7.5) | **+0.81** | 当日秩不变(§0b),增益全在 train(§1.2),而且把 45% 的截面打成并列(§0e) | 源码 + distinct 0.55 + train/valid 分解 |
| 1 | `pow_3`(e: 1 → 3) | **+1.06** | 同上,当日秩不变 | 同上 |
| 2 | 外层 `pow_2` | **+0.62** | 同一个凸化旋钮,套在 W⁴·RV² 上;`cs_winsor` 的对照(head 7 = +0.55)说明「水平版」没有分 | §1.3(iii) |
| 2 | `mul(·, day_var(Ret))` | **+0.17** | 它就是波动本身,乘上去等于把中性化想去掉的东西手动加回来(陷阱 3) | §1.3(ii) |
| 4 | `cross_stddev` 的未去尺度 | **+2.28** | 必要性极高,但未判:到底是 vol-of-vol 还是 RV 水平 | §1.5,**待 R4–R6** |
| 8 | 叶子 `LogFloatShares` | 未测 | = `LogFloatCap − log(价格)`,而 LogFloatCap 是控制;残差就是低价股风格 | §1.6,**待 R7–R9** |

**明确不是烂部件、不要动的**:head 3/5 的内层 `pow_2`(把带符号的 W 折成 W²,必要性 +1.08 / +0.34,`day_wmean(Ret, Ret)` 单独 −0.19);head 4 的 `cross_stddev` 这个算子本身(必要性 +2.28,是它全部的分)。

---

## 3. 之前的任务

### 3.1 E 位 `c06s807Cr1a_Ea`:核心 `pow_2(day_wmean(Ret, Ret))`,84 次评分,20 个过线,**4 个入 heads**

采样计数 `{'c05_no_core': 1519, 'c05_periphery_seen': 6}` —— 被拒的 1519 次是「不含核心」,只有 6 次是「外围与已见过的相同」,说明外围约束几乎没有咬住,GP 的搜索空间是开放的。

计划里的外围是三件事(`r1/missions_final.yaml`):(1) 同日 RV 型分母去波动尺度(`div(W², pow_2(day_wmean(abs_(Ret), Ret)))` = RSJ²,以及 `div(W², day_var(Ret))`);(2) 20 日波动十分位内排序 `cs_bucket_rank(·, cross_mean(day_std(Ret), 20))`;(3) 显式月度聚合分开「典型日 / 尾部日」,以及 `cross_zscore(cross_mean(·, 5), 60)`。11 个种子里有 9 个属于 (1)(2)。

**实际产出的 5 个最好的候选,一个都不在这三件事里**:

| score | train | valid | 表达式 |
|---|---|---|---|
| +1.49 | +1.49 | +2.45 | `ts_mean(pow_2(mul(pow_2(day_wmean(Ret, Ret)), day_var(Ret))), 30)` |
| +1.12 | +1.12 | +1.64 | `cross_decay_linear(cs_normalize(pow_2(day_wmean(Ret, Ret))), 5)` |
| +1.08 | +1.08 | +1.81 | `cross_mean(cross_mean(mul(pow_2(day_wmean(Ret, Ret)), day_var(Ret)), 241), 5)` |
| +1.06 | +1.06 | +1.06 | `ts_var(ts_var(pow_2(day_wmean(Ret, Ret)), 30), 30)` |
| +1.03 | +1.03 | +1.39 | `ts_var(pow_2(day_wmean(Ret, Ret)), 50)` |

**读法:给定一个含波动尺度的核心和一个不惩罚波动的奖励,GP 必然往回长波动。** 两个最好的都把 `day_var(Ret)` 乘了进来;其余三个是纯日轴再聚合(`ts_var`、`cross_decay_linear`、`cs_normalize`)。去尺度的那一族(RSJ²、波动十分位内排序)连前 5 都没进,而 r1 的 R 直接评估告诉我们它们在 +0.17 ~ −0.75(§1.3)。
**这是 E 位机制的一个结构性结论**(配合 §0a:没有家族控制):E 位会可靠地产出 head,但产出的是**奖励最喜欢的那个机制的下一个写法**,不是计划里那个想检验的机制。写 r2 的 E 位时必须把这件事算进预期。

### 3.2 N 位 `c06s807Cr1b_Nb`:85 次评分,**0 个过线,0 个 head**

计划是 VPIN 型日内资金流失衡(`abs_(day_signed_ratio(Ret, Amt))`、15/30 分钟桶级 `in_sum_rolling`、失衡方向不稳定性、重仓分钟冲击)。最好的 5 个候选和种子毫无关系(全是 `cross_semistd_pos(pow_2(cross_quantile_q75(cs_rank(day_mean(Ret)), 241)), 10)` 一类 GP 自己的随机树),score −0.15 ~ −0.41。

共性表的尸检(§1.7)把结论钉死:`abs_(day_signed_ratio(Ret, Amt))` −0.79、`day_signed_ratio(Ret, Amt)` −1.02,是 301 个候选里最差的两个子树。
**判定:资金流失衡通道在 `long_neutral` 奖励下是负的,不是「没调好」。** 原因可以说清楚(并且 r1 的审计员提前指出了一半):按分钟收益符号硬分类的失衡幅度,其截面变化主要是**估计噪声的大小**(∝ 1/√有效笔数),而噪声大小是流动性的非线性函数;十分位内排序把这部分清掉之后,剩下的量没有方向上的预测力。
**对 r2 的直接影响**:不要再用 `day_signed_ratio` / `day_topw_mean(Ret, Amt)` 这条线做 N;r1 lit.md 的 L4 那一节(含那篇 A 股「聪明钱」的证据)可以归档。

### 3.3 R:11 个变体全部评完,**0 个替换,0 个收录**

`R_prev.json`:`replacements: []`,`additions: []`。11 个都过了 gate(coverage ≥ 0.9、distinct ≥ 0.5),`rho_known` 全部 ≤ 0.23。替换门槛是原 head +0.1 = **+1.28**,最高的是 `pow_1_5(pow_2(day_wmean(Ret, Ret)))` = **+1.07**,差 0.21。
收录门槛需要与原 head 的 ρ < 0.5:满足的有 variant 9(`cs_bucket_rank(...)`,ρ 0.21)、variant 4(`cross_med`,ρ 0.38)、variant 2(`cross_quantile_q75`,ρ 0.38)、variant 8(路径效率,ρ 0.47)—— 但它们的 score 是 −0.75 / −0.18 / −0.11 / −0.71,一个都不够 +1.28。
**所以 11 次评估换到的全部是「证据」,没有「库里的东西」。** 这正是 r1 §2 预期的用法,而且买到的证据质量很高(§1.3 整节都建立在它上面)。本轮 R 应该继续这么用,但要加一条:**优先选那些「赢了也对库有好处」的变体**(§4.2 的 R7–R9 是 1 次评估就可能**收录**一个与波动无关的新 head)。

### 3.4 审计员挡掉了什么,为什么,事后看对不对

两个位都是 1 次过审(创新度 3 / 合理度 3,R 组合理度 3),共划掉 6 个种子:

| 划掉 | 理由(audit_1.yaml) | 事后看 |
|---|---|---|
| a 位种子 10、11(`div(·, pow_2(LimitWidth))`) | `LimitWidth` 在 `tradability.board_limit` 里只是**板块 × 日期哑变量**(主板 0.10 / 科创与 2020-08-24 起创业板 0.20 / 北交所 0.30),除以它² 实现的是板块倾斜,并在 train 内制造 2020-08-24 结构断点;Hung–Yang 的归一化针对被日涨跌停截断的日收益 MAX,分钟自加权的 W 不被日限幅直接截断 | **对,而且这条判断可以复用**:`BoardCode` 同理(板块哑变量),r2 的任何位都不要用它做条件化 |
| b 位种子 5 | 相关度表 liq 0.51 / known 0.53 → 机械划掉 | 对(与已知族 ≥ 0.5 本来也会判不合格) |
| b 位种子 3、4 | 它们是 5 的单日版,20 日平均后升到 0.51/0.53,说明持久部分就是流动性;「每个时间窗里成交越稀,\|失衡\| 的抽样噪声越大(∝ 1/√笔数)」,属陷阱 3 | **对,而且比 PI 看得准** —— §3.2 的尸检说明整条通道就是这个问题 |
| b 位种子 12 | 「两个噪声比值之差的绝对值」主要量估计噪声,liq 0.45 / known 0.40 / size 0.42 三个控制同时贴近 0.5 | 对 |

审计员在 R 组的意见里还提前写对了两件事,本轮应当承认:

1. 「变体 1(`cross_max`)、3(`cross_tail_mean_q75`)与 head 的**残差** |ρ| 0.91 / 0.90,只是把『追极端日』从隐式写成显式,并没有去掉判为烂的那部分」—— 实测 +0.77 / +0.81,确实既没超过 head,也没换掉机制。
2. 「变体 1–4 对未去尺度的 W² 做 20 日聚合后,与波动控制的原始 |ρ| 升到 0.52 / 0.60 / 0.57 / 0.55 …… **而 R 的替换规则只查已知族不查波动**,它们若凭非线性波动胜出会把一个波动代理换进库」—— 本轮它们没赢,但这条规则漏洞仍然在,而 r2 我要提的 R 变体里就有两个踩在上面(§4.2 的提醒)。

审计员**唯一**偏保守的地方:它说「RSJ⁴、(W/std)⁴ 与 head 的原始 |ρ| 0.94 / 0.95,说明逐日截面上 σ 尺度并不主导 W 的排序,这个部件『烂』目前只有理论依据」。事后看,**原始日度秩 |ρ| 0.94 和「score 差 1.0」是可以同时成立的**(§5.1)—— 用 ρ 来推断「尺度不主导」这一步不成立。这不是审计员的错(它只能看相关度表),但 r2 的解剖文件应该把这件事讲清楚,免得同一个推论再做一次。

### 3.5 上一轮笔记里的预测对不对

`notebook.md`(PI)的预测:

| 预测 | 实际 | 判 |
|---|---|---|
| a 位产出 ≥ 1 个 head 概率 ~0.40 | 4 个 head | **对**(但低估) |
| 「如果有,最可能是波动十分位内的 W² 月度尾部 / RSJ² 一类,score 0.5–0.9」 | 实际是 W⁴·RV²、W⁴ 再聚合,score 1.03–1.49 | **错**:种类错、量级错 |
| 「valid ≥ train」 | 5 个最好的里 4 个成立 | 对 |
| b 位(N)产出 ≥ 1 个 head 概率 ~0.35 | 0 个,最好 −0.15 | **对**(低概率押注,结果落在预期的另一侧) |
| 「若信念 3 的波动部分占大头,去掉波动后分数会掉到 0.5 以下」 | RSJ⁴ +0.18、(W/σ)⁴ +0.17、十分位内 −0.75 | **对,而且这是本轮最重要的一条验证** |
| P1:`cross_max(pow_2(day_wmean(Ret, Ret)), 20)` score ≥ 0.9 且 valid ≥ train(0.50) | +0.77;valid 1.07 ≥ train 0.77 | **半对**(valid ≥ train 对,≥0.9 错) |
| P2:变体 6–8 都比 head 低 0.3 以上(0.55) | 低 1.00 / 1.01 / 1.89 | **对** |
| P3:变体 9(波动十分位内 W⁴)score ≥ 0.5(0.50) | **−0.75** | **错,错得很远** |
| P4:变体 10、11 都低于 head(0.60) | +0.83、+0.26 | **对** |
| P5:R 最多 1 个变体触发替换或收录(0.65) | 0 个 | **对** |

`r1/analysis.md` §6 的 6 条:P1 半对、P2 **未评**(PI 把波动空对照 `pow_2(pow_2(day_std(Ret)))` 从最终 11 个变体里删掉了 —— 这是 r1 最可惜的一个决定,本轮必须补,见 R3)、P3 错(路径效率 −0.71)、P4 **对**(p = 2 → 3 → 4:train +0.89 → +1.07 → +1.18 单调升,valid +1.66 → +1.54 → +1.35 单调降)、P5 错(4 个 head 不是 ≤1)、P6 对。

**三条信念的重新打分**:信念 1(信息在幅度不在方向)**仍然成立**,但含义变了 —— 幅度里有信息的那部分是**波动尺度**,不是「单边程度」;信念 2(外层凸化不带当日截面信息、增益全来自 EMA)**完全证实**,而且本轮由源码注释(§0b)升级成了定理,并推广到整个 DW 阶梯;信念 3 从 ~0.45 升到 **~0.9**(波动尺度就是来源)。

---

## 4. 本轮候选

### 4.1 值得深挖的核心

#### 先说明确反对的:整个 DW(High) 族,一个 E 位都不要给

机械核心卡的前 3 名里有 2 个、前 12 名里有 6 个是这一族:
`pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1))`(卡 1,自身 +1.78)、`cross_stddev(day_durbin_watson(High), 60)`(卡 3,+1.10)、`ts_sum(pow_3(day_durbin_watson(High)), 1)`(卡 6)、`pow_3(day_durbin_watson(High))`(卡 7)、`ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)`(卡 9)、`cross_fangzheng(pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1)), 60)`(卡 11)、`day_durbin_watson(High)`(卡 12)。**按卡序机械取核心的做法,本轮第一张卡就会落在这里。** 反对的理由按强度排:

1. **规则 §3 的确定性门槛很可能直接挡掉它**:「E 位还要求核心与每个控制的 |ρ| < 0.5」。DW(High) 就是日内已实现方差(§0d),波动控制是 `cross_mean(day_std(Ret), 20)`。参考量级:r1 相关度表里,仅仅是 W² 的 20 日聚合,与波动控制的原始 |ρ| 就到 0.52–0.60。我预计 DW(High) 的 |ρ| 在 **0.55–0.75**,`cross_stddev(DW, 60)` 在 **0.6–0.85**(预测 P3/P4)。**请 PI 先让相关度表算这一列,再决定要不要写这个位** —— 如果 ≥ 0.5,写了也是白写一次审计。
2. **它是陷阱 1 的正面命中**(§1.2 的四点凸度曲线 + §0b 的源码),合理度最多 1 分(「利用了下面的已知陷阱」),位直接不通过。
3. **最高分那张卡还踩在 float32 下溢上**(§0e,distinct 0.5523 擦着 0.5 门槛过),它的多头腿成员由控制投影决定。
4. **库禁令会把外围锁死**:核心的任何单调重写与 head 1 的日度秩 |ρ| = 1.00,一律被拒;GP 只能往 `cross_stddev` / `cross_fangzheng` 那种二阶统计量上长,而这正是 head 4 和卡 11 已经占住的位置。

#### 核心 A(推荐,本轮唯一的 E 位):`pow_2(day_wmean(Ret, Ret))`

- **E 位额度**:整个实验每个核心 ≤ 2 个 E 位,这个核心已用 1 个(r1 a 位),**还剩 1 个,用完就没有了**。
- **门槛**:r1 相关度表给过这个核心的控制列 —— liq 0.06、vol 0.22、rev 0.15、known 0.07、size 0.13,**5 个控制全部 < 0.5**,是快照里少见的满足 E 位硬门槛的核心(本轮请相关度表复算一次确认)。
- **诚实的预期**:§3.1 说明 E 位会产出 head,但产出的是奖励最喜欢的机制的下一个写法。这个位要么拿到 1–3 个「W² 又一种日轴聚合」(对库的样本外帮助很小),要么拿到 0 个真正不同的东西。**它的价值在于把这个核心的最后一个 E 位用在「还没试过的外围族」上,把这个核心彻底做完**,而不是指望它产出高分。
- **周围已经见过的外围写法**(我能从 301 个候选的共性表 + 4 个 E 产出 + 11 个 R 变体 + 13 个种子里枚举到的;`episodes/` 禁读,所以这是**下界**,但引擎会用 `--periphery-seen` 从存档现算,不依赖我枚举全):
  - **外层幂**:`pow_2`(→W⁴)、`pow_1_5`、`pow_2_5`(经由 R);
  - **日轴再聚合**:`ts_mean(·, 25/30/50/100)`、`ts_var(·, 30/50)`、`ts_var(ts_var(·, 30), 30)`、`cross_mean(·, 5/10/20/241)`、`cross_med(·, 20)`、`cross_max(·, 20)`、`cross_min(·, 30)`、`cross_quantile_q75(·, 20)`、`cross_tail_mean_q75(·, 20)`、`cross_decay_linear(·, 5)`、`cross_zscore(cross_mean(·, 5), 60)`;
  - **截面包装**:`cs_normalize`、`cs_winsor`、`cs_bucket_rank(·, cross_mean(day_std(Ret), 20))`、`cs_bucket_rank(·, cross_mean(day_sum(Amt), 20))`;
  - **同日伙伴 / 分母**:`mul(·, day_var(Ret))`、`div(·, day_var(Ret))`、`div(·, pow_2(day_wmean(abs_(Ret), Ret)))`(RSJ²)、`div(·, day_std(Ret))`、`div(·, pow_2(LimitWidth))`(已被审计划掉)、叶子换 `day_wmean(Ret, Amt)` / `day_mean(Ret)` / `day_signed_ratio(Ret, Ret)`;
  - **共现块**:`ts_cov(day_median(Vwap), day_var(Ret), 20)`、`day_var(Ret)`、`day_std(Ret)`。
- **三族还没碰过的外围**(建议本位只长这三族,每一族都避开上面的词汇):
  1. **日内「什么时候动的 / 怎么动的」做伙伴** —— 共性表里一个这样的算子都没有,`Open` 字段在整张表里**一次都没出现过**。
     例:`mul(pow_2(day_wmean(Ret, Ret)), day_centroid(Amt))`(`ops_ext.py` 第 155 行,|x| 的日内重心)、`div(pow_2(day_wmean(Ret, Ret)), day_gini(Amt))`、`mul(pow_2(day_wmean(Ret, Ret)), day_at_max_ratio(Close))`、
     `div(pow_2(day_wmean(Ret, Ret)), pow_2(day_wmean(in_slice(Ret, 1, 120), in_slice(Ret, 1, 120))))`(下午 vs 上午的单边程度之比 —— 注意核心必须原样出现,所以时间切片只能放在**分母**里,不能替换核心内部的 `Ret`)。
     机制:同样幅度的单边日,**尾盘才走完**的那种与开盘一次性跳完的那种是两件事(收盘定价 / 被动资金 / 注意力);这个比值是**无量纲**的,不会把波动尺度再乘一遍。
  2. **静态公司特征做条件化,但只用连续的那两个**:`ListAge`、以及 `sub(LogTotalCap, LogFloatCap)`(= log(总股数/流通股数),**价格精确抵消**,是纯股本结构量,库里完全没有)。
     例:`cs_regres(pow_2(day_wmean(Ret, Ret)), ListAge)`、`mul(pow_2(day_wmean(Ret, Ret)), sub(LogTotalCap, LogFloatCap))`、`cs_bucket_rank(cross_mean(pow_2(day_wmean(Ret, Ret)), 20), ListAge)`。
     **不要用 `BoardCode` 和 `LimitWidth`** —— 审计员已经判过:板块 × 日期哑变量,实现的是板块倾斜,还在 train 内带 2020-08-24 的结构断点(§3.4)。
  3. **时间位置而非时间幅度的聚合**:`cross_argmax(·, 20)`(最单边那天离今天多远)、`cross_sustain`、`cross_rank(·, 60)`、`ts_rank` —— 都不在已见词汇里,而且它们**不是** EMA(核心) 的单调函数,所以不会被库禁令一刀切掉。
- **给 PI 的硬提醒**:种子不能是核心的单调重写(库禁令 ρ = 1.00 直接拒),也不要再出现 `day_var` / `day_std` / `day_durbin_watson` 作为乘数或分母 —— 乘上去是把中性化要去的东西手动加回来(§1.3 ii,陷阱 3),除下去已经测过是 +0.17(§1.3 i)。**这个位的全部意义就是:在不碰波动的前提下,这个核心还剩什么。**

#### 核心 B(备选,仅在相关度表证明核心 A 的 vol 列意外超过 0.5 时启用):`mul(pow_2(day_wmean(Ret, Ret)), day_var(Ret))`

卡 4,自身 +1.10。我**不推荐**:它把 `day_var(Ret)` 焊进核心,E 位的奖励不控制波动,等于让 GP 在一个已经是波动代理的东西外面继续长;它与波动控制的 |ρ| 几乎肯定 ≥ 0.5,会被 §3 的门槛挡掉。列在这里只是因为任务要求 ≤3 个候选时说清取舍。

**第三个核心:我不凑。** 剩下的卡要么是 DW 族(上面已反对),要么是 LogFloatShares 的凸幂(陷阱 3,且与 size 控制 |ρ| 必然 ≥ 0.5),要么是 `day_var(Ret)`(就是波动控制本身)。

### 4.2 R 目标(16 个额度,我提 12 个,按信息价值排序)

硬约束:每个变体必须挂在**快照里已有的 head** 下(`c05_locate.py` 第 179–181 行),8 个 head 都可以挂。每个变体都会给完整的 `score / train / valid / rho_known / coverage / distinct`,不管有没有达到替换门槛,所以**一次评估至少买到一条证据**。替换门槛(原 head + 0.1):head 1 → **+1.875**,head 2 → +1.594,head 3 → +1.281,head 4 → **+1.201**,head 5 → +0.931,head 6 → +0.690,head 7 → +0.650,head 8 → **+0.620**。

**⚠️ 先提醒一条规则漏洞(r1 审计员已经指出过)**:R 的替换/收录规则只查**已知族** |ρ| < 0.5,**不查波动控制**。下面 R3、R5 是故意构造的波动空对照,如果它们胜出,规则会把一个**显式的波动因子**写进库。请 PI 在提交前让相关度表给出每个 R 变体的 vol 列,并对 vol |ρ| ≥ 0.5 的变体在 `missions.yaml` 里**声明它是诊断用、不接受替换**(或干脆把它们放在最后,预算不够就砍)。

**第一组:判 head 1 的 +1.78 是不是数值假象(挂 head 1)**

| # | 变体 | 要回答什么 | 我的预期 |
|---|---|---|---|
| **R1** | `ts_sum(pow_2_5(ts_sum(pow_3(mul(day_durbin_watson(High), 1000.0)), 1)), 1)` | **纯数值检验**。(1000·DW)^7.5 = 1000^7.5 · DW^7.5,是正常数倍;EMA 是线性的,`_zrank` 对正仿射不变 ⟹ **数学上与 head 1 逐位同秩、同 score**。唯一的差别是不再下溢。常数字面量合法(`parser.py` 第 112 行)。 | `distinct` 从 0.55 跳到 ≈ 1.00(P1);score 与 +1.78 相差 ≥ 0.3 |
| **R2** | `ts_sum(pow_2_5(ts_sum(pow_3(cs_winsor(day_durbin_watson(High))), 1)), 1)` | 把当日截面的 1%/99% 尾部剪掉再做同样的凸化:按 `cs_winsor` 的 docstring,这是「peak memory → level」的标准对照,同时顺手消掉下溢的极小端 | score 掉到 +0.9 以下 |
| **R3** | `pow_2_5(ts_sum(pow_3(day_std(Ret)), 1))` = σ^7.5 | **波动空对照**(r1 §4.2 的 R1,被 PI 删掉了,本轮必须补):同一条凸化阶梯套在**奖励自己声明的波动度量**上,量级 0.002^7.5 ≈ 1e-20,不下溢。若它也在 +1 以上,head 1 就是「低波动异象的多头腿」换了个字段 | +0.9 ~ +1.5(P2) |

**第二组:判 head 4 是 vol-of-vol 还是 RV 水平(挂 head 4)**

| # | 变体 | 要回答什么 |
|---|---|---|
| **R4** | `div(cross_stddev(day_durbin_watson(High), 60), cross_mean(day_durbin_watson(High), 60))` | **去尺度的 vol-of-vol**(变异系数)。RV 近似乘性 ⟹ 未去尺度的 std ∝ 水平;这个比值把水平除掉。留得住 ⟹ head 4 真是「风险的不确定性」;掉下去 ⟹ 它就是 RV 水平的又一个写法 |
| **R5** | `cross_stddev(day_std(Ret), 60)` | **空对照**:同一个统计量套在波动控制的被平均量上(⚠️ 见上面的漏洞提醒,门槛 +1.201 并不远) |
| **R6** | `cross_mean(day_durbin_watson(High), 60)` | **水平基线**:60 日 RV 均值。它与波动控制的 \|ρ\| 本身就是最该量的那个数(§1.5) |

**第三组:判 head 8 是不是只是低价股,并顺手给库找一个与波动无关的新 head(挂 head 8)**

head 8 = `ts_sum(LogFloatShares, 30)`,门槛只有 **+0.62**,**收录**门槛是与 head 8 的 ρ < 0.5 且与全部 head |ρ| < 0.7 —— 这三个变体是本轮**最便宜的「可能给库加一个新机制」的通道**,各 1 次评估。

| # | 变体 | 要回答什么 |
|---|---|---|
| **R7** | `ts_sum(sub(LogFloatCap, LogFloatShares), 30)` | = 30 × log(价格),**精确**。若它的 score ≈ +0.52 且与 head 8 的 ρ ≥ 0.5 ⟹ head 8 就是名义价格风格,库里该记成「低价股」而不是「流通股本」(诊断,不求替换) |
| **R8** | `ts_sum(sub(LogTotalCap, LogFloatCap), 30)` | = 30 × log(总股数/流通股数) = **锁仓比例的对数**,价格精确抵消。库里完全没有的输入,与波动无关;若 ≥ +0.62 且与 head 8 的 ρ < 0.5 ⟹ **直接收录成新 head** |
| **R9** | `ts_sum(ts_delta(LogFloatShares, 241), 30)` | = 一年内流通股本的对数增长(增发 / 送转 / **限售解禁**)。共性表的 `cross_fangzheng(pow_2_5(LogFloatShares), 60)`(+1.14,p 0.022)里的 std 项就是这个探测器(§0c/§1.6)。**注意风险**:股本不变的股票上恒为 0,`distinct` 可能过不了 0.5 的门槛 —— 这一次评估即使 gate 不过也值得,因为它直接告诉我们 N-β 能不能做 |

**第四组:给 W 族的两个精确替换(挂 head 2 / head 5)**

| # | 变体 | 要回答什么 |
|---|---|---|
| **R10** | `ts_mean(pow_2(div(pow_2(day_wmean(Ret, Ret)), day_var(Ret))), 30)` | 把 head 2 里的 `mul` 换成 `div`,**只动这一个部件**。乘波动 +1.49、除波动若掉到 0.5 以下 ⟹ 那个部件就是波动本身,证据链闭合(§1.3 ii 的严格对照) |
| **R11** | `ts_mean(cs_winsor(pow_2(mul(pow_2(day_wmean(Ret, Ret)), day_var(Ret)))), 30)` | 对外层凸化的「level 版」对照:必要性 +0.62 的那个 `pow_2` 是不是只是峰值记忆 |
| **R12** | `cross_mean(mul(pow_2(day_wmean(Ret, Ret)), day_centroid(Amt)), 20)` | 挂 head 5(门槛 +0.931)。把波动伙伴换成**日内时点**伙伴 —— 既是 R 的部件替换,也是核心 A 的 E 位第 1 族的 1 次预探;赢了就是一个不含波动的新 head |

剩 4 个额度留给 PI。**不建议**用在 §2 里那两个窗口微调(ts_mean@30→15、ts_sum@1→2)上,理由见 §2。

### 4.3 N 的灵感

**首选 N-α:隔夜 vs 日内的「拔河」(overnight–intraday tug of war)。**

- **为什么是它**:(i) **库里一个相关的东西都没有** —— 301 个候选的共性表里 `Open` 字段**一次都没出现**,也没有任何跨日的「昨收→今开」构造;(ii) 它不是波动的函数,也不是 5 个控制的非线性重写(见下面的正交化写法),所以不踩任何已知陷阱;(iii) 2023-08-08 之前有扎实的文献(Lou–Polk–Skouras 2019 JFE「A Tug of War」;Berkman 等 2012 JFQA),说的是**公司层面持续数月的特征**,不是日内噪声 —— 这对 15 bp 成本 + 纯多头书很关键;(iv) 与 r1 的 N 失败原因正交:那条线死在「测的是估计噪声的大小」(§3.2),这条线测的是**收益在一天里的归属**,不含任何 1/√笔数 的噪声尺度。
- **算子怎么写**(全部可表达,源码已核对:`day_first`/`day_open`/`day_last`/`day_close` 在 `dt_day.py` 第 129–148 行,`ts_delay`/`ts_delta` 在 `nd_ts.py` 第 113–135 行;`parser.py` 第 55 行的官方 `ret_1d` 别名就是这个形状):
  - 隔夜:`sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1)`
  - 日内:`sub(div(day_last(Close), day_first(Open)), 1)`
  - **关键的正交化**:20 日反转控制是 `div(day_last(Close), ts_delay(day_last(Close), 20))`,即**总**收益。所以种子要取**两条腿的差**而不是任一条腿 —— `sub(ts_sum(隔夜, 60), ts_sum(日内, 60))` 这种写法在构造上就把「总收益」那一维去掉了,留下的是纯归属。窗口用 60 / 120 / 241(文献里这是一个持续性特征,长窗口同时压住换手)。
  - 幅度版(与方向版对照):`cross_mean(abs_(隔夜), 20)` —— 但要提醒:这是跳空幅度,**与波动强相关**,很可能被判成陷阱 3;只放 1–2 个作为对照,不要作为主线。
- **方向**:文献是隔夜正、日内负(散户在开盘集中买入 → 隔夜收益高的股票后续更差还是更好,两派证据都有);**方向由奖励在 train 上定**,两边都解释得通,这一点要在 `missions.yaml` 里写清楚,别承诺。
- **预期审计**:创新度 4(输入与机制都不同,与所有 head 的 |ρ| 几乎肯定 < 0.3);合理度 4(有 2023-08-08 前的文献证据)。风险:涨跌停一字板的开盘价会把跳空截断(可以用 `ListAge` / 成交额十分位内排序缓解,**不要用 BoardCode/LimitWidth**);A 股的集合竞价开盘对 `day_first(Open)` 的含义需要在 §7 的 L1 里向文献员确认。

**次选 N-β(建议留到第 3 轮,本轮先用 R8/R9 花 2 次评估预探):股本结构与解禁供给。**

- 来源:§1.6 —— M 的 GP 在 301 个候选里反复找到 LogFloatShares 族(12 + 6 + 4 次,均值差 +1.17 / +1.14 / +1.14),但全部是**凸幂**的形式,也就是陷阱 3 的形状;底下那个真东西是 `cross_fangzheng` 的 std 项,它探的是「这 60 天里流通股本变过没变」。
- 干净的写法:`sub(LogTotalCap, LogFloatCap)`(锁仓比例,**连续、价格精确抵消**)、`ts_delta(LogFloatShares, 241)`(一年股本增长)、以及两者与 `ListAge` 的交互(上市 1–3 年的股票有可预期的解禁时间表)。
- 机制:限售解禁 / 增发把可交易供给放大,供给压力 → 负收益;低自由流通比例 → 筹码集中、定价被少数持有人主导。文献(§7 的 L2)在 2023-08-08 之前是齐的。
- **为什么本轮不做主线**:零膨胀风险 —— `ts_delta(LogFloatShares, 241)` 在股本不变的股票上恒为 0,`distinct ≥ 0.5` 的门槛可能直接拦住,而且并列会让十分位书的成员由列序决定(陷阱 2)。R8/R9 两次评估就能把 coverage/distinct 量出来,再决定第 3 轮要不要给 N 位。

**明确不建议再做的 N**:任何 `day_signed_ratio` / `day_topw_mean(Ret, Amt)` 的资金流失衡变体(§3.2 的尸检),以及任何以「波动的某种非线性函数」为输入的新想法(陷阱 1/3,合理度 1 分)。

---

## 5. 方法学警告(请 PI 写进 notebook;第 1 轮的 5 条继续有效)

### 5.1 新增(本轮最重要):**原始日度秩 |ρ| 高到 0.95,score 仍可以差 1.0**

`pow_2(pow_2(div(day_wmean(Ret, Ret), day_std(Ret))))` 与 head 3 的原始日度秩 |ρ| = **0.95**,score 却是 **+0.17 vs +1.18**;`cs_bucket_rank(pow_2(pow_2(day_wmean(Ret, Ret))), cross_mean(day_std(Ret), 20))` 的 |ρ| = **0.97**,score **−0.75**。
原因在 §0a/§0b:**score 不是由当日截面秩决定的**,而是由「EMA 怎么混合不同的日子」+ 「残差书只持十分位」决定的。于是有两条推论:

1. **库禁令的 ρ ≥ 0.7 和「信息是否重复」几乎是两件事。** 库里可以塞满日度秩高度相关、但交易信号不同的 head(反过来也成立)。r1 相关度表里的「残差」列才是接近交易信号的那个量(variant 5 残差 0.98、variant 9 残差 0.21)。**最终比的是库的样本外表现,所以 PI 在选要不要收录一个 head 时,应该看残差列,不是原始列。**
2. **不能用「与 head 的 ρ 很高」来论证「某个部件不重要」。** r1 审计员正是在这里偏保守了一次(§3.4)。

### 5.2 新增:`distinct` 和 `coverage` 不只是门槛,是**诊断**

`distinct_fraction` 的 docstring 自己说并列会让十分位书的成员由列序决定。本轮 head 1 的 distinct = 0.5523(擦着 0.5 过),其余每一行都 ≥ 0.997。**建议把「distinct < 0.9 且它是一个连续量的函数」当成红旗**,在 `missions.yaml` / 审计记录里显式写出来:它意味着表达式在 float32 下塌了(§0e),而不是数据的性质。

### 5.3 继续有效的(r1 §5)

1. 共性表的 p 不能当检验用(末代精英存档,同血缘,Mann–Whitney 反保守)。本轮的反面教材正好有:`ts_cov(day_median(Vwap), day_var(Ret), 20)` 从 +0.62(p 0.021)塌到 +0.08(p 0.570),`day_median(Vwap)` 从 +0.44 翻到 −0.11。
2. 「均值差 > 0」≠「好」:存档均值约 −0.65,很多正均值差的 `mean_with` 仍是负的。
3. 中性化是秩空间里的线性投影,删不掉与控制的非线性 / 尾部关系(本轮整篇都在说这件事)。
4. 方向、半衰期、被选中的幂次都只在 train 上定;本轮的凸度阶梯(§1.2)显示**凸化买到的分数全在 train 上,valid 从 e = 2.5 起就饱和**。
5. 「必要性 / 敏感性」缺失 ≠ 为零。本轮 28 次拆解把这个缺口补上了大半,但 head 6、7、8 一行拆解都没有(`ablation` 只覆盖了 4 个 head)。

### 5.4 新增:两条规则漏洞,PI 需要自觉

- **R 的替换/收录只查已知族 |ρ| < 0.5,不查波动控制**(r1 审计员发现)。本轮 R3、R5 是故意的波动对照,有可能达到替换线;请在计划里声明它们是诊断用途。
- **E 位没有家族控制**(§0a),所以 E 位的分数与 head 直接可比,「产出 head」这件事比看起来容易得多;head 数不是这个位成功的好指标,**机制是否新**才是。

---

## 6. 可核对的预测(供第 3 轮打分)

| # | 预测 | 置信度 |
|---|---|---|
| **P1** | R1(`mul(day_durbin_watson(High), 1000.0)` 版)的 `distinct` ≥ 0.95(head 1 是 0.5523)—— 即 head 1 的并列是 float32 下溢,不是数据性质 | **0.85** |
| **P2** | R3(`pow_2_5(ts_sum(pow_3(day_std(Ret)), 1))` = σ^7.5)的 score ≥ +0.9 —— 同样的凸化套在声明过的波动度量上一样能跑出高分 | 0.60 |
| **P3** | 相关度表里 `day_durbin_watson(High)` 与波动控制 `cross_mean(day_std(Ret), 20)` 的原始日度秩 \|ρ\| ≥ 0.5 | 0.70 |
| **P4** | `cross_stddev(day_durbin_watson(High), 60)` 与波动控制的 \|ρ\| ≥ 0.5,且 R4(变异系数版)的 score < +0.5 —— head 4 是 RV 水平而不是 vol-of-vol | 0.55 |
| **P5** | R7(`ts_sum(sub(LogFloatCap, LogFloatShares), 30)` = log 价格)与 head 8 的日度秩 \|ρ\| ≥ 0.5,且 score 落在 +0.52 ± 0.3 —— head 8 就是低价股风格 | 0.60 |
| **P6** | R10(head 2 的 `mul` 换成 `div`)的 score 比 head 2 低 ≥ 0.8 | 0.65 |
| **P7** | 核心 A 的第 2 个 E 位产出 ≥ 1 个 head;但**它产出的每一个 head 都仍然含有同日波动量**(`day_var` / `day_std` / `day_durbin_watson`,或未去尺度的 W 的再聚合),而不是 §4.1 第 1/2 族的时点 / 股本结构伙伴 | 0.60 |
| **P8** | N-α(隔夜−日内)若立位,产出 ≥ 1 个 head 的概率 | 0.30 |
| **P9** | R9(`ts_delta(LogFloatShares, 241)`)的 `distinct` < 0.5,gate 不过 | 0.55 |

---

## 7. 文献题目(4 个,交文献员;只用 2023-08-08 之前发表的文献)

**L1 —— 对准 N-α(隔夜 vs 日内的收益归属)**
把一只股票的日收益拆成**隔夜段(昨收→今开)**与**日内段(今开→今收)**,文献里是怎么构造、怎么处理、结论是什么?具体请找:(a) 构造细节 —— 用开盘集合竞价价格还是开盘后第一笔?复权与停牌日怎么处理?**一字板 / 涨跌停的开盘价**会不会被当成缺失;(b) 它是**持续的公司特征**还是短期效应 —— 用多长的回看窗口(1 月 / 6 月 / 1 年)、半衰期多长、换手和交易成本怎么报;(c) 符号 —— 隔夜段高的股票未来收益更高还是更低,两派结论各自的样本与解释(散户开盘集中买入 / 机构日内交易 / 注意力);(d) 怎么与**动量 / 反转 / 波动 / 流动性**分开(是否直接取两段之差以消掉总收益);(e) **A 股**上有没有做过(集合竞价制度、T+1、涨跌停对隔夜段的影响)。
关键词:overnight versus intraday returns; tug of war Lou Polk Skouras; overnight return premium; close-to-open return cross-section; opening auction retail buying; Berkman Koch Tuttle Zhang paying attention /
隔夜收益;开盘跳空;隔夜与日内收益拆分;集合竞价;隔夜收益率横截面;T+1 与隔夜持仓

**L2 —— 对准 N-β / R7–R9(股本结构、解禁与增发供给)**
**自由流通比例(流通股/总股本)**与**流通股本的变动(增发、送转、限售解禁)**作为横截面收益特征,文献里怎么度量、怎么处理?具体请找:(a) 度量 —— 用比例的水平、对数,还是 N 日 / 1 年的变动?有没有用「未来将解禁的份额」这种前瞻口径(我们**不能**用任何未来信息,只能用已发生的变动);(b) **与规模和名义价格分开**的做法 —— 这三者机械相关(log 流通市值 = log 流通股数 + log 价格),文献怎么处理这个恒等式;(c) 解禁 / 增发的**事件窗口与持续期**(价格压力是几天还是几个月),以及它在月度截面因子里能不能活;(d) 股票发行量异象(share issuance anomaly)与自由流通比例异象是不是同一件事;(e) **A 股**的限售股解禁、定向增发、股权分置改革后的自由流通比例研究。
关键词:share issuance anomaly; composite equity issuance; free float ratio and stock returns; lockup expiration price pressure; Field Hanka IPO lockup; Pontiff Woodgate share issuance; Daniel Titman /
限售股解禁;自由流通股比例;定向增发;股本扩张与收益;解禁价格压力;股权分置改革

**L3 —— 对准 head 4 与整个 RV 凸尾族(水平 vs 尾部 vs 波动的波动)**
把**日度已实现方差**聚合成月度横截面特征时,「水平」「月内极端值」「波动的波动(vol-of-vol)」这三者在文献里是不是**互相独立的特征**,各自的证据有多强?具体请找:(a) **vol-of-vol / 风险的不确定性**作为独立定价特征的证据(度量方式:已实现方差的滚动标准差?变异系数?有没有做去尺度),以及它在控制了 IVOL / 已实现方差水平之后还剩多少;(b) MAX / 彩票偏好这条线里,「取窗口最大值」相对「取均值」的增量,在控制异质波动率后是否消失(美股 vs A 股);(c) 有没有人系统比较过**同一个日度量的不同幂次 / L_p 聚合**(p = 1, 2, 4, 8)在样本外的稳定性 —— 我们量到的是「train 单调升、valid 从 p = 2.5 起饱和」;(d) **低波动异象的多头腿**单独(只做多低波动)的样本外表现与它对「怎么度量波动」的敏感性。
关键词:vol-of-vol unknown unknowns Baltussen; uncertainty about risk and stock returns; realized variance level versus extremes; MAX effect idiosyncratic volatility; low volatility anomaly long leg; Lp aggregation of daily risk measures /
波动率的波动;风险不确定性;已实现方差水平与极值;最大日收益率效应;低波动异象;异质波动率之谜

**L4 —— 对准核心 A 的 E 位第 1 族(日内「什么时候动的」)**
同样大小的日内波动 / 单边走势,**发生在一天的哪个时段**,在横截面收益预测里被怎样用过?具体请找:(a) 构造 —— 日内收益或成交量的**重心 / 基尼 / 到达最大值的时点 / 尾盘占比 / 开盘半小时 vs 收盘半小时**,哪些有同行评审的横截面证据;(b) **尾盘(收盘前 30 分钟与收盘集合竞价)**的集中交易与次日 / 次月收益的关系(指数再平衡、ETF、收盘定价、被动资金);(c) 这类「时点」变量怎么与**波动水平、成交额、换手**分开 —— 有没有用比值 / 份额这类无量纲写法;(d) **A 股**上(14:30 之后的成交占比、收盘集合竞价 2018 年起的制度变化)有没有可比研究;(e) 换手与成本:这类日内时点特征的持续性有多长,月度聚合后还剩多少。
关键词:intraday timing of volume and returns; late-day trading and returns; closing auction concentration; intraday volume distribution cross-section; half-hour intraday return predictability; U-shape intraday pattern cross-section /
日内成交分布;尾盘成交占比;收盘集合竞价;日内时点与横截面收益;分时收益可预测性

---

## 8. 一页总结

- **第 2 批带来的 4 个新 head 里,3 个是同一件事**:`day_durbin_watson(High)` 就是日内已实现方差(源码:分母不去均值),head 1 = **RV^7.5**。凸度阶梯 e = 1 / 2.5 / 3 / 7.5 的 score 是 **−1.17 / +0.72 / +0.96 / +1.78**,而这四个表达式**每天的截面秩完全相同**(`steer.py` 的 `MONOTONE_NONNEG` 注释原文:这类包装「changes nothing a rank-based book sees on the day -- only how the days mix under the EMA」)。差别 100% 来自 hl = 20 的 EMA 被拉向月内最极端的那一天,而且**全部涨在 train 上**(valid 从 e = 2.5 起饱和在 +2.6)。这就是规则 §4 陷阱 1 的正面命中。
- **最高分那个 head 还踩在 float32 下溢上**:`DW^7.5` ≈ 8e-44,只有 float32 最小非规格数的 56 倍,约一半股票直接变 0 —— `distinct` 从 1.00 掉到 **0.5523**,擦着 0.5 的门槛过。方向 −1 ⟹ 纯多头书买的正是那个并列块,而并列块内的残差排序**完全由 5 个控制决定**。1 次评估(R1,乘 1000 的恒等变换)就能判定。
- **W 族已经被判清**:去掉波动尺度的四种写法 —— RSJ⁴ **+0.18**、(W/σ)⁴ **+0.17**、路径效率⁴ **−0.71**、波动十分位内排序 **−0.75**;把 `day_var(Ret)` 乘回去 **+0.17 的必要性**;「水平版」(cross_med −0.18、cross_quantile_q75 −0.11、缩尾后 +0.55)全部 ≤ 0.55,「峰值记忆版」(|W|³ +1.07、W⁴ +1.18、30 日均 W⁴·RV² +1.49)全部 ≥ 1.07。**r1 的「日内单边程度本身有信息」在样本内被证伪;真来源是波动的凸尾,也就是低波动 / 反彩票异象的多头腿。**
- **本轮唯一可能不是陷阱的是 head 4**(`cross_stddev(day_durbin_watson(High), 60)`,必要性 +2.28,hl = 0):它是二阶矩而不是凸化,文献里 vol-of-vol 是独立特征。但它未去尺度,2 次评估(R4 变异系数 + R5 空对照)就能判。
- **head 8 是名义价格风格**(`LogFloatShares = LogFloatCap − log(价格)`,而 LogFloatCap 是控制),但它底下藏着本轮唯一一条新线索:共性表的 `cross_fangzheng(pow_2_5(LogFloatShares), 60)` 里的 std 项是一个**流通股本变动探测器**(解禁 / 增发)。`sub(LogTotalCap, LogFloatCap)` = 锁仓比例的对数,价格精确抵消,库里完全没有 —— **1 次 R 评估(R8)就可能把它收录成一个与波动无关的新 head。**
- **明确反对**:一个 E 位都不要给 DW(High) 族(7 张核心卡,机械取法的第一张就是它)。它很可能被规则 §3 的确定性门槛直接挡掉(核心与每个控制 |ρ| < 0.5;我预计 vol 列 0.55–0.85),而且合理度只能给 1 分(已知陷阱)。**请 PI 先要这一列数再决定。**
- **建议的本轮配置**:**1 个 E**(核心 `pow_2(day_wmean(Ret, Ret))`,最后一个额度;外围只长三族没碰过的东西 —— 日内时点伙伴、`ListAge` / 锁仓比例条件化、`cross_argmax` 一类时间位置聚合;不许再出现 `day_var` / `day_std` 做乘数或分母)+ **1 个 N**(隔夜 vs 日内的收益归属:`Open` 字段在 301 个候选里一次都没出现过,机制与波动无关,2023-08-08 前文献齐全)+ **12 个 R**(3 个判 head 1 的数值与凸化、3 个判 head 4、3 个判 head 8 并可能收录新 head、3 个给 W 族做精确部件替换)。
- **两条规则漏洞要自觉**:R 的替换只查已知族不查波动(本轮 R3/R5 是故意的波动对照,可能达到替换线,请在计划里声明是诊断);E 位没有家族控制(§0a 更正 r1),所以「产出 head」很容易,**head 数不是 E 位成功的指标,机制是否新才是**。
