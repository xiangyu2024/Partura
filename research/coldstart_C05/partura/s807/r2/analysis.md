# 结构解剖:种子 807,B 组,第 2 轮

读入:`r2/loc.md`、`r2/loc.json`、`r2/R_prev.json`、`r1/loc.md`、`r1/loc.json`、`r1/analysis.md`、`r1/lit.md`、`r1/missions.yaml`、`notebook.md`、PLAN.md,以及算子与奖励源码
(`alphacube/operators/dt_day.py`、`dt_cross.py`、`nd_ts.py`、`nd_cs.py`、`common.py`,`partura/ops_ext.py`、`partura/steer.py`、`partura/books.py`、`scripts/idea_search.py`)。
只用了 train / valid 的数字。

---

## 0. 先钉死六条机械事实(本轮所有判断都挂在这上面)

读源码得到的,不是推测。后面反复要用。

**(M-a) `ts_sum(x, 1)` 是恒等算子。** `ts_sum = rolling_reduce(x, d, nansum_last, axis=0)`,d = 1 就是 x 自己。
所以快照里最高分的那个 M2 head

    ts_sum(pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1)), 1)

的真身就是 **`day_durbin_watson(High)` 的 7.5 次幂**。证据对得上:knockout 掉内层 `ts_sum` 的变体
`ts_sum(pow_2_5(pow_3(day_durbin_watson(High))), 1)` 得 1.7782,必要性 **−0.0029**;
而 `ts_sum(pow_3(day_durbin_watson(High)), 1)`、`pow_3(day_durbin_watson(High))`、`ts_sum(ts_sum(pow_3(day_durbin_watson(High)), 1), 1)`
三者 score / train / valid 完全相同(0.9641 / 0.9641 / 2.6382)。

**(M-b) 奖励的次序是「先在原始值上做 EMA,再 z-rank 做中性化残差,再分十分位」。**
`partura/steer.py`:`sm0 = bk.smoothed(raw, hl)` → `neutral_residual(sm0, Q)`(内部先 `_zrank` 再投影)→ `sign * sm0` → `book_row`。
而 `books.smoothed(sig, 0)` 直接返回原数组。推论:
- **hl = 0 时,根上任何严格单调的一元包装(`pow_2` 作用于非负量、`pow_3`、`pow_2_5`、`sqrt`)是精确的空操作**;
- **hl > 0 时,这类包装唯一的作用是改变各天在 EMA 里的权重** —— 把时间平均偏向该量最大的那几天。
`steer.py` 的 `MONOTONE_ANY` / `MONOTONE_NONNEG` 注释原文就是这个意思:"At the ROOT of a candidate such a wrapper changes
nothing a rank-based book sees on the day -- only how the days mix under the EMA"。

**(M-c) `day_durbin_watson` 不是教科书的 DW,而且恒为非负。** 源码 `dt_day.py:273`:

    DW(x) = sum_t (x_t - x_{t-1})^2 / (sum_t x_t^2 + 1e-8)      # 分母**没有**去均值

分子分母都是平方和,所以恒 ≥ 0,且在价格水平上**齐次、尺度无关**(分子 ≈ P²·Σ(Δlog High)²,分母 ≈ T·P²),
**不是价格 / 规模的代理**。量纲是「每分钟收益的平方」:

    day_durbin_watson(High) ≈ (1/T)·Σ (ΔHigh_t / P)^2 ≈ 分钟高价序列的每分钟已实现方差

也就是 ≈ `day_std(Ret)` 的平方(差别只在"用分钟最高价序列而不是收盘价序列"这一点上)。
配合 (M-b):`DW ≥ 0` ⇒ `pow_3`、`pow_2_5` 作用在它上面**截面上秩完全不变**,全部效果都在 EMA 的跨日加权里。
(顺带:`day_durbin_watson` 既不在 `NONNEG_OPS` 也不在 `SIGN_KEEPING_OPS`,所以 `steer.py` 的 `nonneg()` 判不出它非负,
`strip_root_monotone` 抓不到 `pow_2_5` 这一层 —— 幂次阶梯因此没有被去重吃掉,每一级都真金白银花了一次评估。这是现象,不提议改代码。)

**(M-d) `cross_*(x, d)` 是沿**天**轴的滚动统计,不是截面统计;`cs_*` 才是截面。**
`rolling_reduce(..., axis=0)`,面板是 (天, 股票)。`cross_fangzheng(x, d) = cross_mean(x, d) + cross_stddev(x, d)`(60 日均值 + 60 日标准差)。
名字容易误读,笔记里要留一条。

**(M-e) 奖励控制的"波动"是 `cross_mean(day_std(Ret), 20)`,是**均值**型。**
`scripts/idea_search.py:178-181`:控制 = 流动性 `liq`、`cross_mean(day_std(Ret), 20)`、
`div(day_last(Close), ts_delay(day_last(Close), 20))`、已知族、`LogFloatCap`。
所以"日内波动的 20 日**平均**"被投影掉了,"日内波动的**极端**"没有。本种子几乎所有发现都长在这条缝里。

**(M-f) `cross_corr(a, b, d)` 在本种子的量纲下**不是相关系数**。**
`common.py:640`:`return cov / (torch.sqrt(var_x * var_y) + EPS)`,`EPS = 1e-9`(`common.py:43`)。
取 `W = day_wmean(Ret, Ret)`(量纲是一个分钟收益,|W| ~ 1e-4 ~ 1e-3):W² ~ 1e-7,W⁴ ~ 1e-14,
`var(W²)` ~ 1e-14,`var(W⁴)` ~ 1e-28,`sqrt(var·var)` ~ **1e-21**,比 EPS 小十二个数量级(float32 下连 `var_x*var_y` 本身都已掉进次正规数)。于是

    cross_corr(pow_2(W), pow_2(pow_2(W)), d) ≈ 1e9 × cov_d(W², W⁴)
    cross_corr(pow_2(W), pow_2(W), d)        ≈ 1e9 × var_d(W²)        # 自己和自己求相关:解析上 = var/(var+EPS)

