# 结构解剖:种子 807,B 组,第 3 轮(最后一轮)

读入:`r3/loc.md`、`r3/loc.json`、`r3/R_prev.json`(第 2 轮 R 的结果)、`r2/loc.md`、`r2/loc.json`、`r2/R_prev.json`(第 1 轮 R 的结果)、
`r2/analysis.md`、`r2/lit.md`、`r2/missions.yaml`、`r1/*`、`notebook.md`、PLAN.md(含全部 11 条修订),
以及算子与奖励源码(`alphacube/operators/common.py`、`dt_cross.py`、`dt_day.py`、`dt_in.py`、`nd_cs.py`,`partura/ops_ext.py`、`partura/steer.py`、`partura/diagnose.py`、`scripts/idea_search.py`)。
只用了 train / valid 的数字。

本轮快照新增:**M 的第 3 批**(14 个 head,全部是同一个新族)+ 本组第 2 轮的 E(r2a)与 N(r2b)。库里 29 个 head,3 个 R 替换生效。

---

## 0. 先钉死本轮新增的机械事实

沿用第 2 轮已钉死的六条((M-a) `ts_sum(x,1)` 恒等;(M-b) 根上单调包装在 hl=0 下是空操作、hl>0 下只改 EMA 跨日权重;
(M-c) `day_durbin_watson` 非负且尺度无关 ≈ 分钟序列的每分钟已实现方差;(M-d) `cross_*` 沿天轴、`cs_*` 才是截面;
(M-e) 控制的"波动"是 `cross_mean(day_std(Ret), 20)`,是**均值**型;(M-f) 本种子量纲下 `cross_corr` 不是相关系数而是 1e9×协方差)。
以下五条是本轮新读出来的,是理解 M 第 3 批和 r2a 的全部钥匙。

**(N-a) `cross_regbeta(x, y, d)` 的第一个参数是解释变量,返回 `cov_d(x,y) / Σ(x−x̄)²`,而且有一道 `var_x > 1e-9` 的 NaN 闸门。**
`dt_cross.py:299` → `common.rolling_ols(x, y, d, axis=0)["beta"]`;`common.py:663`:

    beta = torch.where(var_x > EPS, cov / var_x, NaN)      # var_x = Σ(x−x̄)²,**没有**除以 count;EPS = 1e-9

两个推论,都很硬:
1. **beta 的截面排序被 1/var_x 主导。** beta = corr·σ_y/σ_x,而 σ_x 在截面上跨几个数量级(成交量水平),corr∈[−1,1]、σ_y 相对同质。
   所以 `cross_regbeta(<成交量水平>, ·, d)` 的截面 ≈ **符号 × 1/(该股成交量水平的 d 日离散度)**。
2. **这道闸门把整个 `cross_reg*` 族逼到只能用大量纲的解释变量上。** 10 日窗口里 `day_var(Ret)`(~1e-6)的 Σ(x−x̄)² ≈ 1e-11 < 1e-9 → 全是 NaN;
   `day_std(Volume)`(~1e4–1e5)的 Σ(x−x̄)² ≈ 1e12 ≫ 1e-9。**这解释了 M3 的 14 个 head 为什么第一个参数清一色是 Volume / day_std 的原始量纲**,
   以及为什么它们的 beta 必然是量纲主导的。(写 E 种子时也要用:核心若是小量纲的,`cross_regbeta(核心, ·, d)` 这一支整支是死的,必须先 log / sqrt / cs_normalize。)

**(N-b) `day_distinct_ratio(Volume)` 是一个近乎二值的薄交易旗标,单独不可用。**
`ops_ext.py:607`:当日有限分钟里**不同取值的个数 / 分钟数**,1/n = 一整天一个值,1 = 每分钟都不同。
用在成交量上:正常交易的股票几乎每分钟成交量都不同 → ≈ 1;只有大量零成交分钟(极薄、封板、停牌)才明显 < 1。
定位工具的数字对得上:`day_distinct_ratio(Volume)` 的 `distinct` 只有 **0.0532**、`day_distinct_ratio(in_sum_rolling(Volume,10))` 只有 **0.0316**,
四个 sufficiency 全部 gate false(门槛废品)。**它必须被某种聚合变成可用的截面,它自己不是因子。**

**(N-c) `inv(cs_demean(·))` 是一个把极点放在每日截面均值上的奇异变换。**
`inv(x) = 1.0 / x`(`common.py:191`,**没有** epsilon);`cs_demean(x) = x − cs_mean(x)`。
作用在一个「大多数股票都等于 1」的旗标上:截面均值紧贴 1,于是**旗标恰好落在均值附近的那些股票被映射到 ±∞**,
均值两侧符号相反。这不是单调变换,是一次剧烈重排。

**(N-d) `cs_stddev_full(x)` / `cs_sum(x)` 返回的是行聚合后广播,在截面上是常数;而 `cs_last_high40` 等 `_lexi` 族用 `_pct_rank` 排序,并列按股票列序打破。**
`nd_cs.py:201`:`return std.expand_as(x)`;`ops_ext.py:231`:`_pct_rank` = `argsort(argsort(v, stable), stable)`,是**序数**秩,不是平均秩。
所以 `cs_last_high40(cs_stddev_full(A), B)` 里第一个参数在每一天是同一个数,`_pct_rank` 把它排成 **(该股在有效股票里的列序 + 1)/n** ——
一个每天几乎不变的、由股票列号决定的任意排序。详见 §1.4。
(对比:奖励自己的 `_zrank` 用的是 `rank_rows`,**并列取平均秩**(`diagnose.py:42-60`),所以根上的并列不会产生列序;
列序是在算子内部产生的,奖励端无法补救。)

**(N-e) `cs_mask_top_replace_mean_neg(x)` 把每日截面最低 10% 换成该行均值(`nd_cs.py:240` = `−cs_mask_top_replace_mean(−x)`)。**
三条推论:(i) 它不改动最高十分位的成员,所以对纯多头书的影响**只通过中性化回归**传导(被改的那 10% 改变了控制回归的系数,从而平移所有残差);
(ii) 叠两层 = 原始最低 20% 被压成两个并列块;(iii) 外面套 `cs_robust_z` 之类的仿射变换会改变「行均值在分布里的位置」,
也就是改变那 10% 并列块被停放在截面哪里 —— 在 `cross_regbeta` 的被解释变量位置上,它还额外起到「按每日 MAD 缩放 y」的作用,所以不是秩空操作。

---

## 1. alpha 的来源

### 1.1 真来源 ①(本种子最硬的一条,第 2 轮的 R 把它钉死了):**日内已实现方差的软幂平均**

第 2 轮的 R 给出了一个比预期强得多的结果:为了做空对照而写的
`pow_2_5(pow_3(day_var(Ret)))` 得 **2.0432**(train 2.0432 / valid 3.1583,ρ_known 0.2095,ρ_head 0.8439),
**比它要对照的 head(DW(High)^7.5,1.7753)还高,并且触发了替换**,现在是库里最高分的 head。
配合本轮拆解的阶梯:

| 指数 | 表达式 | score | train | valid |
|---|---|---|---|---|
| ^1 | `day_var(Ret)` | −1.5501 | −1.5501 | +0.1273 |
| ^2.5 | `pow_2_5(day_var(Ret))` | +0.7000 | +0.7000 | +2.6978 |
| ^3 | `pow_3(day_var(Ret))` | +1.1140 | +1.1140 | +3.0526 |
| ^7.5 | `pow_2_5(pow_3(day_var(Ret)))` | **+2.0432** | +2.0432 | +3.1583 |

