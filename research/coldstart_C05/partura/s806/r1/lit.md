# 文献:种子 806,B 组,第 1 轮

读入:`r1/analysis.md` §5 的四个题目(对准核心 A `day_cov(Vwap, Ret)`、N1 的无量纲路径量、`LimitWidth` 部件、
以及本环境 train 定方向 + min(train,valid) 的结构性约束)。只用 WebSearch 查到、且能确认**首版日期在
2023-08-08 之前**的论文 / 工作论文 / 研究报告;日期拿不准的在下面逐条写明「搜不到 / 拿不准,不用」,不编造。

每条处理后面用 `[键]` 标出处,键对应文末「出处列表」。同一出处可能支撑多条处理。

---

## Q1 —— 日内价格路径的时点,怎样被做成截面预测变量(对准核心 A、N1)

**能摘到的处理方式:**

1. **按半小时 / 分钟切片、看「与整个交易日同周期」的位置做收益连续性**,而不是整天合在一起看:
   半小时收益在「相隔整数个交易日的同一时段」上有显著正延续,延续约 40 个交易日;同时存在一个短期(一小时以内)
   由买卖价差驱动的反转。翻成算子语言:把 `day_*` 换成按时段切片后的 `ts_*`(例如开盘后第一个半小时 vs
   收盘前最后一个半小时分别构造,再做跨日的 `ts_corr` / `ts_delay`),不要把一天内的信息直接揉成一个标量。[H2010]

2. **把一天拆成「隔夜」与「盘中」两段分别看,两段的符号经常相反(「拔河」)**:
   在美股上,多数策略的收益几乎只来自隔夜或只来自盘中其中一段,且两段符号相反;其中动量类策略的收益几乎全部来自隔夜段。
   翻成算子语言:核心 A 的 `day_cov(Vwap, Ret)` 本身混合了全天信息,可以按 `day_first(Open)` 到上一交易日 `day_last(Close)`
   的隔夜段、与 `day_first(Open)` 到当日 `day_last(Close)` 的盘中段分别构造后再做差或分别评估,而不是只喂全天变量。[LPS2019]

3. **在 A 股上,日内(首个半小时)与隔夜两段也存在「同段延续、跨段反转」,且作者把跨段反转的来源明确归到
   T+1 交易制度(当天买入的仓位不能当天卖出,只能靠隔夜或次日盘中退出)**。这件事直接提示:
   核心 A 的时点项如果要在 A 股上有效,**预测期应避开「次日全天」这种会同时包含隔夜 + 盘中两段、符号可能互相抵消的窗口**,
   更该试「次日开盘」或「次日最后半小时」这类单一段落的目标;同一篇还报了噪声交易是可预测性的驱动来源,
   且这个效应在市场波动更高时更强(与 PLAN §2 的 `n_vol` 控制项方向一致,值得在 E 的外围里对波动分组后再看时点项)。[CGZ2019]

4. **时点项的尺度不变写法:偏度。** 用高频数据算出的「已实现偏度」(周频)对下一期收益有显著的**负向**预测力
   (低偏度分位组减高偏度分位组,周超额约 19–24bp,t ≈ 3.7),而已实现波动率本身没有这种预测力——
   这正好支持 analysis.md §1.4/§4.3 N1 的判断:**把 `day_cov` 换成 `day_skew`(偏度)是把时点信息和波动量级信息分开的标准做法**,
   且该文献里符号是**负向**(偏度越高、未来收益越低),可作为 N1 的方向参照(但方向仍应交给 GP 定,见 PLAN §1 第 1、3 条的教训)。
   预测期是**周频**,不是日频——这件事提示本环境如果直接用日频目标,效果可能不如先做 `cross_mean(·, 5)` 之类的降频平滑。[ACJV2015]

5. **把日内信息换成「不平衡」而不是「价格水平 × 收益」的协方差写法**:在中国市场上,用日内数据构造的
   买卖订单不平衡对当天内多个区间(1 分钟到 90 分钟)的收益有预测力,作者将其读成市场无效率的证据。
   这类文献普遍把不平衡变量标准化为比例(买量−卖量)/(买量+卖量)而不是原始差值,翻成算子语言是
   `div(sub(x,y), add(x,y))` 这类归一化,而不是 `sub`/`day_cov` 这种带量纲的写法——呼应 analysis.md §1.4
   「除掉量纲」的建议方向。[NNW2015]

