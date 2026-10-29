# 文献:种子 801,C 组,第 2 轮(文献员)

对准 `r2/analysis.md` 第 5 节的四个题目。只用 2023-08-08 之前发表/公开的文献(期刊发表日为准;工作论文 / SSRN / 会议稿以能确认到的最早版本日期为准)。
方法:WebSearch 逐题检索,关键命中用 WebFetch / 直接读 PDF 核对题名、作者、刊物、卷期页、日期与摘要原文。`verified: true` = 这次会话里确实在搜索结果摘要或页面正文中看到了该条目(非我自己的训练记忆)。
搜不到、读不到正文、或日期拿不准的,都在对应小节里明写“没搜到 / 看不到正文 / 日期不确定不用”,不猜。

---

## 题目 1:日内资金流倾斜(对准核心 A)

核心 A 的构造是 `div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret))`,再 `cross_ema(·, 10)`、`cross_mean(·, 20)` 之类做截面平滑——本质是"成交额加权分钟收益 − 等权分钟收益",除以日内波动去量纲。

### 处理方式(摘要 → 翻译成算子语言)

**(a) 归一化分母**
- 经典的"日度订单失衡"文献(Lee & Ready 1991 的逐笔买卖方向标记;Chordia, Roll & Subrahmanyam 2002)并不除以日内波动,而是直接用**买方发起量 − 卖方发起量**(股数或金额)做日度序列,有时再除以总成交量做百分比失衡。换句话说,"除以 `day_std(Ret)` 去量纲"是我们这条核心自己的选择,不是文献里资金流失衡的标准做法;文献更常见的分母是**总成交量/总成交额**,把失衡变成一个 [-1,1] 的比例,而不是一个夏普式统计量。
  → 算子翻译:可以加一个对照版本,分母换成 `day_sum(Amt)`(即 `div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_sum(Amt))` 的某种单调变换),检验"除以波动"这个选择本身是否在买涨指标里引入了额外的波动暴露(与陷阱 1 同构的风险)。
  引用:Lee & Ready (1991);Chordia, Roll & Subrahmanyam (2002)。

**(b) 平滑天数 / 预测期 / 衰减曲线**
- Chordia, Roll & Subrahmanyam (2002, JFE) 报告**日度**层面的市场总失衡高度持久(自身序列持久,但一阶差分负自相关),且大幅负失衡日之后出现收益反转。
- 同一组作者 2005 年的后续研究(常被引作 "Evidence on the Speed of Convergence to Market Efficiency")把失衡的可预测性推到**盘中分钟级**:1996 年样本里滞后失衡能预测未来最长到 30 分钟的收益,但这个窗口随样本往后推移在**缩短**(市场更有效、套利更快)。这给了一条直接可操作的提醒:资金流类信号的"衰减曲线"不是常数,样本内外都可能因为市场结构变化而缩短——对应规则里"样本外是否还在"的论证需要提到这一点。
- Jones, Shi, Zhang & Zhang 的工作论文(题为 *Understanding Retail Investors: Evidence from China*,ABFER 会议稿,首版 2019 年 9 月,见过的版本标注 2022 年 5 月;后来改题发表,发表版本晚于截止日期,这里只用工作论文版本)用**不同规模的散户日度失衡**预测未来 1 到 60 天的收益,是目前找到的唯一明确给出"预测期有多长"的 A 股文献:大散户与机构失衡通常正向预测收益,小散户失衡总是负向预测,且不依赖对手方。
  → 算子翻译:核心 A 现在只在 `cross_ema(·, 10)` / `cross_mean(·, 20)` 两个平滑窗口上试过;可以按 Jones et al. 的 1–60 天区间再扫一遍更短(5 天内)和更长(40–60 天)的窗口,预期是一条随窗口先升后降的曲线,而不是单调。
  引用:Chordia, Roll & Subrahmanyam (2002, JFE);Chordia, Roll & Subrahmanyam (2005,"Evidence on the Speed of Convergence to Market Efficiency" 系列,CFA Digest 摘要确认了盘中 30 分钟窗口和窗口随时间缩短这两点,原文未直接读到);Jones, Shi, Zhang & Zhang,*Understanding Retail Investors: Evidence from China*,工作论文。

**(c) 符号:延续还是反转,PIN/信息交易 vs 流动性交易的区分**
- Chordia, Roll & Subrahmanyam (2002) 的市场层面证据是"大幅负失衡之后收益反转",即失衡本身在**日度**上更像流动性冲击的痕迹,下一期有均值回复的成分,不是纯粹延续。
- Easley / PIN 一类文献(本次检索到的是对 PIN 方法的二手引用与批评:Bongaerts, Rösch & van Dijk 用价格冲击的截面差异把"信息性失衡"从总失衡里分离出来;Kaul, Lei & Stoffman 对"PIN 等于流动性测度"的解释给出了反例)说明同一个"失衡"读数,背后可能是信息交易(该延续)或纯流动性再平衡(该反转),区分依据通常是**价格冲击的大小**或**事件窗口**,不是失衡本身的水平。
  → 算子翻译:核心 A 目前没有做方向假设(符合规则 §3.5 教训 1,交给奖励决定符号),这是对的;但如果要进一步解释"为什么样本外还在",应该在假设里写清楚这条信号更像哪一类(本次检索没有看到能直接套用 A 股分钟数据做信息/流动性分类的现成方法,只能类比)。
  引用:Chordia, Roll & Subrahmanyam (2002, JFE);Bongaerts, Rösch & van Dijk(论文细节本次只看到摘要片段,标题/年份未能确认,**不单独计入参考文献,只作为旁证**,不得作为可核实出处使用)。

