# 结构解剖:种子 801,C 组,第 2 轮

快照:`c05s801M1_I0_open_search`、`c05s801M2_I0_open_search`(M 第 1–2 批)、`c06s801Cr1a_Na`、`c06s801Cr1b_Nb`;326 个已评分候选,5 个 head,R 替换 0 个、R 收录 0 个。
本文件用的材料:`r2/loc.md` / `loc.json`、`r2/R_prev.json`、`r1/`(analysis、lit、missions_final、audit_1、corr_1、audit_record)、`notebook.md`、`rules.md`,以及算子源码
`partura/ops_ext.py`、`partura/steer.py`、`partura/diagnose.py`、`alphacube/operators/common.py`、`operators/dt_cross.py`、`operators/dt_day.py`、`scripts/c05_locate.py`。
没有读其他种子、C01–C05、`guidance/C0*`、`runs/`、`lab/`、`notes/`、`studies/`、`handoff/`、`batches/`、`docs/`、`episodes/`,也没有碰 2023-08-08 之后的任何数字。

为了把算子语义讲清楚,我把 `ops_ext.py` 里的 `_pct_rank` / `_rank_block` / `_lexi` 三个纯函数原样抄出来在 20 只股票 × 5 天的玩具张量上跑了一遍(**只跑算子代码,没有跑服务器、没有碰立方体**)。
下面 §1.1 的三条「位等同」结论来自那次运行。

---

## 0. 一句话结论

**5 个 head 里有 2 个(score +1.53 和 +0.75)是规则 §4.2「列序斜坡」的纯发作,不是 alpha。**
`cs_state_rank(x, d)` 的源码写明它返回**每天一个、全截面相同的市场状态数**;把它喂给任何基于 `_pct_rank` 的 `cs_*` 算子,输出就退化成一条**按股票列序排的静态斜坡**。
head +0.75 的 `cs_last_high10(y, x)` 的 **y 和 x 都是**这种每日常数,所以它的面板**完全不含个股信息**,只是(列序,当日宇宙成员)的函数;
head +1.53 唯一活着的经济输入是一个二值标记「当日 `log(day_first(Open))` 是否在最高 10%」,其余全是列序。
定位输出里的敏感性表已经把这件事写在脸上:head +1.53 的 `High->Low` 得 **+1.5294**(head 本体 +1.529386,四位小数全等、`rho_known` 也全等 −0.0721),
head +0.75 的 `Vwap->Close` 与 `High->Low` 都得 **+0.7493**(head 本体 +0.749257)。**换字段得分位等同 = 字段根本没被读。**

剩下 3 个 head 里:
- **+1.22**(本组 r1b 的产出)是规则 §4.3「控制变量的非线性重写」:分母 `day_sum(pow_3(Volume))` 自身的 `rho_known` = **+0.5805**,`mul(·,·)` 版本 **+0.5249** —— 按环境自己的口径(与已知族 |ρ| ≥ 0.5 判不合格)**这个部件就是已知族**;而且分母凸度越高分越高(÷Σv³ 得 +0.70,÷(Σv³)² 得 +1.22),正是陷阱 1 的指纹。
- **+0.61**(本组 r1a 的产出)是目前**唯一每个部件都干净、敏感性也稳**的 head:日内资金加权收益相对等权收益的倾斜。但 r1 审计员已经先给出一个强力的竞争解释(日内成交额的开收盘 U 形),本轮必须用 R 把它分开。
- **+0.50**(M 第 1 批)仍是 `LogFloatShares` 那条水平线;r1 的 R 把「低名义股价」这个解释**打掉了**(见 §3.4),而剩下的两个解释(残留非线性规模曲率、管道假象)因为 PI 删掉了那三个变体而**至今未检验**。

**对本轮的直接含义:**
1. 定位输出的机械核心卡里,**第 2、7、17、18、19、21 号全部是列序斜坡的零件**,第 3–12 号是 `LogFloatShares` 幂族(size |ρ| = 0.78,E 位必被判死),第 1、16 号是 Σv³ 凸度族(`day_sum(pow_3(Volume))` 的 rho_known 0.58 ≥ 0.5)。
   **B0 会按核心卡顺序取第 1 名,也就是 Σv³ 那个 —— 这正是本实验要比的东西,PI 应当明确写下为什么不取它。**
2. 本轮最值得花的付费评估不是深挖,而是**两次 R:把列序斜坡的「地板分」买下来**(§4.2 的 R6a / R6b)。如果一条纯列序的静态组合在这个奖励下就能拿 ≥ 0.5 的净夏普,那么库里 2 个 head、M 后面两批、以及所有组的结论都要重读一遍。
3. E 位只有一个核心是干净的:`div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret))`。

---

## 1. alpha 的来源

### 1.1 head +1.53 与 head +0.75:列序斜坡(陷阱 §4.2),不是来源

两个 head 的骨架是同一个模板。为了能读,记
`V := cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))`(原文见 loc.md 第 9 行),
则 head +1.53 = `cs_first_high40(cross_corr(inv(V), cs_last_high10(cs_first_high40(cross_corr(inv(V), V, 241), V), log(day_first(Open))), 241), cs_last_high10(cs_first_high40(cross_corr(inv(V), V, 241), V), log(day_first(Open))))`,
head +0.75 = `cs_first_high40(cross_corr(inv(W), W, 241), W)`,其中
`W := cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50)))`。

**源码事实一(`ops_ext.py` 第 547 行):**

```python
@op("nd", "ts", arity=1, requires_window=True)
def cs_state_rank(x, d):
    """A MARKET state, the same number for every stock on a day: ..."""
    r = _trailing_rank(_market_series(x), d)
    return r.unsqueeze(-1).expand_as(x).clone()
```

`_market_series` 是 `torch.nanmean(..., dim=-1)`(整个截面求均值),再 `_trailing_rank` 取它在自己最近 d 天里的分位,最后 `expand_as` 铺回全截面。
**所以 `cs_state_rank(任何东西, 任何窗口)` 在每一天都是一个常数面板,截面标准差恒为 0**(我跑的玩具张量:每日截面 std = 0.0)。

**源码事实二(`ops_ext.py` 第 231、326、339 行):** `cs_last_high10(y, x) = _lexi(y, x, 0.9, 1.0, -1.0)`,即
`_pct_rank(y) − 1·[x 所在的整个并列块落在最高 10% 内]`。而 `_pct_rank` 是

```python
v = torch.where(ok, x, torch.full_like(x, torch.finfo(x.dtype).max))
r = (torch.argsort(torch.argsort(v, dim=-1, stable=True), dim=-1, stable=True) + 1).to(x.dtype)
```

**stable 排序 + 全部取值相同 ⇒ 名次就是列下标。** 于是:

| 我跑出来的 | 结果 |
|---|---|
| `cs_last_high10(每日常数, 真个股量)` 第 0 天 | `[0.05, 0.10, …, 0.65, −0.30, −0.25, 0.80, …, 1.00]` —— 就是 `i/n` 这条斜坡,被标记的两只减 1 |
| 常数整体缩放 ×7.3、平移 +100 后输出 | **位等同**(`torch.equal` = True) |
| 把常数换成**完全不同的随机序列** | **位等同**(`torch.equal` = True) |
| `cs_last_high10(每日常数, 每日常数)`(= W 的形状) | 恰好等于 `i/n`,**band 一次都没触发**,`(v<0).any()` = False |
| 第 3 天有 4 只退出宇宙时 | 斜坡按新的 n 重新归一:`[nan,nan,nan,nan,0.062,…,1.0]` |

**对上定位输出里的数字:**

