# 结构解剖:种子 805,C 组,第 2 轮

快照 = `c05s805M1_I0_open_search` + `c05s805M2_I0_open_search` + `c06s805Cr1a_Ea` + `c06s805Cr1b_Nb`。
heads 6 个,存档已评分候选 320 个,拆解付费评估 41 次,R 候选 1 个,已生效的 R 替换 0 个。

读过:本轮 `r2/loc.md` / `r2/loc.json`,`notebook.md`,`r1/analysis.md`、`r1/lit.md`、`r1/missions.yaml`、`r1/missions_final.yaml`、`r1/audit_1.yaml`、`r1/audit_record.json`、`r1/loc.md` / `loc.json`(审计意见里引用的 `corr_1` 数字一并引用),以及算子与脚本源码:
`partura/ops_ext.py`、`partura/steer.py`、`scripts/c05_locate.py`、`scripts/idea_search.py`、`alphacube/operators/common.py`、`alphacube/operators/nd_ts.py`、`alphacube/operators/nd_cs.py`、`alphacube/operators/dt_day.py`、`alphacube/store.py`。
按规矩没有读其他种子目录、C01–C05 与 C06 的 PLAN.md、`guidance/C0*`、`runs/`、`episodes/` 等,也没有碰 2023-08-08 之后的任何数字。

---

## 0. 一句话结论

1. **本种子有了一个真来源,而且 r1 把它的方向猜反了**:`cross_ema(day_centroid(Volume), 10)` —— 日内成交量重心的**十日平滑水平**,单独当因子 score **+1.31**(train +1.31 / valid +1.58),方向 −1(**做多重心偏早的股票**)。
   r1 断言「静态属性没被定价,东西在偏离里不在水平里」,实测恰好相反:**偏离版 `cross_zscore(day_centroid(Volume), 20)` 是全表最差的一族(5 个候选均值 −2.09),水平版是全库最高分。**
2. **但它有一个必须马上测的要害**:裸核与**已知族控制** `cross_mean(day_std(Amt), 30)` 的 `rho_known = −0.5485`,**已经踩在 §1「与已知族 |ρ| ≥ 0.5 判不合格」的线上**。
   我们那个 +1.28 的 head 之所以合格,全靠外面那层按流动性的 `cs_bucket_rank` 把 `rho_known` 从 −0.55 压到 −0.21 —— 而这层分桶对 **score** 的必要性是 **+0.00**。
   **「分桶不影响分数、只影响合格性」是本轮最重要的一行数字;它同时意味着:这个核心有没有可能是规则 §4-3(波动 / 流动性的非线性重写),本轮还没有被排除。**
3. **M 第 2 批的 4 个 head 全部是人工痕迹**,三种零件拼出来的:(a) 截面常数(`day_pos_ratio(High)` ≡ 1、`ts_argmax(·, 1)` ≡ 1、`cs_mean(·)` 逐日常数、`sub(LogFloatShares, LogFloatShares)` ≡ 0);(b) `LogFloatShares` 与开盘价水平 —— 市值控制只控了 `LogFloatCap` = `LogFloatShares` + log 价格 的**和**,没控**差**;(c) `cs_last_low20` 在奖励反号时把被压下去的 20% 变成整本多头书。
   其中 head +0.58 实际上**就是** `pct_rank(−LogFloatShares)`,一个日频叶子的单调函数,别无其他。
4. 本轮 R 的 16 次直接评估是最值钱的通道:它既是「去烂部件」,也是唯一能把第 2 点那个要害一次测清楚的手段。

---

## 1. alpha 的来源

### 1.1 真来源:`cross_ema(day_centroid(Volume), 10)`,四类证据都在

拆解表(`r2/loc.md` head +1.28 一节;`gate` 全部为真,coverage 0.9993、distinct 0.998–0.999):

| 证据 | 数字 | 读法 |
|---|---|---|
| **充分性** | `cross_ema(day_centroid(Volume), 10)` 单独 = **+1.3132**(train +1.3132 / valid +1.5844,sign −1,hl 5) | 子树自己就是整个 head。head 1.2758,所以 head 的其余部分**在分数上不贡献** |
| **必要性** | 把它从 head 里敲掉(只留裸核在分桶里)→ **−0.6002**,必要性 **+1.88** | 全文件第二大的必要性。**平滑不是装饰,平滑就是信号** |
| **敏感性·字段** | `Volume → Amt`:**+1.3684**(更好),`rho_known` −0.2146 → −0.2131 | 不是 Volume 这个字段的特性;用成交额更干净。稳 |
| **敏感性·窗口** | `cross_ema@10 → 20`:**+1.2208**;`@10 → 5`:**+0.5363**(train 1.05 / valid 0.54) | 单侧稳:窗口加长几乎不掉,**减半掉 0.78**。半衰期有下界,约在 10 附近 |
| **共性** | 子树 `cross_ema(day_centroid(Volume), 10)`:均值差 +0.681、p 0.001、22 / 320,含它的候选均值 **−0.08** | **共性在这里是误导的**:含它的候选平均还是负的,因为大多数外围把它毁掉了。这一轮必须以充分性为准,不以共性为准 |

裸核 `day_centroid(Volume)` 本身:96 / 320,含它的均值 **−0.32**(第 1 轮是 +0.00 / 36 个)。
对照上面的 −0.6002(不平滑、只分桶)可以推出:**裸核自己的 score 大概在 −0.6 到 −0.3 之间,而不是第 1 轮猜的 [−0.1, +0.2]**。日度重心噪声极大(单日重心会被几笔大单带偏),横截面持续的那一部分才是信号。

**方向**:sign = −1,hl = 5。核心本身已是 10 日半衰期的 EMA,奖励再叠一层半衰期 5 的平滑 —— 有效记忆大约 15–30 天,**换手低**,这对扣 15 bp 的纯多头十分位书是加分项,也是「样本外还会在」的一条实质理由(它不靠高频择时)。

### 1.2 决定性的新数字:`rho_known = −0.5485`,以及那层分桶真正在干什么

| 表达式 | score | `rho_known` |
|---|---|---|
| `cross_ema(day_centroid(Volume), 10)`(裸核) | +1.3132 | **−0.5485** |
| `cs_bucket_rank(cross_ema(day_centroid(Volume), 10), cross_mean(cross_mean(cross_mean(day_sum(Amt), 30), 30), 30))` | +1.3054 | **−0.2146** |
| `log(…)` 整个 head | +1.2758 | −0.2146 |
| `log(cross_ema(day_centroid(Volume), 10))`(敲掉分桶) | +1.2734 | **−0.5485** |

三件事:

