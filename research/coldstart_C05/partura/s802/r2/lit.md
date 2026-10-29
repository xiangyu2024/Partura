# 文献:种子 802,B 组,第 2 轮

对准 `analysis.md` §5 的四个题目(L5–L8;接着第 1 轮的 L1–L4,不重复)。核心 A = `cross_mean(day_mean(in_logchg(Volume, 60)), 20)`(全库第一,+1.6680);
核心 B = `day_durbin_watson(High)` 及其凸聚合版本 `pow_2(pow_2_5(day_durbin_watson(High)))`(+1.4497);核心 C = `cross_quantile_q25(LogFloatShares, 241)`(不推荐,仅对照)。
工具:WebSearch / WebFetch(本轮已加载)。**只用 2023-08-08 之前发表/提交的文献**;arXiv 按 v1 提交日期,期刊论文用 Crossref / IDEAS 核对发表(online)日期 ——
本轮搜到一篇相关度很高但发表日期晚于截止日的文献(§L8 第 2 条),已按规则弃用,记录在"未列入上表"一节,不计入证据。
下面每条处理方式后的 `[S#]` 对应文末出处表;出处表里 `verified: true` 表示这次搜索结果或抓取的页面上确实看到了该文献的标题/作者/年份/场所,不是凭记忆写的。

---

## L5(对准核心 B / N 灵感 1:月度信号该用均值还是极值聚合)

搜索关键词:MAX effect, lottery-like stocks, idiosyncratic volatility puzzle, extreme daily returns, jump risk cross-section, power mean / soft-max aggregation。

**能翻译成算子语言的处理方式:**

1. **近一个月的"最大值"而不是"均值"聚合,是资产定价文献里有直接证据、而且方向明确(负)的做法。** Bali, Cakici, Whitelaw (2011) 定义 MAX = 过去一个月日收益率的最大值(稳健版本取最高 5 天的均值),发现 MAX 与未来收益显著负相关,且**在控制了 Ang–Hodrick–Xing–Zhang (2006) 的特质波动率(IVOL)之后依然成立,甚至逆转了 IVOL 与收益之间原本的负向关系的符号**[S1][S2]。
   → 翻译:核心 B 目前只验证过"凸变换叠加后再均值"(`cross_mean(pow_2(pow_2_5(x)), 20)` 这条路线);文献里本来就有一个更直接的算子——`cross_max(x, 20)` 或 `cross_quantile_q90/q95(x, 20)`(近 1 个月最大值 / 高分位),而不是先做凸变换再取均值。
   4.2 第 6 条已经列了 `cross_max(day_durbin_watson(High), 20)`,**这条文献把它的优先级从"值得一试"提升到"应该是本轮核心 B 最先验证的一个变体"**——如果它和凸聚合版本(+1.4497)表现相当甚至更好,说明此前一直在用"软最大值"的昂贵写法逼近一个文献里本来就有的直接构造。
2. **方向是有条件的:如果极端值能归因到可辨识的公司事件,效应会消失。** 检索结果转述 Harvey(2017,EFMA)的后续研究:当月内最高单日收益由业绩公告驱动时,MAX 效应不显著[未独立核实原文全文,仅为二级转述]。本环境没有公告字段,**这是一条明确的局限**:若 `cross_max(day_durbin_watson(High), 20)` 测试段表现不稳定,这条文献给出一个可能的混淆来源(极端粗糙日是否恰好是消息日),但当前算子词表做不了这个区分。
3. **"只留跳跃/极值成分、丢弃其余"在波动率—跳跃文献里也有先例,但多数在市场或组合层面,不是个股日频算子层面。** 一篇用中国市场 5 分钟高频数据的研究把已实现波动拆成跳跃与连续两部分,发现跳跃成分在 Fama–French 风格的投资组合层面**单独定价**[S3]。这支持"从日内统计量里单独抽取极值成分"的方向,但证据粒度和"把 DW(High) 取凸聚合"这个具体构造不匹配,只能当弱的方向性支持。
4. **缺口:"幂平均 / soft-max 聚合"本身(即先凸变换再均值,和直接取分位数/最大值之间的连续谱)在资产定价文献里没有搜到直接比较。** 搜到的"幂平均"材料全部来自风险聚合/运营风险建模领域,和横截面因子构造不是同一个问题[证据很弱,未列入出处表]。这正好是 4.2 第 5/6 条本来就要做的检验——文献没有替我们省掉这一步。

