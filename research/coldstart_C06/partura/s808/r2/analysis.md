# 结构解剖:种子 808,C 组,第 2 轮

快照 4 份:`c05s808M1_I0_open_search`、`c05s808M2_I0_open_search`、`c06s808Cr1a_Na`、`c06s808Cr1b_Nb`;
6 个 head、293 个已评分候选、拆解 **23 次**付费评估、R 候选 0 个、已生效的 R 替换 0 个。

**先说证据等级**(本轮能拿来说话的和不能的):

| 证据 | 有 | 没有 |
|---|---|---|
| 共性(enrichment) | 27 行,n_with 4–34 | — |
| 充分性(子树单独评分) | H1 / H2 / H4 的各级子树都测了 | H5、H6 一次没测 |
| 必要性(跳算子) | H1 两处(+1.10、+2.19)、H4 一处(+0.77) | H2 的唯一一处 knockout 撞闸门(无数字);H3 的 knockout 撞闸门;H5、H6 没有 |
| 敏感性·窗口 | H1 / H2 / H4 各试了 40→20、40→80 | H3 没有窗口可试 |
| 敏感性·换同类字段 | **只有 H3 一处**(`Open`→`Close`) | **离散度那一族(H1/H2/H6)一次换字段都没测** —— 本轮最大的证据缺口 |
| 与 5 个控制的相关度 | 没有(本轮 corr 表还没算);只有拆解表里的 `rho_known`(与已知族,已交易口径)可作参考 | 与 size / vol / liq / rev 的 ρ 全部未知 |

下文凡是没有实测数字支撑的,都标「推断」。引用的表达式都写原文。

---

## 1. alpha 的来源

### 1.1 六个 head 其实是两条轴(库的有效多样性 ≈ 2)

| head | score(train / valid) | 轴 | 判定 |
|---|---|---|---|
| `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)), 40), 40)` | +1.45(1.47 / 1.45) | B 日内离散度 | **最可能的真来源**,但有陷阱 1/3 的变体风险 |
| `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40), 40)` | +0.82(0.82 / 1.36) | B | 同上,是 H1 的内层 |
| `sub(LogFloatShares, day_flat_run_max(Open))` | +0.79(0.85 / 0.79) | A 静态股本 + B 停滞 | 八成是 A,B 只贡献边际 |
| `ts_max(ts_max(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), 40), 40)` | +0.74(0.74 / 0.76) | A(纯市值) | **陷阱 3,教科书级,见 §1.4** |
| `cross_mean(cross_quantile_q50(cross_tail_mean_q75(cross_quantile_q50(cross_mean(LogFloatShares, 15), 241), 15), 241), 15)` | +0.57(0.57 / 0.90) | A | **代理**:比裸水平还差,见 §1.2 |
| `ts_max(cs_bucket_zscore(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), ts_max(cs_bucket_zscore(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), LogFloatCap), 40)), 40)` | +0.56(0.74 / 0.56) | A(纯市值) | 同 H4,再套一层 H1 的自条件写法;零证据 |

**两条轴,不是六个。** 这件事对最终比的「因子库样本外表现」是第一位的:4 个 head(H3/H4/H5/H6)都是同一条静态规模轴的不同写法,
2 个(H1/H2)是同一条日内离散度轴的不同层。

为什么库禁令没挡住:`scripts/idea_search.py:484-496` 的 head 选取是**每个任务内部**做的 ——
先要求 |ρ_pool| < 0.5 且 |ρ_known| < 0.5,再在**本任务自己的 heads 列表内**贪心去重(ρ < 0.7),
库禁令(`c05_round.py:9`)用的是**快照的库**(第 1 轮时 M1 的 heads = 空)。
所以**同一轮里两个并行任务的 head 之间没有任何去重**:`c06s808Cr1a_Na` 的 H3 和 `c06s808Cr1b_Nb` 的 H5 都是 `LogFloatShares` 的函数,
谁也没拦谁。这解释了「过线 9 / 21,各只入 1 个 head」却还是收进两个同轴 head。
→ **给 PI 的第一条操作建议**:本轮两个位不要对着同一条轴,并行位之间不互相去重,撞车的代价要自己付。

### 1.2 轴 A(静态股本 / 规模):第 1 轮「名义股价」的假设被证伪

第 1 轮 `r1/analysis.md` §1.4 把那一簇的身份押在 **(a) 名义股价占六成、(b) 规模的非线性残差占四成**。
本轮有了直接数字,**要反过来**:

| 表达式 | n_with | mean_with | 口径 |
|---|---|---|---|
| `cross_sum(div(LogFloatShares, 5), 5)` | — | **+0.6046**(train 0.6046 / valid 0.8660, hl 5) | 单个候选,≈ 流通股本的 5 日均值,即**裸水平** |
| `cross_sum(mul(LogFloatShares, 1), 5)` / `cross_sum(div(LogFloatShares, 1), 5)` | — | +0.6046 | 同一个东西的另两种写法,分数到小数点后四位相同 |
| `cross_tail_mean_q75(LogFloatShares, 15)` | 14 | +0.531 | 共性 |
| `inv(LogFloatShares)` | 14 | +0.476 | 共性(第 1 轮那一簇) |
| **`sub(LogFloatCap, LogFloatShares)`** = log 未复权股价 | **5** | **−0.227** | 共性 |
| **`cs_bucket_rank(sub(LogFloatCap, LogFloatShares), LogFloatCap)`** = 市值桶内的价格秩 | **4** | **−0.288** | 共性 |

三件事连起来看:

1. **裸水平就值 +0.60**,已经过了 0.5 的发现门槛。第 1 轮说「整簇卡在 0.465–0.486 过不了门槛」是口径误读:
   那是**含该子树的候选的均值**,里面带着别的垃圾;一元单调包装在 hl=0 下不改秩、不改分(`r1/analysis.md` §1.1 的推理本身没错),
   所以干净写法的分数应该都是 +0.60 左右。M 第 1 批 0 个 head,不是因为这个因子不够强,而是因为 **91 个候选里没有一个干净的写法**。
   门槛 0.5 正好切在这个因子的边上,「包装得干不干净」决定了它是不是 head —— 这是本种子最关键的一条量化事实。
2. **把名义股价显式写出来,反而是负的**(−0.227 / −0.288),而且 `cs_bucket_rank(…, LogFloatCap)` 版本第 1 轮的相关度表证明它很干净
   (size 0.000、vol 0.056、liq 0.274、rev 0.089、known 0.223)。所以**不是「市值桶内排序把价格轴也洗掉了」,而是价格轴本身在这个奖励下不值钱**。
