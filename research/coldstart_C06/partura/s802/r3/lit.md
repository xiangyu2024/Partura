# s802 / r3 文献笔记(文献员)

范围:只用 2023-08-08 之前首版/发表的论文、工作论文或研究报告。每条"处理方式"后标 `[R#]` 指向文末参考文献;每个 `[R#]` 都写了 verified。搜不到的小问题明确写"没搜到",不编。

---

## L1 —— 用信号自身的可靠度 / 信噪比做筛选或收缩

### 能翻译成算子语言的处理方式

1. **横截面分组平均,用组内平均稀释个股测量误差,而不是整体剔除低可靠度个股。**
   Black–Jensen–Scholes 的原始动机就是单只股票的 beta 测量误差会把截面回归系数往 0 拉偏;他们的修正不是"剔除噪声大的股票",而是把股票按某个外生变量(他们用的是先验 beta)分组,组内等权平均,测量误差方差按 1/L 缩小。
   算子翻译:不是 `cs_last_low20(y, 可靠度)`(硬剔除 20%),而是 `cs_group_mean(y, cs_rank_bucket(可靠度, L))` —— 对可靠度分 L 档取组内均值,保留所有股票但压低噪声档的权重。`[R1]`

2. **贝叶斯收缩:用"可靠度比"把个股估计往一个先验值拉,可靠度比 = 截面方差 / (截面方差 + 估计误差方差),是一个连续权重,不是 0/1 门槛。**
   Vasicek 对个股 beta 的处理正是这个形式:`shrunk = w·raw + (1-w)·prior`,`w` 随个股自身估计的标准误变化。
   算子翻译:`w = div(var_cross, add(var_cross, var_err(stock)))`;`y_shrunk = add(mul(w, y_raw), mul(sub(1, w), prior))`。这是 L1(b) 里"连续收缩"的标准做法,和我们现在的硬筛(20% 剔除)是同一问题的两种解法。`[R2]`

3. **用观测噪声的代理做加权最小二乘,而不是用噪声代理做剔除。**
   Asparouhova–Bessembinder–Kalcheva 处理的是价格里的短期噪声(买卖价差跳动)对收益率推断的污染;他们的修正是用前一期总收益率做权重做 WLS,噪声大的观测权重小但仍在样本里,不是被删掉。
   算子翻译:回归/合成时用 `inv(noise_proxy)` 当权重,而不是用 `noise_proxy` 当筛选阈值。这是"收缩优于剔除"在订单流/收益噪声问题上的一个具体先例,但它处理的是**价格噪声**,不是**信号自相关意义上的可靠度**,翻译时要注明这个差别。`[R3]`

4. **用"零收益天数占比"这种停滞/冻结报价频率,专门针对流动性噪声做筛选,是另一条独立于"信号自相关"的可靠度定义。**
   Lesmond–Ogden–Trzcinka 的 Zeros 度量:一段窗口内零收益日的占比,用来代理交易成本/流动性噪声,后续文献大量把它当筛选变量用。
   算子翻译:`zeros_ratio = div(day_count(eq(Ret, 0), W), W)`,和我们现在用的 `ts_autocorr(day_signed_ratio(Ret,Volume), 60, 1)` 是两种不同的"可靠度"构造——一个测的是报价是否在动,一个测的是订单流拆单信号本身在自己的时间序列上有多"粘"。两者对应不同的被剔个股群体(见下面 (d))。`[R4]`

5. **"模型选择式"检验一个新信号/新变量相对已有变量的边际贡献是否为零,而不是直接判断它单独是不是因子。**
   Green–Hand–Zhang(94 个特征的联合 Fama–MacBeth)和 Feng–Giglio–Xiu(双重选择 LASSO)都是把"这个变量加不加分"当成一个相对已知变量集合的边际检验问题,这个框架本身不区分"筛选条件"和"因子",但提供了检验(c)问的现象(单独无效、条件下有效)在方法论上怎么被规范化处理的一个参照:把筛选变量当成交互项/条件变量放进联合检验,而不是单独做收益预测回归。
   算子翻译:`screen` 的价值应该用"有 screen 的残差信号边际贡献"而不是"screen 单独预测收益"来评估——这和我们 R-B/R-C/R-D 判决性检验的设计思路一致(但这两篇都不是专门研究"筛选变量"这个主题,是泛化的因子选择方法论,翻译时要注明是类比,不是直接命中)。`[R5]` `[R6]`