## L6(对准核心 A:日内成交量分布作为个股的持久特征)

搜索关键词:intraday volume profile persistence, deseasonalizing intraday volume, log volume change versus volume share, turnover controls。

**能翻译成算子语言的处理方式:**

1. **日内成交量的"形态"存在跨时间段的非平稳性,"U 形"本身在样本期内会漂移。** 对道琼斯蓝筹股 2003–2014 年的研究发现,经典的 U 形**在 2008 年后发生显著变化**(开盘后下降更快、尾盘上冲更陡),作者把这个变化归因于 2008 年美国 SEC 的卖空新规[S5]。
   → 翻译:核心 A 的 `day_mean(in_logchg(Volume, 60))` 如果隐含一个"典型日内形状不随时间变"的假设,这个假设**在国外市场不是时间不变的**——如果 R/N 要检验核心 A 的稳定性,这条文献给了一个"应该分段看年份"的外部先验,类似 3.2 节收盘占比族的 2018-08-20 断点,但这次是外部给的理由,不是我们自己从数据里发现的。
2. **缺口(本轮最大的一个):没有搜到把"个股日内形状"当作一个跨月持久、可以直接用作横截面因子的特征来处理的学术论文。** 搜到的两篇执行类文献——一篇用 Bayesian 方法把"当日剩余成交量预测"拆成总量子模型 + 日内曲线(u-curve)子模型 + 收盘竞价子模型[S6];一篇把成交量拆成"确定性日内形状 + 随突发事件变化的动态部分",用 ARMA/SETAR 建模动态部分[检索结果转述,未独立核对原文,未列入出处表]——都关心**今天怎么执行/预测当天还剩多少量**,不关心**这只股票的形状是不是一个能跨股票排序的持久特征**。
   这个缺口和第 1 轮 L2/L4 的缺口是同一类:核心 A 在这个构造粒度上,目前为止在我查到的范围内**仍然没有直接先例**。
3. **"先剥掉典型日内形状、再看残差"仍是能找到的最接近的处理方式,但来源还是第 1 轮已引用过的 Hawkes 聚集性论文和 Admati–Pfleiderer 理论**(第 1 轮 S8、S1,这里不重复编号,只提醒:这两条对核心 A 同样适用,本轮没有新证据加强或推翻它们)。
4. **换手率水平是标配控制变量,但文献控制的通常是"换手率的水平",不是"换手率的日内形状"。** 一篇研究近年交易活跃度趋势的论文发现换手率系统性上升,且机构持仓占比高的股票换手率上升更多[S9]——提示如果核心 A 想做"流动性旁路检验"(4.2 第 12 条),按机构持仓/成交额分组可能比简单分位数分组更贴近文献对"换手率驱动因素"的理解,但本环境没有机构持仓字段,**这条做不了,只记远期方向**。

## L7(对准 4.2 第 9–10 条与 N 灵感 4:排除式筛选 vs 线性合成)

搜索关键词:screening versus linear combination, exclusion filters, double sorting versus conditional sort, trimming the extreme decile, does the screen carry alpha or remove noise。

**能翻译成算子语言的处理方式:**

