# F107_abs_demean_skew_low — 研究现状(**自动汇编**,2026-10-04 13:10)

> 这一页不是研究员写的。上一位研究员(Opus 5.5,工作流 agent `study:F107_abs_demean_skew_low`)在写下现状之前就被换下了;
> 协调者用脚本(`scripts/autostate.py`,不经过任何模型)把磁盘上**它写过的和做过的**汇编成这一页。
> 它当时怎么想的没有留下 —— 假设的最新状态、对结果的解读,需要接手的主研读下面列出的材料后**重写这一页**。

## 1. 一句话现状

- 配置里的一句话(研究员读完这棵树之后写的):日内价格水平占用分布的偏度偏离全市场多少(折叠) —— 空头腿是封板/跳价事件,多头腿是「安静且随大盘走」的股票
- 已写 notes:02_operators.md、03_decomposition.md、04_grammar.md、05_hypotheses.md、06_baseline.md、07x_1_anatomy.md
- 已拉回本地的运行:S0_baseline;已启动但**结果还没人读**的:S12
- 留出段:未读

## 2. 中间结果(事实在这些文件里,还没有汇总)

- 运行 `S0_baseline`(10-04 11:50):`./scripts/study.sh digest F107_abs_demean_skew_low S0_baseline`
- 自写分析 `x1` 的输出:`logs/F107_abs_demean_skew_low_x1.log`

### 基线读数(原文照录 `notes/F107_abs_demean_skew_low/06_baseline.md`)

**方向**:−1(`\|B\|` 越大之后越跑输),半衰期 20 —— 多头口径和多空口径选到的是同一个,在 train 上定的和在 utrain 上定的也一致,和用户表一致。
S0 复现了用户表的训练列:扣费多空夏普 **2.89**、多头腿**毛**超额 **10.0%**(用户口径,utrain;用户表里的 0.099 是毛超额)。下面是决策口径(方向 / 半衰期在 train 上定)。

要先记住的六件事:

1. **多头腿毛超额不小,但几乎全被换手吃掉。** 多头腿毛超额 train **+9.4%** / valid **+11.4%**,多头书日换手 10.9% → 成本约 8.2 个点,
   净超额只剩 **+1.1% / +3.0%**,纯多头夏普 +0.24 / +0.69(用户口径 utrain:+1.7%、0.36)。对只能做多的使用者,原式照现在的样子基本不可用;
   但毛超额在那里 —— 问题出在换手上。
2. **半衰期顶在可选集合的上界。** 多头书的半衰期扫描(train,净超额 / 日换手):hl0 −63.2% / 90%、hl2 −23.5% / 45%、hl5 −10.2% / 28%、hl10 −3.1% / 18%、hl20 **+1.1%** / 11%,
   单调改善到 20 为止;多空夏普同样(hl0 −14.1 → hl20 +2.81)。树里没有任何日轴记忆,原始日频面板的 rank IC 只有 0.018,平滑之后的可交易信号是 0.034(valid 0.015 → 0.042);
   衰减表的 rank IC 随预测期一路上升(h1 0.034 → h5 0.049 → h20 0.062)。这是一个慢变量,20 日的 EMA 还没有把它平滑够(H11)。
3. **钱在空头腿,而且集中在最差的一个十分位。** train 上多头腿毛超额 +9.4%、空头腿 +32.5%,多头只占毛价差的 22%(valid 27%)。
   分位剖面 train:Q1 **−32.7%**、Q2 −6.3%、Q3 −0.8%、Q4 +1.9%、Q5 +1.5%、Q6 +4.8%、Q7 +5.5%、Q8 +7.8%、Q9 +8.8%、Q10 **+9.6%**;
   valid:−31.0%、−8.7%、−3.6%、−0.4%、+3.7%、+5.9%、+6.0%、+6.1%、+10.2%、+11.8%。
   剖面是单调的,但形状是两段:Q1 远离其余九个(一个「事件」),Q3~Q10 是一段平缓的梯度(每个十分位约 1.5 个点)。多头端不是事件,是梯度的上端。
4. **数值比名次更有信息(对空头腿而言)**:原始面板在 train 上 Pearson IC 0.0377(t = 21.3),rank IC 0.0180(t = 13.8)。`\|B\|` 是厚尾量,极端的那几个值本身带信息(H1)。
5. **多头腿逐年都是正的毛超额,但净超额在 0 上下**:多头腿毛超额 2018~2023 是 +12.4%、+10.6%、+10.1%、+4.5%、+9.1%、+15.4%;净超额 +4.1%、+2.3%、+1.8%、**−4.0%**、+0.5%、+6.8%。
   扣费多空夏普 3.23、3.82、2.54、1.68、2.71、4.06 —— 2021 年两本书都最弱。
6. **按流通市值分五组的条件 IC(可交易信号,train)**:+0.045、+0.045、+0.045、+0.031、**+0.007** —— 最大的五分之一里几乎没有信号;
   按当天成交额分组是平的(+0.026~+0.034)。它是一条中小市值里的因子。

**已知暴露的第一眼**(S0 的中性化表,对象是可交易信号,train):全部 9 个控制变量 R² **0.214**,残差 rank IC 0.0337 → 0.0143;
空头腿毛超额 +32.5% → **+4.6%**(只对 `ctl_dvol20` 一个变量就到 +4.9%),而**多头腿毛超额 +9.4% → +8.2%**。
读法:空头腿基本是「高波动、高换手的票之后跑输」这个已知暴露;多头腿不被这 9 个单调控制变量线性解释。
但原式是折叠过的量,线性秩回归看不见非单调关系 —— 这个 R² 只是下界,x1 §7 用折叠过的控制变量重量之后结论变了(见 07x_1_anatomy)。

与已知家族的秩相关(可交易信号对各自的原始面板;已知家族方向也为负,所以负号表示同向):`cross_max(day_std(Amt), 9)` −0.28、`cross_mean(day_std(Amt), 30)` −0.28、
`cross_max(day_var(Ret), 9)` −0.31、`ctl_dvol20` −0.38。已知家族自己在同一口径下的多头腿净超额是 +12.6%~+13.7% / +22.2%~+22.3%(纯多头夏普 1.8~2.0 / 3.5~3.6)——
原式的 +1.1% / +3.0% 离它很远,这是后面所有候选要面对的第二条基准。


### 已写的阶段结论(原文照录 `notes/F107_abs_demean_skew_low/07x_1_anatomy.md`)

### x1:原式在真实数据上到底读到了什么(`studies/F107_abs_demean_skew_low/x1_anatomy.py`,tag `x1`;只切 utrain 的行)

所有变体都是从同一批日频面板(`A = day_skew(Low)` 等)在 numpy 里拼出来、用与总表相同的书(`st.books`)量的;它们是**探路**,正式数字在 S1 / S2 里用引擎重算。
自检:numpy 复算的 `\|A − 行均值\|` 与引擎面板最大差 8.6e-07;用 `st.books` 重算的原式与 S0 逐项相同(多头腿净超额 +1.1% / +3.0%、多空 2.81 / 3.16)。
另一项自检没有通过 —— numpy 的滚动均值与引擎的 `cross_mean(原式, 30)` 不是同一个面板(Spearman 0.9989,最大差 12.6),放到 x2 §a 查。

