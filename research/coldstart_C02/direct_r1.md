# C02 直接检验(第 1 轮):7 个假设、64 个变体(= B 组 64 次付费评估)

score = 纯多头十分位书扣 15bp 的 train 与 valid 夏普中较差的;发现 = score ≥ 0.7 且未被相关度拒绝(|ρ已知| ≥ 0.5);门槛:覆盖率 ≥ 0.9、取值离散度 ≥ 0.5。

## H1_slow_intraday_reversal

> 盘中价格由追涨杀跌的流动性需求推动:买方急于成交时付出价格冲击,把价格推离其信息价值。 这部分位移没有信息,随后几周随着买压消散而回吐。隔夜那一跳主要是信息与机构委托,不属于这个机制, 所以「只取盘中段」应该比「取整日收益」更干净,平滑 30 天是为了把单日噪声和成本一起压下去。

| 变体 | 角色 | score | train | valid | 方向 | 半衰期 | 换手 | ρ已知 | 结果 | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| v1 | core | +0.84 | +0.97 | +0.84 | -1.0 | 20.0 | +0.030 | +0.23 | **发现** | `cross_mean(log(div(day_last(Close), day_first(Open))), 30)` |
| v2 | core | +0.86 | +0.89 | +0.86 | -1.0 | 20.0 | +0.030 | +0.24 | **发现** | `ts_mean(day_mean(Ret), 30)` |
| v3 | core | +0.42 | +1.06 | +0.42 | -1.0 | 5.0 | +0.042 | +0.30 | 未过线 | `ts_mean(day_mean(Ret), 50)` |
| v4 | core | +0.98 | +0.99 | +0.98 | -1.0 | 5.0 | +0.038 | +0.30 | **发现** | `cross_ema(log(div(day_last(Close), day_first(Open))), 30)` |
| v5 | ablation | +0.66 | +0.66 | +0.72 | -1.0 | 20.0 | +0.041 | +0.11 | 未过线 | `cross_mean(log(div(day_last(Close), day_first(Open))), 15)` |
| v6 | ablation | +0.44 | +0.96 | +0.44 | -1.0 | 5.0 | +0.038 | +0.30 | 未过线 | `cross_mean(log(div(day_last(Close), day_first(Open))), 60)` |
| v7 | ablation | +0.84 | +0.96 | +0.84 | -1.0 | 20.0 | +0.029 | +0.23 | **发现** | `cross_mean(log(div(day_last(Close), day_first(Close))), 30)` |
| v8 | ablation | +0.60 | +0.60 | +0.72 | -1.0 | 20.0 | +0.030 | +0.22 | 未过线 | `div(cross_mean(day_sum(Ret), 30), cross_mean(day_std(Ret), 30))` |
| v9 | ablation | +0.65 | +0.65 | +0.79 | -1.0 | 20.0 | +0.039 | +0.09 | 未过线 | `log(div(day_last(Close), ts_delay(day_last(Close), 20)))` |
| v10 | ablation | +0.13 | +0.13 | +0.64 | -1.0 | 5.0 | +0.057 | +0.18 | 未过线 | `ts_mean(log(div(day_last(Close), ts_delay(day_last(Close), 1))), 30)` |
| v11 | ablation | +0.43 | +0.43 | +1.03 | -1.0 | 20.0 | +0.031 | +0.20 | 未过线 | `div(cross_mean(log(div(day_last(Close), day_first(Open))), 30), cross_mean(log(div(day_max(High), day_min(Low))), 30))` |
| v12 | ablation | +0.22 | +0.64 | +0.22 | -1.0 | 20.0 | +0.026 | -0.01 | 未过线 | `cs_regres(cross_mean(log(div(day_last(Close), day_first(Open))), 30), cross_mean(log(div(day_max(High), day_min(Low))), 30))` |
| v13 | control | -0.47 | -0.47 | +0.67 | -1.0 | 5.0 | +0.022 | +0.53 | 被相关度拒绝 | `cross_mean(log(div(day_max(High), day_min(Low))), 30)` |

