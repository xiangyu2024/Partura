# 文献:种子 804,C 组,第 3 轮

输入:`r3/analysis.md` 第 6 节「文献题目」(4 题,分别对准核心 ①、核心 ②/N 灵感 2、核心 ③/N 灵感 3、R-2 与最终库标注)。
约束:只用 **2023-08-08 之前**发表/上线/存档的论文、工作论文或机构研究报告(arXiv / SSRN 以首版日期为准);日期拿不准的一律不用。
工具:WebSearch(多轮)+ WebFetch(核对个别条目的日期/数字)。

**与 r1、r2 的分工**(避免重复检索):
- 题 1 的理论源头(Admati-Pfleiderer、Heston-Korajczyk-Sadka、Gao et al.、Blau et al.)已在 **r1 lit.md 题 4** 备好,本轮不重复搜,只处理「水平 vs 变化」「投资者结构代理」「分组内中性化」这一层。
- 题 3 的 Amaya et al. 已在 **r2 lit.md 题 2** 逐页核实过偏度方向与「5 分钟 + 排除低价股」的操作性理由,本轮只补**峭度**方向、以及跳跃度量 / 零收益比例这两个新角度,不重复偏度部分的论证。
- 题 4 的 MSCI Barra Non-linear Size(立方 + 正交化)已在 **r1 lit.md 题 2** 和 **r2 lit.md 题 1** 两处逐页核实过,本轮不重复,只补「非单调规模的具体机制(壳价值 / 指数边界)」与「不同量纲相减」这两个没碰过的角度。
- 题 4 的「条件排序 vs 独立排序」方法学背景(Cattaneo-Crump-Farrell-Schaumburg)已在 **r1 lit.md 题 3** 给过,本轮不重复,只在用到的地方点一下。

---

## 题 1(对准核心 ①、真来源 A):日内成交时点是「稳定的公司特征」还是「时变信号」?

### 1.1 能翻译成算子语言的处理方式

1. **检验「量—价关系的方向本身随某个投资者结构代理变化」,而不是假设机制对所有股票统一。**
   Llorente, Michaely, Saar & Wang 的模型里,风险分担型交易产生收益反转、信息型交易产生收益延续,同一只股票在不同时期这个关系的强弱随知情交易占比变化,
   作者用换手率的系统性/非系统性分解去代理这个占比 [①]。→ 对应到我们的结构:不要只问「`day_centroid(sqrt(Volume))` 整体上赚不赚钱」,
   而要在 `cross_mean(day_std(Amt), 30)` 或 `LogFloatShares` 分组内检验它对未来收益的预测方向是否单调变化——如果方向随分组翻转,
   支持「这是参与者结构代理」;如果方向处处一致,更像「统一的信息释放时点」。这正是核心①外围 (a) 桶内排序要做的事,文献给的是**检验思路**而不是现成答案。
2. **「换手率(广义的成交活跃度)」本身可以分解成几乎不随时间变的公司特定部分,和带趋势的系统性部分,这个分解是标准做法。**
   Cremers & Mei 用 Bai-Ng 的因子方法把个股换手率拆成系统性(带时间趋势)和特质性(接近平稳)两块,并证明 Lo & Wang (2000) 「收益和换手率系统性因子数目相同」
   这个限制被数据拒绝 [②]。→ 支持核心①外围 (c) 的实验方向(`sub(ts_mean(·, 20), cross_mean(·, 240))` 拆水平和变化)本身是文献里验证过的标准操作,
   不是我们自己瞎猜的切法;但也提醒:即使拆出来,「哪一块是真正跨年稳定的公司特征」在文献里本身就有争议(系统性部分也有特质性残留),不要指望拆完就是干净的两段。
3. **用「分组内按特征匹配」替代「线性回归取残差」,是把特征和因子暴露分开的标准方法,不是我们自创的权宜之计。**
   Daniel, Grinblatt, Titman & Wermers 构造基准组合的方法是:按规模、账面市值比、动量分别分组,再用股票实际持有的那个格子的平均收益做基准,
   而不是对协变量做线性回归取残差 [③]。→ 这正是核心①外围 (a) `cs_bucket_rank`/`cs_bucket_zscore` 这类「先分桶再排序」写法在文献里对应的方法论,
   支持 PI 把这当成「比线性中性化更贴近文献标准」的处理,而不只是「换一种写法通过审计」。
