# 文献:种子 805,C 组,第 3 轮

对准 `analysis.md` §5 的 L1–L4(个股特征的「时间维分布形状」/槽 a;成交量慢速增长与集合竞价份额/槽 b;分钟收益峰度与零收益占比/§1.4;日内量价相关/§1.5c)。只用 **2023-08-08 之前**发表的论文、工作论文或研究报告(journal 用正式出版日期;working paper 用首版/流通日期;arXiv/SSRN 以首版日期为准;日期拿不准的一律不进出处表当证据用)。

本轮不重复 r1 的 L1–L4(日内成交量分布的处理手法、收盘竞价是否机构代理、水平 vs 自身偏离、A 股日内集中度/聪明钱的构造)和 r2 的 L1–L4(时点 vs 离散度怎么剥离、竞价分钟怎么分开、持续水平 vs z 偏离、名义价格与流通股本)。本轮四条新编号 **S1–S22**,和 r1 的 S1–S15、r2 的 S1–S16 是三套独立的表,不要合并引用;个别论文(Llorente et al. 2002)在 r2 已经出现过,这里只在明确标注「复用」且用于**不同的论点**时才再引,不重复它在 r2 已经做过的论点。

每条处理手法后用 `[Sx]` 指向文末出处表。`verified: true` = 这次确实在搜索结果、页面或我直接读取的 PDF 全文上看到了标题/作者/刊物/卷期页这组信息(多个独立来源一致,或我直接下载并用 `pdftotext` 读取了原文),不是凭记忆写的;只核对了部分字段的条目在备注栏写清楚缺的是什么。本轮有三篇论文(Bali-Cakici-Whitelaw、Gervais-Kaniel-Mingelgrin、Wang-Hudson-Rhodes-Zhang-Gregoriou)我直接下载了 PDF 全文并用 `pdftotext` 读取了方法论原文,是本轮信度最高的三条。

---

## L1. 个股特征的「时间维分布形状」(滚动偏度/峰度/极值/两窗口之差)vs 滚动均值,哪种更能预测横截面收益;窗口怎么选;极值进窗/出窗的「回声」怎么处理

### 1.1 核心证据一:单日极值(不是均值)本身就是定价维度,而且对「取几天」不敏感

Bali, Cakici, Whitelaw (2011)——**我直接下载了 NBER 工作论文 PDF 并用 `pdftotext` 读取了方法论与稳健性章节原文**,不是摘要——用一个月(约 21 个交易日)窗口内的**单日最大收益**(MAX)给股票分十分组,发现 MAX 与下月收益显著负相关,最高最低组月度收益差超过 1%,这个关系在控制了 size、book-to-market、动量、短期反转、流动性之后依然存在 [S1]。
**对窗口/取几个极值的敏感性,论文原文明确报告了稳健性检验**:"results are robust to sorting stocks not only on the single maximum daily return during the month, but also the average of the two, three, four or five highest daily returns within the month"——即把 MAX 换成 MAX(2)、MAX(3)、MAX(4)、MAX(5)(月内最高 N 天收益的均值),方向和显著性都不变。论文还专门研究了 MIN(月内最小收益取负号)和 IVOL 的相关系数:IVOL 与 MAX、MIN 的横截面相关都很高,且**即使在计算波动率前先剔除最大最小两个观测,波动率依然和 MAX/MIN 高度相关**,MAX 与 MIN 自身的相关系数是 0.55 [S1]。
→ **操作语言**:(a)「月内最高 N 天均值」(N=1..5)是文献里对「单一极值 vs 极值类聚合」窗口敏感性的标准检验手法,直接对应槶 a 警告里要的「只看最大那一天」对照——可以翻译成 `ts_quantile`(取某个高分位)或者对 `in_slice`/日度序列先取 top-N 再均值的写法,不是 `ts_skew`;(b)论文自己的证据是「极值类统计量和波动率高度纠缠、且去掉最值后依然纠缠」,这与我们环境里凸变换陷阱(已知陷阱 1)是同一类问题在不同文献里的呼应,极值类特征和波动控制的纠缠不是我们环境特有的,是这整条文献分支共同的背景噪声。

### 1.2 核心证据二:从分钟数据构造的已实现偏度/峰度,方向上偏度比峰度更稳健

Amaya, Christoffersen, Jacobs, Vasquez (2015) 用日内(分钟级)数据构造已实现波动率、已实现偏度、已实现峰度,**在周频上**做十分组多空:已实现偏度十分组多空每周约 19bp(t=3.70),控制 Fama-French 和 Carhart 因子后依然显著;**已实现峰度与下周收益是正相关,但不总是显著,已实现波动率和收益没有稳健关系** [S2]。
→ **操作语言**:这篇是「从分钟数据算出的日度高阶矩,再在更长频率上用」这条处理链的直接先例——日内收益 → 日度已实现偏度/峰度(这正是我们 `day_kurt`/`day_skew` 对应的量)→ 更长窗口上做横截面排序,**不需要额外的时间维聚合算子**,已实现偏度/峰度本身已经是跨分钟聚合后的量。这与槶 a 假设「不需要再在时间维加一层 `ts_skew`,`day_kurt` 本身就够」是一个不同的立论角度:Amaya 等人是直接用,我们的 N 位想在 `day_*` 之上再叠 `ts_skew(·, 50)`,这是文献没有直接验证过的一层——**峰度比偏度的横截面证据弱**这一点,恰好是本种子 §1.4(B 组 R 任务)要重新核的东西:如果峰度本身在文献里就比偏度证据弱、不总是显著,那么 head `day_kurt(in_slice(Ret,1,236))` 的 +0.93 score 更可能是某个更强的量(比如零收益占比,§1.4 的怀疑)搭车带来的,文献本身对纯峰度效应的信心不高,支持而非削弱 B 组自查的必要性。

