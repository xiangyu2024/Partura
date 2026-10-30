# 结构解剖:种子 806,P 组,第 1 轮

快照 `c07s806M1_I0_open_search`(M 的第 1 批)。115 个已评分候选,**0 个 head**,`ablation: []`,`paid: 0`,`r_candidates: []`,`missions_before: []`。

---

## 0. 本轮我手上有什么证据,没有什么证据(先说清,后面每个结论都按这个打折)

任务要我用"共性 / 充分性 / 必要性 / 敏感性"四类证据说话。实际情况:

| 证据类型 | 本轮有没有 | 为什么 |
|---|---|---|
| **共性**(enrichment) | **有**,16 行 | 对 115 个已评分候选算的 |
| **充分性**(子树单独当因子的 score) | **没有** | 拆解需要 head;`scripts/c05_locate.py` 里 `todo = [h for h in sorted(heads, ...)][:MAX_HEADS]`,heads 为空 → `ablation: []`,`paid: 0` |
| **必要性**(knockout 掉多少) | **没有** | 同上 |
| **敏感性**(换同类字段 / 窗口减半加倍) | **没有** | 同上 |

所以这一份解剖**只有一类直接证据(共性)**,其余全部来自:(a) 对 loc.json 做的逐层算术分解(§2,精确,无需新评估);(b) 读算子源码得到的语义事实(§1,其中几条我用玩具张量跑过);(c) 由此推出的机制假设(§3,明确标为假设,每条都给判别实验)。凡是我没有证据的地方都写了"假设"。

还要注意:**所有 115 个候选的 score 都是负的**(全局均值 **-1.4421**,最好的一族均值 -0.47),离"发现"的 0.5 还差一个夏普。`partura/steer.py` 的 `reward` 里**方向与半衰期只在 train 上选**(`best` 按 `train` 的 `long_sharpe` 取),再 `score = min(s_tr, s_va)`。所以 -1.5 的含义是"train 上挑好的方向在 valid 上反过来了 / 或者 15 bp 把两个方向都吃穿了"。**本轮的 enrichment 衡量的不是 alpha 大小,是"换仓成本 + train→valid 翻转"这两种亏法减轻了多少。** loc.json 不带每个候选的 train / valid / turnover 分列,这个歧义我无法在本轮消掉(见 §7 的流水线请求)。

---

## 1. 算子语义:读源码得到的事实

数据是 `(D, M)` 的日 × 分钟张量(`n_minutes=241`,见 `scripts/c06_check.py`)。`day_*` 把分钟轴收成每日一个数,`cross_*` 沿**日**轴滚动。

