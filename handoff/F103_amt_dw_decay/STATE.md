# F103_amt_dw_decay — 交接状态

_自动生成于 2026-10-05 13:33(`python scripts/recorder.py --brief F103_amt_dw_decay` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #820(批次 B01_single_factors)
- 表达式:`cross_max(mul(day_close(Amt), ts_min(pow_3(day_durbin_watson(cross_decay_linear(Amt, 30))), 1)), 5)`

## 现在到哪一步

- **阶段:全部完成**
- **留出段已经读过 2 次**(10-03 23:26, 10-05 12:09)—— **不许再读**。候选在留出段上的数全在 `runs/F103_amt_dw_decay/final.json`(`./scripts/study.sh digest F103_amt_dw_decay final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `audit-mechanism:F103_amt_dw_decay`:已返回结果,最后动作 10-04 00:01 → `handoff/F103_amt_dw_decay/agents/audit-mechanism_a4b7f0588d11e04ba.md`
  - `revise:F103_amt_dw_decay`:已返回结果,最后动作 10-04 00:29 → `handoff/F103_amt_dw_decay/agents/revise_ae84c8cd59be0697d.md`
  - `synth:F103_amt_dw_decay`:已返回结果,最后动作 10-05 11:29 → `handoff/F103_amt_dw_decay/agents/synth_a9e8c11a43c18aade.md`

**接手的人该做什么:** 这条因子做完了。最终结论在 `handoff/F103_amt_dw_decay/results/` 里最新的那个(revised.json 优先,否则 study.json)。

## 研究现状(`notes/F103_amt_dw_decay/state.md`,10-05 11:26 更新)—— **先读这个文件**

# F103_amt_dw_decay — 研究现状(主研覆盖重写,2026-10-05,读完批量扫描 s1 大表 + 市场解剖之后)

原式:`cross_max(mul(day_close(Amt), ts_min(pow_3(day_durbin_watson(cross_decay_linear(Amt, 30))), 1)), 5)`(挖掘库 #820)
口径:**只看多头腿扣 15bp 净超额(Lnet)+ 纯多头夏普(Lshp)**,半衰期按纯多头书选。噪声 ±3 点 / ±0.3。门槛 cov ≥ 0.95、dist ≥ 0.5。

---

## 1. 现状

**结论已经定了,而且是否定的:这棵树在已知成交额族之外没有可交易的多头腿增量。**

- `v_base` tr/va/ut = **+9.4% / +4.5% / +8.1%**,Lshp 1.86 / 0.73 / **1.49**,LTO 4.0%,sg = −1,hlL = 10,ρk +0.34。
- `k_known = cross_mean(day_std(Amt), 30)` = **+12.6% / +22.3% / +15.4%**,Lshp 1.78 / 3.46 / **2.22**,LTO 3.4%。
- s1 的 126 个变体里**没有一个** ut Lnet 超过 +15.4%,也没有一个 ut Lshp 显著超过 2.22(最好的 `ov_p10` 是 2.25,差 +0.03 = 噪声的 1/10,而净超额低 2.9 点、换手翻倍)。
- 决定性证据:`res_known`(对已知族取截面秩残差)valid **−2.1%**、Lshp **−0.27**。正交部分样本外是负的。

第二批 36 条假设已写进 `studies/F103_amt_dw_decay/hypo.yaml`(36/36 通过 `study.sh hypo`),**目的已经不是救这条因子,而是去拿解剖挖出来的两块没人用的钱**。
完整推理在 `notes/F103_amt_dw_decay/synthesis.md`(130 行)。

## 2. 中间结果(全部来自 s1 大表,id 可直接在 `study.sh table F103_amt_dw_decay s1` 里查)

- **`ts_min(·,1)` 是恒等式**:`abl_E` 与 `v_base` 逐列相同、ρo 1.00。树里有一个纯摆设节点。
- **`day_durbin_watson` 不是 DW**:分母 `Σx²` 不是 `Σ(x−x̄)²`。对正值序列 ≈ `var(Δx)/(mean²+var)`,即**无尺度的尖峰占比**;恒 ≥ 0
  (`sub_D_abs_` 与 `abl_D` 逐列相同 = 证据)。与前期研究「C 九成是开盘第一分钟成交占比」一致。记 **C** = 这一层。
- **`cross_decay_linear(Amt,30)` 是跨日的**:对每个分钟槽做 30 日线性衰减均值 → 一条「平均日内成交曲线」,不是日内衰减。
- **指数阶梯 = 全表主轴,与 ρk 单调同向**:pow_05 (ρk .90) ut +13.7% → pow_1 (.84) +12.8% → pow_1.5 (.73) +11.4% → pow_2 (.59) +10.0%
  → pow_2.5 (.46) +8.8% → pow_3 (.34) +8.1%。train Lshp 走反方向(1.64→1.96)⇒ **pow_3 是拟合在 train 上的**。
- **承重的只有 `day_close(Amt)`**:`iso_A` 单独 ut **+13.4% / 1.90**(比原式好);C 腿单独 `iso_E` / `only_F_R` valid **−18.6% / −17.8%**,ut Lshp 0.05 / 0.04。
- **不能删的只有 B 槽的 30 日平滑**:`abl_B` ut −3.3% / −0.60。平滑方式本身不敏感(cross_max 版 +8.1%、60 日 +8.4%)。
- **外层 G 槽是自由参数**:`iso_F` +8.5%、`win_G_10/15` +8.5/+8.4、`sub_G_*` 全在 +8.2~+8.4(只有 argmax/argmin 毁掉,dist 0.00 ✗)。
- **叶子**:A 槽 close ↔ mean = sum ↔ quantile = median(+10.0%),都一样;**Amt→Volume 死**(valid −7.4%),**Amt→in_pct(Amt,1) 死**(ut +0.2%)
  ⇒ 要的是**金额水平**,不是活跃度、不是变化率。`rank_F`(两腿各自排名再相乘)ut −0.1% ⇒ 起作用的是 Amt 的重尾量级不是序。
- **形状层全部无用**:rk 7.6%、win 8.1%、rel60 0.7%、fold_sq/fold_mean −22.3%/−25.6%、mem_zscore5/10 为负且换手 11~14%。

## 3. 过程与逻辑(解剖:为什么说「没有增量」却还值得做第二批)

- **次新段**(占 7.1%,段等权 −28.7%):段内净超额随指数单调 pow_05 −2.7% → pow_1 +4.1% → pow_1.5 +15.0% → pow_2 +19.1% → **pow_3 +25.3%**(k_known +8.6%),
  **与全市场完全相反**。推断:次新票日内成交曲线极端不稳,尖峰占比在这群票里有分散度也有含义(最尖 = 游资追的投机壳);成熟票里它退化成持久标签。
  书只在该段超配 +4.2pp,所以这 +25.3% 被稀释掉了。
- **流动半边**(成交额 20 日分档):`v_base` 段内 −6.4 / −2.0 / −0.1 / **+9.6 / +17.2%** 单调升;`k_known` −4.1 / −5.3 / −8.2 / −5.2 / +2.5(几乎零)。
  但段等权是 +15.1 … −17.8%,`k_known` 在最清淡档超配 **+80.3pp** ⇒ **k_known 的钱全是流动性倾斜,原式的钱一半倾斜、一半是流动半边的桶内分辨力**。
  推断:桶内挑低成交额 = 挑**近期缩量**;流动票里是信息,清淡票里是最小变动价位噪声,所以符号翻转。
- **冻结盘口段**(占 6.5%,段等权 **−67.4%**):完全不碰约值 +4%/年。原式是全表低配最多(−4.5pp)也是段内唯一不亏(+0.5%,k_known −10.9%)
  ⇒ **C 腿有一部分就是在当一字板筛子**,但很弱;现在有 `day_zero_ratio / day_flat_run_max` 可以直接写。
- **状态互补**:逐年 `v_base` +4.0/+15.8/+15.4/+2.5/+8.2/−1.4 与 `k_known` +17.3/+10.4/+6.7/+16.1/+24.7/+18.5 近乎反相;
  原式是唯一跌市更好的变体(+10.4% vs 涨市 +6.4%;k_known 是 +6.0% vs +23.0%)。
- **市值**:段内 `v_base` 平(+7.9…+5.8),`k_known` 单调降到 **+0.7%** ⇒ 大票端是原式唯一比已知族强的地方。板块上超配科创板 +10.4pp 是纯损失(该板段内最差)。

## 4. 假设表

`studies/F103_amt_dw_decay/hypo.yaml` —— 36 条,全部通过 `./scripts/study.sh hypo F103_amt_dw_decay`。五组:

| 组 | 条数 | 在检验什么 |
|---|---|---|
| A `h_C_*` | 10 | C 到底读的是什么:相对抖动 / 峰值占比 / gini 一次方 / centroid 顺序信息 / 去持久水平 / 叶子换 Ret·Volume / B 槽换 EMA / 平滑与读形状的顺序 |
| B `h_*age*`, `h_*_ex_new` | 6 | C 的信息是不是只在次新(年龄桶内中性化作判据);`cross_valid_count` 做次新剔除器叠在 K 上 |
| C `h_*frz*` | 7 | 冻结盘口剔除器(`day_zero_ratio` / `day_flat_run_max` + `cs_last_high20`)。**本批最可能直接超过 K 的一族** |
| D `h_contract*`, `h_liq40_*`, `h_bk_liq_*` | 7 | 流动半边 + 缩量机制显式化;补上 `bk_liq` 漏掉的指数 1 版本 |
| E `h_K_*` | 6 | 已知族自己的升级:cs_winsor+cross_ema、tail_mean q25/q75、以及两条低相关候选 `day_wmean(Ret,Amt)` / `day_signed_ratio(Ret,Amt)` |

## 5. 候选(当前)

本轮**不推荐任何从这棵树出来的候选**。按现有证据,这条因子线的最佳单体仍然不如 `k_known`:

| | ut Lnet | ut Lshp | 备注 |
|---|---|---|---|
| `k_known` | +15.4% | 2.22 | 基准,未被超越 |
| `sub_D_pow_05` | +13.7% | 2.08 | 这棵树的最佳单体,ρk 0.90 —— 本质就是已知族 |
| `abl_D` | +12.8% | 2.11 | 同上,ρk 0.84 |
| `v_base` | +8.1% | 1.49 | 原式 |

真正的候选等 s2 跑完再定,先验上最可能的是 C 组(K + 冻结盘口剔除)和 E 组的 `h_K_tail_q25` / `h_K_winsor_ema30`。

## 6. 后面的思路

1. s2 跑完先看三件事:(甲) `h_K_ex_frz` / `h_K_ex_frzrun` 有没有在 K 上加出 ≥ +3 点且 valid 不掉 —— 这是最便宜的增量;
   (乙) `h_base_bk_age` vs `h_abl_bk_age` 的差 —— 判定「C 的信息只在次新」;(丙) `h_C_peakshare` 能不能以 2 个算子复制 `abl_D`。
2. 若 (甲) 成立,下一批应把剔除器做成一个独立小研究(门槛怎么设、剔多少、与换手率 / 涨停史的重叠),而不是继续挂在 F103 下面。
3. 若 (乙) 成立(C ≈ 次新投机指纹),正确的产品是「次新段内的投机度排序」+ 全市场剔除次新,而不是把 C 乘进全市场的成交额因子。
4. 不要再扫窗口:B 槽 30/60、G 槽 5/10/15 都已经是平台,没有脊。

## 7. 留出段

**已经被读过一次**(台账:holdout 1 次、5 条表达式、`S_final`,见 `notes/F103_amt_dw_decay/10_distilled.md` 的修订说明)。
事前登记的推荐是 `f_std9_k1 = mul(cross_max(day_std(Amt), 9), C)`;原报告在读完之后改选 `f_sum_k2`,修订版已把推荐改回 `f_std9_k1`。
**本轮(批量扫描 s1 + 市场解剖 + 第二批假设)没有碰留出段,一格都没有读。** 后续任何一轮都不要再读:这条因子线的留出段额度已经用完,
新的留出段读取只应发生在一条**结构不同的新因子**(例如冻结盘口剔除器)立项之后。

## 8. 给接手者的提醒

- **别按名字理解算子。** 这棵树里有两个陷阱:`day_durbin_watson` 不是 DW(分母是 Σx²,实际是尖峰占比),`ts_min(·,1)` 是恒等式。
  `cross_*` 沿**交易日轴**滚(逐分钟槽),不是截面;`day_close(Amt)` 是**收盘那一分钟的成交额**,不是收盘价。
- **ρk 低不等于独立。** 本例 ρk 只有 0.34,但残差化之后样本外是负的。判「有没有增量」要看 `res_known` / overlay 行,不看 ρk。
- **「段内很好」不等于能用。** 次新段内 +25.3% 是全表最漂亮的数字,但该段只占 7.1%、段等权 −28.7%,全市场书里什么都不剩。
  读解剖表一定要把「段内」「括号里的超配」「段等权超额」三个数一起看。
- **train 夏普与 valid 夏普反向的节点就是过拟合节点**(这里是 pow_3:train 1.86 / valid 0.73,而 pow_05 是 1.64 / 3.37)。
- 想重跑表:`cd /Users/wxy/Desktop/Partura && ./scripts/study.sh table F103_amt_dw_decay s1`(加 `--all` 看全部 126 个);
  算子定义:`./scripts/study.sh src <算子名>`;新算子清单:`docs/new_operators.md`。
- 前期(逐轮小样本)研究的结论在 `notes/F103_amt_dw_decay/0*–12_*.md`,与本轮大表**不矛盾**(它也判了「没有增量」),但它的数字口径更旧,引用请以本轮为准。

## 研究日志(`notes/F103_amt_dw_decay/journal.md`:1 条,其中研究员自己写的 1 条)

最近的 5 条(更早的和全文看文件):

### 2026-10-05 11:26 [主研] 批量扫描 s1 的综合

- 原式逐层读完:`day_durbin_watson` 的分母是 Σx² 不是 Σ(x−x̄)²,它不是 DW 而是**无尺度的尖峰占比**(恒 ≥ 0:`sub_D_abs_` 与 `abl_D` 逐列相同);`ts_min(·,1)` 是**恒等式**(`abl_E` 与 `v_base` 逐列相同);`cross_decay_linear(Amt,30)` 是**跨日**的分钟槽平滑,不是日内衰减。
- 承重的只有 `day_close(Amt)`:`iso_A` 单独 ut +13.4% / Lshp 1.90(**比原式 +8.1% / 1.49 更好**);C 腿单独 `iso_E` / `only_F_R` 的 valid 是 −18.6% / −17.8%。外层 `cross_max(·,5)` 是自由参数(iso_F +8.5%,sub_G_* 全在 +8.2~+8.4)。唯一不能删的是 B 槽的 30 日平滑(`abl_B` ut −3.3%)。
- 指数阶梯与 ρk 单调同向 = 全表主轴:pow_05(ρk .90)+13.7% → pow_1(.84)+12.8% → pow_1.5(.73)+11.4% → pow_2(.59)+10.0% → pow_2.5(.46)+8.8% → pow_3(.34)+8.1%,而 train Lshp 走反方向(1.64→1.96)⇒ **pow_3 是拟合在 train 上的**。
- 相对已知族**没有增量**:`res_known` valid −2.1% / Lshp −0.27;overlay 最好一档 `ov_p10` 夏普只高 +0.03(噪声 ±0.3)而净超额低 2.9 点、换手翻倍;126 个变体没有一个 ut Lnet 超过 k_known 的 +15.4%。
- 解剖的三块可用发现:(1) 次新段(7.1%,段等权 −28.7%)段内随指数单调 −2.7% → **+25.3%**,与全市场完全相反 ⇒ C 是次新投机指纹;(2) 原式的选股力在成交额最高两档(段内 +9.6% / +17.2%,k_known 只有 −5.2% / +2.5%),而 k_known 的钱全是流动性倾斜(最清淡档超配 +80.3pp);(3) 冻结盘口段占 6.5%、段等权 **−67.4%**,全不碰约值 +4%/年,原式低配最多(−4.5pp)也是段内唯一不亏(+0.5%)。
- 第二批 36 条假设已落盘
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
- `x1`(自写脚本的输出)  10-03 19:40  exit 0  → `logs/F103_amt_dw_decay_x1.log`
- `x2`(自写脚本的输出)  10-03 19:56  exit 0  → `logs/F103_amt_dw_decay_x2.log`
- `x3`(自写脚本的输出)  10-03 23:04  exit 0  → `logs/F103_amt_dw_decay_x3.log`
- `audit1`(自写脚本的输出)  10-03 23:54  exit 0  → `logs/F103_amt_dw_decay_audit1.log`
- `rev1`(自写脚本的输出)  10-04 00:12  exit 0  → `logs/F103_amt_dw_decay_rev1.log`

## 已写的 notes(`notes/F103_amt_dw_decay/`)

`01_expression.md`(3K)、`02_operators.md`(2K)、`03_decomposition.md`(1K)、`04_grammar.md`(1K)、`05_hypotheses.md`(10K)、`06_baseline.md`(3K)、`07_S1_structure.md`(4K)、`07_S2_distil.md`(5K)、`07_SA_audit.md`(1K)、`07_S_final.md`(2K)、`07_conditional.md`(1K)、`07_controls.md`(1K)、`07_neutralise.md`(2K)、`07x_x1_anatomy.md`(5K)、`07x_x2_interaction.md`(8K)、`07x_x3_family.md`(14K)、`07x_x4_audit.md`(7K)、`07x_x5_rev1.md`(10K)、`08_variants.md`(2K)、`09_diagnosis.md`(14K)、`10_distilled.md`(22K)、`11_risks.md`(4K)、`12_next.md`(2K)、`journal.md`(2K)、`state.md`(9K)、`synthesis.md`(11K)

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

报告:`research/alpha_distillation/F103_amt_dw_decay.md`(10-04 12:08 生成)
