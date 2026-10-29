# 文献:种子 803,C 组,第 2 轮(文献员)

查的题目来自 `r2/analysis.md` §5 的 L1–L4。L1 对准第 0 节的判决(两个最高分 head 的「偏度」实际是已实现方差的三阶中心矩,凸度次数 6/36);L2 对准核心 ②`day_centroid(Amt)` 与 N-甲(成交时点 / 量价领先滞后);L3 对准核心 ①`day_hurst(Close)`(日内价格路径形状);L4 对准 N-乙与第 3.3 节的判决(零收益分钟对高阶矩的贡献:个数 vs 排列)。

只用这次用 WebSearch / WebFetch 实际检索到、能确认首版日期早于 **2023-08-08** 的论文 / 工作论文 / 研究报告;日期拿不准的一律不用,在对应小节写明「搜不到」。下面每条「处理方式」后用 `[Sx]` 指向文末出处表;`verified: true` = 这次搜索结果或抓取的页面上确实看到了标题、作者、年份、出处(至少其中大部分),不是凭记忆写的。本次没有写 `verified: false` 的条目——搜不到或细节没对上的,直接在正文说明,不列入出处表当证据。

---

## L1 —— 对准第 0 节:已实现方差的时间序列形状当截面变量,高阶矩之前先不先归一化

**能翻译成算子语言的处理方式:**

1. **先把已实现方差(或其标准差)取 log,再做任何后续统计处理,是这条文献线里的标准配方,不是我们自创的稳健化**。Andersen, Bollerslev, Diebold & Ebens(2001)用道琼斯成分股的高频分笔数据构造日度已实现方差,发现:原始已实现方差 / 协方差的无条件分布强烈右偏,而**对数**已实现标准差(以及按已实现标准差标准化后的收益)近似高斯;他们后续的时序建模全部建立在 log(RV) 上,不是原始 RV 上。→ 翻译:对 `day_durbin_watson(Open)` 这类已实现方差代理做 `ts_skew`/`ts_std` 之前先取 log,正是这条文献的标准配方,对应我们 R 组 A1(`ts_skew(log(DW(Open)),50)`)、A3(`ts_std(log(DW(Open)),50)`)。但要如实说明:该文献关心的是 RV **本身**(均值、自相关)该不该先取 log,没有讨论"50 日窗口内 RV 序列的三阶矩"这个更高阶的具体构造该怎么归一化——log 变换是我们从"让 RV 近似正态"这个更基础的结论外推过来的,不是文献直接给出的针对三阶矩的处理方案。[S1]
2. **"过去一段时间里最极端的一次值"作为独立于整体水平的截面预测变量,文献里有先例,但对象是收益不是波动率**:Bali, Cakici & Whitelaw(2011)用过去一个月日收益率的**最大值**(MAX)做截面排序,发现 MAX 越高、未来收益越低(最低与最高 MAX 十分位差超过 1%/月),且在控制规模、账面市值比、动量、短期反转、流动性、**以及用 Fama-French 三因子回归残差算出的特质波动率**之后依然显著;更关键的是,**加入 MAX 之后,特质波动率异象本身的方向被逆转**——说明"极端单日值"与"整体波动水平"在他们的设定里不是同一个东西,控制了后者,前者仍有净的、方向可能相反的信息。→ 这给第 0 节"m3 读的是窗口内最大波动日"这个判读一个方法论上的类比:**控制整体水平后,"窗口内最大值"这个构造是否还有信息,文献里确实检验过,且答案是"有,方向甚至可能反向"**。但要如实说明:MAX 度量的是最大**收益**,不是最大**已实现方差**;把这个逻辑搬到"过去一个季度最大的单日已实现波动"上,是我们自己的类比迁移,不是文献直接检验过的对象。[S2]
3. **"vol-of-vol" 这个名字在文献里对应的是期权隐含波动率的波动率,构造方式和我们完全不同**:Baltussen, van Bekkum & van der Grient(2018,JFQA)把 vol-of-vol 定义成"过去一个月里每日期权隐含波动率(IV)变化的标准差"(IV 序列本身的离散度,不是已实现方差序列的高阶矩),发现高 vol-of-vol 股票跑输低 vol-of-vol 股票约每年 8%,效应在卖空约束高的股票里更强,与低贝塔、高 IVOL 异象有重叠。→ 这给"vol-of-vol"一个真实的文献对应物,但**构造方式(期权隐含 IV 的标准差)和我们"50 日 RV 序列的三阶中心矩"完全是两回事**,前者测的是"市场对未来波动的预期本身有多不稳定",后者测的是"过去已实现的波动序列的形状"——这个词不能直接借用其文献证据来支持我们的构造。[S3]
4. **一般统计学证据:经典(未归一化)样本偏度 / 峰度对极端值高度敏感,这是促使稳健化测度出现的直接动机**:Kim & White(2004,Finance Research Letters)系统比较了基于原始矩的经典偏度 / 峰度与基于分位数的稳健测度,用标普 500 做实证,出发点正是"经典矩测度被少数极端观测主导,在小样本窗口里不可靠"。→ 方向一致但不是精确证明:它证明了"原始矩类统计量被极端值支配"是业界公认的问题(促使他们改用分位数),但**没有证明**"小标准差窗口下未归一化三阶矩严格等价于窗口最大值"这个我们自己用算术验证出来的精确命题(秩相关 0.992)——那个精确命题是本轮结构解剖员自己做的数值实验,文献只提供了"这类问题确实存在、确实促使别人换了测度"这个背景支持。[S4]
5. **低波动异象多头腿在 A 股的表现:样本结束于 2018 年末,结论是"最稳的那端赢"**:Robeco 首席研究员 David Blitz(2021-05)的研究报告用 2000 年 12 月至 2018 年 12 月的 A 股数据构造 Fama-French 式波动率因子,发现**风险最低的股票组收益最高**,该效应由波动率本身驱动而非市场贝塔,扣除投资与盈利因子后依然存在,且在最大、最流动的股票里也存在(排除流动性解释);作者把驱动力归于以散户为主导的行为偏差。页面摘要层面**没有给出多头腿单独的具体数字**,完整的收益分解需要查原始研究报告全文。[S5]

