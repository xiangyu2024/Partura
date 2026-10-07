# 研究实验 `e4k3_I1_frozen_state`

想法 `I1_frozen_state`;奖励 `long_screen`;每臂预算 192 个候选(种群 48,随机种子 3);搜索只看 20180102–20230807(其中 20220101 起算 valid),测试段没有打开。

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
| 带指引 | 130 | 46 | 84 | 80 / 80 | 59 | 38 | 26 | 16 | **13**(13 族) | +3.16 | +2.52 | 9 | 12 分 |
| 对照 | 155 | 38 | 112 | 80 / 80 | 80 | 58 | 39 | 29 | **3**(3 族) | +2.41 | +2.40 | 2 | 15 分 |

分数的含义:「候选改过的书」减「参照书」的逐日净超额之差在 train+valid 合并段上的信息比(任一段低于 −1 则取那一段);参照书 = 已知族;候选改过的书 = 已知族把候选最高两成(整块并列)排到最后。「分数 ≥」各列数的是互不等价的候选;「族」= 只差价格字段换名、或只在最外层多套一个保序函数的算一族。

带指引的一臂提出了 326 棵树:封禁 2、不在想法邻域 55、按权重抽掉 22、与已提过的等价 2、放行 240。

合并段的 5.6 年里 train 占 4 年,信息比被它主导;所以「发现」另外要求 train、valid 各自的成对信息比都过 0.5(`partura.steer.is_discovery`)。
这次的信息比是**带大小的**:账面每年多赚不到 1 个点的,按比例打折(`partura.steer._sized`)—— 又小又稳的改动不再算数。
筛子的参照:没做过筛子的已知族。
代码指纹:`scripts/idea_search.py` 472605d6746f、`partura/steer.py` 21f384c16642、`partura/steer_fast.py` 9ee240714803、`partura/ops_ext.py` 48ec5dfee49d、`partura/books.py` ecd9009a1f4c、`guidance/B01.yaml` 3deac6f10101;奖励在 cuda 上算。

## 各臂找到的(算作发现的前几个,互不等价;括号里是两段各自的成对信息比)

**带指引**

- +3.16(带大小的成对信息比 train +3.47 / valid +2.23;每年多赚 train +2.9% / valid +1.3%,原始信息比 +3.47 / +2.23;改过的书的纯多头夏普 +2.23 / +3.70,半衰期 0,方向 +1):`ts_decay_linear(cross_scale(cross_max(day_flat_run_max(Ret), 60), 3), 50)`
- +2.44(带大小的成对信息比 train +2.41 / valid +2.67;每年多赚 train +1.3% / valid +1.0%,原始信息比 +2.41 / +2.67;改过的书的纯多头夏普 +1.98 / +3.65,半衰期 0,方向 +1):`cross_max(ts_delta(cross_scale(day_flat_run_max(Ret), 60), 50), 30)`
- +2.39(带大小的成对信息比 train +2.62 / valid +1.79;每年多赚 train +3.0% / valid +2.0%,原始信息比 +2.62 / +1.79;改过的书的纯多头夏普 +2.25 / +3.89,半衰期 20,方向 +1):`cross_scale(day_flat_run_max(Ret), 60)`
- +2.35(带大小的成对信息比 train +2.41 / valid +2.26;每年多赚 train +2.8% / valid +3.2%,原始信息比 +2.41 / +2.26;改过的书的纯多头夏普 +2.23 / +4.12,半衰期 20,方向 +1):`cross_scale(day_flat_run_max(Ret), 241)`
- +2.28(带大小的成对信息比 train +2.31 / valid +2.06;每年多赚 train +1.2% / valid +0.9%,原始信息比 +2.31 / +2.25;改过的书的纯多头夏普 +1.96 / +3.64,半衰期 0,方向 +1):`cross_max(ts_delta(cross_scale(cross_scale(cross_scale(day_flat_run_max(Ret), 60), 60), 60), 50), 30)`
- +2.10(带大小的成对信息比 train +2.51 / valid +0.66;每年多赚 train +2.3% / valid +0.7%,原始信息比 +2.51 / +0.92;改过的书的纯多头夏普 +2.15 / +3.66,半衰期 20,方向 +1):`cross_scale(cross_scale(day_flat_run_max(Ret), 60), 60)`
- +2.09(带大小的成对信息比 train +2.21 / valid +1.74;每年多赚 train +2.6% / valid +1.8%,原始信息比 +2.21 / +1.74;改过的书的纯多头夏普 +2.20 / +3.80,半衰期 0,方向 +1):`ts_decay_linear(cross_scale(day_flat_run_max(Ret), 60), 50)`
- +2.04(带大小的成对信息比 train +2.13 / valid +1.80;每年多赚 train +2.6% / valid +2.0%,原始信息比 +2.13 / +1.80;改过的书的纯多头夏普 +2.21 / +3.86,半衰期 0,方向 +1):`ts_decay_linear(cross_scale(day_flat_run_max(Open), 60), 50)`

**对照**

- +1.32(带大小的成对信息比 train +1.27 / valid +1.45;每年多赚 train +1.1% / valid +1.3%,原始信息比 +1.27 / +1.45;改过的书的纯多头夏普 +1.98 / +3.71,半衰期 5,方向 +1):`cs_first_high20(cs_last_low40(day_min(Amt), day_open(High)), div(day_open(High), day_open(High)))`
- +1.11(带大小的成对信息比 train +1.22 / valid +0.57;每年多赚 train +1.1% / valid +0.6%,原始信息比 +1.22 / +0.95;改过的书的纯多头夏普 +2.00 / +3.62,半衰期 20,方向 -1):`ts_pearson(add(day_zero_ratio(High), day_min(Open)), 50)`
- +1.10(带大小的成对信息比 train +1.21 / valid +0.57;每年多赚 train +1.1% / valid +0.6%,原始信息比 +1.21 / +0.96;改过的书的纯多头夏普 +2.00 / +3.62,半衰期 20,方向 -1):`ts_pearson(day_min(Close), 50)`

## 信念更新

**种子 3(参照 = 未筛的已知族):带指引 13 族发现,对照 3 族;三个种子合计 44 对 4,按事先的标准成立(`episodes/e4_SUMMARY.md`)。**

- 带指引一臂过线的全是搜出来的变体,没有种子本身。
- 这些是样本内的筛子;能不能用要看按规则的测试段读数(K001 的结论是这一类样本外没站住)。

