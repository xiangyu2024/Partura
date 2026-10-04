# F107_abs_demean_skew_low — 交接状态

_自动生成于 2026-10-04 14:30(`python scripts/recorder.py --brief F107_abs_demean_skew_low` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

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
- `05_hypotheses.md`  16788 字节  10-04 14:28
- `06_baseline.md`  3894 字节  10-04 13:05
- `07_S1_parts.md`  12378 字节  10-04 14:28
- `07_S2_memory.md`  12730 字节  10-04 14:29
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
