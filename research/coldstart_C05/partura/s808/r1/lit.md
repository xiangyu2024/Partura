# 文献:种子 808,B 组,第 1 轮

对应 analysis.md §5 的 Q1–Q4。只用 2023-08-08 前发表的论文 / 工作论文 / 研究报告(arXiv、SSRN 以首版日期为准);拿不准发表日期的不用。
每条处理方式后面用 `[R#]` 标出处,对应文末「出处列表」。`verified: true` 表示本次确实在 WebSearch 结果或 WebFetch 页面上看到了标题/作者/刊物/链接这几项;没有查到的,写明"搜不到",不编。

---

## Q1(核心 1:`inv(LogFloatShares)`,对准名义股价轴)

**文献里"名义股价"这个结构是怎么被构造和处理的:**

1. **直接取价格水平,不取对数,按价格分组(高低价组合)。** 最老的处理方式就是这样:Bhardwaj & Brooks(1992)把 1977–86 年美股按名义股价分组,
   发现低价股的一月效应收益显著更高,但**和规模效应绑在一起、和买卖价差偏差(bid-ask bias)绑在一起**,扣除交易成本后低价股的优势明显变小 `[R4]`。
   翻译成我们的算子语言:**单独用 `log(Close)` 或价格轴分组是不够的,必须同时控制流动性(买卖价差 / 冲击成本的代理)**,
   不然"低价股效应"里有一部分根本是交易成本效应——这正好提醒我们核心 1 的"真来源"判定(§1.4)要把 liq 控制的残差单独看一遍,
   不能只看市值中性化后的残差。

2. **用"拟合价格"(fitted price)代替原始价格,把价格里的贴现率成分剥掉。** Birru & Wang(2016)"Nominal Price Illusion"的处理方式是:
   价格和预期收益本来就是机制性反向关联的(高风险 → 高折现率 → 低价格),原始价格排序会把"名义价格幻觉"和"折现率效应"混在一起,
   所以作者先用会计变量拟合出一个"理论价格",再看**实际价格偏离拟合价格的部分**;他们发现这个偏离项才是幻觉的来源,在难以做空(hard-to-arbitrage)
   的股票和高情绪期后更强;并且用拆股(stock split)做了一个干净的检验——拆股后名义价格降低,投资者对未来偏度的预期跳升,但实际偏度事后反而下降 `[R3]`。
   翻译:把 `log(Close)` 换成**残差**——先用其它基本面字段(我们环境里能用的是 `LogFloatCap`/`LogTotalCap`/`LogFloatShares` 这几个)把价格里
   "合理"的部分回归掉(`cs_regres`),剩下的残差才是幻觉轴,而不是直接用 `LogFloatCap - LogFloatShares` 这个精确代数差。
   这与我们 §1.4 "正交于 `LogFloatCap`"的思路一致,但文献提示**残差回归比代数相减更干净**,因为代数相减假设价格和规模的关系是常数,
   而实际这个关系本身就是回归要估的东西。

3. **名义价格是公司行为(拆股/缩股)维持的,不是基本面决定的——这意味着它本身是一个相当稳定的"风格"轴,适合做长周期特征,不需要高频更新。**
   Weld, Michaely, Thaler & Benartzi(2009)"The Nominal Share Price Puzzle"发现美股的平均名义价格几十年来稳定在某个固定美元区间附近(靠不断拆股维持),
   这是一个行为金重现象,而不是估值现象 `[R1]`。Baker, Greenwood & Wurgler(2009)"Catering through Nominal Share Prices"进一步发现,
   管理层会**按当时投资者对低价股/高价股的偏好**主动调整名义价格(迎合式拆股/缩股),这个"迎合强度"本身随时间变化,且能预测未来收益方向 `[R2]`。
   翻译成算子:这支持 analysis.md §4.5 第 2 点——**累计复权因子** `log(day_last(Close)) − (LogFloatCap − LogFloatShares)`(代表历史分红送转留下的痕迹)
   是一个独立于当前价格水平的"管理层迎合历史"特征,文献里这类"迎合强度"通常用**时间序列上的变化量**(而不是水平值)来衡量,
   所以处理方式应该是这个复权因子的**变化率**(例如 `cross_mean` 后再做一次时间差分),不是它的绝对水平。

