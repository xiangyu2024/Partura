# 结构解剖:种子 808,B 组,第 2 轮

快照:`c05s808M1_I0_open_search`、`c05s808M2_I0_open_search`、`c05s808Br1a_Ea`、`c05s808Br1b_Nb`;
6 个 head、320 个已评分候选、拆解 23 次付费评估(上限 48,**浪费 25 次**)、R 候选 0 个、已生效替换 0 个。

本轮**第一次有真的充分性 / 必要性 / 敏感性实测**(第 1 轮拆解表是空的)。下面凡是推断都标「推断」。

---

## 0. 先说两个口径问题(不说清楚,下面的数字会被读错)

### 0.1 共性(enrichment)这一轮已经不可直接解读:它主要在量「这个子树出自哪一次运行」

`scripts/c05_locate.py` 的共性是把**快照里 4 次运行的存档合在一起**(`c05_lib.archive(eps)`,320 个)做 Mann–Whitney。
而这 4 次运行的过线率差了一个量级:

| 运行 | 已评分 | 过线 | 入 heads |
|---|---|---|---|
| M 第 1 批 | 91 | 0 | 0 |
| M 第 2 批 | 61(= 320 − 91 − 84 − 84) | — | 4 |
| `c05s808Br1a_Ea` | 84 | 9 | 1 |
| `c05s808Br1b_Nb` | 84 | 31 | 1 |

全池均值是 **−0.5274**(两行独立反推一致:`inv(LogFloatShares)` 75×(−0.1994) + 245×(−0.6279) = −168.8;
`cross_tail_mean_q75(LogFloatShares, 15)` 26×0.5145 + 294×(−0.6196) = −168.8;/320 都得 −0.5274)。
Br1b 的 84 个里 31 个过线,所以**任何只在 Br1b 里出现的子树都会自动得到 ≈ +1.0 的「均值差」**,
与它本身好不好无关 —— 这正是 `cross_tail_mean_q75(LogFloatShares, 15)`(n=26,+1.13)、
`cross_quantile_q50(cross_tail_mean_q75(LogFloatShares, 15), 241)`(n=14,+1.08)那一串的来历:它们是 N 位种子的部件,
N 位的基准率高,于是整串都「显著」。同理 Br1a 的 84 个全部围着 `inv(LogFloatShares)` 转。
**这是按运行分层的辛普森悖论,不是结构的证据。** 机械核心卡第 6–15 位、第 21 位全部由此而来,顺序没有含义。

能用的还有两处:(i) **同一次运行内部**的对比(下面 §1.1 的 `cs_bucket_zscore` 两种写法、§1.4 的三种两字段组合);
(ii) **负号那一侧**:共性的 40 行按效应截断,最后一行是 −0.936(mean_with ≈ −1.45),
所以凡是没进表的、出现在 ≥ 4 个候选里的子树,其 mean_with 一定 < ≈ −1.45。这条给出了下面 §1.5 的「全军覆没」结论。

### 0.2 本轮的敏感性只有窗口一个维度,字段维度一次都没测

`c05_locate.py:47` 的 `SWAP = {"Close": "Vwap", "Vwap": "Close", "Open": "Close", "High": "Low", "Low": "High", "Volume": "Amt", "Amt": "Volume"}`。
本轮 4 个被拆的 head 只用到 `Ret`、`LogFloatCap`、`LogFloatShares` 三个字段,**一个都不在换表里**,所以 23 次评估里 0 次字段替换。
另外 `wn = next((n for n in nodes if n.window), None)` 只取**第一个**带窗口的节点(根上那层 `ts_max`),
所以 head 1 里面那两个 `ts_max@40`(中间那层、条件变量那层)的窗口**从没被动过**。
→ 这两个缺口正好是本轮 R 的现成题目(§2.3)。

另外 `MAX_HEADS = 4`:head 5(+0.56)与 head 6(+0.56)**本轮没有被拆**,会自动占掉第 3 轮的拆解预算。

---

## 1. alpha 的来源

本轮快照里有**三条互相独立的轴**,证据强度差很多。按强度排:

### 1.1 来源 A(唯一一条像真机制的):分钟级「价格栅格粒度」,在市值十分位内条件标准化

涉及的 head:

- +1.45 `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)), 40), 40)`(sign +1,hl 20)
- +0.82 `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40), 40)`(sign −1,hl 5)

**被测的量是什么**(读源码,`partura/ops_ext.py:607`):
`day_distinct_ratio(x)` = 当日有限分钟里**不同取值的个数 / 分钟数**,「1/n = 一整天一个价,1 = 每分钟都不同」;
注释自己写了「作用在价格上:这一天走过了多少个价位 —— 低价股在一跳的栅格上很粗」。
作用在 `Ret` 上(`alphacube/synthetic.py:131`:`ret = close / open_ - 1`,分钟 bar 收益),
分钟收益的可取值是 `k × 一跳 / 价格` 的整数倍,所以这个比值由三件事决定:
(1) **一跳相对价格的粗细**(价格越低越粗,distinct 越小);(2) **分钟成交活跃度**(没成交的分钟收益重复,distinct 变小);
(3) 真实的日内波动(走过的价位越多,distinct 越大)。
也就是说它是一个**微观结构的「价格粒度」指标**,与 1/价格、与不活跃度高度相关(推断,但 (1) 有源码注释直接支持)。

注意:奖励的控制里已经有流动性、`cross_mean(day_std(Ret), 20)`(波动)、20 日反转、已知族、`LogFloatCap`,
而且全是**秩空间的线性投影**(`partura/steer.py:403` `neutral_basis`:`_zrank` 之后 QR)。
所以留下来的只能是这个量**线性挡不住**的那部分。

**证据(全部来自本轮 23 次付费评估):**

| 证据 | 数字 | 读法 |
|---|---|---|
| 必要性:去掉 `cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap)` | +1.45 → **−0.73**(必要性 **+2.19**) | 整张表最大的一个数。`ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(day_distinct_ratio(Ret), 40)), 40), 40)` 把「市值十分位内」换成「自身 40 日 max」,直接变成**负** alpha |
| 必要性:去掉条件变量里的 `ts_max(·, 40)` | +1.45 → +0.35(必要性 **+1.10**) | 条件变量必须是**近期峰值**(慢变的分组),改成当期值几乎全丢 |
| 充分性:剥掉最外一层 `ts_max` | **+1.17**(train 1.17 / valid 2.01) | 单层就有 1.17,是本种子最强的可单独求值结构 |
| 充分性:只留一层条件化 `ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)` | **+0.58**(train 0.58 / valid 0.90) | 最小的可用单元,自己就过线 |
| 敏感性(窗口):最外 `ts_max@40` → 20 / 80 | +1.27 / +1.16(基准 +1.45) | **三个窗口都 ≥ 1.16**,不是窗口拟合出来的 |
| 稳定性 | train 1.466 / valid 1.455 | 两段几乎相等,是 6 个 head 里唯一这样的 |
| 与已知族 | ρ = −0.21(基准)、−0.18 ~ −0.12(各变体) | 离 0.5 很远 |
| head 2 的窗口敏感性 | 20 → +0.79,40 → +0.82,80 → **+0.86**(valid 1.71) | 更长更好,说明还没到最优(→ R) |

