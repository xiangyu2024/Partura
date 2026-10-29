# 文献:种子 802,C 组,第 2 轮

对准 `analysis.md` §5 的四个题目:
L1/L2 对准**核心 1**(订单流残差,`day_signed_ratio(Ret,Volume)` 一类净主动买入比,配 `cs_last_*` 测量质量筛);
L3 对准**灵感 1**(`ts_delta(LogFloatShares, 241)` = 流通股本一年增量 = 解禁/摊薄供给冲击);
L4 对准**核心 2**(`day_durbin_watson(Volume)` 的凸变换 + `ts_decay_linear` + 横截面排序,等价于「最近极端日」,以及 M 第 2 批最高分 head 的滚动 regbeta 窗口)。
工具:WebSearch / WebFetch(本轮已加载)。**只用 2023-08-08 之前发表/提交的文献**;arXiv / SSRN 按首版(v1 / 最早 Posted)日期计。日期拿不准的条目已明确标注,不计入任何处理方式的证据。
下面每条处理方式后的 `[S#]` 对应文末出处表;`verified: true` 表示本次搜索结果文本或抓取到的页面上确实看到了该文献的标题/作者/年份/场所(至少一项被直接看到),不是凭记忆写的。

---

## L1:核心 1——订单流残差的测量误差与持有期

搜索关键词:order imbalance, tick rule, Lee-Ready misclassification, bulk volume classification, Chordia-Subrahmanyam, order imbalance China A-shares, retail vs institutional order flow。

### (a) 零收益/无成交分钟怎么处理,薄盘股的符号分类误差

1. **我们现在算的东西,严格说不是 Lee-Ready,是对分钟 bar 做「tick rule」。** Lee-Ready(本身没有搜到可独立核实的原文,只在后续文献的引用里反复出现)需要买卖报价中点,逐笔分类;没有报价时才退回 tick rule(按价格涨跌判断方向)。我们的环境只有分钟 OHLCV,没有报价和逐笔成交,所以 `sign(r)` 这个做法天然就是纯 tick rule,而不是 Lee-Ready——这一点本身文献没有否定,但意味着我们要对标的误差文献是「tick rule 在不活跃/低价股上的误判」,不是报价滞后那一类 Lee-Ready 特有的误差来源。
2. **零收益分钟(`r=0`,tick rule 打平)不是文献里的冷门问题,而是整条「交易分类准确性」文献的标准检验对象之一,而且误判率在小单、低价股、报价/成交稀疏时系统性更高。** Aktas & Kryzanowski(2014)在伊斯坦布尔交易所的逐笔数据上直接测了这件事:误判率随成交量变小、成交间隔变短而**上升**,且开盘后 30 分钟与收盘前 30 分钟的误判率高于盘中 [S14]。Odders-White(2000)、Theissen(2001)、Finucane(2000)、Lee & Radhakrishna(2000,TORQ 数据)是这条文献线上反复被引用的几篇,专门检验 Lee-Ready/tick 规则的误判发生率与后果,但本次搜索只拿到了它们的标题/期刊/卷期,没拿到可独立核实的具体误判率数字 [S9][S10][S11]。
   → 翻译:这支持"用 `day_zero_ratio(Ret)` 或类似的零收益分钟占比,以及分钟笔数/成交稀疏度,去做一个独立的测量质量筛"(即 §4.1 核心 1 外围里 PI 已经想到的方向),而不是指望中性化或残差化能把这层误差去掉——这层误差是方向误判,不是幅度偏差,线性操作去不掉。
3. **当没有逐笔数据、只能按「一段时间内的量」分配方向时,标准做法是概率性分配(BVC),不是把前一个有效 tick 的符号强行带过来。** Easley, López de Prado & O'Hara(2016)与 Chakrabarty, Pascual & Shkilko(2015)系统比较了 Bulk Volume Classification(按价格变化的标准化幅度,把一个 bar 的成交量按正态分布概率拆成买/卖两部分)与 tick rule/Lee-Ready:tick rule 在识别"主动方"上总体不差,但 BVC 与知情交易代理的相关性更好,且不依赖逐笔符号的连续性假设 [S13][S12]。
   → 翻译:如果要在算子里处理「全天均价不变/零收益」这类 bar,比起让 `sign(r)` 在 r=0 处继续沿用上一分钟的符号(等价于人为制造正自相关),更贴近文献的做法是让这些分钟**对分子贡献为零、只进分母**(当前写法如果是这样,是对的;如果是「前值填充」,则是在制造一个文献里专门被当作误判来源的伪持续性)。
4. **Easley-O'Hara 的结构模型本身提醒:信息不是只藏在方向里,也藏在"有没有成交"和"多大的单"里。** Easley & O'Hara(1987)证明大单本身携带信息,做市商对大单天然定价更宽 [S7];Easley, Kiefer, O'Hara & Paperman(1996)把这个思路做成 PIN,用交易到达率(而不是方向本身)反推知情交易概率 [S8]。
   → 这条不是直接可改的算子,但提示:如果残差化之后还想再提纯,「笔数/到达率」是比「再换一种符号规则」更有信息增量的方向——不过本环境没有逐笔笔数字段,目前做不了,只记作远期方向。

### (b) 按集中度/笔数/零收益占比筛选再做横截面检验

