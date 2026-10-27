# C01 第 2 轮的 thesis 卡与先验(主研,写在 R2 开跑之前)

依据只有两样:本实验 R1 那 8 次共用搜索的证据(`research/coldstart_C01/digest_r2.md`、
`episodes/c01r1s101..108_I0_open_search/evidence.json`)和算子内核源码。另外用到的公开文献常识一律在正文里
标成「先验」。指引文件:`guidance/C01_r2.yaml`(检查器 ADMISSIBLE,2 ideas / 5 priors)。

## 这一轮押的是什么

R1 的读数是:273 个通过者里 217 个(79%)与 pool / 已知族 |ρ|≥0.5,4 个种子(101/102/106/108)因此一个
head 都没有;18 个 head 里 12 个来自种子 104 同一个结构族(`cs_mask_top_replace_mean_neg` + `inv/div` 套
`day_distinct_ratio(Vwap)` 与 `day_std(Close|Vwap|Ret)`),而收益动态(Ret 叶子 lift 0.63)、日内时点、量价
交互、隔夜与日内的分离一个 head 都没出。

所以 R2 用两个杠杆,分工明确:

1. **先验(5 条 ban)把漏掉的算力收回来。** 在 R1 全部 627 个候选上逐条核对:打掉 189/217 = 87% 的
   「|ρ|≥0.5 且通过」候选,**一个 R1 head 都没碰**(既没被 ban,也没被改权重;5 条全是 ban,没有一条
   weight 规则,所以 `w_ref = 1.0`,没撞上规则的中性候选接受概率仍是 1 —— 这是刻意的,因为
   `accept` 的公式是 `min(1, w/w_ref)`,只要存在一条 w>1 的规则,其余一切都会被按比例降采样)。
   去掉被禁候选后,R1 通过者只剩 84 个,其中 |ρ|≥0.5 的只有 28 个(33%,原来 79%)。
2. **邻域(两个 idea 的 `grammar.day_ops` 硬 must-contain)把主要算力押到新机制上。** 不含该 idea 任一
   day_op 的候选一律判 outside。这同时解决了「不要再收割种子 104 那一族」的问题:那一族的 12 个 head
   没有一个含 C2a 或 C2b 的 day_op,**在 R2 的两个邻域里都不可达**,而我没有为此写任何会命中 head 的先验。
   两道闸合起来之后,R1 的 627 个候选只有 32 个(C2a)和 29 个(C2b)在邻域内且未被禁,其中通过门槛的
   分别只有 1 个和 0 个 —— 不是邻域小(光算 must-contain,邻域分别容得下 R1 的 109 和 147 个候选),
   是 R1 在这块地方基本没找到过东西。

两个 idea 都是「机制 + 让搜索去那里硬搜」,不是把 R1 最好的公式再变一变:R2 的 12 个种子表达式里没有一个
用 `cs_mask_top_replace_mean_neg`,也没有一个以 `day_distinct_ratio` 或 `day_std` 为核。

---

**种子分配**(交给 `scripts/c01_jobs.py 2 guidance/C01_r2.yaml ...` 的那份):
`[{"idea": "C2a_when_the_return_arrives", "seeds": [201, 202, 203, 204]},
{"idea": "C2b_turnover_on_the_up_minutes", "seeds": [205, 206, 207, 208]}]`。
每个 idea 4 次运行 × 192 次付费评估,各带 6 条种子表达式(进初代种群,每条自己占 1 次付费评估)。

## 卡 1:C2a_when_the_return_arrives(种子 201–204)

**机制(一句话)。** A 股 T+1 下今天买的票今天卖不掉,被消息与关注驱动的买家只能在开盘追价并被迫把仓位扛过夜;
一只票的收益长期靠隔夜跳空到账(而不是靠盘中 241 分钟走出来),说明它的边际买家长期是这类受约束的追价者,
这部分需求是价格压力、会回吐。

**先验部分(公开文献,不是本实验的结论)。** A 股隔夜收益系统性为正、日内收益系统性为负,这一背离在小盘、
高散户持股的票上最强,通常归因于 T+1 与关注度驱动的开盘追价;把一天的收益拆成隔夜段与盘中段之后,两段的
横截面含义不同(隔夜段更像散户/关注度需求,盘中段更像耐心资金的吸收)。本实验自己的证据只能说:R1 完全
没有测过这件事。

**对手方,为什么他们会亏。** 看到隔夜消息、第二天开盘追价的散户与关注驱动资金。他们在价格已经把消息含进去
之后成交,又因为 T+1 必须把仓位扛过夜,这笔即时性溢价是付给卖方的;长期靠隔夜到账的票,就是他们长期在买的票。
做多的是另一侧:收益在盘中逐步走出来、能被分批吸收的票。

