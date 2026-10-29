# 文献:种子 805,B 组,第 2 轮

对准 `r2/analysis.md` §6 的 L1–L4:核心 1 `cross_mean(day_corr(Ret, Volume), 20)`、核心 2 `sub(day_centroid(Volume), day_centroid(Ret))`(及 §2.1 的条件化机制)、
§2.2 的价格水平 / 股本代理判定、§2.4 的负面结果(`cross_zscore` 全表最差)。只用 **2023-08-08 之前**发表的论文 / 工作论文 / 研究报告
(journal 用正式出版日期,working paper 用首版 / 流通日期)。每条处理手法后面用 `[Sx]` 指向文末的出处表;`verified: true` = 这次搜索结果、二手摘要或页面上确实看到了标题 / 作者 / 期刊 / 卷期 / 链接这组信息对得上,不是凭记忆写的;
`verified: false` 的条目只记录「存在、主题对得上」,不据此写任何具体处理手法或数字。拿不准发表年月的,正文里写明「未确认」,不进出处表当证据用。

本轮一处方法论说明:对 L1、L2 我都尝试了 WebFetch 打开一次来源 PDF 核对具体构造细节 —— Heston-Korajczyk-Sadka(arXiv 的 HTML 镜像)成功,直接引用了它的原文句子;
Llorente-Michaely-Saar-Wang 的 PDF 是扫描版(CCITT 图像流),WebFetch 只读到了 PDF 结构里的 JSTOR/OUP 链接标识符(SICI 码),没有正文,所以它的具体构造细节(§L1 第 1 条)仍然来自多个独立二手摘要的交叉确认,不是我自己读到原文公式,这一点如实标注。

## L1. 分钟级「收益-成交量相关」当横截面特征,文献怎么处理(对准核心 1)

**结论先说**:经典文献几乎全部在**日频**上研究"量-价关系",用的是回归系数或分组,不是相关系数;"用分钟数据算出当日一个相关系数、再按天滚动平均去做横截面排序"这个具体构造,我没有搜到任何文献做过——这是信息,不是搜索失败。

1. **日频的量价关系用回归系数、不用相关系数,而且区分"投机性"与"风险分散性"交易**:Llorente, Michaely, Saar & Wang(*Review of Financial Studies* 15(4),1005–1047,2002)的核心变量是**次日收益对「当日收益 × 当日成交量」的回归系数**,不是相关系数;他们发现这个系数在横截面上有正有负 —— 系数为正(收益延续)对应信息驱动(投机性)交易占主导的股票,系数为负(收益反转)对应风险分散(对冲)性交易占主导的股票 [S1](**注意**:这条构造细节来自多个独立二手摘要——NYU/NBER 工作论文页、Cochrane 站点转载、各校资料库——的交叉确认,我尝试直接打开论文 PDF 核对原文公式但那份 PDF 是扫描图像,WebFetch 读不出正文,只核对到了 JSTOR 标识符里的刊名/卷期/年份,**正文构造细节本身不算我这次亲眼核对过**)。
   → 操作语言:这给出一个和我们 `day_corr(Ret, Volume)` 不同但**可比较**的处理——我们用的是"当日相关系数"(对称的量价共动强度),文献经典做法是"次日收益对(当日收益×当日成交量)的回归系数"(非对称、带方向的交互项)。核心 1 的 N 位如果想试这条,对应算子是 `cross_mean(mul(Ret, Volume), 1)` 这类乘积而不是相关,且要接到**次日**收益(我们环境里奖励本身已经处理了持有期,不需要额外构造超前变量)。
2. **|收益|-成交量关系是经典、稳健的正相关;带符号收益-成交量关系弱得多、而且不对称**:Karpoff(*Journal of Financial and Quantitative Analysis* 22(1),109–126,1987)的综述确认"混合分布假说"(MDH)框架下成交量与**绝对**价格变化正相关是最稳健的实证规律,而成交量与**带符号**收益的关系证据薄弱得多、方向不稳定 [S2]。
   → 操作语言:**直接支持我们 R 的第 3 条测量**(`day_corr(abs_(Ret), Volume)` vs `day_corr(Ret, Volume)`)——按文献,前者(波动驱动)应该比后者(方向驱动)更稳定;如果本轮 R 实测反而是带符号版本更强,那是对经典 MDH 框架的一个局部反例,值得写进 notebook。
