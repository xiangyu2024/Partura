# 文献:种子 808,C 组,第 2 轮

对应 `analysis.md` §5 的 Q1–Q4。只用 2023-08-08 前发表的论文 / 工作论文 / 研究报告(arXiv、SSRN、NBER 以首版日期为准);拿不准发表日期的不用。
每条处理方式后面用 `[R#]` 标出处,对应文末「出处列表」。`verified: true` 表示本次会话里确实在 WebSearch 结果或 WebFetch 页面上看到了标题 / 作者 / 刊物 / 链接这几项;
没查到的,写明"搜不到",不编。本轮部分文献与第 1 轮 `r1/lit.md` 重叠(Banz、Fama-French 2008、DGTW、涨跌停三篇),是因为第 2 轮 Q3/Q4 问的问题与第 1 轮方法论部分
对准同一批文献,本次重新检索确认后再引用,不是直接照抄。

---

## Q1(对准核心 1–3 / 轴 B:日内价格离散与停滞)

**(i)「当日访问过多少个不同价位 / 收益值」这种计数型度量,文献里有没有先例,还是一律用零收益占比 / 价差代理 / Amihud 冲击?**

1. **"零收益占比"是这支文献的主干,但它是比"计数当日不同值"更粗的一个二元版本。** Lesmond, Ogden & Trzcinka(1999)"A New Estimate of Transaction Costs"(LOT)
   的出发点是:"能用来估计交易成本的数据特征,就是零收益出现的频率"——如果交易成本高,投资者当天不交易,收益就记为零;
   LOT 用零收益的发生频率、beta、特质波动率一起拟合出一个隐含的交易成本带宽 `[R1]`。Fong, Holden & Trzcinka(2017)"What Are the Best Liquidity Proxies for Global Research?"
   给出 LOT 的简化版 FHT:同样基于零收益占比,但假设成本对称、不需要估计 beta,只用月度日收益标准差和零收益占比,配合正态分布函数反解出隐含价差;
   作者强调"对一只高 beta、高特质波动的股票,一天零收益是更强的高成本信号" `[R2]`。Goyenko, Holden & Trzcinka(2009)"Do Liquidity Measures Measure Liquidity?"
   做了横向赛马,零收益类度量(Zeros)在他们单独做的一组长样本比较里表现稳定 `[R3]`。
   **翻译成我们的算子语言**:这三篇用的"零收益占比"(`day_zero_ratio` 的跨日版本)是在**月度 / 跨日**频率上统计"多少天收益恰好为零",
   不是在**日内分钟**频率上统计"一天里出现过多少个不同的价位"——我们的 `day_distinct_ratio(Ret)` 是把同一个直觉(停滞 = 没交易 = 高成本)搬到了日内分钟尺度,
   文献里没有直接对应的先例,这是一个真正的尺度外推,不是抄文献;但外推借用的机制(停滞信号成本)是文献反复验证过的,这给 §1.3 的"真来源"判定加分,
   而不是减分。
2. **直接搜"当日不同价位个数"这个具体计数口径,没有找到可独立核实的资产定价论文**(搜不到,见文末)。
   最接近的是价格"staleness"(报价停滞)这支文献用的"一段时期内零变动的次数",但仍然是跨日 / 跨月的二元事件计数,不是日内分钟级的多值计数;
   另一支更接近的是 Holden(2009)"New Low-Frequency Spread Measures" 的 Effective Tick 方法,用的是**截面**上交易价格落在"整数、半档、四分之一档"等离散价格簇上的**频率**
   来反推隐含价差——这是"价格聚集/离散的频率"思路第一次被当作一个连续可估的量,而不是 0/1 事件,方法论上离我们的 `distinct_fraction` 最近 `[R5]`。

**(ii)这类度量与"相对 tick"(tick / 价格)机械耦合,文献怎么拆开这两部分?**

