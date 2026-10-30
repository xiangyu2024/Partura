# 文献笔记:种子 808,第 1 轮

对准 `analysis.md` §5 的四个题目。每条"处理方式"都尽量写成可以直接对照我们算子语言的句子
(`ts_max`/`ts_mean`/`ts_argmax`/`day_wstd`/`day_wmean`/`day_std`/`cs_demean`/`cs_rank`/`cs_bucket_demean` 等),
出处标注 `verified: true` 的,都是我这次用 WebSearch/WebFetch 真的在搜索结果或页面正文里看到了标题与描述;
`verified: false` 的,是我只在转述/二手摘要里看到、没有拿到一次独立确认,或者是我自己的背景知识、这次没查到独立来源 —— 两种情况我都写明。
找不到的地方,下面直接写"没搜到",不补。
所有引用都满足"2023-08-08 之前"(大多是 2000s–2020 的已发表论文,远早于截止日)。

---

## 题 1 —— 对准核心 A / head1:`ts_max(cs_demean(day_wstd(Ret, Volume)), 148)`

### (a) 极值统计量 vs 同期波动均值水平:独立还是被吸收?

**处理方式 1——"扣掉水平、看极值"在文献里是反过来被证明的,而不是我们这次才发现的。**
Bali, Cakici & Whitelaw (2011) 的 MAX(过去一个月的单日最大收益率,对照算子写法接近
`ts_max(Ret, 21)`)与 Ang, Hodrick, Xing & Zhang (2006) 的特质波动率(IVOL,水平统计量,对照
`cross_mean(day_std(Ret), 21)` 这一类)在横截面上同时存在时,结果不是"MAX 被 IVOL 吸收",而是反过来:
**加入 MAX 之后,IVOL 原来的"高波动→低收益"异象会被逆转/消失**;也就是极值统计量比水平统计量更靠近真正的定价来源。
翻译成我们的问题:`vol` 控制(`cross_mean(day_std(Ret), 20)`,水平)理论上**不应该**吃掉 `ts_max(day_wstd(...), 148)`
(极值)的 alpha,文献里的先例方向和这次的奖励设计思路一致。
- 出处:Bali, T.G., Cakici, N., Whitelaw, R.F. "Maxing Out: Stocks as Lotteries and the Cross-Section of Expected Returns." *Journal of Financial Economics*, 2011, vol. 99, pp. 427–446(工作论文版 NBER WP 14804)。来源:academicnewsletter.sufe.edu.cn/info/356984;nber.org/papers/w14804。`verified: true`
- 出处:Ang, A., Hodrick, R.J., Xing, Y., Zhang, X. "The Cross-Section of Volatility and Expected Returns." *Journal of Finance*, 2006, vol. 61(1), pp. 259–299(工作论文版 NBER WP 10852)。来源:nber.org/papers/w10852;academicnewsletter.sufe.edu.cn/info/361024。`verified: true`

**处理方式 2——MAX 与 IVOL 横截面相关可以到 ~90%,但控制 MAX 之后 IVOL 异象消失(不是反过来)。**
Egginton & Hur (2018) 直接报告两者的横截面相关接近 90%,并重复确认"控制 MAX 之后 IVOL 的异象消失"。
这进一步支持:即使两个统计量高度相关,起作用的是极值那一侧。
- 出处:Egginton, J., Hur, J. "The Robust Maximum Daily Return Effect as Demand for Lottery and Idiosyncratic Volatility Puzzle."(2018,工作论文/会议稿)。来源:scholarworks.boisestate.edu/marketing_facpubs/48;latech.elsevierpure.com(作者页)。期刊/定稿出处未能进一步核实。`verified: true`(标题与年份、结论描述确认过;最终发表期刊未核实)

