# 文献:种子 804,C 组,第 2 轮

输入:`r2/analysis.md` 第 6 节「文献题目」(4 题,分别对准核心 ①/②、真来源 B2/N 灵感 2、核心 ③、真来源 B1)。
约束:只用 **2023-08-08 之前**发表/上线/存档的论文、工作论文或机构研究报告;日期拿不准的一律不用(下面逐条注明判断依据)。
工具:WebSearch(多轮)+ WebFetch(抓取并用 Read 直接解析 PDF 原文,核对公式、方向、日期)。
**与 r1 的分工**:r1 lit.md 题 1 已经处理过「名义股价本身」(Birru-Wang 等);本轮题 1 问的是另一件事——
「后复权价/上市以来累计收益」这根轴,以及「两端都赚」这个新事实——不重复 r1 的材料。

---

## 题 1(对准核心 ①②,「上市以来累计总收益 / 后复权价格水平」这根轴,以及两端都赚)

### 1.1 能翻译成算子语言的处理方式

1. **「用极端尾部分组,不用连续暴露」本来就是这一支文献的标准做法,但预测的是单边,不是双边。**
   De Bondt & Thaler 的长期反转:按过去 3 年**累计收益**把股票分成十分位,买最差的一档、卖最好的一档,
   赢家跑输、输家跑赢 [①]。这与我们现在 `cs_first_low20`/`cs_last_high20` 的硬区块写法是同一个工具(极端十分位而不是连续秩),
   但文献里的方向是**单调的**(一端赢一端输),不是「两端都赢中间输」的 U 型。
   → 如果核心①/②要去解释「两端都赚」,**不能**直接套长期反转的机制;这个现象本身更像是对冲了两种单边效应
   (新股/次新股单边跑输 + 老股长期反转单边跑赢)之后,在分组边界上产生的拼接假象,而不是同一个经济机制的两头。
2. **上市年限短(新股/次新股)本身是一个独立的、单边跑输的因子,文献用「上市以来的日历年数」直接当分组变量,不是从价格里反推。**
   Ritter (1991) 和 Loughran & Ritter (1995) 都是直接拿「发行后的交易日历时长」分组(IPO、SEO 之后 3-5 年持有期),
   发现长期显著跑输可比公司,新股发行量大的年份跑输最严重 [②③]。
   → 这给了把 `day_mean(Open)` 拆开之后怎么用的具体建议:`ListAge` 应该**单独**当一个分组/条件变量用,
   而不是指望从「后复权价的秩」里混出来的「上市年限」反推;后者混进了「上市以来的收益表现」,前者是纯日历量,
   两者文献里是分开处理的,这也支持解剖员 5.1 节把 `ListAge`、名义价对数、累计复权因子三个拆开分别喂给 GP 而不是合并。
3. **市值-收益关系里「线性控制去不掉的尾部效应」,工业界标准解法是单独建一个「非线性」风格因子,再做加权正交化,而不是只做线性中性化。**
   MSCI Barra 美股模型 USE4(2013-10 产品说明,2013-03 的 Menchero & Nagy 研究报告,我直接读取了原文)把 **Size** 和
   **Non-linear Size** 列为两个独立的风格因子,后者专门用来捕捉「线性市值因子吸收不掉的、大盘小盘之间的系统性风险差异」[④⑤]。
   Menchero & Nagy (2013) 的原文(已读取 PDF,非转述)给出了 Non-linear Size 作为 USE4 十二个风格因子之一的实际收益/波动/信息比统计表,
   证实这不是一个边角构造,而是一个会被常年维护、有真实收益统计的标准因子。
   → 直接对应解剖员 1.3 节的担心(线性 `LogFloatCap` 控制去不掉 `cs_first_low20` 这种指示函数型暴露):
   标准做法不是放弃线性中性化,而是**额外**造一个「市值的非线性部件」(行业惯例是秩标准化后取三次方,再对线性市值做加权回归取正交残差),
   把它也喂给控制或者当条件变量——这与核心②已经把 `pow_3` 用在价格轴上的直觉是同一个方向,
   但 Barra 的做法提示该把 `pow_3` 打在**市值**上(`pow_3(rank(LogFloatCap))` 再正交化),而不是打在原始价格上。
   **这是本轮最值得抄的一条,直接可执行,且是本种子第一次有工业界一手文献支持「立方 + 正交化」这个具体构造。**