**条件化的「形状」本身就是 alpha 的一部分**:同样是 `day_distinct_ratio(Ret)` 配 `LogFloatCap`,

- 十分位内条件 z 分 `cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap)`:n=14,mean_with **+0.66**;
- 剔除式筛子 `cs_last_high05(day_distinct_ratio(Ret), LogFloatCap)`:n=7,mean_with **−0.19**。

两者在同一池里差 0.85。(这一条是 §0.1 允许的「同类对比」:两者都主要来自 M 第 2 批。)

**双重去水平是 head 1 比 head 2 强一倍的原因。** head 1 的条件变量是
`ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)` —— 也就是 head 2 的核心本身。
所以 head 1 = 「先按市值十分位去水平,再按**自己近 40 日峰值所在的十分位**去水平」。
第二次去水平把「这只股票一向粒度粗 / 细」这个静态属性也剥掉了,剩下的是**相对自身近期体制的粒度异动**。
这解释了两件事:(i) 为什么 head 1 的 sign 是 +1 而 head 2 是 −1(一个是异动、一个是水平,方向本来就不必相同);
(ii) 为什么必要性 +1.10:把条件变量从「40 日峰值」改成「当期值」,等于拿被解释的量去给自己分组,信息自然塌掉。

**是不是「只是代理」?** 三条反驳:(i) 必要性 +2.19 说明**原始的量没用甚至有害**,起作用的是分位内的相对位置 ——
而流动性与波动的控制是全市场线性的,「分位内的非线性」本来就挡不住,所以它确实是控制挡不住的那部分;
(ii) ρ_known = −0.21,与换手族离得远;(iii) 窗口与两段都稳。
诚实的保留:它仍可能是**流动性 / 波动在市值分位内的非线性暴露**(即「分位内的流动性」而不是新机制),
本轮没有任何证据能排除这一点 —— 这需要把 `Ret` 换成 `Close` / `Vwap`,或把条件变量换成成交额分位才能分开(§2.3 的 R-6 ~ R-10)。

### 1.2 来源 B:规模的非线性 / 杠铃形 —— 判为「只是代理」

涉及的 head:

- +0.74 `ts_max(ts_max(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), 40), 40)`(sign −1,hl 0)
- +0.56 `ts_max(cs_bucket_zscore(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), ts_max(cs_bucket_zscore(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), LogFloatCap), 40)), 40)`(sign −1,hl 0;§1.1 那套双重条件化的同一招,换了被测量)

**它是什么**(`partura/ops_ext.py:397` + `_lexi`,339 行):`cs_last_high05(y, x)` = `rank(y)` 落在 (0,1],
再把 **x 最大的 5%**(按整个并列块)的值 −1 推到所有人下面。这里 y = x = `LogFloatCap`,
所以它就是「**市值秩,但把最大的 5% 扔到最底**」。sign = −1 → 多头那一档 = 原始值最低的 10% = **最大的 5% + 最小的 5%**,
一个**杠铃**。杠铃正是线性秩中性化挡不住的首要非线性(二次项),而 `LogFloatCap` 就在控制里。
→ 这不是新机制,是**控制变量本身的几何残留**。

**证据:**

| 证据 | 数字 | 读法 |
|---|---|---|
| 必要性:去掉 `cs_last_high05(LogFloatCap, LogFloatCap)` | +0.74 → **−0.03**(必要性 +0.77),而且 **ρ_known = −0.5527** | 没有这个 5% 的折点,它就只是 `ts_max(ts_max(ts_max(LogFloatCap, 40), 40), 40)`:既没分、又**超过 0.5 的已知族门槛会被判不合格**。所以这个筛子一半的作用是「躲开已知族」 |
| 充分性链 | 0 层 ts_max **+0.19**(train 1.19 / valid 0.19)→ 1 层 +0.40(1.40 / 0.40)→ 2 层 +0.58(1.10 / 0.58)→ 3 层 +0.74(0.74 / 0.76) | train 一路从 1.4 掉到 0.74,valid 一路从 0.19 爬到 0.76。**score 的提升全部来自 valid**,train 在变差 |
| 敏感性(窗口) | 20 → +0.71,40 → +0.74,80 → **+0.35** | 窗口加倍砍掉一半,不稳 |

`ts_max` 堆叠在这里做的事情很具体:原始值慢变,一只股票刚进「最大 5%」那条带时值会突然掉到 −0.05,
而 `ts_max` 取窗口内最大值 → 它**记住的是进带之前的秩**,等于把分组变动延迟 40 / 80 / 120 天。
在 15bp 成本 + 十分位纯多头的口径下,这主要是**降换手**,不是增信息 —— 和「train 掉、valid 升」的形状完全一致。
**结论:来源 B 过线靠的是「非单调地动一下控制变量」+「把它变慢」。它会过线,但它是代理。**

### 1.3 来源 C:`LogFloatShares` 的水平,被长短两级窗口洗过 —— 第 1 轮那个簇,原地抬了 0.07

涉及的 head:

- +0.61 `div(LogFloatCap, inv(LogFloatShares))`(来自本组 r1 的 E 位;`div(a, inv(b))` = a × b,见 `operators/common.py:175,191`,所以它就是 `LogFloatCap × LogFloatShares`)
- +0.56 `cross_mean(cross_quantile_q50(cross_tail_mean_q75(cross_quantile_q50(cross_tail_mean_q75(LogFloatShares, 15), 241), 15), 241), 15)`(来自本组 r1 的 N 位)

**证据:**

- 充分性:`inv(LogFloatShares)` 单独 **+0.478**(train 0.478 / valid 0.770)—— 第 1 轮解剖说的那个「卡在 0.465–0.486 的簇」,
  本轮第一次被付费测准:**0.478,确实差一点过线**。第 1 轮的推断成立。