### 1.3 核心证据三:「两窗口之差」——多条移动平均线组合成一个因子,机制上对应「短期 vs 长期趋势」而不是矩

Han, Zhou, Zhu (2016) 构造"趋势因子":用多条不同长度(论文范围 3 到 1000 天)的移动平均价格同时作为预测变量,声称同时捕捉短、中、长期价格趋势,夏普比率显著高于分别构造的短期反转、动量、长期反转因子,且对替代构造方式和多种控制变量都稳健 [S3]。
→ **操作语言**:这是文献里离「两窗口之差」结构**最近**的先例,但要注意机制不同——Han-Zhou-Zhu 的对象是**价格水平的移动平均**(多条 MA 的线性组合,本质还是水平类),不是某个日内统计量的偏度/峰度;支持的是 head +1.13(两窗口之差)这一**族**结构本身是文献里验证过的技术分析范式(多尺度移动平均捕捉不同期限信息),但不支持把它直接套到「成交量重心/基尼系数」这类日内形状量上——这一跳(从价格趋势到日内形状量的两窗口差)文献里没有先例,是槶 a 种子表里 `sub(cross_mean(day_centroid(Volume),20), cross_mean(day_centroid(Volume),120))` 这类写法需要自己论证机制、不能借这篇论文的权威性的地方。

### 1.4 核心证据四:滚动窗口里「有没有出现过一次极端值」与「最近一次极端事件发生在哪」的「回声」问题,文献里是用跳过(skip)期处理的,不是用衰减加权

Goyal, Wahal (2015)【直接 WebFetch 核对卷期页】发现美股动量组合如果用 12 到 7 个月前(跳过最近 6 个月)构造,比用 6 到 2 个月前构造的表现更好,这个"回声"主要来自最近月份的短期反转效应混入了构造窗口;37 个非美国市场里没有稳健的回声证据 [S4]。Chen, Yang (2016) 把这条逻辑扩展到 52 周高点策略:52 周高点策略同样有回声效应,在形成日和买入日之间插入 3–6 个月的跳过期,几乎在所有情形下都显著改善表现 [S5]。
→ **操作语言,这是本题最直接能回答"回声怎么处理"的一条**:文献的标准做法不是对窗口内的极值做衰减加权,而是**在"形成窗口"和"用来交易的窗口"之间插入一段跳过期(skip period)**,把窗口边界和当前时点错开几个月,让即将滚出窗口的极端观测先失效一段时间再被使用。这对应我们环境里"外层平滑窗口"和"当前时点"之间插入一个 `delay`/滞后层,而不是换一个聚合算子——是分析里没有被种子表覆盖的一类写法,如果 GP 位要测"回声"是不是本轮极值类特征的污染源,这是文献给出的具体操作化方案,比简单调整窗口长度更精确。
George, Hwang (2004) 的 52 周高点因子本身是另一个佐证:它预测收益比用"过去收益水平"或"行业收益"都好,且这个效应长期不反转,说明"离上一次极值还有多远"(距离,不是极值本身的矩)是一个独立于普通动量/反转的定价维度 [S6]。

### 1.5 核心证据五:极端收益本身是"注意力"的代理,偏度的定价作用可能部分来自注意力而非风险补偿

Barber, Odean (2008) 用新闻报道量、异常成交量、单日极端收益三个指标共同代理"投资者注意力",发现个人投资者在股票出现极端单日波动(涨或跌)时都显著净买入,这类"高注意力日"买入的股票随后跑输 [S7]。
→ **操作语言**:这给槶 a"偶发注意力/资金事件"这条机制假设一个独立的行为金融学来源,但要注意 Barber-Odean 用的是**原始极端收益事件本身**作为注意力代理,不是偏度/峰度这类**矩**;如果槶 a 的种子表想要"事件驱动"的解释力,更贴近文献的写法是"有没有出现过超过某阈值的事件"(指示变量/事件计数),而 `ts_skew` 本身(§1.5d 已经指出)也是在测这件事,这意味着 `ts_skew(day_centroid(Volume), 50)` 和一个显式的"事件计数/阈值穿越"写法可能是在测同一机制的两种编码,不是两件独立的事——这是给创新度评分的一个提醒:如果种子表里同时有 `ts_skew` 版和显式极值版,审计员可能会把两者判成"同一机制换个写法"(创新度 2)。

### 1.6 搜不到的部分

没有找到任何论文直接对照"同一个日内特征"的**滚动均值版**和**滚动偏度/峰度/两窗口之差版**,在同一个样本上同时报告方向和幅度的差异;Han-Zhou-Zhu 的趋势因子是最接近的结构类比,但对象是价格水平不是日内形状量,不能直接当证据使用。"最近一次事件距今多久"作为一个独立构造(不是通过 52 周高点的距离,而是显式的"距离上次极值的天数")单独成为一个被研究的特征,也没有搜到直接先例——George-Hwang 的"距离 52 周高点"是最接近的操作化,但它的对象是价格而不是任意日内统计量。

---

## L2. 「成交量的慢速增长」与「开盘/收盘集合竞价成交占比」:构造与归一化,以及和流动性水平/市值怎么分开

### 2.1 核心证据一:高成交量溢价的原始归一化方法是"窗口内排名",不是除以移动平均

