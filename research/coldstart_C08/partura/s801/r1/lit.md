# 文献:种子 801,P 组,第 1 轮(文献员)

对准 `analysis.md` §5 的 4 个题目。只用 2023-08-08 之前发表/挂出的论文、工作论文或研究报告(arXiv/SSRN 以首版日期为准)。每条「处理方式」后面标出处;出处里 `verified: true` = 这次搜索/抓取确实看到了该文献(标题、作者、摘要或正文片段),`verified: false` = 只在二级引用里见过名字、没有直接核实到。搜不到的,在每题末尾单列「没搜到」。

---

## 题目 1 —— 日内成交量的自相关 / 粗糙度(对准核心 1 `day_durbin_watson(Volume)`)

### 关键结论:没有文献直接把 Durbin–Watson 统计量用在成交量上

搜了「Durbin-Watson + trading volume + factor/roughness/smoothness」「variance ratio + volume persistence + half-life」等多种组合,确认 **DW 统计量是回归残差自相关的诊断量,文献里没人把它直接套在成交量序列上当因子**。这件事本身是有用的否定结果:核心 1 在"构造方式"上是我们自己的发明,文献提供的是**邻近的、已验证的构造方式**,可以拿来对照、拆解、或替换。

### 处理方式 1:自相关直接用自相关函数算,不要用"变化量²/水平量²"这种比值去代理

Lillo, Mike & Farmer 把下单方向序列的持续性,直接算成**自相关函数本身**(各阶 lag 的 ACF),再看它随 lag 衰减的形状(是否幂律衰减、是否在交易日边界断开),用来判断持续性来自"大单拆单"还是"从众"。这是和我们 `day_durbin_watson`(用 Σ(x_t−x_{t-1})² / Σx_t² 这种能量比值代理自相关)完全不同的构造路线:**直接测 ACF,不要用能量比值去反推**。
算子语言翻译:在 `in_demean(Volume)` 之后,不是去构造一个比值,而是直接 `ts_corr(x, ts_delay(x,1), window)` 这类"真自相关"写法;并且可以在多个 lag 上重复,看衰减形状,而不是只看 lag-1。
出处:
- 标题:Theory for Long Memory in Supply and Demand
- 作者:Fabrizio Lillo, Szabolcs Mike, J. Doyne Farmer
- 年-月:2005-06(Phys. Rev. E 71, 066122,2005 年 6 月 22 日发表)
- 来源:Physical Review E(经 iris.unipa.it 镜像确认)
- 链接:https://iris.unipa.it/bitstream/10447/9549/1/PhysRevE.71.066122.pdf
- verified: true(搜索结果中直接看到摘要与机制描述:隐藏大单按幂律分布,被拆成小单以稳定速率提交,产生的自相关呈幂律衰减,γ = β − 1)

### 处理方式 2:成交量的自相关不单独当特征,而是和"收益的自相关"交互,方向由成交量水平决定

Llorente, Michaely, Saar & Wang 的构造不是对成交量本身求自相关,而是用滚动回归 `r_{t+1} = θ0 + θ1·r_t + θ2·(volume_t · r_t) + ε` 把"成交量条件下的收益自相关"θ2 提出来:θ2 为正=有信息交易主导(延续),为负=对冲/流动性交易主导(反转)。这给了"A 到底是信息来源还是代理"的一个独立判据:**不看 DW 本身的横截面排序,而看它和次日收益自相关的交互方向**。
算子语言翻译:构造 `cross_cov`/回归式的交互项,例如把 `day_durbin_watson(Volume)` 当作调制变量,去看 `cross_cov(day_ret, ts_delay(day_ret,1), window)` 在高 DW 组和低 DW 组之间是否变号——这是对 A 机制的一个独立检验,不依赖相关度表。
出处:
- 标题:Dynamic Volume-Return Relation of Individual Stocks
- 作者:Guillermo Llorente, Roni Michaely, Gideon Saar, Jiang Wang
- 年-月:2002(The Review of Financial Studies, Vol. 15, No. 4, Autumn 2002, pp. 1005–1047;更早的工作论文版本是 NYU Stern FIN-00-032,2000 年)
- 来源:Review of Financial Studies / NYU Stern working paper
- 链接:https://archive.nyu.edu/jspui/bitstream/2451/26698/1/FIN-00-032.pdf
- verified: true(搜索结果直接给出模型与检验设计:对冲型交易产生反转,信息型交易产生延续,用日度量与一阶收益自相关的截面关系检验)

