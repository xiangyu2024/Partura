# 结构解剖:种子 804,P 组,第 1 轮

快照 `c07s804M1_I0_open_search`。**0 个 head、0 次拆解评估(`paid: 0`)、0 个 R 候选、0 个之前的任务。**
唯一的证据是 117 个已评分候选上的共性表(12 行)。

---

## 0. 先说清楚本轮有什么证据、没有什么证据

任务要求用「共性 / 充分性 / 必要性 / 敏感性」四类证据说话。本轮**只有共性一类**:

| 证据 | 本轮有没有 | 为什么 |
|---|---|---|
| 共性(均值差、p、含它的候选数) | **有**,12 行 | `c05_locate.py` 对 117 个 archive 候选做的子树存在性检验 |
| 充分性(子树单独当因子的 score) | **没有** | 充分性变体只在 `ablation` 分支里生成,而 `todo = [h for h in heads ...]`;heads 为空 → `plans` 为空 → `paid: 0` |
| 必要性(跳过一个算子掉多少) | **没有** | 同上(`knockout` 也只对 head 生成) |
| 敏感性(换同类字段 / 窗口减半加倍) | **没有** | 同上(`swap` / `window` 也只对 head 生成) |

所以**本轮任何「真来源」的判断都不能靠定位工具的数字**,只能靠(a)共性表内部的算术一致性,(b)算子源码。我下面两样都用,并且把每一条结论写成第 2 轮可以零成本验证的预测(§3.2)。

共性表本身的统计口径也要先打折扣(`c05_locate.py` 第 311–322 行):

- `p` 是**单侧 Mann–Whitney U**(`alternative="greater"`),**没有做多重比较校正**,而表是按 `effect` 排序后取前若干行的 —— 选择性偏差未修正;
- 检验里**没有控制树的大小 / 深度 / 换手**,是纯观察性的;
- 门槛只有 `n_with >= 4`,所以 `n_with = 4 / 5` 的行(`pow_05(cross_ema(LogFloatShares, 241))`、`cs_last_high20(day_pos_ratio(Open), cs_normalize(day_gini(High)))`、`ts_var(LogFloatShares, 10)`)基本上是单个家族的几个近亲重复计数;
- **117 个候选全部是通过了门槛的**(`c05_lib.archive` 只收 `score_p_score` 有限的行;`evaluate` 里 `gate = coverage >= 0.9 and distinct >= 0.5`)。这一点后面很关键。

还有一件事必须先讲明:**117 个候选的表达式原文不在 `loc.md` / `loc.json` 里**。共性表只给了子树。所以 E 位规则「外围不得与已见过的含该核心的候选相同」,PI 单靠定位输出**无法自己核对**;只能靠 §2 说的库禁令(GP 自己拒)兜底。我在 §4 里把共性表能反推出的「已见过的外围」逐个列出来,这是能做到的上限。

---

## 1. alpha 的来源

### 1.1 第一步:把 12 行折叠成 4 个东西(单调变换恒等)

奖励口径是「每天先在截面上转成排名」(`PARTURA_RANK_FIRST=1`,`scripts/server/c08_conductor.sh` 第 7 行强制检查;`steer.py:signal_input`)。规则 §1 明说:**任何单调变换是同一个信号**。源码确认这张表里有三个算子是恒等的:

- `pow_05` → `operators/common.py:209 pow_()`:`e <= 1` 时是 **sign(x)·|x|^e**,在整条实轴上严格单调递增 → **`pow_05(X)` 与 `X` 的日度截面排名逐格相同**。
- `cs_normalize` → `operators/nd_cs.py:286`:逐日 `(x - mean) / std`,正尺度仿射 → **`cs_normalize(X)` 与 `X` 的日内排名相同**。
- `cross_ema(X, 241)`:半衰期 241 天的 EMA。`LogFloatShares` 是只在股本事件日跳一次的台阶函数,241 天 EMA ≈ 它自己的一年滞后均值,排名与自身高度重合(不完全恒等,见 §4.3 N-a)。

折叠后,12 行其实是 **4 个不同的东西**(外加一个板块叶子):

| # | 真正的东西 | 表里的写法(全部是同一个排名或其近亲) | 均值差 / p / n |
|---|---|---|---|
| A | `day_pos_ratio(Open)` | 它自己;`cs_last_high20(day_pos_ratio(Open), cs_normalize(BoardCode))`;`cs_last_high20(day_pos_ratio(Open), cs_normalize(day_gini(High)))` | +0.69 / 0.000 / 31;+0.64 / 0.003 / 10;+0.44 / 0.024 / 4 |
| B | `LogFloatShares`(静态规模) | `pow_05(LogFloatShares)`;`pow_05(cross_ema(LogFloatShares, 241))`;`cross_ema(LogFloatShares, 241)`;`cross_ema(LogFloatShares, 3)` | +0.58 / 0.018 / 8;+0.55 / **0.297** / 4;+0.48 / **0.319** / 17;+0.25 / **0.224** / 6 |
| C | `ts_var(LogFloatShares, 10)`(股本**变动事件**,与 B 不同) | 它自己 | +0.56 / 0.074 / 5 |
| D | `day_gini(High)`(日内价格离散 ≈ 波动) | 它自己;`cs_normalize(day_gini(High))`;`ts_var(day_gini(High), 10)` | −0.18 / 0.617 / 27;−0.01 / 0.061 / 8;−0.11 / 0.761 / 14 |
| E | `cs_normalize(BoardCode)`(板块归属) | 它自己 | +0.21 / 0.063 / 20 |