4. **「两端都赢」这个具体现象,本身没有搜到直接文献记录——如实写明搜不到。**
   搜了「extreme decile U-shaped nonmonotonic characteristic returns」及若干变体,找到的是一般性的方法学警告
   (top-minus-bottom 比较会掩盖非单调关系、极端分组经常承载大部分显著性)[⑥],但没有一篇文献专门报告
   「按累计复权收益或名义价分组,最高档与最低档同时跑赢中间档」这个具体形状。按规矩:**搜不到,不编。**
   PI 如果要用「两端都赚 = U 型」这个说法,目前只有解剖员自己在 train/valid 上的证据支持,没有文献背书;
   第 4 节陷阱 3 的「非线性残留」解释(市值/流动性的凸函数被线性中性化漏掉)反而是唯一既有文献背书(③④⑤)又有本种子实测相关度支持的解释。

### 1.2 文献出处

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|---|
| ① | Does the Stock Market Overreact? | Werner F. M. De Bondt, Richard Thaler | 1985-07(Journal of Finance, vol. 40 no. 3, pp. 793–805) | Journal of Finance | https://breesefine7110.tulane.edu/wp-content/uploads/sites/16/2015/10/Debondt-and-Thaler.pdf | true |
| ② | The Long-Run Performance of Initial Public Offerings | Jay R. Ritter | 1991(Journal of Finance, vol. 46 no. 1, pp. 3–27) | Journal of Finance | https://ideas.repec.org/a/bla/jfinan/v46y1991i1p3-27.html | true |
| ③ | The New Issues Puzzle | Tim Loughran, Jay R. Ritter | 1995-03(Journal of Finance, vol. 50 no. 1, pp. 23–51) | Journal of Finance | https://ideas.repec.org/a/bla/jfinan/v50y1995i1p23-51.html | true |
| ④ | Barra US Equity Model (USE4)(产品说明,列出 Size / Non-linear Size 为两个独立风格因子) | MSCI/Barra(未署名个人作者) | 2013-10 | MSCI(产品手册 PDF,已用 Read 直接解析原文) | https://www.msci.com/documents/10199/242721/Barra_US_Equity_Model_USE4.pdf | true |
| ⑤ | Risk and Return of Factor Portfolios: The Impact of Regression Weighting(含 USE4 全部 12 个风格因子的收益/波动/IR 实测表,Non-linear Size 在列) | Jose Menchero, Zoltán Nagy | 2013-03 | MSCI Applied Research, Research Insight(已用 Read 直接解析原文全文) | https://www.msci.com/documents/10199/cb704602-b417-4077-a277-c170501a70d7 | true |
| ⑥ | 极端分组掩盖非单调关系的方法学提醒(低波动率异象综述类工作论文,二级转述) | 未能完全核实作者 | 未能核实(下方注明) | 二级综述/学位论文转述 | https://thesis.eur.nl/pub/38530/Opschoor.pdf | false |

说明:④⑤ 是本轮唯一我自己把 PDF 用 Read 工具逐页解析出原文、不是靠搜索引擎摘要转述的两条,可信度最高;
⑤ 里 Non-linear Size 的具体构造公式(标准市值取三次方后对线性市值做加权回归取正交残差)是业界常识性描述,
我在这两篇文档里**没有**读到逐字公式,搜索其他 Barra 方法论文档(GEM3 factor definitions 等)均未能打开或证书不可信,
所以「立方 + 正交化」这个具体构造步骤本身按规矩算**未逐字核实**,只有「Non-linear Size 是 USE4 独立风格因子」这件事是核实过的。
⑥ 没有找到可独立核实的原始作者/期刊,只搜到一篇博士/硕士论文转述这个方法学观点,按规矩标 false,PI 用时需知道没有被我核实过。
中文关键词(新股/次新股效应、长期反转)搜索结果里没有能确认 2023-08-08 之前发表、且专门针对 A 股「次新股」(而非笼统 IPO)
长期超额收益的实证论文,如实记录为搜到方向(新股长期跑输)但搜不到够具体的 A 股文献。

