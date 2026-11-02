# Q&A 准备清单 · Q&A preparation (bilingual)

覆盖:为什么这样设计、每个部分怎么做、每个实验的结果和原因、统计口径、局限、成本、工程,以及对抗性的追问。
每题:**Q**(英文问法 / 中文)→ **A-EN**(可以直接说的英文答案)→ **A-中**(中文要点)。数字均来自各研究的 `PLAN.md` /
`RESULT.md`、`research/coldstart_C08/final.json`;**加粗**的是建议必须说出的数字。

Coverage: why each design choice, how each part works, every study's result and reason, statistics, limits, cost,
engineering, and adversarial follow-ups. Numbers come from each study's PLAN/RESULT and C08's final.json.

目录 / Contents
- A. 全局与定位 / Framing (A1–A10)
- B. 数据、任务、标签 / Data, task, label (B1–B9)
- C. 搜索器 AlphaCube 与 GP / The searcher (C1–C9)
- D. 尺子与判读 / Yardstick and evaluation (D1–D14)
- E. Partura 的结构与角色 / Agent architecture (E1–E14)
- F. C01–C07 逐个 / Each earlier study (F1–F16)
- G. C08 设计与结果 / C08 in detail (G1–G20)
- H. 统计与有效性 / Statistics and validity (H1–H12)
- I. 成本 / Cost (I1–I5)
- J. 局限与风险 / Limitations (J1–J10)
- K. 工程与可复现 / Engineering (K1–K8)
- L. 下一步与入职后 / Next steps and fit (L1–L8)
- M. 背景:AlphaCube 自身和其他 Partura 研究 / Context (M1–M6)
- N. 尖锐追问 / Hard questions (N1–N14)

---

## A. 全局与定位 / Framing

**A1. Q: In one minute, what is Partura? / 一分钟介绍 Partura。**
- **A-EN:** Partura is an LLM research team that sits around a genetic-programming alpha miner, AlphaCube. The miner searches
  formulas over a minute-level cube of A-share data at zero token cost. Partura reads what the miner found, forms beliefs about
  where the alpha comes from, and turns them into missions that redirect the miner's extra budget. I ran eight pre-registered
  experiments, each comparing Partura against giving the same extra budget to plain GP. The first seven were worse or
  inconclusive; the eighth beat plain GP in 7 of 8 seeds, p = 0.012, on a development set.
- **A-中:** 围绕遗传规划挖掘器 AlphaCube 的 LLM 研究团队。挖掘器零 token 在分钟数据立方体上搜公式;Partura 读它的产出、形成
  「alpha 从哪来」的信念、派任务改变额外预算的去向。八个事先约定的实验都和「同样额外预算给普通 GP」比;前七次更差或分不出,
  第八次 8 胜 7、p = 0.012(开发集)。

**A2. Q: What is the main claim, precisely? / 你的主张具体是什么?**
- **A-EN:** That spending a fixed extra search budget through Partura's missions produced a better out-of-sample library than
  spending it on more plain GP — **median +0.23 Sharpe, 7 of 8 seeds, p = 0.012** — on a test period that earlier designs had
  already read. It is not a claim that Partura beats the base search (P vs M is +0.24, p = 0.098), and not a claim of a
  high-Sharpe factor.
- **A-中:** 同样的额外搜索预算,交给 Partura 比交给普通 GP 得到更好的样本外因子库(中位 +0.23,8 胜 7,p 0.012),测试段此前被
  读过。不是「Partura 胜过基础搜索」(P 对 M 不显著),也不是「找到了高夏普因子」。

**A3. Q: Why does "alpha found" not prove the LLM helped? / 为什么「找到 alpha」不能证明 LLM 有用?**
- **A-EN:** Because a capable searcher with the same data and compute might find the same or better. Attribution needs a
  counterfactual: same engine, same seeds, comparable paid evaluations (nominally equal by design), with and without the agent,
  judged on data the agent never saw. Every study used that design.
- **A-中:** 同样数据和算力的搜索器也可能找到。归因需要反事实:同引擎、同种子、可比的评估次数(按设计名义相等),有无 agent 对比,在 agent 没见过的
  数据上判读。

**A4. Q: What does "search is cheap, belief is expensive" mean operationally? / 「搜索便宜、信念昂贵」落到操作上是什么?**
- **A-EN:** GP evaluates expressions for no tokens, so the LLM should not compete at generating candidates. Tokens are spent
  once per round to decide where search goes: which core to deepen (E), which part to remove (R), which new mechanism to try (N).
  C08's result fits that: the gain is in allocation of extra search, not single high-Sharpe formulas.
- **A-中:** 生成候选交给 GP;token 每轮只花一次,用来决定搜索方向(E/R/N)。C08 的结果正好体现在「额外搜索怎么分配」上。

**A5. Q: Why an LLM at all? Why not just more GP? / 为什么要用 LLM,不直接多跑 GP?**
- **A-EN:** That is exactly the question each study tests. More GP (arm A) is the baseline. In C08, more GP did not improve on
  the base search (A vs M median 0.00) and sometimes hurt the fused book, while Partura's missions did better than A. So the
  answer, so far, is: more GP has diminishing returns in this setup, and judgement about where to spend it helped.
- **A-中:** 这正是每个实验在检验的。C08 里多跑 GP 没有改善(A 对 M 中位 0),有时还拖累组合;Partura 的任务胜过 A。

**A6. Q: What is new here compared with LLM alpha-mining papers? / 和已有的 LLM 挖因子工作比,新在哪?**
- **A-EN:** Three things. The LLM never writes the final formulas — GP does; the LLM decides where GP looks. Every comparison is
  against a matched GP baseline with paired seeds, pre-registered, with a once-read test. And the results include the failures:
  seven designs that did not beat GP, each turned into a design rule.
- **A-中:** LLM 不写最终公式,只决定 GP 往哪找;每个比较都是和匹配的 GP 基线配对、事先约定、测试段只读一次;失败也报告,
  并各自变成设计规则。

**A7. Q: What did you personally do versus the agents? / 哪些是你做的,哪些是 agent 做的?**
- **A-EN:** I designed the research question, the arms, the yardstick, the verdict rules and the isolation rules, and wrote
  or reviewed the code and every PLAN before the runs. The agents play defined roles inside a round — anatomist, librarian, PI,
  auditor, checker — and their outputs are files that code checks. Interpretation of results and the decision of what to change
  next were mine.
- **A-中:** 研究问题、分组、尺子、判定与隔离规则、每份 PLAN 由我设计并在运行前提交;agent 只在一轮里扮演固定角色,产出由代码检查;
  结果解读与下一步设计由我决定。

**A8. Q: What is the single most important lesson? / 最重要的一条教训?**
- **A-EN:** Fix the referee before judging the agent. Under a leaky yardstick, the LLM optimised the leak (C05) and a
  sensible auditor looked wrong (C06). Only after the yardstick was fixed (C07) did a Partura design beat GP (C08).
- **A-中:** 先修好裁判,再评判 agent。尺子漏的时候,LLM 去优化漏洞(C05),合理的审计员看起来是错的(C06);修好尺子之后才赢(C08)。

**A9. Q: Is this an alpha or a research process? / 这是一个 alpha 还是一个研究流程?**
- **A-EN:** A research process. The deliverable is evidence about where an LLM adds value in alpha research, plus a working
  system. The individual heads are modest: P's extra heads have a median test Sharpe of +0.07.
- **A-中:** 研究流程。产出是「LLM 在因子研究里哪里有用」的证据和一套能跑的系统;单个 head 很一般(中位 +0.07)。

**A10. Q: If you had to bet, will C08 confirm on fresh data? / 你押注 C08 在新数据上能确认吗?**
- **A-EN:** I'd give it better than even odds that P stays at or above A, because the mechanism — avoiding bad extra heads —
  is structural rather than tied to one factor. I'd give lower odds to significance at 8 pairs; one seed can flip it. That is
  why the next step is a frozen protocol, more seeds, and a same-head-count random filter control.
- **A-中:** P 不差于 A 的概率过半(机制是「避免坏的额外 head」,较结构性);8 对仍显著的概率较低。所以下一步冻结流程、加种子、
  加同 head 数随机筛选对照。

---

## B. 数据、任务、标签 / Data, task, label

**B1. Q: What data? / 用什么数据?**
- **A-EN:** A-share minute bars: about 5,200 stocks (5,220 in the C05+ view), 241 one-minute bars a day, 8 minute fields
  (open, high, low, close, VWAP, volume, amount, return), stored as a (stock, day, minute) cube from 2018-01-02 to 2026-09-16.
  From C04 on, six daily fields: log float cap, log total cap, log float shares, limit width, board code, listing age.
- **A-中:** A 股分钟 bar,约 5,200 只(C05 起判读视图 5,220),每天 241 根,8 个分钟字段,(股票, 日, 分钟)立方体,2018-01-02 到
  2026-09-16;C04 起加 6 个日频字段。

**B2. Q: What exactly is the target? / 目标具体是什么?**
- **A-EN:** Signal is computed after day t's close. Buy at day t+1's 09:31–09:45 VWAP, sell at day t+2's same window:
  r = P(t+2)/P(t+1) − 1. Stocks sealed at limit-up through the whole entry window are excluded, because you could not buy them.
- **A-中:** t 日收盘后出信号,t+1 日 09:31–09:45 VWAP 买入,t+2 日同窗口卖出;入场窗口全程涨停封死的剔除(买不进)。

**B3. Q: Why first-15-minute VWAP rather than close-to-close? / 为什么用开盘 15 分钟 VWAP 而不是收盘价?**
- **A-EN:** It is executable: you cannot trade at the close you used to compute the signal. A 15-minute VWAP is a realistic
  fill for a mid-size order and avoids the opening auction print.
- **A-中:** 可执行:不能在用来算信号的收盘价成交;15 分钟 VWAP 对中等单量是现实的成交价,也避开开盘集合竞价那一笔。