注意 B 家族里只有 `pow_05(LogFloatShares)` 的 p 显著(0.018),另外三行的 p 是 0.22–0.32 —— **它们的均值差是被「不含它」那一侧的几个极差候选拉出来的,秩检验不认**。表按 `effect` 排序掩盖了这件事。

### 1.2 把包含关系算出来:谁的提升是真的「广谱」

共性表给了 `n_with` 和 `mean_with`,包含关系是确定的(复合式的候选必然也含它的两个子树),所以可以反解出子集的均值:

- `cs_normalize(BoardCode)`:20 个候选,均值 **−0.9189**。其中 10 个是与 A 的复合式(均值 −0.5078)。
  → 另外 10 个(含 BoardCode 但不含 A 的)均值 = 2×(−0.9189) − (−0.5078) = **−1.33**,比 117 个的总体水平(约 −1.09 ~ −1.13)**更差**。
  **结论:BoardCode 自己不好。它那 +0.21 的提升 100% 来自与 A 的那 10 个复合式。**
- `day_pos_ratio(Open)`:31 个,均值 −0.5835。扣掉两个复合式(10 个 @ −0.5078、4 个 @ −0.6668)后,
  剩下 17 个的均值 = (31×(−0.5835) − 10×(−0.5078) − 4×(−0.6668)) / 17 = **−0.608**。
  **结论:A 的提升是广谱的 —— 它在任何结构位置上都把候选从「灾难」抬到「只是难看」,与它搭谁无关。**

「换个搭配也一样提升」正是**常数**的指纹,不是 alpha 的指纹。alpha 的指纹是「只在某些搭配下起作用」。

### 1.3 一个统一解释:这张表排的是**换手率**,不是 alpha

score 的定义(`steer.py:608` 的 `reward`,kind=`long_neutral`):残差后的**纯多头十分位书、等权、扣 15 bp**,对「有信号且有标签的名字的等权」取超额,取 train / valid 净夏普中较差的。

于是:**信号变得越快 → 日换手越高 → 15 bp 单边吃掉的越多 → 净夏普越负。** 按这个尺子,一个几乎不变的信号哪怕完全没有预测力,净夏普也只是「略负」(成本≈0、超额≈0);一个乱动的信号则会被成本砸到 −1 以下。

拿这把尺子去量共性表,**12 行的符号和大小全部对上**:

| 子树 | 变化速度 | 预测的均值差方向 | 实际 |
|---|---|---|---|
| `day_pos_ratio(Open)` | 常数(§1.4) | 最正 | **+0.69(最正)** |
| `cs_normalize(BoardCode)` | 静态分类 | 正 | +0.21 |
| `LogFloatShares` 家族 | 一年跳几次 / 241 天 EMA | 正 | +0.25 ~ +0.58 |
| `ts_var(LogFloatShares, 10)` | 绝大多数日子恒为 0 | 正 | +0.56 |
| `day_gini(High)` | **每天都变** | **负** | **−0.18** |
| `ts_var(day_gini(High), 10)` | 每天都变 | 负 | −0.11 |

数量级也对得上:总体 `mean_without ≈ −1.1`,慢信号组 `≈ −0.5`,差值 0.6 个夏普 ≈ 一个日换手 30–50% 的多头书一年被 15 bp 吃掉 12–18% 的量级。

> **这是本份解剖最重要的一条结论:第 1 轮的共性表里基本没有 alpha 信息,它是一张「慢 = 便宜」的排序表。**
> 直接把表头的核心拿去开 E,等于花 96 次付费评估重新发现「静态因子换手低」。

### 1.4 核心 A:`day_pos_ratio(Open)` —— **不是来源,是一个坏掉的叶子(§4 数值伪影:面板几乎是常数)**

源码(`partura/ops_ext.py:97–105`):

```python
@op("dt", "day", arity=1)          # 注意:没有 real_valued=True
def day_pos_ratio(x):
    """Share of finite minutes with ``x > 0`` (zeros count as not positive).
    On Ret: the fraction of up-minutes."""
    ok = torch.isfinite(x); n = ok.sum(-1)
    r = ((x > 0) & ok).sum(-1) / n.clamp(min=1)
```

