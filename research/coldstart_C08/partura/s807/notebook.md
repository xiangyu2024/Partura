# 种子 807 · P 组 · PI 笔记

## 第 1 轮

### 上一轮的预测对不对

第 1 轮,没有上一轮,无可核对。

### 我目前对本种子 alpha 来源的信念

快照(M 第 1 批)3 个 head 全是 `cross_regbeta(day_quantile_q75(Volume), Y, d)`。按算子源码化简(恒等,不是近似):

- `cs_median(day_pos_ratio(Open))` ≡ 1.0(Open 恒正);`cs_median(...)` 是每日一个横截面常数,在 `add` 里、在 `cs_bucket_demean` 里、或作为回归自变量的加项时都是精确死重。head 2 ≡ `cross_regbeta(q75Vol, cs_bucket_demean(ts_var(LogFloatCap, 30), LimitWidth), 30)`,head 3 ≡ 同式窗口 20。**3 个 head 实际只有 2 个独立想法。**
- 唯一拿掉就塌的部件是 `ts_var(LogFloatCap, d)`(必要性 +1.34 / +0.65 / +2.90)。它是 log 市值**水平**的方差 ≈ 日频方差·d/6 + 漂移²/12 + 股本跳跃²;控制只覆盖分钟内波动、|漂移| 的 U 形和市值水平,所以残下来的应当是**隔夜 / 日间那一截低频方差**。信心:中(55%)。单独当因子 −2.71 是换手成本(20 点窗口的水平方差 CV ≈ 0.9,每天重排),它需要慢化。
- 外层 `cross_regbeta(q75 Volume, ·)` 主要是代理:beta = corr·sd(Y)/sd(X),截面排序被 sd(X)(本质是成交量水平)主导;Volume→Amt 对 +1 方向的 head 有利。它是来源还是尺度伪影,本轮用 R 的 cross_corr / cross_reg_tvalue 对照钉一下。
- `cs_bucket_demean(·, LimitWidth)` 有中等贡献(+0.44 / +0.33),但 LimitWidth 只有 2–3 个值,桶 = 板块 × 代码片段。
- 奖励的特点:15 bp、十分位纯多头、相对市场的跟踪误差很小 ⇒ **换手是第一约束**。能拿到正分的都是慢信号(外层 30–241 日回归)。所以本轮所有种子都放在 60–120 日尺度。

纠正解剖员的一条:N1「`div(ts_var(...), cs_median(ts_var(...)))`」除以的是每日横截面常数,每日排名不变 ⇒ 与核心本身是同一个信号,不能当新想法。另:`cross_rank(x, d)`、未平滑的 `cs_bucket_rank` 每天只有很少几个取值,过不了 distinct ≥ 0.5 的门槛,种子里不用。

### 本轮计划

- **位 a · E,核心 `ts_var(LogFloatCap, 20)`**(核心卡第 7 位,48 个候选)。外围整个换掉(不含 cross_regbeta / q75 / LimitWidth / cs_median):方差比(log 核心 − log 分钟方差、Yang-Zhang 式相对开盘到收盘方差、时序回归残差)、慢化(120 日均值 / 中位数 / 上尾)、相对自身历史(zscore、log 比、vol-of-vol)、同类相对(规模桶、板块桶)、Amihud 式单位换手方差、量-波协动 corr。
- **位 b · N,交易活跃度与波动的跨日不稳定性**(Chordia-Subrahmanyam-Anshuman 2001;Barber-Odean 2008;Baltussen 等 2018)。灵感来自外层 regbeta 被 1/sd(成交量) 主导这一现象,把它写成尺度无关的变异系数。
- **R**:head 3 六个(Amt、窗口 60、放出 var50、cross_corr / t 值对照、规模分桶),head 2 六个(窗口 60、BoardCode / LogFloatCap 分桶、LogTotalCap 口径、ts_var 窗口 40、cross_corr 对照)。head 2 保留 Volume,避免两条替换收敛成同一个式子。head 1 不动(没有 +0.1 的候选,内层讲不出机制)。