3. 于是 `rank(LogFloatShares)` 对 `rank(LogFloatCap)` 取残差后剩下的那部分,**不能**是 −log 价格:
   如果是,它和显式价格轴只差一个全局符号,而符号由 `sign` 自由选,两者的 score 应该接近,实测相差 0.85。
   代数上 `LogFloatCap − LogFloatShares = log(未复权价)` 是精确的,但奖励做的是**秩空间的线性**投影:
   `rank(股本)` 与 `rank(市值)` 的秩相关很高,残差小而且被两者**非线性**失配的那部分主导;
   `rank(价格)` 与 `rank(市值)` 的秩相关低,残差几乎就是价格本身。两条残差不是彼此的相反数。

**结论(1A)**:轴 A 的身份是**线性市值中性化挡不住的规模非线性暴露**(规则 §4 陷阱 3),不是名义股价。
先验从 (a) 六成改成 **(b) 约八成五、(a) 约一成五**(留的一成五是「低价股的壳价值 / 退市风险」这类与价格相关但不等于价格的东西,
它们会在价格轴的两端都表现得不单调,因此不会被 `cs_bucket_rank` 的桶内均匀化完整保留)。
旁证:拆解表里 `ts_max(ts_max(ts_max(LogFloatCap, 40), 40), 40)`(纯市值)的 `rho_known = −0.5527` —— 纯规模轴与已知族的相关已经越过 0.5,
这也是为什么 M 的 GP 必须把它写歪了才能过 head 选取的 |ρ_known| < 0.5 关卡(§1.4)。

**结论(1A′)**:`sub(LogFloatShares, day_flat_run_max(Open))`(H3,+0.79)= 裸水平(+0.60)+ 日内停滞项(+0.19)。
`day_flat_run_max` 的值域是 [0, 1](`ops_ext.py:415`,最长不动分钟数 / 有效分钟数),而 `LogFloatShares` 的截面跨度约 9 个 log 单位,
**两者相减的权重纯粹是量纲的偶然**(`r1/analysis.md` §1.3 那条「加减结构里 log 规模字段说话」在这里只对了一半:
扰动虽小,但相邻股票的股本差只有千分之几个 log 单位,一个 [0,1] 的扰动足以把一只股票挪动几百个秩位)。
这个权重没人选过,是 R 的现成目标(§2、§4.2)。

### 1.3 轴 B(日内价格离散 / 停滞):本种子最强、也最该深挖的一条

先把算子读准(`partura/ops_ext.py:607`):

> `day_distinct_ratio(x)` = 当日有效分钟里**不同取值的个数 / 分钟数**。1/n = 一整天一个价,1 = 每分钟都不同。
> 源码注释自己写着:"On a price: how many price levels the day visited — **coarse for low-priced stocks on a one-tick grid**"。

作用在 `Ret` 上就是「当日分钟收益取到过多少个不同值」。机械上它同时随三件事上升:
(i) **相对最小变动价位变细**,即 0.01 / 未复权股价变小(高价股的收益网格更密);
(ii) **成交笔数 / 活跃度**上升(死掉的分钟收益恒为 0,只占一个值);
(iii) **日内波幅**变大(以 tick 计的区间更宽)。
注意价格字段是后复权的,但「不同取值的个数」对当日的乘性复权因子不变,所以 (i) 这条通道是真的,不是复权造成的假象。

实测:

| 表达式 | distinct | gate | score | train / valid | sign | rho_known |
|---|---|---|---|---|---|---|
| `day_distinct_ratio(Ret)` | 0.0617 | **否** | — | — | — | — |
| `cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap)` | 0.4331 | **否** | — | — | — | — |
| `ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)` | 0.9614 | 是 | **+0.5845** | 0.5845 / 0.9046 | **−1** | +0.3814 |
| `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40), 40)`(H2) | — | 是 | +0.8156 | 0.8156 / 1.3634 | **−1** | +0.3501(20 日版) |
| `ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)), 40)` | 0.9065 | 是 | **+1.1656** | 1.1656 / 2.0057 | **+1** | −0.2071 |
| H1(上面那个再套一层 `ts_max@40`) | 0.9220–0.9445 | 是 | +1.45 | 1.47 / 1.45 | **+1** | −0.119 ~ −0.175 |
| 共性 `day_distinct_ratio(Ret)` | — | — | 均值差 +0.86,p 0.004,**34 个候选含它**,含 +0.196 / 不含 −0.662 | | | |

**(a) 三条必要性 / 充分性证据**

- 内层的 `cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap)` 跳掉(改成按自己的 40 日最大值分桶):
  `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(day_distinct_ratio(Ret), 40)), 40), 40)` → **score −0.7333,必要性 +2.19**。
  也就是说「**相对于同市值档的同行**来衡量离散度」是整个 head 的命门;换成「相对于自己最近的水平」直接变负。
- 中间那层 `ts_max@40` 跳掉 → `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap)), 40), 40)`
  → score +0.3543,必要性 +1.10。
- 外层整个 `cs_bucket_zscore` 拿掉 → `ts_max(ts_max(day_distinct_ratio(Ret), 40), 40)`,distinct 0.0584,**撞闸门,没有分数**。
  所以「离散度的纯水平」在本环境里**无法单独评估**,充分性这一格永远是空的。

**(b) 窗口稳健**:H1 的外层 40→20 给 +1.27,40→80 给 +1.16;H2 的外层 40→20 给 +0.79,40→80 给 **+0.86**(比原 head 还高)。
20/40/80 三档都远在门槛之上 → 这不是一个靠窗口凑出来的东西,**是一个慢变的股票特征**,不是事件。
(`ts_max(ts_max(·,40),40)` 的有效窗口是 79 天,三层是 118 天。)

**(c) 换同类字段:一次都没测。** 这是本轮最大的缺口。同族可替换的算子在 `ops_ext.py` 里现成有:
`day_zero_ratio(Ret)`(恰好为 0 的分钟占比,注释明确说在 `Ret` 上就是「价格没动的分钟」)、
`day_flat_ratio(Open/Close)`(与上一分钟相同的占比)、`day_flat_run_max`(最长不动段)、`day_at_max_ratio` / `day_at_min_ratio`。
H3 用的正是这一族的另一个成员,而且 `Open`→`Close` 的换字段测试是稳的(+0.79 → +0.83)。
**两个任务、两个不同算子、各自独立地撞到同一条轴**,这是本种子唯一的「汇合证据」,也是我判定它是真来源的主要理由。

**(d) 方向在三处不一致,而且这件事有解释。** H2(水平的 79 日最大值)sign = **−1** → 多头腿是**相对同市值档最不离散 / 最停滞**的票,
这是经典的流动性溢价多头腿;H1(再按自己近期水平分桶后 z 化)sign = **+1** → 多头腿是**相对自己近期异常离散**的票;
H3(`sub(LogFloatShares, day_flat_run_max(Open))`,sign +1)多头腿是股本大且**不停滞**的票。
H1 把 H2 的输出当分桶变量,等于把「水平」变成了「相对自身近期的创新」—— **水平与创新符号相反**,
这正是 Amihud(2002)那一支文献里「非流动性水平」与「非流动性冲击」的区别。
H1 的分桶变量是**市值条件化之后**的量,组内各市值档混杂,因此对组内原始离散度再做 z 化会把一部分规模倾斜带回来(推断,未测)。

