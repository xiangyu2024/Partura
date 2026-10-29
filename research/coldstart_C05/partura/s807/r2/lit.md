# 文献笔记 — s807 / r2(文献员)

范围:只用 **2023-08-08 之前发表**的论文 / 工作论文 / 研究报告(arXiv、SSRN、机构工作论文系列以首版日期为准)。对 analysis.md §5 的 L1–L4 四个题目逐一检索;每条「处理方式」后标出处编号,对应文末〈参考文献〉。搜不到的地方明确写「搜不到」,不补全、不猜测。工具:WebSearch(多轮)+ WebFetch(对关键页面核实);WebFetch 对付费墙 PDF(SSRN/Cambridge)多次返回 403 或只读到压缩流,这类情况在正文和参考文献里都标明「未读到全文,只核实到二次转述/元数据」。

---

## L1 — 日内已实现方差 / 极差型(high-low)波动估计量(对准核心 ②:`day_durbin_watson(High)` ≈ 分钟高价序列的每分钟已实现方差)

**能翻译成算子语言的处理方式:**

1. **分母 / 构造的选择:三条经典估计量用的是同一个"用极值信息代替全部路径"的思路,但具体怎么用差异很大。** Parkinson [1] 只用当日 High、Low 两点,`Var ∝ (ln(High/Low))²`,显式假设零漂移、无隔夜跳空;Garman–Klass [2] 在此基础上加入 Open、Close 四个点,相对收盘价估计量效率提升(二次转述给出的数字是约 7.4 倍,**这个具体倍数我没有在原文里核实到,只在交易平台文档里反复看到同一个数字,标 verified:false 的部分**);Rogers–Satchell [3] 去掉零漂移假设,专门为有趋势的价格序列设计,代价是对真实极值的逼近误差(论文摘要自己承认这一点)更大。
   **翻译过来:** 我们现在的核心 `day_durbin_watson(High)` 既不是 Parkinson 的 `ln(High/Low)` 也不是 GK 的四点组合,而是分钟级 High 序列自身的增量平方和除以水平平方和(`Σ(ΔHigh)²/ΣHigh²`),是"尺度无关的日内抖动",不是"极差"。**这件事本身文献里没有现成对照** —— 经典三个估计量全部依赖 Open/High/Low/Close 四个日内定点,没有一个是"整条分钟序列的自相关结构"这个思路;如果要往文献靠,更接近的操作是把 `High` 换成**真正的日度 High/Low 两点算 Parkinson 式极差**,或者在外围里显式加一条 `pow_2(cross_mean(cross_log(day_high(High), day_low(Low)), N))`(窗口化的 Parkinson)做空对照,把"DW 式序列抖动"和"经典极差"分开比较。

2. **只用 High 还是 High 与 Low 都用,文献里是"都要用、而且角色不对称":** Rogers–Satchell [3] 的估计量显式包含 High 与 Low 两个量,且在推导里两者不是对称项(与 Close 的关系不同)。我们的拆解结果(换字段 `High→Low` 仍有效,1.5391)和文献的提示方向一致:**上行抖动和下行抖动不是同一个东西,但文献没有告诉我们"相减"还是"相除"更好** —— 这正是 analysis.md §4.1 核心②条目里"上下行抖动的不对称(`DW(High)` 与 `DW(Low)` 的差或比)"这条外围方向,目前**没有查到**直接支持或反对它的论文,算是空白,不是被证伪。

3. **日度量聚合成月度截面信号:均值聚合与极值聚合是两条已知会互相替代归因的路线,但测的是"日度方差水平",不是"日度抖动水平"。** Ang–Hodrick–Xing–Zhang [4] 把日度残差方差在月内**求均值**(本质是 IVOL 路线);Bali–Cakici–Whitelaw [9] 把同一类日度量换成**月内取最大值**(MAX 路线),发现两条路线在美股上会互相吸收/反转。**翻译过来:** `day_durbin_watson(High)` 的两种有效聚合——`cross_stddev(·, 60)`(偏向离散度)和 `pow_3 + EMA`(偏向极端日,见 L2)——分别对应文献里"方差聚合"与"极值聚合"这两条已知会互相替代的路线,但**文献测的日度量本身是方差/收益**,没有人把"DW 这种自身已经是尺度无关的抖动量"拿去做同样的均值 vs 极值聚合对比,这件事**搜不到**,是我们在做文献没做过的组合。