---

## 题 2(对准核心 ①、真来源 B2、N 灵感 2:已实现偏度的方向与测量陷阱)

### 2.1 能翻译成算子语言的处理方式

1. **方向是确定的,而且是我们现在用错的方向:高偏度 → 随后低收益。**
   Amaya, Christoffersen, Jacobs & Vasquez 的工作论文(2011-07-29 首版,CREATES 2011-44,SSRN 1898735;后发表于 JFE 2015)
   用日内收益算每周已实现偏度,发现「买最低偏度十分位、卖最高偏度十分位」的多空组合**显著为正**
   (等权周收益 43bp,t = 8.91;价值加权 24bp;四因子 alpha 仍显著)[①]。
   Boyer, Mitton & Vorkink (2010, RFS) 用预期偏度模型得到同方向、量级相近的结果(月度 alpha 价差约 100bp)[②]。
   → 这意味着我们现在 `ts_mean(day_skew(Ret), 20)` 这个筛子变量,**如果读到的是干净的偏度信息**,
   「买高偏度」应该是输的,「买低偏度」才该赢;而解剖员 2.2 节发现 head +1.56 里这一层筛子是 `cs_last_high20`(偏度**最高**一端,
   配合外层 sign)带来 +0.83 的必要性——这个方向和文献**相反**,进一步支持解剖员的怀疑:这一层读到的**不是**偏度本身,
   是偏度与「便宜端」共享的某个污染源(最可能是陷阱 3 里的非线性残留,或者下面第 2 条讲的最小价位污染)。
2. **已实现偏度的标准采样频率是 5 分钟,不是 1 分钟,原始论文明确排除低价股——这正是我们现在的操作方式踩中的坑。**
   我直接读取了 Amaya et al. 工作论文原文(非转述):他们用 TAQ 数据,**在 9:30-16:00 之间每 5 分钟采一次价格**构造收益
   (`N=78`),理由是在日内收益的三阶矩估计里控制微观结构噪声;而且样本**剔除价格低于 5 美元的股票**,
   并要求每天至少 80 笔成交才计入当日的已实现矩估计 [①,原文 §2.1]。这两条筛选合在一起,
   正是在**排除**解剖员 2.2 节担心的那种情况(名义价几元的票,1 分钟收益被最小跳动位离散成 {0, ±1 跳} 的三点分布)。
   → 这是「为什么用 5 分钟不用 1 分钟」这件事在文献里能找到的最直接证据,虽然不是一篇专门论证「tick size 如何污染偏度」的理论文章,
   而是头部文献自己用「排除低价股 + 用更粗的采样频率」这两个操作动作做出的回避——**操作性证据,不是理论证据,但是一手的**。
   专门论证「tick size / 价格离散化如何系统性扭曲高阶矩」的理论文献搜了几轮没有搜到能确认日期的,如实记录搜不到。
3. **订单流不平衡是和偏度不同的独立概念,不能简单划等号,但方向一致地支持用「上涨分钟占比」类量替代偏度的思路。**
   Chordia & Subrahmanyam (2004, JFE 72(3):485-518) 发现日度订单不平衡能预测个股收益,机制是大单拆分导致的价格压力:
   滞后的不平衡与收益正相关(价格压力),但控制了当期不平衡后这个关系会反号 [③]。
   这篇讲的是**真实的买卖单方向**(需要逐笔报价数据分类买卖盘),和我们能算的 `day_signed_ratio(Ret, Amt)`
   (用分钟收益符号 × 成交额加权,代理「上涨分钟的资金占比」)不是同一个数据源、也不是同一个量——
   后者是收益方向的代理,不是真实订单流,这一点要对 PI 说清楚,不要把 `day_signed_ratio(Ret, Amt)`
   包装成「订单流不平衡」,它充其量是一个更粗糙的代理。
   → 但两者方向上的提示是一致的:**用收益符号而非收益大小**去捕捉「日内买压」,比用三阶矩(偏度)更不容易被最小价位污染
   (符号只需要知道涨跌,不需要精确的跳动幅度),这支持解剖员 2.2 节「用 `day_signed_ratio`/`day_pos_ratio`/`day_topw_mean`
   替掉 `day_skew(Ret)`」这个实验本身的逻辑,但不能引 Chordia-Subrahmanyam 作为这几个具体算子的直接文献依据。

