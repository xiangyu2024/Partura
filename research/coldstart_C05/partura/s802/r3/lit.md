# 文献:种子 802,B 组,第 3 轮(最后一轮)

对准 `analysis.md` §5 的四个题目(L9–L12;接着第 1 轮的 L1–L4 与第 2 轮的 L5–L8,不重复)。
核心 α(本轮首选)= `cross_cov(cross_cov(day_max(Ret), day_cov(Ret, Ret), 3), cross_cov(day_max(Ret), day_cov(Ret, Ret), 3), 3)`
——内层是「日内最大收益」与「日内收益方差」这两个**日度统计量**在 3 天窗口上的滚动协方差,外层把这个结果对自己再做一次同样的操作(≈ 再滚动 3 天测它自身的二阶波动);
核心 β(次选)= `day_kurt(Ret)`(+0.9669,对 `Ret` 乘性缩放严格不变);R 目标里还有 `day_durbin_watson(High)`/`(Volume)`、
`ts_regbeta`/`ts_reg_tvalue(day_flat_run_max(Vwap), day_durbin_watson(Volume), d)`(d = 50/100)、`cs_last_high10(...)`、`cross_valid_count(day_std(Ret), 60)` 这几类。
工具:WebSearch / WebFetch(本轮已加载)。**只用 2023-08-08 之前发表/提交的文献**;arXiv 按 v1 提交日期,期刊论文按 Crossref 的在线/印刷发表日期核对——
本轮搜到一篇相关度很高但发表日期晚于截止日的文献(§L10 第 5 条),已按规则弃用,记录在「未列入上表」一节,不计入证据。
下面每条处理方式后的 `[S#]` 对应文末出处表;`verified: true` 表示这次搜索结果或抓取的页面上确实看到了该文献的标题/作者/年份/场所。

---

## L9(对准核心 α 与 N1:日频统计量的横截面信号——用水平还是用它自己的短窗不稳定度)

搜索关键词:volatility of volatility, uncertainty about risk (unknown unknowns), vol-of-vol cross-section of stock returns, coefficient of variation of realized volatility, China A-share vol-of-vol, idiosyncratic volatility of volatility。

**能翻译成算子语言的处理方式:**

1. **「不确定性」被明确定义为"预期波动率的波动率",而且方向是明确的、负的,这正是核心 α 这类构造的直接资产定价先例。** Baltussen, van Bekkum & van der Grient 把"对风险的不确定性"量化为 **vol-of-vol**(预期波动率本身的波动率),发现高 vol-of-vol 的股票比低 vol-of-vol 的股票**每年跑输约 8%**,这个效应在控制了至少 20 个已知异象之后依然存在,在美国与欧洲市场都成立 [S1]。
   → 翻译:核心 α 的"二阶协方差"结构本质上就是这个 vol-of-vol 概念的一个具体算子实现(`cross_cov(x, x, d)` ≈ x 的滚动方差,这里 x 本身已经是"日内最大收益与日内方差的协同"这个一阶统计量)。**这给核心 α 一个明确的方向先验:如果机制和文献一致,"不稳定度高"这一端应该对应更低的未来收益**,PI 写 N1 的种子时可以直接检验符号是否与 [S1] 一致,而不是等奖励分数来猜方向。
2. **这类"二阶"信号在文献里确实有人专门做了窗口长度的系统比较,但比较的对象是日频统计量本身的时间聚合窗口,不是"离散度"这个二阶构造的窗口——两者不矛盾,但不能互相替代证据。** Fičura 用美股 40 只流动性好的个股,把日收益的已实现矩(均值、方差、偏度、峰度)分别按**月、季、年**窗口聚合,发现**季度和年度窗口的矩在单变量回归里对下月收益有显著的正向关系,月度窗口反而较弱**;多变量(Elastic Net)版本在 2004–2019 的样本外跑赢随机 [S2]。
   → 翻译:[S2] 测的是"一阶矩在多长窗口上聚合最好",而 1.1 节与核心 α 测的是"二阶统计量(方差/协方差)在多短窗口上最好"——**这是两条不同的轴,[S2] 不能直接证实或反驳"2–3 天窗口打败 20 天窗口"这个发现**,但它提示一个新检验:如果把核心 α 的外层窗口也推到季度尺度(60 个交易日左右),按 [S2] 的逻辑应该比 20 天更差(因为 [S2] 测的是一阶矩,二阶构造理论上该在短端更强,两条证据方向应该相反),这本身是一个值得记录的交叉验证点。