3. **Harris(1991)"Stock Price Clustering and Discreteness"**:价格聚集程度随价格水平升高、随波动率升高而升高,随公司规模和交易频率升高而降低
   `[R4]`——这正是 §1.3 机械分解里 (i)(ii)(iii) 三条通道的最早文献来源:价格水平(tick/价格的比值)、活跃度(交易频率)、波动率同时驱动"离散/聚集"这个表面现象,
   文献自己也没有一步到位地拆开,而是分别做横截面回归控制。
4. **Holden(2009)把"价格聚集"显式写成相对价差的函数再反解**:他的核心假设是"价格聚集完全由价差大小决定",聚集到某个价格簇的概率是
   "各可能价差取值的概率加权平均"除以均价 `[R5]`。**翻译成算子语言**:这给出了把 tick 通道显式除掉的具体操作依据——
   不是简单地"按市值分桶控制",而是先构造一个相对价差 / 相对 tick 的代理(我们环境里现成能用的就是 `div(day_sum(Amt), day_sum(Volume))` 的倒数再乘 tick,
   或直接用未复权均价做分桶轴),再看"聚集 / 离散"的剩余部分还能不能预测收益——这与 `analysis.md` §1.3(e)/§1.6 提出的"按未复权均价分桶"判别式方法论一致,
   而且 Holden 的论文证明了这个拆分在方差估计里是可行的,不是我们凭空设计的。
5. **O'Hara, Saar & Zhong(2019)"Relative Tick Size and the Trading Environment"**:直接把"相对 tick"(而不是绝对 tick)当作解释交易环境差异的核心变量,
   发现相对 tick 越大,高频做市商的行为模式(挂单久、报价激进、利润率高)越明显,且深度的方向效应在"tick 受限"和"tick 不受限"两种机制下相反 `[R6]`。
   **翻译**:文献里"相对 tick"从来不是一个可以忽略的控制变量,而是本身就决定市场微观结构机制切换的一个阈值变量——
   这支持把"相对 tick"(未复权均价的倒数乘 0.01)当一个独立的条件轴去试,而不仅仅是"用来剥掉 tick 效应的工具变量"。

**(iii)控制了规模和流动性之后,这类度量还有没有定价能力;A 股的 0.01 元 tick / T+1 / 涨跌停制度下有没有专门结果?**

6. **Han & Lesmond(2011)"Liquidity Biases and the Pricing of Cross-Sectional Idiosyncratic Volatility"**:零收益和买卖价差的反弹(bid-ask bounce)
   会让特质波动率的估计产生系统性偏差,这个偏差本身能解释此前"特质波动率能预测收益"这一异象的大部分,控制偏差后预测力消失 `[R11]`。
   **翻译成警示**:这是对 §1.3(e) 那条"陷阱 1/3 同一机制"的文献级佐证——零收益 / 低 distinct 这类度量天生带着波动率估计偏差,
   仅靠线性中性化波动控制、仅靠按市值分桶,都不足以排除"这个度量只是波动率估计偏差的代理"这个可能性;
   更干净的做法应该是像 Han & Lesmond 那样先显式建模偏差再剔除,而不是停留在"残差里还有没有东西"这个层面。
7. **A 股 0.01 元 tick / T+1 / 涨跌停制度下专门针对"价格离散度/零收益"定价能力的文献,搜不到可独立核实的论文**(搜了中英文关键词均未找到,见文末)。

---

## Q2(对准 H1 的自条件写法与 `ts_max` 的极值口径:水平还是冲击)

**(i)「相对自身近期水平的异常」怎么定义——时间序列残差、滚动 z 化、分组内标准化、还是差分?**

