# 文献:种子 802,P 组,第 1 轮(文献员)

对准 `analysis.md` §5 的四个文献题目(Q1–Q4)。只用 **2023-08-08 前发表**的论文 / 工作论文 / 研究报告,
arXiv / SSRN / Fed working paper 以**首版日期**为准。每条"处理方式"后面标出处;出处格式:
标题、作者、年-月、来源、链接、`verified: true/false`。

**核查方式说明(诚实写在前面)**:本轮用 WebSearch 做了约 25 次检索,WebFetch 对两篇直接下载并本地
`pdftotext` 核对过原文(Admati-Pfleiderer 的引用信息、Givry 的 AMF slides);其余论文的"存在性 + 摘要结论"
来自搜索引擎对多个来源(IDEAS/RePEc、作者主页、机构仓库摘要页)的合成摘要,我没有逐篇打开 PDF 核对公式细节。
`verified: true` 指"这次确实在搜索结果或页面上看到了标题/作者/期刊/结论这些信息",不代表我验算过它的回归式。
凡是搜索工具自己说"这是我的背景知识,不是从这次结果里来的",我按**未核实**处理,标 `verified: false` 并在正文里说明。
遇到搜不到的,直接写"搜不到"。

---

## Q1 —— 日内成交量开盘端 vs 收盘端的不对称

**核心 A 的代数本质(见 analysis.md 1.1)是"头尾两块绝对股数之差",中间 211 分钟被精确消掉。**
文献里能查到的处理方式,没有一个是直接做"两端差"的,都是以下三种之一:

### 处理 1 —— 把"两端差"换成"分段量的分布/占比",而不是绝对差
经典的 U 型刻画本身是"按固定区间(通常是小时或半小时)分桶的成交量/成交笔数",模型预测的是全天的
分布形状(U 型或反 J 型),不是头尾两块的差值。这意味着**我们核心丢掉的"中间 211 分钟"在原始文献框架里
恰恰是用来定义"U 型"或"反 J 型"这两种竞争假说的部分** —— analysis.md 1.1 提到的"中间段没用上"
这件事,文献角度看是真的丢了信息,不只是数值上的化简。
可翻译的算子:把 `in_delta(Volume,30)` 的"差"换成对多个固定区段分别 `in_sum`/`in_mean` 后求跨区段的
离散度(如 `day_std` 跨多个 `in_sum(Volume, bucket)`),或者直接在多个区段上做"分布形状"刻画,
而不是只取头尾两点。
- 出处:Admati, A. & Pfleiderer, P., "A Theory of Intraday Patterns: Volume and Price Variability",
  *Review of Financial Studies*, 1988-01, 1(1):3–40. DOI 10.1093/rfs/1.1.3.
  https://ideas.repec.org/a/oup/rfinst/v2y1989i2p189-223.html (及 Stanford GSB 出版物页面)。
  `verified: true`(用 WebFetch/WebSearch 交叉确认了刊物、卷期、页码、DOI)。

