# 文献:种子 802,B 组,第 1 轮

对准 `analysis.md` §5 的四个题目(L1–L4,都对准核心 A = `sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))`,
以及核心 B = `day_mean(neg(in_delta(Volume, 60)))`)。工具:WebSearch / WebFetch(本轮已加载)。
**只用 2023-08-08 之前发表/提交的文献**;arXiv / SSRN 按首版(v1)日期。拿不准日期的条目已标注并不计入处理方式的证据。
搜索是这次会话里实际跑的,下面每条处理方式后面的 `[S#]` 对应文末出处表;出处表里 `verified: true` 表示这次搜索结果或抓取的页面里确实看到了该文献(标题/作者/年份/场所至少一项被直接看到),不是凭记忆写的。

---

## L1:核心 A 的「价格钉在同一档位连续多久」——封板代理,还是呆滞价格流动性代理?

搜索关键词:price limits, magnet effect, limit-hit dynamics, China A-share; zero-return illiquidity measure, stale prices。

**能翻译成算子语言的处理方式:**

1. **按涨跌停带宽(5% / 10% / 20%)做分组,而不是全市场一刀切。** `day_flat_run_max(Vwap)` 的意义(封板 vs 呆滞)在 ST(5%)、主板(10%)、创业板/科创板(20%)下完全不同,带宽越宽,「钉住一天」需要的价格纹理越细,统计意义不同。文献做法是把 ST 股票单独作为一类自然实验(比较同一只股票戴帽 / 摘帽前后的行为差异),而不是把 `LimitWidth` 简单当一个连续回归变量揉进同一个因子 [S3][S4]。→ 建议 N/E 的处理:按 `BoardCode` / `LimitWidth` **分组**(`cs_bucket_rank` 一类算子)比把 `LimitWidth` 当共同回归变量更贴近文献的检验设计。
2. **看「临近涨跌停前的动态演化」而不是静态的一天内统计。** [S2][S3] 两篇都是跟踪涨跌停命中前若干分钟/若干天的成交强度、价格变异的**时间演化路径**,用 logit 模型预测是否会命中,而不是把「钉住了多久」直接当横截面因子。这提示:`day_flat_run_max` 这类静态日内统计,文献里更常见的伴随处理是**滚动窗口内的变化趋势**(例如钉住比例最近 N 天是否在上升),而不是单日取值本身——这与 §1.5 机械发现（`ts_decay_linear` 把并列块重新拆开才拿分）互相印证。
3. **区分「一字板」与「开板」、持续性与反转。** [S4] 用账户级数据证明涨停当天是大户主动买入、次日卖出获利,机制是"目的性钉价"而非单纯缺乏流动性;其结果是**涨停后价格延续、长期才反转**([S2] 摘要也报告同样的「延续而非反转」)。这与 1.1 节「S 的方向是做多斜率持续为负的那端(价格钉住 + 成交量变平滑)」在性质上吻合:**延续性是封板类机制的标志,反转是呆滞流动性代理的标志**——如果 R/E 的变体想检验这一点,可以直接测「钉住事件后 N 日收益延续 vs 反转」作为诊断,而不是只看 rho_known。
4. **把「零收益/价格不变」当流动性代理时,标准做法是按月(或固定窗口)取「零收益天数占比」,而不是原始计数**,再与 Amihud 价格冲击、换手率等常规流动性指标**并列检验、互相对照**,而不是直接拿来当独立因子 [S5][S6][S7]。这支持我们已经做的「与 `cross_mean(day_std(Amt),30)` 正交化」方向是对的;但也说明:如果想论证 `day_flat_run_max(Vwap)` 不是流动性代理,文献里标配的检验是**同时报告它和 Amihud/zero-return 的相关性**,而不仅是 `rho_known`(一个成交额波动代理)。
5. **缺口(搜不到):** 没有搜到任何文献把「一天内连续同一均价的分钟数占比」本身构造成一个分钟级横截面因子——现有「零收益」文献全部是**日级**（一天的收益是否为零),不是**分钟级**(一天里价格钉住多久)。核心 A 的这个叶子在我查到的范围内**没有直接先例**,它更接近 1 和 2 两类文献的交集,但构造粒度是新的。PI 下任务时不要把这当「文献已证实」,只能当「文献给出了怎么分组/怎么检验延续性反转」的方法论借鉴。