4. **控制掉平均波动之后还剩什么:有直接证据,但方向是"不对称下行风险被定价",不是"抖动被定价"。** Bollerslev–Patton–Quaedvlieg [6](实现"半贝塔")发现:负向市场协同负向个股("坏-坏"半协方差)显著正向预测收益,其余符号组合不显著或方向相反;这是在控制了普通协方差之后,**符号拆分**还剩下的定价能力。Bollerslev–Li–Patton–Quaedvlieg [7] 在方差预测(不是收益横截面)里证明同一套符号拆分能显著提升预测力。**翻译过来:** 这条文献支持的是"把 `day_durbin_watson` 的增量按正负号拆开再分别聚合"这个方向(类似 realized semivariance 的做法),而不是支持"抖动的绝对水平"本身;**我没有查到**任何文献直接检验"日内抖动的绝对水平,在控制了日度波动均值之后,还能不能独立预测收益"——这正是我们核心②最大的风险点(analysis.md §4.1 自己也提示了),文献既不支持也不反对,**完全空白**。

5. **A 股特有的条件化:有涨跌停统计本身的文献,但没有把它和已实现方差/极差估计量连起来的文献。** Wan et al. [24](2015,PLoS ONE,2000–2011 年沪深 A 股高频数据)系统统计了涨跌停触及的概率、触及前的日内动态,确认涨跌停是一个会机械压缩当日 High/Low range 的事件(涨停板附近 High ≈ Low ≈ 涨停价,极差估计量会被人为压平)。**翻译过来:** 外围该往哪条件化(analysis.md 已经提了"贴近板宽日"),文献支持这个方向的**机制**(涨跌停会压缩极差),但**没有查到**把这个机制显式用在"已实现方差类估计量按涨跌停幅度 / `LimitWidth` 重新标度"上的论文——L2 的 Hung–Yang [11] 把这个标度方法用在 MAX(单日收益)上,**没有查到**有人把同一招搬到日内极差 / 已实现方差类估计量上,这是一个可以直接抄 Hung–Yang 方法论、但文献本身还没做的空档。
   另外,按流动性 / 规模 / 上市年限分组这类条件化,**没有查到**专门对已实现方差 / 极差估计量做的 A 股分组研究(搜了多轮关键词组合,只搜到泛泛的"流动性与波动共动"综述级描述,没有可核实的具体分组结果)。

6. **中国 A 股的低波动 / IVOL 异象本身是存在的,但结论依赖方法,给核心②的风险定级提供背景。** Chen & Ye [14](2021,*Discrete Dynamics in Nature and Society*)用正式的横截面检验确认 IVOL 溢价之谜在中国 A 股稳健存在,并把解释归到卖空限制;一份资管研究(Robeco,非同行评审,**仅作背景线索、不作为学术证据**)也报告中国"低波动"效应主要来自波动本身而非 beta。**翻译过来:** 这给了核心② R2(`pow_2_5(pow_3(day_std(Ret)))` 空对照)一个明确的先验方向——如果空对照接近核心②本身的分数,说明我们挖到的就是这条已经被学界确认、而不是新发现的异象,analysis.md §1.5 自己的怀疑是对的。

**小结(给 PI 的可用结论):** 经典极差估计量(Parkinson/GK/RS)全部基于日度定点(OHLC),和我们"分钟序列自相关结构"的 DW 核心在构造上不是同一类东西,没有直接文献对照,这既是风险(没有先验可用)也是机会(文献没做过)。符号拆分(正负半方差/半协方差)有扎实文献支持其独立定价能力,是外围值得长的方向;"抖动的绝对水平独立于均值波动"这件事文献完全没有检验过,是真空白;A 股涨跌停会机械压缩极差类估计量,这一机制有文献支持,但"按板宽重新标度已实现方差类核心"这个具体操作没人做过,可以直接把 Hung–Yang 的方法论类比过来当新想法用。

---

## L2 — 同一日度量换聚合方式(对准来源 ①:非负日度量的"凸幂 + 指数加权"聚合,等价于偏向极端日的软幂平均)

**能翻译成算子语言的处理方式:**

1. **"均值聚合 vs 极值聚合"是文献里明确比较过的两条路线,而且已经比较到"软聚合"这一层。** Bali–Cakici–Whitelaw [9] 把 MAX 定义成月内**单日最大收益**(硬极值),但论文自己同时测试过 MAX 定义成**前 2~5 个最大收益的均值**这种软化版本,结论一致稳健(高 MAX 组后续跑输)。**翻译过来:** 这条直接对应我们"硬极值(`cross_max`)输给软幂平均(`pow_2(pow_2(...))` + EMA)"这个本轮最大的发现(R5、R6)——文献里软化 MAX(取前 k 大均值)相对单一最大值**没有降低显著性**,这给了"软聚合优于硬极值"一个方向上的背书,但**文献比较的是"前 k 大均值"这种软化,不是我们"凸幂再做指数加权移动平均"这种连续化的软聚合**,后者**没有查到**直接对照,是我们组合出的、文献没测过的具体形式。

