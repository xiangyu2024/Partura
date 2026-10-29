# 文献:种子 805,B 组,第 1 轮

对准 `analysis.md` §6 的 L1–L4,核心是 `day_centroid(Volume)`(日内成交量重心)。只用 **2023-08-08 之前**发表的论文 / 工作论文 /研究报告(journal 用正式出版日期,working paper 用首版/流通日期)。
每条处理手法后面用 `[Sx]` 指向文末的出处表;出处表里 `verified: true` = 这次搜索结果或页面上确实看到了标题 / 作者 / 期刊 / 链接这组信息对得上,不是凭记忆写的。拿不准发表月份的,一律在正文里写明「未确认月份,未用于下方任何一条处理手法」,不进出处表当证据用。

## L1. 日内成交量分布 / 成交量时点,文献里怎么处理

**结论先说**:经典文献几乎全部停在**水平**和**小时级分桶**,没有一篇把它做成"重心"这种单一标量再拿去做横截面排序因子——这件事本身就是信息(我们环境里的 `day_centroid` 比文献常见处理更激进地压缩了信息)。

1. **水平、不做任何横截面或时序标准化,按小时分箱统计均值/方差**:Jain & Joh (1988) 用 NYSE 逐小时成交量与收益,发现同小时内成交量与收益紧密相关,且这个关系能往前追溯到四小时之前,正收益时的量—价关系比非正收益时更陡 [S1]。
   → 操作语言:这等价于只看 `day_wmean` 式的小时级汇总,**没有**任何归一化步骤;文献自己也没有把"几点钟成交多"压缩成一个数再排序,这正是我们 `day_centroid` 在做但文献没做的事。
2. **把"日内成交集中在开盘和收盘"解释成策略性行为的内生结果,而不是外生的日历效应**:Admati & Pfleiderer (1988) 的理论模型里,有自由选择交易时点的流动性交易者会**聚堆**交易以在知情交易者面前隐藏自己,知情交易者也倾向在流动性交易者聚堆的时段交易——U 形是两类交易者策略互动的产物 [S2]。
   → 操作语言:这条支持的不是某个具体算子,而是**条件化的方向**:如果重心的信息含量来自"知情/流动性交易者的相对强弱",那么重心应该在**高异常成交、高波动的日子更有信息**,而不是任何一天都一样重——对应 C 类交互里按 `cross_mean(day_sum(Amt), 30)` 的偏离程度或 `day_std` 做状态门控(`cs_flip_by_state(day_centroid(Volume), day_sum(Amt))` 已经是这个方向,§5.1 清单里有)。
3. **把成交量时点曲线本身当输入去做 VWAP 执行模型,而不是当 alpha 特征**:佛罗伦萨大学的一篇工作论文把日内成交量份额曲线用 Dirichlet 型 GAS(广义自回归得分)模型来跨日预测,动机是 VWAP 算法交易,论文明确提到价格不可预测性让"份额预测"本身的评估很难 [S3](**注意**:我只在搜索摘要里看到这篇论文的存在和主题,没能打开 PDF 正文核对具体公式,所以下面不据此写任何具体处理手法,只记它的存在和定位——它研究的是"份额曲线"的**跨日自回归结构**,提示 `day_centroid` 这类量本身可能有可预测的时序结构,这条和 L3 的"自身历史标准化"思路是互补的)。

**搜不到的部分**:没搜到任何文献把"成交量重心"(或任何等价的单一标量时点统计量)直接当作横截面股票收益的预测变量来检验——这类研究如果存在,更可能是交易所微观结构期刊里按分钟分箱做方差分解的工作,而不是资产定价期刊里的横截面因子论文,我在允许的搜索次数内没有定位到。

## L2. 收盘集合竞价 / 尾盘成交占比是不是机构 / 指数成分的代理

