# F108_max_ntkurt_close — 交接状态

_自动生成于 2026-10-05 10:53(`python scripts/recorder.py --brief F108_max_ntkurt_close` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #3264(批次 B01_single_factors)
- 表达式:`day_max(pow_1_5(pow_2(nt_ts_kurt(Close, 30))))`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- 留出段:**还没读过**(只能读一次;读之前要在 `10_distilled.md` 里写下候选排序和判据)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `lead:F108_max_ntkurt_close#1`:已返回结果,最后动作 10-04 23:21 → `handoff/F108_max_ntkurt_close/agents/lead_R1_ade0d96923df1e821.md`
  - `work:F108_max_ntkurt_close#1`:已返回结果,最后动作 10-05 00:02 → `handoff/F108_max_ntkurt_close/agents/work_R1_af1297d4e49a82489.md`
  - `lead:F108_max_ntkurt_close#2`:中断,最后动作 10-05 00:20 → `handoff/F108_max_ntkurt_close/agents/lead_R2_a7c78c9c449a0151b.md`

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F108_max_ntkurt_close` 看服务器上的 tag,`./scripts/study.sh digest F108_max_ntkurt_close <tag>` 重看结果)。

## 研究现状(`notes/F108_max_ntkurt_close/state.md`,10-05 00:20 更新)—— **先读这个文件**

# F108_max_ntkurt_close 研究现状(每轮整个覆盖重写;接手先读这一页)

`day_max(pow_1_5(pow_2(nt_ts_kurt(Close, 30))))`,真实形状 = **`max(Kmax, −Kmin)³`**(x1 §0 秩相关 1.00000)。
最后更新:**读完 R2 结果卡的那一轮主研**(recorder 里的 `lead#2`;以工单号为准,本轮下了 R3)。

## 1. 一句话现状

R2 把三道反驳全清掉了(H16 死、H17 死、H18 改写),并意外量出 H19:**头条 +2.5pp 增量里 train 有 +1.3pp 是
universe 效应,真正的结构增量是 +1.2pp(train)/+1.4pp(valid)**。证据够选候选 → 本轮**直接进 (b)**:
`10_distilled.md` 的「读留出段之前」已写定(5 个候选 + 排序 + 判据 1~5),`orders/R3.md`(kind: **final**)已下。
**下一轮必须是 (c) 成文**,不许再开实验(预算 7/8,最后 1 次就是 R3 的 final)。

(…全文 7369 字符,读 `notes/F108_max_ntkurt_close/state.md`)

## 研究日志(`notes/F108_max_ntkurt_close/journal.md`:20 条,其中研究员自己写的 10 条)

最近的 5 条(更早的和全文看文件):

### 2026-10-04 23:48 [auto] 启动 exec x3_attrib:studies/F108_max_ntkurt_close/x3_attrib.py

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
- `x1_anatomy`(自写脚本的输出)  10-04 13:13  exit 97  → `logs/F108_max_ntkurt_close_x1_anatomy.log`
- `x2_longonly`(自写脚本的输出)  10-04 14:42  exit 0  → `logs/F108_max_ntkurt_close_x2_longonly.log`
- `x3_attrib`(自写脚本的输出)  10-04 23:53  exit 0  → `logs/F108_max_ntkurt_close_x3_attrib.log`

## 已写的 notes(`notes/F108_max_ntkurt_close/`)

`01_expression.md`(1K)、`02_operators.md`(5K)、`03_decomposition.md`(4K)、`04_grammar.md`(2K)、`05_hypotheses.md`(23K)、`06_baseline.md`(9K)、`07_S1_nodes.md`(10K)、`07_S2_overlay.md`(13K)、`07x_1_x1_anatomy.md`(20K)、`07x_2_x2_longonly.md`(14K)、`07x_3_x3_attrib.md`(9K)、`10_distilled.md`(6K)、`journal.md`(22K)、`state.md`(11K)、`synthesis.md`(11K)

## 自写的探针与分析脚本(`studies/F108_max_ntkurt_close/`)

- `probes.py`  10-04 12:16  Probes this tree needs:  day_max(pow_1_5(pow_2(nt_ts_kurt(Close, 30)))).
- `x1_anatomy.py`  10-04 12:21  x1 -- anatomy of  day_max(pow_1_5(pow_2(nt_ts_kurt(Close, 30))))  on real data.
- `x2_longonly.py`  10-04 14:37  x2 -- the section x1 lost to the memory guard: does F108 give a pure-long user
- `x3_attrib.py`  10-04 23:52  x3 -- attribution of the S2_overlay long-leg increment (order R2).

## 结构化结果(`handoff/F108_max_ntkurt_close/results/`)

(还没有)