2. **凸变换(平方、立方)再做时间平均,文献里有大量"用方差 / 二阶矩"的先例,但"系统性比较幂次高低"是空白。** Ang–Hodrick–Xing–Zhang [4] 的 IVOL 就是日度残差"平方后求均值",是 `p=2` 情形;再往上到 `p=3、p=7.5` 这种高阶凸幂,**没有查到**任何资产定价文献系统比较过"同一个日度量,换不同的凸幂次(2 次、3 次、更高)再聚合,收益预测力怎么变"。这正好对应 analysis.md §4.1 核心①的提醒("根上再加任何单调包装在 hl=0 下是空操作")和 R6 的幂次扫描(train 在 p≈6 见顶、valid 从 p=2 起就不升)——**文献没有告诉我们这条阶梯该停在哪一级,这件事本质上是我们自己在做超参数扫描,不是复现文献,R7 的"先平滑再凸化"这个顺序选择在文献里也没有先例**,是空白。

3. **指数加权(EMA)相对硬聚合窗口的代价(换手率、信号衰减),文献里讨论的是权衡,没有具体数字可抄。** 我没有查到专门针对"日度风险/活动指标的月度聚合"比较 EMA vs 简单滚动均值 vs 硬极值在换手率和净收益上的论文;能查到的是更一般的信号衰减讨论(把当期信号和滞后信号按衰减因子混合,可以降低换手率,但 IC 会随衰减因子增大而衰减向零,存在一个中间最优点)——**这条不是专门针对我们这类风险/活动指标的研究,只是信号处理的一般结论,不能直接当成"EMA 聚合在这里最优"的证据,标成背景参考,不是直接支持**。
   翻译过来:核心①里"根上已经含一个 `pow_2`,hl>0 时只是 EMA 加权"这条诊断(analysis.md 已经自己发现),和这条背景结论一致——**EMA 本质是信号平滑/去噪,不是新的信息来源**,这进一步支持 PI 把"96 次评估花在幂次阶梯上"标成浪费。

4. **A 股的 MAX 效应是真实存在的,但被涨跌停"削平"过,需要重新标度,这条有扎实的方法论可以直接套用。** Nartea–Kong–Wu [10](2017,A 股个股横截面)确认 MAX 效应在中国存在,且**不**像美股那样吸收/反转 IVOL——两者独立共存。Hung–Yang [11](2018)指出原始 MAX 定义在有涨跌停的市场里会被板子压成同质化的极值,于是**把 MAX 按涨跌停幅度重新标度**后再检验,发现修正后的 MAX 依然显著、且不是 IVOL 的另一种表现。Yao–Wang–Fang–Chiao [12](2021,*International Review of Economics & Finance*,专门研究中国涨跌停对 MAX 的干扰;**我核实到了标题、期刊、卷期页码,但没有核实到摘要本身的具体结论数字,它的论文题目本身已经说明论点方向——涨跌停会让 MAX 的测量失真——但具体怎么失真、修正后系数多大,本次检索没能拿到全文,标 verified:true 仅限于"论文存在、期刊信息、方向性标题",结论细节 verified:false**)。Hoang Van Hai [13](2023,*Cogent Economics & Finance*,我只核实到摘要的第一句"研究中国股市 MAX 与彩票型股票的关联",没有拿到具体结论,同样标注结论细节未核实)。
   **翻译过来:** 这是一条**可以直接套用的方法论**——核心①的外围如果要往"幅度在不同板宽下的可比性"这个方向长,`div(pow_2(cross_mean(day_wmean(Ret,Ret),5)), LimitWidth)` 或类似的按板宽归一化是文献已经验证过有效的操作,呼应 analysis.md 说"核心①用 `LimitWidth` 做条件化"的设想;但目前只有 Hung–Yang [11] 的具体结论(美股式 MAX,修正后仍显著)是我核实到细节的,A 股专门版本([12][13])只核实到存在和方向,不能当成精确的数值证据。

**小结:** "软聚合(前 k 大均值)不输给硬极值"在文献里有直接证据(Bali–Cakici–Whitelaw 自己的稳健性检验),但"连续凸幂 + EMA"这种我们实际在用的具体聚合形式,文献没有测过,幂次该停在哪一级也没有先验,属于纯粹的经验调参,不是复现文献;A 股涨跌停会扭曲极值类信号这件事有方法论可以抄(Hung–Yang),但"抖动类"信号（而不是收益本身）按板宽重新标度,文献还没人做。

---

## L3 — 日内漂移 / 日内动量 / 成交量加权日内收益(对准核心 ①:`pow_2(cross_mean(day_wmean(Ret, Ret), 5))`,先在 5 天上平均再折叠成幅度)

**能翻译成算子语言的处理方式:**