1. **A 股本地证据,机制相关但方法上只做了"市场质量"检验,没有做"按被动持股比例分组"**:Han, Zhao, Chen & Guo (2022, *Pacific-Basin Finance Journal* 74) 用上交所 2018-08-20 实施收盘集合竞价的自然实验,双重差分发现:(a) 成交量从收盘连续竞价阶段**转移到了竞价前**(14:57 前),(b) 竞价前波动率上升,(c) 流动性没有显著变化,(d) 小盘股受益更明显 [S4]。
   → 操作语言:这篇**没有**给出"剔除指数成分股"或"按被动持股比例分组"的具体处理,但它确认了一个前提——14:57–15:00 这个窗口本身在 2018-08-20 之后才有,而我们数据里 `day_centroid` 用全日 241 个分钟格,这意味着**样本早期(2018)和晚期的"收盘集合竞价"机制不是同一回事**,`day_centroid` 在 train 段(2018–2021)内部就跨越了这次制度改变,这是一条值得写进 E/N 任务书的机制提醒,而不是文献给出的处理手法。
2. **美股证据,直接支持"用被动持股比例做非线性剥离"这个方向、但不是 A 股**:Bogousslavsky & Muravyev 的工作论文"Should We Use Closing Prices? Institutional Price Pressure at the Close"(至少 2019 年已流通,多处会议/研讨会记录引用)发现收盘竞价成交量占比与 ETF/被动基金持股的关联远强于与竞价前成交量的关联,指数再平衡日竞价成交量会跳升,且主动型基金没有这种关联 [S5]。
   → 操作语言:这篇**明确支持** `cs_bucket_rank(day_centroid(Volume), LogFloatCap)` 这类按市值分桶再排序的做法,逻辑是"被动持股比例本身高度非线性地依赖市值(成分股门槛是阶梯式的,不是市值的线性函数)",线性中性化(我们奖励里对 `LogFloatCap` 的中性化方式)去不掉这种阶梯效应,分桶排序可以。
   **但这是美股证据,不是 A 股证据** —— 我没能搜到把这条逻辑直接搬到 A 股(例如按沪深300/中证500成分、或按 ETF 持股比例分组)的研究,§2.4 判断通道 1 目前仍然只是机制推断,文献只能提供"这个机制在别的市场成立"的旁证,不能提供 A 股本地的验证。
3. **搜不到的部分**:没搜到任何研究直接把"A 股尾盘成交占比"与"指数成分 / ETF 被动资金 / 机构持股比例"三者联系起来并给出具体剥离方法(剔除调仓窗口、按被动持股比例分组等);Han et al. (2022) 研究的是集合竞价这个**机制**对市场质量的影响,不是"尾盘占比"这个**特征**的代理问题。

## L3. 日内时点的"异常"版本:自身历史标准化 vs 横截面排序

这一题恰好有一组**可以直接对照**的经典文献,一边做横截面排序(水平),一边做自身历史标准化(偏离),结论方向相反:

1. **横截面排序 + 水平(不做时序标准化)**:Datar, Naik & Radcliffe (1998, *Journal of Financial Markets* 1(2), 203–219) 直接用换手率的**原始水平**做横截面排序去检验 Amihud-Mendelson 流动性模型,控制规模/账面市值比/beta 后,换手率越高、未来收益越低,这个关系全年都存在而不只在一月 [S6]。
   → 操作语言:这是 `cross_rank` 或 `cs_rank` 直接作用在**水平**上的经典做法,不涉及任何自身历史的标准化。
2. **自身历史标准化(相对自身过去几周的异常变化)**:Gervais, Kaniel & Mingelgrin (2001, *Journal of Finance* 56(3), 877–919,"The High-Volume Return Premium")不看成交量水平,而是看它**相对自身近期历史**的极端变化,发现成交量出现极端变化(放量或缩量)的股票,其后一个月的收益会被放大(高量后续超额收益为正,低量后续为负),作者把这个归因于"关注度/可见度"变化,后续 Kaniel, Ozoguz & Starks (2012) 把这个结果推广到了 41 个国家,发现在发达市场和不少新兴市场都存在 [S7]。
   → 操作语言:这正是 `cross_zscore(day_centroid(Volume), d)` / `cross_madz(...)` 这条 A 类外围的直接文献原型——"不看量本身,看量相对自己过去 d 天的偏离",只是原论文用在**总成交量**上,我们是用在**重心**(日内形状统计量)上,属于同一处理手法的不同底层特征。