1. **Amihud(2002)"Illiquidity and Stock Returns"自己就是"水平 vs 冲击"这个问题的源头**:他把非流动性拆成"预期的"(expected,用历史序列拟合出的水平)
   和"未预期的"(unexpected,实现值减预期值的差)两部分——预期非流动性抬高事前预期收益(水平溢价),未预期非流动性冲击则与**同期**收益负相关 `[R7]`。
   **翻译成算子语言**:"水平"对应一个较长窗口的平滑统计量(例如 `cross_mean(·, 60)`),"冲击/创新"对应**实现值减去这个平滑统计量**的残差——
   这正是 `analysis.md` §4.3 N-1 里已经写出的 `sub(cross_mean(·, 5), cross_mean(·, 60))` 构造,文献给出的是"时间序列上减去自己的滑动平均",
   不是"除以自己的滑动标准差再 z 化"。
2. **Chordia, Roll & Subrahmanyam(2000)"Commonality in Liquidity"构造"流动性变化"时,用的是逐日的百分比变化(一阶差分),不是滚动 z 化**:
   他们把流动性的"协动"定义为个股流动性与市场 / 行业流动性**变化率**之间的协变 `[R9]`。**翻译**:文献默认的"冲击"算子是**差分**(`sub` 或百分比变化),
   不是 `cs_bucket_zscore` 这类截面标准化——截面 z 化(在同一天里跨股票比较)和时间序列差分(同一只股票跨时间比较)是两件不同的事,
   H1 现在做的是"先截面分桶 z 化,再对 z 化后的序列取 40 日最大值",混合了截面条件化和时间序列极值,文献里没有现成的对照写法,这是 §1.3(d) 那条
   "水平与创新符号相反"现象目前唯一的、还没被文献直接验证过的部分,要诚实地标成推断。
3. **Pástor & Stambaugh(2003)"Liquidity Risk and Expected Stock Returns"构造流动性风险因子时,用的是一个月度流动性度量**(基于成交量条件下的
   收益反转系数)**逐月的变化,当作"流动性冲击"**,再看个股收益对这个冲击序列的敏感度是否被定价 `[R8]`。**翻译**:这进一步印证"冲击"在文献里是
   "这一期的度量减去(或相对于)上一期/长期水平",而不是"自身历史的标准化异常值";如果要给 H1 的自条件写法找一个干净对照,
   应该先试显式差分(`sub`),再试截面 z 化,两者不是同一件事,不能互相替代着验证。

**(ii)用窗口内的极值(而不是均值)当特征,文献里有没有先例和理由?**

4. **George & Hwang(2004)"The 52-Week High and Momentum Investing"是这个问题最直接的先例**:他们直接用过去 52 周价格的**最大值**(而不是均值)
   构造"距 52 周高点的距离"这个特征,发现它比传统的累计收益动量预测力更强、更持久,且在长期不发生反转——作者的解释是投资者会锚定在一个极值参照点上,
   对新信息反应不足 `[R10]`。**翻译成算子语言**:这是文献里"用 `ts_max` 而不是 `cross_mean`"最直接的理由和先例,
   但要诚实说清楚:George & Hwang 给出的机制是**投资者锚定行为**(心理参照点),而 `analysis.md` §1.5 给出的理由是**distinct 闸门的机械开门器**
   (40 日最大值把不同日子的分母混进来才能过阈值)——两者解释的是同一个算子选择,但机制完全不同,不能把 George & Hwang 的"锚定"直接套在 H1/H2 上当作
   机制证据,只能当作"极值类特征本身在文献里站得住"的独立佐证,这两件事要分开记。
5. Bali, Cakici & Whitelaw(2011)"Maxing Out"(已见于 `r1/lit.md` R5)用过去一个月**日收益**的最大值构造 MAX 因子,是另一个"窗口极值当特征"的先例,
   但衡量对象是收益本身而非流动性/离散度,只作为旁证,不单独编号。

**(iii)「相对同规模同行」的条件化与「全市场排序」给出的结论有没有被比较过?**

6. 这个问题与 Q3 的方法论高度重叠,直接复用下面 Q3 §(ii) 的 Hou, Xue & Zhang(2020)和 Fama & French(2008)两篇:
   它们系统性地比较过"全样本等权排序"与"按规模分组/NYSE 断点的条件化排序"给出的显著性结论,发现绝大多数特征的显著性**只在不做规模条件化时才出现**
   `[R13][R14]`(细节见下)。**翻译**:这给了 Q2(iii) 一个明确的方向性答案——条件化排序(within-group)比全市场排序更容易把"真信号"和"规模/微盘代理"
   分开,而不是两者等价、只是写法不同。