6. **微盘股 / 低价股 / 停牌股的标准剔除法(市值分位数断点、NYSE breakpoint),和"可靠度筛"命中的是部分重叠但不完全相同的群体。**
   Fama–French 用 NYSE 20%/50% 市值分位数断点避免等权检验被微盘股主导;Hou–Xue–Zhang 把这套断点用在 452 个异象的复现上,发现很多异象幅度在断点之后大幅缩水。这两篇证实"剔除微盘/低价"是现成的、独立于"信号自相关"的另一条路,而且文献明确承认它和"交易成本/流动性噪声"筛(如 Zeros 度量)命中的是同一群名字(低价、低成交、低市值)。`[R7]` `[R8]`

### 对题目小问的直接回答

- **(a)** 没搜到把"一只股票自己的日度信号序列的滞后 1 阶自相关"正式定义为可靠度比的论文。最接近的类比是经典 errors-in-variables 文献里的"可靠度比"概念(`[R1]` `[R2]`),但它们算的是横截面估计误差方差之比,不是时间序列自相关;自相关当可靠度代理这个具体构造,在本次搜索范围内没有直接证据,如实写为没搜到。
- **(b)** 没搜到一篇直接对比"剔除 vs 收缩"改善幅度的论文。`[R1]` `[R2]` `[R3]` 都是用收缩/加权处理噪声而非硬剔除,但都没有报告"剔除法 vs 收缩法"的头对头夏普/alpha 对比数字。如实写为没搜到量化对比。
- **(c)** 没搜到明确讨论"同一指标单独当因子是负的、当筛选条件有用"这种现象并给出解释的文献。`[R5]` `[R6]` 提供的是方法论上的近似(把变量当条件/交互项而非独立因子来检验),但不是针对这个具体现象的讨论。
- **(d)** 被剔掉的低可靠度/低活跃度名字,在 Zeros 度量和微盘股断点两条线的文献里,被明确认定为**低价、低成交量、低市值**的股票(`[R4]` `[R7]` `[R8]`),这和标准的流动性/价格筛**是同一群名字**。但这些文献研究的是"报价是否在动"(零收益),不是我们筛的"拆单信号本身的自相关",所以"僵尸股/停牌/冻结报价"这个认定不能直接搬到我们这个筛子上,只能说两种筛子大概率有交集,没有证据说是同一机制。

---

## L2 —— 涨跌幅限制、板块、上市年龄条件下的订单流预测力(中国市场)

### 能翻译成算子语言的处理方式

1. **"磁吸效应"的度量方式是价格逼近涨跌停时的运动速度/成交强度,不是简单的"是否封板"二值。**
   上海交易所逐笔数据的磁吸效应研究发现价格临近涨跌停时,价格朝涨跌停方向移动的速度和交易强度会加快。Chen–Gao–He–Jiang–Xiong(下称 CGHJX)用账户级数据发现大户在触及涨停当天净买入、次日卖出,净买入强度直接预测随后的长期反转。
   算子翻译:定义 `near_limit = div(sub(limit_price, Close), limit_price)`(离涨跌停还有多远)和 `hit_limit = eq(Close, limit_price)`(是否封板),把订单流信号 `y` 和这两个量做交互而不是简单相减,例如 `mul(y, near_limit)` 或分桶后看 `cs_group_mean`。`[R9]`

2. **板块/制度(ST vs 非 ST,5% vs 10% 限宽)被当成自然实验分组变量,专门用来剥离"是不是规模/流动性的代理"这个混杂。**
   CGHJX 的核心识别策略正是比较 ST(5% 限宽)和非 ST(10% 限宽)股票,在控制其他特征后,限宽更紧的 ST 股票磁吸/破坏性交易更严重——这是把 `LimitWidth` 当分组/交互变量,而不是线性控制变量来用的直接先例,回应了题目最担心的"限宽本身是规模代理"这个问题:CGHJX 的设计本身就是为了把这层混杂剥开。
   算子翻译:`cs_group_by(BoardCode or LimitWidth_bucket)` 做分组交互,而不是 `cs_regres(y, LimitWidth)` 线性中性化掉它。`[R9]`