3. **同一篇论文内部直接对照"水平版"与"偏离版"**:Lee, Kim & Kim (2016,韩国金融学会会议论文,"Abnormal Trading Volume and the Cross-Section of Stock Returns")把换手率拆成**预期部分**(用过去行为可解释的部分,即近似"水平")和**异常部分**(拆完剩下的残差,即近似"偏离"),发现异常(偏离)部分能正向预测未来最多五周的收益,而预期(水平)部分对收益的预测方向是**负的**、且在更长horizon上持续 [S8](**这篇我没能找到正式期刊出处,只确认了会议论文和二手摘要,下面只引用其"方向相反"这个定性结论,不引用任何具体数字**)。
   → 操作语言:这是目前搜到的**最直接**支持"水平版无效或方向错、偏离版有效"这个假说的文献——如果把 `day_centroid(Volume)` 换成换手率类比,Lee-Kim-Kim 的结果等价于预测 §7 可检验预测 3(A/B 类外围应明显优于纯保序外围)。
4. **窗口通常取多长**:三篇里能确认具体窗口的只有 Gervais-Kaniel-Mingelgrin,用的是"近几周"(原文窗口在摘要/二手总结里写的是"过去几周",我没能从搜索结果里拿到精确的天数,**不写成具体数字**,只记"周级,不是月级也不是年级")[S7]。Lee-Kim-Kim 的"预期部分"回归窗口同样没能从摘要里拿到精确数字 [S8]。**20/60/250 日这三个具体候选窗口,文献摘要层面都没给出确凿依据**,这点要如实报给 PI:窗口选择目前只能靠我们自己的敏感性检验,不能靠文献定。

## L4. A 股日内成交集中度 / "聪明钱"与"开盘-收盘强度"类特征的构造与条件化

1. **"开盘-收盘强度"类(intraday momentum)的权威原型**:Gao, Han, Li & Zhou (2018, *Journal of Financial Economics* 129(2), 394–414,"Market Intraday Momentum")用标普500 ETF 高频数据发现**首个半小时收益**(相对前一日收盘)能预测**最后半小时收益**,这个可预测性在波动更高、成交量更高、衰退期、以及部分宏观新闻发布日更强;同样的模式在另外十个最活跃的国内外 ETF 上也存在。作者把机制归为"不频繁的组合再平衡"和"临近收盘的迟到知情交易" [S9]。
   → 操作语言:这篇是"开盘段收益 vs 收盘段收益"交互的标准写法,对应我们environment 里可以写成 `div` / `sub` 作用在两个按分钟窗口切片的 `day_wmean(Ret, w)` 上(开盘前 N 分钟权重 vs 收盘前 N 分钟权重),是一条 C 类交互的具体实现路径,而不是直接用在 `day_centroid` 上。
2. **A 股本地的"聪明钱"量化证据,但是学术论文、不是我原来设想的卖方研报**:Chen, Liu, Teka & Zhang (2022, *Research in International Business and Finance* 61, "Smart money in China's A-share market: Evidence from big data")用 1999–2019 年 A 股 1 分钟级逐笔数据构造"聪明钱"强度指标(识别知情交易者的交易侵略性,定月度方向),发现这个指标与未来收益是**负向**的横截面关系;用模糊 c-均值聚类分组构造的策略年化夏普最高到 1.169 [S10]。
   → 操作语言:这篇的"聪明钱强度"本质上是一个**分钟内价格冲击 / 成交量**的复合统计量,和我们核心 `day_centroid(Volume)`(只用时点、不用冲击)是不同的信息维度,但它确认了"用分钟级数据构造的强度类指标在 A 股上能找到横截面关系,方向可能和直觉相反(负向)"这个大前提——对应我们 §5.3 第 1 条"同族日内形状统计量值得铺开试"这个判断,是支持而不是反对。**我没搜到这篇论文具体怎么处理涨跌停/停牌样本**,这一点要留白,不能编。
