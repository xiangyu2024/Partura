# C02 直接检验(第 1 轮):6 个假设、64 个变体(= B 组 64 次付费评估)

score = 纯多头十分位书扣 15bp 的 train 与 valid 夏普中较差的;发现 = score ≥ 0.5 且未被相关度拒绝(|ρ已知| ≥ 0.5);门槛:覆盖率 ≥ 0.9、取值离散度 ≥ 0.5。

## H1_price_conditional_range

> 振幅度量分歧。重要的不是振幅有多大(那是波动,奖励的控制变量里已经有),而是分歧出现在价格的哪个位置。 分歧集中在高位,说明上涨是靠不断提高报价从追涨者手里换来的,持有者正在用高振幅派发; 分歧集中在低位,说明下跌中有资金在承接。相关系数把价格与振幅两条腿的量纲和水平都约掉, 只留下这个「配对关系」,所以它既不是价格水平也不是波动水平。开源证券的「理想振幅」是同一思路的日频实现(先验)。

| 变体 | 角色 | score | train | valid | 方向 | 半衰期 | 换手 | ρ已知 | 结果 | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| v1 | core | -1.27 | -0.70 | -1.27 | -1.0 | 20.0 | +0.064 | +0.22 | 未过线 | `cross_corr(day_last(Close), log(div(day_max(High), day_min(Low))), 30)` |
| v2 | core | -0.80 | -0.80 | -0.59 | -1.0 | 20.0 | +0.054 | +0.20 | 未过线 | `cross_corr(day_last(Close), log(div(day_max(High), day_min(Low))), 60)` |
| v3 | core | -0.54 | -0.42 | -0.54 | -1.0 | 20.0 | +0.055 | +0.30 | 未过线 | `cross_corr(day_last(Close), day_std(Ret), 30)` |
| v4 | ablation | -1.75 | -1.58 | -1.75 | -1.0 | 20.0 | +0.057 | +0.19 | 未过线 | `cross_mean(day_corr(Close, abs_(Ret)), 30)` |
| v5 | ablation | -1.93 | -1.37 | -1.93 | -1.0 | 20.0 | +0.078 | +0.15 | 未过线 | `cross_corr(day_last(Close), log(div(day_max(High), day_min(Low))), 15)` |
| v6 | ablation | -1.35 | -0.97 | -1.35 | -1.0 | 20.0 | +0.063 | +0.21 | 未过线 | `cross_corr(day_mean(Vwap), log(div(day_max(High), day_min(Low))), 30)` |
| v7 | ablation | -1.98 | -1.16 | -1.98 | -1.0 | 20.0 | +0.061 | +0.21 | 未过线 | `cross_corr(log(div(day_last(Close), day_first(Open))), log(div(day_max(High), day_min(Low))), 30)` |
| v8 | ablation | -1.06 | +0.11 | -1.06 | -1.0 | 20.0 | +0.060 | +0.17 | 未过线 | `cross_corr(day_last(Close), day_sum(Amt), 30)` |
| v9 | ablation | -2.20 | -1.17 | -2.20 | -1.0 | 20.0 | +0.063 | +0.19 | 未过线 | `cs_regres(cross_corr(day_last(Close), log(div(day_max(High), day_min(Low))), 30), cross_ema(log(div(day_last(Close), day_first(Open))), 30))` |
| v10 | control | -0.29 | -0.29 | +0.59 | -1.0 | 0.0 | +0.056 | +0.53 | 被相关度拒绝 | `cross_mean(log(div(day_max(High), day_min(Low))), 30)` |
| v11 | control | -0.90 | -0.90 | -0.58 | 1.0 | 5.0 | +0.055 | -0.42 | 未过线 | `log(day_last(Close))` |

## H2_smart_money_minutes

> 用 |分钟收益| / 根号(分钟成交量) 度量一分钟的价格冲击效率,最高的那些分钟是有信息、愿意付冲击的激进单。 把这些分钟的均价与全天 VWAP 相比,得到一个围绕 1 的无量纲比值:小于 1 说明激进交易发生在当天的低价区, 是吸筹;大于 1 说明激进交易在高价区,是派发。随后几周价格向知情的那一侧移动。 机制要求的只是「选哪些分钟」,成交量只进入选择与根号归一,量纲在比值里被约掉。 开源证券 2019 的聪明钱因子是同一构造(先验)。

