# 结构解剖:种子 806,B 组,第 2 轮

读入:`r2/loc.md` / `r2/loc.json`(快照 = `c05s806M1_I0_open_search`、`c05s806M2_I0_open_search`、`c05s806Br1a_Ea`、`c05s806Br1b_Nb`;
293 个已评分存档候选,9 个 head,拆解 28 次付费评估,R 候选 2 个,之前任务 2 个);`r1/analysis.md`、`r1/lit.md`、`r1/missions.yaml`、`notebook.md`;`PLAN.md`;
算子与打分源码(`partura/ops_ext.py`、`partura/steer.py`、`partura/books.py`、`partura/diagnose.py`、`alphacube/operators/*`、`alphacube/catalog.py`、`scripts/c05_round.py`、`scripts/idea_search.py`)。

> **先说结论。**
> 1. M 第 2 批把局面彻底改了:第 1 批 0 个 head、全负分,第 2 批约 67 个候选出了 **8 个 head**,最好的 score +1.78(train +2.05 / valid +1.78)。
> 2. 但这 8 个 head 里**至少 5 个的来源是同一件事:奖励只去掉控制变量的「线性」投影,而 GP 找到了把控制变量本身做成「非线性再编码」的写法。**
>    `sqrt` 是 `sqrt(|x|)`(折叠),`cs_last_low40 / cs_first_low20` 只看 `rank(y)` 与 `x` 的并列块(分段),
>    `cs_mask_top_replace_mean_neg` 把最低 10% 整块搬到高分位(错位)。折叠 / 分段 / 错位出来的量与 z-rank 下的线性控制正交,所以能拿满分。
>    本机模拟:头 1 那个结构中性化后的十分位书有 **82% 落在被筛掉的「低成交额 40%」里、平均市值分位 0.22**;头 5 的书有 **89% 是被搬走的那个「最低 10% 流动性」块**。
> 3. 真正尺度不变、与市值 / 价格水平 / 流动性无关、而且有付费证据支撑的来源只有 **两个**:
>    **`ts_quantile_q50(day_centroid(Amt), 20)`**(日内成交的时间重心,20 日中位数;自身 +1.21、必要性 +1.73、换字段与窗口加倍都稳)
>    和 **`day_kurt(Ret)`**(第 1 轮本组 N 位的产出,+0.97)。
> 4. **本轮共性表的前 20 行基本不能当证据用**:20 行的 `mean_without` 全落在 −1.05 ~ −1.19 这 0.14 宽的带子里,这是「不含它的那一堆 = 另外三次运行」的签名,
>    测到的「均值差」主要是「这个子树来自 M 第 2 批」,不是「这个子树有用」。能用的是 28 次付费拆解。
> 5. 第 1 轮的两条判断里,PI 的「代理主导」对了(去量纲的种子大幅变差),解剖员 §6 第 1 条(去量纲更好)**错了**;
>    解剖员 §1.3 第 2 点那条推论(「静态风格暴露在这个奖励下结构上过不了 0.5」)**被 M 第 2 批直接推翻**。

---

## 0. 本轮证据的质量:两条必须先说的话

### 0.1 共性表被「运行混合」污染了,前 20 行不是证据

存档 293 个 = M1 85 个(第 1 轮已知)+ E 位 73 个 + N 位 68 个 + **M2 约 67 个**(293 − 85 − 73 − 68,推算)。
四次运行的分数水平差得极远:M1 全负(0 个 head),E 位最好 +0.006(0 个过线),N 位 2 个过线,M2 出了 8 个 head。

`loc.json` 的小 n 行给出了全档均值:n = 4 的行 `mean_without` 在 −1.047 ~ −1.061,所以**全档均值 ≈ −1.05**。于是:

- 任何**只出现在 M2 里**的子树,它的「均值差」≈ `mean(M2 的那几个候选) − (−1.05)`,自动得到 +1.1 以上。
- 事实正是这样:`loc.md` 前 20 行的 `mean_without` 依次是 −1.121 / −1.061 / −1.060 / −1.082 / −1.186 / −1.095 / −1.062 / −1.069 / −1.107 /
  −1.056 / −1.064 / −1.079 / −1.068 / −1.103 / −1.060 / −1.064 / −1.052 / −1.049 / −1.047 / −1.064 —— **20 行挤在 0.14 宽的区间里**。
  若这些子树真有不同的贡献,它们的对照组不会这么整齐。整齐说明对照组其实是同一个东西:另外三次运行。
- Mann–Whitney 的 p 在此之上再加一层高估(第 1 轮 §0 已说过:存档是一条血统的后代,不是独立抽样)。

**另一处更硬的污染:上一轮 E 位的核心会把它自己的共性读反。**
`day_cov(Vwap, Ret)` 这一行现在是 **effect −0.792、n = 72、p 0.9997**(`mean_with` −1.637 / `mean_without` −0.845)。
E 位强制每个候选都含核心,所以 E 的 73 个候选几乎全部进了 `n_with`,这一行测的是「E 位这次运行好不好」,不是「这个子树好不好」。
同理 `div(day_cov(Vwap, Ret), day_mean(Vwap))`(−3.136,n = 4)和 `day_mean(Vwap)`(−2.531,n = 10)读的是 E 位的手写种子,不是「除以价格水平有害」的一般结论。

> **给 PI 的操作结论**:第 2、3 轮不要用共性表挑核心。可信的证据是 **28 次付费拆解**(同一个 head 内部的对照,运行固定)。
> 共性表只剩一个合法用途:**读出「某个核心周围已经见过哪些外围」**(这正是 `--periphery-seen` 用的那份存档)。

### 0.2 打分口径的三条机械事实(后面所有判断都建在这上面)

从源码读出来,不依赖任何新评估:

1. **中性化只去掉线性投影。** `partura/steer.py: neutral_basis` 把 `[1, z-rank(liq), z-rank(vol), z-rank(rev), z-rank(pool), z-rank(LogFloatCap)]`
   做 QR 得到正交基,`neutral_residual` 减掉信号 z-rank 在这个基上的投影。于是:
   - 控制变量的任何**严格单调**变换 → z-rank 逐位相同 → 被完全去掉;
   - 控制变量的任何**折叠 / 分段 / 错位**变换 → 与线性项正交 → **完整留下**,而且因为它是「控制变量本身的另一种写法」,它的换手极低、15bp 成本几乎不付。
2. **顺序是:原始值 → EMA(半衰期) → z-rank → 去投影 → × 方向 → 取残差前 10% 等权纯多头书,15bp/边。**
   (`steer.py` 的 `reward` 循环;`books.py: TOP_FRAC = 0.10`、`COST = 0.0015`。)方向与半衰期在 **train** 上按 `long_sharpe` 最优选出,score = min(train, valid)。
   注意 EMA 作用在**原始值**上,所以 hl > 0 时单调变换不是严格的恒等。
3. **控制里没有「价格水平」。** 控制的是市值 `LogFloatCap`(= 价格 × 股本),不是股价。所以任何以名义股价为截面主轴的因子都是干净的、未被控制的暴露。

再加三条算子事实:

- `sqrt(x) = torch.sqrt(torch.abs(x))`(`operators/common.py:206`)—— **不是单调变换,是绕零折叠**。只有当参数可能为负时它才改变排序。
- `cs_last_low40(y, x) = rank_pct(y) − 1·[x 的整个并列块落在最低 40%]`,`cs_first_low20(y, x) = rank_pct(y) + 1·[x 落在最低 20%]`
  (`partura/ops_ext.py: _lexi`)。**只用到 `rank(y)` 和 `x` 的并列块**,所以**两个参数的任何严格单调变换都是逐位恒等**。