**搜不到 / 弃用的部分**:没有找到任何文献明确说"未归一化的三阶矩在截面上几乎等价于窗口内最大值"这个精确命题——这是本轮结构解剖员自己的数值发现(第 0 节,秩相关 0.992),不是文献结论,写计划时不能把这条归因给文献。也没有找到专门针对"**已实现方差时间序列本身**"(而不是期权隐含 IV,也不是收益本身)的时序高阶矩作为截面预测变量的论文——"vol-of-vol" 这个名字在文献里全部指向期权隐含波动率,这个空白本身值得写进 notebook:L1 如果真要做出一个干净的 head,我们是在填一个文献也没填的空白,不是在复刻已知异象。

---

## L2 —— 对准核心 ②`day_centroid(Amt)` 与 N-甲:成交的日内时点当截面因子,以及它与价格时点的领先滞后

**能翻译成算子语言的处理方式:**

1. **成交量的日内 U 型(开盘高、午间低、收盘回升但通常不到开盘高度)是业界公认的经验事实,且有竞争性的理论解释**:Jain & Joh(1988,JFQA)用 NYSE 按小时数据报告了显著的 U 型成交量模式,并发现同小时的收益—成交量相关性能持续到滞后 4 小时,正收益时的量价关系比负收益时更陡;Admati & Pfleiderer(1988,RFS)给出一个 Kyle 式理论模型:U 型来自交易者在市场关闭期间积累的需求冲击,知情交易者会"搭便车"躲在流动性交易高峰里下单。→ 翻译:这支持"把一天切成几段分别统计成交量、再看相对位置"这个大方向,但**两篇论文都没有把"成交量的日内时间重心"压缩成单一截面标量**——它们描述的是**群体层面的形状**(整个市场 / 整个样本在每个时段的平均成交量),不是"每只股票每天一个数"。[S6][S7]
2. **"知情交易者倾向于把单子拆小、躲在交易活跃的时段里下单"(stealth trading),但原文没有量化到"几点钟"**:Barclay & Warner(1993,JFE)发现虽然多数成交笔数是小单,但**价格变动的累积贡献主要来自中等大小的成交单**,机制解释是大单会暴露信息、小单效率太低,中等单是"隐身"的最优选择。→ 这给"知情交易会在时点选择上留下指纹"提供理论支持,但**对象是单子大小而不是单子的时间点**,不能直接当成"成交重心偏早 / 偏晚 = 知情交易"的证据——这一步是我们自己的推断,文献没有做。[S8]
3. **半小时级的日内收益存在"隔日同一时段"的持续性,但成交量 / 不平衡 / 波动率的日内形态并不能解释这个收益模式**:Heston, Korajczyk & Sadka(2010,JF)发现整数个交易日间隔(如前一天同一个半小时)的收益会延续约 40 个交易日,效应在开盘和收盘前后半小时最强;他们明确检验过**成交量、订单不平衡、波动率、买卖价差**,发现这些量也呈现相似的日内模式,但都**解释不了**收益的这个模式。→ 对我们最直接的提醒:**"日内时点"本身在文献里被证明是一个独立于成交量 / 波动率形态的收益通道**,这支持"时点类因子不会被五个控制里的流动性 / 波动吃掉"这个预期;但同时也提醒**真正驱动他们那个异象的不是成交量的时点,是收益本身按半小时格的自相关**,机制不同,不能照搬这篇的"为什么"来解释 `day_centroid`。[S9]
4. **中国 2018 年收盘集合竞价改革:确认了"尾盘成交结构被改变"这件事本身,没有检验收益可预测性**:Han, Zhao, Chen & Guo(2022,Pacific-Basin Finance Journal)用上交所 2018-08-20 实施的收盘集合竞价作为自然实验(连续竞价从 13:00–15:00 缩短到 13:00–14:57,14:57–15:00 改为集合竞价),发现改革**把成交量从收盘时刻推到了收盘前夕**(pre-closing),收盘价连续性显著改善,对小盘股的影响更明显,但对整体市场流动性**没有显著影响**。→ 这确认了我们样本期内(2018-08-20 之后)尾盘成交的"时点"确实发生过一次结构性搬移,`day_centroid(Amt)` 这类变量在改革前后应该有一个均值跳跃——**这是写计划时该交代的一个数据细节,不是因子机制的证据**,论文没有测试这个搬移后的量是否预测收益。[S10]

