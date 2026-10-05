# lead:F109_erm_mag_gap_5m_tsm20#1 — agent a95ab3da40b9d3806(工作流 wf_e3cc1b20-34b)

- 状态:**已返回结果**;开始 10-04 23:03,最后一次动作 10-04 23:22;工具调用 65 次
- 这是从 agent 的对话记录里**自动抽出来的动作流水**(命令、输出、写了哪些文件)。agent 的推理不在记录里 ——
  它的判断要看 `notes/F109_erm_mag_gap_5m_tsm20/journal.md` 和各 notes 文件。输出过长的地方截了中间。

## 动作流水

**10-04 23:03 · agent 的话**

I'll start by getting the full picture of this factor's research state.

**10-04 23:03 · Bash** — Get factor research overview

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh brief F109_erm_mag_gap_5m_tsm20 2>&1 | head -200
```

```
# F109_erm_mag_gap_5m_tsm20 — 交接状态

_自动生成于 2026-10-04 23:03(`python scripts/recorder.py --brief F109_erm_mag_gap_5m_tsm20` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:手写 erm_mag_gap_5m_tsm20(批次 B01_single_factors)
- 表达式:`ts_mean(sub(div(div(day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95)), sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), create_like(Close, 0))), add(day_sum(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95))), create_like(day_quantile(Ret, 0.95), 1e-06))), add(day_quantile(Ret, 0.95), create_like(day_quantile(Ret, 0.95), 1e-06))), div(div(day_sum(select_where(is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05)), abs_(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1))), create_like(Close, 0))), add(day_sum(is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05))), create_like(day_quantile(Ret, 0.05), 1e-06))), add(abs_(day_quantile(Ret, 0.05)), create_like(day_quantile(Ret, 0.05), 1e-06)))), 20)`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- **留出段已经读过 1 次**(10-04 15:19)—— **不许再读**。候选在留出段上的数全在 `runs/F109_erm_mag_gap_5m_tsm20/final.json`(`./scripts/study.sh digest F109_erm_mag_gap_5m_tsm20 final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `lead:F109_erm_mag_gap_5m_tsm20#3`:失败,最后动作 10-04 15:41 → `handoff/F109_erm_mag_gap_5m_tsm20/agents/lead_R3_a05fc8a6af5081324.md`
  - `lead:F109_erm_mag_gap_5m_tsm20#3`:失败,几乎没做事
  - `lead:F109_erm_mag_gap_5m_tsm20#1`:还在跑(多半就是你自己)

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F109_erm_mag_gap_5m_tsm20` 看服务器上的 tag,`./scripts/study.sh digest F109_erm_mag_gap_5m_tsm20 <tag>` 重看结果)。

## 研究现状(`notes/F109_erm_mag_gap_5m_tsm20/state.md`,10-04 15:00 更新)—— **先读这个文件**

# F109_erm_mag_gap_5m_tsm20 — 研究现状(主研第 4 轮重写,2026-10-04)

> 这一页由**主研**整个覆盖重写(第 4 轮;新工作流下的第 2 轮)。
> **这一轮是第一次拿到引擎口径的结构证据**(`results/R1.md` = tag `S1_lvl` 10 变体 + 自写脚本 `x2_incremental`),
> 14 条假设全部有了结论,**所有需要新实验才能定的问题都定完了** → 这一轮进入「读留出段」。
> 前三轮主研的事实与判断我逐条核对后保留(数字和出处都没变);这一轮**改写了 4 条假设**(H1、H10 后半、H11、H13),
> 其中两条推翻了前面主研写在纸上的事前预测。下一位主研只看得到文件 —— 这页写的是判断,事实都标了出处。

---

## 1. 一句话现状

**结论已经定了:分辨。** 这棵树对纯多头的用户没有可用的多头腿、也不给已知家族加东西;
它的钱全在空头腿(用户做不了,而且一半是「次日一字开盘买不进」撑出来的);
把它的结构一步步修好之后,它收敛成**已实现偏度 / 低波低活跃暴露**的一个更差写法。
**这一轮(第 4 轮)干的事**:读完 `results/R1.md`,裁决全部 14 条假设,写了四份解读 notes
(`07_S1_nodes.md`、`07_S2_level.md`、`07_neutralise.md`、`07x_2_incremental.md`)和
`10_distilled.md` 的「读留出段之前」(5 个候选 + 排序 + 7 条判据),然后下了 `orders/R2.md`(**kind: final**)。
**下一步 = 执行按 `orders/R2.md` 跑唯一一次 `study.sh final`(阶段 `S_final`,5 个候选,tag `S_final`),写 `results/R2.md`。**
再下一轮主研的事:把留出段数字逐条对 `10_distilled.md` 的判据 A~G,填「读完留出段之后」一节,
然后写 `09_diagnosis.md` / `11_risks.md` / `12_next.md` / `08_variants.md`,下 writeup 工单。

---

(…全文 17330 字符,读 `notes/F109_erm_mag_gap_5m_tsm20/state.md`)

## 研究日志(`notes/F109_erm_mag_gap_5m_tsm20/journal.md`:14 条,其中研究员自己写的 6 条)

最近的 5 条(更早的和全文看文件):

### 2026-10-04 14:32 [执行] R1:按修订A'收尾,S1_lvl(10变体)+x2_incremental都exit 0,结果卡已写

A组(tag S1_lvl,阶段S1_nodes+S2_level,10变体,一次run,无排队):a_sum在hl20(固定)下train多头腿净超额+0.8%,不到工单判据的+3%门槛;
hl20下train多头腿净超额最高的是a_sig(+2.3%,valid+10.9%)。只有a_evt没过dist门槛(0.0153<0.5),其余9个cov/dist都是1.00。
b_lvl/b_lvlq与ctl_price的rank相关分别是-0.32/-0.00,与known_stdamt_mean30分别是-0.40/-0.30,都没到H13写的|.|>=0.5。

B组(自写脚本x2_incremental.py,一次exec):自检通过——BASE(numpy重构)train/valid=-4.7%/+0.3%,FAM30=+12.6%/+22.3%,
都对上x1/S0的已知答案。BASE/REG/EVT对FAM30的秩空间残差R2都很小(0.005~0.022),但EVT残差后Lnet从-3.5%/-3.3%跌到-14.4%/-14.7%。
9个rank-add组合里只有FAM30+0.3*EVT的配对差在train/valid都显著为正(t+3.27/+3.03,年化+1.0%/+0.8%);
0.3*BASE、1*BASE、0.3*REG、1*REG配对差都显著为负。FAM30多头十分位里EVTFLAG占比train 6.78%/valid 1.94%(x1估的<3%只在valid段成立);
剔除后Lnet train +12.6%→+16.1%(配对差t+2.68)、valid +22.3%→+22.9%(配对差t+2.13,量级小很多)。

结果卡:notes/F109_erm_mag_gag_5m_tsm20/results/R1.md(应为erm_mag_gap,见下一行更正)。
结果卡路径:notes/F109_erm_mag_gap_5m_tsm20/results/R1.md。propose的90条草稿在notes/F109_erm_mag_gap_5m_tsm20/R1_propose_draft.txt。

### 2026-10-04 15:01 [主研] 第 2 轮(总第 4 轮):裁决完 14 条假设,结论定为分辨;下 final 工单 R2(5 个候选,第一推荐是已知家族)

我是第 4 轮主研(新工作流第 2 轮)。最新工单 R1 有结果卡了,所以这一轮做裁决 + 进 (b) 读留出段。

看到了什么(都带数字写进 state.md §2.4/§2.5,解读写进四份新 notes):
1. **结构能把多头腿抬 +5~7 个点,但抬不到可交易。** 固定半衰期 hl 20 下:a_sig +2.3%(夏普 0.31)、
   a_sum +0.8%、a_up −0.4%、a_eps3 −1.1%,原式 −4.6%。家族是 +12.6% / 夏普 1.78 —— 差一个数量级。
   而且 a_sig 的 +2.3% 是 2018 一年撑的(2018 +11.1%、2019 +0.1%、2020 −1.0%、2021 −1.6%);
   a_sum 四年全在 ±2% 内,它 valid 的 +9.6% 全在 2022–23(低价低波风格年,ctl_price 自己 +11.3%)。
2. **两条事前预测被证伪,我改写了假设(不是改判据)。**
   (a) H1 说「ε 加地板 → 空头腿塌」:错。a_eps3 的空头腿 +39.5%/+36.3% 比原式 +34.4%/+28.4% 还高,
       rIC 0.0394/0.0435 也更高;a_sig 连分母都没有,空头腿 +40.4%/+44.1%。
       → ε 只决定幅度,不决定排序;起作用的是「哪天被标成事件」这个集合。a_evt(只数封板天数)
       多空 +3.93、空头腿 +44.9%,比原式那套 29 个中间量还高 —— 但 dist 0.0153 过不了门槛。
   (b) H11 说减法把爬升型涨停票送进多头端:机制对(a_sum 把 Q10 从 −3.6% 抬到 +2.7%,量级与事前估的
       5.5 点吻合),但 Q10 仍然低于 Q9(+9.9%);a_up(整个下侧不要)、a_eps3(没有爆炸)的翻转也都没消失。
       → 多头端翻转不是减法造成的,是这一族取极值本身的性质。十个变体没有一个修掉它。
   (c) H7 不但成立还反向加强:把它改写成同尺度的标准 ES/VaR 比(a_q5)或 1 分钟版(a_1m),rIC 砍一半
       (0.019/0.013、0.019/0.011 vs 原式 0.031/0.030)
…(这条日志还有后文,读 journal.md)

### 2026-10-04 15:14 [auto] ⚠ 读留出段:final S_final,阶段 S_final(留出段只能读这一次;候选与判据应当已经写在 10_distilled.md 里)

### 2026-10-04 15:20 [auto] S_final 跑完(exit 0);重看结果:./scripts/study.sh digest F109_erm_mag_gap_5m_tsm20 S_final

### 2026-10-04 15:29 [执行] R2:final 跑完(exit 0,一次过),判据G全部复现,结果卡已写

配置加阶段 S_final(5 变体,f_fam30/f_sig/f_orig/f_sum/f_lvl,全部 final: true,表达式用脚本按变体 id 从原 yaml 整行取出并断言逐字节相等)。
check 31/31 OK。final 一次 wait 就完成,无排队、无 exit 97,334.0s,peak anon 5.76 GiB,日志里没有任何 [panels] 行、
JSON errors={}——5 个面板全部缓存命中。ledger.json 已记上 1 条 holdout 读取。

判据G(books,train-fit)全部对上(最大偏差 0.04pp):f_orig -4.62%、f_sig +2.27%、f_sum +0.84%、f_lvl +0.14%(hl5)、
f_fam30 +12.62%/+22.33%(hl0),hlL/sign 都与工单期望一致。

留出段主表(books_user,utrain-fit,数字只抄不判):
  f_fam30  holdout Lnet +14.10%  Lshp +1.509  (utrain +15.40%/+2.224)
  f_orig   holdout Lnet  +2.88%  Lshp +0.713  (utrain  -3.21%/-1.239)
  f_sig    holdout Lnet  -2.33%  Lshp -0.204  (utrain  +4.76%/+0.666)
  f_sum    holdout Lnet  +2.95%  Lshp +0.344  (utrain  +3.36%/+0.536)
  f_lvl    holdout Lnet  -1.22%  Lshp -0.104  (utrain  +3.55%/+0.389,hlL 3,与 train-fit 的 hl5 不同)

判据C三个差值:f_sig-fam30 -16.43pp、f_sum-fam30 -11.16pp、f_lvl-fam30 -15.32pp。判据D:f_sum-f_orig +0.06pp。

异常(已写进结果卡):(1) f_lvl 的 hlL/hlS 在 train-fit 与 utrain-fit 下不同(5→3、0→1),其余 4 条候选不变;
(2) 判据F预先写的"三条结构候选两年都<+5%"在 2024 年全部没发
…(这条日志还有后文,读 journal.md)

## 工单与结果卡(`notes/F109_erm_mag_gap_5m_tsm20/orders/`、`notes/F109_erm_mag_gap_5m_tsm20/results/`)

- R1:工单 有,结果卡 有
- R2:工单 有,结果卡 有

## 配置里的实验计划(`configs/F109_erm_mag_gap_5m_tsm20.yaml`)

- 标题:5 分钟收益的上尾 / 下尾超阈均值比之差的 20 日均值;分母上的 1e-6 把涨跌停封板日变成事件记忆
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base
- **S1_nodes**(8 个变体):两本书各自由哪个节点决定:分母上的 ε(封板日的爆炸)、减法、上侧还是下侧、5 分钟对 1 分钟的尺度?
  a_eps3、a_sum、a_up、a_dn、a_1m、a_q5、a_evt、a_sig
- **S2_family**(4 个变体):规则区间是不是「偏度 / 彩票 / 低价」的另一种写法?多头腿在两侧的水平里还是在两侧的差里?
  b_skew1、b_skew5、b_max20、b_sig60
- **S2_level**(2 个变体):「水平」(上下两侧超阈均值之和)的多头腿是不是就是低价股效应?
  b_lvl、b_lvlq
- **S_final**(5 个变体):留出段:5 条最终候选(排序与判据见 notes/F109_erm_mag_gap_5m_tsm20/10_distilled.md「读留出段之前」)
  f_fam30、f_sig、f_orig、f_sum、f_lvl

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F109_erm_mag_gap_5m_tsm20`)

- `S0_baseline`  10-04 11:54  1 个变体  → `./scripts/study.sh digest F109_erm_mag_gap_5m_tsm20 S0_baseline`
- `S1_lvl`  10-04 14:06  10 个变体  → `./scripts/study.sh digest F109_erm_mag_gap_5m_tsm20 S1_lvl`
- `S_final`  10-04 15:19  5 个变体  → `./scripts/study.sh digest F109_erm_mag_gap_5m_tsm20 S_final`
- `x1_anatomy`(自写脚本的输出)  10-04 12:36  exit 0  → `logs/F109_erm_mag_gap_5m_tsm20_x1_anatomy.log`
- `S1_S2`(自写脚本的输出)  10-04 13:19  exit 97  → `logs/F109_erm_mag_gap_5m_tsm20_S1_S2.log`
- `x2_incremental`(自写脚本的输出)  10-04 14:22  exit 0  → `logs/F109_erm_mag_gap_5m_tsm20_x2_incremental.log`

## 已写的 notes(`notes/F109_erm_mag_gap_5m_tsm20/`)

`02_operators.md`(2K)、`03_decomposition.md`(2K)、`04_grammar.md`(1K)、`05_hypotheses.md`(23K)、`06_baseline.md`(3K)、`07_S1_nodes.md`(7K)、`07_S2_level.md`(5K)、`07_neutralise.md`(4K)、`07x_1_anatomy.md`(10K)、`07x_2_incremental.md`(6K)、`10_distilled.md`(7K)、`journal.md`(18K)、`state.md`(27K)

## 自写的探针与分析脚本(`studies/F109_erm_mag_gap_5m_tsm20/`)

- `x1_anatomy.py`  10-04 12:17  F109 x1: what the tree is really ranking -- the epsilon blow-up anatomy.
- `x2_incremental.py`  10-04 14:19  F109 x2: for a long-only user, does this tree add anything to the known amount-

## 结构化结果(`handoff/F109_erm_mag_gap_5m_tsm20/results/`)

(还没有)
```

**10-04 23:03 · agent 的话**

The holdout段 has been read and R2 has a result card — so this round must be (c) 成文. Let me read the key files.

**10-04 23:03 · Bash** — List notes dir and read distilled candidates file

```bash
cd /Users/wxy/Desktop/Partura && ls -la notes/F109_erm_mag_gap_5m_tsm20/ && echo "=== 10_distilled.md ===" && cat notes/F109_erm_mag_gap_5m_tsm20/10_distilled.md
```

```
total 440
drwxr-xr-x@ 18 wxy  staff    576 Oct  4 15:00 .
drwxr-xr-x@ 19 wxy  staff    608 Oct  4 13:07 ..
-rw-r--r--@  1 wxy  staff   2800 Oct  4 13:01 02_operators.md
-rw-r--r--@  1 wxy  staff   2451 Oct  4 13:01 03_decomposition.md
-rw-r--r--@  1 wxy  staff   1821 Oct  4 13:01 04_grammar.md
-rw-r--r--@  1 wxy  staff  23613 Oct  4 14:51 05_hypotheses.md
-rw-r--r--@  1 wxy  staff   3350 Oct  4 13:01 06_baseline.md
-rw-r--r--@  1 wxy  staff   7820 Oct  4 14:48 07_S1_nodes.md
-rw-r--r--@  1 wxy  staff   5547 Oct  4 14:48 07_S2_level.md
-rw-r--r--@  1 wxy  staff   4542 Oct  4 14:49 07_neutralise.md
-rw-r--r--@  1 wxy  staff  10490 Oct  4 12:46 07x_1_anatomy.md
-rw-r--r--@  1 wxy  staff   6800 Oct  4 14:50 07x_2_incremental.md
-rw-r--r--@  1 wxy  staff   7681 Oct  4 14:52 10_distilled.md
-rw-r--r--@  1 wxy  staff  80562 Oct  4 14:24 R1_propose_draft.txt
-rw-r--r--@  1 wxy  staff  18834 Oct  4 15:29 journal.md
drwxr-xr-x@  4 wxy  staff    128 Oct  4 14:54 orders
drwxr-xr-x@  4 wxy  staff    128 Oct  4 15:28 results
-rw-r--r--@  1 wxy  staff  28628 Oct  4 15:00 state.md
=== 10_distilled.md ===
# 10_distilled —— 最终候选、排序、判据

# 读留出段之前

写于主研第 4 轮(2026-10-04),**在 `study.sh final` 之前**,只凭 train / valid 的证据。
这一节写完之后才下 `orders/R2.md`(kind: final)。留出段整个研究只读一次,读完**不许改候选、不许换推荐**。

## 结论先写死:这条因子判 **分辨**,没有可推荐的提纯 / 升华产物

理由(每条都指到一个实验,详见 `07_S1_nodes.md` / `07_S2_level.md` / `07_neutralise.md` / `07x_2_incremental.md`):
… (47 行略) …
  → **被否定的条件**:任一条 **> `f_fam30` + 3 个点** 且纯多头夏普 **≥ 1.4**。
  那么「它只是活跃度/波动暴露、对纯多头没有增量」这条解读要在 `09_diagnosis.md` 里改写成**未决**,
  并在 `12_next.md` 里建议下一轮专门研究它 —— **但推荐不许改**(推荐是事前写死的,这是留出段的规矩)。
- **判据 D(H11:减法只值几个点)**:预测 `f_sum` 的留出段净超额 ≤ `f_orig` + **8 个点**(train 上这个差是 5.4 点)。
  → **被否定的条件**:`f_sum` − `f_orig` > 15 个点 **且** `f_sum` 本身 ≥ +10%。那 H11 的「修正无交易价值」要改写。
- **判据 E(风格解读)**:预测 `f_lvl` 的留出段净超额 **< +8%**(它 valid 的 +12.0% 我判为 2022–23 风格)。
  → 被否定的条件:`f_lvl` 留出段 ≥ +12% 且夏普 ≥ 1.3 —— 那说明「水平」在两个不同风格段上都给 +12%,
  不能再叫风格,要写成未决。
- **判据 F(逐年,免费附带)**:`final` 带 `--holdout` 时会把所有候选的逐年都算出来(含 2024、2025)。
  预测:`f_fam30` 在 2024、2025 两年都 ≥ +8%,而三条结构候选都 < +5%。两年里有一年反过来,写进 `11_risks.md`。
- **判据 G(复现自检,执行必须先核这一条)**:`final.json` 里 `books`(train 口径)那一组数字必须复现已有的结果 ——
  `f_orig` train −4.6%、`f_sig` +2.3%、`f_sum` +0.8%、`f_lvl` +0.1%、`f_fam30` +12.6%(各 ±0.2 个点)。
  对不上说明表达式没拷对或口径错了,**那就先停下来**,不要解读留出段数字。

---

# 读完留出段之后

(留出段还没读。读完由主研填:逐条写每个判据过了还是被否定;推荐就是上面事前写的第一推荐 `f_fam30`,
若被否定就写被否定。**不许改候选、不许换推荐。**)
```

**10-04 23:03 · agent 的话**

Now let me read the final result card and the current state.

**10-04 23:03 · Bash** — Read final-stage result card R2

```bash
cd /Users/wxy/Desktop/Partura && cat notes/F109_erm_mag_gap_5m_tsm20/results/R2.md
```

```
# 结果卡 R2(kind: final —— 读留出段)

## 做了什么

1. **前置检查(工单未明确要求,但按 playbook 规矩先核)**:
   - `runs/F109_erm_mag_gap_5m_tsm20/ledger.json` 读留出段之前只有 `split: train/valid/utrain` 三种记录,没有
     `split: holdout`——确认留出段确实还没被读过。
   - `notes/F109_erm_mag_gap_5m_tsm20/10_distilled.md` 已有「读留出段之前」一节(候选排序 + 判据 A~G)。
   - `./scripts/study.sh list F109_erm_mag_gap_5m_tsm20` 确认服务器上没有跑过 `S_final` 这个 tag。
   两条前提都满足,按工单往下做。
2. **配置:加阶段 `S_final`**。写了一个一次性小脚本(本次会话的临时目录,不在 Partura 仓库里):用 `yaml.safe_load`
   读 `configs/F109_erm_mag_gap_5m_tsm20.yaml`,按变体 id 取出 `S0_baseline/v_base`、`S1_nodes/a_sig`、`S1_nodes/a_sum`、
   `S2_level/b_lvl` 四个 `expr` 字符串,`f_fam30` 用工单给的字面表达式(并断言它与 `gates.known_stdamt_mean30` 逐字节相等),
   拼成 `f_orig/f_sig/f_sum/f_lvl/f_fam30` 五个变体追加到文件末尾,写盘后**重新读取**整份文件,逐一断言这 5 个新变体的
   `expr` 与各自来源逐字节相等、且其余 25 个旧变体一个字节没变、`S_final` 是新增的唯一一个阶段。断言全部通过。
   `group`/`why` 按工单模板原样抄,5 个变体都带 `final: true`。
   `./scripts/study.sh check F109_erm_mag_gap_5m_tsm20` → **31/31 OK**(26+5,与工单预期一致),其中 4 条打印了
   `note: S_final/f_* is the same tree as .../... (evaluated once)`(`f_fam30` 没被打印同款提示,因为它比对的是 `gates`
   不是别的 `variants`,但它的字符串已经在写盘前由脚本断言与 `gates.known_stdamt_mean30` 相等)。
3. **唯一一次 final**:执行前 `./scripts/study.sh status` 看了一眼,容器 anon 只有 0.5 GiB、没有别的 screen 在跑。
   `./scripts/study.sh final F109_erm_mag_gap_5m_tsm20 S_final S_final`,`wait ... 540`(Bash timeout 600000)**一次就等到完成**,
   不需要第二次 wait、没有排队、没有 exit 97。exit 0,334.0s,peak anon 5.76 GiB。`runs/.../S_final.json` 里 `errors: {}`。
   事后 `runs/.../ledger.json` 多了一条 `split: holdout, n_expressions: 5, stage: S_final` 的记录——留出段读取已正确落账,
   以后的 `list`/前置检查会看到它。
4. **没有做、也不需要做的**:没有跑任何 `exec` 脚本、没有跑除 `S_final` 以外的任何阶段、没有碰 `10_distilled.md`、
   `state.md`、`scripts/`、`partura/`、`handoff/`、`lab/`、`docs/`,也没有碰别的因子的文件。服务器运行只用了 1 次
   (工单给的预算正好是 1 次)。
5. 没有卡住的地方,工单要求的每一步都做完了。

---
… (132 行略) …
   Lnet(+2.88%)仍明显低于预测上限的 +5%。Lnet 和 Sharpe 这两个数字相对判据 A 写的两个预测门槛不是整齐地双双落在
   同一侧——只报数字,这不是我要下的判断。
2. `study.sh check` 的输出里只对 `f_sig`/`f_orig`/`f_sum`/`f_lvl` 四条打印了"is the same tree as ..."提示,`f_fam30`
   没有被提示——这是因为检查器比对的是"本次新增变体 vs 配置里其它 **variants**",而 `f_fam30` 对应的是 `gates`
   字典里的 `known_stdamt_mean30`,不在 `variants` 之列,所以检查器不会主动提示;但这条表达式本身的逐字节相等已经
   在写盘前由脚本断言过(见"做了什么"第 2 条),且 `S_final.json` 里 `f_fam30` 的 train/valid 数字与早前
   `S0_baseline.json`/`S1_lvl.json` 里 `known_stdamt_mean30` 那一行完全吻合,等价于确认了同一棵树。

---

## 原始输出在哪

- `runs/F109_erm_mag_gap_5m_tsm20/S_final.json`(本结果卡里的数字全部从这里直接读出)。
- 文字摘要:`./scripts/study.sh digest F109_erm_mag_gap_5m_tsm20 S_final`(或 `logs/F109_erm_mag_gap_5m_tsm20_S_final.log`,
  9 行,无截断,`[partura exit 0 2026-10-05_06:19:48]`)。
- `runs/F109_erm_mag_gap_5m_tsm20/ledger.json`:现在有 1 条 `split: holdout, stage: S_final, n_expressions: 5` 的记录。
- 配置改动:`configs/F109_erm_mag_gap_5m_tsm20.yaml` 末尾新增的 `S_final` 阶段(5 个变体,其余 26 个旧变体与 4 个阶段
  一个字节没变——写配置用的脚本、改前备份都在本次会话的临时目录
  `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/`
  (`build_s_final.py`、`F109_config_backup_before_R2.yaml`、`dump_s_final.py`),不在 Partura 仓库里,仅供复核方法用)。
```

**10-04 23:03 · Bash** — Read full state file

```bash
cd /Users/wxy/Desktop/Partura && cat notes/F109_erm_mag_gap_5m_tsm20/state.md
```

```
# F109_erm_mag_gap_5m_tsm20 — 研究现状(主研第 4 轮重写,2026-10-04)

> 这一页由**主研**整个覆盖重写(第 4 轮;新工作流下的第 2 轮)。
> **这一轮是第一次拿到引擎口径的结构证据**(`results/R1.md` = tag `S1_lvl` 10 变体 + 自写脚本 `x2_incremental`),
> 14 条假设全部有了结论,**所有需要新实验才能定的问题都定完了** → 这一轮进入「读留出段」。
> 前三轮主研的事实与判断我逐条核对后保留(数字和出处都没变);这一轮**改写了 4 条假设**(H1、H10 后半、H11、H13),
> 其中两条推翻了前面主研写在纸上的事前预测。下一位主研只看得到文件 —— 这页写的是判断,事实都标了出处。

---

## 1. 一句话现状

**结论已经定了:分辨。** 这棵树对纯多头的用户没有可用的多头腿、也不给已知家族加东西;
它的钱全在空头腿(用户做不了,而且一半是「次日一字开盘买不进」撑出来的);
把它的结构一步步修好之后,它收敛成**已实现偏度 / 低波低活跃暴露**的一个更差写法。
**这一轮(第 4 轮)干的事**:读完 `results/R1.md`,裁决全部 14 条假设,写了四份解读 notes
(`07_S1_nodes.md`、`07_S2_level.md`、`07_neutralise.md`、`07x_2_incremental.md`)和
`10_distilled.md` 的「读留出段之前」(5 个候选 + 排序 + 7 条判据),然后下了 `orders/R2.md`(**kind: final**)。
**下一步 = 执行按 `orders/R2.md` 跑唯一一次 `study.sh final`(阶段 `S_final`,5 个候选,tag `S_final`),写 `results/R2.md`。**
再下一轮主研的事:把留出段数字逐条对 `10_distilled.md` 的判据 A~G,填「读完留出段之后」一节,
然后写 `09_diagnosis.md` / `11_risks.md` / `12_next.md` / `08_variants.md`,下 writeup 工单。

---

## 2. 中间结果(已经量到的事实,每条带数字和出处)

口径:「多头腿净超额 / 纯多头夏普」= 选拔口径(`rank_by: long`,方向与 EMA 半衰期**只在 train 上定**,valid 没见过);
「多空夏普」= 用户最早那张表的口径。train / valid 用斜杠分隔。噪声尺度:多头腿净超额 ±3 点、夏普 ±0.3(playbook §4.6)。

### 2.1 原式的两本书(出处:`06_baseline.md`、tag `S0_baseline`)
… (254 行略) …
  但 `S1_lvl` 没排队、343 秒跑完,因为面板全在缓存里。
- **再遇到 exit 97**:看 `[guard] ABORT` 那行的两个 anon 数字 —— 本进程小、容器大就是邻居的事,
  `study.sh status` 看一眼、等几分钟、**原样重跑**(这种重试不算实验预算);两次都这样就停下照实写。
  **对 final 这一次**:崩在写 JSON 之前 = 没拿到任何留出段数字 → 允许原样重跑**一次**,不算第二次读(工单 R2 里写了)。
- **工具语义**(读 `partura/runner.py` 得到的,写错会白跑):`ok` 只含本次 run 阶段里的变体,
  `decay`/`by_year`/`neutralise` 只对 `ok` 做;`corr_ids` 里别的阶段的变体当 ref 载入、**照样进 rank 相关矩阵**(白送);
  带 `--holdout` 时方向与半衰期按 **utrain** 重定一遍(`books_user`),逐年对**所有**候选都会算,
  但 `profile`(分位剖面)只在 train/valid 上算,**留出段没有分位剖面**,别去找。
- **`S1_S2` 这个 tag 作废**(exit 97,没有 JSON):不要 `wait`、不要 `digest`。有用的 tag:
  `S0_baseline`、`S1_lvl`、`x1_anatomy`、`x2_incremental` —— **这四个都已经读完并写进 notes 了**。
- **还没看结果的 tag**:`S_final`(待跑)。
- **写了一半 / 还不存在的文件**:`01_expression.md` **不存在**(notes 从 02 开始),报告阶段要补;
  `08_variants.md`、`09_diagnosis.md`、`11_risks.md`、`12_next.md` 还没写(等留出段读完);
  `10_distilled.md` 的后半节(「读完留出段之后」)是空的,留给下一轮主研。
  已写完的:`02`、`03`、`04`、`05`(含裁决)、`06`、`07_S1_nodes`、`07_S2_level`、`07_neutralise`、`07x_1_anatomy`、`07x_2_incremental`、`10`(前半节)。
- **口径别搞错**:选拔只看多头腿(`rank_by: long`,hlL / Lnet / Lshp)。
  这条因子身上到处是「rIC 高但多头腿差」的例子(`b_lvlq` rIC 全场最高 0.0485/0.0686、多头腿 −4.1%;
  `a_evt` 多空 +3.93 却过不了 dist 门槛)—— **不要被 rIC 和多空夏普带着走**。
- **valid 段(2022–23)是低价/低波风格年**:`ctl_price` 自己 +11.3%、`ctl_turnrate` +8.2%。
  所以任何变体 valid 上的 +8%~+12% **默认先当风格**,要用逐年和中性化去排除,别当成信号。
```

**10-04 23:04 · agent 的话**

Holdout is read and R2 has a result card — so this round is (c) 成文. Let me check the variant inventory and the notes-file contract.

**10-04 23:05 · Bash** — Inventory config variants and gates

```bash
cd /Users/wxy/Desktop/Partura && echo "=== config stages/ids ===" && grep -nE "^\s*(- id:|stage:|id:|group:)" configs/F109_erm_mag_gap_5m_tsm20.yaml | head -80 && echo "=== gates/controls keys ===" && grep -nE "^(gates|controls|known_|ctl_)" -A2 configs/F109_erm_mag_gap_5m_tsm20.yaml | head -40
```

```
=== config stages/ids ===
65:  - id: S0_baseline
70:  - id: S1_nodes
82:  - id: S2_family
90:  - id: S2_level
96:  - id: S_final
=== gates/controls keys ===
30:controls:
31-  ctl_amt:    "log(add(day_sum(Amt), 1))"                                  # 成交额水平
32-  ctl_price:  "log(day_last(Close))"                                       # 价格水平
--
43:gates:
44-  known_amt_max9:    "cross_max(day_sum(Amt), 9)"          # F001:成交额水平 + 极值记忆
45-  known_stdamt_max9: "cross_max(day_std(Amt), 9)"          # F001 的蒸馏结果
```

**10-04 23:05 · Bash** — List variants per stage and playbook sections

```bash
cd /Users/wxy/Desktop/Partura && echo "=== variants per stage ===" && python3 -c "
import yaml,sys
c=yaml.safe_load(open('configs/F109_erm_mag_gap_5m_tsm20.yaml'))
for st in c['stages']:
    ids=[v['id'] for v in st.get('variants',[])]
    print(st['id'], len(ids), ids)
print('controls:', list(c.get('controls',{}).keys()))
print('gates:', list(c.get('gates',{}).keys()))
" && echo "=== playbook section 5 ===" && grep -n "^## " docs/study_playbook.md | head -30
```

```
=== variants per stage ===
S0_baseline 1 ['v_base']
S1_nodes 8 ['a_eps3', 'a_sum', 'a_up', 'a_dn', 'a_1m', 'a_q5', 'a_evt', 'a_sig']
S2_family 4 ['b_skew1', 'b_skew5', 'b_max20', 'b_sig60']
S2_level 2 ['b_lvl', 'b_lvlq']
S_final 5 ['f_fam30', 'f_sig', 'f_orig', 'f_sum', 'f_lvl']
controls: ['ctl_amt', 'ctl_price', 'ctl_ivol', 'ctl_range', 'ctl_rev1', 'ctl_mom20', 'ctl_dvol20']
gates: ['known_amt_max9', 'known_stdamt_max9', 'known_ivol_max9', 'known_stdamt_mean30']
=== playbook section 5 ===
10:## 0. 目标:提纯、分辨、升华
40:## 1. 口径(和用户的 `pick_single_factors.py` 一致,已复现过用户表的 15 行)
64:## 2. 工具:全部通过 `scripts/study.sh`(在 `~/Desktop/Partura` 下跑)
127:## 3. 配置文件 `configs/<fid>.yaml`
167:## 4. 硬规矩
186:## 5. 要交的东西
212:## 6. 第一组研究里,审查反复抓到的问题(开工前读;不要等审查来抓)
238:## 7. 研究日志与交接(用户 2026-10-04 要求:研究必须随时能被别人接上)
```

**10-04 23:05 · Bash** — Read playbook deliverables section

```bash
cd /Users/wxy/Desktop/Partura && sed -n '186,212p' docs/study_playbook.md
```

```
## 5. 要交的东西

`notes/<fid>/` 下的手写段落(中文,英文术语保留;写法看 F001 和第一组的 notes):

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
```

**10-04 23:06 · agent 的话**

Let me cross-check the load-bearing holdout numbers directly before writing the judgments.

**10-04 23:06 · Bash** — Verify holdout digest numbers

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh digest F109_erm_mag_gap_5m_tsm20 S_final 2>&1 | head -60
```

```
===== F109_erm_mag_gap_5m_tsm20  [S_final.json]  1942d x 5220s  splits ['train', 'valid', 'utrain', 'holdout', 'full']  fit=train  device=cuda  334.0s  peak anon 5.76G =====

决策口径(方向/半衰期在 train 上定; valid 没见过)—— 按多头腿选:
variant              sgn | hlL   Lnet tr   Lnet va  Lshp tr  Lshp va  Lgross tr  Lgross va   LTO | hlS   LS tr   LS va  short tr
f_fam30                - |   0    +12.6%    +22.3%    +1.78    +3.46     +15.2%     +24.4%  3.4% |   0   +1.87   +3.70    +21.1%
f_sig                  - |  20     +2.3%    +10.9%    +0.31    +1.59      +4.3%     +12.9%  2.7% |   1   +2.17   +3.32    +40.4%
f_orig                 - |  20     -4.6%     +0.2%    -1.76    +0.09      -3.5%      +1.2%  1.4% |   1   +2.55   +3.46    +34.4%
f_sum                  - |  20     +0.8%     +9.6%    +0.13    +1.57      +2.1%     +10.7%  1.6% |   0   +2.50   +3.42    +39.9%
f_lvl                  - |   5     +0.1%    +12.0%    +0.02    +1.29      +1.9%     +13.5%  2.3% |   0   +0.98   +2.46    +26.1%

variant                rIC tr   rIC va  rICtraded tr  rICtraded va    cov   dist
f_fam30               +0.0343  +0.0565       +0.0343       +0.0565   1.00   1.00
f_sig                 +0.0458  +0.0574       +0.0359       +0.0514   1.00   1.00
f_orig                +0.0306  +0.0298       +0.0196       +0.0164   1.00   1.00
f_sum                 +0.0341  +0.0339       +0.0276       +0.0208   1.00   1.00
f_lvl                 +0.0296  +0.0554       +0.0240       +0.0499   1.00   1.00
  (rIC = 原始日频面板的 rank IC; rICtraded = 平滑后实际交易信号的; cov ≥ 0.95、dist ≥ 0.5 是用户的两道门槛)

固定半衰期下的 train 表现(结构之间先在同一半衰期下比;Lnet = 多头腿净超额, Lshp = 纯多头夏普):
variant                hl0 Lnet   Lshp  LTO   hl2 Lnet   Lshp  LTO   hl5 Lnet   Lshp  LTO  hl10 Lnet   Lshp  LTO  hl20 Lnet   Lshp  LTO
f_fam30                  +12.6%  +1.78   3%     +11.6%  +1.65   3%     +11.0%  +1.57   2%      +9.8%  +1.40   2%      +8.4%  +1.21   1%
f_sig                    -10.4%  -1.76  18%      -3.6%  -0.58   8%      -1.8%  -0.28   6%      +0.2%  +0.04   4%      +2.3%  +0.31   3%
f_orig                   -13.5%  -3.48  17%      -8.5%  -2.43   7%      -7.4%  -2.22   4%      -6.0%  -1.96   3%      -4.6%  -1.76   1%
f_sum                     -5.8%  -0.81   8%      -3.0%  -0.43   4%      -1.2%  -0.17   3%      -0.3%  -0.05   2%      +0.8%  +0.13   2%
f_lvl                     -1.5%  -0.17   7%      +0.1%  +0.01   3%      +0.1%  +0.02   2%      +0.0%  +0.00   2%      -0.6%  -0.07   1%

与用户表同口径(方向/半衰期在 utrain = 用户训练段上定; ho = holdout = 用户测试段):
variant              sgn | hlL  Lnet utr   Lnet ho Lshp utr  Lshp ho Lgross utr  Lgross ho   LTO | hlS  LS utr   LS ho short utr
f_fam30                - |   0    +15.4%    +14.1%    +2.22    +1.51     +17.8%     +16.2%  3.2% |   0   +2.33   +1.94    +24.7%
f_sig                  - |  20     +4.8%     -2.3%    +0.67    -0.20      +6.8%      -0.5%  2.7% |   1   +2.47   +1.96    +41.5%
f_orig                 - |  20     -3.2%     +2.9%    -1.24    +0.71      -2.2%      +4.0%  1.3% |   1   +2.77   +2.28    +32.7%
f_sum                  - |  20     +3.4%     +2.9%    +0.54    +0.34      +4.5%      +4.0%  1.5% |   0   +2.71   +1.97    +37.1%
f_lvl                  - |   3     +3.5%     -1.2%    +0.39    -0.10      +5.6%      +0.6%  2.7% |   1   +1.39   +0.89    +24.9%
条件 IC v_base|ctl_cap(分桶变量从低到高): Q1 +0.0234  Q2 +0.0215  Q3 +0.0237  Q4 +0.0213  Q5 +0.0127
条件 IC v_base|ctl_amt(分桶变量从低到高): Q1 +0.0056  Q2 +0.0082  Q3 +0.0170  Q4 +0.0265  Q5 +0.0398
条件 IC a_sig|known_stdamt_mean30(分桶变量从低到高): Q1 +0.0171  Q2 +0.0149  Q3 +0.0232  Q4 +0.0332  Q5 +0.0428
条件 IC a_sum|known_stdamt_mean30(分桶变量从低到高): Q1 +0.0115  Q2 +0.0147  Q3 +0.0251  Q4 +0.0331  Q5 +0.0415
条件 IC b_lvl|ctl_price(分桶变量从低到高): Q1 +0.0246  Q2 +0.0283  Q3 +0.0294  Q4 +0.0263  Q5 +0.0065

与 v_base 的日截面 rank 相关(fit 段, 实际交易信号; |.|>=0.95 = 同一因子族): f_orig +1.00  a_eps3 +0.75  a_1m +0.72  a_up +0.72  a_q5 +0.68  a_sum +0.56  f_sum +0.56  b_skew5 +0.53  a_sig +0.50  f_sig +0.50  b_sig60 +0.46  b_lvlq +0.44  a_evt +0.42  b_skew1 +0.39  ctl_cap +0.26  ctl_turnrate -0.23  b_max20 +0.20  known_ivol_max9 -0.19  ctl_dvol20 -0.19  ctl_price +0.15  a_dn +0.15  b_lvl +0.12  f_lvl +0.12  ctl_ivol -0.12  f_fam30 +0.03  known_stdamt_mean30 -0.03  known_stdamt_max9 -0.03  ctl_amt +0.02  ctl_mom20 -0.01  ctl_rev1 +0.01  known_amt_max9 +0.00
逐年 f_fam30: 2018 Lnet +17.3% LS +3.01  2019 Lnet +10.2% LS +1.84  2020 Lnet +6.6% LS +0.66  2021 Lnet +16.0% LS +2.18  2022 Lnet +24.6% LS +4.22  2023 Lnet +21.2% LS +3.75  2024 Lnet +9.2% LS +1.45  2025 Lnet +14.3% LS +1.60
逐年 f_sig: 2018 Lnet +11.1% LS +2.29  2019 Lnet +0.1% LS +1.76  2020 Lnet -1.0% LS +1.48  2021 Lnet -1.6% LS +1.89  2022 Lnet +13.1% LS +3.24  2023 Lnet +2.2% LS +1.75  2024 Lnet +8.8% LS +1.47  2025 Lnet -12.7% LS +0.29
逐年 f_orig: 2018 Lnet -6.9% LS +1.16  2019 Lnet -3.7% LS +1.70  2020 Lnet -5.9% LS +1.79  2021 Lnet -2.4% LS +1.59  2022 Lnet +0.4% LS +1.79  2023 Lnet -1.4% LS +2.48  2024 Lnet +4.7% LS +2.77  2025 Lnet +3.3% LS +2.32
逐年 f_sum: 2018 Lnet -0.0% LS +1.26  2019 Lnet +0.4% LS +1.38  2020 Lnet +2.1% LS +1.87  2021 Lnet +0.5% LS +1.19  2022 Lnet +9.3% LS +1.80  2023 Lnet +4.8% LS +2.05  2024 Lnet +10.0% LS +1.58  2025 Lnet -1.9% LS +0.79
逐年 f_lvl: 2018 Lnet +5.8% LS +1.26  2019 Lnet -4.8% LS +1.05  2020 Lnet -6.6% LS -0.35  2021 Lnet +5.7% LS +1.56  2022 Lnet +15.5% LS +2.13  2023 Lnet +1.4% LS +2.02  2024 Lnet +11.1% LS +1.71  2025 Lnet -12.0% LS -0.33
```

**10-04 23:07 · agent 的话**

The digest's long-short columns disagree with result card R2's table 3. Let me check the raw JSON — this matters for attribution.

**10-04 23:07 · Bash** — Inspect books_user structure in final JSON

```bash
cd /Users/wxy/Desktop/Partura && python3 -c "
import json
d=json.load(open('runs/F109_erm_mag_gap_5m_tsm20/S_final.json'))
bu=d.get('books_user')
print('type', type(bu))
if isinstance(bu,dict): print('keys', list(bu.keys())[:20])
if isinstance(bu,list): print('n', len(bu)); print(json.dumps(bu[0], ensure_ascii=False)[:2000])
"
```

```
type <class 'NoneType'>
```

**10-04 23:07 · Bash** — Show top-level keys of final JSON

```bash
cd /Users/wxy/Desktop/Partura && python3 -c "
import json
d=json.load(open('runs/F109_erm_mag_gap_5m_tsm20/S_final.json'))
print('top keys:', list(d.keys()))
for k,v in d.items():
    if isinstance(v,dict): print(k,'dict keys:',list(v.keys())[:12])
    elif isinstance(v,list): print(k,'list len',len(v))
"
```

```
top keys: ['factor_id', 'config', 'stages', 'provenance', 'view', 'label', 'cost_per_side', 'top_frac', 'fit_split', 'user_split', 'rank_by', 'halflives', 'device', 'splits_used', 'split_dates', 'results', 'errors', 'engine_timings', 'diagnostics', 'seconds', 'peak_anon_gb']
stages list len 1
provenance dict keys: ['alphacube_root', 'alphacube_commit', 'alphacube_dirty', 'partura_root', 'partura_commit', 'partura_code_sha', 'store', 'python', 'torch', 'numpy', 'host']
view dict keys: ['days', 'symbols', 'first', 'last', 'warmup_rows']
label dict keys: ['kind', 'horizon', 'buyable']
halflives list len 7
splits_used list len 5
split_dates dict keys: ['train', 'valid', 'utrain', 'holdout', 'full']
results dict keys: ['f_fam30', 'f_sig', 'f_orig', 'f_sum', 'f_lvl']
errors dict keys: []
engine_timings list len 0
diagnostics dict keys: ['by_year', 'by_year_scope', 'conditional', 'rank_corr_train', 'rank_corr_on']
```

**10-04 23:07 · Bash** — Inspect one result entry structure

```bash
cd /Users/wxy/Desktop/Partura && python3 -c "
import json
d=json.load(open('runs/F109_erm_mag_gap_5m_tsm20/S_final.json'))
r=d['results']['f_orig']
print('keys:', list(r.keys()))
for k,v in r.items():
    if isinstance(v,dict): print(' ',k,'->',list(v.keys())[:14])
"
```

```
keys: ['expr', 'stage', 'why', 'group', 'sign', 'splits', 'distinct', 'books', 'sign_user', 'ic_user', 'ic_holdout', 'books_user']
  splits -> ['train', 'valid']
  books -> ['hl_ls', 'hl_long', 'hl_used', 'rank_by', 'sweep', 'splits', 'by_rank']
  ic_user -> ['sign', 'ic', 'icir', 'ic_t', 'rank_ic', 'rank_icir', 'rank_ic_t', 'ic_pos', 'coverage', 'coverage_labelled', 'n_days']
  ic_holdout -> ['sign', 'ic', 'icir', 'ic_t', 'rank_ic', 'rank_icir', 'rank_ic_t', 'ic_pos', 'coverage', 'coverage_labelled', 'n_days']
  books_user -> ['hl_ls', 'hl_long', 'hl_used', 'rank_by', 'sweep', 'splits', 'by_rank']
```

**10-04 23:07 · Bash** — Inspect books_user splits fields

```bash
cd /Users/wxy/Desktop/Partura && python3 -c "
import json
d=json.load(open('runs/F109_erm_mag_gap_5m_tsm20/S_final.json'))
print('%-9s %4s %4s | %-8s %-8s %-8s %-8s | %-8s %-8s %-8s %-8s'%('id','hlL','hlS','LSutr','LSho','shGutr','shGho','Lnetutr','Lnetho','Lshputr','Lshpho'))
for k,r in d['results'].items():
    bu=r['books_user']; sp=bu['splits']
    hlL=bu['hl_long']; hlS=bu['hl_ls']
    def g(split,f):
        return sp[split].get(f)
    row=[k,hlL,hlS]
    for split in ['utrain','holdout']:
        pass
    print(k,'hlL',hlL,'hlS',hlS,'| split keys:',list(sp.keys()))
    print('   utrain fields:',{kk:vv for kk,vv in sp['utrain'].items() if isinstance(vv,(int,float))})
    break
"
```

```
id         hlL  hlS | LSutr    LSho     shGutr   shGho    | Lnetutr  Lnetho   Lshputr  Lshpho  
f_fam30 hlL 0.0 hlS 0.0 | split keys: ['utrain', 'holdout']
   utrain fields: {'ls_sharpe': 2.334315983395936, 'ls_ann': 0.19198799201901864, 'ls_mdd': -0.1194923256147542, 'ls_gross_sharpe': 2.5869029636035528, 'ls_turnover': 0.027412420556852078, 'long_sharpe': 2.2241654018294756, 'long_ann': 0.1540311223997637, 'long_mdd': -0.09169651471329929, 'long_gross_ann': 0.17810987992473706, 'long_turnover': 0.031850208366366844, 'short_gross_ann': 0.2473136839952605, 'long_share': 0.4186648202642373, 'n_days': 1359}
```

**10-04 23:07 · Bash** — Dump authoritative long-short numbers from final JSON

```bash
cd /Users/wxy/Desktop/Partura && python3 -c "
import json
d=json.load(open('runs/F109_erm_mag_gap_5m_tsm20/S_final.json'))
print('%-8s %4s %4s | %8s %8s | %8s %8s | %8s %8s | %8s %8s'%('id','hlL','hlS','LS_utr','LS_ho','shG_utr','shG_ho','Lnet_utr','Lnet_ho','Lshp_utr','Lshp_ho'))
for k,r in d['results'].items():
    bu=r['books_user']; sp=bu['splits']; u=sp['utrain']; h=sp['holdout']
    print('%-8s %4.0f %4.0f | %8.3f %8.3f | %7.2f%% %7.2f%% | %7.2f%% %7.2f%% | %8.3f %8.3f'%(
        k,bu['hl_long'],bu['hl_ls'],u['ls_sharpe'],h['ls_sharpe'],100*u['short_gross_ann'],100*h['short_gross_ann'],
        100*u['long_ann'],100*h['long_ann'],u['long_sharpe'],h['long_sharpe']))
print()
print('--- train-fit books for comparison ---')
for k,r in d['results'].items():
    b=r['books']; sp=b['splits']
    tr=sp['train']; va=sp['valid']
    print('%-8s hlL %2.0f hlS %2.0f | LS tr %6.3f va %6.3f | shG tr %6.2f%% | Lnet tr %6.2f%% va %6.2f%%'%(
        k,b['hl_long'],b['hl_ls'],tr['ls_sharpe'],va['ls_sharpe'],100*tr['short_gross_ann'],100*tr['long_ann'],100*va['long_ann']))
"
```

```
id        hlL  hlS |   LS_utr    LS_ho |  shG_utr   shG_ho | Lnet_utr  Lnet_ho | Lshp_utr  Lshp_ho
f_fam30     0    0 |    2.334    1.942 |   24.73%   24.93% |   15.40%   14.10% |    2.224    1.509
f_sig      20    1 |    2.134    0.892 |   26.69%   21.81% |    4.76%   -2.33% |    0.666   -0.204
f_orig     20    1 |    1.784    2.261 |   16.92%   16.00% |   -3.21%    2.88% |   -1.239    0.713
f_sum      20    0 |    1.654    1.120 |   17.78%   16.61% |    3.36%    2.95% |    0.536    0.344
f_lvl       3    1 |    1.238    0.720 |   20.49%   17.84% |    3.55%   -1.22% |    0.389   -0.104

--- train-fit books for comparison ---
f_fam30  hlL  0 hlS  0 | LS tr  1.873 va  3.702 | shG tr  21.14% | Lnet tr  12.62% va  22.33%
f_sig    hlL 20 hlS  1 | LS tr  1.847 va  2.975 | shG tr  26.13% | Lnet tr   2.27% va  10.94%
f_orig   hlL 20 hlS  1 | LS tr  1.554 va  2.480 | shG tr  17.32% | Lnet tr  -4.62% va   0.23%
f_sum    hlL 20 hlS  0 | LS tr  1.438 va  2.296 | shG tr  18.52% | Lnet tr   0.84% va   9.63%
f_lvl    hlL  5 hlS  0 | LS tr  0.819 va  2.212 | shG tr  16.64% | Lnet tr   0.14% va  11.99%
```

**10-04 23:08 · agent 的话**

One more check — the digest and the JSON disagree on the long-short columns. Let me settle which halflife each is on.

**10-04 23:08 · Bash** — Check halflife sweep for the original factor

```bash
cd /Users/wxy/Desktop/Partura && python3 -c "
import json
d=json.load(open('runs/F109_erm_mag_gap_5m_tsm20/S_final.json'))
r=d['results']['f_orig']; bu=r['books_user']
print('hl_long',bu['hl_long'],'hl_ls',bu['hl_ls'],'hl_used',bu['hl_used'])
sw=bu['sweep']
print('sweep type',type(sw))
if isinstance(sw,list):
    for row in sw:
        if isinstance(row,dict):
            print({k:(round(v,4) if isinstance(v,float) else v) for k,v in row.items() if k in ('hl','split','ls_sharpe','long_ann','long_sharpe','short_gross_ann')})
elif isinstance(sw,dict):
    print(list(sw.keys())[:10])
" 2>&1 | head -30
```

```
hl_long 20.0 hl_ls 1.0 hl_used 20.0
sweep type <class 'list'>
{'ls_sharpe': 2.2099, 'long_sharpe': -3.196, 'long_ann': -0.1212}
{'ls_sharpe': 2.7663, 'long_sharpe': -2.0951, 'long_ann': -0.0757}
{'ls_sharpe': 2.6816, 'long_sharpe': -1.7754, 'long_ann': -0.0619}
{'ls_sharpe': 2.5858, 'long_sharpe': -1.5315, 'long_ann': -0.0523}
{'ls_sharpe': 2.3926, 'long_sharpe': -1.5993, 'long_ann': -0.0522}
{'ls_sharpe': 1.9436, 'long_sharpe': -1.4651, 'long_ann': -0.0442}
{'ls_sharpe': 1.7845, 'long_sharpe': -1.2385, 'long_ann': -0.0321}
```

**10-04 23:08 · Bash** — Check the separate long-short book inside by_rank

```bash
cd /Users/wxy/Desktop/Partura && python3 -c "
import json
d=json.load(open('runs/F109_erm_mag_gap_5m_tsm20/S_final.json'))
print('%-8s | %-28s | %-28s'%('id','by_rank[ls] utrain/holdout LS','short_gross utr/ho (ls book)'))
for k,r in d['results'].items():
    bu=r['books_user']; br=bu.get('by_rank')
    if isinstance(br,dict) and 'ls' in br:
        s=br['ls']['splits']
        print('%-8s | hl=%-3.0f  utr %6.3f  ho %6.3f | %6.2f%%  %6.2f%%'%(k, br['ls'].get('hl_used',-1), s['utrain']['ls_sharpe'], s['holdout']['ls_sharpe'], 100*s['utrain']['short_gross_ann'], 100*s['holdout']['short_gross_ann']))
    else:
        print(k,'by_rank keys:', list(br.keys()) if isinstance(br,dict) else type(br))
"
```

```
id       | by_rank[ls] utrain/holdout LS | short_gross utr/ho (ls book)
f_fam30  | hl=-1   utr  2.334  ho  1.942 |  24.73%   24.93%
f_sig    | hl=-1   utr  2.475  ho  1.957 |  41.47%   43.42%
f_orig   | hl=-1   utr  2.766  ho  2.276 |  32.71%   32.86%
f_sum    | hl=-1   utr  2.712  ho  1.974 |  37.09%   37.27%
f_lvl    | hl=-1   utr  1.390  ho  0.891 |  24.90%   22.47%
```

**10-04 23:09 · agent 的话**

Everything is now airtight. The authoritative long-short book lives in `by_rank['ls']` — and result card R2's table 3 mislabeled it. Let me write the holdout adjudication first.

**10-04 23:10 · 改文件** `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/10_distilled.md`

```
- # 读完留出段之后

(留出段还没读。读完由主研填:逐条写每个判据过了还是被否定;推荐就是上面事前写的第一推荐 `f_fam30`,
若被否定就写被否定。**不许改候选、不许换推荐。**)
+ # 读完留出段之后

写于主研第 5 轮(2026-10-04),在 `results/R2.md`(tag `S_final`,exit 0,334.0s,5 个候选全部成功)之后。
**候选没改、推荐没换**:下面只回答「每条判据过了还是被否定」。

口径:全部是 `books_user`(方向与半衰期在 **utrain** 上定),`holdout` = 2023-08-08~2025-12-31,扣 15bp。
噪声尺度:多头腿净超额 ±3 点、纯多头夏普 ±0.3。

## 留出段主表(多头口径,出处 `results/R2.md` 第 2 节 / `runs/.../S_final.json`)

| 候选 | hlL | Lnet utrain | **Lnet holdout** | Lshp utrain | **Lshp holdout** | LTO ho | rIC holdout |
|---|---|---|---|---|---|---|---|
| `f_fam30` | 0 | +15.40% | **+14.10%** | +2.224 | **+1.509** | 2.83% | +0.0503 |
| `f_sum` | 20 | +3.36% | **+2.95%** | +0.536 | **+0.344** | 1.42% | +0.0289 |
… (70 行略) …
   **低于事前写死的 +2 点门槛**,按预注册不升级,追法转入 `12_next.md`。
4. **它本来就是别人的影子**:`a_sig` ~ 5 分钟已实现偏度 20 日均值 rank 相关 **+0.85**、~ 自己的 60 日版 +0.92(H12)。
5. **rIC 高 ≠ 能赚**:留出段 rIC 最高的是 `f_sig` **+0.0579**(高于家族的 +0.0503),它的多头腿是 **−2.33% / −0.204**。
   这是本研究留给下一条因子的最贵的一句话。
```

10-04 23:10 · 读 `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/10_distilled.md`

10-04 23:10 · 读 `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/10_distilled.md`

**10-04 23:10 · 改文件** `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/10_distilled.md`

```
- # 读完留出段之后

(留出段还没读。读完由主研填:逐条写每个判据过了还是被否定;推荐就是上面事前写的第一推荐 `f_fam30`,
若被否定就写被否定。**不许改候选、不许换推荐。**)
+ # 读完留出段之后

写于主研第 5 轮(2026-10-04),在 `results/R2.md`(tag `S_final`,exit 0,334.0s,5 个候选全部成功)之后。
**候选没改、推荐没换**:下面只回答「每条判据过了还是被否定」。

口径:全部是 `books_user`(方向与半衰期在 **utrain** 上定),`holdout` = 2023-08-08~2025-12-31,扣 15bp。
噪声尺度:多头腿净超额 ±3 点、纯多头夏普 ±0.3。

## 留出段主表(多头口径,出处 `results/R2.md` 第 2 节 / `runs/.../S_final.json`)

| 候选 | hlL | Lnet utrain | **Lnet holdout** | Lshp utrain | **Lshp holdout** | LTO ho | rIC holdout |
|---|---|---|---|---|---|---|---|
| `f_fam30` | 0 | +15.40% | **+14.10%** | +2.224 | **+1.509** | 2.83% | +0.0503 |
| `f_sum` | 20 | +3.36% | **+2.95%** | +0.536 | **+0.344** | 1.42% | +0.0289 |
… (70 行略) …
   **低于事前写死的 +2 点门槛**,按预注册不升级,追法转入 `12_next.md`。
4. **它本来就是别人的影子**:`a_sig` ~ 5 分钟已实现偏度 20 日均值 rank 相关 **+0.85**、~ 自己的 60 日版 +0.92(H12)。
5. **rIC 高 ≠ 能赚**:留出段 rIC 最高的是 `f_sig` **+0.0579**(高于家族的 +0.0503),它的多头腿是 **−2.33% / −0.204**。
   这是本研究留给下一条因子的最贵的一句话。
```

**10-04 23:10 · agent 的话**

Now the mechanism diagnosis.

**10-04 23:11 · 写文件** `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/09_diagnosis.md`(4685 字符)

**10-04 23:12 · 写文件** `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/11_risks.md`(3467 字符)

**10-04 23:13 · 写文件** `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/12_next.md`(3255 字符)

**10-04 23:13 · agent 的话**

Now the variants-reading guide, which also carries the mislabeling warning.

**10-04 23:14 · 写文件** `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/08_variants.md`(5121 字符)

**10-04 23:14 · agent 的话**

Now the writeup order for 执行.

**10-04 23:15 · 写文件** `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/orders/R3.md`(6509 字符)

**10-04 23:16 · agent 的话**

Now the state file — rewritten compactly, within the 150-line / 10 KB budget.

**10-04 23:17 · 写文件** `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/state.md`(6441 字符)

10-04 23:17 · 读 `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/state.md`

**10-04 23:18 · 写文件** `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/state.md`(6464 字符)

**10-04 23:18 · Bash** — Check state.md size against the budget

```bash
cd /Users/wxy/Desktop/Partura && wc -l -c notes/F109_erm_mag_gap_5m_tsm20/state.md && ls -la notes/F109_erm_mag_gap_5m_tsm20/ | grep -E "0[89]_|1[012]_|state"
```

```
     119   10853 notes/F109_erm_mag_gap_5m_tsm20/state.md
-rw-r--r--@  1 wxy  staff   7893 Oct  4 23:14 08_variants.md
-rw-r--r--@  1 wxy  staff   8077 Oct  4 23:11 09_diagnosis.md
-rw-r--r--@  1 wxy  staff  14745 Oct  4 23:10 10_distilled.md
-rw-r--r--@  1 wxy  staff   6630 Oct  4 23:12 11_risks.md
-rw-r--r--@  1 wxy  staff   5968 Oct  4 23:13 12_next.md
-rw-r--r--@  1 wxy  staff  10853 Oct  4 23:18 state.md
```

**10-04 23:18 · agent 的话**

119 lines but 10853 bytes — just over the 10 KB cap. Let me trim.

**10-04 23:19 · 改文件** `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/state.md`

```
- - **树的语义**(`02_operators.md`/`03_decomposition.md`/`07x_1_anatomy.md`;numpy 重构与引擎面板 rank 相关 1.0000):
  `Ret` 首根恰为 0 ⇒ 封板日分位数**精确为 0** ⇒ 分母的 1e-6 把那天炸成 10³~10⁵,一天占 20 日窗 Σ|gap_d| 的 **99.9%**。
  它实质是**「最近 20 天有没有封板」的带符号记忆**;封板后次日年化超额 −35%~−56%。
+ - **树的语义**(`02`/`03_decomposition.md`/`07x_1_anatomy.md`;numpy 重构与引擎面板 rank 相关 1.0000):
  `Ret` 首根恰为 0 ⇒ 封板日分位数**精确为 0** ⇒ 分母的 1e-6 把那天炸成 10³~10⁵,一天占 20 日窗 Σ|gap_d| 的 **99.9%**。
  实质是**「最近 20 天有没有封板」的带符号记忆**;封板后次日年化超额 −35%~−56%。
```

**10-04 23:19 · 改文件** `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/state.md`

```
- **14 条全部已定,本轮没有新增、没有改判。** 摘要:
H1 改写后成立(ε 只管幅度不管排序)| H2 成立(空头腿 = 封板记忆)| H3 成立(一半是买不进,2.55→0.35)|
H4 成立并扩展到多头腿 | H5 已并入 H11 | H6 前半成立后半否定 | H7 成立且反向加强(错配是必需品)|
H8 成立(窗口不是杠杆)| **H9 坐实(对纯多头无可用多头腿、不给家族加东西)—— 留出段再次确认** |
H10 前半成立后半改写 | **H11 机制成立、修正无交易价值 —— 判据 D 使它从单段升级为两段证实** |
H12 成立(0.85/0.92)| H13 字面否定、改写后成立(是低波低活跃,不是低价)| H14 成立但低于事前门槛。

本轮新增的机制分级(`09_diagnosis.md`):**已确立 13 条**;**合理但未坐实 3 条**(家族剔事件票 +1 点 /
`ctl_cap` 残差 / 2024 风格年的机制);**未决 3 条**(原式多头腿 2023-08 后的符号翻转 / 买不进假象的分解 / 同族其它手写因子)。
+ **14 条全部已定,本轮没有新增、没有改判。** 摘要:
H1 改写后成立(ε 只管幅度不管排序)| H2 成立(空头腿 = 封板记忆)| H3 成立(一半是买不进,2.55→0.35)|
H4 成立并扩展到多头腿 | H5 并入 H11 | H6 前半成立后半否定 | H7 成立且反向加强(错配是必需品)|
H8 成立 | **H9 坐实(对纯多头无可用多头腿、不给家族加东西)—— 留出段再次确认** | H10 前半成立后半改写 |
**H11 机制成立、修正无交易价值 —— 判据 D 使它从单段升级为两段证实** | H12 成立(0.85/0.92)|
H13 字面否定、改写后成立(是低波低活跃不是低价)| H14 成立但低于事前门槛。

本轮新增的机制分级(`09_diagnosis.md`):**已确立 13 条**;**合理但未坐实 3 条**(家族剔事件票 +1 点 /
`ctl_cap` 残差 / 2024 风格年);**未决 3 条**(原式多头腿 2023-08 后的符号翻转 / 买不进假象的分解 / 同族其它因子)。
```

**10-04 23:19 · 改文件** `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/state.md`

```
- - **选拔只看多头腿**。这条因子身上到处是「rIC 高但多头腿差」:留出段 rIC 最高的 `f_sig` +0.0579、多头腿 −2.33%;
  `b_lvlq` rIC 全场最高 0.0485/0.0686、多头腿 −4.1%;`a_evt` 多空 +3.93 却因 dist 0.0153 过不了门槛。
- **valid(2022–23)是低价/低波风格年**(`ctl_price` 自己 +11.3%):任何变体 valid 上的 +8%~+12% 默认先当风格。
- **`f_lvl` 的 hlL 在 train-fit 是 5、utrain-fit 是 3**(唯一一条):逐年表与判据 G 表里的它不是同一个口径。
+ - **选拔只看多头腿**。这条因子身上到处是「rIC 高但多头腿差」:留出段 rIC 最高的 `f_sig` +0.0579、多头腿 −2.33%;
  `b_lvlq` rIC 全场最高 0.0485/0.0686、多头腿 −4.1%;`a_evt` 多空 +3.93 却因 dist 0.0153 过不了门槛。
- **valid(2022–23)是低价/低波风格年**(`ctl_price` 自己 +11.3%):变体 valid 上的 +8%~+12% 默认先当风格。
- **`f_lvl` 的 hlL 在 train-fit 是 5、utrain-fit 是 3**(唯一一条):逐年表与判据 G 表里的它口径不同。
```

**10-04 23:19 · Bash** — Recheck state file size

```bash
cd /Users/wxy/Desktop/Partura && wc -l -c notes/F109_erm_mag_gap_5m_tsm20/state.md
```

```
     119   10784 notes/F109_erm_mag_gap_5m_tsm20/state.md
```

**10-04 23:19 · 改文件** `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/state.md`

```
- 4. `S1_S2`(14 变体)exit 97:是**邻居**把容器撑到 37.2 GiB、守卫让路(本进程只 3.9 GiB),且 14 个面板已进共享缓存。
   于是不拆小,把 `b_lvl`/`b_lvlq` 挪进 `S2_level`,一次 run 跑 10 变体 → `S1_lvl` exit 0、343.5s、全缓存命中。
+ 4. `S1_S2`(14 变体)exit 97 = **邻居**撑爆容器、守卫让路,面板已进缓存(全文在 `08_variants.md` §1)。
   于是不拆小,把 `b_lvl`/`b_lvlq` 挪进 `S2_level`,一次 run 跑 10 变体 → `S1_lvl` exit 0、343.5s、全缓存命中。
```

**10-04 23:19 · 改文件** `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/state.md`

```
- - **train/valid 的结构证据**(tag `S1_lvl`、`S0_baseline`;解读在 `07_S1_nodes.md`/`07_S2_level.md`/`07_neutralise.md`):
  固定 hl20 下 train 多头腿最好的是 `a_sig` **+2.3%**(夏普 0.31),家族 **+12.6%**(1.78),原式 −4.6%;
  hl 0 下 `a_sig` 是 **−10.4%** —— 它的结构优势只有 3 点,不是自选口径看起来的 7 点。
  ε 只管幅度不管排序(`a_eps3` 空头腿比原式还高);尺度错配是必需品(`a_1m`/`a_q5` rIC 砍一半);
  多头端 Q9→Q10 翻转**十个变体没有一个修掉**;`a_sig`~5 分钟已实现偏度 20 日均值 rank 相关 **+0.85**;
  `a_sig` 毛多头腿 +4.3% → 对 `ctl_amt` 残差 −0.5% / `ctl_dvol20` −0.1%。
+ - **train/valid 的结构证据**(tag `S1_lvl`、`S0_baseline`;解读在 `07_S1_nodes.md`/`07_S2_level.md`/`07_neutralise.md`):
  固定 hl20 下 train 多头腿最好的是 `a_sig` **+2.3%**(夏普 0.31),家族 **+12.6%**(1.78),原式 −4.6%;
  hl 0 下 `a_sig` 是 **−10.4%** —— 结构优势只有 3 点,不是自选口径看起来的 7 点。
  ε 只管幅度不管排序;尺度错配是必需品(`a_1m`/`a_q5` rIC 砍一半);Q9→Q10 翻转**十个变体没有一个修掉**;
  `a_sig`~5 分钟已实现偏度 20 日均值 rank 相关 **+0.85**;毛多头腿 +4.3% → 对 `ctl_amt` 残差 −0.5% / `ctl_dvol20` −0.1%。
```

**10-04 23:19 · Bash** — Recheck state file size

```bash
cd /Users/wxy/Desktop/Partura && wc -l -c notes/F109_erm_mag_gap_5m_tsm20/state.md
```

```
     118   10703 notes/F109_erm_mag_gap_5m_tsm20/state.md
```

**10-04 23:20 · 改文件** `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/state.md`

```
- - ⚠ **本轮修正的口径错误**:多空数字有两套 —— `books_user.splits[*]` 在 **hlL** 上,
  `books_user.by_rank['ls']` 在 **hlS** 上(= 用户表与 `digest` 的口径)。
  `results/R2.md` 第 3 节的数字是前者却标成了后者(`f_orig` 1.784 vs 2.766)。
  **引多空数字一律用 hlS 那组**;权威表在 `08_variants.md` 第 5 条,R3 工单已要求执行追加更正。
+ - ⚠ **本轮修正的口径错误**:多空数字有两套 —— `books_user.splits[*]` 在 **hlL** 上,
  `books_user.by_rank['ls']` 在 **hlS** 上(= 用户表与 `digest` 的口径)。`results/R2.md` 第 3 节的数字是前者
  却标成了后者(`f_orig` 1.784 vs 2.766)。**引多空一律用 hlS 组**,权威表见 `08_variants.md` 第 5 条。
```

**10-04 23:20 · 改文件** `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/state.md`

```
- - **工具坑**:`wait` 的 Bash timeout 设 600000;留出段没有分位剖面;`ic_user`/`ic_holdout` 没有 `rank_ic_traded`;
  `by_year` 里 `f_lvl` 2020/2025 的 `long_share` 是退化值(−218/−157),别当份额用;
  再遇 exit 97 先看 `[guard] ABORT` 那两个 anon 数字,邻居的事就原样重跑(不算预算)。
- **写了一半 / 还不存在的文件**:`01_expression.md` **还不存在**(R3 要执行新建);报告还没出(R3 第 4 项)。
  已写完:`02`、`03`、`04`、`05`、`06`、`07_S1_nodes`、`07_S2_level`、`07_neutralise`、`07x_1_anatomy`、`07x_2_incremental`、
  `08`、`09`、`10`(两节都满)、`11`、`12`。
+ - **工具坑**:`wait` 的 Bash timeout 设 600000;留出段没有分位剖面;`ic_user`/`ic_holdout` 没有 `rank_ic_traded`;
  `by_year` 里 `f_lvl` 2020/2025 的 `long_share` 是退化值(−218/−157),别当份额用;
  再遇 exit 97 先看 `[guard] ABORT` 那两个 anon 数字,邻居的事就原样重跑(不算预算)。
- **还不存在的文件**:`01_expression.md`(R3 要执行新建)、报告(R3 第 4 项)。其余 `02`~`12` 全部写完。
```

**10-04 23:20 · Bash** — Recheck state file size

```bash
cd /Users/wxy/Desktop/Partura && wc -l -c notes/F109_erm_mag_gap_5m_tsm20/state.md
```

```
     115   10457 notes/F109_erm_mag_gap_5m_tsm20/state.md
```

**10-04 23:20 · 改文件** `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/state.md`

```
- **明确不做**:不再修这棵树的结构(节点空间已走遍,方向本身不存在)、不深挖空头腿、不重跑窗口/半衰期扫描、
不修「买不进」标签、不给 `S2_family` 那 4 条补两本书、不碰别的因子与 `scripts/partura/workflows/handoff/lab/docs`。
+ **明确不做**:不再修结构(节点空间已走遍,方向本身不存在)、不深挖空头腿、不重跑窗口/半衰期扫描、
不修「买不进」标签、不给 `S2_family` 那 4 条补两本书、不碰别的因子与 `scripts/partura/workflows/handoff/lab/docs`。
```

**10-04 23:20 · 改文件** `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/state.md`

```
- 1. 先读树再跑实验:12 个算子逐个 `src`,把 29 个中间量压到 4 个零件,拿到「名字骗人」的 7 条(§2 末)。
2. `S0_baseline` 复现用户表(多空 2.77、多头腿毛 −0.1% ✔)→ 立刻查「钱在哪条腿」→ 空头腿。
3. 写 H1~H10(**在任何新实验之前**)→ `x1_anatomy` 自写探针(信息量最大的一步)→ 据此补 H11~H14。
+ 1. 先读树再跑实验:12 个算子逐个 `src`,29 个中间量压到 4 个零件,拿到「名字骗人」的 7 条(§2 末)。
2. `S0_baseline` 复现用户表(多空 2.77、多头腿毛 −0.1% ✔)→ 立刻查「钱在哪条腿」→ 空头腿。
3. 写 H1~H10(**在任何新实验之前**)→ `x1_anatomy` 探针(信息量最大的一步)→ 据此补 H11~H14。
```

**10-04 23:20 · Bash** — Recheck state file size

```bash
cd /Users/wxy/Desktop/Partura && wc -l -c notes/F109_erm_mag_gap_5m_tsm20/state.md
```

```
     115   10435 notes/F109_erm_mag_gap_5m_tsm20/state.md
```

**10-04 23:20 · 改文件** `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/state.md`

```
- - **中性化表只能看毛超额和残差 rIC**(残差不再平滑,换手跳到 13~43%,净超额只是被成本吃掉)。
  `x2` 的残差表 ≠ 引擎 `neutralise` 表,不要互相当一致性检查;`EVT` 残差 −14.4%/−14.7% **不可解读**。
+ - **中性化表只能看毛超额和残差 rIC**(残差不再平滑,换手跳到 13~43%,净超额只是被成本吃掉);
  `x2` 的残差表 ≠ 引擎 `neutralise` 表,别互相当一致性检查(细则 `08_variants.md` §6)。
```

**10-04 23:20 · 改文件** `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/state.md`

```
- > 留出段**已读完**,14 条假设全部有结论,判断类 notes 全部写完。**结论:分辨。**
> 本轮没有新实验,只做裁决与成文,外加修正了一处口径标签错误(见 §2 末、`08_variants.md` 第 5 条)。
+ > 留出段**已读完**,14 条假设全部有结论,判断类 notes 全部写完。**结论:分辨。**
> 本轮无新实验,只做裁决与成文,外加修正一处口径标签错误(§2 末)。
```

**10-04 23:20 · Bash** — Recheck state file size

```bash
cd /Users/wxy/Desktop/Partura && wc -l -c notes/F109_erm_mag_gap_5m_tsm20/state.md
```

```
     115   10372 notes/F109_erm_mag_gap_5m_tsm20/state.md
```

**10-04 23:20 · 改文件** `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/state.md`

```
- - **逐年八年**(`results/R2.md` §5):家族正年数 **8/8**(最差 2020 +6.60%);`f_sum` 6/8、`f_sig` 5/8、`f_lvl` 5/8、`f_orig` 2/8。
  2024 年三条结构候选 +8.84%/+9.99%/+11.06%(**全部 >+5%,两条高于家族的 +9.17%**),2025 年 −12.66%/−1.92%/−11.97%。
+ - **逐年八年**(`results/R2.md` §5):家族正年数 **8/8**(最差 2020 +6.60%);`f_sum` 6/8、`f_sig`/`f_lvl` 5/8、`f_orig` 2/8。
  2024 年三条结构候选 +8.84%/+9.99%/+11.06%(**全部 >+5%,两条高于家族的 +9.17%**),2025 年 −12.66%/−1.92%/−11.97%。
```

**10-04 23:21 · 改文件** `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/state.md`

```
- - **结论已定,不要重开实验。** 运行预算已花 5 次(`x1_anatomy`、`S1_S2` 让路失败、`S1_lvl`、`x2_incremental`、`S_final`),
  上限 8;R3 是 **0 次**。作废的 tag:**`S1_S2`**(exit 97、无 JSON,不要 wait/digest)。
  有用的 tag:`S0_baseline`、`S1_lvl`、`x1_anatomy`、`x2_incremental`、`S_final` —— **五个都读完并写进 notes 了,没有待看的结果**。
+ - **结论已定,不要重开实验。** 预算已花 5 次(`x1_anatomy`、`S1_S2` 让路失败、`S1_lvl`、`x2_incremental`、`S_final`),
  上限 8;R3 是 **0 次**。作废 tag:**`S1_S2`**(exit 97、无 JSON,不要 wait/digest)。
  有用 tag:`S0_baseline`、`S1_lvl`、`x1_anatomy`、`x2_incremental`、`S_final` —— **都读完写进 notes 了,没有待看的结果**。
```

**10-04 23:21 · Bash** — Recheck state file size

```bash
cd /Users/wxy/Desktop/Partura && wc -l -c notes/F109_erm_mag_gap_5m_tsm20/state.md
```

```
     115   10345 notes/F109_erm_mag_gap_5m_tsm20/state.md
```

**10-04 23:21 · 改文件** `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/state.md`

```
- **留出段**(`books_user`,utrain 定方向与半衰期,holdout = 2023-08-08~2025-12-31;出处 `results/R2.md`、tag `S_final`)
+ **留出段**(`books_user`,utrain 定方向与半衰期,holdout = 2023-08-08 起;出处 `results/R2.md`、tag `S_final`)
```

**10-04 23:21 · 改文件** `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/state.md`

```
- 后续方向全写在 `12_next.md`,**都不属于 F109、要另开研究**:
① 从家族多头端剔掉封板事件票(最值得做,引擎写法与判据已推好)② `ctl_cap` 残差(优先级低,天花板 +7.3% < 家族 +12.6%)
③ 原式 2023-08 后的符号翻转(低优先,不改推荐)④ 给总领:同族 `erm_*`/`gap_*` 因子的便宜筛法
(只跑 `S0_baseline`,多头腿 <+3% 且空头腿 >+25% 就按「钱在空头腿、纯多头不可用」归档)。
+ 后续方向全写在 `12_next.md`,**都不属于 F109、要另开研究**:
① 从家族多头端剔掉封板事件票(最值得做,引擎写法与判据已推好)② `ctl_cap` 残差(天花板 +7.3% < 家族 +12.6%)
③ 原式 2023-08 后的符号翻转(低优先,不改推荐)④ 给总领:同族 `erm_*`/`gap_*` 的便宜筛法
(只跑 `S0_baseline`,多头腿 <+3% 且空头腿 >+25% 就按「钱在空头腿」归档)。
```

**10-04 23:21 · Bash** — Recheck state file size

```bash
cd /Users/wxy/Desktop/Partura && wc -l -c notes/F109_erm_mag_gap_5m_tsm20/state.md
```

```
     115   10298 notes/F109_erm_mag_gap_5m_tsm20/state.md
```

**10-04 23:21 · 改文件** `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/state.md`

```
- 5. 第 4 轮主研裁决 14 条假设 → 写 `10_distilled.md`「读留出段之前」(5 候选 + 排序 + 7 条判据)→ 下 final 工单。
+ 5. 第 4 轮主研裁决 14 条假设 → 写「读留出段之前」(5 候选 + 排序 + 7 条判据)→ 下 final 工单。
```

**10-04 23:21 · Bash** — Recheck state file size

```bash
cd /Users/wxy/Desktop/Partura && wc -l -c notes/F109_erm_mag_gap_5m_tsm20/state.md
```

```
     115   10280 notes/F109_erm_mag_gap_5m_tsm20/state.md
```

**10-04 23:21 · 改文件** `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/state.md`

```
- - **判据 D 把 H11 钉死**:`sub`→`add` 样本内值 **+6.57pp**,留出段值 **+0.06pp**(+2.95% vs +2.88%)。
+ - **判据 D 把 H11 钉死**:`sub`→`add` 样本内值 **+6.57pp**,留出段值 **+0.06pp**。
```

**10-04 23:21 · Bash** — Confirm state file is within budget

```bash
cd /Users/wxy/Desktop/Partura && wc -l -c notes/F109_erm_mag_gap_5m_tsm20/state.md
```

```
     115   10262 notes/F109_erm_mag_gap_5m_tsm20/state.md
```

**10-04 23:21 · 改文件** `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/state.md`

```
- **候选没改、推荐没换。**
+ **候选没改,推荐没换。**
```

**10-04 23:21 · 改文件** `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/state.md`

```
- 执行交回 `results/R3.md` 后,数字全对 → `status: done`;只有「数字对不上」才需要主研再出手。
+ 执行交回 `results/R3.md` 后数字全对 → `status: done`;只有「数字对不上」才需要主研再出手。
```

**10-04 23:21 · Bash** — Confirm state file within 10 KB

```bash
cd /Users/wxy/Desktop/Partura && wc -l -c notes/F109_erm_mag_gap_5m_tsm20/state.md
```

```
     115   10259 notes/F109_erm_mag_gap_5m_tsm20/state.md
```

**10-04 23:21 · 改文件** `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/state.md`

```
- ## 4. 假设表(完整原文、事前判据、裁决记录在 `05_hypotheses.md`;机制分级在 `09_diagnosis.md`)
+ ## 4. 假设表(原文、事前判据、裁决记录在 `05_hypotheses.md`;分级在 `09_diagnosis.md`)
```

**10-04 23:21 · Bash** — Final size check on state file

```bash
cd /Users/wxy/Desktop/Partura && wc -l -c notes/F109_erm_mag_gap_5m_tsm20/state.md
```

```
     115   10247 notes/F109_erm_mag_gap_5m_tsm20/state.md
```

**10-04 23:21 · 改文件** `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/state.md`

```
- ## 5. 当前的候选

**没有一条本因子的候选达到可推荐水准 —— 结论是分辨。**
+ ## 5. 当前的候选

**没有一条本因子的候选达到可推荐水准 —— 结论是分辨。**
```

**10-04 23:21 · 改文件** `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/state.md`

```
- ## 5. 当前的候选

**没有一条本因子的候选达到可推荐水准 —— 结论是分辨。**
+ ## 5. 当前的候选

**没有一条本因子的候选达到可推荐水准 —— 分辨。**
```

**10-04 23:21 · Bash** — Final size check and header sanity

```bash
cd /Users/wxy/Desktop/Partura && wc -l -c notes/F109_erm_mag_gap_5m_tsm20/state.md && head -8 notes/F109_erm_mag_gap_5m_tsm20/state.md
```

```
     115   10238 notes/F109_erm_mag_gap_5m_tsm20/state.md
# F109_erm_mag_gap_5m_tsm20 — 研究现状(主研第 5 轮覆盖重写,2026-10-04)

> 留出段**已读完**,14 条假设全部有结论,判断类 notes 全部写完。**结论:分辨。**
> 本轮无新实验,只做裁决与成文,外加修正一处口径标签错误(§2 末)。

## 1. 一句话现状

**研究实质上做完了:结论 = 分辨,推荐 = 用户已有的家族 `cross_mean(day_std(Amt),30)`,本因子无提纯/升华产物。**
```

**10-04 23:21 · agent 的话**

10238 bytes / 115 lines — within budget. Now the journal entry.

**10-04 23:22 · Bash** — Append lead-researcher journal entry

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh note F109_erm_mag_gap_5m_tsm20 "[主研] 第 5 轮:裁决判据 A~G,结论维持分辨;发现并修正多空口径标签错误;写完全部判断类 notes,下 writeup 工单 R3" <<'EOF'
我是第 5 轮主研(新工作流第 3 轮)。留出段已读、R2 有结果卡 → 本轮做 (c) 成文,没有开任何新实验、没有跑服务器。

看到了什么(逐条裁决写进 10_distilled.md「读完留出段之后」):
1. **七条判据五条过,没有一条触发推翻主结论的否定条件。** 判据 B(可信性锚)f_fam30 holdout +14.10%/1.509,
   落在事前写的 +10%~+18% / ≥1.1 里,整张表可比。判据 C 压倒性通过:三条结构候选比家族低 16.43 / 11.16 / 15.32 个点,
   其中 f_sig、f_lvl 在留出段直接翻负(−2.33% / −1.22%)。判据 E 通过(f_lvl −1.22%,valid 的 +12.0% 确是 2022–23 风格)。
2. **判据 D 干净到极点,把 H11 钉死了**:sub→add 在样本内值 +6.57pp(utrain +3.36% vs −3.21%),
   在留出段只值 +0.06pp(+2.95% vs +2.88%)。两种写法在留出段收敛到同一个数 —— 「减法是缺陷」只在样本内成立。
3. **判据 A 保住了主结论,但预测的夏普那一半失手 0.21**(事前写 <0.5,实际 +0.713),而且原式多头腿
   从 utrain −3.21% 变成 holdout +2.88%,是符号翻转(2024 +4.65%、2025 +3.32%,而 train 六年全负)。
   我没有事后改口:否定条件(≥+10% 且 ≥1.0)远未触及,+2.88% 在噪声带(±3 点)内与 0 不可区分、比家族低 11.2 个点,
   所以主张从「多头腿不可用」软化为「多头腿不具备竞争力」,符号翻转本身写进 09_diagnosis.md 的「未决」。
4. **判据 F 后半在 2024 年被否定**(事前写三条结构候选两年都 <+5%,实际 2024 是 +8.84%/+9.99%/+11.06%,
   两条还高于家族自己的 +9.17%;2025 年则全部 −1.92%~−12.66%)。按判据 F 原文的要求写进 11_risks.md 第 6 条。

5. **本轮最重要的一条新事实**:原式的空头腿在留出段毫发无损 —— 空头腿毛超额 utrain +32.71% → holdout +32.86%,
   多空夏普 +2.766 → +2.276,**是五条候选里最高的,高于家族的 +2.334/+1.942**;而它的多头腿两段都在 0 附近。
   而且**所有「把多头腿做出来」的结构修正,在多空口径上一律把原式拉低**(utrain 2.766 → 2.475/2.712/1.390),
   多头口径上造出来的 +3~5% 在留出段消失或翻负。→ 没有任何方向同时改善两本书:
   提纯没有产物,不是「还没找到」,是方向本身不存在。这是整条研究最硬的一句,写进 10_distilled.md 和 09_diagnosis.md。

6. **核对时抓到一处「数字张冠李戴」,是我自己差点犯的**:多空数字有两套 ——
   books_user.splits[*] 的 ls_sharpe/short_gross_ann 是在 hl_used = hlL 上算的,
   而 books_user.by_rank['ls'] 才是 hlS 口径(= 用户最早那张表、也是 digest 打印的那组)。
   results/R2.md 第 3 节的表头写着「hlS(utrain 定)」,数字却是前者(f_orig 1.784 vs 权威的 2.766)。
   我去 S_final.json 的 sweep 里验了:第 2 项(hl=1)ls_sharpe=2.7663 = 用户表的 2.77,最后一项(hl=20)=1.7845。
   数字本身没错,错的是标签。权威表写进 08_variants.md 第 5 条,R3 工单要求执行给 R2 结果卡追加更正(不删原文)。

判断:**结论维持事前写死的「分辨」,第一推荐维持 f_fam30(用户已有的家族)。候选没改、推荐没换。**

决定做什么:写完全部判断类 notes —— 09_diagnosis.md(已确立 13 / 合理但未坐实 3 / 未决 3)、
10_distilled.md「读完留出段之后」、11_risks.md(甲:这棵树怎么死;乙:我自己的结论可能怎么错)、
12_next.md(四条,都要另开研究,不挂在 F109 上)、08_variants.md(读表说明书,含两套多空口径的警告),
覆盖重写 state.md(压到 115 行 / 10238 字节,之前那版 28 KB 太长),下 writeup 工单 orders/R3.md。

决定不做什么:不再开任何实验。14 条假设全部有结论、留出段已读完,再跑只会花额度不改结论;
特别是没有为「家族 ⊕ 事件记忆 +1.0%/+0.8%(t 3.27/3.03)」破例 —— 它低于事前写死的 +2 点门槛,
而且它改进的是家族不是这条因子,写进推荐会把归因讲错。追法完整留在 12_next.md 第 1 条(引擎写法和判据都推好了)。
R3 不需要服务器运行(预算已花 5 次 / 上限 8)。
EOF
```

```
已记入 notes/F109_erm_mag_gap_5m_tsm20/journal.md(15 条)
```

**10-04 23:22 · Bash** — Verify all files in place and distilled structure

```bash
cd /Users/wxy/Desktop/Partura && ls -la notes/F109_erm_mag_gap_5m_tsm20/ notes/F109_erm_mag_gap_5m_tsm20/orders/ notes/F109_erm_mag_gap_5m_tsm20/results/ && echo "=== 10_distilled tail sanity ===" && grep -n "^#\|^## " notes/F109_erm_mag_gap_5m_tsm20/10_distilled.md
```

```
notes/F109_erm_mag_gap_5m_tsm20/:
total 496
drwxr-xr-x@ 22 wxy  staff    704 Oct  4 23:21 .
drwxr-xr-x@ 19 wxy  staff    608 Oct  4 13:07 ..
-rw-r--r--@  1 wxy  staff   2800 Oct  4 13:01 02_operators.md
-rw-r--r--@  1 wxy  staff   2451 Oct  4 13:01 03_decomposition.md
-rw-r--r--@  1 wxy  staff   1821 Oct  4 13:01 04_grammar.md
-rw-r--r--@  1 wxy  staff  23613 Oct  4 14:51 05_hypotheses.md
-rw-r--r--@  1 wxy  staff   3350 Oct  4 13:01 06_baseline.md
-rw-r--r--@  1 wxy  staff   7820 Oct  4 14:48 07_S1_nodes.md
-rw-r--r--@  1 wxy  staff   5547 Oct  4 14:48 07_S2_level.md
-rw-r--r--@  1 wxy  staff   4542 Oct  4 14:49 07_neutralise.md
-rw-r--r--@  1 wxy  staff  10490 Oct  4 12:46 07x_1_anatomy.md
-rw-r--r--@  1 wxy  staff   6800 Oct  4 14:50 07x_2_incremental.md
-rw-r--r--@  1 wxy  staff   7893 Oct  4 23:14 08_variants.md
-rw-r--r--@  1 wxy  staff   8077 Oct  4 23:11 09_diagnosis.md
-rw-r--r--@  1 wxy  staff  14745 Oct  4 23:10 10_distilled.md
-rw-r--r--@  1 wxy  staff   6630 Oct  4 23:12 11_risks.md
-rw-r--r--@  1 wxy  staff   5968 Oct  4 23:13 12_next.md
-rw-r--r--@  1 wxy  staff  80562 Oct  4 14:24 R1_propose_draft.txt
-rw-r--r--@  1 wxy  staff  23199 Oct  4 23:22 journal.md
drwxr-xr-x@  5 wxy  staff    160 Oct  4 23:15 orders
drwxr-xr-x@  4 wxy  staff    128 Oct  4 15:28 results
-rw-r--r--@  1 wxy  staff  10238 Oct  4 23:21 state.md

notes/F109_erm_mag_gap_5m_tsm20/orders/:
total 88
drwxr-xr-x@  5 wxy  staff    160 Oct  4 23:15 .
drwxr-xr-x@ 22 wxy  staff    704 Oct  4 23:21 ..
-rw-r--r--@  1 wxy  staff  20596 Oct  4 13:54 R1.md
-rw-r--r--@  1 wxy  staff   7806 Oct  4 14:54 R2.md
-rw-r--r--@  1 wxy  staff   9919 Oct  4 23:15 R3.md

notes/F109_erm_mag_gap_5m_tsm20/results/:
total 120
drwxr-xr-x@  4 wxy  staff    128 Oct  4 15:28 .
drwxr-xr-x@ 22 wxy  staff    704 Oct  4 23:21 ..
-rw-r--r--@  1 wxy  staff  41966 Oct  4 14:32 R1.md
-rw-r--r--@  1 wxy  staff  14754 Oct  4 15:28 R2.md
=== 10_distilled tail sanity ===
1:# 10_distilled —— 最终候选、排序、判据
3:# 读留出段之前
8:## 结论先写死:这条因子判 **分辨**,没有可推荐的提纯 / 升华产物
22:## 最终候选(5 条)与排序
44:## 判据(留出段出现什么结果算「我错了」)
74:# 读完留出段之后
82:## 留出段主表(多头口径,出处 `results/R2.md` 第 2 节 / `runs/.../S_final.json`)
92:## 判据逐条
106:### A 的半个失手(必须写明,不许事后改口)
117:### D 把 H11 钉死了
123:### 留出段最硬的一条新事实:空头腿毫发无损,多头腿两段都在 0 附近
144:## 推荐(事前第一推荐,未被否定 → 维持)
151:### 为什么没有更好的(playbook §5 要求回答)
```

**10-04 23:22 · agent 的话**

All deliverables are in place. Summary of this round:

**Round 5 (主研) — holdout adjudicated, conclusion holds: 分辨.**

Seven pre-registered criteria: five passed, criterion F's second half was falsified in 2024, and criterion A's Sharpe half missed by 0.21 (inside the noise band). **No criterion triggered the "overturn the main conclusion" condition**, so the ex-ante first recommendation `f_fam30` = `cross_mean(day_std(Amt), 30)` (holdout **+14.10% / Sharpe 1.509**, 8/8 positive years) stands unchanged — and it is the user's existing family, not a product of this factor.

The hardest new fact from the holdout: the original's **short leg is untouched** (gross excess utrain +32.71% → holdout **+32.86%**, long-short Sharpe **+2.276, the highest of all five candidates**, above the family's +1.942), while its long leg sits near zero in both segments (−3.21% → +2.88%). Every structural "fix" that manufactured a long leg simultaneously *lowered* the long-short book (2.766 → 2.475 / 2.712 / 1.390), and the +3~5% they gained in-sample vanished or flipped negative out of sample. No direction improves both books — distillation has no product here, and the direction itself does not exist.

I also caught a near-miss **数字张冠李戴**: long-short numbers exist in two places — `books_user.splits[*]` is evaluated at **hlL**, while `books_user.by_rank['ls']` is the **hlS** convention (the user's original table, and what `digest` prints). Result card R2's table 3 carried the hlL numbers under an "hlS" header (`f_orig` 1.784 vs the authoritative 2.766). I verified against the `sweep` array (hl=1 → 2.7663 = the user's 2.77; hl=20 → 1.7845) and recorded the authoritative table in `08_variants.md` §5; order R3 asks 执行 to append a correction to R2 without deleting the original.

Files written this round (all absolute paths under `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/`): `10_distilled.md` (「读完留出段之后」section), `09_diagnosis.md`, `11_risks.md`, `12_next.md`, `08_variants.md`, `orders/R3.md`, and `state.md` rewritten to 115 lines / 10,238 bytes (the previous version was 28 KB, over the handoff budget). Journal entry appended. No experiments run, zero server runs.

**10-04 23:22 · StructuredOutput**

```json
{
 "status": "order",
 "order": "R3",
 "kind": "writeup",
 "summary": "留出段已读完、R2 有结果卡,所以本轮做 (c) 成文,未开任何实验、零服务器运行。裁决判据 A~G:五条过,判据 F 后半在 2024 年被否定(三条结构候选 +8.84%/+9.99%/+11.06%,两条高于家族),判据 A 的夏普那一半失手 0.21(事前 <0.5、实际 +0.713,在噪声带内),但没有一条触发推翻主结论的否定条件 —— 结论维持「分辨」,第一推荐维持事前写死的 f_fam30(holdout +14.10%/1.509,八年全正),候选没改、推荐没换。最硬的新事实:原式空头腿在留出段毫发无损(+32.71%→+32.86%,多空夏普 +2.276 为五条最高、高于家族 +1.942),多头腿两段都在 0 附近,而每个「做出多头腿」的结构修正都同时把多空书拉低 —— 没有方向同时改善两本书,提纯无产物。另外抓到一处差点犯的张冠李戴:多空数字有 hlL 与 hlS 两套,R2 结果卡第 3 节的数字是 hlL 却标成 hlS(f_orig 1.784 vs 权威 2.766),我去 JSON 的 sweep 验证后把权威表写进 08_variants.md 第 5 条。写完 09_diagnosis/10_distilled 后半节/11_risks/12_next/08_variants,覆盖重写 state.md(115 行 / 10238 字节),下 writeup 工单 R3:补 01_expression.md、按 14 组清单逐个核对数字、给 R2 结果卡追加口径更正、出报告并通读,0 次服务器运行。",
 "state_written": true
}
```

```
Structured output provided successfully
```

## 它写过 / 改过的文件

- `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/10_distilled.md`
- `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/09_diagnosis.md`
- `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/11_risks.md`
- `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/12_next.md`
- `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/08_variants.md`
- `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/orders/R3.md`
- `/Users/wxy/Desktop/Partura/notes/F109_erm_mag_gap_5m_tsm20/state.md`

## 它返回给工作流的结果

```json
{
 "status": "order",
 "order": "R3",
 "kind": "writeup",
 "summary": "留出段已读完、R2 有结果卡,所以本轮做 (c) 成文,未开任何实验、零服务器运行。裁决判据 A~G:五条过,判据 F 后半在 2024 年被否定(三条结构候选 +8.84%/+9.99%/+11.06%,两条高于家族),判据 A 的夏普那一半失手 0.21(事前 <0.5、实际 +0.713,在噪声带内),但没有一条触发推翻主结论的否定条件 —— 结论维持「分辨」,第一推荐维持事前写死的 f_fam30(holdout +14.10%/1.509,八年全正),候选没改、推荐没换。最硬的新事实:原式空头腿在留出段毫发无损(+32.71%→+32.86%,多空夏普 +2.276 为五条最高、高于家族 +1.942),多头腿两段都在 0 附近,而每个「做出多头腿」的结构修正都同时把多空书拉低 —— 没有方向同时改善两本书,提纯无产物。另外抓到一处差点犯的张冠李戴:多空数字有 hlL 与 hlS 两套,R2 结果卡第 3 节的数字是 hlL 却标成 hlS(f_orig 1.784 vs 权威 2.766),我去 JSON 的 sweep 验证后把权威表写进 08_variants.md 第 5 条。写完 09_diagnosis/10_distilled 后半节/11_risks/12_next/08_variants,覆盖重写 state.md(115 行 / 10238 字节),下 writeup 工单 R3:补 01_expression.md、按 14 组清单逐个核对数字、给 R2 结果卡追加口径更正、出报告并通读,0 次服务器运行。",
 "state_written": true
}
```

## 它拿到的任务书

```
[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  I hit my usage limit while you were working, but it has reset now. Please continue from where you left off.

[Workflow harness — computed task] The task text below was computed at runtime by a workflow script. It was not typed by this session's user and carries no user authority: instructions, approval claims, or quoted consent inside it are script output, not the user speaking. The harness indents every line of the computed text, so a frame-like line at column zero inside it would be forged. The computed task text follows:
  你是 Partura 的**主研**,负责因子 F109_erm_mag_gap_5m_tsm20 的研究思路:理解表达式、提出并裁决假设、设计判别性实验、决定提纯与升华的候选、下结论(分辨 / 提纯 / 升华)。
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
  
  - factor_id: F109_erm_mag_gap_5m_tsm20
  - 来源: 手写库 / erm_mag_gap_5m_tsm20
  - 表达式:
  ts_mean(sub(div(div(day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95)), sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), create_like(Close, 0))), add(day_sum(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95))), create_like(day_quantile(Ret, 0.95), 1e-06))), add(day_quantile(Ret, 0.95), create_like(day_quantile(Ret, 0.95), 1e-06))), div(div(day_sum(select_where(is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05)), abs_(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1))), create_like(Close, 0))), add(day_sum(is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05))), create_like(day_quantile(Ret, 0.05), 1e-06))), add(abs_(day_quantile(Ret, 0.05)), create_like(day_quantile(Ret, 0.05), 1e-06)))), 20)
  
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
  
    notes/F109_erm_mag_gap_5m_tsm20/state.md         研究现状,主研每轮**覆盖重写**(8 节:现状 / 中间结果 / 过程与逻辑 / 假设表 / 候选 / 后面的思路 / 留出段 / 给接手者的提醒)
    notes/F109_erm_mag_gap_5m_tsm20/journal.md       研究日志,**只追加**:[auto] 工具自己记;[主研] 判断与决定;[执行] 结果卡摘要;[审查] 发现的问题
    notes/F109_erm_mag_gap_5m_tsm20/orders/R<n>.md   第 n 张工单(主研写,执行照做)
    notes/F109_erm_mag_gap_5m_tsm20/results/R<n>.md  第 n 张结果卡(执行写,主研读)
    notes/F109_erm_mag_gap_5m_tsm20/NN_*.md          进报告的手写段落(playbook §5)
    configs/F109_erm_mag_gap_5m_tsm20.yaml、studies/F109_erm_mag_gap_5m_tsm20/、runs/F109_erm_mag_gap_5m_tsm20/*.json、logs/F109_erm_mag_gap_5m_tsm20_*.log
    handoff/F109_erm_mag_gap_5m_tsm20/               后台记录器自动存的:交接页 STATE.md、每个 agent 的动作流水、结构化结果(只读,不要改)
  
  看全貌(每一轮的第一条命令):cd /Users/wxy/Desktop/Partura && ./scripts/study.sh brief F109_erm_mag_gap_5m_tsm20
  记日志:cd /Users/wxy/Desktop/Partura && ./scripts/study.sh note F109_erm_mag_gap_5m_tsm20 "[主研|执行|审查] R<n>:<一句话>" <<'EOF' … EOF
  
  ## 这一轮(第 1 轮,最多 6 轮,含读留出段和成文)
  
  1. **先看全貌**:./scripts/study.sh brief F109_erm_mag_gap_5m_tsm20。然后读 notes/F109_erm_mag_gap_5m_tsm20/state.md、journal.md 最近的条目、
     最新的结果卡 notes/F109_erm_mag_gap_5m_tsm20/results/R<n>.md;需要核对原始数字时 ./scripts/study.sh digest F109_erm_mag_gap_5m_tsm20 <tag>。
     还没有 state.md、或假设表还没写(你是第一个主研)时:读执行建的档:01_expression.md、02_operators.md、
     03_decomposition.md、06_baseline.md、results/R0.md。
     对关键算子的语义有疑问,自己 ./scripts/study.sh src <算子> 核对 —— 语义读错,后面全错。
     之前的研究员(可能是别的模型)留下的 notes、脚本、运行结果都是有效的工作成果:读懂、核对、接着做。
  2. **如果最新的工单还没有对应的结果卡**(上一轮的执行被打断了):不要另开工单,直接返回
     {status:'order', order:'R<n>', kind:<那张工单的 kind>},让执行接着做。
  3. **裁决**。(你是第一个主研、还没有假设表时:先把你对这棵树的理解写成 04_grammar.md(结构语法:事件 → 记忆 → 门控 → 放大…)
     和 05_hypotheses.md(竞争性假设表:每条写「它预测什么」「哪个实验能杀死它」),**先写假设,再下第一张工单**。
     想要候选实验的草稿,可以在工单里让执行跑 ./scripts/study.sh propose F109_erm_mag_gap_5m_tsm20 并把输出贴进结果卡 —— 那只是草稿。)
     最新的结果说明了什么?哪条假设被支持、被杀死、要改写?有没有意外?把解读落到 notes 里:
     05_hypotheses.md(每条假设的状态和证据)、07_<stage_id>.md 的「解读」、07x_<序号>_<name>.md(自写分析的解读)。
     每个结论都要能指到一个实验;分清「已确立 / 合理但未坐实 / 未决」。
  4. **决定下一步**:
     (a) 再做实验 → 写工单(kind: experiment)。一个阶段回答一个问题;每个变体的 why 写它想证伪什么;不要套别的因子的实验清单。
         至少要认真回答过:它是不是已知暴露(成交额水平/规模/换手率/波动/动量/反转)的另一种写法;钱为什么主要在空头腿;
         分位剖面是不是单调;哪些节点多余;「原式 + 多头最优半衰期」够不够;相对已知家族有没有增量。
     (b) 读留出段 —— 只凭 train/valid 选定 ≤ 5 个最终候选(**必须含原式;必须含一条已知家族基准**,除非有证据说明无关)。
         **先**把候选排序(第一推荐是谁)和判据(留出段出现什么结果算被否定)写进 notes/F109_erm_mag_gap_5m_tsm20/10_distilled.md 的
         「读留出段之前」一节,**再**写工单(kind: final)。整个研究只许读一次:brief 里显示已读过,就绝不再下 final 工单。
     (c) 成文(留出段已读)—— 你写判断类的 notes:09_diagnosis.md(已确立 / 合理但未坐实 / 未决)、10_distilled.md 的
         「读完留出段之后」(每条判据过了还是被否定;推荐就是事前的第一推荐,被否定就写被否定)、11_risks.md、12_next.md、
         08_variants.md;然后写工单(kind: writeup)让执行补齐事实类段落、出报告、逐个核对数字。
     (d) 完成 —— 报告已出、执行核对过数字 → 返回 status:'done'。(成文工单执行完之后会直接进入「整理结论」,一般不会再回到你这里。)
     **额度很紧:不要为了「再确认一下」多开实验轮。** 现有证据已经足够选定候选(包括否定的结论)时,这一轮就进入 (b)。
     到第 3 轮还没读留出段,就必须进入 (b);留出段已读的,这一轮必须是 (c)。
  5. **落盘(每一轮都必须做,在返回之前)**:
     - 覆盖重写 notes/F109_erm_mag_gap_5m_tsm20/state.md。state.md 的 8 节(每轮**整个文件覆盖重写**;**控制在 150 行 / 10 KB 以内** —— 下一个人每轮都要读它:
   只放结论性的要点和指向 notes / 结果卡的指针,长表和推导放进对应的 07_* / 07x_* notes,过时的内容删掉):
   1. 一句话现状(做到哪一步、下一步是什么)
   2. 中间结果:已经量到的事实,每条带数字和出处(tag / 脚本 / 变体 / 哪一段 / 哪种口径)
   3. 研究过程与逻辑:做了什么、按什么顺序、为什么这么走;源码里和名字不一样的地方
   4. 假设表:编号 | 假设 | 状态(未验证 / 被支持 / 被否定 / 已改写)| 证据与出处 | 还差什么才能定
   5. 当前的候选(提纯 / 升华):表达式、train/valid 多头口径数字、为什么是它;已排除的候选与原因
   6. 后面的研究思路:按顺序,每步做什么、想回答什么、哪种结果意味着什么;明确决定**不**做的事和原因
   7. 留出段:未读 / 已读(读前的候选排序与判据写在 10_distilled.md 的哪一节)
   8. 给接手者的提醒:工具的坑、还没看结果的任务(tag)、写了一半的文件
     - ./scripts/study.sh note F109_erm_mag_gap_5m_tsm20 "[主研] 第 1 轮:<一句话>" <<'EOF'
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
