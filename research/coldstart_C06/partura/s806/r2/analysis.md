# 结构解剖:种子 806,C 组,第 2 轮

快照:`c05s806M1_I0_open_search`、`c05s806M2_I0_open_search`、`c06s806Cr1a_Ea`、`c06s806Cr1b_Nb`;8 个 head 全部来自 M 第 2 批,R 替换 0 个。
证据来源:`r2/loc.md` / `r2/loc.json`(292 个归档候选的共性、28 次付费拆解)、`r1/` 的 `missions_final.yaml` / `audit_1.yaml` / `audit_record.json` / `corr_1.md`、`notebook.md`,以及算子源码。

---

## 0. 一句话结论

**M 第 2 批的 8 个 head 不是 8 个来源,是 3 个族,而且 3 个族里有 2 个半是「线性中性化挡不住的水平 / 风格暴露」,不是日内信息。**
唯一有资格被叫做「可能的真来源」的是 `day_centroid(Amt)`(当日成交额在分钟轴上的重心)这一族;但它起作用的是**持久水平**,不是日度新息,而且随平滑窗口变长它与已知族的 |ρ| 单调升到 0.56(40 日那版按奖励口径已经不合格)。
本轮两个位应该全部押在「把这个持久水平拿掉之后还剩什么」上,并事先写下判决;库里已经有 5 个 head 压在同一个低价 / 小市值的非线性暴露上,再加同向的东西对最终样本外没有价值。

---

## 1. 先确立三条代码事实(后面所有判断都建在这上面)

这三条都是从源码读出来的,不是推测;它们解释了拆解表里几乎所有「看不懂」的数字。

**(1) 奖励的真实流程是:表达式 → EMA 平滑(半衰期网格) → 截面秩(z-rank) → 对 5 个控制取残差 → 残差的前 10% 等权纯多头。**
`partura/steer.py:636` 先 `bk.smoothed(raw, hl)` 再 `neutral_residual(...)`;`neutral_residual`(同文件 424 行)第一步就是 `dg._zrank`,而 `_zrank` 用 `rank_rows`(**并列取平均秩**,`diagnose.py:64`);`books.py` 里 `TOP_FRAC = 0.10`、`COST = 0.0015`。方向与半衰期都是在 **train 上**挑最好的,再去 valid 评。

**(2) `_lexi` 家族(`cs_first_low*` / `cs_last_low*` / `cs_first_high*` / `cs_last_high*`)只用两个参数的秩。**
`partura/ops_ext.py` 的 `_lexi(y, x, lo, hi, shift)`:`ry = _pct_rank(y)`(在 (0,1] 上的序号秩),`band` = x 的**整个并列块**落在分位带内的股票,输出 `rank(y) + shift·band`。
所以 `cs_last_low40(A, B)` = 「按 A 的秩排,把 B 最低 40% 的股票整体减 1」;`cs_first_low20(A, B)` = 「按 A 的秩排,把 B 最低 20% 的股票整体加 1」。
推论:**套在 `_lexi` 两个参数上的任何单调变换都是死算子**。这正是拆解表里 `log(day_open(Open))` 必要性 −0.00、`cs_normalize(day_open(Open))` 必要性 −0.00、`Open->Close` 与 `Amt->Volume` 互换几乎不动分的原因 —— 不是「稳健」,是**那一处根本没进计算**。

**(3) 一个「平坦块」+ 线性中性化 = 做多控制变量的极端一端。**
设信号在一组股票 B 上取同一个值(`cs_mask_top_replace_mean_neg` 正好造出这种块,`_lexi` 的整体加减 1 造出成段台阶)。平均秩之后 B 内所有股票拿到同一个 z-rank 值 c;残差 r_i = c − (控制拟合值)_i。于是 **B 内部的残差排序恰好是控制拟合值的反序**:如果这个块落在 z-rank 的高位,多头十分位就从 B 里挑「控制拟合值最低」的那些,也就是最小市值 / 最不流动的那一批。
这是规则 §4 陷阱 3 的离散形式,比凸变换更隐蔽:信号与每个控制的**线性** |ρ| 可以都很低,因为信息全在「块」这个非线性结构里。
`cs_mask_top_replace_mean_neg` 的 `top_ratio` 默认 **0.1**(`nd_cs.py:209`),与多头十分位的 `TOP_FRAC = 0.10` 一样大 —— 一个块正好装满一本多头书。

---

## 2. alpha 的来源:逐族取证

### 族 I(head 1、head 6)真来源 = `sqrt` 的绝对值造出来的「市值 V 形」。判定:**代理**

```
+1.78  sqrt(cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile_q75(Amt)), 3))
+1.13  sqrt(cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile(Low)), 3))
```

- **结构**:`sqrt(x) = sqrt(|x|)`(`common.py:199`)。`cs_last_low40(LogFloatCap, ·)` 的取值是 `r − 1·band`,`r = rank(LogFloatCap) ∈ (0,1]`。于是
  - 不在带内(成交额高的 60%):`sqrt(r)`,**随市值递增**;
  - 在带内(成交额最低的 40%):`sqrt(1−r)`,**随市值递减**。
  一个以市值秩为自变量的 V 形,折点由流动性决定。多头取残差前 10%,落在 V 的两端:**最小市值的那几个百分位 + 最大市值的那几个百分位**(粗算各约 5%)。排序键 `LogFloatCap` **就是 size 控制本身**;线性中性化只去掉一次项,V 形的二次部分原样留下 —— 规则 §4 陷阱 3 的教科书写法。
