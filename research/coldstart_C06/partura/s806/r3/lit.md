# 文献:种子 806,C 组(Partura),第 3 轮(文献员)

读入:`r3/analysis.md` §6 的四个题目,对准核心 1 `sub(day_centroid(Amt), day_centroid(Ret))`(量的时点与价格位移的
时点之差)、核心 2 `day_centroid(Ret)`(价格在一天里什么时候动,及开盘段/隔夜的处理)、N 灵感 1(隔夜 vs 日内的拔河)、
族 VI 的判定(日内收益自相关类统计量是否是流动性/价格离散度的非线性重写)。只用 WebSearch / WebFetch 查到、且能确认
**首版/在线/印刷日期在 2023-08-08 之前**的论文、工作论文或研究报告;日期拿不准或访问被拒(如 SSRN 多次 403)的,
在各节「搜不到 / 拿不准,不用」里写明,不编造数值、不编造没有亲眼读到的具体结论。

算子定义按本环境 `AlphaCube`(`src/alphacube/operators/dt_day.py`)与 `Partura`(`partura/ops_ext.py`)的实现:
`day_centroid(x) = sum(t·|x_t|)/sum(|x_t|)/(T-1)`(按分钟序号归一化到 [0,1] 的时间加权重心,0=全在开盘、1=全在
收盘、0.5=对称);核心 1 是 `day_centroid(Amt)`(成交额的时间重心)减 `day_centroid(Ret)`(**以 |分钟收益| 为权重**
的时间重心,即「绝对收益加权时间重心」);`day_open(x)` = 当日第一个有效分钟值(若第 0 根含隔夜跳空,则读到的是
隔夜段);`day_ar1_coefficient(x)` 是逐行 OLS 一阶自相关系数;`day_q_stat_std(x, max_lag=20)` 是 Ljung-Box 式
逐 lag 自相关序列的标准差;`day_at_min_ratio(x)` 是当日取到最小值的分钟占比;`cross_mean(x,d)` 是跨日滚动均值。

---

## Q1 —— 核心 1:量的时点 vs 价格位移的时点,文献里怎样分开度量、怎样证明不是流动性代理

**能摘到的处理方式:**

1. **"量的时点"是一个结构性现象,不是噪声,这是把它当特征而不是当随机巧合使用的前提。** 做市商理论最早的版本
   证明,知情交易者存在时,无信息的流动性交易者有动机把交易挤到市场厚的时段以降低被"吃价差"的概率,U 形的
   成交量日内分布由此内生产生,而不是外生给定的。翻成算子语言:这支持把 `day_centroid(Amt)` 本身(核心 1 的
   被减项)当作一个有理论基础、跨股票可比的量,而不是把"时点"当成任意的数据噪声——这是核心 1 这类"时点差"
   构造能成立的前提,而不是它预测收益方向的证据(模型本身不预测收益方向)。[AP1988]

2. **文献几乎从不把"量的水平 × 收益"直接揉成一个协方差标量,而是先分别构造"量往哪个方向集中"与
   "价格变动往哪个方向集中",再比较两者。** 关于价格变动与成交量关系的经典综述指出,量与价格变动幅度
   同期正相关是股票和期货市场里最稳健的实证规律之一,但该综述同时指出,早期几类理论模型(序贯信息到达模型
   vs 混合分布假设模型)对"量领先价"还是"价领先量"这一问题给出的预测并不一致,综述本身没有给出统一的
   领先滞后方向结论。翻成算子语言:核心 1 的构造——分别对 `Amt` 和 `|Ret|` 各算一次时间重心再相减——
   正是这类文献推荐的"先分开度量,再比较位置"的标准路径,而不是 `day_cov(Amt, Ret)` 这种把两者直接乘在一起
   的写法;但"哪一个重心更靠前"预测收益的方向,文献本身没有给出先验,仍需交给 GP 的样本内结果决定。
   [KA1987]

3. **度量"价格发现发生在哪个时段"的标准做法(加权价格贡献度,Weighted Price Contribution, WPC)用的是
   "该时段的净价格变化占全天净价格变化的份额"作权重,而不是逐分钟绝对收益的份额。** 原始构造把每个时段的
   价格贡献度,按当天净价格变化的绝对值做权重平均,以压低极端日对结果的影响。翻成算子语言:这提示核心 2 /
   核心 1 里 `day_centroid(Ret)` 用"逐分钟 |Ret|"作权重,与文献标准的 WPC 构造有一个具体差异——WPC 先按
   分段**求和**价格变化、再取绝对值(段内双向抵消的噪声会被抹掉),而 `day_centroid` 是逐分钟先取绝对值再加权
   平均(段内反复的小波动即使相互抵消,也会被当作"活跃"计入权重)。这不是说哪个更对,而是提醒 PI:
   核心 1 / 核心 2 测的是"价格波动发生的时点",WPC 测的是"价格净位移发生的时点",**两者在横盘震荡的日子里
   会给出不同的读数**,外围如果想对齐 WPC 的证据,需要一个"先分段求和再取绝对值"的变体作对照,而不能假设
   两者等价。[BW1993]

