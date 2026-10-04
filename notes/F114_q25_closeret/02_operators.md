两个算子的真实语义,来自服务器内核源码(`./scripts/study.sh src day_close cross_quantile_q25`,AlphaCube commit `1698296`)
与 `decompose` 的探针实测值。源码原文附在每节末尾。

---

## `day_close`

**声明**:face `dt` / family `day` / category `unary`,arity 1,计算轴 `M`(日内分钟轴),无窗口参数,`reduces_m=True`(把分钟轴折成 1 个值),`lookahead=False`。

**精确公式**:`day_close(x) = day_last(x)`,逐字节是:

```
day_last(x)      = last_valid_last(x)
last_valid_last(w) 在 w 的最后一维(当天的分钟维)上:
    valid = ~isnan(w)
    last_idx = max{ j : valid[j] }                 # 最后一个非 NaN 的位置;如果没有,记 -1
    若 last_idx >= 0: 返回 w[last_idx]
    否则(整天没有一个非 NaN): 返回 NaN
```

**沿哪条轴 / 窗口与回看**:只在**当天内部**的分钟维上找"最后一个有效值",不跨日、没有交易日窗口参数,也不依赖任何跨日状态。

**齐次度**:实测 `k = 1.0`(直取值,不做任何缩放或非线性变换,`f(c·x) = c·f(x)` 对任意 `c` 成立,包括 `c<0` —— 探针"取负后 = odd"与此一致)。

**NaN / 边界 / 不足窗口**:
- 10% 随机缺失下,输出仍 100% 是有限值(探针 `finite_frac_with_10pct_missing = 1.0`)——因为只需要当天**任意一个**非 NaN 分钟,门槛极低。
- 整天所有分钟都是 NaN → 输出 NaN(探针 `all_nan_input_gives_all_nan = True`)。
- 没有"不足窗口"的概念(本身无窗口)。

**输出**:连续值,不是布尔或档位。

**有没有用到当天之后的数据**:没有。`lookahead=False`;且定义本身只在当天分钟维内部取值,结构上不可能看到其他交易日。

**和名字不一样的地方**:**`day_close` 这个名字字面是"收盘价",但内核定义只是 `day_last` 的别名 —— 对任意喂进来的分钟序列取"当天最后一个非 NaN 值"。**
喂 `Close` 时它确实等于收盘价;但这里喂的是 `Ret`(逐分钟收益字段,见 `01_expression.md` 的证据链)。于是 `day_close(Ret)` 取到的是
**当天最后一个有效分钟自己的那一笔分钟收益**——不是收盘价,也不是"开盘到收盘"的当日总收益,经济含义更接近"尾盘最后一笔报价附近的瞬时涨跌",
是一个单分钟的微观结构量。**未在本次建档里直接验证的事**:`Ret` 的精确定义(简单收益还是对数收益、以哪个价格为基准、"最后一个有效分钟"
具体对应几点)不在本地文档或这两个内核的源码注释里,只能从旁证推断(见 `01_expression.md`),没有另写探针去确认 —— 留作开放问题。

<details><summary>源码原文</summary>

```python
# /root/autodl-tmp/AlphaCube/src/alphacube/operators/dt_day.py:144
@op("dt", "day", arity=1)
def day_close(x: torch.Tensor) -> torch.Tensor:
    """Alias for `day_last` (last non-NaN value of the day)."""
    return day_last(x)

@op("dt", "day", arity=1)
def day_last(x: torch.Tensor) -> torch.Tensor:
    return last_valid_last(x).unsqueeze(-1)

def last_valid_last(w: torch.Tensor) -> torch.Tensor:
    d = w.shape[-1]
    idx = torch.arange(d, device=w.device).expand_as(w)
    valid = ~torch.isnan(w)
    idx_when_valid = torch.where(valid, idx, torch.full_like(idx, -1))
    last_idx = idx_when_valid.max(dim=-1, keepdim=True).values
    has_valid = last_idx >= 0
    last_idx_safe = torch.where(has_valid, last_idx, torch.zeros_like(last_idx))
    val = torch.gather(w, -1, last_idx_safe)
    return torch.where(has_valid, val, torch.full_like(val, float("nan"))).squeeze(-1)
```

</details>

---

## `cross_quantile_q25`

**声明**:face `dt` / family `cross` / category `rolling`,arity 1,计算轴 `D`(交易日轴,按股票独立滚动),窗口在表达式里固定为 `15`
(算子注册表里这一族的合法窗口网格是 `[3, 5, 10, 15, 30, 60, 241]` —— `./scripts/study.sh ops '^cross_quantile'`),`lookahead=False`。

**精确公式**:`cross_quantile_q25` 不是独立 kernel,是 `cross_quantile` 这个通用内核柯里化 `q=0.25` 得到的(`cross_quantile_q50`/`q75`
是同一个内核另外两个柯里化,catalog.py:157)。内核:

```
cross_quantile(x, q, d):
    w = rolling_windows(x, d, axis=0)
    return nanquantile(w, q, dim=-1)

rolling_windows(x, d, axis=0):                      # 因果滚动窗口,左边补 NaN
    pad = NaN,形状 = x 形状但 axis 维长度改成 d-1
    x_padded = concat([pad, x], axis=0)
    返回 x_padded 在 axis 上展开出的、每个位置一个长度-d 窗口(unfold)
```

即在交易日位置 `t`(逐股票独立),窗口取的是该股票自己历史上的 `A[t-14 .. t]`(含当天,共 15 个交易日,因果),再对窗口内**非 NaN**的值取 0.25 分位数。

**沿哪条轴 / 窗口与回看**:交易日轴 `D`,逐股票独立滚动(不跨股票混);窗口 15 个交易日,含当天;**没有跨这 15 天之外的回看**。

**齐次度**:实测 `k = 1.0`(分位数对正标量尺度等变,`f(c·x) = c·f(x)`,`c` 为正标量时成立,与 `torch.nanquantile` 的线性等变性质一致)。

**取负后 / 窗口变长**(实测均为 `neither`,**不要**当成奇函数或单调量来用):
- 取负:整体取负后的 0.25 分位数,等于原序列**0.75 分位数**取负,不等于 `-cross_quantile_q25(x)`——这个算子不是关于 0 对称的。
- 窗口变长:`q25` 不是极值型统计量(不像 `max`/`min` 对窗口变长单调),窗口变长时输出可能上也可能下,探针读数就是"neither"(不单调)。

**NaN / 边界 / 不足窗口**:
- `nanquantile` 在窗口内部忽略 NaN:只要 15 个位置里还有 ≥1 个非 NaN,就返回"基于那部分非 NaN 值"的 0.25 分位数,**不是 NaN**。
- **序列(每只股票自己的历史)刚开始的前 14 个交易日**(含新股上市后的头 14 个交易日)处于"攒样本"的热身状态:第 1 天窗口只有当天 1 个真实值,
  0.25 分位数 = 这个值本身(单点集合的任何分位数都等于该点);样本数逐天从 1 加到 15,第 15 天才第一次是"真正的 15 天分位数"。
  这**不是**整段输出 NaN,也**不是**等窗口攒满才开始输出 —— 是逐天变样本量的渐进过程。
- 若窗口 15 天**全部**是 NaN(比如连续停牌/缺数据超过 15 天),输出 NaN(探针 `all_nan_input_gives_all_nan = True`)。
- 探针实测:给输入加 10% 随机缺失后,99.61% 的输出仍是有限值(`finite_frac_with_10pct_missing = 0.9961`,`day_close` 自己是 1.0 —— 两者缺失的
  是不同的轴,不能直接相加)。这次建档没有另外拆开这 0.39% 具体来自哪些格子,只报告探针读数。
- 探针 `effective_memory`(decompose 的说明:"脉冲输入之后,输出还在多少天里记得它")读数是 **0 天**。只报告这个读数,没有另写探针去确认
  "为什么是 0"(`q25` 是下四分位数,通常的解释方向是"单日的孤立正向异常值落在窗口的上端,不影响下四分位数的位置",但这次没有验证,留作开放问题)。

**输出**:连续值,不是布尔或档位。

**有没有用到当天之后的数据**:没有。探针"日轴因果性 = True",`lookahead=False`;且 `rolling_windows` 的左补 NaN 写法本身就决定了位置 `t`
的窗口只能是 `[t-14, t]`,结构上看不到 `t` 之后的行。

**和名字不一样的地方**:名字(`cross_quantile_q25` = 25% 分位数、滚动窗口 15)与内核实现一致,**没有发现名字和实现不符的情况**。唯一需要说明的是
实现层面它不是一个独立 kernel,是 `cross_quantile` 这个通用内核的柯里化别名。

<details><summary>源码原文</summary>

```python
# /root/autodl-tmp/AlphaCube/src/alphacube/catalog.py:157
("cross_quantile_q25", "cross_quantile", lambda f: (lambda x, d: f(x, 0.25, d))),

@op("dt", "cross", arity=1, requires_window=True)
def cross_quantile(x: torch.Tensor, q: float, d: int) -> torch.Tensor:
    w = rolling_windows(x, int(d), axis=0)
    return torch.nanquantile(w, q, dim=-1)

def rolling_windows(x: torch.Tensor, d: int, axis: int = 0) -> torch.Tensor:
    """Causal rolling windows of length `d` along `axis`, left-padded with
    NaN so every original position (including the first `d-1`) gets a
    window. Output shape = `x.shape` with a new trailing window-dim of
    size `d` appended (the `axis` dim's length is unchanged).
    """
    d = int(d)
    pad_shape = list(x.shape)
    pad_shape[axis] = d - 1
    pad = torch.full(pad_shape, float("nan"), dtype=x.dtype, device=x.device)
    x_padded = torch.cat([pad, x], dim=axis)
    return x_padded.unfold(axis, d, 1)
```

</details>
