# 结构解剖:种子 802,C 组,第 2 轮

读的东西:`r2/loc.md`、`r2/loc.json`(每个变体的 coverage / distinct / sign / hl / rho_known / necessity)、`r2/R_prev.json`、
`notebook.md`、`r1/{analysis.md, lit.md, missions.yaml, missions_final.yaml, audit_1.yaml, audit_2.yaml, audit_record.json}`、`rules.md`;
算子源码 `AlphaCube/src/alphacube/operators/{common,dt_day,dt_in,dt_cross,nd_ts,nd_cs}.py`、`alphacube/catalog.py`、`partura/ops_ext.py`、`partura/steer.py`、
流水线 `scripts/idea_search.py`、`scripts/c05_locate.py`、`scripts/c05_round.py`。

---

## 0. 一句话

M 的第 2 批名义上给了 7 个新 head(+1.45、+1.29、+1.09、+1.07、+1.03、+0.86、+0.56),**实际上是 3 个已知陷阱**:
一个凸化的已实现方差(陷阱 1)、四个「流通股本 = 控制没覆盖的 −log(价格)」(陷阱 3 / 低价股)、两个纯价格水平的分桶改写。
这一批里**唯一有内容的部件不是那些 y,而是包在外面的排除筛** `cs_last_high10(·, day_max(Volume))` / `cs_last_high10(·, day_gini(Volume))`。
本轮 C 组的优势应该花在两处:(a) 把 E 钉在**我们自己第 1 轮 N 产出的订单流残差核心**上 —— 它是库里唯一一份干净的新信息,周围几乎什么都没试过;
(b) 用 R 把「筛」从陷阱 y 上搬下来,并把 S 族已经白送的 +0.238 窗口替换拿走。
**不要**把第 2 个 E 位再给 S:第 1 轮已登记的可证伪条件已经触发(见 §3.5)。

---

## 1. alpha 的来源

### 1.0 先说共性表这一轮为什么不能直接读

300 个存档候选里,`mean_without` 全部落在 **−0.67 ~ −0.73**。也就是说存档的绝大多数是废品,
任何「出现在一条成功谱系里」的子树,均值差都会自动是 +1.0 上下。证据:

| 子树 | n | 含它均值 | 不含它均值 | 均值差 |
|---|---|---|---|---|
| `inv(LogFloatShares)` | 12 | **+0.4834** | −0.7164 | +1.20 |
| `ts_decay_linear(inv(LogFloatShares), 40)` | 6 | **+0.4848** | −0.6919 | +1.18 |
| `ts_decay_linear(LogFloatShares, 40)` | 4 | **+0.4827** | −0.6839 | +1.17 |

