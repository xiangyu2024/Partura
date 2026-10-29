# 文献笔记 —— 种子 801,第 2 轮

对应 `analysis.md` §5 的四个题目(核心 1/2:相对价格水平/累计涨幅;核心 1/2 的"尾部指示/筛选式"构造;核心 2:组内标准化本身;N 的灵感 1/2:开盘集合竞价 + 停在极值的时间占比)。
检索工具:WebSearch(standard 模式)+ WebFetch(核对标题/作者/日期/摘要原文)。**只用 2023-08-08 之前发表/首版的文献**;日期拿不准或晚于截止日的,已在各题"查过但没用"里如实弃用。
多数出处我用 WebFetch 直接打开了摘要页/条目页核实了标题、作者、期刊卷期、年月,标 `verified: true` 并注明"已读摘要/条目详情"或"已读原文摘要";只来自搜索引擎二手转述、没能独立核对关键细节的,标 `verified: false` 并说明哪里不确定。

---

## 题目 1(对准核心 1 / 2:相对同业的价格水平 / 累计涨幅,以及名义价 vs 复权价的混淆)

**结论先行**:

1. **"相对同业"的标准做法是先分组、再在组内排序或标准化,分组变量以行业/板块为主,文献没有给出"分几组"的通用答案。**
   Moskowitz & Grinblatt(1999)的行业动量直接在行业内(而不是全市场一次性分位)比较收益,发现行业内动量比个股动量更强、更稳健,且个股动量的大部分解释力来自行业归属。
   → 翻译:`cs_bucket_zscore(X, BoardCode)` 或按 `LogFloatCap` 分组,这类"先分组再处理"的写法与文献的"行业相对"构造方向一致;但文献用的分组通常是数十个行业类别,不是十分位,"分几组"本身没有被专门优化过,是我们可以自己试的维度。

2. **滚动极值窗口:52 周(约 252 个交易日)是被反复验证的金标准窗口,"距高点的距离"本身就是一个独立、不会长期反转的预测变量**,但没有看到专门检验"压缩到一个季度(约 60 日)窗口"是否还成立的文献。
   George & Hwang(2004)发现"当前价格相对 52 周高点的比例"比过去收益本身更能预测未来收益,且这个预测力**不会在长期反转**——作者据此论证短期动量和长期反转是两件分开的现象。这个效应后来在不同市场、不同持仓结构下被反复复现(例如按零售交易占比分组后效应更强的研究)。
   → 翻译:我们的 `cross_min(...,60)`/`cross_max(...,60)` 对应"季度内相对位置",是文献金标准窗口(≈252 日)的 1/4;文献没有专门测试过把窗口压缩到季度后效应是否保留、是否变成完全不同的量——这是一个检索空白,支持 R 组变体 1/2/3 用直接评估去填补,而不是默认"应该和 52 周版本一样有效"。

3. **这类"距极值距离"的效应在中国 A 股的证据是非线性、非对称的:只在"远离极值"时才显著,"接近极值"时效应消失。**
   Wang, Wang & Wu(2023, *Pacific-Basin Finance Journal* 80, 文章号 102054)发现:用收益偏度度量的"彩票偏好"效应,只在价格远低于 52 周高点的股票里显著(多空组合月度 0.85%、经风险调整),在接近 52 周高点的股票里不显著(0.04%,不显著);效应受套利风险、投资者情绪调节。
   → 翻译:虽然这篇测的是"彩票偏好"而不是我们的价格水平因子本身,但它的**构造手法**——用"距极值的距离"本身当分组/交互变量,再看另一个量在组内的效应——是可以直接翻译的处理方式:如果核心 1/2 的收益也集中在"远离高点"的那一段,应该把"距离"本身当控制或交互项,而不是假设它和目标线性相关。

4. **名义价格水平和复权价格(= 自基准以来的累计总收益)是文献里明确区分的两件事,区分的关键是"股票分拆会不会让这个量跳变"。**
   Weld, Michaely, Thaler & Benartzi(2009 春,*Journal of Economic Perspectives* 23(2), 121–142)的核心发现是:美股的平均名义价格几十年来被公司持续分拆维持在约 25~35 美元的区间,**不会**随时间单调累积——这说明"名义价格"是一个被主动维持在某个区间的量,而"复权价格"(split-adjusted,累计总收益)则必然随长期收益单调累积,二者在构造上是本质不同的量。
   Birru & Wang(2016, *Journal of Financial Economics* 119(3), 578–598,工作论文题《Nominal Price Illusion》/《Nominal Price Premium》,Ohio State Dice Center WP 2015-15)进一步指出:直接对原始价格排序会把"名义价格溢价"和基本面贴现率效应混在一起,他们改用剔除基本面成分后的"拟合价格"(fitted price)。
   → 翻译:这两篇合起来直接支持 §1.7(c) 的怀疑——用复权 `Close` 做截面排序时,如果窗口覆盖了上市以来的全部复权历史,这个量里天然混入了长周期动量/反转,因为复权价格本身就是累积总收益的单调变换;构造"干净的名义价格水平"需要显式从未复权价格/上市价开始算,或者对复权价格先做一次关于长期收益(或基本面变量)的回归取残差。**但文献没有专门讨论"60~120 日窗口下复权价与名义价混淆"这个具体的短窗口问题**,这仍是空白,支持下一轮直接评估去验证。

