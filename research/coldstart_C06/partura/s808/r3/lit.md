# 文献:种子 808,C 组,第 3 轮(最后一轮)

对应 `analysis.md` §5 的 Q1–Q4(核心 1 `day_kurt(Ret)` / N-1 开盘竞价方差占比 / 纯多头十分位书的脆弱性 / 涨跌停对「不动」类度量的污染)。
只用 2023-08-08 前发表的论文 / 工作论文 / 研究报告(arXiv、SSRN、NBER、CREATES 以首版日期为准);拿不准发表日期的不用,如实列在文末。
每条处理方式后标 `[R#]`,对应文末「出处列表」。`verified: true` = 本次会话里确实在 WebSearch 结果或 WebFetch 页面上看到了标题 / 作者 / 刊物 / 链接这几项;没查到的写明「搜不到」,不编。
本轮 Q4 与第 1、2 轮的涨跌停文献(`r1/lit.md`、`r2/lit.md`)有 4 篇重叠,是因为三轮问的都是同一批涨跌停实证文献,本轮问题换了角度(「是不是与停滞类度量同一个机制」),
重新检索确认后再引用,不是直接照抄;其余 22 篇是本轮新查的。

---

## Q1(对准核心 1 / 轴 C:`day_kurt(Ret)` = 日内收益峰度 = 变动的集中度)

**(i)有没有把高频收益的四阶矩 / 峰度本身当横截面特征用过(而不是只用它检验跳跃是否存在)?用的是峰度、已实现四次幂变差、跳跃变差占比,还是最大单根收益比值?方向正还是负?**

1. **有,而且这正是 `day_kurt(Ret)` 这个写法的直接先例。** Amaya, Christoffersen, Jacobs & Vasquez(工作论文 2011,正式发表 2015,*Does Realized Skewness Predict the Cross-Section of Equity Returns?*,JFE 118)
   把每周已实现偏度**和**已实现峰度都当作横截面排序特征直接检验(不是先做跳跃存在性检验再反过来定价),用的是过去一周 5 分钟收益算出的三、四阶矩的周度均值 `[R1]`。
   **结果直接可比我们的方向假设**:已实现偏度与下周收益显著负相关(最低偏度十分位买、最高十分位卖,周均 19bp,t=3.70);**已实现峰度与下周收益是正相关,但显著性弱、不总是稳健**;
   已实现波动本身与下周收益没有稳定关系。**翻译成算子语言**:这篇文献里「峰度本身是正向的横截面特征」这个方向与 `analysis.md` H3 的 sign(+1,多头腿是 kurt 最低的票,
   即「峰度越高未来越该跌/越高越该空」)**方向一致**——但文献的显著性比偏度弱得多,这是一条如实的警示,不要把 H3 的 +1.10 读成「文献已经证实峰度溢价很强」,
   证实的只是方向,强度证据薄弱。
2. **没有找到直接使用「跳跃变差占比(jump variation share)÷已实现四次幂变差(quarticity)」这个具体比值构造横截面特征、再检验定价能力的资产定价论文**(搜不到,见文末)。
   已实现四次幂变差 / bipower variation 在文献里几乎总是用作**跳跃检验的分母(方差的方差)**,不是直接拿来排序——这正好呼应 Q1(ii)。

**(ii)这类度量与波动水平在构造上有分母关系,文献怎么确认它不是波动的非线性改写——按波动分组、取残差,还是用无量纲化的比值?**

3. **Barndorff-Nielsen & Shephard(2006,*Econometrics of Testing for Jumps in Financial Economics Using Bipower Variation*,Journal of Financial Econometrics 4(1))**
   给出了这条问题在高频统计里的标准答案:**把已实现方差(RV)减去双幂次变差(BV),再除以已实现四次幂变差(quarticity)的平方根来标准化**,
   这个比值在「无跳跃」零假设下渐近服从标准正态分布,**不随波动水平本身的高低而改变分布形状** `[R2]`。
   **翻译成算子语言**:这正是 `day_kurt(Ret) = m4/m2² − 3` 的构造逻辑本身——分子是四阶矩、分母是二阶矩的平方,
   文献里「确认不是波动改写」的标准做法**不是按波动分组或取残差,而是构造一个本身就无量纲的比值统计量**,
   `analysis.md` §1.2(a) 的量纲论证(「m4/m2² 是无量纲的,所以不是波动水平换个写法」)与这支文献的方法论完全一致,这是本轮最硬的一条文献支撑。
4. **Lee & Mykland(2008,*Jumps in Financial Markets: A New Nonparametric Test and Jump Dynamics*,RFS 21(6))**走的是同一条路但做到了日内定位:
   检验统计量是**单根收益除以同期双幂次变差估出的局部波动**,模型无关,可以精确定位哪一根 bar 触发了跳跃 `[R3]`。
   **翻译**:这给了 `day_kurt(Ret)` 一个更精细的对照——如果要进一步确认峰度读的是「一根 bar 支配」还是「若干根 bar 共同贡献」,
   文献的标准做法是先用 Lee-Mykland 统计量定位触发日,再看定位出来的触发根是不是系统性地落在第 0 列(09:30 集合竞价),这正是 §4.2 R 第 1 组第 3 颗
   `neg(day_kurt(in_slice(Ret, 1, 237)))` 想回答的问题,只是我们用的是「整段剔除再比较」而不是「逐日定位」,更便宜但分辨率更低,这一点要如实告诉审计。
