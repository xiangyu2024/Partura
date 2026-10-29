# 文献:种子 803,B 组,第 2 轮(文献员)

查的题目来自 `r2/analysis.md` §5 的 L1–L4。本轮四题换的是轴(不重复 r1 已问过的「日内高阶矩与不交易」「尾部统计量稳健化(日内估计量)」「条件分组与涨跌停」「顺序信息与成交钟」):
L1 对准核心 A ——一只股票**自己的已实现方差序列的形状**(不是水平)在截面上值钱吗;
L2 对准「换掉 `ts_skew` 这个部件」——对一条**取正值**的时间序列度量不对称,除了三阶矩偏度还有什么写法;
L3 对准核心 B ——日内**成交的时点**与**波动的时点**,以及两者之差,在截面上怎么处理;
L4 对准反复冒头的混淆——**给定市值之后的名义价格水平**。

只用这次工具(WebSearch / WebFetch)实际检索到、能确认首版日期早于 **2023-08-08** 的论文/工作论文/研究报告;拿不准日期的不用,在正文或出处表里如实写"搜不到"或"日期不确定,弃用"。下面每条处理方式后用 `[Sx]` 指向文末出处表;`verified: true` = 这次搜索结果或抓取页面上确实看到了标题、作者、年份、出处;本轮没有写 `false` 的条目,搜不到的直接说明,不列入出处表。

---

## L1 —— 对准核心 A:已实现方差**自身时间序列的形状**(不是水平),在截面上值不值钱

**能翻译成算子语言的处理方式:**

1. **把"波动率的波动率"当一个独立于波动率水平的风险暴露,而不是波动率水平的衍生品**。Baltussen, van Bekkum & van der Grient (2018, *JFQA*)用期权隐含波动率序列的滚动标准差("vol-of-vol")排序,高 vol-of-vol 组显著跑输低 vol-of-vol 组,**控制了规模、beta、以及隐含波动率水平本身之后依然显著**;高 vol-of-vol 股票同时偏度更正、峰度更高。Huang, Schlag, Shaliastovich & Thimme (2019, *JFQA*)用无模型的隐含 vol-of-vol 发现它和波动率水平(VIX)只是弱相关,两者作为联合定价的风险因子,价格符号都为负。**关键的方法差异要如实告诉 PI**:这两篇的 vol-of-vol 都是**原始标准差**,不是仿射不变量,所以它们必须显式把波动率水平放进同一个回归里当控制项,才能证明"形状之外还有信息"——这和我们 `ts_skew` 天生仿射不变(构造上就躲开水平控制)不是同一个防御机制;我们的核心 A 在这一点上比文献里的标准做法更"干净",但也意味着文献的"控制了水平后依然显著"这条结论**不能直接当成"任何形状统计量都自动过关"的证据**,因为它们的构造本身没有做仿射不变这一步。[S21][S22]
2. **原始滚动偏度对未来偏度的预测力很弱,所以要先拟合"预期偏度"而不是直接用上一期的滚动值**。Boyer, Mitton & Vorkink (2010, *Review of Financial Studies*)发现"用滞后的已实现偏度预测下一期偏度"本身效果很差,于是改用一个截面回归模型(拿换手率、规模、账面市值等去拟合"预期特质偏度"),用拟合值而不是原始滚动值去排序,预期偏度与收益显著负相关,且能部分解释特质波动率异象。→ 提醒:若 E/R 要长期依赖 `ts_skew(day_durbin_watson(Open), 50)` 这类原始滚动统计量,文献的经验是**这类统计量自相关很弱**,核心卡里"50 日窗口"这个选择本身可能需要一个"拟合/平滑"的版本才稳定,而不是直接相信原始滚动值,这点值得写进第 3 轮的核对清单。[S23]
3. **把已实现方差按正负收益拆成上行/下行两个半方差,再做差(不是做比),该差值在控制了几乎全部已知截面变量后依然显著**。Bollerslev, Li & Zhao (2020, *JFQA*)用日内 5 分钟收益把每日已实现方差拆成 `RV+`(正收益贡献)和 `RV-`(负收益贡献),用 `RV- − RV+`("坏波动减好波动")做月度排序,在控制规模、账面市值、动量、流动性、特质波动率水平等一长串变量后依然显著。**要如实指出的差异**:文献用的是**差**,不是我们 R12 想测的**比**(`cross_semistd_pos/cross_semistd_neg`);这给"上下行不对称值钱"这个方向提供了扎实先例,但没有给出"比值这种尺度无关写法"同样有效的直接证据,比值版本是我们自己在文献思路上做的延伸,不是照搬。[S24]
4. **跳跃风险(而非跳跃频率本身)的代理来自期权隐含波动率斜率,不是从日频收益序列里直接数"爆波动日"**。Yan (2011, *JFE*)用期权隐含波动率曲面的斜率代理"平均跳跃幅度",斜率越陡(隐含跳跃风险越大)未来收益越低,这条关系控制规模、账面市值、杠杆、波动率、偏度、成交量后仍然存在。**这条文献搬不进我们的算子库**:我们没有期权数据,无法复刻"隐含波动率斜率"这个具体构造,只能借用它的结论方向(跳跃/爆波动类的风险代理,在控制了一长串标准变量后往往还剩得下东西),不能当作"某个具体算子"的直接先例。[S25]

