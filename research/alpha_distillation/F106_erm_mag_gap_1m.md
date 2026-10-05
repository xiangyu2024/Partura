# Alpha 研究报告 — F106_erm_mag_gap_1m

> 分钟收益右尾 ES/VaR 减左尾 ES/VaR;分母 +1e-6 在「上涨(下跌)分钟不足 5%」的日子塌掉,截面两端由这些日子决定

**数据**: 1942 个交易日 × 5220 只股票 (20180102–20251231) · 标签 `open_vwap15` h=1(可买入:剔除次日开盘封涨停) · 成本 15 bp/单位换手 · 前/后 10% · AlphaCube `1698296` · Partura `6c89c05560a5`

**数据段**: train 20180102–20211231 · valid 20220104–20230807 · utrain 20180102–20230807 · holdout 20230808–20251231 · full 20180102–20251231

> 决策用的数字:方向与 EMA 半衰期在 **train** 上定,在 valid 上确认。与用户表可比的数字:方向与半衰期在 **utrain**(用户的训练段)上定;holdout = 用户的测试段,只在最后读。

## 1. 原始表达式

```
sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Ret, 0))), add(day_sum(is_gt(Ret, day_quantile(Ret, 0.95))), create_like(day_quantile(Ret, 0.95), 1e-06))), add(day_quantile(Ret, 0.95), create_like(day_quantile(Ret, 0.95), 1e-06))), div(div(day_sum(select_where(is_lt(Ret, day_quantile(Ret, 0.05)), abs_(Ret), create_like(Ret, 0))), add(day_sum(is_lt(Ret, day_quantile(Ret, 0.05))), create_like(day_quantile(Ret, 0.05), 1e-06))), add(abs_(day_quantile(Ret, 0.05)), create_like(day_quantile(Ret, 0.05), 1e-06))))
```

**来历**:用户手写库里的 `erm_mag_gap_1m`(extreme-return-magnitude gap,1 分钟版)。用户表里公布的一行是:方向 −1、半衰期 20、
扣费多空夏普 训练 2.91 / 测试 3.11、多头腿毛超额 训练 −4.2% / 测试 −1.4%(用户表只有「训练」「测试」两列,没有单列 valid)。

**Partura 自己的 train / valid 两段**(`books` 决策口径,方向/半衰期在 train 上拟合,`S0_baseline`,`07_S0_baseline.md`):
扣费多空夏普 train **+2.82** / valid **+3.24**,多头腿毛超额 train −5.1% / valid −1.8%。

**留出段复现程度**(= 用户测试段,`S_final`,`books_user` 用户口径即方向/半衰期在 utrain 上拟合,`07_S_final.md` §5):
扣费多空夏普 **+3.108**(公布 3.11)、多头腿**毛**超额 **−1.38%**(公布 −1.4%)——两项都在小数点第二位内精确复现,
说明「原样对纯多头不可用」不是口径/复现误差造成的。用户训练段(utrain)上复现:多空 +2.91、多头腿毛超额 −4.2%,与公布的训练列一致。

**一句话**:对每只股票每天的 241 个分钟收益,算「右尾 5% 的尾内均值 ÷ 95% 分位数」减「左尾 5% 的尾内均值 ÷ 5% 分位数的绝对值」
—— 字面上是 **右尾 ES/VaR 减 左尾 ES/VaR**,一个「上跳比下跳更尖」的日内尾部形状不对称量。

**读完源码和探针之后的一句话**(和字面不一样):两个分母都是「分位数 + 1e-6」。A 股分钟收益里有大量精确的 0(价格没动),
所以一天里上涨分钟不到 5%(≤12 个)时 95% 分位数恰好是 0,右侧比值变成「上涨分钟的平均幅度 × 10⁶」,量级从 1 跳到 10³~10⁵;
左侧同理。截面排序的两端因此不由「尾部形状」决定,而由**哪些股票最近出现过这种「一侧几乎不动」的日子、以及那几分钟跳了多大**决定。
这条因子在用户口径下的全部多空收益来自空头腿(训练段空头腿毛超额 +26.3%),多头腿是负的 —— 对只能做多的用户,它原样不能用。

**一句话它是什么**:不是日内尾部形状,而是「最近有没有封过涨停板、封板前那几分钟跳了多大」的一年期记忆(封板记忆)。详见 `09_diagnosis.md` A1。

## 2. 算子的真实语义

> 每一条都来自注册表与内核源码,加上在张量上实跑的探针;没有一条是从算子名字推断的。探针集合按**这棵树**挑:不适用的写明,本研究新增的单独标出。

### `day_quantile(·, 0.95)`

- **实现**: `operators/dt_day.py:150` (kernel `dt_day.day_quantile`)
- **声明**: face `dt` / family `day` / category `general`, arity 1, 计算轴 `M`, 无窗口, 折叠分钟轴 (M→1), **搜索语法之外的通用调用**(带字面量参数)
- **标志**: 无
- **实测探针**: 分钟顺序依赖 = False; 平移不变 = False; 齐次度 k = 1.0; nan_behaviour = finite_frac_with_10pct_missing=1.0, all_nan_input_gives_all_nan=True; 取负后 = neither
- **本研究新增的探针**: quantile_order_statistic = position_on_ramp_0..240=228.0, position_with_first_minute_missing(values 1..240)=228.05, is_exact_order_statistic_at_241=True, is_interpolated_at_240=True, selfcheck={'median_of_ramp_is_120': True, 'max_of_ramp_is_240': True}; tail_ratio_knot = right_ratio_by_k_up(241 valid)={0: 0.0, 1: 1999.998, 6: 2050.0, 11: 2100.0, 12: 2110.0, 13: 1.064, 14: 1.064, 24: 1.058, 60: 1.044}, right_ratio_by_k_up(240 valid)={0: 0.0, 1: 1999.998, 6: 2050.0, 11: 2100.0, 12: 20.89, 13: 1.064, 14: 1.063, 24: 1.058, 60: 1.044}, left_ratio_by_k_dn(241 valid)={1: 1999.998, 12: 2110.0, 13: 1.064, 24: 1.058}, tree_on_corner_cases={'up_sparse(5 up,40 dn)': 2038.95, 'dn_sparse(40 up,5 dn)': -2038.95, 'both_sparse(5 up,5 dn)': -0.0, 'neither(40 up,40 dn)': 0.0, 'price_never_moves': 0.0}, gaussian_mean_right=1.2616, gaussian_mean_left=1.2595, gaussian_sd_of_tree=0.1043, tail_minutes_float32(right,left)=[12.0, 12.0], tail_minutes_float64(right,left)=[12.0, 12.0], max_abs(tree(r)+tree(-r))_float32=0.0, selfcheck={'gaussian_right_near_1.254': True, 'gaussian_left_near_1.254': True, 'tree_is_odd_in_float64': True}; scale_degree_by_regime = regular_max_abs_change_c2=0.00027, blown_up_ratio_c2=2.0005, regular_max_abs_change_c4=0.00041, blown_up_ratio_c4=4.0015, selfcheck={'day_std_has_degree_1': True, 'regular_is_scale_free': True}; tick_grid_regime_share = vol~1.2%/day={'price_2': {'right_blown': 0.244, 'left_blown': 0.233, 'any_side_ge5': 0.33, 'median_abs_tree': 0.0}, 'price_3': {'right_blown': 0.005, 'left_blown': 0.003, 'any_side_ge5': 0.008, 'median_abs_tree': 0.0}, 'price_5': {'right_blown': 0.0, 'left_blown': 0.0, 'any_side_ge5': 0.0, 'median_abs_tree': 0.0}, 'price_10': {'right_blown': 0.0, 'left_blown': 0.0, 'any_side_ge5': 0.0, 'median_abs_tree': 0.24}, 'price_30': {'right_blown': 0.0, 'left_blown': 0.0, 'any_side_ge5': 0.0, 'median_abs_tree': 0.1}}, vol~0.6%/day={'price_2': {'right_blown': 0.919, 'left_blown': 0.92, 'any_side_ge5': 0.941, 'median_abs_tree': 25.0}, 'price_3': {'right_blown': 0.659, 'left_blown': 0.656, 'any_side_ge5': 0.733, 'median_abs_tree': 11.06}, 'price_5': {'right_blown': 0.039, 'left_blown': 0.041, 'any_side_ge5': 0.068, 'median_abs_tree': 0.0}, 'price_10': {'right_blown': 0.0, 'left_blown': 0.0, 'any_side_ge5': 0.0, 'median_abs_tree': 0.0}, 'price_30': {'right_blown': 0.0, 'left_blown': 0.0, 'any_side_ge5': 0.0, 'median_abs_tree': 0.11}}, selfcheck={'continuous_price_never_blows_up': True, 'continuous_right_ratio_near_1.25': True}; single_minute_leverage = mean_tree_by_gap_in_sigma={0.0: 0.002, 3.0: 0.039, 5.0: 0.14, 10.0: 0.392, 20.0: 0.897, -10.0: -0.386}, first_order_estimate={5.0: 0.149, 10.0: 0.402, 20.0: 0.909}, sd_of_tree_without_gap=0.107, selfcheck={'no_gap_is_centred': True, 'mirror_gap_flips_sign': True}
- <sub>不适用的探针: causal_on_day_axis, rank_preserving, monotone_in_window, effective_memory</sub>
- **docstring**: Per-day quantile of the row. Collapses the original's redundant

### `is_gt(·, ·)`

- **实现**: `operators/common.py:240` (kernel `common.is_gt`)
- **声明**: face `shared` / family `elementwise` / category `general`, arity 2, 计算轴 `None`, 无窗口, **搜索语法之外的通用调用**(带字面量参数)
- **标志**: 无
- **实测探针**: 平移不变 = True; 齐次度 k = 0.0; nan_behaviour = finite_frac_with_10pct_missing=1.0, all_nan_input_gives_all_nan=False; 取负后 = neither
- <sub>不适用的探针: causal_on_day_axis, order_dependent_on_minutes, rank_preserving, monotone_in_window, effective_memory, quantile_order_statistic, tail_ratio_knot, scale_degree_by_regime, tick_grid_regime_share, single_minute_leverage</sub>

### `create_like(·, 0)`

- **实现**: `operators/common.py:87` (kernel `common.create_like`)
- **声明**: face `shared` / family `elementwise` / category `general`, arity 1, 计算轴 `None`, 无窗口, **搜索语法之外的通用调用**(带字面量参数)
- **标志**: 无
- **实测探针**: 平移不变 = True; 齐次度 k = None; nan_behaviour = finite_frac_with_10pct_missing=1.0, all_nan_input_gives_all_nan=False; 取负后 = even
- <sub>不适用的探针: causal_on_day_axis, order_dependent_on_minutes, rank_preserving, monotone_in_window, effective_memory, quantile_order_statistic, tail_ratio_knot, scale_degree_by_regime, tick_grid_regime_share, single_minute_leverage</sub>

### `select_where(·, ·, ·)`

- **实现**: `operators/common.py:294` (kernel `common.select_where`)
- **声明**: face `shared` / family `elementwise` / category `general`, arity 3, 计算轴 `None`, 无窗口, **搜索语法之外的通用调用**(带字面量参数)
- **标志**: 无
- **实测探针**: 平移不变 = False; 齐次度 k = 1.0; nan_behaviour = finite_frac_with_10pct_missing=0.8917, all_nan_input_gives_all_nan=True; 取负后 = odd
- <sub>不适用的探针: causal_on_day_axis, order_dependent_on_minutes, rank_preserving, monotone_in_window, effective_memory, quantile_order_statistic, tail_ratio_knot, scale_degree_by_regime, tick_grid_regime_share, single_minute_leverage</sub>

### `day_sum`

- **实现**: `operators/dt_day.py:83` (kernel `dt_day.day_sum`)
- **声明**: face `dt` / family `day` / category `unary`, arity 1, 计算轴 `M`, 无窗口, 折叠分钟轴 (M→1)
- **标志**: 无
- **实测探针**: 分钟顺序依赖 = False; 平移不变 = False; 齐次度 k = 1.0; nan_behaviour = finite_frac_with_10pct_missing=1.0, all_nan_input_gives_all_nan=True; 取负后 = odd
- <sub>不适用的探针: causal_on_day_axis, rank_preserving, monotone_in_window, effective_memory, quantile_order_statistic, tail_ratio_knot, scale_degree_by_regime, tick_grid_regime_share, single_minute_leverage</sub>

### `create_like(·, 1e-06)`

- **实现**: `operators/common.py:87` (kernel `common.create_like`)
- **声明**: face `shared` / family `elementwise` / category `general`, arity 1, 计算轴 `None`, 无窗口, **搜索语法之外的通用调用**(带字面量参数)
- **标志**: 无
- **实测探针**: 平移不变 = True; 齐次度 k = 0.0; nan_behaviour = finite_frac_with_10pct_missing=1.0, all_nan_input_gives_all_nan=False; 取负后 = even
- <sub>不适用的探针: causal_on_day_axis, order_dependent_on_minutes, rank_preserving, monotone_in_window, effective_memory, quantile_order_statistic, tail_ratio_knot, scale_degree_by_regime, tick_grid_regime_share, single_minute_leverage</sub>

### `add`

- **实现**: `operators/common.py:129` (kernel `common.add`)
- **声明**: face `shared` / family `elementwise` / category `binary`, arity 2, 计算轴 `None`, 无窗口
- **标志**: 无
- **实测探针**: 平移不变 = False; 齐次度 k = 1.0; nan_behaviour = finite_frac_with_10pct_missing=0.8917, all_nan_input_gives_all_nan=True; 取负后 = odd
- <sub>不适用的探针: causal_on_day_axis, order_dependent_on_minutes, rank_preserving, monotone_in_window, effective_memory, quantile_order_statistic, tail_ratio_knot, scale_degree_by_regime, tick_grid_regime_share, single_minute_leverage</sub>
- **docstring**: Elementwise add. `fill_nan_with_zero=True` treats a lone NaN operand as

### `div`

- **实现**: `operators/common.py:167` (kernel `common.div`)
- **声明**: face `shared` / family `elementwise` / category `binary`, arity 2, 计算轴 `None`, 无窗口
- **标志**: 无
- **实测探针**: 平移不变 = False; 齐次度 k = 0.0; nan_behaviour = finite_frac_with_10pct_missing=0.8917, all_nan_input_gives_all_nan=True; 取负后 = even
- <sub>不适用的探针: causal_on_day_axis, order_dependent_on_minutes, rank_preserving, monotone_in_window, effective_memory, quantile_order_statistic, tail_ratio_knot, scale_degree_by_regime, tick_grid_regime_share, single_minute_leverage</sub>

### `day_quantile(·, 0.05)`

- **实现**: `operators/dt_day.py:150` (kernel `dt_day.day_quantile`)
- **声明**: face `dt` / family `day` / category `general`, arity 1, 计算轴 `M`, 无窗口, 折叠分钟轴 (M→1), **搜索语法之外的通用调用**(带字面量参数)
- **标志**: 无
- **实测探针**: 分钟顺序依赖 = False; 平移不变 = False; 齐次度 k = 1.0; nan_behaviour = finite_frac_with_10pct_missing=1.0, all_nan_input_gives_all_nan=True; 取负后 = neither
- **本研究新增的探针**: quantile_order_statistic = position_on_ramp_0..240=12.0, position_with_first_minute_missing(values 1..240)=12.95, is_exact_order_statistic_at_241=True, is_interpolated_at_240=True, selfcheck={'median_of_ramp_is_120': True, 'max_of_ramp_is_240': True}; tail_ratio_knot = right_ratio_by_k_up(241 valid)={0: 0.0, 1: 1999.998, 6: 2050.0, 11: 2100.0, 12: 2110.0, 13: 1.064, 14: 1.064, 24: 1.058, 60: 1.044}, right_ratio_by_k_up(240 valid)={0: 0.0, 1: 1999.998, 6: 2050.0, 11: 2100.0, 12: 20.89, 13: 1.064, 14: 1.063, 24: 1.058, 60: 1.044}, left_ratio_by_k_dn(241 valid)={1: 1999.998, 12: 2110.0, 13: 1.064, 24: 1.058}, tree_on_corner_cases={'up_sparse(5 up,40 dn)': 2038.95, 'dn_sparse(40 up,5 dn)': -2038.95, 'both_sparse(5 up,5 dn)': -0.0, 'neither(40 up,40 dn)': 0.0, 'price_never_moves': 0.0}, gaussian_mean_right=1.2616, gaussian_mean_left=1.2595, gaussian_sd_of_tree=0.1043, tail_minutes_float32(right,left)=[12.0, 12.0], tail_minutes_float64(right,left)=[12.0, 12.0], max_abs(tree(r)+tree(-r))_float32=0.0, selfcheck={'gaussian_right_near_1.254': True, 'gaussian_left_near_1.254': True, 'tree_is_odd_in_float64': True}; scale_degree_by_regime = regular_max_abs_change_c2=0.00027, blown_up_ratio_c2=2.0005, regular_max_abs_change_c4=0.00041, blown_up_ratio_c4=4.0015, selfcheck={'day_std_has_degree_1': True, 'regular_is_scale_free': True}; tick_grid_regime_share = vol~1.2%/day={'price_2': {'right_blown': 0.244, 'left_blown': 0.233, 'any_side_ge5': 0.33, 'median_abs_tree': 0.0}, 'price_3': {'right_blown': 0.005, 'left_blown': 0.003, 'any_side_ge5': 0.008, 'median_abs_tree': 0.0}, 'price_5': {'right_blown': 0.0, 'left_blown': 0.0, 'any_side_ge5': 0.0, 'median_abs_tree': 0.0}, 'price_10': {'right_blown': 0.0, 'left_blown': 0.0, 'any_side_ge5': 0.0, 'median_abs_tree': 0.24}, 'price_30': {'right_blown': 0.0, 'left_blown': 0.0, 'any_side_ge5': 0.0, 'median_abs_tree': 0.1}}, vol~0.6%/day={'price_2': {'right_blown': 0.919, 'left_blown': 0.92, 'any_side_ge5': 0.941, 'median_abs_tree': 25.0}, 'price_3': {'right_blown': 0.659, 'left_blown': 0.656, 'any_side_ge5': 0.733, 'median_abs_tree': 11.06}, 'price_5': {'right_blown': 0.039, 'left_blown': 0.041, 'any_side_ge5': 0.068, 'median_abs_tree': 0.0}, 'price_10': {'right_blown': 0.0, 'left_blown': 0.0, 'any_side_ge5': 0.0, 'median_abs_tree': 0.0}, 'price_30': {'right_blown': 0.0, 'left_blown': 0.0, 'any_side_ge5': 0.0, 'median_abs_tree': 0.11}}, selfcheck={'continuous_price_never_blows_up': True, 'continuous_right_ratio_near_1.25': True}; single_minute_leverage = mean_tree_by_gap_in_sigma={0.0: 0.002, 3.0: 0.039, 5.0: 0.14, 10.0: 0.392, 20.0: 0.897, -10.0: -0.386}, first_order_estimate={5.0: 0.149, 10.0: 0.402, 20.0: 0.909}, sd_of_tree_without_gap=0.107, selfcheck={'no_gap_is_centred': True, 'mirror_gap_flips_sign': True}
- <sub>不适用的探针: causal_on_day_axis, rank_preserving, monotone_in_window, effective_memory</sub>
- **docstring**: Per-day quantile of the row. Collapses the original's redundant

### `is_lt(·, ·)`

- **实现**: `operators/common.py:246` (kernel `common.is_lt`)
- **声明**: face `shared` / family `elementwise` / category `general`, arity 2, 计算轴 `None`, 无窗口, **搜索语法之外的通用调用**(带字面量参数)
- **标志**: 无
- **实测探针**: 平移不变 = True; 齐次度 k = 0.0; nan_behaviour = finite_frac_with_10pct_missing=1.0, all_nan_input_gives_all_nan=False; 取负后 = neither
- <sub>不适用的探针: causal_on_day_axis, order_dependent_on_minutes, rank_preserving, monotone_in_window, effective_memory, quantile_order_statistic, tail_ratio_knot, scale_degree_by_regime, tick_grid_regime_share, single_minute_leverage</sub>

### `abs_`

- **实现**: `operators/common.py:188` (kernel `common.abs_`)
- **声明**: face `shared` / family `elementwise` / category `unary`, arity 1, 计算轴 `None`, 无窗口
- **标志**: 无
- **实测探针**: 平移不变 = False; 齐次度 k = 1.0; 保序 = False; nan_behaviour = finite_frac_with_10pct_missing=0.8917, all_nan_input_gives_all_nan=True; 取负后 = even
- <sub>不适用的探针: causal_on_day_axis, order_dependent_on_minutes, monotone_in_window, effective_memory, quantile_order_statistic, tail_ratio_knot, scale_degree_by_regime, tick_grid_regime_share, single_minute_leverage</sub>

### `sub`

- **实现**: `operators/common.py:145` (kernel `common.sub`)
- **声明**: face `shared` / family `elementwise` / category `binary`, arity 2, 计算轴 `None`, 无窗口
- **标志**: 无
- **实测探针**: 平移不变 = True; 齐次度 k = 1.0; nan_behaviour = finite_frac_with_10pct_missing=0.8917, all_nan_input_gives_all_nan=True; 取负后 = odd
- <sub>不适用的探针: causal_on_day_axis, order_dependent_on_minutes, rank_preserving, monotone_in_window, effective_memory, quantile_order_statistic, tail_ratio_knot, scale_degree_by_regime, tick_grid_regime_share, single_minute_leverage</sub>

<details><summary>每个探针在问什么</summary>

- `causal_on_day_axis` — 输出的某一行会不会被后面的行改变?(读未来)
- `effective_memory` — 脉冲输入之后,输出还在多少天里记得它?
- `homogeneity_degree` — f(c·x) = c^k·f(x) 里的 k 是多少?(带不带尺度)
- `monotone_in_window` — 窗口变长时输出怎么动?(极值型单调,均值型不单调)
- `nan_behaviour` — 10% 缺失下还剩多少有限值?整行缺失会怎样?
- `order_dependent_on_minutes` — 打乱分钟顺序会不会改变输出?(路径统计量 vs 分布统计量)
- `quantile_order_statistic` — 241 个分钟的一行上,这个分位数读的是第几个顺序统计量?少一个分钟(240 个有效值)时是不是插值?  _(本研究新增,来自 `probes.py`)_
- `rank_preserving` — f 会不会改变输入的顺序?(保序的外层变换对排名型指标无效)
- `scale_degree_by_regime` — 把分钟收益整体放大 c 倍:常规区间里整棵树变不变?分母塌掉的区间里呢?  _(本研究新增,来自 `probes.py`)_
- `shift_invariant` — f(x + c) 是否等于 f(x)?(是否只看相对位置)
- `sign_sensitivity` — 把输入整体取负,输出是跟着变号、不变,还是别的?
- `single_minute_leverage` — 常规区间里,一个分钟的离群收益(比如开盘跳空 g 倍分钟波动)能把整棵树推多远?  _(本研究新增,来自 `probes.py`)_
- `tail_ratio_knot` — 一天里只有 k 个上涨分钟(其余为 0)时,右侧 ES/(q95+1e-6) 读多少?结在第几个 k?  _(本研究新增,来自 `probes.py`)_
- `tick_grid_regime_share` — 只因为价格网格(低价 × 低波动),一只股票有多大比例的日子掉进「分母塌掉」的区间?  _(本研究新增,来自 `probes.py`)_

</details>

> 本研究额外加载了探针文件:`/root/autodl-tmp/Partura/studies/F106_erm_mag_gap_1m/probes.py`


### 既往研究留下的先验

_(实验室里没有与这棵树相关的、来自**其他**研究的既往结论 —— 本研究自己的结论不算先验。)_

读了每个算子的服务器内核源码(`study.sh src`),和名字不一样、或者探针表里看不出来的地方:

1. **`day_quantile(x, q)` = `torch.nanquantile(x, q, dim=-1)`,线性插值**。241 个分钟全有值时,q=0.95 的位置是 0.95×240 = 228.0,
   恰好是一个顺序统计量(从小到大第 229 个 = 第 13 大),不插值;少一个分钟(240 个有效值)位置就是 227.05,变成两个相邻顺序统计量的
   5%/95% 加权(探针 `quantile_order_statistic`:斜坡 0..240 上读 228.0;缺第一分钟读 228.05)。
   所以「95% 分位数恰好为 0」的条件是:**上涨分钟 ≤ 12 个**(241 个有效分钟时)。
2. **`is_gt` / `is_lt` 是严格不等号,而且 NaN 比较为假 → 输出 0(不是 NaN)**。两个后果:
   (a) 与分位数并列的分钟不进尾部 —— 分钟收益里并列极多(同一个 tick 的涨跌、0),尾部集合可以远少于 12 个、甚至是空集;
   (b) 缺失分钟在 `select_where` 之后变成 0 而不是 NaN,所以求和、计数都只数有效分钟,整棵树对「部分分钟缺失」没有 NaN 传播;
   只有整天缺失(分位数是 NaN)才输出 NaN —— 这就是 cov = 1.00 的原因。
3. **`create_like(x, 0)` 用的是整数 0 → 张量 dtype 是 int64**;`create_like(x, 1e-06)` 是 float32。`select_where` 里 float32 与 int64
   混用靠 `torch.where` 的类型提升,结果是 float32,数值上没有问题,只是占内存。
4. **计数分母上的 `+1e-6` 只在尾部集合为空时起作用**(求和也是 0,结果 0/1e-6 = 0),是纯粹的除零保护,不改变任何非空情形的值。
   **分位数分母上的 `+1e-6` 才是这棵树的要害**:它是一个带量纲的常数(收益单位),比一个 tick 的收益(10⁻³ 量级)小三个数量级,
   所以分位数为 0 时比值被放大 10⁶ 倍。
5. **右侧分母是 `q95 + 1e-6`(没有绝对值),左侧是 `|q05| + 1e-6`**。q95 理论上可以是负的(全天 95% 的分钟都在跌),
   那时右侧比值会变号甚至再次接近除零;实际上这种日子极少(需要 >229 个分钟为负)。
6. **整棵树在服务器上关于 Ret 是精确的奇函数**(探针:`max|tree(r)+tree(−r)|` = 0.0,两侧尾部各 12 个分钟)。
   本机那份 torch 把 0.95×240 算成比 228 略小,右尾会多收进分位数本身那一个分钟(13 对 12)—— 这是「本机不是事实来源」的一个实例,
   以服务器为准。
7. `day_sum` = `nansum`,整行全 NaN 才给 NaN。`abs_`、`add`、`sub`、`div` 就是 torch 的逐元素运算,没有 NaN 填充(`fill_nan_with_zero` 默认关)。

**这棵树里没有任何日轴算子**:它是纯粹的「当天 241 个分钟 → 一个数」,真实回看 1 天。全部的时间结构来自口径里的因果 EMA(半衰期)。

## 3. 数学分解

