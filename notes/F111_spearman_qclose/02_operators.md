表达式里出现的算子只有两个:`day_quantile`、`ts_spearman`。下面每条都是
`./scripts/study.sh src day_quantile ts_spearman` 读到的内核源码(`/root/autodl-tmp/AlphaCube/src/alphacube/
operators/dt_day.py:150`、`.../operators/nd_ts.py:483`)加探针实测(`./scripts/study.sh decompose` 的输出),
不是按名字猜的。

---

## `day_quantile`

- 注册:`@op("dt", "day", arity=1)`,face `dt` / family `day` / category `unary`,计算轴 **M**(日内分钟),
  `reduces_m=True`(折叠 M→1),`lookahead=False`。
- 精确公式:
  ```python
  def day_quantile(x, q: float = 0.5) -> Tensor:
      return torch.nanquantile(x, q, dim=-1, keepdim=True)
  ```
  对当天所有**非 NaN** 的分钟值,沿分钟轴取第 `q` 分位数(torch 默认线性插值:分钟数为偶数时取中间
  两个有效值的插值,不是就近取整)。
- **本表达式里的调用是 `day_quantile(Close)`——只给了 1 个参数,`q` 用的是默认值 0.5,也就是中位数**,
  不是某个专门挑的分位点。
- 沿交易日轴(D):**没有窗口**,不滚动。第 t 天的 A 值只用第 t 天自己的分钟数据,不依赖其他交易日,
  自然不存在"看未来交易日"的问题(`lookahead=False` 与此一致)。
- 齐次度(探针实测):**k=1.0**——分位数是线性的,x 整体乘常数 c,输出也乘 c(带尺度,单位和输入一致)。
- NaN / 边界:`nanquantile` 直接忽略 NaN;探针"10% 随机缺失下的有限值占比"= **1.0**(只要当天不是
  全部分钟都缺失,就有输出);探针"全 NaN 输入 → 输出也全 NaN"= True。没有"窗口不足"的情形(它不滚动)。
- 输出:连续值,不是布尔或档位。
- 不适用于该算子的探针(声明层面就跳过,不是读数缺失):`causal_on_day_axis`(它不在日轴上滚动,
  这个探针问的是日轴因果性,对它没有意义)、`rank_preserving`、`monotone_in_window`、`effective_memory`
  (后两个都假定有"窗口"这个概念)。

**和名字不一样的地方:**

1. 因子名 "`F111_spearman_qclose`" 里的 "q" 容易让人以为是某个特别选的分位点(比如 0.9 分位的
   "尾部收盘价"),但表达式没写 `q`,实际落到的是**默认中位数(q=0.5)**。
2. 项目的算子表里**另外有一个独立注册的 `day_median`**(`dt_day.py:93`,`@op("dt","day",arity=1)`,
   内部调 `C._median(x).unsqueeze(-1)`,不是 `torch.nanquantile`)。这条因子没有用它,而是靠
   `day_quantile` 省略 `q` 落到同一个统计量(日内中位价)。两者在**统计定义**上是同一个量,但
   **代码路径不同**:`day_quantile(x,0.5)` 走线性插值的 `nanquantile`;`day_median` 走 `C._median`。
   `C._median` 是未注册的内部辅助函数,`./scripts/study.sh src _median` / `src C._median` 都查不到
   (`not found`)——这是工具的解析边界(只认注册表里的算子名),不是这条因子本身的问题,因为
   `day_median` 根本不在这棵树里。**分钟数为偶数的交易日,`day_quantile(Close)` 和 `day_median(Close)`
   是否逐位相同,本次没有验证**(需要读到 `C._median` 的实现或者直接拿两个变体跑数才能确认)。

---

## `ts_spearman`

- 注册:`@op("nd", "ts", arity=1, requires_window=True)`,face `nd` / family `ts` / category `rolling`,
  计算轴 **D**(交易日),`lookahead=False`。**注意 `arity=1`**——声明上只接受一个"数据"参数(另一个
  参数 `d` 是窗口字面量),不是两个序列的相关。
- docstring:"Rolling rank (Spearman) correlation counterpart to `ts_pearson`."
- 完整签名:`ts_spearman(data, d, abs_corr: bool = False, agg: str = "mean")`。本表达式 `ts_spearman(A, 10)`
  用的是 `d=10`,`abs_corr=False`、`agg="mean"` 都是默认值。
