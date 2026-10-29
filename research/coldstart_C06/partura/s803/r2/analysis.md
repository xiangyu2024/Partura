# 结构解剖:种子 803,C 组,第 2 轮

读的东西:`r2/loc.md`、`r2/loc.json`、`r2/R_prev.json`、`notebook.md`、`r1/{analysis.md, lit.md, missions.yaml, missions_final.yaml, audit_1.yaml, audit_record.json, corr_1.md, corr_1.json}`、`rules.md`;代码:`scripts/c06_check.py`、`scripts/c05_locate.py`、`partura/{steer.py, diagnose.py, ops_ext.py}`、`$HOME/Desktop/AlphaCube-steering/src/alphacube/{catalog.py, operators/common.py, operators/dt_day.py, operators/dt_cross.py, operators/nd_ts.py, operators/nd_cs.py}`。
**没有读**:其他种子目录、C01–C05、`guidance/C0*`、`runs/ lab/ notes/ studies/ handoff/ batches/ docs/ episodes/`、任何 2023-08-08 之后的数字。

证据分四类:**(定位)** 定位工具给的付费数;**(表)** r1 的相关度表;**(源码)** 我读代码确认的语义;**(算术)** 我在本机只用随机张量做的数值验证(不碰数据);**(推断)** 未检验的假设。

---

## 0. 本轮最重要的一条:两个最高分 head 的「偏度」不是偏度

**(源码)** `alphacube/operators/common.py:43` `EPS = 1e-9`;`nanskew_last`(第 575–586 行)返回

```
torch.where(std > EPS, m3 / (std ** 3 + EPS), nan)
```

分母是 `std**3 + EPS`,是一个**绝对**的 epsilon。只要输入窗口的标准差小于约 1e-3,`std**3` 就远小于 1e-9,分母被 EPS 钉死,`ts_skew(x, d)` 返回的不再是偏度,而是 **1e9 × 窗口的三阶中心矩**,即一个**三次齐次**的量。

**(算术)** 同一条形状固定的序列,只改整体尺度:

| 输入尺度 | `ts_skew(x,50)` 第 1 列 | float64 真偏度 | `m3 × 1e9` |
|---|---|---|---|
| 1e+00 | +1.817 | +1.817 | +4.86e8 |
| 1e-02 | +1.811 | +1.817 | +486.2 |
| 1e-04 | **+0.0004861** | +1.817 | +0.0004862 |
| 1e-06 | **+4.862e-10** | +1.817 | +4.862e-10 |
| 1e-08 | **+4.862e-16** | +1.817 | +4.862e-16 |

1e-4 以下,输出与 `m3×1e9` 四位有效数字完全相同 —— 归一化被完全摧毁。

那么 `day_durbin_watson(Open)` 有多大?**(源码 + 算术)** `day_durbin_watson(x) = Σ(Δx)² / Σx²`,分母不去均值。作用在**分钟价格**上,分母 ≈ 241·P̄²,分子 = Σ(ΔP)² = P̄²·Σr²,所以

> **`day_durbin_watson(Open)` ≈ `day_std(Ret)`²**,也就是波动控制 `cross_mean(day_std(Ret), 20)` 的日度原料的**平方**。

**(算术)** 随机价格路径,200 天 × 241 分钟,三个波动水平:`DW / day_std(Ret)²` 的均值 = 1.0041 / 1.0037 / 1.0044,日度秩相关 0.996–0.999。
A 股典型分钟波动 0.1%–0.3% ⇒ DW ≈ 1e-6 ~ 1e-5,其 50 日标准差同量级 ⇒ `std³ ≈ 1e-18 ≪ 1e-9`。**真正的归一化项只占分母的十亿分之一。**

所以快照里最强的两个 head 的真实身份是:

| 表达式 | 看起来是什么 | **实际算的是什么** | 对 σ 的齐次次数 | score |
|---|---|---|---|---|
| `day_durbin_watson(Open)` | 日内一阶序列相关 | 已实现方差(= 波动控制日度原料的平方) | 2 | **−2.13** |
| `ts_skew(day_durbin_watson(Open), 50)` | 已实现方差的 50 日偏度 | **1e9 × 50 日已实现方差序列的三阶中心矩** | **6** | **+1.18 / +1.23** |
| `ts_skew(ts_skew(day_durbin_watson(Open), 50), 50)` | 偏度的偏度 | 再做一次三阶矩 | **18** | 门槛废品(coverage 0.871) |
| `cross_autocorr_s1(ts_skew(ts_skew(...),50), 3)` | 3 日滞后 1 自相关 | **1e9 × 3 日滞后 1 协方差**(见下) | **36** | **+1.56** |

**(源码 + 算术)** `cross_corr` 走 `rolling_pair_reduce`,末行是 `cov / (torch.sqrt(var_x*var_y) + EPS)` —— 同一个绝对 epsilon。本机验证:输入尺度 1e-6 及以下时,`cross_autocorr_s1` 的输出与 `cov×1e9` 完全相同(1e-6 时:−1.885e-4 对 −1.885e-4)。双层 ts_skew 的输出量级约 1e-18,所以**这个「自相关」实际是一个协方差,又把次数翻了一倍**。

量级链条有一个来自真实数据的独立确认:**(定位)** `ts_skew(ts_skew(day_durbin_watson(Open), 50), 50)` 的 coverage 只有 **0.8708**(门槛废品),而第一层 ts_skew 的 coverage 是 0.9983。`nanskew_last` 唯一会返回 NaN 的地方就是 `std > EPS` 这道闸 —— 也就是说,**内层 ts_skew 的输出序列有约 13% 的格子,其 50 日标准差落在 1e-9 以下**。这正说明内层输出量级就是 1e-9 左右,反推 m3(DW) ≈ 1e-18、DW 的 50 日标准差 ≈ 1e-6、`day_std(Ret)` ≈ 1e-3 = 0.1%/分钟 —— 和 A 股分钟波动完全对得上。整条推断不是模拟出来的,是被定位输出的两个 coverage 数字钉住的。

### 这意味着什么

1. **凸度阶梯与 score 的关系,恰好是规则 §4 陷阱 1 的指纹**:次数 2 → **−2.13**(线性部分被控制吃干,残差还反向);次数 6 → **+1.18/+1.23**;次数 18 → 浮点撑不住(门槛废品);次数 36 → **+1.56**。陷阱 1 的原话是「凸度越高 score 越高」。
2. **它为什么能躲过中性化**:`neutral_residual` 是在**秩空间**对 [1, 5 个控制] 做逐日线性投影。σ 的 6 次齐次函数不是 20 日平均 `day_std(Ret)` 的线性函数,所以残差不为 0;但方向上它仍然是「波动低 ⇒ 排在底端」。两个 head 的方向都是 **−1**,即**多头腿 = 已实现方差最小的那一端**。这就是**低波动异象的多头腿**。
3. **它为什么能躲过已知族门槛**:唯一的硬性不合格判定是「与已知族 `cross_mean(day_std(Amt), 30)` 的 |ρ| ≥ 0.5」。**(定位)** 这两个表达式的 `rho_known` 分别是 0.2018 / 0.1886 —— 已知族量的是**成交额的日内离散**,不是波动,门槛根本不朝这个方向看。这就是陷阱 1 所说的「缝」。
4. **m3 的截面排序其实是「最近 50 天里最大的那个波动日」**。**(算术)** 持续性对数正态 RV、2000 只股票:50 日 m3 与窗口内 **max** 的秩相关 **0.992**,与窗口 **均值** 0.937,而与**真正(归一化)的偏度**只有 **0.277**;真偏度与窗口均值的秩相关是 0.012。即:这个表达式**读的是「过去一个季度最糟的那一天波动有多大」,几乎不读形状**。
5. **(算术)** 直接的截面检验:300 只股票、150 天、241 分钟,价格水平 2–100 元、分钟波动 2e-4–2e-3、**日波动乘子的分布对所有股票相同**(所以「波动的形状」在截面上被构造成无信息):`ts_skew(DW,50)` 与股票自身波动水平 σ 的秩相关 **+0.923**(加上 0.01 元 tick 量化后 +0.901),与 tick 粗细 −0.44,与基础活跃占比仅 +0.17。**在一个形状没有任何截面差异的世界里,它照样把股票按波动水平排了出来。**