3. **缺口:"对一个正的重尾日度量做凸变换再取移动平均,等价于把它的时间离散度混进信号"这个 Jensen 项的直接表述,这次没有搜到资产定价文献。** 搜到的"幂平均"材料仍然全部来自风险聚合/保险精算领域,和横截面因子构造不是同一个问题(与第 2 轮 L5 的缺口相同)。[S1] 的 vol-of-vol 概念是**最接近的间接支持**——它证明"二阶矩本身就是一个独立于一阶水平的定价因子",但没有文献明确写出"凸变换+均值 ≈ 水平信息+Jensen 缺口里藏着的二阶信息"这个等价关系本身。PI 如果要用这条,应该把它写成"这是我们的推断,文献只证实了二阶矩独立定价,没有证实这个具体的代数等价"。
4. **中国 A 股上没有搜到专门的 vol-of-vol 证据,最接近的是"共同的"(市场层面)特质波动率研究,构造粒度不同。** Su, Shu & Yin 把 Herskovic et al. (2016) 的"共同特质波动率"(CIV,市场层面的 IVOL 共同成分)搬到中国 A 股,确认了类似的定价效应 [S3]——但这测的是**跨股票共同的 IVOL 成分**,不是"单只股票自己的 vol-of-vol"(核心 α 要测的是后者)。**这是一个明确的缺口**:核心 α 在"单股票、短窗、二阶统计量"这个具体构造粒度上,在中国 A 股的文献里没有找到先例,和第 1、2 轮几次搜索的结论一致——它更可能是真正的新发现,不是重新发现已知因子。

---

## L10(对准核心 β 与 N3:日内收益分布的形状,尺度不变口径)

搜索关键词:realized kurtosis cross-section, realized skewness and expected stock returns, signed jump variation (Patton Sheppard), realized semivariance, intraday return distribution shape, China A-share realized moments。

**能翻译成算子语言的处理方式:**

1. **已实现偏度与峰度的标准定义本身就是尺度不变的,而且美股证据里偏度的效应比峰度强得多、方向明确为负。** Amaya, Christoffersen, Jacobs & Vasquez 用分钟级数据算每周的已实现偏度/峰度,定义是**三次方(四次方)日内收益之和,除以已实现方差的 3/2 次方(平方)**——这个除法正是让统计量**对收益的乘性缩放不变**的那一步,和 `day_kurt(Ret)` 的性质完全对应 [S4]。**偏度**:做空最高已实现偏度十分位、做多最低十分位,下一周平均赚 19bp(t = 3.70),Fama-French/Carhart 因子解释不掉;**峰度**:与下周收益正相关,但显著性弱得多、不总是稳健 [S4]。
   → 翻译:这给 `day_kurt(Ret)`(本身已经尺度不变)一个双重提示——(a) 核心 β 选的是文献里**较弱的那一个**矩(峰度),如果 N3 要补一个新原料,`day_skew(Ret)` 在美股证据里是**更强、方向更明确**的那个,优先级应该提到 `day_kurt` 之上,这与 N3 清单里已经列了 `day_skew(Ret)` 吻合,但这条文献把它的优先级从"并列"提升到"应该优先";(b) [S4] 的"峰度较弱"这个结论本身也是对核心 β 的一个提醒:即使本轮 E 位在核心 β 上一无所获,也不等于机制不成立,**文献本身就说峰度是这类信号里信号最弱的一个**。
