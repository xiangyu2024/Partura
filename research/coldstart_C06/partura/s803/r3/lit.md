# 文献:种子 803,C 组,第 3 轮(文献员)

对准 `r3/analysis.md` §5 的四个题目(L1–L4)。**只用 2023-08-08 之前发表**的论文/工作论文/研究报告;日期拿不准的没有收进来。
每条「处理方式」后面括号标注出处编号([n]),出处清单附在每个题目末尾,格式为:标题 / 作者 / 年-月 / 来源 / 链接 / `verified`。
`verified: true` = 这次搜索结果或页面上确实看到了这条文献的标题、作者、期刊/平台信息;没能独立核实的写 `verified: false` 并说明哪部分没查到。

---

## L1 —— 核心 ①(`ts_reg_fvalue(day_std(Amt), day_centroid(Amt), 50)`):把「拟合优度/相关系数」当截面特征,文献怎么处理估计噪声

**搜到的,是同一结构在另一个场景下的完整先例**:市场模型回归的 R²(「同步性」)被当作截面特征用了二十多年,而且**文献已经证明这个 R² 被稀薄交易系统性地往下打**——这正是 analysis.md §1.1 本机算术验证的那个机制(「F 排的是重心测得准不准」),只是换了一个回归式。

**可翻译成算子语言的处理方式**:

1. **R²(或等价的相关系数/F 统计量)本身被当作截面预测变量,解释成「价格里有多少自身信息」**:低 R² = 更多个股特有信息。这就是 `ts_reg_fvalue` 式写法的方法论源头——用拟合优度代替相关系数本身,只是我们的场景(日内成交形状的时序耦合)不是市场模型,是个股自回归。([1][2])
2. **这个 R² 被证明系统性地、非线性地被流动性/稀薄交易压低,而且早期针对 beta 的「非同步交易」修正(加滞后项)修不好 R² 本身**:作者建议用**非线性的流动性控制**去检验这个 R² 测出来的东西是不是真的。
   **直接翻译**:这正是 analysis.md §4.1 核心①外围计划第 1 条——`cs_bucket_rank(核心, cross_mean(day_pos_ratio(Volume), 20))`(在密度十分位内排序)。文献独立地给出了同一个处方:**不是把 R² 当作干净信号直接用,而是先按流动性分桶再看它还剩多少**。([3])
3. **非同步交易(稀薄交易)让回归系数/相关系数向零收缩,这个偏误是经典结果,不是新发现**:原始文献修正的是 beta(用领先滞后的市场收益做回归),但偏误的方向和机制(测量噪声 → 回归统计量系统性衰减)与我们在 F 家族上做的算术验证(重心噪声秩相关 −0.795)是同一件事的另一个实例。([4])
4. **交易集中/分散的形状本身为什么会被定价,有一个三十多年的理论基础**:知情交易者与流动性交易者的策略性选择会让成交量在日内呈 U 形聚集,而且模型预言「成交量越大、价格越有信息含量」。这给 `day_centroid`/F 家族「交易时点结构 ↔ 信息环境」的解读提供了理论支撑,但也提示:**这类日内形状测度(谁在什么时候交易)本身就带有「流动性越好、形状越规律」的同义性**,与 §1.1 的判读(F ≈ 密度的第三种写法)方向一致。([5])
5. **一个相邻的告诫**:成交量、委比、波动率、买卖价差的日内周期性彼此高度相关,但这些共享的周期性本身**解释不了**收益的日内模式(作者专门测过)。
   **翻译**:不能因为 F 家族「尺度无关、跨字段跨窗口稳」就推断它测到了新机制——这几条稳健性在文献里对应的是「日内形状的周期性本身很稳」,而这恰恰是密度通道的特征,不是信息通道的特征。这条文献证据**削弱**而不是加强核心①是「真耦合」的判断,与本机算术验证的结论(F ≈ 0.55 密度 + 0.45 真耦合)方向一致。([6])