3. **投资者结构(散户 vs 机构占比)随时间和板块变化,是背景事实而非某篇论文的分组实证,目前搜到的证据只能支撑"存在差异"这个方向,不能给出订单流预测力如何随之变化的直接证据。**
   中国证监会披露的数据显示 2021 年散户交易额占比首次跌破 70%;科创板通过"港股通"渠道仅允许机构投资者参与,结构性地偏机构;创业板早年(2012 前后)的披露显示机构持仓占比在上升。这些都是投资者结构随时间/板块变化的背景事实,不是"订单流预测力 × 板块"的直接分组检验。`[R10]` `[R11]`

4. **上市年龄 / 解禁对订单流预测力的直接证据没搜到,但"限售股解禁"本身的价格冲击在中国有清晰的事件研究证据,可以作为旁证。**
   针对股权分置改革限售股解禁的研究(非 IPO 限售,但机制类似)发现解禁窗口前后出现约 -14% 的异常收益和约 140% 的成交量放大,且这个冲击即使市场完全预期到解禁日期依然存在,信息披露质量越高冲击越小。这说明"持有人基础变化"本身是能在价格/流动性上留下痕迹的,但没有证据把它和订单流信息含量直接挂钩。
   算子翻译:`days_to_unlock`(到解禁日的天数)或 `ListAge` 作为交互变量而非控制变量放进 `y`,参照 CGHJX 的分组思路。`[R12]` `[R13]`

### 对题目小问的直接回答

- **(a)** 磁吸效应文献度量"价格没能当场走完"的方式,是交易强度/价格逼近速度(`[R9]` 的上交所逐笔研究)和触及涨停后的净买入/次日反转幅度(CGHJX),不是我们字面想的"价格和限价的差"这么简单;但这差也是一个可计算的代理,文献没有排斥它,只是没直接用它。注意:磁吸效应本身在中国市场的证据并不一致(有研究支持、有研究反对,`[R9]` 本身也提到创业板 2020 年限宽从 10% 改到 20% 后没有发现磁吸效应的证据),这条机制故事不是定论,写审计材料时不能当作已证实的事实。
- **(b)** 没搜到直接把"板块投资者结构差异"和"订单流 → 收益"这条关系连起来的分组实证论文。搜到的只是投资者结构本身随时间/板块变化的背景数据(`[R10]` `[R11]`),如实写为没搜到直接证据。
- **(c)** 没搜到"上市年龄/解禁期"和"订单流预测力"直接挂钩的论文。限售股解禁的价格冲击证据(`[R12]` `[R13]`)可以类比但不是同一个问题,如实标注为旁证而非直接证据。
- **(d)** CGHJX 把 ST/非 ST(即限宽)当分组变量用,并且这个设计本身就是为了排除"限宽是规模/流动性代理"这个担心(`[R9]`)。没搜到其他论文明确指出这三个变量(限宽/板块/上市年龄)本身就是规模/流动性代理 —— 但这正是 CGHJX 设计要规避的问题,方向上支持"用分组/交互而不是线性控制"这个处理方式。

---

## L3 —— 隔夜 vs 日内收益的拉锯

### 能翻译成算子语言的处理方式

1. **标准构造:隔夜 = 昨收 → 今开,日内 = 今开 → 今收,两段相加等于当日收盘到收盘收益。**
   Lou–Polk–Skouras(下称 LPS)和 Berkman–Koch–Tuttle–Zhang(下称 BKTZ)都是这个口径,区别在于取的"开盘价"定义(集合竞价成交价 vs 开盘后第一笔成交),以及持有期:LPS 做月度十分位组合(标准动量式月度再平衡),BKTZ 用的是日度样本但看的是月度累计的隔夜/日内收益模式。
   算子翻译和我们草案一致:`隔夜 = div(day_first(Open), cross_delay(day_last(Close), 1))`,`日内 = div(day_last(Close), day_first(Open))`,两者相乘(或对数相加)应等于 `div(day_last(Close), cross_delay(day_last(Close),1))`,即标准日收益——这个恒等式是检验构造对不对的第一道校验,文献隐含用了但没有把它写成显式算子校验,这点是我们这边翻译时该加的保险。`[R14]` `[R15]`