- 两个位各自产出的是**一个**因子、不是一堆:Br1a 的 9 个过线者全挤在 **0.594–0.608**(宽 0.014),只入 1 个 head;
  Br1b 的 31 个过线者全挤在 **0.550–0.555**(宽 0.005),也只入 1 个 head。
- `cross_tail_mean_q75(x, 15)` 是「近 15 日里前 25% 那一档的均值」,`cross_quantile_q50(x, 241)` 是「近 241 日中位数」
  (`ops_ext.py:300` 的 `_tail_mean`)。作用在一个只在解禁 / 增发 / 送转时跳变的阶梯函数上,
  这一串就是**「近期上尾水平 vs 一年中位数」的多级平滑**。把 0.478 抬到 0.555 的是**窗口的长短搭配**,不是任何新信息。

**判为代理**:它是「流通股本在 `LogFloatCap` 被中性化之后剩下的那部分」,属于静态风格;
更要紧的是它和 M 的轴重合风险 —— 见 §4.0。

### 1.4 被证伪的那条:名义股价轴(第 1 轮的假设 (a))

第 1 轮把簇的身份留了两个可能:(a) 名义股价(低价股效应),(b) 规模的非线性残差,先验 55 : 45。
本轮的证据**一致地指向 (b),并且把 (a) 的三种写法全部打掉**:

| 写法 | 口径 | 数字 |
|---|---|---|
| `div(LogFloatCap, inv(LogFloatShares))` = cap × shares(**和**,仍是规模方向) | 付费拆解 / head | **+0.61** |
| `inv(LogFloatShares)` 单字段 | 付费拆解 | **+0.478** |
| `div(LogFloatCap, LogFloatShares)` = cap / shares(**商**,≈ 价格轴) | 付费拆解(knockout) | **−2.00**(必要性 2.61);注意 train 只有 **−0.154**,即 ±1 两个方向在 train 上都不行 |
| `cs_regres(LogFloatCap, inv(LogFloatShares))`(横截面 OLS 残差 ≈ 价格轴;r1 有 9 条种子用它当骨架) | 共性,n=7 | mean_with **−1.17** |
| `inv(inv(LogFloatShares))`(r1 种子 1「精确 log 名义股价」的部件) | 共性,n=9 | mean_with **−0.12** |

同样的两个静态字段,**乘积 +0.61、商 −2.00、回归残差 −1.17**,跨度 2.6 个夏普。
→ 第 1 轮「`LogFloatCap` 与 `LogFloatShares` 的任何线性组合在秩中性化后都退化成同一个残差」这条推理**被证伪**:
秩变换是非线性的,不同的组合面给出不同的秩分布,中性化(秩空间线性)之后剩下的东西完全不同。
→ 并且方向明确:**单调递增于「规模」那一侧的组合才有分(+0.48 / +0.61),把价格轴单独拿出来就没有分。**
这与 §1.2 的杠铃是**同一件事的两种写法**:起作用的是**规模的曲率**,不是每股价格。

顺带修正第 1 轮的另一条推理:「hl = 0 被选中时任何严格单调变换的 score 完全相同」只在 **hl = 0** 成立。
`long_neutral` 是先 `bk.smoothed(raw, hl)` **再** `_zrank`(`partura/steer.py`),hl ∈ {0, 5, 20};
hl > 0 时平滑作用在**原始数值**上,单调变换不再等价。实测:`sqrt(inv(LogFloatShares))`(n=8)mean +0.4976,
而 `inv(LogFloatShares)`(n=75)mean −0.1994;`sqrt(div(LogFloatCap, inv(LogFloatShares)))`(n=4)−0.067
而 `div(LogFloatCap, inv(LogFloatShares))`(n=9)+0.262。(这两对受 §0.1 的运行混杂影响,只当旁证。)

### 1.5 全军覆没的那一侧:价格 / 日收益 / 日内极值类结构,以及涨跌停

共性表的负号一侧非常整齐(这一侧按 §0.1 是可读的):

| 子树 | n | mean_with |
|---|---|---|
| `cross_autocorr_s1(day_topw_mean(High, Vwap), 15)` | 5 | −1.45 |
| `ts_delta(log(day_last(Close)), 1)`(日收益) | 13 | −1.38 |
| `log(day_last(Close))` / `day_last(Close)` | 19 | −1.32 |
| `log(day_max(High))` / `day_max(High)` | 4 / 5 | −1.28 / −1.26 |
| `day_topw_mean(High, Vwap)` | 6 | −1.25 |
| `cross_max(ts_delta(log(day_last(Close)), 1), 20)`(**MAX 效应**) | 4 | −1.22 |
| `day_open(High)` | 8 | −1.17 |
| `day_autocorr_n1(Volume)` | 8 | −1.02 |
| `day_sum(Amt)` | 4 | −0.91 |

全池均值 −0.53,这一串全在 −0.9 ~ −1.5。**在这个奖励里(流动性、20 日波动、20 日反转、换手族、市值都被控制住),
普通的价格 / 日收益 / 日内高点类结构没有残值。** MAX 效应(−1.22)是 r1 两个位的核心假设之一,这里是直接的反例。

**涨跌停这条轴一点痕迹都没留下**:共性 40 行里没有任何含 `LimitWidth` / `BoardCode` / `ListAge` 的子树。
按 §0.1 的截断逻辑(末行效应 −0.936,对应 mean_with ≈ −1.45),能断言的是:
**没有任何出现在 ≥ 4 个候选里的 `LimitWidth` 结构,其均值高于 ≈ −1.45。** r1 的 N 位 16 条种子全部围绕 `LimitWidth`,
它们没有留下任何比全池均值好的后代。

### 1.6 外围算子真正在做的三件事(这比「哪个核心」更能指导本轮)

M 第 2 批的 heads 外面只有两种算子:`ts_max` 和 `cs_bucket_zscore`。它们做的是:

1. **过闸门(`distinct_fraction ≥ 0.5`)。** `day_distinct_ratio(Ret)` 自己 distinct = **0.0617**(门槛废品);
   `cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap)` = **0.4331**(还是废品);
   再套 `ts_max(·, 40)` → **0.9614**(过)。而 `ts_max(ts_max(day_distinct_ratio(Ret), 40), 40)` = **0.0584**(仍废)。
   → **顺序是死的:先条件 z 分(把并列拆成连续值),再 `ts_max`(把各股的历史轨迹拉开)。单靠 `ts_max` 过不了闸门**
   (max 会饱和到共同的高位)。这一条对写种子是硬约束:凡是以 `day_distinct_ratio` / 比例类量为被测量的种子,
   必须自带「条件标准化 + 时序归约」两层,否则白花一次评估(闸门失败照样计入预算)。