5. **Christensen, Oomen & Podolskij(工作论文 2011,CREATES RP 2011-19;正式发表 2014,*Fact or Friction: Jumps at Ultra High Frequency*,JFE)**
   提供了反面的警示:他们用毫秒级数据重新估计发现,**传统的跳跃变差度量会把短时间内的一段「波动爆发」(burst of volatility)误判成跳跃**,
   跳跃对总变差的真实贡献比此前文献估计的小一个数量级 `[R4]`。**翻译成警示**:`day_kurt(Ret)` 用的是日频 241 根分钟 bar(远低于毫秒级),
   这篇论文的结论不能直接套用(我们的频率下真跳跃和波动爆发的区分问题本来就更粗),但它说明「峰度 / 跳跃类度量容易把波动的集中爆发误读成单点跳跃」
   是这支文献里反复出现的陷阱,§1.2(e) 风险清单第 2 条(「与停滞族的机械耦合」)方向是对的,只是机制应该再加一条:
   「集中在少数几根 bar 的波动爆发」本身也会被 `day_kurt` 读成高峰度,不一定是单根跳跃,这件事文献里没有专门针对分钟频率 A 股数据的结果,仍是推断。

**(iii)它与非流动性 / 报价停滞(零收益分钟多 ⇒ 少数几分钟承担全部变动 ⇒ 峰度高)怎么分开?有没有同时控制两者的结果?**

6. **没有找到同时把「峰度 / 跳跃集中度」与「零收益占比 / 报价停滞」两类度量放进同一个横截面检验、看谁被谁吃掉的资产定价论文**(搜不到,见文末)。
   这是本轮 Q1 最大的文献缺口,与 `analysis.md` §1.2(d)「ρ(H2, H3) 三轮下来一次没算过」缺的是同一类证据。
7. **但相邻的高频统计文献给出了一个可以直接抄的操作性答案:不区分机制,直接把高零收益日从跳跃统计里剔除。**
   Bonaccolto, Zambon & Caporin(会议论文,2018,*Systemic events and diffusion of jumps*,第 50 届意大利统计学会年会)
   把日内零收益占比 > 25% 的资产定义为「不流动」,并且**只在非零收益占比 ≥ 75% 的交易日上做跳跃检验,其余的日子直接当「当天无跳跃」处理**,
   不去判断这一天的高集中度读数有多少是跳跃、多少是停滞造成的假象 `[R6]`。**翻译成算子语言**:这支持 §1.2(e) 第 3 条
   (「全天封板 ⇒ `div(0,0)` = NaN ⇒ 封板日自动掉出」)的方向,但给出了一个更强的操作性建议——
   如果 `day_zero_ratio(Ret)` 很高,`day_kurt(Ret)` 本身的读数就应该被当作不可靠而不是「真实的高峰度」,这与我们现在把 `day_zero_ratio` 当**条件化变量**
   (R 第 1 组第 4 颗)不是同一件事:文献里是**过滤 / 剔除**,不是**条件化排序**,这个区分要如实写给 PI,不要把「条件化」说成文献已经验证过的标准做法。
   这篇论文本身建立在 Caporin, Kolokolov & Renò(工作论文 2016,SAFE WP 149;正式发表 2017,*Systemic Co-Jumps*,JFE 126(3))的跳跃检验框架上,
   后者发现**单资产层面的跳跃检验比指数层面的跳跃检验更容易捕捉到大量个股同时出现的协同跳跃**,且这类事件与新闻到达、VIX 跳升同时发生 `[R5]`,
   与我们「kurt 读的是个股日内变动集中度」这个判定方向一致,但样本(美股高频 tick 数据)和频率都与我们的环境相差很远,只能当方法论旁证,不能当数字证据。
8. Bali, Cakici & Whitelaw(工作论文 2009,NBER WP14804;正式发表 2011,*Maxing Out*,JFE 99(2),已见于 `r1/lit.md` R5)用过去一个月**日**收益最大值(MAX)
   构造的因子与峰度衡量的是相关但不同的东西(MAX 是「最大单日收益」,`day_kurt` 是「当天变动有多集中在一根分钟 bar 上」),但两者都属于「极端值主导」这一类特征,
   原论文发现 MAX 与收益负相关,且**部分解释了特质波动率异象**(放入 MAX 后特质波动率与收益的负向关系反转)`[R7]`——
   这是一个额外的警示,提示 `day_kurt` 与特质波动率、与停滞族可能存在类似的三方纠缠,只作为旁证,不单独展开。

---

## Q2(对准 N-1:开盘竞价 / 隔夜那一根 bar 占当日方差的比例)

**(i)用的是带符号的隔夜收益还是隔夜方差占比?两者结论一样吗?有没有讨论「用占比避开与短期反转重叠」?**

1. **文献里两条线都存在,而且方法上是分开的。** 带符号隔夜收益这条线最直接的代表是 Lou, Polk & Skouras(工作论文 2014,LSE/FMG DP744;正式发表 2019,
   *A Tug of War: Overnight versus Intraday Expected Returns*,JFE):他们把动量、反转等已知策略的收益拆成隔夜段和日内段,发现
   **动量的异常收益几乎全部来自隔夜,而其余策略的收益几乎全部来自日内,两段收益经常符号相反**(「拔河」)`[R8]`。
   这篇用的是**带符号**的隔夜收益,不是方差占比。Berkman, Koch, Tuttle & Zhang(2012,*Paying Attention: Overnight Returns and the Hidden Cost of Buying at the Open*,
   JFQA 47(4))同样用带符号隔夜收益,发现受关注的股票隔夜上涨、日内回吐,机制是关注度驱动的开盘买盘压力 `[R9]`。
   **没有找到一篇论文明确讨论「换成隔夜方差占比可以避开与短期反转重叠」这个论证**(搜不到,见文末)——
   这件事目前只是 `analysis.md` §4.3 N-1 自己的方法论判断(用占比而不用带符号收益,因为后者就是反转控制的换皮),文献能提供的只是「带符号隔夜收益确实与反转类策略高度纠缠」
   这个事实本身(Lou-Polk-Skouras 的「拔河」现象、Berkman 等人的隔夜涨日内跌),支持我们**避开**带符号版本的方向判断,但不能说文献「验证过」占比这个具体解法。