由 (M-b),`day_var(Ret) ≥ 0`,所以这四行**在任何一天的截面上秩完全相同**;−1.55 → +2.04 这 3.6 的差距**全部**来自
幂次改变 20 日 EMA 的跨日权重。换句话说:

> **来源 ① = 对日内收益方差在约一个月上取一个「软幂平均」(p≈7.5 配 hl=20,即被最高方差的那几天主导),方向 −1。**
> 纯多头书买的是「最近一个月没有出现过极端日内波动日」的股票。

**为什么这不是已知异象的另一种写法(付费证据,三条都在)**:
- 控制里只有日内波动的 20 日**均值**(M-e),极值 / 离散度没被控制 —— 这条缝是写在奖励定义里的。
- 经典日收益 MAX 被证伪:第 1 轮 R 的 `cross_max(div(day_last(Close), ts_delay(day_last(Close), 1)), 20)` = **−0.8543**。所以不是 Bali 等的日收益彩票效应。
- **硬极值全部输给软幂平均**,三条通道各测一次:`cross_max(day_durbin_watson(High), 20)` = **−0.0573**;
  `cross_tail_mean_q75(day_durbin_watson(High), 20)` = **+0.1801**;`cross_max(pow_2(day_wmean(Ret,Ret)), 20)` = 0.7738(对 1.1814);
  `cross_quantile_q75(pow_2(day_wmean(Ret,Ret)), 20)` = −0.11。**「软」这件事是必要的,不是口味问题。**

**载体是可换的,聚合方式才是本体**(同一条 ^7.5 + EMA20 阶梯换输入):

| 输入 | score | valid | 来源 |
|---|---|---|---|
| `day_var(Ret)`(分钟收盘收益方差) | **+2.0432** | +3.1583 | r2 R |
| `day_durbin_watson(High)` | +1.7753 | +2.6633 | r2 拆解 |
| `day_durbin_watson(Close)` | +1.6800 | +3.1739 | r2 R |
| `day_durbin_watson(Low)` | +1.5391 | +2.7655 | r2 拆解(换字段) |
| `pow_2(log(div(day_max(High), day_min(Low))))`(Parkinson 极差²) | +1.0788 | +2.0800 | r2 R |
| `day_durbin_watson(Vwap)` | — | — | gate false(distinct 0.4129) |

五个互不相同的日内变动量测量,同一条聚合阶梯,全部 ≥ 1.0,valid 全部 ≥ 2.0。
再加一条**完全不同的聚合**也成立:`cross_stddev(day_durbin_watson(High), 60)`(hl 0,不含任何幂次)= +1.1007 / valid 2.0459。

**第 2 轮的解读要改一处:** r2/analysis.md 把核心说成 `day_durbin_watson(High)`(「分钟**最高价**序列的抖动」)。
R2 的空对照把这一层特殊性否掉了 —— 普通的分钟收盘收益方差是**更好**的载体(2.04 对 1.78)。
「最高价序列」「极差」「DW 式抖动」都只是同一个东西的不同写法,**核心应该写成 `day_var(Ret)`**。

### 1.2 真来源 ②(唯一一条非幅度信息,两个空对照都通过了):多日**方向持续**之后再折叠

head `pow_2(pow_2(cross_mean(day_wmean(Ret, Ret), 5)))`(M1,R 替换后生效),1.7104 / train 1.7104 / valid 2.4955。
第 2 轮 R 的两个空对照是为它写的,**都决定性地通过了**:

| 空对照 | score | train | valid | 读法 |
|---|---|---|---|---|
| `pow_2(pow_2(log(div(day_last(Close), ts_delay(day_last(Close), 5)))))`(\|5 日收盘收益\|⁴) | **−1.1987** | −1.1987 | −0.7305 | **不是**「周度极端收益」 |
| `pow_2(pow_2(cross_mean(day_sum(Ret), 5)))`(不加权的 5 日日内漂移⁴) | **−0.0163** | −0.0163 | +0.4804 | 自加权在周度上**仍然必要** |

加上第 2 轮已有的付费证据:充分性 `pow_2(cross_mean(day_wmean(Ret,Ret),5))` = 1.0515(train 1.0515 / valid 1.9396,所在 head 的 62%);
必要性 +0.53(knockout 掉 `cross_mean` 退回 1.1814);窗口 2 / 5 / 10 = 1.4926 / 1.7104 / 1.3986;
而且「先带符号平均再折叠」(1.7104)> 「先折叠再平均」(1.3561)。
**这是本种子唯一一条被两个独立空对照确认、而且不是纯量纲的信息。** 把握从第 2 轮的 0.4 提到约 0.6。
(保留的疑虑:它的父 head 仍在 W 通道里,和 r1a 的 7 个 `cross_corr` head 在最终库去重时可能互相挤掉。)

### 1.3 M 第 3 批的 14 个 head:**一个新的被观测量(薄交易旗标)+ 一个量纲型的 beta 包装**,机制很弱

M3 一次就贡献了 14 个 head(29 个里的一半),全部是同一个骨架:

    cross_regbeta( <成交量 / 价格的原始量纲水平> , <day_distinct_ratio 的某个 cs 变换> , d )

两个子族:
- **子族 A(5 个,sign 全是 +1)**:`inv(cs_demean(day_distinct_ratio(in_sum_rolling(Volume, k))))` 当被解释变量,d = 10。
  代表:`cross_regbeta(day_last(in_sum_rolling(Volume, 10)), inv(cs_demean(day_distinct_ratio(in_sum_rolling(Volume, 10)))), 10)`,1.2147。
- **子族 B(9 个,sign 多为 −1)**:`cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume)))` 及其变体当被解释变量,d = 15。
  代表:`cross_regbeta(day_std(Volume), cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume))), 15)`,1.1995。

**付费证据(本轮 27 次拆解里有 19 次花在这两个代表上)**:

| | 子族 A 代表(1.2147) | 子族 B 代表(1.1995) |
|---|---|---|
| 解释变量单独 | `day_last(in_sum_rolling(Volume,10))` −2.0091,**ρ_known 0.6191** | `day_std(Volume)` −1.6046,**ρ_known 0.5746** |
| 被解释变量单独 | gate false(distinct 0.0316) | gate false(distinct 0.0366 / 0.0532) |
| 去掉 `inv` | +0.0891,必要性 **+1.1256** | — |
| 去掉 `cs_demean` | +0.1005,必要性 **+1.1142** | — |
| 去掉 `cs_mask_top_replace_mean_neg` | — | −0.2556,必要性 **+1.4551**(ρ_known 翻到 −0.5286) |
| 去掉 `cs_robust_z` | — | **+1.2910,必要性 −0.0915** |
| Volume→Amt | +0.6384 / valid 2.2387 | +0.9891 / valid 2.2769 |
| 窗口 | 5 / 10 / 20 = 0.5568 / 1.2147 / 1.1541 | 7 / 15 / 30 = 0.7382 / 1.1995 / 0.9739 |

**我的判断:这一族的「测量」可能是真的,「机制」目前站不住,理由四条:**

1. **分数挂在奇异变换上。** 子族 A 的两个 knockout 各掉 1.11 / 1.13:`inv` 和 `cs_demean` **单独都没用,合起来才有分**。
   而合起来正是 (N-c) 的那个极点。一个真机制不会要求「必须在每日截面均值处除以零」。
2. **beta 的截面被 1/var_x 主导((N-a))。** 两个子族的解释变量**单独都因为 ρ_known ≥ 0.5 被取消资格**(0.619 / 0.575)——
   它们本身就是已知族(`cross_mean(day_std(Amt), 30)`)的近亲。`cross_regbeta` 除掉自己的滚动方差,恰恰是把这份成交量暴露
   从 ρ 0.6 压到 0.5 以下的那一步。所以「这一族 = 成交量离散度的倒数,披了一层 beta 的外衣把已知族闸门绕开了」是**现在最强的替代解释**。
   §4.2 的 A1 / A4(`inv(cross_stddev(·, d))`)和 A3 / A5(把解释变量 cs_normalize)是专门判这件事的。