1. **裸核已经踩线**。规则 §1:「与已知族 |ρ| ≥ 0.5 的判为不合格」。已知族就是 5 个控制之一 `cross_mean(day_std(Amt), 30)`。0.5485 ≥ 0.5。
   **直接后果(PI 必读)**:E 位要求「核心与每个控制的 |ρ| < 0.5」。如果本轮把 `cross_ema(day_centroid(Volume), 10)` 直接当 E 核心,**相关度表很可能当场把这个位判不通过**。能过的写法是把分桶一起固定进核心(§4.1)。
2. **那层分桶在分数上是零、在合格性上是全部**。必要性 +0.00(1.2758 → 1.2734),但 `rho_known` 从 −0.55 变 −0.21。r1 把这类外壳一律读成「保序空操作」是错的:它不保序(十分位内重排),它只是**不改变这本书的夏普,却改变这本书的成分**。
3. **机制上这个 0.55 完全讲得通,而且指向一个具体的替代解释**:成交集中在早盘 ⇒ 分钟 Amt 的日内剖面更不均匀 ⇒ `day_std(Amt)` 更大。所以「重心偏早」和已知族可能是同一现象的两种写法,相关系数 −0.55 的符号也对得上(重心低 ↔ 已知族高),而奖励的中性化是**线性**的,非线性的那部分活着 —— 这正是规则 §4-3 的形状。
   **有一条反证**:按流动性分桶把 `rho_known` 砍掉六成,score 一分没掉。如果 alpha 是已知族的非线性残余,这一刀本该砍掉分数。
   **但这条反证不是决定性的**,因为「按流动性分桶」不是「按已知族分桶」:流动性 `cross_mean(day_sum(Amt), 30)` 与已知族 `cross_mean(day_std(Amt), 30)` 都是 Amt 量纲的量、高度相关,分桶顺手把已知族也带掉了 —— 这解释了 0.55 → 0.21,但没判他清白。
   **决定性的一次测量是:`cs_bucket_rank(cross_ema(day_centroid(Volume), 10), cross_mean(day_std(Amt), 30))` —— 直接按已知族分桶。** 这是一个 R 变体(替换 head 的分桶键),成本 1 次评估。本轮如果只做一件事,做这件。

### 1.3 代理通道:哪些排除了、哪些还空着

r1 §2.4 列了 4 条通道。方向现在知道了(**做多重心偏早**),所以可以把每条通道的符号写具体:

| 通道 | 对重心的机械影响 | 落在多头腿吗 | 本轮证据 |
|---|---|---|---|
| **涨停锁板 / 盘中停牌** | 成交全在早盘 → 重心机械偏小 | **是,正落在多头腿上** | **完全未测**。而且 `steer.py:629`:`mask = ctx.untradable if (… kind in ("long_tradable","long_bucket","long_marginal"))` —— **`long_neutral` 不加不可交易掩码**,锁板、连板、停复牌名字可以整本进多头 |
| **收盘集合竞价** | 成交压到最后几格 → 重心偏大 | 否(在不买的那一端) | 未测。但上交所 2018-08-20 才有收盘竞价(r1 文献 S4),**train 前约 8 个月沪市名字重心系统性偏小**,那段时间信号的一部分就是「做多沪市」的交易所 dummy |
| **指数成分 / 被动资金** | 偏大 | 否 | 未测;是市值的阶梯函数,线性中性化去不掉 |
| **价格网格 / 低价股** | 分钟成交分布粒度随价格变 | 不定 | 未测 |

两条 r1 没有列的新增通道:

5. **已知族 / 波动通道**(§1.2)—— 本轮最大的未决问题。
6. **板块 / 列序通道** —— 见 §1.5 末:股票列序近似代码序,代码段编码交易所与板块;带板块含义的量(`BoardCode`、`LimitWidth`、`ListAge`)本轮一次都没进过任何表达式的条件位。

**判定:证据等级比第 1 轮高了两级(充分性 +1.31、必要性 +1.88、字段与窗口都稳、train 与 valid 同号同量级),但「是不是已知族 / 锁板的非线性重写」这两条还没排除。我给「它是真来源」大约六成信心**;这两次测量(按已知族分桶、按冻结报价分桶)任何一个崩塌,信心掉到两成以下。

### 1.4 被证伪的:A 类「自身历史偏离」

| 子树 | n | 含它的均值 | 均值差 | p |
|---|---|---|---|---|
| `cross_zscore(day_centroid(Volume), 20)` | 5 | **−2.09** | −1.388 | 0.994 |
| `day_centroid(High)` | 10 | −2.22 | −1.554 | 1.000 |
| `cs_state_rank(BoardCode, 10)` | 5 | −1.76 | −1.052 | 0.968 |

那 5 个含 `cross_zscore(day_centroid(Volume), 20)` 的候选,正是 r1 E 位的 A 类种子(`cross_mean(cross_zscore(day_centroid(Volume), 20), 5)`)和建在 A 类上的 C 类交互种子(`cross_mean(mul(cross_zscore(day_centroid(Volume), 20), day_signed_ratio(Ret, Amt)), 10)` 等)。**一刀把 A 类和「建在 A 类上的 C 类」一起废掉了。**

机制解释(和 §1.1 的窗口敏感性是同一件事):日度重心信噪比很低,横截面持续的分量才是信号;`cross_zscore` 恰好把持续分量扣掉、只留噪声。
**这推翻了 r1 的整条先验链**(「截面高度持续 ⇒ 更像股票属性 ⇒ 未被定价 ⇒ 分数该是 0 ⇒ 东西在偏离里」)。实测:持续水平 +1.31,偏离 −2.09。
**第 2 轮不要再在这个核心上写 `cross_zscore` / `cross_madz` / `cross_delta` 类外围**;`day_centroid(High)`(价格路径的重心)也是确定的废品,别碰。

### 1.5 M 第 2 批的 4 个 head:常数 + 规模 / 价格 + 反向筛

先把**截面常数**钉死(都是代码层事实,不是推断):

- `day_pos_ratio(High)` **≡ 1**。`ops_ext.py:98-105`:有限分钟里 `x > 0` 的占比。`High` 是复权后的分钟最高价,恒为正 ⇒ 比值恒为 1(无有限分钟时 NaN)。它出现在 **70 / 320** 个候选里,共性 +1.19 —— M 的 GP 找到了一台常数发生器。
- `ts_argmax(X, 1)` **≡ 1.0**。`alphacube/operators/common.py:509-519` `nanargmax_last`,`pct=True` 返回 `(idx_from_end + 1) / count`;窗口 1 ⇒ `idx_from_start = 0`、`idx_from_end = 0`、`count = 1` ⇒ 恒为 1.0。
  **loc 自己给了实证**:它的 `distinct = 0.0003`、`gate = False`(门槛是 `coverage ≥ 0.9 且 distinct ≥ 0.5`,`scripts/c05_locate.py:162`),单独评估就是「门槛废品」。