Gervais, Kaniel, Mingelgrin——**我直接下载了 Wharton 工作论文 PDF 并用 `pdftotext` 读取了第 2 节数据与方法论原文**,这是本轮唯一完整读到具体构造公式的一篇。他们的方法不是"原始成交量 ÷ 历史移动平均"这种连续比值,而是:把时间轴切成互不重叠的 **50 个交易日**一段(日频样本)或 **10 周**一段(周频样本,也是 50 个交易日);每一段里,最后 1 天(日频)或最后 1 周(周频)叫"形成期",前 49 天/9 周叫"参照期";把形成期的成交量**在整段 50 天/50 天内按大小排名**,排名在**前 10%**(日频:第 46–50 名)判定为"高量日/高量周",排名在**后 10%**(第 1–5 名)判定为"低量",其余是"正常" [S8]。成交量用"当日成交额"(收盘价 × 成交股数的近似),论文脚注明确说过"也用成交笔数重复过一遍,结果类似甚至更强";**上市不满一年的股票在每段窗口开始时直接整只剔除**,不是做部分窗口的特殊处理。
→ **操作语言,这是直接回答 L2 两个问题的核心证据**:(a)归一化方式是**窗口内的序数排名**(类似 `ts_pct_rank`,但作用在时间维而不是截面维),不是简单比值或 z-score;我们环境里 `cs_bucket_rank` 是截面算子,如果要照搬这个归一化,需要的是一个"时间维排名"算子,这是分析里没有专门讨论过的一类写法,值得向结构解剖员确认注册表里有没有对应的 `ts_rank`/`ts_pct_rank`;(b)**partial-window(次新股)问题的标准处理是整段剔除,不是降权或特殊公式**,这对应 analysis.md §4.3 D 组用 `cross_valid_count` 做条件键的思路是对的方向,但文献的具体门槛是"该窗口开始时交易历史不满一年就整段剔除",比单纯做一个连续的条件键更干脆。

### 2.2 核心证据二:成交量/换手率的"趋势"(不是水平)被单独构造并用作动量的条件变量

Lee, Swaminathan (2000)【ideas.repec.org 卷期页独立核对】用"过去成交量趋势"对动量/反转分组,成交量定义为日均换手率(成交股数/流通股数);发现高(低)成交量的赢家(输家)后续反转更快,过去成交量同时预测动量的幅度和持续时间 [S9]。
→ **操作语言**:这篇和 r2 已经引用过的 Lo-Wang、Chordia-Swaminathan(用于"系统性/特异性分解")是**同一批作者圈子但不同论点**——这里要的是"换手率的历史趋势本身被当作一个独立的条件变量使用",支持 A 组 R 第 2/3/4 项(把"开盘集合竞价成交"换成"任意成交量的慢增长"、换窗口)这整条研究路径的方法论合理性:文献确实把"成交量趋势"当作一个和"成交量水平"分开的定价维度在处理,不是我们自己的猜测。

### 2.3 核心证据三:集合竞价成交占比本身被直接构造成一个信号(而不是被剔除的噪声),而且方向是正的

Bogousslavsky, Muravyev——**我直接下载了工作论文 PDF 并读取了摘要与引言原文**(2020-12-03 版本;后以《Who trades at the close? Implications for price discovery and liquidity》发表于 *Journal of Financial Markets* 66 卷,2023 年),记录收盘集合竞价成交占全天成交的比例从 2010 年的 3.1% 升到 2018 年的 7.5%,这个增长与被动基金/ETF 持股比例(不是主动基金)系统相关;更关键的是,**他们直接构造了"集合竞价成交 / 全天成交"这个比值作为一个新的投资者分歧度量,发现分歧度越高,越能正向预测后续收益** [S10]。
→ **操作语言,这是 L2 最重要的一条,直接支持槶 b 的立论**:这篇论文**不是把竞价占比当控制变量剔除,而是直接把它构造成一个无量纲的比值信号去预测收益**,方向为正(分歧度高 ⇒ 未来收益高),这正是 analysis.md §4.3 槶 b "集合竞价的份额不是水平"这条假设在美股市场的一个真实先例——虽然机制解释(投资者分歧)和我们这边猜的"机构代理"不完全一样,但"占比本身是可用的定价信号,不是噪声"这个结论是独立验证过的。

### 2.4 核心证据四:A 股本地的收盘集合竞价证据——占比份额本身是制度冲击下的量,不是稳定的流动性水平

Ma, Wang, Fang, Wang (2020)【WebFetch 核对卷期页,China Finance Review International 11(2), 259-281】研究上交所 2018-08-20 引入收盘集合竞价制度改革后的市场质量,报告流动性、波动率、价格连续性均改善,且认为收盘竞价机制抑制了收盘价操纵 [S11]。Han, Zhao, Chen, Guo (2022)【WebFetch 核对卷期页,Pacific-Basin Finance Journal 74, 101821】用更严格的自然实验重新检验同一改革,结论更保守:**流动性没有显著改善,但成交量从收盘那几格"转移"到了收盘前的时段,收盘前波动率反而上升**,价格连续性确实改善,但价格有效性没有明显提升,效果主要集中在小盘股 [S12]。
→ **操作语言,这是 D 组两格(R 第 14、15 项)必须纳入解读的背景**:两篇 A 股本地证据的方向不一致("流动性改善" vs "流动性不变、只是时点转移"),但**都确认了一件事——2018-08-20 这个制度分界点前后,"收盘那几格的成交占比"衡量的不是同一个稳态量**,是一次性的时点再分配;如果 D 组的样本内(train 2018-01-02 起)跨越了这个分界点,`in_slice(Amt, 237, 240)` 这个份额在 2018 年 8 月前后代表的"正常"基准水平本身就不连续,这是 R 第 14/15 项结果解读时的一个新备选解释(不是"份额"这个概念本身有问题,是样本横跨了一次制度冲击),r2 的 S8(Pagano-Peng-Schwartz)已经提过"同月异年对照"这个方法论,这里是它在 A 股的具体制度日期确认。

