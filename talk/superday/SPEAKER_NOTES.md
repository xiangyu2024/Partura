# Speaker notes · 讲稿(中英对照)— `final.tex`, 13 main pages, ~16.5 min

Each page: target time, what is on the slide, then the **English script** (what to say) and **中文** (same content, for
preparation). The figures carry only short labels; the explanation is in the script. Backup pages are for Q&A only — see
`QA.md`.

每页:目标时长、页面上有什么,然后是**英文讲稿**(实际要说的话)和**中文**(同样的内容,用于准备)。图里只放短标签,解释都在讲稿里。
备用页只在答问时用,见 `QA.md`。

---

## P1 · Title / 标题 (0:20)

**EN.** I'm going to talk about Partura, an LLM research team that steers a symbolic alpha miner. The short version: seven
iterations, one promising result — and I'll be precise about what "promising" means.

**中文.** 今天讲 Partura:一个 LLM 研究团队,去引导一个符号化的因子挖掘器。一句话:七次迭代,一个有希望的结果 —— 我会讲清楚
「有希望」具体指什么。

---

## P2 · Finding an alpha is not evidence that the LLM helped / 找到 alpha 不等于 LLM 有用 (1:10)

*On the slide:* M (main search) feeds both libraries; the extra budget goes either to A (plain GP) or to P (Partura);
the verdict is P − A per seed. One line: what is held equal.

*页面上:* M 同时进入两个库;额外预算要么给 A(普通 GP),要么给 P(Partura);判定是逐种子的 P − A;一行写明哪些保持相同。

**EN.** If you put an LLM into an alpha pipeline and the backtest is good, that only tells you something was found — not
that the LLM added anything. So every experiment is built like this. On the left, the main search M; its results go into
both libraries. Then the same extra budget goes one of two ways: to more plain GP, arm A, or to Partura's missions, arm P.
Each library is M's heads plus that arm's heads, and the verdict is the test Sharpe difference P minus A, seed by seed.
Data, operators, engine, random seeds and paid evaluations are held equal. **The baseline is a capable searcher, not
"no research".**

**中文.** 把 LLM 放进因子流程、回测好看,只说明找到了东西,不说明 LLM 有贡献。所以每个实验都这样搭:左边是主搜索 M,它的结果
同时进入两个库;同样的额外预算有两种花法 —— 给更多普通 GP(A 组),或给 Partura 的任务(P 组)。每个库 = M 的 head + 本组的
head,判定看逐种子的测试段夏普差 P − A。数据、算子、引擎、随机种子、付费评估次数都相同。**基线是能干的搜索器,不是「不做研究」。**

---

## P3 · Search is cheap; belief is expensive / 搜索便宜,信念昂贵 (1:40)

*On the slide:* the two-speed ring. Outer ring = one round: read M and locate → form beliefs → write missions → audit →
run missions → add to library. Inner ring = GP evaluations, 0 tokens. Two directions labelled. Right: tokens only on the
outer ring's LLM steps.

*页面上:* 两种速度的环。外环一圈 = 一轮:读 M 与定位 → 形成信念 → 写任务 → 审核 → 跑任务 → 加入因子库;内环 = GP 评估,0 token;
标出两个方向;右侧:token 只花在外环的 LLM 步骤上。

**EN.** This is the first principle, in one picture. The inner ring is GP: every tick is one evaluated expression, at zero
tokens — that is the cheap part. The outer ring is one research round, and it is the only place tokens are spent. Code reads
M's output and locates what works. The LLM forms a belief about where the alpha comes from, writes missions, and an auditor
checks them. Then GP runs the missions at zero tokens and the heads go into the library. So the loop goes both ways:
**belief → search** through the missions, **search → belief** through heads, ablations and failures. And every score along
the way is computed in code; no role grades its own work. **Tokens should buy beliefs that redirect thousands of cheap
evaluations — not candidates.**

**中文.** 第一条原理,用一张图说明。内环是 GP:每一格是一次表达式评估,零 token —— 这是便宜的部分。外环是一轮研究,也是唯一花
token 的地方:代码读 M 的产出、定位哪些结构有效;LLM 形成「alpha 从哪来」的信念、写任务,审计员检查;然后 GP 零 token 跑任务,
head 进入因子库。所以循环是双向的:**信念 → 搜索**靠任务,**搜索 → 信念**靠 head、拆解和失败。一路上所有分数都由代码计算,
没有哪个角色给自己打分。**token 应该买能改变成千上万次便宜评估方向的信念,而不是买候选。**

---

## P4 · The task / 任务 (0:50)

*On the slide:* the (stock, day, minute) cube → expression x → daily signal → signal card; signal and target formulas.

*页面上:* (股票, 日, 分钟) 立方体 → 表达式 x → 日频信号 → 信号卡;信号与目标公式。

