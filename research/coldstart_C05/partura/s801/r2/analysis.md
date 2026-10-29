# 结构解剖:种子 801,B 组,第 2 轮

快照:`c05s801M1_I0_open_search`、`c05s801M2_I0_open_search`、`c05s801Br1a_Ea`、`c05s801Br1b_Nb`;344 个已评分候选,11 个 head,R 替换 0 个,本轮拆解付费 47 次。
本文件只用 `r2/loc.md` / `r2/loc.json`、`r2/R_prev.json`、`r1/`(analysis / lit / missions / loc)、`notebook.md`、PLAN.md,以及代码与算子源码
(`partura/ops_ext.py`、`partura/steer.py`、`partura/diagnose.py`、`partura/books.py`、`scripts/c05_locate.py`、`scripts/c05_round.py`、`scripts/c05_check.py`、`scripts/idea_search.py`、
`alphacube/operators/dt_day.py`、`dt_cross.py`、`nd_cs.py`、`alphacube/catalog.py`、`alphacube/dailyfields.py`)。没有读任何测试段数字。

---

## 0. 三句话结论

1. **11 个 head 里有 6 个的第一个参数是一个常数面板**。`day_signed_ratio(<任何恒正的价格字段>, <任何字段>) ≡ 1`,
   `cs_state_rank(·, 50)` 是逐日的市场标量;这两种东西进了 `cs_last_high*` / `cs_first_high*` 的 `y` 槽以后,只剩下 `_pct_rank` 对常数的**序号排名 = 面板的列序斜坡**。
   所以这些 head 的真实内容是「**一个 20% 尾部指示 + 一条静态列序倾斜**」,股票层面的唯一活输入是第二个参数(筛选变量)。
   定位工具自己给出了硬证据:`pow_05(day_signed_ratio(Close, Close))` 单独求值时 `distinct = 0.0003, gate = False`。
2. **真来源只有一条强的**:同组内的**相对价格水平、并在近 60 日里从未便宜过** ——
   `cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)`,**单独当因子 score +0.76**(train +0.76 / valid +1.22),
   而它里面那层分组标准化的必要性是 +2.38 / +1.90 —— **是「分组内重新标度」在挣钱,不是价格水平本身**:把它换成裸的 `cross_min(day_sum(Vwap), 60)` 直接掉到 −0.69 / −0.41。
3. **第 1 轮的 13 次 R 推翻了第 1 轮的主要假设,也推翻了我上一轮最担心的那条**:
   显式的 log 名义股价 `sub(LogFloatCap, LogFloatShares)` 得 −2.05,`log(day_last(Close))` 得 −1.13,`cs_bucket_rank(LogFloatShares, LogFloatCap)` 只有 +0.13;
   而「时间凸性 × 中性化造出夏普」的管道假象检验 `inv(pow_3(pow_3(pow_3(LogFloatCap))))` 得 **−3.31**,假象不存在。
   同时 R 还顺手量出一件关键的事:**分钟级的 `Close` 不是名义股价**(见 §1.7),所以 §0.2 那条轴到底是「同组相对价格」还是「长周期累计涨幅」还没分开 —— 这是本轮最值得花钱的一次判别。

---

## 1. alpha 的来源

### 1.1 机械事实一:`day_signed_ratio(Close, Close) ≡ 1`

`ops_ext.py:122`:

```
day_signed_ratio(x, y) = sum(|y| * sign(x)) / sum(|y|)   (按分钟,两者都有限的分钟)
```

分钟价格字段(`Close` / `Vwap` / `Open` / `High` / `Low`)恒为正,所以 `sign(x) ≡ +1`,式子化成 `sum(|y|)/sum(|y|) = 1` —— **逐股逐日恒等于 1**,与两个参数是哪个字段无关。
本地用 torch 复算过(合成面板,`Close`/`Open`/`Vwap` 三种组合全部返回 1.0)。`pow_05(1) = 1`,再包一层也还是常数。

快照里的四条独立硬证据:

| 证据 | 数值 | 只有「它是常数」能解释 |
|---|---|---|
| 单独求值 | `distinct = 0.0003`,`gate = False` | 约 1 个不同取值 / 3000 只股票 |
| 去掉 `pow_05`(knockout) | score / train / valid 与原 head **完全相同**,必要性 `−0.0` | — |
| `Close -> Vwap`(swap) | +1.4874 / +1.7535 / +1.4874,与原 head **逐位相同** | 换了字段还一模一样 |
| 两个 head 只差 `day_signed_ratio(Close, Close)` 与 `day_signed_ratio(Close, Open)` | 两者 score / train / valid **都是 1.068286 / 1.068286 / 1.762772** | 同一个面板 |

受影响的 head(Nb 的 7 个里有 6 个):score +1.49、+1.10、+1.07、+0.92、+0.69、+0.53,表达式都是
`cs_last_high20(pow_05(day_signed_ratio(Close, Close)), <筛选变量>)` 的同一个骨架。

### 1.2 机械事实二:`cs_state_rank(·, 50)` 是逐日市场标量,M2 的两个 head 同病

`ops_ext.py:547` 的 `cs_state_rank(x, d)` 先取 `x` 当日的截面均值,再取它在自己最近 d 天里的分位,然后 `expand_as` 铺回每只股票 ——
**同一天每只股票同一个数**。它的 docstring 自己写着「A per-day constant does nothing to a cross-sectional rank on its own」。

于是 M2 的 head 里 `cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))` 的 `y` 槽同样是常数。证据:
拆解里 `High -> Low` 这次 swap 的 score / train / valid 是 **+1.5294 / +1.5294 / +3.3851,与原 head 逐位相同** ——
换掉 `day_es_ratio_hi` 的输入字段结果一字不变,只有「这棵子树的输出被压平了」能解释。
也就是说 **M2 那个 +1.53 的 head 里,`day_es_ratio_hi(High)` 整条分支是装饰**,它唯一的作用是提供有效掩码。
(`Open -> Close` 的 valid 也完全相同、train 只差 0.047:241 格里第一根 bar 是 09:30 集合竞价,它的 Open 与 Close 是同一笔成交,所以 `day_first(Open) ≈ day_first(Close)`。)

M2 两个 head 的股票层面活输入因此只剩一个:**`log(day_first(Open))` = 开盘集合竞价价格的对数**。

### 1.3 常数进 `_pct_rank` 会变成「列序斜坡」:这类 head 真正在做什么

`ops_ext.py:231` 的 `_pct_rank` 用 `argsort(argsort(v, stable=True))`,是**序号排名**,并列按**列序**打破。
对一个常数面板,它返回的就是「该股票在当日有效股票里按列号数的位次 / 有效只数」—— 一条**几乎静态的、每只股票一个固定数**的斜坡,值域 (0, 1]。本地复算确认。

