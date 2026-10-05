# F101_day_shine_retstd — 交接状态

_自动生成于 2026-10-05 13:33(`python scripts/recorder.py --brief F101_day_shine_retstd` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:手写 day_shine_retstd(批次 B01_single_factors)
- 表达式:`abs_(cs_demean(day_mean(in_sustain_stddev(is_gt(sub(in_slice(Volume, 2, 237), in_delay(in_slice(Volume, 2, 237), 1)), add(in_mean_full(sub(in_slice(Volume, 2, 237), in_delay(in_slice(Volume, 2, 237), 1))), in_stddev_full(sub(in_slice(Volume, 2, 237), in_delay(in_slice(Volume, 2, 237), 1))))), in_slice(Ret, 2, 237), 5))))`

## 现在到哪一步

- **阶段:全部完成**
- **留出段已经读过 2 次**(10-03 23:00, 10-05 11:59)—— **不许再读**。候选在留出段上的数全在 `runs/F101_day_shine_retstd/final.json`(`./scripts/study.sh digest F101_day_shine_retstd final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `audit-mechanism:F101_day_shine_retstd`:已返回结果,最后动作 10-03 23:28 → `handoff/F101_day_shine_retstd/agents/audit-mechanism_a44fe5af2ad163716.md`
  - `revise:F101_day_shine_retstd`:已返回结果,最后动作 10-04 00:02 → `handoff/F101_day_shine_retstd/agents/revise_a7c1f89ef939ebc23.md`
  - `synth:F101_day_shine_retstd`:已返回结果,最后动作 10-05 11:16 → `handoff/F101_day_shine_retstd/agents/synth_ae7cc08a1070145ff.md`

**接手的人该做什么:** 这条因子做完了。最终结论在 `handoff/F101_day_shine_retstd/results/` 里最新的那个(revised.json 优先,否则 study.json)。

## 研究现状(`notes/F101_day_shine_retstd/state.md`,10-05 11:10 更新)—— **先读这个文件**

# F101_day_shine_retstd — 现状(主研,2026-10-05 覆盖重写;以批量扫描 s1 的大表为准)

## 1. 现状

一轮综合已做完:读完 `sweep_s1`(102 个变体)+ `anatomy_s1`(23 个股票段 / 14 个时段),写了
`notes/F101_day_shine_retstd/synthesis.md`(138 行,每条论断带变体 id 和数字)和第二批 40 条假设
`studies/F101_day_shine_retstd/hypo.yaml`(已过 `study.sh hypo`,40/40 parse)。本轮没有起任何服务器计算。
**留出段此前已经被读过一次**(`runs/.../final.json`、`09_diagnosis.md` 第 10 条),不许再读。

结论一句话:**原式 = 「日内分钟收益离散度」在当天截面均值处的 V 形折叠,外面套了一台多余且会失效的放量触发机器。**
按用户口径(多头腿扣费净超额 + 纯多头夏普):任何单体都打不过已知成交额族的净超额(最好 9.7% 对 15.4%),
只在纯多头夏普上更稳(2.68 对 2.22);**作为独立因子对用户没有增量**,唯一还活着的用法是「桶内选股器叠在已知族的 tilt 上」。

## 2. 中间结果(本轮确立的数字)

| 变体 | 掩码 / 改动 | Lnet tr / va / ut | Lshp tr / va / ut | LTO | ρo / ρk |
|---|---|---|---|---|---|
| `v_base` | Δ > μ+σ,hl 10 | +9.0 / −1.6 / +7.1 | 1.96 / −0.38 / 1.37 | 10.4% | 1.00 / 0.14 |
| `k_known` | 基准 | +12.6 / +22.3 / +15.4 | 1.78 / 3.46 / 2.22 | 3.4% | 0.14 / 1.00 |
| `fld_Volume_Amt` | 混单位比较 ≈「有成交额的分钟」,hl 20 | +10.0 / +8.9 / +9.7 | **2.71 / 2.59 / 2.68** | 5.6% | 0.72 / 0.16 |
| `sub_C_mul` | v_t·v_{t−1} > θ ≈ 全部分钟 | +9.3 / +11.6 / +10.0 | 2.29 / 3.10 / 2.51 | 5.2% | 0.69 / 0.18 |
| `abl_F` 一族(5 条) | 阈值退化成 ≈ 0 ⇒ Δ > 0 | +9.0~9.3 / +10.6~11.1 / +9.5~9.8 | 2.2~2.3 / 2.8~3.0 / 2.4~2.5 | 5.2% | 0.66~0.71 / 0.18 |
| `iso_J` = `abl_K` | 不折叠(单调) | −6.8 / +2.1 / −4.2 | −0.81 / +0.28 / −0.52 | 3.1% | 0.18 / 0.35 |
| `rk` | 先 cs_rank 再 EMA | +10.1 / +3.1 / +8.1 | 2.26 / 0.72 / 1.84 | 6.8% | 0.84 / 0.03 |
| `ov_p10` | base 叠已知族(权重 1) | +14.1 / +18.5 / +15.4 | 2.16 / 3.15 / 2.42 | 6.1% | 0.41 / 0.89 |
| `mem_zscore5` | 去掉持久截面水平 | −25.9 / −27.0 / −26.2 | −6.00 / −6.89 / −6.23 | 30.3% | 0.05 / −0.05 |

窗口斜坡 `win_I` 3 / 5 / 10 / 15 → Lshp(ut) 1.20 / 1.37 / 1.85 / 2.03(单调,无峰)。
逐年(utrain 口径):`v_base` +8.1 / +12.4 / +15.4 / **+1.6 / +1.0 / +2.0**;`fld_Volume_Amt` +4.3 / +13.0 / +13.4 / +9.4 / +9.0 / +8.8。
解剖关键段(段内净超额 / 夏普,tilt):流通市值最低20% [0] +16.9% S+2.96 tilt −13.5;20 日成交额最低20% +0.7% S+0.15;
最高20% +20.5% S+2.00(段等权 −17.8%);科创板 −19.4% S−1.01 tilt +2.2;冻结盘口段 [0] +27.5%、稠密族 −6.5~+8.4%。

## 3. 过程与逻辑

1. 先按内核源码逐层写出公式(`study.sh src` 11 个算子),拿到三个"名字骗人"的点:`sustain` = 往后取窗口、
   `abs_` 单独是 no-op(靠 `abl_K ≡ iso_J` 逐位相同坐实)、`abl_G` 的掩码是"Δ 恰好 = 1"。
2. 把 102 个变体按"掩码稠密度"排成一条轴,发现 valid 与半衰期、换手都随稠密度单调改善,而 ρo 从 0.91 掉到 0.66 ——
   这不是噪声,是两个不同的因子。再用逐年表确认:失效发生在 2021,且只发生在稀疏触发版。
3. 解剖表上把"段内分辨力"和"段等权漂移"分开读,得出两条可操作的落差:书被折叠中心推到大票里(小票段内最好却只放 6%),
   以及 16% 的仓位放在零分辨力的清淡段。
4. 把 `k_known` 的段内数字读了一遍(各成交额段 −4 ~ +2.5%),确认它是纯 tilt 收割器 ⇒ 互补性来自"tilt vs 桶内选股",
   于是第二批的 D 组把 overlay / 残差 / 桶内排名全部换成稠密核重做。

## 4. 假设表(第二批 40 条,`studies/F101_day_shine_retstd/hypo.yaml`)

A 最小结构 + 半衰期(8)· B 折叠中心与"用机制替掉折叠"(6)· C 分桶 / 分段(8)· D 已知族增量(5)·
E 被测量互换(5)· F 规范化掩码(2)· G 冻结盘口(2)· H 大胆机制(4)。
每条 `why` 里写了它要证伪哪一条 s1 结论。必跑的对手假设:`h_rv_mono_mean30`(已知族在收益上的孪生兄弟,
若它 ≥ 折叠版,这条因子就只是"已知的波动暴露");伪证实验:`h_rv_own_rel_fold`(预测塌掉)。

## 5. 候选(按现在的证据排序,第二批之前)

1. `fld_Volume_Amt`(表内最好单体):Lshp(ut) 2.68、LTO 5.6%、逐年 2019 后都 ≥ +7.8%。但它的掩码是混单位比较,
   机制上应该写成 `h_gate_amt_above_mean` 或干脆 `h_rv_fold`。
2. `h_rv_fold` / `h_rv_fold_rank_ema30`(第二批):同一机制的最小写法,未验证。
3. `ov_p10` 一类的 overlay —— 只有在稠密核上重做赢出噪声带才算候选。
4. 目前**不推荐**原式:valid −1.6%、2021–2023 多头腿是空的。

## 6. 后面的思路

- 第二批回来后,先看 A 组能不能把触发机器整台删掉(判据:Lshp(ut) ≥ 2.68 且 valid ≥ +8%),再看 C / D 组能不能把
  净超额从 9.7% 推向已知族的 15.4%。
- 若 `h_rv_mono_mean30` 与折叠版打平,就该把这条因子写成"已知波动暴露的非线性写法",研究收口(否定结论同样合格)。
- 还没有人测过的第三批方向:把"投机注意力"用非波动的量来写(H 组的 `day_centroid` / `day_signed_ratio` 若有苗头);
  以及把稠密核与 `k_known` 做"分桶 tilt + 桶内选股"的两层书(需要在 exec 脚本里做,表达式语言写不出两层加权)。

## 7. 留出段

**已经读过一次,不许再读。** 事前推荐 `f_roll5` 的测试段多头净 +6.6%、纯多头夏普 +1.41(原式 +6.0% / +1.32),
4 算子的 `f_ivol` +6.6% / +1.43 / 多空 +3.42 —— "升华没有被样本外支持,最朴素的写法与原式不可区分"
(`09_diagnosis.md` 第 10 条)。第二批的任何赢家都**不能**再去留出段上确认;它只能作为"下一条因子的先验"或等用户另开口径。

## 8. 给接手者的提醒

- 先读 `synthesis.md`(138 行),再读本页;`07x_look*.md` / `09_diagnosis.md` 是前一位研究员的小样本结论,
  有几处(「多头腿越低越好」「低侧悬崖」)已被 s1 大表细化,**以大表为准**。
- `in_sustain_stddev` 的内核只认 `mask == 1.0`;给它喂浮点量会变成"恰好等于 1 的分钟"。读 `abl_*` / `sub_*` 的分数前
  一定先从 `runs/.../sweep_s1.json` 把完整表达式打出来(表里的 expr 列被截断)。
- 两道门槛的坑:`cs_bucket_rank` 在根上 dist 恒约 0.20(十个桶的百分位跨桶重合),不是因子退化;
  需要时用 `h_rv_fold_bk_amt20_tie` 那种 0.001 秩扰动绕过,并在汇报里写明这是工具问题。
- 半衰期网格上限 20 对这一族是边界解;想试更长只能在表达式里写 `cross_ema` / `cross_mean`。
- 混分钟轴宽度会直接报错(236 vs 241):一条表达式里的 `in_*` 叶子要么全切片要么全不切,`day_*` 折叠后再组合才安全。

## 研究日志(`notes/F101_day_shine_retstd/journal.md`:1 条,其中研究员自己写的 1 条)

最近的 5 条(更早的和全文看文件):

### 2026-10-05 11:09 [主研] 批量扫描 s1 的综合

1. 承重的只有两个:截面 V 形折叠(abs_ + cs_demean 必须成对,abl_K 与 iso_J 逐位相同 ⇒ abs_ 单独是 no-op)和「日内收益离散度」这个被测量
   (换 in_corr/in_cov/in_r2、day_first/last、day_skew/gini 全塌到 -0.1 ~ -1.4)。
2. 整台放量触发机器是多余的,而且它就是样本外失效的那一部分:阈值放宽到约 0 / 掩码放稠密后 valid 从 -1.6% 跳到 +8.9~+11.6%、
   Lshp(ut) 1.37 -> 2.4~2.7、换手 10.4% -> 5.2%、最优半衰期 10 -> 20;逐年看 v_base 2021-2023 = +1.6/+1.0/+2.0%,稠密族 = +9~+13%。
   win_I 3/5/10/15 单调上升(1.20/1.37/1.85/2.03)没有峰,证明「5 分钟 + 1σ + Volume」三件事都是装饰。abl_G 的掩码其实是「Δ 恰好=1」
   (内核只认 mask==1.0)却和稠密族逐位接近 ⇒ 掩码近乎任意采样都行,不能读成「删 is_gt 有用」。
3. 市场在哪:小市值段内 S+2.96 却只放书的 6%(tilt -13.5,折叠中心是全市场均值 ⇒ 系统性选大票);20 日成交额最低段零分辨力(S+0.15)
   却占 16% 仓位;最高段段内 +20.5%(段等权 -17.8%,投机溢价);科创板段内 -19.4% 是唯一失效区(20% 涨跌幅让板内分布右移);
   稠密族顺周期(放量 +13.6% vs 缩量 +6.6%、离散度高 +13.8% vs 低 +5.7%)。
4. 增量:ρk 只 0.14~0.18、k_known 几乎没有段内分辨力(纯 tilt 收割器),结构互补;但表里的 overlay 叠的是失效的 v_base,
   utrain 与已知族完全打平(15.4% vs 15.4%,夏普 +0.20 在噪声内)。按净超额任何单体都打不过已知族(9.7% vs 15.4%),
   按纯多头夏普 fld_Volume_Amt 2.68 > 2.22。当前结论:独立因子对用户无增量,唯一还活着的用法是「桶内选股器叠在已知族的 tilt 上」。
5. 第二批 40 条已写入 studies/F101_day_shine_retstd/hypo.yaml 并通过 hypo 检查:A
…(这条日志还有后文,读 journal.md)

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
- `sweep_s1`  10-05 10:42  102 个变体  → `./scripts/study.sh digest F101_day_shine_retstd sweep_s1`
- `anatomy_s1`  10-05 10:49  0 个变体  → `./scripts/study.sh digest F101_day_shine_retstd anatomy_s1`
- `sweep_s2`  10-05 11:47  153 个变体  → `./scripts/study.sh digest F101_day_shine_retstd sweep_s2`
- `anatomy_s2`  10-05 11:58  0 个变体  → `./scripts/study.sh digest F101_day_shine_retstd anatomy_s2`
- `sweepfinal_s2`  10-05 12:01  8 个变体  → `./scripts/study.sh digest F101_day_shine_retstd sweepfinal_s2`
- `look`(自写脚本的输出)  10-03 19:28  exit 0  → `logs/F101_day_shine_retstd_look.log`
- `look2`(自写脚本的输出)  10-03 19:50  exit 0  → `logs/F101_day_shine_retstd_look2.log`
- `look3`(自写脚本的输出)  10-03 22:45  exit 0  → `logs/F101_day_shine_retstd_look3.log`
- `audit1`(自写脚本的输出)  10-03 23:21  exit 0  → `logs/F101_day_shine_retstd_audit1.log`
- `rev2`(自写脚本的输出)  10-03 23:41  exit 0  → `logs/F101_day_shine_retstd_rev2.log`

## 已写的 notes(`notes/F101_day_shine_retstd/`)

`01_expression.md`(1K)、`02_operators.md`(2K)、`03_decomposition.md`(1K)、`04_grammar.md`(1K)、`05_hypotheses.md`(4K)、`06_baseline.md`(3K)、`07_S1_parts.md`(5K)、`07_S2_background.md`(5K)、`07_SA_audit.md`(1K)、`07_SR_rivals.md`(6K)、`07_S_final.md`(2K)、`07_conditional.md`(1K)、`07_controls.md`(1K)、`07_neutralise.md`(2K)、`07x_look.md`(6K)、`07x_look2.md`(4K)、`07x_look3.md`(10K)、`07x_review1_audit.md`(7K)、`07x_review2_rev2.md`(13K)、`08_variants.md`(3K)、`09_diagnosis.md`(13K)、`10_distilled.md`(13K)、`11_risks.md`(4K)、`12_next.md`(2K)、`journal.md`(2K)、`state.md`(6K)、`synthesis.md`(13K)

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
- `synthesis.json`

报告:`research/alpha_distillation/F101_day_shine_retstd.md`(10-04 12:07 生成)