| 变体 | 角色 | score | train | valid | 方向 | 半衰期 | 换手 | ρ已知 | 结果 | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| v1 | core | -2.56 | -0.65 | -2.56 | 1.0 | 20.0 | +0.048 | +0.15 | 未过线 | `cross_mean(div(day_mean(in_topk_masked_exact(div(abs_(Ret), pow_05(Volume)), Close, 20)), day_wmean(Close, Volume)), 30)` |
| v2 | core | -3.89 | -1.53 | -3.89 | 1.0 | 20.0 | +0.075 | +0.04 | 未过线 | `cross_mean(div(day_topw_mean(Close, div(abs_(Ret), pow_05(Volume))), day_wmean(Close, Volume)), 10)` |
| v3 | core | -3.06 | -0.88 | -3.06 | 1.0 | 20.0 | +0.049 | +0.12 | 未过线 | `cross_mean(div(day_topw_mean(Close, div(abs_(Ret), pow_05(Volume))), day_wmean(Close, Volume)), 30)` |
| v4 | core | -1.70 | -1.51 | -1.70 | -1.0 | 20.0 | +0.067 | -0.02 | 未过线 | `cross_mean(div(day_topw_mean(Close, div(abs_(Ret), pow_05(pow_05(Volume)))), day_wmean(Close, Volume)), 30)` |
| v5 | ablation | -0.08 | -0.08 | +0.30 | -1.0 | 5.0 | +0.071 | +0.16 | 未过线 | `cross_mean(div(day_topw_mean(Close, abs_(Ret)), day_wmean(Close, Volume)), 30)` |
| v6 | ablation | -3.39 | -0.99 | -3.39 | -1.0 | 20.0 | +0.038 | +0.23 | 未过线 | `cross_mean(div(day_topw_mean(Close, Volume), day_wmean(Close, Volume)), 30)` |
| v7 | ablation | -1.34 | -1.22 | -1.34 | -1.0 | 20.0 | +0.049 | +0.12 | 未过线 | `cross_mean(div(day_topw_mean(Close, div(abs_(Ret), pow_05(cross_delay(Volume, 3)))), day_wmean(Close, Volume)), 30)` |
| v8 | ablation | -2.40 | -0.69 | -2.40 | 1.0 | 20.0 | +0.047 | +0.16 | 未过线 | `cross_mean(div(day_topw_mean(Vwap, div(abs_(Ret), pow_05(Volume))), day_wmean(Vwap, Volume)), 30)` |
| v9 | ablation | -2.62 | -1.24 | -2.62 | 1.0 | 20.0 | +0.047 | +0.13 | 未过线 | `cs_regres(cross_mean(div(day_topw_mean(Close, div(abs_(Ret), pow_05(Volume))), day_wmean(Close, Volume)), 30), cross_ema(log(div(day_last(Close), day_first(Open))), 30))` |
| v10 | control | -1.83 | -0.64 | -1.83 | -1.0 | 20.0 | +0.071 | -0.01 | 未过线 | `cross_mean(div(day_last(Close), day_wmean(Close, Volume)), 30)` |
| v11 | control | -3.74 | -1.53 | -3.74 | 1.0 | 5.0 | +0.061 | +0.09 | 未过线 | `cross_mean(div(day_mean(Close), day_wmean(Close, Volume)), 30)` |

## H3_signed_variance_asymmetry

> 把一天的分钟平方收益按收益符号拆开:上行占比高,说明这天的波动是正向跳 —— 公众可见的上冲、彩票型的回报形状, 偏好这种分布的投资者愿意为它多付钱,溢价随后回落;下行占比高,说明波动来自抛售,价格被压到折价,随后修复。 它是一个纯形状量:方差的总量在分母里被约掉,值域 [−1, 1],所以与奖励控制里的波动水平正交。 Bollerslev–Li–Zhao 2020 的 RSJ、A 股的「下行波动占比」是同一个量(先验)。

