# Partura 讲稿(13 页主讲,约 17 分钟)

**写法原则**
- 每页只讲一件事;第一句就是这页的结论,后面才解释。
- 屏幕上的数字不全念,只念最关键的一两个。
- 术语第一次出现时用大白话解释一次:head、book、yardstick。
- 页与页之间有过渡句(每页最后一句),听的人始终知道「我们在故事的哪一段」。
- 局限只讲两次:P8 讲诊断是事后推断,P12 讲开发期证据。讲清楚,但不反复道歉。

**故事线**:问题 → 怎么公平地测 → 设计原理 → 最终设计 → 这个设计是怎么从失败里来的 → 一轮真实的运行 → 结果 → 它到底说明了什么 → 结论。

---

## P1 · 标题(0:20)

**EN.** Hi, I'm Xiangyu. My topic is how to design an agentic AI alpha researcher. My answer is a system called Partura: a small team of LLM agents that steers a genetic-programming alpha miner. It took seven redesigns to get one result I think is promising. I'll show you the design, how each piece of it came out of a failure, and what the evidence does and doesn't support.

**中文.** 我讲的题目是怎么设计一个 agentic AI 因子研究员。我的方案叫 Partura:一个小型 LLM agent 团队,去引导一个遗传规划因子挖掘器。改了七次设计,才得到一个我认为有希望的结果。我会讲设计本身、每一块是怎么从失败里来的,以及证据能说明什么、不能说明什么。

---

## P2 · 找到 alpha 不等于 LLM 有用(1:15)

**EN.** First, the question has to be the right one. If I put an LLM into a pipeline and the backtest looks good, that tells me something was found. It doesn't tell me the LLM helped. A good search algorithm alone might have found the same thing.

So every experiment is a controlled comparison. There's a main search, M, that runs once and is shared. Then there's an extra budget. It goes either to more plain search, arm A, or to Partura, arm P. Each arm's library is M's factors plus whatever its extra budget found. The verdict is P minus A, seed by seed.

Same data, same operators, same engine, same random seeds, and the budgets are within two percent of each other. *(point to the blue line)* The baseline is a capable searcher, not "no research". That's the bar the LLM has to clear.

**中文.** 首先问题要问对。把 LLM 放进流程、回测好看,只说明找到了东西,不说明 LLM 有贡献;一个好的搜索算法自己也可能找到。所以每个实验都是对照:主搜索 M 只跑一次,两组共用;额外预算要么给更多普通搜索(A 组),要么给 Partura(P 组);每组的因子库 = M 的因子 + 自己额外找到的;判定看逐种子的 P − A。数据、算子、引擎、随机种子都相同,预算相差 2% 以内。基线是一个能干的搜索器,不是「什么都不做」。这是 LLM 要跨过的门槛。

**过渡:** So what should the LLM actually do in such a system? That's the first design principle.

---

## P3 · 搜索便宜,信念昂贵(1:40)

**EN.** This is the core idea in one picture. *(point to the inner ring)* The inner ring is the genetic-programming search. Every tick is one formula evaluated, at zero LLM tokens. It's fast and it's cheap.

*(point to the outer ring)* The outer ring is one research round, and it's the only place we spend tokens. Code reads what the main search found. The LLM forms a belief about why it works, turns that belief into search missions, an auditor checks them, and the cheap search does the heavy lifting. What comes back changes the belief.

*(point to the right)* That's also why it's affordable. An LLM that writes every formula pays per candidate. Here we pay per round. *(read the blue line)* One belief, many cheap evaluations, evidence, and a revised belief.

**中文.** 核心思想就这一张图。内环是遗传规划搜索:每一格是一次公式评估,0 个 LLM token,快而便宜。外环是一轮研究,也是唯一花 token 的地方:代码读主搜索的产出,LLM 形成「它为什么有效」的信念,把信念变成搜索任务,审计员检查,便宜的搜索去干重活;回来的结果再修正信念。这也是为什么花得起:逐个写公式的 LLM 按候选付费,这里按轮付费。一个信念 → 大量便宜的评估 → 证据 → 修正后的信念。

**过渡:** Concretely, here's what one formula is.

---

## P4 · 任务(0:45)