3. **一个部件的必要性是负的。** `cs_robust_z` 去掉之后更好(1.1995 → **1.2910**,只差 0.0085 没触发替换)。它出现在 5 个 head 里,是纯死重。
4. **而 `cs_mask_top_replace_mean_neg` 必要性 +1.46** —— 由 (N-e),它唯一的作用是把截面最低 10% 的并列块停在某个位置、从而扰动中性化回归。
   1.46 的分数挂在「10% 并列块停在哪」上。这比第 2 轮判它「没有机制、+0.32、p 0.18」要**更坏**:它现在是承重件(n 17,均值差 +0.92,p 0.001)。

**但这个被观测量本身值得认真对待:** `day_distinct_ratio(Volume)` 测的是「分钟成交量序列有多粗糙 / 有多少零成交分钟」,
是一个 Lesmond 型的薄交易 / 报价冻结度量,而奖励只控制了**流动性水平**(`cross_mean(day_sum(Amt),30)`)与已知族(成交额波动的水平)。
它在共性表里是 n 62、均值差 +0.65、p 0.0001,是全表里 n 最大的显著正项(`day_durbin_watson(High)` 的 n 123 见 §1.5 的污染说明)。
**它从来没有在一个干净、非奇异的聚合下被测过** —— §4.2 的 A7 / A8 / A9 就是这三次测量。

### 1.4 r2a 的唯一 head 是**股票列序**的产物(本轮最重要的负面发现)

第 2 轮的 E 位(核心 `day_durbin_watson(High)`)花了 97 次评分,只出 1 个 head:

    cs_last_high40( cs_stddev_full(day_durbin_watson(High)),
                    cross_corr(day_durbin_watson(High), day_quantile(Volume), 20) )     # 0.6326 / valid 1.8534

由 (N-d) 逐层展开:`cs_stddev_full(DW(High))` 在每一天是**同一个数**(行标准差广播);
`_lexi` 对它取 `_pct_rank` —— 序数秩、并列按列序 —— 于是第一项退化成 **(该股在有效股票里的列号+1)/n**,一个每天几乎不变的任意排序;
第二项只做一件事:把 `cross_corr(DW(High), day_quantile(Volume), 20)` 最高 40% 的股票整体减 1。所以这个 head 的真身是

> **一个固定的、按股票列号排出来的名单,外加一个 40% 的筛子。** 核心 `day_durbin_watson(High)` 只通过那个筛子进入信号。

旁证:r2a 前五名里**四个**都用 `cs_stddev_full(...)` 当第一个参数(GP 找到了「让核心原样出现但不贡献信息」的后门);
其中两个(`cs_last_high40(cs_stddev_full(DW(High)), day_quantile_q75(Ret))`,0.4547,与那个套了 `cross_regres` 的,0.4326)
**valid 夏普完全相同(3.263867)**,正是「信号其实由第二个参数单独决定」的签名。

这条要写进笔记,而且是**一般性的后门**:任何 `cs_*` 的行聚合(`cs_stddev_full`、`cs_sum`、`cs_mean`、`cs_median`)放进 `_lexi` 族的第一个参数,
都能把核心约束变成形式上的满足。第 3 轮两个 E 位的任务假设里**必须明写禁止这一支**(E 任务无法在代码层拦,只能靠种子占位和假设说明压低它的采样概率)。
(顺带:M3 的 head `cross_regbeta(day_last(in_sum_rolling(Volume,5)), cross_regbeta(cs_normalize(day_std(High)), cs_sum(day_distinct_ratio(Volume)), 15), 10)`
里的 `cs_sum(day_distinct_ratio(Volume))` 也是截面常数,但它进的是回归的被解释变量位置,用的是**值**不是秩,所以不是列序产物;
它的内层 beta ≈ cov(该股波动 z 分, 全市场旗标)/var,仍然是 1/var 主导。)

### 1.5 共性表本轮更不可读,只有拆解那一栏干净

PLAN 修订 10(1) 说的事在本轮更严重,而且多了一个方向:

- **E 任务的候选分数被系统性压低**(奖励里多加了核心家族),混进 513 个候选的池子里会让含该核心的子树看起来变差。
  实例:`day_durbin_watson(High)` 的均值差从第 2 轮的 **+1.28(n 57)** 掉到本轮的 **+0.48(n 123)**。
  n 正好多了 66 ≈ r2a 的 97 个候选里含核心的那一批。**DW 没有变差,是 r2a 的 E 口径把它的池子稀释了。** 别据此降低对来源 ① 的评价。
- 反过来,**M3 是一次运气好的运行**(14 个 head),它独有的子树(`day_distinct_ratio(Volume)`、`day_last(in_sum_rolling(Volume,5))`、
  `cs_robust_z(...)`)会继承「M3 这次运行好」这份运气。`cs_robust_z(day_distinct_ratio(Volume))` 的 +0.91 / p 0.001 与它
  **必要性 −0.09** 的付费结论直接矛盾 —— 以付费结论为准。
- 存档均值仍在约 −0.75 ~ −0.8,「均值差 > 0」不等于「好」。

**结论:共性表本轮只能当「这一簇长什么样」的目录用,不能当证据。本轮所有判断都只挂在拆解 / R 的付费数字上。**

### 1.6 代理与死胡同(沿用 + 更新)

- **价格水平一族,现在有三个 head、方向可能互相冲突。** `ts_sum(LogFloatShares, 30)`(0.5177,sign +1)由第 2 轮的推导 ≈ −log(价格);
  r2b 新出的两个 head `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(day_last(Open)))`(1.0038,sign **+1**)与
  `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(day_quantile(Open))))`(0.6981,sign +1)
  —— `day_last(Open)` 是最后一分钟的开盘价、`day_quantile(Open)` 是日内价格中位数(`dt_day.py:151`,默认 q=0.5),**都是价格水平本身**。
  两边 sign 都是 +1 而底层方向相反,**交易信号很可能 ρ ≤ −0.5**,最终库按 PLAN §3 会杀掉其中一方(而且 M 的 head 先收,
  所以被杀的大概是 r2b 这两个,即 N 位第 2 次的产出可能整体归零)。这件事必须让 PI 知道,§4.2 的 D15 / D16 是最便宜的判别。
  另外 `day_last(Open)`、`day_quantile(Open)` 的**裸量从来没有付费分数** —— 这是整轮里最便宜的决定性对照。
- `day_signed_ratio(Ret, Amt)`(BVC 净买压):死胡同,共性全表最差,第 1 轮 N 位 0 产出。不再花钱。
- `div(·, LimitWidth)`:两次证伪(R −0.1305;E 位无 head)。不再花钱。
- `day_topw_mean(Ret, Amt)` 原始量:只有折叠 + ^8 过线,属于来源 ① 的第三条通道,不是「聪明钱」。
- `ts_cov(day_median(Vwap), day_var(Ret), 20)`、`day_median(Vwap)`、`day_quantile_q75(Volume)`、`cs_rank(day_mean(Ret))`:血缘固定块。
- **W 通道的 `cross_corr` 一族(r1a 的 7 个 head)**:第 2 轮 R 给了判决 —— 老实写法全部远低于退化原式:
  `cross_stddev(pow_2(W), 241)` = 1.0891(对 1.7835)、`@60` = 0.8803(对 1.7475)、`@20` = **0.6273**(对 1.2106,门槛 1.3106,ρ_head 0.7941);
  真正归一化的变异系数 `div(cross_stddev(pow_2(W),241), cross_mean(pow_2(W),241))` = **−0.3604**。
  **即:这三个 head 的分数是 EPS 阈值非线性「做出来」的,清不干净**(第 2 轮 R7 预测错在这里)。
  它们照样在库里,B 组动不了 M 的 head 除非替换达标 —— 已经试过,没达标。写进笔记当局限。