5. **没有搜到"先按零收益占比/成交集中度筛掉一批股票、再做横截面检验"这个具体操作流程的直接先例。** (a) 里的几篇准确性文献都是在**个股时间序列**上评估误判率,不是把误判率本身当筛选变量去跨股票分组。Barclay & Warner(1993)的 stealth trading 假说提示"中等单量最有信息"[S15,沿用第 1 轮已核实],间接支持"用集中度分组"这个方向有道理,但不是同一个操作。

### (c) 订单不平衡对收益取残差后,预测未来收益的最优持有期/平滑长度

6. **持有期证据分段且不单调,我们现在的「20 日 < 40 日 < 20+40 两层衰减」这个发现只在某一段horizon上成立,文献里不支持无限往长走。**
   - 日内/分钟级:一篇较早的盘中研究发现订单不平衡的预测力在**30 分钟内**就消失,原因是反向交易者介入抵消 [S3 相关引用,来自搜索摘要,未独立确认作者]。
   - 日度/周度:Chordia & Subrahmanyam(2004)本身的机制就是"滞后不平衡对当日收益有正向关系,但一旦控制当期不平衡,这个关系会反转"——即价格压力本身是**短期、会被下一期部分抵消**的东西 [S1]。Kaniel, Saar & Titman(2008)在周/月频率上发现个人净交易预测**下一月**的正超额收益 [S3]。
   - 周到年之间出现**方向反转**:Barber, Odean & Zhu(2009)用小单不平衡代理个人投资者交易,发现**周度**上买方不平衡预测下周**更高**收益(延续),但**年度**上买方不平衡预测未来一年**更低**收益(反转,买超的跑输卖超的 4.4 个百分点)[S4]。
   - Barber, Lin & Odean(《Resolving a Paradox》,SSRN 首次提交 2021-02-18)在更长的样本上重新确认"小单不平衡持续正向预测收益",但同时发现这个预测力集中在被关注、被过度买入的股票上,这些股票本身跑输,所以"不平衡预测收益为正"和"跟着这个信号交易不赚钱"可以同时成立 [S5]。
   - **结论**:文献里确实存在"从日到月是延续"的证据(支持我们 20 日/40 日两层衰减比单纯用 1 日更好),但**没有任何文献支持"越往长走越好"这个单调性能无限延伸**——反而在年度尺度上出现方向反转。这是一个可以直接检验的预测:如果 PI 真的把平滑窗口再往上堆(比如加第三层 80 日或更长),按 Barber-Odean-Zhu 的证据,**不应该**期待分数继续单调上升,中间大概率存在一个从"延续"切换到"反转"的转折点,第 1 轮文献员在另一个核心上也发现过类似的"记忆有自然边界"模式(Heston-Korajczyk-Sadka 的约 40 个交易日)。

### (d) 方向:A 股是"买方不平衡之后收益更高"还是相反?

7. **市场整体层面,我们 train 给出的 sign(=做多被吸收的买压)与 Chordia-Subrahmanyam(2004)的美股方向一致**,但这不是中国市场的直接证据——Shenoy & Zhang(2007)专门做了"中国的订单不平衡与股票收益",是本次搜到的最直接对口文献,但只拿到了标题/期刊/卷期(QREF 47(5), 637-650),**没有拿到摘要,无法确认其报告的方向**,诚实记录为未核实到结论 [S2]。
8. **但方向可能依赖于"谁在失衡",这是本次搜索里最重要的 A 股新证据。** Jones, Shi, Zhang & Zhang(《Understanding Retail Investors: Evidence from China》,ABFER 2022 年会版本,首版 2019-09)用 2016–2019 的账户级数据发现:**大额**散户和机构的净交易通常**正向**预测未来收益(与 Chordia-Subrahmanyam 方向一致),但当它们与**小额**散户同向交易时,这个预测关系会**转负**;小额散户自身的净交易呈现日度动量模式,且是在用流动性(immediacy),不是提供流动性 [S6]。
   → 这给核心 1 一个可操作的细化方向:同一个"净主动买入比"信号,方向的稳健性可能**取决于这只股票当天的成交是被谁主导的**(机构/大户 vs 小额散户),而我们现在的残差是不区分参与者结构、全市场混在一起算的。这是文献给出的、而我们完全没用到的一条增量信息,但目前环境里没有账户级字段,**做不了**,只记作结论性背景:如果 E 位的候选在"成交被少数大户主导"和"被大量小额散户主导"的子样本上表现不一致,那正好对应 Jones et al. 的发现,而不是我们管线出了问题。

### 缺口(搜不到,诚实记录)

- 没有搜到任何文献直接给出"Lee-Ready/tick rule 在中国 A 股低价股/薄盘股上的误判率"这个具体数字——(a)的几篇准确性研究全部是美股或土耳其 BIST 样本。
- 没有搜到"先按零收益占比/集中度筛选、再做横截面订单不平衡检验"这个具体操作流程的直接先例((b)第 5 条)。
- 没有拿到 Shenoy & Zhang(2007)关于中国市场方向的具体结论,只核实了其存在和出处((d)第 7 条)。

---

## L2:核心 1 外围——把"排除筛"当因子构造的一个部件

搜索关键词:penny stock filter, liquidity screens, intraday volume concentration, informed trading, conditional screen vs standalone factor, Lee-Swaminathan volume momentum。

### (a) 低价股/流动性筛通常怎么设:百分位还是绝对门槛

