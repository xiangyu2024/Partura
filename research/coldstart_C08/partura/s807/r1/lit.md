# 文献:种子 807,P 组,第 1 轮(文献员)

对准 `analysis.md` 第 5 节的 L1–L4。每条「处理方式」后面括号里写出处简写,完整出处见各节末的列表。**只用 2023-08-08 之前发表的论文 / 工作论文 / 研究报告**;日期拿不准的已经弃用,在各节末尾单独列出「搜到但弃用/搜不到」。

---

## L1 —— 价格水平方差口径(对准核心 A / 核心 B)

### 文献里怎么处理「窗口内价格 / 市值水平方差混进漂移项」这件事

1. **漂移项的来源是解析可算的,不是只能猜**:对一个近似随机游走的对数价格,窗口内「水平」方差 ≈ 收益方差 × 窗口长度的某个线性函数 + (窗口内累计收益)²/12 这一类漂移项,这正是 `analysis.md` F-block 里写出的那个近似式的同一结构。文献里处理这件事的标准做法不是去"拟合掉"漂移,而是**换一个在构造时就不吃漂移的估计量**:
   - Parkinson (1980) 的极值估计量只用当日 high/low 的对数比的平方,推导时就假设零漂移,**在有趋势的区间会把趋势部分也计入方差、读数偏高**(来源:Rogers-Satchell 条目下的二级来源,转述 Parkinson/Garman-Klass 的假设)。
   - **Rogers & Satchell (1991)** 直接把每日的 open/high/low/close 组合成 `ln(H/C)·ln(H/O) + ln(L/C)·ln(L/O)`,这个量**数学上与当日漂移(日内净涨跌)无关**,是文献里"drift-independent"方差估计量的标准构造。**可翻译成我们的算子**:先在分钟立方体上按日构造 `day_high/day_low/day_open/day_close`(或等价的 `day_quantile_q100/q0` 近似)算出这个逐日标量,再对它做 `ts_mean(·, d)` 取窗口均值 —— 这样得到的「d 日方差」就不会像直接对 `LogFloatCap` 的日频水平做 `ts_var(·, d)` 那样把 d 日累计涨跌幅平方也算进去。
   - **Yang & Zhang (2000)** 在 RS 的基础上再加一个隔夜项(`ln(Open_t/Close_{t-1})` 的方差)和一个日间项,用一个最小方差的权重 k 把三者线性组合,**同时做到漂移无关、且能处理隔夜跳空**,文献把它看作目前能用 OHLC 四个价位拿到的、方差最小的无偏估计量。**可翻译成我们的算子**:这恰好是 §1.2 说的「(a) 日频方差 vs (b) 隔夜/低频那一截」的现成分解公式 —— 隔夜项 `ts_var(log(day_open(Open)/ts_delay(day_last(Close),1)), d)` 可以直接搭,日内项就是 RS 那个逐日标量的窗口均值,两者相加才是"完整"的日频方差,而现有的波动控制 `cross_mean(day_std(Ret), 20)` 只覆盖的是分钟内这一截,不覆盖隔夜项 —— 这给 N2 的「拆开 (a)/(b)」提供了一个有名字、可复现的构造,而不是临时拼公式。

2. **已实现方差本身也能按"连续 vs 跳跃"拆**:Barndorff-Nielsen & Shephard (2004) 把日内已实现方差(分钟收益平方和)与「bipower variation」(相邻分钟绝对收益乘积之和,乘 π/2 校正)相减,得到的正差值就是**跳跃部分**的方差贡献,文献称这是第一个能把二次变差拆成连续段和跳跃段的方法。**可翻译成我们的算子**:在分钟立方体上构造 `day_sum(abs(ret_t)*abs(ret_{t-1}))*pi/2`(bipower)与 `day_sum(ret_t^2)`(已实现方差)的差,得到一个逐日"跳跃强度"标量,再 `ts_mean`/`ts_sum` 到窗口 —— 这是把"流通股本变动引起的市值跳跃"(N2 的 (b) 部分)和"平滑的日内波动"在同一个数学框架下分开的现成办法,比直接拿 `ts_var(LogFloatShares, d)` 当唯一的跳跃代理更细。