即 `day_pos_ratio(x) = (有限且 >0 的分钟数) / (有限的分钟数)`。分母就是分子那一批的全集。**所以只要某个字段在「有限」的分钟上永远为正,这个算子就逐格等于 1.0**(全天无有限分钟时为 NaN)。

`Open` 是价格字段(`catalog.py:375 CUBE_FIELDS`;`synthetic.py:45` 把 Open 构造成正价格;规则 §4 说的是后复权价格,后复权价格恒正)。价格会不会在成交稀疏的分钟上变成 0 或 NaN?源码里有两处直接回答:

- `day_flat_ratio` 的 docstring(`ops_ext.py:82–88`):「**On a price field**: 1.0 = the quote never moved …; a liquid stock sits near 0.2–0.5.」
  → 价格字段在「没动」的分钟上**重复前一分钟的非零价格**,既不是 0 也不是 NaN,而且这类分钟占一只活跃股的 20–50%。
- `day_zero_ratio` 的 docstring(`ops_ext.py:274–279`):「On Ret: … minutes in which the price did not move (locked at the limit, suspended, **no trade**)」,而 `Ret = Close/Open − 1`;无成交分钟之所以让 Ret **等于 0**,正是因为 Open 与 Close 都被前值填充成同一个非零数。

两条合起来:**`Open` 在所有有限分钟上恒为正 ⇒ `day_pos_ratio(Open) ≡ 1.0`(或 NaN)。它是一个常数面板。**

它为什么没被已有的守卫拦住?守卫的逻辑在 `catalog.py:378–394`:

```python
boolean_output   = (distinct <= 2)
trivial_boolean  = (distinct <= 2 and _probe_constant_capable(fn, category, restores))
```

- `_probe_distinct_values`(`catalog.py:278`)用的探针是 **`torch.randn((40, 9))`** —— 有符号正态。`day_pos_ratio` 在上面返回 {0/9,…,9/9} 约 8–10 个不同值 ⇒ `distinct > 2` ⇒ 不是 boolean。
- `_probe_constant_capable`(`catalog.py:183`)的探针家族里**恰好有** `base = rand + 0.5`(**strictly positive**),它的 docstring 写的就是这个失效模式:「A predicate against a FIXED threshold collapses whenever the data sits on one side of it — `is_gt0` on an all-positive panel is all ones … and a constant panel carries no cross-sectional information, yet scores a spurious IC once arithmetic launders it into a legal root.」
- **但这个探针只在 `distinct <= 2` 时才被调用。** `day_pos_ratio` 是「对固定阈值 0 的判别再求均值」,因为求了均值而逃过了 `distinct <= 2`,于是那条正数探针**从来没对它跑过**。邻居 `day_flat_ratio`、`day_zero_ratio` 都显式带了 `real_valued=True`,`day_pos_ratio` 没有。

**它是这个项目自己写在源码注释里的那个陷阱,只是在一个技术细节上漏网了。**

那么它是怎么拿到有限 score 而没被 `gate` 挡掉的?`gate = coverage >= 0.9 and distinct >= 0.5`,常数面板 `distinct_fraction ≈ 1/N ≈ 0.0002`,单独当根必死。答案是**被 `cs_last_high20` 洗白了**:

- `_pct_rank`(`ops_ext.py:231–235`)用 `argsort(argsort(v, stable=True), stable=True)` —— **序数秩,并列按股票列序打破**;
- `_lexi`(`ops_ext.py:339–353`)的 docstring 自己说「The output itself keeps **ordinal ranks** of y, so it stays **free of ties**」。

所以 `cs_last_high20(常数, x)` 的输出是**无并列的**(`distinct_fraction = 1.000`),门槛必过,而它携带的信息只有两样:

1. **股票列序**(= 交易所 + 板块 + 上市批次,规则 §4 明说这是板块信息,**不得据此挡**);
2. **x 的排除筛**。

**裁决:A 是「只是代理」里最坏的一种 —— 一个被洗白的常数。它的 +0.69 是 §1.3 的换手效应(常数书零换手、零成本),不是 alpha。**
真正可能有东西的是那 10 个复合式里的**另一半**,即 E(板块筛),见 §1.6。

一个必须讲的衍生陷阱:**`SWAP` 表(`c05_locate.py:57`)把 `Open` 换成 `Close`,而 `day_pos_ratio(Close)` 同样恒等于 1。** 所以一旦这个核心进了 head、将来跑自动敏感性检验,「换同类字段 → score 不变」会被读成**稳健**,而真实原因是两边都是常数。对这个核心,自动 swap 检验是**空的**;有诊断力的替换是 `Open → Volume` 或 `Open → Ret`(都不在 `SWAP` 表里,必须显式点名)。

### 1.5 核心 B:`LogFloatShares` 家族 —— 真来源,但**被 E 的审计规则挡在门外**;它的价值在「差」里

`pow_05(LogFloatShares)` 与 `LogFloatShares` 排名逐格相同(§1.1)。而 `LogFloatCap` 是**第 5 个控制**(`c05_locate.py:118` 的 `"n_size": "LogFloatCap"`),并且