1. **日内漂移在多日之间累加/平均,是文献里两条独立但方向一致的路线:"同一交易日内的时段续"和"多日之间的符号续"。** Gao–Han–Li–Zhou [17](2018,*Journal of Financial Economics*,"Market Intraday Momentum")发现**同一天内**开盘半小时收益预测收盘半小时收益(美股 ETF,预测 R² 1.6%,高波动/高成交量时更强);这是"日内时段"维度的续,不是我们"多日之间平均"维度的续,**不能直接当成支持证据,只是同一机制家族的近邻**。更贴近我们核心①构造(多日平均)的是 Chu–Gu–Zhou [19](2019,*Finance Research Letters*,A 股市场)——他们发现开盘半小时收益能预测**随后数日**的收益,呈现"动量 + 反转"两段式模式,控制了前一日收益、隔夜收益、星期效应后依然显著,作者把它归因于噪音交易。**翻译过来:** 这条是**直接相关的 A 股证据**,支持"日内收益的某个分量在多日之间有可预测的续性",但 Chu–Gu–Zhou 测的是"开盘半小时收益"这个时段分量,不是我们 `day_wmean(Ret, Ret)` 这种"用收益给自己加权的全天收益"这个构造——**结构不同,方向线索可以借,具体构造不能照搬**。

2. **带符号 vs 折叠(绝对值/平方)这个选择,文献里几乎全部是带符号的,我们核心①的"先平均再平方"(折叠在外层而不是内层)是一个文献没测过的顺序。** Lou–Polk–Skouras [18](2019,*Journal of Financial Economics*,"A Tug of War")把 14 个经典策略的收益拆成隔夜段和日内段,发现**同一个策略在两段里符号常常相反**,且 9/14 的策略全部溢价来自日内段——这条测的是**带符号**的策略收益归因,不折叠。Da–Gurun–Warachka [20](2014,*Review of Financial Studies*,"Frog in the Pan")的信息离散度(ID)用的是**正负收益天数占比之差**(计数,不加权、不折叠),发现连续信息(低 ID)的动量组合比离散信息(高 ID)的动量组合后续收益更高、持续更久(六个月持有期,前者显著性能维持约 8 个月、后者约 2 个月)——这同样是带符号的构造,而且服务于"动量延续性"这个调节效应,不是独立定价变量。
   **翻译过来:** 我们核心①"先在 5 天上 `cross_mean`(带符号地平均)、再在外层 `pow_2`(折叠)"这个顺序,在文献里**没有先例**——文献里"带符号的多日平均"(接近 Chu-Gu-Zhou、ID 的计数版)和"折叠/取幅度"(接近 L1/L2 讨论的 MAX、IVOL)是两件分开讨论的事,**没有查到**谁把两者按"先平均、再折叠"这个顺序叠在一起做过。这与 analysis.md 自己的诊断一致("本种子库里已经挤满了幅度族,这条是唯一的方向持续性信息")——如果真是"方向在多日间的持续性"这个机制,外层折叠这一步在文献的类比框架里相当于「把 Chu-Gu-Zhou 式的带符号延续信号,改造成不分方向的`强度`指标」,这是文献没检验过的新组合,方向上和 N2 预测的"幅度赢、符号没用"一致,但没有文献直接验证。

3. **成交量 / 路径加权的日内收益 vs 等权平均,文献里有扎实的"符号"证据(机构 vs 个人的方向性交易),没有"幅度加权版本单独测"的证据。** Kaniel–Saar–Titman [21](2008,*Journal of Finance*)用机构数据折算的个人净买卖强度发现:个人投资者逆势交易(跌后买、涨后卖),随后一个月被个人净买入的股票超额收益显著为正——这是"净买卖强度(带符号)→ 下月收益"的月度预测关系,用的是**金额加权的买卖方向**,不是我们 `day_wmean(Ret, Ret)`(用分钟收益给自己加权)这种构造。**我没有查到**任何文献把"用成交量/路径给分钟收益加权、再折叠成幅度"这件事单独拿出来检验(即不先假设符号重要)。

4. **日内漂移的持续性与隔夜收益 / 订单失衡持续性的关系:A 股上"隔夜 vs 日内"存在明确的相互替代/拉锯关系,但多日持续性的证据在订单失衡这条线上大多是国际市场、不是 A 股。** Lou–Polk–Skouras [18] 证明美股隔夜段和日内段经常互相抵消;Chu–Gu–Zhou [19] 在 A 股上证明控制了隔夜收益之后日内分量依然显著。订单失衡的**多日持续性**,最直接的证据来自台湾(Lee–Liu–Roll–Subrahmanyam [23],2004,*Journal of Financial and Quantitative Analysis*):小外资机构的订单失衡日间持续性最强、大散户最弱,且价格压力基本不超过一个交易日——**这是台湾市场,不是 A 股,不能直接当 A 股证据**,只能当方法论类比。A 股本身的订单失衡文献(Narayan–Narayan–Westerlund [22],2015,*Pacific-Basin Finance Journal*)测的是**日内 1~90 分钟**的短horizon 预测,**没有测多日持续性**。**翻译过来:** "核心①是不是订单失衡持续性的代理"这条机制假设,A 股上**没有直接的多日持续性证据**可以支持或反驳,是空白;唯一能类比的台湾证据反而提示"价格压力很少超过一天",如果成立,会削弱"5 天窗口"这个选择的机制解释力——这点应该提醒 PI,核心①的"持续了几天"外围方向可能找不到文献支持的窗口长度先验,需要自己扫。

