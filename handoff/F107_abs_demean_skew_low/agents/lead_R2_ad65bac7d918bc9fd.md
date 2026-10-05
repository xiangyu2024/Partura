# lead:F107_abs_demean_skew_low#2 — agent ad65bac7d918bc9fd(工作流 wf_48864a04-f0a)

- 状态:**已返回结果**;开始 10-04 14:20,最后一次动作 10-04 14:43;工具调用 27 次
- 这是从 agent 的对话记录里**自动抽出来的动作流水**(命令、输出、写了哪些文件)。agent 的推理不在记录里 ——
  它的判断要看 `notes/F107_abs_demean_skew_low/journal.md` 和各 notes 文件。输出过长的地方截了中间。

## 动作流水

**10-04 14:20 · agent 的话**

I'll start by getting the full picture of this factor's research state.

**10-04 14:20 · Bash** — Get research brief for factor

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh brief F107_abs_demean_skew_low
```

```
# F107_abs_demean_skew_low — 交接状态

_自动生成于 2026-10-04 14:20(`python scripts/recorder.py --brief F107_abs_demean_skew_low` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #613(批次 B01_single_factors)
- 表达式:`abs_(cs_demean(day_skew(Low)))`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- 留出段:**还没读过**(只能读一次;读之前要在 `10_distilled.md` 里写下候选排序和判据)。
- agent `study:F107_abs_demean_skew_low#3`(wf_759ef2d3-03f):失败,几乎没做事(不用看)
- agent `study:F107_abs_demean_skew_low`(wf_08351f46-81b):中断,最后动作 10-04 13:10 → `handoff/F107_abs_demean_skew_low/agents/study_aeee08397f02b3dd8.md`
- agent `lead:F107_abs_demean_skew_low#1`(wf_3cafb924-05e):已返回结果,最后动作 10-04 13:23 → `handoff/F107_abs_demean_skew_low/agents/lead_R1_a64a56e1b6b3aac64.md`
- agent `work:F107_abs_demean_skew_low#1`(wf_3cafb924-05e):失败,最后动作 10-04 13:29 → `handoff/F107_abs_demean_skew_low/agents/work_R1_a25e6a62e8c78cd9d.md`
- agent `work:F107_abs_demean_skew_low#1`(wf_3cafb924-05e):失败,几乎没做事(不用看)
- agent `lead:F107_abs_demean_skew_low#1`(wf_48864a04-f0a):已返回结果,最后动作 10-04 13:52 → `handoff/F107_abs_demean_skew_low/agents/lead_R1_a5a61945b977394a6.md`
- agent `work:F107_abs_demean_skew_low#1`(wf_48864a04-f0a):已返回结果,最后动作 10-04 14:19 → `handoff/F107_abs_demean_skew_low/agents/work_R1_aa46cb6dfc1b77c78.md`
- agent `lead:F107_abs_demean_skew_low#2`(wf_48864a04-f0a):还在跑(如果这就是你自己,不用看它的流水)

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F107_abs_demean_skew_low` 看服务器上的 tag,`./scripts/study.sh digest F107_abs_demean_skew_low <tag>` 重看结果)。

## 研究现状(`notes/F107_abs_demean_skew_low/state.md`,10-04 13:51 更新)—— **先读这个文件**

# F107_abs_demean_skew_low — 研究现状

> 主研第 1 轮写(Opus 5,2026-10-04;**这是第 1 轮的第二次上岗** —— 第一次下完 R1 之后执行被额度中断,
> R1 一张结果卡都没有,所以本轮仍算第 1 轮,工单号仍是 R1,没有新开工单)。
> 这一页**整页覆盖重写**,覆盖了我自己上一次写的那一版和之前那份 `scripts/autostate.py` 自动汇编的版本。
> 判断的依据:`02_operators.md` / `03_decomposition.md` / `04_grammar.md` / `05_hypotheses.md` / `06_baseline.md` /
> `07x_1_anatomy.md`、`configs/F107_abs_demean_skew_low.yaml`、`studies/.../x1_anatomy.py`、`studies/.../x2_elevate.py`,
> 以及我这一轮自己用 `study.sh src` 核对的五个算子源码(见 §2.2,**本轮唯一的新事实都在那里**)。
> 表达式:`abs_(cs_demean(day_skew(Low)))`,来源 挖掘 #613。方向 −1(做多 `|B|` 小的),半衰期 20。

---

## 1. 一句话现状

**引擎的正式数字还一个都没有,但两个任务此刻正在服务器上跑。**
上一位研究员(Opus 5.5)把这棵树在 numpy 里探了一遍(tag `x1`,结论完整、指向明确且**是否定方向**),
启动了引擎阶段 run `S12`(S1_parts 11 个 + S2_memory 11 个变体),并写好了探针 `x2_elevate.py` 却从没跑过。
我上一次上岗下了 **R1**(收 S12、跑 x2、把 x1 的 numpy 读数和引擎数字逐个对照);执行把 **S12 和 x2 都启动了**
(服务器作业 `635384.pt_F107_S12`、`635516.pt_F107_x2`,10-05 04:29 服务器时间),**然后被额度中断,结果卡没写**。
我这一轮确认两个作业都还在跑,**没有新开工单**,把 R1 原样交回执行去收;另外做了一件只有主研该做的事:
**把五个载荷算子的源码核对了一遍**,排掉一个假 bug、给面板不一致立了第三条解释(§2.2 末尾)。
**下一步**:读 R1 的结果卡,裁决 H14(日内路径形状相对「日频 |特质收益|」有没有增量)和 H13(移心/倾斜的折叠能不能救多头腿)。
按现在的证据,**最可能的结局是「多头腿相对已知家族没有增量」这个否定性结论**,但要等 S12 的引擎数字和 x2 §b/§e 才能定。

---

(…全文 24164 字符,读 `notes/F107_abs_demean_skew_low/state.md`)

## 研究日志(`notes/F107_abs_demean_skew_low/journal.md`:8 条,其中研究员自己写的 3 条)

最近的 12 条(完整的看文件):

### 2026-10-04 12:42 [auto] 启动 run S12:阶段 S1_parts S2_memory

### 2026-10-04 13:23 [主研] 第 1 轮:x1 的 numpy 探路已指向否定结论,但没有一个引擎数字;下 R1 收 S12 + 跑从没跑过的 x2

**看到了什么。** 上一位研究员(Opus 5.5)在被换下之前做完了很多事:语义(02)、分布(03)、语法(04)、
开工前的 12 条竞争性假设(05)、S0 复现用户那一行(06)、以及一次把 12 条假设全扫一遍的 numpy 探针 x1(07x_1)。
x1 的指向非常明确,而且是**否定**的方向:
  - 两条腿是两种机制:空头腿在尾部(截尾/取秩 → 空头腿 +32.5→+17.5、多空 2.81→0.72;钉住日换中性值 → 只剩 +7.8),
    多头腿在主体(截尾/取秩后多头毛纹丝不动 +9.2~9.8/+11.9~12.3)。空头腿这一腿用户做不了。
  - H6 被否定(cs_demean 必需:去掉多头毛 9.4→3.4)、H5 被否定(折叠不对称,最优桶是 (−0.5,−0.25] 而非 0)、
    H7/H8 被否定、H9 对多头腿成立、H10 成立。
  - H11 成立但**归因是平滑**:窗口 10~60 把多头净超额抬到 +5~6%/+6.6~7.5%、夏普 1.0~1.2/1.5~1.7,
    **毛超额不升(train 还降 1~2 点)**,多出来的全部来自换手 10.9%→3~4%。
  - 最要紧的两条:S0 的「多头腿不被控制变量解释」是**线性单调控制变量造成的假象**(playbook §6.5)——
    换成同样折叠过的 `EMA20|去均值日收益|`(完全不看日内路径),一个变量 R² 0.307、残差多头毛只剩 +2.9;
    相对已知家族 K 基本没有增量(残差 +3.9/+1.4,相加净超额不升,**原式多头十分位里 K 最低的三分之一 −0.6%/−4.7%**)。

**判断。** 证据已经强到快可以下「多头腿相对已知家族没有增量」这个否定结论,但**现在还不能写**,因为有两个硬缺陷:
  (1) x1 全部是 numpy 探路,**引擎正式数字一个都没有**;而且 x1 自己承认引擎的 `cross_mean(原式,30)` 与
      滚动 nanmean 不是同一个面板(Spearman 0.9989、最大差 12.6)—— 偏偏时间尺度表(= 候选名单所依赖的那张表)
      就是用滚动 nanmean 算的。拿它当结论等于拿探路当结论。
  (2) H5 被否定留下的结构线索(折叠的中心偏左、方向信息在多头一侧也有:低 |B| 里 EMA20(B)<0 的 +13.7/+11.6
      对 ≥0 的 +4.7/+7.2)是这棵树上**唯一还没试过**的提纯方向,而 `x2_elevate.py` 已经为它写好了 310 行却**从来没跑过**。
  另外运气不错:引擎阶段 run S12(S1_parts + S2_memory 共 22 个变体)已经启动、还在跑,结果没人读 —— 这一轮等于白捡。

**决定。** 这一轮不新开方向,下 R1(kind: experiment):收 S12、跑 x2、把 x1 的 numpy 读数和引擎数字**逐个对照**
(重点是 cross_mean 面板那条,x2 §a 和 S12 的 m* 要一起读)。新增两条假设作为下一轮的裁决点:
  - **H14(最要紧)**:日内路径形状相对「日频 |特质收益| + 同样记忆」没有增量 → 看 S12 的 m20 vs m20_absret、m60 vs m60_absret。
    差 ≤3 点或两段不同向 = H14 成立 = 这棵树的 241 根分钟最低价白读了,直接走读留出段 + 否定结论。
  - **H13**:移心/倾斜的折叠(|B−c| 或 |B|+λ·B)比 abs_ 更纯 → 看 x2 §b 在 train 定的 c/λ 在 valid 上是否复现。

**决定不做的事。** 不再追空头腿(用户做不了,机制已查清);不优化多空口径(选拔只看多头腿);
不碰 day_kurt / 日内相关这些对照变体的提纯(ρ 低或没有多头腿);不把窗口扩到 120 日以上(train/valid 不同向);
不做一字板 NaN/±1 的清理实验(格子 < 0.3% 且只影响空头腿);不重跑 S0 / S12 / x1。

state.md 已整页覆盖重写(8 节),05_hypotheses.md 末尾追加了「第 1 轮裁决」+ H13 / H14。

### 2026-10-04 13:29 [auto] 启动 run S12:阶段 S1_parts S2_memory

### 2026-10-04 13:29 [auto] 启动 exec x2:studies/F107_abs_demean_skew_low/x2_elevate.py

### 2026-10-04 13:52 [主研] 第 1 轮(第二次上岗):R1 没有结果卡、S12+x2 都还在服务器上跑,原样交回执行;等待期间核对算子源码,排掉一个假 bug、给面板不一致立了 H15

**情况。** 上一次我下完 R1,执行把 S12 和 x2 都启动了(服务器作业 `635384.pt_F107_S12`、`635516.pt_F107_x2`,
10-05 04:29 服务器时间),然后被额度中断,**一张结果卡都没写**。`study.sh list` 显示两个作业此刻都还在跑(Detached)。

**决定(主线)。** 按接力规矩,**最新工单还没有结果卡就不另开工单**。R1 的三件事(收 S12、收 x2、留一份 propose 草稿)
一条都没废,所以我**原样把 R1 交回执行**,返回 `{status: order, order: R1, kind: experiment}`。
本轮仍算第 1 轮;下一个主研看到 `results/R1.md` 存在时才是真正的第 2 轮。

**决定(顺手做的)。** 等待不是空等 —— 我用这段时间做了一件只有主研该做的事:**把载荷算子的源码核对了一遍**
(`study.sh src`:`cross_mean`、`nanmean_last`、`cross_delay`、`ts_delay`、`cs_demean`,外加 `x1_anatomy.py:104` 的 `roll_mean`)。
三条收获,全部写进了 state.md §2.2:

1. **排掉一个假 bug,而且是关键的那一个。** config 里 `ctl_rev1` 用 `ts_delay`,而 `r_absret` / `m20_absret` /
   `m60_absret` / `g_absidio20` 用 `cross_delay` —— 看着像不一致。源码里两者在 `d > 0` 时**逐行等价**
   (都是 `res[d:] = x[:-d]`、其余 NaN、axis=D)。**所以 H14 的对手变体是忠实的**,确实是「日频 |特质收益| + 同样记忆」。
   这条很要紧:H14 是全局最要紧的一条假设,要是对手变体算错了,下一轮的裁决全是垃圾。
   反过来也要紧 —— **执行千万不要去「统一」这两个写法**,改了就和 x1 的数字不可比;我在 R1 末尾的附录里专门写了这条。
   副作用记一笔:`cross_delay` 是**裸位移,不是「上一个有效观测」**,所以复牌日 `r_absret` 是 NaN 而不是大跳 ——
   `r_absret` 的覆盖面比原式窄,但 `m20_absret` 过了 `cross_mean` 之后基本补上了,**H14 的主比较(m20 vs m20_absret)不受影响**。

2. **把「引擎 cross_mean ≠ 滚动 nanmean」逼到了第三条解释,并立为 H15。**
   引擎 `cross_mean` = `rolling_reduce(x, d, nanmean_last, axis=0)`,窗口左侧 NaN 补齐、`nanmean` 跳 NaN、
   **`min_periods` 等于 1**(第 1 天就出值);x1 的 `roll_mean` 是 float64 cumsum 版的**同一个语义**(`k2 > 0.5` 才出值)。
   **所以不是 min_periods 的差别,也不可能是浮点误差**(float64 对 `|B| ≤ 15.4` 不会差到 12.6)——
   而 x2 §a 里写好的两个候选解释(「日历行」vs「去掉缺口」)**可能两个都对不上**。
   剩下的解释:`cross_mean(原式, …)` 里的原式是**引擎自己重算的**,被滚动的却是**缓存面板**;
   若引擎在表达式内部给 `cs_demean` 传了 universe/停牌 mask 而缓存面板没有,引擎那侧的 60 日窗口里可能**只剩 1 个有限值**
   (于是 cross_mean = 那一个值,可以是 12 以上)。这条同时解释了三个观测:Spearman 0.9989(主体一致)、
   0.27% 的**有限性**不一致、最大差 12.6(单观测窗口)。
   **判它的数 x2 §a 已经在印了**:8 个最大差格子的 `finite days in window`、`base today`,以及 `|diff|>0.05` 那段的
   `mean finite-days-in-window`(对比 all cells)、`share whose base is NaN today`。
   **个位数 → H15 成立**:不一致是上市/复牌边界伪影,只涉 0.27% 格子,**x1 的时间尺度表(= 候选名单所依赖的那张表)排序可信**;
   **几十天 → H15 被否定**:两个面板真是两个东西,2.3d 和候选名单都要用引擎数字重建。
   **这决定了下一轮先读哪张表**,所以我把它写成了 §6 的第一个分叉:先读 §a/H15,再读 H14。

3. `cs_demean` 的语义核对无误(减当天所有有限值的截面均值),证实 `02_operators.md`。

**决定不做的事。** 不新开工单、不新建阶段、不加变体、不改 config(尤其不去统一 `cross_delay`/`ts_delay`)、
不重跑 S12/x2(正在跑)、不去「修」面板不一致(那是取证对象 H15,不是 bug)、不碰别的因子的文件。
没有任何旧假设的状态因本轮而改变 —— 本轮没有新的实验结果,只有源码事实。

**落盘。** state.md 整页覆盖重写(8 节,新增 H15、把源码核对写进 §2.2 和 §3.4、把 §6 的读表顺序改成「先 §a 再 H14」);
R1 末尾追加「附录」一段:三条「别踩」(别统一 cross_delay、别修面板不一致、别替主研判断哪个面板是真的)
+ 一句「S12/x2 已在跑,直接 wait,不要重跑」—— **没有改 R1 要做的事**。

### 2026-10-04 13:59 [auto] S12 跑完(exit 0);重看结果:./scripts/study.sh digest F107_abs_demean_skew_low S12

### 2026-10-04 14:01 [auto] x2 跑完(exit 0);重看结果:logs/F107_abs_demean_skew_low_x2.log

### 2026-10-04 14:17 [执行] R1:S12(22变体)+x2(a-f六节)已收,均exit 0;结果卡写好,B/C两项数字有结构性缺口

做了什么:接手时 S12、x2 已在服务器跑(上一轮额度中断前起的),本轮未新起任何运行,只 wait+digest 收尾,
跑了一次 propose 草稿。写了结果卡 notes/F107_abs_demean_skew_low/results/R1.md 与三份事实类 notes
(07_S1_parts.md、07_S2_memory.md、07x_2_elevate.md)。

关键数字(全部在结果卡里逐项列出,这里只摘最关键的几个):
- H14(m20/m60 vs 对应的 absret 版本,净超额 tr/va):m20 +4.8%/+7.3% vs m20_absret +4.9%/+13.8%;
  m60 +5.6%/+6.5% vs m60_absret +6.2%/+14.8%。g_absidio20 的表达式与 m20_absret 逐字相同。
- H11 固定半衰期(hl20,train,净超额):v_base +1.1%,m10 +4.6%,m20 +4.8%,m30 +3.9%,m60 +3.3%,m120 +1.0%。
  但**这次引擎输出里没有 valid 侧的半衰期扫描、也没有跨变体同半衰期的"毛"超额**(JSON 的 sweep 只在 train、只有
  long_ann 没有 long_gross_ann)——工单 B 项要的"train 与 valid 都要"的毛/净/换手对照表,valid 那半、毛超额那列拿不到,
  已在结果卡 B 节写清楚,没有新起运行去补。
- C 项同理:g_absidio20/g_kurtlow20/known_stdamt_mean30 不在标准 diagnostics.neutralise 里(gates 本来就不自动进这张表),
  用 x1/x2 的替代数字顶上了(v_base 对 g_absidio20 残差多头毛 +2.9%;m20/m60 对 kurtLow 残差多头毛 +11.3%/+9.2%)。
- H15(x2 §a 取证):cross_mean 面板差集中在"窗口内仅 1 个有限观测"的边界格子,0.27% 的格子 |diff|>0.05,涉及 798 只股票;
  但 m10~m120 的 book 级 Lnet,x1 numpy 与引擎的差全部 ≤0.6pp(在 ±3pp 噪声带以内)。两套数字都抄进了结果卡,没有替主研判哪个面板对。
- H13(x2 §b):mean20(|B|+λB) train 选 λ=+0.6(+7.8%),这个 λ 在 valid 只有 +1.4%;valid 自己在同一网格里最好是 λ=−0.3(+6.7%),
  方向相反。mean60 的版本没有这个问题。
- x1 vs 引擎:p_signed/p_close/r_kurtret/r_kurtlow/r_mktcorr 逐位对齐;p_nodemean/p_rank 的空头腿、多空夏普差 1.4pp/0.06~0.23,
  差异来源不明;m10~m120 差 ≤0.6pp。

## 工单与结果卡(`notes/F107_abs_demean_skew_low/orders/`、`notes/F107_abs_demean_skew_low/results/`)

- R1:工单 有,结果卡 有

## 配置里的实验计划(`configs/F107_abs_demean_skew_low.yaml`)

- 标题:日内价格水平占用分布的偏度偏离全市场多少(折叠) —— 空头腿是封板/跳价事件,多头腿是「安静且随大盘走」的股票
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base
- **S1_parts**(11 个变体):原式三个节点(偏度、截面去均值、折叠)和字段各自是不是必需的?它是不是「日频 |特质收益|」「分钟收益峰度」这类朴素读数的另一种写法?
  p_signed、p_nodemean、p_znorm、p_close、p_range、p_rank、p_cube、r_absret、r_kurtret、r_kurtlow、r_mktcorr
- **S2_memory**(11 个变体):把日轴记忆写进表达式之后,多头腿净超额的改善有多大、来自平滑还是结构?记忆该是均值、中位数还是极值,窗口多长最稳?
  m10、m20、m30、m60、m120、md60、mr60、mx20、m60_nodemean、m20_absret、m60_absret

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F107_abs_demean_skew_low`)