**搜不到 / 弃用的部分**:没有找到任何论文直接对"一只股票自己的已实现方差(或已实现方差的某个日频代理,如 `day_var(Ret)`、`day_durbin_watson(Open)`)**滚动窗口内的三阶矩偏度**"做过截面选股检验——上面四篇分别检验的是"隐含波动率的波动率"(期权)、"收益本身的偏度"(不是方差的偏度)、"上下行半方差的差"(不是形状统计量)、"期权隐含的跳跃斜率",**没有一篇是我们核心 A 的精确对应物**。这件事本身要写进 notebook:核心 A 如果真的有效,我们可能是在做文献没有直接做过的构造,不是在复刻一个已知异象,这和 r1/lit.md 对 N-A(`day_hurst`)的提醒是同一类情况。

---

## L2 —— 对准「换掉 `ts_skew` 这个部件」:正值序列的不对称,三阶矩偏度之外还有什么写法,各自修什么

**能翻译成算子语言的处理方式:**

1. **用分位数构造偏度,而不是三阶矩**:Kim & White (2004, *Finance Research Letters*)系统比较了基于四分位的 Bowley 型偏度 `(Q3+Q1−2Q2)/(Q3−Q1)` 和基于八分位的变体,与标准的三阶矩偏度/四阶矩峰度在模拟和 S&P 500 实证中的表现;核心结论是**标准矩估计量极容易被单个极端观测值支配、且短窗口下方差很大**,分位数版本对两者都明显更稳健。→ 直接对应 §4.2 第 11–13 条"换部件"的方向:把 `ts_skew(day_durbin_watson(Open), 50)` 换成基于滚动分位数的 Bowley 型构造,修的正是"单点支配"和"短窗口噪声",这与我们怀疑的"50 日窗口到底够不够"是同一个问题的文献先例。[S26]
2. **分位数偏度可以用一个参数 α 推广(Hinkley 型),Bowley 是 α=0.25 的特例**:Groeneveld & Meeden (1984, *The Statistician*)给出通用形式 `g_p = s_p / r_1,p`(分位间偏度之差除以分位间距),α 越小越接近三阶矩偏度(效率高、稳健性差),α 越大越稳健但越粗糙。**没有找到**任何文献给出"在金融时间序列的滚动窗口场景下,α 该怎么选"的具体指导——这是个纯统计学问题,没人在我们这个应用场景(50 日滚动窗口、再做截面排序)里专门调过。[S27]
3. **纠正一个任务题目里可能的混淆:变异系数(CV = σ/μ)不是不对称度量,它是离散度量**。多条检索结果一致指出 CV 衡量的是相对于均值的分散程度,且**均值接近 0 时会发散**(我们 `day_durbin_watson(Open)`、`day_var(Ret)` 这类正值序列如果某些窗口均值很小,CV 会不稳定);度量不对称仍然要用偏度本身(矩或分位数版本),CV 和偏度是两个不同维度的量。**这点要明确写给 PI**:analysis.md §4.2 把"变异系数"和"偏度"并列成"另一种不对称写法"是不准确的,CV 换不掉 `ts_skew`,它和 `ts_skew` 是互补的两个维度,不是替代关系。[无独立可引用的单一论文支撑这条,是多个二级来源的一致陈述,按规矩不列入出处表,只作为方法论提醒]
4. **先取对数再算偏度,还是直接对正值序列算偏度,两者在截面选股任务上的直接对比,以及"超过 k 倍中位数的天数占比"这种写法——都搜不到**。没有找到任何论文把"对数变换后偏度"与"原始偏度"在金融时间序列上做过直接的实证对比(多数稳健统计文献只在模拟分布上比较,不是在已实现方差这类实证序列上);也没有找到用"超过某倍中位数的天数占比"衡量不对称并在截面选股任务上检验的文献。这两条按规矩弃用,不编造。

