# 文献笔记 — s807 / r3(文献员)

范围:只用 **2023-08-08 之前发表**的论文 / 工作论文 / 研究报告(arXiv、SSRN、机构工作论文系列、交易所研究中心报告以首版 / 发表日期为准)。对 `r3/analysis.md` §5 的 L1–L4 四个题目逐一检索;每条「处理方式」后标出处编号 `[n]`,对应文末〈参考文献〉。搜不到的地方明确写「搜不到」,不补全、不猜测。L2/L4 与 r2 共用了 Baltussen 等 2018、Heston–Korajczyk–Sadka 2010、Bogousslavsky 2021 三篇——本轮重新检索确认过一次(不是直接照抄 r2 的结论),L4 另外新增了两篇针对 2018-08-20 上交所收盘集合竞价改革本身的实证论文和一篇交易所研究中心报告,把 r2/lit.md 留的"制度公告不算文献"那个空白填上了一部分。

---

## L1 — 分钟级「零成交 / 重复成交 / 不动」型不流动度量(对准核心 A:`day_distinct_ratio(Volume)`)

**能翻译成算子语言的处理方式:**

1. **度量族的共同构造:不是看单日取值,是看一个滚动窗口里"退化日"的占比 / 计数。** Lesmond–Ogden–Trzcinka [1](*RFS* 1999,12(5):1113–1141,"Zeros"/LOT 度量)用零收益天数的发生率估计交易成本;Liu [2](*JFE* 2006,82(3):631–671)的 `LM1`/`LM12` 是过去 12 个月(252 个交易日)**零成交量天数的、经换手率调整的标准化计数**;Fong–Holden–Trzcinka [3](*Review of Finance*,第 21 卷第 4 期头条文章;FHT 估计量工作论文版本约 2014 年流传)的 FHT 把同样的"零收益发生率"简化成一个免优化的估计量,逻辑仍是"交易成本高 ⟹ 当日收益为零的概率高"。
   翻译:三篇的共同形状是 `cross_mean(indicator(该日退化), N)`(N = 21/125/252 这类月 / 年窗口),**不是单日取值,也不是 `day_*` 内部的分钟聚合**。这支持 analysis.md §4.1 建议的外围方向(i)——用 `cross_mean` / `cross_zscore`(窗口 ≥ 20)把 `day_distinct_ratio(Volume)` 从"当日取值"变成"跨日频率",而不是指望任何 `cs_*` 逐日包装把它救活(§0b 已经证明做不到)。
2. **换手率调整不是可选项,是这类度量能单独站得住的必要条件。** Liu [2] 的换手调整明确把"同样的零成交天数,换手率越高判越不流动"反过来写——即**同样的退化计数,要除以 / 结合一个连续的交易活跃度量才算完整**,否则它测的只是"交易日历上的巧合"。
   翻译:这与 analysis.md §4.1 外围方向(ii)"份额 / 无量纲比"同构,但给出了一个比"除以 `day_distinct_ratio(in_sum_rolling(Volume,k))`"更贴近文献的具体形式——**除以/结合一个换手率或成交额水平**(即核心与流动性控制列的交叉),这也是为什么 §4.1 要求先把核心与流动性控制 `cross_mean(day_sum(Amt),30)` 的 |ρ| 算出来再决定写法:文献里这类度量从设计上就没打算与流动性水平独立,E 位要赢的不是"零相关",而是"方式"。
3. **这类度量与 Amihud 式价格冲击度量是两个不同维度,不能互相替代,但也不能假设互不相关。** Goyenko–Holden–Trzcinka [4](*JFE* 2009,92(2):153–181)用日内基准数据给低频流动性代理做"赛马",发现 Amihud [5](*Journal of Financial Markets* 2002,5(1):31–56)的 ILLIQ 在**价格冲击**上表现最好,而零收益 / FHT 类在**交易成本**基准上表现更好;两者衡量的是流动性的不同侧面。
   翻译:`day_distinct_ratio(Volume)` 继承的是"零 / 退化事件"这条线,不是"价格对成交额的冲击"那条线——它与规则 §4 陷阱 3 里列的"流动性(成交额、换手)的非线性函数"不是同一个量,这支持 analysis.md 把它判为"可能是真输入"而不是"波动 / 流动性水平的马甲";但 [4] 同时提醒,两条线在实证里经常被同一批"流动性"论文一起检验,文献没有给出"零事件类度量与成交额水平 |ρ| 应该多低"的具体阈值,核心 A 与流动性控制的相关度还是要靠相关度表自己量。
4. **零/退化事件本身在高频数据里被拆成"系统性"与"个股特异性"两部分,且明确提醒要先剔除纯粹的价格离散化(报价单位)伪影。** Kolokolov–Livieri–Pirino [6](*Journal of Econometrics* 2020,218(1):32–81)把"零收益概率"建模成一个**潜在的连续时间过程**(不是常数),并拒绝"概率恒定"的假设;论文明确讨论零收益的发生率里有多少是**价格离散化(报价最小变动单位)造成的机械伪影**,需要与真实的不流动分开。
   翻译:这给 §0b 的发现("把分钟聚粗,`day_distinct_ratio` 的 distinct 反而更差")提供了一个方法学读法——`Volume` 的取值离散度部分来自**成交量本身的报价/手数粒度**(类似价格的最小变动单位),部分来自真实的"这一分钟没有成交";外围如果想把真实信号和粒度伪影分开,文献的做法是**跨资产 / 跨日的系统性分量 vs 个股分量分解**,对应到我们的算子就是"先 `cross_mean`(或当日截面均值)剥出一条市场级退化率序列,再看个股对它的残差",这与 analysis.md §4.1(iii)"共动用相关系数不用斜率"是同一个方向,但给出了更具体的理由:**不剥出市场分量,个股的"零/退化"读数里会混进交易日历本身的共性(节假日前、指数调仓日等)。**