- `S0_baseline`  10-04 11:50  1 个变体  → `./scripts/study.sh digest F107_abs_demean_skew_low S0_baseline`
- `S12`  10-04 13:59  22 个变体  → `./scripts/study.sh digest F107_abs_demean_skew_low S12`
- `x1`(自写脚本的输出)  10-04 12:31  exit 0  → `logs/F107_abs_demean_skew_low_x1.log`
- `x2`(自写脚本的输出)  10-04 14:01  exit 0  → `logs/F107_abs_demean_skew_low_x2.log`

## 已写的 notes(`notes/F107_abs_demean_skew_low/`)

- `02_operators.md`  3070 字节  10-04 12:55
- `03_decomposition.md`  2863 字节  10-04 12:55
- `04_grammar.md`  2218 字节  10-04 12:28
- `05_hypotheses.md`  10911 字节  10-04 13:22
- `06_baseline.md`  3894 字节  10-04 13:05
- `07_S1_parts.md`  8230 字节  10-04 14:10
- `07_S2_memory.md`  7803 字节  10-04 14:11
- `07x_1_anatomy.md`  10794 字节  10-04 13:06
- `07x_2_elevate.md`  14769 字节  10-04 14:12
- `journal.md`  11411 字节  10-04 14:17
- `state.md`  41025 字节  10-04 13:51

## 自写的探针与分析脚本(`studies/F107_abs_demean_skew_low/`)

- `probes.py`  10-03 17:50  Probes this tree needs: abs_(cs_demean(day_skew(Low))).
- `x1_anatomy.py`  10-04 12:16  x1 -- what  abs_(cs_demean(day_skew(Low)))  reads on REAL data, and where its long leg comes from.
- `x2_elevate.py`  10-04 12:44  x2 -- can the long leg of  abs_(cs_demean(day_skew(Low)))  be made better by STRUCTURE (not only by smoothing)

## 结构化结果(`handoff/F107_abs_demean_skew_low/results/`)

(还没有)
```

**10-04 14:20 · Bash** — List factor notes directory

```bash
cd /Users/wxy/Desktop/Partura && ls -la notes/F107_abs_demean_skew_low/ 2>/dev/null && echo "--- orders ---" && ls -la notes/F107_abs_demean_skew_low/orders/ 2>/dev/null && echo "--- results ---" && ls -la notes/F107_abs_demean_skew_low/results/ 2>/dev/null
```

```
total 264
drwxr-xr-x@ 15 wxy  staff    480 Oct  4 14:12 .
drwxr-xr-x@ 19 wxy  staff    608 Oct  4 13:07 ..
-rw-r--r--@  1 wxy  staff   3070 Oct  4 12:55 02_operators.md
-rw-r--r--@  1 wxy  staff   2863 Oct  4 12:55 03_decomposition.md
-rw-r--r--@  1 wxy  staff   2218 Oct  4 12:28 04_grammar.md
-rw-r--r--@  1 wxy  staff  10911 Oct  4 13:22 05_hypotheses.md
-rw-r--r--@  1 wxy  staff   3894 Oct  4 13:05 06_baseline.md
-rw-r--r--@  1 wxy  staff   8230 Oct  4 14:10 07_S1_parts.md
-rw-r--r--@  1 wxy  staff   7803 Oct  4 14:11 07_S2_memory.md
-rw-r--r--@  1 wxy  staff  10794 Oct  4 13:06 07x_1_anatomy.md
-rw-r--r--@  1 wxy  staff  14769 Oct  4 14:12 07x_2_elevate.md
-rw-r--r--@  1 wxy  staff  11411 Oct  4 14:17 journal.md
drwxr-xr-x@  3 wxy  staff     96 Oct  4 13:14 orders
drwxr-xr-x@  3 wxy  staff     96 Oct  4 14:16 results
-rw-r--r--@  1 wxy  staff  41025 Oct  4 13:51 state.md
--- orders ---
total 24
drwxr-xr-x@  3 wxy  staff     96 Oct  4 13:14 .
drwxr-xr-x@ 15 wxy  staff    480 Oct  4 14:12 ..
-rw-r--r--@  1 wxy  staff  10905 Oct  4 13:42 R1.md
--- results ---
total 72
drwxr-xr-x@  3 wxy  staff     96 Oct  4 14:16 .
drwxr-xr-x@ 15 wxy  staff    480 Oct  4 14:12 ..
-rw-r--r--@  1 wxy  staff  33411 Oct  4 14:16 R1.md
```

**10-04 14:20 · agent 的话**

R1 has a result card now — this is genuinely round 2. Let me read the state, the result card, and the hypothesis table.

**10-04 14:21 · Bash** — Read R1 result card

```bash
cd /Users/wxy/Desktop/Partura && cat notes/F107_abs_demean_skew_low/results/R1.md
```

```
<persisted-output>
Output too large (32.6KB). Full output saved to: /Users/wxy/.claude/projects/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/tool-results/brtsh2txp.txt

Preview (first 2KB):
# 结果卡 R1

factor_id: F107_abs_demean_skew_low · 工单: `orders/R1.md`(kind: experiment) · 执行: Sonnet 5 · 2026-10-04

## 做了什么

工单要求的三件事,**接手时 S12 与 x2 已经在服务器上跑着**(上一位执行在额度中断前启动的,`635384.pt_F107_S12`、`635516.pt_F107_x2`,
10-05 04:29 服务器时间)。本轮没有新启动任何服务器运行,只做了"收"的部分:

| 项 | tag | 动作 | 结果 |
|---|---|---|---|
| 1 | `S12` | `./scripts/study.sh wait F107_abs_demean_skew_low S12 540`(未重跑) | exit 0,10-05 04:59:30 完成,482.2s,device=cuda,peak anon 6.98G |
| 2 | `x2` | `./scripts/study.sh wait F107_abs_demean_skew_low x2 540`(未重跑、未改脚本) | exit 0,10-05 05:01:06 完成,共 1883s(含 guard 排队等 run slot 1485s),真实服务器数据(非 `--mock`) |
| 3 | — | `./scripts/study.sh propose F107_abs_demean_skew_low` | 输出 12 条候选草稿,见文末,**未经主研裁决** |

**没做成 / 需要主研知道的偏差**(详见下面"没人要但值得注意的"与各小节标注):

- x2 没有报错、没有 traceback,**不需要任何最小修复**;脚本逻辑未改一字。
- 工单 B 项("固定半衰期表…train 与 valid 都要")与 C 项(gates 的中性化残差)在这次 S12/x2 的输出里**并不完整**,
  不是我漏抓,是引擎这次产出的数据结构本身就没有这两样东西(见 B、C 节的说明)。我没有为了补全它们新起任何服务器运行
  (工单把新启动的运行限定在 x2 这一次),只如实报告缺口、并给出能找到的最接近的替代数字。
- `configs/F107_abs_demean_skew_low.yaml`、`studies/F107_abs_demean_skew_low/x1_anatomy.py`、`x2_elevate.py` 一字未改。
- 另补了三份事实类 notes(只写事实,解读留白):`07_S1_parts.md`、`07_S2_memory.md`、`07x_2_elevate.md`。

---

## 工单要的数字

### A. S12 主表(22 个变体:S1_parts 11 + S2_memory 11)

**决策口径**(方向/半衰期在 train 上定;Lnet=多头腿净超额,Lgross=多头腿毛超额,Lshp=纯多头夏普,LTO=多头日换手,
Lmdd=多头最大回撤,short=空头腿毛超额(train),hlS/LS=多空口径半衰期与扣费多空夏普,ρ=与 v_base 可交易信号的日截面 rank 相关(train)):

| variant | hlL | Lnet tr | Lnet va | Lgross tr | Lgross va | Lshp tr | Lshp va | LTO | Lmdd tr | Lmdd va | hlS | LS tr | LS va | short tr | ρ(v_base) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| p_signed | 20 | −30.1% | −36.6% | −22.1% | −27.1% | −3.88 | −5.36 | 10.5% | −119.1% | −56.7% | 20 | −2.31 | −4.02 | +11.1% | −0.1036 |
| p_nodemean | 20 | −5.6% | −5.0% | +3.5% | +3.8% | −1.15 | −0.87 | 12.1% | −23.9% | −13.2% | 20 | +2.11 | +1.62 | +32.8% | +0.9029 |
...
</persisted-output>
```

**10-04 14:21 · Bash** — Read state.md

```bash
cd /Users/wxy/Desktop/Partura && cat notes/F107_abs_demean_skew_low/state.md
```

```
<persisted-output>
Output too large (40.1KB). Full output saved to: /Users/wxy/.claude/projects/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/tool-results/bu9w2yyis.txt

