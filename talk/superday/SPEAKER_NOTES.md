# Speaker notes · 讲稿(中英对照)— `final.tex`, 13 main pages, ~16.5 min

Each page: target time, what is on the slide, then the **English script** (what to say) and **中文** (same content, for
preparation). The figures carry short labels; the explanation is in the script. Backup pages are for Q&A only — see
`QA.md`.

每页:目标时长、页面上有什么,然后是**英文讲稿**(实际要说的话)和**中文**(同样的内容,用于准备)。图里只放短标签,解释都在讲稿里。
备用页只在答问时用,见 `QA.md`。

---

## P1 · Title / 标题 (0:20)

**EN.** I'm going to talk about Partura, an LLM research team that steers a symbolic alpha miner. The short version: seven
iterations, and one promising result — and what it took to get there.

**中文.** 今天讲 Partura:一个 LLM 研究团队,去引导一个符号化的因子挖掘器。一句话:七次迭代,一个有希望的结果 —— 以及走到这一步
靠的是什么。

---

## P2 · Finding an alpha is not evidence that the LLM helped / 找到 alpha 不等于 LLM 有用 (1:10)

*On the slide:* M (main search) sends its heads into both libraries through two separate arrows; the extra budget goes either
to A (plain GP) or to P (Partura); the verdict is P − A per seed.

*页面上:* M 通过两条独立的箭头把 head 分别送进两个库;额外预算要么给 A(普通 GP),要么给 P(Partura);判定是逐种子的 P − A。

**EN.** If you put an LLM into an alpha pipeline and the backtest is good, that only tells you something was found — not that
the LLM added anything. So every experiment is built like this. The main search M runs once, and its heads go into both
libraries. Then the extra budget goes one of two ways: to more plain GP, arm A, or to Partura's missions, arm P. Each library
is M's heads plus that arm's heads, and the verdict is the test Sharpe difference, P minus A, seed by seed. Data, operators,
engine and seeds are the same; the GP budgets are comparable — 4,438 against 4,525 scored evaluations. **The baseline is a
capable searcher, not "no research".**

**中文.** 把 LLM 放进因子流程、回测好看,只说明找到了东西,不说明 LLM 有贡献。所以每个实验都这样搭:主搜索 M 只跑一次,它的 head
同时进入两个库;额外预算有两种花法 —— 给更多普通 GP(A 组),或给 Partura 的任务(P 组)。每个库 = M 的 head + 本组的 head,判定看
逐种子的测试段夏普差 P − A。数据、算子、引擎、种子相同;GP 预算可比(4,438 对 4,525 次评估)。**基线是能干的搜索器,不是「不做
研究」。**

---

## P3 · Search is cheap; belief is expensive / 搜索便宜,信念昂贵 (1:50)

*On the slide:* left, the two-speed ring — outer ring is one round (read M and locate → form beliefs → write missions →
audit → run missions → add to library), inner ring is GP at 0 LLM tokens, both directions labelled. Right, cumulative LLM
tokens: writing each formula grows with candidates; Partura grows with rounds (illustrative).

*页面上:* 左边是双速环 —— 外环一圈是一轮(读 M 与定位 → 形成信念 → 写任务 → 审计 → 跑任务 → 加入因子库),内环是 GP,0 个 LLM
token,标出两个方向;右边是累计 LLM token:逐个写公式随候选数增长,Partura 随轮数增长(示意)。

**EN.** This is the first principle, in one picture. The inner ring is GP: each tick is one evaluated expression, at zero LLM
tokens. "Cheap" means no LLM tokens — GP still costs GPU time, 24,000 to 26,000 GPU seconds per arm in C08. The outer ring is one
research round, and it is the only place tokens are spent: code reads M and locates what works; the LLM forms a belief, writes
missions, and an auditor checks them; GP runs them; the heads go into the library. So it goes both ways: belief to search
through the missions, search to belief through heads, ablations and failures. On the right is why this matters for cost: an
LLM that writes each formula pays per candidate; Partura pays per round. **One belief, many GP evaluations, evidence, and a
revised belief.**