3. **带符号的量价关系存在,但不对称,而且这个不对称和卖空限制有关**:Lin(*Investment Management and Financial Innovations* 13(1),92–111,2016-03)用台湾股票和 ETF 做"当期量-带符号收益关系"的跨产品检验,发现股票上这个关系主要是**正向不对称**(涨的时候量价关系比跌的时候更陡),且这个不对称随卖空限制的放宽而减弱,支持"卖空成本高昂假说";同一篇论文里 ETF 上的不对称方向相反,更符合"信息不对称/异质交易者"模型 [S3]。
   → 操作语言:这是少数**真正做过换证券类型(股票 vs ETF)稳健性检验**的文献,结论是"同一个量价不对称构造,在不同证券类型上方向会翻转"——对我们环境的提示是,`day_corr(Ret, Volume)` 的符号与强度可能对**卖空约束**(涨跌停、融券难度)敏感,而 A 股个股的卖空约束比美股/台湾股票更紧,方向判断不能直接照搬文献。
4. **把成交量拆成"订单失衡"和"笔数",控制住收益冲击后,量价共动关系会明显变弱**:Chan & Fong(*Journal of Financial Economics* 57(2),247–273,2000)发现 NYSE/Nasdaq 个股上,在回归里控制了订单失衡对收益的冲击之后,波动率-成交量关系大幅减弱;订单失衡(而不是成交笔数)解释了大部分波动率-成交量共动,且大单类别里的订单失衡对收益的影响更大 [S4]。
   → 操作语言:这暗示 `day_corr(Ret, Volume)` 这种裸相关系数里,很大一部分信息可能是"大单驱动的订单失衡"而不是"量价共动"本身的独立信息——R 的第 4 条测量(把 `Volume` 换成 `in_index(Volume)`,即用相关系数重新编码"成交是否后置")正是在试探这一点的一个侧面;如果想更直接地检验 Chan-Fong 这条,可以在 N 位里试"先按 `Amt` 的日内分布形状分组,再在组内看 `day_corr(Ret, Volume)`"。
5. **平滑多少天、要不要堆到 20 日以上才有效**:上述四篇文献全部在**日频**(一天一个观测值)上做横截面或时序分析,没有一篇把"当日量价相关系数"本身当作需要**多日平滑**才能用的特征——**这个「要堆 20 天平均才过线」的敏感性,文献层面找不到依据,也找不到反例,是我们自己环境里的实测结果,没有文献背书。**
6. **搜不到的部分**:没有搜到任何文献把"分钟级收益-成交量相关系数"(或任何等价的单一标量)直接当作横截面选股因子来检验;中文搜索(研报关键词"分钟级量价相关性""量价背离因子")也没有搜到对应的卖方研报原文,只搜到泛泛的"日内结构类因子"介绍文章,不构成证据,不进出处表。

## L2. 成交时点与波动时点怎么「配对」处理(对准核心 2,以及 §2.1 最硬的那条结论)

**结论先说**:经典文献确认"成交量曲线"与"波动率曲线"在日内形状上高度相关、且都是策略性聚堆的产物,但**配对处理几乎全部是线性的**(回归控制、相关系数),目前最接近的一篇(Heston-Korajczyk-Sadka)明确说线性控制**去不掉**对应的横截面效应——这和我们本轮发现的"分桶(非线性)> 什么都不做 > 相减(线性)"方向一致,但文献没有做过"非线性条件化"这一步,这是真正的空白,不是我没搜到。

1. **U 形是知情交易者与流动性交易者策略互动的产物,不是外生的日历效应**:Admati & Pfleiderer(*Review of Financial Studies* 1(1),3–40,1988)的理论模型里,有自由选择交易时点的流动性交易者会聚堆交易以在知情交易者面前隐藏自己,知情交易者倾向在流动性交易者聚堆的时段交易 [S5](此条已在 r1 的 L1 里引用过,这里重新给出是因为本轮的落点不同:不是"重心本身有没有信息",而是"重心配对别的日内形状量有没有道理")。
   → 操作语言:这条理论**支持"成交时点"和"波动时点"应当共同移动**(两者都是同一批策略性交易者行为的产物),所以把其中一个当另一个的条件变量去分桶,机制上说得通,不是无理由的组合。
2. **最早的实证记录:日内 U 形首先在"收益方差"和"分钟级收益序列的首尾效应"里被发现,去掉首尾段后自相关大幅下降**:Wood, McInish & Ord(*Journal of Finance* 40(3),723–739,1985-07)用 1971–72 和 1982 年 NYSE 交易数据构造分钟级市场收益序列,检验正态性与自相关,发现去掉开盘与收盘段效应能大幅降低序列的自相关 [S6]。
   → 操作语言:这是对"日内形状存在首尾效应、且首尾效应会污染时序统计量"这件事最早的实证确认,但这篇**没有**给出任何"用一条曲线预测/条件化另一条曲线"的具体处理,只确认了现象本身,是机制背景,不是处理手法。
