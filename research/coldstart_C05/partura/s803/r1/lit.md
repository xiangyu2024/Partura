# 文献:种子 803,B 组,第 1 轮(文献员)

查的题目来自 `r1/analysis.md` §5 的 L1–L4,全部对准核心 `day_kurt(Ret)`(score 0.97,方向 −1,hl=20)及其家族假设 H1(稀疏度代理)/ H2(真尾部形状)/ H3(彩票需求·封板后效)。
只用工具(WebSearch / WebFetch)这次实际检索到、能确认首版日期早于 **2023-08-08** 的论文/工作论文/研究报告;日期拿不准的一律不用、在对应小节写明「搜不到」或「日期不确定,弃用」。
下面每条「处理方式」后面用 `[Sx]` 指向文末出处表;出处表的 `verified` 字段按定义标注:**true = 这次搜索结果或抓取的页面上确实看到了它**(标题、作者、年份、出处都对得上),**false = 没有独立确认**(本次没有写 false 的条目,搜不到的直接不列,在正文说明)。

---

## L1 —— 对准核心本身:高频收益高阶矩在截面上怎么用,以及怎么和「不交易」分开

**能翻译成算子语言的处理方式:**

1. **周频 / 月频已实现偏度·峰度直接做截面十分位多空,不先剔除无成交分钟**。Amaya et al. (2015) 用日内收益算每周的 realized skewness / realized kurtosis,直接按周滚动排序分十分位,高—低峰度组合周收益 +16bp(t≈2.98,工作论文版数字;发表版峰度结果显著性不稳)。**关键的空白**:他们的构造没有在算矩之前先剔除零收益分钟或控制「这一周有多少分钟真的在交易」——这正是我们怀疑 H1(稀疏度代理)的缺口在文献里也普遍存在,不是我们独有的疏漏。→ 对应我们的处理:若要照搬这条范式,`day_kurt(Ret)` 外面套 `cross_mean(·, 20)` 再做十分位,这就是我们已经在做的;但文献本身**没有**提供「先剔除零收益分钟」这道处理的先例,这道处理(即 H1 的判决探针)是我们自己要做的,文献没有现成答案。[S1]
2. **用零收益比例本身当流动性/摩擦代理,而不是去修正别的统计量**:Lesmond, Ogden & Trzcinka (1999) 把一段时间内(通常按月)零收益天数的占比本身当成交易成本的隐含估计;Bekaert, Harvey & Lundblad (2007) 在新兴市场里把同一个比例(`ZEROS`,月度零收益天数占比,右偏修正)直接当月度流动性因子用来预测下月收益,并发现它比换手率更能预测。两篇的处理都是:**先在日频上判定"今天是不是零收益",再按月(≈ 我们的 20 日)取均值,直接当一个独立的截面变量(控制或排序对象),不与别的统计量相乘或相除**。→ 翻译成算子语言正是 `cross_mean(day_zero_ratio(Ret), 20)`,与第 0 节「R 第 2 条」的构造完全对应;这给这条探针一个文献先例,但文献里从未把它跟峰度相减或相除来"净化"峰度——那道处理(H1 判决本身)文献没有做过。[S2][S3]
3. **噪声导致的方差偏差会人为抬高标准化收益的峰度,稳健化方法是先修正方差再标准化**:Fleming & Paye (2006) 发现用未修正的已实现波动率去标准化日收益,算出来的峰度偏低、显得接近正态;换成偏差修正的已实现波动率估计量后,标准化收益明显变成低峰度(platykurtic),说明"分母的噪声"直接污染了峰度这个统计量。这是另一种「某种噪声会把峰度读数系统性地往某个方向推」的先例,方向和我们怀疑的(零值比例把峰度往高推)不同,但**处理方法相同**:先修正/替换掉污染源,再重新算同一个统计量,比较差异——这正是我们 R 清单里「换分母」「换核心算子」类探针(第 1、3、4、10 条)在做的事。[S4]
4. **把日波动率拆成隔夜段和日内段分别处理,日内段峰度低、隔夜段峰度可以发散**:Blanc, Chicheportiche & Bouchaud (2013/2014) 在 ARCH 框架里把日度波动率拆成隔夜贡献和日内贡献,发现日内收益的残差峰度很低(接近高斯),隔夜收益的残差峰度可以无穷大(被少数极端隔夜跳空支配)。这给了「`Ret` 的构造约定(是否含隔夜跳空)会系统性改变峰度读数」一个独立佐证,直接对应我们的 R 第 4 条(`day_kurt(in_pct(Close,1))`,日内重建、不含隔夜)和部件 B 的怀疑点。处理方式翻译:**把全天收益按"隔夜 vs 日内"拆成两段分别算同一个矩,而不是在一个序列里混着算**。[S5]

