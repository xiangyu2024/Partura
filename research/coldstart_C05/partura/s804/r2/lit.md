# 文献:种子 804,B 组,第 2 轮

输入:`r2/analysis.md` 第 5 节「给文献员的题目」(4 题,分别对准核心 ①`sub(day_centroid(Volume), day_centroid(Ret))`、
核心 ②`ts_regbeta(...)` 与灵感 2「尺度 vs 共动」、§1.4 的中性化方法敏感性发现、灵感 1「四个从未用过的制度/结构叶子」)。
约束:只用 **2023-08-08 之前**发表/上线/存档的论文、工作论文或机构研究报告;日期拿不准的一律不用。
第 1 轮已查过「名义股价水平」「股本/自由流通比例/非线性规模」「条件排序与段宽」「日内成交量分布」四题(见 `r1/lit.md`),
下面四题刻意避开已查过的具体论文(Weld/Michaely/Thaler/Benartzi、Birru & Wang、Green & Hwang、Pontiff & Woodgate 等不再重复)。
工具:WebSearch(多轮)+ WebFetch(核对个别条目的作者/期号/日期)。每条「处理方式」后括注的是它的出处标号,对应该题下方「文献出处」表里的条目。

---

## 题 1(对准核心 ①,§1.5):日内「成交时点」与「波动时点」的错配

### 1.1 能翻译成算子语言的处理方式

**先如实说明搜索的结论**:没有搜到一篇把「成交量的日内时点质心 − 收益/波动的日内时点质心」直接构造成一个截面预测变量、并拿去做横截面检验的论文
(搜了「intraday volume centroid vs return-variance centroid」「volume-volatility asynchrony cross-sectional predictor」等多种措辞,
搜到的都是分钟级量价关系的理论/实证文献,不是这个具体构造)。下面是能找到的、离这个构造最近的处理方式,按能抄多少排序。

1. **把"量-波动同步 vs 错位"当成两个互斥假说的对照,而不是一个任意符号的量。**
   Mixture-of-Distributions Hypothesis(量与波动同受一个共同的信息流驱动,因此应当同步)与 Sequential Information Arrival Hypothesis
   (信息依次到达不同交易者,因此量与波动应有领先-滞后结构)是这支文献里两个对立的理论框架 [①③],后续多篇实证论文用 Granger 因果
   / 滞后互相关去检验到底是同步还是领先滞后,结果并不统一(有的支持同步、有的支持领先滞后、有的两者都成立)[这部分引用未逐一核实,见下方说明]。
   → 翻译:核心①的符号(量质心领先还是滞后于收益质心)不是一个要在截面里"碰运气"的自由参数,而是对应一个可命名的经济假说;
   值得在 hypothesis 里写明"若量领先、按 SIAH 读法应该是信息优先在量上显现",并检查符号在不同波动率环境/不同板块下是否稳定
   (稳定 → 支持是结构性的领先滞后;不稳定 → 更像噪声或规模代理)。
2. **用"等成交量分桶"(volume clock)而不是"等时间分桶"去定位时点,把累计成交量而不是累计时钟时间当作横轴。**
   VPIN(volume-synchronized probability of informed trading)把一天的成交量切成等量的桶,在每个桶里算买卖不平衡,
   理由是信息到达与成交量同步,而不是与时钟同步 [②]。→ 翻译:`day_centroid` 现在的权重大概率是"分钟内成交量 × 分钟序号"
   (时间质心),可以试一个变体:按累计成交量等分出 N 个桶,质心定义成"收益的累计冲击集中在第几个成交量桶",
   这样时点错配就不再混进"这只股票今天总共成交了多快"这个信息。
3. **理论上解释"为什么量会集中在特定时段":知情交易者与有裁量权的流动性交易者都会把交易挪到冲击成本低的时段,
   而这两类交易者选的时段不一定相同。** Admati & Pfleiderer 的理论模型里,流动性交易者为了降低冲击成本而集中交易,
   知情交易者跟着流动性交易者集中交易以掩护自己,模型预测的是成交量与价格波动的日内形状相似,但并不要求两者的"重心"完全重合 [④]。
   → 翻译:这给了核心①一个具体的证伪方向——如果错配只是"流动性交易者的裁量时段"与"知情交易者的掩护时段"错开,
   那么错配应该与成交量本身的"裁量性"(例如大单占比、换手率)交互更强,而不是与波动率水平本身交互更强;
   可以在 E 的外围里试"错配 × 大单占比"而不是只做"错配 × 波动"。