**搜不到 / 弃用的部分**:没有找到任何论文直接构造"成交的时间重心"(或类似的单一标量化日内时点指标)并把它当成截面预测变量来检验——U 型模式的描述全部停留在"群体 / 时段均值"层面,没有人把它压缩成逐股票逐日的一个数。也没有找到专门度量"成交时点与价格移动时点的领先滞后"的论文,最接近的是 Hasbrouck(1991,*Journal of Finance* 46(1):179–207)的交易—报价 VAR 冲击响应框架,但它测的是"一笔交易对价格的最终影响有多大、要多久完全反映",不是"一天里量和价各自'重心'谁先谁后",两者翻译不过去,**不列入出处表当直接证据**。核心 ②与 N-甲这两个构造(成交时间重心、量价时点领先滞后)在文献里基本是空白,不是在复刻已知异象。

---

## L3 —— 对准核心 ①`day_hurst(Close)`:日内价格路径形状作为个股特征,而不是市场有效性检验工具

**能翻译成算子语言的处理方式:**

1. **Hurst / R-S 应该算在收益(或对数收益)上而不是价格水平上,这是这条文献线反复强调的前提**:标准处理是先把价格差分成收益序列、再对收益序列做 R/S,理由是价格本身是单位根式的随机游走,**直接对价格水平做 R/S 会读到接近 1 的 H,反映的是价格序列本身的"积分 / 非平稳"性质,不是收益里的真实记忆**。这正中我们头号风险:`day_hurst(Close)` 作用在**分钟价格水平**上,不是分钟收益上;核心卡里"随机游走给出 H=0.7465"这个算术结果,与"直接对价格做 R/S 系统性偏高"这个方向完全一致。(如实说明:这条处理规范在多处 R/S 方法说明与软件实现文档里反复出现,但本次没有检索到以这句话为核心论点、且满足日期要求的论文/工作论文原文,**不单独列出处**,只作为背景提醒写进风险段。)
2. **稀疏交易 / 非同步交易会系统性压低方差比类统计量,标准修正是显式建模"不交易概率"**:Lo & MacKinlay(1990,*Journal of Econometrics*)把非同步交易建模成一个带随机"审查"的采样过程,证明非同步交易会在个股和组合收益的方差与自相关里留下可检验的印记(买卖价差反弹和非同步交易会把方差比往下推,即使市场是有效的),并给出用"不交易概率"反推、修正偏误的方法。→ 翻译:这是"按成交活跃度分桶再比较"(核心①外围清单第①条:`cs_bucket_rank(day_hurst(Close), cross_mean(day_zero_ratio(Ret),20))`)这个处理思路的理论来源——先承认稀疏交易会系统性污染这类统计量的方向,再按稀疏度分组,而不是整体中性化掉它。[S11]
3. **修正短程相关性对 R/S 的污染,标准做法是把窗口长度相关的截断阶数作为可调参数显式建模,不是换一个完全不同的统计量**:Lo(1991,*Econometrica*)把经典 R/S 统计量加一个依赖截断阶数 q 的修正项(用 Newey-West 式加权自协方差替换简单标准差),证明修正后的统计量在"存在短程相关但没有真正长记忆"的数据上不再虚假地显示长记忆;用这个修正统计量重新检验美股日度/月度收益,**一旦控制了短程相关,长记忆的证据消失**。→ 对我们的直接提醒:`day_hurst` 如果用的是未修正的经典 R/S,它可能把"价格里正常的短程自相关(例如微结构噪声导致的负自相关)"错读成"趋势记忆",这是另一条独立于"稀疏度"的污染通道,目前核心①的外围清单里没有人在处理这个。[S12]
4. **经典 R/S 估计量在小样本下有偏,偏向 H≈0.7(不是 0.5)**:Couillard & Davison(2005,*Physica A* 348:404–418)重新推导了 R/S 统计量的精确显著性检验,其结论(被多篇后续文献转述确认)是经典最小二乘 R/S 估计量在小样本下存在系统偏误,**对纯随机数据也会读出明显偏离 0.5、偏向 0.7 附近的 H 值**。→ 这给"短窗口(约 241 根分钟)估计 Hurst 的噪声有多大"一个比上一轮(r1,Barunik & Kristoufek 2012,只给出警告)更具体的量级提示:**偏误的方向是系统性地偏高、不是对称噪声**,意味着 `day_hurst(Close)` 的截面均值本身可能就有一个正的偏误基线,跟股票真实的路径形状无关,只跟"241 个点是不是足够大的样本"有关。(本条经由多个搜索结果转述确认标题、作者、年份、期刊卷期,未直接抓取论文全文。)[S13]
5. **把"摩擦 / 非同步"直接压缩成一个标量化的截面特征,并证明它本身能预测收益,是有先例的,但构造方式和 R/S 完全不同**:Hou & Moskowitz(2005,RFS)的 price delay 用"只用同期市场收益"与"再加四周滞后市场收益"两个回归的 R² 之比构造一个"价格反应滞后程度"的标量,发现延迟越大的股票未来收益越高,CAPM、三因子、四因子都解释不了。→ 这给"把一个难以直接解释的微结构统计量压缩成截面排序变量、然后期待它预测收益"这整条路径一个成功先例,但**它的具体构造(两个回归的 R² 比)跟 R/S / Hurst 完全不是一回事**,不能把 price delay 的显著性直接当成 Hurst 会显著的证据,只能当成"这类摩擦代理值得一试"的背景支持。[S14]
6. **业务时间(用方差驱动的"钟"而不是日历时间)采样,目前文献给出的改进版本是"先用跳跃稳健的已实现波动率估计时变方差,再反推业务时间转换函数"**:Dong & Tse(2017,*Econometrics*,MDPI)提出的改进版业务时间采样,先用跳跃稳健方法估计日内积分波动率,构造一个时间变换函数,再用其反函数抽取"业务时间"上的价格点;蒙特卡洛显示这样抽出来的收益更接近正态,已实现波动率估计的均方误差更小。→ 对我们 N-丙(留给第 3 轮的"诚实波动形状族")和核心①外围清单第④条(按未复权成交量 / 成交额分桶)都是一个直接可用的构造模板:**不是简单地把"分钟"换成"每 N 笔成交",而是先估计活跃度再按活跃度反推采样点**,这比我们目前"按 `cross_mean(day_zero_ratio)` 分桶"更精细,但也更难在我们的算子库里实现(需要一个"反函数采样"原语,目前没有)。[S15]