`cs_last_high20(y, x) = _lexi(y, x, 0.8, 1.0, −1.0) = rank(y) − 1·[x 落在最高 20% 的整并列块里]`。把 `y` 的常数斜坡记作 `ramp`:

```
raw = ramp − 1·band ,   ramp ∈ (0,1] 固定 ,  band ∈ {0,1}
```

- 半衰期 5 的 EMA(`books.py:85`,**先平滑原始值再取秩**)把 `band` 变成「最近若干日里待在 band 内的比例」,所以信号是连续的;
- `ramp` 的幅度(跨度 1)和 `band` 的位移(正好 1)**同量级**;
- 长期在 band 内的名字 `raw ∈ (−1, 0)`,长期在外的 `raw ∈ (0, 1]`,所以 **band 成员整体排在非成员下面**,组内次序由列号决定;
- 这些 head 的 `sign = −1`,信号翻转后多头十分位 = **band 成员里列号最靠前的那一半**。

**结论:`cs_last_high20(<常数>, X)` 是这个环境里表达「X 的 20% 尾部指示」的最便宜的合法写法。**
纯指示变量(`is_gt0(sub(cs_rank(X), 0.8))` 一类)只有 2 个不同取值,过不了 `distinct ≥ 0.5` 的门;
常数的序号排名**正好供给了门所要求的区分度**。代价是搭车进来一条没人控制的静态列序倾斜。
所以这 6 个 head 的经济内容是那个 20% 指示;列序斜坡是副产品,它的样本外价值未知(它是一个静态分段押注,换手极低、15bp 成本几乎不吃它,但也完全是区间依赖的)。

### 1.4 真来源 1(强):同组内相对价格水平 + 近 60 日「从未便宜过」

核心表达式(记作 **A**,是 head +1.69 与 +1.49 的真子树):

```
cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)
```

证据链:

| 项目 | 数值 |
|---|---|
| **充分性**:A 单独当因子 | **score +0.7591**(train +0.7591 / valid +1.2248),sign +1,hl 20,`rho_known −0.2371`,`distinct 1.0`,coverage 0.9993 —— **自己就过线** |
| 去掉外层 `cross_min(·, 60)` | −0.1267(train −0.1267 / valid +0.835)⇒ 外层那个滚动最小值值 **+0.89** |
| 只做一层分组(`cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)`)单独 | **−1.3947** |
| **必要性**:在 head +1.69 里把 `cs_bucket_zscore(day_sum(Vwap), cross_min(...))` 换成裸 `day_sum(Vwap)` | score −0.685,**必要性 +2.3793**(全快照最高) |
| 同一处在 head +1.49 里 | score −0.4084,**必要性 +1.8958** |
| 内层那个 `cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)` 的必要性 | 仅 +0.2064 / +0.1163 |
| 共性:`cs_bucket_zscore(day_sum(Vwap), BoardCode)` | 均值差 +1.49,p 0.002,6 个候选(含 +0.75 / 不含 −0.75) |
| 共性:`day_sum(Vwap)` | 均值差 +1.37,p 0.002,7 个候选 |

**读法:挣钱的是「把价格水平放到同组里重新标度」这一步,不是价格水平本身。** 裸价格水平(`cross_min(day_sum(Vwap), 60)`)是 −0.69 / −0.41,
两层分组标准化之后变 +1.5 ~ +1.7。这是整个快照里唯一一处必要性远超噪声的结构。

两件必须写明的机械细节(都影响怎么解释它):

1. **`cs_bucket_zscore(y, BoardCode)` 的「十分位」不是四个板块**。`_buckets` 用的是 `ceil(_pct_rank(x)*10)`,而 `_pct_rank` 是序号排名、并列按列序打破;
   `BoardCode` 只有 4 个类别(`dailyfields.py:71`,主板 / 科创 / 创业 / 北交),所以这 10 个桶是**在板块并列块内部按列号切出来的 10 个等额组**。
   主板占六成以上,它一家就铺满六个桶。所以这个算子实际是「在(板块 × 列序邻域)这个 10% 宽的局部组里做 z 分数」。
   如果 store 的 symbol 是按代码排序的(本地读不到 store,`/root/autodl-tmp/...` 在服务器上),这个「局部组」近似于「同板块、同代码段 = 同上市批次的同业」,在经济上是可解释的;
   如果不是按代码排,它就是任意切片。**这一条必须用一次 R 定下来**(把 `BoardCode` 换成一个真连续字段,比如 `LogFloatCap`,得到真正的十分位)。
2. **`day_sum(Vwap)` 不是纯价格**。`day_sum` 只对有限分钟求和,所以它 = (当日有成交的分钟数) × (平均分钟 VWAP)。
   对停牌 / 封板 / 极薄的名字分钟数会明显小于 241,`cross_min(·, 60)` 又专门去挑一个季度里**最差的那一天**,
   所以 A 也可能是一个「这个季度里有没有出现过很薄的一天」的**流动性 / 封板尾部探测器**,而控制里只有 `cross_mean(day_sum(Amt), 30)` 这种均值型流动性,扣不掉尾部。
   判别很便宜:把 `day_sum(Vwap)` 换成 `day_mean(Vwap)`(把分钟数除掉)。定位工具的 SWAP 表只换字段、不换算子,所以这一类敏感性**一次都没买过**。

### 1.5 真来源 2(弱):`day_autocorr_n1(Vwap)`,分钟 VWAP 的日内一阶自相关

共性 +0.71,p 0.003,26 个候选;`cs_bucket_zscore(day_autocorr_n1(Vwap), BoardCode)` +0.63,p 0.035,16 个候选。进了 4 个 head(+1.10 / +1.07 / +0.92 / +0.53)。
算子是正规的 Pearson 一阶自相关(`dt_day.py:302`,去均值、带 `denom < 1e-8` 守卫),在分钟价格水平序列上度量的是**日内价格路径的平滑度 / 微观噪声**(买卖价跳动读负)。

但它的证据很差:

- 充分性:`cross_min(cs_bucket_zscore(day_autocorr_n1(Vwap), cs_bucket_zscore(day_autocorr_n1(Vwap), BoardCode)), 60)` 单独 **−1.01**;
  `cs_bucket_zscore(day_autocorr_n1(Vwap), BoardCode)` 单独 **−2.34**;再外一层 **−1.62**。**没有任何一种写法单独过线。**
- 必要性在 head +1.10 里是 +1.90 / +1.22 / +0.95,但它只在「当 band 的筛选变量」这一个位置上有效。
- `Vwap -> Close` 这次 swap 把 +1.10 砍到 **+0.23** —— 对一个本该度量微观结构的量,换成分钟收盘价居然塌掉,说明它吃的是 VWAP 这个特定字段的构造细节(含量价加权),不是「自相关」这个概念。

