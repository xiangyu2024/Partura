# 文献:种子 803,B 组,第 3 轮(末轮,文献员)

查的题目来自 `r3/analysis.md` §5 的 L1–L4。本轮四题换的是轴(不重复 r1 的「日内高阶矩与不交易」「尾部统计量的日内稳健估计」「条件分组与 A 股涨跌停」「顺序信息与成交钟」,也不重复 r2 的「已实现方差序列的形状」「正值序列不对称的各种写法」「日内成交 / 波动的时点与收盘集合竞价」「给定市值后的名义价格」):
L1 对准核心①(`ts_skew(day_durbin_watson(Open),50)`)与本轮 E 的产出——**一个异象的溢价随流动性 / 换手条件反转**,方法论上怎么度量、怎么检验;
L2 对准核心③与 N-A——**隔夜收益的分布形状(偏度)**在截面上值不值钱,怎么处理;
L3 对准核心①的内容——**孤立的爆波动日**(频率 vs 严重度)怎么度量,为什么稳健化会杀死它;
L4 对准核心②——**收盘前半小时**成交与波动的时点错位,`abs(r)` 与 `r²` 的稳健性,领先滞后。

只用这次工具(WebSearch / WebFetch)实际检索到、能确认首版日期早于 **2023-08-08** 的论文 / 工作论文 / 研究报告(arXiv / SSRN 以首版 / 最早可确认版本为准);拿不准日期的不用,在正文或出处表里如实写"搜不到"或"日期不确定,弃用"。下面每条处理方式后用 `[Sx]` 指向文末出处表;`verified: true` = 这次搜索结果或抓取页面上确实看到了标题、作者、年份、出处(个别条目的完整作者名单或最终发表细节未逐一核实,在条目里单独注明)。本轮续用 r1(S1–S20)、r2(S21–S38)的编号,从 **S39** 开始。

---

## L1 —— 对准核心①与本轮 E:异象溢价随流动性 / 换手条件反转,怎么度量、怎么检验

**能翻译成算子语言的处理方式:**

1. **把条件变量当第二维分组轴(双重排序),而不是线性控制**,是文献里系统比较过的做法。Müller & Schmickler(2020-07 工作论文,后发表为 *Review of Asset Pricing Studies* 2025)穷举了 102 个已知异象之间全部 10,302 种双重排序组合,发现大量组合在多重检验之后依然显著,**交互收益最大的组合几乎总是一个"交易摩擦类"异象(规模、短期反转、流动性)去配对另一个异象**,且效应在 2000 年后逐渐从"反转类"转移到"盈利类 + 摩擦类"的组合。→ 直接对应我们这个 1.41 分 head 的构造:成交额分桶(高/低)正是一个"交易摩擦类"条件,核心①的溢价在这一维上反转,与文献里"交互收益集中在摩擦类异象"这条大样本规律方向一致。**要如实指出**:这篇论文的双重排序是分桶再比较组合收益,不是我们"两个居中秩相乘"这种连续交互项,构造形式不同,只是方法论大类相同;而且其正式发表版本(RAPS 2025)晚于 2023-08-08,本条只能引用 2020-07 的工作论文版本,发表版本的具体数字不作为证据。[S39]
2. **套利不对称(arbitrage asymmetry)框架,提供了"同一个风险因子在两端表现不对称"的扎实先例,但条件变量不是流动性本身**。Stambaugh, Yu & Yuan(2015,*Journal of Finance*;NBER WP 18560,2012)证明特质波动率(IVOL)异象的负向关系来自"做空比做多更难"这条摩擦不对称:用 11 个已知异象合成一个错误定价指数分组后,IVOL 的负向效应集中在**被高估**的一端,在被低估的一端是正向且更弱。**要如实指出翻译上的落差**:这篇的条件变量是一个复合错误定价分数,不是成交额 / 换手率 / 流动性本身,所以它支持"异象溢价可以在两端不对称甚至反向"这个大方向,但**不能直接当作"成交额当条件变量"这一具体设计的先例**——这是本题问题 2 里"散售占比 / 套利限制"这条解释路径最接近的证据,但也只是接近,不是精确对应。[S40]
3. **成交额与换手率的波动性本身被检验过是不是定价变量,但没有看到"谁更适合当条件变量"的直接比较**。Chordia, Subrahmanyam & Anshuman(2001,*Journal of Financial Economics* 59(1):3–32)发现"美元成交额的波动性"与"股数换手率的波动性"都与未来收益显著负相关,控制规模、账面市值、动量、交易活跃度水平后依然成立,而且这个符号与他们原先的假设方向相反。**这篇论文测的是"成交活跃度的波动性"当成一个独立异象,不是"用当日成交额 vs 当日成交量当另一个异象的条件变量"**,所以它不能回答本题问题 3(为什么我们把成交额换成成交量,交互头从 +1.41 塌到 −0.08)。[S41]
4. **"线性中性化拿不掉交互项"这件事,没有找到专门在因子 / 异象构造语境下讨论它的金融文献**。这本身是线性回归残差的数学性质(OLS 投影只能移除与控制变量线性相关的部分),但把它明确当成"交互项是不是真的新信息、还是只是控制集合的非线性"这个质疑、并在异象检验的语境下讨论的论文,这次没有搜到。