---

## L2:核心 A 的另一半——`day_durbin_watson(Volume)`,日内成交量的「粗糙度」

搜索关键词:intraday volume autocorrelation, U-shape, order-flow burstiness, trade clustering, Durbin-Watson as feature。

**能翻译成算子语言的处理方式:**

1. **先剥掉日内 U 形基准,再谈「粗糙度」/聚集性。** 开盘尾盘成交放量是**结构性的**,理论基础是 Admati–Pfleiderer (1988) 的策略性交易模型:知情交易者和有弹性的流动性交易者都倾向把单子往开盘/收盘集中,U 形是博弈均衡的结果,不是噪声 [S1]。研究中国某只股票高频委托数据的 Hawkes 模型论文把委托到达过程显式拆成「确定性日内形状(U 形基线)+ 自激发的聚集成分」两层,发现聚集主要来自**自激发**而不是不同单类之间的交叉激发 [S8]。
   → 翻译:`day_durbin_watson(Volume)` 现在是对**原始**分钟成交量序列算一阶差分平方和/总平方和,**没有先减掉典型的日内形状**。文献的标准处理是先对 Volume 做「去季节化」(减去跨股票或跨日平均的分钟形状曲线)再算差分统计,这样算出来的才是「超出结构性 U 形之外的粗糙度」,而不是被开盘尾盘两个大峰值主导的伪粗糙度。这是一个具体可做的 N:`day_durbin_watson(Volume - <日内典型形状>)`,或者更简单地只在剔除开盘/收盘若干分钟后的子窗口上算 DW。
2. **用对数变化或百分比变化而不是原始水平做差分,是标配的「尺度无关化」。** Heston–Korajczyk–Sadka (2010) 对半小时成交量用的是**对数变化**或**百分比变化**,不是水平值或水平差分 [S9]。这与 DW 分母是 Σv²(未去均值,但是**同一天自身尺度**)在精神上一致——都是让统计量不被"今天到底有多少成交量"这个水平因素支配,而是看"相对自身的粗糙程度"。这支持 1.1 节「`Volume→Amt` 基本不动」的读法:只要是「同口径、未取对数的量」,DW 这个比值统计量本身已经做了尺度无关化,所以换哪个量纲都差不多——但从未试过的是**换成对数变化后的 DW**,这是文献里更标准的做法,值得一试。
3. **成交量的自相关在「周期性」上有强结构,且能持续约 40 个交易日。** [S9] 发现半小时成交量变化的自相关在滞后 13 的整数倍(即每天固定的时间段)上是**正**的,其余滞后基本是负的,且这个周期性模式能显著延续到 520 个半小时(约 40 个交易日)。这给了核心 A 里 `ts_regbeta` 窗口 50(→ 100 更好)一个外部校准:**50 天本身不算长**,文献里类似的"成交量结构记忆"能延续 40 个交易日,100 天窗口更贴近这个记忆长度的量级,支持 R4/R5(50→100、decay 40→80/120)的方向,但文献给出的不是「越长越好」而是「在约 40 天处有一个自然的记忆边界」,窗口再往上(比如 200)未必继续受益,这是个可以明确检验的预测。
4. **按"知情交易更可能发生在中等单量"分桶,而不是把全部成交量一视同仁。** Stealth trading 假说(Barclay & Warner 1993):92% 的累计价格变化发生在**中等规模**的交易上,知情交易者既不用会暴露信息的大单,也不用太慢建仓的小单 [S10]。这对"成交量粗糙度"给出了一个更精细的处理方向:如果数据里能拿到分钟级的**笔数**和**均单量**,`day_durbin_watson` 可以只在"中等单量"那部分成交量上算,而不是全部 Volume——但本环境的 6 个日频叶子和现有算子словарь里没有单量分桶的字段,这条目前**做不了**,只记录为 N 的远期方向。
5. **缺口(搜不到):** 没有搜到任何文献直接用 Durbin–Watson 统计量(或其等价形式,一阶差分平方和/平方和)作为成交量横截面因子;也没有搜到把它当作"成交量自相关"显式构造的先例。1、2、3 条都是"相邻但不是同一个统计量"的证据,不能当作 DW(Volume) 本身已被验证。

