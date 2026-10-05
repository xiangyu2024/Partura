# F115_all_tide_mean_30 — 交接状态

_自动生成于 2026-10-04 23:02(`python scripts/recorder.py --brief F115_all_tide_mean_30` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:手写 all_tide_mean_30(批次 B01_single_factors)
- 表达式:`cross_mean(div(div(sub(day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5))))), day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), sub(day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), 20)`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- 留出段:**还没读过**(只能读一次;读之前要在 `10_distilled.md` 里写下候选排序和判据)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `work:F115_all_tide_mean_30#2`:已返回结果,最后动作 10-04 15:38 → `handoff/F115_all_tide_mean_30/agents/work_R2_a8e7ee66fab3b647f.md`
  - `lead:F115_all_tide_mean_30#3`:失败,几乎没做事
  - `lead:F115_all_tide_mean_30#3`:失败,几乎没做事

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F115_all_tide_mean_30` 看服务器上的 tag,`./scripts/study.sh digest F115_all_tide_mean_30 <tag>` 重看结果)。

## 研究现状(`notes/F115_all_tide_mean_30/state.md`,10-04 14:59 更新)—— **先读这个文件**

# 研究现状 — F115_all_tide_mean_30

_每一轮由主研**整个覆盖重写**。最后更新:2026-10-04,**第 2 轮**(主研 = Opus 5)。
本轮做的是:裁决 R1 的结果(R1 已跑完、结果卡已交)、把解读写进 07/07x/05、下 R2 工单。本轮没有跑实验。_

---

## 1. 一句话现状

**R1 跑完了,这棵树的内部结构已经钉死;R2 工单已下,只剩两个问题没答案。**
R1(`S1_anatomy` 8 变体 + `x1_anat_mfi` 脚本,都 exit 0)把 H2、H3 杀死,H1、H5 支持,H4、H7b 改写/否定,
并给出**唯一一条确立的提纯结果**(整个 `÷M` 子树可以删掉)。
剩下的两个问题就是 R2 的全部内容:**(一) 对只做多的用户,它掺进已知家族有没有增量(H6);
(二) 潮汐定位是不是只等于一个固定子窗口(H10,新立)。**

**下一步**:执行按 `notes/F115_all_tide_mean_30/orders/R2.md` 做 ——
阶段 `S2_increment`(5 变体)+ 脚本 `studies/F115_all_tide_mean_30/increment.py`(tag `x2_increment`),
共 2 次服务器运行。

**全局判断(新接手的人先看这三句)**:
1. 这条因子**对用户没用**:valid 段多头腿净超额 +0.2%(纯多头夏普 +0.04),而用户指定的已知家族基准
   同段是 **+22.3%**(夏普 3.46)。
2. valid 的崩塌是**毛**崩塌(`Lgross` 9.4%→4.1%),**不是**成本、不是半衰期没调好 —— 而同一段
   已知家族的毛多头腿从 15.2% 升到 24.4%,所以**不是环境问题,是这条因子自己衰减**。
3. 因此本研究的归宿是**一个有证据的否定结论 + 一条提纯结果**,不是升华版。
   **R2 之后直接进入 (b) 读留出段,不要再铺第四个实验阶段。**

---

(…全文 17539 字符,读 `notes/F115_all_tide_mean_30/state.md`)

## 研究日志(`notes/F115_all_tide_mean_30/journal.md`:14 条,其中研究员自己写的 6 条)

最近的 5 条(更早的和全文看文件):

### 2026-10-04 15:09 [auto] 启动 run S2_increment:阶段 S2_increment

### 2026-10-04 15:13 [auto] S2_increment 跑完(exit 0);重看结果:./scripts/study.sh digest F115_all_tide_mean_30 S2_increment

### 2026-10-04 15:23 [auto] 启动 exec x2_increment:studies/F115_all_tide_mean_30/increment.py

### 2026-10-04 15:27 [auto] x2_increment 跑完(exit 0);重看结果:logs/F115_all_tide_mean_30_x2_increment.log

### 2026-10-04 15:36 [执行] R2:S2_increment(5变体)+ x2_increment 都跑完(exit 0),结果卡 results/R2.md 已写;权重曲线在 valid 上随 w 增大严格单调下降(两条 X 都是 w=0 最高),残差 Lgross train 正 valid 全负,H9 实测方向与工单预测相反

主表(train->valid Lnet):a_fixwin95 +4.3%->-9.7%(valid 全场最差,Q10 分位剖面在这批里最烂,-6.1% vs
Q9 +1.7%);c_pure(=a_no_rate 换 id 重跑)+6.4%->+2.0%,与 a_no_rate 逐数字相同,rank_corr=+1.0000,
流水线自检通过;k_stdamt_max9 +13.7%->+22.2%(全套数字第一次拿到);m_blend_base_k30 +9.6%->+17.7%
(dist=0.81);m_blend_pure_k30 +10.9%->+17.1%(dist=0.80)。符号对齐:sign(v_base)=sign(a_no_rate)=
sign(k_stdamt_mean30)=-1,按工单用 add(cs_rank,cs_rank) 写法,未改。

增量权重曲线(H6 核心判据):X=O 和 X=P 两条曲线的 valid Lnet 都随 w 从 0 到 1 严格单调下降
(22.33%->...->0.25% / 22.33%->...->1.96%),w=0(纯 k_stdamt_mean30)始终最高,没有出现"中间某个 w
不低于 w=0"。意外:auto(自动重选半衰期)与 pin(hl=0,不加二次平滑)在全部 12 个(X,w)组合上逐数字
相同,工单担心的"二次平滑代价"这次没有出现。

残差多头腿(2 因子 x 3 组控制,6 组全部同一模式):rIC train/valid 都保持正(+0.0076~+0.0225),但
Lgross(不是 Lnet)train 全正、valid 全部转负——不是成本效应能解释的那种转负。

H9:买不进标签对调后,short 腿几乎不变(train 26.10%->27.20%,valid 27.06%->26.97%),反而是多头腿在
动(valid long_net +0.25%->-0.39%),与工单预测的方向相反;对账 buyable=True 三项(long_share 0.2655、
LS +2.529、shor
…(这条日志还有后文,读 journal.md)

## 工单与结果卡(`notes/F115_all_tide_mean_30/orders/`、`notes/F115_all_tide_mean_30/results/`)

- R0:工单 —,结果卡 有
- R1:工单 有,结果卡 有
- R2:工单 有,结果卡 有

## 配置里的实验计划(`configs/F115_all_tide_mean_30.yaml`)

- 标题:(读完这棵树之后,用一句话写它是什么)
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base
- **S1_anatomy**(8 个变体):N = L x (1/M) 的三个通道里预测力在哪一个;拆掉潮汐定位之后还剩多少?
  a_no_rate、a_width_only、a_plain_ret、a_rank_pre、a_abs、a_win30、a_win60、k_stdamt_mean30
- **S2_increment**(5 个变体):对只能做多的用户,这条因子掺进已知家族有没有增量?潮汐定位是不是只等于一个固定子窗口?
  a_fixwin95、c_pure、k_stdamt_max9、m_blend_base_k30、m_blend_pure_k30

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F115_all_tide_mean_30`)