## H2_overnight_vs_intraday

> 隔夜段没有连续交易,价格只能由集合竞价一次性消化信息和机构的隔夜委托,所以隔夜那一跳偏向「信息」, 在之后几周延续;盘中段由连续的流动性需求推动,偏向「噪音」,随后回吐(即 H1)。 两类收益的来源不同,所以「谁的收益在隔夜到账」本身就是一个带方向的股票特征, 而「隔夜减盘中」把两个相反的机制叠起来,信噪比应高于任一段。

| 变体 | 角色 | score | train | valid | 方向 | 半衰期 | 换手 | ρ已知 | 结果 | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| v1 | core | -1.66 | -0.71 | -1.66 | 1.0 | 20.0 | +0.024 | +0.09 | 未过线 | `ts_mean(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 30)` |
| v2 | core | +0.07 | +0.07 | +0.66 | 1.0 | 20.0 | +0.027 | +0.20 | 未过线 | `sub(ts_mean(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 30), ts_mean(log(div(day_last(Close), day_first(Open))), 30))` |
| v3 | core | +0.86 | +0.89 | +0.86 | 1.0 | 20.0 | +0.030 | +0.24 | **发现** | `cross_mean(sub(mul(2, day_first(Ret)), day_sum(Ret)), 30)` |
| v4 | ablation | -2.04 | -0.86 | -2.04 | 1.0 | 20.0 | +0.029 | +0.10 | 未过线 | `ts_mean(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 20)` |
| v5 | ablation | -1.07 | -0.60 | -1.07 | 1.0 | 20.0 | +0.019 | +0.06 | 未过线 | `ts_mean(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 50)` |
| v6 | ablation | — | — | — | — | — | — | — | 门槛废品 | `cross_mean(day_first(Ret), 30)` |
| v7 | ablation | — | — | — | — | — | — | — | 门槛废品 | `cross_mean(log(div(day_first(Close), day_first(Open))), 30)` |
| v8 | ablation | +0.15 | +0.15 | +0.42 | 1.0 | 5.0 | +0.037 | +0.23 | 未过线 | `sub(ts_mean(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 50), ts_mean(log(div(day_last(Close), day_first(Open))), 50))` |
| v9 | ablation | -2.79 | -1.02 | -2.79 | 1.0 | 20.0 | +0.025 | +0.08 | 未过线 | `cs_regres(ts_mean(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 30), cross_mean(log(div(day_last(Close), day_first(Open))), 30))` |
| v10 | ablation | -1.20 | -0.36 | -1.20 | 1.0 | 5.0 | +0.062 | +0.17 | 未过线 | `cs_regres(cross_mean(sub(mul(2, day_first(Ret)), day_sum(Ret)), 30), cross_mean(log(div(day_last(Close), day_first(Open))), 30))` |
| v11 | control | -0.08 | -0.08 | +1.32 | -1.0 | 20.0 | +0.016 | +0.52 | 被相关度拒绝 | `ts_mean(abs_(log(div(day_first(Open), ts_delay(day_last(Close), 1)))), 30)` |

## H3_money_weighted_price_reverts

> 成批下单(机构拆单、ETF 申赎、散户情绪集中入场)会在少数分钟里同时放量并把价格推开, 这部分位移是流动性对价,之后回吐;真正的信息则是在全天均匀渗透的。 所以「按成交额加权的分钟收益」减去「等权的分钟收益」度量的正是这种集中下单造成的价格压力, 它是无量纲的(Amt 只作权重、被分母约掉),与成交额的水平无关。