2. **"把已实现波动拆成上行/下行两半,只看差异"是一个独立于偏度/峰度的、专门针对不对称性的构造,已经被直接写成了标准算子定义,且与 `day_wmean(Ret, Ret)` 几乎同构。** Barndorff-Nielsen, Kinnebrock & Shephard 提出"已实现半方差"(realised semivariance):分别对日内**正**收益、**负**收益的平方分别求和,得到 RS⁺ 与 RS⁻,两者之差就是一个信号跳跃不对称度 [S5]。
   → 翻译:`day_wmean(Ret, Ret)`(用收益本身加权收益,带符号的半方差不对称度)**在数学结构上就是 RS⁺ − RS⁻ 的一个变体**——这不是类比,是同一类构造。[S5] 给了 N3 清单里这一条一个**直接的方法学出处**,而不只是"看起来像"。
3. **这个"正负分离"的半方差差异,标准化之后在个股横截面上被直接证实能定价,而且标准化的方式就是除以总变动量——这正是 N3 清单已经写出来但还没查到依据的那条种子。** Bollerslev, Li & Zhao 把 [S5] 的构造搬到个股层面,按**"好波动减坏波动,再除以总已实现波动"**把个股排序,报告收益差异大且在控制了其他已知特征之后依然显著 [S6]。
   → 翻译:这把 1.0 节 N3 清单里 `div(day_wmean(Ret, Ret), day_std(Ret))`(标准化版)这条种子,从"PI 凭直觉写的变体"升级成**文献里已经验证过的具体构造**——`day_wmean(Ret,Ret)` 除以 `day_std(Ret)` 几乎就是 [S6] 的"normalized good-minus-bad volatility"的算子翻译。**这应该是本轮 N3 种子里优先级最高的一条**,因为它同时满足"有文献依据"和"库里还没有"两个条件。
4. **缺口 + 一次规则弃用:中国 A 股上专门测"已实现偏度"的论文是本轮搜到的、相关度最高的一篇,但发表日期晚于截止日,按规则不采用。** 搜到 Dai, Jiang, Long, Wang & Zaremba 发表在 *Finance Research Letters* 的论文,专门用月度已实现偏度测中国股票,报告**显著的负向关系**(高偏度 → 低收益),但**控制了相对符号跳跃方差之后这个效应在中国市场消失**(不同于美股,中国市场里没有反转)——用 Crossref 核实其印刷发表日期为 **2023 年 12 月**,元数据登记日期为 2023-08-25,**均晚于 2023-08-08,按规则不采用**,不计入出处表、不作为证据 [未列入上表]。这是本轮唯一一次"搜到相关度很高的文献,但卡在截止日之外"的情况。
5. **缺口:没有搜到"短窗(quarterly 以下)已实现矩在中国 A 股上更强"的直接证据**——[S2] 的季度/年度窗口结论来自美股 40 只流动性最好的个股,样本本身和中国 A 股的流动性结构差很远,不能直接类比。

---

## L11(对准 N2 与 R 目标里的 `ts_regbeta`/`ts_reg_tvalue`:个股自身两条日度序列的滚动回归统计量,该用斜率、t 值还是别的归一化)

搜索关键词:rolling regression beta as a firm characteristic, t-statistic versus raw slope in cross-sectional factors, price delay R-squared, window length for firm-level rolling regressions, estimation error in firm-level betas。

**能翻译成算子语言的处理方式:**

1. **除了"斜率"和"t 值"之外,文献里还有第三种归一化:用两次回归的 R² 做比值,而且这条量尺用的窗口是一整年(约 250 个交易日),比我们试过的 50/100 天都长。** Hou & Moskowitz 把"价格反映信息的滞后程度"(price delay)定义成 **1 − 受限模型 R² / 不受限模型 R²**——用当周 + 前 4 周的滞后市场(或行业)收益去回归个股周收益,这个比值越大说明个股对信息的反应越滞后,用的估计窗口是**一整个日历年的周频数据**(约 52 个点,相当于约 250 个交易日的信息量级)[S7]。
   → 翻译:这给 N2 的"该用斜率还是 t 值"问题补上第三个候选——**R² 比值**(而不是系数本身或系数的 t 值)。这个比值天然在 0–1 之间,对异常值不敏感,如果 PI 想在种子里系统比较归一化方式,`ts_regbeta` / `ts_reg_tvalue` 之外应该加一个 **"1 − 受限 R²/不受限 R²"**的写法(操作上:`div(ts_reg_resid_var(短滞后), ts_reg_resid_var(长滞后))` 这类残差方差比值,需要核对 `partura.ac_plugin.partura_operator_names()` 里有没有现成的残差方差算子)。
   更重要的一点:[S7] 用的窗口是**一整年**,比我们 R 目标第 11 条测过的 50/100 天都长很多——这给"100–200 天比 50 天更好"这个判断一个**方向一致但量级更大**的外部参照:如果核心的"关系型"信息确实需要很长时间才能稳定估计,250 天(或更长)可能还没到头,**但 [S7] 测的是价格对信息的滞后,不是成交量与波动的关系,不能直接当作同一个统计量的窗口证据,只能当方向性支持**。