1. **两种设定方式在文献里都存在,但"学术主流"更偏向横截面百分位,不是绝对价格门槛。** Fama & French 在《Dissecting Anomalies》里用 NYSE 市值的 20 分位/50 分位做 micro/small/big 分组,不是绝对市值或价格门槛(本次搜索只拿到这个方法论描述,未独立核实具体数字,标注为来自搜索摘要)。与之相对,SEC 对 penny stock 的定义是绝对价格 <$5,一些后续研究(如 Erasmus 大学的本科论文、华沙交易所研究)直接套用这个绝对门槛 [均来自搜索摘要,未独立确认作者,不计入出处表]。
2. **按换手率筛选,是一条更直接可比的先例。** Novy-Marx & Velikov(2016)按月度单边换手率筛选 23 个因子策略,换手率低于 50% 的大多数策略在考虑交易成本后仍显著;其方法是分组报告而不是设一个全局绝对阈值 [S18]。
   → 翻译:我们现在用 `cross_quantile_q25` 这类横截面分位数做筛(core 1 第 2 核心里 `cross_quantile_q25(LogFloatShares, 241)`,以及 §4.1 核心 1 候选的几个筛),比起绝对阈值,**更贴近 Fama-French 式的学术主流做法**,这是一个可以在给审计员的合理性说明里直接引用的点,而不是只有"数据驱动"的理由。

### (b) 成交集中度在文献里被当成什么:知情交易?流动性不足?还是测量不可靠?

3. **三种解读都存在,而且互相矛盾,文献没有定论——这正好支持"它更适合当筛,不适合单独当因子"的判断。**
   - **知情交易侧**:Black(2023)的 trade-time clustering 测度结合成交量与成交间隔,报告聚集度越高,知情交易越强 [来自搜索摘要,标题/作者/年份已直接看到,但未独立确认期刊卷期,降级不计入出处表核实];Easley, López de Prado & O'Hara(2016)认为 BVC 类聚集度测度与知情交易代理的相关性好于逐笔分类规则 [S13]。
   - **流动性不足/呆滞价格侧**:第 1 轮文献员已经核实过,"零收益天数占比"在经典文献里是和 Amihud 价格冲击、换手率并列检验的流动性代理,不是独立因子(沿用第 1 轮 [S5][S6][S7])。
   - **测量不可靠侧**:本轮(a)部分的 Aktas & Kryzanowski(2014)把"成交稀疏、单量小"直接对应到交易分类**误判率上升**,也就是"统计量不可信"[S14]。
4. **Barclay & Warner(1993)的 stealth trading 假说给出一个具体的非单调结构:信息集中在中等单量,不在最大也不在最小的单子上**(第 1 轮已核实,沿用 [S15])。这意味着"成交集中在少数分钟"本身不是一个单调的知情/不知情信号,而是要看集中在哪个量级的单子上——我们现有的 `day_gini(Volume)` / `day_max(Volume)` 只看量的分布形状,不区分大中小单,这是文献给出的一个尚未被我们利用的维度,但环境里没有分钟级笔数/单均量字段,记作远期方向。

### (c) 有没有文献明确说"单独当因子没用、当筛选条件有用"

5. **有一个很贴切的先例:Lee & Swaminathan(2000)的"动量生命周期"(MLC)。** 过去成交量本身不是一个被广泛证实的独立收益预测变量,但它强烈**决定**价格动量的强度和持续时间——高成交量的赢家/输家反转得更快,低成交量的更慢,成交量被用来给个股在"受追捧/被忽视"周期里定位,而不是直接排序 [S17]。
6. **但这个先例自带一个必须诚实报告的警告。** 后续批评(Chen, Chou, Hsieh & Rhee,"Momentum life cycle, revisited",本次搜索只拿到标题和研究机构页面,年份与具体期刊未独立核实,不计入出处表)认为 MLC 这个"成交量 × 动量"交互效应,很大程度上只是把两个已经分别被证实的效应(动量本身、换手率本身)**相乘**出来的机械产物,不是真正的新机制。
   → 这对我们的"筛"有直接警示意义:§4.1 分析里已经诊断出 `cs_last_high10(cross_quantile_q25(LogFloatShares,241), day_gini(Volume))` 这类结构,"筛" `day_gini(Volume)` 单独 −3.67,`y` 单独 +0.558,合起来 +1.089——如果这纯粹是两个已知弱效应的乘积(数字游戏),而不是"测量质量真的在改善 y 的信噪比",就正好对应 Lee-Swaminathan 被批评的那种机械交互。§4.2 A 组的 R 变体(把筛迁到其他 y 上)正是检验"是机制还是乘积游戏"的正确方法,文献上的这条批评进一步说明这个检验是必要的,不是多余的审慎。

### 缺口

- 没有搜到任何文献直接做过"同一个指标,单独当因子表现差,但当筛选/分桶条件时显著改进另一个信号"的**横截面资产定价**对照实验(Lee-Swaminathan 是动量场景下最接近的,但不完全是同一个问题设定)。
- 没有搜到针对"分钟级成交量基尼系数"本身的任何横截面因子或筛选研究——这与第 1 轮 L2 的缺口一致,说明这个具体统计量在构造粒度上仍然是新的。

---

## L3:灵感 1——流通股本增量 = 解禁/摊薄的供给冲击

搜索关键词:lockup expiration, IPO lockup expiry price pressure, seasoned equity offering share supply, split-share structure reform China, float increase and returns。

### (a) 怎么构造:比例、对数变化、还是事件哑变量,窗口多长