**1. 事件层面(不平滑):次日超额按带符号的 B 分桶** —— 折叠不是对称的。

| B 所在区间 | 占比 (train) | 次日超额 train | valid |
|---|---|---|---|
| ≤ −2 | 1.6% | **−113.6%** | **−61.8%** |
| (−2, −1] | 7.2% | −0.1% | −1.6% |
| (−1, −0.5] | 12.9% | +7.6% | +3.1% |
| (−0.5, −0.25] | 11.6% | **+8.9%** | **+7.5%** |
| (−0.25, 0] | 14.9% | +6.8% | +2.8% |
| (0, 0.25] | 15.5% | +5.4% | +3.1% |
| (0.25, 0.5] | 12.8% | +1.6% | +1.1% |
| (0.5, 1] | 14.7% | −5.4% | −1.2% |
| (1, 2] | 7.6% | −12.5% | −3.5% |
| > 2 | 1.3% | −37.0% | −22.6% |

负的一侧(大部分时间在高位)是「平台 + 悬崖」:一直到 −1 都是全截面最好的区域,过了 −2 才塌,而且塌得最狠(钉在高位的格子次日年化 −289% / −224%,全天不动的 −508% / −450%,
钉在低位的 −104% / −35%);正的一侧(大部分时间在低位、短暂冲高)是一条从 +0.25 就开始的斜坡。最好的桶是 (−0.5, −0.25],不是 0。
所以 **H5(折叠对称)在事件层面被否定**:`abs_` 把一个「左边悬崖、右边斜坡、最优点偏左」的形状压成了对称的 V。这条线索在 x2 §b 里用移了中心的折叠去追。

**2. 持续层面(EMA20)**:带符号的 `EMA20(B)` 的十分位剖面 train 是 −22.3 / +7.3 / +6.2 / +6.7 / +5.3 / +3.9 / +5.0 / +1.2 / −1.8 / **−11.4**,valid 是 −27.6 / +0.1 / +4.2 / +3.9 / +5.3 / +3.3 / +2.3 / +3.1 / +4.1 / **+1.3**。
最负的一头两段都差;最正的一头 train 差、valid 不差。在 `EMA20\|B\|` 最小的 30% 里(多头一侧),`EMA20(B) < 0` 的格子 +13.7% / +11.6%,`≥ 0` 的 +4.7% / +7.2% —— 方向信息在多头一侧也有,train 强、valid 弱。

**3. 折叠 / 尾部 / 统计量的变体**(方向与半衰期在 train 上定,全部选到 20;ρ = 与原式可交易信号的日截面秩相关)

| 变体 | 多头腿净超额 tr / va | 多头腿毛超额 tr / va | 多头换手 | 扣费多空 tr / va | 空头腿 tr | ρ |
|---|---|---|---|---|---|---|
| 原式 `\|B\|` | +1.1% / +3.0% | +9.4% / +11.4% | 10.9% | 2.81 / 3.16 | +32.5% | 1.00 |
| `\|A\|`(不去均值) | −5.7% / −5.1% | **+3.4% / +3.7%** | 12.1% | 1.96 / 1.56 | +31.4% | 0.90 |
| 带符号的 B | −30.1% / −36.6% | −22.1% / −27.1% | 10.5% | −2.31 / −4.02 | +11.1% | −0.10 |
| `min(\|B\|, 1)`(截尾) | −0.7% / +1.6% | +9.2% / +11.9% | 13.1% | **0.72 / 1.56** | **+17.5%** | 0.87 |
| 逐日截面秩 | −0.4% / +1.9% | +9.8% / +12.3% | 13.4% | 0.89 / 1.51 | +18.2% | 0.88 |
| `1{\|B\| > 2}`(只留尾部) | +1.5% / +1.2% | **+3.2% / +3.3%** | 2.2% | 2.81 / 2.89(hlS 10) | +33.5% | 0.69 |
| `1{钉住或全天不动}`(hl 0) | +2.1% / +2.1% | +3.0% / +2.5% | 1.2% | 3.74 / 2.49(hlS 2) | +52.5% | 0.11 |
| 钉住日换成截面中位数 | −2.9% / +0.8% | +5.9% / +9.5% | 11.6% | −0.38 / 0.83 | +7.8% | 0.84 |
| `(max+min−2·med)/(max−min)` 折叠 | −1.1% / −1.5% | +9.5% / +9.2% | 14.1% | 1.71 / 2.05 | +24.1% | 0.78 |
| `\|去均值 day_skew(Close)\|` | +0.6% / +5.0% | +8.0% / +12.1% | 9.7% | 2.61 / 2.42(hlS 10) | +39.7% | 0.95 |
| `day_kurt(Low)` | −7.3% / −9.4% | **+0.5% / −1.9%** | 10.3% | 2.02 / 0.98 | +29.1% | 0.78 |
| `day_kurt(Ret)` | +0.8% / +10.8% | +2.9% / +12.5% | 2.8% | 2.59 / 2.07(hlS 10) | +37.8% | 0.47 |
| 分钟收益与大盘的日内相关(方向 +) | +3.8% / +6.1% | +6.2% / +9.2% | 3.1% | 0.94 / 0.87 | +15.2% | 0.13 |

读法:

- **两条腿是两种机制**。把尾部截掉或取秩:多头腿毛超额纹丝不动(+9.2%~+9.8% / +11.9%~+12.3%),空头腿少一半、多空夏普从 2.8 掉到 0.7~0.9 ——
  空头腿在尾部(H1 成立),多头腿在主体(H2 成立)。反过来只留尾部(`1{\|B\|>2}`、钉住指示量):多空夏普不掉甚至更高,多头腿毛超额只剩 3 个点。
  把钉住日换成中性值之后空头腿只剩 +7.8%:**空头腿就是「最近封过板 / 被钉住过」**,次日开盘追进去的人吃亏。
- **`cs_demean` 是多头腿的必需节点(H6 被否定)**:去掉它,空头腿不变(+31.4%),多头腿毛超额从 +9.4% / +11.4% 掉到 +3.4% / +3.7%。
  多头端要的不是「偏度绝对值小」,而是「偏度离**当天全市场的形状**近」。
- **字段不重要(H10 成立)**:Close 的可交易信号秩相关 0.95、High 0.93,书在噪声内相同。**三阶矩对多头腿不是必需的(H9 对多头腿成立)**:有界的极差不对称度多头腿毛超额相同,只是换手更高、空头腿更弱。
- **同一条路径的四阶矩 `day_kurt(Low)` 与原式可交易信号秩相关 0.78,却没有多头腿**(+0.5% / −1.9%):原式的多头腿不在它与峰度共享的那部分(尾部事件)里。

**4. 时间尺度(滚动 nanmean,外面再套半衰期网格)** —— H11 成立,而且改进来自换手。

