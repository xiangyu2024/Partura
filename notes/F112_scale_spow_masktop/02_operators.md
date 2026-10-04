# 02 · 算子真实语义(逐个读源码 + 探针实测)

来源:`./scripts/study.sh src <op>`(服务器端内核源码,commit `1698296`)+ `./scripts/study.sh decompose`(内置合成探针,
没有为这条树单独写 `probes.py`,所以探针都是通用合成数据,不是这棵树的真实数据)。表达式里出现的 6 个算子全部读到。

---

## `day_quantile(x, q: float = 0.5)`

- **源码**:`operators/dt_day.py:150`,`return torch.nanquantile(x, q, dim=-1, keepdim=True)`
- **表达式里的调用**:`day_quantile(Close)` —— 只传了 1 个位置参数,**`q` 没有被显式传,用的是默认值 `0.5`,
  即中位数**。不要被「quantile」这个泛指的名字带偏,这条树里它就是中位数,不是别的分位。
- **计算轴**:`M`(日内分钟轴),`reduces_m=True` → 折叠成每股票-日一个值。不跨交易日。
- **齐次度**:`k=1.0`(探针实测)—— 带 `Close` 的价格尺度,**不是无量纲统计量**。
- **取负后**:`odd`(`f(-x)=-f(x)`)——与 `q=0.5` 时中位数关于取负对称的性质一致。
- **平移**:`平移不变=False`,准确说是**平移等变**(`f(x+c)=f(x)+c`),不是「不受平移影响」。
- **NaN/边界**:`nanquantile` 本身忽略 NaN;若当天该股票全部分钟都是 NaN,输出也是 NaN
  (探针 `all_nan_input_gives_all_nan=True`);10% 缺失时 `finite_frac_with_10pct_missing=1.0`,
  即只要还有 1 个有限值,分位数就能算,**没有最小样本量门槛**。
- **输出**:连续值,非布尔/非档位。
- **lookahead**:声明层面 `lookahead=False`。只用当天分钟数据,不涉及跨日,t 日收盘后即可得到。

---

## `day_kurt(x)`

- **源码**:`operators/dt_day.py:123`,整个函数只有一行:`return C._kurt(x).unsqueeze(-1)`。
- **⚠ 工具缺口**:`_kurt` 的源码**没有读到**。试过 `./scripts/study.sh src _kurt` 和
  `./scripts/study.sh src common._kurt`,都返回 `not found`。猜测原因:`C._kurt` 是「模块别名 + 属性」式调用
  (`import ... as C` 之后 `C.foo(...)`),remote_tools 的自动跟踪只解析得了「从模块直接 import 别名」式调用
  (比如 `cs_mask_top_replace_mean` 里的 `_common_rank` 能被正确解析回 `common.rank`,见下文),解析不了
  属性调用。这是**工具本身的局限**,不是没找。
- **跨实现互证**(非源码确认,仅供参考,置信但不等于源码事实):同一代码库里另外两处名字带「kurt」的实现,
  公式完全一致:
  - `nankurt_last`(`operators/common.py:582`,供 `ts_kurt`/`nt_ts_kurt` 用):
    ```
    mean = nanmean(w)
    var  = Σ(w-mean)² / count          (总体矩,除以 count 不是 count-1)
    m4   = Σ(w-mean)⁴ / count
    kurt = m4 / (var² + EPS) − 3       (var > EPS 才算,否则给 NaN)
    ```
  - `day_kurt_masked`(`operators/legacy_framework_compat.py:285`,docstring 自称「Fisher,减 3」):
    ```
    mu  = Σ(x·m)/n
    var = Σ((x-mu)²·m)/n
    std = sqrt(max(var, 1e-8))
    m4  = Σ((x-mu)⁴·m)/n
    kurt = m4/std⁴ − 3
    ```
  两者都是「总体矩算出的 Fisher 超额峰度(减 3)」,结构一致。**`_kurt` 极可能是同一公式,但这一点没有被源码
  逐字确认**,只是跨实现互证 + 探针吻合(见下)。
- **探针实测**(真实读到的,针对 `day_kurt` 本体):齐次度 `k=0.0`(无量纲,与上面公式吻合——峰度的量纲是
  4 阶矩除以方差的平方,缩放会抵消);取负后 `even`(`f(-x)=f(x)`,与「只看中心矩」的峰度定义吻合);
  平移不变 `=True`(超额峰度只看中心矩,加常数不变)。三项探针都与「总体矩算出的 Fisher 超额峰度」一致,
  但不能排除 `_kurt` 还有探针没测到的细节差异(比如方差的 `EPS` 保护写法、小样本下是否退化为 NaN)。