4. **知情交易的时点替代构造是"交易规模结构"(中等规模交易占的累计价格变动份额),不是时间质心本身。**
   Barclay & Warner 的"隐蔽交易"假说发现:多数价格变动发生在中等规模的交易上,而不是在最大或最小的交易上,
   解释是知情交易者故意把订单切成中等大小以躲避被识别,同时在时间上分散执行 [⑤]。
   → 这提醒我们:如果核心①的预测力来自"知情交易的时点",那它本质上和"大单/中单占比"这类规模结构变量应该高度相关;
   值得检验核心①与"大单成交占比"的横截面相关,如果相关很高,说明错配可能只是规模结构的另一种写法(类似解剖员对核心②的尺度担心)。
5. **日内分钟级的量、波动、委托不平衡形状高度相似,但相似的形状本身解释不了跨越数十天的收益延续性。**
   Heston, Korajczyk & Sadka 发现同一半小时时段的收益存在跨越约 40 个交易日的延续性,而量、委托不平衡、波动的日内形状
   虽然彼此相似,却不能解释这个收益延续模式 [⑥]。→ 提示:即使核心①的"质心差"在截面上有效,也不能想当然认为
   机制就是"量波关系";这支文献的教训是量/波动/委托不平衡的日内形状本身是一个相对独立于收益延续性的现象,
   机制解释要更谨慎,E 的 hypothesis 里应避免直接写"因为知情交易在特定时段"这种未经证实的因果说法。
6. **不同的"日内异象"会在一天里不同的窗口兑现,提示按窗口切片(开盘段/午间/收盘前)比连续矩特征更贴近已知证据。**
   Bogousslavsky 发现规模与流动性溢价主要在最后 30 分钟兑现,而其他特征(盈利能力、特质波动率)的溢价是全天逐步累积的 [⑦]。
   → 翻译:核心①外围可以试"错配只在最后 30 分钟窗口内算"或"错配拆成开盘段 vs 收盘段两个独立的差",
   而不是只做整天质心的单一差值;这是一个没见过的外围方向,且有文献先例支持"分窗口"这个处理本身是常见且有效的做法。

**没找到、如实注明搜不到**:专门针对 A 股个股、把"成交质心-收益(或波动)质心"的差当成截面预测变量的实证论文;
也没找到明确把"量领先波动 vs 波动领先量,哪一边之后收益更好"直接检验过的论文。②的 MDH/SIAH 对立框架的早期原始文献
(Clark 1973 关于次生过程、Epps & Epps 1976、Tauchen & Pitts 1983、Copeland 1976、Jennings-Starks-Fellingham 1981)
里,Clark (1973) 本条独立核实过(见下表①),其余几篇只是在搜索结果的归纳摘要里被提到,我没有逐一打开核实标题/卷期,
按规矩标 `verified: false`。