**搜不到 / 弃用的部分**:(a) 没有找到专门比较"双重排序 / Fama-MacBeth 交互项 / 条件加权构造"这三种条件化方法、结论是否一致的论文——Müller & Schmickler 用的是双重排序框架,没有和 FM 交互项做横向对比;(b) 没有找到直接回答"成交额(金额)vs 成交量(股数)vs 换手率(金额/市值)哪个当条件变量更好"的论文;(c) 没有找到在选股 / 因子构造语境下明确提出"线性中性化移除不了交互项"这条方法论警告的金融文献,只有本题末尾的数学性质本身,不编造论文来源。

---

## L2 —— 对准核心③与 N-A:隔夜收益的分布形状在截面上值不值钱,怎么处理

**能翻译成算子语言的处理方式:**

1. **把收益拆成隔夜 / 日内两段分别检验已知异象的溢价集中在哪一段,是成熟且持续在做的方法,但检验的是收益水平,不是收益的分布形状**。Lou, Polk & Skouras(2019,*Journal of Financial Economics* 134(1):192–213;更早版本见 2015–2018 的 LSE/FMG 工作论文)把 14 个经典异象的收益拆成隔夜段与日内段,发现**9 个异象的全部溢价都落在日内段**,动量与反转的溢价主要落在隔夜段,且这个"错配"持续多年。Bogousslavsky(2021,*Journal of Financial Economics* 141(1):172–194;更早的 EPFL 学位论文 / 工作论文版本)发现规模与流动性溢价几乎全部在**最后半小时**实现,而盈利能力与特质波动率溢价是全天逐步累积的,且一个错误定价因子全天为正、收盘前变差。**要如实指出翻译上的落差**:这两篇都是把"某个已知异象的平均收益"按时段拆分,检验的是**均值**在哪一段出现,**没有一篇检验隔夜收益这条序列本身的偏度 / 峰度**当作独立的截面预测变量——这正是我们 1.16 分 head 要做的事,文献目前没有直接先例。[S42][S43]
2. **已实现偏度确实被当独立变量检验过,但度量的对象和我们不是同一条序列**。Amaya, Christoffersen, Jacobs & Vasquez(2015,*Journal of Financial Economics*,DOI 10.1016/j.jfineco.2015.02.009;更早版本 2011–2013 年的 CREATES 工作论文)用**单日内**的高频收益算出当天的已实现偏度 / 峰度,再按周排序,发现已实现偏度与下一周收益显著负相关(做多低偏度),已实现峰度正相关,两者都扛得住 Fama-French-Carhart 因子。**要如实指出这条不是直接对应物**:这篇的偏度是"一天之内、跨多个高频收益点"算出来的横截面(时间上)统计量,我们的核心③是"50 个交易日、跨多天的隔夜收益"这条序列的偏度,维度完全不同(他们是日内维度,我们是跨日维度)。两者唯一的共同点是都用三阶矩,**不能把他们的"做多低偏度"结论直接套到我们的隔夜偏度头上**——这恰好能解释为什么我们核心③的方向(做多高偏度)和核心①、和这篇文献都不一致:它们本来就不是同一个统计对象。[S44]
3. **A 股特有的开盘涨跌停,确实会在开盘价上制造机械的极端值,有直接的实证**。Wu, Wang & Li(2017,*Physica A* 465:464–471)用全部 A 股样本发现,开盘即触及涨跌停之后,后续收益呈"W 形",意味着次日再次触及涨跌停的概率明显抬高,且这个形态随市场整体涨跌趋势变化。**这篇不是直接测隔夜收益偏度**,但给出了一个机械来源:开盘涨跌停本身会在隔夜收益序列里制造出孤立的、极端的观测点(今开对昨收直接跳停),这与核心③、以及核心①"孤立爆波动日"的描述高度吻合,是一条值得写进笔记的机械解释候选,而不是对隔夜偏度异象本身的直接检验。[S55]
4. **散户注意力的代理变量存在,但没有直接和隔夜收益连起来**。Gao, Xiong, Feng, Li & Vigne(2019,*Finance Research Letters* 29:411–417)用东方财富股吧每只股票帖子的日度异常阅读量构造注意力代理,在沪市样本上发现它与同期更高收益、后续反转相关,且与不同类型投资者的交易行为有关。**这篇测的是全天的收益,没有把隔夜段单独拎出来**,所以它只能支持"散户注意力这个机制在 A 股真实存在、和收益有关",不能直接证明"隔夜收益由散户的隔夜委托驱动"这条具体假说。[S56]
5. **50 个隔夜观测算三阶矩,小样本滚动偏度的稳定性要怎么处理**,这次仍然没有搜到专门文献——这是本题第三轮被问到的同一个开放问题(r1 问过日内估计量的稳健化、r2 的 L2 问过取数值而非窗口长度的稳健化写法,都没有解决"窗口该多长"这个工程问题)。