- **计算轴**:`M`,`reduces_m=True`,不跨日。
- **理论取值范围**(由 Fisher 超额峰度的通用性质推出,不是这棵树的实测):Pearson 不等式给出
  「超额峰度 ≥ 偏度² − 2 ≥ −2」,下界 `-2` 在两点分布时取到;上界无理论限制,当日内 `High` 序列出现
  长时间不变后突然跳变(停牌重开、一字板)时可以非常大。
- **输出**:连续值。
- **lookahead**:声明层面 `lookahead=False`。只用当天分钟数据。

---

## `add(a, b, fill_nan_with_zero: bool = False)`

- **源码**:`operators/common.py:129`。
- **表达式里的调用**:`add(day_quantile(Close), day_kurt(High))` —— 只传了 2 个位置参数,
  **`fill_nan_with_zero` 用默认值 `False`**:这是**标准 NaN 传播加法**,`A`、`B` 任一是 NaN,`C` 就是 NaN
  (不会把单边 NaN 当 0 处理;`fill_nan_with_zero=True` 的那条分支在这里**没有被用到**)。
- **计算轴**:`None`(逐元素),不折叠任何轴,也不跨日/跨股票——纯粹是 `A[day,stock] + B[day,stock]`。
- **齐次度**:`k=1.0`(探针实测)。**但要注意这是 `add()` 算子在「两个参数同步缩放」的合成探针下测出的性质**,
  不等于 `C=A+B` 在这棵树的真实数据里是齐次度 1 的量——`A`(价格水平,`k=1`)和 `B`(峰度,`k=0`)在真实世界的
  缩放行为并不同步(例如全市场价格整体重标度,`A` 会跟着变,`B` 不会)。`C` 是**两种不同量纲的量直接相加**,
  不是一个干净的、单一齐次度的量。
- **取负后**:`odd`(合成探针测得)。
- **NaN**:见上,标准传播。
- **输出**:连续值。
- **lookahead**:声明层面 `lookahead=False`。

---

## `cs_mask_top_replace_mean_neg(x, valid_mask=None, top_ratio: float = 0.1)`

- **源码**:`operators/nd_cs.py:239`,整个函数:`return -cs_mask_top_replace_mean(-x, valid_mask, top_ratio)`。
- **表达式里的调用**:`cs_mask_top_replace_mean_neg(add(...))` —— 只传了 1 个位置参数,
  `valid_mask` 用默认 `None`(等价于 `isfinite(x)`),**`top_ratio` 用默认值 `0.1`(10%)**。
- **⚠ 名字陷阱(重要,必须单独标出)**:算子名字里有 `mask_top`,字面像是「遮罩最高的」,
  但因为带 `_neg` 后缀,它用「取负 → 在负值上做 mask_top → 再取负」的技巧把语义从「遮罩最高」反转成
  **「遮罩最低」**。它调用的 `cs_mask_top_replace_mean` 的 docstring 写的是「替换每行最高 `top_ratio`
  比例」,但 `cs_mask_top_replace_mean_neg` 自己的 docstring 已经说清楚了:「Bottom-band counterpart:
  replace the lowest `top_ratio` fraction」。**这条树里实际用到的是 `_neg` 版本,效果是遮罩/替换最低的
  一部分,不是最高的一部分**——这是读代码时最容易看错的一处,因为只看「mask_top」四个字会直接看反。
- **精确算法**(源码逐行展开,`G = cs_mask_top_replace_mean`,`F(x) = -G(-x)`):
  - `valid = isfinite(x)`(`valid_mask=None` 时)。
  - 对当天(横截面,按 `S` 轴跨股票)这一行:`count` = 当天有效(isfinite)股票数;
    `n_top = ceil(count × top_ratio)`(**`ceil`,不是 `round`/`floor`**)。
  - 把 `x`(这条树里是 `C`)升序排名(`common.rank`,`pct=False`,整数排名),**排名最低的 `n_top` 只股票**
    (即 `C` 值最小的 `n_top` 只)被替换成**当天所有有效股票 `C` 的均值**(均值用全部有效值算,
    不是替换前后迭代);其余股票原样保留。
  - 无效(NaN)的股票保持 NaN,不会被替换——判定逻辑是 `top_mask = mask & (...)`,
    `mask` 为 `False` 时 `top_mask` 必为 `False`,`torch.where` 走 `else` 分支原样返回(NaN 还是 NaN)。
