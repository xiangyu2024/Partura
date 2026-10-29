# 文献笔记 — s807 / r2(文献员)

范围:只用 **2023-08-08 之前发表**的论文 / 工作论文 / 研究报告(arXiv、SSRN、机构工作论文系列以首版日期为准)。对 `r2/analysis.md` §7 的 L1–L4 四个题目逐一检索;每条「处理方式」后标出处编号,对应文末〈参考文献〉。搜不到的地方明确写「搜不到」,不补全、不猜测。本轮题目与 r1 不同(r1 是已实现半方差符号/路径效率/资金流失衡),除 L3 的 MAX/IVOL 两篇背景文献外没有重复检索。

---

## L1 — 隔夜 vs 日内收益归属(对准 N-α)

**能翻译成算子语言的处理方式:**

1. **分解方法本身:两腿是"持续性 vs 对期反转",不是单纯取差。** Lou–Polk–Skouras [1](*A tug of war*,JFE 2019)把日收益拆成隔夜段(昨收→今开)与日内段(今开→今收),对 14 个交易策略(含动量、反转等)分别检验,发现**同一个策略的利润几乎全部出现在其中一段,另一段通常方向相反**;公司层面的"隔夜延续、日内延续"效应能持续数年,但跨段("隔夜赢→日内")存在显著反转。
   翻译:这证实了 analysis.md §4.3 提的构造思路——**取两腿之差**(`sub(ts_sum(隔夜,N), ts_sum(日内,N))`)能同时捕捉"哪一段在持续"和"跨段反转"两件事,是文献里真实检验过的分解方式,不是我们自己拍的。但 [1] 的页面没有给出具体的开盘价定义(集合竞价价格 vs 开盘后第一笔),这一点**搜不到**,见下方空白清单。

2. **"计数版"构造,直接对应 analysis.md §4.3 的"方向版 vs 幅度版"取舍。** Akbas–Boehmer–Jiang–Koch [4](JFE 2022)的核心变量不是隔夜与日内收益的幅度差,而是**一个月内"隔夜为正、随后日内为负"这一事件发生的频率**(计数,不加权幅度),频率越高预测未来收益越高,机制解释是日内套利者低估了隔夜可能到达的消息、过度纠偏了隔夜的上行压力。
   翻译:这是一个**比我们 §4.3 写的幅度差分更贴近文献主流的构造**——`cross_mean(mul(gt(隔夜_t, 0), lt(日内_t, 0)), 20)` 这类"符号配对计数"而不是 `sub(ts_sum(隔夜,60), ts_sum(日内,60))` 的幅度差。建议 PI 把这个计数版本也列为候选种子,而不是只写幅度版。

3. **按 size / liquidity 条件化,有直接的机制依据,且方向会反转。** Bogousslavsky [3](JFE 2021)发现:套利资金对隔夜持仓的保证金与融券费约束,使得被低估的因子在**日内**赚钱、在收盘前表现差;**小盘、低流动性股票的尾盘 30 分钟收益高,但隔夜收益大幅为负;大盘、高流动性股票恰好相反**。样本为美股约 30 年。
   翻译:这给了"按规模/流动性分组做条件化"的具体文献依据,但**方向在不同分组下相反**,不能照抄单一符号;这与 analysis.md §4.1 建议用 `ListAge` 条件化的思路相关但不完全同构——文献用的是 size/liquidity 不是 ListAge,我**没有查到**用上市年限做条件化的直接先例。

4. **退休:散户关注度的条件化。** Berkman–Koch–Tuttle–Zhang [2](JFQA 2012)发现隔夜收益为正、随后日内反转的模式**集中在近期被散户关注的股票**(关注度用过去的极端绝对收益/净买入强度代理),且在难估值、套利成本高、散户情绪高涨的时期更强;美股 1996–2008,3000 只最大股票。
   翻译:关注度代理(极端 |收益|)本身是我们池子里能构造的量(`abs_` 加窗口极值),可以作为隔夜效应的条件变量,但这是美股证据,机制是"散户开盘追涨",不是 A 股的 T+1。