**判为代理 / 未定**,不建议本轮做 E。它和真来源 1 还共用 `cs_bucket_zscore(·, BoardCode)` 这层壳,信息很可能重叠。

### 1.6 真来源 3(唯一一个真的「排序变量」,边际 +0.21)

`pow_05(cs_regres(day_at_min_ratio(Vwap), day_first(Volume)))` —— head +1.69 的 `y` 槽,是 11 个 head 里**唯一一个不是常数的 `y`**。
`day_at_min_ratio(x)` = 当日分钟值等于当日最低值的分钟占比(封跌停读近 1,正常日读 1/240);`cs_regres(Y, X)` 是逐日的截面回归残差;`day_first(Volume)` 是 09:30 集合竞价的成交量。
所以它是「**停在当日最低价的时间占比,扣掉开盘竞价量**」。

它值多少钱可以**直接读出来**:head +1.69 与 head +1.49 用的是**同一个筛选变量 A**,只有 `y` 槽不同(真变量 vs 常数)。

```
+1.6943 (train 1.6943 / valid 2.3308)   y = pow_05(cs_regres(day_at_min_ratio(Vwap), day_first(Volume)))
+1.4874 (train 1.7535 / valid 1.4874)   y = pow_05(day_signed_ratio(Close, Close))  <- 常数
```

**边际 +0.21**,而且方向有意思:常数版在 **train 上反而更好**(+1.7535 vs +1.6943),差别全在 valid。
所以这个变量买到的是 valid 上的稳定性,不是 train 上的拟合。+0.21 本身落在噪声带里(见 §2.0),**只能记为「可能有、量级很小」**。

`day_at_min_ratio` / `day_at_max_ratio` 这条轴在快照里几乎是空白(`day_at_max_ratio` 一次都没出现),是 N 的好料(§4.3)。

### 1.7 价格这条轴:第 1 轮 R 把它从「名义股价」改写成了别的东西

`r2/R_prev.json` 的 13 行里有三行决定性:

| 变体 | score | train | valid | distinct | rho_head | 读法 |
|---|---|---|---|---|---|---|
| `LogFloatShares` | **+0.4826** | +0.4826 | +0.7649 | 0.9804 | **+0.9991** | 裸字段 = head,四层包装确认是装饰 |
| `sub(LogFloatCap, LogFloatShares)`(= log 名义股价,恒等式) | **−2.0523** | −0.2134 | −2.0523 | **0.6869** | **−0.8644** | 和 head 同一条轴(abs(ρ) 0.86)**但反向**,而且这一侧完全不挣钱 |
| `log(day_last(Close))` | **−1.1308** | −1.1308 | −0.2926 | **0.9992** | **+0.3317** | **它根本不是名义股价** |

两条推断:

1. **「同一条轴的两侧不对称」**。head 的交易信号与 log 名义股价的相关是 −0.86,也就是说 head ≈ −log(名义股价);
   但 score 是**单边纯多头十分位**的净夏普,所以「做多低价」挣 +0.50 而「做多高价」亏 −2.05 并不矛盾 —— 一条轴只有一侧有钱。
   我上一轮预测 3(两者都 ≥ +0.40 且彼此接近)之所以错得离谱,是因为我用「残差近似相等」去推「score 近似相等」,而 score 是单边的。**这个推理错误要记住。**
2. **分钟级的 `Close` 不是名义股价(推断,未在代码里直接确认)**。两条证据:
   - `distinct`:`sub(LogFloatCap, LogFloatShares)` 是 **0.6869**(大量并列 —— 价格落在 0.01 的报价格栅上,很多股票正好同价),
     而 `log(day_last(Close))` 是 **0.9992**(几乎全不同,没有格栅痕迹);
   - `rho_head`:log 名义股价是 **−0.8644**,`log(day_last(Close))` 只有 **+0.3317**(对应 ρ(log Close, LogFloatShares) ≈ −0.33,而 ρ(log 名义股价, LogFloatShares) ≈ −0.86)。

   两个「价格」只有 0.33 量级的关系 ⇒ 分钟价格字段**多半是复权价**。
   **后果很大**:`day_sum(Vwap)`、`log(day_first(Open))`、`day_cov(Low, Open)` 全都建在分钟价格上,所以它们**不是名义股价水平**,
   而是「名义价 × 自复权基准日以来的累计复权因子」= 很大程度上的**长周期累计涨幅**。于是 §1.4 的真来源有两种竞争解释:

   | 解释 | 含义 | 判别(一次评估) |
   |---|---|---|
   | (i) 同组内相对**价格水平** | 同业里贵的、且一个季度没便宜过 | 把 A 里的 `day_sum(Vwap)` 换成 `sub(LogFloatCap, LogFloatShares)`(精确名义股价)。还得 ~+0.76 ⇒ (i) |
   | (ii) 同组内相对**长周期涨幅** | 复权价高 = 自基准以来涨得多、且季度内没回落 ⇒ 长周期动量 /「赢家」持续性(控制里只有 20 日点对点反转) | 把 `day_sum(Vwap)` 换成 `div(day_last(Close), ts_delay(day_last(Close), 250))`。得分接近 ⇒ (ii) |

   `cross_min(·, 60)` 这个「季度内的最低相对位置」在 (ii) 下读起来特别自然:它就是「距近季低点的距离」,与 52 周高点 / 近高点那一族是同一类构造。

3. 另外两条第 1 轮的结果值得记进来:`LogTotalCap` −0.6914(换同类规模字段就塌 ⇒ **不是没扣干净的非线性规模**),
   `cs_bucket_rank(LogFloatShares, LogFloatCap)` 只有 +0.1312(**市值分档内的股本秩不行**,我预测 ≥0.40 错了)。

### 1.8 M1 那条线(`inv(pow_3(pow_3(pow_3(LogFloatShares))))`)现在的地位

- 仍然是阈值噪声级的通过(+0.500147,余量 0.000147),五个秩等价写法 +0.4688 ~ +0.4831 全部不过线,裸字段 +0.4826。
- 共性表里它的指纹比上一轮更刺眼:`pow_3(LogFloatShares)` 的 `mean_with = +0.482`(28 个候选)、`pow_05(pow_3(LogFloatShares))` +0.481(12 个)、
  `pow_3(pow_3(LogFloatShares))` +0.484(10 个)…… **8 行的 `mean_with` 全落在 [+0.480, +0.484] 这个 0.004 宽的区间里**,
  只能是 x^27 的 1e32~1e38 量级在 `add`/`sub` 里把别的项全压掉、塌缩成同一本书。这一条上一轮的判断不改。