- **精确机制(这是本节最重要的一条,源码读出来的,和算子名/声明的 family 不一致)**:

  `data` 的形状是 `(D, N)`——**整张面板一次性传入**(这也是"ts_* 是 ND 面、一次吃整张面板"的字面
  体现:playbook 里说显存紧张时 `ts_*` 可能求值失败,`cross_*` 按股票分块,原因就在这里)。
  函数体内部有一个 `for i in range(N)` 的 **股票维度循环**:对每只股票 `i`,把它和**所有其他股票
  `j≠i`**(向量化处理)在同一个 `d` 天窗口里做 Spearman 相关,再对 `j` 取平均(`agg="mean"`)或标准差
  (`agg="std"`,本因子没用到)。也就是说:

  > **`ts_spearman(x, d)` 不是"股票自己的值和自己过去的排名/和时间趋势的秩相关"这种单变量时间序列
  > 统计量,而是一个"滚动窗口 + 全市场配对"的混合算子:它用窗口期内的面板,计算每只股票和全市场
  > 其他每只股票的滚动 Spearman 相关,再取横截面平均。**

  具体步骤(对应源码 `operators/nd_ts.py:483-557`):
  1. `data.unfold(0, d, 1).transpose(1,2)` 把面板切成 `[T, d, N]` 的滚动窗口(`T=D-d+1`),
     `windows[t,k,n] = data[t+k, n]`。
  2. 沿 `dim=1`(窗口内的"第几天",大小 d)用双重 `argsort`(`stable=True`)算秩——NaN 先填 `+inf`
     参与排序(这样有限值之间的相对秩不受影响,因为 inf 总排在最后),算完秩再把 NaN 位置盖回 NaN。
     **这是普通的序数秩(0..有效个数-1),没有对并列值做平均秩修正**;`day_quantile(Close)` 这种连续值
     理论上很少出现并列,所以这点实践影响应该很小,但没有对此单独验证。
  3. 秩减去窗口内的均值 → `rc[t,k,n]`(去均值的秩)。
  4. 对每只股票 `i`:取它的 `rc_i[t,:]`,和每只 `j≠i` 的 `rc_j[t,:]` 在"窗口内第几天"这根轴上做
     内积 / 两边模长,得到 `corr(t,i,j)`——这正是股票 `i`、`j` 在该 10 天窗口里**按日期对齐**的值序列
     的 Spearman 相关(两只股票是不是在同样的日子涨、同样的日子跌,按秩衡量)。要求窗口内两只股票
     **重叠的有效天数 ≥ 2**,否则该对相关记 NaN(`torch.where(num_valid>=2, corr, nan)`)。
  5. `F111[t,i] = mean_{j≠i} corr(t,i,j)`(`nanmean`,自动跳过第 4 步里记成 NaN 的那些 j)。
  6. 前 `d-1=9` 行(不够 10 天窗口的交易日)整行 NaN(`final[d-1:,:] = result_per_stock`)。

- 真实回看:**9 个交易日**(算第 t 天需要 `[t-9, t]` 共 10 天);**真实窗口 = 字面参数 d=10,这一点
  和名字字面一致**,不是一个要单独标出来的差异。
- 齐次度(探针实测):**k=0.0**——整张面板同乘正常数,相关系数不变,符合"相关系数不带尺度"。
- 取负(探针实测):**even**(整张面板同时取负号,输出不变)。源码上可以推:取负只让每只股票窗口内
  的秩整体翻转、`rc` 整体变号,但 `rc_i` 和 `rc_j` 同时变号,乘积不变,相关系数不变——这是对探针读数
  的代码推演,不是额外下结论。
- 平移不变(探针实测):**True**(`f(x+c)=f(x)`)——加常数不改变秩的顺序,符合预期。
- NaN / 边界:`d<=1` 或总天数 `D<d` 时整张输出是 NaN;窗口内单只股票自己的 NaN 天不参与排名;
  配对相关要求重叠有效天数 `≥2`,不满足记 NaN 并在横截面平均时跳过。探针"10% 随机缺失下的有限值
  占比" = **0.775**(明显低于 `day_quantile` 的 1.0,说明这个算子对缺失更敏感——这是读数,没有去
  深究具体原因)。
- 输出:连续值(相关系数,理论范围 `[-1,1]`),不是布尔或档位。
- lookahead:声明 `lookahead=False`;探针"日轴因果性" = **True**;`final[d-1:,:]=result_per_stock`
  的对齐方式也印证了第 t 天只用到 `[t-9,t]` 的历史窗口,没有错位去用未来行。
- **探针"脉冲记忆天数"读数 = 0**(待核实的异常,见下)。
- 不适用于该算子的探针:`order_dependent_on_minutes`(它不在分钟轴上操作)、`rank_preserving`
  (它的输出是相关系数,不是对输入的保序变换,这个探针问的是"外层变换是否保序",对它不适用)。

**和名字/声明不一样的地方(汇总,最重要的发现):**

- family 标的是 `ts`(通常理解为"沿时间轴滚动、每只股票独立计算"),但实际实现里有一个显式的
  **跨股票循环**,输出是**横截面平均**——不是单只股票自己的时间序列统计量。
- 算子名字和 docstring("Rolling rank correlation counterpart to `ts_pearson`")容易让人联想到
  "两个序列的滚动相关"(像 `cross_corr(x,y,d)` 那样),但 `ts_spearman` 的**声明 arity=1**,表达式里
  也只写了一个数据参数——它的"另一个操作数"不是表达式里的另一棵子树,而是**股票轴本身**(每只股票
  和全市场其他股票两两配对),这个"操作数"从表达式结构上是看不出来的,必须读函数体内的 `for i in
  range(N)` 循环才知道。

**探针读数异常(留给后续核实,不是结论):**

- `ts_spearman` 是一个 `d=10` 的滚动窗口算子,直觉上单日脉冲应该在之后最多 9 天的窗口里留下可观测的
  残留影响;但内置"脉冲记忆天数"探针测出来是 **0**。没有去改写探针或验证这个读数对这个算子是否有效
  (比如探针的脉冲是否同时扰动了被比较的 `j` 侧、或者"对所有其他股票取平均"这个结构会不会把单只
  股票的脉冲摊薄到探针阈值以下)。**原样记录读数,不替它找原因。**