4. **"低价"和"彩票型"(lottery-like)特征——高偏度、高换手、高波动——高度共线,文献用最大日收益(MAX)而不是价格本身来代理"彩票偏好"。**
   Bali, Cakici & Whitelaw(2011)"Maxing Out"用**过去一个月的最大日收益**(`MAX`)衡量彩票偏好,发现 MAX 最低和最高两组的风险调整收益差超过
   1%/月,在控制规模、账面市值比、动量、短期反转、流动性、偏度之后依然显著,**而且加入 MAX 后能反转 Ang et al. 的特质波动率之谜的符号** `[R5]`。
   翻译成算子:如果想检验"低价股 = 彩票效应"而不是"低价股 = 规模的代理",应该构造一个**独立于价格轴**的彩票特征(例如 `ts_max` 作用在日收益上,
   20 日窗口,而不是作用在 `LogFloatShares` 上)然后看它和核心 1 的秩相关——如果相关很高,说明核心 1 抓住的其实是彩票/高波动效应而不是纯价格效应;
   这是一个比"控制市值"更精确的"是不是代理"检验,可以作为 R2 深挖的必要性检验补充。

**没搜到、不编的部分**:A 股专门针对"名义股价效应"按板块(主板/创业板/科创板)或股龄分组做横截面检验的中文文献,搜不到;
一篇清华-康奈尔的课程论文和一篇研报提到 A 股投资者偏好低价股、"股价幻觉"是低价股溢价三种成因之一,但都不是可独立核实的学术论文(没有标题/刊物/可查链接),不计入出处列表。

---

## Q2(核心 2:`ts_decay_linear(LogFloatShares, 50)`,对准股本轴 / 股本流量)

**文献里"自由流通比例"和"股本变动"是怎么被构造和处理的:**

1. **自由流通比例不是直接拿"流通股/总股本"这个比值,而是先对 log 市值做横截面回归,取残差,再排序分组。**
   Wang & Xu(2004)"What Determines Chinese Stock Returns?"研究 1996–2002 年 A 股,构造方法是:**把自由流通比例对 `log(市值)` 做横截面回归,
   取残差("residual free float"),再按残差分高低两组做 long-short**;加入这个因子和规模因子后,25 个按规模/流通分组的组合的时间序列解释力从
   约 81% 提高到约 90% `[R8]`。这与 analysis.md §1.4 的 (b) 假设直接相关,而且给出了具体做法:
   翻译成算子,应该用 **`cs_regres(LogFloatCap, LogFloatShares)` 的残差**,而不是 §1.4 里写的代数差 `LogTotalCap − LogFloatCap`——
   代数差假设的是"价格精确抵消",但文献的残差回归法连规模的非线性关系都能吸收掉一部分,是检验 P2(两种自由流通比例写法哪个更干净)时
   应该同时跑一遍的第二种构造方式。

2. **股本变动(解禁/定增/回购/送转)在文献里几乎都是事件研究法,用事件窗口里的异常收益和异常成交量,不是把"变动量"当一个连续横截面特征长期持有。**
   Liao, Liu & Wang(2011,原 2009 工作论文题为"Price Discovery in Share Lockups")研究中国股改限售股解禁,482 次解禁事件,
   在 [-120, +20] 交易日窗口内发现约 -14% 的异常收益,伴随约 140% 的异常成交量放大;**价格下跌的主要部分发生在解禁日之前约 40 天**,
   说明市场提前消化了这个完全可预期的事件 `[R9]`。这正好印证了 analysis.md §4.3 / P3 的判断:**解禁作为"事件"天然是离散的,
   文献自己处理这类结构时用的也是事件窗口法而不是连续特征**。翻译成算子:如果要把"解禁冲击"写成能通过我们 `distinct_fraction` 闸门的连续特征,
   不能直接用 0/1 事件旗标,也不能指望用简单的股本差分,而要用**"距离解禁还有/过去多少交易日"的连续倒计时变量**乘进一个连续载体
   (比如成交量或换手率),或者用文献里"异常成交量放大"这条线索——换手率在解禁窗口附近的异常值本身就是一个连续信号。
   另外,文献用的事件窗口是 **120 个交易日量级**,远大于本轮核心 2 用的 50 日窗口,这提示如果要抓股本流量的"冲击",50 日窗口可能太短,
   应该同时试更长的窗口(接近一年,243 日量级)。

