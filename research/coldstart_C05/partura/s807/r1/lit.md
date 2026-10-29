# 文献笔记 — s807 / r1(文献员)

范围:只用 **2023-08-08 之前发表**的论文 / 工作论文 / 研究报告(arXiv、SSRN、机构工作论文系列以首版日期为准)。对 analysis.md §7 的 L1–L4 四个题目逐一检索;每条「处理方式」后标出处编号,对应文末〈参考文献〉。搜不到的地方明确写「搜不到」,不补全、不猜测。

---

## L1 — 已实现半方差 / 符号跳跃变差(对准核心 A:符号无用、幅度有用)

**能翻译成算子语言的处理方式:**

1. **分母:相当一部分文献根本不归一化。** Chao–Liu–Guo [3](中国 A 股、5 分钟数据)把「跳跃」先用 Z 检验从 `RV − BV`(已实现方差减双幂变差)里挑出来,再对正向跳跃和负向跳跃分别求和,**符号跳跃变差 = 正跳跃合计 − 负跳跃合计,单位是原始的跳跃方差,没有再除以 RV、BPV 或 Σ|r|**;月度化时只是求和/求均值/求发生率,不是比率。翻译过来就是:**不是所有「符号半方差之差」都做成 Σ|r| 为分母的比率**——我们现在手里 `day_wmean(Ret, Ret) = (RS⁺−RS⁻)/Σ|r|` 这种显式归一化,在文献里只是其中一种做法,不归一化、直接用绝对尺度的跳跃量也有人用并测出了显著性 [3]。
   **我没有查到** Barndorff-Nielsen–Kinnebrock–Shephard [1] 或 Patton–Sheppard [2] 本身把 RS⁺−RS⁻ 除以 RV / BPV / Σ|r| 做成无量纲比率的具体公式——[1][2] 的检索结果只给出了半方差的构造(用高频收益按符号分桶求平方和),没给出我能确认的「归一化成比率」的那一步。**这一点搜不到实锤,不编。**

2. **绝对值/平方(只要幅度)而非带符号:** Chao–Liu–Guo [3] 测的是**带符号**的 `Sign_Size`(正跳跃 − 负跳跃),发现它在横截面回归里**正向且显著**(系数 0.033,5% 水平),收益随符号跳跃单调上升;同时**负向跳跃单独的解释力更强**(在控制符号跳跃后,负跳跃显著的月份数明显多于仅用负跳跃)。
   **我没有查到**专门把这类信号**取绝对值/平方、只要幅度不要方向**之后再做横截面检验的文献——这正是我们核心 A「折叠有用、符号没用」这条结论在已实现半方差这条线上**缺乏直接对照**的地方,需要标成空白,不能拿「符号版有效」去反推「折叠版也该有效」。

3. **分组:** Chao–Liu–Guo [3] 按**规模(市值)× 账面市值比**做 5×5=25 组 Fama-French 式分组(每年 6 月末按规模分 5 组、按 B/M 分 5 组,交叉),不是按流动性、波动率或涨跌停幅度分组。**没查到**按流动性/波动/涨跌停分组的版本。

4. **周期与股票池:** Chao–Liu–Guo [3] 用 2007–2013 年**5 分钟**的 A 股数据(每天至多 49 笔,含隔夜一笔)。Fang–Jiang–Luo [4] 用 2006–2013 年 A 股高频数据做**指数层面**(非个股横截面)的符号跳跃变差,发现**负向半方差对未来波动的短期预测力更强**,并把这一不对称**部分归因于中国的卖空限制**——这给了一条机制线索:A 股的卖空约束可能让「负向冲击」和「正向冲击」在定价上的不对称比美股更明显,但 [4] 测的是波动率预测、不是收益横截面,不能直接当成「结论反转」的证据,**只能当背景机制参考**。换到 1 分钟 vs 5 分钟的对比**没查到**。