3. **最接近的一篇:把成交量变化、订单失衡变化、波动率变化放进同一个回归里,检验它们能否解释收益的日内延续模式**:Heston, Korajczyk & Sadka(*Journal of Finance* 65(4),1369–1407,2010;也有 arXiv 版 1005.3535)发现股票在某个半小时窗口的收益会在之后约 40 个交易日里持续在**同一个半小时窗口**延续;论文明确写到"to the extent that volume and volatility are correlated, the volume pattern is consistent with the patterns in intraday volatility"(就volume和volatility相关的程度而言,volume模式与日内volatility模式是一致的),并且把收益变化对"滞后收益 + 滞后成交量变化 + 绝对收益 + 相对价差 + 绝对订单失衡变化"做多元回归,**结果是收益可预测性的日内模式"unaffected"(不受影响)**——即线性地控制成交量/波动率/订单失衡的变化,去不掉这个横截面效应 [S7]。
   → 操作语言:这是目前搜到的**唯一一篇把"成交量曲线"和"波动率曲线"的日内模式放在同一个框架里比较**的文献,但它的"配对"方式是**线性回归控制**,不是分桶、不是非线性条件化,而且它的结论恰恰是"线性控制去不掉模式"。这和我们本轮 §2.1 第 3 条的发现 ——"分桶(非线性)> 什么都不做 > 相减(线性)"——方向完全一致:Heston 等人试的是"相减/回归控制"那一档(线性),我们实测这一档确实效果较弱(`sub` 版 0.83 vs 分桶版 1.55);**文献没有试过把其中一个变量当分桶条件变量**,`cs_bucket_zscore(cross_mean(day_centroid(Volume), 20), day_centroid(Ret))` 这个具体构造,在搜到的文献范围内没有先例,是真正的新组合,不是我们重新发明了文献已经否定的东西。
4. **领先滞后(成交先于波动,还是波动先于成交)的横截面结果**:**搜不到**。搜索确实找到了一篇专门做这个领先滞后问题的工作论文(Örebro 大学,2025 年,主张"成交量先对信息反应、波动率后调整"),但它的发表日期在 2023-08-08 之后,按规则不能用,也不记入出处表。搜到的其余文献(Foster & Viswanathan 1990 的理论模型)是研究**日间**(周一效应)而不是**日内**领先滞后,主题不对口,这里不引用。**这个具体的领先滞后机制问题,在允许的日期范围内搜不到答案。**
5. **归一化方式**:搜到的所有文献(Admati-Pfleiderer、Wood-McInish-Ord、Heston-Korajczyk-Sadka)都没有明确给出"曲线各自除以自身全日总量"这类具体归一化步骤的描述——它们报告的是"百分比变化"或"方差",不是我们 `day_centroid` 这种把日内分布压缩成单一重心标量再归一化到 [0,1] 的处理。**这个具体的归一化方式,文献摘要层面没有给出,找不到依据,也找不到反例。**

## L3. 名义股价水平 / 流通股数作为独立于市值的特征;A 股「便宜股角落」怎么剥(对准 §2.2)

**结论先说**:美股文献上"价格水平独立于规模"这件事有双向证据(有的研究说独立,有的说和地区/市场相关、会被规模混淆);A 股特有的"壳价值"污染有扎实的学术证据,而且**已经有现成的处理手法可以直接套用**——不是线性中性化,是**按市值直接剔除最小的一段**或**构造连续的壳概率变量**。

1. **美股名义股价长期维持恒定,背后是管理层迎合投资者偏好的「迎合」行为**:Weld, Michaely, Thaler & Benartzi(*Journal of Economic Perspectives* 23(2),121–142,2009)记录美国股票名义价格自大萧条以来基本没有跟上通胀上涨,并综述了几种行为学解释(交易成本、券商惯例、迎合投资者偏好)[S8]。
   Baker, Greenwood & Wurgler(*Journal of Finance* 64(6),2559–2590,2009-12)把这个"迎合理论"形式化并在时序和个股层面提供证据:当投资者给低价股更高估值时,管理层会倾向把价格维持在低位 [S9]。
   → 操作语言:两篇共同支持"名义价格水平本身是一个被管理层主动维持、被投资者情绪驱动的变量",不是会计恒等式的副产品——这支持把价格水平**当作一个独立的、随时间变化重要性的轴**,而不是简单归为规模的线性函数。