5. **A 股的零收益 / 非流动性溢价证据存在,但样本较早、无法确认完整出处细节。** 一项基于 1997–2005 年 A 股数据的研究,**同时**用 Amihud 非流动性比率、换手率、零收益率、有效流动速度、Pastor–Stambaugh 指标这五种度量衡量流动性,报告"无论用哪个指标,流动性溢价都存在"。
   **这条我无法核实完整的标题 / 作者 / 发表信息**(来源页面 403,只有二次引用的摘要),**不列入参考文献**,只作为"A 股零收益类度量确实有人用过、方向与美股一致"的弱证据记在这里,不要当成可核实的引用。

**搜不到的地方(明确空白,不要当成文献证伪):**
- 分钟级(而不是日级)的"零成交分钟数"或"取值重复分钟数"作为横截面特征的直接先例,**搜不到**;最接近的是上面的高频价格停滞(staleness)文献 [6],但它处理的是**收益**停滞,不是**成交量**取值的离散度,且它更新、更完整的版本(Bandi–Pirino–Reno 的 EXIT 度量)发表时间在 2023-08-08 之后或无法确认首版日期,**不用**。
- [1][2][3] 的精确公式(标准化方式、换手调整的具体代数形式)**搜不到可读的原文**——拿到的 PDF 是扫描 / 压缩格式,工具无法提取文本,只核实了二次引用里的文字描述,没有逐项核实公式本身。
- 这类度量"纯多头一侧单独报没报过"(L1(c)的后半句)——**搜不到**单独的纯多头检验;[2] 的核心检验是多空组合的流动性溢价,没有分腿报告。
- A 股涨跌停一字板 / 停牌对"零成交"类流动性度量的具体影响,**搜不到**专门的同行评审实证(只有涨跌停制度改革对流动性总体影响的研究,与"零成交度量本身怎么被一字板污染"不是同一个问题)。
- 零成交类度量的符号与半衰期(回看窗口多长、持续多久)的具体数字,[1][2][3] 的摘要级信息里**搜不到**。

---

## L2 — 已实现波动率口径、去尺度的 vol-of-vol / 风险不确定性(对准 N-α)

**能翻译成算子语言的处理方式:**

1. **"风险的不确定性"确实是文献里独立检验过的横截面因子,但构造用的是隐含波动率的滚动标准差,不是已实现波动率,而且没有去尺度。** Baltussen–van Bekkum–van der Grient [7](*JFQA* 2018,53(4);工作论文题目直接叫"Unknown Unknowns: Vol-of-Vol and the Cross Section of Stock Returns")把"不确定性"构造成**个股平价期权隐含波动率的月度滚动标准差**(IV 水平序列的 SD,不是变异系数),高 vol-of-vol 组比低组每年跑输约 8%,独立于约 20 个已知的波动相关效应,在卖空约束最松的分组里最弱、不显著。
   翻译:[7] 的构造在算子语言里就是 `cross_stddev(IV, 60)`——**与我们 r2 的 R 替换进库的那个"明写波动的空对照" `ts_sum(cross_stddev(day_std(Ret), 60), 1)` 是同一个形状,只是把 `day_std(Ret)`(已实现波动)换成了隐含波动率**。这件事必须明确写出来:**文献的基准做法本身就是"未去尺度的 std",我们自己在 §1.4 发现它与波动控制 |ρ| = 0.56,这不是文献的错,是"把隐含波动换成已实现波动"这一步引入的问题**——隐含波动率的量纲本身更接近一个"百分比",跨股票的尺度差异远小于已实现波动(尤其是用 `day_std(Ret)` 这种未年化的日频标准差),所以同一个"不做任何去尺度"的构造,套在已实现波动上更容易被尺度本身主导。**去尺度(变异系数)是我们自己为了适配已实现波动口径而加的一步,不是对文献的复刻**,这也是为什么 analysis.md 把这条的合理度封顶在 4(有机制 + train 证据),而不能给 5(文献里没有人直接验证"已实现波动的变异系数"这个具体写法)。
2. **已实现波动率版本的 vol-of-vol(不论是否去尺度)作为独立的横截面排序变量,搜不到同行评审证据——这是一个真实的检索空白,不是我们没搜到技巧。** 检索覆盖了"realized variance dispersion"、"coefficient of variation of realized volatility"、"volatility of volatility realized measures cross-section"等多组关键词,返回的都是邻近但不同的构造:Amaya 等的已实现偏度 / 峰度(不是已实现波动的波动),Bollerslev–Li–Zhao 的上行 / 下行已实现方差不对称性(是同一已实现方差内部的分解,不是跨期的离散度),Ang–Hodrick–Xing–Zhang 的总体波动率风险暴露(是对聚合波动率创新的敏感度,不是个股自身波动的离散度)。**没有一篇把"已实现波动率序列自身的标准差 / 变异系数"当作横截面排序变量。**
   翻译:这直接确认了 analysis.md §4.3 的判断——A 股 + 已实现波动率口径的 vol-of-vol 是明确的空白,N-α 如果做出来,填的是一个真的洞,不是复刻;但也意味着**没有文献能告诉我们"用 `day_std(Ret)` 的变异系数"这个具体写法该用多长窗口、该不该按上行/下行分别算**,这些选择只能靠 train 上的证据,不能再加文献那一分。