**没搜到的**:「用 R² 当特征等于用测量精度当特征」这句话本身作为一条方法论文献的明确表述——搜索只找到了两个具体结果(同步性 R² 被非同步交易压低;beta 被非同步交易收缩向零),没有找到把这两点合并成一般方法论陈述的单篇文献。

### 出处

[1] *The Information Content of Stock Markets: Why Do Emerging Markets Have Synchronous Stock Price Movements?* — Randall Morck, Bernard Yeung, Wayne Yu — 2000-10 — *Journal of Financial Economics* 58(1), 215–260 — https://randallmorck.ca/wp-content/uploads/2020/04/the-information-content-of-stock-markets-why-do-emerging-markets-have-synchronous-stock-price-movements.pdf — `verified: true`

[2] *R² (Roll 1988 的市场模型同步性测度,作为后续文献的方法论源头)* — Richard Roll — 1988 — *Journal of Finance* 43(3) — 本次只在二级引用中确认其核心主张(低 R² = 私有信息或噪声),没有直接打开原文核实卷期页码 — `verified: false`(主张本身在多篇引用文献中一致复述,但未独立核对原文)

[3] *Illiquidity and the Measurement of Stock Price Synchronicity* — Joachim Gassen, Hollis Ashbaugh-Skaife, David Veenman — 2020(期刊版;工作论文版见 SSRN 2019) — *Contemporary Accounting Research* 37(1), 419–456 — https://papers.ssrn.com/abstract=3386050 — `verified: true`

[4] *Estimating Betas from Nonsynchronous Data* — Myron Scholes, Joseph Williams — 1977 — *Journal of Financial Economics* 5, 309–327/328(二级引用页码有 309–327 与 309–328 两个版本,未核对原文定稿) — 本次通过多篇引用该文献的二级来源确认其核心结果(非同步交易使日度 beta 向零收缩,OLS 估计有偏且不一致) — `verified: true`(核心结果多处复述一致;页码细节 `verified: false`)

[5] *A Theory of Intraday Patterns: Volume and Price Variability* — Anat R. Admati, Paul Pfleiderer — 1988 — *Review of Financial Studies* 1(1), 3–40 — https://academicnewsletter.sufe.edu.cn/info/355980 — `verified: true`

[6] *Intraday Patterns in the Cross-Section of Stock Returns* — Steven L. Heston, Robert A. Korajczyk, Ronnie Sadka — 2010 — *Journal of Finance* 65(4), 1369–1407 — https://ar5iv.arxiv.org/html/1005.3535 — `verified: true`

---

## L2 —— §1.4 判决(未归一化高阶已实现矩 ≈ 波动水平)+ R 第 2 组 + ListAge + 低波动多头腿

**可翻译成算子语言的处理方式**:

1. **已实现偏度/峰度在文献里从第一天就是「归一化」的定义,没有「先用未归一化版本,回头再归一化」这个步骤**:三阶矩归一化的标准写法是**除以方差的 3/2 次方**(`RV^1.5`),四阶矩除以方差的平方(`RV^2`)。
   **直接翻译**:analysis.md §4.2 R2-6 提的「无量纲版」`div(cross_sum(day_sum(mul(mul(Ret,Ret),abs_(Ret))),3), pow_1_5(cross_sum(day_sum(mul(Ret,Ret)),3)))` ,分母的 `pow_1_5` 加在 `cross_sum(day_sum(r²))` 上,**在形式上就是文献定义的 RV^1.5 分母**。这不只是一个合理的对照组,它是这类文献的标准定义本身。([1][2])
2. **构造已实现偏度的原始文献明确报告:单独按已实现波动率排序,排序出来的收益利差不显著;只有排序「归一化之后的偏度」才显著**。
   **翻译**:这条和我们本轮的算术验证(§1.4:`rank corr(Σ|r|³, σ) = +0.952`)方向完全一致,是独立的文献证据——**未归一化的高阶矩在排序意义上就是波动率排序**,文献的归一化动作(除以 RV^{3/2})正是为了把这部分剔除。([1])