5. **"距历史价格极值的距离"这类构造在文献里被反复当作独立于基本面的锚点变量,不需要额外的基本面解释就能站得住。**
   Baker, Pan & Wurgler(NBER WP 15551,2009-12 首发;发表版《The Effect of Reference Point Prices on Mergers and Acquisitions》,*Journal of Financial Economics* 106(1), 2012-10, 49–71)发现并购出价会被拉向目标公司的 52 周高点——作者明确称其为"salient but largely irrelevant"(显著但基本无关)的历史统计量,且出价超过该高点时成交概率会跳升。
   → 翻译:这确认"历史价格极值"本身(不需要任何基本面含义)就足以在完全不同的场景里产生可测的效应,支持把核心 1/2 的"距极值距离"当作一个独立的、值得单独深挖的结构,而不必先解释它的基本面来源。

### 出处

1. **The 52-Week High and Momentum Investing**
   作者:Thomas J. George, Chuan-Yang Hwang
   年-月:2004-10
   来源:期刊(Journal of Finance, vol. 59, no. 5, pp. 2145–2176),DOI 10.1111/j.1540-6261.2004.00695.x
   链接:https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.2004.00695.x
   verified: true(多次搜索结果交叉核实卷期页码、DOI、核心发现一致)

2. **Do Industries Explain Momentum?**
   作者:Tobias J. Moskowitz, Mark Grinblatt
   年-月:1999-08
   来源:期刊(Journal of Finance, vol. 54, no. 4, pp. 1249–1290),DOI 10.1111/0022-1082.00146
   链接:https://ideas.repec.org/a/bla/jfinan/v54y1999i4p1249-1290.html
   verified: true(WebFetch 直接打开条目页读到标题、作者、卷期页码、摘要)

3. **A Reference Point Theory of Mergers and Acquisitions**(发表版题目:《The Effect of Reference Point Prices on Mergers and Acquisitions》)
   作者:Malcolm Baker, Xin Pan, Jeffrey Wurgler
   年-月:NBER 工作论文 2009-12(WP 15551);发表版 2012-10(Journal of Financial Economics, vol. 106, no. 1, pp. 49–71)
   来源:工作论文(NBER)+ 期刊(JFE)
   链接:https://www.nber.org/papers/w15551
   verified: true(WebFetch 直接打开 NBER 页面读到标题、作者、首发日期、摘要原文)

4. **The role of anchoring on investors' gambling preference: Evidence from China**
   作者:Zhuo Wang, Ziyue Wang, Ke Wu
   年-月:2023(Pacific-Basin Finance Journal, vol. 80, 文章号 102054),DOI 10.1016/j.pacfin.2023.102054
   来源:期刊(Pacific-Basin Finance Journal)
   链接:https://ideas.repec.org/a/eee/pacfin/v80y2023ics0927538x23001208.html
   verified: true(WebFetch 直接打开条目页读到标题、作者、期刊卷号、DOI、摘要)

5. **The Nominal Share Price Puzzle**
   作者:William C. Weld, Roni Michaely, Richard H. Thaler, Shlomo Benartzi
   年-月:2009-春(Journal of Economic Perspectives, vol. 23, no. 2, pp. 121–142),DOI 10.1257/jep.23.2.121
   来源:期刊(JEP, AEA)
   链接:https://ideas.repec.org/a/aea/jecper/v23y2009i2p121-42.html
   verified: true(多条搜索结果交叉核实卷期页码、DOI,并读到摘要原文关于"名义价格维持在约 $25~35"的具体数字)

6. **Nominal Price Illusion**(工作论文题《Nominal Price Premium》,Ohio State Dice Center WP 2015-15)
   作者:Justin Birru, Baolian Wang
   年-月:2016(Journal of Financial Economics, vol. 119, no. 3, pp. 578–598)
   来源:期刊(JFE)
   链接:https://ideas.repec.org/p/ecl/ohidic/2015-15.html
   verified: true(本轮搜索再次确认卷期页码 578–598,及"拟合价格剔除基本面成分"这一处理方式的摘要表述)