- **并列(ties)处理**:`common.rank`(源码 `operators/common.py`,通过 `nd_cs.py` 里的别名
  `_common_rank` 调用,工具能正确解析这个别名回 `common.rank`)用**两次 `stable=True` 的 `argsort`**
  打破并列,**按张量最后一维里的原始位置顺序**决定谁落在边界内外,不按任何业务含义的次要指标。
  这意味着:如果某天恰好有多只股票的 `C` 值完全相等且正好卡在 `n_top` 的边界上,
  谁被换、谁不被换由它们在数组里的原始排列顺序决定。
- **计算轴**:`S`(横截面,当天所有股票之间),**不跨日**。这是全树**第一个、也是唯一一个跨股票**的节点
  (`A`、`B`、`C` 都是逐股票独立算的)。
- **齐次度**:`k=1.0`(探针实测)——替换成的是均值,均值和原值同量纲,整体保尺度。
- **取负后**:`neither`(探针实测,既不是 odd 也不是 even)——因为「最低 10%」这个被选中的集合本身依赖
  符号,整体取负后被选中的股票集合会变,不是简单的符号对称。
- **平移**:`平移不变=False`。
- **NaN**:见上。
- **输出**:连续值,不是布尔;内部有一个中间布尔量 `top_mask`,但对外输出是替换后的浮点值。
- **lookahead**:声明层面 `lookahead=False`。只用当天跨股票的数据,不跨日,t 日收盘后、当天全部股票的
  `C` 值都确定了就能算。

---

## `signedpower(x, e: float = 2.0)`

- **源码**:`operators/common.py:230`,`return torch.sign(x) * torch.pow(torch.abs(x), e)`。
- **表达式里的调用**:`signedpower(cs_mask_top_replace_mean_neg(...))` —— 只传了 1 个位置参数,
  **`e` 用默认值 `2.0`**,即「带符号平方」:`E = sign(D) · D²`。
- **计算轴**:`None`,逐元素,不跨日/不跨股票。
- **齐次度**:`k=2.0`(探针实测,与 `e=2` 吻合)。
- **保序**:探针显式测出 `保序=True`——对固定 `e=2`,这是处处单调不减的函数(`x=0` 处导数为 0,
  其余各处严格递增)。**但「保序」只在同一时刻、同一比较轴的逐元素比较下成立**,不能据此推出
  「`signedpower` 对整条因子的秩是 no-op」——后面还有 `ts_scale`,它不是逐元素的(见下)。
- **取负后**:`odd`(`f(-x) = sign(-x)|-x|² = -sign(x)x² = -f(x)`,严格成立)。
- **NaN**:标准传播。
- **输出**:连续值。
- **⚠ 工具输出里一个容易误读的地方**:`decompose` 的自动抓取在 `signedpower` 下面附带打印了一段
  「`common.sign` 算子」的源码(`sign(x)=torch.sign(x)`)。`signedpower` 的函数体里调的是 **`torch.sign`
  (torch 原生函数)**,**不是**注册算子 `sign()` 本身;这段多余的附带输出看起来是自动抓取规则把源码文本里
  出现的 `torch.sign(` 误配成了「调用了算子 `sign(`」。不影响 `signedpower` 公式本身(已经从源码直接读到、
  确认无误),只是这一段附带信息和实际调用关系不一致,记下来提醒别被它带偏。
- **lookahead**:声明层面 `lookahead=False`。

---

## `ts_scale(x, d: int, constant: float = 0.0)`

- **源码**:`operators/nd_ts.py:205`:
  ```python
  def ts_scale(x, d, constant=0.0):
      w = rolling_windows(x, d, axis=0)      # 左补 d-1 行 NaN,因果滚动窗口
      return scale_last_ratio(x, w) + constant
  # scale_last_ratio(x, w):
  #   denom = nansum(w, dim=-1)
  #   denom = where(|denom| < EPS, 1, denom)  # 分母保护
  #   return x / denom
  ```
- **表达式里的调用**:`ts_scale(signedpower(...), 30)` —— 显式传了 `d=30`;**`constant` 用默认值 `0.0`**。
- **精确公式**:`F[t] = E[t] / nansum(该股票过去 30 个交易日(含 t)的 E) + 0`。
- **计算轴**:`D`(交易日轴),**逐股票独立**滚动——`rolling_windows(x, d, axis=0)` 的 `axis=0` 是日轴,
  每只股票用的是**它自己**过去 30 个交易日的 `E` 值求和,**分母不是跨股票共享的**。
