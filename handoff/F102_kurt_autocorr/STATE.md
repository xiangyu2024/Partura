# F102_kurt_autocorr — 交接状态

_自动生成于 2026-10-05 13:33(`python scripts/recorder.py --brief F102_kurt_autocorr` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #3961(批次 B01_single_factors)
- 表达式:`cross_sum(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 15)`

## 现在到哪一步

- **阶段:全部完成**
- **留出段已经读过 2 次**(10-03 23:15, 10-05 12:16)—— **不许再读**。候选在留出段上的数全在 `runs/F102_kurt_autocorr/final.json`(`./scripts/study.sh digest F102_kurt_autocorr final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `audit-mechanism:F102_kurt_autocorr`:已返回结果,最后动作 10-03 23:38 → `handoff/F102_kurt_autocorr/agents/audit-mechanism_a2d310a359bfeff69.md`
  - `revise:F102_kurt_autocorr`:已返回结果,最后动作 10-04 00:24 → `handoff/F102_kurt_autocorr/agents/revise_a39c89bd8b2569636.md`
  - `synth:F102_kurt_autocorr`:已返回结果,最后动作 10-05 11:30 → `handoff/F102_kurt_autocorr/agents/synth_a93191635af758ebb.md`

**接手的人该做什么:** 这条因子做完了。最终结论在 `handoff/F102_kurt_autocorr/results/` 里最新的那个(revised.json 优先,否则 study.json)。

## 研究现状(`notes/F102_kurt_autocorr/state.md`,10-05 11:27 更新)—— **先读这个文件**

# F102_kurt_autocorr —— 研究现状(主研,批量扫描 s1 之后重写)

`cross_sum(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 15)` · sg = −1(多头 = 低值) · 挖掘库 #3961
选拔口径:多头腿扣 15bp 净超额 + 纯多头夏普,半衰期按纯多头书选。噪声 ±3 个点 / ±0.3 夏普。

## 1. 现状

一轮批量扫描(94 个变体)+ 市场解剖已读完,综合在 `notes/F102_kurt_autocorr/synthesis.md`,
第二批 40 条假设在 `studies/F102_kurt_autocorr/hypo.yaml`(`study.sh hypo` 40/40 通过),等下一轮扫描。
**留出段已经被上一轮研究员读过一次(`07_S_final`,台账里记着),这一轮没有再读,以后也不能再读。**

当前判断:**它不是一条可以独立上的纯多头因子**(utrain 多头净超额 +8.9% / 夏普 2.05,已知成交额族
`cross_mean(day_std(Amt), 30)` 是 +15.4% / 2.22),但它**不是已知族的重写**(ρk = +0.26),
作为小权重配角能把已知族的夏普从 2.22 抬到 2.5~2.6 而净超额不降。价值约 +0.3 夏普,在噪声沿。

## 2. 中间结果(数字全部来自 `study.sh table F102_kurt_autocorr s1 --all`)

| 变体 | Lnet tr/va/ut | Lshp ut | LTO | ρo | ρk | 说明 |
|---|---|---|---|---|---|---|
| `v_base` | +8.5 / +9.8 / +8.9% | 2.05 | 5.4% | 1.00 | 0.26 | 原式,hl 5 |
| `k_known` | +12.6 / +22.3 / +15.4% | 2.22 | 3.4% | 0.26 | 1.00 | 基准 |
| `sub_D_cross_mean` | +10.1 / +10.3 / +10.2% | **2.32** | 5.2% | 0.99 | 0.27 | 提纯:不再把缺失日记 0 |
| `sub_D_cross_decay_linear` | +11.0 / +10.6 / +10.9% | 2.21 | **2.4%** | 0.79 | 0.18 | 换手减半 |
| `sub_D_cross_ema` | +11.1 / +10.0 / +10.8% | 2.20 | **2.1%** | 0.81 | 0.20 | 换手最低 |
| `mem_mean60` | +10.6 / +11.5 / +10.8% | **2.31** | 2.7% | 0.88 | 0.25 | 全表最佳单因子 |
| `ov_p05` | +13.6 / +19.6 / +15.3% | **2.62** | 4.7% | 0.53 | 0.92 | 叠在已知族上,权重 0.5 |
| `iso_C` | +8.7 / +6.1 / +8.0% | 1.61 | 6.2% | 0.80 | 0.18 | 整个 D 层删掉,只靠书的 hl 20 |
| `abl_C`(无 pow_2) | −6.3 / +1.8 / −4.0% | −0.71 | 1.6% | **0.00** | 0.00 | 折叠承重的证据 |
| `win_A_5` / `win_A_10` | +1.5% / −3.1%(ut) | 0.42 / −0.63 | — | 0.74 / 0.54 | — | 3 分钟孔径没有平台 |

解剖的关键数(全市场多头书,utrain):
- 成交额 20 日五分位 **段内**净超额 = −2.9 / −4.3 / −0.3 / +6.1 / **+12.4%**(单调上升),书对最低桶**超配 +21.1 个点**。
- 「超配 × 段等权超额」点乘:**原式 +5.5 个点来自跨成交额桶倾斜**(占 +8.9% 的六成),`k_known` **+14.7 个点**(占 95%)。
- 冻结盘口段(6.5%、段等权 −67.4%):原式低配 −5.0 → **+3.6 个点**;`k_known` 低配 −2.9 → +2.1 个点。无冻结池内原式只 +5.5%、已知族 +14.1%。
- 科创板(4.0%、段等权 +4.1%):原式**段内 −28.5%** 且**超配 +8.3 个点**(书里 12.3% 仓位);换 `cross_mean` → **+3.0%**。
- 上市不足 250 日(7.1%、段等权 −28.7%):原式 +7.1% → `cross_mean` **+23.5%** / `cross_decay_linear` +25.5%。
- 年度 2018→2023:+8.1 / +11.1 / +9.3 / +5.6 / +10.3 / +9.3%(**无衰减**)。放量 +13.3% vs 缩量 +5.4%;上涨 +13.2% vs 下跌 +3.8%。

## 3. 过程与逻辑(为什么这么读)

1. 算子定义先读代码:`nankurt_last = m4/(var²+EPS) − 3` → `day_kurt` 是**超额**峰度,下界 −2;
   `sub_C_pow_1_5`(`x**1.5`,负数 → NaN)cov 掉到 **0.75** → **25% 的股票-日峰度为负**,这是「可以为负」的直接量测。
2. `pow_2 = pow_(x,2)`,`e>1` 走 `x**e` 分支,**不是**带符号幂 → 它是一个**折叠**。因为超额峰度 ≥ −2,平方把薄尾侧硬顶在 ≤ 4、
   把尖峰侧放大到无穷,实质是 `max(kurt,0)` 的凸版本。所以 `abs_` 能保住 ρo 0.96 而保号的全部归零。
3. `ts_corr` 的分母是 `sqrt(var_x·var_y) + EPS`:窗口内分钟收益全相等(封板 / 停牌 / 无成交)时 var = 0,
   相关**恰好 = 0**。d = 3 时这个退化出口最容易被走到 —— 这解释了为什么孔径 3→5→10 会塌(+8.9 → +1.5 → −3.1%),
   以及为什么整棵树读到的是「冻结盘口」而不是任何自相关。
4. `cross_sum` 用 `nansum_last`(NaN 当 0),`cross_mean` 用 `nanmean_last`(跳过 NaN)。sg = −1 下低 = 买,
   所以 `cross_sum` 系统性**买进**历史不全的票 —— 解剖里科创板 / 次新两段的证据与这条机制完全对上。
5. 「总平滑量守恒」:`iso_C` hl 20、原式 hl 5、`mem_mean60` hl 0,净超额都落在 +8~+11% → 外层 cross 层主要在做平滑,
   信息在单日的 `pow_2(day_kurt(·))` 里。真杠杆是**换手**:同窗口换聚合器就能把 LTO 从 5.4% 压到 2.1%,约 2 个点净超额。

## 4. 假设表(第二批,`studies/F102_kurt_autocorr/hypo.yaml`,40 条)

| 组 | 条数 | 在问什么 |
|---|---|---|
| A 证伪自己 | 7 | 整棵树是不是就等于 `day_zero_ratio(Ret)` / `day_flat_run_max(Close)`;两个方向的 `cs_regres` 残差都跑 |
| B 修缺失日 + 慢化 | 7 | `cross_ema 30/60`、`cross_decay_linear 60`、`cross_max 60`(上一轮推荐式,本表缺)、内层换 mean 的 `mem_mean60`、`cross_tail_mean_q25/q75` |
| C 停牌 / 次新写进表达式 | 2 | `cross_valid_count` 做剔除器 / 分桶,量出科创板那 −28.5% 有多少是 NaN 当 0 |
| D 换掉 3 分钟孔径 | 5 | `in_autocorr_s1`(严格日内,不跨日)、`in_madz`(相对 EPS)、`nt_ts_corr(Ret, Amt, 3)` |
| E 折叠 vs 凸性 | 5 | `abs_` / `sigmoid` / `cs_winsor` / 四次方 / 折叠点挪到截面均值 |
| F 桶内选股 | 4 | 成交额桶、个股放量倍数桶、价格桶;`cs_first_low40` 剔掉最不活跃 40% |
| G 当配角 / 筛子 | 5 | 提纯式 / 低换手式 / 桶内式分别叠在已知族上;`cs_first_high40` 当筛子;用全市场放量倍数调权重 |
| H 新结构 | 5 | `day_centroid(Amt)`、`day_gini`、`day_signed_ratio(Ret, Amt)` —— 不含峰度的封板计 |

## 5. 候选(只凭 train / valid;不许再读留出段)

1. `cross_mean(cross_mean(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 15), 60)`(= `h_meanmean60`)—— 预期最佳:
   把全表最佳 `mem_mean60`(+10.8% / 2.31)的内层缺陷修掉。
2. `cross_ema(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 30)`(`h_ema30`)—— 换手最低的一支,窗口 15 已有 +10.8% / LTO 2.1%。
3. `add(cs_rank(cross_mean(day_std(Amt), 30)), mul(cs_bucket_rank(…, cross_mean(day_std(Amt), 30)), 0.5))`(`h_ov_bucket_p05`)
   —— 只把与已知族正交的那一半叠上去;**这是最符合口径的用法**。
4. 上一轮的推荐式 `cross_max(pow_2(K), 60)`(`h_max60`)—— 必须有这一行才能把两轮对齐。

## 6. 后面的思路

- 若 A 组的残差塌(`h_res_zero60` 掉到 0 附近):结论定为「已知族 + 一个封板掩码」,**这棵树可以退休**,
  把 `cross_max(day_zero_ratio(Ret), 60)` 作为更便宜、更可解释的替代交出去。
- 若 D 组的 `in_madz` / `in_autocorr_s1` 出现窗口平台:说明机制真实、原式只是用了一个脆的估计量,
  下一轮应围绕稳健写法重建,而不是继续修原式。
- 若 F 组的桶内排名保住 ≥ +5% 且夏普 ≥ 1.5:那部分就是真正的增量,直接走 G 组的叠加路线。
- 没做的:多空腿(空头腿毛超额 +28.0% / +23.3%,钱大量在空头腿,但用户只做纯多头,不追)。

## 7. 留出段

- 用户训练段 = 20180102–20230807(train 2018–2021 + valid 20220101–20230807)。本轮**没有读留出段**。
- 上一轮研究员已用掉那一次读取(`07_S_final`,5 个候选 × 2 行半衰期 = 10 个数)。**台账已记,不得再读。**
- 本轮所有结论、候选排序、判据都只用 train / valid。

## 8. 给接手者的提醒

- **先读 `notes/F102_kurt_autocorr/synthesis.md`**,再看本文件第 2 节的表。`10_distilled.md` 是上一轮的报告,
  它的「候选 / 推荐 `f_max60`」仍然可参考,但那是小样本逐轮实验的结论;**以这次的 94 变体大表为准**。
- 三个最容易踩的误解:(a)`day_kurt` 是**超额**峰度、可以为负;(b)`pow_2` 在这里是**折叠**不是放大;
  (c)这棵树与「自相关」无关,`nt_ts_autocorr_s1(Ret, 3)` 在 var = 0 时靠分母的 EPS 吐出恰好的 0,整棵树是封板 / 停牌探测器。
- `cross_sum` vs `cross_mean` 的差别**不是风格问题**,是「缺失日当 0 + sg=−1 → 买历史不全的票」这个实打实的缺陷,
  科创板和次新两段的数字就是它的指纹。任何新变体都应该用 `cross_mean` 系的聚合器写。
- 表里 `cs_bucket_rank` 的两行(`bk_liq` / `bk_known`)dist = 0.20 ✗,是并列导致的离散度误杀;
  `docs/new_operators.md` 说该算子已加全局秩 ×1e-4 打破并列,**第二批里的 `cs_bucket_rank` 行应当不再被误杀**;若仍 ✗,先去查算子版本。
- 不要去追多空夏普(原式 +3.68 / +3.88,很漂亮),用户口径只看多头腿扣费净超额与纯多头夏普。

## 研究日志(`notes/F102_kurt_autocorr/journal.md`:1 条,其中研究员自己写的 1 条)

最近的 5 条(更早的和全文看文件):

### 2026-10-05 11:26 [主研] 批量扫描 s1 的综合

- 读完 s1 大表 94 个变体 + 市场解剖,综合写进 notes/F102_kurt_autocorr/synthesis.md;第二批 40 条假设写进 studies/F102_kurt_autocorr/hypo.yaml(40/40 parse)。
- 它是什么:day_kurt 是**超额**峰度(nankurt_last = m4/var²−3,sub_C_pow_1_5 的 cov=0.75 直接量出 25% 的股票-日为负);nt_ts_autocorr_s1(Ret,3) 只用 4 根分钟收益算相关,窗口内收益全相等时分母的 EPS 让它**恰好吐 0**。所以整棵树 = 封板/停牌/死盘口探测器,与「自相关」无关。pow_2 是折叠(删掉 ρo=0.00、−4.0%),孔径 3 是刀尖(5→+1.5%、10→−3.1%,无平台)。
- 承重 = {3 分钟孔径, autocorr 槽位, day_kurt 槽位, pow_2 折叠, Ret 叶子};多余 = 外层 cross_sum(iso_C 单日 + hl20 已有 +8.0%,总平滑量守恒);窗口 5–60 是平台;真杠杆是换手(cross_ema/decay_linear 把 LTO 从 5.4% 压到 2.1%,净超额 +10.8/+10.9%)。
- cross_sum 把缺失日算成 0 + sg=−1 → 系统性买历史不全的票:科创板段内 −28.5%(书里压 12.3% 仓位)换 cross_mean → +3.0%;次新段 +7.1% → +23.5%。这是全表最便宜的修复。
- 「超配 × 段等权超额」点乘:原式 +5.5 个点来自跨成交额桶的倾斜(占 +8.9% 的六成),k_known +14.7(占 95%);冻结盘口段原式 +3.6、k_known +2.1。段内预测力随成交额单调上升(−2.9/−4.3/−0.3/+6.1/+12.4%)。年度极稳(5.6–11.1%,无衰减),放量 +13.3% vs 缩量 +5.4%。
- 相对已知族:ρk=0.26,但 res_known +3.7%、bk_known +4.0% → 独立上不行(8.9 vs 15.4)。小权重叠加 0.25/0.5/1.0 夏普 2.51/2.62/2.57 对 2.22,反号变坏 → 符号对、量在噪声沿。定性结论:**不是独立纯多头因子,是已知族的减波动配角(约 +0.3 夏普),最可能来源是那 1.5
…(这条日志还有后文,读 journal.md)

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
- `sweep_s2`  10-05 12:12  146 个变体  → `./scripts/study.sh digest F102_kurt_autocorr sweep_s2`
- `anatomy_s2`  10-05 12:16  0 个变体  → `./scripts/study.sh digest F102_kurt_autocorr anatomy_s2`
- `sweepfinal_s2`  10-05 12:18  8 个变体  → `./scripts/study.sh digest F102_kurt_autocorr sweepfinal_s2`
- `x1`(自写脚本的输出)  10-03 19:32  exit 0  → `logs/F102_kurt_autocorr_x1.log`
- `x2`(自写脚本的输出)  10-03 20:05  exit 0  → `logs/F102_kurt_autocorr_x2.log`
- `x3`(自写脚本的输出)  10-03 23:04  exit 0  → `logs/F102_kurt_autocorr_x3.log`
- `audit1`(自写脚本的输出)  10-03 23:33  exit 0  → `logs/F102_kurt_autocorr_audit1.log`
- `rev2`(自写脚本的输出)  10-04 00:04  exit 97  → `logs/F102_kurt_autocorr_rev2.log`

## 已写的 notes(`notes/F102_kurt_autocorr/`)

`01_expression.md`(2K)、`02_operators.md`(3K)、`03_decomposition.md`(3K)、`04_grammar.md`(1K)、`05_hypotheses.md`(11K)、`06_baseline.md`(1K)、`07_S1_layers.md`(3K)、`07_S2_windows.md`(2K)、`07_S3_aggregate.md`(5K)、`07_SA_audit.md`(1K)、`07_SR_horizon.md`(4K)、`07_S_final.md`(4K)、`07_conditional.md`(2K)、`07_controls.md`(1K)、`07_neutralise.md`(4K)、`07x_1_anatomy.md`(8K)、`07x_2_refine.md`(5K)、`07x_3_longleg.md`(8K)、`07x_4_audit.md`(6K)、`07x_5_revision.md`(11K)、`07x_anatomy.md`(1K)、`07x_longleg.md`(1K)、`07x_refine.md`(1K)、`08_variants.md`(3K)、`09_diagnosis.md`(8K)、`10_distilled.md`(12K)、`11_risks.md`(4K)、`12_next.md`(2K)、`journal.md`(2K)、`state.md`(8K)、`synthesis.md`(11K)

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
- `synthesis.json`

报告:`research/alpha_distillation/F102_kurt_autocorr.md`(10-04 12:07 生成)