2. **这类"关系型"特征的经济解释有两种,而且互相竞争,这对 `ts_regbeta` 这个核心本身的机制解释很重要。** Hou & Moskowitz 把 price delay 的溢价归因为**投资者关注度不足导致风险分担不充分**;但 Lin, Singh, Sun & Yu(2014,检索结果转述,未独立核核原文,未列入出处表)认为这个溢价其实来自**系统性流动性风险**,不是风险分担问题 [S7]。
   → 翻译:如果本轮 E/R 在 `ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), d)` 这条线上有新发现,写归因的时候不能只说"这是价格滞后/知情交易",**流动性风险是一个同样有文献支持的竞争解释**,而我们的控制集里本来就有流动性控制——这提示如果家族控制做得够严,这条信号如果还显著,至少可以**部分排除**流动性风险这个解释,是一个可以在笔记里写的检验逻辑。
3. **缺口:这次没有搜到直接比较"斜率 vs t 值"哪个作为横截面特征更稳健的对照实验。** 搜到的间接证据是警示性的,不是支持性的——一篇讨论横截面错误定价检验的论文提醒"单独挑 t 值高的变量"本身是一个已知的数据挖掘陷阱,一个变量即使解释力很弱,也可能单独或和别的变量一起被测出"显著定价"[检索结果转述,未列入出处表];另有证据显示同一个系数在换聚类方式后 t 值会从 3.43 掉到 2.86,系数本身不变——说明 **t 值对标准误的选择很敏感,未必比系数本身"更稳"**,这是对 N2 题目原始假设("t 值应该更稳")的一个**温和的反证据**,不是confirmation。PI 如果坚持用 `ts_reg_tvalue`,应该在笔记里承认"文献没有证实这个直觉,只是没反对"。
4. **缺口:没有搜到"100 天 vs 200 天窗口,哪个更好"的直接对照实验(搜到的几篇都是 2024–2026 年发表,晚于截止日,按规则不采用,不列入出处表)。** 搜到的唯一确定早于截止日、给出具体窗口数字的是 [S7] 的一整年(约 250 个交易日),**比我们测过的范围都长**,这提示"更长窗口更好"这个方向在价格滞后这一类特征上是成立的,但不能跨统计量类比到量价关系这个具体构造上。

---

## L12(对准 1.5 节与 R 第 13、14 条:样本筛选对因子表现的影响,在中国 A 股上)

搜索关键词:sample screens in China A-share factor research, suspension and resumption handling, listing-age filters, does the screen carry alpha or remove noise, minimum number of intraday observations for realized measures, microstructure noise in illiquid stocks。

**能翻译成算子语言的处理方式:**

1. **按市值剔除最小一截是中国 A 股因子研究里最有名、最常用的筛子,理由是"壳公司"污染,而且有具体的量级。** Liu, Stambaugh & Yuan 的规模因子**剔除市值最小的 30%**,理由是这部分股票里很大一块的市值其实是"借壳上市"的壳价值,不是正常的规模溢价;这 30% 只占全市场总市值的约 7% [S8]。
   → 翻译:这给"剔除一截再看因子"这个处理方式一个**明确的、量化过的中国 A 股先例**,但剔除变量是**市值**,不是"最近是否有停牌/缺数据"(我们的 `cross_valid_count` 筛子),构造不完全对应,只能当方向性支持。