**小结(给 PI 的可用结论):** 文献里确实有「符号跳跃/半方差」这条线,但(i)归一化方式不统一,不归一化的原始跳跃量也是主流做法之一;(ii)目前查到的横截面检验都是带符号的,没有「只取幅度」的直接对照;(iii)A 股特有的卖空约束可能是正负不对称的一个机制,但证据在指数层面、不在个股横截面。核心 A 的「折叠有用」目前**没有文献直接背书**,也**没有文献反对**——这件事本身值得写进 notebook:我们的 head 可能是文献没覆盖到的组合(符号跳跃 + 幅度折叠 + 月度尾部聚合三者叠在一起)。

---

## L2 — 日度统计量的月度聚合方式(对准 §1.4/§1.5:外层 `pow_2` ≈ 窗口取极值,且只在 train 上有效)

**能翻译成算子语言的处理方式:**

1. **均值 vs 窗口最大值 vs 高阶矩,确实有人明确比较过,但比较对象是「IVOL(方差/二阶矩的月度均值聚合)」vs「MAX(月度最大值聚合)」。** Ang–Hodrick–Xing–Zhang [5] 把特质波动率构造成「月内日度残差的标准差」(本质是日度方差的**均值**聚合),发现高 IVOL 组后续收益显著更低,且用 Fama-French 三因子调整后依然存在(即著名的异质波动率之谜)。Bali–Cakici–Whitelaw [6] 则把同一类日度数据改成**月内最大单日收益(MAX)**这个「窗口取极值」聚合,发现 MAX 对收益的负向解释力**覆盖、甚至反转了** IVOL 的解释力——换句话说,**同一批日度数据,换一种月度聚合方式(均值的二阶矩 → 窗口极值),结论的归因会整个转移**,这正是我们 §1.5「`pow_2` 的提升几乎全部来自 20 日 EMA 把均值聚合偏向窗口最大值」这一发现在成熟文献里的对应现象。
   翻译成算子语言:`day_var(Ret)` 的 **cross_mean** 聚合 ≈ IVOL 路线;`pow_2(day_wmean(Ret,Ret))` 的 **cross_max 式**聚合(由 EMA 间接实现)≈ MAX 路线。两条路线在美股文献里是**互相替代、而非互补**的关系。
   **高阶矩(四次幂、Lp 范数)与「均值/中位数/高分位/最大值」的系统对比,我没有查到**专门做这件事的文献(搜了「higher moments aggregation daily signal monthly factor」「Lp norm aggregation」等关键词,只搜到 2024 年之后的「factor MAX」类工作,按规则不能用)。这块是**真空白**,不是我漏查。

2. **控制了 IVOL 之后 MAX 还剩多少:因市场而异,不是放之四海的结论。** 在美股 [6],加入 MAX 之后 IVOL 与收益的负向关系被反转/吸收。但在 **A 股**,Nartea–Kong–Wu [7](A 股个股横截面,2017)明确发现:MAX 效应本身存在(与美欧类似),**但它不削弱、不反转 IVOL 之谜——两者在中国市场是独立共存的**,只能部分支持「彩票偏好」解释。这是一条**直接可用的 A 股结论**:不能照搬美股「MAX 吸收 IVOL」的结论,我们的中性化控制里如果同时放 20 日波动控制和这类月度极值信号,在 A 股上两者可能是**互补**而非替代关系,这点值得提醒 PI。

3. **换手率与成本:原始 MAX 论文自己承认这是实现难点,但没有给出具体数字。** Bali–Cakici–Whitelaw [6] 的研究者自己在论文里指出,MAX 策略的**卖空约束和交易成本**可能让策略难以真正实现(没有查到具体百分比或在扣 15bp 假设下的净值)。更直接相关的是 Hung–Yang [8](2018,聚焦**有涨跌停板**的市场):他们指出原始 MAX 定义在**有价格限制的市场**里会被板子「削平」,导致同质化(很多股票的月内最大收益都被压在板宽上),于是把 MAX **按涨跌停幅度重新标准化**后再做横截面检验,发现修正后的 MAX 仍显著预测收益、且**不是** IVOL 效应的另一种表现。
   这条**直接可翻译**:我们池子里就有 `LimitWidth` 这个叶子,Hung–Yang 的处理方式等价于把 `pow_2(day_wmean(Ret, Ret))` 或其显式窗口极值版本(`cross_max(...)`)**除以 `LimitWidth` 做涨跌停幅度归一化**,这正好呼应 analysis.md §4.1 里「核心 A 外围第 1 族:用 `LimitWidth` 做条件化」的设想,现在有文献支持这个方向机制上合理(板宽越窄,日内「单边」的物理上限越低,信号需要按板宽重新标度才可比)。
   **A 股涨跌停幅度分组(10%/20%/ST 5%)下 MAX 效应是否反转,没有查到专门研究**,只有 Hung–Yang [8] 的方法论可以直接套用。