| 写法 | 选到的半衰期 | 多头腿净超额 tr / va | 纯多头夏普 tr / va | 毛超额 tr / va | 换手 |
|---|---|---|---|---|---|
| 原式 | 20 | +1.1% / +3.0% | 0.24 / 0.69 | +9.4% / +11.4% | 10.9% |
| 10 日均值 | 20 | +4.9% / +6.9% | 1.01 / 1.59 | +7.8% / +9.9% | 3.8% |
| 20 日均值 | 20 | +5.0% / +7.5% | 1.01 / 1.74 | +7.1% / +9.6% | 2.7% |
| 30 日均值 | 5 | +4.9% / +6.9% | 1.05 / 1.64 | +8.2% / +10.3% | 4.4% |
| 60 日均值 | 3 | **+6.0% / +6.6%** | 1.17 / 1.54 | +8.5% / +9.2% | 3.4% |
| 120 日均值 | 3 | +4.6% / +9.7% | 0.88 / 2.15 | +6.2% / +11.3% | 2.2% |
| 241 日均值 | 2 | +2.3% / +9.8% | 0.43 / 1.98 | +3.6% / +11.1% | 1.7% |
| EMA 半衰期 40(网格之外) | — | +3.3% / +5.5% | 0.67 / 1.25 | +8.1% / +10.5% | 6.3% |
| EMA 半衰期 60 | — | +3.2% / +7.1% | 0.64 / 1.58 | +6.5% / +10.6% | 4.5% |

10~60 日的窗口都落在 +5%~+6% / +6.6%~+7.5%,纯多头夏普 1.0~1.2 / 1.5~1.7;毛超额没有升(train 还降了 1~2 个点),净超额多出来的 4 个点全部来自换手从 10.9% 降到 3%~4%。
120 日以上 train 往下走、valid 往上走,两段不同向。先取秩或先截尾再求均值(`mean60(秩)` +5.0% / +7.2%)没有更好。

**5. 谁在多头端**(可交易信号的第 10 个十分位,各特征的日内百分位秩均值,train / valid):流通市值 0.49 / 0.51、成交额 0.36 / 0.38、换手率 0.36 / 0.36、
20 日波动 **0.30 / 0.28**、分钟收益峰度 **0.27 / 0.29**、已知家族 `cross_mean(day_std(Amt), 30)` 0.35 / 0.37、与大盘的日内相关 0.46 / 0.49;20 日内出现过 `\|B\| ≥ 2` 的只有 6.8% / 10.5%。
空头端:20 日波动 0.72 / 0.74、换手率 0.67 / 0.69、分钟收益峰度 0.80 / 0.75,80% / 87% 的股票 20 日内出现过 `\|B\| ≥ 2`,56% / 53% 被钉住过。
多头端是「安静的票」:不大不小、成交少、波动低、不跳。与大盘的日内相关在各十分位之间不单调(空头端 0.33,中间 0.55,多头端 0.46)—— **H7(共同路径份额)不成立**,秩相关只有 +0.13。

**6. 已知暴露,用折叠过的 / 这棵树特有的控制变量重量**(对象是可交易信号,train,秩空间逐日回归)

| 控制变量 | R² | 残差 rank IC | 残差多头腿毛超额 | 残差空头腿 |
|---|---|---|---|---|
| (未中性化) | — | 0.0337 | +9.4% | +32.5% |
| 9 个共用控制变量(= S0) | 0.214 | 0.0143 | +8.2% | +4.6% |
| 再加各自的平方项 | 0.254 | 0.0120 | +4.5% | +0.9% |
| 只用 `EMA20 \|去均值 日收益\|`(同样折叠) | **0.307** | 0.0091 | **+2.9%** | +3.3% |
| 只用 `EMA20 1{\|日收益\| > 9%}` | 0.116 | 0.0211 | +5.8% | +1.6% |
| 只用 `EMA20 day_kurt(Low)` | 0.617 | 0.0245 | +13.2% | +3.4% |
| 只用已知家族 `cross_mean(day_std(Amt), 30)` | 0.080 | 0.0258 | **+3.9%** | +17.6% |
| 9 个 + 全部树特有的 | 0.784 | −0.0003 | +3.5% | −2.5% |

S0 的「多头腿不被控制变量解释」是线性单调控制变量造成的假象(playbook §6.5 说的那种):换成同样折叠过的日频量 —— 20 日平均的 `\|特质日收益\|`,
一个完全不看日内路径的量 —— 一个变量就解释 31% 的方差,残差多头腿毛超额只剩 2.9 个点、空头腿 3.3 个点。**原式的大部分是「特质波动(平均绝对特质收益)」的带噪声写法**;
它在这之外是不是还有东西,S1 的 `r_absret` / S2 的 `m20_absret` 直接替换实验来回答。

**7. 对只能做多的用户:相对已知家族 K = `cross_mean(day_std(Amt), 30)`**(K 自己:多头腿净超额 +12.6% / +22.3%,纯多头夏普 1.78 / 3.46,换手 3.4%)

| | train | valid |
|---|---|---|
| 原式可交易信号对 K 取残差:多头腿毛超额 | +3.9% | +1.4% |
| 60 日均值版对 K 取残差:多头腿毛超额 | +2.0% | −3.1% |
| 120 日均值版对 K 取残差 | 0.0% | +1.6% |
| K 单独(同一批格子):净超额 / 纯多头夏普 / 多头回撤 | +13.0% / 1.83 / −9.2% | +22.3% / 3.46 / −4.5% |
| 0.5·秩(60 日均值版) + 秩(K) | +13.4% / 2.01 / −8.1% | +21.2% / 3.55 / −4.1% |
| 秩(60 日均值版) + 秩(K) | +12.7% / 1.93 / −8.1% | +20.2% / 3.57 / −3.8% |
| K 最高十分位内部按原式分三组(低 → 高)的超额 | +12.2% / +18.9% / +19.8% | +26.0% / +27.4% / +25.9% |
| 原式最高十分位内部按 K 分三组(低 → 高) | −0.6% / +11.6% / +17.4% | −4.7% / +14.5% / +25.2% |

残差的多头腿在 0~4 个点之间、valid 上更低;与 K 相加,净超额不升(train +0.4、valid −1.1),纯多头夏普高 0.1~0.2、回撤浅 0.4~1.1 个点 —— 全在噪声带(±3 个点、±0.3)以内。
反过来看更直接:**原式多头十分位里 K 排名最低的三分之一,超额是 −0.6% / −4.7%** —— 原式的多头腿是靠它里面「恰好也是低成交额」的那部分股票撑起来的。
H4(多头腿是已知家族的子集)在 train / valid 上基本成立。

**8. 空头腿里「买不进的票」**(H12):空头十分位里次日开盘封涨停的格子占 0.76% / 0.40%(全体 0.16% / 0.08%,多头十分位 0.08% / 0.05%)。
改用不带过滤的标签:空头腿毛超额 +32.5% → **+24.1%**(train)、+30.3% → +26.9%(valid);扣费多空夏普 2.81 → **1.83**、3.16 → 2.69。
用户表里那一行的多空夏普(训练 2.89)有大约 1.0 是这个口径造成的。多头腿不受影响(毛超额的变动来自基准)。