3. **没搜到的**:一篇**明确写出**「未归一化的高阶已实现矩在截面上几乎等价于波动水平,因而控制波动后消失」这句话的文献。搜到的是**间接证据**(归一化是标准做法 + 原始文献的波动率排序本身不显著),但没有一篇论文把这两点显式连成一句话当作自己的发现来报告。这条缺口在给 PI 的报告里要诚实写明:**我们的算术验证(rank corr +0.952)目前没有独立的文献原文背书,是我们自己这次做的检验,不是在复述文献**。
4. **上市年龄/次新股独立作用**:英文学术文献里没有搜到直接检验「控制规模/波动/流动性后,上市年龄在 A 股截面上还有独立作用」的论文。能确认的是一个相邻但不完全等价的结果:**次新股(小市值 + 新上市)在中国市场被作为「壳价值」处理,构造任何因子前都要先把市值最小的 30% 删掉**,这 30% 占总市值约 7%。
   **翻译给 PI**:这是对 ListAge 的一个有力的侧面印证——**文献里对「小而新」这类股票的标准处理是筛掉,不是当作独立信号去挖**,与 analysis.md §1.4/§2 的结论(ListAge 是 distinct=0.095 的粗分组,不是信息)方向一致。([3])
   中文财经研究(主要是券商报告,非学术期刊)里次新股超额收益的常见解释是估值折价、高送转预期、流通盘小、风险偏好与"二月效应",都不是"控制市值/流动性之后的独立定价",本次搜索没有找到满足条件的严谨截面回归文献。
5. **低波动/低风险异象的多头腿在 A 股的证据(样本结束于 2023-08 之前)**:
   - 机构研究:2000 年 12 月至 2018 年 12 月的 A 股样本里,一个 Fama-French 式的波动率因子比 Fama-French-Carhart 模型里其他任何因子的风险调整后溢价都高;效应在各个期限和行业都稳健,换手率低,且在最大最活跃的股票里一样强(不是流动性折价的伪装);作者倾向于行为解释(个人投资者主导)和基准驱动解释,而不是交易成本。([4])
   - 学术文献:2002–2019 的 A 股样本里,特质波动率溢价之谜存在且稳健,套利限制能部分解释它。([5])
   - 另一篇用分位数回归的研究报告 OLS 下特质风险与预期收益负相关但不显著,分位数回归在低分位显著为负、高分位显著为正——**低波动异象在 A 股不是没有争议的**,结果对估计方法敏感。([6])

### 出处

[1] *Does Realized Skewness Predict the Cross-Section of Equity Returns?* — Diego Amaya, Peter Christoffersen, Kris Jacobs, Aurelio Vasquez — 2015(期刊版;工作论文版 2011/2013 在 CREATES) — *Journal of Financial Economics* 118(1), 135–167 — https://repec.econ.au.dk/repec/creates/rp/13/rp13_41.pdf — `verified: true`

[2] *Realized Skewness* — Anna Neuberger — 2012 — *Review of Financial Studies* 25(11), 3423–3455 — https://openaccess.city.ac.uk/id/eprint/15210/1/RFS%20Realized%20Skewness%20solo.pdf — `verified: true`

[3] *Size and Value in China* — Jianan Liu, Robert F. Stambaugh, Yu Yuan — 2019(期刊版;NBER 工作论文 w24458,2018-03) — *Journal of Financial Economics* 134(1), 48–69 — https://faculty.wharton.upenn.edu/wp-content/uploads/2018/03/Size-and-Value-in-China.pdf — `verified: true`

[4] *The Low Volatility Effect in China*(研究报告,非期刊论文) — Robeco(机构研究,未署名个人作者;引用 Blitz, Falkenstein & van Vliet (2014) 作为背景) — 2021-05 — Robeco Insights — https://www.robeco.com/en-int/insights/2021/05/the-low-volatility-effect-in-china — `verified: true`