**中文.** 第一条原理,用一张图说明。内环是 GP:每一格是一次表达式评估,0 个 LLM token。「便宜」指的是没有 LLM token —— GP 仍然
花 GPU 时间,C08 每组 24,000–26,000 GPU 秒。外环是一轮研究,也是唯一花 token 的地方:代码读 M、定位有效结构;LLM 形成信念、写任务,
审计员检查;GP 跑任务;head 进入因子库。所以是双向的:信念通过任务指导搜索,搜索通过 head、拆解和失败修正信念。右边说明为什么
省成本:逐个写公式的 LLM 按候选付费,Partura 按轮付费。**一个信念 → 大量 GP 评估 → 证据 → 修正后的信念。**

---

## P4 · The task / 任务 (0:50)

*On the slide:* the (stock, day, minute) cube → expression x → daily signal → signal card; signal and target formulas.

*页面上:* (股票, 日, 分钟) 立方体 → 表达式 x → 日频信号 → 信号卡;信号与目标公式。

**EN.** Concretely: about 5,200 A-share stocks, 241 one-minute bars a day, eight minute fields plus six daily fields. One
expression collapses the minutes into one number per stock per day. The target is next-day return from the first 15-minute
VWAP to the next one, so a signal computed after the close is tradable. The finished product is a signal card: thesis,
expression, evidence and provenance.

**中文.** 约 5,200 只 A 股,每天 241 根一分钟 bar,8 个分钟字段加 6 个日频字段。一个表达式把分钟压掉,每只股票每天一个数。目标是
次日收益,从开盘前 15 分钟 VWAP 到下一天同一窗口,所以收盘后算出的信号能交易。最终产物是信号卡:论点、表达式、证据、出处。

---

## P5 · The final design / 最终设计 (1:00)

*On the slide:* Main AlphaCube (M, untouched) → locate tool (code) → Partura (PI, auditor, checker; round 1 also anatomist and
librarian) → E / R / N; library per arm = M's heads + mission heads.

*页面上:* 主 AlphaCube(M,不受干扰)→ 定位工具(代码)→ Partura(PI、审计员、检查;第 1 轮另有解剖员、文献员)→ E / R / N;每组
因子库 = M 的 head + 任务的 head。

**EN.** This is where we ended up. The main AlphaCube, M, is untouched — no agent can ban, reweight or edit it. A locate tool in
code reads M's output. Partura spends only the extra budget, through three mission types: E deepens a good core, R swaps out a
weak part, N tries a new mechanism. GP runs the missions, and each library is M's heads plus that arm's mission heads, scored
on the fixed yardstick. Next page: who decides what.

**中文.** 这是最终的设计。主 AlphaCube(M)不受干扰 —— 任何 agent 都不能禁止、重新加权或修改它。代码写的定位工具读 M 的产出。
Partura 只花额外预算,派三类任务:E 深挖好核心,R 换掉烂部件,N 试新机制。GP 跑任务;每组因子库 = M 的 head + 本组任务的 head,
用修好的尺子打分。下一页讲谁决定什么。

---

## P6 · Who decides what / 谁决定什么 (1:20)

*On the slide:* six decisions, who makes each, what it adds and what it may not do.

*页面上:* 六个决策:谁来做、补充什么、不能做什么。

**EN.** Agents sit only where a decision needs judgement; everything measurable is code. Where is the structure? The locate
tool measures it; in round one an anatomist reads it. Which mechanism? The PI, with a librarian in round one, limited to papers
before August 2023 — the output is a falsifiable claim, not a formula. Where to search next? The PI writes the missions. Is the
plan broken? The auditor — it blocks maths errors and duplicates, and it is explicitly not allowed to predict returns. Is the
plan admissible? A checker runs code. And did it work? Code only; no agent scores its own work. In C08's later rounds we
dropped the anatomist and librarian to save cost. I don't claim that helped — round and flow changed together — but it shows
that **each role exists for one decision, and more agents is not better.**

**中文.** agent 只放在需要判断的决策点上,能测量的都交给代码。结构在哪?定位工具测量,第 1 轮由解剖员解读。什么机制?PI 负责,第
1 轮有文献员,只用 2023 年 8 月之前的论文 —— 产出是可证伪的主张,不是公式。下一步搜哪里?PI 写任务。计划有没有问题?审计员 ——
只挡数学错误和重复,明确不允许预测收益。计划是否合规?检查员跑代码。有没有效?只由代码判断,没有 agent 给自己打分。C08 后两轮为
省成本去掉了解剖员和文献员。我不声称这样更好 —— 轮次和流程同时变了 —— 但它说明**每个角色只为一个决策而存在,agent 不是越多越好。**

---

## P7 · Why the final design looks like this / 为什么最终设计是这样 (1:00)