**B4. Q: Splits? / 样本切分?**
- **A-EN:** Train 2018-01-02 to 2021-12-31; valid 2022-01-04 to 2023-08-07; test 2023-08-08 to 2025-12-31, read once per
  study; forward 2026-01-01 to 2026-09-16, report only. Agents and search only ever see train and valid.
- **A-中:** train 2018–2021;valid 2022-01 到 2023-08-07;测试段 2023-08-08 到 2025-12-31,每个研究只读一次;前推段 2026 只报;
  agent 和搜索只见 train / valid。

**B5. Q: Why is forward only "report"? / 为什么前推段只报不判?**
- **A-EN:** It is 0.67 years — too short to carry a verdict — and it was read in earlier work. It is a consistency check.
- **A-中:** 只有 0.67 年,太短;而且之前被读过。只做一致性检查。

**B6. Q: Survivorship? / 幸存者偏差?**
- **A-EN:** The store has no delisted names. That biases absolute returns upward for both arms equally, so the paired comparison
  is less affected, but absolute Sharpes should be read with that in mind.
- **A-中:** 库里没有退市股;两组同样受影响,配对比较受影响较小,但绝对夏普要打折看。

**B7. Q: Why A-shares, long-only? / 为什么 A 股、只做多?**
- **A-EN:** Shorting individual A-shares is restricted and expensive, so a long-only top-decile book is the realistic product.
  From C04 on, the reward and judgement are long-only.
- **A-中:** A 股个股做空受限且贵;C04 起奖励和判读都只看多头腿。

**B8. Q: How do you handle limit-up/limit-down and T+1? / 涨跌停与 T+1 怎么处理?**
- **A-EN:** The label excludes names you could not buy (sealed limit-up through the entry window). Holding is one day from t+1
  to t+2, consistent with T+1. Limit width is also a daily field, because it differs by board (10% main board, 20% ChiNext and STAR, 30% Beijing, 5% ST).
- **A-中:** 标签剔除买不进的;持有 t+1 到 t+2 一天,符合 T+1;涨跌幅限制按板块不同,作为日频字段。

**B9. Q: Costs? / 交易成本?**
- **A-EN:** 15 bp per side on every book, in rewards and in judgement.
- **A-中:** 每边 15 bp,奖励与判读都扣。

---

## C. 搜索器 AlphaCube 与 GP / The searcher

**C1. Q: What is AlphaCube? / AlphaCube 是什么?**
- **A-EN:** My factor engine: a typed expression language over a three-dimensional tensor (stock, day, minute), with operators
  on three faces — within-day (minute) operators, daily cross-sectional and time-series operators, and per-minute cross-section
  operators — plus GP and four RL miners. An expression like `cs_rank(ts_mean(day_std(Ret), 5))` reduces minutes to a daily
  value, smooths it, and ranks across stocks.
- **A-中:** 我的因子引擎:在 (股票, 日, 分钟) 三维张量上的类型化表达式语言,算子分三张面,带 GP 和 4 个 RL 挖掘器。

**C2. Q: Why GP rather than RL? / 为什么用 GP 不用 RL?**
- **A-EN:** In my earlier AlphaCube work GP was more robust out of sample; for example in a CSI 300-only mining study GP's
  clean out-of-sample result was positive and RL's was negative. GP is also easier to steer through seeds and filters, which is
  what Partura needs.
- **A-中:** 之前的工作里 GP 样本外更稳(如沪深 300 专门挖掘:GP 为正、RL 为负);GP 也更容易通过种子和过滤器引导。

**C3. Q: What is the main search M? / 主搜索 M 是什么?**
- **A-EN:** A plain GP run in 4 batches per seed (budget 192, population 48 per batch in C07/C08). Each batch bans what earlier
  batches found: rank correlation ≥ 0.7 with an existing head, or the same skeleton. No agent touches it; both arms share it.
- **A-中:** 每个种子 4 批的普通 GP(C07/C08 每批预算 192、种群 48),每批禁掉之前批次的 head(秩相关 ≥ 0.7 或骨架相同);
  不受 agent 影响,两组共用。

**C4. Q: What is a "head"? / 什么是 head?**
- **A-EN:** A discovery: an expression whose score — the worse of train and valid residual long-only net Sharpe — is at least
  0.5, and whose correlation with the known family is below 0.5.
- **A-中:** 发现:score(train 与 valid 残差纯多头净夏普中较差的)≥ 0.5,且与已知族相关 < 0.5。

**C5. Q: What does "same skeleton" mean? / 「骨架相同」指什么?**
- **A-EN:** The operator tree with fields, constants and windows stripped. Two expressions that differ only in a window length
  or which volume field they use count as the same structure, so GP cannot farm near-duplicates.
- **A-中:** 去掉字段、常数、窗口后的算子树;只差窗口或字段的算同一结构,防止刷近似重复。

**C6. Q: How do missions enter GP? / 任务怎么进入 GP?**
- **A-EN:** Three handles only: seeds in the initial population, direct evaluation of R variants without a GP run, and the
  library ban that decides what can be accepted. GP itself computes every expression and every score.
- **A-中:** 只有三个接口:初始种群的种子、R 变体的直接评估、决定能否接受的库禁令;所有计算和打分都由 GP 完成。

**C7. Q: What is arm A exactly? / A 组具体是什么?**
- **A-EN:** Two plain GP runs per round for three rounds per seed (population 32, budget 128 each), seeded randomly, with the
  same library ban. In C08 A totals 4,438 scored evaluations over 8 seeds.
- **A-中:** 每个种子 3 轮,每轮 2 次普通 GP(种群 32、预算 128),同样的库禁令;C08 中 8 个种子合计 4,438 次评估。

**C8. Q: Why is A not just one bigger GP run? / 为什么 A 不是一次更大的 GP?**
- **A-EN:** To mirror P's structure: P gets two GP slots per round for three rounds. Matching the run structure isolates the
  question "who chooses what these runs search", rather than "one long run vs. several short ones".
- **A-中:** 与 P 的结构对齐(每轮 2 个任务位 × 3 轮),只比较「谁决定这些运行搜什么」。

**C9. Q: How fast is evaluation? / 评估有多快?**
- **A-EN:** On one RTX 5090, a 96-evaluation GP slot on the full 5,220-stock cube runs in minutes; the full C08 read rebuilt
  123 distinct expressions in about 3.5 minutes on GPU. Panels are cached by expression.
- **A-中:** 一张 5090 上一个 96 次评估的任务位几分钟;C08 判读重算 123 个表达式约 3.5 分钟;面板按表达式缓存。

---

## D. 尺子与判读 / Yardstick and evaluation

**D1. Q: Walk me through the yardstick. / 讲一下尺子。**
- **A-EN:** For each expression: each day, convert values to cross-sectional ranks; smooth with an EMA of half-life 0, 5 or 20
  days; regress out five controls — liquidity, volatility, 20-day reversal, the known family `cross_mean(day_std(Amt), 30)`,
  and log float cap — together with their squares and cubes, 15 columns plus a constant, every day; build a top-decile
  long-only book on the residual, net of 15 bp; score is the worse of train and valid net Sharpe. Direction and half-life are
  chosen on train.
- **A-中:** 逐日截面转排名 → 半衰期 0/5/20 的 EMA → 对 5 个控制(流动性、波动、20 日反转、已知族、流通市值)及其平方、三次方
  共 15 列加常数逐日取残差 → 残差十分位纯多头、扣 15 bp → score = train 与 valid 净夏普较差者;方向与半衰期在 train 上选。

**D2. Q: Why rank first, then smooth? / 为什么先排序再平滑?**
- **A-EN:** If you smooth raw values, a convex transform of a signal is a different signal and can rebuild volatility exposure,
  which the reward then pays for. Ranking first makes every monotone transform the same signal with the same score. That was
  one of the two leaks fixed in C07.
- **A-中:** 先平滑原始值时,凸变换能重新造出波动暴露并被奖励;先排序则任何单调变换得分相同。这是 C07 修的两个漏洞之一。

**D3. Q: Why squares and cubes of the controls? / 为什么用控制变量的平方和三次方?**
- **A-EN:** Linear neutralisation removes a linear exposure but not a U-shape (both extremes of size) or an S-shape. Many
  "discoveries" were non-linear rewrites of size or volatility. Adding squares and cubes of the ranks removes those shapes.
- **A-中:** 线性中性化去不掉 U 形、S 形暴露;很多「发现」是市值或波动的非线性改写。
- 跟进 / follow-up: "Why not a full non-parametric neutralisation?" — EN: cubic on ranks catches the common shapes cheaply and
  is the same for every arm; bucket-wise neutralisation is a possible next step. 中:三次多项式便宜且对各组一视同仁,分桶中性化
  可以作为下一步。

**D4. Q: Why top-decile long-only rather than IC? / 为什么用十分位多头书,不用 IC?**
- **A-EN:** IC rewards ranking the whole cross-section, including the short side we cannot trade. The product is the long book,
  so the reward should be the long book's net Sharpe after costs.
- **A-中:** IC 奖励整个截面的排序,包括做不了的空头;产品是多头书,奖励就应该是扣费后的多头净夏普。

**D5. Q: Why min(train, valid) as the score? / 为什么 score 取 train 与 valid 的较小值?**
- **A-EN:** It penalises candidates that look good in only one period, a cheap guard against overfitting either one.
- **A-中:** 惩罚只在一个时期好看的候选,廉价地防止过拟合某一段。

**D6. Q: How is the library turned into one book? / 因子库怎么变成一本书?**
- **A-EN:** Greedy de-duplication on residual signals (drop a head with ρ ≥ 0.7 or ρ ≤ −0.5 against a kept one), then
  equal-weight z-rank fusion, then neutralise the fused signal once more on the same 16-column basis, then the same
  top-decile long-only book.
