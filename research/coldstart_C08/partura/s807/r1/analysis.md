# 结构解剖:种子 807,P 组,第 1 轮

快照 `c07s807M1_I0_open_search`,3 个 head,114 个归档候选,35 次拆解付费评估。之前没有任何轮次(`missions_before: []`,没有 notebook.md)。

---

## 0. 先摆算子事实(后面每条结论都靠它们)

下面每一条都从源码读出来,并且都有 `loc.json` 里的数字对上。**不读这一节,整份拆解表会被完全误读。**

| # | 事实 | 源码 | 实测吻合 |
|---|---|---|---|
| F1 | `cs_median(x)` / `cs_mean(x)` 返回 `med.unsqueeze(-1).expand_as(x)` —— **每日一个标量,横截面零变化**,而且**抹掉 NaN 掩码**(原本缺失的列也被填满) | `operators/nd_cs.py:107,134` | `cs_median(day_pos_ratio(Open))` 的 `distinct` = 0.0003 ≈ 1/3800 |
| F2 | `day_pos_ratio(x)` = 有限分钟里 `x > 0` 的比例。**`Open` 是后复权价,恒 > 0** ⇒ `day_pos_ratio(Open)` **≡ 1.0**(全日无数据时为 NaN) | `partura/ops_ext.py:98` | 见下面三条独立证据 |
| F3 | `rolling_ols(x, y, d)` 拟合的是 `y ~ alpha + beta*x`,所以 `cross_regbeta(A, B, d)` / `ts_regbeta(A, B, d)` 的**第一个参数是自变量**,输出 `cov_d(A,B) / var_d(A)`。`beta` 对自变量**加常数完全不变** | `operators/common.py:636-676`;`dt_cross.py:299`;`nd_ts.py:273` | — |
| F4 | `beta = where(var_x > EPS, cov/var_x, NaN)`,`EPS = 1e-9` ⇒ 自变量在窗口内恒定的股票直接变 NaN | `common.py:43,656` | head 1 敲掉 `add(...)` 后 `coverage` = 0.0 |
| F5 | `cs_bucket_demean(y, x)` = y 减去「x 的同一十分位桶内 y 的均值」⇒ **y 里任何横截面常数的加项被精确抹掉** | `ops_ext.py:463` | 见 §1.1 |
| F6 | `_pct_rank` 是 `argsort(argsort(stable))` 的**序数**排名,并列按**股票列序**打破 | `ops_ext.py:231` | — |
| F7 | `LimitWidth` ∈ {0.10, 0.20, 0.30},只看代码前缀 + 日期(创业板 **2020-08-24** 起 0.20,科创板 2019-07 起 0.20,北交所 0.30) | `alphacube/tradability.py:18-30` | — |
| F8 | ⇒ `cs_median(LimitWidth)` **≡ 0.10**(10% 板占过半),`signedpower(cs_median(LimitWidth))` **≡ 0.01**:两个**字面常数** | F1 + F7 | 共性表里它们分别在 39 / 30 个候选里,p 0.097 / 0.476 |
| F9 | `pow_05` 是带符号开方,在 `MONOTONE_ANY` 里;奖励**先按日排名再 EMA**(`signal_input` / `rank_first`) ⇒ 单调包装是**精确 no-op** | `partura/steer.py:179,409,639` | `pow_05` 必要性 −0.00 |
| F10 | 5 个控制的确切写法:`liq = cross_mean(day_sum(Amt), 30)`、`n_vol = cross_mean(day_std(Ret), 20)`、`n_rev = div(day_last(Close), ts_delay(day_last(Close), 20))`、`known = cross_mean(day_std(Amt), 30)`、`n_size = LogFloatCap`,加各自排名的平方、三次方 | `scripts/c05_locate.py:117-119,128` | — |
| F11 | ⇒ 波动控制是**分钟内**收益波动,不是日频波动;**价格水平本身不是控制**,`LogFloatShares` 也不是,而 `log(price) = LogFloatCap − LogFloatShares` | F10 + 规则 §1 的叶子清单 | — |
| F12 | 方向与半衰期**只在 train 上挑**(±1 × {0,5,20}),score = min(train, valid) 纯多头夏普 | `steer.py:609,653-667` | 拆解表里 hl 在 0/5/20 之间跳 |
| F13 | `long_neutral` 这一档**不套 untradable 掩码**(掩码只对 `long_tradable`/`long_bucket`/`long_marginal` 生效)⇒ 冻结、次新也能进书 | `steer.py:648` | — |
| F14 | 成本 15 bp/边、换手上限 0.30、top 10% ⇒ **每天重排的噪声信号会拿到 −3 以下**,而不是 0 | `partura/diagnose.py:73-75` | 所有 sufficiency 行都是 −0.7 ~ −3.67 |
| F15 | 门槛 = `coverage ≥ 0.9 且 distinct ≥ 0.5`;`distinct` = 每日(不同取值数 / 有值股票数)的中位数 | `c05_locate.py:163`;`diagnose.py:136` | — |