2. **方向在美股是"隔夜延续、日内反转"(动量几乎全部来自隔夜段);但在中国 A 股,目前搜到的证据(谨慎使用)方向可能是反过来的,机制上归因于 T+1。**
   LPS 在美股发现:14 个策略里,收益几乎总是集中在一侧(隔夜或日内),且两侧符号常相反;动量利润几乎全部来自隔夜,日内部分统计上不显著。BKTZ 把隔夜的正收益、日内的负收益归因于散户关注度驱动的开盘买压。
   中国 A 股这边,搜到的直接、可核实的证据是 Qiu(2022)的博士论文:用 2009–2021 高频数据发现隔夜段和日内段之间有"强持续性和反转模式",把 11 个交易策略的异常收益按日内区间分解,发现呈 U 形(集中在开盘和收盘附近),归因于中国投资者和美国投资者的交易时点结构性不同,并提到 T+1 可能导致机构在开盘时更活跃交易。这篇是可验证的 pre-cutoff 中国证据,但论文摘要本身没有给出"隔夜 vs 日内哪个延续哪个反转"的简单结论,不能直接套用 LPS 的美股结论。`[R14]` `[R15]` `[R16]`
   另外搜到一篇 Hull 大学工作论文《The Nexus of Overnight Trend and Asset Prices in China》,内容正好命中"中国隔夜 vs 日内拉锯 + 机构/散户分段交易"这个主题,但搜索结果把它列为 2024 年期刊文章,**超出 2023-08-08 这个日期线,本次不采用**,如实记录排除理由而不是悄悄忽略。`[R17]`(verified: true,但排除)

3. **机制证据:BKTZ 用散户关注度(搜索/新闻曝光)和机构持仓比例做横截面分组,发现隔夜涨、日内跌的模式在高关注度、低机构持仓的股票上更强,情绪高的月份效应翻倍以上;后续 Aboody 等人直接把隔夜收益本身当成公司层面情绪的度量在用。Qiu(2022)用的是制度性论证(T+1、集合竞价、投资者交易时点差异),不是账户级直接验证。两篇都没有用委托簿/账户数据直接证明"隔夜=散户/日内=机构"这个因果链,只是用关注度/机构持仓做间接分组证据。`[R15]` `[R16]`

4. **和短期反转分开的标准做法:先对收益做正交化(残差动量),再排序;或者直接用一个正交化的"新闻代理"把收益拆成基本面驱动段和非基本面驱动段,只对后者做反转/动量。**
   Blitz–Huij–Martens 的 Residual Momentum 是先对个股收益回归掉市场/规模/价值暴露,用残差收益排序做动量,样本期(1926–2009)残差动量夏普比(0.90)明显高于总收益动量(0.45)。Da–Liu–Schaumburg 是把标准短期反转收益,用分析师预测修正(基本面新闻代理)正交化拆成"基本面驱动"和"非基本面驱动"两段,发现只有非基本面驱动的那一段(定价错误段)反转显著,用这个代理做出来的强化反转策略风险调整收益是标准反转策略的数倍(发表版四倍,工作论文版三倍)。
   这两篇都支持我们草案里"用 `cs_regres(·, ts_sum(day_sum(Ret), 20))` 对 20 日收益取截面残差"这个做法方向是对的——文献里标准做法确实是先正交化掉收益/反转暴露,再看剩余部分,而不是在原始信号上直接做双重排序控制。`[R18]` `[R19]`

### 对题目小问的直接回答