1. **"排除极端一截再排序"在动量文献里有一个直接的、做过对照实验的先例,结论是正面的。** 一篇研究台湾市场的论文把"绝对强度极端"的股票**从赢家组合和输家组合里剔除**(不是线性加进打分),报告剔除后动量收益显著提升、中期窗口更稳健、且不再出现动量崩溃[S10]。
   这是本次检索范围内找到的**唯一一篇直接做了"排除式筛选 vs 不筛选"对照实验的文献**,方向支持 4.2 第 9/10 条:`cs_last_high10` 这类筛子不是瞎猜的操作,文献里有正面证据。但它的筛选变量是"自身收益的极端程度"(用于稳健化同一个因子),不是"用一个不同的 y 去筛 x"(我们的 `cs_last_high10(cross_quantile_q25(LogFloatShares, 241), day_max(Volume))` 是后一种),**结构不完全对应,只能当方向性支持**。
2. **"筛选是去噪还是本身带 alpha"这个问题,在特质波动率文献里恰好有两篇结论相反的论文,正好对应 4.2 第 10 条想分开的两种解释。** Han & Lesmond (2011) 发现:把"价格钉住 / 买卖价差"造成的微观结构偏差**修正掉**之后,特质波动率对收益的预测能力**基本消失**——原来的"因子"主要是噪声[S11]。Chen, Jiang, Xu & Yao (2020) 则发现:把最容易受微观结构噪声污染的股票(微型股、低价股、强短期反转股)**直接从样本里剔除**之后,特质波动率异象**依然强劲且普遍**,结论是"微观结构噪声在削弱这个异象,不是在制造它"[S12]。
   **这两篇结论相反**,说明"筛选之后分数变高/变低"本身不能单独告诉我们筛选变量是不是噪声。翻译给 4.2 第 10 条:如果换一个 x 之后 `cs_last_high10` 把 y 从 +0.56 抬到 +1.0 以上,**不能直接下结论"筛子携带自己的 alpha"**,还需要像这两篇论文一样,检查被筛掉的那一截本身的收益特征(是普遍跑输,还是只在特定 x 配对下才跑输)。
3. **缺口:双重排序对切点比例(5%/10%/20%)敏感性的具体数字,搜到的论文发表日期晚于截止日,按规则弃用。** 搜到一篇专门做"因子模型对切点选择的敏感性"的论文,但其期刊发表日期为 2023-12,**晚于 2023-08-08,按规则不采用**,这里只记录"双重排序对切点敏感"是文献里常被提及的方向,不附具体文献[未列入出处表]。
4. **用一个独立的质量/控制变量做条件排序(而不是筛选掉一截),是和"筛选"、"线性合成"并列的第三条路。** AQR 的"Size Matters, if You Control Your Junk"发现:标准规模效应近年看起来弱,是因为没有控制质量(QMJ);用质量做条件控制之后,小盘和大盘内部的"优质股"与"垃圾股"都能看到显著价差[S13]。
   翻译:这是"条件双重排序"而不是"排除式筛选"的例子——它控制的是全样本范围内的一个连续变量,不是剔除某个极端分位。如果 N 灵感 4 想把筛子系统化成通用处理方式,这篇文献提示**还有一条没写进任务词表的路**:条件双重排序(按核心 A / DW(High) 分组后再看另一个变量的排序能力,`cs_bucket_zscore` 已经是这个方向),而不只是"筛掉一截"。

## L8(对准核心 C / 1.4 节:名义股价水平值不值得在库里占 6 个位置)

搜索关键词:nominal stock price level, low-price effect, price illusion, minimum tick size, retail / lottery preference, China A-share low price anomaly, non-monotonic price effect。

**能翻译成算子语言的处理方式:**

1. **名义股价效应的标准检验是"按价格分十分位看单调性",美股证据报告的是接近单调,不是驼峰形。** 检索结果转述三篇相关论文:从最低价十分位(P1)到最高价十分位(P10),收益几乎单调上升[二级转述,未直接核对原文,未列入出处表]。
   翻译:4.1 节担心的"驼峰形(最便宜的一截反而差)"**在我查到的范围内没有美股的直接证据支持**,反而是相反方向(越贵越好,近似单调)。这对 1.4 节"非单调"的猜想是一个不利信号,但来源是二级转述,只记作"目前没搜到支持驼峰形的文献,也没搜到反对的直接原文"。
