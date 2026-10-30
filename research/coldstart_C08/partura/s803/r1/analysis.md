# 解剖:种子 803,P 组,第 1 轮

快照 `c07s803M1_I0_open_search`(M 第 1 批)。本文只用 train / valid 口径的材料,引用的表达式一律写原文。

## 0. 一句话结论

**本轮快照是空的**:0 个 head、共性表 0 行、拆解 0 次(`paid: 0`)、核心卡 0 张、R 候选 0 个,而归档里有 43 个已评分候选。
按规则 §2 与 `scripts/c06_check.py` 的确定性检查,**E 位与 R 本轮都不可能合法**,所以本轮两个任务位必须都是 N。
下面给出:(1) 为什么空、空意味着什么与不意味着什么;(2) 在这个奖励口径下结构性还剩哪些空地(这部分有代码依据,不是臆测);
(3) 三个可以直接拿去写 N 种子的机制族与具体写法;(4) 4 个文献题目。

## 1. 原材料盘点(事实,全部来自 loc.json / loc.md)

| 项 | 值 |
|---|---|
| 快照 | `c07s803M1_I0_open_search`(只有 M 的第 1 批) |
| 已生效的 R 替换 | 0 |
| heads | **0 个**(heads 表是空表) |
| 已评分归档候选 `n_archived` | 43 |
| 共性表 `enrichment` | **0 行** |
| 拆解 `ablation` / 付费评估 `paid` | **0 / 0** |
| 机械核心卡 `core_cards` | **0 张** |
| R 候选 `r_candidates` | **0 个** |
| 本组之前各轮任务 `missions_before` | `[]`(第 1 轮) |

另外我确认过(`ls -laR`):本种子目录下**只有** `r1/loc.json` 与 `r1/loc.md`。
`notebook.md` 不存在,也没有任何 `missions_final.yaml`、`audit_record.json`、`R_prev.json`、`lit.md`。
所以任务里「之前各轮的文件」这部分**不是读不到,而是确实还没有**。

### 1.1 这是硬约束,不是口味问题(引代码)

- `scripts/c06_check.py:87-95`:合法核心的集合 `known` = 快照里每个 head 的全部子树 ∪ `loc["enrichment"]` 的子树 ∪ `loc["core_cards"]` 的核心。
  本轮这三者都是空的 → `known` 是**空集**;`:115-116` 会对任何 E 核心报
  `the core is not a subtree of a snapshot head nor a locate subtree`,`c06_check.py` 直接退出码 1。
- `scripts/c06_check.py:137-141`:R 的 `head` 必须出现在 `loc.json` 的 heads 里,本轮任何 R 组都会报 `the head is not in the snapshot`;
  即使混过去,`scripts/c05_locate.py:208-210` 的 `direct` 模式还会 `SystemExit`。

**给 PI 的直接建议**:`missions.yaml` 写 2 个 N 位、`R` 留空。16 个 R 变体的预算本轮用不掉,**不要为了用掉它去硬凑**一个不存在的 head。

### 1.2 共性表为空的四个结构性原因(请不要读成「M 的候选里没有共用部件」)

1. **归档本身是按家族去重的**。GP 的 `archive_dedup`:日度秩相关 ≥ 阈值的树算同一个家族,归档只留家族里最好的那一个
   (`AlphaCube/src/alphacube/mining/gp.py:330-342` 与 `:573-627`)。所以这 43 行是 **43 个互相不像的代表**,天然不共用结构。
2. **只数「字符串完全相同」的子树**。`c05_locate.py:304` 的键是 `repr(n)`,窗口与常数都算在身份里:
   `cross_mean(day_std(Ret), 20)` 与 `cross_mean(day_std(Ret), 10)` 不是同一个子树,`day_std(Ret)` 与 `day_std(Vwap)` 也不是。
3. **只数日频子树**。同一行的筛选条件是 `n.operands and n.shape.collapsed and n.shape.degenerate`:
   分钟形状的中间结构(所有 `in_*` 链、裸 `Close` / `Ret`)**永远进不了共性表**,而日内因子的差别恰恰常常就在那一层
   (`AlphaCube/src/alphacube/expression.py:29-41` 的 `Shape`;`collapsed` 才算日频)。叶子因为没有 operands 也被排除。
4. **出现次数门槛**:`c05_locate.py:316` 要求 `4 ≤ n ≤ 0.7 × 43 ≈ 30`。