| 变体 | 角色 | score | train | valid | 方向 | 半衰期 | 换手 | ρ已知 | 结果 | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| v1 | core | +0.51 | +0.51 | +0.63 | -1.0 | 20.0 | +0.023 | +0.40 | 未过线 | `cross_mean(sub(day_signed_ratio(Ret, Amt), day_signed_ratio(Ret, Close)), 30)` |
| v2 | core | +0.05 | +0.05 | +0.43 | -1.0 | 5.0 | +0.046 | +0.26 | 未过线 | `cross_mean(sub(day_wmean(Ret, Amt), day_mean(Ret)), 30)` |
| v3 | core | +0.01 | +0.01 | +0.61 | -1.0 | 5.0 | +0.050 | +0.35 | 未过线 | `cross_mean(sub(day_topw_mean(Ret, Amt), day_mean(Ret)), 30)` |
| v4 | control | -0.67 | -0.67 | +0.56 | -1.0 | 20.0 | +0.030 | +0.09 | 未过线 | `cross_mean(sub(day_topw_mean(Ret, cross_delay(Amt, 3)), day_mean(Ret)), 30)` |
| v5 | ablation | -0.08 | -0.08 | +0.11 | -1.0 | 20.0 | +0.025 | +0.24 | 未过线 | `cross_mean(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 30)` |
| v6 | ablation | -0.40 | -0.40 | +0.16 | -1.0 | 20.0 | +0.026 | +0.31 | 未过线 | `cross_mean(div(sub(day_topw_mean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 30)` |
| v7 | ablation | -0.95 | -0.95 | -0.75 | -1.0 | 20.0 | +0.023 | +0.16 | 未过线 | `cross_mean(day_signed_ratio(Ret, Amt), 30)` |
| v8 | ablation | +0.34 | +0.34 | +0.87 | -1.0 | 20.0 | +0.026 | +0.35 | 未过线 | `cross_mean(day_topw_mean(Ret, Amt), 30)` |
| v9 | ablation | -0.45 | -0.15 | -0.45 | 1.0 | 5.0 | +0.038 | -0.35 | 未过线 | `cs_regres(cross_mean(sub(day_signed_ratio(Ret, Amt), day_signed_ratio(Ret, Close)), 30), cross_mean(log(div(day_last(Close), day_first(Open))), 30))` |
| v10 | ablation | -1.73 | -1.04 | -1.73 | 1.0 | 20.0 | +0.021 | -0.29 | 未过线 | `cs_regres(cross_mean(sub(day_topw_mean(Ret, Amt), day_mean(Ret)), 30), cross_mean(log(div(day_last(Close), day_first(Open))), 30))` |
| v11 | control | -0.32 | -0.32 | +1.34 | -1.0 | 20.0 | +0.029 | +0.07 | 未过线 | `cross_mean(sub(day_signed_ratio(Ret, cross_delay(Amt, 3)), day_signed_ratio(Ret, Close)), 30)` |

## H4_intraday_price_volume_corr

> 日内价量正相关说明价格上行是靠买方不断提高报价换来的 —— 买压与价格同向,是典型的追涨资金在推; 这种推动没有信息支撑,之后回落。负相关则说明下跌中有大额承接,是知情或价值资金在接货,之后修复。 这个读数是无量纲的(相关系数),与成交额的绝对水平无关,所以与已知族在结构上完全不同。