1. **`Ret` 是分钟 bar 自身的收益**(`close/open - 1`,见 `alphacube/synthetic.py`;`partura/ops_ext.py` 的 `in_pct` 文档也写明 "On Close with d=1 this is the minute return (~ the `Ret` field)")。所以 `day_max(Ret)` = **当天最大的那一分钟涨幅**,一个日内跳跃 / MAX 型度量,几乎总是 ≥ 0。
2. **`day_max(Ret)` 恰好为 0 ⟺ 当天没有任何一分钟动过**(一字板封死、长期无成交的僵尸报价)。`day_max(Ret)` 为 NaN ⟺ 当天整天缺失(停牌 / 未上市)—— `ops_ext.cross_valid_count` 的文档直说:"The cube has no listing date and no suspension flag; **both show up only as NaN patterns**"。
3. **`cross_product(x, 3)` 把 NaN 当乘法单位元 1**(`common.nanproduct_last`:`filled = where(isnan(w), ones_like(w), w)`)。`day_max(Ret)` 量级 ~5e-3,所以**窗口里每出现一个 NaN 日,乘积就被放大 ~1/x ≈ 200 倍**。我用玩具张量验证:x=0.005 时正好 **250 倍**;样本最前面两天(左侧 NaN padding)被放大 **4.2e4 倍**。
4. 反过来,**窗口里出现一个 `day_max(Ret) = 0` 的日,乘积精确等于 0**,并且连续 3 天都是 0 → 直接掉到截面最底。
5. **`cross_max(·, 30)` 取 30 日滚动最大**,于是它**专门把第 3 条造出来的 NaN 膨胀尾巴捞到截面顶端**;而第 4 条造出来的 0 在另一端,方向选 -1 时就被捞到顶端。
6. **`abs_` 在非负序列上是恒等变换**(玩具张量验证 `True`)。所以核心卡 #2 `abs_(cross_max(cross_product(day_max(Ret), 3), 30))` 与核心卡 #1 的日度排序**一模一样**,不是一个新东西。
7. **`cross_max(cross_max(y, 30), 30)` 精确等于 `cross_max(y, 59)`**(玩具张量验证 `allclose`)。所以核心卡 #3 只是把窗口从 30 天拉到 59 天,不是新结构。
8. **没有前视**:`rolling_windows` 左侧补 NaN,是因果的;`day_*` 只用当天。真正会前视的 `cross_shift` 没出现在任何子树里。规则 §4 的"前视"这一条在本批上不成立。
9. **门槛(很重要,下面的提议都按它设计)**:`evaluate` 里 `gate = coverage >= 0.9 and distinct >= 0.5`,`distinct_fraction` = 每 5 天取一天、`distinct(值) / 有值的名字数` 的中位数。241 分钟 → `day_zero_ratio` / `day_pos_ratio` / `day_flat_ratio` / `day_at_max_ratio` / `day_flat_run_max` 这类"分钟占比"原子最多 ~242 个取值,对 4000 只有值的股票,distinct ≈ 0.06,**单独当根一定被门槛判废品**。`cross_valid_count` 更是只有 d+1 个取值,同样废品。
10. **奖励里存在一个"不可交易"掩码,但本口径不启用**:`c05_locate.py` 第 117–126 行 `frozen = cross_max(day_zero_ratio(Ret), 15)`、`age = cross_valid_count(day_last(Close), 241)`,`untradable` = 僵尸报价最差那一档 或 上市 / 复牌不足一年;而 `steer.reward` 只在 `kind in ("long_tradable","long_bucket","long_marginal")` 时套这个掩码,`evaluate` 用的是 **`long_neutral`** → **掩码没生效,封死股和新上市 / 刚复牌的股票是可以进多头书的**。(我读不到 `guidance/C05_*`,所以 GP 自己的 fitness_kind 是不是也 `long_neutral`,要 PI 向流水线确认 —— 这一条决定 §3 的通道 B 是否成立。)

---

## 2. alpha 的来源:逐层分解,承重的只有一层

enrichment 表里排前五的是同一条嵌套链,它们的候选集是层层包含的(24 ⊃ 17 ⊃ 14 ⊃ 9 ⊃ 6)。于是可以从 loc.json 精确反解出**"有这一层但没有下一层"的那几个候选的均值**,看每一层各自买到了多少。全局均值 -1.4421。

**Ret 链**

| 层 | 含它的候选 | 均值 | 有这一层但**没有**下一层 | 这一层的边际 |
|---|---|---|---|---|
| `day_max(Ret)` | 24 | -0.759 | n=7,均值 **-1.106** | 比全局 +0.34 |
| `cross_product(day_max(Ret), 3)` | 17 | -0.616 | n=3,均值 **-1.097** | **+0.01(什么也没买到)** |
| `cross_max(cross_product(day_max(Ret), 3), 30)` | 14 | -0.513 | n=5,均值 **-0.573** | **+0.52(全部效应在这里)** |
| `abs_(...)` | 9 | -0.479 | n=3,均值 -0.501 | +0.07(§1.6:恒等变换,这是噪声) |
| `cross_max(abs_(...), 30)` | 6 | -0.469 | — | +0.03(§1.7:只是 59 日窗口) |

**Close 链(对照)**

| 层 | 含它的候选 | 均值 | 有这一层但没有下一层 |
|---|---|---|---|
| `day_max(Close)` | 20 | -1.259 | n=9,-1.235 |
| `cross_product(day_max(Close), 3)` | 11 | -1.278 | n=5,-1.242 |
| `cross_max(cross_product(day_max(Close), 3), 30)` | 6 | -1.307 | n=2,-1.254 |
| `cross_product(cross_max(...), 3)` | 4 | -1.334 | — |

**读出来的三件事:**