**小结:** 「均值 vs 极值」聚合在文献里是两条已知会互相替代归因的路线(美股),但在 A 股上独立共存;涨跌停幅度归一化有现成方法论(Hung–Yang)可直接套进我们的算子;「高阶矩的系统性比较」和「A 股涨跌停分组下的 MAX 效应」都是空白。

---

## L3 — 日内路径效率(无量纲化:Σr / Σ|r| 一类)

**能翻译成算子语言的处理方式:**

1. **分母的几种现成选择:** 技术分析文献里最直接对应的是 **Kaufman 效率比(Efficiency Ratio,ER)**[9]:`ER = |窗口净变动| / Σ|逐期变动|`,分母就是逐期绝对变动之和,与我们 `day_signed_ratio(Ret, Ret) = Σr/Σ|r|` 的分母**完全同构**(只是 Kaufman 的版本取了绝对值、是无符号的「趋势强度」,我们的版本保留符号)。这个指标 1995 年提出,默认窗口 10 期,**是技术指标,不是资产定价文献**——我没查到任何同行评审论文把 Kaufman ER 直接拿去做横截面收益检验,它的「阈值」(0.6、0.75 等)全部来自交易平台文档,不是统计检验出来的。
   另一个可比的分母选择是 **Amihud [10] 的非流动性比率**:`|日收益| / 当日成交额`,分母换成了**成交额**而不是「逐期绝对变动」——这是构造「无量纲化」时的第三种分母候选(我们现在只讨论了 Σ|r|,`day_var`,还没试过日度口径的 Amihud 式分母),可以作为 R 或下一轮 E 的一个变体方向:`div(pow_2(day_wmean(Ret,Ret)), Amt)` 这类换分母的尝试,机制上对应 Amihud 的「价格冲击」解释而不是「路径效率」解释。
   **Parkinson 式高低价区间**作为分母,**我没有查到**可核实的来源,搜不到就不编。

2. **「计数版」的路径效率在动量文献里确实被系统测过,但和我们的「幅度加权版」不是同一个东西,需要分开看。** Da–Gurun–Warachka [11] 的「信息离散度」(Information Discreteness, ID)用的是**月内正收益天数占比 − 负收益天数占比**(按天数计数,不按收益幅度加权),发现 ID 低(即路径连续、小碎步上涨)的动量组合比 ID 高(少数几天跳涨)的动量组合**后续收益更高、持续更久**(六个月持有期,连续信息组合的动量收益显著高于离散信息组合,且前者的显著性能维持约 8 个月、后者约 2 个月就不显著了)。
   这给了一个**可直接复用的机制类比**:ID 是「计数」版的路径效率(`day_signed_ratio` 用的是「幅度」版,`Σsign(r)/N` vs `Σr/Σ|r|`),两者测的都是「同样的累计收益,是走出来的还是跳出来的」,但 ID 面向的是**动量延续性**,不是我们这里要的「横截面收益水平预测」。**没有查到**把 ID 或类似计数版路径效率,像我们这样直接当作一个独立的横截面预测变量(而不是动量的调节变量)来测的文献——这是个空白,但 ID 本身是个可以抄的「计数版」处理方式,可以放进 N 候选:`div(day_signed_ratio(Ret,Ret), ...)` 换成基于天数计数而不是幅度加权的版本。

3. **控制波动与流动性之后还剩多少:没有查到直接证据。** [9] 是技术指标文档、没有做任何横截面控制变量检验;[11] 控制的是动量延续性的调节效应,不是独立定价能力;Amihud [10] 本身是用来**证明**流动性溢价存在的,不是用来"排除"流动性因素后检验别的信号。**这一条——"路径效率在控制了波动和流动性之后还能不能独立预测收益"——搜不到直接文献,是空白**,这恰好说明核心 A 如果真的"扣掉波动尾部空对照(R1/R2)后仍然显著",可能是文献没覆盖到的新结果,不是被文献证伪的方向。