- **(a)** 构造细节見上;LPS/BKTZ 用的开盘价定义在搜索结果里没有给出逐字的"集合竞价 vs 第一笔成交"区分(WebFetch 原文抓取失败,只拿到二次摘要),如实标注这部分构造细节未能从原文直接核实,是从二次综述转述。持有期:LPS 月度,BKTZ/Qiu 是日度加月度两个层次都有。
- **(b)** 美股方向明确(隔夜延续动量、日内反转,`[R14]`);中国 A 股方向在本次搜索里**没有拿到一篇可核实的、给出明确方向结论的 pre-cutoff 论文**——Qiu(2022)证实了"隔夜/日内存在持续性和反转模式"但没在摘要层面给出符号,如实写为部分证据、方向未定。
- **(c)** 机制证据主要是横截面分组(关注度、机构持仓)而非账户/委托数据直接验证,如实注明这是间接证据(`[R15]`)。
- **(d)** 中国 A 股直接证据(2023-08-08 前、可核实):Qiu(2022)博士论文 `[R16]`。另有一篇更对题的 Hull 工作论文(`[R17]`)因发表日期超线被排除,记录在案以免被认为是漏查。
- **(e)** 标准做法是正交化/残差化再用,不是简单双重排序;`[R18]`(对收益做残差)和 `[R19]`(对反转信号做基本面新闻正交化)都支持这一点,方向上支持我们打算的 `cs_regres(·, 20日收益)` 残差化方案。

---

## L4 —— 高度重叠的纯多头信号怎么算重复度

### 能翻译成算子语言的处理方式

1. **信号的日度秩相关和组合持仓重叠是两个会分道而行的量,不能互相替代,需要分别算。**
   Robeco 对动量等因子的多头腿/空头腿分别检验发现:腿与腿之间的收益相关是 0.59–0.85(相当高),但如果看"全部多头腿两两之间"的平均相关,数字反而是 -0.04(接近零或为负),作者据此得出空头腿的信息已经被多头腿完全吸收、空头腿不提供增量。这说明"收益序列相关"和"持仓集合重叠"确实可以给出相反方向的结论,直接支持题目(a)里"秩相关 < 0.7 但书重叠 80–95%"这种情形是真实存在、文献里有记录的现象,不是我们自己的异常。
   算子翻译:日度量 `ρ_signal = corr(y1, y2)` 和持仓量 `overlap = |top_decile(y1) ∩ top_decile(y2)| / |top_decile(y1) ∪ top_decile(y2)|` 要分开算、分开报告,库禁令目前只卡了前者。`[R20]`

2. **纯多头 vs 多空在重复度评估上会给出不同结论,是文献里明确记录的现象,不是我们这边多头口径特有的怪事。**
   Ehsani–Harvey–Li 对"是否该剔除行业暴露"这个共同成分做自举检验,发现多空投资者剔除掉它更常获益(多次自举里 80% 的情形该剔),而纯多头投资者保留它更常获益(78% 的情形该保留)——同一个共同成分,纯多头和多空会被建议用相反的方式处理。这个结论结构(同一份共同成分,long-only 和 long-short 结论相反)直接支持(d):纯多头和多空在"要不要去重复"这件事上确实可能得到相反的答案,不是同一回事。`[R21]`

3. **把多个高度重叠信号合成一个的做法,文献里更规范的做法是边际贡献检验(双重选择 LASSO + 两步截面回归),而不是简单等权平均或正交化。**
   Feng–Giglio–Xiu 的方法直接是为"新因子相对一大批已有因子是否有统计显著的边际贡献"设计的:用双重选择 LASSO 先挑出该控制的已有因子,再做 Fama–MacBeth 式两步回归估计新因子的风险价格,发现"近年提出的大多数新因子相对已有因子集合是冗余的,只有少数(如盈利、投资)有显著的边际解释力"。这个框架可以直接套到"第 k 个高度重叠的纯多头筛选书,边际贡献是不是显著非零"这个问题上,是目前搜到的、方法论上最贴近的处理方式。`[R6]`
   但没搜到一篇专门针对"由同一 y 配不同排除筛生成的纯多头十分位组合"这种具体情形的合成方法论文(等权 / 正交化 / 逐步回归 / 最小方差的头对头比较),如实写为没搜到直接命中,Feng–Giglio–Xiu 是跨到资产定价因子选择这个更大话题的类比,不是专门研究。