## 3. 研究过程与逻辑(从对话记录里抽的动作时间线;每条是研究员给自己那条命令写的说明)

- 10-04 12:03 [看] Inspect existing config, notes, studies, runs and ledger for F107
- 10-04 12:03 [跑] List server-side tags already run for F107  〔study.sh list F107_abs_demean_skew_low 2〕
- 10-04 12:03 [看] Show full ledger entries and existing probes file
- 10-04 12:03 [跑] Print baseline digest for F107  〔study.sh digest F107_abs_demean_skew_low S0_baseline 2〕
- 10-04 12:04 [看] Show how F107 relates to batch factors, controls and known families
- 10-04 12:04 [跑] Print operator dossier, SSA decomposition and lab priors  〔study.sh decompose F107_abs_demean_skew_low 2〕
- 10-04 12:05 [跑] Read kernel source for day_skew, cs_demean, abs_  〔study.sh src day_skew cs_demean abs_ 2〕
- 10-04 12:05 [看] List available day_ operators
- 10-04 12:05 [跑] Try reading the _skew helper source and inspect study.sh  〔study.sh src _skew 2〕
- 10-04 12:05 [看] List project layout and inspect remote_tools functions
- 10-04 12:05 [跑] Read source of skew-related kernels to reach the _skew helper  〔study.sh src cs_skew cross_skew day_skew_masked day_kurt day_std 2〕
- 10-04 12:05 [看] List skew, demean and cross-sectional operators
- 10-04 12:06 [跑] Read nanskew_last and in_skew_full sources to expose the _skew helper  〔study.sh src nanskew_last in_skew_full 2〕
- 10-04 12:06 [看] Locate the local AlphaCube checkout path
- 10-04 12:06 [看] Read the local copy of the _skew and _stddev helpers
- 10-04 12:06 [跑] Read server div kernel and compare with local copy  〔study.sh src div 2〕
- 10-04 12:06 [看] Read local ema_rows and long_short_weights implementations
- 10-04 12:06 [看] List configs and view stage syntax of a prior study config
- 10-04 12:06 [看] Skim lab findings ids and claims
- 10-04 12:07 [看] List notes and study scripts from prior studies for format reference
- 10-04 12:07 [看] Read a prior pre-registration note and an example analysis script
- 10-04 12:07 [看] Read the rest of a prior anatomy analysis script for tool usage patterns
- 10-04 12:08 [看] List cross_ day-axis operators and elementwise/cross-sectional operators
- 10-04 12:08 [跑] Read kernel sources of cross_mean, cross_med, cs_rank, cs_regres, pairwise_min  〔study.sh src cross_mean cross_med cs_rank cs_regres pairwise_min 2〕
- 10-04 12:09 [看] Outline the PanelSet class in panels.py
- 10-04 12:09 [看] Read PanelSet init, target, external, compute and split_slice
- 10-04 12:09 [看] Outline runner.py functions and holdout/final handling
- 10-04 12:09 [看] Read the core of runner.run to learn metric and diagnostics computation
- 10-04 12:12 [看] Locally parse candidate expressions with the local AlphaCube grammar
- 10-04 12:15 [写] studies/F107_abs_demean_skew_low/x1_anatomy.py
- 10-04 12:16 [看] Fix import order and run the anatomy script on mock data locally
- 10-04 12:16 [看] Run the anatomy script on mock data with PYTHONPATH set
- 10-04 12:16 [看] Show mock output for sections 7 to 9
- 10-04 12:18 [写] notes/F107_abs_demean_skew_low/05_hypotheses.md
- 10-04 12:18 [跑] Check server status and launch the anatomy script on the server  〔study.sh exec F107_abs_demean_skew_low x1 x1_anatomy.py 2〕
- 10-04 12:18 [看] Read prior study notes 01, 03, 04, 06 for style reference
- 10-04 12:18 [看] Extract baseline sweep, by-year and book details from the S0 JSON
- 10-04 12:18 [跑] Wait for the anatomy script on the server and print its output  〔study.sh wait F107_abs_demean_skew_low x1 540 2〕
- 10-04 12:28 [写] notes/F107_abs_demean_skew_low/04_grammar.md
- 10-04 12:28 [跑] Wait again for the anatomy script to finish  〔study.sh wait F107_abs_demean_skew_low x1 540 2〕
- 10-04 12:32 [看] Read sections 0 to 3 of the anatomy log
- 10-04 12:33 [看] Outline the local AlphaCube engine kernels module
- 10-04 12:33 [看] Read apply_cube, apply_panel and engine chunking logic in the local copy
- 10-04 12:33 [看] Read engine leaf loading, masking and cube chunk execution in the local copy
- 10-04 12:34 [看] Verify the numpy rolling mean against brute force and the torch kernel locally
- 10-04 12:34 [跑] Read nanmean_last source on the server and the local panel-round code  〔study.sh src nanmean_last cross_max 2〕
- 10-04 12:35 [看] Read sections 4 and 5 of the anatomy log
- 10-04 12:36 [看] Read sections 6 and 7 of the anatomy log
- 10-04 12:36 [看] Read section 8 of the anatomy log on increment over known family
- 10-04 12:38 [跑] Get the propose draft of candidate experiments for the tree  〔study.sh propose F107_abs_demean_skew_low 2〕
- 10-04 12:39 [跑] Read kernel sources for cs_normalize, cross_decay_linear, cross_delay  〔study.sh src cs_normalize cross_decay_linear cross_delay 2〕
- 10-04 12:40 [跑] Add stages S1 and S2 to the config and validate expressions on the server  〔study.sh check F107_abs_demean_skew_low 2〕
- 10-04 12:41 [跑] Rerun the config check and show only the validation lines  〔study.sh check F107_abs_demean_skew_low 2〕
- 10-04 12:42 [跑] Launch stages S1 and S2 on the server in one run  〔study.sh run F107_abs_demean_skew_low S12 S1_parts S2_memory 2〕
- 10-04 12:44 [写] studies/F107_abs_demean_skew_low/x2_elevate.py
- 10-04 12:45 [看] Run the x2 script on mock data and check for section failures
- 10-04 12:45 [看] Self-check rolling correlation, beta and compact mean against brute force
- 10-04 12:45 [跑] Wait for the S1+S2 run and print its digest  〔study.sh wait F107_abs_demean_skew_low S12 540 2〕
- 10-04 12:55 [写] notes/F107_abs_demean_skew_low/02_operators.md
- 10-04 12:55 [写] notes/F107_abs_demean_skew_low/03_decomposition.md
- 10-04 12:55 [跑] Wait again for the S1+S2 run and print its digest  〔study.sh wait F107_abs_demean_skew_low S12 540 2〕
- 10-04 13:05 [看] Check which Partura jobs are running on the server
- 10-04 13:05 [写] notes/F107_abs_demean_skew_low/06_baseline.md
- 10-04 13:06 [写] notes/F107_abs_demean_skew_low/07x_1_anatomy.md
- 10-04 13:07 [跑] Wait again for the S1+S2 run and print its digest  〔study.sh wait F107_abs_demean_skew_low S12 540 2〕