3. **波动的"持续性"(自相关)与波动的"离散度"(标准差/变异系数)在文献里是被当成两件不同的事情处理的,但都不是作为独立的 vol-of-vol 信号单独验证过。** Nath–Sarafidis [23](2017,华沙大学 *JBFE* 系列,第 2 卷第 8 期,27–53 页)研究特异性风险的**持续性**(用自回归式的量)与**收益反转**的关系,发现特异性波动变化量及其滞后项在多个分位数上都影响短期收益,但论文的落脚点是"反转",不是"持续性本身定价";Angelidis–Tessaromatis [24](*International Review of Financial Analysis* 2008,17(3):539–556)发现英国小盘股的特异性波动能预测小盘溢价部分,且**控制了特异性波动可能存在的持续性之后结果依然显著**——即持续性在这篇里是被当成**要控制掉的东西**,不是主角。
   翻译:[23][24] 都是特异性波动(idiosyncratic volatility)的文献,不是已实现波动率水平本身的持续性,而且都不是中国市场、都不是已实现波动率口径——只能算"持续性 vs 离散度是两件不同事"这一点的弱支持,**不能当成"波动自相关 / Hurst 作为独立特征"有同行评审证据**,这与 analysis.md §4.3 N-α 种子方向(iii)"波动的自相关 / Hurst"目前没有直接文献撑腰,要清楚地算作"无文献加分、纯靠机制 + train"。
4. **去尺度这一步本身(未去尺度的 std 在乘性尺度下约等于波动水平本身)——文献没有专门讨论这个共线性问题,这是我们自己从 r2 的 R 结果(§1.4)里读出来的,不是文献命题。** 检索未能找到任何论文明确讨论"用波动率的标准差作为横截面特征时,它与波动率水平本身的共线性"这一点并提出变异系数作为修正——这件事在我们自己的实验里被 R 的替换结果直接证实(§1.4:明写波动的空对照 |ρ|=0.56,变异系数版 |ρ|=0.18),但它是**我们自己的方法学发现**,不是对文献的复述。

**搜不到的地方(明确空白,不要当成文献证伪):**
- 已实现波动率的变异系数(或任何去尺度写法)作为独立横截面排序变量的同行评审证据,**搜不到**(§4.3 已经判了,本轮确认这是真空白)。
- A 股上针对已实现波动率口径的 vol-of-vol 定价检验,**搜不到**。
- "未去尺度的 std 在乘性尺度下约等于水平本身"这一共线性在任何 vol-of-vol 或 beta 文献里被明确讨论并提出修正方法,**搜不到**(本轮在 L3 的 Vasicek/Frazzini–Pedersen 文献里找到了"beta 的尺度问题"的讨论,但没有人把同一逻辑套到"std 作为特征"本身)。
- HAR 模型残差的离散度作为定价变量,**搜不到**相关文献。
- 波动率自相关 / Hurst 指数作为独立于波动离散度的横截面特征,同行评审证据**搜不到**(只有邻近的特异性波动持续性文献 [23][24],且结论本身是作为控制变量而非主角)。

---

## L3 — 把「滚动回归斜率」当横截面特征时,尺度与估计误差怎么处理(对准 F3 的方法学,库的 58%)

**能翻译成算子语言的处理方式(这一节是本轮最实的一节——直接读到了 Frazzini–Pedersen 论文正文,逐字确认):**

1. **标准做法里,beta 从来不是直接用 `cov/var` 的裸回归斜率,而是显式分解成「相关系数 × 波动率比」两部分分别估计,而且两部分用不同的窗口和频率。** 直接读到 Frazzini–Pedersen [8](*JFE* 2014,111(1):1–25,工作论文 2013-05-10 draft,NBER WP 16601)正文「Estimating Ex-ante Betas」一节:他们把个股 beta 写成
   `β̂ = ρ̂ · σ̂_i / σ̂_m`
   ——**与 analysis.md §0a 推出的 `β = corr_d(x,y)·σ_d(y)/σ_d(x)` 是完全同一个代数恒等式**,不是我们自己拍的。原文明确给出两个理由分开估计相关系数和波动率:(i)相关系数的时变比波动率**慢**,所以波动率用 **1 年滚动窗口** + **逐日收益**,相关系数用 **5 年滚动窗口**;(ii)相关系数额外用**重叠的 3 日对数收益**(而不是逐日收益)来控制非同步交易(non-synchronous trading)的噪声——波动率不需要这一步,只有相关系数需要。
   翻译:这是对 F3 骨架的一条直接、可核实的方法学批评——`cross_regbeta(x, y, d)` 用**同一个 d(10/15/30 日)**同时估计分子的协动和分母的方差,文献的标准做法是**波动率用短窗口、相关系数用更长且经非同步交易修正的窗口**,从未见过两者共用一个窗口的写法。R1(`cross_corr` 替换 `cross_regbeta`)方向是对的,但如果要在 E/N 位把这个机制重新搭,**窗口应该不对称**,而不是只是换算子。