4. **文献里证明"量/价时点特征不是单纯流动性代理"的标准方法,是把它投影到一个独立的、经济含义明确的
   协变量上,看效应是否仍然存在、是否随该协变量系统变化**,而不是直接和流动性做双重排序。一项用 23 个
   新兴市场、1504 只股票的研究,按分段 WPC 衡量"开盘后早段的价格发现"程度,发现它与外资直接持股比例稳健
   相关,作者进一步把外资持股比例投影到"私有信息"与"投资者认知度"两组代理变量上,把残差当作"未知因素"
   的效应,发现私有信息这组代理解释力远大于认知度和未知因素。翻成算子语言:这是"分组条件化 + 回归取残差"
   的具体做法——如果核心 1 要回应"这是不是流动性代理"的质疑,可以类比地把 `sub(day_centroid(Amt),
   day_centroid(Ret))` 投影到换手率、机构持仓比例一类的协变量上,看残差是否仍有横截面方差,而不是只做
   一次线性中性化就宣称完成了控制。[CHKZ2020]

5. **把"量"的时点换成"量的集中/分散程度"是另一条独立于时点方向的构造方式,用来做条件化变量而非新核心**:
   用高频数据算出的成交量时间间隔序列(超过某阈值的量之间的 gap)在中国股票和指数上都服从幂律尾部、有长期
   记忆,大额成交后紧跟大额收益的关联在最大成交量上最强。翻成算子语言:核心 1 的外围如果要做"条件化"
   (只在异常成交日取值,见 analysis.md §5.1 第 3 条),`day_gini(Amt)` 或"超过阈值的成交间隔"是比
   `is_gt0(sub(day_sum(Amt), cross_mean(day_sum(Amt),20)))` 更贴合文献构造的条件变量,可作为对照。
   [RZ2010]

**搜不到 / 拿不准,不用:**
- 没搜到任何论文直接构造"成交量加权时间重心 减 绝对收益加权时间重心"这个差值(或等价的"量领先价/价领先量"
  标量)、并做横截面收益预测检验;这是本环境的原创构造,不是文献里现成的因子,上面 5 条都是"构造方式与
  证明方法"的类比支撑,不是"这个因子在别处有效"的直接证据,请 PI 在写计划时把这一点说清楚。
- 关于"量领先价"还是"价领先价"的方向,KA1987 综述本身承认当年的理论模型预测不一致;我搜到的几篇后续
  期货/现货铅后关系研究(如中国沪深 300 期货与现货的领先滞后)衡量的是**两个不同市场**之间的领先滞后,
  不是同一资产"成交量的时点"与"价格位移的时点"之间的领先滞后,结构不同,不能当直接支撑,按"搜不到"处理。
- 没有搜到专门用"同一剖面的高阶矩做对照"(例如用成交量剖面的偏度/峰度去检验时点特征是否只是剖面形状
  的代理)这一具体方法论、针对时间重心类特征的论文;CHKZ2020 的"投影到协变量后取残差"是我能找到的最接近
  的替代方法,偏度/峰度对照这条按"搜不到"处理。

---

## Q2 —— 核心 2 `day_centroid(Ret)`:价格发现时点的度量、开盘集合竞价与隔夜跳空的处理

**能摘到的处理方式:**

1. **"隔夜段"与"日内段"在文献里几乎总是先分开构造再分析,从不把隔夜跳空和开盘后第一根分钟 bar 混在一起
   直接喂给同一个统计量。** 用高频数据在中国市场做的研究,把当日收益显式拆成"隔夜段"(由开盘前集合竞价
   决定)与"开盘后半小时段",发现对下一期收益的预测力几乎全部来自隔夜段,开盘半小时段增量贡献很小;同一篇
   把隔夜段读成"知情机构在隔夜形成的信号",而把日内段读成更多由散户驱动。翻成算子语言:这直接支持
   analysis.md §5.2 (c) 的做法——用 `day_centroid(mul(Ret, greater(in_index(Ret), 0.0)))` 去掉第 0 根再
   和原版相减,把"隔夜跳空混入价格发现时点"这件事单独剥离出来评估,而不是假设第 0 根的隔夜跳空和当日
   日内的分钟波动是同一类信息——这是文献的标准处理,不是本环境特有的权宜之计。[GHLX2019]

2. **度量"价格发现在一天中何时发生"的标准构造(WPC)本身的证据是:价格发现高度集中在开盘后的早段。**
   在 23 个新兴市场的研究里,早段(开盘后)的 WPC 份额系统性高于其他时段,且与外资持股、私有信息代理显著
   相关。翻成算子语言:若 `day_centroid(Ret)` 的横截面分布本身就普遍偏向 0(早段)——这是文献给出的
   "基准形状"预期——那么核心 2 真正有横截面信息含量的,很可能不是水平本身,而是**偏离这个基准形状的
   程度**(即 analysis.md §5.2 (b) 的"相对自身 50 日新息"这条路线,而不是(a)的纯水平路线),这与 r2 轮
   `[H2010]` 的证据(收益延续性集中在两端、不是重心本身)方向一致、互相印证。[CHKZ2020][H2010]
   (H2010 已在 r1/r2 的相关度表与文献里确认,具体细节见 `r1/lit.md` Q1 第 1 条与 `r2/lit.md` Q1 第 3 条,
   不重复摘录核心结论。)

3. **原始 WPC 构造用"该时段净价格变化 / 全天净价格变化绝对值"作权重,这个权重分母本身就是一个"压低极端日
   影响"的归一化,不是简单地把每天都当等权处理。** 这提示:如果核心 2 要和 WPC 一类文献的结论对齐,外围里
   "多日平滑后的水平"(analysis.md §5.2 (a))应该优先在**同样波动水平**的日子内比较(即用波动分桶,见
   (d)),而不是跨波动水平直接平均——否则高波动日的 `day_centroid(Ret)` 读数会被少数极端分钟主导,这恰好
   是 (d) 被列为"本核心最大风险通道"的文献侧理由。[BW1993]