| 变体 | 角色 | score | train | valid | 方向 | 半衰期 | 换手 | ρ已知 | 结果 | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| v1 | core | -0.92 | -0.52 | -0.92 | -1.0 | 20.0 | +0.026 | +0.24 | 未过线 | `cross_mean(day_corr(Close, Volume), 30)` |
| v2 | core | -0.28 | -0.28 | -0.05 | -1.0 | 20.0 | +0.025 | +0.27 | 未过线 | `cross_mean(day_corr(Ret, Volume), 30)` |
| v3 | ablation | -1.30 | -0.82 | -1.30 | -1.0 | 20.0 | +0.036 | +0.17 | 未过线 | `cross_mean(day_corr(Close, Volume), 15)` |
| v4 | ablation | -0.87 | -0.20 | -0.87 | -1.0 | 5.0 | +0.032 | +0.26 | 未过线 | `cross_mean(day_corr(Close, Volume), 60)` |
| v5 | ablation | -0.46 | -0.46 | +0.98 | -1.0 | 5.0 | +0.041 | +0.55 | 被相关度拒绝 | `cross_stddev(day_corr(Close, Volume), 30)` |
| v6 | ablation | +0.39 | +0.39 | +0.79 | -1.0 | 5.0 | +0.042 | +0.50 | 未过线 | `add(cs_rank(cross_mean(day_corr(Close, Volume), 30)), cs_rank(cross_stddev(day_corr(Close, Volume), 30)))` |
| v7 | ablation | -0.18 | -0.18 | +0.91 | -1.0 | 5.0 | +0.054 | +0.26 | 未过线 | `cross_mean(day_corr(in_delay(Ret, 3), Volume), 30)` |
| v8 | ablation | -0.72 | -0.66 | -0.72 | -1.0 | 20.0 | +0.026 | +0.23 | 未过线 | `cs_regres(cross_mean(day_corr(Close, Volume), 30), cross_mean(log(div(day_last(Close), day_first(Open))), 30))` |
| v9 | ablation | -1.23 | -1.23 | -0.83 | 1.0 | 20.0 | +0.023 | -0.21 | 未过线 | `cs_regres(cross_mean(day_corr(Ret, Volume), 30), cross_mean(log(div(day_last(Close), day_first(Open))), 30))` |
| v10 | control | -0.34 | -0.34 | +1.01 | -1.0 | 5.0 | +0.017 | +0.44 | 未过线 | `cross_mean(day_corr(abs_(Ret), Volume), 30)` |

## H5_closing_push_reverts

> 尾盘的买压有特殊来源:以收盘价为基准的委托(指数基金、做市与结算)、盘后信息前的抢筹、 以及刻意影响收盘价的行为。它们把收盘价推离日内均衡,属于临时溢价,之后回吐。 收盘段的收益因此应与未来收益负相关,而同样长度的盘中其它时段不应有这个性质。

| 变体 | 角色 | score | train | valid | 方向 | 半衰期 | 换手 | ρ已知 | 结果 | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| v1 | core | -1.64 | -1.17 | -1.64 | -1.0 | 5.0 | +0.044 | -0.12 | 未过线 | `cross_mean(day_last(in_sum_rolling(Ret, 30)), 30)` |
| v2 | core | +0.17 | +0.17 | +0.93 | -1.0 | 5.0 | +0.043 | -0.01 | 未过线 | `cross_mean(day_last(Ret), 30)` |
| v3 | core | -1.65 | -1.13 | -1.65 | -1.0 | 5.0 | +0.044 | -0.12 | 未过线 | `cross_mean(log(div(day_last(Close), day_last(in_delay(Close, 30)))), 30)` |
| v4 | ablation | -1.75 | -0.76 | -1.75 | -1.0 | 5.0 | +0.048 | -0.01 | 未过线 | `cross_mean(day_last(in_sum_rolling(Ret, 15)), 30)` |
| v5 | ablation | +0.17 | +0.17 | +0.93 | 1.0 | 5.0 | +0.043 | -0.01 | 未过线 | `cross_mean(sub(day_first(Ret), day_last(Ret)), 30)` |
| v6 | ablation | -1.90 | -0.16 | -1.90 | -1.0 | 5.0 | +0.032 | -0.50 | 被相关度拒绝 | `cross_mean(div(day_last(in_sum_rolling(Amt, 30)), day_sum(Amt)), 30)` |
| v7 | ablation | -2.47 | -1.74 | -2.47 | -1.0 | 5.0 | +0.045 | -0.15 | 未过线 | `cs_regres(cross_mean(day_last(in_sum_rolling(Ret, 30)), 30), cross_mean(log(div(day_last(Close), day_first(Open))), 30))` |
| v8 | control | -1.63 | -0.37 | -1.63 | -1.0 | 20.0 | +0.029 | +0.04 | 未过线 | `cross_mean(day_last(in_sum_rolling(in_delay(Ret, 60), 30)), 30)` |

## H6_attention_shock

> 散户的买入决策受注意力约束(Barber–Odean):放量、上榜、上涨会把一只股票带进视野, 引发集中的买单,把价格推到基本面之上,之后几周回落。关键是「相对自身」而不是「绝对量大」: 绝对成交额是规模的代理(已知族),而 5 日对 60 日的比值把水平约掉,只留下冲击。