2. **低价股的超额收益可能来自投资者对其"上涨空间"的认知偏差(非线性、和市值不是同一回事)**:Birru & Wang(*Journal of Financial Economics* 119(3),578–598,2016)发现投资者系统性高估低价股相对高价股的偏度(上涨空间),这个认知偏差能解释部分低价股溢价和期权市场的相关定价模式 [S10]。
   → 操作语言:**这正是 §5.3 备选 N 里"把价格当条件变量去净化别的信号"这个建议的行为学机制依据**——如果低价股溢价的来源是"投资者认知偏差"而不是"规模本身",那么按价格分桶(而不是按市值线性控制)去剥离这个偏差,方向上是对的。
3. **价格水平作为独立于规模的特征,证据因市场而异**:Lu(Cass Business School 博士论文,2009,导师 Hwang)第四章发现美股上股价水平对收益有独立的、反向的效应,控制规模/流动性/账面市值比/盈利收益率/动量之后依然存在 [S11](**这是一篇未发表的博士论文章节,不是期刊论文,我按「研究报告」的口径收录,但要标注它没有经过同行评审**)。
   Elfakhani & Wei(*Review of Financial Economics* 12(4),397–411,2003)在加拿大市场发现相反的结构:存在显著的反向价格效应,但独立规模效应的证据较弱——规模效应只在**较高价格**的那部分股票里出现,暗示规模和价格在加拿大市场是**混淆**的,不是两条独立的轴 [S12]。
   → 操作语言:**这两篇合起来说明"价格独立于规模"不是普遍规律,依赖市场结构**。对我们这个判定(§2.2 判定"B 轴是代理")是一个提醒:不能假设 A 股的价格效应一定独立于市值,Elfakhani-Wei 这类"规模-价格混淆"结构在 A 股同样可能发生,R 第 13 条(band 变量从价格换成市值)正是在直接检验这件事,文献支持这条检验的价值,但不能替我们预判结果。
4. **价格水平与动量/风险的交互(角度不同,但同样把价格当条件变量)**:Chuang(IUJ Research Institute 工作论文 EMS-2021-01,正文落款 2020-03,PDF 日期 2021-02)发现价格水平**极高或极低**的股票动量更弱、系统性风险更高,这个结构在控制了拆股行为之后依然存在,作者把机制归因于"拆股会吸引更多非知情交易者参与,从而减缓信息扩散、放大动量" [S13]。
   → 操作语言:这不是直接支持我们的代理判定,但给出了另一种"把价格当条件变量"的具体用法——**按价格的极端程度(而不是按价格的高低排序)分组**,是一个 §5.3 没列出的新角度,如果 PI 想在价格轴上再做一次 N,这是一个候选方向。
5. **A 股特有的「壳价值」污染,是目前搜到的、针对本轮判定最直接可用的处理手法**:Liu, Stambaugh & Yuan(*Journal of Financial Economics* 134(1),48–69,2019)构建中国的 size/value 因子时,**直接把按市值最小的 30% 股票剔除出 universe**,理由是中国 IPO 管制严格,导致最小的一批上市公司的壳资源价值很高——对一个典型的、落在最小 30% 分位的股票,他们估计其市值里大约 30% 是壳价值而不是经营价值 [S14]。
   Lee, Qu & Shen(Stanford GSB Research Paper No. 3604,2017)用一个更连续的「预期壳概率」(Expected Shell Probability, ESP)变量代替简单的"剔除最小 30%",发现做多(空)ESP 最高(最低)的股票组合有显著超额收益,且这个壳溢价随 IPO/并购重组监管政策的变化而时变 [S15](**这篇我只核对到 Stanford GSB 与 RePEc 的工作论文记录,没能打开 SSRN/GSB 全文核对具体回归系数,只记这个定性结论**)。
   → 操作语言:**这是本题最可操作的一条,直接对应 §2.2 (c) 和 R 第 13 条的决定性检验**。文献给出的不是"线性中性化",而是两种更激进的处理:(a) **按市值分位直接剔除最小的一段**(Liu-Stambaugh-Yuan 用的是 30% 这个具体数字,是 A 股实证得出的,不是任意选的),这可以直接翻译成在 B 轴相关的 E/R 任务里加一条"universe 先按市值砍掉最小 30% 再重新评估这个 head"的检验,比单纯看 `rho_known` 更能回答"这条轴剔除壳污染之后还剩多少";(b) 构造一个连续的"壳概率"条件变量去分桶,而不是直接拿 `LogFloatCap` 做线性控制——如果 PI 想在这条轴上开新的 N,方向应该是"用非线性、market-cap 分位相关的方式剥离壳污染",而不是再加一层线性回归。