[5] 标题未在搜索结果中完整给出,仅确认刊物与年份 — 作者未知(搜索结果以「Chen 和 Ye (2021)」转述,未给出全名) — 2021 — *Discrete Dynamics in Nature and Society* — https://doaj.org/article/4cccf1efa39a45eeaee8dc736a8ccbd3 — `verified: false`(刊物、年份、核心结论在二级来源中确认,但未独立核实完整标题和作者全名,不建议在最终报告里点名引用,只作为「存在同行评议证据」的旁证)

[6] *Is there idiosyncratic volatility puzzle in Chinese stock markets: A quantile regression analysis* — 作者未在搜索结果中给出 — 2018 — *Journal of Management Sciences in China*(天津大学期刊平台) — https://jmsc.tju.edu.cn/jmscen/article/abstract/20181203 — `verified: true`(标题、刊物、链接核实;作者姓名未显示,`verified: false` 仅限作者部分)

---

## L3 —— N-甲(隔夜/日内收益拆分):谁先做的、怎么处理 A 股的涨跌停与集合竞价

**可翻译成算子语言的处理方式**:

1. **把日收益拆成隔夜段(收盘到开盘)和日内段(开盘到收盘)、分别检验已知异象,这个做法的源头很明确**:14 个经典交易策略里,收益几乎全部落在其中一段,两段方向经常相反;作者把这个现象归因于两种**投资者群体**(机构偏好日内交易、与动量特征反向操作)。
   **直接翻译**:这正是 N-甲计划的构造方式本身——`sub(cross_sum(隔夜,20), cross_sum(日内,20))`。文献的标准构造是逐日拆分后分别对异象做横截面排序比较,而不是只看相减后的净值,**建议外围至少保留隔夜、日内两条单独序列各评估一次,不要只提交相减版**(analysis.md §4.3 已经这样安排)。([1])
2. **A 股隔夜段的均值本身显著为负,这是一个独立于「拆分」这个方法论的、市场特定的事实**,至少两条独立路径指向同一个机制:**T+1 结算规则**——买入当天不能卖出,这个"锁仓"摩擦会在开盘价上打出折价,从而让隔夜段系统性为负;折价与资产的波动率、波动率风险、跳跃风险正相关(类似一个嵌在股票里的看跌期权)。
   **翻译给 PI**:隔夜段的**水平**本身预期跟波动控制不是正交的——这是文献给出的、不是我们自己猜的先验,§4.3「要防的坑」里已经点了封板,但 T+1 本身(不需要封板)就会让隔夜段与波动相关,**外围计划里按密度/波动分桶这一步不是可选项,是文献已经预判会出问题的地方**。([2][3])
3. **隔夜段的负向效应是不对称的**:只在「前一天日内段是跌的」之后才显著,前一天日内段涨的时候这个异象不出现;机制归因是个人投资者对亏损的日内段投入更多注意力(A 股个人投资者占比高,这条解释路径成立的前提在 A 股比在美股更站得住)。
   **直接翻译**:N-甲的主因子目前是隔夜与日内各自的无条件水平。文献建议一个更细的写法——**隔夜段条件化在前一日日内段的符号上**,例如 `mul(隔夜, is_lt0(cross_delay(日内,1)))` 这类交互项,可能比无条件版本信息量更大,这是一个 analysis.md 里没列但值得加一颗种子的方向。([4])