### 研究员对这棵树的理解(原文照录 `notes/F107_abs_demean_skew_low/02_operators.md`)

读源码(`study.sh src`,以及 x1 §0 在服务器上打印的 `common._skew`)时发现的、探针表里看不出来或者和名字不一样的事:

1. **`day_skew(Low)` 不是「收益的偏度」,是价格水平占用分布的偏度。** 内核是
   `mean(((x − nanmean(x)) / sqrt(nanmean((x − nanmean(x))²)))³)`:总体矩、不做小样本修正、对 NaN 分钟用 `nanmean` 跳过。
   喂给它的是 241 根分钟最低价的**水平**,所以它读的是「价格在各个价位上待了多久」:
   负偏 = 全天大部分时间在高位、短暂下探(封涨停、探底回升后横在高位);正偏 = 大部分时间在低位、短暂冲高(冲高回落、封跌停、尾盘拉升)。
   探针 `pinned_path_response` 用两点路径核对过解析式 `(1 − 2p) / sqrt(p(1 − p))`:钉在高位 80% / 90% / 98% 的分钟 → −1.51 / −2.67 / −6.73(实测与解析逐位一致)。
   它不看分钟顺序(探针:打乱分钟不变)、不带尺度(齐次度 0)、平移不变、取负后变号。
2. **除法没有保护。** `_skew` 里用的是 `common.div` = `torch.divide`,分母是路径自己的标准差。全天价格一动不动的路径(一字板)得到的是
   0/0 = NaN,或者 float32 求均值的舍入残差被自己归一化之后的 **恰好 ±1**(探针 `constant_row_output`:CPU 上 10 个常数行里 5 个 NaN、5 个 ±1,GPU 上 8 个 NaN)。
   真实数据上(x1 §1,utrain):这类全天不动的格子占有标签格子的 0.20%,其中 73.5% 是 NaN,其余是 ±1;`\|A\|` 恰好等于 1 的格子占全部有限格子的 0.16%。
   量很小,但它们**不是 0** —— 一字板的偏度读数是垃圾值而不是「极端」。原式抓到封板靠的是「钉住但不是全天不动」的那些日子(下一条),不是一字板。
3. **`cs_demean` 减的是当天所有有限值的截面均值**(`x − nanmean(x)`,不看市值、不看是否可交易之外的任何过滤)。
   x1 §0b 用 numpy 复算 `\|A − 行均值\|`,与引擎面板最大差 8.6e-07、NaN 位置完全一致。这个均值不小:见 03_decomposition。
4. **`study.sh src` 展不开 `C._skew`**(内核通过模块别名 `C.` 调用,工具只追本模块全局名)。绕法:x1 开头用 `inspect.getsource` 在服务器上打印;
   本机那份 AlphaCube 的 `_skew` 与服务器逐字相同,但那不是依据 —— 依据是服务器打印的源码加上探针在服务器内核上的两点解析核对。
5. 候选里用到的日轴算子:`cross_mean(x, d)` = 对左侧用 NaN 补齐的 d 日窗口取 `nanmean`(窗口不满也给值,NaN 日被跳过);`cross_med` / `cross_max` 同一骨架换成 `nanmedian` / `nanmax`;
   `cross_delay(x, d)` 是把日频量往后挪 d 天。`cs_rank` 给的是 (0, 1] 的百分位秩,并列按股票顺序稳定排序。
   **引擎算出来的 `cross_mean(原式, 30)` 与「对缓存的原式面板做滚动 nanmean」不是同一个面板**(x1 §0b:日截面 Spearman 0.9989、有限值位置 0.27% 不一致、最大差 12.6)——
   原因在 x2 §a 里查,结论写在 07x_2_elevate。


### 研究员对这棵树的理解(原文照录 `notes/F107_abs_demean_skew_low/03_decomposition.md`)

分解表之外需要写成公式的:记第 d 天第 s 只股票的 241 根分钟最低价为 L(s,d,m),当天的均值、标准差(总体)为 L̄、σ,

```
A(s,d) = mean_m( ((L(s,d,m) − L̄) / σ)³ )          价格水平占用分布的偏度(不是收益偏度)
B(s,d) = A(s,d) − mean_s A(·,d)                    减去当天全市场的平均偏度 μ(d)
C(s,d) = |B(s,d)|                                   原式;方向为负,做多 C 小的
交易的是 EMA_20( −C )                               记忆在表达式外面
```

几个要到数据上才看得见的量(x1 §1,utrain,有标签的格子):

- **A 的分布是厚尾、左偏的**:分位数 0.1% −9.68、1% −2.57、5% −1.50、中位数 −0.01、95% +1.35、99% +2.20、99.9% +4.61。
  241 根里只有一根不同的路径,`\|A\|` 的上界是 (n−2)/√(n−1) ≈ 15.4;随机游走路径的 `\|A\|` 均值约 0.39(探针,连续价格)。
- **`\|B\|` 的中位数 0.46,但截面总和的一半在尾部**:`\|B\| ≥ 1` 的格子占 18.6%、携带截面 `\|B\|` 总和的 49%;`≥ 2` 的占 3.2%、携带 16.5%;`≥ 3` 的占 0.9%、携带 8.2%。
  EMA 是线性的,所以可交易信号里一次 `\|B\| = 5` 的日子要 20 多个交易日才衰减到平常水平 —— 短头一端由事件决定。
- **谁在尾部**:「钉在高位」(分钟最低价的中位数等于全天最高值,即半数以上分钟在最高价位)的格子占 0.79%,平均 A = −4.28,其中 84% 当天收盘涨幅超过 9% —— 封涨停;
  「钉在低位」占 0.33%(平均 A = +3.46,35% 当天跌幅超过 9%);全天不动占 0.20%。`\|B\| ≥ 2` 的格子里钉在高位 / 低位 / 全天不动的合计只占 22%,
  其余 78% 是「没有封死但大部分时间挤在一头」的普通路径(一跳之后横盘、盘中短暂脉冲)。
- **μ(d) 不小**:逐日截面均值的 5% / 25% / 50% / 75% / 95% 分位是 −0.58 / −0.22 / −0.03 / +0.15 / +0.39,截面标准差的中位数 0.98;
  `\|μ\| / 标准差` 的中位数 0.19,**37% 的交易日超过 0.25、11% 超过 0.5**。全市场当天是「早盘拉升后横盘」还是「尾盘跳水」,所有股票的偏度会一起偏。
  所以 `\|A − μ\|` 与 `\|A\|` 不是一回事:逐日秩相关 0.786,各自做 20 日 EMA 之后 0.903。这一刀对多头腿的影响见 07_S1_parts。
- **价格是复权价**(收盘价落在 0.01 网格上的只有 24%),所以「一天跨了几个 tick」只能近似量:全天不动 0.20%、振幅不超过 0.02 元(复权后)的 0.08%,
  低价股网格伪影(H8)涉及的格子不到 0.3%。
