# work:F107_abs_demean_skew_low#1 — agent aa74426b02df5c02f(工作流 wf_e3cc1b20-34b)

- 状态:**已返回结果**;开始 10-04 23:35,最后一次动作 10-04 23:50;工具调用 52 次
- 这是从 agent 的对话记录里**自动抽出来的动作流水**(命令、输出、写了哪些文件)。agent 的推理不在记录里 ——
  它的判断要看 `notes/F107_abs_demean_skew_low/journal.md` 和各 notes 文件。输出过长的地方截了中间。

## 动作流水

**10-04 23:35 · Bash** — Show brief overview for factor F107_abs_demean_skew_low

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh brief F107_abs_demean_skew_low 2>&1 | head -300
```

```
# F107_abs_demean_skew_low — 交接状态

_自动生成于 2026-10-04 23:35(`python scripts/recorder.py --brief F107_abs_demean_skew_low` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #613(批次 B01_single_factors)
- 表达式:`abs_(cs_demean(day_skew(Low)))`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- **留出段已经读过 1 次**(10-04 15:05)—— **不许再读**。候选在留出段上的数全在 `runs/F107_abs_demean_skew_low/final.json`(`./scripts/study.sh digest F107_abs_demean_skew_low final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `lead:F107_abs_demean_skew_low#3`:失败,几乎没做事
  - `lead:F107_abs_demean_skew_low#1`:已返回结果,最后动作 10-04 23:25 → `handoff/F107_abs_demean_skew_low/agents/lead_R1_a3937d7e542beafdb.md`
  - `work:F107_abs_demean_skew_low#1`:还在跑(多半就是你自己)

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F107_abs_demean_skew_low` 看服务器上的 tag,`./scripts/study.sh digest F107_abs_demean_skew_low <tag>` 重看结果)。

## 研究现状(`notes/F107_abs_demean_skew_low/state.md`,10-04 23:24 更新)—— **先读这个文件**

# F107_abs_demean_skew_low — 研究现状

> 主研**第 4 轮**写(Opus 5,2026-10-04),整页覆盖重写(第 3 轮没写 state.md 就中断了)。
> `abs_(cs_demean(day_skew(Low)))`,挖掘 #613。记 `A = day_skew(Low)`、`B = cs_demean(A)`,信号 `|B|`,
> 方向 **−1**(做多 `|B|` 小的),原式多头半衰期 **hl20**。**留出段已读(tag `FINAL`),不许再读。**

## 1. 一句话现状

**研究已做完,结论是否定的,判断类 notes 全部写完;本轮唯一产出是 `orders/R3.md`(kind: writeup)+ 本页。**
下一步照 R3 做(见 §6),做完进入「整理结论」,**一般不再回到主研**。**不要再开实验轮,不要再跑 `final`。**

(…全文 6501 字符,读 `notes/F107_abs_demean_skew_low/state.md`)

## 研究日志(`notes/F107_abs_demean_skew_low/journal.md`:13 条,其中研究员自己写的 6 条)

最近的 5 条(更早的和全文看文件):

### 2026-10-04 14:43 [主研] 第 2 轮:H14/H13/H15/H4 全部落地,四个升华方向在 valid 上全不通过 → 候选与判据写死,下 R2 读留出段

**看到了什么(引擎数字,全部来自 results/R1.md 与 07x_2_elevate.md)。**

1. **H14 已确立,而且方向是「对手更好」。** m20 +4.8%/+7.3% 对 m20_absret +4.9%/**+13.8%**;
   m60 +5.6%/+6.5% 对 m60_absret +6.2%/**+14.8%**;r_absret 单独 +5.3%/+14.5%、Lshp 2.27、rIC +0.0449/+0.0493。
   train 差 ≤0.6pp(噪声内),**valid 上日频替身高 6.5~8.3pp,rIC 近乎翻倍**。第 1 轮定的判据(差 ≤3 点或两段不同向)满足。
   → **这棵树读的 241 根分钟最低价不只是没有增量,是负贡献**:把同样的「去均值 + 折叠 + 20 日记忆」
   施加在一个朴素日频收益上就更好。而 m20_absret 与 config 里的 g_absidio20 是**逐字相同的表达式**,
   与 ctl_dvol20 秩相关 −0.81 → 它就是「低特质波动」这个已知暴露。

2. **H13 被否定。** x2 §b:mean20|B−c| 在 train 上 argmax c=−0.4(+7.7%),该点 valid 只 **+2.2%**,
   而 valid 自己最好的是 c=0(+7.5%);λ 在 20 日那一族上**符号翻转**(train 选 +0.6、valid 偏 −0.3)。
   固定 hl20 下更干净:|B−(−0.4)| tr +5.6% / va +2.1% 对原式 +1.1%/+3.0% —— **train 升 4.5pp、valid 降 0.9pp,两段反向**。
   → 折叠的不对称(x1 §1 的最优桶在 −0.375)是真实的,但 c/λ 是 train 上拟合的常数,**做不成可交易的结构**。

3. **H15 已确立,x1 可以放心引用。** 8 个最大差格子全部是「窗口内仅 1 个有限观测、当天 base 为 NaN」;
   |diff|>0.05 的 0.31% 格子 mean finite-days 19.4(全体 58.1);仅 numpy 有限 24,927 对仅引擎有限 262(引擎侧多一层 mas
…(这条日志还有后文,读 journal.md)

### 2026-10-04 15:00 [auto] ⚠ 读留出段:final FINAL,阶段 S_final(留出段只能读这一次;候选与判据应当已经写在 10_distilled.md 里)

### 2026-10-04 15:06 [auto] FINAL 跑完(exit 0);重看结果:./scripts/study.sh digest F107_abs_demean_skew_low FINAL

### 2026-10-04 15:16 [执行] R2:FINAL(S_final,5变体)已跑完exit 0,留出段数字已读准写入结果卡

看到了什么(用户口径,utrain→holdout,多头腿净超额):f_orig +1.67%→+1.41%、f_m20 +5.40%→+4.34%、
f_K +15.40%→+14.10%、f_m20K +12.82%→+7.98%、f_m20absret +7.44%→+1.21%。五个候选的 sign(train)与
sign_user(utrain)全部是 -1、完全一致,holdout 没有重新拟合。check 一次通过(41/41),f_m20K 用的是
工单给的第一个写法(cs_rank 版),没有退到 cs_normalize 或 f_m60。f_m20absret 与 gates.g_absidio20
逐字比较完全相同。

两处数字贴近 10_distilled.md 写死的 3pp 门槛,精确值(未四舍五入)已写进结果卡:
判据2(f_m20 − f_orig 的 Lnet,holdout)= +2.9266pp,门槛是 ≥3pp,差一点点没过线;
判据4(f_m20 − f_m20absret,holdout)= +3.1295pp,而 valid 阶段是 f_m20absret 领先 f_m20 6.5pp ——
方向在留出段整个翻了过来。判据0(f_K 自检,Lnet+14.10%/Lshp 1.509)落在预期区间内;
判据3(f_m20K − f_K,holdout)= −6.12pp,清楚不贴线,是"更低"不是"更高"。

意外:f_K 留出段最大回撤比 utrain 深了近 5pp(−9.17%→−14.63%),其余四个候选大多是变浅。
分位剖面(Q1..Q10)、留出段固定半衰期表这次输出里都没有;逐年诊断只有自然年口径(2023 没有按
08-08 拆成上下半),三项都已如实记在结果卡 (D) 节,没有为了补数字新起任何运行。

下一步不是执行的事:留给主研按 10_distilled.md 的判据 0~4 逐条判、写「读完留出段之后」一节。

### 2026-10-04 23:25 [主研] 第 4 轮:核验第3轮判断类 notes(数字逐个对过 JSON,全部相符)→ 下 R3(kind: writeup),重写 state.md

**本轮的处境。** `brief` 显示留出段已读过一次(tag `FINAL`,10-04 15:05),而 `lead#3` 失败、最后动作 15:44。
对照文件时间戳发现:**第 3 轮其实把全部判断类 notes 都写完了**(`11_risks.md` 15:35、`09_diagnosis.md` 15:36、
`12_next.md` 15:36、`08_variants.md` 15:37、`10_distilled.md` 15:38、`05_hypotheses.md` + `07_S_final.md` 15:39),
**只差最后两步就中断**:没写 writeup 工单、没重写 state.md(还是第 2 轮那版 40KB)。
按工单规则「留出段已读的,这一轮必须是 (c) 成文」—— (c) 的判断类 notes 已经有了,所以本轮的正确动作不是重做,
而是**核验 + 补上缺的两步**。没有开任何实验轮,没有跑任何求值运行(求值仍是 5/8)。

**核验的结果:第 3 轮的产出可以信,数字我逐个对过 JSON。** 我直接从
`runs/F107_abs_demean_skew_low/FINAL.json` 的 `results.<id>.books_user.splits` 复算了全部五条判据:
判据0 `f_K` +14.103%/1.5086(落在事前 band +13~15%/1.4~1.9);判据1 原式成本 9.04pp 吃掉毛超额 86%;
判据2 `f_m20−f_orig` = **+2.9266pp**(门槛 3pp,差 0.0734pp 没过)、Lshp +0.7100,归因分解 5.74−2.81=2.93 对得上;
判据3 `f_m20K−f_K` = **−6.1233pp / −0.5354**,中点 ho 9.2214% vs 混合 7.98%、utrain 10.4023% vs 12.82%(两段反号);
判据4 `f_m20−f_m20absret` = **+3.1295pp**;`f_m20absret` 衰减 −6.2273pp。**与 notes 里写的全部一致。**
train/valid 侧也从 `S12.json`/`S0_baseline.json` 抽核了十条(`v_bas
…(这条日志还有后文,读 journal.md)

## 工单与结果卡(`notes/F107_abs_demean_skew_low/orders/`、`notes/F107_abs_demean_skew_low/results/`)

- R1:工单 有,结果卡 有
- R2:工单 有,结果卡 有
- R3:工单 有,结果卡 **还没有(待执行)**

## 配置里的实验计划(`configs/F107_abs_demean_skew_low.yaml`)

- 标题:日内价格水平占用分布的偏度偏离全市场多少(折叠) —— 空头腿是封板/跳价事件,多头腿是「安静且随大盘走」的股票
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base
- **S1_parts**(11 个变体):原式三个节点(偏度、截面去均值、折叠)和字段各自是不是必需的?它是不是「日频 |特质收益|」「分钟收益峰度」这类朴素读数的另一种写法?
  p_signed、p_nodemean、p_znorm、p_close、p_range、p_rank、p_cube、r_absret、r_kurtret、r_kurtlow、r_mktcorr
- **S2_memory**(11 个变体):把日轴记忆写进表达式之后,多头腿净超额的改善有多大、来自平滑还是结构?记忆该是均值、中位数还是极值,窗口多长最稳?
  m10、m20、m30、m60、m120、md60、mr60、mx20、m60_nodemean、m20_absret、m60_absret
- **S_final**(5 个变体):只凭 train/valid 选定的 5 个候选,在留出段上是什么样?这条因子对纯多头用户相对已知家族有没有增量?
  f_orig、f_m20、f_K、f_m20K、f_m20absret

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F107_abs_demean_skew_low`)

- `S0_baseline`  10-04 11:50  1 个变体  → `./scripts/study.sh digest F107_abs_demean_skew_low S0_baseline`
- `S12`  10-04 13:59  22 个变体  → `./scripts/study.sh digest F107_abs_demean_skew_low S12`
- `FINAL`  10-04 15:05  5 个变体  → `./scripts/study.sh digest F107_abs_demean_skew_low FINAL`
- `x1`(自写脚本的输出)  10-04 12:31  exit 0  → `logs/F107_abs_demean_skew_low_x1.log`
- `x2`(自写脚本的输出)  10-04 14:01  exit 0  → `logs/F107_abs_demean_skew_low_x2.log`

## 已写的 notes(`notes/F107_abs_demean_skew_low/`)

`02_operators.md`(2K)、`03_decomposition.md`(2K)、`04_grammar.md`(2K)、`05_hypotheses.md`(19K)、`06_baseline.md`(3K)、`07_S1_parts.md`(12K)、`07_S2_memory.md`(12K)、`07_S_final.md`(10K)、`07x_1_anatomy.md`(10K)、`07x_2_elevate.md`(22K)、`08_variants.md`(6K)、`09_diagnosis.md`(11K)、`10_distilled.md`(17K)、`11_risks.md`(6K)、`12_next.md`(4K)、`journal.md`(23K)、`state.md`(9K)

## 自写的探针与分析脚本(`studies/F107_abs_demean_skew_low/`)

- `probes.py`  10-03 17:50  Probes this tree needs: abs_(cs_demean(day_skew(Low))).
- `x1_anatomy.py`  10-04 12:16  x1 -- what  abs_(cs_demean(day_skew(Low)))  reads on REAL data, and where its long leg comes from.
- `x2_elevate.py`  10-04 12:44  x2 -- can the long leg of  abs_(cs_demean(day_skew(Low)))  be made better by STRUCTURE (not only by smoothing)

## 结构化结果(`handoff/F107_abs_demean_skew_low/results/`)

(还没有)
```

**10-04 23:35 · Bash** — Read order R3 and check server job list for this factor

```bash
cd /Users/wxy/Desktop/Partura && echo "===ORDER R3===" && cat notes/F107_abs_demean_skew_low/orders/R3.md && echo "===LIST===" && ./scripts/study.sh list F107_abs_demean_skew_low 2>&1
```

```
===ORDER R3===
# 工单 R3(kind: writeup)

> 主研第 4 轮写(Opus 5,2026-10-04)。
> **这不是实验工单。研究已经结束**:留出段只读过一次(tag `FINAL`,10-04 15:05),判断类 notes 已经写完
> (`09_diagnosis.md`、`10_distilled.md` 两节、`11_risks.md`、`12_next.md`、`08_variants.md`)。
> 本轮只剩两件事:**补齐报告里还空着的事实类段落**,和**把报告从头读一遍、逐个核对数字**。
> **不许新起任何求值运行**(`run` / `final` / `exec` 一次都不要):本研究已用掉 5 次(`S0_baseline`、`S12`、`FINAL`、`x1`、`x2`),
> 本工单加 0 次。`study.sh report` 不是求值运行,它就是本工单要做的事。
> **留出段已读过,绝不许再跑 `final`。**

---

## 想回答的问题

研究的实证问题已经答完,没有假设要验。本工单只回答一个工程问题:
**`./scripts/study.sh report` 生成的报告,从头读到尾,能不能作为这条因子的最终交付?**
—— 表里有没有空的、notes 里引的数字和表/JSON 对不对得上、归因的写法有没有违反规矩。

看到哪种结果意味着什么:
- 所有表都有数、所有抽查的数字都对得上 → 报告可以交,`status: done`。
- 发现空表或对不上的数字 → **逐条写进结果卡**(文件、行、报告里的值、JSON 里的值),并按下面「§3 能改什么、不能改什么」处理。
- 发现报告结构性缺一整块(例如某个阶段的表整个没渲染) → 照实写进结果卡,**不要新起运行去补**。

---

## 要做的事

### 1. 补四份缺的事实类 notes

报告的 note 槽位缺了就**静默渲染成空**(`partura/report.py` 的 `note()`:文件不存在返回 `""`),
所以下面四个槽位现在是**没有正文的**。四份都是**事实类**:抄数字、写清口径、标注陷阱,
**不要写新的结论/推荐/判决** —— 判断在 `09_diagnosis.md` / `10_distilled.md` 里,已经写死了。

> 写法:中文,英文术语保留;参照已有的 `07_S1_parts.md` / `07_S2_memory.md` 的格式。
> 数字一律从**报告自己的表**或 `runs/F107_abs_demean_skew_low/*.json` 抄,**不要从别的 notes 转抄**
> (转抄会把别人的四舍五入误差带进来);抄完和 `09_diagnosis.md` 里的同一个数字对一次,不一致就记进结果卡。

**(1.1) `notes/F107_abs_demean_skew_low/01_expression.md`** —— 报告第 1 节「原始表达式」的正文,现在是空的。

要写的内容(都是事实):
- 来历:挖掘库 #613,批次 `B01_single_factors`(出处:`configs/F107_abs_demean_skew_low.yaml` 的 `published:` / `source` 字段,照抄)。
- 一句话说它算什么:对每个股票-日,取当天 241 根分钟 **Low** 价,算这条路径的**偏度** `day_skew(Low)`;
  减去**当天全市场的截面均值** `cs_demean`;再取**绝对值** `abs_`。记 `A = day_skew(Low)`、`B = cs_demean(A)`,信号是 `|B|`。
  方向 **−1**(做多 `|B|` **小**的票)。
- **必须写明的两件事**(否则读者会读错):
  - **半衰期不在表达式里**。这棵树**没有任何日轴算子**,记忆全在表达式外面(引擎对日频面板做 EMA)。
    原式在多头口径下选到的半衰期是 **hl20,已经顶到网格上界**(出处:`09_diagnosis.md` A2 的半衰期阶梯)。
  - 用户公布的那一行里 `long: [0.099, 0.105]` 是**毛**超额,不是净超额(出处:`08_variants.md` 第 2 条)。
    报告里原式的净超额是 train **+1.1%** / 留出段 **+1.41%** —— 不要把这两组数放在一起当同一个东西比。
- config 的 `title` 一句话照抄进来当定位(「日内价格水平占用分布的偏度偏离全市场多少(折叠)……」)。

**(1.2) `notes/F107_abs_demean_skew_low/07_S0_baseline.md`** —— 报告第 7 节里 `S0_baseline` 这个阶段的正文,现在是空的。
(config 的 `stages` 有四个:`S0_baseline` / `S1_parts` / `S2_memory` / `S_final`,notes 只有后三个的 `07_*.md`。)

这一份**写短**(半页就够),结构 = 问题 → 结果 → 解读:
- 问题:照抄 config 里 `S0_baseline` 的 `question`。
- 结果:`v_base` 的数字,从 `runs/F107_abs_demean_skew_low/S0_baseline.json` 抄
  (`results.v_base.books.splits.{train,valid}`),至少给:`hlL`、`Lnet`、`Lgross`、空头腿毛超额、`LTO`、纯多头夏普;
  以及半衰期阶梯(hl0 / hl2 / hl5 / hl10 / hl20 的 train 净超额)和衰减 rank IC(h1 → h20)。
- **解读这一段只写指针,不要写新判断**:指到 `06_baseline.md`(基线读法)和
  `09_diagnosis.md` 的 **A1**(钱在用户做不了的空头腿)、**A2**(原式对纯多头不可用,原因是换手)、**A7**(慢变量)。
  一句话点明「本阶段只建立基线事实,结论见 09」。

**(1.3) `notes/F107_abs_demean_skew_low/07_neutralise.md`** —— 报告「中性化」表下面的正文,现在是空的。
表里是 `v_base` / `m20` / `m60` 对 9 个控制变量(config `diagnostics.neutralise`)。

要写的内容:
- 把表怎么读说清:被中性化的是**实际交易的信号**(方向 × 面板 × 选定半衰期),残差**不再平滑**
  → 残差换手更高,**残差的扣费夏普塌掉可能只是成本**,看 alpha 还在不在要看 rank IC 和无成本夏普
  (这一段报告的表头自己已经写了,正文里用一句话呼应,不要重复整段)。
- 关键数字照抄表里的:`m20` 的截面 R² **0.182**、残差多头腿毛超额从 **+6.9%** 掉到 **+1.6%**。
- **必须写的陷阱一(playbook §6.5,审查反复抓的错)**:这棵树带 `abs_` + `cs_demean`,是**折叠型**因子
  —— 折叠过的量和**单调**控制变量的 rank 相关天然接近 0、线性 R² 天然偏低,
  **所以表里 R² 不高不能读成「它不是已知暴露」**。真正有判别力的那次测量是用**同样折叠过**的控制变量做的:
  x1 §6 只用一个日频变量 `EMA20|去均值日收益|`(完全不看日内路径),R² **0.307**,残差多头腿毛超额只剩 **+2.9%**
  (出处 `07x_1_anatomy.md`;引用 x1 的数字**必须标注「numpy 探路」**,见 §2 第 (iv) 条)。
- **必须写的陷阱二**:`gates` 里的三个量(`g_absidio20`、`g_kurtlow20`、`known_stdamt_mean30`)
  **不会自动进 `diagnostics.neutralise`**,所以这张表里**本来就没有它们**,不是漏了。
  对它们的中性化是 x1 §6 / x2 §d §e 的 exec 脚本做的(出处 `08_variants.md` 末节)。
- **不要**在这一份里写「它就是已知暴露」这类结论 —— 那条的级别是「合理但未坐实」,写法在 `09_diagnosis.md` B1,照指针引。

**(1.4) `notes/F107_abs_demean_skew_low/07_conditional.md`** —— 报告「条件 IC(fit 段)」表下面的正文,现在是空的。
表里四行(config `diagnostics.conditional`):`v_base|ctl_cap`、`v_base|ctl_amt`、`m60|known_stdamt_mean30`、`m60|ctl_cap`,各 5 桶。

要写的内容:
- 数字照抄表里的五桶 rank IC;点出形状:`v_base|ctl_cap` 是 **+0.045 / +0.045 / +0.045 / +0.031 / +0.007**
  —— 前四桶平、**最高市值桶几乎归零**;`m60|ctl_cap` 同形状(最高桶 **+0.0048**)。
  (抄之前和表核一次;`09_diagnosis.md` A8 写的就是这组数。)
- 交易含义只写一句,并指针到 `11_risks.md` §3:**这是中小市值因子,做大就没有信号,装不了大钱**。
- **必须写明分桶变量的性质**(审查会看这一条):`ctl_cap` / `ctl_amt` 是**外生**变量(与因子本身无关),
  按它们分桶是干净的;`known_stdamt_mean30` **是被检验的已知家族本身**,`m60|known_stdamt_mean30` 这一行
  是**增量检验**(「在 K 的每个桶里,F 还排不排得出收益」),**不能**读成「F 在低 K 的股票上有效」。
  这一行的结论不在这张表里,而在 `09_diagnosis.md` **A4** 和 `07x_2_elevate.md` §e
  (十六个组合 + 留出段一次),照指针引,**不要**只凭 5 个桶下新结论。

### 2. 出报告,从头读一遍,逐个核对数字

1. `cd /Users/wxy/Desktop/Partura && ./scripts/study.sh report F107_abs_demean_skew_low`
2. **把生成的 `.md` 从头读到尾**(不是抽样看),逐项检查:

   **(i) 空表 / 空槽位。** 任何空单元格、`—`、`NaN`、或 note 槽位没有正文的地方,列出来并分类:
   - **预期之内**(照实写明「不是缺陷」):留出段的**分位剖面**没有(`profile` 字段不在 FINAL 输出里)、
     留出段的**固定半衰期表**没有(`books["sweep"]` 只在 `fit_split` = train 上算)、
     `gates` 三个量不在中性化表里、`diagnostics` 没有配 `controls` 所以报告里本来就没有「控制变量」那张表。
   - **真缺陷**:其余任何空的地方,写清在报告哪一节、哪张表、哪一列。
   **(ii) 逐年口径的坑必须在报告里看得见**:`FINAL` 的 `by_year_scope` 是 `['20180102','20251231']`,**自然年**、
   覆盖全历史,**2023 那一行混了 valid(到 08-07)和 holdout(08-08 起)**。确认 `11_risks.md` §1 和
   `07_S_final.md` (D) 的这条警告在报告里确实出现了;如果报告的逐年表没有带上这个警告,在结果卡里指出来。
   **(iii) 载重数字复核(逐个对 JSON,不是对 notes)。** 下面这些是结论赖以成立的数,我已核过一遍,
   你再独立核一遍,**不一致就报**。源:`runs/F107_abs_demean_skew_low/FINAL.json` →
   `results.<id>.books_user.splits.{utrain,holdout}.{long_ann,long_gross_ann,long_sharpe,long_turnover,long_mdd}`:

   | 要核的 | 应当是 |
   |---|---|
   | 五条候选留出段 `Lnet` | `f_orig` +1.41% · `f_m20` +4.34% · `f_K` +14.10% · `f_m20K` +7.98% · `f_m20absret` +1.21% |
   | 判据 2:`f_m20` − `f_orig`(Lnet / Lshp) | **+2.9266pp**(门槛 3pp,**没过**) / +0.7100 |
   | 判据 2 的归因分解 | 成本 9.04pp → 3.30pp(**省 5.74pp**),毛超额 **让掉 2.81pp**,`5.74 − 2.81 = 2.93` |
   | 判据 3:`f_m20K` − `f_K`(Lnet / Lshp) | **−6.1233pp** / **−0.5354** |
   | 判据 3 的中点算术 | 留出段中点 **+9.2214%** vs 混合 +7.98%;utrain 中点 **+10.4023%** vs 混合 +12.82%(**两段反号**) |
   | 判据 4:`f_m20` − `f_m20absret`(Lnet / Lshp) | **+3.1295pp** / +0.8278 |
   | 判据 0:`f_K` 留出段 | Lnet **+14.103%** / Lshp **1.5086**(事前band +13~15% / 1.4~1.9,**落在里面**) |
   | `f_m20absret` 衰减 | **−6.2273pp**(utrain +7.437% → holdout +1.210%) |

   train/valid 侧的源是 `S12.json` / `S0_baseline.json` 的 `results.<id>.books.splits.{train,valid}`。
   我核过这些且**全部相符**:`v_base` +1.13/+2.97(毛 +9.38/+11.41、空头毛 +32.51、LTO 10.91%)、
   `m20` +4.76/+7.26(毛 +6.86/+9.46、LTO 2.77%)、`m60` +5.60/+6.52(hl3)、`m60_nodemean` +1.40/+1.28、
   `m20_absret` +4.89/+13.75、`m60_absret` +6.22/+14.78、`r_absret` +5.35/+14.53、
   `p_rank` 毛 +10.27/+12.20(空头毛 +19.57)、`p_range` 毛 +9.54/+9.19(空头毛 +24.08、LTO 14.14%)。
   **抽查其中至少 5 条**确认我没抄错;另外把 notes 里引到的、上面没列的数字也核一遍。

   **(iv) 归因与标注的规矩(审查反复抓的错,逐条确认报告里没犯)**:
   - 提纯的改进必须写成**来自平滑 / 更低换手**,不能写成「结构更好」。
     报告里凡出现 `f_m20` 比 `f_orig` 好的地方,附近必须有「毛超额反而降了 2.81pp、成本省 5.74pp」这个分解。
   - 凡引用 **x1**(`07x_1_anatomy.md`、tag `x1`)的数字,必须带「**numpy 探路**」的标注
     (它的 `cross_mean` 面板与引擎不是同一张,H15,book 级影响 ≤0.6pp)。**x2 不需要标注**(引擎同口径)。
   - 空头腿与多空夏普**虚高**这件事必须在报告里出现(次日开盘封涨停的票标签 NaN、在空头里记 0;
     换不带过滤的标签 → 扣费多空夏普 2.81 → 1.83;`11_risks.md` §5)。
   - 「升华版」不能被写成新发现的东西:`f_m20absret` / `m20_absret` 与 `gates.g_absidio20` **逐字相同**,
     是已知的「低特质波动」暴露(与 `ctl_dvol20` 秩相关 −0.81)。确认报告里这层身份是明说的。
   - 候选与原式的 rank 相关:`f_m20` ρ **0.918** > 0.8 才算提纯;`f_m120` ρ 0.784、`f_m20absret` ρ 0.51
     **不是**这条因子的提纯版。确认报告没有把后两者当成本因子的候选推荐。
   - **推荐不许改**:事前第一推荐是 `f_m20`,判据 2 未过线 → 推荐状态是「**被否定**」。
     确认报告里**没有**把 `f_K`、`f_m60` 或任何别的东西写成「本研究的推荐」。

### 3. 能改什么、不能改什么(重要:别越界,也别放过错)

- **可以改**:你自己这一轮新写的四份 notes;以及**纯粹的数字四舍五入/笔误**,前提是
  **JSON 明确不同意**、且改动**不触碰任何判断、判决、推荐或措辞**。每一处这样的改动都要在结果卡里
  列出「文件 + 行 + 原值 + 新值 + JSON 路径」。
- **已知要改的一处(我查出来的)**:`05_hypotheses.md` 里 H6 那一行写 `p_nodemean` 多头毛
  「+9.4/+11.4 → **+3.4/+3.7**」,而 `S12.json` 是 **+3.49% / +3.76%**,正确的四舍五入是 **+3.5/+3.8**
  (`09_diagnosis.md` A5 写的就是 +3.5%/+3.8%,是对的)。把 `05_hypotheses.md` 那两个数改成 +3.5/+3.8,
  **只改这两个数字,别动那一行的措辞和状态**。
- **不可以改**:`09_diagnosis.md`、`10_distilled.md`(**两节都不许动**,「读留出段之前」一节是事前写死的)、
  `11_risks.md`、`12_next.md`、`08_variants.md` 里的任何**判断、判决、级别(已确立/合理但未坐实/未决)、
  推荐、排序**。发现这类问题 → **写进结果卡,不要自己改**。
- **一律不要动**:`scripts/`、`partura/`、`workflows/`、`handoff/`、`lab/`、`docs/`、别的因子的任何文件、
  `configs/F107_abs_demean_skew_low.yaml`(研究已结束,不要再加阶段)。

### 4. 写结果卡

`notes/F107_abs_demean_skew_low/results/R3.md`,至少包含:
1. 做了什么(四份 notes 各写了什么、report 跑没跑成、报告文件的路径和行数)。
2. **报告通读的检查清单结果**:§2 的 (i)(ii)(iii)(iv) 逐项「过 / 不过」,不过的逐条写清。
3. **所有改过的数字**:文件 + 行 + 原值 + 新值 + JSON 路径。
4. **发现但没改的问题**(判断类 notes 里的,留给人看)。
5. 没人要但值得注意的异常。

然后 `./scripts/study.sh note F107_abs_demean_skew_low "[执行] R3:<一句话>"` 记日志。

---

## 要带回来的数字

- §2 (iii) 那张表的**每一行**:你独立从 JSON 算出来的值,和表里「应当是」的值并排,写明一致 / 不一致。
- train/valid 侧**至少 5 条**抽查的并排值(源 `S12.json` / `S0_baseline.json`)。
- 报告的**路径、总行数、章节清单**(12 节有没有都在)。
- 空表 / 空槽位的**完整清单**,分成「预期之内」和「真缺陷」。
- `05_hypotheses.md` 那处 `p_nodemean` 修正的前后值。

## 约束

- **只用 train/valid 和已经读过的留出段结果(`FINAL.json`)**;**不许新起任何 `run` / `final` / `exec` 求值运行**(本工单 0 次)。
  `study.sh report` 可以跑,而且必须跑。**绝不许再跑 `final`**(留出段已读过一次)。
- 没有新的 tag。没有新的变体(本工单 0 个变体)。
- 只动这条因子自己的文件:`notes/F107_abs_demean_skew_low/` 下你被允许改的那些。
- 报告必须**整篇读过**才能写结果卡;读不完就在结果卡里说读到哪里,不要假装核对过。
===LIST===
# 已有的运行(tag = 日志名去掉前缀;exit 0 = 成功,97 = 内存守卫让路,其他 = 出错):
  FINAL                  [partura exit 0 2026-10-05_06:05:48]  [有 JSON]
  S0_baseline            [partura exit 0 2026-10-05_02:50:18]  [有 JSON]
  S12                    [partura exit 0 2026-10-05_04:59:30]  [有 JSON]
  x1                     [partura exit 0 2026-10-05_03:31:54]
  x2                     [partura exit 0 2026-10-05_05:01:06]
# 正在跑的:
  (无)
# 已把服务器上的 runs/F107_abs_demean_skew_low/*.json 拉回本地
```

**10-04 23:35 · Bash** — Show full config yaml for this factor

```bash
cd /Users/wxy/Desktop/Partura && echo "=== YAML ===" && cat configs/F107_abs_demean_skew_low.yaml
```

```
=== YAML ===
# Partura study F107_abs_demean_skew_low  (挖掘 / #613)
# 这份文件只有 S0_baseline 是生成的。后面的阶段、变体、额外控制变量、探针,都要按**这棵树**来写。
factor_id: F107_abs_demean_skew_low
title: "日内价格水平占用分布的偏度偏离全市场多少(折叠) —— 空头腿是封板/跳价事件,多头腿是「安静且随大盘走」的股票"
expression: "abs_(cs_demean(day_skew(Low)))"
baseline_id: v_base
probes: [studies/F107_abs_demean_skew_low/probes.py]

# 用户表里公布的这一行(pick_single_factors 的口径);S0 要先把它复现出来
published: {sign: -1, hl: 20, ls: [2.89, 2.45], long: [0.099, 0.105], lib: "挖掘", name: "#613"}

label: {kind: open_vwap15, horizon: 1, buyable: true,
        verify_against: /root/autodl-tmp/AlphaCube/_bench/trainto/allfac_buyable/_target.npy}
cost_per_side: 0.0015
top_frac: 0.10
rank_by: long          # 半衰期按纯多头书选(用户实际能做的那本书);多空口径每个变体也都会算
horizons: [1, 2, 3, 5, 10, 20]
warmup: 60

# train + valid = 用户的训练段(utrain);holdout = 用户的测试段,只在最后读一次
splits:
  train:   ["20180102", "20211231"]
  valid:   ["20220101", "20230807"]
  utrain:  ["20180102", "20230807"]
  holdout: ["20230808", "20251231"]
  full:    ["20180102", "20251231"]
fit_split: train
user_split: utrain

… (84 行略) …
      - {id: m60_absret, group: rival, expr: "cross_mean(abs_(cs_demean(div(day_last(Close), cross_delay(day_last(Close), 1)))), 60)", why: "同上,60 日"}

  - id: S_final
    question: "只凭 train/valid 选定的 5 个候选,在留出段上是什么样?这条因子对纯多头用户相对已知家族有没有增量?"
    variants:
      - {id: f_orig, group: baseline, final: true,
         expr: "abs_(cs_demean(day_skew(Low)))",
         why: "基准 1:原式 + 多头最优半衰期。判据 1:它在测试段应该仍然是「毛超额被换手吃掉」(Lnet +1~+4%、Lshp 0.2~0.8)"}
      - {id: f_m20, group: distilled, final: true,
         expr: "cross_mean(abs_(cs_demean(day_skew(Low))), 20)",
         why: "第一推荐,这条因子的提纯版(ρ(v_base)=0.918)。判据 2:应比 f_orig 高 ≥3pp 净超额、≥0.3 夏普,且毛超额不高于 f_orig"}
      - {id: f_K, group: known, final: true,
         expr: "cross_mean(day_std(Amt), 30)",
         why: "基准 2:已知家族(必含)。判据 0:它自己在测试段应落在 Lnet +13~+15%、Lshp 1.4~1.9;若它塌了,判据 3 作废"}
      - {id: f_m20K, group: blend, final: true,
         expr: "add(cs_rank(cross_mean(abs_(cs_demean(day_skew(Low))), 20)), cs_rank(cross_mean(day_std(Amt), 30)))",
         why: "判据 3(决定性):提纯版与已知家族等权相加。playbook §6.2 指定的增量检验。只有它比 f_K 高 ≥3pp 且 ≥0.3 夏普,才算有增量"}
      - {id: f_m20absret, group: rival, final: true,
         expr: "cross_mean(abs_(cs_demean(div(day_last(Close), cross_delay(day_last(Close), 1)))), 20)",
         why: "判据 4(H14):同样的「去均值+折叠+20 日记忆」,但完全不看日内路径。valid 上它比 f_m20 高 6.5pp;测试段若重现,「241 根分钟最低价是负贡献」就确立"}
```

**10-04 23:35 · Bash** — Inspect S0_baseline.json structure for v_base results

```bash
cd /Users/wxy/Desktop/Partura && which jq python3 && echo "---S0_baseline keys---" && python3 -c "
import json
d = json.load(open('runs/F107_abs_demean_skew_low/S0_baseline.json'))
print(list(d.keys()))
print(list(d['results'].keys()))
print(json.dumps(d['results']['v_base'], indent=1)[:4000])
"
```

```
/usr/bin/jq
/usr/bin/python3
---S0_baseline keys---
['factor_id', 'config', 'stages', 'provenance', 'view', 'label', 'cost_per_side', 'top_frac', 'fit_split', 'user_split', 'rank_by', 'halflives', 'device', 'splits_used', 'split_dates', 'results', 'errors', 'engine_timings', 'diagnostics', 'seconds', 'peak_anon_gb']
['v_base']
{
 "expr": "abs_(cs_demean(day_skew(Low)))",
 "stage": "S0_baseline",
 "why": "\u539f\u59cb\u8868\u8fbe\u5f0f",
 "group": "baseline",
 "sign": -1.0,
 "splits": {
  "train": {
   "sign": -1.0,
   "ic": 0.037715937784190426,
   "icir": 0.6831629212021364,
   "ic_t": 21.309865422592175,
   "rank_ic": 0.01800682495723387,
   "rank_icir": 0.44324041999250724,
   "rank_ic_t": 13.825975337292686,
   "ic_pos": 0.7523124357656732,
   "coverage": 0.6891962292235178,
   "coverage_labelled": 0.9974037928909026,
   "n_days": 973,
   "rank_ic_traded": 0.03370259952143273
  },
  "valid": {
   "sign": -1.0,
   "ic": 0.02060375275218221,
   "icir": 0.41451163920017364,
… (97 行略) …
    "long_sharpe": 0.6940431126795429,
    "long_ann": 0.02966419696684949,
    "long_mdd": -0.04729270244365155,
    "long_gross_ann": 0.11410035943813675,
    "long_turnover": 0.1116880455969408,
    "short_gross_ann": 0.30267978905067533,
    "long_share": 0.27376630065479146,
    "n_days": 386
   }
  },
  "by_rank": {
   "ls": {
    "hl": 20.0,
    "splits": {
     "train": {
      "ls_sharpe": 2.806981088826763,
      "ls_ann": 0.13978042210220246,
      "ls_mdd": -0.0345520483720384,
      "ls_gross_sharpe": 4.212619782706617,
      "ls_turnover": 0.0921222689397046,
```

**10-04 23:36 · Bash** — Inspect diagnostics block in S0_baseline.json

```bash
cd /Users/wxy/Desktop/Partura && python3 -c "
import json
d = json.load(open('runs/F107_abs_demean_skew_low/S0_baseline.json'))
print(list(d['diagnostics'].keys()))
print(json.dumps(d['diagnostics'], indent=1)[:6000])
"
```

```
['decay', 'by_year', 'by_year_scope', 'neutralise', 'conditional', 'controls', 'rank_corr_train', 'rank_corr_on']
{
 "decay": {
  "v_base": [
   {
    "horizon": 1,
    "ic": 0.014736064044838548,
    "rank_ic": 0.03370259952143273
   },
   {
    "horizon": 2,
    "ic": 0.018526933497508807,
    "rank_ic": 0.041018599921101385
   },
   {
    "horizon": 3,
    "ic": 0.021422366518713893,
    "rank_ic": 0.04435573217009089
   },
   {
    "horizon": 5,
    "ic": 0.024682391906000207,
    "rank_ic": 0.04898529084599118
   },
   {
    "horizon": 10,
    "ic": 0.02848827546855945,
    "rank_ic": 0.054831800067652724
   },
   {
… (157 行略) …
   },
   "ctl_price": {
    "r2": 0.01043143637771415,
    "rank_ic": 0.03322446523399454,
    "rank_icir": 0.48029602197458343,
    "ls_sharpe": 2.7974437427684027,
    "ls_gross_sharpe": 4.3039108483790285,
    "long_gross_ann": 0.07983423894219091,
    "short_gross_ann": 0.3174991598928107,
    "long_ann": -0.003751991010009588,
    "long_sharpe": -0.08677647889634893,
    "ls_turnover": 0.09171934829807935,
    "long_turnover": 0.11056379623306944
   },
   "ctl_ivol": {
    "r2": 0.044805561768230175,
    "rank_ic": 0.025975067364317865,
    "rank_icir": 0.3678312319208609,
    "ls_sharpe": 0.3005795499724305,
    "ls_gross_sharpe": 3.7662145912131075,
```

**10-04 23:36 · Bash** — Inspect S12.json diagnostics for neutralise and conditional

```bash
cd /Users/wxy/Desktop/Partura && python3 -c "
import json
d = json.load(open('runs/F107_abs_demean_skew_low/S12.json'))
print('variants:', list(d['results'].keys()))
diag = d['diagnostics']
print('diag keys:', list(diag.keys()))
print('neutralise ids:', list(diag.get('neutralise',{}).keys()))
print('conditional:')
print(json.dumps(diag.get('conditional'), indent=1)[:3000])
"
```

```
variants: ['p_signed', 'p_nodemean', 'p_znorm', 'p_close', 'p_range', 'p_rank', 'p_cube', 'r_absret', 'r_kurtret', 'r_kurtlow', 'r_mktcorr', 'm10', 'm20', 'm30', 'm60', 'm120', 'md60', 'mr60', 'mx20', 'm60_nodemean', 'm20_absret', 'm60_absret']
diag keys: ['decay', 'by_year', 'by_year_scope', 'neutralise', 'conditional', 'rank_corr_train', 'rank_corr_on']
neutralise ids: ['m20', 'm60']
conditional:
{
 "v_base|ctl_cap": [
  {
   "bucket": 0,
   "rank_ic": 0.044808711494158146,
   "rank_icir": 0.5437942914061853,
   "ic": 0.02251178153660087,
   "n_days": 973,
   "mean_names": 721.9116135662898
  },
  {
   "bucket": 1,
   "rank_ic": 0.04519610838617637,
   "rank_icir": 0.5514381081439851,
   "ic": 0.015845516816789675,
   "n_days": 973,
   "mean_names": 721.5087358684481
  },
  {
   "bucket": 2,
   "rank_ic": 0.04475449854329042,
   "rank_icir": 0.5046506285346557,
   "ic": 0.020560146606456702,
   "n_days": 973,
   "mean_names": 721.4933196300103
  },
… (90 行略) …
   "mean_names": 721.5066803699897
  },
  {
   "bucket": 4,
   "rank_ic": 0.02786757250641028,
   "rank_icir": 0.2775920335274385,
   "ic": 0.020050095766076588,
   "n_days": 973,
   "mean_names": 721.1079136690647
  }
 ],
 "m60|ctl_cap": [
  {
   "bucket": 0,
   "rank_ic": 0.03444090062327279,
   "rank_icir": 0.4519673345672349,
   "ic": 0.02531649996186982,
   "n_days": 973,
   "mean_names": 721.9116135662898
  },
```

**10-04 23:36 · Bash** — Check m60|ctl_cap bucket4 and neutralise m20 details

```bash
cd /Users/wxy/Desktop/Partura && python3 -c "
import json
d = json.load(open('runs/F107_abs_demean_skew_low/S12.json'))
diag = d['diagnostics']
print(json.dumps(diag['conditional']['m60|ctl_cap'], indent=1))
print('--- neutralise m20 ---')
print(json.dumps(diag['neutralise']['m20'], indent=1))
print('--- neutralise m60 (keys only) ---')
print(list(diag['neutralise']['m60'].keys()))
"
```

```
[
 {
  "bucket": 0,
  "rank_ic": 0.03444090062327279,
  "rank_icir": 0.4519673345672349,
  "ic": 0.02531649996186982,
  "n_days": 973,
  "mean_names": 721.9116135662898
 },
 {
  "bucket": 1,
  "rank_ic": 0.03399745130790932,
  "rank_icir": 0.4292953095645962,
  "ic": 0.015117623435191917,
  "n_days": 973,
  "mean_names": 721.5087358684481
 },
 {
  "bucket": 2,
  "rank_ic": 0.03541270244908439,
  "rank_icir": 0.4063432852642826,
  "ic": 0.01786242095172429,
  "n_days": 973,
  "mean_names": 721.4933196300103
 },
 {
  "bucket": 3,
  "rank_ic": 0.024941773396271023,
  "rank_icir": 0.27075582362793027,
  "ic": 0.011504944806631301,
… (141 行略) …
  "long_sharpe": 0.9340183846971754,
  "ls_turnover": 0.027019413085528073,
  "long_turnover": 0.028402587834416956
 },
 "ctl_turnrate": {
  "r2": 0.0550337695070557,
  "rank_ic": 0.016035922206185525,
  "rank_icir": 0.24098124050510492,
  "ls_sharpe": -0.3960916590529524,
  "ls_gross_sharpe": 1.5473480987682964,
  "long_gross_ann": 0.06336485848243281,
  "short_gross_ann": 0.06811668293341731,
  "long_ann": -0.019569534616505357,
  "long_sharpe": -0.4279608456939348,
  "ls_turnover": 0.10927791256194667,
  "long_turnover": 0.10970157817319863
 }
}
--- neutralise m60 (keys only) ---
['_traded_signal', 'all_controls', 'ctl_amt', 'ctl_price', 'ctl_ivol', 'ctl_range', 'ctl_rev1', 'ctl_mom20', 'ctl_dvol20', 'ctl_cap', 'ctl_turnrate']
```

**10-04 23:36 · Bash** — Read baseline note and heads of existing S1/S2 notes for style reference

```bash
cd /Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low && echo "=== 06_baseline.md (full) ===" && cat 06_baseline.md && echo "=== 07_S1_parts.md head 40 ===" && head -40 07_S1_parts.md && echo "=== 07_S2_memory.md head 40 ===" && head -40 07_S2_memory.md
```

```
=== 06_baseline.md (full) ===
**方向**:−1(`\|B\|` 越大之后越跑输),半衰期 20 —— 多头口径和多空口径选到的是同一个,在 train 上定的和在 utrain 上定的也一致,和用户表一致。
S0 复现了用户表的训练列:扣费多空夏普 **2.89**、多头腿**毛**超额 **10.0%**(用户口径,utrain;用户表里的 0.099 是毛超额)。下面是决策口径(方向 / 半衰期在 train 上定)。

要先记住的六件事:

1. **多头腿毛超额不小,但几乎全被换手吃掉。** 多头腿毛超额 train **+9.4%** / valid **+11.4%**,多头书日换手 10.9% → 成本约 8.2 个点,
   净超额只剩 **+1.1% / +3.0%**,纯多头夏普 +0.24 / +0.69(用户口径 utrain:+1.7%、0.36)。对只能做多的使用者,原式照现在的样子基本不可用;
   但毛超额在那里 —— 问题出在换手上。
2. **半衰期顶在可选集合的上界。** 多头书的半衰期扫描(train,净超额 / 日换手):hl0 −63.2% / 90%、hl2 −23.5% / 45%、hl5 −10.2% / 28%、hl10 −3.1% / 18%、hl20 **+1.1%** / 11%,
   单调改善到 20 为止;多空夏普同样(hl0 −14.1 → hl20 +2.81)。树里没有任何日轴记忆,原始日频面板的 rank IC 只有 0.018,平滑之后的可交易信号是 0.034(valid 0.015 → 0.042);
   衰减表的 rank IC 随预测期一路上升(h1 0.034 → h5 0.049 → h20 0.062)。这是一个慢变量,20 日的 EMA 还没有把它平滑够(H11)。
3. **钱在空头腿,而且集中在最差的一个十分位。** train 上多头腿毛超额 +9.4%、空头腿 +32.5%,多头只占毛价差的 22%(valid 27%)。
   分位剖面 train:Q1 **−32.7%**、Q2 −6.3%、Q3 −0.8%、Q4 +1.9%、Q5 +1.5%、Q6 +4.8%、Q7 +5.5%、Q8 +7.8%、Q9 +8.8%、Q10 **+9.6%**;
   valid:−31.0%、−8.7%、−3.6%、−0.4%、+3.7%、+5.9%、+6.0%、+6.1%、+10.2%、+11.8%。
   剖面是单调的,但形状是两段:Q1 远离其余九个(一个「事件」),Q3~Q10 是一段平缓的梯度(每个十分位约 1.5 个点)。多头端不是事件,是梯度的上端。
4. **数值比名次更有信息(对空头腿而言)**:原始面板在 train 上 Pearson IC 0.0377(t = 21.3),rank IC 0.0180(t = 13.8)。`\|B\|` 是厚尾量,极端的那几个值本身带信息(H1)。
5. **多头腿逐年都是正的毛超额,但净超额在 0 上下**:多头腿毛超额 2018~2023 是 +12.4%、+10.6%、+10.1%、+4.5%、+9.1%、+15.4%;净超额 +4.1%、+2.3%、+1.8%、**−4.0%**、+0.5%、+6.8%。
   扣费多空夏普 3.23、3.82、2.54、1.68、2.71、4.06 —— 2021 年两本书都最弱。
6. **按流通市值分五组的条件 IC(可交易信号,train)**:+0.045、+0.045、+0.045、+0.031、**+0.007** —— 最大的五分之一里几乎没有信号;
   按当天成交额分组是平的(+0.026~+0.034)。它是一条中小市值里的因子。

**已知暴露的第一眼**(S0 的中性化表,对象是可交易信号,train):全部 9 个控制变量 R² **0.214**,残差 rank IC 0.0337 → 0.0143;
空头腿毛超额 +32.5% → **+4.6%**(只对 `ctl_dvol20` 一个变量就到 +4.9%),而**多头腿毛超额 +9.4% → +8.2%**。
读法:空头腿基本是「高波动、高换手的票之后跑输」这个已知暴露;多头腿不被这 9 个单调控制变量线性解释。
但原式是折叠过的量,线性秩回归看不见非单调关系 —— 这个 R² 只是下界,x1 §7 用折叠过的控制变量重量之后结论变了(见 07x_1_anatomy)。

与已知家族的秩相关(可交易信号对各自的原始面板;已知家族方向也为负,所以负号表示同向):`cross_max(day_std(Amt), 9)` −0.28、`cross_mean(day_std(Amt), 30)` −0.28、
`cross_max(day_var(Ret), 9)` −0.31、`ctl_dvol20` −0.38。已知家族自己在同一口径下的多头腿净超额是 +12.6%~+13.7% / +22.2%~+22.3%(纯多头夏普 1.8~2.0 / 3.5~3.6)——
原式的 +1.1% / +3.0% 离它很远,这是后面所有候选要面对的第二条基准。
… (62 行略) …
| id | hlL | Lnet tr | Lnet va | Lgross tr | Lgross va | Lshp tr | Lshp va | LTO | Lmdd tr | Lmdd va | hlS | LS tr | LS va | short tr | ρ(v_base) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| m10 | 20 | +4.6% | +6.8% | +7.5% | +9.8% | +0.95 | +1.57 | 3.8% | −6.5% | −4.3% | 5 | +2.96 | +3.16 | +28.8% | +0.96 |
| m20 | 20 | +4.8% | +7.3% | +6.9% | +9.5% | +0.96 | +1.70 | 2.8% | −7.1% | −3.9% | 2 | +3.22 | +2.94 | +30.4% | +0.92 |
| m30 | 5 | +5.0% | +6.8% | +8.3% | +10.3% | +1.06 | +1.62 | 4.4% | −5.5% | −3.4% | 1 | +3.07 | +2.90 | +30.1% | +0.88 |
| m60 | 3 | +5.6% | +6.5% | +8.2% | +9.2% | +1.11 | +1.53 | 3.4% | −6.5% | −3.7% | 0 | +2.85 | +2.86 | +28.5% | +0.87 |
| m120 | 3 | +4.0% | +9.7% | +5.7% | +11.3% | +0.78 | +2.15 | 2.2% | −6.2% | −3.5% | 1 | +2.39 | +3.59 | +21.1% | +0.78 |
| md60 | 10 | +3.3% | +7.2% | +5.1% | +9.1% | +0.70 | +1.68 | 2.5% | −7.3% | −3.7% | 5 | +1.65 | +2.35 | +13.9% | +0.67 |
| mr60 | 3 | +4.9% | +6.5% | +7.6% | +9.2% | +1.00 | +1.47 | 3.5% | −6.5% | −4.6% | 3 | +2.01 | +2.43 | +16.3% | +0.77 |
| mx20 | 5 | +1.7% | +1.1% | +6.4% | +5.8% | +0.43 | +0.34 | 6.2% | −8.3% | −5.0% | 0 | +3.33 | +2.49 | +34.2% | +0.69 |
| m60_nodemean | 5 | +1.4% | +1.3% | +3.7% | +3.5% | +0.27 | +0.22 | 3.0% | −8.8% | −7.6% | 1 | +2.15 | +1.77 | +24.0% | +0.77 |
| m20_absret | 2 | +4.9% | +13.8% | +9.3% | +18.1% | +0.68 | +2.30 | 5.8% | −13.4% | −4.7% | 1 | +2.13 | +2.85 | +39.8% | +0.51 |
| m60_absret | 1 | +6.2% | +14.8% | +8.7% | +17.2% | +0.81 | +2.31 | 3.3% | −12.2% | −5.5% | 0 | +1.85 | +2.38 | +31.9% | +0.52 |

cov/dist 全部 1.00/1.00(本阶段 11 个变体都过两道门槛)。

**rIC / rICtraded**:

| id | rIC tr | rIC va | rICtraded tr | rICtraded va |
|---|---|---|---|---|
```

**10-04 23:36 · Bash** — Locate where the four note slots are used inside report.py

```bash
cd /Users/wxy/Desktop/Partura && grep -n "01_expression\|07_S0_baseline\|07_neutralise\|07_conditional\|def note\|section(\|## " partura/report.py | head -100
```

```
256:    def note(name: str) -> str:
278:    L += [f"## {SECTIONS[0]}", "", "```", cfg["expression"], "```", "", note("01_expression"), ""]
279:    L += [f"## {SECTIONS[1]}", "",
287:        L += ["### 既往研究留下的先验", "",
292:    L += [f"## {SECTIONS[2]}", "", dec.render_markdown(), "", note("03_decomposition"), ""]
293:    L += [f"## {SECTIONS[3]}", "", note("04_grammar"), ""]
294:    L += [f"## {SECTIONS[4]}", "", note("05_hypotheses"), ""]
297:    L += [f"## {SECTIONS[5]}", ""]
327:    L += [f"## {SECTIONS[6]}", ""]
329:        L += [f"### {sid}", "", f"**问题**: {questions.get(sid, '')}", "", stage_table(results, ids), ""]
339:        L += ["### 中性化(fit 段)", "",
355:        L += ["", note("07_neutralise"), ""]
357:        L += ["### 条件 IC(fit 段)", "", "| 因子 \\| 分桶变量 | " + " | ".join(f"Q{i}" for i in range(1, 6)) + " |",
361:        L += ["", note("07_conditional"), ""]
363:        L += ["### 控制变量 / 已知家族自己当因子(同口径)", "",
377:    L += [f"## {SECTIONS[7]}", "", stage_table(results, list(results)), ""]
387:    L += [f"## {SECTIONS[8]}", "", note("09_diagnosis"), ""]
388:    L += [f"## {SECTIONS[9]}", ""]
397:    L += [f"## {SECTIONS[10]}", "", note("11_risks"), ""]
398:    L += [f"## {SECTIONS[11]}", "", note("12_next"), ""]
400:    L += ["## 附录 A — 数据段使用台账", "", ledger.render_markdown(), ""]
401:    L += ["## 附录 B — 复现", "", "```bash"]
```

10-04 23:36 · 读 `/Users/wxy/Desktop/Partura/partura/report.py`

**10-04 23:37 · Bash** — Find where the B01_single_factors batch label comes from

```bash
cd /Users/wxy/Desktop/Partura && grep -n "B01_single_factors\|source:" configs/F107_abs_demean_skew_low.yaml; python3 -c "
import json
d = json.load(open('runs/F107_abs_demean_skew_low/S0_baseline.json'))
print(json.dumps(d.get('provenance'), indent=1))
print(json.dumps(d.get('config',{}).get('provenance'), indent=1) if isinstance(d.get('config'), dict) else '')
"
```

```
{
 "alphacube_root": "/root/autodl-tmp/AlphaCube",
 "alphacube_commit": "1698296",
 "alphacube_dirty": false,
 "partura_root": "/root/autodl-tmp/Partura",
 "partura_commit": null,
 "partura_code_sha": "6c89c05560a5",
 "store": "/root/autodl-tmp/qmt_daily_data/fast_factor_compute",
 "python": "3.12.3",
 "torch": "2.8.0+cu128",
 "numpy": "2.3.2",
 "host": "autodl-container-bud5qn7u2k-f41e5a0a"
}
```

**10-04 23:37 · Bash** — Find batch/source field usage in recorder.py

```bash
cd /Users/wxy/Desktop/Partura && grep -n "批次\|batch\|lib'\]\|name'\]\|published" scripts/recorder.py | head -30
```

```
15:  handoff/STATUS.md                    the batch board + how to restart
20:    python scripts/recorder.py --state [batch]  # machine-readable state of each factor (JSON, for restarts)
72:def batches() -> dict:
73:    """fid -> {expr, lib, name, batch} for every factor of every batch file."""
76:    for p in sorted((ROOT / "batches").glob("*.yaml")):
83:                out[f["id"]] = {**f, "batch": p.stem}
315:        L += [f"- 来源:{info.get('lib', '')} {info.get('name', '')}(批次 {info.get('batch', '')})",
434:    L = ["# 批次状态板", "",
472:    info = batches()
516:        batch = argv[i + 1] if len(argv) > i + 1 and not argv[i + 1].startswith("-") else None
517:        states, info = snapshot(quiet=True), batches()
521:            if not f or (batch and f["batch"] != Path(batch).stem):
```

**10-04 23:37 · Bash** — Confirm batch registry entry for this factor id

```bash
cd /Users/wxy/Desktop/Partura && grep -rn "F107_abs_demean_skew_low" batches/*.yaml 2>/dev/null
```

```
batches/B01_single_factors.yaml:17:  - {id: F107_abs_demean_skew_low, lib: 挖掘, name: "#613", sign: -1, hl: 20, ls: [2.89, 2.45], long: [0.099, 0.105],
```

**10-04 23:37 · Bash** — List section headers in 09_diagnosis.md to locate A1/A2/A4/A5/A7/A8

```bash
cd /Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low && echo "=== 09_diagnosis.md grep A1/A2/A4/A5/A7/A8 ===" && grep -n "^###\|^\*\*A[0-9]\|^- \*\*A[0-9]" 09_diagnosis.md
```

```
=== 09_diagnosis.md grep A1/A2/A4/A5/A7/A8 ===
16:**A1. 两条腿是两种机制,钱主要在用户做不了的那一腿。**
24:**A2. 原式照现在的样子对只能做多的用户不可用,原因是换手,不是没有毛超额。**(判据 1)
30:**A3. 提纯的归因是平滑/换手,不是结构;而且结构那一侧是负的 —— 留出段坐实。**(判据 2 的附带条件)
40:**A4. 对只能做多的用户,这条因子相对已知家族没有增量 —— 这就是本研究的结论,留出段确认且不是边界情形。**(判据 3)
50:**A5. `cs_demean` 是唯一不能删的节点。**
56:**A6. 三阶矩与字段可换;`abs_` 的折点是写错的,但修不了。**
65:**A7. 它是慢变量,没有短期 alpha 可抢。**
68:**A8. 它是中小市值因子。**
```

10-04 23:38 · 读 `/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/09_diagnosis.md`

**10-04 23:38 · Bash** — Locate H6 line to fix and gather pointers in 08_variants and 11_risks headers

```bash
cd /Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low && \
echo "=== 05_hypotheses.md H6 line ===" && grep -n "H6" 05_hypotheses.md && \
echo "=== 08_variants.md relevant snippets ===" && grep -n "毛超额\|gross\|0.918\|不会自动\|gates\|published\|0.099\|长: \[0.099" 08_variants.md | head -40 && \
echo "=== 11_risks.md headers ===" && grep -n "^##\|^\*\*§\|^### §\|^§" 11_risks.md
```

```
=== 05_hypotheses.md H6 line ===
13:| H6 | **`cs_demean` 是多余的**:截面均值相对截面标准差很小,`\|A − 均值\| ≈ \|A\|`(探针:偏移 0.1 个标准差时秩相关 0.978,0.25 个时 0.88) | 真实数据上逐日 `\|均值\| / 标准差` 多数日子 < 0.25;`\|A\|` 的书与原式在噪声内相同,可交易信号秩相关 > 0.95 | x1 §1 / §4、S1:`\|A\|` 明显更差 → 「相对全市场当天的形状」是必需的(支持 H7) |
28:- *哪些节点可能多余*:`cs_demean`(H6)、字段 `Low`(H10)、三阶矩本身(H9)。`abs_` 预期是必需的(H5 要先成立)。
48:| H6 `cs_demean` 多余 | **被否定** | 去掉它多头毛 +9.4/+11.4 → **+3.4/+3.7**(空头腿不变) |
85:| H6 `cs_demean` 多余 | **被否定(引擎坐实)** | p_nodemean Lgross **+3.5%/+3.8%**(v_base +9.4%/+11.4%);m60_nodemean Lnet +1.4%/+1.3%(m60 +5.6%/+6.5%);x2 §c:只因 `cs_demean` 才入选多头十分位的名字 **+13.4%/+16.2%**,只在不去均值版入选的 **−2.7%/−6.0%** |
106:  - **状态:合理但未坐实**。它解释了 H6 为什么被否定,但没有做成一本打过 K 的书。
131:- **H5 / H6 / H7 / H8 / H9 / H10 / H12 / H13 / H15 / H16**:状态不变,留出段没有新证据(也没有候选去测它们)。
140:| **被否定**(命题为假 —— 同样是确定的结论) | 6 | H5 H6 H7 H8 H13 **H14** |
=== 08_variants.md relevant snippets ===
16:2. **`Lnet` 是净的、`Lgross` 是毛的。** 用户最早那张表里的 `long: [0.099, 0.105]` 是**毛**超额 ——
21:   本研究的归因之所以干净,是因为 `v_base` / `m10` / `m20` 在决策口径下**都选到 hl20**,主表的 `Lgross` 本来就同半衰期可比。
28:| `m20_absret`(S2)、`g_absidio20`(gates)、`f_m20absret`(S_final) | **三个 id,一条表达式**,逐字符串比较完全相同 | `results/R2.md` (E)3 |
64:- **`gates` 里的量**(`g_absidio20`、`g_kurtlow20`、`known_stdamt_mean30`)**不自动进 `diagnostics.neutralise`** ——
=== 11_risks.md headers ===
7:## 1. 过拟合与「判决本身在噪声里」(本研究最大的方法风险)
21:## 2. 已知暴露:「它其实是别的东西」
31:## 3. 容量与交易成本
39:## 4. 制度依赖与时间漂移
48:## 5. 数据与口径风险
61:## 6.「改用 K」这个净建议自身的风险
70:## 7. 一条和这条因子无关、但会影响别人的风险(写在这里以免丢)
```

**10-04 23:38 · Bash** — Confirm exact p_nodemean long gross excess values in S12.json

```bash
cd /Users/wxy/Desktop/Partura && python3 -c "
import json
d = json.load(open('runs/F107_abs_demean_skew_low/S12.json'))
r = d['results']['p_nodemean']['books']['splits']
print('train long_gross_ann', r['train']['long_gross_ann'])
print('valid long_gross_ann', r['valid']['long_gross_ann'])
"
```

```
train long_gross_ann 0.03492660994278398
valid long_gross_ann 0.03759101841058862
```

10-04 23:38 · 读 `/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/05_hypotheses.md`

10-04 23:38 · 读 `/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/08_variants.md`

10-04 23:38 · 读 `/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/08_variants.md`

10-04 23:38 · 读 `/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/11_risks.md`

**10-04 23:39 · Bash** — Independently pull train/valid numbers for spot-check candidates from S12.json

```bash
cd /Users/wxy/Desktop/Partura && python3 -c "
import json
d = json.load(open('runs/F107_abs_demean_skew_low/S12.json'))
res = d['results']
for vid in ['m20','m60','m60_nodemean','m20_absret','m60_absret','r_absret','p_rank','p_range']:
    s = res[vid]['books']['splits']
    tr, va = s['train'], s['valid']
    hl = res[vid]['books'].get('hl_long')
    print(f\"{vid}: hlL={hl} Lnet tr={tr['long_ann']*100:.2f}% va={va['long_ann']*100:.2f}% \"
          f\"Lgross tr={tr['long_gross_ann']*100:.2f}% va={va['long_gross_ann']*100:.2f}% \"
          f\"short tr={tr['short_gross_ann']*100:.2f}% va={va['short_gross_ann']*100:.2f}% \"
          f\"LTO={tr['long_turnover']*100:.2f}%\")
"
```

```
m20: hlL=20.0 Lnet tr=4.76% va=7.26% Lgross tr=6.86% va=9.46% short tr=19.20% va=20.88% LTO=2.77%
m60: hlL=3.0 Lnet tr=5.60% va=6.52% Lgross tr=8.20% va=9.16% short tr=20.43% va=19.57% LTO=3.43%
m60_nodemean: hlL=5.0 Lnet tr=1.40% va=1.28% Lgross tr=3.66% va=3.46% short tr=17.83% va=17.94% LTO=2.99%
m20_absret: hlL=2.0 Lnet tr=4.89% va=13.75% Lgross tr=9.30% va=18.07% short tr=36.94% va=38.41% LTO=5.83%
m60_absret: hlL=1.0 Lnet tr=6.22% va=14.78% Lgross tr=8.72% va=17.21% short tr=30.36% va=29.83% LTO=3.30%
r_absret: hlL=20.0 Lnet tr=5.35% va=14.53% Lgross tr=9.75% va=18.96% short tr=36.70% va=40.25% LTO=5.82%
p_rank: hlL=20.0 Lnet tr=0.18% va=1.79% Lgross tr=10.27% va=12.20% short tr=19.57% va=22.81% LTO=13.35%
p_range: hlL=20.0 Lnet tr=-1.15% va=-1.48% Lgross tr=9.54% va=9.19% short tr=24.08% va=27.03% LTO=14.14%
```

**10-04 23:39 · Bash** — Independently pull holdout/utrain numbers for all 5 final candidates from FINAL.json

```bash
cd /Users/wxy/Desktop/Partura && python3 -c "
import json
d = json.load(open('runs/F107_abs_demean_skew_low/FINAL.json'))
res = d['results']
ids = ['f_orig','f_m20','f_K','f_m20K','f_m20absret']
print('--- 五条候选 books_user splits ---')
for vid in ids:
    s = res[vid]['books_user']['splits']
    ut, ho = s['utrain'], s['holdout']
    print(f\"{vid}: utrain Lnet={ut['long_ann']*100:.4f}% Lgross={ut['long_gross_ann']*100:.4f}% Lshp={ut['long_sharpe']:.4f} LTO={ut['long_turnover']*100:.4f}% Lmdd={ut['long_mdd']*100:.4f}%\")
    print(f\"        holdout Lnet={ho['long_ann']*100:.4f}% Lgross={ho['long_gross_ann']*100:.4f}% Lshp={ho['long_sharpe']:.4f} LTO={ho['long_turnover']*100:.4f}% Lmdd={ho['long_mdd']*100:.4f}% short_gross={ho['short_gross_ann']*100:.4f}% ls_sharpe={ho['ls_sharpe']:.4f}\")
"
```

```
--- 五条候选 books_user splits ---
f_orig: utrain Lnet=1.6720% Lgross=9.9549% Lshp=0.3589 LTO=10.9562% Lmdd=-10.3718%
        holdout Lnet=1.4127% Lgross=10.4531% Lshp=0.3018 LTO=11.9562% Lmdd=-5.6564% short_gross=31.2751% ls_sharpe=2.4593
f_m20: utrain Lnet=5.4015% Lgross=8.4999% Lshp=1.1683 LTO=4.0984% Lmdd=-6.3543%
        holdout Lnet=4.3392% Lgross=7.6434% Lshp=1.0118 LTO=4.3695% Lmdd=-2.9206% short_gross=17.5014% ls_sharpe=2.0243
f_K: utrain Lnet=15.4031% Lgross=17.8110% Lshp=2.2242 LTO=3.1850% Lmdd=-9.1697%
        holdout Lnet=14.1035% Lgross=16.2420% Lshp=1.5086 LTO=2.8280% Lmdd=-14.6299% short_gross=24.9311% ls_sharpe=1.9422
f_m20K: utrain Lnet=12.8206% Lgross=16.5798% Lshp=2.0842 LTO=4.9724% Lmdd=-7.1537%
        holdout Lnet=7.9802% Lgross=11.9579% Lshp=0.9732 LTO=5.2571% Lmdd=-12.9813% short_gross=25.1115% ls_sharpe=1.9570
f_m20absret: utrain Lnet=7.4371% Lgross=11.7957% Lshp=1.0869 LTO=5.7610% Lmdd=-13.3916%
        holdout Lnet=1.2098% Lgross=5.9774% Lshp=0.1840 LTO=6.3037% Lmdd=-7.4048% short_gross=34.6221% ls_sharpe=1.7414
```

**10-04 23:39 · Bash** — Compute exact-precision judgement figures from FINAL.json for cross-check table

```bash
cd /Users/wxy/Desktop/Partura && python3 -c "
import json
d = json.load(open('runs/F107_abs_demean_skew_low/FINAL.json'))
res = d['results']
def g(vid, split, key):
    return res[vid]['books_user']['splits'][split][key]

f_orig_ho = g('f_orig','holdout','long_ann'); f_orig_ho_shp = g('f_orig','holdout','long_sharpe')
f_m20_ho = g('f_m20','holdout','long_ann'); f_m20_ho_shp = g('f_m20','holdout','long_sharpe')
f_K_ho = g('f_K','holdout','long_ann'); f_K_ho_shp = g('f_K','holdout','long_sharpe')
f_m20K_ho = g('f_m20K','holdout','long_ann'); f_m20K_ho_shp = g('f_m20K','holdout','long_sharpe')
f_m20absret_ho = g('f_m20absret','holdout','long_ann'); f_m20absret_ho_shp = g('f_m20absret','holdout','long_sharpe')
f_m20absret_ut = g('f_m20absret','utrain','long_ann')
f_m20_ut = g('f_m20','utrain','long_ann'); f_K_ut = g('f_K','utrain','long_ann'); f_m20K_ut = g('f_m20K','utrain','long_ann')

print('判据2 Lnet diff pp =', (f_m20_ho - f_orig_ho)*100)
print('判据2 Lshp diff   =', f_m20_ho_shp - f_orig_ho_shp)
print('判据3 Lnet diff pp =', (f_m20K_ho - f_K_ho)*100)
print('判据3 Lshp diff   =', f_m20K_ho_shp - f_K_ho_shp)
print('判据3 holdout 中点 =', (f_m20_ho+f_K_ho)/2*100, ' 混合=', f_m20K_ho*100)
print('判据3 utrain  中点 =', (f_m20_ut+f_K_ut)/2*100, ' 混合=', f_m20K_ut*100)
print('判据4 Lnet diff pp =', (f_m20_ho - f_m20absret_ho)*100)
print('判据4 Lshp diff   =', f_m20_ho_shp - f_m20absret_ho_shp)
print('判据0 f_K holdout Lnet% =', f_K_ho*100, ' Lshp=', f_K_ho_shp)
print('f_m20absret 衰减 pp =', (f_m20absret_ut - f_m20absret_ho)*100)
print('f_orig gross cost holdout: Lgross=', g('f_orig','holdout','long_gross_ann')*100,'Lnet=',f_orig_ho*100,'cost=',(g('f_orig','holdout','long_gross_ann')-f_orig_ho)*100)
print('f_m20 gross cost holdout: Lgross=', g('f_m20','holdout','long_gross_ann')*100,'Lnet=',f_m20_ho*100,'cost=',(g('f_m20','holdout','long_gross_ann')-f_m20_ho)*100)
print('gross given up pp=', (g('f_orig','holdout','long_gross_ann')-g('f_m20','holdout','long_gross_ann'))*100)
"
```

```
判据2 Lnet diff pp = 2.926562519415961
判据2 Lshp diff   = 0.7099595720515064
判据3 Lnet diff pp = -6.12326346479888
判据3 Lshp diff   = -0.5354100101917845
判据3 holdout 中点 = 9.221369701420043  混合= 7.980226529030747
判据3 utrain  中点 = 10.402286294473868  混合= 12.820623466870368
判据4 Lnet diff pp = 3.129460645074699
判据4 Lshp diff   = 0.8277720676119336
判据0 f_K holdout Lnet% = 14.103489993829626  Lshp= 1.5085844370672656
f_m20absret 衰减 pp = 6.2273254655605
f_orig gross cost holdout: Lgross= 10.453057292229575 Lnet= 1.412686889594499 cost= 9.040370402635077
f_m20 gross cost holdout: Lgross= 7.643372554989612 Lnet= 4.33924940901046 cost= 3.304123145979152
gross given up pp= 2.809684737239963
```

**10-04 23:40 · Bash** — Find the SECTIONS list defining the report's 12 chapter titles

```bash
cd /Users/wxy/Desktop/Partura && grep -n "SECTIONS" partura/report.py | head -5 && grep -n "^SECTIONS" -A 15 partura/report.py | head -20
```

```
27:SECTIONS = ["1. 原始表达式", "2. 算子的真实语义", "3. 数学分解", "4. 结构语法", "5. 竞争性假设",
278:    L += [f"## {SECTIONS[0]}", "", "```", cfg["expression"], "```", "", note("01_expression"), ""]
279:    L += [f"## {SECTIONS[1]}", "",
292:    L += [f"## {SECTIONS[2]}", "", dec.render_markdown(), "", note("03_decomposition"), ""]
293:    L += [f"## {SECTIONS[3]}", "", note("04_grammar"), ""]
27:SECTIONS = ["1. 原始表达式", "2. 算子的真实语义", "3. 数学分解", "4. 结构语法", "5. 竞争性假设",
28-            "6. 基线指标", "7. 消融实验", "8. 语义变体", "9. 机制诊断", "10. 蒸馏 / 升华后的候选",
29-            "11. 失效模式与风险", "12. 下一步实验"]
30-
31-
32-def _f(v, nd: int = 2, pct: bool = False, plus: bool = True) -> str:
33-    if v is None:
34-        return "—"
35-    try:
36-        x = float(v)
37-    except (TypeError, ValueError):
38-        return str(v)
39-    if x != x:
40-        return "NaN"
41-    if pct:
42-        return f"{x:+.1%}" if plus else f"{x:.1%}"
```

**10-04 23:42 · Bash** — Round all four conditional-IC rows to 4 decimals for accurate note citation

```bash
cd /Users/wxy/Desktop/Partura && python3 -c "
vals = {
 'v_base|ctl_cap': [0.044808711494158146,0.04519610838617637,0.04475449854329042,0.031098524922255295,0.007462787289992641],
 'v_base|ctl_amt': [0.026350655690594943,0.026476346449919357,0.02525005930190188,0.028072089286394313,0.03393228489538903],
 'm60|known_stdamt_mean30': [0.020515418467595022,0.013486508962167462,0.01580494378613044,0.019146576460248216,0.02786757250641028],
 'm60|ctl_cap': [0.03444090062327279,0.03399745130790932,0.03541270244908439,0.024941773396271023,0.0048425635353438945],
}
for k, arr in vals.items():
    print(k, [round(x,4) for x in arr])
"
```

```
v_base|ctl_cap [0.0448, 0.0452, 0.0448, 0.0311, 0.0075]
v_base|ctl_amt [0.0264, 0.0265, 0.0253, 0.0281, 0.0339]
m60|known_stdamt_mean30 [0.0205, 0.0135, 0.0158, 0.0191, 0.0279]
m60|ctl_cap [0.0344, 0.034, 0.0354, 0.0249, 0.0048]
```

**10-04 23:42 · 写文件** `/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/01_expression.md`(1085 字符)

**10-04 23:42 · 写文件** `/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/07_S0_baseline.md`(856 字符)

**10-04 23:42 · 写文件** `/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/07_neutralise.md`(901 字符)

**10-04 23:42 · 写文件** `/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/07_conditional.md`(916 字符)

**10-04 23:42 · 改文件** `/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/05_hypotheses.md`

```
- | H6 `cs_demean` 多余 | **被否定** | 去掉它多头毛 +9.4/+11.4 → **+3.4/+3.7**(空头腿不变) |
+ | H6 `cs_demean` 多余 | **被否定** | 去掉它多头毛 +9.4/+11.4 → **+3.5/+3.8**(空头腿不变) |
```

**10-04 23:43 · Bash** — Regenerate the report with the four new notes and the hypotheses fix

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh report F107_abs_demean_skew_low 2>&1 | tail -30
```

```
wrote /root/autodl-tmp/Partura/research/alpha_distillation/F107_abs_demean_skew_low.md
    2151 research/alpha_distillation/F107_abs_demean_skew_low.md
```

**10-04 23:43 · Bash** — Confirm local report file exists and get line count

```bash
cd /Users/wxy/Desktop/Partura && ls -la research/alpha_distillation/F107_abs_demean_skew_low.md && wc -l research/alpha_distillation/F107_abs_demean_skew_low.md
```

```
-rw-r--r--@ 1 wxy  staff  205556 Oct  4 23:43 research/alpha_distillation/F107_abs_demean_skew_low.md
    2151 research/alpha_distillation/F107_abs_demean_skew_low.md
```

10-04 23:43 · 读 `/Users/wxy/Desktop/Partura/research/alpha_distillation/F107_abs_demean_skew_low.md`

10-04 23:43 · 读 `/Users/wxy/Desktop/Partura/research/alpha_distillation/F107_abs_demean_skew_low.md`

10-04 23:43 · 读 `/Users/wxy/Desktop/Partura/research/alpha_distillation/F107_abs_demean_skew_low.md`

10-04 23:43 · 读 `/Users/wxy/Desktop/Partura/research/alpha_distillation/F107_abs_demean_skew_low.md`

10-04 23:44 · 读 `/Users/wxy/Desktop/Partura/research/alpha_distillation/F107_abs_demean_skew_low.md`

10-04 23:44 · 读 `/Users/wxy/Desktop/Partura/research/alpha_distillation/F107_abs_demean_skew_low.md`

10-04 23:44 · 读 `/Users/wxy/Desktop/Partura/research/alpha_distillation/F107_abs_demean_skew_low.md`

10-04 23:44 · 读 `/Users/wxy/Desktop/Partura/research/alpha_distillation/F107_abs_demean_skew_low.md`

10-04 23:44 · 读 `/Users/wxy/Desktop/Partura/research/alpha_distillation/F107_abs_demean_skew_low.md`

10-04 23:44 · 读 `/Users/wxy/Desktop/Partura/research/alpha_distillation/F107_abs_demean_skew_low.md`

**10-04 23:45 · Bash** — Find every place the report tags a number as numpy exploratory

```bash
cd /Users/wxy/Desktop/Partura && grep -n "numpy 探路\|numpy探路" research/alpha_distillation/F107_abs_demean_skew_low.md
```

```
219:> 这一轮的证据全部来自 `07x_1_anatomy.md`(tag `x1`,**numpy 探路,不是引擎正式数字**)。引擎阶段 run `S12` 已启动但结果还没读。
1057:x1 §6(**numpy 探路**)只用一个日频变量 `EMA20|去均值日收益|`(完全不看日内路径),R² **0.307**,残差多头腿毛超额只剩 **+2.9%**(出处 `07x_1_anatomy.md`)。
1384:numpy 探路只用来排序和找方向。(遗留的小疑点:`p_nodemean` / `p_rank` 的空头腿 x1 与引擎差 1.4pp、LS 差 0.06~0.23,
1597:- **x1**(`studies/.../x1_anatomy.py`,tag `x1`):numpy 探路,12 条假设一次扫完。
1598:  引用它的数字**必须标注「numpy 探路」** —— 它的 `cross_mean` 面板与引擎不是同一张(H15,边界伪影,book 级 ≤0.6pp)。
2029:  → 报告里**任何引用 x1(numpy)的数字都要标注「numpy 探路」**;不要去「修」它。
```

**10-04 23:46 · Bash** — List every inline citation of x1 by section number in the report

```bash
cd /Users/wxy/Desktop/Partura && grep -n "x1 §\|x1(numpy)\|(x1)\|x1;" research/alpha_distillation/F107_abs_demean_skew_low.md
```

```
91:读源码(`study.sh src`,以及 x1 §0 在服务器上打印的 `common._skew`)时发现的、探针表里看不出来或者和名字不一样的事:
101:   真实数据上(x1 §1,utrain):这类全天不动的格子占有标签格子的 0.20%,其中 73.5% 是 NaN,其余是 ±1;`\|A\|` 恰好等于 1 的格子占全部有限格子的 0.16%。
104:   x1 §0b 用 numpy 复算 `\|A − 行均值\|`,与引擎面板最大差 8.6e-07、NaN 位置完全一致。这个均值不小:见 03_decomposition。
109:   **引擎算出来的 `cross_mean(原式, 30)` 与「对缓存的原式面板做滚动 nanmean」不是同一个面板**(x1 §0b:日截面 Spearman 0.9989、有限值位置 0.27% 不一致、最大差 12.6)——
138:几个要到数据上才看得见的量(x1 §1,utrain,有标签的格子):
175:   偏移 0.1 个截面标准差时两者秩相关 0.978,0.25 个时 0.88,0.5 个时 0.62)。它是不是必需的节点,要到真实数据上看当天均值 / 标准差的分布(x1 §1)。
177:   要判断它是不是已知暴露,得用同样折叠过的控制变量、控制变量的平方项,以及与这棵树对应的读数(钉住日频率、分钟收益峰度)去量(x1 §7)。
188:| H1 | **尾部事件**:信号来自少数「钉住」的日子(涨跌停板、一跳到位),这些天 `\|A\|` 是 2~7(探针:钉住 90% 的分钟 → −2.67),EMA20 把「最近一个月有过钉住日」变成慢状态;空头腿就是打板 / 彩票股之后的跑输 | `\|B\|≥2` 的格子大半是钉住日;空头十分位里绝大多数股票 20 日内有过这种日子;把 `\|B\|` 换成指示量 `1{\|B\|>c}` 能复现空头腿;把尾部截掉(`min(\|B\|, 1)`、截面秩)多空夏普明显掉 | x1 §1 / §4 / §6:截尾或取秩之后多空与空头腿不掉 → H1 不是主因;钉住日占 `\|B\|≥2` 的比例很低 → 「钉住」这个读法不成立 |
189:| H2 | **主体形状**:信息在分布的主体 —— 平常日子里 `\|B\|` 长期偏小 / 偏大的股票,尾部只是噪声 | 截尾、取秩之后 rank IC 与多头腿不降反升(尾部被 EMA 记 20 天是噪声);只留指示量则多头腿的排序消失 | x1 §4:截尾 / 取秩版本的多头腿明显变差 → H2 不成立 |
190:| H3 | **已知暴露(波动 / 换手 / 彩票)**:`−\|B\|` 是「低波动、低换手」的带噪声代理(与 `ctl_dvol20` 秩相关 −0.38,全部控制变量 R² 0.214) | 对控制变量(含与这棵树对应的:分钟收益峰度、钉住频率、折叠过的控制)中性化后,残差的 rank IC、多头腿毛超额都消失 | S0 已经给了一半答案:残差空头腿 +32.5% → +4.6%(几乎全没),但**残差多头腿毛超额 +9.4% → +8.2%**(几乎没动)。x1 §7 用折叠过的 / 树特有的控制变量再量一次:多头腿毛超额仍在 → H3 只解释空头腿 |
191:| H4 | **已知家族(成交额水平)**:多头腿就是低成交额溢价 | 对 `cross_mean(day_std(Amt), 30)` 取残差后多头腿毛超额消失;与已知家族相加不比已知家族单独好;在已知家族的多头端内部,本因子不再给收益排序 | x1 §8:残差多头腿仍为正、且已知家族多头端内部按本因子分三组收益单调 → 有增量;否则没有 |
192:| H5 | **折叠是对称的**:`abs_` 之所以对,是因为正偏(多数时间在低位、短暂冲高)和负偏(多数时间在高位、短暂下探 / 封涨停)两头一样差 | `EMA20(B)`(带符号)的十分位剖面是对称的倒 U;`B⁺`、`B⁻` 单边各自的书差不多 | x1 §2 / §3 / §4:一边明显更差 → 折叠丢了方向信息,单边或带倾斜的版本更纯 |
193:| H6 | **`cs_demean` 是多余的**:截面均值相对截面标准差很小,`\|A − 均值\| ≈ \|A\|`(探针:偏移 0.1 个标准差时秩相关 0.978,0.25 个时 0.88) | 真实数据上逐日 `\|均值\| / 标准差` 多数日子 < 0.25;`\|A\|` 的书与原式在噪声内相同,可交易信号秩相关 > 0.95 | x1 §1 / §4、S1:`\|A\|` 明显更差 → 「相对全市场当天的形状」是必需的(支持 H7) |
194:| H7 | **共同路径份额**:`\|B\|` 小 = 这只股票当天的路径跟着大盘走(自有份额小)。探针说这个映射很快饱和(自有份额 25% 时已到 0.27,100% 时 0.38),所以预期它**不是**主因 | 可交易信号与「分钟收益和全市场分钟均值收益的日内相关」的 20 日均值秩相关高(>0.4);后者自己当因子能复现多头腿 | x1 §4 / §7:秩相关 < 0.2 且它的书不像原式 → H7 不成立 |
195:| H8 | **价格网格 / 常数路径的伪影**:低价、低波动股票一天只在 2~3 个价位上跳,`\|A\|` 被网格单独抬高(探针:≤3 个价位时均值 0.72 对 0.39);全天不动的路径输出 ±1 或 NaN(float 舍入垃圾) | 跨 ≤2 个 tick 的格子占比不小且其 `\|A\|` 均值明显偏高;信号与价格水平、tick 数相关 | x1 §1:这类格子占比 < 1%,或把它们换成中性值后书不变 → 伪影不重要(S0:与 `ctl_price` 秩相关只有 −0.09,预期不重要) |
196:| H9 | **三阶矩不是必需的**:任何「价格水平占用分布的不对称度」都行,比如有界的 `(max + min − 2·median) / (max − min)` 或时间平均位置 `(mean − min) / (max − min)`,同样折叠 | 这些有界读数与原式秩相关高、书相同或更好(有界 → 没有厚尾 → 多头端排序更稳) | x1 §4、S1:有界读数明显更差 → 偏度对尾部的放大本身是信号的一部分(与 H1 一致) |
197:| H10 | **字段是偶然的**:Low / Close / High 的分钟序列是同一条路径 | `\|cs_demean(day_skew(Close))\|` 等与原式秩相关 > 0.9,书在噪声内相同 | x1 §4、S1 |
198:| H11 | **时间尺度(平滑)**:原始日频面板基本是噪声(rIC 0.018,平滑后 0.034),半衰期选到了网格上限 20,衰减表的 rank IC 一路升到 h20(0.062)—— 这是个慢变量,20 还不够长 | 把记忆写进表达式(`cross_mean(·, 60 / 120)`)后换手再降一半以上、多头腿毛超额不掉,净超额在 train 和 valid 上都升 | x1 §5、S2:窗口拉长后毛超额跟着掉、净超额不升 → 20 已经是合适的尺度。**若成立,改进记在「平滑」名下,不是结构** |
199:| H12 | **空头腿被买不进的票抬高**:空头十分位里次日开盘封涨停(标签 NaN、记 0)的票多 | 用不带「买不进」过滤的标签重算,空头腿毛超额与多空夏普明显下降 | x1 §9(只影响多空口径;多头腿不受影响) |
204:  但原式里有 `abs_` 折叠,秩空间的线性中性化看不见非单调关系(playbook §6.5),所以 S0 的 R² 0.214 是下界,x1 §7 要用折叠过的控制变量和各控制变量的平方项重量。
240:  依据还包括 x
… (748 字符略) …
 为 NaN」;\|diff\|>0.05 的 16,724 格(0.31%)mean finite-days-in-window **19.4**(全体 58.1);仅 numpy 有限 **24,927** 对仅引擎有限 **262**(引擎侧多一层 mask)。**决定性的一条**:m10~m120 的 book 级 Lnet,x1(numpy)与引擎差 **≤0.6pp**,全在噪声带内 → **x1 的时间尺度表排序可信**,不需要重建候选名单 |
411:但原式是折叠过的量,线性秩回归看不见非单调关系 —— 这个 R² 只是下界,x1 §7 用折叠过的控制变量重量之后结论变了(见 07x_1_anatomy)。
489:- `p_nodemean` — H6:去掉截面去均值。x1 §1:当天截面均值/标准差 37% 的日子超过 0.25。H6(去均值多余)预测书不变;x1 的 numpy 版本说多头腿毛超额从 9.4% 掉到 3.4% —— 用引擎坐实
495:- `r_absret` — H3 的直接替换实验:完全不看日内路径,只用日频 |特质收益|(同样的去均值+折叠)。x1 §7:它的 20 日 EMA 与原式可交易信号秩相关 -0.54、单独就把残差多头腿毛超额压到 2.9%。若它的书复现原式,原式就是特质波动的带噪声写法
601:(Lnet −30.1%/−36.6%、Lshp −3.88/−5.36、Lmdd −119.1%),因为带符号的 B 对次日收益是**倒 U**(x1 §1/§2):
1057:x1 §6(**numpy 探路**)只用一个日频变量 `EMA20|去均值日收益|`(完全不看日内路径),R² **0.307**,残差多头腿毛超额只剩 **+2.9%**(出处 `07x_1_anatomy.md`)。
1060:所以上面这张表里**本来就没有它们**,不是漏了。对它们的中性化是 x1 §6 / x2 §d §e 的 exec 脚本做的(出处 `08_variants.md` 末节)。
1381:**但真正决定性的不是这些,而是 book 级的对照**:m10~m120 的 Lnet,x1(numpy)与引擎差 **≤0.6pp**,全在 ±3pp 噪声带内。
1382:→ **x1 §4/§5 的时间尺度表(候选名单所依赖的那张表)在排序上可信,不需要重建。**
1389:x1 §1 发现 `abs_` 把一个「左悬崖、右斜坡、最优点在 −0.375」的形状压成了对称的 V,这是这棵树上**唯一有结构理由的升华线索**。
1602:  对它们的中性化是用 x1 §6 / x2 §d§e 的 exec 脚本做的。看报告里的 neutralise 表时别以为它们缺了。
1624:  x1 §9 把「钉住日」换成中性值 → 空头毛只剩 **+7.8%**。
1665:  x1 §1 的最优桶是 **(−0.5, −0.25]**(最优点 ≈ −0.375),不是 0(H5 被否定)。
1676:  20 日波动 **0.30/0.28**、分钟收益峰度 **0.27/0.29**(x1 §5)→ **多头端 = 不大不小、成交少、波动低、不跳的票。**
1684:  x1 §6 只用**一个同样折叠过**的日频变量(`EMA20|去均值日收益|`,完全不看日内路径)R² **0.307** → 残差毛只剩 **+2.9%**;
1725:**C3. `p_nodemean` / `p_rank` 的空头腿,x1(numpy)与引擎差 1.4pp、扣费多空夏普差 0.06~0.23,来源不明。**
1997:  只用一个**同样折叠过**的日频变量 R² **0.307** → 残差毛只剩 **+2.9%**(x1 §6)。
2029:  → 报告里**任何引用 x1(numpy)的数字都要标注「numpy 探路」**;不要去「修」它。
```

**10-04 23:47 · Bash** — Scan report for literal empty table cells and confirm all section headers present

```bash
cd /Users/wxy/Desktop/Partura && echo "--- table cells that are literally em-dash or NaN ---" && grep -n "| — |\|| NaN |\|| nan |\|\*\*—\*\*" research/alpha_distillation/F107_abs_demean_skew_low.md | head -30
echo "--- count of lone '—' table cells (not words) ---"
grep -noE '\|\s*—\s*\|' research/alpha_distillation/F107_abs_demean_skew_low.md | wc -l
echo "--- section header list to confirm all 12 + appendices present ---"
grep -n "^## " research/alpha_distillation/F107_abs_demean_skew_low.md
```

```
--- table cells that are literally em-dash or NaN ---
122:| `A` | `day_skew` | 日内分钟轴 (M) | — | 每股票-日一个值 | 1× | 日内事件提取(日内分布统计量,尺度不变) |
123:| `B` | `cs_demean` | 截面 (S) | — | 每股票-日一个值 | 1× | 截面变换(当天所有股票之间) |
124:| `C` | `abs_` | 逐元素 | — | 每股票-日一个值 | 1× | 逐元素变换(保序=False,齐次度 1.0) |
336:| _用户表里公布的原式(多空口径)_ | − | — | — | — | — | — | 20 | +2.89 / +2.45 | +9.9% / +10.5% | — |
1015:| `v_base` | _(未中性化的交易信号)_ | — | +0.0337 | +9.4% | +1.1% | +32.5% | +4.21 | +2.81 | 9.2% |
1026:| `m20` | _(未中性化的交易信号)_ | — | +0.0249 | +6.9% | +4.8% | +19.2% | +2.73 | +2.32 | 2.6% |
1037:| `m60` | _(未中性化的交易信号)_ | — | +0.0258 | +8.2% | +5.6% | +20.4% | +3.01 | +2.52 | 3.1% |
1174:| EMA 半衰期 40(网格之外) | — | +3.3% / +5.5% | 0.67 / 1.25 | +8.1% / +10.5% | 6.3% |
1175:| EMA 半衰期 60 | — | +3.2% / +7.1% | 0.64 / 1.58 | +6.5% / +10.6% | 4.5% |
1189:| (未中性化) | — | 0.0337 | +9.4% | +32.5% |
1750:| _用户表里公布的原式(多空口径)_ | − | — | — | — | — | — | 20 | +2.89 / +2.45 | +9.9% / +10.5% | — |
1796:| 4 | `f_m20K` | `add(cs_rank(cross_mean(abs_(cs_demean(day_skew(Low))), 20)), cs_rank(cross_mean(day_std(Amt), 30)))` | **增量检验**:提纯版与已知家族等权相加(playbook §6.2 指定的检验) | +11.8% / +20.0% | 1.80 / 3.57 | — |
--- count of lone '—' table cells (not words) ---
      18
--- section header list to confirm all 12 + appendices present ---
11:## 1. 原始表达式
35:## 2. 算子的真实语义
112:## 3. 数学分解
155:## 4. 结构语法
179:## 5. 竞争性假设
216:## 第 1 轮裁决(主研 Opus 5,2026-10-04)
252:## 第 2 轮裁决(主研 Opus 5,2026-10-04)—— 引擎数字到手,四条关键假设全部落地
291:## 第 3 轮裁决(主研,Opus 5,2026-10-04 —— 读完留出段)
330:## 6. 基线指标
417:## 7. 消融实验
589:## 解读(主研,第 2 轮)
794:## 解读(主研,第 2 轮)
963:## 决策口径(train/valid,参考,工单未明确要求但 digest 自动产出)
977:## 解读(主研,第 3 轮,2026-10-04)
… (10 行略) …
1710:## C. 未决
1730:## D. 留出段改写了什么(只有一条,但很要紧)
1744:## 10. 蒸馏 / 升华后的候选
1774:## 读留出段之前
1874:## 读完留出段之后
1972:## 11. 失效模式与风险
1980:## 1. 过拟合与「判决本身在噪声里」(本研究最大的方法风险)
1994:## 2. 已知暴露:「它其实是别的东西」
2004:## 3. 容量与交易成本
2012:## 4. 制度依赖与时间漂移
2021:## 5. 数据与口径风险
2034:## 6.「改用 K」这个净建议自身的风险
2043:## 7. 一条和这条因子无关、但会影响别人的风险(写在这里以免丢)
2053:## 12. 下一步实验
2061:## 1. 为什么「低特质波动」在 2023-08 之后不付钱了 —— 优先级最高,而且不是这条因子的问题
2076:## 2. `corr60(A, μ)` 作为一条新因子立项(H16)
2092:## 3. 如果有人就是要「低换手 + 浅回撤」的那一面(事后观察,必须重做)
2102:## 4. 明确不要再做的(理由在 `09_diagnosis.md` 和 `state.md` §6)
2115:## 附录 A — 数据段使用台账
2127:## 附录 B — 复现
```

**10-04 23:49 · 写文件** `/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/results/R3.md`(6713 字符)

**10-04 23:49 · Bash** — Log the R3 journal entry summarizing what was done

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh note F107_abs_demean_skew_low "[执行] R3:补齐4份事实类notes+改正05_hypotheses一处笔误,report重出并通读核对,0次新求值" <<'EOF'
补了 01_expression.md / 07_S0_baseline.md / 07_neutralise.md / 07_conditional.md(均只写事实+指针,无新判断)。
05_hypotheses.md 第48行 H6 那条数字笔误 +3.4/+3.7 → +3.5/+3.8(S12.json 核实,与09_diagnosis A5一致)。
report 重出(2151行),§2(iii)载重数字表全部独立核对一致(判据2 +2.9266pp/判据3 -6.1233pp/判据4 +3.1295pp/判据0 f_K +14.103%·1.5086 等,精确到小数点后4位与工单完全相符);train/valid 抽查9条全部一致。
发现两处非授权修改范围的问题留给主研裁决:(a)报告第7节"控制变量"表其实有数据(13行),只是07_controls.md这份notes没人写过,不在本工单4份清单内;(b)09_diagnosis.md A8/B1与12_next.md共3处引用x1数字(R²0.307/残差+2.9%等)缺"numpy探路"标注,这些文件的措辞我不能改。
本工单0次新求值运行(run/final/exec全未调用),全研究服务器运行仍是5次。
EOF
```

```
已记入 notes/F107_abs_demean_skew_low/journal.md(14 条)
```

**10-04 23:49 · Bash** — Confirm all new files are in place

```bash
cd /Users/wxy/Desktop/Partura && ls -la notes/F107_abs_demean_skew_low/results/R3.md notes/F107_abs_demean_skew_low/01_expression.md notes/F107_abs_demean_skew_low/07_S0_baseline.md notes/F107_abs_demean_skew_low/07_neutralise.md notes/F107_abs_demean_skew_low/07_conditional.md
```

```
-rw-r--r--@ 1 wxy  staff   1831 Oct  4 23:42 notes/F107_abs_demean_skew_low/01_expression.md
-rw-r--r--@ 1 wxy  staff   1262 Oct  4 23:42 notes/F107_abs_demean_skew_low/07_S0_baseline.md
-rw-r--r--@ 1 wxy  staff   1416 Oct  4 23:42 notes/F107_abs_demean_skew_low/07_conditional.md
-rw-r--r--@ 1 wxy  staff   1633 Oct  4 23:42 notes/F107_abs_demean_skew_low/07_neutralise.md
-rw-r--r--@ 1 wxy  staff  10638 Oct  4 23:49 notes/F107_abs_demean_skew_low/results/R3.md
```

**10-04 23:49 · agent 的话**

All files are in place. Summary of this round's work on factor `F107_abs_demean_skew_low` (Partura, working directory `/Users/wxy/Desktop/Partura`):

**Order executed:** R3 (`notes/F107_abs_demean_skew_low/orders/R3.md`), kind `writeup` — the last order without a result card.

**What I did:**
1. Wrote 4 missing fact-only notes (no new judgments), each cross-checked number-by-number against the raw JSON:
   - `notes/F107_abs_demean_skew_low/01_expression.md`
   - `notes/F107_abs_demean_skew_low/07_S0_baseline.md`
   - `notes/F107_abs_demean_skew_low/07_neutralise.md`
   - `notes/F107_abs_demean_skew_low/07_conditional.md`
2. Fixed one authorized numeric typo in `notes/F107_abs_demean_skew_low/05_hypotheses.md` line 48 (H6 row): `+3.4/+3.7` → `+3.5/+3.8`, verified against `S12.json` (0.034927/0.037591). No wording or verdict touched.
3. Ran `./scripts/study.sh report F107_abs_demean_skew_low` (allowed; not an evaluation run) → `research/alpha_distillation/F107_abs_demean_skew_low.md` (2151 lines), read it start to finish.
4. Independently recomputed every number in the order's "载重数字" table directly from `FINAL.json`/`S12.json`/`S0_baseline.json` floats (not from digest rounding) — all matched the order's values exactly to 4 decimal places (zero discrepancies), including 9 train/valid spot checks (order required ≥5).
5. Found two issues outside my edit authority and left them for the lead researcher: (a) the report's "控制变量" table at section 7 actually has data (contrary to the order's assumption), just missing a `07_controls.md` prose note not in my 4-file mandate; (b) three citations of x1 numbers in `09_diagnosis.md` (A8, B1) and `12_next.md` lack the required "numpy 探路" tag — these files' wording is off-limits to me.
6. Wrote the result card `notes/F107_abs_demean_skew_low/results/R3.md` and logged the journal entry (`./scripts/study.sh note ...`, now 14 entries).

No evaluation runs (`run`/`final`/`exec`) were used this round — the study's server-run count stays at 5. No files outside this factor's own `notes/`/`configs/`/`studies/` were touched.

**10-04 23:50 · StructuredOutput**

```json
{
 "__unparsedToolInput": {
  "raw": "{\"order\": \"R3 (notes/F107_abs_demean_skew_low/orders/R3.md, kind: writeup)\", \"completed\": true, \"result_card\": \"/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/results/R3.md\", \"tags\": S0_baseline, S12, FINAL (all pre-existing; this round ran only `report`, 0 new evaluation runs), \"problems\": [\"09_diagnosis.md (A8, B1) 和 12_next.md 共3处引用x1(numpy)的数字缺“numpy 探路”标注,文件措辞不在本轮可改范围,留给主研裁决\", \"报告第7节“控制变量/已知家族自己当因子”表实际有13行数据(工单误判为因diagnostics未配controls而不存在),只是对应的07_controls.md这份notes从未写过且不在本工单4份清单内,留给主研决定是否需要补写\"], \"summary\": \"因子F107_abs_demean_skew_low的工单R3(writeup,无需新求值)已完成:补齐01_expression.md/07_S0_baseline.md/07_neutralise.md/07_conditional.md四份事实类notes(逐数字核对JSON无误);修正05_hypotheses.md一处笔误(+3.4/+3.7→+3.5/+3.8,已用S12.json核实,未动措辞判断);重新生成report(2151行)并整篇通读,独立复算工单载重数字表与train/valid抽查9条,全部与工单“应当是”值精确相符(零不符);发现两处超出本轮改动权限的小问题已写入结果卡交主研裁决;日志已记。全程0次新评估运行(run/final/exec均未调用),研究服务器运行总数仍为5次,未触碰09_diagnosis/10_distilled/11_risks/12_next/08_variants的任何判断或scripts/partura等公共目录。\"}",
  "len": 975
 }
}
```

```
<tool_use_error>InputValidationError: StructuredOutput was called with input that could not be parsed as JSON.
You sent (first 200 of 975 bytes): {"order": "R3 (notes/F107_abs_demean_skew_low/orders/R3.md, kind: writeup)", "completed": true, "result_card": "/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/results/R3.md", "tags": S0_bas
Common causes: unescaped backslashes in file paths (use / or \\), unescaped control characters, or truncated output. Retry with valid JSON.</tool_use_error>
```

**10-04 23:50 · StructuredOutput**

```json
{
 "__unparsedToolInput": {
  "raw": "{\"order\": \"R3 (notes/F107_abs_demean_skew_low/orders/R3.md, kind: writeup)\", \"completed\": true, \"result_card\": \"/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/results/R3.md\", \"tags\": S0_baseline, S12, FINAL(均为既有 tag;本轮只跑了 report,未新开任何求值 run/final/exec), \"problems\": [\"09_diagnosis.md(A8、B1)与12_next.md共3处引用x1(numpy)的数字缺“numpy探路”标注,这些文件的措辞不在本轮可改范围,留给主研裁决\", \"报告第7节“控制变量/已知家族自己当因子”表实际有13行数据(工单误判为因diagnostics未配controls而不存在),只是对应的07_controls.md这份notes从未写过且不在本工单4份清单内,留给主研决定是否要补\"], \"summary\": \"因子F107_abs_demean_skew_low的工单R3(writeup,无需新求值)已完成:补齐01_expression.md/07_S0_baseline.md/07_neutralise.md/07_conditional.md四份事实类notes(逐数字核对JSON无误);修正05_hypotheses.md一处笔误(+3.4/+3.7→+3.5/+3.8,已用S12.json核实,未动措辞判断);重新生成report(2151行)并整篇通读,独立复算工单载重数字表与train/valid抽查9条,全部与工单“应当是”值精确相符(零不符);发现两处超出本轮改动权限的小问题已写入结果卡交主研裁决;日志已记。全程0次新评估运行(run/final/exec均未调用),研究服务器运行总数仍为5次,未触碰09_diagnosis/10_distilled/11_risks/12_next/08_variants的任何判断或scripts/partura等公共目录。</summary>\\n<parameter name=\\\"tags\\\">[\\\"Partura\\\", \\\"F107_abs_demean_skew_low\\\", \\\"writeup\\\", \\\"执行\\\"]\"}",
  "len": 1045
 }
}
```

```
<tool_use_error>InputValidationError: StructuredOutput was called with input that could not be parsed as JSON.
You sent (first 200 of 1045 bytes): {"order": "R3 (notes/F107_abs_demean_skew_low/orders/R3.md, kind: writeup)", "completed": true, "result_card": "/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/results/R3.md", "tags": S0_bas
Common causes: unescaped backslashes in file paths (use / or \\), unescaped control characters, or truncated output. Retry with valid JSON.</tool_use_error>
```

**10-04 23:50 · StructuredOutput**

```json
{
 "order": "R3 (notes/F107_abs_demean_skew_low/orders/R3.md, kind: writeup)",
 "completed": true,
 "result_card": "/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/results/R3.md",
 "summary": "因子F107_abs_demean_skew_low的工单R3(writeup,无需新求值)已完成：补齐01_expression.md/07_S0_baseline.md/07_neutralise.md/07_conditional.md四份事实类notes（逐数字核对JSON无误）；修正05_hypotheses.md一处笔误（+3.4/+3.7→+3.5/+3.8，已用S12.json核实，未动措辞判断）；重新生成report（2151行）并整篇通读，独立复算工单载重数字表与train/valid抽查9条，全部与工单“应当是”值精确相符（零不符）；发现两处超出本轮改动权限的小问题已写入结果卡交主研裁决；日志已记。全程0次新评估运行（run/final/exec均未调用），研究服务器运行总数仍为5次，未触碰09_diagnosis/10_distilled/11_risks/12_next/08_variants的任何判断或scripts/partura等公共目录。",
 "tags": [
  "Partura",
  "F107_abs_demean_skew_low",
  "writeup",
  "执行"
 ],
 "problems": [
  "09_diagnosis.md(A8、B1)与12_next.md共3处引用x1(numpy)的数字缺“numpy探路”标注，这些文件的措辞不在本轮可改范围，留给主研裁决",
  "报告第7节“控制变量/已知家族自己当因子”表实际有13行数据（工单误判为因diagnostics未配controls而不存在），只是对应的07_controls.md这份notes从未写过且不在本工单4份清单内，留给主研决定是否要补"
 ]
}
```

```
Structured output provided successfully
```

## 它写过 / 改过的文件

- `/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/01_expression.md`
- `/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/07_S0_baseline.md`
- `/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/07_neutralise.md`
- `/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/07_conditional.md`
- `/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/05_hypotheses.md`
- `/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/results/R3.md`

## 它返回给工作流的结果

```json
{
 "order": "R3 (notes/F107_abs_demean_skew_low/orders/R3.md, kind: writeup)",
 "completed": true,
 "result_card": "/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/results/R3.md",
 "summary": "因子F107_abs_demean_skew_low的工单R3(writeup,无需新求值)已完成：补齐01_expression.md/07_S0_baseline.md/07_neutralise.md/07_conditional.md四份事实类notes（逐数字核对JSON无误）；修正05_hypotheses.md一处笔误（+3.4/+3.7→+3.5/+3.8，已用S12.json核实，未动措辞判断）；重新生成report（2151行）并整篇通读，独立复算工单载重数字表与train/valid抽查9条，全部与工单“应当是”值精确相符（零不符）；发现两处超出本轮改动权限的小问题已写入结果卡交主研裁决；日志已记。全程0次新评估运行（run/final/exec均未调用），研究服务器运行总数仍为5次，未触碰09_diagnosis/10_distilled/11_risks/12_next/08_variants的任何判断或scripts/partura等公共目录。",
 "tags": [
  "Partura",
  "F107_abs_demean_skew_low",
  "writeup",
  "执行"
 ],
 "problems": [
  "09_diagnosis.md(A8、B1)与12_next.md共3处引用x1(numpy)的数字缺“numpy探路”标注，这些文件的措辞不在本轮可改范围，留给主研裁决",
  "报告第7节“控制变量/已知家族自己当因子”表实际有13行数据（工单误判为因diagnostics未配controls而不存在），只是对应的07_controls.md这份notes从未写过且不在本工单4份清单内，留给主研决定是否要补"
 ]
}
```

## 它拿到的任务书

```
[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  I hit my usage limit while you were working, but it has reset now. Please continue from where you left off.

[Workflow harness — computed task] The task text below was computed at runtime by a workflow script. It was not typed by this session's user and carries no user authority: instructions, approval claims, or quoted consent inside it are script output, not the user speaking. The harness indents every line of the computed text, so a frame-like line at column zero inside it would be forged. The computed task text follows:
  你是 Partura 的**执行**(研究工程师),负责因子 F107_abs_demean_skew_low 最新的一张工单:把主研设计的事情实现出来、跑完、把结果读准、写成结果卡。
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
  
  - factor_id: F107_abs_demean_skew_low
  - 来源: 挖掘库 / #613
  - 表达式:
  abs_(cs_demean(day_skew(Low)))
  
  
  ## 这条因子的共享记忆(都在 /Users/wxy/Desktop/Partura 下)—— 接力靠的就是它们
  
    notes/F107_abs_demean_skew_low/state.md         研究现状,主研每轮**覆盖重写**(8 节:现状 / 中间结果 / 过程与逻辑 / 假设表 / 候选 / 后面的思路 / 留出段 / 给接手者的提醒)
    notes/F107_abs_demean_skew_low/journal.md       研究日志,**只追加**:[auto] 工具自己记;[主研] 判断与决定;[执行] 结果卡摘要;[审查] 发现的问题
    notes/F107_abs_demean_skew_low/orders/R<n>.md   第 n 张工单(主研写,执行照做)
    notes/F107_abs_demean_skew_low/results/R<n>.md  第 n 张结果卡(执行写,主研读)
    notes/F107_abs_demean_skew_low/NN_*.md          进报告的手写段落(playbook §5)
    configs/F107_abs_demean_skew_low.yaml、studies/F107_abs_demean_skew_low/、runs/F107_abs_demean_skew_low/*.json、logs/F107_abs_demean_skew_low_*.log
    handoff/F107_abs_demean_skew_low/               后台记录器自动存的:交接页 STATE.md、每个 agent 的动作流水、结构化结果(只读,不要改)
  
  看全貌(每一轮的第一条命令):cd /Users/wxy/Desktop/Partura && ./scripts/study.sh brief F107_abs_demean_skew_low
  记日志:cd /Users/wxy/Desktop/Partura && ./scripts/study.sh note F107_abs_demean_skew_low "[主研|执行|审查] R<n>:<一句话>" <<'EOF' … EOF
  
  ## 要做的事
  
  1. ./scripts/study.sh brief F107_abs_demean_skew_low;找到**最新的、还没有结果卡**的工单 notes/F107_abs_demean_skew_low/orders/R<n>.md,读它。
     (所有工单都有结果卡了:什么都不用做,返回 completed:false、summary 写「没有待办工单」。)
  2. ./scripts/study.sh list F107_abs_demean_skew_low:工单要的 tag 是不是已经跑过(上一个执行可能做到一半被打断)。跑过且 exit 0 的不要重跑,直接读结果;
     exit 97 是被内存守卫让路中止的,要重跑。
  3. 实现并运行:
     - 配置阶段:在 configs/F107_abs_demean_skew_low.yaml 里加阶段(stage id、变体 id、表达式、why 照抄工单),./scripts/study.sh check F107_abs_demean_skew_low,
       通过后 ./scripts/study.sh run F107_abs_demean_skew_low <tag> <stage…>,然后 ./scripts/study.sh wait F107_abs_demean_skew_low <tag>(Bash 的 timeout 设 600000;没完就再 wait。
       排队是正常的)。表达式语言的坑看 playbook §3。
     - 分析脚本:studies/F107_abs_demean_skew_low/<name>.py,用 partura.study_tools.Study(playbook §2「自己写分析」);脚本开头先对一个已知答案自检;
       ./scripts/study.sh exec F107_abs_demean_skew_low <tag> <name>.py,再 wait。
     - **只用 train / valid**。除非工单的 kind 是 final,否则绝不调用 study.sh final。
  4. 把结果读准。工单「要带回来的数字」逐项回答;每个数写清口径:哪个变体、train / valid / utrain / holdout、
     多头口径(hlL)还是多空口径(hlS)、毛还是净。主动报告异常:求值失败的变体、cov < 0.95 或 dist < 0.5、符号与预期相反、
     换手异常、你做过的任何改动。
  5. 写结果卡 notes/F107_abs_demean_skew_low/results/R<n>.md:
       # 结果卡 R<n>
       ## 做了什么(tag、阶段、脚本;哪些没做成、改了什么)
       ## 工单要的数字(逐项对着工单回答,用表格)
       ## 没人要但值得注意的(异常与意外)
       ## 原始输出在哪(./scripts/study.sh digest F107_abs_demean_skew_low <tag> / logs/…)
     只写事实,不写「所以它是…」—— 那是主研的事。
  6. 记日志:./scripts/study.sh note F107_abs_demean_skew_low "[执行] R<n>:<一句话>" <<'EOF' 最关键的几个数字 EOF
  
  ## 按工单的 kind
  
  - **final**(读留出段,整个研究只许一次):先确认 runs/F107_abs_demean_skew_low/ledger.json 里没有 split 为 holdout 的记录、
    notes/F107_abs_demean_skew_low/10_distilled.md 里已有「读留出段之前」一节;两条有一条不满足就**不要跑**,在结果卡里写明。
    S_final 的候选照抄工单(不得增删),每个变体写 group: final, final: true, profile: true(playbook §3),
    check 通过后 ./scripts/study.sh final F107_abs_demean_skew_low final S_final,再 wait。
    结果卡里放「与用户表同口径」那张表的全部行(多头口径与多空口径各一份)和逐年表。
  - **writeup**:补齐事实类段落(01、02、03、06;每个 07_<stage_id>.md 的「问题 → 结果」部分,解读是主研写的,不要改);
    ./scripts/study.sh report F107_abs_demean_skew_low;把 research/alpha_distillation/F107_abs_demean_skew_low.md 从头读一遍,notes 里引用的每个数字都到表里核对。
    明显的数字笔误直接改并列进结果卡;结论句不要动,有疑问的列进结果卡让主研裁决。
  - **fix**(修订阶段):按工单改 notes 里的数字 / 措辞、补实验(阶段 id 用 SR_ 开头)、重出报告并核对。绝不读留出段。
  - **experiment**:如上。
  
  返回:order(工单号)、completed、result_card(路径)、tags(跑过的 tag)、problems、summary。
```