### 对题目小问的直接回答

- **(a)** 标准冗余度量在资产定价文献里更常用信号/组合的收益相关(spanning regression、GRS 检验),但 Robeco 对腿级别的分析明确给出了"收益相关"和"持仓重叠"方向相反的例子(`[R20]`),说明秩相关确实可能系统性低估"筛选型"信号的重复度——这正是题目怀疑的方向,文献里有旁证支持,但不是专门针对"筛选型信号"写的论文,是从多空腿分解类比过来的。
- **(b)** 没搜到专门比较等权 / 正交化 / 逐步回归 / 最小方差这几种合成方法在"高度重叠纯多头信号"场景下样本外表现的论文。Feng–Giglim–Xiu 的双重选择 LASSO 框架(`[R6]`)是目前最接近的规范方法,但它是一般意义上的因子选择,不是专门为"纯多头十分位重叠组合"设计的。
- **(c)** 没搜到直接给出"加入第 k 个高度相关信号,边际贡献从第几个开始趋于 0"这种剂量-反应曲线的论文。Feng–Giglio–Xiu 的定性结论("大多数新因子是冗余的,只有少数有显著边际贡献")方向上支持我们的预期,但不是定量的"第几个开始归零"。
- **(d)** 有明确文献证据:同一个共同成分,在纯多头和多空框架下文献给出相反的处理建议(`[R21]`)。这支持"纯多头 vs 多空在重复度评估上结论不同"这个判断,但 `[R21]` 研究的是行业暴露这个共同成分,不是"筛选型纯多头信号"这个具体场景,翻译时要注明是类比而非直接命中。

---

## 参考文献(verified: true = 本次搜索/取页确实看到了标题、作者、刊物/卷期或页面原文中的对应信息;verified: false = 仅来自记忆或二次转述、未在本次搜索结果里直接核实)

`[R1]` Black, F., Jensen, M. C., & Scholes, M. (1972). *The Capital Asset Pricing Model: Some Empirical Tests*. In M. C. Jensen (ed.), *Studies in the Theory of Capital Markets*, Praeger. 摘要/SSRN 二次收录:https://papers.ssrn.com/sol3/papers.cfm?abstract_id=908569 — verified: true(搜索结果里直接看到摘要文本,包括"grouping procedures"原句)。

`[R2]` Vasicek, O. A. (1973-10). *A Note on Using Cross-Sectional Information in Bayesian Estimation of Security Betas*. Journal of Finance, 28(5), 1233–1239. 本次搜索没拿到直接链接,只在二次文献(澳大利亚能源监管局关于 beta 估计的报告)里看到完整的作者/刊名/卷期引用文本 —— verified: true(引用文本本身被搜索结果直接显示),但 **没有可用直链**,如实标注。

`[R3]` Asparouhova, E., Bessembinder, H., & Kalcheva, I. (2013). *Noisy Prices and Inference Regarding Returns*. Journal of Finance, 68(2), 665–714. DOI: 10.1111/jofi.12010. 元数据页:https://academicnewsletter.sufe.edu.cn/info/360193 — verified: true(搜索结果给出了标题、作者、刊物、卷期、页码、DOI 和摘要原文)。

`[R4]` Lesmond, D. A., Ogden, J. P., & Trzcinka, C. A. (1999). *A New Estimate of Transaction Costs*. Review of Financial Studies, 12(5), 1113–1141. 原文 PDF:https://www.bauer.uh.edu/rsusmel/phd/lot_1999RFS.pdf — verified: true(搜索结果给出刊物/卷期/页码,且直接找到 PDF 链接)。

`[R5]` Green, J., Hand, J. R. M., & Zhang, X. F. (2017-12). *The Characteristics that Provide Independent Information about Average U.S. Monthly Stock Returns*. Review of Financial Studies, 30(12), 4389–4436. https://ideas.repec.org/a/oup/rfinst/v30y2017i12p4389-4436..html — verified: true。

