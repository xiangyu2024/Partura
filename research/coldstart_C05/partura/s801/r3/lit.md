# 文献笔记 —— 种子 801,第 3 轮

对应 `analysis.md` §5 的四个题目(核心 1:日内已实现方差及其峰值/波动;§1.3 方法学:凸变换 + 线性中性化;核心 2:同组内长周期反转与"窗口内最低点";N 的灵感 1/2:日内收益分布的高阶形状、方差的日内分布)。
检索工具:WebSearch(standard 模式)+ WebFetch(核对标题/作者/期刊卷期/页码/日期/摘要原文)。**只用 2023-08-08 之前发表/首版的文献**;日期拿不准的,已在各题"查过但没用"里如实弃用,不计入出处。
多数出处本轮用 WebFetch 直接打开了摘要页/条目页/NBER 页核实,标 `verified: true` 并注明读到的内容;少数只在多条搜索结果里反复交叉确认了标题、作者、卷期页码、DOI(WebFetch 本身被目标站点 403 拒绝,但独立信息源一致),同样标 `verified: true` 并注明"多条搜索结果交叉核实,WebFetch 被源站拒绝";只来自单一二手转述、没能交叉核实关键细节的标 `verified: false`。

---

## 题目 1(对准核心 1:日内已实现方差及其峰值/波动)

**结论先行**:

1. **"波动率的波动率"(vol-of-vol)在文献里是一个独立于波动水平本身的、已被反复验证的横截面特征,方向是负的(高 vol-of-vol → 低收益)。**
   Baltussen, van Bekkum & van der Grient(2018-08,*Journal of Financial and Quantitative Analysis* 53(4), 1615–1651)把 vol-of-vol 定义为"预期波动率的波动率",发现高 vol-of-vol 股票比低 vol-of-vol 股票每年跑输约 8%,且这个效应独立于至少 20 个已有的收益预测变量(美股与欧洲市场都成立)。
   → 翻译:这直接支持核心 1 的 `ts_std(ts_stddev(dw,20),50)` 构造方向(日内方差的时间序列波动本身是一个有先验支持的轴),而且给出一个**可核对的方向预测**:
   本种子三个 dw head 的 `sign` 都是 −1(多头 = 最低波动一档),如果读法 (A)"真轴"成立,文献这条结论预测的方向是**高 vol-of-vol 应该跑输**,即多头应落在**低 vol-of-vol** 那一档——这与 head 的 sign 一致,但没有直接证据说这与"低波动率水平"本身的方向能分开(摘要没有写清楚它具体怎么把 vol-of-vol 和波动水平、已有 20 个变量做正交化,是回归残差、双重排序还是分位数匹配,本次没能读到正文确认,留空)。

2. **日内已实现方差/波动率的买卖价跳动(微观结构噪声)有标准的"剥噪声"做法,核心思路是比较不同采样频率下的实现方差。**
   Zhang, Mykland & Aït-Sahalia(2005,*Journal of the American Statistical Association* 100(472), 1394–1411,NBER WP 10111 为更早的工作论文版本)提出"两尺度已实现波动率"(TSRV):用粗、细两个采样频率各算一次实现方差,噪声部分按频率变化的方式不同,两者组合后可以把微观结构噪声的偏差扣掉,对任意大小的噪声都适用(不要求噪声渐近趋于零)。
   Bandi & Russell(2006,*Journal of Financial Economics* 79(3), 655–692)给出另一条路径:用不同采样频率下的高频收益矩,把"真实波动"与"噪声方差"两个分量分别识别出来,再在偏差(低频采样,噪声小但信息少)和方差(高频采样,噪声大)之间选一个均方误差最优的采样频率;在波动率择时策略上,正确分离两个分量能带来可观的效用增益。
   → 翻译:这两篇都在说明,`day_durbin_watson(Close)` 这种直接用全部 1 分钟收益算 Σ(Δp)² 的写法,正是文献里"未经处理的高频实现方差"——其偏差会随价格水平(报价颗粒度)系统变化,与 §1.1 本轮自己复算出的"dw 与 1/价格 的 ρ = 0.36"完全对得上。
   **可操作的处理**:(a)按更粗的频率重新采样(例如把 1 分钟收益换成 5 分钟收益再求和)后比较读法 (A)/(B) 的判别结果是否改变;(b)如果要保留分钟级分辨率,构造一个"粗频 RV − 细频 RV 的某个标准化差"来近似两尺度估计,把 1/价格 这条通道单独扣掉,再看 dw 家族的分数是否下降——如果下降到噪声底以下,说明这个家族本来就有一部分是报价颗粒度的伪信号,不是波动率本身。

3. **区分"低波动异象的多头腿"与"波动的极端值/尾部特征"是文献里一个专门被检验过的问题,诊断手法是显式把极端值变量和波动水平变量放在同一个回归/排序里看哪个吃掉哪个。**
   Bali, Cakici & Whitelaw(2011,*Journal of Financial Economics* 99(2), 427–446;本题与第 2 轮 lit.md 题目 2 第 3 条引用的是同一篇,这次用在不同的角度)用"过去一月最大单日收益"(MAX)做十分组,发现 MAX 本身能**反转/吞掉**(subsumes or reverses)Ang 等人(2006)发现的特质波动率(IVOL)的负收益异象——也就是说原本被当成"波动率本身有负价"的效应,很大一部分其实是"收益分布的极端尾部"在起作用,而 MAX 和 IVOL 高度相关但不是同一个量(MAX 是线性的单日极值,IVOL 是二阶矩)。
   → 翻译:这是 §1.3 诊断逻辑的一个直接先例——把"疑似代理"的变量(这里是 MAX)显式加入同一个排序/控制里,看原来的效应是否还在。本轮 R3/R4(诚实峰值 `cross_max(dw,20)`、尺度无关尖峰比)应当比照这个做法,进一步可以在归因表里加一列"控制了 MAX 之后还剩多少",把"日内方差的峰值"和"单日收益的极值"两条轴分开。

