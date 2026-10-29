# 文献:种子 805,B 组,第 3 轮(最后一轮)

对准 `r3/analysis.md` §6 的 L1–L4:§5.3 的 N(筛选式合取 / 硬性分段)与核心 1 外围、§2.2 的致命检验(新特征是不是已知控制变量的非线性改写)、
核心 2 / §2.5 的 D 轴(自身历史分布形状、高阶矩)、§2.6 的波动尾部(极端分钟相对全天均值)。只用 **2023-08-08 之前**发表的论文 / 工作论文 / 研究报告
(journal 用正式出版日期,working paper 用首版 / 流通日期)。r1 的 L1–L4、r2 的 L1–L4 已经问过的题目这里不再重复问,但同一篇文献如果确实对本轮的题目也适用,
会重新给出并说明是哪一轮先引用的。每条处理手法后面用 `[Sx]` 指向文末的出处表;`verified: true` = 这次搜索结果、二手摘要或页面上确实看到了标题 / 作者 / 期刊 / 卷期 / 链接这组信息对得上,
不是凭记忆写的;`verified: false` 或带强保留的条目只记录「存在、主题对得上」,不据此写任何具体处理手法或数字当证据用。拿不准发表年月、卷期或页码的,正文和出处表里都如实标注「未独立核实」。

本轮方法论说明:这四题比前两轮更偏「方法论」而不是「某个具体异象」,很多检索命中的是教材章节(Bali-Engle-Murray、Grinold-Kahn)和二手书评 / 论坛摘要,
而不是期刊论文原文摘要。教材不是「论文或工作论文」,但贴近 PLAN §2.6 允许的「研究报告」口径,我按「结论先说 + 如实标注是教材不是期刊文章」的方式收录,
并把这类条目在出处表里单独标注,PI 使用时请对待为「业界方法论共识的旁证」,不要当成和期刊论文同等权重的证据。本轮没有一条文献来自 WebFetch 直接打开原文核对
(搜索引擎二次摘要已经能覆盖题目所需的方法论层面细节,我尝试对 Freyberger-Neuhierl-Weber 的 NBER PDF 做二次核对但只重复确认了摘要,没有读出比摘要更多的构造细节,
所以本轮的 verified 全部基于搜索结果 / 二手摘要页面,不是原文页内核对)。

## L1.「先筛选再排序」的构造:条件双重排序怎么选参数、怎么报告(对准 §5.3 的 N 与核心 1 外围)

**结论先说**:条件(sequential)双重排序与独立(independent)双重排序是教材里明确区分、互相不等价的两种方法,核心区别是「先排的变量对结果的影响更大、且结果依赖排序顺序」——
这正好解释了 §5.4(i) 我们自己发现的「原始秩禁令」现象(筛选变量相近时合取候选会被挡)。断点 / 筛选阈值的稳健性检验,文献里确实常做「换一组阈值、分子样本重新跑」,
但做法集中在「按市值分组重跑」和「迭代收缩股票空间再检验异象是否还显著」这两种,**没有一篇我搜到的文献报告过「被筛掉的那部分股票自己的收益」**,也**没有找到任何文献讨论
「筛选带宽与多头持仓档位宽度接近时因子会失效」这个我们自己实测出来的现象**——这两条在允许的文献范围内是真正的空白,不是没搜够。

1. **条件排序(dependent sort)与独立排序(independent sort)是两种有明确定义区别的方法,教材专门单列章节对比**:Bali, Engle & Murray,*Empirical Asset Pricing: The Cross Section of Stock Returns*(Wiley,2016)第 5 章分别用 5.2 节讲独立双重排序(断点、建仓、结果解读)、5.3 节讲条件双重排序(断点、建仓),5.4 节专门标题为「Independent versus Dependent Sort」做对比 [S1](**教材,不是期刊论文**;我核对到的是多个图书馆 / 书店对该章节目录的独立列出,章节标题与页码一致,没有读到正文内容本身)。
   → 操作语言:这给了我们现成的方法论词汇——`cs_first_*` / `cs_last_*` 配合先筛选变量再排序变量的写法,对应的是**条件(dependent/sequential)双重排序**;如果 N 位想测试「换筛选顺序结果会不会变」,等价于教材 5.4 节的比较,这是一个本轮没人做过的、现成可做的消融(先按排序变量分组再筛,对比先筛再按排序变量分组)。
2. **条件排序的核心风险:先排的变量支配结果,换顺序结果会变**(经由对 portsort 这类排序工具文档的交叉确认,工具文档本身总结的是学界公认的方法论共识,不是独立学术发现,**这条不进出处表当独立证据,只作背景常识陈述**)。
3. **按市值分组重跑是文献里最常见的「换一组筛选阈值 / 换子样本」稳健性检验,而且明确报告了「样本子集很小的组不稳健」**:Fama & French,「Dissecting Anomalies」,*Journal of Finance* 63(4),1653–1678(2008-08)。他们在每年 6 月底用 NYSE 20 分位与 50 分位断点把股票分成三组(micro/small/big),发现 microcap 约占样本股票数的 60% 却只占总市值的 3%,很多异象(资产增长、动量减半、盈利能力只在 small 组显著)**只在某些市值分组里成立**,且 net stock issues 与 accruals 的异常收益主要由**极端值**驱动 [S2]。
   → 操作语言:这是「换一组筛选阈值、分子样本报告」最接地气的模板——核心 1 / N 位任何涉及按某个变量筛选的候选,都应该报告「筛选阈值换成另外 1~2 档、按市值分三组分别看 score」,而不是只报全市场一个数字;这也支持我们本轮「至少放一对排除 vs 选择」的要求,因为 Fama-French 这里显示不同市值分组里同一个异象可以方向一致但强度差很多。