### 处理方式 3:高成交量日的收益反转更强(方向性的 volume×autocorrelation 关系)

Campbell, Grossman & Wang 的模型机制是:做市商承接非信息交易者的买卖压力需要补偿,所以**成交量越大的那天,收益的一阶自相关越负(反转越强)**。这不是对 Volume 本身求自相关,而是"用 Volume 的水平去条件化收益的自相关强度"。
算子语言翻译:同处理方式 2 的交互检验族,是另一个独立出处;可以把 A(成交量粗糙度/自相关)和 Volume 水平分别作为两个调制变量,比较哪个更能解释次日收益自相关的强弱。
出处:
- 标题:Trading Volume and Serial Correlation in Stock Returns
- 作者:John Y. Campbell, Sanford J. Grossman, Jiang Wang
- 年-月:1993-11(Quarterly Journal of Economics, Vol. 108, No. 4, pp. 905–939;早期版本 NBER Working Paper No. 4193,1992-10)
- 来源:Quarterly Journal of Economics / NBER
- 链接:https://dash.harvard.edu/bitstream/1/3128710/2/campbell_trading.pdf
- verified: true(搜索结果直接确认机制与发表信息)

### 处理方式 4:交易到达的"持续性"用自回归条件化的到达间隔模型,而不是单一比值统计量

Engle & Russell 的 ACD 模型把交易/成交量到达的聚集性,构造成一个**自回归条件均值过程**(类比 GARCH,但作用在到达间隔/强度上),同时分离出"日内形状的确定性部分"(类似我们的 U 形)和"随机聚集部分"。这提示:如果要把 A 的"持续性"这一半做干净,更接近文献做法的是**先剥掉日内确定性形状,再对剩余部分建模自回归**,而不是一个单期的能量比值。
算子语言翻译:对应到我们的算子,是"先用某种日内基准(如同一分钟桶的历史均值)去标准化,再对标准化后的残差做 `day_ar1_coefficient` 或 `ts_corr`",而不是直接对 raw Volume 做 DW。
出处:
- 标题:Autoregressive Conditional Duration: A New Model for Irregularly Spaced Transaction Data
- 作者:Robert F. Engle, Jeffrey R. Russell
- 年-月:1998-09(Econometrica, Vol. 66, No. 5, pp. 1127–1162;早期版本 NBER Working Paper No. 4966)
- 来源:Econometrica
- 链接:https://www.econometricsociety.org/publications/econometrica/1998/09/01/autoregressive-conditional-duration-new-model-irregularly
- verified: true(搜索结果直接确认模型描述与发表信息;ACD 对成交量的扩展在 NBER 工作论文摘要中提及,但该细节未能直接抓取全文核实,计入处理方式而非单独引用)

### 没搜到

- 没搜到任何文献直接把 Durbin–Watson 统计量(或等价的"能量比值"构造)用作成交量的横截面特征。
- 没搜到专门处理"薄成交股票在自相关类统计量上界/下界处堆积"这个数值问题的论文(这是 analysis.md §1.3 风险 1 的核心关切);题目 4 里 Wan et al. (2015) 间接提到"次新股成交稀薄、更容易撞到统计量边界",但不是针对自相关统计量本身,算部分相关,已归入题目 4。

---

## 题目 2 —— 成交量变异系数 / 换手率波动的定价(对准 §4.2 第 2–3 号,判断 A 是真来源还是代理)

### 处理方式 1:变异系数就是 std/mean,在"月度及以上"的窗口上算,再做横截面排序定价