### 直接可用的两条预测(给 PI 与审计)

- **预测 A**:本轮相关度表里,`ts_skew(day_durbin_watson(Open), 50)` 与波动控制 `cross_mean(day_std(Ret), 20)` 的日度秩 |ρ| 落在 **0.55–0.85**(点估计 0.7);`day_durbin_watson(Open)` 与波动控制 **0.85–0.97**;`cross_autocorr_s1(ts_skew(ts_skew(...),50),3)` 与波动控制 **0.5–0.8**。
- **预测 B**:因此 **DW 家族的任何子树都不能当 E 的核心** —— 规则 §3「E 位还要求核心与每个控制的 |ρ| < 0.5」会把这个位直接判成普通 GP,白费一次审计。要动这个家族,**只能走 R**(R 没有这道门)。

### 另一个必须报的量:**评估的复现噪声 ≈ 0.05**

**(定位)** 完全相同的表达式 `ts_skew(day_durbin_watson(Open), 50)`,同方向(−1)、同半衰期(5),在 heads 表里是 score **1.2257** / valid 2.2876,在拆解的 sufficiency 行里是 score **1.1787** / valid 2.2607。**同一个表达式两次评估差 0.047。**
这是本轮唯一能拿到的噪声标尺,下面所有「必要性」按它读:

> **0.047 以内的必要性 = 0,不要当信息。**

---

## 1. alpha 的来源:逐个核心

### 1.1 `ts_skew(day_durbin_watson(Open), 50)` —— **代理,不是真来源**(陷阱 1)

- 共性:**(定位)** 均值差 **+1.59**,p 0.000,11 个候选含它(含 +0.65 / 不含 −0.94);`ts_skew(day_durbin_watson(Open), 40)` 均值差 +1.17,p 0.032,5 个;`day_durbin_watson(Open)` 均值差 +1.15,p 0.000,25 个。这 3 行全部来自 M 第 2 批的存档(我们两个 r1 任务里没有任何一棵树含 `day_durbin_watson`),所以**这是本轮唯一一组真正独立于我们自己播种的共性证据**。
- 充分性:自身 **+1.18**(train +1.18 / valid +2.26);去掉 `ts_skew` 只剩 `day_durbin_watson(Open)` 掉到 **−2.13**。
- 必要性:外层的第二次 `ts_skew` 必要性 **+0.0065**(远在 0.047 噪声以内)⇒ **完全无用**。
- 敏感性:`Open->Close` **+1.43**(+0.21);窗口 50→25 **+1.06**,50→100 **+1.28**。窗口越长越好,与「它读的是最近一段里最大的波动日」一致。
- 判读:第 0 节已证明它是 σ 的 6 次齐次量,截面排序 ≈ 波动水平 / 季度内最大波动日。这是三类陷阱里的**第 1 类**,而且凸性藏在 `nanskew_last` 的 EPS 里,**光读表达式看不出来**。
- 还剩多少可能是真的:m3 与真偏度的秩相关 0.277(算术),形状成分并非 0,只是小。要把它逼出来,见第 4.2 节 R 的 A 组。

### 1.2 `cross_autocorr_s1(ts_skew(ts_skew(day_durbin_watson(Open), 50), 50), 3)` —— 同一个代理,再乘一层

- **(定位)** 去掉内层 ts_skew 得 **+1.5565**(必要性 +0.0065);窗口 3→2 **+1.44**,3→6 **+1.61**;`Open->Close` **+1.33**。
- **(源码+算术)** 在这个量级下 `cross_autocorr_s1` 不是相关系数而是 `cov×1e9`,所以它只是又一次凸变换。它比子树多出来的 +0.38,**不是「3 日自相关捕捉到了新东西」,而是再平方了一次**。
- 一个必须记下的反面细节:如果只按表达式字面把它当真的 3 点相关系数,我在 O(1) 量级的模拟里得到的分布**严重饱和**:中位数 0.896,49% 的截面挤在 [0.9, 1.0],19% 在 0.99 以上,与 y 的水平秩相关只有 −0.004。**这个读法在真实量级下是错的** —— 写下来是为了提醒:这个算子库里凡是带 `+ EPS` 的归一化算子(`nanskew_last`、`nankurt_last`、`rolling_pair_reduce` 的 corr),**在小量级输入上都会退化成未归一化的矩/协方差**。以后看到 `ts_skew` / `ts_kurt` / `*_corr` 作用在分钟收益、方差、比例这类小量上,先算量级再谈机制。
- `Open` 与 `Close` 的优劣在两个 head 上**符号相反**(head 1:Close 差 −0.23;head 2:Close 好 +0.21),而噪声标尺是 0.047。±0.2 的差在这个家族里**不稳定**,不要据此讲故事。

### 1.3 `sub(day_hurst(Close), day_kurt(Ret))` 与 head 3 —— **真来源只有 `day_kurt(Ret)`;`day_hurst(Close)` 一分没贡献**

head 3 = `cross_ema(cs_winsor(mul(add(sub(day_hurst(Close), day_kurt(Ret)), 0.5), sub(1, cs_winsor(mul(add(sub(day_hurst(Close), day_kurt(Ret)), 0.5), sub(1, day_zero_ratio(Ret))))))), 20)`,score +0.99。

- 充分性:**(定位)** 整个大结构 +1.0132;`sub(day_hurst(Close), day_kurt(Ret))` 单独 **+0.9701**;而 `day_kurt(Ret)` 自己(head)是 **+0.9669**。
  ⇒ **把 `day_hurst(Close)` 减进来只值 +0.003(噪声标尺的 1/15);整个 head 相对裸核心只值 +0.024。**