**可证伪的预测(下一轮 B 臂应该看到什么)。**
- 种子 201–204 这 4 次运行里至少 1 个 head,其核含 `day_first`/`day_last` 作用在 Ret 或 Close 上,或含
  `day_centroid`/`day_argmax`/`day_argmin`;
- 该 head 与 pool 的 |ρ| ≤ 0.3,换手 ≤ 0.12(它应该是个特征,不是在交易每天的跳空);
- 在「隔夜占比」形式上(种子 1、2、3 一族)搜索选到的方向是 **−1**,即做多盘中到账的一侧;
- 这 4 次运行的通过者里 |ρ|≥0.5 的占比 < 40%(R1 全臂 79%)。

**失效条件。**
- (a) 4×192 次付费评估后邻域里一个通过者都没有 → 这个切分在 2018–2023H1 的截面上没有溢价(或者被 15bp
  成本吃掉);
- (b) 通过者 |ρ| 中位数 ≥ 0.5 → 跳空幅度只是小盘/低流动性的代理,机制测不出来;
- (c) 在隔夜占比形式上搜索选到 **+1**(做多靠隔夜到账的票)→ 与机制相反,按失效论处,不要事后改故事;
- (d) head 只出在 `cs_first_low20` 的两个种子上、且方向是 **+1** → 按内核语义,这时被筛中的那 20% 恰好
  成了纯多头书,拿到的是一价/锁停名字,是算子平移的假象,不算这条机制成立(见下面「怎么读 R2」第 2 条)。

**种子(6 条,全部 parse、全部含 MUST 算子、全部不被本文件的先验命中、深度 ≤5)。**

| 种子 | 读什么 |
|---|---|
| `div(abs_(day_first(Ret)), day_std(Ret))` | 隔夜/首分钟那一跳相对自身日内分钟波动的占比 —— 无量纲的「信息在收市时到账」特征 |
| `sub(mul(2, day_first(Ret)), day_sum(Ret))` | 隔夜段减盘中段(= 2×首分钟 − 全天),带符号的背离 |
| `sub(div(day_first(Close), ts_delay(day_last(Close), 1)), div(day_last(Close), day_first(Close)))` | 同一个背离,只用价格构造(开盘价/昨收 − 收盘价/开盘价),不依赖 Ret 首分钟的口径 |
| `cs_first_low20(sub(mul(2, day_first(Ret)), day_sum(Ret)), day_distinct_ratio(Close))` | 背离 + R1 普遍出现的筛选骨架:`day_distinct_ratio(Close)` 最低 20%(一价日的理论最小值 1/n)被顶到核的最高端,在 sign=−1 下排除在多头书外 |
| `sub(day_first(Ret), day_last(Ret))` | 两个会话边界的对比:开盘那一分钟 vs 收盘那一分钟 |
| `cs_first_low20(day_centroid(Amt), day_distinct_ratio(Close))` | 成交额在一天里的重心(0=全在开盘,1=全在收盘),同样带一价日筛选 |

**邻域。** `day_ops: [day_first, day_last, day_sum, day_centroid, day_argmax, day_argmin]`(硬约束 + 8 倍提权),
`ops: [ts_delay, cs_first_low20, div, sub, abs_]`(只提权)。`leaves`/`windows` 按代码不影响搜索,只是说明。
邻域刻意不收窄到具体叶子或窗口:六个 day_op 任含其一即可,`cs_*`/`ts_*`/逐元素算子全部照常可用,sign 与
半衰期(0/5/20)交给搜索。

**和已知族(流动性 / 波动)差在哪。** pool 是 `cross_mean(day_std(Amt), 30)`,量的是成交额的离散度水平;
这里的每个核都是**收益的时间归属**,前三条还按自身日内波动归一,是无量纲量。两者唯一可能的通道是「小票
跳空更大」,这正是预测里把 |ρ|≤0.3 写成硬指标、把 |ρ| 中位数 ≥0.5 写成失效条件的原因。另外本族刻意不碰
`day_distinct_ratio(Vwap)/day_std(Close)`(R1 种子 104 那一族),所以它和 R1 已收 heads 的去重(|ρ|<0.7)
是真有机会过的。

---

## 卡 2:C2b_turnover_on_the_up_minutes(种子 205–208)

**机制(一句话)。** 散户的彩票需求在日内是可观测的:显眼的上涨分钟把成交额吸过去,于是这一天「钱经历的
收益」(按成交额加权的分钟收益)高于「时间经历的收益」(等权分钟收益),分钟收益的右尾也更肥;长期让钱
落在上涨分钟一侧的票长期被追涨,价格里含着这份投机溢价,后续收益更低。