- **年份漂移**:`\|B\|` 的截面均值从 2018 年的 0.55 升到 2021 年的 0.71,`\|B\| ≥ 2` 的占比从 1.9% 升到 4.1%(2020 年 8 月创业板涨跌幅放宽到 20% 之后,
  「大部分时间挤在一头但没封死」的路径变多了);钉住的占比 2020 年最高(1.76%)。


### 研究员对这棵树的理解(原文照录 `notes/F107_abs_demean_skew_low/04_grammar.md`)

这棵树的语法只有三层,没有日轴上的任何记忆:

```
分钟最低价 Low 的**水平**序列(241 根)
    -> 日内折叠:这 241 个价位的总体偏度(「价格在各个价位上待了多久」的不对称度;不带尺度、不看分钟顺序)
        -> 截面:减去当天全市场的平均偏度(去掉「今天大盘是先涨后平还是尾盘拉升」这个共同形状)
            -> 逐元素取绝对值(折叠:偏向哪一边不管,只留偏离了多少)
```

读这棵树要记住的结构性事实:

1. **没有任何日轴算子**。表达式是「当天」的读数,逐日抖得很厉害:原始面板的十分位纯多头书日换手 90%,扣费多头腿净超额 −63%(S0,半衰期 0)。
   用户表里那一行靠的是表达式**外面**的 20 日半衰期 EMA,而且 20 是可选集合的上界(半衰期扫描从 0 到 20 单调改善)。
   被交易的东西是「最近一两个月里,这只股票的日内路径形状有多常、多大程度地偏离全市场」这个慢变量,记忆不在树里。
2. **三个节点都不带尺度**:`day_skew` 齐次度 0、平移不变(价格乘 10、加 5 都不变),`cs_demean` 与 `abs_` 齐次度 1 但作用在一个无量纲量上。
   所以这棵树里**没有任何一处直接读到成交额、价格水平或波动的大小** —— 它与这些已知暴露的关系只能是间接的
   (高波动、高换手的股票更常出现「一跳到位」「封板」这类路径)。这与 F001 家族(成交额水平直接进表达式)是不同的通道。
3. **折叠在截面去均值之后**。`abs_(cs_demean(x))` 与 `abs_(x)` 的差别取决于当天截面均值有多大(探针 `abs_reorders_after_shift`:
   偏移 0.1 个截面标准差时两者秩相关 0.978,0.25 个时 0.88,0.5 个时 0.62)。它是不是必需的节点,要到真实数据上看当天均值 / 标准差的分布(x1 §1)。
4. **折叠之后,任何单调的控制变量在秩空间里都很难线性地解释它**。S0 的中性化 R²(0.214)只能当下界读;
   要判断它是不是已知暴露,得用同样折叠过的控制变量、控制变量的平方项,以及与这棵树对应的读数(钉住日频率、分钟收益峰度)去量(x1 §7)。


## 4. 假设表

下面是研究员在跑实验**之前**写的假设表(原文照录 `notes/F107_abs_demean_skew_low/05_hypotheses.md`)。**其后的实验结果没有回填**:
每条假设现在是「未验证 / 被支持 / 被否定」,要对照第 2 节列出的运行结果重新判定。

### 竞争性假设(在任何阶段实验之前写下;此时手里只有 S0 基线、探针实测和算子源码)

记号:`A = day_skew(Low)`(分钟最低价**水平**的占用分布偏度),`B = cs_demean(A)`,原式 `= \|B\|`,方向 −(做多 `\|B\|` 小的),
实际交易的是 `EMA20(−\|B\|)`。「多头腿」一律指扣 15 bp 之后的纯多头超额;S0 里它是 +1.1% / +3.0%(train / valid,毛 +9.4% / +11.4%,日换手 10.9%)。

| # | 假设 | 它预测什么 | 哪个实验能杀死它 |
|---|---|---|---|
| H1 | **尾部事件**:信号来自少数「钉住」的日子(涨跌停板、一跳到位),这些天 `\|A\|` 是 2~7(探针:钉住 90% 的分钟 → −2.67),EMA20 把「最近一个月有过钉住日」变成慢状态;空头腿就是打板 / 彩票股之后的跑输 | `\|B\|≥2` 的格子大半是钉住日;空头十分位里绝大多数股票 20 日内有过这种日子;把 `\|B\|` 换成指示量 `1{\|B\|>c}` 能复现空头腿;把尾部截掉(`min(\|B\|, 1)`、截面秩)多空夏普明显掉 | x1 §1 / §4 / §6:截尾或取秩之后多空与空头腿不掉 → H1 不是主因;钉住日占 `\|B\|≥2` 的比例很低 → 「钉住」这个读法不成立 |
| H2 | **主体形状**:信息在分布的主体 —— 平常日子里 `\|B\|` 长期偏小 / 偏大的股票,尾部只是噪声 | 截尾、取秩之后 rank IC 与多头腿不降反升(尾部被 EMA 记 20 天是噪声);只留指示量则多头腿的排序消失 | x1 §4:截尾 / 取秩版本的多头腿明显变差 → H2 不成立 |
| H3 | **已知暴露(波动 / 换手 / 彩票)**:`−\|B\|` 是「低波动、低换手」的带噪声代理(与 `ctl_dvol20` 秩相关 −0.38,全部控制变量 R² 0.214) | 对控制变量(含与这棵树对应的:分钟收益峰度、钉住频率、折叠过的控制)中性化后,残差的 rank IC、多头腿毛超额都消失 | S0 已经给了一半答案:残差空头腿 +32.5% → +4.6%(几乎全没),但**残差多头腿毛超额 +9.4% → +8.2%**(几乎没动)。x1 §7 用折叠过的 / 树特有的控制变量再量一次:多头腿毛超额仍在 → H3 只解释空头腿 |
| H4 | **已知家族(成交额水平)**:多头腿就是低成交额溢价 | 对 `cross_mean(day_std(Amt), 30)` 取残差后多头腿毛超额消失;与已知家族相加不比已知家族单独好;在已知家族的多头端内部,本因子不再给收益排序 | x1 §8:残差多头腿仍为正、且已知家族多头端内部按本因子分三组收益单调 → 有增量;否则没有 |
| H5 | **折叠是对称的**:`abs_` 之所以对,是因为正偏(多数时间在低位、短暂冲高)和负偏(多数时间在高位、短暂下探 / 封涨停)两头一样差 | `EMA20(B)`(带符号)的十分位剖面是对称的倒 U;`B⁺`、`B⁻` 单边各自的书差不多 | x1 §2 / §3 / §4:一边明显更差 → 折叠丢了方向信息,单边或带倾斜的版本更纯 |
| H6 | **`cs_demean` 是多余的**:截面均值相对截面标准差很小,`\|A − 均值\| ≈ \|A\|`(探针:偏移 0.1 个标准差时秩相关 0.978,0.25 个时 0.88) | 真实数据上逐日 `\|均值\| / 标准差` 多数日子 < 0.25;`\|A\|` 的书与原式在噪声内相同,可交易信号秩相关 > 0.95 | x1 §1 / §4、S1:`\|A\|` 明显更差 → 「相对全市场当天的形状」是必需的(支持 H7) |
| H7 | **共同路径份额**:`\|B\|` 小 = 这只股票当天的路径跟着大盘走(自有份额小)。探针说这个映射很快饱和(自有份额 25% 时已到 0.27,100% 时 0.38),所以预期它**不是**主因 | 可交易信号与「分钟收益和全市场分钟均值收益的日内相关」的 20 日均值秩相关高(>0.4);后者自己当因子能复现多头腿 | x1 §4 / §7:秩相关 < 0.2 且它的书不像原式 → H7 不成立 |
| H8 | **价格网格 / 常数路径的伪影**:低价、低波动股票一天只在 2~3 个价位上跳,`\|A\|` 被网格单独抬高(探针:≤3 个价位时均值 0.72 对 0.39);全天不动的路径输出 ±1 或 NaN(float 舍入垃圾) | 跨 ≤2 个 tick 的格子占比不小且其 `\|A\|` 均值明显偏高;信号与价格水平、tick 数相关 | x1 §1:这类格子占比 < 1%,或把它们换成中性值后书不变 → 伪影不重要(S0:与 `ctl_price` 秩相关只有 −0.09,预期不重要) |
| H9 | **三阶矩不是必需的**:任何「价格水平占用分布的不对称度」都行,比如有界的 `(max + min − 2·median) / (max − min)` 或时间平均位置 `(mean − min) / (max − min)`,同样折叠 | 这些有界读数与原式秩相关高、书相同或更好(有界 → 没有厚尾 → 多头端排序更稳) | x1 §4、S1:有界读数明显更差 → 偏度对尾部的放大本身是信号的一部分(与 H1 一致) |
| H10 | **字段是偶然的**:Low / Close / High 的分钟序列是同一条路径 | `\|cs_demean(day_skew(Close))\|` 等与原式秩相关 > 0.9,书在噪声内相同 | x1 §4、S1 |
| H11 | **时间尺度(平滑)**:原始日频面板基本是噪声(rIC 0.018,平滑后 0.034),半衰期选到了网格上限 20,衰减表的 rank IC 一路升到 h20(0.062)—— 这是个慢变量,20 还不够长 | 把记忆写进表达式(`cross_mean(·, 60 / 120)`)后换手再降一半以上、多头腿毛超额不掉,净超额在 train 和 valid 上都升 | x1 §5、S2:窗口拉长后毛超额跟着掉、净超额不升 → 20 已经是合适的尺度。**若成立,改进记在「平滑」名下,不是结构** |
| H12 | **空头腿被买不进的票抬高**:空头十分位里次日开盘封涨停(标签 NaN、记 0)的票多 | 用不带「买不进」过滤的标签重算,空头腿毛超额与多空夏普明显下降 | x1 §9(只影响多空口径;多头腿不受影响) |

