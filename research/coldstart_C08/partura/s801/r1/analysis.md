# 结构解剖:种子 801,P 组,第 1 轮

快照 `c07s801M1_I0_open_search`(M 的第 1 批)。heads **0 个**,已评分候选 95 个,R 替换 0 个,`paid: 0`。

## 0. 先说清本轮有什么证据、没有什么证据

定位工具(`scripts/c05_locate.py`)的拆解段只对 **heads** 做消融(第 326–394 行:`todo = [h for h in sorted(heads, ...)]`)。本轮 heads = 0,所以:

| 证据类型 | 本轮有没有 | 来源 |
|---|---|---|
| 共性(均值差 / p / 含它的候选数) | **有**,18 行 | `loc.json: enrichment` |
| 充分性(子树单独当因子的 score) | **完全没有** | `ablation: []`、`paid: 0` |
| 必要性(跳掉一个算子掉多少) | **完全没有**,只能用共性做代理 | 同上 |
| 敏感性:窗口减半加倍 | **只有一对**(cov@15 vs cov@60) | enrichment 第 10 / 16 行 |
| 敏感性:换同类字段 | **完全没有** | 表里没有任何 `Amt` / `Close` 版本 |

**所以本轮所有「来源」判断都是共性(共现)证据,不是因果证据。** 共性的 p 是单边 Mann–Whitney(第 321 行 `alternative="greater"`),既没做多重检验校正,样本又来自同一个 GP 谱系 —— 子树靠繁殖扩散,`n_with = 46` 的有效独立样本远少于 46。本轮第一优先级就是把「充分性」这一栏填上(见 §4.2)。

另外两个必须先摆在桌面上的量级:

- 95 个候选的总体均值可由表反推 ≈ **−1.30**(46 × (−0.9101) + 49 × (−1.6731) = −123.85,/95 = −1.3036;与表尾三行的 `mean_without` −1.3038 / −1.3022 / −1.2974 自洽)。
- 发现门槛是 **+0.50**。表里最好的那一类(`pow_3(LogFloatShares)`,n=4)均值 −0.54,第二好的 `day_durbin_watson(Volume)` 均值 −0.91。**即最强结构类的均值离门槛还差 1.4 个夏普。**
- score 已含方向与半衰期的选择,但两者都只在 **train 上拟合**(`partura/runner.py:168` `sign = dg.sign_from(p64[fit], tgt[fit], ...)`;`partura/books.py:135` 「`sig` is already sign-aligned」,半衰期由 `fit` 切片定)。score = min(train, valid)。所以均值 −1.30 的含义不是「信号反了」,而是 **train 上挑出的方向到 valid 普遍不成立**。这批的病是 train/valid 不稳,不是样本内没东西。

## 1. alpha 的来源

### 1.1 第一步:把表折叠(18 行里只有 13 个不同信号,前 8 行只有 4 个)

奖励规则 §1 写明「任何单调变换(包括凸变换)是同一个信号,拿同样的分」;而且是**先截面排名再做 EMA**,所以根上的单调包装连 EMA 都影响不到,是精确的恒等操作。代码里这件事是显式的:

- `AlphaCube/src/alphacube/operators/common.py:209` `pow_` = 带符号幂:`e <= 1` 时 `sign(x)·|x|^e`,否则 `x^e`。
- `partura/steer.py:177-178`:`MONOTONE_ANY = {pow_05, pow_3, signedpower, sigmoid}`(处处严格递增);`MONOTONE_NONNEG = {pow_1_5, pow_2, pow_2_5, sqrt, abs_}`(操作数非负时递增)。
- `day_durbin_watson` **恒非负**:分子是平方和,分母是平方和 + 1e-8,常数行直接返回 NaN(`dt_day.py:273-298`)。

于是表里这些行是**同一个信号**:

| 折叠后 | 表里的行 | 说明 |
|---|---|---|
| **A** = `day_durbin_watson(Volume)` | 第 2、3、6 行 | `pow_2_5(·)`、`pow_2_5(pow_2_5(·))` 在非负量上都是单调的 |
| **B** = `cross_cov(…, ts_med(day_first(Volume), 30), 15)` | 第 4、5 行 | `pow_05` 是带符号开方,单调 |
| **C** = `cross_cov(…, ts_med(day_skew(Volume), 30), 15)` | 第 7、8、11 行 | 第 11 行 `pow_3(pow_05(·))` = `sign·|x|^1.5`,仍单调 |
| **S** = `LogFloatShares` | 第 1 行 | `pow_3` 是奇次幂,处处递增 |

表格自己证实了这件事:第 4、5 行的 `n_with` 和 `effect` **逐位相同**(4,+0.7193),说明 `pow_05` 那层纯属包装,从不单独出现。

