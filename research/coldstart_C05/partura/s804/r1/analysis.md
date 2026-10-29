# 结构解剖:种子 804,B 组,第 1 轮

输入:`r1/loc.md` / `r1/loc.json`(快照 = M 第 1 批 `c05s804M1_I0_open_search`,5 个 head,124 个已评分候选,46 次拆解评估)。
本种子没有 `notebook.md`、没有前几轮文件(第 1 轮),所以第 3 节为空。

控制口径(从 `scripts/c05_locate.py:94-106` 读出,三组相同):残差 = 信号的 z-rank 对 5 个控制的 z-rank 做日度正交投影后的残差,控制为
`cross_mean(day_sum(Amt), 30)`(流动性)、`cross_mean(day_std(Ret), 20)`(日频波动)、`div(day_last(Close), ts_delay(day_last(Close), 20))`(20 日反转)、
`cross_mean(day_std(Amt), 30)`(已知族)、`LogFloatCap`(市值)。**名义股价本身不在控制里,`LogFloatCap` 在。** 这一条是下面所有判断的支点。
`neutral_residual` 先取 z-rank 再回归(`partura/steer.py:424-440`),所以信号的任何单调变换在最后一层等价 —— `pow_3` 这类外壳只在它被别的算子包住时才可能有作用。

---

## 1. alpha 的来源

### 1.1 先把算子读通(这一批的表达式离不开三个算子)

- `cs_first_low20(y, x)`(`partura/ops_ext.py:509`,转 `_lexi(y, x, -1.0, 0.2, 1.0)`,:339-353):输出 = `rank_pct(y) ∈ (0,1]`,
  **再给 x 处于最低 20%(整个并列块都落在带内才算)的股票加 1**。注释写得很直白:「'trade y only where x is low' as an expression」——
  长端十分位整个来自 x 低的那一段,段内按 y 排序。所以它是一个**条件化/分段**算子,不是普通的二元运算。
- `cross_ema(LogFloatShares, 241)`:`cross_*` 沿**日**轴滚动(`alphacube/operators/dt_cross.py` 头部注释),窗口 241 天 ≈ 一年,
  对象是日频字段 `LogFloatShares = log(FloatShares)`(`alphacube/dailyfields.py:57`)。流通股本一年才动几次,所以这就是「平滑后的流通股本」。
- `day_gini(High)`(`partura/ops_ext.py:136-151`):日内各分钟 `|High|` 的基尼系数,**尺度无关**、有界。
  我在本地用纯合成数做了量级核验(没有碰任何数据):日内振幅 1% / 3% / 10% 时 `day_gini(High)` ≈ 0.0016 / 0.0049 / 0.0158,
  与价格水平无关;再取 10 日方差,`ts_var(day_gini(High), 10)` ≈ **2e-9 ~ 2e-7**。而 `LogFloatShares` 的截面离散度是 O(1)。

### 1.2 把 5 个 head 化简

| head | 化简后等于什么 |
|---|---|
| +0.91 | `sub(sub(E2, C), C)` = **E2 − 2·C**,其中 `E2 = cross_ema(cross_ema(LogFloatShares, 241), 241)`,`C = cs_first_low20(sub(E2, ts_var(day_gini(High), 5)), ts_decay_linear(pow_3(day_mean(Open)), 20))` |
| +0.78 | `rank_pct(cross_ema(LogFloatShares, 241)) + 1{股价最低 20%}` −(约 1e-7) |
| +0.76 | `rank_pct(day_wstd(Vwap, High)) + 1{股价最低 20%}` −(约 1e-7) |
| +0.65 | `rank_pct(|day_corr(Vwap, High)|) + 1{股价最低 20%}` −(约 1e-7) |
| +0.58 | `A − 2·day_centroid(sqrt(Volume))` − 2·(约 1e-7),`A = ts_mean(abs_(neg(pow_1_5(cs_last_low10(day_wmean(Ret, Volume), ts_reg_tvalue(day_quantile(Volume), day_mean(Ret), 10))))), 30) ∈ (0,1]` |