**F2 的三条独立证据**(这是整份分析的支点,所以列全):

1. head 2 敲掉 `cs_median` 后,`cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add(day_pos_ratio(Open), ts_var(LogFloatCap, 30)), LimitWidth), 30)` 的 score / train / valid = **0.7927 / 0.7927 / 1.3171**,与原 head 的 0.792684 / 0.792684 / 1.317086 **逐位相同**,必要性 −0.00。若 `day_pos_ratio(Open)` 有逐股变化,它(量级 ~0.2–1)会把 `ts_var(LogFloatCap, 30)`(量级 ~1e-2)彻底压住,不可能一位不差。
2. head 1、head 2 的 `Open->Close` 互换也**逐位相同**(head 1 变体 1.1057 / 0.9125 对 head 的 1.105685 / 0.912461)。
3. head 1 敲掉 `add(...)` 后整张面板 `coverage` = **0.0**:`ts_regbeta` 的自变量退化成常数,`var_x > EPS` 处处不成立(F4),全 NaN。这同时说明 `cs_median(day_pos_ratio(Open))` 在**时间上也是常数**,即它就是常数 1.0。

---

## 1. alpha 的来源

### 1.1 三个 head 的精确化简

把 F2 / F3 / F5 代进去(**这些是恒等变形,不是近似**):

- **head 2** `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 30)), LimitWidth), 30)`
  ≡ `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(ts_var(LogFloatCap, 30), LimitWidth), 30)`
  (`cs_median(day_pos_ratio(Open))` ≡ 1.0,桶内去均值把常数加项精确抹掉)

- **head 3** `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add(cs_median(ts_var(LogFloatCap, 50)), ts_var(LogFloatCap, 20)), LimitWidth), 30)`
  ≡ `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(ts_var(LogFloatCap, 20), LimitWidth), 30)`
  (`cs_median(ts_var(LogFloatCap, 50))` 是横截面常数,同样被抹掉)

- **head 1** `cross_regbeta(day_quantile_q75(Volume), cs_rank(pow_05(ts_regbeta(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 20)), cs_mean(day_median(Close)), 5))), 241)`
  ≡ `cross_regbeta(day_quantile_q75(Volume), cs_rank(ts_regbeta(ts_var(LogFloatCap, 20), cs_mean(day_median(Close)), 5)), 241)`
  (自变量加常数不改 beta;`pow_05` 必要性 −0.00;`cs_rank` 必要性 −0.02)

**⇒ head 2 和 head 3 是同一个式子,只差 `ts_var` 的窗口(30 对 20)。** 它们之所以都进了库、没被骨架禁令和 ρ ≥ 0.7 禁令拦住,只是因为那个**死的 `add(cs_median(...), ...)` 外壳**长得不一样(一个包 `day_pos_ratio`,一个包 `ts_var`)。

> **给 PI / 审计员的可核对预测**:相关度表里 `ρ(head2, head3)` 应当偏高(两者只差 ts_var 窗口;半衰期 20 对 5 会压低一些,我押 0.6–0.85)。如果确实 ≥ 0.7,那么**快照的 3 个 head 实际上只有 2 个独立想法**,不要为这一个想法花掉 2 个 E 位。

化简还被两处数字独立验证:

- head 3 敲掉 `ts_var(LogFloatCap, 50)` 得到 `cs_bucket_demean(add(cs_median(LogFloatCap), ts_var(LogFloatCap, 20)), LimitWidth)`,score / train / valid / hl = 0.5138 / 0.8404 / 0.5138 / 5,与原 head 的 0.5209 / 0.8369 / 0.5209 / 5 基本重合(必要性 +0.01)—— 正是「两个加项都是横截面常数、桶内去均值后同一张面板」的预测结果。
- head 3 敲掉整个 `add(...)` 得到 `cs_bucket_demean(cs_median(ts_var(LogFloatCap, 50)), LimitWidth)`:数学上恒 0,但 float32 下 `mu = sum/n` 有 ~1e-7 相对舍入,残差 ~1e-9,再除以逐股不同的 `var_x`,得到一张**纯舍入噪声**的连续面板 —— `distinct` 0.9997、**过了门槛**、score −0.13。对照 head 2 同位置的 `cs_bucket_demean(cs_median(day_pos_ratio(Open)), LimitWidth)`:1.0 在 float32 里精确可表示,n 个 1.0 求和除以 n 精确得 1.0,残差精确为 0 ⇒ `distinct` 0.0003、被挡。**两种情形的差别完全按浮点算术预测**,这反过来把 F2 钉死。

> **写进已知陷阱**:`cs_bucket_demean(<横截面常数>, ·)` 产出的是 float32 舍入残渣而不是 0,**distinct ≥ 0.5 的门槛挡不住它**。本轮任何这种形状的变体都应当直接划掉。

### 1.2 真来源:`ts_var(LogFloatCap, d)`

这是三个 head 里**唯一「拿掉就塌」的部件**。