**18 行 → 13 个不同的秩信号;按均值差排的前 8 行只有 4 个不同信号(S、A、B、C);前 10 行只有 6 个。**

一个顺带的、可核对的机制解释:`steer.py` 的 `NONNEG_OPS` 里**没有** `day_durbin_watson`。`nonneg()` 对未知算子保守返回 False,所以规范化不会把 `pow_2_5` 从 DW 上剥掉(注释自己说 "A name missing from the lists only means a rewrite is not made -- never a wrong one")。这正好解释了这批为什么把评估花在单调重写上。

### 1.2 折叠 + 多重检验后,这批里只剩一个统计上站得住的子树

18 次检验,Bonferroni 门槛 0.05/18 ≈ **0.0028**。表里只有 A 的两行进得去(`day_durbin_watson(Volume)` p = 0.0002、`pow_2_5(day_durbin_watson(Volume))` p = 0.0005 —— 同一个信号)。`pow_3(LogFloatShares)` 的 p = 0.033 配 n_with = 4,在 18 次检验下期望假阳性约 0.6 个,**不可信**。

> **结论:M 第 1 批里唯一的真来源候选是 `day_durbin_watson(Volume)`,其余都是它的搭车者、代理,或噪声。**

### 1.3 核心 A:`day_durbin_watson(Volume)` 到底在量什么(必须读源码才知道)

`dt_day.py:273-298` 的分母是 **`Σx²`,不是 `Σ(x−x̄)²`**:

```
DW_here = Σ_{t≥2}(x_t − x_{t−1})² / (Σ_t x_t² + 1e-8)
```

这不是教科书的 Durbin–Watson(教科书版去均值,取值 0–4,且与水平无关)。取期望近似:分子/T ≈ 2σ²(1−ρ₁),分母/T ≈ μ² + σ²,于是

```
DW_here ≈ 2(1 − ρ₁) · CV² / (1 + CV²),   CV = σ/μ(日内成交量的变异系数)
```

**所以 A 是「日内成交量的一阶自相关」和「日内成交量的变异系数」两件事的乘积**,不是纯自相关量。日内成交量 CV 典型在 1–3,`CV²/(1+CV²)` ∈ [0.5, 0.9],两个因子对横截面方差的贡献是同一量级。经济含义:A 高 = 成交量一根一根地蹦(孤立的大单爆发、订单流碎片化);A 低 = 平滑的 U 形量。

**这正是「真来源 vs 代理」必须拆开的地方**:CV 这一半是文献里已知的横截面特征(成交量变异系数定价),自相关那一半才是新东西。拆法见 §4.2 的 1–4 号。

**A 的两个具体风险(都要在相关度表上验,不是用来挡的理由,是研究风险):**

1. **薄成交股在 DW ≈ 2 处堆积。** 若某股一天只有一根非零量的 bar,分子 ≈ 2x²、分母 ≈ x²,DW → 2(上界)。所以次新股、准停牌、ST 这类票会挤在截面顶端形成平台与大量并列。纯多头书取的是顶部十分位 —— **A 的多头腿可能主要由「几乎不交易的票」构成**。规则 §4 明说并列按列序打破不是可挡项,但这会直接决定样本外能不能活。
2. **流动性染色。** CV 与流动性相关。控制里有流动性及其平方、三次方,线性/U/S 形暴露会被去掉,但 A 是个比值而已知族 `cross_mean(day_std(Amt), 30)` 是个水平量,两者不是同一个东西 —— 这点要靠相关度表定。E 位要求核心与每个控制 |ρ| < 0.8,A 的风险点就在流动性这一列。

### 1.4 核心 D:`ts_med(day_skew(Volume), 30)` —— 同一个经济量的慢变版本

- 单独:`day_skew(Volume)` 均值差 **+0.21**(n=18,p 0.066)。
- 包上 30 日中位数后:**+0.58**(n=15,p 0.014)。
- **代理必要性:`ts_med(·, 30)` 这一层贡献 +0.37。**

同一个模式在另一支上重复:`day_ar1_coefficient(Vwap)` +0.27 → `ts_med(…, 30)` +0.37(+0.10)。**两处都是「30 日中位数平滑让共性变好」**,方向一致。读数:起作用的是**持续的股票特征**,不是当天的事件。

但 D 和 A 在经济上是**同一族**:偏度量「少数几根 bar 吃掉大部分成交量」(爆发性的不对称),DW 量「bar 到 bar 的粗糙度」。两个都是成交量爆发性。D 不该当成独立的第二个来源,而该当成「A 的慢变、尺度无关版本」。