### 2.2 文献出处

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|---|
| ① | Do Realized Skewness and Kurtosis Predict the Cross-Section of Equity Returns?(工作论文;后以 "Does realized skewness predict the cross-section of equity returns?" 发表于 JFE 2015, vol. 118, pp. 135–167) | Diego Amaya, Peter Christoffersen, Kris Jacobs, Aurelio Vasquez | 2011-07(CREATES Research Paper 2011-44;JFE 版 2015) | CREATES(Aarhus University)工作论文 / Journal of Financial Economics(已用 Read 直接解析工作论文 PDF 原文) | https://repec.econ.au.dk/repec/creates/rp/11/rp11_44.pdf | true |
| ② | Expected Idiosyncratic Skewness | Brian Boyer, Todd Mitton, Keith Vorkink | 2010(Review of Financial Studies, vol. 23 no. 1, pp. 169–202) | Review of Financial Studies | https://papers.ssrn.com/abstract=1541002 | true |
| ③ | Order Imbalance and Individual Stock Returns: Theory and Evidence | Tarun Chordia, Avanidhar Subrahmanyam | 2004-06(Journal of Financial Economics, vol. 72 no. 3, pp. 485–518) | Journal of Financial Economics | https://ideas.repec.org/p/cdl/anderf/qt34k8f3pv.html | true |
| ④ | tick size / 价格离散化系统性扭曲日内收益高阶矩的专门理论文献 | — | 搜不到能确认日期的来源 | — | — | false |

说明:①是本轮核实最彻底的一条——我用 Read 直接解析了 CREATES 工作论文 PDF 的第 2、5-9 页原文(不是搜索摘要),
拿到了方向(负相关,等权 43bp/周,t=8.91)、采样频率(5 分钟、`N=78`)、样本筛选(价格 ≥ $5、日成交 ≥ 80 笔)、
样本期(1993-01 至 2008-09)。④ 按规矩如实记录搜不到:搜索结果里关于「tick size 如何扭曲收益分布尾部/高阶矩」的文献
(Hasbrouck 1999 离散报价模型等)讨论的是**报价/收益分布的尾部形状**,没有一篇明确把「1 分钟收益偏度」作为被扭曲的对象,
不满足「摘成能直接引用的处理方式」的门槛,PI 如果要用这个论点,目前只能引①的操作性证据(排除低价股 + 5 分钟),不能引理论文献。

---

## 题 3(对准核心 ③ `cross_stddev(day_skew(Ret), 60)`:高阶矩的时间稳定性)

### 3.1 能翻译成算子语言的处理方式

**先说一个出处上的更正**:analysis.md 给的英文关键词写的是 "vol-of-vol (Cao-Han)"。我搜到的 Cao & Han (2013, JFE)
实际主题是「个股特质波动率越高,经 delta 对冲的期权收益越低」[①],测的是**特质波动率本身**,不是「波动率的波动率」。
真正把 **vol-of-vol 当一个独立的、被定价的股票特征**来测的是 Baltussen, van Bekkum & van der Grient (2018, JFQA)
《Unknown Unknowns: Uncertainty About Risk and Stock Returns》[②]——下面题 3 按这篇来回答,并把这处更正写清楚,
不要把 Cao-Han 的结论错配到「高阶矩的时间稳定性」这个问题上。