- 新的:**管道假象被证伪**。`inv(pow_3(pow_3(pow_3(LogFloatCap))))` = **−3.3134**(train −1.9038),`LogFloatCap` 裸的 = −3.0698。
  「EMA 的时间凸性 × 对控制中性化」**不会**自己造出 0.5 级的夏普。我上一轮给这条 55% 的把握,错了,而且这是个全局性的好消息:
  以后不必再怀疑这一类写法是实现产物。
- `cross_min(LogFloatShares, 60)` +0.4819 对 `cross_max(LogFloatShares, 60)` +0.4708,分差 **0.011 < 0.05** —— soft-min 故事是噪声,上一轮预测 5 对。

### 1.9 共性表的两个读数陷阱(影响怎么用它)

1. **自种子污染**。`c05_locate.py` 的共性直接读快照全部 344 个存档候选,其中 111 个来自 Br1a_Ea、88 个来自 Br1b_Nb,
   而 Ea 的 16 个种子里 7 个带 `sub(LogFloatShares, cross_min(LogFloatShares, 120))`。所以共性表里
   `sub(LogFloatShares, cross_min(LogFloatShares, 120))`(+0.78, p 0.004, n=21)、`cross_min(LogFloatShares, 120)`(+0.61, n=24)
   **一半是我们自己上一轮种进去的**,它们的 p 值不能当独立证据。真正独立的共性行是来自 M1 / M2 的那些。
2. **E 位的 score 和别的 score 不是同一个度量**。`idea_search.py:183` 对 E 任务把核心的家族(`--neutral-extra`)加进控制基,
   所以 `c05s801Br1a_Ea` 那个 +1.07 是**在 6 个控制下的增量分**,而 M / N 的 head 是 5 个控制。
   heads 表把两种分混在一列里排序,PLAN §3 的最终融合又只用 5 个控制。**E head 的「标准口径」分数目前是未知的。**

---

## 2. 烂部件(适合做 R)

### 2.0 先定噪声底:约 ±0.4

同一个 head 上把 `Vwap` 换成 `Close`(两个几乎同一个东西的分钟价格字段)会让 score 动 **−0.56**(head +1.69 → +1.13)和 **−0.38**(head +1.49 → +1.11);
`cross_min` 的窗口 60 → 120 在三个 head 上分别是 **+0.31 / −0.15 / +0.01**,方向都不一致。
**所以 0.4 以下的必要性 / 增益一律当噪声读。** 这条直接影响下面两件事。

### 2.1 确定是装饰的部件

| 部件 | 所在 head | 证据 |
|---|---|---|
| `pow_05(·)`(三处) | +1.69 / +1.49 / +1.10 | 必要性 `+0.0009` / `−0.0` / `−0.0`。`pow_(x, 0.5) = sign(x)*abs(x)^0.5` 全域单调,取秩前后不变 |
| **整个 `pow_05(day_signed_ratio(Close, Close))`** | +1.49、+1.10、+1.07、+0.92、+0.69、+0.53 | 常数(`distinct 0.0003`);换字段逐位相同;它唯一的贡献是 §1.3 的列序斜坡 |
| **整个 `day_es_ratio_hi(High)` 分支** | M2 +1.53 | `High -> Low` 逐位相同 ⇒ 输出被 `cs_state_rank` 压成逐日标量后再被 `_pct_rank` 压平 |
| M2 head 最外面两层 | M2 +1.53 | knockout 必要性 **−0.0095**(去掉**更好**:+1.5389 vs +1.5294)和 +0.0875;而内层子树 `cs_first_high40(cross_corr(...), cs_last_high10(...))` 单独就有 **+0.68**。这棵树的体积有一个数量级是白长的 |
| 内层 `cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)` | +1.69 / +1.49 | 必要性 +0.2064 / +0.1163,都在噪声底以下 ⇒ 双层嵌套里的那个内层 `cross_min` 可以去掉 |
| `day_quantile(Ret)`(减法项) | Br1a_Ea 的 3 个过线者 | 三个只差这一项的候选 score **都是 0.692157**(6 位小数全同):`cross_mean(day_sum(Volume), 20)` 是 1e7~1e9 量级,`day_quantile(Ret)` 是 1e-4,float32 下这个减法**不存在**。`log` 又在 `cs_rank` 里面,也是单调装饰 |
| `cs_bucket_zscore(day_autocorr_n1(Vwap), BoardCode)` | +1.10 | 必要性 +0.9452,但它自己单独是 −2.34,而 `Vwap -> Close` 让整个 head 掉到 +0.23 ⇒ 不稳 |

### 2.2 一个有害部件(方向可读)

`c05s801Br1a_Ea` 的过线者只差「事件项出现几次」:

```
+1.0721  add(X, add(X, mul(0.1, cs_rank(...))))     事件项 2 份、换手项 1 份 => 相对权重 0.05
+0.6922  add(X,      mul(0.1, cs_rank(...)))        事件项 1 份、换手项 1 份 => 相对权重 0.10
     其中 X = sub(LogFloatShares, cross_min(LogFloatShares, 120))
```

**把换手项的相对权重从 0.10 降到 0.05,score 从 +0.69 升到 +1.07。** 换手 / 成交量项是有害的,score 随它被稀释而上升。
推到极限就是把它完全去掉,只留 `sub(LogFloatShares, cross_min(LogFloatShares, 120))` —— 但那是个在多数股票日上恰好等于 0 的稀疏量,
可能过不了 `distinct ≥ 0.5` 的门(上一轮我就是这么判的)。**这一条值得花一次 R 去确认**:如果它能过门又能保住分,那 Ea 的 head 就该被它替换掉。

### 2.3 已经触发的那个 R 候选,建议打回

定位工具报了一个:head +1.69 的 `cross_min@60->120`,score +2.0005,增益 +0.3063,`rho_head 0.8668`,形式上满足替换条件(≥ +0.1、ρ ≥ 0.5)。两条保留意见:

1. **+0.31 落在 §2.0 的噪声底以下**,而且同样的窗口改动在 head +1.49 上是 **−0.15**、在 head +1.10 上是 **+0.01** —— 三个 head 上方向不一致。
2. **`rho_known = −0.4959`,离不合格线 abs(ρ) ≥ 0.5 只差 0.0041。** 换成 120 日窗口把它往已知族推了(原 head 是 −0.4939);
   替换之后这个 head 在最终库里几乎贴着已知族的红线。

建议 PI 在任务文件里**明确写上要不要接受这个替换**,并记一条预测供下一轮核对。

---

## 3. 之前的任务