```
LogFloatCap = log(流通股数 × 股价) = LogFloatShares + log(股价)
```

A 股里 log 股价的截面标准差远小于 log 流通股数的,所以二者的秩相关很高。

> **给 PI 的硬警告:规则 §3「E 位还要求核心与每个控制的 |ρ| < 0.8」。`pow_05(LogFloatShares)`(以及 `cross_ema(LogFloatShares, 241)` 这两行)极可能在 size 列上 ≥ 0.8,直接把 E 位判不通过,白耗一次审计机会(每轮至多 3 次)。**

但反过来说,这个家族**为什么会在 117 个候选里反复出现**(8 + 17 + 6 + 4 次),是本轮最有价值的线索。残差口径只扣掉 `rank(LogFloatCap)` 及其平方、三次方,所以 `LogFloatShares` 中**与 LogFloatCap 正交的那一部分**活了下来,而那一部分正好是:

```
LogFloatShares − LogFloatCap = − log(名义股价)
```

**GP 一直在摸的不是「规模」(规模已经被控制掉了),而是「低价股」。** 它摸不到那个差,因为它需要同时拿到两个日频叶子并做减法。这直接给出 §4.3 的 N-b。

同理,`cross_ema(LogFloatShares, 241)` 在 17 个候选里出现而 p 只有 0.32(自己不显著),最自然的解释是:**GP 要的是 `LogFloatShares` 与它自己一年滞后值之差**(= 一年股本扩张率),它拿到了减数,但凑不出那个减法 → N-a。

**裁决:B 是真来源的「影子」:信号在差分里,不在水平值里。水平值本身与 size 控制几乎同一个东西,不该开 E。**

### 1.6 核心 C / E:`ts_var(LogFloatShares, 10)` 与 `cs_normalize(BoardCode)` —— 本轮唯一两个机制干净的核心

**C `ts_var(LogFloatShares, 10)`**(`operators/nd_ts.py:163`,沿日轴 10 日滚动方差)。`LogFloatShares` 只在股本事件日跳变(解禁、定增、回购、转股),其余日子逐日**位级相同** ⇒ 10 日方差**精确为 0.0**。所以这个面板是:

- 绝大多数名字恒为 0 的一个巨大并列块,
- 加上最近 10 天内发生过股本变动的那一小撮的正值。

**它是一个「股本变动事件探测器」,与 `LogFloatShares` 的水平值(= size 控制)几乎正交。这是整张表里唯一一个既不是常数、不是控制代理、也不是换手伪影的东西。**

代价是它单独当根会被门槛打成**废品**(并列块让 `distinct_fraction` 远小于 0.5)。但这**不妨碍它当 E 的核心**(门槛考的是候选整体,核心只被要求 `|ρ|(核心, 每个控制) < 0.8`,这一条它轻松通过)。而且它有一个数学上**正确**的用法:把它放在 `cs_first_*` / `cs_last_*` 的 **x(筛)**位置上。`_rank_block`(`ops_ext.py:326–336`)的设计就是为这种情况:

> 「The band is made of whole **TIE BLOCKS** of x: a block of equal x values is in the band only if all of it fits inside (lo, hi].」

0 的并列块宽于 20%/40%,**永远不会被选进 band**,于是 band 精确地只选中正值那一小撮。`cs_first_high40(y, ts_var(LogFloatShares, 10))` = 「交易 y,但把最近有股本变动的名字顶到最前」。

**E `cs_normalize(BoardCode)`** ≡ `BoardCode`(§1.1)。`BoardCode` 是少数几个取值的静态分类(主板 / 创业板 / 科创板 / 北交所)。`cs_last_high20(y, cs_normalize(BoardCode))` 在 `_rank_block` 的整块逻辑下 = **「把代码最高的那个(些)整板块排除出多头书」**,也就是一个**板块排除筛**。这是一个有真实机制的东西(不同板块涨跌幅限制、投资者门槛、可交易性都不同,15 bp 成本下排除难做的板块确实该有帮助)。

但 §1.2 算出来:**含 BoardCode 而不含常数 A 的那 10 个候选均值 −1.33,比总体还差。** 所以板块筛**目前没有任何独立证据**支持;它在表里的 +0.21 全是 A 的常数效应借给它的。

**裁决:C 是本轮唯一值得开 E 的核心(机制清楚、与控制正交、算子层面有正确用法)。E 机制上合理但证据为零,只能排第二/第三,且更适合拿更锋利的叶子(`LimitWidth`)去替它,见 §4.3。**

### 1.7 核心 D:`day_gini(High)` —— 波动控制的代理