**处理方式 3——在 A 股,MAX 效应和 IVOL 效应是两个独立并存的东西,谁也没吸收谁。**
这是对我们场景最直接的证据:Nartea, Kong & Wu (2017) 用中国市场数据复现了 MAX 效应(方向与美欧一致,
MAX 高→未来收益低),但发现**中国的 MAX 效应没有削弱 IVOL 的反转异象** —— 两者在 A 股横截面上是独立的信息源。
这正好对应 analysis.md 的论断"control 只覆盖 20 日的水平,半年尺度的极值是缝隙":文献里在同一个市场、同样的
"水平 vs 极值"对照下,也观察到二者不是同一件事。
- 出处:Nartea, G.V., Kong, D., Wu, J. "Do Extreme Returns Matter in Emerging Markets? Evidence from the Chinese Stock Market." *Journal of Banking & Finance*, 2017, vol. 76, pp. 189–197。来源:ideas.repec.org/a/eee/jbfina/v76y2017icp189-197.html。`verified: true`

### (b) 回看期长度:文献用多长,有没有报告过 100–150 个交易日这个量级?

**没搜到**直接报告"最优回看期在 100–150 个交易日"这个量级的文献。能确认的两个锚点离这个区间都有一段距离:
- 经典 MAX 用的是**一个月**(约 21 个交易日)的单日最大收益率,比我们的窗口短得多(同一篇 Bali et al. 2011,见上)。
- 另一端是 **52 周高点**(约 252 个交易日 ≈ 12 个月)这一类"长窗口 `ts_max`"结构:George & Hwang (2004)
  发现"价格相对 52 周最高价的位置"主导、并改善了普通动量的预测力,长期也不反转。这是文献里唯一一个
  "`ts_max` 在约一年窗口上有稳健效应"的清楚例子,但它取的是**价格**的 `ts_max`(对照算子接近
  `div(Close, ts_max(Close, 252))`),不是日内波动/收益的极值,而且**符号相反**:越接近历史高点,
  未来收益**越高**(锚定/延续),不是越低。
  - 出处:George, T.J., Hwang, C.-Y. "The 52-Week High and Momentum Investing." *Journal of Finance*, 2004, vol. 59(5), pp. 2145–2176(DOI 10.1111/j.1540-6261.2004.00695.x)。来源:academicnewsletter.sufe.edu.cn/info/361244;alphaarchitect.com/the-secret-to-momentum-is-the-52-week-high。`verified: true`
- 可以作为旁证、但构造方式不同、没能核实具体回看期窗口的:Kelly & Jiang (2014) 的 tail risk 用 Hill 极值估计量
  逐日估计横截面尾部指数,再对近期估计值做"最优平均"得到条件尾部风险暴露(β),高暴露的股票未来收益更高
  (正号,且这是对"系统性尾部风险"的 beta,不是个股自身的 `ts_max`,机制与我们的不同,只能当远亲参考)。
  窗口长度这次没有查到明确数字。
  - 出处:Kelly, B., Jiang, H. "Tail Risk and Asset Prices." *Review of Financial Studies*, 2014(工作论文版 NBER WP 19375)。来源:nber.org/papers/w19375.pdf;academicnewsletter.sufe.edu.cn/info/354177。`verified: true`(论文身份与方法描述确认;具体窗口长度未核实,标记为未知)

结论:**100–150 个交易日(5–7 个月)处在"一个月 MAX"和"一年 52 周高点"两个已知锚点之间,这次没有找到直接针对这个中间尺度的文献**。
这本身是一条有用的信息,应该写回给 PI:不是"文献支持这个窗口",而是"这个窗口在文献版图里是一个没被专门测过的空档"。

### (c) 符号与控制后是否存活

Bali et al. (2011) 报告 MAX 效应控制市值、账面市值比、动量、短期反转、流动性、偏度后依然显著为负,方向与我们一致
(极端大→未来收益低)。Chichernea & Kassa (2019) 进一步发现 IVOL 异象在"更可能被散户用彩票偏好持有"的股票里更强、
在市场下跌期更强 —— 支持"彩票偏好"这个机制解释,但这是机制证据,不是构造方式,这里只作为背景记一笔。
- 出处:Chichernea, D.C., Kassa, H. "Lottery Preferences and the Idiosyncratic Volatility Puzzle." *European Financial Management*, 2019, vol. 25(3), pp. 655–683。来源:ideas.repec.org/a/bla/eufman/v25y2019i3p655-683.html。`verified: true`

---

