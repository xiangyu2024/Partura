# verdict:F107_abs_demean_skew_low — agent ad87e3df3f1628871(工作流 wf_4811c95a-915)

- 状态:**还在跑**;开始 10-05 15:06,最后一次动作 10-05 15:16;工具调用 28 次
- 这是从 agent 的对话记录里**自动抽出来的动作流水**(命令、输出、写了哪些文件)。agent 的推理不在记录里 ——
  它的判断要看 `notes/F107_abs_demean_skew_low/journal.md` 和各 notes 文件。输出过长的地方截了中间。

## 动作流水

**10-05 15:06 · agent 的话**

I'll start by reading the required context.

**10-05 15:06 · Bash** — Read previous synthesis for F107

```bash
cd /Users/wxy/Desktop/Partura && cat notes/F107_abs_demean_skew_low/synthesis.md
```

```
# F107_abs_demean_skew_low —— 批量扫描 s1 的综合(主研,2026-10-05)

口径:只看多头腿扣 15bp 的净超额 Lnet(train / valid / utrain)与纯多头夏普 Lshp;噪声带 ±3pp / ±0.3 夏普;
门槛 cov ≥ 0.95、dist ≥ 0.5。基准 `k_known = cross_mean(day_std(Amt), 30)`:+12.6 / +22.3 / **+15.4%**,Lshp **+2.22**,LTO 3.4%。
记 `A = day_skew(Low)`、`B = cs_demean(A)`,原式信号 = `abs(B)`,方向 −1。

---

## 1. 它是什么(按代码逐层)

- `Low` = 分钟 K 线的最低价,**价格水平**(正、日内相对离散度只有 0.5%~5%),不是收益。
- `day_skew(Low)` = `C._skew` 沿分钟轴 → **当天 241 个分钟最低价这个分布的偏度**。
  **名实不符 ①**:名字像「下行尾部风险」,实际是**价格路径水平分布的不对称**,与尾部风险无关,也几乎与价位无关。
- `cs_demean(x) = x − cs_mean(x)`,`cs_mean` 是**全市场当日 nanmean 再广播**(`nd_cs.py:113`)→ 中心是全市场的,不分板块、不分市值。
- `abs_(x) = |x|`。所以信号 = **「这只票今天的日内路径形状,离今天全市场的平均形状有多远」**,是个两侧对称的**异常度**。
- 方向 −1 → 买 `abs(B)` 最小的 → **多头腿买「路径形状最平庸」的票**。
  **名实不符 ②**:名字里没有一个字说它是个**折叠出来的中心度因子**,而这就是它的全部内容。

折叠这件事被三条互相独立的代码事实钉死(都是**噪声标尺**,不是三个发现):
- `sqrt(x) = sqrt(abs(x))`(`common.py:198`)→ `sub_C_sqrt` 与原式**秩等价**:+1.5% 对 +1.7%,ρo 0.97。
- `pow_2` 同样单调于 `abs(B)` → `sub_C_pow_2` +2.3%,ρo 0.92。
- `cs_normalize` 是正仿射 → `sub_B_cs_normalize` 与原式**完全秩相等**:+2.0%,ρo **0.99**。
  → 四行落在 +1.5~+2.3% 的带子里,**±3pp 的噪声带在这条因子上是对的**。
- **名实不符 ③(算子陷阱)**:`pow_05(x) = sign(x)·abs(x)^0.5`(`e ≤ 1` 保号),**不是 sqrt**;所以 `sub_C_pow_05` 其实是 iso:
  −24.4%、ρo −0.04,和 `iso_B` −31.9% 同族。而 `log(x) = log(abs(x))`,`abs(x) ≤ EPS` 时 NaN —— 它单调于 `abs(B)`,
  但**恰好把最靠近中心的票 NaN 掉了,那正是多头书**:`sub_C_log` −0.1% 对 +1.7%,就是丢掉中心票的罚金。

## 2. 预测力在哪

**承重:折叠本身,和折叠绕的那个中心。**
… (142 行略) …

**best_own(不含已知族成分)**:① `h_gini_ema30 = cross_ema(abs_(cs_demean(day_gini(Low))), 30)` +11.7% / Lshp **2.87** / LTO 4.0% / ρk 0.35 —— 非家族里 utrain 夏普最高,但 **valid 两侧全败家族**(+7.8 对 +22.3、1.85 对 3.46),不是候选;
② `h_vol_std_ret = abs_(cs_demean(day_std(Ret)))` +9.5/+6.4/**+8.7%**、Lshp 2.31/1.65/**2.13**、LTO 5.2%、ρk **0.19** —— **全表唯一「成交额五档段内全正(+2.4/+2.3/+0.5/+7.4/+18.7)且倾斜 ≈ 0」的一条**,
低配最小市值档 −12.0pp 还赚钱,下跌市 +7.0 / 上涨 +10.3、高波动 +8.1 / 低波动 +9.2(全表最平)、六年无负年、冻结盘口段内 +7.9%。**本研究唯一不靠倾斜赚钱的版本。**
③ `h_vol_cv_low` +9.4% / 2.26 —— 机制确证用,被 ① ② 支配。
**best_on_known**:`h_cc_regres_gini_known` +15.8% / 2.53(ρk 0.71)—— 对 `k_known` 持平(+0.4pp / +0.31,都在噪声边上)、对 `k_known_xfrozen` **明确更差**(−2.7pp / −0.62)且贵一倍;
筛子方向无一过关(`scr_xhi_p` +12.7、`scr_xhi_m` +5.9),overlay 阶梯仍单调下坡。→ **建在已知族上没有任何用法强于基准。**

**one_line**:原式的多头腿收益是 `abs_(cs_demean(·))` 折出来的薄度倾斜(换中心 ρo 0.99、抹掉异方差后归零),相对已知族零增量;
s2 唯一的真东西是从它身上剥出来的 `abs_(cs_demean(day_std(Ret)))`(段内全正、倾斜 ≈ 0、ρk 0.19),但净超额仍低家族 6.7pp —— 那是另一条因子,不是 F107 的提纯。

**verdict**:**原式 = 已知族的更弱更贵版本,多头腿不可用**(第三条独立路径复现,且这次说清了钱从哪来)。**不是提纯**(换中心 / 换折叠 / 桶内化 / 中性化 —— 要么零变化要么翻负);
**也当不了筛子**(给已知族当筛子 +12.7 < +15.4)。gini / 波动分支是**另一条因子穿着同一件外套**,机制坐实为「日内相对波动的截面中位度」,但相对已知族同样零增量(res_known valid −1.3)。
→ F107 本体结案(维持 `recommended_id = f_m20`、`known_family`);`abs_(cs_demean(day_std(Ret)))` 连同第三批 A / B / F 三组**另立一个研究**,不要再挂在 F107 名下。

### 4. 第三批假设(24 条,`studies/F107_abs_demean_skew_low/hypo3.yaml`,24/24 parse)

A 同方差桶内折叠(5:`cs_bucket_zscore` / `cs_bucket_demean` / `cross_age` —— 第一次能问「同类股票内部的距离还有没有信息」,这是结案的最后一问)·
B 赢家 `day_std(Ret)` 周围换一圈(6:`day_wstd` / `day_topw_mean` / `cs_robust_z` / `cross_madz` / `day_es_ratio_lo` / ema30)· C 封板两侧与更准的冻结筛子(4:`day_at_max_ratio` / `day_at_min_ratio` / `cross_flat_ratio`,**全部包 neg 保证 sg = +1**)·
D 市场状态(3:`cs_state_rank` / `cs_flip_by_state` / `select_where`)· E 价位格子(2:`day_distinct_ratio`)· F 赢家的增量三件套 + 方向写对的筛子(4,含叠在 `k_known_xfrozen` 上的双筛子 = 门槛最高的一问)。
```

**10-05 15:06 · Bash** — Read new operator batch 4 definitions

```bash
cd /Users/wxy/Desktop/Partura && sed -n '/第四批/,$p' docs/new_operators.md
```

```
**第四批(十条因子的综合里被反复要求的;共 23 个)**

| 算子 | 定义 | 谁要的、为什么 |
|---|---|---|
| `cs_bucket_demean(y, x)` | y 减去「x 的同一个十分位」内 y 的均值(保留量纲) | F101 / F107 / F110:折叠的中心应该是「同类股票的典型值」而不是全市场均值 —— 后者把书推进大票 |
| `cs_bucket_zscore(y, x)` | 同上再除以桶内标准差 | F101 / F106:各桶离散度相差数倍,去均值后的距离仍不可比 |
| `cs_robust_z(x)` | 截面 `(x − 中位数) / (1.4826·MAD)` | F113:重尾量的截面标准化 |
| `cs_first_low20 / cs_first_high20 / cs_last_high40 / cs_last_low40` | 与 `cs_first_low40` 等同语义,补齐 20% / 40% 两档 | F112 |
| `cs_state_rank(x, d)` | 当日 x 的截面均值在它自己近 d 日里的分位,**全市场同一个数** | F107 / F112 / F115:「只在某种市场状态下有效」以前写不进表达式;它可以当两条信号之间的权重,或 `select_where` 的条件 |
| `cs_flip_by_state(y, g)` | 市场级状态(g 的截面均值相对近 241 日中位数)高时取 +rank(y),低时取 −rank(y) | F104:最小的「按市场状态切日子」原语 |
| `day_at_max_ratio(x)` / `day_at_min_ratio(x)` | 当天取值等于当日最大(最小)值的分钟占比 | F106 / F110:封在涨停和封在跌停是两种事件,`day_flat_ratio` 分不开 |
| `day_distinct_ratio(x)` | 当天不同取值的个数 ÷ 有限分钟数 | F107:当天走过多少个价位(低价票在一个 tick 的格子上很粗) |
| `day_wstd(x, w)` | `|w|` 加权的总体标准差 | F101:资金经历的波动,不被没有成交的分钟稀释 |
| `day_topw_mean(y, w)` | `|w|` 最大的 10% 分钟上 y 的均值 | F115:一个节点完成「放量分钟的平均收益」,不用触发掩码 |
| `day_es_ratio_hi(x)` / `day_es_ratio_lo(x)` | 高于 95%(低于 5%)分位的分钟均值 ÷ 该分位;分位数接近 0 时 **NaN** | F106 / F109:手写的 `erm_*` 因子在分母上加 1e-6,把每个封板日变成 1e4 量级的值,因子读到的是「有没有封板」而不是尾部形状;这是同一个量、把那样的日子留作缺失 |
| `in_index(x)` | 分钟在一天里的位置 `t/(T−1)` | F115:按时间加权或比较 |
| `in_zscore_expand(x)` | 日内扩张窗口 z 分数(到当前分钟为止) | F110:「相对今天到目前为止是否异常」,日内因果 |
| `cross_madz(x, d)` | `cross_zscore` 的稳健版(中位数 / MAD,相对 EPS) | F104:分清「标准化这个想法不对」和「估计量太脆」 |
| `cross_flat_ratio(x, d)` | 近 d 日里与前一日取值完全相同的日子占比 | F111 |
| `cross_semistd_neg(x, d)` / `…_pos` | 正值序列日度对数变化的下行(上行)半标准差 | F112 |
| `cross_age(x)` | x 第一次有值以来的交易日数;数据起点就有值的股票从 10000 起算 | F105:不饱和的上市时间 |

已经有、不用新加的(告诉主研):三目选择用现成的 `select_where(c, a, b)`;近 d 日为正的占比 = `cross_mean(is_gt0(x), d)`;
「离截面中心多近」= `abs_(cs_demean(cs_rank(x)))` 的单调变换。

**主研们反复要、但属于数据层的**(6 条因子都提了,需要用户决定是否在 AlphaCube 的立方体里加字段):
- **流通市值 / 流通股本**(F105、F108、F110、F115…):有了它才能写真正的换手率 `day_sum(Amt) / FloatCap`、做规模中性;
  现在只能用价格或成交额水平做代理,而这两个代理在好几棵树上符号相反。
- **板块 / 涨跌幅限制宽度**(F104、F111、F112):科创板 ±20%、无「一字板」状态,多条因子在那里整体失效或被错判。

没有加的:`cs_bucket_rank2(y, x1, x2)`(二维 5×5 格子内排名)—— 算子语法目前只支持 1~2 个张量操作数;
「流通市值」字段 —— 立方体里没有,需要在数据层加(Partura 只把它当外部控制变量用)。这两条留给用户决定。

实现上的一个坑:引擎里 `cross_*` 内核如果写成逐日的 Python 循环会慢 60 倍以上;`cross_ema` 用分块的精确递推
(块内累加、块间进位)解决,和逐日递推的最大误差 1e-6。

加新算子的步骤:在 `ops_ext.py` 里写函数(docstring 写清定义)→ 加进 `NEW_OPERATORS` → 用已知答案核对 →
`rsync` 到服务器 → 在本表登记定义和理由。
```

