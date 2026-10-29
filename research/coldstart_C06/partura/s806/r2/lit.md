# 文献:种子 806,C 组(Partura),第 2 轮

读入:`r2/analysis.md` §6 的四个题目(对准核心 A `day_centroid(Amt)`、核心 A 的外围"水平 vs 新息"、核心 B
`day_signed_ratio(Ret, Volume)`、族 I–III 的"代理 vs 信息"判定)。只用 WebSearch / WebFetch 查到、且能确认
**首版日期在 2023-08-08 之前**的论文 / 工作论文 / 研究报告(期刊论文按刊出年份,早期工作论文版本若能查到具体
年月则一并写出)。日期拿不准的在各节「搜不到 / 拿不准,不用」里写明,不编造数值、不编造找不到全文的论文的
具体结论。

每条处理后面用 `[键]` 标出处,键对应文末「出处列表」。同一出处可能支撑多条处理。算子名称按本环境
`AlphaCube`/`Partura` 的目录(`src/alphacube/catalog.py`、`partura/ops_ext.py`)写,具体定义:
`day_centroid(x) = sum(t·|x_t|)/sum(|x_t|)`(按分钟序号归一化到 [0,1] 的时间加权重心)、
`day_signed_ratio(x,y) = sum(|y|·sign(x))/sum(|y|)`(按 y 定权的 x 符号净占比,[-1,1])、
`cross_zscore(x,d)` / `cross_ema(x,d)` 是跨日(非截面)的历史标准化、`cs_bucket_rank/demean/zscore(y,x)`
是在 x 的十分位桶内对 y 做排名 / 去均值 / 标准化。

---

## Q1 —— 日内成交量 / 成交额的时点分布,文献里怎样构造、方向是什么、怎样剥掉规模/流动性/被动资金

**能摘到的处理方式:**

1. **U 形本身来自"流动性交易者挤到厚市场时段"这个均衡,而不是噪声。** 做市商理论最早的版本认为,知情交易者的存在
   让流动性交易者有动机把交易集中到成交活跃的时段(开盘、收盘)以降低被"吃价差"的概率,这个挤出效应直接推出
   成交量的 U 形。翻成算子语言:`day_centroid(Amt)` 這个核心测的正是"这种挤出发生的程度",值越靠近 0 或 1
   说明挤出越强、越靠近 0.5 说明全天交易越均匀;理论本身没有给出"挤出程度"该如何预测收益的方向,只说明
   U 形是均衡现象,不是随机噪声,适合作为一个结构稳定的特征而不是数据巧合。[AP1988]

2. **在中国市场,U 形中"收盘段"那一半有一个与美股不同、且是本环境核心 A 直接相关的制度性来源:T+1 使得
   收盘买入、次日开盘卖出是本地流动性最好的套利/交易方式,这把成交量系统性地推向收盘段。** 一篇用 2012–2017
   年沪深 300 指数及其 ETF 半小时数据的研究明确写道:"T+1 交易规则禁止当天买卖,因此为流动性考虑的最佳策略
   是在当天收盘买入、次日开盘卖出,这正是日内成交量呈 U 形的主要原因"("the best strategy for liquidity is
   to buy in the today's market close and sell in the next day's market open... main reason for the U-shaped
   pattern"),并在此基础上发现第 7(6)个半小时收益能显著预测最后半小时收益(R² 3.8–5.7%,财务动荡期更高)。
   翻成算子语言:如果 `day_centroid(Amt)` 在 A 股上更靠近 1(收盘侧),这篇文献把它读成"T+1 下的流动性驱动
   买盘",而不是单纯的信息事件——这对 analysis.md §5.1 的外围建议(3)"钱是在价格动之前还是之后进来的"
   有直接含义:应该把 `day_centroid(Amt)` 相对 `day_centroid(abs_(Ret))` 的差值,与 `day_centroid(Amt)`
   本身的收盘侧程度做交互,而不是假设两者独立。[LY2022]

3. **"量的时点"作为预测变量,文献里几乎总是和"收益的时点"分开构造、再做差或做比**,而不是把全天的量价
   直接揉成一个协方差标量。按半小时切片看"与整个交易日同周期"的位置做收益延续性分析(开盘段 vs 收盘段分别
   构造,再跨日比较),这类处理发现收益延续性在**最前和最后的半小时最强**,且独立于公司规模、系统性风险或
   指数成分股身份。翻成算子语言:这支持把 `day_centroid(Amt)` 这个核心的外围做成"分段版本"——例如用
   `day_first(Amt)`(开盘段权重)与 `day_last(Amt)`(收盘段权重)分别构造再相减或相除,而不只是用一个连续
   重心标量,因为文献里证据最强的正是两端、不是重心本身。[H2010]

4. **把"量"换成"量的离散/不均匀程度"(而不是时点)是另一条独立于 U 形方向的构造方式**,用高频数据算出的
   成交量时间间隔序列(超过某阈值的量之间的时间 gap)在中国股票和指数上都服从幂律尾部,且有长期记忆;大额
   成交后紧跟大额收益的关联在最大的成交量上最强。翻成算子语言:这类处理提示除了 `day_centroid`(一阶矩,
   时点)之外,`day_gini(Amt)`(衡量量集中在少数分钟 vs 均匀分布)是同一族但正交的构造——可以作为核心 A
   外围里"条件化"分支的一个候选条件变量,而不是直接做成新核心。[RZ2010]