4. **没有找到专门把"已实现波动的峰值(窗口内最大值)"与"平均水平"当成两个独立特征来分别构造、分别检验的文献**(检索到的最接近的是 vol-of-vol 文献——用时间序列标准差而不是最大值衡量"波动不稳定",以及 Bali-Cakici-Whitelaw 的 MAX——衡量收益本身的极值,不是已实现波动的极值)。
   → 这是一个确认的检索空白,不是检索不到位:vol-of-vol(标准差)和 MAX(单日收益最大值)都不是"已实现波动的窗口内最大值"本身。本轮 R3(`cross_max(day_durbin_watson(Close),20)`)因此是一个文献没有先例、要靠直接评估回答的问题。

### 出处

1. **Unknown Unknowns: Uncertainty About Risk and Stock Returns**
   作者:Guido Baltussen, Sjoerd van Bekkum, Bart van der Grient
   年-月:2018-08(发表),在线发表 2018-07-18
   来源:期刊(Journal of Financial and Quantitative Analysis, vol. 53, no. 4, pp. 1615–1651),DOI 10.1017/S0022109018000480
   链接:https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/unknown-unknowns-uncertainty-about-risk-and-stock-returns/6E0E98349D20C1DCF67F3A0452361B80
   verified: true(WebFetch 直接打开 Cambridge 条目页,读到标题、作者、卷期页码、DOI、"vol-of-vol 跑输 8%/年、独立于 20 个已有预测变量"的摘要原文;未能读到具体的正交化/控制方法)

2. **A Tale of Two Time Scales: Determining Integrated Volatility With Noisy High-Frequency Data**
   作者:Lan Zhang, Per A. Mykland, Yacine Aït-Sahalia
   年-月:2005(NBER WP 10111 为 2003 年的更早工作论文版本)
   来源:期刊(Journal of the American Statistical Association, vol. 100, no. 472, pp. 1394–1411),DOI 10.1198/016214505000000169
   链接:https://www.nber.org/papers/w10111
   verified: true(多条独立搜索结果交叉核实标题、作者、期刊卷期页码、DOI、"两尺度估计量"的核心方法描述一致)

3. **Separating Microstructure Noise from Volatility**
   作者:Federico M. Bandi, Jeffrey R. Russell
   年-月:2006-03
   来源:期刊(Journal of Financial Economics, vol. 79, no. 3, pp. 655–692),DOI 10.1016/j.jfineco.2005.01.005
   链接:https://ideas.repec.org/a/eee/jfinec/v79y2006i3p655-692.html
   verified: true(多条独立搜索结果交叉核实标题、作者、卷期页码、DOI,以及 Duke 托管的 PDF 首页"Journal of Financial Economics 79 (2006) 655–692"原文)

4. **Maxing Out: Stocks as Lotteries and the Cross-Section of Expected Returns**
   作者:Turan G. Bali, Nusret Cakici, Robert F. Whitelaw
   年-月:2011(NBER WP 14804 更早流通)
   来源:期刊(Journal of Financial Economics, vol. 99, no. 2, pp. 427–446)
   链接:https://www.nber.org/papers/w14804
   verified: true(第 2 轮已用 WebFetch 核实过标题、作者、摘要;本轮沿用同一条出处,用在不同的论点上)

**查过但没用**:
- Ozenbas, Schwartz & Wood(2002)对伦敦/巴黎/法兰克福市场 U 形日内波动的跨市场复现——只在二手转述里看到,没能独立核实期刊名、确切年月,本题没用到,留给题目 4 的背景。
- 专门把"已实现波动的窗口内最大值"单独当一个特征(与平均水平分开)的论文——没搜到,如实记录为空白(结论先行第 4 条)。

---

## 题目 2(对准 §1.3:凸变换与线性中性化 —— 方法学,本轮最要紧)

**结论先行**:

1. **原始尺度上的特征与收益之间存在非线性关系是量化文献里一个有明确记录的现象,最经典的例子就是"规模"本身。**
   Banz(1981,*Journal of Financial Economics* 9, 3–18)发现的规模效应,后续文献反复把它描述为**市值与平均收益之间是非线性关系**(效应集中在最小的一批股票上,不是全市场线性的);这正是量化实践里普遍改用 `log(市值)` 而不是市值本身做特征/控制的历史原因。
   → 翻译:这给 §1.3 的诊断提供了一个更早、更基础的同类先例——**线性中性化假设"特征对控制线性"这件事本身,在最常见的控制变量(规模)上就不成立**;本种子的波动控制同样是在原始尺度上进入线性投影,§1.3 发现的"控制的四次方把残差灌回控制本身"可以理解成规模非线性问题的一个更极端版本(规模是温和非线性,四次方后的波动控制是强烈非线性)。