要让归一化重新起作用需要 |W| ≳ 0.05(加权分钟收益 5%),不可能。**结论:r1a 产出的七个 `cross_corr` head 全部是
未归一化的滚动共矩(co-moment)× 1e9,截面排序由 W 的量纲(幅度)主导,外加一个 EPS 造成的阈值型非线性,
不是它们看起来的"窗口内形状 / 相关性"机制。** 第 1 轮 missions.yaml 里写的假设(主押"单边程度在时间上的形状")
在算子层面没有实现成那个东西。

---

## 1. alpha 的来源

### 1.1 真来源 ①(最强):非负日内变动量的**凸时间聚合**

一句话:本种子最大的一块 alpha 不是一个截面特征,而是一个**时间聚合的选择** ——
把一个非负的日内"动得多不多"的量,用凸幂放进 20 日 EMA(等价于一个偏向最大那几天的软幂平均),方向一律 **−1**(纯多头书买没有极端日的股票)。

**三条互相独立的幂次阶梯(每一级在截面上秩完全相同,差别只在 (M-b) 的 EMA 加权):**

| 通道 | 指数 | score | train | valid |
|---|---|---|---|---|
| `day_durbin_watson(High)`,hl 20 | ^1 | −1.1711 | −1.1711 | +0.5771 |
| | ^3 | +0.9641 | +0.9641 | +2.6382 |
| | ^7.5 | **+1.7770** | +1.7770 | +2.6633 |
| `pow_2(day_topw_mean(Ret, Amt))`,hl 20(r1b/N) | ^2(= 折叠) | −0.2982 | −0.2982 | +0.5729 |
| | ^4 | +0.1445 | +0.1445 | +0.8622 |
| | ^8 | **+0.6845** | +0.6845 | +1.6221 |
| `pow_2(day_wmean(Ret, Ret))`,hl 20 | ^1(带符号) | −0.1875 | −0.1541 | −0.1875 |
| | ^2(折叠,真实新信息) | +0.8935 | +0.8935 | +1.6550 |
| | ^3 | +1.0692 | +1.0692 | +1.5376 |
| | ^4 | +1.1814 | +1.1814 | +1.3462 |
| | ^6 | +1.1253 | +1.1889 | +1.1253 |

读法:
- DW 与 topw 两条阶梯 **train 与 valid 同时上升**(DW:valid 0.58 → 2.64 → 2.66;topw:0.57 → 0.86 → 1.62)。
  这两条通道的凸聚合在两段里都真的有信息。
- W 这条阶梯只有**第一步**(带符号 → 折叠)是新的截面信息(−0.19 → +0.89,knockout 必要性 +1.56 / +2.05);
  折叠之后再加幂次,**train 单调上升(0.89 → 1.07 → 1.18 → 1.19)而 valid 单调下降(1.66 → 1.54 → 1.35 → 1.13)**。
  这是第 1 轮 R6 预测的事,预测全中;也是一个很干净的过拟合签名:**W 通道的凸幂是在拿 valid 换 train**。
- 所以"凸幂 + EMA"不是万能的:它在起点很差的通道(DW、topw)上两段都加分,在已经饱和的通道(W²,valid 已 1.66)上只加 train。

**同一来源的另一种聚合(hl = 0,完全不用幂次):** head `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)`
= `cross_stddev(day_durbin_watson(High), 60)`,score +1.1007(train 1.1007 / valid 2.0459),sign −1。
**这是本轮最重要的一条证据**:同一个测量量 `day_durbin_watson(High)`,换成一个完全不同、不含任何幂次 / EMA 技巧的聚合
(60 日滚动标准差),照样过线很多。**说明 `day_durbin_watson(High)` 本身是真来源,不只是"幂次 + EMA"这个技巧的载体。**

**充分性 / 必要性 / 敏感性(付费证据)**:
- 充分性:`pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1))` 自身 1.7770 = 所在 head 的 100%(本来就是同一个表达式);
  `pow_3(day_durbin_watson(High))` 0.9641(54%);裸 `day_durbin_watson(High)` −1.1711。
- 必要性:去掉 `pow_2_5` 这一层 +0.81;去掉 `pow_3` 这一层 +1.06;去掉 `ts_sum` **−0.00**(见 M-a)。
- 敏感性:`High → Low` 换字段 1.5391(train 1.5391 / valid **2.7655**,valid 还更高)—— 稳;
  `ts_sum@1 → 2` 1.9025(更好,+0.127,是本轮唯一的机械 R 候选,ρ_head 0.9994)。
- 共性:`day_durbin_watson(High)` 出现在 279 个存档候选的 57 个里,含 +0.29 / 不含 −1.00,均值差 +1.28,p 0.000。

**共性那一栏要大打折扣(本轮新增的方法学问题)**:279 个存档候选来自四次运行(M1、M2、r1a、r1b),
而 `day_durbin_watson` 只出现在 M2 的存档里、`day_wmean` 基本只出现在 M1 与 r1a 里(r1a 是 E 位,**每个候选都被强制含核心**)。
所以"含它的候选均值高"大部分是在说"M2 这次运行比 r1b 这次运行好",不是"这个子树有用"。
**本轮的共性表已经退化成'哪次运行运气好',只有拆解(付费评估)那一栏是干净的。** 这条要写进笔记,第 3 轮同样适用。

### 1.2 真来源 ②:多日**方向持续性**的幅度

head `pow_2(pow_2(cross_mean(day_wmean(Ret, Ret), 5)))`(M1,R 替换后生效),score 1.7104 / train 1.7104 / valid 2.4955。
拆解:

| 子树 | score | train | valid |
|---|---|---|---|
| `cross_mean(day_wmean(Ret, Ret), 5)`(带符号 5 日平均) | +0.1476 | +0.1476 | +0.2958 |
| `pow_2(cross_mean(day_wmean(Ret, Ret), 5))` | +1.0515 | +1.0515 | +1.9396 |
| head(再平方) | +1.7104 | +1.7104 | +2.4955 |