**由此得到本轮最便宜、先验最高的一个缺口:表里有 `ts_med(day_first(Volume),30)`、`ts_med(day_skew(Volume),30)`、`ts_med(day_ar1_coefficient(Vwap),30)`,却没有 `ts_med(day_durbin_watson(Volume), 30)`。** 而且 `loc.md` 标题写「前 20」却只排出 18 行 —— 说明 n ≥ 4 的子树全集就是这 18 个,所以这个写法在 95 个候选里最多出现 3 次,大概率 0 次。GP 把 `ts_med(…,30)` 套在了三个弱部件上,唯独没套在最强的那个上。

### 1.5 B / C / E:cross_cov 模板是结构性空洞,是 A 的搭车者

`cross_cov(x, y, d)`(`dt_cross.py:188`,axis=0 = 日轴)是**每只股票自己的两条日序列在滚动 d 天上的协方差**。

**(a) 代理必要性:套上 cross_cov 不但没帮忙,还更差。**

| 结构 | 均值差 | 它的 DW 腿单独 | 差 |
|---|---|---|---|
| B = `cross_cov(pow_2_5(pow_2_5(day_durbin_watson(Volume))), ts_med(day_first(Volume), 30), 15)` | +0.72 (n=4) | +0.73 (n=8) | **−0.01** |
| C = `cross_cov(pow_2_5(day_durbin_watson(Volume)), ts_med(day_skew(Volume), 30), 15)` | +0.62 (n=10) | +0.71 (n=44) | **−0.09** |

**没有任何一个组合超过光秃秃的 `day_durbin_watson(Volume)`(+0.76)。** 按共性这把尺子,这批里最好的写法就是不加任何东西的 A。

**(b) B 的第二条腿是死的。** `day_first(Volume)` 单独 **−0.07**(n=9,p 0.60),`ts_med(day_first(Volume), 30)` **−0.02**(n=8)。B 的 +0.72 全部来自 DW 腿。

**(c) 窗口敏感性:唯一的一对窗口对照直接把它打掉。**

- `cross_cov(pow_2_5(day_durbin_watson(Volume)), ts_med(day_ar1_coefficient(Vwap), 30), 15)` → **+0.55**(n=5,p 0.205)
- 同一结构 `…, 60)` → **+0.00**(n=6,p 0.360)

窗口 15 → 60 把效应从 +0.55 打到 0。**这个模板不耐窗口。**

**(d) 为什么它结构上就是空的(算子层面的理由)。** y 腿是 30 日滚动中位数,是条慢变、台阶式的序列;拿它在 15 天窗口里算协方差,窗内它几乎是常数(相邻 15 天的 30 日中位数窗口重叠一半以上),窗内方差极小,只在中位数换序统计量时跳一下。于是 `cross_cov(快, 30日中位数, 15)` 基本上在量「这 15 天里有没有恰好发生一次中位数跳变」。按规则 §4 这算不算「定义坏掉」要审计员定,但作为研究判断:**B、C、E 不值得花 E 位。**

**(e) 还有尺度污染。** 协方差不是归一化量:`cov ∝ σ_x σ_y ρ_xy`,而 y = `ts_med(day_first(Volume),30)` 的 σ_y 与该股成交量水平成正比(量纲 1e5–1e7)。所以 B 的截面排序里混进了一大块**成交量水平**(= 流动性/市值)。`pow_05` 包在外面是单调的,救不了。**B 实质上是「流动性 × DW」的代理。** 想要干净的版本就用 `cross_corr`(`dt_cross.py:193`,同一个 `rolling_pair_reduce` 的 `"corr"`)。

**(f) `pow_2_5(pow_2_5(·))` 在 cov 里的真实作用。** DW ∈ (0, 2],`DW^6.25`:0.5 → 0.013,2 → 76。不溢出(所以不是 §4 的数值伪影),但窗内只有 DW > 1 的那几天还剩可观的数值 —— 协方差被少数几天支配,变成了「大 DW 日有没有撞上高成交量日」的巧合探测器。这解释了 `pow_2_5` 为什么会在 cov 结构里被选中(它在那里**不是**单调无用层),也说明它换来的是极小的有效样本。

### 1.6 其余各行

- **F** `ts_med(day_ar1_coefficient(Vwap), 30)` +0.37(p 0.144)、**H** `day_ar1_coefficient(Vwap)` +0.27(p 0.263):方向与 A 一致(价格路径的自相关 = 日内趋势/反转),但都不显著。是**第三梯队的备用**,本轮不值得占位。
- **G** `day_sum(Vwap)` +0.33(n=6,p 0.412):`day_sum` 在 `SIGN_KEEPING_OPS` 里,对非负价格就是「均价 × bar 数」。bar 数由当日有效分钟数决定(停牌/半日)。这更像是**价格水平 + 数据完整度**的混合,不是机制。不显著,忽略。
- **I** `day_skew(Volume)` +0.21:见 §1.4,是 D 的未平滑版。
- **J / K** `ts_med(day_first(Volume), 30)` −0.02、`day_first(Volume)` −0.07:**负的,烂部件**。

