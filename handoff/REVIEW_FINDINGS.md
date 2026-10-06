# 对抗式审查的结果与处置(工作流 `wf_b7c13476-92d`,2026-10-05 夜)

6 位审查者 + 9 组算子对拍 + 复核,共 93 个 agent。**成立 24 条**(13 条 high 全部被复现)、推翻 31 条、低优先未复核 4 条。
原始返回值:`handoff/workflows/wf_b7c13476-92d/`(`FINAL_RESULT.json` 是汇总)。回归测试:`tests/test_ops_ext.py`、`tests/test_steer.py`。

| # | 严重 | 复现 | 位置 | 缺陷 | 处置(2026-10-06) |
|---|---|---|---|---|---|
| 0 | high | 是 | `partura/steer.py` | long_marginal: the blend and the pool it is subtracted from still live in different universes (the candidate's own NaNs are not aligned) | 已修:边际奖励改成「混合书 − 池子书」在同一批格子上的成对逐日差(partura/steer.py reward;tests/test_steer.py) |
| 1 | high | 是 | `guidance/B01.yaml` | C4_root_winsor rewrites away a cs_winsor that is not rank-neutral, and the two spellings share a dedup_key | 已修:C4 从「改写」降为不加权的备注;IDEMPOTENT_OPS 只留 abs_ / cs_demean / cs_rank |
| 2 | high | 是 | `partura/steer.py` | operator_weights() silently drops the `root:` anchor, so root-only bans become global operator bans in the steer arm | 已修:operator_weights 跳过带 root: 的规则 |
| 3 | high | 是 | `partura/steer.py` | dedup_key collapses every price leaf globally, merging expressions that are not the same experiment | 已修:dedup_key 只做精确等价;新增 family_key(价格叶子按首次出现重标号)+ C7 改成「兄弟少采样」 |
| 4 | high | 是 | `scripts/idea_search.py` | p_rho_known 用原始面板、rho_pool 用 EMA 平滑后信号,却共用 0.5 阈值;NaN 还会直接放行 | 已修:独立性检验改在实际交易的信号上算(rho_known_traded),量不出来的不放行 |
| 5 | high | 是 | `research/alpha_distillation/B01_reverse_guidance.md` | headline 5 与 ban B4 的「+1e-6 删掉后 7 例全部变好」:真正删到 1e-6 的只有 4 例,其中 3 例判废,可用观测只有 1 条 | 已修:报告里那句话删除并写了更正;B4 由封禁降为降权(D0);motif_stats 把 create_like 的「消融」剔出、报两个分母 |
| 6 | high | 是 | `partura/ops_ext.py` | _pct_rank 用序数秩打并列,_lexi 的筛子/分段在并列块内部按股票列序任意切,占 20% 里的 12.9pp 是老票 | 已修:_lexi 的带只收整块并列(partura/ops_ext.py _rank_block);受影响的面板缓存已清,第四轮重跑 |
| 7 | high | 是 | `scripts/sweep.py` | sweep.py 的符号锁只认根节点,包一层 mul/cs_rank 的筛子假设会被按 IC 选成 sign=-1,变成「只买被标出的票」 | 已修(换了做法):变体的方向改按训练段纯多头书定(原式与基准仍按 rank IC),包了一层的筛子不再被翻面 |
| 8 | high | 是 | `partura/ops_ext.py` | cross_zscore's fixed EPS=1e-9 denominator floor is swamped by float32 rounding noise at amount-scale magnitudes, producing spurious +-1 output instead of the mathematically-required 0 | 已修:cross_zscore 对逐位不变的窗口返回 0 |
| 9 | high | 是 | `partura/ops_ext.py` | in_madz: torch.nanmedian's even-count "lower of the two" rule silently breaks the documented median/MAD whenever window d is even | 不改内核(全库的中位数都是 torch.nanmedian 的「取较小者」约定),docstring 已写明 |
| 10 | high | 是 | `partura/ops_ext.py` | cs_flip_by_state invents a signed value when the market state is undefined (g all-NaN that day) | 已修:状态没有定义的日子整行 NaN |
| 11 | high | 是 | `partura/ops_ext.py` | day_es_ratio_hi spuriously admits the tied boundary point at the real M=241 width under float32 | 已修:_es_ratio 在 float64 里算 |
| 12 | high | 是 | `partura/ops_ext.py` | in_zscore_expand's two-pass variance formula catastrophically cancels for amount-scale inputs | 已修:in_zscore_expand 改成平移后的累计矩(float64) |
| 13 | medium | 是 | `partura/steer.py` | long_screen's z > 0.3 is not 'the candidate's top two tenths' on a saturating panel, and one direction can screen nobody and score exactly 0.000 | 已修:筛子按整块并列取最高两成;不改变参照书的方向按 0 计,整条候选不改变参照书则判「无作用」;返回 screened_share |
| 14 | medium | 是 | `scripts/idea_search.py` | steer 臂的 guidance 并非施加在每一棵被提议的树上:mutate_window / mutate_constant 不调 acceptable,generate 重试用尽的回退也不过筛 | 已修(临时):steer 臂把 mutate_window / mutate_constant 也过一遍接受检查;正式修在 AlphaCube 的 WP5 |
| 15 | medium | 是 | `scripts/idea_search.py` | operator_weights() 丢掉 root 作用域,steer 臂的词表被根部禁令全局删掉 5 个算子,control 臂留着 | 同 2 |
| 16 | medium | 是 | `scripts/idea_search.py` | run_mining 的异常被吞掉,崩掉的臂在 evidence.json 里写成合法的零;旧 checkpoint 不清理,files[-1] 可能读到上一次运行 | 已修:崩掉的臂把错误写进 evidence;每臂开跑前清掉旧 checkpoint |
| 17 | medium | 是 | `scripts/motif_stats.py` | 替换统计静默丢掉 69 条 nosc_*(齐次度 0 的无尺度替换),而表题写的是「不论换成谁」;补回后 day_sum → 等多行明显变弱 | 已修:替换统计的正则放宽,落空行数打印出来(s3 上为 0) |
| 18 | medium | 是 | `scripts/batch2_summary.py` | 两份已交付的 B01 报告对同两个候选给出相反结论(「可以和已知族并列持有」vs「只能选一个用,不能叠加」) | 待修:已知族的判定要逐候选算(batch_cluster / batch_fuse),两份报告用同一个判据 |
| 19 | medium | 是 | `partura/ops_ext.py` | day_flat_run_max crashes instead of returning NaN on a day with fewer than 2 minutes | 已修:day_flat_run_max 垫一列零 |
| 20 | medium | 否 | `partura/ops_ext.py` | day_at_max_ratio returns NaN instead of the docstring-implied 1.0 for a single-finite-minute day | 不改行为(少于两个有效分钟返回 NaN),docstring 已写明 |
| 21 | medium | 否 | `partura/ops_ext.py` | day_at_min_ratio returns NaN instead of the docstring-implied 1.0 for a single-finite-minute day | 同上 |
| 22 | medium | 否 | `partura/ops_ext.py` | day_distinct_ratio returns NaN instead of the docstring-implied 1.0 for a single-finite-minute day | 同上 |
| 23 | low | 否 | `partura/ops_ext.py` | cs_flip_by_state's docstring doesn't say how a tie at the median resolves (implementation always resolves it to HIGH) | docstring 已写明(严格高于中位才算 HIGH) |

## 低优先、未复核(记下,未处理)

- `reward-math`:The untradable mask is applied to the raw panel BEFORE the EMA, so it changes the signal's value and not just the universe
- `reward-math`:An unrecognised reward kind silently runs the unmasked `long` reward and records the wrong name
- `pipeline-holdout`:sweep.py 打印的 hlL 是 train 定的半衰期,但表格排序用的 ut 夏普和 dist 门槛都是 utrain 定的半衰期,两者有 782 个变体不一致
- `pipeline-holdout`:逐年表每年重开一本空书,每一年都被多扣一次完整建仓费(实测 −0.145 个点/年),与同一张表里的两段数字口径不一致

## 被推翻的(审查者报了,复核者没能复现或判定不影响结论)

- `reward-math`:fit = 0.03 x score is signed and centred on zero, and AlphaCube's cluster cull uses a cutoff relative to |best|
- `reward-math`:long_screen is baselined against the UNSCREENED known family while the already-screened version is in the pool list, and the pool de-duplication is skipped for this reward
- `matcher-guidance`:B3_day_scalar_multiplier is an unconditional ban, but its no-op argument only holds when the day-scalar multiply is the last op before the cross-sectional rank
- `matcher-guidance`:B4_abs_epsilon_denominator bans any additive constant denominator, anywhere in the tree, and kills the only F109 variants that beat the known family
- `matcher-guidance`:nesting() counts non-adjacent occurrences and dies on alternation heads, so depth_ge rules fire on structures their `why` does not describe
- `gp-hooks`:steer 与 control 在同一 --budget 下实际「付费评估」数差 38%,两个汇报指标朝相反方向偏
- `gp-hooks`:MUST 只取 grammar.day_ops:B01 五个想法里三个根本没有邻域约束,带括号的 day_ops 会让整条 steer 臂退化成 day_*(Field)
- `motif-stats`:s2 的筛子/分段变体方向仍被 rank IC 重拟合:3.1 证据表两行在 s3 整体翻号(+1.01 → −3.18、+0.41 → −4.47)
- `motif-stats`:结论 1 的 +1.18 主要是「底座本来就没用」造成的回归效应,底座夏普 ≥ 1 的因子上只剩 +0.41 中位 / +0.09 均值
- `motif-stats`:「删掉一个节点」实际是把该节点除第一个操作数以外的子树全删:47/97 条消融改动多于一个节点,D7「删掉除法 73% 变好」测的是「删掉整个分母」
- `motif-stats`:叶子正则停在第一个左括号,把 4 种不同替换并成一个 Ret → in_pct 桶;拆开后流向类 +0.22 与价格类 −0.29 符号相反,而 D9 降权只覆盖正的那一半
- `pipeline-holdout`:sweep.py 的 sign 锁把手写筛子假设整条镜像反过来,+2.6 夏普的候选被报成 -2.8 并从规则候选里消失
- `pipeline-holdout`:batch_fuse 记在留出段台账上的 12 条,实际做了 ~130 次留出段读数,report 又引用这个台账说「测试段只读了这一次」
- `pipeline-holdout`:融合 U(「升级版 15 条等权」)的 15 个成员里有 9 个落在 3 个簇里,ρ 0.991 的同一条信号被当两条等权计入
- `screen-ops-universe`:cross_age 把数据起点就存在的全部股票压成同一个值(10000+t),docstring 却说它「不饱和」
- `screen-ops-universe`:idea_search 的 untradable:冻结筛子是固定 20% 名额 + 平均秩,风平浪静的日子照剔两成,并列块大时按天在 0% 与整块之间跳
- `screen-ops-universe`:day_zero_ratio / day_flat_ratio / day_flat_run_max 没有最少有效分钟数门槛,一天只有一笔成交的票读成「全市场最不冻结」
- `screen-ops-universe`:untradable 的「次新」门槛用 trimmed view 的天数算可用历史,忽略了 60 天 warm-up,视图开头上市的票永远不会被标为次新
- `ops2:cs_bucket_rank..`:cs_bucket_rank's docstring omits its own tie-break term and misstates the output's range
- `ops3:cross_tail_mean_q75..`:cross_tail_mean_q75's docstring never names its quantile convention
- `ops3:cross_tail_mean_q75..`:cs_first_low40/high40 and cs_last_high20/low20 don't document the x-bucket's tie-break or rounding
- `ops4:day_flat_run_max..`:cs_robust_z: same torch.nanmedian even-count bug, keyed off the daily finite-stock count's parity
- `ops4:day_flat_run_max..`:cs_robust_z: new_operators.md's formula silently drops the "+EPS" that both the docstring and the code carry, hiding a real MAD=0 blow-up
- `ops4:day_flat_run_max..`:cs_bucket_demean / cs_bucket_zscore: "same decile of x" is not defined in either docstring on its own
- `ops4:day_flat_run_max..`:cs_robust_z crashes on a zero-width cross-section instead of returning an empty/NaN result
- `ops5:cs_first_low20..`:cs_first_low20/high20, cs_last_high40/low40: docstrings never say which universe the x-percentile bucket split is measured over
- `ops7:day_topw_mean..`:day_topw_mean's top-10% ranking pool silently depends on y's NaN pattern, not just |w|'s
- `ops7:day_topw_mean..`:in_index's docstring formula t/(T-1) is undefined at T=1; the code silently returns 0 instead
- `ops8:cross_madz..`:cross_madz's median_d/MAD_d use torch's 'lower median' tie-break, not the textbook median its docstring describes
- `ops8:cross_madz..`:cross_madz's docstring omits cross_zscore's explicit 'today included' window convention
- `ops8:cross_madz..`:cross_semistd_pos's docstring omits the formula and NaN-threshold stated in cross_semistd_neg
