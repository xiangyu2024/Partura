# F115_all_tide_mean_30 — 交接状态

_自动生成于 2026-10-05 11:15(`python scripts/recorder.py --brief F115_all_tide_mean_30` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:手写 all_tide_mean_30(批次 B01_single_factors)
- 表达式:`cross_mean(div(div(sub(day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5))))), day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), sub(day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), 20)`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- **留出段已经读过 1 次**(10-05 00:11)—— **不许再读**。候选在留出段上的数全在 `runs/F115_all_tide_mean_30/final.json`(`./scripts/study.sh digest F115_all_tide_mean_30 final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `lead:F115_all_tide_mean_30#1`:已返回结果,最后动作 10-04 23:49 → `handoff/F115_all_tide_mean_30/agents/lead_R1_a191df6528a633604.md`
  - `work:F115_all_tide_mean_30#1`:中断,最后动作 10-05 00:20 → `handoff/F115_all_tide_mean_30/agents/work_R1_a5f7381bf31230aef.md`
  - `synth:F115_all_tide_mean_30`:已返回结果,最后动作 10-05 11:14 → `handoff/F115_all_tide_mean_30/agents/synth_a552a99162afbe363.md`

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F115_all_tide_mean_30` 看服务器上的 tag,`./scripts/study.sh digest F115_all_tide_mean_30 <tag>` 重看结果)。

## 研究现状(`notes/F115_all_tide_mean_30/state.md`,10-05 11:11 更新)—— **先读这个文件**

# 研究现状 — F115_all_tide_mean_30

_主研每轮**覆盖重写**。2026-10-05,**第 4 轮**(Opus 5,批量扫描口径):读完 s1 大表(121 变体)+ 市场解剖,
写 `synthesis.md`(133 行)、`studies/F115_all_tide_mean_30/hypo.yaml`(40 条,40/40 parse)、本文件。
**没跑新实验。** 本文件只放结论和指针;所有带数字的论断在 `synthesis.md` 里都标了变体 id。_

## 1. 现状

**结论没变,但原因换了,而且找到了两条真改进和一格没试过的增量构造。**

1. **对只能做多、扣 15bp 的用户,原式不可用**:`v_base` +5.6 / **+0.2** / +4.1%(tr/va/ut),Lshp 0.83;
   已知族 `k_known` +12.6 / +22.3 / +15.4%,Lshp 2.22。
2. **本质原因(这一轮新查明)**:半衰期曲线 hl0 = **−6.2%** → hl10 = +5.6%,而**毛**超额在 hl 0→20 走平
   (+9.8…+7.3%)→ 净超额**全部**是把换手从 ~21% 压到 5% 换来的,毛 ~9% 封顶。
   **它的信息是日频、薄的;已知族 hl0 就 +12.6%、LTO 3.4%、越平滑越差 —— 慢而厚。** 扣费口径里永远打不过。
3. **没增量,但不是「就是已知族」**:ρk 只 +0.26,`bk_liq` / `bk_known` 中性化不掉(+5.4/+0.7、+5.2/−0.4 ≈ 原式)。
   失败的机制是**倾斜方向相反**(§2 第 4 条),不是信息重合 —— 这给出了一格没试过的构造。
4. **121 个变体里有两条真改进**(毛超额也好、逐年也稳):`abl_C`、`rank_K`,见 §5。

(…全文 6480 字符,读 `notes/F115_all_tide_mean_30/state.md`)

## 研究日志(`notes/F115_all_tide_mean_30/journal.md`:18 条,其中研究员自己写的 8 条)

最近的 5 条(更早的和全文看文件):

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

### 2026-10-05 11:08 [主研] 批量扫描 s1 的综合

- 读完 s1 大表(121 变体)+ 市场解剖,写了 notes/F115_all_tide_mean_30/synthesis.md(133 行)与
  studies/F115_all_tide_mean_30/hypo.yaml(40 条,40/40 parse)。没跑新实验。
- 结构:载重的只有「峰后那个读数点」F(sub_I_* 不掉 +5.0/+2.2%,对称的 sub_F_* 全塌 −3.6/−12.5%);
  分母 M 空转(abl_K 与 only_K_R 在算术上都塌成 cross_mean(1/M,20),数字一致);÷J 必需(abl_L +3.8/−4.3 << abl_N +6.4/+2.0);
  幅度无用(rk ≈ 原式);外层窗口 10–60 有真平台,内层平滑参数是噪声(不平滑最好)。
- 121 个变体里只有两条真改进,而且是**毛**超额上的改进:abl_C +6.0/+7.4%(毛 +9.5/+10.8)、
  rank_K +5.3/+9.7%(毛 +8.7/+13.1),逐年六年五正,修掉了原式 2019 之后的衰减。
- 半衰期曲线揭穿本质:原式 hl0 = −6.2%,毛超额在 hl 0→20 走平 → 净超额全部是换手换来的;毛 ~9% 封顶。
  已知族 hl0 就 +12.6% 且越平滑越差 → 它的信息慢而厚,F115 的信息快而薄。
- 没增量,机制已查明:选股力在**活跃**档(成交额段内 −1.1/−4.6/−2.0/+2.7/+7.2%),段溢价在**清淡**档
  (段等权 +15.1/…/−17.8%),倾斜方向相反 → 固定权重 overlay 必然单调变差(+14.2/+12.9/+11.9 对 +15.4%)。
  表里没试过的那一格 = 倾斜交给已知族、F115 降级为桶内排序器(h_mix_known_bk*,下一批优先级最高)。
- 解剖两条可检验推断:(1) 板块段内顺序(沪 +3.8 / 深 +5.0 / 创业 +2.0 / 科创 −22.8%)与日涨跌幅上限一致;
  (2) 段内最强的两段(次新 +12.4%、冻结盘口 +18.2%)段等权分别 −28.7% / −67.4% → 对纯多头是净亏,
  这是「段内 alpha ≠ 可投 alpha」的教科书例子,hypo 里一正一反两条用来钉死。
- 工具:abl_D 因 in_slice_to_end 的 pair 维炸开 CUDA OOM
…(这条日志还有后文,读 journal.md)

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

`01_expression.md`(3K)、`02_operators.md`(12K)、`03_decomposition.md`(6K)、`04_grammar.md`(6K)、`05_hypotheses.md`(24K)、`06_baseline.md`(11K)、`07_S1_anatomy.md`(15K)、`07_S2_increment.md`(11K)、`07x_1_anat_mfi.md`(9K)、`07x_2_increment.md`(15K)、`10_distilled.md`(8K)、`journal.md`(25K)、`state.md`(9K)、`synthesis.md`(11K)

## 自写的探针与分析脚本(`studies/F115_all_tide_mean_30/`)

- `anat_mfi.py`  10-04 14:17  F115 R1 / x1_anat_mfi: anatomy of N = L x (1/M) on the six raw daily panels.
- `increment.py`  10-04 15:22  F115 R2 / x2_increment: 增量权重曲线(H6)+ 残差多头腿 + H9(封板票)+ H7b 确认(第 2 件,见

## 结构化结果(`handoff/F115_all_tide_mean_30/results/`)

- `synthesis.json`