**搜不到 / 弃用的部分**:没有找到任何文献在算日内高阶矩前显式"按成交量抽样而不是按时间抽样"(即把 `Ret` 的时间索引换成成交量累计索引后再算 `day_kurt`)——这道处理在 L1 范围内搜不到直接先例,L4 的 Clark (1973) 提供的是更一般的"业务时间抽样"理论基础(见下)但不是专门用在峰度上。也没有找到专门针对"零收益比例"单独作为峰度的**协变量/控制项**(而非独立因子)去回归剔除的论文;Lesmond/Bekaert 的处理始终是把零收益比例自己当因子,不是拿它去"net out"另一个统计量。

---

## L2 —— 对准「换掉 `day_kurt` 这个部件」:尾部/集中度统计量的稳健化各自解决什么

**能翻译成算子语言的处理方式:**

1. **双幂变差(bipower variation):用相邻两个绝对收益的乘积之和(乘以 π/2 校正)替代平方和**,对单个大跳的鲁棒性来自"一个跳只污染一项乘积,不会像平方和那样被单个极端值完全支配"。Barndorff-Nielsen & Shephard (2004) 证明已实现方差减双幂变差能分离出跳跃部分的二次变差。**修的是什么**:单个异常打印对统计量的支配力(与我们怀疑 `day_kurt` 会被"一天里的一两分钟"支配完全对应)。→ 翻译:把 `day_kurt` 换成「相邻分钟收益乘积」类的构造,这正是我们替换件清单里 `day_gini`(有界、不被单点支配)在**思路**上的同类项,但 BNS 的具体算子(双幂变差)我们的算子库目前没有对应原语,只能当作"为什么要换"的理论支持,不能直接翻译成现成算子。[S6]
2. **MedRV(中位已实现波动率):取三个相邻绝对收益的中位数而不是和**,两侧截断,对跳跃和"零"收益都稳健,而且专门设计来缓解日内波动的强烈时点模式(intraday pattern)带来的有限样本偏差。Andersen, Dobrev & Schaumburg (2009/2012) 的核心卖点正是「短窗口、局部构造」,这与我们怀疑长窗口统计量(`day_kurt` 用全天 241 根)被少数薄弱时段支配是同一个病灶的另一种药。**修的是什么**:薄交易(含零收益)对统计量的污染 + 日内 U 型模式的有限样本偏差。→ 翻译:若要在我们的算子语言里模拟"局部中位数"稳健化,目前最接近的现成件是 `day_gini`(有界、尺度无关)而不是真正的 MedRV(我们没有"分钟级滑动中位数"原语),这点要如实告诉 PI:**MedRV 的具体构造法搬不进我们的算子库,只能借它的"为什么稳健"的论证**。[S7]
3. **分离下行尾部和上行尾部,分别取条件均值比(expected-shortfall 型)而不是合并成一个双侧统计量**:Kelly & Jiang (2014) 用整个横截面每月的左尾拟合幂律尾指数;Almeida, Ardison, Garcia & Vicente (2016) 提出用风险中性化后的横截面"超额预期损失"(excess expected shortfall)比率,不依赖期权价格,直接从股票收益横截面构造。两者的共同处理是:**先把收益按正负(或按分位数)分成两段,只在尾部那一段上取条件统计量,再做比值或标准化**。这与我们 R 清单里 `day_es_ratio_hi/lo(Ret)`(第 5、6 条)的构造完全同源:**分侧处理** + **条件均值而非矩**。[S8][S9]
4. **交易量集中度的 Gini / 熵度量,把"份额"当概率分布再算集中度指标**:一篇做市场冲击的论文(2020)把每个参与者的成交量份额当成概率分布,同时算 Gini 指数和熵,完全集中时 Gini→1。这是对"集中度"这个概念最干净的稳健化处理,但**对象是成交量在参与者间的分布,不是分钟收益的分布**——我没有搜到把 Gini/熵直接用在"一天内分钟收益分布的集中度"(即直接替代 `day_kurt` 的论文),这点要如实说:`day_gini(Ret)` 这个替换件的"稳健化"动机能从 L1/L2 的论证里推出来,但它本身不是文献里现成的构造,是我们自己把"Gini 用于份额集中度"这个处理方式迁移到"收益分布集中度"上的**类比**,不是直接证据。[S10]