---

## Q3(对准陷阱 3 / H4 / `LogFloatShares` 簇:非单调的规模暴露)

**(i)有没有记录过「把最大 / 最小 X% 剔掉以后效应才出现 / 才消失」这种拐点形状?**

1. **Banz(1981)本身记录的规模效应就不是线性的**:效应集中在最小一档公司,中等与大公司之间几乎没有差异 `[R12]`。这是"规模效应非单调"这个判断最早的来源,
   文献处理方式是**十分位分组**,不是对 `log(市值)` 做线性残差。**翻译**:检验 H3–H6 是不是"规模非线性残差"的最直接办法,
   是把 `LogFloatCap` 分成十等分,只在最小一档内重新算 score,而不是看中性化后残差还剩多少。
2. **Fama & French(2008)"Dissecting Anomalies"把这个检验标准化了**:用 NYSE 的 20 分位 / 50 分位断点把股票分成 microcap / small / big 三组分别检验,
   发现发行类、动量、应计类异象在三组里都存在,但资产增长、盈利、账面市值比类异象**只在 microcap / small 里显著,在 big 里消失** `[R13]`。
   **翻译**:这给出了一个比"看 ρ_known 高不高"更直接的判定方法——把本轮候选按 `LogFloatCap` 三等分(或用现成的最小 20%/50% 断点),
   分别重算 score,如果只在最小一组里过 0.5,就该标成"规模代理",这正是 §1.6 列的"最大未知"之一,现在有明确的检验配方可以抄。
3. **Hou, Xue & Zhang(2017 NBER WP23394 / 2020 RFS)"Replicating Anomalies"把这件事推到了极致**:只把等权 / 全样本断点换成**价值加权 + NYSE 断点**
   (也就是系统性地降低微盘股权重),452 个此前发表的异象里就有 65% 在 5% 显著性下失效,用 3.0 的 t 阈值失效率升到 82% `[R14]`。
   **翻译**:这是 Q3(iii) 的直接答案——文献对"一个特征只在最小几档市值里有效"的**通行处理不是把它当独立异象,而是默认它是微盘股驱动的,
   要求作者自己证明换成规模加权 / 排除微盘后还站得住**,举证责任在声称发现的人这一边,不是在质疑者这一边。这个结论应该直接写进本轮审计的默认立场。
4. **Liu, Stambaugh & Yuan(2018 NBER WP24458 / 2019 JFE)"Size and Value in China"给出了 A 股专门的版本,而且机制和我们现在遇到的问题几乎一模一样**:
   他们在构造中国的规模因子时,**直接剔除**市值最小的 30% 股票,理由是中国的壳公司重组(reverse merger)制度让这批股票的市值里有很大一块是"壳价值"
   (他们估计这批股票里典型个股约 30% 的市值是潜在壳价值),这批股票只占总市值的 7%,但如果不剔除,会系统性污染规模因子和由此产生的一大批"异象" `[R15]`。
   **翻译**:这是本轮最值钱的一条文献证据——它不是泛泛地说"规模效应非线性",而是针对**A 股**明确说"线性市值中性化 / 残差化挡不住这部分暴露,
   正确做法是整段剔除,不是中性化",与 `analysis.md` §1.2/§1.4 独立得出的结论(「线性市值中性化挡不住的非线性规模暴露」)是同一个诊断的两种语言。
   建议的算子化动作:给 H3–H6 配一个"剔除 `LogFloatCap` 最小 30% 股票后重新算 score"的稳健性检验,而不是只做残差化。

**(ii)「对 log 市值取残差」与「在市值分组内排序」给出不同结论的具体案例?**

