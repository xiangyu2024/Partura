# Speaker notes · 讲稿(中英对照)— `final.tex`, 14 main pages, ~20 min

Each page: target time, then the **English script** (what to say) and **中文** (same content, for preparation). Numbers on
the page are not repeated in full; say the bold ones. Backup pages are for Q&A only — see `QA.md`.

每页:目标时长,然后是**英文讲稿**(实际要说的话)和**中文**(同样的内容,用于准备)。页面上已有的数字不必全念,念加粗的即可。
备用页只在答问时用,见 `QA.md`。

---

## P1 · Title / 标题 (0:20)

**EN.** I'm going to talk about Partura, an LLM research team that steers a symbolic alpha miner. The short version of the
story: seven iterations, and one promising result — and I'll be precise about what "promising" means.

**中文.** 今天讲 Partura:一个 LLM 研究团队,去引导一个符号化的因子挖掘器。一句话概括:七次迭代,一个有希望的结果 ——
我会讲清楚「有希望」具体是什么意思。

---

## P2 · Finding an alpha is not evidence that the LLM helped / 找到 alpha 不等于 LLM 有用 (1:10)

**EN.** If you put an LLM into an alpha pipeline and the backtest is good, that only tells you something was found. It does
not tell you the LLM added anything — a genetic-programming searcher with the same data and the same compute might have found
the same thing or better. So every experiment here is a matched comparison: arm A gives the extra budget to plain GP; arm P
gives exactly the same extra budget to the LLM's missions. Same data, operators, engine, random seeds, and paid evaluations.
We compare the libraries out of sample, seed by seed. **The baseline is a capable searcher, not "no research".**

**中文.** 把 LLM 放进因子流程,回测好看,只说明「找到了东西」,不说明 LLM 有贡献 —— 同样数据、同样算力的遗传规划可能找得一样好
甚至更好。所以这里每个实验都是配对比较:A 组把额外预算给普通 GP;P 组把完全相同的额外预算交给 LLM 派的任务。数据、算子、
引擎、随机种子、付费评估次数都相同,逐种子比较样本外的因子库。**基线是一个能干的搜索器,不是「什么都不做」。**

---

## P3 · Search is cheap; belief is expensive / 搜索便宜,信念昂贵 (1:20)

**EN.** This is the first principle. A GP can score thousands of expressions for no tokens. If the LLM writes formulas one
prompt at a time, its cost grows with the number of candidates and it competes with GP at GP's own game. The design here pays
tokens once per round: the LLM reads what the search found, forms a belief about where the alpha comes from, and turns that
belief into a mission that redirects thousands of cheap evaluations. **Tokens should buy beliefs, not candidates.**

**中文.** 第一条原理。GP 可以零 token 打分成千上万个表达式。如果让 LLM 一条一条写公式,成本随候选数增长,而且是在 GP 擅长的事上
和 GP 竞争。这里的设计是每轮只花一次 token:LLM 读搜索的产出,形成「alpha 从哪里来」的信念,再把信念变成任务,去改变成千上万次
便宜评估的方向。**token 应该买信念,而不是买候选。**

---

## P4 · Two layers, two directions / 两层、双向、代码当裁判 (1:00)

**EN.** The feedback goes both ways. Partura, the belief layer, proposes where to look — E, R and N missions. AlphaCube, the
search layer, reports back heads, ablations and failures, and those revise the belief. Underneath both is a referee in code:
ranking, non-linear neutralisation, a residual long-only book with costs, paired seeds. **Neither side grades itself.**

**中文.** 反馈是双向的。Partura 是信念层,提出往哪里找 —— E、R、N 三类任务。AlphaCube 是搜索层,把找到的 head、拆解结果和失败
报回来,用来修正信念。两层下面是代码写的裁判:排序、非线性中性化、扣成本的残差纯多头书、配对种子。**谁都不给自己打分。**

---

## P5 · The task / 任务 (0:50)

