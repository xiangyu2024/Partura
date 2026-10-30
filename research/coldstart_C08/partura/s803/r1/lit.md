# 文献:种子 803,P 组,第 1 轮

对准 `analysis.md` 末尾(§5)给出的 4 个文献题目,分别对应族 A(日内成交时点)、族 B(日内买压)、族 C(隐含价差 / 价格水平混淆)、以及整个口径(中性化后残差 + 次新股污染)。
只用 2023-08-08 之前发表的论文 / 工作论文 / 研究报告;arXiv / SSRN / NBER / CREATES 工作论文以首版日期为准。每条"处理方式"后面用 `[n]` 标出出处,对应文末参考文献列表。
**搜不到的我直接写搜不到**,列在每节末尾,不假装找到。

---

## 题目 1:日内成交量的时间分布(对准族 A)

没有搜到一篇专门以"成交量重心 / centroid"命名并直接做横截面预测力检验的论文——这个具体构造名字在学术文献里不存在,是我们自己的算子命名。能查到的是三条相关但角度不同的文献线,拼起来对应同一个机制。

**处理方式(可翻译成算子语言):**

1. **"相同的量能水平,时点不同"是一个有理论基础的独立维度,不是量能大小的衍生品。** Admati & Pfleiderer (1988) 的模型里,日内成交在什么时点聚集,是知情交易者与流动性交易者策略互动"内生"决定的,不是随机噪声 [1]。→ 支持把 `day_centroid(Amt)` 当作与 `day_sum(Amt)`、`day_std(Amt)` 机制上独立的量,这与 analysis.md §2.1(a)/(b) 的直觉一致。
2. **量、单子失衡的日内周期性本身"解释不了"收益的日内周期性**——Heston, Korajczyk & Sadka (2010) 发现量与单子失衡在日内半小时频率上也有和收益一样的"隔 N 个半小时"周期性,但把它们当回归控制变量加进去,收益的可预测性几乎不变 [2]。→ 对我们的警示:单纯的"今天量能时点"这种**原始水平**信号,即便统计上显著,也有被同一篇文献证明"不是机制本身"的先例;更稳的做法是像族 A 里 `sub(day_centroid(Amt), cross_mean(day_centroid(Amt), 20))` 那样,看**相对自身习惯的偏离**,而不是当天水平。
3. **量能的"时点"信息要和市场状态交互才显现预测力,且存在量-状态的非线性放大。** Gao, Han, Li & Zhou (2018) 的"日内动量"结果里,开盘半小时收益对收盘半小时收益的预测力在"开盘半小时成交量更大"的那些天明显更强 [3]。→ 直接对应 analysis.md §4.3 跨族写法里的 `cs_flip_by_state` / `cs_state_rank`:量能时点类信号按"今天量能是否异常活跃"分状态使用,比不分状态更接近文献找到的那种条件预测力。
4. **在 A 股分钟数据上,"把哪些分钟算作知情交易"这件事本身能做出有横截面预测力的月度指标。** Chen, Liu, Teka & Zhang (2022) 用 1999–2019 年 A 股分钟数据,按"交易的激进程度"识别知情交易方向,构造月度"聪明钱"指标,发现它与未来收益呈**负向**横截面关系 [4]。→ 这条提示:在我们的口径下,"用日内信息挑出一部分分钟再加权平均"(比如 `day_topw_mean`、`day_wmean`)这一类写法,在 A 股数据上已经有过做出效果的文献先例,但他们的信号方向是负的,不能想当然认为"聪明钱多 = 看多"。

**搜不到、不采用:**
- 东方证券 2017 年"聪明钱因子"原始研报(朱剑涛等)——搜到了作者身份的间接佐证(北大讲座页面提到其曾任东方证券首席量化分析师),但搜不到研报原文、具体发表日期或可核实的方法细节,不采用这条,改用 [4] 这篇可核实的学术论文代替。
- 以"intraday volume profile U-shape deviation"直接命名、做横截面检验的论文——搜到的都是"日内收益/波动率 U 型"的研究(不是成交量 U 型本身的偏离指标),不采用。

---