Preview (first 2KB):
# F107_abs_demean_skew_low — 研究现状

> 主研第 1 轮写(Opus 5,2026-10-04;**这是第 1 轮的第二次上岗** —— 第一次下完 R1 之后执行被额度中断,
> R1 一张结果卡都没有,所以本轮仍算第 1 轮,工单号仍是 R1,没有新开工单)。
> 这一页**整页覆盖重写**,覆盖了我自己上一次写的那一版和之前那份 `scripts/autostate.py` 自动汇编的版本。
> 判断的依据:`02_operators.md` / `03_decomposition.md` / `04_grammar.md` / `05_hypotheses.md` / `06_baseline.md` /
> `07x_1_anatomy.md`、`configs/F107_abs_demean_skew_low.yaml`、`studies/.../x1_anatomy.py`、`studies/.../x2_elevate.py`,
> 以及我这一轮自己用 `study.sh src` 核对的五个算子源码(见 §2.2,**本轮唯一的新事实都在那里**)。
> 表达式:`abs_(cs_demean(day_skew(Low)))`,来源 挖掘 #613。方向 −1(做多 `|B|` 小的),半衰期 20。

---

## 1. 一句话现状

**引擎的正式数字还一个都没有,但两个任务此刻正在服务器上跑。**
上一位研究员(Opus 5.5)把这棵树在 numpy 里探了一遍(tag `x1`,结论完整、指向明确且**是否定方向**),
启动了引擎阶段 run `S12`(S1_parts 11 个 + S2_memory 11 个变体),并写好了探针 `x2_elevate.py` 却从没跑过。
我上一次上岗下了 **R1**(收 S12、跑 x2、把 x1 的 numpy 读数和引擎数字逐个对照);执行把 **S12 和 x2 都启动了**
(服务器作业 `635384.pt_F107_S12`、`635516.pt_F107_x2`,10-05 04:29 服务器时间),**然后被额度中断,结果卡没写**。
我这一轮确认两个作业都还在跑,**没有新开工单**,把 R1 原样交回执行去收;另外做了一件只有主研该做的事:
**把五个载荷算子的源码核对了一遍**,排掉一个假 bug、给面板不一致立了第三条解释(§2.2 末尾)。
**下一步**:读 R1 的结果卡,裁决 H14(日内路径形状相对「日频 |特质收益|」有没有增量)和 H13(移心/倾斜的折叠能不能救多头腿)。
按现在的证据,**最可能的结局是「多头腿相对已知家族没有增量」这个否定性结论**,但要等 S12 的引擎数字和 x2 §b/§e 才能定。

---

## 2. 中间结果:已经量到的事实(每条带数字和出处)

### 2.1 S0_baseline(引擎,tag `S0_baseline`,出处 `06_baseline.md`)—— 唯一已有引擎数字的运行

- **复现成功**:用户表那一行(扣费多空夏普训练 2.89、多头腿毛超额 0.099)被 S0 在 utrain 上逐项复现(2.89 / 10.0%)。
  **用户表里的 `long: [0.099, 0.105]` 是毛超额,不是净超额** —— 别拿它和净超额比。
- 决策口径(方向/半衰期在 train 上定,`rank_by: long`):半衰期 **20**(多头口径与多空口径选到同一个)。
  - 多头腿**毛**超额 train **+9.4%** / valid **+11.4%**;多头书日换手 **10.9%** → 成本约 8.2 个点;
  - 多头腿**净**超额 train **+1.1%** / valid **+3.0%**;纯多头夏普 **0.24 / 0.69**。
  - **→ 原式照现在的样子,对只能做多的用户基本不可用。毛超额在那里,问题全在换手。**
- **半衰期顶在可选集合的上界**:净超额 hl0 −63.2% / hl2 −23.5% / hl5 −10.2% / hl10 −3.1% / hl20 **+1.1%**,单调改善到 20 为止;
  衰减表 rank IC h1 0.034 → h5 0.049 → h20 **0.062**。树里**没有任何日轴算子**,记忆全在表达式外面。这是个慢变量,20 还不够长。
- **钱在空头腿**:多头腿毛 +9.4%、空头腿毛 **+32.5%**,多头只占毛价差的 22%(valid 27%)。
...
</persisted-output>
```

10-04 14:21 · 读 `/Users/wxy/.claude/projects/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/tool-results/brtsh2txp.txt`

**10-04 14:22 · agent 的话**

Let me read the state file and the x2 probe notes in full.

10-04 14:22 · 读 `/Users/wxy/.claude/projects/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/tool-results/bu9w2yyis.txt`

**10-04 14:22 · Bash** — Read x2 elevate notes

```bash
cd /Users/wxy/Desktop/Partura && sed -n '1,400p' notes/F107_abs_demean_skew_low/07x_2_elevate.md
```

```
### x2:多头腿能不能靠结构(不只是平滑)提纯(`studies/F107_abs_demean_skew_low/x2_elevate.py`,tag `x2`,10-05 05:01 完成,exit 0,真实服务器数据,非 `--mock`;只切 utrain 行)

只写事实与表,解读留给主研(见工单 `orders/R1.md` 与结果卡 `results/R1.md`)。完整 stdout 在 `logs/F107_abs_demean_skew_low_x2.log`(202 行)。

#### a. 取证:引擎 `cross_mean(base, 60)` 与缓存 base 面板的 numpy 滚动 nanmean 是不是同一个面板

- 按日历行滚动 nanmean(核源码写法):两边都有限的格子 5,312,401;仅引擎有限 262;仅 numpy 有限 24,927。
  `|diff|` 分位:q0.5=8.02e-05、q0.9=0.000325、q0.99=0.0352、q0.999=0.244、q1=12.6;>1e-3 占 7.63%;>0.05 占 0.31%;Spearman 0.99905。
- 按"最近 60 个有限观测"(去掉缺口)滚动:两边有限 5,301,168;仅引擎有限 11,495;仅 numpy 有限 39。
  `|diff|` 分位:q0.5=8.32e-05、q0.9=0.00286、q0.99=0.0475、q0.999=0.322、q1=15.6;>1e-3 占 10.88%;>0.05 占 0.90%;Spearman 0.99777。
- 8 个最大差的格子(日历行版本)全部满足:该格子窗口内只有 **1 个**有限观测(`finite days in window 1`),`base today` 当天是 NaN,
  例如 20200828/605333.SH:engine 2.813 vs numpy 15.451(window mean 15.451,即窗口内唯一的有限值);20180723/002932.SZ 等同理。
- `|diff| > 0.05` 的格子共 16,724 个:其 mean finite-days-in-window 为 19.4(全部格子的均值是 58.1,即这些格子窗口内观测明显更稀疏);
  这些格子里 base 当天是 NaN 的占 14.8%;engine 比 numpy 大的占 27.5%。涉及 798 只股票,出现最多的 5 只:
  002210.SZ(154)、600078.SH(153)、000820.SZ(150)、002656.SZ(139)、002219.SZ(136)。

#### b. 移心 `|B − c|` 与倾斜 `|B| + λ·B`(numpy 重算书,半衰期网格同原式)

20 日滚动均值:

| 折叠 | hlL | Lnet tr | Lnet va | Lshp tr | Lshp va | Lgross tr | Lgross va | LTO | hlS | LS tr | LS va | short tr | ρ(v_base) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mean20\|B−(−0.6)\| | 5 | +7.4% | −0.7% | +1.71 | −0.12 | +12.1% | +3.9% | 6.2% | 2 | +3.74 | +1.52 | +28.2% | +0.64 |
| mean20\|B−(−0.4)\| | 5 | +7.7% | +2.2% | +1.80 | +0.44 | +12.2% | +6.7% | 6.0% | 1 | +3.73 | +2.15 | +31.5% | +0.74 |
| mean20\|B−(−0.2)\| | 5 | +6.9% | +4.6% | +1.57 | +1.02 | +11.3% | +8.9% | 5.8% | 1 | +3.74 | +2.54 | +33.5% | +0.83 |
| mean20\|B−0\|(=m20 的 numpy 版) | 20 | +5.0% | +7.5% | +1.01 | +1.74 | +7.1% | +9.6% | 2.7% | 2 | +3.19 | +2.96 | +30.1% | +0.92 |
| mean20\|B−(+0.2)\| | 20 | +1.9% | +6.3% | +0.36 | +1.48 | +3.9% | +8.6% | 2.8% | 1 | +2.46 | +2.72 | +32.6% | +0.88 |
| mean20(\|B\|−0.3B) | 20 | +2.3% | +6.7% | +0.44 | +1.51 | +4.4% | +9.0% | 2.8% | 1 | +2.31 | +2.79 | +32.7% | +0.88 |
| mean20(\|B\|+0.3B) | 10 | +6.7% | +5.8% | +1.46 | +1.30 | +9.8% | +8.9% | 4.1% | 2 | +3.64 | +2.35 | +28.0% | +0.86 |
| mean20(\|B\|+0.6B) | 2 | +7.8% | +1.4% | +1.86 | +0.27 | +14.3% | +7.8% | 8.6% | 2 | +3.27 | +0.95 | +23.4% | +0.66 |
… (95 行略) …
| mean60\|B−(−0.4)\| | +0.333 | 0.117 | +5.2%/+1.16/+9.4%/5.5%/+2.70/−3.0% | −8.4%/−1.53/−4.0%/5.9%/−1.93/−15.0% | +19.1%/+3.33/+22.1%/4.0%/+4.50/−3.5% | +21.1%/+3.51/+23.8%/3.5%/+4.48/−3.9% | +27.0% +28.9% +23.9% | 0.119,+25.4% vs +26.7% |
| mean20(\|B\|+0.3B) | +0.334 | 0.119 | +5.8%/+1.30/+8.9%/4.2%/+2.39/−4.9% | −7.2%/−1.40/−3.9%/4.5%/−1.89/−13.3% | +18.8%/+3.33/+21.4%/3.5%/+4.25/−3.5% | +21.0%/+3.52/+23.5%/3.3%/+4.25/−4.0% | +28.6% +27.6% +23.7% | 0.116,+27.7% vs +26.5% |
| corr60(A_i,μ) | +0.386 | 0.155 | +11.1%/+2.05/+14.1%/3.9%/+1.70/−4.9% | −6.8%/−1.12/−3.2%/4.8%/−1.45/−12.8% | +19.7%/+3.17/+22.1%/3.2%/+3.30/−4.0% | +20.9%/+3.27/+23.2%/3.0%/+3.37/−4.4% | +26.9% +28.1% +23.5% | 0.107,+24.0% vs +26.4% |
| resid(mean20\|B\|~kurtLow) | +0.382 | 0.147 | +8.9%/+2.11/+15.9%/9.3%/+1.66/−4.3% | −5.9%/−1.66/+1.2%/9.4%/−2.00/−10.0% | +19.1%/+3.22/+23.7%/6.1%/+3.54/−5.3% | +20.8%/+3.36/+24.6%/5.1%/+3.75/−5.1% | +25.4% +26.2% +28.3% | 0.081,+27.1% vs +26.6% |

(列顺序:Lnet/Lshp/Lgross/LTO/LS/Lmdd)

#### f. 逐年(utrain;多头腿净超额 / 纯多头夏普 / 多头换手)

| signal | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 |
|---|---|---|---|---|---|---|
| base EMA20(=v_base) | +4.1%/0.97/11.0% | +2.3%/0.60/10.9% | +1.8%/0.30/11.0% | −4.0%/−0.81/11.3% | +0.5%/0.13/11.3% | +6.8%/1.54/11.3% |
| K(known_stdamt_mean30) | +17.3%/2.81/4.3% | +10.2%/1.92/3.4% | +6.6%/0.78/3.4% | +16.0%/2.01/2.9% | +24.6%/3.69/2.8% | +18.3%/3.01/3.1% |
| engine m20 @hl20 | +7.6%/1.82/3.0% | +3.6%/0.91/2.9% | +4.3%/0.71/2.9% | +3.2%/0.58/2.9% | +3.7%/0.89/3.0% | +12.9%/2.94/3.1% |
| engine m60 @hl3 | +6.6%/1.51/4.0% | +4.9%/1.26/3.4% | +4.9%/0.79/3.4% | +5.6%/1.03/3.4% | +3.5%/0.82/3.6% | +11.4%/2.67/3.6% |
| 0.5rank(m60)+rank(K) | +18.5%/3.17/3.8% | +10.5%/2.22/3.3% | +9.8%/1.28/3.2% | +15.0%/1.89/3.0% | +22.3%/3.68/3.2% | +19.1%/3.29/3.2% |
| rank(m60)+rank(K) | +16.8%/2.93/3.7% | +9.4%/1.98/3.3% | +9.7%/1.29/3.1% | +14.5%/1.84/3.0% | +20.9%/3.63/3.3% | +18.6%/3.41/3.3% |
| engine m120 @hl3 | +7.1%/1.55/3.0% | +2.9%/0.72/2.1% | +2.6%/0.45/2.3% | +3.1%/0.53/2.2% | +6.9%/1.54/2.4% | +14.0%/3.14/2.3% |

来源:`logs/F107_abs_demean_skew_low_x2.log`(202 行,exit 0,1883s,guard 排队 1485s 后拿到 slot)。
```

**10-04 14:22 · Bash** — Read playbook section 6

```bash
cd /Users/wxy/Desktop/Partura && wc -l docs/study_playbook.md && sed -n '/^## *6/,/^## *8/p' docs/study_playbook.md | head -150
```

```
     279 docs/study_playbook.md
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
5. **秩空间的线性中性化看不见非单调关系**。因子里有 `abs_`、`cs_demean` 后取绝对值、平方这类折叠时,
   它和任何单调控制变量的 rank 相关都接近 0、R² 很低 —— 这不说明它不是已知暴露。要用**同样折叠过的控制变量**去量。
6. **空头腿被「买不进的票」抬高**。次日开盘封涨停的票标签是 NaN,在空头里记 0 收益。涨停、一字板相关的因子
   (峰度、集中度、极端收益类)空头腿和多空夏普会因此虚高 0.5 以上 —— 用 `st.target(buyable=False)` 按**收益贡献**去量。
   (这只影响多空口径;多头腿不受影响,这也是选拔看多头腿的又一个理由。)
