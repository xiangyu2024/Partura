# 结构解剖:种子 802,B 组,第 3 轮(最后一轮)

读的东西:`r3/loc.md`、`r3/loc.json`(含每个变体的 coverage / distinct / sign / hl / rho_known / necessity)、`r3/R_prev.json`(第 2 轮 16 次 R 直接评估的全部结果);
`r2/loc.md`、`r2/loc.json`、`r2/analysis.md`、`r2/lit.md`、`r2/missions.yaml`、`r2/R_prev.json`、`r1/*`、`notebook.md`、`PLAN.md`(含修订 1–12);
代码:`scripts/c05_locate.py`(奖励上下文 `85-118`、评估与 rho_known `118-148`、替换链 `63-71` 与 `158-164`、R 判定 `176-199`、共性 `204-234`、卡 `295-310`)、
`scripts/c05_round.py`(库与 R 替换 `40-48`、家族控制 `220-229`、`seen` 来自全部存档 `216`)、`scripts/idea_search.py`(控制集 `177-186`、核心/外围/骨架判定 `285-335`)、
`partura/ops_ext.py`(`cross_valid_count` `288`、`day_wmean` `109`、`_tail_mean` `300`、`day_topw_mean` `635`)、
`alphacube/operators/{dt_day,dt_cross,common}.py`(`day_cov` `213`、`day_kurt` `124`、`_kurt` `418`、`_stddev` `406`、`rolling_pair_reduce` `621`)、
`alphacube/mining/clustering.py:29`(`skeleton_key`)。

## 0. 四句话

1. **第 3 批给了本实验最硬的一条机制,而且它把第 2 轮我自己写错的那条改对了。** M3 的三个 head 全部是「**日度日内统计量的短窗二阶矩**」:
   `cross_cov(cross_cov(day_max(Ret), day_cov(Ret, Ret), 3), cross_cov(day_max(Ret), day_cov(Ret, Ret), 3), 3)`(+1.34)、
   `cross_cov(day_max(Ret), day_cov(Ret, Ret), 30)`(+0.90)、`cross_cov(day_wmean(Ret, Ret), day_wmean(Ret, Ret), 5)`(+0.67)。
   把它们和 M2 的 `pow_2(pow_2_5(day_durbin_watson(High)))` 放到一起,一个 Jensen 分解就把两批统一了:**凸变换 + EMA ≈ 水平 × 该股自己近期的相对离散度**,
   而控制集里只有**水平**(`cross_mean(day_std(Ret), 20)`)。alpha 全在「不稳定」那一项里,不在水平里。
   第 2 轮我把这件事读成「软最大值」并押 `cross_max` 复现 —— **第 2 轮的 R 把它否了**(`cross_max(day_durbin_watson(High), 20)` = **−0.0573**),我错了;正确的读法是幂平均 / 离散度,不是极值。
2. **E 这个任务位在本种子上两轮共花 176 次付费评估、0 个过线、0 个 head;N 共花 155 次、14 个过线、7 个 head(含库里第 1 和第 5)。**
   第 2 轮 E 的失败不能再用「家族控制太重」解释:这次家族只有 1 个 head,`c05_no_core` 仍然拒了 2209 次,84 个候选最高 **+0.2529**。
   原因是结构性的:「必须原样含核心」把 GP 的变异/交叉几乎全部拒掉,E 的产出 ≈ 手写种子;而 N 的两次产出都是「我给原料、GP 给处理」(第 1 轮我给 `day_mean(in_logchg(Volume, 60))`、GP 加了 `cross_mean(·, 20)`;
   第 2 轮我给 `day_kurt(Ret)` 这个原料、GP 加了 `div(·, cross_valid_count(day_std(Ret), 60))`)。PLAN §2.5 只要求「3 轮里至少 1 个 N 位」,已经满足两次,**所以最后一轮两个位都给 N 是合规的**。
3. **两笔已经付过钱、现在还躺在地上的收益。** (a) 第 2 轮 R 里 `inv(ts_decay_linear(inv(pow_1_5(inv(sigmoid(ts_regbeta(…, 200))))), 40))` = **+1.3271** 和
   `inv(ts_decay_linear(sigmoid(ts_regbeta(…, 200)), 40))` = **+1.3016**,各比原 head 高 +0.18 / +0.34,却因 `rho_head` 0.381 / 0.382 < 0.5 **没能替换、被丢掉**;
   `ts_reg_tvalue(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100)` = **+1.1434**(`rho_known` −0.089)连续两轮被同一条 ρ 门槛丢掉。
   前两个的骨架(窗口被抽象掉)与库里的 head 相同,**结构上进不了库**,只能记为局限;第三个骨架不同、ρ 也低,**第 3 轮必须把它写成 N 的种子**,这是全轮最便宜的一个 head。
   (b) 第 1、2 轮 E 的 176 个候选是在「控制里多加了核心家族」的奖励下评的分,而定位工具的 R 评估用的是**普通 `long_neutral`**(`c05_locate.py:108-110`,没有 `neutral-extra`),
   所以 **R 可以把 E 的最佳候选在普通奖励下重评一次** —— 第 1 轮 E 的头名 `mul(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), day_centroid(Volume))`
   在 5 个家族控制下 train −0.1432 / **valid +1.6350**,它在普通奖励下的分数**从来没有人看过**。
4. **一个事实性问题要记下来:第 2 轮 R 唯一的那次替换没有生效。** `c05_locate.py:63-71` 的 `replacements()` 用「被替换的原 head 表达式」做键,而 `c05_lib.heads()` 永远给出 M 的**原始**表达式;
   第 1 轮已经把 `ts_regbeta` 窗口 50 换成 100,第 2 轮的替换键是**窗口 100 那一版**,于是永远匹配不上。
   r3 的 head 表里这个 head 仍是 **窗口 100、score +1.1555**,而 `replacements_in_force` 写的是 4(它数的是字典条目,不是生效条数)。
   窗口 200 的 +1.3933 只作为**额外库成员**进了禁令(`c05_round.py:46`),没有进 head 表。
   而 R 的请求必须命名快照里的 head(`c05_locate.py:179-181` 否则直接报错),所以**这条链从任务文件这一侧修不了**,照修订 10 的办法记为局限。

---

## 1. alpha 的来源

### 1.0 先把这一轮定位工具的偏差讲清楚

**(a) 存档里 72% 是我自己的任务。** 458 个已评分候选 = M1 的 77 + M2 的 31 + M3 的 **19** + 我的四次任务 92 + 81 + 84 + 74 = **331(72.3%)**。
第 2 轮 §1.0 指出的「共性表混了不同奖励口径」这一轮**完全复现**,而且更干净地暴露了出来:

| 子树 | 均值差 | n_with | 读法 |
|---|---|---|---|
| `inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)))` | **+1.6374**,p 0.0002 | 8 | 纯 M1 残留;`inv` 这个外壳 E 从来没用过,所以 n_with 三轮不变(第 1 轮 +1.49 / 第 2 轮 +1.49 / 本轮 +1.64) |
| `sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))`(只差一层 `inv`) | 掉出前 40(第 2 轮是 **−0.774**) | 47+ | 同一条信息,只因为被我第 1 轮当了 E 核心,就从 +1.3 翻到 −0.8 |

**同一份信息、只差一个单调外壳,均值差相差 2.4 以上 —— 这在真实信号上不可能发生,它只能是污染。** 这一轮同样不可读的还有:
`cross_valid_count(day_std(Ret), 60)`(+1.5639,n=4)、`day_kurt(Ret)`(+1.3583,n=10)、`cross_tail_mean_q75(day_std(Ret), 20)`(+0.4774,n=5)、`cross_mean(day_std(Ret), 20)`(+0.0714,n=7)、
`div(day_last(Amt), day_sum(Volume))`(+1.4084,n=4)、`day_last(Amt)`(+1.1255,n=9)—— **它们全部来自我自己任务的种子谱系,是「我押了它、它赢了」,不是独立证据。**
真正只来自 M、可以当独立证据读的行:`cross_quantile_q25(LogFloatShares, 241)` 一族、`day_cov(Ret, Ret)`(+0.6220,p 0.0133,n=31)、`day_max(Ret)`(+0.4284,p 0.0918,n=17)、
`day_durbin_watson(High)`(+0.6647,p 0.0208,n=20)、`day_durbin_watson(Vwap)`(+0.8848,n=12)、`day_max(Volume)`(+0.9116,n=19)、`day_gini(Volume)`(+0.7211,n=9)、`day_min(High)` / `day_min(Ret)` / `day_sum(*)` 那几行。

**(b) `rho_known` 看不见 EMA。** `c05_locate.py:143-144`:`rho_known = corr(zrank(sign × 原始面板), kz)`,**在 EMA 与残差化之前**算的。
所以它对任何严格单调变换**恒等不变** —— 这就是为什么 `day_std(Ret)` 与 `day_cov(Ret, Ret)` 的 `rho_known` 是 ∓0.2094(同一个绝对值)、
四个 `day_durbin_watson(High)` 幂次的 `rho_known` 第 2 轮全是 0.1329。GP 自己的门槛用的是**交易口径**的 `rho_known_traded`(`idea_search.py:490`),是另一个、更严的量。
**结论:R / 拆解表里的 `rho_known` 低,不能直接当「交易信号与已知族无关」的证明。** 下面凡是引它,我都只用它原来的含义(原始截面秩的相关度)。

**(c) 机械核心卡这一轮前两张是真东西,但和 B 完全重合。** 卡 #1 `day_kurt(Ret)`(自身 +0.9669)、卡 #2 `cross_cov(day_max(Ret), day_cov(Ret, Ret), 3)`(自身 +0.8473)——
这是三轮里第一次机械卡的头部不是单调包装或股价代理。代价是 B 与 B0 本轮在 E 核心上可能撞车(第 2 轮核心 A 不在卡上,是 B 独有的)。卡 #3–#8、#11–#14 仍是 S 的 `inv` 包装与 `LogFloatShares` 一族(见 1.6)。