- `cs_mean(x)` 是**逐日常数**(`alphacube/operators/nd_cs.py:107-110`:截面均值再 `expand_as`)。`cs_mean(day_distinct_ratio(Close))` 共性 +1.05、7 个候选。
- `sub(LogFloatShares, LogFloatShares)` **≡ 0**,共性表里 4 个候选。

再把 `_lexi` 与 `_buckets` 的两种退化钉死(`ops_ext.py:339-411`、`:600-606`;我用纯 Python 复刻 `_pct_rank` / `_rank_block` / `_lexi` 核对过):

- **`cs_last_*(y, 截面常数)` 是完全保序的空操作**。常数的 tie block 覆盖整个截面 ⇒ `bl ≈ 1/n`、`bh = 1.0` ⇒ `band = (bl > -1) & (bh <= 0.2)` 为假 ⇒ 没有任何名字被移位,输出就是 `pct_rank(y)`。我的复刻里 band 命中 0 个,输出与 y 同序。
- **`cs_bucket_*(y, 截面常数)` 的桶就是股票列序**。`_buckets = ceil(_pct_rank(x) * 10)`,而 `_pct_rank` 在全相等输入上退化成双重 stable argsort = 列序;我复刻出的桶号是 `[1,1,2,2,…,10,10]`,严格按列顺序。**这就是规则 §4-2 列序斜坡的分桶版。**

逐个 head:

**head +0.84** `cs_last_low20(cs_last_low20(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), day_first(High)), ts_argmax(day_first(abs_(sub(-1, Open))), 1))`
- 外层筛变量是常数 ⇒ 外层是空操作。三条独立实测佐证:knockout 它 → 0.8229(必要性 **+0.02**);`Open->Close`(只改到那个常数里面)score **一位不差** 0.8419;`ts_argmax@1->2`(把常数变成真的二值变量)反而掉到 0.6631 —— **让死件活过来是有害的**。
- `sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares)` = `1 − 2·LogFloatShares`,**纯粹的负流通股本**。它自己 score **+0.4826**。
  再一条佐证:knockout 掉一层 `LogFloatShares`(变成 `1 − LogFloatShares`)后 score / train / valid / `rho_known` **四个数字全部一位不差**(0.8419 / 0.8419 / 2.1975 / −0.0658)—— 只有当 `day_pos_ratio(High)` 真是常数时才会这样。
- 全部提升来自内层 `cs_last_low20(·, day_first(High))`:knockout 它 → 0.4832(必要性 +0.36)。
- 所以 head +0.84 = **「负流通股本」+「最便宜 20% 的价格带」**。

**head +0.81** `cs_last_low20(cs_last_low20(sub(sub(day_pos_ratio(High), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(High)), ts_argmax(day_first(abs_(sub(-1, Open))), 1))`
- 里面**一个规模叶子都没有**。`abs_(sub(-1, Open))` = `1 + Open`(Open 为正),`abs_(sub(-2, abs_(sub(-1, Open))))` = `3 + Open`,`day_first(·)` 取首个有效分钟 ⇒ **就是开盘首分钟价格的单调函数**。于是 y = `1 − 2(3 + P)` = `−5 − 2P`,**纯粹的负价格水平**。
- y 自己 score **−1.1527**(`rho_known` +0.4222)。加上内层筛之后 **+0.8115**;knockout 内层筛 → −1.1454,必要性 **+1.96**。
  **这个 head 的 100% 来自那个筛。**
- 筛为什么能变出 +0.81:`_lexi` 的 `shift = −1` 把「x 最低 20%」压到所有人之下;奖励对方向取 ±1、选 train 更好的那个(`steer.py:637` `for sign in (1.0, -1.0)`),这个 head 选了 **−1**,于是被压下去的 20% **整体成为多头腿的来源**,十分位书(10%)全部取自那 20% 里面;又因为 y ≈ `−P` 与筛变量 `day_first(High)` ≈ `P` 近乎反序,这本书就是「**买价格分位大约在 10–20% 这一条带上的股票**」。
- **这正是 r1 审计员划掉我们 a-8、b-12 两个种子的理由**(「`cs_last_high10` 只在正方向上是排除屏,反号后被压下去的名字恰好构成整个多头十分位」)。审计员说对了,而且比它自己说的更对:M 的 GP 用这一条机制拿了 3 个 head。

**head +0.58** `cs_last_low20(sub(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), LogFloatShares), ts_argmax(sub(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), LogFloatShares), 20))`
- y = `1 − 3·LogFloatShares`。筛变量 `ts_argmax(y, 20)`:`LogFloatShares` 基本单调不减 ⇒ 绝大多数名字的 argmax 落在最新一天 ⇒ 取值都是 `1/20`,构成一个覆盖最低一大片秩的 tie block ⇒ `bh ≈ 0.9 ≫ 0.2` ⇒ **band 又是空的**。
- 所以这个 head **就是** `pct_rank(−LogFloatShares)`,一个日频叶子的单调函数,sign −1、hl 20、score +0.5824(train 0.5824 / valid 0.6609)。
- 它为什么能过线:市值控制是 `LogFloatCap` = `LogFloatShares` + log 价格。线性残差去掉的是**和**,留下的是**差** ⇒ 这本书约等于**低价股因子**。规则 §4-3 说的「控制变量的非线性重写」在这里甚至不需要非线性,**一个线性无关的分解就够了**。

**head +0.64** `cs_bucket_demean(sub(ts_argmax(day_first(abs_(sub(-1, Open))), 1), LogFloatShares), ts_argmax(day_first(High), 1))`
- y = `1 − LogFloatShares`(负规模),分桶键是常数 ⇒ **按列序切成十段去均值**。
- 两条实测佐证:
  - 把分桶键换成**真的** `day_first(High)`(knockout)→ **0.2532**:**用真桶比用假桶差 0.39**。
  - 把 y 里的常数去掉(变成 `价格 − LogFloatShares`)→ **−2.1491**,必要性 **+2.79** —— 全文件最大的必要性数字,**属于一个截面常数**;它唯一的作用是不让价格水平污染 `LogFloatShares`。
- **推断(不是代码事实)**:列序通常是代码序(`store.py:104` 从 meta 读 symbols,`:306-307` 增量股票 `sorted` 追加),而 A 股代码段编码交易所与板块(600/601/603 沪主板、000/001 深主板、002 中小板、300 创业板、688 科创板)。所以「列序十桶」近似「**板块 / 上市批次十桶**」—— 这解释了为什么假桶比真桶好,也直接给出一个把人工痕迹换成真条件化的 R 变体:**把那个常数换成 `BoardCode` 或 `ListAge`**。