Chordia, Subrahmanyam & Anshuman 把"成交活动的二阶矩"构造为**美元成交量、换手率在较长历史窗口上的标准差/均值**(本质就是 CV),控制规模、账面市值比、动量、以及成交活动的水平之后,做 Fama–MacBeth 横截面回归。结果是**显著为负**:变异性越大,预期收益越低。这正是 analysis.md §4.2 第 3 号(`div(day_std(Volume), day_mean(Volume))`)如果显著为负,会与一个**已知的、已经发表的效应**重合——必须在相关度表上核对这条线会不会撞上这个已知特征(虽然它不在我们的 5 个显式控制里,但审计员判断"同一个东西"时可能参考这类已知文献)。
算子语言翻译:`div(cross_mean(day_std(Volume), window_长), cross_mean(day_mean(Volume), window_长))` 这种跨越多天的 CV,和我们核心 1 §4.2 第 3 号的**日内** CV(`div(day_std(Volume), day_mean(Volume))`,单日内分钟级)是**不同尺度的对象**——前者是"这只股票最近一两个月成交量忽大忽小",后者是"这只股票今天一天之内的分钟成交量忽大忽小"。这个尺度区分本身就是一条可执行的处理建议:不要把两者混为一谈。
出处:
- 标题:Trading Activity and Expected Stock Returns
- 作者:Tarun Chordia, Avanidhar Subrahmanyam, V. Ravi Anshuman
- 年-月:2001-01(Journal of Financial Economics, Vol. 59, No. 1, pp. 3–32)
- 来源:Journal of Financial Economics(经 IDEAS/RePEc 确认条目)
- 链接:https://ideas.repec.org/a/eee/jfinec/v59y2001i1p3-32.html
- verified: true(WebFetch 直接核实标题、作者、期刊、卷期页码;摘要全文需订阅,核心结论来自搜索摘要片段,未在付费墙后核实原文数字)

### 处理方式 2:VCV(std/mean)本身被单独当作信息不对称的代理,不直接当返回因子

Lof & van Bommel 把 VCV = std(volume)/mean(volume) 明确定义为一个**独立构造的比值特征**,在微观结构模型里证明它随知情交易比例单调上升;实证上发现它在分析师覆盖下降(经纪商关停的外生冲击)后上升,在业绩公告等信息披露前后急剧下降。这给出了一个**关键的处理细节**:VCV 这个量对**信息事件的时点很敏感**(财报前后会跳),所以如果要把 §4.2 第 3 号的日内 CV 当作候选特征,需要检查它是否也在财报日附近有类似的跳变——如果有,说明它和"知情交易比例"这条经济机制是一致的,而不是纯噪声。
算子语言翻译:同处理方式 1 的比值构造,但窗口来源不同:Lof & van Bommel 用的是**公司-年度**尺度(用全年日度成交量算 std/mean);核心 1 §4.2 第 3 号用的是**单日分钟内**尺度。两者在数学形式上相同,在经济含义上是两个不同的"知情交易代理"版本(年度版本已发表,日内版本是我们自己的延伸)。
出处:
- 标题:Asymmetric Information and the Distribution of Trading Volume
- 作者:Matthijs Lof, Jos van Bommel
- 年-月:2018-01(Bank of Finland Research Discussion Papers 1/2018;正式发表版 Journal of Corporate Finance, 2023-10,但发表版晚于截止日,这里只引用 2018 年工作论文版本)
- 来源:Bank of Finland Research Discussion Paper
- 链接:https://publications.bof.fi/handle/10024/47882
- verified: true(WebFetch 直接核实标题、作者、日期、VCV 定义与主要发现)

### 处理方式 3:成交量相对自身历史均值的"水平"(不是变异系数)本身就能预测收益,且是股内归一化的