**EN.** The data is a cube: about 5,200 Chinese A-share stocks, 241 one-minute bars a day, several price and volume fields. A formula collapses each stock's minutes into one number per day. That's a daily signal. We trade it at the next morning's 15-minute VWAP, so it's executable. The finished product is a signal card: the formula, the thesis behind it, the evidence and where it came from.

**中文.** 数据是一个立方体:约 5,200 只 A 股,每天 241 根一分钟 bar,若干价量字段。一个公式把每只股票当天的分钟数据压成一个数,就是日频信号;第二天早盘 15 分钟 VWAP 成交,可执行。最终产物是信号卡:公式、背后的论点、证据、来源。

**过渡:** Now the design we ended up with.

---

## P5 · 最终设计(1:00)

**EN.** The single most important rule: *(point to the top left)* the main search runs untouched. No agent can ban, reweight or edit it.

Code reads its output and locates what's working. Partura then spends only the extra budget, through three kinds of missions. E: deepen a good core. Take a structure that works and grow new things around it. R: swap out a weak part of an existing factor. N: try a genuinely new mechanism. The search runs the missions, and each library is M's factors plus the mission factors, all scored on the same fixed yardstick.

**中文.** 最重要的一条:主搜索不受干扰,任何 agent 都不能禁止、重新加权或修改它。代码读它的产出、定位有效结构;Partura 只花额外预算,派三类任务:E 深挖,拿一个有效结构往外长;R 替换,换掉已有因子里弱的部件;N 新想法,试一个新机制。搜索去跑任务;每组因子库 = M 的因子 + 任务找到的因子,用同一把修好的尺子打分。

**过渡:** Inside Partura, who decides what?

---

## P6 · 谁决定什么(1:10)

**EN.** The rule here: agents only where a decision needs judgement, and code everywhere else.

*(walk down the table quickly)* Code finds the structure. The PI, the lead agent, decides which mechanism to bet on and writes the missions. The auditor checks the plan for maths errors and duplicates, and it is explicitly not allowed to predict returns. A checker and code check admissibility. And "did it work?" is code only. No agent ever grades its own work.

*(blue line)* Each role exists for one decision. More agents is not better. In the later rounds we dropped two roles to save cost; I'm not claiming that helped, only that the design doesn't need them everywhere.

**中文.** 原则:只有需要判断的决策点才放 agent,其余都交给代码。代码找结构;PI(主 agent)决定押哪个机制、写任务;审计员只查数学错误和重复,明确不许预测收益;检查员和代码查合规;「有没有用」只由代码判断,没有 agent 给自己打分。每个角色只为一个决策存在,agent 不是越多越好。后两轮为省成本去掉了两个角色,我不声称这样更好,只说明设计不需要处处都有 agent。

**过渡:** None of these rules were obvious at the start. Each one came from an experiment that failed.

---

## P7 · 为什么设计是这样(1:00)

**EN.** These are the eight pre-registered experiments. Each was a hypothesis about where the LLM adds value, judged against plain search on the same seeds.

*(left bracket)* In the first four, the LLM steered the search directly, inside a fixed budget: writing priors, seeding it, banning families of formulas. Twice it was worse, twice it was a tie. Its mistakes crowded out the search's own exploration. *(blue line)* That's why, in the final design, no agent touches the main search.

The next three each fixed one more thing. That's the next page.

**中文.** 这是八个事先约定的实验,每个都是「LLM 在哪有价值」的一个假设,在同样的种子上和普通搜索比。前四次 LLM 在固定预算内直接指挥搜索:写先验、给种子、禁掉一类公式,两次更差、两次打平。它的错误挤掉了搜索自己的探索。所以最终设计里没有 agent 碰主搜索。后面三次各修了一件事,下一页讲。

---

## P8 · 三次失败定下 C08 的规则(2:00)

**EN.** Read each row left to right: what we saw, what we think caused it, and what we changed. The middle column is a diagnosis made after looking at the result, not a separate test.

**C05.** *(top row)* Partura's library looked much better during selection, 1.52 against 0.94, and was exactly tied out of sample. The likely cause was the yardstick itself: certain convex transforms of volatility could score well without being new information. So we changed the yardstick: rank first, then smooth.

**C06.** *(middle row)* We added an auditor. It caught a real error: the PI had treated the minute VWAP as the minute's closing price, which broke its own derivation. But when the auditor also judged which ideas were promising, the ones it rejected did better than the ones it kept. So the auditor now checks maths and duplicates only, and the yardstick also removes non-linear exposure to the risk controls.