- `cs_mask_top_replace_mean_neg(x)` 把每行**最低 10%** 换成该行**均值**(`nd_cs.py:240`,negate-flip-negate),并列按平均秩处理(`diagnose.py: rank_rows`,ties averaged)。
  重尾分布的均值位于上尾:本机模拟(4000 只,lognormal)`mean(Amt^2.5)` 落在 **92 分位**、`mean(Close^2.5)` 落在 **82 分位**(e = 1 时分别是 74 / 65 分位)。
  所以这个算子是**把最低 10% 整块搬到 80~92 分位**,`pow_2_5` 决定搬到哪里。

---

## 1. alpha 的来源

### 1.1 9 个 head 折算成 4 个来源家族

| 家族 | head(score) | 截面主轴 | 判定 |
|---|---|---|---|
| **F1 折叠的市值秩**(按一个「水平」筛子折) | `sqrt(cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile_q75(Amt)), 3))` +1.78;`sqrt(cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile(Low)), 3))` +1.13 | 市值秩在筛子处折叠 | **代理**(市值 × 流动性 / 股价的非线性再编码),但是**定位工具里最强的结构** |
| **F2 名义股价的分段**(最低 20% 推到顶) | `cs_first_low20(day_quantile_q75(Amt), log(day_open(Open)))` +1.40;`cs_first_low20(cs_normalize(day_open(Open)), cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Close))))` +1.32;`cs_first_low20(cs_normalize(day_open(Open)), cs_normalize(day_open(Open)))` +0.81 | 名义股价(低价股),组内按流动性或股价细排 | **未被控制的真暴露**,但是一个**风格**,不是日内信息 |
| **F3 流动性最低一档的错位** | `cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Amt)))` +1.18 | 日内成交额最低 10% | **纯代理**:中性化后书里 89% 就是那一块 |
| **F4 尺度不变的日内形状** | `sqrt(ts_quantile_q50(day_centroid(Amt), 20))` +1.22;`cs_mask_top_replace_mean_neg(ts_quantile_q50(cs_mask_top_replace_mean_neg(ts_quantile_q50(ts_quantile_q50(day_centroid(Amt), 10), 10)), 10))` +0.82;`day_kurt(Ret)` +0.97 | 成交在一天里的时间重心;分钟收益的峰度 | **真来源**(两个) |

### 1.2 F1:`sqrt(cs_last_low40(LogFloatCap, ·))` 是「在筛子处折叠的市值秩」

把头 1 逐层写开(`c` = `cs_last_low40(LogFloatCap, day_quantile_q75(Amt))`):

```
c = rank_pct(LogFloatCap) − 1·[day_quantile_q75(Amt) 在最低 40%]        ∈ (−1, 1]
sqrt(|c|) = { rank_pct(cap)        ,  成交额高的 60%(越大越靠前)
            { 1 − rank_pct(cap)    ,  成交额低的 40%(越小越靠前)   然后开方(保序)
```

即**一个 V 形**:在「高成交额」一侧按市值从大到小排,在「低成交额」一侧按市值从小到大排,两侧的最高分都接近 1。
付费证据完全对得上这个读法:

- **充分性**:内层 `cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile_q75(Amt)), 3)` 单独 **−2.08**,
  `cs_last_low40(LogFloatCap, day_quantile_q75(Amt))` 单独 **−2.08** —— 不折叠就是大幅亏;
  套上 `sqrt` 变成 **+1.78**。**来源就在折叠本身**,不在被折叠的那个秩里。
- **必要性**:去掉 `cs_last_low40` → `sqrt(cross_quantile_q25(LogFloatCap, 3))` = **−3.01**(必要性 +4.80)。单纯的市值(单调量)被控制去干净了,只剩成本。
- **敏感性**:`Amt → Volume` 让 score 从 +1.78 掉到 **−0.03**(train 还有 +1.33,valid 塌成 −0.03)。
  `day_quantile_q75(Amt)` ≈ 价格 × 分钟成交量,换成 `Volume` 就抽掉了价格成分 —— 说明**筛子里起作用的是「钱」而不是「股数」**,与 F2 的股价主轴是同一件事的另一面。
- 头 6 用 `day_quantile(Low)`(分钟最低价的中位数 = 股价水平)当筛子也拿到 +1.13;共性表里还有 `cs_last_low40(LogFloatCap, day_quantile(Vwap))`(n = 5)。
  **同一个折叠结构换三种「水平」筛子都站得住**,这是这个家族最强的证据。

**本机模拟(纯 numpy,不碰数据库、不花评估次数)**:4000 只股票,市值 / 30 日流动性 / 当日成交额分位按现实相关度生成,
对 `sqrt(|rank(cap) − 1·[低成交额 40%]|)` 的 z-rank 去掉 `[1, z-rank(liq30), z-rank(cap)]` 的投影,取残差前 10%:

| | 被筛掉(低成交额 40%)的占比 | 平均市值分位 | 平均 \|市值分位 − 0.5\| |
|---|---|---|---|
| 残差前 10%(书) | **0.82** | **0.22** | **0.46** |
| 全市场 | 0.40 | 0.50 | 0.25 |

**读法:这本书是一个极端的「小市值 × 低日内成交额」组合,而它之所以能活下来,正因为中性化只去线性项。**
它是不是 alpha?按经济含义它是**流动性 / 规模溢价的条件版**(「在最不流动的那 40% 里买最小的」),文献里有名字(条件化的 size–illiquidity 交互);
按本实验的口径它是**最强的结构**(R 之后 +2.11,train +2.11 / valid +2.39 两段都强、换手极低)。
我的判定:**它是「代理」,但是一个口径上合法、样本内两段都稳的代理**;它的风险不在统计上,而在最终因子库融合时会和 F2、F3 高度重叠(§4.4)。

### 1.3 F2:名义股价是这个奖励下唯一「干净且未被控制」的风格

- 头 2 `cs_first_low20(day_quantile_q75(Amt), log(day_open(Open)))`:`rank(日内成交额) + 1·[开盘价在最低 20%]`。
  `log` 作用在 `x` 参数上,而 `_lexi` 只用 `x` 的并列块 → **`log` 是逐位恒等**。付费证据:去掉它 score 完全不变(+1.396 / valid +3.152,必要性 −0.00)。
  中性化之后留下的就是那个 +1 的分段指示量 → **书 = 最便宜的 20% 里成交额最高的那些**。
- 头 9 `cs_first_low20(cs_normalize(day_open(Open)), cs_normalize(day_open(Open)))`:`y` 与 `x` 是同一个量 →
  `rank(股价) + 1·[股价最低 20%]`,**纯股价折在 20 分位处**。score +0.81。
- 头 3 多了一层真有用的东西:`x = cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Close)))` 把**最便宜的 10% 搬到 82 分位**(§0.2 模拟),
  于是 `cs_first_low20` 的那条「最低 20%」带子变成**原始股价的第 10 ~ 30 分位**,即「便宜,但不是最便宜」。
  付费证据:去掉这个外层 → score 从 +1.32 掉到 **+0.87**(必要性 **+0.45**)。**这是整个快照里唯一一个「必要性为正、而且不是单纯折叠」的部件。**
  经济上也讲得通:A 股最低价的那一档混着 ST / 退市风险 / 一字板,剔掉它能提高这个风格的质量。
- 字段敏感性都稳:头 2 `Amt→Volume` +1.38、`Open→Close` +1.39;头 3 `Open→Close` +1.32、`Close→Vwap` +1.29。

**判定:F2 是真暴露(股价水平不在五个控制里),但不是日内信息,是一个慢变风格。** 三个 head 互相 |ρ| < 0.7(否则库禁令会拦),
但经济上是**一个**赌注;`day_quantile_q75(Amt)` 与 `cs_normalize(day_open(Open))` 只是组内的破平局项。