4. **开盘集合竞价本身是不是只在"决定隔夜跳空的大小"上起作用,还是也单独贡献价格发现,文献上有分歧,
   没有定论,这条按"没有统一答案"处理,不要替 PI 下结论。** 一项针对中国创业板的研究发现开盘十分钟集合
   竞价贡献了新股上市首日收益绝大部分的变异(约 95%),但这是 IPO 首日这个特殊场景,不能直接推广到本环境
   的普通交易日场景;一项基于 23 个新兴市场的研究把集合竞价期的价格发现单独列为"该测度在收盘集合竞价/
   隔夜期间是否仍然有效"存疑,提示即便用 WPC 类测度,集合竞价阶段的可靠性本身也是文献里尚有争议的点。
   这两条都只是背景提醒,不构成核心 2 外围构造的直接处理方式。
   [搜不到独立于上述两条、专门针对"A 股开盘集合竞价对日内价格发现的边际贡献"的检验,按拿不准处理]

5. **中国特有的制度背景:T+1 使隔夜收益系统性地带有负偏(与流动性提供者的逆向选择有关),这个负偏不是
   个股特异信息,是全市场共同的结构性漂移。** 一篇用 T+1 与 T+0(股指期货、港股、主要国际指数)对照的研究
   证明,T+1 机制本身导致隔夜收益显著为负,而且这个负偏的大小在"投资者意见分歧更大、风险更高、散户占比
   更高、卖空限制更强、流动性更差"的股票上更明显。翻成算子语言:这条提示核心 2 (c) 把隔夜跳空从
   `day_centroid(Ret)` 里剥离出来是必要的,**而且剥离出来的隔夜那部分本身大概率带有一个和"流动性/风险"
   相关的系统性负偏**——这几个相关维度(风险、流动性、散户占比)和本环境的波动/流动性控制在方向上重叠,
   是核心 2 外围如果误把隔夜段也纳入时点统计,容易把"T+1 结构性负偏"读成"新信息"的一个具体机制性解释,
   补充 analysis.md §5.2「风险」一条的来源。[BZ2020]

**搜不到 / 拿不准,不用:**
- 没搜到专门讨论"收盘集合竞价对日内价格发现贡献度"且针对 A 股、同时控制了被动资金占比的论文;美股/
  欧股被动资金推动收盘量占比上升的证据(BlackRock/SSGA 的报告)是行业白皮书,不是同行评审的截面检验,
  而且 A 股被动占比在样本期内远低于欧美,这条类比的有效性没有直接文献支撑,按"搜不到"处理(与 r2 轮
  Q1 的同一条结论一致,不重复摘录)。
- 没搜到把 `day_centroid(Ret)`(逐分钟绝对收益加权重心)本身与波动控制 `cross_mean(day_std(Ret),20)` 的
  理论关系讲清楚的论文——这正是 analysis.md §5.2 列为"唯一否决通道"的风险点,文献层面(WPC 一类测度是
  有界比值,不是一个无界的二阶矩)只能给出"理论上应该相关度较低"的定性预期,具体数值必须看本轮相关度表,
  这条按规则不能在这里替审计员下结论。
- "加权价格发现贡献 WPDC"这个具体英文术语本身,我搜到的是其更常见的同义构造"weighted price contribution
  (WPC)"(Barclay-Warner 1993 之后的标准叫法),没有搜到一篇单独以"WPDC"这个缩写命名、且独立于 WPC 的
  方法论文献,这条按"等价构造、术语不同"处理,不单列为新处理方式。

---

## Q3 —— N 灵感 1:隔夜 vs 日内的"拔河",客群解释,与 20 日反转控制的正交化

**能摘到的处理方式:**

1. **把收盘到收盘的总收益拆成"隔夜段"(上日收盘到今日开盘)与"日内段"(今日开盘到今日收盘),再分别
   评估每种策略在两段各自的收益,是这支文献的核心处理动作,而不是直接做差。** 对美股 14 种交易策略的检验
   发现,几乎每种策略的收益**完全**来自隔夜段或**完全**来自日内段,且两段符号通常相反;动量类策略的收益
   几乎全部来自隔夜段,其余策略收益几乎全部来自日内段。作者把这个现象读成两类客群对倒:机构倾向日内交易、
   且交易方向与动量特征相反,散户更活跃于隔夜。翻成算子语言:这条文献的标准做法是**分别报告两段各自的
   收益,而不是先验地假设"差值"才是信号**——N 灵感 1 目前的构造 `sub(day_open(Ret), sub(day_sum(Ret),
   day_open(Ret)))` 直接取了差,按文献的标准做法,应该同时评估隔夜段单独、日内段单独、以及差值三者,
   而不是只提交差值这一个候选,因为"拔河"本身说的是两段**分别**有效、方向相反,不是"差值"本身是一个新
   机制。[LPS2019]
   (LPS2019 = Lou, Polk, Skouras 2019, *Journal of Financial Economics*;已在 `r1/lit.md` Q1 第 2 条确认
   过标题、作者、期刊卷期,这里不重复列出处细节,只重新摘录与本轮题目直接相关的处理方式。)