5. 案例就是上面的 Fama-French(2008)vs 其前身做法的对比,以及 Hou-Xue-Zhang 的大规模复现本身——**等权全样本排序**(近似于全市场线性残差化的效果,
   因为两者都没有限制微盘股的权重)和**规模条件化排序**(NYSE 断点分组)给出的显著性结论系统性不同,后者让大多数异象消失 `[R13][R14]`。
   `r1/lit.md` R12 的 Daniel, Grinblatt, Titman & Wermers(1997)特征匹配法(DGTW)是第三条路线,用 125 个规模 × 账面市值比 × 动量的被动组合做基准,
   不假设线性关系,代价是需要足够多股票填格子,在此处重复引用作为与残差化、条件排序并列的第三种方法。

**(iii)只在最小几档市值里有效的特征,文献倾向标成规模代理还是独立异象?**

6. 已在第 1 点回答:**标成规模 / 微盘代理是默认立场**,除非作者能证明换成价值加权或排除微盘后效应仍然存在 `[R13][R14][R15]`。

---

## Q4(对准 N-1 / N-2:涨跌停与停牌对「不动」类度量的污染)

**(i)是剔除封板日和停牌日,还是把它们单独当一个特征?**

1. `r1/lit.md` R14、R15、R16 三篇(本次重新检索确认,链接与细节不变)都不剔除封板日,而是把"触及涨跌停"当一个**独立的事件特征**单独处理:
   Wan et al.(2015)按涨停 / 跌停分别统计次日延续概率,得到冷却效应而非磁吸效应的证据 `[R17]`;
   Chen, Gao, He, Jiang & Xiong(2017 NBER / 2019 J. Econometrics)用涨停日的大户净买入行为预测后续反转,且专门把 ST(窄限制)股票单独拿出来做因果检验 `[R18]`;
   Wu, Wang & Li(2017)发现开板后收益呈"W"形,且连续触及涨跌停的天数长度本身是一个独立影响因素 `[R19]`。
   **翻译**:三篇的共同做法是"保留事件,但把事件变成一个带方向(涨停/跌停)、带强度(连续天数)的独立变量,再看它如何与其他变量交互",
   不是简单地把那几天从样本里删掉。这支持 `analysis.md` §4.3 N-2 的建议:`LimitWidth` 和涨跌停触及应该做成**缩放 / 分组 / 滚动计数变量**,
   而不是直接从 `day_flat_run_max` 这类连续特征的样本里剔除涨跌停日——文献里没有"直接剔除"这个处理方式的先例。

**(ii)涨跌停宽度不同的组(主板 10% / 创业板科创板 20% / ST 5%)之间,这类度量还可比吗,文献怎么归一?**

2. **本轮新找到两篇直接做「同一批股票,宽度改变前后」对照的论文,结论指向"不可直接比"**:Zhang, Wang, Hao & He(2022)"Price Limit and Stock Market Quality"
   用创业板 2020-08-24 从 10% 放宽到 20% 这个准自然实验做双重差分,发现放宽后同一批股票的**流动性指标和知情交易概率都显著上升** `[R20]`;
   Wan & Zhang(2022)"The Effect of Relaxing Daily Price Limit"用事件研究法做同一个变化,也发现放宽后**流动性显著改善、波动率显著上升**,
   但对价格效率没有显著影响 `[R21]`。**翻译成警示**:这两篇量化地证明了"涨跌停宽度本身会机械地改变测得的流动性水平"——
   同一批公司、同一套基本面,仅仅因为制度宽度从 10% 变成 20%,流动性类指标的读数就会系统性跳变。
   这意味着如果把 ST(5%)、主板(10%)、创业板科创板(20%)的股票混在一起直接比较 `day_flat_run_max` / `day_distinct_ratio` 这类"不动"指标的绝对水平,
   相当于把一部分制度性噪声当成了经济信号。