| 变体 | 角色 | score | train | valid | 方向 | 半衰期 | 换手 | ρ已知 | 结果 | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| v1 | core | -0.38 | -0.33 | -0.38 | -1.0 | 20.0 | +0.047 | +0.29 | 未过线 | `cross_mean(day_signed_ratio(Ret, pow_2(Ret)), 30)` |
| v2 | core | -0.41 | -0.10 | -0.41 | -1.0 | 5.0 | +0.049 | +0.31 | 未过线 | `cross_mean(day_signed_ratio(Ret, pow_2(Ret)), 60)` |
| v3 | core | -0.39 | -0.39 | -0.35 | -1.0 | 20.0 | +0.049 | +0.29 | 未过线 | `cross_mean(day_signed_ratio(in_demean(Ret), pow_2(in_demean(Ret))), 30)` |
| v4 | ablation | +0.04 | +0.04 | +1.58 | -1.0 | 20.0 | +0.040 | -0.23 | 未过线 | `cross_mean(day_signed_ratio(Ret, div(abs_(Ret), Volume)), 30)` |
| v5 | ablation | -1.29 | -0.92 | -1.29 | -1.0 | 20.0 | +0.061 | +0.19 | 未过线 | `cross_mean(day_signed_ratio(Ret, Ret), 30)` |
| v6 | ablation | -1.05 | -0.31 | -1.05 | -1.0 | 5.0 | +0.063 | +0.17 | 未过线 | `cross_mean(day_skew(Ret), 30)` |
| v7 | ablation | -0.68 | -0.60 | -0.68 | -1.0 | 20.0 | +0.069 | +0.16 | 未过线 | `cross_mean(day_signed_ratio(Ret, pow_2(Ret)), 10)` |
| v8 | ablation | -0.94 | -0.94 | -0.73 | -1.0 | 20.0 | +0.054 | +0.18 | 未过线 | `cs_regres(cross_mean(day_signed_ratio(Ret, pow_2(Ret)), 30), cross_ema(log(div(day_last(Close), day_first(Open))), 30))` |
| v9 | ablation | -1.25 | -0.70 | -1.25 | -1.0 | 20.0 | +0.047 | +0.34 | 未过线 | `cs_regres(cross_mean(day_signed_ratio(Ret, pow_2(Ret)), 30), cross_mean(day_skew(Ret), 30))` |
| v10 | control | -1.50 | -1.50 | -0.57 | -1.0 | 20.0 | +0.063 | +0.57 | 被相关度拒绝 | `cross_mean(day_pos_ratio(Ret), 30)` |

## H4_volume_conditioned_reversal

> 区分流动性需求与信息:若上涨总是发生在放量日,说明价格是买方用成交量换来的 —— 他们需要即时性、支付冲击, 这部分位移没有信息,随后回吐;若价格变动与成交额无关或反向(缩量时在动),位移更可能来自信息,会延续。 日内版是同一句话:放量分钟里在涨,说明买方在不断提价。相关系数把成交额的量纲约掉, 所以它既不是流动性水平(控制变量),也不是成交额的离散度(已知族)。 Campbell–Grossman–Wang 1993、Llorente 等 2002,以及 A 股的 CPV(先验)。