### 1.7 §4 三类陷阱逐条过

| 陷阱 | 判断 |
|---|---|
| **前视** | 没有。`day_*` 都是当日 bar 内的归约,`ts_med` / `cross_*` 只向过去滚动(`rolling_windows(..., axis=0)`)。已知族控制本身用的就是 `day_std(Amt)`,同一形状。 |
| **数值伪影** | A:**局部有**,见 §1.3 风险 1(薄成交股堆在 DW ≈ 2,产生平台和并列)。DW 自身有 `denominator > 1e-8` 门和常数行返回 NaN,不会爆点。`DW^6.25` 不溢出。B 的协方差量纲 ~1e6,float32 内无妨。若自己写除法要小心:`common.py:168` 的 `div` 是裸 `torch.divide`,**没有 eps 保护** —— 所以 §4.2 里不要写 `div(…, day_var(Volume))`(常数量日 → 爆点),要写 `day_durbin_watson(in_demean(Volume))` 复用 DW 自己的保护。 |
| **定义坏掉** | B / C / E:**接近**。见 §1.5(d),y 腿在 15 天窗内近乎常数,结果主要由中位数跳变决定;暖机期 30 + 15 ≈ 45 天。够不够格挡由审计员定,研究上已足够判它们不值得投入。 |

### 1.8 真来源 vs 代理:一句话总表

| 记号 | 表达式 | 判定 |
|---|---|---|
| **A** | `day_durbin_watson(Volume)` | **唯一的真来源候选**;但它自身是 (1−ρ₁) 与 CV² 的乘积,还要再拆一层才知道真来源是哪一半 |
| **D** | `ts_med(day_skew(Volume), 30)` | 与 A **同族**(成交量爆发性)的慢变版;`ts_med` 层是真起作用的部件(+0.37) |
| **S** | `pow_3(LogFloatShares)` | **纯代理**:奇次幂是单调的 → 秩等同 `LogFloatShares`,而 `LogFloatCap = LogFloatShares + log(价格)` 就是控制之一。n=4,18 次检验下不可信 |
| **B** | `cross_cov(pow_2_5(pow_2_5(day_durbin_watson(Volume))), ts_med(day_first(Volume), 30), 15)` | **搭车者**:全部效应来自 DW 腿,第二条腿单独为负,协方差层贡献 −0.01,且被成交量水平染色 |
| **C** | `cross_cov(pow_2_5(day_durbin_watson(Volume)), ts_med(day_skew(Volume), 30), 15)` | **搭车者 + 自我重复**:两条腿量的是同一件事(爆发性),协方差层贡献 **−0.09** |
| **E** | 同 C 但 y 腿是 `ts_med(day_ar1_coefficient(Vwap), 30)` | **不稳**:窗口 15 → 60 效应归零 |
| F / H | `ts_med(day_ar1_coefficient(Vwap), 30)` / `day_ar1_coefficient(Vwap)` | 弱,不显著,备用 |
| G | `day_sum(Vwap)` | 价格水平 + 当日 bar 数的混合,不显著 |
| J / K | `ts_med(day_first(Volume), 30)` / `day_first(Volume)` | **负** |

## 2. 烂部件(适合做 R 的材料)

按「代理必要性 ≤ 0 或换掉反而更好」排:

1. **`pow_05` / `pow_3` / `pow_2_5` 的根部包装** —— 必要性恒等于 0(规则 §1:单调变换同分)。表里第 5、8、11 行与它们的被包装体逐位同分,实测确认。**在 cov 内部的 `pow_2_5` 不属于此列**(那里它是真的非单调作用,见 §1.5(f)),但也只换来几天的有效样本。
2. **`day_first(Volume)` / `ts_med(day_first(Volume), 30)`** —— 单独 −0.07 / −0.02,是 B 里那条死腿。**替换它**(换成 `day_skew` 或 `day_kurt` 版本)或**整条去掉**。
3. **`cross_cov(…, 15)` 这一层本身** —— B 上代理必要性 −0.01、C 上 **−0.09**:去掉协方差层、直接用 DW 腿反而更好。替换方案:`cross_corr`(去尺度污染)或干脆删层。
4. **`cross_cov` 的窗口 60** —— +0.55 → +0.00。本来就该留在 15 附近;这条是现成的「窗口加倍就崩」的证据。
5. **`pow_2_5(pow_2_5(·))` 的第二层** —— DW^6.25 让协方差只剩几天有效样本。R 变体:剥到一层、剥到零层。
6. **`day_sum(Vwap)`** —— 含当日 bar 数,是数据完整度的混合物,不显著。该换成 `day_mean(Vwap)`(与 bar 数无关)。

