# F115_all_tide_mean_30 — 交接状态

_自动生成于 2026-10-05 10:53(`python scripts/recorder.py --brief F115_all_tide_mean_30` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:手写 all_tide_mean_30(批次 B01_single_factors)
- 表达式:`cross_mean(div(div(sub(day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5))))), day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), sub(day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), 20)`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- **留出段已经读过 1 次**(10-05 00:11)—— **不许再读**。候选在留出段上的数全在 `runs/F115_all_tide_mean_30/final.json`(`./scripts/study.sh digest F115_all_tide_mean_30 final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `lead:F115_all_tide_mean_30#3`:失败,几乎没做事
  - `lead:F115_all_tide_mean_30#1`:已返回结果,最后动作 10-04 23:49 → `handoff/F115_all_tide_mean_30/agents/lead_R1_a191df6528a633604.md`
  - `work:F115_all_tide_mean_30#1`:中断,最后动作 10-05 00:20 → `handoff/F115_all_tide_mean_30/agents/work_R1_a5f7381bf31230aef.md`

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F115_all_tide_mean_30` 看服务器上的 tag,`./scripts/study.sh digest F115_all_tide_mean_30 <tag>` 重看结果)。

## 研究现状(`notes/F115_all_tide_mean_30/state.md`,10-04 23:48 更新)—— **先读这个文件**

# 研究现状 — F115_all_tide_mean_30

_主研每轮**覆盖重写**。2026-10-04,**第 3 轮**(Opus 5):裁决 R2、写满 `05_hypotheses.md`「R2 裁决」
+ 07/07x「解读」、**事前登记 `10_distilled.md`**、下 `orders/R3.md`(kind: final)。没跑实验。
**本文件只放结论和指针。**_

## 1. 一句话现状

**实验做完、结论写死、`R3 = final` 已下 —— 下一步是执行跑那唯一一次留出段运行(`S_final`,1 次)。**
3 阶段 + 2 脚本全部 exit 0;H1–H10 全有裁决;6 个必答问题全答完(§4 末)。

**全局判断**:
1. **对只能做多、扣 15bp 的用户不可用**:valid 多头腿净超额 **+0.2%**(夏普 +0.04),换标签约定
   (`buyable=False`)翻成 **−0.39%**;已知家族同段 **+22.3%**(夏普 3.46)。
2. **衰减是它自己的**(非环境/成本/半衰期):`c_pure` 逐年 `Lnet` +7.8/+13.4/+5.2/**−1.3/+0.9/+3.6%**
   (2018→2023),已知家族同六年全 ≥ +6.6%;valid 是**毛**崩塌(`Lgross` 9.4→4.1%)。
3. **相对已知家族没有增量**(H6,§2.2)。→ 归宿 = **否定结论 + 一条提纯(删 `÷M`)**,**没有升华版。**

(…全文 6467 字符,读 `notes/F115_all_tide_mean_30/state.md`)

## 研究日志(`notes/F115_all_tide_mean_30/journal.md`:17 条,其中研究员自己写的 7 条)

最近的 5 条(更早的和全文看文件):

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

### 2026-10-04 23:49 [主研] 第 3 轮:裁决 R2(H6 支持/H10 否定/H9 否定并改写成 H9b/H7b 确认),事前登记 10_distilled.md,下 R3 = kind: final 读留出段

R2 的 5 变体 + increment.py 都 exit 0,四条判读全部命中或落在工单那张表上,没有要补的实验。

裁决(全文在 05_hypotheses.md 的「R2 裁决」一节):

1. H6「对只做多的用户相对已知家族没有增量」—— **已确立**。权重曲线在 valid 上两条独立的 X 都严格单调
   下降、w=0(纯 k_stdamt_mean30 +22.33%)全程最高,降到 w=1 的 0.25%/1.96%。量级上我刻意写成
   「拿不到增量」而不是「掺进去会亏」:w<=0.25 的下降(-0.3~-1.9pp)本身在 ±3pp 噪声带内,能确立的是
   点估计在 5 个步长单调向下 + 两条 X 同向 + 到 w=0.5 的 -4.7pp 才超出噪声带。第二条独立证据是残差:
   rIC 两段保正(+.0076~+.0225)但残差的**毛** Lgross 在 valid 6 组全负 —— 这是工单那张表没列出的第三
   种情形,正确读法是「秩空间还剩一点信息,但不在多头端」,不是「成本效应」(翻负的是毛不是净),
   也不是「alpha 全没了」。它和 R1 已确立的「顶端不单调 Q10<Q9」是同一件事的两种测法。

2. H10「潮汐定位是纯装饰」—— **被否定**,两条独立理由:a_fixwin95 表现最差(+4.3/-9.7%,比零假设
   a_plain_ret 还差,valid 剖面 Q9 +1.7% -> Q10 -6.1% 全档最低);而且它与原式相关只有 +0.54 < 0.8,
   按 playbook 本来就不是这棵树的提纯版而是另一条因子。所以提纯结论停在「只删 ÷M」,前三层不能删。
   同时纠正 R1 解读里一个诱人的错:I/F/M 的分位数近常数说的是边际分布窄,不等于逐格不变 ——
   预测力恰好在「逐格偏离中位数」那部分。注意这不救这条因子:定位的边际仍只有 +1.6/+2.5pp。

3. H9「空头腿被买不进的票抬高」—— **被否定**(short_gross 26.10->27.20、LS 只掉 0.03),用户表里
   LS 2.29 不是买不进的票撑的,一个常见陷阱干净排除。但它的**镜像**成立,我立为 H9b 并算
…(这条日志还有后文,读 journal.md)

### 2026-10-05 00:06 [auto] ⚠ 读留出段:final S_final,阶段 S_final(留出段只能读这一次;候选与判据应当已经写在 10_distilled.md 里)

### 2026-10-05 00:12 [auto] S_final 跑完(exit 0);重看结果:./scripts/study.sh digest F115_all_tide_mean_30 S_final

## 工单与结果卡(`notes/F115_all_tide_mean_30/orders/`、`notes/F115_all_tide_mean_30/results/`)

- R0:工单 —,结果卡 有
- R1:工单 有,结果卡 有
- R2:工单 有,结果卡 有
- R3:工单 有,结果卡 **还没有(待执行)**

## 配置里的实验计划(`configs/F115_all_tide_mean_30.yaml`)

- 标题:(读完这棵树之后,用一句话写它是什么)
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base
- **S1_anatomy**(8 个变体):N = L x (1/M) 的三个通道里预测力在哪一个;拆掉潮汐定位之后还剩多少?
  a_no_rate、a_width_only、a_plain_ret、a_rank_pre、a_abs、a_win30、a_win60、k_stdamt_mean30
- **S2_increment**(5 个变体):对只能做多的用户,这条因子掺进已知家族有没有增量?潮汐定位是不是只等于一个固定子窗口?
  a_fixwin95、c_pure、k_stdamt_max9、m_blend_base_k30、m_blend_pure_k30
- **S_final**(5 个变体):留出段(20230808 起):事前写死的否定结论与提纯结论成立吗?相对已知家族有没有增量?
  f_orig、f_pure、f_k30、f_k9、f_blend

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F115_all_tide_mean_30`)

- `S0_baseline`  10-04 12:01  1 个变体  → `./scripts/study.sh digest F115_all_tide_mean_30 S0_baseline`
- `S1_anatomy`  10-04 14:09  8 个变体  → `./scripts/study.sh digest F115_all_tide_mean_30 S1_anatomy`
- `S2_increment`  10-04 15:13  5 个变体  → `./scripts/study.sh digest F115_all_tide_mean_30 S2_increment`
- `S_final`  10-05 00:11  5 个变体  → `./scripts/study.sh digest F115_all_tide_mean_30 S_final`
- `sweep_s1`  10-05 10:41  121 个变体  → `./scripts/study.sh digest F115_all_tide_mean_30 sweep_s1`
- `anatomy_s1`  10-05 10:46  0 个变体  → `./scripts/study.sh digest F115_all_tide_mean_30 anatomy_s1`
- `x1_anat_mfi`(自写脚本的输出)  10-04 14:19  exit 0  → `logs/F115_all_tide_mean_30_x1_anat_mfi.log`
- `x2_increment`(自写脚本的输出)  10-04 15:27  exit 0  → `logs/F115_all_tide_mean_30_x2_increment.log`

## 已写的 notes(`notes/F115_all_tide_mean_30/`)

`01_expression.md`(3K)、`02_operators.md`(12K)、`03_decomposition.md`(6K)、`04_grammar.md`(6K)、`05_hypotheses.md`(24K)、`06_baseline.md`(11K)、`07_S1_anatomy.md`(15K)、`07_S2_increment.md`(11K)、`07x_1_anat_mfi.md`(9K)、`07x_2_increment.md`(15K)、`10_distilled.md`(8K)、`journal.md`(23K)、`state.md`(10K)

## 自写的探针与分析脚本(`studies/F115_all_tide_mean_30/`)

- `anat_mfi.py`  10-04 14:17  F115 R1 / x1_anat_mfi: anatomy of N = L x (1/M) on the six raw daily panels.
- `increment.py`  10-04 15:22  F115 R2 / x2_increment: 增量权重曲线(H6)+ 残差多头腿 + H9(封板票)+ H7b 确认(第 2 件,见

## 结构化结果(`handoff/F115_all_tide_mean_30/results/`)

(还没有)