3. **但"文献怎么归一"这部分搜不到**:两篇论文研究的都是"同一个板块,制度改变前后"的纵向对照(准自然实验),
   没有找到专门给"横截面上,不同涨跌停宽度板块之间如何把停滞类指标调整到可比口径"这件事提出显式归一方法的论文(搜了中英文关键词均未找到,见文末)。
   `analysis.md` 给的"不要直接比较、用 `LimitWidth` 做调节变量而不是归一化分母"这条路线,目前只有这两篇论文的间接支持(宽度确实造成机械差异),
   没有文献级的归一公式可以抄,这一点要如实告诉 PI。

**(iii)「封板频率 / 开板后收益形状」本身作为横截面特征,有没有被检验过?**

4. Wu, Wang & Li(2017)测的是**时间序列**上"开板后"的收益动态形状(事件窗口内的条件期望),不是把"封板频率"当一个静态的**横截面**特征去给全市场排序、
   检验其能不能预测未来收益 `[R19]`;Chen et al.(2017/2019)同理,是事件研究而非横截面特征检验 `[R18]`。
   **把"过去 N 日封板次数"当一个独立的横截面排序特征(而不是事件窗口的条件变量)直接检验其预测力的论文,搜不到可独立核实的文献**(见文末)。
   这与 `analysis.md` §4.3 N-2 提出的"滚动计数当缩放/分组变量"是一致的——文献支持"连续天数是独立影响因素"这个机制判断,
   但没有文献证明"这个计数本身可以当独立 alpha 因子来挖",这条界限要分清楚,不要把 §4.3 的建议说成文献已经验证过的结论。

---