**搜不到 / 弃用的部分**:没有找到任何论文直接检验"隔夜收益序列自身的滚动偏度"当截面预测变量(Amaya 等人测的是日内偏度,不是跨日的隔夜收益偏度);没有找到把"按涨跌停幅度缩放跳空""剔除停牌复牌日""开盘集合竞价价格 vs 前收"这几种具体工程处理方式做过系统比较的论文;没有找到小样本(窗口 ≈ 50)滚动偏度在金融时间序列语境下的稳定性指南。这些都如实标注为空白,不替 PI 编造。

---

## L3 —— 对准核心①的内容:孤立的爆波动日怎么度量,为什么稳健化会杀死它

**能翻译成算子语言的处理方式:**

1. **"反过来用"跳跃鲁棒估计量,确实是文献里数跳跃的标准思路,而且有一整套工具链**。Barndorff-Nielsen & Shephard(2004,*Journal of Financial Econometrics* 2(1):1–37)提出已实现双幂变差(bipower variation),证明它对稀疏跳跃近似不敏感,于是"已实现方差 − 双幂变差"就能分离出跳跃部分,这是这整条文献的起点。Andersen, Dobrev & Schaumburg(NBER WP 15533,2009;正式发表于 *Journal of Econometrics*,2012)在此基础上提出 MedRV / MinRV,用三个相邻绝对收益的中位数 / 两两取最小值,比双幂变差效率更高、对"零收益"(停牌 / 报价不动)更稳健,仍保留局部窗口的性质以应对日内波动的周期形态。Lee & Mykland(2008,*Review of Financial Studies* 21(6):2535–2563)给出一个非参数检验,直接定位跳跃发生的时点与幅度,应用在美股个股上发现个股跳跃多数对应公司自身的预定公告(盈利发布等),指数跳跃多数对应宏观消息。→ 可翻译的处理方式:用"原始已实现方差(或其代理)减去任一种跳跃鲁棒估计量"得到一个跳跃强度序列,再对这条序列取偏度 / 做分布统计,这与我们"对 `day_var(Ret)` 这种非跳跃鲁棒的日频代理直接取 50 日偏度"是同一条逻辑的更精细版本,只是我们没有日内数据,无法真正分离跳跃部分,只能用日频代理整体的分布形状去逼近。[S47][S46][S48]
2. **这套跳跃度量确实被直接用在个股截面选股上,而且扛得住和我们一样的高阶矩控制**。Amaya & Vasquez(2011-01 工作论文,EFMA 2011 Braga 年会论文)用高频数据算出个股的"平均跳跃幅度"(已实现方差与双幂变差之差),按周把个股分成十个组,发现**多跳跃组显著跑输少跳跃组**,这条负向价差在控制了上一周收益、已实现波动率、已实现偏度、已实现峰度之后依然显著为负。这是本题找到的、方法论上最贴近我们核心①的一篇:它证明"跳跃 / 爆波动代理可以单独放进个股截面选股,并且扛得住其它高阶矩控制",与我们核心①"扛住已知族五条控制"的结构是同一类证据。**要如实指出**:它用的是高频数据直接算跳跃,不是我们这种日频代理的分布形状,构造层级不同。[S45]
3. **频率(多久一次)与严重度(多大)被明确分开检验过,中国市场也在样本里**。Kshatriya & Prasanna(2020,*International Review of Finance* 20(3):581–604)用一个带跳跃的随机波动率模型分别估计跳跃**幅度**与跳跃**强度**(频率),再用 Fama-MacBeth 回归在印度、中国(上证综指成分股)、韩国、日本四个市场里分别检验,发现**幅度与强度都显著定价**,但各市场的经济幅度差异很大(中国约对应年化 2% 的预期收益差)。Zhou & Zhu(2011,*Journal of Economics and Finance* 35(3):309–331)与 Chao, Liu & Guo(2017,*PLOS ONE* 12(8):1–14)都在中国股市样本上专门检验了(带符号的)已实现跳跃风险对截面收益的解释力。→ 可翻译的处理方式:核心①目前用单一的 `ts_skew` 统计量混合编码了"出现过多少次极端日"(频率)与"极端到什么程度"(严重度)两条信息,文献给出的具体做法是**把这两条拆成两个独立的算子**(一个"超过自身历史 k 倍标准差的天数占比"当频率腿,一个"超过阈值那几天的平均幅度"当严重度腿),分别检验、必要时再做交互,而不是用一个三阶矩数字同时编码两件事。[S50][S51][S52]
4. **"稳健化为什么会杀死这类信号"这句话本身,没有找到哪篇论文用这个措辞明确讲过,但可以从跳跃鲁棒估计量的设计目标直接推出来,不是我们编的**。双幂变差 / MedRV / MinRV 这些估计量,**设计目标本身就是让跳跃部分对估计值的贡献尽量小**(这是它们"鲁棒"的定义),所以对这些量取三阶矩,天然比对原始已实现方差取三阶矩少了跳跃信息。这是从 [S47][S46] 的方法本身能推出的逻辑结论,而不是另一篇独立论文的实证发现——要把这一点如实标注给 PI,不能包装成"有文献证明过"。
5. **波动(或波动形状)的持续性,被当成独立的截面变量检验过,但度量的是水平的持续性,不是形状的持续性**。Simlai(2014,*International Review of Financial Analysis* 33:253–261)构造一个"事前波动率的持续性"组合层面指标,发现它对截面平均收益有很强的预测力,并且在价值股和成长股之间制造出显著的收益差。**要如实指出翻译上的落差**:这是波动率**水平**本身的 AR 持续性系数当因子,不是我们核心①顶头 `cross_autocorr_s1(偏度序列, 6)` 那种"偏度这个形状统计量自己在短窗口里连贯不连贯",对象不同(水平的持续性 vs 形状的持续性),但方法论上是最接近的先例:都是"把一个风险度量自身的时间序列特性(而不是它的水平)当成新的截面特征"。[S53]