2. **缺口 + 一次规则弃用:中国市场的"低价股收益更高"证据存在,但唯一搜到的专门论文发表日期晚于截止日。** 搜到 Bing Zhang, "Betting against low nominal prices: Evidence from China"(*International Review of Economics & Finance*),用 Crossref 核实其线上/印刷发表日期为**2023 年 11 月**,晚于 2023-08-08,**按规则不采用**,不计入出处表、不作为证据。这是本轮唯一一次"搜到相关度很高的文献,但卡在截止日之外"的情况。
3. **机制解释:名义价格效应更可能来自投资者对"便宜"的信念偏差(价格锚定了偏度预期),不是单纯偏好低价本身。** Birru & Wang (2016) 的核心发现:投资者在形成偏度预期时**过度依赖价格**本身(期权隐含的风险中性偏度在拆股后系统性上升,但拆股后**实际实现**的偏度反而下降)——作者把这归为**信念错误**,不是纯粹的偏度偏好[S15]。
   翻译:如果 PI 想检验"核心 C 是不是股价水平的代理",文献给的机制提示是**投资者的信念/预期渠道**,不是"低价股本身有更高尾部风险溢价"——任何想绕开这条代理的处理(比如 4.2 第 11 条的 `cs_bucket_zscore`),重点应该是**切断"价格数字本身"这个变量**,而不是控制换手率或波动率(机制不在流动性,在价格数字本身)。
4. **名义价格是一个跨国、持续数十年的"锚",靠拆股主动维持,不会随时间自然衰减——对 1.4 节"2015 之后是否衰减"的猜想是反面证据。** Bae, Bhattacharya, Kang & Rhee (2019) 用 38 个国家数据证明名义价格锚定是全球现象,公司会用拆股主动维持这个锚(用 1999 年欧元启动做自然实验:欧元换算后股价骤降越多的公司,换算后拆股越少)[S16]。
   翻译:名义价格效应不太可能"自己衰减",因为上市公司的拆股行为本身就在**主动维持**这个锚。如果 2018–2023 这段时间核心 C 的效应真的在变弱,原因更可能是 A 股特有的东西(注册制、涨跌停带宽变化、创业板/科创板扩容改变了"低价股"的构成),而不是"锚定现象本身在全球范围内消退"。**如果库里要去掉核心 C 相关的 head,理由应该停留在"已知、冗余、边际价值低"(1.4 节已有的理由),不应该再加"文献预测它会衰减"这一条——文献不支持这个理由。**
5. **缺口:没有搜到 2023-08-08 之前发表、专门在 A 股做"名义股价效应、且做了市值/流通市值严格中性化"的论文。** 搜到的中国相关证据(低波动率效应、32 个异象的检验)都不专门针对价格水平本身[S17,仅作背景]。这意味着 1.4 节"已知的廉价异象"这个判断,在 A 股语境下其实缺乏我能独立核实的直接文献支撑——它更可能是从美股文献(Birru-Wang、Weld et al.)类比过来的,不是 A 股本身的实证结论。**建议 PI 把这句话写得更谨慎:不是"文献证实了这是已知异象",而是"美股文献证实了机制存在,A 股是否同样成立在这次检索范围内没有直接证据"。**

---

