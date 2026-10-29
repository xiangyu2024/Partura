# 文献:种子 807,B 组,第 3 轮

对准 `r3/analysis.md` §5 的四个题目(L1–L4)。只用 2023-08-08 之前发表的论文 / 工作论文(arXiv、SSRN、工作论文系列以首版日期为准)。
每条处理写明出处编号,对应末尾的参考文献表(含 `verified` 字段:true = 本次确实在搜索结果或抓取的页面上看到了该文献的标题 / 作者 / 年份 / 期刊等信息)。
搜不到、或日期拿不准的,按要求如实写"搜不到"/"不使用",不编造。

---

## L1 —— 对准核心 ①(`day_var(Ret)` 的软幂平均)

**(a) 已实现半方差 / 带符号拆分,作为横截面收益预测变量**

- 做法:把日内(或分钟)收益按正负拆成两支,只用负向(或正向)的那部分分钟收益计算已实现方差,再分别聚合,而不是对全部收益一起取方差。
  Barndorff-Nielsen、Kinnebrock、Shephard 最早提出这个"已实现半方差"(realized up-/down-semivariance)分解 [1]。
  Bollerslev、Li、Zhao 把它用在个股横截面上:对每只股票分别算 realized 上行方差("好波动")与下行方差("坏波动"),
  按"好波动减坏波动"(归一化后)把股票分组,后续组合收益差异经济上显著、统计上显著,控制其他已知特征后依然成立 [2]。
  **翻译成算子语言**:在 `day_var(Ret)` 前面插一步按分钟收益符号筛选(只保留负收益分钟 / 只保留正收益分钟)再求方差,
  得到 `day_var_down(Ret)` 与 `day_var_up(Ret)` 两支;候选方向是"好减坏"的归一化差,而不是像现在这样只看未拆分的水平。
- 做法(跳跃版,直接在中国市场做过):先用 bipower variation 把已实现方差拆成"连续部分"与"跳跃部分",跳跃部分再按正负拆开,
  取"正跳跃方差 − 负跳跃方差"的符号差(而不是跳跃方差的绝对水平)。对 A 股 2007–2013 年高频数据,按市值×账面市值比分 5×5=25 组后做 Fama–MacBeth 检验,
  符号差越正、后续组合收益越高(5% 显著),负向跳跃到达率系数显著为负(10% 显著)[4]。同一方法论(连续 vs. 跳跃的分解聚合层写法,但对象是指数预测不是个股横截面,只能借聚合层的写法,不能当横截面证据)也出现在另一篇 A 股高频研究里 [5]。
  Feunou、Jahan-Parvar、Okou 把同一拆分思路用在方差风险溢价上(期权隐含方差减已实现方差,再按上行/下行拆开),
  发现下行部分贡献了溢价的主要部分(一个说法是 80% 以上),"上行减下行"的缺口本身对未来收益有短中期预测力 [3]。
  三篇一致的信息:**"拆分再比较符号/差值"比"只看水平"更可能有横截面信息**,这与我们已经证明"软的量级比硬极值好"是互补而非冲突的维度。

**(b) 把日内方差相对自身历史标准化**

- 没有找到直接检验"已实现方差 ÷ 自身滚动历史均值(或变异系数、z 分)"作为横截面收益预测变量的论文。
  比较接近的是特质波动率存在均值回复这条线(讨论波动率预测误差的来源,而不是收益可预测性)[9],**不能当作证据使用**。
  **如实记录:关于(b)的直接证据,搜不到。**

**(c) 按上市年限 / 板块 / 流动性 / 规模分组后结论怎么变**

- 搜索没有找到专门针对"已实现方差 / 已实现半方差的横截面定价效力,按上市年限或板块分组"的论文(A 股或其他市场都没有)。
  **如实记录:搜不到。**

**(d) 日内方差在一天之内的分布 / 集中度,有没有被当横截面特征用过**