### 1.1 真来源(一,最硬):日度日内统计量的**短窗不稳定**,不是它的水平

这是本轮唯一一条「能把两批 M 的产出用一个机制串起来」的发现,而且它纠正了我第 2 轮的误读。

**先把 M3 的三个 head 翻译成人话(源码 + 代数)**

- `day_cov(x, y)`(`dt_day.py:213`)是当日分钟上 x 与 y 的**总体**协方差,所以 `day_cov(Ret, Ret)` ≡ 分钟收益的总体方差 ≡ `day_std(Ret)²` = **当日已实现方差(分钟口径)**。
- `cross_cov(a, b, d)`(`dt_cross.py:188` → `common.py:621-637`)是沿日轴的 d 日滚动协方差(除以 d);因此 `cross_cov(x, x, d)` ≡ **x 的 d 日滚动方差**。
  特例:`cross_cov(x, x, 2) = (x_t − x_{t−1})²/4`,即**逐日变化的平方**。
- `day_wmean(x, w)`(`ops_ext.py:109`)= Σ(x·|w|)/Σ|w|,所以 `day_wmean(Ret, Ret)` = Σ(Ret·|Ret|)/Σ|Ret| = **[上行平方和 − 下行平方和] / 总绝对变动** ——
  即**有符号已实现半方差的不对称度**(对 Ret 的乘性缩放是一次齐次,不是尺度不变)。

于是:

| head | 等价含义 | score | train | valid | rho_known |
|---|---|---|---|---|---|
| `cross_cov(cross_cov(day_max(Ret), day_cov(Ret, Ret), 3), cross_cov(day_max(Ret), day_cov(Ret, Ret), 3), 3)` | Var₃[ Cov₃(当日最大分钟收益, 当日已实现方差) ] | **+1.3407** | +1.3407 | +3.2617 | +0.10 |
| `cross_cov(day_max(Ret), day_cov(Ret, Ret), 30)` | Cov₃₀(MAX, 已实现方差) | +0.8972 | +0.8972 | +1.8138 | — |
| `cross_cov(day_wmean(Ret, Ret), day_wmean(Ret, Ret), 5)` | Var₅[ 有符号半方差不对称度 ] | +0.6678 | +0.6678 | +1.3585 | — |

三个都是 sign −1(**做多「低」的一端 = 做多近期自身波动结构稳定的票**)。

**充分性 / 必要性(本轮 27 次拆解里的 7 次给了这一棵)**

| 行 | 数字 | 读法 |
|---|---|---|
| `cross_cov(day_max(Ret), day_cov(Ret, Ret), 3)` 单独 | **+0.8473**(train 0.8473 / valid 2.0513),coverage 0.9993、distinct 0.998、`rho_known` **+0.0545** | 单独就远过发现线,而且是全库所有强子树里**原始截面秩与已知族最不相关**的一个 |
| `day_max(Ret)` 单独 | **−0.2739**(valid +1.3640) | 原料本身不行 |
| `day_cov(Ret, Ret)` 单独 | **−1.5501**(valid +0.1273) | 原料本身更不行 |
| `day_std(Ret)` 单独 | **−2.5564**(valid −2.4001) | 波动水平在控制里,剩下的是负的 |
| 两个 knockout(把一侧换成 `day_max(Ret)`) | 都是 **−1.9644**,必要性 **+3.3051** | 「两侧都必须是那个协方差」是硬的 |
| 外层窗口 3→2 | **+1.4126**(valid 3.1994) | 比 head 高 +0.072(不到替换线) |
| 外层窗口 3→6 | +1.2198 | 比 head 低 |

**所以这一族的 alpha 既不在 MAX 里、也不在已实现方差里,而在「它们在两三天里一起动了多少」里。** 窗口 2 最好 ⇒ 真正起作用的时间尺度是**逐日变化**,不是月度。

**再看 M2 那个 head,用 Jensen 分解把两批统一起来(这是本轮的核心论证)**

管线是 `signal_t = zrank(EMA_hl(sign × x_t))`(`steer.py:632-645`),**先按日 EMA、再截面取秩**。对正的 x 与 p > 1,写 x_s = m_t(1+ε_s),m_t 是 EMA 水平:

```
EMA(x^p) = m_t^p · EMA((1+ε)^p) ≈ m_t^p · (1 + p(p−1)/2 · CV_t²)
EMA(x^p)^{1/p} ≈ m_t · (1 + (p−1)/2 · CV_t²)
```

`u ↦ u^{1/p}` 单调,截面取秩对它不变,所以

> **用 x^p 代替 x,等于把信号从「水平 m_t」换成「水平 × 一个随该股自身近期相对离散度 CV_t 单调上升的因子」,权重随 (p−1) 增长。**
> 同一天的截面排序在 p 变化时**完全不变**(x > 0 ⇒ 幂是严格单调的),唯一变的是 EMA 这一步 —— 所以 x^p 与 x 的分数差**只能**归因于那个离散度项。

六条证据,两条来自本轮拆解,四条来自 M2 与第 2 轮 R:

| 检验 | 数字 | 对假设的意义 |
|---|---|---|
| `day_durbin_watson(High)` 的幂次剂量—反应(第 2 轮拆解) | x¹ **−1.1711** → x² +0.2653 → x^2.5 +0.7240 → x⁵ **+1.4497**,四行 sign / hl / distinct / `rho_known` 全同 | 水平项值 −1.17,离散度项值 **+2.62**;单调、增量递减(饱和) |
| `day_std(Ret)` → `day_cov(Ret, Ret)`(本轮拆解,**独立的第二个原料**) | p = 1 → 2:**−2.5564 → −1.5501**,`\|rho_known\|` 两行都是 0.2094 | 同一条机制、同样的方向,值 **+1.01**。这是本轮新买到的交叉证据 |
| 先取截面秩再求五次方(第 2 轮 R) | `pow_2(pow_2_5(cs_rank(day_durbin_watson(High))))` = **−0.9127** 对 x⁵ 的 +1.4497 | 截面秩把重尾压成均匀分布 ⇒ CV 几乎没了 ⇒ 收益从 +2.62 塌到 +0.26。**离散度必须用原始量级算**,这也否了「只是市场压力日的截面位置」那个纯截面读法的强版本 |
| 显式单日极值(第 2 轮 R) | `cross_max(day_durbin_watson(High), 20)` = **−0.0573**(hl 5) | **我第 2 轮「软最大值」的读法错了。** 单日次序统计量太噪 |
| 显式稳健极值(第 2 轮 R) | `cross_tail_mean_q75(day_durbin_watson(High), 20)` = **+0.1801**(hl 0) | 把「进入统计量的天数」从 1 天 → 5 天 → 整个窗口(凸权重),分数 **−0.057 → +0.180 → +1.450**,是一条干净的剂量—反应:**要的是整个窗口的分布,不是最大那几天** |
| 显式「离散度 ÷ 水平」(第 2 轮 N 的产出,已是 head) | `div(cross_tail_mean_q75(day_std(Ret), 20), cross_mean(day_std(Ret), 20))` = **+0.6139**(valid 1.1732) | 把水平**整个除掉**之后仍然 +0.61 过线;而分母 `cross_mean(day_std(Ret), 20)` 正是控制集里那一项 ⇒ 这一项就是纯离散度 |

**它是真来源还是代理?** 和第 2 轮对 `day_durbin_watson(High)` 的判语一样,我分两句讲:

- **对这个奖励的五个控制(流动性水平、波动水平、20 日反转、已知族、`LogFloatCap`),它不是代理**:控制里只有 `cross_mean(day_std(Ret), 20)` 这个**均值口径**;
  线性投影(`neutral_basis` 对 z-rank 做 QR)张不开二阶矩;三个原料单独都是负的(−0.27 / −1.55 / −2.56),凑成二阶矩之后是 +0.85 / +1.34;`cross_cov(day_max(Ret), day_cov(Ret, Ret), 3)` 的原始 `rho_known` 只有 +0.055。
- **但它的经济内容不是新的**:「风险本身的不确定性 / 波动的波动被定价」是一个已有文献的族(见 L9)。**新的是写法**(哪个统计量、哪个窗口 —— 2 到 5 天,而不是 20 天),不是经济学。
  对 C05 的主指标来说这未必是坏事(一个稳健的已知效应用新函数形式写出来照样能贡献样本外夏普),但不能说它是新信息。
- **一个必须留的保留**:M3 的三个结构都**没有**把水平除掉(Cov₃(MAX, RV) 的量纲是 ret³,Var₃ 之后是 ret⁶),所以它们是「水平 × 离散度」的混合,不是纯离散度。
  纯离散度版本只在 `day_std(Ret)` 这一个原料上被验证过(+0.6139)。`day_durbin_watson(High)` 的纯离散度版本**从来没评过** —— 这是本轮 R 最该买的一个答案(见 4.2 第 2、3 条)。

### 1.2 真来源(二):日内收益分布的**形状** —— `day_kurt(Ret)`

```
核心:  day_kurt(Ret)                                          自身 +0.9669(train 0.9669 / valid 1.5370)
head:  div(day_kurt(Ret), cross_valid_count(day_std(Ret), 60)) +1.2330(train 1.2330 / valid 1.2402),sign −1,hl 20
```

- `day_kurt`(`dt_day.py:124` → `common.py:418`)= 当日 241 根分钟收益的**总体超额峰度** mean(d⁴)/var² − 3。
  **它对 Ret 的任何乘性缩放严格不变** ⇒ 在数学上不可能是波动水平、市值、价格或流动性的另一种写法。sign −1 = **做多日内收益不被几根尖峰支配的票**。