- 必要性:两处 `add(·, 0.5)` 分别 +0.0195 / +0.0126;整个第二因子 `sub(1, cs_winsor(...))` +0.0389 —— **三项全在噪声以内,都是死重**。唯一超过噪声的是 +0.3155,但那一行是把 `sub(hurst, kurt)` 换成 `day_hurst(Close)`,也就是**把 `day_kurt(Ret)` 拿掉**:kurt 是承重墙,hurst 不是。
- 敏感性:`Close->Vwap` **门槛废品(coverage 0.8112)** —— 见 1.6 的工程解释;`cross_ema` 20→10 掉到 +0.846,20→40 +0.994。
- 还有一条来自 r1a 自己产出列表的付费数:`cross_ema(sub(day_hurst(Close), day_kurt(Ret)), 20)` = **+0.8156**,而 `sub(day_hurst(Close), day_kurt(Ret))` = +0.9701。**`cross_ema(·,20)` 这个部件代价 −0.155**(噪声标尺的 3 倍)。原因清楚:奖励本身就在 hl ∈ {0, 5, 20} 上搜,表达式里再平滑一次是重复。
- 这个结构真正的身份:记 X = `sub(day_hurst(Close), day_kurt(Ret)) + 0.5`,则 `mul(X, sub(1, cs_winsor(mul(X, ...))))` ≈ X − X²·(1−零收益比例) —— **一个关于核心的二次(凸)型,再做 EMA**。和 head 6 一样,这是**陷阱 1 的机制搬到峰度轴上**。

### 1.4 `cross_mean(mul(add(day_kurt(Ret), 3), add(day_kurt(Ret), 3)), 15)`(head 6,+0.65)—— **核心的凸改写**

- **(算术/代数)** `day_kurt(Ret) + 3 = (241/k)·c > 0` 恒成立,所以 `(kurt+3)²` 是 `kurt+3` 的**严格单调变换**,逐日截面秩与 `day_kurt(Ret)` **完全相同**。它之所以没被库的 ρ ≥ 0.7 禁令挡住,是因为禁令比的是**平滑后的信号**:凸变换之后再取 15 日平均(Jensen),等于让最近 15 天里**最极端的那一天**主宰(与 1.1 的 m3 是同一个把戏)。
- 判读:**不是新来源,是「核心 + 一次凸变换 + 一次平滑」**。它的 score(+0.65)与 valid(+0.97)也是六个 head 里最低的。

### 1.5 `cs_mask_top_replace_mean(mul(0.5, neg(day_centroid(Amt))))`(head 5,+0.86)—— **真来源,库里唯一的新机制**

- **(源码)** `day_centroid(x)` = `Σ(t·|x|)/Σ|x|/(T−1)` ∈ [0,1],成交额的**日内时间重心**:0 = 全在开盘,1 = 全在收盘。对 Amt 的尺度完全不敏感 ⇒ 不是流动性水平的改写。注意 `day_centroid` 内部先取 `abs()`,所以 `day_centroid(Ret)` ≡ `day_centroid(abs_(Ret))`,**别两个都写**。
- 充分性:**(定位)** `day_centroid(Amt)` 单独 **−0.0846**,`neg(day_centroid(Amt))` 同值(方向是自由参数)。
- 必要性:`mul(0.5, ·)` 必要性 **0.0000** —— 纯死重(正数缩放不改秩,也不改 top-10% 掩码);`neg` 必要性 **+1.4555** —— 全部 alpha 都在这一侧。
- 敏感性:`Amt->Volume` **+0.904**(+0.042,低于 +0.1 替换线)。
- **(源码+算术)** 它到底在选什么?`cs_mask_top_replace_mean` 把每日截面里**最高的 10%** 替换成当日均值。模拟 5000 只股票(centroid ~ Beta(5,5)):被替换的那 10% 落到新分位 **0.549**(正中间),而新信号的**多头十分位**恰好是原始因子的 **80–90 百分位**(min 0.800 / 中位 0.850 / max 0.900)。
  ⇒ **多头腿 = 「成交重心偏早、但不是最早的那一档」**,即 centroid 的 10–20 百分位。
  两个事实其实是同一个事实:裸 −centroid 只有 −0.08(它的多头腿是**最极端偏早**那一档);把 `neg` 去掉(掩码改切最晚一端)后多头腿变成最极端偏早档,掉到 **−0.59**。**最极端偏早的那 10% 是垃圾带**(开盘几分钟吃掉全天成交 = 停牌 / 极薄 / 开盘封板),`cs_mask_top_replace_mean` 正好是把它切掉的算子。
- **陷阱 2 不成立**:**(源码)** `diagnose.rank_rows` 就是 pandas 的 `rank(axis=1)`,**并列取平均秩**,不按列序拆并列;而且 hl=20 的 EMA 发生在排序之前,逐日变动的并列块在 EMA 之后不再精确相等。这 10% 的并列块不会变成列序斜坡。
- 判读:**真来源**。机制 = 成交的**日内时点**。五个控制里有成交额的**水平**(流动性)和**日内离散**(已知族),**没有任何一项是时点**;`rho_known` = −0.194。这是库里唯一一个时点/顺序类的真来源。

### 1.6 工程事实(写给 PI,免得重蹈)

- **(源码)** `day_hurst` 内部 `torch.cumsum`,**NaN 会沿分钟轴传染整行**,`R` 变成非有限 ⇒ 整天 NaN。所以 `day_hurst(Vwap)`、`day_hurst(in_*)`(任何有 NaN 分钟的输入)覆盖率必然塌。定位输出的 `Close->Vwap` **coverage 0.8112 门槛废品**就是这一条。**不要再写 `day_hurst` 作用在 Vwap / in_* 上。**
- **(源码+算术)** `day_durbin_watson` 在 `var_x < 1e-8`(float32 下 `Σx²/n − mean²` 的灾难性相消)时返回 NaN;真实数据里这只命中**全天封板/停牌**(coverage 0.9976),影响很小,但它系统性地把**最极端的那一类日子**从 50 日窗口里剔掉。
- **(算术)** `day_durbin_watson` ∝ **活跃分钟占比 × 活跃分钟方差**:固定每活跃分钟方差,k=240/120/48 时 `DW/(k/240)` = 2.494e-7 / 2.502e-7 / 2.458e-7(常数)。所以这个家族里**稀疏度和波动是乘在一起的**,与第 1 轮 `day_kurt(Ret)` 的稀疏度通道是同一条。
- **(表)** 凡是建立在 `Vwap` 分钟上的日内统计量,都会**通过 Vwap 的 NaN 形态继承流动性控制**:r1 的 b 位里 `cross_mean(div(day_std(in_logchg(Vwap,10)), day_std(in_logchg(Vwap,1))),20)` 的 liq = **0.72**、known 0.67;`cross_mean(day_autocorr(in_logchg(Vwap,1),1),20)` liq **0.69**、known 0.66。写 N 种子时要么避开,要么分桶。
- **(源码)** `log(x) = log(|x|)`,且 |x| ≤ 1e-9 返回 NaN。`log(day_durbin_watson(Open))` 的 NaN 门限相当于 `day_std(Ret) < 3.2e-5`,只有近乎冻结的日子才碰到,可用;但要知道这条底线存在。

---

## 2. 烂部件(适合做 R)

按「超过 0.047 噪声标尺」排序。