| 证据 | 数字 |
|---|---|
| 共性 | `ts_var(LogFloatCap, 20)` 在 **48 / 114** 个候选里,均值差 **+0.75**,p **0.0005**(含 −0.54 / 不含 −1.29)。`ts_var(LogFloatCap, 40)` 均值差 +1.07、p 0.0038 但**只有 6 个候选**;`ts_var(LogFloatCap, 50)` +0.48、p 0.058、16 个。**只有 20 这一档同时有量和显著性** |
| 必要性 | head 2 敲掉 `ts_var(LogFloatCap, 30)`(换成裸 `LogFloatCap`):0.79 → **−0.55**,必要性 **+1.34**;head 3 敲掉整个 `add(...)`:必要性 **+0.65**;head 1 敲掉 `ts_regbeta(...)`:必要性 **+2.90**(全文件最大) |
| 充分性 | 单独当因子很差:`add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 20))` ≡ `ts_var(LogFloatCap,20)` 得 −2.71;`cs_bucket_demean(...)` 得 −0.72 / −0.86。按 F14,这是**换手成本**而不是「没信息」—— 它要外层的长窗口回归去平滑才能用 |
| 敏感性 | 窗口 20 / 30 对应 head 分 0.52 / 0.79;把 head 3 的 var20 换成「var50 + var20 混合」**+0.24**。有影响,不是悬崖 |

**它到底是什么**:`LogFloatCap = log(价格 × 流通股本)`(`FloatCap` 随价格每日变动,见 `tests/test_panels_daily.py:44`),所以 `ts_var(LogFloatCap, d)` 是 log 市值**水平**在 d 天内的方差,**不是收益方差**。对近似随机游走:

```
ts_var(LogFloatCap, d) ≈ 日频收益方差 × d/6  +  (d 日累计 log 变动)²/12  +  流通股本变动(解禁 / 定增)的跳跃²
```

对照 F10 / F11 的控制:波动控制是**分钟内**收益波动,反转控制是带符号的 20 日价格比(它的排名平方 / 三次方已经吸收掉大部分 |20 日涨跌幅|),市值控制是 `LogFloatCap` 的**水平**。**残下来、最可能承载 alpha 的是两块:**

- **(a) 日频(含隔夜跳空)已实现方差里不被分钟内波动张成的那部分** —— 即隔夜 / 低频的那一截波动;
- **(b) 流通股本变动事件**(解禁、定增)带来的 log 市值跳跃 —— 这一块**完全没有控制**,而且 `LogFloatShares` 是现成叶子,可以直接把它分离出来。

按规则 §4 逐条过:不是前视(全是当日及以前的日频字段);不是数值伪影(`ts_var` 非负、量级 ~1e-2,没有近零除法);不是定义坏掉(coverage 0.999)。**判为真来源候选**,但它现在是 (a) 和 (b) 的混合体,分不开 —— 分开它就是本轮 R / N 的主要任务。

### 1.3 半真半代理:`cs_bucket_demean(·, LimitWidth)`

必要性 head 2 **+0.44**、head 3 **+0.33**(拿掉它、直接把 ts_var 当 Y,分数掉到 0.35 / 0.19)。有贡献,但量级只有 `ts_var` 的四分之一到三分之一。

按 F6 / F7 / F8,它实际做的事不是「按限幅分组」:`LimitWidth` 只有 2–3 个取值,十分位桶的边界落在巨大的并列块**内部**,靠股票列序切开,所以桶 = **板块 × 代码连续片段**。而且含义在样本内**随时间变**:

- 2018-01 ~ 2019-07(科创板之前):`LimitWidth` 近乎全场 0.10 ⇒ 桶**纯粹是代码片段**,零限幅信息;
- 2019-07 ~ 2020-08-24:10% 板 + 一小撮科创板;
- 2020-08-24 之后(含**整个 valid 段**):约三分之一是 20% 板 ⇒ 这才是真正的板块切分。

规则 §4 明说「并列靠股票列序打破 …… 携带的是板块信息」,**不是陷阱**;所以这是合法的分组相对波动(「我的 d 日市值方差 vs 同板块、代码相邻的一批同类」),机制也讲得通(组内相对比绝对稳)。但**分组字段选得很差**,这是最值得换部件的地方 —— 现成的 `BoardCode`(真板块标签)、`LogFloatCap`(规模分组,波动本来就随规模变)都更干净。

### 1.4 主要是代理:外层 `cross_regbeta(day_quantile_q75(Volume), Y, d)`

按 F3,它是 `cov_d(X, Y) / var_d(X)`,`X = day_quantile_q75(Volume)` = q75 分钟**股数**成交量。写开:

```
beta_i = corr_i × sd(Y_i) / sd(X_i)
```