### 3.1 槽 a:E,核心 `LogFloatShares` —— 机制对了,押的支错了

- 评分 111,过线 7,**入 heads 1**;采样计数 `{'c05_no_core': 661, 'c05_periphery_seen': 2}`。
- 入库的 head(+1.0721,train +1.0721 / valid +1.2504,sign +1,hl 0;注意是 6 控制下的增量分,§1.9):
  `add(sub(LogFloatShares, cross_min(LogFloatShares, 120)), add(sub(LogFloatShares, cross_min(LogFloatShares, 120)), mul(0.1, cs_rank(sub(log(cross_mean(day_sum(Volume), 20)), day_quantile(Ret))))))`
- **5 个最好的过线者全部含 `sub(LogFloatShares, cross_min(LogFloatShares, 120))`,也就是「流通股扩张事件」那一支。**
- 我上一轮的预测:「最可能是『log 成交量 − 核心』这一支(换手)」—— **错**,换手那一支一个都没过;
  「扩张事件这一支产出 head 的概率 < 10%」—— **错**,它是唯一产出的那一支。两个方向都押反了。
- 但**机制判断是对的**:我上一轮写过「E 是稀疏事件唯一能走的通道 —— 候选自带连续水平项过 `distinct` 门,族中性化再把水平那本书扣掉,剩下被打分的正好是事件层的倾斜」。
  实际发生的正是这个,只是「过门的连续项」不是核心的裸水平,而是那个 `mul(0.1, cs_rank(...))` 的小换手项(而它还是有害的,§2.2)。
- **这是 C01–C05 里第一个「Partura 指挥的槽位产出了普通搜索没有的东西」的证据**:M 的两批 288 次评估里没有任何流通股事件类结构。
  这一条应该在笔记里明确记下来 —— 但别忘了 §1.9.2 的口径问题。
- 效率问题要报给 PI:**661 次 `c05_no_core` 对 111 次评分**,也就是约 86% 的采样被「子代把核心改坏」浪费掉了。叶子核心太容易被变异吞掉。

### 3.2 槽 b:N,涨跌停缩放的收益 —— 假设全败,产出却最多,原因和假设无关

- 评分 88,过线 13,**入 heads 7**(全快照 11 个 head 里的 7 个)。
- **7 个 head 和 5 个最好的过线者里,没有一个含 `LimitWidth`,也没有一个含 `Ret`。** 16 个种子里的任何一支都没有进入过线名单。
- 产出的 7 个 head 全是同一个骨架:`cs_last_high20(<常数>, <价格水平类筛选变量>)`(§1.1、§1.3)—— 一条 GP 自己找到的、与我的 idea 毫无关系的血脉。
- 我上一轮的预测:「产出 heads 概率约 40%;若有 0~2 个;最可能是缩放后的 MAX / 波动 / 上影线,score 0.5~0.7」——
  **数量错得离谱(7 个,score 到 +1.69),内容全错(一个都不是)**。
- **这是本轮最重要的一条方法教训**:N 位「成功」(7 个 head)和 N 位的 idea 之间**没有因果关系**。
  如果归因表把这 7 个 head 记在「涨跌停缩放」这个 idea 名下,下一轮就会得到一个完全错误的结论。建议 PI 在笔记里把这件事写死。
- 我上一轮写过「如果最好的是未缩放的对照,说明缩放这一步没贡献」—— 实际是**两种都没进**,这个判别没拿到答案。
  想拿到答案,正确的工具是花 3~4 次 R 式直接评估去跑那几个缩放 / 未缩放的表达式,**不是再给一个 GP 位**(GP 已经演示过它会丢掉种子)。

### 3.3 R:13 个变体 —— 买到了很好的判别证据,预测对一半

| 预测 | 结果 | 判 |
|---|---|---|
| 1. 替换触发数 = 0 | 13 行 `replaces` 全 false | 对 |
| 2. 裸 `LogFloatShares` 落在 +0.46 ~ +0.49 | +0.4826 | 对 |
| 3. log 名义股价与 `log(day_last(Close))` 都 ≥ +0.40 且彼此接近 | −2.0523 与 −1.1308 | 错(推理错误,见 §1.7.1) |
| 4. `inv(pow_3^3(LogFloatCap))` ≥ +0.3(55%) | −3.3134 | 错(管道假象被证伪,好事) |
| 5. `cross_min` 与 `cross_max` 分差 < 0.05 | 0.011 | 对 |
| 变体 4(市值分档内股本秩)≥ +0.40 | +0.1312 | 错 |
| 变体 5(`LogTotalCap`)< +0.35 | −0.6914 | 对 |
| 变体 7(`LogFloatCap` 地板)极低 | −3.0698 | 对 |
| 变体 10(自由流通比例)< +0.3 | −0.1599(valid +1.0435) | 对 |
| 变体 13(高波动条件化)不比变体 1 高 0.1 | +0.0325 | 对 |
| 6. E 位 0~2 个 head、`peripheries_seen` ≥ 6 | 1 个 head;`c05_periphery_seen` 只拒了 **2** 次 | 半对(数量对,外围约束几乎没起作用) |
| 7. N 位 0~1 个 head | 7 个 | 错 |

记分:10 条里 6 对、4 错,两个任务级预测 1 个半对、1 个全错。**系统性偏差:我高估了先验机制(预测 3、4、变体 4),低估了 GP 自己乱走的产出量(预测 7)。**

---

## 4. 本轮候选

### 4.1 值得深挖的核心(≤ 3,按推荐度)

合法性已核对:`c05_check.py:71-79` 把**快照每个 head 的每一个节点** + 共性表的 40 个子树 + 29 张核心卡全部算作合法核心。下面三个都在里面。
「已见外围」= `idea_search.py:312` 的定义 —— **核心之外算子名字的集合**;`--periphery-seen` 读的是**全部 344 个存档候选**(不只是 head),所以下表是下界。

---

**核心 1(强烈推荐):A = `cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)`**

- 是 head +1.69 与 +1.49 的真子树(合法);**单独 score +0.7591** —— 整个快照里唯一一个「自己就过线」的子树;里层分组标准化的必要性 +2.38 / +1.90。
- 族中性化会生效且很强:库里含它的 head 恰好是 +1.69 和 +1.49 两个(`c05_round.py:222` 取前 ≤6),两本书都会进控制 ⇒ **只有 A 之外的新信息拿分**。
- **已见的外围写法(只有 2 种,都是「把它塞进 `cs_last_high20` 的 x 槽当排除筛选」)**:
  - `{cs_last_high20, cs_regres, day_at_min_ratio, day_first, pow_05}`
  - `{cs_last_high20, day_signed_ratio, pow_05}`
  也就是说 **A 至今只被当成一个 20% 排除筛选用过**。完全没见过的用法:把它当连续因子去**乘 / 比 / 条件化**;把它当**别人的分组变量**(`cs_bucket_rank(Y, A)`);
  对它做**时间维度**的处理(`cross_zscore(A, 60)`、`ts_delta(A, 20)`、`cross_flat_ratio`);和收益 / 成交量做**交互**;以及用 `cs_first_high40` 反向(奖励而非排除)。
