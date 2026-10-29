# 文献:种子 808,B 组,第 2 轮

对应 `analysis.md` §5 的 Q1–Q4(对准核心 1/2 的被测量「分钟级价格栅格粒度」、本种子最强的「处理手法」、来源 B 的规模非单调/杠铃、N 灵感 1 的日内「形状」统计量)。
只用 2023-08-08 前发表的论文 / 工作论文 / 研究报告(arXiv、SSRN 以首版日期为准,机构研究报告以报告落款日期为准);拿不准发表日期的不用。
每条处理方式后面用 `[R#]` 标出处,对应文末「出处列表」。`verified: true` 表示本次确实在 WebSearch 结果或 WebFetch / 直接读取的页面上看到了标题、作者、刊物、年份这几项;没有查到或日期拿不准的,如实写"搜不到"或"日期拿不准,不用",不编。

---

## Q1(核心 1 / 核心 2 的被测量:`day_distinct_ratio(Ret)`,分钟级价格栅格粒度)

**文献里"价格离散性 / 栅格粗细"是怎么被构造和处理的:**

1. **它首先是"价格聚集"(price clustering)的镜像:价格会聚集到整数/简单分数上,聚集强度随价格水平、波动率上升,随市值、交易频率下降。**
   Harris(1991)"Stock Price Clustering and Discreteness"(*Review of Financial Studies* 4(3))系统记录了这个现象,并建了一个聚集强度的计量模型,
   聚集随价格水平和波动率上升、随市值和交易频率下降 `[R1]`。
   翻译成算子语言:`day_distinct_ratio(Ret)` 低,一部分来自真实的"一跳相对价格粗"(低价股),但这条解释和市值、交易频率**本身就相关**,
   这正是本轮分析 §1.1 "诚实的保留"里悬而未决的问题——它可能是流动性/规模在分位内的非线性暴露,而不是独立机制。
   Harris 的结果提示:要把"栅格粗细"和"规模/流动性"分开,**单靠市值十分位条件化不够**,还应该额外按"换手率十分位"或者直接按"价格水平"
   (我们环境里没有裸价格字段,但 `log(day_last(Close))` 可以算出来,只是不能进 GP 树——可以在定位层面单独跑一次拆解)做第二条条件化对照,
   看 alpha 是被市值分位吃掉、还是被换手率分位吃掉。

2. **"零收益天数比例"是文献里最接近的现成横截面流动性测度,并且结构上是 `day_distinct_ratio` 的近亲(两者反向)。**
   Lesmond, Ogden & Trzcinka(1999)"A New Estimate of Transaction Costs"(*Review of Financial Studies* 12(5))用"零收益比例"
   (LOT 测度,还叠加了收益标准差)估计交易成本:投资者在成本高时选择不交易,价格就不动,零收益比例因此随交易成本单调上升 `[R2]`。
   Butt, Demirer, Sadaqat & Suleman(2022,*Quarterly Review of Economics and Finance* 86)在 20 个新兴市场的横截面检验里直接比较了
   LOT 的零收益测度和 Amihud 的金额加权冲击测度,发现**零收益(计数类)测度给出的非流动性溢价更强、更稳健**,但这个溢价本身**随时间在减弱** `[R6]`。
   翻译成算子语言:`day_zero_ratio(Ret)`(已有算子)就是 LOT 测度的日内版本,`day_distinct_ratio(Ret)` 是它的推广(不止零收益,还数"有几个不同值")。
   这给了一个直接可做的 R/敏感性检验:把核心里的 `day_distinct_ratio(Ret)` 换成 `day_zero_ratio(Ret)` 作同样的条件化 + `ts_max`,
   如果两者 score、ρ 都接近,说明本轮的 alpha 本质上就是"分位内条件化的 LOT 流动性溢价",不是价格栅格本身的新信息;如果差很多,
   才能排除"只是 LOT 式流动性代理"这条解释。Hung, Chen & Fang(2015,*International Review of Finance* 15(1))用相对买卖价差、
   Amihud、Amivest 三种流动性测度在 A 股股权分置改革前后做检验,发现流动性对截面收益的解释力在改革后更强、在控制了规模账面市值比之后依然显著 `[R7]`,
   这是"A 股的流动性类结构在控制规模后仍有残值"这个大方向的背景支持(不是 `day_distinct_ratio` 本身的直接证据)。