这里要记一条**对第 1 轮的修正**:r1 §1.3 第 2 点推出「在这个奖励下,任何截面被静态风格 / 板块暴露主导的因子在结构上就不可能过 0.5」。
F1 与 F2 全是慢变的静态风格暴露,score 1.1 ~ 1.8、两段同号。**这条推论被推翻了。** 它当时的理由是「风格暴露的符号在两段里常常翻过来」——
2018–2021 与 2022-01~2023-08 这两段上,小市值 / 低价 / 低流动性这一簇恰好同号,所以推论的前提不成立。
(严格说 r1 §6 预测 3 写的是 `LimitWidth` / `BoardCode` 主导的候选,M 第 2 批里没出现这类候选,那条字面预测**未被检验**;但它背后的一般推论已经错了。)

### 1.4 F3:`cs_mask_top_replace_mean_neg` 单用就是「买最不流动的一档」

头 5 `cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Amt)))`,score +1.18、方向 +1。
因为 `pow_2_5` 保序且 `day_quantile_q75` 逐分钟作用,这个式子精确等于 `(day_quantile_q75(Amt))^2.5` 再做错位,
所以 `pow_2_5` 的唯一作用是**决定被搬走的那 10% 落在哪个分位**(92 分位,§0.2)。

机制:那 10% 的名字原始流动性最低(线性预测值极负),错位后的 z-rank 却接近顶部 → **残差 = 实际 − 预测 = 极正** → 它们整块占满十分位书。
模拟:残差前 10% 里 **89%** 是被搬走的那一块,它们的 30 日流动性平均分位 **0.19**。

付费对照也在:`day_quantile_q75(Amt)` 单独 **−1.19**,加上这一层错位变成 **+1.18**。两者的差 2.37 全部来自错位。
**判定:纯代理 —— 流动性溢价的一次口径穿透,不含任何新信息。** 它仍然会进最终因子库(规则如此),我只是要让 PI 知道它是什么。

### 1.5 F4:两个真来源

#### (a) `ts_quantile_q50(day_centroid(Amt), 20)` —— 日内成交的时间重心,20 日中位数 【本轮最强的真来源】

`day_centroid(x)`(`partura/ops_ext.py:155`)= `Σ t·|x_t| / Σ|x_t| / (T−1)`,在 [0, 1]:**0 = 成交全在开盘,1 = 全在收盘,0.5 = 对称**。
它是 `Amt` 的**齐次零次**量(分子分母同量纲),所以**结构上不可能是价格水平、市值或流动性的代理** —— 这是它和 F1/F2/F3 的根本区别。

付费证据(全部来自同一个 head 的 6 次拆解,运行固定,不受 §0.1 的污染):

| 证据 | 数字 | 读法 |
|---|---|---|
| 充分性 | `ts_quantile_q50(day_centroid(Amt), 20)` 单独 **+1.21**(train +1.21 / valid +1.27);所在 head +1.22 | **核心自己就是全部**,外层 `sqrt` 几乎不加东西(centroid > 0 时 `sqrt` 保序,只通过 EMA 作用在原始值上留下 0.017 的差) |
| 必要性 | 去掉 `ts_quantile_q50` → `sqrt(day_centroid(Amt))` = **−0.51**(必要性 **+1.73**,全快照最大的正必要性) | **alpha 在「持久水平」里,不在当日值里**;当日重心 `day_centroid(Amt)` 单独只有 **−0.085** |
| 敏感性(字段) | `Amt → Volume` **+1.21**(−0.01) | 与「钱还是股数」无关 → 再次确认不是价格 / 规模代理 |
| 敏感性(窗口) | 10 日 **+0.98**,20 日 **+1.22**,40 日 **+1.22** | 单调、平台化,**不是窗口挑出来的** |
| 两段 | train +1.21 / valid +1.27 | 两段几乎相等,是全部 9 个 head 里 train/valid 最对称的一个 |

方向 −1 → **书 = 重心最低的一档 = 成交集中在开盘附近的股票**。
经济含义:成交的日内时间分布是一只股票相当持久的特征(散户在开盘集中下单 / 被动与指数资金在收盘集合竞价成交),
20 日中位数把它变成一个「投资者结构」型特征。这类特征和五个控制都不同维,也和已知族 `cross_mean(day_std(Amt), 30)`(成交额波动)不同维。

旁证(弱,受 §0.1 限制):共性表里这一族占了 4 行,`day_centroid(Amt)` n = 31(全档第二多)、`ts_quantile_q50(day_centroid(Amt), 10)` n = 15;
头 8 也是这一族的嵌套写法(+0.82)。

**未检验的问题**(这正是 E 位该做的):(i) 用的是**滚动中位数**而不是均值,中位数是否必要?
(ii) 重心是否只对「低重心」一侧有效(单边)?(iii) 它和 F1/F2 那簇风格的相关有多大?(iv) 条件化(在不同流动性 / 市值档内分别排)会不会更强?

#### (b) `day_kurt(Ret)` —— 分钟收益的超额峰度 【第 1 轮本组 N 位的产出】

`day_kurt` = 分钟收益的标准化四阶矩 − 3(`operators/common.py:418`),**尺度不变**。score +0.97(train +0.97 / valid +1.54),方向 **−1**(做多**低**峰度)。
没有付费拆解(它是单算子,拆不动),但它有两条独立支撑:

1. 它是 N 位 68 个候选里过线的那一个,外围全家族跟着过线或接近过线:
   `cross_mean(day_kurt(Ret), 30)` +0.61、`cross_mean(cross_mean(day_kurt(Ret), 30), 30)` +0.46、
   `cross_mean(cross_mean(cross_ema(cross_mean(day_kurt(Ret), 20), 10), 20), 20)` +0.46 —— 整族同号同量级,不是一次抽签。
2. **平滑在这里是有害的**:裸峰度 +0.97 → 任何 `cross_mean` 平滑都掉到 0.46 ~ 0.61。注意奖励本身给它选了 hl = 20 的 EMA,
   再叠 `cross_mean` 就是双重平滑。**与 F4(a) 恰好相反**(那里 20 日中位数是必要的),这个对比本身是可用的信息:
   重心的 alpha 在「持久水平」,峰度的 alpha 在「当期值」。

**判定:真来源,但强度只有 F4(a) 的八成,而且外围空间几乎没被探过**(存档里见过的外围只有 `cross_mean` / `cross_ema` 这一类平滑)。

### 1.6 「真来源」与「代理」的分界线,写成一句可操作的话

在这个奖励下,一个结构是代理还是来源,看它**在 `Amt` / 价格 / 股本上是不是齐次零次**:

- 齐次零次(比值、相关、偏度 / 峰度、时间重心、集中度)→ 不可能被市值 / 流动性 / 价格水平解释 → **候选真来源**(F4)。
- 带量纲、或直接拿控制变量 / 价格水平当叶子,再用 `sqrt`(折叠)/ `cs_*_low*`(分段)/ `cs_mask_*`(错位)包起来 → **控制变量的非线性再编码**(F1、F3),
  或**未被控制的风格**(F2)。

这条线也解释了第 1 轮为什么全负:M 第 1 批的血统(`add(LimitWidth, day_cov(Vwap, Ret))`)既不是齐次零次,
也没找到任何折叠 / 分段 / 错位算子 —— 它只有 `add`,而 `add` 一个大常数在 z-rank 之后是**保序**的,等于什么都没做。

---

## 2. 烂部件(适合做 R 的)

### 2.1 必要性 ≤ 0,但**不能**用 R 替换的(别浪费评估次数)