## 题目 2:日内买压 —— 没有逐笔数据时的订单失衡代理(对准族 B)

**处理方式(可翻译成算子语言):**

1. **标准方法(Lee-Ready 规则)需要报价数据,我们没有,但它确立了"跳价方向近似成交方向"这条退路。** Lee & Ready (1991) 的交易方向判定法是"报价规则 + tick 规则"的组合:成交价高于/低于买卖中价判买/判卖,中价成交才退回用 tick 规则 [5]。→ 我们没有盘口数据,相当于**只能用 tick 规则那一半**——这正是 `day_signed_ratio(Ret, Amt)`(按分钟收益正负切成交额)在做的事,文献上这是退化情形,不是我们自己瞎编的近似。
2. **买卖方向的指派应该是"连续加权",不是"按正负硬切"。** Easley, López de Prado & O'Hara (2012) 的 VPIN 用"批量成交分类"(bulk volume classification):每一个成交批次,按该批次价格变动除以价格变动的标准差,用标准正态分布的累积分布函数算出"判为买方发起"的**比例**,而不是简单看涨跌号 [6]。→ 直译成算子语言:比起 `day_signed_ratio(Ret, Amt)` 这种 `sign(Ret)` 硬切,更贴近文献的写法是用一个**连续核**(例如某种标准化后的 `Ret` 过一个 S 形函数)去加权 `Amt`,而不是硬分段——如果我们的算子库里有类似 `cs_sigmoid`/`in_zscore` 之类可以用在分钟收益上的变换,值得往这个方向试一版。
3. **这类"批量分类"代理本身有被证明会系统性地与波动率、成交量机械挂钩的前科,需要自检。** Andersen & Bondarenko (2013) 对 VPIN 的批评是:用真实报价数据做出的精确分类显示,批量分类法(BVC)比标准 tick 规则**更差**,VPIN 对波动率的预测力主要来自分类误差与波动率、成交量本身的机械相关,而不是真的捕捉到了"毒性"订单流 [7]。→ 这是 analysis.md §2.2 讲的"换同类字段 / 窗口减半加倍"自检的文献版本:任何买压代理,如果换成更粗糙或更精细的切分方式后结论跟着大幅变化,很可能是在读分类误差,不是读买压本身。
4. **日度层面,单子失衡存在"当天水平"和"滞后水平"方向相反的经验规律,不能直接线性外推到下一期。** Chordia & Subrahmanyam (2004) 发现:单子失衡本身有自相关,这个自相关会造成"滞后单子失衡"与收益的正向关系,但一旦把**当天**单子失衡放进回归控制住,这个关系会反转;单子失衡策略能挣到统计显著的收益,机制被归因为**存货效应**(做市商/流动性提供者被迫调整库存后的价格压力)[8]。→ 直接对应 analysis.md §2.1(b) 第二条自检建议("把 10 日平均换成当天值,看是不是在吃当日反转"):文献证实了"当天值"和"多日平均值"在单子失衡这一类特征上**真的可能方向相反**,这不是我们过度谨慎,是已知现象。
5. **买卖压力的"水平"本身是另一个已经被记录过的、与"交易活跃度的波动"纠缠的异象维度,要小心重新发现它。** Chordia, Subrahmanyam & Anshuman (2001) 发现换手率 / 成交额的**波动性**(不是水平)与未来收益之间有显著的横截面负向关系,控制规模、账面市值比、动量、交易活跃度水平后依然存在 [9]。→ 警示:如果我们用 `cross_stddev(day_signed_ratio(Ret, Amt), N)` 这种"买压有多不稳定"的写法,要留意它和"交易活跃度波动"这个已知异象维度是不是在读同一个东西——这不在我们的 5 个显式控制里,但審计可能会按"是否在度量同一个东西"把它挡下来,值得 PI 在笔记里主动提一句机制区分。
6. **即使没有逐笔数据,仅用日度收盘价与量就能相当精确地还原日内层面的价格冲击强度(Kyle's λ 的代理)。** Hasbrouck (2009) 用纯日度 CRSP 收盘价数据(Gibbs 抽样)估计的有效交易成本 / 价格冲击指标,在验证样本里与基于高频 TAQ 数据算出的真值相关系数达到 0.965,且该特征对收益的解释力在控制后仍独立于规模效应 [10]。→ 这条支持"日频聚合的买压/冲击代理本身就是靠谱信息来源",不是因为我们没有逐笔数据就必然是弱代理;同时提示要像这篇文献一样,显式检查买压类特征是否独立于规模(我们已有 `LogFloatCap` 控制,方向一致)。

**搜不到、不采用:**
- 专门针对"分钟 K 线(而非逐笔)构造的订单失衡代理"与"逐笔代理"做直接横向比较、报出相关系数或误差的论文——搜到的多是 tick 规则 vs 报价规则(都基于逐笔/报价),没搜到专门分钟 K 线频率的横向验证研究,不采用。

---

## 题目 3:隐含价差 / 流动性度量与价格水平、最小变动价位的混淆(对准族 C)

**处理方式(可翻译成算子语言):**

1. **"收益一阶自相关为负→价差"这条关系本身就是族 C 写法的理论源头,文献对"算不出"的情形有明确、保守的处理,不是让它爆炸。** Roll (1984) 的有效价差 = `2 * sqrt(-Cov(ΔP_t, ΔP_{t-1}))`,只在该序列协方差**为负**时成立;协方差为正时平方根本身无定义,实践中的标准处理是**设为零 / 判定该样本上估计量失效**,而不是对负数强行取绝对值再开方得到一个夸大的数 [11]。→ 这正好是 analysis.md §2.2"数值伪影"那条教训的文献原型:`day_ar1_coefficient(Ret)`、`day_autocorr(Ret,1)` 这类量在跨股票比较时,如果某些股票的自相关恰好翻正(比如涨停锁死日),不该套一个"绝对值再开方"式的变换把它们救成异常大的正数——这正是 `ops_ext.py` 里 `day_es_ratio_hi` 文档记录的那类 bug 的学术对应版本。
2. **区分"价差"和"波动率"的标准手法,是比较同一个量在不同时间尺度上的缩放方式,而不是直接看水平。** Corwin & Schultz (2012) 的核心识别思路是:日内价格区间(High-Low range)里的**波动率成分**随持有期大致线性增长(两天的方差约等于一天的两倍),但**价差成分**不随持有期增长;于是用"一天的 High-Low 比例"和"两天的 High-Low 比例"做对照,把两者分离出来 [12]。→ 这与我们定位脚本本来就有的"窗口减半 / 加倍"敏感性检查是同一个识别逻辑:如果族 C 的某个候选在窗口加倍时的变化幅度,正好符合"波动率该涨的量"而不是"价差该保持不变的量",就是在读波动率,不是在读价差/流动性冲击——这条可以直接写进下一轮核心卡的自检清单,给"窗口加倍"检查一个理论依据,而不只是经验直觉。
3. **更彻底的做法是干脆绕开买卖价差弹跳假设,换一个不依赖"跳价符号"的统计量。** Abdi & Ranaldo (2017) 的估计量不用连续价格变动的协方差,而是用"收盘价 vs 当日(log 高+log 低)/2 的中间价"的协方差,从机制上就不依赖价差弹跳这个假设,对 TAQ 有效价差的跟踪精度比 Roll 类估计量更好,且**对流动性差的股票(通常是低价、小盘股)效果反而相对更好** [13]。→ 这条直接对应 analysis.md 族 C 的"价格水平混淆"担忧:文献里专门验证过,换一种不依赖价格跳动符号的构造方式,恰恰能在最容易被价格水平污染的那批股票上表现更稳,这是我们 `cs_bucket_demean(..., day_last(Close))` 这个"按价格桶去均值"自检写法的直接文献支持——而不是我们自己拍脑袋加的保险。
4. **低频代理在跨指标横向验证(horse race)里经常被发现其实是在代理别的已知特征,而不是真正的流动性。** Goyenko, Holden & Trzcinka (2009) 系统比较了一大批可以从日度数据算出的流动性代理(价差类、冲击类),用高频 TAQ/Rule 605 数据做基准做"赛马",发现不同代理在不同维度上表现差异很大,其中价差类的新估计量整体表现最好,Amihud 类冲击代理在价格冲击维度表现好 [14]。→ 这是"任何一个日内微观结构代理,在真正验证之前都应该怀疑它其实是在代理别的东西"这一研究设计的文献范式,支持我们在族 C 自检里特别强调"先交一个按价格桶去均值的版本,再交一个不去均值的版本"做对照。

**搜不到、不采用:**
- 专门针对"最小变动价位(tick size)如何机械影响 A 股分钟收益自相关"的论文——搜到的是美股/期货市场 tick size 变化(十进制化、E-mini)对价差估计量精度的影响研究,没搜到 A 股最小价格变动单位(1 分钱)下的专门研究,不采用这部分外推到 A 股的具体数字。

---

## 题目 4:中性化之后还剩什么,以及次新股 / 停牌污染(对准整个口径)

**处理方式(可翻译成算子语言):**

1. **A 股市场里,"次新 / 壳价值"污染的标准处理方式是按市值百分位整体剔除,不是按上市天数设一个硬阈值。** Liu, Stambaugh & Yuan (2019, NBER 工作论文版 2018) 在构造 A 股的规模、价值因子时,**无条件剔除全市场最小的 30% 个股**后再构造任何因子,理由是这部分股票的市值里有相当大比例(他们在不同版本里给出约 30%–40%)反映的是"壳资源"的期权价值(可被借壳上市),而不是基本面;他们统计到中国的反向收购壳资源里 83% 来自这最小的 30% [16]。→ 这是能查到、有具体数字的处理方式,直接可用:如果我们要在样本内自查某个候选对"次新 / 壳价值"的依赖,比起只看 `ListAge`,更接近文献做法的是看它对**全市场最小市值分位**的依赖(`LogFloatCap` 的极左尾),这与我们已有的市值控制在方向上是一致的,但文献的做法是**整体剔除**而不是"控制残差"——这条差异值得写进 notebook:我们的奖励口径只对市值做残差化(线性+U型+S型),并不剔除最小市值的股票,所以"次新+小市值"的污染即使残差化后也可能没被完全去掉,文献的做法比我们更激进。
2. **"控制已知特征后看残差是否还有解释力"本身是一套成熟的研究设计,其中专门会检查新发现的特征是不是独立于规模。** Hasbrouck (2009) 明确报告其日度价格冲击特征对收益的解释力在控制后"看起来独立于规模效应",这是研究者主动做的检验,不是默认成立的 [10]。Goyenko, Holden & Trzcinka (2009) 的赛马设计本质上也是"同一批候选代理,谁在控制别的代理后还剩预测力"的残差检验范式 [14]。→ 支持 analysis.md §2.1(b) 的做法本身(控制 5 个已知特征取残差),也提示我们在给出任何 N 候选时,最好主动报告"控制 `LogFloatCap` 之后,该候选在最小市值分位 / 最短上市时间分位的子样本里是否依然显著",作为审计员那句"如果它有 alpha,最可能来自哪里"的佐证材料。

**搜不到、不采用:**
- 专门给出"剔除上市不满 N 个交易日个股"这一具体天数规则、且可核实发表日期在 2023-08-08 之前的 A 股因子构造论文——搜到的都是市值百分位剔除法([16])或首日 IPO 超额收益研究(样本偏早、聚焦上市首日定价而非后续因子污染),没有搜到带精确天数阈值的方法论文献,不采用具体数字。
- 专门讨论"停牌样本在横截面因子检验里如何处理(保留/剔除/插值)"并给出可核实方法论的学术论文——搜到的是停牌制度背景报道与一篇关于"随意停牌"监管的实证论文摘要(未核实到可引用的具体处理方法细节),不采用。
- "风格中性化之后 A 股日内 / 分钟级特征还剩多少横截面预测力"这个问题的直接综述或元分析——没搜到专门的综述文章,只有分散的单篇证据(见题目 1-3 的出处),不采用某个不存在的"综述结论"。

---

## 参考文献(全部字段;`verified` 为 true 表示本次确实在搜索结果或网页上看到)

1. **A Theory of Intraday Patterns: Volume and Price Variability**
   作者:Anat R. Admati, Paul Pfleiderer。年-月:1988(无月份信息)。来源:*Review of Financial Studies*, 1(1), 3–40。
   链接:https://www.gsb.stanford.edu/faculty-research/publications/theory-intraday-patterns-volume-price-variability
   verified: true(WebSearch 命中标题、卷期页码)

2. **Intraday Patterns in the Cross-section of Stock Returns**
   作者:Steven L. Heston, Robert A. Korajczyk, Ronnie Sadka。年-月:2010-08(《Journal of Finance》正刊;印刷页码本次未逐一核实,仅核实标题/作者/期刊/年份)。来源:*Journal of Finance*, 65(4)。
   链接:https://ar5iv.arxiv.org/html/1005.3535
   verified: true(WebFetch 直接读取了 arXiv/ar5iv 全文摘要)

3. **Market Intraday Momentum**
   作者:Lei Gao, Yufeng Han, Sophia Zhengzi Li, Guofu Zhou。年-月:2018-08。来源:*Journal of Financial Economics*, 129(2), 394–414。
   链接:https://profiles.wustl.edu/en/publications/market-intraday-momentum/
   verified: true(WebFetch 直接读取了该页面给出的完整引用与摘要)

4. **Smart Money in China's A-Share Market: Evidence from Big Data**
   作者:Zhenhua Chen, Zhenya Liu, Hanen Teka, Yifan Zhang。年-月:2022(月份信息页面未给出)。来源:*Research in International Business and Finance*, 61, 文章号 101663,DOI 10.1016/j.ribaf.2022.101663。
   链接:https://ideas.repec.org/a/eee/riibaf/v61y2022ics0275531922000514.html
   verified: true(WebFetch 直接读取了引用信息与摘要)

5. **Inferring Trade Direction from Intraday Data**
   作者:Charles M.C. Lee, Mark J. Ready。年-月:1991-06。来源:*Journal of Finance*, 46(2), 733–746。
   链接:https://ideas.repec.org/a/bla/jfinan/v46y1991i2p733-46.html
   verified: true(WebSearch 命中完整卷期页码)

6. **Flow Toxicity and Liquidity in a High-Frequency World**
   作者:David Easley, Marcos M. López de Prado, Maureen O'Hara。年-月:2012(月份未给出)。来源:*Review of Financial Studies*, 25(5), 1457–1493。
   链接:https://ideas.repec.org/a/oup/rfinst/v25y2012i5p1457-1493.html
   verified: true(WebFetch 直接读取了引用信息与摘要)

7. **Reflecting on the VPIN Dispute**
   作者:Torben G. Andersen, Oleg Bondarenko。年-月:2013(月份未给出)。来源:CREATES Research Paper 2013-42,Aarhus University(工作论文)。
   链接:https://ideas.repec.org/p/aah/create/2013-42.html
   verified: true(WebFetch 直接读取了标题与作者信息)

8. **Order Imbalance and Individual Stock Returns: Theory and Evidence**
   作者:Tarun Chordia, Avanidhar Subrahmanyam。年-月:2004(月份未给出)。来源:*Journal of Financial Economics*, 72(3), 485–518,DOI 10.1016/S0304-405X(03)00175-2。
   链接:https://academicnewsletter.sufe.edu.cn/info/357679
   verified: true(WebSearch 命中完整卷期页码与 DOI)

9. **Trading Activity and Expected Stock Returns**
   作者:Tarun Chordia, Avanidhar Subrahmanyam, V. Ravi Anshuman。年-月:2001(月份未给出)。来源:*Journal of Financial Economics*, 59(1), 3–32。
   链接:https://research.iimb.ac.in/fac_pubs/1268
   verified: true(WebSearch 命中完整卷期页码)

10. **Trading Costs and Returns for US Equities: Estimating Effective Costs from Daily Data**
    作者:Joel Hasbrouck。年-月:2009-06。来源:*Journal of Finance*, 64(3), 1445–1477。
    链接:https://ideas.repec.org/a/bla/jfinan/v64y2009i3p1445-1477.html
    verified: true(WebSearch 命中完整卷期页码与摘要要点)

11. **A Simple Implicit Measure of the Effective Bid-Ask Spread in an Efficient Market**
    作者:Richard Roll。年-月:1984-09。来源:*Journal of Finance*, 39(4), 1127–1139。
    链接:https://www.bauer.uh.edu/rsusmel/phd/roll1984.pdf
    verified: true(WebFetch 读取了该 PDF,通过嵌入的 JSTOR SICI 标识确认刊物/卷期/年月;估计量公式本身据多个检索结果交叉确认)

12. **A Simple Way to Estimate Bid-Ask Spreads from Daily High and Low Prices**
    作者:Shane A. Corwin, Paul Schultz。年-月:2012(月份未给出;DOI 10.1111/j.1540-6261.2012.01729.x)。来源:*Journal of Finance*, 67(2), 719–759(另有来源给 719–760,页码尾数两个版本不一致)。
    链接:https://ideas.repec.org/a/oup/rfinst/v30y2017i12p4437-4480..html 的交叉引用页及 academicnewsletter.sufe.edu.cn/info/360309
    verified: true(WebSearch 多个独立来源交叉确认标题/作者/期刊/卷期)

13. **A Simple Estimation of Bid-Ask Spreads from Daily Close, High, and Low Prices**
    作者:Farshid Abdi, Angelo Ranaldo。年-月:2017(月份未给出)。来源:*Review of Financial Studies*, 30(12), 4437–4480。
    链接:https://ideas.repec.org/a/oup/rfinst/v30y2017i12p4437-4480..html
    verified: true(WebFetch 直接读取了引用信息与摘要)

14. **Do Liquidity Measures Measure Liquidity?**
    作者:Ruslan Y. Goyenko, Craig W. Holden, Charles A. Trzcinka。年-月:2009-05。来源:*Journal of Financial Economics*, 92(2), 153–181。
    链接:https://ideas.repec.org/a/eee/jfinec/v92y2009i2p153-181.html
    verified: true(WebSearch 多个独立来源交叉确认完整卷期页码,含获奖信息)

15. **Illiquidity and Stock Returns: Cross-Section and Time-Series Effects**
    作者:Yakov Amihud。年-月:2002(月份未给出)。来源:*Journal of Financial Markets*, 5(1), 31–56。
    链接:https://www.casact.org/abstract/illiquidity-and-stock-returns-cross-section-and-time-series-effects
    verified: true(WebSearch 多个独立来源交叉确认完整卷期页码)

16. **Size and Value in China**
    作者:Jianan Liu, Robert F. Stambaugh, Yu Yuan。年-月:NBER 工作论文 2018-03(Working Paper 24458);正式发表 *Journal of Financial Economics*, 134(1), 48–69, 2019(月份未给出)。
    链接:https://faculty.wharton.upenn.edu/wp-content/uploads/2018/03/Size-and-Value-in-China.pdf(NBER 版本:https://www.nber.org/papers/w24458.pdf)
    verified: true(剔除最小 30% 个股及壳价值比例的具体数字直接出现在 WebSearch 对该 PDF 的检索摘录中)

---

## 给 PI 的一句话总结

四个题目里,**最能直接落成算子写法、且有数字支撑的是题目 3**(Roll / Corwin-Schultz / Abdi-Ranaldo 这条线,支持族 C 已经在用的"差额 / 自身历史标准化 / 按价格桶去均值"写法,并且给了"窗口加倍"自检一个理论依据,不只是经验直觉)。
题目 1、2 的文献更多是从机制和自检角度提供佐证,没有一个能直接照抄的公式;其中 Chen, Liu, Teka & Zhang (2022) [4] 是唯一一篇在 A 股分钟数据上真正做出横截面预测力检验的文献,但搜索没能拿到它的具体构造细节(只到摘要层级)。
题目 4 唯一查到的具体处理方式是 Liu-Stambaugh-Yuan 的"剔除最小市值 30%"[16],比我们现在"只对市值取残差、不剔除"的做法更激进——这条差异建议写进 notebook 的事先信念,而不是当作一定要照做的规则。