**搜不到的部分(任务级别)**:和 r1/lit.md L2 的结论一致,**没有任何文献把"裸偏度 vs 分位数偏度 vs 尾均值比 vs 半偏差比"在截面选股(而不是分布拟合/风险度量)任务上做过直接横向比较**——这些稳健化写法全部是统计学/风险管理的工具,被"借用"到选股场景是我们自己的延伸,文献只能提供"它们各自修什么"的证据,不能提供"哪个在选股上更好"的证据。

---

## L3 —— 对准核心 B:日内**成交的时点**与**波动的时点**,以及两者之差,在截面上怎么处理

**能翻译成算子语言的处理方式:**

1. **按固定的日内时间段(如半小时)切块,检验某只股票"自己在某个时段的历史表现"能不能预测"自己未来同一时段的表现"**:Heston, Korajczyk & Sadka (2010, *Journal of Finance*)发现个股收益在"恰好相隔整数个交易日"的同一时间段上有显著的正自相关,持续约 40 个交易日;成交量和委托不平衡也呈现类似的周期模式,但**这两者本身解释不了收益的周期模式**;规模、系统性风险溢价、是否入选 S&P 500 都不是驱动因素。**要如实指出翻译上的落差**:这篇测的是"同一时段、跨天"的收益自相关,构造粒度是半小时分段 × 多天,不是我们 `day_centroid(Amt)` 这种"一天一个数"的截面统计量;它不能直接当作"成交时点本身当截面因子"的先例,只能提供一个背景事实——成交量的日内分布模式本身**不足以解释**收益的日内模式,这对我们"时点错位"的核心假设既不是正面证据也不是反面证据,是一条独立的提醒。[S28]
2. **日内 U 型成交/波动模式下,开盘段收益能预测收盘段收益,机制归因于知情交易者选择开收盘高流动性时段下单**:Gao, Han, Li & Zhou (2018, *JFE*)在 S&P 500 ETF 等指数/ETF 层面的高频数据上发现"头半小时收益预测尾半小时收益",并把机制归因为知情交易者偏好在开盘和收盘这两个高成交量时段交易。**同样的翻译落差要指出**:这是**指数/ETF 层面**的证据,不是个股截面证据,"知情交易者的时点选择"这个机制本身支持我们"成交时点里有信息"的大方向,但论文没有测试、也不能直接证明"把成交时点本身做成一个个股截面因子"这件事本身有效。[S29]
3. **中国收盘集合竞价改革(2018-08-20,沪市)作为自然实验,一致发现成交量从"收盘那一刻"迁移到"收盘前几分钟",而不是简单消失**:Ma, Wang, Fang & Wang (2020/2021, *China Finance Review International*)用改革前后的面板数据发现流动性、波动率、价格连续性均改善,且交易者在尾盘连续竞价阶段交易更积极;Han 等 (2022, *Pacific-Basin Finance Journal*)用双重差分法重新检验,发现**对整体流动性没有显著影响**,但确认了"成交量从收盘迁移到收盘前"这一效应,尾盘波动率上升,且**对小盘股的影响更明显**,价格连续性有改善。→ 这直接支持 §4.2 第 8 条(R8:砍掉最后 10 分钟)的设计思路,但给出一个更精细的提醒:**文献里"迁移"的时间窗口是"收盘前几分钟"这个模糊区间,不是单指集合竞价那一笔**,所以 R8 砍掉最后 10 分钟这个具体窗口长度本身是我们自己的选择,文献没有给出"恰好 10 分钟"这个数字的先例;另外 Han 等按市值分组发现效应对小盘股更明显,这给"核心 B 的外围按市值分组"提供了一个独立的文献动机(不只是 §4.0 关于 SEEN 的工程考虑),与 §4.1② 建议的"按板块/价格分组"是同一方向的另一条支撑。[S30][S31]

