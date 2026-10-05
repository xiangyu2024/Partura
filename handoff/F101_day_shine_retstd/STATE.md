# F101_day_shine_retstd — 交接状态

_自动生成于 2026-10-04 23:02(`python scripts/recorder.py --brief F101_day_shine_retstd` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:手写 day_shine_retstd(批次 B01_single_factors)
- 表达式:`abs_(cs_demean(day_mean(in_sustain_stddev(is_gt(sub(in_slice(Volume, 2, 237), in_delay(in_slice(Volume, 2, 237), 1)), add(in_mean_full(sub(in_slice(Volume, 2, 237), in_delay(in_slice(Volume, 2, 237), 1))), in_stddev_full(sub(in_slice(Volume, 2, 237), in_delay(in_slice(Volume, 2, 237), 1))))), in_slice(Ret, 2, 237), 5))))`

## 现在到哪一步

- **阶段:全部完成**
- **留出段已经读过 1 次**(10-03 23:00)—— **不许再读**。候选在留出段上的数全在 `runs/F101_day_shine_retstd/final.json`(`./scripts/study.sh digest F101_day_shine_retstd final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `audit-numbers:F101_day_shine_retstd`:已返回结果,最后动作 10-03 23:19 → `handoff/F101_day_shine_retstd/agents/audit-numbers_a8b3d9dbf8b49904e.md`
  - `audit-mechanism:F101_day_shine_retstd`:已返回结果,最后动作 10-03 23:28 → `handoff/F101_day_shine_retstd/agents/audit-mechanism_a44fe5af2ad163716.md`
  - `revise:F101_day_shine_retstd`:已返回结果,最后动作 10-04 00:02 → `handoff/F101_day_shine_retstd/agents/revise_a7c1f89ef939ebc23.md`

**接手的人该做什么:** 这条因子做完了。最终结论在 `handoff/F101_day_shine_retstd/results/` 里最新的那个(revised.json 优先,否则 study.json)。

## 研究员自己写的现状(`notes/F101_day_shine_retstd/state.md`)

(**没有**。上一个研究员没有留下现状说明 —— 假设、逻辑和后面的思路只能从 notes、研究日志和动作流水里重建。)

## 研究日志(`notes/F101_day_shine_retstd/journal.md`:0 条,其中研究员自己写的 0 条)

(还没有。之前的研究员没有记日志 —— 它的想法只能从 notes 和动作流水里推。)

## 配置里的实验计划(`configs/F101_day_shine_retstd.yaml`)

- 标题:方正「适度冒险」的日频零件:成交量激增分钟之后 5 分钟收益波动(耀眼波动率)的日均值,对截面均值取绝对偏离
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base
- **S1_parts**(8 个变体):预测力在三个零件(放量掩码 / 5 分钟窗口 std / 截面折叠)的哪一个里?哪一个可以拿掉或换成朴素等价物?
  s1_nofold、s1_rankfold、s1_fold_ivol、s1_fold_roll5、s1_mask_quiet、s1_win3、s1_win15、s1_fold_dvol20
- **S2_background**(10 个变体):多头腿的稳健性是不是「背景波动」(不被放量爆发主导的那部分波动)的性质?它是不是价格水平 / 报价单位的另一种写法?
  s2_roll5_diag、s2_roll3、s2_roll15、s2_roll60、s2_absret、s2_roll5_noslice、s2_roll5_rankfold、s2_roll5_nofold、s2_fold_logprice、s2_burst_ratio
- **S_final**(5 个变体):样本外(用户的测试段):背景波动折叠的多头腿是不是仍然好于原式?差别来自折叠方式还是统计量?
  f_orig、f_roll5、f_roll5_rank、f_ivol、f_j_rank
- **SR_rivals**(7 个变体):原式相对朴素的日内波动折叠多出来的东西,是 Volume 字段的内容、一字板日的贡献,还是 F001 的日内波动 + 极值记忆族折叠之后就有的?
  sr_fold_jret、sr_fold_q90、sr_orig_nz、sr_ratio_jret、sr_ratio_ivol、sr_ratio_j_jret、sr_fold_kivmax9

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F101_day_shine_retstd`)

- `S0_baseline`  10-03 17:40  1 个变体  → `./scripts/study.sh digest F101_day_shine_retstd S0_baseline`
- `S1_parts`  10-03 19:41  8 个变体  → `./scripts/study.sh digest F101_day_shine_retstd S1_parts`
- `S2_background`  10-03 20:01  10 个变体  → `./scripts/study.sh digest F101_day_shine_retstd S2_background`
- `final`  10-03 23:00  5 个变体  → `./scripts/study.sh digest F101_day_shine_retstd final`
- `rev1`  10-03 23:36  7 个变体  → `./scripts/study.sh digest F101_day_shine_retstd rev1`
- `look`(自写脚本的输出)  10-03 19:28  exit 0  → `logs/F101_day_shine_retstd_look.log`
- `look2`(自写脚本的输出)  10-03 19:50  exit 0  → `logs/F101_day_shine_retstd_look2.log`
- `look3`(自写脚本的输出)  10-03 22:45  exit 0  → `logs/F101_day_shine_retstd_look3.log`
- `audit1`(自写脚本的输出)  10-03 23:21  exit 0  → `logs/F101_day_shine_retstd_audit1.log`
- `rev2`(自写脚本的输出)  10-03 23:41  exit 0  → `logs/F101_day_shine_retstd_rev2.log`

## 已写的 notes(`notes/F101_day_shine_retstd/`)

`01_expression.md`(1K)、`02_operators.md`(2K)、`03_decomposition.md`(1K)、`04_grammar.md`(1K)、`05_hypotheses.md`(4K)、`06_baseline.md`(3K)、`07_S1_parts.md`(5K)、`07_S2_background.md`(5K)、`07_SA_audit.md`(1K)、`07_SR_rivals.md`(6K)、`07_S_final.md`(2K)、`07_conditional.md`(1K)、`07_controls.md`(1K)、`07_neutralise.md`(2K)、`07x_look.md`(6K)、`07x_look2.md`(4K)、`07x_look3.md`(10K)、`07x_review1_audit.md`(7K)、`07x_review2_rev2.md`(13K)、`08_variants.md`(3K)、`09_diagnosis.md`(13K)、`10_distilled.md`(13K)、`11_risks.md`(4K)、`12_next.md`(2K)

## 自写的探针与分析脚本(`studies/F101_day_shine_retstd/`)

- `audit_1.py`  10-03 23:17  F101 audit (reviewer: mechanism & over-fitting).  Train / valid only -- the holdout is never touched.
- `look.py`  10-03 18:35  F101: direct measurements on the pre-fold quantity J and on the fold itself.
- `look2.py`  10-03 19:44  F101, after S1: the surge mask changes the SHORT leg, not the long leg.
- `look3.py`  10-03 22:38  F101, look3 (after S1 + S2): what is the LONG leg made of, and how should the fold be aggregated in time?
- `probes.py`  10-03 17:49  Probes this study needs and the built-ins do not answer.
- `rev_look.py`  10-03 23:37  F101 revision (tag rev2): bespoke numbers the review asked for.  Train / valid only -- the holdout is never to

## 结构化结果(`handoff/F101_day_shine_retstd/results/`)

- `audit-mechanism.json`
- `audit-numbers.json`
- `revised.json`
- `study.json`

报告:`research/alpha_distillation/F101_day_shine_retstd.md`(10-04 12:07 生成)
