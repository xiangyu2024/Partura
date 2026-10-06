# F108_max_ntkurt_close — 交接状态

_自动生成于 2026-10-05 19:23(`python scripts/recorder.py --brief F108_max_ntkurt_close` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #3264(批次 B01_single_factors)
- 表达式:`day_max(pow_1_5(pow_2(nt_ts_kurt(Close, 30))))`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- **留出段已经读过 2 次**(10-05 11:16, 10-05 12:13)—— **不许再读**。候选在留出段上的数全在 `runs/F108_max_ntkurt_close/final.json`(`./scripts/study.sh digest F108_max_ntkurt_close final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `synth:F108_max_ntkurt_close`:已返回结果,最后动作 10-05 11:00 → `handoff/F108_max_ntkurt_close/agents/synth_a3d74598652f5a146.md`
  - `verdict:F108_max_ntkurt_close`:中断,最后动作 10-05 13:53 → `handoff/F108_max_ntkurt_close/agents/verdict_a8c9d4ac94d1c29f6.md`
  - `verdict:F108_max_ntkurt_close`:已返回结果,最后动作 10-05 15:17 → `handoff/F108_max_ntkurt_close/agents/verdict_ae70bca6af3f47ef1.md`

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F108_max_ntkurt_close` 看服务器上的 tag,`./scripts/study.sh digest F108_max_ntkurt_close <tag>` 重看结果)。

## 研究现状(`notes/F108_max_ntkurt_close/state.md`,10-05 15:12 更新)—— **先读这个文件**

# F108_max_ntkurt_close 研究现状(每轮整个覆盖重写;接手先读这一页)

`day_max(pow_1_5(pow_2(nt_ts_kurt(Close, 30))))`,真实形状 = **`(max_m |K_m|)³`**,K = 日内 **30 分钟** Close 的超额峰度。
最后更新:读完批量扫描 s2(136 变体)+ 新解剖、做完对账与定论、并复核了一遍数字的那一轮主研。
本轮**没有起任何服务器计算**(只跑 `hypo3` 语法检查,25/25)。**没有读过测试段**。

## 1. 现状(一句话)

**定论已经做完,可以收口。** 两轮批量扫描(s1 87 条 / s2 136 条)+ 两次解剖,结论:
**提纯成功、升华失败。** 纯多头作排序器不可用(best_own ut **+6.1%** 对 k_known **+15.4%**);
作筛子 / 叠加可用(**+17.1~17.6%** > +15.4%)但**被通用冻结筛子 `k_known_xfrozen`(+18.5% / Lshp 3.15)支配**。
它的真实贡献是**指出了已知成交额族的冻结盘口弱点**,而那个弱点用 `day_zero_ratio(Ret)`(日频、通用、与本树无关)修得更好。
→ **它是那个弱点的次优探针,不是独立 alpha。** 唯一还开着的问题见 §6。

(…全文 6311 字符,读 `notes/F108_max_ntkurt_close/state.md`)

## 研究日志(`notes/F108_max_ntkurt_close/journal.md`:23 条,其中研究员自己写的 13 条)

最近的 5 条(更早的和全文看文件):

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

### 2026-10-05 13:50 [主研] 批量扫描 s2 对账与结论

对账:第二批 32 条里 A/C/G/H/I 五组全部否定(直接状态变量、折叠换频率/集中度/位置、时段门控、慢性读数、封板软 AND);
B 组只确认「尺度泄漏 = 叶子的水平量」一条(h_std_amt30 ut +16.5%、ρk +0.93 = 直接变成已知族),换 Amt/Volume 叶子治不了 EPS 地板(ut −7.1%、sg 翻转);
E 组我上一轮的预言错了 —— cs_bucket_rank(D30, A20) ut +6.1%、ρo +0.86、ρk +0.08,是 best_own;F 组裁决了 R2 与 s1 的冲突:载体必须慢(+17.6% 对未平滑 +14.1%),R2 对。
定论:提纯成功、升华失败。best_on_known = h_ov_mean30_p025 +17.6%/+2.73(叠加)与 z_known_excl_mem30 +17.1%/+2.66(筛子),都强于 k_known +15.4%/+2.22,
但都弱于通用冻结筛子 k_known_xfrozen +18.5%/+3.15 → 本因子是「已知族冻结盘口弱点」的次优探针,不是独立 alpha;seg_xfrozen_p −0.8% 坐实了「剔掉冻结段就什么都不剩」。
两条可迁移的坑:① mul(rank, logical_not(mask)) 在 sg=−1 的载体上是反向筛子(h_scr_hard_q25 −5.8%、ρk −0.65),筛子一律写 cs_last_high20;
② 有界离散读数当排序器会被平局饱和(7 条 dist 0.04~0.17),当筛子闸门却是全表第二(+17.8%)。
产出:synthesis.md 追加「第二轮(s2)对账与结论」、state.md 覆盖重写、hypo3.yaml 25 条 25/25 parse(判决性的一条是 h3_scr_dbl:xfrozen 之上再剔本因子最高 20%)。本轮没起服务器计算,没读测试段。

### 2026-10-05 15:12 [主研] 批量扫描 s2 对账与结论

复核了上一轮(13:50)已落盘的 s2 对账与定论:重跑 table s2 --all 把 synthesis §6–7 里引的每个数字对了一遍,全部一致;
hypo3 语法检查 25/25 通过。结论不变:提纯成功、升华失败 —— best_own = cs_bucket_rank(D30, A20) +6.1%/Lshp 1.16(ρo +0.86、ρk +0.08),
best_on_known = h_ov_mean30_p025 +17.6%/+2.73(叠加)与 z_known_excl_mem30 +17.1%/+2.66(筛子),都 > k_known +15.4%/+2.22、都 < k_known_xfrozen +18.5%/+3.15。
复核时从解剖表补了两条原对账漏掉的:① 筛子赚的是「不持有」—— 冻结段(6.5%、段等权 −67.4%)里 z_known_excl_flatrun 的持仓占比是 −5.6pp(剔到只剩 ~0.9%),
段内 −147.2% 在仓位近零时没有意义;线性叠加只能压到 −4.9pp、压不到零 → 硬剔与软压是两件事,这就是 +18.5% 与 +17.6% 之间那 0.9pp。
② 融合权重曲线(总领做平滑用):train w=0.15/0.25/0.40 = +13.8/+15.1/+14.2%,w=1 等权 +11.1% 已低于家族线 +12.6%,valid 在 [0.1,0.4] 平;
且同一个 w=0.25,载体未平滑只 +14.1% → 配方 = 先 30 日平均、再按 0.2~0.3 小权重叠,等权一定亏。
两条已追加为 synthesis §8,state.md §2-6/§2-7、§8-7。本轮没起服务器计算,没读测试段(sweepfinal_s2.json 未打开)。

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
- `sweep_s3`  10-05 18:10  163 个变体  → `./scripts/study.sh digest F108_max_ntkurt_close sweep_s3`
- `anatomy_s3`  10-05 18:33  0 个变体  → `./scripts/study.sh digest F108_max_ntkurt_close anatomy_s3`
- `sweepfinal_s3`  10-05 18:36  8 个变体  → `./scripts/study.sh digest F108_max_ntkurt_close sweepfinal_s3`
- `x1_anatomy`(自写脚本的输出)  10-04 13:13  exit 97  → `logs/F108_max_ntkurt_close_x1_anatomy.log`
- `x2_longonly`(自写脚本的输出)  10-04 14:42  exit 0  → `logs/F108_max_ntkurt_close_x2_longonly.log`
- `x3_attrib`(自写脚本的输出)  10-04 23:53  exit 0  → `logs/F108_max_ntkurt_close_x3_attrib.log`

## 已写的 notes(`notes/F108_max_ntkurt_close/`)

`01_expression.md`(1K)、`02_operators.md`(5K)、`03_decomposition.md`(4K)、`04_grammar.md`(2K)、`05_hypotheses.md`(23K)、`06_baseline.md`(9K)、`07_S1_nodes.md`(10K)、`07_S2_overlay.md`(13K)、`07x_1_x1_anatomy.md`(20K)、`07x_2_x2_longonly.md`(14K)、`07x_3_x3_attrib.md`(9K)、`10_distilled.md`(6K)、`journal.md`(26K)、`state.md`(10K)、`synthesis.md`(19K)

## 自写的探针与分析脚本(`studies/F108_max_ntkurt_close/`)

- `probes.py`  10-04 12:16  Probes this tree needs:  day_max(pow_1_5(pow_2(nt_ts_kurt(Close, 30)))).
- `x1_anatomy.py`  10-04 12:21  x1 -- anatomy of  day_max(pow_1_5(pow_2(nt_ts_kurt(Close, 30))))  on real data.
- `x2_longonly.py`  10-04 14:37  x2 -- the section x1 lost to the memory guard: does F108 give a pure-long user
- `x3_attrib.py`  10-04 23:52  x3 -- attribution of the S2_overlay long-leg increment (order R2).

## 结构化结果(`handoff/F108_max_ntkurt_close/results/`)

- `synthesis.json`
- `verdict.json`