**C07.** *(bottom row)* With the yardstick fixed, we let the LLM only filter the search's factors. The ones it kept did worse than the ones it dropped. The library improved only because it held fewer factors. So in C08 the LLM proposes, and it doesn't filter.

*(blue line)* The auditor is good at catching errors and bad at predicting returns.

**中文.** 每行从左往右读:看到了什么、我们认为原因是什么、改了什么。中间一列是看过结果之后的诊断,不是单独的检验。C05:Partura 的组合在选拔期好看得多(1.52 对 0.94),样本外完全打平。可能的原因在尺子本身:波动率的某些凸变换不是新信息也能拿高分。所以改尺子:先排序、再平滑。C06:加了审计员。它抓到一个真实错误,PI 把分钟 VWAP 当成了分钟收盘价,推导就不成立了。但让它判断哪些想法有前途时,它挡掉的反而比放行的好。所以审计员只查数学和重复;尺子也去掉对风险控制的非线性暴露。C07:尺子修好后只让 LLM 筛选因子,它留下的比去掉的差,组合变好只因为因子少了。所以 C08 里 LLM 负责提出,不负责筛选。审计员擅长抓错,不擅长预测收益。

**过渡:** Here's what one round of the final design looks like with real files.

---

## P9 · 完整的一轮(1:15)

**EN.** This is the last round we ran: seed 808, round 3. I picked it because it was last, not because of its result.

*(left to right)* Input: the locate tool finds a structure about when in the day a stock's volume trades, and on its own it scores 1.28. Decision: the PI writes an E mission that grows new structure around it, and an N mission on the shape of minute volume. Audit: a correlation table in code, then the auditor; most seeds survive. Output: the search runs 96 evaluations per mission, and the E mission produces three new factors. Their test numbers come from the final read after all rounds. The agents never saw them.

*(blue line)* Every arrow is a file on disk, so any round can be replayed and inspected.

**中文.** 这是最后跑的一轮:种子 808 第 3 轮。选它是因为它是最后一轮,不是因为结果好。输入:定位工具找到一个「一天里成交量什么时候发生」的结构,单独 1.28 分。决策:PI 写一个 E 任务围绕它长新结构,一个 N 任务试分钟成交量的形状。审计:代码算相关度表,再由审计员审,大部分种子留下。输出:搜索每个任务跑 96 次评估,E 找到 3 个新因子。它们的测试段数值是所有轮次结束后才算的,agent 从没见过。每个箭头都是磁盘上的文件,任何一轮都能重放、检查。

**过渡:** Before the result, one check that the comparison is fair.

---

## P10 · 预算可比,规则事先定死(0:50)

**EN.** Both arms get the same 256 evaluations per seed per round. Plain search spends them on two runs; Partura on two missions plus small repair and locate budgets. The actual counts differ by two percent, and Partura used slightly less GPU time. The yardstick and the comparison, P against A over eight paired seeds, were written down and committed before any run, and the test period is read once.

**中文.** 两组每个种子每轮都是 256 次评估:普通搜索花在两次运行上,Partura 花在两个任务加少量修补和定位上。实际次数差 2%,Partura 的 GPU 时间反而略少。尺子和比较方式(P 对 A,8 对种子)在任何运行之前写下并提交,测试段只读一次。

**过渡:** And here's the result.

---

## P11 · 结果(1:30)

**EN.** *(pause, then the three numbers)* Partura's missions beat the same budget spent on plain search in seven of eight seeds. The median gain is 0.23 Sharpe. The average library goes from minus 0.33 to plus 0.16.

*(point at the chart)* Look at where the gap comes from. In seeds 805 and 807, the plain-search library fell to about minus one, and Partura's stayed near zero. The 2026 forward data, which I only report, points the same way.

**中文.** (停一下,再讲三个数)在 8 个种子里有 7 个,Partura 的任务胜过把同样预算花在普通搜索上;中位增益 0.23 夏普;组合均值从 −0.33 到 +0.16。看差距从哪来:805、807 两个种子里,普通搜索的组合跌到 −1 左右,Partura 的停在 0 附近。2026 年的前推数据(只报告)方向相同。