5. **A 股的机制是 T+1,不是散户关注度,方向可能不同。** 白颢睿等 [5](《财经研究》2020-04,46(4):140–154)用 2000–2016 年 A 股数据发现:A 股同时存在日内动量与隔夜动量,**T+1 制度导致两段之间出现强反转**,这正是月度动量效应偏弱的原因;**高风险股票隔夜收益偏低,低风险股票隔夜收益偏高**;波动率越高、T+1 约束越强、跨段反转越明显。
   翻译:这条提醒必须单独标出——"高风险股隔夜收益偏低"意味着隔夜腿本身可能与波动有**非线性**关联(陷阱 3 的风险),种子里如果要用隔夜/日内腿,最好先看一下它与波动控制的相关度表,别重蹈 head 1/2/3 的覆辙。

6. **A 股的"拔河"模式与美股不是同一个符号,不能照搬。** Lin–Chang–Chou [6](*Pacific-Basin Finance Journal*,2023-06,79:102007)把 Lou–Polk–Skouras 的框架搬到中国,发现**不是所有异象都能在隔夜或日内段里单独赚钱**(这点与美股不同,美股几乎每个策略都能在其中一段赚钱),而且**更多策略在隔夜段赚钱**。
   翻译:这是对 analysis.md §4.3「方向由奖励在 train 上定,两边都解释得通」这句话的文献支撑——**不能预先假设方向**,[6] 明确说中国市场的隔夜/日内收益模式本身就与美股系统性不同。

**搜不到的地方(明确空白,不要当成文献证伪):**
- 一字板 / 涨跌停的开盘价在隔夜收益构造里具体怎么处理(当缺失还是用涨跌停价代入),[1][2][3][4][5][6] 都没有给出可核实的处理细节。
- 集合竞价价格与"开盘后第一笔成交价"作为"今开"定义的对比检验,没有查到。
- [1] 的"continuation lasts for years"没有给出半衰期的具体数字(月或日)。
- A 股用 `ListAge` 做条件化的直接先例,没有查到(只有美股用 size/liquidity 条件化的先例,[3])。

---

## L2 — 股本结构、解禁与增发供给(对准 N-β / R7–R9)

**能翻译成算子语言的处理方式:**

1. **"变动量"而非"水平"是经典做法,直接对应 `ts_delta(LogFloatShares, N)`。** Pontiff–Woodgate [7](JF 2008,63(2):921–945)用**净股份发行**(期间流通股数的变化)做横截面收益预测,1970 年之后样本里这个变量的统计显著性**超过规模、账面市值比和动量**;1970 年之前样本里对大多数持有期几乎没有预测力。
   翻译:这直接对应我们 `ts_delta(LogFloatShares, 241)` 的构造——用变动量而不是水平,且文献明确说这个效应**不是对所有时期都稳健**,子样本敏感,提醒 PI 对这条线的样本外预期不要定得太高。

2. **更完整的口径(CEI)同时纳入期权、并购发行、回购/分红,我们目前的构造只覆盖了其中一部分。** Daniel–Titman [8](JF 2006,61(4):1605–1643)的**复合股票发行(composite equity issuance, CEI)**同时计入股票期权行使、并购换股发行、股票回购与分红,是比单纯"流通股数变动"更宽的口径,CEI 独立预测未来收益,且与"无形信息"关联;控制了股份发行之后,账面回报与未来收益之间没有统计上可靠的关系。
   翻译:`ts_delta(LogFloatShares, N)` 只捕捉到了 CEI 的一部分(增发、解禁带来的流通股数变化),**遗漏了股权激励行权、并购发行、股份回购**这三类同样会改变"供给"但未必改变 `LogFloatShares`(回购/激励通常改变总股本而非仅流通股)的渠道——如果要在 A 股做可比的回购/激励口径,需要另外的叶子,目前池子里没有,这是一条值得写进 notebook 的缺口,不是本轮能填的。