- 风险:库禁令(与 head abs(ρ) ≥ 0.7 拒绝)会把「退化成 A 本身」的子代免费毙掉 —— 这是好事(强迫新意),但 Partura 自己写的种子**必须偏离「A 单独取秩」**,否则这一位空转。

---

**核心 2(推荐,更小、更干净):B = `cs_bucket_zscore(day_sum(Vwap), BoardCode)`**

- 共性表第 2 行(均值差 +1.49,p 0.002,6 个候选),同时是 4 个 head 的节点(合法)。它就是 §1.4 里**必要性最高的那一步**:分组内重新标度。
- 族中性化更强:库里含它的 head 有 **4 个**(+1.69、+1.49、+0.92、+0.69),全部进控制。
- 它**单独很可能不过线**(最接近的 `cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)` 单独 = −1.3947),
  所以这一位的全部分数必须来自外围 —— 作为 E 位这是优点(不会靠重新发现核心混分),但 PI 要知道这一位的期望产出比核心 1 低。
- **已见外围(4 种,全部围绕同一个骨架)**:
  `{cross_min, cs_bucket_zscore, cs_last_high20, cs_regres, day_at_min_ratio, day_first, day_sum, pow_05}`、
  `{cross_min, cs_bucket_zscore, cs_last_high20, day_signed_ratio, day_sum, pow_05}`、
  `{cross_min, cs_bucket_zscore, cs_last_high20, day_autocorr_n1, day_signed_ratio, pow_05}`、
  `{cross_min, cs_bucket_zscore, cs_last_high20, day_cov, day_signed_ratio, pow_05}`。
  共同点:**外层永远是 `cross_min(…, 60)` + `cs_last_high20`**。没见过的:别的时间聚合(`cross_max` / `cross_mean` / `cross_zscore` / `cross_tail_mean_q25` / `cross_quantile_q25`)、
  不同的分组对象(把 `BoardCode` 换掉的写法在 head 里从未出现)、以及把它和收益 / 事件 / 开盘竞价量做交互。

---

**核心 3(备选):C = `log(day_first(Open))`**

- 共性 +0.66,p 0.000,**53 个候选**(正效应里样本最大的一行);是 M2 两个 head 的节点(合法)。
- 它是 M2 两个 head 里**唯一的股票层面活输入**(§1.2),也是「价格水平」这条轴最干净的写法,而且 `day_first` 落在 09:30 集合竞价那一根 bar 上 —— 它其实是**竞价价格**。
- 已见外围(1 种):`{cross_corr, cs_first_high40, cs_last_high10, cs_state_rank, day_es_ratio_hi, day_first, inv, log}` ——
  全是「常数 y + 价格筛选 + 241 日滚动相关」这一套。没见过的:当连续因子、与竞价量 `day_first(Volume)` / `day_first(Amt)` 配对、与前收盘比(竞价跳空)、分组标准化。
- 不推荐放在核心 1 / 2 前面的理由:它和核心 1 / 2 大概率是**同一条轴的另一种写法**(都是复权价格水平),
  而 PLAN §3 的最终去重会把 ρ ≥ 0.7 或 ρ ≤ −0.5 的 head 丢掉,同轴再加对主指标贡献很小。**除非 §1.7 的 (i)/(ii) 判别先做完**,否则不知道在深挖什么。
- 另外两个本来够资格、但我**不推荐**的:`day_autocorr_n1(Vwap)`(§1.5,没有任何单独过线的写法,且换字段就塌)、
  `LogFloatShares`(整个实验还剩 1 个 E 位额度,但 §1.8 说明它是阈值噪声;真正有内容的是从它长出来的 `sub(LogFloatShares, cross_min(LogFloatShares, 120))`,共性 +0.78 但被自种子污染)。

### 4.2 R 目标(排好序,共 14 个 ≤ 16)

本轮 R 的首要任务是**把 §1.7 的 (i)/(ii) 和 §1.4 的两个机械细节分开**,其次是把列序斜坡的贡献量出来。替换基本不期望触发(除了 §2.3 那个和第 14 个)。
挂的 head:1~10 挂 `cs_last_high20(pow_05(day_signed_ratio(Close, Close)), A)`(+1.4874),11~12 挂 +1.69 那个,13 挂 +1.10 那个,14 挂 Ea 的 +1.07。

**第一组 —— 这条轴到底是什么(最关键的 3 次)**
1. `cross_min(cs_bucket_zscore(sub(LogFloatCap, LogFloatShares), cross_min(cs_bucket_zscore(sub(LogFloatCap, LogFloatShares), BoardCode), 60)), 60)`
   —— A 换成**精确名义股价**。≈ +0.76 ⇒ 解释 (i);塌掉 ⇒ 不是名义价格。
2. `cross_min(cs_bucket_zscore(div(day_last(Close), ts_delay(day_last(Close), 250)), cross_min(cs_bucket_zscore(div(day_last(Close), ts_delay(day_last(Close), 250)), BoardCode), 60)), 60)`
   —— A 换成**年度累计涨幅**。≈ +0.76 ⇒ 解释 (ii) 长周期动量,整条轴改名。
3. `cross_min(cs_bucket_zscore(day_mean(Vwap), cross_min(cs_bucket_zscore(day_mean(Vwap), BoardCode), 60)), 60)`
   —— `day_sum` → `day_mean`,把「当日有成交的分钟数」除掉。塌掉 ⇒ A 其实是薄 / 封板尾部探测器(§1.4.2)。

**第二组 —— 分组是什么(2 次)**
4. `cross_min(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), LogFloatCap), 60)), 60)`
   —— `BoardCode` → `LogFloatCap`,得到**真正的十分位**(§1.4.1)。保住 ⇒「同组」是规模同业;塌掉 ⇒ 之前的「十分位」靠的是板块内按列序切片。
5. `cross_min(cs_bucket_rank(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60)`
   —— `cs_bucket_zscore` → `cs_bucket_rank`:同样的分组,但用组内秩代替 z 分数。保住 ⇒ 是「相对位置」;塌掉 ⇒ 吃的是 z 分数在厚尾水平量上的尺度。