| 证据 | 数值 | 读法 |
|---|---|---|
| head +1.53,`swap High->Low` | score **+1.5294**,rho_known **−0.0721**(head 本体 +1.529386 / −0.0721) | `day_es_ratio_hi(High)` 的内容被整段丢弃 |
| head +1.53,`swap Open->Close` | score +1.4821,rho_known −0.0718 | 唯一活着的输入是 x 位置上的 `log(day_first(Open))`,换成 `day_first(Close)` 会轻微改变「最高 10%」的成员,所以只差 0.047 |
| head +0.75,`swap Vwap->Close` | score **+0.7493** | 位等同 |
| head +0.75,`swap High->Low` | score **+0.7493** | 位等同 |
| 两个 head 的 `distinct` | 1.0;`coverage` 0.9993 | 斜坡逐只不同,`distinct_fraction ≥ 0.5` 的门形同虚设 —— 陷阱 §4.2 说的「借它通过 distinct 门槛」 |
| 共性表第 1、6、17、18、20、21 行 | 全是这个骨架的零件 | 「n_with = 4、p = 0.003」只是在说「这 4 个候选就是那两个 head 自己」 |

**结论(可判定的部分):**

- head +0.75 的面板是 **(股票列下标, 当日宇宙成员) 的函数,不含任何个股的价格、成交或规模信息**。它的多头十分位 = 一组按列序固定的股票代码,只在有股票上市 / 退出时慢慢漂移。
  列序是什么(代码序、入库序,还是别的)我无从得知,但**无论它是什么,它都不是一个经济量**。train +0.75 / valid +1.66 衡量的是「一个几乎静态的代码段组合在扣掉 5 个控制之后的净夏普」。
- head +1.53 的经济内容只有一条:**「当日 `log(day_first(Open))` 是否落在最高 10%」**。而 `day_first(Open)` 是**后复权**价(r1 审计员已据 `tradability.py` / `label.py` / `daily.py` 指出这一点),
  所以这个标记的含义是「上市以来累计总收益 × IPO 价是否在全市场前 10%」—— 一条**超长期累计动量 / 存活质量**的二值标记,不是名义股价。
  `cross_corr(inv(V), ·, 241)` 读的是这个标记与列序斜坡在过去 241 天里一起变了多少次,`inv` 又把斜坡值接近 1 的被标记名字炸到 −∞ 附近 —— 这一层是数值噪声,不是机制。
- 必要性表看起来「核心很必要」(敲除 `cross_corr` 掉 **+3.43** / **+2.74**),但那只是说「拆掉斜坡的组合方式之后这条静态组合换了一本书」,**不能**读成「这个结构携带信息」。
  同理 `cross_corr@241->120 / 482` 的 +1.35 / +1.33(head +1.53)和 +0.22 / −0.54(head +0.75)只是斜坡漂移窗口的长短,不是预测期的长短。

**真来源 vs 代理:** 两个 head **都不是代理,是零**。head +1.53 里唯一可能是真来源的是那条后复权价格最高十分位的标记(见 §4.1 核心 C)。

### 1.2 head +1.22:凸度买来的分数(陷阱 §4.3 + §4.1)

原文 `cross_mean(div(day_sum(mul(mul(Ret, Ret), Ret)), mul(day_sum(pow_3(Volume)), day_sum(pow_3(Volume)))), 20)`。

| 部件 | 单独当因子(充分性) | 敲除后 | 必要性 | rho_known |
|---|---|---|---|---|
| `div(day_sum(mul(mul(Ret, Ret), Ret)), mul(day_sum(pow_3(Volume)), day_sum(pow_3(Volume))))` | **+0.83** | −0.52 | **+1.73** | −0.1333 |
| `day_sum(mul(mul(Ret, Ret), Ret))`(分子 Σr³) | **−0.35** | — | — | +0.0748 |
| `mul(day_sum(pow_3(Volume)), day_sum(pow_3(Volume)))`((Σv³)²) | −1.65 | +0.70 | **+0.52** | **+0.5249** |
| `day_sum(pow_3(Volume))`(Σv³) | −1.82 | — | — | **+0.5805** |

四条读法:

1. **分母是已知族。** `day_sum(pow_3(Volume))` 的 `rho_known` = **+0.5805**,`mul(·,·)` 版 **+0.5249**。规则 §1 写明「与已知族 |ρ| ≥ 0.5 的判为不合格」—— 这个部件单独提交会被判不合格。
   已知族控制是 `cross_mean(day_std(Amt), 30)`,而 Σv³ 由当日成交量最大的几分钟主导,本质就是**日内成交集中度³ × 成交水平**,与已知族是同一个量的凸变换。这是规则 §4.3 的教科书形态。
2. **凸度越高分越高。** 分母用一次 Σv³ 得 **+0.70**,用 (Σv³)² 得 **+1.22**(必要性 +0.52)。分子单独 −0.35。
   也就是说分数**不是**由「已实现偏度」提供的,而是由「分母对成交量的凸度」提供的 —— 规则 §4.1 描述的「凸度越高 score 越高,线性中性化去不掉凸的那部分」,只不过这里的被重写对象是流动性 / 已知族而不是波动。
3. **GP 是主动离开偏度轴的。** r1 的 b 位种子 6 是正确的 ACJV 归一化 `cross_mean(div(day_sum(mul(mul(Ret, Ret), Ret)), mul(day_sum(mul(Ret, Ret)), sqrt(day_sum(mul(Ret, Ret))))), 20)`,种子 7/8 是精确的 RSJ。
   b 位 83 个评分、4 个过线,**best 5 全部是 Σv³ 分母那一族**(loc.md「本组之前各轮的任务」),没有一个是标准化偏度。GP 把 `Σr²·sqrt(Σr²)` 换成了 `(Σv³)²` —— 它爬的是成交量凸度的梯度。
4. **数值上它是坏的。** `mul(day_sum(pow_3(Volume)), day_sum(pow_3(Volume)))` 的 `coverage` 只有 **0.9228**(其余所有变体都是 0.9993),即 **7.7% 的有标签股票日取值非有限**(float32 上限 3.4e38,Σv³ 再平方会溢出到 inf,`np.isfinite` 判 False);
   `div(...)` 的 `distinct` 掉到 **0.846**、窗口变体 0.8822 / 0.9038,说明还有 10–15% 并列。
   `swap Volume->Amt` 直接 **gate = False(distinct 0.1817)** —— 换一个量纲更大的同类字段,整个表达式塌成常数。**「换同类字段」这项敏感性检验等于不及格。**

**真来源 vs 代理:** 分子(日内已实现三阶矩)是真量但单独无用(−0.35);分母是**已知族的凸重写**。这个 head 应当被读成「非线性流动性暴露 × 弱偏度调制」,它过线主要靠前者。

### 1.3 head +0.61:目前唯一干净的来源

原文 `cross_mean(cross_ema(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 10), 15)`,sign **+1**,hl 20。

机制:`day_wmean(Ret, Amt)` 是成交额加权的分钟收益均值,`day_mean(Ret)` 是等权均值,差值 = **当天的钱是在涨的分钟还是跌的分钟成交的**(日内净买压 / 资金流倾斜),再除 `day_std(Ret)` 去量纲,然后 EMA(10) + 均值(15) 做成约 20–25 天的持续量。sign +1 ⇒ **多头 = 资金流倾斜长期为正的名字(延续,不是反转)**。

| 类型 | 改了什么 | score | 必要性 |
|---|---|---|---|
| sufficiency | `cross_ema(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 10)` | **+0.48** | — |
| sufficiency | `div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret))`(未平滑) | **−2.36** | — |
| sufficiency | `sub(day_wmean(Ret, Amt), day_mean(Ret))` | −2.15 | — |
| sufficiency | `day_wmean(Ret, Amt)` | −1.87 | — |
| knockout | 去 `cross_ema` | +0.38 | +0.23 |
| knockout | 去 `div(·, day_std(Ret))` | +0.06 | **+0.54** |
| knockout | 去 `sub(·, day_mean(Ret))` | +0.38 | +0.23 |
| swap | `Amt->Volume` | +0.60 | −0.01 |
| window | `cross_mean@15->7` | **+0.65** | −0.047 |
| window | `cross_mean@15->30` | +0.50 | +0.105 |