2. **在中国市场,"拔河"现象存在,但方向和美股不同:更多策略的利润来自隔夜段,而不是像美股那样隔夜/日内
   对半分。** 一项专门检验中国 A 股上多种资产定价异象的隔夜/日内收益分解的研究发现,不是所有异象都能在
   日间或隔夜单独获利,且相比美股证据,**更多策略在隔夜段获利**,作者把这归因于中国市场的特有制度结构。
   翻成算子语言:这条提示 N 灵感 1 如果在 A 股上验证"隔夜段"与"日内段"哪个贡献更大,**不能直接套用
   LPS2019 的美股先验**(美股是对半分、符号相反),中国的证据指向隔夜段权重可能系统性更大,这是对
   analysis.md §5.5 第 1 条"机制是客群"这一判断的 A 股侧独立验证,而不只是从美股文献平移过来的类比。
   [LCC2023]

3. **把中国市场隔夜收益的持续预测力归因于"迟到的知情交易"客群,而不是单纯的流动性或风险溢价,是这支
   A 股文献给出的具体机制。** 用中国高频数据做的研究发现,个股层面的日内动量效应强,且这种可预测性几乎
   全部来自隔夜段,开盘半小时段增量贡献很小;可预测性在重大负面信息冲击后变强、正面冲击后变弱,作者将
   隔夜收益解释为一个"知情信号",随后由经验不足或信息劣势的"迟到知情交易者"在隔夜或次日交易中据此行动。
   翻成算子语言:这给 N 灵感 1 的"隔夜段"一个具体的、独立于反转效应的经济机制(信息沿客群扩散的时间差),
   支持 analysis.md §5.5 第 1 条"客群"判断里机构/散户划分之外,还可以补一层"谁先知道、谁后知道"的解释,
   但这条机制本身是方向不对称的(负面冲击后更强),如果要在 GP 里体现,需要额外的非对称项,而不是对称的
   `sub`。[GHLX2019]

4. **中国 A 股隔夜收益系统性为负,根源被归到 T+1 交易规则本身造成的逆向选择,而不是信息或风险溢价。**
   用 T+1(A 股)与 T+0(股指期货、港股、主要国际指数)对照的研究证明,A 股隔夜收益显著为负,而 T+0 的
   同类资产隔夜收益接近零或为正;负偏程度在"投资者意见分歧更大、风险更高、散户占比更高、卖空限制更强、
   流动性更差"的股票上更强。翻成算子语言:这是 N 灵感 1 在做"与 20 日反转控制正交化"之前必须先知道的
   一个**结构性常数项**——如果 `day_open(Ret)` 一侧系统性地比 `sub(day_sum(Ret), day_open(Ret))` 一侧更
   负,这个负偏本身就带有"更高风险、更差流动性"的横截面协变量,和本环境的波动/流动性控制方向重叠;
   analysis.md §5.5 要求的"必查:与 20 日反转控制的 |ρ|"这件事,文献侧给出的提醒是:**即使和反转控制的
   |ρ| 不高,这个因子仍可能和波动/流动性控制有不小的残留相关,这条风险不在 20 日反转这一个控制项里**,
   需要同时看它与 `cross_mean(day_std(Ret),20)` 和流动性控制的 |ρ|,而不仅仅是反转控制。[BZ2020]

5. **怎样与"总收益反转"正交化,文献里给出的是"分别评估两段,而不是对总收益回归取残差"这条路径,我没有
   搜到一篇明确比较"取两段之差"与"对总收益回归取残差"哪个更好的论文。** LPS2019、LCC2023、GHLX2019
   三篇都是分别报告隔夜段和日内段各自的（横截面排序构造的）收益,没有一篇在构造阶段先对"总收益"或某个
   反转特征做回归再取残差——这与 analysis.md §5.5 的差值构造(`sub`)更接近,但"差值"和"分别评估"仍是
   两种不同的处理,前面第 1 条已经指出这个区别,这里再次强调:**文献没有直接回答"哪种正交化方式更好"
   这个具体工程问题**,这是本环境需要自己用相关度表和样本内结果判断的部分,不能归到文献证据里。

**搜不到 / 拿不准,不用:**
- 没有搜到专门报告"隔夜 vs 日内拔河"或"T+1 隔夜负偏"效应在 **2018–2021 与 2022 年之后**存在分段差异
  证据的论文——这类分段检验如果要覆盖 2022 年之后的数据,论文的发表或挂出日期大概率晚于 2023-08-08 的
  截止线,属于按规则本来就不该引用的范围;搜到的几篇(LPS2019、LCC2023、GHLX2019、BZ2020)样本期都停在
  2019 年之前或 2021 年之前,没有一篇直接给出跨越 2022 年的分段结果,这条按"搜不到"处理,不要替 PI 下
  "本环境 2022 年之后会不会失效"的判断。
- 搜到一篇 2024/2025 年发表的、题目直接叫《The Nexus of Overnight Trend and Asset Prices in China》
  (Guo, Han, Li, Li,*Journal of Economic Dynamics and Control*,2025 年卷,2024-11-23 在线),其模型与
  本题高度相关(隔夜客群反应不足、隔夜趋势预测下月收益),但在线日期晚于 2023-08-08 截止线,**按规则不
  使用**,也不采信它对"分段证据"这个具体问题可能给出的答案;与之同主题、但日期更早、确认在线的
  GHLX2019(2019-10)、LCC2023(2023-06)已在上面摘录,供 PI 参考。
- "持有期多长"这个具体问题,LPS2019/LCC2023/GHLX2019 都没有在摘要层面给出一个统一的"推荐持有期"数字
  (它们是横截面排序检验,不是本环境这种带滚动窗口的因子构造),这条不编造具体天数。