2. **China 专门的带符号隔夜收益证据,方向明确且与反转高度绑定:** Qiao & Dam(2020,*The Overnight Return Puzzle and the "T+1" Trading Rule in Chinese Stock Markets*,
   Journal of Financial Markets 50)发现 A 股隔夜收益平均为负,规模约 −14bp,并把它归因于 T+1 规则本身(T+1 禁止当日买入当日卖出,导致开盘价系统性低开)`[R12]`;
   Bai(工作论文,SSRN,2020-01,*Marketability As Real Options: The Cross Sectional Variation of Overnight Returns in China*)用期权定价框架解释同一个现象,
   发现隔夜收益随资产波动率、波动率风险、跳跃风险上升而**变得不那么负**,并说这类「可交易性期权」变量可以解释隔夜收益与非流动性、短期反转、动量之间的关联 `[R13]`。
   **翻译成警示**:两篇独立确认了 A 股「带符号隔夜收益」这个量本身就是反转 / 流动性 / T+1 制度摩擦的混合物,这进一步支持 §4.3 N-1「不要用带符号版本」的判断,
   而且是**专门针对 A 股**的证据,比 Q2(i) 里的两篇美股文献更贴近本环境。

**(ii)开盘集合竞价在高频统计里怎么处理——一律剔除、单独建模,还是当成信息到达的度量?不剔除时高频矩的计算结论差多少?**

3. **主流做法是单独建模,不是剔除也不是直接混进日内跳跃。** Andersen, Bollerslev & Huang(工作论文 2007,CREATES RP 2007-14;正式发表 2011,
   *A Reduced Form Framework for Modeling Volatility of Speculative Prices Based on Realized Variation Measures*,Journal of Econometrics 160(1))
   把每日总方差显式拆成三块:**日内连续路径方差、日内跳跃方差、隔夜收益方差**,三块各自用不同的模型(长记忆 HAR-GARCH、跳跃发生率的 ACH 模型、
   隔夜方差自己的增广 GARCH)分别建模,再合成 `[R11]`。**翻译成算子语言**:这直接回答了 Q2(ii)——**隔夜 / 竞价那一段在文献里是被当作与日内跳跃不同的第三个独立成分,
   单独建模,不是剔除、也不是简单并入日内的跳跃变差**。这支持 `analysis.md` §4.3 N-1 把 `day_first(Ret)` 的方差占比当一个**独立输入**而不是 `day_kurt` 的一个解释变量来处理,
   与我们现在的方案(把它写成一个全新的轴,而不是 kurt 的分解项)方向一致。
   没有找到「不剔除 vs 剔除竞价」对高频矩(方差 / 偏度 / 峰度)计算结果具体差多少的量化对照(搜不到,见文末)——
   Andersen-Bollerslev-Huang 的框架是「分开建模」,不是「测一下差多少」,这条经验量化证据本身在搜索范围内没有找到。
4. French & Roll(1986,*Stock Return Variances: The Arrival of Information and the Reaction of Traders*,JFE 17(1))是这整条文献最早的源头:
   他们发现交易时段的收益方差远高于非交易时段,并通过交易所假期(公开信息流不变但不交易)分离出私人信息到达是交易时段高方差的主因,
   噪声交易只能解释 4%–12% 的日方差 `[R10]`。**翻译**:这是把「隔夜 / 非交易时段」当信息到达的度量这条思路的最早文献来源,
   与 Andersen-Bollerslev-Huang 的三分法是同一条线的两个阶段(French-Roll 证明两段方差机制不同,ABH 把这个区分做成了可估计的统计模型)。

**(iii)隔夜 / 日内方差占比与流动性、规模、关注度的关系有没有被系统控制过?A 股的 T+1、集合竞价、涨跌停制度下有没有专门结果?**

5. **用「方差占比」这个具体构造、同时系统控制流动性 / 规模 / 关注度的 A 股论文,没有找到**(搜不到,见文末)。
   Qiao & Dam `[R12]` 和 Bai `[R13]` 都是用**带符号隔夜收益**做横截面检验,各自控制了常见的风险因子(波动率、跳跃风险等),
   但都不是「方差占比」这个构造,也没有把流动性 / 规模 / 关注度一次性放进同一个回归系统控制。
   这是 Q2 最大的文献缺口,也呼应 §4.4 给 PI 的 corr 请求第 2 条——`div(mul(day_first(Ret), day_first(Ret)), day_sum(mul(Ret, Ret)))` 这个具体构造
   目前只有机制上的文献支持(ABH 的三分法框架),没有文献级的横截面检验结果可以直接对照,§4.3 N-1 说「文献见 §5 的 Q2」时,这一条要如实降级成
   「构造思路有文献支持,具体的定价检验结果是我们自己要做的」。

---

## Q3(对准 §1.4:纯多头十分位书的脆弱性,以及「低相关却承担全部多头收益」的角落泄漏)

**(i)两个秩相关 0.9 的特征,其最高十分位可以差三分之一的成员——文献怎么报告和控制「同一机制不同写法、多头腿差很多」这种现象?**

1. **直接针对「秩相关 0.9 但十分位成员差三分之一」这个具体数字现象的论文,没有找到可独立核实的资产定价文献**(搜不到,见文末;曾搜到一篇 2025 年挂在
   AFA/JOF 网站的工作论文专门研究跨 164 个异象的十分位重叠,但其首版日期晚于 2023-08-08,按规则不能用,如实记录于此,不计入出处列表)。