三个「含它均值」小数点后三位全部一样 —— 和第 1 轮 `analysis.md` §1.4 记下的是同一组数字,说明这 12 / 6 / 4 个候选是**同一小撮重叠候选**。
这三张卡(机械核心卡 #5 / #6 / #7)**从未单独评过分、从未进过任何 head、从未进过拆解**。排名第一不代表因果,只代表搭车。
反过来,真正被反复验证的子树因为出现在很多次(含失败的)变异里,均值差被压得很低:
`sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))` n=49 均值差只有 +0.34(p 0.062),
`cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret))` n=14 只有 +0.22(p 0.38)。
**结论:这一轮共性表的排序 ≈「哪条谱系的候选均值高」,不是「哪个子树带来 alpha」。判断真来源必须靠充分性 / 必要性 / 敏感性,共性只能当线索。**

### 1.1 真来源(一):S 族,窗口已经移到 100 / 200

```
S100 = sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100))
```

(第 1 轮的核心是同一棵树的窗口 50 版;R 组已经把两棵 head 的窗口替换成 100,见 §3.4。)

| 维度 | 这一轮的证据 |
|---|---|
| 充分性 | `pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100))))` 单独 **+0.8869**(train 0.887 / **valid 2.9735**),cov 0.9833,distinct 0.714,rho_known −0.166。窗口 50 的同一棵是 +0.80 / valid 1.14 —— 窗口加长后 valid 翻了一倍半。 |
| 必要性 | 在 head +1.155 上,敲掉中段 `sigmoid(pow_1_5(inv(sigmoid(·))))` 掉到 +0.8085,必要性 **+0.347**(是这棵 head 上唯一一个必要性 > 0.04 的部件)。第 1 轮测过的「整层敲掉 regbeta」必要性 +3.30、「敲掉 sigmoid」+0.80,仍然成立。 |
| 敏感性(窗口) | `ts_regbeta` 50 → **+0.8315**;100 → **+1.1555**;200 → **+1.3933**。单调,两个区间同向(valid 0.98 / 1.66 / 2.42)。 |
| 敏感性(字段) | `Volume→Amt` +1.155 → +1.088(基本不动,与 DW 的尺度不变性一致);**`Vwap→Close` +1.155 → +1.0081,只掉 0.147,而 valid 从 1.66 升到 2.65**。 |
| 共性 | 见 §1.0:n=49 / 53 / 57 的大样本,均值差只有 +0.31 ~ +0.34(p 0.06~0.10)。 |

**两条必须记下的坏消息,它们都在削弱第 1 轮对 S 的读法:**

1. **「钉住的必须是有成交的价格」这条证据变弱了。** 第 1 轮 `Vwap→Close` 在四棵 head 上一致大跌(+1.144→+0.499、+0.832→−1.027 等),
   我据此断定 `day_flat_run_max` 数的是「在成交的分钟里被钉在同一均价」而不是「没成交的呆滞」。
   窗口换成 100 之后,Close 版只掉 0.147、valid 还更高、coverage 0.998、distinct 0.905。
   也就是说**窗口一长,「有成交 vs 没成交」的区别就基本消失了** —— 更像是两个版本都在量同一个慢变的「这只股票的价格有多黏」的个股特征。
2. **β 换 t 值的判决性检验失败了(§3.4 的 R 组 1 变体 4 与 R 组 5)。** 三个 t 值变体全部崩掉:
   `inv(ts_decay_linear(sigmoid(ts_reg_tvalue(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 40))` = **−0.273**(train +0.4365),
   嵌套 head 的两个 t 值版 = **−0.771 / −0.615**。
   t 值去掉的恰好是 β = ρ·σ_y/σ_x 里那个与信号无关的尺度 σ_y/σ_x,而相关度表显示 t 值版对波动控制的 |ρ| 从 0.22 掉到 0.05。
   **分数和波动相关性一起消失,这是「S 的一部分分数来自 σ_y/σ_x 的饱和挑选(即带波动的非线性残留,陷阱 3)」的直接证据。**
   另一种读法仍然活着(审计员 attempt 2 已经指出):n=50 时 `sigmoid(t)` 落在 0.12–0.88,是 ρ 的平滑函数而不是近似符号,
   所以 t 值版失败也可能只是**丢了「近似取符号 + 数处在状态里的天数」这个形状**,与尺度无关。
   这两种读法用一次评估就能分开,见 §4.2 的 B3:把 `sigmoid(β)` 换成 **`sign(β)`** —— 符号形状完全保留,σ_y/σ_x 完全去掉。
   **这是本轮信息量最大的 2 次评估,PI 必须做。**

**它在算什么(源码,核对无误)**:`day_flat_run_max(Vwap)`(`ops_ext.py:413`)= 一天里连续相等的分钟数的最长一段 / 有限分钟数 ∈[0,1];
`day_durbin_watson(x)`(`dt_day.py:273`)= Σ(Δx)²/Σx²,**分母未去均值**,所以在 Volume 上是尺度无关的「分钟成交量相对自身水平有多粗糙」;
`ts_regbeta(x, y, d)` 是 y 对 x 的 d 日滚动 OLS 斜率(x 是自变量)。
方向:做多斜率持续为负的那一端(钉得越久、成交量反而越平稳)。

### 1.2 真来源(二):我们自己第 1 轮 N 产出的订单流残差核心

```
OF   = cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret))        ← 建议的 E 核心
head = ts_decay_linear(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 20), 40)   score +0.887 (train 0.887 / valid 1.85), sign +1, hl 5
```

| 维度 | 证据 |
|---|---|
| 充分性 | 核心外面只套一层衰减就过线:`ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 20)` = **+0.52**(valid 2.22),`…, 40)` = **+0.62**(valid 2.63),两层 20+40 = **+0.887**(valid 1.85)。平滑越重越好,说明信息是慢的。 |
| 正交性 | 第 1 轮相关度表:这一族种子与**全部** head 的原始 \|ρ\| ≤ 0.13、残差 \|ρ\| ≤ 0.28。库里 16 个 head 没有任何一个含价格变化方向。 |
| 必要性 | 没有被拆解(本轮只拆了 score 前 4)。但有一条代数旁证:`cs_regres(cs_regres(X, day_sum(Ret)), day_sum(Ret))` 的分数与单层**逐位精确相等**(+0.62/+0.62、+0.52/+0.52)—— 截面回归残差幂等,符合源码(`nd_cs.py:254`),说明管线理解没错。 |
| 敏感性 | 没测过。字段(Volume→Amt)、窗口、`cs_regres` 的 X 换成别的价格方向量、平滑长度,全是空白。 |
| 共性 | 弱:n=14,均值差 +0.22,p 0.38(原因见 §1.0 —— 分母里混进了 N 位 96 次评估的失败变异)。 |

**它在算什么**:`day_signed_ratio(x, y) = Σ|y|·sign(x)/Σ|y|`(`ops_ext.py:122`),零收益分钟只进分母 —— 用分钟 tick rule 算的日度净主动买入占比;
`cs_regres(Y, X)` 按日做截面回归取残差。所以核心 = **「成交量站在哪一边」减掉「当日价格走了多远」能解释的部分**,即被对手方限价单吸收掉的那部分订单流。

**方向上有一个必须更正的地方**:第 1 轮 PI 预期 sign = −1(做多被吸收的**卖**压),实际产出的 head 是 **sign = +1** ——
做多的是「成交量在买、价格没有相应涨上去」的那一端,也就是**被吸收的买压**。
这正是审计员 attempt 1/2 在 b 位扣分的那一条(「引用的文献 Chordia-Subrahmanyam 2004 说买方不平衡之后收益更高,PI 的事先预期却相反」)——
**数据站在文献那一边,不站在 PI 那一边**。这一条在本轮可以直接拿来把合理度往 5 的方向推(文献 + train 证据 + 方向一致)。

### 1.3 M 第 2 批的 7 个 head:三个陷阱,零份新信息

#### (a) `pow_2(pow_2_5(day_durbin_watson(High)))` +1.45 —— 陷阱 1,凸度阶梯清清楚楚

| 表达式 | 等价幂次 | score | train | valid |
|---|---|---|---|---|
| `day_durbin_watson(High)` | 1 | **−1.1711** | −1.17 | +0.58 |
| `pow_2(day_durbin_watson(High))` | 2 | **+0.2653** | +0.27 | +1.96 |
| `pow_2_5(day_durbin_watson(High))` | 2.5 | **+0.7240** | +0.72 | +2.36 |
| `pow_2(pow_2_5(day_durbin_watson(High)))`(head) | **5** | **+1.4497** | +1.45 | +3.20 |

四个表达式是同一个量的严格单调变换,**score 随凸度严格单调上升** —— 这是 `rules.md` §4.1 逐字描述的那个签名。
机制可以说得更精确:`DW(High) = Σ(ΔP)²/ΣP² ≈ E[(ΔP/P)²]`,就是**分钟收益的已实现方差**(尺度无关,所以 `High→Low` 换了几乎不动:+1.278)。
而奖励管线是 **先按日 EMA(hl=20)→ 再按日截面 z-rank → 再投影掉控制**(`steer.py:633` 的 `bk.smoothed(raw, hl)` 在 `neutral_residual` 之前)。
所以 `EMA(RV^5)` 由窗口里**最大的那一天**主导:这棵 head 实际上是按「最近 20 天的最大日内已实现方差」排序,sign = −1,
即**做多最近没有出现极端波动日的股票**。控制里只有 `cross_mean(day_std(Ret), 20)`(线性的日度波动均值),
「窗口内的极大值」是它的非线性函数,线性中性化去不掉。
**判语:这不是新信息,是低波动 / MAX 异象的多头腿从奖励缝里漏回来。**
它是本种子 score 最高的 head,但对最终融合的边际价值很可能是负的(样本外它要么就是已知的低波动溢价,要么在波动换档时反向)。
**不要在它上面花 E;也不要提出任何「再加一层凸变换」的 R —— 那是 §4.1 的陷阱,审计员会直接给合理度 1。**

#### (b) 流通股本族 4 个 head(+1.294、+1.089、+1.070、+0.856)—— 陷阱 3,而且是**控制根本没覆盖**的那一维

```
+1.294  cs_last_high10(signedpower(pow_2_5(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3))), day_max(Volume))
+1.089  cs_last_high10(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3), day_gini(Volume))
+1.070  cs_last_low20(cross_quantile_q25(LogFloatShares, 241), day_durbin_watson(Vwap))
+0.856  cs_last_high10(cs_last_high10(LogFloatShares, day_durbin_watson(High)), day_durbin_watson(Vwap))
```

机制:`LogFloatShares = LogFloatCap − log(价格)`。中性化控制了 `LogFloatCap`,**没有控制 `LogFloatShares`,也没有控制价格水平**。
所以这一族在残差上剩下的主要就是 **−log(价格)**,即 A 股低价股效应 —— 一个老掉牙的代理。
第 1 轮 `analysis.md` §1.4 就是这么判的,这一轮多了两条硬证据:

1. **`day_max(Volume) → day_max(Amt)`:+1.294 → −0.1713。** Amt = Volume × 价格,两者唯一的差别就是价格加权。
   筛选变量换成带价格的版本,整棵 head 从 +1.29 崩到 −0.17。这棵 head 的两个输入(y 和筛)**都**依赖价格水平。
2. **y 单独 = +0.5578**(`cross_quantile_q25(LogFloatShares, 241)`,cov 0.9993、distinct 0.9703、rho_known −0.2843),
   加上筛之后 +1.084 / +1.294 —— 也就是说 **y 只贡献 0.56,筛贡献 +0.5 ~ +0.7**。

#### (c) 价格水平的分桶改写 2 个 head(+1.032、+0.563)

```
+1.032  cs_last_high10(cs_bucket_zscore(day_quantile_q25(Open), sqrt(day_quantile_q25(Open))), day_gini(Volume))
+0.563  cross_quantile_q25(cs_bucket_zscore(day_quantile_q25(Open), sqrt(day_quantile_q25(Open))), 241)
```

`cs_bucket_zscore(y, x)`(`ops_ext.py:482`)= y 在 x 的同一个十分桶内去均值再除以桶内标准差。这里 **y 和 x 是同一个量**(当日分钟 Open 的 25% 分位 = 价格水平,x 只是它的 sqrt)。
所以这个子树 = **价格水平在它自己的价格十分桶里的相对位置**,是一个只用价格、不用任何量 / 收益信息的函数,截面上是 10 段锯齿。
`cross_quantile_q25(·, 241)` 版(+0.563)是同一个东西的一年滚动分位,和 +1.032 那棵共用 y。
**判语:价格水平的非线性改写,陷阱 3。** 共性表里 `sqrt(day_quantile_q25(Open))` 均值差 +0.81(p 0.023)、`day_quantile_q25(Open)` +0.26 —— 同一条搭车谱系。

#### (d) 这一批真正的收获:**筛是好部件**

`cs_last_high10(y, x)` 的源码(`ops_ext.py:339` 的 `_lexi` + `ops_ext.py:391`)是:

```
cs_last_high10(y, x) = _pct_rank(y) − 1·[x 落在它自己的最高 10% 整块里]
```

即「照 y 排序,但 x 标记的那 10% 永远进不了多头书」。两个被实测过的筛:

| 筛 | y 单独 | y + 筛 | 筛贡献 | 变体的 rho_known |
|---|---|---|---|---|
| `day_max(Volume)` | +0.558 | **+1.294** | +0.74 | **+0.0201**(y 单独是 −0.284 → 筛把已知族相关**压低**了) |
| `day_gini(Volume)` | +0.558 | **+1.084** | +0.53 | **−0.4063**(y 单独 −0.284 → 筛把已知族相关**推高**了) |

而且 `day_gini(Volume)` **单独当因子是 −3.6673**(rho_known **+0.6742**),`day_max(Volume)` 共性 +0.72 p 0.0025 n=18。
**「单独是废品、当排除筛很有用」这件事,是本批唯一值得迁移的结构性发现。**
两条必须一起写下的警告:
- `day_gini(Volume)` 的 rho_known = 0.674 ≥ 0.5,**它不能当 E 核心**(规则 §3「E 位还要求核心与每个控制的 |ρ| < 0.5」会直接挡掉),
  而且它带来的 +0.53 里有一部分是沿已知族方向走的(rho_known 从 −0.28 变到 −0.41)。
- `day_max(Volume)` 的筛是**按股数**算的单分钟峰量,Amt 版崩盘说明它选中的 10% 是低价高换手的那一群,**筛本身也带价格**。

两个筛里,`day_max(Volume)` 对已知族更干净但更依赖价格;`day_gini(Volume)` 机制更可解释(成交集中在少数分钟 = 分钟级统计量不可信)但更脏。

### 1.4 一个机械事实:`cs_*` 的 y 位上,一元单调算子是**精确恒等**

head +1.294 的三层包装,必要性分别是 **0.0000 / 0.0000 / 0.0023**:

| 敲掉 | 变体 | score | 必要性 |
|---|---|---|---|
| `signedpower(…)` | `cs_last_high10(pow_2_5(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3)), day_max(Volume))` | +1.2940 | **0.0000** |
| `pow_2_5(…)` | `cs_last_high10(signedpower(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3)), day_max(Volume))` | +1.2940 | **0.0000** |
| `cross_decay_linear(…, 3)` | `cs_last_high10(signedpower(pow_2_5(cross_quantile_q25(LogFloatShares, 241))), day_max(Volume))` | +1.2916 | 0.0023 |
| `cross_quantile_q25(…, 241)` | `cs_last_high10(signedpower(pow_2_5(cross_decay_linear(LogFloatShares, 3))), day_max(Volume))` | +1.1421 | 0.1518 |

原因在源码:`_lexi` 里 `ry = _pct_rank(y, ok)`,**只用 y 的次序**。`signedpower(x, 2) = sign(x)|x|²` 和 `pow_2_5` 都是严格增的,
所以它们在 y 位上一个 bit 都改不了。于是 head +1.294 **逐位等于** `cs_last_high10(cross_quantile_q25(LogFloatShares, 241), day_max(Volume))`。
这是第 1 轮 §1.5 指出的「`inv` 是 GP 的逃逸出口」的第二个版本:
**往 `cs_*` 的 y 位上套一元单调算子,就能让同一个因子换一个骨架、绕过库禁令,看起来像一次新实验。**
按这个口径数,M 第 2 批的 7 个 head 只有 **3 个不同的因子**(凸化方差 / 流通股本×筛 / 价格锯齿×筛)。
顺带一条有用的:`cs_last_*` / `cs_first_*` 的 x 位用的是 `_rank_block`,**只整块进出,对并列是安全的**;
而 `cs_bucket_*` 用 `_buckets = ceil(_pct_rank·10)`,**在并列块里按列序切桶(陷阱 2)**。
所以要按 `LimitWidth` / `BoardCode` 这类少值字段分组,必须用 `cs_last_*` / `cs_first_*`,**不能**用 `cs_bucket_*`。
(第 1 轮审计员划掉 E 位种子 6 正是这个原因。)

### 1.5 对第 1 轮一个读错规则的更正(影响本轮 E 的写法)

第 1 轮 `analysis.md` §4.1 写了「`c05_round.py:145` 把库里含该核心的 heads 取前 6 个加进控制,所以 E 的奖励会是本批最严的」。
**这对 C06 是错的。** 源码 `c05_round.py:241`:

```python
extra = ["--neutral-extra", str(ff)] if STUDY == "C05" else []   # C06 PLAN §2.3: the E reward is everyone's reward
```

本实验 `STUDY = "C06"`(episode 前缀 `c06s802C…` 可证),所以 **`--neutral-extra` 根本没有传**,E 的奖励里**没有**核心家族控制 ——
和 `rules.md` §2 写的一致(「奖励与所有组相同,**不**额外控制核心的家族」)。
后果有两条,都要告诉 PI:

1. 第 1 轮「纯单调包装的残差接近 0,会把 96 次评估烧光」这个论断**不成立**。所以 E 位长出 S 对 S 的组合(score 0.79 / 0.72)是正常的,不是奖励在惩罚它。
2. 真正挡家族重复的只有库禁令(日度秩 |ρ| ≥ 0.7 或骨架相同)。而 §1.4 刚证明骨架可以用恒等包装绕开,
   **所以 E 位很容易把预算花在「同一份信息的第 N 个写法」上而仍然得分。防这件事只能靠种子和假设,不能靠奖励。**

另外两条操作事实(第 1 轮没写对的):
- `--periphery-seen` 喂进去的是**整个快照存档的 300 个候选**(`c05_locate.py` 的 `seen` 文件),不是 5 个 head。
  含某个核心的候选有多少,`loc.json` 的 `n_with` 就是个下界(S 是 49,OF 核心是 14)。
- `periphery(t)` = 核心之外**算子名的集合**(`idea_search.py:312`,多重集相减后取正)。所以「已见外围」禁的是集合;
  种子的外围算子名集合里只要有**一个新名字**就合法。这就是第 1 轮 `c05_periphery_seen` 只拦下 6 次、而 `c05_no_core` 拦下 **2402 次**的原因:
  真正的瓶颈是 GP 的变异 / 交叉会把核心弄丢,**96 次评估里绝大多数算力花在被拒的树上,所以 ≤16 个手写种子承担了几乎全部工作**。

---

## 2. 烂部件(必要性 ≤ 0、或换掉反而更好)—— R 的料

| head | 部件 | 证据 | 判语 |
|---|---|---|---|
| +1.155 `inv(pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(…, 100))))))))` | `ts_regbeta` 窗口 100 | 100 → +1.1555;**200 → +1.3933**(gain **+0.238**,两个区间同向:train 1.16→1.39、valid 1.66→2.42) | **本轮最确定的一分。** 已在 `loc.md` 的 R 候选里,但 R 只评 PI 请求的变体,**PI 必须显式写进 R 组**才会生效(同族 ρ 必然 ≥ 0.5 → 走替换) |
| +1.155 | 外层 `pow_1_5`、内层 `inv(sigmoid(…))` 这一层 | 必要性 **+0.0069** / **−0.0532** | 纯死重。但敲掉拿不到 +0.1,不能替换;不要花钱 |
| +1.155 | 中段 `sigmoid(pow_1_5(inv(sigmoid(·))))` | 必要性 **+0.347** | **不是**烂部件,是这棵 head 上唯一有用的中段 |
| +1.294 | y 位的 `signedpower`、`pow_2_5`、`cross_decay_linear(·,3)` | 必要性 **0.0000 / 0.0000 / 0.0023**(§1.4) | 代数死重,**精确**恒等。免费证据,不用花 R |
| +1.294 / +1.089 / +1.070 / +0.856 | y = `cross_quantile_q25(LogFloatShares, 241)` / `LogFloatShares` | y 单独只有 +0.558,筛贡献 +0.53 ~ +0.74;`day_max(Volume)→day_max(Amt)` 让整棵从 +1.294 崩到 **−0.171**;`LogFloatShares = LogFloatCap − log(价格)`,而控制只有 `LogFloatCap` | **y 是烂部件(价格水平代理),筛是好部件。** 本轮 R 的主攻方向,见 §4.2 A 组 |
| +1.45 `pow_2(pow_2_5(day_durbin_watson(High)))` | 凸幂 `pow_2(pow_2_5(·))` | 凸度阶梯 1→−1.17、2→+0.27、2.5→+0.72、5→+1.45 | **有害(对样本外),但去掉必然掉分**,拿不到 +0.1。只做结论,不做 R |
| +1.089 | `cross_decay_linear(·,3)`、`cross_quantile_q25(·,241)` | 必要性 0.0047 / 0.0654 | 死重 |
| +0.537 `day_mean(neg(in_delta(Volume, 60)))` | 整个 `neg(in_delta(Volume,60))` | **R4 四个变体全崩**:`in_scale(Volume)@60` −0.067、`in_scale(Amt)@60` −0.032、`@30` −0.305、`@120` −0.578 | 见 §3.4:**不只「水平」被否了,最简单的那个尺度无关时点写法也被否了。** 这棵 head 的 +0.537 基本可以判为流动性水平的残留 |
| 两棵嵌套 regbeta head(+0.832 / 由它派生的 +0.788、+0.717) | 原始斜率 β → t 值 | 两个 t 值变体 **−0.771 / −0.615** | 第 1 轮已登记:「若两个都掉分 → 第 2 轮不再在它上面花 E 或 R」。**条件已触发,照办** |

---

## 3. 之前的任务

### 3.1 E 位 `c06s802Cr1a_Ea`:核心 S(窗口 50)

- 核心:`sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))`;评分 94 次,过线 2,入 heads **2**。
- 采样计数:`{'c05_no_core': 2402, 'c05_periphery_seen': 6, 'mutation_refused': 2, 'c05_skeleton': 2}`(解读见 §1.5)。
- 试了三组外围(假设里的 A / B / C):
  - **(A) 钉在哪里**(`ts_mean(sub(day_at_max_ratio(Vwap), day_at_min_ratio(Vwap)), 50)`、`ts_mean(day_signed_ratio(in_delta(Vwap,1), Volume), 50)` 乘到 `inv(ts_decay_linear(S, 40))` 上)——**3 个种子活到最后,产出 0 个 head**。
  - **(B) 为什么钉住**(`day_distinct_ratio(Vwap)` / `day_flat_ratio(Vwap)` / `day_last(Close)` 做分桶去均值、截面残差、比值)——**全军覆没,被审计员和相关度表划光**。
  - **(C) 何时进入**(`ts_delta(ts_decay_linear(S,20),20)`、`sub(ts_decay_linear(S,10), ts_decay_linear(S,60))`)——**两棵 head 都出自这里**:
    - +0.788 `sub(ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 10), ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 50)), 60))`
    - +0.717 同一个骨架,被减项里又嵌了一层 `sub(S, ts_decay_linear(S,60))`
- **判读**:两棵 head 都是「S 的一个平滑 减 S 族另一个平滑」,**没有引进任何第二个字段**。
  (A) 想带进来的「钉价方向」一个都没活下来;外围里新出现的算子只有 `sub`。
  score 也比 S 族本来的 head 低(0.79 / 0.72 vs 1.155)。
  唯一的正面价值:时间差分形式与 S 的**水平**相关性应该明显低于其它 S 族 head,对最终融合可能有一点分散贡献(本轮 corr 表会给出,`loc.json` 里没有)。

### 3.2 N 位 `c06s802Cr1b_Nb`:被吸收的订单流

- 评分 86 次,过线 5,入 heads **1**(+0.887)。5 个过线候选**全部**是 `cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret))` 加时间衰减,
  **没有一个是差值形式** `sub(day_signed_ratio(Ret,Volume), day_signed_ratio(Ret,Ret))`。
- 所以第 1 轮登记的那个分叉落在「残差」这一支:**信息在「订单流里当日价格解释不掉的那部分」,不在订单流本身,也不在「订单流 − 效率比」这个差上**。
- 方向更正见 §1.2:实际 sign = **+1**(做多被吸收的**买**压),与 PI 预期相反、与 Chordia-Subrahmanyam(2004)一致。

### 3.3 审计员挡掉了什么、为什么(两次审计,最终 a / b 两位都过,R 组 1–4 过、R 组 5 第 1 次被删后重写才过)

| 位 | 划掉 | 理由(归类) |
|---|---|---|
| a(E) | 种子 3、6、8、9、10、11 | **规则硬划**:与某个 head 的 \|ρ\| ≥ 0.7(0.72 / 0.77 / 0.73 / 0.89 / 0.89 / 0.91) |
| a | 种子 7、8 | **陷阱 3**:`day_distinct_ratio(Vwap)` 数的是分钟 Vwap 有多少个不同值,活跃分钟在多个价位成交 → 它主要反映**成交活跃度**,拿它做除数就是流动性的非线性函数(liq 0.59 / known 0.58) |
| a | 种子 4 | 无符号的 `day_at_min_ratio` 只放大缩小、不分方向 → 换皮(残差 ρ 0.81) |
| a | 种子 6 | **陷阱 2**:P 在流动性好的股票上大量恰好为 0,`cs_bucket_demean` 的 `_buckets` 把这一大块并列按列序切进不同的桶 |
| a | 种子 11 | 机制没实现:`day_last(Close)` 是**后复权价**,与真实价位差 2.5–113 倍,不是 Harris(1991)说的最小价位约束 |
| a | 种子 14(attempt 2 补划) | 两个以 0 为中心的**有符号**量相乘 → 同一端装的是「刚进入多头状态且钉在低点」和「刚离开多头状态且钉在高点」两群股票,没有共同理由;与所有 head、所有控制 \|ρ\| ≤ 0.07,接近噪声 |
| b(N) | 种子 8、11 | **规则硬划**:与 20 日反转控制 \|ρ\| 0.56 / 0.57 —— 裸订单流没扣价格方向,就是反转的另一种写法 |
| b | 种子 9 | `ts_autocorr × ts_mean` 两个有符号量相乘,「反持续+净卖」和「持续+净买」落在同一端(与 a 位种子 14 同理) |
| b | 种子 12 | `ts_corr(OF, day_sum(Ret), 40)` 量的是耦合强度、丢掉方向,且 liq 0.39 / known 0.33 |
| b | 种子 14 | 废品:`ts_rank(·, 60)` 在 60 日窗口里只有 60 个取值,distinct 0.048 不过门槛 |
| R 组 5(第 1 次) | 整组删掉,合理度 **1** | PI 说「DW 的 Volume→Amt 让价格水平不同的股票更可比」,但 **DW 对同一只股票同一天尺度不变**,变体与原 head \|ρ\| = 0.998;而且「四棵里三棵 Amt ≥ Volume」是读错拆解表,+0.13 只来自 valid → **判为数字游戏** |

**可以反复用的三条审计口径**(本轮写种子时自己先过一遍):
1. 两个**有符号、以 0 为中心**的量相乘 → 四个象限塌成两端,机制没实现。审计员两个位都用这条划人。
2. 分桶 / 去均值用的变量在一部分股票上**大量并列**(恰好为 0、少数取值)→ `cs_bucket_*` 按列序切桶,陷阱 2。
3. 任何「尺度不变的统计量换个同口径字段」(DW 换 Volume/Amt、后复权价当真实价位)→ 先自己算一遍不变性,再写理由。

### 3.4 R 的替换与收录

15 个变体,**2 个替换、0 个收录**(`R_prev.json`;规则是一棵 head 只取最佳合格变体,`c05_locate.py:220`):

| 原 head | 采纳的变体 | score |
|---|---|---|
| `inv(ts_decay_linear(inv(sigmoid(ts_regbeta(…, 50))), 40))` +0.730 | `inv(ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100)), 40))` | **+1.0477** |
| `inv(pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(…, 50))))))))` +0.834 | `inv(pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100))))))))` | **+1.1555** |

没被采纳的 13 个里,有信息量的几条:

- **「两个各自有效的窗口方向不能叠加」**:`regbeta 100 + decay 80` = **+1.088**(比原 head +1.1438 **更低**);单独 `decay 120` = +1.166(gain 只有 +0.022);单独 `regbeta 100 + decay 40` = +1.136。
  两个改动做的是同一件事(拉长平均、降噪),叠起来是**过度平滑**,不是互补。
- t 值族全崩(见 §1.1 第 2 条)。
- `in_scale` 族全崩(见 §2 最后第二行)。

### 3.5 上一轮笔记里的预测,对不对

| # | 预测(`notebook.md` / `r1/analysis.md` §6) | 结果 | 判 |
|---|---|---|---|
| 1 | E 产出 1–3 个 head,**大概率出自 (A) 组钉价方向**,score 0.6–1.0 | 2 个 head,score 0.79 / 0.72(**在区间内**),但全部出自 **(C)** 组;(A) 产出 0 | **一半错** |
| 2 | (B) 组的分桶 / 截面残差多半被相关度表划掉,14 个里划掉 4–6 个 | (B) 全军覆没;总共划掉 9 个,剩 5 个 | 方向对,**数量低估** |
| 3 | **(C) 组不看好,score < 0.4** | (C) 的种子 13 是两棵 head 的共同祖先 | **错** |
| 4 | 「若 E 只产出纯平滑 / 纯单调的变体,说明 S 已榨干,第 2 轮不再给 S 第二个 E 位」 | 产出的是 S 对 S 的**时间差分**(不是纯单调,但**没有第二个字段**);(A) 带新字段的那一支全灭 | **实质触发**:见 §4.1 |
| 5 | N 产出 1–2 个 head,score 0.5–0.8,与所有 head \|ρ\| < 0.2 | 1 个 head,score **+0.887**(略高于区间);ρ 待本轮 corr 表 | **大体对** |
| 6 | N 的方向 sign = **−1**(做多被吸收的卖压) | 实际 **sign = +1**(被吸收的买压) | **错**,而且是文献对、PI 错 |
| 7 | 裸订单流种子会因与 20 日反转 \|ρ\| ≥ 0.5 被划掉 | 种子 8 / 11 正是这样被划(0.56 / 0.57) | **对** |
| 8 | 「若最终 head 是残差 / 差值形式而裸订单流不行 → 信息在被吸收的那部分」 | 5 个过线候选全是 `cs_regres` 残差,差值形式一个没进 | **对**,并进一步缩到「残差」而非「差值」 |
| 9 | R1 去掉内层 `inv` 会替换原 head | +0.9608,replaces=true(最终被同组更高的窗口 100 版顶掉) | **对** |
| 10 | R1 的 t 值版 ≥ +0.80 | **−0.273** | **错** |
| 11 | R2 窗口 100 → +1.16,替换 | +1.0477(这棵 head 上),替换成立 | **对** |
| 12 | R3 `regbeta100+decay80` > +1.243;`decay120` 落在 1.20–1.30 | **+1.088** / **+1.166** | **两条都错** |
| 13 | R4 `in_scale` 版掉到 < 0.4(B 是流动性残留) | −0.067 / −0.032 / −0.305 / −0.578 | **对**(登记后果:不给 B 第 2 轮的 E 位 → 照办) |
| 14 | R5 有一半把握至少一个 t 值变体 ≥ 原 head + 0.1;**若两个都掉分 → 第 2 轮不在这棵 head 上花 E 或 R** | −0.771 / −0.615 | **错**,登记后果**触发** |
| 15 | `r1/analysis.md` §6-1 的两个代数对账 | PI 没把它们写进 R 组,**未检验**。但有两条免费的旁证支持管线模型:`cs_regres` 幂等那两对分数**逐位相等**;`cs_*` y 位单调包装必要性**恰好 0.0000** | 未测,间接支持 |
| 16 | §6-2「过线的 head 会含第二个叶子或一个二元 / 分桶算子」 | 含二元算子 `sub`,**不含第二个叶子** | **一半对** |

**自评**:可判的 15 条里,完全对 6 条、一半 3 条、错 5 条、未测 1 条。错的那几条有一个共同模式:
**凡是「两个各自有效的改动叠起来会更好」或「我先验觉得哪一支会赢」的预测都错了;凡是「这个部件是水平量 / 代理,换成尺度无关版会崩」的预测都对了。**
本轮据此调整:不再预测「哪一支赢」,只预测**可证伪的崩 / 不崩**。

---

## 4. 本轮候选

### 4.1 值得深挖的核心(≤3,按推荐度)

#### 核心 1(强烈推荐,E 位就用它)

```
cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret))
```

- 证据:§1.2。库里 16 个 head 里唯一一份与价格钉住 / 波动 / 市值 / 价格水平都无关的信息;而且是**我们自己做出来的**。
- 短:3 个算子、2 个叶子。可用节点预算几乎全留给外围。
- 奖励与控制:`cs_regres` 已经把同日截面收益投影掉,这正是与 20 日反转控制重合的那块(裸订单流种子就是被 rev 0.56 划掉的)。
  **PI 下笔前必须在 corr 表上确认核心本身与 5 个控制的 |ρ| < 0.5**(规则 §3 对 E 核心的硬要求);
  第 1 轮同族种子里有 size \|ρ\| 0.24–0.34、rev 最高 0.44,**rev 是最可能出事的那一个**。
  若核心本身的 rev ≥ 0.5,退一步用 `ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 20)`(已评过 +0.52)当核心。

**已经见过的外围写法**(我能看到的;`--periphery-seen` 实际喂的是 300 个存档候选,`n_with = 14`,所以已见集合 ≤14 个):

| 来源 | 外围算子名集合 |
|---|---|
| 核心自身(永久禁) | ∅ |
| head +0.887 `ts_decay_linear(ts_decay_linear(…, 20), 40)` | {`ts_decay_linear`} |
| +0.62 / +0.52 `ts_decay_linear(…, 40)` / `(…, 20)` | {`ts_decay_linear`} |
| +0.62 / +0.52 的双层 `cs_regres` 版 | {`ts_decay_linear`, `cs_regres`, `day_sum`} |
| (第 1 轮 N 位 96 次评估里 GP 自己长出来的变异,我看不到,但都在 SEEN 里) | — |

**这次外围该做什么(四条,都带进核心以外的新输入或新轴)**:

1. **测量质量筛(把 §1.3(d) 的发现搬过来)。** 核心是一个**分钟级 tick rule 统计量**:
   `day_signed_ratio(Ret, Volume) = Σ|V|·sign(Ret)/Σ|V|`,零收益分钟只进分母。
   所以在「成交集中在少数分钟」(`day_gini(Volume)` 高)或「零收益分钟占比高」(`day_zero_ratio(Ret)` 高)的股票上,这个比值由极少数几分钟决定,**是噪声而不是信号**。
   用 `cs_last_high10(核心的平滑, day_gini(Volume))`、`cs_last_high10(…, day_zero_ratio(Ret))`、`cs_last_high10(…, day_max(Volume))` 把这些名字排除出多头书。
   这是一个**测量误差**理由,不是数字游戏,而且和 M 自己找到的结构是同一个 —— 但 y 换成了不是陷阱的东西。
   ⚠️ 两条:`day_gini(Volume)` 的 rho_known = 0.674,筛会把变体的已知族相关往 −0.4 推(§1.3(d)),种子里要同时放 `day_zero_ratio(Ret)` 和 `day_max(Volume)` 版做对照;
   筛的 x 位不要用并列很多的量(`cs_last_*` 的 x 位虽然整块安全,但一个 50% 都并列的 x 会让「最高 10%」变成空集)。
2. **谁在吸收 —— 和 S 族的机制接头(库里两份真信息第一次相遇)。**
   S 说的是「价格被钉在一个价位 + 成交量变平稳」= 盘口在一档被持续吸收;核心说的是「订单流被吸收」。
   两件事指的是同一个现象的两个侧面,而**库里没有任何 head 把它们放在一起**。
   写法:`mul(核心的平滑, ts_mean(day_flat_run_max(Vwap), 60))`、
   `cs_last_low10(核心的平滑, ts_mean(day_flat_run_max(Vwap), 60))`(只在「价格黏」的那群里交易订单流残差)、
   `cs_bucket_demean(核心的平滑, ts_mean(day_durbin_watson(Volume), 60))`(与同样粗糙度的股票比)。
   注意 `day_flat_run_max(Vwap)` 自身 distinct 只有 0.139,**必须先做滚动均值或只当 x / 桶变量用**,不能当被排序的 y。
3. **把第 1 轮 E 位唯一真的有效的时间操作搬过来(跨核心迁移)。**
   S 的 96 次评估里,产出 head 的不是乘法、不是分桶,而是 `sub(ts_decay_linear(·, 10), ts_decay_linear(·, 60))` 这个**短平滑减长平滑**。
   核心这边已知「越平滑越好」(20→+0.52、40→+0.62、20+40→+0.887),所以对称的问题是:
   是「长期一直被吸收」还是「最近刚开始被吸收」给分?`sub(ts_decay_linear(核心, 10), ts_decay_linear(核心, 60))`、`ts_delta(ts_decay_linear(核心, 20), 20)`。
   这一条便宜、有先例、且外围算子名集合({`sub`, `ts_decay_linear`})是新的。
4. **持续性(拆单的痕迹)。** `mul(ts_autocorr_s1(核心, 60), ts_mean(核心, 20))` 这个写法第 1 轮被审计员以「两个有符号量相乘」划掉过,**不要再写**。
   改成只用持续性当筛 / 桶:`cs_last_low10(ts_decay_linear(核心, 40), ts_autocorr_s1(核心, 60))`(只在订单流有自相关 = 像拆单的那群里交易)。

#### 核心 2(备选;我**不推荐**用它,除非 PI 不接受核心 1)

```
sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100))
```

- 理由见 §1.1:充分性强(窗口 100 的 `pow_1_5(inv(sigmoid(·)))` 单独 +0.887 / valid 2.97)、必要性强(+3.30 / +0.347)、窗口单调。
- **但是**:第 1 轮已登记的条件触发(§3.5 第 4 条);t 值检验失败说明一部分分数可能来自饱和挑选(§1.1 第 2 条);
  `Vwap→Close` 在窗口 100 上只掉 0.147,原来那条「必须是有成交的价格」的机制证据站不住了;
  而且库里已经有 **7 个** S 族 head(+1.155、+1.144、+1.048、+0.832、+0.788、+0.717、+0.712),最终融合会砍掉大部分,第 8 个的边际价值接近 0。
- 规则提醒:S 已用掉 1 个 E 位(每个核心整个实验至多 2 个)。窗口 100 与窗口 50 是不同的表达式,
  但审计员评 E 位创新度是看**外围**,所以换窗口换不来创新度;而第 1 轮的外围已经把
  `mul` / `inv` / `ts_decay_linear` / `ts_delta` / `sub` / `cs_bucket_demean` / `cs_regres` / `div` / `day_at_max_ratio` / `day_at_min_ratio` / `day_distinct_ratio` / `day_flat_ratio` / `day_last` / `day_signed_ratio` / `in_delta` / `ts_mean` 全部烧掉了。
- 如果 PI 还是要用,**唯一还没试、而且第 1 轮文献员专门推荐过的外围只有两个**:
  (i) **`LimitWidth` / `BoardCode` / `ListAge` 分组** —— 三个日频叶子里这三个**一个 head 都没用过**,而 S 的机制故事就是涨跌停封板,
  带宽是这件事的制度参数。实现必须用 `cs_last_*` / `cs_first_*`(整块安全)或 `div(·, LimitWidth)`,**不能用 `cs_bucket_*`**(§1.4);
  (ii) **Scholes-Williams / Dimson 的前导+滞后斜率** —— 自变量 `day_flat_run_max(Vwap)` 本身就是「价格稀疏变化」的度量,
  经典文献说这种情况下同期 OLS 斜率向零偏。写法 `add(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100), ts_regbeta(cross_delay(day_flat_run_max(Vwap), 1), day_durbin_watson(Volume), 100))`(`cross_delay` 在 `dt_cross.py:150`)。
  这两条第 1 轮文献员都列为「最硬、可直接改算子」,也都还没试。

#### 核心 3(**只做 R,不做 E**)

```
cs_last_high10(cross_quantile_q25(LogFloatShares, 241), day_gini(Volume))        ← head +1.089 的等价形式
cs_last_high10(cross_quantile_q25(LogFloatShares, 241), day_max(Volume))         ← head +1.294 的等价形式(§1.4)
```

筛是好部件(+0.53 / +0.74),但:
- `day_gini(Volume)` 作为核心会被规则直接挡掉(rho_known **0.674** ≥ 0.5);
- 整棵树作为核心会把 `LogFloatShares` 这个价格水平代理**原样**带进每一个候选 —— 那是把 96 次评估押在陷阱 3 上;
- 所以正确的用法是:**筛当核心 1 的外围(§4.1 核心 1 第 1 条),y 当 R 的替换目标(§4.2 A 组)。**

### 4.2 R 目标(PI 从里面挑 ≤16;每条都写了门槛、预期和「不管涨跌都学到什么」)

**B 组:S 族,先把白送的分拿走,再做一次判决性检验(5 个变体)**

| # | 原 head(门槛) | 变体 | 预期 |
|---|---|---|---|
| B1 | +1.155(≥ **1.256**) | `inv(pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 200))))))))` | 拆解已测 **+1.3933**,gain +0.238,同族 ρ 必 ≥ 0.5 → **替换**。本轮最确定的一分,别漏 |
| B2 | 同上 | 同一棵,`ts_regbeta` 窗口改 **400** | 检验「越长越好」是否单调。**注意 train 从 2018-01-02 起、warmup 60,400 日窗口会吃掉 2018–2019 大半,coverage 可能明显掉**。若 400 继续涨 → 这个量正在退化成一个几乎静态的个股特征,**那是样本外风险的信号,不是好消息**;若掉 → 200 是边界,与第 1 轮文献员查到的「成交量结构记忆约 40 个交易日」(Heston-Korajczyk-Sadka 2010)量级对得上 |
| B3 | +1.048 `inv(ts_decay_linear(sigmoid(ts_regbeta(…, 100)), 40))`(≥ **1.148**) | `inv(ts_decay_linear(sign(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100)), 40))` | **本轮最该做的一发。** `sign` 保留「近似取符号」的形状、彻底去掉 σ_y/σ_x。≥1.148 → 「信息在符号 + 处在状态的天数里」成立,t 值失败只是因为 `sigmoid(t)` 在 n=50 时是 ρ 的平滑函数;< 0.9 → **饱和挑选(带波动)是分数的一部分,S 族整体降级,第 3 轮不要再碰** |
| B4 | 同 B3 | `inv(ts_decay_linear(sign(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100)), 80))` | B3 的平滑长度对照(符号序列的计数需要更长窗口才细) |
| B5 | 同 B3 | `inv(ts_decay_linear(sigmoid(ts_regbeta(day_flat_ratio(Vwap), day_durbin_watson(Volume), 100)), 40))` | `day_flat_run_max`(最长**一段**)换成 `day_flat_ratio`(全天相等分钟的**占比**)。`Vwap→Close` 在窗口 100 上只掉 0.147,说明「连续一段」这个细节可能根本不重要;这一次直接问它。掉分 → 「最长连续段」是必要的,封板读法活;持平 → 它只是「价格有多黏」的一个粗糙代理 |

**A 组:把筛从陷阱 y 上搬下来(6 个变体)**

理由(写给审计员的):y = `LogFloatShares` / `cross_quantile_q25(LogFloatShares, 241)` 是烂部件 ——
`LogFloatShares = LogFloatCap − log(价格)`,中性化控制了 `LogFloatCap` 而没有控制价格,所以 y 的残差主要是低价股效应(陷阱 3);
y 单独只有 +0.558,筛贡献 +0.53~+0.74;`day_max(Volume)→day_max(Amt)` 让整棵从 +1.294 崩到 −0.171,证明两个输入都挂在价格上。

| # | 原 head(门槛) | 变体 | 预期 / 学到什么 |
|---|---|---|---|
| A1 | +0.856 `cs_last_high10(cs_last_high10(LogFloatShares, day_durbin_watson(High)), day_durbin_watson(Vwap))`(≥ **0.956**) | 内层 y `LogFloatShares` → `ts_decay_linear(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 20), 40)` | **门槛最低的一棵**(只需比我们自己的 +0.887 再高 0.07)。⚠️ 收录要求与库里**所有** head \|ρ\| < 0.7,而被换进去的 y 本身就是库里那个 +0.887 的 head,`cs_last_high10` 只把 10% 的名字压到底部、其余保持原秩 → **很可能 ρ ≥ 0.7 被 0.7 禁令挡掉,拿不到收录**。即便挡掉,分数本身就回答了「筛能不能迁移」,而且答案可以直接写进 E 位的种子 |
| A2 | +1.089(≥ **1.189**) | y → 同上的订单流平滑(筛是 `day_gini(Volume)`) | 同 A1,门槛更高。两条一起做可以看出两个筛哪个更能迁移 |
| A3 | +1.294(≥ **1.394**) | y → `pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100))))`(筛是 `day_max(Volume)`) | 把筛迁到 S 族上。S 族也是分钟级统计量,同样怕成交集中。1.394 的门槛很高,主要价值在诊断 |
| A4 | +1.294(≥ **1.394**) | y → `LogFloatCap`,即 `cs_last_high10(cross_quantile_q25(LogFloatCap, 241), day_max(Volume))` | **判决性诊断,预期大跌,不求收录。** 若崩 → y 的 alpha 恰好是 `LogFloatShares − LogFloatCap = −log(价格)`,M 这 4 棵 head 判定为低价股代理,第 3 轮一律不碰;若不崩 → 我的读法错,这一族里有真的规模信息 |
| A5 | +1.294(≥ **1.394**) | y → `day_quantile_q25(Open)`(价格水平本身) | A4 的另一面:若它复现 ≈1.29(sign 由奖励扫描,正负不要紧),则 y ≡ 价格水平,结论闭合 |
| A6 | +1.070 `cs_last_low20(cross_quantile_q25(LogFloatShares, 241), day_durbin_watson(Vwap))`(≥ **1.170**) | y → 订单流平滑 | 第三个筛(排除 DW(Vwap) **最低** 20%)的迁移测试 |

A4 / A5 是两次便宜的判决性评估,**它们不会被收录,但会一次性定下 M 这 4 棵 head(库里 1/4 的 head)到底是不是代理**,
直接决定第 3 轮要不要在「筛」这条线上继续投入。我认为值得。

**C 组:两笔欠账(2 个变体,低优先,有余额再做)**

| # | 原 head(门槛) | 变体 | 预期 |
|---|---|---|---|
| C1 | +0.537 `day_mean(neg(in_delta(Volume, 60)))`(≥ **0.637**) | `day_centroid(Volume)` | 把整段 `neg(in_delta(·,60))` 换成**成交量重心**(`ops_ext.py:155`,∈[0,1],0=全在开盘、1=全在收盘,分母是当日总量,天生尺度无关,而且用上全部 241 分钟而不是首尾两小时之差)。**诚实说明:R4 已经把「水平」和最简单的那个尺度无关写法(首小时占比 − 尾小时占比)都否了(−0.07 ~ −0.58),所以我对这一条的期望不高**;它的价值是用 1 次评估给「日内时点到底有没有横截面信息」一个干净的答案,而不是再用一个 96 次的 N 位去赌 |
| C2 | 同上 | `day_mean(in_delta(Volume, 60))` | 代数对账:`day_mean` 线性 ⇒ `day_mean(neg(x)) ≡ −day_mean(x)`,而奖励对 sign ±1 做扫描(`steer.py:638`)⇒ 分数**必须精确等于 +0.537**。不等则 §1.4 / §1.5 对管线的理解有错,后面所有「单调包装 / 恒等」的论断都要推翻。第 1 轮欠的账 |

**明确不做的 R**:(i) 任何给 `day_durbin_watson` 再加凸变换的变体(陷阱 1,合理度 1);
(ii) 两棵嵌套 regbeta head 上的任何东西(第 1 轮登记后果已触发);
(iii) 剥掉 `cs_*` y 位单调包装的变体 —— 拆解已经免费给了答案(必要性 0.0000),花钱是浪费。

### 4.3 N 的灵感(按我手上的证据排序,PI 定)

1. **流通股本的一年增量 = 解禁 / 摊薄的供给冲击(最推荐)。**
   M 的 4 棵 head 都在用 `cross_quantile_q25(LogFloatShares, 241)`,而拆解显示这层包装里**唯一不是死重的部分正是那个 241 日滞后**(必要性 +0.1518,其余 0.0000 / 0.0023)。
   也就是说:用「一年前的流通股本下沿」比用「当前值」更好。这**暗示有信息的其实是变化量**,而 M 只是碰巧用了一个带滞后的水平量。
   把它写明白:`ts_delta(LogFloatShares, 241)`、`sub(LogFloatShares, cross_quantile_q25(LogFloatShares, 241))` = 过去一年流通股本的对数增长 = 限售股解禁 / 增发造成的**供给冲击**。
   - 为什么是新信息:库里 16 个 head **没有一个**用到任何日频叶子的**变化**;`LogFloatShares` 的**水平**是低价股代理(§1.3(b)),但它的**增量**不是 —— 增量和 `LogFloatCap` 的相关性由中性化处理,剩下的是「谁被稀释了」。
   - 为什么机制清楚:解禁日期在上市 / 增发时就确定、提前可知,是外生的供给事件;A 股的减持 / 解禁研究是一个成熟的实证方向。
   - 和 `ListAge` 的天然交互(锁定期按上市 / 定增时点计):`ListAge` 和 `LimitWidth`、`BoardCode` 一样,**6 个日频叶子里这 3 个一个 head 都没用过**。
   - 要先确认的事:这个量在数据里有没有时间变动。有两条间接证据 —— 若 `LogFloatShares` 逐股恒定,那层 `cross_quantile_q25` 的必要性就会是 0.0000 而不是 0.1518;
     另外 `scripts/server/c04_smoke.py:22` 的日频叶子体检里直接用了 `ts_delta(LogFloatShares, 20)`,说明这个面板本来就被当成会变的。
   - 预期的创新度:输入与机制都和库里不同 → 4(5 要看文献里是不是没有)。
2. **测量质量筛,作为一个独立的机制族。** 如果 PI 决定两个 GP 位都是 E,这一条就并进核心 1 的外围(§4.1 核心 1 第 1 条)。
   如果留一个 N 位,可以做成「分钟级统计量的可信度」这个主题:
   `day_zero_ratio(Ret)`(零收益分钟占比)、`day_gini(Volume)`、`day_max(Volume)`、`day_distinct_ratio(Vwap)` 当**筛 / 桶**,
   被筛的 y 是订单流残差、S 族、`day_topw_mean(Ret, Volume)`。
   机制是测量误差而不是风险溢价,所以它只能**改进别的信号**,不能单独当因子(`day_gini(Volume)` 单独 −3.67 就是证明)。
   作为 N 位的风险:审计员可能判「这是 E 的外围,不是新 idea」。作为 E 外围更稳。
3. **「幅度是噪声」做到底(便宜,放 R 更划算)。** `sign(β)` 的符号占比族,见 §4.2 的 B3 / B4。用 2 次 R 评估就能拿到答案,不值得一个 96 次的 N 位。
4. **(降级)日内成交时点。** R4 把这条线砸得很狠(§3.4)。只留 §4.2 的 C1 一次评估,不要给 N 位。

**我对两个 GP 位的建议**:E = 核心 1(订单流残差,外围 = 测量质量筛 + 与 S 的机制接头 + 短减长平滑);N = 灵感 1(流通股本增量)。
S 族不占 GP 位,只占 B 组的 5 个 R 变体(B1 是白送的替换,B3 是判决性检验)。
规则 §2 的「3 轮里至少 1 个 N 位通过审计」第 1 轮已经满足,所以第 2 个位置用 N 不是被迫的,是因为它的边际正交性最高。

---

## 5. 文献题目(给文献员,只能用 2023-08-08 之前发表 / 提交的)

**L1(对准核心 1:订单流残差的测量误差与持有期)**
用分钟 bar 的 tick rule 构造日度净主动买入占比(`Σ|V|·sign(r)/Σ|V|`)时,文献对**测量误差**做哪些处理?
具体想知道:(a) 零收益 / 无成交分钟怎么处理(只进分母、剔除、还是用上一笔方向填充),低价股和薄盘股的符号分类误差有多大、文献怎么纠正;
(b) 有没有按「当日成交集中度 / 分钟笔数 / 零收益分钟占比」**筛掉或分组**一部分股票再做横截面检验的做法;
(c) 订单不平衡**对当日收益取残差之后**预测未来收益的**最优持有期 / 平滑长度**一般是几天(我们这边 20 日 < 40 日 < 20+40 日两层衰减,越慢越好,想知道文献里这个单调性到哪里为止);
(d) **方向**:在中国 A 股,是「买方不平衡之后收益更高」还是相反?(我们的 train 给出 sign = +1,即做多被吸收的买压,与 Chordia-Subrahmanyam 2004 一致,与我们第 1 轮的事先预期相反,想要一个 A 股的直接证据。)
关键词:订单不平衡、主动买卖盘、净主动买入、tick rule、分笔方向判定、成交量分类、A 股散户机构交易结构;
order imbalance, trade direction classification, tick rule / bulk volume classification, Lee-Ready algorithm misclassification, order imbalance persistence and horizon, order imbalance in Chinese A-shares, retail vs institutional order flow China.

**L2(对准核心 1 的外围:把「排除筛」当因子构造的一个部件)**
文献里「**先按某个指标把一部分股票排除出组合 / 分组,再对剩下的做排序**」这种做法有哪些标准形式和证据?
具体想知道:(a) 低价股 / penny stock / 流动性筛在横截面研究里通常怎么设(百分位还是绝对门槛),剔除它们之后异象收益怎么变;
(b)「当日成交集中在少数分钟」(成交量基尼 / 单分钟峰量占比 / 大单集中度)在文献里被当成什么 —— 知情交易、流动性不足、还是统计量不可靠的标志?
(c) 有没有文献明确区分过「同一个指标单独当因子没用、但当筛选条件很有用」这种情形,并给出解释?
关键词:样本筛选、低价股剔除、流动性过滤、成交集中度、大单占比、知情交易概率、条件化因子;
penny stock filter, liquidity screens in cross-sectional asset pricing, sample screens and anomaly returns, intraday volume concentration / Gini of volume, trade size concentration and informed trading, conditional (double-sort) screens vs standalone factors.

**L3(对准灵感 1:流通股本增量 = 解禁 / 摊薄的供给冲击)**
限售股解禁 / 定向增发后流通股本增加,对股票横截面收益有什么影响?文献里这个量**怎么构造**?
具体想知道:(a) 用的是解禁股数 / 流通股本的比例、还是流通股本的对数变化、还是事件窗口哑变量,时间窗口取多长(事件前后几天 / 几个月);
(b) 效应的**方向和时点**:解禁前后是跌还是涨,是价格压力(临时)还是信息(持久);
(c) 中国市场(大小非解禁、定增解禁、减持新规)的直接证据;
(d) 这个量和**市值 / 价格水平 / 上市年龄**怎样分开(我们的奖励已经线性控制了 `LogFloatCap`,但没控制 `LogFloatShares` 和价格,想知道文献用什么控制);
(e) 锁定期到期与上市年龄的机械关系(1 年 / 3 年),有没有人直接用「上市年龄」当工具。
关键词:限售股解禁、大小非、定向增发解禁、减持、股本扩张、供给冲击、价格压力;
lockup expiration and stock returns, IPO lockup expiry price pressure (Field-Hanka), seasoned equity offering share supply, share unlocking in China / non-tradable share reform, float increase and returns, supply shocks and price pressure.

**L4(对准核心 2 与 M 第 2 批最高分那棵 head:「最近的极端日」类因子)**
把一个日度量(已实现方差、日内粗糙度)**先做凸变换、再做指数加权平均、最后才横截面排序**,等价于按「最近 N 天的极大值」排序。
文献里这类「最近极端日」因子是什么、有没有被证实、和低波动异象是什么关系?
具体想知道:(a)「过去一个月的最大单日收益 / 最大波动」这类因子的横截面证据(方向、幅度、在中国市场是否存在);
(b) 它和特质波动率 / 已实现方差 / 已实现偏度 / 低波动异象的关系 —— 是同一个东西的不同写法,还是独立的;
(c) 文献里把波动类因子的**非线性部分**与线性波动控制分开的标准做法(分桶、残差、还是直接用极值统计量);
(d) 顺带:滚动回归斜率当横截面因子时,**窗口长到什么程度就变成一个几乎静态的个股特征**、文献里有没有讨论过这个退化(我们这边窗口 50→100→200 分数单调上升,想知道这是降噪还是在变成个股固定效应)。
关键词:MAX 效应、最大单日收益、彩票型股票、特质波动率异象、低波动异象、已实现方差、已实现偏度、极值统计量;
MAX effect (Bali-Cakici-Whitelaw), lottery-like stocks, idiosyncratic volatility puzzle, low-volatility anomaly, realized variance / realized skewness as cross-sectional factors, nonlinear transformations of volatility and factor neutralization, rolling beta window length and signal persistence.

---

## 6. 本轮写下的预测(留给第 3 轮对账)

按 §3.5 的自评,这次只写可证伪的崩 / 不崩,不预测「哪一支赢」。

1. **A4(`LogFloatShares → LogFloatCap`)会掉到 < +0.7**(原 head +1.294)。若它反而 ≥ +1.2,我对 M 这 4 棵 head 的「价格水平代理」判定是错的,§1.3(b) 要推翻。
2. **A5(y 换成 `day_quantile_q25(Open)`)落在 +1.0 ~ +1.4**(即大致复现原 head)。1 和 2 同时成立,则「y ≡ −log(价格)」闭合。
3. **B1(`ts_regbeta` 200)会替换 head +1.155**(拆解已给 +1.3933,这里只是走完 R 流程)。
4. **B3(`sigmoid` → `sign`)我押它 ≥ +1.0,但不敢押过 1.148 的替换线;给 50% 的把握落在 [1.0, 1.3]。**
   若 < +0.9,则 S 族的分数有实质一部分来自 sigmoid 的饱和挑选(σ_y/σ_x,带波动),**第 3 轮不再在 S 族上花任何位**。
5. **B2(窗口 400)coverage 会掉到 0.95 以下**;分数我不预测方向。
6. **C2(`day_mean(in_delta(Volume, 60))`)精确等于 +0.537。** 不等 ⇒ §1.4 / §1.5 对管线的理解有错。
7. **E(核心 1)会产出 1–3 个 head,score 0.6–1.1;产出 head 的外围里会含一个 `cs_last_*` 筛或一个来自 S 族的第二输入**,
   而**只含 `ts_decay_linear` / `ts_mean` / `sub` 这类纯时间算子的候选不会超过 +0.95**(即不会比已有的 +0.887 高出多少)。
   若过线的全是纯时间平滑的变体,说明这个核心也只剩「改平滑长度」,第 3 轮不给它第二个 E 位。
8. **N(流通股本增量)最大的风险不是机制而是数据**:若 `ts_delta(LogFloatShares, 241)` 的 distinct 或 coverage 过不了门槛(逐股阶梯状、长期为 0),整个位会废掉。
   我给它 60% 的把握产出至少 1 个 head,且该 head 与现有 16 个 head 的 \|ρ\| < 0.2。
9. **A 组里凡是把 y 换成我们那个 +0.887 订单流 head 的变体(A1 / A2 / A6),即使分数够,也会被 0.7 库禁令挡在收录之外。** 若其中任何一个被收录,说明 `cs_last_high10` 的 10% 排除对日度秩相关的影响比我估计的大得多。