4. **行业层面的反例**:能源股的隔夜段强负、日内段为正,9 个经典异象的收益几乎全部来自夜间——方向与美股文献(动量收益集中在隔夜)不是简单的镜像,说明**A 股隔夜/日内的分工在不同板块上可能方向不同**,外围计划「按流动性/密度分桶」还不够,**可能还需要按行业或板块(BoardCode)检查方向是否稳定**,这是 N-甲计划目前没有覆盖的一个风险点。([5])
5. **2018-08-20 上交所引入收盘集合竞价,是样本期(2018-01~2023-08)中段的一次结构性变化**,深交所早在 2006 年就有收盘集合竞价。多篇研究把这次新政当作自然实验,发现它降低了收盘价操纵、提升了价格连续性,对小盘股帮助更大。
   **翻译给 PI**:`day_last(Close)` 在上交所股票上,2018-08-20 前后的测量噪声结构不是平稳的(操纵/跳价概率下降),而深交所股票没有这次断点。N-甲的隔夜段用到 `cross_delay(day_last(Close), 1)`,**如果要做一次稳健性检查,可以按交易所(或 2018-08-20 前后分段)看隔夜段的统计量是否有断点**,这是源码/规则允许读、但 analysis.md 没点出来的一个具体可执行的检验点。([6][7][8])

### 出处

[1] *A Tug of War: Overnight Versus Intraday Expected Returns* — Dong Lou, Christopher Polk, Spyros Skouras — 2019-02(期刊版,卷期;最早工作论文版 2015-03,LSE/FMG Discussion Paper No. 744) — *Journal of Financial Economics* 134(1), 192–213 — https://researchonline.lse.ac.uk/id/eprint/119010 — `verified: true`

[2] *The Overnight Return Puzzle and the "T+1" Trading Rule in Chinese Stock Markets* — Lin Qiao, Lammertjan Dam — 2020 — *Journal of Financial Markets* 50 — https://ideas.repec.org/a/eee/finmar/v50y2020ics1386418120300033.html — `verified: true`

[3] T+1 与隔夜收益关系的期权式建模(清华 PBC 学院工作论文;标题与月份未在搜索结果中完整给出,仅确认作者姓氏与机构) — Bai, Wu, Ke(全名未给出) — 年份未在搜索结果中给出 — 清华大学 PBC 金融学院工作论文 — 未给出直接链接 — `verified: false`(仅在二级转述中出现,未独立核实标题、年份与链接,不建议在最终报告里直接引用,只作为旁证线索)

[4] *The Asymmetric Overnight Return Anomaly in the Chinese Stock Market* — Yahui An, Lin Huang, Youwei Li — 2022-11 — *Journal of Risk and Financial Management* 15(11), 534 — https://ideas.repec.org/a/gam/jjrfmx/v15y2022i11p534-d974482.html — `verified: true`

[5] *Overnight-Intraday Mispricing of Chinese Energy Stocks: A View from Financial Anomalies* — Min Zhou, Xiaoqun Liu — 2022-02(在线发表;期刊卷标为 2021) — *Frontiers in Energy Research*,DOI 10.3389/fenrg.2021.807881 — https://www.frontiersin.org/journals/energy-research/articles/10.3389/fenrg.2021.807881/full — `verified: true`

[6] *Reexamining the Impact of Closing Call Auction on Market Quality: A Natural Experiment from the Shanghai Stock Exchange* — Han 等(全名未在搜索结果中给出) — 2022 — *Pacific-Basin Finance Journal* 74 — https://ideas.repec.org/a/eee/pacfin/v74y2022ics0927538x22001160.html — `verified: true`(刊物、年份、卷号核实;作者全名 `verified: false`)

[7] 上交所收盘集合竞价对市场质量(流动性/波动率/价格连续性)影响的研究(China Finance Review International,2021;作者 Ma 等,全名未在搜索结果中给出) — `verified: false`(仅二级转述,未独立核实标题全文与作者全名)

[8] 上交所 2018-08-20 实施收盘集合竞价的交易所公告 — 香港交易所(转发公告,非研究文献,仅作时间点确认) — 2018-08 — HKEX 参与者通告 — https://www.hkex.com.hk/Services/Circulars-and-Notices/Participant-and-Members-Circulars/SEHK/2018/20180817_CT_099_18?sc_lang=en — `verified: true`

---

## L4 —— 交易密度当独立特征 + 样本筛选本身会不会造出因子