2. **最接近的、日期合规的证据是 Israel & Moskowitz(2013,*The Role of Shorting, Firm Size, and Time on Market Anomalies*,JFE 108(2))对多头腿单独核算贡献**:
   他们把规模、价值、动量三个异象的收益拆成多头腿和空头腿分别核算,发现**多头腿贡献了几乎全部的规模溢价、约 60% 的价值溢价、一半的动量溢价**,
   且这个分解在不同样本期、不同国际市场上都稳健 `[R14]`。**翻译成算子语言**:这是文献里「只看多头腿会不会把结论做歪」这个问题最直接的量化先例——
   它的方法是**把多头腿单独拎出来核算贡献占比**,不是比较两个相关写法之间的差异,所以不能直接回答「ρ=0.9 的两个写法为什么分数差 0.85」这个具体问题,
   但它确认了「纯多头检验」在文献里本身就是一个需要专门核算、不能想当然外推到空头腿的问题,这支持 §1.4 教训的大方向。
3. **双重排序 / Fama-MacBeth 回归 / 单变量组合排序三种标准方法的系统性介绍**:Bali, Engle & Murray(2016,*Empirical Asset Pricing: The Cross Section of Stock Returns*,
   Wiley 教材)把每一类异象的检验都统一按「单变量组合分析→双变量组合分析→Fama-MacBeth 回归」三步走,双变量组合分析(双重排序)是文献里处理
   「一个特征的效应是不是被另一个变量的非线性暴露污染」这个问题的标准工具 `[R15]`。**翻译**:如果要诊断「新 H2 的 +0.345 是不是重新带回来的规模倾斜」,
   文献的标准做法是先按 size 分组再在组内看 distinct/kurt 的效应是否还在(双重排序),这与 §4.2 R 第 2 组第 1 颗(配完再按市值重新中性化)的思路一致,
   只是文献用的是**分组排序**,我们用的是**条件化中性化**,这两者在方法论上同源但不是同一个操作,写给审计时要讲清楚是「同源的思路」而不是「文献已验证的同一方法」。

**(ii)秩相关很低(0.1–0.3)但极端一端在控制变量上高度集中——有没有标准诊断(双重排序、分段回归、组内中位数检验、特征调整收益)?**

4. **特征调整收益(DGTW)仍是这个问题最成熟的方法**:Daniel, Grinblatt, Titman & Wermers(1997,*Measuring Mutual Fund Performance with Characteristic-Based Benchmarks*,
   JF 52(3),已见于 `r1/lit.md` R16)用 125 个规模 × 账面市值比 × 动量的被动组合做基准,不假设任何线性关系,专门用来检测「一个策略的收益是不是来自对已知特征的
   非线性暴露,而不是真的新信息」`[R16]`。**翻译**:这是诊断「低线性相关、高非线性 / 角落暴露」最直接的工具,比我们现在用的「按控制取残差再算 ρ」更能处理非线性,
   § 4.4 corr 请求第 3 条(8 个 head 与 5 个控制的 |ρ|)如果要进一步升级,可以考虑按控制变量分桶后分别重算 score,而不只是看残差相关系数。
5. **「组内中位数检验」这个具体名字的诊断方法,没有找到**(搜不到,见文末);双重排序(Bali-Engle-Murray `[R15]`)和特征调整收益(DGTW `[R16]`)是找到的、
   日期合规的两种标准诊断,分段回归在这两本/篇文献里都以「按某变量分组再分别跑回归」的形式出现,不是一个独立命名的方法,这一点要如实告诉 PI,
   不要把「组内中位数检验」说成文献已有的专门工具。

**(iii)用 min(样本内, 验证集)这类取最差腿的口径挑参数,文献对它的选择偏差有什么记载?**

6. **记载很多,但角度是「多次试错后挑最好的」,不是「用两个子样本的较差值挑」——这个区分要讲清楚。**
   White(2000,*A Reality Check for Data Snooping*,Econometrica 68(5))首次给出可操作的检验:当研究者在同一个数据集上试了很多个模型 / 规格,
   只报告表现最好的那个,传统的显著性检验会系统性地低估「纯属运气」的概率,他给出了一个基于 bootstrap 的「现实性检查」统计量 `[R18]`。
   Bailey, Borwein, López de Prado & Zhu(2014,*Pseudo-Mathematics and Financial Charlatanism: The Effects of Backtest Overfitting on Out-of-Sample Performance*,
   Notices of the AMS 61(5))把这个问题讲得更极端:试的配置数越多,回测过拟合的概率越高,而且过拟合的策略在样本外**不是零收益,是负收益**(因为均值回复效应)`[R20]`。
   Bailey & López de Prado(2014,*The Deflated Sharpe Ratio: Correcting for Selection Bias, Backtest Overfitting and Non-Normality*,
   Journal of Portfolio Management 40(5))给出了具体的修正方法:把「零技能、独立重复 N 次」能达到的最高 Sharpe 期望值当作新的显著性门槛,
   而不是用零作为门槛 `[R21]`。Harvey, Liu & Zhu(工作论文 2014,NBER WP20592;正式发表 2016,*…and the Cross-Section of Expected Returns*,RFS 29(1))
   把同样的逻辑用在已发表的资产定价异象上,建议把 t 统计量门槛从常见的 2.0 提高到 3.0 `[R19]`;Novy-Marx(工作论文 2015,NBER WP21329,2016 年修订版
   *Testing Strategies Based on Multiple Signals*)进一步区分了「过拟合偏差」和「选择偏差」,后者可以单独放大前者,用 20 个候选信号里选 3 个最好的组合,
   偏差量级可以等同于从 1780 个候选里选 1 个最好的 `[R17]`。
   **翻译成警示**:这五篇**全部**是关于「候选数量越多、只报告最好的、显著性门槛就要越高」这条逻辑,**不是专门针对「用 min(train, valid) 这个特定统计量」的文献**。
   这个区分对我们很重要:min(train, valid) 本身是**用来对抗**单一样本内过拟合的一种保守化手段(只有两段都好才算数,比只看 train 更严),
   但上面这五篇共同指出的问题是——**这种保守化手段并不能对抗「候选数量」这个维度的选择偏差**:如果在 32 个个体、96 次评估里反复试,
   总会有某个随机结构碰巧让 train 和 valid 都不错,而这与「机制真实」无关。`analysis.md` §1.4 的发现(score 是多头那一档成员的函数,不是机制的函数)
   与这五篇文献的核心警示是同一件事的两个侧面:**样本内 / 验证集的选择门槛再严,都挡不住足够多候选带来的运气**,§4.0「库禁令是最紧的约束」这个判断,
   从文献角度看也可以读成「用去重 / 禁令限制有效候选数,是比提高单次门槛更治本的办法」,这条可以直接写进第 3 轮的审计默契。