### 事先预测(给第 2 轮回看)

1. **E 位**:会产出 heads,我押 1–3 个,最好的 score 0.6–1.0。赢家最可能是**慢化类**(核心的 60–120 日均值 / 上尾,或 GP 在方差比外面再套一层长窗平滑),方向 −1(做多低频方差低的一端)。纯「相对自身历史」(zscore / log 比)类会偏快、多半 < 0.3;cross_corr 量-波协动类多半 < 0。风险:慢化类与波动控制的 |ρ| 可能到 0.7–0.8,被表格划掉 1–3 个种子。产出 ≥ 1 个 head(≥ 0.5)的概率 60%。
2. **N 位**:产出 0–2 个 heads。最可能是 60–120 日成交额 CV / log 成交额标准差,方向 −1(做多成交稳定端),score 0.3–0.7;vol-of-vol 种子更弱;短窗异常成交那条若赢,方向是 +1。产出 ≥ 1 个 head(≥ 0.5)的概率 40%。与 head 的 |ρ| 应 < 0.3,与流动性控制 |ρ| 0.2–0.5。
3. **R**:head 3 会被 Amt 系变体替换(score ≥ 1.0,概率 80%),其中窗口 60 + Amt 最好;head 2 被窗口 60 那条(或分桶换字段那条)替换,score ≈ 1.0。cross_corr / cross_reg_tvalue 版**明显低于** regbeta 版(≥ 0.3,概率 60%)⇒ 外层的分数主要来自 1/sd(X) 尺度,不是协动。BoardCode / LogFloatCap 分桶与 LimitWidth 版相差 < 0.2。LogTotalCap 口径与 LogFloatCap 相差 < 0.15 ⇒ 股本跳跃不是来源。

## 第 2 轮

### 上一轮的预测对不对

**E 位(核心 `ts_var(LogFloatCap, 20)`)——机制和方向都猜错了,但"会出 head"猜对了。** 实际产生 2 个 head(+0.79、+0.69,r2/loc.json heads[4][5]),赢家清一色是 `cross_corr(ts_var(LogFloatCap, 20), day_sum(Amt)/log(...), 60)` 这一支——协动机制,方向 **+1**。我押的"慢化类赢、方向 −1"、"cross_corr 量-波协动多半 < 0" 全部不对:14 个种子里,慢化(cross_mean/cross_med/cross_tail_mean/cross_zscore)、相对自身历史、vol-of-vol(div(cross_stddev,cross_mean))、bucket 排名这些支系全部没有进最佳 5(missions_before.best 只有 cross_corr 家族),说明"市值方差"真正能打平的不是"它本身够不够稳",而是"它和同期资金流入(Amt)同步到什么程度"——更像一个**流动性事件共振**代理,不是我原来押的低频波动溢价。产出概率我押 60%,方向是对的(真出了),但具体赢家完全在我预期之外,这是本轮最大的一次纠偏。

**N 位(交易活跃度/风险不稳定性)——大叙事猜对,具体支系猜错,score 正向超预期。** 产生 1 个 head(+0.84 / valid +1.63,sign −1,r2/loc.json heads[3])。方向 −1 对了,"产出 ≥1 个 head"对了,但赢家不是我押的"成交额 CV / log 成交额标准差"(Amt 支系的 14 个种子里一个都没进前 5),而是**风险一侧**的 `cross_stddev(log(day_std(Ret)), 120)` 这颗种子,GP 自己变异出 2、3、4 层 log 和 tail_mean 包装后拿到 +0.84(score 还略超出我押的 0.3–0.7 上界)。更值得记下来的一点:它的 **valid(1.63)比 train(0.84)还高**——是本种子目前样本外表现最强的 head,比任何 round 1 E 位的产物都稳。