- **A-中:** 按残差信号贪心去重(与已留的 ρ ≥ 0.7 或 ≤ −0.5 的丢掉)→ 等权 z-rank 融合 → 融合后再中性化一次 → 同样的十分位多头书。

**D7. Q: Why re-neutralise the fused book? / 为什么融合后再中性化?**
- **A-EN:** In C07's development analysis, fusing many individually neutral heads brought back control exposure. Re-neutralising
  treats the fused signal like any single head. It was added after C07's read, for all arms equally, and the un-neutralised
  version is reported as secondary.
- **A-中:** C07 的开发分析发现,多个各自中性的 head 等权融合后会带回控制暴露;再中性化对所有组相同,是读过 C07 后加的,
  不中性化的版本作为次要结果。

**D8. Q: Why equal-weight fusion? / 为什么等权融合?**
- **A-EN:** Fitting weights on the same in-sample data would add another degree of freedom and more overfitting; equal weight
  is the conservative common choice for all arms.
- **A-中:** 在样本内拟合权重会多一层自由度和过拟合;等权对各组一视同仁,是保守选择。

**D9. Q: Why Wilcoxon signed-rank, one-sided? / 为什么用单侧 Wilcoxon 符号秩?**
- **A-EN:** The unit is a seed pair, there are only 8, and Sharpe differences are not normal. Wilcoxon uses signs and ranks of
  the paired differences without a normality assumption. One-sided because the question is directional: does P do better.
  Verdicts are three-way: better, worse, or cannot tell.
- **A-中:** 单位是种子对,只有 8 对,夏普差不正态;Wilcoxon 只用差的符号和秩;问题是有方向的;判定三选一。

**D10. Q: Why seeds as the unit of replication? / 为什么以种子为重复单位?**
- **A-EN:** GP is stochastic; the variance of a whole research run across seeds is the noise we must beat. Pairing A and P on
  the same seed and the same main search M removes the shared part of that noise. Note what the pairs are not: they measure
  run-to-run search noise on one market history, not eight independent markets or periods.
- **A-中:** GP 是随机的,整个研究流程在种子间的方差就是要战胜的噪声;同种子、同 M 配对消掉共有部分。注意:8 对衡量的是同一段
  市场历史上搜索运行之间的噪声,不是 8 个独立的市场或时期。

**D11. Q: Why 8 seeds? / 为什么 8 个种子?**
- **A-EN:** Compute: each seed is a full three-round study with LLM calls. With 8 pairs the smallest attainable one-sided
  p is 1/256 ≈ 0.004, enough room for a clear verdict. C03/C04 used 16; more seeds is on the next-step list.
- **A-中:** 算力和 token 限制;8 对时单侧最小 p 约 0.004,足以给出明确判定;C03/C04 用过 16 个;加种子在下一步里。

**D12. Q: What counts as "the known family"? / 已知族是什么?**
- **A-EN:** `cross_mean(day_std(Amt), 30)` — the 30-day mean of intraday dispersion of traded value — which dominated early
  discoveries. Anything with |ρ| ≥ 0.5 to it is disqualified, and it is one of the five controls.
- **A-中:** `cross_mean(day_std(Amt), 30)`,早期发现大多是它;|ρ| ≥ 0.5 判不合格,也是五个控制之一。

**D13. Q: How is direction chosen without peeking? / 方向怎么定才不偷看?**
- **A-EN:** On train only, per expression. The verdict books use those train-chosen directions and half-lives.
- **A-中:** 只在 train 上逐表达式选;判读用 train 选好的方向和半衰期。

**D14. Q: How do you know the read reproduces the search? / 怎么确认判读与搜索一致?**
- **A-EN:** Before the read, an in-sample dry run rebuilds every head on the full view and checks its train and valid score
  against the search record. In C08 **152 of 155** reproduce; C07 111 of 112; C05 496 of 543, with each failure explained.
- **A-中:** 判读前先做样本内试跑,重算每个 head 并核对搜索时的分数;C08 152/155,C07 111/112,C05 496/543(逐个解释)。

---

## E. Partura 的结构与角色 / Agent architecture

**E1. Q: What are the roles? / 有哪些角色?**
- **A-EN:** Anatomist (Opus 5) reads the locate output and explains where alpha comes from; librarian (Sonnet 5) finds
  literature dated before 2023-08-08; PI (Opus 5.5) writes the missions; auditor (Opus 5.5) scores the plan; checker (Haiku 5.5)
  runs rule checks. In C08's lean rounds, anatomist and librarian were dropped and PI and auditor ran on Sonnet.
- **A-中:** 解剖员(Opus 5)、文献员(Sonnet 5,只用 2023-08-08 之前的文献)、PI(Opus 5.5)、审计员(Opus 5.5)、检查(Haiku 5.5);
  C08 精简轮去掉解剖与文献,PI 与审计员用 Sonnet。

**E2. Q: What is the locate tool? / 定位工具是什么?**
- **A-EN:** Code, no LLM. It reads M's batches (train/valid only) and produces: the heads table; subtree commonality — for each
  subtree, the mean score of candidates containing it versus not, with a p-value and count; and ablations on each head —
  sufficiency (the subtree alone), knockout (skip one operator), swap (change field), window (halve or double).
- **A-中:** 纯代码:heads 表;子树共性(含 / 不含该子树的候选均分差、p、个数);对每个 head 的拆解 —— 充分性、敲除、换字段、改窗口。

**E3. Q: Define E, R, N. / 定义 E、R、N。**
- **A-EN:** E (deepen): fix a core subtree from a head or the commonality table; every seed must contain it verbatim; GP grows
  only the periphery; at most 2 E slots per core per experiment. R (replace): up to 16 direct variants of a head; if a variant
  scores at least 0.1 higher, it replaces the head (ρ ≥ 0.5 with it) or is added as a new head (ρ < 0.5 and < 0.7 with all
  heads). N (new idea): a new mechanism with up to 16 seeds filling at most half the initial population.
- **A-中:** E:固定核心,种子必须原样含核心,GP 只长外围,每个核心至多 2 个 E 位;R:至多 16 个直接评估的变体,高 0.1 以上则替换
  或收录;N:新机制,至多 16 个种子、占初代至多一半。

**E4. Q: Why must E seeds contain the core verbatim? / 为什么 E 的种子必须原样含核心?**
- **A-EN:** So the mission tests the belief "this core is the source" — GP can change everything around it but not the claimed
  source. Without that, GP drifts and the belief is not tested.
- **A-中:** 这样检验的是「核心就是来源」这一信念;GP 可以改外围,不能改被声称的来源。

**E5. Q: Why is the main search untouched? / 为什么主搜索不让碰?**
- **A-EN:** C01–C04: when the LLM steered GP inside a fixed budget, its mistakes crowded out exploration — e.g. in C04 its ban
  removed the family that later held on test (discoveries 53 vs 173). Keeping M untouched keeps M's discoveries in P's library.
  It does not guarantee the fused book is no worse — fusion can dilute, and in C08 P's book was below M's in three seeds — but it
  removes the C01–C04 failure of crowding out search.
- **A-中:** C01–C04 里 LLM 在固定预算内指挥 GP,错误挤掉探索(C04 的禁令删掉了后来在测试段站住的那一族,发现 53 对 173);
  M 不动让 M 的发现始终在 P 的库里,但不保证融合后的组合不更差(C08 里有 3 个种子 P 低于 M);它消除的是「挤掉探索」这个失败。

**E6. Q: What does the auditor do in C08? / C08 里审计员做什么?**
- **A-EN:** It sees only the plan, a correlation table computed by code, the locate output and earlier rounds' finals — not the
  PI's notes. It may block only maths problems (look-ahead, numerical artefacts, broken definitions) and plain duplicates of a
  head or control. Seeds are auto-struck at |ρ| ≥ 0.7 to a head or ≥ 0.8 to a control; a slot passes with novelty ≥ 3,
  soundness ≥ 3 and at least 4 seeds left. For every pass it writes where the alpha most likely comes from.
- **A-中:** 只看计划、代码算的相关度表、定位输出和之前各轮的定稿,不看 PI 的笔记;只挡数学问题和明显重复;自动划线(head ≥ 0.7、
  控制 ≥ 0.8);通过条件创新度、合理度 ≥ 3 且剩 ≥ 4 个种子;放行时写出最可能的 alpha 来源。

**E7. Q: Why make the auditor permissive after C06? / C06 之后为什么让审计员变宽松?**
- **A-EN:** In C06 the strict auditor's rejected seeds did better out of sample than its accepted ones: test −0.53 vs −0.91,
  34% vs 15% positive, accepted better in only 3 of 24 seed-rounds. Its mathematical critiques were right; its predictive
  judgement was not. So C08 keeps the critique and removes the gate.
- **A-中:** C06 严格审计员挡掉的反而更好(−0.53 对 −0.91,34% 对 15%,24 对里放行的只赢 3 对);数学批评是对的,预测判断不对。

**E8. Q: Did the permissive auditor block anything? / 宽松审计员挡了什么?**
- **A-EN:** 46 of 48 slots passed. Two became plain GP: one scored novelty 1 and soundness 1 (seed 804, round 2); one kept only
  3 of 12 seeds after the correlation strikes (803, round 3). Seeds kept 476 of 592; R groups 30 of 30.
- **A-中:** 48 个位过 46 个;2 个改普通 GP(804 第 2 轮 1/1 分;803 第 3 轮划完只剩 3 个);种子 592 留 476;R 组 30/30。

**E9. Q: How is information isolated? / 信息怎么隔离?**
- **A-EN:** Agents see only 2018 to 2023-08-07; literature must predate 2023-08-08; they cannot read other seeds, other studies,
  the PLAN (which contains earlier test numbers) or any results directory. Reads are audited from session logs after each round.
- **A-中:** agent 只见 2023-08-07 之前的数据;文献须早于 2023-08-08;不能读其他种子、其他研究、PLAN、结果目录;事后按会话记录审计。

