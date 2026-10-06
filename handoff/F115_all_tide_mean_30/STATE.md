# F115_all_tide_mean_30 — 交接状态

_自动生成于 2026-10-05 19:26(`python scripts/recorder.py --brief F115_all_tide_mean_30` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:手写 all_tide_mean_30(批次 B01_single_factors)
- 表达式:`cross_mean(div(div(sub(day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5))))), day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), sub(day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), 20)`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- **留出段已经读过 2 次**(10-05 00:11, 10-05 12:18)—— **不许再读**。候选在留出段上的数全在 `runs/F115_all_tide_mean_30/final.json`(`./scripts/study.sh digest F115_all_tide_mean_30 final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `synth:F115_all_tide_mean_30`:已返回结果,最后动作 10-05 11:14 → `handoff/F115_all_tide_mean_30/agents/synth_a552a99162afbe363.md`
  - `verdict:F115_all_tide_mean_30`:失败,最后动作 10-05 15:37 → `handoff/F115_all_tide_mean_30/agents/verdict_a95e3e90c47e6eb9a.md`
  - `verdict:F115_all_tide_mean_30`:已返回结果,最后动作 10-05 17:06 → `handoff/F115_all_tide_mean_30/agents/verdict_a77b310339e8c0e2b.md`

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F115_all_tide_mean_30` 看服务器上的 tag,`./scripts/study.sh digest F115_all_tide_mean_30 <tag>` 重看结果)。

## 研究现状(`notes/F115_all_tide_mean_30/state.md`,10-05 17:03 更新)—— **先读这个文件**

# 研究现状 — F115_all_tide_mean_30

_主研每轮**覆盖重写**。2026-10-05,**第 5 轮**(Opus 5):读完批量扫描 **s2**(169 变体 = 上一轮 40 条假设
+ 通用筛子/分段)+ 解剖,做对账与定论,写 `synthesis.md` §7–§11、`hypo3.yaml`(24 条,24/24 parse)、本文件。
**没跑新实验,测试段一行没读。** 带数字的论断在 `synthesis.md` 里都标了变体 id。_

## 1. 现状(一句话 + 三件已定的事)

**提纯成功、但量级不够;对已知族零增量,这一条已经证据饱和。**

1. **最好的自有版本是 `h_rawvol_divM_only`:+7.2 / +5.3%(tr/va),Lshp 2.01 / 1.16,LTO 4.6%,ρk 0.21。**
   = 原式,**只把分母 M 里那两个 `day_argmin` 改成用未平滑的 `in_slice(Volume,31,211)` 定位**。
   原式 `v_base` 是 +5.6 / **+0.2%**、1.21 / **0.04** —— valid 夏普 0.04 → 1.16,远超 ±0.3 噪声带,**是真提纯**。
2. **对已知族零增量,九种混合 + 两种筛子全部打平或变差**:`k_known` +12.6/+22.3%(1.78/3.46);
   最好的 `scr_xhi_p` +12.3/+22.5%(1.78/3.53)= 逐位打平;`h_mix_known_bk_rk` +11.9/+20.0% 严格更差。
   **真正要打的线是通用筛子 `k_known_xfrozen` +16.4/+23.2%、Lshp 2.81/3.98** —— 差 4pp / 1.0 夏普以上。
3. **s2 的新事实:符号随流动性翻转**。活跃 40% 段内原符号 +8.8/+13.6%(`seg_hiliq_p`),清淡 40% 段内要反符号
   +9.4/+16.1%(`seg_lowliq_m`);两段的另一半符号只有 −3.1/+4.7% 和 +1.7/+13.1%。

(…全文 6195 字符,读 `notes/F115_all_tide_mean_30/state.md`)

## 研究日志(`notes/F115_all_tide_mean_30/journal.md`:19 条,其中研究员自己写的 9 条)

最近的 5 条(更早的和全文看文件):

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

### 2026-10-05 17:03 [主研] 批量扫描 s2 对账与结论

s2(169 变体)对完账:上一轮 40 条假设里只有 1 条是真改进,优先级最高的那一格决定性失败。
真改进 = h_rawvol_divM_only(+7.2/+5.3%、Lshp 2.01/1.16、LTO 4.6%、rho_k 0.21),只把分母 M 里两个
day_argmin 改用未平滑 Volume 定位;原式 valid 夏普 0.04 → 1.16,是本因子唯一一次真提纯。整棵树去平滑
(h_rawvol_all 0.83)或再删 ÷M(h_pure_raw 0.76)都更差 —— 增益不是「少加工」,是分母那一处的污染。
零增量已饱和:9 种混合(6 固定权重 + 3 桶内 h_mix_known_bk* + 3 状态条件 h_regime_mix*)全部 ≤ k_known
+12.6/+22.3%,当筛子 scr_xhi_p +12.3/+22.5% 与 k_known 逐位打平,全都远低于通用筛子 k_known_xfrozen
+16.4/+23.2%(Lshp 2.81/3.98)。机制类假设 B/C/E/F/戊/己庚 整批否定;D 组口径被钉死成「需要跨两个半场的
长窗口」。新事实:符号随流动性翻转(活跃 40% 原符号 +8.8/+13.6%,清淡 40% 反符号 +9.4/+16.1%)。
verdict = 提纯成功但量级不够 + 对已知族零增量 + 不能当筛子。下一步:hypo3.yaml 24 条(24/24 parse),
先看 A 组能否把那一处再抬、B 组的 select_where 条件符号能否把 verdict 升格。测试段仍未读。

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
- `sweep_s2`  10-05 12:12  169 个变体  → `./scripts/study.sh digest F115_all_tide_mean_30 sweep_s2`
- `anatomy_s2`  10-05 12:18  0 个变体  → `./scripts/study.sh digest F115_all_tide_mean_30 anatomy_s2`
- `sweepfinal_s2`  10-05 12:20  8 个变体  → `./scripts/study.sh digest F115_all_tide_mean_30 sweepfinal_s2`
- `sweep_s3`  10-05 18:15  193 个变体  → `./scripts/study.sh digest F115_all_tide_mean_30 sweep_s3`
- `anatomy_s3`  10-05 18:26  0 个变体  → `./scripts/study.sh digest F115_all_tide_mean_30 anatomy_s3`
- `sweepfinal_s3`  10-05 18:31  8 个变体  → `./scripts/study.sh digest F115_all_tide_mean_30 sweepfinal_s3`
- `x1_anat_mfi`(自写脚本的输出)  10-04 14:19  exit 0  → `logs/F115_all_tide_mean_30_x1_anat_mfi.log`
- `x2_increment`(自写脚本的输出)  10-04 15:27  exit 0  → `logs/F115_all_tide_mean_30_x2_increment.log`

## 已写的 notes(`notes/F115_all_tide_mean_30/`)

`01_expression.md`(3K)、`02_operators.md`(12K)、`03_decomposition.md`(6K)、`04_grammar.md`(6K)、`05_hypotheses.md`(24K)、`06_baseline.md`(11K)、`07_S1_anatomy.md`(15K)、`07_S2_increment.md`(11K)、`07x_1_anat_mfi.md`(9K)、`07x_2_increment.md`(15K)、`10_distilled.md`(8K)、`journal.md`(27K)、`state.md`(9K)、`synthesis.md`(21K)

## 自写的探针与分析脚本(`studies/F115_all_tide_mean_30/`)

- `anat_mfi.py`  10-04 14:17  F115 R1 / x1_anat_mfi: anatomy of N = L x (1/M) on the six raw daily panels.
- `increment.py`  10-04 15:22  F115 R2 / x2_increment: 增量权重曲线(H6)+ 残差多头腿 + H9(封板票)+ H7b 确认(第 2 件,见

## 结构化结果(`handoff/F115_all_tide_mean_30/results/`)

- `synthesis.json`
- `verdict.json`
