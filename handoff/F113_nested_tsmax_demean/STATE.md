# F113_nested_tsmax_demean — 交接状态

_自动生成于 2026-10-04 23:02(`python scripts/recorder.py --brief F113_nested_tsmax_demean` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #1375(批次 B01_single_factors)
- 表达式:`pow_1_5(ts_max(pow_2(cs_demean(mul(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(day_mean(Ret), 5), -5)), 30)), 20), 5))), 30))`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- 留出段:**还没读过**(只能读一次;读之前要在 `10_distilled.md` 里写下候选排序和判据)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `lead:F113_nested_tsmax_demean#2`:已返回结果,最后动作 10-04 15:01 → `handoff/F113_nested_tsmax_demean/agents/lead_R2_aa404b933ea64d85e.md`
  - `work:F113_nested_tsmax_demean#2`:失败,最后动作 10-04 15:43 → `handoff/F113_nested_tsmax_demean/agents/work_R2_a6d503c89ebbaf6ab.md`
  - `work:F113_nested_tsmax_demean#2`:失败,几乎没做事

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F113_nested_tsmax_demean` 看服务器上的 tag,`./scripts/study.sh digest F113_nested_tsmax_demean <tag>` 重看结果)。

## 研究现状(`notes/F113_nested_tsmax_demean/state.md`,10-04 15:00 更新)—— **先读这个文件**

# 研究现状 — F113_nested_tsmax_demean

> 主研每轮**整个覆盖重写**这一页。最近更新:**第 2 轮(主研 Opus 5),2026-10-04**。
> 流水在 `journal.md`(只追加);这一页是"现在的理解"。
> 表达式:`pow_1_5(ts_max(pow_2(cs_demean(mul(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(day_mean(Ret), 5), -5)), 30)), 20), 5))), 30))`

---

## 1. 一句话现状

R0 建档 + R1 实验(`S1_chain` 10 变体 + `x1_ties` 脚本)都已跑完并**裁决完毕**:
**原式的多头腿不可用,但把它的外层折叠拿掉之后,子结构里有一条多头腿两段同向为正的因子
(`c4_nodemean_out`,train/valid `Lnet +6.9% / +13.3%`、`Lshp +0.92 / +2.06`、日换手只有 2.7%)。**
问题是**已知家族自己的多头腿更好**(`known_stdamt_max9 +9.3% / +18.5%`),所以研究的结论现在卡在
一个还没量过的问题上:**候选相对已知家族有没有增量**。
本轮下了工单 **R2**(kind: experiment,2 次服务器运行):(A) `S2_bench` 10 个变体 —— 朴素长窗 MAX /
朴素波动的直接替换 + 最小结构提纯 + 窗口邻域 + 两个已知家族进同一张表 + 秩相加的增量候选;
(B) 脚本 `x2_increment` —— H12 交叉表、候选多头腿的暴露剖面、与已知家族的多头腿重合率、
对已知家族中性化的残差多头腿、多头腿名单的收益分解。
**下一步:执行跑 R2、写 `results/R2.md`;下一轮主研裁决 Q1(是不是朴素 MAX)与 Q2(有没有增量),
然后大概就可以定候选、进留出段。**

服务器运行已用 **2 / 8**(S0 不计),R2 会用掉 2 次 → 4/8,给 final 留足。轮次:第 2 / 10 轮。

---

(…全文 13920 字符,读 `notes/F113_nested_tsmax_demean/state.md`)

## 研究日志(`notes/F113_nested_tsmax_demean/journal.md`:17 条,其中研究员自己写的 8 条)

最近的 5 条(更早的和全文看文件):

### 2026-10-04 15:31 [执行] R2:S2_bench(10变体)跑完,exit 0,337.7s;Q1 答案是'很像但数字不像'——n2 朴素MAX与c4 rank相关+0.95但valid Lnet差4.7pp train差7.2pp且翻号;已知家族kf_mean30/kf_max9自己的多头腿(+12.6%/+22.3%、+9.3%/+22.2%)全面碾压c4

看到了什么(决策口径,多头腿净超额 Lnet,train/valid,扣费):
- n2_max79_plain(79日朴素MAX)-0.3%/+8.6%;m1_rel79_max(79日相对MAX,提纯候选)+3.2%/+14.8%;
  m2_rel50_absmax(绝对值折叠)+2.7%/+14.6%;m3_rel50_absmean(max换mean)+2.1%/+13.3%,m2≈m3(MAX语义不是
  load-bearing,平均绝对相对收益就够)。n4_dvol50_plain(朴素波动)-5.5%/+4.1%,两段比ctl_dvol20(-11.1%/-2.7%)
  好但依然弱,方向验证了"c4不是低波动改写"的预期。
- w1_c4_62(62天回看)+6.7%/+9.7%,w2_c4_102(102天)+6.3%/+12.7%,c4(82天)+6.9%/+13.3%——三点邻域平滑,
  不是82这个点被挑出来的,窗口稳。
- kf_mean30(当前rank_by:long重算)hl=0,+12.6%/+22.3%;kf_max9 hl=5,+9.3%/+22.2%(修好了R0异常①的半衰期
  矛盾)。cb_c4_kf30(秩相加)+12.5%/+22.4%,基本等于kf_mean30自己,没有比已知家族各自更好。
- rank相关(Q1逐格):c4×n2=+0.948,c4×m1=+0.920,c4×w1=+0.890,c4×w2=+0.931,c4×m2=+0.776,c4×m3=+0.697,
  c4×n4(朴素波动)=+0.766,c4×kf_mean30=+0.365,c4×kf_max9=+0.375。m1×m2=+0.809,m2×m3=+0.808,
  kf_mean30×kf_max9=+0.958。
- cov/dist 全部通过:10个新变体cov=1.00,dist除cb_c4_kf30=0.81外全部1.00(两个cs_rank相加没有触发NaN担心)。
- 固定半衰期表(train,hl0/1/2/3/5/10/2
…(这条日志还有后文,读 journal.md)

### 2026-10-04 15:31 [auto] 启动 exec x2_increment:studies/F113_nested_tsmax_demean/x2_increment.py

### 2026-10-04 15:33 [auto] x2_increment 跑完(exit 0);重看结果:logs/F113_nested_tsmax_demean_x2_increment.log

### 2026-10-04 15:34 [auto] 启动 exec x2_increment:studies/F113_nested_tsmax_demean/x2_increment.py

### 2026-10-04 15:39 [执行] R2:x2_increment跑完(改了一次bug后exit 0);H12路由机制两段一致但'赚钱'只train成立;区块5只在c4多头腿这组股票超额中位数两段为负(-0.95%/-13.62%);c4对kf30+kf9残差Lgross两段都<+5%但rIC没归零,kf30对c4残差仍留八成edge

看到了什么(决策口径,全部 train/valid):
- 区块1(H12路由):v_base 10档按sig分、G按截面分位分。(a)v_base档1(空头端)G分位中位数0.950(两段都约0.85-0.95),
  档10(多头端)只有0.655/0.676,档3附近才是G的谷底(0.140/0.102)——低G既不在多头端也不在空头端最浓,
  但多头端的G分位明显低于空头端,方向和H12一致。(b)G档1(最安静)成员池化后41.8%(train)/47.3%(valid)落在
  v_base档3,档9/10都是0.000——低G股票确定性地没有进v_base的多头腿。G档10(最极端)72.1%/69.9%落在档1。
  (c)G档1等权超额年化:train +7.13%(安静股票确实赚钱)、valid -0.90%(反了,没能复现);G档10:train -30.42%、
  valid -13.05%(两段都很负,稳定)。结论:"低G被路由避开多头腿"两段都坐实,但"低G=赚钱"只在train成立。
- 区块2(暴露剖面):c4/m1/n2三者的长腿画像彼此接近(ctl_cap约0.51-0.59偏大盘、ctl_amt约0.27-0.31、ctl_dvol20约
  0.11-0.14偏低波动),但跟kf_mean30的画像明显不同(kf_mean30长腿ctl_amt只0.06-0.07、ctl_cap只0.16-0.22偏小盘)——
  两者是不同的书,这跟区块3的重合率(~0.25-0.29,高于随机基准0.10但远非同一本书)、跟(A)里的rank相关+0.365
  互相印证。
- 区块3:c4 对 ctl_dvol20(当factor独立选半衰期)的多头腿重合率0.39-0.40,比c4对kf30/kf9(0.25-0.29)更高。
- 区块4(残差,sign固定+1.0):c4对{kf30,kf9}中性化,R2=0.142,残差多头腿 train Lnet-1.38%/Lgross-0.01%、
  valid Lnet+1.57%/Lgross+2.85%(两段Lgross都<工
…(这条日志还有后文,读 journal.md)

## 工单与结果卡(`notes/F113_nested_tsmax_demean/orders/`、`notes/F113_nested_tsmax_demean/results/`)

- R0:工单 —,结果卡 有
- R1:工单 有,结果卡 有
- R2:工单 有,结果卡 有

## 配置里的实验计划(`configs/F113_nested_tsmax_demean.yaml`)

- 标题:两层嵌套的「日轴 MAX 记忆 → 截面去均值 → 平方折叠」(只用 Ret):最终排序的是「近 54 日极端收益幅度离当日截面均值的距离」,sign=-1 即做多「极端程度最接近截面典型值、且 30 日内没偏离过」的股票
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base
- **S1_chain**(10 个变体):沿这条不分支的链逐节点消融 + 把外层折叠的中心挪到中位数/秩空间:多头腿是差还是没有意义?哪些节点是多余的?
  c1_b_max5、c2_e_rel34、c3_g_fold1、c4_nodemean_out、c5_nopow15、c6_nomul_nosub、c7_nofold_in、c8_nofold_out、c9_rankfold、c10_medfold
- **S2_bench**(10 个变体):c4 这一类候选是不是朴素长窗 MAX / 低波动的改写?最小结构能不能保住它的多头腿?它相对已知家族有没有增量?
  n2_max79_plain、n4_dvol50_plain、m1_rel79_max、m2_rel50_absmax、m3_rel50_absmean、w1_c4_62、w2_c4_102、kf_mean30、kf_max9、cb_c4_kf30

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F113_nested_tsmax_demean`)