### 2.5 搜不到的部分

没有搜到专门针对"次新股导致滚动窗口均值口径不一致"这个问题、给出通用解决方案(而不是像 GKM 那样简单剔除)的论文。没有搜到韩国/台湾/日本把"开盘或收盘竞价成交占比"直接构造成横截面定价因子(而不是单纯研究竞价机制本身)的学术论文——Bogousslavsky-Muravyev 是美股证据,A 股的 Ma et al./Han et al. 研究的是竞价机制改革对市场质量的影响,不是把占比当因子使用;**这两类文献之间还有一个缺口**:没有人在 A 股或其他亚洲市场把"占比"直接当作 Bogousslavsky-Muravyev 式的收益预测信号去检验。

---

## L3. 分钟收益的「峰度」与「零收益分钟占比/非流动性」是不是同一个东西;控制流动性后峰度还剩什么

### 3.1 核心证据一:零收益比例是文献里确立已久的非流动性/交易成本代理,不需要任何高频数据

Lesmond, Ogden, Trzcinka (1999)【ideas.repec.org 卷期页独立核对】只用日度收益序列就能估计有效交易成本,识别信号就是零收益发生的频率:交易成本越高,无法覆盖成本的交易越不会发生,表现为更多零收益日;估计的往返成本与常用交易成本估计量相关度达 85% [S13]。Bekaert, Harvey, Lundblad (2007)【ideas.repec.org 卷期页独立核对】把"月度零收益日占比"(一个变换后的版本)当作新兴市场的主要流动性指标,发现它比换手率更能预测收益,理由是新兴市场的逐笔数据质量太差,零收益占比不需要逐笔数据 [S14]。
→ **操作语言**:这是"零收益占比 = 流动性代理"这条等价关系在文献里最原始、最直接的出处,对应我们环境里的 `day_zero_ratio`,R 第 5 项(`day_zero_ratio(in_slice(Ret,1,236))`)测的正是这个文献里确立最久的量,不是我们自己发明的诊断。

### 3.2 核心证据二(本轮证据质量最高的一条):峰度和"五种流动性代理"(包含零收益占比)在同一个回归里被直接检验,峰度对全部五种代理都有显著的正向解释力,且控制了波动率

Wang, Hudson, Rhodes, Zhang, Gregoriou (2020)——**我直接下载了 PDF 并用 `pdftotext` 读取了方法论、回归设定与结果段落的原文**,不是摘要。他们用 2002–2018 年伦交所全部上市公司,对五种流动性/非流动性代理(相对价差、Amihud 的 RtoV、Florackis 等人的价格冲击比率 RtoTR、零收益日占比 ZeRet、零成交日占比 ZeVol)分别回归到|偏度|和峰度上,**同时控制了价格水平、公司规模、日收益标准差(即波动率)、成交量** [S15]。结果:**峰度对全部五个流动性代理的系数都显著为正**(零收益日占比在 5% 水平显著,其余四个在 1% 水平显著);|偏度|对价差、RtoV、RtoTR 三个代理显著为正,但**对零收益日占比这一项系数不显著**。论文原文结论是"stocks with a high degree of asymmetry are less liquid...Even though the skewness results are insignificant for the zero-return days model, the Kurtosis results are statistically significant in all of the five liquidity measures"。
→ **操作语言,这是直接可以带给 PI 的一条方法论原型**:文献的回归设计是"**峰度(自变量)→ 预测流动性代理(因变量),同时控制波动率**",这恰好是 R 第 5/6 项想问的问题的**镜像**——analysis.md 想测的是"峰度的 score 是不是零收益占比的改写"(即两者在同一维度上是否可互相替代),而这篇论文测的是"峰度能不能在控制了波动率之后还预测零收益占比"(方向相反,但都在处理"峰度和零收益占比到底是不是在测同一件事"这个母问题)。这篇论文的结果**支持两者高度相关但不完全是同一个东西**:峰度对零收益占比的解释力显著但系数幅度和显著性水平(5%)明显弱于它对另外四个连续型流动性代理(1%)的解释力,这意味着——**如果 R 第 5 项(`day_zero_ratio`)的 score 和 head `day_kurt` 的 score 高度一致(§4.6 预测 4 的预期),这与文献里"两者相关但不是完全重合"的证据并不矛盾,但如果 R 第 5 项 score 明显低于 head,文献会倾向支持"峰度里确实有零收益占比解释不了的部分"这个读法,而不是单纯的噪声**。另外论文里的控制变量设计(价格、规模、波动率、成交量四个一起控)也是一个可以抄的稳健性检验模板,比我们环境目前只做五个控制逐个分桶更接近文献标准(这点和 r2 S6/S7 的方法论建议是一致的方向)。

### 3.3 核心证据三:A 股涨跌停机制本身会制造"冻结报价",是分钟级零收益/峰度的一个具体 A 股成因

