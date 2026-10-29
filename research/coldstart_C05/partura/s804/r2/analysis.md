# 结构解剖:种子 804,B 组,第 2 轮

输入:`r2/loc.md` / `r2/loc.json`(快照 = M 第 1 批 + M 第 2 批 + `c05s804Br1a_Ea` + `c05s804Br1b_Nb`,16 个 head,378 个已评分候选,38 次拆解评估,1 个 R 替换已生效)、
`r2/R_prev.json`(第 1 轮 16 次 R 直接评估)、`r1/analysis.md`、`r1/lit.md`、`r1/missions.yaml`、`notebook.md`。
算子与评分口径从源码读出;所有量级核验都是在本地用**纯合成张量**做的(没有碰任何面板数据,也没有碰任何测试段数字)。

---

## 0. 口径:三条机械事实,是下面所有判断的支点

**(a) hl 与 sign 是按 train 夏普网格选出来的,score = min(train, valid)。**
`partura/steer.py:630-648`:对 `long_neutral`,半衰期 hl ∈ {0, 2, 5, 10, 20} 与方向 sign ∈ {+1, −1} 的 10 个组合里,
选 **train 的 long_sharpe 最大**的那个,然后 `score = min(train, valid)`。所以:
① valid 是一个完全自由的读数,不参与任何选择 —— 这就是为什么几乎所有 head 都是 valid > train;
② 两个秩等价的表达式,只要 hl 落到不同的格子,score 就能差很多(§1.2 的 `sqrt` 正是这种情况)。

**(b) 平滑在取秩之前,所以 hl > 0 时外层单调变换不是恒等。**
`raw → bk.smoothed(raw, hl)`(对**原始数值**做 EMA)→ `_zrank` → 对 5 个控制做日度正交投影(`neutral_residual`)。
合成面板量核:hl = 5 时,外面套一个 `sqrt` 会让 **22.8%** 的格子的截面秩发生变化;hl = 0 时是 **0%**。
(第 1 轮写「取 z-rank 再回归,所以单调变换等价」只在 hl = 0 时成立 —— 这一条要修正。)

**(c) 交易的是残差书,不是原信号的十分位书。**
下面 §1.4 用快照里两个**原信号十分位完全相同**、score 却差 0.67 的真实变体把这一条钉死。
后果:凡是「把某一段名字从分布的上半挪到下半」这类改写,改变的主要不是多头持仓,而是投影之后的整本书 ——
从段宽算术推出来的「经济机制」都要打折。

---

## 1. alpha 的来源

### 1.1 本轮最强的新东西:G,一条带尺度的回归斜率(真来源,但「尺度嫌疑」很重)

把 `c05s804Br1a_Ea` 的 5 个 head 化简,共同的真来源是

```
G = ts_regbeta(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50)
```

**充分性**:G 单独当因子 score **+1.44**(train +1.44 / valid +2.99)—— 是整个快照里自身分数最高的表达式,比它所在的 head(+0.84)高 0.60。
往外每套一层都在扣分:`cs_first_high20(day_autocorr_n1(pow_05(Amt)), G)` = +1.35 → `sqrt(·)` = +1.10 → `cs_bucket_rank(·, ListAge)` = +0.84。

**必要性**:把 G 整段跳掉(换成 `day_median(Volume)`)→ **−2.56**,必要性 **+3.40**;
把里层 `cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3)` 跳掉(剩 `ts_regbeta(day_median(Volume), day_mean(Open), 50)`)→ **−1.46**,必要性 **+2.29**。
被排序的那一项 `day_autocorr_n1(pow_05(Amt))` 单独 **−0.36**,中间那两层 t 值单独是 **−1.20** / **−0.50** ——
又一次是「被筛选 / 被排序的量本身没用,全部 alpha 在那一步算子里」。

**敏感性**:窗口 50 → 25 为 +0.56、50 → 100 为 +0.57(train +0.81),两边各掉约 0.28 —— 中等敏感,50 不是随便哪个窗口都行;
字段 `Volume → Amt`(head 层面)+0.84 → **+0.97**,`Amt → Volume` → +0.77。

**共性**:`day_median(Volume)` n = 26、均值差 +0.64、p 0.009;`day_autocorr_n1(pow_05(Amt))` n = 18、+0.91、p 0.000;
G 的 t 值孪生 `ts_reg_tvalue(day_median(Volume), ..., 50)` n = 11、+0.37、p 0.149。

**算子读通**(`alphacube/operators/common.py:643` `rolling_ols`,`dt_cross.py:299-320`,`nd_ts.py:273-290`):
`reg*(x, y, d)` 是**把 y 回归到 x 上**,`beta = cov/var_x`,`tvalue = beta / sqrt(mse/var_x)`;`cross_*` 沿日轴滚动,
`day_topw_mean(y, w)`(`ops_ext.py:635`)= |w| 最大的那 10% 分钟里 y 的均值,所以 `day_topw_mean(Amt, Ret)` = **波动最大的 10% 分钟里成交的金额**(有钱的量纲)。
于是 G 读作:「波动分钟的成交金额 ↔ 价格」的 3 日共动强度,再套一层同样的 3 日共动,最后与**中位分钟成交量**做 50 日回归斜率。