```
A = day_quantile(Ret, 0.95)
B = is_gt(Ret, A)
C = create_like(Ret, 0)
D = select_where(B, Ret, C)
E = day_sum(D)
F = day_sum(B)
G = create_like(A, 1e-06)
H = add(F, G)
I = div(E, H)
J = add(A, G)
K = div(I, J)
L = day_quantile(Ret, 0.05)
M = is_lt(Ret, L)
N = abs_(Ret)
O = select_where(M, N, C)
P = day_sum(O)
Q = day_sum(M)
R = create_like(L, 1e-06)
S = add(Q, R)
T = div(P, S)
U = abs_(L)
V = add(U, R)
W = div(T, V)
X = sub(K, W)
```

| 变量 | 算子 | 计算轴 | 窗口 | 输出形状 | 被引用 | 结构角色 |
|---|---|---|---|---|---|---|
| `A` | `day_quantile(·, 0.95)` | 日内分钟轴 (M) | — | 每股票-日一个值 | 3× | 日内事件提取(日内分布统计量,齐次度 1.0) |
| `B` | `is_gt(·, ·)` | 逐元素 | — | 每股票-日-分钟一个值 | 2× | 事件判定(0/1 掩码) |
| `C` | `create_like(·, 0)` | 逐元素 | — | 每股票-日-分钟一个值 | 2× | 逐元素变换(保序=None,齐次度 None) |
| `D` | `select_where(·, ·, ·)` | 逐元素 | — | 每股票-日-分钟一个值 | 1× | 多路信号逐元素组合 |
| `E` | `day_sum` | 日内分钟轴 (M) | — | 每股票-日一个值 | 1× | 日内事件提取(日内分布统计量,齐次度 1.0) |
| `F` | `day_sum` | 日内分钟轴 (M) | — | 每股票-日一个值 | 1× | 日内事件提取(日内分布统计量,齐次度 1.0) |
| `G` | `create_like(·, 1e-06)` | 逐元素 | — | 每股票-日一个值 | 2× | 逐元素变换(保序=None,齐次度 0.0) |
| `H` | `add` | 逐元素 | — | 每股票-日一个值 | 1× | 多路信号逐元素组合 |
| `I` | `div` | 逐元素 | — | 每股票-日一个值 | 1× | 多路信号逐元素组合 |
| `J` | `add` | 逐元素 | — | 每股票-日一个值 | 1× | 多路信号逐元素组合 |
| `K` | `div` | 逐元素 | — | 每股票-日一个值 | 1× | 多路信号逐元素组合 |
| `L` | `day_quantile(·, 0.05)` | 日内分钟轴 (M) | — | 每股票-日一个值 | 3× | 日内事件提取(日内分布统计量,齐次度 1.0) |
| `M` | `is_lt(·, ·)` | 逐元素 | — | 每股票-日-分钟一个值 | 2× | 事件判定(0/1 掩码) |
| `N` | `abs_` | 逐元素 | — | 每股票-日-分钟一个值 | 1× | 逐元素变换(保序=False,齐次度 1.0) |
| `O` | `select_where(·, ·, ·)` | 逐元素 | — | 每股票-日-分钟一个值 | 1× | 多路信号逐元素组合 |
| `P` | `day_sum` | 日内分钟轴 (M) | — | 每股票-日一个值 | 1× | 日内事件提取(日内分布统计量,齐次度 1.0) |
| `Q` | `day_sum` | 日内分钟轴 (M) | — | 每股票-日一个值 | 1× | 日内事件提取(日内分布统计量,齐次度 1.0) |
| `R` | `create_like(·, 1e-06)` | 逐元素 | — | 每股票-日一个值 | 2× | 逐元素变换(保序=None,齐次度 0.0) |
| `S` | `add` | 逐元素 | — | 每股票-日一个值 | 1× | 多路信号逐元素组合 |
| `T` | `div` | 逐元素 | — | 每股票-日一个值 | 1× | 多路信号逐元素组合 |
| `U` | `abs_` | 逐元素 | — | 每股票-日一个值 | 1× | 逐元素变换(保序=False,齐次度 1.0) |
| `V` | `add` | 逐元素 | — | 每股票-日一个值 | 1× | 多路信号逐元素组合 |
| `W` | `div` | 逐元素 | — | 每股票-日一个值 | 1× | 多路信号逐元素组合 |
| `X` | `sub` | 逐元素 | — | 每股票-日一个值 | 1× | 多路信号逐元素组合 |

- 节点数 55(含叶子),去重后 24 个中间量,深度 8,用到的字段: Ret
- 日轴最大单窗口 0 天;**沿路径累计的真实回看 1 天**(AlphaCube 的 `max_window` 取最大值而不是路径累加,预热行数按它算)
- 被重复使用的中间量:`A`×3, `B`×2, `C`×2, `G`×2, `L`×3, `M`×2, `R`×2 —— 整棵树其实是围绕它们写的

记当天有效分钟收益为 r₁…rₙ,q⁺ = Q₀.₉₅(r),q⁻ = Q₀.₀₅(r),U = {r > q⁺},D = {r < q⁻}(严格不等):

```
ES⁺ = Σ_U r / (|U| + 1e-6)          ES⁻ = Σ_D |r| / (|D| + 1e-6)
R   = ES⁺ / (q⁺ + 1e-6)             L   = ES⁻ / (|q⁻| + 1e-6)
X   = R − L
```

SSA 表里 24 个中间量其实只有 4 个量:两个分位数(各被引用 3 次)、两个尾内均值。**它有三个取值区间,量级差三到五个数量级**
(探针 `tail_ratio_knot`,用服务器内核、float32):

| 区间 | 条件(241 个有效分钟) | R(或 L)读数 | 含义 |
|---|---|---|---|
| 常规 | 上涨分钟 ≥ 13 个且幅度有差异 | 1.0~3(高斯分钟收益:右 1.262、左 1.260,理论值 1.254) | 尾部形状:ES/VaR |
| 并列 | 上涨分钟 ≥ 13 个但都是同一个 tick | ≈ 1.04~1.06(尾内均值 ≈ 分位数) | 价格网格,不是形状 |
| 塌缩 | 上涨分钟 ≤ 12 个 | **ES⁺ × 10⁶**(一个 0.2% 的 tick → 2000~2110) | 「这一侧几乎没动」× 那几下的幅度 |
| (边缘) | 240 个有效分钟且恰好 12 个上涨分钟 | ≈ 20.9(分位数是 5% × 最小上涨幅度) | 插值造成的过渡 |

整棵树在四个角上的读数(同一个探针):只有上涨稀少 → **+2039**;只有下跌稀少 → **−2039**;两边都稀少且幅度相同 → 0;
两边都不稀少 → 0;价格全天不动 → 0。也就是说:

- **X 的截面两端一定是塌缩日**。常规区间里 X 的标准差只有约 0.10(高斯)到 0.3,塌缩日是 ±10³ 以上。
- **塌缩区间里 X 不再是无量纲的**:探针 `scale_degree_by_regime` —— 常规区间把收益放大 2 倍,X 变化 < 0.0003(齐次度 0);
  塌缩区间放大 2 倍,X 变成 2.0005 倍(齐次度 1)。在塌缩区间里它读的是「那几个分钟平均跳了多大」。
- **口径是先 EMA 再排序**。半衰期 20 的 EMA 里,一个 +2000 的塌缩日要过 20×log₂(2000/0.3) ≈ 250 个交易日才会衰减到常规量级以下。
  所以实际交易的信号 ≈ 「这只股票过去一年里塌缩日的带符号、按幅度加权的累计」,常规区间的尾部形状信息基本被淹没。
  (这是从公式推出来的预期,要在真实数据上量 —— 见 `07x_1_anatomy.md`。)

**价格网格本身能不能造出塌缩日**(探针 `tick_grid_regime_share`,0.01 元 tick 的几何随机游走):
日波动约 1.2% 时,2 元股 24% 的日子右侧塌缩,3 元股 0.5%,5 元以上 0;日波动约 0.6% 时,2 元股 92%、3 元股 66%、5 元股 4%、10 元以上 0。
所以纯粹由 tick 造成的塌缩只发生在 **3 元以下(或 5 元以下且极不活跃)** 的股票上;更高价位的股票要进塌缩区间,得靠别的机制
(封板、停牌前后、全天只有零星成交)。

**一个分钟的离群收益的杠杆**(探针 `single_minute_leverage`):常规区间里把第一个分钟换成 10 倍分钟波动的跳空,X 平均移动 +0.39
(无跳空时 X 的标准差是 0.107);20 倍 → +0.90;−10 倍 → −0.39。一阶近似 (g − 2.06σ)/(12 × 1.645σ) 给出 0.40 / 0.91,对得上。
如果 `Ret` 的第一个分钟带着隔夜跳空,常规区间里的 X 就在很大程度上是「带符号的跳空 ÷ 分钟波动」—— 这要在真实数据上核对。

## 4. 结构语法

结构语法(从里到外):

```
分钟收益 Ret
  → 日内分位数(q95 / q05)                    —— 阈值,各自既当「尾部的门槛」又当「归一化的分母」
  → 严格越过阈值的分钟(0/1 掩码)             —— 事件判定
  → 掩码内的均值(ES)                          —— 尾内幅度
  → ÷ (阈值 + 1e-6)                             —— 归一化;阈值为 0 时变成 ×10⁶
  → 右侧 − 左侧                                  —— 带符号的不对称
(口径)→ 因果 EMA,半衰期 20                    —— 唯一的时间结构;把稀疏的大数变成缓慢衰减的状态
```

和已经研究过的几条都不同:**没有日轴算子、没有成交额字段、没有逐元素乘法(门控)**。所以 F001 的「极值记忆」、
F002 的「成对协方差」、F104 的「截面掩码」这些问题在这里都不存在。这棵树特有的问题是:

1. 阈值兼做分母 → 阈值为 0 时的行为决定了截面两端是谁(`+1e-6` 是一个带量纲的常数)。
2. 输出是一个**混合分布**(常规 O(1) + 塌缩 O(10³~10⁵)),再喂给一个**线性**的 EMA → 排序由大数决定。
   「先排序再平滑」与「先平滑再排序」在这里不是小差别,而是两条不同的因子。
3. 右减左:两侧各自是不是都有预测力、符号相反?还是只有一侧有用、另一侧只是噪声/抵消项?
4. 只用到 `Ret`:第一个分钟的收益里有没有隔夜跳空,决定了常规区间读的是「日内尾部形状」还是「跳空」。

## 5. 竞争性假设

写于任何实验之前(手里只有 S0 基线、源码和探针)。每条写它预测什么、什么结果能杀死它。结论见 `09_diagnosis.md`。

| # | 假设 | 它预测什么 | 哪个实验能杀死它 |
|---|---|---|---|
| H1 | **塌缩日决定一切**:截面两端、乃至整个排序,由「分位数 = 0 → ×10⁶」的日子决定,尾部形状不起作用 | \|X\| 双峰(O(1) 与 O(10³+));EMA 后绝大多数股票的信号由塌缩日主导;只保留「哪一侧塌了」的指示量(不要幅度、不要 ES/VaR)就能复现多空夏普;把 1e-6 换成与收益同量级的常数(塌缩消失)之后与原式的 rank 相关很低、空头腿收益消失 | 去掉塌缩日(或把 ε 调大)之后与原式 rank 相关仍 > 0.8 且多空夏普不变 → H1 死 |
| H2 | **常规区间的尾部形状不对称才是信号**,塌缩只是噪声 | 只在常规日上计算的 X(塌缩日置空/置 0)rank IC 不低于原式;先截面排序再平滑(消掉量级)不伤表现 | 常规版 rank IC ≈ 0 或多空夏普塌掉 → H2 死 |
| H3 | **塌缩日 = 封板日**:上涨稀少且幅度大 = 早盘拉到涨停后封死(或一字板/T 字板);下跌稀少且幅度大 = 跌停板 | 信号空头端(X 最大)的股票,近期涨停日占比远高于全市场;多头端(X 最小)近期跌停日占比高;空头腿收益里有一大块来自「次日开盘买不进」的票(标签 NaN 记 0);把 `buyable=False` 的标签换上,空头腿明显变小 | 两端的涨跌停占比与全市场无差别;换标签后空头腿不变 → H3 死 |
| H4 | **塌缩日 = 低价/不活跃**:tick 相对价格太粗,或全天成交稀疏 → 是价格水平 / 换手率 / 成交额水平的另一种写法 | 塌缩日集中在 3 元以下或成交额最低的股票;信号的折叠量(到截面中位的距离)与 log 价格、换手率、「零收益分钟占比」的 rank 相关很高;对这些变量(及其折叠)中性化后空头腿消失 | 塌缩日在价格/成交额各档均匀分布 → H4 死。注意:S0 的秩空间线性 R² 只有 0.103,但两端都是塌缩日(非单调),线性中性化看不见,要用折叠量去量 |
| H5 | **常规区间读的是隔夜跳空**:如果 `Ret` 的第一个分钟是「开盘价 ÷ 昨收」,它几乎必然落在尾部,X ≈ 带符号的跳空 ÷ 分钟波动 | `day_first(Ret)` 与 开盘/昨收 高度相关且量级是其余分钟的数倍;去掉第一个分钟重算的 X 与原式(常规日)rank 相关明显 < 1;隔夜收益的 EMA 能解释常规区间的 X | `day_first(Ret)` 是 NaN 或量级与其他分钟相同;去掉第一分钟后 rank 相关 ≈ 1 → H5 死 |
| H6 | **钱在空头腿,是因为空头端是「彩票/打板」类股票**(近期涨停、次新、题材股),它们在可买入口径下次日起持续跑输;多头端是它的镜像(跌停/阴跌股),同样跑输 → 分位剖面是倒 U,没有「好的一端」 | 分位剖面两端都负(S0:训练 Q1 −28.4%、Q10 −5.3%,已经符合);把 X 折叠(取 −\|X\| 或只做「没有塌缩日」的那一端)多头腿转正但幅度小(只是「避开坏股票」);多头腿净超额的上限 ≈ 中间几档的平均超额(训练 +3%~+8%) | 存在某个单调变换使多头端十分位稳定为正且 > +10% → H6 的「没有好的一端」部分死 |
| H7 | **平滑在起主要作用,而且半衰期 20 是网格的边界解**:hl 0 → 20 多头腿净超额从 −67% 单调升到 −6.9%,衰减表 rank IC 随持有期上升(h1 0.0165 → h20 0.0338),说明它是一个慢状态变量 | 用显式的更长记忆(`cross_mean`/`cross_sum` 30、60 日,或「过去 N 日塌缩日计数」)替代 EMA-20,rank IC 与多空夏普不降;日换手再降 | 更长窗口使 rank IC 明显下降 → 记忆长度不是越长越好,H7 的「边界解」部分死 |
| H8 | **两侧不对等**:右侧(R)与左侧(L)不是同一个机制的镜像 —— 上涨稀少的塌缩(R 大)对应「阴跌/无人问津」或「封涨停」,下跌稀少(L 大)对应「封跌停」或「缓涨」,各自的后续收益方向未必相反 | 单独的 R 与单独的 L 各自的方向、分位剖面不同;「右减左」里可能有一侧是在抵消另一侧 | R 与 −L 的 rank IC 相同、剖面互为镜像 → H8 死 |
| H9 | **多余节点**:左支的 `abs_`、计数上的 `+1e-6`、`create_like(·,0)` 都不改变排序;真正有内容的只有「分位数作分母 + 1e-6」 | 把 ES/VaR 换成不除分位数的写法(如 ES − VaR、或尾部计数)会变成另一条因子;而去掉计数 ε 完全等价 | (读源码已基本确立,不单独花服务器轮次) |

**对只能做多的用户,事前判断**:这条因子公布的多头腿是负的(训练 −4.2% 毛、S0 净 −5.8%),空头腿 +26.3%。
如果 H3/H6 成立,它本质上是一个「该避开谁」的清单,不是一个「该买谁」的排序;升华的空间只有两条路:
(a) 把「避开」变成一个单调的多头排序(折叠、或只用「干净」的一端);(b) 承认它没有多头腿,结论写「对纯多头无用,相对已知家族无增量」。
两条路都要和 `cross_mean(day_std(Amt), 30)` / `cross_max(day_std(Amt), 9)` 比。

---

## 裁决(主研第 1 轮,2026-10-04)

依据:`S0_baseline`(`06_baseline.md`)与 tag `x1`(`07x_1_anatomy.md` A~G)。完整的证据与数字在 `state.md` §2、§4。