**搜不到 / 拿不准,不用:**
- 没搜到以「price-to-VWAP」或「close-to-VWAP deviation」为直接构造变量、做 A 股或美股截面收益预测的论文
  (搜到的几篇只是把 VWAP 当机器学习特征之一,不是单独检验这个变量);这部分请按「搜不到」处理,不要当作有文献支撑。
- 没搜到专门检验「成交量加权均价 vs 时间加权均价」谁更能代表「真实交易价格水平」从而影响日内指标构造的论文;
  N2 的灵感目前只有操作上的依据(`alphacube/daily.py` 的 Vwap 定义),文献层面搜不到直接支撑。

---

## Q2 —— `day_cov` 的代理风险:已实现方差怎样被分解、价格水平/波动怎样被剥掉

**能摘到的处理方式:**

1. **按高频收益的正负号拆分已实现波动,而不是把全天波动当一个标量。** 单变量的「已实现半方差」把已实现方差拆成
   只累计负收益平方、只累计正收益平方两部分;多变量的「已实现半协方差」把协方差矩阵按两腿收益同号/异号拆成三块,
   发现「同号」部分对相关性和跳跃的信息含量和「异号」部分不一样,危机期的总协方差主要由「同号」部分驱动。
   翻成算子语言:`day_cov(Vwap, Ret)` 里隐含的 `Q`(已实现方差)这一项,可以先用正负收益分别算
   (类似 `day_sum(mul(indicator(Ret>0), Ret²))` vs 负收益那一半),再看核心的时点项在哪一半里更强——
   这是比「整体除掉 `day_var`」更细的处理,文献里证明这种拆分确实能分出不同的信息。[BNKS2010][BLPQ2020]

2. **已实现波动率相对其自身历史水平的「新息」是否是已知的截面预测变量 —— 直接相关的文献没搜到,
   但「特质波动率水平本身」是一个很成熟、方向明确的异象:截面上特质波动率越高,未来收益越低
  （用 Fama-French 三因子残差定义的特质波动率,控制了规模、账面市值比、动量、流动性后依然存在,
   且不能用对总体波动率新息的暴露来解释)。** 这条直接支持 analysis.md §1.4 的担心:
   `day_cov` 里 `P̄·Q/2` 那部分如果残差里还留着「当天波动相对 20 日均值」的信息,很可能就是在变相复刻
   这个已知的、方向为**负**的异象,而不是新信息。翻成算子语言:在核心 A 的外围里,
   应该直接把 `cross_mean(day_std(Ret), 20)`(已在控制里)之外的、**更短窗口或更当下**的波动变量额外纳入检验,
   确认残差里到底剩了多少特质波动率成分。[AHXZ2006]

**搜不到 / 拿不准,不用:**
- 没搜到专门针对「价格水平 × 分钟收益协方差」这个具体构造(即 `day_cov(Vwap, Ret)` 这种写法本身)的分解或洗白方法论文;
  Q2 要找的「分钟价格水平与分钟收益的协方差怎样被分解」更多是我(文献员)用已实现方差/半方差文献做的类比推断,
  不是文献里现成的结论,这一点要跟 PI 说清楚,不要当成直接证据。
- 中国 A 股的「低波动异象」文献结果不一致(有的报告显著为负、有的报告在排除危机期后变正、
  有的报告分位数回归里符号随分位数翻转),我只找到互相矛盾的二级来源摘要,**没有一篇我能确认发表时间且结论干净**,
  所以这条不单独列出处,只在上面提示「中国市场的方向不如 Ang et al. (2006) 的全球证据干净,不要把符号想当然搬过来」。

---

## Q3 —— `LimitWidth` / 板块这个部件,文献里怎样用;2020-08-24 创业板改革怎样被处理

**能摘到的处理方式:**

1. **把涨跌停幅度的改变当「准自然实验」,用双重差分(DiD)比较创业板(处理组)和主板/科创板(对照组)
   在 2020-08-24 前后的变化**,而不是简单地把 `LimitWidth` 当一个静态分组变量用于截面排序。
   这类研究报告:幅度从 10% 放宽到 20% 后,流动性显著改善,但波动率和「知情交易概率」也显著上升。
   翻成算子语言:如果要检验 `LimitWidth` 这个部件本身是否携带信息,应该用**改革前后的时间断点**做
   `ts_delay` / 分段的 `cross_mean` 比较,而不是像 §1.2 那样把它直接相加进一个跨期都用的因子里。[ZWHH2022]