**结论**:在只有 M 第 1 批、且归档按家族去重的情况下,共性表为空几乎是默认结果,它**不构成**「这颗种子没东西」的证据。
真正带信息的只有一条:**M 第 1 批 43 个已评分候选里,没有一个被收成 head** —— 即没有一个 score ≥ 0.5,或达到了却与已知族 |ρ| ≥ 0.5 被判不合格。

## 2. alpha 的来源:本轮无法定位(并说清缺的是哪几类证据)

任务要的四类证据——共性(均值差、p、含它的候选数)、充分性(子树单独当因子的 score)、必要性(knockout 掉多少分)、
敏感性(换同类字段 / 窗口减半加倍)——**在 loc.json 里全部是空的**:`ablation` 为空是因为没有 head 可拆(`c05_locate.py:332` 的 `todo` 取自 heads),
`paid: 0` 说明一次付费评估都没发生。规则 §5 又禁止我读 `episodes/`,所以那 43 个候选的表达式我看不到。
**因此本轮任何「哪个子树是真来源」的断言都只能是编造,我不写。** 本节改为写「来源在结构上只能落在哪里」——这部分全部有代码依据。

### 2.1 奖励口径已经把可能的来源削得很窄

依据 `scripts/c05_locate.py`、`partura/steer.py`、`partura/books.py`、`AlphaCube/src/alphacube/label.py`:

**(a) 根上的单调变换完全无效。** 值先在截面上转成排名再做 EMA(`steer.py:409-417` 的 `signal_input`,规则 §1)。
于是外层的 `log`、`sqrt`、`abs_`(对非负量)、`cs_rank`、`cs_scale`、`cs_normalize`、`cs_robust_z`、`cross_scale` 等保序包装**都是同一个信号**。
只有**改变截面排序**的非单调组合才算新东西:两个量的差、`abs_` 作用在可正可负的量上、桶内去均值、状态翻转、比值。
→ 对 N 的直接含义:16 个种子要在**结构**上不同;靠外层包装凑数量,实际上只有三四个独立信号,审计划掉几个就不够 4 个了。
→ 一个具体例子:`day_durbin_watson(Ret)` 与 `day_autocorr(Ret, 1)` 近似是 DW ≈ 2(1−ρ) 的关系,在同一窗口下几乎同一个量,不要花两个种子。

**(b) 五个控制及其平方、三次方已被去掉**(`steer.py:420-441`,`PARTURA_NEUTRAL_POWERS=1,2,3`;控制的写法见 `c05_locate.py:117-119`):
`cross_mean(day_sum(Amt), 30)`(流动性)、`cross_mean(day_std(Ret), 20)`(波动)、
`div(day_last(Close), ts_delay(day_last(Close), 20))`(20 日反转)、`cross_mean(day_std(Amt), 30)`(已知族)、`LogFloatCap`(市值)。
→ 「成交额水平」「成交额日内离散度」「20 日波动」「20 日反转」「市值」这五个形状,连 U 形与 S 形暴露一起,**都已经不可能是 alpha 的来源**。
→ 注意 `liq` 与 `known` **都是 Amt 做的**:凡是把「成交额有多大 / 多散」当主语的写法都在这条线上。
→ **最省力的躲控制设计模式**:五个控制都是**截面水平量**;把一个量改写成「相对自身历史的偏离」——
  `sub(x_快, x_慢)` 或 x 减自身 60 日中位数——在结构上就与截面水平量近似正交。本文第 4 节的种子大量用这一招。
→ 另一招:控制的表达式是公开的,可以**直接把控制当减项**写进种子,例如
  `sub(cross_mean(day_wstd(Ret, Amt), 20), cross_mean(day_std(Ret), 20))` —— 剩下的正是波动控制解释不掉的那部分。

**(c) 没有被控制、因此特别容易「只是代理」的三条缝**:
- **价格水平 / 最小变动价位的相对大小**。价格不在五个控制里,而很多日内微观量机械地随 1/价格 变化
  (分钟收益的一阶自相关、`day_distinct_ratio(Close)`)。这是本环境最典型的代理风险。