**(d) 按流动性 / 规模 / 散户占比分组后符号是否不同**
- Jones, Shi, Zhang & Zhang(工作论文,见上)按账户规模分组,发现**大户(含机构)失衡正向预测、小散户失衡始终负向预测**——这是目前找到的最直接的"分组后符号不同"证据,虽然是美股式的 Boehmer-Jones-Zhang-Zhang 识别法在中国数据上的应用,不是逐笔 Lee-Ready。
- Bailey, Cai, Cheung & Wang (2009, *Journal of Banking & Finance*) 用上交所数据比较个人 / 机构 / 自营三类失衡,发现**失衡的截面共性(commonality)在个人投资者里远强于机构/自营**,即不同投资者群体的失衡序列结构本身不同,这是分组的另一个维度(不是符号,是相关结构)。
  → 算子翻译:我们没有逐笔委托人身份数据,但可以用 `LogFloatCap` / 流动性控制分桶,检验核心 A 在大盘股 vs 小盘股子样本里符号/幅度是否一致——如果只在小盘股里显著,更接近"散户噪音"而非"机构资金流"的解释,呼应 r1 审计员的竞争解释。
  引用:Jones, Shi, Zhang & Zhang,工作论文(见上);Bailey, Cai, Cheung & Wang (2009, *Journal of Banking & Finance*, 33(1), 9–19)。

**(e) 这类"成交额加权收益 − 等权收益"的截面差异,文献有没有指出主要来自日内 U 形时段构成**
- **没搜到直接做这个归因的文献**(即没有论文明说"VW-EW spread 主要是 U 形造成的,这样扣掉")。能找到的是两组相关但不等价的证据:
  1. Admati & Pfleiderer (1988) 给出 U 形的**理论机制**:无信息的"自由裁量"流动性交易者会集中在厚市场时段(开盘/收盘)交易以降低逆选择成本,这本身就会让开/收盘的成交额权重远高于盘中,如果开盘/收盘的收益系统性不同于盘中均值,`day_wmean(Ret, Amt)` 相对 `day_mean(Ret)` 的差就会部分来自**时段构成**而不是"钱往哪边走"。
  2. Jain & Joh (1988) 的实证进一步确认:不仅成交量是 U 形,**不同小时的收益率本身也不同**,这是 U 形解释成立的必要前提(如果各时段收益率都一样,U 形权重变化不会制造任何加权-等权差)。
  3. Heston, Korajczyk & Sadka (2010, *Journal of Finance*) 是**反向证据**:他们在半小时收益延续的回归里显式控制了成交量变化率、订单失衡变化、价差、大单/小单成交量,发现这些控制**不能解释掉**收益延续效应——即"类似资金流/成交量的量"控制之后,收益模式仍然存在。这不是对我们这个具体构造的检验,但提示"被某个成交量相关的量解释掉"不是必然结果。
  → 算子翻译:这正是 analysis.md 里 R14/R15 要做的事——R14 把 `Amt` 权重换成纯时间权重 `in_index(Amt)`,直接把(e)问题的"文献没做过的归因"变成一次可以自己算的对照实验,这是本题目前最值得花评估次数的地方。
  引用:Admati & Pfleiderer (1988, *Review of Financial Studies*, 1(1), 3–40);Jain & Joh (1988, *Journal of Financial and Quantitative Analysis*,题为 "The Dependence between Hourly Prices and Trading Volume",卷期页本次未能核实到,**日内 U 形与小时收益率差异两点确认属实,卷期页信息 verified: false**);Heston, Korajczyk & Sadka (2010, *Journal of Finance*,通过 arXiv 预印本 1005.3535 核对)。

**(f) A 股(T+1、无做空、散户主导)上的复现与美股差异**
- Jones, Shi, Zhang & Zhang 的工作论文是目前找到的最接近"用 A 股数据测资金流失衡预测力"的文献,结论是**散户内部也不同质**(大户预测对、小户预测错),不能笼统说"A 股散户主导所以资金流信号更强"。
- Bailey, Cai, Cheung & Wang (2009) 的上交所证据说明个人与机构失衡的**统计结构**不同(个人失衡共性更强),提示在全市场截面上做"资金流倾斜"时,信号可能主要被个人投资者的共同行为驱动,而不是机构的信息交易——这和核心 A 的竞争解释(机构资金流 vs 散户 U 形噪音)是同一个问题的两种措辞。
  引用:同 (d)。