2. **原始的时序 beta 永远要先向 1(或截面均值)做 Vasicek 式收缩,目的就是压住极端值,这是行业与学术的共同底线操作,不是可选项。** [8]紧接着写:为了"减少极端值的影响"(reduce the influence of outliers),把时序估计的 beta 向截面均值收缩:`β̂ = w·β̂_TS + (1−w)·β̂_XS`,文中简化为全局 `w = 0.6`、`β̂_XS = 1`,并说明这个收缩常数**不影响组合排序**(只影响多空头的放大倍数)。原始出处是 Vasicek [9](*Journal of Finance* 1973,28(5):1233–1239),其收缩权重本身是估计误差的函数:`w_i = 1 − σ²_{i,TS} / (σ²_{i,TS} + σ²_XS)`——**估计噪声越大(窗口越短、个股越特殊),越应该被拉回截面均值**。[8] 的参考文献列表里同一页还列着 Scholes–Williams [11](*JFE* 1977,5(3):309–327,也是逐字读到的)和 Pástor–Stambaugh [12](*JPE* 2003,111:642–685,同样逐字读到)。
   翻译:**没有任何一个版本的文献会把一个未经收缩的 `cov/var` 斜率直接当成横截面特征来用**——而我们库里 14 个 F3 head 全部是未收缩的裸斜率,恰好对应 analysis.md §0a 发现的「分母只有 `> EPS` 保护、x 几乎不动就会爆」那个极点。这给 §2(C) 的"真正该打的靶子"添了一条文献依据(拿到 L3 可以让核心/R 的合理度从 3 升到 4):**`cross_regbeta` 如果要在新的 E/N 里复用,必须先做 Vasicek 式的收缩(向 1 或向截面均值收缩),而不是只在外围加 `cs_normalize`**(§1.2(4) 的必要性 +0.33 说明"去掉绝对尺度更好",方向与文献一致,但文献要求的是更系统的收缩,不只是去掉 x 的尺度)。
3. **非同步 / 稀疏交易会系统性扭曲同窗口回归斜率,这是一类专门被研究过的偏差,而且机理与我们 F3 的 y 腿(离散量)高度吻合。** Dimson [10](*JFE* 1979,7(2):197–226)的「aggregated coefficients」方法把回归斜率在领先、同期、滞后的市场收益上分别估计再求和,专门纠正"稀疏交易股票的同期回归斜率有偏"这个问题;Scholes–Williams [11] 用类似的领先 / 滞后结构处理非同步交易。
   翻译:F3 的 y 腿(`day_distinct_ratio(Volume)` 及其包装)正是文献里这类方法要修正的对象的一个极端版本——**y 只有几百个取值(distinct 0.03–0.05),意味着大量"当日取值与窗口内历史取值重复"的情况,这正是 Dimson/Scholes–Williams 处理的"非同步/稀疏"机理在被解释变量一侧的类比**(他们处理的是解释变量侧的稀疏交易,我们这里是被解释变量侧的离散量,但"同期窗口回归斜率被稀疏性扭曲"是同一类问题)。**这是一条 analysis.md 的 R 列表里没有的新批评**:R4/R5 测的是"极点"(`inv`/`cs_demean`),但没有一条测"y 腿的离散度本身是否让 `cross_regbeta` 的同窗口估计系统性有偏"——如果还要在 R 里追加,这是一个文献支撑更强的方向。
4. **把"流动性水平"和"流动性贝塔(对流动性共同变动的敏感度)"当成两个必须分开命名、不能互相替代的量,是这个领域的共同底线,而且同一个"贝塔"内部还要再按"谁对谁回归"细分。** Pástor–Stambaugh [12] 把"流动性贝塔"定义为对**市场整体**流动性冲击的敏感度,与个股自身的流动性**水平**是两个独立的变量;Acharya–Pedersen [13](*JFE* 2005,77(2):375–410)把"净贝塔"拆成市场贝塔加三个流动性贝塔(自身流动性与市场流动性的协动、自身收益与市场流动性的协动、自身流动性与市场收益的协动——最后一项符号为负),**三者的符号和大小都不同**,不能混用。Chordia–Roll–Subrahmanyam [14](*JFE* 2000,56(1):3–28,"Commonality in Liquidity")给出了这类"流动性贝塔"在实证里的标准构造:**把个股流动性的变化对市场平均流动性的变化做回归**(含领先 / 滞后项,控制市场收益与波动率),这才是"流动性贝塔"在文献里唯一被反复使用的构造方式。
   翻译:对照来看,**F3 的 `cross_regbeta(day_std(Volume), cs_mask_top_replace_mean_neg(cs_robust_z(day_distinct_ratio(Volume))), 15)` 的两条腿都不是"市场整体流动性",一个是个股自己的成交量波动,一个是个股自己的交易离散度**——它表面上长得像一个"贝塔",但不是文献里任何一种标准贝塔构造(不是市场贝塔、不是 Pástor–Stambaugh 式流动性贝塔、也不是 Chordia–Roll–Subrahmanyam 式流动性共动贝塔)。这给 §1.2(4)"β 的截面排序是流动性的非单调函数"的判断再加一条文献支撑:**F3 不是在构造一个有命名的、文献认可的贝塔,只是借用了"回归斜率"这个形式**,这也直接支持 R6(判断 Volume→Amt 的字段替换是否暴露了一个藏在分母里的名义价格项)——文献的教训是**换哪两个变量进贝塔必须讲清楚机制,F3 没有讲清楚它在为哪个"市场"变量构造敏感度**。
