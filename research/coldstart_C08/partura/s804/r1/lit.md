# 文献笔记:种子 804,P 组,第 1 轮(文献员)

对准 `analysis.md` §5 的 4 个题目。每条"处理方式"后面括号里是出处编号,对应文末的出处列表。
检索范围限定在 **2023-08-08 之前**发表的论文 / 工作论文(以 arXiv/SSRN/working paper series 的首版日期为准);拿不准首版日期的工作论文,我在出处里单独标注,不当结论的唯一支撑。

本轮 `WebSearch` 用到约一半时就被会话级配额打断("this turn's web search budget is used up... shared by every agent in it"),所以第 3 题(自由流通比例)和第 4 题里 ST/价格限制当筛的量化证据搜得比前两题薄,下面明确标出哪里是"搜不到"。

---

## 题目 1 —— 流通股本变动(对准核心① `ts_var(LogFloatShares, 10)` 与 N-a)

**处理方式:**

1. **国际主流文献几乎不用"事件哑变量",而是用连续的"对数股本变化率"**,在月度/年度频率上整池横截面回归,而不是只盯着具体的解禁/增发日前后几天。Pontiff & Woodgate (2008) 的 net share issuance 就是 `log(split_adjusted_shares_t / split_adjusted_shares_{t-1年})`,Fama-French 数据库里的 `NI` 变量做法一样:用上一个财年末到再上一个财年末的对数股数差。(出处 1、2)
   **能直接翻译成我们的算子**:这正是 `analysis.md` N-a 已经写出来的 `sub(LogFloatShares, cross_ema(LogFloatShares, 241))`(或 `ts_delay` 版本)——文献上这是"标准做法"而不是我们临时拼出来的,给 N-a 加了外部背书。
2. **符号是一致的负向**:Daniel & Titman (2006) 的 composite equity issuance、Pontiff & Woodgate (2008) 的 net share issuance,都是"近期股本扩张得越多,未来横截面收益越低"。McLean, Pontiff & Watanabe (2009) 把这个结果扩展到 41 个非美市场,方向一致。(出处 1、2、3)
   → 翻译:`sub(LogFloatShares, cross_ema(LogFloatShares,241))` 这个差分,**预期的横截面方向应该是负的**(扩张越多、后续表现越差),这是一个可以写进 missions 给审计员看的"机制陈述"。
3. **真正做"事件窗口"研究的,是单个制度事件(股改全流通解禁),窗口比我们的 10 天长得多**:Liao/Liu/Wang 对中国股改限售股解禁的研究用 **[-120, +20] 交易日**窗口,报告解禁事件前后出现约 -14% 的异常收益和约 +140% 的成交量放大(出处 5,**细节单薄,见下方核实说明**)。上海交大一篇研究发现解禁前后买卖价差与非流动性上升,信息披露质量越高这个上升越弱(出处 6)。
   → 翻译:如果以后要把这类特征做成"事件探测 + 窗口"(而不是像核心①那样直接吃 `ts_var`),文献提示窗口应该**向前看得更远**(几个月量级,不是 10 天),因为解禁前的"抢跑"是主要部分;10 日窗口更像是在抓"刚发生的变动"这个事实本身,而不是解禁事件的价格效应——这跟 `analysis.md` 把 ① 定位成"股本变动事件探测器"(而非"解禁价格效应捕捉器")是一致的,**不需要改核心①的窗口,但 N-a 如果要往"解禁前抢跑"方向扩展外围,窗口该用 60–120 天量级,不是 10 天**。
4. **"流通股变多"在中国语境下还有一条公司金融机制**:Fang, Song, Nofsinger & Wang (2017) 发现股改后非流通股占比下降(即流通盘变大)的公司现金分红显著下降——作者把这解释成"用分红补偿交易受限的股东,流通性恢复后补偿需求下降"。(出处 4)
   → 这不直接是一个收益预测处理方式,但提示 `LogFloatShares` 的变化与公司支付政策、治理结构相关,不是纯噪声,对核心①"机制干净"的判断是另一条支撑。