## 题 2 —— 对准 N1 与核心 A 的"量加权"那一层:`day_wstd(Ret, Volume)` vs `day_std(Ret)`

### (a) 两者之差被解释成什么

**处理方式 1——用成交量/成交笔数做"时钟"重新采样/加权,而不是按日历时间等权,目的是让收益更接近信息到达节奏。**
Ané & Geman (2000) 的核心结论是:把时间按累计成交量或累计成交笔数重新标定后,收益分布更接近正态;他们发现
**成交笔数做时钟比成交量做时钟效果更好**。翻译过来:我们现在 `day_wstd(Ret, Volume)` 是按成交量(或 `Amt`,
文献证实两者在分钟级几乎共线,等价于按 `|w|` 加权)给分钟收益加权,这是文献里"量时钟"的一个简化版;
文献同时提示,如果以后想换一个更干净的时钟,**成交笔数**理论上比成交量更优 —— 但这条暂时没有可用的叶子字段去落地,
只能记下来,不是这一轮能做的判别式。
- 出处:Ané, T., Geman, H. "Order Flow, Transaction Clock, and Normality of Asset Returns." *Journal of Finance*, 2000, vol. 55(5), pp. 2259–2284。来源:academicnewsletter.sufe.edu.cn/info/361572;lancaster.ac.uk/staff/izzeldin/AG.pdf。`verified: true`
- 背景(二手转述,未独立核实原文):Clark, J.M. (1973) 把价格过程写成"次代(subordinated)随机过程",
  用累计成交量作为该过程的随机时间变换 —— 这是"量时钟"思想最早的来源,但我这次只在 Ané–Geman 相关搜索结果的
  转述里看到这个说法,没有直接打开 1973 年原文确认。`verified: false`

**处理方式 2——量加权之所以有道理,是因为"量大的分钟更有信息"是一个被模型支持的均衡结果,不是经验上的偶然规律。**
Admati & Pfleiderer (1988) 的理论模型里,知情交易者和流动性交易者都倾向于在同一批"厚"的时段集中交易,这个
均衡本身就让**成交量大的时段价格更有信息含量**。翻译:`day_wstd(Ret, Volume)` 给成交量大的分钟更大权重,
等价于"优先看信息含量高的那部分日内波动",这是它和纯等权 `day_std(Ret)` 本质不同的理论依据,不只是工程上的选择。
- 出处:Admati, A.R., Pfleiderer, P. "A Theory of Intraday Patterns: Volume and Price Variability." *Review of Financial Studies*, 1988。来源:academicnewsletter.sufe.edu.cn/info/355980;en.wikipedia.org/wiki/Anat_Admati(引用量说明)。`verified: true`

### (b) 有没有人把"量加权波动 − 等权波动"直接当横截面因子用过,符号是什么

**没有直接搜到**把"量加权已实现波动 减/比 等权已实现波动"直接当作横截面因子使用、并报告符号的论文(即 N1 的具体
写法 `sub(cs_rank(day_wstd(Ret, Volume)), cs_rank(day_std(Ret)))` 本身没有现成文献对照)。
最接近的是把"量加权已实现波动"本身当作一个**独立的新波动率估计量**提出来的工作:

**处理方式 3——量加权已实现波动(VWV)被明确当作一个和传统已实现波动不同的统计量提出,且被证明统计性质不同。**
Padungsaksawasdi & Daigler (2018) 直接构造了"volume weighted volatility (VWV)",用意是捕捉"需求驱动的波动"
而不只是价格本身的变异;他们在股指期货上发现 VWV 和其他波动率度量(含等权已实现波动、极差类波动率)
**只是弱相关**(尤其在波动率最低的那几档),**持续性(自相关)比其他度量更低**,分布也更接近正态。
翻译:这篇论文给了"`day_wstd(Ret, Volume)` 和 `day_std(Ret)` 不是同一个东西、而是两个有独立信息的统计量"
这件事一个直接的经验支撑 —— 支持 N1 的出发点(控制集里只有等权波动,量加权波动是结构性缺失),但没有
现成的符号可以抄,符号需要我们自己评估。
- 出处:Padungsaksawasdi, C., Daigler, R.T. "Volume Weighted Volatility: Empirical Evidence for a New Realised Volatility Measure." *International Journal of Banking, Accounting and Finance*, 2018, vol. 9(1), pp. 61–87。来源:inderscience.com/offer.php?id=89423;ideas.repec.org/a/ids/injbaf/v9y2018i1p61-87.html。`verified: true`(通过 WebFetch 直接读取了摘要页)