---

## Q4(对准 H2 / H3 的方向矛盾与封板污染:涨跌停与停牌对「不动」类度量的制度性污染)

**(i)报价停滞 / 零收益类度量与跳跃 / 集中度类度量,文献认为是同一个机制的两面还是两件事?有没有同时放进横截面、看谁被谁吃掉的结果?**

1. **没有找到把两类度量同时放进同一个横截面检验、看谁解释谁的资产定价论文**(搜不到,见文末,与 Q1(iii) 第 6 条是同一个缺口)。
2. **相邻的高频统计文献(已见于 Q1(iii))把两者当操作上要分开处理的两件事,但没有正面回答「是不是同一个机制」**:Bonaccolto, Zambon & Caporin `[R6]`
   用零收益占比**筛掉**不可靠的交易日,再在剩下的日子上**做**跳跃检验——这个操作本身暗含「停滞和跳跃是两回事,但停滞会污染跳跃的测量」这个立场,
   而不是「停滞和跳跃是同一个机制的两面」。**翻译成警示**:这与 `analysis.md` §1.2(d)「停滞 ⇒ kurt 高」这条机械联动的担忧**不矛盾**,
   但文献给出的处理方式是**先过滤再测量**,不是「测出来再看哪个吃掉哪个」,所以 ρ(H2, H3) 这个数本身,文献帮不上忙,只能靠 corr 请求自己算。

**(ii)封板日和停牌日是剔除、单独当特征,还是不处理?涨跌停宽度不同的板块之间这类度量还可比吗?**

3. **三篇一致:保留事件,当独立的、带方向和强度的变量处理,不是直接剔除**(本次重新检索确认,链接与细节与 `r1/lit.md`、`r2/lit.md` 一致):
   Wan, Xie, Gu, Jiang, Chen, Xiong, Zhang & Zhou(2015-03 arXiv:1503.03548,2015-04 正式发表 PLOS ONE 10(4),*Statistical Properties and Pre-Hit Dynamics
   of Price Limit Hits in the Chinese Stock Markets*)按涨停 / 跌停分别统计次日延续概率,发现冷却效应而非磁吸效应 `[R22]`;
   Chen, Gao, He, Jiang & Xiong(2017-11 NBER WP24014,2019 正式发表 J. Econometrics 208(1),*Daily Price Limits and Destructive Market Behavior*)
   用涨停日大户净买入行为预测后续反转,并把 ST(5% 窄限制)股票单独拿出来做因果对照 `[R23]`;
   Wu, Wang & Li(2017,*Post-hit Dynamics of Price Limit Hits in the Chinese Stock Markets*,Physica A 465)发现开板后收益呈「W」形,
   连续触及涨跌停的天数长度本身是独立的影响因素 `[R24]`。**翻译**:这支持 §4.3 N-2 的建议——`LimitWidth` 和涨跌停触及应该做成缩放 / 分组 / 滚动计数变量,
   不是从 `day_flat_run_max`、`day_kurt` 这类连续特征的样本里直接剔除涨跌停日;文献里没有「直接剔除」这个处理方式的先例。
4. **宽度不同的板块之间不可直接比,这件事本身有量化证据,但「怎么归一」仍然搜不到**(与 `r2/lit.md` Q4(ii) 结论一致,本次重新检索确认):
   Zhang, Wang, Hao & He(2022,*Price Limit and Stock Market Quality: Evidence from a Quasi-Natural Experiment in the Chinese Stock Market*,
   Pacific-Basin Finance Journal 74)用创业板 2020-08-24 从 10% 放宽到 20% 的准自然实验做双重差分,发现放宽后同一批股票的流动性指标和知情交易概率显著上升 `[R25]`;
   Wan & Zhang(2022,*The Effect of Relaxing Daily Price Limit: Evidence from the ChiNext Market of China*,Economics Letters 215)用事件研究法做同一个变化,
   同样发现流动性显著改善、波动率显著上升,对价格效率没有显著影响 `[R26]`。**翻译成警示**:这两篇量化证明了「涨跌停宽度本身会机械地改变测得的流动性 / 波动类指标的读数」,
   如果把 ST(5%)、主板(10%)、创业板科创板(20%)的股票混在一起直接比较 `day_kurt`、`day_distinct_ratio`、`day_flat_run_max` 这类度量的绝对水平,
   相当于把一部分制度性噪声当成了经济信号。**但两篇都是「同一板块,制度改变前后」的纵向对照,没有找到给「横截面上不同宽度板块之间如何归一」提出显式方法的论文**(搜不到,见文末)。

**(iii)封板频率 / 开板后收益形状本身作为横截面特征,有没有被检验过?**