---

## 题目 2 —— 名义股价水平(对准 N-b)

**处理方式:**

1. **原始 `log(股价)` 水平本身是"两股力量打平"的脏信号,文献明确警告不能直接用**:Birru & Wang 的 Dice Center 工作论文《The Nominal Price Premium》(2015)和后续发表的 JFE 论文《Nominal Price Illusion》(2016)都指出,raw price 同时混了(a) 投资者对低价股的乐观偏见("名义价格幻觉"带来的溢价,预期为正)和(b) 低价股隐含更高贴现率的机械效应(预期为负),两者方向相反、几乎抵消,所以 **raw price 对未来收益没有稳健的预测力**。(出处 7、8)
   → 直接翻译:`sub(LogFloatShares, LogFloatCap)`(= −log 名义股价)**不控制贴现率这条腿**,单独拿去当因子很可能和文献里的"raw price 不稳健"撞上——这是对 N-b 的一个警告,不是否定它,而是提示**不能只做这一步差分就收工**。
2. **文献里把"脏信号"拆干净的方法**:用会计口径的每股账面值等基本面变量回归出一个"拟合价格"(fitted price),再看**实际价格相对拟合价格的偏离**(而不是价格水平本身),这部分偏离才是干净的"信念型"低价股溢价,四因子 alpha 月度约 85–88 bp。(出处 7、8)
   → 这一步在我们的字段立方体里做不到(没有每股账面值这类财务字段,规则 §5 也不让读 `research/` 外的财务数据),**但它给了一个可操作的替代思路**:既然拟合不出"基本面隐含价格",可以退一步,用**同一字段在时间上的变化**(例如股价是否刚经历过低价股票的"送转股"式变化、或者是否长期处于低价区间)去部分剥掉贴现率效应——这是下一条的来源。
3. **拆股到更低价格 → 投资者预期偏度立刻跳升,但实际偏度反而下降**:Birru & Wang (2016) 用期权隐含偏度发现,拆股到更低名义价格当天,投资者的偏度预期跳升 40% 以上,但事后实现的偏度是下降的;反向(缩股/合股变贵)则反过来。(出处 7)
   → 翻译:如果以后要给 N-b 配外围,**"最近是否发生过使名义股价降低的事件"(例如送转股)是一个比静态价格水平更锐的变量**——但这类事件在我们的字段里同样算不出来(没有股本变动的具体类型标签),只能停留在文献层面提醒 PI:N-b 现在这个写法测的是"低价股信念溢价"里最粗的那一部分,文献里更干净的版本需要我们没有的字段。
4. **管理层"投喂"低价偏好的机制(catering)**:Baker, Greenwood & Wurgler (2009) 提出,当投资者偏好低价股时,管理层会主动把股价维持在低位(通过拆股等手段),这是公司行为对投资者偏好的"迎合"。(出处 9)
   → 这条解释了为什么"低价"这个特征会持续存在(不会被公司自己的拆股行为抹掉),但它同时说明 **−log(股价) 这个变量里混了"管理层选择"**,不是纯粹的市场定价异象,这是对 N-b 机制判断的又一层复杂化,建议 PI 在 missions 里只说"低价股溢价,文献上有信念/迎合两种解释",不要只说一种。
5. **与彩票 / MAX 特征的关系**:Bali, Cakici & Whitelaw (2011) 发现 high-MAX(近一月最大单日收益)股票偏小、偏低价、特质波动率更高,且 MAX 对未来收益有显著负向预测力。(出处 10)。但后续 Gorman, Akhtar, Durand & Gould (2022, *Critical Finance Review*) 用事件研究反驳了"彩票偏好"的解释,认为这更像是对极端单日涨幅的**过度反应**,跟股票是否事前被归类为"彩票型"无关。(出处 11)
   → 翻译给 PI 的问题 (c):**低价与 MAX/彩票特征高度共生,但哪个是因哪个是果,文献内部还在打架**——如果 N-b 的效果后面被发现主要来自"低价股恰好是近期有过暴涨的股票",这正是 Gorman et al. 的"过度反应"解释在起作用,而不是独立的"名义股价幻觉",这是 N-b 结果出来后要做的一个必要性检验(控一下近期最大单日收益)。