6. **搜不到的部分**:具体的"ST 股 / 退市风险 / 涨跌停与停牌"怎么在构造价格因子时被处理(整天剔除 vs 只剔除涨跌停分钟 vs 按 `LimitWidth` 条件化),学术文献层面搜不到标准做法——搜到的只是中文财经媒体关于个股跌到 0.09 元、逼近 1 元退市线的报道,这些是新闻报道不是学术文献,不构成证据,不进出处表;"双重排序剥离规模与价格"的具体操作细节,除 Elfakhani-Wei 的定性结论外,没有搜到给出排序步骤的论文(我原计划找的 Singal & Tayal 这篇,搜索没有定位到任何确实存在的同名论文,大概率是我记错了作者名,如实报告搜不到,不要凑一个相近的论文顶上)。

## L4. 为什么「相对自身历史的异常值」版本会比「多日平均」版本差这么多;换手 / 成本 / 订单失衡的横截面失效(对准 §2.4,修正 r1 的 L3)

**结论先说**:换手/成本侵蚀的机制,文献证据扎实、可以直接用;但"为什么标准化会把一个本来有效的持续性特征搞成全表最差"这个具体机制问题,**搜不到直接文献**,而且 r1 已经引用的两篇文献(Gervais-Kaniel-Mingelgrin、Lee-Kim-Kim)结论方向与本轮实测相反,这个矛盾要如实报给 PI,不能回避。

1. **换手率是成本侵蚀的主要驱动因子,存在一个大致的经验法则**:Frazzini, Israel & Moskowitz(AQR / NBER 会议工作论文"Trading Costs of Asset Pricing Anomalies",首版 2012-10,此版 2012-12)检验了多个经典异象的交易成本,发现规模、价值、动量这类低到中等换手的策略在很大资金规模下依然能扛住成本,但短期反转这类高换手策略扛不住 [S16](**注意**:这篇后来被作者改写重发为 2018 年的"Trading Costs",但 2012 年这版工作论文本身早于我们的截止日,可以引用;我只在二手摘要里看到"换手每提高、净收益大致线性侵蚀"这类定性描述,没有核对到具体的 bp 数字,不写进任何具体数字)。
   Novy-Marx & Velikov(*Review of Financial Studies* 29(1),104–147,2016;NBER 工作论文版 2014-12)系统检验了多个异象在不同成本缓解手段下的表现,核心结论是:**加一个"买入/持有带"(允许继续持有不会主动交易进的股票,而不是每次重新排序都换仓)是单一最有效的成本缓解手段**;月度单边换手低于 50% 的异象在做了这类处理之后大多还能保持统计显著的净利差,换手更高的大多不能 [S17]。
   → 操作语言:这**直接支持换手类处理手法本身**(而不是解释为什么 z-score 版本更差),可以转译成:给 `cross_zscore(day_centroid(Volume), 20)` 这类本质上是"逐日追踪自身在最近 20 天里的相对位置变化"的构造加一个**买入/持有带**(只有当新的 z-score 偏离上次入选时的值超过某个阈值才换仓),而不是每天重新算。这是一个可以直接写进 R 或下一轮 N 任务书的具体处理,但它**解决的是成本问题,不解决"为什么这个方向本身分数就低"的问题**——按 §2.4 的证据,`cross_zscore` 版本的问题不只是换手贵,是 train/valid score 本身就是全表最差(−4.88),哪怕零成本也救不回来,这一点要如实告诉 PI,不要把这条文献当成"z-score 版本值得再抢救一次"的理由。
2. **带符号的成交量 / 订单失衡,作为横截面特征,预测方向会随 horizon 反转,且短期可预测性会在很短时间内被交易掉**:Chordia & Subrahmanyam(*Journal of Financial Economics* 72(3),485–518,2004-06)发现个股的订单失衡与**短期**(日内/隔日)收益是负向关系,与**更长**horizon 的收益是正向关系——同一个构造,方向随持有期翻转 [S18]。
   Chordia, Roll & Subrahmanyam(*Journal of Financial Economics* 76(2),271–292,2005-05)发现标普 500 成分股的滞后订单失衡对收益的预测力,在 1996 年的样本里 30 分钟内就基本消失,作者把这个归因于"反向交易被引入来抵消这个可预测性"(即市场在学习、套利抹平信号)[S19]。
   → 操作语言:这两篇**直接回应"带方向的成交量作为日频横截面特征,有没有文献报告它失效或方向不稳"**——有,而且是同一批作者的两篇独立论文,结论方向一致:订单失衡类信号的可预测性是**horizon 敏感、会随时间被套利抹平**的。这是对我们 `day_signed_ratio(Ret, Amt)` 本轮实测(4 个候选平均 −3.46,彻底反向)的一个旁证,但要注意**这两篇研究的是市场整体或大盘股样本内、分钟到日的短 horizon**,不是跨股票横截面、用分钟数据构造日频特征再做月度持有的设定,不能把"30 分钟内失效"这个具体数字直接套到我们的环境,只能当作"同一类构造确实存在失效/反转倾向"这个方向性旁证。