### 处理 2 —— 用"占比"而不是"绝对量差";开盘/收盘集合竞价要单独拿出来算
法国 AMF 的研究 slides(用交易所自己的统计数据)把"收盘集合竞价成交量占全天成交量的比重"作为核心变量,
并专门对比了"最后 30 分钟连续竞价的份额变化"。我用 WebFetch 下载并本地 `pdftotext` 核对过原文:
它报告法国 CAC40 的收盘集合竞价份额自 2016 年起显著上升,美股(S&P 500)同期"最后 30 分钟"份额
也有适度上升,但法国市场在"最后 30 分钟"这个子区间没有观察到同样的上升 —— 也就是说**集合竞价份额的
上升和"最后 30 分钟连续竞价份额"的上升不是一回事,必须分开统计**,不能用一个笼统的"收盘端"变量。
可翻译的算子:`div(day_last(Volume), day_sum(Volume))`(收盘集合竞价占比,对应 analysis.md 的 R#7)
和"最后 30 分钟连续竞价量占比"(需要 `in_sum(Volume, 30)` 取最后一段再除以 `day_sum`)是文献里
实际分开检验的两个量,而不是本核心这种"头尾绝对差"。
- 出处:Givry, A. (Autorité des marchés financiers, 法国金融市场管理局), "About the Increasing Part
  of Closing Auction ('Fixing')", 2019-09(幻灯片注明 "September 2018" 的数据窗口,会议/发布约 2019 年),
  LSE Financial Markets Group 活动材料。
  https://www.fmg.ac.uk/sites/default/files/images/6.2019%2009%2005%20-%20About%20the%20increasing%20part%20of%20closing%20auctions-ok%20to%20publish.pdf
  `verified: true`(已用 WebFetch 下载原文并本地 pdftotext 逐页核对,标题、作者、机构、"最后 30 分钟"
  美欧对比的结论都直接读到了原文文字)。
  **纠偏说明**:我在更早一次 WebSearch 的合成摘要里看到过"23% 的收盘竞价收益隔夜反转"这个数字,
  当时以为也是这篇;核对原文后**这篇 10 页的 slides 里没有这个数字**,所以那条统计量的真实出处没能
  确认,按规则**不采用**,只保留这篇我核对过的"份额对比"结论。

### 处理 3 —— A 股场景下,开盘/收盘集合竞价要和"连续竞价阶段"的流动性分开估计(DiD 自然实验)
上交所 2018-08-20 引入收盘集合竞价(与 rules.md §1 的数据窗口、analysis.md 4.3 提到的制度断点日期一致)
之后的实证:引入后,连续竞价阶段的流动性**没有**显著变化,但成交量从"收盘连续竞价"转移到了
"收盘集合竞价前"的时段,改善了收盘价与盘前价的连续性,对小盘股的作用更明显。
可翻译的处理:把这类"制度上线"当结构断点处理,是在面板里加 `reform_dummy`(日期 ≥ 某个切换日)
并与候选交互,或者把 train 窗口按断点切成两段分别报 score,而不是像现在整段平均对待——这与
analysis.md 4.3 提出的"训练窗口内部制度断点"风险是同一件事,文献给出的是标准处理方式(自然实验/DiD),
不是回避它。
- 出处:Han, Q., Zhao, C., Chen, J. & Guo, Q., "Reexamining the Impact of Closing Call Auction on
  Market Quality: A Natural Experiment from the Shanghai Stock Exchange", *Pacific-Basin Finance
  Journal*, 2022, 74:101821. DOI 10.1016/j.pacfin.2022.101821.
  https://ideas.repec.org/a/eee/pacfin/v74y2022ics0927538x22001160.html
  `verified: true`(标题、作者、期刊卷期、DOI、核心结论在两次独立检索中一致出现)。

### 搜不到 / 未核实
- "用成交股数还是成交金额"这个问题本身,在"日内 U 型"这条文献线里**没有查到专门的对比**;
  这条问题的答案主要来自 Q2 的"量 vs 额"文献(见下),不是 Q1 本身的文献线。
- Jain, P. & Joh, G., "The Dependence between Hourly Prices and Trading Volume"(常被引为 NYSE 小时级
  U 型的经典实证,*Journal of Financial and Quantitative Analysis*, 1988)——搜索工具明确说这是它自己的
  背景知识,不是这次检索结果本身返回的,**我没有在搜索结果或页面上确认到它**,按规则标 `verified: false`,
  不作为可引用出处,只记录标题供下一轮核实。
- 该特征(头尾不对称)与短期反转的关系是正交还是重叠:没有直接文献给出"二元判断",比较接近的是
  "量-收益关系的符号取决于当日交易里知情成分占比"这个更一般的框架:
  - 出处:Llorente, G., Michaely, R., Saar, G. & Wang, J., "Dynamic Volume-Return Relation of
    Individual Stocks"(NBER Working Paper No. 8312,首版 2001-06;后发表于 *Review of Financial
    Studies*, 2002)。https://www.nber.org/papers/w8312 `verified: true`(NBER 工作论文首版日期在
    cutoff 前,标题/作者/机制在搜索结果中确认)。
  翻译:这支持 analysis.md 4.1 的 (c) 交互方向(`mul(C, sign(ts_delta(day_last(Close),1)))`)——
  按"昨日涨跌"条件化,本质是在区分"头重"到底是追涨噪音还是知情建仓,与该框架的机制是同一件事,
  但没有文献直接证实这个具体交互设计本身被验证过,只是机制上站得住。

---

## Q2 —— 尺度无关化(除以成交量)与异常成交量的标准定义