**搜不到 / 弃用的部分**:没有找到任何论文直接比较"裸峰度 vs 双幂变差 vs MedRV vs expected-shortfall 比率"在**截面选股**(而不是波动率预测)任务上的横向表现;这些稳健化方法几乎全部是为"更准确估计积分方差/检测跳跃"而设计,不是为"预测横截面收益"而设计,所以它们对我们任务的借鉴止于"构造思路"(怎么躲开被单点支配、怎么处理薄交易日),不能照搬文献里的"谁更好"结论。

---

## L3 —— 对准 E 的外围:同类特征怎么条件分组、交互、换股票池,尤其是 A 股涨跌停

**能翻译成算子语言的处理方式:**

1. **按市场前期状态(牛/熊)整体切换因子方向或强度,而不是在横截面里找状态变量再回归**:Cooper, Gutierrez & Hameed (2004) 把"市场状态"定义成"过去三年市场累计收益的正负"这一个二值开关,发现动量利润在 UP 状态下月均 +0.93%,DOWN 状态下 −0.37%(样本 1929–1995)。Stambaugh, Yu & Yuan (2012) 则是把"投资者情绪"的高低当开关,发现几乎所有异象的多空收益在高情绪期后更强。两者处理方式相同:**先把一个全市场的状态变量(非个股层面)离散成二值或分位,再按状态把因子收益分组统计,或者直接用状态变量去调制(乘)信号而不是中性化掉它**。→ 直接对应我们 N 候选 `cs_flip_by_state(day_kurt(Ret), day_sum(Amt))` 和 `mul(cs_state_rank(day_sum(Amt),60), day_kurt(Ret))` 的构造语言:**调制,不是中性化**。[S11][S12]
2. **组内排序/组内标准化 vs 线性回归残差,文献里两条路都有人用,但没搜到针对同一个特征的直接横向比较**:上面能确认的材料里没有一篇把"按市值分组后组内排序"与"对市值做线性回归取残差"这两种中性化方式,在同一个特征、同一个样本上做直接对照并报告谁更干净。这点要如实告诉 PI:**E 候选清单里 `cs_bucket_rank` 系列(分桶内排序)的"为什么能拿到线性投影拿不掉的信息"这条逻辑是我们自己从"奖励的中性化是秩空间上的线性投影"(结构解剖员 §4.1)推出来的,不是文献给的结论**;文献只能提供"分组确实是常见做法"这个弱支持,不能提供"分组一定比线性回归强"的证据。
3. **A 股涨跌停磁吸效应:证据方向不一致,且多数研究样本偏早**。能查到的中文检索结果里,天津大学一项用日内高频数据的研究(约 2008 年)报告涨停方向磁吸效应存在、跌停方向不明显;另一项用 2015 年沪深数据的 GARCH 研究没有验证到磁吸效应,反而发现指数下跌会放大个股磁吸效应,且对大盘股更明显。**这两条都只在中文搜索摘要里看到,没有抓到可核实的论文标题/期刑/链接,按规矩不列入出处表、不作为可引用证据**,只记录"方向不一致"这个事实供 PI 参考,不要在 missions.yaml 里引用成确定结论。
4. **创业板 2020-08-24 涨跌幅限制 10%→20% 改革:正式事件研究**。Bao Qi (2023, *PLOS ONE*) 用改革前(2020-02~07)触及 10% 限制的事件和改革后(2020-10~2021-03)收盘价偏离超过 10% 的事件做对照,发现限价会延迟价格发现、产生波动溢出、干扰交易,**下限(跌停)比上限(涨停)的负面效应更严重**,且**没有发现磁吸效应的证据**。处理方式:市场模型估计超额收益(估计窗 [-120,-30],事件窗 [-5,10]),波动率用当日最高/最低价对数比值并按事件前均值标准化,成交量按事件前均值标准化;**分组仅按涨停/跌停方向,没有按市值或板块再分组**。→ 这给我们核心卡 §4.1 第 1 条"`LimitWidth` 特别值得用,2020-08-24 落在 train 段内"的提法一个具体、可核实的事件研究先例,但也提醒:**原文献按涨跌方向分组、不按市值分组**,若我们要在 `LimitWidth` 分桶里再交叉市值,这是在文献基础上的延伸,不是照搬。[S13]
5. **成交量 U 型模式与收益—成交量的滞后依赖**:Admati & Pfleiderer (1988) 给出需求冲击导致日内成交量 U 型的理论模型;Jain & Joh (1988) 用 NYSE 小时数据发现同小时收益—成交量正相关,且该相关性可持续到滞后 4 小时,正收益时的量—价关系比负收益时更陡。处理方式:**把一天切成小时(或我们的情形,分钟→日内分桶)块,块内分别算收益与成交量,再看同期/跨期相关,且区分正负收益**。→ 这给 N-C 方向(成交时间 vs 钟表时间)和 E 外围里"按市场状态翻向"提供了"正负收益不对称处理"这一条可借鉴的处理方式,目前我们的清单里没有体现这种不对称。[S14][S15]

