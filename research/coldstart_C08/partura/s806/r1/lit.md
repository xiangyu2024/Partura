# 文献:种子 806,第 1 轮(对准 analysis.md §8 的 Q1–Q4)

检索方式:WebSearch + WebFetch(含对 PDF 用 `pdftotext` 直接读正文)。只用 2023-08-08 之前的论文 / 工作论文 / 报告;日期拿不准的条目在下面逐条注明、不计入可用引用。**本轮 WebSearch 配额在 Q4 后段被用尽**(工具报错 "this turn's web search budget is used up"),所以 Q4 的 (b) 小问(缺失值在乘积型聚合里的处理、"数据缺失模式被挖成因子"这个方法论问题)以及 Q1 的 (c) 小问(跳跃的成交量加权)**没有搜到直接对准的文献**,如实记录在对应小节,没有编造。

每条处理方式后面用 `[Lx]` 指向文末参考文献;参考文献块里写明标题、作者、年-月、来源、链接、`verified`。

---

## Q1 —— 核心 ① `day_max(Ret)`(通道 D:MAX / 跳跃 / 博彩偏好)

**(a) 怎么定义"极端正收益":单一极值 vs 上尾若干个的平均**

- 原始 MAX 的定义是"过去一个月里日收益的最大值"(月窗口里取日频极值,不是日窗口里取分钟频极值)[L1]。这和我们的 `day_max(Ret)`(日窗口取分钟频极值)在"聚合层级"上刚好错一层——**算子语言翻译**:文献的 MAX 结构上更接近 `cross_max(day_ret, 21)`,而不是我们核心卡①本身;我们的 `cross_max(day_max(Ret), 30)` 反而同时叠了两层极值(先分钟→日,再日→月),这解释了为什么核心卡①单独的边际很弱(§2 已经用分解证明过)——**文献里"月度 MAX"只做一层极值,不做两层**,这是我们和标准定义的结构性差异,值得在 N 的笔记里点出来。
- follow-up 工作(Bali, Brown, Murray & Tang 等后续研究,经二次来源转述,未直接读到原文)用 **MAX(5)**:过去一个月里最大 5 个日收益的平均,而不是单一最大值,作为更稳健的版本——**算子语言翻译**:这正是我们判别实验里的 **T4** `cross_tail_mean_q75(day_max(Ret), 30)` 的设计依据:上尾均值而不是单点极值。[次级来源,未独立核实,见文末标注]

**(b) 控制波动率与特质偏度之后还剩多少**

- [L1] 的横截面回归在控制了规模、账面市值比、动量、短期反转、流动性、特质偏度之后,MAX 与下月收益的负向关系依然显著;并且把 MAX 加入回归后,**特质波动率(IVOL)异象的符号会反转**——这条直接对应我们规则 §3 里"5 个控制(含波动率)取残差"这一步:[L1] 的证据是"控制了波动率之后 MAX 效应依然存在",这支持 §6 的风险评估——`day_max(Ret)` 与波动控制相关,但不代表残差化之后就没有信息,只是需要先看 `corr` 表的 `vol` 列(§6 已经这么安排)。
- [L2](Lee, 2023-02)把特质风险分解成 diffusive / 正向跳跃(IPJVAR)/ 负向跳跃(INJVAR)三块,发现**只有正向跳跃方差被定价**(与下月收益显著负相关),diffusive 和负向跳跃都不稳定显著;并且做了一个"赛马"检验,**证明 [L1] 的 MAX 效应主要就是由正向特质跳跃驱动的**(把月份分成"有正跳跃"和"没有正跳跃"两组,MAX 效应集中在前一组)。[L2] 还发现**正向跳跃方差能预测未来偏度**(偏度在文献里被当成博彩型收益的代理)。
  **算子语言翻译**:这条是对 N 位想法 #3(`div(day_max(Ret), day_std(Ret))`、`day_es_ratio_hi(Ret)`)最直接的支持——[L2] 的"区分有无跳跃月份"等价于我们想做的"跳跃相对于波动尺度缩放后还剩不剩";而"跳跃预测未来偏度"这条提示:如果我们要单独验证通道 D(真 MAX/跳跃内容),比起只看 `day_max(Ret)` 的水平值,应该看它相对本地波动的尺度(我们规则里用残差去掉波动暴露,这与 [L2] 的赛马检验在精神上一致,但我们是线性+二次+三次残差,[L2] 是分组赛马,证据力度不同,要留意)。