4. **迭代收缩股票空间、重新检验异象,是另一种成体系的稳健性设计**:Jiang & Zhang,「The Shrinking Space for Anomalies」(工作论文,2011-03)用两种方式收缩股票空间——(a) 按十个经典异象各自分十分位,从对冲组合的买入端和卖出端逐档剔除,每剔除一档重新检验异象是否还显著;(b) 剔除最小市值与最极端账面市值比的股票,直到规模、价值、动量在四因子模型下都不再显著,再在这个「净化」后的样本上重新检验其余异象,发现大多数异象在净化后不再稳健 [S3](**这条我只核对到一个二手博客摘要与一场高校学术报告的标题记录,没能定位到论文本身的 SSRN / 期刊页面,作者名「George Jiang / Andrew Zhang」与那场报告列出的报告人「Jiang Jinyong」是否是同一人也没能核实,按「存在但强保留」收录,PI 使用这条的具体结论前应再核实一次**)。
   → 操作语言:方法 (a)「从两端逐档剔除、每次重新评分」正是「报告被筛掉的那部分」这个要求的最接近的模板,但它剔除的是**同一个变量**的极端分位(不是我们「用筛选变量排除掉的股票,看它们自己表现如何」),所以不能照抄,只能当作「做法存在、可以类比」的参照。
5. **条件双重排序在横截面定价文献里是常规武器,实际使用时控制变量数量通常只到 2 个,断点数量 3~5 档最常见**:Bali, Cakici & Whitelaw,「Maxing Out: Stocks as Lotteries and the Cross-Section of Expected Returns」,*Journal of Financial Economics* 99(2),427–446(2011),NBER 工作论文版更早。该文用 MAX(前一月最大单日收益)做横截面排序,同时用条件双重排序控制规模、账面市值比、动量、短期反转、流动性、偏度等变量,发现 MAX 最高最低两组收益差超过 1%/月,且这个关系在控制了 Ang 等人(2006, 2009)的特质波动率之后依然存在、甚至反转了特质波动率的方向 [S4]。
   → 操作语言:这是「排序变量 + 控制变量」这套条件双重排序在成熟文献里的标准用法,控制变量通常每次只放 1~2 个(不是一次性放 6 个),这给核心 1 的 N 位一个参照:**与其一次性堆更多控制变量,不如每次只加一个,逐个报告增量**,这样能把「哪个控制变量真正吃掉了效应」讲清楚,而不是像我们本轮 E 位那样一次性把 6 个 head 都作为控制。
6. **更正式的、关于「排序断点数量怎么选」的econometric 处理,存在但是渐近理论,不是经验规则**:Cattaneo, Crump, Farrell & Schaumburg,「Characteristic-Sorted Portfolios: Estimation and Inference」,*Review of Economics and Statistics* 102(3),531–551(2020-07;NBER / 纽约联储工作论文版本至少到 2018 年)。论文把「分成多少组」形式化为一个非参数估计问题,组数趋向无穷时等价于核回归 [S5](**这条我只核对到标题、作者、期刊卷期页码与一段摘要描述,没有读到它对「组数怎么选」给出的具体经验规则——论文本身是纯方法论 / 渐近理论性质,不是某个异象的经验检验,PI 如果想用这条的具体建议,需要再去读论文正文**)。
   → 操作语言:它提示「组数」本质上是一个偏差-方差权衡(组数越多越像非参数回归、方差越大;组数越少越像粗分组、偏差越大),这和我们 band 10%/20%/40% 的网格测试思路一致,但论文没有给出具体「几档最优」的经验数字,不能照搬。
7. **搜不到的部分(如实列出,不进出处表当证据用)**:
   - 没有搜到任何文献把「被筛选剔除掉的那部分股票,它们自己的收益表现如何」当作一条独立的稳健性检验来报告(§5.4 之外,只有 Jiang-Zhang 的「逐档剔除再检验剩下的」这种间接做法)。
   - 没有搜到任何文献讨论过「纯多头组合构造中,筛选带宽与持仓十分位宽度接近时筛选效应会消失」这个我们自己实测出来的现象;Clarke, de Silva & Thorley,「Portfolio Constraints and the Fundamental Law of Active Management」,*Financial Analysts Journal* 58(5),48–66(2002)讨论的是长仅约束会引入「意外的小盘股偏向」、降低转移系数(transfer coefficient)[S6],这是**同一大类问题(长仅约束吃掉信息)的旁证**,但不是对我们这个具体现象的直接检验,不能当作文献支持。
   - 条件排序与「对控制变量做线性回归残差」的直接对比(哪个更稳健、哪个丢信息更多),没有搜到专门做这个对比的论文,只有 Freyberger-Neuhierl-Weber(见 L2 [S7])从「非参数方法整体优于线性方法」的角度间接说明,但那篇不是专门比较「排序」与「回归残差」这两种具体操作。

## L2. 新特征是已知控制变量的非线性函数:文献怎么查、怎么报告(对准 §2.2,本轮最硬的否证)