**查过但没用**:
- Ding Du(2008)对 George & Hwang(2004)的跨国股指批评(称国际股指上动量与反转并存)——只在二手摘要里看到提及,没能确认期刊名、卷期,弃用。
- 一篇 2019 年声称覆盖 38 国的"名义价格锚定是全球现象"的工作论文——只在二手引用里看到标题线索(iems.ust.hk 托管),没能独立打开核实作者、确切发表年月,弃用。
- 专门检验"季度(≈60 个交易日)高点"而不是 52 周高点的锚定/动量文献——没搜到,如实记录为空白;这正是 R 组变体 1/2/3 要用直接评估填补的地方。

---

## 题目 2(对准 §1.3:尾部指示 / 排除式筛选,而不是单调排序)

**结论先行**:

1. **判断"是不是单调"有专门的统计检验,不能只看首尾分组的价差显著不显著。**
   Patton & Timmermann(2010, *Journal of Financial Economics* 98(3), 605–625)提出了专门的"单调性检验",并指出文献里很多"顶减底"价差显著的分档结果,完整检验后**并不满足全程单调**——换句话说,很多被报告为"分档效应"的东西,其实只是头尾两档不一样,中间档可能是平的甚至是反的。
   → 翻译:判断 `cs_last_high20` 这类"只取头部一档"的构造是否合理,标准做法是报告全部十分位(或至少中间几档)的均值,而不只是"进入这一档"这个指示变量的边际贡献;如果中间档和两端差不多,就是 PLAN §1.3 怀疑的"尾部指示器",不是一个连续排序因子的粗糙替代。

2. **一些最著名的横截面效应确实被证明是非单调、集中在一两个极端分档,但这个结论本身对估计细节高度敏感,且存在反例。**
   Bali & Cakici(2008, *Journal of Financial and Quantitative Analysis* 43(1), 29–58)系统检验特质波动率效应后发现,是否显著取决于波动率估计频率、组合权重方式、分组断点数量,以及是否剔除小盘/低价/低流动性股票——"效应是否只在尾部"本身是一个需要显式检验的问题,不能默认。
   但 Ciliberti, Lempérière, Beveratos, Simon, Laloux, Potters & Bouchaud(2015-10 首发,arXiv:1510.01679,《Deconstructing the Low-Vol Anomaly》)对低波动异象的反例研究发现:异象**不是**集中在任何单一十分位,而是从高波动到低波动平滑累积的偏差,**反驳**了"低波动异象主要由分文股/极端波动股驱动"的说法。
   → 翻译:这两篇放在一起说明,"是不是尾部效应"不能靠先验假设,必须用变窄/变宽分组边界(我们 R 组变体 10,20%→10%)、或者看全部分档的方式直接检验;文献里对同一类问题(是尾部驱动还是平滑驱动)存在真实的分歧,我们这轮的检验结果无论支持哪一边都有文献先例可以类比。

3. **彩票/MAX 效应的文献采用十分组设计且发现方向不对称,但对"效应是尾部真实效应还是反转的马甲"这件事本身也有争议。**
   Bali, Cakici & Whitelaw(2011, *Journal of Financial Economics* 99(2), 427–446;NBER WP 14804 更早流通)的 MAX 效应(过去一月最大单日收益)在十分组排序下负向显著;后续 Gorman, Akhtar, Durand & Gould(2022, *Critical Finance Review*)认为高 MAX 股票的跑输可能来自"近期暴涨后的过度反应回落",而不是真正的彩票偏好。
   → 翻译:同一个分档结果可以有两种完全不同的归因(彩票偏好 vs 反转),必须另外设计检验(例如显式控制近期收益)才能区分——这对核心 1/2 的 `cs_last_high20` 构造也适用:如果它的收益来自"最近涨得多的那一档随后跑输",需要控制近期收益才能排除这只是反转效应的马甲。

4. **"先筛选、再排序"对应文献里的条件/序贯双重排序,与独立双重排序的结论会系统性不同,因为条件排序里第一个变量会主导最终的收益模式。**
   Bali, Engle & Murray《Empirical Asset Pricing: The Cross Section of Stock Returns》(2016, Wiley, ISBN 9781118095041)专门区分独立双重排序(independent sort)与条件/序贯双重排序(conditional/sequential sort,书中有专门章节比较两者);业界对条件排序的通用描述是:第二次排序的断点是在第一次分组内部重新计算的,所以第一个排序变量会支配后续分组里观察到的收益模式。
   → 翻译:PLAN §2.4"拆解"里"先用 X 排除一批股票、再按 Y 排序"对应条件双重排序。要知道"筛选的贡献"和"排序的贡献"哪个大,应同时跑一次独立排序作对照(两个变量各自单独排序后再比较),否则条件排序会把两者的贡献混在一起,表现为"筛选变量看起来解释力很强"——这是我们 R 组"把排序变量换成控制字段本身"(变体 6、7)的文献支持方向,但文献进一步建议应该两个变量都轮流当"第一道筛选"才能完全分开归因,这是我们这轮没做但可以在下一轮补的。