- **上市年龄 / 次新股**。本研究的奖励 kind 是 `long_neutral`,而 `steer.py:648` 的 `mask` 只对 `long_tradable` / `long_bucket` / `long_marginal` 生效
  → **次新股与常停牌股没有被从多头书里剔掉**(定位脚本里算出来的 `untradable` 在这个口径下不起作用);
  只有「次日开盘窗口整段涨停锁死」的标的因为 `label_buyable=True` 被置 NaN(`label.py:16-20`)。
  所以「买次新」可以在样本内拿到分,而完全不是机制。拿到 head 之后一定要查它对 `ListAge` / `cross_valid_count(day_last(Close), 241)` 的依赖。
- **涨跌停宽度与板块**。`LimitWidth`、`BoardCode` 是离散叶子,自己当根会死在 `distinct_fraction ≥ 0.5` 的门槛上
  (`diagnose.py:136-146`、`c05_locate.py:162-163`),只能当**条件 / 分组**用。

**(d) 标签决定了哪段收益根本拿不到。** `target[t] = V[t+2] / V[t+1] − 1`,V = 当日 09:31–09:45 的 VWAP(`label.py` 顶部 + `ps.target(1)`)。
因子用到 t 日收盘为止的信息,**在 t+1 早盘那 15 分钟买入**。
→ **close(t) → open(t+1) 的隔夜跳空不归我们**:预测收盘后跳空的信号(尾盘委托失衡、收盘集中度)其预测力正好被买入价吃掉。
  能赚到的是 t+1 开盘 15 分钟之后的日内漂移,加上 t+1 → t+2 的隔夜。这条直接否掉了一整类「尾盘」写法,值得写进 notebook。

**(e) 成本与半衰期逼着信号必须「慢」。** 15 bp 乘换手(`books.py:62-71`),半衰期只有 0 / 5 / 20 三挡且在 train 上选(`steer.py:650-666`)。
十分位多头若每天整体换掉,单日成本约 30 bp。
→ **只有名次能持续几天以上的信号才可能到 0.5**。一次性日内冲击类的量必须先变成「持续的股票属性」(多日平均),
  或者变成「相对自身历史的偏离、而偏离本身有持续性」,才有机会。

**(f) 两道门槛与热身期。** `coverage ≥ 0.9`(在有标签的格子上)且 `distinct_fraction` 中位数 `≥ 0.5`(`c05_locate.py:162-163`):
离散 / 标志类、取值很少的比例量直接「门槛废品」。另外 `PanelSet(..., warmup=60)`(`c05_locate.py:113`),
而 `rolling_windows` 左侧补 NaN(`operators/common.py:426-437`)→ **窗口 ≤ 60 个交易日最干净**;
写 241 这种窗口,train 前约 181 个交易日是在「爬坡中的窗口」上算的,正落在规则 §4 的「结果主要由热身期决定」上。

### 2.2 「真来源 vs 只是代理」:本轮只能做成设计期的筛子

规则 §4 的三类陷阱,逐条当清单用:
- **前视**:`day_*` 用的是 t 日整天、t 日收盘后才下单,没有前视;`in_zscore_expand` 是日内因果的。注意不要用任何跨日负位移的 shift。
- **数值伪影**:**不要用 `div` 去除一个会过零的量**(`day_mean(Ret)`、`day_std` 在锁死日为 0)。
  `ops_ext.py:665-683` 的 `day_es_ratio_hi` 文档正好记了这个教训:手写的 `erm_*` 用 `+1e-6` 兜底,锁死日分位数为 0 被救成 ~1e4,
  于是因子读的是「有没有锁死日」而不是尾部形状。要除就用自带近零保护的算子(`day_es_ratio_hi/lo`、`day_gini`)。
- **定义坏掉**:窗口 > 60 的热身期污染;`cs_bucket_demean` 在桶内不足 2 个名字时给 NaN(`ops_ext.py:462-478`)→ 用离散叶子分桶时要留意 coverage。

**代理的三个具体嫌疑(本环境)**:价格水平、上市年龄、停牌 / 锁死比例。
下一轮一旦有 head,定位工具会自动给出敏感性两行——`swap`(`Close↔Vwap`、`Volume↔Amt`、`High↔Low`、`Open↔Close`,`c05_locate.py:59`)
与 `window` 减半 / 加倍(`:361-368`)。**换同类字段就掉得厉害 = 它读的是那个字段的特殊性,不是机制**;窗口减半加倍就翻脸 = 过拟合到某个长度。
这两行是区分真来源与代理最便宜的证据,下一轮优先看。