- 确认了"波动率本身在一天之内有稳定的周期形状(常被描述为 U 形)"这件事本身是成立的、有经典文献支持:
  Andersen、Bollerslev 用马克/美元汇率五分钟数据证明日内波动有很强的周期性,必须先低通滤波去掉这层周期,才能看清跨日的长记忆 [6]。
  但这篇讲的是**波动率动态本身**(外汇市场),不是把"日内方差集中在哪几分钟"当作**个股横截面收益特征**来用。
  搜索没有找到后一种用法的论文。**如实记录:关于把日内集中度当横截面特征的证据,搜不到。**

---

## L2 —— 对准核心 ③ 与 R 的 A 组(`day_distinct_ratio(Volume)`)

**(a) 零成交分钟 / 零收益天数占比,如何被构造成截面变量**

- Lesmond、Ogden、Trzcinka 用"收益恰好为零"这一现象本身去反推隐含交易成本(LOT 模型):零收益发生的频率越高,隐含成本估计越大;
  这是把一个近乎二值的日度现象,通过一个结构化模型映射成连续的成本估计量,而不是直接拿比例进横截面 [7]。
- Liu 构造的 LM12 更接近我们的场景:过去 252 个交易日里"零成交量天数"的计数,再加一个按换手率倒数缩放的微调项,
  最后乘以 252/实际交易日数做窗口长度标准化;即 **"计数 + 换手率倒数调整 + 窗口标准化"的复合量,不是裸比例** [8]。
- Bekaert、Harvey、Lundblad 在新兴市场上确实直接用了"零日收益比例,按月聚合"这种最朴素的构造法当流动性代理,
  而且验证它比换手率更能预测收益(换手率不能预测、零收益比例能)[10]。
  **翻译成算子语言**:三篇指向两种可行做法——
  (i) 最朴素:`cross_mean(zero_return_or_zero_volume_flag, 月度窗口)`,Bekaert 等证明这个简单形式本身就有效,不需要先验地加奇怪的非线性变换;
  (ii) 更接近 Liu 的复合写法:把零成交天数的计数,按 `1/换手率` 做一次缩放再进入截面(而不是对 `day_distinct_ratio` 直接做 `inv(cs_demean(·))` 这种奇异变换)。
  这两条都没有用到 (N-c) 那种除零极点,是"干净聚合"的参考方向。

**(b) 价格离散性 / 最小报价单位 / 整手格点造成的失真,当特征而不是噪声**

- 搜索到一条可能相关的线索(关于 tick size 与 lot size 的权衡,在名义价格与流动性之间产生 U 形关系的工作论文),
  但抓取工具无法访问到可核实作者与确切发表时间的版本(服务器拒绝访问,搜索结果里的作者信息也不一致)。
  **按规则不使用这条,不列入参考文献。**
  搜索也没有找到"一天访问过多少个不同价格档位""成交量落在多少个不同数值上"这类度量被专门构造成个股特征的论文。
  **如实记录:(b) 搜不到可用的、能核实日期的文献。**

**(c) 控制掉成交额水平与波动水平之后还有没有独立定价能力**

- Amihud 的 ILLIQ(日收益绝对值 / 当日成交额,滚动平均)本身在横截面上对预期收益有正向且高度显著的解释力,
  而且这类检验的标准做法就是要控制住成交额(规模)水平作为对照 [11]——这与我们奖励已经控制流动性水平是同一逻辑,
  可以当作"这条控制是标准动作"的佐证,但它**没有**直接回答"薄交易旗标在控制流动性水平后是否还有独立定价力"这个问题。
  搜索没有找到专门回答这一点的论文。**如实记录:(c) 的直接证据搜不到,只有旁证。**

**(d) 把"滚动回归斜率"当个股特征的一般做法,以及 1/var_x 主导问题**

- Kyle 的 lambda 定义为"价格变化对带符号订单流做回归"的斜率,Amihud 的论文把常见的估计方法归纳为 Glosten–Harris 法和 Hasbrouck 法两种 [11][12]。
  但搜索没有找到专门讨论"回归斜率的横截面分布被 1/var_x(解释变量方差)主导时应如何处理"(标准化、取对数、改用 t 值而不是原始斜率)这个具体问题的文献。
  **如实记录:(d) 关于 1/var_x 主导问题的直接讨论,搜不到;只找到背景性的方法归纳 [11][12],不能当作这一点的证据。**