**搜不到 / 弃用的部分**:没有找到任何论文明确说过"这类异象的信息恰恰在被稳健估计量丢掉的那几个极端观测里"这句话本身(§3 第 4 条已如实说明这是推论,不是引用);没有找到专门针对"日频 OHLC 代理(不是高频数据)的跳跃 / 爆波动度量"在个股截面选股上的检验——现有文献(Amaya & Vasquez、Kshatriya & Prasanna 等)全部基于高频 / 期权数据估计跳跃,我们只有日频字段,这是一个真实的构造局限,不是能靠换算子解决的问题。

---

## L4 —— 对准核心②:收盘前半小时的成交与波动错位

**能翻译成算子语言的处理方式:**

1. **"溢价集中在最后半小时"这件事本身有直接先例,但要搭配一条重要的反例一起看**。Bogousslavsky(2021,*Journal of Financial Economics* 141(1):172–194;size/illiquidity 的"最后 30 分钟"这个具体措辞来自更早的工作论文 / EPFL 学位论文版本,**最终发表版本的摘要里只确认了"全天为正、收盘表现差"这个大结论,没有在本次检索到的摘要片段里逐字确认 size/illiquidity 的 30 分钟措辞**,这点要向 PI 说清楚,不要当成发表版本的逐字结论)发现小盘股与低流动性股票的溢价几乎全部在收盘前最后半小时实现,而盈利能力与特质波动率溢价是全天逐步累积的。**反例必须一起写**:Heston, Korajczyk & Sadka(2010,*Journal of Finance* 65(4):1369–1407)发现个股收益在"恰好相隔整数个交易日的同一个半小时时段"上有显著正自相关,持续约 40 个交易日,且这个效应在开盘和收盘半小时更明显;但他们**明确测过**成交量、委托不平衡、波动率、买卖价差在日内的周期形态和收益的周期形态很像,却**解释不了**收益的周期模式。→ 要如实提醒 PI:"成交 / 波动的时点形态像,不代表它能解释收益的时点形态",这是对核心②因果故事的一条独立、直接的警告,不是支持证据。[S43][S54]
2. **`abs(r)` 比 `r²` 更不容易被单根大阳线 / 大阴线主宰,这是幂次变差(power variation)理论的直接结果,不是我们猜的**。Barndorff-Nielsen & Shephard(2004)的幂次变差框架表明,**阶数 p < 2 的幂次变差(例如 p = 1,即绝对收益)比 p = 2(平方收益,即已实现方差本身)对稀疏的大跳跃明显更不敏感**——这正是双幂变差能够鲁棒的数学基础。→ 直接翻译:我们"波动时点那一腿用 `abs(r)` 存活、用 `r²` 直接报废(掉 1.00)"这个结果,和幂次变差理论预测的方向完全一致:**一根大阳线 / 大阴线会在 `r²` 版本的"波动集中在哪个时段"统计量里占据不成比例的权重,而在 `abs(r)` 版本里权重要小得多**。[S47]
3. **成交时点领先波动时点(还是反过来),理论上取决于知情交易者占比,这给核心②的外围提供了一个可操作的分组变量**。Zhang, Bi & Shen(2016,*Physica A* 467:345–355)的连续双向拍卖市场仿真发现,**成交量与收益波动率之间的领先滞后关系,在"知情交易者数量与非知情交易者数量大致相当"时最强,知情交易者占比继续升高后,领先滞后关系减弱、同期相关性反而更突出**。**要如实指出这是仿真模型,不是实证检验**,但它给出一个可翻译的、具体的外围变量方向:核心②(成交时点 vs 波动时点之差)的效应强弱,理论上应该随"这只股票的知情交易者占比"这个不可直接观测的量变化,而成交额 / 换手率 / 机构持仓比例这类我们能拿到的代理变量,可以当作它的间接外围特征去检验这条假说,而不是盲目分组。[S58]
4. **A 股尾盘拉抬 / 做收盘价,目前只搜到监管案例通报,没有搜到同行评审的学术研究**。中文检索命中的是一个具体的尾市操纵监管案例(投资者在减持前一日尾盘三分钟内把股价从 29.35 元拉到 30 元收盘,次日全部卖出,被认定操纵市场),这是监管机构的案例说明,**不是学术论文,不列入出处表**。能找到的学术证据全部来自境外市场:Comerton-Forde & Putniņš(2014,*Review of Finance* 18(1):23–66;更早的工作论文版本标注 2012-10-08)估计约 1% 的收盘价存在被操纵的统计特征,信息不对称程度高、流动性中等或偏低的股票最容易被操纵,操纵集中在月末 / 季末附近——这条"中等或偏低流动性更容易被操纵"的结论,如果放到核心②上,意味着"尾盘成交 / 波动错位"这个信号本身可能混进了一部分操纵痕迹,而不是纯粹的微结构效应,这点要写进对核心②结果的解读警告里。[S57]
5. **指数 / ETF 收盘再平衡在收盘时段制造异常放量,但这是机构 / 实务研究,学术文献里的严格度量没搜到**。多条检索结果(Dimensional、Research Affiliates、Eastspring 等资产管理机构的研究笔记)一致描述"指数成分股调整生效当天,收盘集合竞价阶段成交量异常放大(不同指数 8–27 倍),价格在再平衡当天小幅走高、次日开盘小幅反转"这个现象,但**这些是资产管理机构的研究笔记,不是同行评审论文,且具体数字的首发日期这次没能逐一核实**,按规矩不列入出处表,只作为"收盘放量不只来自我们核心②描述的机制"这条提醒写给 PI,不当作引用证据。