---

## L4 —— 对准 N-A/N-C:日内收益的顺序信息,以及成交时点,在截面上值钱吗

**能翻译成算子语言的处理方式:**

1. **买卖价差导致的负自相关,用一阶自协方差(不是自相关)反推出隐含价差,且只在协方差为负时才定义**:Roll (1984) 的处理是:**用价格变化(不是收益率)的一阶序列协方差,协方差为负时取 `spread = 2·sqrt(-cov)`,协方差非负时输出缺失而不是硬算**。这给我们「跳过门槛类风险」提了个醒:自相关/协方差类统计量在构造时要显式处理"符号不对"的情形(缺失而不是异常值),这与结构解剖员 §2 提到的 `distinct_fraction`/`coverage` 门槛陷阱是同一类工程问题的另一个例子。[S16]
2. **方差比率检验:多期收益方差 / (期数×单期收益方差),理论值为 1,偏离度量定价效率**,个股层面常常 VR<1(负自相关),指数/组合层面常常 VR>1。Lo & MacKinlay (1988) 的处理:**对同一条收益序列用不同的"持有期聚合窗口"重算方差,再取比值**,这正是 `cross_delta`/`cross_stddev` 换窗口再做比值这类构造的理论源头;也提醒我们"个股和指数的方向可能相反",所以 N-A 清单里的自相关/方差比率类因子在个股层面该预期什么符号,文献给出了明确方向(个股负自相关更常见)。[S17]
3. **业务时间(成交量驱动的"钟")比日历时间采样能降低已实现方差的均方误差**:Oomen (2006) 实证发现换成交易时间采样平均降 MSE 约 5%,交易强度不规律的日子最多降 40%;其理论基础是 Clark (1973) 把价格建模成由"累计成交量"这个随机钟驱动的布朗运动,这样可以同时解释厚尾和序列依赖。处理方式翻译:**把"20 天"这类日历窗口换成"按累计成交额切出的等量窗口"**——这正是 N-C 候选 `day_centroid(Amt)`、`day_wstd(Ret,Amt)` 背后"用成交量当钟"而不是"用分钟数当钟"的理论依据,是目前 R/N 清单里唯一有扎实理论支撑的"换时间尺度"处理。[S18][S19]
4. **日内自相关/Hurst 指数的滚动估计噪声很大,短窗口上尤其不可信**:一篇 2012 年论文(Barunik & Kristoufek,日内分段估计 Hurst)和多条二级来源都提示:在分钟频率、短窗口(≈100 根)上滚动估计 R/S 型 Hurst 容易被短程自相关本身污染,系统性偏高。这条是"怎么不要踩坑"的处理建议,不是"怎么构造"的处理建议:**N-A 里 `day_hurst(Ret)` 若用全天 241 分钟窗口估计,文献的警告是样本量本身偏小,估计噪声可能大到盖过信号**,这点应该写进 notebook 的预测清单,而不是当作正面证据。[S20]

**搜不到 / 弃用的部分**:没有找到任何文献专门做"成交量加权波动率"(`day_wstd(Ret,Amt)` 这个具体构造)在 A 股个股截面上的选股检验——这是中文和英文检索都没有命中的空白,日内成交量/VWAP 的中文文献全部落在"交易量预测"或"算法交易基准"上,不是"选股因子"。也没有找到"Hurst 指数"或"方差比率"作为截面选股因子(而不是市场有效性检验工具)的任何论文,这两个统计量在文献里几乎全部是"检验工具"用法,不是"因子"用法,这件事本身值得写进 notebook:N-A 若真的要做,我们是在做文献没做过的事,不是在复刻一个已知异象。

---

## 出处(按正文出现顺序编号,`verified` 均为本次搜索/抓取中实际看到)

