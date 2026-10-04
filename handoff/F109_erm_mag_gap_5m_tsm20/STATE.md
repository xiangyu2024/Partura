# F109_erm_mag_gap_5m_tsm20 — 交接状态

_自动生成于 2026-10-04 13:41(`python scripts/recorder.py --brief F109_erm_mag_gap_5m_tsm20` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:手写 erm_mag_gap_5m_tsm20(批次 B01_single_factors)
- 表达式:`ts_mean(sub(div(div(day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95)), sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), create_like(Close, 0))), add(day_sum(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95))), create_like(day_quantile(Ret, 0.95), 1e-06))), add(day_quantile(Ret, 0.95), create_like(day_quantile(Ret, 0.95), 1e-06))), div(div(day_sum(select_where(is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05)), abs_(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1))), create_like(Close, 0))), add(day_sum(is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05))), create_like(day_quantile(Ret, 0.05), 1e-06))), add(abs_(day_quantile(Ret, 0.05)), create_like(day_quantile(Ret, 0.05), 1e-06)))), 20)`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- 留出段:**还没读过**(只能读一次;读之前要在 `10_distilled.md` 里写下候选排序和判据)。
- agent `study:F109_erm_mag_gap_5m_tsm20#2`(wf_759ef2d3-03f):失败,几乎没做事(不用看)
- agent `study:F109_erm_mag_gap_5m_tsm20#3`(wf_759ef2d3-03f):失败,几乎没做事(不用看)
- agent `study:F109_erm_mag_gap_5m_tsm20`(wf_08351f46-81b):中断,最后动作 10-04 13:10 → `handoff/F109_erm_mag_gap_5m_tsm20/agents/study_aac3edb482327d547.md`
- agent `lead:F109_erm_mag_gap_5m_tsm20#1`(wf_3cafb924-05e):已返回结果,最后动作 10-04 13:22 → `handoff/F109_erm_mag_gap_5m_tsm20/agents/lead_R1_af3d7357655388cba.md`
- agent `work:F109_erm_mag_gap_5m_tsm20#1`(wf_3cafb924-05e):已返回结果,最后动作 10-04 13:27 → `handoff/F109_erm_mag_gap_5m_tsm20/agents/work_R1_a4c38d50d9b987bf4.md`
- agent `lead:F109_erm_mag_gap_5m_tsm20#2`(wf_3cafb924-05e):失败,几乎没做事(不用看)
- agent `lead:F109_erm_mag_gap_5m_tsm20#2`(wf_3cafb924-05e):失败,几乎没做事(不用看)
- agent `lead:F109_erm_mag_gap_5m_tsm20#1`(wf_48864a04-f0a):还在跑(如果这就是你自己,不用看它的流水)

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F109_erm_mag_gap_5m_tsm20` 看服务器上的 tag,`./scripts/study.sh digest F109_erm_mag_gap_5m_tsm20 <tag>` 重看结果)。

## 研究现状(`notes/F109_erm_mag_gap_5m_tsm20/state.md`,10-04 13:31 更新)—— **先读这个文件**

# F109_erm_mag_gap_5m_tsm20 — 研究现状(主研第 2 轮重写,2026-10-04)

> 这一页由**主研**整个覆盖重写(第 2 轮)。第 1 轮主研写的判断我全部核对后保留下来(事实与出处都没变),
> 这一轮新增的是**一条把上一张工单的前提推翻了的运行事实**:`S1_S2` 没跑成(exit 97)。
> 下一位主研只看得到文件 —— 这页写的是判断,事实的出处都标了。

---

## 1. 一句话现状

读树与基线已经做完(S0 + 自写探针 x1),**这棵树的钱全在空头腿、多头腿在 train 上是负的(−4.6%,多头最优半衰期 hl 20)**,
而且空头腿有一半是「次日买不进」撑出来的。
**这一轮(第 2 轮)查出来的关键事实:上一位研究员启动的 `S1_S2`(8+6=14 变体)已经结束,但是 `exit 97`(内存守卫让路)——
没有 JSON、没有本地日志,14 个变体一个都没算出来。** 工单 R1 的 A 组前提(「已经在跑,只收不重跑」)因此失效。
我没有另开工单(按分工规矩:最新工单还没有结果卡就不另开),而是在 `orders/R1.md` 末尾加了一节
**「修订 A′(主研第 2 轮)」**:A 组改成**重跑 `S1_nodes` 单独一个阶段(8 变体,新 tag `S1_nodes`)**,
`S2_family` 推到 R2;B 组(自写脚本 `x2_incremental`)原样不变。
**下一步 = 执行按修订后的 R1 做两件事:重跑 `S1_nodes` + 跑 `x2_incremental`,写结果卡 `results/R1.md`。**
我的倾向性判断仍然是结论会落在**分辨**(多头腿不可用 + 对已知家族无增量),但还缺两块坐实的证据:
S1 的引擎口径复核(numpy 重构说的事要在官方口径上确认)与 x2 的配对差(增量是否超噪声)。

---

(…全文 16368 字符,读 `notes/F109_erm_mag_gap_5m_tsm20/state.md`)

## 研究日志(`notes/F109_erm_mag_gap_5m_tsm20/journal.md`:4 条,其中研究员自己写的 2 条)

最近的 12 条(完整的看文件):

### 2026-10-04 12:48 [auto] 启动 run S1_S2:阶段 S1_nodes S2_family

### 2026-10-04 13:20 [主研] 第 1 轮:重写 state.md,下工单 R1(收 S1_S2 + 跑 x2 增量实验)

我是新分工下的第一位主研。上一位研究员(Opus 5.5)读完树、跑完 S0 与自写探针 x1、启动了 S1_S2 就被换下,
没留下判断,state.md 是脚本自动汇编的。这一轮我读完 02/03/04/05/06 + 07x_1 + S0,把 state.md 按 8 节整个重写了。

看到了什么(都已带数字写进 state.md §2):
- 第一条基准「原式 + 多头最优半衰期(hl 20)」= 多头腿净超额 −4.6% / +0.2%,纯多头夏普 −1.76 / +0.09。
  半衰期从 0 拉到 20 把净超额从 −13.5% 改善到 −4.6%,但毛超额反而从 −2.4% 变到 −3.5% ——
  改善全部来自换手下降(17% → 1.4%),平滑省得下成本,省不出一条本来不存在的多头腿。
- 钱全在空头腿(hl 1 空头腿毛超额 +34.4% / +28.4%),而且 x1 证明它一半是「次日一字开盘买不进」撑出来的:
  换成原始标签,多空夏普 2.55 → 0.35(train)。多头腿几乎不受标签影响(−4.6% → −5.0%)。
- 多头腿为负的机制已经查清:ε=1e-6 把封板日变成 10³~10⁵ 的爆炸;而「负向爆炸」不是跌停,是「一路爬升到涨停」
  (gap_d < −20 的日子当日收益中位数 +9.97%)。两种爆炸之后都大幅跑输(−55.6% / −35.1%),
  但减法把负爆炸那一类送到了多头端 —— Q10 里 15.6% 是负爆炸票,按 −35.1% 估算拖掉约 5.5 个点,
  正好是 Q10(−3.6%)与 Q9(+5.0%)之间差距的大半。这是 H11。
- x1 的 13 个 numpy 重构里没有一个在 train 上有像样的多头腿(最好的「规则日 up+dn」+3.6%、夏普 0.46),
  而 ctl_price 自己在 valid 上就是 +11.3% —— 各变体 valid 上的 +7%~+12% 是 22~23 低价/低波风格,不是这棵树的信息。
- 对已知家族:原式和它的规则部分都「拖累」家族多头腿(+12.6% → +10.6%),只有「只留爆炸日」那一小块 +1 个点。

判断:倾向性结论是分辨(多头腿不可用 + 对已知家族无增量),但还缺两块坐实的证据,所以这一轮不下结论。
缺口一是口径:x1 全是 numpy 重构、方向与半衰期是脚本自己选的,官方引擎口径(含费用、可买入标签、门槛)要复核 ——
而 S1_nodes + S2_family 已经在服务器上跑着了(tag S1_S2,14 个变体),结果至今无人读。
缺口二是决定性问题:「相对已知家族有没有增量」x1 只做了粗糙的秩相加,没有配对差、没有标准误、没有残差多头腿,
所以那 +1 个点到底是信号还是噪声现在说不清。

决定做什么:工单 R1(kind: experiment),0 次新服务器运行 + 1 支自写脚本。
(A) 收 S1_S2 读出来,重点三件事 —— a_sum(sub→add)在同一半衰期下的多头腿与 Q10(裁决 H11,这是唯一可能走到提纯的路径);
    a_eps3/a_sig 的空头腿塌不塌(裁决 H1 的规则 vs 事件);b_lvl/b_lvlq 与 ctl_price 的相关与残差(裁决 H13)。
    特别要了「全部变体在 hl 20 下」的固定半衰期表 —— 这是区分结构改进与平滑改进的唯一归因依据。
(B) 自写脚本 x2 量增量:残差多头腿、秩相加的配对差 ± t 统计量、家族多头十分位里事件票占比、直接排除实验。

决定不做什么(理由写进 state.md §6):不深挖空头腿(用户纯多头做不了,且一半是买不进的假象);
不重跑窗口/半衰期扫描(H8 已定,5~60 天没差别);不做第二轮折叠/非线性变换(x1 的折叠版 train +3.3%、valid −6.2%,
符号都不稳,问题在剖面本身不可交易);不去修买不进标签(平台口径,只在报告里打折扣)。

R2 的判据事先写下了:a_sum 在 hl 20 下 train 多头腿 ≥ +5% 且 Q10 不再为负 → 进 S3 提纯;
train 多头腿 < +3% 或与 ctl_price 相关 ≥ 0.5 → 直接进读留出段,结论写分辨。

### 2026-10-04 13:25 [执行] 本轮因用户额度紧急中止,R1 未展开

响应用户直接指令「快写 state.md,马上就要没有额度了」,这一轮执行只读了 state.md 与工单 `R1.md`,
**没有**按 R1 收 `S1_S2`、也没有写/跑 `x2_incremental`。在 state.md 末尾加了一条附注说明此事,
state.md 第 1~7 节(主研本轮原文)未改动一字。`results/` 仍为空,R1 原样待办,下一位执行从 A/B 两步开始即可。

### 2026-10-04 13:41 [auto] S1_S2 跑完(exit 97);重看结果:logs/F109_erm_mag_gap_5m_tsm20_S1_S2.log

## 工单与结果卡(`notes/F109_erm_mag_gap_5m_tsm20/orders/`、`notes/F109_erm_mag_gap_5m_tsm20/results/`)

- R1:工单 有,结果卡 **还没有(待执行)**

## 配置里的实验计划(`configs/F109_erm_mag_gap_5m_tsm20.yaml`)

- 标题:5 分钟收益的上尾 / 下尾超阈均值比之差的 20 日均值;分母上的 1e-6 把涨跌停封板日变成事件记忆
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base
- **S1_nodes**(8 个变体):两本书各自由哪个节点决定:分母上的 ε(封板日的爆炸)、减法、上侧还是下侧、5 分钟对 1 分钟的尺度?
  a_eps3、a_sum、a_up、a_dn、a_1m、a_q5、a_evt、a_sig
- **S2_family**(6 个变体):规则区间是不是「偏度 / 彩票 / 低价」的另一种写法?多头腿在两侧的水平里还是在两侧的差里?
  b_skew1、b_skew5、b_max20、b_lvl、b_lvlq、b_sig60

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F109_erm_mag_gap_5m_tsm20`)

