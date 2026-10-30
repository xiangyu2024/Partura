# 结构解剖:种子 802,P 组,第 1 轮

快照 `c07s802M1_I0_open_search`,1 个 head,98 个已评分候选,定位只花了 3 次付费评估。
以下所有算子语义都来自源码(`AlphaCube/src/alphacube/operators/`、`Partura/partura/ops_ext.py`),
关键代数等式我都在本地用 numpy 复算过(只验算子算术,没跑服务器、没碰 2023-08-08 之后的任何东西,也没打开其他种子的文件)。

---

## 0. 一句话结论(先看这个)

这一轮的共性表和核心卡**看起来有 13 行 / 6 个核心,实际上只有一个真来源加一个卫生代理**。
真来源是:

> `day_mean(in_delta(Volume, 30))` ≡ 〔最后 30 分钟成交股数之和 − 最前 30 分钟成交股数之和〕/ 211

也就是**日内成交量 U 型的两端不对称**(开盘端重还是收盘端重),sign = −1 → 做多「开盘端重」的票。
剩下的都是单调包装的重复、日频常数、或者 p ≥ 0.17 的噪声。

---

## 1. alpha 的来源

### 1.1 核心的代数真相:它不是「平均 30 分钟成交量变化」

`in_delta` 是**分钟轴**算子(`dt_in.py:301`):

```python
def in_delta(x, d):
    T, N = x.shape
    res = get_nan_tensor(x.shape, ...)
    if d < N:
        res[:, d:] = x[:, d:] - x[:, :-d]
    return res
```

`day_mean` 是分钟轴 **nanmean**(`dt_day.py:89` → `common._mean` = `x.nanmean(dim=-1)`)。
前 d 分钟是 NaN,被 nanmean 跳过,于是求和**精确望远镜式相消**:

```
day_mean(in_delta(V, d)) = (1/(N-d)) · Σ_{t=d}^{N-1} (V[t] − V[t−d])
                         = (1/(N-d)) · [ Σ_{t=N-d}^{N-1} V[t] − Σ_{t=0}^{d-1} V[t] ]
```

N = 241(09:30 集合竞价 + 240 根,见 `dt_in.py:313` 的 `in_half` 注释)。数值验证:

| d | 等式 | 校验 |
|---|---|---|
| 5 | (后 5 分钟和 − 前 5 分钟和)/236 | OK |
| 15 | (后 15 − 前 15)/226 | OK |
| 30 | (后 30 − 前 30)/211 | OK |
| 60 | (后 60 − 前 60)/181 | OK |

**中间 241 − 2d 分钟被精确抵消,一点都没用上。** 任何人(包括 GP 和 PI)把这个写法读成
「平均 30 分钟成交量变化」都是读错了;它是一个**两端块差**。这是本份文件最重要的一条,
后面所有外围设计都从它推出来:**凡是只重新加权开/收两个块的外围都是冗余,凡是动到中间那段的才是真新信息。**

`Volume` 是**每分钟成交股数**(不是累计):`parser.py:51` 的 `vol_1d = day_sum(Volume)`,`amt_1d = day_sum(Amt)`。

### 1.2 共性证据:13 行 ≈ 8 个东西,p<0.05 的只有一族

定位工具的 enrichment 表**不按「排名等价」去重**,所以同一个信号被数了好几遍。逐条拆:

| 行 | 子树 | 真实身份 |
|---|---|---|
| 1 | `day_mean(in_delta(Volume, 5))` | 真来源,d=5 |
| 2 | `day_mean(neg(neg(in_delta(Volume, 5))))` | **与第 1 行函数完全相同**(`neg∘neg` = 恒等,已验证) |
| 3 | `day_mean(neg(in_delta(Volume, 60)))` | = **−1 ×** `day_mean(in_delta(Volume, 60))`(`day_mean(neg(x)) = −day_mean(x)`,已验证);打分自己拟合方向(head 的 `sign` 就是 −1)→ 与 d=60 那个变体同一个信号,**已实测 score +0.519** |
| 4 | `day_last(Amt)` | 收盘那一分钟的成交金额 ≈ 流动性 / 规模水平 |
| 6 | `cs_robust_z(day_last(Amt))` | **与第 4 行排名完全相同**(见 1.4) |
| 5 | `cs_median(cs_robust_z(day_last(Amt)))` | **每天全市场同一个数**(见 1.4) |
| 13 | `cs_stddev_full(cs_robust_z(day_last(Amt)))` | 同上,日频常数 |
| 7 / 8 / 9 | `day_flat_run_max(Vwap)` / 它的 `ts_regbeta(…,50)` / 再套 `sigmoid` | 7 和 8 的 effect/p/n_with **一模一样**(0.8777 / 0.3554 / 6)→ 在档案里完全嵌套、不可分离;9 是 8 套单调 `sigmoid` |
| 10 / 11 | `sqrt(sigmoid(LimitWidth))` / `sigmoid(LimitWidth)` | effect/p/n **一模一样**(0.7234 / 0.456 / 7),因为 `sqrt∘sigmoid` 与 `sigmoid` 都单调 → 排名口径下同一个信号 |
| 12 | `day_durbin_watson(Volume)` | 分钟量路径的锯齿度 |

