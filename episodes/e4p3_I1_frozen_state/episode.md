# 研究实验 `e4p3_I1_frozen_state`

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
| 带指引 | 145 | 54 | 87 | 80 / 80 | 63 | 45 | 7 | 0 | **0**(0 族) | +1.36 | +1.36 | — | 13 分 |
| 对照 | 147 | 33 | 111 | 80 / 80 | 80 | 28 | 0 | 0 | **0**(0 族) | +0.86 | +0.78 | — | 12 分 |

分数的含义:「候选改过的书」减「参照书」的逐日净超额之差在 train+valid 合并段上的信息比(任一段低于 −1 则取那一段);参照书 = 已知族;候选改过的书 = 已知族把候选最高两成(整块并列)排到最后。「分数 ≥」各列数的是互不等价的候选;「族」= 只差价格字段换名、或只在最外层多套一个保序函数的算一族。

带指引的一臂提出了 462 棵树:封禁 2、不在想法邻域 74、按权重抽掉 144、与已提过的等价 0、放行 226。

合并段的 5.6 年里 train 占 4 年,信息比被它主导;所以「发现」另外要求 train、valid 各自的成对信息比都过 0.5(`partura.steer.is_discovery`)。
这次的信息比是**带大小的**:账面每年多赚不到 1 个点的,按比例打折(`partura.steer._sized`)—— 又小又稳的改动不再算数。
筛子的参照:已做过通用冻结筛子的已知族(池子里最强的一个)。
代码指纹:`scripts/idea_search.py` 472605d6746f、`partura/steer.py` 21f384c16642、`partura/steer_fast.py` 9ee240714803、`partura/ops_ext.py` 48ec5dfee49d、`partura/books.py` ecd9009a1f4c、`guidance/B01.yaml` 3deac6f10101;奖励在 cuda 上算。

## 各臂找到的(算作发现的前几个,互不等价;括号里是两段各自的成对信息比)

**带指引**

- +1.36(带大小的成对信息比 train +1.96 / valid +0.27;每年多赚 train +0.8% / valid +0.3%,原始信息比 +2.57 / +1.05;改过的书的纯多头夏普 +2.86 / +4.20,半衰期 0,方向 +1):`sub(day_wstd(Amt, nt_cs_first_low20(Volume, High)), day_flat_run_max(nt_cs_first_low20(Volume, High)))`
- +1.36(带大小的成对信息比 train +1.96 / valid +0.27;每年多赚 train +0.8% / valid +0.3%,原始信息比 +2.57 / +1.05;改过的书的纯多头夏普 +2.86 / +4.20,半衰期 0,方向 +1):`sub(sub(day_wstd(Amt, nt_cs_first_low20(Volume, High)), day_flat_run_max(nt_cs_first_low20(Volume, High))), day_flat_run_max(High))`
- +1.36(带大小的成对信息比 train +1.96 / valid +0.27;每年多赚 train +0.8% / valid +0.3%,原始信息比 +2.57 / +1.05;改过的书的纯多头夏普 +2.86 / +4.20,半衰期 0,方向 +1):`sub(sub(sub(day_wstd(Amt, nt_cs_first_low20(Volume, High)), day_flat_run_max(nt_cs_first_low20(Volume, High))), day_flat_run_max(High)), day_at_min_ratio(High))`
- +1.36(带大小的成对信息比 train +1.96 / valid +0.27;每年多赚 train +0.8% / valid +0.3%,原始信息比 +2.57 / +1.05;改过的书的纯多头夏普 +2.86 / +4.20,半衰期 0,方向 +1):`sub(sub(day_wstd(Amt, nt_cs_first_low20(Volume, High)), day_flat_run_max(nt_cs_first_low20(Volume, High))), day_flat_run_max(Volume))`
- +1.36(带大小的成对信息比 train +1.96 / valid +0.27;每年多赚 train +0.8% / valid +0.3%,原始信息比 +2.57 / +1.05;改过的书的纯多头夏普 +2.86 / +4.20,半衰期 0,方向 +1):`add(sub(day_wstd(Amt, nt_cs_first_low20(Volume, High)), day_flat_run_max(nt_cs_first_low20(Volume, High))), day_flat_run_max(High))`
- +1.22(带大小的成对信息比 train +1.84 / valid +0.16;每年多赚 train +0.8% / valid +0.2%,原始信息比 +2.45 / +0.82;改过的书的纯多头夏普 +2.85 / +4.19,半衰期 0,方向 +1):`sub(day_wstd(Amt, nt_cs_first_low20(Amt, High)), day_flat_run_max(nt_cs_first_low20(Amt, High)))`

**对照**

- +0.86(带大小的成对信息比 train +1.15 / valid +0.28;每年多赚 train +0.7% / valid +0.3%,原始信息比 +1.64 / +1.07;改过的书的纯多头夏普 +2.85 / +4.16,半衰期 5,方向 -1):`cs_last_high20(day_sum(Open), div(day_quantile(High), day_signed_ratio(Amt, High)))`
- +0.79(带大小的成对信息比 train +1.16 / valid +0.12;每年多赚 train +0.7% / valid +0.2%,原始信息比 +1.58 / +0.64;改过的书的纯多头夏普 +2.85 / +4.15,半衰期 5,方向 +1):`div(day_open(Vwap), day_signed_ratio(Amt, High))`
- +0.78(带大小的成对信息比 train +1.35 / valid -0.14;每年多赚 train +0.7% / valid -0.0%,原始信息比 +1.87 / -0.14;改过的书的纯多头夏普 +2.85 / +4.12,半衰期 20,方向 +1):`cs_last_high20(day_signed_ratio(Amt, Open), add(day_open(Amt), day_signed_ratio(Amt, Open)))`
- +0.73(带大小的成对信息比 train +1.10 / valid +0.09;每年多赚 train +0.7% / valid +0.2%,原始信息比 +1.54 / +0.54;改过的书的纯多头夏普 +2.85 / +4.15,半衰期 5,方向 +1):`div(day_open(Open), day_signed_ratio(Amt, Open))`
- +0.73(带大小的成对信息比 train +1.09 / valid +0.09;每年多赚 train +0.7% / valid +0.2%,原始信息比 +1.54 / +0.54;改过的书的纯多头夏普 +2.85 / +4.15,半衰期 5,方向 +1):`div(day_open(Open), day_signed_ratio(Amt, High))`
- +0.73(带大小的成对信息比 train +1.09 / valid +0.09;每年多赚 train +0.7% / valid +0.2%,原始信息比 +1.54 / +0.54;改过的书的纯多头夏普 +2.85 / +4.15,半衰期 5,方向 +1):`div(day_open(High), day_signed_ratio(Volume, Open))`

## 信念更新

**种子 3(参照 = 已做通用冻结筛子的已知族):两臂都是 0 族发现;三个种子合计 0 对 0(`episodes/e4_SUMMARY.md`)。**

- 通用冻结筛子之外,这个邻域里没有可剔的票了;带指引也没有制造出假发现。