- **充分性(付费)**:`cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile_q75(Amt)), 3)` 单独 **−2.08**(train −0.49 / valid −2.08);`cs_last_low40(LogFloatCap, day_quantile_q75(Amt))` 单独 **−2.08**(train −0.30 / valid −2.08)。
- **必要性(付费)**:去掉 `cs_last_low40` → `sqrt(cross_quantile_q25(LogFloatCap, 3))` = **−3.01**,必要性 **+4.80**。
- **决定性的一条**:head 与「head 去掉根上的 `sqrt`」之间**只差一个绝对值**,方向与半衰期相同(sign +1、hl 20),分数从 **+1.78 掉到 −2.08**(train +2.05 → −0.49,valid +1.78 → −2.08)。另一对 `sqrt(cs_last_low40(…)) = +2.11` 对 `cs_last_low40(…) = −2.08` 又独立重复了一次(摆动 +4.2)。
  **这一族的全部 alpha 是 `|·|` 造出来的,不来自任何字段、任何窗口。**
- **敏感性**:`Amt->Volume` → **−0.03**(train +1.33 / valid −0.03):同类字段互换把 valid 腿整条打掉 1.8。窗口 `cross_quantile_q25@3->2` +1.92、`->6` +1.09。带的键换成 `day_quantile(Low)`(价格水平)就是 head 6(1.13)—— 带的键在「成交额水平 / 价格水平」之间可换,在「成交额 / 成交股数」之间不可换。说明有效的是「把截面劈成持久的两段」,具体劈法是拟合出来的。
- **共性**:`cs_last_low40(LogFloatCap, day_quantile(Vwap))` 均值差 +1.36(p 0.009,n 5)、`cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile(Vwap)), 3)` +1.21(p 0.026,n 4)。n 只有 4–5 个,且都是 M2 同一条血统的后代,p 不是独立证据。
- **顺带**:head 1 与 head 6 只差带的键,M 自己的去重(日度秩 ρ ≥ 0.7)没挡住它们 —— 0.7 这个门槛挡不住同族。

### 族 II(head 2、head 3、head 8)真来源 = 价格水平的**非单调带选择**:「便宜,但不是最便宜」。判定:**不是信息,是没被控制的风格**

```
+1.40  cs_first_low20(day_quantile_q75(Amt), log(day_open(Open)))
+1.32  cs_first_low20(cs_normalize(day_open(Open)), cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Close))))
+0.81  cs_first_low20(cs_normalize(day_open(Open)), cs_normalize(day_open(Open)))
```

按事实 (2) 逐个展开(`day_open` = 当日第一个有效分钟值,即开盘价;`pow_2_5` 对正数单调,分位数与单调变换可交换,所以 `day_quantile_q75(pow_2_5(Close))` 的秩 **等于** `day_quantile_q75(Close)` 的秩):

- **head 8**:y 与 x 是**同一个表达式**。输出 = `rank(价格) + 1{价格最低 20%}`,多头十分位 = 价格分位 (10%, 20%] —— 一个**静态的价格第 2 十分位组合**,x 这个参数位没携带任何额外信息。
- **head 3**:x = 把价格最低 10% 整体搬到截面均值(事实 3)之后再取最低 20% 的带 → 带 = 原始价格分位 (10%, 30%];y = 价格秩 → 多头十分位 ≈ 价格分位 (20%, 30%]。**`cs_mask_top_replace_mean_neg` 在这里的作用就是把最便宜的 10% 踢出带外。**
- **head 2**:带 = 价格最低 20%,排序键 = 当日成交额 q75 → 多头 = 低价股里成交额较高的那一半。同样把低价股里最不流动的那部分挤出多头。
- **三个 head 合起来的含义**:**做多便宜但不是最便宜、且不是最不流动的那一段股票**(避开 ST / 退市风险的尾巴,保留低价溢价)。这是讲得通、可交易的 A 股风格结构,但**不是 GP 发现的新信息**:价格水平不在 5 个控制里,中性化对它完全没有作用,带的两个切点是在 train 上拟合出来的。
- **证据**:`day_quantile_q75(pow_2_5(Close))` 单独 **−1.16**(最优方向已是做多低价,仍然 −1.16);套上 mask 之后 `cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Close)))` 单独 **+0.45**,方向翻成 +1。整个分差来自「把最便宜的 10% 挪走」这一步。head 3 里去掉这个 mask → 0.87,必要性 **+0.45**。
- **必要性 / 敏感性**:head 2 去掉 `log` 必要性 **−0.00**;head 3 去掉 `cs_normalize` 必要性 **−0.00**;`Open->Close` 1.32→1.32、`Close->Vwap` 1.32→1.29、`Amt->Volume` 1.40→1.38。按事实 (2),这些「稳」是因为那些算子不进计算,而带与排序键只看秩 —— **对带结构来说,同类字段互换不变是必然的,不构成信息的证据**。要证伪一个风格桶,得看它在规模 / 流动性桶内条件化之后还剩多少,而奖励的线性中性化做不到这件事。
- **共性**:`cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Close)))` 均值差 +1.58(p 0.005,n 4,**机械核心卡第 3 名**)、`log(day_open(Low))` +1.38(p 0.001,n 12)、`day_open(Low)` +1.26、`day_open(Open)` +0.95、`day_quantile(Vwap)` +0.63。富集表前 14 行里有 7 行是价格水平的各种写法。
- **预测(相关度表可验证)**:head 2 / 3 / 8 两两的日度秩 |ρ| 应该很高(我猜 ≥ 0.6,head 3 与 head 8 ≥ 0.8)。如果实测 < 0.7,说明库禁令的 0.7 门槛挡不住同一风格被多次收录,这件事本身要写进记录。

