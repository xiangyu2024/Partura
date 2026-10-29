# 文献:种子 804,B 组,第 1 轮

输入:`r1/analysis.md` 第 5 节「给文献员的题目」(4 题,分别对准核心 ①②③ 与灵感 1/2/3)。
约束:只用 **2023-08-08 之前**发表/上线/存档的论文、工作论文或机构研究报告;日期拿不准的一律不用(下面逐条注明判断依据)。
工具:WebSearch(多轮)+ WebFetch(核对个别条目的作者/期号/日期)。下面每条「处理方式」后括注的是它的出处标号,对应该题下方「文献出处」表里的条目。

---

## 题 1(对准核心 ①、来源 A):名义股价水平作为截面特征

### 1.1 能翻译成算子语言的处理方式

1. **对价格取对数,而不是用原始价格水平。** 名义股价在美股几十年里稳定在一个常数附近(由拆股维持),这个常数本身跨市场、跨时代变化很大,
   所以文献几乎都先取 `log(price)` 再做横截面比较,不直接用原始价格 [①②]。→ 对应我们这批 head 里 `pow_3(day_mean(Open))` 这种单调外壳:
   在最后一层取 z-rank 的框架下外壳本身无效,但提示**该用哪个尺度**(log 还是别的单调变换)仍值得单独试,而不是想当然用原始价格或立方。
2. **把价格分解成「基本面能解释的部分」与「残差」两段,只用残差。** Birru & Wang 用每股资产、每股净资产、每股收益、每股股利回归出一个
   `fitted price`,再用「实际价格 − fitted price」的残差做分层,理由是原始价格排序会把价格和预期收益的机械联系(低价股往往基本面也差)混进去,
   直接排序会**低估**真实的低价溢价 [③]。→ 这是本轮最值得抄的一条:把 `day_mean(Open)`(或其平滑)对我们已有的日频基本面叶子
   (`LogFloatCap`、`LogTotalCap` 等)做横截面回归,取残差再喂给 `cs_first_low20`,而不是直接用价格本身 —— 这样「低价」里刨掉了「本来就该便宜」的部分。
3. **按规模做双重排序(先分市值组,组内再按价格排序),而不是把市值当线性控制变量减掉。** 早期美股证据(Goodman & Peavy)与波兰市场证据
   (Zaremba 等)都用「价格 × 规模」双重排序,而不是回归控制,理由是线性回归控制拿不掉尾部效应——这与解剖员 1.3 节的担心(线性 `LogFloatCap`
   控制拿不掉 `cs_first_low20` 这种指示函数型暴露)是同一个问题,文献给的是**同一个解法方向**:双重排序 / 分组后排序,而不是线性正交化 [④]。
4. **价格本身是投资者用来给股票分类的标签,相近价位的股票会联动。** Green & Hwang 发现拆股前后,股票与「低价组」「高价组」的联动会跟着价格
   档位切换,而且这个联动**不能**被规模、流动性、信息扩散解释掉 [⑤]。→ 支持把「价格分段」当成一个独立、非线性的分类变量来处理
   (我们现在的 `cs_first_low20(y, 价格)` 做法),而不是简单把价格揉进一个连续的线性因子里。
5. **价格溢价的方向和幅度依赖持有期、风险模型,且受规模主导的样本权重影响。** 多篇文献提示:用等权还是市值加权结果会很不一样,极端分组里
   微盘股占比压倒性(Fama & French 的证据,见题 2),所以「低价」在很大程度上和「微盘」高度重叠,报告出来的溢价大小对权重方案很敏感 [⑥]。
   → 提醒 PI:E/R 任务里如果换成等权或别的加权读出来的 score 差很大,不必惊讈,这是文献里的常见现象,不代表 bug。

