# 结构解剖:种子 803,B 组,第 1 轮

读的东西:`r1/loc.md`、`r1/loc.json`、`PLAN.md`(含 3 条修订)、`scripts/c05_locate.py`、`scripts/c05_round.py`、`scripts/c05_check.py`、`scripts/c05_lib.py`、`partura/steer.py`(reward / neutral_basis / neutral_residual)、`partura/diagnose.py`(distinct_fraction / _zrank)、`partura/ops_ext.py`、`$HOME/Desktop/AlphaCube-steering/src/alphacube/operators/{common,dt_day,dt_in,dt_cross}.py`、`catalog.py`、`parser.py`、`dailyfields.py`。
没有 notebook.md(第 1 轮),没有之前各轮的任务。**没有读**任何其他种子目录、C01–C04、`guidance/C0*`、`runs/ lab/ notes/ studies/ handoff/ batches/ docs/`、任何测试段数字。

本轮证据极少,所以下面严格区分四类来源:**(定位)**= 定位工具真给出的数;**(源码)**= 我读代码确认的算子/奖励语义;**(算术)**= 我在本机对算子本身做的数值验证(只用随机张量,不碰数据);**(推断)**= 未经付费评估检验的假设。

---

## 0. 本轮快照的实际信息量:一个 head,零次拆解

(定位)快照 `c05s803M1_I0_open_search`:

| score | train | valid | 方向 | 半衰期 | 表达式 |
|---|---|---|---|---|---|
| +0.97 | +0.97 | +1.54 | −1 | 20 | `day_kurt(Ret)` |

已评分候选 43 个;**共性表空**;**拆解 0 个变体、0 次付费评估**;机械核心卡空;R 候选空。

拆解为什么是 0(源码,`c05_locate.py` 第 246–277 行),四条路全部走不通:

1. **充分性**:子树取 `n in t.nodes()[1:]` 且 `n.operands and n.shape.collapsed and n.shape.degenerate and is_valid_root(n)`。`day_kurt(Ret)` 只有两个节点,非根节点只有叶子 `Ret`,它 `operands` 为空、而且是分钟形状 → 没有任何可单独求值的真子树。
2. **必要性(跳过一个算子)**:循环同样只走 `nodes()[1:]`,**根节点永不被跳过**(PLAN 修订 1 第 4 条明确如此)。所以 `day_kurt` 这个算子本身从来没被检验过。
3. **敏感性(换同类字段)**:`SWAP = {Close↔Vwap, Open→Close, High↔Low, Volume↔Amt}`。**`Ret` 不在 SWAP 里**,没有同类伙伴 → 一个换字段变体都没生成。
4. **敏感性(窗口 ×½/×2)**:`day_kurt(Ret)` 没有带窗口的节点 → 没有窗口变体。

结论:**≤ 48 次拆解预算整轮作废,而且按 PLAN §2.3「用不完的不挪用」不能转给别处**。本轮唯一还能花的付费通道是 **R 的 ≤ 16 次直接评估**。这件事决定了下面第 2、4 节的全部取向:R 今轮不该只拿去「找替换」,它是本轮唯一能买到的诊断。

共性表为什么空(源码):`c05_lib.archive()` 读的是 `<arm>/checkpoints/archive_gen*.csv` 的**最后一个存档检查点**,即 GP 的精英存档(43 个多样化幸存者),不是 192 次评估的全日志。共性门槛是「同一子树出现在 ≥ 4 个候选里」,而键是 `repr(n)`,**含窗口**(`cross_mean(x,20)` 与 `cross_mean(x,30)` 算两个)。在一个已去重的 43 条精英表上,同一个「算子+字段+窗口」重复 4 次的概率本来就很低。
所以**共性表空主要是工具分辨率的问题,不是「没有复现结构」的证据**,不要当成信息。

但有一个可以反推出来的硬结论:如果 `day_kurt(Ret)` 作为**非根**内部子树出现在 ≥ 4 个候选里,它自己就会进共性表(它满足 `operands` + collapsed + degenerate)。共性表空 ⇒ **43 个精英里至多 3 个把 `day_kurt(Ret)` 包在别的东西里**。而 E 任务 `--periphery-seen` 的 `SEEN` 正是从这同一份存档建的(`c05_round.py` 第 135 行),所以:

> **本轮 E 的「外围不得与见过的相同」几乎不构成约束:`SEEN` 至多 4 个元素(含「核心单独」那个空集)。**

---

## 1. alpha 的来源:`day_kurt(Ret)` 是什么,以及它有多可能只是代理

定位工具没给任何共性/充分性/必要性/敏感性的数,所以这一节只能靠源码与算术。**本轮无法断定它是真来源**;但可以把它收窄成一个能被 16 次评估判决的二择。

### 1.1 它在算什么(源码 + 算术)

- `Ret` 是分钟级收益字段(`catalog.CUBE_FIELDS`),`n_minutes=241`。`day_zero_ratio` 的文档串写明 `Ret` 上零值的含义是「这一分钟价格没动(封板、停牌、没成交)」—— 即 **`Ret` 带一个在 0 上的点质量**。
- `day_kurt = C._kurt`,即 `E[(x−μ)^4] / (E[(x−μ)^2])^2 − 3`,无样本量修正。它对**日内常数的仿射变换完全不变**:(算术)`day_kurt(in_demean(Ret))` 与 `day_kurt(Ret)` 差 0.0;除以 `in_stddev_full(Ret)` 或 `in_sum(·)` 差 ~7e−7(浮点)。
- 所以它量的是分钟收益分布的**形状**,尺度已被自己除掉。
- 奖励的波动控制是 `cross_mean(day_std(Ret), 20)` —— 同一条分钟序列的**尺度**。所以 `day_kurt(Ret)` 躲过波动控制**不是偶然,是构造性的**:控制拿掉的正是它已经除掉的那一项。这一点对它有利:它**不是**波动率的另一种写法。

### 1.2 关键风险:它在算术上近似等于「有多少分钟真的在交易」的倒数

设一天 n = 241 分钟,其中 k 分钟有非零收益、n−k 分钟为 0。则(算术,本机数值验证):

| 活跃分钟 k | 活跃分钟为 ±r | 活跃分钟为高斯 | n/k − 3 |
|---|---|---|---|
| 241 | −1.99 | −0.06 | −2.00 |
| 120 | −0.99 | +2.79 | −0.99 |
| 48 | +2.02 | +10.78 | +2.02 |
| 24 | +7.00 | +23.07 | +7.04 |
| 12 | +17.04 | +44.45 | +17.08 |
| 5 | +45.12 | +92.68 | +45.20 |
| 1 | — | +236.0 | +238.0 |

即 **`day_kurt(Ret) + 3 ≈ c · 1/(1 − day_zero_ratio(Ret))`,c ∈ [1, 3]**,随零值比例单调上升而且非常陡:活跃分钟从 241 掉到 24,峰度就从 −2 走到 +7~+23。真实的尾部形状差异要达到同一个量级才能在截面上盖过它。

**方向(定位)是 −1,半衰期 20**,所以多头腿是**残差峰度最低**的那一端 = **分钟收益铺得最匀、连续成交**的股票;被排除的是「几分钟吃掉全天波动」的股票。这正是「长流动的、短稀疏的」。

控制里有 `cross_mean(day_sum(Amt), 30)`(成交额水平)、已知族 `cross_mean(day_std(Amt), 30)`(日内成交额离散)、`LogFloatCap`,但**没有任何一项是「这一天有多少分钟真的成交了」**。成交额水平和成交分钟数对中小市值股可以差得很远(一笔大单撑起成交额,但全天只有十几分钟有成交)。所以线性中性化掉这三项之后,稀疏度那一维很可能还留在残差里。