Gervais, Kaniel & Mingelgrin 的"高成交量收益溢价"构造的是**当天/当周成交量相对该股自身一段历史的异常程度**(不是 CV,是水平的股内标准化),发现异常高(低)成交量之后一个月收益上升(下降),方向与那段时间的收益符号一致,且无法用动量、公告、市场风险或流动性解释。这是文献里**股内时序归一化**最直接的先例,和核心 1 方向 1(`ts_rank`/`ts_zscore`/减去 `ts_med`)在构造哲学上完全一致——只是作用对象是"成交量水平"而不是"成交量粗糙度统计量"。
算子语言翻译:`sub(day_vol_proxy, ts_mean(day_vol_proxy, window))` 再标准化,或 `ts_rank(day_vol_proxy, window)`——这正是核心 1 方向 1 的字面先例,只是文献对象是 Volume 水平,我们想做的是 DW(粗糙度)的股内版本。
出处:
- 标题:The High-Volume Return Premium
- 作者:Simon Gervais, Ron Kaniel, Dan H. Mingelgrin
- 年-月:2001-06(Journal of Finance, Vol. 56, No. 3, pp. 877–919;早期工作论文版本 1998/1999,Wharton Rodney White Center)
- 来源:Journal of Finance
- 链接:https://ideas.repec.org/a/bla/jfinan/v56y2001i3p877-919.html
- verified: true(搜索结果直接给出摘要核心句:高/低成交量冲击后一个月股价升/跌,且无法被反转、公告、市场风险、流动性解释)

### 没搜到

- 没搜到专门把"成交量变异系数"与"成交量自相关结构"**分开检验、各自控制对方**的单篇论文——这正是 analysis.md §4.2 第 2/3/4 号想做但文献里还没人发表过的拆分实验;Lof & van Bommel 和 Chordia et al. 都只做了 CV 这一半,没人同时测自相关那一半并相互控制。这个空白本身是 N-1 的价值所在。

---

## 题目 3 —— 成交量爆发性的度量与持续特征化(对准核心 2、E 的外围写法)

### 处理方式 1:日内成交高度集中/爆发的机制来自流动性交易者与知情交易者的策略性择时,不是随机噪声

Admati & Pfleiderer 的理论(非实证偏度/集中度指标,但是这整条文献的机制源头)说明:**U 形/爆发式的日内成交形态是内生的策略行为**,自由择时的流动性交易者倾向于在市场"厚"的时候交易以降低对知情交易者的损失。这个机制提示:A/D(DW、skew)量到的"爆发性"背后,至少一部分是**流动性交易者的择时**,而不是信息事件本身——这与 analysis.md §1.3 把 A 解释为"CV × 自相关"的拆分是一致的经济学背景,但没有给出具体的偏度/峰度/集中度构造方式。
算子语言翻译:无直接可翻译的构造(这是纯理论机制论文),但作为"为什么要把 A 拆成两半分别检验"的机制背书。
出处:
- 标题:A Theory of Intraday Patterns: Volume and Price Variability
- 作者:Anat R. Admati, Paul Pfleiderer
- 年-月:1988(Review of Financial Studies, Vol. 1, No. 1, pp. 3–40)
- 来源:Review of Financial Studies
- 链接:https://academicnewsletter.sufe.edu.cn/info/355980
- verified: true(搜索结果直接给出发表信息与机制描述:流动性交易者策略性择时产生 U 形集中模式)

### 处理方式 2:成交集中度可以用 Gini 系数量化"少数大单 vs 大量同质小单",而不是用偏度/峰度

Shakeel & Srivastava 对印度股指期货日内数据用 **Gini 系数**衡量"这段时间的成交是来自大量小额同质交易、还是少数大额交易",是偏度/峰度之外的另一条度量路线,且天然在 [0,1] 有界,不会像高阶矩那样被极端值主导。
算子语言翻译:如果要在"爆发性"这件事上找偏度/峰度的替代写法,Gini 的算子化大致是"把一个窗口内的分钟成交量排序后算 Lorenz 曲线下面积",比峰度/偏度更鲁棒但实现成本更高;本轮性价比不一定高,先记录为备选。
出处:
- 标题:Determinants of Intraday Market Liquidity: An Empirical Analysis of Indian Futures Market Using High Frequency Data
- 作者:Moonis Shakeel, Bhavana Srivastava
- 年-月:2020(International Journal of Management Practice, Vol. 13, No. 2, pp. 178–199)
- 来源:International Journal of Management Practice(Inderscience)
- 链接:https://ideas.repec.org/a/ids/ijmpra/v13y2020i2p178-199.html
- verified: true(搜索结果直接给出标题、作者、期刊、Gini 构造描述;全文在付费墙后未核实具体数字)