窗口敏感性:`cross_mean@5 → 2` 1.4926(valid 1.9774);`@5 → 10` 1.3986(valid 2.4940)。2 / 5 / 10 全部 ≥ 1.40,稳。
必要性:knockout 掉 `cross_mean` 退回 `pow_2(pow_2(day_wmean(Ret, Ret)))` = 1.1814,必要性 **+0.53**。

**这和来源 ① 不是一回事,是本种子唯一一条不同的信息。** 关键在次序:先把**带符号**的 W 在 5 天上平均(要求方向连续几天站在同一边),
再折叠成幅度。第 1 轮 R 的对照支持这个读法:`cross_mean(pow_2(pow_2(day_wmean(Ret, Ret))), 5)`(先折叠再平均)只有 1.3561,
`pow_2(pow_2(cross_mean(day_wmean(Ret, Ret), 5)))`(先平均再折叠)1.7104。**先平均再折叠 > 先折叠再平均**,
差的那 0.35 就是"方向在多日之间是否持续"。而且这条阶梯 train 与 valid 同时上升,不像 1.1 里 W 的日度阶梯那样拿 valid 换 train。

### 1.3 不是来源,是数值退化:r1a 的七个 `cross_corr` head

由 (M-f),它们是 `1e9 × 滚动协方差`,排序由 W 的幅度量纲主导。**四条互相独立的旁证:**

1. **符号随窗口翻转**:`cross_corr(pow_2(W), pow_2(pow_2(W)), d)` 在 d = 241 时 sign **+1**、120 时 −1、60 时 −1、30 时 −1;
   `cross_corr(pow_2(W), pow_2(W), d)` 在 20 时 −1、60 时 −1、241 时 −1;而 `(W², W⁴, 20)` 又是 **+1**。一个真机制不会这样。
2. **窗口敏感性崩塌**:241 → 482 时 score 从 1.7835 掉到 **+0.1565**(train 0.2956 / valid 0.1565)。
3. **head #5 `cross_corr(pow_2(day_wmean(Ret, Ret)), pow_2(day_wmean(Ret, Ret)), 20)` 是自己和自己求相关**,
   解析上 = `var/(var+EPS)`,在本量纲下 ≈ `1e9 × var_20(W²)`。它得了 1.2106 —— 这个 head 的真身是
   **`cross_stddev(pow_2(day_wmean(Ret, Ret)), 20)` 的平方**,一个完全可以老实写出来的量,却被写成了一个退化的相关系数。
4. **归一化项正好落在 EPS 量级的那一个最脆**:head `cross_corr(pow_2(day_signed_ratio(Ret, Ret)), pow_2(day_wmean(Ret, Ret)), 20)`
   的 `sqrt(var_x·var_y)` ≈ 1e-9 ≈ EPS,它的截面取决于每只股票的方差落在 EPS 哪一侧,是整组里最不可复现的一个。

这不是说这七个 head 一定没用(valid 都在 0.61 ~ 2.71);是说**它们属于来源 ①(幅度族),不是一条新机制,
而且它们的具体写法依赖一个 1e-9 的常数**。对最终判读的直接影响见 §3.1 末尾。

另外两个顺手的机械等式,写进笔记:
- `day_wmean(Ret, <价格字段>)` ≈ `day_mean(Ret)`。`day_wmean(x, w) = Σx|w|/Σ|w|`,日内价格的相对变化只有 1% 量级,
  所以用 `Low` 当权重 ≈ 等权。head `cross_corr(pow_2(day_wmean(Ret, Low)), pow_2(day_wmean(Ret, Ret)), 20)` 里的
  `day_wmean(Ret, Low)` 实质是 `day_mean(Ret)`,而 `pow_2(pow_2(day_mean(Ret)))` 只有 0.2570、
  `day_wmean(Ret, Low)` 的共性是 **−0.2031**。这个部件没有信息。
- `cross_fangzheng(x, 60) = cross_mean(x, 60) + cross_stddev(x, 60)`;作用在近似常量上(例如 `pow_2_5(LogFloatShares)`)时标准差项 ≈ 0,
  整个算子退化成水平本身。

### 1.4 代理,不是来源

- **`LogFloatShares` 一族 = 低价效应。** `dailyfields.py:57`:`LogFloatShares = log(FloatShares)`、`LogFloatCap = log(FloatCap)`,
  而 `FloatCap = FloatShares × Price`,所以 `LogFloatShares = LogFloatCap − log(Price)`。
  中性化控制里**有 `LogFloatCap`、没有价格**(M-e),于是 `LogFloatShares` 投影掉规模之后剩下的 ≈ **−log(价格)**。
  head `ts_sum(LogFloatShares, 30)`(hl 0,sign +1,score 0.5177)在 hl = 0 下 `ts_sum(·,30)` 只是 30 倍的水平、z-rank 后秩不变,
  所以它就是"纯多头书买低价股",A 股最老的已知异象之一,分数也只有 0.52。
  核心卡 #8 `pow_2_5(LogFloatShares)`、#10 `cross_fangzheng(pow_2_5(LogFloatShares), 60)`、#11 `pow_3(pow_2_5(LogFloatShares))`
  是同一个东西的三种写法(幂次在 hl = 0 下是空操作,fangzheng 退化成水平)。**整个实验都不该给它们 E 位。**
- **`day_signed_ratio(Ret, Amt)`(BVC 净买压)= 死胡同。** 共性是全表最差:n 8,含它的候选均值 **−1.7119**,均值差 −1.0079。
  第 1 轮 N 位把 14 个种子的一半押在这条通道上,0 个过线。别再花钱。
