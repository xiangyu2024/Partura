# 结构解剖:种子 805,B 组,第 2 轮

快照 = `c05s805M1_I0_open_search`、`c05s805M2_I0_open_search`、`c05s805Br1a_Ea`、`c05s805Br1b_Nb`。
heads 9 个,存档已评分候选 303 个,本轮拆解付费 26 次(上限 48),R 候选 0 个,已生效的 R 替换 0 个。
读过:`r2/loc.md` / `r2/loc.json`、`r1/analysis.md` / `r1/lit.md` / `r1/missions.yaml` / `r1/loc.*`、`notebook.md`、PLAN.md,
以及 `partura/ops_ext.py`、`scripts/c05_locate.py`、`scripts/idea_search.py`、`alphacube/operators/{dt_day,nd_ts,nd_cs}.py`。

各次运行的规模(用 303 − 64 − 82 − 69 推出 M2):M1 = 64 评分 / 0 过线;M2 = 88 评分 / 4 heads;r1a(E)= 82 评分 / 23 过线 / 4 heads;r1b(N)= 69 评分 / 2 过线 / 1 head。

## 0. 三句话结论

1. **库里 9 个 head 只有三条轴。**(A)日内成交时点 × 日内波动时点的**条件化**(4 个 head,最好 +1.55);
   (B)**价格水平 / 股本口径**那条静态轴(5 个 head:M2 的 4 个 + E 的 1 个),里面所有 `day_*` 算子都是**常量**;(C)分钟级收益-成交量相关(1 个 head,+0.53,本轮未拆解)。
2. **最可信的一条结论来自两个互不相同的写法给出同一个方向:尾盘集中的成交是坏的。** head1 做多平滑后 centroid **低**的名字(sign −1,+1.55);
   head2 把 centroid **最高**的 20% 直接排除掉(+0.43 的净增量)。这比任何单个 head 都硬。
3. **本轮最重要的那一列数字不在 `loc.md` 里。** `rho_known`(与已知族 `cross_mean(day_std(Amt), 30)` 的相关)只印在 `loc.json`,
   而它恰好决定了为什么 R 候选是空的、为什么 A 轴只能活在一个很窄的窗口带里。见 §1.1。

## 1. 读表之前必须知道的三件事

### 1.1 `rho_known` 只在 `loc.json`,而它是本轮的决定性一列

拆解的每一行都带 `rho_known`,`loc.md` 的表格没有印。关键的几个:

| 表达式 | score | `rho_known` | 判定 |
|---|---|---|---|
| `day_centroid(Volume)` | −0.0868 | −0.195 | 干净,但不赚钱 |
| `cross_mean(day_centroid(Volume), 20)` | **+1.244** | **−0.5123** | **\|ρ\| ≥ 0.5,作为候选不合格** |
| `cs_bucket_zscore(cross_mean(day_centroid(Volume), 10), day_centroid(Ret))` | +1.5214 | −0.3874 | 合格 |
| `cs_bucket_zscore(cross_mean(day_centroid(Volume), 40), day_centroid(Ret))` | +1.2490 | **−0.5489** | **不合格** |
| `sub(day_centroid(Volume), day_centroid(Ret))` | +0.884 | −0.1042 | 很干净 |
| `cross_mean(sub(day_centroid(Volume), day_centroid(Ret)), 20)` | +0.8257 | −0.268 | 干净 |

两条推论:

- **R 候选为空不是因为没有更好的变体,而是因为唯一更好的那个不合格。** `scripts/c05_locate.py:294-299` 要求
  `score ≥ head + 0.1` **且** `abs(rho_known) < 0.5` **且** `rho_head ≥ 0.5`。
  head4 `cross_mean(sub(day_centroid(Volume), day_centroid(Ret)), 20)`(+0.826)的 knockout 变体 `cross_mean(day_centroid(Volume), 20)` 得 +1.244(必要性 **−0.4183**,即去掉那个 `sub` 分数反而涨 0.42),
  但它的 `rho_known` = −0.5123,被第二个条件挡掉。**PI 不要把这个变体写进 R:它一定不会替换。**
- **A 轴整条活在已知族的边界上,而 \|ρ_known\| 随平滑窗口单调变大。** 窗口 10 → −0.387,窗口 40 → −0.549。
  也就是说这条轴能合格的窗口带很窄(大约 ≤ 30 天),而分数的主体来自平滑(必要性 +0.8334)。
  机制上说得通:20 日平均的「成交发生在日内什么时候」和 30 日平均的「日内成交额离散度」都是**平滑后的日内成交形状**,共享的变异本来就多。

### 1.2 共性表已经被本组自己的 r1a 污染,不能再当成跨运行的对照

共性的基线是**全部 303 个候选的混合档**(`mean_without` 全部落在 −0.62 ~ −0.97 这一带)。
r1a 往存档里一次性加进 82 个候选、其中 23 个过线,M1 的非 centroid 候选平均约 −2。于是**任何主要出现在 r1a 里的子树都会白拿一个很大的 effect**。

最明显的例子:核心卡 4、5 是 `cross_mean(day_flat_ratio(Close), 20)`(effect **+1.87**,p 0.0005,4 个候选)和 `day_flat_ratio(Close)`(+1.78,7 个)。
查 r1a 的 top-5 就能看到这 4 个候选长什么样:

- `cs_bucket_zscore(cross_mean(day_centroid(Volume), 20), cross_mean(day_flat_ratio(Close), 20))` = +1.401
- `cross_mean(sub(day_centroid(Volume), pow_3(cs_bucket_rank(day_centroid(Volume), cross_mean(day_flat_ratio(Close), 20)))), 20)` = +1.416

`day_flat_ratio(Close)` 在这里是**分桶变量**,信号是 centroid。它的 +1.87 几乎全部是从 centroid 那边继承来的。
**这两张卡是本轮共性表最大的陷阱,不该据此开 E 位。**(B0 组按机械卡顺序会在用完前三张之后正好撞上它们 —— 不是我能干预的事,但记在这里。)

反向的自检同样说明问题:`day_centroid(Volume)` 本身的 effect 从第 1 轮的 **+2.011** 掉到本轮的 **+0.283**(97 个候选,`mean_with` −0.50)。
信息含量没变,变的是「含它」那一组的成分 —— r1a 往里塞进了几十个含核心但极差的候选。**r1 关于「+2.01 测的是不崩塌、不是赚钱」的判断,被这件事直接证实了。**