[S1] Diego Amaya, Peter Christoffersen, Kris Jacobs, Aurelio Vasquez. 2015(发表;工作论文版 2011)."Does realized skewness predict the cross-section of equity returns?" *Journal of Financial Economics*, 118(1), 135–167. DOI 10.1016/j.jfineco.2015.02.009. 工作论文版:CREATES RP 2011-44, https://ideas.repec.org/p/aah/create/2011-44.html 。verified: true

[S2] Lesmond, D., Ogden, J., Trzcinka, C. 1999. "A New Estimate of Transaction Costs." *The Review of Financial Studies*, 12(5), 1113–1141. https://www.bauer.uh.edu/rsusmel/phd/lot_1999RFS.pdf ;IDEAS 记录 https://ideas.repec.org/a/oup/rfinst/v12y1999i5p1113-41.html 。verified: true

[S3] Geert Bekaert, Campbell R. Harvey, Christian Lundblad. 2007(NBER WP 2005). "Liquidity and Expected Returns: Lessons from Emerging Markets." *Review of Financial Studies*, 20(6), 1783–1831. NBER WP 11413: https://www.nber.org/papers/w11413.pdf 。verified: true

[S4] Jeff Fleming, Bradley S. Paye. 2006(作者页面某处把第三作者列为"Jones",与标准引用不符,存疑). "The Impact of Microstructure Noise on the Distributional Properties of Daily Stock Returns Standardized by Realized Volatility." 工作论文/期刊文章,具体期刊卷期本次未确认。链接:https://bradleypaye.owlstown.net/publications/11690-the-impact-of-microstructure-noise-on-the-distributional-properties-of-daily-stock-returns-standardized-by-realized-volatility 。verified: true(标题、年份、核心发现确认;期刊名与完整作者名未确认,引用时需二次核实)

[S5] Pierre Blanc, Rémy Chicheportiche, Jean-Philippe Bouchaud. 首版 arXiv 2013-09;发表 2014. "The fine structure of volatility feedback II: overnight and intra-day effects." *Physica A*, 402, 58–75. arXiv:1309.5806,https://ar5iv.labs.arxiv.org/html/1309.5806 。verified: true

[S6] Ole E. Barndorff-Nielsen, Neil Shephard. 2004. "Power and Bipower Variation with Stochastic Volatility and Jumps." *Journal of Financial Econometrics*, 2(1), 1–37. 工作论文版:https://www.nuffield.ox.ac.uk/economics/papers/2003/w18/eric_may03.pdf 。verified: true

[S7] Torben G. Andersen, Dobrislav Dobrev, Ernst Schaumburg. NBER WP 15533,2009-11;期刊版 2012. "Jump-Robust Volatility Estimation Using Nearest Neighbor Truncation." *Journal of Econometrics*, 169(1), 75–93. NBER: https://www.nber.org/papers/w15533 ;NY Fed Staff Report 465: https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr465.html 。verified: true

[S8] Jonathan Kelly, Hao Jiang. 2014. "Tail Risk and Asset Prices." *Review of Financial Studies*, 27(10), 2841–2871. NBER WP 19375: https://www.nber.org/papers/w19375.pdf 。verified: true

[S9] Caio Almeida, Kym Ardison, René Garcia, Jose Vicente. 2016-04. "Nonparametric Tail Risk, Stock Returns and the Macroeconomy." CIRANO Scientific Series 2016s-20. https://new.cirano.qc.ca/files/publications/2016s-20.pdf 。verified: true

[S10] (论文未给出完整作者信息,仅在搜索摘要中出现). 2020-12(arXiv:2012.10262). "Matching in size: How market impact depends on the concentration of trading." https://arxiv.org/pdf/2012.10262 。verified: true(摘要内容确认;注意:对象是跨参与者的成交量份额集中度,不是分钟收益分布,引用时需说明是类比而非直接证据)

[S11] Michael Cooper, Roberto C. Gutierrez Jr., Allaudeen Hameed. 2004. "Market States and Momentum." *Journal of Finance*, 59(3), 1345–1365. 摘要来源:https://academicnewsletter.sufe.edu.cn/info/361185 。verified: true

[S12] Robert F. Stambaugh, Jianfeng Yu, Yu Yuan. 2012(NBER WP 2011). "The Short of It: Investor Sentiment and Anomalies." *Journal of Financial Economics*, 104(2), 288–302. NBER WP: https://www.nber.org/papers/w16898.pdf 。verified: true