5. **相关系数本身比波动率比更难估、更需要收缩——这给"去掉极点之后 F3 还剩什么"一个量化的预期。** Blitz–Swinkels–Ūsaitė–van Vliet [16](*Journal of Risk* 2022 年 9 月,24(6):25–44;同样把 beta 分解成相关系数 × 相对波动率两部分,并假设两者独立)发现:给相关系数更重的收缩(收缩系数 0.5)、给波动率比更轻的收缩(0.2)时预测效果最好,原因是**相关系数的估计噪声天生比波动率比大**。
   翻译:对 analysis.md 的 R1(`cross_corr` 替换 `cross_regbeta`)给出一条预期上的提醒——R1 保留的正是文献认为"更难估、更该被重度收缩"的那一半(相关系数),**R1 如果分数不低,不代表共动信息干净,可能只是换了一种噪声更大的方式继续过拟合 train**;这与 analysis.md P1/P2 的判据(score < 0.5 / < 0.8)方向一致,但提醒 PI 在解释 R1 的结果时不要把"没有极点"直接读成"信息干净"。

**搜不到的地方(明确空白,不要当成文献证伪):**
- 把"离散 / 粗网格变量"(只有几十到几百个取值)放在滚动回归的被解释变量一侧,文献对"并列 / 量化误差"的专门讨论,**搜不到**直接对口的资产定价文献;邻近的计量经济学文献(如 Hausman–Liu–Luo–Palmer 关于分位数回归中被解释变量测量误差的 2021 *Econometrica* 论文)讨论的是"被解释变量测量误差"这一大类问题,但场景是分位数回归,不是滚动窗口斜率,只能算方向性邻近,不是直接命中。
- "beta 型特征在不同实现下符号翻转"作为一个诊断方法被文献专门讨论,**搜不到**——本轮 analysis.md §1.2(3)/§0g 的"同族方向不一致 = 方向没被数据识别"这个诊断,看起来是我们自己在这一批数据上总结出来的方法学经验,不是对已发表诊断方法的复刻,值得在 notebook 里标成"本组的方法学贡献",而不是"文献已有的检查项"。
- [3] FHT 与 [1] LOT 的精确公式——已在 L1 的空白清单里记过,这里不重复。

---

## L4 — 尾盘 / 收盘集合竞价的成交份额(对准 N-β;本轮新增两篇直接针对 2018-08-20 改革的实证论文)

**能翻译成算子语言的处理方式:**

1. **"哪个半小时"本身携带可预测信息,且与量、价差、波动率的日内模式不是同一件事——这是支持"时点份额是独立信息"而不是"流动性水平的马甲"的最直接证据。** Heston–Korajczyk–Sadka [17](*JF* 2010,65(4):1369–1407,本轮重新检索确认)用 2001–2005 年 NYSE 数据发现,**某个半小时区间的收益与整数个交易日之前的同一区间收益正相关**,效应持续约 40 个交易日,在开盘和收盘半小时最强;**成交量、委托不平衡、波动率、买卖价差都呈现相似的日内模式,但它们解释不了这个收益模式**。
   翻译:直接支持 analysis.md N-β 的假设前提——`div(day_last(in_sum_rolling(Volume,30)), day_sum(Volume))` 这类"尾盘份额"要测的是一个与波动 / 流动性水平**不同维度**的量,[17] 给出了同行评审的证据基础,不是我们自己的猜测。
2. **按规模 / 流动性分组后,"尾盘占比"效应的方向会反转,不能假设单一符号——这条本轮重新检索确认,结论不变。** Bogousslavsky [18](*JFE* 2021,141(1):172–194,本轮重新检索确认)发现:套利资金对隔夜持仓的保证金 / 融券费约束,使得**小盘、低流动性股票尾盘 30 分钟收益高、隔夜收益大幅为负;大盘、高流动性股票恰好相反**。
   翻译:与 r2/lit.md 的结论一致,N-β 的方向必须按规模 / 流动性条件化,不能照抄单一符号;这与 analysis.md 把 N-β 排在 N-α 之后的理由(方向要分组才稳,纯多头 + 15bp 下尤其吃亏)一致。
3. **A 股 2018-08-20 上交所收盘集合竞价改革,本身就有直接的 DID 实证,不只是制度公告——这是本轮填的最实的一块空白。** Han–Zhao–Chen–Guo [19](*Pacific-Basin Finance Journal* 2022,74:101821,"Reexamining the impact of closing call auction on market quality: A natural experiment from the Shanghai stock exchange")用沪深 A 股 2018 年 5 月至 2019 年 1 月的日内 + 日度数据做双重差分,发现:改革对**市场流动性整体没有显著影响**;交易量从收盘时段**转移到收盘前时段**;收盘前时段的**波动率上升**;收盘价的**连续性显著改善**;价格有效性**没有明显改善**;效应在**小盘股上最明显**。Ma–Wang–Fang–Wang [20](*China Finance Review International* 2020-08,11(2):259–281,"The impact of closing mechanism changes: evidence from the Shanghai stock market")用面板回归研究同一次改革,结论方向相反地乐观:**市场质量(流动性、波动率、价格连续性)在改革后全面改善**,投资者在收盘前的连续竞价阶段**交易更激进**,集合竞价**抑制了收盘价操纵**。
   翻译:两篇用的是同一个事件(2018-08-20),但对"流动性是否改善"的结论不一致,**一致的部分是:交易行为在改革后向收盘前的连续竞价时段转移**——这直接把 r2/lit.md 留的空白("2018 年改革前后尾盘占比类特征是否有结构断点,没有查到专门研究")**部分填上**:现在有两篇直接量化这次改革对日内成交时点分布影响的论文,**结论是"有结构性变化,而且集中在小盘股",但"对流动性水平的净效应"文献本身意见不一**。这给 N-β 的制度风险提示升级:不只是"跨过一个日期要小心",而是**"跨过这个日期,尾盘份额的定义本身的经济含义在变,且这个变化在小盘股上最大、与 N-β 最关心的规模分组恰好重叠"**。