---

## 2. 烂部件(适合做 R)

| # | 部件 / head | 付费证据 | 判断 |
|---|---|---|---|
| 1 | `cs_robust_z(day_distinct_ratio(Volume))` | 必要性 **−0.0915**(去掉后 1.1995 → 1.2910,train 1.4259 / valid 1.2910) | **全部付费记录里唯一一个负必要性。** 出现在 5 个 M3 head 里。去掉就更好,只差 0.0085 没触发替换 → 本轮 R 的头号目标(换窗口 / 换解释变量即可越过门槛) |
| 2 | `inv(cs_demean(·))` 作用在 `day_distinct_ratio` 上 | 两个 knockout 各 +1.13 / +1.11,单独都只剩 0.09 / 0.10 | 分数挂在每日截面均值处的极点上((N-c))。5 个 head。不可能「去掉一个部件」变好,只能整式换成非奇异写法 |
| 3 | `cs_stddev_full(·)` 当 `cs_last_high40` 的第一个参数 | 截面常数 + `_pct_rank` 序数秩 → 列序((N-d));r2a 前五名四个都用它,两个 valid 完全相同 | 不是部件问题,是**整个 head 要重写**。门槛只要 0.7326,是本轮最便宜的一次「把列序产物换成真信号」 |
| 4 | `cs_mask_top_replace_mean_neg` | 必要性 **+1.4551**(子族 B);共性 n 17 / +0.92 / p 0.001;出现在 M3 的 4 个 + r2b 的 2 个 + r1a 的 2 个 head 里 | 第 2 轮判「没机制」,本轮要**改判为承重件** —— 而它承的是 (N-e) 的「10% 并列块停在哪」。去不掉,但要在笔记里标成最终库里最可疑的一类 head |
| 5 | `ts_sum(·, 1)` | 必要性 −0.0029 | 恒等算子。最高分 head 上的两层已随 R 替换消失;还剩 `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)`(1.1007)一处。增益 0,永远触发不了替换,只需在笔记里记下真身 |
| 6 | `day_wmean(Ret, <价格字段>)` 里的价格权重 | 第 2 轮 R 已替换(`cross_corr(pow_2(day_mean(Ret)), ...)` 0.8998,ρ_head 0.7074) | 已处理完毕 |
| 7 | `pow_2(pow_2(day_zero_ratio(Ret)))` 这个空对照 | gate false(distinct 0.0544) | 「薄交易」这条替代解释至今**没有**对照。本轮用 `cross_mean(day_flat_ratio(Volume), 20)` 补(见 §4.2 A9) |

---

## 3. 第 2 轮任务的复盘

### 3.1 E 位 `c05s807Br2a_Ea`,核心 `day_durbin_watson(High)`

97 次评分、1 个过线、1 个进 heads。采样计数 `{c05_no_core: 1331, c05_periphery_seen: 8}` —— 「外围必须没见过」只拦了 8 次,仍然不是瓶颈。
15 个种子分六族:上下行不对称(3)、是哪一种波动(2)、相对自身历史(4)、峰值/均值(1)、跨日共动与持续性(4)、截面条件化(1)。
**六族全部没出 head**;出的那一个来自 GP 自己找到的 `cs_last_high40 + cs_stddev_full` 后门(§1.4),而且是列序产物。

**与第 1 轮对比出来的一条经验,很值钱:**

| E 位 | 家族控制里的 head 数 | 评分次数 | 过线 | 进 heads |
|---|---|---|---|---|
| r1a(核心 `pow_2(day_wmean(Ret,Ret))`) | 1 | 76 | 13 | 7 |
| r2a(核心 `day_durbin_watson(High)`) | 2 | 97 | 1 | 1 |

第 1 轮的教训是「家族控制比想象的弱」,第 2 轮把它翻过来了:**从 1 个到 2 个家族成员,产出从 7 掉到 1。**
两点样本不能定量,但方向很清楚 —— **本轮选核心时,家族控制的大小应当是第一位的筛选条件**,
而不是共性表上的均值差。(这也直接否掉了把 `day_distinct_ratio(Volume)` 当核心的方案:它的家族控制会放进 6 个 head,是历史最重。)

### 3.2 N 位 `c05s807Br2b_Nb`

75 次评分、5 个过线、2 个进 heads。假设是「交易活动的二阶矩」(日内成交锯齿度 / 跨日变异系数),14 个种子全部无量纲。
**产出与假设完全无关**:5 个过线者全是 `cs_mask_top_replace_mean_neg` 套 `day_last(Open)` / `day_quantile(Open)`,即**价格水平 + 掩码**(§1.6)。
14 个种子里没有一个活动类的量进了前五。

两次 N 位的共同点:**没有核心约束时,GP 会离开种子区域**(第 1 轮漂到幅度族,第 2 轮漂到价格水平)。
两个 N 位合计 141 次评分、3 个 head,其中 1 个是来源 ① 的第三种写法、2 个是价格水平且可能在最终去重时被 M 的 head 杀掉。
**「换一条被观测量」这个想法本身没有被实现过一次。** 这是本轮两个位都给 E 的最强理由。

### 3.3 R(16 次付费,2 次替换生效)

替换生效:(i) `pow_2_5(pow_3(day_var(Ret)))`(2.0432)顶掉 DW^7.5 那个 head(1.7753)—— 本轮收益最大的一笔,见 §1.1;
(ii) `cross_corr(pow_2(day_mean(Ret)), pow_2(day_wmean(Ret,Ret)), 20)`(0.8998)顶掉 `Low` 权重那个(0.6092)。
另有 `ts_sum(pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1)), 2)`(1.9025,ρ_head 0.9994)也达标,被 2.0432 那个压过。
R 的主要收获不是替换,是三组判决:来源 ① 的载体可换(§1.1)、来源 ② 的两个空对照都通过(§1.2)、
W 通道的 `cross_corr` 清不干净(§1.6)。

### 3.4 第 2 轮事先预测的打分