2. **去水平**(§1.1 的双重 `cs_bucket_zscore`)。
3. **降换手 / 变慢**(§1.2 的 `ts_max` 堆叠;head 3 的 train 掉 valid 升就是这个形状)。
   注意 hl ∈ {0, 5, 20} 已经在做一层平滑,而三个 head 各选了 hl 20 / 5 / 0 —— 「堆 `ts_max`」和「让 hl 变大」是两条互相替代的变慢途径,
   本轮没有任何证据说明 `ts_max`(峰值)比 `ts_mean` / `ts_decay_linear` / `cross_quantile_q50`(平均 / 中位)更好。**这是 R 最该问的问题。**

### 1.7 两个工具层面的事实,顺手修正第 1 轮的两处误判

- **深核心不受 GP 的 `max_depth = 4` 限制。** 第 1 轮写「深度 2 的核心只给外围留 2 层」。
  实际上 `max_depth = 4` 只配置 `TypedTreeGenerator`(随机初代树、变异子树 `randint(1, max_depth - 1)`);
  `alphacube/mining/gp.py` 的 `_next_generation` 对交叉 / 变异的子代**不做深度检查**(只有 `is_valid_root`),
  种子另有 `seed_max_depth = 9`。所以深度 4、6 的核心都能用,外围照样能长。
- **E 位的「no-core 漏损」可以量出来(推断)。** `inv(LogFloatShares)` 本轮 n_with = **75**,第 1 轮在 M 第 1 批里是 14;
  Br1b 的候选基本不含它,所以 Br1a 贡献 ≈ 61 个,而 Br1a 评了 **84** 个 → **约 23 个(≈ 27%)已评分候选不含核心**
  (与 PLAN 修订 1 的「连续拒绝后退回不含核心的最小树」、冒烟测试 2/16 = 12.5% 同向,实际更高)。
  `sampling = {'c05_no_core': 1289, 'c05_periphery_seen': 13}` 也指向同一件事:**must-contain 是真正在打的那条约束,
  外围新颖性几乎是免费的**(`periphery()` 比的是算子名集合,`scripts/idea_search.py:312`,加一个没见过的算子名就一定新)。
  → 核心越深、越罕见,这个漏损越大(交叉点落在核心内部的概率随核心占树的比例上升)。选核心时要把这 20–30% 的损耗算进去。

---

## 2. 烂部件

### 2.1 必要性 ≤ 0 的部件:一个都没有

本轮 4 个 knockout 全部为正必要性:+2.19、+1.10、+0.77、+2.61。**没有一个部件是多余的。**
这和第 1 轮的推断(「静态字段外面的单调一元包装必要性为 0」)不矛盾 —— 本轮被拆的 4 个 head 里没有那种包装,
`div(LogFloatCap, inv(LogFloatShares))` 的 `inv` 反而必要性 **+2.61**(去掉就从乘积变成商,见 §1.4)。

### 2.2 换掉反而更好的变体:工具口径下 0 个,但有一个差一点

`r_candidates` 要求 `score ≥ head + 0.1` 且非充分性、`|ρ_known| < 0.5`、`ρ_head ≥ 0.5`(`c05_locate.py:294-300`)。
唯一一个**比原 head 好**的变体是:

- head 2 `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40), 40)`(+0.8156)
  → 窗口 80:`ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40), 80)` = **+0.8607**(train 0.861 / valid 1.708,hl 0)。
  增益 **+0.045**,差 0.055 没到替换门槛。

**这是本轮 R 最该顺着走的线头**:同一条趋势上 20 → 40 → 80 给出 0.79 → 0.82 → 0.86,**还在往上**。

### 2.3 R 目标(本轮必须写满,否则再浪费 16 次评估)

第 1 轮 48 次拆解 + 16 次 R 全废,本轮拆解又只花了 23/48。**R 这 16 次是唯一还能救的预算。**
按「信息量 × 替换概率」排序(替换需 ≥ 原 head + 0.1、ρ_head ≥ 0.5、|ρ_known| < 0.5):

**A 组 —— 顺着 §2.2 的趋势走(替换概率最高)**

1. `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40), 120)`(head 2;80 之后继续加长)
2. `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 80), 80)`(head 2;两层都加长)

**B 组 —— 问「峰值 vs 平均」(§1.6 第 3 条,本轮最该问的问题;替换 + 识别双重价值)**

3. `ts_mean(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40), 40)`(外层 max → mean)
4. `ts_decay_linear(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40), 40)`
5. `cross_quantile_q50(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40), 40)`(中位数,抗尾)
   —— 如果 3/4/5 ≈ head 2,那么「变慢」才是外围的作用,`ts_max` 的「峰值」语义是多余的,
   第 3 轮就不该再在 `ts_max` 堆叠上花力气;如果明显更差,峰值本身是信息。

**C 组 —— 补上工具没做的字段替换(§0.2;识别 §1.1 的三条通道,最有科学价值)**

6. `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Close), LogFloatCap), 40), 40)`
   (`Ret` → `Close`:只量**价位栅格**,去掉「没成交的分钟收益重复」这条通道)
7. `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Vwap), LogFloatCap), 40), 40)`
8. `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogTotalCap), 40), 40)`(条件变量换总市值:自由流通比例是否参与)
9. `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), cross_mean(day_sum(Amt), 20)), 40), 40)`
   (条件变量换**成交额分位**:直接问「§1.1 是不是分位内的流动性」)
10. `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), ListAge), 40), 40)`(条件变量换股龄)

**D 组 —— 补 head 1 里从没被动过的两个窗口(§0.2)**

11. `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 120)), 40), 40)`(**条件变量**的窗口 40 → 120)
12. `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 20)), 40), 40)`(→ 20)

**E 组 —— 问来源 B 的筛子宽度(§1.2;便宜,而且直接判定「杠铃」这个读法)**

13. `ts_max(ts_max(ts_max(cs_last_high10(LogFloatCap, LogFloatCap), 40), 40), 40)`(5% → 10%)
14. `ts_max(ts_max(ts_max(cs_last_low05(LogFloatCap, LogFloatCap), 40), 40), 40)`(改筛**最小** 5%:若由正转负 / 大幅变差,「两端杠铃」这个读法成立)

**F 组 —— 剥掉来源 C 的冗余层(§1.3)**

15. `cross_quantile_q50(cross_tail_mean_q75(LogFloatShares, 15), 241)`(head 6 砍掉外面两层;若 ≈ 0.55,证明那两层是纯冗余)
16. `div(LogTotalCap, inv(LogFloatShares))`(head 4 的 `LogFloatCap` → `LogTotalCap`:流通 / 总股本哪一个在起作用)