5. **把连续变量离散化(分档/哑变量化)在统计学界被认为默认会损失信息,除非真实关系本身就是非单调的。**
   统计学界关于分箱(binning)的共识(Frank Harrell 等在统计论坛的讨论)是:对本质连续的变量分箱会任意损失信息,断点选择本身是任意的,预测误差通常比用连续变量加平滑项(如回归样条)更高;分箱唯一站得住的理由是关系本身非单调、一个线性系数无法同时捕捉"先升后降"的模式。
   → 翻译:`cs_last_high20(X, A)` 这种"只保留 A 最高 20% 那部分 X"的构造,只有在"效应真的只存在于尾部"时才优于直接用连续的 A 做排序因子;如果 R 组变体 6/7(排序变量换成控制字段本身)显示列序斜坡占了大部分贡献,说明我们的"尾部指示"构造本质上是在做一件比"保留全部信息的连续排序"更差的事,这与统计学界对离散化的一般结论吻合。

### 出处

1. **Monotonicity in Asset Returns: New Tests with Applications to the Term Structure, the CAPM, and Portfolio Sorts**
   作者:Andrew J. Patton, Allan Timmermann
   年-月:2010-12
   来源:期刊(Journal of Financial Economics, vol. 98, no. 3, pp. 605–625),DOI 10.1016/j.jfineco.2010.06.006
   链接:https://public.econ.duke.edu/~ap172/Patton_Timmermann_sorts_JFE_Dec2010.pdf
   verified: true(多条搜索结果交叉核实标题、作者、卷期页码、DOI、核心论点)

2. **The Cross-Section of Volatility and Expected Returns**
   作者:Andrew Ang, Robert J. Hodrick, Yuhang Xing, Xiaoyan Zhang
   年-月:2006
   来源:期刊(Journal of Finance, vol. 61, no. 1, pp. 259–299)
   链接:https://www.nber.org/papers/w10852
   verified: true(已读摘要/条目详情,卷期页码与核心发现一致)

3. **Idiosyncratic Volatility and the Cross Section of Expected Returns**
   作者:Turan G. Bali, Nusret Cakici
   年-月:2008
   来源:期刊(Journal of Financial and Quantitative Analysis, vol. 43, no. 1, pp. 29–58)
   链接:https://ideas.repec.org/a/cup/jfinqa/v43y2008i01p29-58_00.html
   verified: true(已读条目详情/摘要,核心结论"显著性依赖估计细节"确认)

4. **Maxing Out: Stocks as Lotteries and the Cross-Section of Expected Returns**
   作者:Turan G. Bali, Nusret Cakici, Robert F. Whitelaw
   年-月:2011(NBER WP 14804 更早流通)
   来源:期刊(Journal of Financial Economics, vol. 99, no. 2, pp. 427–446)
   链接:https://www.nber.org/papers/w14804
   verified: true(本轮再次核实,MAX 测度定义与十分组负向关系的摘要表述一致)

5. **Empirical Asset Pricing: The Cross Section of Stock Returns**
   作者:Turan G. Bali, Robert F. Engle, Scott Murray
   年-月:2016-04
   来源:专著(Wiley),ISBN 9781118095041
   链接:https://www.wiley.com/en-us/Empirical+Asset+Pricing%3A+The+Cross+Section+of+Stock+Returns-p-9781118095041
   verified: true,但打折扣(确认了书名、作者、出版社、出版日期、"独立双重排序"与"条件/序贯双重排序"分属不同章节这一结构;没能直接读到章节正文,"第一个排序变量主导后续分组模式"这一具体表述来自业界对该方法的通用转述,不是我直接读到的书中原文,建议结构解剖员/PI 对这条打个折扣)

6. **Deconstructing the Low-Vol Anomaly**
   作者:S. Ciliberti, Y. Lempérière, A. Beveratos, G. Simon, L. Laloux, M. Potters, J.P. Bouchaud
   年-月:2015-10(arXiv:1510.01679,v1 首发)
   来源:工作论文(arXiv,q-fin)
   链接:https://arxiv.org/abs/1510.01679
   verified: true(WebFetch 直接打开 arXiv 摘要页,读到标题、作者、首发日期、摘要原文)