---

## Q4 —— 族 VI 的判定:日内收益自相关类统计量是流动性/价格离散度的非线性重写,还是信息

**能摘到的处理方式:**

1. **用"零收益发生的比例"从日频收益反推交易成本,是这支文献最早、最直接的处理方式,原理是:真正的
   新信息只有在预期收益超过交易成本时才会被套利者交易进价格,成本越高,观察到零收益的频率越高。**
   原始构造只需要日频收益序列,把零收益的发生率嵌入一个收益生成模型里,反推出隐含的有效双边交易成本;
   按十分位分组,大市值股票的估计成本约 1.2%,小市值股票约 10.3%(1963–1990,美股)。翻成算子语言:这条
   直接支持族 VI 判定里"零收益比例是流动性的非线性重写"这个方向——`day_at_min_ratio(Open)`(当日取到
   最小值的分钟占比)是这类"取到某个重复值的频率"测度在**分钟频率**上的类比,原始文献是日频上的零收益,
   机制相通:观测值重复(或取到边界值)的频率越高,背后对应的交易摩擦/有效价差越大,不是新信息。[LOT1999]

2. **把"量集中在少数重复值"这件事推广到中国市场、日频,标准做法是把 Amihud 的价格冲击测度和零收益占比
   结合成一个复合流动性测度,而不是单独使用其中一个。** 一项用上海 A 股 2000–2013 年数据做的研究,构造了
   一个结合 Amihud 非流动性与零收益天数占比的测度,用它去解释股改前后的收益自相关变化,发现高这一复合
   流动性测度的组合,收益自相关(无论延续还是反转)都更强。翻成算子语言:这条是族 VI 判定在**A 股本地**
   的直接支撑——"零值发生频率"与"收益自相关强弱"在中国市场上是同一个流动性故事的两面,而不是两件独立
   的事,这正是 analysis.md 判定 `day_q_stat_std`/`day_ar1_coefficient` 这类自相关统计量读的是流动性,
   而不是信息的关键证据。[CY2015]

3. **买卖价差跳动(bid-ask bounce)本身就会制造出负的一阶序列协方差,即使价格完全没有新信息——这是
   把"自相关系数"读成流动性代理而不是可预测性的最基础的理论模型。** 该模型证明,在有效市场假设下,
   仅凭买卖价差的跳动(交易价格在买价和卖价之间来回跳),观测到的价格变化序列就会出现负的一阶自相关,
   且据此反推出的隐含价差与公司规模密切相关;作者特别提醒应该用序列协方差而不是自相关系数或方差,因为
   后两者更容易被新息污染。翻成算子语言:这是 `day_ar1_coefficient(Open)` 读到负值时最经典的流动性
   解释——负自相关的量级直接由有效价差决定,与"信息"无关,而且该量级本身应该和公司规模(本环境的市值
   控制)系统相关。[ROLL1984]

4. **价格离散(最小变动价位,tick size)本身会扭曲在短周期上计算出来的自相关/相关性,这是一个纯统计
   artefact,不是市场行为,而且价越低、周期越短,扭曲越大。** 用模型和真实市场数据证明,最小变动价位
   会改变收益分布的形状、加厚尾部,并在**短周期**上系统性扭曲相关性估计,这个效应被认为是 Epps 效应
   (相关性随采样间隔缩短而下降)的一个贡献来源,作者给出了一个统计修正方法。翻成算子语言:这条直接
   支持族 VI 判定里"族 VI 的量级近似 1/有效配对数"这一事实——分钟频率、低价股、薄交易的组合恰好是
   tick size 扭曲最严重的场景,`day_q_stat_std`/`day_ar1_coefficient` 在这类股票上的数值,**按构造**
   就会比高价、厚交易股票系统性更极端,这不是额外的信息,是离散化artefact 的强度差异。[MSG2010]

5. **这一整类基于自相关/方差比的统计量,在小样本下存在已知的、有具体文献量化过的检验量偏误(size
   distortion),不是本环境特有的问题。** 对方差比检验做的蒙特卡洛研究发现,在 IID 高斯随机游走的原假设
   下,该类检验的实际检验水平(size)在小样本下会偏离名义水平,且偏误方向和幅度依赖于观测数和滞后期的
   比例,原论文的作者就是提出方差比检验的同一对学者。翻成算子语言:这条是 analysis.md 事实(7)
   "Q 用 T=241 而非有效配对数"这一判断的方法论侧支撑——`day_q_stat_std` 这类基于若干滞后自相关构造的
   统计量,其零假设下的分布本身就依赖样本量,而不是一个与样本量无关的"信息强度"标尺,样本量(或有效配对
   数)不同,同样的"信息含量"会算出不同的统计量数值。[LMK1989]

6. **"当日等于最低价的分钟占比"这类度量,在中国市场遇到涨跌停/停牌时,标准做法是把限价/停牌日当作一个
   独立的、机制性的事件单独处理或剔除,而不是直接喂给通用的统计量。** 用 2000–2011 年沪深 A 股涨跌停数据
   做的研究发现,触及涨跌停之后的下一交易日,价格延续的概率远高于反转,尤其是跌停之后,作者将涨跌停规则
   的效果归纳为"冷却效应"而非"磁吸效应"。这篇虽然没有直接给出"如何处理这类日子里的分钟统计量"的操作性
   建议,但它独立证明了**涨跌停日本身会产生和平常交易日不同的统计规律**,翻成算子语言的含义是:
   `day_at_min_ratio(Open)` 如果在跌停日恰好等于 1(全天封在跌停价附近),这反映的是涨跌停规则的机械
   后果,不是任何"价格发现"信息;一份非同行评审但聚焦 A 股停牌机制的行业研究报告进一步指出,停牌期间的
   收益假设为零会人为压低波动率一类的度量,并把"动态剔除停牌股票"列为业界处理这类日子的常见做法之一。
   [PLH2015][DESCO2021]