**(e) 必须说清的陷阱风险(给 PI 和审计用)。** `day_distinct_ratio` 是一个**有界、饱和**的函数,
吃进去的是波动 × 活跃度 × tick 网格。奖励的 5 个控制里,波动 `cross_mean(day_std(Ret), 20)` 和流动性 `cross_mean(day_sum(Amt), 30)`
只会被**线性**去掉;一个饱和函数的非线性部分留得下来 —— 这就是规则 §4 陷阱 1 / 陷阱 3 的同一个机制,只是凸变换换成了饱和变换。
「按市值分桶」挡不住这条通道,因为它处理的是规模,不是波动和流动性。

**能把真来源和代理分开的判别式(本轮就该买)**:把条件轴从 `LogFloatCap` 换成控制本身 ——
`cs_bucket_zscore(day_distinct_ratio(Ret), cross_mean(day_std(Ret), 20))`、
`cs_bucket_zscore(day_distinct_ratio(Ret), cross_mean(day_sum(Amt), 30))`,
以及把 tick 通道显式除掉:按**未复权均价** `div(day_sum(Amt), day_sum(Volume))` 分桶
(`alphacube/daily.py:25`:价格后复权、`Amt`/`Volume` 原始,所以这个比值是未复权均价;第 1 轮相关度表已验证过这条写法与 size 的 ρ = 0.000)。
- 若在 vol / liq 桶内 score 基本不掉 → 轴 B 是**真来源**,是「同波动同流动性的同行里,谁的价格网格更粗 / 更停滞」。
- 若掉到 0.3 以下 → 它是波动 / 流动性控制的非线性重写,整条轴要降级成代理。
这同时也是 E 位外围最值钱的一件事(§4.1)。

### 1.4 `cs_last_high05(LogFloatCap, LogFloatCap)`:陷阱 3 的教科书例子,有数字

读源码(`ops_ext.py:339` 的 `_lexi` + `:395`):`cs_last_high05(y, x)` = `rank(y)`,再把 `x` 处于最高 5% 的**整个平手块**减 1 压到底部。
这里 `y = x = LogFloatCap`,所以它**就是**「市值的截面秩,但把最大的那 5% 挪到最底下」—— 一个纯粹的、分段的、非单调的市值改写,
**不含 `LogFloatCap` 之外的任何信息**。

| 表达式 | score | train / valid | sign | rho_known |
|---|---|---|---|---|
| `cs_last_high05(LogFloatCap, LogFloatCap)` | +0.1932 | **1.1948 / 0.1932** | −1 | +0.3084 |
| `ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40)` | +0.4014 | 1.3983 / 0.4014 | −1 | +0.3529 |
| `ts_max(ts_max(…, 40), 40)` | +0.5801 | 1.0974 / 0.5801 | −1 | +0.3578 |
| `ts_max(ts_max(ts_max(…, 40), 40), 40)`(H4) | +0.7448 | **0.7448 / 0.7650** | −1 | +0.3626 |
| knockout:`ts_max(ts_max(ts_max(LogFloatCap, 40), 40), 40)`(把拐点去掉) | **−0.0274** | −0.0274 / 0.4017 | +1 | **−0.5527** |

两条读数:

1. **拐点就是全部 alpha**:去掉 `cs_last_high05` 只剩纯市值,score 从 +0.74 掉到 −0.03(必要性 +0.77)。
   而拐点本身不带任何新信息,它只是把市值秩折了一下。
2. **拐点的作用是让一个市值因子绕过资格线**:纯市值的 `|rho_known| = 0.55`(> 0.5,head 选取会直接拒),
   折一下以后 `|rho_known| = 0.31`。规则 §1 的「与已知族 |ρ| ≥ 0.5 判为不合格」和 head 选取的 |ρ_known| < 0.5,
   都是**线性 / 秩相关**口径,一个非单调改写就能把同一个暴露压到线下。

**结论(1B)**:H4 与 H6 不是发现,是**被改写过的市值控制**。它们目前占库里 6 个 head 的两个。
H4 的 train/valid 还有一个值得记下的形状:窗口越长 train 越低、valid 越高(单层 1.40/0.40 → 三层 0.74/0.77 → 80 日版 0.35/0.75),
而 score = min(train, valid),所以 GP 实际上是在**搜「两条腿交叉的那个窗口」**—— 恰好是估计最不稳的地方。
这是 score 口径自带的一个选择偏差,库里所有靠 min 拉上来的 head 都该打折看(H1 train 1.47 / valid 1.45、H3 0.85/0.79 这种两条腿都高的才算结实)。

### 1.5 一个必须写进笔记的机制:`ts_max` 在这里是**闸门的开门器**,不是平滑器

`gate = coverage ≥ 0.9 且 distinct_fraction ≥ 0.5`(`scripts/c05_locate.py:162`)。实测的 distinct:

- `day_distinct_ratio(Ret)` 0.0617(值落在 k/241 的网格上)→ 挡死;
- `cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap)` 0.4331(10 个桶各有自己的均值和标准差,把平手块拆成 10 份)→ **还是差一点**;
- 再套一层 `ts_max(·, 40)` → **0.9614**,过;
- 但 `ts_max(ts_max(day_distinct_ratio(Ret), 40), 40)` 只有 0.0584 —— 离散网格取最大值还在网格上。

所以这个结构的层次是:**桶内 z 化把值变成「股票 × 日 × 桶」三者的函数,40 日最大值再把不同日子的分母混进来,distinct 才够**。
这是陷阱 2「借 distinct 门槛」的一个新变种(规则 §4 写的是 `cs_last_high*(<常数>, X)` 那一类),
区别在于这里**同时**有真实的条件化内容,所以它不是纯粹的作弊。
推论(对所有后续写法都适用):**任何有界离散的日内比例类特征(`day_zero_ratio`、`day_flat_ratio`、`day_flat_run_max`、`day_at_*_ratio`)
单独写一定过不了闸门**(实测:`day_flat_run_max(Open)` distinct 0.0217),必须配一个多日 `cross_*` 平均、或一个带条件的截面算子,
或者乘进 / 减进一个连续载体(H3 正是后者)。写种子前先在心里过一遍 distinct。

### 1.6 汇总:真来源 vs 代理