3. **已实现方差 / 日内波动 与 隔夜波动分别预测什么**:Lou, Polk & Skouras (2019, JFE) 把日收益拆成隔夜(close→open)和日内(open→close)两段,发现**很多策略的收益完全来自其中一段,且两段常常符号相反**、股票在隔夜收益上的高低有持续性并伴随日内收益的低位持续性。**可翻译成我们的算子**:如果 §1.2 的「真来源」确实部分来自隔夜/低频那一截,那么文献给出的预期是 —— 把 `ts_var(LogFloatCap, d)` 换成只用隔夜收益构造的方差,效果不会和用日内收益构造的方差一样,甚至可能符号或半衰期都不同,这是一个可直接核对的预测,呼应 R-E「口径分离」的思路。

4. **这类"水平方差/低波动"代理在 A 股确实可能有定价含量,但机制说法不唯一**:
   - Ang, Hodrick, Xing & Zhang (2006, JF) 的经典结果是**滞后特质波动率越高、未来收益越低**(美股样本);该控制变量用的是收益方差,不是水平方差,所以我们的 `ts_var(LogFloatCap, d)` 如果真有 alpha,按 §1.2 的推理,**理论上不该是这篇文章讲的那个机制的重复**(控制变量已经吃掉分钟内收益波动),但审计员如果要判断"是不是同一个东西",这篇是绕不开的对照。
   - Robeco / Blitz (2021-05) 对 A 股 2000-2018 的研究报告了一个很强的低波动效应,且**在 1 个月到 5 年的估计窗口下结果都差不多**(作者原话转述),把它归因于个人投资者占主导的行为偏差,而不是风险补偿 —— 这给 R-E 里"窗口 20/30/40/50 都试一遍"的稳健性检验提供了文献预期:**如果真机制接近这类低波动异象,窗口长度不应该是悬崖式敏感的**,和 `analysis.md` §1.2 敏感性那一条("有影响,不是悬崖")的实测方向一致。
   - Baltussen, Van Bekkum & Van der Grient (2018, JFQA)的"vol-of-vol"(波动率的波动率)发现高 vol-of-vol 股票未来收益更低,且这个变量**更像个股特征、不是定价因子**。这给 F15/§1.6 里 head 1 那个"波动的波动"(`var_5(ts_var(LogFloatCap,20))`)的机制提供了一个文献先例:这类二阶波动量确实在其他市场有记录在案的、独立于一阶波动的横截面效应,不完全是数值伪影。

### L1 出处

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|---|
| 1 | The Extreme Value Method for Estimating the Variance of the Rate of Return | M. Parkinson | 1980 | Journal of Business, 53(1), 61-65 | 搜索结果中反复出现该引用(TradingView 文档转述),未直接读到原文 PDF | true |
| 2 | Estimating Variance From High, Low and Closing Prices | L.C.G. Rogers, S.E. Satchell | 1991 | Annals of Applied Probability | 搜索结果引用,未直接读到原文 PDF | true |
| 3 | Drift-Independent Volatility Estimation Based on High, Low, Open, and Close Prices | Dennis Yang, Qiang Zhang | 2000 | Journal of Business, 73(3), 477-491 | https://scholars.cityu.edu.hk/en/publications/drift-independent-volatility-estimation-based-on-high-low-open-an/ | true |
| 4 | Power and Bipower Variation with Stochastic Volatility and Jumps | Ole E. Barndorff-Nielsen, Neil Shephard | 2004 | Journal of Financial Econometrics, 2(1), 1-37 | https://www.nuffield.ox.ac.uk/economics/Papers/2003/w18/bipower.txt ;摘要页 https://academic.oup.com/jfec/article/2/1/1/960705 | true |
| 5 | The Cross-Section of Volatility and Expected Returns | Andrew Ang, Robert Hodrick, Yuhang Xing, Xiaoyan Zhang | 2006-02 | Journal of Finance, 61(1), 259-299 | https://www.nber.org/system/files/working_papers/w10852/w10852.pdf | true |
| 6 | A Tug of War: Overnight versus Intraday Expected Returns | Dong Lou, Christopher Polk, Spyros Skouras | 2019 | Journal of Financial Economics, 134(1), 192-213 | https://researchonline.lse.ac.uk/id/eprint/87481/ | true |
| 7 | The Low-Volatility Effect in China(研究简报) | David Blitz(Robeco) | 2021-05 | Robeco 官网研究文章 | https://robeco.com/nl-nl/visie/2021/05/the-low-volatility-effect-in-china | true |
| 8 | Unknown Unknowns: Uncertainty About Risk and Stock Returns | Guido Baltussen, Sjoerd van Bekkum, Bart van der Grient | 2018 | Journal of Financial and Quantitative Analysis, 53(4), 1615-1651(工作论文更早在 2012 前后已流传,见 Quantpedia 2012-08-31 的转述) | https://tinbergen.nl/publication/166928/unknown-unknowns-uncertainty-about-risk-and-stock-returns | true |