**搜不到 / 拿不准,不用:**
- 没搜到专门把"Ljung-Box 统计量"本身(而不是方差比或简单自相关系数)当作**横截面特征**、直接做截面
  收益预测检验、并同时讨论零收益比例/有效样本量偏误的论文;上面第 5 条(LMK1989)是方差比检验的小样本
  偏误,结构上和 Ljung-Box 同属"基于多个滞后自相关构造的检验统计量",但不是同一个统计量,这条类比
  已在正文标注,不冒充为直接证据。
- 没搜到专门量化"有效观测数偏误"与"零收益比例"在同一个检验里的交互作用(即控制了零收益比例之后,
  还剩多少偏误是纯粹的有效样本量问题)的论文,LOT1999 与 LMK1989 分别是零收益和小样本偏误两条独立的
  文献线,没有搜到把两者在同一个框架下合并讨论的工作,这条按"搜不到"处理。
- DESCO2021(De Shaw 的 A 股交易停牌行业研究报告)不是同行评审文献,WebFetch 无法解析其 PDF 正文
  (二进制流),第 6 条里引用它的内容只来自 WebSearch 结果摘要里可定位的片段,没有拿到完整原文验证,
  这条的可信度明显低于其余条目,请 PI 和检查环节知悉,不要把它当作和期刊论文同等级别的证据。

---

## 出处列表

**[AP1988]**
标题:A Theory of Intraday Patterns: Volume and Price Variability
作者:Anat R. Admati, Paul Pfleiderer
年-月:1988(*The Review of Financial Studies*, Vol. 1, No. 1, pp. 3–40)
来源:期刊(The Review of Financial Studies)
链接:https://ideas.repec.org/a/oup/rfinst/v1y1988i1p3-40.html
verified: true(WebFetch 直接打开 IDEAS/RePEc 条目页,确认标题、作者、期刊、卷期、页码、年份;与
`r2/lit.md` 出处列表同一篇,本轮再次独立核实)

**[H2010]**
标题:Intraday Patterns in the Cross-Section of Stock Returns
作者:Steven L. Heston, Robert A. Korajczyk, Ronnie Sadka
年-月:2010(*Journal of Finance*, Vol. 65, No. 4, pp. 1369–1407)
来源:期刊(Journal of Finance);工作论文版本在 arXiv(ar5iv 镜像)
链接:https://ar5iv.arxiv.org/html/1005.3535 ;Kellogg 官方介绍页
https://www.kellogg.northwestern.edu/academics-research/research/detail/2010/intraday-patterns-in-the-cross-section-of-stock-returns
verified: true(与 `r1/lit.md`、`r2/lit.md` 同一出处,本轮 WebSearch 再次独立命中并确认)

**[RZ2010]**
标题:Recurrence interval analysis of trading volumes
作者:Fei Ren, Wei-Xing Zhou
年-月:2010-02(arXiv:1002.1653,首版提交 2010-02-06)
来源:工作论文(arXiv 预印本)
链接:https://arxiv.org/abs/1002.1653 ;https://arxiv.org/pdf/1002.1653
verified: true(与 `r2/lit.md` 同一出处,本轮 WebSearch 再次独立命中确认标题、作者、提交日期)

**[KA1987]**
标题:The Relation between Price Changes and Trading Volume: A Survey
作者:Jonathan M. Karpoff
年-月:1987-03(*Journal of Financial and Quantitative Analysis*, Vol. 22, No. 1, pp. 109–126)
来源:期刊(Journal of Financial and Quantitative Analysis)
链接:https://ideas.repec.org/a/cup/jfinqa/v22y1987i01p109-126_01.html ;
https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/relation-between-price-changes-and-trading-volume-a-survey/DBE2C70FA41E390EB8FA418BBFFD76C8
verified: true(WebSearch 多个独立来源——IDEAS/RePEc、Cambridge 期刊官方页、作者 University of
Washington 个人研究总结页——一致确认标题、作者、卷期、"量与价格变化幅度同期正相关"这一核心结论)

**[BW1993]**
标题:Stealth Trading and Volatility: Which Trades Move Prices?
作者:Michael J. Barclay, Jerold B. Warner
年-月:1993(*Journal of Financial Economics*, Vol. 34, No. 3, pp. 281–305)
来源:期刊(Journal of Financial Economics)
链接:https://orbilu.uni.lu/bitstream/10993/58977/1/WPC%20FRL%20240411.pdf (后续文献对 WPC 构造的转述);
https://academicnewsletter.sufe.edu.cn/info/358241
verified: true(WebSearch 多个独立来源——上海财经大学学术快讯摘要页、卢森堡大学机构知识库挂出的后续
WPC 方法论文 PDF——一致确认标题、作者、期刊卷期页码、"中等规模交易占价格变动的大部分"这一核心结论,
以及 WPC 测度"按日净价格变化绝对值加权"的构造方式)