- **`day_topw_mean(Ret, Amt)` 原始量**:共性 −0.2481(n 12);只有折叠 + ^8 的版本过线,所以它过线靠的是来源 ①,不是"聪明钱"本身。
- 沿用第 1 轮的判断:`ts_cov(day_median(Vwap), day_var(Ret), 20)`(+0.17,p 0.515)、`day_var(Ret)`(+0.09,p 0.621)、
  `day_median(Vwap)`(−0.02)、`day_quantile_q75(Volume)`(−0.08)、`day_std(Close)`(−0.55)、`cs_rank(day_mean(Ret))`(−0.58)
  —— 含它们的候选平均都在亏,是血缘固定块,不是来源。

### 1.5 还没排除的替代解释(本轮最大的未知)

**来源 ① 和被控制掉的 `cross_mean(day_std(Ret), 20)` 是同一族的"均值 / 极值分解"。** 由 (M-c),
`day_durbin_watson(High)` ≈ `day_std(Ret)²`(换了价格序列),而控制掉的是它的 20 日均值。
所以来源 ① 的残差很可能就是 **Bali–Cakici–Whitelaw 的 MAX 相对 IVOL 那一层** 搬到日内已实现波动上。
第 1 轮 R 的两条数字让这件事**不能当成已排除**:

| 第 1 轮 R 变体 | score | train | valid |
|---|---|---|---|
| `pow_2(pow_2(day_std(Ret)))` | +0.0287 | +0.0287 | **+2.0788** |
| `pow_2(pow_2(day_wstd(Ret, Ret)))` | +0.9336 | +0.9336 | **+2.7841** |
| `div(pow_2(day_wmean(Ret, Ret)), day_var(Ret))`(除掉日内方差) | +0.3671 | +0.3671 | +0.7103 |
| `pow_2(day_signed_ratio(Ret, Ret))`(无量纲路径效率) | −0.9894 | −0.9894 | −0.6286 |

第 1 轮笔记按 score 判"波动尾部单独不是来源"(R1 预测正确)—— 但那是 **train 绑定**的结论:
`pow_2(pow_2(day_std(Ret)))` 的 valid 夏普是 **2.08**,`pow_2(pow_2(day_wstd(Ret, Ret)))` 的 valid 是整组 R 里最高的 **2.78**。
波动尾部在 valid 段非常强,只是在 train 段不行。**"排除旧异象"这件事远没有完成。**

同时,两条"去量纲"的对照都塌了(路径效率 −0.99;除掉 `day_var` 从 1.18 掉到 0.37)。
合起来说明:**W 通道里起作用的大部分是"日内动了多大"这个量纲,方向折叠只是在上面加了一点。**
这是对第 1 轮核心解释("日内单边程度")的一次实质修正 —— 它更像"带方向加权的日内波动幅度"。

还有一条全局的方法学提醒:**本种子 12 个 head 里 9 个 valid > train**,所以多数 head 的 score = train 夏普,
而方向、半衰期、幂次、窗口、mask 全部是在 train 上选的。**"这一族有东西"的证据(每个成员 valid 都 ≥ 1.0)远强于
"这个指数 / 这个窗口是对的"的证据。** 别把 1.78 和 1.71 的差别当成机制上的差别。

---

## 2. 烂部件(适合做 R)

| # | 部件 / head | 证据 | 判断 |
|---|---|---|---|
| 1 | `ts_sum(·, 1)`,在最高分 head 里出现**两层** | 必要性 **−0.0029**;去掉两层的 `pow_2_5(pow_3(day_durbin_watson(High)))` = 1.7782 ≥ head 1.7753 | 恒等算子,纯死重。差额不到 +0.1 不能触发替换,但库里要知道这个 head 的真身是 `DW(High)^7.5` |
| 2 | `cs_mask_top_replace_mean_neg`(把截面最低 10% 抹成行均值) | 共性 +0.32、**p 0.177 不显著**;所在的两个 head 一个 0.9972(train 1.00/valid 2.71)、一个 0.7071(**train 2.02 / valid 0.71,全库最大缺口**) | 没有机制,只是抹掉最平静的一成股票的区分度。拿 0.707 那个 head 做 R(门槛只要 0.807,便宜) |
| 3 | head `cross_corr(pow_2(day_wmean(Ret, Ret)), pow_2(pow_2(day_wmean(Ret, Ret))), 241)`(1.7835)整个 | sign +1 与 120/60/30 的 −1 相反;482 窗口塌到 +0.16;叠加 (M-f) 的 EPS 退化 | 不是"可以去掉一个部件",是**整个 head 不可信**。换成老实的归一化 / 未归一化写法去比 |
| 4 | `cross_corr(x, x, d)`(head #5 与两个 knockout 变体) | 解析上 = `var/(var+EPS)`,本量纲下 ≈ `1e9 × var_d(x)` | 可以原样改写成 `cross_stddev(pow_2(day_wmean(Ret, Ret)), d)`,ρ 必然很高,有机会直接替换成一个可解释的 head |
| 5 | `day_wmean(Ret, Low)` 里的 `Low` 权重 | 价格字段当权重 ≈ 等权(§1.3);`pow_2(pow_2(day_mean(Ret)))` 只有 0.2570;`day_wmean(Ret, Low)` 共性 −0.2031 | 这个部件没信息,换成 `day_mean(Ret)` 或 `Amt` 权重 |
| 6 | `div(·, LimitWidth)` / `div(·, pow_2(LimitWidth))` | 第 1 轮 R:`pow_2(pow_2(div(day_wmean(Ret, Ret), LimitWidth)))` = −0.1305(train 0.8627 / valid −0.1305);E 位里这一支也没出 head | 两次独立证伪(E3 预测正确)。整个实验不要再花钱 |
| 7 | `pow_2(pow_2(day_zero_ratio(Ret)))` —— **空对照缺失,不是被排除** | gate **false**,`distinct` 只有 0.0544(取值几乎是常量),根本没评上分 | "薄交易"这条替代解释至今没有对照。要补就换 `day_flat_ratio(Close)` 或 `cross_mean(day_zero_ratio(Ret), 20)` |

---

## 3. 第 1 轮任务的复盘

### 3.1 E 位 `c05s807Br1a_Ea`,核心 `pow_2(day_wmean(Ret, Ret))`

76 次评分、13 个过线、**7 个进 heads**。采样计数 `{c05_no_core: 2452, c05_skeleton: 3, c05_periphery_seen: 13}`
—— 卡住生成器的是"必须原样含核心"(2452 次拒绝),"外围必须没见过"只拦了 13 次,**不是约束瓶颈**。

**试了什么外围、哪一族赢了**:16 个种子分四族(时间形状 7 / 给定幅度后的方向 3 / 放量薄交易共动 2 / 日内时点与归一化 4)。
7 个 head **全部**是 `cross_corr(...)` 形状,最接近种子 #7(`cross_corr(核心, cross_delay(核心, 1), 20)`)、
#9(`cross_corr(核心, day_wmean(Ret, Ret), 20)`)、#12(`cross_corr(核心, day_flat_ratio(Close), 20)`,
GP 把字段换成 `Ret` 并加了 mask,成了 0.9972 那个 head)。
`cross_argmax` / `cross_madz` / 变异系数 / `cross_tail_mean_q25` 这几支没出 head;`mul(核心, 日频叶子)` 那一族、
日内时点那一族、`LimitWidth` 那一族全部没出 head。