(源码)另外两个相关事实:
- `frozen = cross_max(day_zero_ratio(Ret), 15)` 与 `age` 构成的 `untradable` 掩码,在 `long_neutral` 下**不被使用**(`steer.reward` 里 `mask` 只给 `long_tradable / long_bucket / long_marginal`)。所以这本书没过可交易筛。好消息是选中的方向(−1)指向连续成交那一端,正好背对冻结角落;坏消息是 valid 的 +1.54 是在未筛 universe 上读的。
- `div` 是裸 `torch.divide`,没有 eps。(算术)全天 `Ret` 恒为 0 → 0/0 → **NaN**(当天该股票从书里掉出去,不会被当成极低峰度买进来);只有开盘一跳、其余 240 分钟为 0 → ≈ +236,落在被排除的高端。**没有「死股票被买进多头腿」的灾难性假象**,方向是合理的。
  (顺带记一条给后面几轮:日内恒为**非零常数**时,float32 的均值舍入让 demean 后得到一个极小常数,比值恰好 = 1,`day_kurt` 返回 **−2.0** 而不是 NaN。对 `Ret` 不现实,但**若以后出现 `day_kurt` 作用在价格类字段上的 head,封板日会给 −2.0 即最低端,是真假象**,届时先查这一条。)

### 1.3 三个互斥的来源假设(都未检验)

| 假设 | 机制 | 判决用的探针(见第 4.2 节) |
|---|---|---|
| **H1 稀疏度代理**(我认为最可能) | 峰度 ≈ 241/活跃分钟数 − 3,因子实质是「成交分钟数」,是流动性的一种新写法,控制里没有它 | `cross_mean(day_zero_ratio(Ret), 20)` 的 ρ_head;`day_kurt(in_logchg(Vwap, 1))`(Vwap 在无成交分钟为 NaN,等于只在**成交过的分钟**上算峰度)是否仍带 alpha |
| **H2 真尾部形状 / 跳跃集中度** | 全天波动集中在少数几分钟(新闻、单边大单),与成交密度无关 | `day_gini(Ret)`(有界、不被单个打印支配)、`day_es_ratio_hi/lo(Ret)`(**构造上把死日剔成 NaN** 的尾部形状)能否复现 |
| **H3 彩票需求 / 封板后效**(也属「已知异象的另一种写法」,但控制里没有) | hl=20 把它变成「上个月有多少跳日/封板日」;高峰度那端是 MAX 效应与涨跌停磁吸的人群 | `div(day_max(Ret), day_std(Ret))`、`cross_mean(day_at_max_ratio(Close), 20)` 的 ρ_head |

三个都能解释 score 0.97,但判读完全不同:H1 和 H3 都属于「只是别的东西的另一种写法」(虽然都不在控制里,所以照样拿分),H2 才是真的新来源。**判决只需要 ρ_head**,而 `direct` 模式对每个过门槛的变体**都**算 ρ_head(`c05_locate.py` 第 188 行),这是本轮最便宜的信息。

### 1.4 有利于「不是过拟合」的两点(定位)

- train +0.97 / valid +1.54,**valid 比 train 好**,score 取较差者 = train。不是训练段挖出来的尖峰。
- 半衰期 20 是 `ctx.halflives = (0.0, 5.0, 20.0)` 的**上边界**。(推断)最优平滑可能在边界之外,即「更慢更好」:原始日度峰度很吵,alpha 住在它的月度均值里。这同时说明它更像一个**状态/特征**(这只股票平时怎么交易),而不是一个事件信号。这条可测,但属于 E 的地盘(见 4.1)。

### 1.5 关于「代理」的一条额外发现(源码 + 算术)

`day_kurt` 既然对日内常数仿射不变,下面这些**看起来像处理、实际与裸核心逐点相同**:
`day_kurt(in_demean(Ret))`、`day_kurt(div(in_demean(Ret), in_stddev_full(Ret)))`、`day_kurt(div(Volume, in_sum(Volume)))` ≡ `day_kurt(Volume)`(`in_sum` 是全天总和再广播,见 `dt_in.py:196`)。
它们会被库的 ρ ≥ 0.7 禁令挡掉(ρ = 1.0),不浪费预算,但会浪费 E 的生成尝试,并推高 PLAN 修订 1 第 5 条那种「退回最小树」的计数。**写 E 种子时不要碰这一类。**

---

