来源:挖掘库 / #953(批次 `B01_single_factors`)。表达式:

```
ts_spearman(day_quantile(Close), 10)
```

配置里记录的用户发布行(`configs/F111_spearman_qclose.yaml` 的 `published` 字段,pick_single_factors
口径):`sign=+1, hl=10, ls=[2.62, 1.1], long=[0.164, 0.075]`。这一行用的是**多空口径**选半衰期
(`hl=10` 对应的是 hlS,不是现在 playbook §0 定的 hlL);数值对应关系见 `06_baseline.md`。

## 逐层拆开

```
叶子   Close                     分钟级字段(face dt 的输入),价格类(见下)
节点 A  day_quantile(Close)      折叠日内分钟轴 M → 每股票-日一个标量
节点 B  ts_spearman(A, 10)       沿交易日轴 D 滚动 10 天 → 因子输出(根)
```

- **`Close` 字段**:`partura/propose.py:51-56` 的字段分类表把 `Open/High/Low/Close/Vwap` 标成
  `"price"` 类,并在注释里写明"生产 cube 里 `Amt`/`Volume` 是不复权(raw)的,价格类字段是复权
  (back-adjusted)的,二者不能互换"。`Close` 在这里的轴是 **M(日内分钟)**——它是分钟级的收盘价
  序列,不是单一的"当天收盘价"标量(单一标量的当天收盘价是 `day_last(Close)`,参见
  `ctl_price: log(day_last(Close))`)。

- **节点 A = `day_quantile(Close)`**:表达式只传了 1 个位置参数,**没有传 `q`**。`day_quantile`
  的签名是 `day_quantile(x, q: float = 0.5)`(见 `02_operators.md`),所以这里实际调用的是
  **默认值 q=0.5**,即:
  ```
  A[日, 股票] = 当天分钟 Close 序列的中位数  =  nanquantile(Close_当天各分钟, 0.5)
  ```
  S0_baseline 已经成功求值(`runs/F111_spearman_qclose/S0_baseline.json` 有完整数字,不是报错),
  说明引擎确实接受省略 `q` 的调用、落到 Python 默认参数,而不是报"缺参数"的错。
  **这一点和因子名字("qclose",暗示某个特别选的分位点)不一致**——实际算的是日内中位价,
  不是高分位或低分位,见 `02_operators.md` 里单独标出的一条。

- **节点 B(根)= `ts_spearman(A, 10)`**:精确语义见 `02_operators.md`——它不是"A 和过去的自己"
  的秩相关,而是对每只股票 i,把它最近 10 个交易日的 A 路径,分别和**同一 10 天窗口里每一只其他
  股票 j** 的 A 路径做 Spearman(秩)相关,再对所有 j≠i 取**截面平均**(`agg="mean"`,默认;
  `abs_corr=False`,默认)。

## 整条表达式在算什么(一句话 + 公式)

一句话:**每只股票最近 10 个交易日"日内收盘中位价"的路径,和同期全市场其他每只股票的同一条路径,
按秩计算 Pearson 相关(即 Spearman 相关),再对所有其他股票取平均**。

公式(d=10,i 为目标股票,t 为交易日,窗口 [t-9, t]):

```
A[t, n]        = nanquantile_{m∈当天分钟}( Close[t, n, m], 0.5 )              对每只股票 n

rank_i[t, k]   = A[t-9+k, i] 在 {A[t-9, i], …, A[t, i]} 里的秩,k = 0..9        (NaN 天不参与排名)
rc_i[t, k]     = rank_i[t, k] − mean_k(rank_i[t, k])

corr(t, i, j)  = Σ_k rc_i[t,k]·rc_j[t,k]  /  ( ‖rc_i[t,·]‖ · ‖rc_j[t,·]‖ + 1e-8 )   (= 窗口内 i,j 的 Spearman 相关)

F111[t, i]     = mean_{j≠i}  corr(t, i, j)
```

以上只是把计算过程写清楚,不包含"这个量在经济上代表什么"的判断——那是主研的工作。