**真来源还是代理?** 这里有一条非常干净的分离证据:**同一个位置上,`ts_regbeta` 是 +1.44,`ts_reg_tvalue` 是 −0.14**(head +0.73 的充分性行)。
两者只差一个因子:`beta = corr · σ_y / σ_x`,而 `t ≈ corr / sqrt((1−corr²)/df)` 把 σ 全除掉了。
也就是说 **alpha 不在共动的方向 / 显著性里,而在 σ_y / σ_x 这个尺度因子里**,其中 `σ_x = ts_stddev(day_median(Volume), 50)`。
合成核验:当各股票只在 σ_x 上不同、corr 与 σ_y 同分布时,`spearman(|beta|, 1/σ_x) = 0.55`,而 `spearman(beta, 1/σ_x) ≈ −0.06` ——
**符号由 corr 定,能走到截面两端(也就是纯多头书真正买到的那一头)的却是 σ_x 小的名字**。
`ts_stddev(day_median(Volume), 50)` 是「成交量水平的时序离差」,是流动性的一个**非线性函数**;
控制里有 `cross_mean(day_sum(Amt), 30)`、`cross_mean(day_std(Amt), 30)`、`LogFloatCap`,但都是 z-rank 的**线性**投影 ——
这正是第 1 轮给价格尾部下的同一个诊断:**线性控制拿不掉的非线性流动性暴露**。
结论:G 是本批最有力的新结构,但它有可能大半是「1/成交量离差」的另一种写法。**这一条必须先用 R 的直接评估钉死,再决定要不要给它一个 E 位**(§4.2 第 1 组、§4.1 核心 ②)。

### 1.2 head +0.84 的三层外壳全是负担,其中 `sqrt` 是 hl 伪影,不是机制

- `cs_bucket_rank(·, ListAge)`(`ops_ext.py:239`,在 ListAge 的同一个十分位里取 y 的百分位秩):+1.10 → +0.84,**扣 0.26**。
- `sqrt(·)`:+1.35 → +1.10,**扣 0.25**;而拆解里「跳掉 sqrt」那一行写的是必要性 **+0.28**(score +0.56,train +0.92 / valid +0.56)。
  这两件事看起来矛盾,读源码就清楚了:`cs_bucket_rank` 对 y 的任何单调变换**完全不变**(合成核验:`max |rank(y) − rank(sqrt(y))| = 0.0`),
  所以 `sqrt` 在信号层面是恒等的;它唯一的作用通道是 §0(b) 的「EMA 在取秩之前」。
  「跳掉 sqrt」那一行 train 反而从 +0.84 升到 +0.92、valid 从 +2.35 塌到 +0.56 —— 这是 **hl / sign 网格按 train 选、valid 自由落体**的典型形状。
  **判断:`sqrt` 的 +0.28 必要性是伪影,不能当证据;但在最终评分口径下它确实值 0.25 分,所以该不该删要看是不是想赌 hl。我倾向连 `sqrt` 一起剥掉,直接用 G。**
- `cs_first_high20(day_autocorr_n1(pow_05(Amt)), ·)`:+1.44 → +1.35,扣 0.09;被排序项单独 −0.36。

### 1.3 M1 的价格 / 股本轴:第 1 轮的 R 已经把它钉死了(两个假说一个成立、一个被否)

16 次 R(`R_prev.json`)对第 1 轮的结论:

| 变体 | score | 读数 |
|---|---|---|
| `sub(cs_first_low20(abs_(day_wstd(Vwap, High)), pow_3(day_mean(Open))), ts_var(day_gini(High), 10))` | **+0.878** | 去掉有害的 `ts_decay_linear`,**已替换**原 head(+0.755) |
| `cs_first_low20(day_wstd(Vwap, High), day_mean(Open))` | **+0.878** | 最简形与上面**完全同分**(ρ_head 0.986)⇒ `abs_`、`pow_3`、`ts_var(day_gini(High), 10)` 三个部件确实是纯装饰 |
| `cs_first_low20(day_mean(Open), day_mean(Open))` | +0.830 | 段内改按价格本身排序只差 0.048 ⇒ **`day_wstd(Vwap, High)` 基本是价格的代理** |
| `cs_first_low40(day_wstd(Vwap, High), day_mean(Open))` | **−0.457** | **段宽就是全部**:20% → +0.878,40% → 负 |
| `cs_last_low05(cs_first_low20(day_wstd(Vwap, High), day_mean(Open)), day_mean(Open))` | +0.855 | 显式剔除最便宜 5%:**略差** |
| `cs_last_low10(cs_first_low20(day_wstd(Vwap, High), day_mean(Open)), day_mean(Open))` | **+0.164** | 显式剔除最便宜 10%:train 崩(valid 仍 +2.21) |
| `cs_first_low20(LogFloatShares, day_mean(Open))` | +0.826 | 裸股本 + 当日价格 ≈ 原 head(+0.78)的全部 |
| `sub(sub(LogFloatShares, cs_first_low20(LogFloatShares, day_mean(Open))), cs_first_low20(LogFloatShares, day_mean(Open)))` | +0.902 | head +0.915 的裸字段最简形,差 0.012 ⇒ 双重 `cross_ema` 无用 |
| `cs_last_low20(neg(day_mean(Open)), day_mean(Open))` | +0.830 | 与 `cs_first_low20(day_mean(Open), day_mean(Open))` 同分、ρ_head = **−0.62** ⇒ 这是**方向相反的孪生**,按 PLAN §3 的合库规则(ρ ≤ −0.5 也丢)会被丢掉,不要再造这种 |
| `day_centroid(sqrt(Volume))` / `day_centroid(Volume)` | +0.060 / −0.087 | **质心单独毫无价值** |
| `sub(ts_mean(abs_(pow_1_5(cs_last_low10(day_wmean(Ret, Volume), ts_reg_tvalue(day_quantile(Volume), day_mean(Ret), 10)))), 30), day_centroid(sqrt(Volume)))` | +0.370 | A 项确实有贡献(+0.31),但两项都不够门槛 |