7. **分桶变量是内生的**。用「当天成交额」去给一个「放量事件」分桶,事件本身就把股票送进了最高一桶。
   条件 IC 要用不被因子自身污染的变量(更长窗口的水平、滞后值)。
8. **数字张冠李戴**:把别的变体的性质写到原式头上、把 utrain 的数当成 valid 的、把毛超额当成净超额。
   写完 notes 逐个对一遍表。

---

## 7. 研究日志与交接(用户 2026-10-04 要求:研究必须随时能被别人接上)

研究可能在任何一步被打断(额度用尽、断网、机器休眠),接手的很可能是**另一个模型**,它对你做过什么一无所知。
… (19 行略) …
4. **三个必须落盘的时点**(各记一条日志):
   ① 假设表定稿(跑第一个实验之前);
   ② **读留出段之前** —— 候选、排序、判据写进 `10_distilled.md`,**然后**才 `final`;
   ③ 读完留出段 —— 每条判据是过了还是被否定,推荐是谁。
5. **收尾**:返回结构化结果之前,最后记一条「研究完成:推荐 X(半衰期 …),理由 …;未决的是 …」。
6. **研究现状 `notes/<fid>/state.md`** —— 日志是流水(只追加),这一页是「现在的理解」(每次**整个覆盖重写**),接手的人最先读它。
   每看完一个结果就更新。固定 8 节,宁可啰嗦:
   1) 一句话现状;2) 中间结果:量到的事实,每条带数字和出处(tag / 脚本 / 变体 / 哪一段 / 哪种口径);
   3) 研究过程与逻辑:做了什么、为什么这么走、源码里和名字不一样的地方;
   4) **假设表**:编号 | 假设 | 状态(未验证 / 被支持 / 被否定 / 已改写)| 证据与出处 | 还差什么才能定;
   5) 当前的候选(提纯 / 升华):表达式、train/valid 多头口径数字、为什么是它;已排除的候选与原因;
   6) **后面的研究思路**:按顺序,每步做什么、想回答什么、哪种结果意味着什么;明确决定不做的事和原因;
   7) 留出段:未读 / 已读(读前登记在哪);8) 给接手者的提醒:工具的坑、还没看结果的任务、写了一半的文件。
7. **分层接力**(用户定的分工,见 `handoff/README.md`):「主研」(Opus 5)管思路 —— 假设、裁决、设计实验、选候选、下结论,
   把要做的事写成工单 `notes/<fid>/orders/R<n>.md`;「执行」(Sonnet 5)管实现 —— 写配置和脚本、跑服务器、读结果,
   写成结果卡 `notes/<fid>/results/R<n>.md`。每一轮都是新的 agent,彼此只靠这些文件传话。工单要写到执行不需要猜
   (完整表达式、要带回来的每个数字);结果卡只写事实和异常,不替主研下结论。
8. `handoff/` 不用你管:后台记录器(`scripts/recorder.py`,不依赖任何模型和额度)会把你返回的结构化结果
   (`handoff/<fid>/results/`)、你的动作流水(`handoff/<fid>/agents/`)和交接页(`handoff/<fid>/STATE.md`)自动存下来。
   批次的总体进度在 `handoff/STATUS.md`,怎样重启在 `handoff/README.md`。
```

**10-04 14:24 · agent 的话**

Now let me check the config, the final-stage mechanics, and whether a rank-blend is expressible in the grammar.

**10-04 14:24 · Bash** — Read playbook sections 0-4

```bash
cd /Users/wxy/Desktop/Partura && sed -n '1,120p' docs/study_playbook.md
```

```
# 一次研究的操作手册(给做研究的 agent)

先读 `CLAUDE.md` 和 `docs/method.md`(为什么每条表达式都要重新推计划)。这份讲**怎么干**:
口径、工具、规矩、踩过的坑、要交什么。范例是 `research/alpha_distillation/F001_dwgated_covamtlow.md`
和 `notes/F001_dwgated_covamtlow/` —— 看它的**论证方式**(每个结论后面跟着哪个实验),不要抄它的实验清单。
(F001 用的是旧口径:普通标签 + 多空夏普;**现在的口径以本文为准**。)

---

## 0. 目标:提纯、分辨、升华

| | 要回答的问题 | 算做到了 |
|---|---|---|
| **分辨** | 这东西到底是什么?是不是某个已知暴露(成交额水平、规模、换手率、波动、动量、反转)换了个写法?和这批其他因子、和已知家族是不是同一个? | 有中性化的 R² 和残差表现、有 rank 相关、有"把可疑节点换成它的朴素等价物"的直接替换实验 |
| **提纯** | 预测力在树的哪一部分?哪些节点、指数、窗口、字段是多余的? | 给出一个**更小**的结构,在 train 和 valid 上保住(或超过)原式;每删一个节点都有实验 |
| **升华** | 看懂机制之后,能不能写出一个**更好用**的版本? | 见下面的"选拔口径" |

### 选拔口径(用户 2026-10-04 明确定的,不要改)

**用户做的是 A 股纯多头,空头腿做不了。所以选拔只看一件事:多头腿扣费之后能拿到多少。**

1. **第一判据:多头腿净超额(扣 15 bp)与纯多头夏普**,半衰期按**纯多头书**在 fit 段选(`rank_by: long`)。
2. **半衰期是可以调的杠杆,它带来的多头腿净超额是真的、能交易到的。**
   第一组五条因子里,原式只是把半衰期从「为多空夏普选的」(常常 1~3)换成「为多头腿选的」(10~20),
   样本外多头腿净超额就多 1~3 个点。所以:
   - **「原式 + 多头最优半衰期」永远是候选之一**,它就是表里 `v_base` 在「半衰期(多头)」下的那一行,
     也是任何结构候选要比过的**第一条基准**;
   - 一个候选的改进如果全部来自更长的半衰期,它**照样可以被推荐**(更简单、换手更低、净超额更高就是更好用),
     但**归因要写对**:写「改进来自平滑」,不要写成「删节点的功劳」「新结构的功劳」。
3. 多空夏普是**次要**信息(用户最早那张表的口径),每个变体都会同时算出来,用来和那张表对照、以及理解空头腿。
… (69 行略) …
没有现成诊断能回答的问题,就写脚本(这才是"每条表达式都不一样"的落点):

```python
import numpy as np
from partura.study_tools import Study, bk, dg
with Study("<fid>") as st:                       # 自带排队、内存守卫、共享缓存
    p = st.panels({"x": "day_skew(Low)"})["x"]   # (天, 股票) float32
    cap = st.control("ctl_cap")                  # 配置里的控制变量 / 已知家族,按名字取
    tgt, tr, va = st.target(), st.slice("train"), st.slice("valid")
    b = st.books(p, fit="train", evals=("train", "valid"))        # 和表里同口径;b["by_rank"]["long"]["splits"]["valid"]
    sig = st.signal(p)                           # 实际交易的信号(方向 x 面板,按多头口径半衰期平滑),全长
    raw = st.target(buyable=False)               # 不带"买不进"过滤的标签:量空头腿里有多少是封板票撑的
    print(st.ic(p, "valid"), st.rank_corr(sig, st.control("known_stdamt_mean30")))
```

`st.slice("holdout")` 会直接报错 —— 留出段不从分析脚本里读。脚本里用 `print` 输出,`wait` 会打印日志尾部 200 行,
完整日志在 `logs/<fid>_<tag>.log`。脚本没法在本机试跑(没有数据):先用随机数组把形状和 NaN 处理过一遍,
并在脚本开头对一个已知答案做自检。

### 自己写探针:`studies/<fid>/probes.py`
```

**10-04 14:24 · Bash** — Grep config for final and gate keys

```bash
cd /Users/wxy/Desktop/Partura && grep -n "final\|holdout\|utest\|rank_by\|gates\|known_stdamt" configs/F107_abs_demean_skew_low.yaml | head -60
```

```
16:rank_by: long          # 半衰期按纯多头书选(用户实际能做的那本书);多空口径每个变体也都会算
20:# train + valid = 用户的训练段(utrain);holdout = 用户的测试段,只在最后读一次
25:  holdout: ["20230808", "20251231"]
44:gates:
46:  known_stdamt_max9: "cross_max(day_std(Amt), 9)"          # F001 的蒸馏结果
48:  known_stdamt_mean30: "cross_mean(day_std(Amt), 30)"      # B01 第一组里纯多头最好的两算子基准之一
49:  # ---- 本研究加的(x1 §7 之后;放在 gates 而不是 controls,all_controls 的 R² 仍与 S0 可比)
54:            known_amt_max9, known_stdamt_max9, known_ivol_max9, known_stdamt_mean30, g_absidio20, g_kurtlow20]
64:    - {factor: m60, gate: known_stdamt_mean30, buckets: 5}     # 已知家族的多头端是分桶变量最低的一桶(方向为负)
```

**10-04 14:25 · Bash** — Read playbook sections on final and deliverables

```bash
cd /Users/wxy/Desktop/Partura && sed -n '120,230p' docs/study_playbook.md
```

```
见 `docs/method.md` §3 和 `studies/F002_crosscov_highvar/probes.py`、第一组研究各自的 `probes.py`。
在配置里加 `probes: [studies/<fid>/probes.py]`,`decompose` 和报告会自动带上。
**先在已知答案的算子上自检,再拿去读未知算子。**(内置探针对触发型算子如 `in_sustain_*` 基本是空读数 —— 这类必须自己写。)

---

## 3. 配置文件 `configs/<fid>.yaml`

骨架已经生成(S0_baseline 已跑完,结果在 `runs/<fid>/S0_baseline.json`)。你要做的是往后加阶段:

```yaml
stages:
  - id: S1_xxx
    question: "这一组实验在回答哪一个问题?(一句可证伪的话)"
    variants:
      - {id: a_no_abs, group: ablate, expr: "cs_demean(day_skew(Low))", why: "去掉 abs:如果预测力来自偏度的幅度而不是方向,这个应该塌"}
```

- 变体 id 全研究唯一。`why` 必须写它想证伪什么。
- `diagnostics:` 里的 `neutralise / profile / decay / by_year` 列变体 id;`conditional:` 列 `{factor, gate, buckets}`。
- `controls:` / `gates:` 可以按这棵树的嫌疑**增加**;共享的那几个别删。注意往 `controls` 里加东西会改变
  `all_controls` 的 R²(与 S0 那一行不再可比)—— 想单独对某个家族做中性化,加到 `gates` 里并用 exec 脚本量。
- `corr_ids` 列出要进 rank 相关矩阵的变体(可以跨阶段);`corr_with` 列控制变量。
- 留出段那一次:单独建一个阶段(通常叫 `S_final`),放 **≤ 5 个**最终候选,变体写 `final: true`。
  **必须包含**:原式(新 id,如 `f_orig`);**至少一条已知家族基准**(`cross_mean(day_std(Amt), 30)` 或
  `cross_max(day_std(Amt), 9)`),除非你有证据说明它与这条因子无关。用 `study.sh final` 跑。
  **候选的排序(第一推荐是谁)和判据(留出段出现什么算被否定)必须在读之前写进 `notes/<fid>/10_distilled.md`。**

### 表达式语言的坑(都踩过)

… (60 行略) …

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
5. **秩空间的线性中性化看不见非单调关系**。因子里有 `abs_`、`cs_demean` 后取绝对值、平方这类折叠时,
   它和任何单调控制变量的 rank 相关都接近 0、R² 很低 —— 这不说明它不是已知暴露。要用**同样折叠过的控制变量**去量。
6. **空头腿被「买不进的票」抬高**。次日开盘封涨停的票标签是 NaN,在空头里记 0 收益。涨停、一字板相关的因子
   (峰度、集中度、极端收益类)空头腿和多空夏普会因此虚高 0.5 以上 —— 用 `st.target(buyable=False)` 按**收益贡献**去量。
   (这只影响多空口径;多头腿不受影响,这也是选拔看多头腿的又一个理由。)
```

**10-04 14:25 · Bash** — Read factor config

```bash
cd /Users/wxy/Desktop/Partura && cat configs/F107_abs_demean_skew_low.yaml
```

```
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

# ---- 这一批共用的控制变量(都是日频、因果、只用到 t 日收盘)。按这棵树的嫌疑增删。
… (64 行略) …
      - {id: r_kurtlow,  group: rival,      expr: "day_kurt(Low)",
         why: "同一条价格水平路径的四阶矩:x1 里它的 EMA20 与原式可交易信号秩相关 -0.78,多头腿毛超额却是 0。它是用来说明「原式的多头腿不在与峰度共享的那部分里」的对照"}
      - {id: r_mktcorr,  group: rival,      expr: "day_corr(Ret, nt_cs_mean(Ret))",
         why: "H7:直接量「跟不跟大盘走」(分钟收益与全市场分钟均值收益的日内相关,方向预期为正)。若原式的多头腿就是同步性,它应该复现多头腿且秩相关高"}

  # ---- S2:把记忆写进表达式。x1 §5 的 numpy 版本说多头腿净超额从 +1.1% / +3.0% 升到 +5~6% / +7%;这里用引擎给正式数字,并分清「平滑」与「结构」
  - id: S2_memory
    question: "把日轴记忆写进表达式之后,多头腿净超额的改善有多大、来自平滑还是结构?记忆该是均值、中位数还是极值,窗口多长最稳?"
    variants:
      - {id: m10,  group: window, expr: "cross_mean(abs_(cs_demean(day_skew(Low))), 10)",  why: "H11:窗口邻域的短端。与原式在同一固定半衰期下比,看结构(等权窗口)本身有没有贡献"}
      - {id: m20,  group: window, expr: "cross_mean(abs_(cs_demean(day_skew(Low))), 20)",  why: "H11:x1 里 mean20 + 半衰期 20 是 train/valid 最均衡的一个(+5.0% / +7.5%)。预测:多头腿净超额两段都比原式高 3 个点以上,毛超额不升(改进来自换手)"}
      - {id: m30,  group: window, expr: "cross_mean(abs_(cs_demean(day_skew(Low))), 30)",  why: "H11:邻域"}
      - {id: m60,  group: window, expr: "cross_mean(abs_(cs_demean(day_skew(Low))), 60)",  why: "H11:x1 里 +6.0% / +6.6%。预测同 m20;若 m60 明显好于 m20,慢变量的尺度比一个月更长"}
      - {id: m120, group: window, expr: "cross_mean(abs_(cs_demean(day_skew(Low))), 120)", why: "H11 的长端:x1 里 train 降(+4.6%)而 valid 升(+9.7%),两段不同向。它是用来看「更长」是否已经过头的"}
      - {id: md60, group: substitute, expr: "cross_med(abs_(cs_demean(day_skew(Low))), 60)", why: "H2:记忆换成中位数,尾部事件完全不进来。H2(多头腿在主体)预测多头腿不降;若多头腿明显变差,多头端需要「最近没出过事」这条排除信息"}
      - {id: mr60, group: substitute, expr: "cross_mean(cs_rank(abs_(cs_demean(day_skew(Low)))), 60)", why: "H2:先取截面秩再求 60 日均值(尾部压平但仍计数)。与 m60、md60 一起看尾部在多头腿里起多大作用"}
      - {id: mx20, group: substitute, expr: "cross_max(abs_(cs_demean(day_skew(Low))), 20)", why: "H1:记忆换成 20 日极值(只记最出格的一天)。若多头腿只是「最近没出过事」,它应该与 m20 一样好;若多头腿需要主体的平均水平,它会差"}
      - {id: m60_nodemean, group: ablate, expr: "cross_mean(abs_(day_skew(Low)), 60)", why: "H6 在慢尺度上:60 日平均之后,当天的截面均值还重不重要?若仍然明显更差,「相对全市场当天的形状」是多头腿的实质"}
      - {id: m20_absret, group: rival, expr: "cross_mean(abs_(cs_demean(div(day_last(Close), cross_delay(day_last(Close), 1)))), 20)", why: "H3:朴素的日频 |特质收益| 配上同样的 20 日记忆。它与 m20 的多头腿之差,就是日内路径形状在特质波动之外多给的东西"}
      - {id: m60_absret, group: rival, expr: "cross_mean(abs_(cs_demean(div(day_last(Close), cross_delay(day_last(Close), 1)))), 60)", why: "同上,60 日"}