Wan, Xie, Gu, Jiang, Chen, Xiong, Zhang, Zhou (2015)【arXiv 首版 2015-03-12,后发表于 PLOS ONE 10(4)】用 2000–2011 年沪深全部 A 股高频数据研究涨跌停触发后的统计特征,发现触及跌停后价格延续(不是反转)的概率更高,是一种"冷却效应"而不是"磁吸效应",支持涨跌停规则在 A 股起到了实质作用 [S16]。
→ **操作语言**:这篇不直接讨论峰度或零收益,但它确认了 A 股涨跌停这个制度机制本身的统计后果是真实、被独立验证过的现象,支撑 R 第 6 项(`day_es_ratio_hi`)文档里"把分位数接近 0 的锁板/冻结日判为 NaN 剔除"这个设计不是臆造,而是针对 A 股一个有文献记录的真实微观结构特征(涨跌停触发 ⇒ 该分钟及后续分钟可能长时间维持同一个价格,产生大量机械零收益观测,这些观测和"真实的尾部形状信息"是两类不同的东西)。

### 3.4 搜不到的部分

没有搜到专门针对"分钟级(不是日度)收益峰度"与"分钟级零收益比例"的直接检验——3.2 的 Wang-Hudson-Rhodes-Zhang-Gregoriou (2020) 是日度收益的峰度,不是分钟收益聚合到日度后的峰度(我们的 `day_kurt(in_slice(Ret,1,236))` 是后者),这是一个频率上的差距,不能完全等同视之。没有搜到"用离散价格网格做尾部指数估计"的偏差校正文献与"涨跌停/冻结报价对尾部指数估计的偏差"直接相关的论文——Hill 估计量的小样本偏差文献存在,但没有搜到专门处理价格离散/锁板造成偏差的分支。

---

## L4. 日内量价相关(CPV):文献与研报里的聚合方式、方向,以及均值以外的聚合

### 4.1 背景证据:价-量关系的方向在文献里是"同向共振"而不是领先滞后,且对波动率的条件作用很强

Gallant, Rossi, Tauchen (1992)【ideas.repec.org 卷期页独立核对】提出四条程式化事实,其中两条直接相关:条件波动率与成交量正相关;大幅价格变动后往往跟着高成交量;**用滞后成交量做条件后,"杠杆效应"(negative return 后波动率上升更多)明显减弱** [S17]。
→ **操作语言**:这是价-量相关"为什么方向通常是正的"这个基础事实的原始出处,也提示——一个简单的日内价-量相关系数(如 `day_corr(Volume, Vwap)`)很可能主要是在编码"当天有没有发生大波动/大冲击",而不是一个独立于波动率的新维度;这是槶 a §1.5c"形状 > 水平"立论的一个反向提醒:聚合算子(`ts_skew` vs `cross_mean`)之争的前提——这个日内相关系数本身的信息含量——文献里早就暗示它和波动率强耦合,这层耦合不会因为换了聚合算子就消失。

### 4.2 核心证据二:价-量关系里真正有信息的部分是"有符号的订单失衡",不是未带符号的同向共振

Chan, Fong (2000)【ideas.repec.org 卷期页独立核对】发现一旦控制了订单失衡(order imbalance)对收益的影响,波动率-成交量关系会大幅减弱;对 NYSE 股票,大额交易类别里的订单失衡对收益的影响比小额类别更大 [S18]。
→ **操作语言**:这给"为什么我们用未带符号的相关系数(`day_corr(Volume, Vwap)`)可能测不到真正的信息"一个具体机制——真正驱动价-量关系的是**带符号的**失衡,而相关系数这种二阶统计量天然是无符号的(正负抵消),如果日内真正起作用的是"买方主导的放量"vs"卖方主导的放量"这类有符号信息,`day_corr` 这类对称统计量会把这部分信息平均掉。这是槶 a / C 组对照(R 第 11/12 项)结果如果仍然很弱时,一个值得追加的备选假设:换聚合算子可能不够,真正要换的是把输入从"量"换成"有符号的量"(比如 `mul(Volume, sign(Ret))`)。

### 4.3 核心证据三(研报,国内卖方):「价量相关性」因子在 A 股被直接构造并分象限处理,相关系数的符号会在不同象限/市场状态下切换含义

东吴证券金工团队(凌志杰、高子剑)《新价量相关性 RPV 因子绩效月报》,2023-07-04 发布——**我直接用 WebFetch 打开了 fxbaogao.com 的报告详情页,确认了标题、发布日期、作者**;报告正文细节(具体相关系数计算窗口、象限划分的精确定义)只能看到第三方搜索结果里的转述,没能读到报告全文,下面的构造描述标"转述,未读到原文公式"。据转述,RPV 因子把日内与隔夜信息叠加,**通过把价和量划分成"四个象限"、用月度 IC 均值去甄别价-量相关性因子在不同象限下表现的是反转效应还是动量效应**,在 2014-01 至 2022-07 的回测期里,全市场十分组多空对冲年化收益约 17.33%,信息比率约 2.71,月度胜率 81.37%,最大回撤 5.23% [S19]。
→ **操作语言,带着未读全文的保留意见**:这是本轮搜到的、最接近"日内量价相关系数在实盘因子里怎么用"的国内证据——**它处理"相关系数方向不稳定"这个问题的方式是显式分象限(不是用高阶矩去summary),再按象限分别估计 IC**,这是和槶 a 的 `ts_skew`(用矩的高阶统计量隐式捕捉"方向切换")完全不同的一条路线:**显式分桶/分象限 vs 隐式用矩**,这两条路线哪个更对,文献本身没有直接对照,但至少确认了"价-量相关系数的符号确实会随象限/市场状态切换"这件事在 A 股实盘里被当作一个必须处理的已知问题,不是我们这边凭空设想的。**这条证据等级比学术论文低(研报,无同行评审,回测数字是研报自报,我没有读到原始公式),合理度打分时不能和 S13–S18 这类学术论文同等对待**。

