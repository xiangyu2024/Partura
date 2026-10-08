# 研究实验 `e5h2_I1_frozen_state`

想法 `I1_frozen_state`;奖励 `long_screen`;每臂预算 192 个候选(种群 48,随机种子 2);搜索只看 20180102–20230807(其中 20220101 起算 valid),测试段没有打开。

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
| 带指引 | 141 | 51 | 87 | 79 / 80 | 74 | 38 | 18 | 2 | **10**(7 族) | +1.78 | +1.47 | 2 | 16 分 |

分数的含义:「候选改过的书」减「参照书」的逐日净超额之差在 train+valid 合并段上的信息比(任一段低于 −1 则取那一段);参照书 = 已知族;候选改过的书 = 已知族把候选最高两成(整块并列)排到最后。「分数 ≥」各列数的是互不等价的候选;「族」= 只差价格字段换名、或只在最外层多套一个保序函数的算一族。

带指引的一臂提出了 278 棵树:封禁 0、不在想法邻域 28、按权重抽掉 0、与已提过的等价 0、放行 250。

合并段的 5.6 年里 train 占 4 年,信息比被它主导;所以「发现」另外要求 train、valid 各自的成对信息比都过 0.5(`partura.steer.is_discovery`)。
这次的信息比是**带大小的**:账面每年多赚不到 1 个点的,按比例打折(`partura.steer._sized`)—— 又小又稳的改动不再算数。
筛子的参照:没做过筛子的已知族。
代码指纹:`scripts/idea_search.py` 51248194fc24、`partura/steer.py` 21f384c16642、`partura/steer_fast.py` 9ee240714803、`partura/ops_ext.py` 48ec5dfee49d、`partura/books.py` ecd9009a1f4c、`guidance/B01.yaml` 8214d7cca7a7;奖励在 cuda 上算。

## 各臂找到的(算作发现的前几个,互不等价;括号里是两段各自的成对信息比)

**带指引**

- +1.78(带大小的成对信息比 train +1.92 / valid +1.95;每年多赚 train +1.6% / valid +3.6%,原始信息比 +1.92 / +1.95;改过的书的纯多头夏普 +1.99 / +4.15,半衰期 20,方向 -1):`cross_ema(sigmoid(cross_semistd_neg(day_at_max_ratio(Vwap), 241)), 241)`
- +1.67(带大小的成对信息比 train +1.87 / valid +1.76;每年多赚 train +1.5% / valid +3.3%,原始信息比 +1.87 / +1.76;改过的书的纯多头夏普 +1.99 / +4.09,半衰期 5,方向 -1):`cross_ema(cross_semistd_neg(day_at_max_ratio(Vwap), 241), 241)`
- +1.30(带大小的成对信息比 train +1.26 / valid +1.41;每年多赚 train +1.0% / valid +1.5%,原始信息比 +1.26 / +1.41;改过的书的纯多头夏普 +1.92 / +3.80,半衰期 20,方向 -1):`cross_semistd_neg(day_at_max_ratio(Vwap), 241)`
- +1.19(带大小的成对信息比 train +0.84 / valid +1.63;每年多赚 train +0.8% / valid +3.6%,原始信息比 +1.03 / +1.63;改过的书的纯多头夏普 +1.89 / +4.13,半衰期 20,方向 -1):`cross_ema(cross_ema(cross_ema(cross_semistd_neg(day_at_max_ratio(in_regres(Ret, Amt, 5)), 241), 241), 241), 241)`
- +1.17(带大小的成对信息比 train +0.86 / valid +1.55;每年多赚 train +0.8% / valid +3.0%,原始信息比 +1.05 / +1.55;改过的书的纯多头夏普 +1.89 / +4.01,半衰期 20,方向 -1):`cross_ema(cross_ema(cross_ema(cross_ema(day_at_max_ratio(in_regres(Ret, Amt, 10)), 241), 241), 5), 241)`
- +1.11(带大小的成对信息比 train +0.79 / valid +1.41;每年多赚 train +0.8% / valid +2.5%,原始信息比 +1.03 / +1.41;改过的书的纯多头夏普 +1.88 / +3.96,半衰期 20,方向 -1):`cross_ema(cross_ema(day_at_max_ratio(in_regres(Ret, Amt, 10)), 241), 241)`
- +1.03(带大小的成对信息比 train +0.54 / valid +1.45;每年多赚 train +0.5% / valid +1.9%,原始信息比 +1.00 / +1.45;改过的书的纯多头夏普 +1.85 / +3.83,半衰期 5,方向 -1):`cross_ema(cross_ema(day_at_max_ratio(in_regres(Ret, Amt, 5)), 241), 241)`

## 信念更新

**消融的一格(带指引一臂只开:邻域;种子 2):141 次付费评估,实测互不相关的发现 2 个。单看一个 run 不作结论,八格合读见 `episodes/e5_SUMMARY.md`。**