| # | 预测 | 结果 | 实际 |
|---|---|---|---|
| E1 | r2a 产出 ≥ 2 个 head(0.6) | **错** | 1 个(97 次评分)。而且是 §1.4 的列序产物。见 §3.1 的家族控制表 |
| E2 | 上下行不对称族(DW(High) 对 DW(Low)/DW(Close) 的差与比)不出 head(0.6) | **对** | 没有任何 `sub/div(DW(High), DW(·))` 形状进前五 |
| E3 | 若有 head,来自「相对自身历史 / 归一化离散度」或「跨日共动」,不是截面条件化(0.55) | **半错** | 唯一的 head 恰恰是一个**截面筛子**(`cs_last_high40`);但点名的 `cs_bucket_zscore` 那一支也没出东西。两个看好的族都空了 |
| E4 | 分钟已实现方差 / Parkinson 极差² 这一支不过线(0.55) | **对**(GP 里) | E 位里没有这一支的 head;R 给了数字:Parkinson ^7.5 = 1.0788。它**单独**是能过 0.5 的,在 E 口径下过不了是因为被核心家族吃掉 |
| E5 | 过线的 head 多数 valid ≥ train(0.7) | **对** | r2a 前五 valid 全部 > train(1.85/3.26/1.14/1.68/3.26 对 train 0.63/0.45/0.45/0.44/0.43);r2b 前五里 4 个 |
| N1 | N 产出 ≥ 1 个 head(0.5) | **对** | 2 个 |
| N2 | 最好的是**日内**成交锯齿度/集中度、方向 −1(0.5) | **错,而且错得有用** | 最好的是 `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(day_last(Open)))`,sign **+1**,是价格水平,根本不在活动通道上 |
| N3 | 跨日日成交额变异系数(Chordia 原式)单独 score < 0.5(0.55) | **无法核对** | 它是种子不是 head,前五名里没有它。和第 1 轮的 N3 一样无法核对 —— 教训:预测要写成「定位输出能核对的量」 |
| R1 | `ts_sum@1→2` 触发替换(0.95) | **对** | 1.9025,ρ_head 0.9994,`replaces: true`(最后被 2.0432 压过) |
| R2 | `pow_2_5(pow_3(day_var(Ret)))` score < 1.0(0.6) | **错,本轮最有价值的一次错** | **2.0432**,比被对照的 head 还高 0.27,并且成了库里最高分 head。「DW(High) 不只是收盘收益方差的尾部」这个判断反了 |
| R3 | Parkinson 极差² 的 ^7.5 score < 1.0(0.55) | **半对** | 1.0788(擦着过),valid 2.08 |
| R4 | `DW(Close)^7.5` ≥ 1.2(0.6) | **对** | 1.6800 / valid 3.1739。换价格序列不关键 |
| R5 | `cross_max(DW,20)` 与 `cross_tail_mean_q75(DW,20)` 都低于 1.78(0.7) | **对,而且极强** | −0.0573 与 +0.1801。软幂平均赢硬极值赢得毫无悬念 |
| R6 | `cross_stddev(W²,241)` ≥ 1.0 而 241 日变异系数 < 0.5(0.55) | **全对** | 1.0891 与 −0.3604。W 通道是**量纲**,不是形状 |
| R7 | `cross_stddev(W²,20)` 替换掉自相关退化那个 head(0.4) | **错** | 0.6273,门槛 1.3106。退化 head 清不干净(§1.6) |
| R8 | \|5 日收益\|⁴ < 1.0(0.65) | **对,决定性** | −1.1987 |
| R9 | 不加权 5 日日内漂移 ^4 < 1.2(0.6) | **对,决定性** | −0.0163 |
| R10 | `log(day_last(Close))` 不替换低价 head(0.6) | **对** | −1.1308,ρ_head 0.3258 |
| R11 | 本轮替换总数 1~2 个(0.65) | **对** | 2 个(库里累计 3 个生效) |

合计:**对 12、错 4、半对 2、无法核对 1**(19 条)。

**校准教训(与第 1 轮的不同,要分开记):**
第 1 轮错在「高估家族控制、低估量纲相对方向的分量」。
第 2 轮的四个错(E1、N2、R2、R7)聚在另一处:**我高估了「具体写法」的特殊性,低估了「分数其实是聚合层 / 数值效应做出来的」。**
- R2:以为 DW(High) 这个载体特殊,其实普通日内方差更好 —— 载体不特殊,聚合层才是本体。
- R7:以为退化的 head 可以还原成老实写法,其实分数就是退化本身给的。
- E1:以为核心强、外围空就会出 head,其实家族控制一加就塌。
- N2:以为种子能把 GP 按在假设上,其实没有核心约束它就漂走了。
本轮的预测要按这一条调整:**凡是「这个字段 / 这个指数 / 这个窗口是对的」类型的预测,先按「大概不特殊」下注。**

---

## 4. 本轮候选

### 4.1 值得深挖的核心(≤3,按推荐顺序)

#### 核心 ①(首推)`day_var(Ret)` —— 来源 ① 的干净写法

- **证据**(全部付费):幂次阶梯 ^1 / ^2.5 / ^3 / ^7.5 = −1.5501 / +0.7000 / +1.1140 / **+2.0432**,必要性(去 `pow_3`)+1.3432;
  五种载体同一条阶梯全部 ≥ 1.0(§1.1);完全不同的聚合(60 日滚动标准差,hl 0)也成立;
  三条硬极值对照全部大败(−0.06 / +0.18 / 0.77);经典日收益 MAX = −0.85。
- **家族控制只有 1 个 head**(快照里只有 `pow_2_5(pow_3(day_var(Ret)))` 原样含它)—— 由 §3.1 的表,这是历史上产出最好的那档。
- **它周围已经见过的外围写法(极少)**:只有 `{pow_3}`、`{pow_2_5∘pow_3}`、`{pow_2_5}`(本轮拆解)三种,全部是根上的幂次;
  以及第 1 轮 R 的 `div(pow_2(day_wmean(Ret,Ret)), day_var(Ret))`(0.3671)和 r2a 的一个种子 `div(day_durbin_watson(High), day_var(Ret))`(没出 head)。
  **「幂次」这一招之外,这个核心周围是空的。**
- **外围该往哪长(都没见过,而且都在「无量纲 / 条件化」这一侧 —— 正是最终库里最可能 ρ 独立的方向)**:
  (a) **带符号拆分**:上行 / 下行日内半方差的不对称(文献上的 realized semivariance 一族);
  (b) **相对自身历史**:`div(day_var(Ret), cross_mean(day_var(Ret), 60))`、`cross_madz`、5/60 之比 —— 把「天生高波动的股票」与「这个月异常高波动的股票」分开,
      而控制里只投掉了 20 日均值;
  (c) **条件分组**:按 `ListAge`、`BoardCode` 分组内的 z 分 / 分位(第 1、2 轮都没真正测过截面条件化,r2a 那一支是后门污染的);
  (d) **日内方差的形状而不是水平**:日内方差在一天之内的集中度(上下午之比、最重 10% 分钟的方差份额);
  (e) 与**成交 / 冻结报价**的跨日共动(量纲上要先取 log / sqrt,见下)。
- **必须写进任务假设的三条禁令**:
  1. **不要再爬幂次阶梯**。由 (M-b),根上的幂在 hl=0 下是空操作、hl>0 下只改 EMA 权重;^1 / ^2.5 / ^3 / ^7.5 已经全部付过钱,
     而且家族控制会把 2.04 那个 head 整个扣掉。任何 `pow_X(day_var(Ret))` 形状都是浪费。
  2. **`cross_regbeta(day_var(Ret), ·, d)` 这一支是死的** —— 由 (N-a),10~20 日窗口里 Σ(x−x̄)² ≈ 1e-11 < 1e-9,beta 全是 NaN。
     要用回归 / 相关,必须先 `log` / `sqrt` / `cs_normalize`。
  3. **禁 `cs_stddev_full` / `cs_sum` / `cs_mean` 当 `cs_last_high40` 等 `_lexi` 族的第一个参数**((N-d) 的列序后门,§1.4)。
     同理也要避开 `cross_corr(f(day_var), g(day_var), d)`(两边都是 1e-6 量级 → (M-f) 的 EPS 退化,重演 r1a)。

#### 核心 ②(次推)`pow_2(cross_mean(day_wmean(Ret, Ret), 5))` —— 唯一一条非幅度信息

- **证据**:自身 1.0515(所在 head 1.7104 的 62%),必要性 +0.53,窗口 2/5/10 = 1.4926/1.7104/1.3986,
  「先平均再折叠」1.7104 > 「先折叠再平均」1.3561;**第 2 轮的两个空对照都决定性通过**(\|5 日收益\|⁴ = −1.1987;不加权版 = −0.0163,§1.2)。