**EN.** Concretely: the input is a cube of about 5,200 A-share stocks by days by 241 one-minute bars, eight minute fields plus
six daily fields. One expression collapses the minutes and gives one number per stock per day. The target is the next-day
return measured from the first-15-minute VWAP to the next first-15-minute VWAP, so the signal is tradable after the close.
The finished output is a signal card: thesis, expression, evidence, provenance.

**中文.** 具体地说:输入是一个立方体,约 5,200 只 A 股 × 交易日 × 241 根一分钟 bar,8 个分钟字段加 6 个日频字段。一个表达式把
分钟这一维压掉,每只股票每天给一个数。目标是次日收益:从第二天开盘前 15 分钟的 VWAP 买入,到再下一天同一窗口卖出,所以收盘后
算出的信号是能交易的。最终产物是一张信号卡:论点、表达式、证据、出处。

---

## P6 · The final design / 最终设计 (1:10)

**EN.** This is the design we ended with. The main AlphaCube, M, runs untouched — no agent can ban, reweight or edit it. A
locate tool in code reads M's output: the heads, which subtrees are common to good candidates, what an ablation removes.
Partura reads that, and spends only the extra budget on three mission types: E deepens a good core, R removes or swaps weak
parts, N tries a new mechanism. Each arm's library is M's heads plus its own, scored on the fixed yardstick.

**中文.** 这是最终的设计。主 AlphaCube(M)不受任何干扰 —— agent 不能禁止、重新加权或修改它。代码写的定位工具读 M 的产出:
有哪些 head、哪些子树在好候选里反复出现、拆掉一部分会掉多少。Partura 读这些,只花额外预算,派三类任务:E 深挖一个好的核心,
R 去掉或替换烂部件,N 试一个新机制。每组的因子库是 M 的 head 加上本组新增的,用修好的尺子打分。

---

## P7 · Why the final design looks like this / 为什么最终设计是这样 (1:00)

**EN.** Every piece of that design came from a failure. Eight pre-registered experiments, each a hypothesis about where the
LLM adds value. In the first four, the LLM steered GP directly inside a fixed budget — writing priors, designing the first
population, banning families. Twice worse, twice inconclusive. Every LLM mistake crowded out exploration. **So in C08 the
main search is never touched by an agent; the LLM only spends the extra budget.**

**中文.** 这个设计的每一块都来自一次失败。八个事先约定的实验,每个都是关于「LLM 在哪里有价值」的一个假设。前四次,LLM 在固定
预算里直接指挥 GP —— 写先验、设计初始种群、禁掉某些因子族。两次更差,两次分不出。LLM 的每个错误都挤掉了探索。**所以 C08 里
没有 agent 碰主搜索,LLM 只花额外预算。**

---

## P8 · Three failures that set C08's rules / 三次失败定下 C08 的规则 (2:00)

**EN.** Three more failures set the rest. C05: Partura's book led in selection, 1.52 against 0.94, and tied on test at 0.44 —
so we only trust paired, out-of-sample reads at equal compute.

C06 (about 25 seconds): *The Auditor caught a specific mathematical error: the PI treated minute VWAP as the minute closing
price. Correcting this invalidated the original mechanism. However, the Auditor's broader filtering decisions performed poorly
out of sample — the seeds it rejected did better than the ones it accepted. This is why C08 retained the Auditor for
mathematical consistency checks but removed its authority to judge predictive quality.*

C07: the yardstick itself leaked — a convex transform could rebuild volatility, and linear neutralisation left U- and S-shaped
exposure. We fixed it: rank first, then smooth, then neutralise on the controls and their squares and cubes. And when an LLM
only filtered GP's heads, the heads it kept did worse than the ones it dropped. So in C08 the LLM proposes; it does not filter.
**The LLM was a reliable critic but an unreliable gatekeeper.**

**中文.** 另外三次失败定下了其余规则。C05:Partura 的组合在选拔期领先(1.52 对 0.94),到测试段打平(都是 0.44)—— 所以只信
同算力下配对的样本外读数。