**小结:** 多日持续性机制在 A 股上有一条直接证据(Chu–Gu–Zhou,带符号、开盘半小时分量),但构造和我们的核心①不同;"先平均后折叠"这个具体顺序文献完全没测过;机构/个人的方向性交易证据充分但都是带符号的,没人检验过折叠版本是否还有信息;订单失衡的多日持续性在 A 股缺乏直接证据,能参照的台湾证据反而提示价格压力不持久,对"5 天"这个窗口选择没有文献背书。

---

## L4 — 日度风险/活动指标在窗口内的离散度,以及它与冻结报价/零变动分钟的共动

**能翻译成算子语言的处理方式:**

1. **"波动的波动"(vol-of-vol)作为独立定价变量,是有扎实文献的,方向与我们的怀疑一致(波动尾部本身有定价力),但构造细节我没能核实完整。** Baltussen–van Bekkum–van der Grient [15](2018,*Journal of Financial and Quantitative Analysis*,"Unknown Unknowns: Uncertainty About Risk and Stock Returns")报告:对"风险的不确定性"(用期权隐含波动率的波动率衡量)高的股票,相对低的股票,后续跑输约 8% 年化,且用 20 多个已知因子都解释不掉;作者倾向用"偏好解释"而非套利摩擦解释。**我尝试用 WebFetch 直接读取 PDF 全文失败(文件是压缩流,只读到大纲和元数据)**,所以**没有核实到**:(i) 这个 vol-of-vol 具体是不是像我们的 `cross_stddev(..., 60)` 这样对波动水平做标准差、还是像变异系数那样除以水平做了归一化;(ii) 聚合窗口是多长、有没有测试不同窗口的敏感性。这两条**标 verified:false,只引用核心结论(存在性、方向、量级),不引用构造细节**。
   **翻译过来:** 这篇是"离散度本身被定价、且方向是离散度越高收益越低"的最直接证据,支持把核心②的"自身历史位置的离散度"(`cross_stddev(day_durbin_watson(High), 60)`,我们拆解里已经测出 1.1007 有效)当成一条独立信息、不是波动均值的重新包装;但**到底该不该归一化**,文献没有给出可核实的答案,这与我们"证据提示未归一化版本和归一化版本可能结论相反"的怀疑(§1.5)吻合,**仍然是开放问题,不是文献帮我们判定的**。

2. **符号拆分(正负分开算)相对不拆分,在定价力上有差异,这条和 L1 第 4 点重复引用同一批文献,但角度是"离散度"而不是"水平"。** Patton–Sheppard [5] 与 Bollerslev 系列 [6][7] 证明把日度波动按正负拆开(已实现半方差/半协方差)比不拆分的版本提供更多定价信息——如果把"离散度"理解成"已实现方差的方差",这条文献提示**先按符号拆分、再各自算离散度**可能比"不分方向直接算离散度"更有信息,这是 analysis.md 外围方向里没有列出、但可以加进去的一条新想法。

3. **零变动分钟/零收益天数的流动性含义,是文献里最成熟的部分,但"和波动的共动"这件事没有被直接研究过。** Lesmond–Ogden–Trzcinka [16](1999,*Review of Financial Studies*)用月度零收益天数占比估计隐含交易成本(成本太高时价格不动),1963–1990 年美股大盘/小盘股隐含双边成本分别约 1.2%/10.3%;这是最经典的"零变动 = 流动性差"代理,但样本是美股、且是**天数**占比,不是我们 `day_flat_ratio` 这种**分钟**占比。**我没有查到**任何文献把"零变动占比"和"波动 / 活动指标的离散度"的**共动**(而不是各自的水平)放在一起研究过——这与 r1 轮的发现一致(同样的空白),是真空白,不是我漏查。

4. **A 股的涨跌停会制造"冻结报价"状态,这件事本身被充分记录,但没人把它和离散度类信号连起来。** Wan et al. [24] 的高频数据证实涨跌停附近报价会连续多分钟不变(封板),这正是 `day_flat_ratio` 升高的物理机制;Yao et al. [12] 的论文题目本身就在提醒"涨跌停会让极值类测量失真"。**翻译过来:** `day_flat_ratio` 的**跨日波动**(analysis.md N-b 的提议)如果要落地,目前**没有文献** 直接检验过"冻结报价状态本身的不稳定性"这个二阶构造,是我们在做文献还没覆盖的事,风险是没有先验指导窗口和归一化方式,机会是没有被证伪的顾虑。