**没找到、如实注明搜不到**:专门针对中国 A 股「名义股价 / 每股价格」效应、且能确认 2023-08-08 之前上线的实证论文。
搜到一篇张冰(Bing Zhang)《Betting against low nominal prices: Evidence from China》(International Review of Economics & Finance, vol. 88, 2023,
pp. 476–500,DOI 10.1016/j.iref.2023.06.017),内容正好是 A 股低价股溢价、且归因于现金流 beta 而非贴现率 beta,方向和我们 1.3 节的「时段依赖」
担忧高度相关 —— 但页面只给出年份 2023 和卷期号,没有「在线发表」的具体日期,DOI 里的 `2023.06` 只是推断、不是确认,**按规矩不采用**,
PI 如果认为值得读可以自己核实日期后再决定。

### 1.2 文献出处

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|---|
| ① | The Nominal Share Price Puzzle | William C. Weld, Roni Michaely, Richard H. Thaler, Shlomo Benartzi | 2009(春季,vol. 23 no. 2, pp. 121–142) | Journal of Economic Perspectives | https://ideas.repec.org/a/aea/jecper/v23y2009i2p121-42.html | true |
| ② | Nominal Price Illusion | Justin Birru, Baolian Wang | 2016(vol. 119 no. 3, pp. 578–598) | Journal of Financial Economics | https://www.ivey.uwo.ca/media/3777565/birru.pdf | true |
| ③ | The Nominal Price Premium(工作论文,后部分内容并入②) | Justin Birru, Baolian Wang | 2015 初版,2016-03 修订版(Ohio State Dice Center WP 2015-15 / SSRN 2646775) | SSRN / Fisher College of Business 工作论文 | https://www.ivey.uwo.ca/media/3775564/birru.pdf | true |
| ④ | 低价股效应综述与双重排序证据(Goodman & Peavy 早期美股证据 + Zaremba 等波兰市场证据,经二级来源转述,未直接读到原文) | Goodman & Peavy(1986,原文未直接核实);Zaremba et al.(波兰市场,具体年份未核实) | 未能完全核实(下方注明) | 二级综述转述 | 搜索结果转述,无直接可核实链接 | false |
| ⑤ | Price-based return comovement | Jason Green, Byoung-Hyoun Hwang | 2009(vol. 93 no. 1, pp. 37–50) | Journal of Financial Economics | https://ideas.repec.org/a/eee/jfinec/v93y2009i1p37-50.html | true |
| ⑥ | Dissecting Anomalies(规模/权重敏感性部分,与题 2 共用) | Eugene F. Fama, Kenneth R. French | 2008-08(vol. 63 no. 4, pp. 1653–1678) | Journal of Finance | https://www.johnhcochrane.com/s/fama_french_dissecting_anomalies_JF.pdf | true |

说明:④ 是从搜索结果的二级转述里拼出来的(「Goodman and Peavy (1986) 低价效应在控制规模后仍存在」「Zaremba 等在波兰市场发现低价效应反向,
与双重排序方法并用」),没有拿到可独立核实的标题全文或直接链接,按规矩 `verified: false`,**PI 用这条时要知道它没有被我真正核实过**,
只当作一个方向提示,不要当成结论引用。

---

## 题 2(对准核心 ①/来源 B「同一根轴」问题,以及灵感 3):股本数量、自由流通比例、规模的非线性暴露

### 2.1 能翻译成算子语言的处理方式

1. **股本的处理单位是「同比变化量」,不是「水平值」。** Pontiff & Woodgate 和 Fama & French 用的「净发行」变量是
   `log(1 + 过去一个财年流通股数的增长率)`,不是股数本身的水平,他们发现这个**变化量**对收益的预测力比市值、账面市值比、动量都强,
   且在极端分组(微盘)里最强 [①②]。→ 这是本轮没试过的一个高性价比外围:core① / core②(或 B 轴)外面长一个 `cross_ema(LogFloatShares, 241)`
   的**时间差分**(例如 `ts_delta(LogFloatShares, 252)` 或类似的年度变化率),而不是只平滑水平值——解剖员已经确认平滑窗口不敏感,
   但「变化 vs 水平」这个维度完全没被碰过。