## 出处(全部核对时间,均在 2023-08-08 之前)

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|---|
| S1 | Maxing Out: Stocks as Lotteries and the Cross-Section of Expected Returns | Turan G. Bali, Nusret Cakici, Robert F. Whitelaw | 2011(Journal of Financial Economics 99(2), 427–446) | 期刊:Journal of Financial Economics | https://ideas.repec.org/a/eee/jfinec/v99y2011i2p427-446.html | true |
| S2 | The Cross-Section of Volatility and Expected Returns | Andrew Ang, Robert J. Hodrick, Yuhang Xing, Xiaoyan Zhang | 2004-10(NBER Working Paper 10852;正式发表 Journal of Finance 61(1), 259–299, 2006) | NBER / 期刊:Journal of Finance | https://www.nber.org/papers/w10852 | true |
| S3 | Sign realized jump risk and the cross-section of stock returns: Evidence from China's stock market | 作者名单未在搜索结果中完整给出 | 2017(PLoS ONE) | 期刊:PLoS ONE | https://pmc.ncbi.nlm.nih.gov/articles/PMC5542663/ | true |
| S5 | Intraday Seasonalities and Nonstationarity of Trading Volume in Financial Markets: Individual and Cross-Sectional Features | Michelle B. Graczyk, Silvio M. D. Queirós | 2018-10(arXiv v1 提交于 2018-10-22) | arXiv | https://arxiv.org/abs/1810.12099 | true |
| S6 | Quintet Volume Projection | Vladimir Markov, Olga Vilenskaia, Vlad Rashkovich | 2019-04(arXiv v1 提交于 2019-04-02) | arXiv | https://arxiv.org/abs/1904.01412 | true |
| S9 | Recent Trends in Trading Activity and Market Quality | Tarun Chordia, Richard Roll, Avanidhar Subrahmanyam | 2010-11(SSRN 工作论文;正式发表 Journal of Financial Economics 101(2), 243–263, 2011-08) | SSRN / 期刊:Journal of Financial Economics | https://authors.library.caltech.edu/95155/2/SSRN-id1700191.pdf | true |
| S10 | Enhancing momentum profits in the Taiwan Stock Market: The role of extreme absolute strength | Chaonan Lin, Chuanxin Xia, Nien-Tzu Yang, Sheng-Yung Yang | 2019/2020(Pacific-Basin Finance Journal 59;DOI 前缀 2019,期刊卷标注 2020) | 期刊:Pacific-Basin Finance Journal | https://ideas.repec.org/a/eee/pacfin/v59y2020ics0927538x19303993.html | true |
| S11 | Liquidity Biases and the Pricing of Cross-sectional Idiosyncratic Volatility | Yufeng Han, David Lesmond | 2011(Review of Financial Studies 24(5), 1590–1629) | 期刊:Review of Financial Studies | https://ideas.repec.org/a/oup/rfinst/v24y2011i5p1590-1629.html | true |
| S12 | Dissecting the idiosyncratic volatility anomaly | Linda H. Chen, George J. Jiang, Danielle D. Xu, Tong Yao | 2020-12(Journal of Empirical Finance 59, 193–209) | 期刊:Journal of Empirical Finance | https://ideas.repec.org/a/eee/empfin/v59y2020icp193-209.html | true |
| S13 | Size Matters, if You Control Your Junk | Clifford Asness, Andrea Frazzini, Ronen Israel, Tobias Moskowitz, Lasse Heje Pedersen | 2015-01(工作论文初稿,SSRN;正式发表 Journal of Financial Economics 129(3), 479–509, 2018) | SSRN / 期刊:Journal of Financial Economics | https://jacobslevycenter.wharton.upenn.edu/wp-content/uploads/2015/05/Size-Matters-if-You-Control-Your-Junk.pdf | true |
| S15 | Nominal price illusion | Justin Birru, Baolian Wang | 2012-12(工作论文;正式发表 Journal of Financial Economics 119(3), 578–598, 2016) | SSRN / Ohio State Dice Center / 期刊:Journal of Financial Economics | https://ideas.repec.org/a/eee/jfinec/v119y2016i3p578-598.html | true |
| S16 | Nominal Stock Price Anchors: A Global Phenomenon? | Kee-Hong Bae, Utpal Bhattacharya, Jisok Kang, S. Ghon Rhee | 2019-05(HKUST IEMS 工作论文,修订于 2019-05;正式发表 Journal of Financial Markets 44, 31–41, 2019) | 工作论文(HKUST IEMS)/ 期刊:Journal of Financial Markets | https://iems.ust.hk/wp64 | true |
| S17 | Anomalies in the China A-share market(32 个异象的检验,仅作背景,不支持任何具体处理方式) | Martijn Jansen, Laurens Swinkels, Weili Zhou | 2021(Pacific-Basin Finance Journal) | 期刊:Pacific-Basin Finance Journal | https://pure.eur.nl/en/publications/anomalies-in-the-china-a-share-market/ | true |