**搜不到 / 弃用的部分**:没有找到 A 股尾盘拉抬 / 做收盘价的同行评审学术研究(只有境外市场的 Comerton-Forde & Putniņš,和国内监管案例通报,两者性质不同,不能互相替代);没有找到把"成交时点与波动时点之差"直接构造成个股截面因子并检验过的论文(与 r2 的 L3 结论一致,这仍然是文献空白,不是复刻已知异象);Zhang, Bi & Shen 的领先滞后机制是仿真模型的预测,不是对任何真实股票截面做过的实证检验,这点已在正文里标注,不要被 PI 误读成实证证据。

---

## 出处(按正文出现顺序编号,`verified` 均为本次搜索 / 抓取中实际看到;续用 r1/r2 的编号,从 [S39] 开始)

[S39] Robert F. Stambaugh, Jianfeng Yu, Yu Yuan. 2015. "Arbitrage Asymmetry and the Idiosyncratic Volatility Puzzle." *Journal of Finance*, 70(5), 1903–1948. DOI 10.1111/jofi.12286;更早版本 NBER Working Paper No. 18560(2012-11),https://www.nber.org/papers/w18560 。verified: true

[S40] Karsten Müller, Simon Schmickler. 2020-07(工作论文,SSRN 3646417;正式发表为 *Review of Asset Pricing Studies*,2025,15(2),162–216,本条只引用 2020-07 的工作论文内容,发表版本晚于 2023-08-08 截止日不作为证据). "Interacting Anomalies." 工作论文日期经二级来源确认:CXO Advisory 文章(发布于 2020-08-27,文中称其为"a July 2020 paper"并给出 SSRN 链接 papers.ssrn.com/sol3/papers.cfm?abstract_id=3646417),https://cxoadvisory.com/?p=34406 ;正式发表记录(供核对期刊信息,不作为日期依据):https://ideas.repec.org/a/oup/rasset/v15y2025i2p162-216..html 。verified: true(经二级来源确认工作论文日期与 SSRN 编号;直接抓取 SSRN 页面被拒绝 403,未能一次来源同时核实摘要原文,建议 PI/检查二次核实)