**10-05 15:06 · Bash** — List run/study/note files for F107

```bash
cd /Users/wxy/Desktop/Partura && ls -la runs/F107_abs_demean_skew_low/ 2>/dev/null; echo "---STUDIES---"; ls -la studies/F107_abs_demean_skew_low/ 2>/dev/null; echo "---NOTES---"; ls -la notes/F107_abs_demean_skew_low/ 2>/dev/null
```

```
total 2384
drwxr-xr-x@ 11 wxy  staff     352 Oct  5 12:13 .
drwxr-xr-x@ 19 wxy  staff     608 Oct  3 17:37 ..
-rw-r--r--@  1 wxy  staff  129955 Oct  4 15:05 FINAL.json
-rw-r--r--@  1 wxy  staff   41960 Oct  4 11:50 S0_baseline.json
-rw-r--r--@  1 wxy  staff  259949 Oct  4 13:59 S12.json
-rw-r--r--@  1 wxy  staff   67869 Oct  5 10:57 anatomy_s1.json
-rw-r--r--@  1 wxy  staff   67743 Oct  5 12:09 anatomy_s2.json
-rw-r--r--@  1 wxy  staff    4270 Oct  5 12:12 ledger.json
-rw-r--r--@  1 wxy  staff  214578 Oct  5 10:50 sweep_s1.json
-rw-r--r--@  1 wxy  staff  367564 Oct  5 11:58 sweep_s2.json
-rw-r--r--@  1 wxy  staff   48832 Oct  5 12:13 sweepfinal_s2.json
---STUDIES---
total 200
drwxr-xr-x@  7 wxy  staff    224 Oct  5 13:46 .
drwxr-xr-x@ 18 wxy  staff    576 Oct  5 10:31 ..
-rw-r--r--@  1 wxy  staff  15052 Oct  5 11:13 hypo.yaml
-rw-r--r--@  1 wxy  staff  16009 Oct  5 13:46 hypo3.yaml
-rw-r--r--@  1 wxy  staff   8496 Oct  3 17:50 probes.py
-rw-r--r--@  1 wxy  staff  36610 Oct  4 12:16 x1_anatomy.py
-rw-r--r--@  1 wxy  staff  16753 Oct  4 12:44 x2_elevate.py
---NOTES---
total 528
drwxr-xr-x@ 27 wxy  staff    864 Oct  5 13:52 .
drwxr-xr-x@ 19 wxy  staff    608 Oct  4 13:07 ..
-rw-r--r--@  1 wxy  staff   1831 Oct  4 23:42 01_expression.md
-rw-r--r--@  1 wxy  staff   3070 Oct  4 12:55 02_operators.md
-rw-r--r--@  1 wxy  staff   2863 Oct  4 12:55 03_decomposition.md
-rw-r--r--@  1 wxy  staff   2218 Oct  4 12:28 04_grammar.md
-rw-r--r--@  1 wxy  staff  20437 Oct  4 23:42 05_hypotheses.md
-rw-r--r--@  1 wxy  staff   3894 Oct  4 13:05 06_baseline.md
-rw-r--r--@  1 wxy  staff   1262 Oct  4 23:42 07_S0_baseline.md
-rw-r--r--@  1 wxy  staff  12378 Oct  4 14:28 07_S1_parts.md
-rw-r--r--@  1 wxy  staff  12730 Oct  4 14:29 07_S2_memory.md
-rw-r--r--@  1 wxy  staff  10494 Oct  4 15:39 07_S_final.md
-rw-r--r--@  1 wxy  staff   1416 Oct  4 23:42 07_conditional.md
-rw-r--r--@  1 wxy  staff   3009 Oct  5 00:04 07_controls.md
-rw-r--r--@  1 wxy  staff   1633 Oct  4 23:42 07_neutralise.md
-rw-r--r--@  1 wxy  staff  10794 Oct  4 13:06 07x_1_anatomy.md
-rw-r--r--@  1 wxy  staff  23491 Oct  4 14:30 07x_2_elevate.md
-rw-r--r--@  1 wxy  staff   6199 Oct  4 15:37 08_variants.md
-rw-r--r--@  1 wxy  staff  11660 Oct  5 00:03 09_diagnosis.md
-rw-r--r--@  1 wxy  staff  17817 Oct  4 15:38 10_distilled.md
-rw-r--r--@  1 wxy  staff   6821 Oct  5 00:03 11_risks.md
-rw-r--r--@  1 wxy  staff   4888 Oct  4 15:36 12_next.md
-rw-r--r--@  1 wxy  staff  33083 Oct  5 11:15 journal.md
drwxr-xr-x@  5 wxy  staff    160 Oct  4 23:09 orders
drwxr-xr-x@  5 wxy  staff    160 Oct  4 23:49 results
-rw-r--r--@  1 wxy  staff  11454 Oct  5 13:52 state.md
-rw-r--r--@  1 wxy  staff  21436 Oct  5 13:50 synthesis.md
```

**10-05 15:06 · Bash** — Read handoff status

```bash
cd /Users/wxy/Desktop/Partura && cat handoff/STATUS.md 2>/dev/null | head -60
```

```
# 批次状态板

_自动生成于 2026-10-05 15:04(后台记录器 `scripts/recorder.py`,不依赖任何模型)。_

| 因子 | 来源 | 阶段 | 留出段 | 已有结果 | 运行数 | 现状说明 state.md | 日志条数(研究员写的) | 当前 agent | 最后动静 |
|---|---|---|---|---|---|---|---|---|---|
| [F101_day_shine_retstd](F101_day_shine_retstd/STATE.md) | 手写 day_shine_retstd | **完成** | 已读 | audit-mechanism、audit-numbers、revised、study、synthesis | 10 | 10-05 13:51 | 2(2) | verdict(中断) | 10-05 13:53 |
| [F102_kurt_autocorr](F102_kurt_autocorr/STATE.md) | 挖掘 #3961 | **完成** | 已读 | audit-mechanism、audit-numbers、revised、study、synthesis | 10 | 10-05 13:52 | 2(2) | verdict(中断) | 10-05 13:53 |
| [F103_amt_dw_decay](F103_amt_dw_decay/STATE.md) | 挖掘 #820 | **完成** | 已读 | audit-mechanism、audit-numbers、revised、study、synthesis、verdict | 9 | 10-05 13:47 | 2(2) | verdict(已返回) | 10-05 13:52 |
| [F104_kurt_masktop_amt](F104_kurt_masktop_amt/STATE.md) | 挖掘 #4190 | **完成** | 已读 | audit-mechanism、audit-numbers、revised、study、synthesis | 11 | 10-05 13:49 | 6(5) | verdict(中断) | 10-05 13:53 |
| [F105_std_fangzheng_covamt](F105_std_fangzheng_covamt/STATE.md) | 挖掘 #25 | **完成** | 已读 | audit-mechanism、audit-numbers、revised、study、synthesis | 11 | 10-05 13:50 | 2(2) | verdict(中断) | 10-05 13:53 |
| [F106_erm_mag_gap_1m](F106_erm_mag_gap_1m/STATE.md) | 手写 erm_mag_gap_1m | 研究中 | 已读 | synthesis | 7 | 10-05 11:15 | 14(9) | verdict(中断) | 10-05 13:53 |
| [F107_abs_demean_skew_low](F107_abs_demean_skew_low/STATE.md) | 挖掘 #613 | 待审查 | 已读 | study、synthesis | 8 | 10-05 13:52 | 17(10) | verdict(中断) | 10-05 13:53 |
| [F108_max_ntkurt_close](F108_max_ntkurt_close/STATE.md) | 挖掘 #3264 | 研究中 | 已读 | synthesis | 8 | 10-05 13:52 | 22(12) | verdict(中断) | 10-05 13:53 |
| [F109_erm_mag_gap_5m_tsm20](F109_erm_mag_gap_5m_tsm20/STATE.md) | 手写 erm_mag_gap_5m_tsm20 | **完成** | 已读 | audit-numbers、study、synthesis | 8 | 10-05 11:30 | 20(12) | synth(已返回) | 10-05 11:32 |
| [F110_ret_fair_log](F110_ret_fair_log/STATE.md) | 手写 ret_fair_log | 研究中 | 已读 | synthesis | 8 | 10-05 11:18 | 23(12) | synth(已返回) | 10-05 11:21 |
| [F111_spearman_qclose](F111_spearman_qclose/STATE.md) | 挖掘 #953 | 研究中 | 已读 | synthesis | 8 | 10-05 11:18 | 20(10) | synth(已返回) | 10-05 11:20 |
| [F112_scale_spow_masktop](F112_scale_spow_masktop/STATE.md) | 挖掘 #574 | 研究中 | 已读 | synthesis | 9 | 10-05 11:08 | 23(12) | synth(已返回) | 10-05 11:12 |
| [F113_nested_tsmax_demean](F113_nested_tsmax_demean/STATE.md) | 挖掘 #1375 | 研究中 | 已读 | synthesis | 9 | 10-05 11:10 | 23(12) | synth(已返回) | 10-05 11:15 |
| [F114_q25_closeret](F114_q25_closeret/STATE.md) | 挖掘 #1421 | 研究中 | 已读 | synthesis | 11 | 10-05 10:44 | 23(14) | synth(已返回) | 10-05 10:47 |
| [F115_all_tide_mean_30](F115_all_tide_mean_30/STATE.md) | 手写 all_tide_mean_30 | 研究中 | 已读 | synthesis | 9 | 10-05 11:11 | 18(8) | synth(已返回) | 10-05 11:14 |

## 还剩什么

- 研究没做完(8):F106、F108、F110、F111、F112、F113、F114、F115
- 待审查(1):F107
- 待修订(0):无

怎样接着跑(换了模型、换了会话都一样):看 `handoff/README.md`。
```

**10-05 15:06 · agent 的话**

Round 2 appears to have been written already (13:46–13:52). Let me verify against the actual s2 table before deciding what still needs doing.

**10-05 15:07 · Bash** — Dump s2 full table to scratch

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh table F107_abs_demean_skew_low s2 --all > /private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/s2_table.txt 2>&1; wc -l /private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/s2_table.txt
```

```
     188 /private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/s2_table.txt
```

**10-05 15:07 · Bash** — Read current state.md

```bash
cd /Users/wxy/Desktop/Partura && cat notes/F107_abs_demean_skew_low/state.md
```

```
# F107_abs_demean_skew_low — 研究现状

> 主研**第 7 轮(批量扫描 s2 对账轮)**写(Opus 5,2026-10-05),整页覆盖重写。
> `abs_(cs_demean(day_skew(Low)))`,挖掘 #613。记 `A = day_skew(Low)`、`B = cs_demean(A)`,信号 `abs(B)`,方向 **−1**。
> **留出段已读(tag `FINAL`,1 次),额度用完,不许再读**;本轮也没打开 `runs/*/sweepfinal_*.json`。
> 本轮只读 `study.sh table F107_abs_demean_skew_low s2 --all`(124 变体 + 市场解剖)+ 读算子源码,**没起服务器、没跑计算**。

## 1. 现状

**结案。** 对纯多头用户,F107 原式相对已知成交额族 `k_known` **零增量,多头腿不可用** —— 这是第 **3** 条独立路径得到同一结论
(留出段判据 −6.12pp → s1 的成交额段内分解 → s2 的「折叠 = 异方差」机制)。推荐仍是 `recommended_id = f_m20`、`recommended_kind = known_family`,**不改判**。