### 参考文献(题目 1)

| 条目 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|
| Inferring Trade Direction from Intraday Data | Charles M. C. Lee, Mark J. Ready | 1991-06 | Journal of Finance, 46(2), 733–746 | https://ideas.repec.org/a/bla/jfinan/v46y1991i2p733-46.html | true |
| Order imbalance, liquidity, and market returns | Tarun Chordia, Richard Roll, Avanidhar Subrahmanyam | 2002-07 | Journal of Financial Economics, 65(1), 111–130 | https://ideas.repec.org/a/eee/jfinec/v65y2002i1p111-130.html | true |
| Evidence on the speed of convergence to market efficiency(Chordia/Roll/Subrahmanyam 系列,盘中 30 分钟窗口及窗口随时间缩短,二手摘要确认) | Tarun Chordia, Richard Roll, Avanidhar Subrahmanyam | 2005(月份未确认) | CFA Institute Digest 对 JFE 论文的摘要 | https://rpc.cfainstitute.org/en/research/cfa-digest/2005/11/evidence-on-the-speed-of-convergence-to-market-efficiency-digest-summary | true(二手摘要;未读到原文 PDF) |
| A Theory of Intraday Patterns: Volume and Price Variability | Anat R. Admati, Paul Pfleiderer | 1988-03 | Review of Financial Studies, 1(1), 3–40 | https://academicnewsletter.sufe.edu.cn/info/355980 | true |
| The Dependence between Hourly Prices and Trading Volume | Prem C. Jain, Gun-Ho Joh | 1988(卷期页未核实) | Journal of Financial and Quantitative Analysis | (多个二手引用确认题名/作者/年份,未定位到可直接核实卷期页的页面) | true(题名/核心结论);false(卷期页) |
| Intraday Patterns in the Cross-section of Stock Returns | Steven L. Heston, Robert A. Korajczyk, Ronnie Sadka | 2010-05(预印本日期);发表于 Journal of Finance | arXiv:1005.3535 | https://ar5iv.arxiv.org/html/1005.3535 | true |
| Understanding Retail Investors: Evidence from China(工作论文,后以其他标题发表,发表版本晚于截止日期不用) | Charles M. Jones, Donghui Shi, Xiaoyan Zhang, Xinran Zhang | 首版 2019-09,见过版本 2022-05 | ABFER 会议论文 | https://abfer.org/media/abfer-events-2022/annual-conference/papers-investfin/AC22P3020_Understanding-Retail-Investors_Evidence-from-China.pdf | true |
| Stock returns, order imbalances, and commonality: Evidence on individual, institutional, and proprietary investors in China | Warren Bailey, Jun Cai, Stephen Y. L. Cheung, Fenghua Wang | 2009 | Journal of Banking & Finance, 33(1), 9–19 | https://ideas.repec.org/a/eee/jbfina/... (经 IDEAS/HKBU 记录核实题名作者年份;DOI 10.1016/j.jbankfin.2006.08.007) | true |
| Liquidity, Volume, and Order Imbalance Volatility(失衡的"波动率"而非水平被定价,备用旁证,未展开到算子翻译) | Vincent Bogousslavsky, Pierre Collin-Dufresne | 工作论文 2019-12(SFI RP 19-69);发表于 Journal of Finance 2023(发表版晚于截止日期不用,只用工作论文版) | Swiss Finance Institute Research Paper No. 19-69 | https://ideas.repec.org/p/chf/rpseri/rp1969.html | true |

**没搜到 / 不用的**:Bongaerts-Rösch-van Dijk 的具体题名年份(只有摘要片段,未核实);任何直接证明"VW−EW 日内收益差主要由 U 形时段构成解释"的论文(没有)。

---

## 题目 2:高阶矩的分母该放什么(对准 head +1.22 的 R 组)

head +1.22 是 `cross_mean(div(day_sum(mul(mul(Ret,Ret),Ret)), mul(day_sum(pow_3(Volume)), day_sum(pow_3(Volume)))), 20)`——分子是日内三阶矩,分母是**成交量三次方和的平方**。

### 处理方式