### 处理 1 —— 用换手率(股数 / 流通股数)而不是成交金额作流动性代理,是教科书级别的标准做法
用换手率代替原始成交量/金额水平作为流动性代理,发现换手率越高,后续收益越低,这个关系在控制了规模、
账面市值比、beta 之后依然显著;论文本身也用成交金额做过稳健性检验,同样发现金额与月度收益显著负相关。
**这与 analysis.md 1.7/1.5 发现的"换成 Amt,ρ_known 从 0.43 跳到 0.52 越线"方向完全一致**:
金额类成交量本身就是流动性/规模控制那一侧的东西,不是一个独立维度。
可翻译的处理:把原始量差换成 `div(Volume, LogFloatShares 对应的股数)` 这种换手率口径,
是比"除以当日成交量"更贴近文献标准定义的尺度无关化方式。
- 出处:Datar, V., Naik, N. & Radcliffe, R., "Liquidity and Stock Returns: An Alternative Test",
  *Journal of Financial Markets*, 1998, 1(2):203–219.
  https://www.london.edu/faculty-and-research/academic-research/l/liquidity-and-stock-returns-an-alternative-test
  `verified: true`。

### 处理 2 —— 把成交量/换手率当"条件变量"去调节动量,而不是直接当独立因子
过去的成交量(换手率)能预测动量的强度和持续性:高换手率的赢家反转更快,低换手率的输家反转更慢;
作者把成交量框架成连接"动量"和"价值"策略的桥梁,而不是一个独立的横截面因子。
可翻译的处理:如果要保留"头尾不对称"里的方向信息,比起把换手率本身当信号,更接近文献做法的是
`mul(其他信号, cs_bucket(由该特征定义的分组))` 式的交互/分组调节,而不是把归一化后的量差直接送进树。
- 出处:Lee, C. & Swaminathan, B., "Price Momentum and Trading Volume", *Journal of Finance*,
  2000, 55(5):2017–2069。 https://ideas.repec.org/a/bla/jfinan/v55y2000i5p2017-2069.html
  `verified: true`(刊物、卷期、页码一致;月份未能从检索结果精确核实到"几月",故年份标 2000,
  不写具体月)。

### 处理 3 —— "异常成交量"至少有两种并存的标准构造:差值型和比值型
- **差值型**:某个窗口的成交量 **减去** 前置安静窗口的平均成交量(用于衡量"意见分歧"带来的异常量)。
  可翻译:`sub(Volume, ts_mean(ts_delay(Volume, k), N))` 这种"减去自身历史水平"的写法,
  与 analysis.md 4.1 (a) 类"去自身慢速水平"的方向是同一件事,文献上也有先例,不是我们自己瞎编的处理。
  - 出处:Garfinkel, J., "Measuring Investors' Opinion Divergence"(研究新闻/公告后的成交量异常,
    提出"unexplained volume" = 事件后量 − 事件前安静期均量),*Journal of Accounting Research*, 2005。
    `verified: true`(通过搜索结果的二次摘要确认了这个"差值型"定义的存在和方向;没有直接打开原文核对
    精确的窗口长度和公式系数,这部分细节降权,只确认"差值型"这个构造思路本身)。
- **比值型**:当日(或某窗口)成交量 / 过去若干日的历史均量,是另一路常见的"异常成交量"构造,
  常被用作"关注度"的代理变量之一(与新闻报道、极端单日收益并列),但没有查到它的精确公式细节
  (基准窗口长度、是否取对数等)。
  - 出处:Barber, B. & Odean, T., "All That Glitters: The Effect of Attention and News on the Buying
    Behavior of Individual and Institutional Investors", *Review of Financial Studies*, 2008,
    21(2):785–818。 https://ideas.repec.org/a/oup/rfinst/v21y2008i2p785-818.html
    `verified: true`(定性结论——个人投资者是异常高量股票的净买入方,机构相反——在搜索结果中确认);
    但该论文"异常成交量"的具体公式**搜不到**,这部分标 `verified: false`。