## 3. 烂部件:本轮一个都报不出

`ablation` 空、`r_candidates` 空、没有 head → 没有「必要性 ≤ 0」或「换掉反而更好」的部件可报,R 组本轮一定不合格(§1.1)。

下一轮一旦有 head,`c05_locate.py:326-374` 会自动做:最多 4 个 head × 最多 12 个变体
(4 个 sufficiency 子树、4 个 knockout、2 个 swap、2 个 window),R 候选的判定是**变体 score ≥ 原 head + 0.1 且 |ρ_known| < 0.5**
(`:384-390`),与原 head ρ ≥ 0.5 则替换、< 0.5 且与库里所有 head |ρ| < 0.7 则收录(规则 §2)。

→ **本轮 N 的一个附带目标就是「造出至少一个 head」**。否则第 2、3 轮同样没有合法核心、也没有 R 可做,
P 组「深挖 + 去烂部件」的机制整个实验一次都用不上,只剩两个普通 N——那就与对照组没有区别了。这一点建议 PI 写进 notebook 的事先信念里。

## 4. 本轮候选

### 4.1 E 位:不可做

合法核心 0 个(§1.1)。不要尝试拿 M 归档里的候选当核心:它们不是 head,也不在共性表 / 核心卡里,`c06_check.py` 会拒。

### 4.2 R:无目标

### 4.3 替代「核心」的三个机制族(给两个 N 位用)

先说一句**诚实的限制**:我看不到 M 那 43 个候选的表达式(规则 §5 禁读 `episodes/`),
所以**无法列出「这些机制周围已经见过哪些外围写法」**。本轮防重复只能靠库禁令(骨架相同、或与库里 head 日度秩 ≥ 0.7 自动拒),
PI 不必也无法手工避开 M 的写法。以下每族我给:机制、为什么躲得过五个控制、写法、代理嫌疑与自检。

另外提醒一个**命名陷阱**:在这套算子语言里 `cross_*` 是**沿交易日轴**滚动(DT 面,compute_axis = D),
`cs_*` 才是**当日横截面**(ND 面,axis = S),`ts_*` 也是沿日轴。`cross_mean(day_sum(Amt), 30)` 是「30 日均成交额」,不是截面均值。

---

#### 族 A:日内交易的**时点**(when,而不是 how much)

**机制**:同一个成交额水平,可以是早盘集中放量,也可以是尾盘才有人买。日内成交的「重心」是一个**无量纲、与成交额大小无关**的形状量,
它刻画的是这只股票被什么样的参与者交易(日内高频 / 尾盘配置)。这类「习惯」在个股上是持续的,所以在 15 bp 成本下活得下来(§2.1e)。
**为什么躲得过控制**:重心是 [0,1] 的比例,与 `day_sum(Amt)`、`day_std(Amt)`、`LogFloatCap` 没有机械的单调关系;
五个控制里没有任何一个带日内时间轴的信息。

写法(`day_centroid`、`in_index` 见 `partura/ops_ext.py:155-171` 与 `:684-694`):

- `cross_mean(day_centroid(Amt), 20)`
- `cross_mean(day_corr(in_index(Volume), Volume), 20)` ——「放量是不是后置的」(算子文档里的原例)
- `sub(day_centroid(Amt), cross_mean(day_centroid(Amt), 20))` —— 今天的时点相对自身习惯的偏离
- `sub(cross_mean(day_centroid(Volume), 5), cross_mean(day_centroid(Volume), 60))` —— 习惯本身在漂移
- `cross_stddev(day_centroid(Amt), 20)` —— 时点有多不稳定
- `cross_mean(day_corr(in_index(Amt), abs_(Ret)), 20)` —— 波动是不是后置的

**代理嫌疑**:重心会随「有没有一次性大单」而跳;自检用 swap(`Volume↔Amt`)——两者结论应当一致,
若 `Amt` 版本明显更好,说明读的是价格水平而不是时点。

---

#### 族 B:日内**买压** —— 成交加权与等权之差(谁在推价)