**p 值分界非常干净**:只有第 1–6 行 p < 0.05(0.0029 / 0.008 / 0.0028 / 0.0013 / 0.0136 / 0.0095),
第 7–13 行 p ∈ [0.166, 0.470],n_with 只有 4–10(全档 98 个)→ **整体按噪声处理**。
而 p<0.05 的六行里,1/2/3 是同一族真来源,4/6 是同一个代理,5 是日频常数。

档案的基线很低:`mean_without` 普遍 −1.0 ~ −1.2,head 是 +0.69 → **98 个候选绝大多数是废品**,
这让 n_with = 4 的 enrichment 很脆:「含某个子树」在这种档案里很容易只是「没算崩」的同义词。

### 1.3 充分性与必要性:**一条都没有,而且是工具结构上做不出来**

`loc.md` 的「必要性」一栏全是「—」,这**不是**测出来等于 0,是根本没生成测试。`scripts/c05_locate.py`:

- **sufficiency** 只对满足 `n.operands and n.shape.collapsed and n.shape.degenerate and is_valid_root(n)` 的子树生成。
  `day_mean(in_delta(Volume,30))` 唯一的内部子树是 `in_delta(Volume,30)`,它是**分钟形**(不是 collapsed/degenerate)→ 生成不出来。
- **knockout** 需要某个节点有一个**已经是日频(collapsed+degenerate)的孩子**。`day_mean` 的孩子是分钟形,
  `in_delta` 的孩子是 `Volume`(分钟形)→ 也生成不出来。

所以 `paid` 只有 3,三条全是 swap/window。**结论:核心卡上的 6 个核心,没有任何一个有「子树单独当因子」的分数**
(`core_cards` 里 6 个全是 `"source": "enrichment"`,没有 `own_score`)。PI 不要把核心卡当成已验证清单。

### 1.4 关键的「单调包装」陷阱(规则 §1:任何单调变换是同一个信号)

奖励第一步就是**每天截面转排名**,所以任何**日内严格单调**的最外层包装都是恒等变换:

- `cs_robust_z(x) = (x − median)/(1.4826·MAD + EPS)`(`ops_ext.py:500`):分母恒正 → **保序**(已数值验证)。
  **作为最外层 = 完全无效;作为内层**(和别的项做加减乘除时)才有意义 —— 它把两项放到同一个鲁棒尺度上。
  这一点对后面 E 的外围设计有用。
- `sigmoid`、`sqrt`(正值上)、`neg∘neg`:同理,最外层都是无效包装。`neg` 单层是变号,而打分自己拟合 `sign`。

**而 `cs_median` / `cs_stddev_full` 是行归约后 `expand_as` 广播回去**(`nd_cs.py:134-140`、`185-199`):

```python
med = _median(masked)
return med.unsqueeze(-1).expand_as(x)      # 每天 → 全部股票同一个数
```