**搜到但弃用(日期不确定或在 2023-08-08 之后)**:一篇 2025 年 NYU honors thesis、一篇署名 Jinbo Huang 的中南财经政法/深大工作论文(关于 A 股特质波动率异象按采样频率分裂),日期无法确认在 2023-08-08 之前,未采用。

---

## L2 —— 分组去均值 / 板块中性化,与 `LimitWidth` 分桶(对准核心 A、N3)

### 文献里怎么处理「同组同类里相对化」vs「截面回归残差」

1. **行业内相对化是一条有名字的独立做法,不是回归的简化版**:Asness, Porter & Stevens (2000-02, AQR working paper) 把一个特征拆成「行业内相对部分」(一个公司相对同行业均值)和「行业间部分」(该行业相对其他行业),发现**行业内这部分有显著的动量效应**,且短期和中期的符号不同。**可翻译成我们的算子**:行业内相对部分的构造就是 `x - cs_mean(x, 行业分组)`,等价于我们的 `cs_bucket_demean(x, industry_code)`(用真正的行业/板块标签做分组字段,而不是用 `LimitWidth` 这种取值只有 2-3 档、靠列序切片的字段)。这是 N3「分组相对化,但分组字段选对」最直接的文献支撑。
2. **分组去均值与回归残差在"无权重、单一分组因子、无截距之外协变量"时是同一个数学对象**:这点来自对多篇行业中性化文献的交叉阅读(包括 Ehsani, Harvey & Li 下方条目)的直接推导 —— 普通最小二乘对一组分组哑变量回归、不加别的协变量,其残差就精确等于按组去均值后的值。**差别出现在**:(a) 回归里一旦加别的协变量(比如同时控制规模),残差会比纯分组去均值多去掉一层规模暴露;(b) 回归可以加权(比如按 1/σ² 加权降低高波动个股的影响),分组去均值做不到;(c) 分组去均值对「组」的定义很敏感 —— 组数太少、组内异质性大时,去均值去掉的是组均值这个粗糙统计量,保留的组内方差可能主要由与该分组字段无关的东西(比如 §1.3 说的「代码片段」)驱动。这条直接对应 §1.3 的诊断:`LimitWidth` 只有 2-3 个值,按它分桶在 2019 年以前约等于「什么都没分」。
3. **行业内 vs 行业间该保留哪个,取决于你是多空还是纯多头**:Ehsani, Harvey & Li (SSRN 工作论文首发 2021-11,后刊于 Financial Analysts Journal 2023) 系统比较了"保留行业间成分"对多空因子和纯多头因子的影响,发现**纯多头投资者更可能从"不做行业中性化"中受益,而多空投资者更可能从"做行业中性化"中受益**,因为纯多头的行业间成分本身可能携带可观的收益信息,被中性化掉就是扔掉信息。**这对本轮直接有用**:规则 §1 的奖励口径是"纯多头十分位书",按这篇的结论,`cs_bucket_demean(·, BoardCode)` 这种完全剔除板块间差异的做法,在纯多头口径下**不一定比不分桶更好**——这是 R-C 核对 `BoardCode` 版本时值得多看一眼的点,而不是默认"真板块标签就该更好"。
4. **离散多路分桶去均值是经过检验的另一条路,不是回归残差"退化版"**:Daniel, Grinblatt, Titman & Wermers (1997, Journal of Finance)的 DGTW 基准法,把股票按规模 × 账面市值比 × 动量三维分到若干组,用组内平均收益作基准相减,这是分组去均值在学术上被反复使用、检验过的标准做法(用于基金业绩评估,但方法本身是通用的"特征调整收益"构造)。**可翻译**:支持把 `LogFloatCap`(规模)当分桶字段这件事本身是有先例的标准操作,不是临时拼凑。
5. **`LimitWidth` 这个字段在文献里对应的是涨跌幅限制规则,它的经济含量来自"触及限价的那些交易日",不是一个可以当常量分组标签用的静态属性**:
   - Wan et al. (2015, PLOS ONE) 用 2000-2011 的 A 股高频数据发现涨跌停规则总体是"冷却效应"而非"磁吸效应",效应体现在**触及涨跌停的那个交易日及其后续交易日**。
   - Qi (2023-06, PLOS ONE) 用创业板 2020-08-24 的 10%→20% 改革做事件研究,发现 10% 限制下价格发现延迟、波动溢出、交易干扰等效应都在**触及限价附近**更明显,改革后(20%)这些效应减弱。
   - 这两篇合起来说明:涨跌幅限制的"信息"是事件性的(某天触及与否、触及后的行为),而不是"这只股票平时的限幅档位是 10% 还是 20%"这个静态标签本身带来多少横截面信息 —— 后者在样本的大部分时间里(2019 年 7 月之前几乎全市场 10%)**近似是板块身份的代理**,这正是 §1.3 诊断的"桶=板块×代码片段"的文献侧证据。真正想用"涨跌幅限制"信息,更接近文献做法的是构造"是否临近/触及限价"这类事件型变量,而不是用 `LimitWidth` 的档位值当分组键。