| 轴 | 判定 | 最硬的证据 | 最大的未知 |
|---|---|---|---|
| B 日内价格离散 / 停滞(`day_distinct_ratio`、`day_flat_run_max`) | **真来源**(两个任务独立撞到;窗口 20/40/80 都稳;条件化的必要性 +2.19) | §1.3(a)(b)(c) | 与 vol / liq 控制的 ρ 未测;换同类字段未测;是否被涨跌停封板与停牌日主导未测 |
| A 静态规模(`LogFloatShares`、`LogFloatCap`) | **代理**:线性市值中性化挡不住的非线性规模暴露 | 裸水平 +0.6046 vs 显式价格轴 −0.227 / −0.288;纯市值 rho_known −0.55 | 「低价股壳价值 / 退市风险」这一小块无法与规模分开 |
| A′ `cs_last_high05(LogFloatCap, LogFloatCap)` | **纯代理 + 陷阱 3** | 必要性 +0.77 却不含任何新字段;rho_known 0.55 → 0.31 | 无 |
| 名义股价 | **本轮基本排除** | −0.227(n=5)、−0.288(n=4),且相关度表证明写法干净 | 未复权均价 `Amt/Volume` 的 20 日版只测过桶内秩,没测过与离散度的交互 |
| 分钟量价动态(CGW / LMSW) | **第 1 轮已试,失败** | 见 §3.2 | — |

---

## 2. 烂部件

按规则的严格定义(必要性 ≤ 0,或换掉反而更好),本轮**实测**到的只有三处,全都小于 R 的 +0.1 收录门槛,得组合着用:

1. **H3 的 `Open`**:`sub(LogFloatShares, day_flat_run_max(Open))` +0.7948(0.846/0.795)→
   `sub(LogFloatShares, day_flat_run_max(Close))` **+0.8261**(0.840/0.826),必要性 −0.03,两条腿还更平。
   `Open` 是分钟 bar 的开盘价,`Close` 是分钟收盘价;在「最长不动段」这个度量上 `Close` 更贴近「报价没动」。
2. **H5 的四层嵌套平滑**:`cross_mean(cross_quantile_q50(cross_tail_mean_q75(cross_quantile_q50(cross_mean(LogFloatShares, 15), 241), 15), 241), 15)`
   = +0.5662,而同一个静态字段的**裸 5 日均值** `cross_sum(div(LogFloatShares, 5), 5)` = **+0.6046**。
   静态字段上叠 5 层 15/241 日平滑**净亏 0.038**。这是「换掉(去掉)反而更好」的一个干净例子,
   也印证 `r1/analysis.md` §2 那条推论:静态字段外面的归约层都是烂部件。
3. **H2 的外层窗口 40→80**:+0.8156 → **+0.8607**。但这条要小心:单纯把窗口往外推是「数字游戏」,
   审计按合理度 1 处理;除非和一个机制理由绑在一起(例如「流动性是慢变量,118 日的极值比 79 日更接近水平」),否则别拿它当 R 的主理由。

**没有实测必要性的「结构性烂部件」**(score 为正,但部件本身不带信息,属于陷阱):

4. **`cs_last_high05(LogFloatCap, LogFloatCap)`(H4、H6)**:§1.4。必要性 +0.77,但它只是把市值秩折了一下,
   作用是把 |rho_known| 从 0.55 压到 0.31。R 的正确做法不是删掉它(删了变 −0.03),而是**把退化的 `y` 换成真信号**,
   让它回到源码注释里本来的用途(`ops_ext.py:356-364`:"'Trade y only where x is low' as an expression … 用在解剖说明信号只在某一段里选股的时候")。
5. **H6 整棵树**:`ts_max(cs_bucket_zscore(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), ts_max(cs_bucket_zscore(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), LogFloatCap), 40)), 40)`
   = 陷阱 3 的内核 + H1 的自条件写法,**23 次拆解一次都没碰它**,score 0.56 是六个 head 里最低、train/valid 0.74/0.56 也最不平。
   零证据 + 两个已知陷阱叠加,我建议 PI 把它当「待删」而不是「待挖」。

**明确不是烂部件,别去动**(必要性为正且有数字):H1 的内层 `cs_bucket_zscore(…, LogFloatCap)`(+2.19)、
H1 的中层 `ts_max@40`(+1.10,而且是闸门的开门器,去掉直接无分数)、H1 外层的第二个 `ts_max@40`(去掉 1.45 → 1.17)、
H4 的三层嵌套(单层 0.40 / 双层 0.58 / 三层 0.74)。

---

## 3. 之前的任务

### 3.1 E:一个都没有

第 1 轮两个位都是 N(`r1/missions_final.yaml`),理由写在 `r1/analysis.md` §1/§4:当时快照 0 个 head,
7 个合法核心全是 `LogFloatShares` 的包装,判断它们与市值控制的秩相关大概率 ≥ 0.5、E 位会被「核心是控制的替身」直接挡掉。
**所以没有任何核心被用掉过 E 位**,「每个核心至多 2 个 E 位」的额度本轮全额可用。
R 也是 0(代码层面不可能:`heads` 为空集)。按 `r1/analysis.md` §2 的记账,第 1 轮 48 次拆解 + 16 次 R 共 64 次评估确实白费了。

### 3.2 N 的结果:两个位都通过了审计,**也都没有用上自己的假设**

| 任务 | 假设 | 评分 | 过线 | 入 head | 实际的 head |
|---|---|---|---|---|---|
| `c06s808Cr1a_Na` | 名义股价幻觉,市值桶内排序 | 77 | 9 | 1 | `sub(LogFloatShares, day_flat_run_max(Open))` |
| `c06s808Cr1b_Nb` | 分钟量价动态(CGW 1993 / LMSW 2002) | 67 | 21 | 1 | `cross_mean(cross_quantile_q50(cross_tail_mean_q75(cross_quantile_q50(cross_mean(LogFloatShares, 15), 241), 15), 241), 15)` |

- **a 位的假设被证伪**(§1.2):价格轴的两种写法均值 −0.227 / −0.288。
- **b 位的假设没有产出**:两个任务各自的前 5 名全部是 `LogFloatShares` 的 `cross_*` 嵌套,
  b 位 21 个过线者里前 5 名一个分钟量价结构都没有,`day_corr` 系列也没进共性表(含它的候选不足 4 个)。
  可以确定的是:**分钟量价那一族在本种子最高分 < +0.546,没有 head**;精确分数 `loc.json` 里拿不到。
- **两个 head 都来自 GP 自己的随机那一半**(N 位种子最多占初代一半)。手写种子在第 1 轮**零产出**,这一点要诚实记下来:
  本种子第 1 轮,Partura 的通道**输给了随机搜索**。
- 一处值得留的细节:`sub(LogFloatShares, day_flat_run_max(Open))` 的骨架 `sub(<log 规模字段>, <另一项>)`
  正是 a 位主种子 `sub(LogFloatCap, LogFloatShares)` 的骨架,相差一两次变异。
  所以**手写种子贡献的不是假设,而是「把两个字段组合起来」这个结构习惯**——
  这恰好是 `r1/analysis.md` §1.3 坚持的那一条(「91 个候选一次都没把两个字段组合起来」)。这条经验值得继续用。

### 3.3 审计员挡掉了什么,事后看对不对