5. **没有找到把「过去 N 日封板次数」当独立横截面排序特征、直接检验其预测力的论文**(与 `r2/lit.md` 结论一致,本次重新检索未发现新结果,如实记录)。
   Wu, Wang & Li `[R24]` 测的是时间序列上「开板后」的收益动态形状(事件窗口内的条件期望),Chen et al. `[R23]` 同理是事件研究,都不是把封板频率本身
   当一个静态的横截面特征拿去给全市场排序;这与 §4.3 N-2「滚动计数当缩放 / 分组变量,而不是单独当 alpha 因子去挖」的建议方向一致,
   但这条界限本身没有文献可以直接引用去证明,是我们自己要做的方法论工作。

---

## 出处列表

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|---|
| R1 | Does Realized Skewness Predict the Cross-Section of Equity Returns? | Amaya, D.; Christoffersen, P.; Jacobs, K.; Vasquez, A. | 2011(工作论文)/ 2015-02(JFE 118,135-167) | Journal of Financial Economics | https://repec.econ.au.dk/repec/creates/rp/11/rp11_44.pdf | true |
| R2 | Econometrics of Testing for Jumps in Financial Economics Using Bipower Variation | Barndorff-Nielsen, O.E.; Shephard, N. | 2006(JFEctrics 4(1),1-30) | Journal of Financial Econometrics | https://ideas.repec.org/a/oup/jfinec/v4y2006i1p1-30.html | true |
| R3 | Jumps in Financial Markets: A New Nonparametric Test and Jump Dynamics | Lee, S.S.; Mykland, P.A. | 2008(RFS 21(6)) | Review of Financial Studies | https://www.scheller.gatech.edu/directory/research/finance/lee/pdf/leemykland08.pdf | true |
| R4 | Fact or Friction: Jumps at Ultra High Frequency | Christensen, K.; Oomen, R.; Podolskij, M. | 2011(CREATES RP 2011-19)/ 2014(JFE) | CREATES Working Paper / Journal of Financial Economics | https://repec.econ.au.dk/repec/creates/rp/11/rp11_19.pdf | true |
| R5 | Systemic Co-Jumps | Caporin, M.; Kolokolov, A.; Renò, R. | 2016(SAFE WP 149)/ 2017-07(JFE 126(3),563-591) | SAFE Working Paper / Journal of Financial Economics | https://www.research.unipd.it/bitstream/11577/3249256/4/2017_CaporinKolokolovReno_JFE_PostPrint.pdf | true |
| R6 | Systemic Events and Diffusion of Jumps | Bonaccolto, G.; Zambon, N.; Caporin, M. | 2018(第 50 届意大利统计学会年会会议论文) | SIS 50th Scientific Meeting Proceedings | https://meetings3.sis-statistica.org/index.php/sis2018/50th/paper/download/1097/70 | true |
| R7 | Maxing Out: Stocks as Lotteries and the Cross-Section of Expected Returns | Bali, T.G.; Cakici, N.; Whitelaw, R.F. | 2009-03(NBER WP14804)/ 2011(JFE 99(2),427-446) | NBER Working Paper / Journal of Financial Economics | https://ideas.repec.org/a/eee/jfinec/v99y2011i2p427-446.html | true |
| R8 | A Tug of War: Overnight Versus Intraday Expected Returns | Lou, D.; Polk, C.; Skouras, S. | 2014(首次流通,LSE/FMG DP744)/ 2019(JFE) | FMG Discussion Paper / Journal of Financial Economics | https://personal.lse.ac.uk/polk/research/TugOfWar.pdf | true |
| R9 | Paying Attention: Overnight Returns and the Hidden Cost of Buying at the Open | Berkman, H.; Koch, P.D.; Tuttle, L.; Zhang, Y.J. | 2012(JFQA 47(4),715-741) | Journal of Financial and Quantitative Analysis | https://ideas.repec.org/a/cup/jfinqa/v47y2012i04p715-741_00.html | true |
| R10 | Stock Return Variances: The Arrival of Information and the Reaction of Traders | French, K.R.; Roll, R. | 1986(JFE 17(1),5-26) | Journal of Financial Economics | https://www-2.rotman.utoronto.ca/~kan/3032/pdf/AssetPricingAnomalies/French_Roll_JFE_1986.pdf | true |
| R11 | A Reduced Form Framework for Modeling Volatility of Speculative Prices Based on Realized Variation Measures | Andersen, T.G.; Bollerslev, T.; Huang, X. | 2007(CREATES RP 2007-14)/ 2011(J. Econometrics 160(1),176-189) | CREATES Working Paper / Journal of Econometrics | https://repec.econ.au.dk/repec/creates/rp/07/rp07_14.pdf | true |
| R12 | The Overnight Return Puzzle and the "T+1" Trading Rule in Chinese Stock Markets | Qiao, K.; Dam, L. | 2020(JFM 50,100534) | Journal of Financial Markets | https://ideas.repec.org/a/eee/finmar/v50y2020ics1386418120300033.html | true |
| R13 | Marketability As Real Options: The Cross Sectional Variation of Overnight Returns in China | Bai, H. | 2020-01(工作论文,SSRN 2020-03 发布,abstract_id=3513658) | SSRN Working Paper | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3513658 | true |
| R14 | The Role of Shorting, Firm Size, and Time on Market Anomalies | Israel, R.; Moskowitz, T.J. | 2013(JFE 108(2),275-301) | Journal of Financial Economics | https://ideas.repec.org/a/eee/jfinec/v108y2013i2p275-301.html | true |
| R15 | Empirical Asset Pricing: The Cross Section of Stock Returns | Bali, T.G.; Engle, R.F.; Murray, S. | 2016-04 | Wiley | https://mitpressbookstore.mit.edu/book/9781118095041 | true |
| R16 | Measuring Mutual Fund Performance with Characteristic-Based Benchmarks | Daniel, K.; Grinblatt, M.; Titman, S.; Wermers, R. | 1997-07(JF 52(3)) | Journal of Finance | https://ideas.repec.org/a/bla/jfinan/v52y1997i3p1035-58.html | true |
| R17 | Testing Strategies Based on Multiple Signals | Novy-Marx, R. | 2015-07(NBER WP21329)/ 2016-03(修订版) | NBER Working Paper | https://www.nber.org/papers/w21329 | true |
| R18 | A Reality Check for Data Snooping | White, H. | 2000-09(Econometrica 68(5),1097-1126) | Econometrica | https://users.ssc.wisc.edu/~bhansen/718/White2000.pdf | true |
| R19 | …and the Cross-Section of Expected Returns | Harvey, C.R.; Liu, Y.; Zhu, H. | 2014-10(NBER WP20592)/ 2016(RFS 29(1),5-68) | NBER Working Paper / Review of Financial Studies | https://www.nber.org/papers/w20592 | true |
| R20 | Pseudo-Mathematics and Financial Charlatanism: The Effects of Backtest Overfitting on Out-of-Sample Performance | Bailey, D.H.; Borwein, J.M.; López de Prado, M.; Zhu, Q.J. | 2014-05(Notices of the AMS 61(5),458-471) | Notices of the American Mathematical Society | https://scholarworks.wmich.edu/math_pubs/40/ | true |
| R21 | The Deflated Sharpe Ratio: Correcting for Selection Bias, Backtest Overfitting and Non-Normality | Bailey, D.H.; López de Prado, M. | 2014(Journal of Portfolio Management 40(5),94-107) | Journal of Portfolio Management | https://papers.ssrn.com/abstract=2460551 | true |
| R22 | Statistical Properties and Pre-Hit Dynamics of Price Limit Hits in the Chinese Stock Markets | Wan, Y.-L.; Xie, W.-J.; Gu, G.-F.; Jiang, Z.-Q.; Chen, W.; Xiong, X.; Zhang, W.; Zhou, W.-X. | 2015-03(arXiv:1503.03548)/ 2015-04(PLOS ONE 10(4)) | arXiv / PLOS ONE | https://arxiv.org/pdf/1503.03548 | true |
| R23 | Daily Price Limits and Destructive Market Behavior | Chen, T.; Gao, Z.; He, J.; Jiang, W.; Xiong, W. | 2017-11(NBER WP24014)/ 2019-01(J. Econometrics 208(1)) | NBER Working Paper / Journal of Econometrics | https://www.nber.org/papers/w24014 | true |
| R24 | Post-hit Dynamics of Price Limit Hits in the Chinese Stock Markets | Wu, T.; Wang, Y.; Li, M.-X. | 2017(Physica A 465,464-471) | Physica A: Statistical Mechanics and its Applications | https://ideas.repec.org/a/eee/phsmap/v465y2017icp464-471.html | true |
| R25 | Price Limit and Stock Market Quality: Evidence from a Quasi-Natural Experiment in the Chinese Stock Market | Zhang, X.; Wang, Z.; Hao, J.; He, F. | 2022(Pacific-Basin Finance Journal 74,101778) | Pacific-Basin Finance Journal | https://ideas.repec.org/a/eee/pacfin/v74y2022ics0927538x22000737.html | true |
| R26 | The Effect of Relaxing Daily Price Limit: Evidence from the ChiNext Market of China | Wan, X.; Zhang, J. | 2022(Economics Letters 215,110509) | Economics Letters | https://ideas.repec.org/a/eee/ecolet/v215y2022ics0165176522001318.html | true |