两点细节:`ts_decay_linear(pow_3(day_mean(Open)), 20)` 是**股价水平**的 20 日线性衰减均值(`day_mean(Open)` 是日内分钟开盘价均值 ≈ 当日均价,`pow_3` 单调);
`abs_` 作用在 `day_wstd` 上是恒等变换(`day_wstd` 本来非负,`ops_ext.py:631` 返回 `sqrt(var)`),`neg` 被外面的 `abs_` 吃掉,也是恒等。

### 1.3 真来源 A:股价水平低的那一段(分段筛选),证据最强

**必要性**(拆解,付费评估,最可信的一类证据):

- head +0.76:整段 `cs_first_low20(abs_(day_wstd(Vwap, High)), ts_decay_linear(pow_3(day_mean(Open)), 20))` 跳掉 → score **−1.05**,必要性 **+1.81**。
- head +0.65:同一位置跳掉 → score **−2.78**,必要性 **+3.43**。
- 这两个 head 的 y 单独当因子是**负**的:`abs_(day_wstd(Vwap, High))` = −1.06,`abs_(day_corr(Vwap, High))` = −2.78。
  也就是说,被筛选的那个量本身毫无价值甚至有害,**全部 alpha 在筛选这一步上**。

**充分性 / 方向**:`ts_decay_linear(pow_3(day_mean(Open)), 20)` 单独当因子 score = **−1.15**(train −1.15 / valid −0.46)。
长端买高价股亏钱 ⇒ **买低价股赚钱**,与 `cs_first_low20(·, 价格)` 把低价段顶到长端的方向一致。

**共性**:`ts_decay_linear(pow_3(day_mean(Open)), 20)` 出现在 14 / 124 个候选里,均值差 +1.12,p 0.000;`day_mean(Open)`、`pow_3(day_mean(Open))` 各 15 个,+0.99,p 0.000。
这是共性表里**唯一 n 够大、又与拆解结论一致**的一族。

**敏感性**:`Open→Close` 互换 score 不变(+0.91→+0.91,+0.78→+0.78);`ts_decay_linear` 窗口 20→10 更好(+0.76→+0.80、+0.65→+0.67),20→40 更差(+0.70、+0.63)。
⇒ 对「用哪个价格字段」不敏感(说明来源是**价格水平**,不是某个字段的细节),对平滑窗口轻微偏短 ⇒ 平滑本身不是来源。

**是真来源还是代理?** 这是本轮最需要讲清的一条:

- 不是流动性 / 波动 / 反转 / 已知族的改写:这四项已经被投影掉,而且 5 个 head 都过了与 `cross_mean(day_std(Amt), 30)` 的 |ρ| < 0.5 闸门。
- **但它和市值是同一根轴的两种读法。** 股价 = FloatCap / FloatShares,取对数:`log(价格) = LogFloatCap − LogFloatShares`。
  控制里只有 `LogFloatCap`,把它(按 rank 线性)投影掉之后,「低价」≈「同等市值下流通股本大」,也就是下面的来源 B。两者**不是两个独立发现**。
- 更要紧的是:`cs_first_low20` 给的是一个**指示函数**(最低 20% 加 1),而控制是对 `LogFloatCap` 的 rank **线性**投影。
  线性控制拿不掉尾部指示函数这种非线性暴露。所以来源 A 很可能是**市值 / 价格的非线性尾部暴露**,它能活过中性化,机制上却仍然是「最便宜、最微型的那一段」。
- 时段证据与这个担心一致:5 个 head 的 valid 夏普(+1.87 / +1.94 / +2.63 / +2.79 / +1.90)普遍是 train(+0.91 / +0.78 / +0.76 / +0.65 / +0.58)的 2–3 倍,
  valid 段 = 2022-01 ~ 2023-08。这一族很可能在吃一个**时段**,样本外的耐久性要打折。**这是提醒,不是否决**:score 取 train 与 valid 的较差者,
  闸门卡在 train 上,train 也还是 +0.58 ~ +0.91,所以它在样本内是实打实的。