a 位(创新 3 / 合理 4,划掉 4 颗,剩 8):
- 划 2、9(`cs_regres` 版):理由是「原始值的 OLS 线性残差 ≈ M 那一簇换写法,且留着本位自己说要去掉的非线性规模」。
  **事后看:对,但理由不完整**——它们和主种子的差别恰恰是「留不留非线性规模」,而本轮证明**非线性规模才是唯一值钱的那部分**(§1.2)。
  如果当时放它们进去,我们会更早看到「桶内排序 −0.29 vs OLS 残差 ?」这组对照。这是审计规则(划掉与控制等价的写法)和信息价值之间的一个真实张力,
  记在这里供第 3 轮参考:**同一机制的两种中性化写法,是分辨陷阱 3 的最廉价实验,不该被当成「换皮」划掉。**
- 划 7(按 `ListAge` 分桶):理由是 `dailyfields._list_age` 给建库前上市的股票一律记 `10000 + 天数`,同日大量平手,
  `_pct_rank` 用稳定 argsort 按列序破平手 → 陷阱 2。**对,而且源码口径准确**。
- 划 11(`MAX / LimitWidth`,与 vol 控制 ρ = 0.452):理由是 MAX 是特质波动的单调替身,秩相减后多头腿是低波动腿 → 陷阱 1/3。
  **对**。顺带:这颗是 r1 §4.5 第 3 条(交易约束轴)唯一的载体,被划掉以后那条轴至今**一次没跑过**。

b 位(创新 4 / 合理 3,划掉 5 颗,剩 7):
- 相关度表自动划掉 1、3、8、9(与 20 日反转控制 ρ 0.503–0.575),审计员另划 7(`cross_ema(day_corr(Ret, Amt), 10)` = 被划的种子 1 换皮,ρ 0.45 只因窗口更短)。
- 审计员给合理度 3 而不是 4 的三条理由(同期量价相关大半在复述反转;CGW/LMSW 是日频结论搬到分钟,会被集合竞价 bar 支配;
  `mul(Ret, Volume)` 用原始股数、皮尔逊相关被一两分钟决定)。**事后看全部成立**:保留的 7 颗没有一颗产出 head。
  这是第 1 轮审计最有价值的一次判断 —— 它提前说出了「这条线会空转」的机制理由,只是没有权力把位退回去。

### 3.4 上一轮的预测,逐条打分

`r1/analysis.md` §3 的 P1–P4:

- **P1**(只做单字段包装 / 单字段窗口归约的候选会继续落在 0.46–0.49,不会过 0.5)—— **错**。
  `cross_sum(div(LogFloatShares, 5), 5)` = +0.6046,H5 = +0.5662,都是单字段写法且都过了 0.5。错因在 §1.2 第 1 点:
  把「含该子树的候选均值」读成了「该写法自己的分数」。附带的那半句(「若 E 位产出 head,表达式里一定含第二个字段」)没有 E 位可检验;
  但两个 N 位的 head 一个含第二字段(H3)、一个不含(H5),所以这半句**也站不住**。
- **P2**(`sub(LogTotalCap, LogFloatCap)` 的 score 低于 `sub(LogFloatCap, LogFloatShares)`,且在 0.1–0.5 之间)—— **未检验**:
  自由流通比例那条没有进最终种子,共性表里也没有。但 P2 的另一半意外地被测到了:价格轴自己是 **−0.227**,不在任何人预想的区间里。
- **P3**(纯事件差分会被 distinct 闸门挡掉)—— **机制被反复证实**(`day_distinct_ratio(Ret)` 0.0617、`day_flat_run_max(Open)` 0.0217、
  `cs_bucket_zscore(…)` 0.4331 全部 gate=false),但 P3 点名的那个表达式 `sub(LogFloatShares, ts_decay_linear(LogFloatShares, 50))` 没有被评估过。
- **P4**(手写种子的 score 分布明显高于机械嫁接)—— **没有 E 位,无法按原口径检验;改用「手写种子 vs GP 随机那一半」看,结论是反的**(§3.2)。

`notebook.md` 第 1 轮的两条:
- 「M 第 2 批预计仍主要围着 `LogFloatShares` 那一簇转,可能有一个包装刚好过 0.5 进 head;若如此,第 2 轮 R 的第一目标就是它外面那层单调一元算子」
  —— **错**。M 第 2 批整体换轴,拿出 4 个 head,最高 +1.45,主结构是 `day_distinct_ratio(Ret)` 的市值条件化,
  以及 `cs_last_high05(LogFloatCap, LogFloatCap)`。「R 的第一目标是单调一元算子」因此落空(没有这种 head)。
  教训:M 的 GP 不受我们影响,**不要把下一批押在上一批的簇上**。
- 位 a 产出 head 的概率 55%、位 b 60%:各 1 个 head,数量上都对了;但两者产出的**不是**预测里的那条线(预测的主种子表达式、score 区间 0.50–0.65 / 0.5–0.8 全错位)。
- 「与彩票特征的组合预计比纯价格轴高 0.05–0.15」—— 那两颗(`day_skew` 组合)没有单独分数,共性表里没有,无法判定。

---

## 4. 本轮候选

### 4.1 值得深挖的核心(按优先级,≤ 3)

共同的硬约束,写种子前都得过一遍:
- 核心必须是快照某个 head 的子树,或 `loc["enrichment"]` / `core_cards` 里的子树(`c06_check.py:86-95`),裸叶子不算;
- **E 位要求核心与 5 个控制的 |ρ| 全部 < 0.5**(`c06_check.py:182`),这三个核心的这项数字**都还没算过**,
  → **请 PI 把三个核心全部放进 corr 请求,按结果挑一个,另两个作备选**;
- 外围新颖性只看**算子名集合**(`idea_search.py:312-317`,`frozenset`,忽略字段与窗口,空集已在 `SEEN` 里),
  `SEEN` 由流水线用「档案里所有含该核心的候选」初始化,所以**我在下面只能列出快照里看得见的那些**,实际 `SEEN` 会更大;
- 过了外围新颖性还不够:候选还要与 H1/H2/H6 的日度秩 |ρ| < 0.7 才进得了库,**只换窗口 / 只换条件轴回到市值的写法会在这一关被拒**;
- 深度:GP 自己生成的随机树 `max_depth=4`,但**嫁接是把核心替换进随机树的一个退化槽**(`idea_search.py:333-357`),
  手写种子 `seed_max_depth=9`,而 `gp.py` 对后代没有全局深度上限(`max_depth` 只给生成器用)。
  → 修正 `r1/analysis.md` §4.1 那条「深度 3 的核心只剩 1 层」:**核心深一点并不致命,手写种子该写成成品、写足深度**。

