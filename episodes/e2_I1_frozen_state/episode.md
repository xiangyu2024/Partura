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

| 臂 | 付费评估 | 没过门槛 | 活着的 | 互不等价的(存下来的前 80 里) | 分数 ≥ 0 | 分数 ≥ 0.1 | 分数 ≥ 0.2 | 分数 ≥ 0.3 | **发现(分数 ≥ 0.2)** | 最好 | 前五(互不等价)均值 | 过线且不在已知池里、互不重复 | 用时 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 带指引 | 172 | 43 | 129 | 77 / 80 | 77 | 64 | 41 | 19 | **41**(40 族) | +0.46 | +0.40 | 6 | 19 分 |
| 对照 | 152 | 29 | 123 | 80 / 80 | 80 | 52 | 35 | 19 | **35**(34 族) | +0.45 | +0.43 | 10 | 23 分 |

分数的含义:已知族把候选最高的两成排到最后之后的纯多头夏普减已知族自己的,train 与 valid 取较差的(旧口径)。「分数 ≥」各列数的是互不等价的候选;「族」= 只差价格字段换名、或只在最外层多套一个保序函数的算一族。

带指引的一臂提出了 392 棵树:封禁 0、不在想法邻域 74、按权重抽掉 56、与已提过的等价 39、放行 223。

## 各臂找到的(互不等价的前几个;纯多头夏普 train / valid 是奖励口径下的)

**带指引**

- +0.46(train +2.24 / valid +3.94,半衰期 20,与已知族相关 +0.23):`cs_bucket_rank(day_zero_ratio(nt_ts_var(Close, 10)), day_sum(High))`
- +0.42(train +2.20 / valid +3.91,半衰期 20,与已知族相关 +0.29):`cs_first_high40(cs_bucket_rank(day_zero_ratio(nt_ts_var(Close, 10)), day_sum(High)), cs_bucket_rank(day_zero_ratio(nt_ts_var(Close, 5)), day_sum(High)))`
- +0.40(train +2.18 / valid +3.89,半衰期 20,与已知族相关 +0.50):`cross_mean(cs_bucket_rank(day_zero_ratio(nt_ts_var(Close, 5)), day_zero_ratio(nt_ts_var(High, 3))), 15)`
- +0.38(train +2.16 / valid +3.92,半衰期 5,与已知族相关 +0.41):`cross_mean(cs_bucket_zscore(day_zero_ratio(nt_ts_var(Close, 5)), day_autocorr_n1(High)), 15)`
- +0.36(train +2.14 / valid +3.93,半衰期 20,与已知族相关 +0.20):`cs_bucket_rank(day_zero_ratio(nt_ts_var(Close, 10)), day_sum(nt_ts_var(Close, 5)))`
- +0.35(train +2.22 / valid +3.83,半衰期 20,与已知族相关 +0.53):`cross_mean(cs_bucket_rank(day_zero_ratio(nt_ts_var(Close, 5)), day_autocorr_n1(nt_ts_var(Close, 5))), 15)`
- +0.35(train +2.17 / valid +3.82,半衰期 20,与已知族相关 +0.36):`cs_bucket_rank(day_zero_ratio(nt_ts_var(Close, 5)), day_sum(High))`
- +0.35(train +2.13 / valid +4.07,半衰期 20,与已知族相关 +0.38):`cs_first_high40(day_flat_run_max(in_stddev_full(Open)), day_flat_run_max(Close))`

**对照**

- +0.45(train +2.23 / valid +4.07,半衰期 0,与已知族相关 +0.36):`cross_max(ts_min(ts_min(div(day_wstd(Low, Close), day_median(Low)), 20), 20), 60)`
- +0.43(train +2.21 / valid +3.92,半衰期 5,与已知族相关 +0.15):`ts_min(cross_max(div(day_wstd(Low, Close), day_median(Low)), 241), 20)`
- +0.43(train +2.21 / valid +3.92,半衰期 5,与已知族相关 +0.15):`ts_min(cross_max(div(day_wstd(Low, Low), day_median(Low)), 241), 20)`
- +0.42(train +2.26 / valid +3.90,半衰期 20,与已知族相关 +0.19):`cross_max(div(day_wstd(Low, Low), day_median(Low)), 241)`
- +0.42(train +2.26 / valid +3.89,半衰期 20,与已知族相关 +0.19):`cross_max(div(day_wstd(Low, Close), day_median(Close)), 241)`
- +0.42(train +2.25 / valid +3.89,半衰期 20,与已知族相关 +0.19):`cross_max(div(day_wstd(Low, Close), day_median(Low)), 241)`
- +0.41(train +2.19 / valid +3.94,半衰期 5,与已知族相关 +0.15):`cross_max(ts_min(cross_max(div(day_wstd(Low, Close), day_median(Close)), 241), 20), 10)`
- +0.37(train +2.15 / valid +3.98,半衰期 5,与已知族相关 +0.21):`cross_max(div(cross_max(div(day_wstd(Low, Close), day_median(Low)), 241), cross_max(ts_min(day_kurt(Amt), 20), 241)), 241)`

## 信念更新

**想法的邻域里确实有好筛子,但不带任何指引的搜索找到了一样好的 —— 「冻结盘口」不是特殊的,奖励太容易了。**

- 两臂打平:带指引的一臂付费评估 172 个,过线(≥0.2)的互不等价候选 41 个,最好 +0.46;对照臂评估 152 个,过线 35 个,最好 +0.45;≥0.3 的都是 19 个。
  每四个被评估的候选里就有一个「把它最高的两成从已知族里排掉」之后两段都比已知族好 0.2 夏普以上。
- 两臂找到的是两类不同的东西:
  - 带指引:`cs_bucket_rank(day_zero_ratio(nt_ts_var(Close, 10)), day_sum(High))` —— 10 分钟滚动方差为零的分钟占比,**在同价位的股票里**排名。
    低价股因为最小报价单位,零收益分钟天然多;按价位分桶把这部分假冻结扣掉了。这是人没写过、值得留下的写法。
  - 对照:`cross_max(div(day_wstd(Low, Close), day_median(Low)), 241)` —— 过去一年里相对价格的日内波动的最大值。它标出的是「一年内出过极端波动日」的票,与冻结盘口不是一回事,当筛子却一样好。
- 读法:已知族(买成交额波动小的)的多头书里有一条「垃圾尾巴」,任何能标出异常票的量 —— 冻结、极端波动、极端价位 —— 都能把它剔掉一部分。
  所以「对未筛过的已知族」的筛子奖励区分不了想法的好坏,也量不出指引的作用。**筛子类想法的参照必须是已经做过通用筛子的已知族**(`known_xfrozen`):问的是「在通用的冻结盘口筛子之外,它还多剔掉了什么」。主研们在第三轮已经各自得到同一条教训(「交账必须对通用筛子基准」)。
- 对规则的影响:
  1. `long_screen` 的参照改成可选,默认用池子里最强的那个(排掉冻结盘口的已知族);本实验按新参照、新口径(成对逐日差的信息比、整块并列的两成)重跑才算数。
  2. 两个新写法进下一轮批量扫描的通用变体:按价位分桶的冻结度、一年内极端日内波动的记忆,各当一次筛子,和 `k_known_xfrozen` 并排比。
  3. U5(状态筛子升权)的理由要改:不是「冻结盘口这个状态特别」,而是「已知族的书有垃圾尾巴,剔掉它是通用的一步」—— 应当做进奖励(R1),而不是让搜索去一遍遍重新发现。