| 所在 head | 烂部件 | 证据 | 性质 |
|---|---|---|---|
| head 3 | `cross_ema(·, 20)` | 同核心上付费对照:`cross_ema(sub(hurst,kurt),20)` +0.8156 vs `sub(hurst,kurt)` +0.9701,**代价 −0.155**;head 内窗口 20→10 再掉 −0.144 | **有害**(奖励自己在搜 hl,重复平滑) |
| head 5 | `mul(0.5, ·)` | 必要性 **0.0000** | 纯死重(正缩放不改秩) |
| head 1 | 内层 `ts_skew(·, 50)` | 必要性 **+0.0065**;它自己作为子树 coverage 0.8708 门槛废品 | 死重,而且是浮点垃圾 |
| head 3 | 两处 `add(·, 0.5)` | 必要性 +0.0195 / +0.0126 | 死重 |
| head 3 | 整个第二因子 `sub(1, cs_winsor(mul(add(sub(day_hurst(Close), day_kurt(Ret)), 0.5), sub(1, day_zero_ratio(Ret)))))` | 必要性 **+0.0389** | 死重(占了 head 一半字符) |
| head 3 | `day_hurst(Close)` 这一项本身 | 充分性对照:`sub(hurst,kurt)` +0.9701 vs `day_kurt(Ret)` +0.9669,**+0.003** | 在这个写法里没贡献(换写法未必) |
| head 6 | `mul(x, x)` | 代数:`(kurt+3)²` 与 `kurt+3` 逐日截面秩完全相同;它唯一的作用是让 `cross_mean(·,15)` 变成「取最极端那一天」 | **陷阱 1 的机制,应改写成显式尾部统计量** |
| head 2 / head 1 | `ts_skew` 的**未归一化输入** | 第 0 节:EPS=1e-9 把分母钉死,`ts_skew` 返回 1e9·m3,不是偏度;模拟里 m3 与窗口 max 秩相关 0.992、与真偏度 0.277 | **部件在数值上实现的不是它声称的东西** |

**换掉反而更好的(定位已付费)**:
- `ts_skew(day_durbin_watson(Close), 50)` = **+1.4328**,比 head 2(+1.2257)高 **+0.2071**,`rho_head` 0.9424 ≥ 0.5、`rho_known` 0.1933 < 0.5 ⇒ 规则上会**替换** head 2。
- `cross_autocorr_s1(ts_skew(ts_skew(DW(Open),50),50), 6)` = +1.6119(+0.049,不到线);`cs_mask_top_replace_mean(mul(0.5, neg(day_centroid(Volume))))` = +0.904(+0.042,不到线)。

---

## 3. 之前的任务,以及上一轮的预测对不对

### 3.1 `c06s803Cr1a_Ea`(E,核心 `day_kurt(Ret)`)

**(定位)** 评分 104,过线(≥0.5)**41**,入 heads **2**;采样拒绝计数 `{c05_no_core: 1974, c05_skeleton: 36}`,**`periphery_seen` 一次都没触发**。
- **41 个过线只有 2 个进库 ⇒ 39 个被库的 ρ≥0.7 / 骨架禁令挡掉。** 这个位的产出几乎全是核心的改写。
- 进库的两个,按第 1.3 / 1.4 节:head 3 相对裸核心只值 **+0.024**,head 6 是核心的**凸改写**。**结论:这 96 次付费评估没有买到新信息,买到的是两个「核心换皮」的库位。**
- 为什么会这样:C06 的规则(`rules.md` §2)明确「E 的奖励**不**额外控制核心的家族」,防重复全靠库禁令;而**绕过「平滑后秩相关 < 0.7」最便宜的办法恰好就是凸变换 + 平滑**。这是这个位的结构性激励,不是 PI 写坏了。
  (附带更正:`r1/analysis.md` §4.1 写的「家族以 sign×EMA_20 进控制基」是 C05 的规则,**C06 不是这样**。下一轮写 E 时不要再按那条设计。)
- `c05_no_core` 1974 次 vs 评分 104 次:**GP 自己的变异约 95% 的尝试因为不含核心被丢掉**,E 位的有效搜索非常窄 ⇒ **种子质量几乎决定这个位的结果**。

### 3.2 `c06s803Cr1b_Nb`(N,日内价格效率 / 序列相关)

**(定位)** 评分 59,过线 **2**,入 heads 1。前五名:`cs_mask_top_replace_mean(mul(0.5, neg(day_centroid(Amt))))` +0.86、它的 `neg` 版 +0.86(同一个东西)、`neg(LogFloatShares)` +0.48、`pow_2_5(LogFloatShares)` +0.48、`neg(cs_mask_top_replace_mean(mul(LogTotalCap, neg(LogFloatShares))))` +0.38。
- **这个位播下去的机制(方差比、Vwap 自相关、路径效率)在 59 个候选里一个都没进前五。** 唯一的产出 `day_centroid(Amt)` 来自 GP 自己那一半随机树,对应的是 `r1/analysis.md` §4.3 里排第三、**最后没被选中**的 N-C(成交时间 vs 钟表时间)。
- 两个 `LogFloatShares` 的 +0.48(`neg` 与 `pow_2_5` 同分)是**陷阱 3 的教科书例子**:市值控制的非线性改写。没到 0.5 所以没进库,但说明这个位有相当一部分算力花在重写市值上。

### 3.3 R(头 `day_kurt(Ret)`,7 个变体,全部不构成替换/收录)

**(R_prev + 表)**

| 变体 | 门槛 | score | ρ_head(表 / 定位) | ρ_known |
|---|---|---|---|---|
| `day_kurt(in_logchg(Vwap, 1))` | 过 | **+0.024**(train 0.351) | 0.69 / **0.81** | 0.072 |
| `day_kurt(in_pct(Close, 1))` | 过 | +0.9685 | **1.00** / 1.00 | −0.085 |
| `day_kurt(in_madz(Ret, 30))` | **废品**(coverage 0.4665) | — | 0.39 | — |
| `day_gini(Ret)` | 过 | −0.274 | 0.29 / 0.21 | **−0.626 ⇒ 不合格** |
| `day_gini(in_logchg(Vwap, 1))` | 过 | −0.201 | 0.46 / 0.53 | −0.409 |
| `day_es_ratio_hi(Ret)` | 过 | −0.632 | 0.47 / 0.43 | −0.073 |
| `day_es_ratio_lo(Ret)` | 过 | −0.571 | 0.38 / 0.45 | −0.080 |

这一组买到的真东西不是替换件,而是**三个判决**:

1. **`Ret` ≡ `in_pct(Close,1)`**(ρ = 1.00,score 0.9685 ≈ 0.9669):`Ret` 首分钟不含隔夜跳空,「隔夜污染峰度」这个假设**死了**。
2. **把无成交分钟剔掉,ρ 只掉到 0.69–0.81,score 从 +0.97 塌到 +0.02。** 也就是说:**`day_kurt(Ret)` 排序里的 20–30% 承载了全部分数**,而那 20–30% 正是零收益分钟贡献的那一块。
3. **把零质量放大(`day_gini(Ret)` 把零分钟按 |x|=0 算进基尼)⇒ 与已知族 0.626、与流动性 0.67,直接不合格。** 零质量这一维确实属于流动性/摩擦族。