| 部件 | 所在 head | 必要性 | 为什么不值得做 R |
|---|---|---|---|
| `log(·)` 外层 | `cs_first_low20(day_quantile_q75(Amt), log(day_open(Open)))` | **−0.00** | 它在 `_lexi` 的 `x` 位,只有并列块被用到 → **逐位恒等**,增益恒为 0 < 0.1,`score ≥ head + 0.1` 永远不可能满足 |
| `cs_normalize(·)` | `cs_first_low20(cs_normalize(day_open(Open)), cs_mask_top_replace_mean_neg(…))` | **−0.00** | 同理,在 `y` 位只用 `rank(y)` → 逐位恒等 |
| `sqrt(·)` | `sqrt(ts_quantile_q50(day_centroid(Amt), 20))` | 增益 **−0.017** | centroid > 0 → 保序,只通过 EMA 留下浮点级差异 |
| `Amt → Volume` | `sqrt(ts_quantile_q50(day_centroid(Volume), 20))` | 增益 −0.012 | 已付费测过,打平 |

这四条仍然是**有用的知识**:它们说明 M 的 head 里有大量**纯装饰**节点(9 个 head 里至少 4 个带恒等算子),
也说明 `skeleton_key` 禁令会被这种装饰绕开(同一个因子换个恒等外层就是新骨架)。

### 2.2 必要性 ≤ 0 且**能**用 R 替换的

| 部件 | 所在 head(score) | 变体 | 已测 score | 增益 |
|---|---|---|---|---|
| `cross_quantile_q25(·, 3)` | `sqrt(cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile_q75(Amt)), 3))` +1.78 | `sqrt(cs_last_low40(LogFloatCap, day_quantile_q75(Amt)))` | **+2.115**(train +2.115 / valid +2.392) | **+0.33** |
| 同上,只缩窗口 | 同上 | `sqrt(cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile_q75(Amt)), 2))` | +1.923 | +0.14 |

`cross_quantile(x, q, d)` 是沿交易日轴的滚动分位(`alphacube/operators/dt_cross.py:212`),`q25` + `d = 3` ≈ **近 3 日的较小值**。
它在一个几乎不变的量上取近 3 日下分位,只是把折叠后的值往下拖、还把换手抬上去。
**定位工具已经把这两个变体算出来了;重新提交 #1 就能让替换生效(+0.33,且是全快照最高的 score)。** 两个变体只提交增益大的那个(替换后原 head 不在库里,第二个就没有基准了)。

### 2.3 可疑但还没测的部件(R 的新目标)

| 部件 | 所在 head | 怀疑 | 怎么测 |
|---|---|---|---|
| `pow_2_5(·)` | 头 5 `cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Amt)))` +1.18;头 3 的 `x` 参数 | 它唯一的作用是把被错位的那 10% 送到 92(或 82)分位 —— 换成恒等会落到 74(或 65)分位 | 直接评估去掉它的版本 |
| `ts_quantile_q50(·, 20)` 用中位数 | 头 4 +1.22 | 滚动**中位数**对涨跌停 / 调仓日的异常重心是稳健的,均值不是;20 → 40 没变化说明还有加长空间 | 换 `cross_mean(·, 20)`、换窗口 60、换 `ts_quantile_q25 / q75` |
| `cs_last_low40` 的 40% 带宽 | 头 1 +1.78 | 40% 是生成器给的,不是测出来的;`ops_ext` 里有 20 / 10 / 05 的细带 | 换 `cs_last_low20 / low10` |
| 被折叠的那个日频叶子 | 头 1、头 6 | 拆解的 `swap` 只换了分钟字段(Close/Vwap/Open、High/Low、Volume/Amt),**六个日频叶子一个都没换过** | 换 `LogTotalCap` / `LogFloatShares`(去掉价格成分)/ `ListAge` —— 判决「折叠的是市值、股本还是年龄」 |
| 折叠算子本身 | 头 1 | `sqrt` = `sqrt(|·|)`;`abs_`、`pow_2` 是同一折叠的不同曲率 | 换 `abs_` / `pow_2`,看来源是不是「折叠」而不是「开方」 |

---

## 3. 之前的任务:核对第 1 轮的预测

### 3.1 位 a(E,核心 `day_cov(Vwap, Ret)`):0 产出,PI 预测对了

`c05s806Br1a_Ea`:评分 73 / 预算 96,过线 **0**,入 heads **0**;采样计数 `{'c05_no_core': 1269, 'c05_periphery_seen': 8}`。

| 第 1 轮写下的 | 结果 | 判定 |
|---|---|---|
| PI:产出 head 概率约 20%,预期 0 个 | 0 个 | **对** |
| PI:「如果有,最可能是 20 日平滑版,或嫁接种子带进来的搭便车外围」 | 最好的 4 个全是 `ts_corr(pow_2(day_cov(Vwap, Ret)), day_min(Close), 40)` 这一族(+0.006、−0.25、−0.30、−0.36)—— 嫁接带来的 `ts_corr` × `day_min(Close)`,和核心的机制无关 | **后半句对**(搭便车),前半句错(平滑版没冒头) |
| PI:大多数 E 候选 score 在 −0.6 ~ +0.3 | 最好 +0.006、第 5 名 −0.65 | **对** |
| PI 的判决性比较:不去量纲只平滑 vs 纯时点版,差 ≥ 0.2 算「代理主导」 | 共性表读到:`div(day_cov(Vwap, Ret), day_mean(Vwap))` 的 4 个候选均值 **−4.13**、含 `day_mean(Vwap)` 的 10 个均值 **−3.48**,而含 `day_cov(Vwap, Ret)` 的 72 个均值 **−1.64**、`cross_decay_linear(day_cov(Vwap, Ret), 241)` 的 5 个 −1.49 | **方向上「代理主导」成立**:去量纲的那批比不去量纲的差 1.9 ~ 2.6,远超 0.2 的判决线 |
| 解剖员 §6 预测 1:去量纲(`div` 配 `day_var(Ret)` / `day_mean(Vwap)`)的候选 score 会**高于**带 `add`/`LimitWidth` 外围的 | 去量纲 −3.5 ~ −4.1,`add(LimitWidth, day_cov(Vwap, Ret))` −0.67 | **错,而且错得很大(差约 3 个点)** |

**对「为什么去量纲会差这么多」的两个解释,我没法在不花评估的前提下分开**,两个都写下来:

1. **数值退化**:`div` 是裸 `torch.divide`(`operators/common.py` 无 eps 保护)。`day_var(Ret)` 在一字板 / 全天一个价的日子是 0 → `inf`。
   `rank_rows` 用 pandas 的秩,`inf` 会被排到最前(不是当缺失),于是十分位书**正好装满涨跌停封死的票**,valid 段大幅为负。
   支持:含 `mul(day_mean(Vwap), day_var(Ret))` 的那批最差。
2. **经济上就是反的**:`div(day_cov(Vwap, Ret), day_mean(Vwap))` ≈ `(Q/2 − Rδ)/M`,排序由当日已实现方差 `Q` 主导;
   波动控制是 20 日均值,当日方差的新息留在残差里,而它在 train 与 valid 两段的符号会翻。
   支持:这个式子分母不会为 0,却也到了 −4.13。

**两条都指向同一个操作结论:这条线到此为止,第 3 轮不要再花预算。** 若 PI 想留一次直接评估去分开它们,最便宜的一对是
`div(day_cov(Vwap, Ret), cross_mean(day_var(Ret), 20))`(分母不可能为 0)对 `div(day_cov(Vwap, Ret), day_var(Ret))`。我不建议花。

另外:**解剖员 §6 预测 4(「E 位若产出 head,大概率主要靠核心本身」)无法检验**(没有 head)。
核心深度 2 的情况下 `c05_no_core` 仍然是 1269 次(`periphery_seen` 只有 8 次)—— 说明 E 位的损耗**几乎全部来自 GP 变异 / 交叉把核心改坏**,
不是外围判重。73/96 的评分率说明这个机制是能跑的,但**核心越深,损耗越大**(GP 子代受 `max_depth = 4` 限制,种子可到 `seed_max_depth = 9`,`scripts/idea_search.py:406-410`)。

