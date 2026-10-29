# 文献笔记 —— 种子 801,第 1 轮

对应 `analysis.md` §5 的四个题目。检索工具:WebSearch(多数为 standard 模式)+ WebFetch(用于核对关键文献的标题/作者/日期/摘要原文)。
**只用 2023-08-08 之前发表/首版的文献**;日期拿不准的文献已标注或弃用(见各题末尾「查过但没用」)。多数出处是通过网页摘要间接确认的(搜索引擎返回的摘要/第三方引用页),已在 `verified` 字段注明来源可靠程度;凡是我直接打开原文(或原文的可下载 PDF)看到正文或摘要原文的,标 verified: true 并注明「已读原文/摘要」。

---

## 题目 1(对准核心:低名义股价 —— `LogFloatShares` 残差 ≈ −log(股价))

**结论先行**:文献对"名义股价水平"这个特征的处理,可归纳成四类可翻译的操作:

1. **取 log(价格),而不是原始价格或价格分位**。几乎所有文献(从最早的 Weld et al. 2009 到 Birru & Wang 2016)都用 log(price) 作为名义股价水平的度量,因为原始价格分布极度右偏。
   → 翻译:`log(day_last(Close))`,与我们 R 组第 4 条变体一致。
2. **必须先剥离"原始价格由基本面/贴现率决定"的成分,否则效应被稀释或误判**。Birru & Wang(2016)明确指出:直接对原始价格排序会把"名义价格溢价"和"基本面贴现率效应"混在一起,他们改用基于每股账面值等会计量构造的"拟合价格"(fitted price)——即把价格中由基本面解释的部分去掉,只留名义水平的部分。
   → 翻译:这正是我们 R 组第 6、7 条要验证的"管道假象"问题的反面——文献里这步是主动做的,而不是像我们这样事后怀疑。可以理解为"先对 log(Close) 做一次关于市值/账面值的截面回归,残差才是干净的名义价格因子"。
3. **在控制市值之后仍然做实证,并且按"难套利程度"分组、按情绪周期分段**。Birru & Wang 发现溢价在难套利股票(小盘、低机构持股、高波动)中更强,在高情绪时期之后更强。这是"按条件分组再看"的典型处理。
   → 翻译:与 `day_std(Ret)`(波动)、换手率类字段做交互项,而不是单独使用。