**结论先说**:「用非参数 / 非线性方法重新检验一批特征,发现很多特征在控制了其他特征之后不再提供增量信息」这件事,文献里有明确的、方法论成熟的处理
(非参数特征选择、spanning test、double-selection LASSO),而且结论方向和我们本轮 §2.2 的发现(线性中性化 + 秩相关门槛完全没查出「本质是已知族的非线性改写」)一致——
**非线性关系确实会被线性方法漏掉,这不是我们环境的特例,是文献里反复强调的一般结论**。在「成交量 / 流动性」这一大类特征内部「哪些是同一个东西的不同写法」这个具体问题上,
也有直接可用的文献(流动性代理横向比较、Amihud 指标的量价分解)。

1. **非参数方法明确发现:很多特征控制住其他特征后不再提供增量信息,且非线性很重要**:Freyberger, Neuhierl & Weber,「Dissecting Characteristics Nonparametrically」,*Review of Financial Studies* 33(5),2326–2377(2020);NBER 工作论文 No. 23227 首版 2017-03。方法是用 adaptive group LASSO 同时做特征选择和非参数估计特征对预期收益的影响,核心结论是「很多此前被认定有效的收益预测变量,在控制其他变量后并不提供增量信息,而且非线性很重要」,相比线性面板回归样本外解释力更高、夏普比率提升约 50% [S7]。
   → 操作语言:这篇直接支持我们本轮§2.2「线性中性化 + 秩相关门槛查不出非线性重合」的判断——**这不是我们的方法用错了,是整个领域都知道线性方法在这里系统性地漏东西**。对应到我们的算子语言,一个可操作的下一步检验是:把某个候选信号和它怀疑重合的已知族特征一起,用「分桶内排序」(相当于非参数条件化的离散近似)而不是「减去线性回归残差」去看信号还剩多少,这正是 R2(把筛选变量换成已知族)那条测量想问的问题的更一般版本。
2. **用 spanning test 检验「一组特征能不能被另一组特征张成」,是比相关系数更正式的冗余检验**:Huberman & Kandel,「Mean-Variance Spanning」,*Journal of Finance* 42(4),873–888(1987-09)。该文给出检验「K 个基准资产张出的最小方差前沿」是否等于「K 个基准资产加若干个额外测试资产张出的前沿」的联合统计量,原始应用是检验 3 个规模分组组合是否被 33 个规模分组组合张成 [S9]。
   → 操作语言:这是「秩相关系数」之外的一个更正式的冗余检验选项——如果 PI 怀疑某个新 head 和已知族只是同一个东西的另一种写法,除了算秩相关,还可以把新 head 和已知族一起做一个小型 spanning test(新 head 加入已知族的最小方差前沿是否显著扩大),这比单一相关系数阈值更难被「非线性但高度重合」的情况绕过。
3. **更现代的版本:double-selection LASSO + 两步回归,专门用来判断一个新因子是不是「冗余」(能被已知因子张成)**:Feng, Giglio & Xiu,「Taming the Factor Zoo: A Test of New Factors」,*Journal of Finance* 75(3),1327–1370(2020-06);NBER 工作论文 No. 25481。方法结合 Belloni 等(2014)的 double-selection LASSO 与 Fama-MacBeth 两步回归,专门检验一个新提出的因子相对于已有的大型因子库是否提供显著的增量定价能力,并且在「新因子被判定为冗余」时能同时给出一小组张成它的已有因子 [S8]。
   → 操作语言:这是目前搜到的、方法论上**最直接回应「一个新特征是不是已知特征的非线性改写」**的现代处理——比简单相关系数门槛更稳健,但它是回归框架、不是我们这种 GP + 禁令框架,照搬需要工程改造,不适合在仅剩的这一轮里现做,**可以写进 notebook 作为「C05 之后值得补的定位工具」,而不是本轮任务书的内容**。
4. **特征匹配基准(characteristic-matched benchmark)是「分桶内控制」最早的系统化做法之一**:Daniel, Grinblatt, Titman & Wermers,「Measuring Mutual Fund Performance with Characteristic-Based Benchmarks」,*Journal of Finance* 52(3),1035–1058(1997)。他们按市值、账面市值比、前一年收益率各分五档,构造 125 个被动组合作为基准,逐个匹配基金持仓里的每只股票 [S10]。
   → 操作语言:这正是我们 `cs_bucket_zscore` 这类「先按一个变量分桶、再在桶内看另一个变量的相对位置」构造的学术原型——DGTW 分桶数是 5×5×5=125,比我们 band 10%/20%/40% 的细一些,如果 N 位想测试「桶数本身要不要更细」,DGTW 的 5 档是一个有文献背书的参照点,而不需要凭空试。
5. **「流动性代理之间互相重合多少」这一类问题,文献里直接做过大规模horse race**:Goyenko, Holden & Trzcinka,「Do Liquidity Measures Measure Liquidity?」,*Journal of Financial Economics* 92(2),153–181(2009)。他们把大量常用的低频(日度数据)流动性代理和他们新构造的代理,与基于逐笔数据算出的流动性基准做相关性和预测误差两类比较;摘要与二手总结给出的方向是:在价差类代理里,Amihud 与基准相关性较好、LOT 预测误差较小;在价格冲击类代理里,除 Pastor-Stambaugh 外大多数低频代理与高频基准相关性都较高 [S11]。
   → 操作语言:这直接支持我们 §2.1「成交额离散度、换手、非流动性这些量可能是同一个东西」的判断——文献证实这些低频流动性代理彼此高度相关,所以 N 位如果打算同时放入"换手类"与"成交额离散度类"筛选变量,应该先预期它们在原始秩上就高度重合,大概率会被 §5.4(i) 的原始秩禁令挡掉同一批,不必浪费种子凡事都试一遍。