---

## L3 —— 对准核心 ②(`pow_2(cross_mean(day_wmean(Ret,Ret),5))`)

**(a) 收益符号的游程 / 连续同向天数 / 符号自相关**

- Da、Gurun、Warachka 的"信息离散度"(information discreteness)正是一种计数版的持续性度量:
  在形成期窗口内,数"每日收益与窗口累计收益同号的交易日占比",而不是看游程长度本身。
  他们发现:同样的形成期累计收益,"持续小幅同向"(continuous information)比"少数几天大幅跳动"(discrete information)产生的动量更强、反转更慢
  (论文摘要给出的数字级差相当大,连续信息组的动量显著高于离散信息组,且前者在长期不反转而后者反转)[13]。
  **翻译成算子语言**:对 `day_wmean(Ret,Ret)` 的形成窗口,额外算一个"每日值与窗口累计值同号的天数占比",
  作为与"5 日带符号平均"互补的第二维度——一个测"持续了多稳",一个测"持续得多强",两者分开喂给 GP 而不是只喂乘积。
- **反方向的证据,必须让 PI 看到**:Kudryavtsev 在日频个股收益上发现相反的效应——连续同号多天之后,下一天的异常收益显著反转
  (赌徒谬误),而且效应在小盘、高波动股票上更强、连续正向序列后的反转比连续负向序列后更明显 [14]。
  这与核心②"先按符号 5 日平均、再折叠,得分 +1.71"的方向似乎相反,但两者统计对象不同:
  Kudryavtsev 测的是"streak 之后下一天"的反转,核心②测的是"过去 5 天窗口内的带符号平均水平"本身对横截面收益的解释力,
  不构成直接矛盾,但这条文献证据是反向的,PI 决定外围方向时应该知道。

**(b) 日内漂移 / 订单失衡的多日持续性,半衰期有多长**

- Lee、Liu、Roll、Subrahmanyam 直接在台湾股票上做过:净订单失衡存在日度自相关(机构与散户的持续程度不同,大机构持续性强、大散户弱),
  但由此产生的总体价格压力基本不超过一个交易日就消散,文中读成"事实上的做市很有效"[15]。
  Chordia、Roll、Subrahmanyam 在美股(NYSE)市场层面上也发现类似结论:大幅负失衡 + 大幅负收益之后会反转,
  但这种序列相关性不能预测下一交易日的市场收益,即效应同样不超过一天 [16]。
  两篇都没有在 A 股上估计过,搜索也没有找到 A 股上直接估计这类持续期 / 半衰期的工作。
  **如实记录:(b) 的 A 股反例搜不到——与 r2/lit.md 的 L3 结论一致(只有台湾"不超过一天"这一侧的证据)。**

**(c) 这类持续性信号按什么条件分组才显著**

- Medhat、Schmeling 的"短期动量"研究直接回答了这个问题:按上月收益与换手率做双重分组,
  **低换手率的股票里,上月收益后续反转;高换手率的股票里,上月收益后续延续**("短期动量"),
  这个短期动量和经典中期动量一样强、一样持久,交易成本后依然成立,在规模最大、流动性最好、分析师覆盖最多的股票里反而最强 [17]。
  **翻译成算子语言**:把核心②的持续性因子按换手率(或流动性水平)分组后再分别评分——高换手组预期更可能是"持续得多强"占优,
  低换手组预期更可能是"持续了几天"本身就要反着读(接近反转)。这是本题里唯一一条给出明确、可操作分组方向的文献。

**(d) 事件对齐窗口(自上一次方向反转以来,而不是固定 5 天)**

- 搜索没有找到直接构造"自上一次收益符号反转以来的天数"作为窗口定义、并测试其横截面收益预测力的论文。
  **如实记录:(d) 搜不到。**

---

## L4 —— 对准 §1.6 的价格水平方向冲突

**(a) 名义股价本身作为预测变量,控制市值之后还剩什么**