C06(约 25 秒):*审计员抓到了一个具体的数学错误:PI 把分钟 VWAP 当成了分钟收盘价。改正之后,原来的机制就不成立了。但审计员
更广泛的筛选判断在样本外表现很差 —— 它挡掉的种子比它放行的更好。所以 C08 保留审计员做数学一致性检查,但取消了它判断预测价值的
权力。*

C07:尺子本身有漏洞 —— 凸变换能把波动重新造出来,线性中性化去不掉 U 形和 S 形暴露。修法是先排序再平滑,再对控制变量及其平方、
三次方取残差。而让 LLM 只做筛选时,它留下的 head 比去掉的更差。所以 C08 里 LLM 负责提出,不负责筛选。**LLM 是可靠的批评者,
不是可靠的把关人。**

---

## P9 · One round, end to end / 完整的一轮 (1:20)

**EN.** Here is one real round, the last one we ran: seed 808, round 3. Input: the locate tool shows a subtree — the 20-day
average of where in the day a stock's volume trades — scoring 1.28 on its own and necessary inside an existing head. Decision:
the PI keeps it as an E core and grows new structure around it, and opens an N slot on the shape of the minute-volume
distribution. Audit: a correlation table in code, then the auditor scores and strikes; one seed is struck because it is
essentially the liquidity control. Output: GP runs 96 evaluations per slot; E found three heads, N found none. Every arrow is
a file on disk, so any round can be replayed.

**中文.** 这是真实的一轮,也是最后跑的一轮:种子 808,第 3 轮。输入:定位工具显示一个子树 —— 一只股票成交量在一天里的时间
重心,取 20 日均值 —— 单独就有 1.28 分,而且是一个现有 head 的必要部件。决策:PI 把它当 E 核心,在外面长新结构;另开一个 N 位,
看分钟成交量分布的形状。审计:先由代码算相关度表,再由审计员打分、划种子;有一个种子几乎就是流动性控制,被划掉。输出:GP 每个
任务位 96 次评估;E 找到 3 个 head,N 没有。每个箭头都是磁盘上的一个文件,任何一轮都能重放。

---

## P10 · Same extra budget, rules fixed before the run / 同样的额外预算,规则事先定死 (1:00)

**EN.** The budget is matched. Plain GP used 4,438 scored evaluations, Partura 4,525, about two percent more — and Partura
actually used less GPU time. The yardstick and the verdict were committed before any C08 run: P against A, fused-book test
Sharpe, 8 paired seeds, one-sided Wilcoxon at 5 percent. Test segment 2023-08 to 2025-12, read once; forward 2026 is
reported, not judged.

**中文.** 预算是匹配的。普通 GP 用了 4,438 次评估,Partura 用了 4,525 次,多 2% 左右 —— GPU 时间反而少。尺子和判定规则在 C08
任何运行之前就提交了:P 对 A,融合书的测试段夏普,8 对种子,单侧 Wilcoxon,显著性 5%。测试段 2023-08 到 2025-12 只读一次;
2026 年的前推段只报不判。

---

## P11 · Result / 结果 (1:30)

**EN.** And this is the result. Partura's missions beat the same extra budget spent on plain GP in **7 of 8 seeds**. **Median
paired difference +0.23, one-sided p = 0.012.** The mean fused book goes from −0.33 to +0.16. The 2026 forward period points the
same way, 7 of 8. Look at the bars: the big gaps are seeds where plain GP's book fell to −1, and Partura's stayed near zero
or above.

**中文.** 这是结果。在 **8 个种子里有 7 个**,Partura 的任务胜过把同样额外预算花在普通 GP 上。**配对差的中位数 +0.23,单侧
p = 0.012。** 融合书的均值从 −0.33 到 +0.16。2026 前推段方向相同,8 个里也赢了 7 个。看柱子:大的差距出现在普通 GP 的组合跌到 −1 左右、
而 Partura 的停在 0 附近或以上的种子。

---

## P12 · Three comparisons / 三个层次的比较 (2:00)

