# F114_q25_closeret — 交接状态

_自动生成于 2026-10-04 23:02(`python scripts/recorder.py --brief F114_q25_closeret` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #1421(批次 B01_single_factors)
- 表达式:`cross_quantile_q25(day_close(Ret), 15)`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- 留出段:**还没读过**(只能读一次;读之前要在 `10_distilled.md` 里写下候选排序和判据)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `work:F114_q25_closeret#2`:已返回结果,最后动作 10-04 15:31 → `handoff/F114_q25_closeret/agents/work_R2_a0bd0147a32301a5f.md`
  - `lead:F114_q25_closeret#3`:失败,几乎没做事
  - `lead:F114_q25_closeret#3`:失败,几乎没做事

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F114_q25_closeret` 看服务器上的 tag,`./scripts/study.sh digest F114_q25_closeret <tag>` 重看结果)。

## 研究现状(`notes/F114_q25_closeret/state.md`,10-04 14:56 更新)—— **先读这个文件**

# F114_q25_closeret — 研究现状(主研每轮覆盖重写)

最后更新:**第 2 轮**(主研 Opus 5,2026-10-04)。表达式 `cross_quantile_q25(day_close(Ret), 15)`,来源 挖掘 #1421。
**接手的人:先读 §1,再读 §4 假设表、§5 候选、§6 后面的思路。§2 的每个数字都带出处,不要重新测已经有数的东西。
工单 `orders/R2.md` 已经写好并交给执行 —— 如果 `results/R2.md` 还不存在,按任务书第 2 条不要另开工单,把 R2 原样交回执行。**

---

## 1. 一句话现状

R0(建档+基线)、R1(12 个变体 / 2 次运行)都已跑完读完,**本轮(R2 主研)把 R1 全部裁决完了**:
两条提纯路(拆成纯位置 / 纯尺度)**都被实验堵死**,`q75`/`q25` 这对的**整个线性族里原式就是最优点**;
「它等价于日收益下四分位数」这个最危险的可能性被**决定性否定**(rank 相关 +0.00);
**唯一还活着的升华方向是窗口加长**(30 / 60 天,train +2.6% / +3.5% vs 原式 +1.8%,固定半衰期同列也超过)。

**下一步(执行):做 `orders/R2.md`** —— 2 次运行:
① `S4_horizon`(新阶段 `S4_long`:`s4_w241` / `s4_mean60` / `s4_iso`,外加把旧阶段 `S3_window` 一起带进去拿逐年和条件 IC)
→ 定窗口饱和点、定长窗口版是不是制度骑乘;
② `S5_known`(H12:用 `cs_regres` 做残差腿、用 `add`/`sub(cs_rank, cs_rank)` 做相加腿)
→ 正面回答「对只能做多的用户,相对已知成交额家族有没有增量」。

留出段**未读**。服务器运行已用 2 次(上限 8,不含 S0),R2 再用 2 次 → 还剩 4 次(其中 1 次留给 final)。

---

(…全文 22277 字符,读 `notes/F114_q25_closeret/state.md`)

## 研究日志(`notes/F114_q25_closeret/journal.md`:17 条,其中研究员自己写的 10 条)

最近的 5 条(更早的和全文看文件):

### 2026-10-04 15:12 [执行] R2 第1次运行:S4_horizon(S4_long+S3_window)跑完读完,WBEST按工单规则定为60

exit 0,6个新变体(s3_w5/s3_w30/s3_w60/s4_w241/s4_mean60/s4_iso)+v_base缓存行,errors={}。
关键数字(train/valid 多头腿净超额,v_base对照+1.8%/+8.1%):
s4_w241 +1.1%/+9.5%(固定hl20列+1.1%/Lshp+0.19,明显低于s3_w60的hl20列+3.1%/+0.52)——
train上窗口收益不再单调:5<15<30<60但241掉回+1.1%,241没有继续明显上升。
s4_mean60(60日尾盘均值,非稳健)+1.3%/+2.8%,远低于s3_w60+3.5%/+8.6%,Lshp valid仅0.91 vs 1.59。
s4_iso(=day_close(Ret),零记忆)Lnet -2.3%/-1.2%(LTO高达10.4%导致净值差),但原始rIC_tr=+0.0107是本次最高、
Lgross tr/va +5.6%/+7.1%与v_base的+4.1%/+10.5%量级相近。
按工单写死的规则:s3_w30(+2.6%)/s3_w60(+3.5%)/s4_w241(+1.1%)三者cov/dist都过门槛(dist 0.61/0.67/0.55),
s4_w241 train Lnet=+1.1%≤+3.5%,触发规则"WBEST=60"。
异常:s4_w241逐年long_share在2019/2020为-91.0%/-24.9%(因long_gross_ann本身为负:-2.9%/-2.0%,
不是分母接近零而是分子变号,与R1遇到的"分母接近零"是不同机制);已知家族基准06_baseline.md记录的
hl/Lnet与本次重读S0_baseline.json直接拉出来的数不一致(known_amt_max9等三条hl从1/0/10变成5/5/20,
rank_ic完全一致)——怀疑是旧digest在rank_by="ls"时期生成的读数,写进了结果卡异常节,不替主研判断。
下一步:做第2次运行S5_known(WBEST=60),用cs_regres/cs_rank做H12残差腿和相加腿。

### 2026-10-04 15:13 [auto] 启动 run S5_known:阶段 S5_known

### 2026-10-04 15:17 [auto] S5_known 跑完(exit 0);重看结果:./scripts/study.sh digest F114_q25_closeret S5_known

### 2026-10-04 15:19 [执行] R2 第2次运行:S5_known(WBEST=60)跑完读完,H12 六个变体数字齐

exit 0,6个新变体(f_fam_m30/h12_res_base_m30/h12_res_best_m30/h12_add_best_m30/h12_sub_best_m30/h12_res_base_x9),
errors={},cov全部0.999、dist全部≥0.80(无新的门槛失败)。
f_fam_m30(=known_stdamt_mean30 原式再跑一遍)sign=-1,hlL=0,Lnet tr/va +12.6%/+22.3%,Lshp +1.78/+3.46 ——
与S0_baseline.json controls块里known_stdamt_mean30的数字完全对上(交叉验证一致),但与06_baseline.md记录的
另外三条已知家族数字(hl=1/0/10)不一致,现在重读S0_baseline.json这三条的hl_long是5/5/20、Lnet也不同,
rank_ic两次读数完全相同——怀疑06_baseline写于顶层rank_by="ls"期间(R0异常a),已写入结果卡,不作处理。
残差腿:h12_res_base_m30(原式残差)train/valid Lnet +0.4%/+5.4%、rICtraded+0.0044/+0.0140;
h12_res_best_m30(候选=w60残差)+0.7%/+5.4%、rICtraded+0.0040/+0.0097;h12_res_base_x9(换成max9家族)+0.5%/+5.3% ——
三条残差彼此接近,换另一条家族基准结论不敏感。cs_regres取交集的覆盖率担心没有发生:三条残差变体
coverage_labelled仍是0.999(train/valid都是),没有跌破门槛。
组合腿:h12_add_best_m30(与家族同向)Lnet+12.0%/+21.4%、Lshp1.78/3.50,几乎等于家族单独(+12.6%/+22.3%,1.78/3.46);
h12_sub_best_m30(对冲腿,引擎选到sign=+1)Lnet+2.9%/+11.2%,明显更差,印证add是同向组合。
h12_add_best_m30与known_stdamt_mean30的rank相关-0.74,h12_sub_best_m30与其相关-0.67(f_fam_m30自己与
known_stdamt_mean30相关
…(这条日志还有后文,读 journal.md)

### 2026-10-04 15:29 [执行] R2 结果卡写完:两次运行12个变体数字齐,WBEST=60,发现digest的short/TO列账本不一致

notes/F114_q25_closeret/results/R2.md 写完,覆盖工单全部19项数字+第0步已知家族基准,只报事实不下结论。
最关键的几个数字:
- WBEST=60(工单规则机械判定:s4_w241 train Lnet+1.1%≤s3_w60的+3.5%)。
- H16饱和:s4_w241(窗口241)train/valid Lnet+1.1%/+9.5%,固定hl20列+1.1%/+0.19,明显低于s3_w60的+3.1%/+0.52——
  train上窗口收益在241这一档没有继续单调上升。
- H17:s4_mean60(60日均值替代q25)+1.3%/+2.8%,远低于s3_w60+3.5%/+8.6%,稳健分位数在长窗口下仍有必要。
- H12:候选(w60)残差h12_res_best_m30对家族中性化后train/valid Lnet+0.7%/+5.4%(原式残差h12_res_base_m30
  +0.4%/+5.4%,换家族基准x9结果+0.5%/+5.3%,三者接近);组合h12_add_best_m30 Lnet+12.0%/+21.4%几乎等于
  家族单独+12.6%/+22.3%;h12_add/sub与known_stdamt_mean30的rank相关绝对值0.74/0.67,都<0.95门槛。
  家族自己all_controls R²=0.871(全研究最高)。
本卡发现并修正了一个工具读数陷阱:study.sh digest打印的"short tr"/中性化表的"TO"在hlL≠hlS时取自ls账本,
与同行Lgross/未中性化数字不是同一本账本,直接套公式会算错long_share——已在R2.md第1条异常写清楚,并指出
R1.md主表s3_w30/s3_w60两行的short tr用的正是ls账本读数(不是错,是另一种口径,要不要改留给主研)。
另发现06_baseline.md记的已知家族hl/Lnet与现在重读S0_baseline.json不一致(rank_ic相同,hl不同,疑似rank_by="ls"
残留),s4_w241逐年long_share在2019/2020为负三位数(分子变负,非分母趋零)。
两次运行errors均为{},12个新变体cov全部0.9992,无新增门槛失败(s3_w5 dist0.4
…(这条日志还有后文,读 journal.md)

## 工单与结果卡(`notes/F114_q25_closeret/orders/`、`notes/F114_q25_closeret/results/`)

- R0:工单 —,结果卡 有
- R1:工单 有,结果卡 有
- R2:工单 有,结果卡 有

## 配置里的实验计划(`configs/F114_q25_closeret.yaml`)

- 标题:单只股票近 15 日「尾盘最后一个有效分钟那一笔分钟收益」分布的下四分位数;取负后精确等于该分布的四分位距减四分位中点(权重 1:1),把尾盘分钟波动与尾盘卖压反转绑在一起的慢变特征量
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base
- **S1_shape**(6 个变体):原式读出的 0.25 分位数,读的是分布的位置、尺度,还是两者的 1:1 混合?
  s1_q75、s1_loc、s1_scl、s1_q50、s1_std、s1_min
- **S2_where**(3 个变体):「当天最后一个有效分钟」这个取值位置是必要的,还是换成当日收益/全天平均/开盘第一分钟都一样?
  s2_daysum、s2_daymean、s2_dayopen
- **S3_window**(3 个变体):15 天的记忆够不够?(hlL=hlS=20 已顶到 EMA 网格上限、衰减表到 h20 还在升 —— 加长记忆只能靠改窗口)
  s3_w5、s3_w30、s3_w60
- **S4_long**(3 个变体):窗口加长在哪里饱和?长窗口下「下四分位数」这个稳健统计量还必要吗?完全不带记忆又如何?
  s4_w241、s4_mean60、s4_iso
- **S5_known**(6 个变体):对只能做多的用户,这条因子相对已知成交额家族有没有增量?
  f_fam_m30、h12_res_base_m30、h12_res_best_m30、h12_add_best_m30、h12_sub_best_m30、h12_res_base_x9

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F114_q25_closeret`)

- `S0_baseline`  10-04 11:57  1 个变体  → `./scripts/study.sh digest F114_q25_closeret S0_baseline`
- `S1_shape`  10-04 13:54  6 个变体  → `./scripts/study.sh digest F114_q25_closeret S1_shape`
- `S2_aperture`  10-04 14:08  6 个变体  → `./scripts/study.sh digest F114_q25_closeret S2_aperture`
- `S4_horizon`  10-04 15:08  6 个变体  → `./scripts/study.sh digest F114_q25_closeret S4_horizon`
- `S5_known`  10-04 15:16  6 个变体  → `./scripts/study.sh digest F114_q25_closeret S5_known`

## 已写的 notes(`notes/F114_q25_closeret/`)

`01_expression.md`(3K)、`02_operators.md`(8K)、`03_decomposition.md`(2K)、`04_grammar.md`(6K)、`05_hypotheses.md`(22K)、`06_baseline.md`(14K)、`07_S1_shape.md`(7K)、`07_S2_where.md`(5K)、`07_S3_window.md`(7K)、`journal.md`(26K)、`state.md`(35K)

## 自写的探针与分析脚本(`studies/F114_q25_closeret/`)

(无)

## 结构化结果(`handoff/F114_q25_closeret/results/`)

(还没有)