**但必须提醒 PI 一件事:规则 §2 的 R 是「对快照里某个 head 给出去掉或替换部件的变体」。本轮 heads = 0,严格读下来 R 没有合法靶子,16 个 R 变体这一轮用不出去。** 如果流水线允许以非 head 为底(R 本来就是「直接评估」,不经 GP),那上面 1–6 条就是替换清单,而更该先花掉的是 §4.2 的充分性测量 —— 本轮最缺的那一栏。两种读法都请 PI 定,我这边把两份清单都给齐。

## 3. 之前的任务

**本轮是第 1 轮,没有之前的任务。** 核对过:`loc.json` 的 `missions_before: []`、`heads: []`、`ablation: []`、`r_candidates: []`、`replacements_in_force: 0`、`paid: 0`;`s801/` 下只有 `r1/`,没有 `notebook.md`、`missions_final.yaml`、`audit_record.json`、`R_prev.json`。所以:

- **E**:还没有在任何核心上试过任何外围,没有产出 heads。
- **N**:还没有结果。
- **R**:还没有替换与收录。
- **审计员**:还没有挡过任何东西。
- **上一轮笔记的预测**:没有。

为了让第 2 轮能核对,我把本轮的可证伪预测写在 §4.5。

## 4. 本轮候选

### 4.1 值得深挖的核心(2 个 + 1 个备用)

#### 核心 1(强烈推荐):`day_durbin_watson(Volume)` —— **用光秃秃这一版,不要带 pow 包装**

证据:均值差 +0.76,p **0.0002**(18 次检验里唯一过 Bonferroni 的),n_with 46/95。

**挑裸版的理由(关键):** `pow_2_5(day_durbin_watson(Volume))` 的 n_with = 44,而含 `pow_2_5(DW)` 的候选必然含 `DW` —— 44 ⊆ 46,**所以 95 个候选里只有 2 个用了不带 `pow_2_5` 的裸 DW**。把这 2 个反推出来:(46 × 0.9101 − 44 × 0.9206)/2 → 均值 **−0.68**,比那 44 个包装版的 −0.92 还好(n=2,只能当指示)。**GP 几乎没试过裸核心。** 若核心取 `pow_2_5(pow_2_5(day_durbin_watson(Volume)))`,每个候选都被迫带上 DW^6.25,而一旦 GP 在外面加个单调根,整棵树就退回成 A —— 等于用 96 次付费评估重测一遍 A。

**这个核心周围已经见过的外围写法(E 规则要求外围不得与已见过的相同,这些都要避开):**

- 单调根部包装:`pow_2_5(·)`、`pow_2_5(pow_2_5(·))`、`pow_05(·)`、`pow_3(pow_05(·))`
- 协方差模板:`cross_cov(·, ts_med(Z, 30), 15)` 与 `…, 60)`,其中 Z ∈ {`day_first(Volume)`、`day_skew(Volume)`、`day_ar1_coefficient(Vwap)`}
- 以上两类的任意叠加

**换句话说,这批 46 个外围其实是一个想法(「pow 包装 + 跟某个 30 日中位数做 15 天协方差」)被反复重新发现。** 整个 n ≥ 4 的子树全集只有 18 个,这批的多样性低到极点 —— 这就是 95 个候选 0 个 head 的直接原因。

**没被碰过、值得当种子的外围方向:**

1. **股票自身时序上的归一化**(最推荐)。A 的截面水平被流动性和 bar 数染色,但「今天的 DW 相对这只股票自己过去 20/60 天」把股票级污染消掉,把它从**水平**变成**事件/变化**。控制只能去掉对流动性水平的线性/U/S 形暴露,去不掉股内变化 —— 这是残差尺子天然留给我们的空间。写法:`ts_rank(day_durbin_watson(Volume), 20|60)`、`ts_zscore` / `in_quantile` 类、`sub(day_durbin_watson(Volume), ts_med(day_durbin_watson(Volume), 20))`。
2. **平滑成持续特征**:`ts_med(day_durbin_watson(Volume), 30)`(§1.4 论证的最高先验缺口)、`cross_mean(day_durbin_watson(Volume), 5|20)`。
3. **与未被控制的那几个日频叶子交互**:控制只有流动性、波动、20 日反转、已知族、`LogFloatCap`。**`LimitWidth`、`BoardCode`、`ListAge` 完全没被控制,而且 M 的整批里一次都没出现过**(18 行里只有 `LogFloatShares` 一个日频叶子)。
4. **用 `cross_corr` 替掉 `cross_cov`**,把尺度污染去掉后再看协方差模板还剩多少。