*On the slide:* eight boxes C01–C08, the idea in a few words, the verdict underneath; three phases above.

*页面上:* C01–C08 八个方框,几个词的设计思路,下面是判定;上方三个阶段。

**EN.** Every piece of that design came from a failure. Eight pre-registered experiments, each a hypothesis about where the
LLM adds value, in three phases: where should the agent act, which beliefs deserve compute, and is the yardstick right. In
the first four, the LLM steered GP directly inside a fixed budget — writing priors, seeding GP, banning families: twice worse,
twice inconclusive. Its mistakes crowded out exploration. **So in C08, no agent touches M.**

**中文.** 这个设计的每一块都来自一次失败。八个事先约定的实验,每个都是关于「LLM 在哪有价值」的假设,分三个阶段:agent 该在哪起
作用、哪些信念值得给算力、尺子对不对。前四次,LLM 在固定预算内直接指挥 GP —— 写先验、设计种子、禁掉因子族:两次更差、两次分不出。
它的错误挤掉了探索。**所以 C08 里没有 agent 碰 M。**

---

## P8 · Three failures that set C08's rules / 三次失败定下 C08 的规则 (2:00)

*On the slide:* three rows — C05, C06, C07 — each: what we saw → diagnosis after the read → response in C08.

*页面上:* 三行(C05、C06、C07),每行:看到了什么 → 读后的诊断 → C08 的对应设计。

**EN.** Three more failures set the rest. The middle column is a diagnosis after the read, not an isolated test.

C05: Partura's book led in selection, 1.52 against 0.94, and tied on test at 0.44. The likely cause was a reward leak — a convex
transform could rebuild volatility. Response: rank first, then smooth, and judge on one ledgered read.

C06 (about 25 seconds): *The Auditor caught a specific mathematical error: the PI treated minute VWAP as the minute closing
price. Correcting this invalidated the original mechanism. However, the Auditor's broader filtering decisions performed poorly
out of sample — the seeds it rejected did better than the ones it accepted. This is why C08 retained the Auditor for
mathematical consistency checks but removed its authority to judge predictive quality.* Part of the reason, we think, is that
the yardstick paid for non-linear exposure to the controls — so C08 also neutralises their squares and cubes.

C07: with the yardstick fixed, an LLM that only filtered GP's heads kept ones that did worse than those it dropped; the book
improved mostly because it held fewer heads. Response: the LLM proposes; it does not filter.

**中文.** 另外三次失败定下了其余规则。中间一列是读数之后的诊断,不是隔离检验。

C05:Partura 的组合在选拔期领先(1.52 对 0.94),测试段打平(都是 0.44)。可能的原因是奖励漏洞 —— 凸变换能重新造出波动。对应:
先排序再平滑,只按一次记账的读数判。

C06(约 25 秒):*审计员抓到了一个具体的数学错误:PI 把分钟 VWAP 当成了分钟收盘价。改正之后,原来的机制就不成立了。但审计员更广泛
的筛选判断在样本外表现很差 —— 它挡掉的种子比放行的更好。所以 C08 保留审计员做数学一致性检查,但取消了它判断预测价值的权力。*
我们认为部分原因是尺子在为「对控制变量的非线性暴露」付钱 —— 所以 C08 也对控制变量的平方和三次方做中性化。

C07:修好尺子之后,只做筛选的 LLM 留下的 head 比去掉的差;组合变好主要因为 head 少了。对应:LLM 负责提出,不负责筛选。

---

## P9 · One round, end to end / 完整的一轮 (1:20)

*On the slide:* Input → Decision → Audit → Output, and under each stage the real example from seed 808, round 3.

*页面上:* 输入 → 决策 → 审计 → 输出,每一步下面是种子 808 第 3 轮的真实例子。

**EN.** One real round, the last one we ran: seed 808, round 3. Input: the locate tool finds a volume-timing subtree — where in
the day a stock's volume trades — that scores 1.28 on its own. Decision: the PI writes an E slot that grows new structure around
it, and an N slot on the shape of the minute-volume distribution. Audit: a correlation table in code, then the auditor; 11 of 12
and 10 of 12 seeds survive. Output: GP runs 96 evaluations per slot, and E found three heads. Their test values — +0.50, +0.39,
−0.43 — only exist because of the final read after all rounds; the agents never saw them. **Every arrow is a file on disk, so
any round can be replayed.**