4. **把「成交时点的形状」当成投资者类型的代理,文献标准做法是直接从逐笔报价里识别交易方向(次分钱价格标记零售单),而不是从日内形状反推。**
   Boehmer, Jones, Zhang & Zhang 用公开的逐笔数据里次分钱(sub-penny)价格改善这个特征标记零售成交,验证发现零售净买入在长达 12 周的
   窗口里能预测**更低**的未来收益 [④]。→ 这提醒我们一件事要对 PI 说清楚:`day_centroid(sqrt(Volume))` 只是成交量**形状**的代理,
   不是真实的投资者类型标签;文献里真正干净的「谁在交易」识别靠的是逐笔报价特征,我们的分钟立方体做不到这一步,只能退一步用成交量形状做代理,
   这个局限应该写进计划,而不是把 `day_centroid` 包装成「投资者结构的直接测量」。
5. **被动资金的持股比例与「尾盘集中成交」在横截面上直接挂钩,而且这个关系的强度本身随被动基金份额增长在十几年里系统性增强。**
   Shen & Shi 用 2004–2018 年标普 500 全部成分股的逐秒数据发现:被动持股比例高的股票成交量更集中在收盘前,被动持股比例低的股票成交量更集中在开盘后
   (「活跃开盘、被动收盘」的日内形态),且一只股票被从标普 500 剔除后,其收盘前成交量会立刻大幅下滑 [⑤]。→ 这给了「成交质心靠后」一个具体、
   可检验的第三种候选解释——不是「信息在开盘集中释放」也不是「散户早盘下单/机构尾盘执行」,而是**被动/指数资金占比**,这与核心②、N 灵感 2
   (收盘集合竞价占比)其实很可能是同一个潜在因,不是两件独立的事,PI 在 N 灵感 1 里做「信息释放 vs 参与者结构」二分的时候,应该把「被动占比」
   作为第三个候选列出来,并且用相关度表检查核心①(质心)与核心②(尾盘占比)的 |ρ| 是不是已经高到说明它们在测同一个东西。
   同时这篇的「关系强度随时间增强」这个发现本身回答了题目「长期水平还是变化」的问题,给出一个具体的答案:**横截面排序(谁的质心更靠后)可能相对稳定,
   但这个排序对收益的解释力本身是随时间(随被动资金份额)变化的**,不是一个简单的「是/否」二选一。
6. **A 股现有的日内专门结果集中在收益侧(尾盘动量),不是成交量时点分布本身——这是一个值得明说的空白,不是「已经测过换个市场」。**
   杨璐(2022)用 2012–2017 年高频数据,把交易日切成 8 个半小时段,发现最后一个半小时收益能被前一个半小时(第 7 段)显著预测,
   沪深 300 上预测 R² 约 3.8%,并借助 A 股 ETF 的 T+0 规则构造了年化约 12.4% 的策略 [⑥]。→ 这证实 A 股确实有「日内后段」效应的专门研究,
   但测的是**收益动量**,不是「成交量质心/时点分布作为横截面特征」这件事本身,不能当成题目要的那个问题已经有 A 股答案。

**没找到、如实注明搜不到**:专门把「日内成交量时点分布」当**横截面特征**、给出明确方向(偏早/偏晚哪边随后更好)、并且专门讨论
「长期水平 vs 变化」这个区分的单篇论文(美股或 A 股均未找到)。Heston-Korajczyk-Sadka 一类测的是**收益**的日内持续性,不是**成交量形状**本身作为
排序变量;Shen-Shi 测的是「被动持股比例 → 成交量时点」这个因果方向,不是「成交量时点 → 未来收益」。这两条合在一起只能**间接**支持核心①的假说,
不能引用成「文献已经证明」。

### 1.2 文献出处

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|---|
| ① | Dynamic Volume-Return Relation of Individual Stocks | Guillermo Llorente, Roni Michaely, Gideon Saar, Jiang Wang | 2002(Review of Financial Studies, vol. 15 no. 4, pp. 1005–1047) | Review of Financial Studies | https://www.johnhcochrane.com/s/llorente_michaely_saar_wang_volume_rfs.pdf | true |
| ② | Turning Over Turnover | Martijn Cremers, Jianping Mei | 2003–2004(NYU 工作论文);2007(正式发表,Review of Financial Studies, vol. 20 no. 6, pp. 1749–1782) | NYU 工作论文 / Review of Financial Studies | https://archive.nyu.edu/handle/2451/27250 | true |
| ③ | Measuring Mutual Fund Performance with Characteristic-Based Benchmarks | Kent Daniel, Mark Grinblatt, Sheridan Titman, Russ Wermers | 1997-07(vol. 52 no. 3, pp. 1035–1058) | Journal of Finance | https://ideas.repec.org/a/bla/jfinan/v52y1997i3p1035-58.html | true |
| ④ | Tracking Retail Investor Activity | Ekkehart Boehmer, Charles M. Jones, Xiaoyan Zhang, Xinran Zhang | 2021(vol. 76, pp. 2249–2305,DOI 10.1111/jofi.13033) | Journal of Finance | https://doi.org/10.1111/jofi.13033 | true |
| ⑤ | Index-based Investing and Intraday Stock Dynamics | Yiwen Shen, Meiqi Shi | 2020(SSRN 工作论文 abstract_id=3696124;Quantpedia 转述页标注 2020-11-19) | SSRN 工作论文(本条经 Quantpedia / IBKR 二级转述确认,未能直接打开 SSRN 页面原文) | https://papers.ssrn.com/abstract=3696124 | true |
| ⑥ | Last hour momentum in the Chinese stock market | Lu Yang | 2022(China Finance Review International, vol. 12 no. 1, pp. 69–100,DOI 10.1108/CFRI-06-2021-0106) | China Finance Review International | https://ideas.repec.org/a/eme/cfripp/cfri-06-2021-0106.html | true |