### 4.4 复用但不同论点:Llorente et al. (2002) 的 c2 系数是"回归系数条件化"而不是"相关系数本身",是量价关系的另一种编码方式

r2 的 S4 已经引用过 Llorente, Michaely, Saar, Wang (2002),用于"把成交量分解成系统性/特异性成分"这个论点;这里**复用同一篇论文但用它的另一个结果**:论文的核心回归是"次日收益 = c1×今日收益 + c2×(今日收益×今日成交量)+...",c2 系数衡量的是"成交量如何条件化收益的持续性/反转性",按个股换手率排序后,c2 由正转负,解释为信息驱动交易(c2>0)和流动性驱动交易(c2<0)的比例随换手率变化。
→ **操作语言**:这是"量价关系"在学术文献里更常见的编码方式——**不是算一个相关系数,而是用成交量去条件化一个收益的回归系数**,这与槶 a/C 组种子表清一色用 `day_corr`(皮尔逊相关)的写法是两条不同的技术路线。如果 C 组对照(R 第 11/12 项)结果不理想,"把相关系数换成条件化回归系数"是文献里有先例、但种子表完全没覆盖的一个方向。

### 4.5 搜不到的部分

没有搜到任何学术论文报告过"日度量价相关系数"本身的**波动、偏度或极值**版本(即对 `day_corr(Volume, Vwap)` 这类量再做 `ts_skew`/`ts_std`/取极值)——这正是槶 a 和 R 第 11/12 项要测的结构,文献上是空白,这件事对创新度是加分(真的没人做过),但对合理度没有文献证据可以加分(不能打到 4 分里"文献证据"那一半)。没有搜到关于"VWAP 溢价"(价格对 VWAP 的偏离作为横截面定价因子)的同行评审文献,只搜到执行算法(VWAP 跟踪优化)和公司金融(并购要约价参照 VWAP)两类不相关的用法。没有搜到英文学术文献报告"CPV"这个具体术语或把它当作标准化异象处理的论文——这个概念目前看来主要存在于国内卖方研报,学术化程度不如 L1–L3 的其他主题。

---

