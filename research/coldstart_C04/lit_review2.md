# C04 第二轮文献调研:让 Partura 的「假设」在样本外胜过 GP

> 检索日期 2026-10-28。来源是 arXiv、SSRN/NBER、OpenReview、期刊页和会议页。第一轮(`research/coldstart_C02/lit_review.md`)已经覆盖的论文(AlphaAgent、R&D-Agent(Q)、AlphaSchema、Alpha Jungle、AlphaGen/AlphaForge 等),这里只引用结论,不再复述。
> 本轮新核实 49 篇。其中 9 篇读到了方法或结果部分:LaSR、LLM-SR、AlphaEvolve、Tan–Wu–Zhang、Liu–Stambaugh–Yuan、McLean–Pontiff、Huang–Fan、Liao–Liu–Wang、Fan–Hu–Jiang。其余只读了摘要或数据库摘要页。FunSearch、White、Hansen、Romano–Wolf 只通过二手页面确认了出处;Chen–Kelly–Xiu 只看到讲座摘要,正文**未核实**。
> 文中数字都是原文自报,口径各不相同,不能横向比较。

---

## 一、一页摘要

**三个判断**

1. **文献里没有我们要的那种对照。** 本轮专门找过"LLM 先验 vs 盲搜"的因子挖掘对照,要求同预算、多种子、滚动样本外,一篇也没找到。最接近的是金融学里的反面证据:[Chen–Lopez-Lira–Zimmermann](https://arxiv.org/abs/2212.10317) 从 2.9 万个会计比率里挑出 t>2 的,与已发表的预测变量相比,样本期之后两者都只保留约 50%;带理论解释的那些并不更好。也就是说,「有机制故事」本身不带来样本外溢价,这与 C01–C03 一致。
2. **程序合成里,LLM 是在循环里起作用的。** FunSearch、AlphaEvolve、LaSR 都把 LLM 当作循环内的提议分布,而「只生成、不进化」的消融一律明显更差。这些系统都不要求搜索器"遵守"LLM 的意图:LLM 的贡献只通过一条路进入结果,就是它提出的候选被评估器选中。
3. **中性化后 A 股价量异象大多消失,这是常态。** C03 的 64 个变体全部不过线,在预期之内(见 2.2)。Partura 要赢,得给 GP **它没有的东西**,而不是在同一个空间里再给一套先验。

**C04 的三个候选改动(按把握从高到低)**

| # | 改动(改哪一层) | 可证伪假设 | 同预算对照(16 对种子 701–716) | 代价 / 预期收益 |
|---|---|---|---|---|
| 1 | **扩展信息集**:把交易所公开披露做成事件字段(数据层 + 研究层,见 2.5) | B 的配对主指标 > A;并且 B > C,即增益不完全来自数据 | A:GP,只用价量;C:GP,价量 + 事件字段;B:Partura 设计假设和门控结构,价量 + 事件字段。三臂的 GP 评估预算相同 | 高 / 中 |
| 2 | **LLM 在环变异 + 概念库**(LaSR 式),取代"一次性设计初代"(搜索器层,见 2.3) | B 的配对主指标 > A,且 B 最终 heads 里含 LLM 引入子树的比例 ≥30%;否则判为"被绕开" | A:GP;B:每代约 3% 的子代由 LLM 生成;B0:同样比例,但不用概念库。LLM 生成的候选计入同一评估预算 | 中 / 中低 |
| 3 | **只提多头腿机制 + 训练段内 4 折滚动预筛 + 族级预算**(W1 层) | B′ 的假设样本内过线率从 C03 的 0/64 升到 ≥10%,而且配对主指标 ≥ A | A:GP;B:C03 版 Partura;B′:改动后的 Partura | 低 / 低到中 |

- **证伪条件(通用)**:配对单侧检验 p > 0.1;或者样本内领先,但测试段对样本内的保留率低于 A(C02 的形态)。
- **共同协议**:
  - **主指标**:每个种子把全部 heads 等权融合,算残差书在测试段的净夏普;没有 head 的种子记 0。用连续量,不用计数。
  - **检验**:16 对种子做 Wilcoxon 符号秩检验(单侧,α = 0.05),80% 功效下可检出的效应约为 d ≈ 0.62。
  - **次指标**:先聚族再计"有效"数(Holm 校正);前推段同号率;"血统占比"。
  - **共用对照**:三个改动可以共用 A 臂,拼成一个约 5 臂 × 16 种子的 C04。只做一个的话,做改动 1。

---

## 二、分节

### 2.1 假设怎样才带来样本外增益

| 论文 | 发现 | 证据强度 |
|---|---|---|
| [Chen–Lopez-Lira–Zimmermann](https://arxiv.org/abs/2212.10317) | 挖掘出的与同行评审的预测变量,样本期后都保留约 50%;理论标签不加分 | 强(美股,长样本) |
| [Novy-Marx & Velikov,NBER w33363](https://www.nber.org/papers/w33363) | 从 3 万多个挖出的信号出发,让 LLM 给每个通过者批量写带"理论动机"的论文,即把 HARKing(先看结果再编假设)工业化 | 示范性 |
| [Huang & Fan,2603.14288](https://arxiv.org/abs/2603.14288) | agentic 闭环,门槛 \|t\|>3;美股只切一次,主表是毛收益,**没有**同预算的随机或非 LLM 对照 | 弱,代表现有文献的典型水平 |
| [Zhang 等,PPSN'24](https://arxiv.org/abs/2407.10873) | 4 种方法 × 4 个问题 × 9 个 LLM × 5 次运行;指出早先的 LLM 程序搜索多与弱基线比较,"进化搜索本身"才重要 | 中 |

**前视偏差**:
- [Lopez-Lira–Tang–Zhu](https://arxiv.org/abs/2504.14765):LLM 能回忆训练截止日前的宏观数值,"不许用未来信息"的指令无效。
- [Gao–Jiang–Yan](https://arxiv.org/abs/2512.23847):"回忆倾向"LAP 在截止日前为正、截止后归零,预测力在高 LAP 样本上被放大。
- [Glasserman–Lin](https://arxiv.org/abs/2309.17322):把公司名匿名化后,样本内表现反而更好。
- [He 等](https://arxiv.org/abs/2502.21206):只用当时可得文本训练的模型,在新闻→次日收益这个任务上前视偏差不大。
- [MemGuard-Alpha](https://arxiv.org/abs/2603.26797):用成员推断过滤受污染的信号,组合表现并没有改善。
- [Kong 等](https://arxiv.org/abs/2602.14233):164 篇金融 LLM 论文里,任何一种偏差被讨论的比例都 ≤28%。

我们的测试段(2023-08~2025-12)在所用模型的训练截止之前,具体截止日要按模型版本核对。第一轮 Alpha Jungle 的回忆测试显示,**公式层面**的泄漏不明显;但**选哪个族**、**怎样解读事件和文本**,泄漏可能很大。

**多种子或滚动样本外下站得住的设计**:金融领域本轮没有新证据,仍然只有第一轮的 TreEvo、AlphaMemo 和 AlphaPROBE。

**落地(总领层)**
- **职责**:Partura 从"给 GP 先验"改成"给 GP 新字段和在环提议";W1 的直接检验只用来筛选。
- **门控**:不再用 LLM 判断"假设与因子是否一致"来放行候选。
- **匿名化**:处理带公司名或日期的材料前,代码换成随机 ID,日期换成相对日。
- **前推段确认**:决定性结论再用前推段(2026-01-05 起)确认。
- **代价与收益**:代价低;不直接提高胜率,作用是挡住"测试段上的假胜利"。

### 2.2 中性化与增量目标:还剩多少 alpha

| 市场 | 论文 | 经验量级 |
|---|---|---|
| 美股 | [Hou–Xue–Zhang,RFS 2020](https://ideas.repec.org/a/oup/rfinst/v33y2020i5p2019-2133..html) | 452 个异象,用 NYSE 断点、市值加权后,65% 过不了 t = 1.96;门槛 2.78 时 82% 过不了 |
| 美股 | [Green–Hand–Zhang,RFS 2017](https://ideas.repec.org/a/oup/rfinst/v30y2017i12p4389-4436..html) | 94 个特征联合回归,非微盘股有 12 个独立显著,**2003 年后只剩 2 个** |
| 美股 | [Feng–Giglio–Xiu,JF 2020](https://www.nber.org/papers/w25481) | 用双重选择 LASSO 检验 150 个因子的边际贡献,只有少数显著 |
| 美股 | [McLean–Pontiff,JF 2016](https://doi.org/10.1111/jofi.12365) | 样本外收益低 26%,发表后低 58%;样本内收益越高,衰减越多 |
| 全球(反面) | [Jensen–Kelly–Pedersen,JF 2023](https://www.nber.org/papers/w28432) | 在贝叶斯框架下多数因子可复现,但口径是相对 CAPM,不是风格中性 |
| 美股 | [Blitz–Huij–Martens,JEF 2011](https://www.econbiz.de/Record/residual-momentum-blitz-david/10009194616) | 残差动量的风险调整收益约为总收益动量的 2 倍。中性化掉的若是噪声暴露,夏普会**升** |
| A 股 | [Li–Liu–Liu–Wei,Mgmt Sci 2024](https://doi.org/10.1287/mnsc.2023.4904) | 469 个异象,主板断点、市值加权:83% 价差不显著;CAPM alpha 84%,FF3 alpha 87% |
| A 股 | [Liu–Stambaugh–Yuan,JFE 2019](https://faculty.wharton.upenn.edu/wp-content/uploads/2018/03/Size-and-Value-in-China.pdf)(读的是工作论文版) | 10 个显著异象,CH-3 解释 8 个;剩下的反转和异常换手,被 CH-4 的换手因子解释 |
| A 股 | [Leippold–Wang–Zhou,JFE 2022](https://www.sfi.ch/en/publications/machine-learning-in-the-chinese-stock-market) | 流动性是最重要的预测变量;可预测性集中在小盘股和散户 |
| 两边 | [Stambaugh–Yu–Yuan,JFE 2012](https://www.nber.org/papers/w16898) | 异象利润主要来自**空头腿**;多头腿与情绪无关 |

**经验量级(我们的归纳)**
- 对足够全面的风格集合做中性化后,原本显著的异象只剩约 1/5 到 1/3(美股约 35%,A 股约 17%);剩下的部分,样本外量级大约再减半。
- 我们只交易多头腿,而文献里的机制多半是空头腿现象。这很可能是 C03 全军覆没的一个主因。

**增量奖励的方法(都不依赖 LLM)**:AlphaGen 的边际贡献奖励(第一轮已述);Feng–Giglio–Xiu 的双重选择检验;[Harvey–Liu《Lucky factors》](https://doi.org/10.1016/j.jfineco.2021.04.014),在零假设下做 bootstrap 检验新因子的增量,同时控制多重检验。

**落地(奖励层)**
- **(a) 逐步正交化**:把本次运行已收的 heads 加进控制变量,同族变体不再重复吃预算。
- **(b) 加规模控制**:用交易所公开的股本数据算流通市值。C03 的控制里缺规模。
- **(c) 非线性残差**:保留第一轮建议的十分位非线性残差。
- **代价**:每天的截面 OLS 多几列;股本数据需要 1–2 天。
- **预期**:两组的通过数都会继续下降。这一步保证"赢"不是来自风格,而不是让 Partura 赢。

### 2.3 程序合成里的 LLM + 搜索

| 系统 | 机制 | 证据 |
|---|---|---|
| [FunSearch,Nature 2023](https://doi.org/10.1038/s41586-023-06924-6) | LLM 只改写固定骨架里的一个函数;岛模型;用最好的程序做提示 | LLM 本身就是变异算子,评估器是唯一的裁判 |
| [AlphaEvolve,2506.13131](https://arxiv.org/abs/2506.13131) | 在 EVOLVE-BLOCK 标出的区域内做差分编辑;评估级联;多个指标同时优化;Flash 走量,Pro 偶尔给高质量提议 | 消融中,"不进化"(反复喂初始程序)、去掉上下文、只用小模型等,**每一项都显著变差**(数值只在图里,未核实) |
| [LLM-SR,ICLR'25](https://arxiv.org/abs/2404.18400) | LLM 写方程骨架,参数用 BFGS 拟合(最多 10 个) | 4 个自建问题上,样本外 NMSE 多数远好于 PySR(E. coli:0.0037 对 1.01),但不是每题都好。去掉先验后明显变差;去掉迭代精修,NMSE 从 2e-7 恶化到 1e-1 |
| [LLM-SRBench,ICML'25](https://arxiv.org/abs/2504.10415) | 把 Feynman 方程改写成不常见的形式 | 最好的方法只解出 31.5%,常见基准的成绩有一部分来自记忆 |
| [LaSR,NeurIPS'24](https://arxiv.org/abs/2409.09359) | **最接近"LLM 引导 GP"**:PySR 的每次初始化、变异、交叉,以概率 p 换成 LLM 版本,提示里带上概念库采样的概念;概念由 LLM 从高分和低分方程里抽象出来 | Feynman 精确解出 72 个,PySR 59 个(p = 1%);合成题 R² 0.913 对 0.070;去掉概念库收敛变慢;**没有报告种子数** |
| [EoH](https://arxiv.org/abs/2401.02051)、[ReEvo](https://arxiv.org/abs/2402.01145) | LLM 当变异和交叉算子,同时进化"思路"或"反思" | 声称比 FunSearch 省 LLM 调用 |
| [DreamCoder](https://people.csail.mit.edu/asolar/papers/EllisWNSMHCST21.pdf)、[LILO](https://arxiv.org/abs/2310.19791) | 库学习:把成功程序里反复出现的抽象压缩成新原语并入库 | 新原语进入语法本身,只在有用时才会被选中 |

**"LLM 当变异算子 vs 当生成器"**:AlphaEvolve 的"不进化"、LLM-SR 的"不精修"、PPSN'24 的基准,方向一致:**只生成**是最弱的模式。C02 的 W1 直接检验正属于这一种。

**这些系统怎样处理"意图"**:它们不去强制意图,只看 LLM 提出的东西有没有被选中。C01 那种"禁令被绕开"的问题,在它们的框架里不存在。

**预算怎么分**:LaSR 只让 1% 的操作走 LLM 就够了;AlphaEvolve 用便宜模型走量,强模型少量出手。

**落地(搜索器层 + 执行层)**
- **移民口**:GP 每一代插入 k 个由 Sonnet 或 Haiku 生成的候选,约占子代的 3%。
- **生成条件**:前 20 个精英的表达式、残差分数和换手,加上从概念库采样的 3 条概念。
- **概念库**:每 G 代由 Opus 从精英和被拒原因里抽象一次;经过多代验证的子树编译成宏算子,并入 286 个算子。
- **评估级联**:先在 1/4 的股票池上算残差 IC,过线才跑全量十分位书。
- **代价**:中等。GP 要支持异步插入候选。
- **预期收益**:在平稳目标上证据中等;在金融上未知。

### 2.4 多重检验与过拟合控制

**文献给出的门槛与工具**
- [Harvey–Liu–Zhu,RFS 2016](https://doi.org/10.1093/rfs/hhv059):新因子要过 t > 3.0。
- [Chordia–Goyal–Saretto,RFS 2020](https://ideas.repec.org/a/oup/rfinst/v33y2020i5p2134-2179..html):用 200 多万个随机策略估计门槛,时序约 3.8,截面约 3.4;不校正时约 45% 的拒绝是假的。
- [Harvey–Liu《Backtesting》](https://people.duke.edu/~charvey/Research/Published_Papers/P120_Backtesting.PDF):夏普的折扣是非线性的,边际策略被砍得最多。
- [Deflated Sharpe](https://papers.ssrn.com/abstract=2460551):按试验次数和收益分布的高阶矩折算夏普。
- [PBO/CSCV](https://papers.ssrn.com/abstract=2326253):估计回测过拟合的概率。
- White 的 Reality Check、Hansen 的 SPA、[Romano–Wolf 的 StepM](https://www.econometricsociety.org/publications/econometrica/browse/2005/07/01/stepwise-multiple-testing-formalized-data-snooping):用 bootstrap 判断一组策略里谁真的赢了基准。[`arch` 包](https://arch.readthedocs.io/en/latest/multiple-comparison/multiple-comparison-reference.html)有现成实现。
- 反面:[Allen–Karjalainen,JFE 1999](https://papers.ssrn.com/abstract=6996):遗传算法找到的技术规则,扣费后在样本外没有一致超额。

**我们的门槛算账**(假设 head 之间相互独立)

测试段约 2.4 年,t ≥ 2 等价于年化夏普 ≥ 1.29。零假设下,每个 head 被误判为有效的概率是 2.3%。

| 每组 head 数 N | 期望误报 | 某组 ≥2 个假有效 | 两组都无真信号时,被 C03 规则判"B 有用" |
|---|---|---|---|
| 30 | 0.68 | 15% | 9% |
| 50 | 1.14 | 32% | 15% |
| 80 | 1.82 | 54% | 20% |

- **离散度**:heads 同族时离散度更大(C02 的 7 个来自一个家族),所以上表偏乐观。
- **功效**:真实夏普 0.8 的 head,t ≥ 2 下只有 22% 的概率被判有效,t ≥ 3 下只有 4%。前推段只有 0.68 年,要过 t ≥ 2 需要夏普 ≥ 2.4。

**结论**:t ≥ 2 的门槛误报太多,拿它的计数做判决又功效太低;光收紧门槛解决不了,要换判读对象:
1. **主判读**:用连续量做配对比较,见摘要的共同协议。
2. **计数作次指标**:先按测试段残差收益相关 ≥ 0.5 聚族,再计数;组内用 Holm(N = 50 时约 t ≥ 3.09)或 StepM。
3. **样本内**:两组都报告 DSR 和 PBO,试验次数用候选的聚类数估计。
4. **测试段已不干净**:它在 C01–C03 里被读过多次,设计选择(比如改用中性化奖励)本身受了它的影响。用前推段确认,只要求方向一致。

**落地**:改在判读脚本层;代价低,bootstrap 几分钟。

### 2.5 价量之外、不用买的数据(A 股)

| 信息 | 文献证据 | 多头书的用法 / LLM 的角色 |
|---|---|---|
| 限售解禁 | [Liao–Liu–Wang](https://efmaefm.org/0EFMSYMPOSIUM/2010-China/papers/LLW_splitshare20091030.pdf)(股改时期,482 次):[-120, +20] 日异常收益 −14%,成交放大 140%,机构主导事前价格发现。现代 IPO、定增解禁的证据**未核实** | 日程提前公开,"未来 20 日解禁比例"可用来排雷 / 抽取解禁类型 |
| 大宗交易 | [Fan–Hu–Jiang,PBFJ 2012](https://ideas.repec.org/a/eee/pacfin/v20y2012i3p378-397.html):平均折价约 4%;折价成交带来持续 60 个交易日的负向冲击,溢价成交没有 | 排雷 / 角色很小 |
| 指数调整 | [Wang–Murgulov–Haman,EMR 2015](https://ideas.repec.org/a/eee/ememar/v24y2015icp13-33.html):沪深 300 纳入涨、剔除跌,随后部分反转,幅度小于标普 500 | 可按规则事前预测纳入名单 / 角色小 |
| 业绩预告 | [Huang–Li–Tse–Tucker,JBFA 2018](https://researchonline.lse.ac.uk/id/eprint/87113):强制预告有信息含量;管理层会做盈余管理以避开强制门槛。预告后漂移的 A 股专门证据**未找到** | 多头的正向事件 / 从正文抽取区间、幅度、原因(Haiku 足够) |
| 龙虎榜 | [Zhai–Hou–Li,JBEM 2020](https://doaj.org/article/8d3d1e04e2474b4b8af7e499de2b4c68):负面冲击下,上榜带来的注意力越高,后续收益越低 | 排雷;"机构净买"的正向效果**未核实** |
| 融资融券 | [Chang–Luo–Ren,JBF 2014](https://ideas.repec.org/a/eee/jbfina/v48y2014icp411-424.html):卖空能预测收益,融资交易不能;其他研究结论不一 | 优先级低 |
| 北向持股 | [Zhu 等的工作论文](https://sf.cufe.edu.cn/info/1183/8671.htm):周度持股变化做多空,每周最高 61bp 异常收益。但 [HKEX 2024-04-12 公告](https://www.hkex.com.hk/News/Market-Communications/2024/2404122news?sc_lang=en)把持股数据改为按季度披露 | 测试段只有约一年日度数据,**不适合 C04** |
| 文本→信号 | [Tan–Wu–Zhang](https://abfer.org/media/abfer-events-2024/cmd/Large-Language-Models-and-Return-Prediction-in-China_Lin-Tan.pdf):2800 万篇中文新闻(商业数据),2019–2023 样本外市值加权多空年化 35–67%,CH-4 alpha 显著,约 2 天被吸收,小盘更强。另见 [Lopez-Lira–Tang](https://arxiv.org/abs/2304.07619)、[Chen–Kelly–Xiu](https://nlpecofin.web.ox.ac.uk/node/3041271)(正文**未核实**) | 免费替代是交易所公告全文(巨潮) / 匿名化后只做分类,不做预测 |

**落地(数据层 + 研究层)**
- **第一批字段**:F1 未来 20 日解禁比例;F2 近 20 日大宗折价卖出额 ÷ 流通市值;F3 最近一次业绩预告的方向与幅度(随时间衰减)。
- **点时对齐**:都按"公告之后的下一个交易日可用"对齐,与"次日开盘买入"的标签一致。
- **两种用法**:C 臂把这些字段作为 GP 的终端;B 臂由 Partura 额外设计门控结构,比如在价量信号的前 10% 里剔除 F1 或 F2 偏高的股票。
- **代价**:数据管道约 1–2 周;LLM 解析公告的成本很小。
- **预期收益**:中等。

---

## 三、风险与反面证据:哪些改动只会在样本内赢

1. **样本内加速不等于样本外增益**:C02 的 LLM 初代在样本内 8 个种子赢了 7 个,样本外反过来。LaSR 和 AlphaEvolve 的证据都来自平稳目标,改动 2 最可能的效果是更快爬到样本内高点。McLean–Pontiff 也发现,样本内越强,事后衰减越多。所以必须事先登记"保留率"作为证伪条件。
2. **一致性和故事不是证据**:第一轮 AlphaBench 发现"评判因子"是 LLM 最弱的能力;Novy-Marx–Velikov 表明给任何信号配一套理论几乎零成本。拿 LLM 打分或"一致性"做门控,只会在样本内赢。
3. **前视偏差**:测试段在模型的训练截止之前,Partura 选哪个族、怎样解读文本,都可能来自记忆;改动 1 的文本部分风险最高。只在测试段赢、前推段方向不一致的结果,判为"分不出"。
4. **计数的噪声**:见 2.4。像 C02 的"7 对 2",在 N ≈ 50 时,即使两组都没有真信号,也有约 15% 的概率被规则判为一方胜出;同族时更高。
5. **事件数据本身的风险**:
   - 早期样本(股改解禁、2003–2009 年的大宗交易)不一定代表 2023–2025 年。
   - 事件字段稀疏,放进十分位多头书可能退化。
   - 增益可能被 C 臂全部拿走。那样的话,Partura 的"胜利"其实是数据工程,而不是假设。
6. **预算不对等**:LLM 的推理算力不计入 GP 的评估预算。如果 B 只有在额外 token 下才赢,应报告按 GPU 小时和按美元折算的对比。
7. **中性化的反面**:Jensen–Kelly–Pedersen 和残差动量说明,"中性化后什么都不剩"并不是定律;只是 A 股价量类在 CH-4 下的证据偏悲观。