2. **"剔除一截会不会把 alpha 做出来"这个问题,在同一个"壳公司"筛子上,有后续文献直接给出了反面证据,而且结论很具体——这正是 1.5 节与 4.2 第 10 条想分开的两种解释。** Li & Rao 指出 [S8] 的"一刀切剔除最小 30%"在 2017 年之后的政策环境下**已经太粗**,直接剔除会导致**系统性地高估 alpha**;他们改成只剔除"壳概率"估计值超过阈值(主用 1%,0.1%/5% 做稳健性)的个股,结果是更多小盘股被保留下来、规模因子的月度溢价从 0.46% 升到 0.74%,模型的定价误差(HJ 距离)也更小 [S9]。
   → 翻译:[S9] 是本次检索范围内找到的**最直接的"量化过筛子对 alpha 估计值的影响"的证据**——它明确说"一刀切的筛子会让 alpha 看起来更大",这对 4.2 第 15 条(`cs_last_high10` 砍掉两个必要性很低的节点)是一个**提醒而不是否定**:[S9] 针对的是"剔除整整一截股票"这种粗筛子,而 `cs_last_high10` 是"砍掉一个算子节点"(在同一批股票上重新算一个更短的表达式),机制不同,但**同一条逻辑适用**——砍掉节点之后分数不降,不能直接说"这两个节点是死重",还需要像 [S9] 一样做一次"换一种粗细程度的筛法,alpha 还涨不涨"的交叉检验。
3. **停牌是中国 A 股特有的、随时间剧烈变化的现象,筛子的"有效剔除比例"在不同年份完全不同,这对任何固定阈值的筛子都是一个警告。** 2015 年股灾期间**接近 60% 的上市公司**曾被停牌,而 2020 年全年平均**不到 0.5%** 的 A 股处于停牌状态 [S10]。主要指数提供商对停牌的处理不是简单剔除,而是**推迟指数调整、停牌超过复核日两个月就取消该次调整**,并把 `*ST`(风险警示)股票整体排除在可投资范围之外 [S11]。
   → 翻译:`cross_valid_count(day_std(Ret), 60)` 这类"过去 60 天有效天数"筛子,**它的实际筛选强度在 2018–2023 样本内部可能并不均匀**(2015 式的极端停牌潮不在 train/valid 窗口内,但 2018 年之后仍有常规停牌),如果 PI 想检验第 13、14 条"筛子不是通用处理"这个判断,可以按年份分段看这个筛子的命中率,而不是只看一个全样本的 gain 数字。[S11] 的"`*ST` 整体排除"也提示:如果库里还没有一个专门针对 `*ST`/风险警示板的筛选算子(`BoardCode` 字段理论上能做这个),这是指数编制实践里的标准做法,不是我们自己拍的。
4. **用高频数据估计的统计量,流动性越差、估计噪声越大,这是通用的微观结构文献结论,但没有搜到一个具体的"最少多少个观测"的数字。** Aït-Sahalia & Yu 分解纽交所个股的高频价格为"基本价值 + 微观结构噪声"两部分,发现**财务特征上更流动的股票,噪声和噪声/信号比都更低** [S12]。
   → 翻译:这是对 1.5 节"筛子和 `day_kurt` 是配对的(峰度在有缺口的票上估得差)"这个判断的**通用机制支持**——流动性差的票,用分钟级数据算出来的 `day_kurt`/`day_durbin_watson` 这类统计量本身就更噪,筛子抬分很可能真的是在去噪,不是巧合。但**没有搜到任何文献给出"至少需要多少个有效交易日/多少个分钟观测"的具体数字**,这是一个明确的缺口:4.2 第 16 条("筛子窗口换成 241")和第 15 条("砍掉两个必要性节点")目前都只能靠付费评估本身的数字说话,文献给不出一个先验阈值。
5. **缺口:没有搜到专门针对中国 A 股、把"用高频数据估已实现矩"和"最小样本量"连在一起讨论的论文。** 第 1 轮背景引用过的 [S17: Jansen, Swinkels & Zhou (2021), *Anomalies in the China A-share market*](不在本轮出处表里重复列出,信息未变)覆盖的是日频异象的样本处理,不是高频矩估计的样本量问题,这条缺口和第 1、2 轮的几次缺口是同一类:中国 A 股在"高频统计量的估计质量"这个具体问题上的文献比美股薄得多。

---