`[R6]` Feng, G., Giglio, S., & Xiu, D. (2019-01, NBER WP 25481; 正式发表 2020, Journal of Finance). *Taming the Factor Zoo: A Test of New Factors*. https://www.nber.org/papers/w25481.pdf — verified: true(搜索结果直接给出标题、作者、方法摘要原句)。

`[R7]` Fama, E. F., & French, K. R. (2008). *Dissecting Anomalies*. Journal of Finance, 63(4), 1653–1678. PDF:https://www.johnhcochrane.com/s/fama_french_dissecting_anomalies_JF.pdf — verified: true。

`[R8]` Hou, K., Xue, C., & Zhang, L. (工作论文 2017, NBER WP 23394;正式发表 2020, Review of Financial Studies). *Replicating Anomalies*. https://www.nber.org/papers/w23394.pdf — verified: true(搜索结果提到检验 452 个异象、NYSE 断点、等权 vs 加权的结论原句)。

`[R9]` Chen, T., Gao, Z., He, J., Jiang, W., & Xiong, W. (2017, NBER WP 24014;正式发表 2019, Journal of Econometrics, 208(1), 249–264). *Daily Price Limits and Destructive Market Behavior*. https://www.nber.org/papers/w24014.pdf — verified: true(搜索结果直接给出作者、机构、刊物、ST vs 非ST 的核心设计原句)。上交所逐笔数据磁吸效应研究与创业板限宽改革后未发现磁吸效应的研究,仅通过二次摘要确认存在但未取得完整标题/作者 — verified: false,如实标注为"查到结论方向但未核实完整出处"。

`[R10]` 中国证监会副主席李超披露数据,转引自 Caixin(2022-06-24). *Retail Investors' Share of Chinese Stock Markets Falls Below 70%*. https://www.caixinglobal.com/2022-06-24/retail-investors-share-of-chinese-stock-markets-falls-below-70-101903331.html — verified: true(新闻报道,非学术论文,背景事实)。

`[R11]` 深圳市场投资者结构相关披露(约 2012 年,机构持仓占比上升、个人投资者占比从 71.3% 降到 63.4%),二次来源:https://mondovisione.com/media-and-resources/news/investor-structure-and-characteristics-of-behavioural-changes-in-shenzhen-market-2013515/ — verified: false(搜索摘要给出了数字,但原始报告标题/作者未能在本次搜索中直接核实,数字的确切年份和统计口径存疑,使用时要降权)。

`[R12]` 关于中国股权分置改革限售股解禁的事件研究(约 482 个解禁事件,窗口期异常收益约 -14%,成交量放大约 140%),EFMA 会议论文:https://efmaefm.org/0EFMSYMPOSIUM/2010-China/papers/LLW_splitshare20091030.pdf — verified: true(搜索结果直接给出会议、数字、论文来源链接)。注意这是股改限售股解禁,不是 IPO 限售股解禁,机制类似但不是同一制度,引用时要注明。

`[R13]` 另一篇关于限售解禁即使被完全预期、价格冲击依然存在的研究:https://www.feem.it/?p=32507 — verified: true(搜索结果给出了结论原句),但完整标题/作者未在本次搜索中进一步核实。

`[R14]` Lou, D., Polk, C., & Skouras, S. (工作论文长期流传,正式发表 2019, Journal of Financial Economics, 134, 192–213). *A Tug of War: Overnight versus Intraday Expected Returns*. https://personal.lse.ac.uk/polk/research/TugOfWar.pdf ; https://researchonline.lse.ac.uk/id/eprint/87481 — verified: true(搜索结果给出刊物、卷期、页码、核心结论原句)。WebFetch 抓取 PDF 正文失败(只拿到二进制流),构造细节(开盘价定义、正交化步骤)来自二次转述,未能从原文逐字核实,如实标注。

`[R15]` Berkman, H., Koch, P. D., Tuttle, L., & Zhang, Y. J. (2012). *Paying Attention: Overnight Returns and the Hidden Cost of Buying at the Open*. Journal of Financial and Quantitative Analysis, 47(4), 715–741. PDF:https://kuscholarworks.ku.edu/bitstream/1808/10965/1/Koch_Paying%20Attention.pdf — verified: true。