读法:
- **alpha 在「持续性」里,不在当日值里。** 未平滑的日度值 −2.36,EMA(10) 之后 +0.48,再叠 15 日均值 +0.61。双重平滑贡献了 3 个夏普。这既是好消息(日内资金流倾斜是**慢变的股票属性**,不是一次性事件)也是风险(双重平滑等于 20–25 天的低通,很容易和任何慢变风格相关)。
- **每个部件都有正必要性,没有装饰。** 去量纲(÷`day_std(Ret)`)必要性 +0.54 最高 —— 这正是陷阱 1 要求的那一步(不让波动从缝里漏回来)。
- **敏感性稳:** 字段换 Amt→Volume 只差 −0.01;窗口 7 / 15 / 30 得 +0.65 / +0.61 / +0.50,单峰、平滑,不是窗口挑出来的。
- **唯一的竞争解释来自 r1 审计员(audit_1.yaml slot a):** 「分钟成交额有很强的开收盘 U 形,`day_wmean − day_mean` 的截面差异大半是开盘 / 尾盘时段收益减盘中收益,不是 GKM 意义上相对自身历史的异常放量」。
  如果这条对,这个 head 实际读的是**时段构成效应**(开收盘段收益 vs 盘中段收益),而不是资金流。审计员在它还是一个种子的时候就说了这句话,而它恰好就是产出 head 的那个种子 —— **这是本轮最该用 R 买下来的判别**(§4.2 的 R14 / R15)。
- 相关度表(r1 corr_1,平滑 20 日版本):rev **0.49**、vol 0.31、liq 0.13、known 0.17、size 0.01。**rev 0.49 贴着 0.5 的门槛**,是这条轴最大的制度性风险。

### 1.4 head +0.50:`LogFloatShares`,解释被 r1 的 R 推翻了一个、剩两个未检验

见 §3.4。短版:低名义股价的解释**没有复现**;size |ρ| = 0.78 使它永远不能当 E 核心;它的 +0.000147 过线余量仍然是一次掷硬币。

---

## 2. 烂部件(适合做 R)

按「必要性 ≤ 0 或换掉反而更好」的字面标准,`loc.json` 的 `r_candidates` 是空的(没有变体比原 head 高 +0.1)。但按字面标准逐条翻,有 **4 类**可报:

**(A) 必要性恰好为 0 —— 整段死部件(head +1.53、+0.75)**
- head +1.53:`swap High->Low` 得 **+1.5294 / rho_known −0.0721**,与 head 本体(+1.529386 / −0.0721)位等同 ⇒ `cs_state_rank(day_es_ratio_hi(High), 50)` 这整棵子树的**必要性恰好是 0**,它读的字段、它的窗口 50、它的 `day_es_ratio_hi` 全都不进入结果。
- head +0.75:`swap Vwap->Close` 与 `swap High->Low` 都得 **+0.7493** ⇒ `cs_state_rank(day_es_ratio_hi(Vwap), 50)` **和** `log(cs_state_rank(day_es_ratio_hi(High), 50))` 两段都是死部件,整个 head 没有一个活着的经济部件。
- 依据不止是这两个数,还有 §1.1 抄出来的源码和跑出来的位等同。**这是本轮最硬的「烂部件」证据。**

**(B) 必要性为负 —— 去掉略好(head +1.53)**
- 敲除 `cs_last_high10(cs_first_high40(cross_corr(inv(V), V, 241), V), log(day_first(Open)))`(第 2 个参数外面那层 `cs_last_high10`)得 **+1.5389**,必要性 **−0.01**。
- 幅度 0.009,远低于替换门槛 +0.1,单独做 R 不划算;只在证明链里有用。

**(C) 分母是已知族 + 凸度梯度(head +1.22)**
- `day_sum(pow_3(Volume))` 的 `rho_known` **+0.5805**、`mul(·,·)` 版 **+0.5249**,按规则 §1 的口径这个部件就是已知族;
- 分母从 Σv³ 变 (Σv³)² 使 score 从 +0.70 升到 +1.22,凸度是分数的来源;
- `coverage` 0.9228(7.7% 非有限)、`distinct` 0.846、`swap Volume->Amt` 直接不过门。
- **三条都满足「这个部件真是烂的」的举证要求**(数值坏、与控制同族、分数由凸度而非机制提供)。

**(D) 窗口不是最优 —— 幅度不够的小便宜(head +0.61)**
- `cross_mean@15->7` 得 **+0.6526**(+0.047),`swap Amt->Volume` −0.01。单独都到不了 +0.1,要叠着别的改动一起买。

**没有烂部件可报的:** head +0.50 的四层包装(r1 已经买完:裸字段 +0.4826、`inv` 版 +0.4777、`cross_min` +0.4801、`cross_max` +0.4760,必要性全在 +0.02 ~ +0.025 的噪声带里,结论是「装饰」而不是「有害」)。

---

## 3. 之前的任务

### 3.1 E 位:**一个都没开**

r1 两个位都是 N(notebook.md 已写明理由:所有合法核心都是 `LogFloatShares` 的单调变换,size |ρ| 估计 0.75–0.8;corr_1 实测 **0.78**,确认了这个估计,E 位必被判成「控制换个写法」)。
所以「E 在哪个核心上试了什么外围 / 有没有产出 heads / 采样计数」这一问在本种子**无数据**:`missions_before` 两条的 `core` 都是 `—`,`采样计数 {}`。

### 3.2 N 的结果

| 位 | 轴 | 评分 | 过线 | 入 heads | 产出 |
|---|---|---|---|---|---|
| `c06s801Cr1a_Na` | 放量收益反转 / 量价交互 | 86 | 1 | **1** | `cross_mean(cross_ema(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 10), 15)` +0.61 |
| `c06s801Cr1b_Nb` | 彩票偏好 / 已实现偏度 | 83 | 4 | **1** | `cross_mean(div(day_sum(mul(mul(Ret, Ret), Ret)), mul(day_sum(pow_3(Volume)), day_sum(pow_3(Volume)))), 20)` +1.22 |

两个 N 位各入 1 个 head,「3 轮里至少 1 个 N 位通过审计」的约束在第 1 轮就满足了(两位都是 novelty 4 / soundness 3 与 4,一次过)。
a 位产出的是种子 8 `cross_mean(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 20)` 的后代;b 位产出的**不是**任何一个种子的后代,是 GP 把种子 6 的 `Σr²·sqrt(Σr²)` 分母换成 `(Σv³)²` 之后的东西(§1.2 第 3 点)。

### 3.3 审计员挡掉了什么、为什么