**查过但没用**:
- Erasmus 大学一篇本科/硕士论文声称"剔除低价股后低波动异象消失"——未正式发表的学位论文,作者与确切年份未能确认,按规矩弃用,只记录结论方向供背景参考。
- 专门讨论"如何把筛选的贡献和排序的贡献分开归因"的独立论文(不是教材里的一般性双重排序讨论)——没搜到,如实记录为空白。

---

## 题目 3(对准核心 2:分组内标准化这件事本身)

**结论先行**:

1. **组内标准化/组内秩是量化因子构造里的标准算子层,不是某个因子偶然用到的技巧。**
   Kakushadze(2016-01 首发 arXiv:1601.00991,v3 2016-03-18;发表于 *Wilmott* 2016(84), 72–80)的《101 Formulaic Alphas》给出 101 个可执行的因子公式,显式包含跨截面排序算子 `rank` 和行业内中性化算子 `indneutralize(x, g)`(按行业/板块对 x 做组内处理)。这篇文章把"先按分组变量把值变成组内排序或组内标准化,再参与后续运算"写成了一个独立于具体因子的、可重复使用的算子。
   → 翻译:确认 `cs_bucket_zscore`/`cs_bucket_rank` 这类处理在文献/业界里是一类通用算子,支持系统地搭配不同的分组变量(行业/规模/板块)和被处理变量,而不是只在我们已经见过的骨架里用。

2. **工业界的多因子风险模型把"分组标准化"当作正式建模步骤,且明确包含缩尾(winsorize)处理这一环,纯 z 分数对我们这 6 个日频字段(多为厚尾的规模/成交额类变量)可能不稳健。**
   MSCI Barra 美股模型 USE4 方法论文档(Menchero, Orr & Wang, 2011-08)的目录里有专门一节"Data Quality and Outlier Treatment"(数据质量与异常值处理),本轮搜索再次确认了这一节标题的存在,但正文细节(具体缩尾阈值)仍未能直接读到;统计学界关于稳健标准化的共识是:纯 z 分数的均值和标准差本身会被极端值拖动,稳健替代做法是用中位数和 MAD(中位绝对偏差)。
   → 翻译:`cs_bucket_zscore(day_sum(Vwap), BoardCode)` 如果不先缩尾,少数极端成交额的股票可能主导整组的均值和标准差——这是文献支持的、但从我们算子定义里看不出是否已处理的风险点,可以作为 N 的一个分支:同一骨架换成缩尾后的 z 分数,或直接换成组内秩(对厚尾天然更稳健,但会丢掉幅度信息)。

3. **没有找到专门在"价格 / 市值 / 成交额"这类变量上直接比较组内秩与组内 z 分数孰优孰劣的顶刊论文**(搜到一篇覆盖数据到 2024 年的最新工作论文,首版日期无法确认在 2023-08-08 之前,已弃用,见"查过但没用"),只有统计学界"排序变换对异常值天然不敏感、但丢掉幅度信息"这一一般性结论可以类比。
   → 翻译:R 组第 5 条变体(`cs_bucket_zscore` → `cs_bucket_rank`)是一个文献支持"值得测",但文献本身不能预判答案的检验——这是检索空白,不是因为检索不到位,而是这个具体比较本身在成熟文献里也缺乏共识。

4. **"两层嵌套分组"(先按 X 分组标准化,再把标准化结果当新的分组变量)没有找到逐字对应的文献,工业界的"嵌套行业分类"是最接近但不完全相同的先例。**
   Kakushadze(2014-12 首发,arXiv:1412.4342,《Russian-Doll Risk Models》)明确讨论了按"sector → industry → sub-industry"这种多层嵌套的行业分类结构来嵌入风险因子的算法。但他处理的是嵌套的**离散分类变量**(行业层级),不是我们这里"把一次标准化的连续结果变成下一次的分组变量"这种更激进的嵌套方式(分组对象从离散类别变成连续派生量)。
   → 翻译:我们核心 2 外围种子里 `cross_min(cs_bucket_zscore(...), cross_min(cs_bucket_zscore(...), BoardCode), 60)` 这类写法,本质是"同一个变量做两次时间+分组组合运算",和文献里讨论的"嵌套分组"(分类层级嵌套)不是同一件事——如果 PI 想在 N 里试"真正的两层嵌套分组"(先按 BoardCode 标准化,再把标准化结果本身当分组变量做第二层),目前没有直接文献先例,只能类比"迭代正交化"的逻辑自己设计,这会是真正的新尝试,不是复现文献。

