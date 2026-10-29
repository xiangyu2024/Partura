# 文献:种子 808,B 组,第 3 轮

对应 `analysis.md` §5 的四个题目(核心 A `day_centroid(Amt)` 的时点慢分量;核心 A 的识别风险与分组变量选择;
核心 B `day_autocorr_n1(Ret)` 的微观结构噪声;N1/N2 的"排列相关"统计量家族)。只用 **2023-08-08 之前发表**的论文 / 工作论文 /
研究报告(arXiv / SSRN 以首版日期为准);拿不准首发日期的不用。

`verified: true` 表示这次确实在 WebSearch 结果或 WebFetch 页面上看到了标题 / 作者 / 刊物 / 年份这几项;没查到的如实写"搜不到",不编。
第 1、2 轮已经问过的题目和用过的出处(名义股价 / 股本轴、涨跌停、相对一跳与 LOT、Banz / Fama-French(2008)/ DGTW / GKM / George-Hwang
的组内标准化、规模非单调、Admati-Pfleiderer / Gao 等 / Heston 等 / Barclay-Warner 的日内形状统计量)本轮不重复摘录,只在必要处一句话带过
(核对过 `r1/lit.md`、`r2/lit.md` 的出处列表,本轮 14 条出处与它们没有重复)。

---

## Q1:成交的日内时点,作为持续性特征——慢分量、尾盘资金身份、2018 集合竞价的制度风险

### 处理方式(→ 算子语言)

1. **「谁在尾盘交易」决定了方向该怎么读**:Bogousslavsky [R1] 建模"部分交易者只按某个频率调仓",用约 30 年美股分钟数据发现
   规模与流动性溢价**集中实现在收盘前 30 分钟和隔夜**,小盘股在接近收盘时换手率相对大盘股上升。
   → 支持把 `day_centroid(Amt)` 的多头端定成"成交集中在早盘":如果小盘股的异常收益本来就集中在尾盘兑现,"尾盘占比高"更可能对应
   调仓 / 信息交易对象,而不只是噪声。可翻译的新处理:把连续质心换成"最后 N 根分钟占比"这种二分读法,作为 R 的一个新变体。

2. **机构 vs 散户的交易时点在 A 股是可观测、可分的,而且价格跟机构走**:Qiu, Huang, Jiang (2023) [R2] 直接在中国市场发现,
   相对散户,机构更集中在开盘和收盘附近交易,价格跟随的是机构而非散户的成交,他们用这个解释 A 股隔夜跌 / 日内涨的模式。
   → 把 Q1(iv) 从"猜"变成"有方向":成交质心靠后更可能对应机构主导的尾盘成交。他们用的是账户级数据,我们没有,
   不能直接照搬构造,但可以反过来做方向校验(质心轴的多头端应该和"机构持仓占比高"的股票错开,而不是重合)。

3. **把隔夜和日内分开检验,而不是只看全天收益**:Lou, Polk, Skouras (2019) [R3] 发现 14 个经典策略里,每个策略的收益几乎全部来自
   隔夜或全部来自日内,动量收益 **100% 来自隔夜**,他们归因于机构偏好日内交易、且交易方向与动量相反。
   → 可迁移的检验处理:把 `day_centroid(Amt)` 这条轴的 IC 拆成"隔夜收益贡献"vs"日内收益贡献"分别算。如果主要靠隔夜段实现,
   支持"尾盘资金是机构 / 信息交易者"的读法;如果主要靠日内段,则更可能是别的机制。这是诊断用的处理方式,不是构造因子的方式。

4. **被动 / ETF 资金确实把成交推向收盘,但解释力有限**:BlackRock 的全球收盘成交研报 [R4](机构研报,非学术论文)报告
   被动基金 / ETF 的创设赎回与指数再平衡集中在收盘拍卖完成,是尾盘成交占比上升的一个结构性原因,但该研报也承认
   "收盘成交量不能完全由再平衡 / 创设赎回解释"。
   → 方向上支持"尾盘重 = 被动 / 机构代理",但权重不是 100%。如果要分离这个通道,可以测"只在指数成分股 vs 非成分股内分别算
   `day_centroid(Amt)` 的 score",用某种可搜索的指数成分代理字段做分组(如果注册表里有)。