3. **归一化的标准做法是"一跳 / 价格"的相对比值,而不是价格水平本身;这个比值本身就解释了大部分的零收益现象,且对低价股影响最大。**
   Onnela, Töyli & Kaski(2009)"Tick size and stock returns"(*Physica A* 388(4))用同时在纽约和多伦多两个不同一跳制度下挂牌的
   交叉上市股票做自然实验(个股特征不变,只有一跳大小变了),发现**一跳相对价格的比值解释了零收益方差的约 69%**,且离散化效应对低价股最强 `[R3]`。
   O'Hara, Saar & Zhong(2019)"Relative Tick Size and the Trading Environment"(*Review of Asset Pricing Studies* 9(1))进一步说明
   **相对**一跳大小(而不是绝对一跳)决定了高频做市商的行为、挂单深度,且在"受一跳约束"和"不受一跳约束"两种环境下,相对一跳对深度的影响方向相反 `[R4]`。
   翻译成算子语言:这支持 `day_distinct_ratio(Ret)` 本身(算在收益上,不是算在价格上)已经是一种"相对归一化"——它不是绝对一跳,
   而是"一跳 / 当前价格"的一个代理(因为分钟收益 = k × 一跳 / 价格 的整数倍)。但 O'Hara-Saar-Zhong 的"受约束 / 不受约束"二分提示:
   这个归一化效应可能**不是线性的**,在价格很低(一跳相对价格很大,受约束)和价格正常(不受约束)两种状态下含义不同——
   这是分位内条件化(§1.1 的双重 `cs_bucket_zscore`)能部分捕捉、但可能捕捉不干净的一条非线性,值得在 R 里把核心按价格水平(换算出的 `log(Close)`)
   分段重新评估一次,而不只是按市值分段。

4. **时间维度的聚合(滚动最大值 vs 均值)和"控制了流动性与波动之后还有没有残值"这两点,本轮没有找到直接文献。**
   Harris(1991)、Onnela et al.(2009)、LOT(1999)用的都是样本期内的横截面均值或固定窗口估计量,**没有一篇把"价格离散度 / 零收益比例"
   本身再做一次时间序列上的滚动最大值**当作横截面预测变量来用;也没有找到专门检验"价格离散度在控制了常规流动性(Amihud/换手)和波动率之后
   是否还有横截面收益残值"的论文——Amihud(2002)"Illiquidity and Stock Returns"(*Journal of Financial Markets* 5)本身用的是金额加权冲击而不是
   计数类测度,且不专门讨论和离散度的联合检验 `[R5]`。这正是本轮分析 §1.1 "诚实的保留"点出的那个空白,文献没有替我们回答,
   只能靠 §2.3 的 R 目标(换成 `Close`/`Vwap`、换条件变量成成交额分位)自己去测。

**没搜到、不编的部分**:Li & Ye"The Optimal Nominal Price of a Stock: A Tale of Two Discretenesses"(AEA 2022/2023 会议稿,
Cornell 主页列为 Journal of Finance 在审)本来是这条轴上最贴切的理论模型(把一跳宽度和最优名义价格联系起来),但搜不到确切的首次发表 / 流通日期,
2022–2023 年会议稿的时间点离 2023-08-08 太近,拿不准,**不用**;A 股专门针对分钟级价格离散度 / 零收益比例做横截面检验、并控制流动性波动后看残值的
中文或英文论文,搜不到;一篇疑似"illiq_zero = Amihud + 零收益比例"构造、用上证 A 股 2000–2013 年数据的 Springer 论文(DOI 10.1007/s10690-015-9203-5)
因为出版方要求登录,无法核实标题和作者,**不列入出处**,只记录这条线索供后续核查。

---

## Q2(本种子最强的"处理手法":分位内条件标准化 + 自身历史标准化 + 滚动峰值)

**文献里"组内标准化"、"按自身历史标准化"、"滚动极值"是怎么被构造和处理的:**

1. **条件(依赖)排序和独立排序是两种不同的操作,前者等价于桶内标准化,文献的标准教材明确说两者在高维时给出不同结果。**
   Bali, Engle & Murray(2016)《*Empirical Asset Pricing: The Cross Section of Stock Returns*》(Wiley)第 5 章系统讲了
   独立双重排序(independent sort,两个维度各自在全市场排序再取交集)和条件双重排序(conditional/dependent sort,第二个维度只在
   第一个维度的桶内排序):单变量时两者等价,但维度一旦超过一个,结果会明显不同,条件排序的结果强烈依赖先排哪个维度 `[R11]`。
   翻译成算子语言:我们核心用的 `cs_bucket_zscore(y, x)` 正是条件(依赖)排序的桶内标准化版本,和"先做 `cs_regres(y, x)` 再用线性残差"
   是两条不同的路线;`ops_ext.py` 里 `cs_bucket_rank` 的注释已经点出了原因——条件排序能保证**每个 x 分桶里 y 的顶层份额完全一致**,
   线性秩残差做不到这一点("a linear rank residual does not guarantee it in the tails")。这正好是 §2.3 R 目标里该补的一条检验:
   把核心的 `cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap)` 换成 `cs_regres` 残差版本直接评估,看条件排序相对线性残差
   到底贵在哪一段(大概率是尾部)。

