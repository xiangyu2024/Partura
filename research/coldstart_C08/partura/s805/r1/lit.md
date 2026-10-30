# 文献:种子 805,第 1 轮(文献员)

对准 `analysis.md` §5 的 4 个题目,核心是 `day_centroid(Volume)`(日内成交量在时间轴上的重心)及其外围候选
(水平 vs 自身历史偏离、上下午不对称、板块/涨跌停代理)。检索工具 WebSearch/WebFetch,只收 **2023-08-08 之前**
发表或挂出的论文、工作论文、研究报告;日期对不上或查不到首版日期的一律不用。每条"处理方式"后标出处,每个出处
给标题、作者、年-月、来源、链接、`verified`。**搜不到的直接写"搜不到",没有编造任何文献或数字。**

---

## 题目 1——对准核心 `day_centroid(Volume)`:日内成交时点怎么被构造成选股特征

**找到的处理方式:**

1. **U 形本身被当成"策略性聚集"的结果,不是噪音。** Admati & Pfleiderer (1988) 的模型把开盘/收盘两端的高成交量
   解释为知情交易者与流动性交易者**策略性地选择在同一时段交易**(流动性交易者躲进厚的市场、知情者之间的竞争
   压低各自的信息优势)。翻译成算子语言:`day_centroid` 的两个端点权重(开盘竞价占比、尾盘占比)不是对称噪音,
   理论上**尾盘端点更可能携带知情/机构交易的浓度信息**,这支持 `analysis.md` §4.2 第 3 条里"把开盘/收盘分开算"
   的消融设计(`day_centroid(in_slice(...))` 的阶梯),但这篇文献本身是机制理论,**没有给出任何可直接抄的选股
   构造**,也没有报告方向(涨/跌)。
   出处:*A Theory of Intraday Patterns: Volume and Price Variability*,Anat R. Admati, Paul Pfleiderer,
   1988(Review of Financial Studies, Vol 1, No 1),来源:Stanford GSB working paper 页
   (https://www.gsb.stanford.edu/faculty-research/working-papers/theory-intraday-trading-patterns-volume-price-variability),
   `verified: true`。

2. **收盘集合竞价的成交占比在实务/交易所文献里被当成一个独立核算的量,且被指数调仓流严重污染。**
   行业研究(非学术论文,划入"研究报告"类)报告 S&P500 个股收盘集合竞价占全天成交的比例常年约
   4%→10%(近 8 年),而指数大调仓日(quadruple witching)能到约 26%。HKEX 的一份 Phase 2 介绍材料给出
   类似结论:机构权益流在正常日约 10% 走集合竞价,调仓日约 30%。
   翻译成算子语言:**`day_centroid(Volume)` 的高值在调仓日/做市商到期日这类特殊日子里,很大一部分是指数流
   的"事件"贡献,不是个股自身的"特征"贡献**——这正好支持 `analysis.md` §4.3 第 1 类(把水平变成偏离)和
   第 2 类(按板块/制度分桶)外围,也提示还可以加一类本轮没写的外围:**剔除/标记已知的指数调仓窗口**。
   出处(两条,均为交易所/行业材料,不是同行评审论文,可信度低于 1,但确有其文):
   - *CAS Phase 2*(港交所收盘竞价阶段 2 介绍材料),Hong Kong Exchanges and Clearing,日期不详(材料本身未标年月,
     只能确认是 2023-08-08 前已可公开访问的旧版材料,但首版日期查不到,**按规则"拿不准日期不用"处理,下面不计入
     可引用清单,仅作背景**),来源:HKEX 官网 PDF(https://www.hkex.com.hk/eng/market/sec_tradinfra/vcm_cas/Documents/CAS%20Phase%202%20ppt%20vFinal.pdf),
     `verified: true`(看到了材料内容)但**日期不可用,不建议 PI 直接引用其具体数字**。
   - 行业博客引用的"4%→10%""26%"等具体数字来自二级转述(交易博客),**原始出处搜不到**,`verified: false`
     (我没有看到一级来源,只看到转述)。**不建议把这些百分数写进 missions.yaml,只用其方向性结论。**

3. **"用分钟数据捕捉知情交易时点"这条思路,国内文献已经做成过因子,但口径和我们不同、方向是负的。**
   一篇基于 1999–2019 年中国 A 股分钟数据的研究,构造逐分钟的"聪明钱"侵略性度量(用分钟收益与分钟成交量的
   组合识别"聪明时刻"),再把高聪明度时刻的 VWAP 与全天 VWAP 的比值当因子值,发现**该度量与未来收益是截面负相关**,
   且**原始版本噪音大,需要再加一层基于收益离散度的二次筛选(或聚类)才稳定**(文中最优版本——模糊 C 均值聚类——
   年化 Sharpe 1.169,是加了筛选之后的版本,不是原始水平值的表现)。
   翻译成算子语言:**"成交发生在什么时候"这类日内时点度量,文献里的教训是裸的时点统计量本身信噪比不够,
   通常需要和一个收益/量的二次确认信号联立**才能稳定——这与 `analysis.md` §4.3 第 3 类
   (`mul(day_centroid(Volume), day_signed_ratio(Ret, Amt))`,给无方向的重心补上方向)是同一个思路的独立印证,
   而且方向上**这篇文献报的是负相关**,提示 PI 在写 `missions.yaml` 时不要预设 `day_centroid(Volume)` 的方向,
   留给 train 段自己选(规则本来就是方向只在 train 上选,这点与新尺子的规则一致,不是新增约束)。
   出处:*Smart money in China's A-share market: Evidence from big data*,作者**搜不到**(RePEc/IDEAS 列表页
   未显示作者字段,ScienceDirect 原文需订阅,没能确认作者名单),2022,Research in International Business and
   Finance, Vol. 61,DOI 10.1016/j.ribaf.2022.101663,来源:IDEAS/RePEc 列表页
   (https://ideas.repec.org/a/eee/riibaf/v61y2022ics0275531922000514.html)+ 摘要转述页
   (https://sindex.sdl.edu.sa/esploro/outputs/journalArticle/G12-Keywords-Chinas-A-share-Smart-money/9914792208331,
   该链接证书校验失败,未能直接打开,内容来自 WebSearch 摘要,未逐字核对全文),`verified: true`(标题/期刊/年份/DOI
   在搜索结果中确认看到),**作者姓名搜不到,方向(负相关)和筛选细节来自搜索摘要转述、未读到原文全文,置信度打折**。

**搜不到的部分(如实列出,不编造):**
- 直接构造"日内成交量重心/时点"作为**截面选股特征**、并报告"尾盘成交多→未来涨/跌"方向的学术论文——**没有找到**。
  Admati-Pfleiderer 是机制理论,聪明钱论文是不同的构造(逐分钟侵略性分类而非全天单一重心统计量),两者都不能
  替代一个"确实有人做过 `day_centroid` 这个构造并报告了方向"的直接证据。**这件事本轮搜不到,建议 PI 把它当
  "无直接先例、机制自洽"处理,而不是当"文献已验证"处理。**
- 开盘/收盘集合竞价的成交在构造这类特征时是否被**专门剔除**——搜不到专门针对"日内时点选股因子"给出这个
  选择的论文。能找到的只是市场微观结构研究习惯上把集合竞价成交单独核算(上面第 2 条),但那是**描述统计**上的
  习惯,不是"构造因子时该不该剔除"的实证结论。

---

## 题目 2——对准 §4.3 第 1 类外围:水平值 vs 相对自身历史的偏离

**找到的处理方式:**

1. **"相对自身历史的量"这条路径在成交量文献里是经典做法,且早于"时点"类特征。**
   Gervais, Kaniel, Mingelgrin (2001) 把"异常成交量"定义为**相对个股自身近期交易历史的量**(原文称
   "unusually high/low trading volume",用的是**相对自身历史**,不是截面原始水平),发现异常放量/缩量后
   未来一个月有正/负收益的"高量溢价"。翻译成算子语言:这正是 `cross_zscore(X, N)` / `sub(X, cross_mean(X,N))`
   这条路径在成交量上最早、引用最多的先例——**用偏离而不是水平**是主流做法,这支持 `analysis.md` §4.3 第 1 类
   外围的选择方向。
   **但窗口长度我没能从一级来源确认**:我抓取论文页面与一份工作论文 PDF 均未能提取出原文里窗口的具体天数
   (PDF 是压缩流,没能解出文本);只在一篇**转述该文方法的后续复制研究**里看到"近 50 个交易日里是否排进
   最高/最低 5 天"的操作化定义,但那是复制研究自己的操作化,不能确认等于原文窗口,**不作为可靠窗口数字引用**。
   出处:*The High-Volume Return Premium*,Simon Gervais, Ron Kaniel, Dan Mingelgrin,2001-?(月份搜不到,
   只确认年份),Journal of Finance, Vol. 56, pp. 877–919,来源:Duke 个人主页引用页
   (https://sites.duke.edu/sgervais/?p=64),`verified: true`(标题/作者/期刊/卷/页码在页面上确认看到);
   **窗口长度 verified: false**(没有在一级来源里确认,只看到二级复制研究的转述)。

2. **稳健标准化(中位数/MAD)在业界被当成处理截面退化值的标准做法,但我没搜到学术论文系统比较它和普通
   z-score 在因子构造里的样本外差别。** 能找到的是统计/量化实务文档:MAD 标准化默认用中位数定中心、MAD 定尺度,
   对哑变量这类"稳健尺度几乎为零"的情形会退回均值/标准差;按日截面先 winsorize 再标准化是常见实务流程。
   翻译成算子语言:这支持把 `cross_madz` 作为 `cross_zscore` 的稳健版本平行测试(`analysis.md` §4.3 已经这样写),
   但**"MAD 版本是否在样本外系统性更好"这件事,学术文献层面搜不到**,只有工程实务的"建议这样做"而没有对照实验。
   出处:R 包 `winsorize`(`robStandardize` 函数)文档,作者/机构不详(R 包文档,非论文),日期搜不到,来源:
   eddelbuettel.r-universe.dev 包手册(https://eddelbuettel.r-universe.dev/winsorize/doc/manual.html),
   `verified: true`(看到了文档内容),但**这不是论文/工作论文/研究报告,只作为处理惯例的佐证,不作为"文献已证实"
   的依据**。

**搜不到的部分:**
- "系统比较水平值 vs 滚动 z 分数两种口径在日内微观结构类特征上的样本外差别"的论文——**没有找到**。
  Gervais-Kaniel-Mingelgrin 确立了"用偏离"这条路径在成交量上的先例,但那是单一做法的实证,不是两种做法的对照。
- 稳健标准化(MAD)窗口长度的系统性选择依据——搜不到。

---

## 题目 3——对准 N-a / N-b:上下午(或隔夜/日内)不对称

**找到的处理方式:**

1. **"把全天收益拆成两段,看 alpha 分别藏在哪一段"是一条有明确方法论的主线,但原始论文是隔夜/日内拆分,
   不是逐日的上午/下午拆分。** Lou, Polk, Skouras (2019) 把每个 close-to-close 收益拆成隔夜段和日内段,对 14 个
   常见特征(动量、反转等)逐段算收益,发现**几乎每个策略的 alpha 完全集中在某一段、另一段方向相反或为零**,
   且**机构倾向于日内交易、且交易方向与该特征相反**;效应在大盘股/高价股更强。
   翻译成算子语言:这给了 N-a/N-b 一个**必须做的稳健性检验**,而不只是正面证据——
   在给 `sub(day_mean(in_slice(Ret,121,240)), day_mean(in_slice(Ret,1,120)))` 这类"下午减上午"特征打分之前,
   应该先确认它不是在**把某个已知特征(反转、流动性)的已知 alpha,按「哪半天贡献」重新切了一刀**,
   否则它测到的可能是旧东西换了口径,而不是新信息;这与新尺子对 5 个控制的残差化是同一类问题,但新尺子只在
   "全天"颗粒度上控制,不保证控制了"半天颗粒度"的已知效应。
   出处:*A Tug of War: Overnight versus Intraday Expected Returns*,Dong Lou, Christopher Polk, Spyros Skouras,
   2019(Journal of Financial Economics, Vol. 134, No. 1, pp. 192–213;最早以 2014 年工作论文形式流传),
   来源:作者个人页 PDF(https://personal.lse.ac.uk/polk/research/TugOfWar.pdf)+ LSE Research Online 记录
   (https://researchonline.lse.ac.uk/id/eprint/87481),`verified: true`(标题/作者/期刊/卷/页码/2014 工作论文
   首版信息均在搜索结果中确认看到)。

2. **日内同向延续(今天上午 → 今天下午)是另一条独立但相关的主线,机制解释是"晚到的知情交易+尾盘被动再平衡"。**
   Gao, Han, Li, Zhou (2018) 发现标普 500 ETF **开盘后第一个半小时的收益,能预测当天最后半小时的收益**
   (同向延续,而不是反向不对称),1993–2013 年样本;效应在高波动、高成交量日更强,作者把机制归因于**日内交易者
   + 晚到知情交易 + 尾盘不频繁再平衡**;后续跨市场研究(Li, Sakkas, Urquhart)在 16 个市场里的 12 个也找到
   显著的"首段预测末段"关系。
   翻译成算子语言:这篇**不直接支持"上午减下午"的不对称构造**,反而说明"上午"和"下午"的收益在很多市场是
   **正相关的延续关系**,而不是此消彼长的不对称关系——如果 N-a 的"下午减上午"因子有效,机制解释更可能要靠
   Lou-Polk-Skouras 那条"谁在哪段交易"的路线,而不能直接套用 Gao-Han-Li-Zhou 的"延续"机制,**这两条文献的
   机制方向是不一样的,PI 写 missions.yaml 时不要把它们混成同一个故事**。
   出处:*Market Intraday Momentum*,Lei Gao, Yufeng Han, Sophia Zhengzi Li, Guofu Zhou,2018
   (Journal of Financial Economics, Vol. 129, No. 2, pp. 394–414),来源:AlphaArchitect 摘要页
   (https://alphaarchitect.com/2014/08/attention-prop-traders-the-first-half-hour-of-trading-predicts-the-last-half-hour/)
   + 学术转载页(https://academicnewsletter.sufe.edu.cn/info/356150),`verified: true`(标题/作者/期刊/年份在
   多个搜索结果中反复确认一致)。

**搜不到的部分(需要特别提醒 PI,避免误用关键词里的"APM"):**
- 题目给的关键词里有"APM factor asymmetric price momentum",**我搜不到一篇真正叫这个名字、且构造是
  "上午收益 vs 下午收益"的论文或研报**(无论中文券商研报还是英文学术论文)。能搜到的"不对称"文献
  (Liu & Wan, 2022, *North American Journal of Economics and Finance*, Vol. 60,
  "Asymmetric positive feedback trading and stock pricing in China";
  Wan & Yang, 2017, *International Review of Finance*, "买涨比卖跌更强"的中国证据)说的是**对"涨的股"和"跌的股"
  反应力度不对称**(赢家/输家不对称),**不是**"一天里上午和下午"的时点不对称。这是两件不同的事,
  **不要把 Liu & Wan / Wan & Yang 当成 N-a/N-b 的文献支撑**,它们对准的是另一个轴。`verified: true`
  (这两篇确实存在、确实是这个内容,我看到了),但**它们对 N-a/N-b 不构成支持证据,只用于避免 PI 误引**。
- 国内券商研报里专门构造"上下午资金流/收益不对称"的"APM 因子"——搜不到任何可核实的一级来源
  (标题、机构、日期均未找到可验证的页面),**不写入,也不建议 PI 在 missions.yaml 里援引"APM 因子"这个名字**,
  因为它搜不到可验证出处。

---

## 题目 4——对准 §1.3 的代理风险:板块/涨跌停/机构持仓代理

**找到的处理方式:**

1. **涨跌停制度改变会实测改变日内交易动态,且下轨冲击比上轨更严重、短期效应比长期更强。**
   Bao Qi (2023) 用创业板 2020-08-24 日涨跌幅由 10% 放宽到 20% 这次制度变更做准自然实验(前后各取 6 个月),
   发现价格发现延迟、波动溢出、交易干扰等负面效应确实存在,且**触及跌停时更严重**,短期效应大于长期效应;
   同一批文献里另一些研究(放宽后流动性与波动同步上升、知情交易概率上升)方向基本一致。
   翻译成算子语言:这直接证实 `analysis.md` §1.3 的判断——**`BoardCode`/`LimitWidth` 不是静态标签,
   是会随制度变更日(2020-08-24 这类)**产生**结构性跳变的离散状态**,`cs_bucket_demean` 这类按十分位分桶
   的处理只能扣掉"创业板 vs 其他板"这个静态差异,**扣不掉"创业板制度变更前后"这个时间维度的差异**——
   而本研究 train/valid 窗口(2018-01-02~2023-08-07)**正好跨过这次创业板改革**,这是 PI 和下游在解读
   `cs_bucket_rank(day_centroid(Volume), LimitWidth)` 这类外围时应当留意的一个结构性断点,不是本轮候选
   立刻要处理的问题,但值得记进笔记。
   出处:*Effectiveness of price limits: Evidence from China's ChiNext market*,Bao Qi,2023-06
   (PLoS ONE, Vol. 18, No. 6, pp. 1–14,DOI 10.1371/journal.pone.0287548),来源:RePEc/IDEAS 列表页
   (https://ideas.repec.org/a/plo/pone00/0287548.html),`verified: true`(标题/作者/期刊/卷期/页码/DOI/
   2023-06 这个发布月份均在搜索结果中确认看到,早于规则的 2023-08-08 截止线)。

2. **指数调仓日的机构流确实集中在收盘集合竞价,但这条证据来自交易所/行业材料而非同行评审论文,数字不可靠。**
   见题目 1 第 2 条:HKEX 材料与行业转述都指向"调仓日收盘集合竞价占比远高于平常日",支持"收盘占比类因子
   需要防调仓日污染"这个方向性判断,**但具体百分数搜不到可靠一级来源,不建议写入 missions.yaml 的具体数字**。

**搜不到的部分:**
- 专门针对"日内成交时点类指标"、用**分板块回归**或**剔除指数调仓日**的方式把板块/机构代理成分剥掉的
  **学术论文**——没有找到。Bao Qi (2023) 证明了板块制度确实影响日内动态,但没有给出"怎么把这个代理成分
  从一个选股因子里剥掉"的方法;`analysis.md` §4.3 第 2 类(`cs_bucket_demean` 按 `BoardCode`)是基于机制
  推理的设计,**不是文献里现成抄来的方案,这件事本轮搜不到直接先例**。
- 科创板(STAR Market)专门针对竞价规则对日内成交时点分布影响的研究——搜不到(搜到的全部是创业板 ChiNext
  的研究,没有科创板的对应研究)。

---

## 参考文献总表(按首次出现顺序,含未采用的"搜不到"条目不重复列出)

1. Admati, A. R., & Pfleiderer, P. (1988). *A Theory of Intraday Patterns: Volume and Price Variability*.
   Review of Financial Studies, 1(1). 来源:https://www.gsb.stanford.edu/faculty-research/working-papers/theory-intraday-trading-patterns-volume-price-variability
   `verified: true`
2. 作者不详(RePEc 列表页未显示). (2022). *Smart money in China's A-share market: Evidence from big data*.
   Research in International Business and Finance, 61. DOI 10.1016/j.ribaf.2022.101663.
   来源:https://ideas.repec.org/a/eee/riibaf/v61y2022ics0275531922000514.html
   `verified: true`(标题/期刊/年/DOI);作者姓名 `verified: false`(搜不到)
3. Gervais, S., Kaniel, R., & Mingelgrin, D. (2001). *The High-Volume Return Premium*.
   Journal of Finance, 56, 877–919. 来源:https://sites.duke.edu/sgervais/?p=64
   `verified: true`(主体信息);窗口长度细节 `verified: false`
4. Lou, D., Polk, C., & Skouras, S. (2019). *A Tug of War: Overnight versus Intraday Expected Returns*.
   Journal of Financial Economics, 134(1), 192–213(2014 年工作论文首版)。
   来源:https://personal.lse.ac.uk/polk/research/TugOfWar.pdf ; https://researchonline.lse.ac.uk/id/eprint/87481
   `verified: true`
5. Gao, L., Han, Y., Li, S. Z., & Zhou, G. (2018). *Market Intraday Momentum*.
   Journal of Financial Economics, 129(2), 394–414.
   来源:https://alphaarchitect.com/2014/08/attention-prop-traders-the-first-half-hour-of-trading-predicts-the-last-half-hour/
   `verified: true`
6. Liu, X., & Wan, D. (2022). *Asymmetric positive feedback trading and stock pricing in China*.
   North American Journal of Economics and Finance, 60.
   来源:https://ideas.repec.org/a/eee/ecofin/v60y2022ics1062940822000183.html
   `verified: true`(存在且内容如上描述;**对 N-a/N-b 不构成支持,仅为避免误用列出**)
7. Wan, D., & Yang, X. (2017). 相关"买涨比卖跌更强"的不对称证据(买涨比卖跌更强).
   International Review of Finance, 17(4), 493–523.
   来源:搜索结果转述,未逐字核对全文细节
   `verified: true`(存在且方向如上);**同样不构成 N-a/N-b 的支持证据**
8. Bao Qi. (2023-06). *Effectiveness of price limits: Evidence from China's ChiNext market*.
   PLoS ONE, 18(6), 1–14. DOI 10.1371/journal.pone.0287548.
   来源:https://ideas.repec.org/a/plo/pone00/0287548.html
   `verified: true`
9. （背景,不建议引用具体数字）HKEX. *CAS Phase 2*(港交所收盘竞价阶段 2 介绍材料). 日期搜不到.
   来源:https://www.hkex.com.hk/eng/market/sec_tradinfra/vcm_cas/Documents/CAS%20Phase%202%20ppt%20vFinal.pdf
   `verified: true`(看到材料内容);日期 `verified: false`
10. （处理惯例佐证,非论文)`robStandardize`(R 包 `winsorize`文档). 作者/日期搜不到.
    来源:https://eddelbuettel.r-universe.dev/winsorize/doc/manual.html
    `verified: true`(看到文档内容);不计入"论文/工作论文/研究报告"口径

---

## 给下游的一句话摘要

4 个题目里,题目 1(核心本身的先例)和题目 3 的"APM 因子"是**搜不到直接先例**的——`day_centroid(Volume)`
作为截面选股特征、以及"上下午不对称"这个具体名字的构造,文献里没有能直接对上的东西,只有机制相关的旁证
(Admati-Pfleiderer 的 U 形理论、Lou-Polk-Skouras 的隔夜/日内拆分、Gao-Han-Li-Zhou 的日内延续)。
题目 2(水平 vs 偏离)和题目 4(板块/涨跌停代理)有更实的锚点——Gervais-Kaniel-Mingelgrin 坐实了"用偏离
不用水平"这条路径在成交量上的先例,Bao Qi (2023) 坐实了涨跌停制度确实会改变日内动态、且 train/valid 窗口
正好跨过创业板那次改革。**没有一条处理方式是凭空编的;凡是没找到一级来源的,都在对应小节里写了"搜不到"。**