**搜不到 / 弃用的部分**:没有找到一篇专门把 Hurst 指数 / R-S / 方差比当成**个股截面特征去排序选股**(而不是当市场有效性检验工具)并报告 Fama-MacBeth 或分组收益的论文——这个空白在 r1 已经记录过,本轮再次确认,没有新证据推翻它。这意味着**核心①如果真的产出 head,我们是在做文献没有直接做过的事**,这件事应该写进本轮计划给审计员看(呼应规则 §3 创新度评分表"4 分 = 输入与机制都不同,库里和文献里都没有的机制"),但也要如实说:**它目前的合理度证据链只到"机制清楚 + 算子实现了它"这一档**,没有文献的直接正面支持,顶多靠 Lo(1991)/Lo-MacKinlay(1990)的"为什么要修正"侧面支撑,够不上"再加上文献证据"这一档。

---

## L4 —— 对准 N-乙与第 3.3 节的判决:零收益分钟对高阶矩的贡献,"个数" 与 "排列" 之分

**能翻译成算子语言的处理方式:**

1. **"零收益比例"当独立的流动性 / 摩擦代理,是最成熟的处理方式,直接可当控制或排序对象**:Lesmond, Ogden & Trzcinka(1999,RFS)把一段时间内零收益天数的占比当成交易成本的隐含估计量;Bekaert, Harvey & Lundblad(2007,RFS;NBER WP 11413,2005)在新兴市场里把同一个比例(ZEROS,月度零收益天数占比,右偏修正后)直接当月度流动性因子,发现它比换手率更能预测下月收益。→ 与 r1 已经记录的处理完全一致(`cross_mean(day_zero_ratio(Ret),20)`),本轮重新确认:**两篇论文处理的都是"个数"(占比),不是"排列"**。[S16][S17]
2. **零成交量的"个数"也被单独做成过标准化流动性因子,但一样是数个数,不看排列**:Liu(2006,JFE)提出 LM12,用过去 252 个交易日里**零成交量天数的、按换手率调整过的标准化计数**当流动性因子,解释力度在美股里比换手率、Amihud 比率等更强,机制解释是"锁定风险"(极端情况下卖不出去)。→ 这进一步确认"零 ××× 的个数"是文献里反复出现、反复有效的一条处理路径,但**它量的是零成交量(不是零收益),而且仍然只数个数,不问这些零值天 / 分钟在时间上连续还是分散**。[S18]
3. **游程长度(同一状态连续持续了多久),而不是零值的个数,被直接构造成一个独立的流动性因子,并证明它能定价**:Das & Hanouna(2010,*Annals of Operations Research* 176(1):127–152)提出"run length"概念,**不是数零收益 / 零成交的个数,而是量每一段"价格 / 收益维持同一状态"能持续多少个观测**,用日度股票数据(1962–2005)构造一个市场层面的游程长度流动性风险因子,发现它在标准资产定价模型里能被定价;并证明个股游程长度与换手率负相关、与买卖价差和价格冲击正相关,且这个关系对不同采样频率都稳健。→ **这正是 L4 问的"个数 vs 排列"区分在文献里的直接对应**:`day_zero_ratio` 是"个数"路径,`day_flat_run_max(Ret)`(最长静止段)是"排列"路径,后者在文献里有独立的、不依赖前者的定价证据。这是本轮最值得直接写进计划的一条。[S19]
4. **用"交易时间"(以成交笔数为钟)而不是日历时间重新测量收益,日历时间下的尖峰厚尾("峰度几乎总是大于 3")在交易时间下会显著缓解**:Westerfield(1977,JFQA)系统比较了日历时间与交易时间下的收益分布,发现**按日历时间测量的价格变动,其样本峰度几乎总是大于 3**(尖峰厚尾),这与 Clark(1973,*Econometrica* 41(1):135–155)被成交量 / 成交笔数这个随机"子母钟"驱动的布朗运动模型(可同时解释厚尾和序列依赖)是同一条线的互相印证。→ 翻译:这是对第 3.3 节"把钟表口径换成成交口径,同一个矩统计量的截面预测力大幅下降"这个经验发现最直接的理论解释——**不是我们的奖励构造偶然发现了这一点,这正是"钟表时间的高阶矩天然比交易时间的高阶矩更夸张"这条已经被研究近 50 年的机制**,`sub(day_kurt(Ret), day_kurt(in_logchg(Vwap,1)))`(钟表峰度减交易峰度)这个构造,翻译过去就是在量"子母钟理论预言的那部分差异"。[S20][S21]