2. **幅度放宽当天本身伴随正的收益冲击,且对「价格发现效率」没有显著影响,主要影响的是流动性和波动率**——
   提示 `LimitWidth` 的变化点(2020-08-24)附近会有一次性的收益跳变,`day_cov`、`ts_min(·,20)` 这类
   跨越该日期的窗口都会被这次跳变污染(呼应 analysis.md §1.2 对 `ts_min` 的担心),
   构造时序特征时应该把这个日期当已知断点处理,而不是让滚动窗口直接跨过去。[WZ2022]

3. **「磁吸效应」(价格接近涨跌停时,交易行为被幅度本身吸引,日内路径因此失真)这件事在创业板放宽后
   是否存在,文献结论相反:** 一篇用大幅波动分布做事件研究的论文没找到磁吸效应被放宽强化的证据;
   另一篇引入「投资者关注度」做交互项的论文发现放宽后磁吸效应反而更强,且投资者关注度对其有显著正向作用。
   翻成算子语言(后一篇的处理方式):磁吸效应不是幅度的直接函数,而是**幅度 × 关注度代理变量**的交互项
   ——这正好呼应 analysis.md §4.1 核心 A 建议里「`mul`/`div` 配 `LimitWidth` 做缩放而不是 `add`」的方向,
   且提示除了缩放,还可以试「`LimitWidth` × 换手率/成交额这类关注度代理」的交互写法作为新的外围。
   两篇结论相反这件事本身要如实告诉 PI:**磁吸效应在这个改革上是否存在,文献没有定论**,
   不能把其中任何一个方向当作先验写进奖励或种子。[BQ2023][ZLHL2023]

**搜不到 / 拿不准,不用:**
- 没搜到专门讨论**科创板 20% 限幅**(而不是创业板)对日内路径类指标污染的论文,Q3 里这部分搜不到,不用。
- 一字板 / 跌停封死后换手骤降对日内路径类指标(如 `day_cov`)具体会产生什么统计偏差,
  我没搜到直接做这个检验的论文(只有磁吸效应的间接证据),这部分按「搜不到」处理。

---

## Q4 —— 怎样的时序处理能让截面信号的符号在不同市场状态下更稳定;信号衰减大致多快

**能摘到的处理方式:**

1. **用「相对自身历史窗口的标准化分数」给因子的月度收益做时序 z-score,再用这个 z-score 给下一期的因子暴露加权**
  (而不是把原始因子值直接拿去排序)。标准化窗口用的是**扩张窗口**(expanding window,不是固定滚动窗口),
   作者报告这样做能在价值、动量、规模等多个因子上同时提升 alpha 和夏普,且对交易成本有一定稳健性,
   在衰退/危机期表现尤其好。翻成算子语言:核心 A 或 N 位的候选在**跨越 train/valid 两段**时符号不稳定的问题,
   可以试 `div(sub(x, cross_mean(x, W)), cross_stddev(x, W))` 这类"相对自身历史均值的标准化",
   W 用扩张窗口在本环境不好实现,但可以用较长的固定窗口(如 60 日)近似。[FSZ2021]

2. **用「因子半衰期」衡量一个特征的信息衰减速度,不同因子差异很大**:
   在价值、动量、质量、投资、低波动五个全球因子里,价值衰减最慢,动量和投资衰减最快;
   该研究建议的最优再平衡周期从 1 个月(投资类)到 5~6 个月(低波动类)不等。
   这件事直接提示:**本轮核心 A(日内时点类)更接近"动量/投资"这一类高频特征,预期半衰期短**,
   PLAN 环境里 `reward` 按 train 的 `long_sharpe` 选半衰期这一步,对这类因子应该更倾向选短半衰期,
   而不是套用 `LimitWidth` 这种慢变量的半衰期假设。[FV2021]

3. **用"行业内 / 分组内相对值"而不是原始特征值做排序,能把"组间效应"和"组内效应"分开,
   且两者有时符号相反**:用规模、账面市值比等特征相对所属行业的排名(而不是跨行业统一排名)预测收益,
   发现**行业内**的动量/反转效应和**跨行业**的动量/反转效应符号经常不同(短期行业内是反转、跨行业是动量)。
   这正是 analysis.md §1.2/§1.3 诊断出的问题的标准解法:`add(LimitWidth, day_cov(Vwap,Ret))` 的毛病是
   "没有分组就直接相加",而文献里的标准做法是**先按分组(行业/板块)算组内标准化分数,再在全市场排序**,
   对应算子应该是 `cs_demean`/`cs_rank` 配合一个「按 `BoardCode` 分组」的版本,而不是 `add` 一个跨组都不中性化的哑变量。[APS2000]