## 出处(全部核对时间,均在 2023-08-08 之前)

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|---|
| S1 | Unknown Unknowns: Uncertainty About Risk and Stock Returns | Guido Baltussen, Sjoerd van Bekkum, Bart van der Grient | 2018(Journal of Financial and Quantitative Analysis 53(4);工作论文版本 2014 年已流传) | 期刊:Journal of Financial and Quantitative Analysis | https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/unknown-unknowns-uncertainty-about-risk-and-stock-returns/6E0E98349D20C1DCF67F3A0452361B80 | true |
| S2 | Forecasting the Cross-Section of Stock Returns with Realised Moments | Milan Fičura | 2019(European Financial and Accounting Journal 14(2), 71–84;DOI 10.18267/j.efaj.227) | 期刊:European Financial and Accounting Journal | https://efaj.vse.cz/artkey/efa-201902-0004_forecasting-cross-section-of-stock-returns-with-realised-moments.php | true |
| S3 | The pricing effect of the common pattern in firm-level idiosyncratic volatility: Evidence from A-Share stocks of China | Zhi Su, Tengjia Shu, Libo Yin | 2018(Physica A 497, 218–235;DOI 10.1016/j.physa.2018.01.004) | 期刊:Physica A: Statistical Mechanics and its Applications | https://ideas.repec.org/a/eee/phsmap/v497y2018icp218-235.html | true |
| S4 | Does Realized Skewness and Kurtosis Predict the Cross-Section of Equity Returns? | Diego Amaya, Peter Christoffersen, Kris Jacobs, Aurelio Vasquez | 2015(Journal of Financial Economics 118(1), 135–167;CREATES 工作论文版本 2011/2013 年已流传) | 期刊:Journal of Financial Economics | https://repec.econ.au.dk/repec/creates/rp/13/rp13_41.pdf | true |
| S5 | Measuring Downside Risk: Realised Semivariance | Ole E. Barndorff-Nielsen, Silja Kinnebrock, Neil Shephard | 2008(CREATES Research Paper 2008-42 / Nuffield College 工作论文;正式发表为 *Volatility and Time Series Econometrics*(编 Bollerslev, Russell, Watson)一书第 117–136 页,Oxford University Press,2010) | 工作论文(CREATES / Nuffield)/ 书籍章节(OUP) | https://repec.econ.au.dk/repec/creates/rp/08/rp08_42.pdf | true |
| S6 | Good Volatility, Bad Volatility, and the Cross Section of Stock Returns | Tim Bollerslev, Sophia Zhengzi Li, Bingzhi Zhao | 2020(Journal of Financial and Quantitative Analysis 55(3), 751–781;工作论文版本约 2014 年已流传) | 期刊:Journal of Financial and Quantitative Analysis | https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/good-volatility-bad-volatility-and-the-cross-section-of-stock-returns/B9203F87AB93D8DEAD51CB692587350E | true |
| S7 | Market Frictions, Price Delay, and the Cross-Section of Expected Returns | Kewei Hou, Tobias J. Moskowitz | 2005(The Review of Financial Studies 18(3), 981–1020) | 期刊:The Review of Financial Studies | https://ideas.repec.org/a/oup/rfinst/v18y2005i3p981-1020.html | true |
| S8 | Size and Value in China | Jianan Liu, Robert F. Stambaugh, Yu Yuan | 2019(Journal of Financial Economics 134(1), 48–69;NBER Working Paper 24458, 2018-03) | 期刊:Journal of Financial Economics / NBER | https://www.nber.org/papers/w24458 | true |
| S9 | Evaluating Asset Pricing Models: A Revised Factor Model for China | Zhiyong Li, Xiao Rao | 2022(Economic Modelling 116, 106001;DOI 10.1016/j.econmod.2022.106001) | 期刊:Economic Modelling | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3950453 | true |
| S10 | Quick Take: China A-Shares – Exchange Rules Subdue Suspensions | Acadian Asset Management(机构研究笔记,未在搜索结果中给出具体撰稿人姓名) | 2020-04 | 机构研究笔记:Acadian Asset Management | https://www.acadian-asset.com/investment-insights/equities/quick-take-china-a-shares-exchange-rules-subdue-suspension | true |
| S11 | MSCI China All Shares Index Methodology | MSCI(指数方法论文件,机构作者) | 2017-09 | 指数方法论:MSCI | https://www.msci.com/eqb/methodology/meth_docs/MSCI_China_All_Shares_Index_Methodology_Sep2017.pdf | true |
| S12 | High Frequency Market Microstructure Noise Estimates and Liquidity Measures | Yacine Aït-Sahalia, Jialin Yu | 2008-02(NBER Working Paper 13825;正式发表 Annals of Applied Statistics 3(1), 422–457, 2009) | NBER / 期刊:Annals of Applied Statistics | https://www.nber.org/papers/w13825 | true |

