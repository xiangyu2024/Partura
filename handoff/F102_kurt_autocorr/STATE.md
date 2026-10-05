# F102_kurt_autocorr — 交接状态

_自动生成于 2026-10-05 11:26(`python scripts/recorder.py --brief F102_kurt_autocorr` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #3961(批次 B01_single_factors)
- 表达式:`cross_sum(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 15)`

## 现在到哪一步

- **阶段:全部完成**
- **留出段已经读过 1 次**(10-03 23:15)—— **不许再读**。候选在留出段上的数全在 `runs/F102_kurt_autocorr/final.json`(`./scripts/study.sh digest F102_kurt_autocorr final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `audit-mechanism:F102_kurt_autocorr`:已返回结果,最后动作 10-03 23:38 → `handoff/F102_kurt_autocorr/agents/audit-mechanism_a2d310a359bfeff69.md`
  - `revise:F102_kurt_autocorr`:已返回结果,最后动作 10-04 00:24 → `handoff/F102_kurt_autocorr/agents/revise_a39c89bd8b2569636.md`
  - `synth:F102_kurt_autocorr`:还在跑(多半就是你自己)

**接手的人该做什么:** 这条因子做完了。最终结论在 `handoff/F102_kurt_autocorr/results/` 里最新的那个(revised.json 优先,否则 study.json)。

## 研究员自己写的现状(`notes/F102_kurt_autocorr/state.md`)

(**没有**。上一个研究员没有留下现状说明 —— 假设、逻辑和后面的思路只能从 notes、研究日志和动作流水里重建。)

## 研究日志(`notes/F102_kurt_autocorr/journal.md`:0 条,其中研究员自己写的 0 条)

(还没有。之前的研究员没有记日志 —— 它的想法只能从 notes 和动作流水里推。)

## 配置里的实验计划(`configs/F102_kurt_autocorr.yaml`)

- 标题:3 对分钟收益相关的日内峰度,平方后 15 日求和:主体是 4 分钟局部形态分布的形状(水平 + 日间离散),尾部是近 15 日的涨停封板事件;两条腿要的速度不同。留出段多头腿净超额:原式 hl=1 −0.7% / 原式 hl=5 +2.5% / 记忆拉到 60 日 +7.4%(修订:60 日版本对期限匹配的控制 R² 0.45,多头腿约四成是避开近 60 日封板票)
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base
- **S1_layers**(8 个变体):预测力在这棵树的哪一层?pow_2 的折叠、平方的凸性、15 日求和各贡献什么;D1–D9 的排序是不是分钟收益一阶自相关的另一种写法?
  l_k2_today、l_nofold_lin、l_fold_lin、l_max、l_med、l_noac、l_ac15、r_ar1
- **S2_windows**(6 个变体):15 和 3 是不是搜出来的幸运参数?(H9:真效应应该有邻域)
  w_d5、w_d10、w_d30、w_d60、w_a5、w_a10
- **S3_aggregate**(11 个变体):15 日求和这一层到底在做什么(水平 / 离散 / 缺失日),以及两条腿要的速度是不是不一样:把记忆拉长,多头腿净超额能不能在 train 和 valid 上都站住?
  a_mean_sq15、a_mean_abs15、a_level15、a_disp15、u_max30、u_max60、u_max120、u_mean_abs60、u_med60、u_max15_sm10、r_meanA15
- **S_final**(5 个变体):原式、同速度的提纯式、以及极值记忆 15 / 30 / 60 这条'速度'曲线,在 2023-08 之后从未看过的数据上还成立吗?多头腿净超额是不是仍然随记忆变长而上升?
  f_orig、f_mean_abs15、f_max15、f_max30、f_max60
- **SR_horizon**(3 个变体):把与因子同期限的朴素控制(60 日封板代理 / 日内波动 / 成交额 / 最大振幅 / 日频波动 / 最大日收益 / 最大绝对日收益)加进来之后,控制变量张成多少、残差的多头腿还剩多少?
  h_orig、h_max30、h_max60

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F102_kurt_autocorr`)

- `S0_baseline`  10-03 17:40  1 个变体  → `./scripts/study.sh digest F102_kurt_autocorr S0_baseline`
- `s12`  10-03 19:50  15 个变体  → `./scripts/study.sh digest F102_kurt_autocorr s12`
- `s3`  10-03 22:53  12 个变体  → `./scripts/study.sh digest F102_kurt_autocorr s3`
- `final`  10-03 23:15  5 个变体  → `./scripts/study.sh digest F102_kurt_autocorr final`
- `rev1`  10-03 23:54  3 个变体  → `./scripts/study.sh digest F102_kurt_autocorr rev1`
- `sweep_s1`  10-05 11:01  95 个变体  → `./scripts/study.sh digest F102_kurt_autocorr sweep_s1`
- `anatomy_s1`  10-05 11:05  0 个变体  → `./scripts/study.sh digest F102_kurt_autocorr anatomy_s1`
- `x1`(自写脚本的输出)  10-03 19:32  exit 0  → `logs/F102_kurt_autocorr_x1.log`
- `x2`(自写脚本的输出)  10-03 20:05  exit 0  → `logs/F102_kurt_autocorr_x2.log`
- `x3`(自写脚本的输出)  10-03 23:04  exit 0  → `logs/F102_kurt_autocorr_x3.log`
- `audit1`(自写脚本的输出)  10-03 23:33  exit 0  → `logs/F102_kurt_autocorr_audit1.log`
- `rev2`(自写脚本的输出)  10-04 00:04  exit 97  → `logs/F102_kurt_autocorr_rev2.log`

## 已写的 notes(`notes/F102_kurt_autocorr/`)

`01_expression.md`(2K)、`02_operators.md`(3K)、`03_decomposition.md`(3K)、`04_grammar.md`(1K)、`05_hypotheses.md`(11K)、`06_baseline.md`(1K)、`07_S1_layers.md`(3K)、`07_S2_windows.md`(2K)、`07_S3_aggregate.md`(5K)、`07_SA_audit.md`(1K)、`07_SR_horizon.md`(4K)、`07_S_final.md`(4K)、`07_conditional.md`(2K)、`07_controls.md`(1K)、`07_neutralise.md`(4K)、`07x_1_anatomy.md`(8K)、`07x_2_refine.md`(5K)、`07x_3_longleg.md`(8K)、`07x_4_audit.md`(6K)、`07x_5_revision.md`(11K)、`07x_anatomy.md`(1K)、`07x_longleg.md`(1K)、`07x_refine.md`(1K)、`08_variants.md`(3K)、`09_diagnosis.md`(8K)、`10_distilled.md`(12K)、`11_risks.md`(4K)、`12_next.md`(2K)、`synthesis.md`(11K)

## 自写的探针与分析脚本(`studies/F102_kurt_autocorr/`)

- `audit_1.py`  10-03 23:29  audit_1 -- reviewer's refutation attempt (train / valid only, never the holdout).
- `probes.py`  10-03 19:37  Probes this tree needs and neither F001 nor F002 did.
- `r1_revision.py`  10-03 23:55  r1 -- revision after the two reviews (train / valid only, never the holdout; no candidate is changed).
- `x1_anatomy.py`  10-03 18:40  x1 -- what does  cross_sum(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 15)  actually measure?
- `x2_refine.py`  10-03 19:54  x2 -- three questions S1/S2 left open (train/valid only, never the holdout):
- `x3_longleg.py`  10-03 22:56  x3 -- what S3 left open about the long-memory candidates (train/valid only, never the holdout).

## 结构化结果(`handoff/F102_kurt_autocorr/results/`)

- `audit-mechanism.json`
- `audit-numbers.json`
- `revised.json`
- `study.json`

报告:`research/alpha_distillation/F102_kurt_autocorr.md`(10-04 12:07 生成)