注:13、14、16 严格说是「替换部件」,符合 PLAN §2.5 的 R 定义;3–5 也是(换掉一个算子)。
6–10 换的是**字段**,正是 `c05_locate.py` 的 `swap` 本该做却因为换表里没有 `Ret` / `LogFloatCap` 而没做的那一类。

---

## 3. 之前的任务

### 3.1 两个位都没有打到自己瞄的地方,但 E 位达成了「产出第一个 head」这个目标

| 位 | 瞄的 | 实际产出 | 判 |
|---|---|---|---|
| `c05s808Br1a_Ea`(核心 `inv(LogFloatShares)`) | 条件秩 / 条件 z 分、与 MAX / 日内波动 / 价格栅格 / 情绪状态的交互 | 9 个过线全是 `div(LogFloatCap, inv(LogFloatShares))` 的近亲(0.594–0.608),入 1 个 head;**没有一条交互型结构过线** | 目标(激活第 2 轮拆解)达成;机制假设不成立 |
| `c05s808Br1b_Nb`(涨跌停带宽单位的极端收益 / 触板) | 带宽单位 MAX、上影回落、触板强度 | 31 个过线全是 `LogFloatShares` 的 `cross_*` 平滑链(0.550–0.555),入 1 个 head;共性 40 行里**没有任何 `LimitWidth` 子树** | 机制假设完全不成立;GP 漂回 `LogFloatShares` 吸引盆 |

两个位的 16 + 16 条手写种子**都没有改变结果的走向**:两次都落回第 1 轮解剖自己指认的那个静态簇。
`sampling` 也说明 E 位的约束主要消耗在 must-contain 上(1289 次 no-core 拒绝 vs 13 次外围已见)。

### 3.2 第 1 轮预测逐条打分

**解剖员 analysis.md §3:**

- **P1a**(单字段包装 / 单字段窗口归约会继续停在 0.46–0.49,不会过 0.5):**错**。
  Br1b 的 31 个过线者**全部只含 `LogFloatShares` 一个字段**,靠 `cross_tail_mean_q75(·, 15)` + `cross_quantile_q50(·, 241)` + `cross_mean(·, 15)`
  这种**长短两级窗口搭配**从 0.478 抬到 0.555。错在把「窗口归约」当成了无害包装 —— 单窗口(`ts_max(·, 50)`)确实无害,**多级长短搭配不是**。
- **P1b**(E 位若产出 head,一定含第二个字段或同字段差分):**对**。head = `div(LogFloatCap, inv(LogFloatShares))`,两个字段。
- **P2**(`sub(LogTotalCap, LogFloatCap)` 的 score 低于 `sub(LogFloatCap, LogFloatShares)`,且前者在 0.1–0.5):**无法核对**
  (工具不导出单个候选的 score,这两条都没进共性的 40 行)。但 §1.4 的旁证一致:价格轴的三种写法都是负的。
- **P3**(纯股本差分会被 `distinct` 闸门挡掉):**本轮没放这类种子,未直接检验**;机制本身被本轮 4 个闸门失败旁证(§1.6 第 1 条)。
- **P4**(手写种子的 score 分布明显高于机械嫁接):**无法核对**(`loc.json` 只给 `sampling` 计数,不分种子来源)。
  建议 PI 以后要核对这一条,就得在任务里要求把 `evidence` 里的初代分档写出来。

**PI notebook 的预测:**

- **E-P1**(种子 1 `sub(LogFloatCap, inv(inv(LogFloatShares)))`、种子 2 `cs_regres(LogFloatCap, inv(LogFloatShares))` 落在 0.44–0.52):
  **错**。`cs_regres(LogFloatCap, inv(LogFloatShares))` 那一簇 n=7、mean −1.17;`inv(inv(LogFloatShares))` n=9、mean −0.12。
  并且 notebook 自己写的「若任一 > 0.55,说明『线性组合退化成同一残差』这条推理错了」—— 实际的否证来自另一侧:
  它们远**低于**区间,而同两字段的乘积有 +0.61,跨度 2.6 个夏普,同样证明那条推理错了(§1.4)。
- **E-P2**(自由流通种子 3 低于种子 1 且在 0.0–0.4;复权因子种子 4 的 |score| < 0.3):**无法核对**。
- **E-P3**(`cs_bucket_rank(inv(LogFloatShares), LogFloatCap)` 与种子 1 相差 ±0.06 以内):**无法核对**
  (`cs_bucket_rank` 没进共性 40 行)。讽刺的是:**同一个想法的「z 分版」`cs_bucket_zscore(·, LogFloatCap)` 正是 M 第 2 批最强 head 的核心**
  —— 方向对了,但 r1 把它配在了错的被测量(静态股本)上,而 M 把它配在了分钟级粒度上。
- **E-P4**(产出 ≥ 1 head 概率 50%):**对**(1 个)。
  (「最好的 head 是价格轴与 MAX / 日内波动的交互,0.50–0.65」:**错**,是纯静态两字段乘积;
  「纯价格轴过线概率 < 20%」:方向上对,但过线的恰恰是种子 1 / 2 的同类(静态两字段组合),表述也不准;
  「同一位内多个 head 彼此 ρ ≥ 0.7,独立的不超过 2 个」:**对**,9 个过线只入 1 个。)
- **E-P5**(手写种子中位数比机械嫁接高 0.3 以上):**无法核对**。
- **N-P1**(产出 ≥ 1 head 概率 35%):**对**(1 个)。(「最可能的 head 是带宽单位 MAX / 上尾均值 / 上影回落,sign −1,0.5–0.7」:
  **错到底**,实际是 `cross_mean(cross_quantile_q50(cross_tail_mean_q75(...LogFloatShares...), 241), 15)` 一类,sign **+1**,0.555。)
- **N-P2 / N-P3**:**无法核对**。
- **N-P4**(N 的 head 与 E 的 head |ρ| < 0.3):**无法核对**(工具不给 ρ 矩阵),但两个 head 都在 `LogFloatShares` 轴上
  (一个是 `LogFloatCap × LogFloatShares`,一个是 `LogFloatShares` 的长平滑),|ρ| 很可能远高于 0.3 —— 见 §4.0 的后果。