5. **"量的水平"(而不是时点)作为规模/流动性代理的问题,在把量换成"相对自身历史的异常"后依然存在方向性
   预测力,但那是 Q2 的内容(水平 vs 新息),这里只强调:多篇文献报告的成交量 U 形在**成交量本身**上稳健,
   但在**波动率**上不一定呈 U 形(中国 T+1 下日内波动率的 U 形证据比美欧弱),说明 `day_centroid(Amt)` 这个
   核心不能简单类比成 `day_centroid` 用在波动代理上的版本——这条是提醒,不是新处理方式。[RZ2010]

**搜不到 / 拿不准,不用:**
- 没搜到专门以"成交量加权时间重心"(volume-weighted time-of-day centroid)为直接构造变量、做截面收益预测
  检验的论文;搜到的"center of volume mass"文献(Bernile-Gao-Hu)是期权行权价維度的重心,不是时间维度,
  结构不同,不能当作直接支撑。
- 没搜到专门讨论"收盘集合竞价占比"预测截面收益、且明确处理了中国 A 股被动基金占比(A 股被动占比在样本期内
  远低于美股/欧洲,相关欧美文献的被动资金机制不能直接套用)的论文;BlackRock/SSGA 的被动资金驱动收盘量
  份额上升的证据都是美股/欧股的行业报告,不是经同行评议的截面收益预测检验,这条按"搜不到直接证据"处理,
  不要把美股的被动资金逻辑套到 A 股样本上。
- 中国 A 股分段(开盘半小时 vs 收盘半小时)收益延续/反转的具体符号,我在 r1 已经查过 `[CGZ2019]`(Chu-Gu-Zhou
  2019),本轮没有新增独立于 r1 的证据,不重复摘录,请参考 `r1/lit.md` Q1 第 3 条。

---

## Q2 —— 持久水平 vs 相对自身历史的异常,文献里怎样拆、窗口多长、两段各自的预测力

**能摘到的处理方式:**

1. **区分"量的水平"(持久的、规模/流动性代理)与"量的冲击"(相对自身近期历史不寻常)是这支文献最核心的
   处理动作,两者方向相反。** 用 NYSE 日频/周频数据构造的处理是:把每只股票过去 50 个交易日(或 10 周)
   窗口内,当天(或当周)的成交额在窗口内的**秩**排到前 10% 记为"高量",后 10% 记为"低量",其余记为"正常"
   ——这是一个**窗口内排名**,不是回归残差,也不是简单的均值差。构造出的"高量−低量"零投资组合,在随后约
   20 个交易日(约一个月)里持续获得正收益,且这个效应**在没有伴随异常收益的样本里更强**(即与收益自相关
   正交),持续时间长达 100 个交易日(20 周)。翻成算子语言:这正是 `cross_zscore` / 秩版本的构造思路——
   `cross_rank(day_sum(Amt), 50)`(或等价的 `cross_zscore(day_sum(Amt), 50)` 配合阈值化)测的就是"今天的量
   在自己过去 50 天里排第几",而不是绝对水平。这与 analysis.md §5.1 外围建议(1)"新息:今天的重心相对自己
   20 日基准"的方向完全一致,只是 GKM 的原始构造用的是**量的水平**而不是量的**时点**;如果要把这个证据
   直接搬给核心 A,需要先确认文献里"量冲击"预测的是量本身的未来收益效应,不是重心这个二阶统计量的效应——
   这是类比,不是文献里现成的结论,要跟 PI 说清楚。[GKM2001]

2. **用"过去 6 个月趋势"定义的"相对趋势的异常成交量"是另一种窗口更长的新息构造**,与收益偏度(而不是
   收益水平)挂钩:相对过去 6 个月趋势的成交量上升,配合过去 36 个月正收益,预测随后的**负偏度**(崩盘风险
   上升)。这是一个"长期水平(6 个月趋势)+ 短期冲击(相对趋势的新息)"两层构造,且预测的落点是偏度而不是
   均值。翻成算子语言:`sub(day_sum(Amt), cross_mean(day_sum(Amt), 120))` 这类"相对半年趋势"的写法比
   `cross_zscore(·, 20)` 这种一个月窗口的写法,在文献里对应的是不同的预测标的(偏度 vs 收益均值),外围
   如果想要新息,需要先决定是对标哪一种预测力,不能把两种窗口混在一个判决标准里。[CHS2001]

3. **成交活跃度的二阶矩(波动)而不是水平,文献里报告的是与截面收益**负向**的关系**,且控制了规模、
   账面市值比、动量后依然存在:换手率 / 成交额波动率越高,预期收益越低。这条提示 Q1 的 `day_gini(Amt)`
   构造(量集中度)如果滚动化成 `cross_std(day_gini(Amt), 20)`(集中度本身的波动),方向上应该参照"活跃度
   二阶矩为负"这个已知异象去做先验检查,而不是假设新方向。[CSA2001]

4. **把"量"和"收益自相关"的关系按"风险分担交易 vs 投机交易"分解,是比单纯"水平 vs 新息"更细的一层
   处理**:高量伴随的收益自相关由投机(信息)交易主导、倾向于延续,低量伴随的收益自相关由风险分担交易
   主导、倾向于反转;原始构造里还把量和收益序列各自拆成"系统性成分"(跨股票共同变动的部分)与"非系统性
   成分"(个股特有部分)。翻成算子语言:这建议外围的"新息"不要只对 `day_centroid(Amt)` 本身做
   `cross_zscore`,还可以先用 `cs_bucket_demean(day_centroid(Amt), cross_mean(day_sum(Amt), 30))`
   这类按流动性分桶去均值的写法,把"全市场共同的重心漂移"(系统性)和"个股特有的重心异常"(非系统性)
   分开——这与 analysis.md §5.1 外围建议(2)"条件化"是同一个思路,文献提供的是机制支撑而不是新写法。
   [LMSW2002]