---

## 题目 3 —— 自由流通比例 / 股权集中度(对准 N-c)

本题搜索预算不够,证据明显比前两题薄,以下按能确认到什么程度分层写。

**处理方式:**

1. **在中国市场,"自由流通"被当成一个独立的风险/定价因子,而不只是流动性代理**:Wang & Xu (2004, *Financial Analysts Journal*) 用 1996–2002 年 A 股数据做 Fama-French 三因子检验,发现单用市场因子只能解释 81% 的组合收益方差;加入规模因子和**自由流通盘(free float)因子**后提升到 90%。他们给的理由是:A 股市场投机性强、政府持股比例高、会计信息质量低,"自由流通"是比账面市值比更能代表公司基本面质量的变量。(出处 12)
   → 翻译:这是对 N-c 最直接的外部支持——**在扣掉市值之后,流通盘比例本身在 A 股历史上被独立证明有增量解释力**,不是规模的重复品。但这篇是 2004 年、样本止于 2002 年,股改(2005–2006)之后限售股结构整体变了,外推到我们 2018–2023 的样本期需要打折扣。
2. **"自由流通比例"在文献里经常被架在"投机 vs 流动性"这两种解释之间,而不是被单独当成一个明确方向的因子**:Mei, Scheinkman & Xiong (2004) 研究 A/B 股溢价,专门去看"流通盘大小"和"换手率"的关系,想分离出 A 股交易更多是由投机(观点分歧)驱动还是由流动性驱动,结论偏向**投机**解释。(出处 13)
   → 这直接回答 PI 问题 (c) 的另一半:**文献里处理"自由流通比例会不会被换手率/流动性控制吃掉"这个问题的方法,就是显式去看流通盘与换手率的联立关系**,而不是简单做一次回归控制。这提示如果 N-c 的效果后面要立得住,应该专门做一次"流通比例 vs 我们那条 30 日成交额流动性控制"的交叉检验,而不能只看残差后还显著就完事——因为文献本身说这两者可能是同一个"投机强度"的两张脸。
3. **流通盘变化在中国有一条确认过的公司金融渠道**:同题目 1 的出处 4(Fang, Song, Nofsinger & Wang 2017)——非流通股占比下降(流通比例提高)与现金分红下降相关,作者把流通受限解释成一种"需要被补偿的摩擦",补偿方式是分红。这条可以类比到 N-c:自由流通比例低,可能对应"治理 / 大股东锁仓"的代理,而不是单纯的流动性。(出处 4)
4. **搜不到的部分(明确标注)**:
   - 没有搜到 2010 年之后、专门拿"自由流通市值 / 总市值"这个比率做 Fama-MacBeth 式横截面收益回归、并同时控制市值与流动性的中国研究。中文检索返回的几篇(基于 Feltham-Ohlson 模型的流通股比例对股价的影响、354 只次新股解禁超额收益回归)都是**事件研究或定价模型推导**,不是标准的横截面因子检验,而且我没有独立打开全文核实具体数字,**这几条不计入出处列表,只在这里提一下方向供 PI 参考,不作为结论支撑**。
   - 没有搜到专门报告"国有股比例"对 A 股横截面收益方向性影响的、2023-08 之前发表的因子检验类论文;搜到的几篇(默认风险与国企身份的交互、股权集中度与公司估值)都是相邻话题,不直接回答"这个比率本身能不能预测收益"。

---

## 题目 4 —— 分钟级无成交 / 零收益频率,以及低基数分类变量当筛(对准 N-d / N-e、核心①②的"筛"用法)

**处理方式:**