### 3.2 位 b(N,无量纲日内形状):出了 1 个 head,PI 的数量对了、品种错了

`c05s806Br1b_Nb`:评分 68,过线 **2**,入 heads **1**(`day_kurt(Ret)` +0.97;`cross_mean(day_kurt(Ret), 30)` +0.61 过线但被 |ρ| < 0.7 的互斥规则压掉)。

| 第 1 轮写下的 | 结果 | 判定 |
|---|---|---|
| PI:产出 ≥ 1 head 概率约 50%,预期 1–2 个 | 2 个过线、1 个入库 | **对** |
| PI:最可能过线的是**已实现偏度**(20 日平滑、方向负),其次量价相关 `day_corr(Vwap, Volume)`、相对符号跳跃 / 成交不平衡 | 过线的是**峰度** `day_kurt(Ret)`(方向 −1);偏度、量价相关、符号跳跃都没进前 5 | **品种错了**。「方向为负」(做多分布尾部更薄的票)这一点对了,但对的是峰度 |
| PI:`cross_mean(day_corr(Vwap, Ret), 20)`(核心的无量纲孪生)会低于 `day_cov` 血统的最好水平 | 它没进 N 位前 5 → score < +0.46;`day_cov` 血统最好是 E 位的 +0.006 | **分不出**(只能看到前 5 名,无法判定它是否在 +0.006 以上) |
| PI:不太可能过线的 `day_centroid(Ret)`、尾盘 30 分钟、VWAP/TWAP 偏离、`LimitWidth` 缩放的 5 日收益 | 都没进前 5,也没过线 | **一致**(前 5 名的窗口里一致,不是完整检验) |
| PI:「平滑到低换手」是过线的关键 | **反了**:裸峰度 +0.97 > 任何平滑版 0.46 ~ 0.61 | **错**。奖励自带 hl ∈ {0,2,5,10,20} 的 EMA 搜索,手动再平滑是重复劳动 |

值得单记一条:共性表里 `day_corr(in_index(Ret), Ret)` n = 7、均值 −0.199 —— 第 1 轮 N 的「日内与指数同步度」那一支整族偏负,这条线也可以收了。

### 3.3 PI 第 1 轮「第 2 轮的打算」兑现情况

- 「位 b 出了 head,就把第 2 轮的 E 给 score 最高的那个 N head」→ 那个 head 是 `day_kurt(Ret)`,**条件成立**(见 §4.1 核心 B)。
- 「用 R 去掉它里面没用的平滑 / 标准化部件」→ **不适用**:`day_kurt(Ret)` 是单算子,没有部件可去。
- 「位 a 没出 head 且对照显示代理主导,就不再给 `day_cov(Vwap, Ret)` 第二个 E 位」→ **两个条件都成立**,这个核心应当结束(它用掉 1 个 E 位,按 §2.5 还剩 1 个,建议不用)。

---

## 4. 本轮候选

### 4.1 值得深挖的核心(3 个,按建议顺序)

#### 核心 A(**首选**):`ts_quantile_q50(day_centroid(Amt), 20)`

机械核心卡**第 1 名**(ablation 类,自身 score +1.21 / 所在 head +1.22)。这一轮它既是卡面第一、也是我的第一。

- **为什么**:§1.5(a) 的四类付费证据全部齐备且都正(充分 +1.21、必要 +1.73、换字段 −0.01、窗口 ×2 平台化),
  而且它是**齐次零次**量,结构上不可能是市值 / 流动性 / 价格水平的代理 —— 全快照唯一同时满足这两条的结构。
- **家族中性化恰好合适**:库里原样含该核心的 head 只有头 4 一个(头 8 含的是 `…, 10` 的版本,不是原样包含),
  所以 `fam` = {`sqrt(ts_quantile_q50(day_centroid(Amt), 20))`},E 的奖励会把头 4 本身放进控制 → **只有核心之外的新信息才拿分**。这正是 E 位该有的样子。
- **已经见过的外围写法**(这是 `--periphery-seen` 会读到的那份存档,即 293 个候选里原样含该核心的那些):
  - 这个子树**没有出现在共性表里** → 含它的存档候选**少于 4 个**(共性表门槛是 ≥ 4);
  - 能确定的一个是头 4 本身 → 外围算子名集合 **{`sqrt`}**;
  - 另外至多 2 个未知(我读不到存档明细,只能从「不在共性表里」推出上界)。
  - 拆解产出的 `sqrt(ts_quantile_q50(day_centroid(Amt), 10 / 40))`、`sqrt(day_centroid(Amt))` 是**直接评估**,不进存档 → **不计入 seen**。
  - 空集合恒在 `SEEN` 里(`scripts/idea_search.py:317`),所以「核心单独」不能当候选。
  **结论:外围空间几乎全新,`{sqrt}` 之外任何算子名集合都是新的。**
- **没见过、按 §1.5(a) 最该试的外围**(素材,不是指令):
  - 把「水平」换成「相对自身的位置」:`sub(core, cross_mean(core, 60))`、`ts_rank(core, 60)`、`cross_zscore(core, 60)` —— 判决「是水平还是新息」;
  - 条件化而不是叠加:`cs_bucket_zscore(core, LogFloatCap)`、`cs_bucket_zscore(core, LimitWidth)`、`cs_regres(core, LogFloatCap)` ——
    把它和 F1/F2 那簇风格正交开(这也直接回答「它和那簇的重叠有多大」);
  - 单边 / 分段:`cs_last_high40(core, core)`、`cs_first_low20(core, core)`、`cs_mask_top_replace_mean(core)` ——
    重心的收益是不是只在低重心那一侧(F1/F2 的折叠与分段算子,这次用在一个**齐次零次**的量上,不是用在控制变量上);
  - 交互:`mul(core, day_kurt(Ret))`、`div(core, cross_mean(core, 20))`、与 `ListAge` / `LimitWidth` 的乘性交互;
  - **分母类算子要避开 `day_var` / `day_std`**(§3.1 的数值退化)。
- **风险**:核心深度 3(`day_centroid(Amt)` 深 2),GP 子代 `max_depth = 4` 只剩**一层**外围 → `c05_no_core` 拒绝率会比第 1 轮(1269 次)更高。
  手写种子可到深度 9,所以**种子质量决定这一位的产出**;并且 16 个种子必须**骨架互不相同**(`skeleton_key` 把字段抽象成 `F`、日频字段成 `DF`、常数成 `C:*`,
  只换字段或只换窗口算同一骨架,会被 `_seeded_population` 去重掉)。
  **替代方案**:若 PI 担心深度,可以改用 `day_centroid(Amt)`(深 2,两层外围)当核心 —— 代价是 `fam` 会变成 {头 4, 头 8} 两个、
  而且含它的存档候选有 31 个,已见外围多得多(至少 {`ts_quantile`}、{`sqrt`, `ts_quantile`}、{`ts_quantile`, `cs_mask_top_replace_mean_neg`})。我倾向深度 3 那个,因为家族中性化更干净。

#### 核心 B:`day_kurt(Ret)`

机械核心卡第 14 名(enrichment,均值差 +0.93 / p 0.006 —— 这个数字按 §0.1 打折),但它是**库里的一个 head**(+0.97),也是本组第 1 轮 N 位的产出。

- **为什么**:§1.5(b)。尺度不变、整族同号、方向明确(做多低峰度),而且**外围几乎没探过**。
  它还是「本组自己的发现」上做的第一次深挖 —— 这正是 C05 要检验的那条链(N → head → E)。