[S41] Tarun Chordia, Avanidhar Subrahmanyam, V. Ravi Anshuman. 2001. "Trading Activity and Expected Stock Returns." *Journal of Financial Economics*, 59(1), 3–32. DOI 10.1016/S0304-405X(00)00080-5。IDEAS 记录:https://ideas.repec.org/a/eee/jfinec/v59y2001i1p3-32.html 。verified: true

[S42] Dong Lou, Christopher Polk, Spyros Skouras. 2019. "A Tug of War: Overnight versus Intraday Expected Returns." *Journal of Financial Economics*, 134(1), 192–213. DOI 10.1016/j.jfineco.2019.03.011;更早工作论文版本(2015–2018)见 https://personal.lse.ac.uk/polk/research/TugOfWar.pdf 与 FMG Discussion Paper DP744,https://www.fmg.ac.uk/sites/default/files/publications/DP744.pdf 。verified: true

[S43] Vincent Bogousslavsky. 2021. "The Cross-Section of Intraday and Overnight Returns." *Journal of Financial Economics*, 141(1), 172–194. DOI 10.1016/j.jfineco.2020.07.020。正式发表摘要确认来源:https://ideas.repec.org/a/eee/jfinec/v141y2021i1p172-194.html ;"size/illiquidity 在最后 30 分钟实现"这条具体措辞来自更早的工作论文 / EPFL 学位论文版本(https://infoscience.epfl.ch/record/229415/files/EPFL_TH7785.pdf ,2016 前后的研讨会记录亦印证同一表述,https://memento.epfl.ch/event/the-cross-section-of-intraday-and-overnight-return )。verified: true(正式发表的期刊信息与核心结论确认;size/illiquidity 30 分钟这条细节只在工作论文 / 学位论文版本确认,未在本次检索到的发表版摘要片段里逐字核对,引用时需注明版本)