**(c) 是否需要成交量加权**

- 没有搜到直接针对"跳跃 / MAX 型信号要不要按成交量加权才能交易"的文献(搜不到)。能找到的只是比较泛的"知情交易量与收益延续性"文献(如 Llorente/Michaely/Saar/Wang 关于放量下的收益延续、缩量下的收益反转),但这些研究不是针对 MAX/跳跃信号本身做的量权重检验,相关度弱,**不作为正式引用**,只作为"这个方向在金融文献里不是空白、但没有查到针对我们这个具体问题的工作"的说明。
  **算子语言翻译**:没有文献支持或反对 `day_topw_mean(Ret, Amt)`(成交最重 10% 分钟的平均收益)这个具体写法,它目前只是 N 位里一个"干净原子"候选,没有外部文献背书,这一点要诚实地告诉 PI。

**(来自 [L3] 的额外旁证,对应 §3 的"真 MAX 内容"追问)**:Amaya & Vasquez(2011-01)直接用高频(分钟级)数据,通过 realized variance 与 bipower variation 的差分出"跳跃"成分,计算**平均**跳跃大小(不是最大值),按十分位分组,发现**跳跃越负、后续收益越高**(跳跃越正、后续收益越低,方向与 [L1] 的"MAX 越高收益越低"一致),且对规模、账面市值比、前一周收益、波动率、偏度、峰度、流动性都做了双重排序和回归控制,结果稳健。
**算子语言翻译**:这是少数真正用**分钟级高频数据**做跳跃分解的工作,证实"跳跃方向与幅度"本身(不借助 MAX 的"只看最大值"简化)就足以定价;支持我们把 `day_max(Ret)` 换成更贴近"跳跃"定义的量(比如跳跃检测后的符号跳跃均值),但这需要比 `day_max` 更复杂的算子(我们目前的算子集里没有现成的 BV/RV 分解),暂时只能停在"记录这个方向"。

**中国市场证据**:[L4](Wan, 2018)在 A 股发现 IVOL 和 MAX 效应都存在,但**与美欧结果相反**——在中国 MAX 效应没能解释 IVOL 异象,反而 IVOL 异象"吞并"了 MAX 效应,作者认为这和中国市场更强的"套利限制"(institutional frictions)有关。
**算子语言翻译**:这条提醒我们——即便 `day_max(Ret)` 承重层的信息在美股文献里有清晰的"博彩偏好"解释,**不能直接假设同一套机制在 A 股成立**;A 股的制度摩擦(涨跌停、T+1、散户占比)可能是比"博彩偏好"更直接的来源——这正好呼应了我们自己从结构分解(§3)得出的"通道 A(封死)比通道 D(跳跃本身)更可能是真来源"的判断,是独立的外部支持。

另有二次来源提到一项 2016 年中国市场研究认为"价格波动范围和换手率能部分解释 MAX 效应,而特质波动率和特质偏度不能"(与偏度驱动的解释相矛盾),但我没能定位到可核实的完整期刊 / 卷期信息,按规则**不计入引用**,只记录"文献内部在中国市场上对 MAX 的解释机制有分歧"这一事实。

---

## Q2 —— 承重层 `cross_max(·, 30)`(通道 C:滚动最大值的角色)

**(a) 滚动极值类特征的标准做法与经济解释**

- [L5](George & Hwang, 2004)把"距 52 周高点的距离"(当前价 / 过去 52 周最高价)当作一个**状态变量**而不是一个动量分数:它比过去收益本身更能预测未来收益,解释了大部分动量利润,并且**这个预测力在长期不会像标准动量那样反转**。
  **算子语言翻译**:`cross_max(price, T)` 归一化后的比值(= 距滚动最高点的距离)是这类"状态变量"的标准实现;George & Hwang 的结果直接支持我们通道 C 的假设——**滚动最大值本身承载的是一个慢变状态,不是一个需要被解释成"动量"或"反转"的方向性信号**,这也是为什么它在"换仓成本"维度上天然占优(下面 (b))。

**(b) 把"低换手/低成本"和"携带的信息"分开**

