# 研究实验 `e1_I2_dispersion_fold`

想法 `I2_dispersion_fold`;奖励 `long_marginal`;每臂预算 192 个候选(种群 48,随机种子 0);搜索只看 20180102–20230807(其中 20220101 起算 valid),测试段没有打开。

## 假设

日内价格 / 收益的离散度离「同类股票的典型值」越近越好(既不死水也不乱跳);哪个离散度统计量、以谁为参照(全市场 / 同成交额档)、多长的记忆

## 干预(带指引的一臂)

- 种子进首代:`cross_ema(abs_(cs_demean(day_gini(Low))), 30)`、`abs_(cs_demean(day_mean(in_stddev_rolling(in_slice(Ret, 2, 237), 5))))`、`abs_(cs_bucket_demean(day_gini(Ret), cross_mean(day_sum(Amt), 30)))`
- 想法里的算子采样概率 × 8.0;候选必须含这些算子之一:day_gini、day_std、day_es_ratio_hi、day_es_ratio_lo、day_wstd、day_distinct_ratio
- 每棵候选树过指引 `guidance/B01.yaml`:封禁的不放行,降权 / 升权按概率放行,等价写法只放行第一个

## 对照

同一个 GP、同一个奖励、同样的预算与随机种子、同一个算子库;不带种子、不过指引、均匀采样。

## 证据

| 臂 | 付费评估 | 没过门槛 | 活着的 | 互不等价的(存下来的前 80 里) | 分数 ≥ 0 | 分数 ≥ 0.1 | 分数 ≥ 0.2 | 分数 ≥ 0.3 | 最好 | 前五(互不等价)均值 | 过线且不在已知池里、互不重复 | 用时 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 带指引 | 123 | 21 | 102 | 62 / 80 | 0 | 0 | 0 | 0 | -0.62 | -0.67 | — | 22 分 |
| 对照 | 170 | 40 | 130 | 80 / 80 | 0 | 0 | 0 | 0 | -0.75 | -0.87 | — | 52 分 |

分数的含义:候选与已知池五五混合后的纯多头夏普减池子自己的,train 与 valid 取较差的(旧口径)。「分数 ≥」各列数的是互不等价的候选。

带指引的一臂提出了 430 棵树:封禁 0、不在想法邻域 243、按权重抽掉 20、与已提过的等价 0、放行 167。

## 各臂找到的(互不等价的前几个;纯多头夏普 train / valid 是奖励口径下的)

**带指引**

- -0.62(train +2.17 / valid +3.55,半衰期 0,与已知族相关 +0.31):`abs_(cross_ema(abs_(cs_demean(cs_demean(day_gini(Low)))), 241))`
- -0.66(train +2.13 / valid +3.50,半衰期 20,与已知族相关 +0.28):`cross_ema(abs_(cross_ema(abs_(abs_(cs_demean(day_gini(Low)))), 10)), 241)`
- -0.68(train +2.13 / valid +3.43,半衰期 0,与已知族相关 +0.25):`cross_ema(abs_(cross_ema(abs_(cs_demean(day_gini(Low))), 30)), 241)`
- -0.70(train +2.08 / valid +3.50,半衰期 20,与已知族相关 +0.25):`abs_(cross_ema(signedpower(cross_ema(abs_(cs_demean(day_gini(Low))), 30)), 241))`
- -0.70(train +2.08 / valid +3.45,半衰期 0,与已知族相关 +0.20):`cross_ema(abs_(cross_ema(abs_(cross_ema(abs_(cs_demean(day_gini(Low))), 30)), 30)), 241)`
- -0.74(train +2.05 / valid +3.61,半衰期 0,与已知族相关 +0.14):`cross_ema(abs_(cross_ema(cross_ema(abs_(cross_ema(abs_(cs_demean(day_gini(Low))), 30)), 241), 30)), 241)`

**对照**

- -0.75(train +2.05 / valid +3.35,半衰期 0,与已知族相关 +0.81):`cross_tail_mean_q75(pow_2_5(day_sum(in_delta(nt_ts_var(Amt, 60), 5))), 60)`
- -0.77(train +2.01 / valid +3.39,半衰期 20,与已知族相关 +0.30):`ts_spearman(pow_3(day_quantile(High)), 20)`
- -0.94(train +1.85 / valid +3.58,半衰期 20,与已知族相关 +0.86):`day_sum(nt_ts_var(Amt, 3))`
- -0.94(train +1.84 / valid +3.57,半衰期 20,与已知族相关 +0.85):`day_sum(nt_ts_var(Amt, 5))`
- -0.94(train +1.84 / valid +3.57,半衰期 20,与已知族相关 +0.85):`day_mean(nt_ts_var(Amt, 5))`
- -0.96(train +1.82 / valid +3.45,半衰期 5,与已知族相关 +0.81):`day_sum(nt_ts_var(nt_ts_var(Amt, 15), 5))`

## 信念更新

(待写:这次实验让哪条规则的权重 / 状态变了,为什么。)