`day_gini`(`ops_ext.py:135–152`)是**全天分钟 |x| 的基尼系数**。`High` 是价格,一天之内所有分钟的 High 彼此相差不到几个百分点,一组近似相等的正数的基尼 ≈ (平均绝对两两差) / (2×均值),数量级 0.002–0.01。**也就是说 `day_gini(High)` 实质上是一个「尺度无关的日内价格离散度」= 日内波动代理**,而波动正是 5 个控制之一(`"n_vol": "cross_mean(day_std(Ret), 20)"`)。

残差口径把对波动的线性 / U 形 / S 形暴露都扣掉了,剩下的是噪声 —— 它出现在 27 个候选里却**均值差 −0.18**,完全一致。

顺带记一笔(**不是** §4 的问题,不足以挡):`g` 的算式是两个都 ≈ 1.0 的量相减得到 ≈ 0.005 的结果,float32 下相对误差约 1e-5 量级,可用但偏噪。

**裁决:D 是控制的代理 + 高换手拖累,它是「烂部件」而不是来源。**

---

## 2. 烂部件(必要性 ≤ 0 / 换掉更好)

必要性这一列本轮**没有数字**(§0)。能拿来替代的最强证据是共性表的负效应与上面的机制判断:

| 部件 | 证据 | 为什么烂 |
|---|---|---|
| `day_pos_ratio(Open)` | 机制(§1.4):常数面板 | **最烂的一个,尽管它排在表头。** 它是一个死叶子,贡献为零;表面提升全是零换手。换掉它(`Open → Volume` / `Amt` / `Ret`)才有意义 |
| `day_gini(High)` | 均值差 **−0.18**,n=27(最大样本的负效应) | 波动控制的代理,且每天都变 → 吃成本 |
| `ts_var(day_gini(High), 10)` | 均值差 **−0.11**,n=14 | 波动的波动,仍是控制族,仍然快 |
| `cs_normalize(day_gini(High))` | 均值差 **−0.01**,n=8(p=0.061 → 秩上移但均值不动) | 只是避开了最差的尾部,没抬均值;与上同族 |
| `cross_ema(LogFloatShares, 3)` | 均值差 +0.25 但 **p=0.22**,是 B 家族里最弱的一行 | 对一个一年跳几次的台阶函数做 3 天半衰期 EMA ≈ 恒等包装,纯冗余 |
| `pow_05(…)` 这一层(两行) | 源码:`pow_` 在 `e<=1` 时严格单调(`common.py:209`) | **按规则 §1 它和没有它是同一个信号、同一个分。** 任何 `pow_05` 包装层都是零信息的冗余,且会白占 GP 的深度预算与库禁令的骨架位 |

> **但 R 本轮用不了。** 规则 §2「R 去烂部件:对快照里某个 **head** 给出去掉或替换部件的变体」,而 `c05_locate.py` 的 `direct` 模式会硬报错:
> `if bad: raise SystemExit("R requests name heads outside the snapshot")`。
> 快照里 **0 个 head** ⇒ **本轮 16 个 R 名额全部不可用**,`r_candidates` 也必然为空。两个任务位只能是 E / N。

---

## 3. 之前的任务

**本轮是第 1 轮,什么都没有。** `missions_before: []`;目录下只有 `loc.md` / `loc.json`,没有 `missions_final.yaml`、`audit_record.json`、`R_prev.json`、`notebook.md`。E 的外围与 heads、N 的结果、R 的替换与收录、审计员挡掉了什么、上一轮笔记的预测 —— **五项全部为空,无可比对。**

### 3.2 因此本轮改为**落下可检验的预测**(第 2 轮按这一节逐条打勾)

前四条**不花任何付费评估**:它们直接读本轮审计用的 `corr_<n>.md` / `.json` 的 `gate` / `distinct` / `coverage` / 控制列就能判。

| # | 预测 | 怎么验 |
|---|---|---|
| **P1** | `day_pos_ratio(Open)` 的 `distinct ≈ 1/N`(0.000–0.001),`gate = 废品`;且因为常数面板逐日相关系数是 0/0,**5 个控制列会印成 `nan`** | corr 表直接读 |
| **P2** | `pow_05(LogFloatShares)` 与 size 列(`LogFloatCap`)的 `|ρ| ≥ 0.8` → 作为 E 核心会被 §3 自动判不通过 | corr 表 size 列 |
| **P3** | `cs_normalize(BoardCode)`、`LimitWidth` 的 `distinct < 0.01` → 单独当根是废品,只能当筛的 x | corr 表 |
| **P4** | `ts_var(LogFloatShares, 10)` 的 `distinct < 0.5`(废品),但与**全部 5 个控制**的 `|ρ| < 0.3` | corr 表 |
| **P5** | `cs_last_high20(day_pos_ratio(Open), cs_normalize(BoardCode))` 的 `distinct = 1.000`、`gate = 过` —— **门槛抓不住它**,尽管它只携带股票列序 + 板块 | corr 表;这是 §1.4 洗白机制的判决性检验 |
| **P6** | 把 `Open` 换成 `Close`(即 `SWAP` 表的自动替换)后,含 A 的候选 score **几乎不变**;换成 `Volume` 则**大变** | 要付费;留给将来有 head 时的 R |
| **P7** | `sub(LogFloatCap, LogFloatShares)` 与 `day_last(Close)` 的秩相关为**高但明显 <1**(后复权价 ≠ 名义价)。若接近 1,说明我对两个叶子定义的推断错了,N-b / N-c 的立论要改 | corr 表(或任一含两者的候选) |