4. **与薄交易/零收益混淆:没有文献直接连接,但有结构性重叠值得注意。** Lesmond–Ogden–Trzcinka [12] 提出用**月度零收益天数占比**来估计有效交易成本(隐含假设:成本太高时,信息不足以推动价格变动,当日收益记为 0),这是最常见的「零收益 = 薄交易/流动性差」代理,1963–1990 年美股大盘股/小盘股的隐含双边成本分别约 1.2%/10.3%。**我没有查到**文献把这个零收益占比,和「Σr/Σ|r| 类路径效率」的分母放在一起讨论过混淆问题——但结构上两者共享同一个薄弱环节:零收益天数多时,我们这类比率的**分母 Σ|r| 会被同时拉小**,这是算子本身的性质决定的,不是文献告诉我们的,**这句是我自己的推断,不是引用**,写出来提醒 PI 区分。

5. **A 股涨跌停分组:没查到。** 没有查到把路径效率/效率比这类指标按涨跌停幅度(10%/20%/ST 5%)分组或归一化、并在 A 股做检验的文献。

**小结:** `day_signed_ratio` 式的「幅度加权路径效率」在严肃资产定价文献里基本是空白;最接近的两条线——Kaufman ER(技术指标,无回测)和 Da-Gurun-Warachka 的 ID(计数版,服务于动量调节而非独立定价)——都不是同一个问题的直接答案。这意味着核心 A 的外围族如果往这个方向长,**大概率是在做文献没做过的事**,风险和机会并存:没有先验可以借用方向和窗口,但也没有被文献证伪的顾虑。

---

## L4 — 日内资金流失衡(分钟 K 线、无逐笔数据)

**能翻译成算子语言的处理方式:**

1. **构造法——学界有三条明确路线,其中两条可以在分钟 K 线上直接算,不需要逐笔方向数据:**
   - **成交量加权收益(VWAP 偏离)**:Kaniel–Saar–Titman [13](美股 NYSE)用的是机构数据折算的个人净买卖强度,不是分钟 K 线,但他们的**核心发现方向性**可以直接类比我们的通道:个人投资者在**上月下跌后买入、上涨后卖出**(逆势),随后一个月里,被个人大量买入的股票**超额收益为正**,被大量卖出的**超额收益为负**——这是"净买卖强度(符号)→ 下月收益"的月度预测关系,我们的 `day_signed_ratio(Ret, Amt)` 如果要类比检验,应该先看**符号**是否预测下月收益,而不是先假设"幅度不分方向"。
   - **分块成交量分类(Bulk Volume Classification, BVC)**:Easley–López de Prado–O'Hara [14] 提出的 VPIN 框架,专门解决"没有逐笔买卖方向标记、只有成交量和价格变动"时如何估计买卖不平衡——用价格变动的标准化幅度(或符号)把每个时间/成交量桶的成交量按比例分配给"买方发起"和"卖方发起",这**正是我们 `day_signed_ratio(Ret, Amt)`(按分钟收益符号把成交额分成"上涨分钟"和"下跌分钟"两堆再求差)的学术对应方法**——只是 VPIN 用的是更精细的正态分布加权分配,我们的版本是硬分类(符号为正全归上涨、为负全归下跌),可以理解成 BVC 的一个简化/离散版本。
   - **Amihud 式分母**[10]:用日度"|收益|/成交额"做价格冲击代理,也是"只用日度量价、不需要逐笔"的同类思路,但它测的是流动性溢价不是资金流失衡的方向。

2. **归一化:文献里能查到的是"用成交额/成交量做分母",没有查到"换成过去 N 日均额"或"换手率"这种滚动归一化的具体先例。** VPIN [14] 本身在"成交量时间"(volume time,把时钟按等成交量而非等时间分桶)上定义,这是一种归一化思路,但和我们"除以过去 N 日均额"的做法不是同一回事,**不能混用**。`LogFloatCap` 之类的归一化在这两篇里都没出现——这条分组/归一化的具体数值选择,**文献没有给出,需要我们自己试(R/E 里已经有 `LogFloatShares`、`LogFloatCap` 条件化,这是合理的,只是不是文献抄来的,是我们自己的推断)**。