把 2 和 3 跟 r1 审计员的判读对起来:审计员从相关度表(c 修正版与 head 原始 ρ = 0.89)推出「稀疏度只是次要成分,PI 的假设与表对不上」。**这个推论对「排序」成立,对「分数来自哪里」不成立** —— 付费的 R 第 1 条把它翻了过来:乘上 (1−零收益比例) 不会把零分钟从排序里拿掉(只是重新缩放,所以 ρ 还有 0.89),而真的把零分钟剔掉(Vwap 口径)会让分数蒸发。**所以 H1 以更锐利的形式成立:alpha 不是整条峰度排序,而是峰度排序里由「没有成交的分钟」贡献的那一薄层。** 这一条应写进 notebook,并在本轮计划里明确讲给审计员,因为审计员读不到本文件。

### 3.4 审计员挡掉了什么,为什么(r1,两位都 3/3 放行)

- a 位(E):表划种子 1、4、6(与 head 原始 ρ 0.89 / 0.91 / 0.94);审计划 6–11。理由:(i) 7–10 是「只靠外层 20 日平滑躲过库禁令的 head 平滑版」(交易信号残差 0.85–0.87),没有执行本位要做的事;(ii) **种子 10、11 用 `day_last(Close)` 冒充 tick 网格粗细 —— 生产库的 Open/High/Low/Close/Vwap 都是后复权价,与真实成交价差一个 2.5–113 倍的个股因子**,按它分桶实际是按「上市以来累计复权收益 × 发行价」分桶。审计员给出的替代:用 `div(day_sum(Amt), day_sum(Volume))`(未复权价位)。剩 4 颗,刚好到线。
- b 位(N):**表划种子 1–5**,全部因为与流动性 0.51–0.72 / 已知族 0.47–0.67 —— 「一分钟尺度的方差比和带符号一阶自相关在 train 上主要是流动性量」。审计划种子 6(`abs_(day_autocorr(...))` 对流动性是 U 形,线性中性化去不掉,陷阱 3;且 |ρ̂| 的噪声底 ≈ 0.8/√配对数 本身就是稀疏度代理)与 10(后复权价分桶)。剩 5 颗。
  **这两条划法事后看都对**:剩下的 5 颗确实什么也没产出,而被划掉的 5 颗若留下,大概率会生出一堆流动性改写。
- R:3 分放行,并点明 7 个变体里有 3 个浪费(变体 2 ≡ head、变体 3 必然废品、变体 4 把零质量放大回来)。**事后全部命中**(变体 2 ρ=1.00;变体 3 coverage 0.4665;变体 4 已知族 0.626 不合格)。审计员的预判质量明显高于 PI 的,本轮写计划时值得先自己过一遍「这条会不会被这样挡」。

### 3.5 notebook / r1 analysis 里的预测,对不对

| 预测 | 结果 |
|---|---|
| a 位产出 head 概率 ~45%,最可能是分桶系或 20 日均值的代数修正版,score 0.5–0.8,与核心 ρ 0.3–0.6 | **部分对**:产出 2 个 head,但不是分桶系(分桶系被划掉了),是 `cs_winsor` 二次型;score 0.99 / 0.65(高于预测区间上沿) |
| 12 颗种子里 0–3 颗因 ρ≥0.7 被划 | **对**(表划 3 颗:0.89 / 0.91 / 0.94) |
| 核心与流动性控制 \|ρ\| 可能接近 0.5 | **错**:core 的控制 \|ρ\| 最大 0.26(size),liq 0.09、vol 0.007。`day_kurt(Ret)` 是干净的 |
| b 位产出 head 概率 ~40%,最可能是 Vwap 自相关或 VR 分桶版,方向押「多头 = 接近随机游走」 | **机制全错、结果偶然对**:产出 1 个 head,但播下去的机制一个都没过线,赢家是没被选中的 N-C(成交时点) |
| R#1 `day_kurt(in_logchg(Vwap,1))` score 明显低于 0.97(押 < 0.6) | **对**(+0.024) |
| R#3 `day_gini(Ret)` 过门槛且 ρ_head ≥ 0.5,但不够替换线 | **一半**:过门槛 ✓、不够替换线 ✓,但 ρ_head 只有 0.21–0.29(预测 ≥0.5 错) |
| 16 个 R 变体里 1–3 个栽在门槛,最可能 `day_es_ratio_lo` 的 coverage | **数目对、对象错**:实际提交 7 个,1 个废品,是 `day_kurt(in_madz(Ret,30))`(审计员已事先指出 MAD=0);`day_es_ratio_lo` coverage 0.9869 顺利过关 |
| 第 2 轮共性表仍很可能是空的或极少几行 | **错**:15 行。原因正是我们自己的 E 位 —— 104 个候选都被迫含同一个核心,存档里于是出现大量共享子树 |
| 第 2 轮拆解会真的花钱 | **对**:26 次(r1 是 0),因为 M2 的 head 带窗口且含 SWAP 里的 `Open` |
| `periphery_seen` 拒绝计数会很低(<5),skeleton 与库 ρ 禁令高得多 | **对**:periphery_seen 0、skeleton 36;但真正的大头是预料之外的 `no_core` **1974** |

**一条必须写进本轮判读的方法论警告**:共性表的 15 行里,带 `day_kurt(Ret)`、`day_hurst(*)`、`day_zero_ratio(Ret)`、`ts_med(...)`、`ts_quantile_q50(...)`、`day_centroid(Amt)` 的那 11 行,**几乎全部来自我们自己的 r1a / r1b 存档**(r1a 的 104 个候选每一个都含 `day_kurt(Ret)`,所以它的 n_with=65 基本是我们自己造的;`day_hurst(Close)` n=15 里有 14 个就落在 `sub(day_hurst(Close), day_kurt(Ret))` 里)。**自己播下去的子树在共性表里富集,不是独立发现的证据。** 独立于我们的只有 `ts_skew(day_durbin_watson(Open), 50/40)` 和 `day_durbin_watson(Open)` 这三行 —— 而第 0 节说明它们是陷阱 1。

---

## 4. 本轮候选

### 4.1 值得深挖的核心(≤3)

**先说不要碰的**:按预测 B,`day_durbin_watson(Open)`、`ts_skew(day_durbin_watson(Open), 50)`、`cross_autocorr_s1(...)` 作为 E 核心会被「核心与控制 |ρ| ≥ 0.5」判死。这个家族只能走 R。

#### 核心 ①(首选)`day_hurst(Close)`
- 合法性:**(源码)** 它是 head 3 树上的节点,也在共性表与核心卡里 ⇒ 在 `c06_check.py` 的 `known` 里;`is_valid_root` 通过(已本机 parse 验证);E 位用过 0 次。
- 它在算什么:**(源码)** 对**分钟价格**整行做 R/S —— 去均值、累加、极差 / 标准差,再 `log(R/S)/log(241)`。对 x 的**尺度和水平都不敏感**。**(算术)** 同一行上:直线趋势 **0.847**,随机游走 **0.747**,快速振荡 **0.332**,一次性跳一档后保持 **0.874**,单根尖刺 **0.500**;`h(20·rw) = h(rw) = 0.7465`,`h(rw+100) = 0.7465`。
  ⇒ 它读的是**日内价格路径的形状**(走出趋势 / 来回震荡),而且**是库里唯一一个顺序敏感又不等于波动的量**:`day_kurt`、`day_std`、`day_gini`、`day_zero_ratio` 把分钟顺序打乱都不变,`day_durbin_watson` 顺序敏感但已证明等于已实现方差。这正是 r1 的 N-A「日内定价效率」想做的事,只不过是 GP 在我们的 E 位里替我们找到的。