3. **解禁价格压力是永久性水平下移,不是会反弹的脉冲——窗口选择的方法学依据。** Field–Hanka [9](JF 2001,56(2):471–500)发现 IPO 锁定期解禁前后 3 日异常收益约 −1.5%,交易量永久上升 40%,**这个反应不会在之后的几周里反弹**(用来拒绝"临时价格压力"假说),且**即使没有内部人卖出报告,异常收益依然显著为负**。
   翻译:这给出一个具体的方法学依据——如果 `ts_delta(LogFloatShares, 241)` 这类变动量确实捕捉到解禁/增发的供给效应,它应该体现为**水平的永久位移**,不是一个会被下一期抵消的脉冲;所以月度聚合时不需要专门设计"衰减窗口"去迎合一个会反弹的信号,窗口选择应该服务于"多长时间内发生过变动"这个判定,而不是"多久之后信号衰减"。

4. **A 股特有证据:累计异常收益主要在解禁前形成,解禁后部分修复;新增流通股比例越高,负面效应越大。** 刘娥平、唐舜 [10](《财经研究》2014,40(9):86–96)用期权定价模型构造"可交易性折扣",提出解禁本质是可交易性价值从流通股向限售股转移;**累计异常收益主要在解禁前形成,之后持续显著下降,解禁后略有回升**;**新增流通股的相对比例越高、套利风险越大、限售股东减持意愿越强,负面影响越大**。
   翻译:(i)"新增流通股相对比例"这个维度(= `ts_delta(LogFloatShares,N)` 相对基数的大小)直接被证明是机制相关的,支持 R9 的构造方向;(ii)"解禁前下跌、解禁后部分修复"的时间结构提示,如果用**月度**聚合捕捉这个特征,窗口不能太短,否则会把"下跌段"和"修复段"同时纳入、互相抵消部分信号。

5. **自由流通比例(水平,不是变动)在 A 股横截面定价里独立于账面市值比,这是 `sub(LogTotalCap, LogFloatCap)` 这个水平量的直接依据。** Wang–Xu [11](*Financial Analysts Journal*,2004-11,60(6):65–77)用 1996 年 7 月–2002 年 6 月的 A 股非金融股样本,把**自由流通比例**加进三因子模型(理由是中国市场的投机性、政府持股比例大、会计信息质量弱),发现市场 + 规模 + 自由流通三因子能把按"规模 × 剩余自由流通比例"分组组合收益的解释力从简单市场模型的约 81% 提到约 90%;同样的检验里**账面市值比没有显著解释力**。
   翻译:这是支持 `sub(LogTotalCap, LogFloatCap)`(锁仓比例的对数水平,价格精确抵消)这条线的直接 A 股证据——自由流通比例的**水平**本身(不需要先取变动量)在中国市场就有独立的横截面解释力,且账面市值比管不住它。

**搜不到的地方(明确空白):**
- composite equity issuance 异象与 free float ratio 异象是不是"同一件事"的系统性对比文章,没有查到——[7][8][11] 各自独立,没有一篇把两条线放在一起比较。
- A 股定向增发(非公开发行)作为独立供给冲击的同行评审横截面检验,只搜到解禁([10])相关的研究,没有查到专门针对定向增发价格冲击、且做个股横截面检验的论文。
- `LogFloatShares` 变动与规模 / 名义价格恒等式(`LogFloatCap = LogFloatShares + log(价格)`)的分离处理,[8] 的 CEI 设计目的本身就是分离"有形"与"无形"信息,但**没有专门讨论**它与 log 市值的共线性问题,这一点搜不到直接文献。

---

## L3 — 水平 / 月内极端值 / 波动的波动,三者是否独立(对准 head 4 与整个 RV 凸尾族)

**能翻译成算子语言的处理方式:**

1. **IVOL(均值型二阶矩)与 MAX(窗口极值)是文献里明确比较过、且在美股互相替代归因的两条线。** Ang–Hodrick–Xing–Zhang [12](JF 2006,61:259–299;NBER WP10852,2004-10)把特质波动率构造成"月内日度残差标准差"(日度方差的**均值**聚合),高 IVOL 组后续收益显著更低,FF3 调整后依然存在。Bali–Cakici–Whitelaw [13](JFE 2011,99(2):427–446;NBER WP14804,2009-03)把同一类日度数据改成"月内最大单日收益"(**窗口极值**聚合),发现 MAX 的解释力**覆盖、反转**了 IVOL 的解释力。
   翻译(与 r1 §1.2 一致,此处再次确认):`cross_mean(day_var(Ret), 20)` 式的均值聚合 ≈ IVOL 路线;`cross_max(·, 20)` 式的窗口极值聚合(head 1 的 EMA 凸尾本质上是它的平滑版)≈ MAX 路线;**在美股这两条线不是互补,是同一个现象的两种读法**。