**第三组 —— 列序斜坡值多少(2 次,§1.3)**
6. `cs_last_high20(LogFloatCap, A)` —— 排序变量换成**控制字段本身**:它的秩贡献会被中性化扣掉,剩下的就是 band 的净价值。
   ≈ +1.49 ⇒ 列序斜坡不重要,这些 head 的内容就是那个 20% 指示;明显更低 ⇒ 斜坡在贡献一条没人控制的静态倾斜,**整族 head 的样本外价值要打折**。
7. `cs_last_high20(A, A)` —— 同一个变量既当排序又当筛选(= 把 A 的秩里最高 20% 压到底部)。和 6 一起把「粗化成尾部指示」与「静态倾斜」分开。

**第四组 —— 时间聚合与 band 形状(3 次)**
8. `cs_last_high20(pow_05(day_signed_ratio(Close, Close)), cross_mean(cs_bucket_zscore(day_sum(Vwap), cross_min(cs_bucket_zscore(day_sum(Vwap), BoardCode), 60)), 60))`
   —— 外层 `cross_min` → `cross_mean`:「季度最低」是真的有信息,还是只是个平滑器?(knockout 说去掉值 +0.89,但那次把「换成均值」和「什么都不做」混在一起了)
9. 同上但外层换 `cross_max(·, 60)` —— min / max 的分差直接给出「尾部 vs 水平」的方向。
10. `cs_last_high10(pow_05(day_signed_ratio(Close, Close)), A)` —— band 宽度 20% → 10%。真的是尾部效应 ⇒ 变窄应当更强或持平。

**第五组 —— §1.6 那个唯一的真排序变量(2 次)**
11. `cs_last_high20(day_at_min_ratio(Vwap), A)` —— 去掉 `cs_regres(·, day_first(Volume))`:扣开盘竞价量这一步是否必要(当前边际 +0.21,噪声底以下)。
12. `cs_last_high20(day_at_max_ratio(Vwap), A)` —— 换成「停在当日**最高**价的时间占比」(封涨停 / 僵化报价),快照里从未出现过的方向。

**第六组 —— 另两个 head 的烂部件(2 次)**
13. `cs_last_high20(pow_05(day_signed_ratio(Close, Close)), cross_min(cs_bucket_zscore(day_std(Vwap), cs_bucket_zscore(day_std(Vwap), BoardCode)), 60))`
    —— 把 +1.10 那个 head 里的 `day_autocorr_n1(Vwap)` 换成一个解释清楚的日内离散度;`Vwap -> Close` 一换就塌(+1.10 → +0.23)说明原件不稳(§1.5)。
14. `sub(LogFloatShares, cross_min(LogFloatShares, 120))` —— **把 Ea head 里那个有害的换手项完全去掉**(§2.2)。
    先看它能不能过 `distinct ≥ 0.5` 的门;若能过且 ≥ +1.17,它应当替换掉 Ea 的 head(但注意 §1.9.2 的口径差异,PI 要决定怎么比)。

另外请 PI 处理 §2.3:定位工具已经报出的那个 `cross_min@60->120` 替换(增益 +0.31、`rho_known −0.4959`,离不合格线 0.0041)要不要接受。

### 4.3 N 的灵感(按我的偏好)

前提:库里 11 个 head 塌缩成大约**一条半轴**(§1.4 的相对价格 / 涨幅占 8 个 head,流通股扩张事件 1 个,流通股水平 1 个,VWAP 自相关与第一条纠缠)。
PLAN §3 的最终去重(ρ ≥ 0.7 或 ρ ≤ −0.5 就丢)大概会把那 7 个 Nb head 压到 1~2 个。**再加同轴的东西对主指标几乎没有价值。**

1. **09:30 集合竞价(最推荐)**。241 格的第一根 bar 就是集合竞价(`catalog.py:33` 注释:「09:30 auction + 240 bars」),
   所以 `day_first(Volume)` / `day_first(Amt)` / `day_first(Open)` 全是竞价量 / 竞价价。
   快照里只碰过两次(`log(day_first(Open))` 当价格筛选、`day_first(Volume)` 当回归的解释变量,后者恰好是唯一一个真排序变量的组件,§1.6)。
   可写的:竞价成交额占全日比 `div(day_first(Amt), day_sum(Amt))`、竞价量相对自身 20 日均值的异动、竞价价对前收盘的跳空、竞价量 × 跳空方向。
   机制上与价格水平那条轴正交,且五个控制一个都不覆盖。
2. **「停在当日极值的时间占比」这一族**。`day_at_max_ratio` / `day_at_min_ratio` / `day_flat_ratio` / `day_flat_run_max` / `day_distinct_ratio`
   (`ops_ext.py:580-620, 415`)—— 封板、僵化报价、一分钟一个价位的薄股。
   `day_at_min_ratio(Vwap)` 已经在最好的 head 里挣到 +0.21 的边际,`day_at_max_ratio` 一次都没出现过。
   **这其实就是第 1 轮那个「涨跌停」idea 想要的东西,但是用这个环境真正擅长的分钟数据去测,而不是用日收益除以 `LimitWidth`。**
3. **第 1 轮的涨跌停缩放收益:不要再给 GP 位,改成直接评估**。§3.2 已经证明 GP 会把种子丢掉;要知道
   `cross_max(div(day_sum(Ret), LimitWidth), 20)` 这一族成不成,花 3~4 次 R 式直接评估就够,比再烧 96 次评估便宜得多。
4. **自由流通比例 / 解禁存量**(`sub(LogTotalCap, LogFloatCap)`):第 1 轮 R 测过,score −0.16 但 **valid +1.0435** ——
   train 失败所以整体不行,但 valid 的表现说明这条轴不是空的。作为 N 的一个分支(和 `ListAge` 的锁定期交互)可以带,不值得独占一位。

---

## 5. 文献题目(给文献员,≤ 4)

通用要求:只用 **2023-08-08 之前**发表的文献,逐条注明年份;要的不是「这个因子有没有用」,而是**文献里对类似结构 / 特征做过哪些处理** ——
归一化、按条件分组、交互、换周期、换股票池。

**题目 1(对准核心 1 / 2,以及 §1.7 的 (i)/(ii) 判别)**
文献里怎样处理「**相对于同业的价格水平 / 累计涨幅**」这一类截面特征?具体问:
(a) 把价格水平或复权价格做成因子时,是用绝对水平、对数、全市场分位,还是**在分组内**(行业 / 板块 / 规模 / 上市批次)去均值或标准化?分组变量怎么选,分几组?
(b) 对这类水平量取**滚动极值**(例如「近一个季度 / 近 52 周里相对位置的最低点」、「距近高点的距离」)有哪些既有做法,窗口一般取多长?
(c) 文献如何区分「名义股价水平」与「复权价格水平(= 自基准以来的累计总收益)」这两件会被同一个字段混在一起的事?有没有明确讨论过用复权价当截面特征时会混进长周期动量?
中文关键词:相对价格水平、同业比较、行业内中性化、分组标准化、复权价、累计涨幅、52 周高点、近高点、长周期动量、长期反转
英文关键词:peer-relative price, industry-relative valuation, within-group standardization, group demeaning, adjusted price level, 52-week high, nearness to high, George Hwang, long-run momentum, long-term reversal, price level anomaly