### 1.4 真来源 B:平滑后的流通股本(线性读法)

- 充分性:`sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10))` 单独 score **+0.58**;
  `sub(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_var(day_gini(High), 5))` 单独 **+0.59**。两者都已经过发现门槛。
- 由 1.1 的量级核验,这两个表达式**数值上就等于** `cross_ema(LogFloatShares, 241)` / 其双重平滑版(差 1e-7 量级),
  拆解也确认:跳掉里面的 `ts_var(day_gini(High), 5)` 后 score +0.92 vs 原 +0.91(必要性 −0.00),跳掉 `ts_var(day_gini(High), 10)` 后 +0.78 vs +0.78(−0.00)。
- 敏感性:`cross_ema` 窗口 241→120→482,head +0.91 为 +0.92 / +0.93,head +0.78 为 +0.77 / +0.78。**完全不敏感** ⇒ 来源是股本的**水平**,不是它的时间平滑。
- 共性:`cross_ema(LogFloatShares, 241)` 59 / 124 个候选,均值差 +0.95,p 0.000。
- 定位:同 1.3 最后一段,中性化掉 `LogFloatCap` 之后,它 ≈ 负的 log 股价。**来源 A 与 B 应视为一个核心轴**:「同等市值下的每股名义价格 / 股本数」。
  一条侧证:head +0.78 = 股本(单独 +0.58)+ 低价段筛选,合起来只到 +0.78,增量 +0.20 —— 若两者是独立信息,增量应该更大。

### 1.5 三个 head 其实在做同一个修正:「买便宜,但别买最烂的」

把 1.2 的化简并排看:低价段内的排序量分别是 ① `cross_ema(LogFloatShares, 241)`(同等市值下股本大 ⇒ 便宜段里偏大的那些)、
② `day_wstd(Vwap, High)`(分钟 Vwap 的加权标准差,权重 `|High|` 近乎等权 ⇒ **绝对金额单位**的日内价格离散度,不是无量纲的 ⇒ 大体随价格水平上升 ⇒ 便宜段里价格偏高的那些)、
③ `|day_corr(Vwap, High)|`。而 head +0.91 的 **E2 − 2·C** 把 `cs_first_low20` 的 +1 变成 **−2**,等于把最低 20% 价格的股票**压下去**。
三个写法都指向同一件事:**在最便宜的一段里避开最极端的那一头**(A 股里这一头是 ST / 面值退市风险)。这是一个可直接检验的假说,我把它放进第 4 节的 R 和 E 外围。

### 1.6 唯一一条不属于价格轴的东西:日内成交时点(未经拆解,属假说)

head +0.58 没有被拆解(本轮只拆了 score 最高的 4 个)。按 1.2 的化简,它的主项是 **−2·`day_centroid(sqrt(Volume))`**:
`day_centroid`(`ops_ext.py:155-166`)是 `|x|` 沿分钟轴的质心,0 = 全在开盘,1 = 全在收盘,取负 ⇒ **买成交量集中在盘前段的股票**。
另一项 `A ∈ (0,1]` 量级只有它的一半,且 `pow_1_5` 对 `cs_last_low10` 的负值会出 NaN(`pow_` 在 e>1 时走 `torch.pow`,`alphacube/operators/common.py:216-225`;
`catalog.py:145` 把 `pow_1_5` 绑到 e=1.5),所以 A 更像一个被部分遮掉的噪声项。
共性表里 `day_centroid(sqrt(Volume))` 均值差 +0.64、p 0.116、9 个候选 —— p 不过 0.1,**进不了机械核心卡**,但 n=9 说明它不只出现在那一条好血脉里。
这是快照里唯一一条与价格 / 市值轴无关的信息,值得先用 R 的直接评估把它钉死(见第 4 节)。