**四个必须回答的问题,开工前的预判**

- *是不是已知暴露的另一种写法*:空头腿很可能是(H3:`ctl_dvol20` 一个变量就把空头腿从 +32.5% 压到 +4.9%);多头腿不像(对全部控制变量取残差后毛超额还有 +8.2%)。
  但原式里有 `abs_` 折叠,秩空间的线性中性化看不见非单调关系(playbook §6.5),所以 S0 的 R² 0.214 是下界,x1 §7 要用折叠过的控制变量和各控制变量的平方项重量。
- *钱为什么主要在空头腿*:Q1 是 −32.7% / −31.0%,Q2 只有 −6.3% / −8.7% —— 最差的十分位远离其余九个,像是「事件」而不是「梯度」(H1);加上 H3(高波动高换手)和 H12(买不进的票记 0)。
- *分位剖面是否单调*:是。train −32.7 −6.3 −0.8 +1.9 +1.5 +4.8 +5.5 +7.8 +8.8 +9.6;valid −31.0 −8.7 −3.6 −0.4 +3.7 +5.9 +6.0 +6.1 +10.2 +11.8。
  多头端是一段平缓的梯度(Q8~Q10 都在 +6%~+12%),不是事件。所以多头腿和空头腿很可能是**两种机制**:空头腿 = 尾部事件(H1),多头腿 = 主体(H2)。
- *哪些节点可能多余*:`cs_demean`(H6)、字段 `Low`(H10)、三阶矩本身(H9)。`abs_` 预期是必需的(H5 要先成立)。

**对只能做多的用户,真正要回答的是 H11 和 H4**:多头腿毛超额有 +9%~+11%,但 10.9% 的日换手吃掉了 8 个点;
已知家族 `cross_mean(day_std(Amt), 30)` 在同一口径下是 +12.6% / +22.3%(换手 3.4%)。这条因子要有用,必须(a)把换手降下来而毛超额不掉(H11),
并且(b)它的多头腿不是已知家族的子集(H4 被杀死)。

## 5. 当前的候选(提纯 / 升华)

(没有留下。研究还没进行到选候选的阶段,或者候选只在研究员脑子里。)

## 6. 后面的研究思路(研究员已经写进配置和脚本、但还没做完的)

- 阶段 **S0_baseline**(已有结果):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
    - `v_base` = `abs_(cs_demean(day_skew(Low)))` —— 原始表达式
- 阶段 **S1_parts**(**还没有结果**):原式三个节点(偏度、截面去均值、折叠)和字段各自是不是必需的?它是不是「日频 |特质收益|」「分钟收益峰度」这类朴素读数的另一种写法?
    - `p_signed` = `cs_demean(day_skew(Low))` —— H5:去掉折叠。若两头都差(倒 U),带符号的版本应该塌掉;若它不塌,折叠丢了方向信息
    - `p_nodemean` = `abs_(day_skew(Low))` —— H6:去掉截面去均值。x1 §1:当天截面均值/标准差 37% 的日子超过 0.25。H6(去均值多余)预测书不变;x1 的 numpy 版本说多头腿毛超额从 9.4% 掉到 3.4% —— 用引擎坐实
    - `p_znorm` = `abs_(cs_normalize(day_skew(Low)))` —— 去均值之外再除以当天截面标准差:日内同序,但改变了各天在 EMA 里的权重。若截面离散度大的日子(行情极端的日子)才是信号来源,它应该变差
    - `p_close` = `abs_(cs_demean(day_skew(Close)))` —— H10:字段 Low 换成 Close。若 Low 只是同一条路径的另一种采样,书在噪声内相同、秩相关 > 0.9
    - `p_range` = `abs_(cs_demean(div(sub(add(day_max(Low), day_min(Low)), add(day_median(Low), day_median(Low))), sub(day_max(Low), day_min(Low)))))` —— H9:三阶矩换成有界的不对称度 (max+min-2*median)/(max-min)。没有厚尾。H9(三阶矩不必需)预测多头腿不降;空头腿若明显变弱,说明偏度对尾部的放大是空头腿的来源(H1)
    - `p_rank` = `cs_rank(abs_(cs_demean(day_skew(Low))))` —— H1/H2:逐日取截面秩再平滑,尾部被压平。H2(多头腿在主体)预测多头腿毛超额不降;H1(空头腿在尾部)预测多空夏普与空头腿大降
    - `p_cube` = `pow_3(abs_(cs_demean(day_skew(Low))))` —— H1/H2 的另一头:立方把权重全压到尾部事件上。H1 预测空头腿不降;H2 预测多头腿的排序变差(多头端只剩「没出过事」这一条信息)
    - `r_absret` = `abs_(cs_demean(div(day_last(Close), cross_delay(day_last(Close), 1))))` —— H3 的直接替换实验:完全不看日内路径,只用日频 |特质收益|(同样的去均值+折叠)。x1 §7:它的 20 日 EMA 与原式可交易信号秩相关 -0.54、单独就把残差多头腿毛超额压到 2.9%。若它的书复现原式,原式就是特质波动的带噪声写法
    - `r_kurtret` = `day_kurt(Ret)` —— H1 的朴素等价物:分钟收益的峰度(跳价 / 封板日同样极端)。若空头腿相同而多头腿不同,说明原式的多头腿不来自「跳价」这一维
    - `r_kurtlow` = `day_kurt(Low)` —— 同一条价格水平路径的四阶矩:x1 里它的 EMA20 与原式可交易信号秩相关 -0.78,多头腿毛超额却是 0。它是用来说明「原式的多头腿不在与峰度共享的那部分里」的对照
    - `r_mktcorr` = `day_corr(Ret, nt_cs_mean(Ret))` —— H7:直接量「跟不跟大盘走」(分钟收益与全市场分钟均值收益的日内相关,方向预期为正)。若原式的多头腿就是同步性,它应该复现多头腿且秩相关高