2. **vol-of-vol(二阶矩的二阶矩)是文献里明确检验过的"第三条独立线",但度量工具是隐含波动率,不是已实现波动率。** Baltussen–van Bekkum–van der Grient [14](JFQA 2018,53(4))把"风险的不确定性"构造成**隐含波动率的月度滚动标准差**(基于个股平价期权隐含波动率的时序波动率),发现高 vol-of-vol 组比低 vol-of-vol 组**每年跑输约 8%**,这个效应独立于至少 20 个已知的波动相关效应(包含 IVOL、MAX 等组合);在卖空约束最松的分组里,这个效应**最小且在统计上不显著**。
   翻译:这是美股上"vol-of-vol 是独立特征"最直接的证据,但**构造工具是期权隐含波动率的波动率,不是我们 head 4 用的"已实现波动率(DW)的时序标准差"**——两者是同一个概念(风险的不确定性)在不同输入上的实现,**不能把 [14] 的结论直接套到 head 4 头上当"已证实"**,只能当成"这类机制存在且在其他度量方式下独立"的背景支持,这一点必须在 missions.yaml 里写清楚,别混用。

3. **A 股上 MAX 和 IVOL 不是互相独立的——这是本题最直接回应 analysis.md §1.5 的一条证据,方向需要注意。** Wan [15](*International Review of Economics & Finance*,2018,53:1–15)在中国股票市场上检验 MAX 和 IVOL 的关系,结论**不对称**:**IVOL 效应不被 MAX 效应吸收,但 MAX 效应被 IVOL 效应吸收**——也就是说,控制了 IVOL 之后 MAX 的解释力消失,但控制了 MAX 之后 IVOL 依然显著。
   翻译:这与 r1 lit.md 引用的 Nartea–Kong–Wu [17](JBF 2017,76:189–197,"MAX 效应本身存在,且不削弱、不反转 IVOL 之谜,两者独立共存")**不完全一致**——[17] 说"独立共存",[15] 说"MAX 被 IVOL 吸收"。这提示 PI:**A 股上 MAX vs IVOL 的关系本身在文献里没有定论**,head 1(窗口极值机制)和 head 4(二阶矩机制)谁更可能在"去掉波动水平"后依然独立,**不能从美股或单一篇 A 股文献里找到现成答案**,R4–R6 的直接评估比引用文献更可靠。

4. **涨跌停市场需要重新标准化 MAX,这条在 r1 已经引用过,此处确认仍适用于 head 1 的凸尾机制。** Hung–Yang [16](JFM 2018,41:77–91)指出原始 MAX 定义在有价格限制的市场里会被板子"削平",按涨跌停幅度重新标准化后 MAX 依然显著,且不是 IVOL 的另一种表现。
   翻译:这条是 r1 §4.2 已经引用过的同一篇文献([8] in r1),此处确认它同样适用于本轮 head 1(RV 的凸尾/窗口极值机制)—— 如果要测 head 1 是不是纯粹的板宽代理,`LimitWidth` 归一化是文献支持的方向,但审计员已经判过 `LimitWidth`/`BoardCode` 不能用于条件化(analysis.md §3.4),这条路径在本种子事实上被规则堵死了,只能当背景知识,不能写进种子。

5. **低波动异象的多头腿单独的样本外表现:文献给出的是多空价差,多头腿单独的数字没有查到核实来源。** Blitz–van Vliet [18](*Journal of Portfolio Management*,2007 Fall:102–113)报告全球低波动与高波动十分位组合的多空年化 alpha 差约 12%(1986–2006 样本);Baker–Bradley–Wurgler [19](*Financial Analysts Journal*,2011,67(1))用美股 1968–2008 数据确认低贝塔/低波动跑赢高贝塔/高波动,解释机制是机构基准相对考核限制了套利资金。
   翻译:两篇都确认"多空价差"显著,但**多头腿单独的具体数字(相对于市场基准的超额收益率、而非多空价差)我没有查到可核实的原文数字**——网上能搜到的"11.3%/年"是第三方(Quantpedia)从表格估算出来的,不是论文原文,**不建议引用这个具体数字**,只能说"方向上文献支持低波动多头腿有正的风险调整收益"。