- Birru、Wang 的工作论文(2016-03 circulated 版本标题为《The Nominal Price Premium》,我抓取到了这份工作论文首页,
  确认作者、机构与摘要)提出:裸价格排序对未来收益没有稳健的预测力,是因为"低价⇒高预期收益"的机械折现率效应,
  与"投资者对低价股系统性过度乐观(名义价格幻觉)"的错误定价效应方向相反、相互抵消;
  作者构造了一个"拟合价格"(用基本面变量回归出的理论价位)与实际价格的偏离,用这个偏离而不是裸价格去排序,
  得到月度 85(等权 88)个基点的四因子 alpha,效应在难套利股票和高情绪期更强 [18]。
  同一研究后续以《Nominal Price Illusion》为题发表于《Journal of Financial Economics》,
  用期权隐含偏度、分拆事件等做法进一步证实"投资者高估低价股的上涨空间"这一机制 [19]。
  **翻译成算子语言**:不要直接用 `day_last(Open)` / `day_quantile(Open)` 的裸价格水平当信号(文献说这条路本身没有稳健预测力),
  要么构造"实际价格相对基本面拟合价格的偏离",要么像现在这样先承认它是 `LogFloatShares`(≈ −log 价格)的近亲,
  用控制变量或正交化处理,而不是把裸价格直接当作独立信号源。

**(b) A 股上低价 / 高价效应的方向与时期依赖**

- 搜索没有找到专门针对 A 股名义价格效应方向是否随时间翻转的论文。
  （有美股证据显示"低价效应"在 1970 年代之前更明显、1980 年后转为"高价效应"更明显,但这是美股证据且来源工作论文的确切发表时间未能核实,不列入参考文献。）
  **如实记录:(b) 搜不到 A 股专门证据。**

**(c) 名义价格与彩票偏好 / 散户持股比例的交互**

- Kumar 把"彩票型股票"定义为价格低于 5 美元、历史上有高波动与极端正收益的股票,
  发现收入更低、教育程度更低的投资者更偏好买入这类股票,在失业率更高的地区、经济下行期买入更多,
  且这类"赌徒型"投资者事后平均跑输大盘 2–3 个百分点 [20]。
  **翻译成算子语言**:名义价格水平本身可以当作"彩票偏好暴露"的一个代理维度,与波动率、极端收益做交互项使用
  (而不是单独一支信号),这是把"价格水平"从"折现率代理"重新定位成"行为偏好代理"的一条具体路径。

**(d) 文献对"只在部分截面上定义的信号"的处理惯例与警告**