- **`day_max(Ret)` 不是真来源,是载体。** 它单独(不带 3 日乘积)时均值 -1.106,只比全局 -1.442 好 0.34;而核心卡把它排在第 5 位、`+0.86` 的均值差,**绝大部分是它下游那一层带来的,被嵌套关系记到了它头上**。
- **`cross_product(·, 3)` 这一层边际 +0.01,等于零。** 它唯一的作用是制造 §1.3 / §1.4 的两条数值通道。
- **唯一承重的一层是 `cross_max(·, 30)`:-1.097 → -0.513,+0.52。** 而同一个 `cross_max(·, 30)` 套在 Close 链上是 **-1.242 → -1.254,边际为负**。`abs_` 与第二个 `cross_max` 加起来 +0.10,且已证明是恒等 / 换窗口,属噪声。

**打折声明**:边际那一列的 n 是 7 / 3 / 5 / 3,极小;层数又与树的大小、以及候选里"其他东西"混在一起;p 值只对嵌套总量给了,没给边际。所以上面三条是**方向性结论**,不是显著性结论。但它足以改变本轮的下注:**机械核心卡按均值差排序,把 `cross_max(cross_product(day_max(Ret), 3), 30)` 排第 1、`day_max(Ret)` 排第 5,这个排序把承重层和载体混在一起了;真正该问的问题是"`cross_max(·, 30)` 在 Ret 上买到的那 0.52 是什么"。**

---

## 3. 那 0.52 是什么:四条通道,哪些是真来源,哪些只是代理

规则 §4 的三类陷阱里,"前视"已排除(§1.8)。剩下"数值伪影"和"定义坏掉(结果主要由热身期 / 缺失值填充决定)"都**正对着**这条链。四条候选通道:

**A. 封死 / 僵尸报价通道(我认为最可能,且是真东西)**
`day_max(Ret) = 0` 精确标记"今天没有一分钟动过"(一字板、无成交)。`cross_product` 把它放大成连续 3 天的精确 0 → 截面最底;方向选 -1 时这一端就是多头书。涨停封板后的次日连续性是 A 股有文献的真现象,而且**5 个控制(流动性、波动、20 日反转、`cross_mean(day_std(Amt), 30)`、`LogFloatCap`)不张成"封死"这个状态**(封死日的波动与成交额都接近 0,控制只能吸收一部分)。
旁证:GP 在这一批里反复去抓 `LimitWidth`——enrichment 表里有 `cs_first_high40(day_close(Vwap), LimitWidth)`(+0.19)和 `add(LimitWidth, day_cov(High, Ret))`(-0.02)。`LimitWidth` 就是涨跌停板宽度(主板 / ST / 创业板科创板不同),它独立地指向同一件事。
还有一条很关键的旁证:§1.9 的门槛让**所有"分钟占比"型的干净原子(`day_zero_ratio` 等)单独当根必然废品**,连流水线自己定义 `frozen = cross_max(day_zero_ratio(Ret), 15)` 都过不了候选门槛。也就是说 **GP 想表达"封死日"时,`cross_product(day_max(Ret), 3)` 的那个精确 0 可能是它唯一过得了门槛的写法**。这解释了为什么它会选一个这么绕的结构。

**B. 缺失日通道(数值伪影,必须验,如果成立必须改写)**
§1.3 的 NaN→1:窗口里每个 NaN 日把乘积放大 ~250 倍,`cross_max(·, 30)` 专门把这个尾巴捞到顶端。于是这条链的截面顶端 ≈ **最近 30 天里停过牌 / 刚上市的名字,按缺失天数排序**。§1.10 说明本口径没有把这些名字排除出可交易域。
**Close 链的对照正好是 B 的指纹**:Close ~ 10 这种大于 1 的量,NaN→1 是把乘积**缩小** 10 倍,被压到底端,`cross_max` 捞不到 → 所以 `cross_max` 在 Close 链上边际为负。这与 §2 的观察一致。
注意 B 既是伪影(规则 §4"结果主要由缺失值填充决定"),也**混着一个真效应**(新股 / 复牌后的收益形态)。所以处理办法不是扔掉,而是**把它从乘积里拆出来,用 `cross_valid_count` / `cross_age` 明写**,再看它还值不值 0.5。