2. **规模的非线性暴露,标准做法是:先把(标准化后的)规模取三次方,再用加权回归把它相对线性规模正交化,最后再做截尾和标准化。**
   这是 MSCI Barra 美股模型(USE4)与中国股票模型(CNE5)「Non-Linear Size」因子的构造方式,专门用来捕捉「线性市值因子吸收不掉的
   中段最优 / 尾部效应」[③④]。→ 这正好是解剖员 1.3 节担心的问题(线性 `LogFloatCap` 控制拿不掉 `cs_first_low20` 的指示函数暴露)的**标准解法**:
   把 `pow_3(rank(LogFloatCap))` 或 `pow_3(rank(LogTotalCap))` 这类立方项,对线性的 `LogFloatCap` 做加权回归取残差,再丢给 GP 当 y 或当条件变量,
   比直接做指示函数分段更接近「文献标准做法」,也更容易在样本外复现(因为不是一个离散阈值)。
   MSCI 的 Mid-Cap Effect 报告进一步给出这个因子在实际组合里的解读参照 [⑤]。
3. **自由流通比例 / 非流通股比例可以当一个独立于市值的特征,但它与收益的关系在文献里并不稳定,与流动性、波动的关系更稳定。**
   伊斯坦布尔交易所的实证发现自由流通比例越高,成交活跃度和收盘价水平越高,但价格波动也越高,控制公司规模后结论不变,
   该研究**没有**发现自由流通比例与「收益」本身有稳定关系 [⑥]。→ 这提示:`sub(LogTotalCap, LogFloatCap)`(= log 非流通比例,解剖员在灵感 1
   里提到的、不在控制里的干净特征)如果直接当 alpha 可能效果有限,但当成**波动 / 流动性的条件变量**(例如只在高非流通比例的股票里看某个信号)
   文献证据更支持。
4. **关于中国 A 股限售股:搜到方向、没搜到能核实的具体文献。** 搜索结果提到过《财经研究》2008 年有一篇用股改前非流通股协议转让价与股改后
   限售股转让价估计「流通性价值」的研究,结论是股改前流通性价值均值约 66%、股改后约 56%,但搜索结果只给了期刊名和年份,
   没有给出可核实的标题、作者或链接,**按规矩不采用**,如实记录为搜到方向但搜不到可引用的具体出处。

### 2.2 文献出处

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|---|
| ① | Share Issuance and Cross-sectional Returns | Jeffrey Pontiff, Artemiza Woodgate | 2008-04(vol. 63 no. 2, pp. 921–945) | Journal of Finance | https://ideas.repec.org/a/bla/jfinan/v63y2008i2p921-945.html | true |
| ② | Dissecting Anomalies | Eugene F. Fama, Kenneth R. French | 2008-08(vol. 63 no. 4, pp. 1653–1678) | Journal of Finance | https://www.johnhcochrane.com/s/fama_french_dissecting_anomalies_JF.pdf | true |
| ③ | The Barra US Equity Model (USE4) Methodology Notes | Jose Menchero, D.J. Orr, Jun Wang | 2011-08 | MSCI Barra Research Notes | https://www.msci.com/documents/10199/242721/Barra_US_Equity_Model_USE4.pdf | true |
| ④ | The Barra China Equity Model (CNE5) — Empirical Notes | Igor Mashtaler, D.J. Orr | 2012-07 | MSCI Barra Research Notes | https://support.msci.com/www/research-report/the-barra-china-equity-model/014459336 | true |
| ⑤ | Global Market Report — The Mid-Cap Effect | MSCI Research | 2012-12 | MSCI 研究报告 | https://www.msci.com/research-and-insights/paper/global-market-report-the-mid-cap-effect-december-2012 | true |
| ⑥ | The Effects of Free Float Ratios on Market Performance: An Empirical Study on the Istanbul Stock Exchange | Faruk Bostanci, Saim Kilic | 2010 | Istanbul Stock Exchange Review, vol. 12 no. 45, pp. 1–14 | https://ideas.repec.org/a/bor/iserev/v12y2010i45p1-26.html | true |

---

## 题 3(对准「条件化」方法本身,核心 ②、灵感 1):只在某一段股票里用某个信号 —— 怎么做、怎么验?

### 3.1 能翻译成算子语言的处理方式