[S44] Diego Amaya, Peter Christoffersen, Kris Jacobs, Aurelio Vasquez. 2015. "Does Realized Skewness Predict the Cross-Section of Equity Returns?" *Journal of Financial Economics*. DOI 10.1016/j.jfineco.2015.02.009;更早工作论文版本见 CREATES Research Paper 2013-41(2013-02-21),https://repec.econ.au.dk/repec/creates/rp/13/rp13_41.pdf 。verified: true

[S45] Diego Amaya, Aurelio Vasquez. 2011-01(工作论文,EFMA 2011 Braga 年会论文). "Explaining Stock Returns with Intraday Jumps." https://www.efmaefm.org/0efmameetings/EFMA%20ANNUAL%20MEETINGS/2011-Braga/papers/0307.pdf (PDF 元数据创建日期 2011-01-14 已核实;标题、方法与核心结论经搜索结果摘要确认,未直接解压 PDF 正文核对逐字细节)。verified: true

[S46] Torben G. Andersen, Dobrislav Dobrev, Ernst Schaumburg. 2009(NBER Working Paper No. 15533);正式发表版本 *Journal of Econometrics*,2012. "Jump-Robust Volatility Estimation Using Nearest Neighbor Truncation." NBER:https://www.nber.org/papers/w15533 ;SSRN:https://papers.ssrn.com/abstract=1510523 。verified: true

[S47] Ole E. Barndorff-Nielsen, Neil Shephard. 2004. "Power and Bipower Variation with Stochastic Volatility and Jumps." *Journal of Financial Econometrics*, 2(1), 1–37. DOI 10.1093/jjfinec/nbh001。确认来源:https://academic.oup.com/jfec/article/2/1/1/960705 ,工作论文版本 https://www.nuff.ox.ac.uk/economics/papers/2003/w18/eric.pdf 。verified: true

[S48] Suzanne S. Lee, Per A. Mykland. 2008. "Jumps in Financial Markets: A New Nonparametric Test and Jump Dynamics." *Review of Financial Studies*, 21(6), 2535–2563. 确认来源:https://www.scheller.gatech.edu/directory/research/finance/lee/pdf/leemykland08.pdf ,二级确认 https://academicnewsletter.sufe.edu.cn/info/355320 。verified: true

[S49] Martijn Cremers, Michael Halling, David Weinbaum. 2015. "Aggregate Jump and Volatility Risk in the Cross-Section of Stock Returns." *Journal of Finance*, 70(2), 577–614. DOI 10.1111/jofi.12220;更早版本见 2012 年欧洲金融学会会议论文记录。verified: true

[S50] Saranya Kshatriya, Krishna Prasanna. 2020-09. "Unveiling Contemporaneous Relations Between Jump Risk and Cross Section of Stock Returns." *International Review of Finance*, 20(3), 581–604. DOI 10.1111/irfi.12235。确认来源:https://international.vlex.com/vid/unveiling-contemporaneous-relations-between-855667602 ,IIT Madras 记录 https://publications.iitm.ac.in/publication/unveiling-contemporaneous-relations-between-jump-risk-and-cross 。verified: true