另外注意 `cs_mean(day_distinct_ratio(Close))`(卡 15,effect +1.02,p 0.017):`cs_mean` 是**横截面均值并广播回每只股票**(`alphacube/operators/nd_cs.py:107`),
它在横截面上是常量,单独当因子 `distinct` 过不了 0.5 的门槛。**这张卡不能当 E 的核心。**

### 1.3 E 位大约四分之一的预算花在「不含核心的退回树」上

`day_centroid(Volume)` 出现在 97 个候选里,M1 贡献 36 个(第 1 轮的数),M2 几乎不贡献(M2 里的 centroid 都是 `day_centroid(High)`),
所以 r1a 的 82 个候选里只有约 61 个含核心 —— **约 21 个(≈ 26%)是 PLAN 修订 1 说的那种「连续拒绝后退回的最小树」**(冒烟测试里是 2/16,实战里差了一倍)。
采样计数也对得上:`c05_no_core` 737 次、`c05_periphery_seen` 只有 7 次 —— **咬人的是「核心被改掉」,不是 novelty 规则**。

**对本轮的直接含义:核心越大、节点越多,`has_core`(节点 key 相等)越难满足,退回树越多。本轮应当选小核心。**

## 2. alpha 的来源

### 2.1 A 轴(真来源):成交时点 × 波动时点,而且必须是**非线性条件化**

`day_centroid(x)`(`partura/ops_ext.py:155`)= |x| 沿分钟轴的重心 / (T−1),∈ [0, 1],0 = 全在开盘、1 = 全在收盘。
用在 `Volume` 上是「今天的成交发生在日内什么时候」,用在 `Ret` 上是「今天的**波动**发生在日内什么时候」(`day_centroid` 取 |x|)。

**充分性的完整阶梯**(全部是本轮付费评估,同一个奖励):

| 表达式 | score | train | valid | `rho_known` |
|---|---|---|---|---|
| `day_centroid(Volume)`(裸核) | −0.0868 | −0.0868 | +0.5359 | −0.195 |
| `day_centroid(Ret)`(裸,单独当因子) | **−1.3836** | −1.3836 | −0.4808 | +0.148 |
| `cs_bucket_zscore(day_centroid(Volume), day_centroid(Ret))` | +0.715 | +0.715 | +1.5672 | −0.133 |
| `cross_mean(day_centroid(Volume), 20)` | +1.244 | +1.244 | +1.7217 | −0.5123 |
| `cs_bucket_zscore(cross_mean(day_centroid(Volume), 20), day_centroid(Ret))`(head1) | **+1.5484** | +1.5484 | +2.1126 | — |
| `sub(day_centroid(Volume), day_centroid(Ret))` | +0.884 | +0.884 | +1.0484 | −0.1042 |
| `cross_mean(sub(day_centroid(Volume), day_centroid(Ret)), 20)`(head4) | +0.8257 | +0.8257 | +1.2402 | −0.268 |

四件事从这张表里读出来:

1. **水平不是来源,条件化才是。** 裸核 −0.087(r1 预测 1 写的是 [−0.1, +0.2],**命中**)。
   只加一层 `cs_bucket_zscore(·, day_centroid(Ret))`,分数从 −0.087 跳到 **+0.715**(+0.80)。这是整轮最大的单步增益,而且不花平滑、不花换手。
2. **平滑是第二大来源,但它把因子推向已知族。** `cross_mean(·, 20)` 的必要性 **+0.8334**;代价是 `rho_known` 从 −0.195 升到 −0.5123(§1.1)。
3. **处理同一个混淆(波动时点)的三种写法,效果排序是:非线性分桶(+1.55)> 什么都不做(+1.24,不合格)> 线性相减(+0.83)。**
   这是本轮最可操作的一条:**在这个环境里,把一个日内形状量条件化在另一个日内形状量上,分桶比相减好,而且好得多。**
4. **敏感性很稳。** 字段 `Volume → Amt`:1.5484 → 1.4956(head2 上 0.9097 → 0.8695);
   窗口 `cross_mean@20 → 10 / 40`:1.5214 / 1.2490;`sub` 版的窗口 10 / 20 / 40 = 0.838 / 0.826 / 0.827(几乎不动)。
   不是一个靠单一窗口撑着的结构。

**方向上的交叉验证(本轮最硬的一条)。** head1 是 `sign = −1` 作用在平滑后的 centroid 上 ⇒ **做多成交偏早盘的名字**。
head2 `cs_last_high20(LogFloatShares, day_centroid(Volume))` 是 `sign = +1`,按 `_lexi(y, x, 0.8, 1.0, -1.0)`(`ops_ext.py:375`)把 `day_centroid(Volume)` **最高的 20% 推到书底** ⇒ **排除成交偏尾盘的名字**。
两个写法共享的只有「尾盘成交不好」这一句话,其余部分(信号侧、平滑、分桶 vs 排除)完全不同。

**这条轴是真来源还是代理?** 分三块答:

- **不是流动性 / 波动 / 反转 / 市值的代数改写**:五个控制都是水平量或收益量,`day_centroid` 是无量纲时点量(r1 §2.4 已论证,本轮不变)。
- **平滑之后有一半是已知族**(|ρ| 0.51 ~ 0.55)。所以「+1.244」这个数不能当成新信息;**让它变成新信息的是 `day_centroid(Ret)` 那层分桶**(把 |ρ| 压回 0.39 ~ 0.46 的同时还加了 +0.30)。
- **r1 列的四条代理通道,本轮有三条被侧面否掉**:救活它的分桶变量不是 `LogFloatCap`、不是 30 日成交额、不是冻结报价频率
  (这三个都在 r1a 的 16 个种子里,一个都没进 heads、也没进 top-5),而是 GP 自己找到的**日内波动时点**。
  按 r1 预测 4 的第一条,「按市值 / 流动性分桶后仍 ≈ 0 ⇒ 不是规模 / 流动性代理」,**成立**。
  通道 3(停牌 / 锁板人工痕迹)只能算**未排除**:按 `cross_mean(day_flat_ratio(Close), 20)` 分桶给到 +1.401(没塌,但也不是最好的),而 §2.4 会说明 `day_flat_ratio(Close)` 本身就是宇宙掩码的那个变量。

**结论:A 轴是本种子目前唯一有「充分性 + 必要性 + 敏感性 + 两种独立写法方向一致」四重证据的来源。
真正的来源不是 `day_centroid(Volume)` 的水平,而是「成交时点相对波动时点的位置」,并且只有非线性条件化能把它从已知族里分出来。**