### 族 III(head 5,以及 head 3 的 x 参数)真来源 = 10% 平坦块落进多头十分位。判定:**代理**

```
+1.18  cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Amt)))
```

- `day_quantile_q75(pow_2_5(Amt))` 的秩 = `day_quantile_q75(Amt)` 的秩,而后者与**已知族的 |ρ| = 0.885**(拆解表),基本就是流动性控制本身。单独评 `day_quantile_q75(Amt)` = −1.19。
- 唯一改变秩的算子是 `cs_mask_top_replace_mean_neg`:把**最低 10%** 换成截面均值。`pow_2_5` 的作用是把分布拉得极右偏,把均值抬到很高的分位 —— 对数正态近似下 `X^2.5` 的均值落在原分布的 z = 2.5σ/2 处,`σ(log Amt) ≈ 1` 时约第 89 百分位(不做 `pow` 时只有约第 69 百分位)。**凸变换的全部功能是把平坦块抬进多头十分位。**
- 进去之后按事实 (3):块内残差 = 常数 − 控制拟合值,多头就从「最不流动的 10%」里挑控制拟合值最低的那些 → 多头腿 = **微盘 / 最不流动的角落**,方向 +1。
- 判定:陷阱 3 + 陷阱 1 的合成,而且信号与各控制的**线性** |ρ| 可以很低(`cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Close)))` 的 ρ(已知族) = −0.32),所以它能同时通过「|ρ| < 0.5 不合格判定」和「中性化」两道闸。
- **明确的告诫**:顺着这条线加凸度(`pow_2_5 → pow_3`)或收窄带宽(`cs_first_low20 → cs_first_low10`)几乎一定能把样本内分数做得更高,也几乎一定能触发 R 替换。**不要这么做** —— 那是规则 §4 列出的陷阱,审计员按「合理度 1:数字游戏,或利用了已知陷阱」应当直接划掉。

### 族 IV(head 4、head 7)`day_centroid(Amt)` = 当日成交额在分钟轴上的重心。判定:**唯一的真来源候选,但一半是已知族;起作用的是持久水平**

```
+1.22  sqrt(ts_quantile_q50(day_centroid(Amt), 20))        方向 -1
+0.82  cs_mask_top_replace_mean_neg(ts_quantile_q50(cs_mask_top_replace_mean_neg(ts_quantile_q50(ts_quantile_q50(day_centroid(Amt), 10), 10)), 10))   方向 -1
```

- **它是什么**(`ops_ext.py:155`):`sum(t·|x_t|)/sum(|x|)/(T−1) ∈ [0,1]`,0 = 全部成交在开盘,1 = 全部在收盘,0.5 = 对称。**尺度不变、有界、与价格和成交额的水平无关**,这是整批里唯一一个不是「水平」的量。241 格的第 0 根是开盘集合竞价、最后几根含收盘集合竞价(r1 审计员已提醒过),所以它很大程度上读的是**收盘竞价占比 vs 早盘占比**。方向 −1 = 做多「成交集中在早盘」的股票。
- **共性**:`ts_quantile_q50(day_centroid(Amt), 10)` 均值差 **+1.61**(p 0.000,n 15,全表第 1);`day_centroid(Amt)` **+1.41**(p 0.000,n 31,292 个候选里出现最多的有效子树);`ts_quantile_q50(ts_quantile_q50(day_centroid(Amt),10),10)` +1.41(p 0.002,n 9)。注意 n 31 约是 M2 归档的一半 —— 血统收敛,不是独立证据(与 r1 同一个告诫)。
- **充分性(付费)**:`ts_quantile_q50(day_centroid(Amt), 20)` 单独 **+1.21**(train +1.21 / valid +1.27)—— **整批里唯一两段几乎相等的子树**;裸 `day_centroid(Amt)` 单独 **−0.08**(train −0.08 / valid +0.58)。
- **必要性(付费)**:去掉 20 日中位数 → `sqrt(day_centroid(Amt))` = **−0.51**,必要性 **+1.73**。平滑是刚性需要的,**日度新息单独不值钱**。
- **敏感性(付费)**:`Amt->Volume` → **+1.21**(几乎不变 —— 成交额与成交股数的截面差别很大,这是整批里**唯一一次**真正的同类字段互换稳健性);窗口 10 / 20 / 40 → **0.98 / 1.22 / 1.22**,单调、无悬崖。
- **隐患(必须写进本轮计划)**:ρ(已知族)随窗口单调上升 —— **10 日 0.40 / 20 日 0.49 / 40 日 0.56**。40 日那版按奖励口径(|ρ| ≥ 0.5 判不合格)已经不合格。这个指纹与 r1 审计员抓到的 θ 指纹**同型**:「越平均越像控制变量,说明被平均出来的是持久成分」。所以必须承认:**+1.21 里有相当一部分是流动性 / 被动持股结构这个持久特征**(收盘竞价占比高的是指数成分、被动资金交易的名字)。
- **与文献方向相反的一点**:若按「散户注意力买盘集中在早盘」的机制,早盘成交占比高的股票之后应该**跑输**;而样本内拟合出来的方向是做多它们。方向与机制讲不通,这是另一条「它更像风格暴露而不是注意力效应」的旁证 —— 也是本轮要问文献员的事。
- **结论**:唯一值得花一个 E 位的核心,但要事先说清判决:**把持久水平拿掉之后还剩分数,才算真来源;一拿掉就归零,这一族就是流动性 / 规模的代理,第 3 轮放弃。**