**(a) ACJV 的 `sqrt(N)·Σr³/RV^1.5`、BLZ 的 `(RV⁺−RV⁻)/RV` 之外,有没有文献用成交量/成交额的幂当分母**
- Amaya, Christoffersen, Jacobs & Vasquez(直接读了 2013-02-21 的工作论文 PDF 首页与摘要,标题确认为 *Does Realized Skewness Predict the Cross-Section of Equity Returns?*)用**日内收益的三次方和**构造已实现偏度,摘要明确说"compute realized skewness and kurtosis from intraday cubed and quartic returns",分母是已实现波动率的幂(标准写法 `RVar^1.5`),不是成交量。
- Bollerslev, Li & Zhao (2020, *Journal of Financial and Quantitative Analysis*, 55(3), 751–781)的"相对符号跳跃方差"是**已实现上行方差减下行方差、再除以已实现总方差**(页面摘要原文:对股票按"normalized good minus bad volatilities"排序),分母同样是已实现方差本身,不是成交量。
- Patton & Sheppard (2015, *Review of Economics and Statistics*, 97(3), 683–697)是这条测度的更早来源(已实现半方差的不对称性),同样以方差类的量做分母。
- **没有搜到任何一篇把高阶矩除以成交量(或成交额)的幂来做归一化的文献**。所有搜到的"高阶矩/非对称波动"文献分母清一色是已实现方差(或其幂),不是成交量。换句话说,head +1.22 用 `(ΣVolume³)²` 当分母,在这条文献脉络里**找不到对应**——这本身就是 R10(把分母换回已实现方差 `(Σr²)²`)值得做的理由:它是把一个"文献里没有先例"的构造换回"文献里的标准做法"。
  → 算子翻译:R10 `cross_mean(div(day_sum(mul(mul(Ret,Ret),Ret)), mul(day_sum(mul(Ret,Ret)), day_sum(mul(Ret,Ret)))), 20)` 正是把分母从成交量幂换成收益平方和(≈已实现方差)的幂,与 ACJV/BLZ/Patton-Sheppard 的归一化传统一致;如果 R10 分数显著低于 head +1.22,等于文献上"正确"的归一化反而分数更低,这本身是要写进报告的发现。
  引用:Amaya, Christoffersen, Jacobs & Vasquez(工作论文 2013-02,CREATES RP 2013-41;发表版 *Journal of Financial Economics*, 118(1), 135–167, 2015);Bollerslev, Li & Zhao (2020, JFQA);Patton & Sheppard (2015, ReStat)。

**(b) 有没有文献指出"高阶矩除以成交量的幂"实际是流动性/成交集中度的非线性暴露,以及怎样诊断**
- **没搜到**直接做这个诊断的论文(把"除以成交量幂"的高阶矩拿去做分组/双重排序/对成交量样条中性化,专门证明它是流动性暴露)。
- 能找到的最接近的是 Ahadzie & Jeyasreedharan (2020, *Journal of Behavioral and Experimental Finance*, 28, 100413),题为 *Trading volume and realized higher-order moments in the Australian stock market*。摘要明确说"成交量与已实现偏度/峰度的关系少有人研究",说明这块文献本来就稀薄;正文被塔斯马尼亚大学机构库永久封存,**看不到具体诊断方法**,只能确认这篇论文存在、研究对象匹配,方法细节无法核实。
- Hong & Stein (2003, *Review of Financial Studies*, 16(2), 487–525)是更早的理论来源:差异意见模型预测**高成交量时收益负偏度更强**,即成交量和(负)偏度的关联在理论上是预期之中的,但这是"量越大、偏度越负"的方向性理论,不是"除以量的幂做分母"这种构造上的诊断。
  → 算子翻译:既然文献没有现成的"双重排序去混淆"方法,PI 如果要在 train 上自己诊断 head +1.22 是不是流动性暴露,R7–R9 的凸度阶梯加上 R10 的换分母,已经是 analysis.md 设计里能做的最接近"诊断"的事(剂量反应 + 换维度),文献层面找不到更现成的办法可以抄。
  引用:Ahadzie & Jeyasreedharan (2020, *Journal of Behavioral and Experimental Finance*);Hong & Stein (2003, *Review of Financial Studies*)。

**(c) 已实现偏度与成交量集中度/大单占比的截面相关,文献报过吗**
- **没搜到**直接报告这个相关系数的论文。Ahadzie & Jeyasreedharan (2020) 大概率涉及这个问题但正文看不到。
  → 明确记为"搜不到"。

**(d) 分钟收益的最小价位离散与涨跌停截尾对已实现偏度的偏误,文献怎样修正**
- **没搜到**专门针对"已实现偏度 + 最小价位离散/涨跌停截尾"的修正方法论文。相关但不对口的文献:tick size 对收益分布/相关系数的补偿方法(本次检索到一篇用纯 tick size 做补偿、不需要调参的方法,但它修正的是**相关系数**,不是偏度;论文题名/作者本次未能确认,不计入参考文献)。微观结构噪声对已实现波动率的影响是成熟文献(Andersen & Bollerslev 1997 是对日内周期性的处理,见题目 4),但没有一篇把这个和**涨跌停截尾**结合起来谈偏度偏误。
  → 算子翻译:这块文献缺口直接对应环境自己的"已知陷阱 1"——如果我们自己要做截尾修正,目前没有现成文献可抄,只能依赖 `LimitWidth` 做自己的工程修正(呼应 N 灵感 3)。
  引用:无(明确记为没搜到)。

### 参考文献(题目 2)