1. **美股文献几乎全部用"事件窗口"框架,不是连续的对数变化量。** Field & Hanka(2001,约 3000 个 IPO)把解禁日当成一个确定性已知的事件,测量解禁当周的异常收益(约 −2%),窗口是以解禁日为中心的几天到几周 [S19]。Ofek & Richardson(2000)用 1948 个解禁样本,测到解禁时成交量永久性增加约 40%,三日异常收益约 −1.5%,窗口同样是解禁日前后几天 [S20]。
2. **中国的研究因为股改的制度背景(非流通股占比一度高达 60%–80%),用的窗口比美股宽得多,而且更接近连续过程而不是单点事件。** Liao, Liu & Wang(2011,正式发表前工作稿 2008–2009)用 **[-120, +20]** 交易日的宽窗口,测到 482 次解禁的平均异常收益约 **−14%**,异常成交量约 **+140%**,且异常收益的大部分发生在解禁日**之前**约 40 天就开始累积,不是解禁当天跳变 [S21]。
3. **也有中国文献直接把解禁构造成一个连续的"可交易性价值"状态变量,而不是 0/1 哑变量。** 刘娥平、唐舜(2014,《财经研究》)基于期权定价模型提出"可交易性折扣"假说:限售期越短,流通股的可交易性价值越低,解禁本质上是可交易性价值从流通股向限售股**连续转移**的过程;其构造方式更接近把"距解禁还有多久/已解禁多少"当一个连续变量,而不是解禁日哑变量 [S22]。
   → 翻译:`ts_delta(LogFloatShares, 241)`(一年期的对数变化量)在构造粒度上**更接近刘娥平、唐舜的连续状态变量**,而不是 Field-Hanka/Ofek-Richardson/Liao-Liu-Wang 那种"以解禁日为中心的窄窗口事件研究"。这意味着:如果这条 N 的 idea 真的捕捉到了供给冲击,它量的是"过去一年总共摊薄了多少",不是"精确定位某一次解禁事件",**这是比标准事件研究更粗的构造,好处是不需要知道精确解禁日期(我们的数据里也没有这个字段),代价是会把多次解禁、渐进式减持混在一个滚动差分里**,这一点在写给 PI/审计员的机制说明里应该明确承认,而不是暗示它等价于标准解禁事件研究。

### (b) 方向和时点:价格压力(临时)还是信息(持久)

4. **美股证据总体偏向"持久",不是"临时反弹"。** Field & Hanka(2001)的一个核心结论是解禁后的价格下跌**不会在随后几周反弹**,他们据此认为这不是简单的临时供需失衡(价格压力假说),而更接近信息/定价的永久调整;他们也发现即使没有可观察到的内部人卖出,跌幅依然存在,价差也没有显著走阔 [S19]。
5. **中国证据也偏向"解禁前消化、解禁后小幅修复",不是纯粹的事件冲击后反转。** Liao, Liu & Wang(2011)把这个过程定性为"价格发现"——解禁本身在逐步缩小流通股东与非流通股东之间的信息不对称,而不是单纯的卖压 [S21]。刘娥平、唐舜(2014)报告"解禁前累计异常收益持续下降,解禁后小幅回升"——也就是主跌段在消息被定价的过程里(解禁前),解禁后只有部分、不完全的修复 [S22]。
   → 两条证据合起来支持:如果 `ts_delta(LogFloatShares, 241)` 真的在捕捉这个机制,它应该更像"持续的、提前反应的"信号,而不是"解禁当天跳一下随后修复"的信号——这和它用 241 日(约一年)这个慢变量的构造方式是一致的。

### (c) 中国市场的直接证据

6. 除(a)(b)已引用的 Liao-Liu-Wang(2011)[S21]与刘娥平、唐舜(2014)[S22]外,搜索还找到 Beltratti, Bortolotti & Caccavaio 的 FEEM 工作论文《Stock Prices in a Speculative Market: The Chinese Split-Share Reform》(2009),以及上海交通大学学报上一篇关于 IPO 解禁对中国股市流动性影响的研究(报告价差与非流动性在解禁前后显著上升,信息披露质量越高、影响越小)。这两篇本次只核实到标题/机构/大致年份,没有拿到可独立核实的具体数字,不计入出处表,仅作背景提示。

### (d) 怎么把这个量和市值/价格水平/上市年龄分开

7. **这是本轮最大的一个"缺口",而且是对 PI 分析里陷阱判断的一个重要限定。** 本次搜索到的所有解禁文献(美股和中国),控制价格水平/规模效应的方式清一色是**事件研究的匹配基准**(用规模/行业匹配的对照组计算异常收益)或者**横截面分组报告**(按是否有 VC 背书、是否为科技股分组),**没有一篇**显式地把"流通股本变化"从"价格水平"里用回归残差的方式分开。换句话说,§4.1 分析里提出的"`LogFloatShares = LogFloatCap − log(价格)`,中性化控制了市值而没控制价格"这个诊断,**是我们自己从数据结构推出来的,不是文献里已经做过、可以直接引用的标准做法**。A4/A5 这两个判决性诊断(把 y 换成 `LogFloatCap` 或 `day_quantile_q25(Open)`)因此是一次真正意义上的新检验,不是在验证文献已有的结论,这件事本身值得写进给审计员的合理度说明——它提升的是"机制清楚、算子实现了它"这一档,但"文献证据"这一档拿不到,因为文献没有专门做过这个分解。

### (e) 锁定期到期与上市年龄的机械关系