| 被挡 | 表达式 | 理由(原话压缩) |
|---|---|---|
| a 位种子 8(审计员划) | `cross_mean(mul(log(div(day_last(Close), ts_delay(day_last(Close), 1))), sub(log(day_sum(Amt)), cross_mean(log(day_sum(Amt)), 60))), 20)` | 用了**没有除以波动**的原始日收益,是有符号量、幅度 ∝ σ,两端十分位被高波动股占满,线性中性化去不掉 —— 陷阱 1 的路子(本位 vol \|ρ\| 最高 0.31) |
| a 位种子 6 / 9 / 12(相关度表划) | 见 r1 missions.yaml | 与 20 日反转控制 \|ρ\| 0.54 / 0.53 / 0.54 ≥ 0.5 |
| b 位种子 11(审计员划) | `cross_mean(div(day_max(Ret), day_std(Ret)), 20)` | 与 head 原始 \|ρ\| 0.55、残差 0.53;241 个分钟收益的 max/std 是极值 / 峰度不是偏度;对低价股主要读**最小价位**,是 head 的换皮 |
| b 位种子 10(审计员划) | `cross_mean(day_es_ratio_hi(in_logchg(Close, 1)), 20)` | 单侧尾厚不是不对称;流动性差、价格低的名字 95% 分位落在一跳上,**这个比值读的是价位网格和流动性**(size 0.31、liq 0.25 都是本位最高),接近陷阱 3 |
| b 位种子 14(相关度表划) | `cross_mean(div(sub(day_max(High), day_first(Open)), sub(day_max(High), day_min(Low))), 20)` | rev 0.54 |

两位的**不给 4 / 不给 5** 的理由也要带到本轮:
- a 位:CGW 的证据是放量日之后 1–2 天的条件反转,被 20–60 天平均稀释;LMSW 的交互项符号在股票间变号,支持的是**分类**不是单调排序;分钟尺度种子的 Amt 加权**大半是开收盘 U 形**;PI 估的 rev 0.2–0.4 实测是 0.45–0.54。
- b 位:彩票溢价主要在空头腿,纯多头只拿低偏度那一腿;A 股分钟收益受涨跌停截尾与最小价位离散影响,已实现偏度有一部分读的是**价格网格**。

**第 4 条(审计员对 R 的意见)**:它预先指出 `log(day_last(Close))` 与 `log(cross_mean(day_last(Close), 20))` 读的是**后复权价**而不是名义股价(残差 \|ρ\| 只有 0.30,而恒等式版是 0.87),并且与 head 原始 \|ρ\| 只有 0.07 < 0.5,**若高出 0.1 会走「收录」通道**,等于借 R 把一个与本 head 无关的长期累计收益量塞进库;又指出 `sub(LogTotalCap, LogFloatCap)` 不是去烂部件、原始 \|ρ\| 0.53 ≥ 0.5 会走替换通道。
R 组最终以合理度 3 通过、9 个变体全跑,**但 PI 没有按审计意见删掉 4、6、9,也没有保留 r1 analysis §4.2 里那两个最关键的变体**(见下)。

### 3.4 R 的替换与收录:**0 和 0**;而且三个判别变体被 PI 删了

`R_prev.json`:`replacements: []`、`additions: []`,9 个变体全部低于 head 的 +0.5001。

| 变体 | score | train | valid | rho_head | distinct |
|---|---|---|---|---|---|
| `LogFloatShares` | +0.4826 | +0.4826 | +0.7649 | 0.9991 | 0.9804 |
| `inv(LogFloatShares)` | +0.4777 | +0.4777 | +0.7699 | 0.9992 | 0.9804 |
| `cross_min(LogFloatShares, 20)` | +0.4801 | +0.4801 | +0.7736 | 0.9992 | 0.9796 |
| `cross_max(LogFloatShares, 20)` | +0.4760 | +0.4760 | +0.7513 | 0.9990 | 0.9804 |
| `sub(LogFloatCap, LogFloatShares)` | **−2.0523** | −0.2134 | −2.0523 | −0.8644 | **0.6869** |
| `cross_mean(sub(LogFloatCap, LogFloatShares), 20)` | **−2.0351** | −0.2380 | −2.0351 | −0.8646 | 0.9998 |
| `log(day_last(Close))` | **−1.1308** | −1.1308 | −0.2926 | 0.3317 | 0.9992 |
| `log(cross_mean(day_last(Close), 20))` | **−1.1873** | −1.1873 | −0.5836 | 0.3177 | 0.9998 |
| `sub(LogTotalCap, LogFloatCap)` | −0.1599 | −0.1599 | +1.0435 | 0.2293 | 0.7425 |

**这张表推翻了 r1 对这个 head 的主解释。** `steer.py` 第 638 行的 `for sign in (1.0, -1.0)` 是**按 train 的 long_sharpe 取较好的那个方向**,所以 `sub(LogFloatCap, LogFloatShares)` 的 train −0.2134 已经是**两个方向里较好**的那个:log 名义股价这条轴的**上下两端十分位在 train 上都不赚钱**。
而它与 head 的残差 |ρ| 是 0.87(r1 corr_1)。两件事合起来说明:head 的 +0.48 **不住在「股价水平」这条轴上**,而是住在 **`LogFloatShares` 残差的最高那一档**这个具体的十分位里;恒等式换写法之后十分位成员就变了(`distinct` 从 0.98 掉到 0.69,说明 `sub(LogFloatCap, LogFloatShares)` 有约 30% 并列,十分位切点落进并列块 ⇒ 成员又一次由列序决定,陷阱 §4.2 的另一种发作)。

**PI 删掉的三个变体正是判别用的:** r1 analysis §4.2 的第三组 `inv(pow_3(pow_3(pow_3(LogFloatCap))))`(管道假象)、`LogFloatCap`(地板校准)、以及第二组的 `LogTotalCap`(换同类字段 ⇒ 残留非线性规模曲率)**都没有进 missions_final.yaml**。
所以三个竞争解释里 **(a) 低名义股价被推翻、(b) 残留非线性规模曲率与 (c) 管道假象至今零证据**。而 `LogFloatShares` 与 size 控制的 |ρ| = **0.78** 让 (b) 成为先验上最可能的那个。
我把信念改成:**(b) 残留非线性规模 / 秩空间曲率 50%、(c) 管道 + 阈值噪声 30%、(a) 真的价格水平效应 20%**(r1 的 notebook 是 60 / 30 / 10)。

### 3.5 上一轮笔记里的预测,对不对

| # | 预测 | 结果 | 判 |
|---|---|---|---|
| 1 | R 的替换触发数 = 0(把握 75%) | `replacements: []`、`additions: []` | **对** |
| 2 | 裸 `LogFloatShares` 落在 +0.46 ~ +0.49 | +0.4826 | **对** |
| 3 | `sub(LogFloatCap, LogFloatShares)` 与 `log(day_last(Close))` 都 ≥ +0.40 且彼此 \|差\| < 0.1 | −2.05 / −1.13(train −0.21 / −1.13) | **错,而且错得最有信息量**(§3.4) |
| 4 | `inv(pow_3(pow_3(pow_3(LogFloatCap))))` ≥ +0.3(把握 55%) | **未检验**,PI 从 R 组删掉了 | **悬置** |
| 5 | `cross_min` 与 `cross_max(LogFloatShares, 20)` 分差 < 0.05(把握 65%) | 0.4801 vs 0.4760,分差 **0.0041** | **对** |
| 6 | E 位过线 0–2、`peripheries_seen` ≥ 6 | 没开 E 位 | 不适用 |
| 7 | 自由流通比例那条轴若当 N 位,过线 0–1 | 没当 N 位;R 探针 `sub(LogTotalCap, LogFloatCap)` train **−0.16** / valid +1.04 | **事后看,不花 N 位是对的** |
| a 位 | 产出 1–2 个 head(把握 50%);最可能是 `cross_corr(日收益, 成交额, 20)` 或 `day_corr(Ret, Amt)` 的 20 日均值;**方向 −1**;score 0.5–0.7 | 1 个 head ✓;score +0.61 ✓;但形式是 `(day_wmean − day_mean)/day_std` 这一支,**方向 +1**(延续,不是反转) | 数量与量级对,**机制方向错** |
| a 位相关度 | 13 个种子与 head 全部 \|ρ\| < 0.1 ✓;与反转控制 **0.2–0.4**;剩 ≥ 10 个 | head \|ρ\| 全 ≤ 0.08 ✓;rev **7 个落在 0.45–0.54**;实际剩 **9** 个 | 反转相关**显著低估**,剩余数差 1 |
| b 位 | 产出 ≥ 1 个 head(把握 35%);最可能是 RSJ 或 1 分钟已实现偏度的 20 日均值;方向 −1;score 0.5–0.6;剩 ≥ 10 | 1 个 head ✓(4 个过线);方向 −1 ✓;剩 11 ✓;但形式是 **Σr³/(Σv³)²**,score **+1.22** 远超 0.5–0.6,而且**不是偏度** | 数量与方向对,**形式与量级错** |
| b 位失败模式 | 「GP 可能沿着 \|收益\| 与成交量的方向长回波动 / 流动性因子」(写在 **a 位**名下) | **a 位没有,b 位正好这样**(§1.2) | 机制猜对了,位置猜错了 |