2. **组内标准化优于全市场排序,这在"行业内特征"这条轴上有早期的直接实证,而且报告了组内会出现反转、组间会出现动量这个有意思的不对称。**
   Asness, Porter & Stevens(2000,AQR 工作论文)"Predicting Stock Returns Using Industry-Relative Firm Characteristics"把规模、
   账面市值比、现金流价格比、过去收益等特征都拆成"个股相对行业均值"和"行业均值"两部分,发现行业内相对特征比全市场特征更有信息量;
   短期内行业**内部**是反转、跨行业**之间**是动量,且行业内的短期反转主要由买卖价差偏差驱动 `[R10]`。
   翻译成算子语言:这支持把 `cs_bucket_zscore` 的条件变量从 `LogFloatCap` 换成 `BoardCode`(板块,我们环境里可用的类行业字段)做一次平行检验——
   如果分位内条件化这个"手法"是普适的(不止对市值分组有效),换成按板块分组应该也能把 `day_distinct_ratio(Ret)` 从负做到正,
   这是判定"手法 vs 偶然"最直接的一条检验,而且和已有的 N 灵感 2(把中性化本身当成要搜的东西)直接相关。

3. **按自身历史(而不是全市场水平)标准化一个量,本身能产生一条独立不被常规解释的 alpha,经典案例是"异常成交量"。**
   Gervais, Kaniel & Mingelgrin(2001)"The High-Volume Return Premium"(*Journal of Finance* 56(3))发现:一天或一周内成交量
   相对该股票**自身近期历史**异常偏高的股票,接下来一个月收益显著更高,异常偏低的则更低;这个效应不能被收益自相关、公司公告、市场风险、
   流动性解释掉 `[R8]`。Connolly & Stivers(2003)"Momentum and Reversals in Equity-Index Returns During Periods of Abnormal
   Turnover and Return Dispersion"(*Journal of Finance* 58(4))用的是更精细的构造:先给换手率拟合一个"正常"水平(条件期望模型),
   再看当周换手率相对这个正常水平的"意外"偏离,发现连续两周收益的动量/反转方向取决于后一周的换手率是意外偏高还是偏低,
   指数、指数期货、个股都有这个模式 `[R12]`。翻译成算t语言:这两篇都在说"异常"不是"除以历史均值"那么简单,而是**先建立一个条件期望
   (近期历史分布或 AR 类模型),再看当期对这个期望的偏离**。这提示 §2.3 R 目标可以再加一条:把条件变量 `ts_max(cs_bucket_zscore(...), 40)`
   换成某种"自身历史残差"构造(比如 `sub` 当期值与自身滚动均值)做对照,而不仅仅是换成 `ts_mean` / `ts_decay_linear`(这是"中心"的平滑,
   不是"偏离中心"的异常值,两者概念不同,值得分开测)。

4. **滚动最大值 / 近期峰值作为预测信号在文献里确有先例,但取 max 的对象是"价格"本身(投资者对价格的锚定),不是一个已经条件化过的无量纲特征。**
   George & Hwang(2004)"The 52-Week High and Momentum Investing"(*Journal of Finance* 59(5))发现:当前价格与其过去 52 周最高价的
   接近程度,比过去收益本身更能解释动量利润,而且这个信号不会在长期反转,作者据此认为短期动量和长期反转是两种不同的机制 `[R9]`。
   翻译成算子语言:这是"取某个量的滚动最大值再和当前值比较"这类构造在文献里**唯一**站得住的先例,但它取 max 的对象是**价格水平本身**
   (投资者有心理锚点),不是像我们核心 1 那样取一个已经做过分位内 z 分的无量纲特征的滚动最大值。这个区别很重要:
   George-Hwang 的机制解释(锚定效应、投资者心理参照点)**不能**直接套到我们的核心上,因为"分位内条件 z 分的 40 日最大值"没有
   明显的心理锚定对象。这意味着 §1.6 第 3 条提的疑问("`ts_max` 是不是单纯在降换手")**没有文献能替我们排除**——
   George-Hwang 式的"信息锚定"解释和"纯粹降换手"解释在我们的构造上文献区分不开,只能靠 R 目标里 `ts_max` vs `ts_mean` /
   `ts_decay_linear` 的直接对照来回答。