3. **预测符号还是幅度,聚合多少天:** [13] 测的是**符号**(净买 vs 净卖),聚合窗口是**一个月**,预测下一个月的收益——这个时间尺度刚好和我们 head 的"约一个月尾部聚合"一致,是个好的类比对象,但它预测的是符号而不是"不分方向的幅度",这和 analysis.md §4.3 「幅度(不分方向)负向预测收益」的假设**方向上不完全对应**,需要提醒 PI:如果 N 位的种子测出来的是"符号"而不是"幅度"在起作用,那是在复刻 [13] 的机制,不是发现新东西;只有确认"折叠/取绝对值后依然显著、且比带符号版更强"才算是真正在测新的"幅度"假设。

4. **与流动性/成交量/波动区分开:** VPIN 框架 [14] 的全部意义就是想把"知情交易/订单流失衡"和单纯的"流动性水平"分开,但其同一批作者后续用更精细的逐笔数据比较发现 BVC 对"买卖方发起方向"的分类准确度本身是有限的(只在"分块聚合"意义上好用,不代表能精确还原逐笔方向)——这条提醒我们:`day_signed_ratio(Ret, Amt)` 这种硬分类本身就带有分类噪声,和"高波动期噪声更大"是混在一起的,**文献没有告诉我们怎么把这两者分开**,这是空白。

5. **A 股可比研究:搜到的是行业/券商材料,学术论文搜不到可核实的。** 搜索找到一份深交所转载的研究材料(侯丽薇、谢赤等,湖南大学与国信证券),用 A 股分钟级高频数据统计发现"资金净流入对未来股票收益率呈中期反转"——即资金流入多的股票中期反而可能走弱,方向与我们 §4.3 假设的"负向预测"**部分一致**(都是负向),但**我无法核实这份材料的发表年份、期刊/载体和检索链接的稳定性**,只在深交所网站的 PDF 上看到标题和作者,**按规则列入参考文献但标 `verified: false`**,PI 决策时不要把它当成可靠学术证据,只能当线索。
   另外搜到"聪明钱因子"这条路线(国内量化卖方的分钟数据"聪明钱"指标,对应的经济含义接近 `day_topw_mean`:挑出"最聪明"的分钟、看这些分钟的成交量加权均价相对全天 VWAP 的偏离),据二次引用其原始方法论来自魏建榕、傅开波、高鹏(2020)的卖方研究,**但我只在一篇 2026 年的后续研报里看到对 2020 年原始方法的转述,没有直接打开 2020 年原文核实,标 `verified: false`**。真正核实、且是同行评审、并明确做了 A 股个股横截面检验的,是 Chen–Liu–Teka–Zhang [15](2022,*Research in International Business and Finance*):用 1999–2019 年 A 股 1 分钟成交数据构造"分笔聪明度"指标,识别知情交易方向,发现**聪明钱指标与个股未来收益呈负向横截面关系**,基于模糊 C 均值聚类构造的策略年化夏普 1.169,跑赢常规分组策略。这条可以放心引用(`verified: true`),且时间尺度(月度测量)、股票池(A 股)都对得上我们的场景,只是具体"聪明度"的打分公式我没能从检索结果里拿到完整定义,**构造细节本身没有核实到,只核实了"存在这篇论文、结论方向、数据范围"**。

**小结:** `day_signed_ratio(Ret, Amt)` 有扎实的学术对应(VPIN/BVC 框架),`day_topw_mean(Ret, Amt)` 有一篇可核实的 A 股同行评审证据([15],负向横截面关系,量级为年化夏普 1.169 的策略效果,不是单因子 IC),符号预测優先于幅度预测在美股有直接证据([13])。国内"聪明钱"卖方方法论本身只有二次转述、未核实。

---