**小结:** vol-of-vol 作为独立定价变量,文献证据扎实,方向支持我们怀疑的"离散度本身有信息",但具体要不要归一化、窗口多长,文献没给出可核实答案(没能读到全文);符号拆分后再测离散度是文献提示但我们还没做的组合;零变动 / 冻结报价与波动类指标的共动,在 A 股还是美股都没有文献,是最大的空白,值得单独立一个 N 位去填。

---

## 参考文献

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|---|
| 1 | The Extreme Value Method for Estimating the Variance of the Rate of Return | Michael Parkinson | 1980-01(*The Journal of Business*, Vol. 53, No. 1, pp. 61–65) | Journal of Business | https://www.jstor.org/stable/2352357 | true(标题、期刊、卷期页码经多个二次来源一致确认;原文未直接打开核实公式细节) |
| 2 | On the Estimation of Security Price Volatilities from Historical Data | Mark B. Garman, Michael J. Klass | 1980-01(*The Journal of Business*, Vol. 53, No. 1, pp. 67–78) | Journal of Business | https://www.jstor.org/stable/2352358 | true(标题、期刊、卷期页码经多个二次来源一致确认;"7.4 倍效率"这个具体数字只在交易平台文档里看到,未在原文核实,标为存疑) |
| 3 | Estimating Variance From High, Low and Closing Prices | L. C. G. Rogers, S. E. Satchell | 1991(*The Annals of Applied Probability*, Vol. 1, No. 4, pp. 504–512;DOI 10.1214/aoap/1177005835) | Annals of Applied Probability | https://projecteuclid.org/euclid.aoap/1177005835 | true(标题、期刊、卷期页码、DOI 经 Project Euclid 记录确认;摘要文字——"用无漂移布朗运动极值逼近有漂移极值会带来较严重误差"——经二次来源转述确认) |
| 4 | The Cross-Section of Volatility and Expected Returns | Andrew Ang, Robert J. Hodrick, Yuhang Xing, Xiaoyan Zhang | 2006-02(*Journal of Finance*, Vol. 61, pp. 259–299);NBER WP 10852, 2004-10 | Journal of Finance / NBER | https://www.nber.org/papers/w10852 | true |
| 5 | Good Volatility, Bad Volatility: Signed Jumps and The Persistence of Volatility | Andrew J. Patton, Kevin Sheppard | 2015(*Review of Economics and Statistics*, Vol. 97, No. 2, pp. 683–697);工作论文版本至少 2011-10 流传 | Review of Economics and Statistics | https://ideas.repec.org/a/tpr/restat/v97y2015i2p683-697.html | true(存在性、期刊卷期确认;半方差归一化分母的具体公式未核实) |
| 6 | Realized Semibetas: Disentangling "Good" and "Bad" Downside Risks | Tim Bollerslev, Andrew J. Patton, Rogier Quaedvlieg | 2022(*Journal of Financial Economics*, Vol. 144, No. 1, pp. 227–246);工作论文版本至少 2021-04 流传(public.econ.duke.edu,落款"14apr21") | Journal of Financial Economics / Duke 工作论文 | https://public.econ.duke.edu/~ap172/BPQ_semibeta_14apr21.pdf | true(标题、作者、核心结论——"坏-坏"半协方差正向预测收益、其余符号组合不显著或方向相反——经 Duke 学者页与工作论文摘要确认) |
| 7 | Realized Semicovariances | Tim Bollerslev, Jia Li, Andrew J. Patton, Rogier Quaedvlieg | 2020-07(*Econometrica*, Vol. 88, No. 4) | Econometrica | https://www.econometricsociety.org/doi/10.3982/ECTA17056 | true(标题、作者、期刊卷期经 Econometric Society 官方记录确认;论文做的是方差预测,不是收益横截面检验,这点在正文已注明) |
| 8 | (保留编号,未使用) | — | — | — | — | — |
| 9 | Maxing Out: Stocks as Lotteries and the Cross-Section of Expected Returns | Turan G. Bali, Nusret Cakici, Robert F. Whitelaw | 2011-02(*Journal of Financial Economics*, Vol. 99, No. 2, pp. 427–446);NBER WP 14804, 2009-03 | Journal of Financial Economics / NBER | https://www.nber.org/papers/w14804.pdf | true(含"MAX 定义为前 2~5 大收益均值时结论稳健"这条稳健性检验,经二次来源确认属于原文本身的检验,未直接读到原文表格数字) |
| 10 | Do extreme returns matter in emerging markets? Evidence from the Chinese stock market | Gilbert V. Nartea, Dongmin Kong, Ji Wu | 2017(*Journal of Banking & Finance*, Vol. 76, pp. 189–197) | Journal of Banking & Finance | https://ideas.repec.org/a/eee/jbfina/v76y2017icp189-197.html | true |
| 11 | The MAX Effect: Lottery Stocks with Price Limits and Limits to Arbitrage | Weifeng Hung, Jimmy Yang | 2018(*Journal of Financial Markets*, Vol. 41, pp. 77–91) | Journal of Financial Markets | https://ideas.repec.org/a/eee/finmar/v41y2018icp77-91.html | true(摘要核实;样本市场细节未核实到全文) |
| 12 | MAX is not the max under the interference of daily price limits: Evidence from China | Shouyu Yao, Chunfeng Wang, Zhenming Fang, Chaoshin Chiao | 2021(*International Review of Economics & Finance*, Vol. 73, pp. 348–369) | International Review of Economics & Finance | https://ideas.repec.org/a/eee/reveco/v73y2021icp348-369.html | true(标题、作者、期刊卷期页码经多个二次来源一致确认;摘要具体结论数字未核实,只能确认论点方向与标题一致) |
| 13 | MAX, lottery-type stocks, and the cross-section of stock returns: Evidence from the Chinese stock market | Hoang Van Hai | 2023(*Cogent Economics & Finance*, Vol. 11, No. 1, Article 2175471) | Cogent Economics & Finance | https://ideas.repec.org/a/taf/oaefxx/v11y2023i1p2175471.html | true(标题、期刊、卷期、文章号核实;只核实到摘要第一句研究对象陈述,具体结论未核实) |
| 14 | Idiosyncratic Volatility Anomaly and Its Causes in the Chinese Stock Market | (需核实全名)Chen, Ye 等 | 2021(*Discrete Dynamics in Nature and Society*, Article 9549366) | Discrete Dynamics in Nature and Society | https://ideas.repec.org/a/hin/jnddns/9549366.html | false(文章存在、期刊卷期经 IDEAS/DOAJ 确认;但完整作者名单与摘要具体数字本次检索只拿到二次归纳,标 false 以提醒 PI 核实) |
| 15 | Unknown Unknowns: Uncertainty About Risk and Stock Returns | Guido Baltussen, Sjoerd van Bekkum, Bart van der Grient | 2018-07(*Journal of Financial and Quantitative Analysis*, Vol. 53, No. 4, pp. 1615–1651,DOI 10.1017/S0022109018000480) | Journal of Financial and Quantitative Analysis | https://personal.eur.nl/vanbekkum/2018JFQA_unknown_unknowns.pdf | true(标题、作者、核心结论——vol-of-vol 高的股票跑输约 8%/年、不被 20 多个已知因子解释——经多个二次来源一致确认;WebFetch 读取 PDF 全文失败(压缩流),vol-of-vol 具体构造/归一化方式与聚合窗口未核实,正文已标注) |
| 16 | A New Estimate of Transaction Costs | David A. Lesmond, Joseph P. Ogden, Charles A. Trzcinka | 1999(*Review of Financial Studies*, Vol. 12, No. 5, pp. 1113–1141) | Review of Financial Studies | https://www.bauer.uh.edu/rsusmel/phd/lot_1999RFS.pdf | true |
| 17 | Market Intraday Momentum | Lei Gao, Yufeng Han, Sophia Zhengzi Li, Guofu Zhou | 2018(*Journal of Financial Economics*, Vol. 129, No. 2, pp. 394–414) | Journal of Financial Economics | https://ideas.repec.org/a/eee/jfinec/v129y2018i2p394-414.html | true(标题、作者、期刊卷期经多个二次来源一致确认;核心结论——标普 ETF 上开盘半小时收益预测收盘半小时收益——经同一组来源确认) |
| 18 | A Tug of War: Overnight Versus Intraday Expected Returns | Dong Lou, Christopher Polk, Spyros Skouras | 2019(*Journal of Financial Economics*, Vol. 134, pp. 192–213) | Journal of Financial Economics | https://personal.lse.ac.uk/polk/research/TugOfWar.pdf | true(LSE Research Online 与 NBER 会议版确认标题、作者、期刊信息与核心结论——14 个经典策略里 9 个的全部溢价来自日内段,隔夜段与日内段常常符号相反) |
| 19 | Intraday momentum and reversal in Chinese stock market | Xiaojun Chu, Zherong Gu, Haigang Zhou | 2019-09(*Finance Research Letters*, Vol. 30, pp. 83–88,DOI 10.1016/j.frl.2019.04.002) | Finance Research Letters | https://ideas.repec.org/a/eee/finlet/v30y2019icp83-88.html | true(标题、作者、期刊卷期页码、DOI 经多个来源一致确认;核心结论——A 股开盘半小时收益预测随后数日收益,控制隔夜收益与星期效应后仍显著,归因为噪音交易——经摘要转述确认) |
| 20 | Frog in the Pan: Continuous Information and Momentum | Zhi Da, Umit G. Gurun, Mitch Warachka | 2014(*Review of Financial Studies*, DOI 10.1093/rfs/hhu003);工作论文至少 2010 年即流传 | Review of Financial Studies | https://www3.nd.edu/~zda/Frog.pdf | true(标题、作者、发表信息经图书馆目录与机构存档确认;ID 指标的逐字公式未在本次检索中直接核验,数值引自二次转述) |
| 21 | Individual Investor Trading and Stock Returns | Ron Kaniel, Gideon Saar, Sheridan Titman | 2008-02(*Journal of Finance*, Vol. 63, No. 1, pp. 273–310) | Journal of Finance | https://ideas.repec.org/a/bla/jfinan/v63y2008i1p273-310.html | true |
| 22 | Do order imbalances predict Chinese stock returns? New evidence from intraday data | Paresh Narayan, Seema Narayan, Joakim Westerlund | 2015(*Pacific-Basin Finance Journal*, Vol. 34, pp. 136–151,DOI 10.1016/j.pacfin.2015.07.003) | Pacific-Basin Finance Journal | https://ideas.repec.org/a/eee/pacfin/v34y2015icp136-151.html | true |
| 23 | Order Imbalances and Market Efficiency: Evidence from the Taiwan Stock Exchange | Yi-Tsung Lee, Yu-Jane Liu, Richard Roll, Avanidhar Subrahmanyam | 2004(*Journal of Financial and Quantitative Analysis*, Vol. 39, No. 2, pp. 327–341);工作论文版本至少 2001 年流传(UCLA Anderson) | Journal of Financial and Quantitative Analysis | https://ideas.repec.org/a/cup/jfinqa/v39y2004i02p327-341_00.html | true(**样本是台湾证交所,不是 A 股**,正文已注明,不得当 A 股证据使用) |
| 24 | Statistical Properties and Pre-Hit Dynamics of Price Limit Hits in the Chinese Stock Markets | Yu-Lei Wan, Wen-Jie Xie, Gao-Feng Gu, Zhi-Qiang Jiang, Wei Chen, Xiong Xiong, Wei Zhang, Wei-Xing Zhou | 2015-04(*PLoS ONE*, Vol. 10, No. 4, e0120312,DOI 10.1371/journal.pone.0120312) | PLoS ONE | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4395215/ | true(标题、作者、期刊卷期、DOI、样本范围——2000–2011 年沪深 A 股高频数据——经 PMC 记录与多个二次来源一致确认) |