6. **「成交量」本身可能是 Amihud 非流动性溢价真正的驱动力,而不是价格冲击本身**:Lou & Shu,「Price Impact or Trading Volume: Why Is the Amihud (2002) Measure Priced?」,*Review of Financial Studies* 30(12),4481–4520(2017-12);工作论文版至少到 2016-08。该文把 Amihud 非流动性指标(日收益绝对值 / 成交额)分解成「成交量分量」和「价格冲击分量」,发现 Amihud 溢价主要由**成交量分量**驱动,不是价格冲击本身 [S12]。
   → 操作语言:这是对 §2.2「新特征的条件变量 `cross_mean(day_std(Amt), 30)` 本质是已知族」这个判定最直接的方法论支持——**同一大类指标里,"离散度 / 波动"写法和"成交量水平"写法可能被证明是同一个驱动力的两种包装**,Lou-Shu 给出的具体检验方法是「分解 + 看哪个分量承担了溢价」,这比单纯算相关系数更能回答"是不是同一个东西",PI 如果想在最终库里再确认一次核心 1 的独立性,可以考虑类似的分解思路(虽然这超出本轮剩余的算力)。
7. **「分桶内标准化 / 中性化」是业界量化方法论教材里成体系的标准操作,但这是教材不是期刊论文**:Grinold & Kahn,*Active Portfolio Management*(第 2 版,McGraw-Hill,2000)第 14 章「Neutralization of Alpha」讨论了基准中性化、现金中性化等几种「把不想要的暴露置零」的标准化操作,z-score 定义为预测值减去其期望、除以标准差 [S13](**教材,不是期刊论文,我只核对到多个论坛 / 书评对该章节内容的转述,没有读到书的正文**)。
   → 操作语言:这给了我们 `cs_bucket_zscore` 这类构造一个业界方法论名称——「中性化(neutralization)」,是分析师和量化机构的标准操作而不是我们这边的新发明,但教材没有给出「分桶数 / 标准化窗口怎么选」的经验规则,这部分仍然要靠我们自己的网格测试。
8. **搜不到的部分**:没有搜到专门讨论「秩相关不高但经济含量重合」这类案例、并建议用某个具体统计量代替秩相关系数的论文(Huberman-Kandel 的 spanning test 和 Feng-Giglio-Xiu 的 double-selection LASSO 是两个可以类比的候选,但都不是专门针对"秩相关"这个具体统计量的讨论,是更上位的冗余检验框架)。

## L3. 自身历史分布形状(偏度 / 极值)作为横截面特征(对准核心 2 / §2.5)

**结论先说**:「用某个日内统计量的多日水平/均值去预测收益」这一支(高成交量溢价、持续性特征)文献扎实(且 r1 已经引用过 Gervais-Kaniel-Mingelgrin 与 Lee-Kim-Kim,这里不重复);
但「把这个日度序列自己的高阶矩(偏度)当特征」这个更窄的问题,**我搜不到任何文献把"成交量"或"日内成交离散度"的历史序列偏度本身当作横截面选股特征来检验**——这是信息,不是搜索失败。
离这个问题最近的文献是用**日内高频收益**(不是成交量)构造的"已实现偏度",它们确实讨论过偏度统计量对极端观测值的敏感性、以及怎么用高频采样而不是粗颗粒数据来稳健化这个统计量,这部分可以类比过来。

1. **已实现偏度(用高频收益构造,不是用成交量构造)是经过验证的横截面负向预测变量,而且构造方式本身就是对"偏度对极值敏感"问题的一种稳健化**:Amaya, Christoffersen, Jacobs & Vasquez,「Does Realized Skewness Predict the Cross-Section of Equity Returns?」,*Journal of Financial Economics*(2015;DOI 10.1016/j.jfineco.2015.02.009,二手摘要给出的期号是 2015 年 10 月号、页码 135–167,具体卷号未独立核实——Swedroe 的转述文章推断是第 118 卷第 1 期,但我没能在期刊官方页面上直接核对到卷号,此处如实标注);早期工作论文版题为「Do Realized Skewness and Kurtosis Predict the Cross-Section of Equity Returns?」,CREATES Research Paper 2011-44。方法是用五分钟高频收益算每周已实现偏度,发现低已实现偏度组合跑赢高已实现偏度组合,长短组合次周平均收益约 19 个基点(t≈3.70),Fama-French + Carhart 因子控制不住;已实现峰度与下一周收益正相关但不总是显著 [S14]。
   → 操作语言:这篇给出的不是"成交量偏度",是"收益偏度",但方法论直接可以类比:**用高频(分钟级)数据算出的偏度,比用日度 / 更粗颗粒数据算出的偏度更稳健**,因为高频下单个极端观测值对整个窗口三阶矩的占比被摊薄了。对应到我们的 `ts_skew(day_wstd(Volume, Vwap), 50)` 这个构造——`day_wstd` 本身已经是用日内(分钟级)数据算出的一个日度统计量,`ts_skew` 是在这个日度统计量的 50 日序列上再取偏度,这是"时间序列层面的偏度",不是"日内分布层面的偏度",Amaya 等人的稳健化逻辑(用更细颗粒度摊薄极值)在我们这个"日度序列偏度"层面不能直接套用,因为我们的输入已经是日度聚合后的值,50 个观测值本身样本量就小,极值敏感问题可能比 Amaya 等人用分钟数据算单周偏度更严重,这是一个**文献没有覆盖、我们自己要留意的风险点,不是文献已经解决的问题**。