**搜不到的地方(明确空白,与 r1 一致,本轮未发现新证据):**
- 同一个日度风险量换不同幂次 / Lp 范数聚合(p = 1, 2, 4, 8)的样本外稳定性系统比较,没有查到专门做这件事的文献(搜索关键词同 r1:"higher moments aggregation daily signal monthly factor"、"Lp norm aggregation",只搜到 2024 年之后的工作,按规则不能用)。
- 低波动异象多头腿单独对"怎么度量波动"(标准差 vs 方差 vs 已实现方差 vs 隐含波动率)的敏感性分析,没有查到专门检验。
- 已实现方差(不是隐含波动率)的 vol-of-vol 作为独立定价特征,在 A 股上的同行评审检验,没有查到——[14] 是美股+隐含波动率,[15] 是 A 股+MAX/IVOL(不含 vol-of-vol)。

---

## L4 — 日内「什么时候动的」(对准核心 A 的 E 位第 1 族)

**能翻译成算子语言的处理方式:**

1. **"哪个半小时"本身携带可预测信息,且明确与量、价差、波动率的日内模式不是同一件事——这是最直接支持"无量纲时点特征"思路的证据。** Heston–Korajczyk–Sadka [20](JF 2010,65(4):1369–1407)用 2001–2005 年 NYSE 股票数据,把每个交易日切成 13 个半小时区间,发现**某个半小时区间的收益与"整数个交易日之前的同一区间"收益正相关**,这个持续性效应能维持约 **40 个交易日**,在**开盘和收盘半小时最强**(但不限于这两段);**成交量、委托不平衡、波动率、买卖价差都呈现相似的日内模式,但它们不能解释这个收益模式**。
   翻译:这给了两条可直接用的信息:(i)"同一时段跨日比较"(今天这个半小时 vs 过去 N 天同一个半小时)是文献验证过的构造,比"整天聚合"更贴近真实机制,可以翻译成 `ts_mean(某半小时区间信号, 40)` 这类跨日同时段聚合,而不是对全天任意聚合;(ii)**量、价差、波动率的日内模式不能解释收益模式**,这正面支持了 analysis.md §4.1 第 1 族"避开已见过的波动/成交量词汇、找真正的无量纲时点特征"的思路——文献自己说了,时点效应不是波动或流动性的马甲。

2. **按规模/流动性分组后,尾盘占比效应的方向会反转,不能假设单一符号。** Bogousslavsky [3](JFE 2021,141(1):172–194,与 L1 共用)发现**小盘、低流动性股票的尾盘 30 分钟收益高,但隔夜收益大幅为负;大盘、高流动性股票恰好相反**,机制是套利资金对隔夜持仓的保证金/融券费约束使其在收盘前退出头寸。
   翻译:这条同时回应 L1 和 L4——"尾盘占比"类特征(`day_at_max_ratio`、`day_centroid` 一类)如果要在 A 股用,方向大概率需要按规模或流动性分组后才稳定,不能指望全市场单一方向;而 analysis.md §4.1 建议用 `ListAge` 做条件化,**这与文献用 size/liquidity 条件化不完全同构**,没有查到直接对应 `ListAge` 的先例(与 L1 的空白重复,此处再记一次)。

3. **日内成交分布的"形状"指标(重心、基尼系数)在成交量预测/经纪商集中度研究里有用,但没有查到直接拿来预测个股未来收益的同行评审文献。** 搜索只找到用 Gini 系数衡量**经纪商层面**交易集中度(台湾数据)、**期货合约**日内成交集中度(衡量少数大单 vs 多数小单)的研究,它们测的是"谁在交易"或"交易方式",**不是**我们池子里 `day_centroid(Amt)`、`day_gini(Amt)` 这种"全天成交量按时间分布的形状"直接作为个股横截面收益预测变量。
   翻译:这是一条明确的空白——如果核心 A 的外围族要用 `day_centroid`/`day_gini` 做伙伴,这是**文献没有直接检验过的组合**(风险和机会并存,analysis.md §4.1 本身也这么说),不能假设它有文献背书。