说明:⑤ 是本题最关键的一条,但我没能直接打开 SSRN 原文(403),内容来自 Quantpedia 与 Interactive Brokers 的转述,转述里给出的说法比较具体
(「高被动持股股票在收盘前成交更多,低被动持股股票在开盘后成交更多」「股票被剔除出标普 500 后收盘前成交量骤降」),判断为确实检索到了这些具体内容,
故标 `true`,但 PI/审计员如果要进一步提高置信度,应自己去核对 SSRN 原文。

---

## 题 2(对准核心 ②、N 灵感 2):尾盘与收盘集合竞价的成交占比

### 2.1 能翻译成算子语言的处理方式

1. **收盘集合竞价本身在美股的量级参照,以及一个关键的「反转」证据:竞价造成的价格偏离会在隔夜被修正掉,不构成新信息。**
   Bogousslavsky & Muravyev 发现收盘集合竞价这一笔交易占 2018 年美股日成交量的约 7.3%,与 ETF 持股比例和机构再平衡高度相关,
   但这笔巨量成交对价格发现**没有贡献**;收盘价经常显著偏离收盘时的买卖中间价,但这些偏离会在隔夜**完全反转** [①]。
   → 这给核心②一个可以直接执行的拆分检验:把 `div(day_sum(mul(Amt, is_gt(in_index(Amt), 0.9875))), day_sum(Amt))` 这个**占比水平**,
   和「收盘价对竞价前瞬间中间价的偏离幅度」分开构造成两个变量分别测试——如果我们读到的 alpha 主要来自后者(价格被竞价机械推离的噪声),
   文献给的先验是它该在次日开盘前反转、不是真实信息;如果 alpha 只来自占比水平本身(不涉及价格偏离),才更接近「被动资金占比的代理」这个叙事。
2. **被动持股比例越高,成交越集中在收盘前**(与题 1 ⑤ 共享同一篇)。
   → 核心②很可能和核心①测的是同一个潜在因(被动/指数资金占比),这正是 analysis.md 自己担心的「创新度会被审计员判成同机制改窗口」的实质来源,
   PI 如果要把两者都立项,应该先在相关度表里确认二者 |ρ| 的具体数字,而不是假设它们天然独立。
3. **如果担心收盘占比里混进了操纵性质的极端样本,文献给的是一个可操作的识别思路,而不是「信号自己会把这维度剔除干净」。**
   Comerton-Forde & Putniņš 用一批被起诉的操纵案例,构造了一个「操纵概率/强度」指数,量化操纵行为对交易特征和价格准确性的影响 [②]。
   → 这提示:如果要把「被动资金占比」和「收盘价操纵」这两种可能污染源分开,标准做法是单独构造一个辅助的「异常」过滤变量
   (例如竞价窗口内成交量/价格波动相对该股历史分布的异常程度),再把它当排除筛或条件变量,而不是指望占比类主信号自己干净。
4. **中国 2018 年引入收盘集合竞价之后,确实有专门的自然实验研究,但结论是「流动性几乎没变,波动和连续性的结构变了,且集中在小盘股」。**
   上交所于 2018-08-20 实施收盘集合竞价(深交所此前已运行约两年)。韩乾、赵呈志、陈静、郭倩用双重差分设计发现:
   该改革对市场流动性没有显著影响,但把一部分成交从「收盘连续竞价的最后一刻」挪到了「集合竞价前的临近时段」,临近收盘前的波动率上升,
   收盘价与临近收盘价的连续性得到改善,且这些效应在小盘股里最明显 [③]。→ 两点直接可用:(a) 这正是题目问的「中国 2018 年引入后有没有相关研究」
   的答案,是,而且效应集中在小盘股,方向上与核心②实测的 `rho_known`/`rho_liq` 偏高(§5.1 已测 0.46/0.46)一致——小盘股流动性更差,
   收盘集合竞价机制对它们的影响本身更大,这支持「核心②读到的部分信息和流动性/规模纠缠」这个怀疑,不是巧合;
   (b) 如果我们的 train 窗口(2018–2021)跨过了 2018-08-20 这个改革日期,`0.875`/`0.9875` 这两个时段常数在改革前后对应的制度含义不同
   (改革前最后几分钟是连续竞价,改革后是集合竞价),这是一个必须核对的数据细节,PI 写计划时应该说明窗口是否跨越改革日、是否需要分段处理。

