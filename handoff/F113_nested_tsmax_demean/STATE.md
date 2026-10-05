# F113_nested_tsmax_demean — 交接状态

_自动生成于 2026-10-05 10:53(`python scripts/recorder.py --brief F113_nested_tsmax_demean` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #1375(批次 B01_single_factors)
- 表达式:`pow_1_5(ts_max(pow_2(cs_demean(mul(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(day_mean(Ret), 5), -5)), 30)), 20), 5))), 30))`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- **留出段已经读过 1 次**(10-04 23:50)—— **不许再读**。候选在留出段上的数全在 `runs/F113_nested_tsmax_demean/final.json`(`./scripts/study.sh digest F113_nested_tsmax_demean final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `lead:F113_nested_tsmax_demean#1`:已返回结果,最后动作 10-04 23:27 → `handoff/F113_nested_tsmax_demean/agents/lead_R1_add6bc7c98edb6748.md`
  - `work:F113_nested_tsmax_demean#1`:已返回结果,最后动作 10-04 23:59 → `handoff/F113_nested_tsmax_demean/agents/work_R1_a696126293179fc51.md`
  - `lead:F113_nested_tsmax_demean#2`:已返回结果,最后动作 10-05 00:20 → `handoff/F113_nested_tsmax_demean/agents/lead_R2_ad80c965745ae9bd7.md`

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F113_nested_tsmax_demean` 看服务器上的 tag,`./scripts/study.sh digest F113_nested_tsmax_demean <tag>` 重看结果)。

## 研究现状(`notes/F113_nested_tsmax_demean/state.md`,10-05 00:19 更新)—— **先读这个文件**

# 研究现状 — F113_nested_tsmax_demean

> 主研每轮**整个覆盖重写**这一页。最近更新:**第 4 轮(主研 Opus 5),2026-10-05**。
> 表达式:`pow_1_5(ts_max(pow_2(cs_demean(mul(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(day_mean(Ret), 5), -5)), 30)), 20), 5))), 30))`
> 噪声带:`Lnet`(多头腿净超额,扣 15bp)**±3pp**、`Lshp`(纯多头夏普)**±0.3**。

## 1. 一句话现状

**研究已经做完,结论是否定的;留出段读过了,判断类 notes 也写完了。本轮下的是成文工单 R4(kind: writeup)。**
事前判据 **P0~P5 全部未被否定**,推荐就是事前第一推荐:**`f_kf30` = `cross_mean(day_std(Amt), 30)`(已知家族),
即本因子任何版本都不采用**。
**下一步:执行按 `orders/R4.md` 核对数字 + 出报告 + 写 `results/R4.md`(0 次服务器运行),然后整个研究结案。**
服务器运行 **5 / 8**(S1 1 + S2 1 + `x2_increment` 2 次 `exec` + `final` 1;S0 不计),R4 用 0 → 仍是 5/8。

(…全文 6348 字符,读 `notes/F113_nested_tsmax_demean/state.md`)

## 研究日志(`notes/F113_nested_tsmax_demean/journal.md`:22 条,其中研究员自己写的 11 条)

最近的 5 条(更早的和全文看文件):

### 2026-10-04 23:26 [主研] 第3轮:裁决R2——不是朴素MAX但MAX语义是装饰、唯一load-bearing的是第一次cs_demean;候选被已知家族两段碾压且三条口径都没增量 → 结论否定,直接进留出段(工单R3,kind:final,5候选)

看到了什么(全部 train/valid,多头口径,扣费;噪声带 Lnet ±3pp / Lshp ±0.3):

Q1(是不是朴素长窗 MAX / 波动)——答案是"都不是,但代价是 MAX 语义自己也是装饰":
- c4 × n2_max79_plain 的 rank 相关 +0.948 看着像"同一条",但 n2 的 Lnet −0.3%/+8.6%、train Lshp −0.04,
  比 m1(相对 MAX,+3.2%/+14.8%)两段都差 3.5pp/6.2pp,夏普差 0.47/1.25 → 两段同向出噪声带。
  同样地 m3(平均绝对相对收益 +2.1%/+13.3%)比 n4(朴素波动 −5.5%/+4.1%)两段好 7.6pp/9.2pp。
  → **真正 load-bearing 的只有第一次 cs_demean(把当天截面均值减掉)**,这是整条树唯一两段一致有用的算子(新 H13)。
- 但 m2(abs max)vs m3(abs mean)只差 0.6pp/1.3pp(噪声内,相关 +0.808)→ **极值记忆是装饰**,
  它卖的是"相对振幅的水平",名字(nested_tsmax)误导人。
- 族内排序两段翻转:c4 − m1 = train +3.7pp / valid −1.5pp;7 个成员 valid 全在 +12.7~14.8%(跨度 2.1pp)
  → **嵌套结构没买到可复现的优势**(新 H14)。所以 R1 那句"结构更好"必须改写。
  选 c4 当族代表的唯一两段站得住的理由:从 S1_chain.json 补出的分位剖面显示 c4 两段的最高档都在 Q10,
  而 n2/m1 在 train 的 Q10 比 Q8/Q9 低 6.6/3.7pp(顶档塌)。

Q2(相对已知家族有没有增量)——干净的否定,三条独立口径一致:
- 已知家族被 R1 低估了:kf_mean30 +12.6%/+22.3%(hl=0)、kf_max9 +13.7%/+22.2%(hl=5);06_baseline §8 的
  +9.3%/+18.5% 正是 kf_max9 的 hl=0 行 → R0 异常①/③结案。c4 比 kf_mean
…(这条日志还有后文,读 journal.md)

### 2026-10-04 23:43 [auto] ⚠ 读留出段:final S_final,阶段 S_final(留出段只能读这一次;候选与判据应当已经写在 10_distilled.md 里)

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
- `x1_ties`(自写脚本的输出)  10-04 14:22  exit 0  → `logs/F113_nested_tsmax_demean_x1_ties.log`
- `x2_increment`(自写脚本的输出)  10-04 15:35  exit 0  → `logs/F113_nested_tsmax_demean_x2_increment.log`

## 已写的 notes(`notes/F113_nested_tsmax_demean/`)

`01_expression.md`(4K)、`02_operators.md`(10K)、`03_decomposition.md`(7K)、`04_grammar.md`(8K)、`05_hypotheses.md`(27K)、`06_baseline.md`(13K)、`07_S1_chain.md`(7K)、`07_S2_bench.md`(10K)、`07_S_final.md`(9K)、`07x_1_ties_longbook.md`(5K)、`07x_2_increment.md`(9K)、`08_variants.md`(7K)、`09_diagnosis.md`(10K)、`10_distilled.md`(12K)、`11_risks.md`(6K)、`12_next.md`(4K)、`journal.md`(35K)、`state.md`(10K)

## 自写的探针与分析脚本(`studies/F113_nested_tsmax_demean/`)

- `x1_ties_and_longbook.py`  10-04 14:17  studies/F113_nested_tsmax_demean/x1_ties_and_longbook.py -- 工单 R1 (B)。
- `x2_increment.py`  10-04 15:33  studies/F113_nested_tsmax_demean/x2_increment.py -- 工单 R2 (B)。

## 结构化结果(`handoff/F113_nested_tsmax_demean/results/`)

(还没有)