---

## L3:核心 A 机械发现(1.2 节)——「幅度是噪声,符号与持续性才是信息」,回归斜率怎样被稳健化

搜索关键词:rolling beta shrinkage, errors-in-variables, t-statistic vs coefficient, nonsynchronous trading beta bias, time series momentum sign。

**能翻译成算子语言的处理方式:**

1. **向横截面(或分组)均值收缩,权重由估计误差决定(Vasicek 1973)。** 把个股的原始 `ts_regbeta` 向当天全市场(或同行业/同板块)的 regbeta 均值收缩,权重是「自身估计误差的方差」的反函数——误差越大,越往均值拉 [S11]。这是对 1.2 节「裸 beta train +0.45 / valid −0.14(幅度是噪声)」的一个**不同于 sigmoid 硬截断**的稳健化路线:不是把幅度直接压扁成近似二值,而是按估计不确定性做连续的收缩。值得在 R/N 里和「sigmoid + decay」路线并列一试,比较哪个在 valid 上更稳。
2. **当背后数据本身有「价格钉住/稀疏交易」造成的序列相关时,标准修正是用「前导 + 同期 + 滞后」的加总回归系数,而不是单纯的同期斜率(Scholes & Williams 1977;Dimson 1979)。** 这两篇是贝塔估计量的经典文献:稀疏/非同步交易会让原始 OLS 贝塔**向零偏** [S12];Dimson 的修正是把因变量对自变量的当期、若干期领先、若干期滞后**都回归进去再加总系数** [S13]。**这条直接对准核心 A 本身**——`day_flat_run_max(Vwap)` 这个自变量本身就是"价格钉住/稀疏变化"的度量,如果钉住期越长,`ts_regbeta` 的同期配对本来就更容易因为稀疏而产生偏误。可做的检验:把 `ts_regbeta(x, y, 50)` 换成「`y` 对 `x` 的若干阶前导和滞后值回归系数之和」,如果核心 A 的分数因此系统性改变,说明 1.2 节的"幅度是噪声"部分来自这个经典的稀疏交易偏误,而不只是 sigmoid 的饱和效应。
3. **两阶段回归里,用估计出来的斜率做第二阶段回归时,标准做法是修正第二阶段的标准误(即改变 t 值的尺度),而不是改点估计本身(Shanken 1992)。** [S14] 的 errors-in-variables 修正说明:当"斜率"是从第一阶段估计出来的噪声变量时,它在第二阶段的统计显著性(t 值)比看起来的更不可靠,需要专门修正。这从另一个角度支持"用 t 值而不是系数本身"这个 PI 想测的方向是**有文献基础的直觉**(把估计误差的尺度信息并入到用来排序的那个量里),但 Shanken 修正的对象是标准误/t 值本身,不是说"direct 把 t 值当信号"必然更好——这条只能当**方法论类比**,不是"t 值版因子"的直接先例。
4. **时间序列动量文献里,核心信号用的是"过去收益的符号",不是过去收益的幅度(Moskowitz, Ooi & Pedersen 2012)。** 这是"符号/持续性里有 alpha,幅度是噪声"这个假设在资产定价文献里**最直接的先例**:TSMOM 的多空信号就是 `sign(过去 12 个月超额收益)`,完全丢弃幅度 [S15]。这给 1.2 节的发现和 N1 的"用 t 值 / R² / 符号占比替掉 beta+sigmoid"这条路线一个明确的外部支持:**丢弃幅度、只保留方向和持续性**在另一类资产定价信号里是已经被验证过的处理范式,值得在 N 里系统地做(不止试 t 值,也试"过去 N 天斜率符号为正的占比"这类离散化统计量)。
5. **缺口:** 没有搜到任何文献直接做过"把滚动回归系数换成 t 值作为横截面因子,并且在样本外更稳"的直接对照实验;3、4 条都是相邻证据,不是直接先例。R8(`ts_reg_tvalue` 替换 beta)仍然是一次真正的新检验,不是"文献已经告诉我们答案"。