3. **净股本发行(issuance−repurchase)作为连续横截面特征,构造方式是年度股本变化的百分比,按年更新、持有一年,不是短窗口滚动。**
   Pontiff & Woodgate(2008)"Share Issuance and Cross-sectional Returns"发现 1970 年之后,净股本发行对横截面收益的预测力比规模、
   账面市值比、动量都强;发行多的公司未来收益显著更低,回购多的公司未来收益显著更高 `[R6]`。McLean, Pontiff & Watanabe(2009)把这个检验扩展到
   41 个国家,发现这个异象是国际普遍现象,但**效应主要来自"发行后收益低",而不是"回购后收益高"**,方向不对称 `[R7]`。
   翻译成算子:对应 analysis.md 的 `sub(LogFloatShares, ts_decay_linear(LogFloatShares, 50))`,文献的窗口做法是**年度差分**(约 243 个交易日)
   而不是 50 日衰减窗口,而且文献提示**应该分别看"股本增加"和"股本减少"两段的斜率是否一样**(不对称),这是 P1/P2 之外一个值得加的敏感性检验:
   把这个差分按符号拆成两个特征(只在增发时非零、只在回购/缩股时非零),分别看 score。

4. **"流通股比例对股价有负向影响"在更早、更局限的中文文献里是直接用比例做回归,没有做残差化处理。** 任梦、陈玉新(2008)基于扩展
   Feltham-Ohlson 模型的实证研究发现,流通股比例对股价有显著负向影响(研究对象是股权分置改革阶段的 A 股)`[R10]`。这篇方法上比较朴素
   (直接回归,未残差化、未分组),可以当作"不做残差化会怎样"的一个对照,支持第 1 点"应该用残差而不是直接比例/代数差"的建议。

**没搜到、不编的部分**:把"累计分红送转历史"(等价于复权因子)直接当作横截面特征长期持有、检验其对收益预测力的文献,没搜到;
只搜到拆股长期信号效应的研究(Ikenberry, Rankine & Stice 1996 `[R18]`:两年一拆一的美股,拆股后一年有约 7.93% 的超额收益,
拆股意愿本身预示未来业绩)和总派现收益率(payout yield)的研究(Boudoukh, Michaely, Richardson & Roberts 2007 `[R17]`:总派现收益率
+净派现收益率比单纯股息率更能预测横截面收益),这两篇都只是**旁证**,不直接支持"复权因子水平值本身是一个特征"这个具体构造,
写出来但不当作 Q2 核心问题的直接答案。换手率 × 波动率交互、定向增发规模占流通市值比例这类更细的中国特定构造,搜了两次中文关键词都没有
找到可独立核实的期刊论文(只有研报和非学术网页),不计入。

---

## Q3(方法论:市值中性化后残留的非线性规模暴露)

**文献里怎么识别和处理秩空间线性中性化挡不住的非线性规模效应:**

1. **规模效应从一开始就是非线性的,文献的标准处理方式是分组(portfolio sort / 分层),不是线性回归。** Banz(1981)最早发现的规模效应本身就不是线性的:
   "效应集中在最小的一档公司,中等规模和大公司之间几乎没有差异" `[R11]`。这是我们 §1.4 的 (b) 假设("规模的非线性残差")最直接的奠基证据:
   翻译成算子,如果要检验核心 1/2 是不是"规模非线性残差"的代理,应该先按 `LogFloatCap` 分桶(比如五等分或十等分),
   **只在最小的一两个桶内**重新评估核心的 score——如果 score 主要来自最小桶,那就是非线性规模效应而不是独立机制。
   这是一个比"看 ρ 高不高"更直接的判定方法。

2. **"微盘股主导"是后来文献量化这个非线性的标准做法:按 NYSE 分位数断点把股票分成 microcap / small / big 三组,分别检验异象。**
   Fama & French(2008)"Dissecting Anomalies"用 20 分位和 50 分位断点把股票分成三组,发现**发行类、动量类异象在三组里都存在,
   但资产增长、盈利类异象只在 microcap/small 里显著,在 big 里消失**;动量效应在 microcap 里也明显弱于 small/big `[R13]`。
   翻译成算子:这给了一个明确的"是否只是规模代理"的检验配方——**把本组的 head 分别在 `LogFloatCap` 最低 20% / 20%-50% / 50%+ 三组里重新算
   score(或至少重新算与已知族的相关性)**,如果一个因子只在最小盘那组里显著,应该在归因表里标注"疑似微盘股效应",而不是当作独立发现计数。
   这正好可以写进后续轮次的拆解/敏感性检验里。

