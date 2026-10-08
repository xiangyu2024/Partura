# F110_ret_fair_log — 交接状态

_自动生成于 2026-10-06 11:56(`python scripts/recorder.py --brief F110_ret_fair_log` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:手写 ret_fair_log(批次 B01_single_factors)
- 表达式:`mul(sub(div(day_last(Close), day_first(Open)), 1), abs_(sub(day_mean(in_sustain_stddev(is_gt(sub(log(Volume), in_forward_valid_part(log(Volume))), add(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume)))))), Ret, 5)), day_mean(in_sustain_stddev(is_lt(sub(log(Volume), in_forward_valid_part(log(Volume))), sub(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume)))))), Ret, 5)))))`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- **留出段已经读过 2 次**(10-04 23:28, 10-05 12:06)—— **不许再读**。候选在留出段上的数全在 `runs/F110_ret_fair_log/final.json`(`./scripts/study.sh digest F110_ret_fair_log final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `synth:F110_ret_fair_log`:已返回结果,最后动作 10-05 11:21 → `handoff/F110_ret_fair_log/agents/synth_a4f321cb016b5ff04.md`
  - `verdict:F110_ret_fair_log`:失败,最后动作 10-05 15:34 → `handoff/F110_ret_fair_log/agents/verdict_a2400217486ba52bc.md`
  - `verdict:F110_ret_fair_log`:已返回结果,最后动作 10-05 16:13 → `handoff/F110_ret_fair_log/agents/verdict_a50be241e77c4e9fa.md`

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F110_ret_fair_log` 看服务器上的 tag,`./scripts/study.sh digest F110_ret_fair_log <tag>` 重看结果)。

## 研究现状(`notes/F110_ret_fair_log/state.md`,10-05 16:09 更新)—— **先读这个文件**

# F110_ret_fair_log — 研究现状(主研第 8 轮重写,2026-10-06;基于批量扫描 s2)

> 本轮工单:对账第二批假设的结果(208 条变体 + 解剖)、下定论、提第三批。**没跑任何新实验,没读测试段。**
> 产出:`synthesis.md` 的「## 第二轮(s2)对账与结论」(80 行,已按全表复核重写)+ `studies/F110_ret_fair_log/hypo3.yaml`(25 条,25/25 通过)。
> `01`~`04`/`06` 照用;`02` 对 `in_forward_valid_part` 的读法按源码纠正(第 8 节 1)。
> **本轮复核推翻了 s2 初稿的三条判断**(毛净未分、「包装不加分」、「制度互补」),见 `synthesis.md` §2 和第 8 节 2。

## 1. 现状

**结论:提纯成功、升华未成。** 原式本体仍是零(`v_base` −0.0 / −0.6 / −0.2%,`Lshp` −0.03;毛 +7.8% 被 10.6% 换手吃光,
钱在空头腿:`LS` 2.77、底腿 +43%)。但 s2 证明:**整台成交量机器可以整棵删掉**,剩下 `D × |D|` 再平滑就是一条
**净 +10.3 / +9.8%、毛 +12.9%、夏普 1.68 / 1.78、换手 3.6%、六年全正、ρk 0.41** 的独立因子(`h_cvx_ema30`)。
关键是**毛额也涨了**:原式及其全部机器变体的毛额都卡在 +7.4~+9.2,凸化把它推到 +12.9 ⇒ 不是省成本,是真信息。
仍输 `k_known` 毛 +18.0 / 净 +15.4% 和 `k_known_xfrozen` 毛 +21.1 / 净 +18.5%,**单独不够进组合**。
相对已知族的增量目前**仍是否定**,但那是在原式(ρk 0.35、多头腿为零)上测的;hypo3 的 A 组用 CVX 与两个低 ρk 版本重测,
**未测之前不下最终结论**。

## 2. 中间结果(`runs/F110_ret_fair_log/sweep_s2.json` + `anatomy_s2.json`)

`Lnet` = 多头腿扣 15bp 净超额,写 train / valid(utrain);`Lshp` 纯多头夏普;噪声 ±3 点 / ±0.3;门槛 cov ≥ 0.95、dist ≥ 0.5。
`D = sub(div(day_last(Close), day_first(Open)), 1)`;`CVX30 = cross_ema(mul(D, abs_(D)), 30)`。
基准:`k_known` +12.6 / +22.3(+15.4),`Lshp` 1.78 / 3.46;`k_known_xfrozen`(KKX)+16.4 / +23.2(+18.5),`Lshp` 2.81 / 3.98。

| id | Lnet tr / va (ut) | Lshp | LTO | 毛额 | ρo / ρk |
|---|---|---|---|---|---|
| `h_cvx_ema30` | +10.3 / +9.8(+10.2) | 1.68 / 1.78 | 3.6% | **+12.9** | 0.67 / 0.41 |
| `h_cube_ema30` | +9.0 / +8.0(+8.8) | 1.74 / **1.97** | 3.1% | +11.1 | 0.63 / 0.38 |
| `h_flat_bkt` | +9.5 / +8.1(+9.1) | 1.59 / 1.32 | 3.9% | +12.0 | 0.68 / **0.21** |
| `h_dvol_ema30`(内核) | +8.4 / +10.2(+8.9) | 1.36 / 1.67 | 3.6% | +11.6 | 0.75 / 0.37 |
| `h_liq_bkt` | +7.4 / +5.1(+6.8) | 1.19 / 0.77 | 3.8% | +9.7 | 0.66 / **0.05** |
| `h_d_ema30`(不凸化对照) | +6.6 / +8.5(+7.1) | 0.99 / 1.14 | 2.8% | +9.2 | 0.62 / 0.37 |
| `iso_C`(D,不平滑) | −1.3 / −3.3(−1.9) | −0.19 / −0.42 | 14.5% | +9.1 | 0.70 / 0.29 |
| `ov_p025` / `scr_xhi_p`(最好的已知族用法) | +10.5 / +20.6(+13.4) / +9.3 / +18.3(+12.0) | — | 2.6 / 6.3% | — | — / 0.96 / 0.94 |

**毛额换算(本轮新增工具)**:`毛 = Lnet + LTO × 0.756`(15bp 双边 × 252 天),在 s1 报过毛额的三条上复现到 ±0.1 点。
**全灭的两族**:事件后有向反应 `h_evt_*` 五条 +0.7 ~ −6.8;净买压 `h_sign_amt` −10.5 · `h_money_clock` −5.0 · `h_d_x_sign` −1.8。

## 3. 过程与逻辑

1. `D = day_last(Close)/day_first(Open) − 1` = 日内开→收收益(不含隔夜);根 = `D × S`,`S` = |放量后 5 分钟波动 − 缩量后 5 分钟波动|。
2. s1 已证 `S` 这台机器惰性(六个 ablation 在 ±0.5 内,多条变体三段数字逐位相同 ⇒ 掩码只读到「当天成交量最大的分钟」)。
3. s2 把 `S` 换成 `|D|`(凸化)或 `day_std(Ret)`:净额 −0.2% → +8.9~+10.2%,**毛额 +7.8% → +11.6~+12.9%**。
4. 平滑(`cross_ema 30`)的贡献是 **100% 省成本**:`iso_C` 毛 +9.1 → `h_d_ema30` 毛 +9.2,换手 14.5% → 2.8%。
5. 凸化的贡献是**真信息**:`h_d_ema30` 毛 +9.2 → `h_cvx_ema30` 毛 +12.9(+3.7 点)。两件事必须分开记。
6. `cs_bucket_rank(y, x)` 精确削掉 y 里被 x 解释的那一块 —— 该读 ρ 的落差,不是 Lnet(第 8 节 2)。
7. 机制:1 日日内反转 × 自身幅度,在高波动制度下赚钱(`[4]` 波动高 / 低 +18.9 / +1.4),放量(动量制度)里弱。

## 4. 假设表(第三批 25 条,`studies/F110_ret_fair_log/hypo3.yaml`,25/25 通过)

A 建在已知族上(6):CVX 叠加两档 + CVX 当筛子 + `cs_robust_z` 保幅度叠加 + 叠在 KKX 上;
  **本轮新增三条** `h3_ov_flatbkt_p05` / `h3_ov_bzliq_p05` / `h3_ov_xfroz_bkliq` —— 用 ρk 0.21 / 0.05 的低相关版本当伙伴。
B 桶内标准化(3):`cs_bucket_zscore` / `cs_bucket_demean` 按波动水平配对读 + 流动性桶内 z 单独版。
C 状态(1):只留 `cs_flip_by_state`(低波动日 +1.4% 是信号消失还是反向);两条 `select_where` 状态混合已按解剖删掉。
D 倾斜纠错(1):`sub(1, cs_rank(Amt))` 往低流动倾斜(上一轮写反了方向)。
E 冻结与封板方向(3):CVX 剔冻结 20%;`day_at_min_ratio` / `day_at_max_ratio` 分开封涨停与封跌停。
F 尺度升级(4):`day_wstd` · `day_topw_mean` · `day_es_ratio_lo` · `cross_semistd_neg`。
G 最小替换(7):CVX ema60;除自身 60 日平均幅度(治科创板);`in_index` 加权尾盘收益;`cross_age` 剔次新;
  `in_zscore_expand` 做日内因果的放量掩码(机器惰性的最后一个可能解释:阈值用了整天统计量)。

## 5. 候选

**best_own**:① `cross_ema(mul(D, abs_(D)), 30)`(净 +10.2 / 毛 +12.9 / 夏普 1.71 / ρk 0.41);
② `cross_ema(pow_3(D), 30)`(valid 夏普 1.97 最高、换手 3.1% 最低);
③ `cs_bucket_rank(cross_ema(mul(D, day_std(Ret)), 30), day_flat_ratio(Close))`(净 +9.1 / 毛 +12.0 / **ρk 0.21**)—— 最适合进组合的一条。
**best_on_known**:**无**。最好的 `ov_p025` +13.4、`scr_xhi_p` +12.0,均低于 `k_known` +15.4 和 KKX +18.5;
但全部建在原式上,A 组重测前这是**暂定**结论。

## 6. 后面的思路

1. 先看 A 组 6 条:若 `h3_ov_bzliq_p05` / `h3_ov_xfroz_bkliq` 也越不过 +18.5%,best_on_known = 无 可以收口。
2. 两处倒贴要显式处理:科创板(段内 −13.6% 却超配 +7.9%,根因 ±20% 限幅撑大 |D|)→ `h3_cvx_selfscale` / `h3_cvx_bz_vol`;
   次新(段内 +15.5% 而段等权 −28.7%)→ `h3_cvx_xage`。价格分桶和缩尾都已证明无效。
3. 别再往「按日子切制度」花算力(时段 14 格只胜 1)。增量只可能来自「按股票切、桶内中性」。
4. 冻结段(6.5%)与次新段(7.1%)都只有约 7% 的股票,而现有最细的筛子是 20% 档 —— 已提请新增 10% 档(第 8 节 4)。

## 7. 留出段

`runs/F110_ret_fair_log/sweepfinal_s2.json` **本轮没有打开**,全部结论只建立在 train(2018–2021)/ valid(2022–202308)上。
早先轮次读过留出段(见 `journal.md` 前几条),本轮工单明确禁止,故 `synthesis.md` 与本页的每个数字都来自 `sweep_s2.json` / `anatomy_s2.json`。

## 8. 给接手者的提醒

1. **`in_forward_valid_part` 是前向填充**(滞后一格、跳过 0 与 NaN),`02` 里「不是前向填充」的旧读法按源码已纠正。
   副作用:Volume 恰为 1 的分钟(log = 0)被当成无效基数跳过。`in_mean_full` / `in_stddev_full` 是**整天**统计量,
   所以掩码阈值是日级常数、日内因果不成立 —— 这正是 `h3_causal_mask_rev` 要查的。
2. **s2 初稿错了三处,已在 `synthesis.md` §2 更正**:(a) 没分毛净,把凸化的 +3.7 点真信息混进「平滑省成本」;
   (b) 只读 Lnet 就判「包装不加分」,漏掉 `cs_bucket_rank` 把 ρk 从 0.37 砍到 0.05 这件事;
   (c) 说 CVX 与 `k_known`「制度互补」,实际时段 14 格只胜 1 格,互补只在股票范围维度(12 格胜 7)。
3. `abl_I` / `sub_I_*` 那三条 −54~−81% 是**算术退化**(删 σ 后两条阈值同塌成均值、相减抵消),且 cov 0.19~0.43 没过门槛,**不算证据**。
4. **缺的东西**:① 数据层的流通市值 / 板块·涨跌幅限制宽度(科创板是唯一确认的倒贴处,没有限幅字段就只能绕);
   ② 筛子的 10% 档(`cs_last_high10` / `cs_first_low10` 等)—— 要剔的两个段都只占 ~7%,用 20% 档是过切。

## 研究日志(`notes/F110_ret_fair_log/journal.md`:25 条,其中研究员自己写的 14 条)

最近的 5 条(更早的和全文看文件):

### 2026-10-05 00:11 [主研] 第 6 轮:裁决留出段 6 条判据(J4 灰区未裁决、J5 字面过关但事前理由被推翻),推荐不变,写完全部判断类 notes,下 R4(writeup)

**看到了什么。** R3 的 `S_final` exit 0、ledger 确认 holdout 只读 1 次、7 项 canary 全过
(含 `corr(f_orig, v_base) = 1.000`)。最硬的一条外部校验:`f_known30` holdout +14.1%/+1.51
**正好落在用户给的参照 +13~15% / 1.4~1.9 里** ⇒ 段落、口径、扣费、拟合都正常,绝对水平可信,
不必退回「只读相对排序」。5 条候选 holdout 多头口径:`f_orig` −0.8%/−0.07、`f_cmT20` +4.3%/+0.47、
`f_cvxD20` **+12.8%/+1.17**、`f_cmDsig20` +9.5%/+0.99、`f_known30` +14.1%/+1.51。

**六条判据的裁决(全文在 `10_distilled.md` §7)。**
- **J0 过**(正中用户参照)、**J1 过**(原式四段 −0.0/−0.6/−0.2/−0.8%,2024 −0.2%、2025 −2.1%,
  **八年四段无一为正** ⇒ 核心否定结论被留出段确认)、**J6 过**(cov 0.9997、dist ≥0.97)。
- **J2 过,但方式不对称,必须照实写**:`Ln` +12.8% 超门槛 7.9 点,`Lshp` +1.17 只超 0.15。
  留出段变好的是**水平**(`Lg` +10.6%→+15.3%),**风险调整后没变好**(`Lshp` 1.34→1.17)。
  ⇒ 写「净超额更高、夏普持平(略低)」,**不许写「它在留出段上更好」**。
- **J3 两半都过,但比例变了**:原式→`f_cmT20` +5.08 点(`Lg` −0.35、`LTO` 10.31%→3.13% ⇒ **省成本**);
  `f_cmT20`→`f_cvxD20` +8.55 点(`Lg` **+8.68**、`LTO` 3.13%→3.31% ⇒ **真 alpha**)。
  两个机制签名在留出段完整复现,但训练段的「一半一半」变成 **37% 平滑 / 63% 结构**
  ⇒ 报告不许再写「一半一半」。
- **J4 未裁决** —— 这一条我没有当成过关写。|`cvxD20` − `
…(这条日志还有后文,读 journal.md)

### 2026-10-05 00:14 [主研] 第 6 轮补记:抽验 JSON 抓到自己两处笔误(cmDsig20 holdout Lshp = 0.986 非 0.994 ⇒ J4 夏普差 +0.19;2025 是 243 天 ⇒ 2023 后段是 96 天非 98 天),已改 notes 并写进 R4 让执行复核

下 R4 之前我把本轮新算的派生数字从 `runs/F110_ret_fair_log/S_final.json` 独立重算了一遍(没有拿结果卡
的摘要互相印证)。**16 项里 14 项完全对上**,抓到两处是我自己的转录错误:

1. **`f_cmDsig20` 的 holdout `Lshp` 是 0.986,我初稿写成了 0.994** ⇒ J4 的夏普旁证是 **+0.19**(1.175 − 0.986),
   不是 +0.18。已改 `10` §7 J4、`09` §二 A、`state.md` §4。**上一条日志(第 21 条)里的 +0.18 没法改(日志只追加),
   以 notes 为准。** 这不影响 J4 的裁决 —— 0.19 仍在 ±0.3 噪声带内,灰区未裁决的结论不变。
2. **天数**:`results/R3.md` 写「2024 242 天、2025 241 天」,但 `diagnostics.by_year` 里 **2025 是 243 天**
   ⇒ 2023 年的留出部分是 **96 天**(581 − 242 − 243),不是结果卡推的 98 天;2023 全年 242 天 ⇒ valid 部分是 146 天。
   已把全部 notes 的「98 天 / valid 144 天」改成「96 天 / valid 146 天」,并把权重三元组改成 96/242/243。
   **用正确天数重算,结论一模一样**:候选 ≈ **−0.0%**、已知家族 ≈ **+26.0%** ⇒「时间分布近乎互补」这条站得住,
   只是天数要写对。R4 第 11 项让执行从 JSON 确认 2025 的 `days`/`n_days`。

**逐项核对通过的(全精度,供执行对照)**:J3-a +5.078 / J3-b +8.545;holdout `Lg` 两步 −0.351 / +8.678;
归因 37.3% 平滑 / 62.7% 结构;J4 `Ln` 3.351;J5-a +1.256 / J5-b +0.334;
`Ln` 差距 utrain 7.44 → holdout 1.26(
…(这条日志还有后文,读 journal.md)

### 2026-10-05 11:10 [主研] 批量扫描 s1 的综合

- 原式对纯多头仍是零(utrain -0.2%/Lshp -0.03):毛 +7.8% 被 10.5% 换手(~8%/年成本)吃光,钱全在空头腿(LS +2.76、底腿 -43.3%)。
- 整棵成交量子树是惰性的:abl_E/G/J/K/N/O 全在 -0.3~+0.5%,且 sub_E_abs_/sub_E_pow_2/sub_G_add/sub_G_mul/sub_F_* 三段数字逐位相同 -0.7/+1.1/-0.2% => F/G 的差分是 no-op,掩码只读到「当天成交量最大的分钟」。唯一「一换就塌」的 I=in_stddev_full 是算术抵消退化(abl_I cov 0.19 不过门槛)。
- 平滑是唯一真实的杠杆、而且 100% 是省成本:mem_ema30 毛 +7.9% ≈ base 毛 +7.8%,换手 10.5%->3.3%,净 -0.2%->+5.4%;纯平滑天花板 +5.4%,不到 k_known(+15.4%)四成。另:base 的低换手是重尾假象 —— 先 cs_rank 再平滑(rk)换手升到 17.3%、净 -7.3%。
- 增量:叠加行两个方向都单调低于 k_known 单独(+13.4 -> +6.2% vs +15.4%)=> 加不出。残差 -7.7% 这条要带保留:rk 单独就是 -7.3%,所以那 -7% 是「排名删掉幅度」的锅不是中性化的;res_known 的毛额仍 +5.3%,被 17.2% 换手做成负 => 「残差+平滑」是唯一还没测过的干净测法。
- 解剖两条新发现:(1) 它只在 20 日成交额最高一档里段内有效(mem_ema30 +5.0%、decay60 +6.4%,该档段等权 -17.8%),而 k_known 的 +15.4% 几乎全是「超配最不流动档 +80.3%」的段位倾斜 => 两者工作方式不同;(2) 近 15 日有冻结盘口的 6.5% 股票段内 base +19.2%/mem +19.7~24.2%,而 k_known -10.9%,书对该段只超配 +1.3% => 未被利用。倒贴处是科创板(段内 -10.6% 却超配 +11.4%)。
- 已落盘:notes/F110_ret_fair_log/synthesis.md(129 行)、studies/F110_ret_fair_log/hypo.yaml(36 条,hypo 36/36 通过)、state.md 覆盖重写。另:in_forward_v
…(这条日志还有后文,读 journal.md)

### 2026-10-05 15:32 [主研] 批量扫描 s2 对账与结论

对账:上一轮 12 条推论/假设组,支持 2(A 组删机器+显式尺度、制度画像被 day_std(Ret) 保留),否定 9(价格水平放回、同类量尺度、
事件后有向反应 5 条全灭、净买压 4 条全负、残差+平滑、day_flat_ratio 单独、价格分桶抹科创倒贴、流动性加权/分桶三条无差别),
改写 1(「幅度要削尾部」→ 幅度要整条保留:cs_winsor 也不加分)。另发现上一轮把流动性倾斜方向写反了(乘 cs_rank(Amt) = 往高流动)。
定论:best_own = cross_ema(mul(D, abs_(D)), 30) +10.3/+9.8%、Lshp 1.68/1.78、换手 3.6%、六年全正、rho_k 0.41(次为 pow_3 版与
day_std(Ret) 版);best_on_known 无 —— 最好的 ov_p025 +13.4、scr_xhi_p +12.0 都低于 k_known +15.4 与 k_known_xfrozen +18.5,
但 s2 的所有叠加/筛子都建在多头腿为零的原式上,换成 CVX 重测是 hypo3 的 A 组。verdict = 提纯成功、升华未成,单独不进组合。
产出:synthesis.md 新增 73 行对账节、state.md 重写、studies/F110_ret_fair_log/hypo3.yaml 25 条(25/25 解析通过)。没读测试段。

### 2026-10-05 16:09 [主研] 批量扫描 s2 对账与结论

对账(12 组):支持 2(A 组「删机器 + 显式尺度 + 平滑」、制度画像被 day_std(Ret) 保留),否定 9(价格水平放回且 ρk 反升到 0.53;同类量尺度;事件后有向反应 5 条全灭;净买压 4 条全负;残差+平滑;day_flat_ratio 单独;价格分桶治科创板;流动性加权/分桶三条无差别且上一轮把倾斜方向写反了),改写 1(幅度要整条保留,排名 −7.3%、缩尾也不加分)。
本轮复核推翻了 s2 初稿的三条判断,已在 synthesis.md §2 更正:(1) 没分毛净 —— 用 毛 = Lnet + LTO×0.756(15bp 双边 252 天,在 s1 报过毛额的三条上复现到 ±0.1 点)算出:平滑确实 100% 省成本(iso_C 毛 +9.1 → h_d_ema30 毛 +9.2),但凸化是 +3.7 点的真信息(毛 +9.2 → h_cvx_ema30 毛 +12.9),这是两轮里毛额第一次离开 +7.4~+9.2 区间;(2)「包装不加分」只在 Lnet 一轴成立 —— cs_bucket_rank 按 flat_ratio 分桶把 ρk 从 0.37 砍到 0.21 而 Lnet 一点没掉,按流动性分桶砍到 0.05 只付 2 点,按价格分桶 ρk 没动,该读 ρ 的落差;(3)「CVX 与 k_known 制度互补」是错的 —— 逐格比,时段/状态 14 格 CVX 只胜 1 格(2019 +4.0),初稿引为证据的高波动(+18.9 vs +18.5)和缩量(+11.7 vs +11.8)都是死平;互补只在股票范围维度(12 格胜 7:成交额五档段内全胜 +5.7~+11.8、冻结段 +33.3)。
定论:best_own = cross_ema(mul(D, abs_(D)), 30) 净 +10.3/+9.8、毛 +12.9、Lshp 1.68/1.78、换手 3.6%、六年全正、ρk 0.41;次为 pow_3 版(valid 夏普 1.97 最高)与 cs_bucket_rank(…, day_flat_ratio) 版(净 +9.1、毛 +12.0、ρk 仅 0.21,三条里最适合进组合)。best_on_known 暂定为无 —— ov_p025 +13.4、scr_xhi_p +12.0 都低于 k_known +15.4 与 KKX +18.5,但全部建在多头腿为零的原式上,A 组用 CVX 和两个低 ρk 版本
…(这条日志还有后文,读 journal.md)

## 工单与结果卡(`notes/F110_ret_fair_log/orders/`、`notes/F110_ret_fair_log/results/`)

- R1:工单 有,结果卡 有
- R2:工单 有,结果卡 有
- R3:工单 有,结果卡 有
- R4:工单 有,结果卡 **还没有(待执行)**

## 配置里的实验计划(`configs/F110_ret_fair_log.yaml`)

- 标题:日内收益 × |放量后波动 − 缩量后波动|:按『成交量跳变处的价格冲击』加权的日内收益累积(方向为负 = 加权的月度日内反转)
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base
- **S1_long**(8 个变体):把平滑写进表达式(cross_mean 盒式 + 口径里的 EMA)之后,多头腿能不能站住?权重支路还重要吗?它是不是就是 20 日反转?
  w_cmT20、w_cmD20、w_cmDsig20、w_cvxD20、w_cmD60、w_cmD20lag10、w_cmDcc20、w_known30
- **S_final**(5 个变体):5 条最终候选在用户测试段上的纯多头读数(整个研究唯一一次读留出段)
  f_orig、f_cmT20、f_cvxD20、f_cmDsig20、f_known30

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F110_ret_fair_log`)