### 2.2 B 轴(代理):5 个 head 是同一条静态价格 / 股本轴,里面的 `day_*` 算子全是常量

这是本轮最大的发现,也是最容易在表格上看漏的一处。两个退化事实先摆出来:

**(i) `day_pos_ratio(High)` 恒等于 1.0。**
`day_pos_ratio(x)`(`ops_ext.py:98`)= 有限分钟里 `x > 0` 的占比。`High` 是分钟最高价,恒为正;无成交的分钟按前值填充而不是留 NaN
(`day_zero_ratio` 的注释把「无成交」归到 `Ret == 0`,`ops_ext.py:277`),所以每个有限分钟都 > 0 ⇒ 占比恒为 1。
**数据证据**:把 `sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares)` 砍成 `sub(day_pos_ratio(High), LogFloatShares)`,
必要性 = **−0.0000**,valid 从 2.197472 变成 2.1975(同一个数)。`c − L` 和 `c − 2L` 只有在 c 恒定时才秩等价。
共性表里 `c − L`(53 个)、`c − 2L`(28 个)、`c − 3L`(4 个)是同一本书的三种写法,effect 分别 +1.31 / +1.19 / +1.26。

**(ii) `ts_argmax(·, 1)` 恒定,外层的 `cs_last_low20(·, 常量)` 是空操作。**
拆解里 `ts_argmax(day_first(abs_(sub(-1, Open))), 1)` 的充分性行 `gate: false`、`distinct: 0.0003`(`loc.md` 写成「门槛废品」)。
`_lexi` 的 band 由**整个 tie block** 决定(`ops_ext.py:326`):常量 ⇒ `lo = 1/n`、`hi = 1.0`,`hi ≤ 0.2` 不成立 ⇒ band 全空 ⇒ 输出 = `_pct_rank(y)`,是 y 的保序重标度。
必要性实测 **+0.019**;`Open → Close` 的敏感性行 score 0.8419、valid 2.1975,与原 head **逐位相同**。
(0.8036 → 0.84194 之间那 +0.038 的差来自 `hl = 5` 时 EMA 与秩变换不可交换 —— 正好 < 0.1,
**r1 §5.2 留的那条自检「砍掉一个保序外层如果动了 0.1 以上就说明 z-rank 推理有漏洞」因此通过**。)

**(iii) 把常量代掉之后,M2 的 4 个 head 剩下什么。**
`abs_(sub(-1, Open))` = `Open + 1`,`abs_(sub(-2, abs_(sub(-1, Open))))` = `Open + 3`(都是价格的保序函数);`day_first(High)` = 首分钟最高价 ≈ 开盘价水平。于是:

| head | score | 去掉常量之后的真实含义 |
|---|---|---|
| `cs_last_low20(cs_last_low20(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), day_first(High)), ts_argmax(day_first(abs_(sub(-1, Open))), 1))` | +0.842 | rank(−LogFloatShares),最便宜的 20%(按首分钟价)被 band 标出,外层是空操作 |
| `cs_last_low20(cs_last_low20(sub(sub(day_pos_ratio(High), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(High)), ts_argmax(day_first(abs_(sub(-1, Open))), 1))` | +0.811 | rank(−开盘价),同一个 band,外层是空操作 |
| `cs_bucket_demean(sub(ts_argmax(day_first(abs_(sub(-1, Open))), 1), LogFloatShares), ts_argmax(day_first(High), 1))` | +0.643 | −LogFloatShares,**在 10 个按列序切出来的任意分组里**去均值(见下) |
| `cs_last_low20(sub(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), LogFloatShares), ts_argmax(sub(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), LogFloatShares), 20))` | +0.582 | rank(−LogFloatShares),band 变量是「20 日内 LogFloatShares 何时见底」,股本几乎不变 ⇒ 弱 band / 近空操作 |

`cs_bucket_demean(y, 常量)` 更糟:`_buckets` 用 `_pct_rank`,而 `_pct_rank` 对并列值给**序数秩**(`argsort(argsort(stable))`),
所以常量会被均匀铺进 1..10 号桶 —— 桶是按**股票在面板里的列序**切的任意分组(本地核对:100 个相同值 → 每桶恰好 10 个)。
head6 等于「在 10 个毫无意义的固定分组里把 −LogFloatShares 去均值」。**这是库里最差的一个结构。**

**(iv) `sign = −1` 把「排除筛选」变成了「只在被排除的那 20% 里面做多」。**
`_lexi(y, x, -1.0, 0.2, -1.0)`(`cs_last_low20`)把 band 里的名字记成 `rank(y) − 1 ∈ (−1, 0]`,其余是 `rank(y) ∈ (0, 1]`。
奖励按 train 自选方向;挑到 `sign = −1` 时,整本十分位纯多头书**全部落在 band 里面**。
head3 的多头书 = 「按首分钟价最便宜的 20% 之中,股本最大的那些」;head5 = 「同一个 20% 之中,价格最高的那些」(即价格的第 10 ~ 20 百分位带)。
**这是一个算子语义陷阱:`cs_last_*` 是按「排除」设计的,配上自选方向之后变成了「只交易被标记的那一段」。** head2 是 `sign = +1`,那里它才真的是排除。

**(v) 这条轴为什么能活过中性化。** 控制里有 `LogFloatCap`,没有价格。
`LogFloatShares = LogFloatCap − log(价格)`,所以对 `LogFloatCap` 做**线性**投影之后,`LogFloatShares` 残下来的就是 **−log(价格)**。
head3 / head6 / head7 做多高 `LogFloatShares` ⇒ 做多低价;head5 直接做多低价;head2 也是做多高 `LogFloatShares`。
**五个 head 的方向一致,全部指向「最便宜的那个角落」。**

**判定:B 轴是代理。** 它是一个静态的价格水平 / 股本口径因子,加上一个把选股域塌缩到最便宜 20% 的构造性 band;
其中每一个 `day_*` 算子都是常量或价格水平,**没有用到任何分钟信息**。
它在 A 股可能是一条真实的异象(低价效应),但对本实验它有三个坏性质:
(a) 它占了 9 个 head 里的 5 个,库的集中度被严重高估 —— PLAN §3 的去重是 `ρ ≥ 0.7 或 ρ ≤ −0.5`,这 5 个方向相同、hl 与 band 不同,很可能**部分留下来**,等权融合时这一条轴被重复加权;
(b) M 自己的骨架禁令看不见它:`c − L`、`c − 2L`、`c − 3L` 骨架各不相同,所以「用日内算子洗出一个常量」是 C04 那个「改写绕过禁令」的新变种;
(c) 在这个核心上开 E 位只会重新发现价格。