- **家族控制只有 1 个 head**(M1 那个)。
- **它周围已经见过的外围写法**:只有 `{pow_2}`(head 就是它的平方);近邻 `cross_mean(pow_2(pow_2(day_wmean(Ret,Ret))), 5)`(1.3561,顺序相反)。**几乎全空。**
- **外围该往哪长**:方向**持续了几天**(符号游程、自相关、反转以来的天数)而不是持续得多强;
  持续性与成交额 / 隔夜缺口的交互;把固定的 5 天换成「自上一次方向反转以来」;「持续 × 幅度」的二维切分(而不是先乘起来);
  以及 r2/lit.md L4 第 2 点提示过、本种子还没做的一条:**先按符号拆分、再各自算离散度**。
- 同样要写上面那三条禁令(量纲 W² ~ 1e-7,`cross_corr` 必退化;`cross_regbeta` 第一参数位同样会撞 NaN 闸门)。
- 风险:它仍在 W 通道里,父 head 与 r1a 的 7 个 `cross_corr` head 在最终库去重时可能互相挤掉;但它是本种子唯一一条经过两次空对照的非量纲信息。

#### 核心 ③(**不建议给 E 位**,理由写清楚)`day_distinct_ratio(Volume)`

- 为什么诱人:M3 的 14 个 head 的共同不变量;共性 n 62 / +0.65 / p 0.0001;一条全新的被观测量(薄交易 / 报价冻结的分钟级粗糙度),
  奖励只控制了流动性**水平**;而且**这是 B 组唯一有机会把一个干净成员塞进 M 最大那一族的地方**。
- 为什么不给 E 位,三条:
  1. **家族控制会放进 6 个 head**(快照里原样含它的 head 有 9 个,按 score 取前 6:1.1995 / 1.0946 / 0.7508 / 0.7404 / 0.7146 / 0.6726)——
     历史最重,而 §3.1 的表显示 2 个就足以把产出从 7 压到 1。
  2. 它**单独不可求值**(gate false,distinct 0.0532),所以 E 的「核心原样包含」会把 GP 逼向「再加一个奇异 cs 变换」—— 正是 §1.3 判为烂的那一类。
  3. 它的干净写法用 R 就能测,**不必花一个 GP 位**(§4.2 的 A7~A9)。
- **注意一个制度性限制(PLAN 修订 10(2))**:R 只「替换」不「收录」。所以如果 A7(`cross_mean(day_distinct_ratio(Volume), 20)`)
  干净地过了线但与原 head ρ < 0.5,它**评完就丢,进不了库**。这是本轮唯一一个「想要却拿不到」的东西,PI 要在笔记里记成局限。
  (若 PI 不接受这个取舍,核心 ③ 的 E 位是唯一的路 —— 那就要接受 6 个家族成员和大概 0~1 个产出。我的排序是 ① + ② > ① + ③。)

#### 明确不要给 E 位的核心卡

- #2 `ts_sum(pow_3(day_durbin_watson(High)), 1)`、#3 `pow_2_5(ts_sum(pow_3(...), 1))`、#4 `pow_3(day_durbin_watson(High))`、
  #5 `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)`、#6 `cross_fangzheng(pow_2_5(...), 60)`、#11 `cross_stddev(day_durbin_watson(High), 60)`、
  #26 `cs_stddev_full(day_durbin_watson(High))`、#28 `day_durbin_watson(High)`:
  都是把**已知的聚合层**写死进核心(而且 `day_var(Ret)` 是更好的载体,§1.1);#28 还已经用掉 1 个 E 位、产出是列序产物。
- #7 `pow_3(pow_2_5(LogFloatShares))`、#8 `cross_fangzheng(pow_2_5(LogFloatShares), 60)`、#12 `pow_2_5(LogFloatShares)`:低价效应代理,
  幂次在 hl=0 下是空操作、`fangzheng` 作用在近常量上退化成水平。
- #10 `cs_mask_top_replace_mean_neg(day_quantile(Open))`、#15 `day_quantile(Open)`:价格水平 + 烂部件 #4(§1.6)。
- #13 `cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume)))`、#14 `cs_robust_z(day_distinct_ratio(Volume))`、
  #18 `cs_mask_top_replace_mean_neg(day_distinct_ratio(Volume))`:把负必要性的部件(烂部件 #1)写进核心。
- #1 `pow_2(day_wmean(Ret,Ret))`、#9 `pow_2(pow_2(day_wmean(Ret,Ret)))`、#21 `pow_2(cs_mask_top_replace_mean_neg(pow_2(day_wmean(Ret,Ret))))`、
  #23 `day_wmean(Ret,Ret)`:r1a 已用掉 1 个 E 位、7 个 head 是 §1.6 的退化族;家族控制现在要放 6 个。整个实验剩的那 1 个位不值得花在这里。
- #17 `sub(day_durbin_watson(High), day_quantile_q75(Ret))`、#24 `cs_normalize(day_std(High))`、#19 `day_last(in_sum_rolling(Volume,5))`、
  #22 `day_std(Volume)`、#29 `day_std(High)`:前两者来自 r2a 的 E 口径污染;后三者单独 ρ_known 在 0.5 附近或更高(0.57 / 0.62),是已知族近亲。

### 4.2 R 目标(16 个,按价值排序;标明哪些有替换机会、哪些只是买证据)

**A 组 —— M3 的 14 个 head(本轮最高杠杆:B 组能改动 M 的 head 只有这一条路)**

挂 `cross_regbeta(day_std(Volume), cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume))), 15)`(1.1995,门槛 **1.2995**):
- **A1 `inv(cross_stddev(day_std(Volume), 15))`** —— 决定性空对照兼替换候选:若 §1.3 的读法对(beta 的截面 ≈ ±1/var_x),
  这个完全不含 `day_distinct_ratio` 的式子应当接近 1.20,而且与原 head 的 ρ 很可能 ≥ 0.5 → 有机会把一个 regbeta 黑箱换成一句可读的话。