**本轮的实质进展是机制说清了,而且剥出了一条别的因子。**
(a) `abs_(cs_demean(x))` 这个结构量的是 **x 的截面异方差**,不是「离中心的距离」(三条独立证据,§2),原式的 +1.7% 因此必然是薄度倾斜;
(b) s1 留下的 gini 线索被确证为「无尺度的日内相对波动」,且找到更干净的写法 `abs_(cs_demean(day_std(Ret)))`
(**全表唯一段内全正、流动性倾斜 ≈ 0 的一条**),但它相对已知族同样零增量,**应另立研究,不算 F107 的提纯**。

本轮产出:`synthesis.md` 追加「## 第二轮(s2)对账与结论」(76 行)、`studies/<fid>/hypo3.yaml`(**24 条,24/24 parse**)、journal 新一条。

## 2. 中间结果(事实 + 数字 + 出处)

出处一律是 `s2` 大表(124 行)。Lnet = 多头腿扣 15bp 净超额(train / valid / **utrain**),Lshp = 纯多头夏普。
基准:`k_known` +12.6/+22.3/**+15.4%**、Lshp 1.78/3.46/**2.22**、LTO 3.4%;`k_known_xfrozen` **+16.4/+23.2/+18.5%**、Lshp 2.81/3.98/**3.15**(**全表最强行**)。

**机制(本轮核心,三条独立证据):**
① 换中心无效:`h_cc_regres_known` ρo **0.99**(+2.0%)、`h_cc_regres_price` ρo 0.99(+2.2%)、`h_fold_median` ρo **1.00**(+1.1%)、`h_fold_winsor_first` ρo 0.96(+1.4%)。
② 折叠**之后**中性化翻负:`bk_known` −3.3 / `res_known` −3.4 / `bk_liq` −2.5 / `res_liq` −2.7%。
③ 把异方差抹掉**再**折叠就归零:`h_fold_rankfirst` −0.2%、`h_cc_bucket_pre` −3.1%(与 ② 同值)。
→ **原式 = 折叠生出来的薄度倾斜**(最低成交额档超配 +16.5pp、该档段等权超额 +15.1%,而该档段内 −8.1%)。
反证:`day_std(Ret)` 的截面离散度不随流动性变,折叠它**不生倾斜**(五档持仓偏离 +2.2/+2.4/−0.3/−2.3/−2.0pp,段内 +2.4/+2.3/+0.5/+7.4/+18.7 全正)。
… (53 行略) …

**已读,一次(tag `FINAL`,10-04 15:05,exit 0,5 变体)。不许再读、不许再下 final 工单、不许打开 `runs/F107_*/sweepfinal_*.json`。**
事前判据在 `10_distilled.md`「读留出段之前」(一字未改),判决在同文件「读完之后」。服务器运行合计 **5/8**,本轮加 **0** 次。
第二、三批的裁决只能在 train / valid / utrain 上做;真出现值得上留出段的东西,**必须先和总领确认是否另立研究**。

## 8. 给接手者的提醒

- **先读 `notes/<fid>/synthesis.md`**(192 行:前 117 行 = s1 综合,后 76 行 = s2 对账与定论);这页只是索引。
- **筛子算子的方向与 sg 耦合(本轮新坑,会让一整组假设反掉)**:`cs_last_high20/low20/high40/low40`、`cs_first_*` 都是 `_lexi(y,x,lo,hi,shift)`
  = 给被标出那段的 `rank(y)` 加减 1。**只有 sg = +1 时 `cs_last_*` 才是排除筛子;sg = −1 时多头书恰好变成只买那一段。**
  写法:照通用行把 y 包成「高的好」(`cs_last_high20(neg(k_known), x)`),或解释结果前先核对表里的 sg 列。
- **算子按代码不按名字**(已累计四处):`pow_05(x) = sign(x)·|x|^0.5` 保号(其实是 iso);`log(x) = log(|x|)` 且 `|x| ≤ EPS` 时 NaN(恰好把多头书 NaN 掉);
  `sqrt(x) = sqrt(|x|)`、`cs_normalize` 正仿射(都与原式秩等价);**`day_gini` 在正的紧的价格水平上 ≈ σ/μ(相对波动),只有喂 Ret / Amt 才是集中度**。
  旧坑仍成立:`day_skew` 分母是路径自身标准差;`cross_delay` 与 `ts_delay`(d>0)逐行等价不是 bug;引擎 `cross_mean` ≠ 缓存面板滚动 nanmean(引 x1 数字要标「numpy 探路」)。
- **「段内」和「全市场」是两回事**:原式全市场 +1.7%,但成交额每一档的段内都是负的。说「有微弱 alpha」之前先看段内那一行。
  同理 **段内高 ≠ 该倾向那一段**:`h_scr_newlist_gini` 反例(gini 次新段内 +14.8%,倾向次新后 valid 翻负 —— 次新段等权超额 −28.7%)。
- 带 `[boolean_output]` 的算子出来的变体 dist = 0.00 会被门槛杀掉;`day_zero_ratio` / `day_flat_ratio` / `day_flat_run_max` 带 `[trivial_boolean]`,hypo 里先用 `cross_mean(·, d)` 包一层。
  **dist 门槛真会杀掉好行**:`h_path_pos`(+6.1 / Lshp 1.63)dist 0.03 ✗、`h_thin_flatrun`(+8.1)dist 0.17 ✗ —— 写假设时先想它会不会撞上库里已有的东西。
- **判断类 notes 已定稿,不要改**:`08` / `09` / `10` / `11` / `12`。本轮一个字都没动;发现问题写进结果卡。
- 半衰期口径有坑(`f_m20` 在 train 口径选 hl20、utrain 口径选 hl10);ρ 符号约定有坑(`f_K +0.28` 与 `known_stdamt_mean30 −0.28` 是同一式,差在方向有没有乘进交易信号)。
```

**10-05 15:07 · Bash** — View first part of s2 table

```bash
cd /private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad && sed -n '1,95p' s2_table.txt
```

```
== F107_abs_demean_skew_low  批量扫描 s2:124 个变体(只用 train 2018–2021 / valid 2022–202308;方向 sg 与半衰期 hlL 在 train 上定,半衰期按纯多头书选)==
Lnet = 多头腿净超额(扣 15bp,年化),Lshp = 纯多头夏普:train | valid | utrain(用户训练段);LTO = 多头日换手;LS = 多空夏普;
空头腿 = 等权 − 最低十分位(毛,年化):大 = 钱在空头腿(纯多头用不上);为负 = 最低十分位反而跑赢,值得把方向反过来看。
ρo / ρk = 交易信号与原式 / 已知成交额族的 rank 相关;✗ = 没过门槛(cov ≥ 0.95、dist ≥ 0.5),不能当候选。
id                     kind     sg hlL | Lnet tr     va     ut   | Lshp tr    va    ut  | LTO   | LS tr   va  | 空头腿 tr   va   |  ρo    ρk  | cov  dist   | expr
v_base                 base     -1  20 |  +1.1%  +3.0%  +1.7% | +0.24 +0.69 +0.36 | 10.9% | +2.81 +3.16 | +32.5% +30.3% | +1.00 +0.28 | 1.00 1.00   | abs_(cs_demean(day_skew(Low)))
k_known                bench    -1   0 | +12.6% +22.3% +15.4% | +1.78 +3.46 +2.22 |  3.4% | +1.87 +3.70 | +21.1% +33.8% | +0.28 +1.00 | 1.00 1.00   | cross_mean(day_std(Amt), 30)
---------------------------------------- 全部变体,按 utrain 纯多头夏普排序
k_known_xfrozen        bench    +1   3 | +16.4% +23.2% +18.5% | +2.81 +3.98 +3.15 |  3.4% | +4.27 +4.99 | +25.4% +22.4% | +0.25 +0.56 | 1.00 1.00   | cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Ret), 15))
h_gini_ema30           hypo     -1   2 | +13.2%  +7.8% +11.7% | +3.29 +1.85 +2.87 |  4.0% | +2.98 +2.75 | +28.9% +31.3% | +0.29 +0.35 | 1.00 1.00   | cross_ema(abs_(cs_demean(day_gini(Low))), 30)
h_gini_ema10           hypo     -1  10 | +12.6%  +7.8% +11.2% | +3.08 +1.81 +2.71 |  3.7% | +2.90 +2.68 | +26.5% +29.7% | +0.27 +0.34 | 1.00 1.00   | cross_ema(abs_(cs_demean(day_gini(Low))), 10)
h_cc_regres_gini_known hypo     -1  20 | +13.4% +21.7% +15.8% | +2.13 +3.56 +2.53 |  6.0% | +2.90 +3.46 | +30.8% +32.9% | +0.35 +0.71 | 1.00 1.00   | abs_(cs_regres(day_gini(Low), cs_rank(cross_mean(day_std(Amt), 30))))
h_scr_liquid_gini      hypo     -1  20 | +12.4% +12.5% +12.5% | +2.50 +2.37 +2.46 |  8.2% | +1.89 +2.39 | +15.2% +20.3% | +0.16 +0.78 | 1.00 1.00   | cs_first_high40(abs_(cs_demean(day_gini(Low))), cross_mean(day_sum(Amt), 30))
h_ov_gini_p05          hypo     -1  10 | +12.9% +20.1% +15.0% | +2.01 +3.12 +2.33 |  4.2% | +1.71 +3.17 | +17.7% +30.2% | +0.24 +0.95 | 1.00 0.86   | add(cs_rank(cross_mean(day_std(Amt), 30)), mul(cs_rank(abs_(cs_demean(day_gini(Low)))), 0.5))
h_vol_cv_low           hypo     -1  20 | +11.0%  +5.4%  +9.4% | +2.65 +1.28 +2.26 |  9.7% | +3.03 +2.82 | +34.5% +38.0% | +0.28 +0.32 | 1.00 1.00   | abs_(cs_demean(div(day_std(Low), day_mean(Low))))
k_known                bench    -1   0 | +12.6% +22.3% +15.4% | +1.78 +3.46 +2.22 |  3.4% | +1.87 +3.70 | +21.1% +33.8% | +0.28 +1.00 | 1.00 1.00   | cross_mean(day_std(Amt), 30)
h_vol_std_ret          hypo     -1  20 |  +9.5%  +6.4%  +8.7% | +2.31 +1.65 +2.13 |  5.2% | +3.63 +3.32 | +34.3% +35.2% | +0.29 +0.19 | 1.00 1.00   | abs_(cs_demean(day_std(Ret)))
h_gini_close           hypo     -1  20 | +10.3%  +4.6%  +8.7% | +2.49 +1.11 +2.10 |  9.7% | +2.90 +2.68 | +33.9% +37.5% | +0.27 +0.31 | 1.00 0.96   | abs_(cs_demean(day_gini(Close)))
sub_A_day_gini         substitu -1  20 | +10.0%  +5.4%  +8.7% | +2.39 +1.26 +2.07 |  9.7% | +2.83 +2.74 | +33.1% +37.2% | +0.27 +0.33 | 1.00 0.96   | abs_(cs_demean(day_gini(Low)))
ov_p025                overlay  -1  10 | +10.7% +21.0% +13.6% | +1.54 +3.14 +1.98 |  2.9% | +1.42 +3.11 | +13.5% +27.4% | +0.28 +0.96 | 1.00 1.00   | a
… (4608 字符略) …
54 +1.64 | +28.4% +25.2% | +0.31 +0.27 | 1.00 1.00   | abs_(cs_demean(day_gini(in_pct(Close, 5))))
h_scr_price_mem        hypo     -1  20 |  +0.5%  -6.6%  -1.5% | +0.07 -1.15 -0.25 |  0.9% | +2.34 +1.11 | +11.6% +11.7% | +0.52 -0.13 | 1.00 1.00   | cs_last_high20(cross_ema(abs_(cs_demean(day_skew(Low))), 30), day_mean(Close))
h_path_centroid        hypo     -1  20 |  -1.6%  -0.3%  -1.2% | -0.33 -0.08 -0.26 | 10.9% | +3.05 +2.17 | +36.7% +29.3% | +0.42 -0.04 | 1.00 1.00   | abs_(cs_demean(day_centroid(Amt)))
fold_sq                shape    -1  20 |  -1.5%  -1.3%  -1.4% | -0.38 -0.43 -0.38 |  9.6% | +2.55 +2.46 | +27.5% +22.8% | +0.74 +0.16 | 1.00 1.00   | pow_2(cs_demean(abs_(cs_demean(day_skew(Low)))))
sub_C_inv              substitu -1  20 |  -1.2%  +0.1%  -0.8% | -0.60 +0.07 -0.41 |  4.4% | -1.99 -2.92 |  -1.2%  -4.2% | +0.00 +0.01 | 1.00 1.00   | inv(cs_demean(day_skew(Low)))
h_gini_iso_demean      hypo     -1  20 |  -8.5%  +5.9%  -4.4% | -0.82 +0.62 -0.43 |  3.6% | +0.31 +1.35 | +18.8% +27.4% | +0.31 +0.53 | 1.00 0.96   | cs_demean(day_gini(Low))
h_gini_iso             hypo     -1  20 |  -9.2%  +5.8%  -4.9% | -0.88 +0.61 -0.48 |  3.6% | +0.27 +1.34 | +18.6% +27.3% | +0.31 +0.53 | 1.00 0.96   | day_gini(Low)
mem_stddev10           memory   -1  10 |  -2.9%  +0.2%  -1.9% | -0.67 +0.07 -0.48 |  6.7% | +2.22 +1.60 | +21.6% +19.7% | +0.76 +0.20 | 1.00 1.00   | cross_stddev(abs_(cs_demean(day_skew(Low))), 10)
seg_xfrozen_m          segment  +1  20 |  -1.2%  -3.4%  -1.8% | -0.32 -0.89 -0.48 | 11.8% | +0.80 -0.36 | +10.4%  +2.3% | +0.46 -0.06 | 1.00 1.00   | cs_last_high20(neg(abs_(cs_demean(day_skew(Low)))), cross_max(day_zero_ratio(Ret), 15))
```