未列入上表、曾经搜索但没有搜到可用文献,或搜到但因日期不合规被弃用的方向(诚实记录,不编造):
- "幂平均 / soft-max 聚合在月度因子构造里优于均值"的资产定价文献——搜不到(L5 第 4 条)。
- "个股日内成交量形态是跨月持久的横截面因子特征"的直接先例——搜不到(L6 第 2 条,和第 1 轮 L2/L4 的缺口是同一个)。
- "双重排序对切点比例的敏感性分析"的具体数字——搜到了相关论文,但期刊发表日期为 2023-12,晚于截止日,**按规则弃用**,不计入出处表(L7 第 3 条)。
- A 股语境下"名义股价效应、严格做市值中性化"的专门论文——搜到了唯一一篇(Bing Zhang, 2023),但 Crossref 核实其线上发表日期为 2023-11,**晚于 2023-08-08,按规则弃用**,不计入出处表、不作为证据(L8 第 2、5 条)。
- "低价股收益驼峰形(最便宜一截反而差)"的直接原始文献——搜不到,只搜到一条未独立核实的二级转述(方向还是相反的,接近单调)(L8 第 1 条)。

---

## 给 PI 的一句话总结

本轮最硬的两条:**(a) L5 第 1 条——MAX 效应给了核心 B 凸聚合路线一个更直接、更便宜的对照组(`cross_max` / `cross_quantile_q90`),应该优先于继续加深凸变换的幂次去验证**;
**(b) L7 第 2 条——特质波动率文献里"修正噪声后效应消失"(Han–Lesmond)和"剔除噪声股票后效应更强"(Chen–Jiang–Xu–Yao)两篇结论相反,说明 4.2 第 10 条"筛子抬分是不是自带 alpha"不能只看分数涨跌,还要看被筛掉那一截本身的收益特征**。

L8 的教训偏向警示:**驼峰形猜想没搜到支持;唯一一篇专门针对 A 股低价效应的论文因为发表日期(2023-11)晚于截止日被弃用——核心 C"是已知异象"这个判断目前主要靠美股文献类比,不是 A 股直接证据**,PI 写任务文件时这句话的确定性要降一级;
同一条文献(Bae et al. 2019)也说明"等它自己衰减"不是弃用核心 C 相关 head 的合法理由,拆股行为在主动维持这个锚。

L6 没有新证据加强或推翻第 1 轮的结论:**核心 A 在"个股日内形态当持久特征"这个构造粒度上,目前为止在我查到的范围内仍然没有直接先例**——这是支持"核心 A 可能是真发现"的一个诚实信号,但也意味着 PI 不能拿文献给核心 A 的外围写法找背书,只能继续靠 4.1 节列的几条实证路径(条件化分组、不稳定度、与第二形状交互)自己验证。

本轮一个流程性提醒:**日期核对从"看搜索结果里的年份"升级成了"用 Crossref/IDEAS 核对月份"**——L8 第 2 条如果只看"2023"这个年份会被误当合规文献用进任务,幸亏核对到月份(2023-11)才发现晚于截止日。建议检查环节(Haiku)复核日期时,优先复核"年份是 2023 但没写月份"的条目。