**没搜到、不编的部分**:把"组内标准化"(Asness-Porter-Stevens 式)和"按自身历史标准化"(Gervais-Kaniel-Mingelgrin 式)**叠起来**
(先按同组去水平,再按自身历史去水平)的论文,没搜到;专门讨论"一个特征的滚动最大值"(不是价格、不是收益的最大值)作为横截面预测变量的论文,
没搜到——George-Hwang 是最近的类比但对象不同,如实说明不是直接证据;把"异常换手率"构造和"52 周最高价"构造结合起来讨论的论文,没搜到。

---

## Q3(来源 B:`cs_last_high05(LogFloatCap, LogFloatCap)`,规模的非单调 / 杠铃)

**文献里规模效应的非单调性与"剔除极端市值"的处理,是怎么做和怎么报告的:**

1. **这条轴最直接的先例不是"剔除",而是"连续非线性":把标准化规模立方、再正交于规模本身,这是业界风险模型处理"规模杠铃"的标准做法,
   而且在中国市场的版本里被明确列为一个独立风格因子。**
   MSCI Barra 的美国股票模型 USE4 和中国股票模型 CNE5 都把"Non-linear Size"(非线性规模)列为独立的风格因子。
   按 MSCI《Barra China Equity Model (CNE5): Descriptor Details》(2013-09)的定义:先取标准化的 Size 暴露(对数市值)、**立方**,
   再把这个立方值**对 Size 做回归正交化**,最后做缩尾和标准化 `[R19]`;CNE5 把这个因子列为 10 个风格因子之一,与 Beta、动量、
   账面市值比等并列,是在中国市场工程化验证过的标准处理 `[R19]`。MSCI 的配套研究报告《Global Market Report: The Mid-Cap Effect》
   (Ruban, Nagy & Menchero, 2012-12)报告了这个因子的经验含义:大盘股在 Size 上正暴露、在 Non-linear Size 上负暴露,
   随着市值从大盘往中盘移动,Non-linear Size 暴露翻正、Size 暴露翻负——也就是说**中间规模和两端规模**在这个因子上系统性地走向相反方向,
   这正是"杠铃"的经验表现;这篇报告还把全球中盘股在 2008 年金融危机后数年的强势表现,相当一部分归因于这个因子 `[R18]`。
   翻译成算子语言:文献 / 业界的标准做法是**连续的三次方残差化**(`pow(cs_rank(LogFloatCap), 3)` 之类,再对 `LogFloatCap` 做
   `cs_regres` 正交化),而不是我们来源 B 用的**硬阈值筛子**(`cs_last_high05`,把最大 5% 直接推到底部)。这是一条直接可做的 R 目标:
   把 `cs_last_high05(LogFloatCap, LogFloatCap)` 换成"立方 + 正交化"的连续版本,如果连续版本同样能过线甚至更稳(train/valid 不像
   §1.2 那样一个掉一个升),说明杠铃本身是真实的非线性规模效应;如果连续版本不行、只有硬阈值的筛子能过线,
   那就更坐实"来源 B 的 score 主要来自筛子本身的躲避已知族 / 降换手效果"这个判断(§1.2 已经发现去掉筛子后 ρ_known 从 −0.21 升到 −0.55)。

2. **"剔除微盘股"这个处理在文献里有明确的方法论争议和推荐做法,核心论点是:微盘股驱动的异象大概率是交易成本的产物,不是真 alpha。**
   Hou, Xue & Zhang(2020)"Replicating Anomalies"(*Review of Financial Studies* 33(5),工作论文版本 NBER WP23394 于 2017-05
   公开流通)系统重做了 447 个已发表的异象,把"微盘股"定义为 NYSE 市值最小 20% 分位以下的股票,用 NYSE 断点分组 + 市值加权收益
   (而不是全市场断点 + 等权)来抑制微盘股对检验结果的主导;按这个更严格的口径,64% 的异象在 5% 显著性下不再显著,
   按 Harvey-Liu-Zhu(2016)建议的 t ≥ 3 门槛则有 85% 不再显著 `[R17]`。翻译成算子语言:这给了一条直接的归因标准——
   如果一个 head 的 score 显著依赖某个市值端的硬筛子(像来源 B 的 `cs_last_high05`),应该在归因表里单独标注"疑似微盘/巨盘筛子驱动",
   而不是和 §1.1 来源 A 那种"分位内条件化但不依赖硬阈值"的发现同等计数。