## 2. 烂部件:本轮无法用「必要性 ≤ 0」说话,只能换件

两个节点的树没有「多余部件」可去;而且(第 0 节)根算子从不被跳过、`Ret` 没有 SWAP 伙伴,所以**必要性与敏感性这两列整轮是空的,不是 ≤ 0**。诚实的说法是:**本轮没有任何部件被证明是烂的**。

能做的只有「替换部件」,而且有两个部件各自对应一个明确的怀疑:

- **部件 A:根算子 `day_kurt`**。怀疑点是它**会被单个打印支配**(`day_gini` 的文档串原话:有界、尺度无关,「unlike `day_kurt` / max-share it cannot be dominated by one print」),而且在零质量上饱和(`day_flat_run_max` 的文档串:F108 研究里「kurtosis reads '29 still minutes then one print', which is a statement about runs」)。**这套算子库本身就是为了修 `day_kurt` 这个毛病而写的** —— `day_zero_ratio` 的文档串写着「Requested by the F114 study: its tree turned out to be reading this atom」。这是我判 H1 最可能的主要依据。
  → 替换件:`day_gini`、`day_es_ratio_hi/lo`、`day_zero_ratio`、`day_flat_run_max`、`day_distinct_ratio`。
- **部件 B:输入 `Ret`**。怀疑点是它带 0 的点质量,且第一根 bar 的含义取决于数据构造(若含隔夜跳空,峰度会被这一个观测主宰)。
  → 替换件:`in_pct(Close, 1)`(日内重建,首分钟为 NaN,**不含隔夜跳空**)、`in_logchg(Vwap, 1)`(**Vwap 在无成交分钟缺失** → 只在成交过的分钟上算)、`in_madz(Ret, 30)`(对局部波动稳健标准化,MAD=0 处为 NaN 而不是爆炸)、`in_zscore_expand(Ret)`。

**一条必须提醒 PI 的门槛陷阱**(源码,`c05_locate.py` 第 137–139 行 + `diagnose.distinct_fraction`):门槛在**原始面板**上查 `distinct_fraction ≥ 0.5`,它是「每日不同取值数 / 有值股票数」的中位数。形如 k/241 的比例类算子(`day_zero_ratio`、`day_distinct_ratio`、`day_pos_ratio`、`day_flat_run_max`、`day_at_max_ratio`)最多 242 个取值,面对每日四五千只股票,distinct ≈ 0.05,**会被判「门槛废品」,白花一次评估**。奖励里的 EMA 发生在门槛**之后**,救不了。
→ 这类探针必须把平滑写进表达式本身:用 `cross_mean(day_zero_ratio(Ret), 20)` 之类(20 天均值把取值数抬到 ~4800)。这个 `cross_mean` 外壳是**门槛变通,不是新增部件**,写进 missions.yaml 时最好注明。
另一个方向的门槛风险:`day_es_ratio_hi/lo` 在 95%/5% 分位 ≈ 0 时返回 NaN(即薄日),`coverage ≥ 0.9` 可能擦线。这是它的优点(死日被构造性剔除)也是它的风险。

---

## 3. 之前的任务

第 1 轮,没有。`loc.json` 的 `missions_before` 为空。

一条调度事实,会影响 PI 怎么用 R(源码,`c05_round.py` 第 162–169 行):**R 的 direct 作业和两个 GP 位是同一次 `mission` 并发起的**,所以 **R 的结果来不及给本轮的 E 选核心**。本轮的 R 是给第 2、3 轮做判决用的投资,不是本轮 E 的输入。这进一步支持第 2 节的取向:R 要买诊断(ρ_head),不要只买「能不能替换」。

---

## 4. 本轮候选

### 4.1 核心:只有一个是合法的

(源码,`c05_check.py` 第 71–79、98–109 行)核心必须满足 `ct.key() in known`,而 `known` 是快照 heads 树上**所有节点的 key** 加上共性/核心卡里的子树。本轮 `known` = {`day_kurt(Ret)`, `Ret`} 的 key,而 `Ret` 不是 `is_valid_root`(分钟形状)。共性表与核心卡都空。