### 处理 4 —— 原始量/额水平本身也是一个独立的收益溢价来源(visibility 渠道),不是纯噪声
极端高(低)成交量的股票在随后一个月/一周往往有正(负)的异常收益,作者把机制归因于"成交量冲击改变了
股票的可见度,进而改变需求和价格",并指出这个效应在控制了收益自相关、公告效应、市场风险、流动性后依然
存在。**这提示:如果把 Amt/Volume 水平直接作为因子的一部分(哪怕只是作为残差回归的解释变量,
如 analysis.md 4.1 (d) 的 `ts_regbeta(C, day_sum(Volume), 20)`),"去掉的部分"本身可能对应一个
真实、独立于流动性的溢价渠道,而不只是"噪声"——(d) 类操作去掉的到底是噪声还是这个真实渠道,
文献本身没有定论,是我们自己需要在样本外验证的。**
- 出处:Gervais, S., Kaniel, R. & Mingelgrin, D., "The High-Volume Return Premium",
  *Journal of Finance*, 2001, 56(3):877–919. DOI 10.1111/0022-1082.00349.
  `verified: true`(刊物、卷期、页码、DOI 多次独立检索一致;其"按十分位分类高/低量"的具体分类方法
  来自一篇二手 PUC-Rio 工作论文的转述,不是原文本身核对的,这部分细节标 `verified: false`)。

---

## Q3 —— 时点 / 方向性净流向

### 处理 1 —— 文献里对"时点"的常规处理是"固定分段再看持续性",不是对"峰值分钟"本身排序
把全天切成固定的半小时区段(13 段),发现某个区段的收益与之后同一区段(滞后 13、26、39 期……)的收益
显著正相关,并持续至少 40 个交易日。这是目前能查到的、对"日内时点"做横截面/时间序列结构化处理的
最接近的框架 —— 但它处理的是**收益**按固定钟点分段后的自相关,不是"成交量峰值出现在哪个钟点"本身。
- 出处:Heston, S., Korajczyk, R. & Sadka, R., "Intraday Patterns in the Cross-Section of Stock
  Returns", *Journal of Finance*, 2010-08, 65(4):1369–1407。
  https://ar5iv.arxiv.org/html/1005.3535 `verified: true`。

**搜不到**:没有查到任何论文把"`day_argmax(Volume)` 式的日内成交量峰值时间戳/位置"本身,
当作跨股票排序用的横截面因子来检验。analysis.md 的 N1 构造(峰量时点)在我查到的范围内确实是
"处女地",但也意味着没有文献能告诉我们这类特征预期的方向和强度。

### 处理 2 —— 带方向的尾盘净流向:文献给出的预期方向是"反转",不是"趋势延续"
美股尾盘(收盘前最后一小时)期货的带符号成交量失衡(net signed volume)能预测**隔夜**收益,
且呈现"失衡越大、隔夜反转越强"的模式,机制是做市商吸收尾盘失衡后在隔夜向其他投资者转移库存、
收取补偿;作者还报告卖盘失衡后的反转比买盘失衡后的更强(不对称)。
**这对 analysis.md N2(`day_mean(in_delta(mul(Volume, sign(Ret)), 30))`,两端净买卖压力不对称)
给出一个可检验的具体方向预期:如果机制类似,"尾盘净卖压大"更可能对应**次日**的正向反转,
而不是简单的"尾盘买盘重 = 以后涨"这种趋势延续假设 —— 这是审计时"机制清楚"那句话可以直接引用的来源。**
- 出处:Boyarchenko, N., Larsen, L. & Whelan, P., "The Overnight Drift", Federal Reserve Bank of
  New York Staff Reports, No. 917,首版 2020-02(2022-08 修订;正式期刊版发表于 *Review of Financial
  Studies* 2023-09,**已超过 cutoff,不作为出处,只用首版工作论文日期**)。
  https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr917.pdf
  `verified: true`(标题、作者、机构、首版/修订日期、核心机制在搜索结果中一致确认)。

### 处理 3 —— "用成交量本身当时钟"(等量分桶)是另一种时点哲学,和日历分钟轴是两种不同构造
用等成交量分桶(而不是等时间分钟)衡量买卖失衡,本质是把"量"当作时间轴本身,而不是在日历分钟轴上找结构。
这提示:我们核心用的是"日历分钟"的头尾差,如果要做"时点"类的新 idea,还有一个没人试过的维度是
"把时间轴换成成交量累积轴"(例如用累积成交量达到某比例所需的时钟时间,代替用固定分钟数切块),
这是 N1/N3 之外的第三条路,目前候选里没有出现。
- 出处:Easley, D., López de Prado, M. & O'Hara, M., "The Exchange of Flow Toxicity", *Journal of
  Trading*, 2011(Spring), 6(2):8–13;同作者 "The Microstructure of the 'Flash Crash': Flow Toxicity,
  Liquidity Crashes and the Probability of Informed Trading", *Journal of Portfolio Management*,
  2011(Winter), 37(2):118–128。 https://papers.ssrn.com/abstract=1695041 / 1748633
  `verified: true`(标题、作者、刊物、核心方法——等量分桶——在搜索结果中确认;该指标后续受到的
  复现争议——Andersen & Bondarenko 等——也在搜索结果中出现,如实记录但不是我们需要的那部分)。