### 1.2 文献出处

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|---|
| ① | A Subordinated Stochastic Process Model with Finite Variance for Speculative Prices | Peter K. Clark | 1973-01(vol. 41 no. 1, pp. 135–155) | Econometrica | https://www.econometricsociety.org/publications/econometrica/1973/01/01/subordinated-stochastic-process-model-finite-variance | true |
| ② | Flow Toxicity and Liquidity in a High Frequency World | David Easley, Marcos López de Prado, Maureen O'Hara | 2012(vol. 25 no. 5, pp. 1457–1493;早期版本 2011) | Review of Financial Studies(早期版本 SSRN) | https://papers.ssrn.com/abstract=1695596 | true |
| ③ | MDH / SIAH 理论对立框架的归纳转述(Epps & Epps 1976、Tauchen & Pitts 1983、Copeland 1976、Jennings-Starks-Fellingham 1981 的理论归因) | 多篇(未逐一核实) | 未核实 | 二级搜索结果摘要转述 | 无直接可核实链接 | false |
| ④ | A Theory of Intraday Patterns: Volume and Price Variability | Anat R. Admati, Paul Pfleiderer | 1988(vol. 1 no. 1, DOI 10.1093/rfs/1.1.3) | Review of Financial Studies | https://www.gsb.stanford.edu/faculty-research/publications/theory-intraday-patterns-volume-price-variability | true |
| ⑤ | Stealth Trading and Volatility: Which Trades Move Prices? | Michael J. Barclay, Jerold B. Warner | 1993(vol. 34 no. 3, pp. 281–305,DOI 10.1016/0304-405X(93)90029-B) | Journal of Financial Economics | https://doi.org/10.1016/0304-405X(93)90029-B | true |
| ⑥ | Intraday Patterns in the Cross-section of Stock Returns | Steven L. Heston, Robert A. Korajczyk, Ronnie Sadka | 2010(vol. 65 no. 4, pp. 1369–1407;工作论文版 2010-05,arXiv 1005.3535) | Journal of Finance | https://ideas.repec.org/a/bla/jfinan/v65y2010i4p1369-1407.html | true |
| ⑦ | The Cross-Section of Intraday and Overnight Returns | Vincent Bogousslavsky | 2021(vol. 141 no. 1, pp. 172–194;工作论文版本更早,job-market paper 标注 2016) | Journal of Financial Economics | https://ideas.repec.org/a/eee/jfinec/v141y2021i1p172-194.html | true |

---

## 题 2(对准核心 ②与灵感 2,§1.1):滚动回归系数当特征——beta、t 值还是相关系数?尺度是不是流动性代理?

### 2.1 能翻译成算子语言的处理方式

1. **文献里把"滚动回归的斜率"直接当成特征使用时,几乎都保留原始系数(带量纲),而不是取 t 值。**
   Pástor & Stambaugh 的流动性度量 γ 就是"签了号的成交量"对"超额收益反转"做日度回归后的**系数本身**(不是 t 值、不是相关系数),
   γ 越负代表越不流动,且直接把这个带量纲的系数当月度特征用,最后再做横截面平均 [①]。
   → 这与我们核心②里"`ts_regbeta` 单独 +1.44、`ts_reg_tvalue` 单独 −0.14"的发现方向一致:**文献的标准做法恰好是用 beta 而不是 t 值**,
   但文献这样做的理由是把 beta 的量纲(1/σ_x)直接解释成"流动性"或"价格冲击"本身,而不是把它当成一个与流动性无关的新信号。
   这支持解剖员的担心,而不是反驳它:核心②如果真的只是在复刻"反转系数"这类已知流动性构造,那它的 beta 相对 t 值的优势
   可能恰恰来自"混入了流动性的量纲",不是新信息。
2. **Amihud 的非流动性指标本身就是一个"比值型"(斜率的简化版)特征,并把这个比值直接解释为价格冲击系数。**
   ILLIQ = 日度 |收益| / 成交额,再取一段时间的平均,Amihud 把它读成"每一元成交额带来的价格变动百分比",
   即单位成交量的价格冲击 [②]。→ 这是比滚动回归斜率更简单的"尺度型"构造,但处理方式相同:分子分母都不做横截面标准化,
   直接用原始比值的横截面排序。可以把这个思路反过来用在核心②上:做一个"纯尺度比值"版本(例如 `day_mean(Amt)` 的滚动波动
   除以收益波动,不经过任何回归)作为核心②的简化对照,如果分数接近,说明核心②基本是 Amihud 式流动性代理的一个复杂写法。
3. **Kyle 的价格冲击系数(λ)理论上就是"收益对签了号的订单流做回归"的斜率,后续实证文献在把它当特征使用前,
   做法并不统一:有的直接用结构公式估计出的 λ,有的先标准化。** Kyle 的原始模型给出 λ = 价格变动/签了号的订单流 [③];
   后续用日频订单流回归估计 λ 并检验其横截面预测力的实证工作存在,但据搜索结果,其附录里对"回归要不要去中心化/要不要标准化"
   这一点的说明是模糊的,属于复现者自行决定的实现细节 [这一条本身未独立核实出处,如实注明]。
   → **没找到**专门讨论"同一位置上 beta vs t 值 vs 相关系数三者对比、并明确报告哪个更适合做横截面特征"的论文,
   这是一处明确的文献空白。可以理解为:文献的默认做法是"选哪个" 取决于你把这个量解释成什么经济对象
   (price impact → 要带尺度的 beta;co-movement shape → 要 t 值或相关系数),而不是哪个统计上更稳健。