1. **条件排序(先按 x 分段、再在段内按 y 排)和独立排序(x、y 各自独立分段再取交集)是两种不同的方法,条件排序对「先按哪个变量分段」敏感,
   独立排序在高维时容易出现空桶。** 这正是我们 `cs_first_low20(y, x)` 的结构(先按 x 分出最低 20% 这一段,再在段内按 y 排序),属于标准的
   「条件 / 依赖排序」一类 [①,方法学背景经 R 包 `portsort` 文档与 ② 交叉确认]。文献里两者的差异只在两个以上特征时才会显现——
   对我们只有一层分段的 `cs_first_low20` 影响有限,但如果 PI 想做解剖员提到的「双重分段」(先 `cs_first_low20` 再 `cs_last_low10`),
   **分段顺序会改变结果**,这是文献里明确提示过的坑,应该把两种顺序都当独立候选评估,不能假设对称。
2. **分段宽度(10% / 20% / 三分位等)的选择本质是一个偏差—方差取舍:段越窄,段内噪声越大(方差高),段越宽,段里混入的「不该被筛中」的
   股票越多(偏差高)。** Cattaneo、Crump、Farrell、Schaumburg 给了特征排序组合的正式估计理论,专门有一节讨论这个「均方展开」的权衡,
   并给出对规模和动量异象的实证应用作为参照 [②]。→ 支持解剖员已经建议的「换别的分段算子、换分段宽度」方向,
   也提示:如果 GP 在 E 任务里把 20% 的段宽变成一个自由参数去优化,要留意这是一个已知的偏差—方差旋钮,不是额外的自由信息。
3. **系统性地对一大批已知异象做两两条件排序,会产生大量「看起来显著」的交互效应,必须用多重检验校正(如 Bonferroni)才能分辨真假,
   而且交互收益主要集中在少数几类特征(过去收益类、交易成本类)上,会随时间衰减。** Müller & Schmickler 对 102 个异象做了全部两两双重排序
   (10,302 组),校正多重检验后约 8%(EW)的组合仍显著,但增益主要来自短期反转和规模(交易成本)两类,且 2000 年后结构发生变化 [③]。
   → 直接支持解剖员 1.7 节的警告(「共性表这一轮基本在追踪血脉,不是因果」):条件化/交互构造极易产生虚假显著,
   我们现在靠「score ≥ 0.5 门槛 + 库内 ρ 禁令」做的把关,相当于一个粗糙的多重检验校正,但没有 Müller & Schmickler 那种显式的统计校正,
   值得在 PI 写任务笔记时标注这一点,不代表要改判读规则(那不是我们的权限)。
4. **发现新因子的统计门槛,在「已经做过大量隐性数据挖掘」的前提下应该远高于传统的 t ≥ 2。** Harvey, Liu & Zhu 的多重检验框架给出 t ≥ 3.0
   (对应 p < 0.0027)作为「新发现因子」的合理门槛,专门针对金融文献里普遍存在的、未被报告的大量尝试 [④]。
   → 我们的 score 门槛(≥0.5,且是 train/valid 较差者)本身不是 t 统计量,不能直接套用这个数字,但方向一致:
   **条件化 / 交互类因子的「新信息」声称应该比普通因子更谨慎**,这呼应了核心 ① 的奖励设计(加入家族控制、只奖励新信息)本身的用意。
5. **已发表的异象在发表后收益会系统性衰减(平均约 58%),部分是统计偏差(约等于样本外衰减的上限 ~26%),部分是「发表后被套利吃掉」。**
   McLean & Pontiff 用 97 个已发表的预测变量实测了这个衰减,并发现衰减在大盘、流动性好、高分红的股票里更明显 [⑤]。
   → 提醒 PI:即使某个条件化因子在 train/valid 都好看,也要对它的持久性打折,尤其是解剖员已经指出 valid 期夏普是 train 的 2–3 倍这种
   「吃时段」的迹象——这与「条件化因子的样本外稳定性」这个题目问的正是同一件事,文献证据是：会衰减,但衰减主要来自「被发表之后」,
   我们这里是内部挖掘、没有发表这一步,衰减幅度未必能直接套用这个数字。

