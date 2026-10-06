# F101_day_shine_retstd — 交接状态

_自动生成于 2026-10-05 17:10(`python scripts/recorder.py --brief F101_day_shine_retstd` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:手写 day_shine_retstd(批次 B01_single_factors)
- 表达式:`abs_(cs_demean(day_mean(in_sustain_stddev(is_gt(sub(in_slice(Volume, 2, 237), in_delay(in_slice(Volume, 2, 237), 1)), add(in_mean_full(sub(in_slice(Volume, 2, 237), in_delay(in_slice(Volume, 2, 237), 1))), in_stddev_full(sub(in_slice(Volume, 2, 237), in_delay(in_slice(Volume, 2, 237), 1))))), in_slice(Ret, 2, 237), 5))))`

## 现在到哪一步

- **阶段:全部完成**
- **留出段已经读过 2 次**(10-03 23:00, 10-05 11:59)—— **不许再读**。候选在留出段上的数全在 `runs/F101_day_shine_retstd/final.json`(`./scripts/study.sh digest F101_day_shine_retstd final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `synth:F101_day_shine_retstd`:已返回结果,最后动作 10-05 11:16 → `handoff/F101_day_shine_retstd/agents/synth_ae7cc08a1070145ff.md`
  - `verdict:F101_day_shine_retstd`:中断,最后动作 10-05 13:53 → `handoff/F101_day_shine_retstd/agents/verdict_a4598521995a689d5.md`
  - `verdict:F101_day_shine_retstd`:已返回结果,最后动作 10-05 15:24 → `handoff/F101_day_shine_retstd/agents/verdict_aba6480b25c40a77e.md`

**接手的人该做什么:** 这条因子做完了。最终结论在 `handoff/F101_day_shine_retstd/results/` 里最新的那个(revised.json 优先,否则 study.json)。

## 研究现状(`notes/F101_day_shine_retstd/state.md`,10-05 15:20 更新)—— **先读这个文件**

# F101_day_shine_retstd — 现状(主研,2026-10-05 第二轮覆盖重写;以批量扫描 s2 的大表为准)

## 1. 现状

s1(102 变体)建机制,s2(149 变体)把 s1 的全部推论对过账,结论已定。`synthesis.md` 220 行
(末节「## 第二轮(s2)对账与结论」80 行,含本轮新增的「§4 融合与平滑」补账)。第三批假设
`studies/F101_day_shine_retstd/hypo3.yaml` **25 条 / 25 parse**(本轮换掉 7 条低信息的、补上 J 组 7 条)。
没有起任何服务器计算;**没有读测试段**(`runs/.../sweepfinal_*.json` 未打开),所有数字只来自 train / valid。

一句话结论:**它是「5 分钟滚动日内波动的全天平均」在当天截面均值处的 V 形折叠。折叠不可替代;触发机器只能删一半
(5 分钟窗口要留、μ+σ 阈值要去)。提纯成功 —— 纯多头夏普 1.37 → 2.68;升华失败 —— 净超额只有 +9.7%,
叠在已知族上逐位打平,当筛子不如通用的冻结盘口筛子。按用户的纯多头净超额口径:不可用。**

(…全文 6092 字符,读 `notes/F101_day_shine_retstd/state.md`)

## 研究日志(`notes/F101_day_shine_retstd/journal.md`:3 条,其中研究员自己写的 3 条)

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

### 2026-10-05 13:52 [主研] 批量扫描 s2 对账与结论

对账:折叠不可替代(单调对手 h_rv_mono_mean30 ut -4.8%/-0.61),这条站住了。但 s1 的窗口结论方向整个反了——
去掩码后 5 分钟 roll(2.42/valid 2.78)> 15(2.25/2.47)> 全天 std(2.21/valid 1.66),s1 的 win_I 上升斜坡是掩码被稀释的假象。
s1 读解剖表只看段内分辨力、忽略段等权超额,导致「剔清淡段 / 留热门段」两条推论符号全反:只在低换手 40% 建书
ut 2.51~2.67、+14.9~16.0%,但 rho_k 0.62~0.78 且逐年形状与 k_known 重合 = 同一笔钱。平滑/折叠中心/cs_bucket_rank 中性
/overlay/非波动投机代理五类全给否定读数。
定论:best_own = fld_Volume_Amt 2.68/+9.7%(rho_k 0.16)、h_sum_rv_amtchg 2.46、h_rv_roll5_fold 2.42(最小干净结构);
best_on_known = scr_xhi_p 2.60/+16.8%、seg_lowliq_m 2.67/+16.0%、h_ov_k_rv_10 2.41/+15.4%(与 k_known 逐位打平)。
s1 说的「最关键的空白」填上了,答案是没有增量:剥掉已知族只剩 h_bk_k_rv +8.4%/2.08;任何用法都没过 k_known_xfrozen 的 3.15/+18.5%。
结论:提纯成功(夏普 1.37→2.68)、升华失败,按纯多头净超额口径不可用。第三批 25 条已落 hypo3.yaml(25/25 parse),
第一优先 cs_bucket_demean 桶内折叠——解剖里「小票段内 S+2.96 却只放 6% 仓位」这处落差两轮都没被修过。

### 2026-10-05 15:20 [主研] 批量扫描 s2 对账与结论

对账已逐条核回 s2 大表(149 条,只用 train/valid,未开 sweepfinal):折叠不可替代站住(单调对手 h_rv_mono_mean30 ut -4.8%/-0.61);
s1 的窗口结论方向整个反了——去掩码后 roll5 (2.42/valid 2.78) > roll15 (2.25/2.47) > 全天 std (2.21/valid 1.66),s1 的 win_I 上升斜坡是掩码被稀释的假象;
s1 读解剖表漏了「段等权超额」,导致「剔清淡段/留热门段」符号全反(lo40 分段 ut 2.51~2.67 但 rho_k 0.62~0.78、逐年形状与 k_known 重合 = 同一笔钱)。
定论:best_own = fld_Volume_Amt 2.68/+9.7%(rho_k 0.16)、h_sum_rv_amtchg 2.46、h_rv_roll5_fold 2.42(valid 2.78 全族最高);
best_on_known = scr_xhi_p 2.60/+16.8%、seg_lowliq_m 2.67/+16.0%、h_ov_k_rv_10 2.41(与 k_known 逐位打平);剥掉已知族只剩 h_bk_k_rv +8.4%/2.08。
本轮新增补账(用户要「融合+平滑看样本内外」直接逼出来的):s2 的平滑 4 条 + 融合 1 条 + overlay 3 条,本因子腿**全部写的是 day_std(全天)**
——即刚判输的那个核;赢的 RV5 核从没被平滑/融合/叠加过,叠在真门槛 k_known_xfrozen(3.15)上的全表一条都没有。
所以「平滑已用尽/融合无增量/overlay 打平/越不过 3.15」四句话目前只在错核上成立。hypo3.yaml 因此换掉 7 条低信息假设、补 J 组 7 条(25/25 parse)。

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
- `sweep_s3`  10-05 16:31  177 个变体  → `./scripts/study.sh digest F101_day_shine_retstd sweep_s3`
- `anatomy_s3`  10-05 16:36  0 个变体  → `./scripts/study.sh digest F101_day_shine_retstd anatomy_s3`
- `sweepfinal_s3`  10-05 16:38  8 个变体  → `./scripts/study.sh digest F101_day_shine_retstd sweepfinal_s3`
- `look`(自写脚本的输出)  10-03 19:28  exit 0  → `logs/F101_day_shine_retstd_look.log`
- `look2`(自写脚本的输出)  10-03 19:50  exit 0  → `logs/F101_day_shine_retstd_look2.log`
- `look3`(自写脚本的输出)  10-03 22:45  exit 0  → `logs/F101_day_shine_retstd_look3.log`
- `audit1`(自写脚本的输出)  10-03 23:21  exit 0  → `logs/F101_day_shine_retstd_audit1.log`
- `rev2`(自写脚本的输出)  10-03 23:41  exit 0  → `logs/F101_day_shine_retstd_rev2.log`

## 已写的 notes(`notes/F101_day_shine_retstd/`)

`01_expression.md`(1K)、`02_operators.md`(2K)、`03_decomposition.md`(1K)、`04_grammar.md`(1K)、`05_hypotheses.md`(4K)、`06_baseline.md`(3K)、`07_S1_parts.md`(5K)、`07_S2_background.md`(5K)、`07_SA_audit.md`(1K)、`07_SR_rivals.md`(6K)、`07_S_final.md`(2K)、`07_conditional.md`(1K)、`07_controls.md`(1K)、`07_neutralise.md`(2K)、`07x_look.md`(6K)、`07x_look2.md`(4K)、`07x_look3.md`(10K)、`07x_review1_audit.md`(7K)、`07x_review2_rev2.md`(13K)、`08_variants.md`(3K)、`09_diagnosis.md`(13K)、`10_distilled.md`(13K)、`11_risks.md`(4K)、`12_next.md`(2K)、`journal.md`(5K)、`state.md`(9K)、`synthesis.md`(21K)

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
- `verdict.json`

报告:`research/alpha_distillation/F101_day_shine_retstd.md`(10-04 12:07 生成)