- `S0_baseline`  10-04 11:54  1 个变体  → `./scripts/study.sh digest F109_erm_mag_gap_5m_tsm20 S0_baseline`
- `x1_anatomy`(自写脚本的输出)  10-04 12:36  exit 0  → `logs/F109_erm_mag_gap_5m_tsm20_x1_anatomy.log`
- `S1_S2`(自写脚本的输出)  10-04 13:19  exit 97  → `logs/F109_erm_mag_gap_5m_tsm20_S1_S2.log`

## 已写的 notes(`notes/F109_erm_mag_gap_5m_tsm20/`)

- `02_operators.md`  2800 字节  10-04 13:01
- `03_decomposition.md`  2451 字节  10-04 13:01
- `04_grammar.md`  1821 字节  10-04 13:01
- `05_hypotheses.md`  15885 字节  10-04 13:21
- `06_baseline.md`  3350 字节  10-04 13:01
- `07x_1_anatomy.md`  10490 字节  10-04 12:46
- `journal.md`  4821 字节  10-04 13:41
- `state.md`  28898 字节  10-04 13:31

## 自写的探针与分析脚本(`studies/F109_erm_mag_gap_5m_tsm20/`)

- `x1_anatomy.py`  10-04 12:17  F109 x1: what the tree is really ranking -- the epsilon blow-up anatomy.

## 结构化结果(`handoff/F109_erm_mag_gap_5m_tsm20/results/`)

(还没有)
