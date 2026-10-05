# F112_scale_spow_masktop — 交接状态

_自动生成于 2026-10-05 11:11(`python scripts/recorder.py --brief F112_scale_spow_masktop` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #574(批次 B01_single_factors)
- 表达式:`ts_scale(signedpower(cs_mask_top_replace_mean_neg(add(day_quantile(Close), day_kurt(High)))), 30)`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- **留出段已经读过 1 次**(10-04 23:28)—— **不许再读**。候选在留出段上的数全在 `runs/F112_scale_spow_masktop/final.json`(`./scripts/study.sh digest F112_scale_spow_masktop final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `work:F112_scale_spow_masktop#1`:已返回结果,最后动作 10-04 23:40 → `handoff/F112_scale_spow_masktop/agents/work_R1_a2e9337773dd9fbc1.md`
  - `lead:F112_scale_spow_masktop#2`:已返回结果,最后动作 10-05 00:04 → `handoff/F112_scale_spow_masktop/agents/lead_R2_aa3f59c581b7d0b47.md`
  - `work:F112_scale_spow_masktop#2`:中断,最后动作 10-05 00:20 → `handoff/F112_scale_spow_masktop/agents/work_R2_a61c6ea7258b8d7a8.md`

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F112_scale_spow_masktop` 看服务器上的 tag,`./scripts/study.sh digest F112_scale_spow_masktop <tag>` 重看结果)。

## 研究现状(`notes/F112_scale_spow_masktop/state.md`,10-05 11:08 更新)—— **先读这个文件**

# 研究现状 · F112_scale_spow_masktop

> 第 **5** 轮(主研 Opus 5)覆盖重写于 2026-10-05。**每轮整个文件覆盖重写。**
> 读序:本页 → `synthesis.md`(本轮综合,最新口径)→ `studies/F112_scale_spow_masktop/hypo.yaml`(第二批 38 条假设)
> → 旧轮 `10_distilled.md` / `09_diagnosis.md` / `results/R3.md`(留出段结论仍有效)。
> 表达式:`ts_scale(signedpower(cs_mask_top_replace_mean_neg(add(day_quantile(Close), day_kurt(High)))), 30)`
> 本轮证据 = `runs/F112_scale_spow_masktop/sweep_s1.json`(113 变体,train/valid)+ `anatomy_s1.json`(utrain 分段/分时)。
> 本轮**没读留出段、没自己起服务器计算**,只跑了 `study.sh table / src / ops / hypo / note`。数字全是 train / valid / utrain。

## 1. 现状(一句话)

**结论不变:不建议纳入 —— 但「为什么」换掉了。** 旧结论是「落在两个已知暴露之间」;本轮大表 + 解剖证明
这棵树是**两条因子叠在一起**:去掉 `ts_scale` 的那一半是低价 / 微盘 beta(`iso_E` ut +8.4%,但在任何价格桶
内部都 -9%~-26%),带 `ts_scale` 的那一半是一条**1 个月反转**(`abl_D` ut +7.8%,每个价格桶内都正,信息集中在
高流动性 / 冻结盘口 / 创业板 / 高波动)。全市场口径对家族仍**无增量**(overlay 六档全低于 `k_known` +15.4%,
`res_known` ut +0.2%/+0.03)。**唯一活口**:家族自己在成交额桶内几乎没有信息 ⇒ 它是一条流动性 beta,
而比值族的 alpha 恰在家族不去的那一段。下一步 = 跑第二批 38 条(已 parse 通过),重点是 D 组流动性聚焦。

(…全文 6040 字符,读 `notes/F112_scale_spow_masktop/state.md`)

## 研究日志(`notes/F112_scale_spow_masktop/journal.md`:23 条,其中研究员自己写的 12 条)

最近的 5 条(更早的和全文看文件):

### 2026-10-04 23:25 [auto] ⚠ 读留出段:final F1_final,阶段 F1_final(留出段只能读这一次;候选与判据应当已经写在 10_distilled.md 里)

### 2026-10-04 23:28 [auto] F1_final 跑完(exit 0);重看结果:./scripts/study.sh digest F112_scale_spow_masktop F1_final

### 2026-10-04 23:39 [执行] R3:F1_final(kind:final,唯一一次读留出段)跑完,exit 0,结果卡 results/R3.md 已写

tag=F1_final,5变体(f_orig/f_nomask30/f_t50/f_x241/f_known),耗时163.4s,peak 4.12GiB,errors={}。
工单要求的5项一致性检查(新变体 train/valid vs 历史 S0/S1/S2 同树变体)全部逐位相等,diff=0:
f_orig≡v_base、f_nomask30≡s2_f30≡s1_noMask、f_t50≡s2_f_t50、f_x241≡s2_f_x241;
f_known 的 train/valid Lnet/Lshp 与 S0_baseline.diagnostics.controls.known_stdamt_max9 也逐位相等。
rank相关(候选对f_orig):f_nomask30+0.784、f_t50+0.743、f_x241+0.509,与S2_combo历史记录一致。
holdout段(B卷,utrain拟合,与用户表同口径)Lnet:f_orig+6.89%、f_nomask30+11.12%、f_t50+10.47%、f_x241+9.42%、f_known+13.23%。
train段(A卷)Lnet对照:f_orig+3.66%、f_nomask30+7.15%、f_t50+8.12%、f_x241+9.70%、f_known+13.70%。
门槛全过:cov 0.997~1.00、dist 0.975~1.00,5个变体sign全部-1,没有一行按J5作废。
数据形状提醒(写进了结果卡,不是判断):A卷(train拟合)只有train/valid两段,B卷(utrain拟合)只有utrain/holdout两段,
JSON里不存在"train拟合hl去评holdout"这第三种切法;profile诊断只有train/valid,没有holdout;diagnostics里没有controls字段。
没人要但值得注意:f_known与gate known_stdamt_max9字面同一棵树,但rank_corr矩阵给出-0.9224而非±1.0,
原因是矩阵对变体用拟合半衰期平滑后的带符号信号、对controls/gates用未平滑原始值,读数口径问题,不是数据错误。

### 2026-10-04 23:59 [主研] 第 4 轮:裁决留出段(J1/J2/J3/J5 过、J4 未达门槛)、H8 降级、判断类 notes 写完、已下 R4 成文工单

看到了什么(全部来自 results/R3.md,F1_final exit 0,五行门槛全过、无一行按 J5 作废):
holdout(B 卷,fit=utrain,= 用户表口径)Lnet/Lshp —— f_orig +6.89%/+1.031、f_nomask30 +11.12%/+1.328、
f_t50 +10.47%/+1.330、f_x241 +9.42%/+1.338、f_known +13.23%/+1.402。

判据裁决(全表 10_distilled.md「读完留出段之后」§2):
- J1 过:+4.23pp(≥3pp 门槛)。诚实记一句:Lshp 这条腿是 +0.297,恰好没到 0.3,J1 是靠 Lnet 腿过的。
- J2 过:f_t50 +10.47%、f_x241 +9.42%,都在门槛 +8.12% 之上 ⇒ 窗口 50~241 是平台,不是训练段的尖点。
- J3 过,但余量只有 0.58pp(门槛 +9.89%,实测 +10.47%)⇒「f_t50 显著优于原式」不能写成强结论;
  强的是固定半衰期同档那组证据(五档全胜 +4.4~+13.0pp),不是 holdout 的这 0.58pp。
- J5 过。J6:集中度真实,按规矩不改推荐,写进 11_risks.md A3。
- **J4 未达门槛,也未被否定** —— 最好的候选是 f_nomask30(+11.12%),门槛 +14.12%,实测 f_known +13.23%,
  只高 2.11pp(<3pp);Lshp 只高 +0.064~+0.074(<0.3)。落在预注册明确写过的中间区。

判断是什么:
1. 留出段唯一的新信息是「家族自己衰减得比候选厉害」:f_known utrain→holdout Lnet +16.13%→+13.23%、
   Lshp +2.410→+1.402(腰斩),三条候选反而持平或变好。train/valid 上「家族高一倍」这句话在用户测试段上
   不成立,必须从报告里删掉,改成「家族仍名义更高,但差距进入噪声带」。
2. 按预注册的规定执行:J4 的中间区不能单独推翻「相对家族没有增量」,但也不能再说「已确立」
   ⇒ H8 降级为「合理但未坐实」。它现在靠的是 train/valid 的残差检验(Lgross 只剩 25%
…(这条日志还有后文,读 journal.md)

### 2026-10-05 11:06 [主研] 批量扫描 s1 的综合

1. 树的真身:A=day_quantile(Close) 默认 q=0.5 即中位分钟价(元),B=day_kurt(High) 无量纲 ⇒ add 被 A 压倒(iso_A +5.8% 与 iso_C +6.3% 在噪声内);E 平方把 ts_scale 的分母从算术均值推向幂均值 ⇒ 全式约等于 r²/(1+cv²),即「一个月跌幅 × 月内价格变异」的 1 个月反转。
2. 承重=A 叶子与 F 比值;rank_C(让峰度与价格等权)ut -10.8%、only_C_R(只留峰度)-4.8%、sub_B_day_q_stat_std -21.9% ⇒ 第二个加数一旦有可比量级整树就塌。D 截尾有害(abl_D +7.8% vs base +4.2%,cs_winsor 同值 ⇒ 不是离群值问题),最好替代 sub_D_cs_rank +8.8%。窗口 20/30/40/50 = +1.0/+4.2/+4.6/+4.9 单调,越过 50 要用 cross_scale。
3. 发现 ts_scale 的 nansum 分母是未设计的暴露:窗口缺失日越少分母越大 ⇒ 所有含 ts_scale 的变体一律低配次新 -4.9%~-5.5%,不含的 -0.1%~-0.7%。
4. 解剖把因子劈成两族:无比值的 iso_E 族在任何价格桶内部都 -9%~-26%、持仓 +34.7% 压在最低价 ⇒ 它就是低价/微盘 beta;含比值的 abl_D 族在每个价格桶内都正,且信息集中在成交额最高档(+12.4%)、冻结盘口段(+29.6%)、创业板(+11.0%)、高波动段(+17.8%)。原因=反转要错价能被交易回去。
5. 相对家族无增量(全市场口径):overlay 六档全低于 k_known +15.4%、res_known ut +0.2%/+0.03 ⇒ 不建议纳入。唯一活口:家族自己在成交额桶内几乎无信息(-4.1/-5.3/-8.2/-5.2/+2.5)却把 +80.3% 持仓压在最低档 ⇒ 它是流动性 beta,而比值族的 alpha 恰在它不去的那一段;overlay 与线性秩残差测不到这种分段互补,cs_first_high40 没试过。
6. 已落盘 notes/synthesis.md 与 studies/hypo.yaml(38 条,38/38 parse)。

## 工单与结果卡(`notes/F112_scale_spow_masktop/orders/`、`notes/F112_scale_spow_masktop/results/`)

- R0:工单 —,结果卡 有
- R1:工单 有,结果卡 有
- R2:工单 有,结果卡 有
- R3:工单 有,结果卡 有
- R4:工单 有,结果卡 **还没有(待执行)**

## 配置里的实验计划(`configs/F112_scale_spow_masktop.yaml`)

- 标题:「当天价位 + 当天 High 分钟级尖峰度」这个混合量,相对它自己过去 30 个交易日的水平偏离了多少;反向交易
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base
- **S1_minimal**(10 个变体):这棵树的最小充分结构是什么:删掉每个节点、把唯一的跨日窗口换档,多头腿和与原式的 rank 相关怎么变?
  s1_noK、s1_noP、s1_noMask、s1_noSpow、s1_plain30、s1_w10、s1_x30、s1_x60、s1_x241、s1_plain60
- **S2_combo**(10 个变体):mask 去掉之后,剩下的节点和窗口怎么配最好?遮最高一成会不会一样差?
  s2_f30、s2_k30、s2_p30、s2_n30、s2_f_t50、s2_f_x60、s2_f_x241、s2_n_t50、s2_n_x241、s2_masktop
- **F1_final**(5 个变体):留出段:去 mask 与长窗口这两条结构结论在用户测试段还在不在;家族是不是仍然明显更好
  f_orig、f_nomask30、f_t50、f_x241、f_known

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F112_scale_spow_masktop`)

- `S0_baseline`  10-04 11:57  1 个变体  → `./scripts/study.sh digest F112_scale_spow_masktop S0_baseline`
- `S1_minimal`  10-04 13:59  10 个变体  → `./scripts/study.sh digest F112_scale_spow_masktop S1_minimal`
- `S2_combo`  10-04 15:08  10 个变体  → `./scripts/study.sh digest F112_scale_spow_masktop S2_combo`
- `F1_final`  10-04 23:28  5 个变体  → `./scripts/study.sh digest F112_scale_spow_masktop F1_final`
- `sweep_s1`  10-05 10:38  113 个变体  → `./scripts/study.sh digest F112_scale_spow_masktop sweep_s1`
- `anatomy_s1`  10-05 10:45  0 个变体  → `./scripts/study.sh digest F112_scale_spow_masktop anatomy_s1`
- `A1_channels`(自写脚本的输出)  10-04 14:21  exit 0  → `logs/F112_scale_spow_masktop_A1_channels.log`
- `A2_increment`(自写脚本的输出)  10-04 15:37  exit 0  → `logs/F112_scale_spow_masktop_A2_increment.log`

## 已写的 notes(`notes/F112_scale_spow_masktop/`)

`01_expression.md`(4K)、`02_operators.md`(15K)、`03_decomposition.md`(6K)、`04_grammar.md`(6K)、`05_hypotheses.md`(33K)、`06_baseline.md`(11K)、`07_F1_final.md`(5K)、`07_S1_minimal.md`(7K)、`07_S2_combo.md`(7K)、`07x_01_a1_channels.md`(7K)、`07x_02_a2_increment.md`(5K)、`08_variants.md`(5K)、`09_diagnosis.md`(8K)、`10_distilled.md`(14K)、`11_risks.md`(5K)、`12_next.md`(4K)、`journal.md`(38K)、`state.md`(9K)、`synthesis.md`(12K)

## 自写的探针与分析脚本(`studies/F112_scale_spow_masktop/`)

- `a1_channels.py`  10-04 14:19  A1_channels — R1 工单第 2 件。五个小节(§1~§5)各自 try/except,互不拖累。
- `a2_increment.py`  10-04 15:33  A2_increment -- R2 工单运行 2。五节(§0 自检 → §1 独立对照 → §2 残差增量 → §3 合成增量 → §4 mask 机制),

## 结构化结果(`handoff/F112_scale_spow_masktop/results/`)

(还没有)