- 证据:coverage 0.9973、distinct 1.0000、`rho_known` **−0.0854**,自身单独 +0.9669 就远过发现线;它在共性表上的 +1.3583(p 0.0011,n=10)**不算独立证据**(来自我自己第 2 轮 N 的种子谱系,见 1.0)。
- 它和 1.1 节是**互补的两个维度**:1.1 是同一个统计量在**时间**上的二阶矩,1.2 是**同一天内**分布形状的四阶矩。两者都在控制集之外,而且 `rho_known` 都很低。
- **风险**:日内峰度在分钟数少、零成交多的票上估得很差 —— 这正好解释了 head 为什么要配一个筛子(见 1.5)。

### 1.3 真来源(三)已经定案:对数口径的日内成交量时间分布(核心 A)

第 2 轮 R 把两个开放问题都答了,这里只记结论,不再重复推导:

| 问题 | 第 2 轮 R 的答案 |
|---|---|
| 它是不是流动性的另一种写法? | `cs_bucket_zscore(cross_mean(day_mean(in_logchg(Volume, 60)), 20), cross_mean(day_sum(Amt), 30))` = **+1.4370**(train 1.8025 / valid 1.4370),原始 `rho_known` 从 −0.3881 掉到 **−0.0242**。在 30 日成交额十分位**内部**重算 z 分数,train 甚至更高 ⇒ **不是流动性代理**(代数论证升级成了实测;按 1.0(b),这句话只覆盖原始截面秩)。`rho_head` 0.9702 ⇒ 是同一个信号,不能当第二个 head |
| 核内分钟窗口 60 是不是最优? | `cross_mean(day_mean(in_logchg(Volume, 120)), 20)` = **+1.3127**(`rho_head` 0.866)< +1.6680 ⇒ **平滑之后 60 胜 120**。注意这和第 1 轮在**未平滑的水平口径**上「60 ≈ 120」(0.537 / 0.558)不一致 —— 又是一次「同类替换应该差不多」的失败 |
| M2 的排除式筛子搬到它身上灵不灵? | `cs_last_high10(neg(cross_mean(day_mean(in_logchg(Volume, 60)), 20)), day_max(Volume))` = train **+1.0874** / valid **−0.9502** ⇒ **不灵,而且是崩**。筛子不是通用处理(与我第 2 轮预测 #4 的方向一致,幅度比我押的糟得多) |
| 水平口径 head 该不该被对数口径替换? | `rho_head` **0.3929 < 0.5** ⇒ 不替换。**两者是两份信息**(ρ 0.39),库里两个都留 —— 这本身是第 2 轮想要的那个结论 |

**第 2 轮「留给第 3 轮」的条件计划在这里结清**:核心 A 的 E 位 0 个 head,而且 84 个候选最高 +0.2529(同轴的时间结构那一整组 ≤ 0.25,含「20 对 240 偏离」)⇒
按笔记写死的条件,**核心 A 的信息是个股的持久特征,不再给它 E 位**;R 继续花在它的窗口 / 归一化上。

### 1.4 S 一族:窗口剂量—反应到 200 见顶、400 掉头;三个被 ρ 门槛扔掉的近乎正交因子

`ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), w)` 的窗口序列现在四点齐了(同一棵 `inv(pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(·)))))))` 上):

```
w = 50      +0.8315
w = 100     +1.1555
w = 200     +1.3933   (valid 2.4174,rho_head 0.7525,rho_known −0.2015)
w = 400     +0.9223   (valid 2.3323,rho_head 0.5817)
```

**200 是顶,400 掉头。** 我第 2 轮押「400 落在 +1.25 ~ +1.40(饱和)」,方向(不再改善)对、数值错(它跌了 0.47)。
第 1 轮文献那条「约 40 个交易日的记忆边界」在这里仍然是错的:有效窗口大约是 **200 天**。

**三个被 R 的 ρ ≥ 0.5 门槛扔掉的高分变体(都是已经付过钱的数字):**

| 表达式 | score | train / valid | `rho_head` | `rho_known` | 为什么丢了 |
|---|---|---|---|---|---|
| `inv(ts_decay_linear(inv(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 200))))), 40))` | **+1.3271** | 1.3271 / 2.1661 | 0.3812 | −0.2032 | 比原 head(+1.1438)高 +0.18,ρ < 0.5 不算「同一个东西」 |
| `inv(ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 200)), 40))` | **+1.3016** | 1.3016 / 2.2159 | 0.3824 | −0.2042 | 比原 head(+0.9608)高 +0.34,同上 |
| `ts_reg_tvalue(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100)` | **+1.1434** | 1.1434 / 1.9503 | 0.3630(第 1 轮对另一个 head 是 0.0761) | −0.0891 | 连续两轮被同一条门槛丢掉 |

这就是 PLAN 修订 10 第 (2) 条那个「R 只替换、不收录」的洞,在本种子上已经吃掉了三个 +1.1 以上、与 S 的交易信号只有 0.08 ~ 0.38 相关的因子。
**能不能救?一个一个查库禁令**(`idea_search.py:300-306`:骨架用 `skeleton_key` 并把 `@窗口` 抹掉,字段与常数也抽象成 `F`/`DF`;另加 |ρ| ≥ 0.7 的秩禁令):

- 前两个:抹掉窗口之后,它们的骨架与库里 `inv(ts_decay_linear(inv(pow_1_5(inv(sigmoid(ts_regbeta(…, 50)))))), 40)` / `inv(ts_decay_linear(sigmoid(ts_regbeta(…, 50)), 40))` **完全相同** ⇒
  当种子会被 `c05_skeleton` 拒掉。**结构上不可达,只能记为局限。**
- `sigmoid(ts_regbeta(…, 100))`(第 1 轮 R 的 +1.0413):库里有 R 换进来的 `pow_1_5(inv(sigmoid(ts_regbeta(…, 100))))`,而 `pow_1_5(inv(x)) = x^{−1.5}` 对正的 x 是**严格单调**的 ⇒ 原始日度秩相关 |ρ| = 1 ⇒ 必被秩禁令拒。**也不可达。**(第 2 轮笔记的判断(i)是对的。)
- **`ts_reg_tvalue(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100)` 可达**:骨架是 `O:ts_reg_tvalue(O:day_flat_run_max(F),O:day_durbin_watson(F))`,库里没有;
  与两个 S head 的交易信号 ρ 已测为 0.076 / 0.363,远低于 0.7(秩禁令按**原始**日度秩算,数值可能更高一些,这是唯一的风险)。**它必须进第 3 轮 N 的种子。**

### 1.5 一个被误读的部件:`cross_valid_count(·, 60)` 是**筛子**,不是分母

`cross_valid_count(x, d)`(`ops_ext.py:288`)= 最近 d 个交易日里 x 有限的**天数**,整数 0..d、永不 NaN。它在拆解里**连门槛都没过**(distinct 0.0117、gate false)—— 因为绝大多数票都顶在 60。
所以 `div(day_kurt(Ret), cross_valid_count(day_std(Ret), 60))`:

- 对历史完整的票,分母是常数 60 ⇒ 除以它是**纯缩放**,EMA 线性、截面取秩不变 ⇒ 与 `day_kurt(Ret)` **完全同一个信号**;
- 对最近停过牌 / 刚复牌的票,分母变小 ⇒ 数值被放大。日内超额峰度在 A 股几乎总是正的大数,放大之后被推到截面的高端,而 sign = −1(做多低端)⇒ **这些票被赶出多头书**。

**所以这一层是一个「数据质量 / 近期停牌」筛子,不是一个统计量。** 它和奖励自己的剔除条件不重复:奖励用的是 `cross_valid_count(day_last(Close), 241) < 0.9 × min(241, t)`(`idea_search.py:166-168`),
而 60 日的计数能抓到「241 天里够 90%、但最近 60 天内停过牌」的票。

证据:`day_kurt(Ret)` 单独 +0.9669 → head +1.2330,**筛子值 +0.266**;窗口 30 / 60 / 120 = **1.2298 / 1.2330 / 1.2648**(平的,说明不是窗口过拟合);
GP 自己还长出了 `div(day_kurt(Ret), cross_valid_count(day_kurt(Ret), 60))` = +1.2054(把计数算在 `day_kurt` 上,数字几乎一样)⇒ **起作用的是计数,不是被计数的东西**。
拆解里那个 knockout `div(day_kurt(Ret), day_std(Ret))` = +0.2078(必要性 +1.0252)**不能用来证明筛子必要**:它把分母换成了 `day_std(Ret)`,等于把波动水平重新乘回去,是另一件事。

**这是本轮第二条「处理方式」级别的发现,而且它比 M2 的 `cs_last_*` 筛子可信**:`cs_last_*` 搬到非股价代理的 y 上直接崩(1.3 节),
而 `div(·, cross_valid_count(·, 60))` 的作用机制与 y 无关(它只动那几十只有缺口的票)。但第 1、2 轮的系统性偏差 (ii)(「同类处理可以互换」)连错了三轮,
所以**只在两个 head 上各试一次,不要铺开**(4.2 第 13、14 条)。

### 1.6 代理 / 搭车:股价水平一簇(本轮新增两次敲除,结论不变)

本轮拆解把这一簇又照了两棵,结论和第 2 轮一字不改,只补两条新数字:

```
+1.0887  cs_last_high10(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3), day_gini(Volume))
           子树单独:cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3) = +0.5558
                     cross_quantile_q25(LogFloatShares, 241)                       = +0.5578   ← 两个数到三位小数一样
           knockout cross_decay_linear   → +1.0840,必要性 +0.0047   ← 死重
           knockout cross_quantile_q25   → +1.0233,必要性 +0.0654   ← 近乎死重
           day_gini(Volume) 单独          → −3.6673(rho_known +0.6742,已越过不合格线)
           swap Volume→Amt               → +1.0698(−0.019)         ← 几乎不变
           窗口 3→2 / 3→6                 → +1.0954 / +1.0738        ← 平
+1.0696  cs_last_low20(cross_quantile_q25(LogFloatShares, 241), day_durbin_watson(Vwap))
           knockout cross_quantile_q25   → +0.8178,必要性 +0.2518
           swap Vwap→Close               → +0.6621(−0.408)         ← 这里 Vwap 真的要紧
           窗口 241→120 / →482            → +1.0088 / +0.9807
```

两条值得记的新东西:

1. **筛子的 `Volume→Amt` 敏感性是 `day_max` 独有的,不是筛子的性质。** 第 2 轮在 +1.2940 那棵上 `day_max(Volume) → day_max(Amt)` 从 +1.294 崩到 **−0.1713**;
   本轮在 +1.0887 这棵上 `day_gini(Volume) → day_gini(Amt)` 只差 **−0.019**。所以「筛子只在股数口径下有效」那句话要收窄成「`day_max` 这个统计量只在股数口径下携带低价信息」(`day_gini` 是份额型、本来就尺度不变)。
2. **这一簇仍然不值得投 E / N**:它一阶上是名义股价水平的反面(`LogFloatCap = LogFloatShares + log(价格)`,而控制里有 `LogFloatCap`),是已知的廉价异象;
   库里已经有 6 个写法,PLAN §3 的贪心去重会按 ρ ≥ 0.7 砍掉大部分;而且它的内层零件必要性 0.005 / 0.065,E 的机械嫁接只会在死重上浪费节点。

### 1.7 两处必须记进笔记的事实性问题

1. **第 2 轮 R 的替换没有生效(§0 第 4 句)。** r3 head 表里 `inv(pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100))))))))` 仍是 **+1.1555**;
   窗口 200 的 +1.3933 只作为额外库成员进了禁令。原因是 `replacements()` 用「被替换的原表达式」做键,而链式替换(第 1 轮 50→100、第 2 轮 100→200)的第二环永远匹配不上 `c05_lib.heads()` 给出的原始表达式。
   **不要再花一次评估去重做它**:即使第 3 轮的 R 再提一次,产生的替换键还是窗口 100,同样接不上链。
2. **秩禁令的拒绝次数读不出来,连续两轮。** 证据文件里只有 `c05_no_core` / `c05_periphery_seen` / `c05_skeleton` / `mutation_refused` 四个计数;
   第 1 轮用 `cs_bucket_rank(S, day_last(Close))` 做的探针、第 2 轮「至少 2 个种子会被秩禁令拒掉」的预测,**两次都无法对账**。写任务时不要再设计「靠拒绝计数回答的问题」。

---

## 2. 烂部件(必要性 ≤ 0,或换掉反而更好)—— R 的料

| head | 部件 | 证据 | 判语 |
|---|---|---|---|
| +1.0887 `cs_last_high10(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3), day_gini(Volume))` | `cross_decay_linear(·, 3)` 与 `cross_quantile_q25(·, 241)` | 必要性 **+0.0047 / +0.0654**;两个内层子树单独 +0.5558 / +0.5578(到三位小数相同) | **两个都是死重**。单个敲掉 gain ≈ 0,两个一起敲掉从没试过;只值 1 次「保险丝」评估(把 head 缩短 3 个节点,顺便再确认「整条内链是一个单调变量」) |
| +1.4497 `pow_2(pow_2_5(day_durbin_watson(High)))` | 无可去的部件,但**整条凸聚合写法未必最优** | 唯一 knockout 必要性 +1.1844;第 2 轮 R 四种显式写法全败(`cross_max` −0.0573、`cross_tail_mean_q75` +0.1801、`cross_mean(x⁵, 20)` +0.9973、`cs_rank` 版 −0.9127) | **「极值」这条路已死,别再花钱**。真正没试过的是 1.1 节的**显式离散度**:`cross_stddev(·, 20)` 与 `div(cross_stddev, cross_mean)` |
| +1.2330 `div(day_kurt(Ret), cross_valid_count(day_std(Ret), 60))` | 分母不是部件、是筛子(1.5 节) | 窗口 30 / 60 / 120 = 1.2298 / 1.2330 / 1.2648(平);`day_kurt` 单独 +0.9669 | **没有可去的烂部件**。改善轴是筛子的窗口 / 定义,以及「箱式平滑 + EMA」(核心 A 上这一步值 +1.12) |
| +1.3407 双层 `cross_cov` | 无 | 两个 knockout 必要性 **+3.3051**;外层窗口 3→2 = +1.4126(+0.072,不到 +0.1) | **没有烂部件**,但两处窗口都偏长。只值 1 次(注意第 1 轮偏差 (i):叠加两个已证实方向会变差) |
| +1.1438 `inv(ts_decay_linear(inv(pow_1_5(inv(sigmoid(ts_regbeta(…, 50))))), 40))` / +0.9608 同族 | `ts_regbeta` 窗口 50 | 窗口 200 版 **+1.3271 / +1.3016**,各高 +0.18 / +0.34 | **确认是烂部件,但修不了**:`rho_head` 0.381 / 0.382 < 0.5 不能替换,骨架与库里的 head 相同不能当种子(1.4 节)。记为局限 |
| +0.8324 `sigmoid(ts_regbeta(day_flat_run_max(Vwap), sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 50))` | 整个外层 `ts_regbeta(day_flat_run_max(Vwap), ·, 50)` | 第 1 轮 R 剥干净得到 `sigmoid(ts_regbeta(…, 100))` = +1.0413,但 `rho_head` 0.1166 被挡 | 死重确认。它是 23 个 head 里**唯一 valid(0.8324)< train(1.0860)**的一个,也是库里最弱的 S 包装 ⇒ **替换门槛只有 +0.9324,是放「E 候选在普通奖励下重评」的最佳挂点**(4.2 第 6、7 条) |
| +0.7233 `cross_mean(div(div(day_last(Amt), day_sum(Volume)), day_sum(High)), 20)` | `day_sum(High)` 这个分母(量纲不干净) | 第 2 轮 R:干净的收盘分钟股数占比 `cross_mean(div(day_last(Volume), day_sum(Volume)), 20)` = **+0.3868**;对数版 **−0.0309**;两者 `rho_head` 只有 0.284 / 0.270 | **我第 2 轮「它 ≈ 收盘分钟成交占比」的读法不完整。** 代数:`day_last(Amt)/day_sum(Volume)/day_sum(High)` ≈ (V_last/V_day)/241 × (P_last/P̄) ⇒ 它是**占比 × 收盘价对当日均价之比**。干净占比只值 0.387 ⇒ 那个价格因子在出力。1 次评估就能把它单独拿出来 |
| +0.5085 `cross_mean(cross_mean(div(day_last(Amt), day_sum(Amt)), 20), 20)` 与 +0.5245 同族 | 第二层 `cross_mean`(两个 head 的 hl 都选到 0) | — | **不要再花评估**:单重平滑版 `cross_mean(div(day_last(Amt), day_sum(Amt)), 20)` **本来就是第 1 轮 N 的种子之一**,已经评过而且低于 +0.5085(否则它会是 head)。第 2 轮 §4.2 第 15 条作废 |
| +0.5370 `day_mean(neg(in_delta(Volume, 60)))` | 整个「未平滑」这件事 | 同族对数口径加 `cross_mean(·, 20)` 从 +0.5473 升到 **+1.6680**;而这个水平口径**从来没被平滑过**(第 1 轮 R 只动了核内分钟窗口 30 / 120 与份额 / Amt 口径);第 2 轮 R 已证明它与对数口径是两份信息(ρ 0.393) | **本轮期望值最高的一次 R**。风险:平滑会把原始 `rho_known` 推高(对数口径 20 日 −0.388、40 日 −0.444;水平口径混着成交量量级,第 1 轮 Amt 版已经 −0.524),有可能撞 0.5 的不合格线 |
| +0.6678 `cross_cov(day_wmean(Ret, Ret), day_wmean(Ret, Ret), 5)` | 未知 | **本轮没被拆**(每轮只拆 4 个 head),`day_wmean(Ret, Ret)` 从来没单独评过 | 1.1 节的假设在**第三个原料**(有符号半方差不对称度)上的检验点,值 2 次评估(充分性 + 窗口) |
| +0.6139 `div(cross_tail_mean_q75(day_std(Ret), 20), cross_mean(day_std(Ret), 20))` | 窗口 20 | M3 的证据说有效时间尺度是 2–5 天(窗口 2 > 3 > 6);这个 head 的窗口从来没动过 | 2 次评估,`+0.1` 替换线只有 0.7139,是本轮第二高期望值的 R |

---

## 3. 之前的任务

### 3.1 E 两轮的总账:176 次付费评估,0 个过线,0 个 head

| 任务 | 核心 | 家族 | 评分 | 过线 | heads | 采样计数 | 最好的候选 |
|---|---|---|---|---|---|---|---|
| `c05s802Br1a_Ea` | `sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))` | **5 个** | 92 | 0 | 0 | `c05_no_core` **3012**,`c05_periphery_seen` 11,`mutation_refused` 6 | `mul(S, day_centroid(Volume))` train −0.1432 / **valid +1.6350** |
| `c05s802Br2a_Ea` | `day_mean(in_logchg(Volume, 60))` | **1 个** | 84 | 0 | 0 | `c05_no_core` **2209**,`c05_periphery_seen` 9,`c05_skeleton` 1,`mutation_refused` 6 | `cross_corr(day_mean(in_logchg(Volume, 60)), day_mean(Low), 60)` **+0.2529**(valid 0.5516) |

**第 1 轮我把失败归因于「家族控制太重」(当时 5 个 head 把 S 的信息吃干净了)。第 2 轮把家族降到 1 个,结果一样是 0,而且最高分只有 +0.25。所以那个解释是不够的。真正的原因:**

1. **「必须原样含核心」把 GP 关掉了。** 两轮 `c05_no_core` 拒了 3012 / 2209 次才凑出 92 / 84 次评分。`--graft-fill 32` 只管初代;之后的变异/交叉绝大多数改动了核心就被拒。
   **E 的 96 次预算买到的是「我手写的 ≤16 个种子 + 机械嫁接 + 很小的扰动」**,不是一次搜索。
2. **第 2 轮 E 的前五名全是同一个形状**:`cross_corr(day_mean(in_logchg(Volume, 60)), 〈某个价格水平表达式〉, 60)`(第二个参数依次是 `day_mean(Low)`、`log(day_mean(Open))`、
   `log(log(day_mean(Open)))`、`day_open(cross_delta(Close, 3))`、`log(log(day_mean(Low)))`)—— GP 只做了一件事:把我那两个 `cross_corr` 种子的第二个参数换成各种价格水平。
   这同时说明:**在家族控制下,E 的外围里唯一有残差的是「带第二个叶子」**(第 1 轮前三名也全是 `mul(S, 第二个日内形状)`)—— 这一条两轮一致,是 E 唯一稳定的经验。
3. **对比 N**:`c05s802Br1b_Nb` 81 次评分 → 8 过线 → **5 个 head**(含全库第一 +1.6680);`c05s802Br2b_Nb` 74 次评分 → 6 过线 → **2 个 head**(+1.2330、+0.6139)。
   两次 N 的头名都是「**我给原料、GP 给处理**」:第 1 轮我的种子是裸的 `day_mean(in_logchg(Volume, 60))`,GP 加了 `cross_mean(·, 20)`;
   第 2 轮我的种子是 `cross_tail_mean_q75(day_kurt(Ret), 20)`,GP 取了原料 `day_kurt(Ret)` 换上 `div(·, cross_valid_count(day_std(Ret), 60))`。
   **E 的结构正好禁止了这件事**(核心固定 ⇒ 原料固定 ⇒ GP 只能动外围,而外围的新集合又被 SEEN 约束),所以 E 在本种子上拿不到 N 那种收益。

**给 PI 的一句话**:PLAN §2.5 的硬约束只有两条 —— 每个核心至多 2 个 E 位(不紧)、**3 轮里至少 1 个 N 位(已经用了 2 个)**。所以最后一轮两个位都给 N 是合规的;
要不要留一个 E 位是对「C05 这套架构」本身的押注,不是数据逼出来的。数据上的赔率是 **0/176 对 7/155**。

### 3.2 N 第 2 轮(`c05s802Br2b_Nb`):74 次评分,6 个过线,2 个 head

| score | 表达式 | 进 heads? | 读法 |
|---|---|---|---|
| **+1.2330** | `div(day_kurt(Ret), cross_valid_count(day_std(Ret), 60))` | ✓ | 日内超额峰度 + 近期停牌筛子(1.2、1.5 节) |
| +1.2054 | `div(day_kurt(Ret), cross_valid_count(day_kurt(Ret), 60))` | ✗(与上者 ρ ≥ 0.7) | 同一件事 |
| +1.0677 | `div(div(day_kurt(Ret), cross_valid_count(day_std(Ret), 60)), cross_valid_count(day_std(Ret), 60))` | ✗ | 同一件事 |
| +0.9669 | `day_kurt(Ret)` | ✗ | **裸原料本身就过线**;被 ρ 挡在 head 之外,但它是本轮最干净的核心候选 |
| **+0.6139** | `div(cross_tail_mean_q75(day_std(Ret), 20), cross_mean(day_std(Ret), 20))` | ✓ | 波动的尾 / 均之比 = 纯离散度(1.1 节的显式确证) |

**我第 2 轮押的那条(「最可能过线:波动的尾/均比、最大一分钟收益的尾部、封板分钟占比的 20 日最大值」)只中了第一个**,而且头名(+1.2330)完全不在我的押注清单上 ——
它来自我种子里的**原料**(`day_kurt`),处理是 GP 给的。方向(sign −1 = 做多尾部低的一端)对。
「成交量那一侧单独 < 0.5 的居多」与前五名一致(一个都没进),但不可严格对账;「至少 1 个种子被秩禁令拒掉」**又一次读不出来**(1.7 节第 2 条)。

### 3.3 第 2 轮 R(16 次)对账:又一次,错的全集中在「同类处理可以互换」

| # | 变体 | 笔记里的预测 | 实际 | 对? |
|---|---|---|---|---|
| 1 | A2 窗口 200 | +1.3933(已知),确定替换 | **+1.3933**,`rho_head` 0.7525,**replaces = true** | **对**(但替换没传到第 3 轮的 head 表,1.7 节) |
| 2 | A2 窗口 400 | 1.25–1.45;比 200 高 0.05 的概率 35% | **+0.9223** | **错**(低于区间;掉头) |
| 3 | A1 窗口 200 | 1.15–1.40;替换概率 50% | **+1.3271** 在区间内;`rho_head` 0.3812 ⇒ **未替换** | 数值**对**,替换判断错 |
| 4 | A4 窗口 200 | 0.95–1.25;替换概率 50% | **+1.3016** 高于区间;`rho_head` 0.3824 ⇒ 未替换 | **错**(比我押的好) |
| 5 | A5 窗口 200 | 0.95–1.20;≥0.987 的概率 55% | **+0.9346** | 几乎对(略低于区间下沿),≥0.987 不成立 |
| 6 | A5 → `ts_reg_tvalue(·, ·, 100)` | +1.1434 已知;ρ ≥ 0.5 概率 60%,若是则替换 | `rho_head` **0.3630** ⇒ 未替换 | **错**。走的是「t 值是另一份信息」那条分支 ⇒ 按条件计划进第 3 轮种子 |
| 7 | `cross_max(day_durbin_watson(High), 20)` | PI 0.8–1.3(低于 head);**解剖员:≥ +1.20 且 hl ∈ {0,5},概率 70%** | **−0.0573**(hl 5) | **两人都大错,我错得更重**(1.1 节已据此改读法) |
| 8 | `cross_tail_mean_q75(day_durbin_watson(High), 20)` | 0.6–1.2 | **+0.1801** | **错** |
| 9 | `cross_mean(pow_2(pow_2_5(day_durbin_watson(High))), 20)` | 1.30–1.60;替换概率 30% | **+0.9973**(`rho_head` **0.9847**) | **错**(低于区间)。顺带一条有用的旁证:ρ = 0.985 的两个信号分数能差 0.45 ⇒ **0.3–0.4 的分数差在高相关变体之间不算证据** |
| 10 | `pow_2(pow_2_5(cs_rank(day_durbin_watson(High))))` | 0.2–0.9,比原始 x⁵ 低 ≥ 0.4;「若 ≥ 1.3 则我的读法错」 | **−0.9127** | 数值低于区间,但**方向性押注(需要原始量级)成立** |
| 11 | 水平口径 → 对数口径 head | ρ 0.35–0.6;替换概率 45% | `rho_head` **0.3929** | **对** |
| 12 | 核心 A 核内窗口 120 | 1.45–1.75;替换概率 15% | **+1.3127** | 略低于区间 |
| 13 | 流动性十分位内 z 分数 | 1.40–1.70;替换概率 10% | **+1.4370**(`rho_known` −0.0242) | **对** |
| 14 | 排除式筛子搬到核心 A | 1.50–1.90;替换概率 30% | train +1.0874 / valid **−0.9502** | **大错** |
| 15 | 收盘分钟股数占比(干净) | 0.40–0.80 | **+0.3868** | 略低于区间 |
| 16 | 同上取对数 | 0.50–0.90;15/16 至少一个替换概率 30% | **−0.0309** | **大错** |

**总账:16 条里判对约 5 条(1、3、11、13,外加 10 的方向),判错约 10 条。**
**第三轮同一种系统性偏差**:7、8、9、14、16 全是「这个处理在那边有效,搬过来应该也有效」。
第 2 轮我已经写下「一次只动一个部件、不要把同类替换写进任务假设」,**然后自己在第 7 条上犯了同样的错**(把 `cross_max` 当成 `x⁵ + EMA` 的等价写法)。
**第 3 轮的规矩**:凡是「移植一个处理」的变体,整轮不超过 **2 个**,而且必须写明失败时学到什么。

三轮下来真正**能移植**的处理只有两个:(a) 把 `ts_regbeta` 的窗口拉长(50→100→200,到 400 失效);(b) 在一个日度形状统计量上加 `cross_mean(·, 20)` 箱式平滑
—— 而 (b) 换到核内分钟窗口(120)和收盘占比上也失败了。

### 3.4 第 2 轮「留给第 3 轮的条件计划」逐条结清

| 条件 | 实际 | 结论 |
|---|---|---|
| E(核心 A)有 head → 给核心 A 第二个 E 位;没有且「20 对 240 偏离」< 0 → 核心 A 是持久特征,不再给 E | 0 个 head,84 个候选最高 +0.2529,同轴时间结构整组 ≤ 0.25(含那条偏离) | **不再给核心 A 任何 E 位**;R 继续花在它的窗口 / 归一化上 |
| N 有 head,且 R #10(截面秩五次方)≥ 1.3 → 极值聚合是个股层面的通用处理;若远低于 x⁵ → 第 3 轮的 N 改成显式的「市场压力日上的截面位置」 | N 有 2 个 head;#10 = **−0.9127**,远低于 x⁵ | 「个股自身极值」被否。但**两条替代读法里,「市场压力日的截面位置」也被否**(`cs_rank` 已经去掉了市场水平、分数塌了;若是纯市场压力暴露,秩版本不该塌)。正确的第三条路是 1.1 节的**离散度** |
| R #6 的 ρ < 0.5 → t@100 是 S 之外的一份信息,第 3 轮放进种子 | ρ = 0.3630 < 0.5 | **条件成立:`ts_reg_tvalue(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100)` 进第 3 轮 N 的种子**(1.4 节已核过库禁令) |
| R #14 筛子在核心 A 上 ≥ 1.77 → 排除式筛子是通用处理,考虑以它为 N | valid −0.9502 | **条件不成立,这条路关掉**(但 1.5 节那个**另一种**筛子是新的、机制不同) |

---

## 4. 本轮候选

### 4.1 值得深挖的核心(≤3 个,按推荐度)

> 先提醒两件对 E 位全局有效的事:(i) 外围 = 候选的算子名多重集减去核心的算子名多重集之后**仍为正的那些名字构成的集合**(`idea_search.py:312-315`),
> SEEN 来自**全部 458 个存档候选**里含该核心的那些,所以下面列的都是**下界**(我只看得到 heads 与我自己任务的前五名);
> (ii) 骨架禁令抹掉窗口**并且**把字段/常数抽象成 `F`/`DF`(`clustering.py:29-38`),所以「只换窗口 / 只换字段」的写法一律与库里同名 head 撞骨架。

#### 核心 α(首选)

```
cross_cov(day_max(Ret), day_cov(Ret, Ret), 3)
```

- **凭据**:自身 **+0.8473**(train 0.8473 / valid 2.0513),coverage 0.9993、distinct 0.998、原始 `rho_known` **+0.0545**(全库所有强子树里最低);
  所在 head +1.3407(valid 3.2617),两个 knockout 必要性 **+3.3051**;外层窗口 2 / 3 / 6 = +1.4126 / +1.3407 / +1.2198;
  三个原料单独是 −0.2739 / −1.5501 / −2.5564 ⇒ **alpha 在二阶矩里,不在原料里**(1.1 节)。
- **它是 M3 的产出,不是我的** ⇒ 共性 / 拆解上的数字没有被我的任务污染(1.0 节),这一轮只有这一族和 `LogFloatShares` 一族满足这一点。
- **家族控制 = 1 个 head**:库里原样含这个子树(窗口 3)的只有双层那个 +1.3407;`cross_cov(day_max(Ret), day_cov(Ret, Ret), 30)` 窗口不同、key 不同,不进家族。
- **已经见过的外围(下界)**:

  | 来源 | 外围算子名集合 |
  |---|---|
  | 永久禁(核心自身) | ∅ |
  | head +1.3407 `cross_cov(cross_cov(·,·,3), cross_cov(·,·,3), 3)` | {`cross_cov`, `day_max`, `day_cov`} |

  **只有这一个集合被封掉,外围空间几乎全开。** 但骨架禁令额外封住两样东西:`O:cross_cov(O:day_max(F),O:day_cov(F,F))`(= 裸核心,**任何**窗口、任何字段)
  和 `O:cross_cov(O:cross_cov(O:day_max(F),O:day_cov(F,F)),O:cross_cov(O:day_max(F),O:day_cov(F,F)))`(= head 的骨架)⇒ **候选必须把核心包进别的东西里**,GP 想不出新东西时会空转。
- **没试过、而且是另一条轴的外围**(给 PI 写种子用;下笔前请用 `partura.ac_plugin.partura_operator_names()` 对词表):
  1. **把水平除掉**:`div(core, cross_mean(core, 20))`、`div(core, cross_mean(day_cov(Ret, Ret), 20))` —— 1.1 节最后那条保留(M3 的结构是「水平 × 离散度」的混合)直接变成种子;
  2. **换聚合长度而不是换窗口**:`cross_stddev(core, 20)`、`cross_mean(core, 5)` 配第二个名字,避开骨架禁令;
  3. **条件化 / 分组**:`cs_bucket_zscore(core, LimitWidth)` / `cs_bucket_zscore(core, BoardCode)` / `cs_bucket_zscore(core, ListAge)` ——
     「涨跌停带宽窄的票 / 创业板 / 新股里,波动结构不稳更值钱吗」是真的新信息;优先 `cs_bucket_zscore`(改量纲)而不是 `cs_bucket_rank`(桶内秩保留大部分截面排序,容易撞秩禁令);
  4. **1.5 节那个筛子**:`div(core, cross_valid_count(day_std(Ret), 60))`(两次移植试验的配额要和 R 协调,别重复买);
  5. **带第二个叶子的交互**(两轮 E 唯一稳定有残差的一类):`mul` / `div` / `cross_corr` 配 `day_kurt(Ret)`、`day_gini(Volume)`、`day_zero_ratio(Ret)`、`day_wmean(Ret, Ret)`、`day_signed_ratio(Ret, Amt)`。
- **风险**:(a) 量纲是 ret⁶,float32 的动态范围要留神(窗口 3 上 coverage 0.9993,没问题;再叠凸变换可能下溢);
  (b) E 两轮 0/176,先验本来就低;(c) 它是机械卡 #2 ⇒ B0 很可能用同一个核心,B 的差别只剩种子与外围的选择。

#### 核心 β(次选)

```
day_kurt(Ret)
```

- **凭据**:自身 **+0.9669**(train 0.9669 / valid 1.5370),coverage 0.9973、distinct 1.0000、`rho_known` −0.0854;
  **对 Ret 的乘性缩放严格不变** ⇒ 在数学上不可能是波动 / 规模 / 价格 / 流动性的代理(这一点比核心 α 更硬);所在 head +1.2330,而 head 比它多的那一层只是个筛子(1.5 节)。
- **家族控制 = 1 个 head**(`div(day_kurt(Ret), cross_valid_count(day_std(Ret), 60))`)。
- **已经见过的外围(下界)**:

  | 来源 | 外围算子名集合 |
  |---|---|
  | 永久禁(核心自身) | ∅ |
  | head +1.2330 / 候选 `div(div(·, cvc), cvc)` | {`div`, `cross_valid_count`, `day_std`} |
  | 候选 `div(day_kurt(Ret), cross_valid_count(day_kurt(Ret), 60))` | {`div`, `day_kurt`, `cross_valid_count`} |
  | 我第 2 轮的种子 `cross_tail_mean_q75(day_kurt(Ret), 20)` | {`cross_tail_mean_q75`} |

  三个集合封掉,仍然基本全开。骨架禁令只封 `O:div(O:day_kurt(F),O:cross_valid_count(O:day_std(F)))`。
- **没试过的外围**:时间聚合(`cross_mean(·, 20)`、`cross_stddev(·, 20)`、`div(cross_stddev, cross_mean)`)、与波动水平的解耦(`div(day_kurt(Ret), day_std(Ret))` 已知 +0.2078,所以**不要再走这条**)、
  按 `LimitWidth` / `BoardCode` / `ListAge` 分桶、与 `day_skew(Ret)` / `day_wmean(Ret, Ret)` / `day_zero_ratio(Ret)` 的交互(同一天内形状的两个不同侧面)。
- **要诚实记下的两条**:(a) `day_kurt(Ret)` 是**我第 2 轮 N 的种子原料**,它在共性表上的 +1.3583 不是独立证据(1.0 节);真实证据是那次 N 的付费分数;
  (b) 它是机械卡 **#1** ⇒ B0 一定会用它,B 用它等于主动放弃本轮的核心差异。

#### 核心 γ(列出以供对照,**本轮不推荐**)

```
day_wmean(Ret, Ret)       （或整个 head div(cross_tail_mean_q75(day_std(Ret), 20), cross_mean(day_std(Ret), 20))）
```

- `day_wmean(Ret, Ret)` 的外围几乎全开(只见过 {`cross_cov`, `day_wmean`}),机制也是 1.1 节那条(所在 head 是它的 5 日滚动方差 +0.6678),
  但**它从来没有被单独评过** —— 没有充分性证据的核心不该占一个 E 位。R 能补上这个数(4.2 第 9 条),可是 R 与 GP 位在同一轮并行跑,结果赶不上本轮的决策。
- 那个 +0.6139 的 head 整体当核心(修订 3 允许)在方法论上诱人(把「离散度 ÷ 水平」这个**处理**固定住),但 E 的定义是「固定核心、变外围」,
  我们想固定的恰恰是处理、想变的是**原料** —— 和第 2 轮对 `day_durbin_watson(High)` 的判断一样,**这条发现的正确载体是 N,不是 E**。

### 4.2 R 目标(PI 从里面挑 ≤16;按期望值排)

> 规则提醒:替换需要 **score ≥ 原 head + 0.1** 且 **`rho_head` ≥ 0.5** 且 **|`rho_known`| < 0.5**(`c05_locate.py:190`);
> R 的评估用**普通 `long_neutral`**(`c05_locate.py:108-110`),与 M / N 的候选分数直接可比、与 E 的候选分数**不可比**。

**A 组:期望值最高的四条**

1. **head +0.5370 `day_mean(neg(in_delta(Volume, 60)))`** → `cross_mean(day_mean(neg(in_delta(Volume, 60))), 20)`
   依据:同族对数口径加这一层从 +0.5473 升到 +1.6680;水平口径**从来没被平滑过**;第 2 轮已证明两个口径是两份信息(ρ 0.393),所以这是在补库里最弱的那一份。风险:原始 `rho_known` 可能撞 0.5。
2. **head +1.4497 `pow_2(pow_2_5(day_durbin_watson(High)))`** → `div(cross_stddev(day_durbin_watson(High), 20), cross_mean(day_durbin_watson(High), 20))`
   1.1 节的决定性一发:把水平**整个除掉**,只留该股自己的相对离散度。若 ≥ +1.0,机制证实并且库里多一个可读的 head;若 ≈ 0,说明「水平 × 离散度」的乘积才是信号,离散度单独不行。
3. **head +1.4497** → `cross_stddev(day_durbin_watson(High), 20)`
   和第 2 条配对:不除水平的版本。两条一起才能把「水平」「离散度」「两者之积」三种读法分开。
4. **head +0.6139 `div(cross_tail_mean_q75(day_std(Ret), 20), cross_mean(day_std(Ret), 20))`** → `div(cross_stddev(day_std(Ret), 5), cross_mean(day_std(Ret), 5))`
   M3 的证据说有效时间尺度是 2–5 天;这个 head 的窗口从来没动过,替换线只有 +0.7139。

**B 组:买答案(每条都能排除一种读法)**

5. head +0.6139 → `div(cross_tail_mean_q75(day_std(Ret), 5), cross_mean(day_std(Ret), 5))`(同一处理只换窗口,和第 4 条构成「换窗口 vs 换统计量」的二维)
6. **head +0.8324(库里最弱的 S 包装,替换线只要 +0.9324)** → `mul(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), day_centroid(Volume))`
   §0 第 3 句那笔沉没资产:第 1 轮 E 的头名,在 5 个家族控制下 train −0.1432 / **valid +1.6350**,**在普通奖励下的分数从来没人看过**。
7. head +0.8324 → `mul(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), day_distinct_ratio(Volume))`(同上,第 1 轮 E 的第三名,train −0.1652 / valid +1.1937)
8. head +1.3407 → `cross_cov(cross_cov(day_max(Ret), day_cov(Ret, Ret), 2), cross_cov(day_max(Ret), day_cov(Ret, Ret), 2), 2)`
   两处窗口都到 2。**明确承认这违反「不要叠加两个已证实方向」**:外层 3→2 已知 +0.072,内层从没动过;若它低于 +1.4126,偏差 (i) 就是第四次复现。
9. head +0.6678 → `day_wmean(Ret, Ret)`(M3 第三个原料的充分性,全库唯一没评过的强 head 零件)
10. head +0.6678 → `cross_cov(day_wmean(Ret, Ret), day_wmean(Ret, Ret), 2)`(窗口 5→2;若升,1.1 节「2 天最好」在第三个原料上复现)
11. head +1.2330 → `cross_mean(day_kurt(Ret), 20)`(箱式平滑 + EMA;核心 A 上这一步值 +1.12,这是三轮里唯一两次成功移植过的处理之一)
12. head +0.7233 → `cross_mean(div(day_last(Vwap), day_mean(Vwap)), 20)`
    把藏在量纲里的价格因子单独拿出来(2 节):若它 ≥ 0.5,这个 head 其实是一个**收盘价对当日均价的漂移**因子,而不是「收盘分钟成交占比」。

**C 组:筛子的两次移植试验(整轮只做两次,3.3 节的规矩)**

13. head +1.6680 `cross_mean(day_mean(in_logchg(Volume, 60)), 20)` → `div(cross_mean(day_mean(in_logchg(Volume, 60)), 20), cross_valid_count(day_std(Ret), 60))`
14. head +1.3407 → `div(cross_cov(cross_cov(day_max(Ret), day_cov(Ret, Ret), 3), cross_cov(day_max(Ret), day_cov(Ret, Ret), 3), 3), cross_valid_count(day_std(Ret), 60))`
    失败时学到的:1.5 节那个筛子和 `day_kurt` 是配对的(峰度在有缺口的票上估得差),不是通用处理 —— 那就和 M2 的 `cs_last_*` 一样,别再投。

**D 组:保险丝 / 补缺(可选)**

15. head +1.0887 → `cs_last_high10(LogFloatShares, day_gini(Volume))`(一次敲掉两个必要性 0.005 / 0.065 的死重;预期 ≈ +1.02 ~ +1.09、不替换,但把 head 缩短 3 个节点并再确认「整条内链是一个单调变量」)
16. head +1.2330 → `div(day_kurt(Ret), cross_valid_count(day_std(Ret), 241))`(筛子窗口换成奖励自己用的 241;窗口 30/60/120 已知是平的,241 是唯一没试的那一格)
- 替补:head +1.4497 → `pow_2(pow_2_5(day_durbin_watson(Volume)))`(把凸聚合搬到非价格原料上 —— 但这属于「移植」,和第 13、14 条抢配额)
- 替补:head +0.5370 → `day_mean(in_delta(Volume, 60))`(代数保险丝,应与 +0.5370 **精确相等**;连续两轮没执行。第 1 轮 R #4 精确复现过 +1.1555,所以管线的确定性已经确认过一次,这条的优先级可以最低)

**不要再买的**:`cross_mean(div(day_last(Amt), day_sum(Amt)), 20)`(第 1 轮 N 的种子,已评过且 < +0.5085);
`cross_max` / `cross_tail_mean_q75` / `cs_rank` 在 `day_durbin_watson(High)` 上的任何新变体(第 2 轮 R 已三连否);
S 一族的窗口 400(已知 +0.9223);A2 窗口 200 的重做(1.7 节,链接不上)。

### 4.3 N 的灵感(按手上的证据排序,PI 定)

#### N1(最硬):把「**水平 → 短窗不稳定**」当成一种通用处理,铺到不同原料上

一句话假设:*这类日度日内统计量的横截面信息在它**近几天的相对离散度**里,不在它的水平里;控制集里只有水平口径的波动与流动性,线性投影张不开二阶矩,所以离散度口径必然留下残差。*
证据链见 1.1 节(两条独立的幂次剂量—反应、一条「进入统计量的天数」剂量—反应、一条秩版本的否证、一条显式比值的正证、三个 M3 的 head)。
做法:**固定处理、铺开原料**(这正是 N 位该干的事,E 位做不到)。
- 处理:`cross_stddev(x, d)`、`div(cross_stddev(x, d), cross_mean(x, d))`、`div(cross_tail_mean_q75(x, d), cross_mean(x, d))`、`cross_cov(x, y, d)`(两个相关的日度统计量配对,学 M3)、`d ∈ {2, 3, 5, 20}`。
- 原料(避开已在库里的):`day_durbin_watson(Vwap)` / `(Volume)`、`day_gini(Volume)`、`day_distinct_ratio(Volume)`、`day_zero_ratio(Ret)`、`day_at_max_ratio(Vwap)`、
  `day_skew(Ret)`、`day_signed_ratio(Ret, Amt)`、`day_centroid(Volume)`、`day_topw_mean(Ret, Volume)`、以及核心 A `day_mean(in_logchg(Volume, 60))`。
- **两条硬约束必须写进种子设计**:(i) 任何现有 head 的**严格单调改写**(例如把 `cross_cov(z, z, d)` 换成 `cross_stddev(z, d)`)原始日度秩相关 = 1,**必被秩禁令拒** ⇒
  这类诊断只能走 R(4.2 第 2、3 条),不能当种子;(ii) `O:cross_cov(O:day_max(F),O:day_cov(F,F))` 与双层版本的骨架已被封(任何字段、任何窗口),
  `O:div(O:cross_tail_mean_q75(O:day_std(F)),O:cross_mean(O:day_std(F)))` 同样被封 ⇒ 种子要换**算子形状**,不是换字段或窗口。

#### N2(最便宜):把「标准化的滚动关系统计量 + 长窗口」收进库

直接把 `ts_reg_tvalue(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100)` 写成种子(score **+1.1434** 已知、`rho_known` −0.0891、与两个 S head 的交易信号 ρ 0.076 / 0.363、骨架库里没有)——
这是三轮里唯一一个「分数已知 ≥ +1.1、与库近乎正交、库禁令挡不住」的现成因子,**连续两轮被 R 的 ρ 门槛丢掉**。
再把这个处理推广:窗口取 100 / 200(50 已证明太短:t@50 = −0.1061);把 `day_flat_run_max(Vwap)` 换成 `day_gini(Volume)` / `day_distinct_ratio(Volume)` / `day_zero_ratio(Ret)` / `day_kurt(Ret)`,
把 `day_durbin_watson(Volume)` 换成 `day_durbin_watson(High)` / `day_centroid(Volume)` / `day_wmean(Ret, Ret)`。
注意这是「换同类统计量」,三轮里失败率很高 —— 但这一条的**底座**(t@100 本身)分数已知,所以哪怕推广全败,这个 N 位也至少收一个 head。

#### N3(与 N1 互补):日内收益分布的**形状**,尺度不变口径

1.2 节的 `day_kurt(Ret)`(+0.9669,尺度不变)和 1.1 节是两个不同的维度:N1 是**时间**上的二阶矩,N3 是**同一天内**的三、四阶矩与半方差不对称。
种子:`day_skew(Ret)`、`day_kurt(Ret)` 的分桶 / 交互写法、`day_wmean(Ret, Ret)`(有符号半方差不对称度)、`div(day_wmean(Ret, Ret), day_std(Ret))`(标准化版)、
`day_topw_mean(Ret, Volume)`(最重 10% 分钟的平均收益)、`day_zero_ratio(Ret)`、以及它们的 20 日箱式平滑。
**若 PI 把 E 位给核心 β(`day_kurt(Ret)`),这一条要让给 E,免得两个位撞车**;反之若 E 给核心 α,N3 可以和 N1 共用一个位(处理不同、原料不同)。

#### N4(不推荐占位,但要记下):E 的 176 个候选在普通奖励下从来没被看过

1.0 节与 3.1 节的推论。R 已经能做两次(4.2 第 6、7 条),用一个 GP 位去系统地重评它们不划算(大部分含 S 或核心 A,会撞秩禁令);
但**如果第 6、7 条里有一个在普通奖励下 ≥ +1.0**,那说明「E 的奖励口径把 176 次评估的信息藏起来了」是一条真实的结构性损失,应该写进最终笔记,留给下一个实验。

---

## 5. 文献题目(给文献员,只能用 2023-08-08 之前发表的;接着第 1 轮的 L1–L4 与第 2 轮的 L5–L8,不重复)

**L9(对准核心 α 与 N1:把一个日频统计量聚合成横截面信号时,用水平还是用它自己的短窗不稳定度)**
把一个**日频**的风险 / 活跃度统计量(已实现波动、日内价格粗糙度、成交量集中度)聚合成横截面信号时,文献里有没有把**「它自己近期的变动 / 离散度」**与**「它的水平」**分开检验的做法,
离散度那一项在控制掉水平之后还剩多少?具体想要四件事:
(1) **怎么写离散度**:滚动标准差、变异系数(标准差 ÷ 均值)、上尾均值 ÷ 均值、逐日变化的平方、两个相关统计量的滚动协方差 —— 文献用过哪些,有没有互相比较过?
(2) **窗口**:这类「二阶」信号常用几天(2–5 天还是 20 天以上),有没有报告过**短窗(几天)胜长窗**的结果?
(3) 有没有文献明确指出**对一个正的重尾日度量取凸变换(平方、高次幂)再做移动平均**,效果上等价于把它的时间离散度混进信号(幂平均 / Jensen 项),并据此解释过因子强度?
(4) 这一族在**中国 A 股**上的证据,以及它和「彩票偏好 / 异质波动率」那一族是怎么分开的。
关键词:波动率的波动、风险的不确定性、已实现波动的波动、变异系数、二阶矩信号、日内波动不稳定、幂平均;
volatility of volatility, uncertainty about risk (unknown unknowns), vol-of-vol and the cross-section of stock returns, coefficient of variation of realized volatility, instability of realized measures,
realized volatility dispersion, power mean / Jensen term in signal aggregation, rolling covariance of daily realized measures, China A-share vol-of-vol.

**L10(对准核心 β 与 N3:日内收益分布的形状作为横截面特征)**
用高频(分钟)数据算出的**日内收益分布形状**统计量 —— 已实现峰度、已实现偏度、有符号已实现半方差之差(上行平方和减下行平方和)、跳跃成分 —— 在横截面上被怎样处理和定价?具体三件事:
(1) **标准化**:是用**尺度不变**的口径(峰度、偏度、半方差之差 ÷ 总变动)还是原始量纲?文献有没有报告过尺度不变口径能在控制掉波动水平之后仍然显著?
(2) **聚合**:日频的形状统计量要平均多少天(自相关怎样衰减),等权移动平均还是指数加权,要不要取极值 / 分位?
(3) 它和**波动水平、换手率、流动性**是怎么分开的(用什么控制变量),以及在**中国 A 股**上的证据与符号(高峰度 / 高上行不对称预测高还是低收益)。
关键词:已实现峰度、已实现偏度、有符号跳跃、已实现半方差、日内收益分布、尺度不变矩、特质偏度;
realized kurtosis cross-section, realized skewness and expected stock returns, signed jump variation (Patton Sheppard), realized semivariance, intraday return distribution shape as a characteristic,
idiosyncratic skewness, high-frequency moments cross-sectional pricing, China A-share realized moments.

**L11(对准 N2:两个公司层面日度序列之间的「滚动回归统计量」当特征,以及该用斜率还是 t 值)**
把**两个公司自己的日度时间序列**(例如价格粘滞程度与成交量粗糙度)做**滚动回归**,然后用回归结果当横截面特征,文献里有哪些做法和证据?具体想要三件事:
(1) **用斜率、t 值、还是 R²**:有没有文献比较过「斜率」与「用标准误标准化之后的 t 值」在横截面上的表现,并报告过 t 值更稳?常见的处理还有哪些(收缩、Winsorize、压成分位)?
(2) **窗口**:这类个股层面的滚动回归常用多长(一个月、半年、一年、两年),有没有报告过**需要 100–200 个交易日**、更长反而变差的结果?
(3) 这类「关系型」特征通常被解释成什么(流动性供给、知情交易、做市行为、注意力),以及怎样排除它只是波动或换手的另一种写法。
关键词:滚动回归系数当因子、个股层面的时序回归特征、t 值标准化、回归斜率的估计噪声、关系型特征、价格粘滞、量价关系;
rolling regression beta as a firm characteristic, t-statistic versus raw slope in cross-sectional factors, estimation error in firm-level betas, shrinkage of estimated betas,
price staleness / price delay measures, volume-volatility relation at the firm level, window length for firm-level rolling regressions.

**L12(对准 1.5 节与 R 第 13、14 条:样本筛选 / 数据质量筛子对因子表现的影响)**
在**中国 A 股**的因子研究里,**近期停牌、刚复牌、上市不满一段时间、长期涨跌停或零成交**的股票通常怎么处理(剔除、延后纳入、分组),
这些筛选规则对因子收益的影响有多大 —— 有没有文献**量化**过「同一个因子在加/不加这类筛子时的差别」?具体三件事:
(1) 常用的筛选口径与阈值(最近 N 日有成交的天数、上市满多少个月、剔除涨跌停日的交易),有没有做过阈值敏感性?
(2) 「剔掉这些票之后因子变强」通常被解释成**去掉了估计噪声 / 不可交易性**,还是**筛选变量本身携带 alpha**?文献用什么办法把两者分开?
(3) 对**用高频数据估出来的统计量**(已实现波动、峰度)来说,交易不活跃 / 有缺口的股票带来的估计偏差有多大,文献推荐的最小样本量是多少?
关键词:停牌与复牌处理、上市年龄筛选、涨跌停不可交易、样本筛选对因子收益的影响、高频估计的最小样本、A 股实证样本处理;
sample screens in China A-share factor research, suspension and resumption handling, listing-age filters, price-limit hits and tradability,
does the screen carry alpha or remove noise, minimum number of intraday observations for realized measures, microstructure noise in realized moments for illiquid stocks.

---

## 6. 本轮写下的预测(最后一轮,留给判读时的归因对账;只涉及 train / valid)

1. **1.1 节的核心检验**:`div(cross_stddev(day_durbin_watson(High), 20), cross_mean(day_durbin_watson(High), 20))` 落在 **+0.6 ~ +1.3**(概率 60%),
   并且**高于** `cross_stddev(day_durbin_watson(High), 20)` 不除水平的版本。若它 ≤ +0.2,「离散度是全部 alpha」要改成「水平 × 离散度的乘积才是信号」。
   (我第 2 轮在同一个 head 上押 `cross_max` ≥ +1.20 押错了 1.26,所以这次把区间放宽、概率降到 60%。)
2. **`cross_mean(day_mean(neg(in_delta(Volume, 60))), 20)` 落在 +0.9 ~ +1.5**(概率 55%),**替换原 head(+0.5370)的概率 65%**;
   原始 `|rho_known|` ≥ 0.45 的概率 35%(这是它唯一的否决通道)。
3. **`day_wmean(Ret, Ret)` 单独 < +0.3**(概率 70%):按 1.1 节,M3 那个 head 的 alpha 在 5 日方差里,不在原料里 —— 和 `day_max(Ret)`(−0.274)、`day_cov(Ret, Ret)`(−1.550)同型。
   若它 ≥ +0.8,1.1 节在第三个原料上就不成立,M3 第三个 head 要另找解释。
4. **窗口都到 2 的那一发(4.2 第 8 条)低于 +1.4126**(概率 60%)—— 即偏差 (i)「叠加两个已证实方向」第四次复现。
5. **1.5 节那个筛子不是通用处理**:第 13、14 条两次移植里,**至多一次** gain ≥ +0.1(概率 70%);两次都 ≥ +0.1 的概率 10%。
6. **`cross_mean(day_kurt(Ret), 20)` 落在 +1.0 ~ +1.4**(概率 55%),即不会比 head 的 +1.2330 高出 0.1 以上 ⇒ 不替换(概率 70%)。EMA hl 已经是 20,箱式平滑多半是重复平滑。
7. **4.2 第 6 条(第 1 轮 E 头名在普通奖励下重评)≥ +0.9324 并替换 +0.8324 那个 head 的概率 45%**;score ≥ +1.2 的概率 25%。
   这是对「E 的奖励口径藏掉了信息」这个判断的直接检验。
8. **若 E 位给核心 α**:产出 ≥ 1 个 head 的概率 **30%**(两轮 0/176 的先验压着,家族只有 1 个和外围几乎全开是加分项);
   若有 head,它会带一个**第二个叶子**或一个**分桶 / 筛选算子**,不会是核心的纯时间序列变形;与 head +1.3407 的交易信号 |ρ| 落在 0.2 ~ 0.5。
9. **若两个位都给 N**:合计产出 ≥ 2 个 head 的概率 **65%**(两轮 N 的实际是 5 和 2);N2 那个位至少收 1 个 head 的概率 **75%**(底座 t@100 的分数已知 +1.1434,唯一风险是原始秩禁令)。
10. **最终库的结构判断**:23 个 head 里 S 一族 5 个、股价水平一族 6 个,PLAN §3 的贪心去重(ρ ≥ 0.7 或 ρ ≤ −0.5)会把这两族各砍到 1–2 个;
    真正互相正交的大概是「日内成交量时间分布(对数 + 水平两份)」「日内波动结构的不稳定(M3 一族 + DW(High))」「日内收益分布形状(`day_kurt`)」「S / 价格粘滞」「名义股价水平」五条,
    本轮能加的最多再一条(不稳定度的显式写法或 t@100)。