**中文.** 真实的一轮,也是最后跑的一轮:种子 808,第 3 轮。输入:定位工具发现一个关于成交时点的子树(成交量集中在一天里什么时候),
单独 1.28 分。决策:PI 写一个 E 位围绕它长新结构,一个 N 位试分钟成交量分布的形状。审计:先代码算相关度表,再审计员审,种子留下
11/12 和 10/12。输出:GP 每个位 96 次评估,E 找到 3 个 head。它们的测试段数值(+0.50、+0.39、−0.43)是所有轮次结束后最终判读时才
算的,agent 从来没见过。**每个箭头都是磁盘上的文件,任何一轮都能重放。**

---

## P10 · Comparable extra budget, rules fixed before the run / 可比的额外预算,规则事先定死 (1:00)

*On the slide:* bars of scored evaluations — M 4,272 (shared), A 4,438, P 4,525 — and GPU seconds; three rules.

*页面上:* 评估次数柱状图(M 4,272 共用、A 4,438、P 4,525)和 GPU 秒数;三条规则。

**EN.** The budget is matched by design: each arm gets 256 evaluations per seed per round. A spends them as two GP runs of 128;
P as two missions of 96, up to 16 direct R evaluations and up to 48 for the locate tool. The scored counts differ by two
percent, and Partura used less GPU time. The yardstick and the comparison — P against A over eight paired seeds — were fixed
before any C08 run, and the test period is read once.

**中文.** 预算按设计匹配:每组每个种子每轮 256 次评估。A 花在两次 128 的 GP 上;P 花在两个 96 的任务、至多 16 次 R 直接评估和至多
48 次定位评估上。实际打分次数相差 2%,Partura 的 GPU 时间反而更少。尺子和比较方式(P 对 A,8 对种子)在 C08 任何运行之前就定好,
测试段只读一次。

---

## P11 · Result / 结果 (1:30)

*On the slide:* three numbers — 7 / 8 seeds, median paired Sharpe gain +0.23, mean fused-book Sharpe −0.33 → +0.16 — and the
per-seed bars (A outlined, P tinted). p and the forward period are in the footnote; do not read them out.

*页面上:* 三个数字 —— 8 个种子赢 7 个、配对夏普增益中位数 +0.23、融合书均值 −0.33 → +0.16 —— 以及逐种子柱状图(A 空心、P 浅蓝)。
p 值和前推段在脚注里,不用念。

**EN.** And this is the result, in three numbers. Partura's missions beat the same extra budget spent on plain GP in **seven of
eight seeds**. The **median paired gain is +0.23 Sharpe**. And the **mean fused book goes from −0.33 to +0.16**. Look at where
the gaps come from: the big ones are seeds where plain GP's book fell to about −1, while Partura's stayed near zero or above.
The 2026 forward period points the same way.

**中文.** 这是结果,三个数字。在**8 个种子里有 7 个**,Partura 的任务胜过把同样额外预算花在普通 GP 上;**配对夏普增益的中位数是
+0.23**;**融合书均值从 −0.33 到 +0.16**。看差距从哪来:大的差距出现在普通 GP 的组合跌到 −1 左右、而 Partura 停在 0 附近或以上的
种子。2026 年前推段方向相同。

---

## P12 · Where did the extra budget help? / 额外预算在哪里起了作用 (2:00)

*On the slide:* three rows — P − A, P − M, A − M — with the median, wins and losses, and what each says; the takeaway; one
line on the evidence status. p values are only in the footnote.

*页面上:* 三行(P − A、P − M、A − M):中位差、胜负、各自的含义;结论句;一行证据定位。p 值只在脚注里。

**EN.** Three benchmarks, one per row. **Against extra plain GP, Partura is ahead: +0.23, seven wins and one loss.** Against
no extra search at all, Partura is also positive, +0.24, but five wins and three losses — **the evidence there is still
insufficient.** And extra plain GP against no extra search: zero, no clear gain. So what C08 shows is that the extra budget did
better in Partura's hands than in GP's — not yet that Partura beats the base search. Seed by seed, where extra GP found nothing
new, Partura's heads held, and where GP's extra heads hurt the book, Partura's hurt less. **The observed edge is where extra
search went, not a high-Sharpe alpha.**

Then, briefly, and only here: **this is development evidence, not independent confirmation. The statistical evidence is
modest — eight seed pairs on one market history, and earlier iterations informed this design using the same test period.**