**10-05 15:07 · Bash** — View rest of s2 table incl anatomy

```bash
cd /private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad && sed -n '95,188p' s2_table.txt
```

```
abl_W                  ablate   -1  20 |  -4.3%  -4.1%  -4.2% | -0.66 -0.61 -0.64 |  5.2% | +2.10 +1.78 | +32.1% +26.1% | +0.63 -0.08 | 1.00 0.99   | sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Ret, 0))), add(day_sum(is_gt(Ret, day_quantile(Ret, 0.95))), cr
sub_W_sub              substitu -1  20 |  -4.3%  -4.2%  -4.2% | -0.66 -0.63 -0.64 |  5.3% | +2.10 +1.77 | +32.1% +26.1% | +0.63 -0.08 | 1.00 1.00   | sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Ret, 0))), add(day_sum(is_gt(Ret, day_quantile(Ret, 0.95))), cr
rank_V                 interact -1  20 |  -4.3%  -4.4%  -4.3% | -0.65 -0.66 -0.65 |  5.3% | +2.10 +1.75 | +32.1% +26.1% | +0.63 -0.08 | 1.00 0.99   | sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Ret, 0))), add(day_sum(is_gt(Ret, day_quantile(Ret, 0.95))), cr
sub_W_add              substitu -1  20 |  -4.4%  -4.2%  -4.4% | -0.68 -0.63 -0.66 |  5.2% | +2.10 +1.76 | +32.1% +26.1% | +0.63 -0.08 | 1.00 1.00   | sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Ret, 0))), add(day_sum(is_gt(Ret, day_quantile(Ret, 0.95))), cr
sub_H_mul              substitu -1  20 |  -3.7%  -7.2%  -4.7% | -0.53 -1.06 -0.67 |  8.1% | +1.83 +1.26 | +29.8% +24.2% | +0.63 -0.08 | 0.99 1.00   | sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Ret, 0))), mul(day_sum(is_gt(Ret, day_quantile(Ret, 0.95))), cr
h_q90                  hypo     -1  20 |  -1.0%  -4.8%  -2.0% | -0.32 -1.81 -0.70 |  2.2% | +3.37 +2.61 | +30.4% +25.2% | +0.56 +0.01 | 1.00 1.00   | sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.90)), Ret, create_like(Ret, 0))), add(day_sum(is_gt(Ret, day_quantile(Ret, 0.90))), cr
sub_U_pow_2            substitu -1  20 |  -7.9%  +2.5%  -4.9% | -1.07 +0.39 -0.70 |  5.5% | +1.53 +2.55 | +29.4% +24.9% | +0.34 +0.34 | 1.00 0.99   | sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Ret, 0))), add(day_sum(is_gt(Ret, day_quantile(Ret, 0.95))), cr
h_es_vol               hypo     -1  20 |  -7.0%  +0.8%  -4.8% | -1.01 +0.13 -0.71 | 10.8% | +1.55 +2.63 | +34.9% +37.9% | +0.43 +0.32 | 1.00 0.99   | div(sub(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Ret, 0))), add(day_sum(is_gt(Ret, day_quantile(Ret, 0.95))), cr
h_eps2                 hypo     -1  20 |  -7.1%  -0.5%  -5.2% | -0.98 -0.09 -0.76 | 10.5% | +1.86 +2.40 | +38.7% +35.4% | +0.52 +0.29 | 1.00 0.99   | sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Ret, 0))), add(day_sum(is_gt(Ret, day_quantile(Ret, 0.95))), cr
sub_S_mul              substitu +1  20 |  -3.5%  -6.0%  -4.2% | -0.65 -1.09 -0.77 |  8.7% | +1.68 +1.20 | +25.6% +20.7% | +0.22 -0.08 | 0.99 1.00   | sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Ret, 0))), add(day_sum(is_gt(Ret, day_quantile(Ret, 0.95))), cr
fold_rank              shape    -1  20 |  -3.5% -11.9%  -5.8% | -0.47 -1.53 -0.78 | 10.1% | -0.03 -1.40 | +11.9%  +2.9% | +0.18 -0.19 | 1.00 0.85   | abs_(cs_demean(cs_rank(sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Ret, 0))), add(day_sum(is_gt(Ret, day_qu
sub_S_div             
… (9317 字符略) …
00 0.99   | sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Ret, 0))), add(day_sum(is_gt(Ret, day_quantile(Ret, 0.95))), cr
seg_new_m              segment  -1  20 | -12.5% -12.8% -12.5% | -2.84 -2.89 -2.85 | 12.4% | -2.08 -2.66 |  +4.2%  +1.5% | -0.14 +0.04 | 1.00 1.00   | cs_first_low40(neg(sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Ret, 0))), add(day_sum(is_gt(Ret, day_quanti
h_regular_gate         hypo     -1  20 | -12.4% -10.2% -11.8% | -3.15 -3.00 -3.10 | 11.0% | -1.52 -2.17 | +11.0%  +4.8% | +0.43 -0.01 | 1.00 0.99   | mul(sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Ret, 0))), add(day_sum(is_gt(Ret, day_quantile(Ret, 0.95)))
abl_T                  ablate   +1  20 | -18.7%  -8.1% -15.7% | -3.52 -1.88 -3.10 |  1.5% | -0.37 +1.19 | +17.3% +14.5% | -0.28 -0.01 | 1.00 0.99   | sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Ret, 0))), add(day_sum(is_gt(Ret, day_quantile(Ret, 0.95))), cr
h_logcomp              hypo     -1  20 | -12.0% -12.0% -12.0% | -3.01 -3.39 -3.10 | 11.5% | +1.75 +0.90 | +31.7% +23.7% | +0.75 +0.05 | 1.00 0.99   | mul(sign(sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Ret, 0))), add(day_sum(is_gt(Ret, day_quantile(Ret, 0.
nosc_Q_day_skew        substitu +1  10 | -21.3% -18.5% -20.2% | -3.27 -3.29 -3.20 |  3.6% | -2.74 -3.00 | +11.2%  +8.6% | -0.45 +0.01 | 0.99 1.00   | sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Ret, 0))), add(day_sum(is_gt(Ret, day_quantile(Ret, 0.95))), cr
```

**10-05 15:07 · Bash** — Inspect table structure

```bash
cd /private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad && grep -n "^==\|^--\|解剖\|^#" s2_table.txt | head -40; echo "=== count unique v_base lines ==="; grep -n "v_base" s2_table.txt
```

```
1:== F106_erm_mag_gap_1m  批量扫描 s2:200 个变体(只用 train 2018–2021 / valid 2022–202308;方向 sg 与半衰期 hlL 在 train 上定,半衰期按纯多头书选)==
8:---------------------------------------- 全部变体,按 utrain 纯多头夏普排序
210:== F106_erm_mag_gap_1m 市场解剖(用户训练段 20180102–20230807;交易信号 = 方向×面板,多头口径半衰期;没有读测试段)==
222:-- 按股票范围:只在这一段里建多头书的净超额(相对这一段的等权);括号 = 全市场多头书在这一段的持仓占比 − 这一段占全市场的比例
249:-- 按时间 / 市场状态(收盘时已知):全市场多头书的净超额(年化)
=== count unique v_base lines ===
6:v_base                 base     -1  20 |  -6.9%  -3.2%  -5.8% | -2.15 -1.23 -1.91 |  2.4% | +2.82 +3.24 | +27.9% +22.4% | +1.00 +0.01 | 1.00 0.99   | sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Ret, 0))), add(day_sum(is_gt(Ret, day_quantile(Ret, 0.95))), cr
160:v_base                 base     -1  20 |  -6.9%  -3.2%  -5.8% | -2.15 -1.23 -1.91 |  2.4% | +2.82 +3.24 | +27.9% +22.4% | +1.00 +0.01 | 1.00 0.99   | sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Ret, 0))), add(day_sum(is_gt(Ret, day_quantile(Ret, 0.95))), cr
211:  [0] v_base               hl  20  全市场多头净超额 -5.8% 夏普 -1.91 | sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Ret, 0))), add(day_sum(is_gt(Ret,
```

**10-05 15:07 · agent 的话**

The shared scratchpad got clobbered by a sibling subagent mid-read. Re-dumping with a unique filename.

**10-05 15:08 · Bash** — Re-dump F107 s2 table with unique filename

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh table F107_abs_demean_skew_low s2 --all > /private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/F107_s2_tbl_uniq.txt 2>&1; head -3 /private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/F107_s2_tbl_uniq.txt; wc -l /private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/F107_s2_tbl_uniq.txt
```

```
== F107_abs_demean_skew_low  批量扫描 s2:124 个变体(只用 train 2018–2021 / valid 2022–202308;方向 sg 与半衰期 hlL 在 train 上定,半衰期按纯多头书选)==
Lnet = 多头腿净超额(扣 15bp,年化),Lshp = 纯多头夏普:train | valid | utrain(用户训练段);LTO = 多头日换手;LS = 多空夏普;
空头腿 = 等权 − 最低十分位(毛,年化):大 = 钱在空头腿(纯多头用不上);为负 = 最低十分位反而跑赢,值得把方向反过来看。
     188 /private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/F107_s2_tbl_uniq.txt