```

**10-04 14:26 · Bash** — Check fact-note structure for interpretation sections

```bash
cd /Users/wxy/Desktop/Partura && echo "=== S1_parts tail ===" && tail -20 notes/F107_abs_demean_skew_low/07_S1_parts.md && echo && echo "=== S2_memory tail ===" && tail -20 notes/F107_abs_demean_skew_low/07_S2_memory.md && echo && echo "=== grep 解读 ===" && grep -n "解读\|留白" notes/F107_abs_demean_skew_low/07_S1_parts.md notes/F107_abs_demean_skew_low/07_S2_memory.md notes/F107_abs_demean_skew_low/07x_2_elevate.md
```

```
=== S1_parts tail ===
| r_kurtret | −33.7%/−4.87/51% | −6.6%/−0.80/15% | −1.2%/−0.14/8% | +0.2%/+0.02/5% | +0.8%/+0.09/3% |
| r_kurtlow | −76.1%/−16.57/89% | −33.8%/−8.07/44% | −20.6%/−4.77/27% | −13.3%/−2.99/17% | −7.3%/−1.62/10% |
| r_mktcorr | −36.4%/−4.19/66% | −4.8%/−0.46/21% | +0.4%/+0.04/10% | +3.3%/+0.31/6% | +3.8%/+0.36/3% |
| v_base(S0) | −63.2%/−26.09/90% | −23.5%/−6.83/45% | −10.2%/−2.56/28% | −3.1%/−0.70/18% | +1.1%/+0.24/11% |

**分位剖面**(Q1..Q10,Q10=多头端;仅 config 里列入 `diagnostics.profile` 的 S1 变体有此表:p_nodemean、p_rank、p_cube、r_absret):

| id/split | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 |
|---|---|---|---|---|---|---|---|---|---|---|
| p_nodemean tr | −33.5% | −5.6% | +1.4% | +3.6% | +5.8% | +6.1% | +6.1% | +6.7% | +5.9% | +3.7% |
| p_nodemean va | −28.0% | −4.2% | −0.7% | +3.3% | +0.1% | +7.0% | +6.5% | +8.1% | +4.2% | +3.8% |
| p_rank tr | −19.9% | −4.2% | −3.5% | −2.8% | +1.4% | +2.2% | +4.5% | +5.7% | +6.2% | +10.4% |
| p_rank va | −23.4% | −12.0% | −4.4% | −0.9% | +1.6% | +3.8% | +4.9% | +6.7% | +11.5% | +12.3% |
| p_cube tr | −26.0% | −8.8% | −2.1% | −0.2% | +3.1% | +4.9% | +6.7% | +7.1% | +7.8% | +7.5% |
| p_cube va | −22.1% | −3.7% | −2.8% | +0.9% | +0.4% | +4.2% | +3.6% | +6.3% | +5.3% | +7.8% |
| r_absret tr | −37.1% | −11.0% | −3.0% | +3.4% | +3.7% | +7.1% | +6.3% | +10.5% | +10.4% | +9.8% |
| r_absret va | −41.4% | −15.1% | −9.1% | −2.6% | +0.9% | +5.1% | +13.1% | +13.0% | +16.7% | +19.4% |

来源:`./scripts/study.sh digest F107_abs_demean_skew_low S12`(tag S12,10-05 04:59 完成,exit 0,peak anon 6.98G);完整表另存
`results/R1.md` 与 `logs/`(本阶段无独立 log 文件,数字来自 `runs/F107_abs_demean_skew_low/S12.json` 与其 digest 打印)。

=== S2_memory tail ===

| id | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 |
|---|---|---|---|---|---|---|
| m20 | +7.6% / 2.55 | +3.6% / 2.53 | +4.3% / 2.04 | +3.2% / 2.18 | +3.7% / 2.25 | +12.9% / 5.11 |
| m60 | +6.6% / 3.04 | +4.9% / 2.56 | +4.9% / 2.16 | +5.6% / 2.36 | +3.5% / 2.18 | +11.4% / 4.47 |
| m120 | +7.1% / 2.82 | +2.9% / 2.46 | +2.6% / 2.07 | +3.1% / 1.75 | +6.9% / 2.56 | +14.0% / 5.21 |
| mr60 | +6.1% / 2.85 | +3.7% / 1.79 | +4.6% / 1.37 | +4.9% / 2.28 | +3.9% / 1.94 | +10.5% / 3.22 |
| m20_absret | +10.7% / 3.15 | +4.1% / 2.50 | +0.2% / 1.25 | +4.2% / 1.69 | +15.3% / 3.30 | +10.8% / 1.89 |

**衰减**(rank IC at horizon h,config `diagnostics.decay`:m20、m60):

- m20: h1 +0.0249 h2 +0.0306 h3 +0.0334 h5 +0.0378 h10 +0.0443 h20 +0.0533
- m60: h1 +0.0258 h2 +0.0314 h3 +0.0341 h5 +0.0383 h10 +0.0444 h20 +0.0523

**条件 IC**(config 里只对 m60 列了两组分桶):

- m60 | known_stdamt_mean30(低→高五桶):Q1 +0.0205 Q2 +0.0135 Q3 +0.0158 Q4 +0.0191 Q5 +0.0279
- m60 | ctl_cap(低→高五桶):Q1 +0.0344 Q2 +0.0340 Q3 +0.0354 Q4 +0.0249 Q5 +0.0048

来源:`./scripts/study.sh digest F107_abs_demean_skew_low S12`(tag S12,10-05 04:59 完成,exit 0)。

=== grep 解读 ===
notes/F107_abs_demean_skew_low/07_S1_parts.md:3:只写事实与表,解读留给主研(见工单 `orders/R1.md`、结果卡 `results/R1.md`)。方向/半衰期在 train 上定;Lnet=多头腿净超额、Lgross=多头腿毛超额、Lshp=纯多头夏普、LTO=多头日换手、Lmdd=多头最大回撤、short=空头腿毛超额(train)、ρ=与 v_base 可交易信号的日截面 rank 相关(train)。
notes/F107_abs_demean_skew_low/07_S2_memory.md:3:只写事实与表,解读留给主研(见工单 `orders/R1.md`、结果卡 `results/R1.md`)。
notes/F107_abs_demean_skew_low/07x_2_elevate.md:3:只写事实与表,解读留给主研(见工单 `orders/R1.md` 与结果卡 `results/R1.md`)。完整 stdout 在 `logs/F107_abs_demean_skew_low_x2.log`(202 行)。
```

**10-04 14:26 · Bash** — Check hypotheses file tail

```bash
cd /Users/wxy/Desktop/Partura && tail -40 notes/F107_abs_demean_skew_low/05_hypotheses.md
```

```
**对只能做多的用户,真正要回答的是 H11 和 H4**:多头腿毛超额有 +9%~+11%,但 10.9% 的日换手吃掉了 8 个点;
已知家族 `cross_mean(day_std(Amt), 30)` 在同一口径下是 +12.6% / +22.3%(换手 3.4%)。这条因子要有用,必须(a)把换手降下来而毛超额不掉(H11),
并且(b)它的多头腿不是已知家族的子集(H4 被杀死)。

---

## 第 1 轮裁决(主研 Opus 5,2026-10-04)

> 上面那张表是**开工前**写的,没有状态列。这里记每条的状态;**完整的状态表、证据与「还差什么才能定」在 `state.md` §4,以那一页为准。**
> 这一轮的证据全部来自 `07x_1_anatomy.md`(tag `x1`,**numpy 探路,不是引擎正式数字**)。引擎阶段 run `S12` 已启动但结果还没读。

| # | 状态 | 一句话依据 |
|---|---|---|
| H1 空头腿在尾部 | **被支持(numpy)** | 截尾/取秩 → 空头腿 +32.5 → +17.5~18.2、多空 2.81 → 0.72~0.89;钉住日换中性值 → 空头腿只剩 +7.8 |
| H2 多头腿在主体 | **被支持(numpy)** | 截尾/取秩后多头腿毛超额纹丝不动(+9.2~9.8 / +11.9~12.3);只留尾部 → 多头毛只剩 +3.2 |
| H3 已知暴露 | **已改写 → H14** | 9 个单调控制变量只把多头毛压到 +8.2(看似不是),但换成**同样折叠过**的 `EMA20\|去均值日收益\|`,一个变量 R² 0.307、残差多头毛只剩 **+2.9** |
| H4 已知家族的子集 | **被支持(numpy);结论的关键** | 对 K 取残差 +3.9/+1.4(60 日版 +2.0/−3.1);相加净超额不升;**原式多头十分位里 K 最低的三分之一 −0.6%/−4.7%** |
| H5 折叠对称 | **被否定** | 最好的桶是 (−0.5,−0.25] 而非 0;负侧「平台+悬崖」,正侧是斜坡,最优点在 −0.375 附近 |
| H6 `cs_demean` 多余 | **被否定** | 去掉它多头毛 +9.4/+11.4 → **+3.4/+3.7**(空头腿不变) |
| H7 共同路径份额 | **被否定** | ρ 只有 +0.13;日内相关在各十分位间不单调(0.33/0.55/0.46) |
| H8 网格/常数路径伪影 | **被否定** | 涉及格子 < 0.3%;与 `ctl_price` ρ 只有 −0.09 |
| H9 三阶矩不必需 | **对多头腿被支持,对空头腿被否定** | 有界不对称度多头毛相同(+9.5/+9.2),空头腿 +32.5 → +24.1、换手升到 14.1% |
| H10 字段偶然 | **被支持(numpy)** | Close ρ 0.95、High 0.93,书在噪声内相同 |
| H11 慢变量、20 不够长 | **被支持(numpy);归因 = 平滑** | 窗口 10~60 → 净超额 +5~6/+6.6~7.5、夏普 1.0~1.2/1.5~1.7,但**毛超额不升**,改进全部来自换手 10.9% → 3~4% |
| H12 买不进的票抬高空头腿 | **被支持(numpy);不再投入** | 换不带过滤的标签 → 多空夏普 2.81 → 1.83。只影响多空口径 |

**新增两条(第 1 轮)**

- **H13(升华线索)**:H5 被否定的直接后果 —— `abs_` 把「左悬崖、右斜坡、最优点偏左」压成了对称的 V。
  移心 `|B − c|`(c ≈ −0.375)或倾斜 `|B| + λ·B` 应该更纯。
  依据还包括 x1 §2:在 `EMA20|B|` 最小的 30% 里,`EMA20(B) < 0` 的格子 +13.7%/+11.6%,`≥ 0` 的 +4.7%/+7.2%
  —— **方向信息在多头一侧也有,但 train 强、valid 弱**。
  **杀死它的实验**:x2 §b —— train 上定出的最优 c / λ 拿到 valid 上不复现(或两段最优点不一致、valid 掉回 0)→ 它是 train 过拟合。
  要说「结构更好」,必须在**同一半衰期**下比毛超额。
- **H14(全局最要紧的一条)**:H3 的改写 —— **日内路径形状在「特质波动」之外没有增量**。
  `m20` 与 `m20_absret`(完全不看日内路径,只有日频 `|特质收益|` + 同样的 20 日记忆)的多头腿在噪声内相同。
  依据:x1 §6(R² 0.307、残差多头毛 +2.9)与 x1 §3(同一条路径的 `day_kurt(Low)` ρ 0.78 却没有多头腿)。
  **杀死它的实验**:S12 的 `m20` vs `m20_absret`、`m60` vs `m60_absret`、`r_absret` —— 差 > 3 个点且 train/valid 同向。
  若 H14 成立,这棵树读的 241 根分钟最低价白读了,结论往「没有增量」写。
```

**10-04 14:27 · agent 的话**

I have the full picture. The R1 results are decisive. Let me record the adjudication.

**10-04 14:27 · mcp__ccd_session__mark_chapter**

```json
{
 "title": "第 2 轮裁决与读留出段",
 "summary": "裁决 H13/H14/H15/H4:日内路径被日频 |特质收益| 支配、移心折叠不外推、相对已知家族无增量 → 登记候选与判据,下 final 工单"
}
```

```
Chapter marked: "第 2 轮裁决与读留出段". Continue your current work.
```

**10-04 14:28 · Bash** — Append round-2 adjudication to hypotheses

```bash
cd /Users/wxy/Desktop/Partura && cat >> notes/F107_abs_demean_skew_low/05_hypotheses.md <<'MDEOF'

---

## 第 2 轮裁决(主研 Opus 5,2026-10-04)—— 引擎数字到手,四条关键假设全部落地