**核心 1(首选):`day_distinct_ratio(Ret)`** —— 核心卡 #14,共性 n_with=34、均值差 +0.86、p 0.004,含它 +0.196 / 不含 −0.662;深度 2。
- 为什么是它:**只有把条件轴留在外围,才能做 §1.3(e) 的判别式**。核心 2 把 `LogFloatCap` 焊在里面,外围就没法换条件轴了。
- 已见过的外围写法(算子名集合):`{}`(裸,gate 0.0617 挡死)、`{ts_max}`(`ts_max(day_distinct_ratio(Ret), 40)`,只作为分桶变量出现过)、
  `{cs_bucket_zscore}`(gate 0.4331 挡死)、`{cs_bucket_zscore, ts_max}`(H1、H2、H2 的子树、以及两个窗口变体)、
  `{cs_last_high05}`(`cs_last_high05(day_distinct_ratio(Ret), LogFloatCap)`,共性 n=7、均值 **−0.188**)。
- 没见过、而且有机制理由的外围(每一条都至少带一个新算子名):
  - 条件轴换成控制本身:`cs_bucket_zscore(day_distinct_ratio(Ret), cross_mean(day_std(Ret), 20))`、
    `cs_bucket_zscore(day_distinct_ratio(Ret), cross_mean(day_sum(Amt), 30))` → 外围加了 `cross_mean`、`day_std` / `day_sum`,新;
  - 条件轴换成**未复权均价**(把 tick 网格通道非参数地剥掉):`cs_bucket_zscore(day_distinct_ratio(Ret), div(day_sum(Amt), day_sum(Volume)))` → 新算子 `div`、`day_sum`;
  - 水平 vs 创新写成显式差,不靠自分桶:`sub(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40), cross_mean(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 60))` → 新算子 `sub`、`cross_mean`;
  - 极值换成水平:`cross_mean(…, 40)`、`cross_quantile_q50(…, 40)` 代替 `ts_max` —— 既是 H1 自条件读法的判别式,也顺手测了闸门;
  - 分段:`cs_first_low40(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40), LogFloatCap)` = 「只在小盘那 40% 里选股」,
    直接回答 §1.6 里「是不是只在最小几档有效」(Banz / Fama-French 2008 的分层配方,见 `r1/lit.md` Q3)。
- 风险:它是最生的写法,**与 vol / liq 控制的 |ρ| 最可能 ≥ 0.5**;若被挡,降级用核心 2 或 3。

**核心 2:`cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap)`** —— 核心卡 #5,共性 n_with=14、均值差 +1.29、p 0.000;
在 H1 里的必要性 **+2.19**(六个 head 里最大的一个必要性数字);深度 3。
- 已见外围:`{}`(gate 0.4331 挡死)、`{ts_max}`(+0.5845)、`{ts_max, cs_bucket_zscore}`(H1 及其子树与窗口变体)。
- 没见过且合理的外围:`sub` / `div` 与一个未复权价项或波动项组合;`cross_mean` / `cross_stddev` / `cross_quantile_q50` 的多日水平与离散;
  `cs_first_low40` / `cs_last_high05` 的分段;`mul` 乘进 `LimitWidth` 做交易约束缩放。
- 优点:必要性证据最硬,核心自带「相对同市值档」的条件化,机制好讲。缺点:条件轴焊死,做不了判别式;
  且它离 H1/H2 太近,库禁令(ρ < 0.7)会咬掉很多外围。

**核心 3(保底):`ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)`** —— 核心卡 #2,
**自身充分性 +0.5845**(train 0.5845 / valid 0.9046,sign −1),`rho_known = +0.3814`(已交易口径,**是三个核心里唯一有控制相关参考值的**),
distinct 0.9614 已过闸门;深度 4。
- 已见外围:`{}`(它自己 +0.58)、`{ts_max}`(H2 及两个窗口变体)、`{cs_bucket_zscore, ts_max}`(H1 及其子树)。
- 优点:闸门和自给自足都解决了,外围只要加价值;rho_known 0.38 < 0.5 让 E 的核心资格比较可能过关。
  缺点:它就是 H2 的子树,任何「再平滑一层」的外围都会撞库禁令。