### 1.7 一条方法上的警告:共性表这一轮基本在追踪血脉,不是因果

124 个候选来自**同一次** GP 运行。共性表前几行的 `n_with` 是 6 / 5 / 4 —— 就是那 4~6 棵近乎相同的好树本身;
`day_gini(High)` 更极端:72 / 124 个候选含它,含它均值 −0.00、不含它 −0.76,「效应」是被「不含它的那一群普遍很差」撑起来的。
最直接的反证:`sub(cross_ema(LogFloatShares, 241), ts_var(LogFloatShares, 10))`(同样是「股本减一个极小量」的结构)均值差 **−0.02**,
`sub(cross_ema(LogFloatShares, 241), day_gini(High))` 更是 **−0.72**。同一个结构,换一个同样可忽略的减数,共性就反过来。
**所以本轮只把拆解(付费、受控)当证据,共性表只用来挑 n 大且与拆解一致的那几行。**

---

## 2. 烂部件(R 的目标)

按证据强度排:

| 部件 | 证据 | 判断 |
|---|---|---|
| `ts_var(day_gini(High), 5)` / `ts_var(day_gini(High), 10)` | 三次跳掉:必要性 **−0.00 / −0.00 / −0.00**(head +0.91、+0.78 两处);量级核验 ≈ 1e-9~1e-7 对 O(1) | **纯装饰**。在 `sub(股本, 它)` 里数值上等于不存在,唯一可能的作用是 NaN 掩码。出现在 4 个 head 里,是最值得清掉的部件 |
| `ts_decay_linear(·, 20)`(包在价格外面) | 跳掉:head +0.76 → **+0.88**(必要性 −0.12,**这就是本轮唯一的 R 候选,增益 +0.123**)、head +0.78 → +0.80(−0.02);窗口 20→10 两处都变好 | **有害 / 无用**。价格的 20 日平滑不如当日价格 |
| `pow_3` | 跳掉:+0.75(0.00)、+0.64(+0.02);且最后一层取 z-rank,单调变换无效 | 无用(它只因为被 `ts_decay_linear` 包住才非恒等) |
| `abs_(day_wstd(...))` 的 `abs_` | 跳掉必要性 **+0.00**;`day_wstd` 返回 `sqrt(var)` 非负 | **恒等变换**,可直接删 |
| `abs_(day_corr(...))` 的 `abs_` | 跳掉必要性 **−0.00** | 无用 |
| `cross_ema(·, 241)` 的双重 / 单重平滑 | 窗口 241→120→482 score 变化 ≤ 0.02(四处) | 无用。**拆解没有试过彻底去掉它**(去算子只在有日频子节点时做),所以「换成裸 `LogFloatShares`」是一个**没被测过**的高性价比 R |
| head +0.58 里的 `neg`(在 `abs_` 内) | 读源码即知 | 恒等变换 |
| head +0.65 整体 | `Vwap→Close` 换字段 +0.65 → **+0.19**,`High→Low` → +0.56 | 它是 5 个 head 里最脆的一个:同一个段筛选,换成 head +0.76 的 `day_wstd` 写法既更稳又更高。可考虑整体被 R 替换 |

---

## 3. 之前的任务

第 1 轮,`missions_before` 为空,`replacements_in_force = 0`,没有 `notebook.md`。无可对照的预测。

---

## 4. 本轮候选

### 4.1 值得深挖的核心(≤ 3,按推荐度)

**核心 ①(首选):`ts_decay_linear(pow_3(day_mean(Open)), 20)` —— 价格水平项(机械核心卡第 11)**