- **家族中性化最干净的一种情形**:`fam` = 含该核心的 head = **它自己**(头 7,sign −1,hl 20)。
  也就是说 E 的控制里会放进**核心本身的交易信号**,产出必须与裸峰度正交才能得分。
  这是三个候选里「只奖励新信息」最彻底的一个,也因此**最难出 head** —— PI 要按这个预期定规模。
- **已经见过的外围写法**:共性表 n = 9 → 9 个存档候选含它。能确定的(来自 `missions_before` 的前 5):
  - 空集(核心单独,恒在 SEEN);
  - **{`cross_mean`}**(`cross_mean(day_kurt(Ret), 30)`、`cross_mean(cross_mean(day_kurt(Ret), 30), 30)`、三层嵌套那个);
  - **{`cross_mean`, `cross_ema`}**(`cross_mean(cross_mean(cross_ema(cross_mean(day_kurt(Ret), 20), 10), 20), 20)`);
  - 另有 ≤ 4 个未知(第 1 轮种子里还有 `cross_mean(day_kurt(Ret), 20)`,外围同为 {`cross_mean`})。
  **结论:只要外围里出现一个 `cross_mean` / `cross_ema` 之外的算子名,整个集合就是新的。**
- **没见过、最该试的外围**:
  - 条件化:`cs_bucket_zscore(day_kurt(Ret), LogFloatCap)`、`cs_bucket_zscore(day_kurt(Ret), LimitWidth)`、`cs_regres(day_kurt(Ret), LogFloatCap)`;
  - 分段 / 单边:`cs_last_high10(day_kurt(Ret), day_kurt(Ret))`(剔掉尾部最厚的 10%)、`cs_first_low20(day_kurt(Ret), day_centroid(Amt))`
    (「只在开盘集中成交的票里买低峰度」—— 把两个真来源交叉);
  - 交互:`mul(day_kurt(Ret), ts_quantile_q50(day_centroid(Amt), 20))`、`div(day_kurt(Ret), day_skew(Ret))`、与 `ListAge` 的交互;
  - 新息而不是平滑:`sub(day_kurt(Ret), cross_mean(day_kurt(Ret), 60))`、`ts_rank(day_kurt(Ret), 60)`;
  - 和同族的尺度不变量并列:`sub(day_kurt(Ret), day_kurt(Vwap))`、`day_kurt(Amt)`(成交额分布的尾部)。
  - **别再做纯平滑**(§3.2:裸值 +0.97 > 平滑版 0.46~0.61,而且奖励自己会搜 hl)。
- 深度 2 → 两层外围,GP 的损耗会比核心 A 小。

#### 核心 C(可选,我**不建议**占本轮的位):`cs_last_low40(LogFloatCap, day_quantile_q75(Amt))`

机械核心卡里没有它(卡上第 8、11 名是 `day_quantile(Vwap)` 筛子的那个变体)。

- **它是定位工具里最强的结构**(§1.2:R 之后 +2.11,train +2.11 / valid +2.39),`fam` 只有头 1 一个(头 6 的筛子不同),深度 3。
- **已经见过的外围**:不在共性表里 → 含它的存档候选 < 4 个;能确定的是头 1 → **{`sqrt`, `cross_quantile`}**。
- **为什么我不建议**:§1.2 的判定是「控制变量的非线性再编码」。把一个 E 位花在这里,最可能的产出是**更多同类再编码**
  (换折叠曲率、换带宽、换日频叶子),而这些东西 **M 自己正在大量产出**(M2 的 8 个 head 里 5 个是),
  到最终融合时会被 ρ ≥ 0.7 / ρ ≤ −0.5 的去重规则互相挤掉 —— B 组的增量就白花了。
  这个家族要挖,**用 R 的 16 次直接评估更便宜**(§4.2 列了 6 个),不需要一个 96 次的 GP 位。
- 如果 PI 还是要用它(例如想正面检验「折叠」这个机制能不能推广),我的建议是把外围限制在**条件化与带宽**上,
  并且**明确不要再出现 `sqrt` / `abs_` / `pow_2`**(折叠已经在核心外被头 1 占了 `{sqrt, cross_quantile}`,同类再做一遍没有新信息)。

#### 不建议的几个卡面前排

- 卡 2 `ts_quantile_q50(day_centroid(Amt), 10)`、卡 5 `ts_quantile_q50(ts_quantile_q50(day_centroid(Amt), 10), 10)`、卡 6 `day_centroid(Amt)`、
  卡 12 `cs_mask_top_replace_mean_neg(ts_quantile_q50(ts_quantile_q50(day_centroid(Amt), 10), 10))`:
  与核心 A 是同一个东西的不同窗口 / 嵌套。按 §2.5「每个核心至多 2 个 E 位」,把它们各占一位等于把核心 A 做四遍。
- 卡 3 `cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Close)))`(自身 +0.45):这是 §1.3 那条「便宜但不是最便宜」的分段,
  是整个快照里**唯一必要性为正的非折叠部件**(+0.45),作为**灵感**很有价值(见 §4.3 N2),但作为 E 的核心它深度 3、
  而且产出会落在 F2 那簇风格里,和核心 C 同样的理由。
- 卡 18、19 `add(LimitWidth, add(LimitWidth, day_cov(Vwap, Ret)))` / `add(LimitWidth, day_cov(Vwap, Ret))`:
  §1.6 已说明 `add` 一个大常数在 z-rank 之后保序,等于没做;第 1 轮 §1.2 的结论不变。

### 4.2 R 目标(≤ 16 次直接评估)

**唯一一个已经测出增益、能立刻生效的替换**:

1. `sqrt(cs_last_low40(LogFloatCap, day_quantile_q75(Amt)))` —— 替换头 1(+2.115,增益 **+0.33**)。已测,重新提交即可生效。
   (`cross_quantile_q25@3->2` 的那个变体增益只有 +0.14,且与 #1 争同一个 head,不要同时提。)

**其余是诊断性的**(可能不满足 `score ≥ head + 0.1` 或 `ρ ≥ 0.5` 而不触发替换,但每一次都买到一条结构知识)。按价值排:

对头 1(`sqrt(cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile_q75(Amt)), 3))`,+1.78):

2. `sqrt(cs_last_low40(LogFloatShares, day_quantile_q75(Amt)))` —— 被折叠的量换成**股本**(去掉价格成分)。
   和 #3 一起判决「折叠的是市值、还是股本、还是股价」。六个日频叶子在整个拆解里**一次都没换过**,这是信息密度最高的一问。
3. `sqrt(cs_last_low40(LogTotalCap, day_quantile_q75(Amt)))` —— 流通市值换总市值。
4. `sqrt(cs_last_low40(ListAge, day_quantile_q75(Amt)))` —— 换上市年龄:判决它是不是只是「小 / 新」。
5. `abs_(cs_last_low40(LogFloatCap, day_quantile_q75(Amt)))` —— 折叠算子换 `abs_`(同折叠、不同曲率)。
   若与 #1 几乎相同,就证实「来源是折叠本身」(§1.2),不是开方。
6. `sqrt(cs_last_low20(LogFloatCap, day_quantile_q75(Amt)))` —— 筛子带宽 40% → 20%。
7. `sqrt(cs_last_low10(LogFloatCap, day_quantile_q75(Amt)))` —— 带宽 10%(`ops_ext` 的细带就是为这种事加的)。

对头 4(`sqrt(ts_quantile_q50(day_centroid(Amt), 20))`,+1.22):

8. `sqrt(cross_mean(day_centroid(Amt), 20))` —— 滚动**中位数换均值**。判决「中位数的稳健性是不是必要」。
9. `sqrt(ts_quantile_q50(day_centroid(Amt), 60))` —— 窗口再加倍(20 → 40 已经打平 +1.220,看平台在哪里结束)。
10. `sqrt(ts_quantile_q25(day_centroid(Amt), 20))` —— 取 20 日分布的下四分位而不是中位数(「最早的那些天」)。

对头 5(`cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Amt)))`,+1.18):

11. `cs_mask_top_replace_mean_neg(day_quantile_q75(Amt))` —— 去掉 `pow_2_5`。
    §0.2 的模拟说这会把被错位的那 10% 从 92 分位挪到 74 分位;若 score 大幅下降,就证实「错位的落点」才是这个 head 的全部内容(§1.4)。

对头 3(`cs_first_low20(cs_normalize(day_open(Open)), cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Close))))`,+1.32):

12. `cs_first_low20(day_open(Open), cs_mask_top_replace_mean_neg(day_quantile_q75(Close)))` —— 一次去掉两个:
    `cs_normalize`(已证逐位恒等)与 `pow_2_5`。判决那条「第 10~30 分位」的带子对落点有多敏感。
13. `cs_first_low20(day_open(Open), cs_mask_top_replace_mean(day_quantile_q75(Close)))` —— 把错位换到**最高** 10%(`_neg` 去掉):
    判决「剔掉最便宜的 10%」与「剔掉最贵的 10%」哪一边在起作用(§1.3 说前者,这是正面检验)。

对头 2(`cs_first_low20(day_quantile_q75(Amt), log(day_open(Open)))`,+1.40):

14. `cs_first_low20(ts_quantile_q50(day_centroid(Amt), 20), day_open(Open))` —— 把组内的破平局项从「流动性」换成**核心 A**:
    「在最便宜的 20% 里买开盘集中成交的」。这是一个把真来源装进强风格骨架的试探(很可能 ρ < 0.5 不触发替换,但数字本身值钱)。

**明确不要花 R 的地方**:`log`(头 2)、`cs_normalize`(头 3)、`sqrt`(头 4)、`Amt→Volume`(头 4)——
前两个逐位恒等、增益恒为 0,后两个已测且打平,`+0.1` 的门槛永远到不了(§2.1)。

### 4.3 N 的灵感(3 条,按价值排)

**共同出发点**(§1.6):这个奖励会给「控制变量的非线性再编码」很高的分,而 M 自己正在大批量产出这种东西。
B 组的 N 位要是也去做,只会撞 ρ ≥ 0.7 / 骨架禁令,并在最终融合时被挤掉。
**所以 N 位应该只做齐次零次(尺度不变)的量,并且明确避开把 `LogFloatCap` / 股价 / `Amt` 的水平当叶子去折叠或分段。**

**N1(首选):日内活动的「时间形状」—— 把头 4 从一个量推成一族。**
头 4 告诉我们两件事:(i)成交在一天里的时间分布是被定价的;(ii)**起作用的是 20 日持久水平,不是当日值**(必要性 +1.73,当日值单独 −0.085)。
把这两条推广:

- 重心的亲属:`day_centroid(Volume)`、`day_centroid(abs_(Ret))`(**波动**的时间重心)、`day_centroid(pow_2(Ret))`;
- 和重心正交的形状量:`day_gini(Amt)`(一天的成交集中在多少分钟里,与「集中在什么时候」无关)、
  `day_flat_run_max(Close)`(最长无变动分钟串 / 有效分钟数,冻结报价)、分钟成交量的自相关;
- 时段占比:尾盘 30 分钟成交额占比、开盘 30 分钟占比、两者之差(全部写成比值 → 尺度不变);
- **全部套 20 日及以上的滚动中位数 / 均值**(这是 N1 的核心假设,也是和第 1 轮 N 最大的不同:第 1 轮的平滑是为了压换手,这里是因为**信号本身在持久水平里**);
- 必须放的对照种子:同一个量的**新息**版(`sub(x, cross_mean(x, 60))`)—— 判决「水平 vs 新息」,一次把 N1 的整条假设钉死。

**N2:「分段」这个处理用在尺度不变量上。**
§1.3 发现快照里唯一必要性为正的非折叠部件是「把最便宜的 10% 剔出带子」(+0.45)。
这个**处理**(剔掉一个尾部、只在中间一段里排序)本身可能是有价值的手艺,而不只是价格因子的附件。
把它用在齐次零次的量上:`cs_mask_top_replace_mean_neg(day_kurt(Ret))`、`cs_last_high10(day_skew(Ret), day_skew(Ret))`、
`cs_first_low20(day_kurt(Ret), day_centroid(Amt))`、`cs_last_low10(ts_quantile_q50(day_centroid(Amt), 20), ListAge)`(剔掉次新股)。
这一条和核心 A / B 的 E 位有重叠风险(E 的外围也会试分段),所以 N2 的种子应该放**两个来源的交叉**,E 位不会去的地方。

**N3(备选):分钟分布的高阶形状,接着峰度往下走。**
第 1 轮峰度过线、偏度没过,这是一条还没走完的线:上下半方差之比、
`sub(day_kurt(Ret), day_kurt(Vwap))`(收益的尾部 vs 价格水平分布的尾部)、`day_kurt(Amt)`(成交额分布的尾部 = 大单集中度)、
分钟收益的符号串长度。注意**不要再叠 `cross_mean` 平滑**(§3.2)。

**三条共同的实现侧提醒**(源码,会直接影响任务文件):
- 16 个种子必须**骨架互不相同**;只换字段 / 只换窗口是同一骨架,`_seeded_population` 会去重后只留一个。
- N 位 `--seed-share 0.5`,16 个种子占半个种群;E 位 `--seed-share 1.0 --graft-fill 32`,**32 个个体全是种子**,
  第 0 代就要打 32 次分 —— 96 次预算里三分之一花在手写种子上,种子差就是直接浪费。
- 本轮**有库禁令**了(快照 9 个 head):骨架相同或与任一 head 秩相关 ≥ 0.7 的候选一律拒。
  F1 / F2 / F3 那簇风格已经被 9 个 head 占住了大半,这是「N 位不要去碰水平变量」的第二个理由(不只是经济判断,是预算问题)。
- 分母里**不要放 `day_var` / `day_std` / `day_mean`** 这类可能为 0 或近 0 的量(§3.1 的数值退化)。

### 4.4 一条给 PI 的附带观察(不属于本角色的决定,但影响判读)

最终因子库按顺序贪心去重,ρ ≥ 0.7 或 ρ ≤ −0.5 就丢(PLAN §3)。本组现在的 9 个 head 里,
**F1(2 个)+ F2(3 个)+ F3(1 个)共 6 个在经济上是同一簇**(小市值 / 低价 / 低流动性,全部慢变、全部靠「线性中性化去不掉非线性再编码」活着)。
它们互相 |ρ| < 0.7 才都进了库,但在测试段它们很可能同涨同跌。
真正给本组提供分散度的是 F4 的 2 个(`ts_quantile_q50(day_centroid(Amt), 20)`、`day_kurt(Ret)`)。
**这是我建议把两个 E 位都给 F4(核心 A、核心 B)而不给核心 C 的最终理由。**

---

## 5. 文献题目(4 个,给文献员;只用 2023-08-08 之前发表的文献,每条注明年份)

**Q1 —— 对准核心 A(`ts_quantile_q50(day_centroid(Amt), 20)`:日内成交的时间重心,滚动中位数)。**
2023-08 之前的文献里,**「一天的成交量 / 成交额在交易时段内的分布」**(日内成交量的 U 形、开盘与收盘时段的成交占比、成交的时间重心 / 时间加权矩)
被怎样做成**截面**预测变量?具体要:
(a) 归一化口径 —— 用占比、用时间重心、还是用与典型日内曲线的偏离?
(b) **这个特征有多持久**,文献用多长的窗口(当日 / 5 日 / 20 日 / 一个季度)平滑它,有没有报告「水平比新息更有预测力」这类结果?
(c) 它和**投资者结构**(散户在开盘集中交易、指数与被动资金在收盘集合竞价成交)的联系,A 股收盘集合竞价(2018 年起)对这个量的影响;
(d) 符号:成交偏早 / 偏晚哪一边后续收益高;
(e) 作者额外控制了什么(规模、流动性、换手、特质波动),有没有人专门指出它**不是**流动性或规模的代理。
英文关键词:intraday volume distribution, intraday volume U-shape, opening vs closing volume share, volume timing,
time-weighted volume centroid, closing auction volume share, trading activity concentration, retail vs institutional intraday trading,
turnover timing and cross-sectional returns。
中文关键词:日内成交量分布, 日内成交 U 形, 开盘成交占比, 尾盘成交占比, 成交时间重心, 收盘集合竞价, 成交集中度, 散户与机构日内交易, A股截面。

**Q2 —— 对准核心 B(`day_kurt(Ret)`:分钟收益的超额峰度,做多低峰度)。**
2023-08 之前,**高频 / 日内收益的已实现峰度(以及尾部厚度、跳跃强度)**作为截面预测变量有哪些结果?要:
(a) 符号与持有期(次日 / 一周 / 一个月),**有没有文献报告「不要平滑」或「当期值优于移动平均」**;
(b) 它和已实现偏度、跳跃检验量(Barndorff-Nielsen–Shephard 一类)、彩票偏好 / MAX 效应之间的关系 —— 低峰度溢价是不是彩票偏好的反面;
(c) 常见的**条件化**处理:在规模 / 流动性 / 换手分组内标准化,还是双重排序;
(d) 在中国 A 股上的复现结果与符号;
(e) 涨跌停(一字板、全天一个价)会怎样污染日内高阶矩,文献怎么处理这些日子。
英文关键词:realized kurtosis cross-section of stock returns, intraday return tail thickness, jump intensity and expected returns,
realized skewness, lottery demand MAX effect, idiosyncratic tail risk, high-frequency moments China A-shares, price limits and realized moments。
中文关键词:已实现峰度, 日内收益尾部, 跳跃强度, 已实现偏度, 彩票偏好, MAX 效应, 高频矩, A股, 涨跌停对高频矩的影响。

**Q3 —— 对准 F1 / F2(折叠的市值秩、名义股价分段)与「我的中性化只去线性项」这个事实。**
2023-08 之前,文献怎么处理**规模与流动性的「非线性 / 非单调」截面效应**,以及**名义股价**这个特征?要:
(a) U 形 / V 形的规模效应、「只在最不流动的那一档里有效」这类**条件化**结果,以及文献用来呈现它们的手法(双重排序、分组内排序、分段回归、交互项);
(b) **名义股价水平**(低价股)在 A 股与美股的截面证据:它与规模、换手、彩票偏好的区分度,以及把最低价的一档(ST / 面值退市风险)剔掉之后效应还剩多少;
(c) **方法论**:只对规模做**线性**中性化(或线性 z-score 回归)之后,规模的非线性成分会残留 —— 文献里怎么检测和处理这件事
(非参数中性化、分组内去均值、按分位数桶中性化、Fama–MacBeth 加入平方项);
(d) 2018–2023 这段时间 A 股小市值 / 低价这一簇风格的符号稳定性(只要 2023-08 之前发表的证据)。
英文关键词:nonlinear size effect, non-monotonic size premium, conditional size-illiquidity interaction, nominal share price anomaly,
low-priced stocks, penny stock effect, double sorting, within-group standardization, nonparametric risk neutralization,
residual after linear size control。
中文关键词:规模效应非线性, 非单调规模溢价, 规模与流动性交互, 名义股价, 低价股效应, 面值退市, 双重排序, 组内标准化, 非线性中性化, 线性中性化残留。

**Q4 —— 对准 N2 的那个「处理」(剔掉一个尾部 / 只在一段里排序 / 把一档整块搬走)。**
2023-08 之前,**对截面特征做「筛选式」处理**的文献怎么做、报告什么?要:
(a) 「只在 x 低(或高)的那一段里按 y 排序」这种条件化因子的构造与评估惯例(带宽怎么选,20% / 40% 有没有依据,怎么避免带宽挑选造成的过拟合);
(b) **缩尾 / 截断 / 把极端一档替换成均值**对截面因子的影响,文献推荐的位置(1%、5%、10%)和替换值(均值、中位数、边界值);
(c) 筛掉一档会带来多少换手与成本,长仅(long-only)组合里这类筛子的净效果;
(d) 把一个特征**限制在一段股票池里**(小市值内、低流动性内、剔除次新股与 ST)之后,文献报告的样本外衰减有多大。
英文关键词:conditional factor construction, screening factors, double-conditional sorts, bandwidth choice in portfolio sorts,
winsorization of firm characteristics, trimming extreme deciles, long-only factor implementation cost, universe screens and factor decay,
excluding recent IPOs and distressed stocks。
中文关键词:条件因子构造, 筛选式因子, 条件双重排序, 分组带宽选择, 特征缩尾, 截断极端分位, 纯多头实现成本, 股票池筛选与因子衰减, 剔除次新股与ST。

---

## 6. 留给第 3 轮核对的预测(可检验)

1. **核心 A 的 E 位(家族中性化含头 4)产出 ≥ 1 个 head 的概率约 45%。** 若有,最可能的外围是**条件化**
   (`cs_bucket_zscore` / `cs_regres` 配 `LogFloatCap`)而不是平滑或新息 —— 因为头 4 本身已经进控制,只有把它和风格正交开才算新信息。
2. **核心 A 的「水平 vs 新息」判决**:`sub(core, cross_mean(core, 60))` 这类新息写法的 score 会**低于** `core` 本身(+1.21)至少 0.3。
   依据是必要性 +1.73 与当日值 −0.085:这一族的 alpha 在持久水平里。若新息版反而更高,§1.5(a) 的读法要改。
3. **核心 B 的 E 位产出 ≥ 1 个 head 的概率约 25%**,明显低于核心 A —— 因为 `fam` 就是核心自己,门槛最硬。
   若有,最可能来自**两个真来源的交叉**(`day_kurt` × `day_centroid`),而不是峰度的单独加工。
4. **R 的 #1(`sqrt(cs_last_low40(LogFloatCap, day_quantile_q75(Amt)))`)会触发替换**(已测 +2.115,增益 +0.33;与原 head 的交易信号 ρ 远高于 0.5)。
5. **R 的 #2 / #3(`LogFloatShares` / `LogTotalCap` 换叶子)里,至少一个的 score ≥ +1.3**。
   理由:§1.2 说来源是「折叠」而不是被折叠的具体变量,而这三个日频叶子互相秩相关很高。
   若两个都塌到 0.5 以下,说明被折叠的必须正好是**流通市值**,F1 就不只是「折叠」那么简单,§1.2 要补写。
6. **R 的 #5(`abs_` 换 `sqrt`)的 score 与 #1 相差不超过 0.15**(两者在正值上互为单调变换,只通过 EMA 的非线性留下差异)。
   若差距很大,说明 hl > 0 的 EMA 在原始值上的非线性比我估计的重要得多,§0.2 第 2 条要加重。
7. **R 的 #11(去掉 `pow_2_5`)的 score 会比头 5 的 +1.18 低至少 0.3**(落点从 92 分位挪到 74 分位,错位的幅度变小)。
   若几乎不变,§1.4 的「落点决定一切」要改成「只要搬到带子外面就行」。
8. **不会有任何候选以 `LimitWidth` / `BoardCode` 做加法叶子而过线**(第 1 轮 §6 预测 3 的字面版,这一轮仍未被检验,继续挂着)。
   但第 1 轮那条更一般的推论(静态风格暴露过不了 0.5)**已经被 M 第 2 批推翻**,不再作为预测。