1. **零收益频率是一个经典的、只用日频价格就能算的流动性代理,构造方式是"滚动窗口里零收益天数的占比"**:Lesmond, Ogden & Trzcinka (1999, *Review of Financial Studies*) 提出的 LOT 度量,核心逻辑是:当某天的信息价值不足以覆盖交易成本时,投资者选择不交易,当天收益记为零;零收益天数占比越高,隐含的交易成本越高。他们在月度/区间频率上用这个比例估计有效交易成本。(出处 14)
   → 直接翻译:这给 N-d 的 `day_zero_ratio(Ret)` / `cross_max(day_zero_ratio(Ret), 15)` 这类写法提供了文献原型——**但文献用的是"日频收益是否为零",我们已经在用的是"分钟级无成交",是同一个思路往下钻了一层,文献本身没有验证过分钟级版本是否更好或更差**,这是我们比文献更细的地方,没有现成文献背书,风险自己扛。
2. **零收益度量在新兴市场/跨国样本里被反复验证是有效的流动性代理,且与 Amihud 价格冲击度量不是同一个东西**:Bekaert, Harvey & Lundblad 发现这个零收益比例跟传统交易成本度量高度相关;有研究发现在 20 个新兴市场里,零收益度量比 Amihud 度量更能解释非流动性溢价。(出处 15,**细节来自二级搜索摘要,没有独立打开原文核实数字,标注为部分核实**)
   → 翻译给 PI:零收益频率类因子(日频或我们的分钟级版本)**和 Amihud(价量冲击)类度量不是同义词,方向上都该预测正收益(更不流动 → 补偿更高)**,但构造逻辑不同,如果以后要同时用两个,不该指望库禁令会自动拦下重复——它们的算子骨架确实不同。
3. **Amihud 度量本身对"零成交日怎么处理"有明确的构造讲究,直接相关我们在 N-d 里提的 `day_zero_ratio`**:Amihud (2002, *Journal of Financial Markets*) 的原始度量是"日绝对收益 / 当日成交额"的区间平均,只在有成交的日子上定义。后续方法论研究指出,如果简单地把零成交日从平均里剔除(只在有成交的日子上取平均),会**系统性低估**真实的非流动性,原因是分母的"可能交易天数"和"实际交易天数"被混用了;正确做法应该显式把零成交天数计入分母,而不是直接跳过。(出处 16、17)
   → 这是最具体的一条可操作建议:**如果以后 N-d / 核心①②要配合一个"成交额流动性"类的外围算子,分钟立方体里统计 Amihud 类度量时,不能只在"有成交的分钟/日子"上取平均,要把"无成交"本身计入分母**——这恰好是 `day_pos_ratio` 当年犯的同一类错(用子集定义分母),§1.4 的裁决和这条文献建议是同一个教训的两次重复,值得写进给 PI 的提醒里当"通用检查清单"的一条。
4. **低基数分类变量(ST / 板块 / 价格限制档位)在中国 A 股文献里,通常是作为"事前剔除"的样本处理,而不是进回归当一个连续暴露**:有研究在做 A 股应计异象检验时,直接把 ST、PT(特别转让)公司从样本里剔除,再去看异象是否还成立(引用来源是 Wang 2005,我没有独立核实到 Wang 2005 原文,这条是二手引用,标注部分核实)。另有研究确认 ST 股票面临 5% 涨跌幅限制(远低于主板 10%、创业板/科创板 20%),财报要被强制审计。(出处 18,19;**均为二级来源,部分内容未独立核实原文**)
   → 直接翻译,对应核心② 和 N-e:**文献对这类变量的标准做法确实是"筛"不是"因子"**——先把 ST/特殊板块从多头候选池里拿掉,再去测别的因子,这和 `analysis.md` 里"`cs_last_high20(y, cs_normalize(BoardCode))` / 用 `LimitWidth` 当 `_rank_block` 的 x 位"这个处理方式方向一致,文献给的是"事前硬剔除"(更接近 `cross_max` 式的掩码),我们现在的写法是"软排除"(占比筛),两者机制相通但强度不同,**这条可以写进 N-e 的说明,但不改变 E/N 候选本身**。