| 变体 | 角色 | score | train | valid | 方向 | 半衰期 | 换手 | ρ已知 | 结果 | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| v1 | core | -1.02 | -0.71 | -1.02 | -1.0 | 20.0 | +0.060 | +0.08 | 未过线 | `cross_corr(log(div(day_last(Close), day_first(Open))), day_sum(Amt), 30)` |
| v2 | core | -0.27 | -0.09 | -0.27 | -1.0 | 20.0 | +0.043 | +0.07 | 未过线 | `cross_corr(log(div(day_last(Close), day_first(Open))), day_sum(Amt), 60)` |
| v3 | core | -0.89 | -0.14 | -0.89 | -1.0 | 20.0 | +0.045 | +0.15 | 未过线 | `sub(div(cross_mean(mul(log(div(day_last(Close), day_first(Open))), day_sum(Amt)), 30), cross_mean(day_sum(Amt), 30)), cross_mean(log(div(day_last(Close), day_first(Open))), 30))` |
| v4 | ablation | -1.36 | -1.36 | +0.19 | 1.0 | 20.0 | +0.052 | -0.24 | 未过线 | `cross_mean(day_corr(Close, Volume), 30)` |
| v5 | ablation | -1.40 | -1.08 | -1.40 | 1.0 | 20.0 | +0.069 | -0.10 | 未过线 | `ts_corr(log(div(day_last(Close), ts_delay(day_last(Close), 1))), day_sum(Amt), 30)` |
| v6 | ablation | -1.46 | -0.80 | -1.46 | -1.0 | 20.0 | +0.061 | +0.11 | 未过线 | `cross_corr(log(div(day_last(Close), day_first(Open))), log(day_sum(Amt)), 30)` |
| v7 | ablation | +0.22 | +0.22 | +2.30 | 1.0 | 20.0 | +0.047 | -0.27 | 未过线 | `cross_mean(day_corr(Ret, Volume), 30)` |
| v8 | ablation | -1.70 | -1.70 | +0.36 | 1.0 | 20.0 | +0.064 | -0.17 | 未过线 | `cross_mean(day_corr(Close, Volume), 15)` |
| v9 | ablation | -1.67 | -1.10 | -1.67 | -1.0 | 20.0 | +0.058 | +0.03 | 未过线 | `cs_regres(cross_corr(log(div(day_last(Close), day_first(Open))), day_sum(Amt), 30), cross_ema(log(div(day_last(Close), day_first(Open))), 30))` |
| v10 | core | -1.51 | -1.51 | +0.38 | 1.0 | 20.0 | +0.052 | -0.23 | 未过线 | `cs_regres(cross_mean(day_corr(Close, Volume), 30), cross_ema(log(div(day_last(Close), day_first(Open))), 30))` |
| v11 | control | -2.33 | -0.43 | -2.33 | 1.0 | 20.0 | +0.055 | -0.03 | 未过线 | `cross_corr(abs_(log(div(day_last(Close), day_first(Open)))), day_sum(Amt), 30)` |
| v12 | control | -0.24 | -0.09 | -0.24 | -1.0 | 20.0 | +0.046 | +0.30 | 未过线 | `cross_ema(log(div(day_last(Close), day_first(Open))), 30)` |

## H5_vol_of_vol_ambiguity

> 用日内滚动 5 或 15 分钟的波动序列度量「这一天的波动是否稳定」,再取它的变异系数:系数大说明波动忽高忽低, 当天的信息环境模糊(Brenner–Izhakian 2018 的 ambiguity:不是风险的大小,而是对风险本身的不确定)。 模糊会放大过度反应 —— 投资者不确定该相信什么的时候更依赖情绪与关注,价格偏离更远,随后回落。 变异系数把波动水平约掉,所以与奖励控制里的 cross_mean(day_std(Ret), 20) 正交。 方正证券「云开雾散」在 A 股报的方向是做多低模糊;美股文献对模糊溢价的符号不一致, 这里按 A 股取 −1,反号的处置写在 fails_if 里(先验)。

| 变体 | 角色 | score | train | valid | 方向 | 半衰期 | 换手 | ρ已知 | 结果 | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| v1 | core | +0.22 | +0.22 | +1.19 | -1.0 | 0.0 | +0.060 | -0.13 | 未过线 | `cross_mean(div(day_std(in_stddev_rolling(Ret, 5)), day_mean(in_stddev_rolling(Ret, 5))), 30)` |
| v2 | core | +0.04 | +0.04 | +1.00 | -1.0 | 0.0 | +0.053 | +0.02 | 未过线 | `cross_mean(div(day_std(in_stddev_rolling(Ret, 15)), day_mean(in_stddev_rolling(Ret, 15))), 30)` |
| v3 | core | +0.31 | +0.31 | +1.35 | -1.0 | 0.0 | +0.050 | -0.15 | 未过线 | `cross_mean(div(day_std(in_stddev_rolling(Ret, 5)), day_mean(in_stddev_rolling(Ret, 5))), 60)` |
| v4 | ablation | +0.11 | +0.11 | +0.53 | -1.0 | 0.0 | +0.075 | +0.11 | 未过线 | `div(cross_stddev(day_std(Ret), 30), cross_mean(day_std(Ret), 30))` |
| v5 | ablation | +0.38 | +0.38 | +0.86 | -1.0 | 0.0 | +0.059 | +0.09 | 未过线 | `div(cross_stddev(day_std(Ret), 60), cross_mean(day_std(Ret), 60))` |
| v6 | ablation | -0.11 | -0.11 | +1.09 | -1.0 | 0.0 | +0.082 | +0.19 | 未过线 | `cross_mean(day_std(in_stddev_rolling(Ret, 5)), 30)` |
| v7 | ablation | +0.28 | +0.28 | +1.30 | -1.0 | 0.0 | +0.052 | -0.11 | 未过线 | `cross_mean(day_kurt(Ret), 30)` |
| v8 | ablation | -1.03 | -1.03 | +0.49 | -1.0 | 20.0 | +0.050 | -0.07 | 未过线 | `cs_regres(cross_mean(div(day_std(in_stddev_rolling(Ret, 5)), day_mean(in_stddev_rolling(Ret, 5))), 30), cross_mean(day_kurt(Ret), 30))` |
| v9 | control | -1.41 | -1.41 | -0.51 | 1.0 | 0.0 | +0.066 | +0.57 | 被相关度拒绝 | `cross_mean(day_zero_ratio(Ret), 30)` |
| v10 | control | -0.35 | -0.35 | -0.04 | -1.0 | 20.0 | +0.046 | +0.15 | 未过线 | `abs_(cs_demean(cs_rank(cross_mean(day_std(Ret), 30))))` |