P1 / P5 一起成立,就等于**在不花钱的情况下证明了** A 是洗白的常数。若 P1 不成立(`distinct` 明显大于 0),则说明实盘立方体对无成交分钟确实填了 0,那么 `day_pos_ratio(Open)` 就是一个**真的分钟级成交频率(流动性)度量** —— 我的 §1.4 裁决整个反转,A 变成真来源。**这一条是本轮最该先看的一格。**

---

## 4. 本轮候选

### 4.1 值得深挖的核心(≤ 3 个)

合法核心集合:0 个 head ⇒ 只能取共性表 / 核心卡里的子树(规则 §2)。注意裸叶子(`BoardCode`、`LogFloatShares`)**不在**合法集合里 —— 共性表只收 `n.operands` 非空的节点,裸叶子不会出现在表里。

**① `ts_var(LogFloatShares, 10)` —— 首选,建议本轮唯一的 E 位**

- 理由:§1.6。整张表里唯一不是常数、不是控制代理、不是换手伪影的东西;股本变动事件探测器;P4 预测它与 5 个控制全部 `|ρ| < 0.3`。
- **已见过的外围(共性表能反推的):只有 `ts_var(·, 10)` 这个包装本身,n=5。** 同一家族中已被 M 用过的 `LogFloatShares` 包装层是 `pow_05`、`cross_ema@3`、`cross_ema@241`、`pow_05(cross_ema(…,241))`。
- **外围要避开的**:任何 `pow_05` 层(§2,零信息且与规则 §1 冲突);`cross_ema@{3,241}`(M 已反复用过,且库禁令会按骨架拒)。
- **外围值得试的**:把它放到筛的 x 位 —— `cs_first_high40(y, ts_var(LogFloatShares, 10))`、`cs_last_low20(y, ts_var(LogFloatShares, 10))`(`_rank_block` 对 0 并列块是正确的,§1.6);与上市年龄 / 冻结度交互(`cross_valid_count(day_last(Close), 241)`、`cross_max(day_zero_ratio(Ret), 15)`);窗口换成 20 / 60 天(把「最近有事件」拉长成「最近一季有事件」)。
- **给 PI 的提醒**:corr 表会把这个核心本身印成**废品**(P4)。这不是数学问题而是并列块,`_rank_block` 的 docstring 正是为它写的;建议 PI 在 missions 里把这句话写进去 —— 审计员读不到本文件(规则 §5),只能读 missions / corr / loc。

**② `cs_normalize(BoardCode)` —— 次选,机制清楚但证据为零**

- 理由:§1.6,板块排除筛是真实机制。
- **反对的证据要摆明**:§1.2 算出含它而不含常数 A 的 10 个候选均值 **−1.33**,比总体更差。+0.21 是借来的。
- **已见过的外围:`cs_last_high20(day_pos_ratio(Open), ·)`,n=10(占它 20 次出现的一半)。** 另外 10 次的写法共性表没有给(§0)。
- **外围值得试的**:换掉那个常数 y,把真信号放进 y 位 —— `cs_last_high20(<真 y>, cs_normalize(BoardCode))`;换更锋利的筛宽(`cs_last_high10` / `cs_last_high05`,`ops_ext.py:388` 的注释说「a screen is meant to remove 6–7% of the market, and a 20% quota takes two thirds of its victims from somewhere else」);或干脆用 `LimitWidth` 替掉 BoardCode(见 N-e,但那是 N 不是 E)。

**③ 不建议开 E 的三个(尽管它们排在核心卡前列)**

- `day_pos_ratio(Open)` 与两个 `cs_last_high20(day_pos_ratio(Open), …)` 复合式:§1.4。E 位要求**每个候选都原样包含核心**,96 次付费评估会全部挂在一个死叶子 + 股票列序上。
- `pow_05(LogFloatShares)`:§1.5,P2 预测它在 size 列上 ≥ 0.8,会被 §3 自动判不通过,白耗一次审计。

### 4.2 R 目标

**无 —— 本轮 R 不可用(§2 末尾)。** 快照 0 个 head,`c05_locate.py direct` 会直接报错退出。等到有 head 之后,第一批 R 变体我建议盯这三件事:① `day_pos_ratio(Open) → day_pos_ratio(Volume)`(诊断性替换,`SWAP` 表里没有,必须显式点名);② 砍掉任何 `pow_05` 层(应当 score 不变,是对规则 §1 口径的自检);③ `day_gini(High)` 整支换成 `day_centroid(Amt)`(把波动代理换成「钱在一天里什么时候成交」)。