**题目 2(对准 §1.3:尾部指示 / 排除式筛选,而不是单调排序)**
文献里「**只做多(或只排除)某个变量的极端一档**」这种构造是怎么做和怎么评估的?具体问:
(a) 低价股 / 彩票偏好 / 规模这类效应,文献认为是**单调**的还是只集中在**头尾一两个十分位**?有没有专门做过单调性检验或分档收益表?
(b) 把一个连续变量**粗化成哑变量 / 分档指示**之后,预测力是增强还是减弱,文献怎么解释(非线性、噪声削减、还是过拟合)?
(c) 「筛选式因子」(先用 X 排除一批股票,再在剩下的里面按 Y 排序)在文献里的标准做法和常见陷阱是什么?如何把「筛选的贡献」和「排序的贡献」分开归因?
中文关键词:分档收益、单调性检验、十分位、哑变量化、离散化、筛选、排除、条件化排序、双重排序
英文关键词:decile portfolios, monotonicity test, nonmonotonic cross-section, discretizing a continuous signal, indicator variable, screen, conditional double sort, attribution of screen vs rank

**题目 3(对准核心 2:分组内标准化这件事本身)**
文献里**组内去均值 / 组内 z 分数 / 组内秩**(我们这里的 `cs_bucket_demean` / `cs_bucket_zscore` / `cs_bucket_rank`)作为一种特征构造,有哪些既有经验?具体问:
(a) z 分数与组内秩在**厚尾的水平型变量**(价格、市值、成交额)上的差别,文献更推荐哪一种,为什么?
(b) 分组数(四分 / 五分 / 十分)和分组变量的选择对结果的影响;**分组中性化**与「对连续变量做线性回归中性化」相比,在尾部的差别有没有被量化过?
(c) 有没有「**两层嵌套分组**」(先按 X 分组标准化,再用标准化的结果当新的分组变量)的做法?如果没有,文献里最接近的替代是什么(迭代中性化 / 双重排序 / 分层抽样)?
中文关键词:组内标准化、行业内 z 分数、分组中性化、分位数变换、稳健标准化、双重排序、厚尾
英文关键词:within-group z-score, industry-demeaned, group neutralization, rank transformation vs z-score, robust standardization, winsorization, nested double sort, heavy tails in cross-sectional standardization

**题目 4(对准 N 的灵感 1 与 2:开盘集合竞价 + 停在极值的时间)**
A 股(以及有集合竞价和涨跌幅限制的其他市场)的文献里,**开盘集合竞价**和「**价格停在当日极值的时间占比**」这两类分钟级特征是怎么构造的?具体问:
(a) 竞价阶段的成交量 / 成交额占全日比例、竞价价相对前收盘的跳空、竞价量异动,被做成过哪些截面特征?窗口和归一化方式?
(b) 「封板时长 / 封板强度 / 触板后是否打开」这类指标在文献里怎么度量(时间占比、成交量占比、撤单),涨跌停封板后次日的收益结构结论是什么?
(c) 「价格长时间不动」(僵化报价、低流动性)与「价格封在涨跌停」这两件事,文献用什么办法区分开?有没有用「日内不同价位数 / 最长不变 run」这一类度量?
中文关键词:集合竞价、开盘竞价量、跳空、封板时长、封板强度、炸板、涨跌停、僵化报价、日内价位数、流动性枯竭
英文关键词:opening call auction, auction volume share, opening gap, limit-up lock duration, limit hit and reopen, magnet effect, price limits China, stale quotes, zero-return days, intraday price levels visited

---

## 6. 写给下一轮核对的预测

1. **R 第一组是本轮的分水岭。** 我押 **解释 (ii)(长周期涨幅)** 多于 (i):
   - 变体 1(精确名义股价)score **< +0.3**(把握 65%);
   - 变体 2(年度累计涨幅)score **≥ +0.4**(把握 55%);
   - 变体 3(`day_mean` 换 `day_sum`)score **≥ +0.5**,即分钟数那条通道**不是**主因(把握 60%)。
2. 变体 4(`BoardCode` → `LogFloatCap`,真十分位)score **≥ +0.5**(把握 60%):分组标准化这一步是真的,不是靠列序切片。
   若它反而塌到 0 以下,说明 §1.4.1 的担心成立,这整族 head 要重新定性。
3. 变体 6(`cs_last_high20(LogFloatCap, A)`)score **≥ +1.0**(把握 55%):20% 尾部指示本身撑住大部分,列序斜坡的贡献 **< 0.5**。
4. 变体 9(外层 `cross_max` 代替 `cross_min`)比变体 8(`cross_mean`)**低**(把握 60%):「季度内从未便宜过」确实比「季度内最贵过」更对。
5. 变体 14(`sub(LogFloatShares, cross_min(LogFloatShares, 120))` 单独)**过不了 `distinct ≥ 0.5` 的门**(把握 60%);若过了门,score 落在 **+0.3 ~ +0.9**。
6. 变体 12(`day_at_max_ratio`)不优于变体 11(`day_at_min_ratio`)(把握 60%)。
7. 本轮替换触发数:**1 个**(§2.3 那个窗口变体,如果 PI 接受),其余 0 个。
8. E 位(核心 A 或 B,族中性化开启):过线 head **0 ~ 2 个**;`c05_no_core` 的拒绝数仍会在**评分数的 5 倍以上**(§3.1 的 661/111),
   `c05_periphery_seen` 的拒绝数 **< 10**(外围约束在这个搜索空间里几乎不咬人)。
9. 若这一轮仍放一个 N 位:它产出的 head **有一半以上与 idea 无关**(把握 70%)—— 这是 §3.2 的直接外推。
   想让 N 位的产出可归因,唯一的办法是把 idea 本身用直接评估先测一遍。
10. 下一轮(第 3 轮)的 heads 表里,**`cs_last_high*(<常数>, ·)` 这个骨架还会再出现至少 1 个新 head**(把握 65%):
    `distinct ≥ 0.5` 的门在奖励里是硬的,而常数的序号排名是绕过它最便宜的路,GP 会反复找到它。
    如果 PI 想让这件事停下来,能做的只有在 E / N 的种子里给出不依赖这个技巧的替代写法(Partura 不能给 M 下禁令)。