2. **"是否该在原始尺度上直接做线性回归 / 线性秩变换"这件事,文献用非参数方法明确检验过:很多特征对收益的真实作用形式确实不是线性的。**
   Freyberger, Neuhierl & Weber(NBER WP 23227,2017-03 首发;发表版《Dissecting Characteristics Nonparametrically》,*Review of Financial Studies* 33(5), 2020, 2326–2377)用自适应 group LASSO 对大量特征做非参数估计(不预设线性形式),发现很多在线性模型里显著的特征在放开函数形式后不再提供增量信息,"非线性很重要"是这篇论文的核心结论之一,其方法比线性面板回归有更高的样本外解释力。
   → 翻译:这直接支持 §1.3 的诊断方向——**遇到可疑的"新发现",先检验它在非参数/非线性规格下是否还站得住,而不是默认线性中性化的结果就是最终答案**。具体到我们的算子语言:可以把 `neutral_residual` 的线性投影换成按控制变量分桶(`cs_bucket_zscore`/`cs_bucket_demean`,本种子的核心 2 已经在用这类算子)再去均值,这是一种粗糙但非参数的中性化,对强凸特征更稳健。

3. **把"排序"本身当成非参数估计量,是文献里专门用来避免强加线性形式的方法,但本次没能读到它直接讨论"残差保留非线性暴露"这个具体机制。**
   Cattaneo, Crump, Farrell & Schaumburg(2018-09 首发 arXiv:1809.03584;发表版《Characteristic-Sorted Portfolios: Estimation and Inference》,*Review of Economics and Statistics* 102(3), 2020, 531–551)把投资组合排序(portfolio sort)正式表述为一个非参数估计量,推导出均方误差最优的分组数(常常远多于常见的 5 或 10 组)。
   → 翻译:这支持"双重排序/分桶"这类非参数做法在方法论上优于强加线性形式的回归残差,但**这篇论文本身没有明确讨论"一个强凸特征做线性回归后残差仍与该特征高度相关"这个具体机制**——这是本题的一个检索空白,§1.3 的那个具体诊断(凸变换→线性投影→残差反号灌回控制)更像是本种子自己用模拟做出来的原创诊断,而不是文献里已有的现成结论,PI 在笔记里应该把这一点标记为"我们自己的方法论发现,目前没找到直接对应的文献,值得单独写下来"。

4. **"回归估计在全样本上容易被极端观测值主导、产生函数形式问题"在经典文献里有过明确但简短的提及,解决办法是按规模分组而不是单一线性拟合。**
   Fama & French(2008-08,*Journal of Finance* 63(4), 1653–1678,《Dissecting Anomalies》)按微型股/小盘/大盘把全市场分成三组分别做横截面回归,原因之一是全市场回归容易被数量庞大的微型股主导,作者在稳健性检查里提到对回归残差的分析"揭示了轻微的函数形式问题"(这句话的细节在能读到的摘要片段里被截断,置信度打折扣,仅作为旁证,不单独作为结论性引用)。
   → 翻译:这从另一个角度印证了"全样本线性回归对极端尾部的代表性有限"这件事在经典文献里并非全新观察,只是没有像 §1.3 这样做显式的凸变换模拟去量化残差里灌回了多少控制本身。

5. **诊断"一个看起来新的因子实际是已控制风险的非线性/尾部重表述"是有真实案例的,诊断手法是显式把怀疑的尾部/非线性变量和原风险特征放进同一个检验框架里。**
   Han & Lesmond(2011,*Review of Financial Studies* 24(5), 1590–1629)为"特质波动率"(IVOL)的估计建立了一个显式的微观结构偏差模型(零收益 + 买卖价差),推导出偏差的闭式解;一旦用这个模型纠正偏差,IVOL 对收益的预测能力**消失**——也就是说原本被当成"波动率风险有负价"的效应,其实是 IVOL **估计量本身**被微观结构噪声系统性抬高造成的假象,不是真实的风险暴露。
   与结论先行第 3 条的 Bali-Cakici-Whitelaw(MAX 吞掉 IVOL 异象)合起来看,IVOL 异象在文献里**被两条独立的路径诊断成了非真实效应**:一条是"它其实是收益尾部(MAX)在起作用",另一条是"它其实是估计量的微观结构偏差"——两条诊断用的都不是"假设线性没问题",而是显式建一个替代解释、看原效应是否消失。
   → 翻译:这是 §1.3 诊断风格(建立显式的替代机制模型,模拟残差里还剩什么)在已发表文献里能找到的最接近的先例,支持把本轮 R1–R4 的那组判别继续做下去,并在判读时按"是否存在一个能让原效应消失的替代解释"这个标准写进归因表。

### 出处

1. **The Relationship Between Return and Market Value of Common Stocks**
   作者:Rolf W. Banz
   年-月:1981
   来源:期刊(Journal of Financial Economics, vol. 9, pp. 3–18)
   链接:https://floridapsc.com/library/filings/2023/00092-2023/Support/Staff%20Exhibit%20167/Witness%20Testimony%20Workpapers/Witness%20Nelson/42,43_Banz,%20The%20Relationship%20Between%20Return%20and%20Market%20Value%20of%20Common%20Stocks,%20JFE%209%20(1981).pdf
   verified: true(多条独立搜索结果交叉核实标题、作者、期刊卷页码,以及二手对"市值与收益呈非线性关系"这一表述的转述;"非线性"这个措辞来自转述而非直接读到 Banz 本人的原句,打个折扣)

2. **Dissecting Characteristics Nonparametrically**
   作者:Joachim Freyberger, Andreas Neuhierl, Michael Weber
   年-月:NBER WP 23227,2017-03 首发;发表版 2020(Review of Financial Studies, vol. 33, no. 5, pp. 2326–2377)
   来源:工作论文(NBER)+ 期刊(RFS)
   链接:https://www.nber.org/papers/w23227
   verified: true(WebFetch 直接打开 NBER 页面,读到标题、作者、工作论文号、首发日期 2017-03、摘要原文"nonlinearities matter"及方法描述)