### 搜不到 / 低置信度
- "聪明钱 vs 笨钱"这个说法在文献里是**基金资金流**层面的经典概念(资金流向后续表现好的基金/
  被动跟随表现好的基金经理),不是日内时点层面的概念;我**没有找到**把"日内开盘端重的成交量"
  直接等同于某种"聪明钱指标"的文献对应关系。Gruber (1996) / Zheng (1999) 这两篇作为"smart money"
  概念的源头,在搜索结果中确认存在(`verified: true`,仅确认存在性与大致结论方向,未核对原文細節),
  但它们与"日内时点"之间没有搜到直接桥接的论文。
- A 股"尾盘资金流预测次日收益"这个窄问题,**没有查到同行评审论文**,只查到一份挂在深交所官网的
  研究报告:侯丽薇、谢赤(湖南大学工商管理学院)、戴军、葛新元(国信证券经济研究所),
  《A 股市场资金流向指标应用分析》,深圳证券交易所研究报告,关键词"资金流向、噪音交易、羊群效应",
  核心结论是**分钟级**资金流向对未来收益存在**中期**反转效应(不是专门针对"尾盘"窄窗口)。
  https://szse.cn/aboutus/research/secuities/documents/P020180328492183310238.pdf
  `verified: true`(标题、作者、关键词、结论方向在搜索结果中看到了;但发表年月只能从文件名
  `P020180328...` 推断约 2018-03,不是正式标注的出版日期,这一条的"年-月"按低置信度处理,
  不建议直接引用这个日期本身,只引用其结论方向)。
- A 股开盘追涨/散户日内交易模式:查到的是日频层面的"日内-隔夜拔河"效应(同一批作者的一组论文,
  发现 A 股的日间与隔夜收益呈现跷跷板式的同期延续、跨期反转,机制归因于日内/隔夜两类客群主导不同时段),
  但**不是**专门针对"开盘追涨"这个更窄的行为模式。
  - 出处:Gao, Y., Han, X., Li, K. & Xiong, X. (2021), "Investor Heterogeneity and Momentum-Based
    Trading Strategies in China", *International Review of Financial Analysis*, 74。
    `verified: true`(标题、作者、刊物卷号、核心结论在搜索结果中确认;具体 DOI/页码未核实)。

---

## Q4 —— A 股制度细节:收盘集合竞价断点、涨跌停板宽度分组

### 处理 1 —— 2018-08-20 上交所收盘集合竞价上线:标准处理是 DiD 自然实验,核心发现是"流动性不变、量转移"
见 Q1 处理 3 的同一篇论文:引入后对**连续竞价阶段流动性**无显著影响,但把成交量从"收盘连续竞价"
推到了"收盘集合竞价前"的时段,改善了收盘价与盘前价格的连续性,对小盘股影响更大。
对我们直接有用的一点:这意味着 **2018-08-20 之后,"收盘前最后几分钟"的成交量结构本身发生了变化**
(一部分原本在最后几分钟连续竞价里成交的量,现在挪到了集合竞价里),这是 analysis.md 4.3 提到的
"训练窗口内部制度断点"的具体机制来源,而不只是一个猜测。
- 出处:同 Q1 处理 3(Han, Zhao, Chen & Guo, 2022, *Pacific-Basin Finance Journal* 74:101821)。
  `verified: true`。

### 处理 2 —— 更早的集合竞价透明度改革(2006 年上交所开盘集合竞价)提供了同一类型断点的另一个样本
研究上交所 2006 年提高开盘集合竞价信息披露透明度的改革,发现提高透明度后**连续竞价阶段**的流动性改善,
效应集中在原本流动性较差的股票上。这与处理 1 合在一起说明:**开盘端和收盘端的集合竞价改革,在 A 股历史上
不是一次性事件,是分散在不同年份的多次制度调整**,如果要严谨处理"训练窗口内部断点",至少要核对
2006(开盘集合竞价透明度)、2018-08-20(收盘集合竞价上线)这两个已知断点在 train/valid 窗口
(2018-01-02~2023-08-07)里各自落在哪一段。
- 出处:Gerace, D., Liu, Q., Tian, G. & Zheng, W., "Call Auction Transparency and Market Liquidity:
  Evidence from China", *International Review of Finance*, 2015, 15(2):223–255。
  https://ideas.repec.org/a/bla/irvfin/v15y2015i2p223-255.html `verified: true`。