3. **净买压 / 订单失衡的日频代理构造**:
   - Chordia, Roll & Subrahmanyam (2002, *Journal of Financial Economics* 65(1), 111–130)用 NYSE 市场整体的日度**订单失衡**(买方发起成交量减卖方发起成交量)而不是总成交量作为交易活动的度量,发现大跌后失衡会上升(整体投资者是反向操作的),失衡越极端流动性越差,控制了成交量和流动性之后,订单失衡仍然对收益有显著影响,且这个效应不持续超过一天 [S11]。
   - 在没有逐笔买卖方向数据时,一种常见的日频替代构造是"用收益方向给成交量定符号"(按当日涨跌给成交量/成交额定号,再做窗口汇总),新加坡国立大学一篇工作论文把这个思路追溯到 Pastor & Stambaugh (2003) 用"收益定号的美元成交量"做流动性代理的方法,并指出收益很大时这种方法会低估真实的订单失衡 [S12](**这篇我没找到确切的首版年份,只确认了方法描述和它对 Pastor-Stambaugh (2003) 的引用,Pastor-Stambaugh 本身是 2003 年《Journal of Political Economy》论文,早于截止日,可以放心引用这个方法来源;NUS 工作论文本身的日期不确定,不单独作为日期证据使用**)。
   → 操作语言:这组文献直接对应 `day_signed_ratio(Ret, Amt)`(涨分钟成交占比减跌分钟成交占比,净买压代理)这个 §5.3 第 1 条列出的算子——"用分钟内的涨跌给成交定号再汇总"是文献里确认过的标准代理构造,不是我们环境里凑出来的新东西。
4. **涨跌停样本处理**:Wan, Wang, Jiang, Xie & Zhou (2018, *Physica A* 505, 153–163,"The cooling-off effect of price limits in the Chinese stock markets")用 2000–2011 年沪深 A 股高频数据研究涨跌停后的"冷却效应",发现跌停的冷却效应比涨停更强,且牛市熊市下差异不大;机制上归因于专业散户和机构投资者用次优报价起到了稳定作用 [S13]。
   → 这篇**没有**给出"聪明钱/日内集中度"因子里具体怎么剔除涨跌停样本的处理细节(比如是整天剔除还是只剔除涨跌停后的分钟),只确认了涨跌停后成交结构会发生系统性改变,这一点和 §2.4 通道 3(涨跌停锁板导致 `day_centroid` 机械偏小)是同一机制的独立佐证,但不是"怎么处理"的答案。**具体剔除规则(整天剔除 vs 只剔除涨停分钟 vs 按涨跌停带宽 `LimitWidth` 做条件化)在文献层面搜不到标准做法,只能靠我们自己定**。
5. **Gini 集中度度量**:搜到的是股指期货(S&P CNX Nifty)和台湾券商层面的成交集中度 Gini 研究,不是单只 A 股股票的日内成交集中度研究,证据层级不够,**不作为 `day_gini(Amt)` 这个算子的直接文献支持,只记录"Gini 这个工具在相邻领域——期货指数日内集中度、券商层面集中度——被验证过是有信息的"这个弱证据** [S14]。
6. **"开盘/收盘段机构更活跃、价格更跟机构走"的 A 股证据**:Qiu, Huang & Jiang (2023-06, *Finance Research Letters* 54, "When do they trade? Heterogeneous investors in China")发现在 A 股,相比散户,机构在开盘和收盘附近更活跃,且全天价格走势更跟随机构交易而不是散户交易 [S15]。
   → 操作语言:这篇**直接支持** §2.4 判断通道 1/2(开盘段偏散户、尾盘段偏机构资金/指数成分)的机制假设在 A 股成立,也支持 B 类"按 `LogFloatCap` 或流动性分桶"这个处理方向——如果机构在开盘收盘的活跃度和规模相关,分桶应该能把这部分效应剥掉。