- **窗口/回看**:显式窗口 `30`。`rolling_windows` 对日轴左侧补 `d-1=29` 行 NaN,保证序列最前面的交易日也有
  一个(更短、含 NaN)的窗口;`nansum` 自动忽略窗口里的 NaN,即**不足 30 天时用实际可得的天数求和**,
  不是报错或整体置 NaN。这是全树**唯一**跨交易日的节点,也是唯一贡献「回看天数」的节点
  ⇒ **全树真实回看 = 30 个交易日**,与 `decompose` 报的「日轴最大单窗口 30 天」一致(因为只有这一个跨日
  节点,不存在「路径累加 vs 取最大值」的歧义)。
- **分母保护**:`|nansum(窗口)| < EPS` 时,分母整体替换成 `1`(即退化为 `F[t] = E[t]`),避免除零/除以
  接近 0 的数爆炸。`E` 是带符号平方后的量,一个窗口内正负可能部分抵消,这个保护分支在理论上是会被触发的
  (多频繁触发没有做实测,见文末缺口)。
- **齐次度**:`k=0.0`(探针实测)——分子分母同阶,整体对缩放不敏感,是个「比值」量。
- **因果性**:探针显式验证 `日轴因果性=True`(改动 t 之后的行,不影响 t 的输出)。
- **窗口变长**:探针测得 `non_increasing`(在探针的合成输入上,窗口越长输出不增)——这是探针在合成数据上的
  方向性,不是这棵树用真实数据做参数扫描的结果。
- **脉冲记忆**:探针测得 `30` 天,与窗口长度一致,说明没有超出窗口之外的额外记忆。
- **取负后**:`even`(探针实测;公式上 `f(-x) = (-x)/nansum(窗口的-x) = (-x)/(-nansum(窗口的x)) = f(x)`,
  只要没触发 `EPS` 保护分支就严格成立)。
- **NaN/边界**:若某只股票某天的 `E` 本身是 NaN(例如当天 `C` 是 NaN,一路传播下来),**该天输出 `F` 直接是
  NaN**(分子 NaN,NaN 除以任何数还是 NaN),不受分母的 `EPS` 保护影响,也不会被窗口里别的天「平均」掉。
- **⚠ 名字陷阱(重要,必须单独标出)**:「scale」容易被读成「只是在调整数值的量级/幅度,不改变排序、
  不影响多空分组」。但因为**每只股票除以的是它自己的滚动和,不是全市场共享的同一个分母**,`ts_scale`
  在同一天对不同股票做的是**不同倍数**的缩放。两只股票 `i`、`j` 在 `E` 上 `E_i[t] > E_j[t]`,
  换到 `F` 上因为 `denom_i[t] ≠ denom_j[t]`,顺序完全可能反过来。**`ts_scale` 一般不是横截面保序的**
  ——这是直接从公式推出的事实:`decompose` 的探针表把 `rank_preserving` 标成「不适用」(没有对这个算子
  测这一项),所以这一点没有探针读数可以直接引用,是从源码公式推导出来的,不是探针实测到的。
- **输出**:连续值。
- **lookahead**:声明层面 `lookahead=False`,且探针显式验证了日轴因果性。

---

## 调用链汇总(便于核对,`→` 表示「调用」)

```
day_quantile              torch.nanquantile                                        [源码确认]
day_kurt                  C._kurt                                                   [源码点出调用,_kurt 本体未读到;
                                                                                       跨实现互证指向总体矩 Fisher 超额峰度]
add                       create_like(仅当某操作数是 Python 标量时)                    [源码确认;这里两个操作数都是 Tensor,不触发]
cs_mask_top_replace_mean_neg → cs_mask_top_replace_mean(-x,...) → _common_rank(=common.rank)
                                                                 → _mean(=common._mean = nanmean)
                                                                 → nd_cs._valid(=isfinite 与可选 mask 的与)    [全部源码确认]
signedpower                torch.sign、torch.pow(torch 原生函数;附带输出里的「common.sign」
                                                   是自动抓取的误配,不是真实调用)                              [源码确认 + 一处工具误配已标注]
ts_scale                  common.rolling_windows、common.scale_last_ratio             [源码确认]
```

## 本文没有做的事(明确的缺口,留给需要时再补)

1. `day_kurt` 内部 `_kurt` 的源码文本没有读到(工具限制,见上),只做到跨实现互证 + 探针吻合。
2. 没有对任何算子在**这条树的真实数据**上跑自定义探针(没有写 `studies/F112_scale_spow_masktop/probes.py`);
   以上「取值范围」类陈述(峰度的理论下界等)都是通用数学性质,不是这条树的实测分布。
3. `ts_scale` 的 `EPS` 分母保护分支在真实数据里触发的频率没有实测。