> **本轮唯一可做 E 的核心是 `day_kurt(Ret)`**(靠 PLAN 修订 3「整个 head 也可以当核心」才成立)。

它整个实验至多 2 个 E 位,本轮用掉 1 个就只剩 1 个。

**它周围已经见过的外围写法**:定位输出不打印存档表达式,所以我**无法点名**。能说的是第 0 节推出的上界 —— 至多 3 个,`SEEN` 至多 4 个元素。
(源码,`idea_search.py` 第 311–315 行)`periphery(t)` 是「核心之外算子**名字的集合**」(多重集相减后取正数项的名字集,**不含窗口、不含结构**)。所以:
- `cross_mean(day_kurt(Ret), 20)` 与 `cross_mean(day_kurt(Ret), 40)` 的外围**相同**({`cross_mean`}),一个被见过另一个就废;
- 建议外围取**≥ 2 个算子、且至少一个是不常被抽到的算子**,躲开 {`cross_mean`}、{`div`}、{`mul`}、{`add`}、{`cross_ema`} 这类单算子集 —— 它们既最可能已在 `SEEN`,又最可能触发库的 ρ ≥ 0.7 禁令。

**E 的设计铁律(源码,`c05_round.py` 第 145–152 行 + `idea_search.py` 第 183–188 行)**:家族 = 库里含该核心的 heads 前 ≤ 6 个 = **只有 `day_kurt(Ret)` 自己**,它以 `sign × EMA_20` 的形式**进控制基**。`neutral_residual` 是在**秩空间**上对 [1, 五个控制, 核心] 做逐日正交投影。因此:

> E 候选只有在**截面秩上不是核心秩的线性函数**时才可能拿分。纯单调改写、线性改写、单纯换平滑窗口,构造上得分 ≈ 0。

能拿分的外围只有三类(以下全部已在本机 parse + 带核心校验通过):

1. **分组内重排(非线性中性化)** —— 线性投影拿不掉桶内排序:
   `cs_bucket_rank(day_kurt(Ret), LogFloatCap)`、`cs_bucket_rank(day_kurt(Ret), LimitWidth)`、`cs_bucket_rank(day_kurt(Ret), BoardCode)`、`cs_bucket_zscore(day_kurt(Ret), LogFloatCap)`、`cs_bucket_demean(day_kurt(Ret), LimitWidth)`、`cs_bucket_rank(day_kurt(Ret), cross_mean(day_std(Ret), 20))`。
   `LimitWidth` 特别值得用:它是逐日逐板的涨跌幅上限(0.05/0.10/0.20),**创业板 2020-08-24 改 20% 就落在 train 段内**,是现成的自然实验,而且直接对准 H3。
   `BoardCode` 只有 4 类({主板 0, 科创 1, 创业 2, 北交 3}),十分位会塌成 ≤ 4 组,这正是「在自己板内排序」。
   **别用 `ListAge` 当分桶变量**:`dailyfields._list_age` 给 2018 年之前就上市的股票 `LIST_AGE_SENTINEL = 10000` 起算,它们的路径完全相同、截面上没有差异,实际只能分出「新股 vs 其余」。
2. **换时间尺度 / 把水平改成异常** —— 控制里只有核心的 EMA_20 水平:
   `cross_zscore(day_kurt(Ret), 60)`、`cross_madz(day_kurt(Ret), 60)`、`cross_delta(day_kurt(Ret), 20)`、`cross_stddev(day_kurt(Ret), 40)`、`cross_tail_mean_q75(day_kurt(Ret), 40)`(近 40 日里**最跳的那几天**的峰度 = 跳日频率×severity,而不是均值)、`div(day_kurt(Ret), cross_mean(day_kurt(Ret), 60))`。
3. **按市场状态开关/翻向**:`cs_flip_by_state(day_kurt(Ret), day_sum(Amt))`、`mul(cs_state_rank(day_sum(Amt), 60), day_kurt(Ret))`。`cs_flip_by_state` 的文档串给了自带的检验:如果 y 只是在另一种状态下失效而非反向,翻向版会明显更差 —— 这本身就是答案。