**但是**:由 (M-f),赢的这一族在算子层面并不是"时间形状",而是未归一化的共矩。
**「时间形状这条押对了」这个结论要撤回** —— 押中的是"一个同时含核心的二元滚动统计",而它之所以能躲开家族控制,
是因为它带着核心的量纲、却不是核心的单调函数。

**对最终判读的影响(要提醒 PI)**:r1a 名义上的 7 个 head,其中 #1(241,sign +1,hl 0)与 #3(60,sign −1,hl 0)
是同一构造的两个窗口、方向相反。PLAN §3 的最终库去重是"与已收 head ρ ≥ 0.7 **或 ρ ≤ −0.5** 就丢"
(就是为了修 C04 的孪生抵消)。两者 hl 都是 0、输入完全相同、窗口 241 与 60 重叠极大,
交易信号很可能 ρ ≤ −0.5 互相枪毙。**r1a 的 7 个 head 在最终库里大概只值 1~2 个。**
这也是本轮应该去找"不同机制"而不是"同一机制的第八种写法"的最硬的理由。

### 3.2 N 位 `c05s807Br1b_Nb`

66 次评分、1 个过线、1 个 head:`pow_2(pow_2(pow_2(day_topw_mean(Ret, Amt))))`(0.6845 / valid 1.6221)。
前五名里 `day_signed_ratio(Ret, Amt)` 一个都没有,最好的是折叠版。
由 §1.1 的第二条阶梯,**这个 head 不是一条新机制,是来源 ① 在第三条测量通道上的又一次出现**(折叠 + 凸幂 + EMA)。
N 位的"换一条被观测的量"这个想法本身是对的(聪明钱分钟),但产出的 alpha 来自聚合层,不是那条通道。

### 3.3 R(16 次付费,1 次替换)

替换生效:`pow_2(pow_2(cross_mean(day_wmean(Ret, Ret), 5)))`(1.7104)顶掉 `pow_2(pow_2(day_wmean(Ret, Ret)))`(1.1814)。
`cross_mean(pow_2(pow_2(day_wmean(Ret, Ret))), 5)`(1.3561)也达到了门槛,是第二名。
R 的主要收获不是替换,是 §1.5 的四条量纲对照和 §1.1 的 W 幂次扫描。

### 3.4 第 1 轮事先预测的打分

| # | 预测 | 结果 | 实际 |
|---|---|---|---|
| E1 | E 位产出 ≤ 1 个 head(把握 0.65) | **错(错得最有价值)** | 7 个。**教训:带核心量纲、但不是核心单调函数的二元滚动统计,几乎不被家族控制扣分。** 家族控制比预期弱得多 |
| E2 | 若有 head,来自"时间形状"或"给定幅度后的方向",不是乘日频叶子 / 日内时点(0.6) | **字面对、机制上撤回** | 7 个全是 `cross_corr`,乘叶子与日内时点全军覆没;但 (M-f) 说明它不是"形状" |
| E3 | `div(核心, pow_2(LimitWidth))` 不过线(0.75) | **对** | R 的 LimitWidth 版 −0.1305,E 位里也没出 head |
| N1 | N 产出 ≥ 1 个 head(0.55) | **对(擦线)** | 恰好 1 个,66 次评估 |
| N2 | 若有 head,最好的是**带符号**的流向 / 聪明钱,不是折叠版(0.55) | **错** | 赢的是折叠的 `pow_2(pow_2(pow_2(day_topw_mean(Ret, Amt))))`;**反而支持"幅度有信息、符号没有"这条假设,在第二条测量通道上又一次成立** |
| N3 | N 的 head 与 M 的 head 残差 \|ρ\| < 0.5(0.7) | **本轮无法核对** | 定位输出没给这对 ρ。若 PI 要用,得另外算 |
| R1 | `pow_2(pow_2(day_std(Ret)))` score < 0.5(0.6) | **对,但结论要降级** | score 0.0287。**valid 却是 2.0788** —— 波动尾部在 valid 段很强,"排除旧异象"没完成(§1.5) |
| R2 | 经典 MAX < 1.18(0.75) | **对,而且很强** | `cross_max(div(day_last(Close), ts_delay(day_last(Close), 1)), 20)` = −0.8543。**本族不是经典日收益 MAX 效应** |
| R3 | `pow_2(pow_2(day_mean(Ret)))` < 0.5(0.55) | **对** | 0.2570。`day_wmean` 的自加权确实必要 |
| R4 | `pow_2(day_signed_ratio(Ret, Ret))` ≥ 0.5(0.5) | **错** | −0.9894。**无量纲化把它杀死 → 量纲(日内动多大)才是主料** |
| R5 | `cross_max(pow_2(W), 20)` ≥ 0.9 且 valid ≥ train(0.45) | **半对** | 0.7738 < 0.9(错);valid 1.0709 ≥ train 0.7738(对)。硬极值打不过软幂平均 |
| R6 | 幂次扫描:valid 从 p=2 起不升,train 在 p ≥ 4 见顶(0.55) | **全对** | valid 1.655→1.538→1.346→1.125 单调降;train 0.894→1.069→1.181→1.189 在 p≈6 见顶 |
| R7 | 本轮没有任何 R 变体达到替换门槛(0.7) | **错** | 两个达到(1.7104、1.3561)。**先在时间上平均再凸化,是本轮最大的单笔收益(+0.53)** |