| 变体 | 角色 | score | train | valid | 方向 | 半衰期 | 换手 | ρ已知 | 结果 | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| v1 | core | -0.18 | -0.18 | +0.79 | -1.0 | 20.0 | +0.043 | +0.12 | 未过线 | `log(div(cross_mean(day_sum(Amt), 5), cross_mean(day_sum(Amt), 60)))` |
| v2 | core | -0.83 | -0.83 | -0.10 | -1.0 | 20.0 | +0.105 | +0.02 | 未过线 | `mul(sign(cross_sum(day_sum(Ret), 5)), log(div(cross_mean(day_sum(Amt), 5), cross_mean(day_sum(Amt), 60))))` |
| v3 | ablation | -1.62 | -1.62 | -0.52 | -1.0 | 20.0 | +0.040 | +0.10 | 未过线 | `cs_regres(log(div(cross_mean(day_sum(Amt), 5), cross_mean(day_sum(Amt), 60))), cross_ema(cross_scale(mul(signedpower(day_std(Volume)), day_first(Volume)), 241), 15))` |
| v4 | ablation | -0.35 | -0.25 | -0.35 | -1.0 | 5.0 | +0.057 | +0.04 | 未过线 | `div(cross_stddev(day_sum(Amt), 30), cross_mean(day_sum(Amt), 30))` |
| v5 | ablation | -1.71 | -1.71 | -0.63 | -1.0 | 20.0 | +0.039 | +0.07 | 未过线 | `cs_regres(log(div(cross_mean(day_sum(Amt), 5), cross_mean(day_sum(Amt), 60))), cross_mean(log(div(day_last(Close), day_first(Open))), 30))` |
| v6 | control | -1.37 | -1.37 | -0.46 | -1.0 | 20.0 | +0.047 | -0.02 | 未过线 | `log(div(cross_mean(day_std(Ret), 5), cross_mean(day_std(Ret), 60)))` |

## H7_daily_max_lottery

> 偏好彩票型回报的投资者愿意为「最近出现过大涨」的股票多付钱(Bali–Cakici–Whitelaw 的 MAX 效应), 这种溢价之后回落。C01 测过的是日内分钟收益的彩票形状(偏度、最大涨幅比波动),全部为负; 日频右尾在 C01 里一次都没测过(G7 族匹配数为 0),机制上也不同:日频右尾是公众可见的涨停/大涨, 日内分钟形状是公众看不见的微观结构。

| 变体 | 角色 | score | train | valid | 方向 | 半衰期 | 换手 | ρ已知 | 结果 | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| v1 | core | -0.38 | -0.38 | +0.66 | -1.0 | 5.0 | +0.049 | +0.43 | 未过线 | `ts_max(log(div(day_last(Close), ts_delay(day_last(Close), 1))), 20)` |
| v2 | core | -0.67 | -0.67 | +0.21 | -1.0 | 20.0 | +0.038 | +0.07 | 未过线 | `div(ts_max(log(div(day_last(Close), ts_delay(day_last(Close), 1))), 20), ts_std(log(div(day_last(Close), ts_delay(day_last(Close), 1))), 20))` |
| v3 | core | +0.47 | +0.47 | +0.54 | -1.0 | 5.0 | +0.049 | +0.18 | 未过线 | `ts_skew(log(div(day_last(Close), ts_delay(day_last(Close), 1))), 40)` |
| v4 | ablation | -0.89 | -0.89 | -0.16 | -1.0 | 5.0 | +0.050 | +0.37 | 未过线 | `cs_regres(ts_max(log(div(day_last(Close), ts_delay(day_last(Close), 1))), 20), cross_mean(log(div(day_last(Close), day_first(Open))), 30))` |
| v5 | control | -0.95 | -0.95 | +0.07 | -1.0 | 5.0 | +0.040 | +0.51 | 被相关度拒绝 | `ts_std(log(div(day_last(Close), ts_delay(day_last(Close), 1))), 20)` |

