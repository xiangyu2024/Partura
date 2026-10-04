# 01 · 来历与逐层拆解

> 本文只记事实,不下结论。公式均来自 `./scripts/study.sh src <op>` 读到的服务器端内核源码
> (AlphaCube commit `1698296`,无本地改动;Partura code sha `36543cfd8cc8`;见 `runs/F112_scale_spow_masktop/S0_baseline.json.provenance`)。

## 来历

- `factor_id`: `F112_scale_spow_masktop`
- 来源:挖掘库 `#574`,批次 `B01_single_factors`
- 原始表达式(逐字,来自 `configs/F112_scale_spow_masktop.yaml`):

  ```
  ts_scale(signedpower(cs_mask_top_replace_mean_neg(add(day_quantile(Close), day_kurt(High)))), 30)
  ```

- 用户表公布的那一行(`configs/F112_scale_spow_masktop.yaml` 的 `published:` 字段):
  `sign=-1, hl=20, ls=[2.58, 2.64]`(多空夏普,[utrain, holdout]),`long=[0.089, 0.125]`(多头腿毛超额,[utrain, holdout])。
- `S0_baseline` 已在服务器上跑完(`runs/F112_scale_spow_masktop/S0_baseline.json`,耗时 181.5s,峰值显存 3.04GB),
  Partura 自己求值复现方向 `sign=-1`、半衰期(多头口径与多空口径都选到)`hl=20`,与公布值同一个格点。
  **数值上有微小出入**,记在下面「与公布值的出入」,细节(含候选机制)见 `06_baseline.md`。

## 表达式树

```
expr = ts_scale(signedpower(cs_mask_top_replace_mean_neg(add(day_quantile(Close), day_kurt(High)))), 30)

A = day_quantile(Close)                     叶子: Close
B = day_kurt(High)                          叶子: High
C = add(A, B)
D = cs_mask_top_replace_mean_neg(C)
E = signedpower(D)
F = ts_scale(E, 30)                         F 就是因子最终输出
```

节点数 8(含 2 个叶子字段),去重后 6 个中间量(A~F),深度 6,每个节点被引用 1 次(无重复子树)。
用到的字段只有 `Close`、`High`。全树只有 `ts_scale` 一个跨交易日的节点(窗口 30),其余 5 个节点都不跨日
(逐日独立计算,或是当天内部的运算)——详见 `03_decomposition.md`。

## 逐层:它在算什么(一句话 + 公式,机械描述,非经济解读)

| 节点 | 公式(字面,未化简) | 一句话:它在算什么 |
|---|---|---|
| `A` | `nanquantile(Close, 0.5, dim=分钟轴)` (`day_quantile` 的 `q` 未传,用默认值 0.5) | 这只股票**当天**全部 1 分钟 `Close` 的**中位数**(日内分钟轴折叠成一个值) |
| `B` | 总体矩算出的 Fisher 超额峰度(`m4/var² − 3` 这一类公式,见 `02_operators.md`「`_kurt` 源码未读到」的说明) | 这只股票**当天**全部 1 分钟 `High` 序列的**超额峰度**(日内分钟轴折叠成一个值) |
| `C` | `A + B`(NaN 传播,`fill_nan_with_zero` 默认 `False`) | 把「当天 Close 中位数」和「当天 High 峰度」两个数**逐股票、逐日直接相加** |
| `D` | 对每个交易日:在当天所有股票的 `C` 里,把最低 `10%`(`ceil(当天有效股票数×0.1)` 只)替换成当天 `C` 的均值,其余不变(推导见 `02_operators.md`) | 当天横截面上,把 `C` 值**最低的一成股票**的值拉到**当天均值**,其余股票的 `C` 原样保留 |
| `E` | `sign(D) · D²`(`signedpower` 的指数 `e` 未传,用默认值 2.0) | 对 `D` 做**带符号的平方**(方向保留,幅度被平方放大) |
| `F` | `E[t] / nansum(该股票过去 30 个交易日的 E,含当天)`(分母有 `EPS` 下限保护,见 `02_operators.md`) | 每只股票用**它自己过去 30 个交易日 `E` 的滚动和**去除当天的 `E`,得到一个比值 |

## 整条表达式一句话(机械描述)

逐股票、逐交易日:把「当天 1 分钟 `Close` 的中位数」与「当天 1 分钟 `High` 的超额峰度」相加,
在当天横截面上把结果最低的一成股票拉到当天均值,再把该值做带符号平方,
最后用该股票自己过去 30 个交易日(含当天)这个带符号平方量的滚动和去除当天值,得到最终因子值。
方向取 `-1`,半衰期(多头口径与多空口径均)为 `20`(两套网格搜索 `{0,1,2,3,5,10,20}` 的结果,见 `06_baseline.md`)。

## 与公布值的出入(事实,只记数字,原因候选见 06_baseline.md)

| 口径 | 指标 | Partura 复现 | 用户表公布 | 差 |
|---|---|---|---|---|
| utrain,多空口径 | 扣费多空夏普 `LS` | +2.59 | +2.58 | +0.01 |
| utrain,多头口径 | 多头腿毛超额 `Lgross` | +9.1% | +8.9% | +0.2pp |
| holdout | — | 未读 | ls=2.64 / long=0.125 | 无法对比(留出段只能读一次,尚未读) |

## 本文没有做的事(明确的缺口)

- 没有对中间节点 `A`~`E`做真实数据上的经验分布测量(均值/标准差/百分位数);`decompose` 只跑了内置合成探针,
  没有写 `studies/F112_scale_spow_masktop/probes.py`,所以没有任何针对这棵树真实数据的自定义探针被执行过。
  见 `03_decomposition.md` 末尾的详细说明。