**审计风险**:E 位要求核心与每个控制 |ρ| < 0.8。A 的风险列是**流动性**(CV 那一半)和**已知族** `cross_mean(day_std(Amt), 30)`。我的判断是过得去 —— 已知族是个水平量(元),A 是个无量纲比值 —— 但这要相关度表说话,不是我说话。

#### 核心 2(推荐):`ts_med(day_skew(Volume), 30)`

证据:均值差 +0.58,p 0.014,n_with 15;而且 `ts_med(·, 30)` 这层的代理必要性 +0.37(对比 `day_skew(Volume)` 的 +0.21)—— **这是本轮唯一一处「某个部件确实在做事」的证据**。

**已见过的外围**:只当过协方差的 y 腿(`cross_cov(pow_2_5(day_durbin_watson(Volume)), ·, 15)`),以及外面的 `pow_05` / `pow_3` 包装。**它从没当过主角。**

**没碰过的方向**:当主信号配价格侧外围;中位数窗口 10 / 60;把 `ts_med` 换成 `cross_mean` / `ts_quantile_q75`(爆发性的尾部而非中位);`day_kurt` 版本。

**先决条件(请 PI 在相关度表上先看一眼)**:D 与已知族 `cross_mean(day_std(Amt), 30)` 都是「30 日平均的日内交易活动离散度」。规则 §1 写明与已知族 |ρ| ≥ 0.5 判不合格。我的判断是过得去(偏度是无量纲三阶矩,`day_std(Amt)` 是元为单位的水平量),但**如果这一列 ≥ 0.5,核心 2 作废**,换核心 3。

#### 核心 3(备用,只在核心 2 被相关度表打掉时用):`ts_med(day_ar1_coefficient(Vwap), 30)`

+0.37,p 0.144(不显著),n_with 22。好处是它在**价格**侧而不是成交量侧,与 A / D 的机制不同族;坏处是不显著。`ts_med` 层只贡献 +0.10。不显著 → 不建议主动占位。

#### 明确不推荐做 E 核心的

- `pow_3(LogFloatShares)`:单调 → 秩等同市值控制。**预测它会被审计员的自动划线(与控制 |ρ| ≥ 0.8)直接划掉**,规则 §3 的创新度也只能打 1。
- B / C / E 三个 cross_cov 整体:协方差层代理必要性 ≤ 0、窗口不稳、y 腿窗内近常数、尺度污染。
- 任何带根部 `pow_05` / `pow_3` / `pow_2_5` 的核心:白绑一层恒等式。

### 4.2 R 目标(按价值排;**heads = 0,见 §2 末尾的合法性提醒**)

最上面 4 条不是「去烂部件」,是**把本轮空着的「充分性」一栏填上** —— 这是本轮性价比最高的付费评估,也是区分「真来源 vs 代理」的决定性实验:

| # | 变体 | 要回答什么 |
|---|---|---|
| 1 | `day_durbin_watson(Volume)` | **裸核心单独值多少**。整个第 1 轮最该先买的一个数 |
| 2 | `day_durbin_watson(in_demean(Volume))` | **去掉 CV 那一半**。`in_demean`(`dt_in.py:188`)逐日内去均值,使 DW 的分母变成 Σ(x−x̄)²,**正好是教科书 DW ≈ 2(1−ρ₁)**,纯自相关、无量纲;还复用了 DW 自己的 1e-8 保护与常数行 NaN(**不要写 `div(…, day_var(Volume))`,`div` 没有 eps**) |
| 3 | `div(day_std(Volume), day_mean(Volume))` | **只留 CV 那一半**。分母是正的成交量水平,除法在这里是安全的 |
| 4 | `day_ar1_coefficient(Volume)` | 干净的 ρ₁(把 `Vwap` 换成 `Volume`,表里只有 Vwap 版) |
| | | **2、3 的结果决定 A 是不是真来源**:若 3 行 2 不行 → A 其实是已知的成交量变异系数,是代理;若 2 行 → 日内订单流自相关,是新东西 |
| 5 | `ts_med(day_durbin_watson(Volume), 30)` | §1.4 的最高先验缺口(GP 把 `ts_med(…,30)` 套在三个弱部件上,漏了最强的) |
| 6 | 同上,窗口 5 / 60 | 窗口减半加倍 |
| 7 | `cross_corr(day_durbin_watson(Volume), ts_med(day_skew(Volume), 30), 15)` | 把 C 的尺度污染去掉 |
| 8 | `cross_cov(day_durbin_watson(Volume), ts_med(day_skew(Volume), 30), 15)` | 把 C 的 `pow_2_5` 剥掉 |
| 9 | B 的死腿替换:`ts_med(day_first(Volume), 30)` → `ts_med(day_kurt(Volume), 30)` | 换掉必要性为负的部件 |
| 10 | `ts_med(day_skew(Volume), 30)` 裸测 + 窗口 10 / 60 | 核心 2 的充分性与窗口 |
| 11 | `day_durbin_watson(Amt)` | 同类字段(`SWAP` 表里 `Volume → Amt`,`c05_locate.py:59`) |

