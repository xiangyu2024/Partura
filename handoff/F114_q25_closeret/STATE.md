# F114_q25_closeret — 交接状态

_自动生成于 2026-10-05 17:15(`python scripts/recorder.py --brief F114_q25_closeret` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #1421(批次 B01_single_factors)
- 表达式:`cross_quantile_q25(day_close(Ret), 15)`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- **留出段已经读过 3 次**(10-04 23:56, 10-05 11:08, 10-05 12:21)—— **不许再读**。候选在留出段上的数全在 `runs/F114_q25_closeret/final.json`(`./scripts/study.sh digest F114_q25_closeret final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `synth:F114_q25_closeret`:已返回结果,最后动作 10-05 10:47 → `handoff/F114_q25_closeret/agents/synth_a0afe0974e2c8e717.md`
  - `verdict:F114_q25_closeret`:失败,最后动作 10-05 15:35 → `handoff/F114_q25_closeret/agents/verdict_ac75f20cce9734707.md`
  - `verdict:F114_q25_closeret`:已返回结果,最后动作 10-05 17:15 → `handoff/F114_q25_closeret/agents/verdict_adfbc90eeee4b463a.md`

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F114_q25_closeret` 看服务器上的 tag,`./scripts/study.sh digest F114_q25_closeret <tag>` 重看结果)。

## 研究现状(`notes/F114_q25_closeret/state.md`,10-05 17:12 更新)—— **先读这个文件**

# F114_q25_closeret — 研究现状(主研每轮覆盖重写)

第 5 轮主研(Opus 5,2026-10-05)。`cross_quantile_q25(day_close(Ret), 15)`,来源 挖掘 #1421。
本轮**只读**预先跑好的批量扫描 **s2**(129 变体 + 市场解剖),**没有起任何计算、没有读测试段**。
正本 `synthesis.md`(末节 = 本轮对账与结论)、`10_distilled.md`、`05_hypotheses.md`、`07_S1~S5`。

## 1. 一句话现状

**结论已定且是否定的。** 冻结盘口(0 原子)**是污染不是信息** —— 剔掉它把本因子夏普从 0.70 抬到 1.71
(`seg_xfrozen_m`,ρk −0.02,train/valid 逐位一致),这是全程唯一一次真正的提纯;但剔干净后剩下的只是
一个**比已知成交额族小一半**、桶内中性后归零的低流动性倾斜。叠到已知族上只有噪声级增量(夏普 +0.3),
**且一律输给通用筛子 `k_known_xfrozen`(+18.5%、3.15)**。「当筛子」这条 s1 留下的活口已被 s2 否掉。
**下一步(执行):跑 `hypo3.yaml` 的 25 条,train/valid,优先级 W → Q → R → S。**

(…全文 6160 字符,读 `notes/F114_q25_closeret/state.md`)

## 研究日志(`notes/F114_q25_closeret/journal.md`:24 条,其中研究员自己写的 15 条)

最近的 5 条(更早的和全文看文件):

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

### 2026-10-05 10:36 [主研] 批量扫描 s1 的综合

73 变体大表 + 市场解剖读完,写进 `notes/F114_q25_closeret/synthesis.md`;第二批 39 条假设在
`studies/F114_q25_closeret/hypo.yaml`(39/39 parse)。

1. **载重的不是 q25,是输入在 0 上的点质量**:同槽位 q50 → dist 0.16、底腿 +19.0%→+0.2%、LS +2.36→−0.02;
   日内中位数 dist 0.02、LTO 0.004。孔径放宽到 5 分钟(leaf_Ret_ret5)净超额 +3.6%→+0.1%。
   这个 0 原子 = 封板/停牌/无收盘成交的「冻结盘口」,与 F108 的发现同源。**日内分钟量侧叶子全退化**
   (volchg/amtchg dist 0.00)→ 用户「Ret↔量变化率可互换」在这棵树上不成立,因为量没有符号。
2. **多头腿的超额全部是跨成交额桶的倾斜**:成交额五分位段内多头书 −0.7/−2.7/−6.5/−4.2/−5.1 **全负**,
   全市场 +3.6% 来自对最低桶超配 +10.7%。res_known/res_liq 只 +1.8%(train +0.4%)。
3. **慢化只值换手**:w5→w60 单调上坡(+2.9→+5.1),w60 的 hlL 自动掉到 3;mem_ema30 +5.0%/Lshp 0.93 最好。
   毛超额不随慢化上升 → +1.4pp 全是换手。cross_zscore / rel60 全塌 → 载重的是持久截面水平,不是时序事件。
4. **相对已知族是严格稀释**,不只是 wash:6 个 overlay 权重**全部**低于家族单独(+15.4%),|w| 单调向下
   (ov_p025 +12.9 / p05 +12.5 / p10 +11.5 / m05 +7.3)。两分段同向。留出段 f_add +10.6% vs f_fam +14.1% 再次印证。
5. **唯一活口**:近 15 日有冻结盘口段(占 6.5%、段等权 −67.4%)这棵树 +7.7%(mem_min60 +21.6%)而**家族 −10.9%**;
   次新段(7.1%、−28.7%)这棵树 +18.1%。→ 增量只可能以**单尾筛子**存在(G 组 pow_3 / 软 AND),不是线性混合。
6. **制度**:2018–2020 三年 ≈0 或负,2021
…(这条日志还有后文,读 journal.md)

### 2026-10-05 16:12 [主研] 批量扫描 s2 对账与结论

对账:第二批九组全跑完。否定 ⑤(day_flat_ratio 复现原子:A 组 6 条 train 全负 valid 全正)、⑤'(资金加权:B 组 6/6 全负,h_wmean_q25 -14.4 ≈ day_mean -15.9 → 塌陷来自全天聚合本身)、恒等式分解(h_sd_close60 -15.6)、「微观冲击计」(h_amihud15 -4.8)、以及 s1 留下的唯一活口「当已知族的单尾筛子」(scr_xhi_p 2.07、scr_xhi_m 1.75,两个方向都差于不筛 2.22)。支持 E 组(慢化串联无加法,上限 +5.0%/0.93 钉死)、H 组(状态加权是全表最好的叠加)、(乙)跨桶倾斜是全部(桶内 +1.7,dist 0.99 干净)。
最重要的改判:冻结盘口是污染不是信息。seg_xfrozen_m(原式剔掉近 15 日冻结最重 20%)+5.8/+5.6、夏普 1.80/1.50、ρk -0.02、dist 1.00 —— 夏普比原式(0.70)翻 2.4 倍且 train/valid 逐位一致,全表最稳。s1「0 原子 = 一半信息」作废。
定论:best_own = seg_xfrozen_m / h_amtexp_mul(+4.3/+12.2、ρk 0.28)/ seg_new_p,全部 ≤ k_known 的一半 → 多头腿仍不可用。best_on_known = h_gate_vol_mix(+16.9/2.58)、h_ov_slowf_pow3(2.49)、h_ov_flat_p025(2.56 但两段相反),对 k_known 只有夏普 +0.3 的噪声级增量,且全部输给通用筛子 k_known_xfrozen(+18.5/3.15)1.6~2.1pp。verdict = 多头腿不可用 + 只是已知族;提纯成功一次但量级只有基准 1/3,升华失败。
新增三条解剖事实:已知族的多头书整本在成交额最低 40%(z_known_lowliq 与 k_known 逐位相同)而它在最低 20% 桶段内 -4.1%、超配 +80.3% → 增量的位置 = 已知族扎堆桶的桶内重排;叠加项的凸度与冻结段表现单调(p025 -17.1 → p05 -6.4 → pow3 +10.2);flat overlay 的增量落在 2018-2020 和熊市/高波动段,gate 版落在 2021-2022 → 这就是 train/valid 分歧的来源。
第三
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
- `sweep_s1`  10-05 00:52  73 个变体  → `./scripts/study.sh digest F114_q25_closeret sweep_s1`
- `anatomy_s1`  10-05 10:19  0 个变体  → `./scripts/study.sh digest F114_q25_closeret anatomy_s1`
- `sweep_s2`  10-05 12:17  129 个变体  → `./scripts/study.sh digest F114_q25_closeret sweep_s2`
- `anatomy_s2`  10-05 12:21  0 个变体  → `./scripts/study.sh digest F114_q25_closeret anatomy_s2`
- `sweepfinal_s2`  10-05 12:23  8 个变体  → `./scripts/study.sh digest F114_q25_closeret sweepfinal_s2`

## 已写的 notes(`notes/F114_q25_closeret/`)

`01_expression.md`(3K)、`02_operators.md`(8K)、`03_decomposition.md`(2K)、`04_grammar.md`(6K)、`05_hypotheses.md`(26K)、`06_baseline.md`(14K)、`07_S1_shape.md`(7K)、`07_S2_where.md`(5K)、`07_S3_window.md`(7K)、`07_S4_long.md`(8K)、`07_S5_known.md`(7K)、`10_distilled.md`(16K)、`journal.md`(39K)、`state.md`(10K)、`synthesis.md`(17K)

## 自写的探针与分析脚本(`studies/F114_q25_closeret/`)


## 结构化结果(`handoff/F114_q25_closeret/results/`)

- `synthesis.json`
- `verdict.json`