**唯一例外是 head2。** `cs_last_high20(LogFloatShares, day_centroid(Volume))` = +0.9097,而同一条轴不带筛选的版本
(`sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares)`,hl 20,充分性行)= **+0.4826**。
**那层「排除尾盘成交最重的 20%」带来约 +0.43** —— 这是日内信息在 B 轴上的真实贡献,也是 §2.1 那条方向结论的第二个独立证据。

### 2.3 C 轴(最独立、证据最薄):分钟级收益-成交量相关

唯一的 head 是 r1b(N 位)的 `cross_mean(cross_mean(cross_mean(day_corr(Ret, Volume), 20), 3), 20)` = +0.5322(train 0.532 / valid 0.962,sign +1,hl 5)。
`day_corr(Ret, Volume)` = 当天分钟收益与分钟成交量的皮尔逊相关 —— 「大单的分钟是在涨还是在跌」。

- 共性:`cross_mean(day_corr(Ret, Volume), 20)` effect **+1.027**,p 0.038,8 个候选;`day_corr(Ret, Volume)` +0.748,p 0.080,11 个;双层 `cross_mean` 版 +0.921,p 0.136,5 个。(这几行主要来自 r1b,r1b 只有 2 个过线,基线污染比 §1.2 那两张卡轻。)
- 充分性:r1b 的 top-5 给出同族数字 —— 双层 `cross_mean` 版 +0.457,`day_corr(Ret, Amt)` 版 +0.442,`cross_sum` 版 +0.395。
  **单层 `cross_mean(day_corr(Ret, Volume), 20)` 自己从来没被评过分。**
- 必要性 / 敏感性:**完全没有**。`c05_locate.py` 每轮只拆尚未拆过的 score 最高的 4 个,本轮拆的是 +1.55 / +0.91 / +0.84 / +0.83,head8 排第 8。
  第 3 轮会轮到它,**但本轮 E / N 一旦产出更高的 head,它会被再次挤出去**。

**判定:C 轴是本库里和两条已知轴构造上最远的一条,也是唯一「不是日内形状时点、不是静态价格」的信息。
它的弱点是只靠堆平滑(三层 `cross_mean`,有效约 40 天)才勉强过线 +0.53,而且中间那层 `cross_mean(·, 3)` 几乎没有作用(双层版 0.457,三层版 0.532)。
把 §2.1 学到的「非线性条件化」搬到这条轴上,是本轮期望收益最高的一步。**

### 2.4 明确**不是**来源的东西

| 结构 | 证据 | 读法 |
|---|---|---|
| `cross_zscore(day_centroid(Volume), 20)` | 共性 effect **−4.25**,5 个候选 `mean_with` **−4.8789**,p 0.9999(**全表最差一行**) | 「相对自身历史的异常」在这个核心上是毁灭性的,不是中性的 |
| `day_signed_ratio(Ret, Amt)` | 共性 effect −2.80,4 个候选 `mean_with` −3.4582,p 0.99 | 净买压代理裸用 / 轻包装会彻底反向 |
| `day_centroid(High)` | 共性 effect −1.58,10 个候选 `mean_with` −2.2248;`cs_last_low10(day_centroid(High), ListAge)` −2.13 | `day_centroid` 作用在**价格**字段上近乎退化(价格逐分钟几乎不变 ⇒ 重心恒≈0.5),这是一条好的阴性对照 |
| `day_centroid(Ret)` 单独当因子 | 充分性 **−1.3836** | 它是**条件变量**,不是信号。分桶时值 +0.30,单独用时 −1.38 |
| `day_flat_ratio(Close)` | 共性 +1.78 / +1.87(§1.2 已证明是继承来的) | 而且它**几乎就是宇宙掩码那个变量**:掩码是 `frozen = cross_max(day_zero_ratio(Ret), 15)` 的最差 20%(`c05_locate.py:94,102`),而 `day_flat_ratio(Close)`(Close 与前一分钟相等的占比)与 `day_zero_ratio(Ret)` 定义上等价。拿它当信号 = 交易掩码剩下的 80% 里面的冻结报价梯度,属于 r1 §2.4 通道 3 的人工痕迹 |
| `pow_3` 折叠 | `sub(day_centroid(Volume), pow_3(day_centroid(Volume)))` 在 [0,1] 上**非单调**(峰在 0.577),所以不是保序空操作;但实测没有用:`cs_bucket_zscore(cross_mean(sub(...), 20), day_centroid(Ret))` = 1.517 vs 不折叠的 1.548;head9(多一层平滑)只有 0.529;共性 `cross_mean(sub(...), 20)` effect 仅 **+0.038** vs `cross_mean(day_centroid(Volume), 20)` 的 +0.563 | 一个不保序但也不带信息的折叠 |

## 3. 烂部件(必要性 ≤ 0,或换掉反而更好)

按「适合做 R」的程度排:

1. **`day_pos_ratio(High)` —— 恒定 1.0,所以 `sub(day_pos_ratio(High), X)` 就是 `−X`。**
   必要性实测:多砍一层 `sub(·, LogFloatShares)` = **−0.0000**。出现在 head3、head5、head7(以及 70 个候选里的 52+)。
2. **`ts_argmax(·, 1)` —— 恒定(`gate: false`,`distinct: 0.0003`),它外面那层 `cs_last_low20` 整个是空操作。**
   必要性 **+0.019**;`Open → Close` 敏感性与原 head 逐位相同。出现在 head3、head5、head6。
3. **`cs_bucket_demean(·, 常量)` —— 按面板列序切出来的 10 个任意分组。** head6(+0.643)整个结构就是这个。
   它不只是没用,是**让因子取决于股票在面板里的列顺序**。
4. **head4 里的 `sub(·, day_centroid(Ret))` —— 必要性 −0.4183(去掉涨 0.42)。**
   但替换变体 `cross_mean(day_centroid(Volume), 20)` 的 `rho_known` = −0.5123,**按 §2.5 的替换规则一定被拒**。
   这是一个「按分数是烂部件、按合格性是承重墙」的部件。**不要为它花 R。**