| 条目 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|
| Does Realized Skewness Predict the Cross-Section of Equity Returns? | Diego Amaya, Peter Christoffersen, Kris Jacobs, Aurelio Vasquez | 2013-02(工作论文);发表版 2015(JFE 118(1), 135–167) | CREATES Research Paper 2013-41(直接读取 PDF) | http://ssrn.com/abstract=1898735 | true(直接读了 PDF 标题页与摘要) |
| Good Volatility, Bad Volatility, and the Cross Section of Stock Returns | Tim Bollerslev, Sophia Zhengzi Li, Bingzhi Zhao | 2020-05 | Journal of Financial and Quantitative Analysis, 55(3), 751–781 | https://ideas.repec.org/a/cup/jfinqa/v55y2020i3p751-781_2.html | true(直接 WebFetch 该页) |
| Good Volatility, Bad Volatility: Signed Jumps and the Persistence of Volatility | Andrew J. Patton, Kevin Sheppard | 2015 | Review of Economics and Statistics, 97(3), 683–697 | https://ideas.repec.org/a/tpr/restat/v97y2015i2p683-697.html | true |
| Trading volume and realized higher-order moments in the Australian stock market | Kwabena Ahadzie, Nadia Jeyasreedharan | 2020 | Journal of Behavioral and Experimental Finance, 28, 100413 | https://ideas.repec.org:443/a/eee/beexfi/v28y2020ics2214635020303403.html | true(题名/刊物/摘要主旨;正文被永久封存看不到) |
| Differences of Opinion, Short-Sales Constraints, and Market Crashes | Harrison Hong, Jeremy C. Stein | 2003(夏季号) | Review of Financial Studies, 16(2), 487–525 | https://ideas.repec.org/a/oup/rfinst/v16y2003i2p487-525.html | true |

**没搜到 / 不用的**:用成交量幂做高阶矩分母的任何文献;已实现偏度与大单占比截面相关系数的任何数字;已实现偏度的最小价位/涨跌停截尾专门修正方法。

---

## 题目 3:隔夜 vs 盘中切分(对准 N 灵感 1)

### 处理方式

**(a) 两段符号是否相反,预测期多长**
- Lou, Polk & Skouras (2019, *Journal of Financial Economics*, 134(1), 192–213,题为 *A tug of war: overnight versus intraday expected returns*)是这条切分的主文献:14 个经典策略里,利润**要么全部来自隔夜段、要么全部来自盘中段**,且跨段之间存在**反向的拉锯**("tug of war"),这个模式持续多年。平滑后的"隔夜 − 盘中"利润差本身能预测该策略未来整体(close-to-close)表现的时变强弱。
- Berkman, Koch, Tuttle & Zhang (2012, *Journal of Financial and Quantitative Analysis*, 47(4), 715–741,题为 *Paying Attention: Overnight Returns and the Hidden Cost of Buying at the Open*)专门研究隔夜段本身:隔夜收益**系统性为正**,随后盘中**系统性反转**,机制是开盘价相对盘中价偏高;这个效应集中在最近被散户关注、估值难、套利成本高的股票上,随散户情绪走强。
  → 算子翻译:两篇文献都支持 N 灵感 1 的"隔夜/盘中按构造正交"的设计是对的方向;但符号不是固定的(隔夜正、盘中反转 vs 其他策略里隔夜和盘中谁正谁负取决于策略本身),所以种子里不要预设方向,这与规则 §3.5 教训 1 一致。
  引用:Lou, Polk & Skouras (2019, JFE);Berkman, Koch, Tuttle & Zhang (2012, JFQA)。

**(b) 用水平还是占比/之差,窗口多长**
- Lou, Polk & Skouras 把隔夜、盘中各自的**累计收益水平**分开算(对数收益可加),再看"隔夜收益 − 盘中收益"的**平滑差**(他们用的是对该差值的移动平均)作为预测变量,预测的是策略未来的 close-to-close 收益——用的是"水平的平滑差",不是比例。
  → 算子翻译:analysis.md 里给的算子(隔夜 `div(day_first(Open), ts_delay(day_last(Close), 1))`、盘中 `div(day_last(Close), day_first(Open))`,取 log 后 `cross_mean(·, 20/60)`,或两者之差/比)与文献做法一致;20/60 日的平滑窗口量级与 Lou-Polk-Skouras 用"多年持续"的发现方向一致(窗口可以比日度更长)。

**(c) "隔夜=散户/情绪、盘中=机构"的证据与检验方式**
- Berkman 等(2012)的检验方式是:按**最近是否被散户关注**(用成交量/波动率代理关注度)分组,效应只在高关注度组显著;再按**套利成本/估值难度**分组,效应在难套利股票里更强;再看效应**随散户情绪指数走强**。这三条分组检验合在一起,是"隔夜=散户/情绪"这个说法的证据链,不是单一检验。
  → 算子翻译:我们没有散户关注度或情绪指数数据,但可以用波动率、流动性分组(作为关注度/套利成本的代理)重复这个检验逻辑,呼应题目 1 (d) 的分组思路。
  引用:Berkman, Koch, Tuttle & Zhang (2012, JFQA)。