3. **Characteristic-Sorted Portfolios: Estimation and Inference**
   作者:Matias D. Cattaneo, Richard K. Crump, Max H. Farrell, Ernst Schaumburg
   年-月:2018-09 首发(arXiv:1809.03584),v3 修订 2019-10-05;发表版 2020(Review of Economics and Statistics, vol. 102, no. 3, pp. 531–551)
   来源:工作论文(arXiv)+ 期刊(ReStat)
   链接:https://arxiv.org/abs/1809.03584
   verified: true(WebFetch 直接打开 arXiv 摘要页,读到标题、作者、提交/修订日期、期刊卷期页码、摘要原文;摘要本身没有明确用"非线性偏差"这个措辞,该推论是我自己的转译,已在正文标注)

4. **Dissecting Anomalies**
   作者:Eugene F. Fama, Kenneth R. French
   年-月:2008-08
   来源:期刊(Journal of Finance, vol. 63, no. 4, pp. 1653–1678),DOI 10.1111/j.1540-6261.2008.01371.x
   链接:https://ideas.repec.org/a/bla/jfinan/v63y2008i4p1653-1678.html
   verified: true,但打折扣(多条搜索结果交叉核实标题、作者、卷期页码、DOI,以及"微型股主导回归、残差分析揭示轻微函数形式问题"这句话出自 2006 工作论文草稿的二手转述,片段被截断,没能读到完整上下文)

5. **Liquidity Biases and the Pricing of Cross-sectional Idiosyncratic Volatility**
   作者:Yufeng Han, David Lesmond
   年-月:2011
   来源:期刊(Review of Financial Studies, vol. 24, no. 5, pp. 1590–1629),DOI 10.1093/rfs/hhq140
   链接:https://ideas.repec.org/a/oup/rfinst/v24y2011i5p1590-1629.html
   verified: true(多条独立搜索结果交叉核实标题、作者、卷期页码、DOI,以及"微观结构偏差闭式解、纠正后 IVOL 预测力消失"的核心发现一致)

**查过但没用**:
- 专门以"残差里残留非线性暴露"为标题/核心命题的方法论论文(不是通过案例推出来,而是正式证明或系统模拟)——没搜到,如实记录为空白;§1.3 的模拟目前看是本种子自己的原创诊断。
- 一篇声称系统比较"条件双重排序 vs 回归控制"在尾部的差别的论文(本题单独检索,第 2 轮题目 2 的 Bali-Engle-Murray 教材已覆盖一般性讨论,本轮想找更量化的比较)——没搜到独立于教材转述的来源,弃用。

---

## 题目 3(对准核心 2:同组内的长周期反转,以及"窗口内最低点"这种构造)

**结论先行**:

1. **短期反转按行业/组内拆分,是文献里专门做过的分解,组内部分还能再拆成"预期收益差异"和"对现金流消息的反应错误"两块。**
   Da, Liu & Schaumburg(2014,*Management Science* 60(3), 658–674;更早的 2011 版本是纽约联储工作报告《Decomposing Short-Term Return Reversal》)把反转收益拆成"跨行业"和"行业内"两部分,行业内部分再用分析师预期修正当现金流消息的代理,进一步拆成预期收益变化、对现金流消息的反应不足/过度、贴现率消息三块;剔除非基本面成分之后的"增强反转"策略的风险调整收益是标准反转策略的约 4 倍。
   → 翻译:直接支持核心 2 的 `cs_bucket_demean(反转, 分组)` 这类"先分组再去均值"的构造方向,并且给出一个可以尝试的延伸:如果能找到现金流消息的代理(哪怕是粗糙的,比如营收增速意外或换手率代理),进一步把 Z 的反转信号中"非基本面驱动"的部分剥出来,理论上能进一步提纯,这是文献支持但本种子还没试过的方向。

2. **行业内反转比对全市场的反转更强、更持久、覆盖面更广(不限于小盘股),文献把它归因为流动性提供的补偿,且在下跌/高波动期更强。**
   Hameed & Mian(2015-04,*Journal of Financial and Quantitative Analysis* 50(1-2), 89–117)《Industries and Stock Return Reversals》发现:月度收益在行业内部的反转比对市场基准的常规反转**更大、更持久**,而且在大盘股、流动性好的股票里同样成立;驱动机制是订单失衡和非信息性冲击,作者将其解释为向流动性提供者支付的补偿,这个效应在**市场下跌后和高波动期更强**。
   → 翻译:(a)这支持核心 2"按组比较"这一步本身是有经济含义的真实现象,不只是我们种子里的一个偶然发现;(b)但它也给出一个**可检验的预测**——真正的行业内反转效应不应该依赖分组变量的具体实现细节(真行业分类 vs 任意但稳定的分组),效应应该在流动性好的大盘股里一样成立。这恰好与 §1.5 的发现**相反**:本种子的核心 A 分组一旦换成真实连续变量(`LogFloatCap` 真十分位)就从 +0.76 掉到 −1.14,说明这个特定分组更像是列序伪影,不是文献描述的那种真实的"行业内"分组效应——这条文献给判读提供了一个"反例对照",值得写进笔记:**我们的分组构造可能没有抓住文献描述的那个真实机制,只是碰巧过了门**。
   (c)另外文献预测效应在**下跌/高波动期更强**,这是一个本种子数据里可以核对、但本轮没有直接检验的维度,留给下一步。