**先验部分(公开文献,不是本实验的结论)。** A 股的资金流 / 主动买入占比类指标在月度横截面上是反向的
(净流入之后跑输),通常解释为价格压力回吐;彩票需求、日内 MAX 与(特质)偏度的负溢价是同一类故事。
本实验自己的证据只能说:R1 的 627 个候选里,`day_signed_ratio`、`day_wmean(Ret, _)`、`day_corr(Ret, _)`
这类「成交额与收益的配对」**一次都没有进过通过者**,`day_wmean/day_wstd/day_topw_mean` 的第一个参数全部是
Amt 或 Volume(即都在量自己身上,没有一次用来称收益)。

**对手方,为什么他们会亏。** 看到显眼上涨分钟才进场的散户,以及被日内动量吸引的短线资金。他们成交在当天
成交额加权均价之上,买到的是彩票形状的分布,让渡掉的是期望收益;向这份需求卖出的,是同一天分批派发的资金。

**可证伪的预测。**
- 种子 205–208 这 4 次运行里至少 1 个 head,其核含 (Ret, @flow) 的配对原子(`day_signed_ratio` /
  `day_wmean` / `day_wstd` / `day_topw_mean` / `day_corr` 的第一个参数是 Ret)或 `day_es_ratio_hi(Ret)`;
- 方向是「做多没被追的一侧」(在 `day_signed_ratio` 写法上是 −1);
- 这 4 次运行通过者的 |ρ| 中位数 < 0.4;
- 它与 C2a 的 head 的 |ρ| < 0.7 —— 否则两个 idea 其实是同一个关注度因子,去重后只剩一个,这一轮的
  「机制多样化」目标只达成一半,要如实记。

**失效条件。**
- (a) 邻域里的通过者 |ρ| 全部 ≥ 0.5 → 成交额加权与时间加权的收益差只是买卖价差 / 刻度粗细的代理;
- (b) 这些 head 与 R1 种子 104 那一族的 |ρ| ≥ 0.7、被跨轮去重刷掉 → 读到的是一价日与粗价格刻度(低名义
  股价),不是追涨。这是本卡最该担心的confound:低价股一个 tick 就是几十 bp,分钟收益的符号会被刻度牵着走;
- (c) 搜索选到的方向是「做多被追的一侧」→ 那是日内动量的延续,不是彩票式高估,按失效论处;
- (d) 这 4 次运行一个通过者都没有。

**种子(6 条,全部 parse、全部含 MUST 算子、全部不被本文件的先验命中、深度 ≤4)。**

| 种子 | 读什么 |
|---|---|
| `day_signed_ratio(Ret, Amt)` | 上涨分钟的成交额份额减下跌分钟的份额,∈[−1,1],天然无量纲 |
| `div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_wstd(Ret, Amt))` | 钱经历的收益减时间经历的收益,按成交额加权波动归一 |
| `div(day_topw_mean(Ret, Amt), day_wstd(Ret, Amt))` | 成交额最大的 10% 分钟的平均收益(一个节点里的事件研究),同样归一 |
| `cs_first_low20(day_signed_ratio(Ret, Amt), day_distinct_ratio(Close))` | 同上 + 一价日筛选(sign=−1 下把一价/锁停挡在多头书外) |
| `day_corr(Ret, Amt)` | 分钟收益与分钟成交额的日内相关 —— 量价交互的最朴素写法 |
| `day_es_ratio_hi(Ret)` | 分钟收益右尾形状(95% 分位之上的均值 ÷ 该分位),内核在分位≈0 时返回 NaN,所以死盘/锁停日**自动**出局,与 sign 无关 |

**邻域。** `day_ops: [day_signed_ratio, day_wmean, day_wstd, day_topw_mean, day_corr, day_es_ratio_hi, day_skew]`,
`ops: [cs_first_low20, div, sub]`。注意与先验的刻意配合:`day_wmean/day_wstd/day_topw_mean/day_skew` 这几个
**算子**被提权 8 倍,而它们「第一个参数是 Amt/Volume」的退化写法被 C2P1/C2P2 禁掉 —— 提权算子、禁掉退化
实例,是让搜索必须把这些加权算子用来称**收益**,而不是再称一遍成交额。`day_cov` 刻意没放进邻域:
`day_cov(Ret, Amt)` 的量纲随成交额走,横截面上就是流动性水平的代理。

**和已知族差在哪。** 所有核都是无量纲的(份额、相关、比值,或按自身波动归一),没有一个是成交额的水平或
离散度;量价交互的方向(钱落在涨的分钟还是跌的分钟)是 pool 这类「只看量的离散度」结构上读不出来的信息。