**(d) 与 1 个月反转、动量的关系——是不是其中一段才带着反转**
- Lou, Polk & Skouras (2019) 明确说传统动量策略的利润**几乎全部来自盘中段**,而很多反转类策略的利润**几乎全部来自隔夜段**(两者方向相反,互相抵消,这正是题目说的"是不是其中一段才带着反转")。
  → 这直接支持 analysis.md 里"5 个控制里的反转是两段之和、和与差正交"的论证:既然反转利润主要来自隔夜段,而我们的 20 日反转控制没有单独扣掉隔夜,核心轴(隔夜 − 盘中之差/比)确实能带来和反转控制不完全重合的新信息。
  引用:Lou, Polk & Skouras (2019, JFE)。

**(e) A 股 T+1 与集合竞价的专门研究,开盘集合竞价收益要不要单独剔除**
- Qiao & Dam (2020, *Journal of Financial Markets*, 50, 文章编号見刊物页)题为"The overnight return puzzle and the 'T+1' trading rule in Chinese stock markets":A 股隔夜收益显著为负,归因为 T+1 规则本身——T+1 限制当日买入的股票不能当日卖出,导致开盘价相对前一日收盘存在折价,从而机械产生负隔夜收益。这与美股隔夜收益为正的 Berkman 等结论**方向相反**,是题目要求的"美股差异"的直接证据。
- Jiang, Luo & Ye(2023-05,*Global Finance Journal*, 56, 文章编号 100827,题为 *Factor beta, overnight and intraday expected returns in China*)用 Fama-French 五因子的贝塔做切分:市场、价值、盈利能力因子的贝塔溢价主要在**隔夜**兑现、盘中为负;规模和投资因子的贝塔溢价则相反。作者倾向用"投资者客群"(散户倾向开盘交易、机构倾向尾盘)而非风险定价来解释,这支持 N 灵感 1"隔夜=散户决策、盘中=机构执行"的制度论证。
- 一篇基于 2000–2016 年 A 股数据、应用 Lou-Polk-Skouras 分解的中文期刊论文(本次检索到的是其摘要与部分数字,期刊/作者未能完全核实,**暂不计入可核实参考文献**)报告隔夜动量与盘中动量方向相反、且 T+1 约束在高波动期更强地压制月度动量——如果这条成立,是直接支持 N 灵感 1"为什么样本外还在"(T+1 制度在样本期后没变)的证据,但因为无法核实出处,这里只作为需要进一步确认的线索,不写进可引用列表。
  → 算子翻译:开盘集合竞价本身的收益是否要单独剔除,本次检索**没有看到明确建议**;Qiao & Dam 把开盘价本身(含集合竞价结果)作为"隔夜段终点",没有另外剔除集合竞价段。我们用后复权 `day_first(Open)` 算隔夜收益,口径与 Qiao & Dam 一致,不需要额外处理集合竞价。
  引用:Qiao & Dam (2020, *Journal of Financial Markets*);Jiang, Luo & Ye (2023-05, *Global Finance Journal*)。

**(f) 用后复权价算隔夜收益时的除权日处理**
- 没有在 A 股专门文献里搜到除权日处理的细节讨论。美股文献(LuxAlgo 的操作说明,**非学术论文,仅作工程参考不计入正式引用**)的通行做法是:用复权价(adjusted close)算隔夜收益,且开盘价要用和收盘价**同一个复权因子**调整,否则除权日当天的隔夜收益会被人为扭曲。
  → 算子翻译:environment 的价格字段已经是后复权(r1 审计员据 `tradability.py`/`label.py`/`daily.py` 确认),`day_first(Open)` 与 `day_last(Close)` 用的是同一套复权规则,不需要我们自己再做除权调整——但这意味着 `log(day_first(Open))` 的水平本身混入了历史分红的影响,这一点 analysis.md 已经在核心 C 的讨论里提到,这里不重复展开,只确认"算隔夜收益不需要额外处理"这一条是安全的。
  引用:无学术文献,仅工程惯例确认,不计入正式参考文献表。

### 参考文献(题目 3)

| 条目 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|
| A tug of war: overnight versus intraday expected returns | Dong Lou, Christopher Polk, Spyros Skouras | 2019 | Journal of Financial Economics, 134(1), 192–213 | https://researchonline.lse.ac.uk/id/eprint/87481 | true(直接 WebFetch 该页) |
| Paying Attention: Overnight Returns and the Hidden Cost of Buying at the Open | Henk Berkman, Paul D. Koch, Laura Tuttle, Ying Jenny Zhang | 2012-08 | Journal of Financial and Quantitative Analysis, 47(4), 715–741 | https://ideas.repec.org/a/cup/jfinqa/v47y2012i04p715-741_00.html | true |
| The overnight return puzzle and the "T+1" trading rule in Chinese stock markets | Kenan Qiao, Lammertjan Dam | 2020 | Journal of Financial Markets, 50 | https://ideas.repec.org/a/eee/finmar/v50y2020ics1386418120300033.html | true |
| Factor beta, overnight and intraday expected returns in China | Danling Jiang, Yunfeng Luo, Zhengke Ye(作者署名顺序在不同数据库记录不一致) | 2023-05 | Global Finance Journal, 56, 100827 | https://ideas.repec.org/a/eee/glofin/v56y2023ics1044028323000224.html | true |