**R——Amt 置换、cross_corr 塌分两条确认,且比预测更强;cross_reg_tvalue、LogFloatCap 分桶两条预测落空,是本轮的新发现。**
- head 3(旧,`ts_var(LogFloatCap,50)+20` 核心)被 Amt + 窗口 60 变体替换,score 1.4255,远超我押的"≥1.0,概率 80%"——确认。
- cross_corr 版 0.7912 对 regbeta 版 1.4255,差 0.63,比我押的"≥0.3,概率 60%"差距更大——确认且更强:外层分数的大头确实是 `1/sd(X)` 尺度而不是协动。
- **但 cross_reg_tvalue 版 1.2569,只比 regbeta 低 0.17**,远没到我押的 ≥0.3——**预测落空**。t 值本身就是"斜率除以自己的标准误",它和裸相关系数对尺度污染的敏感程度不一样:t 值保住了 regbeta 的大部分信息,说明外层真正的构造里既有尺度伪影也有真实的统计显著性结构,不是纯粹的尺度污染,round 1 的结论("主要是代理")需要打折。
- BoardCode 分桶(1.0025)对同基准 LimitWidth 分桶 1.0191 的 LogFloatCap(30)+window60+Volume 版,差 0.017,**吻合**(<0.2)。但 **LogFloatCap 本身当分桶字段只有 0.6734,差 0.3457,远超 0.2,预测落空**:用规模自己给市值方差分桶,比用板块或限幅分桶明显更差——大概率是因为 `ts_var(LogFloatCap,·)` 本身和 `LogFloatCap` 的水平机械相关,拿 LogFloatCap 分桶等于部分抵消了核心自己的横截面变化,不是"更干净的分组",是"抵消了信号"。这是本轮一条新规律:**不要用和核心共享同一个字段的东西做分桶**。
- LogTotalCap(30)+window60+LimitWidth+Volume = 1.0485,对同基准 LogFloatCap(30)+window60+LimitWidth+Volume = 1.0191(r1/analysis.md §2),差 0.029,远小于我押的 <0.15——**确认**:口径几乎不影响分数,流通股本跳跃不是主要来源,r1/analysis.md §1.2 的 (a)(日频/隔夜方差)比 (b)(股本事件)更可能是主体这一判断站得住。

### 我目前对本种子 alpha 来源的信念(更新)

- `ts_var(LogFloatCap, 20)` 这条线,现在看更像「流通市值短期方差 ↔ 资金流入(Amt)的协动」,而不是单纯的低频波动溢价;它和流动性控制的关系没有被相关度表直接验证过(这条线本轮没有再用 cross_corr 类种子),是后续该盯的风险点。
- **新发现、信心上调到中高:「波动的波动」**(`day_std(Ret)` 在时间上的离散,目前实现为 3 层 log 压缩 + 120 日 cross_stddev)是本种子迄今样本外表现最强、最稳的信号,与 Baltussen 等 (2018) 的「未知的未知」直接对应。round 1 的拆解已经把窗口(60/120/240)和 log 层数(1–4 层)、tail_mean 包装这几类外围用尽,但从来没有问过:这个离散是不是对称的(上行波动冲击 vs 下行波动骤降)、是不是有记忆结构(自相关/Hurst)、是不是规模或板块的构成效应、是不是波动水平控制的非线性影子。本轮 E 位把核心退回最浅的裸 `day_std(Ret)`(sufficiency 行证实 1/2/3 层 log 单独当因子分数逐位相同,层数是外围不是核心),专门打这四个空白。
- **这一批从未被当独立特征用过的东西**:`day_quantile_q75(Volume)` 66 次全部只当回归自变量;叶子 `ListAge` 一次没出现过。本轮 N 位把「日内成交量 q75/q25 比值 / Gini 系数」(交易节奏的日内形状,而不是日与日之间的活跃度或波动)当一个独立特征来试,并用 ListAge 分组做稳健性检验。
- 新规律:**分桶字段不能和被分桶的量共享同一个底层字段**(LogFloatCap 分桶 ts_var(LogFloatCap,·) 系统性变差,差距远超真板块/限幅分桶),本轮 E/N 位里继续用 LogFloatCap 分桶是作为"反向校验"(预计同样会比 BoardCode 差),不是作为主力假设。