4. **去掉尺度污染的标准处理是"先把特征在横截面上标准化/转成秩,再使用",而不是直接把带量纲的原始回归系数拿去用。**
   Gu, Kelly & Xiu 在构造机器学习特征时,把每个特征在每个时间截面上转成排名并映射到 [−1, 1] 再喂进模型,
   目的正是让不同量纲、不同尺度的特征可比、且不被尺度本身的大小左右 [④]。
   → 这是一条具体可执行的建议:对核心②做一次消融——把 `day_median(Volume)` 自身先在横截面上排序/标准化,
   再做同样的两层嵌套回归,如果 enrichment(+3.40)大幅下降,说明核心②的分数主要来自"原始尺度"本身,
   而不是"嵌套回归结构"这个新写法;这比我们现在"把尺度单独拎出来算一次"更贴近文献的标准诊断方式,
   且是机械核心卡与机械 R 候选都不会生成的组合(两者都不包含"先标准化输入再重复同一结构"这一类变体)。
5. **换成无量纲的相关系数(或 R²)是文献里把"量价弹性/斜率"和"非流动性尺度"分开的常见手法,但这条本身没有找到专门论文证实。**
   这条是从①②③的构造方式反推出来的推论,而不是某篇文献明说的结论,如实标注为推论而非引用。

### 2.2 文献出处

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|---|
| ① | Liquidity Risk and Expected Stock Returns | Ľuboš Pástor, Robert F. Stambaugh | 2003(vol. 111 no. 3, pp. 642–685,DOI 10.1086/374184) | Journal of Political Economy | https://www.johnhcochrane.com/s/pastor_stambaugh_jpe.pdf | true |
| ② | Illiquidity and Stock Returns: Cross-Section and Time-Series Effects | Yakov Amihud | 2002(vol. 5,Journal of Financial Markets) | Journal of Financial Markets | https://www.cis.upenn.edu/~mkearns/finread/amihud.pdf | true |
| ③ | Continuous Auctions and Insider Trading | Albert S. Kyle | 1985-11(vol. 53 no. 6, pp. 1315–1336,来源对末页页码有 1335/1336 两种说法) | Econometrica | https://www.econometricsociety.org/publications/econometrica/1985/11/01/continuous-auctions-and-insider-trading | true |
| ④ | Empirical Asset Pricing via Machine Learning | Shihao Gu, Bryan Kelly, Dacheng Xiu | 2020(DOI 10.1093/rfs/hhaa009;早期版本 NBER WP 25398,2018-12) | Review of Financial Studies | https://papers.ssrn.com/abstract=3159577 | true |

---

## 题 3(对准 §1.4 这条方法发现):中性化/控制的方式本身会不会改变一个尾部异象的结论?

### 3.1 能翻译成算子语言的处理方式

**先如实说明搜索的结论**:没有搜到一篇直接把"同一个信号,分别用回归残差中性化 / 分组内重排 / 双重排序三种方法,
比较结论差多少"当成主题的论文;也没有搜到专门讨论"纯多头相对多空组合,对信号分布非多头端形状的敏感度有何不同"的论文。
下面是能确认支持"控制方式/阈值选择会改变结论"这个方向的、经过核实的证据,以及它们各自能抄的具体处理方式。

1. **剔除微盘股的方式(用 NYSE 口径断点 + 市值加权,而不是全市场断点 + 等权重)本身就能让大多数已发表异象失去显著性,
   原因几乎全部来自小盘股被等权重放大。** Hou, Xue & Zhang 用 NYSE 断点加市值加权复现 452 个已发表异象,
   发现 65%(单检验门槛 |t|≥1.96)到 82%(多重检验门槛 |t|≥2.78)不再显著;微盘股(按 NYSE 市值第 20 百分位定义)
   只占全市场 3% 的市值,却在等权重、全市场断点的常见做法里占了 60% 的样本数 [①]。
   → 这是对 §1.4 发现的直接外部印证:**阈值/断点/权重方案不是工程细节,是会单独决定"有没有这个异象"的变量**。
   翻译到我们的语境:§4.2 候选 12(只改分布下半部分、不改多头持仓)问的正是同一个问题;
   建议在报告里把"用全样本断点"和"按某个制度/规模分组内断点"两种阈值方案的 score 都给出,而不是只报一个。