**EN.** Concretely: about 5,200 A-share stocks, 241 one-minute bars a day, eight minute fields plus six daily fields. One
expression collapses the minutes into one number per stock per day. The target is next-day return from the first 15-minute
VWAP to the next one, so a signal computed after the close is tradable. The finished product is a signal card: thesis,
expression, evidence and provenance.

**中文.** 具体地说:约 5,200 只 A 股,每天 241 根一分钟 bar,8 个分钟字段加 6 个日频字段。一个表达式把分钟压掉,每只股票每天一个数。
目标是次日收益,从开盘前 15 分钟 VWAP 到下一天同一窗口,所以收盘后算出的信号能交易。最终产物是信号卡:论点、表达式、证据、出处。

---

## P5 · The final design / 最终设计 (1:10)

*On the slide:* Main AlphaCube (M, untouched) → locate tool (code) → Partura (PI, auditor, checker) → E / R / N;
library per arm = M's heads + mission heads, scored on the fixed yardstick.

*页面上:* 主 AlphaCube(M,不受干扰)→ 定位工具(代码)→ Partura(PI、审计员、检查)→ E / R / N;每组因子库 = M 的 head + 任务的
head,用修好的尺子打分。

**EN.** This is where we ended up. The main AlphaCube, M, is untouched — no agent can ban, reweight or edit it. A locate tool,
pure code, reads M's output: the heads, which subtrees are common to good candidates, what an ablation removes. Partura —
the PI, an auditor and a checker; in round one also an anatomist and a librarian — spends only the extra budget, through
three mission types. E deepens a good core. R swaps out a weak part. N tries a new mechanism. GP runs the missions, and each
arm's library is M's heads plus its own mission heads, scored on the fixed yardstick.

**中文.** 这是最终的设计。主 AlphaCube(M)不受干扰 —— 任何 agent 都不能禁止、重新加权或修改它。定位工具是纯代码,读 M 的产出:
有哪些 head、哪些子树在好候选里反复出现、拆掉某一部分会掉多少。Partura(PI、审计员、检查;第 1 轮另有解剖员和文献员)只花额外
预算,派三类任务:E 深挖一个好核心,R 换掉烂部件,N 试新机制。GP 跑任务;每组因子库 = M 的 head + 本组任务的 head,用修好的尺子打分。

---

## P6 · Why the final design looks like this / 为什么最终设计是这样 (1:00)

*On the slide:* eight boxes C01–C08, each with the idea in a few words and the verdict underneath; three phases above.

*页面上:* C01–C08 八个方框,每个写几个词的设计思路,下面是判定;上方三个阶段。

**EN.** Every piece of that design came from a failure. Eight pre-registered experiments, each a hypothesis about where the
LLM adds value, in three phases: where should the agent act, which beliefs deserve compute, and is the yardstick right. In
the first four, the LLM steered GP directly inside a fixed budget — writing priors, seeding GP, banning families: twice
worse, twice inconclusive. Every LLM mistake crowded out exploration. **So in C08, no agent touches M.**

**中文.** 这个设计的每一块都来自一次失败。八个事先约定的实验,每个都是关于「LLM 在哪有价值」的一个假设,分三个阶段:agent 该在
哪里起作用、哪些信念值得给算力、尺子对不对。前四次,LLM 在固定预算内直接指挥 GP —— 写先验、设计种子、禁掉因子族:两次更差、两次
分不出。LLM 的每个错误都挤掉了探索。**所以 C08 里没有 agent 碰 M。**

---

## P7 · Three failures that set C08's rules / 三次失败定下 C08 的规则 (2:00)

*On the slide:* three rows — C05, C06, C07 — each: what we saw → why → rule in C08.

*页面上:* 三行(C05、C06、C07),每行:看到了什么 → 为什么 → C08 的规则。

**EN.** Three more failures set the rest; read each row left to right.

C05: Partura's book led in selection, 1.52 against 0.94, and tied on test at 0.44. The LLM had fitted a leaky reward. Rule:
only paired seeds, one read, same compute.

C06 (about 25 seconds): *The Auditor caught a specific mathematical error: the PI treated minute VWAP as the minute closing
price. Correcting this invalidated the original mechanism. However, the Auditor's broader filtering decisions performed
poorly out of sample — the seeds it rejected did better than the ones it accepted. This is why C08 retained the Auditor for
mathematical consistency checks but removed its authority to judge predictive quality.*

C07: the yardstick itself leaked — a convex transform could rebuild volatility, and linear neutralisation left U- and
S-shaped exposure. And when an LLM only filtered GP's heads, the ones it kept did worse than the ones it dropped. Rule: rank
first, neutralise the controls with their squares and cubes, and let the LLM propose rather than filter. **A reliable critic,
an unreliable gatekeeper.**

