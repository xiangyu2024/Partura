**来历**:手写库 `all_tide_mean_30`(批次 B01_single_factors)。表达式见 `configs/F115_all_tide_mean_30.yaml`
(与工单里给出的一致,已通过 `S0_baseline` 在服务器上求值)。库名里的 `_30` 与表达式里实际的
`cross_mean` 窗口参数 **20** 不一致——只记录这个不一致,命名规则/来源未知,不做解释。

**逐层拆开**(变量名与 `./scripts/study.sh decompose` 给出的 SSA 分解表一致;每个算子的精确语义、
NaN/边界行为见 `02_operators.md`;量纲/取值范围/重复子树见 `03_decomposition.md`):

```
A = in_slice(Close, 31, 211)            # 当天 Close 的 181 分钟切片(第 31~211 根,241 格里掐掉首 31、尾 29 根)
B = in_slice(Volume, 31, 211)           # 同一切片窗口里的 Volume
C = in_local_mean(B, 5)                 # B 的 9 分钟居中滑动平均(非因果,半径 4)——"潮汐"曲线
D = day_argmax(C)                       # C 在切片内的最大值所在分钟(局部坐标 0..180)——"潮顶"
E = in_slice_to_end(C, D)               # C 里下标 ≥ D 的后半段(含 D 这一列),其余 NaN
H = in_slice_from_start(C, D)           # C 里下标 ≤ D 的前半段(含 D 这一列),其余 NaN
F = day_argmin(E)                       # 后半段的最小值所在分钟——"潮后低谷"(恒有 F ≥ D)
I = day_argmin(H)                       # 前半段的最小值所在分钟——"潮前低谷"(恒有 I ≤ D)
G = day_locate(A, F)                    # 用 F 这个分钟位置去取 A(Close 切片)里的值
J = day_locate(A, I)                    # 用 I 这个分钟位置去取 A(Close 切片)里的值
K = sub(G, J)                           # 潮后低谷的 Close − 潮前低谷的 Close
L = div(K, J)                           # 上面那个差 ÷ 潮前低谷的 Close → 一个无量纲的涨跌幅
M = sub(F, I)                           # 潮后低谷与潮前低谷之间隔了多少分钟(恒 ≥ 0)
N = div(L, M)                           # 涨跌幅 ÷ 分钟数 → "潮前谷到潮后谷,每分钟的价格变化率"
O = cross_mean(N, 20)                   # N 的 20 个交易日因果滚动均值 —— 因子最终输出
```

**一句话**:每天,在当日(剔除开盘/收盘集合竞价两端后的)成交量 9 分钟平滑曲线上找到峰值分钟,
在峰值前、后两段里各找一个量能最低的分钟("潮前谷""潮后谷"),量这两个分钟之间 Close 的涨跌幅、
再除以两者相隔的分钟数,得到一个"每分钟价格变化率";因子值是这个日频量的 20 个交易日滚动均值。

**S0_baseline 已复现用户表公布的这一行**(数字见 `06_baseline.md` 第 1 节):用户口径
(utrain,方向/半衰期在 utrain 上定)多空夏普 **+2.29**,与 `configs/F115_all_tide_mean_30.yaml` 里
`published.ls[0] = 2.29` 完全一致;多头腿毛超额 **+7.9%**,与 `published.long[0] = 0.08` 基本一致
(四舍五入前 7.9% vs 8.0%);方向 −、半衰期 2,与 `published.sign = -1`、`published.hl = 2` 一致。
留出段(`published.ls[1]=1.65`、`published.long[1]=0.084`)按规矩未读。