**没找到、如实注明搜不到**:专门针对「收盘集合竞价占比」与「尾盘连续竞价占比」在**经济含义上是两件不同的事**(一次性撮合 vs 连续执行)
这个具体对比做横截面检验的论文——Bogousslavsky-Muravyev 和 Han et al. 分别研究了竞价本身的机制和改革的市场质量效应,
但没有一篇直接把「两种尾盘成交占比」放在同一个横截面回归里比较谁更干净地代理被动资金。这个对比目前只能靠我们自己在相关度表和 R 评估里做。

### 2.2 文献出处

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|---|
| ① | Should We Use Closing Prices? Institutional Price Pressure at the Close(工作论文标题;正式发表题目为 "Who Trades at the Close? Implications for Price Discovery and Liquidity") | Vincent Bogousslavsky, Dmitriy Muravyev | 2019-11(工作论文,二级页面标注 2019-11-12);2023(正式发表,Journal of Financial Markets, vol. 66) | 工作论文 / Journal of Financial Markets | https://optionmetrics.com/?p=327 | true |
| ② | Measuring Closing Price Manipulation | Carole Comerton-Forde, Tālis J. Putniņš | 2011(Journal of Financial Intermediation, vol. 20 no. 2, pp. 135–158,DOI 10.1016/j.jfi.2010.03.003) | Journal of Financial Intermediation | https://opus.cloud1.lib.uts.edu.au/bitstream/10453/18830/1/2011002687.pdf | true |
| ③ | Reexamining the impact of closing call auction on market quality: A natural experiment from the Shanghai stock exchange | Qian Han, Chengzhi Zhao, Jing Chen, Qian Guo | 2022(Pacific-Basin Finance Journal, vol. 74, 101821,DOI 10.1016/j.pacfin.2022.101821) | Pacific-Basin Finance Journal | https://ideas.repec.org/a/eee/pacfin/v74y2022ics0927538x22001160.html | true |

说明:① 的「2019-11-12」是我在 OptionMetrics 的二级转述页面上直接看到的日期标注,不是 SSRN 原始页面(没能打开),PI 如果要在计划里引用
「首版日期」,应自己去核实 SSRN 的 posted date;即便该工作论文最终发表版本(2023,Journal of Financial Markets)本身已晚于本题截止日期,
但按规矩 SSRN/工作论文以**首版**日期为准,2019 年的版本可以用。③ 的作者顺序和单位信息来自 Cardiff/Birkbeck 两个机构repository 的转述,
核心数字(流动性无显著影响、成交挪到临近收盘前、小盘股效应最明显)在多个独立转述源之间一致,判断为可信。

---

## 题 3(对准核心 ③):分钟 |收益| 的峰度、零收益分钟占比、价位离散化

### 3.1 能翻译成算子语言的处理方式

1. **峭度的方向参照(与 r2 已核实的偏度方向对照):文献给的是「高峭度 → 略高的下一期收益」,方向为正,但比偏度弱、也不总是显著。**
   Amaya et al. 的工作论文版本报告「买最高已实现峭度十分位、卖最低」的多空组合约 16bp/周(t = 2.98);正式发表的 JFE 版本摘要把峭度的关系
   描述为「为正但不总是显著」,显著性和稳健性都明显弱于偏度(偏度 19bp/周,t = 3.70)[①,与 r2 lit.md 题 2 ① 同一篇,此处只取峭度结论]。
   → 这给 `day_kurt(abs_(Ret))` 一个可以直接对照的先验方向:如果我们读到的是「干净」的已实现峭度,方向应该是「高峭度票随后收益略高」,
   量级应该比偏度弱很多;而我们现在 valid 夏普 1.52 远高于文献里偏度(更强的那个效应)的量级,这个「量级倒挂」本身就是支持
   §2.3「它可能不是真峭度、是别的东西的单调函数」怀疑的一条间接证据,值得在计划里明说。