### 3.2 文献出处

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|---|
| ① | （方法学背景,非单一论文:条件排序 vs 独立排序的标准定义,经 `portsort` R 包文档与 ② 交叉确认,不单独计分) | — | — | R 包文档(`portsort`),辅助背景 | https://www.stats.bris.ac.uk/R/web/packages/portsort/vignettes/portsort.html | true |
| ② | Characteristic-Sorted Portfolios: Estimation and Inference | Matias D. Cattaneo, Richard K. Crump, Max H. Farrell, Ernst Schaumburg | 2018-09(arXiv 首版 2018-09-10;正式发表 2020,Review of Economics and Statistics, vol. 102 no. 3, pp. 531–551) | arXiv / Review of Economics and Statistics | https://arxiv.org/abs/1809.03584 | true |
| ③ | Interacting Anomalies | Karsten Müller, Simon Schmickler | 2020-07(工作论文) | SSRN 工作论文(经二级来源 CXO Advisory 转述确认主要数字,未直接打开 SSRN 页面) | https://www.cxoadvisory.com/equity-premium/best-stock-return-anomaly-double-sorts/ | true |
| ④ | ...and the Cross-Section of Expected Returns | Campbell R. Harvey, Yan Liu, Heqing Zhu | 2014-10(NBER WP No. 20592);正式发表 2016(Review of Financial Studies, vol. 29 no. 1, pp. 5–68) | NBER 工作论文 / Review of Financial Studies | https://www.nber.org/papers/w20592 | true |
| ⑤ | Does Academic Research Destroy Stock Return Predictability? | R. David McLean, Jeffrey Pontiff | 2016-02(vol. 71 no. 1, pp. 5–32) | Journal of Finance | https://www.gwern.net/doc/economics/2016-mclean.pdf | true |

说明:①不是一篇独立论文,是方法学背景的转述确认,不计入独立文献数;③只读到二级转述(CXO Advisory 的总结),没有打开 SSRN 原页面核实,
但数字在该转述里给得很具体(10,302 组双重排序、Bonferroni 校正、797/351 组显著),判断为 `verified: true` 是指「确实在搜索结果里看到了这些具体说法」,
不是指我核对过 SSRN 原文每个数字,PI 使用时请知道这一层区别。

---

## 题 4(对准核心 ③、灵感 2):日内成交量的时点分布作为截面预测变量

### 4.1 能翻译成算子语言的处理方式

1. **U 形日内成交量不是外生给定的,是知情交易者和流动性交易者「择时」的策略均衡结果 —— 知情交易者倾向在交易量大、价格更有信息含量的时段
   加大交易,流动性交易者也倾向在同样的时段交易以降低冲击成本,两者互相强化出 U 形。** 这是该领域的理论源头 Admati & Pfleiderer 的核心机制 [①]。
   → 支持把 `day_centroid(sqrt(Volume))`(成交量质心)当成一个「信息 / 择时」代理变量来处理是有理论依据的,而不是纯粹的技术噪声特征;
   但理论本身预测的是「U 形」而不是「质心偏移」,质心这个统计量把开盘和收盘两段的信息混在一个数里,**理论并不直接支持单一质心有方向性**,
   这是我们核心③「risk:它的单独 score 未知」的一个理论侧面的呼应 —— 值得先用 R 评估把开盘段和收盘段分开算,而不是只看一个合成质心。
2. **把一天分成离散的时间窗口(尤其是「第一个半小时」和「最后一个半小时」),比用连续的全天质心更能抓到可预测性,且这个可预测性在控制了
   成交量、订单失衡、波动率之后依然存在。** Heston, Korajczyk & Sadka 发现半小时收益在「整数个交易日」的间隔上有持续性,
   在开盘和收盘半小时最强,且这个模式不能被当天的量/失衡/波动解释掉,也不是规模或系统性风险驱动的 [②]。Gao, Han, Li & Zhou 进一步发现
   单只股票(或指数)「第一个半小时收益」能预测「最后半小时收益」,这是一个具体可复制的时间窗口动量结构,不是质心这种连续统计量 [③]。
   → 给核心③一个更具体、文献验证过的外围方向:把 `day_centroid` 换成或配合「开盘段 vs 收盘段」的离散切片(比如前 30 分钟成交额占比、
   后 30 分钟成交额占比,或者前 30 分钟收益本身),而不是只停留在一个连续质心统计量上。