**成立的**:装饰部件(`abs_`、`pow_3`、1e-7 的 `ts_var(day_gini(High), ·)` 尾巴、`ts_decay_linear`、双重 `cross_ema`)全是无用或有害 ——
第 1 轮的「烂部件」清单逐条被证实。
**被否的**:「买便宜但不是最便宜」。显式剔除最便宜的一段只会更差(+0.855 / +0.164)。
原因见 §1.4:`cs_first_low20(y, 价格)` 的原信号多头十分位**本来就是价格分位 10–20%**,甜区已经内建;
再往上挪只会把分布形状改坏。

### 1.4 一条必须记住的方法事实:原信号的十分位可以完全相同,score 差 0.67

`cs_first_low20(y, 价格)` 给低价 20% 的名字 +1,所以这 1000 只(约 5000 只的 20%)全部排在其他人之上;
原信号的多头十分位(500 只)= 这个段里 y 最高的一半。
`cs_last_low10(cs_first_low20(y, 价格), 价格)` 把最便宜的 10% 压到最底,剩下的段成员恰好是**价格分位 10–20% 的那 500 只**;
而 `cs_first_low20(价格, 价格)` 的多头十分位也**恰好是价格分位 10–20% 的那 500 只**。
合成核验(N = 5000):两者的原信号多头十分位重合度 **100%**,价格分位区间都是 [0.100, 0.200]。
可是它们的 score 是 **+0.164 对 +0.830**(sign、hl 都是 +1 / 5)。
⇒ 差别完全来自 §0(c):书是 z-rank 对 5 个控制投影之后的**残差**书,**分布下半部分的名字放在哪里会改写整本书**。
这对本种子有两个直接后果:
1. 任何从「段宽 / 指示函数算术」推出来的经济解释(包括第 1 轮的「避开最烂的一头」)都不可靠,只能当假说;
2. 「把一段名字挪到分布另一端」这类改写是**一个独立的自由度**,GP 和 R 都可以拿它换分 —— 这既是机会,也是过拟合的入口。

### 1.5 真正干净的新来源:日内「时点错配」`sub(day_centroid(Volume), day_centroid(Ret))`

第 1 轮 N 位的最好产出(score **+0.88**,train +0.88 / valid +1.05,sign −1,hl 20)。

- **充分性(关键)**:两条腿单独都没用甚至有害 —— `day_centroid(Volume)` **−0.09**、`day_centroid(Ret)` **−1.38**;
  第 1 轮 R 又独立量过 `day_centroid(sqrt(Volume))` = **+0.06**、`day_centroid(Volume)` = **−0.09**。
  **整个快照里只有这一个 head,它的分数无法由它的任何一个部件复现 —— 它是一个真正的交互项,不是某个单项的包装。**
- **敏感性**:`Volume → Amt` → +0.90(+0.02),稳。没有窗口可动。
- **代理嫌疑最小**:`day_centroid`(`ops_ext.py:155`)是 |x| 沿分钟轴的质心除以 (T−1),**尺度无关、有界在 [0,1]**,
  所以成交量 / 市值的量纲进不来。对照 `day_cov(in_index(Volume), Volume)`(head +0.67 的主项)带着成交量量纲,就有尺度嫌疑。
- **时段风险最小**:valid / train = 1.19;价格族是 2.0–4.3,G 族是 2.7–2.8。这是库里最不像「只吃 2022-01 ~ 2023-08 一段行情」的 head。
- **机制读法**:`day_centroid(Ret)` 用的是 |Ret|,所以它是**波动发生的时点**;整条信号 = 成交时点 − 波动时点,sign −1 ⇒
  多头是**成交偏早、波动偏晚**的股票。这是一个「量领先波动」的日内领先滞后量,文献里有对应的东西(§5 题 1)。

### 1.6 M2 的两个 head 是**退化**的:`day_signed_ratio(High, Open)` 恒等于 1

`day_signed_ratio(x, y)`(`ops_ext.py:122`)= `Σ|y|·sign(x) / Σ|y|`。分钟 `High`、`Close`、`Low` 都是**正的价格**,`sign` 恒为 +1
⇒ **`day_signed_ratio(High, Open)` ≡ 1.0**(合成核验:四天四个值全是 1.0;`day_signed_ratio(Close, Low)` 同样 ≡ 1.0)。
而 `_pct_rank`(`ops_ext.py:231`)对全部并列的一行返回 `(i+1)/n`,也就是**股票在 store 符号表里的列序**(合成核验:8 只全并列 → 0.125…1.0)。
于是:

- head +0.64 `cs_first_high40(cross_delay(day_signed_ratio(High, Open), 60), ts_stddev(pow_2_5(cs_mask_top_replace_mean(cs_mask_top_replace_mean(day_durbin_watson(Ret)))), 10))`
  = **「列序 + 1{条件变量在最高 40%}」**(合成核验:`cs_first_high40(常数, x)` 返回 0.1…0.6 与 1.7…2.0,正是列序加 band),sign −1;
  `cross_delay(·, 60)` 作用在常数上只剩**一件事**:把 NaN 前移 60 天,等于一个「60 天前有数据」的上市年龄筛子。