**搜了但没有可独立核实的文献(或日期不合规),不编、如实列在这里(不算出处):**

- 直接用「跳跃变差占比(jump variation share)÷已实现四次幂变差」这个具体比值构造横截面特征、并检验定价能力的资产定价论文(Q1(i))。
- 把「峰度 / 跳跃集中度」类度量与「零收益占比 / 报价停滞」类度量同时放进同一个横截面检验、看谁被谁吃掉的资产定价论文(Q1(iii)、Q4(i),两问是同一个缺口)。
- Kolokolov & Renò,*Jumps or Staleness?*(Journal of Business & Economic Statistics 42(2),2024,正面回答「零收益 / 报价停滞会系统性扭曲跳跃检验」,
  与本轮 Q1(iii)/Q4(i) 高度对题),但正式发表年份是 2024,且查不到更早的、可独立核实日期的工作论文版本(DOI 前缀含 2023,但未能确认「网络首发」具体月份是否早于
  2023-08-08),按规则「拿不准日期的不用」,**不计入出处列表**,如实记录于此,供下一次(如果还有机会)复核。
- 「开盘集合竞价剔除前后,高频矩(方差 / 偏度 / 峰度)计算结果具体差多少」的量化对照论文(Q2(ii))。
- 用「隔夜 / 日内方差占比」这个具体构造、同时系统控制流动性、规模、关注度的 A 股定价检验论文(Q2(iii))——已有的两篇 A 股证据(Qiao-Dam、Bai)都是用带符号隔夜收益,
  不是方差占比。
- Sobotka,*The Intersection of Expected Returns*(2025 年工作论文,跨 164 个异象的十分位重叠研究,核心发现与 Q3(i) 高度对题:
  一小部分「重叠股」贡献了远超其持仓占比的异象收益),但首版日期(2025)晚于 2023-08-08,**不计入出处列表**,如实记录于此。