2. **搜不到的部分(逐项如实列出)**:
   - 没有搜到任何文献把"一只股票自身成交量(或成交额、换手率)历史序列的偏度 / 峰度"本身当作横截面选股特征来检验;搜到的"成交量冲击"(abnormal volume shock)、"高成交量溢价"文献全部是**事件式**(某一天的成交量相对自身近期均值有多异常)或**水平式**(近期成交量 / 换手率绝对水平高低),不是"50 天窗口里成交量序列的分布形状"这种**分布式**构造。
   - 因此"事件式(某一天放量)与分布式(50 天偏度)两种写法有没有被放在一起比较过"——**没有搜到**,这两支文献在搜索结果里几乎不互相引用、不在同一张表里比较。
   - "日内成交离散度"(而不是日成交量水平)的日度序列,拿来做偏度 / 高阶矩分析的文献——**没有搜到**。
   - "偏度这类统计量在重尾正序列上几乎由最大的一个观测决定"这个统计学一般性问题,Amaya 等人的高频构造是一种**间接**的应对方式(把粗颗粒度换成细颗粒度),但没有搜到专门讨论"winsorize / 分位数差 / 极值计数代替三阶矩"这几种具体稳健化手段、并在金融特征构造场景下比较它们的论文。
   - VWAP / 执行价位对齐这类"日内价格水平"特征,学术文献里几乎全部出现在**交易执行成本评估**场景(VWAP 作为被动交易者的近似成本基准),源头是 Berkowitz, Logue & Noser,「The Total Cost of Transactions on the NYSE」,*Journal of Finance* 43(1),97–112(1988)[S20](这条本身是扎实的经典引用,但它回答的是"VWAP 怎么被当执行成本基准用",不是"日内量在高位还是低位相关这类量怎么被当横截面特征构造",所以只能算背景常识,不直接支持我们 M3 那个 head 的内层构造——那个"当天分钟成交量与分钟价位的相关"式的构造,在允许的文献范围内**没有找到先例**)。

## L4. 日内波动尾部相对自身均值水平,作为横截面特征(对准 §2.6)

**结论先说**:「把已实现波动拆成连续部分与跳跃部分」这一支文献非常扎实、方法论成熟(bipower variation、已实现四次幂变差),且跳跃风险的横截面定价方向在**总量 / 系统性**层面是明确的
(对跳跃 / 波动风险敏感的股票预期收益更低,也就是"波动均匀、无明显跳跃的股票收益更高"这个方向有间接支持);但「哪些分钟是'最重的'(成交最大)」与「哪些分钟是'最极端的'(波动最大)」
**不是同一件事**,而且文献里有一篇经典论文明确说"成交量最大的那批交易"未必是推动价格变动最多的那批交易——这对我们 §2.6 那个 head 用"成交最重的 10% 分钟"而不是"波动最大的 10% 分钟"
提了一个需要谨慎对待的警示。

1. **跳跃与连续波动的分解,方法论原点**:Barndorff-Nielsed & Shephard,「Power and Bipower Variation with Stochastic Volatility and Jumps」,*Journal of Financial Econometrics* 2(1),1–37(2004;首版工作论文 2003,牛津 Nuffield College)。核心思路是已实现方差(realized variance)同时捕捉连续波动和跳跃,而二次幂变差(bipower variation)对跳跃稳健,两者的差就能把二次变差(quadratic variation)分解成连续部分和跳跃部分,论文称这"可能是第一个能把二次变差分解成连续与跳跃两部分的方法" [S16]。
   → 操作语言:这是"日内波动尾部相对全天平均"这类构造的标准学术分解——`day_topw_mean(abs_(Ret), Ret)`(最极端若干分钟的 |收益| 占比)在方法论上接近"跳跃占比"的一个简化、非参数版本;如果想更贴近文献标准做法,可以考虑构造 `(已实现方差 − 二次幂变差) / 已实现方差` 这个比值作为备选写法,和我们现有的 `cs_bucket_zscore(...topw_mean..., ...mean...)` 做对照。
2. **配套的"已实现四次幂变差"(quarticity),是检验这类统计量显著性时需要的标准化分母**:Barndorff-Nielsen & Shephard,「Econometric Analysis of Realized Volatility and Its Use in Estimating Stochastic Volatility Models」,*Journal of the Royal Statistical Society: Series B* 64(2),253–280(2002)。论文推导了已实现波动误差(已实现波动与积分波动之差)的矩与渐近分布,"quarticity"是该文的关键词之一 [S17]。
   → 操作语言:如果 PI 之后想对"跳跃占比"类特征做显著性检验而不是只做横截面排序,这篇给出的是标准化分母的理论来源,但本轮不需要做到这个精细度。