**E10. Q: Why separate the PI from the auditor? / 为什么 PI 和审计员分开?**
- **A-EN:** Proposer and judge should not be the same mind; the auditor does not see the PI's reasoning, only the plan, so a
  persuasive narrative cannot carry a broken formula through.
- **A-中:** 提议者与评判者分开;审计员只看计划不看理由,说服力强的叙述带不过坏公式。

**E11. Q: What does a mission file look like? / 任务文件长什么样?**
- **A-EN:** YAML: two slots, each with type (E or N), core (for E), a hypothesis stating mechanism, implementation and why it
  should survive out of sample, literature with dates, and 8–16 seeds; optional R groups with the head, why, and variants.
  A deterministic checker rejects inadmissible plans before the audit.
- **A-中:** YAML:两个任务位(类型、核心、假设:机制/实现/为何样本外还在、带日期的文献、8–16 个种子)+ 可选 R;确定性检查先过一遍。

**E12. Q: How many rounds and why three? / 几轮,为什么三轮?**
- **A-EN:** Three per seed; round k sees M's batches 1..k. Three gives the belief loop two chances to update on its own results
  while keeping the token and GPU budget bounded.
- **A-中:** 每个种子 3 轮,第 k 轮看 M 的第 1..k 批;让信念有两次根据自身结果更新的机会,同时控制成本。

**E13. Q: Why is the schedule fixed rather than asynchronous? / 为什么信息时间表固定?**
- **A-EN:** So both arms see the same information at the same time and the comparison is clean. It is a known limitation — a
  real desk would be asynchronous.
- **A-中:** 让两组同时看到同样的信息,比较干净;这是已知局限。

**E14. Q: What if an agent fails mid-round? / agent 中途失败怎么办?**
- **A-EN:** Every step writes a file; a restart resumes at the first missing file. Usage-limit interruptions in C05, C06 and C08
  were resumed seed by seed, each logged as a PLAN revision.
- **A-中:** 每步落盘,重启从第一个缺失的文件续跑;C05、C06、C08 的用量中断都逐种子续跑并记为 PLAN 修订。

---

## F. C01–C07 逐个 / Each earlier study

**F1. Q: C01 — design and result? / C01 的设计与结果?**
- **A-EN:** Partura wrote guidance files — priors and neighbourhoods that reweight GP's proposal distribution; 3 rounds,
  8 seeds, budget 192 per arm per seed; plain long reward, no neutralisation. **Worse:** valid test heads A 19, Partura 13.
- **A-中:** 写指引文件(先验 + 邻域)改 GP 提议分布;3 轮、8 种子;未中性化奖励。**更差**:A 19、Partura 13。

**F2. Q: Why did C01 fail? / C01 为什么失败?**
- **A-EN:** The only channel was syntactic priors matched on how a formula is written; a belief about a mechanism cannot pass
  through that. Also, one revision that removed `ts_spearman` discoveries from both arms (A 90, B 1) favoured B and B still lost.
- **A-中:** 只能通过「按写法匹配的先验」影响 GP,信念传不过去;去掉 `ts_spearman` 的修订偏向 B,B 仍输。

**F3. Q: C02? / C02?**
- **A-EN:** The LLM tested its hypotheses directly with controlled variants and designed the initial population; GP refined.
  **Worse:** new valid heads uncorrelated with C01's, A 7 vs Partura 2.
- **A-中:** LLM 直接检验假设、设计初始种群,GP 精修。**更差**:新有效 head A 7、Partura 2。

**F4. Q: What did C02 teach? / C02 的教训?**
- **A-EN:** Most "valid" heads in C01–C02 were style exposure: after style neutralisation C01's went 19 → 2 and 13 → 1,
  C02's 7 → 2 and 2 → 0. Both the searcher and the agent were optimising a reward that paid for style.
- **A-中:** 「有效」head 大多是风格暴露:中性化后 C01 19 → 2、13 → 1,C02 7 → 2、2 → 0;两边都在优化为风格付钱的奖励。