## 出处列表

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|---|
| R1 | A New Estimate of Transaction Costs | Lesmond, D.A.; Ogden, J.P.; Trzcinka, C.A. | 1999(RFS 12(5)) | Review of Financial Studies | https://ideas.repec.org/a/oup/rfinst/v12y1999i5p1113-41.html | true |
| R2 | What Are the Best Liquidity Proxies for Global Research? | Fong, K.Y.L.; Holden, C.W.; Trzcinka, C.A. | 2017-03(Advance Access)/2017-07(RoF 21(4)) | Review of Finance | https://host.kelley.iu.edu/cholden/Fong%20Holden%20and%20Trzcinka%20(2017).pdf | true |
| R3 | Do Liquidity Measures Measure Liquidity? | Goyenko, R.Y.; Holden, C.W.; Trzcinka, C.A. | 2009-05(JFE 92(2)) | Journal of Financial Economics | https://ideas.repec.org/a/eee/jfinec/v92y2009i2p153-181.html | true |
| R4 | Stock Price Clustering and Discreteness | Harris, L. | 1991(RFS 4(3)) | Review of Financial Studies | https://ideas.repec.org/a/oup/rfinst/v4y1991i3p389-415.html | true |
| R5 | New Low-Frequency Spread Measures | Holden, C.W. | 2009(JFM 12(4)) | Journal of Financial Markets | https://host.kelley.iu.edu/cholden/Holden%20(2009).pdf | true |
| R6 | Relative Tick Size and the Trading Environment | O'Hara, M.; Saar, G.; Zhong, Z. | 2019(RAPS 9(1)) | Review of Asset Pricing Studies | https://ideas.repec.org/a/oup/rasset/v9y2019i1p47-90..html | true |
| R7 | Illiquidity and Stock Returns: Cross-Section and Time-Series Effects | Amihud, Y. | 2002(JFM 5(1)) | Journal of Financial Markets | https://www.cis.upenn.edu/~mkearns/finread/amihud.pdf | true |
| R8 | Liquidity Risk and Expected Stock Returns | Pástor, Ľ.; Stambaugh, R.F. | 2003(JPE 111(3)) | Journal of Political Economy | https://www.johnhcochrane.com/s/pastor_stambaugh_jpe.pdf | true |
| R9 | Commonality in Liquidity | Chordia, T.; Roll, R.; Subrahmanyam, A. | 2000(JFE 56(1)) | Journal of Financial Economics | https://doi.org/10.1016/S0304-405X(99)00057-4 | true |
| R10 | The 52-Week High and Momentum Investing | George, T.J.; Hwang, C.-Y. | 2004-10(JF 59(5)) | Journal of Finance | https://doi.org/10.1111/j.1540-6261.2004.00695.x | true |
| R11 | Liquidity Biases and the Pricing of Cross-Sectional Idiosyncratic Volatility | Han, Y.; Lesmond, D. | 2011(RFS 24(5)) | Review of Financial Studies | https://ideas.repec.org/a/oup/rfinst/v24y2011i5p1590-1629.html | true |
| R12 | The Relationship Between Return and Market Value of Common Stocks | Banz, R.W. | 1981(JFE 9(1)) | Journal of Financial Economics | https://floridapsc.com/library/filings/2023/00092-2023/Support/Staff%20Exhibit%20167/Witness%20Testimony%20Workpapers/Witness%20Nelson/42,43_Banz,%20The%20Relationship%20Between%20Return%20and%20Market%20Value%20of%20Common%20Stocks,%20JFE%209%20(1981).pdf | true |
| R13 | Dissecting Anomalies | Fama, E.F.; French, K.R. | 2008-08(JF 63(4)) | Journal of Finance | https://ideas.repec.org/a/bla/jfinan/v63y2008i4p1653-1678.html | true |
| R14 | Replicating Anomalies | Hou, K.; Xue, C.; Zhang, L. | 2017-05(NBER WP23394)/2020(RFS 33(5)) | NBER Working Paper / Review of Financial Studies | https://www.nber.org/papers/w23394 | true |
| R15 | Size and Value in China | Liu, J.; Stambaugh, R.F.; Yuan, Y. | 2018-03(NBER WP24458,修订 2018-12)/2019(JFE 134(1)) | NBER Working Paper / Journal of Financial Economics | https://www.nber.org/papers/w24458 | true |
| R16 | Measuring Mutual Fund Performance with Characteristic-Based Benchmarks | Daniel, K.; Grinblatt, M.; Titman, S.; Wermers, R. | 1997-07(JF 52(3)) | Journal of Finance | https://ideas.repec.org/a/bla/jfinan/v52y1997i3p1035-58.html | true |
| R17 | Statistical Properties and Pre-Hit Dynamics of Price Limit Hits in the Chinese Stock Markets | Wan, Y.-L.; Xie, W.-J.; Gu, G.-F.; Jiang, Z.-Q.; Chen, W.; Xiong, X.; Zhang, W.; Zhou, W.-X. | 2015-03(arXiv:1503.03548)/2015-04(PLOS ONE 10(4)) | arXiv / PLOS ONE | https://arxiv.org/pdf/1503.03548 | true |
| R18 | Daily Price Limits and Destructive Market Behavior | Chen, T.; Gao, Z.; He, J.; Jiang, W.; Xiong, W. | 2017-11(NBER WP24014)/2019-01(J. Econometrics 208(1)) | NBER Working Paper / Journal of Econometrics | https://www.nber.org/papers/w24014 | true |
| R19 | Post-hit Dynamics of Price Limit Hits in the Chinese Stock Markets | Wu, T.; Wang, Y.; Li, M.-X. | 2017(Physica A 465) | Physica A: Statistical Mechanics and its Applications | https://ideas.repec.org/a/eee/phsmap/v465y2017icp464-471.html | true |
| R20 | Price Limit and Stock Market Quality: Evidence from a Quasi-Natural Experiment in the Chinese Stock Market | Zhang, X.; Wang, Z.; Hao, J.; He, F. | 2022(Pacific-Basin Finance Journal 74, 101778) | Pacific-Basin Finance Journal | https://ideas.repec.org/a/eee/pacfin/v74y2022ics0927538x22000737.html | true |
| R21 | The Effect of Relaxing Daily Price Limit: Evidence from the ChiNext Market of China | Wan, X.; Zhang, J. | 2022(Economics Letters 215, 110509) | Economics Letters | https://ideas.repec.org/a/eee/ecolet/v215y2022ics0165176522001318.html | true |