**搜不到 / 弃用的部分**:没有找到任何文献直接构造"成交量重心"或"波动重心"这类单日一个数的时点统计量、并把它(或两者之差)当个股截面因子检验过——这是英文和中文检索都没有命中的空白,现有文献全部落在"日内收益/成交量的周期性模式"或"指数层面的日内动量"上,不是"把时点本身当个股选股因子"。也没有找到专门测"成交时点领先/滞后波动时点"这种两个时点之差的度量,这条和核心 B 的 N-B 候选(§4.3)一样,**是文献没做过的事,不是复刻已知异象**。

---

## L4 —— 对准反复冒头的混淆:给定市值之后的**名义价格水平**

**能翻译成算子语言的处理方式:**

1. **名义价格的截面信息量是时变的,源于投资者对"低价股"的偏好本身随时间变化,管理层据此选择拆股/定价**:Baker, Greenwood & Wurgler (2009, *Journal of Finance*)的"迎合"框架里,用低价股的估值溢价和拆股公告效应构造一个时间序列指数,衡量某个时期投资者对低价股的偏好强弱,管理层据此选择名义价格水平。**提醒**:这不是一个截面因子构造,而是提醒我们"名义价格给的信号强度本身可能随时间漂移",对应我们只能在 train/valid(2018–2023)这一段里检验 §1.4 的代理判定,文献本身支持"不要假设这个效应在任何时段都一样强"这条谨慎态度。[S32]
2. **控制了规模、账面市值、流动性、信息扩散之后,"价格相近的股票"收益仍然联动,是直接支持"名义价格净于市值后仍是独立效应"最扎实的一条**:Green & Hwang (2009, *JFE*)发现拆股后的股票会和低价股组合的联动增强、与高价股组合的联动减弱,这种"按价格分类"的联动**不能用基本面、规模、流动性或信息扩散的变化解释**,在控制了市场、行业、规模、账面市值、交易成本、动量等组合后依然存在。处理方式:**直接按名义价格水平分桶**(不做任何标准化),检验分桶组合收益对个股收益的解释力,同时控制一组标准因子组合。[S33]
3. **但同一个发现在更稳健的检验设计下大部分消失,主要被动量吸收**:Chen, Singal & Whitelaw (2016, *JFE*)重新检验 Green & Hwang 式的双变量回归,换成稳健单变量回归 + 匹配对照样本后,**几乎全部的"超额联动"证据消失**,他们把残余部分主要归因于动量(赢家股票的 beta 本身会上升,制造出联动的假象)。**这是本题最重要的一条方法论警告,要明确写给 PI**:若 §4.2 第 10 条 `sub(LogFloatCap, LogFloatShares)` 真的测出某个分数,在第 3 轮解读时**必须先排除动量**(我们的控制基里已经有 20 日反转,但 Chen 等人用的是标准动量窗口,不完全是同一个东西),否则很可能是在重新发现"动量混进了价格分桶"这个文献已经证明过的假象,不是发现了真的价格效应。[S34]
4. **名义价格本身和过去收益历史机械相关(价格 = 历史复利收益的函数),裸价格排序天然被这条机械关系污染,文献的解法是改用"名义计价的基本面"而不是裸价格**:Birru & Wang (2016, "The Nominal Price Premium")指出对原始价格做排序,其选出来的低价股本身就是"历史上跌得多的股票",这会系统性压低对价格溢价的估计;他们改用每股账面价值、每股盈余、每股股息这类**名义计价的基本面变量**来规避这条机械关系。**这条翻译不过来,要如实说明**:我们允许的 6 个日频叶子里没有任何"每股基本面"类字段(没有账面价值、盈余、股息),`sub(LogFloatCap, LogFloatShares)` 恰恰就是文献警告的那种"裸价格"构造,没有办法用我们现有的算子库规避这条机械关系,这是一个真实的构造局限,不是能靠换算子解决的问题。[S35]
5. **相对最小报价单位(tick/价格)本身是一个由风险、规模、可见度共同决定的内生选择,拆股的目的之一就是把它维持在某个目标区间**:Angel (1997, *Journal of Finance*)的模型把最优相对 tick 和特质风险、规模、可见度连起来,公司拆股是为了让 tick/价格比维持在某个区间。**相对 tick 大小本身还会改变流动性提供者之间的竞争方式**:Chen Yao & Mao Ye (2018, *Review of Financial Studies*)用杠杆 ETF 拆股当作相对 tick 的外生冲击,发现相对 tick 变大后,高频交易者凭速度(而不是报价竞争)占据流动性提供的主导地位,整体流动性反而可能下降——这与"tick 越大流动性越好"的朴素直觉相反。→ 这两篇合起来说明:按名义价格分组看到的任何差异,有一部分可能来自**微结构层面的、与"错误定价"无关的机制**(谁在提供流动性、以什么方式竞争),这是按名义价格分组时必须考虑的另一类混淆,和 Chen 等人讲的"动量混淆"是性质不同的另一条警告。[S36][S38]
6. **价格离散(报价网格)导致的方差/序列协方差偏差,大小取决于波动率水平**和买卖价差,不是价格水平本身的单调函数,文献给出的是参数化修正公式,不是"按价格分组"**:Harris (1990, *JFQA*)证明价格离散会像噪声一样系统性抬高测得的方差、产生负的序列协方差,偏差大小同时取决于真实波动率水平和买卖价差的大小;他给出了可以直接修正标准方差/协方差估计量的近似公式。**要如实指出我们的局限**:文献给的"正确"解法是用价差信息去修正估计量本身,我们 6 个允许的日频叶子里没有买卖价差,无法复刻这条修正;§4.2 第 10 条用"按名义价格分组再看组内"是一个更粗糙的非参数替代品,Harris 的发现(偏差同时依赖价差)意味着**单按名义价格分组不能把离散偏差完全分离出来**,分组后组内仍可能残留一部分由价差差异带来的偏差,这点要写进第 3 轮对 §4.2 第 10 条结果的解读里。[S37]