- 已见过的外围写法(全部出自我们自己的 r1a 存档,都把它和 `day_kurt(Ret)` 绑在一起):
  `sub(day_hurst(Close), day_kurt(Ret))`;`ts_med(sub(day_hurst(Close), day_kurt(Ret)), 40)`;`cross_ema(sub(day_hurst(Close), day_kurt(Ret)), 20)`;head 3 那个 `cross_ema(cs_winsor(mul(add(sub(...), 0.5), sub(1, cs_winsor(mul(add(sub(...), 0.5), sub(1, day_zero_ratio(Ret))))))), 20)`;同族的 `sub(day_hurst(Ret), day_kurt(Ret))`、`ts_med(sub(day_hurst(Ret), day_kurt(Ret)), 40)`。
  ⇒ **「不含 `day_kurt(Ret)` 的外围」整片空白**;而 `periphery` 是「核心之外算子**名字**的集合」,所以只要外围不出现 `day_kurt`,就一定不与见过的相同。
- 外围该做的事(方向,不是结论):① **把稀疏度条件掉** —— 算术已显示「一天只跳一档」会读成 0.874(假趋势),所以 `cs_bucket_rank(day_hurst(Close), cross_mean(day_zero_ratio(Ret), 20))` 这类组内排序直接对准已知污染;② **换成「相对自己平时」** `cross_zscore(day_hurst(Close), 60)` / `cross_madz`;③ **稳健平滑** `ts_med(day_hurst(Close), 40)`;④ **按未复权价位分桶**(审计员 r1 给的工具)`cs_bucket_rank(day_hurst(Close), div(day_sum(Amt), day_sum(Volume)))`;⑤ 按 `LimitWidth` / `BoardCode` 分桶(创业板 2020-08-24 的 10%→20% 改革落在 train 段内)。
- 风险(要在计划里写明):它**从未被单独评估过**,这个位同时在买那个测量;它在 head 3 里的边际贡献只有 +0.003。

#### 核心 ②`day_centroid(Amt)`(或 `neg(day_centroid(Amt))`)
- 合法性:共性表 / 核心卡里都有;E 位用过 0 次;`rho_known` −0.194。预测它与 5 个控制的 |ρ| 全部 < 0.3(它对 Amt 的尺度不敏感,而控制里只有 Amt 的**水平**与**日内离散**)。
- 为什么值得:第 1.5 节 —— 库里**唯一**的真新机制,而且我们已经知道**问题出在哪**(最极端偏早的 10% 是垃圾带),外围有一件明确的活可干。
- 已见过的外围写法:`neg(·)`;`mul(0.5, neg(·))`;`cs_mask_top_replace_mean(mul(0.5, neg(·)))`;`neg(cs_mask_top_replace_mean(mul(0.5, neg(·))))`;以及拆解里的 `cs_mask_top_replace_mean(neg(·))` 与 Volume 版。外围算子集合至今只用过 `{neg}`、`{mul, neg}`、`{cs_mask_top_replace_mean, mul, neg}`。
- 外围该做的事:① **诚实地切垃圾带** `cs_winsor`、`cs_bucket_*`、`cross_tail_mean_q25/75`(替代把 10% 并到均值这种粗暴写法);② **时点的稳定性而不是水平** `cross_madz(day_centroid(Amt), 20)` / `cross_stddev(·, 20)`(「一直很早」vs「偶然很早」);③ **两个时点相减** `sub(day_centroid(Amt), day_centroid(Volume))`(贵的那几分钟在哪里 = 大单时点)、`div(day_centroid(Amt), day_centroid(Volume))`;④ 按流动性 / 市值分桶。
- 注意:若 E 位选了这个核心,**N 位就不要再做时点家族**(见 4.3 的搭配)。

#### 核心 ③(备选)`day_kurt(Ret)`(剩 1 个 E 位)
- 合法性:**(表)** 控制 |ρ| 最大 0.26,E 位已用 1 次、还剩 1 次。
- 第 1 轮之后锐化的假设(第 3.3 节):**alpha 在峰度排序里「由没有成交的分钟贡献」的那 20–30%**,不是整条排序。所以外围要做的不是「把稀疏度拿掉」(r1 做过,c 修正与核心 ρ 0.89,等于没拿掉),而是**把那一层单独拎出来**:`sub(day_kurt(Ret), day_kurt(in_logchg(Vwap, 1)))`(钟表口径减成交口径 = 零分钟对四阶矩的净贡献)、用**停顿的结构**而不是**停顿的个数**(`cross_mean(day_flat_run_max(Ret), 20)`、`day_distinct_ratio`)。
- 为什么排第三:上一个 E 位在这个核心上花了 96 次评估,买回来两个换皮;审计员对「同一机制再净化一次」已经给过「够不上 4」的评价。要再来一次,外围机制必须明显不同(上面那条减法是的)。

### 4.2 R 目标(建议 15 个变体,按优先级;超了就从后往前砍)

**A 组 —— 头 `ts_skew(day_durbin_watson(Open), 50)`。烂部件:`ts_skew` 的未归一化输入**(依据:第 0 节 —— EPS=1e-9 把 `std³+EPS` 钉死,算子返回 1e9·m3 而不是偏度;双层版 coverage 0.8708 是 `std > EPS` 这道闸在 1e-9 上咬住的直接证据)。
1. `ts_skew(log(day_durbin_watson(Open)), 50)` —— 诚实的「对数已实现方差的偏度」。**本轮信息量最大的一次评估。**
2. `ts_skew(div(day_durbin_watson(Open), cross_mean(day_durbin_watson(Open), 50)), 50)` —— 诚实且自归一化,没有 log 的下界问题。
3. `ts_std(log(day_durbin_watson(Open)), 50)` —— 如果形状里有东西,可能是**离散度(vol-of-vol)**而不是偏度。
4. `cross_mean(pow_3(day_durbin_watson(Open)), 50)` —— 把 `ts_skew` 实际在算的东西**显式写出来**:纯 6 次凸性、零形状成分。**提醒 PI 在计划里写明**:预测它与 head 2 的 ρ ≥ 0.6(两者都 ∝ σ⁶),所以万一它赢了,规则会走「替换」而不是「收录」,不会给库里加一个新位。
5. `ts_skew(day_durbin_watson(Close), 50)` —— 定位已付费 +1.4328(+0.2071),按规则会替换 head 2。**要不要拿**:拿到的是免费的样本内分数,换来的是同一个陷阱的另一份(ρ_head 0.94,不增加任何多样性),而且 Open/Close 的优劣在两个 head 上符号相反(+0.21 vs −0.23),只有噪声标尺的 4 倍。我的意见:可以拿(不占新库位),但别把它当成发现。

**预测**:1 与 2 的 score 掉到 **< 0.5**(押 0.0–0.4),4 的 score **≥ 1.1**。若如此,规则 §4 陷阱 1 就在本种子最强的 head 上被当场证实,第 3 轮不该再在这个家族上花 GP 位。若 1 或 2 反而 ≥ 1.1,则第 0 节的判读推翻,M2 家族是真的 vol-of-vol 形状因子,第 3 轮应该用一个 E 位去挖它。

