# 结构解剖:种子 802,B 组,第 2 轮

读的东西:`r2/loc.md`、`r2/loc.json`(含每个变体的 coverage / distinct / sign / hl / rho_known / rho_head)、`r2/R_prev.json`(第 1 轮 16 次 R 直接评估的全部结果)、
`r1/loc.md`、`r1/loc.json`、`r1/analysis.md`、`r1/lit.md`、`r1/missions.yaml`、`notebook.md`、`PLAN.md`(含修订 1–9);
代码:`partura/ops_ext.py`、`partura/steer.py`(奖励管线 `172-181`、`403-440`、`625-650`)、`scripts/idea_search.py`(控制集 `158-189`、核心/外围判定 `295-335`)、
`scripts/c05_round.py`(家族控制 `220-229`、`seen` 来自全部存档 `216`)、`scripts/c05_lib.py`(`archive()` 只读 GP 存档 CSV)、`scripts/c05_locate.py`(共性 `204-234`、卡 `295-310`)、
`alphacube/operators/{common,dt_in,dt_day,dt_cross,nd_ts}.py`、`alphacube/dailyfields.py`、`alphacube/catalog.py`。

## 0. 三句话

1. **本轮最重要的一条是关于定位工具本身的**:共性表是把四次运行的分数**混在一个池子里**比较的,而第 1 轮 E 任务的 92 个候选是在**多了 5 个家族控制**的奖励下评的分(全部约 −1.5)。
   结果 `sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))` 的均值差从第 1 轮的 **+1.335(p 0.000)** 翻成第 2 轮的 **−0.774(p 0.999)**。
   **S 没有变坏,是我们自己把它的样本污染了。** 第 2 轮起,凡是做过 E 核心的子树(及其零件、及 E 种子里用过的算子)在共性表上的数字一律不可读;只有来自 M 各批的行是干净的。
2. **真正的新信息在 N 任务那一侧**:`cross_mean(day_mean(in_logchg(Volume, 60)), 20)` = +1.67(train 1.67 / valid 2.26),是全库第一。
   它是「日内成交量**几何均值**的尾段 ÷ 首段」的 20 日平均,对当日成交量的任何**乘性**缩放严格不变,所以它在数学上**不可能**是换手率水平、换手率趋势、规模或流动性的代理。
   第 1 轮那个 +0.54 的 `day_mean(neg(in_delta(Volume, 60)))` 是它未归一化的粗糙版本;R 的 16 次评估正好证明了**对数归一化行得通、份额归一化行不通**(+0.547 对 −0.067)。
3. **M 第 2 批给了一个机械发现和一条代理主线**:机械发现是 `pow_2(pow_2_5(day_durbin_watson(High)))` —— 指数 1 → 2 → 2.5 → 5 时 score 单调 **−1.17 → +0.27 → +0.72 → +1.45**,
   而同一天的截面排序完全没变;唯一变的是**凸变换让 EMA 变成了对窗口内的「软最大值」**。代理主线是 `LogFloatShares` / `day_quantile_q25(Open)` 那一簇(M2 的 7 个 head 里有 6 个碰它),
   按 `LogFloatCap = LogFloatShares + log(价格)`、而控制里有 `LogFloatCap`,它的残差一阶上就是**名义股价水平** —— A 股的低价股效应,不是新信息。

---

## 1. alpha 的来源

### 1.0 先把定位工具的两处偏差讲清楚(决定下面所有数字怎么读)

**(a) 共性表混了四种奖励。** `c05_locate.py:204-234` 把 `c05_lib.archive(snapshot)` 的全部 281 个有分候选放进一个池子,对每个子树比较「含它的均值 − 不含它的均值」。
但这 281 行来自四次运行:M1、M2(普通 `long_neutral`)、`c05s802Br1a_Ea`(92 次评分,奖励里**多了 5 个 S 家族控制**)、`c05s802Br1b_Nb`(81 次评分,普通奖励)。
E 的候选个个含 S、个个在更严的奖励下评分、最好的一个只有 −0.14。于是:

| 子树 | 第 1 轮(77 个存档) | 第 2 轮(281 个存档) | 真实含义 |
|---|---|---|---|
| `sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))` | +1.335,p 0.000,11 个 | **−0.774**,p 0.999,47 个 | 新增的 36 个几乎全是 E 的候选 |
| `ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)` | +0.990,p 0.001 | **−0.719**,p 0.999,51 个 | 同上 |
| `day_flat_run_max(Vwap)` | +0.776,p 0.007 | **−0.633**,p 0.998,57 个 | 同上 |
| `day_durbin_watson(Volume)` | +0.909,p 0.002 | **−0.622**,p 0.998,55 个 | 同上 |
| `day_flat_run_max(Close)` | —— | **−1.160**,9 个 | 全部来自我自己写的 E 种子 11、12 |
| `day_centroid(Volume)` | —— | **−0.805**,6 个 | 全部来自 E 种子 13(`mul(S, day_centroid(Volume))`,E 的最佳候选,valid +1.64) |
| `day_at_max_ratio(Vwap)` | —— | **−0.806**,10 个 | 全部来自 E 种子 8、9 |

**这七行没有一行能当「这个零件不好」的证据。** 特别是 `day_centroid(Volume)`:它的 −0.805 完全来自「它被放在 E 的家族控制下面」,
而 E 的最佳候选恰恰是 `mul(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), day_centroid(Volume))`(train −0.14 / **valid +1.64**)。
B0 按机械规则会把这些负数当「别碰」,这是错的。

**可以放心读的行**(只来自 M1 / M2 的存档,没进过我的任务):`inv(LogFloatShares)` 一族、`cross_quantile_q25(LogFloatShares, 241)` 一族、
`cs_bucket_zscore(day_quantile_q25(Open), sqrt(day_quantile_q25(Open)))`、`sqrt(day_quantile_q25(Open))`、`day_gini(Volume)`、`day_max(Volume)`、
`day_durbin_watson(Vwap)`、`day_durbin_watson(High)`、`pow_2_5(day_durbin_watson(High))`、`cross_regalpha(LimitWidth, day_sum(Open), 241)`。
**反向污染同样存在**:`div(day_last(Amt), day_sum(Volume))`(+1.256,4 个)、`day_last(Amt)`(+0.977,9 个)基本都来自 N 任务自己的种子谱系 —— 是「我押了它、它赢了」,不是独立证据。

**(b) 机械核心卡的前 4 张又是同一条信息。** 卡 #1–#4 全部出自同一个 head `inv(pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100))))))))`,
自身 score 1.2074 / 1.1969 / 1.1486 / 0.8869 —— 前三个几乎相同,因为 `inv(pow_1_5(inv(x))) ≡ x^1.5` 对正的 x 恒等,它们是**同一条信息的单调包装**(第 1 轮 §1.5 已证,本轮完全复现)。
卡 #5 `inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)))` 的 n_with 还是 8、均值差 +1.49 —— **和第 1 轮一模一样**,因为 E 的候选从没在 S 外面套 `inv`。所以卡 #5 是纯 M1 残留,不是新证据。
卡 #6–#8、#13 是 `LogFloatShares` 一族(见 1.4)。**B0 这一轮会把 E 位钉在卡 #1 上:一个比 S 长 6 个节点、信息和已有 5 个 head 完全相同的核心,而且家族控制会把它全部减掉。**

### 1.1 真来源(一):日内成交量的时间分布,对数口径 —— 本轮最硬的一条

```
核心:  day_mean(in_logchg(Volume, 60))                       自身 +0.5473(train 0.5473 / valid 0.7595)
head:  cross_mean(day_mean(in_logchg(Volume, 60)), 20)       +1.6680(train 1.6680 / valid 2.2596),sign −1,hl 5
```

**它在算什么(源码 + 代数)**:`in_logchg(x, d)`(`ops_ext.py:58`)= `log(x[t]/x[t−d])`,只在两端都 > 0 时有值,前 d 分钟为 NaN;
`day_mean` 对当日有限分钟取均值(241 根分钟,index 0 = 09:30 集合竞价,index 240 = 15:00)。于是

```
day_mean(in_logchg(Volume,60)) = [ Σ_{t=181..240} log V_t − Σ_{t=0..59} log V_t ] / 181
                               ≈ (60/181) · [ 末 60 分钟的对数成交量均值 − 首 60 分钟的对数成交量均值 ]
```

