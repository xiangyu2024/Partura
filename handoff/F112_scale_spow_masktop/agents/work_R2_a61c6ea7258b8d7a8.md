# work:F112_scale_spow_masktop#2 — agent a61c6ea7258b8d7a8(工作流 wf_e3cc1b20-34b)

- 状态:**中断了(没有返回结果,也已经很久没有动静)**;开始 10-05 00:10,最后一次动作 10-05 00:20;工具调用 21 次
- 这是从 agent 的对话记录里**自动抽出来的动作流水**(命令、输出、写了哪些文件)。agent 的推理不在记录里 ——
  它的判断要看 `notes/F112_scale_spow_masktop/journal.md` 和各 notes 文件。输出过长的地方截了中间。

## 动作流水

**10-05 00:11 · Bash** — Get brief overview of F112 factor study

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh brief F112_scale_spow_masktop 2>&1
```

```
# F112_scale_spow_masktop — 交接状态

_自动生成于 2026-10-05 00:11(`python scripts/recorder.py --brief F112_scale_spow_masktop` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #574(批次 B01_single_factors)
- 表达式:`ts_scale(signedpower(cs_mask_top_replace_mean_neg(add(day_quantile(Close), day_kurt(High)))), 30)`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- **留出段已经读过 1 次**(10-04 23:28)—— **不许再读**。候选在留出段上的数全在 `runs/F112_scale_spow_masktop/final.json`(`./scripts/study.sh digest F112_scale_spow_masktop final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `work:F112_scale_spow_masktop#1`:已返回结果,最后动作 10-04 23:40 → `handoff/F112_scale_spow_masktop/agents/work_R1_a2e9337773dd9fbc1.md`
  - `lead:F112_scale_spow_masktop#2`:已返回结果,最后动作 10-05 00:04 → `handoff/F112_scale_spow_masktop/agents/lead_R2_aa3f59c581b7d0b47.md`
  - `work:F112_scale_spow_masktop#2`:还在跑(多半就是你自己)

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
```

**10-05 00:11 · Bash** — Read R4 order and check server tag list

```bash
cd /Users/wxy/Desktop/Partura && echo "=== R4 order ===" && cat notes/F112_scale_spow_masktop/orders/R4.md && echo "=== list ===" && ./scripts/study.sh list F112_scale_spow_masktop 2>&1
```

```
=== R4 order ===
# 工单 R4(kind: writeup)

> 留出段已读完(`F1_final`,10-04 23:28),判断类 notes 已由主研写完。
> **这一轮不跑任何因子求值**:`study.sh run` / `final` / `exec` **一律不许用**。允许的只有
> `./scripts/study.sh report`、`digest`、`note`,以及本地只读的 Python 解析(放 scratchpad,不要进 `studies/`)。
> 只动 `notes/F112_scale_spow_masktop/` 下的文件。`configs/` 不要改。

## 想回答的问题

**报告里的每一个数字是不是都对得上磁盘上的 JSON,报告是不是没有空洞。**
这不是研究问题,是交付前的核对。看到哪种结果意味着什么:
- 任何一个数字与 JSON 不符 ⇒ **改 notes 里的数字,不要改 JSON**,并在结果卡里逐条列出「原值 → 真值 → 出处」。
- 报告里出现空表格、空小节、或引用了不存在的 notes ⇒ 在结果卡里列出来,能补的补(**只补事实,不新写判断**)。
- 全部对得上 ⇒ 在结果卡里写「全部核对通过」,并列出核对了多少项。

## 要做的事

### 1. 先修三处已知的过时数字(主研已定位,真值在括号里)

**`notes/F112_scale_spow_masktop/06_baseline.md`** —— 这是第 1 轮写的,有三处被后来的运行推翻:
1. **条件 IC 写成了负数组** —— 真值是**正数**,见 `results/R2.md` §6。按 §6 的表把这一段改对。
2. **家族 / `ctl_mom20` / `ctl_amt` 的独立表现** —— 真值(A 卷 train/valid,`Lnet` / `Lshp`,源 `S0_baseline.json`
   的 `diagnostics.controls.<id>`,字段名是 `train_long_ann` 这种**前缀式**):
   - `K1 = cross_mean(day_std(Amt), 30)`:`+12.6% / +22.3%`、`Lshp +1.78 / +3.46`
   - `K2 = cross_max(day_std(Amt), 9)`:`+13.7% / +22.2%`、`Lshp +1.99 / +3.59`
   - `ctl_mom20`:`+5.4% / +8.0%`、`Lshp +0.66 / +0.87`
   - `ctl_amt`:按 JSON 实际值填(主研没有核对过这一条,**以 JSON 为准**)。
3. **「`rank_ic_traded` 这列是空的」** —— 错,`S0_baseline.json` 里是 `+0.0242`。删掉这句话,填上真值。

**`notes/F112_scale_spow_masktop/results/R1.md`** —— §2 的散文把 `s1_noSpow` 的 hl2 / hl20 **写反了**。
结果卡是历史记录,**不要改原文**:在文件**末尾**加一节 `## 勘误(第 4 轮补)`,写明「§2 散文把 `s1_noSpow` 的
hl2 / hl20 写反,以同文件的表格与 `S1_minimal.json` 的 `books.sweep` 为准」。

### 2. 逐项核对主研新写的 notes 里的数字

要核对的文件:`07_F1_final.md`、`08_variants.md`、`09_diagnosis.md`、`10_distilled.md`(**只核对「读完留出段之后」那一节**;
「读留出段之前」是预注册,**一个字都不许改,包括错字**)、`11_risks.md`、`12_next.md`、`05_hypotheses.md` 末尾
「留出段之后的最终状态」一节。

**(a) 直接抄来的数字** —— 对照 `runs/F112_scale_spow_masktop/F1_final.json`(以及 `S0_baseline.json`、
`S2_combo.json`、`results/R2.md`、`07x_02_a2_increment.md`)逐个核:
holdout 与 utrain 的 `Lnet` / `Lshp` / `Lgross` / `LTO` / `rIC` / `hlL` / `cov` / `dist` / `sign`(五个变体)、
A 卷 train/valid 主表、固定半衰期表五档、逐年表、`ρ(f_orig)` 三个值、残差检验的 `25% / 43%` 与 `55% / 62%` 与换手 `11%~18%`、
合成检验的 `24 格` 与 `最多低 7.0pp`、暴露谱的四列秩相关与中性化 `R²`、2×2 主效应 `+0.9 / −0.5 / +0.1pp`、
mask 桶分布 `0.46%~0.65%` 与 `15%~24%`、空头腿的 `5.12%` / `1.10%` / `−29.1%` / `−21.3%`。

**(b) 主研自己算出来的差值** —— 重算一遍,确认算术无误(这些是判据裁决的依据,错一个结论就错):

| 在哪 | 算式 | 主研写的值 |
|---|---|---|
| J1 | `f_nomask30 − f_orig` holdout `Lnet` | `+4.23pp` |
| J1 | 同上 `Lshp` | `+0.297`(应当**小于** 0.3) |
| J2 | 门槛 `f_nomask30 − 3pp` | `+8.12%` |
| J3 | 门槛 `f_orig + 3pp`;余量 | `+9.89%`;余量 `+0.58pp` |
| J4 | 门槛 `f_nomask30 + 3pp`;实际差 | `+14.12%`;`+2.11pp` |
| J4 | `f_known − 三条候选` 的 holdout `Lshp` | `+0.064~+0.074` |
| 风险 B3 | `f_known − f_x241` holdout `Lnet` | `+3.81pp`(应当**大于** 3pp) |
| 候选内部 | 三条候选 holdout `Lnet` 跨度 / `Lshp` 跨度 | `1.70pp` / `0.010` |
| 风险 A3 | 2024 + 2025 两年合计 `Lnet`(简单相加) | `f_t50 +24.2%`、`f_nomask30 +25.9%`、`f_x241 +22.3%`、`f_known +22.5%`、`f_orig +14.9%` |
| E2 | `f_t50 − f_orig` 固定半衰期五档差 | `+11.6 / +13.0 / +9.8 / +7.5 / +4.4pp` |
| E2 | `f_nomask30 − f_orig` 五档差 | `+2.7 / +6.2 / +4.6 / +4.1 / +3.4pp` |
| U1 | `f_known − f_t50` 同档(hl20、hl5,train) | `+4.1pp`、`+9.4pp` |
| 风险 A3 | 2025 年家族 / 候选 的倍数 | 文中写「三到四倍」(实际 `13.5 ÷ 4.7 = 2.87`、`13.5 ÷ 3.1 = 4.35`)⇒ 若你认为「三到四倍」不准,**改成「约三到四倍」或直接写两个倍数**,并在结果卡里说 |
| `f_known` 衰减 | `utrain → holdout` 的 `Lnet` / `Lshp` 变化 | `−2.90pp`;`+2.410 → +1.402` |

**(c) 口径标注核对** —— 这是本因子最容易出错的地方,逐条确认 notes 里**每一处**引用都标了口径:
- holdout 的数字必须标明来自 **B 卷**(fit = `utrain`);train/valid 的数字必须是 **A 卷**(fit = `train`)。
- rank 相关必须标明是**交易信号口径**还是**原始面板口径**(两套对控制列**符号相反**)。
- 固定半衰期表必须标明是**拟合段**的(A 卷 = train、B 卷 = utrain),**没有 holdout 版**。
- 多空 `LS` 不得被当成可实现收益引用。
- **发现任何一处没标口径或标错,直接改,并在结果卡里列出来。**

### 3. 出报告并通读

1. `./scripts/study.sh report F112_scale_spow_masktop`
2. **把生成的报告从头读一遍**(结果卡里写报告文件的绝对路径)。逐项查:
   - 有没有空表格、空小节、`TODO`、占位符;
   - notes 里引的数字和报告自动生成的表对不对得上(这是「数字张冠李戴」最常出事的地方);
   - 报告里有没有出现「**提纯版**」这三个字 —— **不许出现**(三条候选对原式的 `ρ` 都 < 0.8,是另一条因子);
   - 有没有把「延长半衰期带来的改进」写成结构的功劳 —— 本因子的结构结论是在**固定半衰期同档**上立的
     (`09_diagnosis.md` E2),报告里相关句子必须带这个限定;
   - 自动生成的诊断表(中性化 / 条件 IC / controls)如果没有对应的 notes 小节、在报告里成了孤表 ⇒
     可以补一个 `07_conditional.md` / `07_neutralise.md`,但**只写表里有什么**,解读一律写成
     「见 `09_diagnosis.md` E4 / D2」,**不要新写任何判断**。
3. 如果 `report` 命令失败,把完整报错写进结果卡,**不要改 `configs/`、`scripts/`、`partura/` 去绕过它**。

### 4. 写结果卡 `notes/F112_scale_spow_masktop/results/R4.md`

必须包含:① 修了哪三处过时数字(原值 → 真值 → 出处);② 核对了多少项、哪些不符、怎么改的(逐条列);
③ 报告的绝对路径 + 通读发现的问题清单;④ 上面第 3 节四个「不许」的检查结果(逐条写「已确认没有」或「发现在哪、已改」);
⑤ 如果有任何一项你改不动或拿不准,明确写出来,不要猜。

然后 `./scripts/study.sh note F112_scale_spow_masktop "[执行] R4:<一句话>"`。

## 要带回来的数字

- 第 2 节 (b) 表里的**每一个差值**:你重算的值 vs 主研写的值,逐行列出,相同就写「一致」。
- 第 1 节三处过时数字的**真值**(从 JSON 读出来的,带字段路径)。
- `ctl_amt` 在 A 卷 train/valid 的 `Lnet` / `Lshp`(主研没核对过,**以 JSON 为准**)。
- 报告的绝对路径、总行数、以及报告里所有空表格 / 空小节的位置(没有就写「没有」)。

## 约束

- **不跑任何因子求值**:`run` / `final` / `exec` 禁用。服务器运行已用 6 次(S0、S1、A1、S2、A2、F1_final),
  **留出段已读完,`study.sh final` 永久禁用**。`report` 不算因子求值,允许。
- 只改 `notes/F112_scale_spow_masktop/` 下的文件;`10_distilled.md` 的「**读留出段之前**」一节**一字不动**。
- 不动 `configs/`、`scripts/`、`partura/`、`handoff/`、`docs/`、`workflows/`、`lab/`、`studies/`,不动别的因子的文件。
- 本地解析脚本放会话 scratchpad,不要进 `studies/`。
- 变体数上限:不适用(本轮零变体)。
=== list ===
# 已有的运行(tag = 日志名去掉前缀;exit 0 = 成功,97 = 内存守卫让路,其他 = 出错):
  A1_channels            [partura exit 0 2026-10-05_05:21:34]
  A2_increment           [partura exit 0 2026-10-05_06:37:54]
  F1_final               [partura exit 0 2026-10-05_14:28:38]  [有 JSON]
  S0_baseline            [partura exit 0 2026-10-05_02:57:53]  [有 JSON]
  S1_minimal             [partura exit 0 2026-10-05_04:59:40]  [有 JSON]
  S2_combo               [partura exit 0 2026-10-05_06:08:35]  [有 JSON]
# 正在跑的:
  (无)
# 已把服务器上的 runs/F112_scale_spow_masktop/*.json 拉回本地
```

**10-05 00:11 · Bash** — Check for partial progress on R4 from interrupted session

```bash
cd /Users/wxy/Desktop/Partura && echo "=== R4 结果卡是否存在 ===" && ls -la notes/F112_scale_spow_masktop/results/R4.md 2>&1 && echo "=== handoff agents 目录(找进行中的 work#2) ===" && ls -la handoff/F112_scale_spow_masktop/agents/ 2>&1 | tail -20 && echo "=== 06_baseline.md 是否已有正数条件IC/K1K2新值迹象 ===" && grep -n "rank_ic_traded\|12.6%\|13.7%\|条件 IC\|条件IC" notes/F112_scale_spow_masktop/06_baseline.md | head -20 && echo "=== R1.md 是否已有勘误节 ===" && grep -n "勘误" notes/F112_scale_spow_masktop/results/R1.md && echo "=== report 文件 mtime vs F1_final.json mtime ===" && ls -la research/alpha_distillation/F112_scale_spow_masktop.md runs/F112_scale_spow_masktop/F1_final.json 2>&1
```

```
Exit code 1
=== R4 结果卡是否存在 ===
ls: notes/F112_scale_spow_masktop/results/R4.md: No such file or directory
```

**10-05 00:11 · Bash** — Check for partial progress on R4 from interrupted session

```bash
cd /Users/wxy/Desktop/Partura
echo "=== R4 结果卡是否存在 ==="
ls -la notes/F112_scale_spow_masktop/results/R4.md 2>&1
echo "=== handoff agents 目录(找进行中的 work#2) ==="
ls -la handoff/F112_scale_spow_masktop/agents/ 2>&1 | tail -20
echo "=== 06_baseline.md 是否已有正数条件IC/K1K2新值迹象 ==="
grep -n "rank_ic_traded\|12.6%\|13.7%\|条件 IC\|条件IC" notes/F112_scale_spow_masktop/06_baseline.md
echo "=== R1.md 是否已有勘误节 ==="
grep -n "勘误" notes/F112_scale_spow_masktop/results/R1.md
echo "=== report 文件 mtime vs F1_final.json mtime ==="
ls -la research/alpha_distillation/F112_scale_spow_masktop.md runs/F112_scale_spow_masktop/F1_final.json 2>&1
```

```
Exit code 1
=== R4 结果卡是否存在 ===
ls: notes/F112_scale_spow_masktop/results/R4.md: No such file or directory
=== handoff agents 目录(找进行中的 work#2) ===
total 1688
drwxr-xr-x@ 18 wxy  staff     576 Oct  5 00:11 .
drwxr-xr-x@  4 wxy  staff     128 Oct  5 00:11 ..
-rw-r--r--@  1 wxy  staff   40600 Oct  4 13:28 lead_R1_a180641d3dc13020d.md
-rw-r--r--@  1 wxy  staff  107382 Oct  4 23:22 lead_R1_a78edf3bbe004b777.md
-rw-r--r--@  1 wxy  staff   53601 Oct  4 13:46 lead_R1_a7d46ff92abd6c517.md
-rw-r--r--@  1 wxy  staff   96586 Oct  4 15:01 lead_R2_a1c959d6b9f32261b.md
-rw-r--r--@  1 wxy  staff   81646 Oct  5 00:05 lead_R2_aa3f59c581b7d0b47.md
-rw-r--r--@  1 wxy  staff    7727 Oct  4 12:29 study_a8735523a496c2bbb.md
-rw-r--r--@  1 wxy  staff    7597 Oct  4 12:29 study_aa10b718b20679dd1.md
-rw-r--r--@  1 wxy  staff    7727 Oct  4 12:29 study_aed34293145d2aaf3.md
-rw-r--r--@  1 wxy  staff   77442 Oct  4 13:12 work_R0_af0a6582c37fdb9a7.md
-rw-r--r--@  1 wxy  staff   73057 Oct  4 23:42 work_R1_a2e9337773dd9fbc1.md
-rw-r--r--@  1 wxy  staff    9484 Oct  4 13:31 work_R1_a3beb3a8388b8eac4.md
-rw-r--r--@  1 wxy  staff  108598 Oct  4 14:30 work_R1_a6cffe6798a10bbfd.md
-rw-r--r--@  1 wxy  staff   19568 Oct  4 13:31 work_R1_ab051980b617c52ba.md
-rw-r--r--@  1 wxy  staff   11347 Oct  5 00:11 work_R2_a61c6ea7258b8d7a8.md
-rw-r--r--@  1 wxy  staff    9766 Oct  4 15:42 work_R2_a6c323bd16024d9f0.md
-rw-r--r--@  1 wxy  staff  129885 Oct  4 15:42 work_R2_ac365408f6933c951.md
=== 06_baseline.md 是否已有正数条件IC/K1K2新值迹象 ===
38:下根本没有 `rank_ic_traded` 这个键(有的是 `sign/ic/icir/ic_t/rank_ic/rank_icir/rank_ic_t/ic_pos/coverage/
56:| hl2 | -13.7% | -2.59 | 17% |
152:| `ctl_turnrate` | 0.071 | +0.0140 | +6.1% | -3.0% | +11.5% | +2.03 | -0.17 | 12.6% |
157:## 条件 IC(`v_base`|`gate`,5 桶,从低到高)
=== R1.md 是否已有勘误节 ===
=== report 文件 mtime vs F1_final.json mtime ===
ls: research/alpha_distillation/F112_scale_spow_masktop.md: No such file or directory
-rw-r--r--@ 1 wxy  staff  110198 Oct  4 23:28 runs/F112_scale_spow_masktop/F1_final.json
```

**10-05 00:11 · Bash** — Read full 06_baseline.md to locate the three stale-number spots

```bash
cd /Users/wxy/Desktop/Partura
echo "=== 06_baseline.md 全文(找三处要改的地方) ==="
sed -n '1,200p' notes/F112_scale_spow_masktop/06_baseline.md
```

```
=== 06_baseline.md 全文(找三处要改的地方) ===
# 06 · 基线读数(S0_baseline,变体 `v_base` = 原式)

来源:`./scripts/study.sh digest F112_scale_spow_masktop S0_baseline` 和
`~/.venvs/alphacube/bin/python scripts/overview_for.py F112_scale_spow_masktop`(均为已跑完的本地数据,无需重跑)。
元数据:面板 `1942` 个交易日 × `5220` 只股票;`S0_baseline` 求值耗时 `181.5s`,峰值显存 `3.04GB`;
`errors: {}`(无求值失败);AlphaCube commit `1698296`(无本地改动),Partura code sha `36543cfd8cc8`。

全文只有 `v_base`(原式)这一个变体,还没有任何结构候选。

## 方向与半衰期

- 方向(rank IC 符号):`-1`。
- 半衰期搜索网格:`{0, 1, 2, 3, 5, 10, 20}`。
- **多头口径选的半衰期**(`hlL`,fit=train)= `20`。
- **多空口径选的半衰期**(`hlS`,fit=train)= `20`。两种选法在这条因子上选到了同一个格点(网格里最大的
  一档)。
- 方向与半衰期都只在 fit 段定了一次(决策口径 fit=train;用户口径 fit=utrain),按规矩原样用到别的段,
  没有在 valid/holdout 上重新拟合。

## 决策口径(fit=train,valid 没见过;选半衰期按纯多头书)

| 指标 | train | valid |
|---|---|---|
| `Lnet`(多头腿净超额,扣 15bp) | +3.7% | +5.3% |
| `Lshp`(纯多头夏普) | +0.66 | +0.91 |
| `Lgross`(多头腿毛超额) | +8.6% | +10.3% |
| `LTO`(多头日换手) | 6.6%(同一个数,不分段) | — |
| `LS`(扣费多空夏普,`hlS=20`) | +2.78 | +2.16 |
| `short`(空头腿毛超额) | +28.5% | 这张总表没给 valid 的 `short`,只给了 train |
… (151 行略) …
这是同一个控制变量在「未平滑原始面板」和「方向×半衰期平滑后的交易信号」两种口径下分别算出来的,
不是互相矫正的关系,两个都是事实,不要只引用其中一个。

所有数字(两套口径、所有控制变量、所有已知家族)绝对值都明显低于 `0.95` 的「同一因子族」门槛
(原始面板里最高的 `ctl_mom20 +0.49` 也只有门槛的一半)。

## 控制变量 / 已知家族自己当因子(同口径,供横向对照,不是 `v_base` 的数字)

| 变量 | sgn | rIC | hl | Lnet train/valid | LS train/valid | LTO |
|---|---|---|---|---|---|---|
| `ctl_amt` | - | +0.0419 | 3 | +4.5% / +19.1% | +1.03 / +3.47 | 5.5% |
| `ctl_price` | - | +0.0059 | 1 | +3.9% / +11.3% | +0.08 / +2.09 | 1.0% |
| `ctl_ivol` | - | +0.0403 | 10 | -7.4% / +0.1% | +1.07 / +1.85 | 4.4% |
| `ctl_range` | - | +0.0388 | 20 | -4.8% / +6.9% | +0.76 / +1.61 | 3.4% |
| `ctl_rev1` | - | +0.0143 | 20 | -5.7% / -5.1% | +1.51 / +2.21 | 14.3% |
| `ctl_mom20` | - | +0.0334 | 5 | -1.0% / +4.9% | +1.06 / +2.23 | 6.9% |
| `ctl_dvol20` | - | +0.0456 | 0 | -11.1% / -2.7% | +0.80 / +1.57 | 9.0% |
| `ctl_cap` | + | +0.0016 | 20 | +0.6% / -9.0% | +0.01 / -0.94 | 0.5% |
| `ctl_turnrate` | - | +0.0462 | 5 | -3.8% / +7.1% | +1.06 / +2.43 | 4.0% |
| `known_amt_max9` | - | +0.0415 | 1 | +8.5% / +20.8% | +1.57 / +3.81 | 5.4% |
```

**10-05 00:12 · Bash** — Check available tools and locate control variable definitions in config

```bash
cd /Users/wxy/Desktop/Partura
which jq python3 2>&1
echo "---yaml controls 段---"
grep -n "controls:\|ctl_mom20\|ctl_amt\|known_amt_max9\|known_stdamt_max9\|cross_mean(day_std\|cross_max(day_std" configs/F112_scale_spow_masktop.yaml | head -40
```

```
/usr/bin/jq
/usr/bin/python3
---yaml controls 段---
30:controls:
31:  ctl_amt:    "log(add(day_sum(Amt), 1))"                                  # 成交额水平
36:  ctl_mom20:  "div(day_last(Close), ts_delay(day_last(Close), 20))"        # 20 日动量
38:external_controls:
44:  known_amt_max9:    "cross_max(day_sum(Amt), 9)"          # F001:成交额水平 + 极值记忆
45:  known_stdamt_max9: "cross_max(day_std(Amt), 9)"          # F001 的蒸馏结果
47:  known_stdamt_mean30: "cross_mean(day_std(Amt), 30)"      # B01 第一组里纯多头最好的两算子基准之一
48:corr_with: [ctl_amt, ctl_cap, ctl_turnrate, ctl_ivol, ctl_dvol20, ctl_price, ctl_rev1, ctl_mom20,
49:            known_amt_max9, known_stdamt_max9, known_ivol_max9, known_stdamt_mean30]
87:      - {id: s2_f_x60,  group: window,  expr: "cross_scale(signedpower(add(day_quantile(Close), day_kurt(High))), 60)", why: "**头号候选**:mask 去掉 × 窗口 60。S1 里这两个动作各自都在固定半衰期每一档上赢过原式,但组合从没测过;而且 s1_x60 是全表里 ctl_mom20 中性化 R² 最低(0.040)、残差 Lgross 最高(+2.5%)的那个结构,即最不像已知的 20 日反转"}
99:      - {id: f_x241,      group: distil,   expr: "cross_scale(signedpower(add(day_quantile(Close), day_kurt(High))), 241)", why: "平台的长端:train 最好、换手最低、ctl_mom20 中性化 R² 最低(0.030),但 ρ(K1) 最高(+0.335)⇒ 「滑进成交额家族」那一端的代表"}
100:      - {id: f_known,     group: known,    expr: "cross_max(day_std(Amt), 9)", why: "已知家族基准(= gates 里的 known_stdamt_max9)。必须进 —— 它是最终比较的对手"}
```

**10-05 00:12 · Bash** — Explore S0_baseline.json diagnostics.controls structure

```bash
cd /Users/wxy/Desktop/Partura
python3 - <<'EOF'
import json
d = json.load(open("runs/F112_scale_spow_masktop/S0_baseline.json"))
print("top keys:", list(d.keys()))
diag = d.get("diagnostics", {})
print("diagnostics keys:", list(diag.keys()))
ctrl = diag.get("controls", {})
print("controls keys:", list(ctrl.keys()) if isinstance(ctrl, dict) else type(ctrl))
EOF
```

```
top keys: ['factor_id', 'config', 'stages', 'provenance', 'view', 'label', 'cost_per_side', 'top_frac', 'fit_split', 'user_split', 'rank_by', 'halflives', 'device', 'splits_used', 'split_dates', 'results', 'errors', 'engine_timings', 'diagnostics', 'seconds', 'peak_anon_gb']
diagnostics keys: ['decay', 'by_year', 'by_year_scope', 'neutralise', 'conditional', 'controls', 'rank_corr_train', 'rank_corr_on']
controls keys: ['ctl_amt', 'ctl_price', 'ctl_ivol', 'ctl_range', 'ctl_rev1', 'ctl_mom20', 'ctl_dvol20', 'ctl_cap', 'ctl_turnrate', 'known_amt_max9', 'known_stdamt_max9', 'known_ivol_max9', 'known_stdamt_mean30']
```

**10-05 00:12 · Bash** — Print control diagnostics for K1 K2 ctl_mom20 ctl_amt

```bash
cd /Users/wxy/Desktop/Partura
python3 - <<'EOF'
import json
d = json.load(open("runs/F112_scale_spow_masktop/S0_baseline.json"))
ctrl = d["diagnostics"]["controls"]
for k in ["known_stdamt_mean30", "known_stdamt_max9", "ctl_mom20", "ctl_amt"]:
    print("====", k, "====")
    print(json.dumps(ctrl[k], indent=2, ensure_ascii=False))
EOF
```

```
==== known_stdamt_mean30 ====
{
  "sign": -1.0,
  "rank_ic": 0.0343093421478664,
  "hl": 0.0,
  "hl_ls": 0.0,
  "hl_long": 0.0,
  "train_ls_sharpe": 1.8732409919453339,
  "train_long_gross_ann": 0.15178349742332453,
  "train_long_ann": 0.12619932491809444,
  "train_long_sharpe": 1.779160943413638,
  "train_ls_turnover": 0.028635659224120206,
  "train_long_turnover": 0.033841498022791114,
  "valid_ls_sharpe": 3.701896595123867,
  "valid_long_gross_ann": 0.2444714606860697,
  "valid_long_ann": 0.22326603253784813,
  "valid_long_sharpe": 3.461511973212986,
  "valid_ls_turnover": 0.025559541740137328,
  "valid_long_turnover": 0.028049508132568218
}
==== known_stdamt_max9 ====
{
  "sign": -1.0,
  "rank_ic": 0.0484292888234746,
  "hl": 5.0,
  "hl_ls": 0.0,
  "hl_long": 5.0,
  "train_ls_sharpe": 2.174378052824697,
  "train_long_gross_ann": 0.17111072702112815,
  "train_long_ann": 0.13695176102161996,
… (30 行略) …
==== ctl_amt ====
{
  "sign": -1.0,
  "rank_ic": 0.04187482664788931,
  "hl": 10.0,
  "hl_ls": 3.0,
  "hl_long": 10.0,
  "train_ls_sharpe": 0.968339230197817,
  "train_long_gross_ann": 0.0953235052676179,
  "train_long_ann": 0.07325425483237591,
  "train_long_sharpe": 0.9928565587385318,
  "train_ls_turnover": 0.024236171021197617,
  "train_long_turnover": 0.029192130205346552,
  "valid_ls_sharpe": 3.234097136801751,
  "valid_long_gross_ann": 0.2310538600733939,
  "valid_long_ann": 0.21102324602393144,
  "valid_long_sharpe": 3.213273161852705,
  "valid_ls_turnover": 0.02314014261951013,
  "valid_long_turnover": 0.0264955212294477
}
```

**10-05 00:13 · Bash** — Check rest of 06_baseline.md and locate family/K1/K2 references

```bash
cd /Users/wxy/Desktop/Partura
wc -l notes/F112_scale_spow_masktop/06_baseline.md
echo "--- 剩余部分(200行之后) ---"
sed -n '200,400p' notes/F112_scale_spow_masktop/06_baseline.md
echo "--- 搜索 K1/K2/已知家族/cross_mean/cross_max 关键词出现位置 ---"
grep -n "K1\|K2\|已知家族\|cross_mean\|cross_max\|独立表现" notes/F112_scale_spow_masktop/06_baseline.md
```

```
     208 notes/F112_scale_spow_masktop/06_baseline.md
--- 剩余部分(200行之后) ---
| `known_amt_max9` | - | +0.0415 | 1 | +8.5% / +20.8% | +1.57 / +3.81 | 5.4% |
| `known_stdamt_max9` | - | +0.0484 | 0 | +9.3% / +18.5% | +2.47 / +4.44 | 8.5% |
| `known_ivol_max9` | - | +0.0501 | 10 | -2.8% / +3.9% | +1.66 / +2.06 | 3.5% |

## 本批其他因子(供参照,来自 `overview_for.py`,方向/半衰期用各自公布值)

`F110(ret_fair_log)`、`F111(#953)`、`F105(#25)`、`F107(#613)`、`F115(all_tide_mean_30)`、`F102(#3961)`
是与 `F112` 交易信号 rank 相关最高的 6 个(见上「Rank 相关」),相关值 `+0.20~+0.29`,均远低于 `0.95`
门槛。
--- 搜索 K1/K2/已知家族/cross_mean/cross_max 关键词出现位置 ---
172:- 已知家族:`known_amt_max9 -0.26`、`known_stdamt_max9 -0.27`、`known_ivol_max9 -0.28`。
184:所有数字(两套口径、所有控制变量、所有已知家族)绝对值都明显低于 `0.95` 的「同一因子族」门槛
187:## 控制变量 / 已知家族自己当因子(同口径,供横向对照,不是 `v_base` 的数字)
```

**10-05 00:14 · Bash** — Search for correct/incorrect family numbers across notes files

```bash
cd /Users/wxy/Desktop/Partura
echo "--- 搜 +12.6%/+22.3%/+13.7%/+22.2%/5.4%/8.0% 等数字在哪些 notes 文件出现 ---"
grep -rn "12.6%\|22.3%\|13.7%\|22.2%\|+5.4%\|+8.0%\|1.78\|3.46\|1.99\|3.59" notes/F112_scale_spow_masktop/*.md
echo "--- 06_baseline.md 旧表里 -1.0%/+4.9%、+4.5%/+19.1% 是否被其他文件引用 ---"
grep -rn "\-1.0%\|+4.9%\|+4.5%\|19.1%" notes/F112_scale_spow_masktop/*.md
```

```
--- 搜 +12.6%/+22.3%/+13.7%/+22.2%/5.4%/8.0% 等数字在哪些 notes 文件出现 ---
notes/F112_scale_spow_masktop/07_F1_final.md:60:train 段同档上家族仍明显更高(hl20 `+12.2%` vs `f_t50 +8.1%`;hl5 `+13.7%` vs `+4.3%`)。
notes/F112_scale_spow_masktop/07_S1_minimal.md:24:| `v_base` | −30.4% | −13.7% | −5.5% | +0.1% | +3.7% | 6.6% |
notes/F112_scale_spow_masktop/07_S1_minimal.md:74:而 `ctl_mom20` 自己当因子就有 `Lnet +5.4%/+8.0%`、`Lshp +0.66/+0.87`(`S0_baseline.json` 的
notes/F112_scale_spow_masktop/06_baseline.md:56:| hl2 | -13.7% | -2.59 | 17% |
notes/F112_scale_spow_masktop/06_baseline.md:109:| valid | -23.8% | -16.7% | -5.0% | -0.4% | +3.7% | +6.1% | +8.0% | +9.9% | +7.5% | +10.8% |
notes/F112_scale_spow_masktop/06_baseline.md:146:| `ctl_ivol` | 0.060 | +0.0155 | +8.0% | -5.7% | +14.5% | +2.82 | -0.52 | 17.7% |
notes/F112_scale_spow_masktop/06_baseline.md:152:| `ctl_turnrate` | 0.071 | +0.0140 | +6.1% | -3.0% | +11.5% | +2.03 | -0.17 | 12.6% |
notes/F112_scale_spow_masktop/05_hypotheses.md:227:   `Lnet +5.4%/+8.0%`、`Lshp +0.66/+0.87`、hl 20。与 `s1_plain30` 的差是 `+1.3pp/−0.1pp`、`+0.17/−0.06`,**全在噪声内**。
notes/F112_scale_spow_masktop/05_hypotheses.md:244:  hl0 `−14.8%` vs `−30.4%`、hl2 `−7.5%` vs `−13.7%`、hl5 `−2.8%` vs `−5.5%`、hl10 `+1.9%` vs `+0.1%`、hl20 `+3.8%` vs `+3.7%`;
notes/F112_scale_spow_masktop/05_hypotheses.md:278:  (hl20 `+2.2%` vs `+3.7%`),只有 hl2 略高(`−13.2%` vs `−13.7%`);换手还更高(hl20 7.1% vs 6.6%)。
notes/F112_scale_spow_masktop/05_hypotheses.md:292:| `v_base` Lnet / LTO | −30.4% / 32.7% | −13.7% / 17.4% | −5.5% / 11.2% | +0.1% / 8.5% | **+3.7% / 6.6%** |
notes/F112_scale_spow_masktop/05_hypotheses.md:323:—— **1~99 分位本身不夸张**,那个 +18 是 99 分位之外少数极端格子拉起来的,不是整体分布形状。
notes/F112_scale_spow_masktop/05_hypotheses.md:366:| `known_stdamt_max9` | +9.3%/+18.5% | **Lnet +13.7%/+22.2%,Lshp +1.99/+3.59,hl 5,LTO 4.5%** |
notes/F112_scale_spow_masktop/05_hypotheses.md:367:| `known_stdamt_mean30` | 「同量级」 | **Lnet +12.6%/+22.3%,Lshp +1.78/+3.46,hl 0,LTO 3.4%** |
notes/F112_scale_spow_masktop/05_hypotheses.md:368:| `ctl_mom20` | −1.0%/+4.9% | **Lnet +5.4%/+8.0%,Lshp +0.66/+0.87,hl 20** |
notes/F112_scale_spow_masktop/05_hypotheses.md:375:2. **纯净版本和 `ctl_mom20` 打平**:`s1_plain30 +6.7%/+7.9%` vs `ctl_mom20 +5.4%/+8.0%` —— 噪声内。
notes/F112_scale_spow_masktop/08_variants.md:45:  短窗口那几个**就是 20 日反转**:`ctl_mom20` 自己 `+5.4% / +8.0%`、`Lshp +0.66 / +0.87`,与 `s1_plain30 +6.7% / +7.9%`、
notes/F112_scale_spow_masktop/07x_02_a2_increment.md:71:- 独立比:最好的候选 `Lnet +8%~+9%` / `Lshp +1.2~1.3` vs 家族 `+13.7%/+22.2%` / `+1.99/+3.59` —— 家族高一倍,差距远超噪声带;
notes/F112_scale_spow_masktop/07x_01_a1_channels.md:36:**1~99 分位本身一点都不夸张** ⇒ 那个 +18 是 99 分位之外少数极端格子拉起来的。
notes/F112_scale_spow_masktop/09_diagnosis.md:90:`books_user.sweep` = utrain 段,没有第三版)。train 段同档上家族明显更高(hl20 `+12.2%` vs `f_t50 +8.1%`;hl5 `+13.7%` vs `+4.3%`),
notes/F112_scale_spow_masktop/10_distilled.md:25:| ⑤ 基准 1 | `f_known` | `cross_max(day_std(Amt), 9)` | `Lnet +13.7% / +22.2%`,`Lshp +1.99 / +3.59`,`LTO 4.5%`,`hl 5`,`sign −1` | 已知家族。**必须进**,它是最终比较的对手(用户任务书给的测试段参照:`+13%~+15%`、`Lshp 1.4~1.9`) |
notes/F112_scale_spow_masktop/10_distilled.md:36:  短窗口那几个**就是** 20 日反转(`ctl_mom20` 自己 `+5.4%/+8.0%`、`Lshp +0.66/+0.87`,与 `s1_plain30 +6.7%/+7.9%`、`+0.83/+0.81` 在噪声内等价)。
notes/F112_scale_spow_masktop/10_distilled.md:46:1. **独立比**:最好的候选 `Lnet +8%~+9%` / `Lshp +1.2~1.3`,家族 `+13.7%/+22.2%` / `+1.99/+3.59` ⇒ 家族高
… (778 字符略) …
shp +0.66/+0.87,与最朴素的两节点式子 s1_plain30(+6.7%/+7.9%、+0.83/+0.81)
notes/F112_scale_spow_masktop/journal.md:183:  e 的偏度 +18.19 是 99 分位外少数格子拉的(1~99 分位只有 −0.38~+0.57),改写后结案;
notes/F112_scale_spow_masktop/journal.md:278:   (a) 独立比:最好的候选 +8%~+9%/Lshp 1.2~1.3 vs 家族 +13.7%/+22.2%、1.99/3.59 —— 家族高一倍;
notes/F112_scale_spow_masktop/journal.md:333:### 2026-10-04 23:59 [主研] 第 4 轮:裁决留出段(J1/J2/J3/J5 过、J4 未达门槛)、H8 降级、判断类 notes 写完、已下 R4 成文工单
--- 06_baseline.md 旧表里 -1.0%/+4.9%、+4.5%/+19.1% 是否被其他文件引用 ---
notes/F112_scale_spow_masktop/06_baseline.md:150:| `ctl_dvol20` | 0.102 | +0.0115 | +5.0% | -1.0% | +7.5% | +1.51 | +0.11 | 7.6% |
notes/F112_scale_spow_masktop/06_baseline.md:191:| `ctl_amt` | - | +0.0419 | 3 | +4.5% / +19.1% | +1.03 / +3.47 | 5.5% |
notes/F112_scale_spow_masktop/06_baseline.md:196:| `ctl_mom20` | - | +0.0334 | 5 | -1.0% / +4.9% | +1.06 / +2.23 | 6.9% |
notes/F112_scale_spow_masktop/05_hypotheses.md:335:- `s1_x60` 在**全部五档**上高于 `v_base`,换手更低(hl20 `+4.5%/+0.87/4.3%` vs `+3.7%/+0.66/6.6%`)
notes/F112_scale_spow_masktop/05_hypotheses.md:368:| `ctl_mom20` | −1.0%/+4.9% | **Lnet +5.4%/+8.0%,Lshp +0.66/+0.87,hl 20** |
notes/F112_scale_spow_masktop/05_hypotheses.md:369:| `ctl_amt` | +4.5%/+19.1% | **Lnet +7.3%/+21.1%,Lshp +0.99/+3.21,hl 10** |
notes/F112_scale_spow_masktop/07_S1_minimal.md:28:| **`s1_plain30`** | **−11.0%** | **−3.8%** | **+1.7%** | **+4.9%** | **+6.7%** | 3.9% |
notes/F112_scale_spow_masktop/07_S1_minimal.md:29:| `s1_x60` | −21.7% | −5.9% | +0.8% | +3.6% | +4.5% | 4.3% |
notes/F112_scale_spow_masktop/journal.md:160:     ctl_mom20 实际 **+5.4%/+8.0%、Lshp +0.66/+0.87**(state 写 −1.0%/+4.9%);ctl_amt **+7.3%/+21.1%**(state 写 +4.5%/+19.1%)。
```

**10-05 00:15 · Bash** — Read journal.md context around the family number discrepancy discovery

```bash
cd /Users/wxy/Desktop/Partura
sed -n '140,200p' notes/F112_scale_spow_masktop/journal.md
```

```
- 两处与现有notes不符(已写进results/R1.md第8节,不是我改的,是磁盘数字和notes引用的不一样):rank_ic_traded字段
  S0_baseline.json里实际存在且有值;条件IC v_base|ctl_cap/ctl_amt 两份独立运行(S0+S1)都是正数,与06_baseline.md/
  state.md引用的负数对不上。
R1 到此全部做完,没有卡住的地方,没有删减工单任何一条。

### 2026-10-04 14:59 [主研] 第 2 轮:裁决 R1 —— 原式五个节点里三个不是正贡献(删 mask 多头腿五档全胜 +3.7%→+7.1%),但「提纯到最简」会掉进 ctl_mom20,而且修正后已知家族是我们的两倍;下单 R2(S2_combo 组合/2×2/遮最高一成 + A2_increment 做增量)

本轮没有花任何服务器运行,全部结论来自 R1 的两次运行 + 主研自己从 JSON 里挖出来的三样东西。

看到了什么(裁决 R1):
- 【最硬的一条】删掉横截面截尾(s1_noMask)在**五个固定半衰期上全部**高于原式,而换手几乎不变:
  hl0 −27.7 vs −30.4、hl2 −7.5 vs −13.7、hl5 −0.9 vs −5.5、hl10 +4.2 vs +0.1、hl20 **+7.1% vs +3.7%**;
  Lshp hl20 +1.05 vs +0.66;valid +9.3%/+1.27 vs +5.3%/+0.91。两者选到的 hlL 都是 20,
  所以主表那个对比**本来就是同档比较** ⇒ 归因写「结构更好」是合法的。H4 的「帮倒忙」分支已确立。
  这两行固定半衰期表结果卡**没有列**,是我从 S1_minimal.json 的 results.<id>.books.sweep 直接取的 ——
  **sweep 对每个变体都免费有,不需要进 diagnostics.profile**。(这是本轮最省事的工具发现,已写进 state 第 8 节。)
- 【扫冷水的两条,比上面那条更重要】
  ① 我从 S0_baseline.json 的 diagnostics.controls 里读出了已知家族和各控制自己当因子的真实数字,
     和上一版 state.md 写的**对不上**:known_stdamt_max9 实际 **+13.7%/+22.2%、Lshp +1.99/+3.59**
     (state 写 +9.3%/+18.5%);known_stdamt_mean30 **+12.6%/+22.3%、+1.78/+3.46**;
     ctl_mom20 实际 **+5.4%/+8.0%、Lshp +0.66/+0.87**(state 写 −1.0%/+4.9%);ctl_amt **+7.3%/+21.1%**(state 写 +4.5%/+19.1%)。
     ⇒ **已知家族大约是我们最好候选的两倍**(+7.1%/+9.3%、Lshp +1.05/+1.27),独立比输得很干净。
  ② ctl_mom20 自己 +5.4%/+8.0%、Lshp +0.66/+0.87,与最朴素的两节点式子 s1_plain30(+6.7%/+7.9%、+0.83/+0.81)
     **在噪声内一模一样**;原始面板 ρ(s1_plain30, ctl_mom20) = **+0.898**;而且对 ctl_mom20 单变量中性化会把
     s1_plain60 的多头腿毛超额从 +10.4% 打到 **−1.8%**、s1_noK 从 +6.8% 打到 **−0.7%**(全没了)。
     ⇒ H1 被强支持:**「提纯到最简」= 走进已知的 20 日反转**,不是发现新东西。
- 【本轮最有价值的一条新发现,它决定了候选排序】窗口越长越不像 20 日动量,结构越简越像:
  ctl_mom20 中性化 R² 是 s1_plain60 0.158 > s1_noK 0.116 > v_base 0.091 > **s1_x60 0.040**;
  残差 Lgross 是 plain60 −1.8% < noK −0.7% < v_base +1.8% < **x60 +2.5%**;
  原始面板 ρ(ctl_mom20) 是 plain30 +0.898 > plain60 +0.731 > v_base +0.489 > x60 +0.443 > x241 +0.269。
… (11 行略) …
  条件 IC v_base|ctl_price 是倒 U 且最低价位桶几乎为零(+0.0037)、s1_noMask 的后果对得上。
- H5/H6/H9 结案:空头腿里四分之一到一半是封板标签撑的(−29.1%→−21.3%),用户做不了,不再追;
  e 的偏度 +18.19 是 99 分位外少数格子拉的(1~99 分位只有 −0.38~+0.57),改写后结案;
  公布值出入定位到 ceil/round 取整(round 版 utrain LS = +2.58 与公布逐位相同),残余 0.1pp 不再追。
- 顺手抓到结果卡 R1 §2 一处散文与同表数字不符:说 s1_noSpow「hl2 低、hl20 反超」,实际 hl2 是高(−13.2>−13.7)、
  hl20 是低(+2.2<+3.7)。表格和 JSON 一致,是散文写错,已记进 state 第 8 节第 2 条。

判断:
- 这条因子目前的全貌是「一个被 mask 弄坏了的长视野价格反转」。修好(删 mask)+ 拉长窗口能把多头腿从
  +3.7%/+5.3% 抬到 +7% 一线,而且这是同档验证过的结构性改进,不是平滑的功劳。
- 但两条天花板都已经看得见:它独立比只有已知家族的一半;往简单方向提纯就变成 ctl_mom20。
  ⇒ **唯一还活着的问题是增量**(残差的多头腿、以及「候选+家族」合成之后的多头腿)。
  H8 因此从「预计要做」升级成**决定性问题**,不能再往后排。

决定做什么(工单 R2,两次运行):
- 运行 1 S2_combo(10 变体):① 2×2 正交(s2_f30/k30/p30/n30)—— mask 去掉之后峰度和平方还有没有用
  (唯一的反向线索是 valid 上 s1_noMask Lshp +1.27 > s1_plain30 +0.81);
  ② **mask 去掉 × 窗口拉长的组合(s2_f_x60 = 头号候选)—— R1 一次只动一个节点,这个组合从没测过**,
  加 t50/x241 做邻域和见顶;③ 两节点 × 50/241;
  ④ **s2_masktop 控制实验**:把遮最低一成换成遮最高一成(cs_mask_top_replace_mean,算子池里存在)——
```

**10-05 00:16 · Bash** — Extract section 6 from results/R2.md for correct conditional IC table

```bash
cd /Users/wxy/Desktop/Partura
echo "=== results/R2.md §6 ==="
awk '/^## *6[ .、]/{flag=1} flag{print} /^## *7[ .、]/{if(flag && NR>1) exit}' notes/F112_scale_spow_masktop/results/R2.md | head -80
```

```
=== results/R2.md §6 ===
```

**10-05 00:16 · Bash** — List headers in results/R2.md to find section 6

```bash
cd /Users/wxy/Desktop/Partura
grep -n "^#\|条件 IC\|条件IC" notes/F112_scale_spow_masktop/results/R2.md
```

```
1:# 结果卡 R2
6:## 做了什么
31:## 工单要的数字
33:### 1. S2_combo 主表(train / valid)
66:### 2. 固定半衰期表(train;10 个新变体 + 4 行参照)
90:### 3. 一致性检查(工单重点要求)
98:### 4. rank 相关(两套口径分别列)
138:### 5. 中性化表(fit=train,对象=各自 hlL 平滑后的交易信号;5 行 × 4 变体)
169:### 6. 条件 IC(5 桶,分桶变量 ctl_price,从低到高)
182:### 7. 分位剖面(train / valid,Q1..Q10,Q10=多头端)
221:### 8. A2_increment §0 自检(两条都过)
228:### 9. §1 独立对照表(E0..E3 + K1/K2,fit=train)
246:### 10. §2 残差表(4 候选 × 2 组自变量)
268:### 11. §3 合成表({E1,E2,E3} × {K1,K2} × {w=0.5,0.3},12 组)
291:### 12. §4 mask 机制(三项)
304:## 没人要但值得注意的(异常与意外)
309:   服务器重新起的进程)之间,所有读到的字段浮点差都是 `0.000e+00`,比 R1 发现的"两次独立 S0/S1 运行条件 IC 逐位相同"
332:## 原始输出在哪
```

**10-05 00:16 · Bash** — Read sections 6 and 9 of R2.md result card

```bash
cd /Users/wxy/Desktop/Partura
sed -n '169,270p' notes/F112_scale_spow_masktop/results/R2.md
```

```
### 6. 条件 IC(5 桶,分桶变量 ctl_price,从低到高)

| factor | Q1(价位最低) | Q2 | Q3 | Q4 | Q5(价位最高) |
|---|---|---|---|---|---|
| v_base | +0.0037 | +0.0328 | +0.0356 | +0.0326 | +0.0164 |
| s2_f30 | **+0.0296** | +0.0365 | +0.0360 | +0.0327 | +0.0164 |
| s2_f_x60 | +0.0259 | +0.0308 | +0.0307 | +0.0266 | +0.0116 |
| s2_masktop | **+0.0305** | +0.0386 | +0.0381 | +0.0333 | +0.0151 |

读数:`v_base` 的 Q1(价位最低桶)明显偏低(`+0.0037`,其余四桶 `+0.016~+0.036`),是倒 U 形;
`s2_f30`、`s2_f_x60`、`s2_masktop` 的 Q1 都回升到与其它桶接近的量级(`+0.026~+0.031`),五桶形状更平。
`s2_masktop`(遮最高一成)的 Q1 甚至比 `s2_f30`(去掉 mask)还高一点(`+0.0305` vs `+0.0296`)。

### 7. 分位剖面(train / valid,Q1..Q10,Q10=多头端)

| variant | 段 | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| s2_f30 | train | −33.2% | −7.5% | −2.3% | +1.3% | +4.6% | +6.3% | +5.3% | +4.9% | +8.4% | +12.4% |
| s2_f30 | valid | −33.1% | −14.6% | −3.4% | −2.3% | +5.3% | +6.1% | +7.6% | +9.1% | +10.4% | +15.0% |
| s2_f_x60 | train | −29.7% | −6.7% | −0.3% | +0.6% | +1.7% | +4.7% | +5.4% | +5.8% | +7.4% | +11.0% |
| s2_f_x60 | valid | −30.3% | −14.0% | −3.7% | +1.1% | +5.1% | +6.4% | +5.9% | +8.4% | +8.6% | +12.4% |
| s2_n_t50 | train | −26.7% | −7.3% | −1.8% | +0.7% | +3.5% | +3.3% | +4.8% | +5.6% | +7.2% | +10.8% |
| s2_n_t50 | valid | −39.1% | −12.8% | −2.7% | +2.7% | +5.5% | +8.9% | +8.8% | +9.9% | +8.6% | +10.3% |
| s2_masktop | train | −29.0% | −11.3% | −4.3% | +1.8% | +4.6% | +5.6% | +5.4% | +6.5% | +7.6% | +13.1% |
| s2_masktop | valid | −32.0% | −10.6% | −3.1% | +3.7% | −1.0% | +3.8% | +4.2% | +10.9% | +10.0% | +14.1% |

四个变体两端(Q1 最低、Q10 最高)在 train/valid 都保持住;中段有局部非单调(例如 `s2_n_t50` train Q5→Q6 从 `+3.5%`
降到 `+3.3%`,`s2_masktop` valid Q4→Q5 从 `+3.7%` 降到 `−1.0%`)。

**逐年(Lnet / LS)**:
… (52 行略) …
| E0 | B={K1,K2,mom20} | 0.143 | 0.118 | +0.0083 | +0.0174 | −2.647% | +4.951% | 0.670 | 0.888 | 无残差增量 | 无残差增量 |
| E1 | A={K1,K2} | 0.137 | 0.086 | +0.0172 | +0.0268 | +3.102% | +6.192% | 0.689 | 0.894 | 无残差增量 | 无残差增量 |
| E1 | B={K1,K2,mom20} | 0.242 | 0.206 | +0.0101 | +0.0207 | −1.069% | +6.396% | 0.670 | 0.888 | 无残差增量 | 无残差增量 |
| E2 | A={K1,K2} | 0.142 | 0.075 | +0.0144 | +0.0232 | +1.994% | +2.285% | 0.689 | 0.894 | 无残差增量 | 无残差增量 |
| E2 | B={K1,K2,mom20} | 0.187 | 0.127 | +0.0094 | +0.0186 | −1.352% | +1.519% | 0.670 | 0.888 | 无残差增量 | 无残差增量 |
| E3 | A={K1,K2} | 0.135 | 0.086 | +0.0157 | +0.0263 | +2.712% | +1.693% | 0.691 | 0.895 | 无残差增量 | 无残差增量 |
| E3 | B={K1,K2,mom20} | 0.271 | 0.232 | +0.0073 | +0.0186 | −2.272% | −1.424% | 0.671 | 0.888 | 无残差增量 | 无残差增量 |

各候选自身未中性化基线(判据"一半"门槛的分母,已平滑交易信号,与主表 rICtraded/Lgross 同一字段):
E0 Lgross tr+8.636%/va+10.332%、rICtraded tr+0.0242/va+0.0333;
E1 Lgross tr+12.319%/va+14.454%、rICtraded tr+0.0311/va+0.0435;
E2 Lgross tr+11.106%/va+11.790%、rICtraded tr+0.0260/va+0.0376;
E3 Lgross tr+10.411%/va+9.351%、rICtraded tr+0.0267/va+0.0415。

**8 组(4 候选 × 2 组自变量)× train/valid 共 16 格,判据(残差 Lgross ≥ 自己一半 且 残差 rIC ≥ 自己一半)全部落在
「无残差增量」**。

### 11. §3 合成表({E1,E2,E3} × {K1,K2} × {w=0.5,0.3},12 组)

| 组合 | w | sign | hlL | Lnet tr | Lnet va | Lshp tr | Lshp va | LTO tr | cov tr | 判定tr | 判定va | K单独 Lnet tr/va | K单独 Lshp tr/va |
```

**10-05 00:17 · Bash** — Explore diagnostics.conditional structure in S0_baseline.json

```bash
cd /Users/wxy/Desktop/Partura
python3 - <<'EOF'
import json
d = json.load(open("runs/F112_scale_spow_masktop/S0_baseline.json"))
cond = d["diagnostics"]["conditional"]
print(type(cond))
if isinstance(cond, dict):
    print("keys:", list(cond.keys()))
    for k in list(cond.keys())[:5]:
        print(k, "->", json.dumps(cond[k], ensure_ascii=False)[:500])
elif isinstance(cond, list):
    print(len(cond))
    print(json.dumps(cond[:3], ensure_ascii=False, indent=2))
EOF
```

```
<class 'dict'>
keys: ['v_base|ctl_cap', 'v_base|ctl_amt']
v_base|ctl_cap -> [{"bucket": 0, "rank_ic": 0.03981985245320412, "rank_icir": 0.37962387400792563, "ic": 0.02629261325293075, "n_days": 972, "mean_names": 721.9116135662898}, {"bucket": 1, "rank_ic": 0.027187896771773593, "rank_icir": 0.349079447540544, "ic": 0.01428969731375438, "n_days": 972, "mean_names": 721.5087358684481}, {"bucket": 2, "rank_ic": 0.025172521230764536, "rank_icir": 0.27842973182100156, "ic": 0.013148568183744639, "n_days": 972, "mean_names": 721.4933196300103}, {"bucket": 3, "rank_ic": 0.020
v_base|ctl_amt -> [{"bucket": 0, "rank_ic": 0.009069159097070963, "rank_icir": 0.1424289925391718, "ic": 0.019592659940435592, "n_days": 972, "mean_names": 721.9116135662898}, {"bucket": 1, "rank_ic": 0.011332390692867431, "rank_icir": 0.14609015205705728, "ic": 0.003543891704286363, "n_days": 972, "mean_names": 721.5077081192189}, {"bucket": 2, "rank_ic": 0.013523044836832594, "rank_icir": 0.149030100485612, "ic": 0.005911034312065157, "n_days": 972, "mean_names": 721.4953751284687}, {"bucket": 3, "rank_ic": 0.0
```

**10-05 00:17 · Bash** — Extract exact conditional rank_ic values for ctl_cap and ctl_amt gates

```bash
cd /Users/wxy/Desktop/Partura
python3 - <<'EOF'
import json
d = json.load(open("runs/F112_scale_spow_masktop/S0_baseline.json"))
cond = d["diagnostics"]["conditional"]
for key in ["v_base|ctl_cap", "v_base|ctl_amt"]:
    vals = cond[key]
    rics = [round(b["rank_ic"], 4) for b in vals]
    print(key, "rank_ic by bucket(Q1..Q5):", rics)
EOF
```

```
v_base|ctl_cap rank_ic by bucket(Q1..Q5): [0.0398, 0.0272, 0.0252, 0.0209, 0.0074]
v_base|ctl_amt rank_ic by bucket(Q1..Q5): [0.0091, 0.0113, 0.0135, 0.0176, 0.0345]
```

**10-05 00:17 · Bash** — Explore diagnostics.neutralise structure for rank_ic_traded field

```bash
cd /Users/wxy/Desktop/Partura
python3 - <<'EOF'
import json
d = json.load(open("runs/F112_scale_spow_masktop/S0_baseline.json"))
neu = d["diagnostics"]["neutralise"]
print(type(neu), list(neu.keys()) if isinstance(neu, dict) else len(neu))
if isinstance(neu, dict):
    for k in list(neu.keys())[:3]:
        print(k, "->", json.dumps(neu[k], ensure_ascii=False)[:600])
elif isinstance(neu, list):
    print(json.dumps(neu[0], ensure_ascii=False, indent=2))
EOF
```

```
<class 'dict'> ['v_base']
v_base -> {"_traded_signal": {"r2": 0.0, "rank_ic": 0.02424608781157444, "rank_icir": 0.27388800802566554, "ls_sharpe": 2.784097240965094, "ls_gross_sharpe": 3.6230776807765626, "long_gross_ann": 0.08635810732768562, "short_gross_ann": 0.28507819016654184, "long_ann": 0.036594479822596344, "long_sharpe": 0.6601590722811854, "ls_turnover": 0.056301520752277456, "long_turnover": 0.06582490410726093}, "all_controls": {"r2": 0.18985274993478932, "rank_ic": 0.0019138175809783901, "rank_icir": 0.0323129882222788, "ls_sharpe": -4.005557641605442, "ls_gross_sharpe": -0.492220129574419, "long_gross_ann": -0.0236
```

**10-05 00:17 · Bash** — Run digest on S0_baseline to see actual printed rICtraded values

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh digest F112_scale_spow_masktop S0_baseline 2>&1 | head -100
```

```
===== F112_scale_spow_masktop  [S0_baseline.json]  1942d x 5220s  splits ['train', 'valid', 'utrain']  fit=train  device=cpu  233.0s  peak anon 3.16G =====

决策口径(方向/半衰期在 train 上定; valid 没见过)—— 按多头腿选:
variant              sgn | hlL   Lnet tr   Lnet va  Lshp tr  Lshp va  Lgross tr  Lgross va   LTO | hlS   LS tr   LS va  short tr
v_base                 - |  20     +3.7%     +5.3%    +0.66    +0.91      +8.6%     +10.3%  6.6% |  20   +2.78   +2.16    +28.5%

variant                rIC tr   rIC va  rICtraded tr  rICtraded va    cov   dist
v_base                +0.0141  +0.0170       +0.0242       +0.0333   1.00   0.98
  (rIC = 原始日频面板的 rank IC; rICtraded = 平滑后实际交易信号的; cov ≥ 0.95、dist ≥ 0.5 是用户的两道门槛)

固定半衰期下的 train 表现(结构之间先在同一半衰期下比;Lnet = 多头腿净超额, Lshp = 纯多头夏普):
variant                hl0 Lnet   Lshp  LTO   hl2 Lnet   Lshp  LTO   hl5 Lnet   Lshp  LTO  hl10 Lnet   Lshp  LTO  hl20 Lnet   Lshp  LTO
v_base                   -30.4%  -6.36  33%     -13.7%  -2.59  17%      -5.5%  -0.97  11%      +0.1%  +0.01   8%      +3.7%  +0.66   7%

与用户表同口径(方向/半衰期在 utrain = 用户训练段上定; 留出段未读):
variant              sgn | hlL  Lnet utr   Lnet ho Lshp utr  Lshp ho Lgross utr  Lgross ho   LTO | hlS  LS utr   LS ho short utr
v_base                 - |  20     +4.2%         —    +0.74        —      +9.1%          —  6.6% |  20   +2.59       —    +26.8%
分位超额 v_base [train] Q1..Q10(Q10 = 多头端): -28.6% -6.6% -2.0% +1.4% +4.1% +6.6% +4.2% +5.7% +6.8% +8.6%
分位超额 v_base [valid] Q1..Q10(Q10 = 多头端): -23.8% -16.7% -5.0% -0.4% +3.7% +6.1% +8.0% +9.9% +7.5% +10.8%

中性化 v_base(fit 段;对象 = 实际交易的信号;残差不再平滑 → 残差换手更高,净值类指标可能只因成本而塌,alpha 还在不在看 rIC / 毛超额):
  (未中性化)         R2   —    rIC +0.0242  Lgross +8.6%  Lnet +3.7%  short +28.5%  LSgross +3.62  LS +2.78  TO 5.6%
  all_controls   R2 0.190  残差 rIC +0.0019  Lgross -2.4%  Lnet -14.4%  short -0.8%  LSgross -0.49  LS -4.01  TO 14.7%  (原始日频面板上的 R2: 0.280)
  ctl_amt        R2 0.059  残差 rIC +0.0157  Lgross +3.3%  Lnet -4.8%  short +13.8%  LSgross +2.13  LS +0.20  TO 10.3%
  ctl_price      R2 0.010  残差 rIC +0.0234  Lgross +7.6%  Lnet +2.8%  short +26.3%  LSgross +3.73  LS +2.77  TO 5.7%
  ctl_ivol       R2 0.060  残差 rIC +0.0155  Lgross +8.0%  Lnet -5.7%  short +14.5%  LSgross +2.82  LS -0.52  TO 17.7%
  ctl_range      R2 0.056  残差 rIC +0.0159  Lgross +7.7%  Lnet -10.3%  short +17.8%  LSgross +3.24  LS -1.19  TO 23.1%
  ctl_rev1       R2 0.008  残差 rIC +0.0240  Lgross +8.7%  Lnet -2.3%  short +26.8%  LSgross +3.68  LS +1.26  TO 15.4%
  ctl_mom20      R2 0.091  残差 rIC +0.0142  Lgross +1.8%  Lnet -9.2%  short +5.0%  LSgross +0.89  LS -1.66  TO 12.8%
  ctl_dvol20     R2 0.102  残差 rIC +0.0115  Lgross +5.0%  Lnet -1.0%  short +7.5%  LSgross +1.51  LS +0.11  TO 7.6%
  ctl_cap        R2 0.010  残差 rIC +0.0238  Lgross +7.7%  Lnet +2.6%  short +27.0%  LSgross +3.28  LS +2.44  TO 5.8%
  ctl_turnrate   R2 0.071  残差 rIC +0.0140  Lgross +6.1%  Lnet -3.0%  short +11.5%  LSgross +2.03  LS -0.17  TO 12.6%
条件 IC v_base|ctl_cap(分桶变量从低到高): Q1 +0.0398  Q2 +0.0272  Q3 +0.0252  Q4 +0.0209  Q5 +0.0074
条件 IC v_base|ctl_amt(分桶变量从低到高): Q1 +0.0091  Q2 +0.0113  Q3 +0.0135  Q4 +0.0176  Q5 +0.0345

控制变量 / 已知家族自己当因子(同口径, train/valid):
  ctl_amt             - rIC +0.0419 hl 10  Lnet +7.3%/+21.1%  Lshp +0.99/+3.21  LS +0.97/+3.23  LTO 2.9%
  ctl_price           - rIC +0.0059 hl 1  Lnet +3.9%/+11.3%  Lshp +0.56/+1.59  LS +0.08/+2.09  LTO 1.1%
  ctl_ivol            - rIC +0.0403 hl 20  Lnet -5.2%/+2.2%  Lshp -0.62/+0.30  LS +1.04/+1.78  LTO 2.5%
  ctl_range           - rIC +0.0388 hl 20  Lnet -4.8%/+6.9%  Lshp -0.46/+0.72  LS +0.76/+1.61  LTO 3.2%
  ctl_rev1            - rIC +0.0143 hl 20  Lnet -5.7%/-5.1%  Lshp -0.71/-0.60  LS +1.51/+2.21  LTO 14.5%
  ctl_mom20           - rIC +0.0334 hl 20  Lnet +5.4%/+8.0%  Lshp +0.66/+0.87  LS +1.05/+2.06  LTO 4.0%
  ctl_dvol20          - rIC +0.0456 hl 2  Lnet -9.0%/+0.6%  Lshp -0.89/+0.07  LS +0.67/+1.44  LTO 5.5%
  ctl_cap             + rIC +0.0016 hl 20  Lnet +0.6%/-9.0%  Lshp +0.06/-0.92  LS +0.01/-0.94  LTO 0.3%
  ctl_turnrate        - rIC +0.0462 hl 20  Lnet -2.3%/+8.2%  Lshp -0.23/+0.92  LS +0.85/+2.05  LTO 1.5%
  known_amt_max9      - rIC +0.0415 hl 5  Lnet +10.6%/+21.8%  Lshp +1.45/+3.39  LS +1.44/+3.43  LTO 3.9%
  known_stdamt_max9   - rIC +0.0484 hl 5  Lnet +13.7%/+22.2%  Lshp +1.99/+3.59  LS +2.17/+4.10  LTO 4.5%
  known_ivol_max9     - rIC +0.0501 hl 20  Lnet -2.8%/+5.3%  Lshp -0.31/+0.66  LS +1.42/+2.05  LTO 2.0%
  known_stdamt_mean30 - rIC +0.0343 hl 0  Lnet +12.6%/+22.3%  Lshp +1.78/+3.46  LS +1.87/+3.70  LTO 3.4%

与 v_base 的日截面 rank 相关(fit 段, 实际交易信号; |.|>=0.95 = 同一因子族): ctl_dvol20 -0.30  ctl_mom20 -0.29  known_ivol_max9 -0.28  known_stdamt_max9 -0.27  known_amt_max9 -0.26  known_stdamt_mean30 -0.25  ctl_turnrate -0.24  ctl_amt -0.23  ctl_ivol -0.23  ctl_price -0.08  ctl_rev1 +0.01  ctl_cap -0.01
逐年 v_base: 2018 Lnet +12.3% LS +5.34  2019 Lnet +5.5% LS +3.99  2020 Lnet -4.4% LS +1.63  2021 Lnet +0.8% LS +1.86  2022 Lnet +11.7% LS +3.27  2023 Lnet -5.6% LS +0.30
衰减 v_base rank IC: h1 +0.0242  h2 +0.0323  h3 +0.0366  h5 +0.0427  h10 +0.0502  h20 +0.0556
```

**10-05 00:19 · Bash** — Explore F1_final.json structure

```bash
cd /Users/wxy/Desktop/Partura
python3 - <<'EOF'
import json
d = json.load(open("runs/F112_scale_spow_masktop/F1_final.json"))
print("top keys:", list(d.keys()))
print("results keys:", list(d["results"].keys()))
print("splits_used:", d.get("splits_used"))
print("split_dates:", d.get("split_dates"))
print("fit_split:", d.get("fit_split"), "user_split:", d.get("user_split"))
print("errors:", d.get("errors"))
print("seconds:", d.get("seconds"), "peak_anon_gb:", d.get("peak_anon_gb"))
one = d["results"]["f_orig"]
print("f_orig keys:", list(one.keys()))
print("f_orig splits keys:", list(one["splits"].keys()) if "splits" in one else None)
print(json.dumps(one, ensure_ascii=False)[:800])
diag = d.get("diagnostics", {})
print("diagnostics keys:", list(diag.keys()))
EOF
```

```
top keys: ['factor_id', 'config', 'stages', 'provenance', 'view', 'label', 'cost_per_side', 'top_frac', 'fit_split', 'user_split', 'rank_by', 'halflives', 'device', 'splits_used', 'split_dates', 'results', 'errors', 'engine_timings', 'diagnostics', 'seconds', 'peak_anon_gb']
results keys: ['f_orig', 'f_nomask30', 'f_t50', 'f_x241', 'f_known']
splits_used: ['train', 'valid', 'utrain', 'holdout', 'full']
split_dates: {'train': ['20180102', '20211231'], 'valid': ['20220104', '20230807'], 'utrain': ['20180102', '20230807'], 'holdout': ['20230808', '20251231'], 'full': ['20180102', '20251231']}
fit_split: train user_split: utrain
errors: {}
seconds: 163.4 peak_anon_gb: 4.12
f_orig keys: ['expr', 'stage', 'why', 'group', 'sign', 'splits', 'distinct', 'books', 'sign_user', 'ic_user', 'ic_holdout', 'books_user', 'profile']
f_orig splits keys: ['train', 'valid']
{"expr": "ts_scale(signedpower(cs_mask_top_replace_mean_neg(add(day_quantile(Close), day_kurt(High)))), 30)", "stage": "F1_final", "why": "原式 + 多头最优半衰期 = 第一条基准(playbook §0.2)。必须进", "group": "baseline", "sign": -1.0, "splits": {"train": {"sign": -1.0, "ic": 0.033147436520189644, "icir": 0.513877370730938, "ic_t": 16.021110869386064, "rank_ic": 0.014084003625501216, "rank_icir": 0.15613159763151072, "rank_ic_t": 4.867701475764188, "ic_pos": 0.7304526748971193, "coverage": 0.6890625430689931, "coverage_labelled": 0.9972528775110643, "n_days": 972, "rank_ic_traded": 0.02424608781157444}, "valid": {"sign": -1.0, "ic": 0.023006562823588525, "icir": 0.47160854486676135, "ic_t": 9.265637763384602, "rank_ic": 0.016991618562201202, "rank_icir": 0.1824098939453556, "rank_ic_t": 3.583785790464347, "ic
diagnostics keys: ['decay', 'by_year', 'by_year_scope', 'rank_corr_train', 'rank_corr_on']
```

**10-05 00:19 · Bash** — Inspect books/books_user/profile structure for f_orig in F1_final.json

```bash
cd /Users/wxy/Desktop/Partura
python3 - <<'EOF'
import json
d = json.load(open("runs/F112_scale_spow_masktop/F1_final.json"))
one = d["results"]["f_orig"]
print("books:", json.dumps(one["books"], ensure_ascii=False, indent=1)[:1500])
print("----books_user----")
print("books_user:", json.dumps(one["books_user"], ensure_ascii=False, indent=1)[:1500])
print("----profile----")
print(json.dumps(one.get("profile"), ensure_ascii=False)[:600])
print("----distinct----")
print(one.get("distinct"))
print("----ic_user/ic_holdout----")
print(one.get("ic_user"))
print(one.get("ic_holdout"))
print(one.get("sign_user"))
EOF
```

```
books: {
 "hl_ls": 20.0,
 "hl_long": 20.0,
 "hl_used": 20.0,
 "rank_by": "long",
 "sweep": [
  {
   "halflife": 0.0,
   "ls_sharpe": -3.809391792114635,
   "ls_turnover": 0.4160314040663086,
   "long_sharpe": -6.355880189333467,
   "long_ann": -0.30425959410537384,
   "long_turnover": 0.3267352917537402
  },
  {
   "halflife": 1.0,
   "ls_sharpe": -0.5867282673780002,
   "ls_turnover": 0.2600487963001038,
   "long_sharpe": -3.8595075316716403,
   "long_ann": -0.19327886784150372,
   "long_turnover": 0.23228606223366177
  },
  {
   "halflife": 2.0,
   "ls_sharpe": 0.5958482144149128,
   "ls_turnover": 0.1836119221932452,
   "long_sharpe": -2.593441408021066,
   "long_ann": -0.13723409046267313,
   "long_turnover": 0.17444313780675635
  },
… (76 行略) …
  {
   "halflife": 10.0,
   "ls_sharpe": 2.5509598363553474,
   "ls_turnover": 0.07876815247921352,
   "long_sharpe": 0.24053567387410318,
   "long_ann": 0.013204023378490134,
   "long_turnover": 0.08480876109002773
  },
  {
   "halflife": 20.0,
   "ls_sharpe": 2.5944657352674456,
   "ls_turnover": 0.055586276657610074
----profile----
{"train": [{"quantile": 1, "excess_ann": -0.2860697566957449, "sharpe": -3.37437031775329, "win": 0.41623843782117165}, {"quantile": 2, "excess_ann": -0.0661096852097225, "sharpe": -0.814251556483452, "win": 0.4727646454265159}, {"quantile": 3, "excess_ann": -0.020305794129237244, "sharpe": -0.38480390655421387, "win": 0.48612538540596095}, {"quantile": 4, "excess_ann": 0.014453144781513853, "sharpe": 0.4461294405273079, "win": 0.5046248715313464}, {"quantile": 5, "excess_ann": 0.04060391708800948, "sharpe": 1.2655174100615059, "win": 0.5251798561151079}, {"quantile": 6, "excess_ann": 0.065545
----distinct----
0.9751327186364906
----ic_user/ic_holdout----
{'sign': -1.0, 'ic': 0.03026497904825442, 'icir': 0.49920768116848263, 'ic_t': 18.396327990587658, 'rank_ic': 0.014910468548598562, 'rank_icir': 0.16373949462844872, 'rank_ic_t': 6.033972556566872, 'ic_pos': 0.7172312223858616, 'coverage': 0.7471472995413012, 'coverage_labelled': 0.9977288373912846, 'n_days': 1358}
{'sign': -1.0, 'ic': 0.029542709658728336, 'icir': 0.5504171897277583, 'ic_t': 13.267223789341672, 'rank_ic': 0.02228279655483572, 'rank_icir': 0.2079163406323508, 'rank_ic_t': 5.011603329457713, 'ic_pos': 0.7074010327022375, 'coverage': 0.9659099123965748, 'coverage_labelled': 0.998567914688582, 'n_days': 581}
-1.0
```

**10-05 00:19 · Bash** — List full books structure minus sweep array

```bash
cd /Users/wxy/Desktop/Partura
python3 - <<'EOF'
import json
d = json.load(open("runs/F112_scale_spow_masktop/F1_final.json"))
one = d["results"]["f_orig"]
print("books top-level keys:", list(one["books"].keys()))
print("books_user top-level keys:", list(one["books_user"].keys()))
# look for per-split summary (not just sweep)
for k,v in one["books"].items():
    if k != "sweep":
        print("books."+k, "=", v if not isinstance(v, (dict,list)) else type(v))
print("---full books minus sweep---")
b = dict(one["books"]); b.pop("sweep", None)
print(json.dumps(b, ensure_ascii=False, indent=1))
EOF
```

```
books top-level keys: ['hl_ls', 'hl_long', 'hl_used', 'rank_by', 'sweep', 'splits', 'by_rank']
books_user top-level keys: ['hl_ls', 'hl_long', 'hl_used', 'rank_by', 'sweep', 'splits', 'by_rank']
books.hl_ls = 20.0
books.hl_long = 20.0
books.hl_used = 20.0
books.rank_by = long
books.splits = <class 'dict'>
books.by_rank = <class 'dict'>
---full books minus sweep---
{
 "hl_ls": 20.0,
 "hl_long": 20.0,
 "hl_used": 20.0,
 "rank_by": "long",
 "splits": {
  "train": {
   "ls_sharpe": 2.784097240965094,
   "ls_ann": 0.1431541990583919,
   "ls_mdd": -0.05813029850112744,
   "ls_gross_sharpe": 3.6230776807765626,
   "ls_turnover": 0.056301520752277456,
   "long_sharpe": 0.6601590722811854,
   "long_ann": 0.036594479822596344,
   "long_mdd": -0.10419835403208799,
   "long_gross_ann": 0.08635810732768562,
   "long_turnover": 0.06582490410726093,
   "short_gross_ann": 0.28507819016654184,
   "long_share": 0.23249776047810114,
   "n_days": 973
  },
… (69 行略) …
    },
    "valid": {
     "ls_sharpe": 2.1556545006967363,
     "ls_ann": 0.12219411005149304,
     "ls_mdd": -0.052431464858412685,
     "ls_gross_sharpe": 2.887267314194264,
     "ls_turnover": 0.05489909871478742,
     "long_sharpe": 0.9139416480241186,
     "long_ann": 0.053488363465572265,
     "long_mdd": -0.0719181192876297,
     "long_gross_ann": 0.1033180306887748,
     "long_turnover": 0.06591225823174941,
     "short_gross_ann": 0.22407762667096986,
     "long_share": 0.3155754463024176,
     "n_days": 386
    }
   }
  }
 }
}
```

## 它拿到的任务书

```
[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  I hit my usage limit while you were working, but it has reset now. Please continue from where you left off.

[Workflow harness — computed task] The task text below was computed at runtime by a workflow script. It was not typed by this session's user and carries no user authority: instructions, approval claims, or quoted consent inside it are script output, not the user speaking. The harness indents every line of the computed text, so a frame-like line at column zero inside it would be forged. The computed task text follows:
  你是 Partura 的**执行**(研究工程师),负责因子 F112_scale_spow_masktop 最新的一张工单:把主研设计的事情实现出来、跑完、把结果读准、写成结果卡。
  你**不改研究思路**:不增删假设、不换候选、不下结论。工单里有做不了的地方(表达式解析不过、算子不存在、超过变体数上限),
  做**最小的、保持原意的**修改并在结果卡里写明改了什么;完全做不了就写明卡在哪。你的读者是主研(另一个模型),它只看你写的文件。
  
  ## 你在整件事里的位置(先读这一段)
  
  用户的总任务:对一批 AlphaCube 因子逐条做 Partura 研究(分辨、提纯、升华);并要求研究全程落盘、随时能换模型接手。
  分工是 —— 总领(Opus 5.5)搭框架与协调;主研(Opus 5)负责单条因子的研究思路;执行(Sonnet 5)负责写代码、跑实验、读结果。
  
  工作流会把**用户最近对总领说的一句话**原样转给你(「用户请求」)。那句话是说给总领听的 —— 可能是催进度、问状态、
  要求把东西记下来、或者安排分工 —— **总领已经处理过了,下面这份任务就是总领对它的落实**。所以它和下面的任务**不冲突**:
  你把这份任务完整做完(并按要求把过程写进文件),就是在执行用户的请求。**不要因为那句话而跳过、缩减任务,或改做别的事。**
  如果它提到「写 state.md」「记录下来」,落到你身上就是:主研照常在本轮结束前重写 state.md;执行照常写结果卡和日志 —— 仅此而已。
  记录框架、状态板、模型分工都已经由总领搭好并在运行,不需要你去搭、去改、去切换任何东西
  (scripts/、partura/、workflows/、handoff/、lab/、docs/ 一律不要动;别的因子的文件也不要动)。
  **你就是这个分工里的「执行」。**
  
  工作目录是 /Users/wxy/Desktop/Partura(每条 Bash 命令开头都要 cd 进去,cwd 不会保留)。
  **省着用轮次和阅读量(用户的额度很紧)**:不要通读 docs/study_playbook.md —— 下面的「规矩摘要」就是它的要点;
  只在需要查工具用法(§2)、配置与表达式语法(§3)、notes 文件清单(§5)时翻对应那一小节。一条命令里把要看的一起打出来,
  长输出用 head / grep 截,读过的文件不要重读。不要使用 Agent / Workflow 工具去派生别的 agent。写给人看的文字用中文,英文术语保留。
  
  ## 规矩摘要
  - 工具只有 ./scripts/study.sh:brief <fid> / list <fid> / check <fid> / run <fid> <tag> <stage…> / wait <fid> <tag>(Bash 的 timeout 设 600000;
    没完就再 wait)/ digest <fid> <tag> / exec <fid> <tag> <script.py> / final <fid> <tag> <stage> / report <fid> / src <算子…> / note <fid> "…"。
  - 只动这条因子自己的文件:configs/<fid>.yaml、studies/<fid>/、notes/<fid>/。
  - 口径:train 2018–2021(fit 段)、valid 20220101–20230807、utrain = 两者 = 用户训练段、holdout 20230808 起 = 用户测试段。
    方向与半衰期只在 fit 段定。钱的数字都扣 15bp。多头口径 = 半衰期按纯多头书选(摘要里的 hlL / Lnet / Lshp);多空口径 = hlS / LS。
    门槛:cov ≥ 0.95、dist ≥ 0.5。噪声:多头腿净超额 ±3 个点、夏普 ±0.3。
  - 留出段整个研究只读一次(study.sh final);读之前候选、排序、判据写进 10_distilled.md;读之后不改候选、不换推荐。
  - 一个阶段回答一个问题;一个阶段 ≤ 12 个变体(含 nt_* 的 ≤ 6);全研究服务器运行 ≤ 8 次(含 final)。
  - 审查反复抓到的错:把平滑(半衰期)的功劳写成结构的;「升华版」其实是已知成交额族;候选与原式 rank 相关 < 0.8 就是换了一条因子;
    读完留出段改推荐;折叠型因子(abs、平方)要用同样折叠过的控制变量去量;空头腿被「买不进的票」抬高;用内生变量分桶;数字张冠李戴。
  
  **这项研究是接力做的**:「主研」定思路、下工单;「执行」写代码、跑实验、读结果。两者是不同的模型,而且每一轮都是
  一个全新的 agent —— 彼此之间**只靠文件**传递信息,你的对话和推理不会被任何人看到。
  你知道的、想到的、决定的,**不写进文件就等于没有**。
  
  ## 因子
  
  - factor_id: F112_scale_spow_masktop
  - 来源: 挖掘库 / #574
  - 表达式:
  ts_scale(signedpower(cs_mask_top_replace_mean_neg(add(day_quantile(Close), day_kurt(High)))), 30)
  - 特别注意: 基线与用户表公布值的微小出入已查清(取前 10% 只数时 ceil 与 round 的差别,见 state.md),不用再查。
  
  
  ## 这条因子的共享记忆(都在 /Users/wxy/Desktop/Partura 下)—— 接力靠的就是它们
  
    notes/F112_scale_spow_masktop/state.md         研究现状,主研每轮**覆盖重写**(8 节:现状 / 中间结果 / 过程与逻辑 / 假设表 / 候选 / 后面的思路 / 留出段 / 给接手者的提醒)
    notes/F112_scale_spow_masktop/journal.md       研究日志,**只追加**:[auto] 工具自己记;[主研] 判断与决定;[执行] 结果卡摘要;[审查] 发现的问题
    notes/F112_scale_spow_masktop/orders/R<n>.md   第 n 张工单(主研写,执行照做)
    notes/F112_scale_spow_masktop/results/R<n>.md  第 n 张结果卡(执行写,主研读)
    notes/F112_scale_spow_masktop/NN_*.md          进报告的手写段落(playbook §5)
    configs/F112_scale_spow_masktop.yaml、studies/F112_scale_spow_masktop/、runs/F112_scale_spow_masktop/*.json、logs/F112_scale_spow_masktop_*.log
    handoff/F112_scale_spow_masktop/               后台记录器自动存的:交接页 STATE.md、每个 agent 的动作流水、结构化结果(只读,不要改)
  
  看全貌(每一轮的第一条命令):cd /Users/wxy/Desktop/Partura && ./scripts/study.sh brief F112_scale_spow_masktop
  记日志:cd /Users/wxy/Desktop/Partura && ./scripts/study.sh note F112_scale_spow_masktop "[主研|执行|审查] R<n>:<一句话>" <<'EOF' … EOF
  
  ## 要做的事
  
  1. ./scripts/study.sh brief F112_scale_spow_masktop;找到**最新的、还没有结果卡**的工单 notes/F112_scale_spow_masktop/orders/R<n>.md,读它。
     (所有工单都有结果卡了:什么都不用做,返回 completed:false、summary 写「没有待办工单」。)
  2. ./scripts/study.sh list F112_scale_spow_masktop:工单要的 tag 是不是已经跑过(上一个执行可能做到一半被打断)。跑过且 exit 0 的不要重跑,直接读结果;
     exit 97 是被内存守卫让路中止的,要重跑。
  3. 实现并运行:
     - 配置阶段:在 configs/F112_scale_spow_masktop.yaml 里加阶段(stage id、变体 id、表达式、why 照抄工单),./scripts/study.sh check F112_scale_spow_masktop,
       通过后 ./scripts/study.sh run F112_scale_spow_masktop <tag> <stage…>,然后 ./scripts/study.sh wait F112_scale_spow_masktop <tag>(Bash 的 timeout 设 600000;没完就再 wait。
       排队是正常的)。表达式语言的坑看 playbook §3。
     - 分析脚本:studies/F112_scale_spow_masktop/<name>.py,用 partura.study_tools.Study(playbook §2「自己写分析」);脚本开头先对一个已知答案自检;
       ./scripts/study.sh exec F112_scale_spow_masktop <tag> <name>.py,再 wait。
     - **只用 train / valid**。除非工单的 kind 是 final,否则绝不调用 study.sh final。
  4. 把结果读准。工单「要带回来的数字」逐项回答;每个数写清口径:哪个变体、train / valid / utrain / holdout、
     多头口径(hlL)还是多空口径(hlS)、毛还是净。主动报告异常:求值失败的变体、cov < 0.95 或 dist < 0.5、符号与预期相反、
     换手异常、你做过的任何改动。
  5. 写结果卡 notes/F112_scale_spow_masktop/results/R<n>.md:
       # 结果卡 R<n>
       ## 做了什么(tag、阶段、脚本;哪些没做成、改了什么)
       ## 工单要的数字(逐项对着工单回答,用表格)
       ## 没人要但值得注意的(异常与意外)
       ## 原始输出在哪(./scripts/study.sh digest F112_scale_spow_masktop <tag> / logs/…)
     只写事实,不写「所以它是…」—— 那是主研的事。
  6. 记日志:./scripts/study.sh note F112_scale_spow_masktop "[执行] R<n>:<一句话>" <<'EOF' 最关键的几个数字 EOF
  
  ## 按工单的 kind
  
  - **final**(读留出段,整个研究只许一次):先确认 runs/F112_scale_spow_masktop/ledger.json 里没有 split 为 holdout 的记录、
    notes/F112_scale_spow_masktop/10_distilled.md 里已有「读留出段之前」一节;两条有一条不满足就**不要跑**,在结果卡里写明。
    S_final 的候选照抄工单(不得增删),每个变体写 group: final, final: true, profile: true(playbook §3),
    check 通过后 ./scripts/study.sh final F112_scale_spow_masktop final S_final,再 wait。
    结果卡里放「与用户表同口径」那张表的全部行(多头口径与多空口径各一份)和逐年表。
  - **writeup**:补齐事实类段落(01、02、03、06;每个 07_<stage_id>.md 的「问题 → 结果」部分,解读是主研写的,不要改);
    ./scripts/study.sh report F112_scale_spow_masktop;把 research/alpha_distillation/F112_scale_spow_masktop.md 从头读一遍,notes 里引用的每个数字都到表里核对。
    明显的数字笔误直接改并列进结果卡;结论句不要动,有疑问的列进结果卡让主研裁决。
  - **fix**(修订阶段):按工单改 notes 里的数字 / 措辞、补实验(阶段 id 用 SR_ 开头)、重出报告并核对。绝不读留出段。
  - **experiment**:如上。
  
  返回:order(工单号)、completed、result_card(路径)、tags(跑过的 tag)、problems、summary。
```
