# F104_kurt_masktop_amt — 研究现状(2026-10-05 主研重写;接手者先读这一页)

## 1. 现状

批量扫描 s1(70 个变体)+ 市场解剖已跑完并读完。综合写在 `notes/F104_kurt_masktop_amt/synthesis.md`(每个论断带变体 id 和数字),
第二批 38 条假设写在 `studies/F104_kurt_masktop_amt/hypo.yaml`(`study.sh hypo` 38/38 通过,尚未回测)。
**留出段(holdout)在 2026-10-04 已经读过一次(tag `final`),绝不能再读。**

结论分两层:
- **原式**(`day_kurt(nt_cs_mask_top_replace_mean_neg(abs_(Amt)))`):对只做多的用户 **none_robust** —— 相对已知成交额族没有增量。
  (与 2026-10-04 修订版一致,但这次是在 70 个变体的大表上确认的,不再依赖小样本逐轮实验。)
- **新的东西**:这棵树里的 **mask 是一个真的、可交易的「流动性下限」**。
  候选 `sub_C_day_std` = `day_std(nt_cs_mask_top_replace_mean_neg(abs_(Amt)))`,
  **纯多头夏普两段都显著高于已知族基准**。它 ρk = 0.85,必须按**已知成交额族的改良成员**上报,不是新因子。

## 2. 中间结果(口径:多头腿扣 15bp 净超额 / 纯多头夏普,train 2018–2021 / valid 20220101–20230807 / utrain 合并)

基准 `k_known = cross_mean(day_std(Amt), 30)`:+12.6% / +22.3% / +15.4%,Lshp 1.78 / 3.46 / 2.22,LTO 3.4%。

| 变体 | 表达式 | Lnet tr/va/ut | Lshp tr/va/ut | LTO | ρo | ρk |
|---|---|---|---|---|---|---|
| v_base | 原式 | +4.8 / −5.8 / +1.8% | 1.00 / −1.24 / 0.38 | 7.0% | 1.00 | 0.26 |
| **sub_C_day_std** | day_std(mask(abs_(Amt))) | +12.0 / +15.5 / **+13.0%** | 2.49 / 3.98 / **2.85** | 4.1% | 0.12 | 0.85 |
| sub_A_sqrt(=pow_05) | day_kurt(mask(sqrt(Amt))) | +12.2 / +18.8 / +14.1% | 1.81 / 3.29 / 2.18 | 4.0% | 0.84 | 0.60 |
| sub_C_day_ar1 | ar1(mask(abs_(Amt))) | +9.0 / +16.5 / +11.2% | 1.47 / 3.05 / 1.88 | 6.5% | 0.04 | 0.78 |
| sub_A_log | day_kurt(mask(log(Amt))) | +8.7 / +13.0 / +10.0% | 1.46 / 2.23 / 1.68 | 4.7% | 0.24 | 0.82 |
| mem_min10 | cross_min(原式, 10) | +6.0 / +8.1 / +6.6% | 1.05 / 2.25 / 1.27 | 2.9% | 0.66 | 0.38 |

坏的一端:abl_B(删 mask)ut −5.0% / ρk **−0.35**;nt_cs_rank 替代 −16.7%;nt_cs_quantile_q50 −28.1%;
pow_1_5(凸变换)−50.6%(cov 0.23 ✗);cross_zscore 5/10/30/60 全崩 −28.6~−10.8%(换手 12~33%)。
overlay 六条(已知族 + λ·原式,λ = ±0.25/±0.5/±1.0)ut = 13.1 / 12.4 / 11.5 / 10.8 / 9.0 / 3.7,**全部严格低于 15.4**;
res_known −0.4%、res_liq +0.9%、bk_known −2.0% ✗、bk_liq −1.2% ✗。