8. **没有搜到任何文献直接把"上市年龄"当解禁的工具变量或分组变量使用。** Field & Hanka(2001)讨论了锁定期长度(多数 180 天)本身的变化,但没有用上市年龄做分组;中国的一年/三年强制锁定期规则(大股东三年、其他股东一年)在本次搜索的中国文献里是背景制度介绍,没有一篇把 `ListAge` 当成一个显式的解禁时点代理变量去回归。这与 §4.3 N1 里"和 ListAge 的天然交互"的提法一样,是一个**没有文献先例、需要我们自己验证数据里是否成立**的假设,不是已验证的结论。

### 缺口(诚实记录)

- 没有拿到 Ofek & Richardson(2000)关于"哪些假说被拒绝、哪些部分解释了异常收益"的具体清单,只核实了核心数字(1%–3% 跌幅,40% 放量)。
- 没有搜到把"流通股本变化"从"价格水平/规模"中用回归残差方式分开的解禁文献(见(d)第 7 条,这是本轮最重要的一条缺口)。
- 没有搜到用上市年龄做解禁工具变量/分组变量的文献(见(e)第 8 条)。

---

## L4:核心 2——"最近的极端日"类因子,与 M 第 2 批最高分 head 的滚动 regbeta 窗口

搜索关键词:MAX effect, lottery-like stocks, idiosyncratic volatility puzzle, realized skewness, rolling beta window length, Bali-Cakici-Whitelaw。

### (a) "过去一个月最大单日收益/波动"类因子的横截面证据,中国市场是否存在

1. **美股证据非常直接,而且方向是我们需要注意的:MAX 越高,未来收益越低(不是越高)。** Bali, Cakici & Whitelaw(2011)用过去一个月的单日最高收益作为 MAX 代理,发现最高 MAX 组比最低 MAX 组未来月度收益低超过 1 个百分点 [S24]。
2. **中国市场有直接的、可独立核实的证据支持效应存在。** Li & Liu(2019,《济南大学学报》)用 2011–2018 年上海 A 股样本,确认 MAX 效应在中国存在,并把机制归因于投资者注意力和彩票偏好(关注度越高,效应越强;市场情绪越高,效应越强)[S30]。本次搜索也看到另外几篇关于"中国 MAX 效应"的工作论文/期刊论文,但标题、作者、确切年份在搜索摘要里不一致或互相矛盾(例如一篇说中国 MAX 效应不会让 IVOL 异象反转,另一篇说效应不稳健),**没有逐一核实,不计入出处表**,只记录"证据方向不完全一致"这个事实。
   → 翻译:核心 2 的方向(凸变换 + 衰减 + 排序 ≈ 按"最近极端日"排序)如果在 train/valid 上拿到的是"MAX 越大、后续收益越低",这与 Bali-Cakici-Whitelaw 和 Li-Liu 的方向一致;如果拿到的是反方向,需要额外解释,不能默认"反正是个新发现"。

### (b) 与特质波动率/已实现方差/已实现偏度/低波动异象的关系:同一个东西,还是独立的

3. **Bali-Cakici-Whitelaw 自己给出的答案是"很大程度上是同一个东西"。** 他们报告控制了 MAX 之后,Ang-Hodrick-Xing-Zhang 的特质波动率异象**显著减弱甚至消失**——即 IVOL 异象的很大一部分,其实是 MAX 效应在起作用 [沿用第一次搜索摘要,信息来自对 S24 的二次描述,核实为该论文的已知结论]。但这个结论本身有争议:Kowalke(2022)等后续工作对这个稳健性提出质疑,本次只拿到摘要层面的描述,未独立核实其方法和期刊,不计入出处表。
4. **已实现偏度是第三个相关但不完全相同的量。** Amaya, Christoffersen, Jacobs & Vasquez(2015)用分钟级数据构造周度已实现偏度,发现**最低**已实现偏度组比**最高**组未来一周收益高约 19 个基点(t=3.70),且该效应**在高波动股票里最明显,在低波动股票里几乎消失**——即它和波动率水平之间有乘性交互,不是独立加性效应 [S27]。
   → 翻译:这给出一个具体、可检验的预测——如果核心 2 的凸变换结构真的在逼近"极值统计量",那它的分数大概率会和"已实现偏度/MAX"高度相关(同一族),而不是和"已实现方差的线性水平"独立;这也回答了 L4(b) 的问题:三者在经验上高度重叠,不是互相独立的机制,但也不是完全等价,已实现偏度对波动率水平有明显的条件依赖,MAX 对 IVOL 有"吸收"关系。

### (c) 把波动类因子的非线性部分与线性波动控制分开的标准做法

5. **文献的主流做法是"整体分桶排序",不是"残差分解"。** Bali-Cakici-Whitelaw、Ang-Hodrick-Xing-Zhang、Amaya 等人全部用十分位/五分位组合报告收益差,是对原始统计量直接排序分组,不是先把某个波动代理拆成"线性部分 + 凸部分"再分别处理 [S24][S25][S27]。Bali & Cakici(2008)在 JFQA 上专门讨论过"用股票层面还是组合层面的断点、是否做加权"这类分桀细节会显著改变 IVOL 异象是否显著,但这仍然是分桶方法论内部的细节,不是"先剥凸、再线性中性化"这条路线 [未独立确认到足够细节,不计入出处表]。
   → 这意味着:规则 §4 陷阱 1(凸变换会把波动重新造出来)里描述的问题——"线性中性化去不掉凸的那部分"——**在我们查到的范围内,文献里没有一个标准做法专门针对这个问题**,学术界处理这类非线性是靠"整体分组排序"绕开线性中性化,而不是像我们这样"先中性化再看残差"。这支持陷阱 1 是我们自己在这套特定的"残差化纯多头"管线里发现的问题,不是文献已经解决、我们没学到的东西——但也说明,如果想在文献里找"怎么在残差化框架下处理凸性"这个具体问题,**大概率找不到**,因为主流资产定价文献根本不用这个框架。