**搜不到 / 弃用的部分**:没有找到任何专门针对**中国 A 股**的"名义价格效应 / 控制市值后的名义价格 / 相对 tick 作为流动性代理"研究(检索到的全部是美国市场);也没有找到任何论文直接报告"按名义价格分组后,日内波动类因子(偏度、方差比等)的表现差异"——这正是 §4.2 第 10 条和 N-A 要去填的空白,不是复刻已有结论。

---

## 出处(按正文出现顺序编号,`verified` 均为本次搜索/抓取中实际看到;本轮续用 r1 的编号起点,从 [S21] 开始)

[S21] Guido Baltussen, Sjoerd van Bekkum, Bart van der Grient. 2018. "Unknown Unknowns: Uncertainty About Risk and Stock Returns." *Journal of Financial and Quantitative Analysis*, 53(4), 1–37. DOI 10.1017/S0022109018000480。ERIM 记录:https://erim.eur.nl/people/guido-baltussen 。verified: true

[S22] Darien Huang, Christian Schlag, Ivan Shaliastovich, Julian Thimme. 2019(工作论文 SAFE WP No. 210,2018-05). "Volatility-of-Volatility Risk." *Journal of Financial and Quantitative Analysis*, 54(6), 2423–2452. IDEAS 记录:https://ideas.repec.org/a/cup/jfinqa/v54y2019i6p2423-2452_5.html ;工作论文:https://publikationen.ub.uni-frankfurt.de/files/46676/SSRN-id3183610.pdf 。verified: true

[S23] Brian J. Boyer, Todd Mitton, Keith Vorkink. 2010(在线提前出版约 2009). "Expected Idiosyncratic Skewness." *Review of Financial Studies*, 23(1), 169–202. BYU ScholarsArchive:https://scholarsarchive.byu.edu/facpub/8929 ;SSRN:https://papers.ssrn.com/abstract=1541002 。verified: true