2. **A 股特有的、与"规模"方向一致但机制不同的阈值先例:剔除最小的一段股票,理由是"壳价值污染",不是"流动性"。**
   Liu, Stambaugh & Yuan 在构造中国的规模因子时,直接剔除最小的 30% 股票,理由是这部分股票里约 30% 的市值反映的是
   被借壳重组的潜在价值(因为 IPO 审批门槛高,最小的上市公司变成稀缺的壳资源),这部分股票的收益与基本面
   (用盈余超预期代理)的关系更弱、与 IPO 活动的关系更强 [②]。
   → 这是一个**必须写进风险清单**的提醒:我们现在筛"最便宜 5%/10%/20%"主要是在价格维度上筛,
   但在 A 股,"最小市值的一段"同时携带"壳价值"这个完全不同的机制;如果核心③/价格族的尾部筛选阈值恰好与
   "壳资源股"高度重叠,那么这条轴测出来的"低价溢价"有一部分可能是壳价值溢价,而不是题 1(第 1 轮)讨论的名义价格效应。
3. **退市收益缺失对异象的影响不是单向的,会让某些异象变强、另一些变弱,取决于异象本身的方向。**
   Shumway 发现 CRSP 对很多因负面原因(如破产)被摘牌的公司缺失了退市收益,这部分缺失的收益往往非常差,
   后续研究发现补上这部分缺失收益会让某些策略(基于盈余、现金流、账面市值比)的收益增加,
   让另一些策略(基于应计利润)的收益减少 [③]。
   → 翻译:我们纯多头书对"停牌/退市/ST"股票的价格处理方式(停牌期怎么填、退市价怎么定)如果改变,
   不能假设所有 head 的分数都往同一个方向移动;§4.2 候选 12 与阈值敏感性检验应该和"退市/停牌处理方式"的敏感性一起报告,
   而不是分开看,两者可能相互抵消或相互放大。
4. **长仅(long-only)版本的异象本身仍然显著,做空成本不是决定性因素——但这回答的是"纯多头是否仍有异象",
   不是"中性化方式会不会改变多头端的结论"这个更具体的问题。**
   一项对七个经典异象(规模、价值、盈利能力、投资、动量、应计、净发行)1963–2016 年的检验发现,
   仅做多头部的组合依然有显著的时间序列 alpha,做空成本只占平均空头 alpha 的约 15%(市值加权口径)[④]。
   → 这条只能当背景支撑用,不能直接回答 §1.4 的具体问题(中性化方法改变分布非多头端形状、从而改写多头持仓),
   如实标注为间接证据。

**没找到、如实注明搜不到**:直接比较"回归残差中性化 vs 分组内重排 vs 双重排序"三种方法在同一个信号上结论差异的论文;
专门讨论"纯多头组合对信号分布非多头端形状的敏感度"的论文;"筛选阈值该如何定、该不该报告阈值敏感性"的方法学综述类论文
(搜到的都是具体异象论文里顺带用到某个阈值,没有搜到专门讨论这个选择本身的方法论文章)。

### 3.2 文献出处

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|---|
| ① | Replicating Anomalies | Kewei Hou, Chen Xue, Lu Zhang | 2020(vol. 33 no. 5, pp. 2019–2133;工作论文版 2017-05,NBER WP 23394) | Review of Financial Studies | https://www.nber.org/papers/w23394.pdf | true |
| ② | Size and Value in China | Jianan Liu, Robert F. Stambaugh, Yu Yuan | 2019(vol. 134, pp. 48–69) | Journal of Financial Economics | https://faculty.wharton.upenn.edu/wp-content/uploads/2018/03/Size-and-Value-in-China.pdf | true |
| ③ | The Delisting Bias in CRSP Data | Tyler Shumway | 1997(vol. 52 no. 1, pp. 327–340) | Journal of Finance | https://ideas.repec.org/a/bla/jfinan/v52y1997i1p327-40.html | true |
| ④ | 长仅版本经典异象仍显著、做空成本占比有限的研究(七个 CAPM 异象,1963–2016) | 未能确认具体作者/标题(搜索结果仅给出发现内容,未独立核实论文标题与作者) | 未核实 | 二级搜索结果转述(疑似经由 quantpedia/cxoadvisory 等转述) | 无直接可核实链接 | false |

