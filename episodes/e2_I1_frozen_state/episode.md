# 研究实验 `e2_I1_frozen_state`

想法 `I1_frozen_state`;奖励 `long_screen`;每臂预算 192 个候选(种群 48,随机种子 0);搜索只看 20180102–20230807(其中 20220101 起算 valid),测试段没有打开。

## 假设

盘口冻结(封板、停牌前后、无成交)是一个持续几周的状态,处在这个状态里的票系统性跑输;哪一种「冻结度」的写法、多长的记忆最能标出它

## 干预(带指引的一臂)

- 种子进首代:`cross_max(day_zero_ratio(Ret), 15)`、`cross_mean(day_flat_ratio(Close), 15)`、`cross_max(day_flat_run_max(Close), 15)`、`cross_mean(day_zero_ratio(Amt), 30)`
- 想法里的算子采样概率 × 8.0;候选必须含这些算子之一:day_zero_ratio、day_flat_ratio、day_flat_run_max、day_distinct_ratio、day_at_max_ratio、day_at_min_ratio
- 每棵候选树过指引 `guidance/B01.yaml`:封禁的不放行,降权 / 升权按概率放行,等价写法只放行第一个

## 对照

同一个 GP、同一个奖励、同样的预算与随机种子、同一个算子库;不带种子、不过指引、均匀采样。

## 证据

| 臂 | 付费评估 | 没过门槛 | 活着的 | 互不等价的(存下来的前 80 里) | 分数 ≥ 0 | 分数 ≥ 0.1 | 分数 ≥ 0.2 | 分数 ≥ 0.3 | 最好 | 前五(互不等价)均值 | 过线且不在已知池里、互不重复 | 用时 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 带指引 | 172 | 43 | 129 | 78 / 80 | 78 | 65 | 43 | 21 | +0.46 | +0.42 | — | 19 分 |

分数的含义:已知族把候选最高的两成排到最后之后的纯多头夏普减已知族自己的,train 与 valid 取较差的。「分数 ≥」各列数的是互不等价的候选。

带指引的一臂提出了 392 棵树:封禁 0、不在想法邻域 74、按权重抽掉 56、与已提过的等价 39、放行 223。

## 各臂找到的(互不等价的前几个;纯多头夏普 train / valid 是奖励口径下的)

**带指引**

- +0.46(train +2.24 / valid +3.94,半衰期 20,与已知族相关 +0.23):`cs_bucket_rank(day_zero_ratio(nt_ts_var(Close, 10)), day_sum(High))`
- +0.46(train +2.24 / valid +3.94,半衰期 20,与已知族相关 +0.23):`cs_bucket_rank(cs_bucket_rank(day_zero_ratio(nt_ts_var(Close, 10)), day_sum(High)), day_sum(High))`
- +0.42(train +2.20 / valid +3.91,半衰期 20,与已知族相关 +0.29):`cs_first_high40(cs_bucket_rank(day_zero_ratio(nt_ts_var(Close, 10)), day_sum(High)), cs_bucket_rank(day_zero_ratio(nt_ts_var(Close, 5)), day_sum(High)))`
- +0.40(train +2.18 / valid +3.89,半衰期 20,与已知族相关 +0.50):`cross_mean(cs_bucket_rank(day_zero_ratio(nt_ts_var(Close, 5)), day_zero_ratio(nt_ts_var(High, 3))), 15)`
- +0.38(train +2.16 / valid +3.92,半衰期 5,与已知族相关 +0.41):`cross_mean(cs_bucket_zscore(day_zero_ratio(nt_ts_var(Close, 5)), day_autocorr_n1(High)), 15)`
- +0.36(train +2.14 / valid +3.93,半衰期 20,与已知族相关 +0.20):`cs_bucket_rank(day_zero_ratio(nt_ts_var(Close, 10)), day_sum(nt_ts_var(Close, 5)))`

## 信念更新

(待写:这次实验让哪条规则的权重 / 状态变了,为什么。)