- head +0.60 是同一个东西套了两层:里层 `cs_first_high40(常数, 条件变量)`,`cross_delay(·, 60)` 取它 **60 天前**的值,
  外层 `cs_first_high40(z, z)` 对自己做 band(单调)⇒ 实质是「**60 天前的那个 band**」。

**判断:M2 这一批对本种子没有贡献任何可解释的横截面信息。**它真正用到的只有条件变量
`ts_stddev(pow_2_5(cs_mask_top_replace_mean(...day_durbin_watson(Ret))), 10)`(日内收益自相关的 10 日波动,共性 +1.14 / p 0.027 / n = 5),
段内选谁则由一个**时间上恒定的任意标签**(列序)决定 —— 这个标签不是随机数:A 股的符号表若按代码排序,代码本身编码交易所 / 板块 / 上市年代,
所以它是一个**偷来的、未声明的截面特征**。这两个 head 的 train 0.64 / 0.60、valid 2.12 / 1.66 都要按这个读法打折。
(我没有去核对 store 的符号表到底怎么排 —— 不论怎么排,结论都是「段内排序不含数据信息」。)

### 1.7 共性表的第二次警告:这一轮有四行是常数

第 1 轮说过共性表在追血脉;这一轮更硬:`day_signed_ratio(High, Open)`(n = 46,均值差 **+0.743**,**p 0.0019**)、
`day_signed_ratio(Close, Low)`(n = 10,+0.842,p 0.050)、`day_signed_ratio(Low, Low)`(n = 15,+0.434)
**全都恒等于 1**;`ts_stddev(day_signed_ratio(Low, Low), 10)`(n = 14,+0.398)**恒等于 0**。
一个 n = 46、p = 0.002 的「强共性子树」可以是一个常数。
⇒ 共性表只能用来挑「n 大 + 与拆解一致」的行;**机械核心卡的 enrichment 部分(第 5–34 条)不可直接当核心用**,
B0 会按卡取,这正是 B 能赢的地方之一。

---

## 2. 烂部件(R 的目标)

| 部件 / 位置 | 证据 | 判断 |
|---|---|---|
| head +0.84 的 `cs_bucket_rank(·, ListAge)` | 剥掉 +0.84 → +1.10 | **纯负担 −0.26**,剥 |
| head +0.84 的 `sqrt` | 剥掉 +1.10 → +1.35;源码上对 `cs_bucket_rank` 是恒等(合成核验差 0.0) | **非机制**;在 hl > 0 的口径下仍值 0.25,连同上一条一起剥到 G |
| head +0.84 / +0.73 的 `cs_first_high20(day_autocorr_n1(pow_05(Amt)), ·)` | 剥掉 +1.35 → +1.44;被排序项单独 −0.36 | 负担 −0.09,可剥 |
| head +0.73 的 `ts_reg_tvalue`(同一位置) | 同位 `ts_regbeta` 单独 +1.44,`ts_reg_tvalue` 单独 **−0.14** | **换算子**,预期 +0.6 以上 |
| head +0.67 `add(day_cov(in_index(Volume), Volume), day_centroid(Ret))` 里的 `day_centroid(Ret)` | 量纲差了几个数量级(cov 带成交量量纲,质心 ∈ [0,1]);存档里 `sub(add(A, c), c)`(= A)得 **+0.667**,`add(A, c)` 得 **+0.669** | **装饰,差 0.002**。所以「剥掉它」不可能够 +0.1 门槛 —— 不要为替换花评估,只值得花在**归一化版本**上 |
| head +0.64 / +0.60 的 `cross_delay(day_signed_ratio(High, Open), 60)` 整项 | §1.6:恒等于 1,秩 = 列序 | **最该换掉的部件**:换成一个真信号(`day_signed_ratio(Ret, Amt)` 才是这个算子的本意:净买压) |
| head +0.64 里重复的 `cs_mask_top_replace_mean` | 两次嵌套(第二次换掉的是第一次之后新的前 10%),信息量低 | 可疑但非恒等,低优先 |
| 价格族(head +0.915 / +0.878 / +0.78 / +0.653)的装饰 | 第 1 轮 16 次 R 已全部清掉或证明无用,`ts_var(day_gini(High), ·)` 必要性 −0.00 三处 | **已做完,本轮不要再花** |
| 已有的唯一机械 R 候选(增益 +0.13) | `cs_bucket_rank(sqrt(cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_regbeta(day_median(Amt), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50))), ListAge)` | 合法但**保留了两层负担外壳**;直接剥到 G(+0.60)更好 |

**一条可利用的不对称**:`scripts/c05_locate.py:296` 的 `r_candidates` 明确写着 `if kind != "sufficiency" and ...` ——
**「剥掉外壳、只留子树」这一类替换永远不会出现在机械 R 候选里**。B0 按机械候选取,所以 §4.2 第 1 组是 B 组白捡的分。

---

## 3. 之前的任务(第 1 轮对账)

### 3.1 E 位 `c05s804Br1a_Ea`,核心 `day_mean(Open)`:产出很好,但**不是价格**

95 次评分、8 个过线、6 个入 heads(全轮最多);采样计数 `{'c05_no_core': 701, 'c05_periphery_seen': 3}` ——
生成器为了塞进核心被拒 701 次,而「外围必须没见过」这条几乎没有约束力(只拒了 3 次)。