> 证据来源:`results/R1.md`(tag `S12`,22 个变体,引擎正式数字)+ `07x_2_elevate.md`(tag `x2`,§a~§f,引擎 `st.books`)。
> 口径:多头腿扣 15bp 净超额(Lnet)/ 纯多头夏普(Lshp),方向与半衰期在 train 上定;噪声带 ±3pp 净超额、±0.3 夏普。
> **这一轮之后,假设表上不再有「未验证」的条目。完整状态表以 `state.md` §4 为准。**

| # | 状态(第 2 轮) | 引擎证据(一句话) |
|---|---|---|
| H1 空头腿在尾部 | **已确立** | p_rank short +19.6%、p_range +24.1%(v_base +32.5%);p_rank 的多空 LS 2.81 → 1.12 |
| H2 多头腿在主体 | **已确立** | p_rank(尾部压平)Lgross +10.3%/+12.2% ≥ v_base +9.4%/+11.4%;p_cube(权重压到尾部)反而降到 +7.2%/+7.5% |
| H3 已知暴露 | **已改写 → H14,且 H14 成立** | m20 的 `all_controls` R² 0.182,残差 Lgross +6.9% → **+1.6%**;`ctl_dvol20` 单变量 R² 0.127 → 残差 Lgross +2.4% |
| H4 已知家族的子集 | **已确立 —— 这就是结论** | x2 §e:8 条候选(含全部升华候选)**对 K 取残差的 Lnet 在 valid 上无一为正**(−0.3%~−9.9%);`rank F + rank K` 在 valid 上**全部低于 K 单独**(+17.8~+20.2 vs **+22.3**);`0.5rankF + rankK` 同样(+19.7~+21.5 vs +22.3);**K 最高十分位内按 F 分三档,valid 上翻向**(m60:+27.7/+26.9/+25.1,最低档反而最好) |
| H5 折叠是对称的 | **被否定** | x1 §1 最优桶 (−0.5,−0.25];后续是 H13 |
| H6 `cs_demean` 多余 | **被否定(引擎坐实)** | p_nodemean Lgross **+3.5%/+3.8%**(v_base +9.4%/+11.4%);m60_nodemean Lnet +1.4%/+1.3%(m60 +5.6%/+6.5%);x2 §c:只因 `cs_demean` 才入选多头十分位的名字 **+13.4%/+16.2%**,只在不去均值版入选的 **−2.7%/−6.0%** |
| H7 多头腿 = 跟着大盘走(分钟收益同步性) | **被否定** | r_mktcorr ρ(v_base) 仅 **+0.1325**,Lnet +3.8%/+6.1% —— 是另一条因子,不是这棵树的多头腿。**注意它和 H16 不是一回事**(见下) |
| H8 价格网格/常数路径伪影 | **被否定** | 涉及格子 < 0.3%;与 `ctl_price` ρ −0.09 |
| H9 三阶矩不是必需的 | **已确立(对多头腿)** | p_range Lgross +9.5%/+9.2% ≈ v_base,但 LTO 升到 14.1%、short 降到 +24.1%、`dist` 掉到 0.90 |
| H10 字段是偶然的 | **已确立** | p_close ρ **0.9508**,Lgross +8.0%/+12.1%、Lnet +0.6%/+5.0%,全在噪声带内 |
| H11 它是慢变量,20 日半衰期不够长 | **已确立;归因 = 平滑,已坐实** | **同一半衰期 hl20**(v_base / m10 / m20 都选到 20):Lgross +9.4%/+11.4% → **+6.9%/+9.5%(毛超额降 2.5/1.9pp)**,LTO **10.9% → 2.8%**,Lnet +1.1%/+3.0% → +4.8%/+7.3%。固定 hl20 的 train 净超额:v_base +1.1、m10 +4.6、**m20 +4.8**、m30 +3.
… (952 字符略) …
:8 个最大差格子**全部**是「窗口内仅 1 个有限观测、当天 base 为 NaN」;\|diff\|>0.05 的 16,724 格(0.31%)mean finite-days-in-window **19.4**(全体 58.1);仅 numpy 有限 **24,927** 对仅引擎有限 **262**(引擎侧多一层 mask)。**决定性的一条**:m10~m120 的 book 级 Lnet,x1(numpy)与引擎差 **≤0.6pp**,全在噪声带内 → **x1 的时间尺度表排序可信**,不需要重建候选名单 |

### 新增一条(第 2 轮):H16

- **H16(机制;替 H7 收尾)**:`cs_demean` 之所以必需,**不是**因为「跟着大盘的分钟收益走」(那是 H7,已被否定,ρ 仅 0.13),
  而是因为它在偷偷量**「我今天的日内价格水平形状,跟不跟当天全市场的形状走」** —— 一个 60 日尺度的形状同步性。
  - **证据(两段同向)**:x2 §c —— 只因 `cs_demean` 才进入多头十分位的那 3.5%/3.6% 名字,`corr60(A,μ)` 的日内百分位秩是
    **0.83 / 0.84**(只在不去均值版入选的那组是 0.40 / 0.31),次日超额 **+13.4% / +16.2%**(对 −2.7% / −6.0%);
    `Spearman(corr60, v_base 可交易信号)` train **+0.512**。
  - **但它不是这棵树的提纯,也过不了 K**:`corr60(A,μ)` 单独 Lnet tr +5.1% / va **+11.1%**、Lshp 0.94/2.05,
    ρ(v_base) 仅 **+0.51**(< 0.8 → 按 playbook §6.3 是**换了一条因子**),对 K 取残差 **−2.7% / −6.8%**,
    与 K 相加 valid +20.9% < K 单独 +22.3%。
  - **状态:合理但未坐实**。它解释了 H6 为什么被否定,但没有做成一本打过 K 的书。
    **不在本研究继续投入**(它是另一条因子),写进 `12_next.md` 当分支建议。
MDEOF
echo OK
```

```
OK
```

**10-04 14:28 · agent 的话**

Now the interpretations on the three fact notes.

**10-04 14:28 · Bash** — Append interpretation to S1_parts note

```bash
cd /Users/wxy/Desktop/Partura && cat >> notes/F107_abs_demean_skew_low/07_S1_parts.md <<'MDEOF'

---

## 解读(主研,第 2 轮)

**这一阶段问的是:三个节点(偏度 / 截面去均值 / 折叠)和字段各自必不必需?它是不是一个朴素日频量的另一种写法?**
引擎的答案很整齐,而且把这棵树切成了「必需的一个节点 + 两个可替换的节点 + 一个写错的节点」。

**1. `cs_demean` 是唯一不能动的节点。** `p_nodemean`(去掉它)多头腿毛超额从 +9.4%/+11.4% 掉到 **+3.5%/+3.8%**,
空头腿几乎不动(+32.8% 对 +32.5%)—— 也就是说**空头腿根本不需要截面去均值**(封板票的 `|A|` 本身就极端),
**多头腿的全部内容都在「相对当天全市场的形状」这一层**。这把 H6 彻底否定了。
它的分位剖面也印证:`p_nodemean` 的 Q10 只有 +3.7%/+3.8%,而 Q6~Q8 反而更高(+6.1~6.7%)——
**去掉去均值之后多头端不再是梯度的上端,排序在右半边塌了。**

**2. 折叠(`abs_`)是写错的那一个,但不是可以修的。** `p_signed`(不折叠)整本书是反的
(Lnet −30.1%/−36.6%、Lshp −3.88/−5.36、Lmdd −119.1%),因为带符号的 B 对次日收益是**倒 U**(x1 §1/§2):
两头都差,中间好。`abs_` 把倒 U 折成单调是**必要的**,只是折点不对(最优在 −0.375 而非 0)。
「修折点」这条路由 H13 单独裁决,结论是**不外推**(见 `07x_2_elevate.md` §b 的解读)。

**3. 偏度的三阶矩与字段 `Low` 都是偶然的 —— 对多头腿而言。**
`p_range`(换成有界不对称度 `(max+min−2med)/(max−min)`,完全没有厚尾)多头毛 +9.5%/+9.2% ≈ 原式,
但空头腿掉到 +24.1%、换手升到 14.1%、`dist` 掉到 0.90 → **三阶矩的厚尾只服务于空头腿**(H9/H1)。
`p_close` ρ(v_base)=**0.9508**、书在噪声带内相同 → **字段可换**(H10)。
`p_znorm`(再除以当天截面标准差)Lnet +1.6%/+3.1% ≈ 原式 → 截面离散度大的日子不是信号来源。
`p_rank` / `p_cube` 这一对把 H1/H2 钉死:**压平尾部(p_rank)多头毛不降(+10.3%/+12.2%)而多空 LS 从 2.81 掉到 1.12;
把权重压到尾部(p_cube)多头毛降到 +7.2%/+7.5% 而空头腿不动(+31.5%)** —— 两条腿确实是两种机制。