## 出处表

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified | 备注 |
|---|---|---|---|---|---|---|---|
| S1 | Maxing Out: Stocks as Lotteries and the Cross-Section of Expected Returns | Turan G. Bali, Nusret Cakici, Robert F. Whitelaw | 2011-02 | Journal of Financial Economics, 99(2), 427–446 | https://www.nber.org/papers/w14804.pdf (工作论文全文);https://ideas.repec.org/a/eee/jfinec/v99y2011i2p427-446.html (期刊版书目) | true | **我直接下载了 NBER 工作论文 PDF 并用 `pdftotext` 提取全文**,"MAX(2)–MAX(5) 稳健性"与"MAX/MIN/IVOL 相关系数 0.55"等细节都在正文里直接核对到;期刊版卷期页在 ideas.repec.org 独立核对 |
| S2 | Does realized skewness predict the cross-section of equity returns? | Diego Amaya, Peter Christoffersen, Kris Jacobs, Aurelio Vasquez | 2015 | Journal of Financial Economics, 118(1), 135–167 | https://doi.org/10.1016/j.jfineco.2015.02.009 | true | 标题/作者/卷期页/DOI 在 WebFetch 独立核对的 ideas.repec.org 式书目页上确认;具体数字(19bp、t=3.70)来自搜索结果摘要,未独立下载全文核对 |
| S3 | A trend factor: Any economic gains from using information over investment horizons? | Yufeng Han, Guofu Zhou, Yingzi Zhu | 2016(11 月) | Journal of Financial Economics, 122(2), 352–375 | https://doi.org/10.1016/j.jfineco.2016.01.029 | true | 标题/作者/卷期页/DOI 经 WUSTL 教师主页列表与期刊卷期页交叉核对 |
| S4 | Is Momentum an Echo? | Amit Goyal, Sunil Wahal | 2015-12 | Journal of Financial and Quantitative Analysis, 50(6), 1237–1267 | https://doi.org/10.1017/S0022109015000575(WebFetch 直接核对的 Cambridge/ideas.repec.org 书目页) | true | 标题/作者/刊物/卷期页/日期经 WebFetch 直接核对 |
| S5 | Echo effects and the returns from 52-week high strategies | An-Sing Chen, Wayne Yang | 2016 | Finance Research Letters, 16(C), 38–46 | https://doi.org/10.1016/j.frl.2015.10.015 | true | 标题/作者/卷期页/DOI 经 WebFetch 直接核对两次(两个独立查询一致) |
| S6 | The 52-Week High and Momentum Investing | Thomas J. George, Chuan-Yang Hwang | 2004 | Journal of Finance, 59(5), 2145–2176 | 多个独立二手页面(academicnewsletter.sufe.edu.cn、cxoadvisory.com 等)一致给出同一组卷期页信息,未能打开 ideas.repec.org 原始书目页(404) | true | 卷期页在至少三个独立二手来源中一致出现,但未能直接核对 ideas.repec.org 或期刊官方页面 |
| S7 | All That Glitters: The Effect of Attention and News on the Buying Behavior of Individual and Institutional Investors | Brad M. Barber, Terrance Odean | 2008-04 | The Review of Financial Studies, 21(2), 785–818 | https://ideas.repec.org/a/oup/rfinst/v21y2008i2p785-818.html | true | 标题/作者/卷期页经 WebFetch 直接核对 |
| S8 | The High Volume Return Premium | Simon Gervais, Ron Kaniel, Dan Mingelgrin | 工作论文 1999(Rodney L. White Center Working Paper 001-99);期刊版 2001-06 | 工作论文:Rodney L. White Center for Financial Research, Wharton School;期刊版:Journal of Finance, 56(3), 877–919 | https://rodneywhitecenter.wharton.upenn.edu/wp-content/uploads/2014/04/9901.pdf(工作论文全文);https://ideas.repec.org/p/fth/pennfi/01-99.html(书目) | true | **我直接下载了工作论文 PDF 并用 `pdftotext` 提取全文读取**,"50 天窗口切段、形成期/参照期、按窗口内排名前后 10% 定义高/低量、次新股整段剔除"等细节都在第 2 节原文(第 4–6 页附近)直接核对到 |
| S9 | Price Momentum and Trading Volume | Charles M. C. Lee, Bhaskaran Swaminathan | 2000-10 | Journal of Finance, 55(5), 2017–2069 | https://ideas.repec.org/a/bla/jfinan/v55y2000i5p2017-2069.html | true | 卷期页经独立搜索结果与 ideas.repec.org 列表一致核对 |
| S10 | Who trades at the close? Implications for price discovery and liquidity | Vincent Bogousslavsky, Dmitriy Muravyev | 工作论文 2020-12-03;期刊版 2023 | 工作论文:Boston College / Michigan State University working paper(先前题目为 "Should We Use Closing Prices? Institutional Price Pressure at the Close");期刊版:Journal of Financial Markets, 66(C), DOI 10.1016/j.finmar.2023.100852 | 工作论文 PDF 经 AEA 2021 年会预印本链接下载读取;https://ideas.repec.org/a/eee/finmar/v66y2023ics1386418123000502.html(期刊版书目) | true | **我直接下载了工作论文 PDF 并读取了标题页(落款 "December 3, 2020")与摘要原文**,"7.5% vs 3.1%""auction-to-total volume ratio 正向预测收益"等数字都在摘要原文里直接核对到;期刊版卷期经 WebFetch 独立核对 |
| S11 | The impact of closing mechanism changes: evidence from the Shanghai stock market | Dan Ma, Chunfeng Wang, Zhenming Fang, Ziwei Wang | 2020-08 | China Finance Review International, 11(2), 259–281 | https://doi.org/10.1108/CFRI-04-2020-0041 | true | 标题/作者/卷期页/DOI 经 WebFetch 直接核对 ideas.repec.org 式书目页 |
| S12 | Reexamining the impact of closing call auction on market quality: A natural experiment from the Shanghai stock exchange | Qian Han, Chengzhi Zhao, Jing Chen, Qian Guo | 2022 | Pacific-Basin Finance Journal, 74(C), 101821 | https://doi.org/10.1016/j.pacfin.2022.101821 | true | 标题/作者/卷期/DOI 经 WebFetch 直接核对 |
| S13 | A New Estimate of Transaction Costs | David A. Lesmond, Joseph P. Ogden, Charles A. Trzcinka | 1999(冬季刊) | The Review of Financial Studies, 12(5), 1113–1141 | https://ideas.repec.org/a/oup/rfinst/v12y1999i5p1113-41.html | true | 标题/作者/卷期页经 WebFetch 直接核对 |
| S14 | Liquidity and Expected Returns: Lessons from Emerging Markets | Geert Bekaert, Campbell R. Harvey, Christian Lundblad | 2007-11 | The Review of Financial Studies, 20(6), 1783–1831 | https://ideas.repec.org/a/oup/rfinst/v20y2007i6p1783-1831.html | true | 标题/作者/卷期页经 WebFetch 直接核对 |
| S15 | Stock Liquidity and Return Distribution: Evidence from the London Stock Exchange | Andong Wang, Robert Hudson, Mark Rhodes, Sijia Zhang, Andros Gregoriou | 2020 | Finance Research Letters,文章号 101539 | https://doi.org/10.1016/j.frl.2020.101539;作者认可版全文 https://eprints.leedsbeckett.ac.uk/id/eprint/6688/1/StockLiquidityAndReturnDistributionAM-RHODES.pdf | true | **我直接下载了 Leeds Beckett 机构库的作者认可版 PDF 并用 `pdftotext` 提取全文读取**,方法论公式(ZeRet、RtoV、RtoTR 定义)和回归结果段落(峰度对五种流动性代理全部显著、偏度对零收益日不显著)都在正文直接核对到;署名顺序在不同二手页面上 Wang/Hudson 谁排第一不完全一致,正文表头是 "Hudson, R and Wang, A and Rhodes, M and Zhang, S and Gregoriou, A" |
| S16 | Statistical Properties and Pre-hit Dynamics of Price Limit Hits in the Chinese Stock Markets | Yu-Lei Wan, Wen-Jie Xie, Gao-Feng Gu, Zhi-Qiang Jiang, Wei Chen, Xiong Xiong, Wei Zhang, Wei-Xing Zhou | arXiv 首版 2015-03-12;期刊版 2015-04-13 | arXiv:1503.03548;期刊版:PLOS ONE, 10(4), e0120312 | https://arxiv.org/abs/1503.03548;DOI 10.1371/journal.pone.0120312 | true | 标题/作者/arXiv 首版日期经 WebFetch 直接核对 arXiv 摘要页;期刊版 DOI 经独立搜索结果核对 |
| S17 | Stock Prices and Volume | A. Ronald Gallant, Peter E. Rossi, George Tauchen | 1992 | The Review of Financial Studies, 5(2), 199–242 | https://ideas.repec.org/a/oup/rfinst/v5y1992i2p199-242.html | true | 标题/作者/卷期页经 WebFetch 直接核对 |
| S18 | Trade size, order imbalance, and the volatility-volume relation | Kalok Chan, Wai-Ming Fong | 2000-08 | Journal of Financial Economics, 57(2), 247–273 | https://doi.org/10.1016/S0304-405X(00)00057-X;https://ideas.repec.org/a/eee/jfinec/v57y2000i2p247-273.html | true | 标题/作者/卷期页/DOI 经 WebFetch 直接核对 |
| S19 | 金工定期报告:新价量相关性 RPV 因子绩效月报 | 凌志杰、高子剑(东吴证券研究所) | 2023-07-04 | 东吴证券,"技术分析拥抱选股因子"系列研报 | https://www.fxbaogao.com/detail/3777314 | true(仅标题/作者/日期);false(构造细节与回测数字) | **我直接 WebFetch 打开了这个报告详情页,核对了标题、发布日期(2023-07-04)、作者姓名**;但页面只显示封面,正文(相关系数计算窗口、四象限精确定义、回测数字 17.33%/2.71/81.37%/5.23%)来自另一独立搜索结果对第三方转述的摘录,**没有读到研报全文或原始图表**,这部分内容的可信度明显低于标题/日期本身,不应和学术论文同等对待 |