**中文.** 另外三次失败定下了其余规则,每行从左往右读。

C05:Partura 的组合在选拔期领先(1.52 对 0.94),测试段打平(都是 0.44);原因是 LLM 拟合了一个有漏洞的奖励。规则:只信同算力、
配对种子、只读一次的检验。

C06(约 25 秒):*审计员抓到了一个具体的数学错误:PI 把分钟 VWAP 当成了分钟收盘价。改正之后,原来的机制就不成立了。但审计员更
广泛的筛选判断在样本外表现很差 —— 它挡掉的种子比放行的更好。所以 C08 保留审计员做数学一致性检查,但取消了它判断预测价值的权力。*

C07:尺子本身有漏洞 —— 凸变换能重造波动,线性中性化去不掉 U 形、S 形暴露;而让 LLM 只筛 GP 的 head 时,它留下的比去掉的差。
规则:先排序,对控制变量及其平方、三次方中性化,让 LLM 提出而不是筛选。**可靠的批评者,不可靠的把关人。**

---

## P8 · One round, end to end / 完整的一轮 (1:20)

*On the slide:* Input → Decision → Audit → Output, and under each stage the real example from seed 808, round 3.

*页面上:* 输入 → 决策 → 审计 → 输出,每一步下面是种子 808 第 3 轮的真实例子。

**EN.** Here is one real round, the last one we ran: seed 808, round 3. Input: the locate tool finds a subtree about volume
timing — where in the day a stock's volume trades — that scores 1.28 on its own. Decision: the PI writes two slots: E grows
new structure around that core, N tries the shape of the minute-volume distribution. Audit: a correlation table in code, then
the auditor; 11 of 12 and 10 of 12 seeds survive — one was essentially the liquidity control. Output: GP runs 96 evaluations
per slot; E found three heads, two of them positive on test. **Every arrow is a file on disk, so any round can be replayed.**

**中文.** 这是真实的一轮,也是最后跑的一轮:种子 808,第 3 轮。输入:定位工具发现一个关于成交时点的子树(股票的成交量集中在一天
里的什么时候),单独就有 1.28 分。决策:PI 写两个任务位 —— E 围绕这个核心长新结构,N 试分钟成交量分布的形状。审计:先由代码算
相关度表,再由审计员审;种子分别留下 11/12 和 10/12(有一个几乎就是流动性控制)。输出:GP 每个任务位 96 次评估,E 找到 3 个 head,
其中 2 个测试段为正。**每个箭头都是磁盘上的一个文件,任何一轮都能重放。**

---

## P9 · Same extra budget, rules fixed before the run / 同样的额外预算,规则事先定死 (1:00)

*On the slide:* bars of scored evaluations — M 4,272 (shared), A 4,438, P 4,525 — with GPU seconds; three rules.

*页面上:* 评估次数的柱子(M 4,272 共用、A 4,438、P 4,525)和 GPU 秒数;三条规则。

**EN.** The budget is matched: plain GP used 4,438 scored evaluations, Partura 4,525, about two percent more — and Partura
used less GPU time. The yardstick and the verdict were committed before any C08 run: P against A, eight paired seeds,
one-sided Wilcoxon at five percent. The test segment, August 2023 to December 2025, is read once; 2026 is reported, not
judged.

**中文.** 预算是匹配的:普通 GP 用了 4,438 次评估,Partura 4,525 次,多约 2%,GPU 时间反而更少。尺子和判定规则在 C08 任何运行
之前提交:P 对 A,8 对种子,单侧 Wilcoxon,显著性 5%。测试段(2023-08 到 2025-12)只读一次;2026 年只报不判。

---

## P10 · Result / 结果 (1:30)

*On the slide:* three headline numbers; per-seed bars, A outlined and P tinted, with P − A under each seed.

*页面上:* 三个主数字;逐种子柱状图(A 空心、P 浅蓝),每个种子下面写 P − A。

**EN.** And this is the result. Partura's missions beat the same extra budget spent on plain GP in **seven of eight seeds**:
**median paired difference +0.23, one-sided p = 0.012**. The mean fused book goes from −0.33 to +0.16, and the 2026 forward
period points the same way, seven of eight. Look at where the gaps are: the big ones are seeds where plain GP's book fell to
about −1, while Partura's stayed near zero or above.

**中文.** 这是结果。在**8 个种子里有 7 个**,Partura 的任务胜过把同样额外预算花在普通 GP 上:**配对差中位数 +0.23,单侧 p =
0.012**。融合书均值从 −0.33 到 +0.16;2026 前推段方向相同,8 个里赢 7 个。看差距在哪:大的差距出现在普通 GP 的组合跌到 −1 左右、
而 Partura 停在 0 附近或以上的种子。