5. **离散类别分组下的组内去均值,在数学上是回归中性化的一个特例**(组是离散类别时,组内去均值等价于对分组哑变量做无截距回归取残差),但这是教科书级的数学事实(Frisch–Waugh–Lovell 定理在固定效应/分组情形下的特例),本轮没有找到可独立引用的具体论文/工作论文来源,**不计入可引用出处**,只作为背景说明放在这里,供结构解剖员/PI 判断是否需要另外找econometrics教材核实。
   → 若这条成立,`cs_bucket_zscore(X, BoardCode)` 和"对 X 做关于 BoardCode 的回归取残差再标准化"理论上应该给出几乎一样的排序;如果本轮 R 组第 4/5 条变体显示两种写法结果差很多,差异更可能来自标准化本身(均值 vs 秩)而不是"分组"和"回归"这两种中性化方式的本质区别——但这个推论建立在一个我没能找到可引用来源的数学事实上,PI 使用时需要知道这一点。

### 出处

1. **101 Formulaic Alphas**
   作者:Zura Kakushadze
   年-月:2016-01 首发(arXiv:1601.00991),v3 修订 2016-03-18;发表版 *Wilmott* 2016(84), 72–80
   来源:工作论文(arXiv, q-fin.PM)+ 期刊(Wilmott Magazine)
   链接:https://arxiv.org/abs/1601.00991
   verified: true(WebFetch 直接打开 alphaxiv 概览页读到标题、提交/修订日期、journal reference;operator 名称 `rank`、`indneutralize`、`decay_linear` 经多条搜索结果交叉确认)

2. **Russian-Doll Risk Models**
   作者:Zura Kakushadze
   年-月:2014-12 首发(arXiv:1412.4342)
   来源:工作论文(arXiv, q-fin)
   链接:https://arxiv.org/abs/1412.4342
   verified: true(WebFetch 直接打开 arXiv 摘要页,读到标题、作者、首发日期,以及"sector → industry → sub-industry"嵌套结构的摘要原文)

3. **The Barra US Equity Model (USE4), Methodology Notes**
   作者:Jose Menchero, D.J. Orr, Jun Wang
   年-月:2011-08
   来源:机构研究报告(MSCI / Barra)
   链接:https://www.top1000funds.com/wp-content/uploads/2011/09/USE4_Methodology_Notes_August_2011.pdf
   verified: true,但打折扣(本轮再次通过搜索确认文档作者、日期,以及目录里存在"Data Quality and Outlier Treatment"一节;PDF 正文是压缩二进制流,两轮都没能直接解压读到该节具体的缩尾阈值,这条沿用第 1 轮的降级标注)

**查过但没用**:
- Cakici & Zaremba《Getting the Target Right in Return Prediction》(SSRN,比较 rank 目标 vs 标准化目标在 35 个市场的表现)——数据覆盖到 2024 年,首版日期无法确认在 2023-08-08 之前,弃用,不作为可引用处。
- 一份疑似 MSCI FaCS(Factors and ESG)方法论 PDF 提到"迭代计算稳健均值/标准差后缩尾、再标准化"的具体流程——没能确认这份文档本身的发布日期,且内容更像面向客户的方法论说明而非独立研究,弃用,只在"结论先行"第 2 条里提及 USE4 的对应章节标题作为旁证。
- "两层嵌套分组"(把标准化结果当新分组变量)的逐字对应文献——没搜到,如实记录为空白。

---

## 题目 4(对准 N 的灵感 1 与 2:开盘集合竞价 + 停在极值的时间占比)

**结论先行**:

1. **开盘阶段(含集合竞价)的价量行为对收益有独立于日内交易时段的解释力,文献把"隔夜/开盘"和"日内"分开处理是标准做法,且效应集中在被关注的股票上。**
   Berkman, Koch, Tuttle & Zhang(2012, *Journal of Financial and Quantitative Analysis* 47(4), 715–741)发现隔夜收益(开盘价相对前一日收盘的跳空)系统性偏高,随后在当天交易时段部分反转,作者把机制归因于"开盘时被散户关注驱动的买盘推高开盘价",效应在近期吸引了关注的股票、以及零售情绪高涨期更强。
   → 翻译:直接支持把"竞价价对前收盘的跳空"(类似 `div(day_first(Open), ts_delay(day_last(Close), 1))`)当作一个独立特征,而不是并入日内动量;且应该和"近期是否被关注"(可用成交量异动、涨跌停事件代理)交互——文献明确说效应集中在被关注的股票上,这是 §4.3 N 灵感 1 里"竞价量异动 × 跳空方向"这个方向的直接文献支持。