**三条要带进本轮的教训:**
1. **方向不要先验写死。** a 位把 CGW 的反转方向写进了假设,GP 交出来的是 sign +1 的延续。奖励自己会挑方向;PI 在假设里押方向只会在审计时被扣合理度。
2. **别低估与反转控制的相关。** 任何「日收益 × 成交」的 20 日平滑量,rev |ρ| 的实测中位数在 0.45–0.54 一带,不是 0.2–0.4。本轮凡是同类种子,PI 应当预设 **rev ≈ 0.5**,并把去反转那一步(除以自身滚动波动、或减掉自身滚动均值)**写进种子**而不是指望中性化。
3. **GP 会离开你指定的轴,爬向凸度。** b 位给的是尺度不变的偏度,交回来的是六次方的成交量。**N 位的种子必须把「不许在分母上堆成交量 / 波动的幂」写进假设的算子约束里**,否则这一位的产出会落在陷阱 §4.3 上。

---

## 4. 本轮候选

### 4.1 值得深挖的核心(3 个,按推荐度)

先说**不推荐**的,因为机械核心卡的前几名全在这里:

| 核心卡 | 表达式 | 为什么不要 |
|---|---|---|
| 1、16 | `div(day_sum(mul(mul(Ret, Ret), Ret)), mul(day_sum(pow_3(Volume)), day_sum(pow_3(Volume))))`、`mul(day_sum(pow_3(Volume)), sqrt(day_sum(mul(in_logchg(Close, 1), Ret))))` | §1.2:分母是已知族(rho_known 0.52 / 0.58),分数由凸度提供,coverage 0.9228。**B0 取的就是第 1 名** —— PI 必须写下为什么 C 组不取 |
| 3 | `day_sum(pow_3(Volume))` | rho_known **+0.5805 ≥ 0.5**,E 位的「核心与每个控制 \|ρ\| < 0.5」**直接不过** |
| 2、7、17、18、19、21 | 全部含 `cs_state_rank(…)` 或 `cs_last_high10(cs_state_rank(…), …)` | §1.1:列序斜坡。E 位在它外面长出来的任何东西都在给一条按代码排的静态组合加装饰,合理度必是 1(陷阱 §4.2) |
| 4–12 | `pow_*(LogFloatShares)` 全族 | size \|ρ\| = **0.78**(corr_1 实测),E 位必被判「控制换个写法」;且陷阱 §4.3 |
| 20、28 | `day_es_ratio_hi(Vwap)`、`day_es_ratio_hi(High)` | r1 审计员**已经**用同一个理由划掉了 `day_es_ratio_hi(in_logchg(Close, 1))`:「流动性差、价格低的名字 95% 分位落在一跳上,这个比值读的是价位网格和流动性」。对价格字段同样成立(日内 Vwap 的上尾宽度 ≈ 日内波幅 / 最小价位),大概率被判陷阱 3。**我原本想推它,看完 r1 审计记录后收回** |

**核心 A(首选):`div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret))`** —— 核心卡 15,共性 +1.24 / p 0.003 / 8 个候选

- 它是 §1.3 那个 head 的**日度内核**,量纲已去掉,每个部件必要性都 > 0,字段敏感性(Amt↔Volume)只差 0.01。
- 用**未平滑**的日度版本当核心(而不是核心卡 13 的 `cross_ema(…, 10)`)有两个理由:(i) 拆解说 alpha 在时间聚合层,把这一层留给 GP 才有东西可长;(ii) 核心与控制的 |ρ| 是在核心本体上算的,日度未平滑版比 20 日平滑版(rev 0.49)**离 0.5 的门远得多**。
- **它周围已经见过的外围(全部是纯时间平滑,`{cross_mean, cross_ema}` 的组合)**:
  - `cross_mean(X, 20)`(r1 a 位种子 8)
  - `cross_ema(X, 10)`、`cross_ema(X, 15)`(a 位过线名单第 3、5)
  - `cross_mean(cross_ema(X, 10), 15)`(= head)、`cross_mean(cross_ema(X, 10), 7)`、`cross_mean(cross_ema(X, 10), 30)`(定位窗口变体)
  - `cross_ema(cross_mean(cross_ema(X, 10), 15), 10)`(a 位过线名单第 2)
  - 旁系(核心不同但同一机制):`cross_mean(div(cross_ema(day_corr(Ret, Amt), 10), day_std(Ret)), 15)` +0.44
  → **外围算子集合见过的只有 `{cross_mean}`、`{cross_ema}`、`{cross_mean, cross_ema}` 三种。** 想拿到创新度 ≥ 3,本轮的外围必须**离开时间平滑族**:
    (i) **相对自身历史**:`div(X, cross_stddev(X, 120))`、`sub(X, cross_mean(X, 120))` —— 把「水平」变成「异常」(GKM 口径,正是 r1 审计员说种子没做到的那一点);
    (ii) **分段条件化**:`cs_bucket_rank(cross_mean(X, 15), cross_mean(day_sum(Amt), 30))` —— 在流动性十分位内部排序(`cs_bucket_rank` 的文档说它比线性秩残差在尾部更干净),检验 LMSW 的「符号在股票间变号」而不是单调排序;
    (iii) **市场状态加权**:用 `cs_state_rank(day_sum(Amt), 60)` 当 **`add(mul(s, a), mul(sub(1, s), b))` 里的权重**(ops_ext 文档明确说这是它的正当用法),**绝不可以**把它塞进 `cs_*` 的参数位(那就是陷阱 §4.2);
    (iv) **上下行拆开**:把 `sub(day_wmean(Ret, Amt), day_mean(Ret))` 的正负两半分别平滑再相减(是不是只有「钱在跌的分钟进场」那一侧有信息)。
- 风险:rev |ρ| 是这条轴的制度性上限,平滑越长越贴 0.5。外围里任何「加长平滑」的方向都要预期被相关度表划掉。
- 这个核心本实验还没用过 E 位(上限 2 个)。

**核心 B(次选):`day_corr(Ret, Amt)`** —— 核心卡 25(共性 +0.67 / p 0.100 / 16 个候选);或它的平滑版核心卡 22 `cross_ema(day_corr(Ret, Amt), 10)`(+0.85 / p 0.083 / 10 个)

- 同一条经济轴(日内量价交互)的**另一个函数形式**:相关系数而不是加权均值之差。它对成交额的分布形状不敏感,是检验 §1.3 那条「U 形 vs 资金流」竞争解释的**结构性对照**。
- 已见外围:`cross_ema(·, 10)`、`cross_mean(·, 20)`(r1 a 位种子 7、9,后者被相关度表按 rev 0.53 划掉)、`cross_mean(div(cross_ema(·, 10), day_std(Ret)), 15)`(a 位过线名单第 4,+0.44)。→ 见过的是 `{cross_ema}`、`{cross_mean}`、`{cross_mean, div, day_std, cross_ema}`。
- p 值 0.083 / 0.100 都不显著,共性证据比核心 A 弱一档;而且与核心 A 在同一条轴上,两个 E 位都押这里会把本轮的多样性花光。**建议只在 PI 想开两个 E 位时用它当第二个。**