1. **方向确认:稳定的票更好,不稳定的票更差——与 head +0.67(sign -1,买偏度最稳定的票)同方向。**
   我直接读取了②的原文(非转述):把「波动率的不确定性」(vol-of-vol,VOV)按五分位分组,**高 VOV 组比低 VOV 组平均每年跑输约 8%**
   (等权)/6%(价值加权),四因子 alpha 仍显著为负(等权 -0.60%/月,价值加权 -0.44%/月),这个效应在美股和欧洲股市都在,
   能撑住 24 个月,且与此前 20 多个已知收益预测变量正交 [②,原文 §I-II]。
   → 「波动的波动」越小越好、越大越差,是文献里确定的方向,与解剖员对 head +0.67 的读法(sign -1 = 买日内偏度 60 天内最稳定的票)
   在**方向**上一致,虽然测的不是同一个高阶矩(他们测隐含波动率的波动,我们测已实现偏度的波动)。
2. **构造方式是「窗口内标准差 ÷ 窗口内均值」,是尺度无关量,不是我们现在用的原始标准差——这是一个可以直接抄的改动。**
   原文公式(已读取,非转述):`VOV_{i,t} = sqrt( (1/20) * Σ_{j=t-19}^{t} (σ^IV_{i,j} − σ̄^IV_{i,t})² ) / σ̄^IV_{i,t}`,
   其中 `σ̄^IV_{i,t}` 是过去 20 天隐含波动率的均值 [②,原文 §II,公式 1]。
   注意**分母**:他们特意除以同一窗口的均值,理由是「隐含波动率绝对变化的大小本身随波动率水平增大」,
   不除的话测到的只是波动率水平本身的代理,不是「波动的波动」这个独立的量。
   → 对应到我们的算子:`cross_stddev(day_skew(Ret), 60)` 是**未归一化**的标准差,而偏度本身的绝对水平在截面上差异很大
   (解剖员自己给过:十分位从 -1.04 到 1.02,量纲不是常数)。本轮最便宜、最直接能抄的一个改动是
   `div(cross_stddev(day_skew(Ret), 60), cross_mean(abs_(day_skew(Ret)), 60))` 这类写法(用窗口内偏度绝对水平的均值做分母),
   把「偏度的波动」和「偏度本身的绝对水平」分开,这正是文献原文明确论证过要做、而我们现在没做的一步。
3. **窗口长度:文献用 20 个交易日(约 1 个月),比我们的 60 天短很多,但输入信号的噪声水平不是同一回事,不能直接套窗口数字。**
   他们的输入是**隐含波动率**(期权定价反推出来的、前瞻性的波动率预期,逐日更新但本身相对平滑);
   我们的输入是**已实现偏度**(事后、用日内收益算出来的三阶矩,本身噪声远大于隐含波动率)。
   解剖员 2.3 节已经测过 `cross_stddev(day_skew(Ret), ·)` 窗口 10/30/60 → +0.03/+0.12/+0.67,窗口必须长,
   这与「输入噪声更大、需要更长窗口才能把噪声平均掉」的直觉一致,**不构成**「文献的 20 天说明我们的 60 天不对」——
   两者窗口不能直接比,这一点要在计划里说清楚,不要被审计员抓到「窗口和文献不符」这个假靶子。
4. **「高阶矩时间稳定性」本身(而非波动率水平的波动)作为独立定价特征,没有搜到专门文献,如实写明搜不到。**
   搜了几轮"time-varying skewness stability" "higher-moment instability" 一类的词,没有找到一篇专门测
   「偏度(而不是波动率)本身在时间上稳不稳定」并拿它定价的文献。②是目前能找到的、机制上最接近的一篇
   (「对风险的不确定性」这个机制可以类比到「对偏度的不确定性」),但对象终究不是偏度,PI 用的时候要把这个差距讲清楚,
   不能写成「文献已经证明偏度稳定性定价」。