5. **搜不到的部分(明确标注)**:
   - 没有搜到任何论文**量化**报告"事前剔除 ST 后,纯多头组合扣费后夏普改善了多少"这个具体数字。这正是题目 4 问题 (c) 的核心,**搜不到**,不编。
   - 没有搜到专门针对分钟级(而非日频)零成交/零收益度量、且发表于 2023-08 之前的中国 A 股实证论文;能找到的都是日频 LOT/零收益类研究,分钟级是我们自己的推断,没有文献直接对照。

---

## 出处列表

**出处 1** — Daniel, Kent; Titman, Sheridan. "Market Reactions to Tangible and Intangible Information." *Journal of Finance*, 61(4), 1605–1643. 2006-08. 来源:American Finance Association(同期 NBER Working Paper No. 9743)。链接:https://ideas.repec.org/p/nbr/nberwo/9743.html 。verified: true(搜索结果给出卷期页码与核心结论一致)。

**出处 2** — Pontiff, Jeffrey; Woodgate, Artemiza. "Share Issuance and Cross-Sectional Returns." *Journal of Finance*, 63(2), 921–945. 2008-04. 来源:American Finance Association。链接:https://ideas.repec.org/a/bla/jfinan/v63y2008i2p921-945.html 。verified: true(页面给出卷期页码、月份及摘要要点)。

**出处 3** — McLean, R. David; Pontiff, Jeffrey; Watanabe, Akiko. "Share issuance and cross-sectional returns: International evidence." *Journal of Financial Economics*, 94(1), 1–17. 2009. 来源:Elsevier。链接:https://ideas.repec.org/a/eee/jfinec/v94y2009i1p1-17.html 。verified: true(出现在搜索结果且卷期页码一致;未独立核实月份)。

**出处 4** — Fang, Hongyan; Song, Zhihui; Nofsinger, John R.; Wang, Yuyue. "Trading restrictions and firm dividends: The share lockup expiration experience in China." *Journal of Banking & Finance*, 85, 83–98. 2017(月份页面未列出)。来源:Elsevier,DOI 10.1016/j.jbankfin.2017.08.012。链接:https://ideas.repec.org/a/eee/jbfina/v85y2017icp83-98.html 。verified: true(直接 WebFetch 该页面拿到标题、作者、卷期页码与摘要)。

**出处 5** — 作者姓氏推断为 Liao / Liu / Wang("LLW",全名未核实);文件名 `LLW_splitshare20091030.pdf`,标题未能从可读文本确认(原始 PDF 二进制无法解析,WebFetch 两次都失败)。推断主题:中国股改限售股解禁事件研究,[-120,+20] 交易日窗口,约 -14% 异常收益、约 +140% 成交量放大。年份:约 2009-10(文件名日期)。来源:EFMA(欧洲财务管理学会)2010 年中国专题研讨会论文集。链接:https://efmaefm.org/0EFMSYMPOSIUM/2010-China/papers/LLW_splitshare20091030.pdf 。verified: **false**(我自己两次 WebFetch 该 PDF 都只拿到无法解读的二进制流,具体数字和作者全名来自 WebSearch 工具给出的摘要而非我本人读到的原文,不满足"确实在搜索结果或页面上看到"的较高标准——按规则这里应算部分核实,结论里已注明"细节单薄"并未单独作为任何处理方式的唯一支撑)。

**出处 6** — 上海交通大学学报(或其英文版)刊载论文,主题为中国 IPO 限售股解禁对流动性(买卖价差)的影响,信息披露质量的调节作用。作者、年-月、卷期未核实。来源:`xuebao.sjtu.edu.cn`。链接:https://xuebao.sjtu.edu.cn/sjtu_en/EN/abstract/article/1007-1172/42542 。verified: false(只看到搜索摘要,未打开原文确认作者和年份,日期也无法确认是否在 2023-08-08 之前,**这条只作为旁证提及,不单独支撑任何结论**)。

**出处 7** — Birru, Justin; Wang, Baolian. "Nominal Price Illusion." *Journal of Financial Economics*, 119(3), 578–598. 2016(月份页面未列出)。来源:Elsevier,DOI 10.1016/j.jfineco.2016.01.027。链接:https://ideas.repec.org/a/eee/jfinec/v119y2016i3p578-598.html 。verified: true(直接 WebFetch 该页面拿到标题、作者、卷期页码与摘要)。