4. **和"彩票偏好 / MAX 效应"的度量要么证明是独立贡献,要么证明是混淆变量,必须分开检验**。Bali, Cakici & Whitelaw(2011)的 MAX(月内最大单日收益)效应被 Birru & Wang 证明和名义价格溢价是两回事(控制偏度、特质波动率、MAX 之后名义价格溢价依然显著)。Kang & Shim(2014,韩国市场)则发现 MAX 效应在散户交易占比高的股票中更强,且高 MAX 股票本身就是"小盘、低价、高特质波动"的股票。
   → 翻译:我们 R 组目前只检验"是不是股价水平"(#3、#4)和"是不是管道假象"(#6、#7),文献提示还应该做的、但这轮没做的一条敏感性:把这个因子与 `day_std(Ret)`、换手率类代理做正交化,确认它不是 MAX/特质波动的马甲——建议写进 N 候选或下一轮 R。
5. **用股票分拆(送转股)作为"价格水平外生变化"的自然实验**。Green & Hwang(2009)发现分拆后,股票的收益与低价股组的共动性上升、与高价股组的共动性下降,而基本面、规模、流动性都没变——证明价格水平本身(不是它关联的任何基本面)驱动了共动性。
   → 翻译:A 股的"送转股"是对应的自然实验,可以用 `ts_delta` 在送转股事件前后对比,但这是一个新的构造方向,不是本轮核对项。
6. **"迎合理论"(catering)对立面的证据要知道**:Baker, Greenwood & Wurgler(2009)提出管理层会在投资者偏好低价股时主动把新股/分拆后价格定得更低(迎合动机)。但 Perez & Shkilko(2017)用更稳健的方法重新检验后发现,原始检验的持续性数据容易产生伪回归,调整后"分拆响应迎合动机"的证据很弱,对 IPO 定价的证据也混杂。
   → 对我们的启示:如果核心 1(`LogFloatShares`)的真实来源确实是股价水平,不该简单假设"低价 = 公司主动选择的信号",迎合理论本身在样本外并不稳固。

### 出处

1. **The Nominal Share Price Puzzle**
   作者:William C. Weld, Roni Michaely, Richard H. Thaler, Shlomo Benartzi
   年-月:2009-春(Journal of Economic Perspectives vol. 23, no. 2)
   来源:期刊(Journal of Economic Perspectives, AEA),DOI 10.1257/jep.23.2.121
   链接:https://ideas.repec.org/a/aea/jecper/v23y2009i2p121-42.html
   verified: true(已读摘要/条目详情,卷期页码、DOI 核实一致)

2. **Price-based return comovement**
   作者:T. Clifton Green, Byoung-Hyoun Hwang
   年-月:2009(Journal of Financial Economics, vol. 93, no. 1, pp. 37–50)
   来源:期刊(JFE)
   链接:https://ideas.repec.org/a/eee/jfinec/v93y2009i1p37-50.html
   verified: true(已读摘要/条目详情)

3. **Nominal Price Illusion**(工作论文期题目:"The Nominal Price Premium")
   作者:Justin Birru, Baolian Wang
   年-月:工作论文 2015-15(Ohio State Dice Center,后于 2016 发表于 Journal of Financial Economics, vol. 119, no. 3, pp. 578–598)
   来源:期刊(JFE)+ 作者个人主页 CV 交叉核实
   链接:https://ideas.repec.org/p/ecl/ohidic/2015-15.html ;发表版 DOI 10.1016/j.jfineco.2016.01.027
   verified: true(通过作者 CV 与 IDEAS 条目交叉核实卷期页码一致)

4. **Maxing Out: Stocks as Lotteries and the Cross-Section of Expected Returns**
   作者:Turan G. Bali, Nusret Cakici, Robert F. Whitelaw
   年-月:2011(Journal of Financial Economics, vol. 99, pp. 427–446;NBER working paper w14804 更早流通)
   来源:期刊(JFE)+ NBER 工作论文
   链接:https://www.nber.org/papers/w14804.pdf
   verified: true(已读摘要,核心发现与卷期页码核实一致)

5. **복권 성향의 주식에 대한 선호와 주식수익률의 횡단면**(英译:Lottery-Like Stocks and the Cross-Section of Expected Stock Returns in the Korean Stock Market)
   作者:강장구(Jangkoo Kang)、심명화(Myunghwa Shim)
   年-月:2014-05(《재무연구》/Journal of Finance Studies,韩国财务学会,第 27 卷第 2 号,pp. 297–332)
   来源:期刊(韩国财务学会)
   链接:https://m.earticle.net/Article/A238246
   verified: true(WebFetch 直接打开页面读到标题、作者、期刊、年月、摘要原文)

6. **Catering through Nominal Share Prices**
   作者:Malcolm Baker, Robin Greenwood, Jeffrey Wurgler
   年-月:2009-12(Journal of Finance, vol. 64, no. 6, pp. 2559–2590)
   来源:期刊(Journal of Finance)
   链接:https://ideas.repec.org/a/bla/jfinan/v64y2009i6p2559-2590.html ;NBER 版 https://www.nber.org/papers/w13762.ack
   verified: true(卷期页码、DOI 经多条来源交叉核实)

7. **Catering Through Nominal Share Prices Revisited**
   作者:M. Fabricio Perez, Andriy Shkilko
   年-月:2017-03(Critical Finance Review, vol. 7, no. 1, pp. 43–75)
   来源:期刊(Critical Finance Review)
   链接:https://ideas.repec.org/a/now/jnlcfr/104.00000042.html
   verified: true(已读摘要/条目详情)

**查过但没用**:Hwang & Lu(2008)——搜索工具最初给出的归因经交叉核对后判断是误引(很可能与 Green & Hwang 2009 混淆),找不到独立存在的"Hwang and Lu (2008)"原文,弃用。Hammerich(2021)关于 41 国名义价格效应的博士论文——2021 年发表,晚于我们的截止日,只做背景了解,不作为可引用处理方式的出处。

---

## 题目 2(对准核心的"代理"问题:股数 vs 市值)

**结论先行**:文献里把"股本数量 / 流通比例"从市值里剥离出来,主要用三类可翻译的处理:

1. **把浮动股本(流通股/自由流通比例)当成一个与市值并列、但独立的回归变量,而不是市值的子集**。Wang & Xu(2004)对中国 A 股的三因子模型显式加入"自由流通"代理变量,解释力从 81% 提升到 90%,证明在市值之外,流通股结构本身带有定价信息。
   → 翻译:这正是 PLAN 环境里 `LogFloatShares`、`LogFloatCap`、`LogTotalCap` 三个叶子分开存在的理由——文献支持"不要把它们合并成一个市值变量"。
2. **把"流通股規模"和"非流通股規模"分开检验,分离出真正的规模效应 vs 流动性效应**。Cui & Wu(2007,工作论文)利用中国特有的流通股/非流通股二元结构做分解:用非流通股规模(不受交易驱动)作为"纯规模"的代理,发现它在控制了流动性指标和流通股规模之后依然显著,但效应远弱于流通股规模本身——说明中国的"规模效应"里,流动性成分比纯规模成分更强。
   → 翻译:这是我们 §1.4(b)"残留规模曲率"假说的直接文献支持方法论——用另一个规模相关但构造不同的字段(`LogTotalCap` vs `LogFloatCap` vs `LogFloatShares`)做横向比较,正是本轮 R 组第 5、12 条在做的事。
3. **把流通股规模(float)和换手率放在一起看,流通股小的股票换手率异常高被解释为"投机驱动"而非"流动性驱动"**。Mei, Scheinkman & Xiong(2004)用中国 A/B 股溢价研究发现:A 股流通盘小、换手率高达年化 500%,且换手率能解释大部分 A-B 股溢价的截面差异,作者将其归因于投机交易而非流动性,流通盘越小、越容易被炒作。
   → 翻译:支持把 `LogFloatShares` 或 `LogFloatCap` 与换手率/`Amt` 类字段做交互,而不是单独使用——这是本轮定位工具没做但文献支持优先尝试的交互方向。
4. **工业界标准做法:把"非线性规模暴露"构造成"规模的三次方,再对线性规模做回归取残差",这与我们的 `pow_3` 管道假象假说几乎是同一个操作**。MSCI Barra 的美股模型 USE4(Menchero, Orr & Wang, 2011-08 方法论文档)和中国股票模型 CNE5(2012-07)都包含一个标准风格因子"Non-linear Size"(非线性规模):把标准化后的 log(市值)取三次方,再对线性 Size 因子做(加权)回归正交化,最后做缩尾和标准化。这是成熟多因子模型里"故意构造、再扣除线性规模"的标准操作,而不是意外产物。
   → **这对本轮最关键的启示**:业界把"三次方规模暴露"当作一个独立的、需要专门正交化处理的风格因子,说明 `pow_3(pow_3(pow_3(LogFloatCap)))` 这类写法如果不做类似的正交化,很可能正是在拾取这个已知的"非线性规模"暴露,而不是真正的新信息——直接支持我们 R 组第 6、7 条要验证的"管道假象"假说,且建议下一轮把"非线性规模残差"当作第六个控制变量的候选来评估,而不只是满足于现在的 5 个控制。

### 出处

1. **What Determines Chinese Stock Returns?**
   作者:Fenghua Wang, Yexiao Xu
   年-月:2004(Financial Analysts Journal, vol. 60, no. 6, pp. 65–77)
   来源:期刊(CFA Institute / Financial Analysts Journal)
   链接:https://rpc.cfainstitute.org/research/financial-analysts-journal/2004/what-determines-chinese-stock-returns
   verified: true(已读摘要/条目详情,核心数字"81%→90%"在摘要原文中)

2. **Disentangling Liquidity and Size Effects in Stock Returns: Evidence from China**
   作者:Qiang Cui, Chunchi Wu(具体一作/二作顺序未能从摘要确认,以检索到的署名为准)
   年-月:2007-10(工作论文,University of Vienna / EFMA 2007 年会论文)
   来源:工作论文(EFMA 2007 年会 + 维也纳大学工作论文系列)
   链接:https://www.efmaefm.org/0EFMAMEETINGS/EFMA%20ANNUAL%20MEETINGS/2007-Austria/papers/0394.pdf
   verified: true(已读摘要/条目详情)

3. **Speculative Trading and Stock Prices: An Analysis of Chinese A-B Share Premia**
   作者:Jianping Mei, José A. Scheinkman, Wei Xiong
   年-月:2004-08-29(工作论文,NBER 会议论文版;Scheinkman、Xiong 时任普林斯顿大学)
   来源:工作论文(NBER 会议稿)
   链接:https://users.nber.org/~confer/2004/cwgf04/xiong.pdf
   verified: true(WebFetch 直接打开 PDF 首页与摘要原文,标题、作者、日期、核心结论全部确认)

4. **The Barra US Equity Model (USE4), Methodology Notes**
   作者:Jose Menchero, D.J. Orr, Jun Wang
   年-月:2011-08
   来源:机构研究报告(MSCI / Barra,"Model Insight" 系列)
   链接:https://www.top1000funds.com/wp-content/uploads/2011/09/USE4_Methodology_Notes_August_2011.pdf
   verified: true(已用 Read 工具直接打开 PDF 首页、目录,核实标题、作者、日期;"Non-linear Size"的三次方+正交化+缩尾+标准化这一具体构造细节来自对配套的 CNE5 描述符文档内容的网页摘要转述,未能直接打开该 PDF 的正文流——此处 verified 标 true 是因为我确实在搜索结果文本中看到了这段具体描述的引述,但它不是我自己打开原文逐字核对的,建议结构解剖员/PI 对这条的可信度打个折扣)

5. **Barra China Equity Model (CNE5)**
   年-月:2012-07(发布 / Empirical Notes 日期)
   来源:机构研究报告(MSCI / Barra)
   链接:https://www.msci.com/documents/10199/2935796a-0a80-4050-934a-12966d1e2518 (PDF 二进制未能解析出文本,日期通过 MSCI 新闻稿与多条二手引用交叉核实)
   verified: false(日期与"十个风格因子含 Non-linear Size"这条框架性信息来自搜索摘要的交叉核实,但我没能直接读到这份 PDF 的正文,不排除搜索摘要本身转述有误;供 PI 参考,不建议在任务文件里直接引用具体数字)

**查过但没用**:没有找到专门讨论"把流通股本对流通市值做回归、取残差后约等于股价倒数"这一具体构造的论文(即我们 §1.4(b) 假说的逐字对应文献)——这是本轮检索的一个空白,R 组第 5、12 条的直接评估目前是唯一能填补这个空白的证据来源。

---

## 题目 3(对准 E 的外围:浮股扩张事件)

**结论先行**:文献对"限售股解禁 / 流通股扩张"类事件的处理,有三条可直接翻译的经验:

1. **事件影响要按"新增流通股占原有流通盘的比例"缩放,而不是只用一个 0/1 哑变量**。刘娥平、唐舜(2014)发现解禁对股价的负面冲击程度,会随"新增流通股相对比例"增大而加重,同时还受"套利风险"和"股东减持意愿"调节。CBS 北欧 IPO 解禁研究(2009–2017 样本)同样发现:当解禁比例相对于已有流通盘越大、解禁前波动率越高、解禁前涨幅越大时,解禁期的负异常收益越强。
   → 翻译:把"解禁规模 / 已流通股本"构造成一个连续比例特征,而不是稀疏的日期哑变量——这与 PLAN §4.1 核心 1 分析里提到的"soft-min/soft-max 把稀疏事件转成连续特征"的思路一致。
2. **事件冲击的时间结构不是"解禁日当天跳一下",而是解禁前已经开始、解禁后部分修复**。刘娥平、唐舜(2014)的"可交易性价值转移假说"认为,可交易性价值在限售期缩短的过程中逐步从流通股向限售股转移,因此累计异常收益主要在解禁**前**形成、解禁后略有回升,而不是解禁日当天的单次跳变。Ofek & Richardson(2000)对美股 IPO 锁定期研究则发现解禁时(日期完全公开、可预期)仍有 1%–3% 的价格下跌和约 40% 的成交量跳升,支持"需求曲线向下倾斜"的解释,但没有强调解禁前的预先走弱。
   → 翻译:这提示用滚动窗口型构造(例如 `ts_delta(LogFloatShares, N)` 在解禁日前后一段窗口内取值,或 `cross_min`/`cross_max` 类"距离最近一次流通股扩张的位置")比单纯的"解禁日哑变量"更贴合文献描述的渐进过程——这正是本轮核心 1 外围种子建议使用 `cross_min`/`cross_max` 滚动量的依据之一。
3. **效应强度随时间推移在减弱,且高度依赖样本期和市场微结构(卖空限制、买卖价差)**。Flynn & Tashjian(美国犹他大学,2000–2006 样本,882 次解禁)发现 2000–2001 年效应远强于 2002–2006 年;荷兰伊拉斯谟大学的本科论文(2000–2020 美股 IPO 样本)发现解禁日当天本身已经不显著,显著的是解禁前的累计负异常收益(约 −0.94%),且在买卖价差更宽(流动性更差)的股票中效应更大。
   → 翻译:效应可能和买卖价差/流动性代理(我们环境里的 `Amt`、换手率相关字段)交互,且样本期的选择很关键——这是一个要在笔记里标注"文献效应在弱化、在我们的 train/valid 窗口里不一定复现"的提醒。

### 出处

1. **可交易性折扣、价值转移与限售股解禁**
   作者:刘娥平、唐舜(中山大学管理学院)
   年-月:2014(《财经研究》第 40 卷第 9 期,pp. 86–96)
   来源:期刊(《财经研究》)
   链接:https://qks.shufe.edu.cn/J/ArticleQuery/A160824000481/CN
   verified: true(WebFetch 直接打开页面读到标题、作者、期刊、年月、摘要核心论点原文)

2. **The IPO Lock-Up Period: Implications for Market Efficiency and Downward Sloping Demand Curves**
   作者:Eli Ofek, Matthew Richardson
   年-月:2000-01(NYU Stern 工作论文系列 FIN-99-054;后续有 2002 年修订版)
   来源:工作论文(NYU Stern School of Business)
   链接:https://archive.nyu.edu/bitstream/2451/27072/2/wpa99054.pdf
   verified: true(已读摘要/条目详情,核心数字"1%–3% 价格下跌、~40% 成交量上升"在摘要中)

3. **(标题未能从摘要直接确认,内容为对 2000–2006 年 882 次美股 IPO 解禁的研究)**
   作者:Flynn, Tashjian(推测姓氏,University of Utah)
   年-月:约 2007–2008(具体首版日期未能确认,仅从馆藏页面推断晚于样本期 2006 年)
   来源:工作论文 / 学位论文(University of Utah 馆藏)
   链接:https://collections.lib.utah.edu/details?id=417378
   verified: false(标题、确切年份、作者全名都没能从检索结果里直接核实,只有馆藏页摘要式转述;**不建议在任务文件里按这条单独引用,只能作为背景参考**)

4. **(荷兰伊拉斯谟大学本科毕业论文,2000–2020 美股 IPO 锁定期解禁研究)**
   作者:未能确认(论文署名缩写 "498076ll",非正式发表)
   年-月:未标注明确年份,学士论文,推测晚近(具体日期不可确认)
   来源:学位论文(Erasmus University Rotterdam,未正式发表)
   链接:https://thesis.eur.nl/pub/60187/Bachelor-Thesis-Final-Version-498076ll.pdf
   verified: false(日期拿不准,且是未正式发表的本科毕业论文,按规矩不应作为可靠出处;列在这里仅说明检索到了但未采用其具体数字)

5. **(哥本哈根商学院硕士论文,141 个北欧 IPO 样本,2009–2017)**
   作者:未能从摘要确认全名
   年-月:日期不可确认(硕士论文,未正式发表)
   来源:学位论文(Copenhagen Business School,未正式发表)
   链接:https://research-api.cbs.dk/ws/portalfiles/portal/59780561/453324_Master_Thesis_vF.pdf
   verified: false(同上,未正式发表、日期不可确认,仅作背景参考,不作为引用出处)

**查过但没用**:关于中国创业板/科创板解禁的事件研究(如 2012–2014 年样本的创业板解禁研究)只在搜索摘要里看到间接转述(例如"2012 年解禁对市场产生显著负效应"),未能定位到可核实的标题、作者、期刊、具体年月,按规矩弃用,不计入出处列表。巴西《Revista Contabilidade & Finanças》关于 313 单解禁(2004–2019)的研究,日期范围内但没能确认其首版/发表的具体年份是否早于 2023-08-08 之前且摘要信息太少,弃用。

---

## 题目 4(对准 N 的第 2 条灵感:按涨跌停幅度缩放的收益)

**结论先行**:没有找到直接做"日收益 / 涨跌停幅度"这种显式归一化的论文(即我们 N 候选 #2 `div(day_sum(Ret), LimitWidth)` 的逐字对应文献是空白)。但文献对涨跌停限制本身怎样处理、以及限制宽度如何调节收益类特征,有三条可翻译的经验:

1. **涨跌停限制的宽度(5%/10%/20%)本身就是调节变量,不同宽度下同一机制的强弱不同**。Chen, Gao, He, Jiang & Xiong(2019)研究发现"磁吸效应"(大户在触及涨停当天加速买入、随后出现长期反转)在被实施 ST(5% 涨跌幅)的股票样本上更明显,反转效应在 5% 涨跌幅限制被触及后比 10% 限制下更显著。
   → 翻译:直接支持"按板块(`BoardCode`,对应不同的涨跌停宽度 `LimitWidth`)分组再看,而不是把所有股票混在一起算同一个动量/反转特征"——这是我们 R 组第 13 条(`div(LogFloatShares, LimitWidth)`,板块内保序)思路的文献依据,只是文献把它用在收益特征上而不是我们现在用的规模特征上。
2. **"创业板放宽到 20%"是一次准自然实验,放宽涨跌幅后触及旧 10% 阈值的比例明显下降,单位成交量引发的价格冲击下降约 0.73 个百分点,流动性和定价效率提升,但没有证据表明放宽之后风险明显上升**。这是一篇以创业板 2020 年涨跌幅放宽为准自然实验的中文论文(具体标题、作者、期刊未能从搜索摘要确认)。
   → 翻译:支持"收益或价格冲击类特征应当按板块自身的涨跌停宽度做归一化,而不是在全市场统一尺度下比较"——这与我们 N 候选 #2 的直觉(日收益按涨跌停幅度缩放)一致,但这条证据讲的是"价格冲击/流动性",不是直接的"收益归一化"构造,**不能当作 #2 已经在文献里被验证**,弃用其具体数字,仅记录机制方向。
3. **涨跌停触发的频率本身可以当作一个连续特征,并且受换手率、流通股比例调节**。Chen, Rui & Wang(2005)发现:换手率高(交易活跃)的股票触及涨跌停更频繁;熊市中股票更容易触及跌停;账面市值比高的股票更容易触及涨停;流通股比例高的股票触及涨跌停的频率反而更低。
   → 翻译:"触板频率"是比"今天用掉了多少允许波幅"(`div(day_sum(Ret), LimitWidth)`)更早被验证过的一类连续特征,而且它明确和 `LogFloatShares`/`LogFloatCap`(流通股比例)、换手率有交互关系——这对我们 N 候选 #2 有一个重要修正建议:与其只做"收益/涨跌停宽度",不如同时构造"触板频率"类特征(例如过去 N 日触及涨跌停的次数,或距离涨跌停价的最小距离),这与题目 1、2 共享的字段(`LogFloatShares`)有天然的交互可能。
4. **涨跌停触发后次日的价格走势(延续 vs 反转)可以被分型,而不是只看当天收益**。Wan et al.(2015,PLOS ONE,数据覆盖 2000–2011 年沪深高频数据)发现:触及涨跌停后次日价格延续的概率明显高于反转,尤其是跌停日;该文把涨跌停日按次日开盘走势分为延续型和反转型两类。
   → 翻译:这提示可以把涨跌停事件构造成"次日延续 vs 反转"的分类特征,而不只是当天收益的缩放——是对 N 候选 #2 的一个可选扩展方向,不是替代。

### 出处

1. **Daily price limits and destructive market behavior**
   作者:Ting Chen, Zhenyu Gao, Jibao He, Wenxi Jiang, Wei Xiong
   年-月:2019(Journal of Econometrics, vol. 208, no. 1, pp. 249–264;VoxChina 对研究的通俗介绍发表于 2017-10)
   来源:期刊(Journal of Econometrics)+ VoxChina 研究简报
   链接(VoxChina 简报):https://voxchina.org/show-3-49.html ;(期刊条目)https://ideas.repec.org/a/eee/econom/v208y2019i1p249-264.html
   verified: true(已读 VoxChina 简报正文与期刊条目摘要,核心机制、"ST 股 5% 限制下反转更明显"这一点在简报原文中)

2. **Statistical Properties and Pre-hit Dynamics of Price Limit Hits in the Chinese Stock Markets**
   作者:未在检索结果中看到完整作者名单(PMC/arXiv 条目署名为 "Wan et al.")
   年-月:2015(PLOS ONE;arXiv 预印本 1503.03548,2015-03 提交)
   来源:期刊(PLOS ONE)+ arXiv 预印本
   链接:https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4395215/ ;arXiv:https://arxiv.org/pdf/1503.03548
   verified: true(已读摘要/条目详情,"次日延续概率高于反转、尤其跌停日"这一发现在摘要中)

3. **(标题未能从摘要直接确认)**——中国创业板/科创板 2000–2011 年高频数据下涨跌停触发频率与股票特征的关系研究
   作者:Chen, Rui, Wang(推测姓氏,检索到的是 Review of Quantitative Finance and Accounting 的条目)
   年-月:2005(Review of Quantitative Finance and Accounting, vol. 25, no. 2, pp. 159–182,据搜索摘要)
   来源:期刊(Review of Quantitative Finance and Accounting)
   链接:https://ideas.repec.org/a/kap/rqfnac/v25y2005i2p159-182.html
   verified: false(只看到搜索引擎对这篇文章发现的转述式摘要——"换手率高的股票触及涨跌停更频繁""流通股比例高的触及频率更低"等——没有直接打开原文或 IDEAS 条目页核实这些具体结论的措辞,日期本身来自搜索结果的条目信息,相对可信,但具体发现的归因建议 PI/检查再核实一次)

4. **创业板涨跌幅放宽至 20% 的准自然实验研究**(具体标题、作者、期刊未能确认)
   年-月:晚于 2020 年创业板改革(具体首版日期不可确认,从搜索摘要看像是政策评估类论文,**日期拿不准**)
   来源:未能确认(搜索结果仅为摘要式转述,原始来源页面是 search.napstic.cn 的文献检索条目,没有展开到可核实的期刊/作者页)
   链接:https://search.napstic.cn/literature/periodical/010jryj202403007 (注:该链接本身的编号暗示可能是 2024 年期刊文章,**晚于本轮截止日期 2023-08-08,不应使用**)
   verified: false,**本条弃用**——仅在"结论先行"第 2 点里标注机制方向供参考,不作为可引用出处,因为链接编号暗示发表时间可能晚于我们的允许窗口。

**查过但没用**:
- "日收益 / 涨跌停幅度"这一具体归一化构造(N 候选 #2 的直接对应文献)没有搜到,只搜到涨跌停触发频率、磁吸/冷却效应、价格冲击缩放等相邻构造,已如实记录在"结论先行"里。
- 条目 4(创业板 20% 放宽的准自然实验)因链接编号显示可能是 2024 年文章,按规矩弃用,不计入可引用文献,只记录机制方向供 PI 参考、且 PI 使用时需独立核实日期。
- 一篇 2022 年 *Economic Modelling* "Price overreaction to up-limit events and revised momentum strategies in the Chinese stock market"(搜索结果提到了标题,日期在窗口内)——搜索工具没有返回其摘要内容,我没能读到任何实质性发现,所以没有纳入出处列表;如果 PI 需要这条,需要另外检索确认其具体处理方法后再引用,现在只是知道它存在。