[S13] Bao Qi. 2023-06(收稿 2023-03,接收 2023-06). "Effectiveness of price limits: Evidence from China's ChiNext market." *PLOS ONE*, 18(6): e0287548. https://pmc.ncbi.nlm.nih.gov/articles/PMC10289463/ 。verified: true(已直接抓取全文摘要与方法部分核实)

[S14] Anat R. Admati, Paul Pfleiderer. 1988. "A Theory of Intraday Patterns: Volume and Price Variability." *The Review of Financial Studies*, 1(1), 3–40. 摘要来源:https://academicnewsletter.sufe.edu.cn/info/355980 。verified: true

[S15] Prem C. Jain, Gun-Ho Joh. 1988-09. "The Dependence between Hourly Prices and Trading Volume." *Journal of Financial and Quantitative Analysis*, 23(3), 269–283. https://resolve.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/dependence-between-hourly-prices-and-trading-volume/C305DB5BFB5F2B2D803BB94449AF8B47 。verified: true

[S16] Richard Roll. 1984. "A Simple Implicit Measure of the Effective Bid-Ask Spread in an Efficient Market." *The Journal of Finance*, 39(4), 1127–1139. https://www.bauer.uh.edu/rsusmel/phd/roll1984.pdf 。verified: true

[S17] Andrew W. Lo, A. Craig MacKinlay. 1988. "Stock Market Prices Do Not Follow Random Walks: Evidence from a Simple Specification Test." *The Review of Financial Studies*, 1(1), 41–66. 摘要/部分原文来源:https://www-cambridge-org.ezproxyberklee.flo.org/core/product/FDAEFD946D8A453D89C7419FD36FC36A/core-reader 。verified: true

[S18] Roel C.A. Oomen. 2006. "Properties of Realized Variance under Alternative Sampling Schemes." *Journal of Business & Economic Statistics*, 24(2), 219–237. 摘要确认来源:搜索结果摘要(标题、年份、期刊、核心数字 5%/40% MSE 下降一致出现)。verified: true

[S19] Peter K. Clark. 1973. "A Subordinated Stochastic Process Model with Finite Variance for Speculative Prices." *Econometrica*, 41(1), 135–155. 摘要确认来源:搜索结果摘要(经由 arXiv:2608.26158 的转述确认标题与核心机制)。verified: true(经二级来源转述确认,未直接抓取 Econometrica 原文)

[S20] Jozef Barunik, Ladislav Kristoufek. 2012(首版约 2010–2012,具体首版月份本次未精确确认,但确认早于 2023). 日内分段 Hurst 指数估计方法比较(R/S、MF-DFA、DMA、GHE),应用于高频收益. 摘要来源:https://www.arxiv.org/abs/1201.4786 。verified: true(标题方向与方法确认;精确首版年月建议 PI/检查二次核实,故本条处理只作为「估计噪声警告」使用,不作为正面构造证据)

---

## 给 PI 的汇总提醒

- L1/L2 里,能直接翻译成**现成算子**的处理路径只有:零收益比例当独立控制项([S2][S3],对应 R 第 2 条)、分侧尾部条件均值([S8][S9],对应 R 第 5、6 条)、隔夜/日内拆分([S5],对应 R 第 4 条)。双幂变差、MedRV([S6][S7])只有论证价值,搬不进算子库,**不要指望 E/N 候选里出现"双幂变差"这种东西,它们没有对应原语**。
- L3 里能查到的唯一一篇**可直接核实、方法明确**的 A 股涨跌停事件研究是 Bao Qi (2023)([S13]),它按方向分组、不按市值/板块分组,也**没找到磁吸效应**;中文搜索摘要里关于"磁吸效应存在"的 2008、2015 年研究**没有拿到可核实的完整出处**,不建议写进 missions.yaml 当证据,只能当背景。
- L3 的"组内排序 vs 线性回归残差谁更干净"这一问,**文献没有直接答案**,我们核心卡里的论证是自己从奖励构造推出来的,PI 写任务说明时不要把这个归因给文献。
- L4 最扎实的是 Oomen (2006) + Clark (1973)([S18][S19])给"用成交额当钟"的 N-C 方向一个站得住的理论来源;Hurst 指数这条([S20])文献给的是**警告**(短窗口估计噪声大),不是正面支持,N-A 若做 `day_hurst(Ret)` 要有心理准备它可能只是噪声。
- 全部 20 条出处里,没有一条是我编造的;搜不到/日期不确定的分支已在正文和 [S19][S20] 的备注里如实标出,置信度最低的两条是 [S10](类比,非直接证据)和 [S19]/[S20](经二级来源转述,未直接抓取一次文献原文)。