- 为什么:必要性最大(+1.81、+3.43),是 4 个 head 共用的那一件东西,方向明确(单独 −1.15 ⇒ 买便宜),字段换 `Open→Close` 不变。
- 奖励加核心家族之后被中性化掉的 head:快照里含它的是 head +0.91 / +0.78 / +0.76 / +0.65 —— **四个**,控制最强,只有真正的新信息才拿分。这是本轮能构造的最干净的 E。
- **周围已经见过的外围写法**(E 必须避开的集合):
  1. `cs_first_low20(y, 核心)`,y = `sub(cross_ema(LogFloatShares, 241), ts_var(day_gini(High), 10))`(head +0.78);
  2. 同上,y = `sub(cross_ema(cross_ema(LogFloatShares, 241), 241), ts_var(day_gini(High), 5))`(head +0.91 内部);
  3. 同上,y = `abs_(day_wstd(Vwap, High))`(head +0.76);
  4. 同上,y = `abs_(day_corr(Vwap, High))`(head +0.65);
  5. 把 ① 的输出再 `sub` 一个极小量 `ts_var(day_gini(High), 10)`(三个 head 的尾巴);
  6. `sub(E2, 2·cs_first_low20(...))` 这种「把低价段压下去」的符号翻转(head +0.91);
  7. 窗口 10 / 20 / 40,`pow_3` 有无,`Open/Close` 互换 —— 全试过了,别再花预算。
- **没见过、值得 GP 去长的外围**(供 PI 写种子):换别的分段算子(`cs_first_low40` / `cs_first_high20` / `cs_last_low10` / `cs_last_high20` / `cs_bucket_demean` / `cs_bucket_zscore` /
  `cs_robust_z`);**双重分段**(先 `cs_first_low20(·, 价格)` 再 `cs_last_low10(·, 价格)`,直接检验 1.5 的「买便宜但避开最烂」);
  用价格**相对自身历史**的位置(`ts_*` 作用在价格上)而不是截面位置;把价格段与日内形状(`day_centroid` / `day_gini` 作用在 `Volume` / `Amt` 上)交互;
  以及用 6 个日频叶子里**没被碰过的** `LimitWidth`、`BoardCode`、`ListAge`、`LogTotalCap` 做条件。
- 一个要让 PI 权衡的取舍:核心取更小的 `day_mean(Open)`(共性 n=15、p 0.000,4 个 head 同样都含它)会把平滑方式的自由度交回 GP(而证据说短窗更好),
  但核心越小越容易被 GP 塞在无关紧要的位置上,E 就退化成「带一个价格叶子的自由搜索」。我倾向用完整的 ①:它是一个具体统计量,
  「外围必须与见过的不同」这条约束也好核对,而且它正好在机械核心卡上(与 B0 可比)。

**核心 ②:`cs_first_low20(abs_(day_wstd(Vwap, High)), ts_decay_linear(pow_3(day_mean(Open)), 20))`(机械核心卡第 3,自身 score +0.75)**

- 为什么:把「便宜段里的一本完整的书」整件固定住,让 GP 在外面长择时 / 加权 / 二次筛选。它是 4 个 head 里最稳的那个(字段互换 ±0.01,远好于 +0.65 那个的 −0.46)。
- 已见外围:外面只见过 `sub(·, ts_var(day_gini(High), 10))` 这一种(head +0.76),以及把内部 `ts_decay_linear` 换窗口 / 去掉的 4 个拆解变体。**外围几乎是空白**,GP 有很大空间。
- 注意:含它的 head 只有 1 个,奖励里加的家族只有 1 条,控制比核心 ① 弱,更容易长出和原 head 近似的东西(靠库里 ρ≥0.7 与骨架禁令兜底)。

**核心 ③(探索性,须先用 R 钉死):`day_centroid(sqrt(Volume))`**

- 为什么:快照里**唯一**一条不属于价格 / 市值轴的信息(1.6),而 §2.5 只要求核心是「快照里某个 head 或存档候选的子树、能单独求值」,它符合。
- 已见外围:只见过 head +0.58 里的「取负 ×2 再减两个极小量」,以及 `sqrt` 这一层。外围基本空白。
- 风险:它的单独 score **未知**(本轮没拆 head +0.58),p = 0.116 没过共性闸门。**建议先花 R 的直接评估量一下**(见 4.2),不行就别占 E 位。