### (c) 这个差别主要由哪些微观结构现象驱动

**处理方式 4——量加权波动可能主要是在给"成交活跃度驱动的连续方差"加权,不是在给"跳跃/尾部"加权。**
这是一条需要写给 PI 的重要警告:Giot, Laurent & Petitjean (2010) 把已实现波动拆成连续成分(用 Barndorff-Nielsen
& Shephard 的 bi-power variation 估计)和跳跃成分,发现**交易活跃度(尤其是成交笔数)只和连续成分正相关,
和跳跃成分没有关系**。如果这个结论能搬到我们的场景,那么 `day_wstd(Ret, Volume)` 的"量加权"这一层,
可能主要是在强调"交易活跃、方差持续偏高"的日子,而不是在强调"单日跳价"的日子 —— 这和 analysis.md
§1.4 把这一族定性为"极端事件尾部统计量"的说法是有张力的,**支持 analysis.md 自己提出的 R#4 判别式
(`ts_max` 换成 `ts_mean`)是对的问题**:如果真相是"活跃度驱动的连续方差",`ts_mean` 应该和 `ts_max`
表现接近;如果真相是"尾部/跳跃事件",`ts_mean` 应该明显更差。
- 出处:Giot, P., Laurent, S., Petitjean, M. "Trading Activity, Realized Volatility and Jumps." *Journal of Empirical Finance*, 2010, vol. 17(1), pp. 168–175。来源:cris.maastrichtuniversity.nl/en/publications/trading-activity-realized-volatility-and-jumps。`verified: true`

**处理方式 5——即使按成交量/成交笔数重新采样,也不能把"波动聚集"本身去掉,所以量加权之后残留的长记忆不全是"信息"。**
Lillo, Gillemot & Farmer 发现,即使固定成交量或成交笔数来重新取样价格变动,**波动聚集现象依然很强**,
单纯按交易频率归一化不足以消除这个现象。翻译成提醒:`ts_max(day_wstd(Ret,Volume), W)` 里有多少是
"量加权带来的新信息",有多少只是"任何波动类序列本身就有的长记忆/聚集性被滚动窗口放大",这篇论文说明
不能想当然地把全部功劳记给"量加权"这一层。
- 出处:Lillo, F., Gillemot, L., Farmer, J.D. "There's More to Volatility Than Volume." arXiv:physics/0510007。来源:arxiv.org/pdf/physics/0510007;ar5iv.labs.arxiv.org/html/physics/0510007。`verified: true`

---

## 题 3 —— 对准核心 B / head2:`ts_max(day_wmean(Ret, Volume), 99)`

### (a) 它被当作什么代理

**先说清楚一个落差**:这次没有搜到直接研究"资金加权日内收益(或 VWAP 与收盘价之差)的**长窗口(数月)极值**"
这个具体结构的论文。能找到的文献全部是**短horizon**(日内、隔日、一周)的研究,没有人在这个量上套
`ts_max(..., 99)`。下面是能搬过来的最近邻证据。

**处理方式 1——按成交量算出的"净买压/订单不平衡",当日同向、隔日反转,机制是做市商库存调整。**
Chordia & Subrahmanyam (2004) 构造的每日订单不平衡(买量-卖量)/总量,和 `day_wmean(Ret, Volume)`
(资金加权的日内收益均值)在方向上是同一类东西的代理:谁在用钱投票。他们发现**当日的订单不平衡与当日收益正相关,
但滞后一期的不平衡与下一期收益负相关**(机制:做市商库存效应)。
翻译:这给了 head2 的符号一个"便宜"的解释候选 —— `ts_max(day_wmean(Ret, Volume), 99)` 方向是 -1
(资金加权涨幅最大的那一天涨得越猛,未来收益越低),这和文献里"净买压滞后后反转"的符号**是同一个方向**,
只是我们把它拉长到了 5 个月的"最猛的一天"而不是"昨天"。这意味着 head2 有一部分可能只是这个经典反转效应的
慢速/极值版本,不一定是一个新机制 —— 这一点应该写给 PI,作为对 head2"是否真的新"的一个提醒,
而不是单纯的利好证据。
- 出处:Chordia, T., Subrahmanyam, A. "Order Imbalance and Individual Stock Returns: Theory and Evidence." *Journal of Financial Economics*, 2004, vol. 72(3), pp. 485–518。来源:academicnewsletter.sufe.edu.cn/info/357679;cis.upenn.edu/~mkearns/finread/Chordia_buy-sell_orders.pdf。`verified: true`