2. **把「跳跃」从「峭度」里剥离出来,文献有现成的工具,不需要我们自己发明——已实现方差与二次幂变差之差,只对跳跃敏感,对连续部分的高峭度不敏感。**
   Barndorff-Nielsen & Shephard 证明:在「扩散 + 偶发跳跃」模型下,已实现方差(RV)收敛到积分方差加跳跃的二次变差,而二次幂变差(bipower variation,BV)
   只收敛到积分方差本身,两者之差就分离出了跳跃部分 [②]。Huang & Tauchen 在此基础上提出相对跳跃度量 RJ = (RV − BV)/RV。
   → 如果 PI 想把「跳跃/信息冲击」和「零收益分钟占比污染」这两种读法分开,可以在 train 上粗配一个日内版的 RV−BV 差(或 RJ),
   分别检验它与 `day_kurt(abs_(Ret))`、`day_zero_ratio(Ret)` 的相关:如果 `day_kurt` 和跳跃度量高相关、和零收益占比低相关,支持「读到的是真跳跃」;
   反过来则支持解剖员的怀疑。这是比「换采样频率」更直接的分离方法,文献里是现成公式,不需要我们重新论证。
3. **跳跃尾部风险本身在文献里是被定价的独立维度,但证据在指数层面,不在个股横截面,不能直接套用到我们的 `day_kurt`。**
   Bollerslev & Todorov 用期权隐含的跳跃尾部测度构造「投资者恐惧指数」,发现对稀有事件的补偿解释了股票和方差风险溢价里的一大部分 [③]。
   → 这支持「峭度类测度原理上可能对应真实的风险溢价,不是无中生有」这件事有理论依据,但这篇测的是**市场指数**层面的跳跃尾部,
   用的是**期权隐含**信息,不是个股已实现峭度,方法和标的都不同,只能当一个方向性的理论背书,不能当成「文献已经证明 day_kurt(abs_(Ret)) 在定价」。
4. **零收益分钟/天数占比在文献里的标准定位是「流动性/交易成本的代理」,不是「没有跳跃」的信号,构造方式最简单——不需要任何高阶矩。**
   Lesmond, Ogden & Trzcinka 的 ZERO 测度就是某窗口内零收益观测数占总观测数的比例,逻辑是:当信息价值不足以覆盖交易成本时,
   当天(或当分钟)就不会发生价格变动 [④]。Bekaert, Harvey & Lundblad 把这个测度用在 19/20 个新兴市场上,发现它能显著预测未来收益,
   而换手率做不到;方向是**正的流动性溢价**——零收益比例越高(越不流动)的股票,要求的预期收益越高 [⑤]。
   → 这给 `day_zero_ratio(Ret)` 两点具体指导:(a) 如果 PI 想要一个「干净」的零收益比例变量,应该直接用最简形式(窗口内零收益观测数占比)
   作为对照基准,而不是只让它以「污染源」的身份出现在别的算子的残差里;(b) 文献给的先验方向是**正**(不流动 → 更高预期收益),
   如果我们实测方向相反,要么是 A 股/分钟频率下机制不同,要么是这个变量读到的其实是别的东西,这个方向检验本身就是一次免费的证伪机会。
5. **价位离散化(最小价位 / tick size)扭曲收益分布的证据是存在的,而且这个扭曲在换算成收益率之后不会消失——但文献证明的是尾部形状和相关系数,不是专门针对峭度这个统计量。**
   Münnix, Schäfer & Guhr 证明,在小的收益间隔上,价格的离散网格会系统性扭曲收益分布的尾部形状,并且导致相关系数随采样间隔缩短而衰减(Epps 效应),
   这个扭曲在从价格变动换算成收益率之后依然存在,不会因为换算就消失 [⑥]。→ 这是题目问的「价位离散化怎么系统性扭曲高阶矩」在文献里能找到的
   最接近的证据来源——方向上支持解剖员的担忧有物理机制依据(价格网格效应不会因为单位换算就自动消失,对低价股影响应该更强,
   因为有效 tick/价格的比值更大),但它论证的对象是「收益分布尾部」和「相关系数」,不是专门针对「峭度」这一个具体的四阶矩统计量,
   这个差距要在计划里说清楚,不能写成「文献已经证明峭度被离散化污染」。

**没找到、如实注明搜不到(与 r2 题 2 ④ 同一类空白,这里是峭度版)**:专门导出「1 分钟收益峭度」作为「零收益分钟占比」的解析偏差公式或
系统性蒙特卡洛论证的文献;专门测「A 股分钟频率下价位离散化对高阶矩的扭曲程度」的论文。Amaya et al.(靠「5 分钟 + 排除低价股」的操作性回避)
和 Münnix et al.(tick size 扭曲收益尾部的一般性证据)加在一起只能构成**间接**支持,不能当成「文献已证明 day_kurt(abs_(Ret)) 是
day_zero_ratio(Ret) 的单调函数」这个具体猜想的证据,这个猜想目前只能靠我们自己在 train 上实测相关度去验证。