- `S0_baseline`  10-04 11:53  1 个变体  → `./scripts/study.sh digest F110_ret_fair_log S0_baseline`
- `S1_long`  10-04 15:08  8 个变体  → `./scripts/study.sh digest F110_ret_fair_log S1_long`
- `S_final`  10-04 23:28  5 个变体  → `./scripts/study.sh digest F110_ret_fair_log S_final`
- `sweep_s1`  10-05 10:40  163 个变体  → `./scripts/study.sh digest F110_ret_fair_log sweep_s1`
- `anatomy_s1`  10-05 10:48  0 个变体  → `./scripts/study.sh digest F110_ret_fair_log anatomy_s1`
- `sweep_s2`  10-05 11:57  210 个变体  → `./scripts/study.sh digest F110_ret_fair_log sweep_s2`
- `anatomy_s2`  10-05 12:04  0 个变体  → `./scripts/study.sh digest F110_ret_fair_log anatomy_s2`
- `sweepfinal_s2`  10-05 12:08  8 个变体  → `./scripts/study.sh digest F110_ret_fair_log sweepfinal_s2`
- `sweep_s3`  10-05 18:24  234 个变体  → `./scripts/study.sh digest F110_ret_fair_log sweep_s3`
- `anatomy_s3`  10-05 18:37  0 个变体  → `./scripts/study.sh digest F110_ret_fair_log anatomy_s3`
- `sweepfinal_s3`  10-05 18:39  8 个变体  → `./scripts/study.sh digest F110_ret_fair_log sweepfinal_s3`
- `sweep_s4`  10-06 10:22  234 个变体  → `./scripts/study.sh digest F110_ret_fair_log sweep_s4`
- `anatomy_s4`  10-06 11:22  0 个变体  → `./scripts/study.sh digest F110_ret_fair_log anatomy_s4`
- `sweepfinal_s4`  10-06 11:26  8 个变体  → `./scripts/study.sh digest F110_ret_fair_log sweepfinal_s4`
- `x1`(自写脚本的输出)  10-04 13:07  exit 97  → `logs/F110_ret_fair_log_x1.log`
- `x1c`(自写脚本的输出)  10-04 14:05  exit 0  → `logs/F110_ret_fair_log_x1c.log`
- `x1d`(自写脚本的输出)  10-04 14:09  exit 0  → `logs/F110_ret_fair_log_x1d.log`
- `x2`(自写脚本的输出)  10-04 15:07  exit 0  → `logs/F110_ret_fair_log_x2.log`

## 已写的 notes(`notes/F110_ret_fair_log/`)

`01_expression.md`(1K)、`02_operators.md`(4K)、`03_decomposition.md`(3K)、`04_grammar.md`(2K)、`05_hypotheses.md`(24K)、`06_baseline.md`(4K)、`07_S1_long.md`(8K)、`07x_01_x1_anatomy.md`(14K)、`07x_02_x2_GHI.md`(8K)、`08_variants.md`(5K)、`09_diagnosis.md`(12K)、`10_distilled.md`(19K)、`11_risks.md`(7K)、`12_next.md`(6K)、`journal.md`(41K)、`state.md`(7K)、`synthesis.md`(23K)

## 自写的探针与分析脚本(`studies/F110_ret_fair_log/`)

- `probes.py`  10-04 12:14  Probes this tree needs:  D * | M - Q |
- `x1_anatomy.py`  10-04 15:04  F110 X1: anatomy of  T = D * |M - Q|  and of the signal that is actually traded, -EMA20(T).

## 结构化结果(`handoff/F110_ret_fair_log/results/`)

- `synthesis.json`
- `verdict.json`