解剖(utrain 全市场多头书;段内 = 只在该段建书):
原式只在 **6.5% 的冻结盘口段**(段等权 −67.4%)段内 **+12.1%**,在无冻结的 93.5% 段 **−0.3%**;
成交额五档段内 −4.0 / −6.8 / −6.9 / −3.6 / **+7.4%**(书却超配最低档 +25.1pp,该档段等权 +15.1%、最高档 −17.8%);
主板 +4.9 / +6.9,创业板 −3.5、科创板 −6.9;次新(7.1%)−9.7%;逐年 +5.5/+6.4/+1.4/+5.8/**−3.9/−8.7**;缩量日 +4.7% vs 放量日 −1.7%。
候选 sub_C_day_std:四板块全正(+8.5/+14.5/+18.7/+8.8),成交额五档段内 −1.5/+1.6/+0.3/+0.3/+1.9(**唯一不为负的一列**,基准是 −4.1/−5.3/−8.2/−5.2/+2.5),
书落在第二档(+43.9pp,最低档只 +5.9pp),逐年 18.6/13.7/6.2/9.4/16.8/13.6 全正。

## 3. 过程与逻辑

读算子定义 → 发现 `nt_cs_mask_top_replace_mean_neg` 名字三处骗人(遮的是**最低** 10%,沿**股票轴**,替换值是**市场级**截面均值 M[d,m],
比被遮票自身大 10~100 倍)→ 由此推出 day_kurt(masked) 是流动性的**驼峰型**函数、书是杠铃(解剖里得到证实:成交额档超配 +25.1 / −7~−13 / +6.1pp)
→ 再看三类变体:删 mask 翻号(mask 定符号)、换 reader 时「保尺度 / 持续性」赢而「标准化高阶矩」输、前置凹变换单调改善
→ 统一解释:**多头腿的钱全在 mask 漏进来的成交额水平里,而 day_kurt 的工作恰恰是把它除掉** → overlay/残差全败,确认原式无增量;
但 `day_std(masked)` 把最死的票挤出书(它们大半分钟写着 M),等于一个可交易的流动性下限,夏普优于基准 → 这才是研究产物。

## 4. 假设表(第二批,38 条,`studies/F104_kurt_masktop_amt/hypo.yaml`,未回测)

A 连续无漂移的底十分位标记(6):`nt_cs_rank(Amt)` 的 day_mean / q25 / min,`day_pos_ratio(nt_cs_quantile_q75(Amt))`(修 sub_B 的 dist ✗)。
B 死分钟直读(5):day_zero_ratio / day_flat_ratio / day_flat_run_max + cross_mean/cross_max;Ret 与 Amt 零占比之差 = 封板排队。
C 保 mask 换 reader(6):day_mean / day_quantile_q25 / day_centroid;候选 + 30 日均值 / 低尾均值;遮最高一成的镜像。
D 压缩杠杆(4):Amt^0.25、sqrt×day_std、sqrt×ar1、log×day_std。
E 新叶子(4):\|Ret\| × kurt / std、sqrt(Volume)、5 分钟量变化率 × day_std。
F 分段写进表达式(6):已知族 + 剔最清淡 20% / 剔死分钟 / 剔封板 / 剔次新;原式关进最活跃 40% 与最清淡 40%。
G 状态与新算子(7):个股放缩量比做段;in_madz 的自身历史门槛;day_gini;day_signed_ratio;cross_tail_mean_q25。

## 5. 候选

1. **`day_std(nt_cs_mask_top_replace_mean_neg(abs_(Amt)))`**(sub_C_day_std)—— 第一推荐,按已知族改良成员报。
   判据:夏普 2.85 vs 2.22(两段都高、超 ±0.3 噪声);净超额 13.0 vs 15.4(valid 低 6.8 点,是它的弱点);ρk 0.85。
2. `day_kurt(nt_cs_mask_top_replace_mean_neg(sqrt(Amt)))`(sub_A_sqrt)—— ρo 0.84 还保着原式的序,ut +14.1%;多空 LS 4.79/5.04 是全表最好,但那不是用户的口径。
3. `cross_min(原式, 10)`(mem_min10)—— 若一定要交易原式:换手只有 2.9%、valid 为正(+8.1%),但 +6.6% 远低于基准,不值得。
原式本身 **不是候选**。

## 6. 后面的思路

- 先跑第 4 节的 38 条;最该先看的是 F 组(h_known_nofloor / h_known_nofrozen):若显式下限就追平了候选,mask 可以整条删掉,结论变成「已知族 + 一个剔除器」。
- 其次是 C 组 h_mask_mean 与 h_mask_std_m30:把「下限」「二阶矩」「一天 vs 一个月」三件事拆开。
- 若 A 组(nt_cs_rank 一族)能达到候选的水平,整棵树都可以用一个有界、无尖峰、不随市场量漂移的量替代 —— 那是更干净的产物。
- 候选若要上报,还需要:(i) 它与 F001 成员 `cross_max(day_std(Amt), 9)` 的相关与对比(本次大表没放这条基准);(ii) 多头腿最大回撤(大表不出这一列)。

## 7. 留出段

**已用掉(2026-10-04,tag `final`,5 条候选)。不得再读。** 本轮所有数字都来自 train / valid,没有碰 holdout。
若要为候选 sub_C_day_std 申请第二次留出段,必须先由用户同意,并在读之前把排序与判据写进 `10_distilled.md`。

## 8. 给接手者的提醒

- **算子按定义理解,不要按名字**:`nt_cs_mask_top_replace_mean_neg` 遮的是最低 10%、替换值是市场级截面均值;
  `cs_regres(Y, X)` 返回残差不是系数;`cs_quantile_qXX` flag 的是**上** XX% 的带;`cross_*` 滚交易日轴;`in_slice(x,a,b)` 是闭区间。
- `sqrt` 与 `pow_05` 是同一个算子,大表里占了两行(sub_A_sqrt / sub_A_pow_05 数字完全相同)。
- 大表的多头半衰期网格封在 **hlL = 20**,很多变体正好取到上限;旧版 state 的 rev2 网格外实验显示 train 最优在 30~40。
  比较「水平类」变体时要记得这个截断。
- `cs_bucket_rank` 在这条因子上即使修了并列也过不了 dist(bk_liq 0.20、bk_known 0.20 ✗),别再用它做中性化;用 `cs_first_*/cs_last_*`。
- 用 `cs_first_*` / `cs_last_*` 时,y 必须写成「高 = 该买」(已知族要加 `neg`),否则 sg 取 −1 会把哪一段在书顶整个翻掉。
- 布尔输出 + day_kurt 会因为取值太少被 cov/dist 误杀(sub_B_q75:ut +7.9% / Lshp 1.73 却 cov 0.79 / dist 0.15 ✗);要连续化(day_pos_ratio / day_mean)。
- 旧 notes(01~12、07x_*)是 2026-10-03/04 那一轮的,口径与结论**以本页和 synthesis.md 为准**。
