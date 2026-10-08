# 研究实验 `e5sh1_I1_frozen_state`

想法 `I1_frozen_state`;奖励 `long_screen`;每臂预算 192 个候选(种群 48,随机种子 1);搜索只看 20180102–20230807(其中 20220101 起算 valid),测试段没有打开。

## 假设

盘口冻结(封板、停牌前后、无成交)是一个持续几周的状态,处在这个状态里的票系统性跑输;哪一种「冻结度」的写法、多长的记忆最能标出它

## 干预(带指引的一臂)

- 种子进首代:`cross_max(day_zero_ratio(Ret), 15)`、`cross_mean(day_flat_ratio(Close), 15)`、`cross_max(day_flat_run_max(Close), 15)`、`cross_mean(day_zero_ratio(Amt), 30)`
- 想法里的算子采样概率 × 8.0;候选必须含这些算子之一:day_zero_ratio、day_flat_ratio、day_flat_run_max、day_distinct_ratio、day_at_max_ratio、day_at_min_ratio
- 每棵候选树过指引 `guidance/B01.yaml`:封禁的不放行,降权 / 升权按概率放行,等价写法只放行第一个

## 对照

同一个 GP、同一个奖励、同样的预算与随机种子、同一个算子库;不带种子、不过指引、均匀采样。

## 证据

| 臂 | 付费评估 | 没过门槛 | 活着的 | 互不等价的(存下来的前 80 里) | 分数 ≥ 0 | 分数 ≥ 0.5 | 分数 ≥ 1 | 分数 ≥ 1.5 | **发现(合并段 ≥ 1 且两段各 ≥ 0.5)** | 最好 | 前五(互不等价)均值 | 过线且不在已知池里、互不重复 | 用时 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 带指引 | 146 | 71 | 71 | 71 / 71 | 64 | 50 | 38 | 24 | **13**(11 族) | +2.40 | +2.23 | 2 | 15 分 |

分数的含义:「候选改过的书」减「参照书」的逐日净超额之差在 train+valid 合并段上的信息比(任一段低于 −1 则取那一段);参照书 = 已知族;候选改过的书 = 已知族把候选最高两成(整块并列)排到最后。「分数 ≥」各列数的是互不等价的候选;「族」= 只差价格字段换名、或只在最外层多套一个保序函数的算一族。

带指引的一臂提出了 254 棵树:封禁 0、不在想法邻域 24、按权重抽掉 0、与已提过的等价 0、放行 230。

合并段的 5.6 年里 train 占 4 年,信息比被它主导;所以「发现」另外要求 train、valid 各自的成对信息比都过 0.5(`partura.steer.is_discovery`)。
这次的信息比是**带大小的**:账面每年多赚不到 1 个点的,按比例打折(`partura.steer._sized`)—— 又小又稳的改动不再算数。
筛子的参照:没做过筛子的已知族。
代码指纹:`scripts/idea_search.py` 51248194fc24、`partura/steer.py` 21f384c16642、`partura/steer_fast.py` 9ee240714803、`partura/ops_ext.py` 48ec5dfee49d、`partura/books.py` ecd9009a1f4c、`guidance/B01.yaml` 8214d7cca7a7;奖励在 cuda 上算。

## 各臂找到的(算作发现的前几个,互不等价;括号里是两段各自的成对信息比)

**带指引**

- +1.46(带大小的成对信息比 train +1.43 / valid +1.67;每年多赚 train +1.3% / valid +0.9%,原始信息比 +1.43 / +1.81;改过的书的纯多头夏普 +2.01 / +3.64,半衰期 0,方向 -1):`neg(cross_stddev(day_flat_run_max(Low), 30))`
- +1.44(带大小的成对信息比 train +1.42 / valid +1.50;每年多赚 train +1.9% / valid +2.0%,原始信息比 +1.42 / +1.50;改过的书的纯多头夏普 +2.11 / +3.97,半衰期 20,方向 +1):`neg(sigmoid(cross_stddev(sigmoid(sigmoid(sigmoid(cross_stddev(day_flat_run_max(Ret), 30)))), 241)))`
- +1.44(带大小的成对信息比 train +1.43 / valid +1.48;每年多赚 train +1.9% / valid +2.0%,原始信息比 +1.43 / +1.48;改过的书的纯多头夏普 +2.11 / +3.97,半衰期 20,方向 -1):`pow_2(sigmoid(cross_stddev(pow_2(sigmoid(cross_stddev(day_flat_run_max(Ret), 30))), 241)))`
- +1.44(带大小的成对信息比 train +1.43 / valid +1.47;每年多赚 train +1.9% / valid +1.9%,原始信息比 +1.43 / +1.47;改过的书的纯多头夏普 +2.11 / +3.97,半衰期 20,方向 -1):`pow_2(sigmoid(cross_stddev(cross_stddev(day_flat_run_max(Ret), 30), 241)))`
- +1.44(带大小的成对信息比 train +1.42 / valid +1.50;每年多赚 train +1.8% / valid +2.0%,原始信息比 +1.42 / +1.50;改过的书的纯多头夏普 +2.11 / +3.97,半衰期 20,方向 -1):`pow_2(sigmoid(cross_stddev(sigmoid(sigmoid(sigmoid(cross_stddev(day_flat_run_max(Ret), 30)))), 241)))`
- +1.43(带大小的成对信息比 train +1.41 / valid +1.49;每年多赚 train +1.8% / valid +2.0%,原始信息比 +1.41 / +1.49;改过的书的纯多头夏普 +2.11 / +3.97,半衰期 20,方向 -1):`pow_2(sigmoid(cross_stddev(sigmoid(sigmoid(cross_stddev(day_flat_run_max(Ret), 30))), 241)))`
- +1.38(带大小的成对信息比 train +1.43 / valid +1.26;每年多赚 train +1.9% / valid +1.7%,原始信息比 +1.43 / +1.26;改过的书的纯多头夏普 +2.10 / +3.93,半衰期 20,方向 -1):`pow_2(sigmoid(cross_stddev(sigmoid(sigmoid(cross_stddev(day_flat_run_max(Ret), 60))), 241)))`
- +1.31(带大小的成对信息比 train +1.16 / valid +1.66;每年多赚 train +1.2% / valid +1.8%,原始信息比 +1.16 / +1.66;改过的书的纯多头夏普 +1.98 / +3.86,半衰期 20,方向 -1):`cross_stddev(day_flat_run_max(Ret), 241)`

## 信念更新

**消融的一格(带指引一臂只开:种子 + 邻域;种子 1):146 次付费评估,实测互不相关的发现 2 个。单看一个 run 不作结论,八格合读见 `episodes/e5_SUMMARY.md`。**