4. **A 股的收盘集合竞价制度是 2018 年引入的,这是构造"尾盘"特征时需要注意的制度背景(非学术文献,仅作背景事实,不计入引用证据)。** 公开报道显示,上交所自 2018 年 8 月 20 日起改用收盘集合竞价产生收盘价(14:57–15:00 集合竞价,不可撤单)。这条是制度公告层面的事实,不是同行评审研究,**不满足"论文/工作论文/研究报告"的引用要求**,只在这里提示 PI:2018-08-20 之前与之后的"尾盘"数据在 A 股的生成机制不同,如果种子的回看窗口跨过这个日期,"尾盘占比"类特征的含义可能不连续;train 窗口(2018-01-02 起)刚好跨过这个日期,需要注意。

**搜不到的地方(明确空白):**
- 日内成交量/收益的重心、基尼系数、到达最大值的时点,作为个股横截面收益预测变量的同行评审检验,没有查到(见上第 3 点)。
- "尾盘占比"与次日/次月收益关系的 A 股专门学术研究,没有查到——只搜到美股证据([3])和 A 股的制度公告,没有同行评审论文把二者连起来。
- 2018 年上交所收盘集合竞价改革前后,"尾盘成交占比"这类特征在横截面检验中是否出现结构断点,没有查到专门研究(这本身是一个 r3 可以追的方法学问题,不是本轮能填的)。
- `ListAge` 作为日内时点特征条件化变量的先例,没有查到(与 L1 共同的空白)。

---