**核心在不在实质位置?不在,而且是被算子整除掉的。** `day_mean(Open)` 在产出里只出现在两种位置:
1. `cross_reg_tvalue(day_mean(Open), ·, 3)` —— `beta = cov/var_x`、`t = beta/se_beta` 都只看窗口内的离差,
   **每只股票各自的价格水平和幅度被整除掉**。合成核验:把价格换成 `a·价格 + b`(每只股票各自的 a、b)后,3 日 t 值的相对变化中位数 **3.4e-04**、p99 2.6%,只剩 float32 舍入。
   第 1 轮的来源 A 是「价格的**截面水平**」,而这里进去的只有 3 日价格变动的相关形状 —— 两件完全不同的事。
2. `cs_flip_by_state(LogFloatShares, day_mean(Open))`(`ops_ext.py:562`)—— 第二个参数只用来算**全市场均值**与它自己 241 日中位数的比较,
   是一个市场级的开关,也不是截面价格。

**结论**:第 1 轮笔记里写的风险(「GP 长出核心只是一个无关紧要的价格叶子的树」)**完全命中**,而且比担心的更彻底:
不是「无关紧要」,是算子在数学上把核心除掉了。
**但这个 E 位并没有浪费**:奖励里已经加了含核心的 4 个价格 head 当控制,所以它长出来的东西**必须**是价格族之外的新信息 ——
它找到了 G(自身 +1.44,快照最高),是本轮最有价值的新结构。
**给 PI 的设计教训**:「原样包含核心」这条约束可以被**消去核心的算子族**(`*_reg*` 的 beta / t 值、`cs_flip_by_state` 的第二参、任何只用核心的截面均值的位置)
形式上满足。要么在 E 的种子里把核心放在**秩 / 分段 / 桶**这类保留截面序的位置上并在 hypothesis 里写明,
要么接受「E 位有一半概率退化成一次带锚的自由搜索」—— 后者这一轮的结果其实不差。

### 3.2 N 位 `c05s804Br1b_Nb`,日内成交时点:方向对了,机制不是「质心」

81 次评分、5 个过线、3 个入 heads。
预测对账:① 产出 ≥ 1 个 head 概率 0.45 → **有 3 个**;② 方向「买成交偏早盘的」→ **对**(三个 head 的 sign 都是 −1);
③ score 0.5–0.8 → 最好的是 **0.88**,略高于预期;④ valid/train 比价格族更接近 1(< 2)→ **对**(1.19 / 0.53 / 1.98);
⑤「最可能是 10–20 日平滑过的时点特征(早盘成交占比,或最重分钟的位置)」→ **不对**:过线的既不是 `in_half` 占比也不是 `day_topw_mean(in_index(Volume), Volume)`,
而是**两个时点的差**;只有 `ts_mean(cs_bucket_rank(day_centroid(Volume), LogFloatCap), 10)` 用到了 10 日平滑。
⑥ 质心单独 ≥ 0.5 的概率 0.4 → **错得很干脆:+0.06**。
**最有价值的一条对账**:第 1 轮把 head +0.58 的主项读成「−2×质心」,并据此认为质心是一条独立来源 —— 这是错的。
质心单独几乎是 0;真东西是**质心之间的差**(§1.5)。条件计划里写的「若 N 位出了时点类 head,第 2 轮把时点子树当 E」条件已满足。

### 3.3 R:16 次,1 个替换成立,预测大体准(明细见 §1.3)

预测准的:去 decay 版 +0.878 且替换成立(预测 0.9)、最简形 ≥ 0.855(0.6)、段内按价格排序与最简形差 < 0.1(0.5)、
段宽 40% 更差(0.6)、head +0.915 裸字段最简形差 0.05 以内(0.7)、head +0.78 最简形落在 0.75–0.85(主预测)、A 项有贡献(0.4)。
预测错的:「剔除最便宜 5% / 10% 更好」(0.45)→ 反而更差;「`cs_last_low20(LogFloatShares, 价格)` ≥ 0.5」(0.6)→ 0.425;
「质心单独 ≥ 0.5」(0.4)→ 0.06。
**净判断:关于「哪些部件是装饰」的预测几乎全中(这类判断来自读源码和量级);关于「经济机制」的预测(甜区在次便宜、质心是来源)全错。**
这与 PLAN §1 对 C01–C04 的总结一致,本轮继续按这个权重分配信任。

---

## 4. 本轮候选

### 4.1 值得深挖的核心(≤ 3,按推荐度)

**核心 ①(首选):`sub(day_centroid(Volume), day_centroid(Ret))`**(整个 head 当核心,PLAN 修订 3 允许;score +0.88,sign −1,hl 20)

- 为什么选它:§1.5 —— 快照里**唯一**一个分数不能由任何部件复现的 head(两条腿单独 −0.09 / −1.38),
  **唯一**一个尺度无关、因此没有流动性 / 规模代理嫌疑的 head,**唯一**一个 valid/train ≈ 1.2 的 head;
  而库里 16 个 head 的分布是:价格 / 股本轴 4 个(+0.91 / +0.88 / +0.78 / +0.65),G 族 5 个,退化的 M2 2 个,时点轴 3 个,另外 2 个各自孤立 —— M1 的 +0.58(质心 + A 项的组合,两项单独都不过线)和 E 的 +0.55 `cs_bucket_rank(sqrt(cs_flip_by_state(day_mean(Open), day_mean(Open))), ListAge)`(其实还是价格的秩,只是符号随市场状态翻转)。按最终合库(ρ ≥ 0.7 或 ρ ≤ −0.5 丢)算,时点轴是唯一还有空位的方向。