**核心 C(高风险高回报):`log(day_first(Open))`** —— 核心卡 23,共性 +0.72 / **p 0.000** / **53 个候选**(与 `day_first(Open)` 的 57 个并列为全表支持面最广的两行)

- 它是 §1.1 里 head +1.53 **唯一活着的经济输入**。价格字段是**后复权**的(r1 审计员据 `tradability.py` / `label.py` / `daily.py` 指出),所以它的含义不是名义股价,而是 **log(IPO 价 × 上市以来累计总收益)** —— 一条**超长期累计动量 / 存活质量**轴。5 个控制里只有 20 日点对点反转,**没有任何多年尺度的累计收益控制**,这条轴在环境里是合法的新信息。
- 已见外围:`cs_last_high10(cs_state_rank(…), log(day_first(Open)))` 及其上面那一整套 `cross_corr` / `cs_first_high40` 组合(即两个 artifact head,外围 = `{cs_last_high10, cs_state_rank, day_es_ratio_hi, cross_corr, inv, cs_first_high40}`);`cs_last_high10(cs_state_rank(log(day_first(Open)), 50), log(day_first(Open)))`(核心卡 7);`cs_state_rank(log(day_first(Open)), 50)`(核心卡 14);裸 `log` / `day_first`。
  → **见过的外围全部是 `cs_*` 列序斜坡那一族。** 任何不含 `cs_state_rank` 的外围都是未见过的,创新度上比较容易说清。
- **两个必须当面讲清的风险:**
  1. **E 核心与控制的门槛。** r1 corr_1 里 `log(day_last(Close))` 的 liq = **0.46**、size = 0.42、known = 0.42。`log(day_first(Open))` 大概同量级。**0.46 离 0.5 只有 4 个点**,相关度表完全可能把这个 E 位直接判死。PI 若要用,应当做好「核心被控制卡掉、这一位退成普通 GP」的准备。
  2. **它自己不是因子。** r1 的 R 测过 `log(day_last(Close))` = −1.13、`log(cross_mean(day_last(Close), 20))` = −1.19(都是两个方向里较好的那个)。E 位不要求核心自己得分,但 PI 要在假设里写明「我们买的是外围,不是这条水平线」,否则合理度会被按「数字游戏」处理。
- 如果相关度表放过它,这是本轮**唯一一个既有最广共性支持、又有一条文献上成熟机制、又完全没有被非 `cs_*` 外围探索过**的核心。

### 4.2 R 目标(15 个,≤ 16;按价值排序)

全部挂在快照 head 上,全部是「去掉或替换部件」。**第一组是本轮最值得花的两次评估。**

**第一组 —— 把列序斜坡的地板买下来(挂 head +1.53,2 次)**

| # | 变体 | 要证明什么 | 预期 |
|---|---|---|---|
| R6b | `cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), cs_state_rank(day_es_ratio_hi(High), 50))` | **纯列序斜坡**(band 永不触发,见 §1.1 的玩具运行)在 `long_neutral` 下的净夏普 = **artifact 地板分** | 我给「≥ +0.5」**50%** 的把握。coverage 0.9993、distinct 1.0 有保证 |
| R6a | `cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))` | 斜坡 **+ 后复权价最高十分位标记**。R6a − R6b = **那个标记单独值多少** | +0.2 ~ +0.8;若 R6a ≫ R6b,核心 C 的 E 位就有了 train 证据 |

**这两次的风险必须写进计划并让审计员看见**:若 R6a / R6b 的 score ≥ head +1.53 + 0.1 = **+1.63**,它们会被 R 通道**装进库**。与 head +1.53 的 ρ ≥ 0.5 时走「替换」(用一条写得更诚实的列序因子顶掉一条写得很绕的列序因子,库里 head 数不增);ρ < 0.5 且与所有 head |ρ| < 0.7 时走「**收录**」,库里会多出一条**纯列序**的 head。
我认为这个风险值得承担:它要么不触发(大概率),要么触发 —— 而「这个奖励可以被股票列序刷到 1.6 以上的净夏普」本身就是整个实验最重要的一条发现,PI 必须把它写进报告并上报。挂在 +1.53 而不是 +0.75 上就是为了把替换门槛顶到最高。

**第二组 —— 证死两个 artifact head(4 次)**

| # | 挂 | 变体 | 预期 |
|---|---|---|---|
| R1 | +0.75 | 见下方原文(把 `cs_state_rank(day_es_ratio_hi(Vwap), 50)` 换成 `cs_state_rank(day_sum(Volume), 50)`) | **位等同 +0.7493**。把握 90% |
| R4 | +1.53 | 见下方原文(只把 `cs_state_rank(day_es_ratio_hi(High), 50)` 换成 `day_es_ratio_hi(High)`,其余一字不改) | 分数**大幅变化**(我押下降到 < +0.6)。这是最干净的一次:经济内容没变,只是让 y 真的进截面 |
| R3 | +0.75 | 见下方原文(两层 `cs_state_rank` 全去) | 塌到 ±0.3 以内 |
| R5 | +1.53 | 见下方原文(把 `log(day_first(Open))` 换成 `day_pos_ratio(Volume)`) | 若仍 ≥ +1.2,连那个价格标记都不是来源,整个 head 100% 是列序 |

(R2 —— 把 head +0.75 的 x 换成 `log(day_first(Open))` 让 band 有机会触发 —— 可留作备选,它和 R3 的信息重叠。)

**第三组 —— head +1.22 的凸度剂量反应(4 次)**

分子固定为 `day_sum(mul(mul(Ret, Ret), Ret))`、外层固定 `cross_mean(·, 20)`,只换分母的幂:

| # | 分母 | 变体原文 |
|---|---|---|
| R7 | 线性成交量 | `cross_mean(div(day_sum(mul(mul(Ret, Ret), Ret)), mul(day_sum(Volume), day_sum(Volume))), 20)` |
| R8 | 1.5 次 | `cross_mean(div(day_sum(mul(mul(Ret, Ret), Ret)), mul(day_sum(pow_1_5(Volume)), day_sum(pow_1_5(Volume)))), 20)` |
| R9 | 2.5 次 | `cross_mean(div(day_sum(mul(mul(Ret, Ret), Ret)), mul(day_sum(pow_2_5(Volume)), day_sum(pow_2_5(Volume)))), 20)` |
| R10 | 换成**已实现方差**(ACJV 的正确归一化,同样的平方形状) | `cross_mean(div(day_sum(mul(mul(Ret, Ret), Ret)), mul(day_sum(mul(Ret, Ret)), day_sum(mul(Ret, Ret)))), 20)` |

R7 → R8 → R9 → head(3 次)是一条 **1 / 1.5 / 2.5 / 3 的凸度剂量阶梯**;R10 把「凸」这件事保留、把「对成交量凸」换成「对波动凸」。
- 若 score 随幂单调上升 ⇒ 规则 §4.1 / §4.3 的凸度漏洞确认,head +1.22 应当在笔记里标成 artifact,**不要**在它上面开 E 位。
- 若 R10 ≈ head ⇒ 来源是「凸归一化」这件事本身,与成交量无关;若 R10 ≪ head ⇒ 来源是成交量(已知族)。
- `pow_1_5` / `pow_2_5` 走 `common.py::pow_` 的 `e > 1` 分支(`torch.pow(x, e)`),Volume ≥ 0 没有符号问题;幂降低也顺手避开了 (Σv³)² 的 float32 溢出(head 自己的 coverage 只有 0.9228)。