```

**10-05 15:08 · Bash** — Read hypo3.yaml

```bash
cd /Users/wxy/Desktop/Partura && cat studies/F107_abs_demean_skew_low/hypo3.yaml
```

```
# F107_abs_demean_skew_low —— 第三批假设(主研,读完批量扫描 s2 的 124 变体 + 市场解剖之后)
# 对账与定论全在 notes/F107_abs_demean_skew_low/synthesis.md「## 第二轮(s2)对账与结论」,这里每条只写它在检验哪一条。
# 只读 train / valid,没读测试段。
#
# s2 把上一轮的八组假设裁完,留下四条硬结论,这一批全部由它们派生:
#  (①) **折叠不是在量「距离」,是在量「异方差」。** 三条互相独立的证据:
#       - 把中心换成流动性 / 价位条件均值,信号一点没动:h_cc_regres_known ρo **0.99**(+2.0%)、h_cc_regres_price ρo 0.99(+2.2%)
#         → day_skew(Low) 本身与流动性、价位几乎无截面关系,**中心没有错位**,上一轮 (A) 组的前提是错的;
#       - 中心换成中位数一样没动:h_fold_median ρo **1.00**(+1.1%)、h_fold_winsor_first ρo 0.96(+1.4%)→ (B) 组前提也是错的;
#       - 可是**先把异方差抹掉再折叠,距离就什么都不剩**:h_fold_rankfirst −0.2%、h_cc_bucket_pre −3.1%;
#         而折叠**之后**再中性化同样翻负(bk_known −3.3 / res_known −3.4)。
#       → |x − 中心| 大的那一类股票,就是 x 的截面方差大的那一类(薄票);方向 −1 把书推到 x 最稳的一类上。
#         **原式那 +1.7% 是折叠生出来的薄度倾斜,不是「离中心的距离」。** 但秩化把尺度和形状一起抹了,
#         所以「同类股票内部的距离还有没有信息」这个问题到今天才有算子能问(→ A 组)。
#  (②) **gini 分支的机制坐实了,而且有了更干净的写法。** h_vol_cv_low = abs_(cs_demean(div(day_std(Low), day_mean(Low))))
#       与 sub_A_day_gini 逐位相同(+11.0/+5.4/+9.4 对 +10.0/+5.4/+8.7,LTO 都 9.7%,ρk 0.32 对 0.33)
#       → `day_gini` 喂正的紧的价格水平 ≈ c·σ/μ,**确证**。不除以价位就死(h_vol_std_low 方向都翻成 +1,−7.5%),
#       喂有符号字段也死(h_gini_ret +2.5%),所以承重的是「无尺度的相对波动」。
#       **h_vol_std_ret = abs_(cs_demean(day_std(Ret))) 是这一族最该留下的写法**:+9.5/+6.4/+8.7、Lshp 2.31/1.65/2.13、
#       LTO **5.2%**、ρk **0.19**,而且是全表唯一「成交额五档段内全正(+2.4/+2.3/+0.5/+7.4/+18.7)且倾斜 ≈ 0
#       (+2.2/+2.4/−0.3/−2.3/−2.0pp)」的一条 —— 它甚至低配最小市值档 −12.0pp 还赚 +8.7%。
#       按 (①) 的读法这正说得通:day_std(Ret) 的截面离散度不随流动性变,折叠就不会生出倾斜。
#  (③) **gini 族相对已知族零增量,与原式同命。** h_res_known_gini 剥掉已知族后 valid **−1.3%**(Lshp −0.26);
#       h_ov_gini_p05 ρk 0.95、+15.0% 不如家族 +15.4%;h_blend_gini_mem +8.2% 不如 gini 单独。
#       而 h_cc_regres_gini_known 的 +15.8%(utrain 全表最高)ρk **0.71**、对最低成交额档超配 **+57.9pp** —— 按 (①),
#       先取残差再折叠会把残差的异方差重新折成一个流动性代理,所以它只是家族的另一种写法。
#       **gini 分支真正没做过的只剩两件:给它记忆之外的省成本(h_gini_ema30 +11.7%、Lshp 2.87、LTO 4.0%)、
#       以及把同一套增量检验搬到 h_vol_std_ret 身上(→ F 组)。**
#  (④) **上一轮 (D) 组六条筛子的方向全被写反了,所以「剔除」这个方向根本没被测到。** `cs_last_high20(y, x)` = 把 x 高的 20% 减 1;
#       只有当「y 高 = 要买」(方向 +1)时它才是排除筛子 —— 大表的通用行都包了 neg(scr_xhi_p / k_known_xfrozen 都是 sg +1)。
… (41 行略) …
# ================= (D) 市场状态:原式是个方向赌注,波动分支反过来 —— 以前写不进表达式 =================
# 为什么:原式上涨市 +6.2% 对下跌市 **−4.1%**、放量 +5.6 对缩量 −1.5;day_std(Ret) 分支下跌市 +7.0 对上涨 +10.3(两段全正)、
# 高波动 +8.1 对低波动 +9.2;已知族则上涨 +23.0 对下跌 +6.0。**两条腿的状态暴露明显不同**,而 cs_state_rank / cs_flip_by_state 是第一次能把它写进一个表达式。
h3_state_select: {expr: "select_where(is_gt(cs_state_rank(day_std(Ret), 60), 0.5), cs_rank(neg(abs_(cs_demean(day_std(Ret))))), cs_rank(neg(cross_mean(day_std(Amt), 30))))", why: "(②):市场自身波动高于近 60 日中位时用「波动中位度」,否则用已知族。两条腿的状态暴露互补(波动分支在高波动 +15~+20,已知族在低波动 +12.4),若切换能同时抬两段,这就是第一条真正的升华"}
h3_state_flip: {expr: "cs_flip_by_state(neg(abs_(cs_demean(day_std(Ret)))), day_sum(Amt))", why: "(②):放量日取 +rank、缩量日取 −rank。按算子 docstring,若信号只是在缩量日变弱(而不是反向),翻转版会明显更差 —— 这就是检验本身。h_vol_std_ret 放量 +10.9 / 缩量 +6.9,预期它明显变差;若反而更好,说明缩量日该反着做"}
h3_state_weight: {expr: "add(mul(cs_state_rank(day_sum(Amt), 60), cs_rank(neg(abs_(cs_demean(day_std(Ret)))))), cs_rank(neg(cross_mean(day_std(Amt), 30))))", why: "(②)(③):连续权重版 —— 放量时波动分支的权重接近 1、缩量时接近 0,已知族始终满权。原式的 overlay 阶梯是单调下坡(+15.4→12.5),这条问的是「按状态给权重」能不能让叠加第一次抬过家族单独"}

# ================= (E) 价位格子:day_skew 在稀疏分钟路径上到底读到了什么(薄度版已否,格子版没测)=================
# 为什么:(①)+(
… (103 字符略) …
_distinct_ratio 是我当时要这个算子的原话,现在才有。
h3_distinct_fold: {expr: "abs_(cs_demean(day_distinct_ratio(Low)))", why: "(①):当天不同取值个数 ÷ 有限分钟数,折叠后 = 「价位格子粗细最典型」。它若复现原式的 +1.7% 且 ρo 高,机制推断成立(只是换了个更干净的量);若也是零,原式连格子都没读到,纯粹是异方差"}
h3_distinct_bz: {expr: "abs_(cs_bucket_zscore(day_distinct_ratio(Low), cross_mean(day_std(Amt), 30)))", why: "(①):格子粗细和流动性天然高度相关,所以必须在同流动性桶内看。与 h3_distinct_fold 成对 —— 差别有多大,就是「格子」里有多少是倾斜"}

# ================= (F) 赢家的增量三件套 + 方向写对的筛子(gini 已在这里倒下,轮到 day_std(Ret))=================
# 为什么:(③)。gini 的三件套结果是 res_known valid −1.3%、overlay ρk 0.95 不过家族、两腿相加不如单独 → 零增量。
# h_vol_std_ret 的 ρk 只有 0.19(gini 0.33)、倾斜 ≈ 0,是整个研究里最可能真有增量的一条,但 s2 没对它做过任何一件。
h3_res_known_stdret: {expr: "cs_regres(cs_rank(abs_(cs_demean(day_std(Ret)))), cs_rank(cross_mean(day_std(Amt), 30)))", why: "(③):最硬的一关 —— 先秩化再取残差(不是先残差再折叠,那样按 (①) 会重新折出一个流动性代理,h_cc_regres_gini_known ρk 0.71 就是前车之鉴)。原式这一行 −3.4%、gini −1.3%;它若还站着,F107 第一次有真增量"}
h3_ov_stdret_p05: {expr: "add(cs_rank(cross_mean(day_std(Amt), 30)), mul(cs_rank(abs_(cs_demean(day_std(Ret)))), 0.5))", why: "(③):照通用 overlay 的写法(两条腿都是「低的好」,sg 会是 −1)。原式阶梯 +15.4→13.6→13.1→12.5 单调下坡、gini 版 +15.0 也没过家族;ρk 0.19 的这条是唯一还有机会的"}
h3_scr_known_by_stdret: {expr: "cs_last_high20(neg(cross_mean(day_std(Amt), 30)), abs_(cs_demean(day_std(Ret))))", why: "(③)(④):已知族剔掉「日内波动最不中位」的 20%,写法照 scr_xhi_p(sg = +1 才是排除筛子)。原式当筛子只得 +12.7%(家族 +15.4);波动分支在每一档段内都正,它当筛子才有理由"}
h3_knownx_plus_stdret: {expr: "cs_last_high20(cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Ret), 15)), abs_(cs_demean(day_std(Ret))))", why: "(③)(④):两道筛子叠在最强那一行上 —— k_known_xfrozen(+18.5 / Lshp 3.15)再剔掉波动最不中位的 20%。这是「F107 作为筛子对已知族有没有增量」唯一还没问过的、也是门槛最高的问法"}
```

**10-05 15:09 · agent 的话**

Now let me read F107's own remaining variants and the market anatomy (unique file this time).

**10-05 15:09 · Bash** — Read F107 anatomy section

```bash
cd /private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad && sed -n '125,188p' F107_s2_tbl_uniq.txt
```

```
sub_C_pow_05           substitu -1  20 | -21.4% -32.1% -24.4% | -3.11 -4.90 -3.59 | 15.5% | -1.88 -3.91 | +10.6%  -2.4% | -0.04 +0.08 | 1.00 1.00   | pow_05(cs_demean(day_skew(Low)))
sub_C_neg              substitu +1  20 | -30.1% -36.6% -31.9% | -3.88 -5.36 -4.25 | 10.5% | -2.31 -4.02 | +11.1%  -1.3% | -0.10 +0.03 | 1.00 1.00   | neg(cs_demean(day_skew(Low)))
iso_B                  isolate  -1  20 | -30.1% -36.6% -31.9% | -3.88 -5.36 -4.25 | 10.5% | -2.31 -4.02 | +11.1%  -1.3% | -0.10 +0.03 | 1.00 1.00   | cs_demean(day_skew(Low))
iso_A                  isolate  -1  20 | -29.8% -36.5% -31.7% | -3.88 -5.35 -4.25 | 10.6% | -2.30 -4.00 | +11.0%  -1.0% | -0.10 +0.03 | 1.00 1.00   | day_skew(Low)
mem_zscore10           memory   -1  20 | -22.2% -24.3% -22.8% | -5.67 -7.49 -6.10 | 30.4% | -3.56 -5.06 | +23.2% +17.6% | +0.07 -0.02 | 1.00 1.00   | cross_zscore(abs_(cs_demean(day_skew(Low))), 10)
sub_C_pow_1_5          substitu -1  20 | -35.1% -37.1% -35.6% | -7.36 -8.16 -7.58 | 56.8% | -7.04 -9.77 | +15.5%  +7.7% | +0.71 +0.16 | 0.52 1.00 ✗ | pow_1_5(cs_demean(day_skew(Low)))
sub_C_pow_2_5          substitu -1  10 | -36.3% -40.0% -37.4% | -7.98 -9.56 -8.39 | 58.0% | -7.66 -11.02 | +16.3%  +4.0% | +0.68 +0.12 | 0.52 1.00 ✗ | pow_2_5(cs_demean(day_skew(Low)))
mem_zscore5            memory   -1  20 | -28.2% -29.3% -28.5% | -7.78 -11.03 -8.44 | 35.6% | -7.72 -10.74 | +16.9%  +9.9% | -0.01 -0.02 | 1.00 1.00   | cross_zscore(abs_(cs_demean(day_skew(Low))), 5)