### 处理方式 3:把横截面特征做成"股内时序标准化"版本,样本外风险调整收益系统性更好、和截面版本相关性低

MSCI 的从业者研究直接做了"截面版本 vs 股内时序版本"的头对头比较(用的是估值比率,不是成交量,但方法论完全是我们想要的那种对照):**股内版本**是把每只股票自己的特征值在**自身过去 5 年的日度历史**里做 z-score;**截面版本**是在同一时点对同一批股票做 z-score。20 年的回测里,股内版本的风险调整收益更稳定(两个十年子期都更一致),两个版本之间的暴露相关性很低(说明确实抓到了不同的信息),简单平均两者的组合收益更高但风险调整后不如纯股内版本。**这直接支持 analysis.md 核心 1 方向 1 的判断方向**:股内归一化值得单独试,而不是只是截面排名的一个变体。
算子语言翻译:`in_zscore`(或 `sub` + `div` 自行构造的股内 z-score,窗口取 1 年左右,文献用 5 年)去标准化 `day_durbin_watson(Volume)` / `day_skew(Volume)`,再与截面版本的相关性对照;这正是 analysis.md §4.1 方向 1 的字面依据之一。
出处:
- 标题:The Theory of (Value) Relativity
- 作者:Waman Virgaonkar, Mehdi Alighanbari
- 年-月:2021-05
- 来源:MSCI Research Insight(从业者研究,非同行评审期刊)
- 链接:https://www.msci.com/research-and-insights/blog-post/the-theory-of-value-relativity
- verified: true(WebFetch 直接核实作者、日期、方法与发现)

### 处理方式 4:偏度作为"赌博偏好"的代理,在中国市场显著负向定价,但文献用的是收益偏度,不是成交量偏度

Yao, Wang, Cui & Fang 用"特异性偏度"(idiosyncratic skewness,基于收益,不是成交量)作为赌博偏好代理,发现中国市场显著的"高偏度、低后续收益"效应,并归因于个人投资者的注意力交易和套利限制。这给出一个**需要小心区分的边界**:核心 2(`ts_med(day_skew(Volume), 30)`)量的是**成交量的偏度**,文献里更成熟、更多被研究的是**收益的偏度**——两者经济含义不同,不能把后者的显著结果直接当作前者"有 alpha"的证据,只能当作"偏度类特征在中国市场确实能定价"的背景支持。
算子语言翻译:无直接翻译,是一个边界提醒,不是构造方式;但文献没有报告偏度的具体滚动窗口/股内 z-score 细节(摘要未提供,全文受限,无法核实),所以 analysis.md 核心 2 提出的"中位数平滑窗口 10/30/60 对照"仍是我们自己要做的实验,没有文献先例可直接照搬。
出处:
- 标题:Idiosyncratic Skewness, Gambling Preference, and Cross-Section of Stock Returns: Evidence from China
- 作者:Shouyu Yao, Chunfeng Wang, Xin Cui, Zhenming Fang
- 年-月:2019-01(Pacific-Basin Finance Journal, Vol. 53, pp. 464–483)
- 来源:Pacific-Basin Finance Journal
- 链接:https://ideas.repec.org/a/eee/pacfin/v53y2019icp464-483.html
- verified: true(WebFetch 核实标题、作者、期刊、卷期页码与摘要大意;偏度的具体构造窗口未能核实,全文受限)

### 没搜到