---

## 先验(5 条,全部 ban;逐条在 R1 的 627 个候选上核对过)

核对口径与 R1 证据一致:`pass` = score ≥ 1;`|ρ|≥0.5` = max(|rho_pool|, |rho_known_traded|) ≥ 0.5(两者在
R1 的 273 个通过者里恒等),缺失时退回 |rho_known|;`head` = 该次运行自己的 heads 列表。命中数是用
`partura.steer.Guidance`(即搜索真正用的那套匹配,含 canonical)算的,不是手数的。

| id | 模式 | 命中 \|ρ\|≥0.5 的通过者 | 命中 head | 命中其它 |
|---|---|---:|---:|---:|
| C2P1_flow_plain_reducers | `{day_max\|day_min\|day_mean\|day_median\|day_sum\|day_quantile\|day_quantile_q25\|day_quantile_q75\|day_var\|day_skew\|day_kurt}(@flow)` | 86 | **0** | 65 |
| C2P2_flow_weighted_by_flow | `{day_wmean\|day_wstd\|day_topw_mean}(@flow, _)` | 72 | **0** | 9 |
| C2P3_pool_restated | `{cross_mean\|cross_scale\|cross_stddev\|cross_rank\|cross_quantile_q25\|cross_quantile_q75\|cross_tail_mean_q25\|cross_tail_mean_q75}(day_std(@flow), _)` | 26 | **0** | 0 |
| C2P4_open_close_bar_flow_level | `{day_first\|day_last\|day_open\|day_close}(@flow)`,`unless: cs_first_low20(day_open(@flow), _)` | 25 | **0** | 11 |
| C2P5_price_variance_level | `day_var(@price)` | 30 | **0** | 4 |
| **并集** | | **189 / 217(87%)** | **0 / 18** | |

每条的理由(可证伪的那句话原文写在 YAML 的 `why` 里):

1. **C2P1** —— 成交额与成交量的平凡日内聚合(水平、离散度、形状)只是已知流动性族换个写法。R1 里这一族
   既便宜又容易过门槛(`day_max(Amt)` 裸值就 +2.09、ρ+0.81),种子 106 的 31 个通过者几乎全在这里、heads 0;
   种子 101 的 77 个通过者主干是 `day_sum(Volume)` 与 `day_var(Low)` 的 `pow_1_5` 膨胀链、heads 0。
   可证伪:R2 B 臂通过者里 |ρ|≥0.5 的占比从 79% 降到 40% 以下而 heads 数不降;若整组颗粒无收且 evidence
   的 `sampling.banned` 占掉提议的大头,说明禁得过宽,R3 应改成降权。
2. **C2P2** —— 把成交额自己当被加权量得到的还是成交额水平(`day_wstd(Amt, Amt)` +2.28/ρ+0.78);把 Ret 当
   被加权量才是量价交互。这条只禁前者,**故意**把 `day_*(Ret, @flow)` 整个留给 C2b。可证伪:R2 里不再出现
   |ρ|>0.7 的 `day_w*(@flow, _)` 通过者,而 C2b 的 (Ret, Amt) 配对至少出 1 个 head;若 C2b 也一个都出不来,
   说明被禁掉的不是陪跑,而是这类算子的全部信号。
3. **C2P3** —— pool 就是 `cross_mean(day_std(Amt), 30)`,把外层换成另一个按日滚动的归并算子得到的是同一个
   东西,按判读规则永远不可能成为 head(R1 里这一形状 26 个候选、全部通过、全部 |ρ|≥0.5、heads 0)。
4. **C2P4** —— 开盘或收盘那一分钟的成交额仍是流动性水平(裸 `day_open(Amt)` 就 +1.56、ρ+0.91,种子 103 把
   24 个候选花在这个 y 上)。C2a 把 `day_first`/`day_last` 提权 8 倍,等于给这个水平量开了一条**带提权的
   后门**,所以必须连带禁掉;`unless` 原样豁免 R1 两个 head 用的 `cs_first_low20(day_open(@flow), _)` 结构,
   所以这条规则对 18 个 head 的命中数是 0,R1 那两个 head 的表达式在 R2 既不被禁也不被降权。
5. **C2P5** —— 价格叶子的日内方差是「名义股价² × 日内波动²」,量纲随股价走,是 pool 的近亲而不是无量纲特征;
   R1 的 18 个 head 没有一个用 `day_var`。这条比 E2 测过的 `day_var(Low)` 宽了一点(同样 30 个 |ρ|≥0.5 的
   通过者,多命中 2 个未通过候选),代价是顺带关掉了 `day_std(@price)` 的单调孪生写法 —— 这正是本轮不想
   再收割的那一族,而且它按跨轮去重也成不了新 head。可证伪:若禁错了,R2 B 臂每百次付费评估的 heads 数会
   低于 R1 同种子水平,R3 应退回只禁 `day_var(Low)`。