3. **"为什么标准化会让一个持续性特征变差"这个机制问题,搜不到,而且和 r1 已引用的文献方向相反**:**没有搜到任何文献**直接讨论"对一个本身有信息的、持续性很强的日内特征做自身历史标准化(z-score / 偏离度),为什么会比简单多日平均表现更差"。更需要如实报告的是:r1 的 L3 引用的 Gervais-Kaniel-Mingelgrin(*Journal of Finance* 56(3),2001)和 Lee-Kim-Kim(2016 会议论文,未确认期刊出处)都指向**相反方向**——"相对自身历史的异常值"版本(高量后续收益溢价)比"水平"版本更有效。本轮实测恰好相反:`cross_zscore(day_centroid(Volume), 20)` 是全表最差的一行。**这个矛盾不能靠搜更多文献解决,因为两边说的不是同一个特征**(GKM/Lee-Kim-Kim 测的是成交量/换手率的**总量**水平,我们测的是日内成交**时点**这个形状统计量的 z-score,底层驱动力可能完全不同——前者的"异常"对应"关注度/信息事件冲击",后者的"异常"可能只是measurement noise被标准化放大,因为`day_centroid`这个量本身的横截面分布本就很窄、时序方差可能主要是噪声而不是信号)。**这是我能给出的最接近的机制猜测,不是文献结论,PI 如果要用这条推理,必须标注「推断,非文献证实」。**