**一句话总结第 1 轮**:12 条可核对的预测里,方向性对的 3 条(E-P4 / N-P1 的产出概率、P1b、「同位内 head 互相高相关」),
明确错的 4 条(P1a、E-P1、E-P4 的内容、N-P1 的内容),无法核对 6 条。
**凡是关于「哪个机制会过线」的预测全错;凡是关于「GP 会把预算花在哪、产出会不会互相重复」的预测都对。**
这和 PLAN §1 第 1 条(C03 / C04 里 Partura 的先验机制几乎都不成立)完全一致。
→ 本轮写任务时,信「工具 / 预算 / 去重」层面的判断,别信「机制」层面的先验。

---

## 4. 本轮候选

### 4.0 先说一条比选核心更重要的约束(直接决定本组的增量能不能留下)

PLAN §3:最终库按 **M 第 1..4 批 → 本组各轮**的顺序贪心去重,与已收 head **ρ ≥ 0.7 或 ρ ≤ −0.5 就丢**。
M 排在前面 → **本组任何与 M 的 head 相关度高(或强负相关)的产出,在最终库里一定被丢掉,等于白花。**
两个后果:

1. 本组 r1 的两个 head(`div(LogFloatCap, inv(LogFloatShares))`、`cross_mean(cross_quantile_q50(...LogFloatShares...))`)
   **彼此很可能 ρ ≥ 0.7**(同一条静态股本轴),最终库里**大概率只剩一个**。别把第 1 轮算成「2 个 head 的产出」。
   而且 M 第 3、4 批若落到这条轴上(M 第 1 批有约四成预算在这里),这一个也会被顶掉。
2. E 位的「家族控制」(把含核心的 heads 当控制加进中性化,`scripts/idea_search.py:183`)**和这条判读规则是对齐的**:
   它正好只奖励「M 已有的那条轴之外」的新信息。所以本轮的 E 应该**选一个家族非空的核心**,让这个控制替我们干活;
   选家族为空的核心(第 1 轮那种「E 位很便宜」的情形)反而会生产注定被去重掉的东西。

### 4.1 值得深挖的核心(≤ 3,按推荐顺序)

#### 核心 1(首选):`ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)`

(= 机械核心卡第 2 位;自身 score **+0.58**,train 0.58 / valid 0.90,distinct 0.961 **过闸门**,ρ_known 0.38)

- **为什么**:它是 §1.1 唯一那条像真机制的轴上**最小的、能单独过闸门的单元**。必要性证据最硬(+2.19 / 门槛废品),
  窗口三档都稳,train / valid 都 ≥ 0.58。而且它**过闸门**这一点很关键:核心自身 distinct 0.961 → 外面随便长也不容易变成门槛废品
  (对比:卡第 5 位 `cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap)` 自身 distinct 只有 0.433,
  以它为核心的候选每一个都要自己把并列拆开,闸门失败照样烧预算 —— §1.6 第 1 条)。
- **家族控制**(非空,正是我们要的):含它的 heads 有**两个** —— head 1(+1.45)和 head 2(+0.82)
  (head 1 的条件变量就是它本身)。所以 E 的奖励会把 M 第 2 批最好的两个 head 都减掉,**只有真的新信息才拿分**。
  这是本轮能买到的最干净的「增量」测量。
- **周围已经见过的外围写法**(共性 n_with = 11;`seen` 文件给的是快照全部 320 个候选的表达式,
  `periphery()` 比的是**算子名集合**):
  - `{}`(核心自己)——`SEEN` 默认含空集,所以「只把核心当因子」会被拒;
  - `{ts_max}` —— head 2 `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40), 40)`,以及 `ts_max@80` / `@20` 的那些变体;
  - `{ts_max, cs_bucket_zscore, day_distinct_ratio}` —— head 1,与卡第 1 位 `ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)), 40)`;
  - 快照里还有 `cs_last_high05(day_distinct_ratio(Ret), LogFloatCap)` 一系(n=7,mean −0.19),但它不含本核心,不进 `SEEN`;
  → **「再堆 `ts_max`」和「再做一次 `cs_bucket_zscore` 双重条件化」这两条路已经被 M 走过,会被外围新颖性直接拒掉。**
    必须换别的外围算子名:时序归约换 `ts_mean` / `ts_decay_linear` / `cross_quantile_q50` / `cross_tail_mean_q75` / `cross_zscore` / `cross_madz`;
    条件 / 分组换 `cs_bucket_rank` / `cs_bucket_demean` / `cs_regres` / `cs_flip_by_state` / `cs_state_rank` / `cs_last_*`;
    或者与第二个量交互(`mul` / `sub` 配 `cs_rank`)。
- **风险**:核心深度 4,`must-contain` 的 no-core 漏损按 §1.7 大概 20–30%,可能更高;
  而且家族控制很强,**产出 0 个 head 的概率不低**。但按 §4.0,这是唯一一种「如果产出了就真的留得下」的任务。

#### 核心 2(备选,和核心 1 二选一):`ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)), 40)`

(= 机械核心卡第 1 位;自身 score **+1.17**,train 1.17 / valid 2.01,distinct 0.907,ρ_known −0.21)

- **为什么**:全种子最强的可单独求值结构,而且它的**家族只有 head 1 一个**(head 2 不含它),家族控制比核心 1 轻一档。
- **周围已见外围**:只有 `{ts_max}`(head 1 本身)与 `{}`。**除了「再套 `ts_max`」,外围几乎是全新的。**
- **风险**:深度 6,核心占树的比重大 → 交叉 / 变异打坏核心的概率最高,no-core 漏损最严重(§1.7);
  而且它自身已经 1.17,E 要在一个 1.45 夏普的 head 被减掉之后再找新信息,门槛很高。
- 若 PI 要两个 E 位,**核心 1 + 核心 2 不要同时用**:它们在同一条轴上,家族高度重叠,等于把一个问题问两遍。

#### 核心 3(不推荐花 E 位,列出以备):`ts_max(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), 40)`

(= 卡第 3 位;自身 +0.58,train 1.10 / valid 0.58;家族 = head 3)

- 按 §1.2 它是控制变量的几何残留、窗口不稳(×2 掉到 0.35)、去掉筛子后 ρ_known = −0.55。
- 已见外围:`{ts_max}`(head 3)、`{ts_max, cs_bucket_zscore}`(head 5)。
- **建议用 R(§2.3 的 13、14)去问它,别花 96 次评估。**

**明确不要的核心**:`inv(LogFloatShares)`(已用 1 个 E 位,第 2 个只会再生产一遍 0.59–0.61 那个簇,
而且按 §4.0 这条轴的产出最可能被 M 顶掉)、卡第 6–15 位与第 21 位(全是 §0.1 的运行混杂假象)、
`day_distinct_ratio(Ret)` 裸量(distinct 0.0617,门槛废品,会把预算烧在闸门上)。

### 4.2 R 目标