**不要选**:`cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40))`(核心卡 #4,
均值差 +1.63 最高)—— 自条件写法,机制还没弄清是「创新」还是「锯齿重编码」(§1.3(d)),把 E 位押在没弄清的结构上不值;
`cs_last_high05(LogFloatCap, LogFloatCap)`、`ts_max(…, 40)`、`ts_max(ts_max(…, 40), 40)`(核心卡 #3/#13/#15)——
陷阱 3,而且核心与 size 控制的 |ρ| 必然远超 0.5,E 位会被 `core_is_a_control` 直接挡掉;
`LogFloatShares` 系的 6 行共性(核心卡 #6–#12)—— 同上,且已证明是代理。

### 4.2 R 目标(16 个变体怎么分)

**R 的真实价值在这一轮不只是收录**:它是我们**唯一能自己点菜**的确定性评估,而 23 次拆解把「换同类字段」这一格整个漏掉了(§1 表)。
每个目标的收录门槛(原 head + 0.1)我都标出来了。

1. **H3 `sub(LogFloatShares, day_flat_run_max(Open))`(+0.79,门槛 ≥ 0.89)—— 最有机会收录,给 6–7 个变体。**
   已知 `Open`→`Close` 值 +0.83(差 0.06 到门槛)。往上加的三条理由各自独立:
   - 换成同族里**已被证明最强**的成员:`sub(LogFloatShares, day_distinct_ratio(Ret))`、`sub(LogFloatShares, day_zero_ratio(Ret))`、
     `sub(LogFloatShares, day_flat_ratio(Close))`。注意**符号**:`day_distinct_ratio` 是「活跃」方向,`day_flat_*` / `day_zero_ratio` 是「停滞」方向,
     相减的内部相对符号**不会**被全局 `sign` 吸收,方向搞反会相互抵消(H2 说多头腿是停滞那一侧、H3 说是活跃那一侧,§1.3(d) 本来就没定论)
     → 建议同一个载体上**两个方向各写一个**,让数据说话;
   - 去掉日噪声:`sub(LogFloatShares, cross_mean(day_flat_run_max(Close), 20))`(同机制,少一半测量噪声,这是「原部件是单日值」这个烂点的正面修法);
   - 修权重:`sub(LogFloatShares, mul(day_flat_run_max(Close), 3))` 之类 —— 原写法的混合权重纯粹来自量纲偶然(§1.2 结论 1A′),
     这是一个有理由、而且审计能验证的「部件是烂的」论证。
2. **H4 `ts_max(ts_max(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), 40), 40)`(+0.74,门槛 ≥ 0.84)—— 给 4–5 个变体,目的是把陷阱 3 换成真信号。**
   烂部件的论据写 §1.4 的两行数字(拐点不含新字段;rho_known 0.55 → 0.31)。变体把退化的 `y` 换掉、保留「排除最大 5%」这个筛子本来的用途:
   - `ts_max(ts_max(ts_max(cs_last_high05(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40), LogFloatCap), 40), 40), 40)`;
   - `cs_last_high05(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40), LogFloatCap)`(不套 `ts_max`,看筛子本身加不加分);
   - 对照:把筛子换成 `cs_first_low40(…, LogFloatCap)`(「只在小盘 40% 里选」)—— 和上一条一起就能回答「是排除大盘还是只在小盘有效」。
   注意 `cs_last_high05(day_distinct_ratio(Ret), LogFloatCap)` 在档案里已有 7 个候选、均值 **−0.188**,所以**生的离散度 + 筛子不行**;
   要用的是已经条件化并过了闸门的版本。
3. **H2 `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40), 40)`(+0.82,门槛 ≥ 0.92)—— 给 3–4 个变体,买敏感性。**
   这是**用 R 买回拆解漏掉的换字段测试**:把 `day_distinct_ratio(Ret)` 换成 `day_zero_ratio(Ret)`、`day_flat_ratio(Close)`、`day_flat_run_max(Close)`。
   收录机会不大(门槛高),但这几个数字直接决定第 3 轮要不要继续押轴 B,而且它们会进相关度表,顺手把「与 vol / liq 的 ρ」也量出来。
   **不要**把变体写成单纯的窗口外推(40→120),那是数字游戏。
4. **H5(+0.57,门槛 ≥ 0.67)—— 只给 1 个变体,目的是诊断,不是收录。**
   `cross_mean(LogFloatShares, 15)`(把 4 层平滑剥掉)。它的分数大概落在 +0.60(§2 第 2 点),到不了 0.67;
   但它进了相关度表以后,我们就能读到 **ρ(裸股本水平, H3) 和 ρ(裸股本水平, H5)** ——
   如果两个都 ≥ 0.7,就确认了 §1.1 的推断:库里有一对重复 head,这件事对最终的样本外评估有直接影响,值得花一个变体去确认。
5. **不建议**:对 H1 做 R(门槛 ≥ 1.55,三个已测变体最高 1.27);对 H6 做 R(零证据、两个陷阱叠加,应该等它被替换掉而不是加固)。

### 4.3 N 的灵感

先说口径:规则 §2 要求「3 轮里至少 1 个 N 位通过审计」,第 1 轮**两个 N 位都通过了**,所以这条约束已经满足,
本轮在制度上可以 E+E。我的建议是 **E + N**:库现在只有 2 条轴,而最终比的是整个库的样本外表现,
第 3 条轴的边际价值大于同一条轴上的第 4 个 head —— 尤其因为最强的那条轴(A)已经判定是陷阱 3。

**N-1(首选):零收益 / 停滞分钟的流动性度量族,以及它的「水平 vs 冲击」。**
- 机制:日内「价格不动的分钟」是零收益 / 停滞类非流动性度量(LOT、FHT、%zero 一支),度量的是报价没有更新、
  没有成交、或封板。文献里这一支的横截面结论是非流动性溢价;Amihud(2002)一支的结论是**水平与冲击要分开**,两者符号可以不同 ——
  而本种子的 H2(sign −1,水平)与 H1(sign +1,相对自身近期)**正好给出了相反的符号**(§1.3(d)),这就是样本内的证据。
- 算子:载体用 `day_zero_ratio(Ret)`(注释明确:`Ret` 上就是「价格没动的分钟」,且与 `day_flat_ratio` 的「动了同样幅度两次」区分开)、
  `day_flat_ratio(Close)`、`day_flat_run_max(Close)`;**必须**外面套 `cross_mean(·, 20/60)` 才过得了 distinct 闸门(§1.5);
  水平写 `cross_mean(·, 60)`,冲击写 `sub(cross_mean(·, 5), cross_mean(·, 60))` 或 `cs_bucket_zscore(cross_mean(·, 5), cross_mean(·, 60))`。
- 与轴 B 的关系要在假设里讲清楚:输入同类(日内分钟价格的停滞),**算子族不同、机制讲的是水平 vs 冲击的分离**,
  按规则 §3 的表这是「同一类输入但机制不同」= 创新度 3;想要 4 很难,别硬争。
- 和控制的关系:`day_zero_ratio` 是有界比例,**和流动性控制 `cross_mean(day_sum(Amt), 30)` 的相关可能偏高**,
  这是这条线最可能被相关度表划掉的地方;先准备一个在 `LogFloatCap` 桶内条件化、或除以成交笔数代理的版本。

**N-2(备选):交易约束轴(`LimitWidth` / `BoardCode`)。**
至今一次没跑过(唯一的载体被第 1 轮审计划掉了,§3.3),而 `r1/lit.md` Q4 已经给了三条可引的证据:
`[R15]`(ST / 窄限制组的反转更强 → `LimitWidth` 当**调节变量**而不是独立因子)、`[R14]`(冷却效应,按涨停 / 跌停分别统计)、
`[R16]`(连续封板天数是独立影响因素 → 用滚动计数而不是单日旗标)。
写法上两条硬约束:`LimitWidth`(3–4 档)、`BoardCode`(4 档)**单独当因子必然被 distinct 闸门挡死**,只能做缩放 / 分组;
而且**不要用它们做 `cs_bucket_*` 的分桶变量** —— `_buckets` 走 `_pct_rank`,4 档值上会用稳定 argsort 按列序破平手,正是第 1 轮被划掉的 `ListAge` 那个坑(陷阱 2)。
用 `mul` / `div` 缩放,或者用 `_lexi` 系(`cs_last_high05` 等)—— 后者按**整个平手块**取 band,不会按列序切。
这条线还有一个本轮新增的理由:**轴 B 的度量(不动的分钟)天然会被封板和停牌污染**,
`day_flat_run_max` 的源码注释自己就举了「封在涨跌停上 240 分钟」的例子;
而标签那一侧只挡住了「次日开盘窗口封涨停买不进」这一种情况(`alphacube/label.py` 的 `buyable`、`tradability.py`),
**信号这一侧的封板日照样进特征**。把 `LimitWidth` 放进来既是新轴,也是轴 B 的对照。

**N-3(不建议单独占位)**:自由流通比例 `sub(LogTotalCap, LogFloatCap)`(P2 至今未测)。
价格轴已经证伪、规模轴已判为陷阱 3,这条大概率是规模的第三种写法;可以在别的位里搭 1–2 颗种子,不值一个位。

---

## 5. 文献题目(给文献员;只用 2023-08-08 之前发表的)

**Q1(对准核心 1–3 / 轴 B:日内价格离散与停滞)**:
文献里「**价格离散性 / 零收益分钟 / 报价停滞**」这类结构是怎么构造和处理的?
具体问:(i) 有没有用过「当日访问过多少个不同价位(或不同收益值)」、「最长不动区间」这种**计数型**度量,
还是一律用零收益占比(LOT / FHT / %zero)、价差代理(Roll)、Amihud 冲击?
(ii) 这类度量与**最小变动价位相对价格的比值**(相对 tick = tick / 价格)机械耦合,文献怎么拆开这两部分 ——
按价格分组、除以相对 tick、还是用价格聚集(price clustering)单独度量?
(iii) 控制了规模和流动性之后这类度量还有没有横截面定价能力;在 A 股的 0.01 元 tick、T+1、涨跌停制度下有没有专门结果?
中文关键词:零收益率比例、价格离散性、最小变动价位、相对买卖价差、价格聚集、非流动性度量、流动性溢价、停牌与停滞报价、A 股流动性因子。
English: zero-return proportion, LOT measure, FHT measure, price discreteness, price clustering, tick size / relative tick, number of distinct prices visited, stale quotes, illiquidity premium, Amihud illiquidity, Roll spread, China A-share liquidity measures.

**Q2(对准 H1 的自条件写法与 `ts_max` 的极值口径:水平还是冲击)**:
文献里**非流动性 / 换手 / 活跃度**预测横截面收益,用的是**水平**还是**变化(创新、冲击)**?两者的符号一致吗?
具体问:(i) 「相对自身近期水平的异常」怎么定义 —— 时间序列残差、滚动 z 化、分组内标准化、还是差分?
(ii) 用**窗口内的极值**(例如过去 2 个月的最大值)而不是均值当特征,文献里有没有先例和理由?
(iii) 「相对同规模同行」的条件化(分组内比较)与「全市场排序」给出的结论有没有被比较过?
中文关键词:非流动性水平与冲击、流动性风险、流动性冲击、异常换手率、滚动标准化、组内比较。
English: illiquidity level vs innovation, liquidity shocks, Amihud (2002) innovations, Pastor-Stambaugh liquidity risk, abnormal turnover, rolling z-score / within-stock standardization, extreme vs average of a rolling window, peer-group (within-size) conditioning.

**Q3(对准陷阱 3 / H4 / `LogFloatShares` 簇:非单调的规模暴露)**:
文献里规模效应是**单调**的吗,还是分段 / 非单调?
具体问:(i) 有没有记录过「**把最大的 X%(或最小的 X%)剔掉以后效应才出现 / 才消失**」这种拐点形状
(Banz 的「集中在最小一档」、Fama-French 2008 的 microcap 分层、NYSE 分位断点、排除微盘)?
(ii) 「对 log 市值取残差」与「在市值分组内排序」给出不同结论的具体案例有哪些,文献倾向哪一种?
(iii) 一个特征如果只在最小几档市值里有效,文献的通行处理是把它标注为规模代理,还是当独立异象?
中文关键词:规模效应非单调、微盘股、剔除极小市值、剔除大盘股、分层检验、市值中性化残差、规模分段、双变量排序。
English: nonlinear / non-monotonic size effect, microcap, NYSE breakpoints, excluding the largest or smallest X%, Banz (1981), Dissecting Anomalies, size neutralization vs double sorting, kinked size exposure, characteristic-adjusted returns.

**Q4(对准 N-1 / N-2:涨跌停与停牌对「不动」类度量的污染)**:
在**有涨跌停和停牌**的市场里,零收益 / 停滞类流动性度量会被制度性地污染,文献怎么识别和修正?
具体问:(i) 是剔除封板日和停牌日,还是把它们单独当一个特征(封板频率、连续封板天数)?
(ii) 涨跌停宽度不同的组(主板 10% / 创业板科创板 20% / ST 5%)之间,这类度量还可比吗,文献怎么归一?
(iii) 「封板频率 / 开板后的收益形状」本身作为横截面特征,有没有被检验过?
中文关键词:涨跌停导致的零收益、封板、一字板、停牌、涨跌幅限制与流动性度量、T+1、流动性度量的制度性偏误。
English: price limits and zero-return measures, limit-hit days, limit-locked, trading suspension and illiquidity measures, T+1 settlement, comparability of liquidity measures across limit regimes, China ChiNext / STAR 20% limit.

---

## 附:给 PI 的六句话

1. **第 1 轮的主假设错了,而且错得有用**:名义股价轴实测 −0.227 / −0.288,而流通股本的**裸水平**值 +0.6046。
   所以 `LogFloatShares` 那一簇不是价格轴,是**线性市值中性化挡不住的非线性规模暴露**(陷阱 3)。先验从 (a)6:(b)4 翻成约 (b)8.5:(a)1.5。
2. **库里 6 个 head 只有 2 条轴**,而且 4 个属于那条已判为陷阱 3 的规模轴;`cs_last_high05(LogFloatCap, LogFloatCap)` 是教科书例子 ——
   拐点不含任何新字段,作用只是把 |rho_known| 从 0.55 压到 0.31。H6 零证据 + 双陷阱,建议当「待删」。
3. **同一轮里两个并行任务的 head 之间没有去重**(head 选取在任务内部做,库禁令只看快照的库)。
   第 1 轮我们因此收了一对同轴 head(H3 / H5);本轮两个位**不要对着同一条轴**。给 H5 配一个变体 `cross_mean(LogFloatShares, 15)`,
   就能从相关度表里读出这对重复到底有多重。
4. **真来源最可能是轴 B:日内价格离散 / 停滞**(`day_distinct_ratio`、`day_flat_run_max`)。
   两个任务用两个不同算子独立撞到它;窗口 20/40/80 都稳;「相对同市值档的同行」这层条件化的必要性是 +2.19。
   但 23 次拆解**一次没换过同类字段**,与 vol / liq 控制的 ρ 也没算过 —— 这两件事本轮必须买回来(E 的外围 + H2 的 R 变体)。
5. **最值钱的一个实验**:把条件轴从 `LogFloatCap` 换成波动控制、流动性控制、以及未复权均价 `div(day_sum(Amt), day_sum(Volume))`。
   撑住了,轴 B 就是真来源;掉到 0.3 以下,它就是波动 / 流动性控制的**饱和型**非线性重写(陷阱 1/3 的同一个机制)。
   做这个实验需要核心留在 `day_distinct_ratio(Ret)` 这一层 —— 这是我推荐它当首选核心的唯一理由。
6. **三件机制层面的提醒**:(i) 有界离散的日内比例类特征单独写一定过不了 distinct 闸门(0.02–0.43,实测),
   必须配多日 `cross_*` 平均或条件算子;`ts_max@40` 在 H1/H2 里**同时**是闸门的开门器,别当平滑层去掉。
   (ii) 不要用 `LimitWidth` / `BoardCode` 做 `cs_bucket_*` 的分桶变量(列序破平手,就是第 1 轮被划掉的 `ListAge` 那个坑);
   要分段就用 `_lexi` 系(`cs_last_high05` / `cs_first_low40`,按整个平手块取 band)。
   (iii) score = min(train, valid) 会奖励「两条腿刚好交叉的那个窗口」(H4 的窗口阶梯 1.40/0.40 → 0.74/0.77 → 0.35/0.75 就是这么来的);
   选 R 变体和写种子时,优先两条腿都舒服高过 0.5 的写法,别去追 min 的最大值。