### L2 出处

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|---|
| 1 | Predicting Stock Returns Using Industry-Relative Firm Characteristics | Cliff Asness, R. Burt Porter, Ross L. Stevens | 2000-02 | AQR / SSRN working paper(abstract_id=213872) | https://www.aqr.com/Insights/Research/Working-Paper/Predicting-Stock-Returns-Using-IndustryRelative-Firm-Characteristics | true |
| 2 | Measuring Mutual Fund Performance with Characteristic-Based Benchmarks | Kent Daniel, Mark Grinblatt, Sheridan Titman, Russ Wermers | 1997 | Journal of Finance, 52(3), 1035-1058 | https://ideas.repec.org/a/bla/jfinan/v52y1997i3p1035-58.html | true |
| 3 | Is Sector-Neutrality in Factor Investing a Mistake? | Sina Ehsani, Campbell R. Harvey, Feifei Li | 2021-11(工作论文,SSRN 3959116;后刊于 Financial Analysts Journal, 2023, 79(3), 95-117,该刊版日期晚于本轮截止,仅工作论文版本计入) | SSRN working paper / Quantpedia 转述 | https://quantpedia.com/should-factor-investors-neutralize-the-sector-exposure/ | true |
| 4 | Statistical Properties and Pre-Hit Dynamics of Price Limit Hits in the Chinese Stock Markets | Yu-Lei Wan, Wen-Jie Xie, Gao-Feng Gu, Zhi-Qiang Jiang, Wei Chen, Xiong Xiong, Wei Zhang, Wei-Xing Zhou | 2015-04 | PLOS ONE, 10(4), e0120312 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4395215 | true |
| 5 | Effectiveness of Price Limits: Evidence from China's ChiNext Market | Bao Qi | 2023-06 | PLOS ONE, 18(6), e0287548(收稿 2023-03-24,接受 2023-06-06,发表 2023-06-23,**在 2023-08-08 之前**) | https://pmc.ncbi.nlm.nih.gov/articles/PMC10289463/ | true |

---

## L3 —— 滚动回归斜率当横截面因子的尺度污染(对准 §1.4 / R-D,最要紧的一题)

### 文献里怎么处理"斜率天生带 1/sd(自变量)"这个问题