5. **head8 里的 `cross_mean(·, 3)` —— 近乎无效。** 双层 0.457 / 三层 0.532,差 0.075;三层嵌套的有效平滑约 40 天,中间那个 3 日层只是噪声。
6. **head9 里重复的 `cross_mean(·, 20)` 层。** r1a 已经给出去掉它的数字:1.517 vs head9 的 0.529。
   **但不要为它花 R**:那个变体与 head1(1.548)是近孪生,最终库 §3 的 `ρ ≥ 0.7` 去重会把它收掉,替换掉 head9 等于白花一次评估、库里还少一个 head。
7. 保序外层(非负输入上的 `pow_1_5` / `pow_2_5` / `sqrt` / `log` / `cs_rank` …):r1 §3.2 的清单继续有效。
   本轮的证据是共性里它们的 `mean_with` 全在 0 附近(`pow_1_5` +0.079,`pow_2_5` +0.024,`pow_3` −0.033),而同期 `day_centroid(Volume)` 整体 −0.50。

## 4. 之前的任务,和 r1 预测的对账

### 4.1 E 位 `c05s805Br1a_Ea`(核心 `day_centroid(Volume)`)

82 评分 / 23 过线 / 4 heads,最好 +1.5484。采样计数 `c05_no_core` 737、`c05_periphery_seen` 7。
**和 M 自己的两批比:M1 = 64 评分 / 0 过线,M2 = 88 评分 / 4 heads(最好 +0.84)。E 位用更少的评估拿到同样多的 head、分数高一倍。**

试过的外围(可见部分)与结果:
- **B 类 非线性条件化:全胜。** 4 个 head 里 3 个用 `cs_bucket_zscore` / `cs_last_high20`;top-5 里 4 个是 `cs_bucket_*`。
- **A 类 自身时序偏离:全败,而且是全表最差。** `cross_zscore(day_centroid(Volume), 20)` 的 5 个候选平均 **−4.88**。
- **C 类 交互:败。** `day_signed_ratio(Ret, Amt)` 的 4 个候选平均 −3.46;`cross_corr` / `cs_flip_by_state` 的种子一个都没进 top-5。
- **GP 自己加的那一层:`day_centroid(Ret)` 作为分桶变量。** 这个变量**不在 r1 写的 16 个种子里的任何一个**。

### 4.2 N 位 `c05s805Br1b_Nb`(日内形状统计量铺开)

69 评分 / 2 过线 / 1 head。过线的只有量价相关这一支,而且要三层平滑。
`day_at_max_ratio` / `day_at_min_ratio` / `day_distinct_ratio` / `day_gini` / `day_skew` / `day_topw_mean` / `day_wmean(Ret, in_index(Ret))` / `day_corr(Close, Volume)` 全部没过线。

### 4.3 r1 的 5 条预测逐条打分

| # | 预测 | 实测 | 判定 |
|---|---|---|---|
| 1 | 裸核 score 落在 [−0.1, +0.2] | **−0.0868** | **对** |
| 2 | `pow_*` 族与裸核差 < 0.05、秩相关 > 0.99 | 没有被直接评分(共性里 `mean_with` +0.08 / +0.02,方向一致但不是检验) | **无法核对** |
| 3 | A 类(偏离)与 B 类(分桶)外围的 score 都明显高于纯保序外围 | B 类**大胜**;A 类 **−4.88**,比保序外围(≈0)差了将近 5 个夏普 | **一半对,而且错的那一半是重点** |
| 4 | 按市值 / 流动性分桶后仍 ≈ 0 ⇒ 不是代理;按 `day_flat_ratio` 分桶后塌掉 ⇒ 人工痕迹 | 市值 / 流动性 / 冻结三个分桶变量的种子一个都没进 heads 或 top-5(⇒ 不是这三者的代理,**对**);按 `cross_mean(day_flat_ratio(Close), 20)` 分桶 **没塌**(+1.401)⇒ 不能判为人工痕迹,但也不是最优 | **对(第一条);第二条未触发** |
| 5 | 拒绝计数不会集中在少数几个外围类上 | `c05_no_core` 737 vs `c05_periphery_seen` 7:novelty 规则几乎没咬到;但它担心的「退化成同一外围换窗口」**部分发生了**(top-5 里 1.548@20 与 1.521@10 只差窗口) | **字面对,担心的事半发生** |

**r1 笔记(notebook §「本轮各任务的事先预测」)里最关键的两条,一条对一条错:**
- 「若有 head,方向为**负**(晚盘成交之后跑输)」—— **对**,而且被 head1 / head2 两种写法交叉验证。
- 「**不会**来自 B 类;B 类的种子 score 与 0 相差不超过 0.15:分桶不会把这个属性救活」—— **彻底错**。
  分桶把裸核从 −0.087 抬到 **+0.715**(+0.80,是预测区间的 5 倍以上),而且全部 4 个 head 都是 B 类。
- 细看之下,错得有结构:r1 猜的三个**分桶变量**(`LogFloatCap`、30 日成交额、冻结报价频率)大概确实都没用;
  有用的那个(`day_centroid(Ret)`,日内波动时点)是 GP 自己找到的。
  **即「Partura 给对了算子类(B 类 `cs_bucket_*`),GP 给对了变量」—— 和 C04 的 C2a(Partura 给构造、GP 给方向)是同一种分工。这一条值得写进 notebook。**

## 5. 本轮候选

### 5.1 值得深挖的核心(按推荐顺序,≤ 3)

「已见外围」= `scripts/idea_search.py:312` 的 `periphery(t)`(核心之外的算子**名字集合**,重数相减之后还剩的名字),
`SEEN` 从快照全部存档建一次、运行中不增长,空集预置。**我只看得到 heads + 各 mission 的 top-5 + 共性表,所以下面每一行都是下界。**

#### 核心 1(首选)`cross_mean(day_corr(Ret, Volume), 20)`

- **凭什么**:共性 effect +1.027,p 0.038,8 个候选;这条轴有 1 个 head(+0.532);**和两条已知轴构造上最远**;本轮没被拆解,家族控制只有 1 个 head。
- **已见外围(来自 r1b)**:`{cross_mean}`(`cross_mean(cross_mean(core, 20), 20)`、`...(core,20),3)`、`...(core,3),20)`)、`{cross_mean, cross_sum}`(`cross_mean(cross_sum(core, 15), 20)`)。
  **其余几乎全新**,特别是整个 `cs_bucket_*` / `cs_last_*` / `cross_corr` / `cs_flip_by_state` 家族一次都没在它周围出现过。