合计:对 7、错 4、半对 1、无法核对 1。四个错的恰好是信息量最大的:家族控制比想象的弱(E1)、
幅度胜过方向(N2)、无量纲化就死(R4)、先平滑再凸化赢很多(R7)。

---

## 4. 本轮候选

### 4.1 值得深挖的核心(按推荐顺序)

**核心 ①(首推)`pow_2(cross_mean(day_wmean(Ret, Ret), 5))`** —— 机械核心卡 #3,自身 score 1.0515,所在 head 1.7104。

- 为什么是它:§1.2 的三条证据齐(充分性 1.05 = head 的 62%;必要性 +0.53;窗口 2/5/10 全 ≥ 1.40),
  而且**是本种子唯一一条不是"幅度"的信息**(方向在多日之间的持续性)。最终指标是融合后的残差书、去重按 ρ 砍,
  本种子库里已经挤满了幅度族,**再加一个幅度族成员的边际价值接近 0,加一条不同的信息才值钱**。
- **它周围已经见过的外围写法(很少,这是它最大的优势)**:只有 `{pow_2}`(head 本身就是它的平方);
  R 里见过的近邻是 `cross_mean(pow_2(pow_2(day_wmean(Ret, Ret))), 5)`(先折叠再平均,1.3561)。
  家族控制只会放进一个 head(1.7104),是三个候选里最轻的。
- 外围该往哪长(都没见过):持续了**几天**与持续得**多强**的区分(符号的游程 / 自相关)、
  持续性与成交额 / 隔夜缺口 / 板宽的交互、把固定的 5 天换成"自上一次方向反转以来"、
  以及"方向持续 × 幅度"的二维切分(而不是先乘起来)。
- 注意:核心里已经含了一个 `pow_2`,所以根上再加任何单调包装在 hl = 0 下是空操作、hl > 0 下只是 EMA 加权(M-b);
  任务假设里要写明,别让 GP 把 96 次评估花在幂次阶梯上(M2 就是这么浪费的)。

**核心 ②(次推)`day_durbin_watson(High)`** —— 机械核心卡 #7,共性 +1.2848 / p 0.000 / n 57。

- 为什么是它:§1.1 里它是唯一有**两种互相独立的有效聚合**的测量量(`^7.5` + EMA20 → 1.7770;
  `cross_stddev(·, 60)` + hl 0 → 1.1007),换字段 `High → Low` 还稳(1.5391,valid 2.7655)。
  **取裸的测量量而不是 `pow_3(...)` 版本**:凸幂那一层已经被证明只是时间聚合(M-b/M-c),
  把它写进核心等于把家族控制必然扣光的那一层固定住,白送 96 次评估。
- **它周围已经见过的外围写法**:`{pow_3, pow_2_5, ts_sum}`(= `DW^7.5`,head 1.775);
  `{ts_sum, cross_stddev@60}`(head 1.101);`{cross_fangzheng@60, pow_2_5, ts_sum, pow_3}`(共性,n 4);
  `{pow_3}`、`{pow_2_5 ∘ pow_3}`。概括起来**只见过"幂次"和"滚动标准差 / fangzheng"两招**,而这两招都会进家族控制。
- 外围该往哪长:**条件化**(只在跳空日 / 贴近板宽日 / 高 `day_flat_ratio` 日上算)、
  相对自身历史的位置(`cross_madz`、分位、5 日减 60 日)、
  **上下行抖动的不对称**(`DW(High)` 与 `DW(Low)` 的差或比 —— 换字段证据说明两边都带信息)、
  按 `ListAge` / `BoardCode` 分组、以及和活动通道的交互。
- **风险(必须写进任务假设)**:由 (M-c)+(M-e),它 ≈ `day_std(Ret)²` 换了价格序列,而控制掉的是后者的 20 日均值;
  §1.5 说明"波动尾部"在 valid 段很强、远没被排除。**本轮的 R 空对照拿不到结果就要写这个 E 位**
  (R 和 GP 位同一轮并行),所以这个位有可能整个花在一条已知异象上。这是我把它排第二的唯一理由。

**核心 ③(本轮不推荐,留给第 3 轮)`pow_2(day_wmean(Ret, Ret))`** —— 整个实验还剩 1 个 E 位。
r1a 已经在它身上花了 76 次评估、出了 7 个 head,家族控制现在要放进 6 个(按 score 取前 6);
而且那 7 个 head 的真身是 §1.3 的 EPS 退化共矩,**先用 R11~R13 把这一族的真身判清楚,再决定第 3 轮要不要用掉最后一个位**。

**明确不要给 E 位的核心卡**:#4 `ts_sum(pow_3(day_durbin_watson(High)), 1)`、#5 `pow_3(day_durbin_watson(High))`、
#6 `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)`、#12 `cross_stddev(day_durbin_watson(High), 60)`、
#9 `cross_fangzheng(pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1)), 60)` —— 都是把已知的聚合层写死在核心里(理由同核心 ② 的第一条);
#8 `pow_2_5(LogFloatShares)`、#10、#11 —— 低价效应代理(§1.4);
#13 `day_wmean(Ret, Ret)`、#14 `pow_2(cs_mask_top_replace_mean_neg(pow_2(day_wmean(Ret, Ret))))`、#15 —— 同 ③ 或已判烂部件。