- E 位预算:这个核心用过 0 次(`day_mean(Open)` 已用 1 次)。
- **周围已经见过的外围(E 必须避开的集合)**:严格地说**一个都没有** —— 快照里只有这一个候选原样含它(它自己),外面什么都没有。
  为了不重新发现同一个东西,下面是这两条腿周围已经见过的写法,种子应当避开:
  1. `cs_bucket_rank(day_centroid(Volume), day_centroid(Ret))`(+0.71,存档);
  2. `ts_mean(cs_bucket_rank(day_centroid(Volume), LogFloatCap), 10)`(head +0.67);
  3. `add(day_cov(in_index(Volume), Volume), day_centroid(Ret))` 与 `sub(add(·), day_centroid(Ret))`(head +0.67 及其孪生);
  4. `day_centroid(sqrt(Volume))`、`day_centroid(Amt)`、`day_corr(in_index(Volume), Volume)`、`day_sum(in_half(Volume))`(第 1 轮 N 的种子与存档);
  5. `sub(day_centroid(Volume), ts_mean(day_centroid(Volume), 20))`(第 1 轮 N 种子)。
- **没见过、值得长的外围方向**(供 PI 写种子):把错配量**按条件分组 / 交互**(`LimitWidth`、`BoardCode`、`ListAge`、`sub(LogTotalCap, LogFloatCap)` 这四个叶子在 378 个候选里出现 **0 次**);
  用错配量**当分段条件**而不是被排序量(`cs_first_low20(y, 核心)` / `cs_last_high20(y, 核心)`);
  错配的**时序性质**(自身 20 / 60 日分位、相对自身习惯的偏离、符号的持续性);
  与**价格段**交互(把时点错配只用在低价段里 —— 这是把库里两条最强的轴乘起来,而且两条轴的 head 都已在控制里,只有交互项能拿分);
  第三条腿(把 `day_centroid(Ret)` 换成波动 / 价差 / 净买压的时点,构成「量 − 波动」「量 − 买压」两种错配的对照)。
- **必须写进 hypothesis 的风险**:核心被消去(§3.1)。它是一个有界 [−1, 1] 的量,一旦被包进 `cross_reg*` / `ts_reg*` 的任一参数位或 `cs_flip_by_state` 的第二参,
  截面序就没了。种子要把核心放在秩 / 段 / 桶 / 同量纲加减的位置上。
- 弱点(要如实告诉 PI):奖励控制里能加的「核心家族」只有 1 个 head(就是它自己),比第 1 轮 E 的 4 个弱,
  所以更容易长出与原 head 近似的东西,只能靠库禁令(ρ ≥ 0.7、骨架相同)兜底。

**核心 ②:`ts_regbeta(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50)`**(机械核心卡第 1,自身 +1.44)

- 为什么:快照里自身分数最高,必要性 +3.40,是 5 个 head 的共同来源。
- **已见外围**:`cs_first_high20(day_autocorr_n1(pow_05(Amt)), ·)`、`sqrt(·)`、`cs_bucket_rank(·, ListAge)`、
  `cs_bucket_rank(·, day_mean(Open))`、以及 head +0.59 里把整条链再自嵌一次。外围很窄,空间大。
- **但是**:§1.1 的尺度嫌疑没解决之前不建议占 E 位。**建议顺序:先用 §4.2 第 1 组的 3–4 次直接评估判定,若「尺度项单独」就能拿到 +1 以上,
  那么这个核心大概只是 1/成交量离差的写法,E 位会被浪费;若尺度项单独很弱,它就是本实验最值得深挖的核心,第 3 轮再上。**
- 另一个考虑:它正好在机械核心卡第 1 位,所以 B0 第 2 轮大概也会挖它 —— B 组去挖它,主比较上拿不到差异;去挖核心 ①(不在机械卡上)才有区分度。

**核心 ③:`cs_first_low20(abs_(day_wstd(Vwap, High)), pow_3(day_mean(Open)))`**(机械核心卡第 4,自身 +0.87)

- 为什么:它是价格段那一整本书,字段互换 ±0.01、装饰部件全部证明无用、外围只见过 `sub(·, ts_var(day_gini(High), 10))` 一种,外围几乎空白。
- 为什么排第三:价格 / 股本轴已有 4 个 head 且 valid/train 2.1–4.3(时段风险);§1.3–1.4 说明这一轮能对它做的「机制检验」基本已经做完,
  剩下的自由度主要是「把分布下半挪来挪去」这种过拟合入口;而且第 1 轮在同一条轴上的 E 已经交付过一次(虽然核心是更小的 `day_mean(Open)`)。

### 4.2 R 目标(≤ 16 次直接评估;替换要求 score ≥ 原 head + 0.1、ρ_head ≥ 0.5、|ρ_known| < 0.5)

**第 1 组(最高优先,几乎白捡;对准 head +0.839,门槛 ≥ +0.939)**

1. `ts_regbeta(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50)`
   —— 剥掉三层外壳,**分数已知 +1.44**,只差 ρ_head / ρ_known 的确认;机械 R 候选不含 sufficiency 行,所以必须我们自己提。
2. `cs_first_high20(day_autocorr_n1(pow_05(Amt)), ts_regbeta(day_median(Volume), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50))`
   —— 已知 +1.35,作 1 的备选(若 1 的 ρ_head < 0.5)。