见 §2.3,16 条写满。优先级:A 组(2 条,替换概率最高)> C 组(5 条,识别 §1.1 的通道)> B 组(3 条,判定 `ts_max` 的语义)
> D 组(2 条,补工具的缺口)> E 组(2 条)> F 组(2 条)。

### 4.3 N 的灵感

本轮 N 的处境和第 1 轮完全不同:**M 第 2 批交出了一个被验证过的「处理手法」**
(分位内条件 z 分 + 时序归约,把一个 distinct 0.06 的门槛废品做到 +1.45),而本种子**只在一个被测量上用过它**(`day_distinct_ratio(Ret)`)。
所以最高期望的 N 不是新机制,而是**把这个手法迁移到别的被测量上**。

1. **(首选)把「分位内条件标准化 + 时序归约」迁移到其他分钟级「形状」量。**
   §1.5 说明价格 / 日收益 / 日内极值类**水平量**在这个奖励里全军覆没(−0.9 ~ −1.5),
   而 §1.1 说明**比例 / 形状类**的量在条件化之后能到 +1.45。`partura/ops_ext.py` 里同类、快照**完全没碰过**的量:
   `day_flat_ratio`(零变动分钟占比)、`day_zero_ratio`、`day_at_max_ratio` / `day_at_min_ratio`(在日内极值附近停留的时间占比)、
   `day_flat_run_max`(最长停滞段)、`day_gini`(成交分布的不平均度)、`day_centroid`(成交的日内重心,早盘 vs 尾盘)、
   `day_topw_mean`、`day_es_ratio_hi` / `_lo`、`day_distinct_ratio(Volume)`(手数栅格)。
   每条都必须自带「条件标准化 + 时序归约」两层(§1.6 第 1 条),否则过不了 `distinct ≥ 0.5`。
   方向一律交给 `sign`。—— 这条的好处是:被测量和 M 的 head 不同,**不容易被最终去重顶掉**(§4.0)。
2. **把「中性化的形状」本身当成要搜的东西。** 奖励的中性化是全市场秩空间线性投影;
   M 第 2 批证明「分位内」能把同一个量从负做到正。可以系统地试条件化的**各种形状**:
   `cs_bucket_rank` / `cs_bucket_demean`(保留量纲)/ 双层分桶(市值 × 股龄、市值 × 板块)/
   `cs_flip_by_state`(按全市场成交热度翻转)/ `cs_state_rank`。
   注意第 1 轮文献 Q3-3(DGTW 1997 的特征匹配、Fama-French 2008 的三档断点、Banz 1981 的「效应集中在最小一档」)
   给的正是这一条的文献依据,而且**当时提的「把中性化换成分桶内条件秩」被 M 独立做出来并且成了最强 head** —— 这条先验罕见地站住了。
3. **把「变慢」这件事和「峰值」分开。** §1.6 第 3 条:外围 `ts_max` 堆叠在这个奖励(15bp、十分位纯多头)里
   主要是降换手。如果 R 的 B 组证实「平均和峰值一样好」,那么 N 可以直接搜**低换手的构造**:
   长窗口中位数 / 衰减加权 / `cross_quantile_q50(·, 241)` 这类,配上 hl = 20。
   (这一条和第 1 轮 N 位 31 个过线者的来历一致 —— 它们过线靠的就是长短窗口搭配,不是机制。)

**建议的本轮配置**:1 个 E(核心 1)+ 1 个 N(灵感 1)。
理由:E 的 must-contain 把被测量钉死在 `day_distinct_ratio(Ret)` 上,**只有 N 能换被测量**;
而按 §4.0,「换被测量」是本组最不容易被 M 顶掉的增量来源。PLAN §2.5 的「3 轮至少 1 个 N」第 1 轮已满足,所以两个 E 也合法,
但两个 E 会落在同一条轴上(§4.1 末),不如 E + N。
**N 的风险要先写进笔记**:N 位没有家族控制,只有库禁令(ρ ≥ 0.7 或骨架相同)。
`day_X_ratio` 换一个算子名骨架就不同了,所以近亲(ρ 0.5–0.7)能进本组的库,但在最终去重时会被排在前面的 M 顶掉。
→ N 的种子必须让**被测的量真正不同**,不是 `day_distinct_ratio` 的近亲。

---

## 5. 文献题目(交给文献员,只用 2023-08-08 之前发表的)

**Q1(对准核心 1 / 核心 2 的被测量:分钟级价格栅格粒度)**
一只股票一天里「走过多少个不同的价位 / 多少个不同的分钟收益」这类**价格离散性 / 栅格粗细**的度量,
文献里是怎么构造和处理的?具体想知道:(i) 它主要被当成什么的代理 —— 相对最小变动价位(一跳占价格的比例)、
流动性(零收益天数比例那一派)、还是价格聚集 / 整数关口行为?(ii) **归一化**怎么做 —— 除以价格、除以一跳、
还是在规模 / 成交额分组内比较?(iii) 时间维度怎么聚合 —— 均值、**滚动最大值**、还是持续性?
(iv) 有没有做过横截面收益预测,有没有在控制了流动性与波动之后还有残值的证据?
中文关键词:最小变动价位、一跳、价格离散性、报价栅格、价格粒度、零收益天数比例、价格聚集、整数关口、低价股的流动性代理、分钟级流动性。
English: relative tick size, tick size as a fraction of price, price discreteness / price granularity, number of distinct prices visited,
price clustering, proportion of zero returns (Lesmond-Ogden-Trzcinka), zero-return illiquidity, minimum tick binding, tick size pilot,
Amihud illiquidity, China A-share microstructure.

**Q2(对准本种子最强的那个「处理手法」:分位内条件标准化 + 自身历史标准化 + 滚动峰值)**
第 1 轮已经问过「市值中性化残留的非线性」(得到 Banz 1981 / Fama-French 2008 / DGTW 1997),
本轮要问的是**标准化与聚合的具体做法**,不要重复那三条:
(i) 把一个特征先**按规模分桶、桶内做 z 分 / 条件秩**(而不是全市场回归残差)—— 文献里这种「组内标准化」
和「回归正交化」被比较过吗,结论差在哪?序贯排序(conditional / sequential sort)与独立排序(independent sort)各在什么时候用?
(ii) 把一个特征**按它自己的历史**标准化(相对自身近期均值 / 分位的「异常」水平,例如异常换手 —— Gervais-Kaniel-Mingelgrin 的高成交量溢价),
文献里有哪些这样的构造,效果比用水平值好在哪?
(iii) 用一个特征在过去 1–6 个月的**滚动最大值 / 近期峰值**(而不是均值)当信号 —— 文献里有这种用法吗
(52 周最高价的锚定效应、MAX 这类「极值」信号,但那些是**收益**的极值;我问的是**特征本身**的极值)?
(iv) 把 (i) 和 (ii) **叠起来**(先按同行分组去水平,再按自身历史去水平)有没有先例?
中文关键词:组内标准化、分桶内 z 分、条件排序、序贯排序 vs 独立排序、特征正交化、按自身历史标准化、异常换手率、
高成交量溢价、滚动最大值、近期峰值、52 周最高价、锚定效应。
English: within-group standardization, bucket demeaning / within-size z-score, conditional vs independent double sort,
sequential sorting, orthogonalized vs raw characteristics, standardizing a characteristic by its own trailing mean/sd,
abnormal turnover, high-volume return premium (Gervais, Kaniel & Mingelgrin 2001), running maximum of a characteristic,
52-week high (George & Hwang 2004), anchoring.