**C. 持久性 / 换手通道(只是代理,不是来源)**
`cross_max(·, 30)` 是一个很"黏"的阶梯函数:只有新极值进来或旧极值出窗口才变,比 EMA(半衰期 20)慢得多。15 bp 双边成本对高换手信号是致命的,而本批所有候选都是负分 —— 慢下来就少亏。证据方向一致:对快而噪的 Ret 叶,层层平滑的效应**递增**(+0.86 → +0.97 → +1.06);对本来就很慢的 Close 价位叶,效应**递减**(+0.22 → +0.18 → +0.14)。
C 和 B 都能解释"帮 Ret 不帮 Close",所以**必须用专门的实验把两者分开**(下面 T1–T4)。

**D. 真 MAX / 日内跳跃内容(基本被 §2 否掉)**
如果 alpha 真在"当天最大一分钟涨幅"里,`day_max(Ret)` 单独那 7 个候选不该只有 -1.106。它可能还被波动控制(及其平方、三次方)吃掉了一大块 —— MAX 型度量与波动在水平上通常高度相关。**D 作为"主来源"已经可以放下;但它值得作为"相对波动的跳跃"再问一次(见 §6 的 N)。**

### 判别实验(这是本轮最该买的信息)

一个 2×2 把 B 和 C 分开(改"乘积"和改"取极值"两件事):

| | 外层取**最大**(捞尾) | 外层取**均值 / 尾均值**(不捞尾) |
|---|---|---|
| 内层**乘积**(有 NaN 膨胀) | 原链(已知 -0.513) | **T3** `cross_mean(cross_product(day_max(Ret), 3), 30)` |
| 内层**均值 / 无内层**(无 NaN 膨胀) | **T1** `cross_max(day_max(Ret), 30)`;**T2** `cross_max(cross_mean(day_max(Ret), 3), 30)` | **T4** `cross_tail_mean_q75(day_max(Ret), 30)` |

读法:**T1 / T2 维持原分 → B 死,C(+A)活**(`nanmax_last` 正确跳过 NaN,不存在膨胀);**T1 / T2 崩到 -1.1 而 T3 也崩 → 承重的是"捞尾"这个动作,B 活**;**T4 维持 → 承重的是"上尾的平均水平"而不是某一天,A / C 活、B 死**。

另外两组(都保持满基数、过门槛):

- **筛掉 B 的名字**:`cs_last_low20(cross_max(cross_product(day_max(Ret), 3), 30), cross_valid_count(day_last(Close), 32))` 与同式把窗口换 `241`。`_lexi` 的档位是**整块同值块**,文档里专门讲了 `cross_valid_count`("93% of the names tied at the window length")→ 被压下去的正好是没饱和的那批(近期停牌 / 新上市),不会误伤老股。score 崩 → B 是来源。
- **筛掉 A 的名字**:`cs_last_high20(cross_max(cross_product(day_max(Ret), 3), 30), cross_max(day_zero_ratio(Ret), 15))`(用流水线自己的 `frozen` 定义做键)。score 崩 → A 是来源。

---

## 4. 烂部件

**必须说明**:没有 ablation,**"必要性 ≤ 0"这个量本轮根本没有被测过**。下面只能用 enrichment 的符号(弱得多的证据)加结构阅读:

| 子树 | 均值差 | p | n | 判断 |
|---|---|---|---|---|
| `day_cov(High, Ret)` | **-0.19** | 0.316 | 11 | 最烂。而且有**结构缺陷**:分钟级的 `(High - mean High) × (Ret - mean Ret)` 对价格是一次齐次,而 `High` 是后复权价、股票之间差几个数量级 → 它的截面排序主要是**后复权价位**,不是日内关系。换成尺度无关的 `day_corr(High, Ret)`,或 `day_cov(in_logchg(High, 1), Ret)` / `day_signed_ratio(Ret, Amt)`,才是它想表达的东西。 |
| `day_close(Ret)` | **-0.11** | 0.577 | 6 | 当天最后一分钟的 bar 收益 —— 一个分钟的噪声,还正好落在收盘集合竞价附近。换 `day_topw_mean(Ret, Amt)`(成交最重的那 10% 分钟的平均收益)或 `cross_tail_mean_q75`。 |
| `add(LimitWidth, day_cov(High, Ret))` | **-0.02** | 0.203 | 4 | **量纲不匹配的 `add`**:`LimitWidth` 是 0.1 量级的档位数,`day_cov(High, Ret)` 是"价格 × 收益"量级。排序前相加,结果被截面散度大的那一项独占,到底是哪一项是尺度的偶然 —— 等于把两个想法相加后丢掉一个。应改成 `cs_first_high40(·, LimitWidth)` / `cs_last_high20(·, LimitWidth)` 这种**分段**写法(GP 自己在另一行已经这么写了)。 |
| `abs_(...)`、第二个 `cross_max(..., 30)` | +1.04 / +1.03 | 0.000 | 9 / 6 | **挂着高均值差的烂部件**:§1.6 证明 `abs_` 在非负序列上是恒等变换,§1.7 证明两层 `cross_max(·,30)` 等于 `cross_max(·,59)`。它们的 +1.0 全是从内层继承来的,自身边际 +0.07 / +0.03。**不要为它们单独开 E 位,核心卡 #2 / #3 与 #1 实质是同一个东西。** |
| `cross_product(day_max(Ret), 3)` | +0.97 | 0.000 | 17 | **边际 +0.01 的"看起来很好"的部件**(§2)。它唯一的作用是制造 §1.3 / §1.4 两条数值通道。真正该做的是把它**换掉**(T1–T3),而不是深挖。 |

