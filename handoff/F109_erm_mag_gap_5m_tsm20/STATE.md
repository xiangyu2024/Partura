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