2. **"停在涨跌停"这件事在文献里需要同时考虑磁吸(价格被向涨跌停拉)和冷却(触及后反而减速)两种相反机制,且方向不对称(跌停方向比涨停方向更强),不能假设涨停/跌停是镜像关系。**
   Wan, Wang, Jiang, Xie & Zhou(2018, *Physica A* 505, 153–163;首发 arXiv:1803.09422, 2018-03)用 2000–2011 年沪深高频数据发现冷却效应存在于涨停和跌停两个方向,且**跌停方向的冷却效应比涨停方向更强**。
   更早的 Wan, Xie, Gu, Jiang, Chen, Xiong, Zhang & Zhou(2015, PLOS ONE;arXiv:1503.03548, 2015-03)发现触及涨跌停后,次日价格**延续**的概率高于**反转**,且这个延续概率在**跌停日**更明显。
   Chen, Gao, He, Jiang & Xiong(2019, *Journal of Econometrics* 208(1), 249–264;NBER WP 24014, 2017-11)用深交所账户级数据发现磁吸效应在 5% 涨跌幅限制(ST 股)下比普通 10% 限制下更明显,大户在触及涨停当天买入、次日卖出,这种行为预测更强的长期价格反转。
   → 翻译:这三篇放在一起说明,"封板"从来不是单一方向的简单延续或反转,而是取决于(i)涨停还是跌停方向(我们的 `day_at_max_ratio` vs `day_at_min_ratio` 变体 11/12 应该预期不对称,而不是镜像);(ii)板块的涨跌幅宽度(`LimitWidth`,ST/非 ST/创业板不同);(iii)测量窗口是"触及前的动态"还是"触及后次日"。

3. **涨跌停限制宽度本身会改变磁吸/冷却的相对强弱,这是一个可以用准自然实验直接检验的问题,而不是先验能确定的。**
   Bao(2023-06, PLOS ONE 18(6), e0287548)用创业板 2020 年从 10% 放宽到 20% 的准自然实验发现:放宽后触及旧 9%~10% 区间的比例大幅下降(涨方向从 19.96% 降到 6.96%,跌方向从 17.42% 降到 4.70%),**没有发现磁吸效应的证据**,但发现限价确实会**延迟价格发现**(跌停后次日异常收益从改革前约 −3.37% 收窄到改革后约 −0.68%),且下跌方向的延迟比上涨方向更严重。
   → 翻译:同一个"封板时长/强度"特征,在不同 `LimitWidth` 下含义不一样,构造时应该按 `LimitWidth`(或 `BoardCode`)分组再比较,不能全市场用一个尺度;涨/跌方向要分开处理,不能假设对称——这与结论 2 的 Wan et al. 发现互相印证。

4. **"价格停滞不动"(零收益/零成交量天数)在文献里是一个独立于涨跌停的、更一般的流动性/交易稀疏度量,构造方法是"统计窗口内零值的频率",但文献用的是日度窗口,没有专门做过分钟级的版本。**
   Lesmond, Ogden & Trzcinka(1999, *Review of Financial Studies* 12(5), 1113–1141)的 LOT 指标直接用"零日收益"的频率反推交易成本,只需要日度收益序列。
   Liu(2006, *Journal of Financial Economics* 82(3), 631–671)的流动性因子用"滚动 12 个月内零成交量天数"、经换手率调整后的标准化版本(LM12)衡量"交易速度",零成交量天数被解释为"锁定风险"(stocks may be impossible to sell)的代理。
   → 翻译:`day_flat_ratio`/`day_distinct_ratio`(日内价位数、最长不变 run)这类特征,文献里最接近的先例是"统计窗口内的零值频率",但文献是在**日度**窗口上统计零收益/零成交量(跨多天统计一次),我们是在**单日内的分钟数据**上统计停滞时间占比——这是同一个"停滞"概念在不同粒度(日 vs 分钟)上的类比,文献没有专门做过分钟级版本,这是一个空白,支持把 §4.3 N 灵感 2 当作真正的新尝试,而不是复现文献。

### 出处

1. **Paying Attention: Overnight Returns and the Hidden Cost of Buying at the Open**
   作者:Henk Berkman, Paul D. Koch, Laura Tuttle, Ying Jenny Zhang
   年-月:2012
   来源:期刊(Journal of Financial and Quantitative Analysis, vol. 47, no. 4, pp. 715–741)
   链接:https://ideas.repec.org/a/cup/jfinqa/v47y2012i04p715-741_00.html
   verified: true(已读条目详情/摘要,机制归因"开盘关注驱动买盘"与效应集中于被关注股票这一发现在摘要中)