### 4.3 N 的灵感

全部来自同一个观察:**GP 反复摸 `LogFloatShares` 家族,是因为它需要的信号在差分里,而它凑不出那个减法。** 四个日频叶子(`LogFloatShares`、`LogFloatCap`、`LogTotalCap`、`LimitWidth`)两两相减就能拿到三个 A 股里有名有姓、而且**从分钟立方体里根本算不出来**的特征。

- **N-a 一年股本扩张率**:`sub(LogFloatShares, cross_ema(LogFloatShares, 241))`(或 `sub(LogFloatShares, ts_delay(LogFloatShares, 241))`)。
  = 过去一年流通股数的对数增长 = 解禁 / 定增 / 转股的累计幅度。**这直接解释了 `cross_ema(LogFloatShares, 241)` 为什么出现在 17 个候选里却自己不显著(p=0.32):GP 拿到了减数,缺了被减数。** 对应国际上的「股票发行异象 / 综合股权发行」。慢变量 → 15 bp 下便宜。
- **N-b 低价股(名义股价)**:`sub(LogFloatShares, LogFloatCap)` = **− log(名义股价)**(§1.5)。
  关键点:残差只扣掉 `rank(LogFloatCap)` 及其幂,**名义股价这一维没有被控制**;而且它**无法用后复权的 `Close` 复现**(后复权价的截面排序是累计收益,不是价格水平,规则 §4 自己说了这件事)。这是本轮我最看好的一条。
- **N-c 自由流通比例 / 股权集中度**:`sub(LogTotalCap, LogFloatCap)` = − log(流通市值 / 总市值) = 限售与大股东锁仓的程度。`LogTotalCap` 是**完全没被 M 碰过**的叶子,同样算不出替代品,同样是慢变量。
- **N-d 修好 A:分钟级无成交频率**。`day_pos_ratio(Open)` 想做而没做成的那件事,有三个写对了的算子:`day_pos_ratio(Volume)`(成交量在无成交分钟确实是 0,不会被前值填充)、`day_zero_ratio(Ret)`、`day_flat_ratio(Close)`(docstring:活跃股 0.2–0.5,**有真实截面变化**)。
  额外的机制论据:`long_neutral` 这个 reward **不套 `untradable` 掩码**(`steer.py:648`,掩码只对 `long_tradable` / `long_bucket` / `long_marginal` 生效),而流水线自己判定「冻结」用的就是 `cross_max(day_zero_ratio(Ret), 15)`(`c05_locate.py:117`)。**也就是说,这一族正好补上了纯多头书缺的那道筛。** 正确用法是放在筛的 x 位:`cs_last_high20(y, cross_max(day_zero_ratio(Ret), 15))`。
- **N-e `LimitWidth` 当筛**:涨跌幅限制在 A 股里是 5%(ST)/ 10%(主板)/ 20%(创业板、科创板)。**一个叶子同时给出 ST 状态和板块,比 `BoardCode` 锋利**(ST 是主板里最该被纯多头书排除的一撮,而 BoardCode 分不出来)。取值只有几个 → 单独当根是废品(P3),但当 `cs_last_*` 的 x 完全正确(整块逻辑,§1.6)。这同时是对 ② 的更好替代。

实施上的两条注意:N 位「种子 ≤ 16 个、至多占初代一半」;上面五条每条都该配 2–3 个写法(不同窗口 / 不同筛宽 / y 位放不同东西),正好填满。另外 N-a ~ N-c 全是慢变量,而 §1.3 说明这把尺子本身偏爱慢变量 —— **所以第 2 轮判断它们时,必须拿「它比同样慢的常数基准好多少」来看,不能只看 score 比总体高。** 建议 PI 在本轮顺手把一个「纯慢基准」(例如 `cs_normalize(BoardCode)` 自己)放进 corr 请求里当标尺。

---

## 5. 给文献员的题目(4 个)

**题目 1 —— 对准核心 ① `ts_var(LogFloatShares, 10)` 与 N-a**
文献里怎么处理「流通股本的变动」这一类特征?具体问三件事:(a) 把它做成**事件哑变量**(解禁日、定增完成日前后的窗口)还是做成**连续的扩张率**,哪种在横截面回归里更稳?(b) 事件效应的持续期是多少个交易日 / 月(决定我该用 10 日还是 20/60 日窗口)?(c) 已有文献报告的符号是什么(股本扩张后跑输?解禁前抢跑?)
关键词:限售股解禁、定向增发、股本扩张、股票发行异象、事件窗口、流通股本变动 / share lockup expiration, seasoned equity offering (SEO), private placement, share issuance anomaly, composite equity issuance, net share issuance, equity expansion, China A-share