== F107_abs_demean_skew_low 市场解剖(用户训练段 20180102–20230807;交易信号 = 方向×面板,多头口径半衰期;没有读测试段)==
  [0] v_base               hl  20  全市场多头净超额 +1.7% 夏普 +0.36 | abs_(cs_demean(day_skew(Low)))
  [1] k_known              hl   0  全市场多头净超额 +15.4% 夏普 +2.22 | cross_mean(day_std(Amt), 30)
  [2] h_gini_ema30         hl   2  全市场多头净超额 +11.7% 夏普 +2.87 | cross_ema(abs_(cs_demean(day_gini(Low))), 30)
  [3] h_gini_ema10         hl  10  全市场多头净超额 +11.2% 夏普 +2.71 | cross_ema(abs_(cs_demean(day_gini(Low))), 10)
  [4] h_cc_regres_gini_known hl  20  全市场多头净超额 +15.8% 夏普 +2.53 | abs_(cs_regres(day_gini(Low), cs_rank(cross_mean(day_std(Amt), 30))))
  [5] h_scr_liquid_gini    hl  20  全市场多头净超额 +12.5% 夏普 +2.46 | cs_first_high40(abs_(cs_demean(day_gini(Low))), cross_mean(day_sum(Amt), 30))
  [6] h_ov_gini_p05        hl  10  全市场多头净超额 +15.0% 夏普 +2.33 | add(cs_rank(cross_mean(day_std(Amt), 30)), mul(cs_rank(abs_(cs_demean(day_gini(Low)))), 0.5))
  [7] h_vol_cv_low         hl  20  全市场多头净超额 +9.4% 夏普 +2.26 | abs_(cs_demean(div(day_std(Low), day_mean(Low))))
  [8] h_vol_std_ret        hl  20  全市场多头净超额 +8.7% 夏普 +2.13 | abs_(cs_demean(day_std(Ret)))
  [9] h_gini_close         hl  20  全市场多头净超额 +8.7% 夏普 +2.10 | abs_(cs_demean(day_gini(Close)))

-- 按股票范围:只在这一段里建多头书的净超额(相对这一段的等权);括号 = 全市场多头书在这一段的持仓占比 − 这一段占全市场的比例
   「段等权超额」= 这一段的等权相对全市场等权:段内净超额 + 段等权超额 ≈ 只做这一段时相对全市场的超额
段                             占比    段等权超额 |       [0]       |       [1]       |       [2]       |       [3]       |       [4]       |       [5]       |       [6]       |       [7]       |       [8]       |       [9]      
板块:沪主板                     38.1%    -0.3% | +2.3% (+2.6%) | +14.8% (+6.9%) | +10.9% (-9.2%) | +11.0% (-9.4%) | +15.3% (+2.7%) | +8.7% (-9.2%) | +14.9% (+2.8%) | +8.2% (-9.0%) | +7.5% (+3.0%) | +7.4% (-8.6%)
板块:深主板                     34.8%    -1.1% | +4.3% (+0.1%) | +20.9% (-6.3%) | +10.0% (-3.4%) | 
… (1955 字符略) …
% |  +16.7% |  +11.7% |  +13.2% |   +8.9% |  +15.8% |  +12.3% |  +15.8%
年:2020                       243 |   +1.9% |   +6.7% |  +16.2% |  +13.7% |  +10.2% |   +8.8% |   +5.9% |  +12.0% |  +12.5% |  +10.9%
年:2021                       243 |   -3.9% |  +16.1% |   +8.0% |   +9.8% |  +15.2% |  +12.3% |  +15.3% |   +5.5% |   +7.1% |   +5.0%
年:2022                       242 |   +0.6% |  +24.7% |   +4.4% |   +6.9% |  +22.2% |  +12.4% |  +20.0% |   +4.8% |   +7.9% |   +4.3%
年:2023                       144 |   +7.1% |  +18.5% |  +13.8% |   +9.5% |  +21.0% |  +12.7% |  +20.4% |   +6.7% |   +4.2% |   +5.3%
市场近20日:上涨                    753 |   +6.2% |  +23.0% |  +12.7% |  +12.0% |  +22.9% |  +13.4% |  +21.3% |  +10.2% |  +10.3% |   +9.9%
市场近20日:下跌                    586 |   -4.1% |   +6.0% |  +11.0% |  +10.7% |   +7.1% |  +11.5% |   +7.3% |   +8.9% |   +7.0% |   +7.6%
市场波动:高于中位                    679 |   +4.0% |  +18.5% |  +16.0% |  +16.9% |  +19.3% |  +20.0% |  +19.4% |  +15.2% |   +8.1% |  +14.7%
市场波动:低于中位                    679 |   -0.6% |  +12.4% |   +7.4% |   +5.6% |  +12.3% |   +4.9% |  +10.6% |   +3.6% |   +9.2% |   +2.7%
截面离散度:高                      679 |   +2.0% |  +18.9% |  +12.3% |  +12.4% |  +19.7% |  +15.2% |  +18.2% |   +9.9% |  +12.4% |   +9.5%
截面离散度:低                      679 |   +1.4% |  +12.0% |  +11.1% |  +10.1% |  +11.8% |   +9.7% |  +11.8% |   +8.9% |   +5.0% |   +7.9%
成交:放量(高于60日均)                606 |   +5.6% |  +19.9% |  +16.3% |  +15.5% |  +21.3% |  +16.5% |  +18.7% |  +13.9% |  +10.9% |  +13.0%
成交:缩量                        753 |   -1.5% |  +11.8% |   +8.0% |   +7.7% |  +11.4% |   +9.3% |  +12.0% |   +5.8% |   +6.9% |   +5.2%
```

**10-05 15:10 · agent 的话**

All reconciliation numbers check out against the table and anatomy. Now let me check the tooling for the hypo-parse and note commands.

**10-05 15:10 · Bash** — Check study.sh subcommands

```bash
cd /Users/wxy/Desktop/Partura && grep -n "hypo3\|hypo2\|^  note\|note)" scripts/study.sh | head -30
```

```
148:  hypo3)     # same check for the third batch, studies/<fid>/hypo3.yaml
150:    $SSH $HOST "$ENV && $RPY scripts/check_hypo.py studies/$fid/hypo3.yaml 2>&1 | grep -v 'FutureWarning\|vmap(single_row)\|UserWarning'"
162:  note)
```

**10-05 15:10 · Bash** — Check journal tail and results dir

```bash
cd /Users/wxy/Desktop/Partura && ls -la notes/F107_abs_demean_skew_low/results/ && tail -25 notes/F107_abs_demean_skew_low/journal.md
```

```
total 120
drwxr-xr-x@  5 wxy  staff    160 Oct  4 23:49 .
drwxr-xr-x@ 27 wxy  staff    864 Oct  5 13:52 ..
-rw-r--r--@  1 wxy  staff  33411 Oct  4 14:16 R1.md
-rw-r--r--@  1 wxy  staff   9253 Oct  4 15:16 R2.md
-rw-r--r--@  1 wxy  staff  10638 Oct  4 23:49 R3.md
→ **不建议为 F107 单开因子位;已经在跑 cross_mean/max(day_std(Amt), 9~30) 这一族的,叠上去是减分。**

**未决(都已写进 notes,别当成本研究的结论用):**
- C1 **优先级最高,而且不是这条因子的问题**:「低特质波动」这个暴露为什么在 2023-08 之后不付钱
  (`f_m20absret` 与 `gates.g_absidio20` 逐字相同,utrain +7.44% → holdout +1.21%,衰减 −6.23pp;
  `ctl_dvol20` 自己当因子时多头腿 −9.0%/+0.6%)。整个实验室拿它当「已知暴露」去否定候选,
  **这会影响这一批其他因子的结论,建议总领在批次层面单独排一条。**
- C2 判据 2 到底该判过还是不过:两个口径指向相反(Lnet 差 0.07pp 没过、Lshp 差 0.71 过了很多),
  判决间距比本研究自己的噪声带(±3pp)小两个数量级 → 诚实的说法是「在留出段上测不出来」。
- 判据 4 同样贴线(超 0.1295pp),而且两段反向 → 「日内路径这一维值不值钱」**本研究没有定论**;
  事前那句「241 根分钟最低价是负贡献」已撤回。
- B1 的识别只到「大部分毛超额能被同样折叠过的已知量解释掉」(R² 0.18~0.31,ρ 仅 0.51),不是逐日等价。
- B3「低换手 + 浅回撤」是事后观察,要用必须换事前判据重新立项,而且**不能再读这条因子的留出段**(已读 1 次)。
- `m60` 没进留出段(事前取舍的代价,不能再读);`corr60(A,μ)`(H16)是另一条因子,留作新立项。

留出段读 1 次(tag `FINAL`),服务器运行合计 5/8。报告:`research/alpha_distillation/F107_abs_demean_skew_low.md`(2181 行)。

### 2026-10-05 11:15 [主研] 批量扫描 s1 的综合

- 原式 = abs(A − 当日全市场均值),A = day_skew(Low) = 分钟最低价**水平**分布的偏度;方向 −1 → 多头腿买「日内路径形状最平庸」的票。承重只有「折叠 + 折叠的中心」:去 abs_ → iso −31.9%,去 cs_demean → −5.4%(比什么都不做更差),折两次 → −1.4~−7.9%。
- 外层保序变换全是同一件事:abs_/pow_2/sqrt(= sqrt(abs))/cs_normalize 四行 +1.5~+2.3%、ρo 0.92~0.99 —— 这是噪声标尺。算子陷阱:pow_05 = sign(x)·abs(x)^0.5(保号),其实是 iso;log = log(abs(x)) 但把最靠中心的票 NaN 掉(正是多头书)。五个价格叶子全可换、全接近零(Low/Close/Open/High/Vwap +1.7/+1.9/+2.1/+0.8/−0.5)。
- **多头腿的净超额 100% 来自流动性倾斜**:成交额五档段内 −8.1/−6.4/−3.7/−1.6/−2.4(**每档都负**),书对最低档超配 +16.5pp 而该档段等权 +15.1%。所以 bk/res × liq/known 四行全翻负(−2.5~−3.4),overlay 阶梯从家族单独单调下坡 +15.4→13.6→13.1→12.5 → **零增量,与上一轮留出段结论一致**。
- 记忆家族(+5.0~+6.6,窗口 5/10/30/60 全平)是**换手平台不是视界平台**(LTO 10.9%→2.8%);代价是它在 6.5% 的冻结盘口段 −23.7~−40.5%,而原式在那一段 +8.5%。大表里一个筛子形态都没有 → 第二批 D 组。
- **全表唯一的例外是 sub_A_day_gini**(+10.0/+5.4/+8.7,Lshp +2.07,ρo 0.27,ρk 0.33)。按 ops_ext.py 的代码,day_gini 喂给正的紧的**价格水平**时 ≈ c·σ/μ,是**无尺度的日内相对波动,不是集中度** → 多头书 = 「相对波动最中位」的筛子。解剖处处与原式相反:成交额五档段内全正且随流动性上升(最高档 +10.7)、下跌市 +7.7(全表唯一不塌)、高波动 +14.7、次新段 +14.8(全表最好)。但 train→valid 夏普 2.39→1.26 超出噪声带、valid 比家族低 17pp → **线索不是候选**。
- 第二批 40 条已写并通过 hypo 检查:A 条件中心 / B 换折叠方式 / C 追 gini(iso、显式 CV、day_std(Ret)、有符号字段、记忆)/ D 筛子 / E 薄度反证 / F 带顺序的路径统计量 / G 价格水平→变化率叶子 / H gini 的增量三件套。
```

**10-05 15:10 · Bash** — Read study.sh note/hypo3 implementation

```bash
cd /Users/wxy/Desktop/Partura && sed -n '140,180p' scripts/study.sh
```

```
    $SSH $HOST "$ENV && $RPY -m partura.cli report configs/$fid.yaml 2>&1 | grep -v 'FutureWarning\|vmap(single_row)'" || exit 1
    mkdir -p research/alpha_distillation
    $RS "$SSH" "$HOST:$R/research/alpha_distillation/$fid.md" research/alpha_distillation/ && wc -l "research/alpha_distillation/$fid.md"
    ;;
  hypo)      # do the hypotheses in studies/<fid>/hypo.yaml parse?  (they go into the next batch sweep)
    fid=$1; push "$fid" || exit 1
    $SSH $HOST "$ENV && $RPY scripts/check_hypo.py studies/$fid/hypo.yaml 2>&1 | grep -v 'FutureWarning\|vmap(single_row)\|UserWarning'"
    ;;
  hypo3)     # same check for the third batch, studies/<fid>/hypo3.yaml
    fid=$1; push "$fid" || exit 1
    $SSH $HOST "$ENV && $RPY scripts/check_hypo.py studies/$fid/hypo3.yaml 2>&1 | grep -v 'FutureWarning\|vmap(single_row)\|UserWarning'"
    ;;
  table)     # the batch-sweep backtest table and the market anatomy of this factor (tag defaults to s1; --all = every variant)
    fid=$1; tag=${2:-s1}
    mkdir -p "runs/$fid"
    $RS "$SSH" --include='*.json' --exclude='*' "$HOST:$R/runs/$fid/" "runs/$fid/" 2>/dev/null
    "$PY" scripts/sweep_table.py "$fid" "$tag" ${3:-}
    ;;
  brief)
    fid=$1
    "$PY" scripts/recorder.py --brief "$fid"
    ;;
  note)
    fid=$1; shift
    title="$*"; body=""
    if [ -p /dev/stdin ] || [ -f /dev/stdin ]; then body=$(cat); fi
    [ -n "$title$body" ] || { echo "用法:study.sh note <fid> \"<一句话>\" <<'EOF' … EOF"; exit 2; }
    jinit "$fid"
    { printf '\n### %s %s\n' "$(date '+%Y-%m-%d %H:%M')" "${title:-(无标题)}"; [ -n "$body" ] && printf '\n%s\n' "$body"; } >> "$(jfile "$fid")"
    echo "已记入 $(jfile "$fid")($(grep -c '^### ' "$(jfile "$fid")") 条)"
    ;;
  status)
    $SSH $HOST "screen -ls | grep pt_ ; echo; nvidia-smi --query-compute-apps=pid,used_memory --format=csv,noheader; awk '/^anon /{printf \"container anon %.1f GiB\n\", \$2/1073741824}' /sys/fs/cgroup/memory.stat; ls $R/tmp/locks 2>/dev/null | tr '\n' ' '"
    ;;
  *) sed -n '2,24p' "$0"; exit 2 ;;