5. **A 股 2018 年引入收盘集合竞价,确实改变了尾盘成交的横截面分布,而且对小盘股影响更大**:Han, Zhao, Chen, Guo (2022) [R5]
   用双重差分法研究上交所 2018-08-20 引入收盘集合竞价,发现成交量从收盘阶段**转移到收盘前阶段**,对小盘股的影响尤其明显,
   收盘价连续性改善,但价格有效性没有明显提升。
   → **直接回答 Q1(v):这不是一个无害的制度变化**。它改变的恰恰是"成交在日内的时间分布本身",且跨市值不均匀(小盘股受影响更大),
   `day_centroid(Amt)` 测的正是这件事。样本从 2018-01 开始、改革在 2018-08-20,训练段头 8 个月和之后在"尾盘占比的生成机制"上
   可能不是同一个分布,断点又正好靠近小盘股,容易被误读成规模效应——这是一条有文献实证支持的真实制度风险,不是我们自己的猜测。

### 本题没搜到、不编的部分

- 没搜到专门把"一只股票的日内成交时间分布 / 质心"当作**独立的横截面收益预测变量**(而不是事件研究或制度评估)来检验的学术论文——
  Heston-Korajczyk-Sadka(第 2 轮已引用)最接近,但它测的是"半小时收益的跨日周期性",不是"单只股票的时点分布作为持续性特征"。
- 没搜到专门检验"相对市场平均 U 型曲线的偏离度"这个具体构造的论文。
- 没搜到把"20 / 30 日平均"和"当日值"做对照、报告"只有慢分量是信号"这个具体现象的论文——文献通常直接用低频特征,
  不会先算当日值再去平均,这个对照本身是我们构造层面的发现,不是检验层面已有的结论。

---

## Q2:分组变量怎么选——条件排序的非线性正交化

### 处理方式(→ 算子语言)

1. **"增量信息"要用非参数方法测,不能只看两两相关系数**:Freyberger, Neuhierl, Weber [R6] 用非参数(核 / 序列展开)方法同时检验
   很多特征"谁对预期收益有独立信息",发现很多被证实过的预测变量**在控制了其他特征之后没有增量信息**,而且**非线性**很重要——
   线性 Fama-MacBeth 回归会漏掉的信息,非参数方法能抓到。
   → 这给我们正在做的事一个学术说法:`cs_bucket_zscore(y, x)` 式的"在 x 的十分位内看 y"正是一种非参数 / 非线性的控制方法。
   同时提醒我们,`day_centroid(Amt)` 的增量应该在**多个控制变量同时存在**的情况下测,不只是对已知族单独测 ρ
   (目前 §1.1 的检验只做了两两;更完整的做法是把 `day_centroid(Amt)`、已知族、流动性分组变量一起放进增量检验)。

2. **"特征匹配基准"是条件正交化的另一种实现方式,而且表现好**:Bessembinder, Cooper, Zhang (2019) [R7] 提出用"市场范围内对若干
   特征(规模、账面市值比、盈利能力、资产增长、动量)做回归得到的拟合值"作为基准,拿事件后收益减去这个基准,发现很多"异常收益"
   在这个基准下大幅缩小或消失,而且一个只用 5 个特征的简单版本和更复杂模型表现一样好。
   → 这是条件标准化的"回归版"而不是"分桶版":`sub(y, 用多特征线性拟合出的期望)`。可以在 R 里加一条:把
   `cs_bucket_zscore(day_centroid(Amt), LogFloatCap)` 换成"用流动性 + 规模 + 波动做 Fama-MacBeth 拟合后的残差"
   (若可搜索注册表里有多元回归残差类算子),直接对照"分桶 vs 回归残差,哪个抓住的非线性更多"——这正是 §1.1 末那句
   可迁移的话("组内条件标准化 = 奖励的线性中性化挡不住的那次非线性正交化")的一个可做实验。

### 本题没搜到、不编的部分

- 没搜到**专门比较条件双重排序中"先按哪个变量分组"这个选择本身对结果的影响**的学术论文——能找到的只是方法论教材
  (Bali-Engle-Murray,第 2 轮已引用)对"条件排序依赖顺序"的一般性说明,没有一篇论文专门做"换成另一个分组变量,结果差多少"
  的系统比较,更没有针对"规模分组 vs 流动性分组 vs 微观结构噪声分组"三者的对照研究。
- 没搜到把"组内标准化"明确称为"非线性正交化"并和线性回归残差做数值对比(例如报告两者保留的收益预测力差多少)的论文——
  Freyberger 等人的工作最接近,但他们比较的是"非参数方法 vs 线性 Fama-MacBeth",不是"组内标准化 vs 回归残差"这个具体操作对。