### 本轮计划

- **位 a · E,核心退回裸 `day_std(Ret)`**(第 2 次、也是这个核心按规则允许的最后一次 E 位)。外围四类:(1) `cross_semistd_pos/neg` 的非对称波动的波动(Patton & Sheppard 2015);(2) `cross_autocorr`/`cross_hurst` 的记忆结构(Corsi 2009);(3) `cross_zscore(cross_stddev(...))` 的动态"现在是否比平时更不稳"版;(4) 对已验证 head(0.84)做真分组字段中性化(BoardCode/LogFloatCap)和对自身历史波动水平的时序回归残差(`cross_regres`),检验是不是规模/板块构成效应或波动控制的影子。详细机制与为何不同见 r2/missions.yaml。
- **位 b · N,日内成交节奏的形状**(灵感:`day_quantile_q75(Volume)` 的空白用法 + 完全未用过的 `ListAge`)。核心构造是 60/120 日慢化的日内 q75/q25 成交量(金额/股数)比值与 Gini 系数,外加 ListAge/BoardCode/LogFloatCap 分组中性化作稳健性检验。文献:Admati & Pfleiderer (1988)、Kaniel-Saar-Titman (2008)、Zhang (2006)、Amihud & Mendelson (1986)。
- **R**:3 组,分别对当前 3 个 regbeta/corr 系 head 做「已知最大杠杆 + 窗口 + 分桶字段」的组合与交叉验证(见 r2/missions.yaml 各组 why 字段),包括一次 `cross_reg_tvalue@120` 的复核(检验本轮刚发现的"t 值掉分远小于相关系数"这条规律在新窗口下是否还成立)。

### 事先预测(给第 3 轮回看)

1. **E 位**:押非对称(semistd_pos/neg 的 sub 或 div)最可能出 head,因为 round 1 的赢家本身就是"压缩右尾"在起作用,非对称直接针对右尾的来源(是不是波动骤升,而不是骤降,在驱动分数)。自相关/Hurst 类押偏弱(< 0.3),因为它们衡量可预测性,不是离散度,和奖励筛出来的机制距离更远。bucket-demean(BoardCode)版押分数保留大部分(> 0.6,不塌),LogFloatCap 分桶版押明显更差(< 0.5,呼应上面的新规律)。核心与波动控制 `cross_mean(day_std(Ret), 20)` 的 |ρ|:押落在 0.5–0.75,< 0.8(不被判"是控制")的概率 70%。整体位产出 ≥1 个 head 的概率 65%,score 区间 0.5–0.9。
2. **N 位**:押 60/120 日慢化的 q75/q25 比值或 Gini 版最可能出 head,方向 −1(稳定的日内节奏更好,呼应同一个「厌恶不确定性」大叙事);未慢化的单日版本(种子 1)押很弱(< 0,换手成本吃掉);day_gini 和 q75/q25 比值两种写法的 |ρ| 押 > 0.7(同一件事的两种估计量)。ListAge 中性化后分数保留 > 0.6;`cs_rank(ListAge)` 单独押 < 0.3(不到发现线)。整体位产出 ≥1 个 head 的概率 45%,score 区间 0.3–0.6。
3. **R**:head1(Amt,window60,LimitWidth)窗口 120 应接近已知的 1.6957(r_candidates),90 介于 60 和 120 之间;BoardCode 分桶与 LimitWidth 相差 < 0.2,LogFloatCap 分桶明显更差(> 0.3 差距,复验上面的新规律);`cross_reg_tvalue@120` 相对 `regbeta@120` 的掉分应同样 < 0.3(复验"t 值掉分小"这条新规律,而不是 round 1 最初押的 ≥0.3)。head2(LogTotalCap)Amt 置换应接近已知的 1.6296;LogFloatCap 口径差距仍 < 0.15。head5(cross_corr)的 Volume 置换应接近已知的 1.1316,叠加窗口 30 后押在 1.0–1.3 之间(两个方向都是正贡献但不完全叠加)。