- [L6](Novy-Marx & Velikov, 2016-12 / RFS 2016)系统比较了一批异象在不同成本缓释设计下的净收益:**单边月换手率低于 50% 的异象,在设计得当时大多仍能产生显著的净收益**;换手率更高的异象大多扛不住成本。他们发现**最有效的成本缓释手法是"买入/持有阈"(buy/hold spread)**——用比"进场"更宽松的"出场"阈值,人为把一个连续分数变成一个"黐性"(sticky)状态,从而**直接把换手率压下来,同时尽量不丢信息**。
  **算子语言翻译**:这条是对通道 C 假设(§3:"慢下来就少亏,而不是信息更多")最直接的外部支持——`cross_max(·, 30)` 的"只有新极值进来或旧极值出窗口才变"这个性质,结构上就是一种天然的"买入/持有阈"规则(进场门槛是创新高,出场门槛是跌出窗口,两者不对称、比逐日排名慢得多)。这给了我们一个**可操作的对照方向**:既然文献证明"人为做成黐性"本身就能提升净分数,那么判别实验 T1–T4 里,**即使 T4(上尾均值,没有"黐性")在"均值水平"上不输 T1/T2,它的净分数也可能因为没有这种天然黐性而更差**——这是我们原来的判别实验设计没有覆盖到的一个额外维度,值得向 PI 指出:四个 T 不仅要比"均值差",还该看换手率(§7 第 1 条已经在请求 turnover 分列,这条文献给了"为什么要看"的理由)。

**(c) 用上尾条件均值 / 高分位数替代单一最大值的稳健化**

- 没有找到金融文献里专门做"用上尾均值替代滚动最大值"的工作(搜不到针对因子构造场景的直接文献)。能找到的只是统计学里关于稳健尾部估计的工作,例如 [L7](Brazauskas & Serfling, 2000)比较了 Pareto 分布尾指数的不同估计量,发现**截尾均值(trimmed mean)比单点极值 / 极大似然估计更稳健、对上尾异常值不那么敏感**,但这是纯统计方法论文献,不是金融因子构造场景,相关度是间接的。
  **算子语言翻译**:[L7] 只能当作"上尾均值在统计上比单点极值更稳健"这个一般原理的旁证,不能当成"在因子构造里这样做更好"的金融证据;**T4 的设计(`cross_tail_mean_q75`)目前没有金融文献背书,是我们自己基于一般稳健统计原理做的延伸**,这一点要如实告诉 PI,不要包装成"文献证实"。

---

## Q3 —— 通道 A(封死 / 僵尸报价;也是 N 位主假设)

**(a) 封死状态的常用代理变量**

- 没有找到专门汇总"封死日代理变量清单"的综述;能确认的是 [L9] 直接从高频数据构造"收盘价等于涨跌停价"这个离散指示变量作为封板的代理,和我们的 `day_max(Ret) = 0`(当天没有一分钟动过)是**不同的代理口径**——[L9] 用的是"收盘价触及涨跌停",我们用的是"全天零变动",二者在**一字板**(开盘即封死到收盘)上重合,但在**先涨后封**或**盘中打开又封回**的情况下会不一致。
  **算子语言翻译**:这提示我们 `day_max(Ret) = 0` 可能是封死状态的一个**偏严格的子集**(只抓一字板,抓不到"盘中有过交易、尾盘才封死"的情况),如果要更贴近文献的"封板"定义,应该用 `LimitWidth` + 收盘价位置构造一个显式的触及涨跌停指示,而不是依赖"零变动"这个更严的条件——这是 N 位里"状态只当筛选键"那条可以更精确化的地方。

**(b) 封板日之后的收益形态,以及是否随板宽不同**