---

## Q3:分钟收益 lag-1 自相关——Roll 价差、微观结构噪声、滚动上包络、中国市场

### 处理方式(→ 算子语言)

1. **构造的源头是序列(协)方差,不是"自相关系数"本身**:Roll (1984) [R8] 的估计量是
   `spread = sqrt(-2·cov(ΔP_t, ΔP_{t-1}))`,只在协方差为负时有定义;`day_autocorr_n1` 读的是相关系数(协方差除以方差),
   符号信息和 Roll 价差是同一件事,但没做"开根号"这一步非线性变换。
   → 可以直接测"把 `day_autocorr_n1(Ret)` 换成 Roll 价差本身(协方差取负、开根号、协方差为正时截断为 0)"是不是更干净的构造——
   这是 §2.5 第 13 条"AR1 系数对照"之外的另一个身份检验,而且有明确的构造公式,不需要猜。

2. **微观结构噪声会让流动性溢价被系统性高估,需要加权方法纠偏**:Asparouhova, Bessembinder, Kalcheva (2010) [R9] 证明
   价格里的测量噪声会让"用噪声代理做横截面排序"类检验产生向上偏误(噪声越大的股票,估计溢价被高估越多),建议用 WLS 替代
   OLS 纠偏,纠偏后溢价仍显著但变小。
   → 警示性的处理方式:如果 `day_autocorr_n1(Ret)` 本身是微观结构噪声的代理(§1.3 的猜测),那么"用它分组再看收益"这个操作
   本身可能产生类似偏误——分桶标准化部分缓解了问题,但可以测"用成交额加权重新算这条轴的 score,是否比等权更低"
   (加权会压低噪声大的小盘股的权重,如果 score 掉得多,说明原分数部分来自没纠偏的噪声溢价)。

3. **滞后信号在更长的跨月窗口里仍有横截面增量,但持续期比我们的构造短得多**:Subrahmanyam (2008) [R10] 发现用滞后的净委托流
   预测未来最多两个月的收益,控制了滞后收益之后仍有增量,归因于"库存控制效应"。
   → 给"用过去的流动性 / 噪声状态预测未来收益"这个大方向文献支撑,但它的持续期是"最多两个月"的净委托流,我们用的是
   "40×40 日的上包络",时间尺度长得多。可以测一个"滞后 1-2 个月的 `day_autocorr_n1(Ret)` 水平值(不做上包络)"当对照组,
   看信号衰减多快——如果两个月窗口已明显不如 40×40,说明我们的轴需要比文献典型持续期更长的平滑,这本身值得写进笔记。

4. **中国市场的 T+1 制度本身会制造日内 / 隔夜反转,需要先把这个效应剥离**:Qiu 的博士论文(2022)[R11] 的一章专门研究中国市场的
   日内收益反转和散户投资者的关系,用 2009–2021 年高频数据,报告隔夜和日内收益存在明显的持续性和反转模式,且反转强度与未来
   收益相关,把反转和 T+1 规则、散户主导联系在一起。
   → `day_autocorr_n1(Ret)` 在 A 股可能部分读到的是"T+1 导致的日内反转"这个制度性效应,而不是(或不只是)Roll 式的买卖价差
   反弹——这是 Roll 价差之外的另一个候选身份,值得在 R 里补一条"控制变量换成 T+1 相关的换手率 / 涨跌停触及次数,看
   `day_autocorr_n1` 的增量还剩多少"。

### 本题没搜到、不编的部分

