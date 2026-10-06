# F106_erm_mag_gap_1m — 交接状态

_自动生成于 2026-10-05 19:23(`python scripts/recorder.py --brief F106_erm_mag_gap_1m` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:手写 erm_mag_gap_1m(批次 B01_single_factors)
- 表达式:`sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Ret, 0))), add(day_sum(is_gt(Ret, day_quantile(Ret, 0.95))), create_like(day_quantile(Ret, 0.95), 1e-06))), add(day_quantile(Ret, 0.95), create_like(day_quantile(Ret, 0.95), 1e-06))), div(div(day_sum(select_where(is_lt(Ret, day_quantile(Ret, 0.05)), abs_(Ret), create_like(Ret, 0))), add(day_sum(is_lt(Ret, day_quantile(Ret, 0.05))), create_like(day_quantile(Ret, 0.05), 1e-06))), add(abs_(day_quantile(Ret, 0.05)), create_like(day_quantile(Ret, 0.05), 1e-06))))`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- **留出段已经读过 2 次**(10-04 15:35, 10-05 12:15)—— **不许再读**。候选在留出段上的数全在 `runs/F106_erm_mag_gap_1m/final.json`(`./scripts/study.sh digest F106_erm_mag_gap_1m final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `synth:F106_erm_mag_gap_1m`:已返回结果,最后动作 10-05 11:20 → `handoff/F106_erm_mag_gap_1m/agents/synth_a2e1488766b481d6b.md`
  - `verdict:F106_erm_mag_gap_1m`:中断,最后动作 10-05 13:53 → `handoff/F106_erm_mag_gap_1m/agents/verdict_a5251c36b37e7743a.md`
  - `verdict:F106_erm_mag_gap_1m`:已返回结果,最后动作 10-05 15:18 → `handoff/F106_erm_mag_gap_1m/agents/verdict_ae0c50256218363f2.md`

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F106_erm_mag_gap_1m` 看服务器上的 tag,`./scripts/study.sh digest F106_erm_mag_gap_1m <tag>` 重看结果)。

## 研究现状(`notes/F106_erm_mag_gap_1m/state.md`,10-05 15:12 更新)—— **先读这个文件**

# F106_erm_mag_gap_1m — 研究现状(主研第 6 轮覆盖重写,2026-10-05:批量扫描 s2 对账与定论)

> 每轮覆盖重写,只放结论与指针。**本轮全文在 `synthesis.md` 末节「## 第二轮(s2)对账与结论」(每条论断带变体 id 和数字);第三批假设在 `studies/F106_erm_mag_gap_1m/hypo3.yaml`(25 条,已过 `study.sh hypo3` 25/25)。** s1 的综合在 `synthesis.md` 前半,更早的细表在 `07_S_final.md` / `07x_1` / `07x_2` / `05_hypotheses.md`,判断在 `09`~`12`。
> 本轮**只用 train 2018–2021 / valid 2022–202308**,没有打开 `runs/.../sweepfinal_s2.json`(测试段);服务器运行 0 次。

## 1. 现状

**结论类型 = 分辨,第二轮扫描把它钉死了。** 原式多头腿 train/valid/utrain 三段全负(−6.9% / −3.2% / −5.8%,Lshp −2.15 / −1.23 / −1.91),相对已知成交额族无增量 —— 这些 s1 已有。**s2 新增的决定性一条:把段间搬钱拿掉之后,它在任何桶内都没有选股力**(`h_bk_X_frozen` −5.5 / −3.4、`h_bk_liq_sm5` −5.8 / −7.7),所以 s1 那个「6.5% 冻结段段内 +18.2%」**不是可迁移的段内 alpha**,是「在一个等权 −67.4%/年的段里少亏一点」。它**也不能当筛子、不能当 overlay**:含 X 的最好用法 `ov_p025` +9.8 / +19.4,比 `k_known`(+12.6 / +22.3)差 2.8~2.9pp,比 `k_known_xfrozen`(+16.4 / +23.2)差 6.6pp。

**唯一值得继承的不是这条因子,是它指出的筛子口径。** `k_known_xfrozen` = `cs_last_high20(neg(k_known), cross_max(day_zero_ratio(Ret),15))`(硬剔近 15 日冻结最重的 20%)把基准抬到 **+16.4% / +23.2%、Lshp 2.81 / 3.98**(+3.8 / +0.9pp),**功劳记给筛子,不记给 F106**。

(…全文 6310 字符,读 `notes/F106_erm_mag_gap_1m/state.md`)

## 研究日志(`notes/F106_erm_mag_gap_1m/journal.md`:15 条,其中研究员自己写的 10 条)

最近的 5 条(更早的和全文看文件):

### 2026-10-04 23:16 [主研] 第 3 轮:R2 的 final 已跑完但结果卡被打断 → 按规矩原样交回(并在工单末尾写明禁止再跑 final);我自己读 S_final.json 裁决 C1~C6,六条全部成立,结论定稿=分辨

看到了什么:
- brief 显示留出段已读(10-04 15:35),但 notes/.../results/R2.md 和 07_S_final.md 都不存在 → 上一个执行跑完 final 之后被额度打断了两次。
  磁盘事实:runs/F106_erm_mag_gap_1m/S_final.json 存在(135 KB、seconds 310、errors 空、5 个变体全部求值成功);
  ledger.json 的 summary 里 holdout {reads: 1, expressions: 5} → 那唯一一次读取已经用掉了。
- 按工作流第 2 条(最新工单没有结果卡 → 不另开工单,原样交回),本轮返回 {status: order, order: R2, kind: final}。

这一轮我做的三件事:
1. **给 R2 补了一节「补充(主研第 3 轮)」**,这是本轮最要紧的动作:工单正文第 0~3 步写的是「怎么跑 final」,已经过时;
   如果换上来的执行照着做,就会第二次读留出段 —— 这项研究唯一不可挽回的错误。补充里写明:本轮服务器运行 = 0 次,
   跳过 check/final/run,直接 digest + 写两份文件;并逐项给了 JSON 路径与字段映射(books 是 train 拟合只报 train/valid,
   books_user 是 utrain 拟合、报 utrain/holdout → holdout 一律读后者),以及三件要照实写明的事:
   (a) 用的是主版不是兜底版(f_known30r 与 f_known30 的书逐项相同、rank 相关 1.000 → cs_rank 语义与预期一致);
   (b) holdout 的分位剖面「缺」(profile 只有 train/valid,f_known30r / f_excl_lu15 的 profile 是空的),不要重跑;
   (c) C3/C4 的读法必须降级并写明降级(见下)。
2. **自己读 S_final.json,按事前登记的判据裁决 C1~C6:六条全部成立,一条都没被否定。**
   f_orig holdout(用户口径,hl 在 utrain 上拟合
…(这条日志还有后文,读 journal.md)

### 2026-10-04 23:34 [执行] R2:留出段已读(本轮服务器运行0次,只digest+读JSON),S_final五条候选的数字已带回,结果卡与07_S_final.md写完

本轮没有调用 check/final/run/exec,只重看已跑完的 S_final(exit 0,10-04 15:35)+ 直接读 JSON 核对字段;ledger.summary.holdout={reads:1,expressions:5} 确认留出段没有被第二次读取。

C1/C2(f_orig holdout,books_user 用户口径,hlL=hlS=20):Lnet −3.19%、Lshp −0.69、Lgross −1.38%、LS +3.11 —— 与用户表 test 列(LS 3.11 / Lgross −1.4%)精确复现。
C5(f_known30 holdout):Lnet +14.10%、Lshp +1.51,落在用户给的 +13~15%/1.4~1.9 区间内。
C3/C4(排除性增量 ΔLnet,holdout,引擎各自拟合半衰期下的上界):f_excl_blown15−f_known30r = +0.54pp(hl1对hl0);f_excl_lu15−f_known30r = +0.75pp(hl1对hl0)。train/valid 口径下 C3 恰好是同hl的干净对照(+1.63pp / +0.57pp),C4 始终是不同hl的上界(+2.56pp / +1.22pp)。
C6:5个变体 cov(ic_holdout.coverage)全部 0.9675,dist 全部 ≥0.9933 —— 全过门槛。

核实的三件事:(1) 主版非兜底 —— 两条叠加候选 expr 字段核对都是 cs_rank 版;f_known30 与 f_known30r 在 hl0 下书逐项相同、rank相关(train)=1.000。(2) holdout 分位剖面缺(profile 字段只有 train/valid;f_known30r/f_excl_lu15 连 profile 字段都不存在)。(3) holdout 固定半衰期表缺(sweep 只在各自拟合段算),C3/C4 已按降级读法处理并在表里标出是否同一半衰期。

异常/值得注意:无求值失败、无 NaN;5 个变体 sign/sign_user 全部 −1;cov 这个数在 train(0.691)/valid(0.895)/utrain(0.749)/holdout(0.967)差
…(这条日志还有后文,读 journal.md)

### 2026-10-05 00:02 [主研] 第 4 轮:R2 结果卡已到 → 留出段已读 ⇒ 本轮必须是 (c) 成文;写完 08/09/10后半节/11/12 + 05 留出段确认表,下工单 R3(kind: writeup,服务器运行 0 次);并订正了「上界」这个措辞

(工作流给我的轮次计数是「第 2 轮」,但磁盘上这是第 4 个主研轮次 —— state.md 和日志一律按磁盘的数走,免得接手的人对不上。)

看到了什么:
- brief 显示 R2 的结果卡已经写好(10-04 23:34,执行本轮服务器运行 0 次,只 digest + 读 JSON)。
  `ledger.summary.holdout = {reads: 1, expressions: 5}` 仍然是 1 —— 留出段没有被第二次读取。
  → 工作流第 2 条(最新工单没有结果卡就原样交回)不再适用;规矩里「留出段已读的,这一轮必须是 (c)」生效。
- 结果卡和 07_S_final.md 的数字我自己对着 07_S_final.md 的 §2b/§3/§4/§7/§8 核过,与第 3 轮我直接读 JSON 得到的 C1~C6 裁决一致,没有出入。

判断(这一轮唯一的新判断,其余都是把已有结论落成文字):
- **上一轮把 holdout 的 ΔLnet +0.54 pp 叫做「上界」,这个措辞不准,我订正了。** 理由:
  叠加候选在留出段拟合到 hl 1、基准拟合到 hl 0,所以差值里混了半衰期错配。错配有多大,可以用**有网格的 utrain** 去量
  (只借 hl 敏感性,不是把 utrain 的数当成 holdout 的数 —— 那正是「张冠李戴」):
  own-hl Δ = 16.71 − 15.40 = +1.31 pp;同 hl0 Δ = 16.73 − 15.40 = +1.33 pp;同 hl1 Δ = 16.71 − 15.00 = +1.71 pp。
  → 错配量级 ≲0.4 pp,而且 own-hl 读数比干净的 hl0 对照**还低 0.02 pp** —— 偏差方向不定,不是单方向的上界。
  这个订正让结论更稳(不再需要「只是上界」这个让步),而且两个方向都远低于 +1.5 pp 门槛与 ±3 pp 噪声 → **C3 的裁决不变、推荐不变**。
  写在 09_diagnosis.md B1,10_distilled.md 的降级说明里也指过去;R3 工单让执行在报告里按 B1 写,并把 07_S_final.md §
…(这条日志还有后文,读 journal.md)

### 2026-10-05 11:09 [主研] 批量扫描 s1 的综合

152 个变体 + 23 段 × 14 时段的解剖读完,结论不变(分辨:多头腿不可用、相对成交额族无增量),但大表给了四条前几轮没有的硬事实:
1. 承重的是「分位数当分母 + 1e-6」一个节点:abl_G(A+1e-6 → A+A,结构不动只抹平塌缩)把公布的多空夏普 +2.82 变成 +0.06、ρo 变成 −0.26;abl_J/abl_V 把 LS 变成 −1.59/−1.14;abl_R 全 NaN。计数侧的同一个 1e-6 是装饰(abl_H ρo +0.98)。半衰期网格 hl0 [−67.2%, −19.51, −25.67] → hl20 [−6.9%, −2.15, +2.82] 说明 LS 全是线性 EMA 拖出来的,不是任何一天的信号(基准 k_known 的网格单调相反)。
2. abs_ 可证明是装饰:sub_U_neg / sub_N_neg 与 v_base 逐位相同(ρo +1.00);abl_N ≡ sub_X_add 逐行相同,两腿是严格镜像。计数可以整个删掉(only_H_R / sub_F_day_* ut +1.5%、valid +10.8%,全表非 overlay 最好)。
3. 解剖:23 个段里 22 个段内为负,唯一正数是 6.5% 的冻结盘口段(段内 +18.2%,该段自身等权 −67.4%/年,书还超配 +4.6pp);干净段 93.5% 段内 −6.9%。市值/成交额/价格五档全负 → 不是规模或流动性因子。科创板 −23.6% 最差。六年全负。
4. 新增对基准的理解:k_known 的多头腿是段间倾斜而非段内选股 —— 它在成交额五档段内是 −4.1/−5.3/−8.2/−5.2/+2.5,靠超配最低成交额档 +80.3pp 拿到 +15.4%。abl_M(ut +3.4%、六年全正、ρk 只 +0.06)在成交额五档段内五档全负,靠超配最低档 +26.2pp —— 同一个机制的更弱版本,低 ρk 不等于有增量。
下一步:第二批 37 条假设已写进 studies/F106_erm_mag_gap_1m/hypo.yaml(全部通过 hypo 检查),六个方向见 synthesis.md §5;另报四个工具问题(最要紧的是 dist 门槛算在 EMA 之前,机械判死计数/占比类面板,上一轮的 H11 就死在这里)。

### 2026-10-05 15:12 [主研] 批量扫描 s2 对账与结论

200 个变体 + 新解剖读完,只用 train / valid(没打开 sweepfinal_s2.json)。上一轮六条推论四条被否定,最重要的一条是 s1 的「冻结段段内 +18.2%」:按冻结状态或成交额分桶后,X 在任何桶内都没有选股力(h_bk_X_frozen −5.5 / −3.4,h_bk_liq_sm5 −5.8 / −7.7),所以那 +18.2% 只是「在一个等权 −67.4%/年的段里少亏一点」,不是可迁移的段内 alpha。
R3 被否定且更糟:常规区间不是空的而是反的(h_regular_gate 只留非塌缩日 −12.4 / −10.2、TO 11.0%、LS −1.52),互补的 h_blown_gate LS +0.67 —— 多空夏普确实住在塌缩日。R4 多头腿支持、多空否定:去掉 eps 后 LS 只从 +2.82 掉到 +1.5~+2.6,掉的是换手(2.4% → 10~11%)。R1 部分否定:有界版只拿到底腿一半,而且带符号 ≫ 不带符号(h_pin_dir30 +1.8 / +7.6、ρk 0.00 vs h_zero_m30 −4.8 / +8.4、空头腿 −1.4%,涨停与跌停相加互相抵消)。R2 否定,R5 未检验。
定论 = 分辨,比 s1 更硬:best_own 三条(abl_M +3.1 / +4.3、h_pin_dir30 +1.8 / +7.6、h_centroid_ret30 −0.9 / +11.1)全在 ±3pp 噪声内;best_on_known 没有可用用法 —— 含 X 的最好是 ov_p025 +9.8 / +19.4,差于 k_known 2.8pp、差于 k_known_xfrozen 6.6pp,当筛子两个方向都输。多头腿不可用、不能当筛子、不能当 overlay、分桶中性后段内为负。
本轮最有价值的副产品不属于 F106:同一个量硬筛赢软叠加 —— cross_max(day_zero_ratio(Ret),15) 硬剔 20% 把基准抬到 +16.4% / +23.2%(k_known_xfrozen),同一个量做 −0.25 overlay 只有 +9.3% / +21.2%(基准以下 3.3pp),做 rank 相减 valid 掉 13.2pp。要给融合层贡献,贡献的是这个硬筛口径,功劳记给筛子不记给 F106。
第三批 25 条写进 studies/F106_erm_mag_gap_1m
…(这条日志还有后文,读 journal.md)

## 工单与结果卡(`notes/F106_erm_mag_gap_1m/orders/`、`notes/F106_erm_mag_gap_1m/results/`)

- R1:工单 有,结果卡 有
- R2:工单 有,结果卡 有
- R3:工单 有,结果卡 **还没有(待执行)**

## 配置里的实验计划(`configs/F106_erm_mag_gap_1m.yaml`)

- 标题:分钟收益右尾 ES/VaR 减左尾 ES/VaR;分母 +1e-6 在「上涨(下跌)分钟不足 5%」的日子塌掉,截面两端由这些日子决定
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base
- **S1_regime**(10 个变体):公布的多空夏普(和空头腿)是「塌缩日 = 封板事件」做出来的,还是「尾部形状不对称」做出来的?差的符号有没有信息?
  a_right、a_left、a_sum、a_abs、a_regular、a_eps3、a_flag、a_rankfirst、a_lockshare、a_limitup
- **S_final**(5 个变体):读留出段之前写死的结论(原式多头腿全负 / 排除性增量在噪声以下 / 和已知家族相加更差)在用户的测试段(20230808–20251231)上成不成立?
  f_orig、f_known30、f_known30r、f_excl_blown15、f_excl_lu15

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F106_erm_mag_gap_1m`)

- `S0_baseline`  10-04 11:50  1 个变体  → `./scripts/study.sh digest F106_erm_mag_gap_1m S0_baseline`
- `S_final`  10-04 15:35  5 个变体  → `./scripts/study.sh digest F106_erm_mag_gap_1m S_final`
- `sweep_s1`  10-05 10:35  155 个变体  → `./scripts/study.sh digest F106_erm_mag_gap_1m sweep_s1`
- `anatomy_s1`  10-05 10:45  0 个变体  → `./scripts/study.sh digest F106_erm_mag_gap_1m anatomy_s1`
- `sweep_s2`  10-05 11:51  203 个变体  → `./scripts/study.sh digest F106_erm_mag_gap_1m sweep_s2`
- `anatomy_s2`  10-05 12:12  0 个变体  → `./scripts/study.sh digest F106_erm_mag_gap_1m anatomy_s2`
- `sweepfinal_s2`  10-05 12:17  8 个变体  → `./scripts/study.sh digest F106_erm_mag_gap_1m sweepfinal_s2`
- `sweep_s3`  10-05 17:42  228 个变体  → `./scripts/study.sh digest F106_erm_mag_gap_1m sweep_s3`
- `anatomy_s3`  10-05 17:50  0 个变体  → `./scripts/study.sh digest F106_erm_mag_gap_1m anatomy_s3`
- `sweepfinal_s3`  10-05 18:03  8 个变体  → `./scripts/study.sh digest F106_erm_mag_gap_1m sweepfinal_s3`
- `x1`(自写脚本的输出)  10-04 12:30  exit 0  → `logs/F106_erm_mag_gap_1m_x1.log`
- `x2`(自写脚本的输出)  10-04 13:54  exit 0  → `logs/F106_erm_mag_gap_1m_x2.log`

## 已写的 notes(`notes/F106_erm_mag_gap_1m/`)

`01_expression.md`(2K)、`02_operators.md`(2K)、`03_decomposition.md`(3K)、`04_grammar.md`(1K)、`05_hypotheses.md`(21K)、`06_baseline.md`(3K)、`07_S0_baseline.md`(3K)、`07_S_final.md`(13K)、`07x_1_anatomy.md`(10K)、`07x_2_longonly.md`(23K)、`08_variants.md`(5K)、`09_diagnosis.md`(10K)、`10_distilled.md`(13K)、`11_risks.md`(6K)、`12_next.md`(4K)、`journal.md`(31K)、`state.md`(9K)、`synthesis.md`(21K)

## 自写的探针与分析脚本(`studies/F106_erm_mag_gap_1m/`)

- `probes.py`  10-04 12:13  Probes this tree needs:  ES/VaR of the right tail of minute returns  minus  ES/VaR of the left tail.
- `x1_anatomy.py`  10-04 12:19  x1 -- what the ES/VaR gap tree reads on REAL data, and who sits at the ends of the traded signal.
- `x2_longonly.py`  10-04 13:02  x2 -- for a LONG-ONLY user: does this factor add anything to the known amount-level family?

## 结构化结果(`handoff/F106_erm_mag_gap_1m/results/`)

- `synthesis.json`
- `verdict.json`

报告:`research/alpha_distillation/F106_erm_mag_gap_1m.md`(10-05 00:18 生成)