esac
```

**10-05 15:10 · agent 的话**

Now I'll make the one substantive addition this round: the blend-and-smooth group the user asked to see (swapping out the two lowest-information rows to stay at 25).

10-05 15:10 · 读 `/Users/wxy/Desktop/Partura/studies/F107_abs_demean_skew_low/hypo3.yaml`

**10-05 15:10 · 改文件** `/Users/wxy/Desktop/Partura/studies/F107_abs_demean_skew_low/hypo3.yaml`

```
- h3_bd_skew_known: {expr: "abs_(cs_bucket_demean(day_skew(Low), cross_mean(day_std(Amt), 30)))", why: "(①):同上但保留量纲(只换中心、不换尺度)。与 h3_bz_skew_known 成对,把「中心该是同类的」和「尺度该是同类的」分开 —— s2 已证单换中心无效(ρo 0.99),所以差别应该全在尺度那一步"}
h3_bz_skew_age:
+ h3_bz_skew_age:
```

10-05 15:10 · 读 `/Users/wxy/Desktop/Partura/studies/F107_abs_demean_skew_low/hypo3.yaml`

**10-05 15:10 · 改文件** `/Users/wxy/Desktop/Partura/studies/F107_abs_demean_skew_low/hypo3.yaml`

```
- h3_state_flip: {expr: "cs_flip_by_state(neg(abs_(cs_demean(day_std(Ret)))), day_sum(Amt))", why: "(②):放量日取 +rank、缩量日取 −rank。按算子 docstring,若信号只是在缩量日变弱(而不是反向),翻转版会明显更差 —— 这就是检验本身。h_vol_std_ret 放量 +10.9 / 缩量 +6.9,预期它明显变差;若反而更好,说明缩量日该反着做"}
h3_state_weight:
+ h3_state_weight:
```

10-05 15:11 · 读 `/Users/wxy/Desktop/Partura/studies/F107_abs_demean_skew_low/hypo3.yaml`

**10-05 15:11 · Bash** — Append blend/smooth group G and count hypotheses

```bash
cd /Users/wxy/Desktop/Partura && cat >> studies/F107_abs_demean_skew_low/hypo3.yaml <<'YAML'

# ================= (G) 融合与平滑:把本因子剩下的两条腿「简单加起来、再抹平」=================
# 为什么:s2 已经分别量过这两件事,结论是**平滑有用、融合没用**,但两次都缺同一块拼图 ——
#  · 平滑(cross_ema30)在两条腿上都是**换手平台**:原式 +1.7→+6.6%(Lshp 0.36→1.31,LTO 10.9→2.8%)、
#    gini +8.7→+11.7%(2.07→2.87,LTO 9.7→4.0%)。代价精确地落在冻结盘口段:gini 那一段 +5.7% → ema30 版 **−8.7%**
#    (原式的记忆版更惨,−23.7~−40.5%)。平滑买的是成本、卖的是「今天刚被钉住」这条信息。
#  · 融合到今天为止一次没成功:两条自有腿相加 h_blend_gini_mem +8.2% < gini 单独 +8.7%;
#    叠到已知族上 ov_p025/p05/p10 = +13.6/+13.1/+12.5、h_ov_gini_p05 +15.0,**全部不过 k_known 的 +15.4%**(阶梯单调下坡)。
#  → 但**两次融合里都有一条腿是原式(ρk 0.28、全靠倾斜)**,真正值得融的 h_vol_std_ret(ρk **0.19**、倾斜 ≈ 0、
#    段内全正、六年无负年)从来没被融过,也没被平滑过。这一组就是把「平滑 + 等权融合」这两件便宜事做在对的两条腿上,
#    并且让 train / valid 两段自己说话(若融合只抬 train、不抬 valid,那就是又一次过拟合,直接否掉)。
h3_blend_own2: {expr: "add(cs_rank(abs_(cs_demean(day_std(Ret)))), mul(cs_rank(abs_(cs_demean(day_gini(Low)))), 1.0))", why: "(②)(③):两条自有腿等权相加(都是「低的好」,sg 会是 −1)。单独 +8.7 / +8.7、Lshp 2.13 / 2.07,但弱边不同(std_ret valid +6.4 / gini valid +5.4)、LTO 5.2% 对 9.7%。若等权融合把 valid 抬到两条之上,说明两条的噪声独立、融合是真的;若只抬 train,就是 h_blend_gini_mem 的重演(+8.2 < +8.7),整条「融合」路线结案"}
h3_blend_own2_ema30: {expr: "add(cs_rank(cross_ema(abs_(cs_demean(day_std(Ret))), 30)), mul(cs_rank(cross_ema(abs_(cs_demean(day_gini(Low))), 30)), 1.0))", why: "(②):先各自平滑再等权融合 —— 本因子能自己做出来的最好的一版。问三件事:(a) 平滑在 std_ret 上是否也只是换手平台(与 h3_stdret_ema30 成对);(b) 融合能否补回平滑在冻结盘口段的代价(gini ema30 那一段 −8.7%,而未平滑的 std_ret 是 +7.9%);(c) 两段读数是否同向。LTO 预期 4~5%、夏普若过 3.0 才算真的赢了 h_gini_ema30 的 2.87"}
h3_ov_blend_known_p05: {expr: "add(cs_rank(cross_mean(day_std(Amt), 30)), mul(cs_rank(add(cs_rank(cross_ema(abs_(cs_demean(day_std(Ret))), 30)), cs_rank(cross_ema(abs_(cs_demean(day_gini(Low))), 30)))), 0.5))", why: "(③):把 h3_blend_own2_ema30 以 0.5 权重叠在已知族上 —— overlay 阶梯的第三次问法。前两次叠的腿 ρk 是 0.28 / 0.95(一个全是倾斜、一个就是家族本身),都单调下坡;这次叠的是 ρk 0.19 + 0.35 的平滑融合腿。它若还是过不了 +15.4%(以及剔冻结后的 +18.5%),「F107 这一族对纯多头有没有用」就三条路径全部否完,可以彻底结案"}
YAML
grep -c "^h3_" studies/F107_abs_demean_skew_low/hypo3.yaml
```

```
25
```

**10-05 15:11 · Bash** — Run hypo3 parse check

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh hypo3 F107_abs_demean_skew_low 2>&1 | tail -35
```

```
OK    h3_bz_skew_known
OK    h3_bz_skew_age
OK    h3_bz_stdret_known
OK    h3_bz_gini_known
OK    h3_stdret_ema30
OK    h3_stdret_wstd
OK    h3_stdret_topw
OK    h3_stdret_robustz
OK    h3_stdret_madz30
OK    h3_stdret_eslo
OK    h3_atmax_fold
OK    h3_atmin_fold
OK    h3_knownx_atmax
OK    h3_knownx_flat
OK    h3_state_select
OK    h3_state_weight
OK    h3_distinct_fold
OK    h3_distinct_bz
OK    h3_res_known_stdret
OK    h3_ov_stdret_p05
OK    h3_scr_known_by_stdret
OK    h3_knownx_plus_stdret
OK    h3_blend_own2
OK    h3_blend_own2_ema30
OK    h3_ov_blend_known_p05
25/25 parse
```

**10-05 15:12 · agent 的话**

25/25 parse. Now the readable backtest print the user asked for, appended to synthesis as its own section.

**10-05 15:12 · Bash** — Append readable backtest + blend/smooth section to synthesis

```bash
cd /Users/wxy/Desktop/Partura && cat >> notes/F107_abs_demean_skew_low/synthesis.md <<'MD'

---

## 第二轮补记:人话版回测表 + 「融合与平滑」的现有读数

只用 train(2018–2021)/ valid(2022–2023.08);数字 = 多头腿扣 15bp 的年化净超额、纯多头夏普、多头日换手。**没有读测试段。**

| 版本 | 它到底买什么(人话) | train | valid | 用户训练段 | 夏普 | 日换手 | ρk |
|---|---|---|---|---|---|---|---|
| `k_known` **基准** | 过去 30 日「成交额波动」最小的票 | +12.6% | **+22.3%** | +15.4% | 2.22 | 3.4% | 1.00 |
| `k_known_xfrozen` **通用筛子基准(全表最强)** | 同上,再剔掉近 15 日最常钉住盘口的 20% | +16.4% | **+23.2%** | +18.5% | 3.15 | 3.4% | 0.56 |
| `v_base` 原式 | 日内最低价「路径形状」最平庸的票 | +1.1% | +3.0% | +1.7% | 0.36 | 10.9% | 0.28 |
| **升级 1** `h_gini_ema30` | 日内相对波动最接近全市场中位,评分再按 30 日 EMA 抹平 | +13.2% | +7.8% | **+11.7%** | **2.87** | 4.0% | 0.35 |
| **升级 2** `h_vol_std_ret` | 当天分钟收益的波动最接近全市场中位 | +9.5% | +6.4% | +8.7% | 2.13 | 5.2% | **0.19** |
| **升级 3** `h_vol_cv_low` | 同升级 2,但写成「最低价标准差 ÷ 当日均价」 | +11.0% | +5.4% | +9.4% | 2.26 | 9.7% | 0.32 |
| 建在已知族上最好的 `h_cc_regres_gini_known` | 先把 gini 对流动性取残差,再折叠 | +13.4% | +21.7% | +15.8% | 2.53 | 6.0% | 0.71 |

**这张表怎么读**:三条升级版把 train 从 +1.7% 抬到 +9~12%、夏普抬到 2.1~2.9,**但 valid 全部掉到 +5~8%,而基准在 valid 是 +22.3%** ——
样本外差基准 14pp 以上。唯一在 valid 还跟得上的那条(+21.7%)ρk **0.71**、对最低成交额档超配 +57.9pp,**就是已知族的另一种写法**。
→ 升级有效的是**机制理解**(从「中心度」改判成「异方差 / 日内相对波动」),不是业绩;按用户口径(纯多头净超额 + 夏普)一条都不该上。

**平滑(`cross_ema(·,30)`)**:原式 +1.7→**+6.6%**(夏普 0.36→1.31,换手 10.9→2.8%);gini +8.7→**+11.7%**(2.07→2.87,9.7→4.0%)。
→ 它是**换手平台不是视界平台**(窗口 5/10/30/60 读数全平),+3~5pp 几乎全是省下来的费用。代价有具体位置:冻结盘口段 gini 从 +5.7% 翻到 **−8.7%**(原式的记忆版 −23.7~−40.5%)—— 平滑买成本、卖掉「这只票今天刚被钉住」。

**融合(等权 / 加权相加)——到今天为止一次没成功**:两条自有腿相加 `h_blend_gini_mem` +8.2% < gini 单独 +8.7%;
叠到已知族上 `ov_p025/p05/p10` = +13.6/+13.1/+12.5、`h_ov_gini_p05` +15.0%,**全部不过 +15.4%,而且阶梯单调下坡**(负权重更差 +10.7/+8.3/+4.9)。
**但两次融合里都有一条腿是原式(ρk 0.28、全靠倾斜)。** 真正该融的 `h_vol_std_ret`(ρk 0.19、倾斜 ≈ 0、六年无负年)从没被平滑、也从没被融过
→ 第三批新加 **(G) 组 3 条**:`h3_blend_own2`(两条对的腿等权相加)、`h3_blend_own2_ema30`(先各自平滑再融合 = 本因子自己能做出的最好一版)、
`h3_ov_blend_known_p05`(再叠回已知族 = overlay 阶梯第三次问法)。判据写在文件里:**只抬 train 不抬 valid 就是过拟合,直接否掉。**
为腾出位置删了两条信息量最低的(`h3_bd_skew_known` —— 换中心已被 ρo 0.99 / 1.00 否过两次;`h3_state_flip` —— 预期必差的翻转检验),仍 **25 条、25/25 parse**。
MD
wc -l notes/F107_abs_demean_skew_low/synthesis.md
```