### 3.2 文献出处

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|---|
| ① | Do Realized Skewness and Kurtosis Predict the Cross-Section of Equity Returns?(与 r2 lit.md 题 2 ① 同一篇,此处只取峭度结论) | Diego Amaya, Peter Christoffersen, Kris Jacobs, Aurelio Vasquez | 2011-07(CREATES Research Paper 2011-44;JFE 版 2015) | CREATES 工作论文 / Journal of Financial Economics | https://repec.econ.au.dk/repec/creates/rp/11/rp11_44.pdf | true |
| ② | Econometrics of Testing for Jumps in Financial Economics Using Bipower Variation | Ole E. Barndorff-Nielsen, Neil Shephard | 2003(Nuffield College 工作论文 2003-W21);2006(正式发表,Journal of Financial Econometrics, vol. 4 no. 1, pp. 1–30) | Nuffield College 工作论文 / Journal of Financial Econometrics | https://www.nuffield.ox.ac.uk/economics/papers/2003/w21/split.pdf | true |
| ③ | Tails, Fears, and Risk Premia | Tim Bollerslev, Viktor Todorov | 2011(Journal of Finance,具体卷期未逐字核实) | Journal of Finance | https://projects.nber.org/confer/2010/APf10/Bollerslev_Todorov.pdf | true |
| ④ | A New Estimate of Transaction Costs | Dennis A. Lesmond, Joseph P. Ogden, Charles A. Trzcinka | 1999(Review of Financial Studies, vol. 12 no. 5, pp. 1113–1141) | Review of Financial Studies | https://www.bauer.uh.edu/rsusmel/phd/lot_1999RFS.pdf | true |
| ⑤ | Liquidity and Expected Returns: Lessons from Emerging Markets | Geert Bekaert, Campbell R. Harvey, Christian Lundblad | 2005-06(NBER WP11413);2007-11(正式发表,Review of Financial Studies, vol. 20 no. 6, pp. 1783–1831,DOI 10.1093/rfs/hhm030) | NBER 工作论文 / Review of Financial Studies | https://www.nber.org/papers/w11413 | true |
| ⑥ | Impact of the Tick-Size on Financial Returns and Correlations | Michael C. Münnix, Rudi Schäfer, Thomas Guhr | 2010-01(arXiv 首版,arXiv 编号 1001.5124 对应 2010 年 1 月;v4 修订 2010-07-12);正式发表 Physica A, vol. 389 no. 21, pp. 4828–4843(2010) | arXiv / Physica A | https://arxiv.org/abs/1001.5124 | true |

说明:③ 没能核实具体卷期页码,只核实了机制(期权隐含跳跃尾部测度、投资者恐惧指数、补偿解释风险溢价的一大部分),按规矩仍标 `true`
(确实在搜索结果里看到了这些具体说法),但 PI 用卷期信息时应自己核对。⑥ 的 arXiv 首版日期是从 arXiv 编号本身推断(1001.5124 → 2010-01),
这是 arXiv 编号的标准约定,不是我瞎猜;正式发表的 Physica A 版本号也已核实。

---

## 题 4(对准 R-2 与最终库的标注):非单调的规模暴露,与「两个不同量纲的量相减」

### 4.1 能翻译成算子语言的处理方式

1. **非单调规模效应的一个具体 A 股机制:不是「中间市值段跑赢」,而是小盘段的「溢价」很大一部分是壳价值,不是规模本身。**
   Lee, Qu & Shen 用 2007–2015 年的反向收购交易数据,发现非上市公司为买一个上市壳平均付出 30–40 亿元人民币,超过中位数上市公司市值的三分之二;
   构造出「预期壳概率」(ESP)因子后,把它加入常见的五因子模型,**常见模型里那个异常大的规模溢价本身就消失了** [①]。→ 这给 R-2
   (head +0.834 的「市值带」判断)一个具体、可执行的检验方向:不是直接假设「非单调 = 市值带」,而是构造一个 A 股壳价值的近似代理
   (比如 `LogFloatCap` 处于某个低区间、且 `ListAge` 久、且 `LogFloatShares` 低——我们没有财务叶子,只能退一步用这几个日频叶子的组合近似),
   再检验 head +0.834 的信号是否主要集中在这个代理变量高的子样本里,这比「直接把 `pow_2_5(LogFloatCap)` 当非线性市值暴露」更接近文献里
   「先找机制再检验」的标准路径。