**Q3(对准来源 B:把规模最大的 5% 单独剔到最底 = 非单调的规模处理)**
规模效应的**非单调性**与「剔除某一端」的做法,文献里是怎么处理和报告的?
具体:(i) 有没有证据说规模效应是 **U 形 / 杠铃**(最大和最小两端都好),而不是单调递减?
(ii)「剔除最大(或最小)x% 的股票池」这种处理在文献里怎么做、为什么做(NYSE 断点、剔除微盘、剔除大盘、等权 vs 市值加权)?
(iii) 指数成分股 / 超大市值这一端有没有被单独当成一个效应(指数纳入、被动资金、机构持股集中)?
(iv) 一个因子如果只在剔除了最大一端之后才有效,文献里会怎么判它 —— 真效应还是池子构造的产物?
中文关键词:规模效应非单调、规模溢价 U 形、微盘股、剔除最大市值、剔除微盘、市值分组断点、等权与市值加权、指数成分股效应、指数纳入。
English: non-monotonic size effect, size premium U-shape / barbell, microcap exclusion, excluding the largest percentile,
NYSE size breakpoints, equal- vs value-weighted size portfolios, mega-cap underperformance, index membership / index inclusion effect,
institutional ownership concentration and size.

**Q4(对准 N 灵感 1:非波动类的日内「形状」统计量)**
除了已实现波动率之外,**日内形状**类统计量有哪些被证明能预测横截面收益?
具体想知道这几类的构造与处理:(i) 日内成交的**时间分布**(早盘 / 尾盘占比、收盘集合竞价占比、成交重心、日内动量);
(ii) 成交的**集中度 / 不平均度**(基尼、前若干分钟占比、大单占比的分钟级代理);
(iii) **停滞 / 无成交分钟的占比**与最长停滞段(日内流动性空洞);
(iv) 在日内最高 / 最低价附近**停留的时间占比**(而不是极值本身的大小)。
每一类请注明:用什么做分母 / 怎么归一化(除以当日总量、按规模组内比较、还是相对自身历史),
以及是不是在控制了流动性与波动之后才报的结果。
中文关键词:日内成交分布、尾盘成交占比、收盘集合竞价、日内动量、日内反转、成交集中度、大单占比、无成交分钟、
日内流动性、分钟级特征、日内形状。
English: intraday volume distribution, U-shaped intraday volume, closing auction share, intraday momentum
(Gao, Han, Li & Zhou), last half-hour return, trade concentration / Gini of intraday volume, large-trade share,
fraction of zero-volume minutes, intraday liquidity gaps, time spent at the daily high/low, minute-level firm characteristics.

---

## 附:给 PI 的六句话

1. **本种子第一次有了真东西,而且不是我们挖出来的 —— 是 M 第 2 批。**
   `cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap)` 这一族:必要性 +2.19(去掉就从 +1.45 变 −0.73)、
   窗口 20 / 40 / 80 都 ≥ 1.16、train 1.47 / valid 1.45、ρ_known −0.21。它是唯一一条既不是静态风格、也不是控制变量变形的轴。
2. **第 1 轮的两个 head 都在静态股本轴上,按 PLAN §3 的去重顺序(M 在前、ρ ≥ 0.7 或 ≤ −0.5 就丢),
   它们彼此很可能只剩一个,还随时会被 M 第 3 / 4 批顶掉。** 别把第 1 轮算成 2 个产出。
   本组真正的增量只能来自与 M 的 6 个 head 低相关的东西 —— E 的家族控制正好替我们强制这一点,所以这轮要选**家族非空**的核心。
3. **第 1 轮的机制先验全错,工具层面的判断全对。** 名义股价轴三种写法(cap/shares −2.00、`cs_regres` 残差 −1.17、
   `inv(inv(·))` −0.12)全废,起作用的是规模的曲率;MAX 效应 −1.22;16 条 `LimitWidth` 种子没留下任何比全池均值好的后代。
   而「GP 会掉回同一个簇」「同位内的 head 互相高相关」这两条都应验了。写这一轮时按这个权重分配信心。
4. **共性表这一轮不能直接读**:320 个候选来自 4 次过线率差一个数量级的运行,Br1b(31/84 过线)的任何部件都会自动拿到 ≈ +1.0 的「均值差」。
   机械核心卡第 6–15、21 位全是这个假象。可信的只有 23 次付费拆解,以及共性的**负号那一侧**。
5. **R 这 16 次必须写满**(第 1 轮 64 次全废,本轮拆解又只花 23/48)。§2.3 给了 16 条,其中
   `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40), 80)` 已经实测 **+0.86 > head 的 +0.82**(只差 0.055 没到替换门槛),
   顺着 120 / 两层都加长走是最可能真替换成功的一条;C 组 5 条字段替换是工具因为换表里没有 `Ret` / `LogFloatCap` 而漏掉的,
   它们能回答「§1.1 是真机制还是分位内的流动性」这个本实验最要紧的问题。
6. **写 E 的种子时三条硬约束**:(i)「再堆 `ts_max`」和「再做一次双重 `cs_bucket_zscore`」的外围**已经被 M 走过**,
   会被外围新颖性拒掉,必须换算子名;(ii) 以比例 / 形状类量为被测量时,必须自带「条件标准化 + 时序归约」两层,
   否则 `distinct < 0.5` 过不了闸门,而闸门失败照样烧预算;(iii) 深核心能用(GP 的 `max_depth = 4` 不管交叉子代,种子上限是 9),
   但 must-contain 的漏损实测约 20–30%(`inv(LogFloatShares)` 那一轮:84 个已评分里约 23 个不含核心),核心越深越糟。
