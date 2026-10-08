# F113_nested_tsmax_demean — 交接状态

_自动生成于 2026-10-06 11:56(`python scripts/recorder.py --brief F113_nested_tsmax_demean` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #1375(批次 B01_single_factors)
- 表达式:`pow_1_5(ts_max(pow_2(cs_demean(mul(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(day_mean(Ret), 5), -5)), 30)), 20), 5))), 30))`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- **留出段已经读过 2 次**(10-04 23:50, 10-05 12:14)—— **不许再读**。候选在留出段上的数全在 `runs/F113_nested_tsmax_demean/final.json`(`./scripts/study.sh digest F113_nested_tsmax_demean final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `synth:F113_nested_tsmax_demean`:已返回结果,最后动作 10-05 11:15 → `handoff/F113_nested_tsmax_demean/agents/synth_a24c39d4d136d4c36.md`
  - `verdict:F113_nested_tsmax_demean`:失败,最后动作 10-05 15:34 → `handoff/F113_nested_tsmax_demean/agents/verdict_af3628082ff5e07ad.md`
  - `verdict:F113_nested_tsmax_demean`:已返回结果,最后动作 10-05 17:15 → `handoff/F113_nested_tsmax_demean/agents/verdict_a2288ebb0f74dbfec.md`

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F113_nested_tsmax_demean` 看服务器上的 tag,`./scripts/study.sh digest F113_nested_tsmax_demean <tag>` 重看结果)。

## 研究现状(`notes/F113_nested_tsmax_demean/state.md`,10-05 17:11 更新)—— **先读这个文件**

# 研究现状 — F113_nested_tsmax_demean

> 主研每轮**整个覆盖重写**这一页。最近更新:**第 6 轮(主研 Opus 5)批量扫描 s2 的对账与结论,2026-10-05**。
> 表达式:`pow_1_5(ts_max(pow_2(cs_demean(mul(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(day_mean(Ret), 5), -5)), 30)), 20), 5))), 30))`
> 噪声带:`Lnet`(多头腿净超额,扣 15bp)**±3pp**、`Lshp`(纯多头夏普)**±0.3**;门槛 cov ≥ 0.95、dist ≥ 0.5。
> 完整论证在 **`notes/<fid>/synthesis.md`**:§1–5 是 s1 的综合,**§6–8 是本轮的对账与定论(先读 §8)**。

## 1. 现状

**结案方向没变,本轮把「为什么」钉死,并找到唯一值得继续的东西。**
原式多头腿 utrain **+0.7% / Lshp 0.17**、6 年 3 年为负;它「有信息」那段(`h_s4` +8.0% / 1.17)**过得了 dist 门槛但过不了
成交额桶内中性**(→ `h_q1` +1.8% / 0.25),ρk +0.46 ⇒ **3/4 是已知成交额族的弱复制**;筛子用法与 `k_known` 逐格打平,
远不及通用筛 `k_known_xfrozen`(**+18.5% / 3.15**)。**产出不在原式身上,在一条新因子**
`h_g6_gini_bk_amt` = `cs_bucket_rank(cross_mean(day_gini(Ret),30), cross_mean(day_sum(Amt),30))`
+8.1% / **2.00** / LTO 1.8% / **ρk +0.05** / ρo +0.08 / 6 年全正 —— 应独立立案。
**下一步:执行跑 `studies/<fid>/hypo3.yaml` 的 25 条(已 25/25 过 `study.sh hypo3`)。**

(…全文 6604 字符,读 `notes/F113_nested_tsmax_demean/state.md`)

## 研究日志(`notes/F113_nested_tsmax_demean/journal.md`:24 条,其中研究员自己写的 13 条)

最近的 5 条(更早的和全文看文件):

### 2026-10-04 23:50 [auto] S_final 跑完(exit 0);重看结果:./scripts/study.sh digest F113_nested_tsmax_demean S_final

### 2026-10-04 23:59 [执行] R3:final S_final 已读留出段(exit 0,5/5 无错,服务器 5/8)——P0~P5 机械判据全部未被否定,但两处工单没预先设想的新事实:f_cb holdout 比 f_kf30 差 5.17pp/0.465(超噪声带,不是预写的'打平'),f_c4/f_m1 valid→holdout 衰减 9~12pp 远超 f_kf30 自己的 1.3pp

决策留给下一轮主研,这里只记数字(全部多头口径 Lnet/Lshp,holdout 列用 books_user 即 fit=utrain 的书,未在 holdout 上重选方向/半衰期):

- f_orig: train +1.60%/+0.39, valid -1.73%/-0.52, utrain +0.68%/+0.17, holdout -0.58%/-0.15 → P1(原式多头腿不可用)holdout 复现,未被否定。
- f_c4: train +6.87%/+0.92, valid +13.26%/+2.07, utrain +8.71%/+1.21, holdout +1.44%/+0.14 → 比 valid 掉 11.9pp。
- f_m1: train +3.17%/+0.43, valid +14.75%/+2.41, utrain +6.48%/+0.93, holdout +5.15%/+0.60 → 比 valid(utrain)掉 9.6pp 之内更小;holdout 上 f_m1 > f_c4(train 是反过来)。
- f_kf30: train +12.62%/+1.78, valid +22.33%/+3.46, utrain +15.40%/+2.22, holdout +14.10%/+1.51 → P0(用户表口径校准,期望 8~20%/1.0~2.5)、P5(自身稳,期望 Lshp≥0.5)都通过,基准本身在 holdout 上最稳。
- f_cb: train +12.52%/+1.76, valid +22.41%/+3.56, utrain +15.36%/+2.22, holdout +8.93%/+1.04 → 比 f_kf30 holdout 低 5.17pp/0.465(train/valid/utrain 三段都接近 f_kf30,holdout 这一段明显拉开)。
- P3(有无增量)两个否定条件(f_cb 或 f_c4/f_m1 比 f_kf30 高 ≥3pp)都不成立
…(这条日志还有后文,读 journal.md)

### 2026-10-05 00:20 [主研] 第4轮:裁决留出段——P0~P5全部未被否定,推荐仍是事前第一推荐f_kf30(本因子任何版本都不用);新事实是f_cb在holdout比f_kf30低5.17pp(负增量)、f_c4掉进噪声带而4节点的f_m1反而撑住;已写完09/10读后/11/12/08/07_S_final并下成文工单R4(0次服务器运行)

看到了什么(全部多头口径,holdout 列来自 books_user,fit=utrain,未在 holdout 上重选;噪声带 Lnet ±3pp / Lshp ±0.3):

判据逐条(10_distilled.md §4 已逐行落盘,事前写死的候选/排序/推荐一个字没改):
- P0 不只是"没被否定",是一次干净的口径对齐:f_kf30 holdout +14.10% / 1.509,正落在用户给的测试段参考
  (+13%~+15% / 1.4~1.9)的中间 → holdout 这一列可以直接拿去和用户自己的表比,下面所有 pp 差都有意义。
- P1:f_orig 三段 +1.60% / -1.73% / -0.58%(Lshp +0.39/-0.52/-0.15)——三段全在噪声带内、两段为负;
  逐年 8 年里 4 年为负;多头腿只占多空毛差价的 15.7%/4.3%/15.0% → 三段都有 >=84% 的钱在空头腿。
  注意措辞:"几乎全在空头腿"最贴 valid(95.8%),holdout 是 85.0%,别写成 96%。
- P2 只被 f_m1 兑现:f_m1 holdout +5.15% / +0.603(噪声带外,真实但弱);f_c4 只有 +1.44% / +0.137,
  整条掉进噪声带。事前写的"两条都为正、量级 +5%~+15%"只中了一条。
- P3(最重要)两个否定条件都不成立:f_cb - f_kf30 = -5.17pp / -0.465;f_c4 - f_kf30 = -12.66pp;
  f_m1 - f_kf30 = -8.95pp。碾压这件事四列 16 格一格没翻。
- P4:|f_c4 - f_m1| holdout 3.71pp < 6pp 且方向与 train 相反 → 未被否定,H14 反而加强。
- P5:f_kf30 holdout Lshp 1.509,utrain→holdout 只掉 1.30pp,逐年 8 年全正 → 分母是可靠的。
→ P1~P5 全部未被否定,走事前约定的"预期情形"写法。

判断是什么:
…(这条日志还有后文,读 journal.md)

### 2026-10-05 11:06 [主研] 批量扫描 s1 的综合

读完 189 变体的大表 + 市场解剖,写了 notes/synthesis.md(150 行)和第二批 40 条假设 studies/hypo.yaml(40/40 过 hypo 检查)。

1. 最大的新发现是一个精度 bug:`sub(x, -5)` 在信息上被下一层 cs_demean 精确抵消(iso_B 与 iso_C 的 ut、ρk 逐格相同:
   −2.6% / ρk +0.50),但把 float32 截面分辨率砸掉 78%(dist 1.00 → 0.22);abl_C 删掉它收益不变(+0.6%)而 dist 回 1.00;
   极端版 sub_H_add(把 5 加在 ~1e-8 的量上)dist 0.00、LTO 0.2%。→ 整个有信息的子树族(iso_D~I dist 0.22–0.26、
   abl_I 0.28)是被这个常数判了 dist 门槛的死刑,不是没信息。第二批 h_s1~h_s7 / h_g1 就是"去掉 +5 再跑"。
2. abl_J 的 +12.4% / Lshp 2.38 不能信:J 位置保号的 5 条(abl_J、pow_1_5、pow_05、signedpower、inv)全在 +11.8~+13.7%
   且 cov 全是 0.43(pow_1_5 对负数返回 NaN,剔掉 57% 的票),折叠的 2 条(abs_、sqrt)全是 +0.8% / cov 1.00 ——
   与 universe 筛选完全混淆。h_s1(保号不 NaN)对 h_s2(abs 折叠)拆这一对。
3. 全表唯一既过门槛(cov 1.00 / dist 0.97)又显著赢原式的是叶子替换 nosc_A_day_gini:+6.3% / Lshp 1.44、ρo 0.06、ρk 0.20,
   逐年 6 年 5 正,次新段内 +17.9%,但封板段内 −41.4%。它其实是一条新因子(日内集中度),第二批重心放在它身上。
4. 解剖:原式只在成交额最高 20%(段内 +8.8%)和有冻结盘口(+11.9%)里有段内信息,无冻结的 93.5% 是 −2.3%,
   6 年 3 年为负 → 相当一部分是"伪装成收益因子的冻结分钟探测器"(F108 教训)。窗口 15 条、记忆 28 条全在噪声带内,
   没有平台、没有半衰期杠杆。
5. 增量仍然是没有:ov_p025 +14.8% / 2.27 vs 已知族 +15.4% / 2.22(两项
…(这条日志还有后文,读 journal.md)

### 2026-10-05 16:13 [主研] 批量扫描 s2 对账与结论

对账(s1 的推论):支持 5 条、否定 7 条。H16 确认且最干净 —— h_s3~h_s6 删掉 +5 后三段收益与 ρk 逐格不变而 dist 0.22→1.00
(例外:gini 叶子量级 ~0.5,h_g1 与 nosc_A 完全同格);H17 确认但两份功劳都在 —— 全覆盖保号的 h_s1 只有 +7.6%/1.07,
abl_J 的 +12.4%/2.38 里 4.8pp 归 NaN 剔掉的 57%,而 h_s1 比折叠版 h_s2(+3.5%,valid −0.6%)高 4.1pp 说明符号也值 ~4pp。
否定:冻结分钟探测器(h_f1 与原式 ρo 仅 +0.04,而它自己 +5.7% 远好于原式)、「有界叶子⇒双层折叠无害」(pos_ratio/centroid/
wmean/signed_ratio 全负)、「gini 后 6 层是装饰」(最小形 h_g3 −10.6%)、秩距离(h_r1~r3 valid 全负)、手写择时(≈0 且 LTO 翻倍)、
记忆杠杆(h_m1~m3 ≤ +0.1%)。

定论:原式多头腿不可用、当筛子也不可用。它「有信息」那段(h_s4 +8.0%/1.17)过得了 dist 门槛但过不了成交额桶内中性
(h_q1 +1.8%/0.25),ρk +0.46 ⇒ 3/4 是已知成交额族。筛子 scr_xhi_* +15.2%/2.24 与 k_known 逐格打平,远不及新基准
k_known_xfrozen(+18.5%/3.15);best_on_known 的 h_k2 +17.2%/2.66 赢 k_known 但输 xfrozen 筛 1.3pp/0.49 夏普,且分子单独为负。

意外发现(本轮唯一值得继续的):h_g6_gini_bk_amt = cs_bucket_rank(cross_mean(day_gini(Ret),30), cross_mean(day_sum(Amt),30))
+8.4/+7.1/+8.1%、Lshp 2.00、LTO 1.8%、ρo +0.08、ρk +0.05、cov/dist 双 1.00、6 年全正、状态不敏感 —— 而分子单独是 −1.3%/−0.19。
同一分子换四种桶(裸用 −1.3 / 成交额桶 +8.1 / 已知族桶 +6.5 但 valid 2.8 / 冻结度桶 −1.3)+ 反向(h_s3 +7.9 → 桶内 +1.8)
⇒ 新结论 H18:「桶内比较」是会改
…(这条日志还有后文,读 journal.md)

## 工单与结果卡(`notes/F113_nested_tsmax_demean/orders/`、`notes/F113_nested_tsmax_demean/results/`)

- R0:工单 —,结果卡 有
- R1:工单 有,结果卡 有
- R2:工单 有,结果卡 有
- R3:工单 有,结果卡 有
- R4:工单 有,结果卡 **还没有(待执行)**

## 配置里的实验计划(`configs/F113_nested_tsmax_demean.yaml`)

- 标题:两层嵌套的「日轴 MAX 记忆 → 截面去均值 → 平方折叠」(只用 Ret):最终排序的是「近 54 日极端收益幅度离当日截面均值的距离」,sign=-1 即做多「极端程度最接近截面典型值、且 30 日内没偏离过」的股票
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base
- **S1_chain**(10 个变体):沿这条不分支的链逐节点消融 + 把外层折叠的中心挪到中位数/秩空间:多头腿是差还是没有意义?哪些节点是多余的?
  c1_b_max5、c2_e_rel34、c3_g_fold1、c4_nodemean_out、c5_nopow15、c6_nomul_nosub、c7_nofold_in、c8_nofold_out、c9_rankfold、c10_medfold
- **S2_bench**(10 个变体):c4 这一类候选是不是朴素长窗 MAX / 低波动的改写?最小结构能不能保住它的多头腿?它相对已知家族有没有增量?
  n2_max79_plain、n4_dvol50_plain、m1_rel79_max、m2_rel50_absmax、m3_rel50_absmean、w1_c4_62、w2_c4_102、kf_mean30、kf_max9、cb_c4_kf30
- **S_final**(5 个变体):留出段(holdout, 20230808 起)读一次:原式多头腿不可用/最好子结构(c4,m1)被已知家族碾压/相对已知家族无增量,这三条 train+valid 事前结论是否仍成立(判据 P0~P5,10_distilled.md §3,事前写死)
  f_orig、f_c4、f_m1、f_kf30、f_cb

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F113_nested_tsmax_demean`)

- `S0_baseline`  10-04 11:57  1 个变体  → `./scripts/study.sh digest F113_nested_tsmax_demean S0_baseline`
- `S1_chain`  10-04 14:03  10 个变体  → `./scripts/study.sh digest F113_nested_tsmax_demean S1_chain`
- `S2_bench`  10-04 15:12  10 个变体  → `./scripts/study.sh digest F113_nested_tsmax_demean S2_bench`
- `S_final`  10-04 23:50  5 个变体  → `./scripts/study.sh digest F113_nested_tsmax_demean S_final`
- `sweep_s1`  10-05 10:44  189 个变体  → `./scripts/study.sh digest F113_nested_tsmax_demean sweep_s1`
- `anatomy_s1`  10-05 10:49  0 个变体  → `./scripts/study.sh digest F113_nested_tsmax_demean anatomy_s1`
- `sweep_s2`  10-05 12:02  240 个变体  → `./scripts/study.sh digest F113_nested_tsmax_demean sweep_s2`
- `anatomy_s2`  10-05 12:14  0 个变体  → `./scripts/study.sh digest F113_nested_tsmax_demean anatomy_s2`
- `sweepfinal_s2`  10-05 12:16  8 个变体  → `./scripts/study.sh digest F113_nested_tsmax_demean sweepfinal_s2`
- `sweep_s3`  10-05 17:54  265 个变体  → `./scripts/study.sh digest F113_nested_tsmax_demean sweep_s3`
- `anatomy_s3`  10-05 18:04  0 个变体  → `./scripts/study.sh digest F113_nested_tsmax_demean anatomy_s3`
- `sweepfinal_s3`  10-05 18:08  8 个变体  → `./scripts/study.sh digest F113_nested_tsmax_demean sweepfinal_s3`
- `sweep_s4`  10-06 10:46  265 个变体  → `./scripts/study.sh digest F113_nested_tsmax_demean sweep_s4`
- `anatomy_s4`  10-06 10:54  0 个变体  → `./scripts/study.sh digest F113_nested_tsmax_demean anatomy_s4`
- `sweepfinal_s4`  10-06 10:59  8 个变体  → `./scripts/study.sh digest F113_nested_tsmax_demean sweepfinal_s4`
- `x1_ties`(自写脚本的输出)  10-04 14:22  exit 0  → `logs/F113_nested_tsmax_demean_x1_ties.log`
- `x2_increment`(自写脚本的输出)  10-04 15:35  exit 0  → `logs/F113_nested_tsmax_demean_x2_increment.log`

## 已写的 notes(`notes/F113_nested_tsmax_demean/`)

`01_expression.md`(4K)、`02_operators.md`(10K)、`03_decomposition.md`(7K)、`04_grammar.md`(8K)、`05_hypotheses.md`(27K)、`06_baseline.md`(13K)、`07_S1_chain.md`(7K)、`07_S2_bench.md`(10K)、`07_S_final.md`(9K)、`07x_1_ties_longbook.md`(5K)、`07x_2_increment.md`(9K)、`08_variants.md`(7K)、`09_diagnosis.md`(10K)、`10_distilled.md`(12K)、`11_risks.md`(6K)、`12_next.md`(4K)、`journal.md`(39K)、`state.md`(9K)、`synthesis.md`(20K)

## 自写的探针与分析脚本(`studies/F113_nested_tsmax_demean/`)

- `x1_ties_and_longbook.py`  10-04 14:17  studies/F113_nested_tsmax_demean/x1_ties_and_longbook.py -- 工单 R1 (B)。
- `x2_increment.py`  10-04 15:33  studies/F113_nested_tsmax_demean/x2_increment.py -- 工单 R2 (B)。

## 结构化结果(`handoff/F113_nested_tsmax_demean/results/`)

- `synthesis.json`
- `verdict.json`