2. **非单调规模效应的另一个机制:指数纳入边界本身造成的机械性价格效应,与基本面无关,出现在市值分布的某个特定位置(不是「中间」,是指数成分股边界)。**
   Chang, Hong & Liskovich 用罗素 1000/2000 指数的规模排名断点做准自然实验,发现刚好跨过断点(从罗素 1000 掉入罗素 2000,或反之)的股票,
   价格会相对「险些没跨过」的邻近股票产生显著的非连续变化,机制是指数基金的被动买卖压力,不是基本面信息 [②]。→ 如果 head +0.834 里
   `cs_last_low40`/`pow_2_5(LogFloatCap)` 这类写法恰好卡在某个 A 股指数(沪深 300 / 中证 500 等)的纳入边界附近,这篇文献提示该怀疑是不是
   「指数效应」而不是「风格因子」,检验方法是看信号是否集中在「刚好在指数成分股边界两侧」的小样本里,这是和「壳价值」平行的第二个具体机制候选,
   两者都比「笼统地说是市值带」更可检验。
3. **检验「一个因子的收益其实来自某个规模带」,标准做法是先按规模分组、组内再检验目标因子,而不是看目标因子本身的边际分布形状。**
   Daniel & Titman 的「特征平衡组合」方法:先按因子暴露(协方差结构)分组控制住,再在组内比较特征的高低,用来论证是**特征**本身
   (而不是协变结构)驱动收益的横截面差异 [③]。→ 这正是关键词「characteristic-balanced portfolios (Daniel-Titman)」指向的那篇论文和方法本身,
   与 r1 题 1 提到的「先分市值组、组内再排序」(Goodman-Peavy / Zaremba 等)是同一个工具家族,也与 r1 题 3 的条件排序方法学背景(Cattaneo et al.,
   不重复引用)互相印证:给「怎么检验一个因子的收益其实来自某个规模带」这个方法学问题一个标准答案——按市值先分组、组内再检验,
   而不是像我们现在那样对市值做单一线性/立方残差化之后直接看目标因子。
4. **「非参数/样条控制规模」有具体可执行的例子,而且这个例子本身给出一个重要提醒:规模—收益关系的形状年度间变化很大,不是稳定结构。**
   Horowitz, Loughran & Savin 用分段线性样条(而不是单一线性或立方项)拟合市值十分位对收益的暴露关系,发现拟合出的形状**逐年剧烈变化** [④]。
   → 这给题目问的「样条/非参数控制」一个具体、可翻译的例子:对市值秩做分段线性而不是单一多项式;但更重要的是它的发现本身——
   即使我们在 A 股上用类似方法测出某种「非单调」的市值暴露形状,这个形状很可能在不同年份/不同样本窗口下变化很大,不构成稳定结构,
   PI 如果要往这个方向走,应该把「这个形状样本外还在不在」当成单独的检验项,而不是只看 train 上一次拟合的结果就下结论。
5. **(方法学背景,非金融文献)「谁的散布大谁说了算」这个问题,金融文献里没有专门讨论,但公共政策的复合指标构造方法学文献直接讨论过同一个统计问题。**
   Kaiser, Chen & Gluckman 在评论一个全球指数构造方法时指出:把量纲不同的子指标直接合成(包括相加或相减)而不先标准化,
   数值范围/离散度更大的那个指标会系统性主导结果,这是复合指标方法学里反复被讨论的经典陷阱,标准解法是先做 z-score 或取秩再合成 [⑤]。
   → 把这个一般性统计原则翻译回我们的算子语言:`sub(cross_stddev(day_skew(Ret), 60), LogFloatCap)` 这类「两个不同量纲的量直接相减」的写法,
   本身就处在这个已知陷阱里——不需要专门的金融文献来证明这件事有问题,统计方法学的一般结论已经足够;但这也说明:金融文献里**没有**
   专门为「我们这个具体相减」背书,不能反过来写成「文献支持这样处理市值」,只能写成「文献确认了这是一个已知的一般性陷阱」。

**没找到、如实注明搜不到**:(a) 专门针对 A 股用双重排序/特征平衡组合**直接**验证「规模效应非单调」这件事的论文——Lee-Qu-Shen 测的是
壳价值因子,Chang-Hong-Liskovich 测的是美股罗素指数边界,都是**相邻**证据,不是 A 股「非单调规模」本身的直接证据;(b) 专门的金融方法学文献
点名讨论「两个不同量纲特征直接相减」这个具体操作(用的是政策学复合指标文献做类比,不是金融文献)。这两条如实记录为用类比/相邻证据拼出来的。