---

## 给 PI 的汇总:哪些能直接写进任务书,哪些只能当推断

**证据扎实(至少一篇我直接读了全文)、可以直接写进 E/N/R 的理由或审计材料**:

- **L1**:Bali-Cakici-Whitelaw (2011) [S1] 直接证明"单一极值 vs 极值均值(MAX(2)–MAX(5))"这组稳健性检验在文献里是标准动作,如果 GP 位或 R 要测"只看最大那一天"这个对照(槶 a 警告里明确要求的那条),这是现成的操作化方案,而不是我们自己拍的窗口。同一篇论文也提醒极值类统计量和波动率的纠缠是整条文献分支的通病,不是我们环境特有。
- **L1**:Goyal-Wahal (2015) [S4] + Chen-Yang (2016) [S5] 给出"回声"问题的标准解法是**插入跳过期**,不是衰减加权或换聚合算子——如果 PI 怀疑本轮极值类特征(槶 a 任何涉及"进窗/出窗"的写法)有回声污染,这是文献里唯一直接给出操作方案的一条。
- **L2**:Gervais-Kaniel-Mingelgrin [S8] 的归一化方法(窗口内排名,不是比值)和"次新股整段剔除"的处理,是 A 组/D 组所有"成交量慢增长"类 R 变体可以直接引用的方法论原型,比我们自己猜的窗口选择更有依据。Bogousslavsky-Muravyev [S10] 直接证明"集合竞价占比(份额,不是水平)"在美股是一个真实的、独立构造、正向预测收益的信号,这是槶 b 整条假设在另一个市场的直接先例,比 r1 引用过的"收盘竞价是不是机构代理"这类间接证据更贴题。
- **L2**:Ma-Wang-Fang-Wang (2020) [S11] + Han-Zhao-Chen-Guo (2022) [S12] 确认 2018-08-20 是 A 股收盘集合竞价制度的真实分界点,前后"收盘几格占比"代表的不是同一个稳态量——这是 D 组两格(R 第 14、15 项)结果解读时必须补充的一条备选解释,而不是我们环境独有的问题。
- **L3**:Wang-Hudson-Rhodes-Zhang-Gregoriou (2020) [S15] 是本轮证据等级最高的一篇,直接给出"峰度 vs 五种流动性代理(含零收益占比)"的回归设计和结果:峰度对全部五个代理都显著,但幅度/显著性在零收益占比上明显弱于另外四个连续型代理——这给 B 组 R 第 5/6 项的结果解读一个具体的文献对照基准,不是单纯的"像/不像"判断。

**机制上说得通、但证据是技术分析范式或研报,不是严格的学术因子检验,写任务书时必须标注"推断/研报,非严格文献证实"**:

- L1 的"两窗口之差"——Han-Zhou-Zhu [S3] 验证的是价格水平的多尺度移动平均,不是日内形状量的两窗口差,这一跳没有文献先例。
- L4 整题——国内 CPV/RPV 研报 [S19] 是最贴题的材料,但我没读到全文公式,回测数字是研报自报;Chan-Fong [S18] 给出"有符号失衡 vs 无符号相关"的机制提醒,是学术证据但不是直接针对"日内相关系数聚合方式"的检验。**L4 比其他三题证据薄弱得多,是本轮四题里学术文献最空白的一题**。

**搜不到、如实记录,不要当成文献支持**:

- L1:没有论文直接对照同一特征的"滚动均值版"和"滚动偏度/峰度/两窗口差版"并报告方向幅度差异。
- L2:没有论文把"次新股滚动窗口不一致"系统解决(不是简单剔除);没有论文在亚洲市场把竞价占比直接构造成横截面因子并检验。
- L3:没有论文直接检验"分钟级"(不是日度)收益峰度与"分钟级"零收益比例的关系,也没有找到价格离散/涨跌停对尾部指数估计偏差的直接文献。
- L4:没有任何学术论文报告过日度量价相关系数的波动/偏度/极值版本——这正是本轮 N 位和 R 第 11/12 项要测的结构,文献空白;也没有找到"VWAP 溢价"作为横截面因子的同行评审证据。