3. **跳跃对横截面收益可预测性确实有贡献,但不是对所有已知异象都有贡献**:Jiang & Yao,「Stock Price Jumps and Cross-Sectional Return Predictability」,*Journal of Financial and Quantitative Analysis* 48(5),1519–1544(2013-10)。用日度价格识别跳跃,发现基于价值加权组合时,跳跃能解释价值溢价,但不能解释动量或净股票发行这两个异象 [S18]。
   → 操作语言:这提示"跳跃相关的横截面效应"不是一个万能解释,E/N 位如果想在 D 轴继续挖,不该预设"只要是和跳跃/极值相关的构造就一定有效",要分异象讨论。
4. **系统性跳跃与波动风险的价格是负的——对跳跃/波动风险敏感的股票预期收益更低**:Cremers, Halling & Weinbaum,「Aggregate Jump and Volatility Risk in the Cross-Section of Stock Returns」,*Journal of Finance* 70(2),577–614(2015-04)。发现对总量跳跃风险和总量波动风险敏感度高的股票,预期收益显著更低,两者的风险价格都是负的 [S19]。
   → 操作语言:这是对"波动均匀 / 无明显跳跃的股票收益更高"这个方向**最直接的间接支持**——但要注意,这篇测的是对**系统性(总量)**跳跃/波动风险的**敏感度(beta)**,不是个股自己历史上有没有出现过跳跃,这是两个不同的构造(系统性暴露 vs 自身历史统计量),不能简单等同,PI 如果想用这条支持 §2.6 那个 head 的方向,要在任务书里写清楚"文献支持的是系统性跳跃暴露为负价格,我们的 head 测的是个股自身极端分钟占比,是一个类似但不完全相同的构造"。
   这篇和 Jiang & Yao [S18]、Barndorff-Nielsen & Shephard [S16] 都没有专门讨论"怎么排除流动性和交易成本的解释"这个具体稳健性步骤——**这部分没有搜到直接文献**。
5. **成交量最大的那批交易,未必是推动价格变化最多的那批——"大单驱动价格"这个直觉在经典实证里是有条件成立的,不是无条件成立的**:Barclay & Warner,「Stealth Trading and Volatility: Which Trades Move Prices?」,*Journal of Financial Economics* 34,281–305(1993)。用 108 次要收购事件的 NYSE 审计轨迹数据发现,虽然大多数交易是小单,但累积价格变动的大部分来自**中等规模**的交易,不是最大的单子,作者据此提出"隐蔽交易假说"(知情交易者倾向于用中等规模的单子隐藏自己)[S15](二手摘要之间页码有 281–305 / 281–306 的细微差异,未独立核实到精确结尾页)。
   → 操作语言:这对我们 §2.6 那个 head 的内层构造——"成交最重的 10% 分钟"(`day_topw_mean`,用成交量加权)——是一个**需要谨慎对待而不是直接采信的提醒**:文献的经典发现是"最大的单子"未必是"推动价格最多的单子",中等单子才是;如果 N 位想继续在这条轴上扩展,"成交最重的 10% 分钟"与"价格变动最大的 10% 分钟"是两个不同的筛选标准,**该不该用成交量当权重、还是该直接用价格变化幅度当权重,文献这里给出的是反对"越大越重要"这个朴素假设的证据,不是支持它的证据**。
6. **搜不到的部分**:
   - 没有搜到任何文献明确报告过"跳跃风险的横截面定价"研究里专门排除流动性与交易成本解释的具体方法(例如像 Novy-Marx & Velikov [r2 已引用] 那样做成本敏感性分析)。
   - 没有搜到专门比较"用波动最大的 10% 分钟"与"用成交最重的 10% 分钟"这两种筛选标准、并直接对照它们对收益预测力差异的论文——Barclay-Warner [S15] 只是从"哪类交易推动价格"这个相邻问题给出一个方向性警示,不是对我们这个具体对照的直接检验。
   - "日内已实现四次幂变差与已实现波动之比"这个具体比值作为横截面特征的检验,没有搜到(只搜到它作为显著性检验标准化分母的理论角色 [S17])。