即**尾段与首段成交量的几何均值之比(取对数)**。sign −1 = 做多这个量低的一端 = 做多「**早盘重、尾盘轻**」。
第 1 轮那个水平口径的 head `day_mean(neg(in_delta(Volume, 60)))`(+0.537,sign +1)按同样的伸缩是 (首 60 根之和 − 末 60 根之和)/181,sign +1 也是做多早盘重 —— **两种口径方向一致**,PI 第 1 轮的方向预测对了。

**四条证据**:

| 维度 | 证据 |
|---|---|
| 充分性 | 子树单独 +0.5473(train 0.5473 / valid 0.7595),coverage **0.9993**、distinct **1.0000**、`rho_known` **−0.1275**。单独就过 0.5 的发现线,离已知族很远,而且不靠筛股票池。 |
| 必要性 | 没有 knockout 行(`cross_mean` 敲掉就是充分性那一行;`day_mean` 敲掉会留下分钟形状,按 §2.4 不做)。所以「必要性」这一维本轮是**空白**,下面用第 1 轮 R 的 16 次评估补。 |
| 敏感性(字段) | `Volume→Amt`:+1.6429(train 1.6429 / valid 2.1088)—— 基本不变,说明信息在**形状**不在量纲;但 `rho_known` 从 −0.1275 升到 **−0.3865**,所以 Volume 版更干净。 |
| 敏感性(窗口) | `cross_mean@20→10`:+1.4391(train 1.4705 / valid 1.4391);`@20→40`:+1.4516(train 1.4516 / valid 1.7114)。20 是个**平顶**(1.44 / 1.67 / 1.45),不是尖峰 —— 不是窗口过拟合。 |

**第 1 轮 R 给出的必要性(这是本轮最有价值的交叉证据)**:同一族的水平口径版本被拆了 4 次,

- `div(day_mean(in_delta(Volume, 60)), day_mean(Volume))`(除以当日平均分钟量 = 份额差)→ **−0.0666**(rho_head 0.4403)。**份额归一化把它杀死了。**
- `day_mean(neg(in_delta(Amt, 60)))`(水平口径换 Amt)→ **−1.8761**,而且 `rho_known` **−0.5243** 已越过 0.5 的不合格线。
- 窗口 30 → +0.3628;窗口 120 → +0.5579(rho_head 0.9795 / 0.9739)。60 与 120 相当,30 偏短。

把这三条和对数口径放在一起,结论很清楚:**信息在「典型那一分钟」的早晚之比里,不在「成交量最大的那几分钟」里。**
水平口径的差分被开盘那几根大柱子支配,除以当日均量之后剩下的就是这几根柱子的噪声(−0.067);Amt 水平口径还把价格和规模混进来(−1.876、rho_known −0.52);
对数口径对每一分钟等权,于是同样的经济含义在 +0.55 处稳住、再平滑 20 天到 +1.67。**对数是这一族的正确归一化方式,这是本轮用 16 次付费评估买到的、可以直接用的处理方式。**

**为什么它不是代理(这条可以严格说)**:`in_logchg` 比较的是**同一天内**第 t 分钟与第 t−60 分钟,所以把当日成交量整体乘上任何常数(换手率水平高低、日度放量缩量、规模、价格),
这个统计量**完全不变**。因此它在数学上不可能是换手率水平、换手率趋势、流动性水平、市值的另一种写法。
残余的一条流动性通道是:成交量为 0 的分钟变成 NaN、被 `day_mean` 跳过,稀薄的票被平均的分钟数更少 —— 但 coverage 0.9993、distinct 1.0、`rho_known` −0.13 说明这条通道很细。
(要做实只需一次条件化检验,见 4.2 第 12 条。)

**一处必须记下的上限**:平滑窗口越长,`rho_known` 越靠近不合格线(原始 −0.128 → 10 日 −0.308 → 20 日(head)→ 40 日 **−0.4443**)。
门槛是 |ρ| ≥ 0.5 判不合格,所以「再多平滑」这条路最多还剩一点余量就撞线。**E 的外围要找的是别的处理,不是更长的窗口。**

### 1.2 真来源(二,但更像「已知族的尾部函数」):凸变换把 EMA 变成软最大值

```
head:  pow_2(pow_2_5(day_durbin_watson(High)))      +1.4497(train 1.4497 / valid 3.1992),sign −1,hl 20,rho_known +0.1329
```

拆解给出一条**干净的剂量—反应**:

| 表达式 | 等价指数 | score | train | valid | distinct |
|---|---|---|---|---|---|
| `day_durbin_watson(High)` | x^1 | **−1.1711** | −1.1711 | +0.5771 | 0.9997 |
| `pow_2(day_durbin_watson(High))` | x^2 | +0.2653 | +0.2653 | +1.9566 | 0.9997 |
| `pow_2_5(day_durbin_watson(High))` | x^2.5 | +0.7240 | +0.7240 | +2.3649 | 0.9997 |
| `pow_2(pow_2_5(day_durbin_watson(High)))` | x^5 | **+1.4497** | +1.4497 | +3.1992 | 0.9997 |

四行的 sign 全是 −1、hl 全是 20、distinct 全是 0.9997、`rho_known` 全是 0.1329。DW ≥ 0,所以 `pow_2`、`pow_2_5` 在它上面是**严格单调**的:
**同一天的截面排序四行完全相同**,唯一的区别是 `steer.py:632-640` 的管线顺序 —— **先按日 EMA(hl ∈ {0,5,20}),再 z-rank**。
EMA 作用在原始数值上,所以 `EMA(x^e)^{1/e}` 是指数 e 的**幂平均**:e = 1 是算术平均,e → ∞ 是窗口内的最大值。
于是这四行其实是同一个特征的**四种时间聚合**:平均 → 软最大值。score 单调升 2.62。

**这是本轮唯一一条「处理方式」级别的机械发现**,而且它比第 1 轮 §1.5 那条(`inv` 改变 EMA 里哪几天占权重)更强:那里是副作用,这里是**主效应,值 +2.6**。
顺带一个边界条件:hl 与 sign 是按 **train** 的纯多头夏普挑的(`steer.py:636-645`),所以这条机制在 hl = 0 时必然消失(同日排序相同)—— 这给了一个可证伪的检查(见 4.2 第 6 条)。

**`day_durbin_watson(High)` 在算什么**:`dt_day.py:272` = Σ(Δx)²/Σx²,**分母不去均值**。对价格序列 P,Σ(ΔP)²/ΣP² ≈ (1/241)·Σ(ΔP/P)² = **分钟收益的均方** ≈ 日内已实现方差(每分钟口径,尺度无关)。
`High→Low`:+1.2779(train 1.2779 / valid 2.8000)—— 换字段几乎不动,所以它真的是「日内价格序列的粗糙度」,与 High 这个字段本身无关。
sign −1 = 做多「最近 20 天里最粗糙的那一天不太粗糙」的票。

**所以它是真来源还是波动率代理?我的判断:两者各算一半,必须讲清楚。**
控制里有 `cross_mean(day_std(Ret), 20)`(20 日平均的分钟收益标准差),那是**平均**波动;本 head 是同一原料的**尾部**(幂平均 5 ≈ 近月最粗糙的一天)。
线性投影(`neutral_basis` 对 z-rank 做 QR,`steer.py:403`)无法张开一个凸函数,所以残差上剩下 +1.45 是**真的**,`rho_known` 只有 +0.13。
但它的经济内容是「近月极端日内波动,规避之」—— 这正是资产定价里的 MAX 效应 / 异质波动率之谜那一族。**新的是聚合方式,不是原料。**
对 C05 的主指标(最终库的测试段夏普)来说这未必是坏事:一个稳健的已知异象用新函数形式表达出来,照样能贡献样本外夏普;只是不能说它是新信息。

**可直接检验的推论(本轮 R 就能做)**:(i) 指数再往上(x^6.25、x^10)应继续升然后饱和;(ii) 换成**显式**的窗口最大值 / 高分位
(`cross_max(day_durbin_watson(High), 20)`)应该复现甚至超过 +1.45,且 hl 会落到 0 或 5;(iii) 若 (ii) 成立,这条处理方式可以搬到任何日度统计量上(见 4.3 第 1 条)。

### 1.3 真来源(三):被 R 规则扔掉的那个近乎正交的因子

第 1 轮 R 的 16 次评估里有一条结果比所有替换都重要:

```
ts_reg_tvalue(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100)
   score +1.1434(train +1.1434 / valid +1.9503),sign −1,hl 20,coverage 0.9833,distinct 1.0000
   rho_known −0.0891,与原 head 的交易信号 rho_head **+0.0761**
```