**机制**:没有逐笔数据时,「钱是在上涨的分钟里成交的,还是在下跌的分钟里成交的」就是订单失衡的代理。
`day_signed_ratio(Ret, Amt)` 正是「上涨分钟成交额占比 − 下跌分钟成交额占比」∈ [−1,1](`ops_ext.py:122-134`);
`sub(day_wmean(Ret, Amt), day_mean(Ret))` 是「钱经历的收益 − 分钟平均收益」,差额的符号说明成交是否推动了价格。
**为什么躲得过控制**:两者都是**比例 / 差额**,分母把成交额的量纲约掉了;等权收益那一项还把日内收益水平也减掉了。

写法:

- `cross_mean(day_signed_ratio(Ret, Amt), 10)`
- `sub(day_signed_ratio(Ret, Amt), cross_mean(day_signed_ratio(Ret, Amt), 20))`
- `cross_mean(sub(day_wmean(Ret, Amt), day_mean(Ret)), 20)`
- `cross_mean(sub(day_topw_mean(Ret, Volume), day_mean(Ret)), 10)` —— 最重的 10% 分钟的平均收益减去全天平均(`ops_ext.py:635-645`)
- `cross_mean(day_signed_ratio(in_demean(Close), Amt), 20)` —— 成交额有多大比例成交在**当日均价之上**
- `sub(cross_mean(day_wstd(Ret, Amt), 20), cross_mean(day_std(Ret), 20))` —— 「钱经历的波动」减去**波动控制本身**

**代理嫌疑**:买压与反转控制 `div(day_last(Close), ts_delay(day_last(Close), 20))` 在方向上可能同向;
好在反转的线性 / U 形 / S 形都已被残差去掉,剩下的是日内结构。自检:把 10 日平均换成当天值,
若当天值远好于 10 日平均,说明它主要在吃当日反转而不是持续的买压。

---

#### 族 C:日内微观**持续性 / 隐含价差的变化**(流动性冲击)

**机制**:分钟收益的一阶自相关为负是买卖价差弹跳(Roll 的思路),其绝对大小是**有效价差**的代理。
但横截面上的**水平**几乎就是「贵 / 便宜 + 流动性」,所以水平不能直接用;
**能用的是「相对自身常态的突变」**——流动性冲击,它预示之后几天的流动性溢价。
**为什么躲得过控制**:自身历史标准化之后,与五个截面水平量结构上近似正交(§2.1b)。

写法(`day_ar1_coefficient`、`day_autocorr(x, n)`、`day_hurst` 见 `AlphaCube/src/alphacube/operators/dt_day.py:252-365`;
`day_distinct_ratio` 见 `partura/ops_ext.py:607-620`):

- `sub(cross_mean(day_ar1_coefficient(Ret), 5), cross_mean(day_ar1_coefficient(Ret), 60))`
- `sub(cross_mean(day_autocorr(Ret, 1), 5), cross_mean(day_autocorr(Ret, 1), 60))`
- `cs_bucket_demean(cross_mean(day_ar1_coefficient(Ret), 20), day_last(Close))` —— 在**价格十分位内**去均值,正面消掉价格水平代理
- `cs_bucket_demean(cross_mean(day_distinct_ratio(Close), 20), day_last(Close))` —— 同价位同行里,一天走过的价位数有多少
- `sub(cross_mean(day_hurst(Ret), 10), cross_mean(day_hurst(Ret), 60))`

**代理嫌疑(本族最大)**:价格水平。**必做的自检**:同时交一个按价格桶去均值的版本和一个不去均值的版本;
若不去均值的明显更好,说明这一族读的是低价股,不是微观流动性——那它就只是代理,规则 §4 不会挡它,但它在样本外最容易死。

---

#### 跨族写法:只在某种市场状态下用一个信号

`cs_state_rank(x, d)` 给出一个**每天对所有股票相同**的市场状态(`ops_ext.py:547-560`)。
**重要:`mul(cs_state_rank(...), x)` 单独写是空操作**——每日一个正的常数乘上去不改变当日截面排序,
在 rank-first 口径下完全没有效果。按算子文档,唯一正确的用法是**在两个信号之间加权**,或者用 `cs_flip_by_state`:

- `cs_flip_by_state(cross_mean(day_signed_ratio(Ret, Amt), 10), day_sum(Amt))` —— 市场活跃时顺着用,清淡时反着用
  (若只是「另一种状态下失效」而非反转,翻转版会明显更差,这本身就是检验,见 `ops_ext.py:562-578`)
- 两信号加权的形式按 `cs_state_rank` 文档的 `add(mul(s, a), mul(sub(1, s), b))` 写;**常数的写法以 `c06_check.py` 能解析为准**,
  PI 写完先跑一次 `scripts/c06_check.py 803 1`。