## 出处表

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|---|
| S1 | The Dependence between Hourly Prices and Trading Volume | Prem C. Jain, Gun-Ho Joh | 1988-09 | Journal of Financial and Quantitative Analysis, 23(3), 269–283 | https://ideas.repec.org/a/ucp/jnlbus/v61y1988i2p219-31.html ; https://resolve.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/dependence-between-hourly-prices-and-trading-volume/C305DB5BFB5F2B2D803BB94449AF8B47 | true |
| S2 | A Theory of Intraday Patterns: Volume and Price Variability | Anat R. Admati, Paul Pfleiderer | 1988 | Review of Financial Studies, 1(1), 3–40 | https://www.gsb.stanford.edu/faculty-research/publications/theory-intraday-patterns-volume-price-variability ; https://ideas.repec.org/a/oup/rfinst/v2y1989i2p189-223.html | true |
| S3 | (未确认标题/作者;佛罗伦萨大学 DISIA 工作论文,日内成交量份额 Dirichlet-GAS 模型,动机为 VWAP 执行) | 未确认 | 2014(PDF 元数据创建日期 2014-02;论文首版日期未确认) | DISIA working paper,Università degli Studi di Firenze | https://labdisia.disia.unifi.it/wp_disia/2014/wp_disia_2014_01.pdf | false(只在搜索摘要里看到主题描述,没能打开/核对 PDF 正文的标题页与作者) |
| S4 | Reexamining the impact of closing call auction on market quality: A natural experiment from the Shanghai stock exchange | Qian Han, Chengzhi Zhao, Jing Chen, Qian Guo | 2022-09 | Pacific-Basin Finance Journal, 74, 101821 | DOI 10.1016/j.pacfin.2022.101821 ; https://orca.cardiff.ac.uk/151359 | true(经 Crossref 元数据核对 published/issued = 2022-09) |
| S5 | Should We Use Closing Prices? Institutional Price Pressure at the Close (working paper title) | Vincent Bogousslavsky, Dmitriy Muravyev | 至少 2019(多处 2019-11 / 2020-09 会议页面已引用,未能直接打开 SSRN 摘要页确认首版日期) | SSRN working paper | ssrn.com/abstract=3485840(直接访问返回 403,未能核对) | true(标题、作者、核心发现在多个独立二手页面——OptionMetrics 2019-11 博客、Boston College 2020-09 研讨会页——反复一致地出现) |
| S6 | Liquidity and stock returns: An alternative test | Vinay T. Datar, Narayan Y. Naik, Robert Radcliffe | 1998-08 | Journal of Financial Markets, 1(2), 203–219 | https://www.london.edu/faculty-and-research/academic-research/l/liquidity-and-stock-returns-an-alternative-test ; https://ideas.repec.org/ (vol 1(2) 203-219) | true |
| S7 | The High-Volume Return Premium | Simon Gervais, Ron Kaniel, Dan Mingelgrin | 2001-06(Journal of Finance 56(3)) | Journal of Finance, 56(3), 877–919 | https://ideas.repec.org/a/bla/jfinan/v56y2001i3p877-919.html ; https://sites.duke.edu/sgervais/?p=64 | true |
| S7b | (跟进,仅作背景,不单独作为处理手法证据)The High Volume Return Premium 跨国证据 | Ron Kaniel, Arzu Ozoguz, Laura Starks | 2012 | 二手摘要确认,具体期刊页码未核对 | https://efnchina.com/content-7-62240-1.html | false(未核对原始期刊页) |
| S8 | Abnormal Trading Volume and the Cross-Section of Stock Returns | Deok Hyeon Lee, Min Ki Kim, Tong Suk Kim | 2016(韩国金融学会会议论文;正式期刊出处未确认) | Korean Finance Association 会议论文 / 二手摘要(Quantpedia、播客摘要) | https://vvv.quantpedia.com/?p=711 ; https://podcast.ausha.co/papers-with-backtest-an-algorithmic-trading-journey/abnormal-trading-volume-key-findings-on-stock-returns | true(标题、作者、"预期负向/异常正向"这一定性结论在至少两个独立二手来源里一致出现;**具体回测数字不采信**) |
| S9 | Market intraday momentum | Lei Gao, Yufeng Han, Sophia Zhengzi Li, Guofu Zhou | 2018-08(JFE 129(2)) | Journal of Financial Economics, 129(2), 394–414 | DOI 10.1016/j.jfineco.2018.05.009 ; https://www3.nd.edu/~zda/intramom.pdf | true |
| S10 | Smart money in China's A-share market: Evidence from big data | Zhenhua Chen, Zhenya Liu, Hanen Teka, Yifan Zhang | 2022(RIBAF 61) | Research in International Business and Finance, 61, 101663 | DOI 10.1016/j.ribaf.2022.101663 ; https://ideas.repec.org/a/eee/riibaf/v61y2022ics0275531922000514.html | true |
| S11 | Order imbalance, liquidity, and market returns | Tarun Chordia, Richard Roll, Avanidhar Subrahmanyam | 2002-07(JFE 65(1)) | Journal of Financial Economics, 65(1), 111–130 | https://ideas.repec.org/a/eee/jfinec/v65y2002i1p111-130.html | true |
| S12 | (方法引用:日频订单失衡的"收益定号成交额"代理,追溯到 Pastor & Stambaugh 的流动性度量构造;NUS 工作论文本身标题/日期未确认) | 未确认(NUS 工作论文);被引用的方法来自 Lubos Pastor, Robert F. Stambaugh | 方法来源 Pastor & Stambaugh (2003-08,JPE 111(3),"Liquidity Risk and Expected Stock Returns");引用它的 NUS 工作论文日期未确认 | Journal of Political Economy(Pastor-Stambaugh 部分);NUS 工作论文日期不明 | https://rmi.nus.edu.sg/wp-content/uploads/2020/10/35.-JinGi-Ha_updated.pdf | true(Pastor-Stambaugh 2003 这一部分确认;NUS 工作论文日期不确认,不单独作证据) |
| S13 | The cooling-off effect of price limits in the Chinese stock markets | Yu-Lei Wan, Gang-Jin Wang, Zhi-Qiang Jiang, Wen-Jie Xie, Wei-Xing Zhou | 2018 | Physica A: Statistical Mechanics and its Applications, 505, 153–163 | arXiv:1803.09422 ; https://ideas.repec.org/a/eee/phsmap/v505y2018icp153-163.html | true |
| S14 | (弱证据,不单独支撑任何具体处理手法)股指期货 / 券商层面成交集中度的 Gini 度量,具体论文标题未逐一核对 | 未逐一核对 | 未逐一核对 | 二手摘要 | 搜索结果里的多篇二手摘要,未打开原文 | false |
| S15 | When do they trade? Heterogeneous investors in China | Jiayan Qiu, Wei Huang, Ying Jiang | 2023-06(FRL 54) | Finance Research Letters, 54, 103729 | DOI 10.1016/j.frl.2023.103729 ; https://research.nottingham.edu.cn/en/publications/when-do-they-trade-heterogeneous-investors-in-china/ | true(经 Crossref 元数据核对 published/issued = 2023-06,在 2023-08-08 截止日之前) |