**没搜到 / 不用的**:开盘集合竞价收益是否要单独剔除的明确文献建议;2000–2016 年 A 股隔夜/盘中动量反转的中文期刊论文(找到摘要但出处无法核实,不计入);除权日调整在 A 股语境下的专门讨论。

---

## 题目 4:日内成交的时点(对准 N 灵感 2)

### 处理方式

**(a) 度量方式**
- Heston, Korajczyk & Sadka (2010, *Journal of Finance*,通过 arXiv:1005.3535 核对)把交易日切成 13 个半小时区间,用**半小时收益**本身做基本单位,副产品是成交量、订单失衡、波动率、价差都呈现相同的日内周期性(他们统计了这几类量按半小时的分布),但论文主角是收益延续,不是"资金几点成交"这个量本身。
- Gao, Han, Li & Zhou (2018, *Journal of Financial Economics*, 129, 394–414,题为 *Market Intraday Momentum*)用**第一个半小时收益**预测**最后半小时收益**,核心度量是"开盘段收益"而非成交量/成交额的时点分布,但方法论上示范了"把一天切成有限几段、用某一段的量去预测另一段"这种构造——这是 N 灵感 2 里"开盘占比"、"尾盘占比"这类度量的方法论近亲。可预测性随**波动率和成交量**走高而走高。
  → 算子翻译:`day_wmean(in_index(Amt), Amt)`(成交额加权的平均时点)、`day_topw_mean(in_index(Amt), Amt)`(尾盘集中度)这类度量在文献里没有逐字对应,但 Heston-Korajczyk-Sadka 的半小时切分和 Gao-Han-Li-Zhou 的"首段预测尾段"提供了两种相邻的构造思路,可以作为种子的变体方向(例如把 `in_index` 换成离散的半小时桶再做首尾段对比,而不是连续的加权平均时点)。
  引用:Heston, Korajczyk & Sadka (2010, JF);Gao, Han, Li & Zhou (2018, JFE)。

**(b) 怎样去掉日内周期性与市场共同成分**
- Andersen & Bollerslev (1997, *Journal of Empirical Finance*, 4(2–3), 115–158,题为 *Intraday periodicity and volatility persistence in financial markets*)是这条处理方法的源头:用**柔性傅里叶形式(Flexible Fourier Form)**单独估计日内周期性成分,把它从条件日度波动率模型中剥离出来,是后续文献处理"先去周期性、再谈个股特征"的标准手法。
- Heston, Korajczyk & Sadka (2010) 没有用傅里叶去周期性,而是用**按时间段分组**(开盘半小时 / 午盘 / 收盘半小时单独报告)加上对等权市场收益的风险调整(13 期前后滞后回归)来处理共同的日内模式。
  → 算子翻译:N 灵感 2 里提议的"相对自身 60 日均值的偏离"是比傅里叶形式更简化的去周期性方法,方向上和 Andersen-Bollerslev 的思路一致(都是"先估计一个基准周期形状,再看偏离"),但没有文献直接验证"除以自身 60 日均值"这种简化版本是否足够干净——这是一个需要在 train 上自己验证的简化,不是照抄文献。
  引用:Andersen & Bollerslev (1997, *Journal of Empirical Finance*);Heston, Korajczyk & Sadka (2010, JF)。

**(c) 它与规模/流动性/指数成分资格的机械相关有多强,文献怎样中性化**
- Han, Zhao, Chen & Guo (2022, *Pacific-Basin Finance Journal*, 74, 101821,题为 *Reexamining the impact of closing call auction on market quality: A natural experiment from the Shanghai stock exchange*)用 2018 年 8 月 20 日上交所收盘集合竞价改革做自然实验:改革把一部分成交量从连续竞价阶段**挤到了收盘前的集合竞价阶段**,抬高了收盘前波动率;效应在**小盘股**里最明显。这说明"尾盘成交占比"这个量本身就和规模(以及制度改革的时间点)机械相关,且这个机械相关在样本期内(训练集覆盖到 2018 年改革前后)**不是稳定的**——是一个制度断点,不是平滑漂移。
  → 算子翻译:呼应 analysis.md 自己写的风险点,N 灵感 2 的种子如果要控制规模/流动性的机械相关,2018-08-20 这个日期在我们的 train 窗口(2018-01-02 起)内,构造尾盘占比类特征时要留意这个断点可能在 train 早期制造一次性的分布漂移,不只是题目 (e) 说的"长期趋势"。
  引用:Han, Zhao, Chen & Guo (2022, *Pacific-Basin Finance Journal*)。