**搜了但没有可独立核实的文献,不编、如实列在这里(不算出处):**

- 直接用"当日访问过多少个不同价位 / 不同收益值"这一具体计数口径构造横截面特征、并检验其定价能力的资产定价论文(Q1(i))。
- A 股 0.01 元 tick、T+1、涨跌停制度下,专门针对"价格离散度 / 零收益占比"定价能力给出结果的论文(Q1(iii))。
- 专门给"横截面上,不同涨跌停宽度板块(主板 / 创业板科创板 / ST)之间如何把零收益 / 停滞类指标调整到可比口径"提出显式归一方法的论文(Q4(ii))——
  只找到"同一板块放宽前后对照"的准自然实验(`[R20][R21]`),没有找到跨板块横截面归一的方法论文献。
- 把"过去 N 日封板次数"当作独立的横截面排序特征(而非事件窗口条件变量)直接检验其预测力的论文(Q4(iii))。
- 中文文献里专门检验"A 股零收益率/价格离散度与换手率交互"的期刊论文:搜到一篇基于 1997–2005 年 A 股数据、同时使用 Amihud、换手率、零收益率、
  有效流速、Pastor-Stambaugh 指标做流动性溢价检验的硕士学位论文,但只在 core.ac.uk 上有记录条目,没有可独立核实的标题/作者/刊物三要素齐全的链接,
  不计入出处列表,如实记录于此。

---

## 给核心 / R 变体的直接翻译(摘要,方便 PI 和结构解剖员对表)

- **判别式实验的文献支持更硬了**:Holden(2009)`[R5]` 和 O'Hara-Saar-Zhong(2019)`[R6]` 都把"相对 tick / 价格聚集频率"当作可以显式拆出来的量,
  支持 `analysis.md` §1.3(e)/§1.6 提出的"按未复权均价分桶"判别式——这不是我们自己设计的特例检验,是文献里拆分 tick 通道的标准做法搬过来的。
- **H1 的 `ts_max` 自条件写法,文献给了"极值当特征"的先例(George-Hwang `[R10]`),但机制不能照搬**:52 周高点的解释是投资者锚定,
  不是 distinct 闸门——两件事都支持用极值,但为完全不同的理由,写假设时要分开说,不能把锚定效应当成本种子的机制证据。
- **"水平 vs 冲击"的标准构造是时间序列上的差分或预期/实现分解(Amihud `[R7]`、Pastor-Stambaugh `[R8]`、Chordia-Roll-Subrahmanyam `[R9]`)**,
  不是截面 z 化——H1 现在做的"先截面分桶 z 化再取时间序列极值"在文献里找不到直接对照写法,§1.3(d) 的"水平与创新符号相反"目前只能算推断。
- **轴 A(规模)最硬的新证据是 Liu-Stambaugh-Yuan(2019)`[R15]`**:A 股语境下,文献自己的结论是"线性残差化不够,要整段剔除最小 30%",
  与 `analysis.md` §1.2/§1.4 独立得出的"线性市值中性化挡不住的非线性规模暴露"是同一个诊断;建议真的加一个"剔除 `LogFloatCap` 最小 30%"的稳健性检验。
- **"只在最小几档市值里有效 → 标成规模代理"是文献的默认立场,不是我们自己定的规则**(Fama-French 2008 `[R13]`、Hou-Xue-Zhang 2020 `[R14]`,
  65%–85% 的已发表异象在规模条件化后失效)——举证责任在声称发现的一方,这条可以直接写进第 3 轮的审计默契。
- **N-2(涨跌停轴)的"别剔除、当独立变量处理"的建议,文献三篇一致支持(`[R17][R18][R19]`),但"跨板块宽度归一"和"封板频率当横截面特征"这两小块
  没有文献可抄,是我们自己要做的方法论工作,不要在计划里说成"文献已验证"。**