---

## L4:核心 B / N3——日内成交量的「时间斜率」(放量/缩量形态)

搜索关键词:intraday volume slope/trend, opening/closing volume share, informed trading, Admati-Pfleiderer。

**能翻译成算子语言的处理方式:**

1. **U 形是知情交易者与有策略的流动性交易者共同选择交易时点的均衡结果,不是外生噪声(Admati & Pfleiderer 1988)。** [S1] 的理论含义是:`in_delta(Volume, 60)` 这种"一小时尺度的成交量斜率"在不同时段的含义不对称——早盘的放量和尾盘的放量背后的交易者构成不同。处理上应该**按时段分段**而不是对全天取一个单一的 `day_mean`:比如分别算"早盘到午盘"和"午盘到尾盘"两段斜率,而不是把一天揉成一个数。
2. **按成交笔的规模分桶(小单/大单),能把"知情"和"噪音"交易者的贡献分开(Heston-Korajczyk-Sadka 2010 的小单 vs 大单切分;Barclay & Warner 1993 的中单占优假说)。** [S9] 把半小时成交量切成 <1000 股与 ≥1000 股两组分别回归;[S10] 的"中等单量承载大部分价格变化"假说进一步提示,如果能拿到分钟级的单均量或笔数,"量斜率"因子应该优先在中等单量那部分上构造。本环境没有单量分桶字段,这条暂时做不了,记作远期方向(与 L2 第 4 条相同的缺口)。
3. **把"量的时间形态"拆成"确定性日内曲线 + 残差聚集成分"两层,只用残差层(Hawkes 自激发文献)。** [S8] 的方法学直接可用:先对 `Volume` 减去(或除以)一个典型的日内形状基准(例如全市场当天同一分钟桶的平均成交量占比),再对**残差**做 `in_delta` 差分取均值。这样 `day_mean(in_delta(Volume,60))` 就不会被"每天固定存在的开盘冲量、尾盘冲量"这个结构性分量主导,而是真正捕捉"今天的放量/缩量形态相对典型形态有多反常"。这是对核心 B 最直接可操作的一条新处理,而且**和核心 A 需要的"剥 U 形基准"是同一个预处理**,两个核心可以共用。
4. **"收盘集合竞价成交占比"作为知情交易/分歧代理,证据初步、未定论。** 查到一篇 2021 年的 AEA 会议初稿,把"集合竞价成交量 / 当日总成交量"的比值当作投资者分歧的代理,报告该比值越高未来收益越高,但作者自己把这个结果定位为**分歧**而非知情交易,而且是会议初稿、未见期刊发表版本 [S16]。**这条证据弱,不建议直接当机制先验使用**,只记录作为"开盘/尾盘占比"这个方向在文献里确实有人做过的一个弱先例。
5. **缺口:** 没有搜到任何文献直接构造"分钟级成交量在小时尺度上的差分、再按日取均值"这个具体统计量;也没有搜到中国 A 股市场专门针对"日内放量缩量形态"的横截面因子研究(搜到的中国相关论文多是知情交易的 PIN/U 形验证性研究,不是因子构造研究)。

---