- 直接针对「两个秩相关 0.9 的特征,其最高十分位可以差三分之一成员」这一具体现象、且日期合规的资产定价论文(Q3(i))。
- 名为「组内中位数检验」的独立命名诊断方法(Q3(ii))——双重排序和特征调整收益(DGTW)是找到的标准工具,但这个具体名字没有找到对应文献。
- 专门给「横截面上,不同涨跌停宽度板块(主板 / 创业板科创板 / ST)之间如何把零收益 / 停滞 / 集中度类指标调整到可比口径」提出显式归一方法的论文(Q4(ii))——
  只找到「同一板块放宽前后对照」的准自然实验(`[R25]`、`[R26]`),没有找到跨板块横截面归一的方法论文献。
- 把「过去 N 日封板次数」当作独立的横截面排序特征(而非事件窗口条件变量)直接检验其预测力的论文(Q4(iii))。

---

## 给核心 / R 变体的直接翻译(摘要,方便 PI、结构解剖员、审计员对表)

- **核心 1(`day_kurt(Ret)`)的量纲论证,文献给了最硬的方法论支持**:Barndorff-Nielsen & Shephard(2006)`[R2]` 确认跳跃检验的标准做法本身就是构造
  一个「分子四阶矩 / 分母二阶矩」式的无量纲比值,而不是按波动分组或残差化——`analysis.md` §1.2(a) 的量纲论证不是我们自己的特例辩护,是这支文献的标准做法。
- **`day_kurt(Ret)` 本身当横截面特征(而不是先做跳跃检验),文献里有直接先例且方向一致**:Amaya-Christoffersen-Jacobs-Vasquez(2015)`[R1]` 的已实现峰度
  与下周收益正相关,方向与 H3 的 sign=+1(多头腿是 kurt 最低的票)一致,但**显著性比已实现偏度弱得多**——不要把这条读成「峰度溢价已被文献证实很强」。
- **R 第 1 组第 3 颗(剥掉 09:30 竞价)是本轮最该买的一次评估,文献支持它的必要性而不是替代它**:Lee & Mykland(2008)`[R3]` 的逐日定位思路说明
  「剥掉第 0 列再比较」是一个比「逐日定位触发 bar」更粗糙但更便宜的版本,方向一致,分辨率更低,这件事要如实告诉审计。
  Christensen-Oomen-Podolskij(2014)`[R4]` 提醒:峰度类度量容易把「波动集中爆发」误读成「单点跳跃」,这是 §1.2(e) 风险清单该补的一条机制,不只是「与停滞族机械耦合」。
- **零收益占比与峰度 / 跳跃集中度「是不是同一个机制」,文献里没有正面答案,只有操作性的旁证**:Bonaccolto-Zambon-Caporin(2018)`[R6]` 和其底层的
  Caporin-Kolokolov-Renò(2017)`[R5]` 把高零收益占比的日子**过滤掉**再测跳跃,不是条件化排序——这支持 R 第 1 组第 4 颗做这个实验的价值(前所未有的数据点),
  但不能预判结果;**ρ(H2, H3) 和两者各自与控制的 ρ,仍然只能靠 corr 请求自己算,文献帮不上忙。**
- **N-1(开盘竞价方差占比)的构造,文献给出了明确的方法论先例**:Andersen-Bollerslev-Huang(2011)`[R11]` 把隔夜方差当一个独立于日内跳跃方差的
  第三个成分单独建模,支持把 `day_first(Ret)` 的方差占比写成一个全新的轴而不是 `day_kurt` 的分解项;但「不剔除竞价对矩计算的具体影响有多大」、
  「方差占比与流动性 / 规模 / 关注度的系统控制」这两块,搜索范围内都没有可用的量化文献,§4.3 N-1 引用文献时要把这两条降级成「我们自己要做的检验」。
  A 股隔夜收益的两篇证据(Qiao-Dam `[R12]`、Bai `[R13]`)进一步确认**带符号**隔夜收益与 T+1、反转纠缠很深,支持用**方差占比**而不是带符号收益,
  但这是「避开已知的脏变量」,不是「文献验证过占比有效」。
- **§1.4 的核心教训(score 是多头那一档成员的函数,不是机制的函数),文献给出的是同一问题的「候选数量」版本,不是「两段取较差值」版本**:
  White(2000)`[R18]`、Harvey-Liu-Zhu(2016)`[R19]`、Novy-Marx(2016)`[R17]`、Bailey 等人的两篇(2014)`[R20][R21]` 全部指向
  「候选越多、只报告最好的,显著性就要越严」,min(train, valid) 是对抗单样本过拟合的保守化手段,**挡不住候选数量维度的选择偏差**——
  这支持 §4.0「库禁令是比提高单次门槛更治本的办法」这个判断,可以直接写进第 3 轮的审计默契,但不要说成「文献验证了 min(train,valid) 这个具体统计量」。
- **「新 H2 的 +0.345 是不是重新带回来的规模倾斜」,文献给出的是方法论对照而非数字答案**:Bali-Engle-Murray(2016)`[R15]` 的双重排序和
  DGTW(1997)`[R16]` 的特征调整收益,是诊断「低线性相关、高非线性暴露」的两种标准工具,支持 §4.2 R 第 2 组第 1 颗(配完再按市值重新中性化)的方向,
  但文献本身给不出「+0.345 有多少是干净的、多少是规模」这个具体数字,**这件事仍然只能靠那次 R 评估自己钉死**。
- **涨跌停三篇(`[R22][R23][R24]`)和跨板块宽度两篇(`[R25][R26]`)重新检索确认不变**:保留事件、当独立变量处理,不剔除;不同宽度板块的「不动」类
  读数不可直接比,但没有文献给出显式归一公式——这两条结论与第 1、2 轮一致,支持 §4.3 N-2 的建议,也支持「别把 `LimitWidth` 当分母去归一化,
  当调节变量去交互」这条路线继续往下走。