`Y` 是桶内去均值的 `ts_var` 或一个排名,`sd(Y_i)` 在股票之间量级接近;而 `sd(X_i)` 跨 **3–4 个数量级**。所以 beta 的横截面排序由 **`sign(corr_i)` 和 `1 / sd_d(q75 Volume)`** 共同决定:**最正和最负两端都被 `sd(X)` 最小的股票占据**,也就是成交量最不活跃、最不变动的那批。十分位纯多头书(方向由 train 挑,F12)因此是一张**低成交量离散度的书**,再配合 F13(这一档不剔除冻结 / 次新),集中度风险是真实的。

再按 F11:`sd(q75 Volume) ≈ sd(q75 Amt) / 价格`,而流动性控制用的是**金额** `cross_mean(day_sum(Amt), 30)`。所以股数口径相对控制**多出来的正是后复权价格水平** —— 它不是控制,它在股票之间的排序 ≈ 自基期以来的累计收益(规则 §4 明说这是长周期动量 / 反转,不是陷阱),而且在 `LogFloatCap` 被控制住之后,价格水平等价于 **−`LogFloatShares`**(小股本),后者也不是控制。

**⇒ 外层回归最可能的真实身份是「(低成交量离散度 × 价格水平 / 小股本) × 协动方向」,而不是「与自身成交量的关联度」。** 支持它的证据:

- `day_quantile_q75(Volume)` 单独当因子 `distinct` **0.3566**、被门槛挡掉(分钟股数按手取整,大量并列);它在 114 个候选里**从来没有以别的身份出现过**(共性表里唯一另一条含它的是 `cross_regbeta(day_quantile_q75(Volume), LogFloatShares, 241)`,均值差 **−0.24**、n=4、p 0.73)。
- `Volume->Amt` 互换(= 把价格那一份去掉):head 3 **+0.59**(0.52→1.11,valid 0.52→**3.06**)、head 2 +0.04(valid 1.32→2.20)、head 1 **−0.27**。两个 sign +1 的 head 明显变好,唯一变差的是内层本身是废料的 head 1。⇒ **价格那一份在 +1 方向上是拖累而不是来源**;真正剩下的候选是 `1/sd(q75 Amt)`(金额离散度倒数,相对流动性控制仍有残余)与协动方向本身。
- 窗口方向一致:head 2 / head 3 外层 30→60 都涨到 ~1.02(+0.23 / +0.50),30→15 都变差(head 2 掉到 **0.03**);head 1 的 241→120 轻微变差(0.83)、→482 塌到 **0.33**。偏好更长的平滑,但不是越长越好 —— 说明外层不只是在降换手。

**这一条必须用对照钉死,别猜**:把外层换成尺度无关的 `cross_corr` 就把两件事分开了 —— 若分数基本保住,来源是**协动**;若塌掉,来源是 `1/sd(X)` 这个**尺度因子**(即流动性 / 价格的残余)。两种答案对第 2、3 轮都值钱。见 §4 的 R-D。

### 1.5 判为纯代理、不要当核心的东西

- **`cs_median(day_pos_ratio(Open))` / `day_pos_ratio(Open)`**:共性表两行数字完全相同(均值差 +0.86、p 0.0003、各 60 个候选),说明归档里 `day_pos_ratio(Open)` **从来没有裸用过,全被 `cs_median` 包着**。而按 F2 它 ≡ 1.0。所以这条 +0.86 的「共性」**全部是血缘代理**:60 个候选都是同一支系。核心卡第 5、6 位应当直接划掉。
- **`cs_median(LimitWidth)`(39 个候选,+0.46)、`signedpower(cs_median(LimitWidth))`(30 个,+0.19)**:按 F8 是**字面常数 0.10 / 0.01**。常数不可能携带信息,这两行也是血缘代理。凡是把它们当分桶字段或乘子的写法(如共性表里的 `cs_bucket_demean(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 20)), signedpower(cs_median(LimitWidth)))`,6 个候选、p **0.53**)等于「按 10 个代码连续片段去均值」,零限幅信息。
- **`cs_mean(day_median(Close))`(5 个候选,均值差 +1.33,p 0.001,核心卡第 1 位)**:按 F1 是**每日一个标量** —— 全市场等权价格指数水平。n=5 且只有 head 1 含它 ⇒ **单一支系**,+1.33 是血缘而不是共性。它在 head 1 里是 `ts_regbeta` 的**因变量**,所以不是死重(见下),但**绝不能当 E 的核心**:固定住它,GP 只能在一个每日标量外面长。
- **`ts_var(LogFloatCap, 40)`(+1.07)、`day_median(Close)`(+0.38)、`day_skew(Open)`(+0.25)**:n = 6 / 7 / 5,都是支系级样本。`day_skew(Open)` 还是后复权价**水平**的日内偏度,基本是价格路径形状,和价格水平高度纠缠。

### 1.6 head 1 的内层单独说一句

化简后内层是 `ts_regbeta(ts_var(LogFloatCap, 20), cs_mean(day_median(Close)), 5)` = `cov_5(v_i, B) / var_5(v_i)`,其中 `v_i` = 我的 20 日 log 市值方差,`B` = 全市场等权价格指数(横截面常数、逐日变)。即:**最近 5 天里,市场指数对我自己的市值方差的回归斜率**。