**4. 最要紧的一行是 `r_absret`,它是这棵树的判决书。**
`abs_(cs_demean(日收益))` —— **完全不看日内路径**,只把「去均值 + 折叠」这两个动作施加在日频收益上 ——
Lnet **+5.3%/+14.5%**、Lshp 0.69/**2.27**、rIC **+0.0449/+0.0493**,**每一项都好过原式**(+1.1%/+3.0%、0.24/0.69、+0.0337/+0.0418),
换手只有 5.8%(原式 10.9%)。它的分位剖面在 valid 上是 −41.4% → **+19.4%**,比原式的 −31.0% → +11.8% 陡得多。
→ **这棵树的「结构」(241 根分钟最低价 → 水平占用分布的三阶矩)不是信号的来源;
「去均值 + 折叠」这两个动作才是,而它们施加在一个朴素的日频量上效果更好。**
(ρ(v_base) 只有 +0.5439,所以 `r_absret` **不是原式的提纯,是另一条因子** —— 按 playbook §6.3 必须这么写。
它和 `g_absidio20` 的秩相关是 **−0.9816**(同一表达式)、和 `ctl_dvol20` **−0.8066** → 它就是「低特质波动 / 低已实现波动」这个已知暴露。)

**5. 两条对照把「多头腿不在哪」说清楚了。**
`r_kurtlow`(同一条价格水平路径的四阶矩)ρ 0.7842 却 Lnet **−7.3%/−9.4%**、Lgross +0.5%/−1.9%
→ **原式与峰度共享的那 61% 方差里没有多头腿**(见 `07x_2_elevate.md` §d)。
`r_mktcorr`(分钟收益与全市场分钟均值的日内相关)ρ 仅 **+0.1325** → H7 被否定,**多头腿不是分钟级的同步性**
(但 60 日尺度的**形状**同步性是另一回事 → H16)。

**这一阶段确立的事:** H6 被否定(`cs_demean` 必需)、H9/H10 成立(三阶矩与字段对多头腿可换)、
H1/H2 成立(两条腿两种机制)、H7 被否定、**H14 的第一半成立(日频替身更好)**。
**这一阶段没有产出任何提纯候选** —— S1 里没有一个变体的多头腿净超额超过原式 3 个点以上,
唯一超过的是 `r_absret` 这条**换了因子**的对照。提纯只能来自 S2(把记忆写进表达式)。
MDEOF
echo OK1
```

```
OK1
```

**10-04 14:29 · Bash** — Append interpretation to S2_memory note

```bash
cd /Users/wxy/Desktop/Partura && cat >> notes/F107_abs_demean_skew_low/07_S2_memory.md <<'MDEOF'

---

## 解读(主研,第 2 轮)

**这一阶段问的是:把日轴记忆写进表达式之后,多头腿净超额的改善有多大、来自平滑还是结构?**
答案:**改善是真的(+3.7pp/+4.3pp,可以交易到),但 100% 来自换手;原始预测力反而降了。**

**1. 归因:在同一个半衰期下比,毛超额是降的。**
这是本阶段最要紧的一组对照,而且不需要额外运行 —— **`v_base`、`m10`、`m20` 三者在多头口径下都选到 hl=20**,
所以 A 表里它们的 `Lgross` 本来就是同一半衰期下的数字:

| 在 hl20 下 | Lgross tr/va | LTO | Lnet tr/va | Lshp tr/va |
|---|---|---|---|---|
| v_base(原式) | +9.4% / +11.4% | 10.9% | +1.1% / +3.0% | 0.24 / 0.69 |
| m20 | **+6.9% / +9.5%** | **2.8%** | **+4.8% / +7.3%** | **0.96 / 1.70** |

**毛超额降了 2.5pp / 1.9pp,换手降到四分之一,净超额因此升了 3.7pp / 4.3pp。**
→ 按 playbook §6.1 必须写成「**改进来自更长的记忆 / 更低的换手(平滑)**」,**不能写成结构更好**。
固定半衰期表(train 净超额)给出同一结论,并且告诉我们窗口有内点最优:
v_base +1.1 → m10 +4.6 → **m20 +4.8** → m30 +3.9 → m60 +3.3 → m120 +1.0。
**在同一半衰期下,20 日窗口是最优窗口;再长就只能靠把半衰期调短(m30/m60/m120 分别选到 hl 5/3/3)来换净超额。**

**2. 记忆该用什么形式:均值最好,极值最差 —— 这是 H2 的第二次检验,通过了。**
`mx20`(20 日极值,只记最出格的一天)Lnet 只有 +1.7%/+1.1%、Lshp 0.43/0.34 —— **比 m20 差 3pp 以上**。
`md60`(中位数)+3.3%/+7.2%、`mr60`(先取秩再平均)+4.9%/+6.5%,都在 m60 的噪声带内。
→ **多头端要的是「主体的平均水平」,不是「最近有没有出过事」。** 这与 S1 的 `p_rank`/`p_cube` 一致(H2)。
`m60_nodemean`(60 日平均但不去均值)Lnet +1.4%/+1.3% —— **在慢尺度上 `cs_demean` 依然必需**,H6 再次被否定。

**3. 窗口邻域是稳的,但这不是结构稳,是平滑稳。** m10/m20/m30/m60 的 Lnet 落在 +4.6~+5.6% / +6.5~+7.3%,
Lshp 0.95~1.11 / 1.53~1.70,邻域换一档不塌。m120 是边界情形:train 最弱(+4.0%)、valid 最强(+9.7%),
而在固定 hl20 下 train 只有 +1.0%(= 原式水平)→ **m120 的全部优势来自它选到 hl3、换手 2.2%**,结构上它已经过头了。
逐年也支持 m20/m60 比 m120 稳:m20 六年 +3.2~+12.9% 全正,m120 在 2019~2021 只有 +2.6~+3.1%。
**原式 2021 年是负的(−4.0%),m20/m60 把那一年救成 +3.2%/+5.6%** —— 这是平滑最直接的好处。

**4. 但本阶段最重要的一行,是把这整族否掉的那一行:`m20_absret` / `m60_absret`。**

| | Lnet tr / va | Lshp tr / va | rIC tr / va | LTO |
|---|---|---|---|---|
… (14 行略) …
→ **最大的五分之一里几乎没有信号**(与 S0 的 +0.045…+0.007 一致)。
`m60 | known_stdamt_mean30` 五桶 +0.0205 +0.0135 +0.0158 +0.0191 +0.0279 —— 在 K 的各档里都有一点 rank IC,
**但 rank IC 有一点 ≠ 多头腿有增量**(增量的检验在 `07x_2_elevate.md` §e,结论是没有)。
衰减表 m20 h1 +0.0249 → h20 **+0.0533** 单调上升 → 它确实是慢变量(H11),但这也意味着**它没有短期的 alpha 可以抢**。

**这一阶段确立的事:** H11 成立且**归因 = 平滑(已坐实,同半衰期下毛超额降)**;H2 第二次通过(均值 > 中位数 > 极值);
H6 在慢尺度上再次被否定;**H14 已确立**。
**产出的候选:`m20`(ρ(v_base)=0.918,提纯)与 `m60`(ρ=0.866)。两者都没能打过已知家族 K(+12.6%/+22.3%)。**
MDEOF
echo OK2
```

```
OK2
```

**10-04 14:30 · Bash** — Append interpretation to x2 elevate note

```bash
cd /Users/wxy/Desktop/Partura && cat >> notes/F107_abs_demean_skew_low/07x_2_elevate.md <<'MDEOF'

---

## 解读(主研,第 2 轮)

x2 是为「**多头腿能不能靠结构、而不只是靠平滑提纯**」而写的,六节各管一件事。结论:**六节里五节是否定的,
一节(§c)给出了机制解释但指向另一条因子。这一次探针把这棵树上剩下的结构空间清空了。**

### §a — H15 已确立:面板不一致是边界伪影,x1 的候选名单可信

三个观测同时对上「引擎在表达式内部重算原式时带了一层 universe/停牌 mask,而缓存面板没有」这条解释:
8 个最大差格子**全部**是「窗口内只有 1 个有限观测、当天 base 为 NaN」;`|diff|>0.05` 的 16,724 格(0.31%)
mean finite-days-in-window **19.4**(全体 58.1);**仅 numpy 有限 24,927 对仅引擎有限 262**(引擎侧少了格子,方向正确)。
**但真正决定性的不是这些,而是 book 级的对照**:m10~m120 的 Lnet,x1(numpy)与引擎差 **≤0.6pp**,全在 ±3pp 噪声带内。
→ **x1 §4/§5 的时间尺度表(候选名单所依赖的那张表)在排序上可信,不需要重建。**
**这条坑的正确处理方式是「知道它存在、绕开它」,不是去修它**:做 book 级判断用引擎数字,
numpy 探路只用来排序和找方向。(遗留的小疑点:`p_nodemean` / `p_rank` 的空头腿 x1 与引擎差 1.4pp、LS 差 0.06~0.23,
这两个变体**不含** `cross_mean`,所以不是本条原因,来源不明;只影响空头腿,对结论不关键,**不再投入**。)

### §b — H13 被否定:折叠的不对称是真的,但做不成可交易的结构

x1 §1 发现 `abs_` 把一个「左悬崖、右斜坡、最优点在 −0.375」的形状压成了对称的 V,这是这棵树上**唯一有结构理由的升华线索**。
x2 把它做成了书,结果是**train 上很漂亮、valid 上作废**:

| | train argmax | 该点在 valid | valid 自己的 argmax |
|---|---|---|---|
| mean20\|B−c\| | c=−0.4(**+7.7%**) | **+2.2%** | c=**0**(+7.5%) |
| mean60\|B−c\| | c=−0.4(**+9.2%**) | **+5.2%** | c=−0.2(+6.9%);c=0 是 +6.6% |
| mean20(\|B\|+λB) | λ=**+0.6**(+7.8%) | **+1.4%** | λ=**−0.3**(+6.7%)—— **符号翻转** |
| mean60(\|B\|+λB) | λ=+0.6(+7.4%) | +5.2% | λ=+0.3(+6.3%) |

**两段的最优点不一致,20 日那一族连符号都翻。** 在**固定 hl20**(排掉平滑的干扰)下看得更干净:
`|B−(−0.4)|` Lnet tr **+5.6%** / va **+2.1%**,对 v_base 的 +1.1% / +3.0% —— **train 升 4.5pp,valid 降 0.9pp,两段反向**;
毛超额同样(tr +9.4→+14.5,va +11.4→+11.0)。
→ **c 与 λ 是在 train 上拟合出来的常数,不外推。** 按硬规矩 6(两段不同向的改进不算改进),**H13 被否定**。
写报告时要写成:「折叠的不对称在样本内是真实的(事件层最优桶在 −0.375),但把它写进表达式之后在 valid 上不复现 ——
这棵树没有可交易的结构升华空间。」

### §c — H16:`cs_demean` 到底在量什么(机制,两段同向,但指向另一条因子)
… (58 行略) …
**这是整份研究里唯一一处混合看起来有用的地方,但它只有一年、而且 2020 是创业板涨跌幅放宽那一年(`03` 记的制度变化),
按 playbook §6.4,只靠某一年的规律最多算「合理但未坐实」,不能用来翻结论。**

### x2 整体的意义

**这一次探针的作用是「清空」**:它把这棵树上**所有**还没试过的结构方向(移心、倾斜、形状同步性、去掉与峰度共享的部分)
一次性做成书并在 valid 上检验,**全部不通过**;同时把唯一的方法学疑点(面板不一致,H15)排掉,
让 x1 的探路结果可以放心引用。**在它之后,这条因子已经没有「再想一个变体」的空间了 —— 该去读留出段了。**
MDEOF
echo OK3
```

```
OK3
```

**10-04 14:30 · agent 的话**

Now the pre-registration — candidates and criteria, before the holdout read.

**10-04 14:32 · 写文件** `/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/10_distilled.md`(5128 字符)

**10-04 14:32 · agent 的话**

Now the order for the holdout read.

**10-04 14:33 · 写文件** `/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/orders/R2.md`(5073 字符)

**10-04 14:33 · agent 的话**

Now the full state rewrite — the handoff page.

**10-04 14:37 · 写文件** `/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/state.md`(23430 字符)

10-04 14:38 · 读 `/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/state.md`

**10-04 14:42 · 写文件** `/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/state.md`(24708 字符)

**10-04 14:42 · agent 的话**

Now the journal entry.

**10-04 14:43 · Bash** — Write round-2 journal entry

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh note F107_abs_demean_skew_low "[主研] 第 2 轮:H14/H13/H15/H4 全部落地,四个升华方向在 valid 上全不通过 → 候选与判据写死,下 R2 读留出段" <<'EOF'
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
   |diff|>0.05 的 0.31% 格子 mean finite-days 19.4(全体 58.1);仅 numpy 有限 24,927 对仅引擎有限 262(引擎侧多一层 mask)。
   **决定性的是 book 级:m10~m120 的 Lnet,x1 与引擎差 ≤0.6pp,全在噪声带内。**
   这条坑的正确处理是「知道它、绕开它」,不是去修它。

4. **H4 已确立 —— 这就是结论。** x2 §e 把八条候选(三条引擎变体 + 五条升华候选,**所有还活着的方向**)对 K 做了三个检验:
   对 K 取残差的 Lnet **在 valid 上全为负**(−0.3 ~ −9.9);`rank F+rank K` 与 `0.5rankF+rankK`
   = **十六个组合,valid 上无一超过 K 单独的 +22.3%**;最锋利的是「K 最高十分位内按 F 分三档」——
   train 上 F 有排序能力(m60 +9.2/+20.6/+18.2),**valid 上翻向**(+27.7/+26.9/+25.1),
   而「K top 落进 F 底 30%」那批在 valid 上是 **+26.6% 对 +26.6%,一点差别都没有**。
   → **「用这条因子给已知家族的头部做一道筛」在 train 上看起来值钱,在 valid 上是零。**

5. **归因做干净了,而且没花额外运行。** v_base / m10 / m20 在多头口径下**都选到 hl20**,
   所以主表的 Lgross 本来就是同一半衰期下的数字:毛超额 +9.4%/+11.4% → **+6.9%/+9.5%(降 2.5/1.9pp)**,
   换手 10.9% → 2.8%,净超额因此升 3.7/4.3pp。**改进 100% 来自换手。**
   (R1 工单里要的「固定半衰期毛超额表」引擎这次没产出,但这条替代路径让它变成不必要的,所以没有为它新起运行。)

6. **一个意外(正面的,但指向别处)—— 立为 H16。** x2 §c:只因 cs_demean 才进入多头十分位的那 3.5%/3.6% 名字,
   次日超额 **+13.4%/+16.2%**,它们的 corr60(A,μ) 百分位 **0.83/0.84**;只在不去均值版入选的那组 −2.7%/−6.0%、百分位 0.40/0.31。
   → **cs_demean 在偷偷量「我的日内价格水平形状跟不跟当天全市场的形状走」(60 日尺度的形状同步性)。**
   **这和 H7 不是一回事**(H7 测的是分钟收益的同步性,ρ 仅 0.13,已被否定)—— 这个区分值得记住。
   但 corr60(A,μ) 单独 ρ(v_base) 只有 0.51(换了一条因子)、对 K 残差 −2.7%/−6.8%,**救不了这条因子**。

**判断。** 假设表上 16 条**没有一条停在「未验证」**;四个结构升华方向(移心/倾斜、形状同步性、去掉与峰度共享的部分、
换记忆形式)在 valid 上**全部不通过**。结论已经成型且是否定的:
… (11 行略) …
槽位给了能回答别的问题的第 4、5 条 —— 这是事前的取舍,代价已写进 10_distilled.md,将来要写进 11_risks.md);
不把 H16 做成本研究的候选(ρ 0.51,是另一条因子,写进 12_next.md);
不为补「固定半衰期毛超额表 / gates 版 neutralise 表」新起运行(已有替代路径);
不去统一 cross_delay/ts_delay、不去修 cross_mean 面板不一致(H15 已确立为边界伪影);不下第二张 final 工单。

**落盘。** state.md 整页覆盖重写(8 节,假设表扩到 16 条);05_hypotheses.md 追加「第 2 轮裁决」+ H16;
07_S1_parts.md / 07_S2_memory.md / 07x_2_elevate.md 各补「解读(主研,第 2 轮)」一节;
**新建 10_distilled.md 的「读留出段之前」(候选 + 排序 + 判据 0~4,已写死,不再改)**;新建 orders/R2.md(kind: final)。
EOF
echo "--- note written ---"
```

```
已记入 notes/F107_abs_demean_skew_low/journal.md(9 条)
--- note written ---
```

**10-04 14:43 · Bash** — Verify files written and holdout still unread

```bash
cd /Users/wxy/Desktop/Partura && ls -la notes/F107_abs_demean_skew_low/ notes/F107_abs_demean_skew_low/orders/ && echo "=== 留出段状态 ===" && ./scripts/study.sh brief F107_abs_demean_skew_low 2>/dev/null | grep -i "留出段\|阶段:" | head -5
```

```
notes/F107_abs_demean_skew_low/:
total 352
drwxr-xr-x@ 16 wxy  staff    512 Oct  4 14:42 .
drwxr-xr-x@ 19 wxy  staff    608 Oct  4 13:07 ..
-rw-r--r--@  1 wxy  staff   3070 Oct  4 12:55 02_operators.md
-rw-r--r--@  1 wxy  staff   2863 Oct  4 12:55 03_decomposition.md
-rw-r--r--@  1 wxy  staff   2218 Oct  4 12:28 04_grammar.md
-rw-r--r--@  1 wxy  staff  16788 Oct  4 14:28 05_hypotheses.md
-rw-r--r--@  1 wxy  staff   3894 Oct  4 13:05 06_baseline.md
-rw-r--r--@  1 wxy  staff  12378 Oct  4 14:28 07_S1_parts.md
-rw-r--r--@  1 wxy  staff  12730 Oct  4 14:29 07_S2_memory.md
-rw-r--r--@  1 wxy  staff  10794 Oct  4 13:06 07x_1_anatomy.md
-rw-r--r--@  1 wxy  staff  23491 Oct  4 14:30 07x_2_elevate.md
-rw-r--r--@  1 wxy  staff   9032 Oct  4 14:32 10_distilled.md
-rw-r--r--@  1 wxy  staff  17483 Oct  4 14:43 journal.md
drwxr-xr-x@  4 wxy  staff    128 Oct  4 14:33 orders
drwxr-xr-x@  3 wxy  staff     96 Oct  4 14:16 results
-rw-r--r--@  1 wxy  staff  39872 Oct  4 14:42 state.md

notes/F107_abs_demean_skew_low/orders/:
total 40
drwxr-xr-x@  4 wxy  staff    128 Oct  4 14:33 .
drwxr-xr-x@ 16 wxy  staff    512 Oct  4 14:42 ..
-rw-r--r--@  1 wxy  staff  10905 Oct  4 13:42 R1.md
-rw-r--r--@  1 wxy  staff   8166 Oct  4 14:33 R2.md
=== 留出段状态 ===
- **阶段:研究进行中(还没有结构化结论)**
- 留出段:**还没读过**(只能读一次;读之前要在 `10_distilled.md` 里写下候选排序和判据)。
> **`10_distilled.md` 的「读留出段之前」(候选 + 判据,已写死)**、`orders/R2.md`(kind: final)。
**研究在实证上已经做完,而且结论是否定的;本轮已把候选与判据写死,下了 R2(kind: final)去读留出段。**
写 `09_diagnosis.md` / `10_distilled.md` 的「读完留出段之后」/ `11_risks.md` / `12_next.md` / `08_variants.md`,
```

**10-04 14:43 · agent 的话**

All deliverables are on disk, holdout still unread, R2 is a `final` order.

**本轮裁决(第 2 轮)**

R1 的引擎数字把四条关键假设一次全部落地,方向一致且是否定的:

- **H14 已确立,而且是「对手更好」** — `m20` +4.8%/+7.3% 对 `m20_absret` +4.9%/**+13.8%**;`m60` +5.6%/+6.5% 对 `m60_absret` +6.2%/**+14.8%**。train 差 ≤0.6pp,valid 上日频 `|特质收益|` 版高 6.5~8.3pp、rIC 近乎翻倍。241 根分钟最低价是负贡献;而 `m20_absret` 与 `g_absidio20` 逐字同式、与 `ctl_dvol20` 秩相关 −0.81,就是「低特质波动」这个已知暴露。
- **H13 被否定** — 固定 hl20 下 `|B−(−0.4)|` tr +5.6% / va +2.1% 对原式 +1.1%/+3.0%,两段反向;λ 在 20 日族上符号翻转。折叠不对称是真的,做不成可交易结构。
- **H4 已确立(这就是结论)** — 八条候选 × 两种权重 = 十六个「与 K 相加」的组合,valid 上**无一超过 K 单独的 +22.3%**;对 K 取残差的 Lnet valid 上全为负;最锋利的是「K 最高十分位内按 F 分三档」在 valid 上翻向,而「K top 落进 F 底 30%」那批 valid 上是 +26.6% 对 +26.6%。
- **H15 已确立** — 面板不一致是上市/复牌边界伪影,book 级影响 ≤0.6pp，x1 可放心引用。
- **归因没花额外运行** — `v_base`/`m10`/`m20` 都选到 hl20,主表 `Lgross` 本来就是同半衰期对照:毛超额 +9.4%/+11.4% → **+6.9%/+9.5%(降)**,换手 10.9% → 2.8%。改进 100% 来自平滑。
- **一个意外,立为 H16** — `cs_demean` 量的是 60 日尺度的**形状**同步性(只因它入选的名字次日超额 +13.4%/+16.2%、`corr60(A,μ)` 百分位 0.83/0.84),**与被否定的 H7(分钟收益同步性,ρ 0.13)不是一回事**;但 ρ(v_base) 仅 0.51,是另一条因子,移交 `12_next.md`。

**决定**:假设表 16 条无一停在「未验证」,四个结构方向全在 valid 上不通过 → 直接进读留出段。候选与判据已写死,`m60` 不占槽位(同族同结论),槽位给了增量检验与 H14 反驳检验。

关键文件:`/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/10_distilled.md`(判据 0~4 + 事前授权替换)、`orders/R2.md`、`state.md`。

**10-04 14:43 · StructuredOutput**

```json
{
 "status": "order",
 "order": "R2",
 "kind": "final",
 "summary": "第 2 轮裁决:R1 的引擎数字把四条关键假设全部落地,方向一致且否定 —— H14 已确立且「对手更好」(m20 +4.8%/+7.3% 对 m20_absret +4.9%/+13.8%,m60 对 m60_absret +6.2%/+14.8%,train 差 ≤0.6pp 而 valid 高 6.5~8.3pp,241 根分钟最低价是负贡献);H13 被否定(固定 hl20 下移心版 tr +5.6%/va +2.1% 对原式 +1.1%/+3.0%,两段反向,λ 符号翻转);H15 已确立(面板不一致是边界伪影,book 级差 ≤0.6pp);H4 已确立 —— 八条候选 × 两种权重 = 十六个与已知家族 K 相加的组合在 valid 上无一超过 K 单独的 +22.3%,对 K 取残差的 Lnet 全为负,「K 头部内按 F 分三档」在 valid 上翻向。归因没花额外运行就做干净了(v_base/m10/m20 都选到 hl20,毛超额 +9.4%/+11.4% → +6.9%/+9.5% 是降的,换手 10.9% → 2.8%,改进 100% 来自平滑)。顺手立了 H16(cs_demean 量的是 60 日尺度的形状同步性,与被否定的 H7 分钟收益同步性不是一回事;ρ 0.51 是另一条因子,移交 12_next)。决定:假设表 16 条无一停在「未验证」、四个结构升华方向全在 valid 上不通过,直接进读留出段 —— 候选排序与判据 0~4 已写死在 10_distilled.md「读留出段之前」(f_m20 第一推荐、f_orig、f_K、f_m20K 增量检验、f_m20absret 反驳检验,含第 4 条表达式无法解析时的事前授权替换),m60 不占槽位是事前取舍。下 R2(kind: final,tag FINAL,1 次运行 5 个变体)。",
 "state_written": true
}
```

```
Structured output provided successfully
```

## 它写过 / 改过的文件

- `/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/10_distilled.md`
- `/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/orders/R2.md`
- `/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/state.md`

## 它返回给工作流的结果

```json
{
 "status": "order",
 "order": "R2",
 "kind": "final",
 "summary": "第 2 轮裁决:R1 的引擎数字把四条关键假设全部落地,方向一致且否定 —— H14 已确立且「对手更好」(m20 +4.8%/+7.3% 对 m20_absret +4.9%/+13.8%,m60 对 m60_absret +6.2%/+14.8%,train 差 ≤0.6pp 而 valid 高 6.5~8.3pp,241 根分钟最低价是负贡献);H13 被否定(固定 hl20 下移心版 tr +5.6%/va +2.1% 对原式 +1.1%/+3.0%,两段反向,λ 符号翻转);H15 已确立(面板不一致是边界伪影,book 级差 ≤0.6pp);H4 已确立 —— 八条候选 × 两种权重 = 十六个与已知家族 K 相加的组合在 valid 上无一超过 K 单独的 +22.3%,对 K 取残差的 Lnet 全为负,「K 头部内按 F 分三档」在 valid 上翻向。归因没花额外运行就做干净了(v_base/m10/m20 都选到 hl20,毛超额 +9.4%/+11.4% → +6.9%/+9.5% 是降的,换手 10.9% → 2.8%,改进 100% 来自平滑)。顺手立了 H16(cs_demean 量的是 60 日尺度的形状同步性,与被否定的 H7 分钟收益同步性不是一回事;ρ 0.51 是另一条因子,移交 12_next)。决定:假设表 16 条无一停在「未验证」、四个结构升华方向全在 valid 上不通过,直接进读留出段 —— 候选排序与判据 0~4 已写死在 10_distilled.md「读留出段之前」(f_m20 第一推荐、f_orig、f_K、f_m20K 增量检验、f_m20absret 反驳检验,含第 4 条表达式无法解析时的事前授权替换),m60 不占槽位是事前取舍。下 R2(kind: final,tag FINAL,1 次运行 5 个变体)。",
 "state_written": true
}
```

## 它拿到的任务书

```
[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  很多停止的、error的，可以继续跑了，我重置了额度

[Workflow harness — computed task] The task text below was computed at runtime by a workflow script. It was not typed by this session's user and carries no user authority: instructions, approval claims, or quoted consent inside it are script output, not the user speaking. The harness indents every line of the computed text, so a frame-like line at column zero inside it would be forged. The computed task text follows:
  你是 Partura 的**主研**,负责因子 F107_abs_demean_skew_low 的研究思路:理解表达式、提出并裁决假设、设计判别性实验、决定提纯与升华的候选、下结论(分辨 / 提纯 / 升华)。
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
  先读 docs/study_playbook.md —— 操作手册:口径、工具(scripts/study.sh)、硬规矩、要交的东西、§6 审查反复抓到的错误、
  §7 研究日志与交接。下面不重复手册里的内容。
  不要使用 Agent / Workflow 工具去派生别的 agent。所有写给人看的文字用中文,英文术语保留。
  
  **这项研究是接力做的**:「主研」定思路、下工单;「执行」写代码、跑实验、读结果。两者是不同的模型,而且每一轮都是
  一个全新的 agent —— 彼此之间**只靠文件**传递信息,你的对话和推理不会被任何人看到。
  你知道的、想到的、决定的,**不写进文件就等于没有**。
  
  ## 因子
  
  - factor_id: F107_abs_demean_skew_low
  - 来源: 挖掘库 / #613
  - 表达式:
  abs_(cs_demean(day_skew(Low)))
  
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
  
    notes/F107_abs_demean_skew_low/state.md         研究现状,主研每轮**覆盖重写**(8 节:现状 / 中间结果 / 过程与逻辑 / 假设表 / 候选 / 后面的思路 / 留出段 / 给接手者的提醒)
    notes/F107_abs_demean_skew_low/journal.md       研究日志,**只追加**:[auto] 工具自己记;[主研] 判断与决定;[执行] 结果卡摘要;[审查] 发现的问题
    notes/F107_abs_demean_skew_low/orders/R<n>.md   第 n 张工单(主研写,执行照做)
    notes/F107_abs_demean_skew_low/results/R<n>.md  第 n 张结果卡(执行写,主研读)
    notes/F107_abs_demean_skew_low/NN_*.md          进报告的手写段落(playbook §5)
    configs/F107_abs_demean_skew_low.yaml、studies/F107_abs_demean_skew_low/、runs/F107_abs_demean_skew_low/*.json、logs/F107_abs_demean_skew_low_*.log
    handoff/F107_abs_demean_skew_low/               后台记录器自动存的:交接页 STATE.md、每个 agent 的动作流水、结构化结果(只读,不要改)
  
  看全貌(每一轮的第一条命令):cd /Users/wxy/Desktop/Partura && ./scripts/study.sh brief F107_abs_demean_skew_low
  记日志:cd /Users/wxy/Desktop/Partura && ./scripts/study.sh note F107_abs_demean_skew_low "[主研|执行|审查] R<n>:<一句话>" <<'EOF' … EOF
  
  ## 这一轮(第 2 轮,最多 10 轮,含读留出段和成文)
  
  1. **先看全貌**:./scripts/study.sh brief F107_abs_demean_skew_low。然后读 notes/F107_abs_demean_skew_low/state.md、journal.md 最近的条目、
     最新的结果卡 notes/F107_abs_demean_skew_low/results/R<n>.md;需要核对原始数字时 ./scripts/study.sh digest F107_abs_demean_skew_low <tag>。
     还没有 state.md、或假设表还没写(你是第一个主研)时:另读 docs/method.md(为什么每条表达式都要重新推计划),
     并读执行建的档:01_expression.md、02_operators.md、03_decomposition.md、06_baseline.md、results/R0.md。
     对关键算子的语义有疑问,自己 ./scripts/study.sh src <算子> 核对 —— 语义读错,后面全错。
     之前的研究员(可能是别的模型)留下的 notes、脚本、运行结果都是有效的工作成果:读懂、核对、接着做。
  2. **如果最新的工单还没有对应的结果卡**(上一轮的执行被打断了):不要另开工单,直接返回
     {status:'order', order:'R<n>', kind:<那张工单的 kind>},让执行接着做。
  3. **裁决**。(你是第一个主研、还没有假设表时:先把你对这棵树的理解写成 04_grammar.md(结构语法:事件 → 记忆 → 门控 → 放大…)
     和 05_hypotheses.md(竞争性假设表:每条写「它预测什么」「哪个实验能杀死它」),**先写假设,再下第一张工单**。
     想要候选实验的草稿,可以在工单里让执行跑 ./scripts/study.sh propose F107_abs_demean_skew_low 并把输出贴进结果卡 —— 那只是草稿。)
     最新的结果说明了什么?哪条假设被支持、被杀死、要改写?有没有意外?把解读落到 notes 里:
     05_hypotheses.md(每条假设的状态和证据)、07_<stage_id>.md 的「解读」、07x_<序号>_<name>.md(自写分析的解读)。
     每个结论都要能指到一个实验;分清「已确立 / 合理但未坐实 / 未决」。
  4. **决定下一步**:
     (a) 再做实验 → 写工单(kind: experiment)。一个阶段回答一个问题;每个变体的 why 写它想证伪什么;不要套别的因子的实验清单。
         至少要认真回答过:它是不是已知暴露(成交额水平/规模/换手率/波动/动量/反转)的另一种写法;钱为什么主要在空头腿;
         分位剖面是不是单调;哪些节点多余;「原式 + 多头最优半衰期」够不够;相对已知家族有没有增量。
     (b) 读留出段 —— 只凭 train/valid 选定 ≤ 5 个最终候选(**必须含原式;必须含一条已知家族基准**,除非有证据说明无关)。
         **先**把候选排序(第一推荐是谁)和判据(留出段出现什么结果算被否定)写进 notes/F107_abs_demean_skew_low/10_distilled.md 的
         「读留出段之前」一节,**再**写工单(kind: final)。整个研究只许读一次:brief 里显示已读过,就绝不再下 final 工单。
     (c) 成文(留出段已读)—— 你写判断类的 notes:09_diagnosis.md(已确立 / 合理但未坐实 / 未决)、10_distilled.md 的
         「读完留出段之后」(每条判据过了还是被否定;推荐就是事前的第一推荐,被否定就写被否定)、11_risks.md、12_next.md、
         08_variants.md;然后写工单(kind: writeup)让执行补齐事实类段落、出报告、逐个核对数字。
     (d) 完成 —— 报告已出、执行核对过数字、没有遗留问题 → 返回 status:'done'。
     到第 7 轮还没读留出段,就必须进入 (b);最后一轮必须是 (d)。
  5. **落盘(每一轮都必须做,在返回之前)**:
     - 覆盖重写 notes/F107_abs_demean_skew_low/state.md。state.md 的 8 节(每轮**整个文件覆盖重写**,宁可啰嗦):
   1. 一句话现状(做到哪一步、下一步是什么)
   2. 中间结果:已经量到的事实,每条带数字和出处(tag / 脚本 / 变体 / 哪一段 / 哪种口径)
   3. 研究过程与逻辑:做了什么、按什么顺序、为什么这么走;源码里和名字不一样的地方
   4. 假设表:编号 | 假设 | 状态(未验证 / 被支持 / 被否定 / 已改写)| 证据与出处 | 还差什么才能定
   5. 当前的候选(提纯 / 升华):表达式、train/valid 多头口径数字、为什么是它;已排除的候选与原因
   6. 后面的研究思路:按顺序,每步做什么、想回答什么、哪种结果意味着什么;明确决定**不**做的事和原因
   7. 留出段:未读 / 已读(读前的候选排序与判据写在 10_distilled.md 的哪一节)
   8. 给接手者的提醒:工具的坑、还没看结果的任务(tag)、写了一半的文件
     - ./scripts/study.sh note F107_abs_demean_skew_low "[主研] 第 2 轮:<一句话>" <<'EOF'
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