1. **"betting against beta"自己就是一个「斜率信号被重新加工过才敢用」的现成案例**:Frazzini & Pedersen (2014, JFE) 构造 BAB 因子时,并不是直接拿滚动回归的原始 beta 去排序/加权,而是先把时间序列 beta 向 1 做收缩(shrinkage),再按**排序**(rank)而不是原始数值去决定多空腿的杠杆,且把多空两腿都调整到市场 beta = 1(即剔除掉"整条腿到底有多大 beta 水平"这个尺度维度,只保留相对排序)。**这等于文献自己承认**:回归斜率的原始数值不能直接当横截面排序变量用,必须先做收缩和排序化处理,否则会被估计噪声和尺度效应污染。
2. **这个"污染"后来被证实是真实存在、方向明确的**:Novy-Marx & Velikov (工作论文 2018-11,后刊于 JFE 2022,143(1),80-106)专门证明 Frazzini-Pedersen 的 beta 估计量**可被市场波动率系统性、可预测地偏向**,即原始回归 beta 里混有一块"和自变量/市场波动率尺度相关、但不是真协动"的成分,这个偏差解释了 BAB 相当一部分表现。**可直接翻译到本轮**:这就是 §1.4 诊断的「`cross_regbeta` 的排序由 `sign(corr) × 1/sd(X)` 共同决定」在文献里的对应说法 —— 不是我们这次分析独创的担忧,是因子投资文献里反复出现、且已经被专门写文章证伪过的一类陷阱。
3. **相关系数、t 值、斜率三者的取舍是教科书级别但常被混用的区别**:斜率 = 相关系数 × (sd(Y)/sd(X));在简单回归里,斜率的 t 检验和相关系数的 t 检验**给出同一个显著性结论**(F 统计量就是 t 的平方),但**点估计的大小**不同 —— 相关系数和 t 值是去掉了尺度的「两者多可靠地一起动」,斜率额外带着 Y、X 各自的标准差比。**可翻译成我们的算子**:把 `cross_regbeta(X, Y, d)` 换成 `cross_corr(X, Y, d)` 就是把尺度那一项精确剔除,这正是 R-D 要做的对照,文献上这不是"猜一个消融",而是统计学里斜率/相关系数相互转换关系的直接应用。
4. **个股特征与"自身成交量"的协动,文献上有一个长达四十年的、已经被过度研究过的解释:混合分布假说(MDH)**:Clark (1973, Econometrica) 提出用一个潜在的信息到达过程同时驱动价格变化幅度和成交量,解释两者的正相关。Tauchen & Pitts (1983, Econometrica) 把它扩展成价格变化与成交量的联合分布模型。Harris (1987, JFQA)、Richardson & Smith (1994, JFQA) 等后续工作用交易数据直接检验这个假说,总体上支持"成交量和波动率的相关是因为共同受信息流驱动"这个机制,而不是两者之间有什么新的、未被研究过的结构性关系。**这对 §1.4 的判断是个佐证**:外层 `cross_regbeta(day_quantile_q75(Volume), Y, d)` 如果真有 alpha,按 MDH 文献最朴素的读法,"个股成交量和个股某个波动类变量协动"本身不是新发现,新发现只能来自**协动的方向在横截面上怎么排序**(谁的协动更强)这一层,而不是协动本身的存在——这进一步支持用 `cross_corr` 而不是 `cross_regbeta` 做诊断:若换成 corr 后排序基本不变,说明抓到的是"协动强弱"这个真正可能新的维度;若塌掉,说明抓到的只是"谁的成交量分散度小"这个和 MDH 无关的尺度人工产物。

### L3 出处

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|---|
| 1 | Betting Against Beta | Andrea Frazzini, Lasse Heje Pedersen | 2014 | Journal of Financial Economics, 111(1), 1-25 | https://ideas.repec.org/a/taf/ufajxx/v70y2014i4p24-41.html(转述该文定价与卷页信息);原文 https://www.johnhcochrane.com/s/BettingAgainstBeta.pdf | true |
| 2 | Betting Against Betting Against Beta | Robert Novy-Marx, Mihail Velikov | 2018-11(工作论文,SSRN 3300965;刊于 Journal of Financial Economics, 2022, 143(1), 80-106) | Rochester 个人主页工作论文 + 二级来源确认刊期 | https://mysimon.rochester.edu/novy-marx/research/BABAB.pdf | true |
| 3 | A Subordinated Stochastic Process Model with Finite Variance for Speculative Prices | Peter K. Clark | 1973 | Econometrica, 41(1), 135-155 | https://www.econometricsociety.org/publications/econometrica/1973/01/01/subordinated-stochastic-process-model-finite-variance | true |
| 4 | The Price Variability-Volume Relationship on Speculative Markets | George E. Tauchen, Mark Pitts | 1983-03 | Econometrica, 51(2), 485-506 | https://www.econometricsociety.org/publications/econometrica/1983/03/01/price-variability-volume-relationship-speculative-markets | true |
| 5 | Transaction Data Tests of the Mixture of Distributions Hypothesis | Lawrence Harris | 1987 | Journal of Financial and Quantitative Analysis | https://cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/abs/transaction-data-tests-of-the-mixture-of-distributions-hypothesis/2E5155033E96A3DCBAC463816C980DBB | true |
| 6 | A Direct Test of the Mixture of Distributions Hypothesis: Measuring the Daily Flow of Information | Matthew Richardson, Tom Smith | 1994 | Journal of Financial and Quantitative Analysis | https://cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/direct-test-of-the-mixture-of-distributions-hypothesis-measuring-the-daily-flow-of-information/8FCAE5652862FF3C0AE720BD52451270 | true |