### (d) 滚动回归斜率窗口长到什么程度会变成几乎静态的个股特征

6. **没有搜到直接讨论"滚动回归窗口退化为静态个股特征"这个具体现象的论文**,但找到两篇相邻、可以用来类比推理的文献。
   - Lewellen & Nagel(2006)讨论过一个相关的方差分解:beta 估计值的方差 = 真实 beta 的方差 + 估计误差的方差;他们选择用**短**窗口(季度/月度)而不是长窗口做条件 CAPM 检验,逻辑正是"窗口越长,估计出来的东西越接近无条件(即接近不随时间变化)的 beta,窗口越短才可能捕捉到真正的时变性"[S28]。
   - Levi & Welch(2017)系统讨论估计 beta 时的窗口长度取舍:数据越多,噪声越小,但越"过时"、越不能反映近期风险结构的变化;他们的框架本身就是在权衡"更长窗口 = 更低噪声但更接近静态估计"与"更短窗口 = 更贴近当前但噪声更大"[S29]。
   - **这两篇合起来支持一个合理推断,但不是直接证据**:`ts_regbeta` 窗口从 50→100→200 分数单调上升,按 Lewellen-Nagel 的框架,完全可能是"噪声在下降"而不是"信号在变强"——窗口越长,这个量越接近一个几乎不随时间变化的个股常数,这正是 B2(窗口 400)这个 R 变体想要检验的东西,而文献虽然没有直接证明"多长算退化",但明确支持"窗口越长越接近静态"这个方向性判断,这件事可以写进 B2 的预期说明里增加一点文献依据(§4.2 B2 目前只有"记账式"的 coverage 预期,没有文献支持这一条)。

### 缺口

- 没有搜到任何文献直接给出"滚动回归窗口长度超过多少天,会使这个量退化为一个几乎静态的个股特征"这个具体的阈值或判据——(d)第 6 条的两篇文献是方法论类比,不是直接先例。
- 没有搜到在"残差化/线性中性化"框架下专门处理波动类非线性成分的标准做法——(c)第 5 条的"搜不到"本身是一个诚实的信号。
- 中国市场关于 MAX 效应的证据,除 Li & Liu(2019)外,其余几篇因作者/年份/期刊在搜索结果里核实不充分,没有列入出处表,不能当作"中国证据很厚实"的依据。

---