**过渡:** So what does this actually show? There are three comparisons here, and they say different things.

---

## P12 · 额外预算在哪里起了作用(2:00)

**EN.** *(top row)* Against extra plain search, Partura is ahead: plus 0.23, seven to one. That's the comparison the experiment was designed for.

*(middle row)* Against no extra search at all, Partura is also ahead, plus 0.24, but only five to three. That's not enough to claim it beats the base search.

*(bottom row)* And extra plain search versus none is zero. More of the same search didn't help.

So the honest reading is: the extra budget did better in Partura's hands than in the search's own hands. *(blue line)* The edge is in where the extra search went, not in discovering one high-Sharpe alpha.

*(slow down for the last line)* And one caveat I want to be clear about. This is development evidence, not independent confirmation. It's eight seed pairs on one market history, and earlier iterations were designed using the same test period. That's why the next step is fresh data.

**中文.** 第一行:对比额外的普通搜索,Partura 领先,+0.23,7 比 1,这是实验设计要回答的比较。第二行:对比完全不加额外搜索,Partura 也领先(+0.24),但只有 5 比 3,不够说它胜过基础搜索。第三行:额外普通搜索对比不加,是 0,多跑同样的搜索没有帮助。所以诚实的读法是:额外预算交给 Partura,比交给搜索自己用得好。优势在额外搜索去了哪里,而不是找到了某一个高夏普因子。还有一点要说清楚:这是开发期证据,不是独立确认。只有一段市场历史上的 8 对种子,而且之前的迭代用同一个测试期影响过这个设计。所以下一步是新数据。

**过渡:** Let me pull it together.

---

## P13 · 结论(1:00)

**EN.** Four lessons for designing an agentic researcher.

One: search is cheap and belief is expensive. Use the LLM to decide where cheap search goes, not to write formulas.

Two: keep the LLM out of the main search. When it steered directly, it never beat plain search.

Three: fix the referee before you judge the agent. A leaky yardstick rewarded the wrong things, and the agent got very good at exploiting it.

Four: use the LLM as a critic. It caught real errors, and it failed every time we asked it to predict returns.

*(blue line)* Seven redesigns, one promising result, and fresh data decides. The next steps are one read on data after September 2026, a random filter with the same number of factors as a control, and new seeds. Thank you.

**中文.** 设计 agentic 研究员的四条经验:
1. 搜索便宜、信念昂贵:让 LLM 决定便宜的搜索去哪,而不是让它写公式。
2. 不让 LLM 进主搜索:它直接指挥的时候,从没赢过普通搜索。
3. 先修好裁判,再评判 agent:有漏洞的尺子奖励了错误的东西,agent 很擅长钻漏洞。
4. 把 LLM 当批评者:它抓到了真实的错误,但每次让它预测收益都失败了。

七次重新设计,一个有希望的结果,新数据说了算。下一步:在 2026 年 9 月之后的数据上读一次;用同样因子数的随机筛选做对照;新种子。谢谢。

---

## 时间与压缩

合计约 17 分钟。超时的话:
- P4 只说一句;
- P6 只念蓝线;
- P7 只讲「前四次直接指挥失败」;
- P9 只讲输入和输出。

**不要压缩 P8、P11、P12**,它们是故事的核心。

## 最容易被问到的五个问题(各 20 秒答)

1. **「p 值是多少?测试期读了几次?」**
   One-sided p is 0.012 on the pre-specified test, but the test period has been read eight times across iterations. So I treat it as a promising development result, not confirmation. The confirmation is one read on data after September 2026.
2. **「为什么 Partura 能赢,而单个因子并不强?」**
   Its extra factors are individually modest. The gain is at the library level: where plain search's extra factors dragged the book down, Partura's did less damage. That's an allocation-of-search effect, not one star factor.
3. **「随机挑任务会不会一样好?」**
   That's the right control and it's on my next-steps list: a random filter or random missions with the same budget and the same number of factors.
4. **「LLM 有没有看到测试期数据?」**
   No. Agents only see the training and validation periods. Their reads are audited from the session logs, and every test number is computed in code after all rounds.
5. **「成本多少?」**
   GPU time is comparable across arms. LLM tokens are the extra cost, spent per round, not per candidate; the later rounds used cheaper models with the same rules.