- 搜索没有找到专门讨论"把最低 10%~20% 温莎化 / 压到均值再做截面回归"这类部分样本信号的处理惯例与警告的文献。
  **如实记录:(d) 搜不到。这正是 `cs_mask_top_replace_mean_neg`(烂部件 #4)最需要外部判据的地方,
  但本轮文献检索没有覆盖到,PI / 结构解剖员需要知道这一条是空的,不能当作"文献支持这种稳健化手法"的依据。**

---

## 参考文献(按首次出现编号;verified = 本次搜索/抓取确实看到了该文献的标题与关键信息)

1. Barndorff-Nielsen, O. E., Kinnebrock, S., & Shephard, N. "Measuring downside risk: realised semivariance."
   工作论文首发于 Oxford/CREATES 系列,2008;收录于 *Volatility and Time Series Econometrics* (T. Bollerslev, J. Russell, M. Watson 编,
   Engle 纪念文集),Oxford University Press, 2010。
   链接:https://www.nuff.ox.ac.uk/economics/papers/2008/w2/downside.pdf ;https://economics.web.ox.ac.uk/node/1465231
   verified: true

2. Bollerslev, T., Li, S. Z., & Zhao, B. "Good Volatility, Bad Volatility, and the Cross Section of Stock Returns."
   *Journal of Financial and Quantitative Analysis*, 2020,55(3): 751–781。
   链接:https://ideas.repec.org/a/cup/jfinqa/v55y2020i3p751-781_2.html ;https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/good-volatility-bad-volatility-and-the-cross-section-of-stock-returns/B9203F87AB93D8DEAD51CB692587350E
   verified: true

3. Feunou, B., Jahan-Parvar, M. R., & Okou, C. "Downside Variance Risk Premium."
   *Journal of Financial Econometrics*, 2018,16(3): 341–383(始于 2015 年 Federal Reserve FEDS 工作论文)。
   链接:https://www.federalreserve.gov/econres/feds/downside-variance-risk-premium.htm ;https://econbiz.de/Record/downside-variance-risk-premium-feunou-bruno/10011987780
   verified: true

4. Chao, Y., Liu, X., & Guo, S. "Sign realized jump risk and the cross-section of stock returns: Evidence from China's stock market."
   *PLoS ONE*, 2017-08-03,12(8): e0181990。
   链接:https://pmc.ncbi.nlm.nih.gov/articles/PMC5542663/
   verified: true(直接抓取到全文页面,核对了方法、分组方式与方向)

5. Fang, N., Jiang, W., & Luo, R. "Realized Semivariances and the Variation of Signed Jumps in China's Stock Market."
   *Emerging Markets Finance and Trade*, 2017,53(3): 563–586。
   链接:https://ideas.repec.org/a/mes/emfitr/v53y2017i3p563-586.html
   verified: true(搜索结果给出了完整的刊名、卷期、页码)

6. Andersen, T. G., & Bollerslev, T. "Intraday periodicity and volatility persistence in financial markets."
   *Journal of Empirical Finance*, 1997,4(2–3): 115–158。
   链接:https://ideas.repec.org:443/a/eee/empfin/v4y1997i2-3p115-158.html ;https://scholars.duke.edu/publication/761297
   verified: true

7. Lesmond, D. A., Ogden, J. P., & Trzcinka, C. A. "A New Estimate of Transaction Costs."
   *Review of Financial Studies*, 1999,12(5): 1113–1141。
   链接:https://www.bauer.uh.edu/rsusmel/phd/lot_1999RFS.pdf ;https://ideas.repec.org/a/oup/rfinst/v12y1999i5p1113-41.html
   verified: true

8. Liu, W. "A liquidity-augmented capital asset pricing model."
   *Journal of Financial Economics*, 2006,82(3): 631–671。
   链接:https://rpc.cfainstitute.org/-/media/documents/article/cfa-digest/2007/dig-v37-n2-4603-pdf.pdf ;https://www.casact.org/abstract/liquidity-augmented-capital-asset-pricing-model
   verified: true

9. Bozhkov, S., Lee, H., & Sivarajah, U. (关于特质波动率均值回复与估计量偏差的研究,*Annals of Operations Research*, 2018)。
   链接:https://bura.brunel.ac.uk/bitstream/2438/16140/3/FullText.pdf
   verified: true(仅作为"搜不到直接证据"时的旁证提及,正文未把它当作(b)的证据使用)

10. Bekaert, G., Harvey, C. R., & Lundblad, C. "Liquidity and Expected Returns: Lessons from Emerging Markets."
    *Review of Financial Studies*, 2007(NBER Working Paper No. 11413,2005 年首发)。
    链接:https://www.nber.org/papers/w11413 ;https://business.columbia.edu/sites/default/files-efs/imce-uploads/gbekaert/lessons.pdf
    verified: true

11. Amihud, Y. "Illiquidity and stock returns: cross-section and time-series effects."
    *Journal of Financial Markets*, 2002,5(1): 31–56。
    链接:https://www.cis.upenn.edu/~mkearns/finread/amihud.pdf ;https://www.casact.org/abstract/illiquidity-and-stock-returns-cross-section-and-time-series-effects
    verified: true

12. Kyle, A. S. "Continuous Auctions and Insider Trading." *Econometrica*, 1985,53(6): 1315–1335
    (本次搜索未直接确认原文细节,只确认了后续文献对其 lambda 定义与 Glosten-Harris / Hasbrouck 估计法的归纳,见 Amihud 2002 的描述)。
    verified: false(经典文献本身的细节本次没有直接核实,只核实了二手归纳)

13. Da, Z., Gurun, U. G., & Warachka, M. "Frog in the Pan: Continuous Information and Momentum."
    *Review of Financial Studies*, 2014,27(7): 2171–2218。DOI: 10.1093/rfs/hhu003
    链接:https://www3.nd.edu/~zda/Frog.pdf ;https://ideas.repec.org/a/oup/rfinst/v27y2014i7p2171-2218..html
    verified: true

14. Kudryavtsev, A. "The Effect of Preceding Sequences on Stock Returns."
    *European Financial and Accounting Journal*, 2017,12(4): 83–96。DOI: 10.18267/j.efaj.202
    链接:https://efaj.actavia.vse.cz/artkey/efa-201704-0006_the-effect-of-preceding-sequences-on-stock-returns.php
    verified: true

15. Lee, Y.-T., Liu, Y.-J., Roll, R., & Subrahmanyam, A. "Order Imbalances and Market Efficiency: Evidence from the Taiwan Stock Exchange."
    *Journal of Financial and Quantitative Analysis*, 2004,39(2): 327–341。
    链接:https://ideas.repec.org/a/cup/jfinqa/v39y2004i02p327-341_00.html
    verified: true

16. Chordia, T., Roll, R., & Subrahmanyam, A. "Order imbalance, liquidity, and market returns."
    *Journal of Financial Economics*, 2002,65(1): 111–130。
    链接:https://ideas.repec.org/a/eee/jfinec/v65y2002i1p111-130.html
    verified: true

17. Medhat, M., & Schmeling, M. "Short-Term Momentum."
    *Review of Financial Studies*, 2022,35(3): 1480–1526。DOI: 10.1093/rfs/hhab055(CEPR DP15857 工作论文版)。
    链接:https://repec.cepr.org/repec/cpr/ceprdp/DP15857.pdf
    verified: true

18. Birru, J., & Wang, B. "The Nominal Price Premium." 工作论文,2016-03。
    链接:https://www.ivey.uwo.ca/media/3777565/birru.pdf
    verified: true(本次直接抓取并读取了论文首页原文:标题、作者、日期、摘要全部核对)

19. Birru, J., & Wang, B. "Nominal Price Illusion."
    *Journal of Financial Economics*, 2016,119(3): 578–598(与条目 18 为同一研究的后续发表版本,题目不同)。
    链接:https://rpc.cfainstitute.org/research/cfa-digest/2016/11/nominal-price-illusion-digest-summary
    verified: true(CFA Institute Digest 摘要页给出了完整的二手归纳;发表版的卷期页码来自搜索结果中的机构页面,未直接抓取原文核对,risk 略高于条目 18)

20. Kumar, A. "Who Gambles in the Stock Market?"
    *Journal of Finance*, 2009,64(4): 1889–1933。DOI: 10.1111/j.1540-6261.2009.01483.x
    链接:https://ideas.repec.org/a/bla/jfinan/v64y2009i4p1889-1933.html
    verified: true

---

## 没有用上的线索(如实记录,供 PI / 检查核对)

- 关于 tick size / lot size 权衡造成名义价格与流动性 U 形关系的工作论文(可能作者为 Mao Ye 及合作者,AEA 2022/2023 会议程序里出现过):
  抓取被源站拒绝(HTTP 403),搜索结果里作者信息也不一致,**无法核实,不使用**。
  [https://acfr.aut.ac.nz/__data/assets/pdf_file/0006/578751/Mao-Ye-The-Tradeoff-between-Discrete-Pricing-and-Discrete-Quantities.pdf](https://acfr.aut.ac.nz/__data/assets/pdf_file/0006/578751/Mao-Ye-The-Tradeoff-between-Discrete-Pricing-and-Discrete-Quantities.pdf)
- "Does realized skewness predict the cross-section of Chinese stock returns?"(*Finance Research Letters*, 2023,卷 58 Part B):
  搜索结果显示的是 2023 年 part B,无法确认是否在 2023-08-08 之前正式发表(线上优先发表日期未能核实),**不使用**。
- 美股"低价效应 1970 年代前更强、高价效应 1980 年后更强"的 Vlerick 工作论文:确切发表时间未能核实,**不使用,只在 L4(b) 正文里提及其存在但不列为参考文献**。