同一个关系统计量在窗口 50 处是 **−0.1061**(train −0.0073 / valid −0.1061)。所以:

- 「幅度是噪声」第 1 轮的读法要**修正**:不是「幅度永远是噪声」,而是「**50 日的 beta 太噪,标准化救不回来;100 日的 t 值是干净的标准化,而且比同窗口的 `sigmoid(beta)` 还好一点**」
  (t@100 = +1.1434 对 `sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100))` = +1.0413)。
  解剖员第 1 轮预测「t 值版 ≥ 0.80」在 100 处对、在 50 处错;PI 预测「0.4–0.75」两处都错。
- 它的 `rho_head` 只有 **0.0761**,所以按 §2.5 的 R 规则(要求与原 head 的交易信号 ρ ≥ 0.5 才算「同一个东西」)它**不能替换**,于是**被丢掉了**。
  同样被丢掉的还有 `sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100))`(+1.0413,rho_head 0.1166)。
- **这是 R 这个机制的结构性漏洞**:R 只会「替换」,高分而正交的发现无处可去。而 PLAN §3 的最终去重会丢掉 ρ ≥ 0.7 的重复,正交的 head 才值钱。
  **这两个表达式应该作为任务种子进库,而不是作为 R 的变体被丢掉。** 库禁令挡不住它们:骨架里是 `ts_reg_tvalue` 而不是 `sigmoid(ts_regbeta(...))`,
  与任一 head 的秩相关也远低于 0.7(ρ_head 0.08 / 0.12)。给 PI 的话:**这是本轮最便宜的一笔收益,两个种子就能把两个 +1.0 以上、与 S 几乎正交的 head 收进库。**

### 1.4 代理 / 搭车:M 第 2 批的主线是名义股价水平

M2 的 7 个 head 里有 **6 个**碰 `LogFloatShares` 或 `day_quantile_q25(Open)`:

```
+1.29  cs_last_high10(signedpower(pow_2_5(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3))), day_max(Volume))
+1.09  cs_last_high10(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3), day_gini(Volume))
+1.07  cs_last_low20(cross_quantile_q25(LogFloatShares, 241), day_durbin_watson(Vwap))
+1.03  cs_last_high10(cs_bucket_zscore(day_quantile_q25(Open), sqrt(day_quantile_q25(Open))), day_gini(Volume))
+0.86  cs_last_high10(cs_last_high10(LogFloatShares, day_durbin_watson(High)), day_durbin_watson(Vwap))
+0.56  cross_quantile_q25(cs_bucket_zscore(day_quantile_q25(Open), sqrt(day_quantile_q25(Open))), 241)
```

**代数**(`alphacube/dailyfields.py:57`:`LogFloatShares = log(FloatShares)`、`LogFloatCap = log(FloatCap)`,而 `FloatCap = FloatShares × 价格`):

```
LogFloatCap = LogFloatShares + log(价格)
```

而 `long_neutral` 的控制里有 `LogFloatCap`(`idea_search.py:182`)。控制是先取 z-rank 再做 QR 投影,所以不是严格的代数恒等,但**一阶上**:
把 `LogFloatCap` 投影掉之后,`LogFloatShares` 的残差 ≈ **−log(价格)** 的残差。head 的 sign = +1 = 做多 `LogFloatShares` 高的一端 = **做多低价股**。
**这就是 A 股的名义低价股效应**,控制集里没有价格水平这一项,所以它必然反复出现。

**拆解把这一簇的内部结构照得很清楚(+1.29 那棵)**:

| 行 | 数字 | 读法 |
|---|---|---|
| 四个嵌套子树单独当因子 | **0.5557 / 0.5515 / 0.5558 / 0.5578**(valid 均 ≈ 0.777,`rho_known` 均 −0.284) | 四个数几乎相同 ⇒ `signedpower`、`pow_2_5`、`cross_decay_linear(·,3)` 对一个**慢变量**全是单调包装,整条内链就是**一个变量**:慢口径的流通股数(≈ 低价) |
| 三个 knockout | 必要性 **0.0000 / 0.0000 / 0.0023** | 三个零件是**纯死重** |
| 敲掉 `cross_quantile_q25(·, 241)` | 必要性 +0.1518 | 只有这一层(241 日的 q25,等于把慢变量再滞后/平滑)有一点作用 |
| 筛子 `cs_last_high10(·, day_max(Volume))` | 0.5578 → **1.2940**(+0.736) | **分数的 2/3 来自这个「排除」动作,不来自被排除的那个变量** |
| `day_max(Volume) → day_max(Amt)` | +1.2940 → **−0.1713** | 筛子只在**股数**口径下有效 |
| `cross_decay_linear@3→2 / →6` | +1.2987 / +1.2767 | 窗口无所谓(再次印证是单调包装) |

`day_max(Volume)` = 当日最大的单分钟**股数**成交量。给定市值,股数 ∝ 1/价格,所以它本身也重度携带低价信息;
把它的最高 10%(整块并列)压到书底(`ops_ext.py:339` 的 `_lexi`:那些票取 `rank(y) − 1`),等于**在低价股里再剔掉最便宜、换手最猛的那一截尾巴**。
换成 `day_max(Amt)`(元口径、与价格无关)就变成剔大成交额的票,直接崩到 −0.17。
**所以这一簇的经济内容是:做多低价股,但排除最极端的那一截 —— 一个关于股价水平的非单调(驼峰形)押注。**

`cs_bucket_zscore(day_quantile_q25(Open), sqrt(day_quantile_q25(Open)))` 更露骨:`sqrt` 是单调的,所以 `x` 的十分位 = `y` 的十分位(`ops_ext.py:458` 的 `_buckets` 用 `_pct_rank(x)`),
这整个表达式就是**「股价在自己所在的股价十分位里的 z 分数」** —— 把全局价格水平减掉、只留桶内位置的锯齿函数。又是价格水平的一种非单调再表达。

**结论与第 1 轮的差别(要诚实记下)**:第 1 轮我把 `inv(LogFloatShares)` 一族判为「零充分性证据的搭车现象、不要投资」。
第 2 轮它有了充分性证据(**+0.5578 单独过线**),所以「不是真的」这句话要收回:**在 train / valid 上它是一份真实的残差 alpha**。
但「不值得深挖」这个结论不变,而且理由更硬了:它是**已知的廉价异象**(名义低价效应),不是新信息;
PLAN §3 的最终去重会把 ρ ≥ 0.7 的重复丢掉,所以库里已经有 6 个它的写法之后,再加一个的边际价值接近 0。
另外第 1 轮指出的「三个 `LogFloatShares` 共性卡的含它均值 0.4834 / 0.4848 / 0.4827 几乎相同」在本轮**一字未变**(n_with 还是 12 / 6 / 4),
即这 4–12 个候选全部来自 M1 的同一条谱系,仍然是搭车,**不是**独立证据。

**真正新的那一点在这一簇里,但不是「被筛的那个变量」,而是「筛子」本身**:`cs_last_*` 是「y,但永远不碰 x 标出来的那些票」,
和把 x 线性加进去是完全不同的处理方式。三个不同的 y(慢流通股数、桶内股价 z 分数、裸 `LogFloatShares`)配三个不同的 x
(`day_max(Volume)`、`day_gini(Volume)`、`day_durbin_watson(Vwap)`)都涨了 +0.5 ~ +0.74。这一点值得花几次 R 弄清楚(见 4.2 第 9–10 条),**但不值得花一个 E 位**。

### 1.5 对第 1 轮两个判断的修正

1. **「价格字段必须是 Vwap」要打折。** 第 1 轮在窗口 50 上看到 `Vwap→Close` 四棵全崩(+0.834→+0.699、+0.832→**−1.027**、+1.144→+0.499、+0.730→+0.324),
   据此判定 S 讲的是「有成交的钉价」而不是「没成交的呆滞」。本轮在窗口 **100** 上重做:
   `inv(pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Close), day_durbin_watson(Volume), 100))))))))` = **+1.0081**(train 1.0081 / valid 2.6529),
   对 Vwap 版的 +1.1555 只低 0.147,coverage 0.9981、distinct 0.9054。
   **窗口拉长之后 Close 版几乎一样好。** 所以「必须是分钟 Vwap」这个判断只在短窗口成立;更可能的读法是:短窗口下 Vwap 版的信噪比更高,
   而信息本身是更一般的「价格序列的粘滞」,Close 也能量到。第 1 轮由此推出的机制故事(封板 vs 呆滞)**证据被削弱了**,不要再当已证实的前提用。