`[R16]` Qiu, J. (2022-11). *Essays in Overnight Returns, Intraday Reversals, and Short-Selling Constraints in Chinese Stock Market*. PhD thesis, University of Nottingham Ningbo China (Nottingham University Business School China). https://unnc.globalimpact.cn/en/studentTheses/essays-in-overnight-returns-intraday-reversals-and-short-selling-/ — verified: true(直接取页核实了标题、作者、答辩日期 2022-11-12、机构、主要发现原句)。

`[R17]`(查到但不采用,因发表日期超线) Guo, J., Han, X., Li, K., & Li, Y. *The Nexus of Overnight Trend and Asset Prices in China*. University of Hull Business School 工作论文,repository 记录标注为 2024 年期刊文章。https://hull-repository.worktribe.com/OutputFile/4922844 — verified: true(搜索结果给出标题、作者、机构、核心论点原句),但 **发表/定稿年份为 2024,晚于 2023-08-08 截止线,本次研究不采用**,记录在案以示已查到而非漏查。

`[R18]` Blitz, D., Huij, J., & Martens, M. (2011). *Residual Momentum*. Journal of Empirical Finance, 18(3), 506–521. DOI: 10.1016/j.jempfin.2011.01.003. https://repub.eur.nl/pub/22252 — verified: true。

`[R19]` Da, Z., Liu, Q., & Schaumburg, E. (工作论文 2011-09, NY Fed Staff Report No. 513, *Decomposing Short-Term Return Reversal*;正式发表 2014, Management Science, 60(3), 658–674, *A Closer Look at the Short-Term Return Reversal*). https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr513.html — verified: true(搜索结果给出两版标题、刊物、卷期页码、核心结论原句)。

`[R20]` Robeco 研究团队, *When Equity Factors Drop Their Shorts*(约 2019,行业研究报告,非同行评审期刊论文). https://alphaarchitect.com/2019/11/do-long-only-factor-portfolios-deliver/ — verified: true(搜索结果直接给出多头腿/空头腿相关系数的具体数字 0.59–0.85 和 -0.04/0.31)。注意这是卖方/资管机构研究报告,不是学术期刊论文,引用时要降一级可信度。

`[R21]` Ehsani, S., Harvey, C. R., & Li, F. *Is Sector Neutrality in Factor Investing a Mistake?*(工作论文,Duke 人员主页托管). https://people.duke.edu/~charvey/Research/Published_Papers/P165_Is_sector_neutrality.pdf — verified: true(搜索结果给出核心自举结果:多空 20% 情形该保留行业暴露、纯多头 78% 情形该保留,原句核实)。完整发表信息(期刊/年份)本次未进一步核实,如实标注。

---

## 小结(给 PI/审计员看的一句话版)

L1:筛选 vs 收缩这条线,文献里的标准答案是"收缩(连续权重)优于硬剔除",但没有一篇论文是针对"自相关当可靠度"这个具体构造写的,我们这个用法在搜到的范围内是新的(创新度判断可以用这个事实)。
L2:磁吸效应和限宽/板块当分组变量都有扎实先例(CGHJX),但磁吸效应本身在中国市场的证据并不一致,且"板块结构是规模代理"这个担心没有被文献正面排除,只是 CGHJX 的设计方向上规避了它。
L3:美股"隔夜延续、日内反转"证据扎实,中国 A 股方向目前搜到的可核实证据(Qiu 2022)只证实了存在拉锯模式,没给出符号;一篇更对题的 Hull 论文因日期超线被排除。正交化用残差而不是双重排序,文献支持我们的方案方向。
L4:秩相关和持仓重叠确实会分道而行、纯多头和多空确实可能给出相反结论,这两点都有文献旁证(都是从多空腿分解类比过来,不是专门研究"筛选型纯多头重叠"),但没有专门的"合成方法头对头比较"或"边际贡献随 k 衰减的剂量曲线"文献命中。