- `S0_baseline`  10-04 12:01  1 个变体  → `./scripts/study.sh digest F115_all_tide_mean_30 S0_baseline`
- `S1_anatomy`  10-04 14:09  8 个变体  → `./scripts/study.sh digest F115_all_tide_mean_30 S1_anatomy`
- `S2_increment`  10-04 15:13  5 个变体  → `./scripts/study.sh digest F115_all_tide_mean_30 S2_increment`
- `x1_anat_mfi`(自写脚本的输出)  10-04 14:19  exit 0  → `logs/F115_all_tide_mean_30_x1_anat_mfi.log`
- `x2_increment`(自写脚本的输出)  10-04 15:27  exit 0  → `logs/F115_all_tide_mean_30_x2_increment.log`

## 已写的 notes(`notes/F115_all_tide_mean_30/`)

`01_expression.md`(3K)、`02_operators.md`(12K)、`03_decomposition.md`(6K)、`04_grammar.md`(6K)、`05_hypotheses.md`(16K)、`06_baseline.md`(11K)、`07_S1_anatomy.md`(15K)、`07_S2_increment.md`(7K)、`07x_1_anat_mfi.md`(9K)、`07x_2_increment.md`(10K)、`journal.md`(19K)、`state.md`(27K)

## 自写的探针与分析脚本(`studies/F115_all_tide_mean_30/`)

- `anat_mfi.py`  10-04 14:17  F115 R1 / x1_anat_mfi: anatomy of N = L x (1/M) on the six raw daily panels.
- `increment.py`  10-04 15:22  F115 R2 / x2_increment: 增量权重曲线(H6)+ 残差多头腿 + H9(封板票)+ H7b 确认(第 2 件,见

## 结构化结果(`handoff/F115_all_tide_mean_30/results/`)

(还没有)