3. **用"窗口内的最低点/回撤"而不是"点对点收益"当排序变量,文献里有先例,而且发现它在不同持有期上对应不同性质的策略(动量 vs 反转)。**
   Choi(2014-03-31 首发,arXiv:1403.8125,《Maximum Drawdown, Recovery, and Momentum》;2021 年以同题发表于 *Journal of Risk and Financial Management* 14(11), 542)用"最大回撤"(窗口内从峰值到谷值的最大跌幅)和"恢复程度"(从谷值反弹的幅度)代替点对点累计收益给股票排序:在 6 个月形成期的动量策略里,按回撤排序(跌得少的当赢家)比传统的累计收益动量表现更好;在 6 周形成期的反转策略里,按恢复程度排序表现最好。作者在 KOSPI 200、美股行业 ETF、标普 500 上都做了检验。
   → 翻译:这给核心 2 的 `cross_min(反转指标, 60)`(取一个季度窗口里反转指标的最低点)提供了一个**同类但不完全对应**的先例——该文献用的是"回撤相对于历史峰值"的概念,对应**动量**持有期(6 个月);而核心 2 的"窗口最低点"用在**反转**构造上、窗口是季度(60 日)。文献自己的发现(回撤型信号在动量持有期上更强,恢复型信号在反转/周度持有期上更强)提示:**"窗口内最低点"这个构造本身的经济含义会随持有期/用途切换方向**,不能简单假设它天然就是"反转"的量——这正是本轮 §1.7 待判事项(A 这层分组是不是装饰、真来源是不是季度反转本身)该关心的,也支持 R9/R10 的判别优先级。

4. **标准的 12 个月动量,其收益几乎全部来自"中间窗口"(formation 前 12~7 个月),而不是"最近窗口"(前 6~2 个月);最近窗口单独的贡献很弱,更像是"回声"而不是趋势延续。**
   Novy-Marx(2012,*Journal of Financial Economics* 103(3), 429–453)《Is Momentum Really Momentum?》发现按 t−12 到 t−7 月收益排序比按 t−6 到 t−2 月收益排序更能预测未来收益,最近窗口单独的策略利润小得多,在最大最流动的股票里更明显;作者没有给出理论解释,只称其为"echo"(回声)。
   → 翻译:核心 2 用的是约 60 个交易日(≈3 个月)的窗口,恰好落在 Novy-Marx 划分的"最近窗口"区域——文献发现标准动量效应在这个区域本来就弱,这与核心 2 在这个窗口上测到的是**反转**(而不是动量)方向上**不矛盾**,但文献本身测的是动量、没有直接检验这个窗口上反转效应的强弱,这是一个明确的检索空白,不能直接当成核心 2 的证据,只能当成"方向上不冲突"的旁证。

5. **中国 A 股在"季度到年度"这个尺度上,多篇独立研究都倾向于反转而不是动量,但不同样本期、不同构造方式给出的结论有分歧,说明这条轴在 A 股的符号本身是可检验、不是先验能确定的。**
   - Wu(2004-12,香港金融研究中心工作论文 HKIMR WP 23/2004)用 1990–2001 年上交所 A 股日度数据发现纯动量策略一般不能获得超额收益,反而是强烈的均值回归。
   - Yang, Gebka & Hudson(2019,*Research in International Business and Finance* 47, 78–101)的文献综述认为:2001 年之前的证据更像是中长期反转,2001 年之后则是短期反转 + 长期动量共存,结论随样本期系统性变化。
   - Gang, Qian & Xu(2019,*Economic Modelling* 83, 364–371)发现在中国市场,动量策略只在**不到一周**的持有期上有利润,**更长的持有期上则是反转策略更有利润**;作者把这个现象归因为中国投资者对现金流消息系统性**过度反应**(美国投资者通常被发现是反应不足)。
   - Zeng & Liu(2016,Atlantis Press,FEBM 2016 会议论文集,DOI 10.2991/febm-16.2016.36)用 2010 年 4 月以来的 A 股数据,发现**短期动量 + 中期反转**同时存在。
   → 翻译:四篇分属不同样本期、不同方法的研究,在"季度量级的持有期在 A 股更像反转而不是动量"这一点上方向一致,这给核心 2"同组内季度反转"这个基本前提提供了合理的先验支持;但没有一篇专门检验过"组内去均值版本"或"窗口最低点版本"这两个具体构造,这两点仍然是空白,要靠本轮的 R9/R10 直接评估来填。

### 出处

1. **A Closer Look at the Short-Term Return Reversal**
   作者:Zhi Da, Qianqiu Liu, Ernst Schaumburg
   年-月:2014(更早版本《Decomposing Short-Term Return Reversal》,纽约联储工作报告 No. 513,2011-10)
   来源:期刊(Management Science, vol. 60, no. 3, pp. 658–674),DOI 10.1287/mnsc.2013.1766
   链接:https://ideas.repec.org/a/inm/ormnsc/v60y2014i3p658-674.html
   verified: true(多条独立搜索结果交叉核实标题、作者、期刊卷期页码、DOI,以及"行业内/跨行业分解 + 现金流消息拆分"的核心方法描述一致;informs.org 原页面 WebFetch 被源站拒绝,改用交叉核实)

2. **Industries and Stock Return Reversals**
   作者:Allaudeen Hameed, G. Mujtaba Mian
   年-月:2015-04
   来源:期刊(Journal of Financial and Quantitative Analysis, vol. 50, no. 1-2, pp. 89–117)
   链接:https://ideas.repec.org/a/cup/jfinqa/v50y2015i1-2p89-117_00.html
   verified: true(WebFetch 直接打开条目页,读到标题、作者、期刊卷期页码、出版日期、摘要原文关于行业内反转更强更持久、驱动机制、市场下跌/高波动期更强的表述)