→ `cs_median(cs_robust_z(day_last(Amt)))`(核心卡 #5)**截面上零信息**。
`distinct_fraction`(`partura/diagnose.py:136`,= 每天 distinct 值数 / 有值股票数的中位数)= 1/5220 ≈ 0.0002,
门槛是 ≥ 0.5(`c05_locate.py:163`)→ 单独评估必然是**门槛废品**。
它唯一的合法用法是在更大的树里当**市场级 regime 标量**(`cs_stddev_full(cs_robust_z(·))` 其实是
「收盘分钟金额截面的 σ/MAD 比」= 截面厚尾度,一个情绪标量)。

同样地:
- `day_flat_run_max(Vwap)`(`ops_ext.py:415`)返回「最长连续相等分钟数 / 有效分钟数」,取值是 k/241 这种整数格
  → distinct ≈ 241/5220 ≈ 0.046 → **单独也过不了门槛**。语义上它是**滞涨/停牌/涨跌停锁死**探测器。
- `sigmoid(LimitWidth)`:`LimitWidth` 只有 ~3–4 个取值(主板 10% / 创业板科创板 20% / ST 5%)→ distinct ≈ 0.001,
  整块并列靠列序打破。规则 §4 说「并列靠列序」不算数学问题(列序携带板块信息),但这里 `LimitWidth` **本身就是板块信息**,
  等于用板块信息给板块排序,循环;加上 p = 0.456 → 别碰。

### 1.5 敏感性:窗口很稳,字段**必须是股数**

| 变体 | score | train | valid | distinct | ρ_known |
|---|---|---|---|---|---|
| `day_mean(in_delta(Volume, 15))` | +0.506 | 0.506 | **1.338** | 0.883 | −0.410 |
| `day_mean(in_delta(Volume, 30))`(head) | **+0.692** | 0.692 | 0.981 | — | — |
| `day_mean(in_delta(Volume, 60))` | +0.519 | 0.594 | 0.519 | 0.947 | −0.433 |
| `day_mean(in_delta(Amt, 30))` | **−0.806** | 0.113 | −0.806 | 1.000 | **−0.518** |

**窗口**:三点都 ≥ 0.5,平台很宽 → 结构稳。但方向很有信息:
**valid 腿随 d 单调下降(1.338 → 0.981 → 0.519),train 腿在 30 处最高**。
短窗在 valid 上明显更强 → **信号更靠两端(集合竞价附近),不是整段连续竞价**。
d=15 和 d=30 的 score 都被 **train 腿**卡住,d=60 被 **valid 腿**卡住。

**字段**:`Volume → Amt` 掉 1.50,而且 ρ_known 从 −0.41/−0.43 跳到 **−0.5177,已越过 0.5 不合格线**。
机制很清楚 —— 5 个控制(`scripts/c05_controls.py:52`)是:

| | 表达式 |
|---|---|
| liq | `cross_mean(day_sum(Amt), 30)` |
| vol | `cross_mean(day_std(Ret), 20)` |
| rev | `div(day_last(Close), ts_delay(day_last(Close), 20))` |
| known | `cross_mean(day_std(Amt), 30)` |
| size | `LogFloatCap` |

三个是 Amt / 市值口径。**换成成交金额就是把因子推到控制那一侧。这个 alpha 必须用股数。**
注意 `SWAP` 字典(`c05_locate.py:59`)对 `Volume` **只有 `Amt` 一个同类字段** → 定位工具的字段敏感性在这个 head 上**已经用尽**,想再测字段必须手写。

### 1.6 规则 §4 三类陷阱逐条过

- **前视:无。** `in_delta` 只用当日 ≤ t 的分钟,日频值在 15:00 已知;标签是 `label_kind="open_vwap15"`
  (`c05_controls.py:50`)= **次日开盘 15 分钟 VWAP 成交**,信号与执行隔了一夜。
- **数值伪影:无。** head 里没有除法、没有近零分母;`Volume` 非负;coverage 0.9993,distinct 0.883–1.000。
- **定义坏掉:有一处,但在 head 之外 ——**
  `in_delta` 的 `if d < N`,**d = 241 时条件不成立 → 整行保持 NaN → coverage 0,门槛废品**(已验证)。
  而 dt 窗口网格是 `(3, 5, 10, 15, 30, 60, 241)`(`catalog.py:34`),**241 这一格是坏的**,别浪费 R。
  另外:若有分钟是 NaN(未成交),`in_delta` 在端点缺失处是 NaN,**精确望远镜等式只对「分钟网格完整」的名字成立**,
  薄票上只是近似(我用 25% 随机 NaN 验过:望远镜式 52.49 vs 实际 29.44)。coverage 0.9993 说明日频值几乎处处可算,
  所以这不是覆盖率问题,只是解释上要留一句。

### 1.7 一个真实的结构性污染(不是数学问题,是经济口径问题)

核心是**原始股数差**,**没有除以当日成交量**。所以它的量级随个股成交水平放大
→ **高成交名字占据分布两尾,低成交名字堆在 0 附近的中间**。
奖励对流动性的残差化是「排名及其平方、三次方」的线性去除,去不掉这种**「尾部被流动性筛选」**。
这既解释了为什么 ρ_known 已经到 −0.41/−0.43(离 0.5 线只剩三分之一),也是本轮最该下手的地方。

还有一点:head 胜在**半衰期 20**,而五个控制全是 20/30 日均值类的**慢速水平量**。
EMA-20 把一个本来是「当日日内时点」的量变慢了,这本身就抬高了它与慢速控制的相关。
→ **把「水平」变成「相对自身近期水平的偏离」应当在保留时点信息的同时压低 ρ。**

### 1.8 真来源 vs 代理:判定

**真来源(一个)**:`day_mean(in_delta(Volume, d))` 一族 = 日内成交量两端不对称。
机制清楚、三个窗口都 ≥ 0.5、无前视无伪影、与 5 个控制都在线内、
而且 rev 控制是**收益**反转、不是**成交时点**,所以这是控制抓不到的一个独立维度。

**只是代理(全部)**:
- `day_last(Amt)` / `cs_robust_z(day_last(Amt))` —— **卫生代理**。98 个候选里出现 22 次(最常见的叶子),
  `mean_without` = −1.20 低于全档均值 ≈ −1.0 → 它的 enrichment 更像「引用了一个覆盖率高、不会算崩的金额叶子的候选,
  比其余算崩的候选分高」。而且它正好是 liq / known / size 的口径。不是 alpha。
- `cs_median(…)` / `cs_stddev_full(…)` —— 日频常数,截面零信息。
- `day_flat_run_max(Vwap)` / `ts_regbeta(…)` / `sigmoid(LimitWidth)` / `day_durbin_watson(Volume)` —— p ≥ 0.166,噪声级;
  前两个在档案里还完全混淆,后两个单独过不了 distinct 门槛。

---

## 2. 烂部件(R 的料)

**必要性 ≤ 0 的部件:一个都没测出来**,原因见 1.3(工具结构上生成不出 knockout)。
所以本轮 R 不能走「去掉算子」的路,只能走**「换部件」和「拿掉一侧」**。

### 已确认的烂部件

1. **叶子 `Volume → Amt`:已证伪。** score −0.806(掉 1.50),ρ_known −0.5178 越线。
   而且 `SWAP` 对 Volume 只有 Amt 一个选项 → 工具的字段维度到此为止。
2. **窗口 241:定义坏掉**(全 NaN,见 1.6)。网格里这一格别用。
3. **`day_mean` 换 `day_sum`:单调等价,同一个信号。** 分母 (241−d) 是常数 → `day_sum ≡ day_mean × 常数`。
   **别浪费 R 格子。**(换成 `day_median` / `day_std` 就不等价了 —— 那会破坏望远镜,是新 idea,归 N。)
4. **任何最外层单调包装**(`neg∘neg`、`cs_robust_z`、`sigmoid`、`sqrt`):零收益,见 1.4。

### 一个必须告诉 PI 的恒等式(已数值验证)

任何**日频**(按日为常数)归一量 X 都可以**精确**提到外面:

```
day_mean(in_delta(div(Volume, X), d))  ≡  div(day_mean(in_delta(Volume, d)), X)
```

(d = 5/30/60 都验过,rtol 1e-12。原因:X 在分钟轴上是常数,`in_delta` 是线性的。)

两种写法的**算子骨架不同**(抽掉字段/常数/窗口也不一样)→ **库禁令的骨架去重抓不到**,
但它们是**完全相同的面板**。**PI 千万别两种都跑。** 建议把它放在 **R**(叶子替换,便宜、立刻有答案),
把 96 次评估的 E 位省下来做真正长在核心外面、**提不出去**的东西(截面算子、二元组合)。

### 不建议进 R 的

任何含 Amt 的变体(ρ_known 已证越线);`day_sum` 替 `day_mean`;窗口 241;
任何再加一层 `cross_mean` / EMA 的平滑 —— head 已经在半衰期 20 上胜出,奖励本身就在做 0/5/20 的 EMA,再平滑高度重复。

---

## 3. 之前的任务

**本轮是第 1 轮,之前什么都没有。** 具体核对:

- `loc.json` 的 `missions_before` = `[]`,`r_candidates` = `[]`,`replacements_in_force` = 0;
  `loc.md` 的「本组之前各轮的任务」写明「(第 1 轮,还没有)」,「比原 head 好的拆解变体」写明「(没有)」。
- 种子目录下**只有** `r1/loc.md` 和 `r1/loc.json`。没有 `notebook.md`、没有 `missions_final.yaml`、
  没有 `audit_record.json`、没有 `R_prev.json`、没有 `lit.md`。
- **E**:还没有过,没有 heads 产出。
- **N**:还没有过。提醒 PI 规则 §2:**3 轮里至少要有 1 个 N 位通过审计**,现在 1/3,还有余量但不宜一直推后;
  N 位的审计风险(创新度)比 E 低,早做早安全。
- **R**:还没有过。定位工具也**没给出任何 R 候选** —— 三个拆解变体没有一个达到 `head + 0.1`(门槛是 0.792)。
- **审计员**:还没挡过任何东西,没有已知的被挡理由可以借鉴。
- **上一轮笔记的预测**:没有上一轮。

### 库很空带来的机会和风险

库里**只有 1 个 head**(`day_mean(in_delta(Volume, 30))`),所以本轮库禁令几乎不构成约束 ——
这是整个实验里**最容易收录新 head 的时候**,应该优先去拿「与原 head ρ < 0.5」的新东西。

反过来是风险:**唯一的 head 和我们最想深挖的核心是同一族**,
所以 E 的产出很容易因为与它日度秩 ρ ≥ 0.7 被 GP 当场拒掉。
→ **E 的外围必须做「改变信号性质」的事(归一化、去自身慢速水平、按板块中性化、与另一项组合),
不能只做「微调同一个量」。** 这是本轮 E 位成败的关键。

---

## 4. 本轮候选

### 4.1 核心(建议只开 1 个 E 位在核心 A 上)

#### 核心 A(首选):`day_mean(in_delta(Volume, 30))` —— 直接用 head 本体当核心

规则 §2 允许整个 head 当核心。选 30 而不选核心卡 #1 的 5,理由:
**30 是唯一有实测 score(+0.692)的点**;d=5 只有 n_with=4 的 enrichment,并且有 4.3 里两条具体风险。

**它周围已经见过的外围写法**(诚实说明:我只能看到共性表里的**子树**,看不到 98 个候选的完整表达式,
所以下面是从共性表反推的):
- 直接套在核心上的:`neg(·)`、`neg(neg(·))` —— 变号 / 恒等,**等于什么都没加**。
- 与它共现的材料(GP 到目前为止的外围词汇):`day_last(Amt)`、`cs_robust_z`、`cs_median`、`cs_stddev_full`、
  `day_flat_run_max(Vwap)`、`day_durbin_watson(Volume)`、`ts_regbeta(·, ·, 50)`、`sigmoid(LimitWidth)`、`sqrt`。
  → 也就是**「截面标准化 + 流动性/涨跌停旗标」**。
- **没有任何人试过除以当日成交量,也没有人试过减去自身近期水平,也没有人按板块中性化。这个 E 空间基本是处女地。**

**建议的 E 外围方向**(都要求候选原样含核心;重点是**提不出去**的操作):

| | 写法 | 为什么 |
|---|---|---|
| (a) 去自身慢速水平 | `sub(C, cross_mean(C, 20))`、`div(C, cross_stddev(C, 20))`、`ts_delta(C, 5)` | 把「水平」变成「变化」,直接压低与 liq/known/size 这些 20/30 日均值类控制的相关(见 1.7) |
| (b) 截面/板块中性化 | `cs_bucket_demean(C, BoardCode)`、`cs_bucket_zscore(C, BoardCode)` | 截面算子,**提不出去**;把 1.7 的「尾部被流动性筛选」按板块拆开 |
| (c) 条件化 / 交互 | `mul(C, sign(ts_delta(day_last(Close), 1)))`、`mul(C, cs_robust_z(<另一项>))` | 昨日涨跌决定「开盘端重」的含义(追涨 vs 恐慌);`cs_robust_z` 在**内层**才有用(见 1.4) |
| (d) 跨日回归分解 | `ts_regbeta(C, day_sum(Volume), 20)`、`ts_regres(C, day_sum(Volume), 20)` | 「自身成交水平解释不了的那部分倾斜」—— 对症 1.7,而且与原 head 的 ρ 有机会掉到 0.5 以下 → 可能**收录**而不是替换 |

(C = `day_mean(in_delta(Volume, 30))`。nd 窗口网格是 `(1, 5, 10, 20, 30, 40, 50)`,`catalog.py:35`。)

**审计风险预判**:(a)(b)(d) 在做实质不同的事,创新度应当 ≥ 3;
**但凡「除以一个日频标量」的写法创新度会被怀疑成「只是换了写法」,而且和 R 重复 —— 别放进 E。**
E 位还要求核心与每个控制 |ρ| < 0.8:核心 A 的三个窗口变体 ρ_known 只有 0.41–0.43,应当安全。

#### 核心 B(备选,**只在 R 的短端结果支持时才开**):`day_mean(in_delta(Volume, 5))`(核心卡 #1)

外围见过的同上(只有 `neg` / `neg∘neg`),n_with 仅 4。
注意规则 §2「每个核心整个实验至多 2 个 E 位」,而 **A 和 B 抽掉窗口后骨架相同**,
库禁令按骨架去重 → 两者产出会互相挤。**本轮 A、B 只开一个。**

#### 明确建议从核心卡里划掉的

| 核心卡 | 为什么划掉 |
|---|---|
| #2 `day_mean(neg(neg(in_delta(Volume, 5))))` | 与 #1 **函数完全相同**(已验证),但多两个节点、骨架不同 → **库禁令的骨架去重抓不到它**,会把 96 次评估白花在和 #1 一样的空间里。**请 PI 直接删掉。** |
| #5 `cs_median(cs_robust_z(day_last(Amt)))` | 每天全市场同一个数,截面零信息,distinct ≈ 0.0002 远低于 0.5 门槛。当 E 核心等于把格子浪费在一个日频标量上。 |
| #4 `day_last(Amt)` / #6 `cs_robust_z(day_last(Amt))` | 两者排名完全相同(同一个东西);是卫生代理,且正好是 liq/known/size 的口径。E 位开在这里大概率一轮白费,还有撞 §3「核心与控制 abs(ρ) < 0.8」的风险 —— 审计员拿确定性相关度表会直接看到。 |
| #3 `day_mean(neg(in_delta(Volume, 60)))` | 与 d=60 变体同一个信号(只差符号,打分自己拟合方向),**已实测 +0.519**,比 head 低。如果要做长窗,用 d=60 的写法,别用带 `neg` 的。 |

**核心卡的机械顺序(「B0 按这个顺序取」)前三名里两个是重复、第五个是日频常数 → PI 必须覆盖这个顺序。**

### 4.2 R 目标(上限 16,建议用 8)

| # | 变体 | 测什么 |
|---|---|---|
| 1 | `day_mean(in_delta(Volume, 3))` | 窗口短端 |
| 2 | `day_mean(in_delta(Volume, 5))` | **核心卡 #1 的前提** |
| 3 | `day_mean(in_delta(Volume, 10))` | 窗口短端 |
| 4 | `day_mean(in_delta(div(Volume, day_sum(Volume)), 30))` | 尺度无关化(治 1.7) |
| 5 | `day_mean(in_delta(div(Volume, cross_mean(day_sum(Volume), 20)), 30))` | 按自身近期水平归一,保留当日量的 surprise |
| 6 | `div(day_first(Volume), day_sum(Volume))` | **开盘侧单独** = 开盘集合竞价占日成交比重 |
| 7 | `div(day_last(Volume), day_sum(Volume))` | **收盘侧单独** = 收盘集合竞价占比 |
| 8 | `sub(day_mean(in_delta(Volume, 30)), cross_mean(day_mean(in_delta(Volume, 30)), 20))` | 去自身慢速水平 |

说明与预期:
- **1–3 是本轮 R 的第一优先。** valid 随 d 下降的趋势 + 核心卡 #1 就是 d=5
  → **在花 96 次评估的 E 位之前,先用 3 个便宜的 R 格子把「短端更好」证实或证伪。**
- **6、7 严格符合 R 的「去掉部件」定义** —— 核心本来是一个差,先问 alpha 在哪一侧。
  `day_first` / `day_last` 取第一个 / 最后一个**有效**分钟(`dt_day.py:129/134`),正是两个集合竞价格。
  这两个与原 head 的 ρ 有机会 < 0.5 → **最可能把库从 1 个 head 扩到 2–3 个的路**(走**收录**而非替换)。
- 4、5、8 与原 head 共用同一个分子,ρ 大概率 ≥ 0.5 → 若 ≥ head + 0.1(即 ≥ 0.792)走**替换**。
- 4 和「E 的外围除法」是**同一个面板**(见第 2 节恒等式),**只跑 R 这一份。**

**不要放进 R**:任何 Amt 版本;`day_sum` 替 `day_mean`;窗口 241;任何最外层单调包装。

### 4.3 两条必须写进任务说明的短端风险

- **distinct / 并列块**:d=15 的 distinct 已经掉到 0.883,机制是「前 d 分钟与后 d 分钟都没成交 → 差恰好为 0」的并列块。
  d 越小这个 0 块越大 → **d=3 有可能逼近 0.5 的门槛**。R 的结果里要看 `distinct` 这一列,不只看 score。
- **训练窗口内部的制度断点**:A 股收盘集合竞价 2018-08-20 才上线,train 从 2018-01-02 开始
  → 最后一分钟在 train 前约 7.5 个月**不是**集合竞价。d 越小这一格占比越大(d=3 时占三分之一)
  → 这会**专门压短端的 train 腿**,而三个已测窗口的 score 恰好都是被 train 腿或 valid 腿卡住的。
  这不是规则 §4 的「定义坏掉」(不该据此挡),但是解释 d=3/5 结果时必须考虑的结构性非平稳。

### 4.4 N 的灵感(都要与核心 A 骨架不同,避开库禁令)

- **N1 日内成交量的「重心」,而不是「两端差」。** 核心精确丢掉了中间 241 − 2d 分钟(第 1.1 节),
  这是最明显的空白。`day_argmax(Volume)` 直接给出当日最大成交分钟的列序号(`dt_day.py:169`,0-based)= **峰量时点**。
  **注意它只有 ~241 个取值,distinct ≈ 0.046,单独过不了门槛**,必须配连续量,
  或者改用 `day_mean(in_argmax(Volume, 30))`(`dt_in.py:393`,`pct=True`,滚动窗口内峰值位置的百分位 → 取值连续得多)。
- **N2 带方向的量的时点。** 把「总量」换成「净流向」再问时点:`day_mean(in_delta(mul(Volume, sign(Ret)), 30))`
  → 两端的**净买卖压力**不对称,而不是总成交量不对称。叶子变了,骨架不同。
- **N3 日内量的集中度(而不是时点)。** `div(day_max(Volume), day_sum(Volume))`、
  `day_std(in_delta(Volume, 30))`(**破坏望远镜**,变成「30 分钟量变化的波动」);
  `day_durbin_watson(Volume)` 那条噪声线索在这里才有正确的用法(锯齿度 = 量的时间结构的另一个切面)。
- **N4 上午 / 下午口径。** d=120 恰好等于「下午(cols 121..240)− 上午(cols 0..119)」(已验证),
  但 **120 不在 dt 窗口网格 (3,5,10,15,30,60,241) 里**。要做半天口径得绕开窗口:
  `sub(day_sum(in_slice(Volume, 121, 240)), day_sum(in_slice(Volume, 0, 119)))`
  (`in_slice(x, start, end)` = `x[:, start:end+1]`,`dt_in.py:324`;`in_half` 的布尔参数能否在表达式里写,请让检查角色先确认一下解析)。
  骨架与核心不同,算新 idea。

---

## 5. 文献题目(给文献员,4 个)

**Q1 —— 对准核心 A(日内成交量两端不对称)**
文献里对「当日成交量在开盘端 vs 收盘端的不对称」这种结构做过哪些处理?具体想知道:
用成交股数还是成交金额、要不要除以当日总成交量、开盘/收盘集合竞价是否单独拿出来处理、
以及这个特征与短期反转、与流动性因子的关系是正交还是重叠。
- EN: `intraday volume U-shape`, `opening versus closing volume share cross-section stock returns`,
  `share of daily volume traded in the last 30 minutes return predictability`, `closing auction volume share`,
  `volume timing`, `order flow concentration at open and close`
- CN: `日内成交量 U 型`, `开盘 收盘 成交量占比 选股`, `收盘集合竞价 成交占比 收益预测`,
  `日内成交时点`, `成交量分布 倾斜 横截面收益`

**Q2 —— 对准第 1.7 / 第 2 节的「尺度无关化」设计点**
把一个「原始股数差」型的成交量因子除以当日成交量(或近期平均成交量)之后,
它与流动性/规模因子的相关性、以及它的表现通常怎么变?文献里对「用水平量 vs 用占比/换手率口径」有定论吗?
异常成交量(abnormal volume)的标准定义是哪几种?
- EN: `share volume versus dollar volume factor construction`, `normalizing volume signals by turnover`,
  `abnormal volume definition volume over average volume`, `liquidity contamination of volume factors`,
  `size and liquidity neutralization of volume based signals`
- CN: `成交量因子 归一化 换手率`, `异常成交量 定义`, `成交额 与 成交股数 口径`,
  `成交量因子 流动性污染`, `规模 流动性 中性化`

**Q3 —— 对准 N1 / N2(时点与方向)**
文献里怎么度量「当日成交量的时间重心 / 峰值时点」和「带方向的日内净流向时点」?
这类特征对次日收益有预测力吗?中国 A 股有没有专门的结果(尤其是尾盘资金流、开盘追涨)?
- EN: `volume weighted average time of day`, `intraday timing of peak volume`,
  `intraday order imbalance by time of day`, `late day order imbalance return predictability`,
  `smart money dumb money open versus close indicator`, `Chinese A-share retail intraday trading patterns`
- CN: `成交量 时间重心`, `日内 峰量 时点`, `分时 净主动买卖`, `尾盘 资金流 预测`,
  `聪明钱指标 开盘 尾盘`, `A 股 散户 日内交易 模式`

**Q4 —— 对准 4.3 的两条短端风险(A 股制度细节)**
A 股收盘集合竞价(2018-08-20 起)与开盘集合竞价的成交占比有哪些实证结果?
这类制度上线造成的样本内结构断点,实证上一般怎么处理?
另外涨跌停板宽度(主板 10% / 创业板科创板 20% / ST 5%)作为分组变量,在因子研究里的常规处理是什么?
- EN: `China closing call auction 2018 introduction effects`, `closing auction volume share A-shares`,
  `call auction microstructure China`, `structural break market design change factor study`,
  `price limit width ChiNext STAR board 20 percent grouping`
- CN: `收盘集合竞价 2018 上线 影响`, `A 股 集合竞价 成交占比`, `制度变更 结构断点 处理`,
  `涨跌幅限制 创业板 科创板 分组`, `ST 股 5% 涨跌幅 因子研究`

---

## 6. 给下一轮留的预测(供第 2 轮核对)

1. **R 的 d=3/5/10**:d=5 和 d=10 的 score ≥ 0.5(落在已见平台内);d=5 的 valid 腿超过 d=15 的 1.338 的可能性中等,
   但 **d=5 / d=3 的 train 腿会低于 d=30 的 0.692**(集合竞价制度断点 + 并列块)→ 最终 score 不一定超过 head。
   d=3 的 `distinct` 明显低于 0.883,有小概率跌破 0.5 直接废品。
2. **R 的第 4、5 项(除以成交量)**:abs(ρ_known) 会从 0.43 明显**往 0 的方向走**;score 有过 head + 0.1 的实质机会。
   这是我认为本轮最可能产生**替换**的一项。
3. **R 的第 6、7 项(单侧)**:两者与原 head 的 ρ 不同 —— **收盘侧**(第 7 项)与原 head 的 ρ 更高(核心的 sign = −1,
   做多开盘端重 = 做空收盘端重);**开盘侧**(第 6 项)更有机会 ρ < 0.5 走**收录**。
   两者至少有一个 score ≥ 0.5。
4. **E(核心 A)**:产出 heads 的最大障碍不是分数,是**与原 head 日度秩 ρ ≥ 0.7 被 GP 拒掉**。
   (a) 类(去自身慢速水平)和 (d) 类(跨日回归残差)最可能突破 0.7 这道墙;
   纯粹的单调包装 / 再平滑类种子会被大量拒绝。
5. **审计**:最可能被挡的是「除以一个日频标量」类的 E 种子(创新度 1,与 R 重复),
   以及任何以 `cs_median(…)` / `sigmoid(LimitWidth)` / `day_flat_run_max(Vwap)` 为主体的东西(面板几乎是常数)。
   核心 A 本身与 5 个控制的 abs(ρ) 应当全部 < 0.8,E 位的核心门槛不会卡住。