### 4.2 R 目标(按价值排序;R1 已付过钱)

挂 `ts_sum(pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1)), 1)`(1.7753):

1. **`ts_sum(pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1)), 2)`** —— 定位工具已评过:1.9025,增益 +0.1273,ρ_head 0.9994,**达到替换门槛**。PI 只需确认替换,不花预算。
2. **`pow_2_5(pow_3(day_std(Ret)))`** —— 决定性空对照:同一条幂次阶梯换成被控制掉的那个波动输入本身。若接近 1.78,来源 ① 就是"日内波动的极值 / 均值分解",§1.5 的替代解释成立。
3. **`pow_2_5(pow_3(day_durbin_watson(Close)))`** —— `Close` 不在 `High↔Low` 的换字段组里,从没测过。判"最高价序列"这件事是否必要。
4. **`pow_2_5(pow_3(day_durbin_watson(Amt)))`** —— 换成活动通道:是价格的抖动还是成交的抖动。(DW 尺度无关,所以这是"分钟成交额曲线有多锯齿"。)
5. `pow_2_5(pow_3(day_durbin_watson(Vwap)))` —— 更平滑的价格序列:是极值 / 极差特有,还是一般的日内变动。
6. `cross_max(day_durbin_watson(High), 20)` —— 硬最大值,不含幂次与 EMA。W 通道上硬极值输了(0.7738 对 1.1814),在 DW 通道上再判一次"软幂平均 vs 硬极值"。
7. `pow_3(pow_3(day_durbin_watson(High)))`(= `DW^9`)—— 幂次阶梯再往上一格。还涨 ⇒ 纯凸性;掉了 ⇒ 7.5 是在 train 上拟合出来的。
8. `pow_1_5(day_durbin_watson(High))`(= `DW^1.5`)—— 补阶梯低端(现在只有 1、3、7.5)。
9. `cross_stddev(pow_3(day_durbin_watson(High)), 60)` —— 把两个各自有效的聚合叠起来。
10. `div(pow_2_5(pow_3(day_durbin_watson(High))), pow_2_5(pow_3(day_std(Ret))))` —— 显式的"High 序列抖动相对普通波动的超出部分"。

挂 `cross_corr(pow_2(day_wmean(Ret, Ret)), pow_2(pow_2(day_wmean(Ret, Ret))), 241)`(1.7835):

11. **`cross_stddev(pow_2(day_wmean(Ret, Ret)), 241)`** —— 老实的未归一化写法(由 M-f,head 本来就约等于它的协方差近亲)。
12. **`div(cross_stddev(pow_2(day_wmean(Ret, Ret)), 241), cross_mean(pow_2(day_wmean(Ret, Ret)), 241))`** —— 真正归一化的变异系数。11 与 12 一起把"形状还是量纲"这件事判死:若 11 行、12 不行 ⇒ 量纲(§1.5 的修正成立);若 12 行 ⇒ 真有形状机制,而且换来一个可解释的 head。

挂 `cross_corr(pow_2(day_wmean(Ret, Ret)), pow_2(day_wmean(Ret, Ret)), 20)`(1.2106,自相关退化):

13. **`cross_stddev(pow_2(day_wmean(Ret, Ret)), 20)`** —— 解析上是同一个东西的老实写法,ρ 必然很高,门槛 1.3106,很可能直接替换掉一个退化 head。

挂 `cross_corr(pow_2(day_wmean(Ret, Ret)), pow_2(pow_2(cs_mask_top_replace_mean_neg(pow_2(day_wmean(Ret, Ret))))), 20)`(0.7071):

14. `cross_corr(pow_2(day_wmean(Ret, Ret)), pow_2(pow_2(pow_2(day_wmean(Ret, Ret)))), 20)` —— 去掉 mask 层、保留幂次深度。门槛只要 0.8071,便宜,直接判烂部件 #2。

挂 `cross_corr(pow_2(day_wmean(Ret, Low)), pow_2(day_wmean(Ret, Ret)), 20)`(0.6092):

15. `cross_corr(pow_2(day_mean(Ret)), pow_2(day_wmean(Ret, Ret)), 20)` —— 把 `Low` 权重换成等权(§1.3 说二者近似相等),验证烂部件 #5。门槛 0.7092。

说明:2~5、10 大概过不了"与原 head ρ ≥ 0.5"这一条,是**买证据**用的(和第 1 轮一样);1、11~15 是真有机会替换的。

### 4.3 N 的灵感

- **N-a(首选)把凸时间聚合搬到「活动的抖动」上**:`day_durbin_watson(Amt)`、`day_durbin_watson(Volume)`
  = `Σ(ΔAmt)²/ΣAmt²`,尺度无关,衡量分钟成交额曲线有多锯齿(爆发式成交 vs 平滑成交)。
  奖励的流动性控制只控了**水平**,没控**抖动**;这是一条全新的被观测量,
  而本种子三条通道已经证明"非负日内量 + 凸幂 + EMA(或滚动标准差)"这套聚合能把这类量变成 alpha。
  还可以给"价格抖动与成交抖动之比"(`div(day_durbin_watson(High), day_durbin_watson(Amt))`,一个日内的价格冲击代理)。