### 4.4 给 PI 的事先预期(可被证伪,便于下一轮对账)

1. 族 A / 族 B 的「多日平均」版本比「当日值」版本更可能过线(成本与半衰期的约束,§2.1e)。
2. 族 C 不按价格桶去均值的版本若明显更好,则它是价格水平的代理,样本外会消失。
3. 任何本质上是 `Amt` 水平或日内离散度单调函数的种子,残差后接近噪声,score 会贴近 0,而不是负很多。
4. 本轮最可能的失败模式不是「机制错」,而是**门槛废品**(`distinct_fraction < 0.5`,比例类算子取值太少)与
   **与控制 |ρ| 过线被自动划掉**。建议每个位的 16 个种子里,至少有 6 个是「差额 / 自身历史标准化」形式。

### 4.5 关于审计的一个提醒

`c06_check.py:43` 里控制划线的默认值是 `C06_CTRL_STRIKE=0.5`(由 `workflows/c06_round.js:23` 的 `--ctrl_strike` 传入),
而规则 §3 写的自动划掉线是与控制 |ρ| ≥ 0.8。两者不一致时**按工具实际生效的那个**执行。
稳妥的做法是把种子与五个控制的**原始秩** |ρ| 压到 0.5 以下——「差额 / 自身历史标准化」形式天然满足这一点。

## 5. 文献题目(给文献员,4 个)

**题目 1(对准族 A:日内成交时点)**
文献里如何构造与标准化「日内成交量的时间分布」类特征(成交量重心、尾盘 / 早盘成交占比、相对日内 U 型的偏离),
这些特征用什么方式做横截面标准化、用多长的平均窗口,以及它们在控制了规模与流动性之后是否仍有横截面预测力?
- 中文关键词:日内成交量分布、成交量重心、日内交易时点、尾盘成交占比、日内 U 型偏离、分钟成交量形态
- English: intraday volume distribution, volume centroid / center of mass, late-day volume share, intraday U-shape deviation,
  intraday trading time preference, cross-sectional return predictability

**题目 2(对准族 B:日内买压)**
在没有逐笔 / 委托簿数据、只有分钟 K 线的条件下,文献用哪些方法构造订单失衡与主动买压的代理
(上涨分钟成交额占比、成交加权收益与等权收益之差、最重分钟的收益、均价之上成交占比),
它们各自怎么归一化,持续期多长,预测的是哪一段收益?
- 中文关键词:订单失衡代理、主动买卖压力、成交额加权收益、分钟级买卖压力、均价之上成交占比、知情交易代理
- English: order imbalance proxy from minute bars, signed turnover / volume share, volume-weighted vs equal-weighted intraday return,
  buy-sell pressure without tick data, informed trading proxy

**题目 3(对准族 C:隐含价差与价格水平混淆)**
以收益自协方差为基础的有效价差 / 流动性度量(Roll 估计及其后续改进)在实证中如何构造,
以及文献如何处理它与**价格水平、最小变动价位**的机械混淆(分桶、标尺化、用变化量而非水平量)?
这类度量的「冲击 / 变化」形式是否比「水平」形式有更干净的预测力?
- 中文关键词:隐含价差、Roll 价差估计、买卖价差弹跳、有效价差度量、最小变动价位、低价股混淆、流动性冲击
- English: Roll effective spread estimator, bid-ask bounce autocovariance, high-frequency illiquidity measures,
  Corwin-Schultz spread, tick size effect, price-level confound, liquidity shock vs liquidity level

**题目 4(对准整个口径:中性化之后还剩什么,以及次新股污染)**
在已经中性化了规模、流动性、波动与短期反转(含非线性暴露)之后,A 股的日内 / 分钟级特征还剩多少横截面预测力?
相关研究用什么样的中性化与分组方式?以及这类研究如何处理**上市年龄 / 次新股**与停牌样本的污染(本环境没有把次新股剔出多头书)?
- 中文关键词:风格中性化后的残差预测力、A 股日内特征、分钟数据因子、次新股效应、上市年龄、停牌样本处理
- English: residual predictive power after size/liquidity/volatility/reversal neutralization, China A-share intraday characteristics,
  minute-bar factors, newly-listed / IPO-age effect, double-sorted controls, suspension sample bias