- **假设**:这条轴目前靠堆平滑勉强过线;§2.1 证明在这个环境里「日内形状量 + 非线性横截面条件化」能加 +0.3 ~ +0.8。
  把条件化搬过来应当能把 0.53 推到 0.8 以上,而且不增加换手。
- **核心大小**:3 个节点,`has_core` 容易满足(§1.3)。**核心配额:0 / 2 已用。**

#### 核心 2 `sub(day_centroid(Volume), day_centroid(Ret))`

- **凭什么**:充分性 +0.884(高于它所在的 head 0.826),`rho_known` 仅 **−0.1042**(整轮最干净的一个有分数的结构);
  窗口敏感性 0.838 / 0.826 / 0.827 几乎不动;字段换 Amt 后 0.828。核心卡 2。
- **已见外围**:`{cross_mean}`(head4,也是 r1 的种子之一)。**其它全部未见。**
- **假设**:§2.1 第 3 条说「同一个混淆,分桶 > 什么都不做 > 相减」。核心固定成**相减**版之后,E 要找的是
  **在相减之上再条件化 / 再分段**的写法(例如把差值在波动时点或集中度的桶里再标准化、按市场状态翻转、与 `day_corr(in_index(Volume), Volume)` 交互)。
  它比核心 3 干净得多(ρ_known 0.10 vs 0.51),E 不用和已知族的门槛打架。
- **顾虑**:家族控制会加入 head4(0.826),门槛不高;但核心本身就是一个**次优的实现**(相减),E 只能在它外面补救,上限可能被锁住。
- **核心配额:0 / 2 已用。**

#### 核心 3(备选)`cross_mean(day_centroid(Volume), 20)`