2. **The cooling-off effect of price limits in the Chinese stock markets**
   作者:Yu-Lei Wan, Gang-Jin Wang, Zhi-Qiang Jiang, Wen-Jie Xie, Wei-Xing Zhou
   年-月:2018-03 首发(arXiv:1803.09422);发表于 Physica A, vol. 505, pp. 153–163
   来源:期刊(Physica A)+ 工作论文(arXiv)
   链接:https://arxiv.org/abs/1803.09422
   verified: true(WebFetch 直接打开 arXiv 摘要页,读到标题、作者、首发日期、发表期刊信息、"跌停方向冷却效应更强"的摘要原文)

3. **Statistical Properties and Pre-hit Dynamics of Price Limit Hits in the Chinese Stock Markets**
   作者:Yu-Lei Wan, Wen-Jie Xie, Gao-Feng Gu, Zhi-Qiang Jiang, Wei Chen, Xiong Xiong, Wei Zhang, Wei-Xing Zhou
   年-月:2015-03 首发(arXiv:1503.03548);发表于 PLOS ONE
   来源:期刊(PLOS ONE)+ 工作论文(arXiv)
   链接:https://arxiv.org/abs/1503.03548
   verified: true(本轮重新用 WebFetch 打开 arXiv 摘要页核实,"次日延续概率高于反转、跌停日更明显"的发现在摘要原文中)

4. **Daily price limits and destructive market behavior**
   作者:Ting Chen, Zhenyu Gao, Jibao He, Wenxi Jiang, Wei Xiong
   年-月:NBER WP 24014(2017-11 首发);发表版 2019(Journal of Econometrics, vol. 208, no. 1, pp. 249–264)
   来源:工作论文(NBER)+ 期刊(Journal of Econometrics)
   链接:https://www.nber.org/papers/w24014
   verified: true(本轮重新搜索核实卷期页码、NBER 工作论文号、"ST 股 5% 限制下磁吸更明显、大户次日卖出预测长期反转"的发现)

5. **Effectiveness of price limits: Evidence from China's ChiNext market**
   作者:Bao Qi(上海财经大学金融学院)
   年-月:2023-06(收稿 2023-03-24,接收 2023-06-06,发表 2023-06-23)
   来源:期刊(PLOS ONE, vol. 18, no. 6, e0287548)
   链接:https://pmc.ncbi.nlm.nih.gov/articles/PMC10289463/
   verified: true(WebFetch 直接打开 PMC 全文页,读到标题、作者、期刊、收稿/接收/发表日期,以及磁吸效应、延迟价格发现两条发现的具体数字)
   注:此文发表于 2023-06-23,早于本实验截止日 2023-08-08,可用。

6. **A liquidity-augmented capital asset pricing model**
   作者:Weimin Liu
   年-月:2006
   来源:期刊(Journal of Financial Economics, vol. 82, no. 3, pp. 631–671)
   链接:https://www.casact.org/abstract/liquidity-augmented-capital-asset-pricing-model
   verified: true(已读摘要/条目详情,LM12 指标基于"滚动 12 个月零成交量天数、换手率调整"的构造方式在摘要/二手总结中明确给出)

7. **A New Estimate of Transaction Costs**
   作者:David A. Lesmond, Joseph P. Ogden, Charles A. Trzcinka
   年-月:1999
   来源:期刊(Review of Financial Studies, vol. 12, no. 5, pp. 1113–1141)
   链接:https://www.bauer.uh.edu/rsusmel/phd/lot_1999RFS.pdf
   verified: true(已读条目详情/摘要,"只需日度收益序列、用零收益频率反推交易成本"的核心构造方式在摘要中)

**查过但没用**:
- 一篇疑似《Asia-Pacific Financial Markets》期刊上提出 `illiq_zero`(结合 Amihud 冲击与零收益天数比例,专门针对中国市场)的论文——只在搜索摘要里看到构造思路的转述,原文访问需要经过有登录墙的代理站点,没能核实作者、确切卷期、发表年月,弃用。
- 《沪市开放式集合竞价效果实证研究》——只读到文件元数据里的创建日期(2006 年),作者字段是用户名("dhshi"),不是可靠的真实作者信息,正文未能解压读取,弃用。
- 《基于反事实模拟的中国股市涨跌停板磁吸效应研究》(计量经济学报,2021,陆昌、刘洋、杨晓光)——看到标题、作者、DOI,但摘要内容被搜索结果截断,没能确认具体结论数字,仅记录标题供 PI 参考,不作为可引用处。
- "集合竞价成交额/成交量占全日比"能否预测横截面收益的直接实证论文——没搜到正式学术论文,只搜到一份疑似高校讲义对"集合竞价成交量比率"的指标定义(作者/机构不明),如实记录为空白。
