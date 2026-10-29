# 文献:种子 806,B 组,第 2 轮

读入:`r2/analysis.md` §5 的四个题目(Q1 对准核心 A `ts_quantile_q50(day_centroid(Amt), 20)`;Q2 对准核心 B `day_kurt(Ret)`;
Q3 对准 F1/F2(折叠的市值秩、名义股价分段)与「中性化只去线性项」这个机械事实;Q4 对准 N2 的「筛选式/分段」处理)。
只用 WebSearch / WebFetch 查到、且能确认**首版日期(或该版本在 SSRN/期刊 DOI 上的最早登记日期)在 2023-08-08 之前**的论文、工作论文、研究报告。
日期拿不准、或经核实发现实际晚于 2023-08-08 的,一律在「搜不到 / 拿不准」里写明,不当证据用,不编造。

每条处理方式后面用 `[键]` 标出处,键对应文末「出处列表」。同一出处可能支撑多条处理。

---

## Q1 —— 日内成交的时间分布(核心 A:成交的时间重心,20 日中位数)怎样被做成截面预测变量

**能摘到的处理方式:**

1. **把「成交集中在哪个时段」读成「哪类投资者在主导当时的交易」,而不是读成一个中性的统计矩。**
   最早的理论工作证明,U 形的日内成交 / 波动模式是知情交易者与流动性交易者**策略性地把交易扎堆**到执行成本低的时段
   这一内生选择的结果,而不是外生噪声;该模型还推出「成交量越大的时段价格越有信息含量」。
   翻成算子语言:`day_centroid(Amt)` 不该只当一个连续的「0~1 水平」用,更该按它所在的**时段分桶**(偏开盘 / 偏收盘 / 居中)来读,
   因为两端在理论上对应不同的交易者构成,是「分类」问题,不只是「排序」问题 —— 这为 analysis.md §4.1 建议的
   `cs_bucket_zscore(core, ·)` 这类条件化处理提供了理论依据(不是只能用 `sub`/`ts_rank` 这类连续变换)。[AP1988]

2. **同一批作者明确检验过「这是不是量 / 流动性的代理」,结论是不是。**
   Heston–Korajczyk–Sadka(2010,已在 r1 用过)报告:半小时收益的跨日延续现象持续约 40 个交易日,
   同一批数据里**成交量、订单不平衡、波动率、买卖价差都呈现相似的日内模式,但这些量本身解释不了收益延续**。
   翻成算子语言:这是文献里少数**直接检验「日内量的模式是不是价格水平/流动性代理」并给出否定答案**的例子,
   支持 analysis.md §1.5(a) 「`day_centroid` 结构上不是代理」这条判断,但要注意:这篇测的是**收益延续**(40 日窗口),
   不是「时间重心」这个具体构造本身,只能当类比旁证,不是直接证据。[H2010]

3. **中国 A 股的开盘段由散户主导、收盘段由机构主导,且这个「谁在交易」的构成本身能预测跨期收益的符号翻转。**
   用中国 A 股做的研究发现:市场、价值、盈利能力这几个因子的贝塔溢价**隔夜为正、盘中为负**,规模与投资类因子正好相反;
   这个日夜差异在「投资者成熟度」更高的股票上更弱,作者把这个交替模式归因于**投资者构成**(clientele)而非风险补偿
   (风险解释需要日夜同号,但观测到的是异号)。
   翻成算子语言:把 `day_centroid(Amt)` 的「低(偏开盘)」读成散户主导、「高(偏收盘)」读成机构主导是有文献支撑的,
   支持把这个核心和「投资者成熟度」的代理(例如 `LogFloatCap`、换手率分桶)做**条件化交互**而不是单独使用。[JLY2023]

4. **收盘集合竞价的那部分成交量本身主要是机构 / ETF 被动再平衡驱动的,价格压力隔夜几乎完全反转。**
   对美股收盘集合竞价的研究发现:单次收盘撮合占到全天成交量的 7%+,与机构持仓 / ETF 再平衡高度相关,
   但这部分巨量成交**对价格发现的贡献很小**;收盘价相对收盘时点报价中点的偏离,平均会**隔夜完全反转**,
   约一半的反转在收盘后很快发生;且「收盘占全天成交量之比」本身能预测次日收益(负向)。
   翻成算子语言:这支持 analysis.md §1.5(a) 「核心的 alpha 在 20 日持久水平,不在当日值」这条必要性证据
   (+1.73)背后的一个可能机制 —— **当日的「重心偏收盘」很大一部分是会反转的价格压力噪声**,
   20 日中位数能把这部分噪声平掉,留下更稳定的「这只股票惯常的交易时点」信号。[BM2019]

**搜不到 / 拿不准,不用:**