3. **指数纳入 / 机构持仓集中是"最大那一档单独有效应"的另一条解释,和"杠铃"的几何解释是竞争关系,需要分开。**
   Shleifer(1986)"Do Demand Curves for Stocks Slope Down?"(*Journal of Finance* 41(3),Papers and Proceedings)用标普 500
   成分股调整的事件研究发现:纳入指数的股票价格显著且持续性地上涨,涨幅和指数基金的被动买入强度正相关,据此论证股票的需求曲线不是水平的 `[R15]`。
   Gompers & Metrick(2001)"Institutional Investors and Equity Prices"(*Quarterly Journal of Economics* 116(1),
   工作论文 NBER WP6723 于 1999-08 公开流通)发现大机构相对其他投资者系统性偏好市值更大、流动性更好的股票,
   1980–1996 年间大机构的持仓份额几乎翻倍,作者认为这解释了小盘溢价在样本后期的消失 `[R20]`。
   翻译成算子语言:这两篇合起来提示,**最大市值那一档**(我们来源 B 筛子剔除的那 5%)系统性地被机构持仓和指数资金"托住",
   这是一种和"几何杠铃"完全不同的机制(资金流 vs 非线性定价关系)。如果本组的定位工具以后有机会接入指数成分 / 机构持仓类字段,
   这是检验来源 B 真正身份的一条路;在当前 6 个日频字段叶子里没有直接对应物,只能记录这个局限。

4. **规模效应本身的时间不稳定性是一个独立的背景事实,降低了"这一批里规模相关的 head 一定代表真实 alpha"的先验。**
   Van Dijk(2011)"Is size dead? A review of the size effect in equity returns"(*Journal of Banking & Finance* 35(12))
   综述 30 年规模效应文献,结论是效应"没有死,但状态不好"——多数市场原始收益上小盘仍跑赢大盘,但风险调整后的结果不稳定,
   且效应强度随时间大幅波动 `[R14]`。Hou & van Dijk(2019)"Resurrecting the Size Effect"(*Review of Financial Studies* 32(7))
   则给出一个具体机制:规模效应在 1980 年代早期后"消失",是因为小盘股此后系统性地遭遇意外的负向盈利冲击、大盘股遭遇正向冲击,
   调整了这个盈利冲击的价格影响之后,规模效应重新稳健地出现 `[R16]`。翻译:这提示即使不考虑杠铃,**规模轴本身的 score 高低可能
   和样本期内大小盘的相对盈利冲击有关**,是一个我们控制不住的样本期效应,这也是为什么 §1.2 的证据链里"train 掉、valid 升"
   这种形状特别值得怀疑——它既可能是降换手,也可能是样本期内规模溢价本身的结构性漂移。

**没搜到、不编的部分**:专门在 Fama-MacBeth 框架里用"剔除最大 x%"(而不是连续非线性)处理规模并报告显著性的论文,没搜到
(业界的标准做法是连续非线性,见上面第 1 条,这本身就是一个值得记录的"文献没有直接支持硬阈值剔除法"的空白);A 股市场专门检验
"剔除最大市值一档后因子才显著"这类构造是真效应还是池子构造产物的论文,没搜到;CSI300/沪深300 指数纳入对**个股**(而不是组合层面)
横截面收益预测力的专门研究,搜到的几篇(Wang, Murgulov & Haman 2015;Yao et al. 2022 等)讨论的是纳入/剔除事件本身的异常收益,
不是"指数成分"当作一个持续特征放进横截面回归里控制的构造,只能作旁证,不直接支持 §4.1 核心 1/2 之外的任何具体算子建议。

---

## Q4(N 灵感 1:非波动类的日内"形状"统计量)

**文献里日内成交的时间分布、集中度、停滞段是怎么被构造和处理的:**

1. **U 型日内交易量 / 波动模式是最早、最基础的理论基准,源于知情交易者和流动性交易者的策略互动,不是噪音。**
   Admati & Pfleiderer(1988)"A Theory of Intraday Patterns: Volume and Price Variability"(*Review of Financial Studies* 1(1))
   构建了一个知情交易者和流动性(噪音)交易者的策略均衡模型,交易量和价格波动的日内集中模式(开盘、收盘高,午间低)是内生结果,
   不是外生噪音;论文称这部分解释了当时关于日内成交量、价格波动模式的经验发现 `[R21]`。翻译成算子语言:这是 `day_centroid`
   (成交重心,早盘 vs 尾盘)这类构造的理论基准——U 型本身是**预期中**的形状,如果要让 `day_centroid` 这类量承载信息,
   更合理的做法不是直接用早盘/尾盘占比的水平值,而是看**相对 U 型基准的偏离**(比如用过去 N 日的典型形状做分母再归一化),
   这和 Q2 第 3 条"按自身历史标准化"的建议是同一个思路在日内维度上的应用。