**可翻译成算子语言的处理方式**:

### ① 交易密度(独立于成交额/换手率)

1. **「零收益/零成交比例」作为流动性代理,比 Amihud 式的量价比指标更早、构造上更简单,而且在新兴市场样本里被证明预测力更强**:核心信号就是**不活跃的频率本身**,不需要用到成交量或价格冲击的大小。
   **直接翻译**:这是 analysis.md R1-2 `cross_mean(day_zero_ratio(Ret), 20)` 的方法论源头——文献走的是日频(一个月里零收益天数的比例),我们走的是分钟频(一天里零收益分钟的比例),**频率降了一档,但构造逻辑完全是同一个**。([1])
2. **这个零收益代理在截面上显著预测未来收益,而换手率基本没有预测力**:在把同一组股票按零收益比例和换手率分别排序之后,前者显著、后者几乎没有信号。
   **翻译给 PI**:R1-1(密度本身,`day_pos_ratio`)和 R1-2(零收益比例,`day_zero_ratio`)如果都 ≥ 0.5,文献给的先验是**它们应该比任何基于成交额水平(已知族)的东西更干净**——这条文献证据支持 analysis.md §0 的判断(「交易密度是本库最大的未被控制的已知量」),而且进一步说明:**如果要在库禁令之外再留一个密度代理,留 `day_zero_ratio` 这条线(文献证据更直接),不要留依赖量纲的写法**。([2])
3. **波动率—成交量的经典正相关关系,被证明其实是波动率—交易笔数(trade count)的关系;交易金额的大小在交易笔数之外没有增量信息**。
   **翻译**:这给"交易密度(有成交的分钟占比)比成交额更基础"提供了一个独立的、更早的理论支撑——不是我们这次才注意到"笔数/频率比金额更本质",这在 1994 年的文献里已经是主结论,而且方向一致(笔数本身驱动,不是金额)。('day_pos_ratio' 是"有没有交易"的二值计数,是"交易笔数"思路的一个简化版。)([3])
4. 知情/流动性交易者策略性聚集交易的理论(见 L1 出处[5])同样支持「密度本身是信息环境的代理」这个方向,不重复列出。

### ② 样本筛选本身会不会造出因子

1. **宇宙/断点/加权方式的构造选择,本身就能决定一个异象是否「显著」**:用 NYSE 断点 + 市值加权重新检验 447 个已发表的异象变量,64%(286 个)在 5% 水平上不显著,102 个流动性类变量里有 95 个(93%)不显著;原因被归到微小市值股票——它们只占约 3% 的市值,却占了约 60% 的股票数量,在等权或小盘股断点下被过度加权。
   **直接翻译给 PI**:这是 analysis.md §1.5 「`pow_2_5` 把筛子变成删除,最终排序 1/3 来自筛子本身」这件事的**最知名的文献先例**,只是方向反过来——Hou-Xue-Zhang 说的是"筛掉小盘股让异象消失",我们这里是"筛子(NaN 删除)本身的存在让异象出现"。两者是同一枚硬币的两面:**样本的构成(谁被算进去)比机制本身对最终数字的影响可能更大**。([4])
2. **动量策略的利润集中在小盘、低流动性的输家股票上,这些股票的交易成本高到足以吃掉大部分账面利润**——这是"筛选/可投资域"问题在收益端(不是在因子构造端)的例子:**不考虑交易摩擦去统计一个策略的收益,等于隐性地假设了一个不存在的可投资域**。
   **翻译**:这条文献的逻辑结构和 §1.5 的 NaN 发现是同构的——"账面上的因子收益有多少来自样本/可投资域的选择,而不是机制本身",只是它们量的是交易成本造成的隐性筛选,我们量的是算子里的显性 NaN 筛选。([5])