---

## 题 4(对准灵感 1,§4.3):A 股的制度/股本结构标签当分段条件——限售比例、涨跌幅制度、板块

### 4.1 能翻译成算子语言的处理方式

1. **把"自由流通比例"直接当成一个独立于规模的横截面因子使用,能显著提升模型对 A 股收益的解释力。**
   Wang & Xu 把自由流通比例(可自由交易的股份占总股本的比例)作为规模因子之外的第二个 A 股专有因子加入模型,
   理由是国有股占比高、会计信息质量低,自由流通比例可以当成公司基本面的一个代理;加入后三因子模型对市场模型的
   解释力从 81% 提升到 90% [①]。→ 直接支持灵感 1:`sub(LogTotalCap, LogFloatCap)`(= 限售/非自由流通比例)
   作为一个独立因子使用(不只是分段条件,也可以直接当排序变量),在 A 股文献里有现成的先例和明确的经济解释
   (国有股/限售股比例高 → 代理问题更重 → 应该有独立于规模的定价含义)。
2. **A 股"最小一段股票"剔除的理由是壳价值,不是流动性或规模本身——这意味着限售比例与"最小市值"不是同一件事,
   值得分开处理而不是互相替代。** 同题 3 的 ②:最小 30% 股票里约 30% 市值是壳价值 [②]。
   → 翻译:灵感 1 里"限售比例"这个变量和"市值"这个变量在 A 股的机制解释不同(一个是国企/控股股东代理问题,
   一个是壳资源稀缺性),用 `sub(LogTotalCap, LogFloatCap)` 做分段条件时,应该在控制了 `LogFloatCap` 之后看它是否仍有信息,
   而不是直接把它当成规模的另一种写法去跳过。
3. **涨跌幅限制(10% vs 20%)本身有自然实验式的文献可用:ChiNext 从 10% 放宽到 20% 这个制度变更,
   被直接用来检验限价制度对价格发现、波动率、交易行为的影响,2023-06 发表、在我们的日期线之前。**
   Bao Qi 比较 ChiNext 2020-02~07(10% 限制下触及 10%)与 2020-10~2021-03(20% 限制下突破 10%)两组事件,
   发现限价制度延迟价格发现、产生波动溢出、干扰交易,下跌方向触及限制时效应更强,且没有发现"磁吸效应"的证据 [③]。
   → 翻译:`LimitWidth`(10%/20%/ST 的 5%)作为分段条件,文献给出的具体切法是"按触及限制的方向(涨停/跌停)分开看",
   而不是只按宽度本身分组;下跌方向的限价效应系统性更强,这给了一个具体、有文献支持的交互方向:
   错配/尾部类信号 × (是否为跌停更敏感的限价宽度)。
4. **涨跌停触及后"延续比反转更常见",且涨停/跌停在日内的时点分布不同(涨停多在开盘附近,跌停多在收盘前一小时),
   方向上存在明显的牛熊市/涨跌不对称。** 万昱磊等用 2000–2011 年全部 A 股普通股(剔除 ST 的 ±5% 限制股)算出:
   跌停后次日延续概率(75.9%)高于涨停后(63.7%);涨停收在涨停价的比例(65.3%)高于跌停收在跌停价(51.0%);
   涨停集中在开盘附近触发,跌停更多在最后一小时触发 [④]。更早的 Chen, Rui & Wang 发现涨跌限制对**上涨方向**延迟价格发现,
   对下跌方向没有这个效应,且牛熊市下结论不同 [⑤]。
   → 这两条合起来给出一个具体、可操作的提醒:`LimitWidth` 与 `BoardCode` 的分段效果很可能**方向不对称**
   (涨停和跌停不是同一个机制的两个符号,而是两种不同的现象,日内时点也不同);
   如果核心①(日内时点错配)与涨跌停制度交互,涨停段和跌停段应该分开报告,不要合并成一个"触及限制"的哑变量。