## 出处表(全部核对时间,均在 2023-08-08 之前;续用第 1 轮编号规则,本轮重新从 S1 编起)

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|---|
| S1 | Order imbalance and individual stock returns: Theory and evidence | Tarun Chordia, Avanidhar Subrahmanyam | 2004-06 | 期刊:Journal of Financial Economics 72(3), 485–518 | https://ideas.repec.org/a/eee/jfinec/v72y2004i3p485-518.html | true |
| S2 | Order imbalance and stock returns: Evidence from China | Catherine Shenoy, Ying Jenny Zhang | 2007-12 | 期刊:The Quarterly Review of Economics and Finance 47(5), 637–650 | https://ideas.repec.org/a/eee/quaeco/v47y2007i5p637-650.html | true(仅核实标题/作者/卷期,摘要内容未核实到) |
| S3 | Individual Investor Trading and Stock Returns | Ron Kaniel, Gideon Saar, Sheridan Titman | 2008-02 | 期刊:Journal of Finance 63(1), 273–310 | https://ideas.repec.org/a/bla/jfinan/v63y2008i1p273-310.html | true |
| S4 | Do Retail Trades Move Markets? | Brad M. Barber, Terrance Odean, Ning Zhu | 2009-01 | 期刊:The Review of Financial Studies 22(1), 151–186 | https://ideas.repec.org/a/oup/rfinst/v22y2009i1p151-186.html | true |
| S5 | Resolving a Paradox: Retail Trades Positively Predict Returns but Are Not Profitable | Brad M. Barber, Shengle Lin, Terrance Odean | 2021-02(SSRN 首次提交 2021-02-18;2023-03 修订;期刊 Journal of Financial and Quantitative Analysis 正式刊出晚于本轮截止日,仅首版日期计入) | SSRN / 期刊:Journal of Financial and Quantitative Analysis | https://faculty.haas.berkeley.edu/odean/Papers%20current%20versions/resolving_a_paradox_retail_trades_positively_predict_returns_but_are_not_profitable.pdf | true |
| S6 | Understanding Retail Investors: Evidence from China | Charles M. Jones, Donghui Shi, Xiaoyan Zhang, Xinran Zhang | 2019-09(首版;本次读到的版本为 2022-05 ABFER 年会稿) | 工作论文:ABFER | https://abfer.org/media/abfer-events-2022/annual-conference/papers-investfin/AC22P3020_Understanding-Retail-Investors_Evidence-from-China.pdf | true |
| S7 | Price, trade size, and information in securities markets | David Easley, Maureen O'Hara | 1987-09 | 期刊:Journal of Financial Economics 19(1), 69–90 | https://ideas.repec.org/a/eee/jfinec/v19y1987i1p69-90.html | true |
| S8 | Liquidity, Information, and Infrequently Traded Stocks | David Easley, Nicholas M. Kiefer, Maureen O'Hara, Joseph B. Paperman | 1996-09 | 期刊:Journal of Finance 51(4), 1405–1436 | https://ideas.repec.org/a/bla/jfinan/v51y1996i4p1405-36.html | true |
| S9 | Inferring investor behavior: Evidence from TORQ data | Charles M. C. Lee, Balkrishna Radhakrishna | 2000-05 | 期刊:Journal of Financial Markets 3(2), 83–111 | https://ideas.repec.org/r/eee/intfin/v11y2001i2p147-165.html(引用页) | true(标题/作者/期刊/卷期在搜索结果文本中直接出现) |
| S10 | On the occurrence and consequences of inaccurate trade classification | Elizabeth R. Odders-White | 2000-08 | 期刊:Journal of Financial Markets 3(3), 259–286 | https://ideas.repec.org/a/eee/finmar/v3y2000i3p259-286.html | true |
| S11 | A test of the accuracy of the Lee/Ready trade classification algorithm | Erik Theissen | 2001 | 期刊:Journal of International Financial Markets, Institutions and Money 11(2), 147–165 | https://ideas.repec.org/a/eee/intfin/v11y2001i2p147-165.html | true |
| S12 | Evaluating trade classification algorithms: Bulk volume classification versus the tick rule and the Lee-Ready algorithm | Bidisha Chakrabarty, Roberto Pascual, Andriy Shkilko | 2015 | 期刊:Journal of Financial Markets 25, 52–79 | https://ideas.repec.org/a/eee/finmar/v25y2015icp52-79.html | true |
| S13 | Discerning Information from Trade Data | David Easley, Marcos López de Prado, Maureen O'Hara | 2016 | 期刊:Journal of Financial Economics 120(2), 269–285 | https://ideas.repec.org/a/eee/jfinec/v120y2016i2p269-285.html | true |
| S14 | Trade classification accuracy for the BIST | Osman Ulas Aktas, Lawrence Kryzanowski | 2014 | 期刊:Journal of International Financial Markets, Institutions and Money 33, 259–282 | https://ideas.repec.org/a/eee/intfin/v33y2014icp259-282.html | true |
| S15 | Stealth trading and volatility: Which trades move prices? | Michael J. Barclay, Jerold B. Warner | 1993 | 期刊:Journal of Financial Economics 34(3), 281–305 | （沿用第 1 轮核实结果,搜索结果给出标题/作者/卷期,未独立确认 DOI/直接链接） | true |
| S16 | Dynamic Volume-Return Relation of Individual Stocks | Guillermo Llorente, Roni Michaely, Gideon Saar, Jiang Wang | 2000-08(NYU 工作论文 FIN-00-032 首版;正式发表 Review of Financial Studies 15(4), 1005–1047, 2002) | 工作论文 / 期刊:Review of Financial Studies | https://ideas.repec.org/a/oup/rfinst/v15y2002i4p1005-1047.html | true |
| S17 | Price Momentum and Trading Volume | Charles M. C. Lee, Bhaskaran Swaminathan | 2000 | 期刊:Journal of Finance 55(5), 2017–2069 | https://ideas.repec.org/a/bla/jfinan/v55y2000i5p2017-2069.html | true |
| S18 | A Taxonomy of Anomalies and Their Trading Costs | Robert Novy-Marx, Mihail Velikov | 2016(NBER 工作稿 2014-12) | 期刊:The Review of Financial Studies 29(1), 104–147 | https://ideas.repec.org/a/oup/rfinst/v29y2016i1p104-147..html | true |
| S19 | The Expiration of IPO Share Lockups | Laura Casares Field, Gordon Hanka | 2001-04 | 期刊:Journal of Finance 56(2), 471–500 | https://ideas.repec.org/a/bla/jfinan/v56y2001i2p471-500.html | true |
| S20 | The IPO Lock-Up Period: Implications for Market Efficiency and Downward Sloping Demand Curves | Eli Ofek, Matthew Richardson | 2000-01 | 工作论文:NYU Stern Finance Working Paper 99-054 | https://ideas.repec.org/p/fth/nystfi/99-054.html | true |
| S21 | Information Discovery in Share Lockups: Evidence from the Split-Share Structure Reform in China(工作稿题为 Price Discovery in Share Lockups,首版 2008-02,本次读到版本 2009-10) | Li Liao, Bibo Liu, Hao Wang | 2008-02(首版;正式发表 2011-12,Financial Management 40(4), 1001–1027) | 工作论文(EFMA) / 期刊:Financial Management | https://efmaefm.org/0EFMSYMPOSIUM/2010-China/papers/LLW_splitshare20091030.pdf | true |
| S22 | 可交易性折扣、价值转移与限售股解禁 | 刘娥平、唐舜 | 2014-09 | 期刊:《财经研究》40(9), 86–96 | https://qks.shufe.edu.cn/J/ArticleQuery/A160824000481/CN | true |
| S23 | Share Issuance and Cross-sectional Returns | Jeffrey Pontiff, Artemiza Woodgate | 2008-04 | 期刊:Journal of Finance 63(2), 921–945 | https://ideas.repec.org/a/bla/jfinan/v63y2008i2p921-945.html | true |
| S24 | Maxing out: Stocks as lotteries and the cross-section of expected returns | Turan G. Bali, Nusret Cakici, Robert F. Whitelaw | 2011-02 | 期刊:Journal of Financial Economics 99(2), 427–446 | https://ideas.repec.org/a/eee/jfinec/v99y2011i2p427-446.html | true |
| S25 | The Cross-Section of Volatility and Expected Returns | Andrew Ang, Robert J. Hodrick, Yuhang Xing, Xiaoyan Zhang | 2006-02 | 期刊:Journal of Finance 61(1), 259–299 | https://ideas.repec.org/a/bla/jfinan/v61y2006i1p259-299.html | true |
| S26 | High Idiosyncratic Volatility and Low Returns: International and Further U.S. Evidence | Andrew Ang, Robert J. Hodrick, Yuhang Xing, Xiaoyan Zhang | 2009-01 | 期刊:Journal of Financial Economics 91(1), 1–23 | https://www.nber.org/papers/w13739 | true |
| S27 | Does realized skewness predict the cross-section of equity returns? | Diego Amaya, Peter Christoffersen, Kris Jacobs, Aurelio Vasquez | 2013-11(CREATES 工作稿;正式发表 2015,Journal of Financial Economics 118(1), 135–167) | 工作论文(Aarhus CREATES) / 期刊:Journal of Financial Economics | https://ideas.repec.org/a/eee/jfinec/v118y2015i1p135-167.html | true |
| S28 | The Conditional CAPM Does Not Explain Asset-Pricing Anomalies | Jonathan Lewellen, Stefan Nagel | 2006(NBER 工作稿 w9974, 2003) | 期刊:Journal of Financial Economics 82(2), 289–314 | https://www.nber.org/papers/w9974.pdf | true |
| S29 | Best Practice for Cost-of-Capital Estimates | Yaron Levi, Ivo Welch | 2017-04 | 期刊:Journal of Financial and Quantitative Analysis 52(2), 427–463 | https://ideas.repec.org/a/cup/jfinqa/v52y2017i02p427-463_00.html | true |
| S30 | 投资者关注与最大日收益率效应(Investor Attention and the Max Effect) | 李杰松(Jiesong Li)、刘媛(Yuan Liu) | 2019-05 | 期刊:《济南大学学报(社会科学版)》29(3), 94–105 | https://journal.ujn.edu.cn/en/article/22549152/ | true |