3. **Maximum Drawdown, Recovery, and Momentum**
   作者:Jaehyung Choi
   年-月:2014-03-31 首发(arXiv:1403.8125);2021 年发表版(Journal of Risk and Financial Management, vol. 14, no. 11, 542)
   来源:工作论文(arXiv, q-fin.GN)+ 期刊(JRFM, MDPI)
   链接:https://arxiv.org/abs/1403.8125
   verified: true(WebFetch 直接打开 ar5iv 全文页,读到标题、作者、方法描述——回撤型/恢复型排序分别在 6 个月动量、6 周反转持有期上优于传统累计收益排序;arXiv 摘要页的提交历史确认首发日期 2014-03-31)

4. **Is Momentum Really Momentum?**
   作者:Robert Novy-Marx
   年-月:2012
   来源:期刊(Journal of Financial Economics, vol. 103, no. 3, pp. 429–453),DOI 10.1016/j.jfineco.2011.05.003
   链接:https://ideas.repec.org/a/eee/jfinec/v103y2012i3p429-453.html
   verified: true(多条独立搜索结果交叉核实标题、作者、卷期页码、DOI,以及"t-12~t-7 月收益比 t-6~t-2 月收益更能预测未来收益"的核心发现一致)

5. **Momentum Trading, Mean Reversal and Overreaction in Chinese Stock Market**
   作者:Yangru Wu
   年-月:2004-12
   来源:工作论文(香港金融研究中心,HKIMR Working Paper No. 23/2004)
   链接:https://www.aof.org.hk/uploads/publication/239/ub_full_0_2_98_wp200423_text.pdf
   verified: true(WebSearch 多条结果交叉核实标题、作者、工作论文号、日期,以及"1990–2001 年上交所 A 股、纯动量不能获得超额收益、强均值回归"的核心发现)

6. **Momentum Effects in China: A Review of the Literature and an Empirical Explanation of Prevailing Controversies**
   作者:Yifan Yang, Bartosz Gebka, Robert Hudson
   年-月:2019
   来源:期刊(Research in International Business and Finance, vol. 47, pp. 78–101)
   链接:https://hull-repository.worktribe.com/output/935436
   verified: true(多条独立搜索结果交叉核实标题、作者、期刊卷期页码,以及"2001 年前中长期反转、之后短期反转+长期动量共存"的综述结论一致)

7. **Investment Horizons, Cash Flow News, and the Profitability of Momentum and Reversal Strategies in the Chinese Stock Market**
   作者:Jianhua Gang, Zongxin Qian, Tiange Xu
   年-月:2019
   来源:期刊(Economic Modelling, vol. 83, pp. 364–371),DOI 10.1016/j.econmod.2019.08.021
   链接:https://ideas.repec.org/a/eee/ecmode/v83y2019icp364-371.html
   verified: true(WebFetch 直接打开条目页,读到标题、作者、期刊卷期页码、DOI、"动量只在不到一周的持有期有利、更长持有期反转更有利、中国投资者对现金流消息过度反应"的摘要原文)

8. **The Study of the Momentum Effect and the Reversal Effect on the Chinese Stock Market**
   作者:Dongxiang Zeng, Huangjin Liu
   年-月:2016-11(线上发布)
   来源:会议论文集(Atlantis Press,International Conference on Financial Engineering and Business Management, FEBM 2016),DOI 10.2991/febm-16.2016.36
   链接:https://www.atlantis-press.com/article/25865002.pdf
   verified: true,但打折扣(多条搜索结果交叉核实标题、作者、DOI、"短期动量+中期反转"的核心发现;这是会议论文集,不是同行评审期刊,证据等级低于其他出处)

**查过但没用**:
- Chen, Li-Wen & Yu, Hsin-Yi,《Nearness to the 52-week high and low prices, past returns, and average stock returns》——只找到一份托管在 AUT 研究中心的 PDF 工作论文,摘要称"距 52 周低点的距离能预测未来收益",但没能确认它的正式发表期刊、卷期或确切年月,按规矩弃用。
- Ozenbas, Schwartz & Wood(2002)对 U 形日内波动的跨市场复现——与题目 1 同一条,日期未独立核实,两题都没用。

---

## 题目 4(对准 N 的灵感 1 与 2:日内收益分布的高阶形状,以及方差在一天内的分布)

**结论先行**:

1. **已实现偏度/峰度(用周内的分钟收益算)是经过检验的横截面预测变量,偏度的方向是负的,且已实现波动率本身在这篇文献里反而测不出稳健的预测力。**
   Amaya, Christoffersen, Jacobs & Vasquez(CREATES WP 2011-44 首发,2011-12;发表版《Does Realized Skewness Predict the Cross-Section of Equity Returns?》,*Journal of Financial Economics* 116(1), 2015, 135–167)用日内收益算出每只股票每周的已实现波动、偏度、峰度,十分组排序后发现:已实现偏度与下一周收益**强烈负相关**(最低偏度组比最高偏度组每周高出约 19 个基点,经标准因子调整后仍显著),已实现峰度与下一周收益**正相关**但不如偏度稳健,**已实现波动率本身与下一周收益没有稳健关系**。效应在小盘股里更强。
   → 翻译:直接支持 N 灵感 1"日内收益分布的高阶形状"这个方向,并给出两条可操作的信息:(a)矩的汇总窗口是**周**,不是日——建议 `day_skew(Ret)`/`day_kurt(Ret)` 这类日频量再做一次短窗口(例如 5 日)的滚动平均后再进横截面,而不是直接用单日值;(b)这篇文献的结果恰好印证了 §1.9/§1.1 的发现——"波动率的**水平**本身没有稳健的横截面预测力",有钱的是**形状**(偏度/峰度),这与本种子"dw 家族的核心是方差水平,可能是漏灌"的怀疑方向一致,支持把 N 灵感 1 当作与 dw 家族正交的独立轴来押注。