**搜不到 / 弃用的部分**:没有找到任何论文直接比较"同一个高阶矩统计量,剔除无成交分钟前后"的截面预测力变化(即直接检验"预测力来自零质量本身,而不是整条排序"这个我们自己在 r1 的 R 里验证出来的判决)——Das & Hanouna 的游程因子和 Lesmond / Bekaert 的零比例因子都是独立构造的新因子,不是"对同一个因子做剔除前后对照"的实验设计。这个对照实验(把 Vwap 口径和钟表口径的峰度相减)本身,目前看是我们自己在做,文献没有先例。

---

## 出处(按正文出现顺序编号,`verified` 均为本次搜索 / 抓取中实际看到)

[S1] Torben G. Andersen, Tim Bollerslev, Francis X. Diebold, Heiko Ebens. 2001. "The Distribution of Realized Stock Return Volatility." *Journal of Financial Economics*, 61(1), 43–76. 确认来源:https://www.kellogg.northwestern.edu/faculty/research/detail/2001/the-distribution-of-realized-stock-return-volatility/?p=1 。verified: true(已直接抓取页面核实标题、作者、期刊、核心发现)

[S2] Turan G. Bali, Nusret Cakici, Robert F. Whitelaw. NBER WP 14804,2009-03;发表 2011. "Maxing Out: Stocks as Lotteries and the Cross-Section of Expected Returns." *Journal of Financial Economics*, 99(2), 427–446. NBER: https://www.nber.org/papers/w14804 。verified: true(已直接抓取 NBER 页面核实标题、作者、日期、核心发现)