**关于第 11 条,一个省算力的提醒:`Volume ↔ Amt` 在日内形状统计上几乎是恒等的。** 日内 `Amt_t ≈ P_t × V_t`,而日内价格只摆动百分之几,成交量却摆动几倍 —— 所以 `day_durbin_watson(Amt) ≈ day_durbin_watson(Volume)`、`day_skew(Amt) ≈ day_skew(Volume)`。**这一族的「换同类字段」敏感性测试结构上就是空的**(我预测 ρ > 0.9),最多买 1 个当对照,不要买一组。这一族真正有意义的「同类变化」是**归一化轴**(§4.1 方向 1),不是字段。若 `Ret` 叶子可用,`day_durbin_watson(Ret)` 才是真的换了经济内容(日内收益粗糙度 ≈ 已实现方差类,大概率被波动控制吃掉 —— 这本身也是个有用的否定结果)。

### 4.3 N 的灵感(2 个)

**N-1:把 A 拆成三个部件,各自当因子(机制实验,不是数字游戏)。**
DW_here ≈ 2(1−ρ₁)·CV²/(1+CV²) 把两件经济上不同的事乘在了一起。种子就是 §4.2 的 1–4 号,再加它们的时序归一化版本与 30 日平滑版本。**这个 N 的价值在于它无论哪个方向出结果都有信息**:若 CV 腿赢,A 就是已知特征的代理,整条线可以早点放弃;若自相关腿赢,我们就拿到了一个控制集里没有的机制,后两轮全部押它。合理度上它有源码级的机制推导,不是「说不清为什么」。

**N-2:用未被控制的制度维度(`LimitWidth` / `BoardCode` / `ListAge`)去条件化成交量爆发性。**
5 个控制是流动性、波动、20 日反转、已知族、`LogFloatCap` —— **`LimitWidth`、`BoardCode`、`ListAge` 一个都不在里面**,而 M 的整批 95 个候选里这三个叶子一次都没出现过(18 行里唯一的日频叶子是 `LogFloatShares`)。A 股的涨跌停宽度本身就在截断成交量形态(触板日的量形是被制度削掉的),上市年龄决定了换手的量级。这是一整片既没被控制、也没被 GP 碰过的空地。它同时还能治 §1.3 的风险 1:`ListAge` / `LimitWidth` 正是「薄成交次新股堆在 DW 顶端」这件事的条件变量。

规则 §2 要求 3 轮里至少 1 个 N 位过审计。**N-1 的机制最硬,建议本轮就上 N-1**(配 1 个 E 位在核心 1 上);N-2 留第 2 轮,等文献回来再定写法。

### 4.4 建议的本轮配置

- **E 位**:核心 1 = `day_durbin_watson(Volume)`(裸版),种子全部走 §4.1 的方向 1–4,避开那 46 个已见外围。
- **N 位**:N-1(拆 A)。
- **R**:若合法则按 §4.2 的 1–11 排;**若严格按「R 必须打在 head 上」则本轮 R 为空**,请把这 16 个额度的意图并进 N-1 的种子里(1–4 号正是 N-1 的种子)。
- 核心 1 整个实验至多 2 个 E 位,本轮用掉 1 个,给第 2 / 3 轮留 1 个。

### 4.5 可核对的预测(留给第 2 轮打分)

1. 相关度表上 `pow_3(LogFloatShares)` 与市值控制 |ρ| ≥ 0.8,被自动划掉。(信心高)
2. `day_durbin_watson(Volume)` 与流动性控制 |ρ| 落在 0.3–0.7,< 0.8,E 核心过审计。(信心中)
3. `ts_med(day_durbin_watson(Volume), 30)` 的 score 高于裸 `day_durbin_watson(Volume)`。(信心中,依据是 `ts_med(…,30)` 两处 +0.37 / +0.10 的一致方向)
4. B、C 这两个 cross_cov 的 score **不超过**它们各自的裸 DW 腿。(信心中高)
5. 裸 `day_durbin_watson(Volume)` 的 score 在 (−0.6, +0.4),即明显好于档案均值 −1.30,但单独过不了 +0.50 的线。(信心中)
6. `day_durbin_watson(Amt)` 与 `day_durbin_watson(Volume)` 的 |ρ| > 0.9,字段交换几乎是恒等操作。(信心高)
7. 本轮若不动归一化轴,只在 cross_cov 模板内继续长,96 次评估仍然 0 个 head。(信心中高)