3. **知情交易者的隱蔽交易(stealth trading)在开盘和收盘时段对价格的冲击最大,中段(midday)相对最弱,这与交易量的 U 形时段重合但角度不同:
   它看的是「不同交易规模的冲击」,不是「成交量本身」。** Blau, Van Ness & Van Ness 在 NYSE 数据上发现,大额交易在开、收盘段对价格的
   冲击显著大于中段 [④]。→ 提示:如果要把 `day_centroid` 这类日内形状特征做得更精细,可以不只用 `Volume` 或 `Amt`,
   而是按成交单大小分层后再算质心或占比(例如区分大单 / 小单的日内分布),这是文献里用来分离「知情 vs 噪声」交易的常见处理,
   比单纯换 `sqrt(Volume)` 为 `Volume` / `Amt`(解剖员已经建议的敏感性测试)更进一步。

### 4.2 文献出处

| # | 标题 | 作者 | 年-月 | 来源 | 链接 | verified |
|---|---|---|---|---|---|---|
| ① | A Theory of Intraday Patterns: Volume and Price Variability | Anat R. Admati, Paul Pfleiderer | 1988(vol. 1 no. 1, pp. 3–40) | Review of Financial Studies | https://da.lib.kobe-u.ac.jp/da/kernel/81000053/81000053.pdf | true |
| ② | Intraday Patterns in the Cross-Section of Stock Returns | Steven L. Heston, Robert A. Korajczyk, Ronnie Sadka | 2010-08(vol. 65 no. 4, pp. 1369–1407) | Journal of Finance | https://arxiv.org/pdf/1005.3535 | true |
| ③ | Market Intraday Momentum | Lei Gao, Yufeng Han, Sophia Zhengzi Li, Guofu Zhou | 2018(vol. 129 no. 2, pp. 394–414) | Journal of Financial Economics | https://doi.org/10.1016/j.jfineco.2018.05.009 | true |
| ④ | Intraday Stealth Trading: Which Trades Move Prices During Periods of High Volume? | Benjamin M. Blau, Bonnie F. Van Ness, Robert A. Van Ness | 2009(vol. 32 no. 1, pp. 1–21) | Journal of Financial Research | https://ideas.repec.org/a/bla/jfnres/v32y2009i1p1-21.html | true |

**没找到、如实注明搜不到**:专门针对中国 A 股(尤其是 CSI300 / 沪深300 成分股)日内成交量时点分布作为**横截面**预测变量的研究。
搜到一篇利物浦大学的博士论文(Dongqi Sun,《An Examination of Informed Trades in China's Stock Market》,用 2012–2014 年 CSI300 高频数据,
发现 U 形日内成交量 / 波动 / 流动性 / 价格发现模式),但其机构存档记录的存档日期是 **2023-08-30**,晚于本题的硬截止 2023-08-08,**排除不用**。
另搜到一篇看起来高度相关的中国市场「开盘半小时成交量占比预测收尾盘收益」论文(International Journal of Financial Studies),
但该刊卷号(vol. 14)对应年份推算在 2026 年附近,无法确认是 2023-08-08 之前发表,**同样排除不用**。

---

## 给 PI 的一句话总结

四题里最值得直接变成外围写法的两条:(1)题 2 的「立方 + 加权回归正交化」是解剖员 1.3 节「线性 `LogFloatCap` 控制拿不掉非线性尾部暴露」
这个顾虑的标准文献解法,比继续用离散分段(`cs_first_low40` 等)更接近「新处理方式」;(2)题 1 的「价格对基本面叶子回归取残差」
是另一条没试过的、能直接把「核心 ① 之外的新信息」往「价格的非价格面解释部分」上引的路。题 3 和题 4 更偏方法论风险提示,
不直接给出新结构,但题 4 的「开盘/收盘离散窗口 优于 连续质心」这条,对核心③要不要占 E 位、怎么设计 R 的直接评估,是有具体指导意义的。