**中文.** 三个基准,一行一个。**对比额外的普通 GP,Partura 领先:+0.23,7 胜 1 负。** 对比完全不加额外搜索,Partura 也为正(+0.24),
但 5 胜 3 负 —— **这方面的证据还不足。** 额外普通 GP 对比不加:0,没有明确改善。所以 C08 说明的是额外预算交给 Partura 比交给 GP
好 —— 还不能说 Partura 胜过基础搜索。逐种子看:额外 GP 什么也没加的种子,Partura 的 head 站住了;GP 的额外 head 拖累组合的种子,
Partura 拖累更小。**观察到的优势在额外搜索去了哪里,而不是高夏普因子。**

然后,简短地、只在这里说一次:**这是开发期证据,不是独立确认。统计证据并不强 —— 只有一段市场历史上的 8 对种子,而且之前的迭代
用同一个测试期影响过这个设计。**

---

## P13 · What the evidence supports / 结论 (1:00)

*On the slide:* four takeaways; then, large, "Seven iterations, one promising result. Fresh data decides."; one line on the
next tests.

*页面上:* 四条结论;下面大字「七次迭代,一个有希望的结果。新数据说了算。」;一行下一步的检验。

**EN.** Four takeaways. Search is cheap and belief is expensive — in C08 the gain came from where extra search went, not from
one strong factor. Keep the LLM out of the main search. Fix the referee before judging the agent. And use the LLM as a critic:
it caught real errors, but it failed at predictive gatekeeping. Next comes one read on data after September 2026, a random
filter with the same number of heads, and new seeds. Seven iterations, one promising result. **Fresh data decides.** Thank you.

**中文.** 四条结论。搜索便宜、信念昂贵 —— C08 的收益来自额外搜索去了哪里,而不是某一个强因子。不让 LLM 进主搜索。先修好裁判,
再评判 agent。把 LLM 当批评者:它抓到了真实的错误,但在预测性把关上失败了。下一步是在 2026 年 9 月之后的数据上读一次、同样 head
数的随机筛选对照、新种子。七次迭代,一个有希望的结果。**新数据说了算。** 谢谢。

---

## Timing check / 时间核对

0:20 + 1:10 + 1:50 + 0:50 + 1:00 + 1:20 + 1:00 + 2:00 + 1:20 + 1:00 + 1:30 + 2:00 + 1:00 = **16:20**, leaving about
3.5 minutes. If running long, shorten P4 (one sentence), P7 (only the C01–C04 line) and P9 (Input → Output only).

合计约 16 分 20 秒,留约 3.5 分钟余量。超时就压缩 P4(一句话)、P7(只讲 C01–C04 那句)和 P9(只讲输入和输出)。

## If someone asks about the p-value / 被问到 p 值时

Go to the backup page "the test period was read eight times" and say: *C08 is the first design that produced a statistically
significant paired improvement under its pre-specified within-study test (one-sided p = 0.012). Because earlier designs
repeatedly used the same test period, I treat it as a promising development result rather than independent confirmation.*
Details in `QA.md` §H.

翻到备用页「the test period was read eight times」,说:*C08 是第一个在事先约定的研究内检验下得到显著配对改进的设计(单侧
p = 0.012)。但因为之前的设计反复使用了同一个测试期,我把它当作有希望的开发期结果,而不是独立确认。* 细节见 `QA.md` §H。

## What changed from the previous version / 与上一版相比

- The p-value page left the main deck (now the backup "the test period was read eight times"); its caveat is one line on P12,
  and its next steps are one line on P13.
- P11 leads with three numbers — 7 / 8 seeds, +0.23, −0.33 → +0.16; p and forward are in the footnote.
- P12 shows wins and losses, not p; P − M is "evidence still insufficient"; the bottom line states development evidence.
- P10's rule bullet no longer shows α; the test name is in the footnote.
- The script reads no p-value anywhere; the statistical caveat is said once, at the end of P12.

- p 值那一页移出主讲(现为备用页);它的局限说明变成 P12 的一行,下一步变成 P13 的一行。
- P11 先讲三个数字(8 个赢 7 个、+0.23、−0.33 → +0.16);p 值和前推段放进脚注。
- P12 只写胜负、不写 p;P − M 写「证据还不足」;底部一行写明是开发期证据。
- P10 的规则不再写 α,检验方法放进脚注。
- 讲稿全程不念 p 值;统计上的保留只在 P12 末尾说一次。