**(d) 预测的是收益还是波动/流动性;尾盘占比高=机构/被动资金痕迹的收益证据**
- Heston, Korajczyk & Sadka (2010) 是把"量的日内分布"和"收益延续"放在一起测的少数文献之一,结论是量的周期性**不能解释**收益延续,即量的时点分布本身在他们的设定里更像是和收益延续**共生**而非**因果**的关系。
- Han, Zhao, Chen & Guo (2022) 测的是**市场质量**(流动性、波动率、价格连续性),不是收益可预测性,没有做"尾盘占比高→未来收益"的截面检验。
- **没搜到**一篇直接做"尾盘成交占比→未来个股收益"截面检验、且把尾盘占比解释为"机构/被动资金痕迹"的学术论文(能找到的只有非学术的行业简报,且数据是香港市场、日期大概率晚于 2023-08-08,不计入)。
  → 这是本题最大的文献空白:N 灵感 2 目前没有现成文献支持"尾盘占比预测收益"这个具体方向,analysis.md 里"预防性降相关"的设计思路(相对自身 60 日均值的偏离)在没有文献背书的情况下,更依赖 train 上的自我验证,审计时如果按"合理度 4"(文献证据)来要求,这一条目前只能打到"合理度 3"(机制说得通、没有文献或 train 证据)。
  引用:Heston, Korajczyk & Sadka (2010, JF);Han, Zhao, Chen & Guo (2022, *Pacific-Basin Finance Journal*)。

**(e) 收盘集合竞价占比上升的长期趋势会不会让这个特征的分布随时间漂移**
- Han, Zhao, Chen & Guo (2022) 的证据本身就是这条问题的答案雏形:2018 年改革之后,集合竞价阶段分走了更多成交量,前后是**两个不同的分布**,不是连续漂移。如果我们的 `cs_state_rank` 之类按历史分位数做的算子跨过这个断点,分位数定义本身在断点前后就不一致。
  → 算子翻译:如果 N 灵感 2 的种子使用任何依赖长期历史分布做归一化的算子(如 `cross_mean(·, 60)` 起步阶段跨过 2018-08-20),要在假设里提一句这个断点,审计员大概率会问。
  引用:Han, Zhao, Chen & Guo (2022, *Pacific-Basin Finance Journal*)。

### 参考文献(题目 4)

| 条目 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|
| Intraday Patterns in the Cross-section of Stock Returns | Steven L. Heston, Robert A. Korajczyk, Ronnie Sadka | 2010-05(预印本);发表于 Journal of Finance | arXiv:1005.3535 | https://ar5iv.arxiv.org/html/1005.3535 | true |
| Market Intraday Momentum | Yan Gao, Yeguang Han, Sophia Zhengzi Li, Guofu Zhou | 2018 | Journal of Financial Economics, 129, 394–414 | https://academicnewsletter.sufe.edu.cn/info/356150 | true |
| Intraday periodicity and volatility persistence in financial markets | Torben G. Andersen, Tim Bollerslev | 1997 | Journal of Empirical Finance, 4(2–3), 115–158 | https://ideas.repec.org:443/a/eee/empfin/v4y1997i2-3p115-158.html | true |
| Reexamining the impact of closing call auction on market quality: A natural experiment from the Shanghai stock exchange | Han, Zhao, Chen, Guo(名未逐一核实,姓氏见于 Cardiff ORCA 记录) | 2022 | Pacific-Basin Finance Journal, 74, 101821 | https://orca.cardiff.ac.uk/id/eprint/151359/ | true(题名/刊物/卷期/主要结论;作者全名未逐一核实) |

**没搜到 / 不用的**:尾盘成交占比直接预测个股未来收益、并被解释为"机构/被动资金痕迹"的学术论文;A 股(而非香港)收盘集合竞价成交占比的长期时间序列数据或学术研究。

---

## 给 PI 和结构解剖员的一句话归纳

- 题目 1、3 文献最厚,能直接支持 analysis.md 已经设计好的 R 组(尤其 R14/R15 对应题目 1(e)的文献空白,是本题唯一可以自己补上的地方)。
- 题目 2 的核心发现是**负向的**:遍历了已实现偏度/相对跳跃方差这条文献线,没有一篇用成交量的幂做分母——head +1.22 这个构造在文献里找不到先例,R10(换回已实现方差做分母)不是"锦上添花",而是把构造换回文献主流做法后的一次直接对照。
- 题目 4 的核心发现也是**负向的**:尾盘成交占比预测收益这条链路目前没有学术文献支持,只有一篇关于集中竞价改革对市场质量(而非收益)影响的论文,且该论文本身提示 2018-08-20 在 train 窗口内是一个分布断点。N 灵感 2 如果要达到"合理度 4",目前只能靠 train 证据,文献这条路走不通。