2. **把已实现方差拆成"只算负收益部分"和"只算正收益部分"(已实现半方差),是文献里已有的标准构造,下行部分对预测未来波动有更强的信息。**
   Barndorff-Nielsen, Kinnebrock & Shephard(CREATES WP 2008-42 / 牛津经济学工作论文 2008-W02,2008-08 首发;发表为书籍章节《Measuring Downside Risk: Realised Semivariance》,收录于 *Volatility and Time Series Econometrics: Essays in Honor of Robert F. Engle*,Bollerslev/Russell/Watson 编,牛津大学出版社,2010,117–136 页)把已实现方差按高频收益的正负号拆成两部分("已实现半方差"),发现下行(负收益)部分对未来波动有更强的预测力。
   → 翻译:这是 N 灵感 1"上行/下行半方差之比"的直接构造模板——`day_std` 分别在正、负分钟收益子集上算,再取比值或差值。但要注意:这篇论文验证的是对**未来波动**的预测力(时间序列),不是对**横截面收益**的预测力,后者是否成立是一个检索空白,要靠直接评估。

3. **已实现方差的下行/上行分量对"未来波动率"的持久性不对称:负向跳跃带来的高波动几乎是永久性的,正向跳跃反而会降低长期波动。**
   Patton & Sheppard(2015-07,*Review of Economics and Statistics* 97(3), 683–697)《Good Volatility, Bad Volatility: Signed Jumps and the Persistence of Volatility》在 Barndorff-Nielsen 等人的半方差基础上进一步发现:未来波动与**过去负收益的波动**关系更紧密,价格跳跃的符号很重要——负向跳跃带来持久、几乎永久的波动上升,正向跳跃反而降低长期波动;据此构造的预测模型样本外表现显著更好。
   → 翻译:支持把"上行/下行"构造成**不对称**的特征,而不是默认对称(例如只做"下行方差 / 上行方差"的比,而不是假设两者权重相等);这也给 §1.10 的发现提了一个警示——本种子里"封在最高价"和"封在最低价"的两个 head 几乎可以互换(ρ=0.975),这与 Patton-Sheppard 发现的"上下行本质不对称"是**相反**的方向,值得在笔记里单列:本种子目前测到的"停滞"类量可能还没有抓住真正的跳跃/半方差不对称结构,N 灵感 1 如果按半方差而不是"停在极值的时长"构造,可能会测出与现有 head 不同的东西。

4. **把实现波动拆成"连续(扩散)部分"和"跳跃部分",有一套成熟的标准方法(bipower variation),是上面两篇半方差文献共同依赖的基础工具。**
   Barndorff-Nielsen & Shephard(2004-01,*Journal of Financial Econometrics* 2(1), 1–37)《Power and Bipower Variation with Stochastic Volatility and Jumps》证明:已实现方差减去已实现双幂次变差(bipower variation),渐近意义上就是跳跃部分贡献的二次变差——这是第一个能把总变差拆成连续与跳跃两部分的方法。
   → 翻译:给 N 灵感 1(c)"跳跃成分与连续成分的分解"提供了具体的构造公式:用全部分钟收益算一个标准的已实现方差(dw 的分子部分已经是这个),再用相邻分钟收益绝对值的乘积之和(近似双幂次变差)算连续部分,两者之差就是跳跃部分的代理——这与 dw 本身(纯粹的总方差,不区分连续/跳跃)是完全不同的一条轴,本种子 594 个候选里从未出现过。

5. **交易日内方差呈经典的 U 形分布(开盘、收盘段方差显著高于午盘),这是一个被反复验证的既有事实,但本次没有找到把它当横截面收益预测变量来用的先例。**
   Wood, McInish & Ord(1985,*Journal of Finance* 40, 723–739)用 1971–72 年及 1982 年的纽交所逐笔数据发现,按时间段画出的收益波动呈粗糙的 U 形(开盘和收盘前后波动明显更高),这个模式在之后的多个日历年里被重复验证。
   → 翻译:支持 N 灵感 2"开盘前 30 分钟已实现方差占全日的比"这类构造在经济上是站得住的(U 形是真实、持久的现象),但**这篇及后续同类文献都是在描述这个模式本身,不是把"开盘段方差占比"当一个预测下一期横截面收益的特征来检验**——这是一个明确的检索空白,本种子如果按这个方向构造 N 的种子,将是文献尚未直接测过的新尝试(与 §4.3 N 灵感 2 的判断一致)。