**B 组 —— 头 `cross_autocorr_s1(ts_skew(ts_skew(day_durbin_watson(Open), 50), 50), 3)`。烂部件:内层 `ts_skew`(必要性 +0.0065,且自身 coverage 0.8708)+ 3 日窗口(2→3→6 单调:+1.4447 / +1.5630 / +1.6119)。**
6. `cross_autocorr_s1(ts_skew(day_durbin_watson(Open), 50), 6)`
7. `cross_autocorr_s1(ts_skew(day_durbin_watson(Open), 50), 10)`
8. `cross_autocorr_s1(ts_skew(log(day_durbin_watson(Open)), 50), 6)` —— 诚实内层 + 稳定窗口;顺便告诉我们那 +0.38 是不是也只是凸性。

**C 组 —— 头 `cross_mean(mul(add(day_kurt(Ret), 3), add(day_kurt(Ret), 3)), 15)`。烂部件 `mul(x, x)`:`(kurt+3)²` 与 `kurt+3` 逐日截面秩完全相同(kurt+3 = (241/k)·c > 0),它唯一的作用是让后面的 15 日平均变成「取最极端那一天」。应写成显式的尾部统计量。**
9. `cross_quantile_q75(add(day_kurt(Ret), 3), 15)`
10. `cross_tail_mean_q75(day_kurt(Ret), 15)`
11. `cross_max(add(day_kurt(Ret), 3), 15)`
**预测**:至少一条 ≥ 0.65(= 原 head);能不能到 +0.75 的替换线不好说。若能,库里就用一个说得清机制的写法换掉一个凸改写。

**D 组 —— 头 `cs_mask_top_replace_mean(mul(0.5, neg(day_centroid(Amt))))`。烂部件:`mul(0.5, ·)`(必要性 0.0000,纯死重)与一刀切 10% 的 `cs_mask_top_replace_mean`(把十分之一的截面并到当日均值,信息被丢掉而不是被利用)。**
12. `cs_winsor(neg(day_centroid(Amt)))` —— 诚实的 1%/99% 截尾。它能不能复现 +0.86,直接告诉我们「垃圾带」有多宽。
13. `cs_mask_top_replace_mean(cs_mask_top_replace_mean_neg(neg(day_centroid(Amt))))` —— 两端都切。
14. `cs_mask_top_replace_mean(neg(day_centroid(Volume)))` —— 定位已付费 +0.904(+0.042,不到线),凑满时才放。

**E 组 —— 头 `cross_ema(cs_winsor(mul(...)), 20)`(head 3)。烂部件:`cross_ema(·, 20)`,同核心上付费对照代价 −0.155,原因是奖励本身在 hl ∈ {0,5,20} 上搜,表达式里再平滑一次是重复。**
15. `ts_med(sub(day_hurst(Close), day_kurt(Ret)), 40)` —— 用稳健的滚动中位数替掉 `cs_winsor + cross_ema`,同时把那一堆死重(两处 `add(·,0.5)`、整个第二因子)一并去掉。它也是核心卡第 8 条(均值差 +1.45,p 0.002)。
**预测**:head 3 靠简化很难过 +0.1(裸子树 +0.9701 < 0.9901+0.1),这一条主要是信息,不是替换。只给它 1 个位。

### 4.3 N 的灵感

**N-甲(首选,与核心 ① 搭配)成交时点与价格时点的领先滞后。**
- 机制:`day_centroid` 给的是「这一天的量落在什么时候」。作用在 `Amt`、`Volume`、`|Ret|` 上就得到三个时间重心(注意 **`day_centroid` 内部先取 `abs()`,所以 `day_centroid(Ret)` ≡ `day_centroid(abs_(Ret))`**)。`sub(day_centroid(Ret), day_centroid(Amt))` = **价格的移动发生在成交到来之前还是之后**:知情交易先推价格、成交随后跟进(负值),还是流动性 / 指数流在收盘集中、价格被动跟随(正值)。`sub(day_centroid(Amt), day_centroid(Volume))` = 贵的那几分钟相对普通分钟的位置 = **大单时点**。`day_corr(in_index(Amt), Amt)`、`day_argmax(Amt)` 是同族的另两种写法。全部是时间指数的差 / 比,**无量纲**,对波动、成交额水平、市值都不敏感。
- 为什么库里没有:五个控制里有成交额的水平与日内离散,**没有时点**;六个 head 只有一个碰到时点(head 5,只用了 `Amt` 的重心,`rho_known` −0.194)。**领先滞后(两个重心之差)与「量偏早还是偏晚」是不同的机制。**
- 要防的坑:① 极薄股票的重心会被开盘 / 收盘集合竞价钉死 ⇒ 必须 `cross_mean(·, 20)` 以上的平滑 + 按流动性分桶;② 不要用 Vwap 口径的量(表证据:Vwap 类日内统计量的 liq |ρ| 0.38–0.72)。
- 若 E 位选了核心 ②(`day_centroid(Amt)`),**这个 N 的创新度会被判成「与已有 head 同一机制」** ⇒ 二者只能选一个。

**N-乙(与核心 ② 搭配)停顿的结构,而不是停顿的个数。**
- 机制:第 3.3 节证明了「把无成交分钟剔掉,ρ 只掉到 0.69–0.81,分数塌到 0.02」,所以 alpha 在零分钟贡献的那一层;而 `day_zero_ratio` 只数**个数**,`day_gini(Ret)` 把它放大到流动性族里去(已知族 0.626,不合格)。真正没人碰的是**排列**:`cross_mean(day_flat_run_max(Ret), 20)`(最长静止段)、`day_distinct_ratio`、`sub(day_kurt(Ret), day_kurt(in_logchg(Vwap, 1)))`(钟表口径与成交口径之差 = 零分钟对四阶矩的净贡献)。
- 要防的坑:比例类日度量 distinct ≈ 0.05 会被判门槛废品,必须自带 `cross_mean(·, 20)` 外壳(r1 已踩过)。

**N-丙(只有在 A 组 R 结果反转时才值得)诚实的日内波动形状族。** `ts_skew(log(DW(Open)),50)`、`ts_std(log(DW(Open)),50)`、`ts_kurt(log(DW(Open)),50)`、`div(day_durbin_watson(Open), cross_mean(day_durbin_watson(Open), 50))`,全部必须 `cs_bucket_rank(·, cross_mean(day_std(Ret), 20))` 在波动十分位内排序。但 R 的 A 组本轮就会给出答案,而 R 与 GP 位是同一次任务并发起的(r1 已记:R 的结果来不及给同一轮的 GP 位用),所以**这个 N 本轮做不了,留给第 3 轮**。

**搭配建议**:E = 核心 ①(`day_hurst(Close)`)+ N = N-甲(时点领先滞后)。理由:两个位的机制(路径形状 / 时点领先滞后)互不重叠,都不是现有 head 的改写;E 的核心从未有过不含 `day_kurt` 的外围,N 的对象与唯一的时点 head 相隔一层(差而非水平)。备选搭配:E = 核心 ②(`day_centroid(Amt)`)+ N = N-乙。
顺便:**「3 轮里至少 1 个 N 位通过审计」这条已经满足**(r1 的 b 位 N 通过且有种子),本轮两个位的类型不受这条约束。