3. `ts_regbeta(day_median(Amt), cross_reg_tvalue(day_mean(Open), cross_reg_tvalue(day_mean(Open), day_topw_mean(Amt, Ret), 3), 3), 50)`
   —— `Volume → Amt` 的最简形(head 层面这个 swap 是 +0.84 → +0.97)。

**第 2 组(对准 head +0.729,门槛 ≥ +0.829;同时是核心 ② 的尺度判定)**

4. 第 1 组第 2 条同一表达式,挂在 head +0.729 下 —— 把 `ts_reg_tvalue` 换成 `ts_regbeta`,预期 +1.35(+0.62)。
   ⚠️ 提醒 PI:4 与 1 的结果彼此 ρ 很可能 ≥ 0.7,最终合库只会留一个,**不要指望两个替换都变成两个独立 head**;要的是把两个 head 各自升级。
5. `ts_stddev(day_median(Volume), 50)` —— **纯尺度项单独**。这是判定 §1.1 的那一刀:若它自己就 ≥ +1,核心 ② 基本等于「1/成交量离差」。
6. `ts_regbeta(day_median(Volume), day_topw_mean(Amt, Ret), 50)` —— 去掉两层 3 日 t 值、只留同一个尺度与一个简单的 y。
   5 与 6 合起来能把「尺度 / 共动 / 嵌套」三者分开。

**第 3 组(对准 M2 的两个退化 head;head +0.64 门槛 ≥ +0.74,head +0.60 门槛 ≥ +0.70)**

7. `ts_stddev(pow_2_5(cs_mask_top_replace_mean(cs_mask_top_replace_mean(day_durbin_watson(Ret)))), 10)` —— 条件变量单独(head +0.64 真正用到的全部东西)。
8. `cs_first_high40(day_signed_ratio(Ret, Amt), ts_stddev(pow_2_5(cs_mask_top_replace_mean(cs_mask_top_replace_mean(day_durbin_watson(Ret)))), 10))`
   —— 把恒等于 1 的被排序项换成这个算子**本意**的用法(净买压 = 上涨分钟成交额占比 − 下跌分钟占比),head +0.64。
9. `ts_stddev(pow_2_5(cs_mask_top_replace_mean(day_durbin_watson(Ret))), 10)` —— 条件变量单独、单层 mask(head +0.60)。

**第 4 组(时点轴的尺度检验;对准 head +0.669,门槛 ≥ +0.769)**

10. `day_corr(in_index(Volume), Volume)` —— `day_cov` 的归一化版本。按 §2,`day_centroid(Ret)` 那一项值 0.002,所以这一次评估问的是
    「head +0.669 到底是『量后置』还是『成交量量纲』」:若归一化版本也 ≥ +0.77,说明是形状;若明显更差,说明这个 head 是又一个非线性流动性代理。

**第 5 组(可选,还有余量时;对准 head +0.674,门槛 ≥ +0.774)**

11. `ts_mean(cs_bucket_rank(day_centroid(Volume), LogFloatCap), 20)` —— head +0.674 是库里**唯一** train(+1.26)> valid(+0.67)的 head,
    平滑窗口加倍看 valid 能不能跟上(窗口替换)。
12. (纯方法性,只在 PI 认为值得时做)`cs_last_high40(cs_first_low20(day_wstd(Vwap, High), day_mean(Open)), day_mean(Open))`
    —— 只改动分布**下半部分**、完全不改多头持仓,用来在第二个族上验证 §1.4 的发现(残差书对分布形状的敏感度)。
    不要指望它替换任何 head;它买的是下一轮的判断力。

合计 10–12 次,留 4–6 次余量。**不要**再花在价格族的装饰上(第 1 轮已做完),也不要花在
`sub(day_centroid(Amt), day_centroid(Ret))`(已知 +0.90,增益 +0.02,不够门槛)和 `day_cov(in_index(Volume), Volume)` 单独(已知 ≈ +0.667)上。

### 4.3 N 的灵感(按与证据的贴合度)

1. **四个从未出现过的制度 / 结构叶子。** `LimitWidth`、`BoardCode`、`LogTotalCap` 在 378 个候选、40 行共性、16 个 head 里出现 **0 次**,`LogFloatCap` 只出现 2 次。
   其中 `sub(LogTotalCap, LogFloatCap)` = log(总市值/流通市值) = **限售 / 非自由流通比例**,由两个叶子直接算出、**不在控制里**;
   `LimitWidth` 是涨跌幅制度(10% / 20%),`BoardCode` 是主板 / 科创 / 创业 / 北交的分类标签(`dailyfields.py:68`)。
   这和本轮的两条机械发现正好对上:(a) 这个奖励偏爱「只在某一段里下单」的结构(M1、M2、E 三批独立找到 `cs_first_*` 这个母题);
   (b) 库里最强的一族吃的是价格 / 微盘的**非线性尾部**,而制度分段正是把这个尾部切开的自然条件。
   N 可以是「用这四个从未用过的制度 / 结构标签做分段与交互」。
2. **「尺度 vs 共动」的显式搜索**(来自 §1.1)。既然同一位置上带尺度的 `beta` 是 +1.44、去掉尺度的 `t` 是 −0.14,
   那么「某个量的时序离差本身」可能就是一条未被控制住的轴。N 可以显式去搜离差 / 离差之比(量的离差、金额的离差、波动的离差、它们的比值),
   并把归一化版本与未归一化版本同时放进种子当对照。风险要写明:这很可能就是流动性的非线性代理,而流动性已在控制里(只是线性)。