3. **另一条路线不是回归残差,也不是简单分组,而是给每只股票匹配一个"特征基准组合",用超额部分当作特征调整后的 alpha。**
   Daniel, Grinblatt, Titman & Wermers(1997)提出的"特征调整收益"(characteristic-adjusted returns)方法,是按规模、账面市值比、
   过去一年收益把股票匹配到 125 个被动组合之一,用实际收益减去匹配组合的收益作为"调整后"的部分 `[R12]`。
   这与我们当前用的 `cs_regres`(秩空间线性回归残差)是两条不同的路线:**匹配法对非线性暴露更稳健**(因为它不假设特征和收益是线性关系),
   代价是需要足够多的股票填满每个匹配格。翻译成算子:可以把这个思路简化成"先按 `LogFloatCap` 分桶,再在桶内做 `cs_rank`"
   (也就是条件秩,而不是全市场一次性秩),这是比当前 `neutral_residual` 的全市场线性投影更接近 DGTW 匹配法的做法,
   值得作为 N 新想法的一个候选:**把中性化本身从"全市场线性回归残差"换成"分桶内条件秩"**。

**没搜到、不编的部分**:专门在 Fama-MacBeth 横截面回归里加入"规模的平方项"来直接检验非线性规模暴露的论文,搜了关键词没有找到可独立核实的具体文献
(只找到一篇 Newcastle 的工作论文讨论规模变量在横截面回归里容易给出伪显著结果,这是一个方法论警示,但不是"加平方项"这个具体做法的来源,不单独列出处);
"双变量排序 vs 正交化给出不同结论"的具体对照案例也没搜到可独立核实的文献,只搜到间接讨论(Chan 等对 attribute-matched 基准的批评,
但论文标题没能核实,未列入出处)。

---

## Q4(N 灵感 3:涨跌停幅度 / 板块作为缩放 / 分组变量)

**文献里涨跌停这类交易约束是怎么被当作横截面变量使用的:**

1. **是磁吸效应还是冷却效应,文献没有共识,但双方的构造方法都是:统计触及涨跌停后次日的"延续 vs 反转"概率,按涨停/跌停分别统计。**
   Wan, Xie, Gu, Jiang, Chen, Xiong, Zhang & Zhou(2015)研究全部 A 股 2000–2011 年涨跌停数据,发现**冷却效应**(与磁吸效应相反的证据):
   触及涨跌停后次日**价格延续比反转更常见**,尤其是跌停,而且这篇论文明确说"磁吸效应还是冷却效应,文献没有共识" `[R14]`。
   翻译成算子:处理方式是**不要把涨跌停当 0/1 事件旗标**,而要按涨停/跌停分别构造"触及后续"的连续信号(比如触及当天到次日的收益,
   分涨停组和跌停组分别看符号),这与 analysis.md §4.3 的闸门问题(事件类特征过不了 `distinct_fraction`)是一致的提示——
   必须把"涨跌停"转成一个连续的、按涨停/跌停方向区分的载体,而不是单一的事件指示变量。

2. **大户资金在涨停日的净买入行为预测更强的长期反转,且 ST 股票(更窄的涨跌幅限制)反转更明显——这提示涨跌停限制的宽度本身是一个调节变量。**
   Chen, Gao, He, Jiang & Xiong(NBER WP24014,2017;正式发表于 Journal of Econometrics, 2019)用深交所账户级数据发现,
   大投资者在股票触及 10% 涨停当天净买入,随后次日卖出,这个净买入行为能预测更强的长期价格反转;**ST 股票(5% 涨跌幅限制)的反转效应比普通股票更明显** `[R15]`。
   翻译成算子:这直接支持用 `LimitWidth`(涨跌停宽度,主板 10%/科创创业板 20%/ST 5%-20%)做**调节变量**而不是独立因子——
   把一个反转类因子按 `LimitWidth` 分组或者和 `LimitWidth` 做交互(窄限制组的反转系数应该更大),而不是像本轮共性那样把它单独当一元信号用。