### 4.2 R 目标(≤ 16 次直接评估,按优先级;替换门槛 = 原 head + 0.1,且与原 head 信号 ρ ≥ 0.5)

已有的唯一 R 候选(loc 自带,增益 +0.123,**已过门槛**):
`sub(cs_first_low20(abs_(day_wstd(Vwap, High)), pow_3(day_mean(Open))), ts_var(day_gini(High), 10))`,对应 head +0.76。

在它之上继续清理烂部件(第 1 组,针对 head +0.755,门槛 ≥ +0.855):

1. `cs_first_low20(abs_(day_wstd(Vwap, High)), pow_3(day_mean(Open)))` —— 再去掉没用的尾巴 `ts_var(day_gini(High), 10)`
2. `cs_first_low20(day_wstd(Vwap, High), day_mean(Open))` —— 最简形(去 `abs_`、去 `pow_3`、去尾巴)
3. `cs_first_low20(abs_(day_wstd(Vwap, High)), ts_decay_linear(pow_3(day_mean(Open)), 5))` —— 窗口再缩短(10 已证明优于 20)
4. `cs_last_low10(cs_first_low20(day_wstd(Vwap, High), day_mean(Open)), day_mean(Open))` —— 直接检验 1.5 的「买便宜但避开最烂的 10%」

第 2 组,针对 head +0.78(门槛 ≥ +0.88),主要测「`cross_ema` 到底需不需要」:

5. `cs_first_low20(cross_ema(LogFloatShares, 241), pow_3(day_mean(Open)))`
6. `cs_first_low20(LogFloatShares, day_mean(Open))` —— 裸股本 + 当日价格,最简形
7. `cs_last_low10(cs_first_low20(LogFloatShares, day_mean(Open)), day_mean(Open))`

第 3 组,针对 head +0.58(门槛 ≥ +0.68),把 1.6 的假说钉死:

8. `neg(day_centroid(sqrt(Volume)))` —— 主项单独(同时是「子树充分性」的补做)
9. `neg(day_centroid(Volume))`
10. `neg(day_centroid(Amt))` —— 9、10 是换同类字段的敏感性
11. `sub(ts_mean(abs_(pow_1_5(cs_last_low10(day_wmean(Ret, Volume), ts_reg_tvalue(day_quantile(Volume), day_mean(Ret), 10)))), 30), day_centroid(sqrt(Volume)))`
    —— 去掉恒等的 `neg` 与两个极小项、系数从 2 改回 1,看 A 项是否真有贡献
    (注:`sub(neg(day_centroid(sqrt(Volume))), day_centroid(sqrt(Volume)))` 不必试,它等于 2× 主项,rank 等价)

第 4 组(低优先,门槛 +1.015 很高,只在还有余量时做):

12. `sub(LogFloatShares, cs_first_low20(LogFloatShares, day_mean(Open)))` —— head +0.91 的最简形(双重 `cross_ema` 换裸字段)

> 这些变体几乎都是「删一个已证无用的部件」,互相可叠加,12 次评估在预算内;PI 可按 1–8 的顺序截断。

### 4.3 N 的灵感(按与证据的贴合度)

1. **把「条件化」本身当成方法,换条件变量。** 本轮唯一有效的东西不是某个 y,而是 `cs_first_low20` 这个分段算子(1.3:y 单独是负的,筛选贡献 +1.8~+3.4)。
   而 6 个日频叶子里 `LimitWidth`(10% / 20% 涨跌幅制度)、`BoardCode`(主板 / 创业 / 科创 / 北交)、`ListAge`、`LogTotalCap` 在这一批里**一次都没出现过**。
   其中 `sub(LogTotalCap, LogFloatCap)` = log(总市值 / 流通市值) = **限售 / 非自由流通比例**,它由两个叶子直接算出,且**不在控制里**(控制只有 `LogFloatCap`)——
   这是一个干净的、未被占用的截面特征。N 可以是「在这些未被使用的制度 / 结构分段里建条件化的书」。