[S3] Guido Baltussen, Sjoerd van Bekkum, Bart van der Grient. 2018-08. "Unknown Unknowns: Uncertainty About Risk and Stock Returns." *Journal of Financial and Quantitative Analysis*, 53(4), 1615–1651. 作者页面 PDF:https://personal.eur.nl/vanbekkum/2018JFQA_unknown_unknowns.pdf ;Cambridge 记录:https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/unknown-unknowns-uncertainty-about-risk-and-stock-returns/6E0E98349D20C1DCF67F3A0452361B80 。verified: true(搜索结果中看到标题、作者、期刊卷期、核心数字即每年约 8% 的多空收益)

[S4] Tae-Hwan Kim, Halbert White. 2004-03. "On More Robust Estimation of Skewness and Kurtosis." *Finance Research Letters*, 1(1), 56–73. IDEAS 记录:https://ideas.repec.org/a/eee/finlet/v1y2004i1p56-73.html 。verified: true(搜索结果中看到标题、作者、期刊卷期页码、研究动机)

[S5] David Blitz. 2021-05-19. "The Low Volatility Effect in China." Robeco Insights(研究报告). https://www.robeco.com/en-int/insights/2021/05/the-low-volatility-effect-in-china 。verified: true(已直接抓取页面核实标题、作者、发布日期、样本区间、主要结论;页面未给出多头腿单独的具体收益数字)

[S6] Anat R. Admati, Paul Pfleiderer. 1988. "A Theory of Intraday Patterns: Volume and Price Variability." *The Review of Financial Studies*, 1(1), 3–40. 摘要来源:https://academicnewsletter.sufe.edu.cn/info/355980 。verified: true(本轮搜索结果再次看到标题、作者、期刊、核心机制描述)

[S7] Prem C. Jain, Gun-Ho Joh. 1988-09. "The Dependence between Hourly Prices and Trading Volume." *Journal of Financial and Quantitative Analysis*, 23(3), 269–283. https://resolve.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/dependence-between-hourly-prices-and-trading-volume/C305DB5BFB5F2B2D803BB94449AF8B47 。verified: true(本轮搜索结果再次看到标题、作者、期刊、U 型与滞后相关性的具体描述)

[S8] Michael J. Barclay, Jerold B. Warner. 1993. "Stealth Trading and Volatility: Which Trades Move Prices?" *Journal of Financial Economics*, 34(3), 281–305. DOI 10.1016/0304-405X(93)90029-B。verified: true(搜索结果中看到标题、作者、期刊卷期页码、DOI,以及"中等大小交易贡献大部分累积价格变动"的核心发现)

[S9] Steven L. Heston, Robert A. Korajczyk, Ronnie Sadka. 2010-08. "Intraday Patterns in the Cross-Section of Stock Returns." *The Journal of Finance*, 65(4), 1369–1407. arXiv 版:https://ar5iv.arxiv.org/html/1005.3535 。verified: true(搜索结果与 arXiv 页面核实标题、作者、期刊卷期页码、核心发现及"成交量/不平衡/波动率解释不了收益模式"这一关键细节)