- 阶段 **S2_memory**(**还没有结果**):把日轴记忆写进表达式之后,多头腿净超额的改善有多大、来自平滑还是结构?记忆该是均值、中位数还是极值,窗口多长最稳?
    - `m10` = `cross_mean(abs_(cs_demean(day_skew(Low))), 10)` —— H11:窗口邻域的短端。与原式在同一固定半衰期下比,看结构(等权窗口)本身有没有贡献
    - `m20` = `cross_mean(abs_(cs_demean(day_skew(Low))), 20)` —— H11:x1 里 mean20 + 半衰期 20 是 train/valid 最均衡的一个(+5.0% / +7.5%)。预测:多头腿净超额两段都比原式高 3 个点以上,毛超额不升(改进来自换手)
    - `m30` = `cross_mean(abs_(cs_demean(day_skew(Low))), 30)` —— H11:邻域
    - `m60` = `cross_mean(abs_(cs_demean(day_skew(Low))), 60)` —— H11:x1 里 +6.0% / +6.6%。预测同 m20;若 m60 明显好于 m20,慢变量的尺度比一个月更长
    - `m120` = `cross_mean(abs_(cs_demean(day_skew(Low))), 120)` —— H11 的长端:x1 里 train 降(+4.6%)而 valid 升(+9.7%),两段不同向。它是用来看「更长」是否已经过头的
    - `md60` = `cross_med(abs_(cs_demean(day_skew(Low))), 60)` —— H2:记忆换成中位数,尾部事件完全不进来。H2(多头腿在主体)预测多头腿不降;若多头腿明显变差,多头端需要「最近没出过事」这条排除信息
    - `mr60` = `cross_mean(cs_rank(abs_(cs_demean(day_skew(Low)))), 60)` —— H2:先取截面秩再求 60 日均值(尾部压平但仍计数)。与 m60、md60 一起看尾部在多头腿里起多大作用
    - `mx20` = `cross_max(abs_(cs_demean(day_skew(Low))), 20)` —— H1:记忆换成 20 日极值(只记最出格的一天)。若多头腿只是「最近没出过事」,它应该与 m20 一样好;若多头腿需要主体的平均水平,它会差
    - `m60_nodemean` = `cross_mean(abs_(day_skew(Low)), 60)` —— H6 在慢尺度上:60 日平均之后,当天的截面均值还重不重要?若仍然明显更差,「相对全市场当天的形状」是多头腿的实质
    - `m20_absret` = `cross_mean(abs_(cs_demean(div(day_last(Close), cross_delay(day_last(Close), 1)))), 20)` —— H3:朴素的日频 |特质收益| 配上同样的 20 日记忆。它与 m20 的多头腿之差,就是日内路径形状在特质波动之外多给的东西
    - `m60_absret` = `cross_mean(abs_(cs_demean(div(day_last(Close), cross_delay(day_last(Close), 1)))), 60)` —— 同上,60 日
- 脚本 `studies/F107_abs_demean_skew_low/probes.py`:Probes this tree needs: abs_(cs_demean(day_skew(Low))).

The tree is "a moment of the intraday PRICE-LEVEL path -> minus the cross-sectional
mean -> magnitude".  None of the built-in probes answers what one needs to know
to read it:

* ``pinned_path_response`` -- day_skew is fed a price LEVEL, so it is a statistic
  of how long the price sat at each level (an occupancy distribution), not of
  returns.  What does it read on a day the price is pinned at one extreme for a
  fraction p of the minutes (a limit board, a one-jump day)?  Analytic answer for
  a two-point path: (1-2p)/sqrt(p(1-p)).
* `
- 脚本 `studies/F107_abs_demean_skew_low/x1_anatomy.py`:x1 -- what  abs_(cs_demean(day_skew(Low)))  reads on REAL data, and where its long leg comes from.

No stock diagnostic answers these, and the stage plan depends on the answers:

  0. helper sources the `src` tool cannot show (common._skew), and two self-checks of this script
     (numpy |A - rowmean(A)| == the engine's panel;  numpy rolling nanmean == the engine's cross_mean)
  1. day_skew(Low) on real data: heavy tails, constant paths (+-1 / NaN garbage), tick-grid levels,
     pinned paths; how big the cross-sectional mean is next to the cross-sectional sd (does cs_demean matter?)
  2. even
- 脚本 `studies/F107_abs_demean_skew_low/x2_elevate.py`:x2 -- can the long leg of  abs_(cs_demean(day_skew(Low)))  be made better by STRUCTURE (not only by smoothing)?

x1 left four leads that only make sense for this tree, plus one engine discrepancy to chase:

  a. forensics: the engine's cross_mean(base, N) is not the rolling nanmean of the cached base panel
     (x1 0b: Spearman 0.9989, max abs diff 12.6).  Where, and why?
  b. the fold centre: at the event level the best next-day bucket is B in (-0.5, -0.25], not B = 0, and the
     positive side is a slope while the negative side is a cliff.  Shifted folds |B - c| and tilted folds |B| + lam*B

## 7. 留出段

未读。读之前要先在 `10_distilled.md` 里写下候选排序和判据。

## 8. 给接手者的提醒

- `S12`(10-04 12:42 用 run 启动)在服务器上跑着或已跑完,**结果没人读过**:`./scripts/study.sh wait F107_abs_demean_skew_low S12` 拉回来看。
- 上一位研究员的完整动作流水(含每条命令的输出):`handoff/F107_abs_demean_skew_low/agents/`。
- 这一页是自动汇编的;你读完材料、形成判断之后,**按 playbook §7 的 8 节把它整个重写**。