2. **"日内动量"(当日前段收益预测后段收益)是有直接文献的,但证据在指数/ETF 层面,迁移到个股横截面没有现成支持。**
   Gao, Han, Li & Zhou(2018)"Market Intraday Momentum"(*Journal of Financial Economics* 129(2))用 1993–2013 年标普 500
   ETF 的高频数据发现:(相对前一日收盘计算的)当日第一个半小时收益能预测最后半小时收益,在波动率更高、成交量更大、衰退期、
   部分宏观数据发布日这个预测力更强 `[R22]`。翻译成算子语言:这支持用 `in_index` 配合 `day_topw_mean` 或者直接切片构造
   "开盘段收益 vs 收盘段收益"的交互项当作新 idea 的候选结构,但要如实标注:原论文的预测对象是**同一资产自己的未来收益**
   (时间序列),不是**横截面上哪只股票未来收益更高**;这个跨层级的迁移(指数时间序列 → 个股横截面)文献里没有直接先例,
   是本条建议最大的不确定性。Heston, Korajczyk & Sadka(2010)"Intraday Patterns in the Cross-section of Stock Returns"
   (*Journal of Finance* 65(4))倒是在个股横截面层面发现了类似现象:半小时粒度上、**与昨天同一个时点**对齐的收益存在延续性,
   能持续至少 40 个交易日;但论文同时指出成交量、委托不平衡、波动率、买卖价差也有类似的日内周期模式,却**解释不了**收益延续
   本身,言下之意是用这些流动性类统计量直接当作这个日内动量的来源会落空 `[R23]`。翻译:如果要做"日内形状预测收益"这条 N,
   更该参考的是"按日内时点对齐后再比较"这个结构(类似我们 `in_index` 算子能支持的构造),而不是单纯的日内统计量水平值;
   同时要避免把"流动性类的日内形状"误当成这个效应的来源,因为 Heston 等人已经排除了这条解释。

3. **成交集中度 / 大单占比的文献基准是"隐蔽交易假说":知情交易者偏好中等规模的单子,不是最大的单子。**
   Barclay & Warner(1993)"Stealth Trading and Volatility: Which Trades Move Prices?"(*Journal of Financial Economics* 34(3))
   用 108 次要约收购前的交易数据发现,**中等规模**交易(500–9,999 股)贡献了要约公告前约 92.8% 的累计价格变动,
   提出知情交易者会把单子拆成中等大小以规避被识别("隐蔽交易"假说)`[R24]`。翻译成算子语言:这对我们已有的 `day_topw_mean`
   (取当日权重最大的前 10% 分钟均值,相当于捕捉"大额分钟")提出一个直接的警示——如果知情交易偏好**中等**而不是**最大**规模,
   只看最大 10% 权重的分钟可能漏掉信息最集中的那一段。这是一条可以直接翻译成 R 目标的新检验:把 `day_topw_mean(y, w)` 换成
   "取权重落在中间某个分位带(比如 40%–60% 分位)的分钟均值"做对照,看是不是比"最大 10%"更有信息量——这是此前没有人提过的检验,
   而且有明确的文献动机。

4. **停滞分钟占比、在日内高低点附近停留的时间比例,本轮没有找到任何直接的横截面收益预测文献——这更可能是真的空白,而不是没搜到。**
   `day_flat_ratio`、`day_zero_ratio`、`day_at_max_ratio`/`day_at_min_ratio`、`day_flat_run_max`、`day_gini` 这些结构在
   微观结构文献里通常是作为流动性 / 交易活跃度的**描述性**统计量出现(参见 Q1 的 LOT 测度 `[R2]`,其内核就是零收益比例),
   但没有搜到专门把"停留在日内高/低点的时间占比"或"最长停滞段"当作一个独立的、控制了常规流动性和波动之后仍有横截面收益残值的
   预测变量来检验的论文。这和本种子目前唯一验证过的真信号(`day_distinct_ratio(Ret)` 条件化之后)形成一个值得注意的对照:
   如果这类"日内形状"结构在文献里确实是空白,那么按 §4.3 灵感 1 的思路把"分位内条件标准化 + 时序归约"这个手法迁移过去,
   更可能是在探索一片没被学术界测过的区域,而不是在重复验证一个已知效应——这既是机会,也意味着没有文献能替我们预判方向和强度。

**没搜到、不编的部分**:收盘集合竞价成交占比对**个股**横截面收益预测力的专门研究(A 股 2018 年引入收盘集合竞价后的文献多是研究
该制度对流动性 / 波动率 / 价格发现的影响,不是把"集合竞价占比"当作持续性横截面特征),没搜到;"成交基尼系数"(`day_gini`)
作为独立横截面预测变量的论文,没搜到;把"日内停留在高低点的时间比例"和已实现波动率一起放进同一个横截面检验、报告谁的解释力更强的论文,
没搜到;Van Bommel 提出的"成交量变异系数(标准差/均值)代理知情交易比例"这个构造本身可能相关,但搜到的版本是工作论文,
拿不准首次流通日期,不用。