---

## 给 PI 的检索空白清单(明确搜不到,不要当成"文献证伪")

- **L1**:没有查到任何文献把"分钟序列自相关结构(DW 式抖动)"当作已实现方差 / 极差估计量的一种,和经典 Parkinson/GK/RS 对照过;没有查到"抖动的绝对水平独立于均值波动"是否仍能定价的检验;没有查到把已实现方差 / 极差类估计量按涨跌停幅度(`LimitWidth`)重新标度的研究(有方法论可以从 L2 的 Hung–Yang 类比过来,但原文没做);没有查到按流动性 / 规模 / 上市年限对此类估计量分组的 A 股研究。
- **L2**:没有查到"连续凸幂(2/3/7.5 次)+ 指数加权"这种具体聚合形式与简单均值/中位数/高分位/硬极值的系统性横向比较;没有查到幂次该停在哪一级的任何先验;Yao et al. [12]、Hoang Van Hai [13] 两篇专门研究 A 股 MAX 与涨跌停/彩票偏好的论文,本次检索只核实到标题与期刊信息,具体结论数字没有核实到,PI 若要引用具体数字需要另外找全文。
- **L3**:没有查到把"先在多日之间带符号平均、再在外层折叠成幅度"这个具体顺序测试过的文献;没有查到"用成交量/路径给分钟收益加权后再折叠"单独作为横截面预测变量的检验;没有查到订单失衡在 A 股的多日持续性研究(可类比的台湾证据——价格压力很少超过一个交易日——如果适用,会削弱"5 天窗口"的机制解释)。
- **L4**:Baltussen 等 [15] 的 vol-of-vol 具体构造(是否归一化)与聚合窗口,本次检索未能从全文核实,只核实到核心结论与量级;没有查到"零变动占比"与"波动/活动指标离散度"的共动研究(美股、A 股均无,这是本轮四个题目里最明确的真空白);没有查到把"冻结报价状态的不稳定性"本身当作信号构造并检验过的文献。