- 没搜到任何论文把「成交的时间加权重心(`Σt·|Amt_t| / Σ|Amt_t|`)」当作确切的截面预测构造直接检验;
  上面四条都是**相关但不是这个具体构造**的研究(日内模式理论、收益延续、投资者构成、收盘拍卖),是类比推断,不是文献里现成的
  「时间重心预测收益」结论,这一点必须跟 PI 说清楚,不要当成直接证据。
- 没搜到专门报告「这个特征该用多长的窗口平滑、水平是否比新息更有预测力」这类**持久性比较**的论文(Q1(b)这部分没有文献证据,
  §1.5(a) 「必要性 +1.73」目前只是本组自己的付费证据,是孤证)。
- 另有一条**非学术的制度性事实**,供 PI 参考但不计入文献证据:上交所于 2018-08-06 发布规则、**自 2018-08-20 起**把股票收盘价
  改由 14:57–15:00 的收盘集合竞价产生(此前是连续竞价下最后一笔成交价);这意味着 `day_centroid` 里「收盘附近」这一段的
  微观结构在 train 窗口(2018–2021)中途发生过一次真实变化,不是文献,是交易所公告,来源见出处列表 [SSE2018](标注为「非学术来源」)。

---

## Q2 —— 分钟收益的已实现峰度(核心 B,做多低峰度)作为截面预测变量

**能摘到的处理方式:**

1. **已实现偏度负向、稳健地预测下周收益;已实现峰度正向但不稳健地预测下周收益 —— 符号与我们这里相反,必须如实报告。**
   Amaya–Christoffersen–Jacobs–Vasquez(2015,已在 r1 用过)用周频已实现矩做截面检验:买低偏度卖高偏度周超额约 19bp 且显著;
   **峰度到收益是正向关系,但不总是显著**,早期工作论文版本(2011)报告过「买高峰度卖低峰度」周超额约 16bp、t≈2.98。
   这与 analysis.md §1.5(b) 的方向(**做多低峰度**,即峰度负向预测收益)**符号相反**。
   三个可能的原因需要摆给 PI:(i)频率不同(文献是周频已实现矩,我们是分钟标准化四阶矩做日频信号后再 EMA);
   (ii)市场不同(美股 vs A 股);(iii)文献的峰度结果本身就不稳健("not always significant"),符号可能本来就不可靠。
   **这条不是用来否定核心 B,而是提醒 PI:核心 B 的方向目前只有本组的付费证据支撑,文献对"峰度"这个量本身的方向其实是模糊的**,
   比偏度弱得多。[ACJV2015]

2. **"彩票偏好"这个更大的家族里,"尾部厚/爆发力强的股票未来收益更低"是稳健结果,但度量用的是 MAX(月内最大单日收益)而不是峰度。**
   Bali–Cakici–Whitelaw(2011,NBER 工作论文 2009-03 先行)发现:按月内最大单日收益(MAX)排序,
   最低档减最高档的原始/风险调整收益差超过 1%/月,控制规模、账面市值比、动量、短期反转、流动性、**偏度**后依然稳健;
   加入 MAX 后,Ang 等(2006)的特质波动率异象那个"负向且难解释"的关系会被**吸收甚至反转**。
   翻成算子语言:这支持核心 B 的**方向**(厚尾/爆发型股票收益更低)在一个更大的、独立验证过的家族里是成立的,
   但 MAX 是"单日极值",峰度是"整体尾部形状",两者相关但不是同一个量 —— N 位可以把 `day_max`/`day_min` 类的极值量
   当作峰度的**正交对照**去测(§2.5 的"必须放对照种子"那条思路可以搬到这里)。[BCW2011]

3. **在中国市场上,把已实现的"跳跃"按正负拆开分别定价,比用一个对称的高阶矩更细。**
   Chao–Liu–Guo(2017,PLoS ONE)用中国 A 股 5 分钟数据,把已实现跳跃拆成正向、负向、符号跳跃三部分分别做 Fama-MacBeth,
   发现符号跳跃强度和连续波动率都显著定价,负向跳跃到达率单独显著(10% 水平)。
   翻成算子语言:直接支持 analysis.md §4.3 N3 的方向 —— **把 `day_kurt(Ret)` 换成"上半方差 vs 下半方差之比"或
   "正向超额矩 − 负向超额矩"这类不对称构造**,而不是只用对称的四阶矩;这篇论文没有检验"峰度",是跳跃强度,是类比,
   不是直接证据。注意:我专门查过,这篇论文**没有讨论涨跌停/一字板对高阶矩估计的污染**,也**没有把规模或流动性当控制变量**
   写进横截面回归,这两点不能当作文献支撑。[CLG2017]