[S24] Tim Bollerslev, Sophia Zhengzi Li, Bingzhi Zhao. 2020. "Good Volatility, Bad Volatility, and the Cross Section of Stock Returns." *Journal of Financial and Quantitative Analysis*, 55(3), 751–781. IDEAS 记录:https://ideas.repec.org/a/cup/jfinqa/v55y2020i3p751-781_2.html 。verified: true

[S25] Shu Yan. 2011. "Jump Risk, Stock Returns, and Slope of Implied Volatility Smile." *Journal of Financial Economics*, 99(1), 216–233. DOI 10.1016/j.jfineco.2010.08.011。摘要来源:https://academicnewsletter.sufe.edu.cn/info/356921 。verified: true

[S26] Tae-Hwan Kim, Halbert White. 2004-03. "On More Robust Estimation of Skewness and Kurtosis." *Finance Research Letters*, 1(1), 56–73. IDEAS 记录:https://ideas.repec.org/a/eee/finlet/v1y2004i1p56-73.html 。verified: true

[S27] Richard A. Groeneveld, Glen Meeden. 1984. "Measuring Skewness and Kurtosis." *The Statistician*, 33(4), 391–399. 二级来源确认(UMN 研究库记录、多篇引用文献一致给出卷期页码):https://experts.umn.edu/en/publications/measures-of-skewness/ 。verified: true

[S28] Steven L. Heston, Robert A. Korajczyk, Ronnie Sadka. 2010. "Intraday Patterns in the Cross-Section of Stock Returns." *Journal of Finance*, 65(4), 1369–1407. arXiv 预印本(2010 之前已流通):https://ar5iv.arxiv.org/html/1005.3535 ;Kellogg 摘要:https://www.kellogg.northwestern.edu/academics-research/research/detail/2010/intraday-patterns-in-the-cross-section-of-stock-returns/?p=1 。verified: true

[S29] Lei Gao, Yufeng Han, Sophia Zhengzi Li, Guofu Zhou. 2018. "Market Intraday Momentum." *Journal of Financial Economics*, 129(2), 394–414. 摘要/二级来源确认:https://profiles.wustl.edu/en/publications/market-intraday-momentum/ 。verified: true

[S30] Dan Ma, Chunfeng Wang, Zhenming Fang, Ziwei Wang. 在线 2020-08-18,正式出版 2021. "The Impact of Closing Mechanism Changes: Evidence from the Shanghai Stock Market." *China Finance Review International*, 11(2), 259–281. DOI 对应记录:https://ideas.repec.org/a/eme/cfripp/cfri-04-2020-0041.html ;Emerald:https://emerald.com/insight/content/doi/10.1108/CFRI-04-2020-0041/full/html 。verified: true

[S31] Han 等(具体全部作者姓名本次未逐一核实,检索结果给出至少 Han、Zhao、Chen、Guo 四位). 2022. "Reexamining the Impact of Closing Call Auction on Market Quality: A Natural Experiment from the Shanghai Stock Exchange." *Pacific-Basin Finance Journal*, 74, 101821. IDEAS 记录:https://ideas.repec.org/a/eee/pacfin/v74y2022ics0927538x22001160.html 。verified: true(标题、期刊、卷期、年份确认;完整作者名单未逐一核实,引用时需二次核对)

[S32] Malcolm Baker, Robin Greenwood, Jeffrey Wurgler. 2009(NBER WP 13762,2008-01). "Catering through Nominal Share Prices." *Journal of Finance*, 64(6), 2559–2590. DOI 10.1111/j.1540-6261.2009.01511.x。NBER:https://www.nber.org/system/files/working_papers/w13762/w13762.pdf 。verified: true

[S33] T. Clifton Green, Byoung-Hyoun Hwang. 2009-07. "Price-Based Return Comovement." *Journal of Financial Economics*, 93(1), 37–50. DOI 10.1016/j.jfineco.2008.09.002。IDEAS 记录:https://ideas.repec.org/a/eee/jfinec/v93y2009i1p37-50.html 。verified: true

[S34] Honghui Chen, Vijay Singal, Robert F. Whitelaw. 2016. "Comovement Revisited." *Journal of Financial Economics*, 121(3), 624–644. IDEAS 记录:https://ideas.repec.org/a/eee/jfinec/v121y2016i3p624-644.html 。verified: true

