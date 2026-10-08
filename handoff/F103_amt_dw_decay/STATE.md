# F103_amt_dw_decay — 交接状态

_自动生成于 2026-10-06 11:53(`python scripts/recorder.py --brief F103_amt_dw_decay` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #820(批次 B01_single_factors)
- 表达式:`cross_max(mul(day_close(Amt), ts_min(pow_3(day_durbin_watson(cross_decay_linear(Amt, 30))), 1)), 5)`

## 现在到哪一步

- **阶段:全部完成**
- **留出段已经读过 2 次**(10-03 23:26, 10-05 12:09)—— **不许再读**。候选在留出段上的数全在 `runs/F103_amt_dw_decay/final.json`(`./scripts/study.sh digest F103_amt_dw_decay final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `revise:F103_amt_dw_decay`:已返回结果,最后动作 10-04 00:29 → `handoff/F103_amt_dw_decay/agents/revise_ae84c8cd59be0697d.md`
  - `synth:F103_amt_dw_decay`:已返回结果,最后动作 10-05 11:29 → `handoff/F103_amt_dw_decay/agents/synth_a9e8c11a43c18aade.md`
  - `verdict:F103_amt_dw_decay`:已返回结果,最后动作 10-05 13:52 → `handoff/F103_amt_dw_decay/agents/verdict_a2ce53d5ead3818bd.md`

**接手的人该做什么:** 这条因子做完了。最终结论在 `handoff/F103_amt_dw_decay/results/` 里最新的那个(revised.json 优先,否则 study.json)。

## 研究现状(`notes/F103_amt_dw_decay/state.md`,10-05 13:47 更新)—— **先读这个文件**

# F103_amt_dw_decay — 研究现状(主研覆盖重写,2026-10-05,读完批量扫描 s2 之后)

原式:`cross_max(mul(day_close(Amt), ts_min(pow_3(day_durbin_watson(cross_decay_linear(Amt, 30))), 1)), 5)`(挖掘库 #820)
口径:**只看多头腿扣 15bp 净超额(Lnet)+ 纯多头夏普(Lshp)**,半衰期按纯多头书选。噪声 ±3 点 / ±0.3。门槛 cov ≥ 0.95、dist ≥ 0.5。
**两轮都没有读测试段**(`runs/F103_amt_dw_decay/sweepfinal_*.json` 未打开;结论全部建立在 train / valid 上)。

---

## 1. 现状 —— 结论已闭合

**verdict = 只是已知族(提纯成功、升华失败)。** 两轮扫描(s1 126 + s2 172 个变体)之后:

- `v_base` tr/va/ut **+9.4/+4.5/+8.1%**、Lshp 1.86/0.73/**1.49**、LTO 4.0%、sg −1、hlL 10、ρk 0.34。
- `k_known = cross_mean(day_std(Amt), 30)` **+12.6/+22.3/+15.4%**、1.78/3.46/**2.22**、LTO 3.4%。
- `k_known_xfrozen = cs_last_high20(neg(K), cross_max(day_zero_ratio(Ret), 15))` **+16.4/+23.2/+18.5%**、2.81/3.98/**3.15**(s2 起的通用筛子基准)。
- **best_own**:`h_C_relstd` = `cross_max(mul(day_close(Amt), day_std(in_pct(cross_decay_linear(Amt,30),1))), 5)`
  **+11.9/+20.7/+14.4%**、1.92/3.56/**2.37**、LTO 3.0%、ρk **0.83**。次 `h_C_peakshare` 2.20、`abl_D` 2.11。
- **best_on_known**:`scr_xhi_p`(原式当剔除筛子叠在 K 上)+14.0/+21.1/**+16.0%**、2.14/3.44/**2.49**、ρk 0.85。
- 提纯幅度真实(1.49 → 2.37,净超额 +8.1 → +14.4%),**但落点在已知族内**:ρk 0.83、净超额仍比 K 低 1 点、夏普高 0.15(噪声带一半)。
  筛子位置上本因子值 +0.27 夏普,而通用冻结筛子同一位置值 **+0.93**,且两道筛子会互相吞掉((丁),§3)。
- 决定性旁证(s1):`res_known`(对 K 取截面秩残差)valid **−2.1%** / Lshp **−0.27**。正交部分样本外是负的。

**一句话**:C 那一层是「写错了的相对抖动」,改对之后夏普 1.49 → 2.37,但跳进了已知族里面;它顺带做的那点「躲冻结盘口」被通用冻结筛子以 6 倍幅度做掉。

(…全文 6322 字符,读 `notes/F103_amt_dw_decay/state.md`)

## 研究日志(`notes/F103_amt_dw_decay/journal.md`:2 条,其中研究员自己写的 2 条)

最近的 5 条(更早的和全文看文件):

### 2026-10-05 11:26 [主研] 批量扫描 s1 的综合

- 原式逐层读完:`day_durbin_watson` 的分母是 Σx² 不是 Σ(x−x̄)²,它不是 DW 而是**无尺度的尖峰占比**(恒 ≥ 0:`sub_D_abs_` 与 `abl_D` 逐列相同);`ts_min(·,1)` 是**恒等式**(`abl_E` 与 `v_base` 逐列相同);`cross_decay_linear(Amt,30)` 是**跨日**的分钟槽平滑,不是日内衰减。
- 承重的只有 `day_close(Amt)`:`iso_A` 单独 ut +13.4% / Lshp 1.90(**比原式 +8.1% / 1.49 更好**);C 腿单独 `iso_E` / `only_F_R` 的 valid 是 −18.6% / −17.8%。外层 `cross_max(·,5)` 是自由参数(iso_F +8.5%,sub_G_* 全在 +8.2~+8.4)。唯一不能删的是 B 槽的 30 日平滑(`abl_B` ut −3.3%)。
- 指数阶梯与 ρk 单调同向 = 全表主轴:pow_05(ρk .90)+13.7% → pow_1(.84)+12.8% → pow_1.5(.73)+11.4% → pow_2(.59)+10.0% → pow_2.5(.46)+8.8% → pow_3(.34)+8.1%,而 train Lshp 走反方向(1.64→1.96)⇒ **pow_3 是拟合在 train 上的**。
- 相对已知族**没有增量**:`res_known` valid −2.1% / Lshp −0.27;overlay 最好一档 `ov_p10` 夏普只高 +0.03(噪声 ±0.3)而净超额低 2.9 点、换手翻倍;126 个变体没有一个 ut Lnet 超过 k_known 的 +15.4%。
- 解剖的三块可用发现:(1) 次新段(7.1%,段等权 −28.7%)段内随指数单调 −2.7% → **+25.3%**,与全市场完全相反 ⇒ C 是次新投机指纹;(2) 原式的选股力在成交额最高两档(段内 +9.6% / +17.2%,k_known 只有 −5.2% / +2.5%),而 k_known 的钱全是流动性倾斜(最清淡档超配 +80.3pp);(3) 冻结盘口段占 6.5%、段等权 **−67.4%**,全不碰约值 +4%/年,原式低配最多(−4.5pp)也是段内唯一不亏(+0.5%)。
- 第二批 36 条假设已落盘
…(这条日志还有后文,读 journal.md)

### 2026-10-05 13:48 [主研] 批量扫描 s2 对账与结论

- **定论:只是已知族(提纯成功、升华失败)。** best_own = `h_C_relstd`(C 换成 `day_std(in_pct(cross_decay_linear(Amt,30),1))`)tr/va/ut **+11.9/+20.7/+14.4%**、Lshp 1.92/3.56/**2.37**、LTO 3.0% —— 比原式(1.49)高 **+0.88 夏普**,但 ρk **0.83**、净超额仍比 `k_known`(+15.4% / 2.22)低 1 点 ⇒ 提纯的终点在已知族里面。best_on_known = `scr_xhi_p`(原式当剔除筛子叠在 K 上)+16.0% / **2.49**,比 K 高 +0.27 夏普,但比 `k_known_xfrozen`(+18.5% / **3.15**)低 0.66。
- **对账**:(甲) A 组支持 —— `day_durbin_watson` 确认只是「写错了的相对抖动」;log 版更差(2.08)、`cross_zscore` 版崩掉(−11.3% / −1.78)⇒ C 的价值是**持久截面水平**不是异常;centroid 1.86 = 什么都不做。(乙) B 组机制否定 —— 年龄桶内 pow_3 反而**升到** 1.62(pow_1 版 2.02 仍赢)⇒ pow_3 不是伪装的次新押注;`seg_new_p` valid Lshp 0.62 ⇒ 次新段 +25.3% 不可收割;次新筛子对 K / 对原式各值 +0.29 / +0.30(与载体无关)⇒ C 腿没在躲次新。(丙) C 组强烈支持 —— 冻结筛子 2.22 → 3.15(+0.93),同一道筛子加在原式上只 +0.15 ⇒ C 腿已顺带做掉大部分但做得很差。(丁) 冻结+次新**不可加**(3.16 ≈ 3.15)。(戊) D 组七条全负,且显式限定的清淡半边(2.25)**高于**流动半边(2.07),与解剖方向相反。(己) `h_K_tail_q75` 2.42 ≫ q25 1.16 ⇒ K 的钱在「忙的日子」;`h_K_winsor_ema30` 2.34 且换手 3.4%→2.1%;两条低相关候选与 `h_K_plus_C` 全死。
- **新结构事实**:`h_C_leaf_vol` 与 `abl_D` **逐列相同** ⇒ C 腿完全价格盲,s1 里 Amt→Volume 的死亡全部来自 A 腿。意外彩
…(这条日志还有后文,读 journal.md)

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
- `sweep_s2`  10-05 12:00  172 个变体  → `./scripts/study.sh digest F103_amt_dw_decay sweep_s2`
- `anatomy_s2`  10-05 12:05  0 个变体  → `./scripts/study.sh digest F103_amt_dw_decay anatomy_s2`
- `sweepfinal_s2`  10-05 12:11  8 个变体  → `./scripts/study.sh digest F103_amt_dw_decay sweepfinal_s2`
- `sweep_s3`  10-05 17:32  197 个变体  → `./scripts/study.sh digest F103_amt_dw_decay sweep_s3`
- `anatomy_s3`  10-05 18:30  0 个变体  → `./scripts/study.sh digest F103_amt_dw_decay anatomy_s3`
- `sweepfinal_s3`  10-05 18:33  8 个变体  → `./scripts/study.sh digest F103_amt_dw_decay sweepfinal_s3`
- `sweep_s4`  10-06 10:44  197 个变体  → `./scripts/study.sh digest F103_amt_dw_decay sweep_s4`
- `anatomy_s4`  10-06 10:50  0 个变体  → `./scripts/study.sh digest F103_amt_dw_decay anatomy_s4`
- `sweepfinal_s4`  10-06 11:09  8 个变体  → `./scripts/study.sh digest F103_amt_dw_decay sweepfinal_s4`
- `x1`(自写脚本的输出)  10-03 19:40  exit 0  → `logs/F103_amt_dw_decay_x1.log`
- `x2`(自写脚本的输出)  10-03 19:56  exit 0  → `logs/F103_amt_dw_decay_x2.log`
- `x3`(自写脚本的输出)  10-03 23:04  exit 0  → `logs/F103_amt_dw_decay_x3.log`
- `audit1`(自写脚本的输出)  10-03 23:54  exit 0  → `logs/F103_amt_dw_decay_audit1.log`
- `rev1`(自写脚本的输出)  10-04 00:12  exit 0  → `logs/F103_amt_dw_decay_rev1.log`

## 已写的 notes(`notes/F103_amt_dw_decay/`)

`01_expression.md`(3K)、`02_operators.md`(2K)、`03_decomposition.md`(1K)、`04_grammar.md`(1K)、`05_hypotheses.md`(10K)、`06_baseline.md`(3K)、`07_S1_structure.md`(4K)、`07_S2_distil.md`(5K)、`07_SA_audit.md`(1K)、`07_S_final.md`(2K)、`07_conditional.md`(1K)、`07_controls.md`(1K)、`07_neutralise.md`(2K)、`07x_x1_anatomy.md`(5K)、`07x_x2_interaction.md`(8K)、`07x_x3_family.md`(14K)、`07x_x4_audit.md`(7K)、`07x_x5_rev1.md`(10K)、`08_variants.md`(2K)、`09_diagnosis.md`(14K)、`10_distilled.md`(22K)、`11_risks.md`(4K)、`12_next.md`(2K)、`journal.md`(4K)、`state.md`(9K)、`synthesis.md`(18K)

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
- `synthesis.json`
- `verdict.json`

报告:`research/alpha_distillation/F103_amt_dw_decay.md`(10-04 12:08 生成)