### 族 V(r1 的 N 位遗产)`day_signed_ratio(Ret, Volume)` = 量价不平衡。判定:**唯一尺度不变且稳定高于池均值的一支,但只在 valid 上有效**

- **它是什么**(`ops_ext.py:122`):`sum(|y|·sign(x))/sum(|y|) ∈ [−1,1]`。`day_signed_ratio(Ret, Volume)` = 上涨分钟的成交占比 − 下跌分钟的成交占比(tick 规则的净买压代理)。与 5 个控制的 |ρ| 全部 ≤ 0.14(r1 相关度表 slot b seed 13:liq 0.01 / vol 0.01 / rev 0.14 / known 0.01 / size 0.06)。
- **共性**:`day_signed_ratio(Ret, Volume)` 均值差 **+0.26**(p 0.062,n 17);`sub(day_signed_ratio(Ret, Volume), day_signed_ratio(Ret, Ret))` +0.13(p 0.18,n 13);而 `day_signed_ratio(Ret, Ret)`(= ΣRet/Σ|Ret|,路径效率)**+0.01**(n 19)。
  → **信息在成交量的那一侧,不在价格路径里**,这是 r1 的 N 位挖出来的一条真结论。
- **r1 的 5 个最好候选全是它的 20 / 60 日平均**,score +0.12 / +0.06 / −0.12 / −0.13 / −0.21,但 **train ≈ 0 而 valid +1.34 / +2.33 / +1.93 / +2.26 / +2.31**。score 取两段较差的,全军没过线。
- **要指出的一个退化部件**:最好那条用了 `day_signed_ratio(Amt, Ret)`。`Amt` 非负 ⇒ `sign(Amt)` 在成交分钟恒为 1 ⇒ 这一项 = 「有成交的分钟占了当日 Σ|Ret| 的多大比重」,是一个**薄交易 / 流动性度量**(分钟 bar 无成交时 Ret 通常为 0,所以它大体是个接近常数的东西),不是任何意义上的不平衡。那条表达式实际上 ≈ 「20+20 日平滑的量不平衡」加一个近常数位移。

---

## 3. 烂部件清单(必要性 ≤ 0,或换掉反而更好)

| head | 部件 | 证据 | 适合做 R? |
|---|---|---|---|
| `sqrt(cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile_q75(Amt)), 3))` | `cross_quantile_q25(·, 3)` | 必要性 **−0.33**;去掉后 **+2.11**,train 2.05→2.11、valid 1.78→2.39 **两段都变好**;ρ(原 head) 0.97 | **是(R1,替换)** |
| 同上 | `cross_quantile_q25@3->2` | +1.92,增益 +0.14;同一部件的弱化版 | 是(R2,备选) |
| head 7(上面那条长表达式) | 两个 `cs_mask_top_replace_mean_neg` + 多余的嵌套中位数 | 两条依据:(i) 同核心、无 mask 的 head 4 高 **+0.41**;(ii) 事实 (3) + 方向 −1 ⇒ 重心的截面均值 ≈ 0.5(成交量 U 形),这里的 mask 把**最低 10% 重心**搬到中间,等于把自己最想持有的那一档股票从多头里剔掉 | **是(R3,替换)** |
| `cs_first_low20(day_quantile_q75(Amt), log(day_open(Open)))` | `log(·)` | 必要性 **−0.00**,分数逐位相同(1.3964 / 1.3964,valid 3.1523 / 3.1523)。原因见事实 (2):它在 `_lexi` 的带参数位上,只有秩进计算 | 否(增益 0)。但要记录:**死算子让骨架看起来不同而书完全一样**,库禁令只靠 ρ ≥ 0.7 那一条拦得住 |
| head 3 | `cs_normalize(·)` | 必要性 **−0.00**;同上,在 `_lexi` 的 y 位上只有秩进计算 | 否(同上) |
| `sqrt(ts_quantile_q50(day_centroid(Amt), 20))` | 根上的 `sqrt` | 去掉 = +1.21 vs +1.22,差 0.017。重心恒正,`sqrt` 对秩无影响,只通过「EMA 作用在变换后的值上」留下一点残差 —— 近乎死算子 | 否(增益 < 0.1) |
| `cs_first_low20(cs_normalize(day_open(Open)), cs_normalize(day_open(Open)))` | x 参数位整体 | y 与 x 同一表达式 ⇒ 这个 head 退化成「做多价格第 2 十分位」,x 位没有任何信息 | 否(任何改法都是把静态风格押注做得更极端) |

---

## 4. 之前各轮发生了什么

### 4.1 E 位(`c06s806Cr1a_Ea`,核心 `day_cov(Vwap, Ret)`)

- 计划的外围:除以 `mul(day_mean(Vwap), day_var(Ret))` / `mul(day_std(Vwap), day_std(Ret))` 去量纲、`cross_zscore(·, 20)` 取自身历史新息、`cs_bucket_zscore` / `cs_bucket_rank` 在方差 / 价格十分位桶内条件化、带号版本。定稿留下 5 个种子。
- 结果:**评分 77,过线 0,入 heads 0**。最好 5 条:
  `ts_corr(day_cov(Vwap, Ret), cross_reg_fvalue(cross_autocorr_s1(day_cov(Vwap, Ret), 241), day_cov(Vwap, Ret), 3), 40)` −0.09、同型的 −0.10、`inv(cross_autocorr_s1(day_cov(Vwap, Ret), 241))` −0.36、`inv(cross_decay_linear(day_cov(Vwap, Ret), 10))` −0.38、`inv(cross_decay_linear(day_cov(Vwap, Ret), 30))` −0.40。