## 出处(全部核对时间,均在 2023-08-08 之前)

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|---|
| S1 | A Theory of Intraday Patterns: Volume and Price Variability | Anat R. Admati, Paul Pfleiderer | 1988(Review of Financial Studies 创刊卷 Vol.1 No.1) | 期刊:Review of Financial Studies | https://www.gsb.stanford.edu/faculty-research/publications/theory-intraday-patterns-volume-price-variability | true |
| S2 | Statistical Properties and Pre-hit Dynamics of Price Limit Hits in the Chinese Stock Markets | Yu-Lei Wan, Wen-Jie Xie, Gao-Feng Gu, Zhi-Qiang Jiang, Wei Chen, Xiong Xiong, Wei Zhang, Wei-Xing Zhou | 2015-03(arXiv v1 提交于 2015-03-12;正式发表 PLoS ONE 10(2):e0120312, 2015) | arXiv / PLoS ONE | https://arxiv.org/abs/1503.03548 | true |
| S3 | The cooling-off effect of price limits in the Chinese stock markets | Yu-Lei Wan, Gang-Jin Wang, Zhi-Qiang Jiang, Wen-Jie Xie, Wei-Xing Zhou | 2018-03(arXiv v1 提交于 2018-03-26) | arXiv | https://arxiv.org/abs/1803.09422 | true |
| S4 | Daily price limits and destructive market behavior | Ting Chen, Zhenyu Gao, Jibao He, Wenxi Jiang, Wei Xiong | 2019-01(期刊版;NBER Working Paper 24014 为 2017-11 的早期版本;VoxChina 科普稿《Daily Price Limits and the Magnet Effect》2017-10-25) | 期刊:Journal of Econometrics 208(1), 249–264 | https://ideas.repec.org/a/eee/econom/v208y2019i1p249-264.html ;科普稿 https://voxchina.org/show-3-49.html | true |
| S5 | A New Estimate of Transaction Costs | David A. Lesmond, Joseph P. Ogden, Charles A. Trzcinka | 1999(Review of Financial Studies 12(5)) | 期刊:Review of Financial Studies | https://ideas.repec.org/a/oup/rfinst/v12y1999i5p1113-41.html | true |
| S6 | Liquidity and Expected Returns: Lessons from Emerging Markets | Geert Bekaert, Campbell R. Harvey, Christian Lundblad | 2007(Review of Financial Studies 20(5)) | 期刊:Review of Financial Studies | （本次搜索结果中以摘要/二级引用形式出现,未直接打开原文页面确认链接;标题/作者/年份已在搜索结果文本中看到) | true |
| S7 | Do emerging stock markets offer an illiquidity premium for local or global investors? | Hilal Anwar Butt, Riza Demirer, Mobeen Sadaqat, Tahir Suleman | 2022(年份确认,月份未在搜索结果中给出;The Quarterly Review of Economics and Finance, 86, 502–515) | 期刊:The Quarterly Review of Economics and Finance | https://ideas.repec.org/a/eee/quaeco/v86y2022icp502-515.html | true |
| S8 | Modeling aggressive market order placements with Hawkes factor models | （论文研究对象含一只中国股票的高频委托数据;搜索结果未给出完整作者名单) | 2018-11(arXiv v1 提交于 2018-11-20;正式发表 PLOS ONE, 2020) | arXiv / PLOS ONE | https://arxiv.org/abs/1811.08076 | true |
| S9 | Intraday Patterns in the Cross-section of Stock Returns | Steven L. Heston, Robert A. Korajczyk, Ronnie Sadka | 2010-05(arXiv v1 提交于 2010-05-03;正式发表 Journal of Finance 65(4), 1369–1407, 2010-08) | arXiv / Journal of Finance | https://ar5iv.arxiv.org/html/1005.3535 | true |
| S10 | Stealth trading and volatility: Which trades move prices? | Michael J. Barclay, Jerold B. Warner | 1993(Journal of Financial Economics 34(3), 281–305) | 期刊:Journal of Financial Economics | （搜索结果给出标题/作者/卷期页码,未独立确认 DOI/直接链接） | true |
| S11 | A Note on Using Cross-Sectional Information in Bayesian Estimation of Security Betas | Oldrich A. Vasicek | 1973-12(Journal of Finance 28(5), 1233–1239) | 期刊:Journal of Finance | https://ideas.repec.org/r/bla/jfinan/v28y1973i5p1233-39.html | true |
| S12 | Estimating betas from nonsynchronous data | Myron Scholes, Joseph Williams | 1977(Journal of Financial Economics 5, 309–327) | 期刊:Journal of Financial Economics | （搜索结果给出标题/作者/卷页,未独立确认 DOI/直接链接） | true |
| S13 | Risk measurement when shares are subject to infrequent trading | Elroy Dimson | 1979(Journal of Financial Economics 7(2), 197–226) | 期刊:Journal of Financial Economics | （搜索结果给出标题/作者/卷期页码,未独立确认 DOI/直接链接;另有评论文章 Rorke, Journal of Financial Economics 12, 279–283, 1983） | true |
| S14 | On the Estimation of Beta-Pricing Models | Jay Shanken | 1992(Review of Financial Studies 5(1), 1–33) | 期刊:Review of Financial Studies | https://ideas.repec.org/a/oup/rfinst/v5y1992i1p1-33.html | true |
| S15 | Time Series Momentum | Tobias J. Moskowitz, Yao Hua Ooi, Lasse Heje Pedersen | 2012(Journal of Financial Economics 104(2), 228–250;SSRN 工作稿更早,具体提交日期未在搜索结果中给出) | 期刊 / SSRN | https://papers.ssrn.com/abstract=2089463 | true |
| S16 | （2021 年 AEA 会议初稿,把集合竞价成交占比当"投资者分歧"代理;未发现期刊发表版,标题/完整作者未在搜索结果中给出) | 不详(会议系统列为初稿) | 2021(会议初稿,证据弱,未定论) | AEA 2021 会议初稿 | https://aeaweb.org/conference/2021/preliminary/paper/H9T4hef7 | true |