**出处 8** — Birru, Justin; Wang, Baolian. "The Nominal Price Premium." Dice Center Working Paper 2015-15. 2015(月份未列出)。来源:Ohio State University, Charles A. Dice Center for Research in Financial Economics。链接:https://ideas.repec.org/p/ecl/ohidic/2015-15.html 。verified: true(直接 WebFetch 该页面拿到标题、作者、工作论文编号与摘要)。首版日期在 2023-08-08 之前,可用。

**出处 9** — Baker, Malcolm; Greenwood, Robin; Wurgler, Jeffrey. "Catering through Nominal Share Prices." *Journal of Finance*, 64(6), 2559–2590. 2009-12。来源:American Finance Association(同期 NBER Working Paper No. 13762)。链接:https://www.nber.org/papers/w13762.ack 。verified: true(搜索结果给出卷期页码、月份,与 NBER 工作论文编号对应)。

**出处 10** — Bali, Turan G.; Cakici, Nusret; Whitelaw, Robert F. "Maxing Out: Stocks as Lotteries and the Cross-Section of Expected Returns." *Journal of Financial Economics*, 99(2), 427–446. 2011。来源:Elsevier。链接:https://pages.stern.nyu.edu/~rwhitela/cvWhitelaw.pdf(个人简历页列出该文卷期信息,原文未独立打开)。verified: true(卷期页码经三个独立来源交叉确认一致,但未独立读到原文摘要全文,结论性描述来自搜索摘要)。

**出处 11** — Gorman, Jake; Akhtar, Farida; Durand, Robert B.; Gould, John. "It Could Be Overreaction, Not Lottery Seeking, That Is Behind Bali, Cakici and Whitelaw's Max Effect." *Critical Finance Review*, 11(3-4), 647–675. 2022-08。来源:now publishers,DOI 10.1561/104.00000123。链接:https://ideas.repec.org/a/now/jnlcfr/104.00000123.html 。verified: true(直接 WebFetch 该页面拿到标题、作者、卷期页码、年月与摘要)。

**出处 12** — Wang, Fenghua; Xu, Yexiao. "What Determines Chinese Stock Returns?" *Financial Analysts Journal*, 60(6), 65–77. 2004-11。来源:Taylor & Francis(CFA Institute),DOI 10.2469/faj.v60.n6.2674。链接:https://ideas.repec.org/a/taf/ufajxx/v60y2004i6p65-77.html 。verified: true(直接 WebFetch 该页面拿到标题、作者、卷期页码、年月与摘要)。

**出处 13** — Mei, Jianping; Scheinkman, Jose A.; Xiong, Wei. "Speculative Trading and Stock Prices: An Analysis of Chinese A-B Share Premia." NYU Stern Finance Working Paper No. FIN-03-017. 2004-09(署名 issued 2004-09-14)。来源:NYU Stern School of Business Faculty Digital Archive。链接:https://archive.nyu.edu/handle/2451/27188 。verified: true(直接 WebFetch 该页面拿到标题、作者、工作论文编号与发布日期)。

**出处 14** — Lesmond, David A.; Ogden, Joseph P.; Trzcinka, Charles A. "A New Estimate of Transaction Costs." *The Review of Financial Studies*, 12(5), 1113–1141. 1999。来源:Oxford University Press(美国金融学会)。链接:https://ideas.repec.org/a/oup/rfinst/v12y1999i5p1113-41.html 。verified: true(搜索结果给出卷期页码,核心构造逻辑——零收益比例代理交易成本——与多条独立二级来源一致)。

**出处 15** — 关于零收益度量在新兴市场优于 Amihud 度量、以及 Bekaert-Harvey-Lundblad 发现零收益与传统交易成本高度相关这两条,均来自搜索结果的二级摘要,未独立确认原始论文标题、作者全名、年份和期刊。verified: false。**只作为旁证,不单独支撑任何处理方式的唯一结论**(题目 4 处理方式 2 的主结论由出处 14 支撑)。