---

## P11 · Three comparisons / 三个层次的比较 (2:00)

*On the slide:* a triangle M, A, P with the three comparisons on its edges; right: the two seed-level patterns.

*页面上:* M、A、P 三角形,三条边是三个比较;右侧是逐种子的两种情形。

**EN.** There are three comparisons, one per edge. A against P: +0.23, seven of eight, significant. M to P — Partura against
no extra search at all — +0.24, but not significant. M to A: flat; more plain GP did not help on average. So what C08 shows
is that **the extra budget did better in Partura's hands than in GP's** — not that Partura beats the base search. On the
right, seed by seed: where extra GP found nothing new, 804 and 805, Partura's heads held up; where GP's extra heads dragged
the book down, 803, 806 and 807, Partura's hurt less. Its median book is only +0.05. **The value is in where the extra
search goes, not in a high-Sharpe factor** — which is exactly what "search is cheap, belief is expensive" predicts.

**中文.** 三个比较,一条边一个。A 到 P:+0.23,8 个里赢 7 个,显著。M 到 P(Partura 对比完全不加额外搜索):+0.24,但不显著。
M 到 A:持平,多跑普通 GP 平均没有帮助。所以 C08 说明的是**额外预算交给 Partura 比交给 GP 好**,不是 Partura 胜过基础搜索。右边
逐种子看:额外 GP 什么也没加的种子(804、805),Partura 的 head 站住了;GP 的额外 head 拖累组合的种子(803、806、807),Partura
拖累更小。它的组合中位数只有 +0.05。**价值在额外搜索往哪去,而不在高夏普因子** —— 这正是「搜索便宜、信念昂贵」所预测的。

---

## P12 · How to read p = 0.012 / 怎么理解 p = 0.012 (1:30)

*On the slide:* the test segment with eight reads (C01–C08) and, dashed, fresh data after 2026-09-16; the statement; four
dashed boxes for the confirming tests.

*页面上:* 测试段被读了 8 次(C01–C08),虚线框是 2026-09-16 之后的新数据;统一口径的那句话;四个虚线框是能确认结果的检验。

**EN.** Now the honest part. Look at the timeline: the same test segment was read by every study, and C08's is the eighth
read — the earlier reads shaped its design. So: *C08 is the first design that produced a statistically significant paired
improvement under its pre-specified within-study test. However, because earlier designs repeatedly used the same test
period, I treat this as a promising development result rather than independent confirmation.* Four things would confirm it,
shown dashed because they are planned: one read on fresh data after September 2026, a random filter with the same number of
heads, new seeds with one fixed flow, and GPU and tokens on one ledger.

**中文.** 下面是诚实的部分。看时间线:同一个测试段被每个研究都读过,C08 是第 8 次,之前的读数影响了它的设计。所以:*C08 是第一个
在事先约定的研究内检验下得到显著配对改进的设计。但因为之前的设计反复使用了同一个测试期,我把它当作有希望的开发期结果,而不是
独立确认。* 有四件事能确认它(虚线表示还没做):在 2026 年 9 月之后的新数据上读一次;同样 head 数的随机筛选对照;固定流程的新种子;
GPU 和 token 记在同一本账上。

---

## P13 · What the evidence supports / 结论 (1:00)

**EN.** Five takeaways. Search is cheap, belief is expensive — and Partura helped exactly there, by choosing where extra
search goes. Keep the LLM out of the main search. Fix the referee before judging the agent. Use the LLM as a critic, not a
gatekeeper. And: seven iterations, one promising result — fresh data decides. Thank you.

**中文.** 五条结论。搜索便宜、信念昂贵 —— Partura 正是在这里起作用:决定额外搜索往哪去。不让 LLM 进主搜索。先修好裁判,再评判
agent。把 LLM 当批评者,不当把关人。七次迭代,一个有希望的结果 —— 新数据说了算。谢谢。

---

## Timing check / 时间核对

0:20 + 1:10 + 1:40 + 0:50 + 1:10 + 1:00 + 2:00 + 1:20 + 1:00 + 1:30 + 2:00 + 1:30 + 1:00 = **16:30**, leaving about 3.5
minutes for transitions or a question during the talk. If running long, shorten P4 (one sentence) and P8 (Input → Output only).

合计约 16 分 30 秒,留约 3.5 分钟余量。超时就压缩 P4(一句话带过)和 P8(只讲输入和输出)。

## Where things moved / 页面变动

The old "two layers, two directions" page is merged into P3 (the ring shows both directions); the cost-curve figure is now a
backup page, "tokens buy beliefs, not candidates".

原来的「两层、双向」一页并入 P3(环图同时表示两个方向);成本曲线图移到备用页「tokens buy beliefs, not candidates」。