## 参考文献

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|---|
| 1 | A tug of war: overnight versus intraday expected returns | Dong Lou, Christopher Polk, Spyros Skouras | 2019(*Journal of Financial Economics*, Vol. 134, No. 1, pp. 192–213);工作论文版本至少 2015 年即流传(FMG DP744) | Journal of Financial Economics / LSE 工作论文 | https://researchonline.lse.ac.uk/id/eprint/87481 ; https://www.fmg.ac.uk/sites/default/files/publications/DP744.pdf | true |
| 2 | Paying Attention: Overnight Returns and the Hidden Cost of Buying at the Open | Henk Berkman, Paul D. Koch, Laura Tuttle, Ying Jenny Zhang | 2012-08(*Journal of Financial and Quantitative Analysis*, Vol. 47, No. 4, pp. 715–741) | Journal of Financial and Quantitative Analysis | https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/paying-attention-overnight-returns-and-the-hidden-cost-of-buying-at-the-open/F9AAD159B512C651F09D5D52011D88E0 ; https://kuscholarworks.ku.edu/bitstream/1808/10965/1/Koch_Paying%20Attention.pdf | true |
| 3 | The cross-section of intraday and overnight returns | Vincent Bogousslavsky | 2021(*Journal of Financial Economics*, Vol. 141, No. 1, pp. 172–194),DOI 10.1016/j.jfineco.2020.07.020 | Journal of Financial Economics | https://doi.org/10.1016/j.jfineco.2020.07.020 | true |
| 4 | Overnight returns, daytime reversals, and future stock returns | Ferhat Akbas, Ekkehart Boehmer, Chao Jiang, Paul D. Koch | 2022(*Journal of Financial Economics*, Vol. 145, No. 3, pp. 850–875),DOI 10.1016/j.jfineco.2021.09.019 | Journal of Financial Economics | https://ideas.repec.org/a/eee/jfinec/v145y2022i3p850-875.html | true |
| 5 | 中国股票市场月频动量效应消失之谜——基于T+1制度下隔夜折价现象的研究 | 白颢睿、吴辉航、柯岩 | 2020-04(《财经研究》第 46 卷第 4 期,140–154 页),DOI 10.16538/j.cnki.jfe.2020.04.010 | 财经研究 | https://qks.shufe.edu.cn/J/PDFFullDown/A67fdee67-f823-44ad-8489-d42bcfae03ae | true(标题、作者、期刊卷期、主要结论经搜索结果摘要核实;全文 PDF 未能直接读取文字层) |
| 6 | Overnight versus intraday returns of anomalies in China | Chaonan Lin, Hui-Wen Chang, Robin K. Chou | 2023-06(*Pacific-Basin Finance Journal*, Vol. 79, Article 102007),DOI 10.1016/j.pacfin.2023.102007 | Pacific-Basin Finance Journal | https://ideas.repec.org/a/eee/pacfin/v79y2023ics0927538x23000732.html | true(标题、作者、期刊卷期、摘要核心结论经 WebFetch 直接核实;确切出版月份"2023-06"来自国立政治大学教师著作列表,未在 Elsevier 页面上直接核实到日期) |
| 7 | Share Issuance and Cross-Sectional Returns | Jeffrey Pontiff, Artemiza Woodgate | 2008-04(*Journal of Finance*, Vol. 63, No. 2, pp. 921–945) | Journal of Finance | https://ideas.repec.org/a/bla/jfinan/v63y2008i2p921-945.html | true |
| 8 | Market Reactions to Tangible and Intangible Information | Kent Daniel, Sheridan Titman | 2006(*Journal of Finance*, Vol. 61, No. 4, pp. 1605–1643);NBER WP9743 更早流传 | Journal of Finance / NBER | https://ideas.repec.org/p/nbr/nberwo/9743.html | true |
| 9 | The Expiration of IPO Share Lockups | Laura Casares Field, Gordon Hanka | 2001-04(*Journal of Finance*, Vol. 56, No. 2, pp. 471–500) | Journal of Finance | https://ideas.repec.org/a/bla/jfinan/v56y2001i2p471-500.html | true(标题、作者、卷期、−1.5%/3 日异常收益、交易量+40%、无内部人卖出仍显著等结论经多个二次来源交叉确认;未直接读取全文 PDF) |
| 10 | 可交易性折扣、价值转移与限售股解禁 | 刘娥平、唐舜 | 2014(《财经研究》第 40 卷第 9 期,86–96 页) | 财经研究 | https://qks.sufe.edu.cn/J/ArticleQuery/A160824000481/CN | true(WebFetch 直接读取页面上的标题、作者、期刊卷期与方法/结论摘要) |
| 11 | What Determines Chinese Stock Returns? | Fenghua Wang, Yexiao Xu | 2004-11(*Financial Analysts Journal*, Vol. 60, No. 6, pp. 65–77) | Financial Analysts Journal | https://ideas.repec.org/a/taf/ufajxx/v60y2004i6p65-77.html | true(WebFetch 直接读取标题、作者、卷期与摘要) |
| 12 | The Cross-Section of Volatility and Expected Returns | Andrew Ang, Robert J. Hodrick, Yuhang Xing, Xiaoyan Zhang | 2006-02(*Journal of Finance*, Vol. 61, pp. 259–299);NBER WP10852,2004-10 | Journal of Finance / NBER | https://www.nber.org/papers/w10852 | true |
| 13 | Maxing Out: Stocks as Lotteries and the Cross-Section of Expected Returns | Turan G. Bali, Nusret Cakici, Robert F. Whitelaw | 2011-02(*Journal of Financial Economics*, Vol. 99, No. 2, pp. 427–446);NBER WP14804,2009-03 | Journal of Financial Economics / NBER | https://www.nber.org/papers/w14804.pdf | true |
| 14 | Unknown Unknowns: Uncertainty About Risk and Stock Returns | Guido Baltussen, Sjoerd van Bekkum, Bart van der Grient | 2018(*Journal of Financial and Quantitative Analysis*, Vol. 53, No. 4);工作论文版本至少 2012 年流传("Uncertainty and Stock Returns") | Journal of Financial and Quantitative Analysis | https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/unknown-unknowns-uncertainty-about-risk-and-stock-returns/6E0E98349D20C1DCF67F3A0452361B80 ; https://personal.eur.nl/vanbekkum/2018JFQA_unknown_unknowns.pdf | true(标题、作者、期刊卷期、"8%/年跑输"核心结论在搜索结果摘要里直接出现;未逐页核实全文) |
| 15 | Is the idiosyncratic volatility anomaly driven by the MAX or MIN effect? Evidence from the Chinese stock market | Xiaoyuan Wan | 2018(*International Review of Economics & Finance*, Vol. 53, pp. 1–15),DOI 10.1016/j.iref.2017.10.015 | International Review of Economics & Finance | https://ideas.repec.org/a/eee/reveco/v53y2018icp1-15.html | true(WebFetch 直接核实标题、作者、期刊卷期与"MAX 被 IVOL 吸收、IVOL 不被 MAX 吸收"的核心结论;MAX/MIN 的具体度量公式未核实到) |
| 16 | The MAX Effect: Lottery Stocks with Price Limits and Limits to Arbitrage | Weifeng Hung, Jimmy Yang | 2018(*Journal of Financial Markets*, Vol. 41, pp. 77–91) | Journal of Financial Markets | https://ideas.repec.org/a/eee/finmar/v41y2018icp77-91.html | true(与 r1 lit.md 的 [8] 同一篇,本轮再次确认适用于 head 1) |
| 17 | Do extreme returns matter in emerging markets? Evidence from the Chinese stock market | Gilbert V. Nartea, Dongmin Kong, Ji Wu | 2017(*Journal of Banking & Finance*, Vol. 76, pp. 189–197) | Journal of Banking & Finance | https://ideas.repec.org/a/eee/jbfina/v76y2017icp189-197.html | true(与 r1 lit.md 的 [7] 同一篇,本轮用于对照 [15] 的不一致结论) |
| 18 | The Volatility Effect: Lower Risk Without Lower Return | David Blitz, Pim van Vliet | 2007(*Journal of Portfolio Management*, Fall 2007, pp. 102–113);SSRN 工作论文 980865 更早流传 | Journal of Portfolio Management / SSRN | https://papers.ssrn.com/abstract=980865 | true(标题、作者、期刊、"全球多空年化 alpha 差 12%(1986–2006)"核实;多头腿单独的具体数字未核实,见正文) |
| 19 | Benchmarks as Limits to Arbitrage: Understanding the Low-Volatility Anomaly | Malcolm Baker, Brendan Bradley, Jeffrey Wurgler | 2011(*Financial Analysts Journal*, Vol. 67, No. 1);工作论文 2010 年即流传 | Financial Analysts Journal | https://www.cfainstitute.org/en/research/financial-analysts-journal/2011/benchmarks-as-limits-to-arbitrage-understanding-the-low-volatility-anomaly ; https://papers.ssrn.com/abstract=1745108 | true |
| 20 | Intraday Patterns in the Cross-Section of Stock Returns | Steven L. Heston, Robert A. Korajczyk, Ronnie Sadka | 2010(*Journal of Finance*, Vol. 65, No. 4, pp. 1369–1407);工作论文至少 2008 年即流传 | Journal of Finance | https://arxiv.org/pdf/1005.3535 ; https://www.bauer.uh.edu/departments/finance/documents/Heston_Korajczyk_Sadka_paper_UH.pdf | true |