**4 个 M2 head 的共同点**:都是近似静态的个股属性(流通股本、价格水平、板块),valid 远高于 train(2.20 / 2.58 / 0.66 / 0.64 对 0.84 / 0.81 / 0.58 / 1.01)。`score = min(train, valid)`,所以它们靠 train 那一端过线;而 **valid ≫ train 是「静态特征恰好赶上一段行情」的形状,不是信号的形状**。它们不受我们控制,也不能从库里删;我们能做的只有 R 替换(§4.2)。

### 1.6 这一轮的共性表怎么读:前 7 行是我们自己污染的

| 子树 | 均值差 | n | 单独评估的 score |
|---|---|---|---|
| `cross_mean(cross_mean(day_sum(Amt), 30), 30)` | **+1.843**(全表第一) | 4 | **−2.1378** |
| `cross_mean(cross_mean(cross_mean(day_sum(Amt), 30), 30), 30)` | — | — | **−1.8181** |
| `cross_mean(day_sum(Amt), 30)` | +1.531 | 11 | 未测(**就是流动性控制原文**) |
| `day_sum(Amt)` | +1.341 | 14 | 未测 |

共性表第一名单独评估是 **−2.14**。原因很简单:它只是我们 r1 E 位那个赢家的**分桶键**,搭车进了 4 个高分候选。
**结论:核心卡 #5、#6、#7 是污染,不是发现;任何把它们当核心的计划都会被「核心与控制 |ρ| < 0.5」直接判死。**
同理,`cs_last_low20(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), day_first(High))`(卡 #4,共性第三)和 `sub(day_pos_ratio(High), LogFloatShares)`(53 个候选)是 M2 自己的痕迹搭车。
**本轮共性表唯一有独立价值的信息在负的那一端**(§1.4 的三行)。

---

## 2. 烂部件(R 的素材)

### 2.1 必要性 ≤ 0 的部件

| 所在 head | 部件 | 必要性 | 去掉后 |
|---|---|---|---|
| +0.81 | `ts_argmax(day_first(abs_(sub(-1, Open))), 1)` | **−0.13** | **+0.9387**,增益 **+0.1272** ⇒ **已满足 R 门槛** |
| +0.84 | `sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares)` 的第二层 `LogFloatShares` | **−0.00** | 0.8419,四个数字一位不差 ⇒ 纯冗余 |
| +0.84 | `ts_argmax(day_first(abs_(sub(-1, Open))), 1)` | +0.02 | 0.8229,不到门槛,但证明它是死件 |
| +1.28 | 整个 `cs_bucket_rank(…)` 外壳(只对**分数**而言) | **+0.00** | 1.2734;**但 `rho_known` 从 −0.21 退回 −0.55,所以这件不能砍**(§1.2) |
| +0.58 | 整个 `cs_last_low20(·, ts_argmax(·, 20))` | 未测,代码上是空操作 | 预测 ≈ 0.55–0.58 |

### 2.2 换掉反而更好 / 换掉就露馅的部件

- head +0.81 去掉常数筛:+0.1272(上表;**loc 的 `r_candidates` 已经列出这一条**)。
- head +1.28 的核心字段 `Volume → Amt`:**+1.3684**,增益 **+0.0926** —— 差 0.0074 到 R 的 +0.1 门槛。要越线需要再叠一处(窗口 20、或分桶键多平滑一层)。
- head +0.64 的分桶键从常数换成真变量 `day_first(High)`:**0.2532**(掉 0.39)。这不是「更好」,而是「一换就露馅」—— 本轮关于列序斜坡最干脆的实证。

### 2.3 保序包装能把分数挪动多少:r1 §5.2 留的校验,结果

r1 写过:「砍掉一个保序外层让 score 变了 0.1 以上,说明我关于 z-rank 的推理有漏洞」。三组同族对照(`alphacube/operators/common.py:204`:`log(x) = log(|x|)`,`|x| > EPS` 否则 NaN;`cs_bucket_rank` 输出 ∈ (0, 1.0001] 所以一层 `log` 保序,两层 `log` 变成**反序**):

| 表达式 | score | sign |
|---|---|---|
| `cs_bucket_rank(cross_ema(day_centroid(Volume), 10), cross_mean(day_sum(Amt), 30))` | 1.1009 | −1 |
| `log(cs_bucket_rank(cross_ema(day_centroid(Volume), 10), cross_mean(day_sum(Amt), 30)))` | 1.0789 | −1 |
| `log(log(cs_bucket_rank(cross_ema(day_centroid(Volume), 10), cross_mean(day_sum(Amt), 30))))` | 1.1494 | **+1** |

**校验结论:秩等价(含反序)的改写在这个环境里能把 score 挪动 0.02–0.07,不是 < 0.01,但也不到 0.1。** 来源是奖励内部那一步 EMA 平滑与非线性变换不可交换(`steer.py:632` 先 `bk.smoothed(raw, hl)`、再 `neutral_residual` 取秩)。两层 `log` 让方向都翻了,奖励的 sign 搜索把它吸收掉。
**两条用法**:(i) **score 的小数第二位不是信息**;(ii) R 的 +0.1 门槛大致安全(0.1 > 0.07),但不宽裕 —— **只改保序包装的变体不要放进 R**,它可能靠这点噪声蹭到接近门槛。

### 2.4 负面清单(给 E / N 的种子表)

沿用 r1 §3.2 的「非负输入上的 `pow_*` / `sqrt` / `abs_` / `log` / `sigmoid` / `cs_rank` 等保序空操作」,本轮新增:

1. **任何以 `ts_argmax(·, 1)`、`day_pos_ratio(<价格字段>)`、`cs_mean(·)`、`sub(X, X)` 当参数的写法** —— 它们是截面常数,进 `cs_*` 就是列序斜坡(§4-2),进 `sub` 就是加常数。
2. **`cs_last_*` / `cs_first_*` 这一族(`_lexi`)** —— 奖励会对方向取 ±1,反号时「排除屏」变成「只买被排除的名字」。**要做条件化就用 `cs_bucket_rank` / `cs_bucket_zscore` / `cs_bucket_demean`,它们没有反号陷阱。** 这是本轮最该带走的一条方法论。
3. **`cross_zscore` / `cross_madz` 类自身偏离用在 `day_centroid` 上**(§1.4,实测 −2.09)。
4. **`day_centroid(High)` 等价格字段的重心**(实测均值 −2.22)。

---

## 3. 之前的任务

### 3.1 E 位 `c06s805Cr1a_Ea`(核心 `day_centroid(Volume)`)

- 评分 87,过线(≥ 0.5)**13**,入 heads **2**。采样拒绝计数 `{'c05_no_core': 890, 'c05_periphery_seen': 3}`。
- 前五名全是同一族:
  - `log(cs_bucket_rank(cross_ema(day_centroid(Volume), 10), cross_mean(cross_mean(cross_mean(day_sum(Amt), 30), 30), 30)))` +1.2758
  - `log(log(cs_bucket_rank(cross_ema(day_centroid(Volume), 10), cross_mean(day_sum(Amt), 30))))` +1.1494
  - `cs_bucket_rank(cross_ema(day_centroid(Volume), 10), cross_mean(day_sum(Amt), 30))` +1.1009
  - `cs_bucket_rank(cross_ema(day_centroid(Volume), 10), cross_mean(cross_mean(day_sum(Amt), 30), 30))` +1.0902
  - `log(cs_bucket_rank(cross_ema(day_centroid(Volume), 10), cross_mean(day_sum(Amt), 30)))` +1.0789
- **第三名就是我们手写的第 4 号种子原样**(`missions_final.yaml` 第 51 行)。也就是说:**GP 的 96 次付费评估没有找到新的书**,只把种子从 1.10 抬到 1.28,而抬分主要来自给分桶键多叠两层 `cross_mean(…, 30)`(必要性 +0.21)和那层 `log`(§2.3,量级 0.02–0.07)。
  → **r1 §5.1 第 4 条「PI 手写的 ≤16 个种子是唯一能决定覆盖面的东西」得到完全证实。第 2 轮的全部杠杆还在种子表上。**
- 拒绝几乎全是 `no_core`(890 : 3),**novelty 门槛形同虚设**,与 r1 对 `SEEN` 的代码分析一致(`idea_search.py:310-330`:外围是算子名的 `frozenset`,重数、窗口、字段都被抽掉,运行中不增长)。
- **两个 head 入库**:+1.2758,以及 `sub(LogFloatShares, cross_ema(day_centroid(Volume), 40))` +0.5138(sign **+1**,hl 5,train 0.5138 / valid 0.7995)。后者是「规模 − 重心」,是 13 个过线候选里唯一与第一名日度秩 |ρ| < 0.7 的,所以只进了 2 个。

### 3.2 N 位 `c06s805Cr1b_Nb`(定号成交的日内时点差)

- 评分 83,过线 **0**,入 heads **0**。
- 最好 **+0.2652**(train 0.5676 / valid 0.2652,sign **−1**,hl 20):
  `cross_ema(sub(day_signed_ratio(Ret, mul(Volume, in_index(Volume))), day_signed_ratio(Ret, mul(Volume, sub(1, in_index(Volume))))), 5)`
  读法:「时刻加权净买压 − 反时刻加权净买压」,sign −1 ⇒ **做多净买压偏早的股票**。
  **这与 E 位的 sign −1(做多重心偏早)方向一致** —— 两个独立的位、两套不同算子,指向同一个符号。这是本轮最可复用的一条机制结论。
- 第二名掉到 +0.0100,其余为负。**把时点定号没有加强信号,反而削掉了约一个数量级**:分钟收益符号给成交定号引入大量噪声,锁板分钟两边都不进导致样本缺失。
- 第 3–5 名是 train 极差 / valid 极好的形状(−0.086 / 2.087,−0.137 / 1.311,−0.325 / 1.144):N 的池子里有一批只在 valid 段成立的结构,`min(train, valid)` 全压掉了 —— 这个 score 定义在起保护作用,值得记一笔。

### 3.3 R

r1 的 R 是空的(快照 0 个 head;r1 §1 用代码论证了任何 R 请求会让子进程非零退出)。**本轮 R 第一次可用,16 个变体额度是全新的测量通道。**

### 3.4 审计员挡掉了什么,以及事后看对不对

`audit_1.yaml`:a 位创新 3 / 合理 3,划掉 3、5、8 号;b 位创新 4 / 合理 3,划掉 12 号;两位都通过,没有重写。`struck_by_table` 两位都是 0。

| 被划 | 理由 | 事后评价 |
|---|---|---|
| a-3 `cross_rank(cross_ema(day_centroid(Volume), 3), 120)` | 相关度表判废品(distinct 0.097),约 120 个离散值,截面大量并列,靠列序破平(§4-2) | **对**。和本轮 M2 那堆常数是同一种病 |
| a-5 `cs_bucket_rank(cross_ema(day_centroid(Volume), 10), LogFloatCap)` | 按市值分桶后与 liq / vol / known 的 \|ρ\| 从 0.18 / 0.16 / 0.20 升到 0.44 / 0.44 / 0.47,判为 §4-3 | **代价最大的一次划掉**。被留下的孪生兄弟(按流动性 `cross_mean(day_sum(Amt), 30)` 分桶)就是 +1.28 的 head,而它的 `rho_known` 是 −0.21,**比裸核的 −0.55 还低**。同一个工具换个分桶键,与控制的相关度方向相反。**结论:分桶键的选择不是风格问题,是合格性问题** —— 下一份计划要为每个分桶键说清它把哪个控制带走、把哪个带进来 |
| a-8 / b-12 `cs_last_high10(·, cross_mean(day_flat_ratio(Close), 20))` | `cs_last_high10` 只在正方向上是排除屏,奖励反号后被压下去的 10% 整体成为多头十分位,而 `long_neutral` 不加不可交易掩码 | **对,而且被 M2 的 3 个 head 完全证实**(§1.5)。**代价**:锁板 / 冻结报价这条通道因此一次都没测到,而它恰好落在我们多头腿那一侧(§1.3)。**补法:本轮用 `cs_bucket_rank(·, cross_mean(day_flat_ratio(Close), 20))` 分桶,不用筛** |

### 3.5 上一轮的预测,逐条核对

**`notebook.md` 的 4 条(PI)**

1. 「核心与 5 控制 |ρ| 都 < 0.5,最大的是市值或流动性,约 0.2–0.35;每位被相关度表划掉 ≤ 2 个」→ **一半对**。`struck_by_table = 0 / 0` ✓;幅度 ✓(审计意见:最大 0.20);但**最大的那个是已知族,不是市值或流动性** ✗。而且本轮 loc 量到:**加 10 日平滑之后 `rho_known` 从 0.20 跳到 0.5485** —— 平滑让重心与已知族(本身就是 30 日平均)的频率对齐,相关度被**放大**。谁都没预料到这件事,它现在是本种子最大的风险点。
2. 「槽 a 产出 ≥ 1 head 概率 30%;最佳 E 候选 score 在 0.3–0.6;head 的外围属于 A 类或 C 类,**不是**纯平滑加分桶的水平版;纯水平版落在 [−0.15, 0.25]」→ **产出 2 个 head、最佳 +1.28**,数值远超区间;外围归属**完全反了**,赢的恰好是「纯平滑 + 分桶的水平版」,纯水平版实测 +1.09 ~ +1.28。
   **PI 自己写的证伪条件被触发了**:「若最佳 E 候选是纯水平分桶版且 ≥ 0.5,『水平无价』的判断错,第 2 轮应回到水平条件化方向。」→ **按本种子自己定下的决策规则,第 2 轮应当回到水平条件化方向。**
3. 「槽 b 产出 ≥ 1 head 概率 35%;方向预测为正(晚买早卖 → 随后上涨)」→ 0 个 head;最好的那个 sign = **−1**,即**早买晚卖 → 随后上涨**,**方向预测反了**。「N 与 E 的 head |ρ| < 0.3」无 head,不可核对。
4. 「两位都不产出的概率 45%;若如此第 2 轮应换掉日内时点这一维」→ 没有发生;**恰好相反,这一维给出了全库最高分,不要换掉。**

**`r1/analysis.md` §7 的 5 条(上一任结构解剖员)**

1. 「裸核 score 落在 [−0.1, +0.2]」→ **不可直接核对,而且这是一次被白白放掉的零成本测量**:r1 §5.1 建议把裸核等 4 个表达式放进 N 的种子表,`missions_final.yaml` 最后**一个都没放**。间接证据(`log(cs_bucket_rank(day_centroid(Volume), cross_mean^3))` = −0.6002)指向裸核在 −0.6 到 −0.3,**预测偏乐观,错**。
   → **第 2 轮不要重复这个失误**:把需要数字的表达式塞进 N 的种子表(初代会被评分并进存档),是不花额外预算的测量通道。
2. 「`pow_1_5(core)` 一族与裸核 score 差 < 0.05、秩相关 > 0.99」→ 无并列评估,不可直接核对;`log` 的三组对照给出 0.02–0.07(§2.3),**量级对,边界略紧**。
3. 「A / B 类外围 score 明显高于纯保序外围」→ **半对**:B 类赢,**A 类是全表最差的一族之一**。r1 为这条配的决策(「如果不是,放弃这个核心」)**不适用**:失效的是 A 类,不是核心。
4. 「分桶后仍接近 0 ⇒ 不是代理;分桶后变好 ⇒ 代理压住了信号」→ 实测「分桶后变好」,按 r1 自己的判据指向「代理确实压住了信号」。
   **但有一个混淆必须指出**:平滑和分桶是同时引入的。把分数从 −0.60 抬到 1.31 的是**平滑**(必要性 +1.88);分桶抬的是**合格性**(`rho_known` −0.55 → −0.21),不是分数。r1 这条判据把两件事混进了一个观测。
   「按 `day_flat_ratio(Close)` 分桶后塌掉 ⇒ 主要是锁板痕迹」→ **未测**(审计员以正当理由划掉了那个种子,§3.4)。
5. 「会出现相当数量的 `periphery_seen` / `no_core` 拒绝,但不会集中在少数几个外围类上」→ 拒绝 890 : 3,**几乎全是 no_core**;「不集中」在结果上成立(13 个过线),但实际机制正是 r1 自己担心的退化:**96 次评估基本花在同一个外围族上换窗口**。**预测对,担忧也成真。**

---

## 4. 本轮候选

### 4.1 值得深挖的核心(≤ 3)

**先说本轮 E 位的第一性约束,它比「外围新不新」重要得多。**
`idea_search.py:300-335`:库里 6 个 head ⇒ `SKEL_BAN` 有 6 个骨架(抽掉字段、常数、窗口),`RankSimilarityBan` 以 0.7 开启。库里已经有 head #1 = `log(核心卡 #2)`,而核心卡 #2 与它**秩等价**。于是:
- **任何只在核心外面套保序 / 轻度包装的候选,都会被 0.7 的秩禁令拒掉**;
- 审计规则还会**在跑之前**就划掉「与某个 head 的日度秩 |ρ| ≥ 0.7」的种子,而任务位通过要求「划完还剩 ≥ 4 个种子」。
→ **E 的外围必须按设计大幅移动这本书**,而这恰好就是我们想要的东西(新信息)。PI 写种子时要按 ρ 预算来写,并多写几个备胎。

| # | 核心 | 证据 | 已见过的外围 | 判断 |
|---|---|---|---|---|
| **1** | `cs_bucket_rank(cross_ema(day_centroid(Volume), 10), cross_mean(cross_mean(cross_mean(day_sum(Amt), 30), 30), 30))`(核心卡 #2) | 自身 +1.3054;`rho_known` **−0.2146**;内部 `cross_ema` 必要性 +1.88;字段换 Amt 更好、窗口加倍稳 | 存档里含它原样的只有 head #1 ⇒ 已见外围 ≈ `{}`(空集永远被拒)、`{log}`。**外围 novelty 几乎不设限** | **首选**。它是唯一既被证明、又能过「核心与每个控制 \|ρ\| < 0.5」这一关的写法 |
| 2 | `cross_ema(day_centroid(Volume), 10)`(核心卡 #1) | 自身 **+1.3132**(更高) | `{cs_bucket_rank, cross_mean, day_sum}`、`{log, cs_bucket_rank, cross_mean, day_sum}`,以及 87 个 E 候选里我看不见的若干 | **不要直接用**:`rho_known = −0.5485` ≥ 0.5,**相关度表很可能让这个位直接不通过**。先看相关度表(算法不同:只用 train、每 5 天取一天)再决定 |
| 3 | `cs_last_low20(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), day_first(High))`(核心卡 #4) | 自身 +0.8036 | — | **不要用**。= 常数 + 负流通股本 + 价格带反向筛(§1.5),是 §4-2 与 §4-3 的叠加;它近似 `pct_rank(−LogFloatShares)`,与市值控制的 \|ρ\| 我预测在 **0.6–0.9**,E 位会被规则直接判死 |

核心卡 #5 / #6 / #7(`cross_mean^k(day_sum(Amt), 30)`、`day_sum(Amt)`)= 流动性控制本身,见 §1.6,不可用。

**围绕核心 1 的外围,两类能活过 0.7 秩禁令的写法**(都原样含核心;`has_core` 判的是节点 key 相等,所以括号里面动不了 —— 改分钟层输入属于 N,不属于 E):

- **甲类:把核心当信号,但乘 / 减 / 残差化一个方差可比的另一维。** `mul(核心, cs_rank(日频量))`、`sub(cs_rank(核心), cs_rank(日频量))`、`cross_regres(核心, 日频量, 60)` 取残差。「另一维」优先用**本轮已知方向一致**的那个:`cross_ema(day_signed_ratio(Ret, mul(Amt, in_index(Amt))), 10)`(净买压的时刻加权**水平**,r1 N 位最好的那条,符号一致)。
- **乙类:把核心当条件变量,而不是当信号。** `cs_bucket_rank(X, 核心)`、`cs_bucket_zscore(X, 核心)`、`cs_flip_by_state(X, 核心)` —— 书由 X 驱动、在重心的十分位内比较。
  这类与 head #1 的 ρ 天然很低,**几乎肯定活过禁令**;而且它回答一个我们完全没有的问题:**重心是只能当信号,还是也能当一个「别的因子在哪些股票上有效」的条件维度?** 规则上完全合法(核心原样出现)。
  我认为这是本轮创新度最高、又最不容易被禁令卡死的一类,建议在种子表里占一半。

### 4.2 R 目标(≤ 16,按优先级;全部用 `cs_bucket_*` 而不是 `cs_last_*`)

**第一组:head +1.28 的合格性与代理通道(本轮最值钱的测量)**

1. 分桶键 → `cross_mean(day_std(Amt), 30)`(**已知族本身**):`cs_bucket_rank(cross_ema(day_centroid(Volume), 10), cross_mean(day_std(Amt), 30))`。**决定性诊断**(§1.2)。
2. 分桶键 → `cross_mean(day_std(Ret), 20)`(波动控制):针对波动通道。
3. 分桶键 → `cross_mean(day_flat_ratio(Close), 20)`:**锁板 / 冻结报价**通道,补回 r1 被划掉的那次测量(§3.4)。
4. 分桶键 → `LimitWidth`:涨跌停带宽,一次同时覆盖锁板机制与板块(主板 10% / 创业板科创板 20% / ST 5%)。
5. 分桶键 → `BoardCode`:板块与交易所,对准上交所 2018-08-20 收盘集合竞价的制度跳变。
6. 分桶键 → `ListAge`。
7. 核心里 `Volume → Amt`(已测 +1.3684,增益 +0.0926,差一点点到门槛;作为 8 的基线保留)。
8. 核心里 `Volume → Amt` **且** `cross_ema@10 → 20`:赌它越过 +0.1。
9. 核心里 `cross_ema@10 → 30`:窗口上端(10→20 只掉 0.09,再看一格)。
10. 核心里 `Volume → mul(Volume, is_gt0(in_index(Volume)))`:**去掉开盘集合竞价那一格**(r1 的 N 位已核对过这个写法恰好去第 0 格)。
11. 核心里 `Volume → mul(Volume, is_lt0(sub(in_index(Volume), 0.98)))`:**去掉收盘竞价那几格**(241 格,0.98 ≈ 第 236 格起;边界请按 `in_index` 源码再核一次)。**「重心是不是收盘竞价占比的改写」的决定性检验。**
12. 10 与 11 合并:只剩连续竞价段的重心。
13. 核心里 `Volume → mul(Volume, is_gt0(abs_(Ret)))`:只留价格真的动过的分钟(排除锁板 / 冻结分钟)。

**第二组:把 M2 那 4 个 head 的人工痕迹换成诚实的部件**

14. head +0.81:去掉 `ts_argmax(day_first(abs_(sub(-1, Open))), 1)` → 已测 **+0.9387**,增益 **+0.1272**,**唯一已知满足门槛的替换,直接写进计划**(与原 head 的 ρ 必然 ≥ 0.5 ⇒ 替换)。
    提醒:替换后筛变量变成真的价格水平,**书还是价格带书**,只是库里那一行不再含一个常数。
15. head +0.64:分桶键 `ts_argmax(day_first(High), 1)` → `BoardCode`(或 `ListAge`)。把列序假桶换成真桶;需 ≥ 0.7433 才替换,我预测会掉(真桶换假桶那次掉到 0.2532),但这是把列序斜坡写进审计记录的办法。
16. head +0.58:去掉整个 `cs_last_low20(·, ts_argmax(·, 20))` → `sub(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), LogFloatShares)`。证明那个筛是空操作(预测 ≈ 0.55–0.58,不到门槛,记录值)。

若 16 个放不下,砍 6、9、15、16;**1、11、3、10、14 不能砍**。
R 只评合理度,而「去掉或替换的部件是否真是烂的」在第一组里靠的是**合格性论证**(把 `rho_known` 与控制相关度写进理由),在第二组里靠的是**代码事实 + loc 自己的 `gate = False` / `distinct = 0.0003`**。

### 4.3 N 的灵感

**库禁令同样作用于 N**:任何「同一条日内成交曲线的另一个泛函」都有与 head #1 的 |ρ| ≥ 0.7 被相关度表划掉的风险,而任务位通过要求划完还剩 ≥ 4 个种子。**N 的种子表必须一半近、一半远。**

1. **把「重心」拆成成交份额的几段,看信息在哪一段。** 已知「偏早 → 好」,但不知道是「早盘多」「尾盘少」还是「竞价格少」。写法:`div(day_sum(mul(Amt, is_lt0(sub(in_index(Amt), 0.125)))), day_sum(Amt))`(首 30 分钟份额)、对应的尾 30 分钟份额、收盘竞价份额,全部 `cross_ema(·, 10..20)`。
   **这一条还有一个别的办法做不到的用处**:`day_std(Amt)`(已知族)对「早盘多」和「尾盘多」是**对称**的,份额的方向性不是 —— 所以「只有偏早那一侧有效」会是把真信息和已知族分开的最强证据(§1.2)。
2. **成交金额重心与成交量重心之差**:`cross_ema(sub(day_centroid(Amt), day_centroid(Volume)), 10)`。同一条曲线的两种加权,差值 ≈「大单 / 高价时点」偏离「普通成交时点」的程度。`Volume → Amt` 让 score 从 1.28 升到 1.37,说明两者不等价,这个差是一条现成的新维度。
3. **定号 × 水平,而不是定号 × 偏离。** r1 的 N 把所有交互建在 `cross_zscore`(已证伪)上,而它自己最好的那条用的是**水平**(+0.2652)。所以:把时刻加权净买压的**水平** `cross_ema(day_signed_ratio(Ret, mul(Amt, in_index(Amt))), 10..20)` 单独做一遍,并与重心水平互相条件化(`cs_bucket_rank` 两个方向各一遍)。方向已知(早 → 好),可证伪性强。
4. **同一机制在别的日内形状量上的痕迹,只测「偏早」那一侧**:`cross_ema(day_argmax(Volume), 10)`(放量时点,比重心稳健于尾部)、`cross_ema(day_gini(Amt), 10)`、`cross_ema(day_es_ratio_hi(Amt), 10)`。这是 r1 §5.3 第 1 条的保留项,现在有了方向约束,便宜很多。
5. **(免费的测量,务必带上)** 把需要数字的表达式塞进 N 的种子表 —— 初代会被评分并进存档,第 3 轮的共性表就有数字了:`day_centroid(Volume)`(裸核,E 永远测不到,r1 漏了一次)、`cross_ema(day_centroid(Amt), 10)`、`cross_ema(day_centroid(Volume), 60)`。

**槽位配法建议**:「3 轮至少 1 个 N 位通过审计」这条**已经满足**(r1 b 位创新 4 / 合理 3 通过),本轮两个槽自由。建议 **E(核心 1,甲 + 乙两类外围)+ N(灵感 1 为主、2/3 为辅,带上灵感 5 的免费测量)**:E 把已证明的核心往「新信息」方向推,N 直接回答 §1.2 / §1.3 那两个未决的机制问题;R 的 16 次同时做诊断和去烂部件。

---

## 5. 文献题目(交文献员,只用 2023-08-08 之前发表的)

四题各对准一个核心或一条灵感,问的都是「**文献里对类似的结构 / 特征做过哪些处理**」。
r1 的 L1–L4 已覆盖:日内成交量分布的处理手法、收盘竞价是否机构代理、水平 vs 自身偏离、A 股日内集中度 / 聪明钱的构造。**本轮不要重复那四题**;下面四题对准 r1 结论被实测推翻的地方和新出现的要害。

**L1(对准核心 1 与 R 第 1、2 项)日内成交「时点」和日内成交「离散度 / 波动」,文献里怎么区分、怎么互相剥离?**
要处理手法:有没有论文报告过这两类量的相关性量级,以及用什么办法把一个从另一个里剥出来(按波动分桶 / 双重排序 / 对波动做残差回归 / 同族内中性化 / 正交化的先后顺序);有没有报告「控制了日内波动或成交离散度之后,时点类特征还剩多少」。
关键词:日内成交量时点、日内成交集中度、日内已知波动与已实现方差、量-波动关系、双重排序、特征正交化;
intraday volume timing vs intraday volume dispersion / volume concentration and realized volatility / volume-volatility relation / double sorting on volatility / orthogonalizing a characteristic against volatility / residualizing against a known factor.

**L2(对准 R 第 10–12 项与 N 灵感 1)研究「开盘 / 收盘集合竞价成交占比」时,文献怎么把竞价分钟和连续竞价分钟分开?**
要具体做法:有没有把「去掉竞价分钟后日内指标是否还成立」做成标准稳健性检验;在同样有收盘竞价的市场(A 股、日本、韩国、台湾、欧洲)里,论文怎么处理竞价成交量量级远大于普通分钟这件事(剔除、缩尾、单独建变量);有没有处理过「某个交易所中途才引入收盘竞价」造成的样本内制度跳变。
关键词:收盘集合竞价成交占比、开盘竞价、剔除竞价分钟、连续竞价段、制度变更的样本处理、稳健性检验;
closing auction volume share / opening call auction / excluding auction trades / continuous session only robustness / auction volume outliers / structural break from auction introduction.

**L3(对准 §1.4 被证伪的那条,以及窗口敏感性)对持续性强的高频个股特征,文献报告过「多日平均 / EMA 的持续水平」和「自身历史 z 分数的偏离」哪一种更能预测横截面收益?**
要的是:有没有论文明确做过这两种处理的对照并报告方向;有没有人用「测量噪声 / 信噪比」解释为什么短平滑窗口失效、长窗口有效;平滑窗口长度的敏感性通常怎么报告。
关键词:特征的持续性、特征的测量噪声、多日平均、EMA 半衰期、平滑窗口敏感性、信号衰减;
persistence of firm characteristics / measurement error in high-frequency characteristics / averaging over multiple days / smoothing window sensitivity / signal-to-noise of intraday measures / characteristic level versus innovation.

**L4(对准 §1.5 的 4 个 M2 head)「名义股价水平」和「流通股本」在横截面上怎么与市值分开?**
要的是:控制了市值之后,名义价格或流通股本(股数)还有没有独立的横截面溢价,A 股有没有本地证据;这类研究怎么处理板块(沪主板 / 深主板 / 中小板 / 创业板 / 科创板)和上市年龄;有没有人指出「用市值做控制、同时让股数与价格各自进因子」这种写法会把一个已知风格重新造出来。
关键词:低价股效应、名义股价、流通股本、股数与市值、市值中性排序、板块分割、上市年龄;
nominal stock price effect / low-priced stock anomaly / share count versus market capitalization / float shares / size-neutral sorting / China A-share board segmentation / listing age effects.
这一题的实用价值:它决定我们要不要在 R 上继续花力气替换 M2 的 4 个 head —— 如果「控市值后的低价效应」是一个已被记录、在样本外站得住的现象,它们是脏但真的头;如果没有,它们就是纯痕迹,库里这 4 行会在样本外拖累整组。

---

## 6. 给第 3 轮核对的可检验预测

1. `cs_bucket_rank(cross_ema(day_centroid(Volume), 10), cross_mean(day_std(Amt), 30))`(按已知族分桶)**score ≥ 1.0 且 |rho_known| ≤ 0.15**。信心 **65%**。
   **证伪 ⇒ 若 score < 0.5,我们最高分的 head 是规则 §4-3 的实例,第 3 轮不要再给这个核心任何 E 配额。**
2. 去掉收盘竞价那几格之后(R 第 11 项),核心 score **仍 ≥ 0.9**。信心 **55%**。若掉到 < 0.5,信息其实是「收盘竞价成交占比」,第 3 轮应直接把那个份额写成因子(更干净也更好解释)。
3. 按 `cross_mean(day_flat_ratio(Close), 20)` 分桶后(R 第 3 项)score **≥ 0.9**。信心 **60%**。若崩塌 ⇒ 多头腿主要是锁板 / 冻结名字,而 `long_neutral` 不加掩码,这个 head 在真实交易里不可执行,应主动用 R 把它替换成分桶版。
4. 相关度表里:`cross_ema(day_centroid(Volume), 10)` 与**已知族控制**的 |ρ| 落在 **0.45–0.60**(有实质风险过不了 E 位的核心门槛);核心卡 #2 落在 **0.15–0.30**(能过)。
5. E 位种子里**乙类**(把核心当分桶 / 状态键)与 head #1 的 |ρ| **< 0.4**,全部存活;**甲类**里只套轻度包装的那些 |ρ| **≥ 0.7**,会被相关度表划掉。被划掉的种子数这一轮会**明显多于**第 1 轮的 3 个(第 1 轮库是空的,这一轮库有 6 个 head)。
6. E 位的采样拒绝计数这一轮会第一次出现 `c05_skeleton`(第 1 轮没有,因为库是空的);`no_core` 仍占绝大多数。
7. 第 3 轮 loc 的共性表前几行,又会是我们本轮 E 位自己用的那些子树(和本轮前 7 行同样的污染)。**PI 与解剖员都不要把共性表的头部当独立证据;这一轮已经证明充分性(ablation)是唯一可信的那一列。**
8. M2 那 4 个 head 在样本外会明显退化(静态属性 + 一段行情),而 +1.28 这个 head 若通过了预测 1–3 的诊断,退化幅度明显更小。**本实验内无法核对,留给最终样本外评估。**