---

## 出处列表

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|---|
| R1 | Stock Price Clustering and Discreteness | Harris, L. | 1991(RFS 4(3),389-415) | Review of Financial Studies | https://ideas.repec.org/a/oup/rfinst/v4y1991i3p389-415.html | true |
| R2 | A New Estimate of Transaction Costs | Lesmond, D.A.; Ogden, J.P.; Trzcinka, C.A. | 1999(RFS 12(5),1113-1141) | Review of Financial Studies | https://ideas.repec.org/a/oup/rfinst/v12y1999i5p1113-41.html | true |
| R3 | Tick size and stock returns | Onnela, J-P.; Töyli, J.; Kaski, K. | 2009(Physica A 388(4),441-454) | Physica A: Statistical Mechanics and its Applications | https://ideas.repec.org/a/eee/phsmap/v388y2009i4p441-454.html | true |
| R4 | Relative Tick Size and the Trading Environment | O'Hara, M.; Saar, G.; Zhong, Z. | 2019(RAPS 9(1),47-90) | Review of Asset Pricing Studies | https://ideas.repec.org/a/oup/rasset/v9y2019i1p47-90..html | true |
| R5 | Illiquidity and Stock Returns: Cross-Section and Time-Series Effects | Amihud, Y. | 2002-01(JFM 5(1),31-56) | Journal of Financial Markets | https://www.casact.org/abstract/illiquidity-and-stock-returns-cross-section-and-time-series-effects | true |
| R6 | Do emerging stock markets offer an illiquidity premium for local or global investors? | Butt, H.A.; Demirer, R.; Sadaqat, M.; Suleman, M.T. | 2022-11(QREF 86,502-515) | Quarterly Review of Economics and Finance | https://ideas.repec.org/a/eee/quaeco/v86y2022icp502-515.html | true |
| R7 | Non-Tradable Share Reform, Liquidity, and Stock Returns in China | Hung, C-H.D.; Chen, Q.; Fang, V. | 2015-03(IRF 15(1),27-54) | International Review of Finance | https://ideas.repec.org/a/bla/irvfin/v15y2015i1p27-54.html | true |
| R8 | The High-Volume Return Premium | Gervais, S.; Kaniel, R.; Mingelgrin, D.H. | 2001-06(JF 56(3),877-919;工作论文 Wharton Rodney White Center 99-01) | Journal of Finance | https://ideas.repec.org/a/bla/jfinan/v56y2001i3p877-919.html | true |
| R9 | The 52-Week High and Momentum Investing | George, T.J.; Hwang, C-Y. | 2004-10(JF 59(5),2145-2176) | Journal of Finance | https://academicnewsletter.sufe.edu.cn/info/361244 | true |
| R10 | Predicting Stock Returns Using Industry-Relative Firm Characteristics | Asness, C.S.; Porter, R.B.; Stevens, J.L. | 2000-02(AQR 工作论文) | AQR Capital Management Working Paper | https://www.aqr.com/Insights/Research/Working-Paper/Predicting-Stock-Returns-Using-IndustryRelative-Firm-Characteristics | true |
| R11 | Empirical Asset Pricing: The Cross Section of Stock Returns(第 5 章:双重排序方法论) | Bali, T.G.; Engle, R.F.; Murray, S. | 2016 | Wiley(教材) | https://mitpressbookstore.mit.edu/book/9781118095041 | true |
| R12 | Momentum and Reversals in Equity-Index Returns During Periods of Abnormal Turnover and Return Dispersion | Connolly, R.; Stivers, C. | 2003-08(JF 58(4),1521-1556) | Journal of Finance | https://ideas.repec.org/a/bla/jfinan/v58y2003i4p1521-1556.html | true |
| R13 | Size Matters, if You Control Your Junk | Asness, C.S.; Frazzini, A.; Israel, R.; Moskowitz, T.J.; Pedersen, L.H. | 2015-01 工作论文 / 正式发表 2018-09(JFE 129(3),479-509) | Journal of Financial Economics | https://jacobslevycenter.wharton.upenn.edu/wp-content/uploads/2015/05/Size-Matters-if-You-Control-Your-Junk.pdf | true |
| R14 | Is size dead? A review of the size effect in equity returns | Van Dijk, M.A. | 2011-12(JBF 35(12),3263-3274) | Journal of Banking & Finance | https://ideas.repec.org/a/eee/jbfina/v35y2011i12p3263-3274.html | true |
| R15 | Do Demand Curves for Stocks Slope Down? | Shleifer, A. | 1986-07(JF 41(3),579-590,Papers and Proceedings) | Journal of Finance | https://shleifer.scholars.harvard.edu/publications/do-demand-curves-stocks-slope-down | true |
| R16 | Resurrecting the Size Effect: Firm Size, Profitability Shocks, and Expected Stock Returns | Hou, K.; Van Dijk, M.A. | 2010 工作论文 / 正式发表 2019-07(RFS 32(7),2850-2889) | Review of Financial Studies | https://ideas.repec.org/a/oup/rfinst/v32y2019i7p2850-2889..html | true |
| R17 | Replicating Anomalies | Hou, K.; Xue, C.; Zhang, L. | 2017-05(NBER WP23394) / 正式发表 2020-05(RFS 33(5),2019-2133) | NBER Working Paper / Review of Financial Studies | https://www.nber.org/papers/23394 | true |
| R18 | Global Market Report: The Mid-Cap Effect | Ruban, O.; Nagy, Z.; Menchero, J. | 2012-12 | MSCI(机构研究报告) | https://www.msci.com/research-and-insights/paper/global-market-report-the-mid-cap-effect-december-2012 | true |
| R19 | Barra China Equity Model (CNE5): Descriptor Details | MSCI / Barra | 2013-09 | MSCI(Model Insight,机构研究报告) | https://zhiqiang.org/media/images/notes/202106/ea021009818156021bdc3e00d100b151.pdf | true |
| R20 | Institutional Investors and Equity Prices | Gompers, P.A.; Metrick, A. | 1999-08(NBER WP6723)/ 正式发表 2001-02(QJE 116(1),229-259) | NBER Working Paper / Quarterly Journal of Economics | https://www.nber.org/papers/w6723 | true |
| R21 | A Theory of Intraday Patterns: Volume and Price Variability | Admati, A.R.; Pfleiderer, P. | 1988(RFS 1(1),3-40) | Review of Financial Studies | https://academicnewsletter.sufe.edu.cn/info/355980 | true |
| R22 | Market Intraday Momentum | Gao, L.; Han, Y.; Li, S.Z.; Zhou, G. | 2018-08(JFE 129(2),394-414) | Journal of Financial Economics | https://academicnewsletter.sufe.edu.cn/info/356150 | true |
| R23 | Intraday Patterns in the Cross-section of Stock Returns | Heston, S.L.; Korajczyk, R.A.; Sadka, R. | 2010-08(JF 65(4),1369-1407) | Journal of Finance / arXiv:1005.3535 | https://arxiv.org/abs/1005.3535 | true |
| R24 | Stealth Trading and Volatility: Which Trades Move Prices? | Barclay, M.J.; Warner, J.B. | 1993-12(JFE 34(3),281-305) | Journal of Financial Economics | https://ideas.repec.org/r/eee/jfinec/v34y1993i3p281-305.html | true |