## 给 PI 的汇总(哪些处理手法有文献撑,哪些没有)

- **有扎实文献支持、可以直接写进 E/N 任务书**:
  - A 类自身偏离(`cross_zscore`/`cross_madz`):S7(水平 vs 偏离,偏离版有效)+ S8(预期/水平版方向错,异常/偏离版方向对)是目前最硬的两条。
  - B 类按市值/流动性分桶(`cs_bucket_rank(..., LogFloatCap)`):S5(美股,ETF/被动持股与市值阶梯非线性相关)+ S15(A 股,机构活跃度在开盘收盘确实更高、确实和散户不同)。
  - C 类与净买压交互(`day_signed_ratio(Ret, Amt)`、或按 `day_wmean(Ret, w)` 切片做开盘/收盘段交互):S9(开盘段收益预测收盘段收益的权威原型)+ S11/S12(订单失衡/净买压的日频代理构造有文献依据)。
- **机制上说得通但 A 股本地证据缺失,写任务书时要标注"推断,非文献证实"**:按被动持股比例/指数成分剥离尾盘占比(§2.4 通道 1)——S4 只证实了集合竞价机制本身影响市场质量,S5 的被动资金关联是美股证据。
- **搜不到、如实记录,不要在 PI 的任务书里当成文献支持**:
  - 涨跌停样本的具体剔除规则(整天 vs 只剔分钟 vs 按 `LimitWidth` 条件化)。
  - "成交量重心"这个单一标量本身被当作横截面因子检验的任何文献。
  - 中文卖方"聪明钱因子"研报原文(只找到对应的学术论文 S10,机制相近但构造细节不同)。
  - L3 里 20/60/250 日窗口选择的文献依据——没有,窗口是我们自己要测的。