## 出处表

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|---|
| S1 | Dynamic Volume-Return Relation of Individual Stocks | Guillermo Llorente, Roni Michaely, Gideon Saar, Jiang Wang | 2002(RFS 15(4), Autumn 2002, 1005–1047;NBER WP No. 8312 为 2001 年版) | Review of Financial Studies, 15(4), 1005–1047 | DOI 10.1093/rfs/15.4.1005 ; https://www.nber.org/papers/w8312 ; https://archive.nyu.edu/handle/2451/26698 | true(刊名/卷期/年份经 PDF 内 JSTOR SICI 标识符核对;构造细节来自多个独立二手摘要交叉确认,非直接读到正文公式) |
| S2 | The Relation between Price Changes and Trading Volume: A Survey | Jonathan M. Karpoff | 1987-03 | Journal of Financial and Quantitative Analysis, 22(1), 109–126 | https://ideas.repec.org/a/cup/jfinqa/v22y1987i01p109-126_01.html ; https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/relation-between-price-changes-and-trading-volume-a-survey/DBE2C70FA41E390EB8FA418BBFFD76C8 | true |
| S3 | Contemporaneous and asymmetric volume-return relationship: cross-product evidence from an emerging market | Jung-Chu Lin | 2016-03 | Investment Management and Financial Innovations, 13(1), 92–111 | DOI 10.21511/imfi.13(1).2016.09 ; https://businessperspectives.org/index.php/component/zoo/contemporaneous-and-asymmetric-volume-return-relationship-cross-product-evidence-from-an-emerging-market | true |
| S4 | Trade size, order imbalance, and the volatility-volume relation | Kalok Chan, Wai-Ming Fong | 2000(JFE 57(2), 247–273) | Journal of Financial Economics, 57(2), 247–273 | DOI 10.1016/S0304-405X(00)00057-X | true |
| S5 | A Theory of Intraday Patterns: Volume and Price Variability | Anat R. Admati, Paul Pfleiderer | 1988 | Review of Financial Studies, 1(1), 3–40 | https://www.gsb.stanford.edu/faculty-research/publications/theory-intraday-patterns-volume-price-variability ; https://ideas.repec.org/a/oup/rfinst/v2y1989i2p189-223.html | true(与 r1 lit.md 的 S2 同一篇,本轮重新核对) |
| S6 | An Investigation of Transactions Data for NYSE Stocks | Robert A. Wood, Thomas H. McInish, J. Keith Ord | 1985-07 | Journal of Finance, 40(3), 723–739 | https://ideas.repec.org/r/bla/jfinan/v40y1985i3p723-39.html ; https://digitalcommons.memphis.edu/facpubs/11516 | true |
| S7 | Intraday Patterns in the Cross-Section of Stock Returns | Steven L. Heston, Robert A. Korajczyk, Ronnie Sadka | 2010(JF 65(4), 1369–1407) | Journal of Finance, 65(4), 1369–1407;同一内容的 arXiv 版 1005.3535 | DOI 10.1111/j.1540-6261.2010.01573.x ; https://ar5iv.arxiv.org/html/1005.3535 | true(通过 WebFetch 直接打开 arXiv HTML 镜像核对了原文句子,包括 "to the extent that volume and volatility are correlated, the volume pattern is consistent with the patterns in intraday volatility" 与回归不受影响的结论) |
| S8 | The Nominal Share Price Puzzle | William C. Weld, Roni Michaely, Richard H. Thaler, Shlomo Benartzi | 2009(JEP 23(2), 121–142;DOI 10.1257/jep.23.2.121;早期工作论文版题为"The Nominal Price Puzzle",SSRN abstract=891213,与下面 S9 的 NBER WP 13762 是**两篇不同的论文**,我用 WebFetch 直接核对过 NBER 13762 页面的标题/作者/年份,确认它属于 S9 不属于本条,已更正早先搜索摘要里的混淆) | Journal of Economic Perspectives, 23(2), 121–142 | https://ideas.repec.org/a/aea/jecper/v23y2009i2p121-42.html ; https://papers.ssrn.com/abstract=891213 | true |
| S9 | Catering through Nominal Share Prices | Malcolm Baker, Robin Greenwood, Jeffrey Wurgler | 2009-12(JF 64(6), 2559–2590;NBER WP No. 13762,2008-01 发布,经 WebFetch 直接核对 NBER 页面标题/作者/年份) | Journal of Finance, 64(6), 2559–2590 | DOI 10.1111/j.1540-6261.2009.01511.x ; https://www.nber.org/papers/w13762 | true |
| S10 | Nominal Price Illusion | Justin Birru, Baolian Wang | 2016(JFE 119(3), 578–598;工作论文版至少 2012-12) | Journal of Financial Economics, 119(3), 578–598 | DOI 10.1016/j.jfineco.2016.01.027 | true |
| S11 | Essays on Cross-Sectional Asset Pricing(第四章:股价水平的横截面效应) | Chensheng Lu(导师 Soosung Hwang) | 2009 | 未发表博士论文,Cass Business School(City University London) | https://openaccess.city.ac.uk/id/eprint/19574/1/Lu,%20Chensheng.pdf | true(标题、作者、导师、第四章主题经 City Research Online 仓库记录核对;**未经同行评审,不是期刊论文**) |
| S12 | The survivorship bias, share price effect, and small firm effect in Canadian markets | Said Elfakhani, Jack Wei | 2003(Review of Financial Economics, 12(4), 397–411) | Review of Financial Economics, 12(4), 397–411 | https://ideas.repec.org/a/wly/revfec/v12y2003i4p397-411.html | true |
| S13 | How Much Does Nominal Share Price Matter? | Hongwei Chuang | 正文落款 2020-03,PDF 发布 2021-02(IUJ Research Institute Working Paper EMS-2021-01) | International University of Japan, Economics & Management Series working paper | https://ideas.repec.org/p/iuj/wpaper/ems_2021_01.html ; https://iuj.repo.nii.ac.jp/record/958/files/EMS_2021_01.pdf | true |
| S14 | Size and Value in China | Jianan Liu, Robert F. Stambaugh, Yu Yuan | 2019(JFE 134(1), 48–69;NBER WP No. 24458) | Journal of Financial Economics, 134(1), 48–69 | DOI 10.1016/j.jfineco.2019.03.008 ; https://www.nber.org/papers/w24458 | true |
| S15 | Reverse Mergers, Shell Value, and Regulation Risk in Chinese Equity Markets | Charles M.C. Lee, Yuanyu Qu, Tao Shen | 2017(Stanford GSB Research Paper No. 3604) | Stanford Graduate School of Business working paper | https://ideas.repec.org/p/ecl/stabus/repececlstabus3604.html ; https://www.gsb.stanford.edu/faculty-research/working-papers/reverse-mergers-shell-value-regulation-risk-chinese-equity-markets | true(标题/作者/机构/编号经 RePEc 与 Stanford GSB 页面核对;未能打开全文核对具体回归系数,定性结论来自摘要) |
| S16 | Trading Costs of Asset Pricing Anomalies | Andrea Frazzini, Ronen Israel, Tobias J. Moskowitz | 首版 2012-10,此版 2012-12(AQR / NBER 会议工作论文;后于 2018 年改写为"Trading Costs") | AQR Capital Management working paper;NBER conference paper | https://www.aqr.com/Insights/Research/Working-Paper/Trading-Costs-of-Asset-Pricing-Anomalies ; https://conference.nber.org/conf_papers/f68262/f68262.pdf | true(标题/作者/日期经 AQR 官网与 NBER 会议论文页核对;具体 bp 数字只在二手摘要出现,未采信为精确数字) |
| S17 | A Taxonomy of Anomalies and Their Trading Costs | Robert Novy-Marx, Mihail Velikov | 2016(RFS 29(1), 104–147;NBER WP No. 20721 为 2014-12 版) | Review of Financial Studies, 29(1), 104–147 | DOI 10.1093/rfs/hhv063 ; https://www.nber.org/papers/w20721 | true |
| S18 | Order imbalance and individual stock returns: Theory and evidence | Tarun Chordia, Avanidhar Subrahmanyam | 2004-06(JFE 72(3), 485–518) | Journal of Financial Economics, 72(3), 485–518 | DOI 10.1016/S0304-405X(03)00175-2 | true |
| S19 | Evidence on the speed of convergence to market efficiency | Tarun Chordia, Richard Roll, Avanidhar Subrahmanyam | 2005-05(JFE 76(2), 271–292) | Journal of Financial Economics, 76(2), 271–292 | DOI 10.1016/j.jfineco.2004.06.004 | true |

