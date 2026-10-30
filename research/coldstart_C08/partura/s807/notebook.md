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