- `S0_baseline`  10-04 11:57  1 个变体  → `./scripts/study.sh digest F113_nested_tsmax_demean S0_baseline`
- `S1_chain`  10-04 14:03  10 个变体  → `./scripts/study.sh digest F113_nested_tsmax_demean S1_chain`
- `S2_bench`  10-04 15:12  10 个变体  → `./scripts/study.sh digest F113_nested_tsmax_demean S2_bench`
- `x1_ties`(自写脚本的输出)  10-04 14:22  exit 0  → `logs/F113_nested_tsmax_demean_x1_ties.log`
- `x2_increment`(自写脚本的输出)  10-04 15:35  exit 0  → `logs/F113_nested_tsmax_demean_x2_increment.log`

## 已写的 notes(`notes/F113_nested_tsmax_demean/`)

`01_expression.md`(4K)、`02_operators.md`(10K)、`03_decomposition.md`(7K)、`04_grammar.md`(8K)、`05_hypotheses.md`(16K)、`06_baseline.md`(13K)、`07_S1_chain.md`(7K)、`07x_1_ties_longbook.md`(5K)、`08_variants.md`(3K)、`journal.md`(22K)、`state.md`(21K)

## 自写的探针与分析脚本(`studies/F113_nested_tsmax_demean/`)

- `x1_ties_and_longbook.py`  10-04 14:17  studies/F113_nested_tsmax_demean/x1_ties_and_longbook.py -- 工单 R1 (B)。
- `x2_increment.py`  10-04 15:33  studies/F113_nested_tsmax_demean/x2_increment.py -- 工单 R2 (B)。

## 结构化结果(`handoff/F113_nested_tsmax_demean/results/`)

(还没有)