4. **涨跌停(一字板)会截断观测到的收益分布,导致朴素的波动率/高阶矩估计失真,标准做法是用截断模型重建,而不是直接丢弃或直接算。**
   Adcock–Ye–Yin–Zhang(2019,Journal of the Operational Research Society)在中国 A 股上用截断 GARCH 模型处理涨跌停,
   发现传统模型对涨跌停日的拟合明显更差,截断模型给出的波动率/价格发现结论实质不同。
   翻成算子语言:`day_kurt(Ret)` 在一字板(全天一个价、分钟收益几乎全为 0)的日子上,标准化四阶矩的分母(方差)趋近 0,
   数值上会退化(呼应 §3.1 已经发现的 `div` 数值退化问题,但这次是峰度算子本身,不是外层算子);
   文献的建议是**用截断模型重建**,比直接在算子层面"跳过这天"更复杂,实现上不现实,但至少提示
   **R/E 的变体里应该检验"剔除当日振幅极小的样本后 `day_kurt` 会不会变"**,这是一个没花过评估、但文献能支撑的怀疑点。[AYYZ2019]

**搜不到 / 拿不准,不用:**

- 没搜到任何论文明确报告"已实现峰度不要平滑"或"当期值优于移动平均"这类结论(Q2(a)的后半部分);
  §1.5(b) "平滑在这里是有害的"这条目前完全是本组自己的付费证据,文献没有佐证也没有反证。
- 没搜到专门在中国市场上直接检验"已实现峰度"(不是偏度、不是跳跃)对横截面收益预测力的论文。
  搜到一篇 2023 年的《Does realized skewness predict the cross-section of Chinese stock returns?》
  (Dai, Jiang, Long, Wang, Zaremba,*Finance Research Letters* vol 58)看着很对题,但 Crossref 记录的 DOI 创建日期是
  **2023-08-25**,晚于 2023-08-08 的截止线,按规则**不用**(而且它测的也是偏度不是峰度)。
- 没搜到专门做"按规模/流动性/换手分组内标准化峰度"这类条件化处理的论文(只有 Chao-Liu-Guo 的"按正负拆开"这个不同维度的条件化)。

---

## Q3 —— F1(折叠的市值秩)/ F2(名义股价分段)与「线性中性化会残留非线性成分」这个机械事实

**能摘到的处理方式:**

1. **规模效应本身就不是沿整个市值谱线性的,几乎完全集中在微盘股一段,对中盘、大盘边际上很弱。**
   Fama–French(2008,*Journal of Finance*,"Dissecting Anomalies")用回归法重新检验规模、价值等异象,
   发现规模对收益的解释力**几乎全部来自微盘股**(约占样本只数 60%、总市值约 3%),对小盘和大盘股的边际效应很弱。
   翻成算子语言:这是规模效应"非线性 / 只在一段里起作用"的直接证据(虽然这篇测的是"微盘段",不是"按流动性再分段"),
   支持 F1/C 核心"只在最低成交额 40% 里按市值排"这种**分段读规模**的做法本身在文献里有先例,
   不是 GP 凭空发明的伪装;但要跟 PI 说清楚,这篇分段用的是市值本身,不是"流动性 × 市值"的二维交互,是类比不是直接证据。[FF2008]

2. **名义股价能预测收益,但原始股价混着两股方向相反的力,标准做法是用"拟合股价"把它纯化,而不是直接用原始股价当变量。**
   Birru–Wang("Nominal Price Illusion",*Journal of Financial Economics* 2016,vol 119,pp. 578–598)发现:
   用"拟合股价"(剔除掉能被基本面解释的那部分股价水平)而不是原始股价做排序,能找到一个干净得多的定价效应
   (价值加权四因子 alpha 约 85bp/月);**原始股价本身对未来超额收益几乎没有预测力**(两股相反的力互相抵消)。
   翻成算子语言:这**直接**支持 analysis.md §1.3 的怀疑 —— 头 3 里"把最便宜 10% 搬到 82 分位"那层
   (`cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Close)))`)能带来正必要性(+0.45),
   很可能就是在做一个粗糙版的"纯化股价"(剔掉最容易被基本面噪声污染的那一档);
   更标准的做法应该是先把 `day_open(Open)` 对 `LogFloatCap`(甚至换手率)做回归取残差,再用残差去做 `cs_first_low20` 的筛子,
   而不是像现在这样直接用原始股价。[BW2016]