[S51] Haigang Zhou, John Qi Zhu. 2011-07. "Jump Risk and Cross Section of Stock Returns: Evidence from China's Stock Market." *Journal of Economics and Finance*, 35(3), 309–331. DOI 10.1007/s12197-009-9097-z。IDEAS 记录:https://ideas.repec.org/a/spr/jecfin/v35y2011i3p309-331.html 。verified: true

[S52] Youcong Chao, Xiaoqun Liu, Shijun Guo. 2017-08. "Sign Realized Jump Risk and the Cross-Section of Stock Returns: Evidence from China's Stock Market." *PLOS ONE*, 12(8), 1–14. DOI 10.1371/journal.pone.0181990。确认来源:https://pmc.ncbi.nlm.nih.gov/articles/PMC5542663/ ,IDEAS 记录 https://ideas.repec.org/a/plo/pone00/0181990.html 。verified: true

[S53] Prodosh Simlai. 2014. "Persistence of Ex-ante Volatility and the Cross-Section of Stock Returns." *International Review of Financial Analysis*, 33, 253–261. DOI 10.1016/j.irfa.2014.03.002。IDEAS 记录:https://ideas.repec.org/a/eee/finana/v33y2014icp253-261.html 。verified: true(摘要确认;全文未能检索到,方法细节的具体持续性参数定义未逐一核实)

[S54] Steven L. Heston, Robert A. Korajczyk, Ronnie Sadka. 2010. "Intraday Patterns in the Cross-Section of Stock Returns." *Journal of Finance*, 65(4), 1369–1407. 确认来源:https://ar5iv.arxiv.org/html/1005.3535 ,https://www.kellogg.northwestern.edu/academics-research/research/detail/2010/intraday-patterns-in-the-cross-section-of-stock-returns/ 。verified: true

[S55] Ting Wu, Yue Wang, Ming-Xia Li. 2017. "Post-hit Dynamics of Price Limit Hits in the Chinese Stock Markets." *Physica A: Statistical Mechanics and its Applications*, 465, 464–471. DOI 10.1016/j.physa.2016.08.048。IDEAS 记录:https://ideas.repec.org/a/eee/phsmap/v465y2017icp464-471.html 。verified: true

[S56] Ya Gao, Xiong Xiong, Xing Feng(原文作者顺序以 IDEAS 记录为准,完整作者名单含 Benjamin M. Vigne), 等. 2019. "A New Attention Proxy and Order Imbalance: Evidence from China." *Finance Research Letters*, 29, 411–417. DOI 10.1016/j.frl.2018.11.009。IDEAS 记录:https://ideas.repec.org/a/eee/finlet/v29y2019icp411-417.html 。verified: true(标题、期刊、卷期、核心发现确认;完整作者姓名顺序未逐一核实,引用时需二次核对)

[S57] Carole Comerton-Forde, Tālis J. Putniņš. 2014. "Stock Price Manipulation: Prevalence and Determinants." *Review of Finance*, 18(1), 23–66. DOI 10.1093/rof/rfs040;更早的"forthcoming"工作论文版本标注日期 2012-10-08,https://opus.cloud1.lib.uts.edu.au/bitstream/10453/34251/4/DCEmanipulation_RevFin_20121008_forthcoming.pdf 。verified: true

[S58] Wei Zhang, Zhengzheng Bi, Dehua Shen. 2016. "Investor Structure and the Price-Volume Relationship in a Continuous Double Auction Market: An Agent-Based Modeling Perspective." *Physica A: Statistical Mechanics and its Applications*, 467, 345–355. DOI 10.1016/j.physa.2016.10.044。IDEAS 记录:https://ideas.repec.org/a/eee/phsmap/v467y2017icp345-355.html 。verified: true(标题、作者、期刊、核心仿真结论确认;该文是仿真 / 理论模型,不是实证检验,正文已标注)