[S35] Justin Birru, Baolian Wang. 2016-03(工作论文;正式期刊出处本次未核实). "The Nominal Price Premium." 二级来源(Larry Swedroe/ETF.com 专栏摘述):https://www.etf.com/sections/index-investor-corner/swedroe-low-priced-stocks-no-bargain 。verified: true(标题、作者、核心发现经二级来源确认;未直接抓取论文原文或确认最终发表期刊,引用时需二次核实)

[S36] James J. Angel. 1997. "Tick Size, Share Prices, and Stock Splits." *Journal of Finance*, 52(2), 655–681. IDEAS 记录:https://ideas.repec.org/a/bla/jfinan/v52y1997i2p655-81.html 。verified: true

[S37] Lawrence Harris. 1990. "Estimation of Stock Price Variances and Serial Covariances from Discrete Observations." *Journal of Financial and Quantitative Analysis*, 25(3), 291–306. IDEAS 记录:https://ideas.repec.org/a/cup/jfinqa/v25y1990i03p291-306_00.html 。verified: true

[S38] Chen Yao, Mao Ye. 2018. "Why Trading Speed Matters: A Tale of Queue Rationing under Price Controls." *Review of Financial Studies*, 31(6), 2157–2183. DOI 10.1093/rfs/hhy002。IDEAS 记录:https://ideas.repec.org/a/oup/rfinst/v31y2018i6p2157-2183..html 。verified: true

---

## 给 PI 的汇总提醒

- **L1**:四篇(vol-of-vol [S21][S22]、预期偏度 [S23]、上下行半方差差 [S24]、跳跃斜率代理 [S25])都支持"波动率/收益的形状类统计量,在控制了水平和一长串标准变量后往往还剩得下东西"这个大方向,但**没有一篇是核心 A 的精确对应物**(已实现方差自身滚动窗口的三阶矩偏度),核心 A 若真出 head,是在填一个文献空白,不是复刻已知异象。另外 [S23] 给出一条具体可核查的预测:原始滚动偏度的自相关文献证据很弱,这可能是核心 A 后续稳定性的一个风险点,建议第 3 轮关注。
- **L2**:最直接可翻译成算子的是 Kim & White 的分位数偏度 [S26],修的是"单点支配"和"短窗口噪声",正对应 §4.2 第 11–13 条的方向;**变异系数不是偏度的替代品**这条纠正请务必带给 PI,analysis.md §4.2 原文把两者并列是不准确的。窗口参数(分位数的 α、是否先取对数)文献没有金融场景下的具体指导,这两条按规矩标记为搜不到。
- **L3**:三篇([S28][S29]可信但只在时间段模式/指数层面,[S30][S31]是扎实的中国收盘集合竞价证据)合起来支持"收盘前成交迁移"这个机制性事实,直接给 R8(砍最后 10 分钟)一个文献背景,但**没有一篇把"成交时点本身"当个股截面因子检验过**——"成交重心"和"两个时点之差"这两个具体构造,英文中文检索都是空白,这和 N-A(Hurst)、L1 核心 A 是同一类"我们在做文献没做过的事"的情况。[S31] 额外给出"效应对小盘股更明显"这条,支持按市值分组看核心 B 外围的动机。
- **L4**:这题最重要的产出不是正面支持,是**两条方法论警告**——(a) [S34] 证明 Green-Hwang 式的裸价格联动证据在更稳健的设计下大部分会被动量吃掉,§4.2 第 10 条的结果解读必须先排除动量,不能直接当成价格效应;(b) [S35][S36][S38] 合起来说明裸价格排序同时被"历史收益的机械关系"和"相对 tick 驱动的微结构效应"两条通道污染,而我们的叶子集合里**没有办法规避任何一条**(没有基本面叶子、没有价差数据),§4.2 第 10 条这个测试的结果无论正负,都建议在 notebook 里标注"存在至少两条已知混淆通道,本测试无法单独排除"。
- 全部 18 条新出处(S21–S38)里,没有一条是编造的;唯一需要二次核实的两处已在 [S31](完整作者名单)和 [S35](最终发表期刊)的备注里标出。