3. **连续触及涨跌停的天数长度,本身影响"开板后"的预期收益形状,文献按连续天数分组而不是看单日。**
   Wu, Wang & Li(2017,Physica A)发现开板后的预期收益呈"W"形,**连续触及涨跌停的天数长度是一个独立的影响因素**,
   价格动态还依赖大盘当时的走势 `[R16]`。翻译成算子:可以构造"过去 N 日里触及涨跌停的滚动计数"(类似 `ts_sum` 作用在涨跌停触及指示上)
   当分组/缩放变量,而不是单日的 0/1 指示——这是把"连续事件长度"变成连续特征的一个具体做法,可以直接套用。

**没搜到、不编的部分**:直接把"日收益 / 波动率除以 `LimitWidth`"(即用涨跌停幅度做分母归一化日频收益或波动率)这种具体处理方式的文献,搜不到;
PLAN §1 第 3 条提到的「日收益按涨跌停幅度缩放」是 Partura 自己在 C01–C04 里的构造,不是来自外部文献,此处如实说明没有外部文献直接支持这个具体除法,
只有上面三条"涨跌停宽度做调节/分组变量"的间接支持。A 股涨跌停制度下专门针对"动量/反转因子做涨跌停归一化处理"的文献,搜了中英文关键词都没有找到。

---