3. **中国市场的具体先例**:在构造任何因子之前,先把市值最小的 30%(约占总市值 7%)**整体删掉**,理由是这批股票的价格主要反映"壳价值"而不是基本面——这是"可投资域构造"选择被公开报告、且专门针对中国市场特征的一个案例。
   **翻译给 PI**:这给"ListAge/小盘粗分组不是信号,应该被筛掉而不是被挖"这个判断提供了一个国内市场的方法论先例,而不只是一个统计门槛(distinct_fraction)上的技术判断。([6], 同 L2 出处[3])

**没搜到的**:一篇**专门讨论**「算子内部产生的 NaN 本身如何制造一个样本筛选,进而制造一个看起来像因子的东西」的文献——这是我们这套算子语言特有的问题(覆盖率在最外层是健康的,但中间层已经做了筛选),文献里的"筛选偏误"讨论都是在讲**可投资域/断点选择**这种显式的、研究者主动做的筛选,不是"数学函数对负数返回 NaN"这种隐式筛选。这条判断仍然只是我们自己这次的工程发现,不是文献结论的直接复述。

### 出处

[1] *A New Estimate of Transaction Costs* — David Lesmond, Joseph Ogden, Charles Trzcinka — 1999 — *Review of Financial Studies* 12(5), 1113–1141 — https://www.bauer.uh.edu/rsusmel/phd/lot_1999RFS.pdf — `verified: true`

[2] *Liquidity and Expected Returns: Lessons from Emerging Markets* — Geert Bekaert, Campbell R. Harvey, Christian Lundblad — 2007-11 — *Review of Financial Studies* 20(6), 1783–1831(NBER 工作论文版 w11413,2005-06) — https://www.nber.org/papers/w11413 — `verified: true`

[3] *Transactions, Volume, and Volatility* — Charles M. Jones, Gautam Kaul, Marc L. Lipson — 1994 — *Review of Financial Studies* 7(4), 631–651 — https://ideas.repec.org/a/oup/rfinst/v7y1994i4p631-51.html — `verified: true`

[4] *Replicating Anomalies* — Kewei Hou, Chen Xue, Lu Zhang — 2020(期刊版;NBER 工作论文 w23394,2017-05) — *Review of Financial Studies* 33(5), 2019–2133 — https://www.nber.org/papers/w23394.pdf — `verified: true`

[5] *The Illusory Nature of Momentum Profits* — David A. Lesmond, Michael J. Schill, Chunsheng Zhou — 2004 — *Journal of Financial Economics* 71(2), 349–380 — https://faculty.wharton.upenn.edu/wp-content/uploads/2014/03/Illusion_29Jul2003.pdf — `verified: true`

[6] *Size and Value in China* — Jianan Liu, Robert F. Stambaugh, Yu Yuan — 2019 — *Journal of Financial Economics* 134(1), 48–69 — https://faculty.wharton.upenn.edu/wp-content/uploads/2018/03/Size-and-Value-in-China.pdf — `verified: true`(与 L2 出处[3] 同一篇,两个题目都用到)

---

## 给 PI 的一句总结

四个题目里,**L1 和 L4① 的文献支撑最硬**:核心①的外围计划第 1 条(密度分桶)和 R1 组(密度/零收益当独立特征)都有二十年以上的独立文献先例,不是我们这次现编的。
**L4② 的文献支撑是方向性的**(构造选择能制造/消灭异象),但没有文献专门讨论我们这里的具体机制(NaN 隐式删除);这一条在最终报告里要写清楚是"我们的工程发现,文献给的是同构但不同机的先例"。
**L2 的归一化问题**有文献的标准定义撑着(R2-6 的分母形式就是文献定义本身),但"未归一化版本≈波动水平、因而控制波动后消失"这句话本身没有文献原文直接背书。
**L3 最值得注意的是两条文献独立给出的、analysis.md 目前没列的风险点**:T+1 本身(不靠封板)就会让隔夜段与波动相关;上交所 2018-08-20 引入收盘集合竞价是样本期中段的一次结构性断点,`day_last(Close)` 在这之后的测量性质变了。