4. **交易所研究中心的报告本身证实了"集合竞价适配指数化资金"这条机制假设,同时记录了一个必须避免的操纵渠道——这条本轮把出处核实到了可引用的程度(此前 r2/lit.md 只能引用制度公告本身)。** 上海证券交易所研究中心研究报告 [21](施东晖,2006 年 9 月,《收盘集合竞价设计与股价操纵》)认为,收盘采用集合竞价既契合指数化投资的趋势,也能在市场承压时保证价格发现;同时分析了新加坡和澳大利亚交易所的两起收盘价操纵案例——操纵者在集合竞价前下大额委托,制造买卖盘失衡以影响收盘价。
   翻译:这是一份交易所研究中心的研究报告(不是同行评审论文,但符合本轮"论文 / 工作论文 / 研究报告"的口径,比 r2/lit.md 里"制度公告层面的事实"更进一步),给 N-β 的机制假设(指数再平衡 / 被动资金在收盘集中交易)提供了制度层面的依据,但也提了一个必须写进假设的风险:**尾盘成交份额异常升高的一部分来源,文献上确认过是操纵性委托,不是被动资金的正常行为**——如果种子的回看窗口短、又没有做跨日平滑,这条风险比"结构断点"更隐蔽。
5. **收盘集合竞价机制本身(不只是中国的 2018 年改革)在海外市场的引入,普遍被发现改善了收盘时段的价格发现——这给"尾盘交易是信息性的,不是纯噪声"再加一层非 A 股的背景支持。** Pagano–Schwartz [22](*JFE* 2003,68(3):439–484)研究 Euronext Paris 分阶段引入电子收盘集合竞价(1996 年先用于低流动性股票,1998 年推广到高流动性股票),发现收盘时段**价格发现改善**,对开盘时段也有较小的正向溢出。
   翻译:这是非中国市场的证据,方向支持"收盘集合竞价机制让尾盘交易更具信息性",但**机制、股票池、交易制度(T+1 等)都不同于 A 股**,只能当背景支持,不能假设幅度或符号可以照搬到 A 股的尾盘份额特征上。

**搜不到的地方(明确空白,不要当成文献证伪):**
- `day_centroid` / `day_gini` 这类连续的日内分布形状指标(而不是简单的"最后 k 分钟占比")直接预测个股未来收益的同行评审文献,**搜不到**(与 r2/lit.md 的空白一致,本轮没有新进展)。
- A 股"尾盘占比"(而不是"收盘集合竞价机制改革"本身)与次日 / 次月横截面收益关系的专门学术研究,**搜不到**——[19][20] 研究的是改革对市场质量(流动性、波动率、价格连续性、操纵)的影响,不是"尾盘占比"作为选股特征的收益可预测性。
- Bogousslavsky–Muravyev《Who Trades at the Close? Implications for Price Discovery and Liquidity》(作者简历标注"forthcoming, *Journal of Financial Markets*"):检索到会议幻灯片(2022-10-18)与一篇可能是同一项目早期版本的 2020 年研讨会标题,但**没有找到可以独立核实的首次公开日期**,按规则"拿不准日期的不用"——**不列入参考文献,只记在这里**;它的结论方向(收盘量由指数化 / ETF 资金驱动,价格发现贡献很小)与 [19][20][21] 的"被动资金 + 价格发现有限"一致,如果以后能找到可核实的日期,值得补录。
- "谁在收盘交易"(散户 / 机构 / 被动资金)在 A 股的同行评审横截面收益证据,**搜不到**(与 r2/lit.md 一致)。

---