**第四组 —— head +0.61:资金流,还是开收盘 U 形?(5 次)**

这一组买的是 §1.3 最后一条、r1 审计员提出的竞争解释。关键是 `in_index(x)`(`ops_ext.py` 第 684 行):它返回分钟在当日的位置 `t/(T-1)`,**只在 x 有值的分钟上有定义**,所以它是一条**几乎不含个股信息的时间斜坡**。

| # | 变体原文 | 要证明什么 |
|---|---|---|
| R14 | `cross_mean(cross_ema(div(sub(day_wmean(Ret, in_index(Amt)), day_mean(Ret)), day_std(Ret)), 10), 15)` | 把成交额权重换成**纯时间权重**(晚盘加权)。若它复现 ≈ +0.6,这个 head 读的是**时段构成**,不是资金流 |
| R15 | `cross_mean(cross_ema(div(sub(day_wmean(Ret, Amt), day_wmean(Ret, in_index(Amt))), day_std(Ret)), 10), 15)` | 用**时间加权均值**代替等权均值当基准,把 U 形按构造扣掉。若 score 保住或变好 ⇒ 真的是资金流;若塌 ⇒ U 形 |
| R11 | `cross_mean(cross_ema(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 5), 7)` | 定位已给出 `@15->7` = +0.6526;再把 EMA 也减半,看两个小改动叠起来能不能过 +0.1 |
| R12 | `cross_mean(cross_ema(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_wstd(Ret, Amt)), 10), 15)` | 去量纲用**资金加权波动**而不是等权波动(定位的 SWAP 表不含这种同类算子替换) |
| R13 | `cross_mean(cross_ema(div(sub(day_topw_mean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 10), 15)` | 换成**最重 10% 分钟**的平均收益(GKM 口径)。注意 r1 的 `cross_mean(·, 20)` 版本被相关度表按 **rev 0.54** 划掉过,这一支有被划的风险,PI 要有心理准备 |

**第一、二组的变体原文(机械替换生成,逐字可用):**

```
R1  (挂 head +0.75)
cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_sum(Volume), 50), log(cs_state_rank(day_es_ratio_hi(High), 50)))), cs_last_high10(cs_state_rank(day_sum(Volume), 50), log(cs_state_rank(day_es_ratio_hi(High), 50))), 241), cs_last_high10(cs_state_rank(day_sum(Volume), 50), log(cs_state_rank(day_es_ratio_hi(High), 50))))

R2  (挂 head +0.75,备选)
cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(day_first(Open))))

R3  (挂 head +0.75)
cs_first_high40(cross_corr(inv(cs_last_high10(day_es_ratio_hi(Vwap), log(day_first(Open)))), cs_last_high10(day_es_ratio_hi(Vwap), log(day_first(Open))), 241), cs_last_high10(day_es_ratio_hi(Vwap), log(day_first(Open))))

R4  (挂 head +1.53)
cs_first_high40(cross_corr(inv(cs_last_high10(day_es_ratio_hi(High), log(day_first(Open)))), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(day_es_ratio_hi(High), log(day_first(Open)))), cs_last_high10(day_es_ratio_hi(High), log(day_first(Open))), 241), cs_last_high10(day_es_ratio_hi(High), log(day_first(Open)))), log(day_first(Open))), 241), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(day_es_ratio_hi(High), log(day_first(Open)))), cs_last_high10(day_es_ratio_hi(High), log(day_first(Open))), 241), cs_last_high10(day_es_ratio_hi(High), log(day_first(Open)))), log(day_first(Open))))

R5  (挂 head +1.53)
cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), day_pos_ratio(Volume))), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), day_pos_ratio(Volume))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), day_pos_ratio(Volume)), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), day_pos_ratio(Volume))), day_pos_ratio(Volume)), 241), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), day_pos_ratio(Volume))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), day_pos_ratio(Volume)), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), day_pos_ratio(Volume))), day_pos_ratio(Volume)))
```

### 4.3 N 的灵感(按我的偏好)

库里现有的轴:浮股 / 规模水平线、列序斜坡(×2,artifact)、日内三阶矩 ÷ 成交量凸度、日内资金流倾斜。**完全没有碰过的是「时间」这个维度** —— 既没有隔夜 / 盘中的切分,也没有日内时段的切分。两条灵感都在这里。

**1(首选)隔夜 vs 盘中收益的切分。** 同一段 20 日收益,拆成「隔夜那部分」和「盘中那部分」。
- 算子:隔夜 = `div(day_first(Open), ts_delay(day_last(Close), 1))`;盘中 = `div(day_last(Close), day_first(Open))`;再 `log`、`cross_mean(·, 20/60)`,或两者之差 / 比。
- 为什么正交:5 个控制里的反转是 `div(day_last(Close), ts_delay(day_last(Close), 20))`,是**两段之和**;和与差正交,线性中性化扣掉的只是和。这是**按构造**的正交,不是估计出来的 —— 合理度上很好说。
- 为什么样本外还在:A 股 **T+1** 与开盘集合竞价的制度,把散户的隔夜决策与机构的盘中执行机械地分开,这个制度在样本期后没变。文献面也足(见 §5 题 3)。
- 方向交给奖励(§3.5 教训 1),不要在假设里押。
- 预防:不要用 `day_first(Open)` 的**水平**(那是核心 C 的轴,而且后复权),只用**比值**。

**2(次选)日内成交的时点。** 「钱是在一天的什么时候成交的」这个纯形状量。
- 算子:`day_wmean(in_index(Amt), Amt)`(成交额加权的平均时点,∈[0,1])、`day_corr(in_index(Volume), Volume)`(成交是不是后置 —— `ops_ext.py` 第 684 行的文档就举了这个例子)、尾盘集中度 `day_topw_mean(in_index(Amt), Amt)`。
- 为什么新:库里和 5 个控制里**没有任何时点信息**;它是 [0,1] 的形状量,与成交额水平、波动、市值都没有机械关系(**不是**它们的凸变换,避开陷阱 1、3);不含 `cs_*`(避开陷阱 2)。
- 为什么可能有信号:尾盘资金占比是机构 / 指数资金的痕迹,开盘占比是散户隔夜决策的痕迹;它也直接检验 §1.3 那条 U 形竞争解释。
- 风险:时点分布与流动性分层相关(大盘股尾盘占比高),liq |ρ| 可能到 0.3–0.4;要在种子里做**相对自身 60 日均值的偏离**来降相关。

**3(备选)按涨跌停幅度缩放的收益。** r1 §4.3 的第 2 条灵感,`LimitWidth` 至今未用,r1/lit.md 题 4 已经把文献做完了(现成的合理度 4 证据)。例如 `cross_mean(div(log(div(day_last(Close), ts_delay(day_last(Close), 1))), LimitWidth), 20)`、触板距离 `div(sub(LimitWidth, abs(日收益)), LimitWidth)`。
注意 `LimitWidth` 逐股恒定且只有 3–4 个取值,单用过不了 `distinct` 门,只能当除数 / 分组变量。

**4(不建议本轮用)自由流通比例。** `sub(LogTotalCap, LogFloatCap)` 的 R 探针 train **−0.16**;这条轴在 train 上是死的(§3.5 第 7 行)。

---

## 5. 文献题目(给文献员,4 个)

共同约束:**只用 2023-08-08 之前发表 / 公开的文献**,逐条注明年份与出处;重点不是「这个因子有没有用」,而是**文献对类似结构 / 特征做过哪些处理**(归一化、分组、交互、换周期、换股票池),以及**样本外 / 跨市场是否复现**。