叠起来的组合也合法、外围集合更独特,例如 `cs_bucket_rank(cross_zscore(day_kurt(Ret), 60), LogFloatCap)`(外围 = {`cs_bucket_rank`, `cross_zscore`})。

**要不要本轮就用掉 E 位**:我倾向用。理由是 (a) 本轮只有这一个核心,不用 E 位就只能两个 N;(b) 家族控制里含核心,**在一个可疑核心上做 E 反而是自我保护的** —— 任务无法因为把假象重写一遍而得分,它被迫去找核心之外的东西;(c) 第 2、3 轮核心会变多,但第二个 E 位留给同一核心时,能用上本轮学到的东西。风险是 `--must-contain` 逼着假象留在树里,候选自己的面板仍带着它。

### 4.2 R 目标:16 次全部用来做判决,按优先级排

(全部已在本机通过 parse + `is_valid_root`;头一律是 `day_kurt(Ret)`)

**第一优先 —— 判 H1 对 H2(4 个)**
1. `day_kurt(in_logchg(Vwap, 1))` —— 最干净的一刀。Vwap 在无成交分钟缺失,`day_kurt` 跳过 NaN,等于**只在成交过的分钟上**算同一个统计量。还带着 alpha ⇒ H1 被否;丢掉 ⇒ 来源就是未成交分钟的质量。
2. `cross_mean(day_zero_ratio(Ret), 20)` —— H1 的直接代理(`cross_mean` 是门槛变通)。ρ_head ≳ 0.7 ⇒ 这个 head 就是稀疏度。
3. `day_gini(Ret)` —— 有界、不被单个打印支配的同一「集中度」思想。既是判决也是**最有希望的真替换件**。
4. `day_kurt(in_pct(Close, 1))` —— 日内重建分钟收益,**首分钟为 NaN**,把隔夜跳空和 `Ret` 的构造约定一起拿掉。

**第二优先 —— 尾部哪一侧、要不要双侧(3 个)**
5. `day_es_ratio_hi(Ret)` 6. `day_es_ratio_lo(Ret)` 7. `day_skew(Ret)`
峰度是双侧的。若只有一侧在起作用,单侧替换件应该直接超过原 head 0.1 以上(即构成真替换)。

**第三优先 —— 判 H3(2 个)**
8. `div(day_max(Ret), day_std(Ret))` —— 尺度无关的 MAX。
9. `cross_mean(day_at_max_ratio(Close), 20)` —— 停在当日最高价的时间占比的月均 ≈ 封板频率。

**第四优先 —— 「集中在成交里」而不是「集中在钟表时间里」(2 个)**
10. `div(day_wstd(Ret, Amt), day_std(Ret))` —— 成交额加权波动 ÷ 钟表波动。`day_wstd` 文档串:「dead minutes no longer dilute it」。这是这个核心**经济上说得通**的版本。
11. `day_topw_mean(Ret, Amt)` —— 最重的 10% 分钟的平均收益。

**第五优先 —— 是收益分布还是成交分布(2 个)**
12. `day_kurt(Amt)` 13. `day_gini(Amt)`
(注:`day_kurt(div(Volume, in_sum(Volume)))` 与 `day_kurt(Volume)` 逐点相同,别两个都报。)

**备选(3 个,凑满 16 时按此序)**
14. `day_kurt(in_madz(Ret, 30))` 15. `day_kurt(in_zscore_expand(Ret))` 16. `cross_mean(day_flat_run_max(Ret), 20)`

**不建议放进 R**:`cross_mean(day_kurt(Ret), 40)`、`cross_zscore(day_kurt(Ret), 60)` 这类「在核心外面加东西」的,既不是 §2.5 说的「去掉或替换部件」,又正好是 E 位要覆盖的地盘,放 R 是重复花钱。

### 4.3 N 的灵感(两个,建议选一个)