### 4.2 文献出处

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|---|
| ① | Reverse Mergers, Shell Value, and Regulation Risk in Chinese Equity Markets(后修订发表为 "Gate Fees: The Pervasive Effect of IPO Restrictions on Chinese Equity Markets", Review of Finance 2023——发表版晚于本题截止日期,本条只引用 2017 工作论文版本) | Charles M. C. Lee, Yuanyu Qu, Tao Shen | 2017-09(Stanford GSB 工作论文 No. 3604,日期 2017-09-09) | Stanford GSB 工作论文 | https://www.gsb.stanford.edu/faculty-research/working-papers/reverse-mergers-shell-value-regulation-risk-chinese-equity-markets | true |
| ② | Regression Discontinuity and the Price Effects of Stock Market Indexing | Yen-cheng Chang, Harrison Hong, Inessa Liskovich | 2013-08(NBER WP19290);2015(正式发表,Review of Financial Studies, vol. 28 no. 1, pp. 212–246,DOI 10.1093/rfs/hhu041) | NBER 工作论文 / Review of Financial Studies | https://www.nber.org/papers/w19290 | true |
| ③ | Evidence on the Characteristics of Cross-Sectional Variation in Common Stock Returns | Kent Daniel, Sheridan Titman | 1996-06(NBER WP5604);1997-03(正式发表,Journal of Finance, vol. 52 no. 1, pp. 1–33) | NBER 工作论文 / Journal of Finance | https://www.nber.org/system/files/working_papers/w5604/w5604.pdf | true |
| ④ | A Spline Analysis of the Small Firm Effect: Does Size Really Matter? | Joel L. Horowitz, Tim Loughran, N. E. Savin | 1996-07(University of Iowa 工作论文 96-09,1996-07-23 版) | University of Iowa 工作论文 | https://econwpa.ub.uni-muenchen.de/econ-wp/em/papers/9608/9608001.pdf | true |
| ⑤ | Should policy makers trust composite indices? A commentary on the pitfalls of inappropriate indices for policy formation(非金融文献,公共政策方法学,仅作「不同量纲合成」这一统计问题的类比证据) | Matthias Kaiser, Andrew Tzer-Yeu Chen, Peter Gluckman | 2020-08(arXiv 工作论文,编号 2008.13637 对应 2020 年 8 月);2021-03(正式发表,Health Research Policy and Systems) | arXiv / Health Research Policy and Systems | https://arxiv.org/pdf/2008.13637 | true |

说明:① 的工作论文日期(2017-09-09)和编号(No. 3604)是我直接用 WebFetch 打开 Stanford GSB 工作论文页面看到的,不是转述,置信度高;
发表版本"Gate Fees"(2023, Review of Finance)虽然晚于本题截止日期不能引用其发表版数字,但按规矩工作论文以首版日期为准,2017 年版本可用,
PI 使用时请只引用 2017 工作论文摘要里给出的量级(2007–2015 期间 3–4 十亿人民币/壳),不要混入发表版(2007–2020 期间、超 5 亿美元)的数字。
⑤ 是本轮唯一一条不是金融文献的条目,收录理由是金融文献检索多轮后没有找到专门讨论「不同量纲特征直接相减」这个具体问题的文献,
这个统计学一般性陷阱本身是真实存在且可核实的,但 PI 用它的时候要清楚这是跨领域类比,不是金融界的共识或惯例。

---

## 给 PI 的一句话总结

四题里最值得直接变成外围/检验写法的两条:(1)题 1 的 Shen-Shi(⑤)把「成交质心靠后」和「被动资金占比」直接挂钩,且发现这个关系强度本身随时间变化——
这应该让 PI 把「被动占比」列为核心①/核心②共享的第三个候选机制,并在相关度表里直接检查两个核心的互相 |ρ|;(2)题 4 的 Lee-Qu-Shen(①)给了
R-2「市值带」判断一个具体、可执行的替代检验(壳价值代理子样本),比继续猜「是不是市值带」更接近文献标准。题 2 的 Han et al.(③)提醒 PI 核对
train 窗口是否跨过 2018-08-20 这个 A 股制度改革日期,这是一个容易被忽略的数据细节,不只是文献背景。题 3 全程没有找到能直接验证
「day_kurt(abs_(Ret)) 就是 day_zero_ratio(Ret) 的单调函数」这个猜想的文献,Barndorff-Nielsen-Shephard 的 RV−BV 分解(②)是目前能提供的
最直接的**检验工具**(不是答案),建议 PI 如果要用核心③,先用这个工具在 train 上跑一次粗检验,而不是只靠相关度表的静态数字下判断。
四题各自的「搜不到」之处已在各节如实注明,其中题 3、题 4 的空白比题 1、题 2 更大,说明这两个核心/R 目标目前更依赖 train/valid 上的实测,
文献能提供的只是检验思路和方向性先验,不是现成结论。