- 没搜到任何论文直接用 Herfindahl/HHI 指数去量化"日内成交量的集中度"并当作可交易特征(只找到 Gini 这个邻近替代,以及一篇研究经纪商层面成交集中度的台湾论文,但该文作者信息无法确认,未计入上面的出处,记为搜不到)。
- 没搜到直接比较"滚动均值 vs 滚动中位数"两种平滑方式对样本外表现差异的论文(MSCI 的对照是"截面 vs 股内",不是"均值 vs 中位数"这个维度);`ts_med` vs `cross_mean` 的选择在文献里没有直接依据,仍需靠我们自己的敏感性测试。

---

## 题目 4 —— 涨跌停 / 板块 / 上市年龄对成交量日内形态的改变(对准 N-2)

### 处理方式 1:临近涨跌停时成交强度与价格波动系统性改变,且涨停与跌停不对称

Wong, Liu & Zeng 用上证的逐笔数据发现:临近涨跌停时价格逼近限价的速度变快、交易强度上升、价格波动加大(支持"磁吸效应");但涨停和跌停不对称——**跌停附近成交量和单笔成交规模反而下降、价差走宽**(可能是个人投资者恐慌性观望或知情交易者策略性撤单)。这是一个明确的**处理建议**:A/D 这类成交量形态特征,在临近涨跌停(可以用 `LimitWidth` 配合当日涨跌幅算出"距涨跌停还有多远")时会被系统性扭曲,而且扭曲方向在涨停和跌停两侧不同,不能只加一个"距离限价"的线性控制,要分方向处理。
算子语言翻译:构造 `distance_to_limit = f(Close, LimitWidth, 昨收)`,再按涨停侧/跌停侧分别和 `day_durbin_watson(Volume)` 交互,或直接把该距离及其符号作为条件变量去看 A 在两侧是否对称。
出处:
- 标题:Can Price Limits Help When the Price Is Falling? Evidence from Transactions Data on the Shanghai Stock Exchange
- 作者:Woon K. Wong, Bo Liu, Yong Zeng
- 年-月:2009-03(China Economic Review, Vol. 20, No. 1, pp. 91–102)
- 来源:China Economic Review
- 链接:https://uwe-repository.worktribe.com/output/998540
- verified: true(搜索结果直接给出标题、作者、期刊、发表日期与核心发现片段)

### 处理方式 2:次新股撞到涨跌停的概率系统性更高,原因直接归因于"上市时间短",且薄成交导致统计量在边界堆积

Wan et al. 的统计发现一批股票撞涨跌停的概率异常高,作者把原因归结为"这些股票刚上市不久";同时指出临近涨跌停的订单簿本身很薄(流动性差),这与我们 §1.3 风险 1(薄成交股在 DW≈2 处堆积)是**同一类数值现象在不同统计量上的表现**:上市时间短 → 成交稀薄 → 容易撞到各种统计量的边界(涨跌停是价格的边界,DW 是我们构造的那个比值的边界)。这给出一个具体的处理方式:**用上市年龄或成交稀薄程度做门槛筛除**,而不是事后再去解释边界堆积。
算子语言翻译:`filter(ListAge > N)` 或在因子里直接用 `ListAge` 做条件化(如 N-2 提议),是文献里确认过的、针对"次新股统计量异常"的标准处理方式之一。
出处:
- 标题:Statistical Properties and Pre-Hit Dynamics of Price Limit Hits in the Chinese Stock Markets
- 作者:Yu-Lei Wan, Wen-Jie Xie, Gao-Feng Gu, Zhi-Qiang Jiang, Wei Chen, Xiong Xiong, Wei Zhang, Wei-Xing Zhou
- 年-月:2015-04(PLoS ONE, 10(4):e0120312)
- 来源:PLoS ONE
- 链接:https://pmc.ncbi.nlm.nih.gov/articles/PMC4395215/
- verified: true(WebFetch 直接核实标题、作者、期刊、日期;"次新股撞限价概率高、归因于上市时间短"与"限价附近订单簿薄"均在全文摘要/正文片段中直接看到)

### 处理方式 3:研究涨跌停效应时,文献的标准做法是直接把刚上市的股票整批剔除,而不是控制上市年龄