## 参考文献

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|---|
| 1 | Measuring Downside Risk: Realised Semivariance | Ole E. Barndorff-Nielsen, Silja Kinnebrock, Neil Shephard | 2008-02(工作论文首版,Nuffield College Economics WP 2008-W2);正式收录 2010(*Volatility and Time Series Econometrics: Essays in Honor of Robert F. Engle*, OUP, pp.117–136) | Nuffield College Economics Discussion Paper / OUP 书章 | https://www.nuffield.ox.ac.uk/economics/Papers/2008/w2/downside.txt ; https://ideas.repec.org/p/nuf/econwp/0802.html | true |
| 2 | Good Volatility, Bad Volatility: Signed Jumps and The Persistence of Volatility | Andrew J. Patton, Kevin Sheppard | 2015(*Review of Economics and Statistics*, Vol. 97, No. 2, pp. 683–697);工作论文版本至少 2011-10 流传(public.econ.duke.edu PDF 落款 "7oct11") | Review of Economics and Statistics / Duke 工作论文 | https://ideas.repec.org/a/tpr/restat/v97y2015i2p683-697.html ; https://public.econ.duke.edu/~ap172/Patton_Sheppard_Realized_Semivariance_7oct11.pdf | true(存在性、期刊卷期确认;归一化分母的具体公式未核实,见正文) |
| 3 | Sign realized jump risk and the cross-section of stock returns: Evidence from China's stock market | Youcong Chao, Xiaoqun Liu, Shijun Guo | 2017-08(*PLoS ONE*, 12(8): e0181990;收稿 2016-08-28,接收 2017-03-29) | PLoS ONE | https://pmc.ncbi.nlm.nih.gov/articles/PMC5542663/ | true(WebFetch 直接读取全文摘要内容) |
| 4 | Realized Semivariances and the Variation of Signed Jumps in China's Stock Market | Fang, Jiang, Luo | 2017(*Emerging Markets Finance and Trade*, 53(3), pp. 563–586) | Emerging Markets Finance and Trade | https://ideas.repec.org/a/mes/emfitr/v53y2017i3p563-586.html | false(只看到搜索引擎的二次归纳描述,未直接核实原文摘要页) |
| 5 | The Cross-Section of Volatility and Expected Returns | Andrew Ang, Robert J. Hodrick, Yuhang Xing, Xiaoyan Zhang | 2006-02(*Journal of Finance*, Vol. 61, pp. 259–299);NBER WP 10852, 2004-10 | Journal of Finance / NBER | https://www.nber.org/papers/w10852 | true |
| 6 | Maxing Out: Stocks as Lotteries and the Cross-Section of Expected Returns | Turan G. Bali, Nusret Cakici, Robert F. Whitelaw | 2011-02(*Journal of Financial Economics*, Vol. 99, No. 2, pp. 427–446);NBER WP 14804, 2009-03 | Journal of Financial Economics / NBER | https://www.nber.org/papers/w14804.pdf | true |
| 7 | Do extreme returns matter in emerging markets? Evidence from the Chinese stock market | Gilbert V. Nartea, Dongmin Kong, Ji Wu | 2017(*Journal of Banking & Finance*, Vol. 76, pp. 189–197) | Journal of Banking & Finance | https://ideas.repec.org/a/eee/jbfina/v76y2017icp189-197.html | true |
| 8 | The MAX Effect: Lottery Stocks with Price Limits and Limits to Arbitrage | Weifeng Hung, Jimmy Yang | 2018(*Journal of Financial Markets*, Vol. 41, pp. 77–91) | Journal of Financial Markets | https://ideas.repec.org/a/eee/finmar/v41y2018icp77-91.html | true(摘要核实;样本市场细节未核实到全文) |
| 9 | Efficiency Ratio(效率比) | Perry J. Kaufman | 1995(《Smarter Trading》一书提出;非期刊论文) | 书籍 / 交易平台文档转述 | https://doc.stocksharp.com/en/topics/api/indicators/list_of_indicators/kaufman_efficiency_ratio | true(指标定义与出处书名多处交易平台文档确认一致;非同行评审检验) |
| 10 | Illiquidity and Stock Returns: Cross-Section and Time-Series Effects | Yakov Amihud | 2002(*Journal of Financial Markets*, Vol. 5, pp. 31–56) | Journal of Financial Markets | https://www.casact.org/abstract/illiquidity-and-stock-returns-cross-section-and-time-series-effects | true |
| 11 | Frog in the Pan: Continuous Information and Momentum | Zhi Da, Umit G. Gurun, Mitch Warachka | 2014(*Review of Financial Studies*, DOI 10.1093/rfs/hhu003);工作论文至少 2010 年即在 SMU 存档流传 | Review of Financial Studies / SMU 工作论文存档 | https://ink.library.smu.edu.sg/lkcsb_research/2994 ; https://www3.nd.edu/~zda/Frog.pdf | true(标题、作者、发表信息经图书馆目录与机构存档确认;具体 ID 公式的逐字定义未在本次检索中直接核验,数值引自二次转述) |
| 12 | A New Estimate of Transaction Costs | David A. Lesmond, Joseph P. Ogden, Charles A. Trzcinka | 1999(*Review of Financial Studies*, Vol. 12, No. 5, pp. 1113–1141) | Review of Financial Studies | https://www.bauer.uh.edu/rsusmel/phd/lot_1999RFS.pdf | true |
| 13 | Individual Investor Trading and Stock Returns | Ron Kaniel, Gideon Saar, Sheridan Titman | 2008-02(*Journal of Finance*, Vol. 63, No. 1, pp. 273–310) | Journal of Finance | https://ideas.repec.org/a/bla/jfinan/v63y2008i1p273-310.html | true |
| 14 | Flow Toxicity and Liquidity in a High-Frequency World | David Easley, Marcos López de Prado, Maureen O'Hara | 2012(*Review of Financial Studies*, Vol. 25, No. 5, pp. 1457–1493) | Review of Financial Studies | https://ideas.repec.org/a/oup/rfinst/v25y2012i5p1457-1493.html | true |
| 15 | Smart money in China's A-share market: Evidence from big data | Zhenhua Chen, Zhenya Liu, Hanen Teka, Yifan Zhang | 2022(*Research in International Business and Finance*, Vol. 61, Article 101663) | Research in International Business and Finance | https://ideas.repec.org/a/eee/riibaf/v61y2022ics0275531922000514.html | true(存在性、作者、期刊、主结论核实;"聪明度"打分公式细节未核实) |
| 16(存疑,不建议引用为学术证据) | 资金流向对 A 股未来收益率呈中期反转(深交所转载研究材料) | 侯丽薇、谢赤等(湖南大学 / 国信证券) | 不详 | 深交所研究资料 PDF | https://szse.cn/aboutus/research/secuities/documents/P020180328492183310238.pdf | false(发表年份、期刊/载体均未能核实,只核实到标题与作者线索) |
| 17(存疑,不建议引用为学术证据) | 聪明钱因子 2.0(原始方法论,仅经二次转述) | 魏建榕、傅开波、高鹏(卖方研究,据称 2020) | 2020(未直接核实) | 卖方研究报告(仅见于 2026 年后续报告的转述) | https://finance.sina.cn/2026-08-29/detail-inipyfhv5524506.d.html(转述来源,非原文) | false(原始报告未直接检索到,发表机构、具体日期均未核实) |

---

## 给 PI 的检索空白清单(明确搜不到,不要当成"文献证伪")

- L1:没有查到「符号半方差之差取绝对值/平方(只要幅度)」的横截面检验;没有查到按流动性/波动/涨跌停分组的版本;没有查到 1 分钟 vs 5 分钟频率对比。
- L2:没有查到「均值 / 中位数 / 高分位 / 高阶矩」五种月度聚合方式的系统性横向比较;没有查到 A 股按涨跌停幅度分组(10%/20%/ST 5%)下 MAX 效应是否反转的研究。
- L3:没有查到任何同行评审文献把「Σr/Σ|r| 式无量纲路径效率」直接当横截面收益预测变量、并控制波动与流动性做检验;没有查到 Parkinson 型高低价区间作为此类比率分母的来源;没有查到与零收益/薄交易混淆问题的直接讨论;没有查到 A 股涨跌停分组版本。
- L4:没有查到"换成过去 N 日均额/换手率"这类滚动归一化在资金流失衡指标里的具体先例;没有查到把 BVC 分类噪声与波动率噪声分开的方法;国内"聪明钱"原始方法论(魏建榕等 2020)与深交所资金流反转材料均未能直接核实,只能作为线索而非证据。
