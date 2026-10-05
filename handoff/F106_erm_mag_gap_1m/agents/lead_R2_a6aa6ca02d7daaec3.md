# lead:F106_erm_mag_gap_1m#2 — agent a6aa6ca02d7daaec3(工作流 wf_e3cc1b20-34b)

- 状态:**已返回结果**;开始 10-04 23:40,最后一次动作 10-05 00:02;工具调用 64 次
- 这是从 agent 的对话记录里**自动抽出来的动作流水**(命令、输出、写了哪些文件)。agent 的推理不在记录里 ——
  它的判断要看 `notes/F106_erm_mag_gap_1m/journal.md` 和各 notes 文件。输出过长的地方截了中间。

## 动作流水

**10-04 23:40 · agent 的话**

I'll start by getting the full picture.

**10-04 23:40 · Bash** — Get factor study overview

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh brief F106_erm_mag_gap_1m
```

```
# F106_erm_mag_gap_1m — 交接状态

_自动生成于 2026-10-04 23:40(`python scripts/recorder.py --brief F106_erm_mag_gap_1m` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:手写 erm_mag_gap_1m(批次 B01_single_factors)
- 表达式:`sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Ret, 0))), add(day_sum(is_gt(Ret, day_quantile(Ret, 0.95))), create_like(day_quantile(Ret, 0.95), 1e-06))), add(day_quantile(Ret, 0.95), create_like(day_quantile(Ret, 0.95), 1e-06))), div(div(day_sum(select_where(is_lt(Ret, day_quantile(Ret, 0.05)), abs_(Ret), create_like(Ret, 0))), add(day_sum(is_lt(Ret, day_quantile(Ret, 0.05))), create_like(day_quantile(Ret, 0.05), 1e-06))), add(abs_(day_quantile(Ret, 0.05)), create_like(day_quantile(Ret, 0.05), 1e-06))))`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- **留出段已经读过 1 次**(10-04 15:35)—— **不许再读**。候选在留出段上的数全在 `runs/F106_erm_mag_gap_1m/final.json`(`./scripts/study.sh digest F106_erm_mag_gap_1m final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `lead:F106_erm_mag_gap_1m#1`:已返回结果,最后动作 10-04 23:16 → `handoff/F106_erm_mag_gap_1m/agents/lead_R1_a805dc20e1bfb679c.md`
  - `work:F106_erm_mag_gap_1m#1`:已返回结果,最后动作 10-04 23:35 → `handoff/F106_erm_mag_gap_1m/agents/work_R1_a2cc3b41af9915b6e.md`
  - `lead:F106_erm_mag_gap_1m#2`:还在跑(多半就是你自己)

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F106_erm_mag_gap_1m` 看服务器上的 tag,`./scripts/study.sh digest F106_erm_mag_gap_1m <tag>` 重看结果)。

## 研究现状(`notes/F106_erm_mag_gap_1m/state.md`,10-04 23:15 更新)—— **先读这个文件**

# F106_erm_mag_gap_1m — 研究现状(主研第 3 轮覆盖重写,2026-10-04)

> 每轮覆盖重写,**≤150 行 / 10 KB**:只放结论与指针,细表在 `07x_1_anatomy.md`、`07x_2_longonly.md`、`05_hypotheses.md`、`10_distilled.md`、`results/R1.md`。

## 1. 一句话现状

**留出段已读(S_final,exit 0),事前登记的 C1~C6 六条判据全部按预期成立、一条都没被否定。结论定稿:分辨 —— 原样对纯多头用户不可用,相对已知家族没有可交易的增量。**
**本轮:R2 的结果卡还没写(执行被打断两次),按规矩把 R2 原样交回;结果卡一到就进 (c) 成文。**

(…全文 7389 字符,读 `notes/F106_erm_mag_gap_1m/state.md`)

## 研究日志(`notes/F106_erm_mag_gap_1m/journal.md`:12 条,其中研究员自己写的 7 条)

最近的 5 条(更早的和全文看文件):

### 2026-10-04 15:08 [主研] 第 2 轮:H10 被否定/H11 被支持但不产生候选/H12 改写;算出排除增量的天花板 → 不再做实验,直接读留出段(工单 R2 kind: final)

看到了什么(R1 的 x2 五节;我自己对着 logs/F106_erm_mag_gap_1m_x2.log 第 16~157 行核对过,结果卡准确):
- H10(排除性增量)按**事前登记的四条判据被否定**:(a)(b) 过,(c)(d) 不过。
  塌缩标记 ΔLnet 四格 +1.59/+0.52/+1.60/+0.40 —— train 有一点六,**valid 只剩 0.4~0.5 个点**,噪声是 ±3 个点;
  share 在 known9/valid 只有 0.016(低于 2% 门槛,全表 36 格唯一一格)。机制那半条是过的(被标记票次日超额四格全部远差于未标记票)。
- **这一轮最重要的新结果(我自己算的,不在结果卡里):天花板可以预测出来。**
  ΔLnet ≈ (被标记票占多头十分位的比例) × (标记与未标记的超额之差) = 2.0 / 0.70 / 1.93 / 0.57,
  与实测 +1.59/+0.52/+1.60/+0.40 **四格全部吻合到 25% 以内**。
  而 share 之所以低,是因为**已知家族本来就在躲这些票**:被标记票占全市场 8.0%/6.7%,
  占 known30 多头十分位只有 5.1%/2.2%、known9 只有 4.1%/1.6% → 相对持有频率只有 24%~64%(涨停标记 15%~37%)。
  → **不是 F106 的「不要买」清单不准,是已知家族本来就没买那些票。这张清单是多余的。** 这是整条研究解释力最强的一句话。
- H11(记忆太长)**被支持**:计数构造 rank IC 是 EMA-20(X) 的 1.7~4.8 倍、两段全优;叠加里 20 日窗口四格全面优于 60 日。
  **但它不产生候选**:优势只出现在取值几乎全是 0 的计数构造(过不了 dist ≥ 0.5),三条连续构造的 rank IC 反而低于原式。
- H12 **改写**:字面版(完全被朴素涨停替代)被否定 —— 残差 rank IC 保住 0.55×/0.26×(EMA20 涨停)、0.68×/0.79×(all four),
  折叠量 R² 0.444 不是 1.0。**但残差 Lnet 五行全负**(train −5.8%~−8.6%、valid −3.4%~−
…(这条日志还有后文,读 journal.md)

### 2026-10-04 15:29 [auto] ⚠ 读留出段:final S_final,阶段 S_final(留出段只能读这一次;候选与判据应当已经写在 10_distilled.md 里)

### 2026-10-04 15:35 [auto] S_final 跑完(exit 0);重看结果:./scripts/study.sh digest F106_erm_mag_gap_1m S_final

### 2026-10-04 23:16 [主研] 第 3 轮:R2 的 final 已跑完但结果卡被打断 → 按规矩原样交回(并在工单末尾写明禁止再跑 final);我自己读 S_final.json 裁决 C1~C6,六条全部成立,结论定稿=分辨

看到了什么:
- brief 显示留出段已读(10-04 15:35),但 notes/.../results/R2.md 和 07_S_final.md 都不存在 → 上一个执行跑完 final 之后被额度打断了两次。
  磁盘事实:runs/F106_erm_mag_gap_1m/S_final.json 存在(135 KB、seconds 310、errors 空、5 个变体全部求值成功);
  ledger.json 的 summary 里 holdout {reads: 1, expressions: 5} → 那唯一一次读取已经用掉了。
- 按工作流第 2 条(最新工单没有结果卡 → 不另开工单,原样交回),本轮返回 {status: order, order: R2, kind: final}。

这一轮我做的三件事:
1. **给 R2 补了一节「补充(主研第 3 轮)」**,这是本轮最要紧的动作:工单正文第 0~3 步写的是「怎么跑 final」,已经过时;
   如果换上来的执行照着做,就会第二次读留出段 —— 这项研究唯一不可挽回的错误。补充里写明:本轮服务器运行 = 0 次,
   跳过 check/final/run,直接 digest + 写两份文件;并逐项给了 JSON 路径与字段映射(books 是 train 拟合只报 train/valid,
   books_user 是 utrain 拟合、报 utrain/holdout → holdout 一律读后者),以及三件要照实写明的事:
   (a) 用的是主版不是兜底版(f_known30r 与 f_known30 的书逐项相同、rank 相关 1.000 → cs_rank 语义与预期一致);
   (b) holdout 的分位剖面「缺」(profile 只有 train/valid,f_known30r / f_excl_lu15 的 profile 是空的),不要重跑;
   (c) C3/C4 的读法必须降级并写明降级(见下)。
2. **自己读 S_final.json,按事前登记的判据裁决 C1~C6:六条全部成立,一条都没被否定。**
   f_orig holdout(用户口径,hl 在 utrain 上拟合
…(这条日志还有后文,读 journal.md)

### 2026-10-04 23:34 [执行] R2:留出段已读(本轮服务器运行0次,只digest+读JSON),S_final五条候选的数字已带回,结果卡与07_S_final.md写完

本轮没有调用 check/final/run/exec,只重看已跑完的 S_final(exit 0,10-04 15:35)+ 直接读 JSON 核对字段;ledger.summary.holdout={reads:1,expressions:5} 确认留出段没有被第二次读取。

C1/C2(f_orig holdout,books_user 用户口径,hlL=hlS=20):Lnet −3.19%、Lshp −0.69、Lgross −1.38%、LS +3.11 —— 与用户表 test 列(LS 3.11 / Lgross −1.4%)精确复现。
C5(f_known30 holdout):Lnet +14.10%、Lshp +1.51,落在用户给的 +13~15%/1.4~1.9 区间内。
C3/C4(排除性增量 ΔLnet,holdout,引擎各自拟合半衰期下的上界):f_excl_blown15−f_known30r = +0.54pp(hl1对hl0);f_excl_lu15−f_known30r = +0.75pp(hl1对hl0)。train/valid 口径下 C3 恰好是同hl的干净对照(+1.63pp / +0.57pp),C4 始终是不同hl的上界(+2.56pp / +1.22pp)。
C6:5个变体 cov(ic_holdout.coverage)全部 0.9675,dist 全部 ≥0.9933 —— 全过门槛。

核实的三件事:(1) 主版非兜底 —— 两条叠加候选 expr 字段核对都是 cs_rank 版;f_known30 与 f_known30r 在 hl0 下书逐项相同、rank相关(train)=1.000。(2) holdout 分位剖面缺(profile 字段只有 train/valid;f_known30r/f_excl_lu15 连 profile 字段都不存在)。(3) holdout 固定半衰期表缺(sweep 只在各自拟合段算),C3/C4 已按降级读法处理并在表里标出是否同一半衰期。

异常/值得注意:无求值失败、无 NaN;5 个变体 sign/sign_user 全部 −1;cov 这个数在 train(0.691)/valid(0.895)/utrain(0.749)/holdout(0.967)差
…(这条日志还有后文,读 journal.md)

## 工单与结果卡(`notes/F106_erm_mag_gap_1m/orders/`、`notes/F106_erm_mag_gap_1m/results/`)

- R1:工单 有,结果卡 有
- R2:工单 有,结果卡 有

## 配置里的实验计划(`configs/F106_erm_mag_gap_1m.yaml`)

- 标题:分钟收益右尾 ES/VaR 减左尾 ES/VaR;分母 +1e-6 在「上涨(下跌)分钟不足 5%」的日子塌掉,截面两端由这些日子决定
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base
- **S1_regime**(10 个变体):公布的多空夏普(和空头腿)是「塌缩日 = 封板事件」做出来的,还是「尾部形状不对称」做出来的?差的符号有没有信息?
  a_right、a_left、a_sum、a_abs、a_regular、a_eps3、a_flag、a_rankfirst、a_lockshare、a_limitup
- **S_final**(5 个变体):读留出段之前写死的结论(原式多头腿全负 / 排除性增量在噪声以下 / 和已知家族相加更差)在用户的测试段(20230808–20251231)上成不成立?
  f_orig、f_known30、f_known30r、f_excl_blown15、f_excl_lu15

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F106_erm_mag_gap_1m`)

- `S0_baseline`  10-04 11:50  1 个变体  → `./scripts/study.sh digest F106_erm_mag_gap_1m S0_baseline`
- `S_final`  10-04 15:35  5 个变体  → `./scripts/study.sh digest F106_erm_mag_gap_1m S_final`
- `x1`(自写脚本的输出)  10-04 12:30  exit 0  → `logs/F106_erm_mag_gap_1m_x1.log`
- `x2`(自写脚本的输出)  10-04 13:54  exit 0  → `logs/F106_erm_mag_gap_1m_x2.log`

## 已写的 notes(`notes/F106_erm_mag_gap_1m/`)

`01_expression.md`(1K)、`02_operators.md`(2K)、`03_decomposition.md`(3K)、`04_grammar.md`(1K)、`05_hypotheses.md`(19K)、`06_baseline.md`(3K)、`07_S_final.md`(13K)、`07x_1_anatomy.md`(10K)、`07x_2_longonly.md`(23K)、`10_distilled.md`(7K)、`journal.md`(22K)、`state.md`(12K)

## 自写的探针与分析脚本(`studies/F106_erm_mag_gap_1m/`)

- `probes.py`  10-04 12:13  Probes this tree needs:  ES/VaR of the right tail of minute returns  minus  ES/VaR of the left tail.
- `x1_anatomy.py`  10-04 12:19  x1 -- what the ES/VaR gap tree reads on REAL data, and who sits at the ends of the traded signal.
- `x2_longonly.py`  10-04 13:02  x2 -- for a LONG-ONLY user: does this factor add anything to the known amount-level family?

## 结构化结果(`handoff/F106_erm_mag_gap_1m/results/`)

(还没有)
```

**10-04 23:40 · agent 的话**

Holdout已读、R2结果卡已到 → 这一轮必须是 (c) 成文。先读关键文件。

**10-04 23:41 · Bash** — Read state.md and R2 result card

```bash
cd /Users/wxy/Desktop/Partura && echo "=====STATE=====" && cat notes/F106_erm_mag_gap_1m/state.md && echo "=====R2_RESULT=====" && cat notes/F106_erm_mag_gap_1m/results/R2.md
```

```
=====STATE=====
# F106_erm_mag_gap_1m — 研究现状(主研第 3 轮覆盖重写,2026-10-04)

> 每轮覆盖重写,**≤150 行 / 10 KB**:只放结论与指针,细表在 `07x_1_anatomy.md`、`07x_2_longonly.md`、`05_hypotheses.md`、`10_distilled.md`、`results/R1.md`。

## 1. 一句话现状

**留出段已读(S_final,exit 0),事前登记的 C1~C6 六条判据全部按预期成立、一条都没被否定。结论定稿:分辨 —— 原样对纯多头用户不可用,相对已知家族没有可交易的增量。**
**本轮:R2 的结果卡还没写(执行被打断两次),按规矩把 R2 原样交回;结果卡一到就进 (c) 成文。**

## 2. 中间结果

### 2.1 留出段(本轮主研直接读 `runs/F106_erm_mag_gap_1m/S_final.json`;**用户口径** = 方向/半衰期在 utrain 上拟合、报 `books_user.splits.holdout`;20230808–20251231,581 天)

| id | sign | dist | hlL | **Lnet** | Lgross | **Lshp** | LTO | LS | short | cov |
|---|---|---|---|---|---|---|---|---|---|---|
| `f_orig` 原式 | −1 | 0.993 | 20 | **−3.19%** | −1.38% | **−0.69** | 2.40% | +3.11 | +24.7% | 0.967 |
| `f_known30` 已知家族 | −1 | 1.000 | 0 | **+14.10%** | +16.24% | **+1.51** | 2.83% | +1.94 | +24.9% | 0.967 |
| `f_known30r` cs_rank 版 | −1 | 1.000 | 0 | +14.10%(与上行**逐项相同**) | | +1.51 | | +1.94 | | 0.967 |
| `f_excl_blown15` 叠加 | −1 | 1.000 | **1** | +14.64% | +16.57% | +1.57 | 2.55% | +3.29 | +37.6% | 0.967 |
| `f_excl_lu15` 朴素涨停叠加 | −1 | 1.000 | **1** | +14.85% | +16.74% | +1.60 | 2.49% | +3.52 | +47.3% | 0.967 |

逐年多头腿净超额(`diagnostics.by_year`,2018→2025;**2023 跨分界 20230808,holdout 干净整年只有 2024/2025**):
`f_orig` −9.2/−6.2/−8.6/−4.1/−0.8/−6.7/**−5.1**/**−0.4**% → **八年全负**;`f_known30` +17.3/+10.2/+6.6/+16.0/+24.6/+21.2/**+9.2**/**+14.3**% → 八年全正。
rank 相关(train 段,`diagnostics.rank_corr_train`):`f_orig`↔`f_known30` **0.005**(近乎正交);`f_known30r`↔`f_known30` **1.000**;叠加↔基准 0.922/0.892;两张标记互相 **0.893**(抓同一批票)。
**用户公布的 test 列被精确复现**:用户表 多空夏普 **3.11** / 多头腿毛 **−1.4%**,我们 holdout **3.108** / **−1.38%** → 「原样不可用」不是口径差异。

### 2.2 C1~C6 裁决(判据**读之前**写死在 `10_distilled.md`「读留出段之前」;**下一轮 (c) 照抄,不要重算、不要换推荐**)

| | 事前判断 | 留出段实测 | 裁决 |
… (120 行略) …
`profile` 字段里没有 `holdout` 键(工具没有算,不是遗漏重跑);`f_known30r`、`f_excl_lu15` 连 `profile` 字段本身都不存在。能看的只有 `f_orig`、`f_known30`、`f_excl_blown15` 的 train/valid 两段,`f_orig` 的倒 U 形在这两段都还在(Q1、Q10 两端明显弱于中段)。

### rank 相关(train 段,交易信号;详见 `07_S_final.md` §8)

f_orig ↔ f_known30 = **+0.0055**(几乎正交);f_excl_blown15 ↔ f_known30r = **+0.923**;f_excl_lu15 ↔ f_excl_blown15 = **+0.893**。

## 没人要但值得注意的(异常与意外)

- **没有求值失败,没有 NaN 异常,5 个变体 `errors` 全空。**
- `sign`/`sign_user` 对全部 5 个变体都是 −1(包括 `f_known30r`)——不存在叠加候选被反着读的风险。
- `cov`(ic_holdout.coverage)这个数在 train(0.691)/valid(0.895)/utrain(0.749)/holdout(0.967)之间差异很大,但对 5 个变体完全相同 —— 看起来是面板覆盖率随日历时间上升的结构性统计量,不是任何表达式求值失败;C6 门槛用的是 holdout 这一档(0.967),全过。
- `diagnostics.by_year` 到底是按 `books`(train 拟合半衰期)还是 `books_user`(utrain 拟合半衰期)算的,JSON 里没有字段标注;`f_excl_blown15` 是唯一两套 hl 不同的变体,但它的数字落在两种假设中间,没能排除任何一种。不影响本卡引用的 f_orig / f_known30 的逐年读数(这两条在两套口径下 hl 是一样的,没有歧义),只是提醒这张表的 hl 来源有一点不确定。
- C3 在 train/valid 恰好是同一半衰期的干净对照(两边都拟合到 hl0),但到 utrain/holdout `f_excl_blown15` 自己拟合出的 hl 变成 1,C3 就变成了上界;C4 在全部四段里 `f_excl_lu15` 的 hl 始终是 1、`f_known30r` 始终是 0,所以 C4 从来都不是同一半衰期的对照。这一点 §4 已经按表列出,这里只是提醒:C3 和 C4 的「干净程度」不一样。

## 原始输出在哪

- `./scripts/study.sh digest F106_erm_mag_gap_1m S_final`
- `runs/F106_erm_mag_gap_1m/S_final.json`(135KB)、`runs/F106_erm_mag_gap_1m/ledger.json`
- `logs/F106_erm_mag_gap_1m_S_final.log`
- 完整数据表(sweep 全表、分位剖面、逐年、rank 相关矩阵):`notes/F106_erm_mag_gap_1m/07_S_final.md`
```

**10-04 23:41 · Bash** — Read 10_distilled.md, notes listing, playbook section 5

```bash
cd /Users/wxy/Desktop/Partura && echo "=====10_DISTILLED=====" && cat notes/F106_erm_mag_gap_1m/10_distilled.md && echo "=====LS=====" && ls -la notes/F106_erm_mag_gap_1m/ && echo "=====PLAYBOOK5=====" && sed -n '/^## *§*5/,/^## *§*6/p' docs/study_playbook.md | head -80
```

```
=====10_DISTILLED=====
# 10 — 最终候选、排序与判据

---

## 读留出段之前(主研第 2 轮写,2026-10-04;写在 `study.sh final` 之前,之后一个字不改)

> 这一节是**事前登记**。留出段(20230808–20251231 = 用户的测试段)整个研究只读一次。
> 下面的候选集合、排序、判据,**只用 train(20180102–20211231)和 valid(20220101–20230807)的证据**定出来。
> 读完之后另起一节「读完留出段之后」,逐条写判据过了还是被否定;**推荐就是下面的第一推荐,被否定就写被否定**(playbook §6.4)。

### 这条研究的结论类型:**分辨**(不是提纯、不是升华)

**没有任何 F106 变体进入推荐。** 理由(全部来自 train/valid,出处见 `state.md` §2、`05_hypotheses.md` 裁决):

1. 原式的多头腿净超额在**半衰期网格的每一个点**(0/1/2/3/5/10/20)、train 和 valid、**毛和净全都是负的**
   (train −67.2% → −6.9%,valid −3.2%);分位剖面是**倒 U**(train Q1 −28.4%、Q10 −5.3%),两端都是近期封板股。
2. 「原式 + 多头最优半衰期」**就是用户表里公布的那一行本身**(hlL = hlS = 20)—— 这条因子没有「延长半衰期」这条免费改进。
3. 这棵树派生出的**所有连续构造**(只留常规日 / 先排序再 EMA / clip(±3) / 只留 R / 只留 L / 折叠 / log(1+\|X\|) / R+L / log(1+R+L)),
   多头腿净超额在 train 和 valid **同时为正的一个都没有**。
4. 和已知家族相加:24 行(2 方向 × 3 权重 × 2 家族 × 2 段)**没有一行**好于已知家族自己,且随权重单调下降。
5. 排除性叠加(H10):方向对、机制看得见,但 **valid 上只剩 +0.4~+0.5 个点**,而噪声是 **±3 个点**;
   而且天花板是结构性的 —— 已知家族持有被标记票的频率只有全市场的 24%~64%,**它本来就在躲这些票**。
6. 唯一在 valid 上拿到一个点以上的标记是 `listed < 250d`(+1.09 / +1.95)——**那是新股过滤器,不是这条因子的功劳**。

### 最终候选(5 条,排序 = 第一推荐在前)

| 名次 | id | 是什么 | train / valid 多头口径(已有数字) | 为什么在表里 |
|---|---|---|---|---|
| **1** | `f_known30` | `cross_mean(day_std(Amt), 30)` —— **已知家族基准**(规则要求必含) | sign −1、hlL **0**;Lnet **+12.6% / +22.3%**;Lshp **+1.78 / +3.46**;LTO 3.4% / 2.8% | **第一推荐,但它不是这条因子的产物。** 对只能做多的用户,这条研究唯一可操作的输出是「F106 不要进书,继续用已知家族」。留出段要确认这本书在用户的测试段上仍然成立(用户给的参考:+13%~+15%、夏普 1.4~1.9) |
… (40 行略) …
_(留出段还没读。读完之后在这里逐条写 C1~C6 过了还是被否定、推荐是谁。)_
=====LS=====
total 280
drwxr-xr-x@ 16 wxy  staff    512 Oct  4 23:33 .
drwxr-xr-x@ 19 wxy  staff    608 Oct  4 13:07 ..
-rw-r--r--@  1 wxy  staff   1323 Oct  4 12:15 01_expression.md
-rw-r--r--@  1 wxy  staff   2769 Oct  4 12:15 02_operators.md
-rw-r--r--@  1 wxy  staff   3249 Oct  4 12:15 03_decomposition.md
-rw-r--r--@  1 wxy  staff   1562 Oct  4 12:15 04_grammar.md
-rw-r--r--@  1 wxy  staff  19561 Oct  4 14:53 05_hypotheses.md
-rw-r--r--@  1 wxy  staff   3247 Oct  4 12:20 06_baseline.md
-rw-r--r--@  1 wxy  staff  14084 Oct  4 23:33 07_S_final.md
-rw-r--r--@  1 wxy  staff  10386 Oct  4 12:41 07x_1_anatomy.md
-rw-r--r--@  1 wxy  staff  24250 Oct  4 14:53 07x_2_longonly.md
-rw-r--r--@  1 wxy  staff   8010 Oct  4 14:56 10_distilled.md
-rw-r--r--@  1 wxy  staff  23201 Oct  4 23:34 journal.md
drwxr-xr-x@  4 wxy  staff    128 Oct  4 14:59 orders
drwxr-xr-x@  4 wxy  staff    128 Oct  4 23:33 results
-rw-r--r--@  1 wxy  staff  12376 Oct  4 23:15 state.md
=====PLAYBOOK5=====
```

**10-04 23:41 · Bash** — Find notes file spec in playbook

```bash
cd /Users/wxy/Desktop/Partura && grep -n "0[89]_\|1[12]_\|13_\|notes 文件" docs/study_playbook.md | head -40
```

```
202:| `08_variants.md` | 怎么读总表、哪些变体其实是同一个东西 |
203:| `09_diagnosis.md` | 机制诊断:已确立 / 合理但未坐实 / 未决 |
205:| `11_risks.md` | 失效模式:泄漏、过拟合、尺度污染、已知暴露、容量、成本、制度依赖 |
206:| `12_next.md` | 只列能显著降低不确定性的下一步 |
```

**10-04 23:41 · Bash** — Read playbook notes file table

```bash
cd /Users/wxy/Desktop/Partura && sed -n '190,225p' docs/study_playbook.md
```

```
| 文件 | 内容 |
|---|---|
| `journal.md` | 研究日志(§7):只追加;每看完一个结果一条。不进报告正文,是给接手的人看的 |
| `01_expression.md` | 这条因子的来历、一句话说它是什么 |
| `02_operators.md` | (可选)读源码时发现的、探针表里看不出来的事 |
| `03_decomposition.md` | 分解表之外需要说明的:关键公式、容易被名字骗的地方 |
| `04_grammar.md` | 结构语法:事件 → 记忆 → 门控 → 放大… |
| `05_hypotheses.md` | 竞争性假设表:每条写"预测什么""哪个实验能杀死它"。**在跑实验之前写** |
| `06_baseline.md` | 基线读法:多头腿在两种半衰期下各是多少、钱在多头腿还是空头腿、分位剖面是不是单调、逐年、衰减 |
| `07_<stage_id>.md` | 每个阶段的结论(问题 → 结果 → 解读),文件名里的 stage_id 要和配置一致 |
| `07_neutralise.md` / `07_conditional.md` / `07_controls.md` | 对应诊断表的解读 |
| `07x_<序号>_<name>.md` | 自己写的分析(studies/ 下脚本)的结果与解读;加序号是因为报告按文件名排序拼接 |
| `08_variants.md` | 怎么读总表、哪些变体其实是同一个东西 |
| `09_diagnosis.md` | 机制诊断:已确立 / 合理但未坐实 / 未决 |
| `10_distilled.md` | **读留出段之前**:候选排序与判据;**读之后**:结果、推荐、为什么比原式好(或为什么没有更好的) |
| `11_risks.md` | 失效模式:泄漏、过拟合、尺度污染、已知暴露、容量、成本、制度依赖 |
| `12_next.md` | 只列能显著降低不确定性的下一步 |

最后 `./scripts/study.sh report <fid>`,并**把生成的报告从头读一遍**:表里有没有空的、notes 里引的数字和表对不对得上。

---

## 6. 第一组研究里,审查反复抓到的问题(开工前读;不要等审查来抓)

第一组五条因子的研究都被独立审查提了 3~6 条 major。下面这些是**重复出现**的,和具体因子无关:

1. **归因写错:把平滑的功劳记到结构头上**。原式按多空口径选到的半衰期常常很短(1~3);候选选到 10 或 20,
   换手减半,多头腿净超额自然高几个点。这个改进是**真的、可以推荐**(见 §0),但要写成「来自更长的半衰期」。
   想说「结构更好」,就必须在**同一个半衰期**下比(固定半衰期表),并且比过 `v_base` 的多头口径那一行。
2. **「升华版」其实是已知家族**。候选的多头腿好,是因为它滑向了成交额水平家族(`cross_max/mean(day_std(Amt), 9~60)`:
   第一组里它在测试段的多头腿净超额是 +13%~+15%、纯多头夏普 1.4~1.9)。推荐它没问题,但要**说清楚它是什么**:
   「对只能做多的用户,这条因子相对已知家族有 / 没有增量」。有没有增量的检验:候选对已知家族中性化后的残差
   多头腿、以及候选与已知家族相加之后的多头腿。
3. **候选与原式的 rank 相关低于约 0.8,就不是提纯,是换了一条因子**。可以推荐,但必须这么写。
4. **读完留出段之后改推荐、加「已确立」**。读完之后,推荐就是事前的第一推荐;留出段否定了它,就写「被否定」。
   读完留出段才冒出来的「规律」(尤其是只靠某一年)最多算「合理但未坐实」。
```

**10-04 23:41 · Bash** — List section headers of existing notes

```bash
cd /Users/wxy/Desktop/Partura && grep -n "^#" notes/F106_erm_mag_gap_1m/07_S_final.md notes/F106_erm_mag_gap_1m/07x_1_anatomy.md notes/F106_erm_mag_gap_1m/07x_2_longonly.md notes/F106_erm_mag_gap_1m/05_hypotheses.md notes/F106_erm_mag_gap_1m/06_baseline.md
```

```
notes/F106_erm_mag_gap_1m/07x_1_anatomy.md:1:### x1:这棵树在真实数据上读到的是什么(`studies/F106_erm_mag_gap_1m/x1_anatomy.py`,tag `x1`;只用 utrain)
notes/F106_erm_mag_gap_1m/07_S_final.md:1:# 07_S_final — S_final 阶段事实记录(留出段;工单 R2)
notes/F106_erm_mag_gap_1m/07_S_final.md:6:## 问题(配置里 S_final 阶段的 question)
notes/F106_erm_mag_gap_1m/07_S_final.md:12:## 0. 本轮做了什么(服务器运行次数)
notes/F106_erm_mag_gap_1m/07_S_final.md:18:## 1. 用的是主版,不是兜底版
notes/F106_erm_mag_gap_1m/07_S_final.md:23:## 2. 五条候选主表
notes/F106_erm_mag_gap_1m/07_S_final.md:25:### 2a. 决策口径(`books`;方向/半衰期在 **train** 上拟合;只报 train / valid)
notes/F106_erm_mag_gap_1m/07_S_final.md:35:### 2b. 用户口径(`books_user`;方向/半衰期在 **utrain**(=用户训练段)上拟合;报 utrain / **holdout**)
notes/F106_erm_mag_gap_1m/07_S_final.md:47:### 2c. sign / dist / cov
notes/F106_erm_mag_gap_1m/07_S_final.md:57:## 3. 固定半衰期扫描(`sweep`)—— 只在各自的拟合段上算,**没有 valid / holdout 的网格**
notes/F106_erm_mag_gap_1m/07_S_final.md:61:### 3a. `books.sweep`(train,hl → (Lnet%, Lshp))
notes/F106_erm_mag_gap_1m/07_S_final.md:71:### 3b. `books_user.sweep`(utrain,hl → (Lnet%, Lshp))
notes/F106_erm_mag_gap_1m/07_S_final.md:83:## 4. C3 / C4(排除性增量 ΔLnet)—— 因为 holdout 没有 hl 网格,降级后的读法
notes/F106_erm_mag_gap_1m/07_S_final.md:98:## 5. f_orig 与用户公布行对照
notes/F106_erm_mag_gap_1m/07_S_final.md:109:## 6. 分位剖面 Q1~Q10 —— **holdout 缺**,只有 train / valid
notes/F106_erm_mag_gap_1m/07_S_final.md:126:## 7. 逐年(`diagnostics.by_year`,2018→2025,多头口径 Lnet / LS)
notes/F106_erm_mag_gap_1m/07_S_final.md:141:## 8. rank 相关(`diagnostics.rank_corr_train`,**train 段**,`rank_corr_on` = "traded signals (sign x panel, smoothed at the fitted half-life); controls raw")
notes/F106_erm_mag_gap_1m/07_S_final.md:150:## 9. 异常与注意事项汇总
notes/F106_erm_mag_gap_1m/07_S_final.md:160:## 10. 原始输出在哪
notes/F106_erm_mag_gap_1m/07x_2_longonly.md:1:# 07x_2 — `x2_longonly.py` 的输出(事实记录,R1,执行写)
notes/F106_erm_mag_gap_1m/07x_2_longonly.md:7:## 0. 跑法与核对
notes/F106_erm_mag_gap_1m/07x_2_longonly.md:25:## 1. 已知家族多头十分位的构成(9 个 flag × 2 split × 2 family = 36 行)
notes/F106_erm_mag_gap_1m/07x_2_longonly.md:30:### known30 = `cross_mean(day_std(Amt), 30)`(`sign -1, hl_long 0`;train Lnet +12.6% Lshp +1.78;valid Lnet +22.3% Lshp +3.46)
notes/F106_erm_mag_gap_1m/07x_2_longonly.md:55:### known9 = `cross_max(day_std(Amt), 9)`(`sign -1, hl_long 5`;train Lnet +13.7% Lshp +1.99;valid Lnet +22.2% Lshp +3.59)
notes/F106_erm_mag_gap_1m/07x_2_longonly.md:84:## 2. 剔除被标记的票之后,多头腿的变化(同一 sign / 同一 half-life,**不重新拟合**)
notes/F106_erm_mag_gap_1m/07x_2_longonly.md:90:### known30(基准:train Lnet +12.6% Lshp +1.78 Lgross +15.2% LTO 3.4%;valid Lnet +22.3% Lshp +3.46 Lgross +24.4% LTO 2.8%)
notes/F106_erm_mag_gap_1m/07x_2_longonly.md:113:### known9(基准:train Lnet +13.7% Lshp +1.99 Lgross +17.1% LTO 4.5%;valid Lnet +22.2% Lshp +3.59 Lgross +25.1% LTO 3.9%)
notes/F106_erm_mag_gap_1m/07x_2_longonly.md:140:## 3. 和书 `rank(known) + w·rank(F106)`,以及双向中性化残差
notes/F106_erm_mag_gap_1m/07x_2_longonly.md:144:### known30
notes/F106_erm_mag_gap_1m/07x_2_longonly.md:158:### known9
notes/F106_erm_mag_gap_1m/07x_2_longonly.md:177:## 4. F106 信号对「近期涨停」类变量中性化后的残差(秩空间)
notes/F106_erm_mag_gap_1m/07x_2_longonly.md:199:## 5. 显式短记忆构造(9 行;方向在 train 上拟合)
notes/F106_erm_mag_gap_1m/07x_2_longonly.md:226:## 异常与注意(逐项对应"要带回来的数字"第 6 条)
notes/F106_erm_mag_gap_1m/07x_2_longonly.md:245:## 原始输出
notes/F106_erm_mag_gap_1m/07x_2_longonly.md:252:## 解读(主研第 2 轮,2026-10-04)
notes/F106_erm_mag_gap_1m/07x_2_longonly.md:256:### 这份输出回答的那个问题
notes/F106_erm_mag_gap_1m/07x_2_longonly.md:263:### 结论:**没有增量。而且这不是运气不好,是结构决定的。**
notes/F106_erm_mag_gap_1m/07x_2_longonly.md:280:### 两个「意外」,都是有意义的
notes/F106_erm_mag_gap_1m/07x_2_longonly.md:293:### 这份输出**不能**用来说的事
notes/F106_erm_mag_gap_1m/05_hypotheses.md:22:## 裁决(主研第 1 轮,2026-10-04)
notes/F106_erm_mag_gap_1m/05_hypotheses.md:48:## R1 的读法预登记(主研,2026-10-04,**在 x2 的数字回来之前写**)
notes/F106_erm_mag_gap_1m/05_hypotheses.md:54:### H10(排除性增量)—— 四条全部满足才算「被支持」
notes/F106_erm_mag_gap_1m/05_hypotheses.md:70:### H11(记忆长度错配)—— 只看 rank IC 和叠加,不看计数构造的多头腿
notes/F106_erm_mag_gap_1m/05_hypotheses.md:78:### H12(被朴素的「近期涨停」替代)—— 以**完整定义**的那一版为准
notes/F106_erm_mag_gap_1m/05_hypotheses.md:93:## 裁决(主研第 2 轮,2026-10-04)—— 照「R1 的读法预登记」逐条对
notes/F106_erm_mag_gap_1m/05_hypotheses.md:98:### H10(排除性增量)→ **被否定**(四条判据 (a)(b) 过、**(c)(d) 不过**)
notes/F106_erm_mag_gap_1m/05_hypotheses.md:135:### H11(记忆长度错配)→ **被支持**,但它**不产生候选**
notes/F106_erm_mag_gap_1m/05_hypotheses.md:152:### H12(被朴素的「近期涨停」替代)→ **已改写**(字面版被否定,操作版被支持)
notes/F106_erm_mag_gap_1m/05_hypotheses.md:174:### 顺带被 R1 坐实的两件事
```

10-04 23:41 · 读 `/Users/wxy/Desktop/Partura/notes/F106_erm_mag_gap_1m/07_S_final.md`

**10-04 23:43 · agent 的话**

全部材料到手。留出段已读、C1~C6 已裁决 → 本轮是 (c) 成文。我先写判断类 notes。

**10-04 23:44 · 写文件** `/Users/wxy/Desktop/Partura/notes/F106_erm_mag_gap_1m/09_diagnosis.md`(5505 字符)

**10-04 23:45 · 改文件** `/Users/wxy/Desktop/Partura/notes/F106_erm_mag_gap_1m/10_distilled.md`

```
- ## 读完留出段之后

_(留出段还没读。读完之后在这里逐条写 C1~C6 过了还是被否定、推荐是谁。)_
+ ## 读完留出段之后(主研写,2026-10-04;留出段读过**一次**:`S_final`,10-04 15:35,exit 0,`ledger.json` 里 `holdout {reads: 1, expressions: 5}`)

> 上面那一节是事前登记,**一个字没改**(14:59 写,早于 15:29 启动 `final`)。下面逐条对判据。
> 数字全部来自 `runs/F106_erm_mag_gap_1m/S_final.json`,完整表在 `07_S_final.md`,执行的核对记录在 `results/R2.md`。
> **holdout 一律读 `books_user`**(方向/半衰期在 utrain = 用户训练段上拟合);`books` 字典没有 holdout 字段。

### 留出段主表(20230808–20251231,581 个交易日;用户口径)

| id | sign | hlL | **Lnet** | Lgross | **Lshp** | LTO | LS | dist | cov |
|---|---|---|---|---|---|---|---|---|---|
| `f_known30`(第一推荐,已知家族) | −1 | 0 | **+14.10%** | +16.24% | **+1.51** | 2.83% | +1.94 | 1.000 | 0.967 |
| `f_known30r`(cs_rank 版,同构基准) | −1 | 0 | +14.10%(**与上行逐项相同**) | +16.24% | +1.51 | 2.83% | +1.94 | 1.000 | 0.967 |
| `f_excl_blown15`(F106 标记叠加) | −1 | 1 | +14.64% | +16.57% | +1.57 | 2.55% | +3.29 | 1.000 | 0.967 |
| `f_excl_lu15`(朴素涨停叠加) | −1 | 1 | +14.85% | +16.74% | +1.60 | 2.49% | +3.52 | 1.000 | 0.967 |
… (36 行略) …

- 没有新增「已确立」条目;`09_diagnosis.md` 里所有 A 档的核心证据都来自 train/valid,留出段只用于按事前判据确认。
- 没有换候选、没有换排序、没有改判据、没有重跑任何阶段(本轮及上一轮**服务器运行 0 次**)。
- 留出段上**拿不到**的东西照实写缺,不重跑补:分位剖面(`profile` 无 holdout 键)、固定半衰期表(`sweep` 只在拟合段)。
```

**10-04 23:45 · Bash** — Locate placeholder section line number

```bash
cd /Users/wxy/Desktop/Partura && grep -n "^## 读完留出段之后" notes/F106_erm_mag_gap_1m/10_distilled.md && wc -l notes/F106_erm_mag_gap_1m/10_distilled.md
```

```
68:## 读完留出段之后
      70 notes/F106_erm_mag_gap_1m/10_distilled.md
```

**10-04 23:46 · 写文件** `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/post_holdout.md`(3726 字符)

**10-04 23:46 · Bash** — Replace placeholder section with post-holdout section

```bash
cd /Users/wxy/Desktop/Partura && head -n 67 notes/F106_erm_mag_gap_1m/10_distilled.md > /private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/dist_head.md && cat /private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/dist_head.md /private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/post_holdout.md > notes/F106_erm_mag_gap_1m/10_distilled.md && tail -5 notes/F106_erm_mag_gap_1m/10_distilled.md && grep -c "" notes/F106_erm_mag_gap_1m/10_distilled.md && grep -n "^## \|^---" notes/F106_erm_mag_gap_1m/10_distilled.md
```

```
### 留出段读完之后**没有**新增的东西(照规矩写明)

- 没有新增「已确立」条目;`09_diagnosis.md` 里所有 A 档的核心证据都来自 train/valid,留出段只用于按事前判据确认。
- 没有换候选、没有换排序、没有改判据、没有重跑任何阶段(本轮及上一轮**服务器运行 0 次**)。
- 留出段上**拿不到**的东西照实写缺,不重跑补:分位剖面(`profile` 无 holdout 键)、固定半衰期表(`sweep` 只在拟合段)。
121
3:---
5:## 读留出段之前(主研第 2 轮写,2026-10-04;写在 `study.sh final` 之前,之后一个字不改)
66:---
68:## 读完留出段之后(主研写,2026-10-04;留出段读过**一次**:`S_final`,10-04 15:35,exit 0,`ledger.json` 里 `holdout {reads: 1, expressions: 5}`)
```

**10-04 23:46 · agent 的话**

10_distilled.md 已补上「读完留出段之后」,事前登记那一节原封不动。现在写 11_risks / 12_next / 08_variants。

**10-04 23:47 · 写文件** `/Users/wxy/Desktop/Partura/notes/F106_erm_mag_gap_1m/11_risks.md`(3016 字符)

**10-04 23:48 · 写文件** `/Users/wxy/Desktop/Partura/notes/F106_erm_mag_gap_1m/12_next.md`(2415 字符)

**10-04 23:49 · 写文件** `/Users/wxy/Desktop/Partura/notes/F106_erm_mag_gap_1m/08_variants.md`(2977 字符)

**10-04 23:49 · Bash** — Append holdout confirmation table to hypotheses file

```bash
cd /Users/wxy/Desktop/Partura && cat >> notes/F106_erm_mag_gap_1m/05_hypotheses.md <<'EOF'

---

## 留出段之后的确认(主研,2026-10-04;**不升级任何假设的状态**)

规矩:读完留出段不新增「已确立」、不改推荐(playbook §6.4)。下面只记录「事前登记的判据在留出段上没有推翻哪条假设」,状态一律照上面第 2 轮的裁决不变。

| 假设 | 第 2 轮裁决(不变) | 留出段上对应的判据 | 结果 |
|---|---|---|---|
| H1 / H3 / H6 / H8(塌缩日=封板日决定一切、两端都是打板股、倒 U、两侧不对等) | 被支持 | 留出段**没有分位剖面**(`profile` 无 holdout 键)→ 倒 U 在留出段**无数据可看** | 没有被检验,也没有被推翻;照实写缺 |
| H2 / H4 / H5(常规区间尾部不对称是信号 / 塌缩日=低价股 / 读隔夜跳空) | 被否定 | 无直接判据(留出段只跑了 5 条候选) | 维持被否定 |
| 「原样对纯多头不可用」(H1 的操作后果) | — | **C1**:`f_orig` holdout Lnet −3.19% / Lshp −0.69 / Lgross −1.38%,逐年八年全负 | **没被推翻** |
| 「公布的多空夏普是真的但与多头腿无关」 | — | **C2**:holdout LS +3.108,与用户表 3.11 精确复现 | **没被推翻** |
| **H10**(排除性增量) | **被否定** | **C3**:holdout ΔLnet **+0.54 pp** < +1.5 pp 门槛(valid +0.57 pp);错配污染 ≲0.4 pp、符号不定(`09_diagnosis.md` B1) | 维持被否定 |
| **H11**(记忆长度错配) | **被支持,但不产生候选** | 无判据(计数构造过不了 dist,没有进 S_final) | 维持「被支持但不产生候选」 |
| **H12**(被朴素「近期涨停」替代) | **已改写**(字面版否定、操作版支持) | **C4**:朴素涨停叠加 **+0.75 pp** > F106 自己的 **+0.54 pp**(朴素反而高 0.21 pp) | 操作版维持被支持 |
| **H13**(真正值钱的是新股过滤器) | **合理但未坐实** | 无判据(没有进 S_final 候选) | 维持未坐实 → `12_next.md` 第 1 条 |

顺带:**C5**(已知家族 holdout +14.10% / 夏普 +1.51,落在用户区间内)和 **C6**(五条 cov 0.9675、dist ≥0.9933)都成立 —— 这两条不对应任何假设,是「参照系还在、门槛不是瓶颈」的前提条件。
EOF
echo done && wc -c notes/F106_erm_mag_gap_1m/05_hypotheses.md
```

```
done
   21695 notes/F106_erm_mag_gap_1m/05_hypotheses.md
```

**10-04 23:49 · agent 的话**

Now the writeup 工单 R3。

**10-04 23:50 · 写文件** `/Users/wxy/Desktop/Partura/notes/F106_erm_mag_gap_1m/orders/R3.md`(5957 字符)

**10-04 23:50 · Bash** — List orders and results cards

```bash
cd /Users/wxy/Desktop/Partura && ls notes/F106_erm_mag_gap_1m/results/ notes/F106_erm_mag_gap_1m/orders/
```

```
notes/F106_erm_mag_gap_1m/orders/:
R1.md
R2.md
R3.md

notes/F106_erm_mag_gap_1m/results/:
R1.md
R2.md
```

**10-04 23:50 · 改文件** `/Users/wxy/Desktop/Partura/notes/F106_erm_mag_gap_1m/orders/R3.md`

```
- - 不改已有的结果卡(`results/R0.md`、`R1.md`、`R2.md`)—— 结果卡只追加新的。
+ - 不改已有的结果卡(`results/R1.md`、`R2.md`;没有 R0)—— 结果卡只追加新的。
```

**10-04 23:50 · agent 的话**

Now 覆盖重写 state.md(控制在 150 行 / 10 KB 内)。

**10-04 23:52 · 写文件** `/Users/wxy/Desktop/Partura/notes/F106_erm_mag_gap_1m/state.md`(7263 字符)

**10-04 23:53 · 写文件** `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md`(7263 字符)

**10-04 23:53 · Bash** — Install new state.md and check size

```bash
cd /Users/wxy/Desktop/Partura && cp /private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md notes/F106_erm_mag_gap_1m/state.md && grep -c "" notes/F106_erm_mag_gap_1m/state.md && wc -c notes/F106_erm_mag_gap_1m/state.md && ls -la notes/F106_erm_mag_gap_1m/
```

```
89
   12365 notes/F106_erm_mag_gap_1m/state.md
total 376
drwxr-xr-x@ 20 wxy  staff    640 Oct  4 23:49 .
drwxr-xr-x@ 19 wxy  staff    608 Oct  4 13:07 ..
-rw-r--r--@  1 wxy  staff   1323 Oct  4 12:15 01_expression.md
-rw-r--r--@  1 wxy  staff   2769 Oct  4 12:15 02_operators.md
-rw-r--r--@  1 wxy  staff   3249 Oct  4 12:15 03_decomposition.md
-rw-r--r--@  1 wxy  staff   1562 Oct  4 12:15 04_grammar.md
-rw-r--r--@  1 wxy  staff  21695 Oct  4 23:49 05_hypotheses.md
-rw-r--r--@  1 wxy  staff   3247 Oct  4 12:20 06_baseline.md
-rw-r--r--@  1 wxy  staff  14084 Oct  4 23:33 07_S_final.md
-rw-r--r--@  1 wxy  staff  10386 Oct  4 12:41 07x_1_anatomy.md
-rw-r--r--@  1 wxy  staff  24250 Oct  4 14:53 07x_2_longonly.md
-rw-r--r--@  1 wxy  staff   5146 Oct  4 23:49 08_variants.md
-rw-r--r--@  1 wxy  staff  10516 Oct  4 23:44 09_diagnosis.md
-rw-r--r--@  1 wxy  staff  14203 Oct  4 23:46 10_distilled.md
-rw-r--r--@  1 wxy  staff   6499 Oct  4 23:47 11_risks.md
-rw-r--r--@  1 wxy  staff   5040 Oct  4 23:48 12_next.md
-rw-r--r--@  1 wxy  staff  23201 Oct  4 23:34 journal.md
drwxr-xr-x@  5 wxy  staff    160 Oct  4 23:50 orders
drwxr-xr-x@  4 wxy  staff    128 Oct  4 23:33 results
-rw-r--r--@  1 wxy  staff  12365 Oct  4 23:53 state.md
```

**10-04 23:53 · agent 的话**

state.md 是 12.4 KB,超了 10 KB 上限,我压一遍。

**10-04 23:54 · 改文件** `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md`

```
- 源码里和名字不一样的地方:`day_quantile` 线性插值,但 241 分钟时 q=0.95 恰落第 13 大、不插值;`is_gt`/`is_lt` 严格不等号 + NaN 为假 + 输出 int(尾部可空集、全树无 NaN 传播);**计数分母的 1e-6 是除零保护,分位数分母的 1e-6 才是要害**(带量纲,比一个 tick 小三个数量级);树里**没有日轴算子**(真实回看 1 天,时间结构全来自口径里的因果 EMA);`cross_*` 窗口网格 3/5/10/15/30/60/241(**没有 20**);**本机 torch 与服务器内核的分位数位置不一致 → 以服务器为准**。
+ 源码里和名字不一样的地方(全文在 `02_operators.md`):**计数分母的 1e-6 是除零保护,分位数分母的 1e-6 才是要害**(带量纲,比一个 tick 小三个数量级);树里**没有日轴算子**(真实回看 1 天,时间结构全来自口径里的因果 EMA);`day_quantile` 线性插值,但 241 分钟时 q=0.95 恰落第 13 大、不插值;`is_gt`/`is_lt` 严格不等号 + NaN 为假 + 输出 int;`cross_*` 窗口网格 3/5/10/15/30/60/241(**没有 20**);**本机 torch 与服务器内核的分位数位置不一致 → 以服务器为准**。
```

**10-04 23:54 · 改文件** `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md`

```
- ## 4. 假设表(H1~H13 全部已定,**不要再查**;证据与留出段确认表在 `05_hypotheses.md`)

- **被支持**:H1 塌缩日决定一切、H3 塌缩日=封板日、H6 两端都是打板股/剖面倒 U、H8 两侧不对等非镜像、H9 多余节点不改排序。
- **被否定**:H2 常规区间尾部不对称才是信号、H4 塌缩日=低价不活跃股、H5 常规区间读隔夜跳空;**H10 排除性增量**(事前四判据 (a)(b) 过、(c)(d) 不过;valid +0.57 pp、holdout +0.54 pp;天花板见 §2.3)。
- **方向反了 → 改写**:H7 → **H11 记忆长度错配**:**被支持但不产生候选**(计数构造 rank
… (333 字符略) …
`):只留常规日、先排序再 EMA、clip(±3)、只留 R、只留 L、折叠(train +2.4% 但 valid −6.0%)、log(1+|X|)/R+L/log(1+R+L)、短记忆计数(过不了 dist)、`rank(known)+w·rank(F106)`、延长半衰期(hl20 已是端点)、加大 ε(= 去掉塌缩日)。
+ ## 4. 假设表(H1~H13 全部已定,**不要再查**;证据与留出段确认表在 `05_hypotheses.md`)

- **被支持**:H1 塌缩日决定一切、H3 塌缩日=封板日、H6 两端都是打板股/剖面倒 U、H8 两侧不对等非镜像、H9 多余节点不改排序。
- **被否定**:H2(常规区间尾部不对称才是信号)、H4(塌缩日=低价不活跃股)、H5(读隔夜跳空);**H10 排除性增量**(事前四判据 (a)(b) 过、(c)(d) 不过;valid +0.57 pp、holdout +0.54 pp;天花板见 §2.3)。
- **H7 方向反了 → 改写为 H11 记忆长度错配**:**被支持但不产生候选**(计数构造 rank IC 是 EMA20(X) 的 1.7~4.8 倍、两段全优,但取值几乎全 0 → 过不了 `dist ≥ 0.5`)。
- **H12 已改写**:字面版(完全被朴素涨停替代)否定(残差 rank IC 保住 0.26×~0.79×、折叠量 R² 0.444 ≠ 1.0),**操作版被支持**(排除用途上朴素标记反而更好,C4)。
- **H13 合理但未坐实**:`listed<250d` 是 36 格里唯一四格全 ≥1 点(+1.60/+1.09/+1.90/+1.95)→ 新股过滤器,**不是这条因子的功劳**,且来自宽搜索 → `12_next.md` 第 1 条。

## 5. 候选

**没有任何 F106 变体可以推荐。结论类型 = 分辨**(不是提纯、不是升华)。不是「没找到」:六条理由在 `10_distilled.md`「为什么没有更好的」。
事前第一推荐 = **`f_known30` = `cross_mean(day_std(Amt), 30)`**(已知家族,规则要求必含;holdout +14.10%/+1.51,C5 成立)—— **它不是这条因子的产物**。
对纯多头用户唯一可操作的输出:**F106 不进书,继续用已知成交额家族;要「别买刚封过板的票」这个排除效果,一个朴素日线涨停标记就够**(而且两者在留出段都在噪声里,连叠加本身也不推荐)。
已排除的候选与原因(数字见 `07x_1_anatomy.md` E 表 / `07x_2_longonly.md`):只留常规日、先排序再 EMA、clip(±3)、只留 R / 只留 L、折叠(train +2.4% 但 valid −6.0%)、log(1+|X|) / R+L / log(1+R+L)、短记忆计数(过不了 dist)、`rank(known)+w·rank(F106)`、延长半衰期(hl20 已是端点)、加大 ε(= 去掉塌缩日)。
```

**10-04 23:55 · 改文件** `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md`

```
- - **还没看结果的任务:无。** 唯一在飞的是工单 R3(本轮刚下,还没有结果卡)。
- **成文的判断部分已经写完,不要重写**:`08_variants.md`(怎么读总表)、`09_diagnosis.md`(A 已确立 / B 合理但未坐实 / C 未决)、`10_distilled.md` 后半节(C1~C6 裁决 + 推荐)、`11_risks.md`、`12_next.md`、`05_hypotheses.md` 末尾的留出段确认表。
- **两套书别混**:`books` 在 train 拟合、只报 train/valid;`books_user` 在 utrain 拟合、报 utrain/**holdout** → holdout 一律读
… (832 字符略) …
s_rank` 吃得下 DT 面日频量。
- **一句话**:三件事都已确立并在用户测试段上按事前判据验过 —— 「它是什么」(封板记忆)、「原样不可用」(holdout 多头腿 −3.19%、八年全负)、「相对已知家族没有增量」(holdout Δ +0.54 pp,天花板可算)。**不要抢救、不要换推荐**,剩下的全是核对数字。
+ - **还没看结果的任务:无。** 唯一在飞的是工单 R3(本轮刚下,还没有结果卡)。
- **成文的判断部分已经写完,不要重写**:`08_variants.md`、`09_diagnosis.md`(A 已确立 / B 合理但未坐实 / C 未决)、`10_distilled.md` 后半节、`11_risks.md`、`12_next.md`、`05_hypotheses.md` 末尾的留出段确认表。
- **两套书别混**:`books` 在 train 拟合、只报 train/valid;`books_user` 在 utrain 拟合、报 utrain/**holdout** → holdout 一律读后者(`books` 没有 holdout 字段)。
- **JSON 里没有的东西**(别找、别重跑):留出段的分位剖面(`profile` 只有 train/valid,`f_known30r`/`f_excl_lu15` 连这个字段都没有)、留出段的固定半衰期表(`sweep` 只在拟合段);`by_year` 没标注用哪套 hl(不影响 `f_orig`/`f_known30`,两套 hl 相同)。
- **最容易张冠李戴的一处**:x2 的叠加行是**20 日窗口、hl 不重拟合**(ΔLnet +1.59/+0.52),S_final 的 `f_excl_blown15` 是**15 日窗口、引擎重拟合**(+1.63/+0.57)。接近是互相印证,**不是同一行**(`08_variants.md` §5)。
- `cov` 随 split 变(train 0.691 / valid 0.895 / utrain 0.749 / holdout 0.967)但五个变体完全相同 → 面板覆盖率,不是求值失败;门槛用 holdout 这一档。
- 0/1 与小整数计数构造的「多头腿」是假的(并列按股票代码取 10%);x2 叠加行的 `LS`/`short` 不可读,只读 `Lnet/Lshp/Lgross/LTO`。
- 服务器很挤:x2 排了 1480 秒;`S1_regime` 被内存守卫顶掉(**exit 97 = 根本没跑**);`[guard] waiting` 正常,别起第二个 job;`wait` 只打最后 200 行 → 读 `logs/<fid>_<tag>.log` 全文。假警报(已排除):`g_max30`/`g_limitup30` 两个 control 都存在;`cs_rank` 吃得下 DT 面日频量。
- **一句话**:三件事都已确立并在用户测试段上按事前判据验过 —— 「它是什么」(封板记忆)、「原样不可用」(holdout 多头腿 −3.19%、八年全负)、「相对已知家族没有增量」(holdout Δ +0.54 pp,天花板可算)。**不要抢救、不要换推荐**,剩下的全是核对数字。
```

**10-04 23:55 · 改文件** `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md`

```
- - **它读的不是日内尾部形状,而是「最近有没有封过涨停板、那几分钟跳多大」的一年期记忆**:上涨分钟 ≤12 时分母塌成 1e-6 → 读数 ×10⁶;塌缩日 86.3%/77.8% 是涨停收盘(基准 1.59%,富集约 50 倍),不是低价股(<3 元占 0.2%)。
- 多头腿在半衰期网格 {0,1,2,3,5,10,20} **每一点、毛和净全负**(train hl0 −67.22% → hl20 −6.91%;utrain −66.50% → −5.82%)→ **不是成本问题**。**hlL = hlS = 20 = 用户公布那一行 → 「原式 + 多头最优半衰期」就是原式本身**(网格是全局约定,不扩)。
- 剖面**倒 U**(train 
… (341 字符略) …
57,对实测 +1.59/+0.52/+1.60/+0.40,**四格吻合到 25% 内**;share 低是因为**已知家族本来就在躲这些票**(相对持有频率只有全市场的 24%~64%)→ **不是清单不准,是这张「不要买」清单多余。**
- 相加(24 行无一胜已知家族、随 w 单调下降)与中性化残差(多头腿五行全负)都否定。
+ - **它读的不是日内尾部形状,而是「最近有没有封过涨停板、那几分钟跳多大」的一年期记忆**:上涨分钟 ≤12 时分母塌成 1e-6 → 读数 ×10⁶;塌缩日 86.3%/77.8% 是涨停收盘(基准 1.59%,富集约 50 倍),不是低价股(<3 元占 0.2%)。
- 多头腿在半衰期网格 {0,1,2,3,5,10,20} **每一点、毛和净全负**(train hl0 −67.22% → hl20 −6.91%;utrain −66.50% → −5.82%)→ **不是成本问题**。**hlL = hlS = 20 = 用户公布那一行 → 「原式 + 多头最优半衰期」就是原式本身**(网格是全局约定,不扩)。
- 剖面**倒 U**(train Q1 −28.4%、Q10 −5.3%;valid −22.7%/−1.8%),两端都是近期封板股 → 线性中性化看不见东西;折叠型要用**同样折叠过的**控制量。
- 不是成交额/规模/换手/波动/动量/反转的改写:corr(signal, mom20) −0.013;十档动量秩 0.47~0.54;折叠量对五个水平变量 R² **0.068**,对四个「近期涨停」变量 R² **0.444**。
- 公布的多空夏普一半以上靠**次日买不进的票**(train 2.82 → 0.42);去塌缩日或 clip(±3) → 转负。多头腿不受此影响。
- **增量的天花板可以算出来**(解释力最强):ΔLnet ≈ share × 超额之差 = 2.0/0.70/1.93/0.57,对实测 +1.59/+0.52/+1.60/+0.40,**四格吻合到 25% 内**;share 低是因为**已知家族本来就在躲这些票**(相对持有频率只有全市场的 24%~64%)→ **不是清单不准,是这张「不要买」清单多余。** 相加(24 行无一胜已知家族、随 w 单调下降)与中性化残差(多头腿五行全负)也都否定。
```

**10-04 23:55 · Bash** — Reinstall trimmed state.md and check size

```bash
cd /Users/wxy/Desktop/Partura && cp /private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md notes/F106_erm_mag_gap_1m/state.md && grep -c "" notes/F106_erm_mag_gap_1m/state.md && wc -c notes/F106_erm_mag_gap_1m/state.md
```

```
87
   12185 notes/F106_erm_mag_gap_1m/state.md
```

**10-04 23:55 · 改文件** `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md`

```
- | id | sign | hlL | **Lnet** | Lgross | **Lshp** | LTO | LS | dist | cov |
|---|---|---|---|---|---|---|---|---|---|
| `f_orig` 原式 | −1 | 20 | **−3.19%** | −1.38% | **−0.69** | 2.40% | +3.11 | 0.993 | 0.967 |
| `f_known30` 已知家族 | −1 | 0 | **+14.10%** | +16.24% | **+1.51** | 2.83% | +1.94 | 1.000 | 0.967 |
| `f_known30r` cs_rank 版 |
… (102 字符略) …
叠加 | −1 | 1 | +14.64% | +16.57% | +1.57 | 2.55% | +3.29 | 1.000 | 0.967 |
| `f_excl_lu15` 朴素涨停叠加 | −1 | 1 | +14.85% | +16.74% | +1.60 | 2.49% | +3.52 | 1.000 | 0.967 |
+ (全表含 Lgross/LTO/dist 在 `10_distilled.md` 后半节与 `07_S_final.md` §2b;五条 sign 全 −1、cov 全 0.967、dist ≥0.993)

| id | hlL | **Lnet** | **Lshp** | LS |
|---|---|---|---|---|
| `f_orig` 原式 | 20 | **−3.19%** | **−0.69** | +3.11 |
| `f_known30` 已知家族 | 0 | **+14.10%** | **+1.51** | +1.94 |
| `f_known30r` cs_rank 版 | 0 | +14.10%(与上行**逐项相同**,rank 相关 1.000) | +1.51 | +1.94 |
| `f_excl_blown15` 叠加 | 1 | +14.64% | +1.57 | +3.29 |
| `f_excl_lu15` 朴素涨停叠加 | 1 | +14.85% | +1.60 | +3.52 |
```

**10-04 23:56 · 改文件** `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md`

```
- ⚠ **C3/C4 的读法降级了,报告必须写明**:引擎只在拟合段算 hl 网格,**留出段没有固定半衰期表**,+0.54/+0.75 是「各自拟合 hl」下的(叠加 hl1 对基准 hl0)。
**本轮订正了上一轮的措辞**:它**不是**单方向的「上界」。用 utrain 的 hl 敏感性量错配(只借敏感性,不是把 utrain 的数当 holdout 的数):own-hl Δ +1.31 pp、同 hl0 Δ +1.33 pp、同 hl1 Δ +1.71 pp → **污染 ≲0.4 pp、符号不定**(own-hl 甚至比干净的 hl0 低 0.02 pp)。两个方向都远低于 +1.5 pp 门槛与 ±3 pp 噪声 → 裁决不变。见 `09_diagnosis.md` B1。
`07_S_final.md` §4 和 `results/R2.md` 写的是「上界」,**报告以 B1 为准**(R3 工单已交代)。
+ ⚠ **C3/C4 的读法降级了,报告必须写明**:引擎只在拟合段算 hl 网格,**留出段没有固定半衰期表**,+0.54/+0.75 是「各自拟合 hl」下的(叠加 hl1 对基准 hl0)。
**本轮订正了上一轮的措辞**:它**不是**单方向的「上界」—— 用 utrain 的 hl 敏感性量错配(own-hl Δ +1.31 / 同 hl0 +1.33 / 同 hl1 +1.71 pp)得到**污染 ≲0.4 pp、符号不定**(own-hl 甚至比干净的 hl0 低 0.02 pp),两个方向都远低于门槛与噪声 → 裁决不变。推导见 `09_diagnosis.md` B1;`07_S_final.md` §4 与 `results/R2.md` 写的是「上界」,**报告以 B1 为准**(R3 工单已交代)。
```

**10-04 23:56 · 改文件** `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md`

```
- 已排除的候选与原因(数字见 `07x_1_anatomy.md` E 表 / `07x_2_longonly.md`):只留常规日、先排序再 EMA、clip(±3)、只留 R / 只留 L、折叠(train +2.4% 但 valid −6.0%)、log(1+|X|) / R+L / log(1+R+L)、短记忆计数(过不了 dist)、`rank(known)+w·rank(F106)`、延长半衰期(hl20 已是端点)、加大 ε(= 去掉塌缩日)。
+ 已排除的候选 11 条及原因:见 `10_distilled.md`「为什么没有更好的」第 2/3/5 点与 `07x_1_anatomy.md` E 表(只留常规日、先排序再 EMA、clip(±3)、单侧、折叠、三种压缩变换、短记忆计数、和书、延长半衰期、加大 ε)。
```

**10-04 23:56 · 改文件** `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md`

```
- - `cov` 随 split 变(train 0.691 / valid 0.895 / utrain 0.749 / holdout 0.967)但五个变体完全相同 → 面板覆盖率,不是求值失败;门槛用 holdout 这一档。
- 0/1 与小整数计数构造的「多头腿」是假的(并列按股票代码取 10%);x2 叠加行的 `LS`/`short` 不可读,只读 `Lnet/Lshp/Lgross/LTO`。
- 服务器很挤:x2 排了 1480 秒;`S1_regime` 被内存守卫顶掉(**exit 97 = 根本没跑**);`[guard] waiting` 正常,别起第二个 job;`wait` 只打最后 200 行 → 读 `logs/<fid>_<tag>.log` 全文。假警报(已排除):`g_max30`/`g_limitup30` 两个 control 都存在;`cs_rank` 吃得下 DT 面日频量。
+ - 另外三个读表的坑都写在 `08_variants.md`:`cov` 随 split 变但五个变体相同(= 面板覆盖率,不是求值失败,§2)、0/1 计数构造的「多头腿」是假的(§7)、x2 叠加行的 `LS`/`short` 不可读(§8)。
- 服务器很挤:x2 排了 1480 秒;`S1_regime` 被内存守卫顶掉(**exit 97 = 根本没跑**);`[guard] waiting` 正常,别起第二个 job;`wait` 只打最后 200 行 → 读 `logs/<fid>_<tag>.log` 全文。假警报(已排除):`g_max30`/`g_limitup30` 两个 control 都存在;`cs_rank` 吃得下 DT 面日频量。
```

**10-04 23:56 · Bash** — Reinstall trimmed state.md and recheck size

```bash
cd /Users/wxy/Desktop/Partura && cp /private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md notes/F106_erm_mag_gap_1m/state.md && grep -c "" notes/F106_erm_mag_gap_1m/state.md && wc -c notes/F106_erm_mag_gap_1m/state.md
```

```
87
   11807 notes/F106_erm_mag_gap_1m/state.md
```

**10-04 23:56 · 改文件** `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md`

```
- ### 2.3 train/valid 的事实(第 1~2 轮确立,**不要重查**)

- **它读的不是日内尾部形状,而是「最近有没有封过涨停板、那几分钟跳多大」的一年期记忆**:上涨分钟 ≤12 时分母塌成 1e-6 → 读数 ×10⁶;塌缩日 86.3%/77.8% 是涨停收盘(基准 1.59%,富集约 50 倍),不是低价股(<3 元占 0.2%)。
- 多头腿在半衰期网格 {0,1,2,3,5,10,20} **每一点、毛和净全负**(train hl0 −67.22% → hl20 −6.91%;utrain −66.50% → −5.82%)→ **不是成本问题**。**hlL = hlS = 20 = 用户公布那一行 → 「原式 + 多头最
… (385 字符略) …
.57,对实测 +1.59/+0.52/+1.60/+0.40,**四格吻合到 25% 内**;share 低是因为**已知家族本来就在躲这些票**(相对持有频率只有全市场的 24%~64%)→ **不是清单不准,是这张「不要买」清单多余。** 相加(24 行无一胜已知家族、随 w 单调下降)与中性化残差(多头腿五行全负)也都否定。
+ ### 2.3 train/valid 的事实(第 1~2 轮确立,**不要重查**;每条的完整数字与出处在 `09_diagnosis.md` A1~A7)

- **它读的不是日内尾部形状,而是「最近有没有封过涨停板、那几分钟跳多大」的一年期记忆**:上涨分钟 ≤12 时分母塌成 1e-6 → 读数 ×10⁶;塌缩日 86.3%/77.8% 是涨停收盘(基准 1.59%,富集约 50 倍),不是低价股。(A1)
- 多头腿在半衰期网格 {0,1,2,3,5,10,20} **每一点、毛和净全负**(train −67.22% → −6.91%)→ **不是成本问题**;**hlL = hlS = 20 = 用户公布那一行 → 「原式 + 多头最优半衰期」就是原式本身**(网格是全局约定,不扩)。(A2)
- 剖面**倒 U**(train Q1 −28.4% / Q10 −5.3%),两端都是近期封板股 → 线性中性化看不见东西,折叠型要用**同样折叠过的**控制量。(A4)
- 不是成交额/规模/换手/波动/动量/反转的改写(折叠量对五个水平变量 R² **0.068**,对四个「近期涨停」变量 R² **0.444**)。(A5)
- 公布的多空夏普一半以上靠**次日买不进的票**(train 2.82 → 0.42);去塌缩日或 clip(±3) → 转负。多头腿不受此影响。(A3)
- **增量的天花板可以算出来**(解释力最强):ΔLnet ≈ share × 超额之差 = 2.0/0.70/1.93/0.57 对实测 +1.59/+0.52/+1.60/+0.40,**四格吻合到 25% 内**;share 低是因为**已知家族本来就在躲这些票**(相对持有频率只有全市场的 24%~64%)→ **不是清单不准,是这张「不要买」清单多余。** 相加(24 行无一取胜)与中性化残差(五行全负)也都否定。(A6/A7)
```

**10-04 23:57 · 改文件** `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md`

```
- 读源码(不信字面)→ 要害是「分位数作分母 +1e-6」→ 探针量出三个取值区间 → 推出「截面两端一定是塌缩日」→ x1 真实数据解剖 → 裁决 H1~H9 → 只剩「对纯多头相对已知家族有没有增量」→ H10~H12 + 工单 R1(x2)→ 第 2 轮裁决并算出天花板,**不再做实验** → 事前登记 + final 工单 R2 → 执行跑完 `final` 被打断两次 → 第 3 轮把 R2 原样交回并自己裁决 C1~C6 → **本轮(第 4 轮)写完判断类 notes,下工单 R3 成文**。
+ 读源码(不信字面)→ 要害是「分位数作分母 +1e-6」→ 探针量出三个取值区间 → 推出「截面两端一定是塌缩日」→ x1 解剖真实数据 → 裁决 H1~H9 → 只剩「对纯多头相对已知家族有没有增量」→ H10~H12 + 工单 R1(x2)→ 第 2 轮裁决并算出天花板,**不再做实验** → 事前登记 + final 工单 R2 → 执行跑完 `final` 被打断两次 → 第 3 轮把 R2 原样交回、自己裁决 C1~C6 → **第 4 轮(本轮)写完判断类 notes,下工单 R3 成文**。
```

**10-04 23:57 · 改文件** `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md`

```
- 1. **下一轮:执行做工单 R3(kind: writeup)** —— 补事实类段落(`01` 补公布行与复现度、`06` 查缺补齐、**新建 `07_S0_baseline.md`**(磁盘上没有,S0 跑过))、`study.sh report`、**逐项核对 14 项数字**(表在 R3 工单里)、单位(ΔLnet 必须写 pp)与口径(holdout 只能来自 `books_user`)两项检查。**服务器运行 0 次。**
2. **再下一轮**:14 项全对 → `status: done`;有对不上的 → R4(kind: fix),**只改数字/措辞,不改结论、不改推荐**。
3. **明确不做**:不再下实验工单;不重跑 `S1_reg
… (9 字符略) …
 97 = 根本没跑,x1 已答);不找 X 的单调变换;不抢救空头腿/多空夏普;不扩半衰期网格;**不补留出段的剖面与固定半衰期表(重跑 = 第二次读留出段)**;H13 不在本研究里验;不动 `scripts/`、`partura/`、`workflows/`、`handoff/`、`lab/`、`docs/`、别的因子的文件。
+ 1. **下一轮:执行做工单 R3(kind: writeup)** —— 补事实类段落(`01` 补公布行与复现度、`06` 查缺补齐、**新建 `07_S0_baseline.md`**:磁盘上没有而 S0 跑过)、`study.sh report`、**逐项核对 14 项数字**(表在工单里)、单位(ΔLnet 写 pp)与口径(holdout 只来自 `books_user`)两项检查。**服务器运行 0 次。**
2. **再下一轮**:14 项全对 → `status: done`;有对不上的 → R4(kind: fix),**只改数字/措辞,不改结论、不改推荐**。
3. **明确不做**:不再下实验工单;不重跑 `S1_regime`(exit 97,x1 已答);不找 X 的单调变换;不抢救空头腿/多空夏普;不扩半衰期网格;**不补留出段的剖面与固定半衰期表(重跑 = 第二次读留出段)**;H13 不在本研究里验;不动 `scripts/`、`partura/`、`workflows/`、`handoff/`、`lab/`、`docs/`、别的因子的文件。
```

**10-04 23:57 · Bash** — Reinstall and recheck state.md size

```bash
cd /Users/wxy/Desktop/Partura && cp /private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md notes/F106_erm_mag_gap_1m/state.md && grep -c "" notes/F106_erm_mag_gap_1m/state.md && wc -c notes/F106_erm_mag_gap_1m/state.md
```

```
87
   11693 notes/F106_erm_mag_gap_1m/state.md
```

**10-04 23:57 · 改文件** `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md`

```
- ## 4. 假设表(H1~H13 全部已定,**不要再查**;证据与留出段确认表在 `05_hypotheses.md`)

- **被支持**:H1 塌缩日决定一切、H3 塌缩日=封板日、H6 两端都是打板股/剖面倒 U、H8 两侧不对等非镜像、H9 多余节点不改排序。
- **被否定**:H2(常规区间尾部不对称才是信号)、H4(塌缩日=低价不活跃股)、H5(读隔夜跳空);**H10 排除性增量**(事前四判据 (a)(b) 过、(c)(d) 不过;valid +0.57 pp、holdout +0.54 pp;天花板见 §2.3)。
- **H7 方向反了 → 改写为 H11 记忆长度错配**:**被支持但不产生候选**(计数构造 rank IC 是 
… (119 字符略) …
 0.444 ≠ 1.0),**操作版被支持**(排除用途上朴素标记反而更好,C4)。
- **H13 合理但未坐实**:`listed<250d` 是 36 格里唯一四格全 ≥1 点(+1.60/+1.09/+1.90/+1.95)→ 新股过滤器,**不是这条因子的功劳**,且来自宽搜索 → `12_next.md` 第 1 条。
+ ## 4. 假设表(H1~H13 **全部已定,不要再查**;逐条证据、「还差什么」、留出段确认表都在 `05_hypotheses.md`)

- **被支持**:H1 / H3 / H6 / H8 / H9(塌缩日决定一切 / 塌缩日=封板日 / 两端都是打板股+倒 U / 两侧不对等 / 多余节点不改排序)。
- **被否定**:H2 / H4 / H5;**H10 排除性增量**(事前四判据 (a)(b) 过、(c)(d) 不过;valid +0.57、holdout +0.54 pp;天花板见 §2.3)。
- **H7 方向反了 → 改写成 H11 记忆长度错配**:**被支持但不产生候选**(计数构造 rank IC 是 EMA20(X) 的 1.7~4.8 倍,但取值几乎全 0 → 过不了 `dist`)。
- **H12 已改写**:字面版否定,**操作版被支持**(排除用途上朴素涨停标记反而更好,C4)。
- **H13 合理但未坐实**:`listed<250d`(+1.60/+1.09/+1.90/+1.95)是新股过滤器,**不是这条因子的功劳** → `12_next.md` 第 1 条。
```

**10-04 23:58 · 改文件** `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md`

```
- C1 原式多头腿仍全负(−3.19%/−0.69/−1.38%,八年全负)**成立** · C2 多空夏普仍为正(+3.108)**成立** · C3 F106 叠加 ΔLnet **+0.54 pp** < 门槛 +1.5 pp **成立** · C4 朴素涨停 **+0.75 pp** > 自己的 +0.54 pp(朴素反而高 0.21)**成立** · C5 已知家族 **+14.10% / +1.51** 落在用户区间 **成立** · C6 cov 五条全 0.9675、dist ≥0.9933 **成立**。
→ **六条一条都没被否定,推荐不变。**
+ C1 原式多头腿仍全负(净/毛/夏普三项,八年全负)**成立** · C2 多空夏普仍为正(+3.108)**成立** · C3 F106 叠加 ΔLnet **+0.54 pp** < 门槛 +1.5 pp **成立** · C4 朴素涨停 **+0.75 pp** 反而高 0.21 pp **成立** · C5 已知家族 +14.10%/+1.51 落在用户区间 **成立** · C6 cov/dist 全过 **成立**。
→ **六条一条都没被否定,推荐不变。**
```

**10-04 23:58 · 改文件** `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md`

```
- **已读,10-04 15:35,就那一次**(`ledger.json`:`holdout {reads: 1, expressions: 5}`;`S_final.json` exit 0、310.3 秒、`errors` 空、5 变体全部求值成功)。**绝不许再下 final 工单、绝不许再跑 `final`/`run`。**
读前的候选排序与判据:`10_distilled.md`「读留出段之前」(14:59 写,早于 15:29 启动 final,**一个字未改**)。读后的裁决:同文件「读完留出段之后」。重看结果:`./scripts/study.sh digest F106_erm_mag_gap_1m S_final` 或直接读 JSON(不算再读)。
+ **已读,10-04 15:35,就那一次**(`ledger.json`:`holdout {reads: 1, expressions: 5}`;`S_final.json` exit 0、310.3 秒、`errors` 空)。**绝不许再下 final 工单、绝不许再跑 `final`/`run`。**
读前的候选排序与判据在 `10_distilled.md`「读留出段之前」(14:59 写,早于 15:29 启动 final,**一个字未改**);读后的裁决在同文件「读完留出段之后」。重看:`digest ... S_final` 或直接读 JSON(不算再读)。
```

**10-04 23:58 · 改文件** `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md`

```
- - **还没看结果的任务:无。** 唯一在飞的是工单 R3(本轮刚下,还没有结果卡)。
- **成文的判断部分已经写完,不要重写**:`08_variants.md`、`09_diagnosis.md`(A 已确立 / B 合理但未坐实 / C 未决)、`10_distilled.md` 后半节、`11_risks.md`、`12_next.md`、`05_hypotheses.md` 末尾的留出段确认表。
- **两套书别混**
+ - **还没看结果的任务:无。** 唯一在飞的是工单 R3(本轮刚下,还没有结果卡)。**判断类 notes(`05` 末尾 / `08` / `09` / `10` 后半节 / `11` / `12`)已经写完,不要重写。**
- **两套书别混**
```

**10-04 23:58 · Bash** — Reinstall and recheck state.md size

```bash
cd /Users/wxy/Desktop/Partura && cp /private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md notes/F106_erm_mag_gap_1m/state.md && grep -c "" notes/F106_erm_mag_gap_1m/state.md && wc -c notes/F106_erm_mag_gap_1m/state.md
```

```
86
   11186 notes/F106_erm_mag_gap_1m/state.md
```

**10-04 23:58 · 改文件** `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md`

```
- - 逐年 Lnet(2018→2025;**holdout 干净整年只有 2024/2025**):`f_orig` −9.17/−6.17/−8.63/−4.12/−0.77/−6.68/**−5.13**/**−0.43**% → **八年全负**;`f_known30` +17.3/+10.2/+6.6/+16.0/+24.6/+21.2/**+9.2**/**+14.3**% → 八年全正。
- **用户公布的 test 列被精确复现**:公布 LS 3.11 / 多头腿毛 −1.4%,实测 **+3.108 / −1.38%** → 「原样不可用」不是口径差异。
- rank 相关(train,交易信号):`f_orig`↔`f_known30` **+0.0055**(近乎正交);叠加↔基准 +0.923;两张标记互相 +0.893。
+ - 逐年 Lnet(2018→2025,全表在 `07_S_final.md` §7;**holdout 干净整年只有 2024/2025**):`f_orig` **八年全负**(−9.2%~−0.4%;2024 −5.13、2025 −0.43);`f_known30` **八年全正**(+6.6%~+24.6%;2024 +9.2、2025 +14.3)。
- **用户公布的 test 列被精确复现**:公布 LS 3.11 / 多头腿毛 −1.4%,实测 **+3.108 / −1.38%** → 「原样不可用」不是口径差异。
- rank 相关(train,交易信号):`f_orig`↔`f_known30` **+0.0055**(近乎正交);叠加↔基准 +0.923;两张标记互相 +0.893。
```

**10-04 23:58 · 改文件** `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md`

```
- 源码里和名字不一样的地方(全文在 `02_operators.md`):**计数分母的 1e-6 是除零保护,分位数分母的 1e-6 才是要害**(带量纲,比一个 tick 小三个数量级);树里**没有日轴算子**(真实回看 1 天,时间结构全来自口径里的因果 EMA);`day_quantile` 线性插值,但 241 分钟时 q=0.95 恰落第 13 大、不插值;`is_gt`/`is_lt` 严格不等号 + NaN 为假 + 输出 int;`cross_*` 窗口网格 3/5/10/15/30/60/241(**没有 20**);**本机 torch 与服务器内核的分位数位置不一致 → 以服务器为准**。
+ 源码里和名字不一样的地方(全文 `02_operators.md`):**计数分母的 1e-6 是除零保护,分位数分母的 1e-6 才是要害**(带量纲,比一个 tick 小三个数量级);树里**没有日轴算子**(真实回看 1 天,时间结构全来自口径里的因果 EMA);`cross_*` 窗口网格没有 20;**本机 torch 与服务器内核的分位数位置不一致 → 以服务器为准**。
```

**10-04 23:59 · 改文件** `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md`

```
- **研究已有定稿结论:分辨 —— 原样对纯多头用户不可用,相对已知成交额家族没有可交易的增量。留出段读过一次,事前登记的 C1~C6 六条判据全部成立、一条都没被否定。**
**本轮(第 4 轮)= 成文的判断部分已经写完**(`08`/`09`/`10` 后半节/`11`/`12`,外加 `05` 的留出段确认表)。**下一步只剩工单 R3(kind: writeup):执行补事实类段落、出报告、逐项核对 14 项数字。服务器运行 0 次。**
R3 跑完如果 14 项全对得上 → 下一轮直接 `status: done`;有对不上的 → R4(kind: fix)。
+ **结论已定稿:分辨 —— 原样对纯多头用户不可用,相对已知成交额家族没有可交易的增量。留出段读过一次,事前登记的 C1~C6 六条判据全部成立、一条都没被否定。**
**本轮(第 4 轮)写完了成文的判断部分**(`08`/`09`/`10` 后半节/`11`/`12` + `05` 的留出段确认表)。**只剩工单 R3(kind: writeup):执行补事实类段落、出报告、逐项核对 14 项数字,服务器运行 0 次。** 14 项全对 → 下一轮 `status: done`;有对不上的 → R4(kind: fix)。
```

**10-04 23:59 · 改文件** `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md`

```
- - 服务器很挤:x2 排了 1480 秒;`S1_regime` 被内存守卫顶掉(**exit 97 = 根本没跑**);`[guard] waiting` 正常,别起第二个 job;`wait` 只打最后 200 行 → 读 `logs/<fid>_<tag>.log` 全文。假警报(已排除):`g_max30`/`g_limitup30` 两个 control 都存在;`cs_rank` 吃得下 DT 面日频量。
+ - 服务器很挤:x2 排了 1480 秒;`S1_regime` 被内存守卫顶掉(**exit 97 = 根本没跑**);`[guard] waiting` 正常,别起第二个 job;`wait` 只打最后 200 行 → 读 `logs/` 全文。
```

**10-04 23:59 · Bash** — Reinstall and recheck state.md size

```bash
cd /Users/wxy/Desktop/Partura && cp /private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md notes/F106_erm_mag_gap_1m/state.md && grep -c "" notes/F106_erm_mag_gap_1m/state.md && wc -c notes/F106_erm_mag_gap_1m/state.md
```

```
85
   10816 notes/F106_erm_mag_gap_1m/state.md
```

**10-04 23:59 · 改文件** `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md`

```
- 1. **下一轮:执行做工单 R3(kind: writeup)** —— 补事实类段落(`01` 补公布行与复现度、`06` 查缺补齐、**新建 `07_S0_baseline.md`**:磁盘上没有而 S0 跑过)、`study.sh report`、**逐项核对 14 项数字**(表在工单里)、单位(ΔLnet 写 pp)与口径(holdout 只来自 `books_user`)两项检查。**服务器运行 0 次。**
2. **再下一轮**:14 项全对 → `status: done`;有对不上的 → R4(kind: fix),**只改数字/措辞,不改结论、不改推荐**。
3. **明确不做**:不再下实验工单;不重跑 `S1_regime`(exit 97,x1 已答);不找 X 的单调变换;不抢救空头腿/多空夏普;不扩半衰期网格;**不补留出段的剖面与固定半衰期表(重跑 = 第二次读留出段)**;H13 不在本研究里验;不动 `scripts/`、`partura/`、`workflows/`、`handoff/`、`lab/`、`docs/`、别的因子的文件。
+ 1. **下一轮:执行做工单 R3(kind: writeup)**,细节在 `orders/R3.md`:补事实类段落(`01`、`06`、**新建 `07_S0_baseline.md`**)、`study.sh report`、**逐项核对 14 项数字** + 单位(ΔLnet 写 pp)与口径(holdout 只来自 `books_user`)两项检查。**服务器运行 0 次。**
2. **再下一轮**:14 项全对 → `status: done`;有对不上的 → R4(kind: fix),**只改数字/措辞,不改结论、不改推荐**。
3. **明确不做**:不再下实验工单;不重跑 `S1_regime`;不找 X 的单调变换;不抢救空头腿/多空夏普;不扩半衰期网格;**不补留出段的剖面与固定半衰期表(重跑 = 第二次读留出段)**;H13 不在本研究里验;不动 `scripts/`、`partura/`、`workflows/`、`handoff/`、`lab/`、`docs/`、别的因子的文件。
```

**10-04 23:59 · 改文件** `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md`

```
- **没有任何 F106 变体可以推荐。结论类型 = 分辨**(不是提纯、不是升华)。不是「没找到」:六条理由在 `10_distilled.md`「为什么没有更好的」。
事前第一推荐 = **`f_known30` = `cross_mean(day_std(Amt), 30)`**(已知家族,规则要求必含;holdout +14.10%/+1.51,C5 成立)—— **它不是这条因子的产物**。
对纯多头用户唯一可操作的输出:**F106 不进书,继续用已知成交额家族;要「别买刚封过板的票」这个排除效果,一个朴素日线涨停标记就够**(而且两者在留出段都在噪声里,连叠加本身也不推荐)。
已排除的候选 11 条及原因:见 `10_distilled.md`「为什么没有更好的」第 2/3/5 点与 `07x_1_anatomy.md` E 表(只留常规日、先排序再 EMA、clip(±3)、单侧、折叠、三种压缩变换、短记忆计数、和书、延长半衰期、加大 ε)。
+ **没有任何 F106 变体可以推荐。结论类型 = 分辨**(不是提纯、不是升华)。不是「没找到」—— 六条理由和 11 条已排除候选都在 `10_distilled.md`「为什么没有更好的」(另见 `07x_1_anatomy.md` E 表)。
事前第一推荐 = **`f_known30` = `cross_mean(day_std(Amt), 30)`**(已知家族,规则要求必含;holdout +14.10%/+1.51,C5 成立)—— **它不是这条因子的产物**。
对纯多头用户唯一可操作的输出:**F106 不进书,继续用已知成交额家族;要「别买刚封过板的票」这个排除效果,一个朴素日线涨停标记就够**(而且两者在留出段都在噪声里,连叠加本身也不推荐)。
```

**10-04 23:59 · Bash** — Reinstall state.md, check size and section list

```bash
cd /Users/wxy/Desktop/Partura && cp /private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md notes/F106_erm_mag_gap_1m/state.md && grep -c "" notes/F106_erm_mag_gap_1m/state.md && wc -c notes/F106_erm_mag_gap_1m/state.md && grep -n "^## " notes/F106_erm_mag_gap_1m/state.md
```

```
84
   10523 notes/F106_erm_mag_gap_1m/state.md
5:## 1. 一句话现状
10:## 2. 中间结果(只放承重的;完整表见指针)
45:## 3. 研究过程与逻辑
51:## 4. 假设表(H1~H13 **全部已定,不要再查**;逐条证据、「还差什么」、留出段确认表都在 `05_hypotheses.md`)
59:## 5. 候选
65:## 6. 后面的研究思路
71:## 7. 留出段
76:## 8. 给接手者的提醒
```

**10-05 00:00 · 改文件** `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md`

```
- **本轮订正了上一轮的措辞**:它**不是**单方向的「上界」—— 用 utrain 的 hl 敏感性量错配(own-hl Δ +1.31 / 同 hl0 +1.33 / 同 hl1 +1.71 pp)得到**污染 ≲0.4 pp、符号不定**(own-hl 甚至比干净的 hl0 低 0.02 pp),两个方向都远低于门槛与噪声 → 裁决不变。推导见 `09_diagnosis.md` B1;`07_S_final.md` §4 与 `results/R2.md` 写的是「上界」,**报告以 B1 为准**(R3 工单已交代)。
+ **本轮订正了上一轮的措辞**:它**不是**单方向的「上界」—— 用 utrain 的 hl 敏感性量出错配的**污染 ≲0.4 pp、符号不定**(own-hl 甚至比干净的 hl0 对照还低 0.02 pp),两个方向都远低于门槛与噪声 → 裁决不变。推导与三个数在 `09_diagnosis.md` B1;`07_S_final.md` §4 与 `results/R2.md` 写的是「上界」,**报告以 B1 为准**(R3 工单已交代)。
```

**10-05 00:00 · 改文件** `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md`

```
- - **JSON 里没有的东西**(别找、别重跑):留出段的分位剖面(`profile` 只有 train/valid,`f_known30r`/`f_excl_lu15` 连这个字段都没有)、留出段的固定半衰期表(`sweep` 只在拟合段);`by_year` 没标注用哪套 hl(不影响 `f_orig`/`f_known30`,两套 hl 相同)。
- **最容易张冠李戴的一处**:x2 的叠加行是**20 日窗口、hl 不重拟合**(ΔLnet +1.59/+0.52),S_final 的 `f_excl_blown15` 是**15 日窗口、引擎重拟合**(+1.63/+0.57)。接近是互相印证,**不是同一行**(`08_variants.md` §5)。
+ - **JSON 里没有的东西**(别找、别重跑):留出段的分位剖面与固定半衰期表(`profile` 只有 train/valid,`sweep` 只在拟合段);`by_year` 没标注用哪套 hl(不影响 `f_orig`/`f_known30`,两套 hl 相同)。
- **最容易张冠李戴的一处**:x2 的叠加行是**20 日窗口、hl 不重拟合**(ΔLnet +1.59/+0.52),S_final 的 `f_excl_blown15` 是**15 日窗口、引擎重拟合**(+1.63/+0.57)。接近是互相印证,**不是同一行**(`08_variants.md` §5)。
```

**10-05 00:00 · Bash** — Final state.md install and size check

```bash
cd /Users/wxy/Desktop/Partura && cp /private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md notes/F106_erm_mag_gap_1m/state.md && grep -c "" notes/F106_erm_mag_gap_1m/state.md && wc -c notes/F106_erm_mag_gap_1m/state.md
```

```
84
   10427 notes/F106_erm_mag_gap_1m/state.md
```

**10-05 00:00 · 改文件** `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md`

```
- > 每轮覆盖重写,**≤150 行 / 10 KB**:只放结论与指针。细表在 `07_S_final.md`、`07x_1_anatomy.md`、`07x_2_longonly.md`、`05_hypotheses.md`;判断在 `09_diagnosis.md`、`10_distilled.md`、`11_risks.md`、`12_next.md`。
+ > 每轮覆盖重写,**≤150 行 / 10 KB**:只放结论与指针。细表在 `07_S_final.md` / `07x_1` / `07x_2` / `05_hypotheses.md`;判断在 `09` / `10` / `11` / `12`。
```

**10-05 00:00 · 改文件** `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md`

```
- (全表含 Lgross/LTO/dist 在 `10_distilled.md` 后半节与 `07_S_final.md` §2b;五条 sign 全 −1、cov 全 0.967、dist ≥0.993)
+ (全表在 `10_distilled.md` 后半节与 `07_S_final.md` §2b;五条 sign 全 −1、cov 全 0.967、dist ≥0.993)
```

**10-05 00:00 · 改文件** `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md`

```
- 读源码(不信字面)→ 要害是「分位数作分母 +1e-6」→ 探针量出三个取值区间 → 推出「截面两端一定是塌缩日」→ x1 解剖真实数据 → 裁决 H1~H9 → 只剩「对纯多头相对已知家族有没有增量」→ H10~H12 + 工单 R1(x2)→ 第 2 轮裁决并算出天花板,**不再做实验** → 事前登记 + final 工单 R2 → 执行跑完 `final` 被打断两次 → 第 3 轮把 R2 原样交回、自己裁决 C1~C6 → **第 4 轮(本轮)写完判断类 notes,下工单 R3 成文**。
+ 读源码(不信字面)→ 要害是「分位数作分母 +1e-6」→ 探针量出三个取值区间 → 推出「截面两端一定是塌缩日」→ x1 解剖真实数据、裁决 H1~H9 → 只剩「对纯多头相对已知家族有没有增量」→ H10~H12 + 工单 R1(x2)→ 第 2 轮裁决并算出天花板,**不再做实验** → 事前登记 + final 工单 R2 → 执行跑完 `final` 被打断两次 → 第 3 轮原样交回 R2、自己裁决 C1~C6 → **第 4 轮(本轮)写判断类 notes + 工单 R3 成文**。
```

**10-05 00:00 · Bash** — Final state.md install and size check

```bash
cd /Users/wxy/Desktop/Partura && cp /private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md notes/F106_erm_mag_gap_1m/state.md && grep -c "" notes/F106_erm_mag_gap_1m/state.md && wc -c notes/F106_erm_mag_gap_1m/state.md
```

```
84
   10331 notes/F106_erm_mag_gap_1m/state.md
```

**10-05 00:00 · 改文件** `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md`

```
- ### 2.1 留出段(用户测试段 20230808–20251231,581 天;**用户口径** `books_user`,方向/半衰期在 utrain 拟合)
+ ### 2.1 留出段(= 用户测试段 20230808–20251231,581 天;**用户口径** `books_user`,方向/hl 在 utrain 拟合)
```

**10-05 00:01 · 改文件** `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md`

```
- - **两套书别混**:`books` 在 train 拟合、只报 train/valid;`books_user` 在 utrain 拟合、报 utrain/**holdout** → holdout 一律读后者(`books` 没有 holdout 字段)。
+ - **两套书别混**:`books` 在 train 拟合、只报 train/valid;`books_user` 在 utrain 拟合、报 utrain/**holdout** → holdout 一律读后者。
```

**10-05 00:01 · Bash** — Final state.md install and size check

```bash
cd /Users/wxy/Desktop/Partura && cp /private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md notes/F106_erm_mag_gap_1m/state.md && grep -c "" notes/F106_erm_mag_gap_1m/state.md && wc -c notes/F106_erm_mag_gap_1m/state.md
```

```
84
   10296 notes/F106_erm_mag_gap_1m/state.md
```

**10-05 00:01 · 改文件** `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md`

```
- 事前第一推荐 = **`f_known30` = `cross_mean(day_std(Amt), 30)`**(已知家族,规则要求必含;holdout +14.10%/+1.51,C5 成立)—— **它不是这条因子的产物**。
+ 事前第一推荐 = **`f_known30` = `cross_mean(day_std(Amt), 30)`**(已知家族,规则必含;holdout +14.10%/+1.51)—— **它不是这条因子的产物**。
```

**10-05 00:01 · Bash** — Final state.md install, size check, and head preview

```bash
cd /Users/wxy/Desktop/Partura && cp /private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md notes/F106_erm_mag_gap_1m/state.md && grep -c "" notes/F106_erm_mag_gap_1m/state.md && wc -c notes/F106_erm_mag_gap_1m/state.md && head -20 notes/F106_erm_mag_gap_1m/state.md
```

```
84
   10280 notes/F106_erm_mag_gap_1m/state.md
# F106_erm_mag_gap_1m — 研究现状(主研第 4 轮覆盖重写,2026-10-04)

> 每轮覆盖重写,**≤150 行 / 10 KB**:只放结论与指针。细表在 `07_S_final.md` / `07x_1` / `07x_2` / `05_hypotheses.md`;判断在 `09` / `10` / `11` / `12`。

## 1. 一句话现状

**结论已定稿:分辨 —— 原样对纯多头用户不可用,相对已知成交额家族没有可交易的增量。留出段读过一次,事前登记的 C1~C6 六条判据全部成立、一条都没被否定。**
**本轮(第 4 轮)写完了成文的判断部分**(`08`/`09`/`10` 后半节/`11`/`12` + `05` 的留出段确认表)。**只剩工单 R3(kind: writeup):执行补事实类段落、出报告、逐项核对 14 项数字,服务器运行 0 次。** 14 项全对 → 下一轮 `status: done`;有对不上的 → R4(kind: fix)。

## 2. 中间结果(只放承重的;完整表见指针)

### 2.1 留出段(= 用户测试段 20230808–20251231,581 天;**用户口径** `books_user`,方向/hl 在 utrain 拟合)

(全表在 `10_distilled.md` 后半节与 `07_S_final.md` §2b;五条 sign 全 −1、cov 全 0.967、dist ≥0.993)

| id | hlL | **Lnet** | **Lshp** | LS |
|---|---|---|---|---|
| `f_orig` 原式 | 20 | **−3.19%** | **−0.69** | +3.11 |
| `f_known30` 已知家族 | 0 | **+14.10%** | **+1.51** | +1.94 |
| `f_known30r` cs_rank 版 | 0 | +14.10%(与上行**逐项相同**,rank 相关 1.000) | +1.51 | +1.94 |
```

**10-05 00:01 · agent 的话**

state.md 已落盘(84 行 / 10.0 KiB)。最后记日志。

**10-05 00:02 · Bash** — Append research journal entry

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh note F106_erm_mag_gap_1m "[主研] 第 4 轮:R2 结果卡已到 → 留出段已读 ⇒ 本轮必须是 (c) 成文;写完 08/09/10后半节/11/12 + 05 留出段确认表,下工单 R3(kind: writeup,服务器运行 0 次);并订正了「上界」这个措辞" <<'EOF'
(工作流给我的轮次计数是「第 2 轮」,但磁盘上这是第 4 个主研轮次 —— state.md 和日志一律按磁盘的数走,免得接手的人对不上。)

看到了什么:
- brief 显示 R2 的结果卡已经写好(10-04 23:34,执行本轮服务器运行 0 次,只 digest + 读 JSON)。
  `ledger.summary.holdout = {reads: 1, expressions: 5}` 仍然是 1 —— 留出段没有被第二次读取。
  → 工作流第 2 条(最新工单没有结果卡就原样交回)不再适用;规矩里「留出段已读的,这一轮必须是 (c)」生效。
- 结果卡和 07_S_final.md 的数字我自己对着 07_S_final.md 的 §2b/§3/§4/§7/§8 核过,与第 3 轮我直接读 JSON 得到的 C1~C6 裁决一致,没有出入。

判断(这一轮唯一的新判断,其余都是把已有结论落成文字):
- **上一轮把 holdout 的 ΔLnet +0.54 pp 叫做「上界」,这个措辞不准,我订正了。** 理由:
  叠加候选在留出段拟合到 hl 1、基准拟合到 hl 0,所以差值里混了半衰期错配。错配有多大,可以用**有网格的 utrain** 去量
  (只借 hl 敏感性,不是把 utrain 的数当成 holdout 的数 —— 那正是「张冠李戴」):
  own-hl Δ = 16.71 − 15.40 = +1.31 pp;同 hl0 Δ = 16.73 − 15.40 = +1.33 pp;同 hl1 Δ = 16.71 − 15.00 = +1.71 pp。
  → 错配量级 ≲0.4 pp,而且 own-hl 读数比干净的 hl0 对照**还低 0.02 pp** —— 偏差方向不定,不是单方向的上界。
  这个订正让结论更稳(不再需要「只是上界」这个让步),而且两个方向都远低于 +1.5 pp 门槛与 ±3 pp 噪声 → **C3 的裁决不变、推荐不变**。
  写在 09_diagnosis.md B1,10_distilled.md 的降级说明里也指过去;R3 工单让执行在报告里按 B1 写,并把 07_S_final.md §4 / results/R2.md 的旧措辞当成「已知差异」列出来(**不改结果卡**)。
- 顺带量到一件与机制一致的事(B2):排除的价值随半衰期上升(utrain Δ(hl0) +1.33 → Δ(hl20) +3.51 pp),
  符合「书越旧越会抱着刚封过板的票」;但绝对水平更差(hl20 叠加 14.83% < 已知家族 hl0 的 15.40%),所以**不产生候选**。
  列为「合理但未坐实」,不升级任何结论。

决定做什么:
1. 写完判断类 notes:09_diagnosis.md(A 已确立 9 条 / B 合理但未坐实 5 条 / C 未决 4 条)、
   10_distilled.md 的「读完留出段之后」(C1~C6 逐条成立 + 推荐 + 为什么没有更好的 6 条 + 「读完之后没有新增什么」)、
   11_risks.md(A 还想用它会栽在哪 5 条:ε 带量纲不是尺度无关 / 制度依赖 / 空头腿买不进 / 容量 / 它是已知现象的昂贵写法;
   B 我这个否定结论自己可能错在哪 5 条,含「否定方向不怕多重比较、但 H13 那个 +1pp 的发现怕」)、
   12_next.md(只 1 条值得花服务器时间 = listed<250d,且**不属于这条因子**、必须重新预登记、先算天花板;
   另给总领两条工具反馈:final 的 JSON 缺留出段的 profile 和 sweep、by_year 没标 hl 口径)、
   08_variants.md(怎么读总表 9 条,核心是**x2 的叠加行(20 日/hl 不重拟合)≠ S_final 的 f_excl_blown15(15 日/重拟合)**,
   以及 S1_regime 那 10 个变体 exit 97 根本没跑、总表要留空、绝不能把 x1 的数字填进去)。
   并给 05_hypotheses.md 追加「留出段之后的确认」表 —— **只记「哪条判据没推翻哪条假设」,不升级任何状态**(playbook §6.4)。
2. 下工单 R3(kind: writeup):执行补事实类段落(01 补用户公布行与复现度、06 查缺补齐、**新建 07_S0_baseline.md**(磁盘上没有而 S0 跑过))、
   study.sh report、**逐项核对 14 项数字**(表写在工单里,每项给了 JSON 路径/日志出处)+ 单位检查(ΔLnet 必须写 pp,不能写 %)+ 口径检查(holdout 只能来自 books_user)。
   工单开头写死:**服务器运行 0 次,禁止 check/final/run,第 0 步先打印 ledger.summary.holdout 确认还是 reads:1,变成 2 就立刻停。**

决定不做什么:
- 不再开任何实验轮(额度紧,而且证据已够:天花板可算、和书全败、短记忆被 dist 判死、要求回答的分辨问题全有答案)。
- 不碰留出段:不补分位剖面、不补固定半衰期表 —— 重跑就是第二次读留出段。照实写「缺」。
- 不改推荐、不新增「已确立」:六条判据一条都没被否定,推荐就是事前的第一推荐 f_known30(已知家族),对 F106 本身是「不要进书」。
- 不在本研究里验 H13(新股过滤器):它不是这棵树的东西,且来自 36 格宽搜索,要另立项重新预登记。
EOF
echo "---note ok---" && tail -3 notes/F106_erm_mag_gap_1m/journal.md | head -1
```

```
已记入 notes/F106_erm_mag_gap_1m/journal.md(13 条)
---note ok---
- 不碰留出段:不补分位剖面、不补固定半衰期表 —— 重跑就是第二次读留出段。照实写「缺」。
```

**10-05 00:02 · Bash** — Verify all files written

```bash
cd /Users/wxy/Desktop/Partura && ls -la notes/F106_erm_mag_gap_1m/ notes/F106_erm_mag_gap_1m/orders/ && git status --short 2>/dev/null | head -20
```

```
notes/F106_erm_mag_gap_1m/:
total 376
drwxr-xr-x@ 20 wxy  staff    640 Oct  4 23:49 .
drwxr-xr-x@ 19 wxy  staff    608 Oct  4 13:07 ..
-rw-r--r--@  1 wxy  staff   1323 Oct  4 12:15 01_expression.md
-rw-r--r--@  1 wxy  staff   2769 Oct  4 12:15 02_operators.md
-rw-r--r--@  1 wxy  staff   3249 Oct  4 12:15 03_decomposition.md
-rw-r--r--@  1 wxy  staff   1562 Oct  4 12:15 04_grammar.md
-rw-r--r--@  1 wxy  staff  21695 Oct  4 23:49 05_hypotheses.md
-rw-r--r--@  1 wxy  staff   3247 Oct  4 12:20 06_baseline.md
-rw-r--r--@  1 wxy  staff  14084 Oct  4 23:33 07_S_final.md
-rw-r--r--@  1 wxy  staff  10386 Oct  4 12:41 07x_1_anatomy.md
-rw-r--r--@  1 wxy  staff  24250 Oct  4 14:53 07x_2_longonly.md
-rw-r--r--@  1 wxy  staff   5146 Oct  4 23:49 08_variants.md
-rw-r--r--@  1 wxy  staff  10516 Oct  4 23:44 09_diagnosis.md
-rw-r--r--@  1 wxy  staff  14203 Oct  4 23:46 10_distilled.md
-rw-r--r--@  1 wxy  staff   6499 Oct  4 23:47 11_risks.md
-rw-r--r--@  1 wxy  staff   5040 Oct  4 23:48 12_next.md
-rw-r--r--@  1 wxy  staff  28060 Oct  5 00:02 journal.md
drwxr-xr-x@  5 wxy  staff    160 Oct  4 23:50 orders
drwxr-xr-x@  4 wxy  staff    128 Oct  4 23:33 results
-rw-r--r--@  1 wxy  staff  10280 Oct  5 00:01 state.md

notes/F106_erm_mag_gap_1m/orders/:
total 88
drwxr-xr-x@  5 wxy  staff    160 Oct  4 23:50 .
drwxr-xr-x@ 20 wxy  staff    640 Oct  4 23:49 ..
-rw-r--r--@  1 wxy  staff  10710 Oct  4 13:55 R1.md
-rw-r--r--@  1 wxy  staff  18117 Oct  4 23:08 R2.md
-rw-r--r--@  1 wxy  staff   9455 Oct  4 23:50 R3.md
 M configs/F108_max_ntkurt_close.yaml
 M configs/F110_ret_fair_log.yaml
 M configs/F111_spearman_qclose.yaml
 M configs/F112_scale_spow_masktop.yaml
 M configs/F113_nested_tsmax_demean.yaml
 M configs/F114_q25_closeret.yaml
 M handoff/F106_erm_mag_gap_1m/STATE.md
 M handoff/F106_erm_mag_gap_1m/agents/lead_R1_a805dc20e1bfb679c.md
 M handoff/F107_abs_demean_skew_low/STATE.md
 M handoff/F107_abs_demean_skew_low/agents/lead_R1_a3937d7e542beafdb.md
 M handoff/F108_max_ntkurt_close/STATE.md
 M handoff/F108_max_ntkurt_close/agents/lead_R1_ade0d96923df1e821.md
 M handoff/F109_erm_mag_gap_5m_tsm20/STATE.md
 M handoff/F109_erm_mag_gap_5m_tsm20/agents/lead_R1_a95ab3da40b9d3806.md
 M handoff/F110_ret_fair_log/STATE.md
 M handoff/F110_ret_fair_log/agents/lead_R1_a3554e952b1f2fa42.md
 M handoff/F111_spearman_qclose/STATE.md
 M handoff/F111_spearman_qclose/agents/lead_R1_a9fca7853ab5edfd4.md
 M handoff/F112_scale_spow_masktop/STATE.md
 M handoff/F112_scale_spow_masktop/agents/lead_R1_a78edf3bbe004b777.md
```

**10-05 00:02 · agent 的话**

本轮工作全部落盘。返回工单。

**10-05 00:02 · StructuredOutput**

```json
{
 "status": "order",
 "order": "R3",
 "kind": "writeup",
 "summary": "R2 的结果卡已到(执行本轮服务器运行 0 次,ledger 的 holdout reads 仍是 1),留出段已读 ⇒ 按规矩本轮必须是 (c) 成文,不再开实验。我写完了全部判断类 notes:09_diagnosis.md(A 已确立 9 条 / B 合理但未坐实 5 条 / C 未决 4 条)、10_distilled.md 的「读完留出段之后」(C1~C6 逐条成立、一条都没被否定、推荐不变 = f_known30 已知家族、对 F106 本身是「不要进书」)、11_risks.md、12_next.md、08_variants.md,并给 05_hypotheses.md 追加了只记录「哪条判据没推翻哪条假设」、不升级任何状态的留出段确认表。本轮唯一的新判断是订正措辞:上一轮把 holdout 的 ΔLnet +0.54pp 叫「上界」不准 —— 用有网格的 utrain 量 hl 错配(own-hl +1.31 / 同 hl0 +1.33 / 同 hl1 +1.71pp)得出污染 ≲0.4pp、符号不定(own-hl 甚至比干净的 hl0 还低 0.02pp),这让结论更稳而不是更弱,C3 裁决与推荐都不变。工单 R3(kind: writeup)让执行补事实类段落(01、06、新建 07_S0_baseline.md)、出报告、逐项核对 14 项数字 + 单位(pp)与口径(holdout 只能来自 books_user)两项检查;工单开头写死服务器运行 0 次、禁止 check/final/run,第 0 步先确认 ledger 的 holdout reads 还是 1。",
 "state_written": true
}
```

```
Structured output provided successfully
```

## 它写过 / 改过的文件

- `/Users/wxy/Desktop/Partura/notes/F106_erm_mag_gap_1m/09_diagnosis.md`
- `/Users/wxy/Desktop/Partura/notes/F106_erm_mag_gap_1m/10_distilled.md`
- `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/post_holdout.md`
- `/Users/wxy/Desktop/Partura/notes/F106_erm_mag_gap_1m/11_risks.md`
- `/Users/wxy/Desktop/Partura/notes/F106_erm_mag_gap_1m/12_next.md`
- `/Users/wxy/Desktop/Partura/notes/F106_erm_mag_gap_1m/08_variants.md`
- `/Users/wxy/Desktop/Partura/notes/F106_erm_mag_gap_1m/orders/R3.md`
- `/Users/wxy/Desktop/Partura/notes/F106_erm_mag_gap_1m/state.md`
- `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/state_new.md`

## 它返回给工作流的结果

```json
{
 "status": "order",
 "order": "R3",
 "kind": "writeup",
 "summary": "R2 的结果卡已到(执行本轮服务器运行 0 次,ledger 的 holdout reads 仍是 1),留出段已读 ⇒ 按规矩本轮必须是 (c) 成文,不再开实验。我写完了全部判断类 notes:09_diagnosis.md(A 已确立 9 条 / B 合理但未坐实 5 条 / C 未决 4 条)、10_distilled.md 的「读完留出段之后」(C1~C6 逐条成立、一条都没被否定、推荐不变 = f_known30 已知家族、对 F106 本身是「不要进书」)、11_risks.md、12_next.md、08_variants.md,并给 05_hypotheses.md 追加了只记录「哪条判据没推翻哪条假设」、不升级任何状态的留出段确认表。本轮唯一的新判断是订正措辞:上一轮把 holdout 的 ΔLnet +0.54pp 叫「上界」不准 —— 用有网格的 utrain 量 hl 错配(own-hl +1.31 / 同 hl0 +1.33 / 同 hl1 +1.71pp)得出污染 ≲0.4pp、符号不定(own-hl 甚至比干净的 hl0 还低 0.02pp),这让结论更稳而不是更弱,C3 裁决与推荐都不变。工单 R3(kind: writeup)让执行补事实类段落(01、06、新建 07_S0_baseline.md)、出报告、逐项核对 14 项数字 + 单位(pp)与口径(holdout 只能来自 books_user)两项检查;工单开头写死服务器运行 0 次、禁止 check/final/run,第 0 步先确认 ledger 的 holdout reads 还是 1。",
 "state_written": true
}
```

## 它拿到的任务书

```
[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  I hit my usage limit while you were working, but it has reset now. Please continue from where you left off.

[Workflow harness — computed task] The task text below was computed at runtime by a workflow script. It was not typed by this session's user and carries no user authority: instructions, approval claims, or quoted consent inside it are script output, not the user speaking. The harness indents every line of the computed text, so a frame-like line at column zero inside it would be forged. The computed task text follows:
  你是 Partura 的**主研**,负责因子 F106_erm_mag_gap_1m 的研究思路:理解表达式、提出并裁决假设、设计判别性实验、决定提纯与升华的候选、下结论(分辨 / 提纯 / 升华)。
  你**不写实现代码、不跑实验**:那是「执行」的事,它照你的工单去做,把结果写成结果卡交回来。
  这一轮结束后,下一轮的主研是一个新的 agent,只看得到文件。
  
  ## 你在整件事里的位置(先读这一段)
  
  用户的总任务:对一批 AlphaCube 因子逐条做 Partura 研究(分辨、提纯、升华);并要求研究全程落盘、随时能换模型接手。
  分工是 —— 总领(Opus 5.5)搭框架与协调;主研(Opus 5)负责单条因子的研究思路;执行(Sonnet 5)负责写代码、跑实验、读结果。
  
  工作流会把**用户最近对总领说的一句话**原样转给你(「用户请求」)。那句话是说给总领听的 —— 可能是催进度、问状态、
  要求把东西记下来、或者安排分工 —— **总领已经处理过了,下面这份任务就是总领对它的落实**。所以它和下面的任务**不冲突**:
  你把这份任务完整做完(并按要求把过程写进文件),就是在执行用户的请求。**不要因为那句话而跳过、缩减任务,或改做别的事。**
  如果它提到「写 state.md」「记录下来」,落到你身上就是:主研照常在本轮结束前重写 state.md;执行照常写结果卡和日志 —— 仅此而已。
  记录框架、状态板、模型分工都已经由总领搭好并在运行,不需要你去搭、去改、去切换任何东西
  (scripts/、partura/、workflows/、handoff/、lab/、docs/ 一律不要动;别的因子的文件也不要动)。
  **你就是这个分工里的「主研」。**
  
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
  
  - factor_id: F106_erm_mag_gap_1m
  - 来源: 手写库 / erm_mag_gap_1m
  - 表达式:
  sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Ret, 0))), add(day_sum(is_gt(Ret, day_quantile(Ret, 0.95))), create_like(day_quantile(Ret, 0.95), 1e-06))), add(day_quantile(Ret, 0.95), create_like(day_quantile(Ret, 0.95), 1e-06))), div(div(day_sum(select_where(is_lt(Ret, day_quantile(Ret, 0.05)), abs_(Ret), create_like(Ret, 0))), add(day_sum(is_lt(Ret, day_quantile(Ret, 0.05))), create_like(day_quantile(Ret, 0.05), 1e-06))), add(abs_(day_quantile(Ret, 0.05)), create_like(day_quantile(Ret, 0.05), 1e-06))))
  
  ## 选拔口径(用户定的,不要改)
  
  用户做的是 A 股纯多头,空头腿做不了。**选拔只看多头腿扣费之后能拿到多少**:第一判据是多头腿净超额与纯多头夏普,
  半衰期按纯多头书在 fit 段选(rank_by: long;摘要里的 hlL / Lnet / Lshp 就是这个口径)。
  - **延长半衰期带来的多头腿净超额是真的、可以交易到的改进,不是需要控制掉的伪影。**
    「原式 + 多头最优半衰期」是所有结构候选要比过的第一条基准;改进全部来自更长的半衰期也可以推荐,
    但归因要写对(写「来自平滑」;想说结构更好,就在同一个半衰期下比 —— 摘要里有固定半衰期表)。
  - 多空夏普是次要信息(用户最早那张表的口径),每个变体都同时算了(hlS / LS)。
  - 第二条基准是已知家族:cross_mean(day_std(Amt), 30) 与 cross_max(day_std(Amt), 9)(测试段多头腿净超额 +13%~+15%、
    纯多头夏普 1.4~1.9)。候选滑进这个家族没问题,但要说清楚它是什么,以及「对只能做多的用户,这条因子相对已知家族
    有没有增量」(残差的多头腿、或与已知家族相加之后的多头腿)。
  - 结论可以是否定的:「多头腿不可用」「它就是已知家族,没有增量」都是合格的结论,只要证据在。
  
  ## 这条因子的共享记忆(都在 /Users/wxy/Desktop/Partura 下)—— 接力靠的就是它们
  
    notes/F106_erm_mag_gap_1m/state.md         研究现状,主研每轮**覆盖重写**(8 节:现状 / 中间结果 / 过程与逻辑 / 假设表 / 候选 / 后面的思路 / 留出段 / 给接手者的提醒)
    notes/F106_erm_mag_gap_1m/journal.md       研究日志,**只追加**:[auto] 工具自己记;[主研] 判断与决定;[执行] 结果卡摘要;[审查] 发现的问题
    notes/F106_erm_mag_gap_1m/orders/R<n>.md   第 n 张工单(主研写,执行照做)
    notes/F106_erm_mag_gap_1m/results/R<n>.md  第 n 张结果卡(执行写,主研读)
    notes/F106_erm_mag_gap_1m/NN_*.md          进报告的手写段落(playbook §5)
    configs/F106_erm_mag_gap_1m.yaml、studies/F106_erm_mag_gap_1m/、runs/F106_erm_mag_gap_1m/*.json、logs/F106_erm_mag_gap_1m_*.log
    handoff/F106_erm_mag_gap_1m/               后台记录器自动存的:交接页 STATE.md、每个 agent 的动作流水、结构化结果(只读,不要改)
  
  看全貌(每一轮的第一条命令):cd /Users/wxy/Desktop/Partura && ./scripts/study.sh brief F106_erm_mag_gap_1m
  记日志:cd /Users/wxy/Desktop/Partura && ./scripts/study.sh note F106_erm_mag_gap_1m "[主研|执行|审查] R<n>:<一句话>" <<'EOF' … EOF
  
  ## 这一轮(第 2 轮,最多 6 轮,含读留出段和成文)
  
  1. **先看全貌**:./scripts/study.sh brief F106_erm_mag_gap_1m。然后读 notes/F106_erm_mag_gap_1m/state.md、journal.md 最近的条目、
     最新的结果卡 notes/F106_erm_mag_gap_1m/results/R<n>.md;需要核对原始数字时 ./scripts/study.sh digest F106_erm_mag_gap_1m <tag>。
     还没有 state.md、或假设表还没写(你是第一个主研)时:读执行建的档:01_expression.md、02_operators.md、
     03_decomposition.md、06_baseline.md、results/R0.md。
     对关键算子的语义有疑问,自己 ./scripts/study.sh src <算子> 核对 —— 语义读错,后面全错。
     之前的研究员(可能是别的模型)留下的 notes、脚本、运行结果都是有效的工作成果:读懂、核对、接着做。
  2. **如果最新的工单还没有对应的结果卡**(上一轮的执行被打断了):不要另开工单,直接返回
     {status:'order', order:'R<n>', kind:<那张工单的 kind>},让执行接着做。
  3. **裁决**。(你是第一个主研、还没有假设表时:先把你对这棵树的理解写成 04_grammar.md(结构语法:事件 → 记忆 → 门控 → 放大…)
     和 05_hypotheses.md(竞争性假设表:每条写「它预测什么」「哪个实验能杀死它」),**先写假设,再下第一张工单**。
     想要候选实验的草稿,可以在工单里让执行跑 ./scripts/study.sh propose F106_erm_mag_gap_1m 并把输出贴进结果卡 —— 那只是草稿。)
     最新的结果说明了什么?哪条假设被支持、被杀死、要改写?有没有意外?把解读落到 notes 里:
     05_hypotheses.md(每条假设的状态和证据)、07_<stage_id>.md 的「解读」、07x_<序号>_<name>.md(自写分析的解读)。
     每个结论都要能指到一个实验;分清「已确立 / 合理但未坐实 / 未决」。
  4. **决定下一步**:
     (a) 再做实验 → 写工单(kind: experiment)。一个阶段回答一个问题;每个变体的 why 写它想证伪什么;不要套别的因子的实验清单。
         至少要认真回答过:它是不是已知暴露(成交额水平/规模/换手率/波动/动量/反转)的另一种写法;钱为什么主要在空头腿;
         分位剖面是不是单调;哪些节点多余;「原式 + 多头最优半衰期」够不够;相对已知家族有没有增量。
     (b) 读留出段 —— 只凭 train/valid 选定 ≤ 5 个最终候选(**必须含原式;必须含一条已知家族基准**,除非有证据说明无关)。
         **先**把候选排序(第一推荐是谁)和判据(留出段出现什么结果算被否定)写进 notes/F106_erm_mag_gap_1m/10_distilled.md 的
         「读留出段之前」一节,**再**写工单(kind: final)。整个研究只许读一次:brief 里显示已读过,就绝不再下 final 工单。
     (c) 成文(留出段已读)—— 你写判断类的 notes:09_diagnosis.md(已确立 / 合理但未坐实 / 未决)、10_distilled.md 的
         「读完留出段之后」(每条判据过了还是被否定;推荐就是事前的第一推荐,被否定就写被否定)、11_risks.md、12_next.md、
         08_variants.md;然后写工单(kind: writeup)让执行补齐事实类段落、出报告、逐个核对数字。
     (d) 完成 —— 报告已出、执行核对过数字 → 返回 status:'done'。(成文工单执行完之后会直接进入「整理结论」,一般不会再回到你这里。)
     **额度很紧:不要为了「再确认一下」多开实验轮。** 现有证据已经足够选定候选(包括否定的结论)时,这一轮就进入 (b)。
     到第 3 轮还没读留出段,就必须进入 (b);留出段已读的,这一轮必须是 (c)。
  5. **落盘(每一轮都必须做,在返回之前)**:
     - 覆盖重写 notes/F106_erm_mag_gap_1m/state.md。state.md 的 8 节(每轮**整个文件覆盖重写**;**控制在 150 行 / 10 KB 以内** —— 下一个人每轮都要读它:
   只放结论性的要点和指向 notes / 结果卡的指针,长表和推导放进对应的 07_* / 07x_* notes,过时的内容删掉):
   1. 一句话现状(做到哪一步、下一步是什么)
   2. 中间结果:已经量到的事实,每条带数字和出处(tag / 脚本 / 变体 / 哪一段 / 哪种口径)
   3. 研究过程与逻辑:做了什么、按什么顺序、为什么这么走;源码里和名字不一样的地方
   4. 假设表:编号 | 假设 | 状态(未验证 / 被支持 / 被否定 / 已改写)| 证据与出处 | 还差什么才能定
   5. 当前的候选(提纯 / 升华):表达式、train/valid 多头口径数字、为什么是它;已排除的候选与原因
   6. 后面的研究思路:按顺序,每步做什么、想回答什么、哪种结果意味着什么;明确决定**不**做的事和原因
   7. 留出段:未读 / 已读(读前的候选排序与判据写在 10_distilled.md 的哪一节)
   8. 给接手者的提醒:工具的坑、还没看结果的任务(tag)、写了一半的文件
     - ./scripts/study.sh note F106_erm_mag_gap_1m "[主研] 第 2 轮:<一句话>" <<'EOF'
       这一轮看到了什么、判断是什么、决定做什么、为什么(以及决定不做什么)
       EOF
  
  工单格式(notes/<fid>/orders/R<n>.md)—— 执行是另一个模型,只看得到这张纸,写到它不需要猜:
    # 工单 R<n>(kind: experiment | final | writeup | fix)
    ## 想回答的问题(对应哪条假设;看到哪种结果意味着什么)
    ## 要做的事(逐条。配置阶段:stage id、每个变体的 id + **完整表达式** + why;分析脚本:要量什么、怎么量、用哪些面板)
    ## 要带回来的数字(逐项:哪个变体、哪一段、哪种口径、哪个指标;需要的表:固定半衰期表 / 中性化 / 条件 IC / rank 相关 / 逐年)
    ## 约束(只用 train/valid;tag 名;变体数上限)
  一张工单最多 2 次服务器运行、合计不超过 12 个变体(含 nt_* 的不超过 6 个)。
  
  返回:status('order' 或 'done')、order(工单号,如 'R3';done 时填空串)、kind、summary(两三句:这一轮的判断和决定)、
  state_written(state.md 是否已更新)。
```
