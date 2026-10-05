# F114_q25_closeret — 交接状态

_自动生成于 2026-10-05 00:42(`python scripts/recorder.py --brief F114_q25_closeret` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #1421(批次 B01_single_factors)
- 表达式:`cross_quantile_q25(day_close(Ret), 15)`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- **留出段已经读过 1 次**(10-04 23:56)—— **不许再读**。候选在留出段上的数全在 `runs/F114_q25_closeret/final.json`(`./scripts/study.sh digest F114_q25_closeret final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `lead:F114_q25_closeret#1`:已返回结果,最后动作 10-04 23:47 → `handoff/F114_q25_closeret/agents/lead_R1_aabcc661842828a07.md`
  - `work:F114_q25_closeret#1`:已返回结果,最后动作 10-05 00:12 → `handoff/F114_q25_closeret/agents/work_R1_a2af85fe053c7b981.md`
  - `lead:F114_q25_closeret#2`:中断,最后动作 10-05 00:20 → `handoff/F114_q25_closeret/agents/lead_R2_a9262d78a60d3e050.md`

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F114_q25_closeret` 看服务器上的 tag,`./scripts/study.sh digest F114_q25_closeret <tag>` 重看结果)。

## 研究现状(`notes/F114_q25_closeret/state.md`,10-04 23:46 更新)—— **先读这个文件**

# F114_q25_closeret — 研究现状(主研每轮覆盖重写)

第 3 轮主研(Opus 5,2026-10-04)。`cross_quantile_q25(day_close(Ret), 15)`,来源 挖掘 #1421。
**长表和推导不在这里**:各阶段看 `07_S1_shape.md`/`07_S2_where.md`/`07_S3_window.md`/`07_S4_long.md`/`07_S5_known.md`;
假设的正本是 `05_hypotheses.md` 末节;候选与判据是 `10_distilled.md`。

## 1. 一句话现状

实验全做完(24 变体 / 4 次运行),**结论已成形且是否定的**:对只能做多的用户,这条因子相对已知成交额家族
**没有可用的增量**(H12 被支持)。**本轮已裁决完 R2、把候选和判据写死在 `10_distilled.md`,并下了 `orders/R3.md`
(kind: final)。下一步(执行):跑那唯一一次 `study.sh final`。** 留出段**仍未读**。

(…全文 6172 字符,读 `notes/F114_q25_closeret/state.md`)

## 研究日志(`notes/F114_q25_closeret/journal.md`:22 条,其中研究员自己写的 13 条)

最近的 5 条(更早的和全文看文件):

### 2026-10-04 23:46 [主研] 第 3 轮:裁决 R2,证据已足够下否定结论,直接进留出段(工单 R3 = final,候选与判据已写死)

**看到了什么(R2 的 12 个变体)**
1. H16 被支持:窗口在 60 单峰。固定 hl20 的 train 多头腿净超额 w5 +1.5 / w15 +1.8 / w30 +2.6 / w60 +3.1 / w241 +1.1 ——
   w241 连原式都不如;它的 rIC 只 +0.0045(t 2.72)、train 剖面最高档在 Q6、2019/2020 多头腿**毛**超额为负(−2.9%/−2.0%)。
   **陷阱**:w241 的 valid +9.5% 是全研究最高,只看 valid 就会选它。上一轮事先写下的「valid 整段落在小盘/高波动制度里」
   在这里救了一次。w241 排除。
2. H17 被否定:`mean(…,60)` 只 +1.3%/+2.8%、固定 hl20 列 +0.9%(低于原式)→ 读「下四分位」在长窗口下仍必要。mean60 排除。
3. 新的已确立事实:`s4_iso`(= `day_close(Ret)` 自己,零记忆)原始 rIC **+0.0107(t 12.29,全研究最高)**、毛超额 +5.6%,
   但换手 10.4% → 净 −2.3%。滚动 q25 在毛超额几乎不掉(+5.6%→+5.8%)的前提下把换手压到 1/3.4,滚动均值也降频
   但把毛超额一起平掉(+3.0%)。→ **这棵树唯一真实的结构贡献是「用顺序统计量做保尾低通滤波」,买到的是换手而不是新信息。**
   归因在固定 hl20 列上成立,不是把平滑的功劳写成结构的。
4. H12 被支持(= 本研究的结论):① 家族 +12.6%/+22.3% 压过最好版本 3.5~5 倍,且家族 train 长端**严格单调**
   (Q8 +8.6 < Q9 +11.4 < Q10 +15.8),这棵树没有一个版本做到;② 残差腿 train 只 +0.4%~+0.7%,**没过我上一轮事先写的
   +1pp 判据**,逐年 2018/2019/2020 三年全负、正收益全在 2021 之后 —— 残差的「增量」和原式本身的病是同一个病(H11);
   ③ 等权组合 +12.0%/+21.4% vs 家族单独 +12.6%/+22.3%,**连毛超额的增量 +1.3pp/+0.9pp 都在 ±3pp 噪声带内**。

**判断**
- 「它不是已知暴露
…(这条日志还有后文,读 journal.md)

### 2026-10-04 23:51 [执行] R3:开始,准备读留出段

前置检查通过:ledger.json 24 条记录(8 train/8 utrain/8 valid),无 holdout;10_distilled.md 第9行已有「读留出段之前」一节,
候选(f_orig/f_w30/f_w60/f_fam/f_add)与判据 J1-J7 已写死。list 显示服务器无在跑任务,S6_final 未跑过。
准备按工单在 configs/F114_q25_closeret.yaml 追加 S6_final 阶段(5 变体,逐字照抄工单表达式)并替换 diagnostics/corr_ids 两块,
check 通过后跑唯一一次 study.sh final。

### 2026-10-04 23:53 [auto] ⚠ 读留出段:final S6_final,阶段 S6_final(留出段只能读这一次;候选与判据应当已经写在 10_distilled.md 里)

### 2026-10-04 23:56 [auto] S6_final 跑完(exit 0);重看结果:./scripts/study.sh digest F114_q25_closeret S6_final

### 2026-10-05 00:11 [执行] R3:final 跑完,留出段数字已读、结果卡 R3.md 写完

study.sh final F114_q25_closeret S6_final S6_final,exit 0,194.9s,errors={}。只跑了这一次,没有第二次调final。
J7自检:5个新id(f_orig/f_w30/f_w60/f_fam/f_add)的train/valid Lnet/Lshp与旧变体(v_base/s3_w30/s3_w60/f_fam_m30/
h12_add_best_m30)逐位相同,PASS,留出段数字可用。

最关键的数字(全部来自books_user,唯一含holdout的账本):
J1:f_orig holdout Lnet+0.22%/Lshp+0.03——比"train那一侧"的事前预期(+1.8%/+0.33)还低,不是落在train或valid哪一侧,
  是更弱。①Lnet<0否②Lshp<0否③≥5%且≥1.5否。
J2:f_w30−f_orig holdout Lnet+1.9pp/Lshp+0.22,f_w60−f_orig +1.6pp/+0.19,两条都满足"不更差"(≥−3pp/−0.3)。
J3:三条holdout Lnet都明显低于各自valid(差−6.2~−7.9pp),Lshp都<1.0,没有≥1.5的。按holdout Lnet排序最弱是
  f_orig(+0.22%),不是工单附注预设要查的f_w60(f_w60 +1.85%反而比f_orig强)。
J4(唯一能翻转总结论的判据):f_add−f_fam holdout Lnet差−3.47pp(精确值,越过了−3pp下沿,落进"等权加入有害"那支),
  Lshp差−0.174(在±0.3噪声带内,落在"没有增量"那支)——两个子判据指向不同分支,原样报出未下结论。
J5:f_fam holdout Lnet+14.1%/Lshp+1.51,落在用户给的[13%,15%]/[1.4,1.9]带内,口径交叉验证通过。
J6:f_w30 vs f_orig rank相关+0.9220,f_w60 vs f_orig+0.7608,与10_distilled.md记录一致(事前写死,本次只是复核)。

异常(已读partura/runner.py源码确认机制,不是猜测):
1) 工单要求确认sign/hlL/hlS是否为fit段那套(应为f_w60 −1/3/5)——四个变体对上了,**f_w60的hlL
…(这条日志还有后文,读 journal.md)

## 工单与结果卡(`notes/F114_q25_closeret/orders/`、`notes/F114_q25_closeret/results/`)

- R0:工单 —,结果卡 有
- R1:工单 有,结果卡 有
- R2:工单 有,结果卡 有
- R3:工单 有,结果卡 有

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
- **S6_final**(5 个变体):事前选定的 5 个最终候选在留出段上的多头腿:原式、提纯版(窗口30)、相近版(窗口60)、已知家族基准、家族+候选等权组合
  f_orig、f_w30、f_w60、f_fam、f_add

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F114_q25_closeret`)

- `S0_baseline`  10-04 11:57  1 个变体  → `./scripts/study.sh digest F114_q25_closeret S0_baseline`
- `S1_shape`  10-04 13:54  6 个变体  → `./scripts/study.sh digest F114_q25_closeret S1_shape`
- `S2_aperture`  10-04 14:08  6 个变体  → `./scripts/study.sh digest F114_q25_closeret S2_aperture`
- `S4_horizon`  10-04 15:08  6 个变体  → `./scripts/study.sh digest F114_q25_closeret S4_horizon`
- `S5_known`  10-04 15:16  6 个变体  → `./scripts/study.sh digest F114_q25_closeret S5_known`
- `S6_final`  10-04 23:56  5 个变体  → `./scripts/study.sh digest F114_q25_closeret S6_final`

## 已写的 notes(`notes/F114_q25_closeret/`)

`01_expression.md`(3K)、`02_operators.md`(8K)、`03_decomposition.md`(2K)、`04_grammar.md`(6K)、`05_hypotheses.md`(26K)、`06_baseline.md`(14K)、`07_S1_shape.md`(7K)、`07_S2_where.md`(5K)、`07_S3_window.md`(7K)、`07_S4_long.md`(8K)、`07_S5_known.md`(7K)、`10_distilled.md`(16K)、`journal.md`(34K)、`state.md`(9K)

## 自写的探针与分析脚本(`studies/F114_q25_closeret/`)

(无)

## 结构化结果(`handoff/F114_q25_closeret/results/`)

(还没有)
