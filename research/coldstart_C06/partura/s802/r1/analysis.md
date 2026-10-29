# 结构解剖:种子 802,B 组,第 1 轮

读的东西:`r1/loc.md`、`r1/loc.json`(含每个变体的 coverage / distinct / sign / hl / rho_known / rho_head)、`PLAN.md`;
算子源码 `alphacube/operators/{common,nd_ts,dt_day}.py`、`partura/ops_ext.py`;奖励与书的实现 `partura/steer.py`、`partura/books.py`、`scripts/idea_search.py`、`scripts/c05_locate.py`、`scripts/c05_round.py`。
本种子没有 `notebook.md`,也没有前几轮的任何文件(第 1 轮)。

## 0. 一句话

M 的第 1 批名义上给了 6 个 head,实际上只给了 **两份信息**:一份是
`sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))`(下称 **S**,占 5 个 head),
一份是 `day_mean(neg(in_delta(Volume, 60)))`。
5 个 head 里有 4 个是 **S 的单调函数**,只在「哪些天进 EMA 的权重」上不同 —— 这不是 5 个结构,是 1 个结构加 4 种时间加权。
所以本轮的 E 应该钉在**最短的那个充分核心 S** 上,并且外围必须带进**第二个字段 / 另一条轴**;再往 S 上套一层单调包装是白烧 96 次。

---

## 1. alpha 的来源

### 1.1 真来源(一):核心 S

```
S = sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))
```

四条证据都指向它,而且是指向**这个长度**的它:

| 维度 | 证据 |
|---|---|
| 充分性 | S 单独当因子:score **+0.8024**(train +0.8024 / valid +1.1435),sign −1、hl 20,coverage 0.9635、distinct 0.6727,`rho_known` −0.119。单独就过 0.5 的发现线,且远离已知族。 |
| 共性 | S 出现在 77 个存档候选的 11 个里,含它 +0.527 / 不含它 −0.808,均值差 **+1.335**,p 0.000;`inv(S)` 8 个,+1.362,p 0.0001;裸 beta `ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)` 15 个,+0.990,p 0.0007;`day_durbin_watson(Volume)` 18 个,+0.909,p 0.002;`day_flat_run_max(Vwap)` 21 个,+0.776,p 0.0066。 |
| 必要性 | 在 head `inv(ts_decay_linear(inv(sigmoid(ts_regbeta(...))), 40))`(+0.730)里:把 **regbeta 整层敲掉** → `inv(ts_decay_linear(inv(sigmoid(day_flat_run_max(Vwap))), 40))` = **−2.5653**(必要性 **+3.30**);把 **sigmoid 敲掉** → `inv(ts_decay_linear(inv(ts_regbeta(...)), 40))` = **−0.0718**(必要性 **+0.80**)。两层都不可去。 |
| 敏感性 | `Vwap→Close` 在四棵被拆的 head 上**全部变差**:+1.144→+0.499、+0.834→+0.699、+0.832→**−1.027**、+0.730→+0.324。`Volume→Amt` 基本不动或更好:+1.114、+0.817、+0.958、+0.737 —— 字段的「单位」不重要,**价格字段必须是 Vwap**。`ts_regbeta` 窗口 50→25 大跌(+0.398、−0.046),50→100 在非嵌套那棵上大涨(+0.834→**+1.1555**)。 |

**它在算什么(源码)**:

- `day_flat_run_max(Vwap)`(`partura/ops_ext.py:413`)= 一天里**连续相等的分钟数的最长一段 / 有限分钟数**,∈[0,1];实现里 `eq = (a==b) & isfinite(a) & isfinite(b)`,NaN 分钟会打断 run 且不计入分母。分钟 Vwap 的约定是 `amt/volume`,无成交的分钟为 NaN(`alphacube/synthetic.py:126`),所以这个量数的是「**在成交的分钟里,价格被钉在同一个均价上最长连续几分钟**」 —— 在 A 股就是封板 / 极薄盘口单一档位成交,不是「没成交的呆滞」。`Vwap→Close` 一致变差正好符合这一点:分钟 Close 会沿用上一笔,它的 flat run 数的是「没成交」,coverage 0.998、distinct 0.988(几乎连续),是另一个人群,分数全线下降。
- `day_durbin_watson(Volume)`(`alphacube/operators/dt_day.py:273`)= Σ(Δv)² / Σv²(注意分母是**未去均值**的平方和),所以它是**尺度无关的「分钟成交量相对自身水平有多粗糙」**,不是成交量水平 —— 这也是它能在已经控制了流动性 / `cross_mean(day_std(Amt),30)` 之后还剩东西的原因。
- `ts_regbeta(x, y, 50)`(`nd_ts.py:273` → `common.py:643`)是 `y ~ α + β·x` 的 50 日滚动 OLS 斜率,**x 是自变量**。所以核心是「**过去 50 个交易日里,这只股票的日内成交量粗糙度对价格被钉住程度的回归斜率**」。
- 方向:5 个 regbeta head 的 sign / hl 合起来一律指向**做多斜率持续为负的那一端**(S 小 = beta 很负):head +1.144 = `inv(ts_decay_linear(S^1.5, 40))` sign +1;head +0.712 = `S^-1.5` sign +1;head +0.730 = `inv(ts_decay_linear(1/S, 40))` sign −1;S 自身 sign −1。**没有 C04 §1.4 那种方向相反的孪生 head**,所以融合时不会互相抵消 —— 但冗余很重(见 1.4)。
- 机械上,「钉住得越久 → 成交量越碎」(beta 为正)是自然的;**beta 为负**是反常的那一类:钉住的同时成交量反而变**平滑**。这正是「大单连续封在一个价位」的形态,而不是「薄到只偶尔成一笔」。这是**可以被文献和 `LimitWidth` 直接检验的机制**,不是事后编的故事。

**为什么不是代理**:奖励是对流动性、波动、20 日反转、已知族、`LogFloatCap` 做完截面中性化之后的残差建书(`idea_search.py:177-188`),S 在残差上就有 0.80 / 1.14;`rho_known` = −0.119;coverage 0.9635(只比 Close 版的 0.998 少 3.5 个点,**不是靠筛掉股票池取胜**)。所以它不是流动性 / 规模 / 波动的另一种写法。

### 1.2 sigmoid 在做什么 —— 这是本批最有用的一条机械发现

`sigmoid` 不是「平滑地压一下」,它在这里是**硬截断 + 造并列块**:

| 表达式 | distinct | score | train | valid |
|---|---|---|---|---|
| `ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)` | **1.000** | −0.137 | +0.451 | −0.137 |
| `sigmoid(...)` = S | **0.673** | +0.802 | +0.802 | +1.144 |
| `inv(ts_decay_linear(S, 40))` | **0.842** | +0.961 | +0.961 | **+2.432** |
| `inv(ts_decay_linear(S^1.5, 80))`(head +1.144 的 ×2 窗口) | **0.933** | +1.243 | +1.243 | +2.618 |

`day_flat_run_max` 的方差很小(∈[0,1] 且并列极多),beta = cov/var 量级很大,sigmoid 直接饱和成 0 / 1:distinct 从 1.000 掉到 0.673,即典型一天有三分之一的股票落进并列块。裸 beta 的 train 是 +0.45 而 valid 是 −0.14 —— **幅度是噪声,sigmoid 把幅度切掉之后 valid 从 −0.14 变成 +1.14**。
接着 `ts_decay_linear` 的作用不是「再平滑」,而是**把并列块重新拆开**(distinct 0.673 → 0.842 → 0.933),等于把「最近多少天处在极端状态」数成一个连续量 —— 分数随之 +0.802 → +0.961 → +1.243。
**结论:这份 alpha 在 beta 的符号 / 持续性里,不在 beta 的大小里。** 这直接给出 R 和 N 的方向(用 t 值、R²、符号占比替掉「beta + sigmoid」)。

### 1.3 真来源(二):唯一正交的那个 head

```
day_mean(neg(in_delta(Volume, 60)))        score +0.537(train +0.537 / valid +1.264),sign +1,hl 20
```