---

## 5. 文献题目(给文献员,4 个;只要 2023-08-08 之前发表的,每条注年份)

**L1 —— 对准第 0 节的判决:股票「已实现方差时间序列的形状」在截面上怎么用,取高阶矩之前先不先归一化?**
文献里把个股**已实现方差 / 波动率的时间序列**本身的形状(vol-of-vol、RV 的时序偏度、过去一段里**最大的那个波动日**)当截面预测变量时,**具体做了哪些处理**:是先取 log(RV) 或除以自己的滚动均值再算高阶矩,还是直接在原始 RV 上算?有没有文献明确指出**未归一化的三阶矩在截面上几乎等价于「窗口内最大值」或「波动水平」**?另外:「过去一个季度最大的单日波动」作为独立变量,在控制了波动水平之后还有没有预测力?低波动 / 低 idiosyncratic-vol 异象的**多头腿**在 A 股的表现(只要样本结束于 2023-08 之前的研究)?
EN:`volatility of volatility cross-section of stock returns`;`realized variance time-series skewness predictor`;`vol-of-vol anomaly idiosyncratic`;`maximum daily volatility cross-section`;`log realized variance normalization higher moments`;`low volatility anomaly long leg China A-share`;`extreme value statistics of realized variance`
ZH:`波动率的波动率 截面收益`;`已实现方差 时序偏度 因子`;`最大单日波动 截面预测`;`对数已实现方差 归一化 高阶矩`;`低波动异象 多头 A 股`;`个股波动率的极值统计`

**L2 —— 对准核心 ② 与 N-甲:成交的日内时点(重心、U 型、尾盘集中)当截面因子,以及它与价格移动时点的领先滞后。**
文献里有没有把**日内成交量 / 成交额的时间重心**(center of mass / volume-weighted time、尾盘或收盘集合竞价占比、U 型的偏斜)当成个股**截面**预测变量?用的是什么归一化(占比 vs 时间加权平均 vs 分位),怎么处理极薄股票把重心钉在开盘 / 收盘那一端(截尾?分桶?剔除?)。另一半:**成交时点与价格移动时点的领先滞后**(量先价后 vs 价先量后)有没有被度量过、怎么度量;中国 2018 年引入收盘集合竞价之后尾盘成交结构的研究。
EN:`intraday volume timing cross-section of returns`;`volume center of mass intraday distribution`;`closing auction volume share stock returns China`;`intraday U-shape skewness volume`;`lead-lag between volume and price intraday`;`trade timing informed trading intraday`;`late-day volume concentration returns`
ZH:`日内成交时点 截面因子`;`成交量时间重心 日内分布`;`收盘集合竞价 成交占比 A 股`;`日内 U 型 成交量 偏斜`;`量价领先滞后 日内`;`尾盘成交集中 收益`

**L3 —— 对准核心 ①:日内价格路径形状(R/S、Hurst、方差比)作为个股特征,而不是市场有效性检验工具。**
把**日内价格路径**的形状统计量(R/S 重标极差、Hurst 指数、方差比、路径效率)用作个股**特征**(而不是检验市场有效性)的文献有哪些;特别是:这些统计量在**薄交易**下的系统性偏误(「一天只跳一档」会被读成强趋势)文献里怎么处理 —— 按成交密度分组、按成交量时间抽样,还是剔除?把 R/S 算在**价格水平**上(而不是收益上)是否有先例、读出来的是什么?短窗口(约 241 点)估计 Hurst 的噪声有多大(r1 的文献员已找到一条警告,这次要的是**处理办法**)。
EN:`intraday Hurst exponent stock characteristic cross-section`;`rescaled range analysis intraday prices`;`variance ratio thin trading bias correction`;`price delay measure thin trading adjustment`;`business-time sampling intraday path statistics`;`short sample bias Hurst estimation high frequency`;`intraday price path efficiency stock selection`
ZH:`日内 Hurst 指数 个股特征`;`重标极差 R/S 日内价格`;`方差比 稀疏交易 偏误 修正`;`成交量时间抽样 日内路径`;`短样本 Hurst 估计偏误`;`日内价格路径效率 选股`

**L4 —— 对准 N-乙与第 3.3 节的判决:零收益分钟对高阶矩的贡献 —— 「个数」与「排列」之分。**
文献在用日内高阶矩(峰度、已实现四阶矩、跳跃测度)时,区分过「**有多少分钟没有成交**」和「**这些不成交的分钟是怎么排列的**(最长静止段、停顿的游程结构)」吗?有没有研究报告过:把无成交分钟剔掉之后,同一个矩统计量的截面预测力会**大幅下降**(而排序只小幅改变)—— 也就是说预测力来自零质量本身?游程 / 静止段长度类的流动性度量(相对于零收益**比例**)在截面上有没有独立的预测力?
EN:`zero return minutes higher moments contamination`;`run length of zero returns liquidity measure`;`longest flat run intraday illiquidity`;`realized kurtosis excluding non-trading minutes`;`trade-time versus calendar-time moments stock returns`;`zero-return proportion versus duration liquidity proxy`
ZH:`零收益分钟 高阶矩 污染`;`静止段 游程 长度 流动性度量`;`剔除无成交分钟 已实现峰度`;`成交时间 与 钟表时间 矩统计量`;`零收益比例 与 持续时间 流动性代理`

---

## 6. 建议写进 notebook 的可检验预测(供第 3 轮核对)

1. **R A1/A2**(`ts_skew(log(DW(Open)),50)`、自归一化版)score **< 0.5**(押 0.0–0.4);**R A4**(`cross_mean(pow_3(DW(Open)),50)`)score **≥ 1.1** 且与 head 2 的 ρ ≥ 0.6。若反过来(A1/A2 ≥ 1.1),第 0 节全盘推翻。
2. 相关度表里 `ts_skew(day_durbin_watson(Open), 50)` 与波动控制的 |ρ| ∈ **0.55–0.85**;`day_durbin_watson(Open)` 与波动控制 **0.85–0.97**。
3. **R C 组**至少一条(显式的 15 日尾部统计量)≥ 0.65;能否到 0.75 的替换线,押**不能**。
4. **R D12**(`cs_winsor(neg(day_centroid(Amt)))`)score ∈ **0.2–0.7**,明显低于 0.86 —— 1%/99% 截尾切不掉一整个十分位的垃圾带。
5. E 位(若用 `day_hurst(Close)`)产出 head 概率 **40%**;若产出,最可能是**按活跃度或未复权价位分桶**的版本,与 `day_kurt(Ret)` 的 |ρ| < 0.4;`c05_no_core` 的拒绝计数仍会在 1500–2500,`periphery_seen` 仍为 0。
6. N 位(若用 N-甲)产出 head 概率 **35%**;与 head 5 的 |ρ| < 0.3。最可能的失败原因:两个重心之差在 20 日平均之后只剩噪声(r1 的 `cross_mean(day_autocorr(in_logchg(Vwap,1),5),20)` 就是这样,与所有 head 和控制 |ρ| ≤ 0.07)。
7. 第 3 轮的共性表会进一步被我们自己的 E 位污染:本轮 E 核心的子树会以 n_with ≥ 40 的规模出现在共性表顶部。**不要把它读成独立发现。**