2. **`day_durbin_watson(Volume)` 的内容不是「自相关」。** 第 1 轮 R 把它换成一阶自相关和 Gini:
   `day_autocorr_n1` → **−1.8325**(train −0.4413 / valid −1.8325);`day_gini` → **−0.2745**(train +0.7984 / valid −0.2745);
   `day_flat_run_max(Vwap) → day_flat_ratio(Vwap)` → +0.5568(对 +0.712,只低 0.155)。
   DW 的分母是 **Σv²(未去均值)**,而 `day_autocorr_n1` 是去均值并标准化的,所以 DW 携带的是「相对自身**水平**的粗糙度」,
   既有序列依赖也有离散度,两者缺一不可。**「换一个尺度无关的日内粗糙度都行」这个猜想被否了:只有 DW 这个具体比值行。**

---

## 2. 烂部件(必要性 ≤ 0,或换掉反而更好)—— R 的料

| head | 部件 | 证据 | 判语 |
|---|---|---|---|
| +1.1555 `inv(pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100))))))))` | `ts_regbeta` 窗口 100 | 100→200 = **+1.3933**(train 1.3933 / valid 2.4174),gain **+0.2378**,`rho_head` 0.7525,`rho_known` −0.2015 | **唯一的合规 R 候选,已评过、不花预算,直接替换**。窗口序列 50 / 100 / 200 = 0.8315 / 1.1555 / 1.3933,**单调** |
| 同上 | 中段 `inv(sigmoid(pow_1_5(inv(sigmoid(·)))))` | 敲掉 → +1.2087,必要性 **−0.0532** | 有害但 gain 差 0.047 够不上 +0.1 线。**和窗口 200 叠起来才有机会** |
| 同上 | 最外层 `inv(pow_1_5(·))` | 子树单独 +1.2074(gain +0.0519)、knockout 必要性 +0.0069 | 纯节点浪费 |
| 同上 | `Volume→Amt` / `Vwap→Close` | +1.0882 / +1.0081 | 都更差,不替换(但 Close 版见 1.5) |
| +1.4497 `pow_2(pow_2_5(day_durbin_watson(High)))` | 无 | 唯一的 knockout 必要性 +1.1844;`High→Low` −0.172 | **没有烂部件**。但指数的剂量—反应(1.2 节)说明「还没推到头」,这是 R 的机会而不是去部件 |
| +1.2940 `cs_last_high10(signedpower(pow_2_5(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3))), day_max(Volume))` | `signedpower`、`pow_2_5`、`cross_decay_linear(·,3)` | 必要性 **0.0000 / 0.0000 / 0.0023** | **三个零件同时是死重**。单个敲掉 gain = 0,够不上替换线;**三个一起敲掉从没试过**,值 1 次评估(得到一个短 3 个节点的干净 head,也是一个干净的核心候选) |
| +1.6680 `cross_mean(day_mean(in_logchg(Volume, 60)), 20)` | 无 | 两个窗口都更差,`Volume→Amt` −0.025 | **没有烂部件**。R 要花在没试过的轴上(核内分钟窗口、平滑核形状) |
| +0.8324 `sigmoid(ts_regbeta(day_flat_run_max(Vwap), sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 50))` | 整个外层 `ts_regbeta(day_flat_run_max(Vwap), ·, 50)` | 第 1 轮 R 试过:剥成 `sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100))` = +1.0413(gain +0.209)但 `rho_head` **0.1166 < 0.5**,**被 ρ 门槛挡住、没能替换** | 死重确认,但「剥干净」产生的是**另一个因子**,不是同一个因子的更好版本。这个 head 本轮仍是库里最弱的 S 包装(train 1.086 / valid 0.832,是 18 个 head 里唯一 valid < train 的) |
| +0.5370 `day_mean(neg(in_delta(Volume, 60)))` | 整个水平口径 | 对数口径的同族 head 是 +1.6680;份额口径 −0.0666;Amt 水平口径 −1.8761(rho_known −0.5243) | 这个 head 现在是**同一份信息的最差写法**。但 `cross_mean(day_mean(in_logchg(Volume,60)),20)` 与它的 `rho_head` 未知;若 ρ ≥ 0.5,一次评估就能把它替换掉(gain +1.13),**本轮性价比最高的一次 R** |

---

## 3. 之前的任务

### 3.1 E(`c05s802Br1a_Ea`,核心 S@50):92 次评分,0 个过线,0 个 head

采样计数 `{'c05_no_core': 3012, 'c05_periphery_seen': 11, 'mutation_refused': 6}`。最好的五个:

| score | train | valid | 表达式 |
|---|---|---|---|
| −0.1432 | −0.1432 | **+1.6350** | `mul(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), day_centroid(Volume))` |
| −0.1506 | −0.1506 | +0.4889 | 上面那个再套一层 regbeta + `day_distinct_ratio(Volume)` |
| −0.1652 | −0.1652 | **+1.1937** | `mul(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), day_distinct_ratio(Volume))` |
| −0.8077 | +0.1278 | −0.8077 | `ts_corr(mul(sigmoid(ts_regbeta(...)), day_at_max_ratio(Vwap)), day_flat_run_max(Close), 60)` |
| −0.8556 | −0.4723 | −0.8556 | 上面那个的二次嵌套 |

**为什么 0 个过线 —— 三条原因,按重要性排**:

1. **家族控制太重。** `c05_round.py:224-226` 把库里含该核心的 head 按 score 取前 6 个加进控制;当时库里 6 个 head 有 **5 个**含 S。
   奖励等于先把 S 的信息**全部**减掉,再要求候选「必须原样含 S」。这是一个几乎空的集合:要同时和 S 绑死、又和 S 正交。
   证据就在前三行:**train 全是 −0.14 ~ −0.17,而 valid 是 +1.64 / +0.49 / +1.19**。train 上 S 家族把残差吃干净了,valid 上没吃干净 ——
   score = min(train, valid),于是全军覆没。
2. **约束把有效搜索压到很小。** `c05_no_core` 拒绝了 **3012** 次,才凑出 92 次评分;`--graft-fill 32` 只管初代。
   实际发生的是:初代 = 我写的 14 个种子 + 18 个机械嫁接,之后的变异/交叉绝大多数被「必须含核心」拒掉。
   **E 的产出 ≈ 手写种子的质量**:最好的五个全是种子 13(`mul(S, day_centroid(Volume))`)、种子 8/9(`day_at_max_ratio`)、种子 11(`ts_corr(S, day_flat_run_max(Close), 60)`)的直系后代,
   GP 本身几乎没有贡献新东西。
3. **我选的那两条外围轴里,「交互」比「状态动力学」好。** 前三名全是 `mul(S, 另一个日内形状)`;状态动力学那一组(`ts_rank` / `cross_zscore` / `ts_stddev` / `cross_flat_ratio` / `ts_argmin` / 短长均值差)
   一个都没进前五。给第 2 轮的教训:**在家族控制下,「和 S 同轴的时间序列变形」注定被减掉,只有「带第二个叶子的交互」还有残差。**

**不可对账的一条**:第 1 轮预测 `cs_bucket_rank(S, day_last(Close))` 会被库的秩禁令拒掉(用来检验「S 是不是相对最小价位的代理」)。
证据文件里只有 `c05_*` 三个计数器,没有秩禁令的拒绝记录,前五名里也没有它。**这个探针的结果读不出来,那个问题仍然没有答案。**
而它现在更要紧了:1.4 节证明**股价水平本身在这个奖励下就有 +0.56 的残差 alpha**,所以「S 有多少是股价水平的代理」必须另找办法回答(见 4.2 第 11 条)。

### 3.2 N(`c05s802Br1b_Nb`,日内成交量时间分布):81 次评分,8 个过线,**5 个 head**

5 个 head 分成三条写法,方向全部一致(`sign` 都是 −1 = 做多早盘重 / 尾盘轻):