| # | 状态 | 一句话理由 |
|---|---|---|
| H1 | **被支持**(已确立) | 去掉塌缩日后多空夏普 +2.82/+3.24 → −1.45/−2.11;Pearson IC 0.0316 ≫ rank IC 0.0067 |
| H2 | **被否定**(已确立) | 常规版 rank IC 0.0036/**0.0006**,多头腿 −12.0%/−9.7%,比原式更差 |
| H3 | **被支持**(已确立) | 右侧塌缩 86.3% / 左侧 77.8% 是涨停收盘,基准率 1.59% → 富集 50 倍 |
| H4 | **被否定**(已确立) | 塌缩日里 <3 元占 0.2%、成交额后 20% 占 10%(随机 20%);折叠量对五个水平变量 R² 仅 0.068 |
| H5 | **被否定**(已确立) | 第一分钟 `Ret` 在 100% 的股票-日上恰好是 0;去掉它重算 rank 相关 0.999 |
| H6 | **被支持**(已确立) | 剖面两端都负(train −28.4% / −5.3%),两端都是近期封板股;连续构造的多头腿 train/valid 无一同时为正 |
| H7 | **已改写(方向反了)** | 事件效应只持续 ~20 天、40 天归零,EMA-20 却记约一年;标记类构造的多头最优半衰期是 hl 0~1 → **记忆太长,不是太短**。改写为 H11 |
| H8 | **被支持**(已确立) | 只留 L 的方向**也是** −,与 R 同向 → 「右减左」是两个同向读数互相抵消,不是镜像 |
| H9 | **被支持**(读源码确立) | 计数上的 ε 只在空集时起作用且结果仍为 0;要害只有「分位数作分母 + 1e-6」。不单独花服务器轮次 |

**新增的竞争性假设(主研第 1 轮提出,R1 来裁决)**

| # | 假设 | 它预测什么 | 哪个实验能杀死它 |
|---|---|---|---|
| H10 | **排除性增量**:F106 的封板标记(短记忆)对**已知家族的多头书**有增量 —— 这是 H6 之后唯一剩下的用途。它不是一本可交易的书,而是一张「不要持有谁」的清单 | 已知家族 `cross_mean(day_std(Amt),30)` 的多头十分位里**确实含有**被标记的票,而且这些票拖后腿;剔除它们之后多头腿净超额在 train 和 valid **同时**提高 ≥ 1 个点;`rank(known) − w·rank(F106)` 的和书优于纯已知家族 | 已知家族多头端几乎不含被标记票(占比 < 2%),或剔除后多头腿不变 / 变差 → H10 死,结论是彻底的否定 |
| H11 | **记忆长度错配**:显式的短记忆(近 10/20 日塌缩日计数、近 N 日涨停计数)优于 EMA-20(X) | 短记忆的 rank IC 与多头腿同时改善(事件效应 20 天内结束,x1 D) | 短记忆的 rank IC 和多头腿都不优于 EMA-20(X) → H11 死,EMA-20 的长记忆不是缺陷 |
| H12 | **它被更朴素的「近期涨停」完全替代**(最该杀的一条) | F106 信号对 `g_limitup30` / EMA20(涨停标记) 中性化后,残差的 rank IC 与多头腿增量都塌掉 —— 因为涨停日数量是塌缩涨停日的 4 倍多(62,438 对 14,680),而没塌缩的涨停日事后同样跑输(−69 bp),原式只抓到了「封得死」的五分之一 | 中性化后残差仍有可观的 rank IC 和多头腿增量 → H12 死,这棵树有独立增量。**H12 成立 = 对纯多头用户的结论是「没有独立增量,用涨停标记就够了」** |

---

## R1 的读法预登记(主研,2026-10-04,**在 x2 的数字回来之前写**)

R1 跑的 `x2_longonly.py` 会打出 **9 张标记 × 2 个已知家族 × 2 段 = 36 行**叠加结果。
18 个(标记, 家族)组合里「train 和 valid 同时变好」靠运气就会出现(playbook §4.6:多头腿净超额的噪声约 ±3 个点)。
所以把判据**事前**写死在这里,下一轮只许照着读,不许挑一行好看的讲故事。

### H10(排除性增量)—— 四条全部满足才算「被支持」

| | 条件 | 为什么 |
|---|---|---|
| (a) | 起作用的标记必须是**事前有动机的短记忆事件标记**:`blown day within 20d` 或 `limit-up close within 20d` | x1 D 量到的事件窗口就是约 20 天。`F106 signal decile 1` / `\|F106 signal\| >= 5` 只是 EMA-20 读数的换一种写法,`listed < 250d` 是新股过滤,都**不是**这棵树的功劳 |
| (b) | ΔLnet > 0 在 **train 和 valid**、**known30 和 known9** 四个格子上**全部**成立 | 单段单家族过不了 §4.6 的噪声 |
| (c) | 被标记票占已知家族多头十分位 **≥ 2%**,且被标记票的次日超额在两段都**差于**同十分位里没被标记的票 | 机制必须看得见,不能只有净值变好 |
| (d) | ΔLnet ≥ 1 个点在 train 和 valid 都成立,且四个格子的中位数 ≥ 1 个点 | 效应要在噪声之外 |

- (a) 不成立而 (b)(c)(d) 成立 → 写成「**合理但未坐实**」,当成一条**新的、另外的**假设,**不算 H10 被支持**。
- 只有 `listed < 250d` 赢 → 诚实的结论是「值钱的是排除新股,不是这条因子」(x1 C 已经量到:信号最低 1% 里 95.2% 是上市不满 250 日的新股)。
- **叠加行的 `LS` 和 `short` 由构造决定、不可读**:`push_down` 把被标记票压到当天所有票之下,等于把它们推进了**空头十分位** ——
  叠加之后的空头腿是「做空被标记的票」,不是已知家族的空头腿。只读 `Lnet / Lshp / Lgross / LTO`。
- 叠加**不重新拟合**方向和半衰期(脚本第 118 行 no refit),`Lnet` 已经扣了 15bp/边的费 → 标记开关造成的额外换手已经付过钱。
  所以 ΔLnet 就是可以直接读的数,`LTO` 前后对比只用来确认成本没有吃掉收益。

### H11(记忆长度错配)—— 只看 rank IC 和叠加,不看计数构造的多头腿

第 5 节里「近 10/20/40 日塌缩日计数 / 涨停计数」**绝大多数格子取值为 0**,而拟合方向是 −,
于是它们的**多头端 = 「计数 0」这一大片并列**,实际持有的 10% 是按股票代码顺序切出来的 ——
**和 state.md §8.3 里 0/1 标记那个「假的多头腿」是同一个毛病**,过不了 dist 门槛,不是一本可交易的书。
→ H11 的裁决只认两样:(1) 短记忆构造的 **rank IC** 在**两段**都优于 EMA-20(X)(交易信号 0.0165 / 0.0086,原始面板 0.0067 / 0.0027);
(2) 短记忆标记在第 2 节的叠加里更有用。第 5 节里只有 `log(1+|X|)`、`R+L`、`log(1+R+L)` 三行是连续的、多头腿可以当书读。

### H12(被朴素的「近期涨停」替代)—— 以**完整定义**的那一版为准

第 4 节的两个「近期涨停」控制变量**定义不一样**,强弱不同:

- `g_limitup30`(配置 `gates`,第 51 行)= 近 30 日里「收在当日最高价且涨幅 > 9.5%」的天数 → **只抓 ≥9.5% 的板**,漏掉 5% 的 ST 板。
- `lu20e` = EMA20(`x1.limit_flags(...)["up"]`)= 「在 5/10/20% band 内且收在当日极值」→ **完整定义**。

→ **H12 的主要证据看 `EMA20(limit-up close flag)` 和 `all four` 两行的残差**:
残差的 rank IC 掉到原信号的三分之一以下、且残差的多头腿没有增量 = H12 被支持。
只有 `g_limitup30` 一行塌掉的话,证据是弱的(它本来就是个不完整的涨停计数)。
R² 本身是**次要**的(playbook §6.5:秩空间线性中性化读不出折叠关系)—— 要配合第 4 节最后那几行
「折叠量对这几组控制变量的 R²」一起看,脚本算它就是为了这个。

---

## 裁决(主研第 2 轮,2026-10-04)—— 照「R1 的读法预登记」逐条对

依据:结果卡 `results/R1.md`、事实记录 `07x_2_longonly.md`,我自己对着 `logs/F106_erm_mag_gap_1m_x2.log`
(第 16~157 行)把下面用到的每个数字重新核对过一遍,与结果卡一致。

### H10(排除性增量)→ **被否定**(四条判据 (a)(b) 过、**(c)(d) 不过**)

只有事前有动机的那两张短记忆标记进入裁决(判据 (a)),它们在四个格子(train/valid × known30/known9)上的 ΔLnet:

| 标记 | known30 train | known30 valid | known9 train | known9 valid | (b) 四格全正 | (d) 两段都 ≥1 点 |
|---|---|---|---|---|---|---|
| `blown day within 20d` | **+1.59** | **+0.52** | **+1.60** | **+0.40** | ✅ | ❌(valid 只有 0.4~0.5) |
| `limit-up close within 20d` | +1.92 | +0.50 | +1.89 | **−0.04** | ❌ | ❌ |

- **(a) 过**:起作用的确实是 `blown day within 20d` / `limit-up close within 20d`,不是 `F106 signal decile 1`、`\|F106 signal\| >= 5` 这类
  「EMA-20 读数的换一种写法」(它们的 ΔLnet 更小:known30 valid +0.03、−0.44)。
- **(b)**:`blown day within 20d` 过(四格全正);`limit-up close within 20d` 不过(known9/valid −0.04)。
- **(c) 不过**:`blown day within 20d` 占已知家族多头十分位的比例 known30 0.051/0.022、known9 0.041/**0.016** ——
  known9/valid 那一格 1.6% **低于 2% 门槛**(全表 36 格里唯一低于 2% 的一格)。
  「机制看得见」这半条是过的:被标记票的次日超额在四个格子里全部远差于未标记票(−22.1% vs +17.4%、−4.1% vs +27.7%、
  −27.6% vs +19.4%、−7.6% vs +28.0%)。
- **(d) 不过**:ΔLnet 在 train 是 +1.59/+1.60(≥1 点),在 **valid 只有 +0.52/+0.40**,远低于 1 个点,
  而 playbook §4.6 给的多头腿净超额噪声是 **±3 个点**。四格中位数 1.06 勉强过,但「两段都 ≥1 点」这半条不过。

**→ H10 被否定。** 方向是对的、机制是看得见的,但**量级在噪声以下**,不构成一个可以推荐的候选。

**为什么它必然这么小(这一轮新算的量化机制,把四个格子都解释到 25% 以内)**:
叠加的收益 ≈(被标记票占多头十分位的比例)×(被标记票与未标记票的次日超额之差)。

| 格子 | share | 超额之差 | 乘积(预测) | 实测 ΔLnet |
|---|---|---|---|---|
| known30 / train | 0.051 | 17.4 −(−22.1) = 39.5 | **2.0** | +1.59 |
| known30 / valid | 0.022 | 27.7 −(−4.1) = 31.8 | **0.70** | +0.52 |
| known9 / train | 0.041 | 19.4 −(−27.6) = 47.0 | **1.93** | +1.60 |
| known9 / valid | 0.016 | 28.0 −(−7.6) = 35.6 | **0.57** | +0.40 |

valid 上两个因子同时变小(share 减半、超额之差从 ~40 收到 ~33)→ 增量掉到三分之一。
**而 share 之所以这么低,是因为已知家族本来就在躲这些票**:被标记票占全市场 0.080/0.067,
占已知家族多头十分位只有 0.051/0.022(known30)、0.041/0.016(known9)——
已知家族持有被标记票的频率只有全市场的 **24%~64%**(`limit-up close within 20d` 更极端:**15%~37%**)。
**「低 Amt 波动」这个条件已经把近期封板股筛掉了大半,F106 的清单和它要剔的票高度重叠 —— 这就是排除性增量的天花板。**

### H11(记忆长度错配)→ **被支持**,但它**不产生候选**

按预登记,H11 只看 rank IC 和叠加表现:

- **rank IC**:六行计数构造(塌缩/涨停 × 10/20/40 日)train +0.0288~+0.0433、valid +0.0260~+0.0417,
  对照 EMA-20(X) 的交易信号 **0.0165 / 0.0086** → train 上是 1.7~2.6 倍、**valid 上是 3.0~4.8 倍**,两段全部更优。✅
- **叠加**:20 日窗口在四个格子上全部优于 60 日窗口 ——
  塌缩标记 +1.59/+0.52/+1.60/+0.40 vs +0.94/+0.47/+1.32/+0.19;
  涨停标记 +1.92/+0.50/+1.89/−0.04 vs +1.50/+0.36/+0.82/−0.67。✅

**→ H11 被支持(已确立):EMA-20 把一个 10⁴ 的塌缩读数记约一年,而事件效应 20 天内结束 —— 记忆长了一个数量级,这是这棵树的结构性缺陷。**

**但修好记忆救不了它**:短记忆的优势只出现在**取值几乎全是 0 的计数构造**上(过不了 `dist ≥ 0.5`,多头端是并列按代码切的);
第 5 节三条**连续**取值、多头腿能当书读的构造(`log(1+\|X\|)`、`R+L`、`log(1+R+L)`)rank IC 只有
**+0.0076/+0.0010、+0.0137/+0.0109、+0.0137/+0.0109**,全部**低于或仅接近原式**,Lnet 没有一条两段同正。
→ H11 是一条**诊断结论**(说清了缺陷在哪),不是一条升华路线。

### H12(被朴素的「近期涨停」替代)→ **已改写**(字面版被否定,操作版被支持)

按预登记,主证据是 `EMA20(limit-up close flag)`(5/10/20% 完整定义)和 `all four` 两行的残差,
判据是「残差 rank IC 掉到原信号 1/3 以下 **且** 残差多头腿没有增量」。

| 中性化于 | 残差 rIC(train/valid) | 占原信号(0.0165/0.0086) | 残差 Lnet(train/valid) |
|---|---|---|---|
| `EMA20(limit-up close flag)` | +0.0091 / +0.0022 | 0.55× / 0.26× | −8.5% / −6.2% |
| `all four` | +0.0113 / +0.0068 | 0.68× / 0.79× | −6.3% / −4.1% |

- **字面版(「完全被替代」)被否定**:残差 rank IC 在 train 上保住了原信号的 55%~68%,没有掉到 1/3 以下。
  折叠量对 `all four` 的 R² 是 **0.444** —— 朴素的近期涨停变量解释了折叠信号的约四成四,**不是全部**。
  这棵树里确实有「封得死的那五分之一 + 跳了多大」这部分朴素标记拿不到的信息。
- **但这部分独立信息对纯多头一文不值**:五行残差的 Lnet 在 train 和 valid **全部仍为负**
  (train −5.8%~−8.6%、valid −3.4%~−7.0%),没有一行翻正。
- **操作版被支持**:在唯一还上得了台面的用途(排除性叠加)上,朴素涨停标记与 F106 自己的塌缩标记**打平** ——
  ΔLnet +1.92/+0.50/+1.89/−0.04 对 +1.59/+0.52/+1.60/+0.40,train 上朴素的更好,valid 上互有胜负、差距都在 0.5 点以内。
  → 对用户的那句话是:**「要这个排除效果,一个日线涨停标记就够了;而且这个效果本身在 valid 上只值半个点,在噪声里。」**

**→ H12 改写为:统计上没有被完全替代(残差 rank IC 和 56% 的折叠方差还在),但剩下的独立部分没有多头腿价值;
在排除性用途上朴素标记与它打平。**

### 顺带被 R1 坐实的两件事

- **和书这条路彻底死掉**:`rank(known) + w·rank(F106)`(两个方向 × w = 0.25/0.5/1 × 两个家族 × 两段)**24 行没有一行**
  Lnet 高于已知家族自己的基准,且**随 w 单调下降**(known30 valid:+22.3% → +18.7% → +16.5% → +13.4%)。
  → `v_sum` 候选排除。
- **反向中性化**:已知家族对(F106 信号 + 其折叠)中性化后,R² 只有 0.014/0.020,残差 Lnet +11.1%/+21.2%(known30,
  自身基准 +12.6%/+22.3%)—— 已知家族的钱几乎完全不在 F106 的方向上,而且剔掉 F106 的方向还略有损失。
  F106 信号对已知家族中性化,R² 0.002/0.004,残差 Lnet −6.4%/−3.0%(known30)、−7.5%/−4.3%(known9)
  → **两者近乎正交,但正交的那部分是负的 alpha。**

---

## 留出段之后的确认(主研,2026-10-04;**不升级任何假设的状态**)

规矩:读完留出段不新增「已确立」、不改推荐(playbook §6.4)。下面只记录「事前登记的判据在留出段上没有推翻哪条假设」,状态一律照上面第 2 轮的裁决不变。

| 假设 | 第 2 轮裁决(不变) | 留出段上对应的判据 | 结果 |
|---|---|---|---|
| H1 / H3 / H6 / H8(塌缩日=封板日决定一切、两端都是打板股、倒 U、两侧不对等) | 被支持 | 留出段**没有分位剖面**(`profile` 无 holdout 键)→ 倒 U 在留出段**无数据可看** | 没有被检验,也没有被推翻;照实写缺 |
| H2 / H4 / H5(常规区间尾部不对称是信号 / 塌缩日=低价股 / 读隔夜跳空) | 被否定 | 无直接判据(留出段只跑了 5 条候选) | 维持被否定 |
| 「原样对纯多头不可用」(H1 的操作后果) | — | **C1**:`f_orig` holdout Lnet −3.19% / Lshp −0.69 / Lgross −1.38%,逐年八年全负 | **没被推翻** |
| 「公布的多空夏普是真的但与多头腿无关」 | — | **C2**:holdout LS +3.108,与用户表 3.11 精确复现 | **没被推翻** |
| **H10**(排除性增量) | **被否定** | **C3**:holdout ΔLnet **+0.54 pp** < +1.5 pp 门槛(valid +0.57 pp);错配污染 ≲0.4 pp、符号不定(`09_diagnosis.md` B1) | 维持被否定 |
| **H11**(记忆长度错配) | **被支持,但不产生候选** | 无判据(计数构造过不了 dist,没有进 S_final) | 维持「被支持但不产生候选」 |
| **H12**(被朴素「近期涨停」替代) | **已改写**(字面版否定、操作版支持) | **C4**:朴素涨停叠加 **+0.75 pp** > F106 自己的 **+0.54 pp**(朴素反而高 0.21 pp) | 操作版维持被支持 |
| **H13**(真正值钱的是新股过滤器) | **合理但未坐实** | 无判据(没有进 S_final 候选) | 维持未坐实 → `12_next.md` 第 1 条 |

顺带:**C5**(已知家族 holdout +14.10% / 夏普 +1.51,落在用户区间内)和 **C6**(五条 cov 0.9675、dist ≥0.9933)都成立 —— 这两条不对应任何假设,是「参照系还在、门槛不是瓶颈」的前提条件。

## 6. 基线指标

**与用户表同口径**(方向、半衰期在用户训练段上定;多头口径在前,多空口径 = 用户最早那张表的口径)

| 结构 | 方向 | 半衰期(多头) | **多头腿净超额** 训练/测试 | 纯多头夏普 训练/测试 | 多头腿毛超额 训练/测试 | 多头日换手 | 半衰期(多空) | 扣费多空夏普 训练/测试 | 多头腿毛超额@多空半衰期 训练/测试 | 空头腿毛超额 训练/测试 |
|---|---|---|---|---|---|---|---|---|---|---|
| _用户表里公布的原式(多空口径)_ | − | — | — | — | — | — | 20 | +2.91 / +3.11 | -4.2% / -1.4% | — |
| `f_orig` `sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(...` | − | 20 | **-5.8% / -3.2%** | -1.91 / -0.69 | -4.2% / -1.4% | 2.2% | 20 | +2.91 / +3.11 | -4.2% / -1.4% | +26.3% / +24.7% |

**决策口径**(方向、半衰期在 train 上定;valid 是它没见过的)

| 变体 | 表达式 | 方向 | 半衰期(多头) | **多头腿净超额** train/valid | 纯多头夏普 train/valid | 多头腿毛超额 train/valid | 多头日换手 | 半衰期(多空) | 扣费多空夏普 train/valid | 空头腿毛超额 train | rank IC train/valid | cov / dist |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `v_base` | `sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)...` | − | 20 | **-6.9% / -3.2%** | -2.15 / -1.23 | -5.1% / -1.8% | 2.4% | 20 | +2.82 / +3.24 | +27.9% | +0.0067 / +0.0027 | 1.00 / 0.99 |

**半衰期扫描(fit 段)** — ◀多头 = 按纯多头夏普选中的,◁多空 = 按多空夏普选中的

| 半衰期 | 纯多头夏普 | 多头腿净超额 | 多头日换手 | 扣费多空夏普 | 多空日换手 |
|---|---|---|---|---|---|
| 0 | -19.51 | -67.2% | 87.7% | -25.67 | 87.0% |
| 1 | -13.61 | -45.5% | 55.1% | -8.18 | 49.1% |
| 2 | -9.93 | -32.5% | 36.7% | -1.90 | 28.8% |
| 3 | -8.16 | -25.8% | 27.2% | +0.09 | 18.2% |
| 5 | -5.82 | -18.5% | 17.1% | +1.07 | 10.2% |
| 10 | -3.26 | -10.6% | 7.2% | +2.29 | 4.9% |
| 20 ◀多头 ◁多空 | -2.15 | -6.9% | 2.4% | +2.82 | 2.3% |

**信号分位的次日超额**(相对当天有信号有标签的票的等权;十分位书默认「越强越好」,这张表检验它)

| 信号分位(1=最低) | 年化超额 train | 年化超额 valid |
|---|---|---|
| Q1 | -28.4% | -22.7% |
| Q2 | +0.1% | +3.5% |
| Q3 | +3.5% | +10.2% |
| Q4 | +2.0% | +2.6% |
| Q5 | +4.7% | +2.6% |
| Q6 | +6.6% | +5.4% |
| Q7 | +7.9% | +1.3% |
| Q8 | +5.9% | -1.2% |
| Q9 | +3.2% | +0.1% |
| Q10 | -5.3% | -1.8% |

**逐年**(实际交易的信号)

| 变体 | 指标 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 |
|---|---|---|---|---|---|---|---|
| `v_base` | 多头腿净超额 | -9.2% | -6.2% | -8.6% | -4.1% | -0.8% | -7.4% |
| | 扣费多空夏普 | +1.82 | +4.17 | +3.25 | +2.33 | +3.22 | +3.31 |

**不同预测期的 rank IC(fit 段)**

| 变体 | h=1 | h=2 | h=3 | h=5 | h=10 | h=20 |
|---|---|---|---|---|---|---|
| `v_base` | +0.0165 | +0.0201 | +0.0218 | +0.0247 | +0.0288 | +0.0338 |

**复现**:用户训练段(utrain)上 S0 给出方向 −、半衰期 20、扣费多空夏普 +2.91、多头腿毛超额 −4.2%,与公布的那一行(2.91 / −4.2%)一致。
两种口径选到的半衰期相同(多头口径 20、多空口径 20),所以这条因子**没有「换成多头最优半衰期」这条免费的改进** ——
「原式 + 多头最优半衰期」就是公布的那一行本身。

**多头腿(选拔口径)是负的,而且在每一个半衰期下都是负的**:

| 半衰期(train) | 0 | 2 | 5 | 10 | 20 |
|---|---|---|---|---|---|
| 多头腿净超额 | −67.2% | −32.5% | −18.5% | −10.6% | −6.9% |
| 纯多头夏普 | −19.51 | −9.93 | −5.82 | −3.26 | −2.15 |
| 多头日换手 | 88% | 37% | 17% | 7% | 2% |

决策口径下:多头腿净超额 train −6.9% / valid −3.2%,纯多头夏普 −2.15 / −1.23,多头腿**毛**超额也是负的(−5.1% / −1.8%)。
所以负的多头腿不是成本问题:把换手压到 2.4% 之后它仍然跑输等权。半衰期从 0 拉到 20 只是把亏损从「成本 + 选股」缩到「选股」。
半衰期 20 是网格的上边界,扫描在边界上仍在改善(−10.6% → −6.9%)—— 最优的记忆长度很可能在 20 以外。

**钱全在空头腿**:train 空头腿毛超额 +27.9%(valid +22.4%),多头腿毛超额 −5.1%(valid −1.8%);扣费多空夏普 +2.82 / +3.24 完全由空头腿撑起。

**分位剖面是倒 U,而且极不对称**(Q1 = 空头端 = X 的 EMA 最大的一档;Q10 = 多头端):

| | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 |
|---|---|---|---|---|---|---|---|---|---|---|
| train | −28.4% | +0.1% | +3.5% | +2.0% | +4.7% | +6.6% | +7.9% | +5.9% | +3.2% | −5.3% |
| valid | −22.7% | +3.5% | +10.2% | +2.6% | +2.6% | +5.4% | +1.3% | −1.2% | +0.1% | −1.8% |

一档(Q1)独自跑输 23~28 个点,其余九档里八档在 0~+10% 之间、多头端一档为负。这不是一个「信号越大越好」的排序:
它是「有一档很坏」。中间几档的正超额大体上只是「全市场均值扣掉那一档坏股票」之后的算术结果(九档平均 ≈ +3%)。

**Pearson IC 远大于 rank IC**:原始日频面板 train 的 Pearson IC 0.0316(ICIR 0.59),rank IC 只有 0.0067。预测力在取值的**量级**里
(也就是那些 10³ 以上的塌缩值),不在排序的中段 —— 与 `03_decomposition.md` 里「两端由塌缩日决定」的推断一致。
平滑之后实际交易信号的 rank IC 是 0.0165 / 0.0086(train / valid)。

**逐年**(utrain 内,多空口径):2018 +1.82、2019 +4.17、2020 +3.25、2021 +2.33、2022 +3.22、2023 +3.31,年年为正;
多头腿净超额年年为负(−9.2%、−6.2%、−8.6%、−4.1%、−0.8%、−7.4%)。

**衰减**:rank IC 随持有期上升(h1 0.0165 → h5 0.0247 → h20 0.0338)。信号是一个慢变量:今天排在空头端的股票,二十天后还在跑输。

**条件 IC**:按成交额分桶,IC 随成交额上升(0.0039 → 0.0330);按市值分桶,小市值里更高(0.0214 → 0.0082)。
即「成交活跃的小票」里最有效 —— 与「空头端是被炒作的票」的读法相容,但这两个分桶变量与因子本身的关系要另量(`07x_1_anatomy.md`)。

**门槛**:cov 1.00、dist 0.99,两道都过。

## 7. 消融实验

### S0_baseline

**问题**: Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?

| 变体 | 表达式 | 方向 | 半衰期(多头) | **多头腿净超额** train/valid | 纯多头夏普 train/valid | 多头腿毛超额 train/valid | 多头日换手 | 半衰期(多空) | 扣费多空夏普 train/valid | 空头腿毛超额 train | rank IC train/valid | cov / dist |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `v_base` | `sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)...` | − | 20 | **-6.9% / -3.2%** | -2.15 / -1.23 | -5.1% / -1.8% | 2.4% | 20 | +2.82 / +3.24 | +27.9% | +0.0067 / +0.0027 | 1.00 / 0.99 |

<details><summary>每个变体为什么存在</summary>

- `v_base` — 原始表达式

</details>

# 07_S0_baseline — S0_baseline 阶段事实记录(工单 R3 补写)

来源:`runs/F106_erm_mag_gap_1m/S0_baseline.json`(10-04 11:50,exit 0,220.0s,splits `['train','valid','utrain']`,只有 1 个变体 `v_base`)。
本文件只记事实,**不下结论**(解读见 `09_diagnosis.md` A2)。`S0_baseline` 不是 final 阶段,没有触发留出段读取,JSON 里没有 `holdout` 字段 —— 这是预期行为,不是遗漏。

## 问题(配置里 S0_baseline 阶段的 question)

> Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?

## 1. v_base 两套书

### 1a. 决策口径(`books`;方向/半衰期在 train 上拟合;报 train / valid)

| sgn | hlL | Lnet tr | Lnet va | Lshp tr | Lshp va | Lgross tr | Lgross va | LTO | hlS | LS tr | LS va | short tr |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| − | 20 | −6.9% | −3.2% | −2.15 | −1.23 | −5.1% | −1.8% | 2.4% | 20 | +2.82 | +3.24 | +27.9% |

固定半衰期扫描(train,`books.sweep`):

| hl | Lnet | Lshp | LTO |
|---|---|---|---|
| 0 | −67.2% | −19.51 | 88% |
| 2 | −32.5% | −9.93 | 37% |
| 5 | −18.5% | −5.82 | 17% |
| 10 | −10.6% | −3.26 | 7% |
| 20 | −6.9% | −2.15 | 2% |

### 1b. 用户口径(`books_user`;方向/半衰期在 utrain 上拟合;报 utrain / holdout——holdout 本阶段未算)

| sgn | hlL | Lnet utr | Lnet ho | Lshp utr | Lshp ho | Lgross utr | Lgross ho | LTO | hlS | LS utr | LS ho | short utr |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| − | 20 | −5.8% | **—(未算)** | −1.91 | **—** | −4.2% | **—** | 2.2% | 20 | +2.91 | **—** | +26.3% |

## 2. cov / dist

rIC(原始日频面板):train +0.0067、valid +0.0027。rICtraded(平滑后交易信号):train +0.0165、valid +0.0086。
**cov = 1.00、dist = 0.99**(两道门槛都过;这里的 cov 是 train/valid 范围内的面板覆盖率,数值上与 `S_final` 的 holdout cov 0.9675 不同,
是因为统计的 split 不同,不是矛盾,见 `08_variants.md` §2)。

## 3. 分位超额 Q1..Q10(Q10 = 多头端)

| split | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 |
|---|---|---|---|---|---|---|---|---|---|---|
| train | −28.4% | +0.1% | +3.5% | +2.0% | +4.7% | +6.6% | +7.9% | +5.9% | +3.2% | −5.3% |
| valid | −22.7% | +3.5% | +10.2% | +2.6% | +2.6% | +5.4% | +1.3% | −1.2% | +0.1% | −1.8% |

倒 U,两端(Q1、Q10)都明显弱于中段。

## 4. 逐年(`by_year`,utrain 范围内,2018–2023;本阶段非 final,没有 2024/2025)

| | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 |
|---|---|---|---|---|---|---|
| Lnet | −9.2% | −6.2% | −8.6% | −4.1% | −0.8% | −7.4% |
| LS | +1.82 | +4.17 | +3.25 | +2.33 | +3.22 | +3.31 |

六年 Lnet 全负。

## 5. 核对:`S0_baseline/v_base` 与 `S_final/f_orig` 是不是同一本书

**是**。两处是同一个表达式在两次运行里各算一次,train/valid 的全部数字(1a 表、固定半衰期扫描、分位剖面、逐年 2018–2023)**逐项相同**
(对照 `07_S_final.md` §2a/§3a/§6/§7 的 f_orig 行),cov/dist 在 train/valid 范围内也相同(1.00/0.99)。
`S0_baseline` 的 utrain 行(Lnet +… / Lshp … / LS +2.91 / short +26.3%)与 `S_final` 的 f_orig utrain 行逐项相同。
没有发现不一致。

## 解读

原样对纯多头用户不可用,且不是成本问题(半衰期网格 {0,2,5,10,20} 上每一点毛/净全负)。判断全文见 `09_diagnosis.md` A2。

## 原始输出在哪

- `./scripts/study.sh digest F106_erm_mag_gap_1m S0_baseline`
- `runs/F106_erm_mag_gap_1m/S0_baseline.json`
- （该阶段还有中性化、已知家族自比较、条件 IC、衰减等输出,工单未要求逐项抄录,`digest` 命令可查全文,未在本文件重复。）

### S_final

**问题**: 读留出段之前写死的结论(原式多头腿全负 / 排除性增量在噪声以下 / 和已知家族相加更差)在用户的测试段(20230808–20251231)上成不成立?

| 变体 | 表达式 | 方向 | 半衰期(多头) | **多头腿净超额** train/valid | 纯多头夏普 train/valid | 多头腿毛超额 train/valid | 多头日换手 | 半衰期(多空) | 扣费多空夏普 train/valid | 空头腿毛超额 train | rank IC train/valid | cov / dist |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `f_orig` | `sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)...` | − | 20 | **-6.9% / -3.2%** | -2.15 / -1.23 | -5.1% / -1.8% | 2.4% | 20 | +2.82 / +3.24 | +27.9% | +0.0067 / +0.0027 | 1.00 / 0.99 |
| `f_known30` | `cross_mean(day_std(Amt), 30)` | − | 0 | **+12.6% / +22.3%** | +1.78 / +3.46 | +15.2% / +24.4% | 3.4% | 0 | +1.87 / +3.70 | +21.1% | +0.0343 / +0.0565 | 1.00 / 1.00 |
| `f_known30r` | `cs_rank(cross_mean(day_std(Amt), 30))` | − | 0 | **+12.6% / +22.3%** | +1.78 / +3.46 | +15.2% / +24.4% | 3.4% | 0 | +1.87 / +3.70 | +21.1% | +0.0343 / +0.0565 | 1.00 / 1.00 |
| `f_excl_blown15` | `add(cs_rank(cross_mean(day_std(Amt), 30)), mul(cross_max(mul(greate...` | − | 0 | **+14.3% / +22.9%** | +2.05 / +3.57 | +16.9% / +25.1% | 3.5% | 0 | +3.39 / +4.78 | +36.6% | +0.0407 / +0.0594 | 1.00 / 1.00 |
| `f_excl_lu15` | `add(cs_rank(cross_mean(day_std(Amt), 30)), mul(cross_max(mul(sub(cr...` | − | 1 | **+15.2% / +23.5%** | +2.16 / +3.64 | +17.4% / +25.4% | 2.9% | 0 | +2.91 / +4.74 | +40.2% | +0.0459 / +0.0630 | 1.00 / 1.00 |

<details><summary>同一半衰期下的多头腿(fit 段)—— 比结构之前先看这张</summary>

| 变体 | hl 0: 多头净超额 / 纯多头夏普 / 换手 | hl 2: 多头净超额 / 纯多头夏普 / 换手 | hl 5: 多头净超额 / 纯多头夏普 / 换手 | hl 10: 多头净超额 / 纯多头夏普 / 换手 | hl 20: 多头净超额 / 纯多头夏普 / 换手 |
|---|---|---|---|---|---|
| `f_orig` | -67.2% / -19.51 / 87.7% | -32.5% / -9.93 / 36.7% | -18.5% / -5.82 / 17.1% | -10.6% / -3.26 / 7.2% | -6.9% / -2.15 / 2.4% |
| `f_known30` | +12.6% / +1.78 / 3.4% | +11.6% / +1.65 / 2.6% | +11.0% / +1.57 / 2.1% | +9.8% / +1.40 / 1.8% | +8.4% / +1.21 / 1.4% |
| `f_known30r` | +12.6% / +1.78 / 3.4% | +11.6% / +1.64 / 2.6% | +10.9% / +1.55 / 2.1% | +9.5% / +1.36 / 1.8% | +7.8% / +1.14 / 1.4% |
| `f_excl_blown15` | +14.3% / +2.05 / 3.5% | +13.5% / +1.98 / 2.6% | +13.2% / +1.97 / 2.2% | +13.1% / +1.97 / 1.8% | +12.0% / +1.81 / 1.4% |
| `f_excl_lu15` | +14.7% / +2.08 / 3.4% | +14.9% / +2.13 / 2.6% | +14.8% / +2.12 / 2.2% | +14.2% / +2.01 / 1.8% | +12.4% / +1.77 / 1.5% |

</details>

<details><summary>每个变体为什么存在</summary>

- `f_orig` — 规则要求必含原式。C1/C2:留出段上它的多头腿是不是还是负的 —— 这是整份报告的中心结论。预期:Lnet < 0、Lshp < 0、LS > 0
- `f_known30` — 规则要求必含一条已知家族基准,也是第一推荐。C5:用户给的参考是测试段多头腿 +13%~+15%、纯多头夏普 1.4~1.9,留出段要确认
- `f_known30r` — 两条叠加候选的同构基准(它们外层带 cs_rank)。hl 0 下它与 f_known30 应当是同一本书 —— 如果不是,说明 cs_rank 的语义和理解的不同,在结果卡里特别写出来
- `f_excl_blown15` — C3:F106 自己的事件(近 15 日塌缩日)把被标记票推出已知家族多头腿,有没有真增量。cs_rank 取值在 [0,1],加 2.0 保证被标记票排在当天所有未标记票之后(sign = −1 → 它们落到最空头端 = 被剔出多头腿)
- `f_excl_lu15` — C4:同一个叠加,标记换成朴素日线涨停。H12 的操作版:要这个排除效果,一个日线涨停标记够不够

</details>

# 07_S_final — S_final 阶段事实记录(留出段;工单 R2)

来源:`runs/F106_erm_mag_gap_1m/S_final.json`(10-04 15:35,exit 0,310.3s,135KB,5 变体全部求值成功,`errors` 为空)。
本文件只记事实与异常,**不下结论**(C1~C6 的裁决在 `state.md` §2.2,由主研写)。

## 问题(配置里 S_final 阶段的 question)

> 读留出段之前写死的结论(原式多头腿全负 / 排除性增量在噪声以下 / 和已知家族相加更差)在用户的测试段(20230808–20251231)上成不成立?

`split_dates`:train `20180102–20211231`;valid `20220104–20230807`;utrain `20180102–20230807`;**holdout `20230808–20251231`(581 个交易日)**;full `20180102–20251231`(1942 天)。

## 0. 本轮做了什么(服务器运行次数)

**本轮服务器运行 = 0 次。** S_final 已经在更早的一轮跑完(exit 0);`runs/F106_erm_mag_gap_1m/ledger.json` 的 `summary.holdout = {reads: 1, expressions: 5}` —— 留出段唯一一次读取已经用掉。本轮只做了:
- `./scripts/study.sh digest F106_erm_mag_gap_1m S_final` 重看;
- 直接用 `python3` 读 `S_final.json` 核对字段级细节(重看已有结果不算再读留出段;本轮没有新增任何 `check` / `final` / `run` / `exec` 调用)。

## 1. 用的是主版,不是兜底版

逐项核对 JSON 里 5 个变体的 `expr` 字段:两条叠加候选(`f_excl_blown15`、`f_excl_lu15`)用的都是工单正文里的 `cs_rank(cross_mean(day_std(Amt), 30))` 主版,不是兜底的乘法推挤版(`mul(..., 999.0)`)。
`f_known30`(`cross_mean(day_std(Amt),30)`)与 `f_known30r`(`cs_rank(...)`)在 train 段(hl 都是 0)的书**逐项相同**(Lnet/Lshp/Lgross/LTO/LS/short 全部一致,见下表),rank 相关(train,交易信号)= 0.999999999988 ≈ **1.000**。→ `cs_rank` 的语义与工单预期一致,没有触发 DT/ND 不兼容的兜底分支。

## 2. 五条候选主表

### 2a. 决策口径(`books`;方向/半衰期在 **train** 上拟合;只报 train / valid)

| id | group | hlL | Lnet tr | Lnet va | Lshp tr | Lshp va | Lgross tr | Lgross va | LTO | hlS | LS tr | LS va | short tr |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| f_orig | baseline | 20 | −6.9% | −3.2% | −2.15 | −1.23 | −5.1% | −1.8% | 2.4% | 20 | +2.82 | +3.24 | +27.9% |
| f_known30 | known | 0 | +12.6% | +22.3% | +1.78 | +3.46 | +15.2% | +24.4% | 3.4% | 0 | +1.87 | +3.70 | +21.1% |
| f_known30r | known | 0 | +12.6%(与上行逐项相同) | +22.3% | +1.78 | +3.46 | +15.2% | +24.4% | 3.4% | 0 | +1.87 | +3.70 | +21.1% |
| f_excl_blown15 | overlay | 0 | +14.3% | +22.9% | +2.05 | +3.57 | +16.9% | +25.1% | 3.5% | 0 | +3.39 | +4.78 | +36.6% |
| f_excl_lu15 | overlay | 1 | +15.2% | +23.5% | +2.16 | +3.64 | +17.4% | +25.4% | 2.9% | 0 | +2.91 | +4.74 | +40.2% |

### 2b. 用户口径(`books_user`;方向/半衰期在 **utrain**(=用户训练段)上拟合;报 utrain / **holdout**)

| id | group | hlL | Lnet utr | **Lnet ho** | Lshp utr | **Lshp ho** | Lgross utr | **Lgross ho** | LTO utr | LTO ho | hlS | LS utr | **LS ho** | short utr | short ho |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| f_orig | baseline | 20 | −5.82% | **−3.19%** | −1.91 | **−0.69** | −4.16% | **−1.38%** | 2.19% | 2.40% | 20 | +2.91 | **+3.11** | 26.29% | 24.68% |
| f_known30 | known | 0 | +15.40% | **+14.10%** | +2.22 | **+1.51** | +17.81% | **+16.24%** | 3.19% | 2.83% | 0 | +2.33 | **+1.94** | 24.73% | 24.93% |
| f_known30r | known | 0 | +15.40%(与上行逐项相同) | **+14.10%** | +2.22 | **+1.51** | +17.81% | **+16.24%** | 3.19% | 2.83% | 0 | +2.33 | **+1.94** | 24.73% | 24.93% |
| f_excl_blown15 | overlay | 1 | +16.71% | **+14.64%** | +2.47 | **+1.57** | +18.81% | **+16.57%** | 2.78% | 2.55% | 0 | +3.73 | **+3.29** | 35.94% | 37.60% |
| f_excl_lu15 | overlay | 1 | +17.58% | **+14.85%** | +2.55 | **+1.60** | +19.67% | **+16.74%** | 2.75% | 2.49% | 0 | +2.94 | **+3.52** | 33.28% | 47.26% |

`books` 没有 `holdout` 字段,所以 holdout 一律只能来自 `books_user`(= 用户口径,方向/半衰期在 utrain 上定)。

### 2c. sign / dist / cov

| id | sign | sign_user | dist(`distinct`) |
|---|---|---|---|
| f_orig | −1 | −1 | 0.9933 |
| f_known30 / f_known30r / f_excl_blown15 / f_excl_lu15 | −1 | −1 | 1.0000 |

**cov 是结构性的、不随变体变化**:`ic_holdout['coverage']` 对 5 个变体全部等于 **0.9675**(≥0.95,C6 的 holdout 这一半全过)。
顺带发现(§9 展开):同一统计量在不同 split 下不同 —— train 0.6911、valid 0.8947、utrain(`ic_user.coverage`)0.7489、holdout 0.9675 —— 5 个变体完全一致,说明这是面板覆盖率(随日历时间单调上升,可能反映上市股票数随时间增加),不是任何表达式自身的求值失败。

## 3. 固定半衰期扫描(`sweep`)—— 只在各自的拟合段上算,**没有 valid / holdout 的网格**

`books['sweep']` 只在 **train**(books 的拟合段)上扫描;`books_user['sweep']` 只在 **utrain**(books_user 的拟合段)上扫描。valid 和 holdout **没有独立的 hl 网格**,各自只有「拟合段选出的那一个 hl」对应的单点,即上面 2a/2b 表里已经给出的数字。

### 3a. `books.sweep`(train,hl → (Lnet%, Lshp))

| id | hl0 | hl1 | hl2 | hl5 | hl10 | hl20 |
|---|---|---|---|---|---|---|
| f_orig | −67.22%, −19.51 | −45.47%, −13.61 | −32.46%, −9.93 | −18.46%, −5.82 | −10.57%, −3.26 | −6.91%, −2.15 |
| f_known30 | +12.62%, +1.78 | +12.21%, +1.72 | +11.62%, +1.65 | +11.04%, +1.57 | +9.81%, +1.40 | +8.39%, +1.21 |
| f_known30r | +12.62%, +1.78 | +12.17%, +1.72 | +11.59%, +1.64 | +10.88%, +1.55 | +9.55%, +1.36 | +7.83%, +1.14 |
| f_excl_blown15 | +14.25%, +2.05 | +14.13%, +2.05 | +13.51%, +1.98 | +13.23%, +1.97 | +13.12%, +1.97 | +11.95%, +1.81 |
| f_excl_lu15 | +14.68%, +2.08 | +15.18%, +2.16 | +14.92%, +2.13 | +14.85%, +2.12 | +14.16%, +2.01 | +12.43%, +1.77 |

### 3b. `books_user.sweep`(utrain,hl → (Lnet%, Lshp))

| id | hl0 | hl1 | hl2 | hl5 | hl10 | hl20 |
|---|---|---|---|---|---|---|
| f_orig | −66.50%, −19.41 | −44.67%, −13.59 | −31.49%, −9.81 | −17.49%, −5.56 | −10.02%, −3.16 | −5.82%, −1.91 |
| f_known30 | +15.40%, +2.22 | +15.06%, +2.17 | +14.54%, +2.10 | +14.01%, +2.02 | +13.03%, +1.88 | +11.73%, +1.72 |
| f_known30r | +15.40%, +2.22 | +15.00%, +2.16 | +14.48%, +2.09 | +13.89%, +2.01 | +12.92%, +1.87 | +11.32%, +1.66 |
| f_excl_blown15 | +16.73%, +2.46 | +16.71%, +2.47 | +16.23%, +2.40 | +16.07%, +2.40 | +15.98%, +2.40 | +14.83%, +2.25 |
| f_excl_lu15 | +17.12%, +2.48 | +17.58%, +2.55 | +17.44%, +2.53 | +17.37%, +2.53 | +16.76%, +2.42 | +14.94%, +2.17 |

(加粗/斜体省略;hl0 行就是「同一半衰期下比」预登记想要的行,但只在 train / utrain 上存在,**holdout 没有这一行**。)

## 4. C3 / C4(排除性增量 ΔLnet)—— 因为 holdout 没有 hl 网格,降级后的读法

两种口径都给:(a) 各自引擎拟合到的半衰期(即 2a/2b 表的数字,不同口径 hl 可能不同);(b) train/valid 恰好都在 hl=0 时的「同半衰期」对照(仅 C3 在 train/valid 上成立,因为 `f_excl_blown15` 的 train 拟合 hl 正好也是 0)。

| split | 口径 | f_known30r(hl) | f_excl_blown15(hl) | **C3 = Δ** | f_excl_lu15(hl) | **C4 = Δ** | 这一行是否同一半衰期 |
|---|---|---|---|---|---|---|---|
| train | books(own hl) | 12.62%(0) | 14.25%(0) | **+1.63 pp** | 15.18%(1) | **+2.56 pp** | C3 同 hl(干净);C4 不同 hl |
| valid | books(own hl) | 22.33%(0) | 22.89%(0) | **+0.57 pp** | 23.55%(1) | **+1.22 pp** | C3 同 hl(干净);C4 不同 hl |
| utrain | books_user(own hl) | 15.40%(0) | 16.71%(1) | **+1.30 pp** | 17.58%(1) | **+2.18 pp** | 两条都不同 hl(上界) |
| **holdout** | books_user(own hl) | **14.10%**(0) | **14.64%**(1) | **+0.54 pp** | **14.85%**(1) | **+0.75 pp** | 两条都不同 hl(上界) |

- **holdout 的 C3/C4 都是「引擎各自拟合半衰期」下算的上界**,含一点平滑的功劳,不是严格同一半衰期的对照。
- 巧合:C3 在 train/valid 上恰好是同一半衰期(两边都是 hl0)的干净对照,因为 `f_excl_blown15` 在 train 上拟合出的 hl 正好也是 0;但到 utrain/holdout,`f_excl_blown15` 拟合出的 hl 变成 1,C3 也变成了上界。C4 在全部四段里 `f_excl_lu15` 的 hl 都是 1、`f_known30r` 都是 0,所以 C4 在任何一段都不是同一半衰期的对照。
- **不要**把 §3 的 `books_user.sweep` hl0 行(utrain 的网格)当成 holdout 的固定半衰期表来读 —— 那是拟合段的数,不是 holdout 的数。

## 5. f_orig 与用户公布行对照

用户表 test 列:多空夏普 **3.11**;多头腿**毛**超额 **−1.4%**。

| | LS | Lgross | Lnet | Lshp | 口径 |
|---|---|---|---|---|---|
| 用户表(公布) | 3.11 | −1.4% | — | — | — |
| 本次 holdout 实测(`books_user`,方向/半衰期在 utrain 拟合,hlL=hlS=20) | **+3.108** | **−1.38%** | −3.19% | −0.69 | 与用户口径一致 |

两项都在小数点第二位内精确复现。注意:这一行只能来自 `books_user`(用户口径),`books`(train 拟合)字典本身没有 holdout 字段可比。

## 6. 分位剖面 Q1~Q10 —— **holdout 缺**,只有 train / valid

`profile` 字段里只有 `train`、`valid` 两个键,**没有 `holdout`、没有 `utrain`**(工单要的「holdout 分位剖面」这一项,引擎没有算,不能靠重跑补,因为重跑就是第二次读留出段)。另外 `f_known30r`、`f_excl_lu15` 这两个变体**连 `profile` 这个键本身都不存在**(不是空字典,是没有这个字段)。

| id | split | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10(多头端) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| f_orig | train | −28.4% | +0.1% | +3.5% | +2.0% | +4.7% | +6.6% | +7.9% | +5.9% | +3.2% | −5.3% |
| f_orig | valid | −22.7% | +3.5% | +10.2% | +2.6% | +2.6% | +5.4% | +1.3% | −1.2% | +0.1% | −1.8% |
| f_known30 | train | −21.4% | −13.2% | −7.8% | −2.6% | +0.1% | +3.7% | +5.5% | +8.6% | +11.4% | +15.8% |
| f_known30 | valid | −34.1% | −24.0% | −13.3% | −5.1% | +0.5% | +3.7% | +9.6% | +15.1% | +21.0% | +26.6% |
| f_excl_blown15 | train | −37.4% | −16.0% | −3.2% | −1.8% | +3.8% | +6.1% | +7.1% | +10.9% | +13.3% | +17.4% |
| f_excl_blown15 | valid | −39.9% | −22.0% | −14.5% | −5.5% | +1.9% | +5.4% | +9.7% | +16.2% | +21.6% | +27.2% |
| f_known30r | train/valid | **无此字段** | | | | | | | | | |
| f_excl_lu15 | train/valid | **无此字段** | | | | | | | | | |

f_orig 的倒 U 在 train/valid 都还在(两端 Q1 和 Q10 都明显弱于中段);holdout 是否仍然倒 U **没有数据可看**。

## 7. 逐年(`diagnostics.by_year`,2018→2025,多头口径 Lnet / LS)

`by_year_scope` = `20180102–20251231`(覆盖全部 8 年,不分 train/valid/holdout)。**holdout 从 20230808 开始,2023 这一列跨了 valid/holdout 分界,holdout 里干净的整年只有 2024 和 2025。**

| id | 2018 | 2019 | 2020 | 2021 | 2022 | 2023(混合年) | **2024(holdout)** | **2025(holdout)** |
|---|---|---|---|---|---|---|---|---|
| f_orig Lnet | −9.17% | −6.17% | −8.63% | −4.12% | −0.77% | −6.68% | **−5.13%** | **−0.43%** |
| f_orig LS | +1.82 | +4.17 | +3.25 | +2.33 | +3.22 | +1.99 | **+3.70** | **+3.37** |
| f_known30 Lnet | +17.3% | +10.2% | +6.6% | +16.0% | +24.6% | +21.2% | **+9.2%** | **+14.3%** |
| f_known30 LS | +3.01 | +1.84 | +0.66 | +2.18 | +4.22 | +3.75 | **+1.45** | **+1.60** |

八年里 f_orig 的 Lnet 全部为负(含两个 holdout 干净年);f_known30 的 Lnet 全部为正(含两个 holdout 干净年)。

**精度提示(不确定项,原样写出不强行判定)**:JSON 里没有字段标注 `by_year` 到底是按 `books`(train 拟合半衰期)还是 `books_user`(utrain 拟合半衰期)算的;阶段元信息里 `fit=train`,`rank_corr_on` 的说明文字是「smoothed at the fitted half-life」(单数),倾向于是 `books` 口径,但数字上没能排除另一种可能 —— `f_excl_blown15` 是唯一两套 hl 不同的变体(books hl0 / books_user hl1),它 2018–2021 均值 ≈14.0%,正好落在 hl0(train 14.25%)和 hl1(train 14.13%,相距很近)之间,这条变体也没法把两种假设区分开。**不影响本表的事实读数,只是不确定这张表背后具体是哪一套 hl。**

## 8. rank 相关(`diagnostics.rank_corr_train`,**train 段**,`rank_corr_on` = "traded signals (sign x panel, smoothed at the fitted half-life); controls raw")

| pair | rank corr(train) |
|---|---|
| f_orig ↔ f_known30 | **+0.0055**(几乎正交) |
| f_excl_blown15 ↔ f_known30r | **+0.923** |
| f_excl_lu15 ↔ f_excl_blown15 | **+0.893**(两张标记抓到的票高度重叠,但不是同一批) |
| (附)f_known30 ↔ f_known30r | +0.999999999988 ≈ 1.000(§1 已用于确认同一本书) |

## 9. 异常与注意事项汇总

- 没有求值失败、没有 NaN 异常;5 个变体 `errors` 字段均为空。
- `sign` 与 `sign_user` 对全部 5 个变体都是 **−1**,包括 `f_known30r` —— 不存在「叠加候选被反着读」的风险。
- `cov`(= `ic_holdout.coverage`)5 个变体全部是 0.9675,`dist` 全部 ≥0.9933 —— **C6 全过,没有一条卡在门槛上**。
- `cov` 这个数在 train(0.691)/valid(0.895)/utrain(0.749)/holdout(0.967)之间差异很大,但 5 个变体完全相同 —— 判断是面板覆盖率随日历时间变化的结构性统计量,不是任何表达式求值失败,详见 §2c。
- `f_known30` 与 `f_known30r` 在 hl0 下逐项相同、rank 相关 1.000 —— 符合工单预期,**不是异常**,但工单明确要求「如果不是同一本书要特别写出来」,所以这里确认「是」。
- §7 的「by_year 用哪套 hl」有一点不确定性,已在上面写明,不强行判定。
- 本文件、`results/R2.md` 之外没有对 `configs/F106_erm_mag_gap_1m.yaml`、`studies/` 下已有脚本做任何修改。

## 10. 原始输出在哪

- `./scripts/study.sh digest F106_erm_mag_gap_1m S_final`
- `runs/F106_erm_mag_gap_1m/S_final.json`(135KB)、`runs/F106_erm_mag_gap_1m/ledger.json`
- `logs/F106_erm_mag_gap_1m_S_final.log`(1475 字节,运行摘要)

### 中性化(fit 段)

> 被中性化的是**实际交易的信号**(方向 × 面板、按选定的半衰期平滑),对控制变量做秩空间逐日截面回归;残差不再平滑,直接建书 —— 所以残差的换手更高,**扣费夏普塌掉可能只是成本**;alpha 还在不在看 rank IC 与无成本夏普。R² 是控制变量张成的部分。

| 变体 | 对谁中性化 | 截面 R² | rank IC | 多头腿毛超额 | 多头腿净超额 | 空头腿毛超额 | 无成本多空夏普 | 扣费多空夏普 | 多空日换手 |
|---|---|---|---|---|---|---|---|---|---|
| `v_base` | _(未中性化的交易信号)_ | — | +0.0165 | -5.1% | -6.9% | +27.9% | +3.32 | +2.82 | 2.3% |
| `v_base` | all_controls | 0.103(原始日频面板上 0.047) | +0.0104 | -3.6% | -9.7% | +14.4% | +2.36 | -1.06 | 10.1% |
| `v_base` | ctl_amt | 0.003 | +0.0175 | -4.4% | -7.6% | +27.8% | +3.23 | +2.42 | 3.9% |
| `v_base` | ctl_price | 0.022 | +0.0180 | -3.2% | -6.0% | +29.8% | +3.44 | +2.85 | 3.0% |
| `v_base` | ctl_ivol | 0.011 | +0.0134 | -4.0% | -10.4% | +25.7% | +3.48 | +1.27 | 9.1% |
| `v_base` | ctl_range | 0.010 | +0.0141 | -3.4% | -11.4% | +26.7% | +3.79 | +0.99 | 11.4% |
| `v_base` | ctl_rev1 | 0.004 | +0.0172 | -3.5% | -10.9% | +29.1% | +3.88 | +1.47 | 10.5% |
| `v_base` | ctl_mom20 | 0.005 | +0.0157 | -4.5% | -8.1% | +23.4% | +2.93 | +1.79 | 4.7% |
| `v_base` | ctl_dvol20 | 0.025 | +0.0118 | -5.4% | -8.6% | +20.6% | +2.67 | +1.55 | 4.3% |
| `v_base` | ctl_cap | 0.061 | +0.0177 | -2.0% | -5.1% | +28.5% | +3.80 | +3.07 | 3.4% |
| `v_base` | ctl_turnrate | 0.044 | +0.0083 | -5.5% | -12.2% | +13.7% | +1.38 | -1.09 | 9.7% |



### 条件 IC(fit 段)

| 因子 \| 分桶变量 | Q1 | Q2 | Q3 | Q4 | Q5 |
|---|---|---|---|---|---|
| v_base|ctl_cap | +0.0214 | +0.0203 | +0.0207 | +0.0161 | +0.0082 |
| v_base|ctl_amt | +0.0039 | +0.0073 | +0.0153 | +0.0231 | +0.0330 |



### 控制变量 / 已知家族自己当因子(同口径)

| 控制变量 | 方向 | rank IC(fit) | 半衰期 | 多头腿净超额 train/valid | 纯多头夏普 train/valid | 扣费多空夏普 train/valid | 多头日换手 |
|---|---|---|---|---|---|---|---|
| `ctl_amt` | − | +0.0419 | 10 | +7.3% / +21.1% | +0.99 / +3.21 | +0.97 / +3.23 | 2.9% |
| `ctl_price` | − | +0.0059 | 1 | +3.9% / +11.3% | +0.56 / +1.59 | +0.08 / +2.09 | 1.1% |
| `ctl_ivol` | − | +0.0403 | 20 | -5.2% / +2.2% | -0.62 / +0.30 | +1.04 / +1.78 | 2.5% |
| `ctl_range` | − | +0.0388 | 20 | -4.8% / +6.9% | -0.46 / +0.72 | +0.76 / +1.61 | 3.2% |
| `ctl_rev1` | − | +0.0143 | 20 | -5.7% / -5.1% | -0.71 / -0.60 | +1.51 / +2.21 | 14.5% |
| `ctl_mom20` | − | +0.0334 | 20 | +5.4% / +8.0% | +0.66 / +0.87 | +1.05 / +2.06 | 4.0% |
| `ctl_dvol20` | − | +0.0456 | 2 | -9.0% / +0.6% | -0.89 / +0.07 | +0.67 / +1.44 | 5.5% |
| `ctl_cap` | + | +0.0016 | 20 | +0.6% / -9.0% | +0.06 / -0.92 | +0.01 / -0.94 | 0.3% |
| `ctl_turnrate` | − | +0.0462 | 20 | -2.3% / +8.2% | -0.23 / +0.92 | +0.85 / +2.05 | 1.5% |
| `known_amt_max9` | − | +0.0415 | 5 | +10.6% / +21.8% | +1.45 / +3.39 | +1.44 / +3.43 | 3.9% |
| `known_stdamt_max9` | − | +0.0484 | 5 | +13.7% / +22.2% | +1.99 / +3.59 | +2.17 / +4.10 | 4.5% |
| `known_ivol_max9` | − | +0.0501 | 20 | -2.8% / +5.3% | -0.31 / +0.66 | +1.42 / +2.05 | 2.0% |
| `known_stdamt_mean30` | − | +0.0343 | 0 | +12.6% / +22.3% | +1.78 / +3.46 | +1.87 / +3.70 | 3.4% |



### x1:这棵树在真实数据上读到的是什么(`studies/F106_erm_mag_gap_1m/x1_anatomy.py`,tag `x1`;只用 utrain)

脚本先做了三个自检:探针在服务器内核上全部通过;用零件重算的 R − L 与整棵树的最大相对差 9.8e-4;
原式的方向 −、多头半衰期 20、train 多头腿净超额 −6.9%,与 S0 一致。

**A. `Ret` 是什么**(决定 H5 的生死)

- 每个有值的股票-日都是 241 个有效分钟(100.00%),所以分位数永远恰好是一个顺序统计量,没有插值造成的过渡区间。
- **第一个分钟的 `Ret` 在 100% 的股票-日上恰好是 0** —— `Ret` 不含隔夜跳空。`day_sum(Ret)` 与「收盘/开盘 − 1」的相关 0.9989、
  中位绝对差 0.027%;与「收盘/昨收 − 1」的相关只有 0.8985、中位绝对差 0.42%。
- 去掉第一个分钟重算整棵树,在常规日上与原式的日截面 rank 相关 0.999。
- **H5(常规区间读的是隔夜跳空)被杀死**:第一分钟不可能落在尾部。这棵树是纯日内的。

**B. 三个区间在真实数据上各占多少、各是什么日子**

| | 占全部股票-日 | 涨停收盘占比 | 跌停收盘占比 | 收盘价 < 3 元 | 成交额排名后 20% |
|---|---|---|---|---|---|
| 两侧都常规 | 99.40% | 1.2% | 0.6% | — | — |
| 右侧塌缩为主(X ≥ +500) | 0.32%(17,013 个) | **86.3%** | 6.6% | 0.2% | 10.8% |
| 左侧塌缩为主(X ≤ −500) | 0.14%(7,622 个) | **77.8%** | 16.0% | 0.2% | 10.1% |
| 边缘(5 ≤ \|X\| < 500) | 0.06%(2,957 个) | 56.2% | 24.6% | 0.1% | 18.6% |
| 全部股票-日的基准率 | | 1.59% | 0.67% | | 20% |

- X 的分位数:0.1% −3192、1% −1.18、5% −0.62、25% −0.149、中位 +0.056、75% +0.29、95% +0.82、99% +1.63、99.9% **+13814**。
  常规区间里 R 的中位数 1.573、L 的中位数 1.506(比高斯的 1.254 重尾),X 的四分位距只有 0.44。
- **塌缩日就是封板日**:八成左右是涨停收盘(基准率 1.6%,富集 50 倍),其余主要是跌停收盘。**H3 被支持**。
- **塌缩日不是低价/不活跃股票**:收盘价低于 3 元的只占 0.2%,成交额排名在后 20% 的只占 10% 上下(比随机的 20% 还少)。
  探针里「2~3 元的股票因为 tick 太粗而塌缩」在真实数据上基本不发生。**H4 被杀死**。
- 一字板(全天价格不动)**不在**塌缩日里:`Ret` 全为 0,两侧尾部集合都是空的,X 读 0,被归进「常规」。
  原式看不见一字板本身,只看得见「大部分时间封死、但有几分钟在动」的板。
- X 在封板日的符号取决于板是怎么封上的:几分钟拉到涨停然后封死(上涨分钟 ≤ 12 个)→ 右侧塌缩 → X ≈ +10⁴;
  一路缓涨到涨停、下跌分钟很少 → 左侧塌缩 → X ≈ −10³~−10⁴。两种都是涨停日。
- 塌缩日之后一天的表现(这些格子的次日超额,年化;可买入标签 / 不过滤的标签 / 次日开盘买不进的比例):
  只有右侧塌缩 −565% / −187% / 23.4%;两侧都塌缩 −332% / −264% / 8.0%;只有左侧塌缩 −201% / −184% / 5.3%;
  两侧常规 +1.8% / +1.4% / 2.0%。也就是 **封板日次日(能买进的那部分)每天跑输 0.8~2.2 个点**,不分 X 的正负。

**C. 实际交易的信号(EMA-20 的 −X)里,每一档是谁**(train)

- 28.5% 的格子 \|信号\| ≥ 5(仍被某个塌缩日统治);39.0% 的格子所属股票**从未**出现过塌缩日;最近一次塌缩日在 20 / 60 / 250 天以内的各占 8.3% / 19.6% / 46.2%。

| 档 | 信号中位数 | \|信号\|≥5 | 距上次塌缩日(中位,天) | 近 20 日有涨停 | 近 60 日有涨停 | 上市不满 250 日 | 市值秩 | 换手率秩 | 次日超额(可买入) | 次日超额(不过滤) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1(空头端) | −327.9 | 97.5% | 23 | 55.3% | 87.1% | 26.8% | 0.33 | 0.71 | **−28.5%** | −13.0% |
| 2 | −36.8 | 92.2% | 64 | 26.5% | 63.5% | 6.5% | 0.41 | 0.56 | −0.2% | −1.2% |
| 3 | −2.7 | 31.4% | 139 | 16.5% | 38.8% | 2.5% | 0.44 | 0.51 | +3.7% | +2.3% |
| 4~9 | −0.21~+0.03 | 0% | 从未(4 档:325) | 10~13% | 24~31% | 5~7% | 0.48~0.61 | 0.40~0.49 | +1.7%~+7.9% | −0.5%~+5.8% |
| 10(多头端) | +13.0 | 64.4% | 61 | 32.6% | 62.6% | 3.6% | 0.48 | 0.54 | **−5.2%** | −6.3% |
| 全市场 | | | | 19.7% | 41.1% | 7.4% | | | | |

- **两端都是「近期封过板的股票」**:空头端是最近(中位 23 天前)出现过「秒板」的小市值、高换手股票,其中四分之一是上市不到一年的新股;
  多头端是两个月前出现过「缓涨封板」的股票。中间六档是一年内没有任何塌缩日的股票,它们之间才是按常规区间的尾部不对称排的序。
- 把空头端再切细:信号最低的 1% 里 **95.2% 是上市不满 250 日的新股**(连续涨停期的 ES 把 EMA 顶到 −3.5 万),
  这一组用可买入标签是 −52.5%、用不过滤的标签是 **+86.4%**,7.9% 的格子次日买不进 —— 完全是口径造成的;
  1%~2% 一组 −55.6% / −51.1%,2%~5% 一组 −41.2% / −36.9%,5%~10% 一组 −11.1% / −10.7%,10%~20% 一组 −0.2%。
  多头端最高的 2% 是 −22.2% / −21.4%(其中 66.5% 近 20 日有过涨停),95%~98% 一组 −1.7%。
- 所以 **真正的跑输集中在信号两头各 2%~5% 的股票上,它们都是近期封板股**;倒 U 的两臂是同一类股票。**H6 被支持**。

**D. 事件时间:塌缩日之后第 k 天的超额(可买入标签,bp/天)**

| 事件 | 个数 | k=0 | 1 | 2 | 5 | 10 | 20 | 40 | 60 |
|---|---|---|---|---|---|---|---|---|---|
| 右侧塌缩且涨停收盘 | 14,680 | −172.2 | −56.0 | −47.4 | −19.5 | −10.3 | −8.2 | −0.1 | +0.1 |
| 右侧塌缩、非涨停 | 2,169 | −118.8 | −72.5 | −30.3 | −48.2 | +1.7 | +5.5 | +3.0 | +6.9 |
| 左侧塌缩且跌停收盘 | 1,221 | −90.9 | −61.1 | −47.2 | −2.2 | −6.0 | −3.7 | +1.2 | +2.0 |
| 左侧塌缩、非跌停 | 6,333 | −91.8 | −20.2 | −24.1 | −10.4 | −6.7 | +3.0 | −2.3 | +0.7 |
| **涨停收盘但 X 常规** | 62,438 | −69.2 | −29.2 | −29.9 | −16.5 | −11.1 | −10.0 | −4.5 | −1.9 |
| 跌停收盘但 X 常规 | 32,465 | −38.2 | −22.0 | −4.3 | −6.6 | +0.1 | +1.6 | −5.7 | +1.3 |

- 封板之后的跑输持续约 20 个交易日,40 天之后归零。而 EMA-20 把一个 10⁴ 的读数记上一年 —— **记忆长度比效应长一个数量级**,
  这就是 Q2、Q3、Q10 这些「几个月前封过板」的档位收益平平的原因。
- **没塌缩的涨停日事后同样跑输**(−69 bp、之后二十天每天 −10~−30 bp),而它们的数量是塌缩涨停日的四倍多(62,438 对 14,680)。
  原式只抓到了涨停日里「封得死」的那五分之一。

**E. 各种构造的两本书(numpy 版,fit = train;train / valid)**

| 构造 | 方向 | hlL | 多头腿净超额 | 纯多头夏普 | hlS | 多空夏普 | 空头腿(train) | 日频 rank IC | 与原式信号的秩相关 |
|---|---|---|---|---|---|---|---|---|---|
| 原式 X | − | 20 | −6.9% / −3.2% | −2.15 / −1.23 | 20 | +2.82 / +3.24 | +27.9% | 0.0067 / 0.0027 | 1.00 |
| 只留常规日(塌缩日置 0) | − | 20 | −12.0% / −9.7% | −2.49 / −2.45 | 20 | **−1.45 / −2.11** | +9.8% | 0.0036 / 0.0006 | 0.41 |
| 先截面排序再 EMA | − | 20 | −12.8% / −13.2% | −2.17 / −2.49 | 20 | **−0.93 / −1.40** | +14.7% | 0.0067 / 0.0027 | 0.48 |
| clip(X, ±3) | − | 20 | −10.7% / −9.3% | −2.28 / −2.37 | 20 | +0.80 / +0.13 | +25.6% | 0.0067 / 0.0027 | 0.61 |
| 只留右侧 R | − | 20 | −4.2% / −4.0% | −0.65 / −0.60 | 20 | +2.10 / +1.78 | +32.1% | 0.0135 / 0.0104 | 0.63 |
| 只留左侧 L | **−** | 20 | −8.2% / −3.4% | −1.60 / −0.60 | 20 | +1.61 / +1.76 | +27.5% | 0.0083 / 0.0087 | 0.19 |
| 任一侧塌缩的 0/1 标记 | − | 1 | +2.7% / +3.5% | +0.42 / +0.44 | 5 | +3.40 / +2.66 | +38.6% | 0.0320 / 0.0236 | 0.38 |
| 日线涨停标记(5/10/20% 板) | − | 0 | +2.1% / +1.9% | +0.33 / +0.19 | 1 | +3.09 / +3.73 | +51.2% | 0.0424 / 0.0319 | 0.06 |
| 多头 = \|EMA20(X)\| 最小 | (强制) | 20 | +2.4% / −6.0% | +0.34 / −0.88 | 2 | +2.07 / +1.05 | +26.8% | — | 0.56 |

- **去掉塌缩日(或抹掉量级),多空夏普从 +2.82 / +3.24 变成负的** → 常规区间的尾部形状不对称没有可交易的信号。**H1 被支持、H2 被杀死**。
- **L 单独用的方向也是 −**(L 越大越差),与 R 同向 → 「右减左」是在让两个同向的读数互相抵消。**H8 被支持**(两侧不是镜像)。
- 一个不带任何幅度的塌缩标记、乃至一个朴素的日线涨停标记,多空夏普就与原式相当或更高,日频 rank IC 是原式的 5~6 倍。
  (这些 0/1 构造的「多头腿」是并列里按股票代码顺序取的 10%,没有意义;它们过不了 dist 门槛,只用来分辨。)
- 上涨/下跌/零收益分钟占比这类「活跃度」读数的多头腿在 train 为负、valid 为正(−8.5% / +5.5% 等),是换手率/波动家族的制度性表现,不是这棵树的东西。
- 所有从这棵树派生出来的连续构造,**多头腿净超额在 train 和 valid 上没有一个同时为正**。

**F. 空头腿里有多少是「买不进的票」撑的**(原式信号,半衰期 20)

| | 空头腿(可买入标签) | 多空夏普 | 空头腿(不过滤标签) | 多空夏普 |
|---|---|---|---|---|
| train | +27.9% | +2.82 | **+12.5%** | **+0.42** |
| valid | +22.4% | +3.24 | +16.8% | +2.26 |

train 上空头腿 27.9 个点里有 15.4 个点来自「次日开盘封涨停、标签缺失、在空头里记 0」的票(主要是连板新股);
换成不过滤的标签,多空夏普从 2.82 掉到 0.42。valid 上掉 5.6 个点、夏普从 3.24 到 2.26。
**公布的多空夏普有一半以上(train)是口径造成的**;多头腿不受这个影响(不过滤标签下 train −6.1%、valid −1.4%,仍然为负)。

**G. 折叠之后是不是已知暴露**(train,日截面 rank 相关 / 秩空间 R²)

信号到截面中位的距离(折叠量)与「近 20 日塌缩日密度(EMA)」的 rank 相关 +0.615,单变量 R² 0.384;
与价格、成交额、市值、换手率、日内波动五个控制变量合起来的 R² 只有 0.068(加上塌缩密度后 0.398)。
带符号的信号对塌缩密度的 R² 是 0.166。也就是说:折叠量的近四成就是「最近封过板没有」,它不是成交额/规模/波动/换手这些水平型暴露。

# 07x_2 — `x2_longonly.py` 的输出(事实记录,R1,执行写)

> 本文件只记 `studies/F106_erm_mag_gap_1m/x2_longonly.py`(tag `x2`)的输出事实与异常,**不做判断、不下结论** ——
> 判据已经事前登记在 `05_hypotheses.md`「R1 的读法预登记」,裁决由下一轮主研做。
> 全部数字只在 **utrain**(= train + valid)上;本工单未碰留出段,也没有新增/修改 `configs/F106_erm_mag_gap_1m.yaml` 里的任何阶段。

## 0. 跑法与核对

- tag `x2`,脚本 211 行,上一位研究员写好、上一个执行 agent 起的(`study.sh exec F106_erm_mag_gap_1m x2 x2_longonly.py`)。
  `selftest`(`push_down` 的性质,随机数组)此前已经跑过并通过(输出 `x2 selftest OK`),**本轮未重跑**。
- 本轮执行只做了 `./scripts/study.sh wait F106_erm_mag_gap_1m x2`:job 在服务器上已经是 `exit 0`
  (`2026-10-05_04:54:27` 服务器时间),**没有重跑、没有起第二个**。`wait` 等了约 1480 秒(内存守卫排队,
  `container anon` 一度到 36~43 GiB),之后把日志整份拉回本地 `logs/F106_erm_mag_gap_1m_x2.log`(157 行,之前本地没有),
  屏幕上和文件里的内容逐字一致(该文件总行数本身小于 200,所以这次没有被 `tail -200` 截断的问题)。`runs/` 没有对应
  JSON(exec 脚本自己打印输出,不产出结构化 JSON,这是预期行为)。
- `st.control("g_max30")` 与 `st.control("g_limitup30")` **核对后都存在**,不是假警报:
  - `g_max30 = cross_max(div(day_last(Close), cross_delay(day_last(Close), 1)), 30)`(近 30 日最大单日涨幅,MAX/彩票效应代理)
  - `g_limitup30 = cross_sum(mul(sub(1, less(Close, High)), greater(Close/Close_delay1, 1.095)), 30)`
    (近 30 日「收在当日最高价且涨幅 ≥ 9.5%」的天数 —— **只抓 ≥9.5% 的板,漏掉 5% 的 ST 板**)
  两者都定义在 `configs/F106_erm_mag_gap_1m.yaml` 的 `gates:` 第 50–51 行,第 4 节正常跑通,没有触发脚本里的自造等价量分支。
- 脚本全程没有抛异常;唯一带 try/except 的是 `book_line`(逐行捕获,失败只打印 `FAILED` 不中断),**9 行全部正常输出,没有一行 FAILED**。

---

## 1. 已知家族多头十分位的构成(9 个 flag × 2 split × 2 family = 36 行)

列含义:`share of long decile` = 已知家族多头十分位里被该 flag 标记的票占比;`share of universe` = 全体有已知家族信号的票里被标记的占比(基准率);
`flagged ex` / `unflagged ex` = 多头十分位里「被标记」/「没被标记」的票,次日超额(按日横截面均值去中心化后)年化。

### known30 = `cross_mean(day_std(Amt), 30)`(`sign -1, hl_long 0`;train Lnet +12.6% Lshp +1.78;valid Lnet +22.3% Lshp +3.46)

与 F106 信号(train)的秩相关:+0.005;与 \|pct(F106)-0.5\|(折叠)的秩相关:−0.094。

| flag | split | share of 多头十分位 | share of universe | flagged ex | unflagged ex |
|---|---|---|---|---|---|
| blown day within 20d | train | 0.051 | 0.080 | −22.1% | +17.4% |
| blown day within 20d | valid | 0.022 | 0.067 | −4.1% | +27.7% |
| blown day within 60d | train | 0.131 | 0.194 | +3.4% | +17.9% |
| blown day within 60d | valid | 0.078 | 0.167 | +17.7% | +27.7% |
| limit-up close within 20d | train | 0.073 | 0.197 | −25.2% | +18.6% |
| limit-up close within 20d | valid | 0.034 | 0.154 | +11.7% | +27.7% |
| limit-up close within 60d | train | 0.208 | 0.411 | +5.1% | +18.8% |
| limit-up close within 60d | valid | 0.130 | 0.341 | +20.6% | +27.5% |
| limit-up or -down within 20d | train | 0.128 | 0.264 | −32.2% | +19.0% |
| limit-up or -down within 20d | valid | 0.067 | 0.193 | +17.5% | +27.6% |
| F106 signal decile 1(short end) | train | 0.045 | 0.100 | −22.1% | +17.0% |
| F106 signal decile 1(short end) | valid | 0.042 | 0.100 | +15.4% | +27.4% |
| F106 signal decile 1 or 10 | train | 0.138 | 0.200 | +3.9% | +17.5% |
| F106 signal decile 1 or 10 | valid | 0.114 | 0.200 | +24.5% | +27.4% |
| \|F106 signal\| >= 5 | train | 0.229 | 0.285 | +12.3% | +17.5% |
| \|F106 signal\| >= 5 | valid | 0.189 | 0.265 | +26.4% | +26.4% |
| listed < 250d | train | 0.043 | 0.074 | **−127.0%** | +17.0% |
| listed < 250d | valid | 0.100 | 0.083 | +14.8% | +28.3% |

### known9 = `cross_max(day_std(Amt), 9)`(`sign -1, hl_long 5`;train Lnet +13.7% Lshp +1.99;valid Lnet +22.2% Lshp +3.59)

与 F106 信号(train)的秩相关:+0.035;与折叠的秩相关:−0.114。

| flag | split | share of 多头十分位 | share of universe | flagged ex | unflagged ex |
|---|---|---|---|---|---|
| blown day within 20d | train | 0.041 | 0.080 | −27.6% | +19.4% |
| blown day within 20d | valid | **0.016** | 0.067 | −7.6% | +28.0% |
| blown day within 60d | train | 0.122 | 0.194 | +9.9% | +19.5% |
| blown day within 60d | valid | 0.073 | 0.167 | +25.4% | +27.6% |
| limit-up close within 20d | train | 0.054 | 0.197 | −29.1% | +20.1% |
| limit-up close within 20d | valid | 0.023 | 0.154 | +17.9% | +27.7% |
| limit-up close within 60d | train | 0.197 | 0.411 | +9.4% | +19.7% |
| limit-up close within 60d | valid | 0.125 | 0.341 | +26.7% | +27.2% |
| limit-up or -down within 20d | train | 0.108 | 0.264 | −27.5% | +20.8% |
| limit-up or -down within 20d | valid | 0.055 | 0.193 | +24.4% | +27.5% |
| F106 signal decile 1(short end) | train | 0.044 | 0.100 | −17.7% | +19.0% |
| F106 signal decile 1(short end) | valid | 0.040 | 0.100 | +25.9% | +27.7% |
| F106 signal decile 1 or 10 | train | 0.136 | 0.200 | +9.6% | +19.1% |
| F106 signal decile 1 or 10 | valid | 0.113 | 0.200 | +29.2% | +27.5% |
| \|F106 signal\| >= 5 | train | 0.223 | 0.285 | +18.3% | +19.0% |
| \|F106 signal\| >= 5 | valid | 0.186 | 0.265 | +29.3% | +26.5% |
| listed < 250d | train | 0.047 | 0.074 | **−97.2%** | +19.4% |
| listed < 250d | valid | 0.097 | 0.083 | +11.7% | +28.9% |

(粗体是「没人要但值得注意的」里要点出的格子,见本文件末尾。)

---

## 2. 剔除被标记的票之后,多头腿的变化(同一 sign / 同一 half-life,**不重新拟合**)

`push_down` 把被标记的票压到当天所有票之下。**本节每行的 `LS`、`short` 不代表已知家族的空头腿**——push_down 把被标记票送进了
空头十分位,叠加后的空头腿是「做空被标记的票」,不是已知家族自己的空头腿,所以下表只列 `Lnet / Lshp / Lgross / LTO / dLnet`。
`Lnet` 已经扣了 15bp/边的费,`dLnet` 可以直接读。

### known30(基准:train Lnet +12.6% Lshp +1.78 Lgross +15.2% LTO 3.4%;valid Lnet +22.3% Lshp +3.46 Lgross +24.4% LTO 2.8%)

| flag | split | Lnet | Lshp | Lgross | LTO | dLnet |
|---|---|---|---|---|---|---|
| blown day within 20d | train | +14.2% | +2.06 | +16.8% | 3.5% | +1.59 |
| blown day within 20d | valid | +22.9% | +3.58 | +25.0% | 2.9% | +0.52 |
| blown day within 60d | train | +13.6% | +2.00 | +16.1% | 3.3% | +0.94 |
| blown day within 60d | valid | +22.8% | +3.57 | +24.9% | 2.8% | +0.47 |
| limit-up close within 20d | train | +14.5% | +2.11 | +17.3% | 3.7% | +1.92 |
| limit-up close within 20d | valid | +22.8% | +3.57 | +25.0% | 2.9% | +0.50 |
| limit-up close within 60d | train | +14.1% | +2.08 | +16.7% | 3.4% | +1.50 |
| limit-up close within 60d | valid | +22.7% | +3.57 | +24.8% | 2.7% | +0.36 |
| limit-up or -down within 20d | train | +14.3% | +2.10 | +17.3% | 4.0% | +1.73 |
| limit-up or -down within 20d | valid | +22.4% | +3.53 | +24.8% | 3.1% | +0.12 |
| F106 signal decile 1(short end) | train | +13.9% | +1.98 | +16.4% | 3.3% | +1.29 |
| F106 signal decile 1(short end) | valid | +22.4% | +3.50 | +24.4% | 2.8% | +0.03 |
| F106 signal decile 1 or 10 | train | +13.4% | +1.95 | +16.0% | 3.5% | +0.74 |
| F106 signal decile 1 or 10 | valid | +22.5% | +3.57 | +24.7% | 2.9% | +0.22 |
| \|F106 signal\| >= 5 | train | +13.0% | +1.92 | +15.3% | 3.1% | +0.35 |
| \|F106 signal\| >= 5 | valid | +21.9% | +3.50 | +23.9% | 2.6% | −0.44 |
| listed < 250d | train | +14.2% | +2.02 | +16.7% | 3.2% | +1.60 |
| listed < 250d | valid | +23.4% | +3.70 | +25.5% | 2.7% | +1.09 |

### known9(基准:train Lnet +13.7% Lshp +1.99 Lgross +17.1% LTO 4.5%;valid Lnet +22.2% Lshp +3.59 Lgross +25.1% LTO 3.9%)

| flag | split | Lnet | Lshp | Lgross | LTO | dLnet |
|---|---|---|---|---|---|---|
| blown day within 20d | train | +15.3% | +2.28 | +18.7% | 4.6% | +1.60 |
| blown day within 20d | valid | +22.6% | +3.67 | +25.6% | 4.0% | +0.40 |
| blown day within 60d | train | +15.0% | +2.27 | +18.4% | 4.4% | +1.32 |
| blown day within 60d | valid | +22.4% | +3.67 | +25.3% | 3.9% | +0.19 |
| limit-up close within 20d | train | +15.6% | +2.32 | +19.1% | 4.7% | +1.89 |
| limit-up close within 20d | valid | +22.1% | +3.60 | +25.1% | 4.0% | **−0.04** |
| limit-up close within 60d | train | +14.5% | +2.19 | +17.8% | 4.4% | +0.82 |
| limit-up close within 60d | valid | +21.5% | +3.49 | +24.4% | 3.8% | −0.67 |
| limit-up or -down within 20d | train | +14.9% | +2.22 | +18.6% | 5.0% | +1.19 |
| limit-up or -down within 20d | valid | +21.7% | +3.55 | +24.8% | 4.1% | −0.42 |
| F106 signal decile 1(short end) | train | +15.0% | +2.20 | +18.3% | 4.4% | +1.27 |
| F106 signal decile 1(short end) | valid | +22.4% | +3.66 | +25.3% | 3.9% | +0.22 |
| F106 signal decile 1 or 10 | train | +14.5% | +2.16 | +17.9% | 4.6% | +0.75 |
| F106 signal decile 1 or 10 | valid | +22.2% | +3.66 | +25.2% | 3.9% | +0.03 |
| \|F106 signal\| >= 5 | train | +14.5% | +2.18 | +17.6% | 4.1% | +0.81 |
| \|F106 signal\| >= 5 | valid | +21.1% | +3.50 | +23.8% | 3.6% | −1.08 |
| listed < 250d | train | +15.6% | +2.28 | +18.9% | 4.3% | +1.90 |
| listed < 250d | valid | +24.1% | +3.94 | +27.0% | 3.8% | +1.95 |

(粗体同上,见文末「异常」。)

---

## 3. 和书 `rank(known) + w·rank(F106)`,以及双向中性化残差

两个已知家族自己的基准(与上面相同):known30 train +12.6%/valid +22.3%;known9 train +13.7%/valid +22.2%。

### known30

| 构造 | train Lnet | train Lshp | train Lgross | train LTO | valid Lnet | valid Lshp | valid Lgross | valid LTO |
|---|---|---|---|---|---|---|---|---|
| rank(known30) + 0.25·rank(F106) | +11.9% | +1.75 | +15.2% | 4.3% | +18.7% | +3.15 | +21.6% | 3.9% |
| rank(known30) + 0.5·rank(F106) | +8.5% | +1.32 | +12.5% | 5.3% | +16.5% | +3.09 | +20.6% | 5.3% |
| rank(known30) + 1·rank(F106) | +6.9% | +1.16 | +11.7% | 6.3% | +13.4% | +2.86 | +18.4% | 6.5% |
| rank(known30) + 0.25·(−fold F106) | +11.4% | +1.71 | +15.7% | 5.7% | +19.6% | +3.17 | +23.5% | 5.1% |
| rank(known30) + 0.5·(−fold F106) | +9.1% | +1.43 | +15.2% | 8.1% | +16.1% | +2.79 | +21.9% | 7.7% |
| rank(known30) + 1·(−fold F106) | +5.4% | +0.92 | +13.9% | 11.2% | +10.9% | +2.08 | +19.5% | 11.4% |

- F106 信号对 known30 中性化:R² = 0.002;残差 Lnet train **−6.4%** Lshp −2.04 Lgross −4.3% LTO 2.7%,valid **−3.0%** Lshp −1.17 Lgross −1.4% LTO 2.1%
- known30 对(F106 信号 + 其折叠)中性化:R² = 0.014;残差 Lnet train +11.1% Lshp +1.57 Lgross +14.4% LTO 4.4%,valid +21.2% Lshp +3.32 Lgross +24.2% LTO 4.1%

### known9

| 构造 | train Lnet | train Lshp | train Lgross | train LTO | valid Lnet | valid Lshp | valid Lgross | valid LTO |
|---|---|---|---|---|---|---|---|---|
| rank(known9) + 0.25·rank(F106) | +13.1% | +1.97 | +16.9% | 5.0% | +18.6% | +3.25 | +22.0% | 4.5% |
| rank(known9) + 0.5·rank(F106) | +9.6% | +1.54 | +14.1% | 5.9% | +15.3% | +2.94 | +19.6% | 5.8% |
| rank(known9) + 1·rank(F106) | +6.9% | +1.19 | +12.1% | 6.9% | +12.8% | +2.78 | +18.1% | 6.9% |
| rank(known9) + 0.25·(−fold F106) | +12.7% | +1.94 | +17.5% | 6.3% | +19.1% | +3.19 | +23.4% | 5.8% |
| rank(known9) + 0.5·(−fold F106) | +9.8% | +1.57 | +16.2% | 8.5% | +16.3% | +2.94 | +22.6% | 8.3% |
| rank(known9) + 1·(−fold F106) | +6.3% | +1.09 | +15.1% | 11.6% | +10.1% | +2.01 | +19.0% | 11.8% |

- F106 信号对 known9 中性化:R² = 0.004;残差 Lnet train **−7.5%** Lshp −2.38 Lgross −5.4% LTO 2.9%,valid **−4.3%** Lshp −1.61 Lgross −2.6% LTO 2.2%
- known9 对(F106 信号 + 其折叠)中性化:R² = 0.020;残差 Lnet train +12.0% Lshp +1.76 Lgross +16.1% LTO 5.4%,valid +21.2% Lshp +3.43 Lgross +25.1% LTO 5.1%

**事实(不是结论)**:上面两张"和书"表里,`w` 从 0.25 升到 1(两个方向:+rank(F106) 与 +(−fold F106)),`Lnet` 相对各自已知家族基准
单调下降,train/valid、known30/known9 四组全部如此,没有一个 w 让 Lnet 高于基准。

---

## 4. F106 信号对「近期涨停」类变量中性化后的残差(秩空间)

F106 信号基准(无中性化):train Lnet −6.9% Lshp −2.15 Lgross −5.1% LTO 2.4% LS +2.82 short +27.9% rIC +0.0165;
valid Lnet −3.2% Lshp −1.23 Lgross −1.8% LTO 1.8% LS +3.24 short +22.4% rIC +0.0086。

| 中性化于 | R² | train Lnet | train Lshp | train Lgross | train LTO | train LS | train short | train rIC | valid Lnet | valid Lshp | valid Lgross | valid LTO | valid LS | valid short | valid rIC |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| g_max30(近30日最大单日涨幅) | 0.017 | −8.5% | −2.28 | −5.5% | 4.0% | +1.45 | +19.6% | +0.0119 | −5.9% | −2.20 | −3.9% | 2.7% | +1.88 | +18.4% | +0.0052 |
| g_limitup30(近30日涨停收盘天数,≥9.5%) | 0.041 | −8.6% | −2.19 | −6.1% | 3.3% | −1.40 | +3.3% | +0.0101 | −7.0% | −2.45 | −4.8% | 2.8% | −2.54 | −3.3% | +0.0016 |
| EMA20(limit-up close flag,完整5/10/20%定义) | 0.084 | −8.5% | −2.06 | −5.9% | 3.4% | +0.42 | +13.1% | +0.0091 | −6.2% | −2.10 | −4.2% | 2.6% | +0.90 | +12.4% | +0.0022 |
| EMA20(blown flag,\|X\|>=5) | 0.159 | −5.8% | −1.73 | −4.1% | 2.2% | +1.03 | +15.3% | +0.0139 | −3.4% | −1.33 | −2.3% | 1.5% | +2.13 | +16.9% | +0.0083 |
| all four | 0.164 | −6.3% | −1.88 | −4.5% | 2.3% | −0.31 | +9.2% | +0.0113 | −4.1% | −1.59 | −2.8% | 1.8% | −0.66 | +6.0% | +0.0068 |

折叠量(\|pct(F106)−0.5\|)对同一组控制变量的 R²(供"折叠关系"参照,playbook §6.5):
g_max30 0.042;g_limitup30 0.100;EMA20(limit-up close flag) 0.203;EMA20(blown flag) 0.437;all four **0.444**。

**事实(不是结论)**:5 行残差(含 `all four`)的 `Lnet` 在 train、valid 都仍是负的,没有一行翻正;`g_limitup30` 单独一行残差
把 `LS` 由 +2.82/+3.24 翻到 −1.40/−2.54(叠加 `all four` 后 LS 也是负的,−0.31/−0.66)。带符号信号对这组变量的 R² 全部 ≤ 0.164,
而折叠量对 `EMA20(blown flag)`、`all four` 的 R² 到 0.437/0.444。

---

## 5. 显式短记忆构造(9 行;方向在 train 上拟合)

| 名字 | 方向 | hlL | train Lnet | valid Lnet | train Lshp | valid Lshp | LTO(train) | hlS | train LS | valid LS | short(train) | train rIC | valid rIC | corr(base) | fin(train) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| count of blown days, last 10d | − | 1 | **+3.3%** | **+3.1%** | +0.52 | +0.36 | 0.4% | 0 | +3.35 | +1.34 | +33.2% | +0.0333 | +0.0303 | +0.40 | 0.69 |
| count of limit-up closes, last 10d | − | 0 | **+4.9%** | **+3.0%** | +0.80 | +0.29 | 1.4% | 0 | +3.69 | +2.63 | +47.1% | +0.0433 | +0.0412 | +0.13 | 0.69 |
| count of blown days, last 20d | − | 1 | **+3.3%** | **+3.1%** | +0.52 | +0.37 | 0.4% | 0 | +3.57 | +1.96 | +35.0% | +0.0316 | +0.0300 | +0.40 | 0.69 |
| count of limit-up closes, last 20d | − | 0 | **+6.3%** | **+4.1%** | +1.07 | +0.41 | 1.4% | 0 | +3.32 | +2.70 | +40.1% | +0.0424 | +0.0417 | +0.17 | 0.69 |
| count of blown days, last 40d | − | 1 | **+3.3%** | **+3.1%** | +0.52 | +0.36 | 0.4% | 0 | +2.79 | +1.60 | +27.7% | +0.0288 | +0.0260 | +0.40 | 0.69 |
| count of limit-up closes, last 40d | − | 0 | **+6.9%** | **+3.9%** | +1.25 | +0.41 | 1.3% | 0 | +2.78 | +2.40 | +32.3% | +0.0397 | +0.0373 | +0.21 | 0.69 |
| log(1+\|X\|) | − | 20 | −0.1% | −15.2% | −0.01 | −1.62 | 7.4% | 20 | +2.43 | +0.55 | +35.9% | +0.0076 | +0.0010 | +0.37 | 0.69 |
| R + L | − | 20 | −3.2% | −3.3% | −0.51 | −0.52 | 4.6% | 20 | +2.26 | +2.01 | +32.6% | +0.0137 | +0.0109 | +0.47 | 0.69 |
| log(1+R+L) | − | 20 | −6.9% | +1.5% | −1.12 | +0.22 | 4.4% | 20 | +2.40 | +2.74 | +36.2% | +0.0137 | +0.0109 | +0.33 | 0.69 |

对照:F106 原信号(EMA-20(X))的 rIC 是 train +0.0165 / valid +0.0086(见第 4 节)。

**Lnet 在 train 和 valid 同时为正的行(按脚本原样读数)**:上表前 6 行(两种「近 10/20/40 日计数」构造,共 6 行,已用粗体标出)。
后 3 行(`log(1+\|X\|)`、`R + L`、`log(1+R+L)`)Lnet 不是两段同正:前两行两段都是负的,`log(1+R+L)` 是 train 负 valid 正(−6.9%/+1.5%)。

⚠️ **主研已在工单 R1 的补注里标出**:前 6 行(两种计数 × 10/20/40 日窗口)在 train 上拟合出的方向都是 `−`、
取值绝大多数格子是 0,所以这 6 行的"多头腿 10%"实际上是「计数 = 0」这一大片并列里**按股票代码顺序**切出来的,
**不是可交易的书**,和 state.md §8.3 提到的 0/1 标记"假多头腿"同一个毛病。只有 `log(1+\|X\|)`、`R + L`、`log(1+R+L)` 三行的取值连续,
多头腿数字可以当书读。本文件按脚本原样抄了全部 9 行数字,但并列书这三个字必须跟着这 6 行一起抄,不能只抄数字。
`fin`(train 覆盖率)9 行全部是 0.69,等于 F106 base 面板自身的覆盖率,和窗口长度、构造方式无关。

---

## 异常与注意(逐项对应"要带回来的数字"第 6 条)

1. **`listed < 250d` 这一 flag,train 和 valid 的 `flagged ex` 符号相反、量级相差一个数量级**:known30 train −127.0% → valid +14.8%;
   known9 train −97.2% → valid +11.7%。这是 9 个 flag 里唯一一个两段读数方向都不一致、且绝对值远超其余任何一格的。
2. **`blown day within 20d` 在 known9/valid 的「share of 多头十分位」是 0.016**,是全表(36 格)里唯一低于 2% 的一格
   (其余所有格子,包括同一 flag 在 known30/valid 的 0.022,都 ≥ 2%)。
3. **`limit-up close within 20d` 在 known9/valid 的叠加 `dLnet` 是 −0.04**,是这个 flag 在四个(split × family)格子里唯一不为正的一格
   (其余三格 +1.92 / +0.50 / +1.89)。
4. 第 3 节「和书」构造:`rank(known) + w·rank(F106)`(两个方向、w = 0.25/0.5/1,两个已知家族,两段)一共 24 行,
   **没有一行的 Lnet 高于对应已知家族自己的基准**,且随 w 增大单调下降。
5. 第 4 节:把 F106 信号对 `g_max30`/`g_limitup30`/`EMA20(limit-up close flag)`/`EMA20(blown flag)`/`all four` 分别中性化,
   **残差 Lnet 在 train 和 valid 全部仍为负**,没有一行翻正;其中 `g_limitup30` 和 `all four` 两行的残差 `LS` 由正翻负。
6. 第 4 节折叠量的 R² 普遍比带符号信号的 R² 高出 2~3 倍(例如 `all four`:折叠 0.444 vs 带符号 0.164)——数字已照抄,
   这与 playbook §6.5「秩空间线性中性化看不见非单调折叠关系」一致。
7. 第 5 节 9 行里有 6 行(两类计数 × 10/20/40 日窗口)是并列书,已在上面单独标出;这 6 行恰好是「Lnet 两段同正」的全部 6 行。
8. **没有脚本报错、没有 NaN 比例异常、没有需要自造的 control**(`g_max30`/`g_limitup30` 都正常解析)。
   本工单没有新增/修改 `configs/F106_erm_mag_gap_1m.yaml` 里的阶段,因此这些数字没有(也不需要)走 S0/S1 式的
   引擎级 `cov`/`dist` 门槛——第 5 节的 `fin`(覆盖率)是脚本自己算的一个更简单的指标,不是同一个口径。

## 原始输出

- `logs/F106_erm_mag_gap_1m_x2.log`(157 行,已拉回本地;`[x2 done]` / `[partura exit 0 2026-10-05_04:54:27]`)
- `./scripts/study.sh digest F106_erm_mag_gap_1m x2` 不适用(exec 脚本没有 JSON digest,直接读日志)

---

## 解读(主研第 2 轮,2026-10-04)

上面是执行记录的事实。这一节是判断。逐条裁决写在 `05_hypotheses.md` 的「裁决(主研第 2 轮)」一节,这里只讲这份输出**意味着什么**。

### 这份输出回答的那个问题

x1 之后,这条因子只剩一个用途还没被排除:**它不是一本书,而是一张「不要持有谁」的清单** ——
对用户真正会持有的那本书(已知家族 `cross_mean(day_std(Amt),30)` / `cross_max(day_std(Amt),9)`)有没有排除性增量。
x2 的五节正是为这件事设计的:第 1 节看已知家族多头腿里有没有这些票,第 2 节看剔掉之后多了多少,
第 3 节看相加和残差,第 4 节看朴素涨停标记够不够,第 5 节看换成短记忆行不行。

### 结论:**没有增量。而且这不是运气不好,是结构决定的。**

1. **第 2 节的 ΔLnet 方向全对、量级不够。** 塌缩标记在四个格子上都是正的(+1.59/+0.52/+1.60/+0.40),
   机制也看得见(被标记票的次日超额在四格里全部远差于未标记票),但 **valid 上只剩半个点**,
   而 playbook §4.6 给的噪声是 **±3 个点**。按事前登记的判据 (c)(d),H10 被否定。
2. **天花板是可以算出来的。** 叠加收益 ≈(被标记票占多头十分位的比例)×(标记与未标记的超额之差);
   这个乘积在四个格子上分别是 2.0 / 0.70 / 1.93 / 0.57,与实测 +1.59/+0.52/+1.60/+0.40 全部吻合到 25% 以内。
   → 想让增量变大,只能靠「已知家族多头腿里有更多被标记票」或「被标记票更差」,两个都不是我们能调的。
3. **已知家族本来就在躲这些票。** 被标记票占全市场 8.0%/6.7%,占已知家族多头十分位只有 5.1%/2.2%(known30)、
   4.1%/1.6%(known9)—— **只有全市场频率的 24%~64%**(涨停标记更极端,15%~37%)。
   「低 Amt 日内波动」这个条件和「最近没封过板」高度重合。**F106 想剔的票,已知家族大半已经没买。**
   这是整条研究最有解释力的一句话:**不是 F106 的清单不准,是这张清单对这本书来说是多余的。**
4. **相加更糟。** 第 3 节 24 行没有一行好于基准,而且随权重单调下降 —— F106 的排序往已知家族里掺多少都是在稀释它。
   `v_sum` 这条候选排除。
5. **换一个更朴素的变量也拿得到同样的效果。** 第 2 节里朴素涨停标记与塌缩标记打平(train 上朴素的还更好)。
   对用户的可操作结论因此是:**要这个排除效果,一个日线涨停标记就够;而且这个效果只值 valid 上的半个点。**

### 两个「意外」,都是有意义的

- **第 5 节 rank IC 的跃升坐实了 H11,但救不了这棵树。** 显式短记忆(近 10/20/40 日计数)的 rank IC 是
  EMA-20(X) 的 1.7~4.8 倍,**两段都更优**,而且 20 日窗口在叠加上全面优于 60 日窗口 —— 记忆太长这件事坐实了。
  但优势只出现在**取值几乎全是 0** 的计数构造上(过不了 `dist ≥ 0.5`、多头端是并列按股票代码切的);
  三条连续构造的 rank IC 反而**低于原式**。→ 记忆修对了也不产生候选,这是一条诊断结论。
- **`listed < 250d` 打败了每一张 F106 标记。** ΔLnet +1.60/+1.09(known30)、+1.90/+1.95(known9),
  四格全部 ≥ 1 个点,是唯一一张在 valid 上也拿到一个点以上的标记。
  按事前登记,这条的诚实读法是:**「这里值钱的是一个新股过滤器,不是这条因子」**(x1 C 早就量到:信号最低 1% 里 95.2% 是上市不满 250 日的新股)。
  ⚠️ 它的 `flagged ex` 两段符号相反、量级差一个数量级(known30 train −127.0% → valid +14.8%),
  说明 train 上那个 −127% 是少数连板新股在可买入标签下的极端值,**不要把它当成一个稳定的 −127%**;
  但「剔掉新股对已知家族多头腿有稳定的一个多点好处」这件事两段一致。**这是给用户的一条顺手的建议,不是这条因子的功劳。**

### 这份输出**不能**用来说的事

- 任何一行叠加的 `LS` / `short`:`push_down` 把被标记票推进了空头十分位,叠加后的空头腿是「做空被标记的票」,
  不是已知家族的空头腿。事前登记已说明,这些列一律不读(所以上面的表里没有它们的解读)。
- 第 5 节六行计数构造的 `Lnet`(+3.0%~+6.9%):并列书,不是可交易的多头腿。
- 第 4 节的 R² 本身:秩空间线性中性化在这条因子上读不出折叠关系(playbook §6.5),
  所以主证据是**折叠量**的 R²(`all four` 0.444)和**残差的 Lnet / rank IC**,不是带符号信号的 R²(0.164)。

## 8. 语义变体

| 变体 | 表达式 | 方向 | 半衰期(多头) | **多头腿净超额** train/valid | 纯多头夏普 train/valid | 多头腿毛超额 train/valid | 多头日换手 | 半衰期(多空) | 扣费多空夏普 train/valid | 空头腿毛超额 train | rank IC train/valid | cov / dist |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `v_base` | `sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)...` | − | 20 | **-6.9% / -3.2%** | -2.15 / -1.23 | -5.1% / -1.8% | 2.4% | 20 | +2.82 / +3.24 | +27.9% | +0.0067 / +0.0027 | 1.00 / 0.99 |
| `f_orig` | `sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)...` | − | 20 | **-6.9% / -3.2%** | -2.15 / -1.23 | -5.1% / -1.8% | 2.4% | 20 | +2.82 / +3.24 | +27.9% | +0.0067 / +0.0027 | 1.00 / 0.99 |
| `f_known30` | `cross_mean(day_std(Amt), 30)` | − | 0 | **+12.6% / +22.3%** | +1.78 / +3.46 | +15.2% / +24.4% | 3.4% | 0 | +1.87 / +3.70 | +21.1% | +0.0343 / +0.0565 | 1.00 / 1.00 |
| `f_known30r` | `cs_rank(cross_mean(day_std(Amt), 30))` | − | 0 | **+12.6% / +22.3%** | +1.78 / +3.46 | +15.2% / +24.4% | 3.4% | 0 | +1.87 / +3.70 | +21.1% | +0.0343 / +0.0565 | 1.00 / 1.00 |
| `f_excl_blown15` | `add(cs_rank(cross_mean(day_std(Amt), 30)), mul(cross_max(mul(greate...` | − | 0 | **+14.3% / +22.9%** | +2.05 / +3.57 | +16.9% / +25.1% | 3.5% | 0 | +3.39 / +4.78 | +36.6% | +0.0407 / +0.0594 | 1.00 / 1.00 |
| `f_excl_lu15` | `add(cs_rank(cross_mean(day_std(Amt), 30)), mul(cross_max(mul(sub(cr...` | − | 1 | **+15.2% / +23.5%** | +2.16 / +3.64 | +17.4% / +25.4% | 2.9% | 0 | +2.91 / +4.74 | +40.2% | +0.0459 / +0.0630 | 1.00 / 1.00 |

**变体之间(以及与控制变量)的日截面 rank 相关(fit 段;变体用的是实际交易的信号,控制变量是原始面板)** — ≥0.95 在 AlphaCube 里算同一因子族

| | `a_right` | `a_left` | `a_sum` | `a_abs` | `a_regular` | `a_eps3` | `a_flag` | `a_rankfirst` | `a_lockshare` | `a_limitup` | `f_orig` | `f_known30` | `f_known30r` | `f_excl_blown15` | `f_excl_lu15` | `ctl_amt` | `ctl_cap` | `ctl_turnrate` | `ctl_ivol` | `ctl_dvol20` | `ctl_price` | `ctl_rev1` | `ctl_mom20` | `known_amt_max9` | `known_stdamt_max9` | `known_ivol_max9` | `known_stdamt_mean30` | `g_max30` | `g_limitup30` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `a_right` | +1.00 | +0.76 | +0.95 | +0.85 | +0.26 | +0.56 | +0.67 | +0.35 | -0.44 | +0.09 | +0.63 | -0.08 | -0.08 | +0.03 | +0.04 | +0.14 | +0.40 | -0.25 | -0.14 | -0.22 | +0.24 | +0.01 | -0.00 | +0.11 | +0.05 | -0.26 | +0.08 | -0.21 | -0.31 |
| `a_left` | +0.76 | +1.00 | +0.86 | +0.73 | +0.04 | +0.22 | +0.63 | +0.10 | -0.38 | +0.06 | +0.19 | -0.09 | -0.09 | +0.02 | +0.01 | +0.14 | +0.32 | -0.18 | -0.14 | -0.21 | +0.20 | +0.02 | +0.00 | +0.12 | +0.06 | -0.24 | +0.09 | -0.18 | -0.28 |
| `a_sum` | +0.95 | +0.86 | +1.00 | +0.90 | +0.15 | +0.45 | +0.73 | +0.25 | -0.47 | +0.10 | +0.47 | -0.07 | -0.07 | +0.06 | +0.06 | +0.13 | +0.39 | -0.26 | -0.16 | -0.25 | +0.23 | +0.02 | -0.00 | +0.10 | +0.04 | -0.28 | +0.07 | -0.23 | -0.34 |
| `a_abs` | +0.85 | +0.73 | +0.90 | +1.00 | +0.19 | +0.48 | +0.74 | +0.29 | -0.55 | +0.10 | +0.49 | -0.04 | -0.04 | +0.08 | +0.08 | +0.10 | +0.31 | -0.20 | -0.15 | -0.19 | +0.27 | +0.01 | +0.00 | +0.08 | +0.02 | -0.24 | +0.04 | -0.18 | -0.33 |
| `a_regular` | +0.26 | +0.04 | +0.15 | +0.19 | +1.00 | +0.71 | +0.09 | +0.84 | -0.07 | +0.01 | +0.43 | -0.01 | -0.01 | -0.01 | +0.01 | +0.03 | +0.12 | -0.11 | -0.03 | -0.02 | +0.13 | -0.01 | -0.02 | +0.02 | -0.01 | -0.07 | +0.01 | -0.03 | -0.03 |
| `a_eps3` | +0.56 | +0.22 | +0.45 | +0.48 | +0.71 | +1.00 | +0.38 | +0.78 | -0.28 | +0.08 | +0.72 | +0.10 | +0.10 | +0.16 | +0.18 | -0.06 | +0.25 | -0.32 | -0.16 | -0.24 | +0.14 | -0.01 | -0.08 | -0.08 | -0.12 | -0.24 | -0.10 | -0.23 | -0.26 |
| `a_flag` | +0.67 | +0.63 | +0.73 | +0.74 | +0.09 | +0.38 | +1.00 | +0.18 | -0.60 | +0.13 | +0.37 | +0.08 | +0.08 | +0.21 | +0.20 | -0.00 | +0.27 | -0.28 | -0.23 | -0.32 | +0.17 | +0.01 | -0.03 | -0.03 | -0.08 | -0.31 | -0.08 | -0.30 | -0.42 |
| `a_rankfirst` | +0.35 | +0.10 | +0.25 | +0.29 | +0.84 | +0.78 | +0.18 | +1.00 | -0.12 | +0.04 | +0.48 | +0.03 | +0.03 | +0.05 | +0.06 | -0.01 | +0.16 | -0.18 | -0.04 | -0.08 | +0.14 | -0.02 | -0.04 | -0.02 | -0.05 | -0.10 | -0.03 | -0.08 | -0.10 |
| `a_lockshare` | -0.44 | -0.38 | -0.47 | -0.55 | -0.07 | -0.28 | -0.60 | -0.12 | +1.00 | -0.15 | -0.27 | -0.00 | -0.00 | -0.10 | -0.17 | -0.08 | -0.17 | +0.09 | +0.30 | +0.17 | -0.30 | -0.00 | +0.07 | -0.05 | +0.03 | +0.32 | +0.00 | +0.21 | +0.51 |
| `a_limitup` | +0.09 | +0.06 | +0.10 | +0.10 | +0.01 | +0.08 | +0.13 | +0.04 | -0.15 | +1.00 | +0.06 | +0.04 | +0.04 | +0.11 | +0.16 | -0.09 | +0.02 | -0.12 | -0.10 | -0.12 | -0.00 | -0.20 | -0.13 | -0.07 | -0.11 | -0.12 | -0.04 | -0.15 | -0.24 |
| `f_orig` | +0.63 | +0.19 | +0.47 | +0.49 | +0.43 | +0.72 | +0.37 | +0.48 | -0.27 | +0.06 | +1.00 | +0.01 | +0.01 | +0.06 | +0.07 | +0.03 | +0.24 | -0.20 | -0.09 | -0.14 | +0.15 | +0.00 | -0.01 | +0.02 | -0.01 | -0.15 | -0.01 | -0.13 | -0.19 |
| `f_known30` | -0.08 | -0.09 | -0.07 | -0.04 | -0.01 | +0.10 | +0.08 | +0.03 | -0.00 | +0.04 | +0.01 | +1.00 | +1.00 | +0.92 | +0.89 | -0.89 | -0.54 | -0.42 | -0.21 | -0.51 | -0.42 | +0.03 | -0.09 | -0.92 | -0.87 | -0.22 | -1.00 | -0.48 | -0.36 |
| `f_known30r` | -0.08 | -0.09 | -0.07 | -0.04 | -0.01 | +0.10 | +0.08 | +0.03 | -0.00 | +0.04 | +0.01 | +1.00 | +1.00 | +0.92 | +0.89 | -0.89 | -0.54 | -0.42 | -0.21 | -0.51 | -0.42 | +0.03 | -0.09 | -0.92 | -0.87 | -0.22 | -1.00 | -0.48 | -0.36 |
| `f_excl_blown15` | +0.03 | +0.02 | +0.06 | +0.08 | -0.01 | +0.16 | +0.21 | +0.05 | -0.10 | +0.11 | +0.06 | +0.92 | +0.92 | +1.00 | +0.89 | -0.82 | -0.46 | -0.42 | -0.24 | -0.54 | -0.36 | +0.02 | -0.13 | -0.86 | -0.84 | -0.28 | -0.92 | -0.51 | -0.43 |
| `f_excl_lu15` | +0.04 | +0.01 | +0.06 | +0.08 | +0.01 | +0.18 | +0.20 | +0.06 | -0.17 | +0.16 | +0.07 | +0.89 | +0.89 | +0.89 | +1.00 | -0.80 | -0.40 | -0.47 | -0.28 | -0.63 | -0.34 | +0.02 | -0.19 | -0.85 | -0.84 | -0.34 | -0.89 | -0.62 | -0.61 |
| `ctl_amt` | +0.14 | +0.14 | +0.13 | +0.10 | +0.03 | -0.06 | -0.00 | -0.01 | -0.08 | -0.09 | +0.03 | -0.89 | -0.89 | -0.82 | -0.80 | +1.00 | +0.56 | +0.53 | +0.32 | +0.47 | +0.45 | +0.05 | +0.25 | +0.93 | +0.89 | +0.24 | +0.89 | +0.41 | +0.28 |
| `ctl_cap` | +0.40 | +0.32 | +0.39 | +0.31 | +0.12 | +0.25 | +0.27 | +0.16 | -0.17 | +0.02 | +0.24 | -0.54 | -0.54 | -0.46 | -0.40 | +0.56 | +1.00 | -0.34 | -0.06 | -0.08 | +0.42 | +0.02 | +0.09 | +0.54 | +0.49 | -0.18 | +0.54 | -0.03 | -0.06 |
| `ctl_turnrate` | -0.25 | -0.18 | -0.26 | -0.20 | -0.11 | -0.32 | -0.28 | -0.18 | +0.09 | -0.12 | -0.20 | -0.42 | -0.42 | -0.42 | -0.47 | +0.53 | -0.34 | +1.00 | +0.46 | +0.64 | +0.10 | +0.04 | +0.20 | +0.47 | +0.47 | +0.47 | +0.42 | +0.51 | +0.38 |
| `ctl_ivol` | -0.14 | -0.14 | -0.16 | -0.15 | -0.03 | -0.16 | -0.23 | -0.04 | +0.30 | -0.10 | -0.09 | -0.21 | -0.21 | -0.24 | -0.28 | +0.32 | -0.06 | +0.46 | +1.00 | +0.48 | +0.01 | +0.08 | +0.29 | +0.25 | +0.30 | +0.70 | +0.21 | +0.41 | +0.32 |
| `ctl_dvol20` | -0.22 | -0.21 | -0.25 | -0.19 | -0.02 | -0.24 | -0.32 | -0.08 | +0.17 | -0.12 | -0.14 | -0.51 | -0.51 | -0.54 | -0.63 | +0.47 | -0.08 | +0.64 | +0.48 | +1.00 | +0.18 | -0.03 | +0.19 | +0.53 | +0.53 | +0.61 | +0.51 | +0.79 | +0.56 |
| `ctl_price` | +0.24 | +0.20 | +0.23 | +0.27 | +0.13 | +0.14 | +0.17 | +0.14 | -0.30 | -0.00 | +0.15 | -0.42 | -0.42 | -0.36 | -0.34 | +0.45 | +0.42 | +0.10 | +0.01 | +0.18 | +1.00 | +0.02 | +0.09 | +0.44 | +0.38 | -0.01 | +0.42 | +0.16 | +0.02 |
| `ctl_rev1` | +0.01 | +0.02 | +0.02 | +0.01 | -0.01 | -0.01 | +0.01 | -0.02 | -0.00 | -0.20 | +0.00 | +0.03 | +0.03 | +0.02 | +0.02 | +0.05 | +0.02 | +0.04 | +0.08 | -0.03 | +0.02 | +1.00 | +0.16 | -0.02 | -0.02 | -0.03 | -0.03 | +0.00 | -0.01 |
| `ctl_mom20` | -0.00 | +0.00 | -0.00 | +0.00 | -0.02 | -0.08 | -0.03 | -0.04 | +0.07 | -0.13 | -0.01 | -0.09 | -0.09 | -0.13 | -0.19 | +0.25 | +0.09 | +0.20 | +0.29 | +0.19 | +0.09 | +0.16 | +1.00 | +0.24 | +0.27 | +0.28 | +0.09 | +0.25 | +0.21 |
| `known_amt_max9` | +0.11 | +0.12 | +0.10 | +0.08 | +0.02 | -0.08 | -0.03 | -0.02 | -0.05 | -0.07 | +0.02 | -0.92 | -0.92 | -0.86 | -0.85 | +0.93 | +0.54 | +0.47 | +0.25 | +0.53 | +0.44 | -0.02 | +0.24 | +1.00 | +0.96 | +0.31 | +0.92 | +0.46 | +0.33 |
| `known_stdamt_max9` | +0.05 | +0.06 | +0.04 | +0.02 | -0.01 | -0.12 | -0.08 | -0.05 | +0.03 | -0.11 | -0.01 | -0.87 | -0.87 | -0.84 | -0.84 | +0.89 | +0.49 | +0.47 | +0.30 | +0.53 | +0.38 | -0.02 | +0.27 | +0.96 | +1.00 | +0.39 | +0.87 | +0.47 | +0.36 |
| `known_ivol_max9` | -0.26 | -0.24 | -0.28 | -0.24 | -0.07 | -0.24 | -0.31 | -0.10 | +0.32 | -0.12 | -0.15 | -0.22 | -0.22 | -0.28 | -0.34 | +0.24 | -0.18 | +0.47 | +0.70 | +0.61 | -0.01 | -0.03 | +0.28 | +0.31 | +0.39 | +1.00 | +0.22 | +0.52 | +0.42 |
| `known_stdamt_mean30` | +0.08 | +0.09 | +0.07 | +0.04 | +0.01 | -0.10 | -0.08 | -0.03 | +0.00 | -0.04 | -0.01 | -1.00 | -1.00 | -0.92 | -0.89 | +0.89 | +0.54 | +0.42 | +0.21 | +0.51 | +0.42 | -0.03 | +0.09 | +0.92 | +0.87 | +0.22 | +1.00 | +0.48 | +0.36 |
| `g_max30` | -0.21 | -0.18 | -0.23 | -0.18 | -0.03 | -0.23 | -0.30 | -0.08 | +0.21 | -0.15 | -0.13 | -0.48 | -0.48 | -0.51 | -0.62 | +0.41 | -0.03 | +0.51 | +0.41 | +0.79 | +0.16 | +0.00 | +0.25 | +0.46 | +0.47 | +0.52 | +0.48 | +1.00 | +0.68 |
| `g_limitup30` | -0.31 | -0.28 | -0.34 | -0.33 | -0.03 | -0.26 | -0.42 | -0.10 | +0.51 | -0.24 | -0.19 | -0.36 | -0.36 | -0.43 | -0.61 | +0.28 | -0.06 | +0.38 | +0.32 | +0.56 | +0.02 | -0.01 | +0.21 | +0.33 | +0.36 | +0.42 | +0.36 | +0.68 | +1.00 |

# 08 — 怎么读变体总表(哪些变体其实是同一个东西,哪些容易张冠李戴)

> 报告里的总表会把所有阶段的变体拼在一起。这一页是读那张表的说明书。**先读这页,再读表**,否则很容易把两个不同口径的数字当成同一行。

---

## 1. 两套书,别混:`books`(决策口径) vs `books_user`(用户口径)

| | 方向 / 半衰期在哪一段拟合 | 报哪些段 |
|---|---|---|
| `books` | **train**(20180102–20211231) | train、valid |
| `books_user` | **utrain**(20180102–20230807 = 用户训练段) | utrain、**holdout**(20230808–20251231) |

- **留出段的数字只可能来自 `books_user`** —— `books` 字典里根本没有 holdout 字段。
- 同一个变体在两套书里**半衰期可能不同**:`f_excl_blown15` 在 `books` 里 hl = 0,在 `books_user` 里 hl = 1。报告引它的时候必须带口径。
- `f_orig` 和 `f_known30` 两套书的 hl 相同(20 / 0),所以这两条没有歧义 —— 报告的承重数字恰好都在这两条上,是运气也是刻意(预登记时就是按它们定的)。

## 2. 同一条因子出现在两个阶段:`S0_baseline / v_base` ≡ `S_final / f_orig`

**同一个表达式**(配置里的原式),只是分别在 S0 和 S_final 两次求值。不要当成两条候选、不要在总表里并列成「两个变体都是负的」—— 那是**同一条**。
- 两处的 `cov` 看起来不一样(S0 报 1.00,S_final 的 holdout 报 0.9675):**不是矛盾**。`cov` 是随 split 变的**面板覆盖率**,train 0.691 / valid 0.895 / utrain 0.749 / holdout 0.967,而且**五个变体完全相同** → 它是面板统计量,不是任何表达式的求值失败(`07_S_final.md` §2c)。门槛判定用 holdout 这一档。

## 3. `f_known30` 与 `f_known30r` 在 hl = 0 下是**同一本书**

`f_known30 = cross_mean(day_std(Amt), 30)`;`f_known30r = cs_rank(cross_mean(day_std(Amt), 30))`。
- 两条在 hl 0 下 Lnet/Lshp/Lgross/LTO/LS/short **逐项相同**,rank 相关(train)= 0.999999999988 ≈ **1.000**(秩等价)。
- 只有 hl > 0 时才会分开,因为 `EMA(cs_rank(x)) ≠ cs_rank(EMA(x))`(先排序再平滑 vs 先平滑再排序)—— 在 `books.sweep` 里看得见:hl20 时 known30 是 +8.39%、known30r 是 +7.83%。
- **总表里它们不算两条候选**,`f_known30r` 存在的唯一目的是给两条 `cs_rank` 写法的叠加候选做**同构基准**(否则 ΔLnet 会把「排序 vs 不排序」的差混进「排除」的功劳里)。

## 4. 两张排除标记不是同一个东西,但重叠度很高

`f_excl_blown15`(F106 自己的塌缩日标记,|X| > 5)↔ `f_excl_lu15`(朴素日线涨停:收盘 = 当日最高价且日涨幅 > 9.5%):rank 相关(train)**+0.893**。
→ 「高度重叠」是结论的一部分(C4:朴素标记可以替代),但不要写成「同一张标记」。

## 5. ⚠ 最容易张冠李戴的一处:x2 的叠加行 ≠ S_final 的叠加候选

| | 窗口 | 半衰期 | ΔLnet(train / valid) |
|---|---|---|---|
| x2 脚本的叠加行(`07x_2_longonly.md` §2) | **20 日** | **不重新拟合**(沿用基准的 sign/hl) | +1.59 / +0.52(known30) |
| S_final 的 `f_excl_blown15`(引擎口径) | **15 日** | **引擎重新拟合** | +1.63 / +0.57 |

两者**构造不同**(窗口 20 vs 15、hl 固定 vs 重拟合),数字只是**非常接近**。
- 好消息:两条独立实现互相印证(train 一点六、valid 半个点),这是结论的稳健性证据。
- 但报告**不能**把它们写成同一行、也不能互相替换引用。引 ΔLnet 时必须写清是「x2 的 20 日固定 hl 版」还是「S_final 的 15 日重拟合版」。

## 6. `S1_regime`(10 个变体)**根本没跑**,总表里这一阶段应当是空的

`exit 97` = 被服务器的内存守卫顶掉,**不是跑完以后结果不好**。它想问的问题(公布的多空夏普是塌缩日=封板事件做出来的,还是尾部形状不对称做出来的)由自写脚本 x1 答掉了。
→ **不要**把 x1 的数字填到 `S1_regime` 那 10 个变体(`a_right`、`a_left`、`a_abs`、`a_limitup`…)的行里。那些 id 在磁盘上没有任何结果。

## 7. 0/1 和小整数构造的「多头腿」是假的

`07x_2_longonly.md` §5 的短记忆**计数**构造(20 日内封板次数之类):取值几乎全是 0 → 多头十分位是在一大堆并列里**按股票代码顺序**切出来的,不是一本可交易的书,`dist` 过不了 0.5。
→ 这些行的 rank IC 可以读(H11 就是靠它),**Lnet / Lshp 不能读**。

## 8. x2 叠加行的 `LS` / `short` 不可读

x2 里的叠加是在**多头腿**上做排除,空头腿那半没有对应处理 → 那些行的多空夏普和空头腿数字没有意义。只读 `Lnet / Lshp / Lgross / LTO`。
(S_final 的 `f_excl_*` 是引擎跑的完整书,`LS`/`short` 可以读,但对纯多头用户没用;`f_excl_lu15` 的 holdout short 跳到 47.26%(utrain 33.28%)就是这类数字,别拿它说事。)

## 9. 单位约定

Lnet / Lgross / LTO / short 都是百分数;**ΔLnet 一律写 pp(个点)**,免得「+0.54%」被读成相对变化(相对 14.10% 的 0.54% 是 0.08 pp,差了一个数量级)。钱的数字全部**已扣 15 bp**。

## 9. 机制诊断

# 09 — 机制诊断(主研,2026-10-04,留出段已读之后写)

> 分三档:**已确立**(有实验指得到、且在预登记的判据下过了留出段)/ **合理但未坐实**(方向一致但没有书级或留出段证据)/ **未决**(本研究不打算定)。
> 规矩:留出段读完之后**不新增「已确立」**,也不因为留出段的数字改任何结论(playbook §6.4)。下面每一条「已确立」的核心证据都来自 train/valid,留出段只是按事前登记的判据确认它没被推翻。

---

## A. 已确立

### A1. 它读的不是「日内尾部形状」,而是「最近有没有封过涨停板、封板前那几分钟跳了多大」

字面上是「分钟收益右尾 ES/VaR 减左尾 ES/VaR」。真正决定取值的是**分母塌缩**:当日上涨分钟 ≤ 12 个时 `day_quantile(Ret, 0.95)` ≈ 0,被 `+1e-6` 接住,读数放大到 ~10⁶ 量级。
- 塌缩日里 **86.3%(train)/ 77.8%(valid)是涨停收盘**,全市场基准 1.59% → **富集约 50 倍**;不是低价股(< 3 元只占 0.2%)。出处 `07x_1_anatomy.md` A/B/C 表。
- 树里**没有任何日轴算子**,真实回看只有 1 天;时间结构全部来自口径里的因果 EMA。按用户的多头口径半衰期 hl = 20,等效记忆约一年 → 交易信号是「近一年封板史」的加权记忆。出处 `02_operators.md`、`03_decomposition.md`。
- 分母的 `1e-6` 是**要害**(带收益量纲,比一个 tick 小三个数量级);计数分母上的 `1e-6` 只是除零保护。两者不要混为一谈。

### A2. 原样对纯多头用户不可用,而且不是成本问题

多头腿净超额在半衰期网格 {0,1,2,3,5,10,20} 的**每一个点、毛和净全部为负**:train hl0 −67.22% → hl20 −6.91%;utrain hl0 −66.50% → hl20 −5.82%(`07_S_final.md` §3a/3b)。扣费前就是负的 → 不是 15bp 吃掉了收益。
- 留出段(用户测试段,**C1**):Lnet **−3.19%**、Lshp **−0.69**、Lgross **−1.38%**,三项全负;逐年 2018→2025 **八年全负**(−9.17/−6.17/−8.63/−4.12/−0.77/−6.68/−5.13/−0.43%)。
- **「原式 + 多头最优半衰期」就是用户公布的那一行本身**:hlL = hlS = 20,已经是全局网格的端点 → 这条因子没有「延长半衰期」这条免费改进可拿。

### A3. 公布的多空夏普是真的,但与多头腿无关,且一半以上靠「次日买不进的票」

- 留出段(**C2**)LS **+3.108**、Lgross **−1.38%**,与用户表 test 列(3.11 / −1.4%)**在小数点第二位内精确复现** → 「原样不可用」不是口径差异造成的。
- train 上去掉塌缩日、或 clip(±3)之后,多空夏普从 +2.82 **转负** → **常规取值区间里没有可交易信号**,钱全在塌缩日这一小块。
- 把「次日涨停/一字板买不进」的票按不可成交处理后,train 多空夏普 2.82 → **0.42**。空头腿的这个毛病**不影响多头腿的结论**:多头端恰好是「近期没封板」的票。

### A4. 分位剖面是倒 U,不是单调

train Q1 −28.4% … Q10 −5.3%;valid Q1 −22.7% … Q10 −1.8%(`07_S_final.md` §6)。两端都是近期封板股,只是封板方向/强度不同。
两条方法论后果,报告里要写:(a) **线性中性化在这条因子上看不见东西**(非单调);(b) 量折叠型结构必须用**同样折叠过的**控制变量(`07x_1_anatomy.md` D 表)。

### A5. 不是成交额水平 / 规模 / 换手 / 波动 / 动量 / 反转的另一种写法

- rank 相关(train,交易信号)`f_orig ↔ f_known30` = **+0.0055**,几乎正交(`07_S_final.md` §8)。
- corr(signal, mom20) = −0.013;十档动量的秩 0.47~0.54(全市场 0.50)。
- 折叠量对五个水平变量(成交额/市值/换手/波动/价格)**R² 仅 0.068**;对四个「近期涨停」变量 **R² 0.444**。
→ 它的真实暴露是**封板事件**,不是任何水平变量。这也是说「它是已知家族的改写」会错的原因。

### A6. 对纯多头用户,相对已知成交额家族没有可交易的增量

三条路都走过,全部否定(`07x_2_longonly.md` §2/§3/§4):
1. **相加**:`rank(known) + w·rank(F106)`,24 行(2 方向 × 3 权重 × 2 家族 × 2 段)**没有一行**好于已知家族自己,且随 w **单调下降**。
2. **中性化残差**:F106 对已知家族中性化后的残差,多头腿净超额**五行全负**(train −5.8%~−8.6%、valid −3.4%~…)。
3. **排除性叠加**(把被标记的票从已知家族多头腿里推走):方向对、机制看得见,但量不够 —— valid 只剩 **+0.57 pp**,留出段(**C3**)**+0.54 pp**,预登记门槛是 +1.5 pp、噪声是 **±3 pp**。
   换成**朴素日线涨停**标记(收盘=当日最高价且涨幅>9.5%)反而更高:留出段 **+0.75 pp**(**C4**)→ 要这个排除效果,一个日线涨停标记就够,不需要这棵树。

### A7. 增量的天花板是结构性的,可以事先算出来 —— **这是整条研究解释力最强的一句话**

ΔLnet ≈ (被标记票占已知家族多头十分位的比例) × (标记票与未标记票的次日超额之差)。
代入得 2.0 / 0.70 / 1.93 / 0.57,实测 +1.59 / +0.52 / +1.60 / +0.40(known30/known9 × train/valid)—— **四格全部吻合到 25% 以内**。
share 之所以小,是因为**已知家族本来就在躲这些票**:被标记票占全市场 8.0%/6.7%,但只占 known30 多头十分位 5.1%/2.2%、known9 的 4.1%/1.6% → 相对持有频率只有 **24%~64%**(涨停标记 15%~37%)。
→ **不是 F106 的「不要买」清单不准,是已知家族本来就没买那些票。这张清单是多余的。**
机制那一半是**成立**的(被标记票次日超额四格全部远差于未标记票),所以这不是「因子没信息」,是「这点信息已经被已知家族隐含地用掉了」。

### A8. 已知家族在用户的测试段上仍然成立(第一推荐站得住)

`f_known30 = cross_mean(day_std(Amt), 30)` 留出段 Lnet **+14.10%**、Lshp **+1.51**(**C5**),落在用户给的 +13%~+15% / 1.4~1.9 区间内;逐年 2018→2025 **八年全正**。

### A9. 门槛不是问题

五条候选留出段 cov 全部 **0.9675**、dist 全部 ≥ **0.9933**(**C6**)。没有一条是被门槛判死的 —— 否定结论靠的是钱,不是可用性。

---

## B. 合理但未坐实

### B1. 半衰期错配给 +0.54 pp 带来的偏差只有零点几个点,方向还不定

留出段**没有**固定半衰期表(引擎只在拟合段扫 hl),所以 C3/C4 读的是「引擎各自拟合的 hl」(叠加 hl 1 对基准 hl 0)。
在**有**网格的两段上可以量这个错配有多大(只用拟合段的 hl 敏感性,**不是**把拟合段的数当成 holdout 的数):
utrain 上 own-hl Δ = 16.71 − 15.40 = **+1.31 pp**;同 hl0 Δ = 16.73 − 15.40 = **+1.33 pp**;同 hl1 Δ = 16.71 − 15.00 = **+1.71 pp**。
→ 错配的量级 **≲ 0.4 pp**,而且在 utrain 上 own-hl 读数比同 hl0 的干净对照**还低 0.02 pp**。
**所以把 +0.54 pp 单方向地叫「上界」是不准的**(`results/R2.md` 和 `07_S_final.md` 的措辞偏保守);更准确的写法是:**错配污染的量级 ≲0.4 pp、符号不定**。无论取哪个方向,+0.54 pp 都远在 +1.5 pp 门槛和 ±3 pp 噪声之下 → **C3 的裁决不变**。
未坐实的原因:这是从拟合段的 hl 敏感性外推的,留出段的网格拿不到了。

### B2. 排除的价值随半衰期上升,这与机制一致,但不产生候选

utrain 上 Δ(hl0) = +1.33 pp,Δ(hl20) = 14.83 − 11.32 = **+3.51 pp**。书越旧,越会抱着刚封过板的票不放 → 排除越值钱,方向与 A1 的机制完全一致。
**但绝对水平更差**:叠加在 hl20 只有 14.83% < 已知家族在 hl0 的 15.40% → 没有一个 (hl, 叠加) 组合能赢过「已知家族 + 它自己的最优 hl」。这条只是机制的旁证,不是一条路。

### B3. 记忆长度错配(H11):效应约 20 天,EMA-20 记了约一年

事件效应约 20 个交易日、40 天归零;显式短记忆的**计数构造** rank IC 是 EMA-20(X) 的 **1.7~4.8 倍、两段全优**,20 日窗口在叠加里四格全面优于 60 日。
未坐实的原因:优势只出现在**取值几乎全是 0** 的计数构造上,过不了 `dist ≥ 0.5`(多头端是并列里按股票代码切出来的 10%,不是一本可交易的书);三条连续构造的 rank IC 反而低于原式。**修好记忆不产生候选**,这是诊断,不是升华路线。

### B4. H13:真正值钱的那个标记是新股过滤器,不是这条因子

`listed < 250d` 是 36 格里**唯一四格全部 ≥ 1 个点**的标记(+1.60 / +1.09 / +1.90 / +1.95)。
未坐实的原因:(a) 它与这棵树无关,是独立的过滤器;(b) 它来自一个 9 标记 × 2 家族 × 2 段的宽搜索,有多重比较风险;(c) 两段的符号/量级有异常。→ 写进 `12_next.md`,本研究不验。

### B5. 「买不进」占公布多空夏普的比例

train 2.82 → 0.42(约 85%)用的是一套次日涨停/一字板近似。量级可靠(去掉塌缩日也独立地把多空夏普打到转负),**精确比例**没有在留出段重算。

---

## C. 未决(本研究不打算定,也不影响结论)

1. **`diagnostics.by_year` 用的是哪一套半衰期** —— JSON 里没有字段标注(`fit = train`、`rank_corr_on` 写的是单数「the fitted half-life」,倾向 `books` 口径);`f_excl_blown15` 是唯一两套 hl 不同的变体,它的数字恰好落在两种假设中间,分不开。**不影响** `f_orig` / `f_known30` 的逐年读数(这两条两套 hl 相同,无歧义)。
2. **留出段的分位剖面和固定半衰期表** —— 引擎没算(`profile` 只有 train/valid,`f_known30r` / `f_excl_lu15` 连这个字段都没有;`sweep` 只在拟合段)。**不能靠重跑补 —— 重跑就是第二次读留出段。** 所以「留出段上是否仍然倒 U」**没有数据可看**,报告要照实写「缺」。
3. **`S1_regime` 阶段**(10 个变体)被内存守卫顶掉,**exit 97 = 根本没跑**。它想问的「塌缩日 vs 尾部形状」已经由自写脚本 x1 答掉了(A1/A3),但没有引擎口径的书级数字。报告的总表里这一阶段**应当是空的**。
4. **折叠(左尾取 abs)单独贡献多少** —— H8 已确立两侧不对等、不是镜像,但没有把「折叠」这一步单独量到书级。

---

## 一句话

三件事都已确立,并且在用户的测试段上按事前登记的判据验过:**它是什么**(封板记忆,A1)、**原样不可用**(留出段多头腿 −3.19%,A2)、**相对已知家族没有可交易的增量**(留出段 Δ +0.54 pp,天花板可算,A6/A7)。结论类型 = **分辨**。

## 10. 蒸馏 / 升华后的候选

**最终对比,与用户表同口径**(留出段 = 用户的测试段;多头口径 = 半衰期按纯多头书在用户训练段上选)

| 结构 | 方向 | 半衰期(多头) | **多头腿净超额** 训练/测试 | 纯多头夏普 训练/测试 | 多头腿毛超额 训练/测试 | 多头日换手 | 半衰期(多空) | 扣费多空夏普 训练/测试 | 多头腿毛超额@多空半衰期 训练/测试 | 空头腿毛超额 训练/测试 |
|---|---|---|---|---|---|---|---|---|---|---|
| _用户表里公布的原式(多空口径)_ | − | — | — | — | — | — | 20 | +2.91 / +3.11 | -4.2% / -1.4% | — |
| `f_orig` `sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(...` | − | 20 | **-5.8% / -3.2%** | -1.91 / -0.69 | -4.2% / -1.4% | 2.2% | 20 | +2.91 / +3.11 | -4.2% / -1.4% | +26.3% / +24.7% |
| `f_known30` `cross_mean(day_std(Amt), 30)` | − | 0 | **+15.4% / +14.1%** | +2.22 / +1.51 | +17.8% / +16.2% | 3.2% | 0 | +2.33 / +1.94 | +17.8% / +16.2% | +24.7% / +24.9% |
| `f_known30r` `cs_rank(cross_mean(day_std(Amt), 30))` | − | 0 | **+15.4% / +14.1%** | +2.22 / +1.51 | +17.8% / +16.2% | 3.2% | 0 | +2.33 / +1.94 | +17.8% / +16.2% | +24.7% / +24.9% |
| `f_excl_blown15` `add(cs_rank(cross_mean(day_std(Amt), 30)), mul(cross_max(...` | − | 1 | **+16.7% / +14.6%** | +2.47 / +1.57 | +18.8% / +16.6% | 2.8% | 0 | +3.75 / +3.37 | +19.2% / +16.9% | +37.2% / +40.7% |
| `f_excl_lu15` `add(cs_rank(cross_mean(day_std(Amt), 30)), mul(cross_max(...` | − | 1 | **+17.6% / +14.9%** | +2.55 / +1.60 | +19.7% / +16.7% | 2.8% | 0 | +3.32 / +3.65 | +19.6% / +16.9% | +41.3% / +52.0% |

**最终候选逐年**(含留出段年份;方向与半衰期是用户训练段上定的)

| 变体 | 指标 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|
| `f_orig` | 多头腿净超额 | -9.2% | -6.2% | -8.6% | -4.1% | -0.8% | -6.7% | -5.1% | -0.4% |
| | 扣费多空夏普 | +1.82 | +4.17 | +3.25 | +2.33 | +3.22 | +1.99 | +3.70 | +3.37 |
| `f_known30` | 多头腿净超额 | +17.3% | +10.2% | +6.6% | +16.0% | +24.6% | +21.2% | +9.2% | +14.3% |
| | 扣费多空夏普 | +3.01 | +1.84 | +0.66 | +2.18 | +4.22 | +3.75 | +1.45 | +1.60 |
| `f_known30r` | 多头腿净超额 | +17.3% | +10.2% | +6.6% | +16.0% | +24.6% | +21.2% | +9.2% | +14.3% |
| | 扣费多空夏普 | +3.01 | +1.84 | +0.66 | +2.18 | +4.22 | +3.75 | +1.45 | +1.60 |
| `f_excl_blown15` | 多头腿净超额 | +19.2% | +11.3% | +9.1% | +16.5% | +25.5% | +21.7% | +10.0% | +14.6% |
| | 扣费多空夏普 | +4.44 | +4.37 | +2.17 | +2.79 | +5.69 | +4.38 | +3.13 | +2.65 |
| `f_excl_lu15` | 多头腿净超额 | +20.5% | +12.9% | +9.0% | +17.9% | +26.3% | +21.8% | +9.6% | +15.4% |
| | 扣费多空夏普 | +3.52 | +3.53 | +1.70 | +1.93 | +4.61 | +4.64 | +3.16 | +3.25 |

# 10 — 最终候选、排序与判据

---

## 读留出段之前(主研第 2 轮写,2026-10-04;写在 `study.sh final` 之前,之后一个字不改)

> 这一节是**事前登记**。留出段(20230808–20251231 = 用户的测试段)整个研究只读一次。
> 下面的候选集合、排序、判据,**只用 train(20180102–20211231)和 valid(20220101–20230807)的证据**定出来。
> 读完之后另起一节「读完留出段之后」,逐条写判据过了还是被否定;**推荐就是下面的第一推荐,被否定就写被否定**(playbook §6.4)。

### 这条研究的结论类型:**分辨**(不是提纯、不是升华)

**没有任何 F106 变体进入推荐。** 理由(全部来自 train/valid,出处见 `state.md` §2、`05_hypotheses.md` 裁决):

1. 原式的多头腿净超额在**半衰期网格的每一个点**(0/1/2/3/5/10/20)、train 和 valid、**毛和净全都是负的**
   (train −67.2% → −6.9%,valid −3.2%);分位剖面是**倒 U**(train Q1 −28.4%、Q10 −5.3%),两端都是近期封板股。
2. 「原式 + 多头最优半衰期」**就是用户表里公布的那一行本身**(hlL = hlS = 20)—— 这条因子没有「延长半衰期」这条免费改进。
3. 这棵树派生出的**所有连续构造**(只留常规日 / 先排序再 EMA / clip(±3) / 只留 R / 只留 L / 折叠 / log(1+\|X\|) / R+L / log(1+R+L)),
   多头腿净超额在 train 和 valid **同时为正的一个都没有**。
4. 和已知家族相加:24 行(2 方向 × 3 权重 × 2 家族 × 2 段)**没有一行**好于已知家族自己,且随权重单调下降。
5. 排除性叠加(H10):方向对、机制看得见,但 **valid 上只剩 +0.4~+0.5 个点**,而噪声是 **±3 个点**;
   而且天花板是结构性的 —— 已知家族持有被标记票的频率只有全市场的 24%~64%,**它本来就在躲这些票**。
6. 唯一在 valid 上拿到一个点以上的标记是 `listed < 250d`(+1.09 / +1.95)——**那是新股过滤器,不是这条因子的功劳**。

### 最终候选(5 条,排序 = 第一推荐在前)

| 名次 | id | 是什么 | train / valid 多头口径(已有数字) | 为什么在表里 |
|---|---|---|---|---|
| **1** | `f_known30` | `cross_mean(day_std(Amt), 30)` —— **已知家族基准**(规则要求必含) | sign −1、hlL **0**;Lnet **+12.6% / +22.3%**;Lshp **+1.78 / +3.46**;LTO 3.4% / 2.8% | **第一推荐,但它不是这条因子的产物。** 对只能做多的用户,这条研究唯一可操作的输出是「F106 不要进书,继续用已知家族」。留出段要确认这本书在用户的测试段上仍然成立(用户给的参考:+13%~+15%、夏普 1.4~1.9) |
| 2 | `f_known30r` | `cs_rank(cross_mean(day_std(Amt), 30))` | 与 `f_known30` 在 **hl 0 下是同一本书**(秩等价、不平滑);hl > 0 时不同(playbook:先 EMA 再排序,`EMA(cs_rank(x))` ≠ `cs_rank(EMA(x))`) | 两条叠加候选的**同构基准**。叠加候选里有 `cs_rank`,不单独有这一行就没法做同口径的 ΔLnet |
| 3 | `f_excl_blown15` | `f_known30r` 的多头腿里把「近 15 日出现过塌缩日(\|X\| > 5)」的票推到最短端 —— **F106 自己的事件** | x2 的 20 日版(hl 不重拟合):ΔLnet **+1.59 / +0.52**(known30)、+1.60 / +0.40(known9) | **不推荐。** 列进来是为了检验我「train 的 +1.6 是这一段独有的、valid 只剩 +0.5、在噪声里」这个判断对不对 |
| 4 | `f_excl_lu15` | 同上,但标记换成**朴素日线涨停**(收盘 = 当日最高价且日涨幅 > 9.5%) | x2 的 20 日版:ΔLnet **+1.92 / +0.50**(known30)、+1.89 / **−0.04**(known9) | **不推荐。** 回答 H12 在用户的测试段上:要这个排除效果,一个日线涨停标记够不够 |
| **5** | `f_orig` | **原式**(规则要求必含;表达式见 `configs/F106_erm_mag_gap_1m.yaml`) | sign −1、hlL = hlS = **20**;Lnet **−6.91% / −3.16%**;Lshp **−2.15 / −1.23**;Lgross −5.09% / −1.81%;LS +2.82 / +3.24 | **明确不推荐。** 排在最后不是凑数:留出段上它的多头腿是不是还是负的,就是这份报告的中心结论 |

**为什么不列 `cross_max(day_std(Amt), 9)`(另一条已知家族)**:它在 train/valid 上给出的结论与 known30 完全一致
(自身 +13.7%/+22.2%,叠加 ΔLnet 同样是 train 一点几、valid 零点几),再占一个名额不会增加信息;
把名额留给「F106 标记 vs 朴素标记」这个对比更有用。known9 的数字在 `07x_2_longonly.md` 第 1~3 节里,报告可以直接引。

**为什么不列任何「短记忆计数」候选**:它们的 rank IC 确实是原式的 1.7~4.8 倍(H11 被支持),
但取值几乎全是 0 → **过不了用户的 `dist ≥ 0.5` 门槛**,多头端是并列里按股票代码顺序切出来的 10%,不是一本可交易的书。
修好记忆不产生候选,这是诊断结论,不是升华路线。

### 判据(留出段出现什么结果算「被否定」)

| 编号 | 事前判断(只凭 train/valid) | 留出段上**什么结果算它被否定** |
|---|---|---|
| **C1** | **原式的多头腿在留出段仍然是负的**(多头口径,净和毛都负;纯多头夏普也负) | `f_orig` 的 holdout **Lnet > 0 且 Lshp > 0** → C1 被否定,「原样不可用」这个中心结论错了,报告必须改写 |
| **C2** | 原式的多空夏普在留出段仍为正(用户表公布 test = 3.11),但那和多头腿无关、且有一部分是「买不进的票」撑的 | `f_orig` 的 holdout **LS < 0** → 用户表的 test 列没复现,报告里要专门写一段(**不改推荐**,因为推荐本来就不靠多空) |
| **C3** | **F106 自己的排除叠加没有真增量**:`f_excl_blown15` 相对 `f_known30r` 的 ΔLnet 在留出段 **< +1.5 个点**(**在同一个半衰期下比,优先读固定半衰期表的 hl 0 行**) | ΔLnet **≥ +1.5 个点** → C3 被否定:我把 train 的 +1.6 判成噪声是错的,排除性增量是真的,报告要改成「F106 作为已知家族多头书的排除项有增量」 |
| **C4** | **朴素涨停标记不差于 F106 自己的标记**(H12 操作版):两者 ΔLnet 之差在 1 个点以内 | `f_excl_lu15` 的 ΔLnet 比 `f_excl_blown15` **低 1.0 个点以上** → C4 被否定:F106 的「封得死 + 跳多大」确实有朴素标记拿不到的东西,报告要写「朴素标记不能替代」 |
| **C5** | **已知家族在留出段仍是一本好的纯多头书**(用户参考:+13%~+15%、夏普 1.4~1.9) | `f_known30` 的 holdout **Lnet < +5%** 或 **Lshp < 0.8** → 第一推荐被否定,报告要写「连已知家族在用户的测试段上也不成立」,并把这当成对整批研究的警告 |
| **C6** | 门槛:`f_orig`、`f_known30` 两道门槛都过(S0 已知 `f_orig` cov 1.00 / dist 0.993) | 任何候选 **cov < 0.95 或 dist < 0.5** → 照实写它过不了,**不替它找借口、不换算法**。叠加候选过不了门槛就直接写「这个构造不可交易」 |

**噪声口径(playbook §4.6,写在这里免得读完之后改口)**:测试段上多头腿净超额 **±3 个点**、纯多头夏普 **±0.3**、多空夏普 **±0.3**。
所以 C3 的门槛定在 +1.5 个点(半个噪声)而不是 +0.5:**+0.5 个点的差别在这个段上读不出来**,
如果留出段的 ΔLnet 落在 0~+1.5 之间,结论仍然是「没有可交易的增量」,不算 C3 被否定。

### 读的方式(写给执行,也写给下一轮的我自己)

- 一次 `study.sh final F106_erm_mag_gap_1m S_final_tag S_final`,**只跑这一次**。跑之前必须先 `study.sh check` 过。
- 要同时带回**多头口径和多空口径**两套数字(`final.json` 里都有,读它们不算第二次读)、**固定半衰期表**、
  `cov` / `dist`、逐年、分位剖面。
- **ΔLnet 一律在同一个半衰期下算**(优先 hl 0 行):`f_excl_*` 和 `f_known30r` 如果被引擎拟合到不同的半衰期,
  直接相减会把「平滑的功劳」记到「排除」头上(playbook §6.1)。

---

## 读完留出段之后(主研写,2026-10-04;留出段读过**一次**:`S_final`,10-04 15:35,exit 0,`ledger.json` 里 `holdout {reads: 1, expressions: 5}`)

> 上面那一节是事前登记,**一个字没改**(14:59 写,早于 15:29 启动 `final`)。下面逐条对判据。
> 数字全部来自 `runs/F106_erm_mag_gap_1m/S_final.json`,完整表在 `07_S_final.md`,执行的核对记录在 `results/R2.md`。
> **holdout 一律读 `books_user`**(方向/半衰期在 utrain = 用户训练段上拟合);`books` 字典没有 holdout 字段。

### 留出段主表(20230808–20251231,581 个交易日;用户口径)

| id | sign | hlL | **Lnet** | Lgross | **Lshp** | LTO | LS | dist | cov |
|---|---|---|---|---|---|---|---|---|---|
| `f_known30`(第一推荐,已知家族) | −1 | 0 | **+14.10%** | +16.24% | **+1.51** | 2.83% | +1.94 | 1.000 | 0.967 |
| `f_known30r`(cs_rank 版,同构基准) | −1 | 0 | +14.10%(**与上行逐项相同**) | +16.24% | +1.51 | 2.83% | +1.94 | 1.000 | 0.967 |
| `f_excl_blown15`(F106 标记叠加) | −1 | 1 | +14.64% | +16.57% | +1.57 | 2.55% | +3.29 | 1.000 | 0.967 |
| `f_excl_lu15`(朴素涨停叠加) | −1 | 1 | +14.85% | +16.74% | +1.60 | 2.49% | +3.52 | 1.000 | 0.967 |
| `f_orig`(**原式**) | −1 | 20 | **−3.19%** | −1.38% | **−0.69** | 2.40% | **+3.11** | 0.993 | 0.967 |

### 判据逐条裁决

| 编号 | 事前判断 | 留出段实测 | 裁决 |
|---|---|---|---|
| **C1** | 原式多头腿仍为负(净、毛、纯多头夏普都负) | Lnet **−3.19%**、Lgross **−1.38%**、Lshp **−0.69**,三项全负;干净整年 2024 **−5.13%**、2025 **−0.43%**;逐年 2018→2025 **八年全负** | **成立**(否定条件是 Lnet>0 **且** Lshp>0 —— 没发生)。中心结论站住 |
| **C2** | 多空夏普仍为正,但与多头腿无关 | LS **+3.108**;与用户表 test 列(3.11 / 毛 −1.4%)在小数点第二位内**精确复现**(实测毛 −1.38%) | **成立**(否定条件是 LS<0 —— 没发生)。推荐本来不靠多空,不改推荐 |
| **C3** | F106 自己的排除叠加 ΔLnet **< +1.5 pp** | **+0.54 pp**(14.64 − 14.10),与 valid 的 +0.57 pp 一致 | **成立**。落在预登记写明的「0 ~ +1.5 之间仍判没有可交易增量」区间里 |
| **C4** | 朴素涨停标记不差于 F106 自己的标记(差 ≤ 1 pp) | 朴素 **+0.75 pp** > 自己的 **+0.54 pp** —— 朴素反而**高 0.21 pp** | **成立**(否定条件是朴素低 1.0 pp 以上 —— 没发生)。朴素标记可以替代 |
| **C5** | 已知家族仍是一本好的纯多头书(+13~15% / 夏普 1.4~1.9) | **+14.10% / +1.51**,落在区间内;逐年八年全正 | **成立**。第一推荐站住 |
| **C6** | 所有候选 cov ≥ 0.95、dist ≥ 0.5 | cov 五条全 **0.9675**;dist **0.9933 + 1.0000×4** | **成立**。没有一条被门槛判死 |

**六条判据一条都没有被否定。按事前登记,推荐不变。**

⚠️ **C3/C4 的读法降级了,报告必须写明**:预登记要求「在同一个半衰期下比,优先读固定半衰期表的 hl 0 行」,但引擎**只在拟合段算 hl 网格**,留出段没有这张表(`07_S_final.md` §3)。
+0.54 / +0.75 是**引擎各自拟合的半衰期下**算的(叠加 hl 1 对基准 hl 0)。错配带来的污染有多大,可以用有网格的 utrain 去量(**只借 hl 敏感性,不是把 utrain 的数当成 holdout 的数**):utrain own-hl Δ = +1.31 pp、同 hl0 Δ = +1.33 pp、同 hl1 Δ = +1.71 pp → **量级 ≲ 0.4 pp、符号不定**(own-hl 甚至比干净的 hl0 对照低 0.02 pp)。所以它**不是单方向的「上界」**,而是「污染 ≲0.4 pp 的读数」;无论往哪边算,都远低于 +1.5 pp 门槛和 ±3 pp 噪声 → C3 的裁决不受影响。详见 `09_diagnosis.md` B1。
`07_S_final.md` §4 和 `results/R2.md` 里写的是「上界」,措辞偏保守;**报告以 B1 的写法为准**,并说明两处为什么不同。

### 推荐

**第一推荐 = 事前登记的第一推荐 = `f_known30` = `cross_mean(day_std(Amt), 30)`(已知家族基准),不是这条因子的任何变体。**
**对 F106_erm_mag_gap_1m 本身的推荐是:不要进书。** 结论类型 **分辨**。

对只能做多的用户,这条研究可操作的输出只有一句:**F106 不进书,继续用已知成交额家族;要「别买刚封过板的票」这个排除效果,用一个朴素的日线涨停标记就够,不需要这棵树**(C4:朴素 +0.75 ≥ 自己 +0.54;而且两者在留出段都在噪声里,所以连这个叠加本身也不推荐)。

### 为什么没有更好的(不是「没找到」)

1. **没有免费的平滑改进**:原式的多头最优半衰期 hlL = 20 已经是全局网格端点,「原式 + 多头最优半衰期」就是用户公布那一行本身;而多头腿在网格**每一点、毛和净全负**(train hl0 −67.2% → hl20 −6.9%)→ 不是成本、不是平滑不够。
2. **所有连续构造都试过**:只留常规日 / 先排序再 EMA / clip(±3) / 只留 R / 只留 L / 折叠 / log(1+|X|) / R+L / log(1+R+L) —— 多头腿净超额在 train 和 valid **同时为正的一个都没有**。
3. **和已知家族相加更差**:24 行无一胜已知家族,且随权重单调下降;中性化残差的多头腿五行全负。
4. **叠加的增量有可以算出来的天花板**:ΔLnet ≈ share × 超额之差,预测 2.0/0.70/1.93/0.57 对实测 +1.59/+0.52/+1.60/+0.40,四格吻合到 25% 内;share 小是因为已知家族持有被标记票的相对频率只有 **24%~64%** —— **它本来就在躲这些票,这张「不要买」清单是多余的**。
5. **修好记忆也不产生候选**:短记忆计数构造 rank IC 是原式的 1.7~4.8 倍(H11 被支持),但取值几乎全是 0,**过不了 `dist ≥ 0.5`**。
6. **唯一超过一个点的标记是新股过滤器**(`listed < 250d`),那不是这条因子的功劳 → `12_next.md`。

### 留出段读完之后**没有**新增的东西(照规矩写明)

- 没有新增「已确立」条目;`09_diagnosis.md` 里所有 A 档的核心证据都来自 train/valid,留出段只用于按事前判据确认。
- 没有换候选、没有换排序、没有改判据、没有重跑任何阶段(本轮及上一轮**服务器运行 0 次**)。
- 留出段上**拿不到**的东西照实写缺,不重跑补:分位剖面(`profile` 无 holdout 键)、固定半衰期表(`sweep` 只在拟合段)。

## 11. 失效模式与风险

# 11 — 失效模式与风险

> 这条研究的结论是**分辨 / 不推荐**,所以这一页的重点和「推荐一条因子」时不一样:
> 一半写**「如果有人还想用它,会在哪里栽」**,另一半写**「我这个否定结论自己可能在哪里错」**。

---

## A. 如果有人还是想用这棵树,风险在哪

### A1. 尺度污染:`1e-6` 带量纲 —— 这条因子**不是尺度无关的**

要害在 `add(day_quantile(Ret, 0.95), create_like(..., 1e-06))`:这个 ε 带**收益量纲**,比一个 tick 小三个数量级。
- 当日上涨分钟 ≤ 12 个 → 分子分母同时趋 0,ε 接住分母 → 读数跳到 **~10⁶** 量级。整条因子的截面两端**全部**由这些塌缩日决定(`07x_1_anatomy.md` A 表)。
- 后果:**`Ret` 的单位一改(小数 ↔ 百分数)、分钟格一改(241 根 ↔ 别的根数),塌缩的触发条件就变了**,因子也跟着变成另一条因子。
- `day_quantile` 是线性插值的,但 241 分钟时 q = 0.95 恰好落在第 13 大、**不插值**;换成别的 bar 数(半日、科创板不同节奏、停牌半天)语义会变。
- 这是**结构性脆弱**,不是数值小毛病:谁要复用这个写法,ε 必须按量纲写(例如一个 tick 的若干分之一),或者干脆把事件显式写出来。

### A2. 制度依赖:整条信号挂在涨跌停板制度上

塌缩日 86.3% / 77.8% 是涨停收盘。所以它依赖:
- **涨跌幅限制本身**(主板 ±10%、科创/创业板 ±20%,2020-08 之后)—— 限制放宽/取消,塌缩日的构成就变;样本期内创业板限幅就改过一次。
- **241 分钟连续竞价 + 收盘集合竞价**的日内结构。
- 「封板 → 次日买不进」这套微观结构,这是空头腿那半收益的来源(见 A3)。
→ 把它当成一条「市场规律」来跨市场/跨制度搬运,是错的;它是一条**制度产物**。

### A3. 空头腿不可实现:公布的多空夏普有一半以上买不进

把次日涨停 / 一字板按不可成交处理后,train 多空夏普 **2.82 → 0.42**。另一条独立证据:去掉塌缩日或 clip(±3),多空夏普直接**转负**。
→ 用户表里那个 **test LS = 3.11**(我们复现到 3.108)**不是一条可交易的夏普**。这条必须写进报告,否则看表的人会以为「至少多空能做」。
用户做纯多头,这条本来就不影响推荐 —— 但它影响**对这张表的信任**。

### A4. 容量与可交易性:信息集中在 6.7%~8.0% 的「刚封过板」的票上

- 多头腿换手 2.40%/日(hl = 20),换手本身不是瓶颈。
- 但它的**信息**集中在被标记的那一小撮票(占全市场 8.0%/6.7%),而这些票恰好是封板票 —— 流动性在封板时反而是最差的、经常根本没有对手盘。
- 对纯多头用户,多头端是「近期没封板」的票,容量不成问题;但这也正是它没有信息的那一端(A2 of `09_diagnosis.md`)。

### A5. 已知暴露:它的真实暴露不是成交额水平,而是「近期涨停」这个已知现象

- 对已知家族几乎正交(rank corr **+0.0055**),对动量也几乎无关(corr −0.013)→ 「它是成交额/动量的改写」这种说法是**错的**,报告不要这样写。
- 但折叠量对四个「近期涨停」变量 **R² = 0.444**:它的暴露是 A 股**涨停板效应**,一个人尽皆知的现象。而且在唯一有用的用途(排除)上,**一个朴素日线涨停标记做得还更好**(留出段 +0.75 对 +0.54)。
→ 风险的说法是:**它不是新暴露,是一个已知现象的昂贵写法**。

---

## B. 我这个否定结论自己可能在哪里错(逐条写明怎么已经防过)

### B1. 过拟合 / 多重比较 —— 在「否定」方向上风险是低的,但在那个 +1pp 的发现上是高的

- 否定结论靠的是**多头腿在 7 个半衰期 × 2 段 × 毛净全负**、**连续构造 9 条无一两段同正**、**相加 24 行无一取胜**。这类「全负/全败」的证据不怕多重比较 —— 搜得越宽越支持否定。
- 但 H13(`listed < 250d` 四格全 ≥1 pp)来自一个 **9 标记 × 2 家族 × 2 段 = 36 格**的搜索,**这个正向发现有真实的多重比较风险**,只能算「合理但未坐实」,必须另外预登记再验(`12_next.md`)。
- 所有否定判据(C1~C6)和门槛(+1.5 pp、±3 pp)都是在**读留出段之前**写死的(`10_distilled.md` 前半节,14:59 写,15:29 才启动 `final`)→ 不存在「看完再定线」。

### B2. 留出段的证据有两个口径上的缺口(都已照实写,都不改结论)

1. **C3/C4 不是严格同一半衰期的对照**:引擎只在拟合段算 hl 网格。错配污染的量级用 utrain 的 hl 敏感性量过,**≲ 0.4 pp、符号不定**(`09_diagnosis.md` B1)→ 远低于 +1.5 pp 门槛,裁决不变。
2. **留出段没有分位剖面、没有固定半衰期表**(引擎没算)→ 「留出段上是否仍然倒 U」**无数据**。补不了:重跑就是第二次读留出段。
→ 这两个缺口都只影响**次要**结论(剖面形状、Δ 的小数位),不影响 C1(多头腿 −3.19%、八年全负)和 C5(已知家族 +14.10%)这两条承重墙。

### B3. 「泄漏」这条基本可以排除

树里**没有任何日轴算子**,真实回看 1 个交易日;塌缩的触发条件(当日上涨分钟数、当日分位数)在**当日收盘时**全部已知,信号用于 t+1 交易;时间结构全部来自口径里的**因果** EMA。
唯一要小心的不是泄漏,而是 A3 那种**不可成交**(信息是真的,但那个价拿不到)。

### B4. 否定结论最可能被推翻的一种情形(写明,方便以后打脸)

如果有人把记忆长度改对(≈20 天,配上 H11 的证据)、同时让取值连续到能过 `dist`,那么「封板记忆」这块信息**有可能**变成一本可交易的书 —— 本研究没有证伪这件事,只证伪了「**这棵树写出来的那条因子**」。
但注意天花板论证(`09_diagnosis.md` A7)对那条路也部分适用:已知家族本来就在躲这些票,相对持有频率只有 24%~64%。所以即便做成了,它更可能是一条**独立的小因子**,而不是对已知家族的增量。

### B5. 一条不属于这条因子的系统性风险(对整批研究)

已知家族 `cross_mean(day_std(Amt), 30)` 在样本里 **8 年逐年全正**、留出段 +14.10%/夏普 +1.51。这么稳的东西本身要留个心:它是整批研究的参照系,**如果它哪天失效,所有「相对已知家族有没有增量」的结论都要重读**。本研究只验到 2025 年底。

## 12. 下一步实验

# 12 — 下一步(只列能显著降低不确定性的)

> 这条因子本身**已经做完了**(结论:分辨;`10_distilled.md` 后半节)。下面三条里只有第 1 条值得花服务器时间,而且**它不属于这条因子**。

---

## 1. 值得做:`listed < 250d` 新股过滤器,作为已知家族多头书的叠加项(独立研究,不是 F106 的续集)

**为什么**:在 x2 的 9 标记 × 2 家族 × 2 段 = 36 格里,`listed < 250d` 是**唯一四格全部 ≥ 1 个点**的标记(ΔLnet +1.60 / +1.09(known30 的 train/valid)、+1.90 / +1.95(known9))。F106 自己的标记只有 +1.59 / **+0.52**,朴素涨停 +1.92 / **+0.50** —— 两者 valid 都塌到半个点,只有新股过滤器两段都站得住。

**为什么不在本研究里做**:它和这棵树没有关系(它不读 `Ret`、不读分位数、不是 F106 的任何子结构)。把它算成这条因子的成果就是审查反复抓的那个错(「升华版其实是别的东西」)。

**怎么做才算算**:
- 它是从 36 格里挑出来的 → **必须重新预登记**:先写死候选(已知家族 / 已知家族 + 新股排除)、判据(ΔLnet ≥ ? pp 才算有增量,门槛要考虑 ±3 pp 噪声)、再读它自己的留出段(**F106 的那一次留出段读取与它无关,不能复用**)。
- 需要分清三件事:**(a)** 新股本身次日超额差(可能只是 IPO 后的均值回复);**(b)** 已知家族是不是本来就在躲新股(**照 A7 那套 share × 超额之差的天花板算法先算一遍,算完可能就不用跑了**);**(c)** 这是不是一个「上市满一年才买」的通用风控规则,而不是一条因子。
- 先算天花板:如果已知家族多头十分位里新股的 share 很小,ΔLnet 的上限就定住了,一次服务器运行都不用花。

## 2. 可能值得做,但不是这条因子的提纯:把「封板记忆」显式写成一条短记忆因子

**线索**:H11 被支持 —— 显式计数构造的 rank IC 是 EMA-20(X) 的 **1.7~4.8 倍、两段全优**;事件效应约 20 天、40 天归零,而口径里的 EMA-20 记了约一年 → **记忆比效应长一个数量级**。

**卡在哪**:计数构造取值几乎全是 0,**过不了 `dist ≥ 0.5`**(多头端是并列里按股票代码切出来的 10%,不是一本书)。要能交易,必须把「计数」和一个连续的幅度量拼起来(例如 20 日内封板次数 × 封板前那几分钟的跳幅),这件事**本研究没有试过**。

**为什么优先级低**:`09_diagnosis.md` A7 的天花板论证对这条路也部分适用 —— 已知家族持有被标记票的相对频率只有 24%~64%,所以即便做成了,它更像一条**独立的小因子**,而不是对已知家族的增量。要做就当新因子立项、单独预登记,不要挂在 F106 名下。

## 3. 明确**不**做(写明原因,免得下一个人再花轮次)

| 不做什么 | 为什么 |
|---|---|
| 再找 X 的单调变换(log / clip / 折叠 / 只留一侧…) | 9 条连续构造,多头腿 train+valid **同时为正的一个都没有**;而且倒 U 剖面说明问题不是单调性,是两端都是同一类票 |
| 延长半衰期 | hlL = 20 已经是全局网格端点,「原式 + 多头最优半衰期」就是用户公布那一行本身;而且网格每一点都是负的 |
| 抢救空头腿 / 优化多空夏普 | 用户做 A 股纯多头;而且那半收益有 85% 是次日买不进的票(`11_risks.md` A3) |
| 重跑 `S1_regime`(exit 97 = 被内存守卫顶掉,根本没跑) | 它想问的「塌缩日 vs 尾部形状」已经由自写脚本 x1 答掉;花一次服务器运行换一张格式更好的表,不值 |
| 补留出段的分位剖面 / 固定半衰期表 | **重跑就是第二次读留出段** —— 这项研究唯一不可挽回的错误。照实写「缺」 |
| 加大 ε / 只留常规日 | 这两件事等价于「去掉塌缩日」,而塌缩日就是这条因子的全部内容 —— 做完它就不是这条因子了(多空夏普转负) |

---

## 4. 给总领的两条工具层面的反馈(不是这条因子的研究内容,但对整批有用)

1. **`final` 阶段的 JSON 缺两样东西,而这两样正是预登记会要的**:留出段的**分位剖面**(`profile` 只有 train/valid,而且有的变体连这个字段都没有)和留出段的**固定半衰期表**(`sweep` 只在拟合段算)。
   后果很具体:预登记写了「ΔLnet 一律在同一个半衰期下比,优先读 hl 0 行」,结果留出段读不到这一行,只能降级成「引擎各自拟合的 hl」并另外去量错配有多大(`09_diagnosis.md` B1)。**整批研究只要用到「同一半衰期下的差值」这个判据,都会撞上同一个坑。**
2. **`diagnostics.by_year` 没有标注它用的是哪一套半衰期**(`books` 还是 `books_user`),JSON 里没有字段可查,靠数字也分不开(`07_S_final.md` §7 的精度提示)。逐年表是报告里常引的东西,建议加一个字段标注。

(两条都只是反馈,**我没有改 `scripts/`、`partura/`、`workflows/`、`handoff/`、`lab/`、`docs/` 里的任何东西**。)

## 附录 A — 数据段使用台账

| 数据段 | 区间 | 读取次数 | 累计打分表达式 |
|---|---|---|---|
| train | 20180102–20211231 | 5 | 9 |
| valid | 20220101–20230807 | 5 | 9 |
| holdout | 20230808–20251231 | 1 | 5 |
| full | 20180102–20251231 | 1 | 5 |
| utrain | 20180102–20230807 | 5 | 9 |

> 留出段被读取 1 次(5 条表达式)。

## 附录 B — 复现

```bash
# S0_baseline: 220.0s, 峰值 anon 3.15 GiB, stages ['S0_baseline']
# S_final: 310.3s, 峰值 anon 5.71 GiB, stages ['S_final']
scripts/run_server.sh configs/F106_erm_mag_gap_1m.yaml <stage...>          # EXTRA=--holdout 才读留出段
python -m partura.cli report configs/F106_erm_mag_gap_1m.yaml
```

```json
{
 "alphacube_root": "/root/autodl-tmp/AlphaCube",
 "alphacube_commit": "1698296",
 "alphacube_dirty": false,
 "partura_root": "/root/autodl-tmp/Partura",
 "partura_commit": null,
 "partura_code_sha": "6c89c05560a5",
 "store": "/root/autodl-tmp/qmt_daily_data/fast_factor_compute",
 "python": "3.12.3",
 "torch": "2.8.0+cu128",
 "numpy": "2.3.2",
 "host": "autodl-container-bud5qn7u2k-f41e5a0a"
}
```
