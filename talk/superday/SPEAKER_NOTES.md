# Speaker notes: `final.tex` (14 main pages, about 20 minutes)

Times are targets. The backup pages are for questions only.

| Page | Time | Say |
|---|---|---|
| 1 | 0:20 | Partura is an LLM research team that steers a symbolic alpha miner. Seven iterations, one promising result. |
| 2 | 1:10 | A good backtest only shows that something was found. The question is whether the LLM made search better than search alone, so the baseline is plain GP with the same data, seeds and extra budget. |
| 3 | 1:20 | Search is cheap and belief is expensive. An LLM that writes formulas one by one competes with GP at GP's game. Tokens should buy beliefs that redirect thousands of cheap evaluations. |
| 4 | 1:00 | There are two layers and two directions. Partura proposes where to look, AlphaCube reports what it found and what failed, and a referee in code scores both. |
| 5 | 0:50 | The task: one formula over the minute cube gives one daily signal. The target is next-day return, entry at the first-15-minute VWAP. |
| 6 | 1:10 | Final design: the main search M runs untouched. Partura reads its output and spends only the extra budget, on E, R and N missions. |
| 7 | 1:00 | Why the design looks like this. In C01–C04 the LLM steered GP inside a fixed budget: twice worse, twice inconclusive. Hence the first rule: no agent touches the main search. |
| 8 | 2:00 | Three failures set the other rules. **C06 script, about 25 s, below.** |
| 9 | 1:20 | One real round, seed 808 round 3: locate output, the PI's two slots, the audit's strikes, and three heads from GP. |
| 10 | 1:00 | Same extra budget: 4,438 scored evaluations for plain GP, 4,525 for Partura. The rule was fixed before the run: P against A, 8 paired seeds, one-sided Wilcoxon. |
| 11 | 1:30 | The result: Partura's missions beat extra plain GP in 7 of 8 seeds, with median +0.23 and p 0.012. |
| 12 | 2:00 | Three comparisons. P beats A, but P against M alone is not significant, and A against M is flat. The edge is in how the extra budget is spent: where GP found nothing, Partura added heads that held; where GP's extra heads hurt, Partura's hurt less. Its median book is only +0.05. This fits "search is cheap; belief is expensive". |
| 13 | 1:30 | How to read p = 0.012: read the statement on the page aloud, then name what would confirm it. |
| 14 | 1:00 | The takeaways: back to the two principles; critic, not gatekeeper; fresh data decides. |

## Page 8, C06 (about 25 seconds)

> The Auditor caught a specific mathematical error: the PI treated minute VWAP as the minute closing price.
> Correcting this invalidated the original mechanism. However, the Auditor's broader filtering decisions
> performed poorly out of sample. This is why C08 retained the Auditor for mathematical consistency checks
> but removed its authority to judge predictive quality.

Supporting material: backup "C06, the auditor as critic and as gate". It holds the derivation (θ = VWAP's position inside the bar) and the table of accepted against rejected seeds.

## Page 13, the statement

> C08 is the first design that produced a statistically significant paired improvement under its pre-specified
> within-study test. However, because earlier designs repeatedly used the same test period, I treat this as a
> promising development result rather than independent confirmation.

## Likely follow-up questions and their backup pages

- "Show me one real signal end to end." Use "One finished signal card". It also shows that GP changed the PI's thesis, so the explanation has to describe the final expression.
- "Is this just fewer heads?" Possibly. The fix is a random filter with the same head count, the second confirmation test on page 13. C07's book also improved mostly by holding fewer heads (backup C07).
- "Which heads carried it?" Use "C08 heads, one by one". Round 3 did best, round 1 worst, but round and flow are confounded.
- "Cost?" GPU seconds: A 26,294, P 24,421. LLM tokens are not budget-matched; that is the fourth confirmation test.