## 参考文献

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|---|
| 1 | A New Estimate of Transaction Costs | David Lesmond, Joseph Ogden, Charles Trzcinka | 1999(*Review of Financial Studies*,Vol. 12, No. 5, pp. 1113–1141) | Review of Financial Studies | https://www.bauer.uh.edu/rsusmel/phd/lot_1999RFS.pdf | true(标题、期刊、卷期页码在多条搜索结果摘要里直接出现;PDF 为扫描件,工具无法提取公式原文,未逐页核实) |
| 2 | A Liquidity-Augmented Capital Asset Pricing Model | Weimin Liu | 2006-12(*Journal of Financial Economics*,Vol. 82, No. 3, pp. 631–671),DOI 10.1016/j.jfineco.2005.10.001 | Journal of Financial Economics | https://rpc.cfainstitute.org/-/media/documents/article/cfa-digest/2007/dig-v37-n2-4603-pdf.pdf | true(标题、卷期页码、DOI 在搜索结果中直接出现;公式细节只核实到文字描述,未核实代数式) |
| 3 | What Are the Best Liquidity Proxies for Global Research?(FHT 估计量;头条文章) | Kingsley Y. L. Fong, Craig W. Holden, Charles A. Trzcinka | *Review of Finance*,Vol. 21, No. 4(头条文章);FHT 估计量工作论文版本约 2014 年流传,确切首发年份未能在搜索结果中精确核实 | Review of Finance | https://host.kelley.iu.edu/cholden/Fong%20Holden%20and%20Trzcinka%20(2017).pdf | true(标题、作者、期刊卷期在搜索结果中出现;确切出版年份与页码范围未能逐一核实,按本条备注处理) |
| 4 | Do Liquidity Measures Measure Liquidity? | Ruslan Goyenko, Craig Holden, Charles Trzcinka | 2009(*Journal of Financial Economics*,Vol. 92, pp. 153–181) | Journal of Financial Economics | https://www.icmagroup.org/assets/documents/Regulatory/Secondary-markets/Bond-Market-Liquidity-Library/Goyenko-RY_Holden-CW_Trzcinka-CA---2009---Do-liquidity-measures-measure-liquidity-290118.pdf | true |
| 5 | Illiquidity and Stock Returns: Cross-section and Time-series Effects | Yakov Amihud | 2002(*Journal of Financial Markets*,Vol. 5, No. 1, pp. 31–56) | Journal of Financial Markets | https://www.cis.upenn.edu/~mkearns/finread/amihud.pdf | true |
| 6 | Statistical Inferences for Price Staleness | Aleksey Kolokolov, Giulia Livieri, Davide Pirino | 2020(*Journal of Econometrics*,Vol. 218, No. 1, pp. 32–81) | Journal of Econometrics | https://ricerca.sns.it/retrieve/e3aacdfd-f331-4c98-e053-3705fe0acb7e/MS2018440_Kolokolovetal.pdf | true |
| 7 | Unknown Unknowns: Uncertainty About Risk and Stock Returns(工作论文题目:Unknown Unknowns: Vol-of-Vol and the Cross Section of Stock Returns) | Guido Baltussen, Sjoerd van Bekkum, Bart van der Grient | 2018(*Journal of Financial and Quantitative Analysis*,Vol. 53, No. 4),DOI 10.1017/S0022109018000480 | Journal of Financial and Quantitative Analysis | https://personal.eur.nl/baltussen/ ; https://personal.eur.nl/vanbekkum/2018JFQA_unknown_unknowns.pdf | true(本轮重新检索确认,与 r2/lit.md 的核实结果一致) |
| 8 | Betting Against Beta | Andrea Frazzini, Lasse H. Pedersen | 工作论文 draft 2013-05-10(NBER WP 16601);正式发表 2014(*Journal of Financial Economics*,Vol. 111, No. 1, pp. 1–25) | Journal of Financial Economics / NBER | https://static1.squarespace.com/static/5e6033a4ea02d801f37e15bb/t/5f5a8f8657f86f3c596958d8/1599770505417/BettingAgainstBeta.pdf | true(直接读取 PDF 全文「Estimating Ex-ante Betas」一节原文,逐字核实了 β=ρ·σ_i/σ_m 分解、1 年/5 年窗口、Vasicek 收缩 w=0.6 等细节) |
| 9 | A Note on Using Cross-sectional Information in Bayesian Estimation of Security Betas | Oldrich A. Vasicek | 1973-12(*Journal of Finance*,Vol. 28, No. 5, pp. 1233–1239) | Journal of Finance | https://ideas.repec.org/r/bla/jfinan/v28y1973i5p1233-39.html | true(标题、卷期页码在搜索结果中确认;并在 [8] 的参考文献列表原文中逐字读到同一条引用) |
| 10 | Risk Measurement When Shares Are Subject to Infrequent Trading | Elroy Dimson | 1979-06(*Journal of Financial Economics*,Vol. 7, No. 2, pp. 197–226) | Journal of Financial Economics | https://ideas.repec.org/a/eee/jfinec/v7y1979i2p197-226.html | true |
| 11 | Estimating Betas from Nonsynchronous Data | Myron Scholes, Joseph Williams | 1977(*Journal of Financial Economics*,Vol. 5, No. 3, pp. 309–327) | Journal of Financial Economics | — | true(在 [8] 的参考文献列表原文中逐字读到此条引用) |
| 12 | Liquidity Risk and Expected Stock Returns | Ľuboš Pástor, Robert F. Stambaugh | 2003(*Journal of Political Economy*,Vol. 111, pp. 642–685) | Journal of Political Economy | https://www.johnhcochrane.com/s/pastor_stambaugh_jpe.pdf | true(搜索结果确认,并在 [8] 的参考文献列表原文中逐字读到同一条引用) |
| 13 | Asset Pricing with Liquidity Risk | Viral V. Acharya, Lasse H. Pedersen | 2005(*Journal of Financial Economics*,Vol. 77, No. 2, pp. 375–410) | Journal of Financial Economics | https://archive.nyu.edu/bitstream/2451/27289/2/wpa03044.pdf | true |
| 14 | Commonality in Liquidity | Tarun Chordia, Richard Roll, Avanidhar Subrahmanyam | 2000(*Journal of Financial Economics*,Vol. 56, No. 1, pp. 3–28),DOI 10.1016/S0304-405X(99)00057-4 | Journal of Financial Economics | https://doi.org/10.1016/S0304-405X(99)00057-4 | true |
| 15 | Common Factors in Prices, Order Flows, and Liquidity | Joel Hasbrouck, Duane J. Seppi | 2001-03(*Journal of Financial Economics*,Vol. 59, No. 2/3, pp. 383–411);工作论文版本(NYU FIN-99-011)1998 年流传 | Journal of Financial Economics | https://ideas.repec.org/a/eee/jfinec/v59y2001i3p383-411.html | true(标题、卷期页码在搜索结果中确认;仅作为"over-differencing 导致残差自相关"这条方法学提醒的间接引用,未核实原文论证细节) |
| 16 | Shrinking Beta | David Blitz, Laurens Swinkels, Kristina Ūsaitė, Pim van Vliet | 2022-09(*Journal of Risk*,Vol. 24, No. 6, pp. 25–44) | Journal of Risk | https://www.econbiz.de/Record/shrinking-beta/10013549669 ; https://pure.eur.nl/en/publications/shrinking-beta/ | true |
| 17 | Intraday Patterns in the Cross-Section of Stock Returns | Steven L. Heston, Robert A. Korajczyk, Ronnie Sadka | 2010(*Journal of Finance*,Vol. 65, No. 4, pp. 1369–1407),DOI 10.1111/j.1540-6261.2010.01573.x | Journal of Finance | https://arxiv.org/pdf/1005.3535 | true(本轮重新检索确认,与 r2/lit.md 的核实结果一致) |
| 18 | The Cross-Section of Intraday and Overnight Returns | Vincent Bogousslavsky | 2021(*Journal of Financial Economics*,Vol. 141, No. 1, pp. 172–194),DOI 10.1016/j.jfineco.2020.07.020 | Journal of Financial Economics | https://doi.org/10.1016/j.jfineco.2020.07.020 | true(本轮重新检索确认,与 r2/lit.md 的核实结果一致) |
| 19 | Reexamining the Impact of Closing Call Auction on Market Quality: A Natural Experiment from the Shanghai Stock Exchange | Qian Han, Chengzhi Zhao, Jing Chen, Qian Guo | 2022(*Pacific-Basin Finance Journal*,Vol. 74, Art. 101821),DOI 10.1016/j.pacfin.2022.101821 | Pacific-Basin Finance Journal | https://ideas.repec.org/a/eee/pacfin/v74y2022ics0927538x22001160.html | true |
| 20 | The Impact of Closing Mechanism Changes: Evidence from the Shanghai Stock Market | Dan Ma, Chunfeng Wang, Zhenming Fang, Ziwei Wang | 2020-08(*China Finance Review International*,Vol. 11, No. 2, pp. 259–281),DOI 10.1108/CFRI-04-2020-0041 | China Finance Review International | https://ideas.repec.org/a/eme/cfripp/cfri-04-2020-0041.html | true |
| 21 | 收盘集合竞价设计与股价操纵 | 施东晖 | 2006-09(上海证券交易所研究中心研究报告) | 上海证券交易所研究中心 | https://www.sse.com.cn/ (原始报告链接未在搜索结果中直接给出,来源标题 / 作者 / 机构 / 日期在搜索结果摘要中核实) | true(标题、作者、机构、年-月在搜索结果摘要中直接出现;未读到报告原文全文) |
| 22 | A Closing Call's Impact on Market Quality at Euronext Paris | Michael Pagano, Robert A. Schwartz | 2003(*Journal of Financial Economics*,Vol. 68, No. 3, pp. 439–484) | Journal of Financial Economics | https://academicnewsletter.sufe.edu.cn/info/357720 | true |
| 23 | Does Persistence in Idiosyncratic Risk Proxy Return-Reversals? | Harmindar B. Nath, Vasilis Sarafidis | 2017(*Journal of Banking and Financial Economics*,华沙大学系列,Vol. 2, Iss. 8, pp. 27–53),DOI 10.7172/2353-6845.jbfe.2017.2.2 | Journal of Banking and Financial Economics | https://press.wz.uw.edu.pl/jbfe/vol2017/iss8/2 | true(卷期标注在不同来源间有出入——DOI 显示 2017.2.2,RePEc 显示 v2y2017i8,已如实记录两种标注;仅作为弱 / 邻近证据使用,见 L2 正文) |
| 24 | Idiosyncratic Volatility and Equity Returns: UK Evidence | Timotheos Angelidis, Nikolaos Tessaromatis | 2008-06(*International Review of Financial Analysis*,Vol. 17, No. 3, pp. 539–556) | International Review of Financial Analysis | https://ideas.repec.org/a/eee/finana/v17y2008i3p539-556.html | true(仅作为弱 / 邻近证据使用,见 L2 正文;论文摘要未明确给出"持续性"结论的具体数值,只核实了"控制持续性后结果依然显著"这句话) |