[S10] Han, Zhao, Chen, Guo. 2022. "Reexamining the Impact of Closing Call Auction on Market Quality: A Natural Experiment from the Shanghai Stock Exchange." *Pacific-Basin Finance Journal*, 74, 101821. 工作论文版:https://orca.cardiff.ac.uk/id/eprint/151359/ 。verified: true(搜索结果中看到标题、作者、期刊卷期页码、2018-08-20 改革细节与核心发现;完整作者名单本次未逐一核实全名)

[S11] Andrew W. Lo, A. Craig MacKinlay. 1990. "An Econometric Analysis of Nonsynchronous Trading." *Journal of Econometrics*, 45(1–2), 181–211(MIT 作者页面写 181–212,页码最后一位两来源不一致,引用前需核对期刊原文)。NBER WP 2960 工作论文版;MIT:https://web.mit.edu/~alo/www/Papers/lo-mackinlay-90a.html 。verified: true(多处搜索结果与作者页面核实标题、作者、期刊、核心方法与结论)

[S12] Andrew W. Lo. 1991-09. "Long-Term Memory in Stock Market Prices." *Econometrica*, 59(5), 1279–1313. https://www.jstor.org/stable/2938368 ;NBER WP 2984。verified: true(搜索结果中看到标题、作者、期刊卷期页码、核心方法——修正 R/S 统计量——与结论"控制短程相关后长记忆证据消失")

[S13] J.-F. Couillard, M. Davison. 2005. "A Comment on Measuring the Hurst Exponent of Financial Time Series." *Physica A*, 348, 404–418. IDEAS 记录:https://ideas.repec.org/a/eee/phsmap/v348y2005icp404-418.html 。verified: true(多篇搜索结果与引用它的后续论文中看到标题、期刊、卷期页码,以及"经典最小二乘 R/S 估计量在小样本下有偏、偏向 H≈0.7"这一结论的转述;未直接抓取原文全文)

[S14] Kewei Hou, Tobias J. Moskowitz. 2005. "Market Friction, Price Delay, and the Cross-Section of Expected Returns." *The Review of Financial Studies*, 18(3), 981–1020. verified: true(搜索结果中看到标题、作者、期刊卷期页码、price delay 的具体构造方式——两个回归的 R² 之比——以及核心发现)

[S15] Yingying Dong, Yiu-Kuen Tse. 2017. "Business Time Sampling Scheme with Applications to Testing Semi-Martingale Hypothesis and Estimating Integrated Volatility." *Econometrics*(MDPI), 5(4), 51. https://www2.mdpi.com/2225-1146/5/4/51 。verified: true(已看到标题、作者、期刊、核心方法——跳跃稳健估计时变方差再反推时间变换函数——与蒙特卡洛结论)

[S16] David A. Lesmond, Joseph P. Ogden, Charles A. Trzcinka. 1999. "A New Estimate of Transaction Costs." *The Review of Financial Studies*, 12(5), 1113–1141. https://www.bauer.uh.edu/rsusmel/phd/lot_1999RFS.pdf 。verified: true(本轮搜索结果再次看到标题、作者、期刊、零收益比例的构造方式)

[S17] Geert Bekaert, Campbell R. Harvey, Christian Lundblad. 2007(NBER WP 11413,2005). "Liquidity and Expected Returns: Lessons from Emerging Markets." *Review of Financial Studies*, 20(6), 1783–1831. NBER WP:https://www.nber.org/papers/w11413.pdf 。verified: true(本轮搜索结果再次看到标题、作者、ZEROS 构造方式与核心发现)

[S18] Weimin Liu. 2006-12. "A Liquidity-Augmented Capital Asset Pricing Model." *Journal of Financial Economics*, 82(3), 631–671. DOI 10.1016/j.jfineco.2005.10.001。verified: true(搜索结果中看到标题、作者、期刊卷期页码、DOI,以及 LM12(零成交量天数标准化计数)的具体构造方式与"锁定风险"机制解释)

[S19] Sanjiv R. Das, Paul Hanouna. 2010-04. "Run Lengths and Liquidity." *Annals of Operations Research*, 176(1), 127–152. DOI 10.1007/s10479-008-0508-x。verified: true(已直接抓取 IDEAS 页面核实标题、作者、期刊卷期页码、年份,以及"游程长度与换手率负相关、与价差和价格冲击正相关、该关系对采样频率稳健"的核心发现)