- **N-b 冻结报价状态的不稳定性**:`day_flat_ratio` 的水平被流动性控制吃掉,但它的**跨日波动**没有。
  第 1 轮那个 0.9972 的 head 里已经出现了 `day_flat_ratio(Ret)`,是个提示。注意 `day_zero_ratio` 的空对照上一轮 gate 失败(烂部件 #7)。
- **N-c 条件化的极端日加权**(只统计跳空日 / 贴近板宽日的日内抖动)—— 但 `LimitWidth` 已经两次被证伪(烂部件 #6),降权;
  这条更适合当核心 ② 的 E 外围,不值得单独一个 N 位。

**两个 GP 位怎么分配(我的排序,PI 决定)**:PLAN 的"3 轮至少 1 个 N"第 1 轮已满足,本轮两个位都给 E 是合法的。
① E(核心 ①)+ E(核心 ②) > ② E(核心 ①)+ N-a > ③ 其它。
理由:核心 ① 的家族控制最轻、外围最空、而且是唯一一条非幅度的信息;核心 ② 的共性最强但有波动代理风险;
N-a 虽然是一条真的新通道,但它要赌的"聚合层"已经被来源 ① 验证过,放到第 3 轮(等 R2~R5 的空对照结果出来)风险更小。

---

## 5. 文献题目(交文献员,≤4;只收 2023-08-08 之前发表的)

**L1 —— 对准核心 ②(`day_durbin_watson(High)` ≈ 分钟高价序列的每分钟已实现方差)**
问:文献里对**日内已实现方差 / 极差型(high-low)波动估计量**做过哪些处理?具体想要:
(a) 用最高价 / 最低价序列而不是收盘价序列估计日内波动的估计量族(Parkinson、Garman–Klass、Rogers–Satchell)有什么各自的信息内容差异;
(b) 把日度的已实现方差**聚合成一个月度截面信号**时都用过什么(均值、最大值、分位、指数加权、波动的波动);
(c) 在控制掉平均波动 / IVOL 之后,还剩什么被定价(极值部分、不对称的上下行已实现半方差);
(d) 在 A 股 / 有涨跌停的市场里这类量怎么被条件化(按流动性、规模、板块、上市年限分组)。
关键词(EN):realized variance; range-based volatility estimator; Parkinson / Garman-Klass / Rogers-Satchell; high-frequency intraday volatility;
realized semivariance; volatility of volatility; aggregation of daily realized measures; idiosyncratic volatility puzzle; China A-share low volatility anomaly。
关键词(中):已实现方差;极差波动率估计量;日内高频波动;已实现半方差;波动率的波动率;日度波动的月度聚合;特质波动率之谜;低波动异象;A 股。

**L2 —— 对准来源 ①(§1.1 的核心机制:非负日度量的「凸幂 + 指数加权」聚合,等价于偏向极端日的软幂平均)**
问:文献里讨论过**同一个日度风险 / 活动指标,换不同的跨日聚合方式会不会定价不同**吗?具体想要:
(a) MAX(月内最大日收益)相对 IVOL(均值型)的分解,以及把"最大值"换成"前 k 大的均值"、分位、幂平均时结论怎么变;
(b) 有没有文献明确比较"硬极值聚合"与"指数加权 / 幂平均这种软聚合"(含换手率与信号衰减的代价);
(c) 对日度观测取凸变换(平方、立方)再做时间平均,这个做法在哪些文献里出现过、是被当成设定选择还是被当成过拟合来源;
(d) 在 A 股上 MAX / 彩票偏好这一族的实证结论和窗口长度、加权方式的关系。
关键词(EN):MAX effect; lottery demand; extreme daily returns; aggregation choice; power mean; exponentially weighted moving average signal;
signal decay and turnover; top-k average; idiosyncratic volatility versus maximum; robustness to window length。
关键词(中):MAX 效应;彩票偏好;极端日度收益;聚合方式的选择;幂平均;指数加权移动平均;信号衰减与换手率;前 k 大均值;窗口长度稳健性;A 股。

**L3 —— 对准核心 ①(`pow_2(cross_mean(day_wmean(Ret, Ret), 5))`:成交 / 路径加权的日内漂移,先在 5 天上平均再折叠成幅度)**
问:文献里对**日内漂移 / 日内动量 / 成交量加权的日内收益**做过哪些处理?具体想要:
(a) 把日内漂移在**多日之间累加 / 平均**的做法(周内持续性、连续信息对跳跃式信息的区分,Frog-in-the-Pan 那一类);
(b) 什么时候用**带符号**的值、什么时候用**绝对值 / 平方**(折叠成幅度),文献里给的理由是什么;
(c) 用成交量 / 成交额 / 路径长度给分钟收益加权(VWAP 型、trade-weighted return)和等权平均相比多了什么信息;
(d) 日内漂移的持续性与隔夜收益、订单失衡持续性、知情交易的关系;A 股上的实证。
关键词(EN):intraday momentum; intraday drift; volume-weighted intraday return; trade-weighted return; continuous information versus jumps;
Frog in the Pan; order imbalance persistence; signed versus absolute return measures; overnight versus intraday returns; China A-share。
关键词(中):日内动量;日内漂移;成交量加权日内收益;连续信息与跳跃;路径依赖;订单失衡的持续性;带符号与取绝对值;隔夜与日内收益;A 股。

**L4 —— 对准 §1.3 / §1.5 的判读(日度风险指标在窗口内的离散度,以及它与"冻结报价 / 零变动分钟"的共动)**
问:文献里怎么度量和定价**一个日度波动 / 活动指标在一个窗口里的稳定性或离散度**?具体想要:
(a) 波动的波动、已实现方差的方差、日度波动的变异系数 —— 这些量是怎么构造的,和水平分开之后还有没有定价能力;
(b) 这类"离散度"指标该不该做归一化(除以均值 / 标准化),文献里给的做法与理由(我手上的证据提示未归一化版本和归一化版本可能结论相反);
(c) 零变动 / 报价不动的分钟或天数(Lesmond 型零收益率流动性度量、涨跌停封板与停牌)怎么被用作特征,
    以及它和波动 / 活动指标的**共动**(而不是水平)有没有被研究过;
(d) A 股涨跌停制度下这类度量的特殊处理。
关键词(EN):volatility of volatility; variance of realized variance; dispersion of daily volatility; coefficient of variation of volatility;
zero-return days; Lesmond zero-return illiquidity measure; proportion of zero returns; co-movement of volatility and illiquidity;
price limits and frozen quotes; China price limit hits。
关键词(中):波动率的波动;已实现方差的方差;日度波动的离散度;波动的变异系数;零收益率天数;零变动比例;流动性与波动的共动;
涨跌停与停牌;报价冻结;A 股涨跌停。