未列入上表、曾经搜索但没有搽到可用文献的方向(诚实记录,不编造):
- "一天内连续同一均价的分钟数占比"作为分钟级横截面因子的直接先例——搜不到(L1 第 5 条)。
- Durbin–Watson 统计量(或其等价形式)被直接用作成交量横截面因子的先例——搜不到(L2 第 5 条)。
- "把滚动回归斜率替换成 t 值作为因子、且样本外更稳"的直接对照实验——搜不到(L3 第 5 条)。
- "分钟级成交量小时尺度差分、按日取均值"这个具体统计量,或中国 A 股市场专门的日内放量缩面形态横截面因子研究——搜不到(L4 第 5 条)。

---

## 给 PI 的一句话总结

四条题目里,**最硬、最可直接改算子的两条**是:(a)L3 第 2 条——核心 A 的自变量本身就是"价格钉住/稀疏交易"的度量,而 Scholes-Williams/Dimson 这类经典文献专门处理这种情况下的回归偏误,**用前导+滞后加总的回归系数替换同期 `ts_regbeta`** 是一个有外部文献支持、此前从未在本种子试过的具体变体;
(b)L2/L4 共用的一条——**先剥掉日内 U 形基准再谈"粗糙度"或"放量缩量形态"**,这对核心 A 的 `day_durbin_watson(Volume)` 和核心 B 的 `in_delta(Volume,60)` 都适用,且有 Admati-Pfleiderer 的理论基础和 Hawkes 聚集性文献的方法论先例。
L1 和 L4 的其余条目更多是"怎么分组、怎么检验机制"的方法论借鉴,不是可以直接替换进算子树的处理方式;L1/L2/L4 都各有一条明确的"搜不到"——核心 A、核心 B 在这个构造粒度上都没有直接的文献先例,这本身也是一个诚实的信号:它们更可能是本次 GP 搜索的真正新发现,而不是重新发现了已知因子。