## 5. 文献题目(交给文献员,≤ 4)

**题目 1 —— 对准核心 1 的机制(日内成交量的一阶自相关 / 粗糙度)**
文献里对「日内成交量序列的自相关、持续性、bar 到 bar 的粗糙度」这类结构做过哪些处理:怎么构造(Durbin–Watson / 一阶自相关 / 方差比)、怎么归一化(去均值?除以水平?股内时序标准化?)、横截面上与预期收益是什么方向的关系、作者怎么处理薄成交股在统计量上界处堆积的问题?
*中文关键词*:日内成交量自相关、成交量持续性、订单流自相关、成交量序列相关、分钟成交量形态、Durbin-Watson 统计量 因子
*English*:intraday volume autocorrelation, order flow autocorrelation, volume persistence, serial correlation of trading volume, Durbin–Watson statistic as a stock characteristic, volume clustering, trade arrival clustering

**题目 2 —— 对准 §4.2 的 1–4 号(决定 A 是真来源还是代理)**
文献里「成交量的变异系数 / 换手率波动 / 成交量不确定性」作为横截面特征被怎么定价?已有结论的方向与强度如何,是否在控制了规模、流动性、波动之后还在?有没有把「成交量水平的波动」与「成交量的自相关结构」分开检验过的工作?
*中文关键词*:成交量变异系数、换手率波动、成交量不确定性、交易活跃度与预期收益、成交量波动定价
*English*:coefficient of variation of trading volume, volatility of liquidity, volume uncertainty, trading activity and expected stock returns, turnover volatility and the cross-section of returns

**题目 3 —— 对准核心 2 与 E 的外围写法(爆发性怎么度量、怎么归一化)**
文献里怎么度量「日内成交量的爆发性 / 块状化」(偏度、峰度、大单占比、赫芬达尔集中度),以及把这类日频统计量变成**持续股票特征**时用的是哪种时间聚合(滚动均值、滚动中位数、股内 z 分数、时序分位),窗口一般取多长?有没有直接比较过「截面水平」和「股内时序归一化」两种口径的样本外差异?
*中文关键词*:日内成交量偏度、成交量集中度、大单成交占比、日内成交量分布、滚动中位数 平滑 因子、股内时序标准化
*English*:intraday volume skewness, volume concentration / Herfindahl of intraday volume, lumpy volume, block trade share, within-stock time-series normalization vs cross-sectional level, rolling median smoothing of daily characteristics

**题目 4 —— 对准 N-2(未被控制的制度维度)**
A 股的涨跌停制度、板块(主板 / 创业板 / 科创板 / ST)和上市年龄怎么改变成交量的日内形态?文献里把「价格涨跌幅限制」「上市年龄」当条件变量或当控制变量时是怎么做的,有没有用它们来剔除 / 条件化次新股与准停牌股造成的量形异常?
*中文关键词*:涨跌停板、价格涨跌幅限制、磁吸效应、ST 股、上市年龄、次新股、创业板 20% 涨跌幅、停牌复牌 成交量
*English*:price limits and trading volume, magnet effect, limit hit China A-shares, listing age and turnover, newly listed stocks volume patterns, daily price limit regime China, ST stocks

---

### 附:本文引用到的源码位置(供核对)

- `AlphaCube/src/alphacube/operators/dt_day.py:273-298` —— `day_durbin_watson`,分母是 `Σx²`(非去均值),有 `>1e-8` 门与常数行 NaN
- `AlphaCube/src/alphacube/operators/common.py:209` —— `pow_` 带符号幂;`:168` —— `div` 裸除法,**无 eps**
- `AlphaCube/src/alphacube/operators/dt_cross.py:188,193` —— `cross_cov` / `cross_corr`(axis=0 = 日轴)
- `AlphaCube/src/alphacube/operators/dt_in.py:188` —— `in_demean`
- `AlphaCube/src/alphacube/mining/rankban.py:1-19` —— 秩禁令:单调重写与原式的相关恰好 1.0
- `partura/steer.py:162-178` —— `NONNEG_OPS`(**不含 `day_durbin_watson`**)、`MONOTONE_ANY`、`MONOTONE_NONNEG`
- `partura/runner.py:168` —— 方向只在 train 切片上拟合;`partura/books.py:133-148` —— 半衰期在 `fit` 切片上拟合
- `scripts/c05_locate.py:294-324` —— 共性的定义(单边 Mann–Whitney,`n ≥ 4` 且 `n ≤ 0.7×95 = 66.5`);`:326-394` —— 消融**只对 heads** 做;`:59` —— `SWAP` 字段交换表