→ 如果 R 可用(本轮不可用,见 §5),R 的目标顺序就是:`cross_product(·,3)` → `cross_mean(·,3)` / 整层去掉;`abs_` 去掉;第二层 `cross_max` 去掉;`day_cov(High, Ret)` → `day_corr(High, Ret)`;`add(LimitWidth, ·)` → `cs_*(·, LimitWidth)`。

---

## 5. 之前的任务

**第 1 轮,本组之前没有任何任务**:`missions_before: []`,没有 E / N / R,没有 heads,没有审计记录,没有上一轮笔记(`s806/notebook.md` 不存在 —— 这一轮我要写的就是它的第一条)。所以"E 在哪个核心上试了什么外围 / 有没有产出 heads / N 的结果 / R 的替换与收录 / 审计员挡掉了什么 / 上轮预测对不对"这几问本轮**全部为空**。

**但有一条必须立刻告诉 PI 的硬约束:本轮 R 一个都不能用。**
`scripts/c05_locate.py` 的 `direct` 模式:

    bad = [hd for hd, _ in todo if hd not in byexpr]
    if bad:
        raise SystemExit(f"R requests name heads outside the snapshot: {bad[:3]}")

`byexpr` 是快照 heads 的字典,本轮为空 → **任何 R 请求都会直接退出**。那 16 个 R 名额这一轮是死的。§3 / §4 里我想买的那些变体,必须改走 **E / N 的种子**(初代会把种子全部评估一遍,等价于买到同样的信息),这是本轮唯一的通路。

另外两条给 PI 去跟流水线确认的事:
- `direct` 模式里 R 的**收录**(additions)分支是 `if STUDY == "C06"`;rules.md §2 给 C08 也写了收录。第 2 轮如果要靠收录,得先确认这个分支对 C08 打开。
- `scripts/c06_check.py` 的 `CTRL_STRIKE` 默认 **0.5**(注释写 "C08 (permissive audit)"),而 rules.md §3 写的是 **0.8**。**如果环境变量 `C06_CTRL_STRIKE` 没被设成 0.8,一个与波动控制 |ρ| ∈ [0.5, 0.8) 的核心会被误划掉** —— 这正好可能落在 `day_max(Ret)` 身上(见 §6 的风险项)。

---

## 6. 本轮候选

### 值得深挖的核心(≤ 3)