**N-A 日内自相关 / 定价效率族**(我的首选,离现有库最远)。`day_ar1_coefficient(Ret)`、`day_durbin_watson(Ret)`、`day_hurst(Ret)`、`day_q_stat_std(Ret)`,配 `cross_*` 平滑与分桶。理由:它们是尺度无关的**时序结构**统计量,和矩族完全不同;五个控制(成交额水平、日内波动、20 日反转、成交额离散、市值)一个都没碰到自相关;分钟收益的负自相关是买卖价差/做市商库存的经典读数,正自相关是价格延迟。和 `day_kurt(Ret)` 共享「分钟序列」这个输入,但用的是**顺序信息**,而峰度把顺序整个扔掉了。

**N-B 日频下行风险与收益不对称**。`cross_semistd_neg(day_last(Close), 20)`、`cross_semistd_pos(...)` 及其比值。理由(源码):波动控制是 `cross_mean(day_std(Ret), 20)`,是**日内**波动;**日频**的、而且分上下行的半偏差完全不在控制里 —— 这是控制集里一个干净的缺口。风险是它可能和 20 日反转控制相关。

**N-C 成交时间 vs 钟表时间**(若 PI 想和 E 配套)。`day_centroid(Amt)`、`day_corr(in_index(Amt), Amt)`、`div(day_wstd(Ret, Amt), day_std(Ret))`、`day_topw_mean(Ret, Amt)` 加 `cross_ema` 平滑与按市值分桶。注意:它和 R 第 10、11 条重叠,若 R 已经买了这两条,N 位就别再花 96 次。

---

## 5. 文献题目(给文献员,4 个;只要 2023-08-08 之前发表的,每条注年份)

**L1 —— 对准核心 `day_kurt(Ret)`:高频收益的高阶矩在截面上被怎么用,以及怎么和「不交易」分开?**
文献里用分钟/日内收益算的峰度、已实现四阶矩、跳跃测度,预测截面收益时**做过哪些处理**:是否先剔除无成交分钟、是否按成交量抽样而不是按时间抽样、是否先去掉隔夜跳空、是否对零收益比例另设控制。特别想知道:**有没有文献明确指出这类高阶矩统计量会被「零收益分钟/停牌/封板」污染,以及他们用什么办法分离。**
EN:`intraday return kurtosis cross-section`;`realized kurtosis stock returns`;`realized skewness cross-section of expected returns`;`jump variation idiosyncratic`;`proportion of zero returns liquidity measure`;`zero-return days transaction cost estimate`;`microstructure noise high frequency moments`;`overnight versus intraday return decomposition`
ZH:`日内收益率峰度 截面`;`已实现峰度 已实现偏度 预测收益`;`跳跃测度 个股`;`零收益率比例 流动性度量`;`隔夜收益 日内收益 分解`;`分钟频率 微观结构噪声 高阶矩`

**L2 —— 对准「换掉 `day_kurt` 这个部件」:尾部/集中度统计量的稳健化与归一化,各自解决什么?**
用高频数据度量「波动集中在少数时点」时,文献用过哪些**更稳健的写法**:双幂变差、中位已实现波动率、截断已实现方差、尾部条件均值比(expected-shortfall 型)、基尼/熵型集中度。每一种相对裸峰度**具体修掉了什么**(单个异常打印的支配?薄交易日?低价股的价格网格?),以及有没有直接的横向比较。
EN:`bipower variation jump test`;`median realized volatility MedRV robust`;`truncated realized variation`;`Barndorff-Nielsen Shephard jump test`;`Lee Mykland jump detection`;`realized quarticity noise robust estimator`;`expected shortfall ratio tail shape`;`Gini concentration intraday trading volume`;`entropy of intraday volume distribution`
ZH:`双幂变差 跳跃检验`;`中位已实现波动率 稳健`;`截断已实现方差`;`尾部条件均值 比率`;`日内成交集中度 基尼系数 熵`;`价格网格 低价股 估计偏误`