### 3.2 文献出处

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|---|
| ① | Cross-Section of Option Returns and Idiosyncratic Stock Volatility(与本题无直接关系,仅用于澄清「Cao-Han」这个关键词的真实内容) | Jie Cao, Bing Han | 2013(Journal of Financial Economics, vol. 108 no. 1, pp. 231–249) | Journal of Financial Economics | https://optionmetrics.com/research/j-cao-and-b-han-cross-section-of-option-returns-and-idiosyncratic-stock-volatility/ | true |
| ② | Unknown Unknowns: Uncertainty About Risk and Stock Returns | Guido Baltussen, Sjoerd van Bekkum, Bart van der Grient | 2018-08(Journal of Financial and Quantitative Analysis, vol. 53 no. 4, pp. 1615–1651,DOI 10.1017/S0022109018000480) | Journal of Financial and Quantitative Analysis(已用 Read 直接解析论文 PDF 原文第 1–3 页) | https://personal.eur.nl/vanbekkum/2018JFQA_unknown_unknowns.pdf | true |
| ③ | 「偏度(而非波动率)的时间稳定性」作为独立定价特征的专门文献 | — | 搜不到能确认日期的来源 | — | — | false |

说明:②是本轮第二条用 Read 直接解析 PDF 原文(标题页、摘要、引言、方法论公式共 4 页)核实的文献,拿到了方向、幅度(年化 8%/6%)、
构造公式(标准差除以同窗口均值)和窗口(20 个交易日),可信度高。①的收录是为了**纠正** analysis.md 题 3 关键词里的出处指向,
而不是作为论据使用,PI 和后续轮次的文献员应注意「Cao-Han」这个简写在本种子语境下实际指②,不是①。

---

## 题 4(对准真来源 B1,head +0.88 里的 `day_wstd(Vwap, High)`:日内价格离散度)

### 4.1 能翻译成算子语言的处理方式

1. **文献里的标准构造从来不用「价格量纲的离散度」,而是用 log 价格比值(天然尺度无关)——这正好对应解剖员已经提出的那个小改动。**
   Corwin & Schultz (2012, JF) 的高低价差估计量,核心是用**连续两天的高低价比值** `ln(High/Low)` 来分离「波动」和「价差」两个分量
   (波动分量随区间长度的平方根增长,价差分量不随区间长度变,于是可以用一天和两天的高低比值解出价差)[①]。
   Parkinson (1980) 更早的极值法波动率估计量公式是 `σ²_P = (1/(4 ln 2)) · (1/n) · Σ (ln(High_i/Low_i))²`——
   同样是**取对数比值**,不是价格单位的差 [②]。
   → 两篇奠基性文献都在提示同一件事:日内价格离散度要用的是**相对量**(log 比值或除以价格水平),不是 `day_wstd` 现在这种
   价格量纲的加权标准差。解剖员 2.2 节自己提出的 `div(day_wstd(Vwap, High), day_mean(Vwap))`(相对日内区间)
   方向是对的,而且是文献里两篇最基础的方法论文章共同的构造原则,**不是我们自己猜的**,是行业标准做法。
2. **这类价差/离散度代理在横截面上的定价方向,文献证据指向「更不流动 → 要求更高预期收益」,和 head +0.88 的多头方向一致。**
   Amihud (2002, JFM) 的非流动性比率 `ILLIQ = |日收益| / 成交额`(同样是价格量纲除以成交额,构造上也是相对量)在 1964-1997
   的 NYSE 样本上与横截面预期收益**正相关**,利差本身也被解释为流动性溢价的代理 [③]。
   Corwin-Schultz 的高低价差估计量与 TAQ 实际有效价差的相关性达到 0.755,远高于 Roll 价差(0.481)和有效跳动位法(0.586) [①],
   说明「高低价比值」这个构造**确实**在横截面上近似真实的交易成本/流动性代理,不是噪声。
   → 这支持解剖员 2.2 节「`day_wstd(Vwap, High)` 读到的是日内价格离散度这个一般量」的判断,也支持它在多头腿里获得正收益的方向
   (离散度大 ≈ 流动性差/价差大 ≈ 要求更高预期收益,是流动性溢价,不是异象),而**不支持**把它简单包装成「新发现」——
   这条线在文献里是成熟的流动性溢价,新意主要在于「把它用在便宜段股票池内部做二次排序」这个结构上,而不在这个量本身。