3. **在中国 A 股上,低价股溢价的符号与美股相反(是正的,不是负的),这件事本身已经被独立检验过两次。**
   Zhang(2023,*International Review of Economics & Finance* vol 88,DOI 创建于 2023-07-04,在截止线之前)发现
   中国市场上"做多低价股"是一个**正向**溢价(与美股的符号相反),归因于两个市场现金流贝塔的方向不同;
   Yang–Yang(2022,*Humanities and Social Sciences Communications*,2022-04 上线)把一个低价溢价因子加进中国版
   Fama-French 模型,发现它是一个可靠的定价成分。
   翻成算子语言:F2 家族"做多便宜股"这个方向在**中国市场的独立文献**里是有支撑的(不是美股证据硬套到 A 股),
   但两篇给的机制(现金流贝塔)都和 analysis.md §1.3 给的机制("折叠/分段绕开线性中性化")不是同一个解释,
   这是一个该让 PI 知道的、还没调和的分歧:**方向对,但"为什么"可能不是我们认为的那个机制**。[ZB2023][YY2022]

4. **"线性中性化之后非线性规模成分会残留"这件事,主流风险模型文献里有一个现成的、专门的处理方式:构造一个独立的"非线性规模"因子。**
   Menchero–Orr–Wang(MSCI,"The Barra US Equity Model (USE4) Methodology Notes",2011-08)描述了风险模型里标准的
   描述量清洗流程:先用多步算法识别离群值,把"合法但过大"的观测**截尾到均值 ± 3 个标准差**(不是按百分位缩尾),
   再用"市值加权均值 + 等权标准差"把描述量标准化为均值 0、标准差 1(市值加权均值是为了让一个分散的市值加权组合在风格因子上
   暴露接近零,标准差用等权是为了不让大盘股主导尺度)。文档里明确提到 **"Non-Linear Size"因子的作用正是捕捉
   中盘股与整体市场的收益差"**(§2.2、§2.3,原文已读)。
   同系列文档 MSCI《Barra China Equity Model (CNE5) Descriptor Details》(2013-09)给出了这个因子的**确切构造**:
   **先把标准化后的规模暴露(市值对数)三次方(cube),再把这个结果对线性规模因子做(按回归加权的)正交化,
   最后再缩尾、标准化一次**(原文已读:"First, the standardized Size exposure…is cubed. The resulting factor is then
   orthogonalized to the Size factor on a regression-weighted basis. Finally, the factor is winsorized and standardized.")。
   翻成算子语言:这是业界对"线性中性化后残留的非线性规模成分该怎么处理"这个问题**现成的、专门针对中国市场**的标准答案 ——
   F1 的 `sqrt(cs_last_low40(LogFloatCap, ·))`(V 形折叠)和 Barra 的"三次方 + 对线性规模再正交化"是**同一个问题的两种不同解法**:
   都是把标准化后的规模暴露做一个**奇/偶非线性变换**再用。文献这条额外提示了 analysis.md 自己没想到的一步 ——
   **把折叠后的因子再对线性规模因子做一次显式正交化**(不只是依赖奖励的线性中性化隐式去掉),
   这应该是 R 里"折叠算子本身"那条(§2.3)该补的一个新变体。[MOW2011][MSCI2013]

**搜不到 / 拿不准,不用:**

- 没搜到专门做"规模 × 流动性"条件交互、或明确检验"非单调/U 形/V 形规模效应"的截面检验论文(只有 Fama-French(2008)的
  "规模效应集中在微盘股"这个间接支撑,和 Barra/MSCI 风险模型里现成的"Non-Linear Size"因子构造;后者是**业界方法论文献**,
  不是专门检验"规模-流动性交互"的学术论文,这个区别必须跟 PI 说清楚,不要混为一谈)。
- Hwang & Lu(常被二级来源当作"名义股价"最早的现代研究之一引用的 2008 年工作论文)搜不到任何可验证的原始出处或日期,不用;
  Fritzmeier(1936,常被当作"低价股效应"最早的出处)也只搜到二级引用,没有验证到原始文献,不用。
- "只对规模做线性中性化之后,非线性成分怎样被检测"这个更一般的统计方法论(非参数中性化、Fama-MacBeth 加平方项)
  本轮没有搜到比 r1 更多的新证据,沿用 r1 的结论(没有找到专门的方法论文献,Barra 的做法是目前能找到的最接近的现成答案)。

---

## Q4 —— 「筛选式」处理(剔掉一个尾部 / 只在一段里排序 / 把一档整块搬走)在文献里怎样被构造和评估

**能摘到的处理方式:**

1. **分组断点(带宽)的选择本身是任意的,文献里明确承认这一点,且窄断点与宽断点之间有一个"更强但更吵"的权衡。**
   Fama & French 自己在 1993 年就写过"断点的切法是任意的,我们没有搜过别的选择,也没理由认为检验结果对这个选择不敏感"
   (该原话被 Hollstein–Prokopczuk–Voigts 的海报原文引用)。Hollstein–Prokopczuk–Voigts
   ("How Robust are Empirical Factor Models to the Choice of Breakpoints?",AFA 2023 博士生海报展示,2023 年 1 月,
   美国金融学会年会)系统检验了把标准 30/70 分位断点移动后的效果,发现:**断点越靠外(越极端/越窄),因子对异象的暴露越强,
   但特质噪声也越大**("specification vs. diversification" 的权衡);**用更多条件变量做多维分组时,应该用更居中的断点**
   (因为维度越高、每个格子里的股票越少,越容易被特质噪声主导);他们给出三条操作性建议:
   (i)排序维度越高,断点应越居中;(ii)截面数据质量差(某个时点股票数少)时,断点也应更居中;
   (iii)模型越复杂(涉及的异象暴露越多),越适合用居中断点,因为复杂模型捕捉异象的能力已经足够,窄断点带来的噪声不值得。
   翻成算子语言:这**直接**回应 analysis.md §2.3 "cs_last_low40 的 40% 带宽是生成器给的,不是测出来的"这条怀疑 ——
   文献的结论是**窄带宽(10%/20%)预期 score 会更高但样本外更不稳定**,这应该写进 R 任务 #6、#7(带宽改 20%/10%)的预期里,
   不能只看 train/valid 的 score 谁更高,还要关注收窄后头 1 的换手和稳定性有没有恶化。[HPV2023]

2. **筛选式处理在"要不要买/卖"这两个阶段上,标准的省成本手艺是给进入和留仓设不同的带宽(买入门槛比持有门槛更严),而不是一刀切。**
   Novy-Marx & Velikov("A Taxonomy of Anomalies and their Trading Costs",NBER 工作论文 2014-12,后发表于
   *Review of Financial Studies* 2016,vol 29)系统检验了几十个异象的换手与交易成本,发现**"买/持区间"(buy/hold spread,
   即开仓门槛比持仓门槛更严格的不对称带宽)是最有效的省成本手段**;月度单边换手率低于 50% 的策略在算完成本后仍然显著,
   高换手的策略大多数不能。
   翻成算子语言:本组现在测的 R(§4.2)都是"一刀切"地替换 `cs_last_low40`/`cs_first_low20` 的**静态**带宽,
   文献提示了一个本组完全没试过的处理方式 —— **给同一个筛子设两个不同的带宽,一个决定新进入这一档,一个决定继续留在这一档**
   (例如"跌破最低 10% 才买入,回升到最低 25% 以上才卖出"),这应该是 R 或 N2 的一个新目标,
   直接针对"筛选式处理在纯多头实现里的换手成本"(Q4(c))。[NMV2014]

3. **缩尾的一个具体、可验证的业界惯例:截尾到均值 ± 3 个标准差,而不是按固定百分位(1%/5%/10%)。**
   同 Q3 的 Menchero–Orr–Wang(2011)USE4 方法论文档:USE4 把"合法但过大"的描述量**截尾到 3 个标准差**,
   极端到被当作数据错误的直接从估计里剔除;CNE5 的"Non-Linear Size"因子构造里,缩尾是**在三次方 + 正交化之后**的最后一步,
   不是对原始输入做缩尾。
   翻成算子语言:这回答了 Q4(b)里"缩尾该放在哪个位置、缩到多宽"——文献(至少风险模型这一支)给出的是**标准差尺度的截尾**,
   **且作用在变换后的衍生量上而不是原始叶子上**;这和本组头 5(`cs_mask_top_replace_mean_neg`,把最低 10% 整块搬到均值)
   是不同的处理(一个是"截尾压缩",一个是"错位搬走"),但提示§2.3"折叠算子本身"那条 R 测试时,
   可以额外加一个"先按 3σ 截尾、再折叠"的变体做对照,看文献这种更温和的处理会不会比 GP 找到的"整块搬走"更稳。[MOW2011][MSCI2013]

**搜不到 / 拿不准,不用:**

- 没搜到专门比较"缩尾在 1% / 5% / 10% 位置"对截面因子构造效果的论文(只有 Barra 风险模型的 3σ 截尾这个具体但维度不同的惯例 ——
  那是给**协方差矩阵估计**用的,不是直接为**收益预测**设计的,这个区别必须讲清楚,不能当成同一件事)。
- 没搜到专门量化"把一个特征限制在某个股票池内(剔除次新股、ST、低流动性)后,样本外因子衰减有多大"的学术论文;
  只搜到中文二级来源描述"常见做法是剔除 ST/*ST/退市风险警示股,次新股剔除窗口 3/6/12 个月不等",
  这些是**描述性的行业惯例**,不是可验证的学术文献结论,不能当证据用。
- "双重排序(dependent vs. independent double sort)"这个方法论差异本身,本轮只搜到 r1 没有的新旁证(`portsort` R 包文档,
  不是学术论文),没有新的、可独立核实日期的学术文献,不再单独列出处。

---

## 出处列表

**[AP1988]**
标题:A Theory of Intraday Patterns: Volume and Price Variability
作者:Anat R. Admati, Paul Pfleiderer
年-月:1988-03(*The Review of Financial Studies*, Vol. 1, No. 1, pp. 3–40)
来源:期刊(The Review of Financial Studies)
链接:作者个人学术履历页列出该文确切卷期页码(通过 WebSearch 命中其 CV/简介页独立确认)
verified: true(WebSearch 命中多个独立来源——作者所属机构简介、RePEc/IDEAS 条目——对标题、期刊、卷期、页码一致确认)

**[H2010]**
标题:Intraday Patterns in the Cross-section of Stock Returns
作者:Steven L. Heston, Robert A. Korajczyk, Ronnie Sadka
年-月:2010(*Journal of Finance*, Vol. 65, No. 4, pp. 1369–1407)
来源:期刊(Journal of Finance);工作论文版本在 arXiv(ar5iv 镜像)
链接:https://ar5iv.arxiv.org/html/1005.3535
verified: true(本轮再次独立 WebSearch 确认,与 r1 结论一致;多个来源——Kellogg 官方介绍页、arXiv 镜像——一致确认标题、作者、期刊卷期)

**[JLY2023]**
标题:Factor beta, overnight and intraday expected returns in China
作者:Zhengke Ye, Danling Jiang, Yunfeng Luo
年-月:Crossref 记录「created」日期 2023-03-12,先行工作论文版本至少 2022-08 已在流通(见下);正式发表于
*Global Finance Journal*, Vol. 56, 2023-05(文章号 100827,DOI 10.1016/j.gfj.2023.100827)
来源:期刊(Global Finance Journal);早期版本为 SSRN 工作论文(abstract_id=4138715)
链接:https://ideas.repec.org/a/eee/glofin/v56y2023ics1044028323000224.html ;
Crossref:https://api.crossref.org/works/10.1016/j.gfj.2023.100827
verified: true(WebFetch 直接查询 Crossref API 得到 DOI 创建日期 2023-03-12,早于 2023-08-08;Quantpedia 于 2022-08-26
发布的介绍文章独立确认这篇 SSRN 工作论文最晚在 2022 年 8 月已经流通;Stony Brook 大学研究门户页独立确认题目、作者、期刊、卷期)

**[BM2019]**
标题:Should We Use Closing Prices? Institutional Price Pressure at the Close(后更名为 Who Trades at the Close?
Implications for Price Discovery and Liquidity)
作者:Vincent Bogousslavsky, Dmitriy Muravyev
年-月:工作论文首版 2019-11-12(SSRN abstract_id=3485840);正式发表于 *Journal of Financial Markets*, Vol. 66, 2023-11
(DOI 10.1016/j.finmar.2023.100852,Crossref「created」日期 2023-06-24)
来源:工作论文(SSRN);后发表于期刊
链接:https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3485840 (SSRN 页面本身无法直接 WebFetch 访问,日期经
OptionMetrics 研究列表页独立确认);期刊版 Crossref:https://api.crossref.org/works/10.1016/j.finmar.2023.100852
verified: true(WebFetch 直接读取 OptionMetrics 研究列表页,明确给出工作论文发布日期 2019-11-12 与 SSRN 链接,
早于 2023-08-08;期刊版 Crossref 创建日期 2023-06-24 也早于截止线,两条路径互相独立确认)

**[ACJV2015]**
标题:Does Realized Skewness Predict the Cross-Section of Equity Returns?
作者:Diego Amaya, Peter Christoffersen, Kris Jacobs, Aurelio Vasquez
年-月:2015(*Journal of Financial Economics*, Vol. 118, pp. 135–167,DOI 10.1016/j.jfineco.2015.02.009);
早期工作论文版本 2011 年已挂出(CREATES)
来源:期刊(Journal of Financial Economics);早期工作论文版本见 CREATES
链接:https://repec.econ.au.dk/repec/creates/rp/13/rp13_41.pdf
verified: true(本轮再次独立 WebSearch 确认,与 r1 结论一致;命中期刊 DOI、CREATES 工作论文页、二级摘要,标题/作者/卷期一致;
本轮额外确认:发表版峰度结果为「正向但不总是显著」,2011 工作论文版报告过「16bp/周,t≈2.98」的峰度多空利差)

**[BCW2011]**
标题:Maxing out: Stocks as lotteries and the cross-section of expected returns
作者:Turan G. Bali, Nusret Cakici, Robert F. Whitelaw
年-月:2011(*Journal of Financial Economics*, Vol. 99, No. 2, pp. 427–446,DOI 10.1016/j.jfineco.2010.08.014);
NBER 工作论文版本 No. 14804,2009-03 先行
来源:期刊(Journal of Financial Economics);NBER 工作论文
链接:https://www.nber.org/papers/w14804.pdf ;IDEAS/RePEc:https://ideas.repec.org/a/eee/jfinec/v99y2011i2p427-446.html
verified: true(WebSearch 命中 NBER 官方工作论文页、IDEAS/RePEc 期刊条目、AlphaArchitect 二级总结,标题/作者/卷期/DOI 一致确认)

**[CLG2017]**
标题:Sign realized jump risk and the cross-section of stock returns: Evidence from China's stock market
作者:Youcong Chao, Xiaoqun Liu, Shijun Guo
年-月:2017-08-03(*PLoS ONE*, Vol. 12, No. 8, e0181990;收稿 2016-08-28,接受 2017-03-29,发表 2017-08-03,
DOI 10.1371/journal.pone.0181990)
来源:期刊(PLoS ONE)
链接:https://pmc.ncbi.nlm.nih.gov/articles/PMC5542663/
verified: true(WebFetch 直接读取 PMC 全文页面,明确给出收稿/接受/发表三个日期,发表日 2017-08-03 远早于截止线;
同时确认该文未讨论规模/流动性控制变量,也未讨论涨跌停对高频矩的污染,这两点在正文中已如实注明)

**[AYYZ2019]**
标题:Price discovery and volatility spillover with price limits in Chinese A-shares market: A truncated GARCH approach
作者:C. J. Adcock, C. Ye, S. Yin, D. Zhang
年-月:2019-10(*Journal of the Operational Research Society*, Vol. 70, No. 10, pp. 1709–1719,
DOI 10.1080/01605682.2018.1542973)
来源:期刊(Journal of the Operational Research Society,Taylor & Francis)
链接:https://ideas.repec.org/a/taf/tjorxx/v70y2019i10p1709-1719.html
verified: true(WebFetch 直接读取 IDEAS/RePEc 条目,标题/作者/卷期/页码/DOI 明确列出,年份 2019 早于截止线)

**[FF2008]**
标题:Dissecting Anomalies
作者:Eugene F. Fama, Kenneth R. French
年-月:2008-08(*The Journal of Finance*, Vol. 63, No. 4, pp. 1653–1678)
来源:期刊(The Journal of Finance)
链接:https://ideas.repec.org/a/bla/jfinan/v63y2008i4p1653-1678.html ;全文 PDF(作者个人站点镜像)
https://www.johnhcochrane.com/s/fama_french_dissecting_anomalies_JF.pdf
verified: true(WebSearch 命中 IDEAS/RePEc 条目、CFA Institute 摘要、多个大学机构镜像,标题/作者/卷期/页码一致确认;
这是极为确立的经典文献,本次独立复核而非仅凭训练记忆)

**[BW2016]**
标题:Nominal Price Illusion
作者:Justin Birru, Baolian Wang
年-月:2016(*Journal of Financial Economics*, Vol. 119, pp. 578–598,DOI 10.1016/j.jfineco.2016.01.027)
来源:期刊(Journal of Financial Economics)
链接:多个来源(EFMA 会议论文列表、Ohio State 大学 Dice Center 工作论文页、ETF.com 对该文的介绍文章)一致确认
verified: true(WebSearch 命中三个相互独立的来源——学术新闻摘要页、Dice Center 工作论文列表、Swedroe 在 ETF.com 的评论文章——
对标题、作者、期刊、卷期、页码、DOI 一致确认;发表年份 2016 本身已远早于 2023-08-08 截止线,不依赖更早的工作论文版本日期)

**[ZB2023]**
标题:Betting against low nominal prices: Evidence from China
作者:Bing Zhang
年-月:2023(*International Review of Economics & Finance*, Vol. 88, pp. 476–500,DOI 10.1016/j.iref.2023.06.017;
Crossref「created」日期 2023-07-04)
来源:期刊(International Review of Economics & Finance)
链接:https://ideas.repec.org/a/eee/reveco/v88y2023icp476-500.html ;
Crossref:https://api.crossref.org/works/10.1016/j.iref.2023.06.017
verified: true(WebFetch 直接读取 IDEAS/RePEc 条目确认标题/作者/卷期/DOI;再用 Crossref API 直接核实创建日期为
2023-07-04,早于 2023-08-08 截止线)

**[YY2022]**
标题:Asset pricing and nominal price illusion in China
作者:Pujian Yang, Liu Yang
年-月:2022-04-06 上线(*Humanities and Social Sciences Communications*, Vol. 9, No. 1, Article 1,
DOI 10.1057/s41599-022-01133-4;期刊卷期标注 2022-12)
来源:期刊(Humanities and Social Sciences Communications,Springer/Palgrave)
链接:https://ideas.repec.org/a/pal/palcom/v9y2022i1d10.1057_s41599-022-01133-4.html ;
Crossref:https://api.crossref.org/works/10.1057/s41599-022-01133-4
verified: true(WebFetch 直接读取 IDEAS/RePEc 条目确认标题/作者/DOI;再用 Crossref API 直接核实「published-online」
日期为 2022-04-06,远早于截止线)

**[MOW2011]**
标题:The Barra US Equity Model (USE4): Methodology Notes
作者:Jose Menchero, D.J. Orr, Jun Wang
年-月:2011-08(MSCI Research,"Model Insight"系列)
来源:机构研究报告(MSCI/Barra)
链接:https://www.top1000funds.com/wp-content/uploads/2011/09/USE4_Methodology_Notes_August_2011.pdf
verified: true(直接下载并用 pdftotext 读取全文第 8 页「2.2 Data Quality and Outlier Treatment」与「2.3 Style Exposures」
两节原文:离群值截尾到均值 ± 3 个标准差,描述量用「市值加权均值 + 等权标准差」标准化;第 7 页原文提到「Non-Linear Size」因子
经正交化后捕捉中盘股与整体市场的收益差;封面确认标题、作者、日期 2011 年 8 月)

**[MSCI2013]**
标题:Barra China Equity Model (CNE5): Descriptor Details
作者:MSCI Research(机构作者,未署名个人)
年-月:2013-09
来源:机构研究报告(MSCI/Barra,"Model Insight"系列)
链接:经 WebSearch 命中的第三方镜像 PDF(内容已用 pdftotext 直接读取确认)
verified: true(直接读取 PDF 第 1 页确认标题「Barra China Equity Model (CNE5) / Descriptor Details / September 2013」;
第 4 页读到「Non-linear Size」因子条目原文:"First, the standardized Size exposure (i.e., log of market cap) is cubed.
The resulting factor is then orthogonalized to the Size factor on a regression-weighted basis. Finally, the factor is
winsorized and standardized.")

**[HPV2023]**
标题:How Robust are Empirical Factor Models to the Choice of Breakpoints?
作者:Fabian Hollstein, Marcel Prokopczuk, Victoria Voigts
年-月:2023-01(AFA / ASSA 年会,"AFA PhD Student Poster Session 2023",Leibniz Universität Hannover)
来源:会议海报 / 工作论文(美国金融学会年会学生海报展示)
链接:经 WebSearch 命中的 AEA 2023 会议论文页(http://www.aeaweb.org/conference/2023/program/paper/KHr64hyz)下的海报 PDF
verified: true(直接读取海报 PDF 图像,确认标题、作者、机构(Leibniz Universität Hannover)、以及「AFA PhD Student Poster
Session 2023」字样;美国金融学会年会固定于每年 1 月与 AEA/ASSA 年会同期举行,2023 年会议日期在 2023-08-08 之前;
海报正文含完整摘要、方法、结果与三条操作性准则,原文已读)

**[NMV2014]**
标题:A Taxonomy of Anomalies and their Trading Costs
作者:Robert Novy-Marx, Mihail Velikov
年-月:NBER 工作论文 No. 20721,2014-12;正式发表于 *Review of Financial Studies*, Vol. 29, No. 1, pp. 104–147(2016),
DOI 10.1093/rfs/hhv063
来源:工作论文(NBER);后发表于期刊
链接:https://nber.org/papers/w20721
verified: true(WebFetch 直接读取 NBER 官方工作论文页,「Issue Date」字段明确显示 2014 年 12 月,远早于截止线;
期刊版信息经 IDEAS/RePEc 条目独立确认标题/作者/卷期/DOI 一致)

**[SSE2018](非学术来源,仅供 PI 参考,不计入文献证据)**
标题:上海证券交易所交易规则(2018 年修订)及收盘集合竞价相关配套业务规则公告
来源:上海证券交易所官方公告
年-月:2018-08-06 发布,2018-08-20 起施行
链接:https://www.sse.com.cn/lawandrules/sselawsrules2025/repeal/rules/c/c_20180806_10784917.shtml ;
https://www.sse.com.cn/aboutus/mediacenter/hotandd/c/c_20180806_4607055.shtml
verified: true(WebSearch 命中上交所官网公告原文,明确给出发布日期 2018-08-06 与施行日期 2018-08-20,以及
「股票收盘价改由收盘集合竞价(14:57–15:00)产生」这一条具体规则变化)