Bao (2023) 研究创业板涨跌幅从 10% 放宽到 20% 的政策实验时,**直接剔除了上市不满约 100 个交易日的新股**(因为它们適用注册制下不同的上市规则,会和限价放宽的效应混在一起),再在事件窗口 [-1, +10] 内用标准化的日成交量检验"交易干扰假说",发现效应在价格下跌时更强(不对称,与处理方式 1 呼应)。这给出一个比"控制 ListAge"更干脆的处理方式:**直接设阈值剔除次新股**,是已发表研究验证过的做法。
算子语言翻译:`ListAge > ~100 交易日` 作为硬性筛选阈值(而不是作为连续控制变量放进因子),以及"事件窗口内标准化成交量"(`day_volume / ts_mean(day_volume, 过去N天)`,在限价事件发生日附近取窗口)的构造方式。
出处:
- 标题:Effectiveness of Price Limits: Evidence from China's ChiNext Market
- 作者:Bao Qi
- 年-月:2023-06(PLoS ONE, 18(6):e0287548)
- 来源:PLoS ONE
- 链接:https://pmc.ncbi.nlm.nih.gov/articles/PMC10289463/
- verified: true(WebFetch 直接核实标题、作者、期刊、发表日期、剔除新股的阈值、事件窗口检验设计与"未发现磁吸效应、跌价时交易干扰更强"的结论)

### 处理方式 4:大户在涨停附近有可预测的次日卖出行为,本身是一种"距涨停远近 → 次日成交/流向"的条件化构造

Chen, Gao, He, Jiang & Xiong 用深交所账户级数据发现:大投资者倾向于在股票逼近涨停时买入、第二天卖出,这种群体行为本身把价格推向涨停(磁吸效应的一种微观解释),是一种破坏性而非稳定性的交易策略。这提示一个具体可做的条件化特征:**"昨日收盘价/成交是否贴近涨停"这个二元或连续状态,对次日成交量形态有预测力**。
算子语言翻译:用 `LimitWidth` 和前一日 Close 构造"昨日是否贴近涨停"的指标,再看它对今日 `day_durbin_watson(Volume)` 等形态特征的条件化作用,或者直接把这个指标纳入 N-2 的候选树。
出处:
- 标题:Daily Price Limits and Destructive Market Behavior
- 作者:Ting Chen, Zhenyu Gao, Jibao He, Wenxi Jiang, Wei Xiong
- 年-月:2017-11(NBER Working Paper No. 24014;正式发表版 Journal of Econometrics, Vol. 208, No. 1, pp. 249–264, 2019-01)
- 来源:NBER Working Paper / Journal of Econometrics
- 链接:https://www.nber.org/papers/w24014
- verified: true(搜索结果直接给出工作论文编号、日期、正式发表信息,以及"账户级数据研究 10% 涨跌停"的主题描述)

### 没搜到

- 没搜到任何论文专门把 **BoardCode**(主板/创业板/科创板/ST)当作条件变量去系统性解释成交量日内形态差异的研究(涨跌停宽度不同本身会导致 BoardCode 和 LimitWidth 高度共线,这点文献里没人单独拆开过)。
- 没搜到专门研究 ST 股票的异常交易量形态(而非价格异常)的学术论文——搜索结果全是近两年的交易所公告和新闻(2024–2026),不满足发表时间要求,也不是同行评审研究,**明确记为搜不到**,不得作为出处使用。

---

## 附:本次检索方式说明

所有检索均通过 WebSearch(多数为 standard 模式)与 WebFetch 完成;对每条拟采用的出处,优先用 WebFetch 直接打开原文页面或可靠的书目记录站点(IDEAS/RePEc、PMC、机构仓库、期刊官方页)核实标题、作者、年月与关键结论,未能打开全文的在对应条目里注明"全文受限,未核实到具体数字"。日期一律以论文/工作论文的**首次公开版本**为准;Lof & van Bommel 与 Chen et al. 两篇都存在"工作论文版本早于截止日、正式期刊发表版本晚于或接近截止日"的情况,本文献综述只引用、只依赖其**工作论文版本**的内容和日期。