分母 `var_5(v_i)` 是「20 日滚动方差」在 5 天内的方差 —— **「波动的波动」,量级 ~1e-6,很容易接近 0**。这正是它 `coverage` 只有 **0.9555**(全文件最低,其余都是 0.998–0.999)的原因:约 4.5% 的股票因 `var_x ≤ EPS` 被判 NaN(F4)。横截面排序因此很大程度由 `1 / var_5(ts_var(LogFloatCap, 20))` 支配,也就是「我的 20 日市值方差这一周有多稳」,符号由与指数的协动给出。

这离规则 §4 的「除以近零的量造成的爆点支配了截面」只有一步之遥,**但我判定它不构成挡的理由**:量级估算下 `var_5(v_i)` 典型值 ~1e-6,比 `EPS = 1e-9` 高三个数量级,爆点不是主导,而是尾部;且面板先按日排名(F9),爆点只表现为「排在两端」,不会放大。真正的问题是**它讲不出机制、且是三个 head 里最不稳的**(241→482 塌到 0.33,Volume→Amt 是三个 head 里唯一变差的)。**结论:head 1 不值得花 E 位。**

---

## 2. 烂部件(适合做 R)

| # | 部件 | 所在 | 证据 | 判断 |
|---|---|---|---|---|
| 1 | `cs_median(ts_var(LogFloatCap, 50))` | head 3 | 必要性 **−0.24**(拿掉 → 0.7576,`rho_head` 0.5338) | **最干净的一条**。它是横截面常数(F1),被桶内去均值精确抹掉(F5);唯一的作用就是把本来有用的 `ts_var(LogFloatCap, 50)` 加项**藏在 `cs_median` 里废掉**。拿掉 `cs_median` 后 var50 真正参与,+0.24 |
| 2 | `ts_var(LogFloatCap, 50)` | head 3 | 必要性 **+0.01** | 不是说 var50 没用,是说**被 `cs_median` 包住后**它和任何别的横截面常数(`cs_median(LogFloatCap)`)等价。与第 1 条是同一件事的两面 |
| 3 | `add(cs_median(day_pos_ratio(Open)), ·)` | head 1、head 2 | 必要性 **−0.00**,且 `Open->Close` 逐位相同 | **6 个节点的精确死重**(F2 + F3 + F5)。不止不涨分 —— 它会让 GP 在死分支里一直变异,也是 head 2 / head 3 绕过库禁令的原因 |
| 4 | `pow_05(...)` | head 1 | 必要性 **−0.00** | 精确 no-op(F9)。纯死重 |
| 5 | `cs_rank(...)` | head 1 | 必要性 **−0.02**(0.9125 → 0.9315) | 只影响进入外层回归的尺度。可去,但增益 0.019 < R 的 +0.1 门槛 |
| 6 | 外层窗口 `30` | head 2、head 3 | 30→60:**+0.23 / +0.50**;30→15:−0.76 / +0.08 | 30 偏短 |
| 7 | `Volume` 口径 | head 2、head 3 | →Amt:**+0.04 / +0.59** | 股数口径既带着价格水平(§1.4),又按手取整(`distinct` 0.356)。head 1 是唯一反例(−0.27) |
| 8 | `cs_median(LimitWidth)` / `signedpower(cs_median(LimitWidth))` | 不在 head 里,但在 **39 / 30** 个归档候选里 | ≡ 0.10 / 0.01(F8) | 凡是把它当分桶字段或乘子的写法一律划掉 |

**现有 4 个 R 候选的归属**(我按规则 §2 核对了 `rho_head`):4 个的 `rho_head` 都 ≥ 0.5(0.7624 / 0.7410 / 0.5338 / 0.5481),`rho_known` 都在 −0.04 ~ −0.16,所以**全部走「替换」而不是「收录」**。每个 head 只能被最好的那个替换:

- head 3 ← `cross_regbeta(day_quantile_q75(Amt), cs_bucket_demean(add(cs_median(ts_var(LogFloatCap, 50)), ts_var(LogFloatCap, 20)), LimitWidth), 30)`,score 1.1126(增益 +0.59)
- head 2 ← `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 30)), LimitWidth), 60)`,score 1.0191(增益 +0.23)
- head 1:**没有** R 候选(最好的是 `cs_rank` 敲除,增益 0.019)

**注意**:若替换后 head 2 / head 3 都往「`day_quantile_q75(Amt)` + 窗口 60」靠,两者的 ρ 会更高,很可能触发「同一个东西」的判断。建议 PI 让这两条走**不同方向**(一条换口径,一条换分桶字段),别同时收敛。

---

## 3. 之前的任务

**第 1 轮,没有任何前置记录**:`missions_before` 为空,目录下没有 `missions_final.yaml` / `audit_record.json` / `R_prev.json` / `notebook.md`,`replacements_in_force: 0`。所以:

- **E**:还没有试过任何核心,没有产出 heads。
- **N**:还没有跑过。规则 §2 要求「3 轮里至少 1 个 N 位通过审计」—— 本轮 2 个任务位里**最好先放 1 个 N**,不要把这个硬约束压到第 3 轮。
- **R**:还没有替换与收录(`replacements_in_force: 0`);快照里 3 个 head 全部来自 M 的第 1 批 `c07s807M1_I0_open_search`。
- **审计员**:还没挡过任何东西。
- **上一轮笔记的预测**:无可核对。我在 §1.1 和 §4.4 留了本轮可核对的预测,供第 2 轮回看。

---

## 4. 本轮候选

### 4.1 值得深挖的核心(≤ 3)

规则 §2 要求核心是快照里某个 head 的子树,或定位输出共性表 / 核心卡里的子树。下面三个都在核心卡里,**按写法原样引用**(括号里注明化简后的实质)。

**核心 A(首选)—— 核心卡第 4 位**
`cs_bucket_demean(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 20)), LimitWidth)`
均值差 +0.87、p 0.0137、9 个候选。实质 ≡ `cs_bucket_demean(ts_var(LogFloatCap, 20), LimitWidth)`,即 §1.2 的真来源 + §1.3 的分组相对化,**把 §1.4 那个主要是代理的外层整个留在外面给 GP 长**。这是本轮性价比最高的核心。
*已见过的外围写法*(务必避开,规则 §2 要求外围不得与已见过的含该核心的候选相同):`cross_regbeta(day_quantile_q75(Volume), ·, {15, 30, 60})`、`cross_regbeta(day_quantile_q75(Amt), ·, 30)`;分桶字段的孪生 `cs_bucket_demean(add(...), signedpower(cs_median(LimitWidth)))`(6 个候选,p 0.53)。
*未探过的方向*:把它当 `cross_corr` / `cross_reg_tvalue` 的一边;对它自己的历史取相对位置(`cross_rank`、`cross_quantile_q75`、`div` 到自身均值);和 `ts_var(LogFloatCap, 50)` 的**比值**而不是和;`cs_bucket_demean` 之后再叠一层时序平滑而不是回归。
*审计风险*:E 位要求核心与每个控制 |ρ| < 0.8。核心 A 是桶内去均值的 20 日市值方差,和波动控制 `cross_mean(day_std(Ret), 20)` 最可能高 —— 但一个是**日频水平方差**、一个是**分钟内收益波动**,又经过桶内去均值,我估 0.4–0.7,应当能过。这是本轮唯一需要盯的核心 ρ。

**核心 B —— 核心卡第 7 位**
`ts_var(LogFloatCap, 20)`
均值差 +0.75、p **0.0005**、**48 个候选**(量和显著性都最好)。深度 2,外面空间最大,能让 GP 找到一台**和 `cross_regbeta(q75Vol, ·)` 完全不同的机器** —— 这正是我在 §1.4 想摆脱的那台。
*已见过的外围写法*:`add(cs_median(day_pos_ratio(Open)), ·)`(≡ 恒等)、`add(cs_median(ts_var(LogFloatCap, 50)), ·)`(≡ 恒等)、`add(ts_var(LogFloatCap, 50), ·)`、`cs_bucket_demean(·, LimitWidth)`、`cs_bucket_demean(·, signedpower(cs_median(LimitWidth)))`、`ts_regbeta(·, cs_mean(day_median(Close)), 5)`、`cs_rank` / `pow_05` 包装,以及外层 `cross_regbeta(day_quantile_q75(Volume), ·, {15, 30, 60, 120, 241, 482})`。
*注意*:这个核心和核心 A 是包含关系。规则说「每个核心整个实验至多 2 个 E 位」,A 和 B 算两个核心,但同一轮同时上会让两个 E 位高度重叠。**建议本轮只上 A 或只上 B,另一位给 N。**

**核心 C(备选,我不推荐本轮用)—— 核心卡第 2 位**
`day_quantile_q75(Volume)`
均值差 +1.11、p 0.000、**66 个候选**(n 最大)。看着最诱人,但 §1.4 的证据说它主要是「低成交量离散度 × 价格水平」的代理;它单独当因子 `distinct` 0.3566 直接被门槛挡;而且它在 114 个候选里**只以 `cross_regbeta` 自变量这一个身份出现过**。
*审计风险最高*:它要和流动性控制 `cross_mean(day_sum(Amt), 30)` 比 |ρ| < 0.8。q75 分钟股数 vs 30 日日均金额,秩相关很可能在 0.7–0.85 —— **本轮最可能被 E 的核心 ρ 卡死的就是它**。若 PI 仍想用,请准备 A 或 B 作为回退。

### 4.2 R 目标(至多 16 个变体)

先把已有的 4 个按 §2 的归属提交(head 3 取 Amt 那条、head 2 取窗口 60 那条),再加下面几组。全部是「去掉或替换快照里某个 head 的部件」,符合规则 §2 的 R 定义。