**题目 1(对准核心 A:日内资金流倾斜 =(成交额加权分钟收益 − 等权分钟收益)/ 日内波动)**
文献里怎样把「日内订单流 / 资金流失衡」做成截面预测变量?具体问:(a) 归一化用什么分母 —— 日内波动、成交额、分钟数,还是不归一化?(b) 平滑多少天,信号的预测期是几天还是一个月以上,**衰减曲线**长什么样?(c) 符号:做多持续净买压(延续)还是做空(反转)?在什么条件下变号(LMSW 的信息交易 vs 流动性交易分类)?(d) 有没有**按流动性 / 规模 / 散户占比分组**后符号不同的证据?(e) 有没有文献指出这类「成交额加权收益 − 等权收益」的截面差异主要来自**日内 U 形时段构成**(开盘 / 尾盘段收益与盘中段收益之差),以及用什么办法把时段效应扣掉?(f) A 股(T+1、无做空、散户主导)上的复现与美股差异。
中文关键词:日内资金流、资金流向、主动买卖、净买入压力、成交额加权收益、量价失衡、订单流失衡、日内 U 形、尾盘资金、机构资金流
英文关键词:intraday order flow imbalance, money flow, trade imbalance, volume-weighted intraday return, buy-sell imbalance, VWAP tilt, intraday U-shape of volume, Lee-Ready, PIN, retail order imbalance, China A-share order imbalance

**题目 2(对准 head +1.22 的 R 组:高阶矩的分母该放什么)**
已实现偏度 / 相对符号跳跃这一族,文献用的**归一化分母**是什么,换成别的会怎样?具体问:(a) ACJV 2015 的 `sqrt(N)·Σr³/RV^1.5`、BLZ 2020 的 `(RV⁺−RV⁻)/RV` 之外,有没有文献用**成交量 / 成交额的幂**当分母?如果有,给出处;如果没有,也要明确说「没有」。(b) 有没有文献专门指出「把一个高阶矩除以成交量的幂」得到的截面排序**实际上是流动性 / 成交集中度的非线性暴露**,以及用什么诊断(分组、双重排序、对成交量的样条中性化)把两者分开?(c) 已实现偏度与**成交量集中度 / 大单占比**的截面相关有多高,文献报过吗?(d) 分钟收益的**最小价位离散与涨跌停截尾**对已实现偏度的偏误,文献怎样修正(过滤零收益分钟、改用 5 分钟、改用价差中点)?
中文关键词:已实现偏度、相对符号跳跃、上行下行已实现方差、高阶矩归一化、成交量集中度、大单占比、非线性流动性暴露、双重排序、最小价位、涨跌停截尾
英文关键词:realized skewness normalization, relative signed jump variation, upside downside realized variance, higher-moment scaling, volume concentration, order size concentration, nonlinear liquidity exposure, double sorting, tick size discreteness, price limit truncation

**题目 3(对准 N 灵感 1:隔夜 vs 盘中切分)**
把同一段持有期收益拆成**隔夜段**与**盘中段**,文献做过哪些处理?具体问:(a) 两段的截面预测符号是否相反,各自的预测期多长(日、周、月)?(b) 用**水平**(各段平均收益)还是**占比 / 之差**?窗口多长?(c) 有没有「隔夜段代表散户 / 情绪、盘中段代表机构」的证据与检验方式?(d) 这个切分与常规 1 个月反转、与动量的关系 —— 是不是其中一段才带着反转?(e) **A 股的 T+1 与集合竞价**制度下的专门研究,以及开盘集合竞价收益是否要单独剔除?(f) 用后复权价算隔夜收益时的除权日处理。
中文关键词:隔夜收益、隔夜效应、盘中收益、日内收益、收益分解、开盘集合竞价、T+1、隔夜与日内反转、散户隔夜交易
英文关键词:overnight returns, intraday returns, overnight versus intraday, return decomposition, tug of war, close-to-open return, open-to-close return, opening auction, overnight return reversal, T+1 constraint China

**题目 4(对准 N 灵感 2:日内成交的时点)**
「一天里成交发生的时点」作为截面特征,文献里有哪些度量与处理?具体问:(a) 度量方式 —— 成交量加权平均时点、尾盘(最后 15 / 30 分钟或收盘集合竞价)成交占比、开盘占比、日内成交的偏度 / 重心?(b) 怎样**去掉日内周期性与市场共同成分**(Heston-Korajczyk-Sadka 一类的日内周期性处理、相对自身近期均值的去趋势)?(c) 它与规模 / 流动性 / 指数成分资格的机械相关有多强,文献怎样中性化?(d) 它预测的是**收益**还是**波动 / 流动性**?有没有「尾盘成交占比高 = 机构 / 被动资金痕迹」的截面收益证据?(e) 收盘集合竞价占比上升这个长期趋势会不会让这个特征的分布随时间漂移(对样本外稳定性的影响)。
中文关键词:日内成交分布、尾盘成交占比、收盘集合竞价、开盘成交占比、日内周期性、成交量重心、被动资金、指数调仓
英文关键词:intraday volume distribution, closing auction volume share, close-of-day trading, intraday periodicity in volume, volume-weighted average time, volume timing, passive flows, index rebalancing, U-shaped intraday volume

---

## 6. 写给下一轮核对的预测

1. **R6b(纯列序斜坡)的 score ≥ +0.5 的把握 50%;≥ +0.75 的把握 25%;≥ +1.63(会被装进库)的把握 8%。** 若 ≥ +0.5,库里 2 个 head 全部被解释完,并且这是整个实验级别的发现。
2. **R6a − R6b ≥ +0.2 的把握 60%**(后复权价最高十分位那个标记真的带信息)。若成立,核心 C 的 E 位有了 train 证据;若 R6a ≈ R6b,核心 C 不值得开。
3. **R1 与 head +0.75 的 score 在四位小数上相同,把握 90%。**
4. **R4 的 score < +0.6 的把握 70%**(把 y 从每日常数换成同一个量的个股版本就会毁掉 head +1.53)。若 R4 反而 ≥ +1.4,我的 §1.1 判断错了,必须在下一轮笔记里撤回。
5. **第三组凸度阶梯单调上升(R7 < R8 < R9 < head +1.22)的把握 55%**;「R7(线性成交量)≤ +0.6」的把握 65%;**R10(ACJV 正确归一化)≤ +0.7 的把握 70%** —— 即 head +1.22 的分数主要由成交量凸度买来。
6. **第四组:R15 ≥ +0.5 的把握 55%**(资金流倾斜在扣掉时段构成之后还活着);**R14(纯时间权重)≥ +0.4 的把握 40%**。若 R14 ≥ R15,head +0.61 应改读成时段构成效应,核心 A 的 E 位要重写假设。
7. **R 组触发替换或收录的总数 = 0 的把握 60%**(比 r1 的 75% 低,因为第一组有真实的上行风险)。
8. 若本轮开 E 位在核心 A 上:**过线 head 0–2 个**;并且凡是外围只做「更长的时间平滑」的候选,会被相关度表按 rev ≥ 0.5 大量划掉 —— **我预测 PI 提交的种子里有 1/4 到 1/3 会因为 rev 被划**。
9. 若开 E 位在核心 C(`log(day_first(Open))`)上:**核心自己因为 liq |ρ| ≥ 0.5 被判死、这一位退成普通 GP 的把握 35%**。
10. **M 第 3 批里还会出现至少一个含 `cs_state_rank(…)` 的 head,把握 55%** —— 库禁令比的是面板的秩和算子骨架,而列序斜坡可以用任意多个不同的 `cs_*` 骨架和任意多个被丢弃的字段写出来,每一种都是「新」骨架。如果这条成立,PI 应当在报告里把它作为**环境层面的建议**提出来(例如要求 `cs_*` 的参数位拒绝截面常数)。