**搜不到 / 拿不准,不用:**
- 没搜到专门针对**中国 A 股**、给出"滚动标准化 vs 原始值"在不同市场状态下稳定性对比的论文
  (Flögel et al. 和 Flint & Vermaak 的证据都是全球/发达市场样本,不是 A 股);Q4 里"A股异象稳定性"这部分证据不足,
  只能把全球证据当类比,不能当 A 股特有的结论转述给 PI。
- 没搜到把"双重排序"(conditional double sort)直接用在日内路径类特征上的论文;
  上面第 3 条的 Asness-Porter-Stevens(2000)是行业相对特征的经典工作,但不是针对日内变量,引用时要注明这个差距。

---

## 出处列表

**[H2010]**
标题:Intraday Patterns in the Cross-Section of Stock Returns
作者:Steven L. Heston, Robert A. Korajczyk, Ronnie Sadka
年-月:2010(*Journal of Finance*, Vol. 65, No. 4, pp. 1369–1407)
来源:期刊(Journal of Finance);工作论文版本在 arXiv(ar5iv 镜像)
链接:https://ar5iv.arxiv.org/html/1005.3535 ;期刊介绍页 https://www.kellogg.northwestern.edu/academics-research/research/detail/2010/intraday-patterns-in-the-cross-section-of-stock-returns
verified: true(WebSearch 结果中多个独立来源——Kellogg 官方介绍页、arXiv 镜像、工作论文 PDF——一致确认标题、作者、期刊卷期)

**[LPS2019]**
标题:A Tug of War: Overnight Versus Intraday Expected Returns
作者:Dong Lou, Christopher Polk, Spyros Skouras
年-月:2019(*Journal of Financial Economics*, Vol. 134, No. 1, pp. 192–213)
来源:期刊(Journal of Financial Economics);作者主页挂有工作论文全文
链接:https://personal.lse.ac.uk/polk/research/TugOfWar.pdf ;LSE 版本 https://researchonline.lse.ac.uk/id/eprint/87481
verified: true(WebSearch 命中 LSE 机构库、作者个人主页 PDF、NBER 会议论文版本,标题/作者/卷期一致)

**[CGZ2019]**
标题:Intraday momentum and reversal in Chinese stock market
作者:Xiaojun Chu, Zherong Gu, Haigang Zhou
年-月:2019(*Finance Research Letters*, Vol. 30, pp. 83–88;线上记录日期 2019-09-01,DOI 10.1016/j.frl.2019.04.002)
来源:期刊(Finance Research Letters)
链接:https://ideas.repec.org/a/eee/finlet/v30y2019icp83-88.html ;机构库 https://engagedscholarship.csuohio.edu/bus_facpub/288
verified: true(WebSearch 命中 IDEAS/RePEc 条目与作者所在 Cleveland State 大学机构知识库,标题/作者/卷期/DOI 一致)

**[ACJV2015]**
标题:Does Realized Skewness Predict the Cross-Section of Equity Returns?
作者:Diego Amaya, Peter Christoffersen, Kris Jacobs, Aurelio Vasquez
年-月:2015(*Journal of Financial Economics*, Vol. 118, pp. 135–167,DOI 10.1016/j.jfineco.2015.02.009)
来源:期刊(Journal of Financial Economics);早期工作论文版本见 CREATES
链接:https://repec.econ.au.dk/repec/creates/rp/13/rp13_41.pdf
verified: true(WebSearch 命中期刊 DOI、二级摘要、CREATES 工作论文 PDF,标题/作者/卷期/DOI 一致;具体数值在工作论文版与发表版之间有微小差异,引用时按"发表版 19bp / 工作论文版 24bp 并存"处理)