| score | 表达式 | 读法 |
|---|---|---|
| +1.6680 | `cross_mean(day_mean(in_logchg(Volume, 60)), 20)` | 尾/首段对数成交量之比,20 日平均 |
| +0.7233 | `cross_mean(div(div(day_last(Amt), day_sum(Volume)), day_sum(High)), 20)` | **价格约掉之后的收盘那一分钟成交占比**:`Amt/Volume` 是元/股 ≈ 价格,再除以 `day_sum(High)` ≈ 241×价格,余下 ≈ 收盘分钟的量占比 / 241 |
| +0.6578 | `cross_mean(day_mean(in_scale_rolling(Volume, 60)), 20)` | `in_scale_rolling(x,60) = x[t]/Σ_{t−59..t}x`(`common.py:686`),即每分钟占前一小时的份额 ⇒ 日内成交量的**集中度 / 爬升度**,20 日平均 |
| +0.5245 | `cross_mean(cross_mean(div(div(day_last(Amt), day_sum(Volume)), day_sum(Volume)), 3), 20)` | 同上但分母多了一次 `day_sum(Volume)`,量纲不干净,混进规模 |
| +0.5084 | `cross_mean(cross_mean(div(day_last(Amt), day_sum(Amt)), 20), 20)` | **收盘那一分钟的成交额占比**,双重平滑 |

**N 完胜 E:同样 96 次预算,N 给了 5 个 head(含全库第一),E 给了 0 个。** 而且三条写法彼此独立地说同一件事(早盘重 / 尾盘轻),互相印证。
PI 第 1 轮「N 产出 ≥1 个 head 的概率约 60%、预期 1–3 个」偏保守(实际 5 个);但「最可能过线的是**归一化的首末段份额差**或 `day_centroid` 的 20 日均值」这一条**错了**:
份额差口径是 −0.0666,`day_centroid` 一个 head 都没进 —— 过线的是**对数口径**(种子 `day_mean(in_logchg(Volume, 60))`)。族对了,归一化方式猜错了。
「只用 15:00 那一分钟占比的单独写法 score < 0.5」也只对了一半:双重平滑的 `cross_mean(cross_mean(div(day_last(Amt), day_sum(Amt)), 20), 20)` = **+0.5084**,过线了。
hl 的预测(20)也错:winner 选了 hl 5、双重平滑那两个选了 hl 0 —— 因为 `cross_mean` 已经把平滑做掉了。
「N 的 heads 与 S head 的交易信号 |ρ| < 0.3」**无法对账**:定位输出里没有跨任务的 ρ 表。

**两条必须写下的保留**:
- `day_last(·)` 取的是当日**最后一个非 NaN** 分钟(`dt_day.py:134`),而上交所 2018-08-20 才有收盘集合竞价。
  train(2018-01 起)的前 8 个月里,沪市票的 `day_last` 是最后一根连续竞价分钟,深市票口径不同 ⇒ train 前段有一个**按交易所分叉的结构性断点**。
  两个收盘占比 head 的 score 是 min(train, valid),所以这个断点已经在分母里,但「它在 2018 上半年部分地当了一个交易所哑变量」这个风险实际存在。PI 第 1 轮就预判过这件事,**是对的**。
- 双重 `cross_mean` 的两个 head(+0.5245、+0.5084)hl 都选到了 **0**:平滑已经做够了,EMA 不再帮忙。它们和单重平滑版本的差别很可能是死重,值 1 次 R(见 4.2 第 15 条)。

### 3.3 R(16 次直接评估,3 次替换生效)—— 预测对账

| # | 变体 | 第 1 轮预测 | 实际 | 对? |
|---|---|---|---|---|
| 1 | A1 窗口 100 + decay 80 | 1.25–1.40,65% 替换 | **+1.0883**(valid 2.6155),rho_head 0.8788,**未替换** | **错**。两个「已证实的方向」叠起来反而低于原 head(+1.1438) |
| 2 | A1 窗口 100、decay 40 | 1.15–1.30 | +1.1345(hl 0),rho_head 0.4669 | 在区间内,但未替换 |
| 3 | A1 beta→t 值(窗口 50) | 0.7–1.1 | **−0.2730**(train 0.4365) | **大错** |
| 4 | A2 窗口 100 | 复现 1.1555,确定替换 | **+1.1555**,替换 ✓ | **对**(精确复现) |
| 5 / 9 | A3、A5 → `sigmoid(ts_regbeta(…, 100))` | 0.95–1.10,55% / 70% 替换 | **+1.0413**,gain +0.209,但 `rho_head` **0.1166**,**被 ρ 门槛挡住** | 数值对,替换判断错 —— **没想到「剥掉死重」会变成另一个因子** |
| 6 | 裸 t 值 50 | 解剖员 ≥0.80;PI 0.4–0.75 | **−0.1061** | 两人都**错** |
| 7 | 裸 t 值 100 | 同上 | **+1.1434**(valid 1.9503),rho_head 0.0761 | 解剖员**对**、PI 错;而且这是本轮最有价值的一条(1.3 节) |
| 8 | A4 去内层 inv | 复现 0.9608,确定替换 | **+0.9608**,替换 ✓ | **对** |
| 10 | DW→`day_autocorr_n1` | 0.2–0.6 | **−1.8325** | **大错**(1.5 节第 2 条) |
| 11 | DW→`day_gini` | 0.0–0.6 | −0.2745(train +0.7984) | train 在区间内,valid 崩 |
| 12 | `flat_run_max→flat_ratio` | 0.3–0.8 | **+0.5568** | **对** |
| 13 | A6 除以当日平均分钟量 | 0.4–0.8,rho_head 0.4–0.7 | **−0.0666**,rho_head 0.4403 | 分数**大错**(份额归一化杀死了它),rho_head 对 |
| 14 | A6 换 Amt | 0.45–0.65 | **−1.8761**,rho_known −0.5243 | **大错** |
| 15 / 16 | A6 窗口 30 / 120 | 0.4–0.7 / 0.3–0.6 | +0.3628 / **+0.5579** | 30 略低于区间,120 高于区间 |

**替换生效 3 个**:A2 → 窗口 100(+1.1555)、A4 → 去内层 inv(+0.9608)、A5 → 窗口 100(+0.8869)。
第 1 轮预测 #5「R 之后 S 一族仍占 4–5 个 head」:**对** —— 现在 S@50 家族 3 个(+1.1438 / +0.9608 / +0.8324)+ S@100 家族 2 个(+1.1555 / +0.8869)= 5 个。
第 1 轮预测 #1(两条代数对账,要求分数**精确相等**)**没有执行**:PI 最终的 16 个 R 变体里没有这两行。那个用来校验「我们对管线的理解」的检查点**还空着**。