- **R-A 两处好处叠加**(head 3):`cross_regbeta(day_quantile_q75(Amt), cs_bucket_demean(add(cs_median(ts_var(LogFloatCap, 50)), ts_var(LogFloatCap, 20)), LimitWidth), 60)` —— Amt(+0.59)和窗口 60(+0.50)是两个独立的单改,叠加是最明显的一步。head 2 的同款:同式把 `ts_var(LogFloatCap, 20)` 换成 `30`、`day_quantile_q75(Amt)`、窗口 `60`。
- **R-B 把被 `cs_median` 废掉的 var50 放出来**(head 3):`cross_regbeta(day_quantile_q75(Amt), cs_bucket_demean(add(ts_var(LogFloatCap, 50), ts_var(LogFloatCap, 20)), LimitWidth), 60)` —— 第 1 条烂部件 + 两处好处一起。
- **R-C 换分桶字段**(head 2、head 3):把 `LimitWidth` 换成 `BoardCode`(真板块标签,不靠列序切片)、换成 `LogFloatCap`(规模分组 —— 波动本来就随规模变,而且控制去掉的是**最终信号**对 LogFloatCap 的暴露,不是桶内条件化,所以不是重复控制)、换成 `LogFloatShares`。直接检验 §1.3:那 +0.44 / +0.33 是板块信息还是代码片段。
- **R-D 尺度无关的外层**(head 2、head 3)**—— 本轮最有诊断价值的一条**:把 `cross_regbeta` 换成 `cross_corr`(以及中间档 `cross_reg_tvalue`),例如 `cross_corr(day_quantile_q75(Amt), cs_bucket_demean(add(cs_median(ts_var(LogFloatCap, 50)), ts_var(LogFloatCap, 20)), LimitWidth), 60)`。保住分数 ⇒ 来源是**协动**;塌掉 ⇒ 来源是 `1/sd(X)` 这个**尺度因子**。两种答案都直接决定第 2、3 轮怎么走。(`cross_corr` 不在禁用算子里 —— 禁的只有 `ts_spearman` 和全部 `nt_*`。)
- **R-E `ts_var` 的窗口与口径**(head 2、head 3):窗口扫 `20 / 30 / 40 / 50`(共性表给 40 的均值差最高 +1.07,但只有 6 个候选,值得一次便宜的验证);**口径分离** —— 把 `ts_var(LogFloatCap, d)` 换成 `ts_var(LogFloatShares, d)`(只剩解禁 / 定增的股本跳跃)和 `ts_var(LogTotalCap, d)`。这是把 §1.2 的 (a) 日频方差和 (b) 股本事件**分开的最便宜办法**。
- **不要提交的**:head 2 / head 3 的**精确化简式**(`cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(ts_var(LogFloatCap, 30), LimitWidth), 30)` 之类)。它们和原 head 的 ρ = 1.0,既达不到 +0.1 的门槛,又会被库禁令拒绝。它们的价值是当 **E 的核心**(核心 A 已经把它包进去了),不是当 R。

### 4.3 N 的灵感

- **N1 相对波动,而不是绝对波动**:`cs_median` / `cs_mean` 在 `add` 里是精确死重(§2 第 3 条),但当**除数**时就活了。`div(ts_var(LogFloatCap, 20), cs_median(ts_var(LogFloatCap, 20)))` = 我的市值方差 / 全市场中位市值方差 —— 尺度无关、不会被任何去均值抹掉,而且 GP 在 head 3 里已经把 `cs_median(ts_var(LogFloatCap, 50))` 拿到手上了,只是用错了算子(用了 `add`)。**这是把本轮最大的死重直接翻成一个新想法。**
- **N2 把 (a) 和 (b) 拆开**:围绕 `ts_var(LogFloatShares, d)`(纯股本事件:解禁、定增)和「日频方差净掉分钟内波动」这两件事各建一支。后者的写法例如 `div(ts_var(LogFloatCap, 20), cross_mean(day_std(Ret), 20))` 这一类「低频 / 高频波动比」—— 分子分母都在手上,而控制只有分母。
- **N3 分组相对化,但分组字段选对**:以 `BoardCode` 或 `LogFloatCap` 为桶,做「组内相对波动 / 相对换手」,替掉 `LimitWidth` 这个 2–3 取值、靠列序切片、含义随时间变的字段。
- **N4 把 q75 成交量变成一个真正的特征**:它在 114 个候选里只当过回归自变量。`div(day_quantile_q75(Amt), day_quantile_q25(Amt))`(日内成交金额的分布宽度)、`div(day_quantile_q75(Amt), cross_mean(day_quantile_q75(Amt), 30))`(相对成交强度)都是尺度无关、和金额流动性控制不同的东西。

### 4.4 本轮可核对的预测(给第 2 轮回看)