## 出处列表

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|---|
| R1 | The Nominal Share Price Puzzle | Weld, W.C.; Michaely, R.; Thaler, R.H.; Benartzi, S. | 2009-05(JEP 23(2)) | Journal of Economic Perspectives | https://ideas.repec.org/a/aea/jecper/v23y2009i2p121-42.html | true |
| R2 | Catering through Nominal Share Prices | Baker, M.; Greenwood, R.; Wurgler, J. | 2008-01(NBER WP13762,正式发表 2009-12,JF 64(6)) | NBER Working Paper / Journal of Finance | https://www.nber.org/papers/w13762 | true |
| R3 | Nominal Price Illusion | Birru, J.; Wang, B. | 2012-12 工作论文稿 / 正式发表 2016(JFE 119(3)) | EFMA 2013 会议稿 / Journal of Financial Economics | https://www.efmaefm.org/0efmameetings/EFMA%20ANNUAL%20MEETINGS/2013-Reading/papers/EFMA2013_0526_fullpaper.pdf | true |
| R4 | The January Anomaly: Effects of Low Share Price, Transaction Costs, and Bid-Ask Bias | Bhardwaj, R.; Brooks, L. | 1992(JF 47(2)) | Journal of Finance | https://ideas.repec.org/a/bla/jfinan/v47y1992i2p553-75.html | true |
| R5 | Maxing Out: Stocks as Lotteries and the Cross-Section of Expected Returns | Bali, T.G.; Cakici, N.; Whitelaw, R.F. | 2009-03(NBER WP14804,正式发表 2011,JFE 99(2)) | NBER Working Paper / Journal of Financial Economics | https://ideas.repec.org/a/eee/jfinec/v99y2011i2p427-446.html | true |
| R6 | Share Issuance and Cross-sectional Returns | Pontiff, J.; Woodgate, A. | 2008-04(JF 63(2)) | Journal of Finance | https://ideas.repec.org/a/bla/jfinan/v63y2008i2p921-945.html | true |
| R7 | Share Issuance and Cross-Sectional Returns: International Evidence | McLean, R.D.; Pontiff, J.; Watanabe, A. | 2009-10(JFE 94(1)) | Journal of Financial Economics | https://ideas.repec.org/a/eee/jfinec/v94y2009i1p1-17.html | true |
| R8 | What Determines Chinese Stock Returns? | Wang, F.; Xu, Y. | 2004-11(FAJ 60(6)) | Financial Analysts Journal | https://rpc.cfainstitute.org/en/research/financial-analysts-journal/2004/what-determines-chinese-stock-returns | true |
| R9 | Information Discovery in Share Lockups: Evidence from the Split-Share Structure Reform in China(工作论文题为 Price Discovery in Share Lockups) | Liao, L.; Liu, B.; Wang, H. | 2009-10 工作论文 / 正式发表 2011-12(Financial Management 40(4)) | EFMA 工作论文 / Financial Management | https://efmaefm.org/0EFMSYMPOSIUM/2010-China/papers/LLW_splitshare20091030.pdf | true |
| R10 | 流通股比例对股票价格影响的实证研究 | 任梦;陈玉新 | 2008(辽宁石油化工大学学报 28(1),92-95) | 辽宁石油化工大学学报 | https://journal.lnpu.edu.cn/CN/Y2008/V28/I1/92 | true |
| R11 | The Relationship Between Return and Market Value of Common Stocks | Banz, R.W. | 1981(JFE 9(1)) | Journal of Financial Economics | https://floridapsc.com/library/filings/2023/00092-2023/Support/Staff%20Exhibit%20167/Witness%20Testimony%20Workpapers/Witness%20Nelson/42,43_Banz,%20The%20Relationship%20Between%20Return%20and%20Market%20Value%20of%20Common%20Stocks,%20JFE%209%20(1981).pdf | true |
| R12 | Measuring Mutual Fund Performance with Characteristic-Based Benchmarks | Daniel, K.; Grinblatt, M.; Titman, S.; Wermers, R. | 1997-07(JF 52(3)) | Journal of Finance | https://ideas.repec.org/a/bla/jfinan/v52y1997i3p1035-58.html | true |
| R13 | Dissecting Anomalies | Fama, E.F.; French, K.R. | 2008-08(JF 63(4)) | Journal of Finance | https://ideas.repec.org/a/bla/jfinan/v63y2008i4p1653-1678.html | true |
| R14 | Statistical Properties and Pre-Hit Dynamics of Price Limit Hits in the Chinese Stock Markets | Wan, Y-L.; Xie, W-J.; Gu, G-F.; Jiang, Z-Q.; Chen, W.; Xiong, X.; Zhang, W.; Zhou, W-X. | 2015-03(arXiv:1503.03548,正式发表 2015-04,PLOS ONE 10(4)) | arXiv / PLOS ONE | https://arxiv.org/pdf/1503.03548 | true |
| R15 | Daily Price Limits and Destructive Market Behavior | Chen, T.; Gao, Z.; He, J.; Jiang, W.; Xiong, W. | 2017-11(NBER WP24014,正式发表 2019,Journal of Econometrics 208(1)) | NBER Working Paper / Journal of Econometrics | https://www.nber.org/papers/w24014 | true |
| R16 | Post-hit dynamics of price limit hits in the Chinese stock markets | Wu, T.; Wang, Y.; Li, M-X. | 2017(Physica A 465) | Physica A: Statistical Mechanics and its Applications | https://ideas.repec.org/a/eee/phsmap/v465y2017icp464-471.html | true |
| R17 | On the Importance of Measuring Payout Yield: Implications for Empirical Asset Pricing | Boudoukh, J.; Michaely, R.; Richardson, M.; Roberts, M.R. | 2004-07(NBER WP10651,正式发表 2007-04,JF 62(2)) | NBER Working Paper / Journal of Finance | https://www.nber.org/papers/w10651 | true |
| R18 | What Do Stock Splits Really Signal? | Ikenberry, D.L.; Rankine, G.; Stice, E.K. | 1996-09(JFQA 31(3)) | Journal of Financial and Quantitative Analysis | https://ideas.repec.org/a/cup/jfinqa/v31y1996i03p357-375_00.html | true |

**搜了但没有可独立核实的文献,不编、如实列在这里(不算出处):**

- A 股专门检验"名义股价效应"按板块 / 股龄分组的中文期刊论文(Q1)。
- 把"累计分红送转历史(复权因子水平值)"直接当横截面特征检验预测力的论文(Q2)。
- 换手率 × 波动率交互项 + 自由流通股 + 定向增发/解禁规模占流通市值比例,同时出现在一篇可核实论文里的构造(Q2)。
- Fama-MacBeth 回归里显式加入"规模平方项"检验非线性规模暴露的具体论文,以及"双变量排序 vs 正交化给出不同结论"的具体对照案例(Q3)。
- 直接用涨跌停幅度 `LimitWidth` 做日收益 / 波动率的归一化分母的文献,以及专门研究 A 股涨跌停制度下动量/反转因子归一化处理的文献(Q4)。