## 给 PI 的汇总(哪些处理手法有文献撑,哪些没有,哪些是矛盾)

- **可以直接写进任务书、而且是本轮最具体可操作的一条**:核心 1 的 R/N 若要处理 §2.2 的价格代理问题,文献支持**非线性剥离**而不是线性中性化——Liu-Stambaugh-Yuan [S14] 的具体做法是**按市值剔除最小 30%**,Lee-Qu-Shen [S15] 的做法是构造连续的壳概率条件变量;这两条都比"再加一层线性回归"更接近文献证据,可以直接对应到 R 第 13 条(band 换市值)之外再加一条"universe 先砍掉最小 30% 再重算"的检验。
- **机制上支持、但文献只做到线性控制,没做到我们本轮证明有效的非线性分桶**:核心 2 的配对逻辑(成交时点 × 波动时点)——Admati-Pfleiderer [S5] 支持"两者应当共同移动"这个前提,Heston-Korajczyk-Sadka [S7] 实际比较过两者并明确说线性控制去不掉对应效应,这和我们"分桶 > 相减"的发现方向一致,但**没有文献做过 `cs_bucket_zscore` 这种具体的非线性配对**,核心 1 的 E 位若往这个方向走,是在填一个文献空白,不是在重复已被否定的东西。
- **有文献但方向提示要谨慎,不能直接套用**:核心 1 的带符号成交量/订单失衡构造——Chan-Fong [S4]、Chordia-Subrahmanyam [S18]、Chordia-Roll-Subrahmanyam [S19] 都指向"这类信号 horizon 敏感、容易被套利抹平",与我们 `day_signed_ratio(Ret, Amt)` 本轮 −3.46 的实测方向一致,但这些文献研究的是分钟到日的短 horizon、美股大盘股样本,不能把具体数字(如"30 分钟内失效")套到我们的月度持有、A 股全市场设定上。
- **明确的矛盾,必须如实报给 PI,不能回避**:§2.4 的负面结果(`cross_zscore` 全表最差)和 r1 已引用的 Gervais-Kaniel-Mingelgrin / Lee-Kim-Kim(方向相反)之间的冲突**搜不到文献能解决**——这不是因为我搜索不够,是因为两边测的不是同一类特征(成交量总量 vs 日内时点形状)。能给的只有一个未经文献证实的机制猜测(day_centroid 的时序方差可能主要是噪声,被标准化放大),PI 如果要用这条,必须标注「推断,非文献证实」。
- **搜不到、如实记录,不要在任务书里当成文献支持**:
  - "分钟级收益-成交量相关系数"本身被当作横截面选股因子检验的任何文献(L1 第 6 条)。
  - 成交时点曲线与波动时点曲线之间"谁领先谁"的横截面结果(L2 第 4 条;唯一找到的一篇日期在截止日之后,不能用)。
  - "曲线各自除以自身全日总量"这类具体归一化步骤的文献依据(L2 第 5 条)。
  - A 股 ST 股 / 涨跌停 / 停牌样本在构造价格类因子时的具体剔除规则(L3 第 6 条;只有新闻报道,不是学术文献)。
  - "Singal & Tayal" 这篇我在上一轮题目里设想存在的论文,这轮没搜到任何证据它存在,大概率是记错了作者名,不要在后续任务书里再引用这个名字。
  - "为什么对一个持续性特征做自身历史标准化会让它变差"这个机制问题本身(L4 第 3 条)。