## 出处表

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|---|
| S1 | Empirical Asset Pricing: The Cross Section of Stock Returns(第 5 章,5.2–5.4 节:独立 / 条件双重排序) | Turan G. Bali, Robert F. Engle, Scott Murray | 2016-04 | Wiley(教材,ISBN 978-1-118-09504-1) | https://www.wiley-vch.de/en/areas-interest/finance-economics-law/empirical-asset-pricing-978-1-118-09504-1 | true(**教材而非期刊论文**;标题、作者、出版社、章节编号经多个书店 / 图书馆目录的独立列出互相核对一致,未读到正文) |
| S2 | Dissecting Anomalies | Eugene F. Fama, Kenneth R. French | 2008-08(JF 63(4), 1653–1678) | Journal of Finance, 63(4), 1653–1678 | https://ideas.repec.org/a/bla/jfinan/v63y2008i4p1653-1678.html ; https://www.johnhcochrane.com/s/fama_french_dissecting_anomalies_JF.pdf | true |
| S3 | The Shrinking Space for Anomalies | George Jiang, Andrew Zhang(署名未完全独立核实) | 2011-03(工作论文) | 未确认期刊 / SSRN 出处,仅见二手博客摘要与一场高校学术报告列表 | https://www.cxoadvisory.com/?p=12818 | true,但强保留(**只核对到标题 / 日期 / 方法描述出现在二手摘要页面,没有定位到论文原始页面,作者是否与某高校报告的报告人为同一人也未核实,PI 引用具体结论前应再核实一次**) |
| S4 | Maxing Out: Stocks as Lotteries and the Cross-Section of Expected Returns | Turan G. Bali, Nusret Cakici, Robert F. Whitelaw | 2011(JFE 99(2), 427–446;NBER WP No. 14804 为更早版本) | Journal of Financial Economics, 99(2), 427–446 | https://www.nber.org/papers/w14804.pdf ; https://archive.nyu.edu/handle/2451/27871 | true |
| S5 | Characteristic-Sorted Portfolios: Estimation and Inference | Matias D. Cattaneo, Richard K. Crump, Max H. Farrell, Ernst Schaumburg | 2020-07(Review of Economics and Statistics 102(3), 531–551;NBER / NY Fed 工作论文版至少到 2018) | Review of Economics and Statistics, 102(3), 531–551 | https://arxiv.org/abs/1809.03584 ; https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr788.pdf | true(标题 / 作者 / 期刊卷期页码核对一致;论文对「组数怎么选」的具体建议未读到正文,只核对到方法论定位) |
| S6 | Portfolio Constraints and the Fundamental Law of Active Management | Roger Clarke, Harindra de Silva, Steven Thorley | 2002(FAJ 58(5), 48–66) | Financial Analysts Journal, 58(5), 48–66 | https://ideas.repec.org/a/taf/ufajxx/v58y2002i5p48-66.html | true |
| S7 | Dissecting Characteristics Nonparametrically | Joseph Freyberger, Andreas Neuhierl, Michael Weber | 2020(RFS 33(5), 2326–2377;NBER WP No. 23227,首版 2017-03) | Review of Financial Studies, 33(5), 2326–2377 | https://www.nber.org/papers/w23227 ; DOI 10.1093/rfs/hhz123 | true |
| S8 | Taming the Factor Zoo: A Test of New Factors | Guanhao Feng, Stefano Giglio, Dacheng Xiu | 2020-06(JF 75(3), 1327–1370;NBER WP No. 25481) | Journal of Finance, 75(3), 1327–1370 | https://www.nber.org/papers/w25481 ; DOI 10.1111/jofi.12883 | true |
| S9 | Mean-Variance Spanning | Gur Huberman, Shmuel Kandel | 1987-09(JF 42(4), 873–888) | Journal of Finance, 42(4), 873–888 | https://ideas.repec.org/a/bla/jfinan/v42y1987i4p873-88.html | true |
| S10 | Measuring Mutual Fund Performance with Characteristic-Based Benchmarks | Kent Daniel, Mark Grinblatt, Sheridan Titman, Russ Wermers | 1997(JF 52(3), 1035–1058) | Journal of Finance, 52(3), 1035–1058 | https://ideas.repec.org/a/bla/jfinan/v52y1997i3p1035-58.html | true |
| S11 | Do Liquidity Measures Measure Liquidity? | Ruslan Y. Goyenko, Craig W. Holden, Charles A. Trzcinka | 2009(JFE 92(2), 153–181) | Journal of Financial Economics, 92(2), 153–181 | https://www.icmagroup.org/assets/documents/Regulatory/Secondary-markets/Bond-Market-Liquidity-Library/Goyenko-RY_Holden-CW_Trzcinka-CA---2009---Do-liquidity-measures-measure-liquidity-290118.pdf | true |
| S12 | Price Impact or Trading Volume: Why Is the Amihud (2002) Measure Priced? | Xiaoxia Lou, Tao Shu | 2017-12(RFS 30(12), 4481–4520;工作论文版至少到 2016-08) | Review of Financial Studies, 30(12), 4481–4520 | https://academicnewsletter.sufe.edu.cn/info/353351 ; https://icmagroup.org/assets/documents/Regulatory/Secondary-markets/Bond-Market-Liquidity-Library/Lou-X_Shu-T---2016---Price-Impact-or-Trading-Volume-Why-is-the-Amihud-2002-Illiquidity-Measure-Priced-290118.pdf | true |
| S13 | Active Portfolio Management(第 2 版,第 14 章:Neutralization of Alpha) | Richard C. Grinold, Ronald N. Kahn | 2000 | McGraw-Hill(教材) | https://forum.bionicturtle.com/threads/neutralization-of-alpha-aim-53-3-grinold-kahn-chapter-14.7341 | true(**教材而非期刊论文**;章节标题与核心定义经培训论坛对该章节的转述核对,未读到书的正文原文) |
| S14 | Does Realized Skewness Predict the Cross-Section of Equity Returns? | Diego Amaya, Peter Christoffersen, Kris Jacobs, Aurelio Vasquez | 2015(JFE,DOI 10.1016/j.jfineco.2015.02.009;二手摘要给出期号为 2015-10、页码 135–167,具体卷号未独立核实;早期工作论文版 CREATES Research Paper 2011-44,题为"Do Realized Skewness and Kurtosis Predict…") | Journal of Financial Economics | DOI 10.1016/j.jfineco.2015.02.009 ; https://repec.econ.au.dk/repec/creates/rp/11/rp11_44.pdf | true(标题 / 作者 / DOI / 核心数字 19bp,t≈3.70 经学术转述页核对;**卷号推断为 118 卷第 1 期,未在期刊官方页面独立核实,如实标注**) |
| S15 | Stealth Trading and Volatility: Which Trades Move Prices? | Michael J. Barclay, Jerold B. Warner | 1993(JFE 34, 281–305,二手摘要间页码有 281–305 / 281–306 的细微差异) | Journal of Financial Economics, 34, 281–305 | DOI 10.1016/0304-405X(93)90029-B | true |
| S16 | Power and Bipower Variation with Stochastic Volatility and Jumps | Ole E. Barndorff-Nielsen, Neil Shephard | 2004(Journal of Financial Econometrics 2(1), 1–37;首版工作论文 2003,Nuffield College, Oxford) | Journal of Financial Econometrics, 2(1), 1–37 | DOI 10.1093/jfec/nbh001 ; https://academic.oup.com/jfec/article/2/1/1/960705 | true |
| S17 | Econometric Analysis of Realized Volatility and Its Use in Estimating Stochastic Volatility Models | Ole E. Barndorff-Nielsen, Neil Shephard | 2002(JRSS Series B 64(2), 253–280) | Journal of the Royal Statistical Society: Series B, 64(2), 253–280 | DOI 10.1111/1467-9868.00336 | true |
| S18 | Stock Price Jumps and Cross-Sectional Return Predictability | George J. Jiang, Tong Yao | 2013-10(JFQA 48(5), 1519–1544) | Journal of Financial and Quantitative Analysis, 48(5), 1519–1544 | DOI 10.1017/S0022109013000513 | true |
| S19 | Aggregate Jump and Volatility Risk in the Cross-Section of Stock Returns | Martijn Cremers, Michael Halling, David Weinbaum | 2015-04(JF 70(2), 577–614) | Journal of Finance, 70(2), 577–614 | DOI 10.1111/jofi.12220 ; https://ideas.repec.org/a/bla/jfinan/v70y2015i2p577-614.html | true |
| S20 | The Total Cost of Transactions on the NYSE | Stephen A. Berkowitz, Dennis E. Logue, Eugene A. Noser Jr. | 1988(JF 43(1), 97–112) | Journal of Finance, 43(1), 97–112 | DOI 10.1111/j.1540-6261.1988.tb02591.x | true(背景引用,回答的是 VWAP 作为执行成本基准的来源,不直接支持我们的特征构造,详见 L3 第 2 条「搜不到的部分」) |