### 处理 3 —— 涨跌停板宽度的常规处理:分组/固定效应,不是当连续特征直接进回归
价格限制(price limits)研究的标准处理路数,是按制度分组(例如创业板/科创板 vs 主板,或 ST vs 非 ST)
做事件研究或面板固定效应,比较"磁吸效应"(临近涨跌停时交易强度和波动放大)与"冷却效应"
(限制本身压低波动)这两种竞争假说;综述文献明确指出**这两种效应在实证上是否存在,目前没有共识**,
不同作者在同一个 2020 年创业板涨跌停扩大(10%→20%)事件上得出过相反结论(有的找到磁吸效应增强,
有的没找到磁吸效应)。
可翻译的处理:这进一步支持 analysis.md 1.4 对 `sigmoid(LimitWidth)` 的判断——
**`LimitWidth` 应该被当作分组哑变量/固定效应处理(如 `cs_bucket_demean(X, LimitWidth 对应的分组)`),
不应该被当作一个连续的、可以直接 sigmoid 压缩后送进树的"特征"**,这与规则 §4
"并列靠列序=板块信息"是同一个处理哲学的两种说法。
- 出处(明确核实到月份的具体事件研究):Bao, Q., "Effectiveness of Price Limits: Evidence from
  China's ChiNext Market", *PLOS ONE*, 2023-06-23, 18(6):e0287548. DOI 10.1371/journal.pone.0287548.
  `verified: true`(用 WebFetch 直接打开该页面核对了标题、作者、精确发表日期 2023-06-23、
  以及"未发现磁吸效应,但涨/跌两个方向的成交量恢复速度不对称"的结论——这个发表日期在
  2023-08-08 前,可以安心引用)。
- 出处(综述,确认这是一个有分歧、没有共识的领域):Sifat, I. & Mohamad, A., "A Survey on the Magnet
  Effect of Circuit Breakers in Financial Markets", *International Review of Economics & Finance*,
  2020, 69:1–17。 `verified: true`(标题、作者、刊物卷号在搜索结果中确认存在;具体综述内容
  未逐条核对,只确认了"该领域没有共识"这个定性判断的存在)。

### 搜到但日期不确定,**不采用**
- Zhang, X., Li, X., Hao, J. & Li, P., "Price Limit Change and Magnet Effect: The Role of Investor
  Attention", *Finance Research Letters*, 2023, 53(C)。该文结论(涨跌停扩大后磁吸效应**增强**,
  与投资者关注度正相关)与 Bao (2023) 的结论(未发现磁吸效应)直接冲突,如果要用需要两边都核实清楚
  —— 但更关键的是,我没能确认这篇的发表月份(只确认到年份 2023 和卷号 53),按规则"拿不准日期的不用",
  **这篇不作为本轮可引用出处**,只记录标题供下一轮核实月份后再用。 `verified: false`(日期这一项)。

---

## 给 PI / 结构解剖员的一句话小结

四个题目里,**查到最硬、最可直接翻译成任务说明的是 Q1 处理 2/3 和 Q4 处理 1/2**:
A 股自己的收盘集合竞价(2018-08-20)和更早的开盘集合竞价透明度改革(2006)都有同行评审文献,
且结论方向一致——集合竞价要单独算占比,不要和连续竞价的量混在一起,训练窗口要留意这两个断点。
**Q2 的"换手率优于金额水平"和"异常量=减去历史均量"两条,直接支持 analysis.md 4.1 (a)/(d) 两类外围设计**,
不是我们自己编的,文献上站得住。
**Q3 的"峰值时点"(N1)在能查到的范围内是真的没人做过**,没有文献能给方向预期,风险自担;
但 N2(带方向的尾盘净流向)**有**一篇可直接引用的机制来源,且预期方向是反转,不是追涨——
如果 PI 把 N2 写成"尾盘净卖压预测正收益"而不是"正收益预测本身方向不确定",审计员那句
"如果它有 alpha,最可能来自哪里"会更容易写。
