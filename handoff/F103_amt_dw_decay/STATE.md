# F103_amt_dw_decay — 交接状态

_自动生成于 2026-10-05 11:26(`python scripts/recorder.py --brief F103_amt_dw_decay` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #820(批次 B01_single_factors)
- 表达式:`cross_max(mul(day_close(Amt), ts_min(pow_3(day_durbin_watson(cross_decay_linear(Amt, 30))), 1)), 5)`

## 现在到哪一步

- **阶段:全部完成**
- **留出段已经读过 1 次**(10-03 23:26)—— **不许再读**。候选在留出段上的数全在 `runs/F103_amt_dw_decay/final.json`(`./scripts/study.sh digest F103_amt_dw_decay final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `audit-mechanism:F103_amt_dw_decay`:已返回结果,最后动作 10-04 00:01 → `handoff/F103_amt_dw_decay/agents/audit-mechanism_a4b7f0588d11e04ba.md`
  - `revise:F103_amt_dw_decay`:已返回结果,最后动作 10-04 00:29 → `handoff/F103_amt_dw_decay/agents/revise_ae84c8cd59be0697d.md`
  - `synth:F103_amt_dw_decay`:还在跑(多半就是你自己)

**接手的人该做什么:** 这条因子做完了。最终结论在 `handoff/F103_amt_dw_decay/results/` 里最新的那个(revised.json 优先,否则 study.json)。

## 研究员自己写的现状(`notes/F103_amt_dw_decay/state.md`)

(**没有**。上一个研究员没有留下现状说明 —— 假设、逻辑和后面的思路只能从 notes、研究日志和动作流水里重建。)

## 研究日志(`notes/F103_amt_dw_decay/journal.md`:0 条,其中研究员自己写的 0 条)

(还没有。之前的研究员没有记日志 —— 它的想法只能从 notes 和动作流水里推。)

## 配置里的实验计划(`configs/F103_amt_dw_decay.yaml`)

- 标题:收盘集合竞价成交额 × (30 日平均日内成交曲线的粗糙度)³,套 5 日极值记忆
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base
- **S1_structure**(11 个变体):预测力在收盘竞价额支、粗糙度支,还是两者的乘积里?ts_min / pow_3 / cross_max 这三个节点各自是不是多余的?
  a_no_tsmin、a_A5、a_C、e_pow1、e_pow2、m_none、m_mean5、f_sum、f_share、i_rankmul、i_addrank
- **S2_distil**(12 个变体):把树收成 水平腿 x 集中度^k 之后:哪个配比在 train 和 valid 上都站得住(尤其是多头腿)?水平腿用全天成交额还是 F001 的蒸馏结果?它比已知家族多了什么?
  d_sum_k3、d_sum_k2、d_sum_k1、d_amt、b_stdamt9、x_std9_k1、x_std9_k2、e_peak_k2、x_std9_pk2、g_stdB、x_std9_k1_w15、x_std9_k1_w60
- **S_final**(5 个变体):样本外(用户的测试段):删节点、改配比、换水平腿,这三步各自还成立吗?这棵树在留出段上有没有给已知家族(F001 的蒸馏结果)加东西?
  f_orig、f_sum_k3、f_sum_k2、f_std9_k1、f_stdamt9

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F103_amt_dw_decay`)

- `S0_baseline`  10-03 17:43  1 个变体  → `./scripts/study.sh digest F103_amt_dw_decay S0_baseline`
- `S1_structure`  10-03 19:34  11 个变体  → `./scripts/study.sh digest F103_amt_dw_decay S1_structure`
- `S2_distil`  10-03 23:19  12 个变体  → `./scripts/study.sh digest F103_amt_dw_decay S2_distil`
- `final`  10-03 23:26  5 个变体  → `./scripts/study.sh digest F103_amt_dw_decay final`
- `sweep_s1`  10-05 11:02  126 个变体  → `./scripts/study.sh digest F103_amt_dw_decay sweep_s1`
- `anatomy_s1`  10-05 11:06  0 个变体  → `./scripts/study.sh digest F103_amt_dw_decay anatomy_s1`
- `x1`(自写脚本的输出)  10-03 19:40  exit 0  → `logs/F103_amt_dw_decay_x1.log`
- `x2`(自写脚本的输出)  10-03 19:56  exit 0  → `logs/F103_amt_dw_decay_x2.log`
- `x3`(自写脚本的输出)  10-03 23:04  exit 0  → `logs/F103_amt_dw_decay_x3.log`
- `audit1`(自写脚本的输出)  10-03 23:54  exit 0  → `logs/F103_amt_dw_decay_audit1.log`
- `rev1`(自写脚本的输出)  10-04 00:12  exit 0  → `logs/F103_amt_dw_decay_rev1.log`

## 已写的 notes(`notes/F103_amt_dw_decay/`)

`01_expression.md`(3K)、`02_operators.md`(2K)、`03_decomposition.md`(1K)、`04_grammar.md`(1K)、`05_hypotheses.md`(10K)、`06_baseline.md`(3K)、`07_S1_structure.md`(4K)、`07_S2_distil.md`(5K)、`07_SA_audit.md`(1K)、`07_S_final.md`(2K)、`07_conditional.md`(1K)、`07_controls.md`(1K)、`07_neutralise.md`(2K)、`07x_x1_anatomy.md`(5K)、`07x_x2_interaction.md`(8K)、`07x_x3_family.md`(14K)、`07x_x4_audit.md`(7K)、`07x_x5_rev1.md`(10K)、`08_variants.md`(2K)、`09_diagnosis.md`(14K)、`10_distilled.md`(22K)、`11_risks.md`(4K)、`12_next.md`(2K)、`synthesis.md`(11K)

## 自写的探针与分析脚本(`studies/F103_amt_dw_decay/`)

- `audit_1.py`  10-03 23:47  audit_1 -- 审查员的反驳实验。只读 train / valid(utrain = 两者之和);留出段的行从不被索引。
- `probes.py`  10-03 18:43  Probes this tree needs:
- `rev1_matched.py`  10-04 00:08  rev1 -- 修订阶段的补充分析。只读 train / valid(utrain = 两者之和);留出段的行从不被索引。
- `x1_anatomy.py`  10-03 18:46  X1 -- anatomy of F103's two operands, before any stage is designed.
- `x2_interaction.py`  10-03 19:45  X2 -- after S1: the tree is (amount level) x (roughness of the 30-day average intraday Amt curve),
- `x3_family.py`  10-03 22:40  X3 -- after S1 / X1 / X2 the tree is  (amount level) x (roughness of the 30-day average intraday Amt curve)^k.

## 结构化结果(`handoff/F103_amt_dw_decay/results/`)

- `audit-mechanism.json`
- `audit-numbers.json`
- `revised.json`
- `study.json`

报告:`research/alpha_distillation/F103_amt_dw_decay.md`(10-04 12:08 生成)