**① `day_max(Ret)`(核心卡 #5;首选)**

为什么选这个最浅的,而不是均值差最高的核心卡 #1:**只有以 `day_max(Ret)` 为核心,§3 的全部判别实验才能合法地当这个 E 位的种子**。E 的规则是每个候选必须**原样包含核心**;T1 `cross_max(day_max(Ret), 30)`、T2 `cross_max(cross_mean(day_max(Ret), 3), 30)`、T3、T4 都改动了链的内部,**如果核心取 #1,它们都不包含核心、全部非法**;而它们统统包含 `day_max(Ret)`。两组筛选式(`cs_last_low20(...)` / `cs_last_high20(...)`)也都包含它。也就是说这个核心让一个 E 位同时做到:固定住真正的载体、让 GP 自己去长外围、并且把 §3 的四条通道一次性定价。

- **已经见过的外围写法**(只能从 enrichment 表反推 —— 115 个候选的完整表达式在 `episodes/` 里,我按规则 §5 不能读;权威的"已见过"集合是归档,见 §7 的请求):
  `cross_product(·, 3)`;`cross_max(cross_product(·, 3), 30)`;`abs_(cross_max(cross_product(·, 3), 30))`;`cross_max(abs_(cross_max(cross_product(·, 3), 30)), 30)`;另外 `day_cov(High, Ret)` 与 `add(LimitWidth, day_cov(High, Ret))` 说明 `Ret` 也被拿去和 `High` 做过日内配对、和 `LimitWidth` 做过相加。
  **GP 在这一批的"房屋风格"非常窄:外围几乎只用 `{cross_product(·,3), cross_max(·,30), abs_}` 这一摞。** 又因为**库是空的(0 个 head),这一轮没有任何库禁令**,E 位会很容易把同一摞重新长出来。所以种子必须**刻意**避开这摞:`cross_mean`、`cross_tail_mean_q75`、`cross_ema`、`cross_madz`、`cs_*` 筛选、`day_topw_mean` / `day_signed_ratio` 这些方向。
- **风险(PI 必须先看相关度表再定)**:MAX 型度量与**波动控制**在水平上常常 0.6–0.8。规则 §3 要求 E 的核心与每个控制 |ρ| < 0.8;而 §5 提到代码默认的 `CTRL_STRIKE` 是 0.5。相关度表(`corr` 模式)**免费**给出 `vol` 这一列,先看再定。
- **退路**:若 `day_max(Ret)` 的 `vol` 列过不了,退到 **`cross_product(day_max(Ret), 3)`(核心卡 #4)** —— 它因为被两条数值通道掺过,与波动的相关性反而更低;代价是 T1 / T2 不能再当种子(只剩 T3、T4 与两组筛选)。

**② `cross_max(cross_product(day_max(Ret), 3), 30)`(核心卡 #1;只在不开 N 位时才考虑)**

它是**承重层所在的那个最小完整结构**(§2),均值差 +1.06、p 0.000、n=14。把它整体固定住,GP 只能在**外面**长 —— 那正好只剩"筛选 / 分段 / 与另一个信号组合"这些写法,也就是 §3 里那两组筛选实验的方向。
- **已见过的外围**:`abs_(·)`、`cross_max(abs_(·), 30)` —— 而这两个按 §1.6 / §1.7 是恒等变换与换窗口,所以**这个核心周围真正"见过"的外围几乎是空的**,E 位的自由度很大。
- **但我不推荐把本轮的第二个位给它**:§2 说它内部那层 `cross_product` 边际为零、还是两条数值通道的来源;固定住它,等于先承认那两条通道、再在外面找补。先用 ① 把通道定价,第 2 轮再决定要不要固定它,顺序更对。
- 规则允许一个核心整个实验最多 2 个 E 位,这个核心留到第 2 轮完全来得及。

**③ `day_max(Close)`(核心卡 #6;列出但本轮不推荐下注)**

+0.22、p 0.098,是 Close 链**唯一**买到东西的一层(§2:它的三层外围边际全为负或零)。它就是**后复权价位**,按规则 §4,这等于"从某个基期以来的累计收益",是长周期动量 —— 不是陷阱,但也不是新东西,而且 96 次评估换一个 p=0.098 的载体太贵。
- **已见过的外围**:`cross_product(·, 3)`、`cross_max(cross_product(·, 3), 30)`、`cross_product(cross_max(cross_product(·, 3), 30), 3)`。
- 同理,`cs_first_high40(day_close(Vwap), LimitWidth)`(+0.19,**p 0.365**,n=7)在统计上与噪声无法区分,不适合当核心;但它的**写法**(按板块 / 涨跌停宽度分段)值得继承到 N 里。

### R 目标

**本轮 R 不可用**(§5:`direct` 模式对 0 个 head 直接 `SystemExit`)。把它们原样转成 ① 的 E 种子。等第 2 轮有 head 之后,R 的优先队列按 §4 末尾那一行。

### N 的灵感

**假设(给 PI 写进 N 位的一句话)**:这一批唯一承重的那 0.52,来自一个**状态变量**(当天封死 / 僵尸报价、近期停牌或新上市),而不是来自跳跃幅度本身;5 个控制不张成这个状态;GP 之所以用 `cross_product(day_max(Ret), 3)` 的精确 0 和 NaN→1 去表达它,是因为**干净的原子写法全被 `distinct >= 0.5` 门槛判废品了**(§1.9)。把这个状态诚实、过门槛地写出来,应当不差于那条链,而且告诉我们该不该继续在这里挖。

过门槛的种子方向(全部是连续值的根,或 `cs_*` 的序数秩输出):

1. **把三条通道各自写成干净原子**:`day_topw_mean(Ret, Amt)`(成交最重 10% 分钟的平均收益 —— 跳跃发生在哪里有没有量)、`day_signed_ratio(Ret, Amt)`(净买压)、`cross_tail_mean_q75(day_max(Ret), 30)`(上尾均值,不被单日支配)、`cross_age(day_last(Close))`(上市 / 存续天数)。
2. **状态只当筛选键,不当信号**(这是绕过门槛的正确姿势,`_lexi` 的整块同值块语义正是为此而写):`cs_last_high20(y, cross_max(day_zero_ratio(Ret), 15))`(踢掉封死那一档)、`cs_last_low20(y, cross_valid_count(day_last(Close), 241))`(踢掉新上市 / 刚复牌)、`cs_first_high40(y, LimitWidth)`(宽板段)。`y` 取第 1 条里的干净原子。
   注意:`LimitWidth` 只有少数几个取值,`_lexi` 的档位必须整块装进 (lo, hi],**档可能是空的**,那时 `cs_*` 退化成 `y` 的纯秩、等于核心本身的改写 —— 审计员可以据此当重复划掉。优先用连续的键。
3. **"相对波动的跳跃"**(把 D 再问一次,避开波动控制):`div(day_max(Ret), day_std(Ret))` 一类的比值、或 `day_es_ratio_hi(Ret)`(右尾形状,`ops_ext` 文档说明它刻意用 NaN 而不是 `+1e-6`,避开了"封死日变成 1e4"的老毛病)。注意 enrichment 表里已经出现过 `day_es_ratio_lo(High)`(+0.11,n=5)—— **左**尾、而且作用在 `High` 上,右尾作用在 `Ret` 上是没见过的写法。
4. **慢下来但不靠"捞尾"**:`cross_ema(·, 5)`(其文档:缺失日被跳过而不是当 0,且旧尖峰衰减而不是出窗口掉落)—— 它是 `cross_max(·, 30)` 在"持久性"这一面的干净替身,正好做 §3 通道 C 的对照。

做 N 还有一个程序上的理由:规则 §2 要求"3 轮里至少 1 个 N 位通过审计",第 1 轮做掉它风险最小 —— 而且本轮 R 名额作废,算力本来就该挪过来。

**建议的两个位**:① 一个 E 位,核心 `day_max(Ret)`,16 个种子就是 §3 的 T1–T4 + 两组筛选 + 刻意避开 `{cross_product, cross_max, abs_}` 那摞的外围;② 一个 N 位,上面这个假设。

---

## 7. 给 PI 的流程提醒(都能省评估)

1. **相关度表是免费的**:`corr` 模式对计划里每个表达式都给出 **门槛(coverage / distinct)**、与 5 个控制的 |ρ|,**不计分、不花评估**。把所有可疑基数的原子(§1.9)和所有核心候选都塞进去,先拿门槛和 `vol` 列,再定种子。本轮没有 head,所以"与 head 最大 |ρ|"那几列会全是 0 / `—`,这表这一轮纯粹是门槛 + 控制检查。
2. **`c06_check.py` 用严格语法 parse 每个种子**,算子名 / 参数写错会在本地就被挡下来(不花评估)。
3. **本轮没有任何库禁令**(库 = M 的 heads + 本组 heads + R,全空),E 位极易重新长出 `{cross_product(·,3), cross_max(·,30), abs_}` 那一摞。种子要刻意反向。
4. **三个流水线请求**(都很便宜,对第 2 轮收益很大):
   - loc.md 的共性表加上每个子树的 **train / valid / turnover 分列均值** —— §0 的那个歧义("是减少了成本拖累,还是减少了 train→valid 翻转")就能直接读出来,`long_turnover` 本来就在 `keep` 里;
   - loc.md 附上**已评分候选的表达式清单**(至少含 top 核心的那些)—— E 的"外围不得与见过的相同"这条规则,现在只有归档知道,我按规则 §5 读不到 `episodes/`;
   - 确认 C08 的 GP fitness_kind 是 `long_neutral` 还是 `long_tradable`(§1.10),这一条直接决定 §3 通道 B 是否成立。
5. **`CTRL_STRIKE`**:确认环境里设了 `C06_CTRL_STRIKE=0.8`(§5),否则 `day_max(Ret)` 这个核心有被误划的风险。

---

## 8. 文献题目(交文献员;每条对准一个核心或通道)

**所有来源必须有年份且早于 2023-08-08**(`c06_check.py` 的硬检查)。

**Q1 —— 对准核心 ① `day_max(Ret)`(通道 D)**
文献里对"极端正收益 / 最大收益"这类特征具体怎么做?(a) 定义上用**日内分钟收益的最大值**还是日收益的月内最大值,用一个极值还是上尾若干个的平均?(b) 控制掉波动率与特质偏度之后它还剩多少,在中国 A 股上的结论是什么?(c) 是否需要用成交量加权(跳跃发生时有没有量)才能交易?
关键词:MAX effect, lottery demand, extreme positive returns, idiosyncratic skewness, intraday jump, realized jump variation, volume-weighted intraday return;极端收益、最大收益效应、博彩偏好、特质偏度、日内跳跃、分钟收益最大值。

**Q2 —— 对准 §2 的承重层 `cross_max(·, 30)`(通道 C)**
文献里当一个特征是"过去一个月 / 一年的滚动最大值"时,它被当成**信号**还是**状态**?(a) 距 52 周高点 / 滚动极值类特征的标准做法与经济解释;(b) 有没有工作专门把"滚动极值带来的低换手、低成本"与"它携带的信息"分开(成本前后收益、换手率对照、用平滑后的同期信号做对照组)?(c) 用上尾条件均值 / 高分位数替代单一最大值,文献有没有做过这种稳健化?
关键词:running maximum, 52-week high, nearness to 52-week high, rolling window maximum, persistence vs turnover, transaction costs and signal decay, conditional tail mean;滚动最大值、距 52 周高点、信号持久性与换手、交易成本对因子收益的侵蚀、上尾条件均值。

**Q3 —— 对准通道 A(封死 / 僵尸报价;也是 N 位的主假设)**
A 股的涨跌停(含一字板、封板)在横截面因子研究里**怎么度量、怎么处理**?(a) "当天没有一分钟动过"这类封死状态的常用代理变量(封板时长、封单量、零收益分钟占比)有哪些?(b) 封板日之后次日 / 数日的收益形态(磁吸效应、封板后连续性)文献结论是什么,是否随板宽(主板 / ST / 创业板)不同?(c) 实证里通常是把这些名字**剔除**还是**单独建仓**?
关键词:price limits, limit-up, limit hit, magnet effect, limit-up continuation, zero-return days, illiquidity and stale prices, China A-share price limit;涨跌停、一字板、封板、磁吸效应、涨停板次日效应、零收益日、停盘价与僵尸报价、板宽。

**Q4 —— 对准通道 B(缺失日 / 上市年龄,以及构造卫生)**
(a) 横截面因子研究里对**新上市与停牌复牌**名字的标准筛选做法(上市满多少个月、停牌日的处理),以及剔除之后是否还有被记录的收益形态(新股长期弱势、复牌后漂移)?(b) 更偏方法论的一问:文献或行业实践里,**滚动窗口内的缺失值**在"乘积 / 几何平均"型聚合里怎么处理才算正确,把缺失当乘法单位元 1 会造成什么样的伪造信号?有没有讨论"数据缺失模式本身被挖成因子"的工作?
关键词:listing age, new listings, IPO underperformance, trading suspension, trading halt, post-halt drift, sample screening in cross-sectional asset pricing, missing data in factor construction, data-driven artifacts in factor mining;上市年龄、新股、停牌复牌、复牌后漂移、样本筛选标准、因子构造中的缺失值处理、缺失模式被当成因子挖出来。