**出处 16** — Amihud, Yakov. "Illiquidity and Stock Returns: Cross-Section and Time-Series Effects." *Journal of Financial Markets*, 5, 31–56. 2002。来源:Elsevier。链接:https://www.cis.upenn.edu/~mkearns/finread/amihud.pdf 。verified: true(多条独立来源交叉确认卷期页码与核心构造——日绝对收益/成交额之比——一致;原始度量只在有成交日定义,与出处 17 的"零成交日处理"问题衔接)。

**出处 17** — Brunel University 工作论文,主题为 Amihud 非流动性比率在包含零成交日时的系统性偏差,以及剔除零成交日会低估真实非流动性的论证与重新标度方法。作者、题目全文、年份均未独立核实。来源:`bura.brunel.ac.uk`。链接:https://bura.brunel.ac.uk/bitstream/2438/20476/1/FullText.pdf 。verified: false(内容来自搜索摘要,未独立打开原文确认;**题目 4 处理方式 3 的"不能只在有成交日上平均"这条建议主要依据是这篇未核实原文的论文,置信度低于其他条目,给 PI 的提醒里已经注明是方法论层面的一般性原则,不是某个具体 A 股实证结果**)。

**出处 18** — 关于中国 A 股应计异象研究中剔除 ST/PT 公司的做法,二次引用自某研究对 Wang (2005) 的转述。Wang (2005) 原文标题、期刊、具体年月均未核实。来源:搜索结果摘要。verified: false。

**出处 19** — 关于 ST 股票面临 5% 涨跌幅限制(主板 10%、创业板/科创板 20%)、财报强制审计等制度事实,来自多条搜索结果摘要(含硕士论文、期刊论文片段),具体条款的权威出处(交易所规则文件)未独立核实。verified: false(**制度事实本身在业内是常识,但本轮没有独立打开交易所官方规则文件核实,按规则标注为未核实,不作为"数学问题"或"陷阱"判断的依据,只作为背景**)。

---

## 给 PI 的小结(方便直接抄进 missions)

- N-a(流通股本扩张率):文献上的标准构造就是我们已经写的那个差分(出处 1、2、3),方向预期为负(扩张越多、未来收益越差),可以直接这样写进机制陈述。
- N-b(低价股):文献警告 raw price 本身是"信念溢价"和"贴现率机械效应"打平的脏信号(出处 7、8),我们的写法(−log 名义股价)测的是这个脏信号的粗糙版本,不是文献里"干净拆开"后的版本(我们缺每股账面值这类字段拆不开),而且它和 MAX/彩票特征、以及管理层拆股选择都有纠缠(出处 9、10、11)——建议在 missions 里把"低价股溢价,信念与迎合两种解释都有,效应可能部分来自近期暴涨股票的过度反应"写清楚,别只说一种机制。
- N-c(自由流通比例):有一篇 2004 年的 A 股研究直接支持"自由流通是独立于规模的定价因子"(出处 12),但同样年代的另一篇提示这类变量在 A 股可能是"投机强度"而不是"流动性"的代理(出处 13),而且样本都在股改之前,外推要打折扣;专门做"自由流通比例 vs 流动性控制"交叉检验的文献没搜到,这条证据在四题里最薄,建议 PI 对 N-c 的预期往下调一档。
- N-d/N-e 与核心①②的"筛"用法:零收益/零成交类度量是有文献原型的标准流动性代理(出处 14、16),但我们把它做到分钟级、文献只做到日频,是我们自己往下钻的一层,没有文献直接验证;Amihud 类度量在构造时"不能只在有成交日上平均"这条工程提醒(出处 17,未核实)值得抄给 PI,因为它和 `day_pos_ratio` 翻车是同一类错误。低基数分类变量当"事前剔除筛"而非"连续因子"是中国 A 股文献里的常见做法(出处 18、19,均未核实原文),方向上支持核心②/N-e 现在的处理方式,但没有搜到任何量化的"剔除 ST 改善多少净夏普"的数字。