## H6_turnover_instability

> 成交额的不稳定是情绪资金进出的痕迹:一只票被一阵关注推高成交、随后冷却,这个来回本身说明它的持有者里 短线与情绪资金占比高,定价被这类资金的进出推离价值,随后回落。 关键是变异系数而不是标准差:均值把规模与流动性水平约掉,留下的是「相对自身的忽冷忽热」 —— 这是它能和控制变量里的流动性水平、已知族的成交额离散度分开的唯一理由,也是本假设的全部风险。 Chordia–Subrahmanyam–Anshuman 2001 用换手率的波动度量这件事,A 股的换手率波动因子同向(先验)。

| 变体 | 角色 | score | train | valid | 方向 | 半衰期 | 换手 | ρ已知 | 结果 | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| v1 | core | -0.50 | -0.50 | -0.24 | -1.0 | 20.0 | +0.064 | +0.04 | 未过线 | `div(cross_stddev(day_sum(Amt), 30), cross_mean(day_sum(Amt), 30))` |
| v2 | core | -0.39 | +0.24 | -0.39 | -1.0 | 5.0 | +0.068 | -0.03 | 未过线 | `div(cross_stddev(day_sum(Amt), 60), cross_mean(day_sum(Amt), 60))` |
| v3 | core | -1.10 | +0.21 | -1.10 | -1.0 | 0.0 | +0.087 | +0.07 | 未过线 | `cross_stddev(log(day_sum(Amt)), 60)` |
| v4 | core | -1.55 | -1.55 | +1.27 | -1.0 | 20.0 | +0.049 | -0.07 | 未过线 | `cross_stddev(ts_delta(log(day_sum(Amt)), 1), 60)` |
| v5 | ablation | -0.47 | -0.47 | +0.13 | -1.0 | 0.0 | +0.062 | -0.14 | 未过线 | `div(cross_stddev(day_sum(Amt), 241), cross_mean(day_sum(Amt), 241))` |
| v6 | ablation | -0.27 | -0.07 | -0.27 | -1.0 | 5.0 | +0.069 | -0.12 | 未过线 | `div(cross_max(day_sum(Amt), 60), cross_mean(day_sum(Amt), 60))` |
| v7 | ablation | -0.62 | -0.23 | -0.62 | -1.0 | 5.0 | +0.070 | -0.04 | 未过线 | `cs_regres(div(cross_stddev(day_sum(Amt), 60), cross_mean(day_sum(Amt), 60)), cross_scale(mul(signedpower(day_std(Volume)), day_first(Volume)), 241))` |
| v8 | control | -0.05 | +0.31 | -0.05 | 1.0 | 20.0 | +0.033 | -0.00 | 未过线 | `abs_(cs_demean(cs_rank(cross_mean(day_sum(Amt), 30))))` |
| v9 | ablation | -0.78 | -0.78 | -0.46 | -1.0 | 20.0 | +0.069 | -0.00 | 未过线 | `div(cross_stddev(day_sum(Amt), 15), cross_mean(day_sum(Amt), 15))` |
| v10 | control | -0.74 | -0.74 | +0.41 | 1.0 | 20.0 | +0.110 | -0.12 | 未过线 | `log(div(cross_mean(day_sum(Amt), 5), cross_mean(day_sum(Amt), 60)))` |