### (b) 已知的横截面符号与持续期

**处理方式 2——用高频数据构造的"形状"统计量(偏度)比"水平"统计量(波动率本身)更有横截面预测力,而且符号为负。**
Amaya, Christoffersen, Jacobs & Vasquez (2015) 直接用 5 分钟高频数据构造**周频**已实现偏度、已实现波动率、
已实现峭度,发现:已实现偏度对下一周收益有显著的负向预测力(做多低偏度、做空高偏度,约 19bp/周,
Fama-French+Carhart 不能解释),**而已实现波动率本身对下一周收益没有显著关系**。
翻译成我们的问题:这是一篇独立的、方法论上很接近的文献证据,支持"裸的日内波动/收益水平(`day_wstd`/`day_wmean`
本身)没有阿尔法,形状/极值类统计量才有"这个大方向的判断 —— 和 analysis.md §1.3 里"三族原料单独上场都是
-2.5~-3.5"的发现是同一个结论在另一个市场、另一种构造方式下的重复。可以作为"为什么要在日内统计量上面
再加一层非线性变换(`ts_max`/偏度/极值)才会出现阿尔法"这一大判断的文献支撑,写入 N2(日内形状)那条
会比直接对准 head2 更贴切。
- 出处:Amaya, D., Christoffersen, P., Jacobs, K., Vasquez, A. "Does Realized Skewness Predict the Cross-Section of Equity Returns?" *Journal of Financial Economics*, 2015, vol. 118(1), pp. 135–167。来源:academicnewsletter.sufe.edu.cn/info/356501;rdocumentation.org/packages/highfrequency/versions/1.0.2/topics/rSkew(引用确认)。`verified: true`

### (c) 有没有人取它的长窗口极值用过

**没搜到**。无论是 VWAP−收盘价、订单不平衡,还是资金加权日内收益,这次查到的文献全部是取"当期值"或
"短窗口均值/累积",没有一篇对它取数月尺度的 `ts_max`/`ts_min`。这意味着 head2 如果成立,"把这一类量
拉到 5 个月极值"这一步本身,在我查到的范围内**没有现成文献先例**,是这一族相对 head1(至少有 MAX 效应
一类的先例)更原创、但也更没有校验依据的地方——这一点应该明确告诉 PI。

---

## 题 4 —— 对准涨跌幅限制 / 板块 / 上市年龄

### 涨跌幅限制对日内已实现波动及其极值的机械性影响

**处理方式 1——价格撞到涨跌停附近之后,下一交易日更可能延续(不是反转),且下轨比上轨更明显。**
Wan, Xie, Gu, Jiang, Chen, Xiong, Zhang & Zhou (2015) 用 2000–2011 年全部 A 股高频数据研究涨跌停撞板前后的动态,
发现的是"冷却效应"而不是"磁吸效应":**撞板当天之后,下一交易日价格延续的概率明显高于反转,跌停尤其明显**。
翻译:这对我们判断"ListAge/LimitWidth 代理是不是纯粹的机械噪声"有用 —— 撞板本身带有真实的短期自相关/延续性,
不是一次性的、可以当独立同分布噪声处理的事件;所以 `ts_max(day_wstd(Ret,Volume), 148)` 里哪怕真的主要在
捕捉"撞过板",这个"撞过板"信号本身在文献里也不是纯噪声,而是有短期延续结构的东西 —— 这是对
"低换手代理"假说(analysis.md §1.4 代理 1)的一个旁证:撞板之后的延续性,恰好也是一种"慢变量",
可能进一步混在"低换手"和"尾部"两个解释之间,需要在判别式里留意。
- 出处:Wan, Y.-L., Xie, W.-J., Gu, G.-F., Jiang, Z.-Q., Chen, W., Xiong, X., Zhang, W., Zhou, W.-X. "Statistical Properties and Pre-hit Dynamics of Price Limit Hits in the Chinese Stock Markets." *PLOS ONE*, 2015(同一版本 arXiv:1503.03548,2015-03)。来源:ncbi.nlm.nih.gov/pmc/articles/PMC4395215;arxiv.org/abs/1503.03548。`verified: true`(通过 WebFetch 直接读取了摘要)