- **A2 `cross_regbeta(day_std(Volume), cs_mask_top_replace_mean_neg(day_distinct_ratio(Volume)), 20)`** —— 去掉负必要性的 `cs_robust_z`(烂部件 #1)。
  15 窗口版已付过钱:1.2910,差 **0.0085** 没达标;全链窗口 7/15/30 = 0.74/1.20/0.97,20 没测过,是最便宜的一次替换机会。
- **A3 `cross_regbeta(cs_normalize(day_std(Volume)), cs_mask_top_replace_mean_neg(day_distinct_ratio(Volume)), 15)`** ——
  同时去掉 `cs_robust_z` 并把解释变量日度 z 分(消掉 1/σ 的量纲主导)。既是 1.1995 的替换候选,也可挂 1.0946 那个 head(门槛 1.1946)。

挂 `cross_regbeta(day_last(in_sum_rolling(Volume, 10)), inv(cs_demean(day_distinct_ratio(in_sum_rolling(Volume, 10)))), 10)`(1.2147,门槛 **1.3147**):
- **A4 `inv(cross_stddev(day_last(in_sum_rolling(Volume, 10)), 10))`** —— 同 A1,子族 A 版。
- **A5 `cross_regbeta(cs_normalize(day_last(in_sum_rolling(Volume, 10))), inv(cs_demean(day_distinct_ratio(in_sum_rolling(Volume, 10)))), 10)`** ——
  解释变量 z 分。A1 / A4 / A5 三条一起把「是不是 1/成交量离散度」判死。
- **A6 `cross_regbeta(day_last(in_sum_rolling(Volume, 10)), inv(cs_demean(day_distinct_ratio(in_sum_rolling(Volume, 10)))), 15)`** ——
  唯一没测过的窗口(5/10/20 = 0.5568/1.2147/1.1541,峰可能在 10~15 之间)。

买证据(ρ 大概 < 0.5,**不会**替换,见 §4.1 核心 ③ 的制度性限制):
- **A7 `cross_mean(day_distinct_ratio(Volume), 20)`** —— 这个被观测量在**非奇异聚合**下的第一次测量。
  ≥ 0.5 ⇒ M3 这一族有可解释的替身,下一个实验应该从这里开始;≤ 0 ⇒ 整族是 cs 变换的产物,B 组库里继承了 14 个脆弱 head(写进笔记当局限)。
- **A8 `cross_stddev(day_distinct_ratio(Volume), 20)`** —— 旗标的**不稳定性**(Chordia 式二阶矩)。
- **A9 `cross_mean(day_flat_ratio(Volume), 20)`** —— 姐妹测量(分钟成交量与上一分钟相同的占比,`ops_ext.py:82`),
  顺手补上烂部件 #7 一直缺的「薄交易」空对照(第 1 轮的 `day_zero_ratio(Ret)` 版 gate 失败)。

**B 组 —— 来源 ①(库里权重最大的那个 head)**

挂 `pow_2_5(pow_3(day_var(Ret)))`(2.0432,门槛 **2.1432**):
- **B10 `pow_2_5(pow_3(day_wstd(Ret, Ret)))`** —— 第 1 轮的 `pow_2(pow_2(day_wstd(Ret,Ret)))` 是整组 R 里 valid 最高的
  (0.9336 / valid **2.7841**);把同一通道推到 ^7.5 阶梯上,是本轮唯一有机会顶掉库里最高分 head 的一条。
- **B11 `pow_2_5(pow_3(div(day_var(Ret), cross_mean(day_var(Ret), 60))))`** —— 阶梯作用在「相对自身 60 日水平」的无量纲方差上。
  控制里只有 20 日均值;这一条把「天生高波动」与「这个月异常高波动」分开,是来源 ① 机制上最干净的说法,也可能直接替换。

挂 `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)`(1.1007,门槛 **1.2007**):
- **B12 `cross_stddev(day_var(Ret), 60)`** —— 把「第二种独立聚合」换到更好的载体上(顺带去掉恒等的 `ts_sum`,烂部件 #5)。
  门槛低、ρ 有机会 ≥ 0.5,是 B 组少见的「同时换掉烂部件和差载体」的机会。

**C 组 —— r2a 的列序 head(门槛最低)**

挂 `cs_last_high40(cs_stddev_full(day_durbin_watson(High)), cross_corr(day_durbin_watson(High), day_quantile(Volume), 20))`(0.6326,门槛 **0.7326**):
- **C13 `cs_last_high40(day_durbin_watson(High), cross_corr(day_durbin_watson(High), day_quantile(Volume), 20))`** ——
  把截面常数的第一个参数换成真面板,信号从「列序名单 + 筛子」变成真正的词典序筛选。门槛只要 0.7326。
  风险要说清:两者结构差别大,ρ 可能 < 0.5 而不触发替换;但 B 组这一个 head 若留着就是 §1.4 的产物,值得一次尝试。
- **C14 `cross_corr(day_durbin_watson(High), day_quantile(Volume), 20)`** —— 那个筛子变量自己是不是因子。
  **量纲上这一个 `cross_corr` 不退化**(var_y ~ 1e10,`sqrt(var_x·var_y)` ~ 1e-1 ≫ EPS),是真相关系数,可以直接读。

**D 组 —— 价格水平的方向冲突(最便宜的决定性对照)**

挂 `cs_mask_top_replace_mean_neg(cs_mask_top_replace_mean_neg(day_last(Open)))`(1.0038,门槛 **1.1038**):
- **D15 `day_last(Open)`** —— 裸价格水平,**整个实验还没有付费分数**。它决定 r2b 的两个 head 是「价格水平」(那么它们与
  `ts_sum(LogFloatShares, 30)` 方向相反,最终库按 ρ ≤ −0.5 很可能把 r2b 的产出整体杀掉)还是「掩码扰动中性化回归」。
- **D16 `cs_mask_top_replace_mean_neg(day_last(Open))`** —— 一层掩码(现在只有两层 1.0038 和三层 0.6981 的数字),补齐阶梯、判烂部件 #4。

说明:A1~A6、B10~B12、C13、D16 有替换机会;A7~A9、C14、D15 是买证据(并且由 PLAN 修订 10(2),买证据的那些**不会进库**)。
另:`ts_sum(·,1)`(烂部件 #5)增益恒为 0,不要再为它花 R;`div(·, LimitWidth)`、`day_signed_ratio(Ret, Amt)` 两次证伪,不要花钱。

### 4.3 N 的灵感(我建议两个位都给 E,这里是备选)

- **N-a(若必须选 N,首选)把干净聚合搬到薄交易旗标上**:`cross_mean(day_distinct_ratio(Volume), 20)`、
  `cross_stddev(day_distinct_ratio(Volume), 60)`、`cross_madz(day_distinct_ratio(Volume), 60)`、`day_flat_ratio(Volume)` 及其跨日离散度、
  以及 `div(day_distinct_ratio(Volume), day_distinct_ratio(Amt))`(成交量格点粗糙度 / 成交额格点粗糙度,区分「手数格点」与「真没成交」)。
  这是**唯一一条能让 M 最大那一族的干净版本进库**的路(R 做不到,见 §4.1 核心 ③)。方向交给奖励。
- **N-b 日内方差的形状**:日内已实现方差在一天内的集中度(上下午之比、最重 10% 分钟的方差份额、`day_argmax(pow_2(Ret))` 的分布),
  全部无量纲 —— 来源 ① 已证明「水平 + 凸聚合」有效,没人问过「这一天的波动集中在什么时候」。
- **N-c(降权)活动的二阶矩**:第 2 轮已经押过,14 个种子 0 个进前五(§3.2)。不要再押同一组。

**两个 GP 位怎么分配(我的排序,PI 决定)**:
**① E(核心 ① `day_var(Ret)`)+ E(核心 ② `pow_2(cross_mean(day_wmean(Ret,Ret),5))`)** > ② E(核心 ①)+ N-a > ③ E(核心 ①)+ E(核心 ③)。
理由:两个核心的家族控制都只有 1 个 head(§3.1 的表说这是唯一一档出过东西的配置);两个核心周围的外围都只见过「幂次」一招;
两次 N 位合计 141 次评分、3 个 head、0 次「换一条被观测量」成功(§3.2),先验很差;
而「至少 1 个 N 位」的约束第 1、2 轮已经各满足一次,本轮两个位都给 E 是合法的。

---

## 5. 文献题目(交文献员,≤4;只收 2023-08-08 之前发表的)

r2/lit.md 的 L1(极差型 / 已实现方差估计量)、L2(聚合方式)、L3(日内漂移与多日平均)、L4(波动的波动、零变动占比)**不要重复**;
下面四题都是按本轮的新证据重新对焦的,并且都标明了「我要用它决定什么」。

**L1 —— 对准核心 ①(`day_var(Ret)` 的软幂平均;§1.1)。要决定:E 位的外围该押「带符号拆分」「相对自身历史」还是「条件分组」。**
问:文献里对**日内已实现方差**做过哪些**超出「水平 / 均值」的处理**?具体想要:
(a) **已实现半方差 / 带符号拆分**(把日内收益按正负分开各算方差)作为**横截面收益预测变量**(不是波动预测变量)的检验,
    以及拆分之后哪一半被定价、符号方向如何;
(b) **把日内方差相对该股自身历史水平标准化**(除以自身 60 日均值、变异系数、z 分、分位)之后还有没有定价能力,
    以及文献给的归一化理由(r2 的 L4 在 vol-of-vol 上没能从全文核实这一点,这次换成「已实现方差相对自身水平」再问一次);
(c) 这类度量按**上市年限、板块、流动性、规模**分组之后结论怎么变(我手上的 `ListAge`、`BoardCode` 两个叶子还没用过);
(d) **日内方差在一天之内的分布 / 集中度**(日内波动的 U 型、上下午之比、方差集中在哪几分钟)有没有被当成横截面特征用过。
关键词(EN):realized semivariance; signed jump variation; downside realized variance cross-section of returns;
normalized realized variance; variance ratio to own trailing level; intraday volatility pattern U-shape;
volatility concentration within the day; conditional sorts by listing age / board / liquidity; China A-share realized volatility。
关键词(中):已实现半方差;带符号跳跃;下行已实现方差与横截面收益;相对自身历史标准化的波动;日内波动的日内分布;U 型日内波动;
波动在日内的集中度;按上市年限 / 板块 / 流动性分组;A 股已实现波动。

**L2 —— 对准核心 ③ 与 R 的 A 组(`day_distinct_ratio(Volume)`:分钟成交量序列的「取值个数 / 粗糙度」;§1.3、(N-b))。
要决定:这个被观测量该用什么聚合变成横截面变量,以及它是不是已知流动性度量的另一种写法。**
问:文献里怎么构造和定价**价格 / 成交量序列的「离散性、粗糙度、取值个数」类度量**?具体想要:
(a) **零成交分钟 / 零收益天数占比**(Lesmond 型、Liu 式零成交天数、新兴市场的零收益比例)如何被构造成月度截面变量 ——
    尤其是**把一个近乎二值的日度旗标聚合成截面变量**的做法(计天数、滚动均值、滚动标准差、相对自身历史的异常);
(b) **价格离散性 / 最小报价单位 / 整手(A 股 100 股)格点**造成的度量失真,有没有被当成特征而不是噪声来用过
    (「一天访问过多少个价格档位」「成交量落在多少个不同数值上」这一类);
(c) 这类度量**在控制掉成交额水平与波动水平之后**还有没有独立定价能力(我的奖励已经投掉了流动性水平与成交额波动的水平);
(d) **把「滚动回归斜率」当成个股特征**的一般做法 —— Kyle's lambda / Amihud / 价格冲击弹性是怎么估的,
    文献怎么处理 beta = cov/var 被 1/var 主导这件事(标准化、取对数、用 t 值而不是斜率)。这条直接关系到 M3 那 14 个 head 该怎么读。
关键词(EN):zero-volume days; proportion of zero returns; Lesmond Ogden Trzcinka; Liu liquidity measure zero trading days;
price discreteness; tick size and lot size effects; number of distinct prices visited; odd-lot / round-lot trading China;
Kyle lambda estimation; Amihud illiquidity; price impact elasticity rolling regression; scaling of regression slopes as characteristics。
关键词(中):零成交天数;零收益率比例;Lesmond 隐含交易成本;流动性度量;价格离散性;最小报价单位;整手与手数格点;A 股整手交易;
Kyle lambda 估计;Amihud 非流动性;价格冲击弹性;滚动回归斜率当特征;斜率的标准化。

**L3 —— 对准核心 ②(`pow_2(cross_mean(day_wmean(Ret,Ret),5))`:先在多日上带符号平均、再折叠成幅度;§1.2)。
要决定:外围押「持续了几天」(游程 / 自相关)还是「持续得多强」,以及多日窗口该怎么选。**
r2 的 L3 已经确认「先平均再折叠」这个顺序文献没测过,这次只问能指导外围与窗口的部分:
(a) **收益符号的游程 / 连续同向天数 / 符号自相关**作为横截面变量的文献(Frog-in-the-Pan 的信息离散度是计数版,还有别的吗),
    以及「连续几天同向」与「这几天一共动了多大」被分开定价的证据;
(b) 日内漂移 / 订单失衡 / 净买压的**多日持续性**到底有多长 —— 有没有在 A 股上直接估过半衰期 / 持续天数的工作
    (r2 的 L3 只找到台湾的「价格压力很少超过一天」,我需要知道这是否有 A 股反例);
(c) 这类持续性信号在文献里通常**按什么条件分组**(成交量、投资者结构、换手率、规模)才显著;
(d) 「自上一次方向反转以来」这种**事件对齐的窗口**(而不是固定 5 天)有没有被用过。
关键词(EN):return sign runs; consecutive same-sign days; sign autocorrelation cross-section; information discreteness Frog in the Pan;
order imbalance persistence half-life China A-share; intraday drift persistence horizon; event-aligned window since last reversal;
conditional sorts turnover / investor composition。
关键词(中):收益符号游程;连续同向天数;符号自相关;信息离散度;订单失衡的持续性与半衰期;A 股日内漂移的持续期;
自上次反转以来的窗口;按换手率 / 投资者结构分组。

**L4 —— 对准 §1.6 的方向冲突(三个价格水平 head,sign 都是 +1 但底层方向相反)。
要决定:要不要为 r2b 的两个 head 花 R,以及最终库里该留哪一边。**
问:**名义价格水平**在横截面上怎么被定价、以及它和市值 / 彩票偏好的关系?具体想要:
(a) **名义股价本身**(不是市值)作为预测变量的证据与方向(名义价格幻觉、低价股效应),
    尤其是**控制掉市值之后**名义价格还剩什么(我的控制里有 `LogFloatCap`、没有价格,所以 `LogFloatShares` ≈ −log 价格);
(b) A 股上低价股 / 高价股的实证方向与时期依赖(有没有按年份翻转的报告)—— 我手上两个方向相反的 head 在 2018–2023 上都过线,需要外部判据;
(c) 名义价格与**彩票偏好 / 散户持股比例 / 涨跌停触及频率**的交互;
(d) 文献里对「只在部分截面上定义的信号」(把最低 10%~20% 温莎化 / 压到均值再做截面回归)有什么处理惯例与警告 ——
    这关系到 (N-e) 的 `cs_mask_top_replace_mean_neg` 到底算正当的稳健化还是在扰动中性化回归。
关键词(EN):nominal share price cross-section of returns; nominal price illusion; low-price effect; penny stock premium;
price level controlling for market capitalization; lottery preference and nominal price; retail ownership and share price;
winsorization before cross-sectional regression; partial-sample signals。
关键词(中):名义股价与横截面收益;名义价格幻觉;低价股效应;控制市值后的价格水平;彩票偏好与股价;散户持股与股价;
截面回归前的温莎化;只在部分样本上定义的信号。

---

## 6. 给 PI 的三条提醒(不是本角色该决定的,但影响任务书怎么写)

1. **E 的家族控制 ≠ 最终库的去重集合。** E 奖励只把「含该核心的 ≤6 个 head」放进控制,
   而 PLAN §3 的最终库要和**之前收下的全部 head** 比 ρ(≥0.7 或 ≤−0.5 就丢),而且 **M 的四批先收**。
   所以一个在 E 口径下高分的 head,完全可能在最终库里被 M 的某个 head 杀掉(r1a 的 7 个很可能就是这样,§1.6)。
   选核心时要同时看「家族控制轻不轻」和「它的产出会落在库里哪个已经很挤的区域」。
2. **本轮是最后一轮,R 是 B 组唯一还能改动 M 的 head 的工具**,而 M3 的 14 个 head 里有 5 个挂在负必要性的部件上、
   5 个挂在一个除零极点上。A 组的六条(尤其 A1、A2、A4)是本轮期望收益最高的支出。
3. **两条预测写法上的教训**:第 1、2 轮各有一条预测(N3)因为「定位输出里没有这个量」而无法核对。
   本轮的事先预测请只写定位工具下一轮一定会打印的量(head 表、拆解表、R_prev 的 score / ρ / replaces、missions_before 的 passers / heads / sampling)。