- 采样计数 `{'c05_no_core': 1616, 'c05_periphery_seen': 9}`:绝大多数拒绝是「没有包含核心」,只有 9 次是「外围见过」。
- **本轮必须吸收的经验(比结论本身更重要)**:最好的 5 条里**没有一条是计划里的形态**,没有一条用到 `div` 去量纲或 `cs_bucket_*`;GP 走到了它自己的算子偏好上(`inv`、`cross_decay_linear`、`cross_autocorr_s1`、`ts_corr`、`cross_reg_fvalue`)。
  → **种子只决定起点,外围的分布由 GP 决定。想让外围做指定的事,必须把那件事做进核心,而不是指望外围去做。**
- r1 审计员的预判被证实:「GP 在核心外自由生长,`cross_mean` 一类外围会很快找到 θ 这条流动性捷径」。最好的两条正是多日衰减平均 `inv(cross_decay_linear(·, 10/30))`,而且 **train −0.38 / −0.40、valid +0.63 / +1.50** —— 持久成分在 valid 上像信号、在 train 上是负的,与「平均出来的是持久的 θ」完全吻合。

### 4.2 N 位(`c06s806Cr1b_Nb`,日内偏度 / 尾部 / 量价不对称)

- 结果:**评分 62,过线 0,入 heads 0**,最好 +0.12。
- **偏度族在第一代之后就被淘汰了**:富集表收录所有出现 ≥ 4 次的有效子树(`c05_locate.py`:`n < 4 or n > 0.7·len(cand)` 才跳过),而 292 个候选的富集表里**没有任何 `day_skew` / `day_es_ratio_hi` / `day_max` / 半方差占比的行**;留下来的全是 `day_signed_ratio` 这一支(§2 族 V)。
- 这正好触发了 PI 写下的条件:「如果偏度类全军覆没,说明彩票性被市值 / 波动控制吸收掉了,第 2 轮转向量价不对称」。GP 自己已经转过去了,而且那一支是整个 r1 里离过线最近的。

### 4.3 R

r1 没有 R(快照 0 个 head)。本轮 `loc.json` 第一次给出 2 个 R 候选,都在 head 1 上(§3)。替换 0 个、收录 0 个,目前「已生效的 R 替换 0 个」。

### 4.4 审计员挡掉了什么、为什么

- **a 位 创新 3 / 合理 3,通过**;14 个种子划掉 9 个剩 5 个。
  - 确定性划掉 3、4、5、12:与 liq / known 的 |ρ| ≥ 0.5(0.52 / 0.73 / 0.63 / 0.53)。
  - 7:`ts_rank(·, 20)` 逐日窗口内只有 ≤ 20 个取值,**distinct 0.018 未过门槛**(废品)。
  - 9、10:5 日平均的分桶版,liq 0.48 / 0.45,同一个 θ 问题只是还没跨 0.5。
  - 13、14:审计员指出 PI 的展开式有实质错误 —— `Vwap` 是 bar 内成交均价而不是 bar 收盘价,所以 `day_cov(Vwap,Ret)·M/P̄ ≈ (θ−½)·Q − R·δ`,**½ 实际上是随股票持久不变的 θ(bar 内 VWAP 位置,活跃股 ≈ ½、冷门股趋近 1,是流动性 / 微观结构特征)**;`sub(·, 0.5)` 减错了常数,这两个种子主要在读 `sign(R)`。
  - 这条修正是 r1 最有价值的产物,而且它的**预测被本轮数据证实**(见 4.1)。
- **b 位 创新 4 / 合理 4,通过**;15 个划掉 3 个剩 12 个。
  - 3:`cross_max(day_skew(Ret), 20)` 的截面差异主要来自偏度估计量的抽样离散度(薄交易、价格离散的股票更大),size 0.29 / vol 0.19 是本位最高;而且它不是 MAX 效应。
  - 6:正半方差占比的 20 日均值 ≈ 20 日里上涨的比重,**rev |ρ| 0.49 紧贴 0.5**,是 20 日反转的非线性重写。
  - 13:`day_signed_ratio(Ret, Volume)` 单独用时主要读当天涨跌方向。
  - 还留了四条提醒:`day_topw_mean(Ret, Volume)` 在 U 形成交量下取到的是开盘段;第 0 根 bar 是开盘集合竞价、最后几根是收盘集合竞价;偏度极值多是触板日;创业板 2020-08 起改 20% 涨跌幅。**第二条提醒本轮直接变成了族 IV 的核心问题。**

### 4.5 上一轮笔记里的预测,对不对