**题目 2 —— 对准 N-b(低价股)**
文献里对「名义股价水平」这个特征做过哪些处理?具体问:(a) 它在控制了市值 / 流通市值之后还有没有独立的横截面溢价(我的口径已经把市值秩及其平方三次方扣掉了)?(b) 常见的处理是取 log 股价、取股价分位、还是做低价股哑变量?(c) 它和彩票型偏好 / 散户比例 / 最大日收益(MAX)这些变量是什么关系 —— 会不会其实是同一个东西?
关键词:低价股效应、名义股价、股价幻觉、彩票型股票、散户偏好、送转股 / nominal share price, low-price effect, price level anomaly, nominal price illusion, lottery-like stocks, MAX effect, retail investor preference, stock splits, China A-share

**题目 3 —— 对准 N-c(自由流通比例)**
文献里怎么用「自由流通市值 / 总市值」这个比率(等价地:限售股占比、股权集中度)?具体问:(a) 它被当成风险因子、流动性代理,还是治理 / 大股东行为的代理?(b) 在中国市场有没有报告它对收益的横截面预测力,方向如何?(c) 它和换手率、流动性度量的相关性有多高 —— 我有一个 30 日成交额的流动性控制,想知道这个比率会不会被它吃掉?
关键词:自由流通比例、限售股占比、股权集中度、大股东持股、国有股、流通市值与总市值之比 / free float ratio, free-float-adjusted market cap, restricted shares, ownership concentration, insider holdings, state ownership, float-to-total-cap ratio, China A-share

**题目 4 —— 对准 N-d / N-e,以及核心 ① 和 ② 的「筛」用法**
文献里对「分钟级无成交 / 零收益的频率」这类微观流动性度量做过哪些处理,以及对**取值很少的分类型特征**(涨跌幅限制档位、ST 状态、板块)通常是当因子还是当**筛选条件**?具体问:(a) 零收益比例 / 零成交比例这类度量,常见是用日频零收益天数还是分钟级频率,报告的预测方向如何?(b) 它和成交额 / Amihud 这类流动性度量的增量信息有多少?(c) 做纯多头组合时,ST 与特殊板块通常是**事前剔除**还是作为因子暴露处理 —— 事前剔除对扣费后夏普的改善有多大?
关键词:零收益比例、零成交、分钟级流动性、买卖价差代理、涨跌停、ST 股票、特别处理、剔除规则、纯多头组合构建 / zero-return proportion, LOT measure (Lesmond-Ogden-Trzcinka), zero-volume days, intraday illiquidity, bid-ask spread proxy, Amihud illiquidity, price limits, special treatment (ST) stocks, exclusion screen, long-only portfolio construction, China A-share

---

## 附:本份解剖引用的源码位置(供复核)

| 结论 | 位置 |
|---|---|
| `day_pos_ratio` 定义、**没有** `real_valued=True` | `partura/ops_ext.py:97–105` |
| 价格字段在未成交分钟重复前值(非 0、非 NaN) | `partura/ops_ext.py:82–88`(`day_flat_ratio`)、`273–279`(`day_zero_ratio`) |
| 常数守卫的正数探针、以及它只在 `distinct<=2` 时才跑 | `src/alphacube/catalog.py:183–200`、`278–296`、`378–394` |
| 「被算术洗白的近常数指标拿到虚假 IC」这一已知失效模式 | `src/alphacube/catalog.py:353–369`;`cli.py:313–316` |
| `pow_05` 是全实轴严格单调 | `src/alphacube/operators/common.py:209–217` |
| `cs_normalize` 是逐日正尺度仿射 | `src/alphacube/operators/nd_cs.py:286–300` |
| 序数秩 + 并列按列序打破;`_lexi` 输出无并列 | `partura/ops_ext.py:231–235`、`339–353` |
| 整块(tie block)筛选逻辑 | `partura/ops_ext.py:326–336` |
| `day_gini` 算式 | `partura/ops_ext.py:135–152` |
| 门槛 `coverage>=0.9 and distinct>=0.5`;`distinct_fraction` 定义 | `scripts/c05_locate.py:168`;`partura/diagnose.py:136–146` |
| score = 纯多头十分位、扣 15 bp、min(train, valid) | `partura/steer.py:608–670`;`partura/diagnose.py:73–75` |
| `long_neutral` **不**套 `untradable` 掩码 | `partura/steer.py:648` |
| 5 个控制的表达式原文 | `scripts/c05_locate.py:116–118` |
| 共性检验 = 单侧 Mann–Whitney,无多重比较校正、不控树大小 | `scripts/c05_locate.py:300–323` |
| 充分性 / 必要性 / 敏感性只对 head 生成 ⇒ 本轮为空 | `scripts/c05_locate.py:328–370` |
| R 要求 head 在快照里,否则报错退出 | `scripts/c05_locate.py:206–209` |
| `SWAP` 表(`Open → Close`) | `scripts/c05_locate.py:57` |
| 奖励是 rank-first(单调变换同分) | `scripts/server/c08_conductor.sh:7`;`partura/steer.py:403–417` |