- 没搜到专门用"某个股票特征的多日滚动**最大值**(而不是均值)"作为处理手法、并给出解释(例如"近期最差的流动性状态才是
  定价的那个状态")的论文——这是我们自己在 §1.2/§1.3 验证出的经验规律,文献里搜不到对应的理论或实证先例,标注为文献空白。
- 没搜到专门在**分钟频率**上应用 Roll (1984) 估计量、并报告偏误大小的论文(Roll 本人及后续 Stoll / Choi 等的改进都是日频或
  更低频的构造背景,搜到的"存在向下偏误"是低频、小样本下的一般性结论,不是专门针对分钟频率的系统研究)。
- 没搜到专门检验"A 股分钟级 lag-1 自相关读到的是买卖价差反弹还是 T+1 反转"这个具体身份问题、并给出能区分两者的实证设计的
  论文——Qiu 的论文研究的是日度的隔夜 / 日内反转,不是分钟级。

---

## Q4:为什么"排列相关"的分钟统计量活下来,"排列无关"的占比类全死

### 处理方式(→ 算子语言)

1. **Hurst 指数和"可预测性"在跨市场层面确实正相关,但这是指数级别,不是个股特征**:Eom, Choi, Oh, Jung [R12] 用 60 个国家级
   市场指数,发现 Hurst 指数(长记忆程度)越偏离 0.5,用最近邻方法预测方向的命中率越高——效率越低,越可预测。
   → 支持把 `day_hurst(Ret)` 当作一个"排列相关"统计量纳入 N2 候选,但要注意它验证的尺度是"跨市场指数、跨期",不是
   "个股横截面";这只是方向性背书,不是强证据。

2. **一个反例:运行检验 + 方差比检验在法国股票上都测不出可预测性**:Stachowiak (2004) [R13] 用 CAC40 和 MIDCAC 股票
   1999–2000 年的日内数据,同时做 Box-Pierce、运行检验(runs test)和方差比检验,结论是"无法用过去收益预测未来收益",
   符合弱式有效市场。
   → **这是一条反例,值得写进笔记**:在法国股票上,"排列相关"的检验(运行检验本身就是测排列,不是测占比)也可能测不出任何
   东西——说明"排列相关的统计量更容易有信号"不是一个普遍规律,至少不是在所有市场 / 所有频率下都成立;本种子的结果(分钟频率、
   A 股、特定处理手法下)有可能是更局部的现象,§1.5 的结论表述要加限定词。

3. **委托流自相关衰减很慢,是研究信息含量的标准框架,但没有直接检验"委托流自相关"本身作为横截面特征**:Hasbrouck (1991) [R14]
   用结构化 VAR 把委托方向和价格变化的互相冲击分解成"永久(信息型)"和"暂时(摩擦型)"两部分,这是研究委托流信息含量的经典
   方法;委托流本身自相关衰减很慢是后续文献常见的背景事实,但 Hasbrouck 本人测的是"价格对委托流冲击的反应",不是
   "委托流自相关本身能不能预测横截面收益"。
   → 如果要把"委托流自相关"做成被测量,更接近文献原意的构造是"VAR 分解出的永久冲击占比",而不是裸的自相关系数;这个构造
   需要逐笔委托数据,可能无法在当前算子语言里直接实现,需要 PI 确认数据能不能支持,否则只能当背景知识,不能当可执行的处理方式。

### 本题没搜到、不编的部分

- 没搜到直接解释"为什么依赖分钟排列顺序 / 取值重复结构的统计量比与排列无关的占比 / 集中度统计量更有横截面信息"这个一般性
  问题的论文——这更像是我们自己从 16 条种子里总结出的经验规律,文献里没有对应的理论解释;Stachowiak 的反例提示这个规律
  可能不是普遍的。
- 没搜到把"成交基尼系数"、"贴着日内高低点的时间占比"这类占比 / 集中度统计量,在**控制了常规流动性与波动之后**专门报告
  "失效"的论文。搜到一篇关于"成交量集中度"(类似 Herfindahl / Gini)和收益关系的博士论文(台湾大学,1963–2010 年美股样本),
  但拿不准其确切发表日期、也没能确认是否发表在可核实的期刊上,不列入出处。
- 没搜到专门比较"价格反转次数"(零穿越计数)和占比类统计量谁在横截面上更有效的论文。

---

## 出处列表

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|---|
| R1 | Infrequent Rebalancing, Return Autocorrelation, and Seasonality | Bogousslavsky, V. | 2015-10 工作论文(EPFL)/ 正式发表 2016-12(JF 71(6),2967-3006) | EPFL 工作论文 / Journal of Finance | https://infoscience.epfl.ch/record/229415 | true |
| R2 | When do they trade? Heterogeneous investors in China | Qiu, J.; Huang, W.; Jiang, Y. | 2023-06(FRL 54,103729) | Finance Research Letters | https://ideas.repec.org/a/eee/finlet/v54y2023ics1544612323001034.html | true |
| R3 | A Tug of War: Overnight Versus Intraday Expected Returns | Lou, D.; Polk, C.; Skouras, S. | 2015-03 工作论文(LSE FMG DP744)/ 正式发表 2019(JFE 134(1),192-213) | LSE 工作论文 / Journal of Financial Economics | https://researchonline.lse.ac.uk/id/eprint/87481 | true |
| R4 | Viewpoint: A Global Perspective on Market-on-Close Activity | BlackRock | 2020-07(机构研报) | BlackRock | https://www.blackrock.com/corporate/literature/whitepaper/viewpoint-a-global-perspective-on-market-on-close-activity-july-2020.pdf | true |
| R5 | Reexamining the impact of closing call auction on market quality: A natural experiment from the Shanghai stock exchange | Han, Q.; Zhao, C.; Chen, J.; Guo, Q. | 2022(PBFJ 74,101821) | Pacific-Basin Finance Journal | https://ideas.repec.org/a/eee/pacfin/v74y2022ics0927538x22001160.html | true |
| R6 | Dissecting Characteristics Nonparametrically | Freyberger, J.; Neuhierl, A.; Weber, M. | 2017-03(NBER WP23227)/ 正式发表 2020-05(RFS 33(5),2326-2377) | NBER Working Paper / Review of Financial Studies | https://www.nber.org/papers/w23227 | true |
| R7 | Characteristic-Based Benchmark Returns and Corporate Events | Bessembinder, H.; Cooper, M.J.; Zhang, F. | 2019(RFS 32(1),75-125) | Review of Financial Studies | https://ideas.repec.org/a/oup/rfinst/v32y2019i1p75-125..html | true |
| R8 | A Simple Implicit Measure of the Effective Bid-Ask Spread in an Efficient Market | Roll, R. | 1984-09(JF 39(4),1127-1139) | Journal of Finance | https://www.bauer.uh.edu/rsusmel/phd/roll1984.pdf | true |
| R9 | Liquidity Biases in Asset Pricing Tests | Asparouhova, E.; Bessembinder, H.; Kalcheva, I. | 2010(JFE 96(2),215-237) | Journal of Financial Economics | https://ideas.repec.org/a/eee/jfinec/v96y2010i2p215-237.html | true |
| R10 | Lagged Order Flows and Returns: A Longer-Term Perspective | Subrahmanyam, A. | 2008(QREF 48(3),623-640) | Quarterly Review of Economics and Finance | https://ideas.repec.org/a/eee/quaeco/v48y2008i3p623-640.html | true |
| R11 | Essays in Overnight Returns, Intraday Reversals, and Short-Selling Constraints in Chinese Stock Market(博士论文,第 2 章"散户与日内反转") | Qiu, J. | 2022-07 完成 / 2022-11 授予 | University of Nottingham(博士论文) | https://research.nottingham.edu.cn/files/531719892/Thesis_Jiayan.pdf | true |
| R12 | Hurst exponent and prediction based on weak-form efficient market hypothesis of stock markets | Eom, C.; Choi, S.; Oh, G.; Jung, W-S. | 2007-12(arXiv:0712.1624)/ 正式发表 2008(Physica A 387(18),4630-4636) | arXiv / Physica A | https://arxiv.org/pdf/0712.1624 | true |
| R13 | Prévisibilité des rentabilités boursières. Une étude empirique du marché boursier français sur données intraquotidiennes | Stachowiak, C. | 2004(Économie et Prévision 166(5),71-85) | Économie et Prévision | https://ideas.repec.org/a/prs/ecoprv/ecop_0249-4744_2004_num_166_5_7382.html | true |
| R14 | Measuring the Information Content of Stock Trades | Hasbrouck, J. | 1991-03(JF 46(1),179-207) | Journal of Finance | https://ideas.repec.org/a/bla/jfinan/v46y1991i1p179-207.html | true |

**搜了但没有可独立核实的文献,不编、如实列在这里(不算出处):**

- 条件双重排序"先按哪个变量分组"对结果影响的系统比较研究(Q2)。
- "组内标准化 vs 线性回归残差"数值对比(两者保留的收益预测力差多少)的专门论文(Q2)。
- 分钟频率上 Roll (1984) 估计量偏误大小的专门研究;A 股分钟级 lag-1 自相关"买卖价差反弹 vs T+1 反转"身份区分的专门实证设计(Q3)。
- 某股票特征多日滚动**最大值**(而非均值)处理手法的理论或实证先例(Q3)。
- "排列相关 vs 排列无关"统计量横截面信息差异的一般性理论解释(Q4)。
- 成交量集中度(Herfindahl / Gini 类)在控制常规流动性与波动后"失效"的专门报告——搜到一篇台湾大学博士论文疑似相关,
  但拿不准确切发表日期与是否发表于可核实期刊,不列入出处(Q4)。
- "价格反转次数"(零穿越计数)vs 占比类统计量的横截面效力对比研究(Q4)。