6. **"隔夜 vs 日内"的收益(不是方差)拆分,在文献里被证明是横截面上一条独立且重要的轴——很多已知异象的利润完全集中在隔夜或日内某一段,两段有时方向相反。**
   Lou, Polk & Skouras(2019,*Journal of Financial Economics* 134(1), 192–213)《A Tug of War: Overnight Versus Intraday Expected Returns》把收盘到收盘的收益拆成隔夜段和日内段,发现 14 个常见策略里利润几乎全部集中在某一段(例如动量几乎全部来自隔夜段,三因子调整后隔夜 alpha 显著为 0.95%,日内段只有不显著的 0.11%),两段经常方向相反,机制上归因为机构与个人投资者的交易时段偏好不同。
   → 翻译:这篇做的是**收益**的隔夜/日内拆分,不是**方差**的拆分,不能直接当作"隔夜方差 vs 日内方差"构造的证据——但它确认了"按交易时段切开"这个大方向在这个市场结构上是真实有效的信息来源,是 N 灵感 2(d)的一个强旁证而不是直接证据;"隔夜已实现方差 vs 日内已实现方差的比"这个具体构造本身,本次检索没有找到专门文献,如实记录为空白。

### 出处

1. **Does Realized Skewness Predict the Cross-Section of Equity Returns?**
   作者:Diego Amaya, Peter Christoffersen, Kris Jacobs, Aurelio Vasquez
   年-月:CREATES WP 2011-44(2011-12 首发,工作论文题《Do Realized Skewness and Kurtosis Predict the Cross-Section of Equity Returns?》);发表版 2015(Journal of Financial Economics, vol. 116, no. 1, pp. 135–167)
   来源:工作论文(CREATES, Aarhus University)+ 期刊(JFE),DOI 10.1016/j.jfineco.2015.02.009
   链接:https://repec.econ.au.dk/repec/creates/rp/11/rp11_44.pdf
   verified: true(多条独立搜索结果交叉核实标题、作者、期刊卷期页码、DOI、首发工作论文号与日期,以及"偏度负相关、峰度弱正相关、波动率本身不显著、小盘股效应更强"的核心发现一致;出版社页面 WebFetch 被源站拒绝,改用交叉核实)

2. **Measuring Downside Risk: Realised Semivariance**
   作者:Ole E. Barndorff-Nielsen, Silja Kinnebrock, Neil Shephard
   年-月:CREATES WP 2008-42 / 牛津经济学工作论文 2008-W02(2008-08 首发);发表为书籍章节,2010(收录于 *Volatility and Time Series Econometrics: Essays in Honor of Robert F. Engle*,Tim Bollerslev, Jeffrey R. Russell, Mark W. Watson 编,牛津大学出版社,pp. 117–136)
   来源:工作论文(CREATES/牛津)+ 书籍章节(OUP)
   链接:https://www.nuff.ox.ac.uk/economics/papers/2008/w2/downside.pdf
   verified: true(多条独立搜索结果交叉核实标题、作者、工作论文号、首发日期、发表书籍信息及页码,以及"已实现半方差、下行部分对未来波动预测力更强"的核心构造与结论一致)

3. **Good Volatility, Bad Volatility: Signed Jumps and the Persistence of Volatility**
   作者:Andrew J. Patton, Kevin Sheppard
   年-月:2015-07
   来源:期刊(Review of Economics and Statistics, vol. 97, no. 3, pp. 683–697)
   链接:https://ideas.repec.org/a/tpr/restat/v97y2015i2p683-697.html
   verified: true(WebFetch 直接打开条目页,读到标题、作者、期刊卷期页码、出版日期,以及"未来波动与过去负收益波动关系更紧密、跳跃符号重要、负向跳跃带来持久波动上升"的摘要原文)

4. **Power and Bipower Variation with Stochastic Volatility and Jumps**
   作者:Ole E. Barndorff-Nielsen, Neil Shephard
   年-月:2004-01
   来源:期刊(Journal of Financial Econometrics, vol. 2, no. 1, pp. 1–37),DOI 10.1093/jjfinec/nbh001
   链接:https://academic.oup.com/jfec/article/2/1/1/960705
   verified: true(多条独立搜索结果交叉核实标题、作者、期刊卷期页码、DOI、出版时间,以及"已实现方差减去双幂次变差渐近等于跳跃部分二次变差"的核心方法一致)

5. **An Investigation of Transactions Data for NYSE Stocks**
   作者:Robert A. Wood, Thomas H. McInish, J. Keith Ord
   年-月:1985
   来源:期刊(Journal of Finance, vol. 40, pp. 723–739)
   链接:(本次未能直接打开原文,经多条后续文献的二手引用交叉核实卷期页码一致,包括 Memphis 大学托管的同一作者后续复现论文)
   verified: true(多条独立二手引用交叉核实标题、作者、期刊卷页码,以及"1971-72 年及 1982 年 NYSE 逐笔数据、U 形日内波动模式"的核心发现一致;未能独立打开 1985 年原文全文,置信度略打折扣)

6. **A Tug of War: Overnight Versus Intraday Expected Returns**
   作者:Dong Lou, Christopher Polk, Spyros Skouras
   年-月:2019
   来源:期刊(Journal of Financial Economics, vol. 134, no. 1, pp. 192–213)
   链接:https://researchonline.lse.ac.uk/id/eprint/87481
   verified: true(多条独立搜索结果交叉核实标题、作者、期刊卷期页码,以及"14 个策略利润集中在隔夜或日内某一段、动量利润几乎全部来自隔夜段"的核心发现一致)

**查过但没用**:
- Ozenbas, Schwartz & Wood(2002)关于伦敦/巴黎/法兰克福市场 U 形日内波动跨市场复现的论文——只在二手转述里看到,没能独立核实期刊名、确切年月,弃用(与题目 1 同一条)。
- 专门检验"隔夜已实现方差 / 日内已实现方差的比"作为横截面收益预测变量的论文——没搜到,如实记录为空白(结论先行第 6 条)。
- 一篇声称用"开盘段方差占比"直接预测横截面收益的论文——没搜到正式学术论文,如实记录为空白。