---

## 给 PI 的检索空白清单(明确搜不到,不要当成"文献证伪")

- L1:一字板/涨跌停开盘价在隔夜收益构造里的具体处理方式,搜不到;集合竞价价格 vs 开盘后第一笔价格的定义对比,搜不到;[1] 效应持续"数年"的具体半衰期数字,搜不到;用 `ListAge` 做隔夜/日内效应条件化的先例,搜不到(与 L4 共同空白)。
- L2:composite equity issuance 异象与 free float ratio 异象是否为同一机制的系统性对比文章,搜不到;A 股定向增发作为独立供给冲击的同行评审横截面检验,搜不到;`LogFloatShares` 变动与 log 市值恒等式的共线性处理方法,搜不到。
- L3:同一日度风险量不同幂次/Lp 聚合的样本外系统比较,搜不到(与 r1 一致,本轮未发现新证据);低波动多头腿单独对"波动度量方式"的敏感性检验,搜不到;已实现方差(非隐含波动率)的 vol-of-vol 在 A 股的独立定价检验,搜不到;Blitz–van Vliet 多头腿单独的可核实具体数字,搜不到。
- L4:`day_centroid`/`day_gini` 一类日内分布形状指标直接预测个股未来收益的同行评审文献,搜不到;A 股"尾盘占比"与次日/次月收益关系的专门学术研究,搜不到;2018 年上交所收盘集合竞价改革前后的结构断点研究,搜不到。