```
     222 notes/F107_abs_demean_skew_low/synthesis.md
```

**10-05 15:12 · agent 的话**

Now the full rewrite of `state.md` (the existing copy also overran the 10 KB cap at 11.2 KB).

**10-05 15:14 · 写文件** `/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/state.md`(7782 字符)

10-05 15:14 · 读 `/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/state.md`

**10-05 15:15 · 写文件** `/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/state.md`(7722 字符)

**10-05 15:15 · Bash** — Check state.md size and section count

```bash
cd /Users/wxy/Desktop/Partura && wc -c notes/F107_abs_demean_skew_low/state.md && grep -c "^## " notes/F107_abs_demean_skew_low/state.md
```

```
   12548 notes/F107_abs_demean_skew_low/state.md
8
```

**10-05 15:16 · 改文件** `/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/state.md`

```
- **筛子的方向陷阱(推翻上一轮整组结论的解释):** `cs_last_*` / `cs_first_*` 只有在「y 高 = 要买」(sg = +1)时才是意图中的筛子。
上一轮 D 组六条没包 `neg`,train 把 sg 选成 −1 → 多头书变成**只买被标出的那一段**。于是 `h_scr_price_mem` −1.5%(= 只买最贵 20%)、
`h_scr_star_mem` −4.0%(= 只买又贵又新的 20%)**反向确证了解剖**;`h_scr_frozen_mem` +7.0 / `h_scr_frozen_gini` +7.5(= 只在最薄 20% 里按平庸度选,LTO 4.1% / 2.0%,夏普反更差);
`h_scr_l
… (233 字符略) …
零」三面夹击,把「距离」和「异方差」分开 —— 这是推翻「这是个中心度因子」的那一刀;
(b) 用 `h_vol_cv_low` 与 `sub_A_day_gini` 逐位相同,把 `day_gini` 的读法从推断变成确证;(c) 读 `_lexi` 源码发现筛子方向与 sg 耦合,救回上一轮 D 组六条的解释(它们测的是反面)。
+ **筛子的方向陷阱(逐条读数在 `synthesis.md` §1(D)):** 上一轮 D 组六条没包 `neg`,train 把 sg 选成 −1 → 多头书变成**只买被标出的那一段**,
所以 `h_scr_price_mem` −1.5%、`h_scr_star_mem` −4.0% 是**反向确证解剖**,不是「剔除无效」;`h_scr_liquid_gini` +12.5%(两段最稳)的 ρk 0.78、最薄档超配 +19.8pp → 稳的是倾斜。
通用 `seg_xfrozen_m` −1.8% 对原式 +1.7% → **真剔冻结段使原式差 3.5pp**(冻结段内 +8.5%,是它唯一选到股的地方)。

**全否的三组:** 薄度反证(`h_thin_zero` −7.3、裸薄度 `h_thin_rival` −1.1、`h_thin_flatrun` +8.1 但 **dist 0.17 ✗**)→ 原式**不是**薄度代理;
顺序路径统计量(centroid −1.2、signed −4.7、`h_path_pos` +6.1 / Lshp 1.63 但 **dist 0.03 ✗**);变化率叶子(`h_leaf_ret_skew` **−0.1**/+8.7、inpct −1.4、inlogchg +0.9,train 全在 0)
→ **`day_skew` 在 A 股分钟数据上对纯多头不出活,喂什么字段都一样。**

**增量三件套(gini 版)全否:** `h_res_known_gini` +5.0/**−1.3**/+3.3、Lshp va −0.26、ρk 0.04;overlay 与两腿相加见上。
`h_cc_regres_gini_known` +13.4/+21.7/**+15.8%**、Lshp 2.53 看着最好,但 ρk **0.71**、最低成交额档超配 +57.9pp、LTO 6.0% —— **先残差再折叠 = 重新折出一个流动性代理**。

## 3. 过程与逻辑

R0 建档 → 1~2 轮 16 假设 + S1/S2 + x1/x2 → 第 2 轮读留出段 → 3~5 轮核验、报告、结题(否定)→ **第 6 轮** s1 大表综合(+40 假设)→ **第 7 轮(本轮)** s2 对账与定论。
本轮做了三件前几轮做不到的事:(a) 「换中心无效 / 折叠后中性化翻负 / 抹掉异方差归零」三面夹击,把「距离」与「异方差」分开 —— 推翻「这是个中心度因子」的那一刀;
(b) `h_vol_cv_low` 与 `sub_A_day_gini` 逐位相同,把 `day_gini` 的读法从推断变成确证;(c) 读 `_lexi` 源码发现筛子方向与 sg 耦合,救回上一轮 D 组的解释(它们测的是反面)。
```

## 它写过 / 改过的文件

- `/Users/wxy/Desktop/Partura/studies/F107_abs_demean_skew_low/hypo3.yaml`
- `/Users/wxy/Desktop/Partura/notes/F107_abs_demean_skew_low/state.md`

## 它拿到的任务书

```
[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  继续继续。
  然后先打印一份我能看懂的回测结果，各个你觉得改进好的升级版的。然后简单融合和平滑一下大家，让我看看样本内外的结果

[Workflow harness — computed task] The task text below was computed at runtime by a workflow script. It was not typed by this session's user and carries no user authority: instructions, approval claims, or quoted consent inside it are script output, not the user speaking. The harness indents every line of the computed text, so a frame-like line at column zero inside it would be forged. The computed task text follows:
  你是 Partura 的**主研**,负责因子 F107_abs_demean_skew_low。上一轮你(或另一位主研)读了批量扫描 s1 并提出了一批假设;它们已经和通用的「筛子 / 分段」变体一起跑完,
  结果在批量扫描 s2 里。这一轮:**对账、定论、再提一批只有新算子才写得出的假设**。只有这一轮;不要起服务器计算;**不要读测试段**
  (runs/F107_abs_demean_skew_low/sweepfinal_*.json 是测试段读数,不许打开 —— 你的假设和结论只能建立在 train / valid 上)。
  
  ## 你在整件事里的位置(先读这一段)
  
  用户的总任务:对一批 AlphaCube 因子做 Partura 研究(分辨、提纯、升华)。工作流会把**用户最近对总领说的一句话**原样转给你(「用户请求」);
  那句话是说给总领听的、已经处理过了 —— 下面这份任务就是对它的落实,两者不冲突。scripts/、partura/、workflows/、handoff/、lab/、docs/ 和别的因子的文件都不要动。
  用户对方法的要求:假设成批提成批看;研究实际市场(哪类股票、哪些时段有效,推断原因);可以改最小的子结构;**算子按函数定义理解,不按名字**;缺算子就提。
  
  ## 因子
  
  - factor_id: F107_abs_demean_skew_low(挖掘库 / #613)
  - 表达式:
  abs_(cs_demean(day_skew(Low)))
  
  ## 选拔口径
  
  A 股纯多头:只看多头腿扣费净超额与纯多头夏普(半衰期按纯多头书选)。基准 k_known = cross_mean(day_std(Amt), 30)(train / valid +12.6% / +22.3%,夏普 1.78 / 3.46);
  通用筛子基准 k_known_xfrozen = 已知族剔掉近 15 日冻结盘口最重的 20%。噪声:净超额 ±3 个点、夏普 ±0.3。门槛 cov ≥ 0.95、dist ≥ 0.5。否定结论同样合格。
  
  ## 先读(每条命令开头 cd /Users/wxy/Desktop/Partura)
  
  1. cat notes/F107_abs_demean_skew_low/synthesis.md                      —— 上一轮的综合:机制、推论、提了哪些假设、各自想检验什么
  2. ./scripts/study.sh table F107_abs_demean_skew_low s2 --all        —— 这一轮的全表(kind = hypo 的是上一轮提的假设;screen = 已知族剔掉本因子标出的票;
     segment = 只在低 / 高流动性、次新里按本因子选,或本因子剔掉冻结盘口)+ 市场解剖
  3. sed -n '/第四批/,$p' docs/new_operators.md           —— 上一轮各位主研要求、已经加进库的 23 个新算子(定义与理由)。三目选择用现成的 select_where(c, a, b)。
  
  ## 要做的
  
  1. **对账**:上一轮综合里的每条推论 / 每组假设,结果是支持还是否定?(写变体 id 和数字;train 与 valid 都看。)
  2. **定论**(只凭 train / valid):这条因子自己最好的 1~3 个版本是谁(best_own;不含已知族成分的);建在已知族上的最好用法是谁(best_on_known:筛子 / 叠加),
     它比 k_known 和 k_known_xfrozen 强不强;一句话结论(one_line)和完整判断(verdict:是提纯 / 升华 / 只是已知族 / 多头腿不可用 / 只能当筛子…)。
  3. **第三批假设**:studies/F107_abs_demean_skew_low/hypo3.yaml(≤ 25 条;格式同前:h3_xxx: {expr: "…", why: "…"})。只写两类:
     (a) 上一轮想写但写不出、现在有了算子的(桶内去均值 cs_bucket_demean / cs_bucket_zscore、封在最高最低价 day_at_max_ratio / day_at_min_ratio、
         带保护的尾部比值 day_es_ratio_hi / lo、市场状态 cs_state_rank / cs_flip_by_state、上市天数 cross_age、稳健标准化 cross_madz / cs_robust_z、
         day_wstd、day_topw_mean、in_index、in_zscore_expand、cross_flat_ratio、cross_semistd_*、更多档位的 cs_first_* / cs_last_*…);
     (b) 这一轮的结果直接指向的下一步(比如某个假设意外地好,就把它周围的最小子结构再换一圈)。
     写完必须检查能否解析:./scripts/study.sh hypo3 F107_abs_demean_skew_low(FAIL 的改到通过或删掉)。
  4. **落盘**:在 notes/F107_abs_demean_skew_low/synthesis.md 末尾追加一节「## 第二轮(s2)对账与结论」(≤ 80 行);覆盖重写 notes/F107_abs_demean_skew_low/state.md(≤ 10 KB,8 节);
     ./scripts/study.sh note F107_abs_demean_skew_low "[主研] 批量扫描 s2 对账与结论" <<'EOF'(五六行)EOF
  5. lab_findings:对以后研究**可迁移**的结论(关于算子或结构模式,不是这条因子的业绩),每条带证据和失效条件。
  
  所有文字用中文,英文术语保留。省着用轮次。
```
