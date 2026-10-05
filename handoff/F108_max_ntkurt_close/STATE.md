# F108_max_ntkurt_close — 交接状态

_自动生成于 2026-10-05 13:33(`python scripts/recorder.py --brief F108_max_ntkurt_close` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #3264(批次 B01_single_factors)
- 表达式:`day_max(pow_1_5(pow_2(nt_ts_kurt(Close, 30))))`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- **留出段已经读过 2 次**(10-05 11:16, 10-05 12:13)—— **不许再读**。候选在留出段上的数全在 `runs/F108_max_ntkurt_close/final.json`(`./scripts/study.sh digest F108_max_ntkurt_close final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `work:F108_max_ntkurt_close#1`:已返回结果,最后动作 10-05 00:02 → `handoff/F108_max_ntkurt_close/agents/work_R1_af1297d4e49a82489.md`
  - `lead:F108_max_ntkurt_close#2`:中断,最后动作 10-05 00:20 → `handoff/F108_max_ntkurt_close/agents/lead_R2_a7c78c9c449a0151b.md`
  - `synth:F108_max_ntkurt_close`:已返回结果,最后动作 10-05 11:00 → `handoff/F108_max_ntkurt_close/agents/synth_a3d74598652f5a146.md`

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F108_max_ntkurt_close` 看服务器上的 tag,`./scripts/study.sh digest F108_max_ntkurt_close <tag>` 重看结果)。

## 研究现状(`notes/F108_max_ntkurt_close/state.md`,10-05 10:57 更新)—— **先读这个文件**

# F108_max_ntkurt_close 研究现状(每轮整个覆盖重写;接手先读这一页)

`day_max(pow_1_5(pow_2(nt_ts_kurt(Close, 30))))`,真实形状 = **`(max_m |K_m|)³`**,K = 日内 **30 分钟** Close 的超额峰度。
最后更新:**读完批量扫描 s1 大表(87 变体)+ 市场解剖的那一轮主研**。本轮**没有起任何服务器计算**(只跑了 `hypo` 语法检查)。
研究方式已切到「成批提假设 / 成批看回测」,上一轮的单条工单流程(R0~R3)不再是主线。

## 1. 现状(一句话)

s1 大表已读完并落成 **`notes/F108_max_ntkurt_close/synthesis.md`(123 行,每个论断带变体 id 和数字)**
与 **`studies/F108_max_ntkurt_close/hypo.yaml`(32 条,32/32 parse)**。
**结论已经可以写成合格的否定结论:对只能做多的用户,这条因子作为排序器相对已知成交额族没有增量**
——六条线性 overlay 全部严格差于家族单独(ut **+14.1%** 对 **+15.4%**)。
唯一还没被否掉的用法是**筛子**(不是混合):s1 表里一条筛子形态都没有。那就是第二批(hypo.yaml 的 F 组)的主攻。

## 2. 中间结果(带数字;长表在 synthesis.md,不要从日志重刨)

train 2018–2021 / valid 20220101–20230807 / utrain = 两者;% = 年化多头腿净超额(扣 15bp),半衰期按纯多头书选。
基准 `k_known = cross_mean(day_std(Amt), 30)` = **+12.6 / +22.3 / +15.4%**,Lshp +1.78 / +3.46 / **+2.22**。

- **多头腿是零**:`v_base` hlL20 **+0.3 / +2.5 / +1.0%**,Lshp +0.05 / +0.46 / **+0.15**,LTO 4.7%;
  底腿(最高 max\|K\| 十分位)毛超额 **−30.6 / −30.0%**,LS +2.83 / +2.53。**31pp 多空差价里多头腿只拿到约 1pp。**
- **死重**:`pow_1_5`(`abl_C` ρo +0.97)、外层 `cs_winsor`(ρo +1.00)、`signedpower`(ρo +0.99)。
  **`pow_2` 不是死重,它是树里唯一的 abs**(删它 `abl_B` ut −0.6%、LTO 4.7%→7.4%)—— 这一条**修正了 R2 的 H2**。
- **`sub_A` / `abl_A` 不是提纯**:`nt_ts_var/std/delta` ρo 只 **+0.09/+0.08/+0.04**、ρk **+0.52/+0.55/+0.54**、
  ut +8.1/+7.3/+7.4%,但多头书超配「价格最低 20%」**+71.6/+74.4/+75.1pp**(`abl_A` = (当日最高价)³,+79.9pp)
  → **它们是低价书**(Close 是水平量,30 分钟方差 ∝ 价格²),而且都打不过家族。
- **折叠与窗口**:`day_first/day_open` **符号翻转**(ut −6.0%、dist 0.50 ✗ —— 读的是左侧 NaN 补齐的伪影,
  2 个点的超额峰度恒为 −2);`day_quantile` ut −19.3%;窗口 10 **翻符号**、15 **−2.9%**、30 +1.0%、60 valid −0.8%
  → **没有平台,结构脆**。
- **状态量不是事件量**:`cross_zscore` 5/10/30/60 = **−21.4/−16.2/−8.6/−5.0%**(LTO 到 29.7%);`rel60`、`fold_sq` 两段反号;
  `cross_min` 是唯一改变了对象的记忆(`mem_min60` ρo +0.26、dist 0.54、**Lshp +0.95、LTO 2.1%**,
  但 Lnet +3.7/+1.7% **在 ±3pp 噪声内**)。`cross_max` 一族(+0.9~+1.4%)全不如 `cross_min`。
- **28 条 memory 的平滑一族**全是 ρo +0.91~+0.99、ut 挤在 **+2.4~+2.8%**,hlL 从 20 掉到 1~3
  → 表达式内平滑与 EMA 半衰期是替代品,统一比 base 高约 1.5pp。按手册 §6.1 这叫「改进来自平滑」。
- **解剖(本轮最有价值的一段)**:
  流通市值五档段内 **+5.3/+5.4/+6.4/+5.7/−0.4%**,但书**超配最大档 +35.8pp**(倾斜花在零能力的那一桶);
  成交额五档段内 **−2.9/−3.5/−2.5/+6.4/+11.4%**(与市值方向相反)→ 甜点 = 小市值 × 高成交额;
  **冻结盘口段(6.5%,段等权 −67.4%)段内 +37.3%,而家族 −10.9%**;无冻结段(93.5%)段内 **−3.1%**;
  次新段(7.1%)原式 +5.0%、`mem_min60` **+12.8%**;科创板 **−13.3%**(十列全负);
  价格最低档 **−6.7%**;低波动段 **+8.4%** vs 高波动 **−6.4%**;逐年 2019/2020/2023 正,2018/2021/2022 负。

## 3. 过程与逻辑

本轮一步到底:读 s1 大表 + 算子源码(`day_max` / `pow_1_5` / `pow_2` / `nt_ts_kurt`,外加 `nankurt_last`、
`cs_bucket_rank`、`day_flat_ratio` 等)+ `docs/new_operators.md`,然后写 synthesis + hypo。没有重跑任何东西。
**提假设的逻辑**:大表已把「结构/叶子/窗口/记忆/形状/中性/叠加」六类扫过一遍,结论是**结构侧走到头了**
(窗口无平台、死重已清、换算子就换因子)。所以第二批不求「更好的峰度」,分三路:
① 用**无 EPS、无饱和**的直接状态变量(`day_flat_ratio`、`day_durbin_watson`)替掉峰度这个读数;
② 把解剖出来的两条缺陷写进表达式(规模倾斜 → 价格桶内中性;时段依赖 → 市场波动门控);
③ 做唯一没试过的形态:**筛子 / 凸罚项**,瞄准 6.5% 病态段里家族亏 10.9% 这件事。

## 4. 假设表

**第二批 = `studies/F108_max_ntkurt_close/hypo.yaml`,32 条,32/32 parse。**
A 直接状态(4)· B 尺度泄漏与 EPS(5)· C 日内折叠换频率/集中度/位置(5)· D 窗口两端(2)·
E 规模倾斜(5)· **F 筛子/凸叠加(5,优先级最高)** · G 时段门控(2)· H 慢性读数(2)· I 两条新结构(2)。
每条的 `why` 都指到 synthesis.md 的某一节。

**上一轮(R2)已定、不用再碰**:H1/H6/H7 被否定;H5 空头腿是已知暴露、多头腿不是;H6′ 机制 = 冻结盘口里的孤立价;
H9 多头端 = 大市值安静票;H10 空头腿被封板票抬高约 14%;H15 `m_mean30` 的改进来自平滑;H16/H17 死;
H18 改写为「w 在 0.15~0.4 之间都一样」;H19 结构增量 +1.2/+1.4pp(配对口径)。
**本轮修正**:H2(`pow_2` 死重)**不对**,见 §2。
**本轮发现的冲突**:R2 的 overlay 增量用的是 `D30 = cross_mean(原式, 30)` 载体 + 固定 hl0;s1 表用**未平滑原式**
载体 + 逐变体重选半衰期,得到 **−1.3pp**。**载体不同,s1 表缺 D30 那一行** → `h_ov_mean30_p025` 专门去对齐。

## 5. 候选(当前排序)

1. **什么都不推荐、写否定结论** —— 多头腿 +1.0% / Lshp +0.15,线性叠加全差于家族。这是目前证据支持的第一推荐。
2. `h_scr_hard_q25` / `h_scr_soft_pow3`(筛子形态)—— 第二批里若打过家族 +15.4%,才改推荐。
3. `mem_min60` 一族(Lshp +0.95、LTO 2.1%、dist 0.54)—— 慢性读数,Lnet 在噪声内,等第二批 H 组定性。
4. `h_ov_mean30_p025` —— **不是候选**,只是去对齐与 R2 的冲突。
5. R2 的旧第一推荐 `z_over25`(`cs_rank(K1) + 0.25·cs_rank(D30)`,hl0 +15.1%/+23.7%)—— 与 s1 表的 overlay 行冲突,
   **在 §4 的冲突解决之前不能当候选**。

## 6. 后面的思路

- 第二批回来先看 **F 组**:筛子赢不了家族,这条因子就彻底定性为「只对多空有用」,可以收口成文。
- 若 **A 组**(`day_flat_ratio` / `day_durbin_watson`)复现了原式的空头端**而且窗口有平台**,
  正确产出就不是「提纯 F108」,而是「F108 是一个有噪声的冻结盘口读数,直接写状态变量更好」——这要写进报告。
- 还没做、值得做:**按价格限幅制度切时间**(创业板 2020-08-24 改 ±20%),这是科创板 −13.3% 那条推断的直接检验;
  需要一个按板块×年份的分段诊断(表达式里写不出限幅)。
- **决定不做**:① 不为多空夏普优化;② 不在 valid 上重拟方向/半衰期/权重;③ 不做「再扫一批相近窗口」式搜索。

## 7. 留出段

**一次都没读过。** `orders/R3.md`(kind: final)是上一轮下的工单;本轮的结论把 `10_distilled.md` 的
「读留出段之前」那一节(R2 的 5 个候选)**作废**了 —— 要读留出段,必须先按本页 §5 重写事前登记(排序 + 判据)。
`brief` 若显示已读过,就**绝不**再下第二张 final 工单。

## 8. 给接手者的提醒

1. **先读 `synthesis.md`,再读本页**;`02_operators.md` / `03_decomposition.md` 里的算子事实仍然有效。
2. **名字骗人的地方**:窗口是日内 30 **分钟**;`pow_1_5`/`pow_2` 的 "signed power" 分支**只在 e ≤ 1 时生效**
   (这里走普通 `x**e`)→ `pow_2` 是 abs、`pow_1_5` 单独作用在有符号量上给 NaN;`cs_quantile_q25` 标记的是**最高** 25%;
   `pow_3` 是有符号立方;`cross_*` 窗口池没有 9(写 10),nt 面窗口池是 [3,5,10,15,30,60]。
   **`04_grammar.md` 把这棵树叫「孤立跳变探测器」是错的**(真跳变峰度**低**),写报告时要改。
3. **`nankurt_last` 的 EPS 是绝对值 1e-9**:`m4/(var²+1e-9)−3`。低价票 30 分钟价格 var² ~1e-8,与 EPS 同量级 →
   峰度被压向 −3(解剖里价格最低档 −6.7% 就是它);**任何收益尺度的叶子 var² ~1e-11 会被 EPS 完全吃掉 ——
   不要写 `nt_ts_kurt(Ret, d)`,它大概率近似常数**。这是本轮提新算子请求(相对 EPS 的峰度 / 基于 MAD 的孤立度)的原因。
4. **工具问题(先解决再跑第二批)**:`cs_bucket_rank` 的两条变体(`bk_liq`/`bk_known`)dist 只 **0.20**、被门槛判掉,
   而它的输出按定义是桶内均匀的百分位 —— 很像 dist 指标对注册标记 `[boolean_output,trivial_boolean]` 的误判。
   这会自动枪掉**整类**分桶中性化假设(用户明确要求用的手段)。hypo.yaml 里每条 `cs_bucket_rank` 都配了 `cs_regres` 版当保险。
5. **其他工具限制(R2 实测)**:`by_year`/`neutralise`/`profile` 只对本次 run 的 stage 内变体生效;
   `digest` 的固定半衰期表只有 train。**内存守卫**:x1 曾因邻居撑满容器 anon 挂掉(exit 97);
   GPU 被占时走 CPU,**NT 面约 4 分钟一条**,排队/超时只能继续 `wait`,不要重跑。
6. **口径不一致、别混用**:发布的 Lnet +5.6% 未复现(utrain + 固定 hl10 实测 −0.6%),详见 `06_baseline.md`,**不要去查来源**。
   数据从 20180102 开始、没有预热行;算子语义一律以 `study.sh src`(服务器)为准。
7. 只动自己的文件:`configs/F108_max_ntkurt_close.yaml`、`studies/F108_max_ntkurt_close/`、`notes/F108_max_ntkurt_close/`。

## 研究日志(`notes/F108_max_ntkurt_close/journal.md`:21 条,其中研究员自己写的 11 条)

最近的 5 条(更早的和全文看文件):

### 2026-10-04 23:48 [auto] x3_attrib 跑完(exit 0);重看结果:logs/F108_max_ntkurt_close_x3_attrib.log

### 2026-10-04 23:53 [auto] 启动 exec x3_attrib:studies/F108_max_ntkurt_close/x3_attrib.py

### 2026-10-04 23:57 [执行] R2 第2次运行 x3_attrib 跑完(第1次自检没过已改正重跑,第2次exit 0):H16死、H17/H18仍待主研裁决、r>=24.9只解释一成增量

x3_attrib第1次提交:自检没过(book1 train Lnet复现13.9%而不是12.6%,diff 1.3pp>0.5pp门槛),原因是book①的ranking universe
多交了一个isfinite(D30)限制(K1单独的书不该依赖D30是否有值);book②本身没受影响(复现到+0.02~0.05pp)。按脚本自己写的
门槛"对不上就先停下",第1次没往下算A/B/C/D。诊断后改成每一支各按自己的可得性排名(ok1=isfinite(K1)给book①,
ok2=ok1&isfinite(D30)给book②,严格对应引擎cs_rank各自独立求值再by add()合并NaN的语义),第2次重跑自检四项全过
(diff -0.03~+0.05pp),往下跑完A/B/C/D。两次都exit 0、都计入服务器运行次数——R2从计划的2次变成3次,
全研究累计7/8(含S0),final只剩1次、零余量。

§A(H16死):剔掉标签NaN的名字重新归一后,增量train 2.56pp→2.52pp、valid 1.47pp→1.30pp,几乎不变、两段都仍≥1pp同向
→按工单自己定的判据,H16死,这+2.5pp不是"买不进记0"的记账效应。dropped/added里NaN占比都不高(dropped 7.5%/14.3%,
added 0.7%/1.4%);NaN组的"次日真实超额"因为avgN只有0.1~2.5只、算出±1300~2000%这种数字,是小样本噪声,不是真实水平,
非NaN组才稳(avgN100+):train侧drop非NaN组-0.4%、add非NaN组+11.5%,valid侧drop非NaN组+22.0%、add非NaN组+26.7%
——两段都是"换进来的比换出去的强",不是靠买不进的名字撑场子。
§B:dropped几乎全在D30最差2个十分位(decile8+9占72%train/64%valid),added几乎全在最好4个十分位(86%/92%)——
机制干净。但r分桶显示dropped/added的大头(44~86%)都落在r∈[0,6)这个"正常"区间,r>=24.9只占dropped的2.8%/1.8%;
专门构造的"只剔r>=24.9"书只拿到总增量的10.5%(train)/12
…(这条日志还有后文,读 journal.md)

### 2026-10-05 00:01 [执行] R2 完成:结果卡 results/R2.md 写完,07_S2_overlay.md/07x_3_x3_attrib.md 事实部分已补,交主研裁决

R2 的三个疑点现在都有数字了:
- H16(买不进记账):死。剔 NaN 后增量仍有 train+2.52pp/valid+1.30pp,两段同向、都≥1pp。
- H18(单点权重 vs 平台):不干净的中间状态。相对家族线,w∈[0.1,0.6] 两段都更好(不是尖峰);但 train 上 w=0.25
  比邻近的 0.15/0.4 高 0.9~1.3pp(不是纯平台)。valid 侧 0.1~0.4 更平。
- H17(任意弱相关信号都行):三个安慰剂都没达到"增量≥g_w25"的判据,但 p_k2(混入家族第2成员)最接近
  (train 增量+1.5pp<+2.5pp,valid 增量反而−0.2pp),值得专门看一眼。
- 附带结论:避开一字板(r≥24.9)只能解释总增量的 10.5%(train)/12.7%(valid),H14 的单侧剔除写法(g_tail)
  配置里实测远差于 g_w25(同 hl0 下 +6.2%/+15.4% 对 +15.1%/+23.7%)。逐年 6 年里 5 年增量为正,不是只靠 1~2 年。
运行预算:R2 多跑了 1 次(x3_attrib 自检失败重跑),全研究累计 7/8,只剩 1 次留给 final,零余量——R3 不能再加实验。

### 2026-10-05 10:53 [主研] 批量扫描 s1 的综合

读完 s1 大表(87 变体)+ 市场解剖,写定 notes/.../synthesis.md(123 行)与 studies/.../hypo.yaml(32 条,32/32 parse)。
1) 形状确认:(max_m |30 分钟 Close 超额峰度|)³。pow_1_5 / cs_winsor / signedpower 全是死重(ρo +0.97~+1.00);
   pow_2 是树里唯一的 abs(docstring 的 signed-power 分支只在 e≤1 时生效,这里走普通 x**e)。
2) 多头腿是零:ut +1.0% / Lshp +0.15,底腿 −30.6%、LS +2.83 —— 31pp 多空差价里多头腿只拿到约 1pp。
3) sub_A(var/std/delta)与 abl_A 的 +6~8% 不是提纯:ρo 只 +0.04~+0.09、超配最低价格档 +71.6~+79.9pp = 低价书,且仍打不过 k_known +15.4%。
4) 状态量不是事件量:cross_zscore 5/10/30/60 全崩(−21.4~−5.0%),cross_min60 是唯一改对象的记忆(ρo +0.26、Lshp +0.95、LTO 2.1%,但 Lnet 在噪声内)。
5) 解剖的三条:市值段内 +5.3/+5.4/+6.4/+5.7/−0.4 但书超配最大档 +35.8pp(倾斜花错地方);成交额段内符号相反(−2.9…+11.4);
   选股力全在 6.5% 冻结盘口段(段内 +37.3%,家族 −10.9%)与 7.1% 次新段;科创板 −13.3%;低波动 +8.4% vs 高波动 −6.4%。
6) 增量:六条线性 overlay 全差于家族单独(+14.1% 对 +15.4%)→ 对纯多头没有增量。但表里**没有筛子形态**,
   且与 R2 的 D30 载体结论冲突(载体不同),这两点是第二批的主攻(F 组)。

## 工单与结果卡(`notes/F108_max_ntkurt_close/orders/`、`notes/F108_max_ntkurt_close/results/`)

- R0:工单 —,结果卡 有
- R1:工单 有,结果卡 有
- R2:工单 有,结果卡 有
- R3:工单 有,结果卡 **还没有(待执行)**

## 配置里的实验计划(`configs/F108_max_ntkurt_close.yaml`)

- 标题:(读完这棵树之后,用一句话写它是什么)
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base
- **S1_nodes**(8 个变体):哪些节点是多余的?把软极值记忆显式写进表达式,比口径里的 EMA 好吗?
  n_pow3、n_nocube、n_pow5、n_mean、m_mean30、m_mean60、k_mean30、k_max10
- **S2_overlay**(9 个变体):R1 §A3 那点叠在已知家族(K1=cross_mean(day_std(Amt),30))上的多头增量(+2.5pp)是真的,还是三种廉价解释之一(H18 单点权重尖峰 / H17 任何弱相关第二信号 / 配置里复现不出来)?
  g_w25、g_w15、g_w40、g_raw、g_k2w25、g_tail、p_k2、p_ivol、p_cap

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F108_max_ntkurt_close`)

- `S0_baseline`  10-04 11:50  1 个变体  → `./scripts/study.sh digest F108_max_ntkurt_close S0_baseline`
- `S1_nodes`  10-04 14:52  8 个变体  → `./scripts/study.sh digest F108_max_ntkurt_close S1_nodes`
- `S2_overlay`  10-04 23:32  9 个变体  → `./scripts/study.sh digest F108_max_ntkurt_close S2_overlay`
- `sweep_s1`  10-05 10:30  89 个变体  → `./scripts/study.sh digest F108_max_ntkurt_close sweep_s1`
- `anatomy_s1`  10-05 10:41  0 个变体  → `./scripts/study.sh digest F108_max_ntkurt_close anatomy_s1`
- `sweep_s2`  10-05 12:04  139 个变体  → `./scripts/study.sh digest F108_max_ntkurt_close sweep_s2`
- `anatomy_s2`  10-05 12:10  0 个变体  → `./scripts/study.sh digest F108_max_ntkurt_close anatomy_s2`
- `sweepfinal_s2`  10-05 12:15  8 个变体  → `./scripts/study.sh digest F108_max_ntkurt_close sweepfinal_s2`
- `x1_anatomy`(自写脚本的输出)  10-04 13:13  exit 97  → `logs/F108_max_ntkurt_close_x1_anatomy.log`
- `x2_longonly`(自写脚本的输出)  10-04 14:42  exit 0  → `logs/F108_max_ntkurt_close_x2_longonly.log`
- `x3_attrib`(自写脚本的输出)  10-04 23:53  exit 0  → `logs/F108_max_ntkurt_close_x3_attrib.log`

## 已写的 notes(`notes/F108_max_ntkurt_close/`)

`01_expression.md`(1K)、`02_operators.md`(5K)、`03_decomposition.md`(4K)、`04_grammar.md`(2K)、`05_hypotheses.md`(23K)、`06_baseline.md`(9K)、`07_S1_nodes.md`(10K)、`07_S2_overlay.md`(13K)、`07x_1_x1_anatomy.md`(20K)、`07x_2_x2_longonly.md`(14K)、`07x_3_x3_attrib.md`(9K)、`10_distilled.md`(6K)、`journal.md`(24K)、`state.md`(9K)、`synthesis.md`(11K)

## 自写的探针与分析脚本(`studies/F108_max_ntkurt_close/`)

- `probes.py`  10-04 12:16  Probes this tree needs:  day_max(pow_1_5(pow_2(nt_ts_kurt(Close, 30)))).
- `x1_anatomy.py`  10-04 12:21  x1 -- anatomy of  day_max(pow_1_5(pow_2(nt_ts_kurt(Close, 30))))  on real data.
- `x2_longonly.py`  10-04 14:37  x2 -- the section x1 lost to the memory guard: does F108 give a pure-long user
- `x3_attrib.py`  10-04 23:52  x3 -- attribution of the S2_overlay long-leg increment (order R2).

## 结构化结果(`handoff/F108_max_ntkurt_close/results/`)

- `synthesis.json`