| 预测 | 结果 |
|---|---|
| a 位约 25% 出 head | **错**(偏乐观):0 个,最好 −0.09 |
| a 位产出最可能是「5–20 日平滑的无量纲时点比值或方差桶内 z 分数」 | **错**:最好的 5 条没有一条是这个形态,全是 GP 自己的 `inv` / `ts_corr` / `cross_decay_linear` |
| 事先判决:本位候选 score 若低于 `add(LimitWidth,·)` 组的 −0.58,**第 2 轮放弃这个核心** | **触发了**:含 `day_cov(Vwap, Ret)` 的 75 个归档候选均值 **−1.45**(不含的 −0.93),而 `add(LimitWidth, day_cov(Vwap,Ret))` 组在本轮表里是 −0.67。归一化那一支比 LimitWidth 那一支**更差**。按 PI 自己写下的规则:**本轮放弃 `day_cov(Vwap, Ret)`** |
| 风险:核心与**波动**控制 \|ρ\| 可能接近 0.5 | **错在通道**:实测 core 的 vol 0.04 / liq 0.19 / known 0.18。真正的泄漏是**流动性**,而且只在外围做了多日平均之后才出现(0.35 → 0.52 → 0.73) |
| b 位约 30% 出 head;最可能是周 / 月频平滑的偏度或正半方差占比 | **错**:0 个,而且偏度族在富集表里连 4 次出现都没有;活下来的是量价不平衡 |
| 「`add(LimitWidth, ·)` 那一族过不了 0.5」 | **目前成立**:M 第 2 批 8 个 head 里没有一个含 `LimitWidth`;那一族在 292 个候选里的均值仍是 −0.67 |
| 「三阶矩 / 上下不对称 / 量价不对称是本种子最值得押的新方向」 | **半对**:三阶矩 / 尾部被 GP 淘汰;量价不对称是 r1 唯一的近失(valid 腿 +1.3…+2.3,train 腿 ≈ 0) |

---

## 5. 本轮候选

### 5.1 核心 A(首选,给 E 位)`ts_quantile_q50(day_centroid(Amt), 20)` —— 机械核心卡第 1 名,自身 score +1.21

**为什么选带 20 日中位数的版本而不是裸的 `day_centroid(Amt)`**:
按 4.1 的经验,想让外围做「把持久水平减掉」,就要**把持久水平本身做成核心**,这样外围唯一能对它做的有意义的事就是「减掉它 / 用它分组」。E 位要求每个候选原样包含核心,而 `sub(day_centroid(Amt), ts_quantile_q50(day_centroid(Amt), 20))`、`cs_bucket_rank(day_centroid(Amt), ts_quantile_q50(day_centroid(Amt), 20))` 都包含核心。裸核心做不到这一点(GP 大概只会再加一层平滑,而那会被库禁令按 ρ ≥ 0.7 直接拒掉 —— 这一次库禁令是在帮我们)。

- **已经见过的外围(全部)**:`{sqrt}` = head 4(+1.22);`{}`(子树本身,+1.21);窗口变体 `{sqrt}@10`(+0.98)、`@40`(+1.22);同核心族的其它写法 `ts_quantile_q50(ts_quantile_q50(day_centroid(Amt),10),10)`(富集 +1.41)、`cs_mask_top_replace_mean_neg(ts_quantile_q50(ts_quantile_q50(·,10),10))`(富集 +1.19)、head 7。
  **即:见过的外围只有 {平滑、`sqrt`、`cs_mask_top_replace_mean_neg`} —— 全是在水平上再做平滑或砍掉底部 10%。**
- **本轮外围要做的事(与上面明显不同,创新度应到 3)**:
  1. **新息**:今天的重心相对自己的 20 日基准 —— `sub(day_centroid(Amt), <核心>)`、`div(day_centroid(Amt), <核心>)`;
  2. **条件化**:在规模 / 流动性十分位桶内比较 —— `cs_bucket_rank(<核心>, LogFloatCap)`、`cs_bucket_zscore(<核心>, cross_mean(day_sum(Amt), 30))`(直接针对 ρ(已知族) 0.49 这个隐患);
  3. **量的时点 vs 价格位移的时点**:`sub(<核心>, ts_quantile_q50(day_centroid(abs_(Ret)), 20))` —— 钱是在价格动之前还是之后进来的,尺度不变、与水平无关;
  4. **买卖两侧的时点差**:`day_centroid(mul(Amt, is_gt0(Ret)))` 与 `day_centroid(mul(Amt, is_lt0(Ret)))` 之差(`is_gt0` / `is_lt0` 见 `catalog.py:149-150`;`day_centroid` 取 `|x|` 且零值不进分母,所以这是「上涨分钟的成交重心」);
  5. 明确**不要**:再加一层平滑的水平版(见过了,且会被库禁令拒)、40 日及更长窗口(ρ(已知族) 0.56 已不合格)、任何 `cs_mask_top_replace_mean_neg`。
- **合法性风险(请 PI 在相关度表里先确认)**:核心的 ρ(已知族)在拆解表里是 **0.4931**。E 位要求核心与**每个**控制 |ρ| < 0.5 —— 离门槛只有 0.007,而相关度表用的是 train 每 5 天取一天的另一个样本,**可能落到 0.5 以上**。
  **备选核心**:`ts_quantile_q50(day_centroid(Amt), 10)`(核心卡第 2,富集 +1.61 / p 0.000 / n 15,ρ(已知族) **0.4027**,余量大得多)。若 20 日那版超线就换它,机制与外围写法照搬。
- **事先判决建议**:如果「把持久水平减掉」那一类候选的 score 不高于「水平本身」那一类,或本位 0 个 head 且最好候选 < 0.3,则认定 `day_centroid` 族是流动性 / 规模的代理,第 3 轮不再碰。

### 5.2 核心 B(次选,给第二个 E 位)`day_signed_ratio(Ret, Volume)` —— 机械核心卡第 19 名