未列入上表、曾经搜索但没有搜到可用文献,或搜到但因日期不合规被弃用的方向(诚实记录,不编造):
- 「对一个正的重尾日度量做凸变换再取移动平均,等价于把时间离散度混进信号」这个 Jensen 项的直接资产定价文献表述——搜不到,只有 [S1] 的 vol-of-vol 概念作为间接支持(L9 第 3 条)。
- 中国 A 股上专门的「单股票 vol-of-vol」证据——搜不到,只搜到市场层面的「共同特质波动率」研究 [S3],构造粒度不同(L9 第 4 条)。
- 中国 A 股「已实现偏度」的专门论文——搜到 Dai, Jiang, Long, Wang & Zaremba,*Finance Research Letters* 58(PB)(2023),Crossref 核实印刷发表日期为 **2023-12**、元数据登记日期 **2023-08-25**,**均晚于 2023-08-08,按规则弃用**,不计入出处表、不作为证据(L10 第 4 条)。
- 「斜率 vs t 值哪个作为横截面特征更稳健」的直接对照实验——搜不到;搜到的两条间接证据(聚类方式改变 t 值、t 值挑选的数据挖掘陷阱)方向偏向于*不*支持「t 值天然更稳」这个直觉,但都是转述,未列入出处表(L11 第 3 条)。
- 「100 天 vs 200 天窗口哪个更好」的直接对照实验——搜到的几篇都发表于 2024–2026 年,晚于截止日,按规则弃用,不列入出处表(L11 第 4 条)。
- 「用高频数据估已实现矩所需的最少观测数」的具体数字(中国 A 股或其他市场)——搜不到具体阈值,只搜到方向性结论 [S12](L12 第 4、5 条)。
- D.E. Shaw 的 2021-09 研究笔记《The Point of No Returns: Trading Halts and Other Market Structure Considerations in China A-Shares》——标题与日期在搜索结果中确认看到,但本轮没能把 PDF 正文解析成可读文本,具体数字无法核实,**未采用其任何具体论断**,不计入出处表。

---

## 给 PI 的一句话总结

本轮最硬的两条:**(a) L10 第 2、3 条——`day_wmean(Ret, Ret)` 和它的标准化版 `div(day_wmean(Ret, Ret), day_std(Ret))` 不是 PI 凭直觉写的种子,而是已实现半方差文献([S5] 提出构造、[S6] 证实个股层面定价)的直接算子翻译,N3 如果要选一条种子优先做,应该是这条标准化版**;
**(b) L12 第 2 条——Li & Rao(2022)用同一个「壳公司」筛子的前后两个版本,量化证明了"剔除一截之后 alpha 看起来更大"本身不能当成"筛子携带 alpha"的证据,4.2 第 15 条那种必要性检验的解读需要多一道交叉检验,不能只看分数涨跌。**

本轮唯一的负面提醒在 L9:**Baltussen et al. [S1] 给出的 vol-of-vol 效应方向是负的(不确定性越高、未来收益越低)**——如果核心 α 的"二阶协方差"构造机制和文献一致,PI 写 N1 的种子时应该预期**和不稳定度正相关的那一端对应更低的分数**,而不是方向不定;本轮搜索也再次确认,核心 α 这个具体构造粒度(单股票、2–3 天窗口、二阶统计量)在中国 A 股文献里仍然没有直接先例,这与第 1、2 轮几次搜索的结论一致——更可能是真发现,不是重新发现已知因子。
