# F105_std_fangzheng_covamt — 交接状态

_自动生成于 2026-10-04 12:50(`python scripts/recorder.py --brief F105_std_fangzheng_covamt` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #25(批次 B01_single_factors)
- 表达式:`ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5)`

## 现在到哪一步

- **阶段:全部完成**
- **留出段已经读过 1 次**(10-03 23:11)—— **不许再读**。候选在留出段上的数全在 `runs/F105_std_fangzheng_covamt/final.json`(`./scripts/study.sh digest F105_std_fangzheng_covamt final`)。
- agent `study:F105_std_fangzheng_covamt`(wf_759ef2d3-03f):中断,最后动作 10-03 20:47 → `handoff/F105_std_fangzheng_covamt/agents/study_a3b8cc84648ef1c22.md`
- agent `study:F105_std_fangzheng_covamt`(wf_759ef2d3-03f):中断,几乎没做事(不用看)
- agent `study:F105_std_fangzheng_covamt`(wf_759ef2d3-03f):中断,几乎没做事(不用看)
- agent `study:F105_std_fangzheng_covamt`(wf_759ef2d3-03f):已返回结果,最后动作 10-03 23:21 → `handoff/F105_std_fangzheng_covamt/agents/study_a77f2d6ff5f146117.md`
- agent `audit-numbers:F105_std_fangzheng_covamt`(wf_759ef2d3-03f):已返回结果,最后动作 10-03 23:33 → `handoff/F105_std_fangzheng_covamt/agents/audit-numbers_ace2cc0e601104fb8.md`
- agent `audit-mechanism:F105_std_fangzheng_covamt`(wf_759ef2d3-03f):已返回结果,最后动作 10-03 23:34 → `handoff/F105_std_fangzheng_covamt/agents/audit-mechanism_a634d8b8d73e7330b.md`
- agent `revise:F105_std_fangzheng_covamt`(wf_759ef2d3-03f):已返回结果,最后动作 10-04 00:19 → `handoff/F105_std_fangzheng_covamt/agents/revise_a05e6538df5a93b1b.md`

**接手的人该做什么:** 这条因子做完了。最终结论在 `handoff/F105_std_fangzheng_covamt/results/` 里最新的那个(revised.json 优先,否则 study.json)。

## 研究员自己写的现状(`notes/F105_std_fangzheng_covamt/state.md`)

(**没有**。上一个研究员没有留下现状说明 —— 假设、逻辑和后面的思路只能从 notes、研究日志和动作流水里重建。)

## 研究日志(`notes/F105_std_fangzheng_covamt/journal.md`:0 条,其中研究员自己写的 0 条)

(还没有。之前的研究员没有记日志 —— 它的想法只能从 notes 和动作流水里推。)

## 配置里的实验计划(`configs/F105_std_fangzheng_covamt.yaml`)

- 标题:分钟成交额方差的一年期 mean+std 水平在最近 5 天的变化量 —— 带成交额平方尺度的「放量事件进入/滑出一年窗口」探测器
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base
- **S1_what**(3 个变体):原式的预测力在哪一样东西里:成交额尺度(水平)、还是事件的方向?它和已知家族 cross_max(day_std(Amt),9) 比怎么样?
  s1_level、s1_signed、s1_known_stdamt9
- **S1b_events**(3 个变体):把成交额尺度除掉之后,「事件」这一半自己还剩多少?硬窗口的周年回声、一年窗口本身,是在挣钱还是在稀释?
  s1_relchg、s1_noecho、s1_recent
- **S2_nodes**(10 个变体):树里哪些节点是多余的:3 日极值、fangzheng 的 mean 项 / std 项、日内方差这个字段、241 和 5 这两个窗口?把外层 std 换成 |5 日差分| 能不能去掉上市首日的伪影?
  s2_dtface_check、s2_no_max3、s2_mid_std、s2_mid_mean、s2_min3、s2_field_std、s2_field_sum、s2_w60、s2_out20、s2_absdelta
- **S3_family**(6 个变体):原式的水平部分 C 近似一年最大值(07x:scale-free rank 相关 0.984),已知家族是 9 日最大值:cross_max(day_std(Amt), d) 这一族里,多头腿净超额在哪个 d 上最好?长窗口下 max 还比 mean 好吗?
  s3_max241、s3_max20、s3_max60、s3_max120、s3_mean60、s3_mean241
- **S4_longleg**(6 个变体):已知家族 cross_max(day_std(Amt), d) 的多头腿在 d=20~60 上是稳定的平台,还是两个点的运气?多头腿要的是「没爆过量」(极值)还是「平时成交少」(中位数/均值)?原式的「事件」那一半写干净之后有没有多头腿?
  s4_max15、s4_max30、s4_mean20、s4_med60、s4_summax30、s4_pos
- **S_final**(5 个变体):只凭 train/valid 选出来的结论 ——「原式 = 已知家族的一个更吵的写法;换成 cross_max(day_std(Amt), 30) 多头腿更好」—— 在用户的测试段(20230808–20251231)上站不站得住?
  f_orig、f_min3、f_max15、f_max30、f_max60

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F105_std_fangzheng_covamt`)

- `S0_baseline`  10-03 17:43  1 个变体  → `./scripts/study.sh digest F105_std_fangzheng_covamt S0_baseline`
- `S1_what`  10-03 19:37  6 个变体  → `./scripts/study.sh digest F105_std_fangzheng_covamt S1_what`
- `S1b_S2_S3`  10-03 20:12  21 个变体  → `./scripts/study.sh digest F105_std_fangzheng_covamt S1b_S2_S3`
- `S2S3_nodes_family`  10-03 22:45  19 个变体  → `./scripts/study.sh digest F105_std_fangzheng_covamt S2S3_nodes_family`
- `S4_longleg`  10-03 22:57  6 个变体  → `./scripts/study.sh digest F105_std_fangzheng_covamt S4_longleg`
- `final`  10-03 23:11  5 个变体  → `./scripts/study.sh digest F105_std_fangzheng_covamt final`
- `x1_events`(自写脚本的输出)  10-03 19:28  exit 0  → `logs/F105_std_fangzheng_covamt_x1_events.log`
- `x2_longleg`(自写脚本的输出)  10-03 23:05  exit 0  → `logs/F105_std_fangzheng_covamt_x2_longleg.log`
- `audit1`(自写脚本的输出)  10-03 23:29  exit 0  → `logs/F105_std_fangzheng_covamt_audit1.log`
- `rev1`(自写脚本的输出)  10-03 23:51  exit 0  → `logs/F105_std_fangzheng_covamt_rev1.log`
- `rev2`(自写脚本的输出)  10-03 23:59  exit 97  → `logs/F105_std_fangzheng_covamt_rev2.log`

## 已写的 notes(`notes/F105_std_fangzheng_covamt/`)

- `01_expression.md`  796 字节  10-03 23:17
- `02_operators.md`  1856 字节  10-03 18:40
- `03_decomposition.md`  1821 字节  10-03 18:40
- `04_grammar.md`  1652 字节  10-03 18:40
- `05_hypotheses.md`  5573 字节  10-03 23:17
- `06_baseline.md`  3246 字节  10-03 18:43
- `07_S1_what.md`  4281 字节  10-04 00:07
- `07_S1b_events.md`  6424 字节  10-04 00:14
- `07_S2_nodes.md`  4212 字节  10-03 22:50
- `07_S3_family.md`  4733 字节  10-04 00:08
- `07_S4_longleg.md`  6536 字节  10-04 00:14
- `07_S_final.md`  6215 字节  10-04 00:15
- `07_conditional.md`  3793 字节  10-04 00:09
- `07_controls.md`  1068 字节  10-03 23:09
- `07_neutralise.md`  3047 字节  10-03 23:09
- `07x_events.md`  8400 字节  10-04 00:15
- `07x_longleg.md`  5989 字节  10-04 00:09
- `07x_review_audit.md`  8841 字节  10-04 00:03
- `07x_revision.md`  20173 字节  10-04 00:06
- `08_variants.md`  3371 字节  10-04 00:09
- `09_diagnosis.md`  11941 字节  10-04 00:11
- `10_distilled.md`  13630 字节  10-04 12:04
- `11_risks.md`  4522 字节  10-04 00:13
- `12_next.md`  2974 字节  10-04 00:13

## 自写的探针与分析脚本(`studies/F105_std_fangzheng_covamt/`)

- `audit_1.py`  10-03 23:27  F105 audit (reviewer, mechanism / overfitting lens).  train / valid only -- never the holdout.
- `events.py`  10-03 18:42  F105: what orders the root, and which kind of stock-day earns the money.
- `longleg.py`  10-03 23:00  F105: why the slow members of the known family have a better long leg than the original,
- `probes.py`  10-03 18:37  Probes this tree needs: ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5).
- `rev1.py`  10-03 23:42  F105 revision 1 -- the researcher's follow-up to the two reviews.  train / valid only: every panel is cut at
- `rev2.py`  10-03 23:57  F105 revision 2 -- is the "entry event" result manufactured by the label's buyable filter?

## 结构化结果(`handoff/F105_std_fangzheng_covamt/results/`)

- `audit-mechanism.json`
- `audit-numbers.json`
- `revised.json`
- `study.json`

报告:`research/alpha_distillation/F105_std_fangzheng_covamt.md`(10-04 12:08 生成)