**[NNW2015]**
标题:Do order imbalances predict Chinese stock returns? New evidence from intraday data
作者:Paresh Kumar Narayan, Seema Narayan, Joakim Westerlund
年-月:2015(*Pacific-Basin Finance Journal*, Vol. 34, pp. 136–151)
来源:期刊(Pacific-Basin Finance Journal)
链接:https://ideas.repec.org/a/eee/pacfin/v34y2015icp136-151.html ;作者机构页 https://ehl.lu.se/joakim-westerlund/publication/ef7f5b03-fc09-4f71-9af6-d06ef43dd8c7
verified: true(WebSearch 命中 IDEAS/RePEc 条目与 Lund University 作者机构页,标题/作者/卷期一致)

**[BNKS2010]**
标题:Measuring downside risk: realised semivariance
作者:Ole E. Barndorff-Nielsen, Silja Kinnebrock, Neil Shephard
年-月:2010(收录于 *Volatility and Time Series Econometrics: Essays in Honor of Robert F. Engle*;工作论文版本 2008 年已挂出)
来源:书章节/工作论文(Oxford 工作论文 + CREATES 工作论文)
链接:https://www.nuff.ox.ac.uk/economics/papers/2008/w2/downside.pdf ;CREATES 版本 https://repec.econ.au.dk/repec/creates/rp/08/rp08_42.pdf
verified: true(WebSearch 命中牛津大学工作论文页面与 CREATES 工作论文页面,标题/作者一致;2010 年收录出处来自 R 包 `highfrequency` 文档的引用格式,独立确认)

**[BLPQ2020]**
标题:Realized Semicovariances
作者:Tim Bollerslev, Jia Li, Andrew J. Patton, Rogier Quaedvlieg
年-月:2020-07(*Econometrica*, Vol. 88, No. 4, pp. 1515–1551,DOI 10.3982/ECTA17056)
来源:期刊(Econometrica)
链接:https://www.econometricsociety.org/doi/10.3982/ECTA17056
verified: true(WebSearch 命中 Econometric Society 官方出版页、Duke 大学机构知识库、SMU 机构知识库,三方独立来源对卷期/页码/日期一致确认为 2020 年 7 月)

**[AHXZ2006]**
标题:The Cross-Section of Volatility and Expected Returns
作者:Andrew Ang, Robert J. Hodrick, Yuhang Xing, Xiaoyan Zhang
年-月:2006(*Journal of Finance*, Vol. 61, No. 1;NBER Working Paper No. 10852 先行版本)
来源:期刊(Journal of Finance);NBER 工作论文
链接:https://www.nber.org/papers/w10852
verified: true(WebSearch 命中 NBER 官方工作论文页、哥伦比亚商学院教师研究页、SSRN 摘要页,标题/作者一致;此为高度确立的经典文献,我在本次搜索中独立复核而非仅凭训练记忆)

**[BQ2023]**
标题:Effectiveness of price limits: Evidence from China's ChiNext market
作者:Bao Qi
年-月:2023-06(*PLoS ONE*, Vol. 18, No. 6, e0287548;收稿 2023-03-24,接受 2023-06-06,发表 2023-06-23,DOI 10.1371/journal.pone.0287548)
来源:期刊(PLoS ONE)
链接:https://pmc.ncbi.nlm.nih.gov/articles/PMC10289463/
verified: true(WebFetch 直接读取 PMC 全文页面,明确给出收稿/接受/发表三个日期,发表日 2023-06-23 早于 2023-08-08 截止线)

**[ZLHL2023]**
标题:Price limit change and magnet effect: The role of investor attention
作者:Xiaotao Zhang, Xinxian Li, Jing Hao, Peigong Li
年-月:DOI 注册/线上可用于 2022-12(Crossref `created` 字段 2022-12-07);印刷版 *Finance Research Letters*, Vol. 53, 2023-05,文章号 103577,DOI 10.1016/j.frl.2022.103577
来源:期刊(Finance Research Letters)
链接:https://ideas.repec.org/a/eee/finlet/v53y2023ics154461232200753x.html
verified: true(WebFetch 直接查询 Crossref API 得到 DOI 注册/created 日期为 2022-12-07、印刷卷期为 2023-05,两者均早于 2023-08-08;标题作者经 IDEAS/RePEc 条目确认)

**[ZWHH2022]**
标题:Price limit and stock market quality: Evidence from a quasi-natural experiment in the Chinese stock market
作者:Xiaotao Zhang, Ziqiao Wang, Jing Hao, Feng He
年-月:2022(*Pacific-Basin Finance Journal*, Vol. 74,DOI 10.1016/j.pacfin.2022.101778)
来源:期刊(Pacific-Basin Finance Journal)
链接:https://ideas.repec.org/a/eee/pacfin/v74y2022ics0927538x22000737.html
verified: true(WebFetch 直接读取 IDEAS/RePEc 条目,标题/作者/卷期/DOI 明确列出,年份 2022 早于截止线)