- [L9](Wan 等, 2015-03,高频数据 2000–2011)发现**涨跌停规则在中国市场体现的是"冷却效应"而不是"磁吸效应"**(与磁吸效应方向相反);并且**封板之后次日更可能是"延续"而不是"反转"**,这个延续概率在**跌停**上比涨停上更强(文献摘要给出的数字是跌停延续概率 75.9% vs 涨停延续概率 63.7%),次日开盘价沿原方向跳空的概率很高。
- [L8](Chen, Gao, He, Jiang, Xiong, 2017-11, NBER WP24014)用**账户级**数据发现:在触及 +10% 涨停当天买入的往往是大户,他们**次日卖出**,而他们在封板日的净买入量能预测更强的长期反转;论文专门用**ST 股票(涨跌停板宽收窄到 5%)** 做了一个近似自然实验式的对照,来识别涨跌停规则本身造成的扭曲效应。
- [L10](Qi, 2023-06-23, PLOS ONE)用创业板 2020 年把板宽从 10% 放宽到 20% 这个政策改革做检验,发现**涨跌停板导致价格发现延迟、波动溢出**,这个扭曲在**跌停**端更严重,**没有发现磁吸效应的证据**。
  **算子语言翻译**(三条放在一起看):三篇都用了不同的数据和方法,但在"次日延续 vs 磁吸"上基本一致指向**延续**而非磁吸,而且都强调了**板宽(LimitWidth)和涨跌方向的不对称性**——这直接支持 analysis.md §6 里"把 `LimitWidth` 当分段筛选键而不是加法项"的建议([L8] 用 ST 的窄板宽做对照、[L10] 按主板/创业板板宽对比,都是分段逻辑,不是相加逻辑);同时提示我们 N 位的筛选式应该**分涨跌停两个方向单独做**(目前 N 位 #2 里 `cs_last_high20(y, cross_max(day_zero_ratio(Ret), 15))` 是对称处理"零变动"的,没有区分涨停封死和跌停封死,而 [L9] 明确说这两个方向的延续强度不一样),这是一个具体、可执行的改进点。

**(c) 实证里通常剔除还是单独建仓**

- 没有找到专门讨论"封死名字在构造横截面因子时该剔除还是单独建仓"的文献(这几篇都是事件研究 / 价格发现角度,不是因子构造角度的文献)。这一点和 Q4(a) 的 [L12] 有交集(剔除小盘股的理由不完全是"封死",但处理思路相通),留给 Q4 讨论。

**另需说明**:二次来源里提到过"Wong, Liu, Zeng (China Economic Review, 2009)",称其用上交所交易数据发现涨停端价格发现延迟、跌停端价格反转——这个方向和 [L9]/[L10] 的"跌停延续更强"结论**正好相反**(一个说跌停反转,另两个说跌停延续更强)。我尝试直接核实这篇的标题、作者全名、卷期,但来源页面(orca.cardiff.ac.uk、uwe-repository.worktribe.com)都返回 403 无法访问,**没能独立核实**,所以按规则 `verified: false` 处理,不当成确定结论,只记录"文献之间在涨跌停不对称方向上确实存在分歧",这个分歧本身值得写进给 PI 的笔记。

---

## Q4 —— 通道 B(缺失日 / 上市年龄 / 构造卫生)

**(a) 新上市与停牌复牌名字的标准筛选做法**

- [L12](Liu, Stambaugh, Yuan, 2018-03 / JFE 2019)在构造中国市场的规模因子时,**标准做法是剔除按市值排名最小的 30% 的股票**,理由不是"统计噪声",而是一个具体的制度性机制:中国 IPO 配额紧张,小盘壳公司因为"壳价值"(被借壳上市的潜在价值)被系统性地定价过高,这部分不是正常的"规模效应",混进去会污染整个规模因子。
  **算子语言翻译**:这是一篇一线的、方法论对齐的证据,直接支持 N 位 #2 的筛选式思路——**用一个显式的筛选键(我们是 `cross_valid_count` 代理的上市年龄/存续天数,[L12] 是市值百分位)把"不干净"的一批名字按分位数挡在信号计算之外,而不是让它们留在排序里被当成普通样本**。但也要注意差异:[L12] 挡的是"壳价值导致的规模效应污染",我们要挡的是"缺失值导致乘积膨胀的数值伪影"——两者的污染机制不同,[L12] 不能直接证明我们的"挡法"对不对,只能证明"按分位数筛掉一批特殊名字,再在剩下的样本上定义因子"这个**构造流程**在中国市场的横截面资产定价研究里是被接受的标准做法,这给我们的筛选式一个"流程合法性"的支持,不是"效应本身"的支持。

**(b) 滚动窗口内缺失值在乘积型聚合里的正确处理;"缺失模式被挖成因子"这个方法论问题**

- **搜不到**。本轮 WebSearch 配额在搜到 [L12] 之后被用尽,我没能检索"滚动乘积 / 几何平均对缺失值的正确处理方式"以及"数据缺失模式本身被 GP/自动化方法挖成因子"这两个更偏方法论的问题。这两条如实记录为未检索到,不编造来源。如果后续轮次配额恢复,这是下一次该补的检索方向(关键词可以是 "missing data imputation rolling product factor"、"spurious factor data mining missingness pattern"、"survivorship bias panel construction")。

**(c) 停牌复牌后的收益形态**

- **搜不到**(同上,配额用尽前未检索到)。我知道"新股长期弱势"(IPO long-run underperformance)和"复牌后漂移"是两个独立的经典研究方向,但本轮没有检索到可核实的具体文献,**不写入引用列表**,留给下一轮或流水线请求补充。

---

## 参考文献(按 Q1–Q4 顺序,`verified` 字段按本次实际检索结果填写)

**[L1]** Bali, Turan G.; Cakici, Nusret; Whitelaw, Robert F. "Maxing Out: Stocks as Lotteries and the Cross-Section of Expected Returns." *Journal of Financial Economics*, Vol. 99, No. 2, pp. 427–446. 2011(刊期号 Vol.99 No.2;工作论文版本circulated 更早,但发表版本足够早于截止日)。来源:WebSearch 命中 Robert Whitelaw 的 NYU Stern 简历页与 NYU 档案条目,多处独立转述一致给出卷/期/页码。链接:https://www.stern.nyu.edu/faculty/static/cv/cv_rw2_20240703.pdf (另见 https://archive.nyu.edu/handle/2451/27871)。`verified: true`

**[L2]** Lee, Suzanne S. "The Role of Idiosyncratic Jumps in Stock Markets." 工作论文,Georgia Institute of Technology, Scheller College of Business. 2023-02。来源:直接下载 PDF 并用 `pdftotext` 读取全文摘要与导言。链接:https://www.scheller.gatech.edu/directory/research/finance/lee/pdf/idiosyncraticlee_2023_feb.pdf 。`verified: true`

**[L3]** Amaya, Diego; Vasquez, Aurelio. "Explaining Stock Returns with Intraday Jumps." 工作论文(EFMA 2011 Braga 年会论文)。2011-01-14。来源:直接下载 PDF 并用 `pdftotext` 读取全文摘要与导言。链接:https://www.efmaefm.org/0efmameetings/EFMA%20ANNUAL%20MEETINGS/2011-Braga/papers/0307.pdf 。`verified: true`

**[L4]** Wan, Xiaoyuan. "Is the Idiosyncratic Volatility Anomaly Driven by the MAX or MIN Effect? Evidence from the Chinese Stock Market." *International Review of Economics & Finance*, Vol. 53(C), pp. 1–15. 2018(月份未在页面给出)。来源:WebFetch 读取 IDEAS/RePEc 条目页。链接:https://ideas.repec.org/a/eee/reveco/v53y2018icp1-15.html 。`verified: true`

**[L5]** George, Thomas J.; Hwang, Chuan-Yang. "The 52-Week High and Momentum Investing." *Journal of Finance*, Vol. 59, No. 5, pp. 2145–2176. 2004。来源:WebSearch 命中上海财经大学学术通讯页与 CXO Advisory 摘要,两处独立转述给出一致的刊名/卷/期/页码。链接:https://www.cxoadvisory.com/1284/technical-trading/the-52-week-high-as-a-momentum-indicator-for-individual-stocks/ 。`verified: true`

**[L6]** Novy-Marx, Robert; Velikov, Mihail. "A Taxonomy of Anomalies and Their Trading Costs." NBER Working Paper No. 20721. 2014-12(发表版本:*Review of Financial Studies*, Vol. 29, No. 1, pp. 104–147, 2016)。来源:WebFetch 直接读取 NBER 页面。链接:https://www.nber.org/papers/w20721 。`verified: true`

**[L7]** Brazauskas, Vytaras; Serfling, Robert. "Robust and Efficient Estimation of the Tail Index of a Single-Parameter Pareto Distribution." *North American Actuarial Journal*. 2000。来源:WebSearch 结果摘要给出标题/作者/年份及一句话结论(统计方法论文献,未完整读取正文,与金融因子构造的相关性是间接的,仅作一般原理旁证)。链接:https://sites.uwm.edu/vytaras/files/2016/04/2000_NAAJ-zdngkl.pdf 。`verified: true`(仅指"在搜索结果里看到了标题与结论",正文未读)

**[L8]** Chen, Ting; Gao, Zhenyu; He, Jibao; Jiang, Wenxi; Xiong, Wei. "Daily Price Limits and Destructive Market Behavior." NBER Working Paper No. 24014. 2017-11(发表版本:*Journal of Econometrics*, 2019)。来源:WebFetch 直接读取 NBER 页面。链接:https://www.nber.org/papers/w24014 。`verified: true`

**[L9]** Wan, Yu-Lei; Xie, Wen-Jie; Gu, Gao-Feng; Jiang, Zhi-Qiang; Chen, Wei; Xiong, Xiong; Zhang, Wei; Zhou, Wei-Xing. "Statistical Properties and Pre-hit Dynamics of Price Limit Hits in the Chinese Stock Markets." arXiv:1503.03548(同一研究亦发表于 *PLOS ONE*, 2015)。首版提交日期 2015-03-12。来源:WebFetch 直接读取 arXiv 摘要页。链接:https://arxiv.org/abs/1503.03548 。`verified: true`

**[L10]** Qi, Bao. "Effectiveness of Price Limits: Evidence from China's ChiNext Market." *PLOS ONE*, Vol. 18, No. 6, e0287548. 发表于 2023-06-23(早于 2023-08-08 的硬截止)。来源:WebFetch 直接读取 PMC 文章页(含 received/accepted 日期)。链接:https://pmc.ncbi.nlm.nih.gov/articles/PMC10289463/ 。`verified: true`

**[L11]**(未独立核实,仅记录分歧)"Wong, Liu, Zeng",据二次来源转述发表于 *China Economic Review*,2009,用上交所交易数据发现涨停端价格发现延迟、跌停端价格反转。来源:WebSearch 结果的转述性摘要;尝试通过 orca.cardiff.ac.uk/49184 与 uwe-repository.worktribe.com/output/998540 两个页面核实原文,均返回 HTTP 403,无法独立确认标题全文、作者全名或卷期。链接(不可访问):https://orca.cardiff.ac.uk/49184 。`verified: false`

**[L12]** Liu, Jianan; Stambaugh, Robert F.; Yuan, Yu. "Size and Value in China." NBER Working Paper No. 24458,发布于 2018-03(修订于 2018-12);发表版本:*Journal of Financial Economics*, Vol. 134, 2019, DOI 10.1016/j.jfineco.2019.03.008。来源:WebFetch 直接读取 NBER 页面。链接:https://www.nber.org/papers/w24458 。`verified: true`

---

## 给 PI 的一句话小结

四条通道里,**通道 A(封死)和通道 C(滚动最大值的黐性)都有相当扎实的外部文献支持**(分别是 [L8][L9][L10] 和 [L5][L6]),且都给出了**具体、可执行**的结构建议:封死要按涨/跌方向分开处理、要用 `LimitWidth` 分段而不是相加;滚动最大值的"黐性"本身可能就是净分数的一部分来源,判别实验除了看均值差也该看换手率。**通道 D(跳跃本身)的文献支持其实也存在**([L1][L2][L3]),但指向的是"跳跃相对波动的尺度"而不是跳跃的原始水平,这进一步支持把 N 位 #3 的"相对波动的跳跃"而不是核心卡①本身当作检验真 MAX 内容的正确位置。**通道 B(缺失值数值伪影)这一侧,文献只能部分支持**:[L12] 支持"用分位数筛选键挡掉异常名字"这个构造流程,但没有文献直接讨论"乘积对缺失值的处理"或"缺失模式被挖成因子"这两个更底层的方法论问题——这两条本轮确实搜不到,不是没有查,是配额用尽前没查到,需要下一轮补。中国市场的证据总体上提示:**不要直接搬美股"博彩偏好"的解释给 A 股的 MAX 效应**([L4]),A 股更可能是涨跌停这类制度摩擦(通道 A)而不是投资者偏好(通道 D)在起作用,这和我们自己从结构分解得出的判断方向一致。