`in_delta(x,60)` 是分钟轴上的 60 分钟差分(`dt_in.py:301`),`day_mean` 再按日取均值 —— 即「**日内成交量在一小时尺度上的平均斜率**」(放量/缩量形态)。
它**没有被拆解**(本轮只拆了 score 最高的 4 个),所以充分性 / 必要性 / 敏感性全部是空白;共性表里 `day_durbin_watson(in_delta(Volume, 60))` 的均值差是 **−0.06(p 0.75)**,说明 `in_delta` 这个叶子**不是通用的好零件**,只有在 `day_mean` 这个形态下有用。
证据薄,但它是库里**唯一一份与 S 无关的信息**。按 PLAN §3,最终融合会丢掉 ρ ≥ 0.7 的 head,所以「再多一个 S 的单调包装」对 SR 的贡献接近 0,而任何与它正交的东西贡献很大 —— 这个 head 的边际价值被严重低估了。

### 1.4 「只是代理 / 搭车」的东西 —— 不要在上面花 E

1. **`inv(LogFloatShares)`(卡 #9)、`ts_decay_linear(inv(LogFloatShares), 40)`(#10)、`ts_decay_linear(LogFloatShares, 40)`(#11)**:只有共性证据,**零充分性证据**(从没进过任何 head、也没进过拆解)。三者的「含它的均值」分别是 0.4834 / 0.4848 / 0.4827 —— 三位小数都一样,只有「同一批候选高度重叠」才会这样,这是**同一条谱系的搭车现象**,不是因果。而且 `LogFloatShares` 是单调的规模变量,hl=0 时任何单调变换都是恒等(见 1.5),中性化已经回归掉 `LogFloatCap`,`inv(LogFloatShares)` 在残差上剩下的主要就是**股价水平**(cap/shares)—— A 股的低价股效应,一个老掉牙的代理。C01–C04 栽的就是「凭先验下注」这一跤,这里反过来:**定位工具给的共性排名第 3 的那张卡,证据最弱,最像陷阱**。
2. **`day_flat_run_max(Vwap)` 自身(卡 #14)**:coverage 0.9993 但 **distinct 0.1385**,被门槛(coverage ≥ 0.9 且 distinct ≥ 0.5,`c05_locate.py:138`)判为废品,单独不能当因子。它只能**作为回归的自变量**进来。共性 +0.776 完全是靠 S 那条谱系带起来的。
3. **head +0.832 的外层嵌套 regbeta**:`sigmoid(ts_regbeta(day_flat_run_max(Vwap), S, 50))` 比内层的 S 只高 +0.03(0.832 vs 0.802),三个 knockout 全部 distinct 不过关(0.479 / 0.411 / 0.139),`Vwap→Close` 掉到 −1.027,窗口 25 掉到 −0.046、窗口 100 也只剩 +0.466。**纯死重 + 脆弱**,不是新来源。

### 1.5 为什么 1 份信息会变成 5 个 head(机械原因,影响本轮决策)

奖励的管线是:原始面板 → **按日 EMA(半衰期 ∈ {0, 5, 20})** → **按日截面 z-rank** → 投影掉控制 → 十分位纯多头书(`steer.py:633-646`、`neutral_residual` 在 `steer.py:424`)。
EMA 在 z-rank **之前**。所以:

- **hl = 0 时,任何严格单调变换都是恒等**(单调减的被 sign ±1 扫掉)。证据就在数据里:`ts_decay_linear(inv(pow_1_5(inv(S))), 40)` 单独跑选中了 **hl = 0**、score +0.5052;而它外面套一个 `inv` 的那棵就是 head +1.144(hl = 20)。**同一条信息,仅仅因为 `inv` 改变了「哪些天在 20 日 EMA 里占权重」,score 从 +0.505 变成 +1.144。** 代码注释自己写着这件事(`steer.py:178-181`:"At the ROOT ... changes nothing a rank-based book sees on the day — only how the days mix under the EMA")。
- 所以把这几个 head 的壳子算清楚(`inv(pow_1_5(inv(x))) ≡ x^1.5`):
  - +1.144 = `inv(ts_decay_linear(S^1.5, 40))`
  - +0.834 = `[sigmoid(S^-1.5)]^1.5`
  - +0.730 = `inv(ts_decay_linear(S^-1, 40))`
  - +0.712 = `S^-1.5`
  - +0.832 = 上面 1.4 第 3 条的嵌套版

  **四个是 S 的单调函数。**
- 为什么 GP 的去重没拦住:`MONOTONE_ANY` / `MONOTONE_NONNEG`(`steer.py:179-180`)里有 `sigmoid pow_1_5 pow_2 sqrt …`,**没有 `inv`** —— 因为 1/x 跨 0 不单调。但这里 `inv` 的操作数是 sigmoid 的输出(严格正),它就是单调的。**`inv` 是这批 GP 的逃逸出口**:套一层 `inv` 就能让同一条信息看起来像一次新实验,互相的 |ρ| 又恰好 < 0.7(R 候选与原 head 的 `rho_head` = 0.639 / 0.727 / 0.998,都卡在门槛附近)。`steer.py:316` 的注释记过同样的事("episode e3_I1: both arms' lists of finds were padded with such re-wrappings")。

**给 PI 的直接后果**:机械核心卡 #1、#3、#4、#5、#6 **都是 S 的单调包装**(#1 = `sigmoid(S^-1.5)`、#3 = `[1/sigmoid(S^-1.5)]^1.5`、#4 = `1/sigmoid(S^-1.5)`、#5 = `S^1.5`、#6 = `S^-1.5`)。B0 按卡序会把 E 位钉在 #1 上 —— 一个比 S 长 4 个节点、信息完全相同的核心。**B 组这一轮能拿到的最明确的优势,就是钉最短的那个充分核心(卡 #2 = S),把节点预算和「新外围」的要求全部留给真正的新信息。**

---

## 2. 烂部件(必要性 ≤ 0,或换掉反而更好)—— R 的料

| head | 部件 | 证据 | 判语 |
|---|---|---|---|
| +0.730 `inv(ts_decay_linear(inv(sigmoid(ts_regbeta(...))), 40))` | 内层 `inv` | 敲掉 → `inv(ts_decay_linear(sigmoid(ts_regbeta(...)), 40))` = **+0.9608**(train 0.961 / valid **2.432**),必要性 **−0.230**,`rho_head` 0.639、`rho_known` −0.158 | **有害**。gain +0.230 ≥ 0.1 且 ρ_head ≥ 0.5 → 合规替换(已在 `r_candidates`)。头号 R。 |
| +0.730 | `ts_decay_linear(…, 40)` | 敲掉 → +0.8032,必要性 **−0.07** | 无用(在这棵上)。但在 +1.144 那棵上必要性 +0.43 —— **按 head 判,不要一刀切** |
| +0.834 `inv(pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(...)))))))` | 中段 `pow_1_5(inv(sigmoid(·)))` | 敲掉 → +0.9325,必要性 **−0.096** | 有害,但 gain +0.0957 **差 0.004 够不上 +0.1 的替换线**。值得做一个「两层 pow_1_5 一起去掉」的干净版本去撞这条线 |
| +0.834 | 最外两层 `inv/pow_1_5` | 必要性 +0.02、+0.08 | 无用(纯节点浪费) |
| +0.832 | 整个外层 `ts_regbeta(day_flat_run_max(Vwap), ·, 50)` | 比内层 S 只高 +0.03;knockout 全部 distinct 不过关;Close −1.027;窗口 100 → +0.466 | **死重 + 脆弱**,应整层拿掉 |
| +0.537 `day_mean(neg(in_delta(Volume, 60)))` | `neg` | `day_mean` 是线性的 ⇒ `day_mean(neg(x)) ≡ −day_mean(x)`,而奖励对 sign ±1 做扫描(`steer.py:638`)⇒ **`neg` 在这里是精确的恒等** | 代数空操作。去掉**分数必须一模一样**(所以拿不到 +0.1,不能替换),但值得花 1 次直接评估当**对账**:如果不等,说明我们对管线的理解有错 |
| 全部 | `ts_regbeta` 窗口 50 | 50→25:+0.398 / −0.046(大跌,coverage 也掉到 0.926);50→100:+1.1555(非嵌套那棵,gain **+0.321**) | 50 偏短。**窗口 100 是已证实的方向** |
| +1.144 | `ts_decay_linear` 窗口 40 | 20 → +1.112,40 → +1.144,80 → **+1.243**(gain +0.0992,**差 0.0008 够不上替换线**) | 40 偏短;与窗口 100 叠加是本轮最该试的一发 |

---

## 3. 之前的任务

第 1 轮,没有。`missions_before` 为空,本种子目录下只有 `r1/`。

---

## 4. 本轮候选

### 4.1 值得深挖的核心(按推荐度)

**核心 A(强烈推荐,本轮 E 就用它)**

```
sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))
```

机械卡 #2;自身 +0.8024(train 0.802 / valid 1.144),共性 +1.335 p 0.000,必要性 +0.80 / +3.30,coverage 0.9635,`rho_known` −0.119。
是**最短的充分核心**:比卡 #1/#3/#4/#5/#6 都短,信息完全相同(1.5 节已证)。
代价要讲清楚:`c05_round.py:145` 把「库里含该核心的 heads」按 score 取前 6 个加进控制,含 A 的 head 有 **5 个**(除 `day_mean(neg(in_delta(Volume,60)))` 外全部),所以 E 的奖励会是**本批最严的**。这是优点:只有真正的新信息才拿分。

**已经见过的外围写法**(`idea_search.py:312` 的 `periphery()` = 核心之外的**算子名集合**,多重集相减后取正;真正的 SEEN 来自全部 77 个存档候选,我只能看到成为 head 的这 5 条):

| 来源 | 外围算子名集合 |
|---|---|
| 永久禁(核心自身) | ∅ |
| head +1.144 | {`inv`, `ts_decay_linear`, `pow_1_5`} |
| head +0.834 | {`inv`, `pow_1_5`, `sigmoid`} |
| head +0.832 | {`sigmoid`, `ts_regbeta`, `day_flat_run_max`} |
| head +0.730 | {`inv`, `ts_decay_linear`} |
| head +0.712 | {`inv`, `pow_1_5`} |

**务必注意两件事**:(1) 禁的是**集合**,所以 {`inv`,`ts_decay_linear`,`sigmoid`} 这种「再加一个名字」的单调叠层**仍然合法**,禁令挡不住它;(2) 但 E 的奖励里已经有 5 个含核心的 head 做控制,**纯单调包装的残差接近 0**,会把 96 次评估全部烧掉。
所以手写的 ≤16 个种子要把核心放进**二元算子**里、第二个输入来自**另一个字段或另一条轴**,而不是继续往外套一元函数。可用的新素材(都在 6 个日频叶子或 Partura 扩展算子里,PI 下笔前请用 `partura.ac_plugin.partura_operator_names()` 对一遍词表):

- `LimitWidth` —— 核心讲的就是「价格被钉在一个档位」,涨跌停带宽是这件事的制度参数(主板 10% / 创业板科创板 20% / ST 5%)。直接检验封板解释。C04 里 Partura 唯一留下来的贡献也正是「按涨跌停幅度缩放」。
- `BoardCode`、`ListAge` —— 分组 / 条件化(限价与投机结构按板块、按上市年龄差别很大)。
- 另一个日内形状统计量配对:`day_gini`、`day_zero_ratio`、`day_at_max_ratio`、`day_pos_ratio`、`day_wstd`、`day_distinct_ratio`(都在 `ops_ext.py`)—— 和 DW 一样是尺度无关的日内形状,但不是同一条信息。
- 对核心本身做**日度滚动统计**而不是再平滑:`cross_stddev` / `ts_stddev`(把「beta 的不稳定度」变成因子)。注意 `ts_decay_linear` 已经见过。
- 条件化而非相加:`cs_bucket_rank` / `cs_bucket_zscore` / `cs_flip_by_state` 这类按状态分桶的算子(`ops_ext.py`),用 `LogFloatShares` / `LimitWidth` 当桶 —— 「小盘里核心更强吗」是新信息,而把 `inv(LogFloatShares)` 加进去只是代理(1.4 第 1 条)。

**核心 B(备选,主打正交性)**

```
day_mean(neg(in_delta(Volume, 60)))          —— 或按 PLAN 修订 3,用整个 head 当核心
```

唯一与 S 正交的信息;+0.537 / valid +1.264。但它**完全没被拆过**,`in_delta` 作为通用零件的共性是 −0.06(p 0.75)。
**建议**:本轮不要把 E 给它,先用 R 的直接评估把它拆一遍(见 4.2 的第 10 条,3–4 次评估);如果它的字段 / 窗口敏感性过关,第 2 轮再给它一个 E 位 —— 那时它对最终融合的边际价值(PLAN §3 丢 ρ ≥ 0.7)会比 S 的第 6 个包装高得多。

**核心 C(不推荐,仅列出以供对照)**

```
ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)
```

机械卡 #12,裸 beta。自身 −0.137,但必要性 +3.30。好处是把「用什么压幅度」交回给 GP 去搜;坏处是 1.2 节已经证明「压幅度」是必需的,把它放出去等于让 GP 用 96 次评估重新发明 sigmoid,而含它的 head 全部进控制之后这些重新发明又都不得分。**用 A 不用 C。**

### 4.2 R 目标(PI 从里面挑 ≤16;前 3 个是拆解里已经评过的,不花预算)

已评过、合规(gain ≥ 0.1 且 ρ_head ≥ 0.5、|ρ_known| < 0.5):

1. head +0.730 → `inv(ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 40))`,gain **+0.230**,ρ_head 0.639,ρ_known −0.158。
2. head +0.834 → `inv(pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100)))))))))`,gain **+0.321**,ρ_head 0.727。
3. head +0.832 → `sigmoid(ts_regbeta(day_flat_run_max(Vwap), sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Amt), 50)), 50))`,gain **+0.126**,ρ_head 0.998。

新提议(每条都接着一条已证实的方向,不是凭先验):

4. **把两个已证实的窗口方向叠起来**(目标 head +1.144):
   `inv(ts_decay_linear(pow_1_5(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100))), 80))`
   —— regbeta 50→100 在别处 +0.321,decay 40→80 在这棵上 +0.099(单独差 0.0008 够不上线)。本轮最该试的一发。
5. 同上只动 decay,检验「越长越好」是不是单调:`inv(ts_decay_linear(pow_1_5(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))), 120))`(已知 20 → +1.112、40 → +1.144、80 → +1.243)。
6. 再加 Amt(四棵里三棵 Amt ≥ Volume):`inv(ts_decay_linear(pow_1_5(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Amt), 100))), 80))`。
7. **整层剥掉 head +0.832 的死重**:`sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Amt), 50))`(从未评过;Volume 版是 +0.802,Amt 在嵌套版上 +0.958)。
8. **「幅度是噪声」的直接检验**,把 beta 换成 t 值(`ts_reg_tvalue`,`nd_ts.py:286`;禁令只禁 `ts_spearman` 与 `nt_*`):
   `inv(ts_decay_linear(sigmoid(ts_reg_tvalue(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 40))`,以及去掉 sigmoid 的版本 `inv(ts_decay_linear(ts_reg_tvalue(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50), 40))` —— 如果 t 值版不需要 sigmoid 就能打到 ≥ 0.96,1.2 节的读解就被证实,后面两轮可以直接改用 t 值族。
9. **代数对账(各 1 次,预期分数必须严格相等,用来验证我们对管线的理解)**:
   `day_mean(in_delta(Volume, 60))` 应 ≡ +0.537;
   `inv(ts_decay_linear(pow_1_5(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))), 40))` 应 ≡ +1.1438(比 head 少 2 个节点)。
10. **把唯一正交的 head 拆一遍**(它从没被拆过):`day_mean(in_delta(Amt, 60))`、`day_mean(in_delta(Volume, 30))`、`day_mean(in_delta(Volume, 120))`。
11. head +0.834 的「两层 pow_1_5 一起去掉」的干净版(单层去掉差 0.004 够不上线):
    `inv(sigmoid(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100)))))`。

### 4.3 N 的灵感(按我手上的证据排序,PI 定)

1. **「关系的稳定性」而不是「关系的斜率」**(最硬的一条,来自 1.2):沿 `ts_reg_tvalue` / `ts_reg_fvalue`(R²)/ `ts_pearson` 这条线重做「日内粗糙度 × 价格钉住」的关系,并把它推广到别的日内形状对。假设一句话:*这类日内微观结构关系的横截面信息在它的符号与持续性里,幅度是噪声,所以应该用标准化统计量而不是回归系数。*
2. **封板解释的正面检验**:用 `LimitWidth` 把「价格被钉住」归一化 / 分组(`day_flat_run_max(Vwap)` 自身 distinct 只有 0.139 过不了门槛,必须先做滚动占比或分桶再用),看核心的信息是不是来自带宽制度。
3. **日内成交量形态族**(把唯一正交的那份信息系统化):开盘 / 尾盘成交占比、日内成交量斜率、量的 U 形残差,配 `day_gini` / `day_zero_ratio` / `day_centroid` / `day_topw_mean`。
4. **换掉 DW,保留「尺度无关的日内粗糙度」**:`day_gini(Volume)`、`day_distinct_ratio`、`day_wstd/day_std` 之比等,检验核心对「粗糙度怎么量」是否稳健(类似 `Volume→Amt` 的不敏感)。

---

## 5. 文献题目(给文献员,只能用 2023-08-08 之前发表的)

**L1(对准核心 A 的「是真来源还是流动性代理」)**
日内价格被钉在同一档位的连续时长 / 零收益分钟占比,在文献里是怎样被处理的?它通常被当成**涨跌停封板**还是**呆滞价格(stale/zero-return)流动性代理**?常见的处理有哪些:按涨跌停带宽归一化、按板块 / ST 分组、区分「一字板」与「开板」、剔除还是单独建组、与换手率 / Amihud 正交化?
关键词:涨跌停、一字板、封板、价格限制、停牌、零收益率流动性指标、呆滞价格;price limits, limit-hit, limit-lock, magnet effect, zero-return illiquidity measure (Lesmond-Ogden-Trzcinka), stale prices, China A-share price limits.

**L2(对准核心 A 的另一半:DW(Volume))**
日内分钟成交量的**自相关 / 粗糙度 / 爆发性**类指标在文献里被怎样构造和处理?特别是:要不要先剔除日内 U 形形态、要不要按当日成交量水平标准化(尺度无关化)、常用窗口多长、与波动率和换手率怎样正交化?Durbin–Watson 这类「一阶差分平方和 / 平方和」的统计量有没有被用作横截面因子?
关键词:日内成交量形态、成交量自相关、成交量 U 型、订单流聚集、交易强度;intraday volume autocorrelation, volume profile / U-shape, order-flow burstiness, trade clustering, volume timing, Durbin-Watson statistic as a feature.

**L3(对准 1.2 的发现:幅度是噪声)**
把**两条个股日度序列之间的滚动回归斜率**当横截面因子时,文献用哪些办法处理斜率的估计误差?具体有:收缩(Vasicek / Bayesian)、winsorize / 截断、改用 t 值或 R²、改用秩相关、拉长估计窗口、用符号或状态占比代替数值。哪种处理在样本外最稳?窗口长度一般取多少?
关键词:滚动回归贝塔、贝塔估计误差、贝塔收缩、稳健化、t 值、横截面因子的极值处理;rolling beta as a cross-sectional signal, beta estimation error, Vasicek shrinkage, winsorizing factor tails, t-statistic versus coefficient, signal-to-noise in estimated betas.

**L4(对准核心 B / N3:日内成交量斜率)**
「日内成交量的时间斜率 / 放量-缩量形态」(例如一小时尺度上的成交量差分按日取均值、尾盘与开盘成交占比)在文献里有哪些做法?通常怎样归一化(除以当日总量、去掉 U 形基准)、取什么周期、是否按规模 / 换手率分组、与知情交易和次日收益的关系是什么?
关键词:日内成交量斜率、尾盘成交占比、开盘成交占比、放量缩量、知情交易概率;intraday volume trend/slope, end-of-day volume share, opening volume share, intraday volume distribution and future returns, informed trading.

---

## 6. 本轮写下的预测(留给第 2 轮对账)

1. `day_mean(in_delta(Volume, 60))` 的 score **精确等于** +0.537(`neg` 是恒等);`inv(ts_decay_linear(pow_1_5(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))), 40))` 精确等于 +1.1438。若不等,1.5 节对管线的理解有错,后面所有「单调包装」的论断都要推翻。
2. E(核心 A)跑完后,**外围只含一元单调算子(`inv` / `pow_*` / `sigmoid` / `sqrt` / `abs_`)的候选,score 会普遍 < 0.2**;真正过线的 head 会含**第二个叶子或一个二元 / 分桶算子**。
3. 第 4 条 R(regbeta 100 + decay 80)**> +1.243**;第 5 条(decay 120)落在 +1.20 ~ +1.30。
4. t 值版(第 8 条 R)**不需要 sigmoid 就能达到 ≥ +0.80**。
5. 本批 5 个 regbeta head 在 PLAN §3 的贪心去重里会被砍掉**至少 2 个**(ρ ≥ 0.7),所以「E 产出 head 的个数」不是本轮的成败标准,**与 S 的正交性才是**。