- **为什么**:292 个候选里唯一一个「尺度不变、与 5 个控制 |ρ| ≤ 0.14、而且含它的候选均值高于不含的」的量(+0.26,p 0.062,n 17);而路径效率 `day_signed_ratio(Ret, Ret)` 的均值差只有 +0.01,说明信息在成交量那一侧。r1 它已经是最接近过线的一支。
- **已经见过的外围(全部,来自 r1 N 位最好的 5 条)**:`{sub, cross_mean@20}`、`{sub, cross_mean@60}`、`{sub, sub, cross_mean@20}`、`{sub, cross_mean@20, cross_mean@20}`,减项是 `day_signed_ratio(Ret, Ret)` 或退化的 `day_signed_ratio(Amt, Ret)`。**算子集合只有 {sub, cross_mean} 两个。**
- **本轮外围要做的事**:(a) 相对自身历史的新息 `cross_zscore(day_signed_ratio(Ret, Volume), 20)`(r1 唯一一个五个控制全 ≤ 0.03 的写法用的就是 `cross_zscore`);(b) 在波动 / 流动性桶内取秩;(c) 把大单与小单侧分开(`day_signed_ratio(Ret, Amt)` 与 `day_signed_ratio(Ret, Volume)` 之差);(d) 不平衡的**持续性**(20 日内同号比例)而不是再做一次平均。
- **事先判决建议**:r1 的事实是 **train ≈ 0、valid +1.3…+2.3**。本位要解决的只有一件事:**train 腿**。判决写成「若本位所有候选的 train 腿仍然 ≤ 0.2,则这一族在 2018–2021 不存在,放弃」,而不是看 score。
- **注意**:N 位的硬要求(3 轮里至少 1 个 N 位通过审计)在 r1 已满足(b 位 创新 4 / 合理 4 通过),所以本轮两个位都用 E 是允许的。

### 5.3 明确不推荐的核心(但它在机械核心卡上排第 3,必须说清楚)

`cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Close)))`(富集 +1.58,p 0.005,n 4),以及 `cs_last_low40(LogFloatCap, day_quantile(Vwap))`(+1.36,n 5)、`day_quantile_q75(Amt)`(+1.27)、`log(day_open(Low))`(+1.38)、`day_open(Open)`(+0.95)。
理由见 §2 族 I–III:这些核心的「alpha」来自平坦块 / 折叠 / 价格带,外围长出来的东西只会把同一个风格暴露做得更极端。另外 `day_quantile_q75(Amt)`、`cs_last_low40(LogFloatCap, day_quantile_q75(Amt))`、`cross_quantile_q25(cs_last_low40(…), 3)` 的 ρ(已知族)分别是 **0.885 / 0.769 / 0.799**,按 E 位规则(核心与每个控制 |ρ| < 0.5)**本来就不合法**。

### 5.4 R 目标(16 个额度,建议只用 2–3 个)

| # | 原 head | 变体 | 依据 | 预期 |
|---|---|---|---|---|
| **R1** | `sqrt(cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile_q75(Amt)), 3))` | `sqrt(cs_last_low40(LogFloatCap, day_quantile_q75(Amt)))` | 已付费测过:必要性 −0.33,score +2.11(train 2.11 / valid 2.39),两段都优于原 head;ρ(原 head) 0.97;ρ(已知族) −0.103 | 增益 +0.33 ⇒ **替换**。换掉的只是 3 日 q25 的抖动,留下的仍是族 I 的市值 V 形 |
| R2 | 同上 | `sqrt(cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile_q75(Amt)), 2))` | 同一部件的弱化版,已测 +1.92,增益 +0.14 | R1 的备选 |
| **R3** | head 7 | `ts_quantile_q50(ts_quantile_q50(ts_quantile_q50(day_centroid(Amt), 10), 10), 10)`(剥掉两个 mask) | (i) 同核心、无 mask 的 head 4 高 **+0.41**;(ii) 事实 (3) + 方向 −1 ⇒ 这两个 mask 把最低 10% 重心的股票从多头里剔掉,正是这个 head 最想持有的一档 | 预期增益 +0.3 ⇒ **替换**。**代价要说清**:替换后它与 head 4 的 ρ 会很高(≈0.9),库里会多一个近重复项;但多头腿是「控制变量折叠」的 head 比一个重复项更糟,所以我建议做 |
| (可选) | head 4 | `ts_quantile_q50(·, 20)` → `cross_mean(·, 20)` | 20 日中位数只取窗口里的一个次序统计量;窗口 10→20→40 的分数 0.98→1.22→1.22 说明「用更多天」是有益方向 | 风险明确:中位数版 20 日 ρ(已知族) 已 0.49、40 日 0.56,均值版很可能 ≥ 0.5 ⇒ 按 R 规则(与已知族 |ρ| < 0.5)**被判不合格**。额度不紧张时再提 |

**不要提交的 R**(会提高样本内分数但属于规则 §4 陷阱,审计应按合理度 1 划掉):`pow_2_5 → pow_3`、`cs_first_low20 → cs_first_low10`、`cs_last_low40 → cs_last_low20/10`、给族 I/II/III 的任何 head 加凸变换。

### 5.5 N 的灵感(如果第二个位用 N 而不是 E)

1. **成交的时点 vs 位移的时点**:`sub(day_centroid(Amt), day_centroid(abs_(Ret)))` —— 当日的钱是在价格动之前还是之后进来的(量领先 / 量滞后)。有界、尺度不变、与价格和成交额的水平都无关,结构上不可能是控制变量的重写;与库里 8 个 head 没有共同子树。
2. **买盘时点与卖盘时点之差**:`sub(day_centroid(mul(Amt, is_gt0(Ret))), day_centroid(mul(Amt, is_lt0(Ret))))` —— 把族 IV(时点)和族 V(量价不平衡)合起来,是两者都没覆盖的量:不平衡读「哪一侧」,重心读「什么时候」,这个读「哪一侧在什么时候」。
3. **成交时点剖面的不稳定性**:`day_centroid(Amt)` 相对自身 20 日分布的离散度(而不是水平)—— 交易时间结构突然改变往往对应资金面 / 事件,水平则是风格;它天然躲开「越平均越像控制」这个指纹。