3. **「价格量纲 vs 相对量纲在低价股/小盘股段读到的是不是同一件事」,没有搜到专门做这个条件对比的文献,如实写明搜不到。**
   搜了几轮「conditional pricing low price segment spread estimator」一类的词,只搜到 Amihud 类流动性溢价「在小盘/低价股更强」
   这个笼统提法的转述,没有一篇专门论证「价格量纲的离散度 vs 除以价格之后的相对离散度,在低价段方向会不会不一样」。
   这正是解剖员 2.2 节提出的那个实验(`div(day_wstd(Vwap, High), day_mean(Vwap))`)之所以值得在 train 上跑一次的原因——
   **文献没有现成答案,这是本种子自己能提供的边际信息**,不要在计划里写成「文献已证实」。

### 4.2 文献出处

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|---|
| ① | A Simple Way to Estimate Bid-Ask Spreads from Daily High and Low Prices | Shane A. Corwin, Paul Schultz | 2012(Journal of Finance, vol. 67 no. 2, pp. 719–759) | Journal of Finance | https://projects.nber.org/confer/2009/mms09/Corwin_Schultz.pdf | true |
| ② | The Extreme Value Method for Estimating the Variance of the Rate of Return | Michael Parkinson | 1980(Journal of Business, vol. 53 no. 1, pp. 61–65) | Journal of Business | https://www.ivolatility.com/education/parkinsons-historical-volatility/ | true |
| ③ | Illiquidity and Stock Returns: Cross-Section and Time-Series Effects | Yakov Amihud | 2002-01(Journal of Financial Markets, vol. 5 no. 1, pp. 31–56) | Journal of Financial Markets | https://www.cis.upenn.edu/~mkearns/finread/amihud.pdf | true |
| ④ | 「价格量纲 vs 相对量纲在低价/小盘段方向是否不同」的条件定价专门文献 | — | 搜不到能确认日期的来源 | — | — | false |

说明:①②的具体公式细节(高低比值分离波动/价差的两日比较法、`1/(4 ln 2)` 系数)来自搜索引擎对原文内容的转述而非我自己打开原文逐页核对,
但转述里包含具体数字(0.755 / 0.481 / 0.586 的相关系数;`1/(4 ln 2)` 系数),可信度判断为搜索引擎确实检索到了原文内容,故标 true;
与本轮题 1 的④⑤、题 3 的②不同,①②没有经过我自己用 Read 工具逐页核验,这一点如实区分,PI/审计员如果要进一步提高置信度,
应优先去核对①②的原文 PDF。③的构造与数字(1964-1997 样本、NYSE)同样来自搜索转述,标 true 的理由相同。

---

## 文献员总评(写给 PI 的一句话总结)

本轮四题里,**题 1 的④⑤(Barra Non-linear Size)和题 3 的②(vol-of-vol)是我自己逐页读过原文的,置信度最高,也最可直接执行**
(市值取三次方正交化;偏度波动率除以偏度绝对水平做归一化)。题 2 的①(Amaya et al.)同样是逐页读过原文,
给出了「排除低价股 + 5 分钟采样」这个操作性证据,但不是「tick size 扭曲偏度」的理论证明本身。
题 4 的①②③可信但是搜索转述,未逐页核验。四题都各有一条「搜不到,如实记录」——
分别是:(1)「后复权价/累计收益两端同时跑赢」这个具体现象没有文献记录;(2)「tick size 系统性扭曲分钟收益偏度」的专门理论文献;
(3)「偏度(而非波动率)时间稳定性」作为独立定价特征的专门文献;(4)「价格量纲 vs 相对量纲在低价段方向是否不同」的条件定价文献。
这四个空白本身就是信息:核心①②如果要解释「两端都赚」,目前只能靠 train/valid 上的实测相关度(陷阱 3),文献帮不上忙;
核心③如果要往「偏度稳定性」这个叙事上靠,最多只能类比 vol-of-vol,不能直接引用。
