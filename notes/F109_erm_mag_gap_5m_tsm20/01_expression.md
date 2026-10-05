# 01 — 表达式与来历

> 事实类段落(R3 工单 §1 补齐)。只记来历与字面事实,不含判断;判断见 `09_diagnosis.md` / `10_distilled.md`。

## 来历

- 手写库 / `erm_mag_gap_5m_tsm20`,批次 `B01_single_factors`。
- 完整表达式(程序化从 `configs/F109_erm_mag_gap_5m_tsm20.yaml` 的 `expression` 字段整行提取,未手工转录):

```
ts_mean(sub(div(div(day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95)), sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), create_like(Close, 0))), add(day_sum(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95))), create_like(day_quantile(Ret, 0.95), 1e-06))), add(day_quantile(Ret, 0.95), create_like(day_quantile(Ret, 0.95), 1e-06))), div(div(day_sum(select_where(is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05)), abs_(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1))), create_like(Close, 0))), add(day_sum(is_lt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.05))), create_like(day_quantile(Ret, 0.05), 1e-06))), add(abs_(day_quantile(Ret, 0.05)), create_like(day_quantile(Ret, 0.05), 1e-06)))), 20)
```

## 一句话

每天把 236 个 5 分钟收益分成上尾(> 当天 1 分钟收益 `Ret` 的 95% 分位)与下尾(< 5% 分位)两组,
各算「超阈均值 ÷ 该侧分位阈值」,两侧相减,再取 20 日均值。

## 关键的「名字骗人」之处

(照抄 `03_decomposition.md`,未重新推导)

- `in_delay(Close, 5)` 不跨日。
- 分位数阈值用的是 **1 分钟** `Ret`,而分子是 **5 分钟**收益(尺度错配)。
- `Ret` 首根恰好为 0 ⇒ 全天上涨分钟 ≤12 根时 `q95` **精确为 0** ⇒ 分母上的 `1e-6` 把涨跌停封板日炸成 10³~10⁵。
- `abs_` 只在下侧。
- 没有任何截面算子、不用量/额字段。

## 口径

- `rank_by: long`(选拔只看多头腿,即用户实际能做的那本书);方向与半衰期只在 fit 段(`train`)定。
- 成本 `cost_per_side: 0.0015`(单边 15bp,钱的数字都已扣除)。
- `train` 2018-01-02~2021-12-31;`valid` 2022-01-01~2023-08-07;
  `utrain`(= train+valid,用户训练段)2018-01-02~2023-08-07;`holdout`(用户测试段)2023-08-08 起。

来源:以上要点均已在 `03_decomposition.md`、`04_grammar.md`、`configs/F109_erm_mag_gap_5m_tsm20.yaml` 中给出;
本文件按 R3 工单 §1 的要求,把「来历 + 表达式 + 一句话」集中整理成独立的事实类说明,不新增任何判断或结论。