- **凭什么**:核心卡 1,自身 score +1.244(整轮最高的充分性数字),所在 head +1.548。
- **已见外围(至少)**:`{cs_bucket_zscore, day_centroid}`(head1)、`{cs_bucket_zscore, cross_mean, day_flat_ratio}`(r1a #5);
  共性说它出现在 11 个候选里,我能指认 2 个。
  注意**窗口是核心 key 的一部分**:`cross_mean(day_centroid(Volume), 10)` 不含这个核心,所以 1.521 那个近孪生既不在家族控制里、也不在 SEEN 里。
- **两条硬顾虑**(写清楚给 PI):
  1. **`rho_known` = −0.5123,核心本身就不合格。** E 的候选只有在外围能把 |ρ| 压回 0.5 以下时才可能成为 head。
     本轮已知能做到这件事的外围只有一类(`cs_bucket_*(·, day_centroid(Ret))`),而它**已经在 SEEN 里**。
     很可能出现「分数很高、一个都不合格」的 96 次评估。
  2. **配额的实质。** `day_centroid(Volume)` 已经用掉 1 / 2 个 E 位;`cross_mean(day_centroid(Volume), 20)` 是另一个 key,
     技术上有全新的 2 个配额,但**实质上是同一个机制的第二次深挖**。家族控制(head1,+1.548)会抵掉一部分便宜,但不能抵掉「配额被同一条轴吃掉」这件事。
     我的建议是**这一轮不用它**;如果第 3 轮核心 1 / 核心 2 都落空,再回来。

**明确不推荐的核心**:核心卡 3 `cs_last_low20(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), day_first(High))`(§2.2:价格代理,7 个节点、退回树会很多);
核心卡 4 / 5 `cross_mean(day_flat_ratio(Close), 20)` / `day_flat_ratio(Close)`(§1.2 污染 + §2.4 掩码变量);核心卡 15 `cs_mean(day_distinct_ratio(Close))`(横截面常量)。

### 5.2 R 目标(≤ 16 次直接评估;R 同时是本轮唯一的额外测量通道)

`c05_locate.py direct` 对每个变体都写出 score / train / valid / `rho_known` / `rho_head`,**不管它是否替换**。
head8(C 轴)本轮没被拆解、第 3 轮也可能被挤掉,所以 **R 是现在唯一能拿到它的必要性 / 敏感性的通道**。
下面 15 个按价值排,标注「冲替换」还是「测量」:

对 head8 `cross_mean(cross_mean(cross_mean(day_corr(Ret, Volume), 20), 3), 20)`(+0.532):
1. `cs_bucket_zscore(cross_mean(cross_mean(day_corr(Ret, Volume), 20), 20), day_centroid(Ret))` —— **冲替换**(把 A 轴学到的条件化搬过来;A 轴同一步值 +0.30 ~ +0.80)
2. `cross_mean(cross_mean(day_corr(Ret, Volume), 20), 60)` —— 冲替换 + 测量(砍掉无效的 3 日层、换长平滑;双层 20/20 已知 0.457)
3. `cross_mean(cross_mean(day_corr(abs_(Ret), Volume), 20), 20)` —— **测量**(「涨的分钟成交大」vs「波动大的分钟成交大」,这条轴最关键的语义分叉)
4. `cross_mean(cross_mean(day_corr(in_index(Volume), Volume), 20), 20)` —— **测量**(`in_index` 的注释就是「成交是否后置」;等于用相关系数重新编码 A 轴,顺便给出 centroid 的第二种写法的分数)

对 head2 `cs_last_high20(LogFloatShares, day_centroid(Volume))`(+0.9097):
5. `LogFloatShares` —— **测量,信息量最大的一次**(整层筛选去掉。预期 ≈ +0.48;若接近 +0.9,则这个 head 是纯价格代理,§2.2 (c) 那条 +0.43 的推断作废)
6. `cs_last_high20(LogFloatShares, cross_mean(day_centroid(Volume), 20))` —— **冲替换**(1 日噪声筛选 → 20 日平滑筛选)
7. `cs_last_high10(LogFloatShares, cross_mean(day_centroid(Volume), 20))` —— 冲替换(把排除带从 20% 收到 10%)
8. `cs_last_high20(LogFloatShares, cross_mean(day_sum(Amt), 30))` —— **测量(安慰剂)**(筛选变量换成流动性。若与 6 同分,说明筛选变量不重要;注意它的 `rho_known` 很可能 ≥ 0.5,不会替换,但数字仍然有用)

对 head1 `cs_bucket_zscore(cross_mean(day_centroid(Volume), 20), day_centroid(Ret))`(+1.5484):
9. `cs_bucket_zscore(cross_mean(day_centroid(Volume), 20), cross_mean(day_centroid(Ret), 20))` —— 冲替换(条件变量与信号同样平滑;现在条件变量是 1 日噪声)
10. `cs_bucket_rank(cross_mean(day_centroid(Volume), 20), day_centroid(Ret))` —— 测量(rank 条件化 vs zscore 条件化)
11. `cs_bucket_zscore(cross_mean(day_centroid(Volume), 20), day_gini(Volume))` —— **测量**(条件变量换成**集中度**而不是时点:检验「条件变量必须是时点」还是「任何日内形状都行」。这一条直接决定核心 1 / 核心 2 的 E 要不要在条件变量上铺开)

对 head3 `cs_last_low20(cs_last_low20(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), day_first(High)), ts_argmax(day_first(abs_(sub(-1, Open))), 1))`(+0.842):
12. `cs_last_low10(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), day_first(High))` —— **冲替换 + 测量**(去掉空操作外壳 **且** 把价格带 20% → 10%。按 §2.2 (iv),多头书整个落在 band 里面,收紧 band 应当变好;若反而变差,我关于 `sign = −1` 翻转的读法错了)
13. `cs_last_low20(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), LogFloatCap)` —— **测量(决定性的代理检验)**(band 变量从价格换成市值。市值已被线性中性化,所以若同分 ⇒ 这条轴只是小盘;若明显变差 ⇒ 它真的是**价格水平**这条未被控制的轴)
14. `cs_last_low20(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), cross_mean(day_flat_ratio(Close), 20))` —— 测量(band 变量换成冻结报价频率:直接检验 r1 §2.4 通道 3)

对 head4 `cross_mean(sub(day_centroid(Volume), day_centroid(Ret)), 20)`(+0.826):
15. `cross_mean(div(day_centroid(Volume), day_centroid(Ret)), 20)` —— 冲替换 + 测量(同一个错位的**比值**写法,仍然无量纲;`sub` 版 ρ_known 只有 −0.27,比值版应当同样干净)

**不要花 R 的两个**(§3 第 4、6 条):`cross_mean(day_centroid(Volume), 20)` 替 head4(`rho_known` −0.5123,一定被拒);
`cs_bucket_zscore(cross_mean(sub(day_centroid(Volume), pow_3(day_centroid(Volume))), 20), day_centroid(Ret))` 替 head9(会成功,但与 head1 近孪生,最终库去重会收掉,等于白花)。

### 5.3 N 的灵感

**主推:把「日内时点的错位」从一种编码扩成一族,并且统一套上本轮证明有效的两件处理(≥ 20 日平滑 + 横截面非线性条件化)。**

理由全部来自本轮的数据,不靠先验:(a) 唯一有四重证据的来源是「量的时点 vs 价的时点」;(b) `day_centroid` 只是这件事的一种编码,
`ops_ext.py:684` 的注释本身就给出了第二种 —— `day_corr(in_index(Volume), Volume)` =「成交是否后置」(相关系数编码,对 V 的尺度做了归一,与 centroid **不是**单调变换);
(c) 条件化的增益(+0.30 ~ +0.80)比任何换字段 / 换窗口都大,而 r1b 的 N 位一次都没用过 `cs_bucket_*`。

- 量的时点编码:`day_centroid(Volume)`、`day_corr(in_index(Volume), Volume)`、`day_argmax(Volume)`、`day_wmean(in_index(Volume), Volume)`(后者与 centroid 应当秩等价,放进来当重写等价性的探针)
- 价的时点编码:`day_centroid(Ret)`、`day_corr(in_index(Ret), abs_(Ret))`、`day_argmax(abs_(Ret))`
- 配对方式(按本轮的排序):`cs_bucket_zscore(cross_mean(量时点, 20), 价时点)` > 不配对 > `sub(量时点, 价时点)`;另加 `cs_bucket_rank`、`div`、`cross_corr(量时点, 价时点, 20)`
- 顺带两条独立轴:`day_corr(abs_(Ret), Volume)`(波动-成交量的分钟级共动,和 head8 的 `day_corr(Ret, Volume)` 是不同信息)、`day_gini(Volume)` 与 `day_gini(Ret)` 的配对(集中度版的同一个想法)
- **本轮实测出来的负面清单,必须写进 N 的任务书**:不用 `cross_zscore` / `cross_madz` 这类自身时序偏离(−4.88);不用裸或轻包装的 `day_signed_ratio(Ret, Amt)`(−3.46);
  不把 `day_centroid` 用在价格字段上(−1.58);不用 `cs_mean(·)` 当信号(横截面常量);不用 `day_flat_ratio(Close)` 当信号(掩码变量)。

**备选 N(不推荐本轮用)**:把「价格水平的非线性」做干净 —— 库里已经有 5 个 head 偶然挖到它(§2.2),而控制里没有价格。
不推荐的理由就是这一条:再加一个同轴的 head 只会加重库的集中度,PLAN §3 的去重未必能收掉。
如果 PI 想动这条轴,更好的用法是把价格当**条件变量**去净化别的信号(`cs_bucket_zscore(<日内形状>, day_first(Close))`),而不是再做一个价格因子。

## 6. 文献题目(交文献员,只用 2023-08-08 之前发表的)

四题分别对准核心 1、核心 2、§2.2 的代理判定、以及 §2.4 的那个负面结果。问的都是**文献里对类似的结构 / 特征做过哪些处理**,不是问「这个因子有没有用」。

### L1. 分钟级「收益-成交量相关」这类当日统计量,被当成股票层面的横截面特征时,文献怎么处理?(对准核心 1)

要的是处理手法清单:用原始水平还是相对自身历史;**是否按某个条件变量分组后再标准化 / 排序**(行业、规模、流动性、波动、或另一个日内统计量);
平滑多少天(1 / 5 / 20 / 60)、持有多久;有没有报告过「要堆 20 天以上的平均才有效」这类平滑敏感性;有没有换股票池 / 换市场复核过;
以及用 `|收益|` 还是带符号收益与成交量求相关的区别(即「大单在涨的分钟」vs「大单在波动大的分钟」)在文献里是否被分开讨论。
关键词:分钟级量价相关、日内量价关系、成交量-收益同期相关、量价配合、知情交易的分钟级代理、日内特征的平滑与持有期;
intraday return-volume correlation / contemporaneous volume-return relation / minute-level price-volume comovement / volume-volatility comovement /
intraday characteristic as a cross-sectional predictor / smoothing window and holding period for high-frequency characteristics / signed vs absolute return in volume-return correlation.

### L2. 「成交在日内什么时候发生」和「波动在日内什么时候发生」这两件事,文献里是怎么**配对**处理的?(对准核心 2 与 §2.1)

这是本轮唯一有四重证据的机制,而 r1 的 L1 只问到「成交时点怎么处理」,没问到「成交时点与价格 / 波动时点的相对关系」。
要的是:有没有文献把日内成交量曲线与日内波动率曲线(或日内收益曲线)放在一起比较 —— 用差、用比值、用相关、用领先滞后回归、用分组;
它们怎么归一化这两条曲线(各自除以自身全日总量、取重心 / 分位、按小时分箱);有没有「成交先于波动 / 波动先于成交」这类领先滞后的横截面结果;
以及这种配对量是否被用来识别知情交易或流动性供给。
关键词:日内成交量曲线与波动率曲线、量价日内同步性、成交领先波动、日内 U 形的量与波动对比、日内领先滞后、成交量时点与价格发现;
intraday volume curve versus volatility curve / volume-volatility intraday synchronization / lead-lag between intraday volume and volatility /
timing of volume relative to price discovery / U-shape of volume vs U-shape of volatility / normalizing intraday profiles before cross-sectional comparison.

### L3. 名义股价水平(以及「流通股数」这个口径)作为一个**独立于市值**的横截面特征,文献怎么处理?A 股的便宜股角落怎么剥?(对准 §2.2)

对准本轮最大的代理判定:库里 5 个 head 实质上都是「做多最便宜的那个角落」,而奖励只对 `LogFloatCap` 做了**线性**中性化,
`LogFloatShares = LogFloatCap − log(价格)`,所以价格水平这条轴整条活下来了。
要的是:(a) 有没有文献把低价股效应 / 名义股价作为独立于市值与账面市值比的特征检验过,用什么办法把它和规模分开(双重排序、分组内排序、对 log 价格做非线性控制、剔除最低价的若干百分位);
(b) A 股文献里怎么处理「便宜股角落」的已知污染 —— 退市风险、ST 股、壳资源 / 重组预期、涨跌停与停牌、股本结构;
(c) 有没有报告过「只在最便宜的 X% 里面做多」这种分段构造,以及它们怎么选 X 和怎么做稳健性。
关键词:低价股效应、名义股价与收益、股价水平异象、ST 股与退市风险、壳价值与重组预期、市值与股价的双重排序、流通股本口径;
nominal price level anomaly / low-priced stock effect / share price as a characteristic independent of size /
penny stock effect and delisting risk / double sorting on size and price / China A-share ST stocks and shell value / float shares versus float market cap.

### L4. 对持续性很强的日内特征,为什么「相对自身历史的异常值」版本会比「多日平均」版本差得多?文献里怎么选平滑 / 换手 / 成本处理?(对准 §2.4 的负面结果,并修正 r1 的 L3)

r1 的 L3 问的是「水平 vs 自身历史标准化,哪种更站得住」,文献员找到的证据(Gervais-Kaniel-Mingelgrin、Lee-Kim-Kim)全部指向「偏离版有效」。
**本轮实测恰好相反:`cross_zscore(day_centroid(Volume), 20)` 是全表最差的一行(5 个候选平均 −4.88),而多日平均版本是全部有效结构的共同形态。**
所以这一题要的是**反面与边界条件**:有没有文献报告过「异常 / 偏离版本在某些特征上失效或反向」;
它们把这件事归因于什么(换手与交易成本、测量噪声被标准化放大、特征本身的持续性就是定价信息、分母的标准差估计不稳、极端值);
对这类特征文献通常怎么处理成本(双边多少 bp、怎么限制换手、是否用多日平均或半衰期平滑代替偏离);以及有没有把「水平 / 均值版」与「偏离版」在同一张表里对比并报告净收益(扣成本后)的工作。
顺便问一条:带方向的成交量(订单失衡 / 收益定号成交额)作为**日频横截面**特征,有没有文献报告它失效或方向不稳(本轮 `day_signed_ratio(Ret, Amt)` 的 4 个候选平均 −3.46)。
关键词:换手率与交易成本对因子的侵蚀、特征的持续性与定价、时序标准化的失效、扣成本后的净收益、信号平滑与半衰期、订单失衡的横截面失效;
turnover and transaction costs eroding factor returns / when standardization amplifies noise / persistence of characteristics as priced information /
failure of abnormal-versus-level specifications / net-of-cost factor performance / signal smoothing and half-life / cross-sectional failure of order imbalance proxies.

## 7. 给第 3 轮核对的可检验预测

1. **R 第 12 项**(把 head3 的价格 band 从 20% 收到 10%)score **上升**;若下降,§2.2 (iv) 关于 `sign = −1` 把 band 变成选股域的读法错了。
2. **R 第 13 项**(band 变量价格 → 市值)score **明显下降**(≥ 0.15),因为市值已被线性中性化;若基本不变,那这条轴只是小盘效应,不是价格水平。
3. **R 第 5 项**(`LogFloatShares` 裸评)score 落在 **[0.40, 0.60]**;若 ≥ 0.80,head2 那 +0.43 的日内贡献不存在,§2.1 的方向交叉验证只剩 head1 一条腿。
4. **R 第 1 项**(把 `cs_bucket_zscore(·, day_centroid(Ret))` 搬到 C 轴)score ≥ **0.70**(即至少 +0.17);
   若它反而变差,说明「非线性条件化」不是一条可迁移的处理,而只是 centroid 这个特定核心的局部现象 —— 那么核心 1 的 E 位应当立刻改方向。
5. **核心 1 的 E 位**产出 ≥ 1 个 head 的概率约 **55%**,最好的 score 落在 **[0.6, 1.1]**;`c05_no_core` 的拒绝率与 r1a 同量级(≈ 90%),
   退回的无核树约占评分数的 **20% ~ 30%**(r1a 实测 ≈ 26%)。
6. **共性表在第 3 轮会继续漂移**:本轮两张「`day_flat_ratio(Close)`」卡的 effect 会随着本轮新运行的候选加进存档而**明显回落**(与 `day_centroid(Volume)` 从 +2.011 掉到 +0.283 同理)。
   如果它们没回落,说明它们确实有独立信息,§1.2 的污染判断要收回。