**没找到、如实注明搜不到**:专门比较"主板 vs 创业板 vs 科创板 vs 北交所"之间某个具体异象(动量、反转、我们的任一轴)
是否存在显著差异的论文(搜到的是板块间估值差、流动性结构差异的描述性报道,不是异象检验);
专门把 ST/`*ST` 制度标签当成截面预测变量或分段条件、且能确认 2023-08-08 之前发表的实证论文
(搜到的是对 ST 制度规则本身的描述和二级转述的"Wang (2012)"一条发现,未能独立核实该论文的标题、期刊与确切年份,
按规矩不采用、不计入表格);解禁事件对 A 股个股横截面收益预测力的专门论文(搜到的是对 IPO 解禁后流动性下降的描述,
不是收益预测检验)。

### 4.2 文献出处

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|---|
| ① | What Determines Chinese Stock Returns? | Fenghua Wang, Yexiao Xu | 2004-11(vol. 60 no. 6) | Financial Analysts Journal | https://rpc.cfainstitute.org/research/financial-analysts-journal/2004/what-determines-chinese-stock-returns | true |
| ② | Size and Value in China(与题 3 出处②相同,此处用其"壳价值剔除"部分) | Jianan Liu, Robert F. Stambaugh, Yu Yuan | 2019(vol. 134, pp. 48–69) | Journal of Financial Economics | https://faculty.wharton.upenn.edu/wp-content/uploads/2018/03/Size-and-Value-in-China.pdf | true |
| ③ | Effectiveness of price limits: Evidence from China's ChiNext market | Bao Qi | 2023-06(收稿 2023-03-24,接受 2023-06-06;vol. 18 no. 6, e0287548) | PLoS ONE | https://pmc.ncbi.nlm.nih.gov/articles/PMC10289463/ | true |
| ④ | Statistical Properties and Pre-Hit Dynamics of Price Limit Hits in the Chinese Stock Markets | Yu-Lei Wan, Wen-Jie Xie, Gao-Feng Gu, Zhi-Qiang Jiang, Wei Chen, Xiong Xiong, Wei Zhang, Wei-Xing Zhou | 2015-04(vol. 10 no. 4, e0120312) | PLoS ONE | https://pmc.ncbi.nlm.nih.gov/articles/PMC4395215/ | true |
| ⑤ | The Effectiveness of Price Limits and Stock Characteristics: Evidence from the Shanghai and Shenzhen Stock Exchanges | Gong-meng Chen, Oliver M. Rui, Steven Shuye Wang | 2005(vol. 25 no. 2, pp. 159–182) | Review of Quantitative Finance and Accounting | https://ideas.repec.org/a/kap/rqfnac/v25y2005i2p159-182.html | true |

---

## 5. 给 PI 的小结(4 题各一句)

- **题 1**:没找到现成的"量-波动质心差"预测变量,但 MDH/SIAH 的理论对立、VPIN 的"等量分桶"、Admati-Pfleiderer 的
  "裁量交易时段"机制、Barclay-Warner 的"中等规模交易"视角,都指向核心①外围值得试的具体方向(等量分桶、按大单占比交互、
  按日内窗口切片),而不是反驳核心①本身。
- **题 2**:文献的标准做法印证了解剖员的怀疑——把滚动回归**系数**(带量纲)直接当特征用、并解释成流动性/冲击成本,
  是 Pástor-Stambaugh、Amihud 两条主线的共同做法;没找到专门比较 beta/t 值/相关系数三者优劣的论文,
  但"先标准化再用"(Gu-Kelly-Xiu)是一个具体可做的消融,比"单独测尺度项"更贴近文献的诊断方式。
- **题 3**:阈值/断点/权重方案会单独决定"有没有异象"这件事,在 Hou-Xue-Zhang 的全市场证据与 Liu-Stambaugh-Yuan 的
  A 股壳价值证据里都被坐实;没找到直接回答"中性化方法 vs 纯多头持仓形状"这个具体问题的论文,这仍是一处方法论空白,
  §1.4 的发现本身可能是比现有文献更直接的证据。
- **题 4**:自由流通比例在 A 股文献里有独立因子的先例(Wang & Xu);涨跌停制度的效应有明确的方向不对称
  (跌停延续更强、涨停/跌停日内时点不同,Bao Qi / 万昱磊等 / Chen-Rui-Wang);板块(`BoardCode`)与 ST 标签
  作为分段条件,没找到可用的专门异象文献,这两个标签上的 N 想法要更依赖我们自己的数据,而不是文献先验。