5. **换手率本身作为"水平"类特征,在动量文献里被发现与收益的关系依赖于方向(赢家 vs 输家)**:高换手率的
   赢家比低换手率的赢家反转更快,高换手率的输家比低换手率的输家反转也更快——换手率在这里不是独立预测
   变量,而是调节已知动量效应衰减速度的变量。这条提示:如果外围把 `cross_mean(day_sum(Amt), 30)`(已是
   控制变量)之外的换手率变体当"新信息"检验,应该先按方向(多头 vs 空头腿)分别看,而不是统一看多头腿,
   否则容易把"换手率调节动量衰减"误读成"换手率本身有 alpha"。[LS2000]

**搜不到 / 拿不准,不用:**
- 没搜到专门针对**中国 A 股**的"异常换手率"(abnormal turnover)截面预测力检验、且控制了本环境用到的
  5 个控制变量的论文;GKM2001 和 CHS2001 都是美股证据,这条类比的跨市场有效性没有直接文献支撑。
- 没搜到把"时间加权重心"本身(而不是水平)做"持久 vs 新息"拆分的论文,Q2 的落点(核心 A 的外围"持久 vs
  新息")目前只能用"量的水平"类文献做类比,结构层面(重心是比值、有界于 [0,1],量的水平是无界的)是否
  能直接套用同一套窗口选择,文献没有现成答案,这条按"类比、非直接证据"向 PI 说明。
- 滚动 z 分数的"窗口长度如何选"这个具体问题(20 日 vs 60 日 vs 更长),文献里给出的窗口五花八门
  (GKM 用 50 天 / CHS 用 6 个月),没有一篇专门比较不同窗口对本环境这类有界比值特征的影响,这条不用。

---

## Q3 —— tick 规则日内成交量不平衡,在中国 A 股:归一化基准、预测期限、分组条件化、大单小单

**能摘到的处理方式:**

1. **"买卖不平衡"几乎总是被归一化成比例,而不是带量纲的差值**,这与 analysis.md §3 指出的"烂部件"
   (`day_signed_ratio(Amt, Ret)` 退化成接近常数)正好相反方向地提醒:核心 B
   `day_signed_ratio(Ret, Volume)` 本身已经是比例形式(`sum(|Volume|·sign(Ret))/sum(|Volume|)`,
   [-1,1]),这正是文献里的标准写法——用日内数据构造的"买卖订单不平衡"预测多个区间(1 分钟到 90 分钟)
   的收益,这类文献把不平衡定义为 (买量−卖量)/(买量+卖量) 这种比例,而不是原始差值。[NNW2015]

2. **预测期限:中国 A 股的证据集中在日内短区间(分钟到 1.5 小时),不是日频或更长**,持续到当天剩余时间内
   都显著,作者把这读成市场无效率的证据而不是结构性 alpha 来源。另一篇用早盘买卖比例预测日内价格发现的
   研究报告,不平衡的波动率在**开盘**附近最高,**早盘**的不平衡对日内价格发现的预测力显著强于当天剩余
   时段(作者原话:早盘信息"主导了"当天剩余时段揭示的信息)。翻成算子语言:这两条一起提示,核心 B 如果要
   在本环境的日频奖励下有效,外围应该优先尝试"只用开盘段构造的不平衡"(例如限定在前若干分钟的
   `day_signed_ratio`),而不是全天平均后的版本——全天平均可能把早盘最强的信号和尾盘较弱的信号混在一起,
   稀释掉早盘那部分。[NNW2015][ZWB2011]

3. **日频/更长期限上,文献报告的是"同期正相关、滞后负相关"这个符号翻转,而不是单调预测**:市场层面的
   日度订单不平衡同期推动收益,但不能预测次日收益;个股层面扩展后发现同期不平衡与收益正相关,**滞后**
   不平衡与当期收益**负相关**,作者将其解读为价格压力的均值回复(做市商库存效应),而不是信息效应。
   这条是核心 B 外围建议(d)"不平衡的持续性"的风险提示:如果外围把 `day_signed_ratio(Ret, Volume)`
   做成 20 日内"同号比例"这种持续性构造,文献证据说这类滞后构造更可能捕捉到的是均值回复(方向应为负),
   而不是延续,方向判断不能想当然。[CRS2002][CS2004]

4. **大单/小单分类后,结论在不同市场、不同样本期互相矛盾,没有一个"大单=知情/小单=知情"的普适结论**:
   美股证据是小单不平衡(散户代理)有显著的"一周买入predict下周正收益、持续 3–4 周后反转"模式,大单
   不平衡呈相反模式;中国 2004–2005 年熊市样本的证据是**中等规模**订单信息含量最高(类比纽约证券交易所
   的隐蔽交易模式);另一篇用上海 A 股高频数据的研究反而报告中国知情交易者在**牛市用小单、熊市用大单**,
   与纽约的"中等规模"模式不同。翻成算子语言:这条直接支持 analysis.md §5.2 外围建议(c)"大单与小单侧
   分开"的方向是对的,但**具体该分出哪一档**(按成交额分位数切几档、牛熊市场状态是否要交互)没有统一
   答案,外围如果要做大小单分离,应该把市场状态(例如用 `cross_mean(day_sum(Amt), 60)` 的趋势或
   `cross_quantile` 滚动分位数代理牛熊)当交互项,而不是假设固定的大小单阈值。[COW2011][LLS2014]

5. **预测力随流动性/波动分组条件化这件事,文献里直接给出了"开盘不平衡"这个场景下的条件化依据**:ZWB2011
   的早盘不平衡预测力结果本身就是在"日内价格发现"框架下按时段条件化得出的,不是在波动或流动性十分位
   桶内条件化;流动性 / 波动分桶内条件化这个具体处理方式(对应 analysis.md §5.2 外围建议(b)"在波动/
   流动性桶内取秩"),文献里能查到的证据来自更一般的市场微观结构文献(做市商库存模型),不是专门针对
   `day_signed_ratio` 这类构造的检验,这条按类比处理,不单独列出处。

**搜不到 / 拿不准,不用:**
- 没搜到任何一篇文献**明确报告中国 A 股订单不平衡的预测力在 2018–2021 与 2022 年之后不同**(分段样本期
  结果);这正是 analysis.md §5.2 判决建议最关心的问题(r1 的 train 腿 ≈ 0、valid 腿 +1.3…+2.3),文献
  搜不到直接证据,这条按"搜不到"处理,不能把文献的沉默当成"稳定"或"不稳定"的证据,判决只能继续依赖
  本环境自己的样本内结果。
- 没搜到专门比较"tick 规则"(用价格变动方向代理买卖方向,即 `sign(Ret)`)与真实逐笔买卖盘标记,在**中国
  A 股**数据上分类准确率差多少的论文;美股的 Lee-Ready / tick rule 准确率对比(Nasdaq 约 77–81%)不能
  直接当作 A 股的准确率,这条按"跨市场类比、非直接证据"向 PI 说明,不要把美股的 80% 准确率当成 A 股
  `sign(Ret)` 代理买卖方向的可信度。
- 路径效率(`day_signed_ratio(Ret, Ret)`,即 analysis.md §5.2 用来验证"信息在成交量那一侧"的对照量)
  对应的是技术分析里的 Kaufman 效率比率(累计变化 / 逐步变化绝对值之和),这是交易员手册(Kaufman,
  *Smarter Trading*,1995)里的构造,不是学术论文/工作论文/研究报告,按规则不计入「出处」,只作为
  背景说明:它和 `day_signed_ratio(Ret, Volume)` 的差值能分离"价格路径本身的效率"与"量的净方向"这两
  个信息源,这点在 analysis.md 里已经由 PI 自己提出,文献没有独立佐证,也没有反驳。

---

## Q4 —— 非单调 / 分段特征与线性中性化的相互作用;A 股低价/微盘溢价与非单调结构

**能摘到的处理方式:**

1. **线性正交化之后残留非线性暴露这件事,文献里的标准应对不是"用更高阶多项式回归",而是换成非参数方法,
   并明确报告"线性方法漏掉了非线性"这个诊断结果本身。** 用自适应分组 LASSO 做非参数估计,检验哪些特征
   对截面预期收益有独立信息量的研究发现:很多此前被认定独立有效的特征,在非参数设定下**不再提供增量
   信息**,且非线性效应**是重要的**;样本外解释力高于线性面板回归,夏普比率提升约 50%。翻成算子语言:
   这直接支持 analysis.md §3 把"折叠 V 形""分段门槛"这类结构标记为"线性中性化去不掉"的判断——文献
   证实的正是这件事的反面案例(线性设定系统性遗漏非线性),而不是反驳;对应到 R 组的判决上,`cs_bucket_rank`
   /`cs_bucket_zscore`(在某控制的十分位桶内再排名/标准化)是这篇文献隐含推荐的"替代方案"之一(非参数、
   按组条件化,而不是一次性线性回归残差)。[FNW2020]

2. **"折叠/V 形/门槛"这类特征与线性中性化的冲突,有专门的统计检验可以在样本内直接验证,而不是只能靠
   讲机制:单调性检验。** 该检验专门针对"理论预测单调关系、但样本里可能不单调"的场景构造(贝塔分十档
   排序的 CAPM、期限结构、动量/反转的分组收益),检验结果显示:**规模分组的收益递减关系、短期反转、动量
   效应,在 1963 年后样本里都没能通过单调性检验**——即这些"教科书单调"的异象,严格检验下其实是非单调
   或分段的。翻成算子语言:这既是一个**方法**(可以用来验证 analysis.md §2 族 I "市值 V 形"的判断是否
   成立,而不是只靠 `_lexi`/`sqrt(|·|)` 源码推断),也是一个**先验**(连规模效应这种最成熟的异象都可能
   非单调,族 I 的候选如果声称自己是"单调的市值效应",需要更强证据)。[PT2010]

3. **把"按市值十分位折叠、只在某个分位带选股"这类非单调结构,用标准的"剔除最小 30%"而不是线性中性化
   去处理,是中国市场文献里对"壳价值"扭曲的实际做法。** 剔除按市值最小的 30% 公司(约占总市值 7%)后
   构造规模因子的研究报告:未剔除时,A 股最小一档公司的壳价值(被借壳上市的控制权价值)能解释其市值的
   相当一部分,这部分价值与基本面无关,线性中性化对市值取残差去不掉这种"只在最小一档出现"的非线性
   溢价。翻成算子语言:这支持 analysis.md §3 把 `cs_last_low40(LogFloatCap, ·)` 这类"只锁定市值最低
   一端"的构造标记为"族 I 的市值 V 形押注"而不是信息——文献证实的正是"最小一档"这个位置本身携带一个
   与线性市值暴露无关的壳价值溢价,如果族 I 的多头腿落在这个位置,很可能是在复刻这个已知的、与基本面
   无关的溢价,而不是新信息。[LSY2019]

4. **"低价股溢价"在美股上是一个确认了的、但**原始排序会低估真实幅度**的异象,中国的方向可能相反。**
   美股证据:按**原始**名义股价排序会因为"价格与预期收益的机械联系"而低估真实的低价溢价幅度;用会计
   每股变量(资产、账面值、盈利、股息)构造的"拟合价格"排序后,低价股相对高价股的四因子 alpha 约
   85–88 个基点/月,原始价格排序没有预测力。翻成算子语言:这提示如果族 II/III 的候选想检验"低价股溢价"
   是否是新信息(而不是市值/流动性的重写),不能直接用 `Close` 或 `Open` 的原始水平排序,需要先构造一个
   "用基本面/流通股本预期应该是多少价"的基准,再看偏离——这比 analysis.md §2 族 II 用到的
   `cs_normalize(day_open(Open))` 更进一步,`cs_normalize` 只是截面标准化,不是"拟合价格"残差。
   **方向上的重要提醒:一篇专门做中国市场的研究报告,低价股溢价在中国是正的(越便宜预期收益越高),
   方向与美股一致,但作者把它归因于现金流贝塔(低价股现金流风险更高),而不是美股文献里的"投资者对低价股
   过度乐观"这个行为金融学解释**——这条如果属实,说明即使族 II/III 的多头腿真的在赚"低价溢价",这个
   溢价在中国可能是**风险补偿**而不是**错误定价**,不构成"这是信息、应该继续挖"的证据,反而更支持
   "这是一个已知的规模/困境代理,奖励函数没有对应的控制,应该当代理处理"的判断。[BW2016][Zhang2023]

5. **按行业/板块分组内再排名,是文献里处理"组间效应淹没组内效应"的标准动作,但不是无条件更优。**
   把一个特征的预测力拆成"行业间差异"和"行业内个股差异"两部分的研究报告:行业内部分通常信息量更大,
   这是多头-空头投资者应该对冲掉行业暴露的依据;但对纯多头策略,结论相反——纯多头投资者平均而言**不该**
   做行业中性化。**这条对本环境的奖励口径(纯多头十分位书)是一个直接、需要澄清给 PI 的提醒**:
   analysis.md §4.4 提到的"按 `BoardCode` 分组"建议,如果参照这篇文献的纯多头结论,方向可能是反的
   ——文献里纯多头不做行业中性化反而更好,不是"应该先按板块分组内标准化"。[EHL2023]

**搜不到 / 拿不准,不用:**
- 没搜到专门针对**A 股、剔除 ST/退市风险尾部之后**的"低价但不是最低价"这种非单调结构的论文(即"便宜但
  不是最便宜"这个具体形状);Zhang2023 和 BW2016 都是线性方向的"越便宜预期收益越高",不是非单调的
  "中间价位最优"结构,这条按"搜不到"处理,analysis.md §2 族 II 如果要论证"均值落在第 89 百分位、不是
  最低价"这个具体非单调形状,目前没有文献可以直接引用,只能靠本环境自己的相关度表和持仓构成验证。
- 没搜到把"`cs_bucket_rank` 式十分位桶内条件化"与"线性中性化回归残差"做**直接数值对比**(同一个数据集
  同一个特征算两种方法再比较残留暴露量)的论文;FNW2020 证实了非参数方法整体更优,但不是针对
  `cs_bucket_rank` 这个具体算子的检验,这条按"方法论上的合理类比",不是逐字对应的文献证据。
- ST 标记、退市风险本身作为一个独立的非单调门槛特征(而不是市值/价格的副产品),在 2023-08-08 之前的
  英文文献里几乎搜不到专门检验,中文文献检索也没有展开(规则里英文/中文文献搜索工具的覆盖面本身对中文
  期刊较弱),这条按"搜不到"处理,不构成族 III "ST/退市尾部"判断的独立证据。

---

## 出处列表

**[AP1988]**
标题:A Theory of Intraday Patterns: Volume and Price Variability
作者:Anat R. Admati, Paul Pfleiderer
年-月:1988(*Review of Financial Studies*, Vol. 1, No. 1, pp. 3–40)
来源:期刊(Review of Financial Studies)
链接:https://ideas.repec.org/p/stl/stlewp/95-11.html(引用该文的 RePEc 条目);期刊原文需机构订阅
verified: true(WebSearch 多个独立来源——IDEAS/RePEc、Kobe University 工作论文引用页、Cardiff 大学 ORCA
机构库——一致确认标题、作者、期刊卷期与核心结论;原文全文未直接打开,机制描述依据二级来源转述)

**[H2010]**
标题:Intraday Patterns in the Cross-Section of Stock Returns
作者:Steven L. Heston, Robert A. Korajczyk, Ronnie Sadka
年-月:2010(*Journal of Finance*, Vol. 65, No. 4, pp. 1369–1407)
来源:期刊(Journal of Finance);工作论文版本在 arXiv(ar5iv 镜像)
链接:https://ar5iv.arxiv.org/html/1005.3535 ;Kellogg 官方介绍页
https://www.kellogg.northwestern.edu/academics-research/research/detail/2010/intraday-patterns-in-the-cross-section-of-stock-returns
verified: true(与 r1/lit.md 同一出处,本轮 WebSearch 再次独立命中并确认)

**[RZ2010]**
标题:Recurrence interval analysis of trading volumes
作者:Fei Ren, Wei-Xing Zhou
年-月:2010-02(arXiv:1002.1653,首版提交 2010-02-06)
来源:工作论文(arXiv 预印本)
链接:https://arxiv.org/abs/1002.1653 ;https://arxiv.org/pdf/1002.1653
verified: true(WebFetch 直接打开 arXiv 摘要页,确认标题、作者、提交日期、摘要内容)

**[LY2022]**
标题:Last hour momentum in the Chinese stock market
作者:Lu Yang(Shenzhen University)
年-月:2022(*China Finance Review International*, Vol. 12, No. 1, pp. 69–100;收稿 2021-06-06,
录用 2021-09-09)
来源:期刊(China Finance Review International, Emerald)
链接:DOI 10.1108/CFRI-06-2021-0106 ;PDF 副本
https://www.acem.sjtu.edu.cn/ueditor/jsp/upload/file/20230705/1688558855821058862.pdf
verified: true(Read 工具直接解析 PDF 前 3 页图像,确认标题、作者、摘要、数据期间 2012-05-28~2017-12-31、
T+1 机制表述原文、R² 与夏普比率数值)

**[GKM2001]**
标题:The High-Volume Return Premium
作者:Simon Gervais, Ron Kaniel, Dan Mingelgrin
年-月:2001(*Journal of Finance*, Vol. 56, No. 3, pp. 877–919);工作论文版本 1998-01(首版)/
1998-12(本次读取版本)
来源:期刊(Journal of Finance);Wharton Rodney L. White Center 工作论文 001-99
链接:https://rodneywhitecenter.wharton.upenn.edu/wp-content/uploads/2014/04/9901.pdf
verified: true(Read 工具直接解析工作论文 PDF 前 9 页图像,确认标题、作者、摘要、50 天/10 周窗口排名
构造公式 (2)、零投资组合构造公式 (3)(4)、20 个交易日测试期与 100 个交易日的效应持续性)

**[CSA2001]**
标题:Trading activity and expected stock returns
作者:Tarun Chordia, Avanidhar Subrahmanyam, V. Ravi Anshuman
年-月:2001(*Journal of Financial Economics*, Vol. 59, No. 1, pp. 3–32)
来源:期刊(Journal of Financial Economics)
链接:https://research.iimb.ac.in/fac_pubs/1268 ;https://academicnewsletter.sufe.edu.cn/info/357854
verified: true(WebSearch 多个独立来源——IIMB 机构知识库、学术快讯摘要——一致确认标题、作者、期刊卷期、
核心结论原文措辞)

**[CHS2001]**
标题:Forecasting Crashes: Trading Volume, Past Returns, and Conditional Skewness in Stock Prices
作者:Joseph Chen, Harrison Hong, Jeremy C. Stein
年-月:2000-11(NBER Working Paper No. 7687,首版);正式发表 2001(*Journal of Financial Economics*,
Vol. 61, No. 3, pp. 345–381)
来源:工作论文(NBER)+ 期刊(Journal of Financial Economics)
链接:https://www.nber.org/papers/w7687 ;https://web.mit.edu/jcstein/www/for-crash.pdf
verified: true(WebSearch 多个独立来源——NBER 官方页、MIT Stein 个人主页 PDF、Harvard Stein 学术页——
一致确认标题、作者、核心结论:6 个月趋势成交量上升 + 36 个月正收益预测负偏度)

**[LS2000]**
标题:Price Momentum and Trading Volume
作者:Charles M. C. Lee, Bhaskaran Swaminathan
年-月:2000-10(*Journal of Finance*, Vol. 55, No. 5, pp. 2017–2069)
来源:期刊(Journal of Finance)
链接:https://www.kellogg.northwestern.edu/academics-research/research/detail/2000/price-momentum-and-trading-volume
verified: true(WebSearch 多个独立来源——Kellogg 官方介绍页、IDEAS/RePEc、作者个人主页 PDF——一致确认
标题、作者、卷期、核心结论)

**[LMSW2002]**
标题:Dynamic Volume-Return Relation of Individual Stocks
作者:Guillermo Llorente, Roni Michaely, Gideon Saar, Jiang Wang
年-月:2002(*Review of Financial Studies*, Vol. 15, No. 4, pp. 1005–1047);工作论文版本
NYU FIN-00-032(2000-08)
来源:期刊(Review of Financial Studies)+ 工作论文(NYU)
链接:https://img.nber.org/papers/w8312 ;https://archive.nyu.edu/handle/2451/26698
verified: true(WebSearch 多个独立来源——NBER、NYU 机构知识库、John Cochrane 个人网站 PDF——一致确认
标题、作者、卷期、核心机制表述)

**[BCS1998]**
标题:Alternative factor specifications, security characteristics, and the cross-section of expected
stock returns
作者:Michael J. Brennan, Tarun Chordia, Avanidhar Subrahmanyam
年-月:1998(*Journal of Financial Economics*, Vol. 49, No. 3, pp. 345–373)
来源:期刊(Journal of Financial Economics)
链接:https://ideas.repec.org/a/eee/jfinec/v49y1998i3p345-373.html
verified: true(WebSearch 多个独立来源——IDEAS/RePEc、学术快讯摘要、后续引用论文——一致确认标题、作者、
卷期;具体用到"价格""换手"作为特征这一点来自摘要级描述,未读全文方法细节)

**[NNW2015]**
标题:Do order imbalances predict Chinese stock returns? New evidence from intraday data
作者:Paresh Kumar Narayan, Seema Narayan, Joakim Westerlund
年-月:2015(*Pacific-Basin Finance Journal*, Vol. 34, pp. 136–151)
来源:期刊(Pacific-Basin Finance Journal)
链接:https://ideas.repec.org/a/eee/pacfin/v34y2015icp136-151.html ;RMIT 机构知识库
https://research-repository.rmit.edu.au/articles/journal_contribution/Do_order_imbalances_predict_Chinese_stock_returns_New_evidence_from_intraday_data/27477654
verified: true(与 r1/lit.md 同一出处,本轮 WebSearch 再次独立命中并确认标题、作者、卷期、1 分钟至
90 分钟预测期限这一结论)

**[ZWB2011]**
标题:Order Imbalance and Intraday Price Discovery: Evidence from Chinese Stock Markets
作者:Zhaohui Zhang, Jiamin Wang, Ronald Bremer
年-月:2011(*Review of Pacific Basin Financial Markets and Policies*, Vol. 14, No. 4, pp. 693–714)
来源:期刊(Review of Pacific Basin Financial Markets and Policies)
链接:https://ideas.repec.org/a/wsi/rpbfmp/v14y2011i04ns0219091511500019.html
verified: true(WebFetch 直接打开 IDEAS/RePEc 条目页,确认标题、完整作者名、卷期页码、DOI 与摘要核心
结论原文措辞)

**[CRS2002]**
标题:Order imbalance, liquidity, and market returns
作者:Tarun Chordia, Richard Roll, Avanidhar Subrahmanyam
年-月:2002(*Journal of Financial Economics*, Vol. 65, No. 1, pp. 111–130)
来源:期刊(Journal of Financial Economics)
链接:https://www.cis.upenn.edu/~mkearns/finread/Chordia_buy-sell_orders.pdf
verified: true(WebSearch 多个独立来源——UPenn 课程阅读材料 PDF、IDEAS/RePEc、学术快讯摘要——一致确认
标题、作者、卷期、核心结论原文措辞)

**[CS2004]**
标题:Order imbalance and individual stock returns: Theory and evidence
作者:Tarun Chordia, Avanidhar Subrahmanyam
年-月:2004(*Journal of Financial Economics*, Vol. 72, No. 3, pp. 485–518;在线记录 DOI
10.1016/S0304-405X(03)00175-2,工作论文草稿 2002-10)
来源:期刊(Journal of Financial Economics)
链接:https://ideas.repec.org/p/cdl/anderf/qt34k8f3pv.html
verified: true(WebSearch 多个独立来源——IDEAS/RePEc、UCLA Anderson 工作论文页、台湾大学机构知识库引用
该文的硕士论文——一致确认标题、作者、卷期、"同期正相关、滞后负相关"这一核心结论)

**[BOZ2009]**
标题:Do Retail Trades Move Markets?(工作论文阶段曾用名 "Do Noise Traders Move Markets?")
作者:Brad M. Barber, Terrance Odean, Ning Zhu
年-月:2009(*Review of Financial Studies*, Vol. 22, No. 1, pp. 151–186)
来源:期刊(Review of Financial Studies)
链接:https://haas.berkeley.edu/wp-content/uploads/Noise.pdf ;
https://ideas.repec.org/a/oup/rfinst/v22y2009i1p151-186.html
verified: true(WebSearch 多个独立来源——UC Berkeley Haas 工作论文 PDF、IDEAS/RePEc、学术快讯摘要——
一致确认标题、作者、期刊卷期、TAQ/ISSM 小单不平衡与散户数据相关、3–4 周后反转这一结论)

**[KST2008]**
标题:Individual Investor Trading and Stock Returns
作者:Ron Kaniel, Gideon Saar, Sheridan Titman
年-月:2008(*Journal of Finance*, Vol. 63, No. 1, pp. 273–310)
来源:期刊(Journal of Finance)
链接:https://ideas.repec.org/a/bla/jfinan/v63y2008i1p273-310.html ;
https://www.johnhcochrane.com/s/kaniel_saar_titman_trading_and_returns.pdf
verified: true(WebSearch 多个独立来源——IDEAS/RePEc、John Cochrane 个人网站 PDF、NYU 机构知识库——
一致确认标题、作者、卷期、"散户净买入预测次月正超额收益"这一核心结论)

**[COW2011]**
标题:The Bear Market In China: Which Trades Push The Stock Prices Down?
作者:Jinghan Cai, Hongbing Ouyang, Michael Chak Sham Wong
年-月:2011(*Annals of Financial Economics*, Vol. 6, No. 1, pp. 1–22)
来源:期刊(Annals of Financial Economics)
链接:https://ideas.repec.org/a/wsi/afexxx/v06y2011i01ns2010495211500023.html
verified: true(WebSearch 命中 IDEAS/RePEc 条目,确认标题、作者、卷期、2004-06~2005-05 样本期、
"中等规模订单信息含量最高"这一核心结论)

**[LLS2014]**
标题:An Empirical Study on the Stealth Trading in Shanghai A Stock Market
作者:刘善存(Liu Shancun)、林德强(Lin Deqiong)、宋玉涛(Song Yutao)
年-月:2014(《北京航空航天大学学报(社会科学版)》,Vol. 27, No. 1, pp. 68–75)
来源:期刊(Journal of Beijing University of Aeronautics and Astronautics, Social Sciences Edition)
链接:https://bhxb.buaa.edu.cn/bhsk/en/article/id/9572
verified: true(WebFetch 直接打开期刊英文摘要页,确认标题、作者、卷期页码、"牛市用小单、熊市用大单,
与纽约的中等规模模式不同"这一核心结论原文措辞)

**[BW2016]**
标题:Nominal price illusion(工作论文阶段曾用名 "The Nominal Price Premium")
作者:Justin Birru, Baolian Wang
年-月:2016(*Journal of Financial Economics*, Vol. 119, No. 3, pp. 578–598);工作论文摘要日期
2016-03
来源:期刊(Journal of Financial Economics)
链接:https://www.ivey.uwo.ca/media/3775564/birru.pdf ;作者 CV
https://fisher.osu.edu/~birru.2/
verified: true(WebSearch 多个独立来源——Ivey Business School 工作论文 PDF、作者 Ohio State 个人学术页
CV、IDEAS/RePEc——一致确认标题、作者、期刊卷期、"拟合价格"构造与 85–88bp/月 的核心结论)

**[Zhang2023]**
标题:Betting against low nominal prices: Evidence from China
作者:Bing Zhang
年-月:2023-06(DOI 10.1016/j.iref.2023.06.017,按 DOI 的月份前缀推断在线出版约在 2023 年 6 月;
正式卷期 *International Review of Economics & Finance*, Vol. 88, pp. 476–500)
来源:期刊(International Review of Economics & Finance)
链接:https://ideas.repec.org/a/eee/reveco/v88y2023icp476-500.html
verified: true(WebFetch 直接打开 IDEAS/RePEc 条目页,确认标题、作者、卷期页码、DOI、摘要核心结论:
中国低价股溢价为正、归因于现金流贝塔而非美股式的投资者乐观偏差;**日期置信度低于其余条目**——
只确认到月,没有确认到具体日期,DOI 月份前缀通常对应在线出版月份,按此推断早于 2023-08-08,但请 PI
知悉这条的日期判断是推断而非直接读到的出版日戳)

**[LSY2019]**
标题:Size and Value in China
作者:Jianan Liu, Robert F. Stambaugh, Yu Yuan
年-月:2019(*Journal of Financial Economics*, Vol. 134, No. 1, pp. 48–69);NBER Working Paper
No. 24458(工作论文版本)
来源:期刊(Journal of Financial Economics)+ 工作论文(NBER)
链接:https://repository.hku.hk/bitstream/10722/273695/1/content.pdf ;
https://www.nber.org/papers/w24458
verified: true(WebSearch 多个独立来源——香港大学机构知识库全文 PDF、NBER 官方页、作者所在高校学术
新闻页——一致确认标题、作者、期刊卷期、"剔除最小 30%、约占总市值 7%"这一核心数字)

**[PT2010]**
标题:Monotonicity in asset returns: New tests with applications to the term structure, the CAPM,
and portfolio sorts
作者:Andrew J. Patton, Allan Timmermann
年-月:2010(*Journal of Financial Economics*, Vol. 98, No. 3, pp. 605–625)
来源:期刊(Journal of Financial Economics)
链接:https://public.econ.duke.edu/~ap172/Patton_Timmermann_sorts_JFE_Dec2010.pdf
verified: true(WebSearch 多个独立来源——作者 Duke 个人主页全文 PDF、Duke 经济系教职数据库、CAS
摘要页——一致确认标题、作者、期刊卷期、"规模分组收益递减关系在 1963 年后样本未通过单调性检验"这一
核心结论)

**[FNW2020]**
标题:Dissecting Characteristics Nonparametrically
作者:Joachim Freyberger, Andreas Neuhierl, Michael Weber
年-月:2020(*Review of Financial Studies*, Vol. 33, No. 5, pp. 2326–2377);NBER Working Paper
No. 23227(工作论文版本,首版 2017 年前后)
来源:期刊(Review of Financial Studies)+ 工作论文(NBER)
链接:https://papers.ssrn.com/abstract=2935432 ;https://www.nber.org/papers/w23227
verified: true(WebSearch 多个独立来源——SSRN、NBER 官方页、清华五道口金融学院学术预告页——一致确认
标题、作者、期刊卷期、"自适应分组 LASSO""样本外解释力提升、夏普比率提升约 50%"这一核心结论;具体
50% 这个数字在不同版本的摘要里有出入(更早的研讨会预告写 70%),按最终发表版摘要的 50% 为准,已在
正文标注)

**[EHL2023]**
标题:Is Sector Neutrality in Factor Investing a Mistake?
作者:Sina Ehsani, Campbell R. Harvey, Feifei Li
年-月:2023-07(*Financial Analysts Journal*, Vol. 79, No. 3, pp. 95–117;工作论文版本据二级来源
提示约 2021 年已有稿件流传,但本次核实的是期刊版)
来源:期刊(Financial Analysts Journal)
链接:https://ideas.repec.org/a/taf/ufajxx/v79y2023i3p95-117.html ;作者个人主页工作论文 PDF
https://people.duke.edu/~charvey/Research/Published_Papers/P165_Is_sector_neutrality.pdf
verified: true(WebFetch 直接打开 IDEAS/RePEc 条目页,确认标题、作者、期刊卷期页码、出版月份
2023 年 7 月(早于 2023-08-08 截止日,但页面未给出具体日期)、摘要核心结论:纯多头投资者平均不应该做
行业中性化、多空投资者应该)