**F5. Q: C03? / C03?**
- **A-EN:** Reward = residual book after liquidity, volatility, reversal and the known family; 16 seeds; threshold 0.5.
  **Cannot tell:** new valid heads 0 and 0 (A's best t = 1.98); none of Partura's direct mechanism tests passed.
- **A-中:** 奖励改为残差书;16 种子。**分不出**:都是 0(A 最好 t = 1.98);Partura 的直接机制检验全不过。

**F6. Q: C04? / C04?**
- **A-EN:** Both arms got six daily fields; size added to controls; long leg only; 16 seeds; primary became the paired fused-book
  Sharpe. **Cannot tell, leaning worse:** median −0.17, p(worse) 0.11, B higher in 4 of 16. Partura's ban removed A's family
  that held on test (discoveries 53 vs 173); direct tests 0 of 64. One construction survived: daily return scaled by limit width
  — 12 of its 14 GP descendants positive on test — but GP reversed Partura's sign, and its forward mean was 0.04.
- **A-中:** 两组加 6 个日频字段、控制加市值、只看多头、16 种子、主指标改为配对融合书。**分不出(偏差)**:中位 −0.17、p 0.11;
  禁令删掉 A 的有效族;直接检验 0/64;唯一留下的构造(日收益除以涨跌幅限制)方向被 GP 反转,前推均值 0.04。

**F7. Q: What is the C04 lesson? / C04 的教训?**
- **A-EN:** Inside a fixed budget, every LLM mistake costs exploration directly. That is why C05 onward leave M untouched and
  give Partura only extra budget.
- **A-中:** 固定预算里 LLM 的错误直接挤掉探索 → C05 起 M 不动,只给额外预算。

**F8. Q: C05 design? / C05 设计?**
- **A-EN:** M untouched; each round a snapshot of M's first k batches plus the arm's earlier missions; 3 rounds, 256 extra
  evaluations per round per arm. A = 2 plain GP; B = locate → anatomist → librarian → PI → checker with E/R/N missions;
  B0 = the same tools and mission types driven by fixed rules, no LLM.
- **A-中:** M 不动;每轮快照;3 轮,每轮每组 256 次额外评估;A 普通 GP;B 是 LLM 流程;B0 是同样工具但由死规则驱动。

**F9. Q: C05 result? / C05 结果?**
- **A-EN:** **Cannot tell.** Test median +0.08, p 0.42; mean book 0.44 for both. Selection (valid) B 1.52 vs A 0.94, higher in
  7 of 8. Forward B 0.29 vs A 0.87, lower in 6 of 8. B's extra heads were the weakest singly: test Sharpe 0.32 vs A 0.80,
  B0 0.69; test-valid heads B 3/94, A 15/101, B0 10/56.
- **A-中:** **分不出**:中位 +0.08、p 0.42、均值都是 0.44;选拔期 1.52 对 0.94;前推 0.29 对 0.87;B 的单个 head 最弱。

**F10. Q: Why did C05 look good in selection but not on test? / C05 为什么选拔好、样本外没了?**
- **A-EN:** Post-read inference: Goodhart. The LLM was better at optimising a leaky reward — convex transforms rebuilt
  volatility; at least 5 of 25 E cores were size or volatility rewritten. And researcher degrees of freedom: with the same locate
  information, the LLM's picks were worse than fixed rules (B0).
- **A-中:** 读后推断:古德哈特 —— LLM 更会优化有漏洞的奖励(凸变换重造波动;25 个 E 核心至少 5 个是市值/波动改写);研究者自由度
  —— 同样的信息,LLM 挑得比死规则差。

**F11. Q: What did C05 get right? / C05 做对了什么?**
- **A-EN:** It kept M's discoveries available: with M untouched, Partura's test book tied A's (0.44 vs 0.44). That is not a
  guarantee — fusion can dilute, and in C08 P's book was below M's in three seeds — but it removed the C01–C04 problem of the
  LLM crowding out search. That architecture is kept in C08.
- **A-中:** M 不动让 M 的发现始终可用:C05 测试段 Partura 与 A 打平(0.44 对 0.44)。这不是保底保证(融合会稀释;C08 有 3 个种子
  P 低于 M),但消除了 C01–C04「LLM 挤掉探索」的问题;这个架构保留到 C08。

**F12. Q: C06 design and result? / C06 设计与结果?**
- **A-EN:** C05 plus an independent auditor (Opus 5.5) scoring novelty and soundness 1–5 before any mission ran; seeds struck
  at |ρ| ≥ 0.7 to a head or ≥ 0.5 to a control; up to 3 rewrites. All 48 slots eventually passed; seeds accepted 474, struck
  147. **Cannot tell:** median +0.01, p 0.42, 4 wins 4 losses; selection again better (train 1.95 vs 1.44).
- **A-中:** C05 + 独立审计员(创新度、合理度 1–5,至多重写 3 次);48 个位最终全过。**分不出**:中位 +0.01、p 0.42、4 胜 4 负。

**F13. Q: What was the VWAP error? / VWAP 错误是什么?**
- **A-EN:** In seed 806 round 1, the PI's E core was `day_cov(Vwap, Ret)`. It derived the covariance as if each minute's VWAP were
  the bar's close (θ = 1), giving ≈ Q/2 − Rδ. The auditor pointed out VWAP is an average inside the bar; with θ its position in
  the bar, the term is ≈ (θ − ½)Q − Rδ — a non-linear liquidity trait that linear neutralisation cannot remove. The four E seeds'
  correlation with liquidity rose with the averaging window (0.35 to 0.73), and three were struck.
- **A-中:** 806 第 1 轮,PI 把分钟 VWAP 当成 bar 收盘价推导 `day_cov(Vwap, Ret)`(θ = 1);审计员指出 VWAP 是 bar 内均价,项变为
  (θ − ½)Q − Rδ,是线性中性化去不掉的非线性流动性特征;4 个 E 种子与流动性的相关随平均窗口升高(0.35 到 0.73),划掉 3 个。

**F14. Q: Why did a correct auditor filter badly? / 审计员的判断都对,为什么筛选结果差?**
- **A-EN:** Post-read inference: the yardstick paid for non-linear rewrites of controls, which the auditor correctly blocked —
  so under that yardstick its blocks looked costly. Mechanistic soundness is also simply not the same as predictive value. The
  disease was the yardstick, which C07 addressed.
- **A-中:** 读后推断:尺子在为「控制变量的非线性改写」付钱,审计员按规则挡掉,于是显得更差;机制合理也不等于能预测。病根在尺子。

**F15. Q: C07 design and result? / C07 设计与结果?**
- **A-EN:** Fixed the yardstick (rank first; non-linear neutralisation) and reran M and A without LLM. Then an LLM verifier
  (Opus 5.5) kept or dropped each candidate head: V_tr saw train only, V_all also valid. **Cannot tell, leaning V:** median
  +0.11, p 0.062, 4 wins 1 loss, 3 ties; forward 5–0, p 0.031. Only 68 candidates survived the new yardstick; all arms' test
  books were negative (A −0.52, V_tr −0.09).
- **A-中:** 修尺子并在新尺子下重跑 M、A;LLM 验证员逐个留去(只看 train / 也看 valid)。**分不出(偏 V)**:中位 +0.11、p 0.062;
  候选只剩 68 个;各组测试段都为负。

**F16. Q: What did C07 reveal? / C07 揭示了什么?**
- **A-EN:** The verifier kept 9 of 68; the 59 it dropped did better singly (+0.40 vs −0.13). The book improved mostly by holding
  fewer heads — 807 kept none (0 beats −0.22), 808 kept 1 of 37. So filtering was not discrimination, and C08 put the LLM back
  to proposing. It also suggested that equal-weight fusion of many heads can cancel signal and leave shared exposure, which led
  to re-neutralising the fused book.
- **A-中:** 验证员留 9/68,去掉的单个更好(+0.40 对 −0.13);书变好主要因为 head 少了。所以过滤不等于鉴别,C08 让 LLM 回到提出;
  也引出了融合后再中性化。

---

## G. C08 设计与结果 / C08 in detail

**G1. Q: What is C08's question? / C08 的问题?**
- **A-EN:** Under the fixed yardstick, does the same extra compute give a better out-of-sample library when Partura assigns the
  missions (P) than when it goes to more plain GP (A)?
- **A-中:** 修好的尺子下,同样的额外算力交给 Partura 派任务,样本外是否好过多跑普通 GP?

**G2. Q: What changed from C06's mission design? / 与 C06 的派任务设计相比改了什么?**
- **A-EN:** Three things: the new yardstick everywhere (E rewards, R evaluation, locate); round 1 recomputed from scratch under
  it; and the permissive audit rule. M and A were reused from C07 — same seeds 801–808, same yardstick.
- **A-中:** 三处:新尺子用于 E/R/定位;第 1 轮在新尺子下重算;宽松审计。M、A 复用 C07。

**G3. Q: What is the lean flow and why? / 精简流程是什么,为什么?**
- **A-EN:** After round 1, the LLM quota ran low. Rounds 2–3 (and seed 808's round 1) dropped the anatomist and librarian,
  ran PI and auditor on Sonnet, and audited once — a failing slot became plain GP. GP missions, budgets, yardstick and verdict
  rules did not change. It was recorded as PLAN revision 1 before any C08 result existed.
- **A-中:** 第 1 轮后额度紧张;第 2、3 轮去掉解剖与文献、PI 与审计用 Sonnet、只审一次;GP 任务、预算、尺子、判定不变;在任何结果
  之前记为修订 1。

**G4. Q: What is revision 2? / 修订 2 是什么?**
- **A-EN:** When the owner's quota ran out mid round 3, the remaining steps were finished in a separate cloud session: 803's
  finalisation (deterministic; I first reproduced the other six seeds' finals byte for byte), and 808's PI plan and audit by
  fresh agents with the same prompts and read restrictions. Recorded before any result.
- **A-中:** 第 3 轮中途额度用完,在云端会话收尾:803 定稿(确定性,先逐字节复现另外 6 个种子)、808 的 PI 与审计由新起的 agent
  按同样提示和读取限制完成;在结果之前记录。

**G5. Q: Is the budget really matched? / 预算真的匹配吗?**
- **A-EN:** By design, yes: each arm gets 256 evaluations per seed per round — A as two GP runs of 128, P as two missions of 96
  plus up to 16 direct R evaluations and up to 48 locate evaluations. Actually scored: A 4,438, P 4,525 (+2%), so "comparable",
  not identical. GPU seconds: A 26,294, P 24,421. LLM tokens are not matched — A has none — and are reported separately.
- **A-中:** 按设计是:每组每种子每轮 256 次 —— A 是两次 128 的 GP,P 是两个 96 的任务 + 至多 16 次 R + 至多 48 次定位。实际打分
  A 4,438、P 4,525(+2%),所以是「可比」而非完全相同;GPU 秒 A 26,294、P 24,421;token 不匹配(A 没有),单独报告。

**G6. Q: The headline result? / 主结果?**
- **A-EN:** **P better, median +0.23, p = 0.012, 7 wins 1 loss** (802, −0.12). Mean fused-book test Sharpe A −0.33, P +0.16.
  Forward: median +0.54, 7 of 8, p = 0.020; means A −0.28, P +0.46.
- **A-中:** **P 更好,中位 +0.23,p 0.012,7 胜 1 负(802 −0.12)**;均值 A −0.33、P +0.16;前推 +0.54、8 胜 7、p 0.020。

**G7. Q: Per seed? / 逐种子?**
- **A-EN:** P − A: 801 +0.07, 802 −0.12, 803 +0.25, 804 +1.40, 805 +1.07, 806 +0.20, 807 +0.82, 808 +0.21. Test books
  A / P: 805 −1.05 / +0.02, 807 −0.97 / −0.16, 804 −0.45 / +0.95.
- **A-中:** 见左;大的差距在 804、805、807。

**G8. Q: What about P vs M and A vs M? / P 对 M、A 对 M?**
- **A-EN:** P vs M: +0.24, 5 wins 3 losses, p 0.098 — not significant. A vs M: 0.00, 2 wins 3 losses — extra GP did not help on
  average and hurt three books (803, 806, 807 by 0.37–0.48).
- **A-中:** P 对 M +0.24、5 胜 3 负、p 0.098,不显著;A 对 M 0.00,在 803、806、807 拖累了组合。

**G9. Q: So where does P's edge come from? / P 的优势从哪来?**
- **A-EN:** Two patterns. Where GP's extra search found nothing new (804, 805: A identical to M), Partura's missions added heads
  that held (+1.40 and +1.07 vs A). Where GP's extra heads hurt (803, 806, 807), Partura's hurt less or helped. It is allocation
  of extra search, not a high-Sharpe factor: P's median book is +0.05. This is a reading after the result, not a test.
- **A-中:** 两种情形:GP 什么也没加的种子(804、805)Partura 加了站得住的 head;GP 的额外 head 拖累的种子 Partura 拖累更小或有帮助。
  价值在分配,不在高夏普;读后解读。

**G10. Q: How did P's extra heads do individually? / P 新增的 head 单个表现?**
- **A-EN:** 55 extra heads: median test Sharpe +0.07, 32 positive. Round 3's were best (12 heads, median +0.34, 10 positive);
  round 1's full-flow heads were worst (15, −0.34, 5 positive). Round and flow are confounded.
- **A-中:** 55 个,中位 +0.07,32 个为正;第 3 轮最好(10/12),第 1 轮完整流程最差(5/15);轮次与流程混在一起。

**G11. Q: Does that mean the cheap flow is better? / 这说明便宜的流程更好吗?**
- **A-EN:** No. Round 3 saw more of M and two rounds of its own feedback; the flow changed at the same time. You cannot separate
  them from this design. A fixed-flow rerun is on the next-step list.
- **A-中:** 不能。第 3 轮看到更多 M 和自身两轮反馈,流程同时变化,分不开;下一步用固定流程重跑。

**G12. Q: What was the most common structure found? / 最常见的结构是什么?**
- **A-EN:** The intraday volume centroid, `day_centroid(Volume)` — where in the day a stock's volume trades — appeared in 17 of
  55 extra heads. It did not hold out of sample: median test +0.03, forward mean −0.23.
- **A-中:** 成交量日内重心 `day_centroid(Volume)`,出现在 17/55 个新增 head 里;样本外没站住(测试中位 +0.03)。

**G13. Q: Show me one signal end to end. / 给我看一个完整的信号。**
- **A-EN:** Backup page "one finished signal card". Seed 808, round 1, E slot on the core `day_wmean(Ret, Volume)`. The PI's seed
  summed the best-quartile and worst-quartile volume-weighted days over 120 days, so volatility cancels and upside asymmetry
  remains — a MAX/lottery effect (Bali, Cakici, Whitelaw 2011). GP replaced the downside term with the volume centroid, so the
  PI's thesis no longer describes the signal. Final: test +0.90, forward +0.59. I chose it after the read for readability; it is
  not typical.
- **A-中:** 808 第 1 轮 E 位;PI 的种子用上下四分位相加抵消波动、留下上行不对称(MAX 效应);GP 把下行项换成了成交量重心,
  PI 的论点不再适用;测试 +0.90、前推 +0.59;读后按可读性挑的,不典型。

**G14. Q: How do you explain a signal GP changed? / GP 改过的信号怎么解释?**
- **A-EN:** The thesis must describe the final expression, not the seed. If GP changed the structure or the sign, the original
  explanation is void and the new one is an untested reading until a direct test supports it.
- **A-中:** 论点必须描述最终表达式;GP 改了结构或方向,原解释作废,新解释在被检验前只是解读。

**G15. Q: Did the strict shadow auditor differ? / 旁听的严格审计员有不同吗?**
- **A-EN:** It scored the six slots of seeds 801, 803, 805 in round 1 at 3 or 4 — it would also have passed all of them — so the
  planned split "slots it would block" is empty.
- **A-中:** 801、803、805 第 1 轮 6 个位都给 3–4 分,也会全部放行;「它会挡的」一组为空。

**G16. Q: Walk through seed 808 round 3. / 讲讲 808 第 3 轮。**
- **A-EN:** Locate: `cs_rank(ts_mean(day_centroid(Volume), 20))` alone scored +1.28 and was necessary in a +0.83 head. E slot
  around that core (drift, instability, bucketing); N slot on the shape of the minute-volume distribution (Gini, tail ratio).
  Audit: E novelty 3, soundness 4, 11 of 12 seeds; N 4/4, 10 of 12 (one seed was the liquidity control, |ρ| 0.80). Output:
  E found 3 heads (test +0.50, +0.39, −0.43); N none.
- **A-中:** 见左。

**G17. Q: Why was the slot-b core in 803 round 3 flagged "junk" but passed? / 803 第 3 轮那个「废品」标记为何没挡?**
- **A-EN:** The flag measures whether ties in the decile book are broken by column order; the rules say tie-breaking by column
  order is not a maths problem (column order carries board information), and the evaluated seeds were all transformed versions
  without the flag. The auditor checked the source code before passing it.
- **A-中:** 该标记测的是十分位并列是否靠列序打破;规则写明这不是数学问题;实际评估的种子都经过变换、没有该标记;审计员读源码确认。

**G18. Q: How many candidates did P score? / P 打分了多少候选?**
- **A-EN:** 48 slots of 52 to 108 scored candidates each; E slots produced 35 heads (20 of 25 E slots found at least one),
  N slots 13 heads (9 of 21).
- **A-中:** 48 个位,每个 52–108 个候选;E 位 35 个 head(25 个位里 20 个有产出),N 位 13 个(21 个里 9 个)。

**G19. Q: Was the fusion re-neutralised in the verdict? / 判读用的是再中性化的融合书吗?**
- **A-EN:** Yes, as pre-registered for all arms. The un-neutralised version is a secondary output; I have not used it for any
  claim.
- **A-中:** 是,事先约定、所有组相同;不中性化版本是次要输出,没用于任何结论。

**G20. Q: What does C08 not show? / C08 没有说明什么?**
- **A-EN:** That Partura beats the base search; that any individual factor is good; that the lean flow is better; that the
  result is independent of the earlier reads of the test segment.
- **A-中:** 不说明 Partura 胜过基础搜索、不说明某个因子好、不说明精简流程更好、不独立于之前对测试段的读取。

---

## H. 统计与有效性 / Statistics and validity

**H1. Q: Is p = 0.012 real? / p = 0.012 可信吗?**
- **A-EN:** It is the correct nominal value of the pre-specified test on these 8 pairs. But the test segment had been read
  seven times and those reads shaped C08's design, so it is a development result. *C08 is the first design that produced a
  statistically significant paired improvement under its pre-specified within-study test. Because earlier designs repeatedly
  used the same test period, I treat it as a promising development result rather than independent confirmation.*
- **A-中:** 名义值正确,但测试段被读过 7 次、影响了设计,所以是开发期结果(念那句统一口径)。

**H2. Q: Isn't this the garden of forking paths? / 这不就是分岔路花园吗?**
- **A-EN:** Partly, yes, across studies: eight designs, each informed by the previous read. Within C08 the rules, arms and
  test were fixed before any run and the read happened once. The cure for the across-study part is fresh data with a frozen
  protocol, which is the first next step.
- **A-中:** 跨研究层面是的;C08 内部规则事先固定、只读一次;跨研究的问题只能靠冻结流程在新数据上解决。

**H3. Q: Should you correct for 8 studies? / 要不要对 8 次研究做多重比较校正?**
- **A-EN:** A Bonferroni over eight would put the bar at about 0.006, and 0.012 would not clear it. The studies are not
  independent tests of one hypothesis — each tested a different design — but the conservative reading is the same: not
  confirmed.
- **A-中:** 按 8 次 Bonferroni 门槛约 0.006,0.012 过不了;各研究检验的不是同一假设,但保守结论相同:未确认。

**H4. Q: What is the power with 8 pairs? / 8 对的功效?**
- **A-EN:** The smallest attainable one-sided p is 1/256 ≈ 0.004. Seven wins gives p between 0.008 and 0.098 depending on the
  rank of the loss; here the loss was the second smallest, giving 0.012. One flipped seed could change the verdict.
- **A-中:** 最小 p 约 0.004;7 胜 1 负的 p 在 0.008–0.098 之间,取决于输的那对的秩;这里输的是第二小,得 0.012。

**H5. Q: Why one-sided? Isn't that generous? / 单侧是不是太宽松?**
- **A-EN:** It was pre-registered and directional, and "worse" is tested separately with its own one-sided p (0.99 here). A
  two-sided p would be 0.023, still under 0.05.
- **A-中:** 事先约定、有方向;「更差」单独检验(这里 0.99);双侧也是 0.023。

**H6. Q: Is the forward period independent confirmation? / 前推段算独立确认吗?**
- **A-EN:** No. It is short (0.67 years) and was read in earlier studies. It is consistent (7 of 8, p 0.020) — useful, not
  decisive.
- **A-中:** 不算:短、被读过;方向一致,有用但不决定性。

**H7. Q: Could the result be "fewer heads", like C07? / 会不会只是「head 少了」?**
- **A-EN:** Possibly partly. P actually had about as many heads as A (65 vs 67 after de-duplication), so it is not simply a
  smaller book; but in seeds like 808, A's 36 heads vs P's 12 could matter. A random or rule-based filter that matches P's head
  count per seed is the control that would settle it.
- **A-中:** 可能部分是。去重后 P 65、A 67,总数相近;但个别种子(808:A 36、P 12)可能有影响。同 head 数随机筛选对照可以回答。

**H8. Q: Could size or volatility exposure explain it? / 会不会是市值或波动暴露?**
- **A-EN:** Every head and the fused book are residualised on the five controls including squares and cubes, so linear, U and S
  exposures are removed by construction. Residual exposures to factors outside the five are possible and untested.
- **A-中:** 每个 head 和融合书都对 5 个控制及平方三次方取残差;5 个之外的暴露可能存在,未检验。

**H9. Q: Did anything change after you saw C08's numbers? / 看到 C08 结果后有没有改东西?**
- **A-EN:** No rule or comparison changed. After the read I added interpretation — the three-level reading and the round
  breakdown — and labelled it as post-read analysis.
- **A-中:** 没有改规则或比较;读后只加了解读,并标明是读后分析。

**H10. Q: How do you prevent the LLM from leaking the future? / 怎么防止 LLM 泄露未来?**
- **A-EN:** Data after 2023-08-07 is never shown, literature must predate 2023-08-08, and reads are audited. But the model's
  training data extends past 2023, so its general priors could encode knowledge of what worked later. That cannot be removed;
  arm A has no LLM, and the only clean answer is a read on data after the model's knowledge, i.e. after 2026-09-16.
- **A-中:** 不给 2023-08-07 之后的数据、文献须早于 2023-08-08、读取审计;但模型训练数据晚于 2023,先验可能带有后验知识,无法去除;
  干净的答案是在模型知识之后的数据上读。

**H11. Q: Why trust the auditor's "no maths problem" judgement? / 为什么信审计员说「没有数学问题」?**
- **A-EN:** I don't rely on it alone: the correlation table, admissibility checks, finite-value checks and the in-sample
  reproduction are code. The auditor's value is catching conceptual errors code cannot see, like the VWAP case.
- **A-中:** 不只靠它:相关度表、合规检查、数值检查、复现都是代码;审计员的价值在代码看不到的概念错误。

**H12. Q: What would falsify your claim? / 什么结果会推翻你的主张?**
- **A-EN:** On fresh data after 2026-09-16 with C08 frozen: P not better than A (median ≤ 0, or p(better) large), or P's edge
  disappearing against a same-head-count random filter.
- **A-中:** 冻结 C08、在 2026-09-16 后的新数据上:P 不优于 A;或在同 head 数随机筛选对照下优势消失。

---

## I. 成本 / Cost

**I1. Q: How many tokens? / 用了多少 token?**
- **A-EN:** LLM output tokens: C05 arm B 13.21 M (101 agent calls); C06 arm C 16.91 M (222 calls, 38 by the auditor); C07's
  verifier 1.36 M sub-agent tokens over 16 calls; C04 0.78 M. C08's round 2 in the lean flow was about 4.9 M sub-agent tokens;
  the full-flow round 1 cost about a third of the planned budget.
- **A-中:** C05 1,321 万、C06 1,691 万输出 token;C07 136 万;C04 78 万;C08 第 2 轮精简约 490 万子 agent token。

**I2. Q: Is Partura worth its cost? / Partura 值这个成本吗?**
- **A-EN:** Not established. GPU is matched; tokens are an extra cost A does not pay. The fair test is all-in: give GP the dollar
  equivalent of the tokens as extra compute and compare. That is on the next-step list.
- **A-中:** 尚未证明;GPU 匹配,token 是 A 没有的额外成本;公平检验是把 token 折成钱给 GP 加算力再比。

**I3. Q: Where do the tokens go? / token 花在哪?**
- **A-EN:** In the full flow, mostly on reading: the anatomist reading locate output and code, the librarian searching. The
  lean flow drops those and keeps PI and auditor; C08's lean rounds did not do worse.
- **A-中:** 完整流程主要花在阅读(解剖员读定位与源码、文献员检索);精简流程去掉这两步,C08 精简轮并不更差。

**I4. Q: GPU time? / GPU 时间?**
- **A-EN:** C08: M 19,835 s, A 26,294 s, P 24,421 s on RTX 5090s across two servers; the final read about 7 minutes.
- **A-中:** 如左。

**I5. Q: How would you cut cost further? / 怎么进一步降成本?**
- **A-EN:** Use the cheap model for PI and auditor (already done in lean rounds), cache locate summaries, and call the LLM only
  when the locate output changes materially between rounds.
- **A-中:** PI 与审计用便宜模型(已做)、缓存定位摘要、只在定位输出明显变化时调用 LLM。

---

## J. 局限与风险 / Limitations

**J1. Q: Biggest limitation? / 最大的局限?**
- **A-EN:** The test segment has been read eight times; the result is development evidence. Second: 8 pairs is low power.
- **A-中:** 测试段读了 8 次;其次 8 对功效低。

**J2. Q: Absolute performance is weak — does it matter? / 绝对表现很弱,要紧吗?**
- **A-EN:** For a production alpha, yes; for this question, no. Under the fixed yardstick, everything is residual to five
  controls and their shapes, so books near zero are expected; the question is the paired difference.
- **A-中:** 对生产 alpha 要紧;对这个研究问题不要紧 —— 去掉 5 个控制及其非线性后,接近 0 是预期的,问题看配对差。

**J3. Q: Capacity and turnover? / 容量和换手?**
- **A-EN:** Not studied in the C-series; books are equal-weight top decile with 15 bp costs. AlphaCube's separate tradable
  backtest simulates a 1 M CNY account with lot sizes, per-name caps, suspensions and limit moves, but that was run on AlphaCube's
  own champions, not on C08's books.
- **A-中:** C 系列没研究;AlphaCube 另有 100 万真实账户回测(整手、单票上限、停牌、涨跌停),但跑的是 AlphaCube 冠军,不是 C08。

**J4. Q: Regime dependence? / 依赖行情吗?**
- **A-EN:** Test 2023-08 to 2025-12 includes the early-2024 small-cap crash; forward covers 2026. Two years plus is still one
  market and one period; regime robustness is not established.
- **A-中:** 测试段含 2024 年初小盘暴跌,前推到 2026;仍是一个市场、一个时期。

**J5. Q: Survivorship — how big? / 幸存者偏差有多大?**
- **A-EN:** Not quantified; delisted names are missing. It affects both arms; it would matter more for absolute returns of
  small-cap tilted books.
- **A-中:** 未量化;两组同受影响;对偏小盘的组合绝对收益影响更大。

**J6. Q: Is the process reproducible by someone else? / 别人能复现吗?**
- **A-EN:** The deterministic parts yes: every file is on disk, scripts rebuild the read, and finals reproduce byte for byte.
  LLM steps are stochastic; reproducing them means rerunning with the same prompts and comparing distributions, not outputs.
- **A-中:** 确定性部分可以(逐字节复现);LLM 步骤是随机的,只能重跑比较分布。

**J7. Q: Why only one market? / 为什么只做一个市场?**
- **A-EN:** Data access and the minute cube. The method is market-agnostic; the operators and yardstick would carry over.
- **A-中:** 数据所限;方法与市场无关。

**J8. Q: What about the known family dominating? / 已知族占主导怎么办?**
- **A-EN:** It is a control and a disqualifier (|ρ| ≥ 0.5). C02/C03 showed most early discoveries were it or style; after
  that, nothing is credited for rediscovering it.
- **A-中:** 既是控制也是淘汰线;之后不再为重新发现它给分。

**J9. Q: The protocol changed mid-study (lean flow). Isn't that a problem? / 中途改流程不是问题吗?**
- **A-EN:** It is a limitation, recorded before any result: P is not one constant process. It affects interpretation of what
  part of Partura matters, not the validity of the A-vs-P comparison, since budgets and rules did not change.
- **A-中:** 是局限,结果之前已记录;影响「哪部分有用」的解读,不影响 A 对 P 比较本身。

**J10. Q: Fixed information schedule? / 固定信息时间表?**
- **A-EN:** Round k sees M's first k batches — not truly asynchronous like a live desk. It keeps arms comparable.
- **A-中:** 不是真异步;为了可比。

---

## K. 工程与可复现 / Engineering

**K1. Q: How is a round executed? / 一轮怎么执行?**
- **A-EN:** On the laptop, a workflow runs the LLM roles for all seeds; on each GPU server, a conductor runs the missions when
  a plan appears and computes the next round's locate output; a keeper watches health. Files move with a sync script that
  pushes atomically and checks md5.
- **A-中:** 笔记本上 workflow 跑 LLM 角色;服务器上 conductor 见计划就开跑并算下一轮定位,keeper 做健康检查;同步脚本原子推送并核对 md5。

**K2. Q: What is on disk per round? / 每轮落盘什么?**
- **A-EN:** `loc.md/json` (locate), `missions.yaml` (PI), `corr_n.md/json` (correlation table), `audit_n.yaml` (auditor),
  `missions_final.yaml` and `audit_record.json` (finalised), then each GP slot's `evidence.json`.
- **A-中:** 如左。

**K3. Q: How do you ensure the test is read once? / 怎么保证测试段只读一次?**
- **A-EN:** A ledger file per study; the final script refuses to run a second read for the same tag. Dry runs touch train and
  valid only.
- **A-中:** 每个研究一本台账,同一标签不让读第二次;试跑只碰 train / valid。

**K4. Q: What went wrong operationally? / 工程上出过什么问题?**
- **A-EN:** GPU memory and lock lanes needed tuning; queue time-outs killed jobs; one seed's memory issue moved it to a second
  server; an R-replacement chain bug; usage-limit interruptions. Each is a dated PLAN revision, none changed a comparison rule.
- **A-中:** 显存与锁通道、排队超时、内存问题换服务器、R 链 bug、用量中断;都记为 PLAN 修订,没有改比较规则。

**K5. Q: Two servers — any risk of mismatch? / 两台服务器有不一致风险吗?**
- **A-EN:** Each seed runs entirely on one server; before the read, the old server's evidence is copied to the new one by a
  gather script that checks counts (24 evidence files expected), and the read runs in one place.
- **A-中:** 每个种子只在一台机器上跑;判读前汇总脚本核对数量,在一处读。

**K6. Q: How large is the code base? / 代码规模?**
- **A-EN:** AlphaCube's steering branch passes about 966 tests; Partura has its own test suite (about 280 tests) and scripts per
  study. Default paths were verified byte-identical against the old engine before switching.
- **A-中:** AlphaCube 分支约 966 个测试通过;Partura 约 280 个测试;切换前验证默认路径与旧引擎逐字节相同。

**K7. Q: How do agents hand off work? / agent 之间怎么交接?**
- **A-EN:** Only through files; agent reasoning is not persisted, so anything not written down did not happen. Notes, journals
  and state files let any model resume a study.
- **A-中:** 只靠文件;没写下的判断等于没做;任何模型都能凭状态文件接手。

**K8. Q: Can you replay a round? / 能重放一轮吗?**
- **A-EN:** The deterministic parts — locate, correlation table, finalisation, GP slots with fixed seeds, the read — yes. In
  this study I re-ran six seeds' finalisation and matched the originals byte for byte.
- **A-中:** 确定性部分可以;这次重跑 6 个种子的定稿,逐字节一致。

---

## L. 下一步与入职后 / Next steps and fit

**L1. Q: What exactly would you run next? / 下一步具体跑什么?**
- **A-EN:** (1) Freeze C08 and read once on data after 2026-09-16, separate ledger. (2) Add a control arm: random or rule-based
  selection with P's head count per seed. (3) New seeds with one fixed flow and model set. (4) All-in cost: tokens converted to
  extra GP compute for A.
- **A-中:** 冻结 C08 读新数据;加同 head 数随机筛选对照;固定流程新种子;token 折算算力的全成本比较。

**L2. Q: How would you scale the number of seeds? / 怎么扩大种子数?**
- **A-EN:** The lean flow makes 16–24 seeds affordable; GPU is two slots of 96 evaluations per round per seed, so the bottleneck
  is the LLM calls, which can be batched.
- **A-中:** 精简流程下 16–24 个种子负担得起;瓶颈在 LLM 调用,可以批量。

**L3. Q: How would this fit a research desk? / 放到研究团队里怎么用?**
- **A-EN:** As a budget allocator sitting beside the existing search: it reads the search's output, proposes where to spend the
  next block of compute, and its critic role checks derivations. Its decisions are logged and scored like any other model.
- **A-中:** 作为现有搜索旁边的预算分配器;批评者角色检查推导;决策留痕、像模型一样被评分。

**L4. Q: What would you change in the architecture? / 架构上会改什么?**
- **A-EN:** Add an allocation layer that chooses between mission types and plain GP per round based on measured yield, and make
  the critic a separate, cheap, always-on check rather than a gate.
- **A-中:** 加一个按实际产出在任务类型与普通 GP 之间分配的层;批评者做成常开的便宜检查而不是闸门。

**L5. Q: What would you do differently from the start? / 从头再来会怎么做?**
- **A-EN:** Fix and stress-test the yardstick first, with planted signals and known leaks, before any agent experiment; reserve
  a truly untouched final test period; and budget for 16+ seeds from the start.
- **A-中:** 先用植入信号和已知漏洞把尺子压测好;留一段真正不碰的最终测试期;一开始就按 16+ 种子做预算。

**L6. Q: How do you decide when an agent design has failed? / 怎么判断一个 agent 设计失败了?**
- **A-EN:** By the pre-registered verdict. "Cannot tell" is treated as no evidence of value; the next design must change
  something specific that the previous result points to.
- **A-中:** 按事先约定的判定;「分不出」当作没有价值的证据;下一版必须针对上一个结果改具体的东西。

**L7. Q: What generalises beyond A-shares? / 哪些能推广到 A 股以外?**
- **A-EN:** The protocol (matched GP baseline, paired seeds, once-read test), the yardstick design (rank first, non-linear
  neutralisation), and the role split (LLM as critic and allocator, not generator or gatekeeper).
- **A-中:** 评估流程、尺子设计、角色分工。

**L8. Q: What did you learn about yourself as a researcher? / 你作为研究者学到了什么?**
- **A-EN:** To write the verdict rule before the run and to report the failures with the same care as the success; most of the
  value came from turning each failure into one specific design change.
- **A-中:** 先写判定规则再跑;失败与成功同样认真报告;价值大多来自把每次失败变成一个具体的设计改动。

---

## M. 背景:AlphaCube 自身和其他 Partura 研究 / Context

**M1. Q: How good is AlphaCube on its own? / AlphaCube 自己表现如何?**
- **A-EN:** Its two-level champions (fusing ~100 factor families) reached a test long-short Sharpe of about 4.9 and a long-only
  net excess of about +17% a year with excess Sharpe ~2.1–2.2 over 2023-08 to 2025-12, under the old (pre-C07) yardstick. On
  2026 forward data they held at about +16.6–16.9% excess. These are AlphaCube's own results, separate from the Partura question.
- **A-中:** 两层合成冠军测试段多空夏普约 4.9、纯多头净超额约 +17%/年(超额夏普约 2.1–2.2,旧尺子);2026 前推约 +16.6%–16.9%。
  与 Partura 问题是两回事。

**M2. Q: Then why is C08's absolute Sharpe near zero? / 那为什么 C08 的绝对夏普接近 0?**
- **A-EN:** Different object and yardstick. The champions fuse thousands of factors and are not residualised on non-linear
  controls; C08 books are small libraries per seed, residualised on five controls with squares and cubes. The C-series measures
  the marginal value of the agent, not the best achievable book.
- **A-中:** 对象和尺子不同:冠军融合上千因子、没做非线性中性化;C08 是每个种子的小库、做了严格残差。C 系列测的是 agent 的边际价值。

**M3. Q: What about risk control? / 风险控制做过吗?**
- **A-EN:** Yes, separately: none of the methods significantly improved out-of-sample Sharpe; the book's beta to the
  equal-weight market was 1.09. A market-trend half-position rule cut max drawdown from −37% to −21% at a cost of 5–9 points
  a year — insurance, not alpha.
- **A-中:** 单独做过:没有方法显著提高样本外夏普;组合对等权市场 beta 1.09;趋势半仓把回撤从 −37% 降到 −21%,年化少 5–9 个点。

**M4. Q: Any standalone findings from Partura's other studies? / Partura 其他研究有什么独立发现?**
- **A-EN:** In the daily-fields study (K002): known families out of sample were largely size; within a size bucket, a
  "typicality" signal reached +12.6% / Sharpe 2.06; and excluding stocks that hit limit-up in the last 10 days improved the known
  family by +1.2 points with t = 4.4 — the first rule-read result with t ≥ 2.
- **A-中:** K002:已知族样本外基本是市值;同市值档内的「典型性」+12.6% / 2.06;剔除近 10 日涨停过的股票对已知族 +1.2 个点、t 4.4。

**M5. Q: What is "reverse guidance"? / 「反向指引」是什么?**
- **A-EN:** Turning research conclusions into interventions on the search — reward, evaluation, priors, short searches — and
  testing them against a same-budget control. C01's guidance files were the first version; C05 onward replaced them with missions.
- **A-中:** 把结论编成对搜索的干预(奖励、评估、先验、短搜)并和同预算对照比;C01 是第一版,C05 起改为任务。

**M6. Q: Where is everything? / 东西都在哪?**
- **A-EN:** `research/coldstart_C0x/` (PLAN, RESULT, per-seed files), `scripts/c0x_*.py`, `workflows/c06_round.js`, and the
  AlphaCube steering branch for the engine.
- **A-中:** 如左。

---

## N. 尖锐追问 / Hard questions

**N1. Q: Seven failures and one win at p 0.012 — isn't that what chance predicts? / 七败一胜、p 0.012,不就是运气吗?**
- **A-EN:** It could be. Across eight designs, one nominal p of 0.012 is not strong evidence on its own. What makes it more than
  a lottery ticket is that C08 was designed by fixing specific failures, the forward period agrees, and the mechanism is
  plausible. Still, I call it a development result until fresh data.
- **A-中:** 可能。八次里出一个 0.012 本身不强;让它不只是彩票的是:C08 是逐个修失败得来的、前推一致、机制合理。仍只称开发期结果。

**N2. Q: You picked the signal card example after seeing results. / 信号卡是看完结果挑的。**
- **A-EN:** Yes, and the page says so. It illustrates the format and the "GP changed the thesis" point, not performance. The
  representative number is the median single head, +0.07.
- **A-中:** 是,页面已注明;它用来说明格式和「GP 改了论点」,代表性数字是中位 +0.07。

**N3. Q: Isn't P just "fewer, better-chosen heads" — a filter? / P 不就是一个过滤器吗?**
- **A-EN:** P adds heads rather than filtering — its library is M plus its own missions' heads, 65 in total vs A's 67. The
  difference is what the extra heads are. A same-count random control would quantify how much is book size.
- **A-中:** P 是加 head 不是筛;总数 65 对 67;差在加了什么;同数随机对照可以量化。

**N4. Q: A's extra GP hurt the book — maybe your A is just badly configured? / A 的额外 GP 拖累组合,是不是 A 配置不好?**
- **A-EN:** A uses the same engine, ban and yardstick as M, reused unchanged from C07 where it was pre-registered. That more GP
  heads hurt an equal-weight book is itself a finding about fusion; a stronger A (e.g. fused with weights) would be a fair
  extension, applied to P too.
- **A-中:** A 与 M 同引擎同规则,复用 C07 事先约定的;额外 head 拖累等权组合本身是关于融合的发现;更强的融合应对 P 同样适用。

**N5. Q: Why not compare against RL or a random-search baseline? / 为什么不和 RL 或随机搜索比?**
- **A-EN:** GP was the strongest searcher in my earlier AlphaCube work, so it is the hardest fair baseline; random search would
  be weaker. RL could be added but would not change the question.
- **A-中:** GP 是之前最强的,作基线最难;随机搜索更弱;RL 可加但不改问题。

**N6. Q: If P vs M isn't significant, why should a desk care? / P 对 M 不显著,团队为什么要在意?**
- **A-EN:** Because desks do spend extra compute, and the evidence says naive extra GP is flat or harmful while Partura-directed
  extra compute helped. The decision is how to spend the next unit of compute, and that is where it helped.
- **A-中:** 团队确实会花额外算力;证据是多跑 GP 持平或有害,而 Partura 引导的额外算力有帮助;决策正是下一份算力怎么花。

**N7. Q: The LLM's "beliefs" — are they real or post-hoc stories? / LLM 的「信念」是真的还是事后故事?**
- **A-EN:** They are written before the run as testable claims (the E core is the source; this mechanism predicts this sign),
  and GP results test them. Many were wrong — e.g. GP reversed C04's sign, and the volume-centroid family failed out of sample.
  Stories that GP overturns are discarded.
- **A-中:** 运行前写成可检验的主张,由 GP 结果检验;很多是错的(C04 方向被反转、重心族样本外失败);被推翻的就作废。

**N8. Q: Why should I believe the auditor didn't leak test information? / 怎么保证审计员没泄露测试信息?**
- **A-EN:** It never had access: inputs are files restricted to train/valid, and sessions are audited for reads outside the
  allowed set; C07's isolation audit had zero hits.
- **A-中:** 输入只有 train / valid 的文件;会话事后审计;C07 隔离审计零命中。

**N9. Q: How sensitive is the verdict to the re-neutralisation choice? / 判定对再中性化敏感吗?**
- **A-EN:** The un-neutralised fusion is a pre-registered secondary output; I report the primary only. The rule was set for all
  arms before C08 ran.
- **A-中:** 不中性化版本是事先约定的次要输出;主判定只用主口径;规则在 C08 前对所有组固定。

**N10. Q: 802 lost — why? / 802 为什么输?**
- **A-EN:** P's book was −0.03 vs A's +0.09; 802 had the largest M library (10 heads) and P added 7 more, so there was less room
  to help and more to dilute. One seed; I would not read much into it.
- **A-中:** P −0.03 对 A +0.09;802 的 M 库最大(10 个),P 再加 7 个,帮助空间小、稀释风险大;单个种子不多解读。

**N11. Q: Your forward Sharpe for P is +0.46 — isn't that the real story? / 前推 P 是 +0.46,这不才是重点吗?**
- **A-EN:** It is consistent, but 0.67 years and previously read; I won't lead with it.
- **A-中:** 一致,但只有 0.67 年且被读过,不作为主结论。

**N12. Q: Is the LLM doing anything a simple rule couldn't? / LLM 做的事规则做不到吗?**
- **A-EN:** In C05 a rule-based arm (B0) with the same tools did better than the LLM. In C08 there was no rule-based arm, so
  this is open — a rule-based allocator under the fixed yardstick is a natural next control.
- **A-中:** C05 规则组 B0 比 LLM 好;C08 没有规则组,所以这是开放问题;下一步可加规则分配器对照。

**N13. Q: Why did you keep going after seven non-wins? / 七次没赢为什么还继续?**
- **A-EN:** Because each failure had a specific, diagnosable cause — a channel that could not carry beliefs, a leaky reward, a
  gate that blocked the wrong things — and each fix was testable. Had the failures been unexplained noise, I would have stopped.
- **A-中:** 每次失败都有具体可诊断的原因,修法可检验;如果是无法解释的噪声,我会停。

**N14. Q: What is the one thing you would not claim? / 你绝对不会主张的一件事?**
- **A-EN:** That an LLM can find alpha better than a good searcher. The evidence supports a narrower claim: under a fixed
  yardstick, letting it decide where extra search goes helped, on a development set.
- **A-中:** LLM 比好的搜索器更会找 alpha。证据只支持更窄的主张:修好尺子后,让它决定额外搜索往哪花有帮助(开发集上)。