---

## 本轮与 r2 的差异(供 PI 核对)

- L2、L4 各有一篇"骨架"文献([7] Baltussen、[17] Heston–Korajczyk–Sadka、[18] Bogousslavsky)与 r2/lit.md 重复,**本轮重新检索确认过一次**,不是直接照抄;结论与 r2 一致,写在正文里标明"本轮重新检索确认"。
- L4 新增 [19][20][21][22] 四篇,**把 r2/lit.md 留下的"2018 年改革前后尾盘占比是否有结构断点,没有查到专门研究"这个空白部分填上**:现在有两篇直接做了 2018-08-20 改革的实证([19][20],结论对流动性净效应意见不一,但都确认交易量在改革后向收盘前时段转移),以及一篇交易所研究中心报告([21],机制依据 + 操纵风险)和一篇非 A 股的机制背景([22])。
- L1、L3 是全新检索,不与 r1/r2 的任何题目重叠。L3 是本轮信息密度最高的一节——直接读到 Frazzini–Pedersen [8] 论文正文,确认了 analysis.md §0a 的 `β=corr·σ_y/σ_x` 分解是标准文献写法,也确认了"裸斜率当特征用"在文献里从未出现过,这给核心 A / N-α / R 系列的合理度评分提供了比 r1/r2 更硬的文献支撑。
- 两处本想核实但没有核实到、因此**没有写进参考文献**的线索,专门记录一下避免以后重复花时间搜:(a)1997–2005 年 A 股五指标流动性溢价研究的完整出处(来源页面 403,只有摘要);(b)Bogousslavsky–Muravyev《Who Trades at the Close?》的可核实公开日期(作者简历标注"forthcoming",没有找到独立可核实的首发时间)。
