**来历**:挖掘库(机械挖掘产物),编号 `#1421`(`batches/B01_single_factors.yaml` 第 32 行;`configs/F114_q25_closeret.yaml` 的 `published` 字典)。
没有人工命名或自然语言描述流传下来 —— 挖掘库条目只有编号,"这棵树在算什么"要靠读表达式和内核源码重建,不能按 `#1421` 这个编号本身得到任何信息。

**表达式**(原样):

```
cross_quantile_q25(day_close(Ret), 15)
```

**逐层拆开**(详细算子语义见 `02_operators.md`,逐层公式见 `03_decomposition.md`):

```
A = day_close(Ret)              # 每只股票、每个交易日一个数
B = cross_quantile_q25(A, 15)   # 对 A 的最近 15 个交易日(含当天)取 0.25 分位数
因子 = B
```

- `Ret` 是逐分钟字段(逐分钟收益)。证据:`configs/F114_q25_closeret.yaml` 自己把 `ctl_ivol` 定义为 `day_std(Ret)` 并注释"日内已实现波动"
  —— 这是已实现波动的标准构造(逐分钟步进收益的标准差),说明 `Ret` 在这个项目里是"逐分钟步进的收益",不是从开盘累计的路径值。
  旁证:`notes/F001_dwgated_covamtlow/07_S5_fields.md` 把 `Low` 换成 `Ret` 称为"换成分钟收益";`notes/F102_kurt_autocorr/02_operators.md`
  把 `nt_ts_autocorr_s1(Ret,3)` 读成"4 个连续分钟收益上的 3 对 Pearson 相关"。两份都是别的因子的研究笔记,只作旁证,不是本次直接验证的结论。
- `day_close(x)` 的内核定义是 `day_last(x)` 的别名 —— "取当天最后一个非 NaN 的值"(见 `02_operators.md`)。
  **喂进来的是 `Ret` 而不是价格字段**,所以 `A` 取到的是"当天最后一个有效分钟自己的那一笔分钟收益",不是收盘价,也不是"开盘到收盘的当日总收益"。
- `cross_quantile_q25(A, 15)` 是对 `A` 这个"每天一个数"的序列,按交易日轴做因果滚动(窗口 15,含当天),取 0.25 分位数。

**一句话**(只摘录机械事实,不含对"这是什么"的判断):这条因子 = 对"每天最后一个有效分钟的分钟收益"这个每日序列,滚动 15 个交易日取下四分位数。
方向 `sign = -1`(`published.sign` 与 S0 在 `train` 上独立选出的方向一致)。

**与用户发布值的对照**(只列事实性对照,解读与候选判断不在本文件;完整基线数字见 `06_baseline.md`):

- `configs/F114_q25_closeret.yaml` 的 `published` 字典:`sign: -1, hl: 20, ls: [2.36, 0.91], long: [0.059, 0.023]`。
- S0_baseline 在 `utrain`(用户训练段)上独立复现:方向 `-1`、半衰期 `20`(多头口径与多空口径两种选法都选到 20,见 `06_baseline.md` §2);
  扣费多空夏普 `+2.36`、多头腿**毛**超额 `+5.9%` —— 与 `published.ls[0]`、`published.long[0]` 两个数字分别对上。
  `published.long` 对应的是**毛超额**,不是净超额;Partura 额外算出的多头腿**净**超额(`utrain +3.6%`)是用户原表里没有的列。
- `holdout`(用户测试段)未读(`runs/F114_q25_closeret/ledger.json` 里没有 `holdout` 记录),`published.ls[1]=0.91`、`published.long[1]=0.023`
  是用户自己原表的数字,本次没有、也不应该用 Partura 自己的计算去核对它。