**[WZ2022]**
标题:The effect of relaxing daily price limit: Evidence from the ChiNext market of China
作者:Xiaoyuan Wan, Jiachen Zhang
年-月:2022(*Economics Letters*, Vol. 215, 110518)
来源:期刊(Economics Letters)
链接:https://ideas.repec.org/a/eee/ecolet/v215y2022ics0165176522001318.html
verified: true(WebFetch 直接读取 IDEAS/RePEc 条目,标题/作者/卷期明确列出,年份 2022 早于截止线)

**[FSZ2021]**
标题:Momentum-Managed Equity Factors(发表版标题;SSRN 工作论文首版亦用此标题)
作者:Volker Flögel, Christian Schlag, Claudia Zunft
年-月:工作论文首版 2021-07(SSRN/SAFE Working Paper No. 317);正式发表于 *Journal of Banking & Finance*, Vol. 137, 2023(106251)——按"以首版日期为准",本条取 2021-07
来源:工作论文(SSRN / SAFE Working Paper);后发表于期刊
链接:https://publikationen.ub.uni-frankfurt.de/opus4/files/61452/SSRN-id3423287.pdf
verified: true(WebSearch 命中法兰克福大学机构知识库挂出的 SSRN 工作论文 PDF 及 SAFE 工作论文列表页,首版日期 2021-07 独立确认于两个来源)

**[FV2021]**
标题:Factor Information Decay: A Global Study
作者:Emlyn Flint, Rademeyer Vermaak
年-月:工作论文(样本期 2002-01~2019-12);二级来源(Quantpedia、AlphaArchitect)一致称其为"2021 年 12 月的研究",但 SSRN 原始页面本次被 403 拒绝访问,未能直接核实首版挂出日期
来源:工作论文(SSRN,摘要号 3986499);AlphaArchitect 称其后发表于 *Journal of Portfolio Management*
链接:https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3986499(本次访问被拒,403)
verified: false —— 标题、作者、核心结论(五因子半衰期、推荐再平衡周期)经 Quantpedia 与 AlphaArchitect 两个独立二级来源互相印证,但"2021-12"这个具体首版日期**我没有在 SSRN 原始页面上亲眼确认**(访问被拒绝),按规则标 false;给 PI 的建议是如果要引用这条,优先引用其后发表的期刊版本并让检查环节核实期刊卷期的确切出版日期。

**[APS2000]**
标题:Predicting Stock Returns Using Industry-Relative Firm Characteristics
作者:Clifford S. Asness, R. Burt Porter, Ross L. Stevens
年-月:2000-02(AQR 工作论文,日期 2000-02-24;样本期 1963-06~1998-11)
来源:工作论文(AQR Capital Management working paper)
链接:https://www.aqr.com/Insights/Research/Working-Paper/Predicting-Stock-Returns-Using-IndustryRelative-Firm-Characteristics
verified: true(WebSearch 命中 AQR 官方工作论文页面与 Scinapse 摘要页,标题/作者/日期/样本期一致确认)

---

## 给 PI 的提醒(不是指令)

1. 四个题目里,**Q1 与 Q3 的证据比较扎实**(多个独立期刊来源互相印证);**Q2 是我做的类比推断而非文献直接结论**,
   请不要把"已实现方差分解"文献当成"`day_cov(Vwap,Ret)` 这个具体写法已经被文献处理过"的证据——没有人直接处理过这个写法。
2. **Q3 磁吸效应的两篇文献结论相反**([BQ2023] 无证据、[ZLHL2023] 有证据且更强),这件事本身比任一个结论更重要:
   不要把其中一个方向当先验塞进核心 A 或 N3 的种子方向里。
3. [FV2021] 是本轮唯一一条 verified: false 的出处,原因是 SSRN 原页面访问被拒、首版日期未能亲眼核实;
   它的结论(动量类因子半衰期短、价值类长)与 [FSZ2021]、[APS2000] 的方向不冲突,可以作为旁证,
   但检查环节如果要抽查日期,这条请优先抽查。
4. 本轮没有花任何付费评估额度;以上处理方式都还没有在本环境里验证过,是否真的提升 score 需要 E/N 位的实际评估结果。
