# F112_scale_spow_masktop — 交接状态

_自动生成于 2026-10-05 00:42(`python scripts/recorder.py --brief F112_scale_spow_masktop` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

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

## 研究现状(`notes/F112_scale_spow_masktop/state.md`,10-05 00:03 更新)—— **先读这个文件**

# 研究现状 · F112_scale_spow_masktop

> 第 **4** 轮主研(Opus 5)覆盖重写于 2026-10-04 晚。**每轮整个文件覆盖重写。**
> 读序:本页 → `10_distilled.md`「读完留出段之后」→ `09_diagnosis.md` → `results/R3.md`;长表在 `07_*`、`07x_*`、`results/R1~R3.md`。
> 表达式:`ts_scale(signedpower(cs_mask_top_replace_mean_neg(add(day_quantile(Close), day_kurt(High)))), 30)`
> **A 卷** = fit `train`(train/valid);**B 卷** = fit `utrain`(utrain/**holdout**,= 用户表口径)。

## 1. 一句话现状

**留出段已读、判断类 notes 已全部写完,本轮进入成文。** 结论是**否定的**:原式的多头腿可交易
(holdout `+6.89%` / `Lshp 1.03`),删掉截尾节点并把窗口放长能稳定提到 `+9%~+11%` / `Lshp 1.33`,
但这条线索落在两个已知暴露之间、相对已知成交额家族拿不出残差增量,而家族同段给 `+13.23%` / `Lshp 1.40` 且换手更低。
**不建议纳入。** 已下 `orders/R4.md`(kind: **writeup**,零服务器运行)。**下一轮应是 (d) 完成,不要再开实验。**

(…全文 6217 字符,读 `notes/F112_scale_spow_masktop/state.md`)

## 研究日志(`notes/F112_scale_spow_masktop/journal.md`:22 条,其中研究员自己写的 11 条)

最近的 5 条(更早的和全文看文件):

### 2026-10-04 23:21 [主研] 第 3 轮:裁决 R2,假设表收口,进入读留出段(已下 R3 = kind:final)

看到了什么(全部来自 results/R2.md,两次运行 exit 0):
1. 2×2 正交:固定 hl20 同档下,峰度主效应 +0.9pp、平方主效应 −0.5pp、交互 +0.1pp —— 全在 ±3pp 噪声内。
   这直接关掉了上一轮 state.md 留的唯一「升华」方向(两通道显式等权),它的触发条件是 s2_f30 ≫ s2_n30,
   实测 +7.1% vs +6.7%、Lshp +1.05 vs +0.83,条件不成立。**不做,是被实验否掉的,不是没来得及做。**
2. 本轮最重要的发现,是从执行已经带回但没有横向读的那张表里读出来的:R2 §4 的原始面板口径秩相关,
   随窗口 30→50→60→241 **四列全部单调**:ρ(ctl_mom20) +0.554→+0.540→+0.519→+0.341,
   ρ(ctl_price) +0.257→+0.399,ρ(K1) +0.086→+0.335,ρ(K2) +0.198→+0.344;ctl_mom20 中性化 R² 同向 0.153→0.068→0.030。
   ⇒ H1 必须改写成 H1′:这棵树的多头腿是一条**连续谱**上的一点,短窗口那端是 20 日反转、长窗口那端是低价/成交额家族,
   窗口参数就是谱上的位置旋钮。**两端都是已知暴露 ⇒ 旋钮转到哪里都走不出已知家族,只会换一个家族。**
   执行把这张表只读成了「两套口径符号相反的再次确认」,没读窗口方向 —— 这是本轮唯一的新增认知,没花服务器运行。
3. H8(决定性问题)有了答案,是**否定**的,三条独立证据:
   (a) 独立比:最好的候选 +8%~+9%/Lshp 1.2~1.3 vs 家族 +13.7%/+22.2%、1.99/3.59 —— 家族高一倍;
   (b) 残差(口径匹配,主证):对 {K1,K2} 取残差后 E1 的 Lgross 从 +12.3%/+14.5% 掉到 +3.1%/+6.2%(只剩 25%/43%),
       rICtraded 剩 55%/62%,16 格判据全部「无残差增量」;残差换手升到 11%~18%(未中性化 4%~7%)⇒ 残差本身不可交易,
       而且这套算子语法根本写不出一个逐日回归残差 ⇒ 对用户这是最终的,不是「有待实现」;
   (c) 合成(旁证):24 格全部「无
…(这条日志还有后文,读 journal.md)

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
- `A1_channels`(自写脚本的输出)  10-04 14:21  exit 0  → `logs/F112_scale_spow_masktop_A1_channels.log`
- `A2_increment`(自写脚本的输出)  10-04 15:37  exit 0  → `logs/F112_scale_spow_masktop_A2_increment.log`

## 已写的 notes(`notes/F112_scale_spow_masktop/`)

`01_expression.md`(4K)、`02_operators.md`(15K)、`03_decomposition.md`(6K)、`04_grammar.md`(6K)、`05_hypotheses.md`(33K)、`06_baseline.md`(11K)、`07_F1_final.md`(5K)、`07_S1_minimal.md`(7K)、`07_S2_combo.md`(7K)、`07x_01_a1_channels.md`(7K)、`07x_02_a2_increment.md`(5K)、`08_variants.md`(5K)、`09_diagnosis.md`(8K)、`10_distilled.md`(14K)、`11_risks.md`(5K)、`12_next.md`(4K)、`journal.md`(36K)、`state.md`(9K)

## 自写的探针与分析脚本(`studies/F112_scale_spow_masktop/`)

- `a1_channels.py`  10-04 14:19  A1_channels — R1 工单第 2 件。五个小节(§1~§5)各自 try/except,互不拖累。
- `a2_increment.py`  10-04 15:33  A2_increment -- R2 工单运行 2。五节(§0 自检 → §1 独立对照 → §2 残差增量 → §3 合成增量 → §4 mask 机制),

## 结构化结果(`handoff/F112_scale_spow_masktop/results/`)

(还没有)