2. **日内成交时点**(1.6):`day_centroid` 族(作用在 `Volume` / `Amt` / `Ret` 上)、以及它与价格段的交互。先看 4.2 第 3 组的结果再定要不要上 N 位。
3. 非线性尾部的另一面(1.3 最后):既然线性 `LogFloatCap` 控制拿不掉指示函数型暴露,N 可以显式去找「对市值 / 价格的非单调(中段最优)」结构,
   例如 `cs_last_low10` 与 `cs_last_high20` 同时作用在价格上(两头都切掉)。

---

## 5. 给文献员的题目(≤ 4)

> 约束提醒:只能用 **2023-08-08 之前发表** 的文献,每条注明年份。下面每题都对准第 1 / 4 节的一个核心或灵感。

**题 1(对准核心 ①、来源 A):名义股价水平作为截面特征,文献里是怎么处理的?**
问:名义每股价格(不是市值)作为预测变量时,常见的处理有哪些 —— 取对数 / 分位数、与规模做双重排序或正交化、是否剔除最便宜的尾部(ST、面值退市、仙股)、
用什么持有期、在 A 股与美股里的符号是否一致、它与规模 / 流动性 / 波动的关系被如何分离?
关键词:低价股效应、名义股价、每股价格、仙股、面值退市、ST 股、双重排序、规模中性化;
nominal share price, price level effect, low-priced stocks, penny stocks, price per share anomaly, double sort on size, size-neutral.

**题 2(对准核心 ①/来源 B 的「同一根轴」问题,以及灵感 3):股本数量、自由流通比例、以及规模的非线性暴露**
问:文献里有没有把**流通股本 / 总股本 / 自由流通比例**当成独立于市值的特征来用?有没有证据说**规模的非线性(尾部指示函数、分段、中段最优)暴露**
无法被线性规模控制吸收?微盘 / 小盘的收益是不是集中在极端尾部,以及 2021–2023 年前的文献怎么讨论这一族的时段依赖与拥挤?
关键词:流通股本、总股本、自由流通比例、限售股比例、股本结构、微盘股、小市值效应、非线性规模暴露、分段回归;
shares outstanding, free float ratio, restricted shares, share structure, micro-cap, non-linear size exposure, size tails, piecewise/threshold size effect, factor crowding.

**题 3(对准「条件化」这个方法本身,核心 ②、灵感 1):只在某一段股票里用某个信号 —— 怎么做、怎么验?**
问:条件化 / 分段因子构造(「signal y 只在特征 x 的某一段里用」)在文献里的做法:条件排序 vs 双重排序 vs 交互项 vs 分组回归;
段宽(10% / 20% / 三分位)怎么定、对段宽敏感不敏感;段内排序与全市场基准的可比性怎么处理;这类条件化结果的样本外稳定性与数据挖掘风险怎么评估?
关键词:条件排序、双重排序、分组回归、交互项、条件化因子、分位数筛选、样本外稳健性、多重检验;
conditional sorts, double sorts, characteristic-conditioned factors, interaction vs double sort, quantile screen, bandwidth choice, conditional alpha, out-of-sample robustness, multiple testing.

**题 4(对准核心 ③、灵感 2):日内成交量的时点分布作为截面预测变量**
问:日内成交量**在一天里的分布 / 质心 / 时点**(开盘段占比、尾盘占比、U 形偏斜)被当作横截面预测变量时怎么构造与归一化?
符号是什么(成交集中在早盘还是尾盘更好)?它与流动性 / 波动 / 换手如何分离?有没有与规模或价格分段交互的做法?
关键词:日内成交量分布、成交时点、开盘成交占比、尾盘成交占比、日内 U 形、资金流时点、分钟级成交分布;
intraday volume distribution, volume timing, intraday volume centroid, opening/closing volume share, U-shaped intraday pattern, time-of-day order flow, intraday trading patterns cross-section.