未列入上表、曾经搜索但没有搜到可独立核实文献的方向(诚实记录,不编造):
- Lee-Ready 算法本身(1991 年原文)的直接核实——本次只核实到大量引用它的后续文献,没有独立核实原文的期刊/卷期。
- 中国 A 股市场上,买方不平衡预测未来收益的**具体方向和幅度**——Shenoy & Zhang(2007)的标题/出处核实到了,摘要内容没有(L1(d)第 7 条)。
- "先按零收益占比/成交集中度筛选、再做横截面订单不平衡检验"这个具体操作流程的直接先例(L1(b)第 5 条)。
- "同一个指标单独当因子没用、当筛选条件有用"这个情形在严格的横截面资产定价场景下的直接对照实验(Lee-Swaminathan 是动量场景下最接近的类比,不是同一个问题)(L2(c))。
- 把"流通股本变化"从"价格水平/规模"中用回归残差方式分开的解禁文献(L3(d)第 7 条,本轮最重要的一条缺口)。
- 用上市年龄做解禁工具变量/分组变量的文献(L3(e)第 8 条)。
- "在残差化/线性中性化框架下专门处理波动类非线性成分"的标准做法(L4(c)第 5 条)。
- "滚动回归窗口长度超过多少天会退化为静态个股特征"的具体阈值或判据(L4(d)第 6 条)。

---

## 给 PI 的一句话总结

四条题目里,**最硬、最可直接改算子/写进合理度说明的三条**是:
(a)L1(c)——持有期证据显示"延续"只在日到月的尺度上成立,年度尺度上方向会反转(Barber-Odean-Zhu),这对"平滑窗口越长越好"的假设是一个明确的、可检验的上界警告,不支持无限往长堆;
(b)L3(d)——没有一篇解禁文献把"流通股本变化"从"价格水平"里用回归残差分开,这意味着 A4/A5 这两个判决性诊断是真正的新检验,不是在重复文献已有的结论,这件事本身应该写进给审计员的合理度说明里(到不了"有文献证据"那一档,但机制和检验设计都是干净的);
(c)L4(b)——Bali-Cakici-Whitelaw 自己报告控制 MAX 后 IVOL 异象显著减弱,说明"最近极端日"类因子和特质波动率异象在经验上高度重叠,如果核心 2 产出的 head 和库里已有的波动类 head 日度秩相关很高,不该被当成独立新发现。
L1(d) 的 Jones-Shi-Zhang-Zhang 发现(方向取决于谁在失衡)和 L2(c) 的 Lee-Swaminathan 机械交互警告,都是"做不了但要记住"的背景知识——前者因为缺账户级字段,后者因为提醒 §4.2 A 组的迁移检验是必要的而不是多余的。
L1(a)(b)、L2(b)、L3(e)、L4(c)(d) 都各有明确的"搜不到",这本身是诚实的信号:这几条在我们这个构造粒度和这个残差化框架下,确实没有现成文献可以照抄,是需要靠 train/valid 证据自己判断的地方。