**搜了但没有可独立核实的文献,不编、如实列在这里(不算出处):**

- Li & Ye"The Optimal Nominal Price of a Stock: A Tale of Two Discretenesses"(一跳宽度与最优名义价格的理论模型,2022/2023 AEA 会议稿,
  Cornell 主页列为 JF 在审):内容和 Q1 高度相关,但搜不到确切的首次发表 / 流通日期,2022–2023 年的会议时间点离 2023-08-08 太近,拿不准,不用(Q1)。
- 疑似"illiq_zero = Amihud + 零收益比例"构造、用上证 A 股 2000–2013 年数据的论文(DOI 10.1007/s10690-015-9203-5,疑似发表于
  *Asia-Pacific Financial Markets*):出版方要求登录,无法核实标题与作者,不列入出处(Q1)。
- A 股专门检验"分钟级价格离散度 / 零收益比例"横截面预测力、并控制流动性波动后看残值的论文(Q1);把"组内标准化"和"按自身历史标准化"
  叠加使用的论文(Q2);专门讨论"一个特征本身(非价格、非收益)的滚动最大值"作为横截面预测变量的论文,George-Hwang(52 周最高价)
  是最近的类比但取 max 的对象是价格水平本身,不是同一类构造(Q2)。
- 在 Fama-MacBeth 框架里用"剔除最大 x% 市值"(而非连续非线性)处理规模并报告显著性的论文;CSI300/沪深300 指数成分身份当作持续性
  横截面特征(而不是纳入/剔除事件)放进收益回归的专门研究(Q3)。
- 收盘集合竞价成交占比对个股横截面收益预测力的专门研究;"成交基尼系数"作为独立横截面预测变量的论文;"日内停留在高低点时间比例"
  与已实现波动率联合检验解释力的论文(Q4)。
- Van Bommel"成交量变异系数(标准差/均值)代理知情交易比例"的构造:搜到的版本是工作论文,拿不准首次流通日期,不用(Q4)。