**L3 —— 对准 E 的外围:同类特征怎么做条件分组、交互、换股票池?尤其是 A 股的涨跌停。**
波动/跳跃类特征在文献(特别是 A 股)里**怎么被条件化**:按市值分组、按板块(主板/创业板/科创板)分组、按涨跌幅限制宽度分组、按市场状态(牛熊、成交活跃度)分段;用的是**组内排序/组内标准化**还是线性回归残差,两者结论差别大不大;涨跌停封板当日与次日收益的已知结论(磁吸效应、封板后反转);**创业板 2020 年 8 月把涨跌幅限制从 10% 改到 20% 之后**有没有事件研究说这类日内波动特征的表现变了。
EN:`price limit China A-share magnet effect`;`limit-hit stocks subsequent returns China`;`ChiNext price limit reform 20 percent 2020`;`size-conditional anomalies Chinese stock market`;`within-group rank neutralization factor construction`;`conditional double sorting size volatility`;`market state conditional anomaly returns`
ZH:`涨跌停 磁吸效应`;`涨跌停板 封板 次日收益`;`创业板 涨跌幅限制 20% 改革 2020`;`市值分组 条件化 异象 A 股`;`组内排序 中性化 因子构建`;`双重分组 市值 波动率`;`市场状态 分段 异象`

**L4 —— 对准 N-A/N-C:日内收益的顺序信息(自相关、成交时点)在截面上值钱吗?**
分钟收益自相关、方差比率、Hurst 指数这类**顺序/效率**度量,在截面收益预测里被怎么用、怎么标准化(是否先去 U 型日内波动模式、是否按成交量时间抽样),以及它们与价差/流动性度量的关系有多强;另一半:成交量的日内时点(U 型、尾盘集中)、成交量加权的波动率(business-time vs calendar-time 抽样)对截面收益的预测力。
EN:`intraday return autocorrelation price delay`;`variance ratio intraday price efficiency`;`Hurst exponent intraday returns stock`;`business time sampling versus calendar time realized volatility`;`volume-weighted realized volatility`;`intraday volume U-shape timing`;`late-day volume concentration returns`;`bid-ask bounce negative autocorrelation`
ZH:`日内收益自相关 定价效率`;`方差比率 价格效率 个股`;`Hurst 指数 日内`;`交易时间抽样 日历时间 已实现波动率`;`成交量加权 已实现波动率`;`日内成交量 U 型 尾盘`;`买卖价差 负自相关`

---

## 6. 建议写进 notebook 的可检验预测(供第 2、3 轮核对)

1. **R 第 2 条** `cross_mean(day_zero_ratio(Ret), 20)` 与 head 的 ρ_head ≥ 0.5(我押 0.5–0.8)。即 H1 至少占一半。
2. **R 第 1 条** `day_kurt(in_logchg(Vwap, 1))` 的 score 明显低于 0.97(我押 < 0.6)。若反而 ≥ 0.97,H1 被否、H2 成立,整个判读要翻。
3. **R 第 3 条** `day_gini(Ret)` 过门槛且 ρ_head ≥ 0.5;是否够 +0.1 的替换线,我押**不够**(有界化会丢掉高端的分辨力)。
4. 16 个 R 变体里会有 **1–3 个**栽在 `distinct_fraction ≥ 0.5` 或 `coverage ≥ 0.9` 上(最可能是 `day_es_ratio_lo(Ret)` 的 coverage)。
5. **第 2 轮的共性表仍然很可能是空的或只有极少几行**(快照变成 2 份精英存档 ≈ 85 个候选,门槛 ≥ 4 且键含窗口)。第 2 轮的信息还是会主要来自新 head 的拆解。
6. **第 2 轮拆解会真的花钱**:只要 M 第 2 批出的 head 带窗口或带 SWAP 里的字段,拆解就会生成变体。若 M 第 2 批又全是 `day_X(Ret)` 这种形状,拆解会再次是 0 —— 若连续两轮为 0,应在笔记里记下这是本实验里 B 组的一个结构性损失(48×3 次预算作废),作为判读时的已知局限。
7. E 位若用 `cs_bucket_*` 或 `cross_zscore` 类外围,`c05_periphery_seen` 的拒绝计数会很低(< 5),因为 `SEEN` 至多 4 个元素;而 `c05_skeleton` 和库 ρ 禁令的拒绝计数会高得多。