**没搜到 / 弃用**:没搜到专门讨论"量化因子构造中斜率 vs 相关系数 vs t 值该怎么选"的学术论文(只搜到统计学教材级别的页面,已在正文里作为通用统计关系使用,不单独列为文献出处);中国市场"换手率/成交量与波动协动"的专题论文只搜到摘要页,方向描述不一致(有的说流动性溢价、有的说共同变动为负),没有找到能确认发表日期且方法清晰的单篇,未采用。

---

## L4 —— 流通股本变动事件(对准 N2 的 (b) 部分)

### 文献里各类流通股本跳跃事件的已知效应,与"连续因子化"的现成做法

1. **限售股解禁 / 股改解禁**:Liao, Liu & Wang (发表版 2011,题为 *Information Discovery in Share Lockups: Evidence from the Split-Share Structure Reform in China*,Financial Management, 40(4), 1001-1027;会议工作论文版本题为 *Price Discovery in Share Lockups*,首稿 2008,修订稿 2009-10)用 482 次解禁事件,在 [-120, +20] 交易日窗口里发现约 **-14% 的累计异常收益,伴随约 140% 的异常成交量**,且异常收益的方向与公司信息透明度正相关、与代理问题程度负相关。**关键点**:负向效应主要发生在解禁**之前**(市场提前消化),不是解禁当天才出现。
2. **可交易性结论可翻译成算子语言**:解禁本质上是"流通股本的一次性台阶式上升",对应到我们的叶子就是 `LogFloatShares` 的一次正向跳跃。文献里把这类事件处理成**连续因子**的标准做法,就是本轮能找到的最接近"现成做法"的东西——**事件研究法本身**:以解禁日为 0,构造一个相对日历位置的窗口变量(例如"距离解禁还有几天""解禁后第几天"),而不是把跳跃幅度本身直接当一个全市场、全历史都打分的连续特征。**可翻译**:`ts_delta(LogFloatShares, d)`(有符号的 d 日股本变化)可以近似捕捉到跳跃本身,但文献强调效应**在跳跃发生前已经部分实现**(提前消化),所以单纯看"跳跃当天或跳跃后"的 `ts_var`/`ts_delta` 可能错过大头,这是 N2/R-E 用 `ts_var(LogFloatShares, d)` 时要留意的一个文献性風险,而不是单纯"信号太稀疏"的问题。
3. **私募定增(定向增发)的解禁**:多篇研究(摘要层面)一致认为私募定增解禁前的负向超额收益**集中在解禁前的几个交易日**,但本次没能确认到一篇标题、作者、发表venue 都能核实清楚、且确定发表于 2023-08-08 之前的单篇论文 —— 这条**标记为搜到但未核实**,不作为可引用出处,只作为方向性参考。
4. **股份回购**:Gan, Bian, Wu & Cohen (2017), *Determinants of Share Returns Following Repurchase Announcements in China*, Investment Management and Financial Innovations, 14(2), 4-18,用 2000-2012 年 417 次回购公告,发现市场会综合看公司成长性和估值水平(用市盈率代理高估程度)给回购定价,高市盈率公司回购后的累计异常收益更低。**翻译**:回购对应 `LogFloatShares` 的**负向**跳跃,和解禁的正向跳跃在方向上是相反的公司行为,文献上两者的预期符号也不同 —— 这是 §4.4 节如果要把"流通股本变动"做成单一连续因子时必须用**带符号**的跳跃(而不是 `ts_var` 这种对符号不敏感的量)来分开解禁(扩股,偏负面)和回购(缩股,偏正面)两类事件的关键原因。
5. **股权质押**:Li, Liu & Scott (2018), *Share Pledges and Firm Value*(AUT 工作论文 / 2018 Manawatū Seminar Series 与 Financial Markets and Corporate Governance Conference 报告稿),用 2003-2015 年中国上市公司大股东质押样本,发现质押与公司价值**正相关**,且这个关系受国有股東是否为第一大股东、股权集中度调节。**这与另一类文献(质押引发平仓压力、推高崩盘风险)方向相反**,说明股权质押对价格的净效应在文献里**没有定论**,方向随样本期、识别方法而变。质押本身通常不直接造成 `LogFloatShares` 的跳跃(质押股份一般仍计入流通股本,只是被动受限),除非触发强制平仓导致的减持,所以它更适合作为"解释 `ts_var(LogFloatCap,d)` 为什么有时和基本面脱钩"的背景机制,而不是直接对应某个叶子字段的跳跃。