**[CHKZ2020]**
标题:Foreign Investors, Private Information, and Price Discovery
作者:Jun Cai, Richard Ho, Robert Korajczyk, Zheng Zhang
年-月:2020(Kellogg 官方工作论文介绍页标注年份 2020;SSRN 摘要号 1687116,首版挂出日期本次因 SSRN
返回 403 未能独立核实)
来源:工作论文(Kellogg School of Management 研究页 / SSRN)
链接:https://www.kellogg.northwestern.edu/academics-research/research/detail/2020/foreign-investors-private-information-and-price-discovery
;https://papers.ssrn.com/author=3570275
verified: true(WebFetch 直接打开 Kellogg 官方工作论文介绍页,确认标题、作者、摘要——23 个新兴市场
1504 只股票、按分段加权价格贡献度衡量价格发现、与外资持股/私有信息的关系;**SSRN 原始首版日期未能
独立核实**,按年份标注 2020,置信度低于其余条目,请 PI 知悉)

**[GHLX2019]**
标题:Overnight Momentum, Informational Shocks, and Late-Informed Trading in China
作者:Ya Gao, Xing Han, Youwei Li, Xiong Xiong
年-月:2019(*International Review of Financial Analysis*, Vol. 66, 文章号 101394;在线出版日期
2019-10-22)
来源:期刊(International Review of Financial Analysis);工作论文版本 MPRA Paper No. 96784
链接:https://ideas.repec.org/p/pra/mprapa/96784.html ;
https://hull-repository.worktribe.com/OutputFile/3016448
verified: true(WebSearch 多个独立来源——Hull 大学机构知识库、MPRA 工作论文记录、大连理工大学作者
个人主页——一致确认标题、作者、期刊卷期、文章号、在线出版日期 2019-10-22,以及"隔夜段主导日内动量
可预测性、负面冲击后更强"这一核心结论)

**[LPS2019]**
标题:A Tug of War: Overnight Versus Intraday Expected Returns
作者:Dong Lou, Christopher Polk, Spyros Skouras
年-月:2019(*Journal of Financial Economics*, Vol. 134, No. 1, pp. 192–213)
来源:期刊(Journal of Financial Economics)
链接:https://personal.lse.ac.uk/polk/research/TugOfWar.pdf ;https://eprints.lse.ac.uk/87481/
verified: true(与 `r1/lit.md` [LPS2019] 同一出处,本轮 WebSearch 再次独立命中——LSE Research Online、
作者 LSE 个人页 PDF、NBER 会议论文版——一致确认标题、作者、期刊卷期、"14 种策略利润几乎全部来自隔夜或
日内其中一段、符号相反"这一核心结论、以及"机构日内交易且与动量方向相反、散户隔夜更活跃"的客群解释)

**[LCC2023]**
标题:Overnight versus intraday returns of anomalies in China
作者:Chaonan Lin, Hui-Wen Chang, Robin K. Chou
年-月:2023-06(*Pacific-Basin Finance Journal*, Vol. 79,文章号 102007,DOI 10.1016/j.pacfin.2023.102007)
来源:期刊(Pacific-Basin Finance Journal)
链接:https://ideas.repec.org/a/eee/pacfin/v79y2023ics0927538x23000732.html
verified: true(WebFetch 直接打开 IDEAS/RePEc 条目页,确认标题、作者、期刊卷期、DOI、文章号后缀
102007;另有政治大学教师发表记录页独立确认发表月份 2023-06,早于 2023-08-08 截止线;摘要核心结论:
中国市场的拔河效应方向与美股不同,更多策略利润来自隔夜段)

**[BZ2020]**
标题:T+1 trading mechanism causes negative overnight return
作者:Bing Zhang
年-月:2020(*Economic Modelling*, Vol. 89, pp. 55–71,DOI 10.1016/j.econmod.2019.10.013)
来源:期刊(Economic Modelling)
链接:https://ideas.repec.org/a/eee/ecmode/v89y2020icp55-71.html
verified: true(WebFetch 直接打开 IDEAS/RePEc 条目页,确认标题、作者、期刊卷期页码、DOI、年份;摘要
核心结论:A 股隔夜收益显著为负、T+0 资产隔夜收益接近零或为正,负偏在高分歧度/高风险/高散户占比/强
卖空限制/低流动性的股票上更强)

**[LOT1999]**
标题:A New Estimate of Transaction Costs
作者:David A. Lesmond, Joseph P. Ogden, Charles A. Trzcinka
年-月:1999(*The Review of Financial Studies*, Vol. 12, No. 5, pp. 1113–1141)
来源:期刊(The Review of Financial Studies)
链接:https://ideas.repec.org/a/oup/rfinst/v12y1999i5p1113-41.html ;
https://www.bauer.uh.edu/rsusmel/phd/lot_1999RFS.pdf
verified: true(WebFetch 直接打开 IDEAS/RePEc 条目页,确认标题、作者、期刊卷期页码、年份,以及摘要
原文"the incidence of zero returns"这一核心构造依据;后续文献俗称的"Zeros"测度名称本身不在原摘要
逐字出现,正文已注明这一点,不冒充原文用语)

**[ROLL1984]**
标题:A Simple Implicit Measure of the Effective Bid-Ask Spread in an Efficient Market
作者:Richard Roll
年-月:1984-09(*The Journal of Finance*, Vol. 39, No. 4, pp. 1127–1139)
来源:期刊(The Journal of Finance)
链接:https://www.bauer.uh.edu/rsusmel/phd/roll1984.pdf ;
https://resolver.caltech.edu/CaltechAUTHORS:20190501-103050384
verified: true(WebFetch 读取 PDF 的 SICI 元数据确认期刊 ISSN、年月 1984-09、卷期 39(4)、起始页 1127;
WebSearch 另有授课讲义、metricgate 说明页独立确认公式 spread = 2√(−Cov(Δp_t, Δp_{t-1})) 与"买卖价差
跳动产生负序列协方差"这一核心机制)

**[MSG2010]**
标题:Impact of the Tick-Size on Financial Returns and Correlations
作者:Michael C. Münnix, Rudi Schäfer, Thomas Guhr
年-月:2010-01(arXiv:1001.5124,首版提交 2010-01-28)
来源:工作论文(arXiv 预印本)
链接:https://arxiv.org/pdf/1001.5124 ;https://ar5iv.arxiv.org/html/1001.5124
verified: true(WebFetch 直接打开 arXiv 摘要页,确认标题、作者、首版提交日期 2010-01-28,以及摘要核心
结论:最小变动价位会改变收益分布形状、在短周期上扭曲相关性估计、是 Epps 效应的贡献来源之一)

**[PLH2015]**
标题:Statistical Properties and Pre-hit Dynamics of Price Limit Hits in the Chinese Stock Markets
作者:Yu-Lei Wan, Wen-Jie Xie, Gao-Feng Gu, Zhi-Qiang Jiang, Wei Chen, Xiong Xiong, Wei Zhang,
Wei-Xing Zhou
年-月:2015-03(arXiv:1503.03548,首版提交 2015-03-12);同年发表于 *PLoS ONE*, Vol. 10, No. 6
来源:工作论文(arXiv 预印本)+ 期刊(PLoS ONE)
链接:https://arxiv.org/abs/1503.03548 ;https://ideas.repec.org/a/plo/pone00/0120312.html
verified: true(WebFetch 直接打开 arXiv 摘要页,确认标题、全部 8 位作者及所属机构、首版提交日期
2015-03-12,以及摘要核心结论:2000–2011 年沪深 A 股涨跌停后呈"冷却效应"而非"磁吸效应",跌停后价格
延续概率明显高于反转)

**[CY2015]**
标题:An Empirical Study of Liquidity and Return Autocorrelations in the Chinese Stock Market
作者:Chen Yang
年-月:2015-09(*Asia-Pacific Financial Markets*, Vol. 22, No. 3, pp. 261–282,DOI
10.1007/s10690-015-9203-5)
来源:期刊(Asia-Pacific Financial Markets, Springer / 日本金融工程学会)
链接:https://ideas.repec.org/a/kap/apfinm/v22y2015i3p261-282.html
verified: true(WebFetch 直接打开 IDEAS/RePEc 条目页,确认标题、作者、期刊卷期页码、DOI、出版日期
2015-09;摘要核心结论:结合 Amihud 非流动性与零收益天数占比的复合测度,在上海 A 股股改前后的收益
自相关变化中,高该测度组合的自相关更强,原文摘要原句"All return autocorrelations are stronger for
high-illiquidity portfolios")

**[LMK1989]**
标题:The Size and Power of the Variance Ratio Test in Finite Samples: A Monte Carlo Investigation
作者:Andrew W. Lo, A. Craig MacKinlay
年-月:1989(*Journal of Econometrics*, Vol. 40, No. 2, pp. 203–238);早期版本为 NBER Working Paper
No. t0066(1988)
来源:期刊(Journal of Econometrics);工作论文(NBER)
链接:https://web.mit.edu/~alo/www/Papers/lo-mackinlay-89.html ;https://www.nber.org/papers/t0066
verified: true(WebSearch 多个独立来源——作者 MIT 个人学术页、NBER 官方工作论文页、IDEAS/RePEc——
一致确认标题、作者、期刊卷期页码,以及"方差比检验在小样本下的检验水平会偏离名义水平,偏误依赖样本量
与滞后期比例"这一核心结论)

**[LMK1988]**
标题:Stock Market Prices Do Not Follow Random Walks: Evidence from a Simple Specification Test
作者:Andrew W. Lo, A. Craig MacKinlay
年-月:1988(*The Review of Financial Studies*, Vol. 1, No. 1, pp. 41–66)
来源:期刊(The Review of Financial Studies)
链接:https://web.mit.edu/~alo/www/Papers/lo-mackinlay-88.html
verified: true(WebFetch 直接打开作者 MIT 个人学术页上的论文介绍,确认标题、作者、期刊、卷期、页码、
年份,以及方差比检验的基本做法——比较不同抽样频率下算出的方差估计量)

**[DESCO2021]**
标题:Market Insights: China A Trading Halts(D. E. Shaw & Co. 行业研究报告,非同行评审)
作者:D. E. Shaw & Co.(机构作者,未署名具体分析师)
年-月:2021-09-17(按文件名日期戳)
来源:行业研究报告(资产管理机构官网发布的市场洞察文章)
链接:https://www.deshaw.com/assets/articles/DESCO_Market_Insights_China_A_Trading_Halts_20210917.pdf
verified: true(WebSearch 命中该 PDF 并给出可定位的原文片段——"动态剔除停牌股票"作为业界常见处理方式
之一、停牌期间零收益假设会人为压低波动率一类度量;**WebFetch 未能解析该 PDF 的二进制正文**,未能
亲眼看到完整原文,可信度与细节完整性明显低于其余期刊/arXiv 条目,请 PI 与检查环节知悉,不要等同期刊
论文采信)