**对账的总账**:16 条里数值方向判对的大约 6 条,判错的 6 条,其余部分对。**系统性偏差有两个:
(i) 我们高估了「把两个已证实的方向叠加」的收益(#1);(ii) 我们以为统计量之间可以互换(#3、#6、#10、#11、#13、#14 全是这一类,无一例外地错得很远)。**
本轮据此改原则:**一次只动一个零件;「换一个同类统计量应该差不多」这种猜想一律先花 1 次评估,不要写进任务假设。**

### 3.4 第 1 轮「留给第 2 轮的条件计划」现在怎么样

- 「N 有 head → 第 2 轮给最好的那个 N head 的最短充分子树一个 E 位」:**条件成立**,最短充分子树 = `day_mean(in_logchg(Volume, 60))`(+0.5473)。
  注意它**过不了机械核心卡的门槛**(规则要求自身 score ≥ 0.5 **且 ≥ 所在 head 的 60%**;0.5473 < 0.6 × 1.6680 = 1.0008),所以**它不在卡上、B0 用不了它**。
  按 §2.5 的字面,B 只要求核心是「快照里某个 head 或存档候选的子树、能单独求值」—— 它完全合法。**这是 B 相对 B0 本轮最明确的一处优势。**
- 「E(S) 没有 head → S 的第 2 个 E 位先不用」:条件成立,**不要再给 S 一个 E 位**(而且 1.3 节说明 S 这条线剩下的价值是把 t@100 收进库,那是种子的事,不是 E 的事)。
- 「若裸 t 值 ≥ 0.8,考虑把标准化的关系统计量推广到别的日内形状对」:t@100 = +1.1434,**条件成立**(见 4.3 第 2 条)。
- 「第 2 批 M 若出现新的高分结构,优先把 E 给它」:M2 给了两条,一条是机械发现(1.2 节,更适合走 N),一条是股价水平代理(1.4 节,不值得 E)。

---

## 4. 本轮候选

### 4.1 值得深挖的核心(按推荐度,≤3 个)

#### 核心 A(强烈推荐)

```
day_mean(in_logchg(Volume, 60))
```

- **凭据**:自身 +0.5473(train 0.5473 / valid 0.7595),coverage 0.9993、distinct 1.0000、`rho_known` −0.1275;
  它所在的 head 是全库第一(+1.6680 / valid 2.2596);窗口 10 / 20 / 40 = 1.4391 / 1.6680 / 1.4516(平顶);`Volume→Amt` 1.6429(字段不敏感);
  对当日成交量的乘性缩放**严格不变** ⇒ 不是流动性 / 换手 / 规模 / 价格的代理(1.1 节)。
- **家族控制只有 1 个 head**:库里 18 个 head 中,原样含这个子树的只有 `cross_mean(day_mean(in_logchg(Volume, 60)), 20)`
  (`cross_mean(day_mean(in_logchg(Amt, 60)), 20)` 换了字段、核心 key 不同;双重平滑那个没进 heads)。
  按 `c05_round.py:224` 取前 ≤6 个,家族 = 1。**这直接拆掉了第 1 轮 E 失败的首要原因(3.1 节第 1 条:当时家族 5 个)。**
- **已经见过的外围写法**(外围 = 核心之外的**算子名集合**,`idea_search.py:312`;`seen` 由全部 281 个存档算出,而我只能看到 heads 与各任务前五名,**下面是下界**):

  | 来源 | 外围算子名集合 |
  |---|---|
  | 永久禁(核心自身) | ∅ |
  | head +1.6680 | {`cross_mean`} |
  | N 任务前五的 `cross_mean(cross_mean(·,20),20)` | {`cross_mean`}(同一个集合) |

  **所以只有「加平滑」这一个集合被禁掉了,整个外围空间几乎全开。** 但禁的是**集合**,{`cross_mean`,`cross_zscore`} 这种「再加一个名字」仍然合法 ——
  而 1.1 节已经说明再延长平滑会把 `rho_known` 推向 0.5 的不合格线,所以**不要再在平滑上花评估**。为稳妥,手写种子最好一次带进 **≥2 个**新算子名,免得撞上我看不到的 SEEN 集合。
- **没试过、而且是另一条轴的外围**(给 PI 写种子用;下笔前请用 `partura.ac_plugin.partura_operator_names()` 对词表):
  1. **条件化 / 分组**(文献和 C04 唯一留下的贡献都指这里):`cs_bucket_rank` / `cs_bucket_zscore` / `cs_bucket_demean`,桶用 `LimitWidth`、`BoardCode`、`ListAge`、`LogFloatShares`;
     「小盘 / 创业板 / 新股里早盘重更值钱吗」是真的新信息。注意库禁令按**原始日度秩** |ρ| ≥ 0.7 拒绝,桶内秩会保留大部分截面排序,所以优先用 `cs_bucket_zscore`(改量纲)而不是 `cs_bucket_rank`。
  2. **排除式筛子**(M2 本轮唯一的新处理方式,1.4 节):`cs_last_high10(核心的平滑版, day_gini(Volume))`、`cs_last_low10(·, …)` 等 ——
     把「永远不碰某一截票」这个动作搬到一个**不是股价代理**的 y 上。这是把 M2 的方法论借到 N 的成果上,是本轮 B 组最像「深挖」的一步。
  3. **形状的不稳定度而不是形状的水平**:`cross_stddev(day_mean(in_logchg(Volume, 60)), 20)`、`cross_zscore(·, 60)` ——
     「这只票的日内成交时间分布有多不稳 / 今天相对自己的历史有多反常」是和「它平均偏早还是偏晚」不同的一份信息。
  4. **与第二个日内形状做交互**(E 第 1 轮前三名全是这一类,是唯一有数据支持的一条):`mul` / `div` / `day_corr` 配 `day_gini(Volume)`、`day_centroid(Volume)`、
     `day_distinct_ratio(Volume)`、`day_at_max_ratio(Vwap)`、`day_zero_ratio(Ret)`。
     **注意**:共性表上 `day_centroid(Volume)` = −0.805、`day_at_max_ratio(Vwap)` = −0.806 是我自己第 1 轮 E 种子造成的污染(1.0 节),**不是**这些零件不好的证据。
  5. **与 1.2 节的凸聚合叠起来**:核心是**有符号**的对数比,所以 `pow_2` / `pow_2_5` 在它上面不是单调变换(是「偶」变换,把早盘重和尾盘重都算成极端),
     而 `signedpower` / `pow_3` 才是保序的凸变换 —— 两种都值得各放一个种子,它们问的是不同的问题。
- **风险**:核心单独只有 +0.55,离发现线不远;E 的奖励再减掉那 1 个家族 head 之后,残差空间有多大是未知的。缓解:家族只有 1 个,而且上面第 1、2、4 条都带第二个叶子。

#### 核心 B(备选,方法论价值最高)

```
day_durbin_watson(High)        （或 pow_2_5(day_durbin_watson(High)) —— 但见下面的取舍）
```

- **凭据**:见 1.2 节的剂量—反应表(指数 1 / 2 / 2.5 / 5 → −1.17 / +0.27 / +0.72 / +1.45),`High→Low` +1.2779(字段不敏感),`rho_known` +0.1329。
- **家族控制 = 2 个 head**(`pow_2(pow_2_5(day_durbin_watson(High)))` +1.4497;`cs_last_high10(cs_last_high10(LogFloatShares, day_durbin_watson(High)), day_durbin_watson(Vwap))` +0.8564)。
- **已经见过的外围写法**(下界):

  | 来源 | 外围算子名集合 |
  |---|---|
  | 永久禁(核心自身) | ∅ |
  | head +1.4497 | {`pow_2`, `pow_2_5`} |
  | 存档候选 `pow_2_5(day_durbin_watson(High))`(共性 n=11) | {`pow_2_5`} |
  | head +0.8564 | {`cs_last_high10`, `day_durbin_watson`} |
  | 存档候选 `cross_corr(cross_regalpha(LimitWidth, day_sum(Open), 241), pow_2_5(day_durbin_watson(High)), 30)`(共性 n=5) | {`cross_corr`, `cross_regalpha`, `day_sum`, `pow_2_5`} |

  纯粹的幂叠加基本已被 {`pow_2_5`}、{`pow_2`,`pow_2_5`} 两个集合封住 —— **这正好逼着 GP 换真东西**。
  (顺带:M2 自己探过 `LimitWidth` × DW(High) 的组合,共性 +0.4507 但 p 0.42、没成 head —— 第 1 轮想做的涨跌停带宽机制检验,M 已经试过一次、没结果,这是一条弱的反面证据。)
- **取舍**:核心取裸 `day_durbin_watson(High)` 的好处是把「怎么聚合」交回给 GP;坏处是它单独只有 −1.17,家族控制减掉的是 x^5 版本,
  GP 很可能把 96 次评估花在重新发明幂次上(而幂次的集合又被禁了,于是容易空转)。
  **我的判断:这条发现的正确载体是 N 而不是 E** —— E 的定义是「固定核心、变外围」,而这里我们想固定的是**处理方式**(凸聚合 / 软最大值)、变的是**原料**。
  C05 的任务词表里没有「固定处理方式」这种位,所以它只能走 N(见 4.3 第 1 条)。核心 B 只在 PI 决定本轮要两个 E 位时才用。

#### 核心 C(列出以供对照,**不推荐**)

```
cross_quantile_q25(LogFloatShares, 241)
```

- 自身 +0.5578、家族 3 个 head、共性卡 #13(+1.2084,p 0.000,n=32)。B0 很可能会用到它(它的卡序更靠后,但卡 #1–#4 是 S@100 的单调包装)。
- **不推荐的理由**(1.4 节):它一阶上就是**名义股价水平的反面**,是已知的廉价异象;库里已经有 6 个它的写法;PLAN §3 的去重会把 ρ ≥ 0.7 的丢掉,
  所以再长出来的任何东西边际价值都接近 0。更糟的是它的三个内层零件必要性全是 0,E 的机械嫁接会在这些死重上浪费节点预算。
- 已见外围(下界):{`cs_last_high10`,`signedpower`,`pow_2_5`,`cross_decay_linear`,`day_max`}、{`cs_last_high10`,`cross_decay_linear`,`day_gini`}、
  {`cs_last_low20`,`day_durbin_watson`}、{`cross_decay_linear`}、{`pow_2_5`,`cross_decay_linear`}、{`signedpower`,`pow_2_5`,`cross_decay_linear`}、{`ts_argmin`}。

### 4.2 R 目标(PI 从里面挑 ≤16;第 1 条已评过、不花预算)

**已评过、合规,直接替换:**

1. head +1.1555 → `inv(pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 200))))))))`
   gain **+0.2378**,`rho_head` 0.7525,`rho_known` −0.2015。

**新提议(每条都接一条已证实的方向,括号里是依据):**

2. **把那个 +1.67 的 head 用来替换它自己的水平口径祖宗**(2 节最后一行):对 head `day_mean(neg(in_delta(Volume, 60)))` 直接评
   `cross_mean(day_mean(in_logchg(Volume, 60)), 20)` —— gain +1.13,只要 `rho_head` ≥ 0.5 就替换。
   **本轮性价比最高的一次**:一次评估把库里最弱的那个写法换成最强的。(若 ρ < 0.5,说明对数口径和水平口径是两份信息,那本身就是重要结论。)
3. **窗口单调性再推一格**(50 / 100 / 200 = 0.8315 / 1.1555 / 1.3933):
   `inv(pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 400))))))))`。
   第 1 轮文献(L2 第 3 条,HKS 2010 的「约 40 个交易日记忆边界」)预测 200 之后不该继续受益,而 200 已经受益了 —— 这一发同时检验结构和那条文献推断。
4. **把窗口 200 和已证实的死重剥离叠起来**(中段 knockout 必要性 −0.0532):
   `inv(pow_1_5(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 200)))))))`。
   注意第 1 轮 #1 的教训(叠加两个方向反而变差),所以这是**和第 3 条并列的两个单变量**,不是替代。
5. **凸聚合的剂量—反应**(1.2 节):`pow_2_5(pow_2_5(day_durbin_watson(High)))`(x^6.25)、`pow_2(pow_2(pow_2_5(day_durbin_watson(High))))`(x^10)。
   预期继续升然后饱和;若在 x^6.25 就掉头,说明 x^5 附近最优,软最大值的读法仍成立但要加一句「不要推到硬最大值」。
6. **凸聚合的显式版本**(同上,决定性的一发):`cross_max(day_durbin_watson(High), 20)`,以及 `cross_mean(pow_2(pow_2_5(day_durbin_watson(High))), 20)`。
   若前者 ≈ 或 > +1.4497 且 hl 落到 0 / 5,**1.2 节的机制就被证实**,而且库里会多一个可读的 head(「近月最粗糙的那一天」)。
7. **粗糙度的字段一般性**:`pow_2(pow_2_5(day_durbin_watson(Vwap)))`、`pow_2(pow_2_5(day_durbin_watson(Close)))`。
   (`day_durbin_watson(Vwap)` 共性 +0.7350、p 0.014、n=12,且进了另一个 head;`High↔Low` 已知基本等价。)
8. **一次敲掉三个死重**(2 节,必要性 0.0000 / 0.0000 / 0.0023):`cs_last_high10(cross_quantile_q25(LogFloatShares, 241), day_max(Volume))`。
   预期 ≈ +1.29、不足 +0.1 不替换,但它把 head 缩短 3 个节点、并验证「整条内链是一个变量」的读法。
9. **筛子的配额剂量—反应**(筛子贡献 +0.736):把 +1.2940 那棵的 `cs_last_high10` 换成 `cs_last_high05` 和 `cs_last_high20`。
   5% 若 ≥ +1.39 就替换;三点连起来还能告诉我们「要排除的那一截有多宽」。
10. **筛子是不是通用的**(y 固定、x 轮换):`cs_last_high10(cross_quantile_q25(LogFloatShares, 241), day_gini(Volume))`、
    `cs_last_high10(cross_quantile_q25(LogFloatShares, 241), day_durbin_watson(Vwap))`。若任意 x 都能把 y 从 +0.56 抬到 +1.0 以上,
    筛子携带的是**自己的** alpha(那就该单独做因子);若只有特定配对有效,它是「切掉 y 的毒尾巴」。这一条决定 4.1 核心 A 第 2 条外围值不值得写种子。
11. **「S 是不是股价水平的代理」的正面检验**(3.1 节那个读不出来的探针 + 1.4 节的新证据):
    `cs_bucket_zscore(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100)), day_quantile_q25(Open))`
    —— 在**股价十分位内**重算 S 的位置。若分数与 S@100 相当,S 不是股价水平的代理;若大幅下降,第 1 轮的封板故事要再打一次折。
    (这是 R 里的「替换部件」,即使不替换也买到一个明确答案。)
12. **核心 A 的流动性旁路检验**(1.1 节那条细通道):
    `cs_bucket_zscore(cross_mean(day_mean(in_logchg(Volume, 60)), 20), cross_mean(day_sum(Amt), 30))`
    —— 在流动性十分位内重算。若基本不变,「不是流动性代理」从代数论证升级为实测。
13. **核心 A 的分钟窗口在平滑之后的最优值**(第 1 轮只在未平滑的水平口径上试过 30 / 60 / 120):
    `cross_mean(day_mean(in_logchg(Volume, 30)), 20)`、`cross_mean(day_mean(in_logchg(Volume, 120)), 20)`。
14. **核心 A 的平滑核形状**(窗口 10 / 20 / 40 已知是平顶,核形状没试过):`cross_decay_linear(day_mean(in_logchg(Volume, 60)), 20)`、
    `cross_med(day_mean(in_logchg(Volume, 60)), 20)`(对异常日的稳健性)。
15. **收盘占比族的死重**(3.2 节:双重 `cross_mean` 的两个 head 的 hl 都选到 0):`cross_mean(div(day_last(Amt), day_sum(Amt)), 20)`
    —— 单重平滑版本,对 head +0.5084。
16. **第 1 轮没做的代数对账,补 1 次**(第 1 轮预测 #1 至今空着):`day_mean(in_delta(Volume, 60))` 应与 head `day_mean(neg(in_delta(Volume, 60)))` 的 **+0.5370 精确相等**
    (`day_mean` 线性 ⇒ `day_mean(neg(x)) ≡ −day_mean(x)`,而奖励对 sign ±1 扫描,`steer.py:638`)。不等就说明我们对管线的理解有错,
    后面所有「单调包装」和「凸聚合」的论断都要重算。**这一次评估是全轮的保险丝,建议务必保留。**

### 4.3 N 的灵感(按手上的证据排序,PI 定)

1. **「凸聚合 / 软最大值」当成一种通用处理方式,系统地做一遍(最硬的一条,来自 1.2 节)。**
   一句话假设:*这类日内微观结构统计量的横截面信息在它近一个月的**极值**里,不在均值里;而控制集里只有均值口径的波动与流动性,所以尾部聚合必然留下残差。*
   做法:对一批尺度无关的日度形状统计量(`day_durbin_watson` 于 High / Low / Vwap / Close / Volume、`day_gini(Volume)`、`day_distinct_ratio(Volume)`、
   `day_at_max_ratio(Vwap)`、`day_zero_ratio(Ret)`、核心 A)分别取 `cross_max(·, 20)`、`cross_quantile_q75 / q90(·, 20)`、保序的凸变换(`signedpower` / `pow_3`)、
   以及「最近 20 天里超过自身 60 日高分位的天数占比」。这是**一组而不是一个**,正合 N 位的用法。
   注意库禁令会拒掉与 `pow_2(pow_2_5(day_durbin_watson(High)))` 秩相关 ≥ 0.7 的东西,所以种子要铺开到**别的原料**上,不要全押 DW(High)。
2. **「标准化的关系统计量 + 长窗口」把 1.3 节那两个被丢掉的因子收进库(最便宜的一条)。**
   直接把 `ts_reg_tvalue(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100)`(+1.1434,ρ_head 0.0761)和
   `sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100))`(+1.0413,ρ_head 0.1166)写进种子;
   再把这条处理方式推广到**别的日内形状对**(把 `day_flat_run_max(Vwap)` 换成 `day_gini(Volume)`、`day_distinct_ratio(Volume)`、`day_zero_ratio(Ret)`,
   把 `day_durbin_watson(Volume)` 换成 `day_durbin_watson(High)`、`day_centroid(Volume)`),窗口一律取 100 / 200(50 已证明太短:t@50 = −0.1061)。
   骨架不同、秩相关远低于 0.7,**进库概率很高**。
3. **日内成交量时间分布的「条件化」与「不稳定度」(把 N 第 1 轮的胜果往前推一步)。**
   第 1 轮 N 回答了「哪种归一化对」(对数),没回答「在什么票上更强」「它的不稳定度本身是否被定价」。
   种子:按 `LimitWidth` / `BoardCode` / `ListAge` / 流动性分桶后的桶内 z 分数;`cross_stddev(·, 20)` 与 `cross_zscore(·, 60)`;
   把一天切成「早盘→午盘」和「午盘→尾盘」两段分别算(第 1 轮 L4 第 1 条,Admati–Pfleiderer 的分时段不对称);
   以及收盘占比族的干净写法 `div(day_last(Amt), day_sum(Amt))` 配**按交易所 / 板块分组**(处理 3.2 节那个 2018-08-20 的断点)。
   若 PI 选了核心 A 的 E 位,这一条的 1、2 两项要让给 E,N 只留分时段切分与断点处理,避免两个位撞车。
4. **排除式筛子当成通用处理方式(来自 1.4 节,等 4.2 第 10 条的结果再定)。**
   `cs_last_*` / `cs_first_*` 这一族把「永远不碰某一截票」写成了表达式。M2 用它把一个 +0.56 的代理抬到 +1.29。
   若 4.2 第 10 条显示筛子是通用的,就把它作用在**非股价代理**的 y 上(核心 A 的平滑版、DW(High) 的凸聚合版),x 用日内形状统计量。
   这是本轮唯一一条「从 M 的产出里学到处理方式、搬到自己的产出上」的路径,正是 C05 设计里 B 组应该干的事。

---

## 5. 文献题目(给文献员,只能用 2023-08-08 之前发表的;接着第 1 轮的 L1–L4,不重复)

**L5(对准核心 B / N 灵感 1:把日度统计量聚合成月度信号时,均值还是极值)**
把一个**日频**的风险 / 活跃度统计量(已实现波动、日内价格粗糙度、成交量集中度)聚合成一个**月度横截面信号**时,文献用过哪些聚合方式,哪一种在样本外更强:
算术均值、**最大值 / 高分位**、幂平均、超过阈值的天数占比、指数加权?有没有文献明确比较过「近一个月的最大值」和「近一个月的均值」,并报告极值版本在控制掉均值版本之后**仍然**显著?
特别想要:**MAX 效应**(近月最大单日收益预测低收益)、异质波动率之谜、跳跃 / 极端日的横截面定价,以及「用凸变换(平方、高次幂)再做移动平均」这种写法有没有先例、被怎样解释。
关键词:极值聚合、近月最大收益、彩票型股票、异质波动率、跳跃风险、幂平均、日内已实现方差;
MAX effect (Bali Cakici Whitelaw), lottery-like stocks, idiosyncratic volatility puzzle, extreme daily returns and the cross-section, realized variance versus realized quarticity, jump risk cross-section, aggregating daily measures into monthly signals (mean versus maximum), power mean / soft-max aggregation.

**L6(对准核心 A:日内成交量分布作为个股的持久特征,以及怎么归一化)**
个股**自己的**日内成交量形态(早盘重 / 尾盘重、尾段与首段之比)在文献里被当成一个**持久的个股特征**处理过吗?具体想要三件事:
(1) **归一化**:用「占当日总量的份额」、用「对数变化 / 几何均值之比」,还是用「减掉全市场当日的典型分时曲线」?有没有文献比较过这几种,并报告过份额口径失效、对数口径有效之类的结果?
(2) **要平均多少天**:个股日内形态的**持续性**有多长(自相关怎样衰减),文献常用的平滑窗口是多少天,等权移动平均还是指数加权?
(3) 这个特征和**换手率水平 / 换手率趋势**是怎样分开的(文献用什么控制变量说明它不是流动性的另一种写法),以及要不要按交易所 / 板块 / 价格限制分组。
关键词:日内成交量形态、分时成交分布、首末段成交占比、日内形态的持续性、成交量季节性去除、对数成交量变化;
intraday volume profile as a stock characteristic, persistence of intraday volume patterns, end-of-day versus opening volume share, deseasonalizing intraday volume, log volume change versus volume share, intraday volume distribution and the cross-section of returns, turnover controls.

**L7(对准 4.2 第 9–10 条与 N 灵感 4:用「排除一截」代替「线性相加」)**
在构造横截面因子时,把第二个变量用作**排除式筛选**(把它最极端的 5% / 10% / 20% 从多头端剔掉)而不是把它线性地加进打分,文献里有哪些做法和证据?
具体:筛选比例一般怎么定(有没有做过比例的敏感性分析)?筛选 / 双重排序 / 线性合成三者在样本外的稳定性比较过吗?
「剔掉极端尾巴之后因子变强」通常被解释成**去掉了噪声或微观结构污染**,还是**筛选变量自身携带 alpha**?文献用什么办法把这两种解释分开?
关键词:排除式筛选、剔除极端值、双重排序、分组条件化、因子构造中的样本筛选、尾部剔除的敏感性;
screening versus linear combination in factor construction, exclusion filters, double sorting versus conditional screens, trimming the extreme decile, breakpoint sensitivity, does the screen carry alpha or remove noise.

**L8(对准核心 C / 1.4 节:名义股价水平这件事值不值得在库里占 6 个位置)**
**名义股价水平**(低价股效应)在 A 股的横截面证据有多强,在**控制掉市值 / 流通市值之后**还剩多少?
文献里它通常被当成什么(散户偏好、彩票偏好、最小价位 / 相对买卖价差、涨跌停与投机),有哪些标准处理:取对数、分桶、**非单调**(剔掉最便宜的那一截)、按板块分组、与换手率交互?
特别想要:有没有文献报告过**驼峰形**的结果(中低价最好、最便宜的一截反而差),以及这个效应在 2015 之后 / 2018–2023 这段时间里是否衰减。
关键词:低价股效应、名义股价、股价幻觉、最小价位、散户偏好、彩票偏好、市值中性化后的价格效应;
nominal stock price level and the cross-section, low-price effect, price illusion, minimum tick size and relative spread, retail / lottery preference for low-priced stocks, China A-share low price anomaly, non-monotonic price effect, decay of the low-price effect after 2015.

---

## 6. 本轮写下的预测(留给第 3 轮对账)

1. **4.2 第 16 条的代数对账会精确相等**(`day_mean(in_delta(Volume, 60))` = +0.5370)。若不等,1.2 / 1.5 节关于「单调变换只通过 EMA 起作用」的全部论断要推翻。
2. **凸聚合的显式版本会复现**:`cross_max(day_durbin_watson(High), 20)` ≥ +1.20,且选中 hl = 0 或 5(概率 70%);
   `pow_2_5(pow_2_5(day_durbin_watson(High)))`(x^6.25)落在 +1.35 ~ +1.60(即继续升或持平,不掉头)。
3. **4.2 第 8 条(一次敲掉三个死重)落在 +1.27 ~ +1.31**(即 ≈ 原 head,gain < 0.1、不替换)。若显著偏离,「整条内链是一个单调变量」的读法有错。
4. **筛子不是通用的**:4.2 第 10 条里把 x 换成 `day_gini(Volume)` / `day_durbin_watson(Vwap)` 之后,分数低于 +1.29、但高于被筛的 +0.56(落在 +0.7 ~ +1.2),
   即筛子既带一点自己的信息、也依赖与 y 的配对。(与之相反的两种极端结果都会直接改变 N 灵感 4 的取舍。)
5. **窗口 400(4.2 第 3 条)不再继续改善**,落在 +1.25 ~ +1.40(即 200 附近饱和)。
6. **若 E 位给核心 A**:产出 ≥ 1 个 head 的概率约 **55%**(远高于第 1 轮 E 的 35% 先验,理由是家族控制从 5 个降到 1 个);
   过线者会**带第二个叶子或一个分桶 / 筛选算子**,而不是核心的时间序列变形;与 head +1.6680 的交易信号 |ρ| 落在 0.3 ~ 0.6。
7. **t@100 与 sigmoid(beta)@100 作为种子进任务之后,至少有一个成为 head 的概率约 80%**(两者各自的 score 已知 ≥ +1.04,与库里任一 head 的 ρ 已知 ≤ 0.12,骨架不同)。
   这是本轮最可能兑现的一笔收益,也是对「R 只替换、不收纳」这个机制漏洞的补救。
8. **股价水平那一簇在 PLAN §3 的贪心去重里会被砍掉至少 3 个**(6 个写法互相的秩相关很可能 ≥ 0.7),所以它在最终库里的实际权重远小于「6 个 head」看起来的样子。