### 对"把它写成连续因子"这个子问题的诚实结论

本轮没有搜到任何一篇论文给出"把限售解禁/定增/回购这类离散公司行为,转成一个随时可读、不依赖固定事件窗口的连续横截面因子"的现成构造法。能找到的全部是**事件研究框架**(固定事件窗口 + 累计异常收益),或者是指数编制方做法里的**离散触发式调整**(例如 Morningstar 系列指数规则:自由流通股本变动达到 10% 才触发即时重新平衡,平时不连续更新),后者本质上也是阈值事件,不是连续因子。**这条标记为:搜不到现成做法**——如果 N2/R-E 要把这类事件做成连续特征,需要自己设计时间衰减核(比如距最近一次股本跳跃的天数、配合跳跃符号与幅度),而不是照抄某篇论文的方法。

### L4 出处

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|---|
| 1 | Information Discovery in Share Lockups: Evidence from the Split-Share Structure Reform in China(会议工作论文版题为 Price Discovery in Share Lockups) | Li Liao, Bibo Liu, Hao Wang | 2011(发表版);工作论文首稿 2008、修订稿 2009-10 | Financial Management, 40(4), 1001-1027 | 工作论文 PDF https://efmaefm.org/0EFMSYMPOSIUM/2010-China/papers/LLW_splitshare20091030.pdf ;发表版信息经二次搜索确认(IDEAS/RePEc 等转述) | true |
| 2 | Determinants of Share Returns Following Repurchase Announcements in China | Christopher Gan, Chao Bian, Damon Wu, David A. Cohen | 2017 | Investment Management and Financial Innovations, 14(2), 4-18 | https://businessperspectives.org/journals/investment-management-and-financial-innovations/issue-251/determinants-of-share-returns-following-repurchase-announcements-in-china | true |
| 3 | Share Pledges and Firm Value | Michelle Li, Chelsea Liu, Tom Scott | 2018 | AUT 工作论文(2018 Manawatū Seminar Series / Financial Markets and Corporate Governance Conference 报告稿) | https://openrepository.aut.ac.nz/handle/10292/12150 | true |

**搜到但未核实,未计入引用**:
- 私募定增(定向增发)解禁前负向超额收益的具体单篇论文(标题/作者/venue 在多次搜索中不稳定,很可能是把好几篇不同论文的结果混在了一起转述,没有确认到可核实的单一出处);
- 中南财经政法/深圳大学关于 A 股特质波动率异象按采样频率分裂的工作论文(发表日期无法确认在 2023-08-08 之前);
- 香港 IPO 锁定期到期的对照研究(来源页面只给出机构仓库记录,未能确认标题与作者)。

---

## 给 PI / 结构解剖员的一句话总结

L1 的 Rogers-Satchell / Yang-Zhang 分解,以及 Barndorff-Nielsen-Shephard 的连续/跳跃拆分,**都是现成的、不需要重新发明的公式**,可以直接把 §1.2 的 (a)(b) 拆开,比临时拼 `ts_var(LogFloatShares,d)` 更贴近文献做法。L2 的关键提醒是:行业内相对化在纯多头口径下不一定赢行业间差异,`BoardCode` 不是无脑更优。L3 的 `cross_corr` 对照(R-D)有整整一条因子投资文献线(BAB 的构造方式本身 + Novy-Marx/Velikov 的证伪)在背后撑着,不是本轮临时起意的消融。L4 唯一的诚实结论是:没有现成的"连续因子化"公式,解禁/回购必须用带符号的跳跃分开处理,且解禁的负向效应**提前**于跳跃本身出现。