### 5.6 希望在本轮相关度表里看到的(帮审计员,也帮判决)

- `ts_quantile_q50(day_centroid(Amt), 20)`(及备选 `@10`)与 **5 个控制**的 |ρ| —— 决定 E 位是否合法;
- R1 / R3 变体与**每个 head** 的 |ρ|:R3 与 head 4 的 ρ(量化「库里多一个近重复」的代价),R1 与 head 6 的 ρ(验证族 I 内部是同一个押注);
- 若能加诊断行:head 2 / 3 / 8 两两的 |ρ|,以及它们与 `cs_normalize(day_open(Open))` 的 |ρ| —— 验证 §2 族 II 的「三个 head 是同一个价格带」判断。

---

## 6. 给文献员的题目(4 个)

1. **对准核心 A(`day_centroid(Amt)`)。**
   「文献里对**日内成交量 / 成交额在一天之内的时点分布**(开盘段占比、收盘集合竞价占比、成交重心 / 时间加权重心)做过哪些处理?它预测截面收益的**方向**是什么?有没有证据表明这个量主要是规模 / 被动持股 / 流动性的代理,文献用什么办法把那部分剥掉(分桶、对规模回归、取相对自身历史的异常值)?2023-08-08 之前的证据优先,中国 A 股优先。」
   关键词:成交量日内分布、成交重心、收盘集合竞价占比、开盘买盘、被动资金 / 指数成分、交易时点;intraday volume timing / distribution, closing auction volume share, time-weighted volume centroid, "when during the day volume is traded", passive ownership and close-auction trading, overnight returns and buying at the open, high-volume return premium, Admati–Pfleiderer intraday volume patterns.

2. **对准核心 A 的外围(水平 vs 新息)。**
   「一个**持久的微观结构 / 交易行为特征**,文献里怎样把它拆成『持久部分(风格、流动性暴露)』和『相对自身历史的异常部分』?异常成交量 / 异常换手(abnormal turnover)这一类做法用什么窗口、什么标准化、预测期限多长,两部分各自的预测力如何?」
   关键词:异常换手率、去趋势成交量、相对自身历史标准化、滚动 z 分数、特征的持久成分与短期成分;abnormal turnover, detrended / standardized unexpected volume, volume innovation, characteristic level vs. innovation decomposition, rolling z-score standardization of firm characteristics.

3. **对准核心 B(`day_signed_ratio(Ret, Volume)`)。**
   「tick 规则的**日内成交量不平衡**(上涨分钟成交占比 − 下跌分钟成交占比)在中国 A 股上的处理:相对什么基准归一化(成交量 / 成交额 / 路径效率)、预测期限多长(日 / 周 / 月)、是否需要在流动性或波动分组内条件化、分大单小单后结论是否不同?有没有文献报告它的预测力**在 2018–2021 与 2022 年之后不同**(样本期分段结果)?」
   关键词:订单不平衡、tick 规则交易方向判定、成交量不平衡、分笔规模(大单 / 小单)、路径效率;order imbalance, tick-rule trade classification, volume order imbalance China A-shares, trade-size-classified imbalance, order imbalance predictability horizon, subsample stability.

4. **对准族 I–III 的判定(需要外部依据支持「这是代理而不是信息」)。**
   「文献里对**非单调 / 分段 / 门槛型的截面特征**(例如『按市值秩折叠』、『只在某个分位带内选股』、『把最低一档替换成均值』)与**线性中性化**的相互作用有什么结论?线性正交化之后残留的**非线性规模暴露**有多大、怎么度量、推荐用什么替代(分桶中性化、单调性检验、非参数残差)?以及 A 股『低价股 / 微盘股溢价』在剔除 ST / 退市风险尾部之后的刻画(『便宜但不是最便宜』这种非单调结构有没有文献版本)?」
   关键词:非线性因子暴露、分段 / 门槛特征、分桶中性化、低价股溢价、微盘股、ST 与退市风险、非单调性;nonlinear factor exposure after linear neutralization, piecewise / threshold characteristics, within-group (bucket) neutralization vs. linear residualization, low-price premium, microcap premium, delisting / distress risk tail in Chinese A-shares, non-monotonic characteristic–return relations.

---

## 7. 我可能错在哪里(留给审计与下一轮复盘)

1. §2 族 I 的「市值 V 形 + 多头落在两端」是从 `_lexi`、`sqrt(|·|)`、`_zrank`、`long_short_weights` 的源码推出来的,**没有付费评估直接验证两端的持仓构成**。能验证它的是相关度表:head 1 / head 6 与 size 控制的原始 |ρ| 应该不高(V 形的一次项 ≈ 0),而两者之间的 ρ 应该很高。如果 head 1 与 size 的 |ρ| 反而很高,我的 V 形读法就要改。
2. §2 族 III 里「均值落在第 89 百分位」用的是对数正态近似和 `σ(log Amt) ≈ 1` 的假设,没有实测。结论(平坦块进多头十分位)对这个数字不敏感,但如果真实的 σ 小很多,块可能落在中位附近,那时 head 5 的解释要换成「把最不流动的 10% 从多头里剔掉」(与 head 7 的 mask 同型)。
3. §5.1 的事先判决假设「GP 会沿着核心被迫做新息」。4.1 的经验说 GP 未必听话;如果本位又长出一堆与计划无关的东西,那说明 E 位这个机制对本种子不好用,第 3 轮应该改用 N 位 + 更强的种子约束。