[S20] Randolph Westerfield. 1977-12. "The Distribution of Common Stock Price Changes: An Application of Transactions Time and Subordinated Stochastic Models." *Journal of Financial and Quantitative Analysis*, 12(5), 743–765. https://resolve.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/distribution-of-common-stock-price-changes-an-application-of-transactions-time-and-subordinated-stochastic-models/127A07EA1B24E7E70A68E77E549B42CE 。verified: true(搜索结果中看到标题、作者、期刊卷期页码、"日历时间下样本峰度几乎总是大于 3"这一核心发现)

[S21] Peter K. Clark. 1973. "A Subordinated Stochastic Process Model with Finite Variance for Speculative Prices." *Econometrica*, 41(1), 135–155. verified: true(本轮搜索结果——包括引用它的 Westerfield 论文摘要转述——中再次看到标题、作者、年份、期刊与核心机制描述;未直接抓取 Econometrica 原文)

---

## 给 PI 的汇总提醒

- **L1 最actionable的一条**:Andersen-Bollerslev-Diebold-Ebens(2001)[S1] 确认"先 log 再做后续统计"是这条文献线的标配,直接支持 R 组 A1/A3;但**没有任何文献支持"未归一化三阶矩≈窗口最大值"这个精确命题**——那是我们自己的数值发现,计划里不要写成"文献证实"。Bali-Cakici-Whitelaw [S2] 和 Baltussen 等 [S3] 都只能当类比背景,前者对象是收益不是波动率,后者构造方式(期权隐含)和我们完全不同,**不要把这两条当成"vol-of-vol 异象在我们的构造上成立"的证据**。
- **L2 最重要的发现是一个空白**:没有任何文献把"成交的日内时间重心"压缩成一个逐股票逐日的标量去做截面预测,U 型模式([S6][S7])和知情交易时点([S8])都停留在群体/机制描述层面。核心②与 N-甲**在文献里都是空白**,这件事本身该如实告诉审计员(对应创新度评分表第 4–5 档),但也意味着**合理度打分拿不到"文献证据"那一档**,只能靠机制清楚 + 算子实现这一档。Han et al.(2022)[S10] 提供的是一个数据背景提醒(2018-08-20 改革改变了尾盘成交结构),不是因子证据。
- **L3 两条最该写进计划**:① 标准处理是 Hurst/R-S 算在**收益**上、不是价格水平上(本条因找不到满足日期要求的直接论文,未列出处,只作背景提醒,但方向与我们自己"随机游走给出 H=0.7465"的算术结果一致,**风险真实存在**);② Couillard & Davison(2005)[S13] 给出一个比 r1 的 Barunik-Kristoufek 更具体的信号:短窗口 R/S 的偏误是**系统性偏高**,不是对称噪声,`day_hurst(Close)` 的截面均值可能自带一个与真实路径形状无关的正偏误基线。Lo(1991)[S12] 和 Lo-MacKinlay(1990)[S11] 分别给出"修正短程相关"和"修正非同步交易"两条独立的污染通道及其标准修正思路,目前核心①外围清单只覆盖了后者(按活跃度分桶),没有覆盖前者(短程相关修正)。
- **L4 本轮最扎实的一条是 Das & Hanouna(2010)[S19]**:它是"个数 vs 排列"这个区分在文献里的**直接对应**——`day_zero_ratio` 对应"个数"路径([S16][S17][S18] 全部是数个数),`day_flat_run_max` 对应"排列"路径([S19] 独立构造、独立证明能定价)。Westerfield(1977)[S20] + Clark(1973)[S21] 给"钟表口径峰度系统性比交易口径峰度更夸张"一个近 50 年的理论基础,直接支持 `sub(day_kurt(Ret), day_kurt(in_logchg(Vwap,1)))` 这个构造,但**没有文献直接做过"剔除无成交分钟前后对照同一个矩统计量"这个实验**,那部分判决(第 3.3 节)仍然是我们自己的发现。
- 全部 21 条出处里,没有一条是编造的;搜不到或证据不完整的分支已在正文和各节「搜不到/弃用」段如实标出。置信度最低的两条是 [S13]、[S21](均经由搜索结果/二级来源转述确认,未直接抓取论文原文全文),[S10] 的完整作者名单本次也未逐一核实。