3. 时点错配的其它读法(量 − 买压、量 − 价差、最重分钟的位置之差)—— 如果 E 位取了核心 ①,这条**不要**再占 N 位,会和 E 抢同一片信息。

---

## 5. 给文献员的题目(≤ 4)

> 约束:只能用 **2023-08-08 之前发表**的文献,每条注明年份。第 1 轮已经查过「名义股价水平」「股本 / 自由流通比例 / 非线性规模」
> 「条件排序与段宽」「日内成交量分布」四题(见 `r1/lit.md`),下面四题刻意避开已查过的部分。

**题 1(对准核心 ①,§1.5):日内「成交时点」与「波动时点」的错配 —— 两个时点之差作为截面预测变量**
问:文献里有没有把**成交量的日内时点**与**波动 / 收益的日内时点**之差(领先滞后、错配、不同步)当成一个变量?
怎么构造(质心、持续期、时段占比、量与 |收益| 的互相关的峰值位置)、怎么归一化(是否除以当日总量、是否按股票自身历史去均值)、
符号是什么(量领先波动 vs 波动领先量,哪一边之后收益更好)、与规模 / 流动性 / 换手怎么分离、用什么持有期?
量-波动关系(mixture-of-distributions / 信息到达)这一支文献里,**不同步**本身有没有被解释为知情交易或流动性提供的代理?
关键词:日内成交时点、成交与波动的领先滞后、量价不同步、成交质心、信息到达率、知情交易时点、日内量波关系;
intraday timing of volume versus volatility, volume-volatility lead-lag, volume-volatility asynchrony, intraday volume centroid vs return-variance centroid,
mixture of distributions hypothesis, information arrival, informed trading timing, cross-sectional predictor from intraday timing mismatch.

**题 2(对准核心 ② 与灵感 2,§1.1):滚动回归系数当特征 —— beta、t 值还是相关系数?尺度(1/σ)是不是就是流动性代理?**
问:把**滚动回归的斜率**当成横截面特征时,文献的做法是什么:用 beta、t 值、相关系数还是 R²?
有没有明确讨论过 `beta = ρ·σ_y/σ_x` 里那个 **1/σ_x 的尺度因子**会把变量变成「1/成交量」「1/波动」这类量纲量,从而变成流动性 / 规模的代理?
Amihud 式的非流动性指标(|收益|/成交额)本身就是一个斜率 / 比值型的量 —— 文献怎么把「量价弹性 / 斜率」与「非流动性」分开?
标准做法是先标准化再回归、还是用无量纲的相关系数?有没有证据说这类斜率特征的预测力在控制了规模 / 流动性 / 特质波动之后还剩多少?
关键词:滚动回归斜率、量价弹性、非流动性指标、Amihud、价格冲击系数、特征标准化、量纲、规模代理;
rolling regression beta as a characteristic, price impact slope, volume-return elasticity, Amihud illiquidity as a slope, Kyle's lambda,
beta versus t-statistic as a predictor, scaling/units of regression-based characteristics, size and liquidity proxies in slope measures.

**题 3(对准 §1.4 这条方法发现):中性化 / 控制的方式本身会不会改变一个尾部异象的结论?**
问:同一个信号,用不同的中性化方式(对特征的秩做线性回归取残差、在分组内重排、双重排序、非参数 / 分位回归、
把尾部指示函数显式加进控制)得到的结论差多少?文献里有没有报告过**控制方式的敏感性**?
纯多头(long-only)分位组合与多空组合在这件事上的差别呢 —— 对纯多头来说,信号分布**非多头端**的形状会不会通过中性化改写多头持仓?
还有:筛选阈值(最便宜的 5% / 10% / 20%)该怎么定、要不要报告阈值敏感性、极端尾部(退市风险、ST、面值风险)该剔除还是该保留?
关键词:中性化方法、残差化、分组内中性、双重排序、纯多头组合、尾部筛选阈值、阈值敏感性、ST 与退市风险剔除、稳健性检验;
neutralization method sensitivity, residualizing on characteristic ranks versus within-group sorts, long-only versus long-short portfolio construction,
screen threshold choice and sensitivity, penny-stock / delisting-risk filters, robustness of tail anomalies to control specification.

**题 4(对准灵感 1,§4.3):A 股的制度 / 股本结构标签当分段条件 —— 限售比例、涨跌幅制度、板块**
问:2023-08 之前的文献里,**限售 / 非自由流通股比例**(总股本与流通股本之差)、**涨跌幅限制的宽度**(10% 与 20% / ST 的 5%)、
**上市板块**(主板 / 创业板 / 科创板 / 北交所)、**解禁事件**这些 A 股特有的制度标签,被当成横截面预测变量或**分组条件**时是怎么用的?
它们与规模 / 流动性 / 价格的关系被如何分离?有没有证据说某个异象只在某一类板块 / 某一种涨跌幅制度下存在?
涨跌幅限制本身对收益分布与动量 / 反转的影响有哪些已知结论?
关键词:限售股比例、自由流通比例、解禁、涨跌幅限制、涨跌停、科创板、创业板、北交所、ST 制度、分板块异象、制度分段;
China A-share price limits, limit-hit effects, free-float versus total shares, lockup expiration, restricted shares,
ChiNext/STAR/Beijing Stock Exchange board differences, ST designation, segment-conditional anomalies in China.