**没有写的先验,以及为什么。**
- 不写任何针对 R1 种子 104 那一族(`cs_mask_top_replace_mean_neg`、`inv(div(...))`、`day_std(@flow)`、
  `{day_gini|day_skew|day_kurt}(@flow)` 里的 gini 支)的 ban 或降权:这些模式会命中 R1 的 head
  (`cs_mask_top_replace_mean_neg(_)` 命中 13/18、`inv(_)` 命中 11/18、`day_std(@flow)` 与
  `{day_gini|day_skew|day_kurt}(@flow)` 各命中 1),按本轮的规矩不许用。压住这一族交给邻域的 must-contain。
- 不写 weight 规则:`accept` 是 `min(1, w/w_ref)`、`w_ref` 取所有 weight 规则里的最大值,一条 w>1 的规则会
  把其余一切按比例降采样。要「提权」就用 idea 的 grammar(它作用在生成器挑算子那一步,不动接受概率)。
- 不写 `rewrite`:`day_open`→`day_first` 这类别名合并能省几次重复评估,但它会改写 canonical 形,从而让
  C2P4 的 `unless` 失效、规则反过来命中那两个 head。收益小、耦合脆,不做。

## 怎么读 R2(给 R3 的自己和总领留的判读纪律)

1. **不要朝 valid 调参。** 本文件没有一处用 valid 分数来选 idea 或选种子:R1 的 valid 段(2022–2023H1)正是
   微盘/低价强势期,而据公开信息测试段含 2024 年初的微盘流动性踩踏,valid 高分本身不构成证据。两个 idea
   选的都是与「做多低流动性慢变量」不同方向的机制,机制多样化本身就是对冲。
2. **`cs_first_low20` 的 sign 陷阱。** 按内核语义(`_lexi` 把筛中的那段 `rank(y)` 加 1),被筛中的 20% 永远
   在核的最高端:sign=−1 时它被排除在纯多头书外(这是我要的),sign=+1 时它**就是**纯多头书。所以任何来自
   204 / 208 这两个种子、方向为 +1 的 head 都要当成嫌疑品:先核它的多头书是不是一价/锁停名字,再决定算不算。
   顺带记一条代码事实:本实验的奖励是 `long`,`RewardContext.untradable` 那套可交易性掩码只在
   `long_tradable/long_bucket/long_marginal` 下生效,所以**书本身没有涨停/停牌/次新掩码**(引擎只把停牌与
   未上市的分钟置 NaN,涨跌停锁死那天 day_status 仍是 TRADING)。这就是我在种子里显式写一价日筛选的原因。
3. **不要用筛选平移排名来刷 head 数。** `cs_first_low20` 这类算子把 20% 整段平移,即使其余 80% 一个名次没变,
   与未平移信号的秩相关也会从 1 掉到约 0 —— 它能把 |ρ| 刷低而多头书照旧。本轮只在 2 个种子里用它,而且
   用途是排除一价日,不是压 ρ;判读时如果一个 head 的 ρ 低但多头书与某个已知族的多头书高度重合,按坏 head 记。
4. **几个测量假设,R2 的结果会顺带检验它们。**
   - 种子 1、2、4 依赖「Ret 的首个分钟含隔夜/集合竞价那一跳」这个口径。种子 3 用价格比值重算同一件事、不依赖
     这个口径;两者结果差很远,本身就是关于 Ret 口径的读数。
   - 种子 3 含 `ts_delay(..., 1)`,前一交易日停牌的票当天会变 NaN,有一定概率撞上覆盖率 ≥0.9 的门槛;若它
     gate_fail,代价是 1 次付费评估,这条 idea 还有 5 个种子。
   - `day_argmax`/`day_argmin` 返回的是**分钟下标**而不是价格(内核事实),C2a 正是要这个时点量;读 R2 时
     不要把含它们的核当价格类量解释。
5. **邻域是否过窄,看 evidence 的 `sampling` 计数器。** R1 的 `sampling` 全是空字典(对照臂不走
   `guidance_accept`)。R2 的 B 臂应该出现 `outside`/`banned`/`thinned`/`sibling` 的计数;若某次运行
   `outside` 吃掉绝大部分提议而通过者为 0,就是邻域(不是先验)把搜索卡死了,R3 必须放宽 day_ops。