1. `ρ(head2, head3)` ≥ 0.6(我押 0.6–0.85);若 ≥ 0.7,快照的 3 个 head 实际只有 2 个独立想法。
2. R-D(`cross_corr` 版)会**明显低于** `cross_regbeta` 版 —— 即 §1.4 的尺度因子是外层分数的主要来源。(信心中等:60%。)
3. R-C 里 `BoardCode` 版 ≥ `LimitWidth` 版,`LogFloatCap` 版最好 —— 分组相对化的价值在「同规模同类」而不在「同限幅」。
4. R-E 里 `ts_var(LogFloatShares, d)` 单独**达不到** 0.5 的发现门槛(股本事件太稀疏),但它和 `ts_var(LogFloatCap, d)` 的 ρ 会很低(< 0.3),说明 §1.2 的 (a) 才是主体。
5. 若核心 C(`day_quantile_q75(Volume)`)被提交,它与流动性控制的 |ρ| 落在 0.7–0.85,有真实概率被 E 位的 |ρ| < 0.8 卡掉。

---

## 5. 文献题目(给文献员)

**L1 —— 对准核心 A / 核心 B 的「价格水平方差」口径**
文献里怎么处理**对数价格 / 市值「水平」在一个窗口内的方差**(而不是收益方差)?它混进去的漂移项(窗口内累计涨跌幅的平方)通常怎么被剥掉?日频已实现方差与日内分钟波动分别预测什么、两者之差(隔夜 / 低频那一截)有没有独立的横截面定价作用?
*关键词*:已实现方差 / 日内波动 与 隔夜波动 分解、价格水平方差 vs 收益方差、方差比检验、特质波动率异象、A 股 低波动异象、波动的波动;realized variance decomposition, overnight vs intraday volatility, variance of log price level, variance ratio test, idiosyncratic volatility anomaly, vol-of-vol, low-volatility anomaly China A-shares

**L2 —— 对准核心 A 的 `cs_bucket_demean(·, LimitWidth)` 与 N3**
把一个特征放在**同组同类里相对化**(分组去均值 / 分组排名)和做**截面回归残差**,文献上各有什么已知差别和坑?分组字段该用什么(行业、板块 / 交易所、规模、涨跌幅限制),当分组字段取值极少、靠并列次序切片时会发生什么?
*关键词*:板块中性化、行业中性化、分组去均值 与 回归残差、同业相对估值 / 相对波动、涨跌幅限制 板块差异、规模分组内相对指标;peer-group demeaning vs regression residual neutralization, industry/board neutralization, within-group relative volatility, characteristic-adjusted returns, price limit rules China, size-bucket conditioning

**L3 —— 对准 §1.4 和 R-D(最要紧的一题)**
把一个「滚动时序回归斜率」当横截面因子用,文献里怎么处理**斜率天生带着 1/sd(自变量) 这个尺度污染**的问题?相关系数、t 值、R²、标准化后的 beta 分别适合做什么?另外:个股特征与其**自身**成交量 / 换手的协动(混合分布假说一脉)文献上发现了什么?
*关键词*:滚动回归 beta 当因子、斜率 的 尺度污染、beta 与 相关系数 与 t 值 的取舍、成交量 与 波动 的协动、混合分布假说、量价协动;rolling beta as a cross-sectional signal, slope vs correlation vs t-statistic scaling, scale contamination in regression coefficients, volume-volatility co-movement, mixture of distributions hypothesis, turnover-volatility comovement

**L4 —— 对准 N2(b) 的股本事件那一支**
流通股本的变动本身能不能预测收益?限售解禁、定增 / 再融资、股份回购、股权质押导致的流通股本跳跃,在 A 股文献里各有什么已知的事件效应和时间窗口?把它写成一个连续的横截面因子(而不是事件研究)有哪些现成做法?
*关键词*:限售股解禁、定向增发、流通股本变动、股份回购、股权质押、流通市值 跳跃、事件驱动因子化;lockup expiration, share unlock, seasoned equity offering (SEO), secondary offering, share repurchase, free-float changes, index free-float adjustment, event-driven factor construction China A-shares

---

## 附:给 PI 和审计员的三条硬提醒

1. **凡是出现 `cs_median(...)` / `cs_mean(...)` 的提议,先确认它不是死重。** 它是每日一个标量(F1)。作为 `add` 的加项,在 `cs_bucket_demean`、`cs_demean` 里、或作为回归自变量的一部分时(F3),它是**精确 no-op**;作为除数、或作为 `ts_*` 回归的因变量时才有作用。
2. **`cs_bucket_demean(<横截面常数>, ·)` 过得了 `distinct ≥ 0.5` 的门槛**,但产出的是 float32 舍入残渣(本轮实测 `distinct` 0.9997、score −0.13)。这种形状应当按规则 §4「数值伪影 / 面板几乎是常数」划掉。
3. **`day_pos_ratio` 只对 `Ret` 之类可正可负的量有意义。** 作用在 `Open`/`Close`/`High`/`Low`/`Vwap`/`Amt`/`Volume` 这些非负叶子上,它退化成一个「当日有无数据」的指示器(价格恒 ≡ 1.0)。本轮 60 个归档候选、核心卡的第 5、6 位都踩在这上面。