**处理方式 2——冷却效应对涨停、跌停不对称,跌停更强。**
同一批作者的后续论文用 logit 模型直接验证"冷却效应"(而非磁吸效应)在涨停和跌停两侧都存在,但**跌停更强**。
翻译:给 analysis.md §1.4 代理 3(板块/涨跌幅宽度)和 N4(上行/下行不对称)都提供了背景支撑 ——
如果要做涨跌不对称的判别式(`cross_semistd_neg`/`cross_semistd_pos` 之类),文献里已经确认涨跌停本身的
动力学就是不对称的,不对称性不是我们假设出来的。
- 出处:Wan, Y.-L., Wang, G.-J., Jiang, Z.-Q., Xie, W.-J., Zhou, W.-X. "The Cooling-off Effect of Price Limits in the Chinese Stock Markets." arXiv:1803.09422,2018-03。来源:arxiv.org/abs/1803.09422。`verified: true`(通过 WebFetch 直接读取了摘要)

**处理方式 3(机构测算,非学术论文,背景参考,核实过但要单独标注信源类型)——20% 涨跌幅相对 10% 能大幅减少"撞板日"的比例。**
上交所相关人士的测算(经财经媒体转载)是:把涨跌幅从 10% 放宽到 20%,可以减少约八成的"撞板"(涨跌停)现象。
翻译:这会让 §1.4 代理 3 的机制假设复杂化 —— 原来的假设是"20% 限幅板块日内波动机械地更大 → 极端值的
`ts_max` 系统性更高";但如果 20% 限幅同时大幅减少了"卡在涨跌停、全天几乎零波动(一字板)"的天数,
那么 20% 限幅股票的"有效波动信息"可能反而**更完整**(较少被一字板截断),净效应方向不是单向明确的,
`cs_bucket_demean(core, LimitWidth)` 这个判别式的结果因此更难只用一个方向去预判,需要真跑出来看。
- 出处:上海证券交易所相关人士测算,经《中国证券报》系媒体转载(非学术论文,时政/行业报道)。来源:cs.com.cn/gppd/gsyj/202008/t20200824_6088089.html。`verified: true`(确认看到了这条测算数字及其转载来源;未找到对应的同行评审论文)
- 另外搜到一篇摘要,把创业板 20% 放宽当准自然实验、报告"撞板比例下降、冲击后价格更平稳、流动性冲击成本下降约 0.73 个百分点/亿元成交量、定价效率提升但风险未上升",但**题目/作者/期刊这次没能确认**(只看到摘要页)。来源:search.napstic.cn/literature/periodical/010jryj202403007。`verified: false`(内容看到了,但引用三要素不全,不建议直接采用这条结论)

### 一字板 / 停牌造成的"全天分钟收益恒为 0"在已实现波动类因子里怎么处理

**没搜到**专门针对 A 股涨跌停/一字板这个具体场景、给出"标准处理方法"的论文(分板块排名 / 分组去均值 / 直接剔除,
三选一这种方法论对照,这次没有查到)。能搬过来的最近邻证据是关于"零收益"本身统计性质的一般性研究:

**处理方式 4——高频数据里的"零收益"不是独立同分布的,也不能只用日内确定性模式解释,说明它携带结构化信息。**
Kolokolov, Livieri & Pirino (2020) 提出了对"价格陈旧(零收益比例)"做统计推断的方法,在 10 只纽交所股票上
检验发现:**日内零收益不是独立同分布的**,而且**单纯的日内确定性周期(如开盘收盘效应)不能解释零收益比例的
日内变化**。翻译:这支持 analysis.md §1.4 的判断"这不是坏掉,但缺失本身带了信息"——哪怕是在没有涨跌停制度的
市场,零收益/价格不变这件事本身也被证明是结构化的,不是可以简单当缺失值随便填补的噪声;对应到 A 股的一字板场景,
`day_wstd(Ret, Ret)` 分母为零触发 NaN、`ts_max` 跳过 NaN 继续沿用旧值,这个处理方式(让缺失"冻结"而不是"填 0"
或"插值")在方向上和文献对"零收益非随机"的告诫是一致的 —— 填 0 或线性插值反而更可能人为抹掉这段信息。
- 出处:Kolokolov, A., Livieri, G., Pirino, D. "Statistical Inferences for Price Staleness." *Journal of Econometrics*, 2020, vol. 218(1), pp. 32–81。来源:publikationen.ub.uni-frankfurt.de/frontdoor/index/index/docId/48376;ricerca.sns.it/retrieve/e3aacdfd-f331-4c98-e053-3705fe0acb7e/MS2018440_Kolokolovetal.pdf。`verified: true`

### 上市年龄(ListAge)

这次没有找到直接研究"上市年龄与已实现波动极值"关系的文献(搜到的都是 IPO 定价/长期收益率方向的研究,
不是波动率构造方向)。能确认、但方向不是波动率而是收益率的背景事实:2014–2019 年 A 股新股首日曾设 44% 的
涨跌幅上限,之后(注册制改革)取消首日上限、创业板统一放宽到 20%;多篇二手资料提到这类限价规则本身
"显著放大了 IPO 抑价和短期价格冲高"。这只说明新股定价机制本身有特殊的价格行为,**没有**直接证据说明
这会通过 `rolling_windows`/`nanmax_last` 的补 NaN 机制系统性压低新股的运行最大值(analysis.md §1.4 代理 2
提出的那个代码层面的机制,这次没能在文献里找到直接对照,仍然只能靠 R#11 的 `cs_bucket_demean(…, ListAge)`
自己跑出来判断)。
- 出处(背景,方向是收益率不是波动率极值,标注清楚以免误用):综合自多条关于 2014–2019 年中国新股定价规则的
  二手报道/研究摘要,具体论文题目与作者这次没有逐一核实到可引用的程度。`verified: false`

---

## 小结:三条最该写给 PI 的话

1. **题 1 的核心判断(文献支持 analysis.md 的方向)**:极值统计量和水平统计量在美股、中国 A 股两处文献里都被证明
   是两个独立的信息源,不是谁吃掉谁——但**没有文献报告过 100–150 个交易日这个具体窗口量级**,这个尺度是
   "一个月 MAX"和"一年 52 周高点"之间的空档,是我们自己要补的实验,不是在抄文献的现成结论。
2. **题 2 的核心判断(给 R#4 加一层文献理由)**:量加权波动在文献里被证明是和等权波动统计性质不同的东西
   (VWV 论文),但也有文献警告"交易活跃度主要关联连续方差、不关联跳跃"——这让 analysis.md 自己提出的
   R#4(`ts_max` 换 `ts_mean`)不只是一个工程判别式,它直接对应文献里"连续方差 vs 跳跃"这组争议,建议
   在写 lit 对照时把这条判别式的重要性再往上调一档。
3. **题 3 的核心判断(风险提示,不是利好)**:head2 的符号(资金加权涨幅最大的一天→未来收益低)和经典的
   日度订单不平衡"滞后反转"效应同方向,而"把这个反转效应拉到 5 个月极值"这件事在文献里**没有先例**——
   PI 排 E/N 的时候应该意识到,head2 有相当一部分解释力可能只是一个被拉长了的经典反转效应,核心 B
   "最安全"的说法(来自结构解剖员,基于与控制的低相关性)和"最原创"不是一回事,这次的文献检索没有找到
   独立支持"长窗口资金加权极值是新机制"的证据。