## 给 PI 的汇总(哪些处理手法有文献撑,哪些没有,哪些要谨慎)

- **L1 最可操作的一条**:核心 1 / N 位的条件双重排序,方法论名字和标准参数参照 Bali-Engle-Murray 教材 [S1] 与 Fama-French (2008) [S2]——**控制变量一次只加 1~2 个、逐个报告增量**(参照 Bali-Cakici-Whitelaw [S4] 的做法),而不是一次性堆 6 个;筛选阈值 / 带宽要按市值或其他维度分组重跑,报告子样本差异(参照 [S2])。**没有文献支持或反对**「筛选带宽接近持仓档位宽度时因子失效」这个我们自己的发现,也没有文献报告过「被筛掉那部分自己的收益」,这两条是真正的空白,PI 如果要在任务书里写这两条,应标注为「本种子自己的实测发现,无文献背书」。
- **L2 最可操作的一条**:§2.2 的否证(线性中性化查不出非线性重合)在文献里有扎实的一般性支持——Freyberger-Neuhierl-Weber [S7] 明确说线性方法系统性漏掉非线性冗余;流动性 / 成交量这一大类特征互相高度重合也有直接文献支持(Goyenko-Holden-Trzcinka [S11]、Lou-Shu 对 Amihud 的量价分解 [S12])。更正式的冗余检验(spanning test [S9]、double-selection LASSO [S8])存在,但工程上超出本轮剩余算力,**建议写进 notebook 作为"C05 之后值得补的定位工具",不写进本轮任务书**。
- **L3 的核心结论是"搜不到"**:成交量(或任何日内量)自身历史序列的偏度/峰度,学术文献里**没有**被当作横截面特征系统检验过;唯一能类比的是用高频收益构造的已实现偏度 [S14],它的"用细颗粒度摊薄极值"稳健化逻辑,在我们"日度序列偏度(只有 50 个观测)"这个更粗颗粒的构造上**不能直接套用**,反而提示这个构造对极值更敏感、风险更高,PI 如果要继续在 D 轴上挖(§5.3 的"备选 N"),这是一条要写进风险提示的空白,不是可以援引文献来背书的方向。
- **L4 的核心结论是"方向有间接支持,但构造层面要谨慎"**:系统性跳跃/波动风险的价格是负的 [S19],方向上支持"波动均匀的股票收益更高",但那是对**总量风险的敏感度**,不是个股自身的历史统计量,两者不能等同;而且 Barclay-Warner [S15] 提醒"成交最重的交易"不等于"推动价格最多的交易",§2.6 那个 head 用成交量加权挑最重的 10% 分钟,这个权重选择本身在文献里**没有被验证优于**用波动本身加权,如果 PI 想把这个方向写进 N 位,应该同时试一个"用 |收益| 而不是成交量" 当权重的平行版本,而不是只信任现有 head 的构造。
- **教材类来源的提醒(S1、S13)**:Bali-Engle-Murray 和 Grinold-Kahn 是方法论共识的旁证,不是期刊论文的实证证据,PI 引用它们时应该说"这是业界/教学标准做法",不要和 S2、S4、S7 这类期刊论文的具体实证数字放在同一个证据等级上。