**EN.** There are three comparisons, and they matter. P against A is significant. P against M — Partura against no extra search
at all — is positive, +0.24, but not significant. And A against M is flat: extra plain GP did not help on average. So what C08
shows is that **the extra budget did better in Partura's hands than in GP's** — not that Partura beats the base search. Seed by
seed: where GP's extra search found nothing new, 804 and 805, Partura's missions added heads that held. Where GP's extra heads
dragged the book down, 803, 806, 807, Partura's hurt less or helped. Its median book is only +0.05. **So the value is allocation
of extra search, not a high-Sharpe factor** — which is exactly what "search is cheap, belief is expensive" predicts.

**中文.** 有三个比较,而且都重要。P 对 A 显著。P 对 M —— Partura 对比完全不加额外搜索 —— 为正(+0.24),但不显著。A 对 M 持平:
平均来说,多跑普通 GP 没有帮助。所以 C08 说明的是**额外预算交给 Partura 比交给 GP 好**,不是 Partura 胜过基础搜索。逐种子看:
普通 GP 的额外搜索什么也没加的种子(804、805),Partura 的任务加进了站得住的 head;普通 GP 的额外 head 拖累组合的种子(803、806、
807),Partura 的拖累更小或反而有帮助。它的组合中位数只有 +0.05。**所以价值在于额外搜索怎么分配,而不是找到高夏普的因子** ——
这正是「搜索便宜、信念昂贵」所预测的。

---

## P13 · How to read p = 0.012 / 怎么理解 p = 0.012 (1:30)

**EN.** Now the honest part. 0.012 is the correct nominal value for this study's pre-specified test. But the same test segment
had been read seven times before, and those results shaped C08's design. With eight pairs, seven wins gives anything from 0.008
to 0.098 depending on how big the one loss is. And the forward period agrees but is short and had been read before. So:
*C08 is the first design that produced a statistically significant paired improvement under its pre-specified within-study
test. However, because earlier designs repeatedly used the same test period, I treat this as a promising development result
rather than independent confirmation.* What would confirm it: freeze C08 and read once on data after September 16, 2026; a
random filter with the same head count; new seeds; and GPU plus tokens on one ledger.

**中文.** 下面是诚实的部分。0.012 是这个研究事先约定的检验的正确名义值。但同一个测试段此前被读过七次,那些结果影响了 C08 的
设计。8 对里赢 7 对,按那一对输的大小,p 可以在 0.008 到 0.098 之间。前推段方向一致,但很短,也被读过。所以:*C08 是第一个在
事先约定的研究内检验下得到显著配对改进的设计。但因为之前的设计反复使用了同一个测试期,我把它当作有希望的开发期结果,而不是
独立确认。* 什么能确认它:冻结 C08,在 2026-09-16 之后的数据上读一次;同样 head 数的随机筛选作对照;新种子;GPU 与 token 记在
同一本账上。

---

## P14 · What the evidence supports / 结论 (1:00)

**EN.** Five takeaways. One: search is cheap, belief is expensive — and Partura's value showed up exactly there, in deciding
where extra search goes. Two: keep the LLM out of the main search. Three: fix the referee before judging the agent. Four: use
the LLM as a critic, not a gatekeeper. Five: after seven iterations, one promising result; fresh data decides. Thank you.

**中文.** 五条结论。一,搜索便宜、信念昂贵 —— Partura 的价值正好出现在这里:决定额外搜索往哪花。二,不让 LLM 进主搜索。
三,先修好裁判,再评判 agent。四,把 LLM 当批评者,不当把关人。五,七次迭代之后,一个有希望的结果;新数据说了算。谢谢。

---

## Timing check / 时间核对

0:20 + 1:10 + 1:20 + 1:00 + 0:50 + 1:10 + 1:00 + 2:00 + 1:20 + 1:00 + 1:30 + 2:00 + 1:30 + 1:00 = **17:10**, leaving ~3 min
slack for transitions or one question mid-talk. If running long, shorten P5 and P9 (say only Input → Output).

合计约 17 分 10 秒,留约 3 分钟余量。超时就压缩 P5 和 P9(P9 只讲输入和输出)。
