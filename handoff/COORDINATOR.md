# 总领(协调者)的现状 —— B01 批次(15 条单因子)

_最后更新:2026-10-04 13:15 PDT,Opus 5.5 主会话(用户额度将尽时写的)。每到一个里程碑更新这一页。_

## 现在在跑什么

| 工作流(任务号 / run id) | 内容 | 模型 |
|---|---|---|
| `wj5ko0nm4` / `wf_c8c98127-70d` | F111–F115:建档 → 主研/执行轮转 → 结论 → 审查 → 修订 | 主研 Opus 5,执行 Sonnet 5 |
| `wn8cwv4l7` / `wf_3cafb924-05e` | F106–F110:接着被换下的 Opus 5.5 研究员做(从 `notes/<fid>/state.md` 起) | 同上 |
| 后台记录器 `scripts/recorder.py --loop 150` | 写 `handoff/`(状态板、交接页、结构化结果、动作流水) | 无(普通进程) |

旧的 Opus 5.5 工作流(`wf_08351f46-81b`)已在 13:10 停掉:F104 的修订已完成并返回(none_robust);
F106–F110 的研究做到三四成,现状已写进各自的 `state.md`(F108 是研究员自己写的;F106/F107/F109/F110 是
`scripts/autostate.py` 从磁盘汇编的 —— 研究员没来得及写)。它们在服务器上启动的任务
(F106 `S1_regime`、F107 `S12`、F108 `x1_anatomy`、F109 `S1_S2`、F110 `x1`)会自己跑完,接手的主研/执行用 `study.sh wait` 拉回。

**如果一切都停了**(额度耗尽、Mac 睡眠):什么都不会丢。按 `handoff/README.md`「接着跑」一节:
`python scripts/recorder.py --state batches/B01_single_factors.yaml` → 去掉 done 的 → 起 `workflows/partura_tiered.js`。
不需要 resumeFromRunId。

## 已经完成的(读过留出段、有结论)

| 因子 | 结论(多头口径:多头腿净超额 训练/测试) |
|---|---|
| F101 手写 day_shine_retstd | 蒸馏:日内波动水平的 V 形截面折叠。原式@hl20 +7.1%/+7.1%;`abs_(cs_demean(day_mean(in_stddev_rolling(in_slice(Ret,2,237),5))))`@hl20 +9.5%/+7.0%;更简的 `abs_(cs_demean(day_std(in_slice(Ret,2,237))))` +9.1%/+8.0%。与成交额族无关,是真增量 |
| F102 挖掘 #3961 | 升华:`cross_max(pow_2(day_kurt(nt_ts_autocorr_s1(Ret,3))),60)`@hl2 +11.3%/+7.0%;原式@hl5 +8.9%/+2.5%(@hl1 是 +4.8%/−0.7%)。空头腿是封板事件 |
| F103 挖掘 #820 | 升华但落在已知成交额族:`mul(cross_max(day_std(Amt),9), day_durbin_watson(cross_decay_linear(Amt,30)))`@hl10 +15.6%/+14.2%;原式@hl10 +8.1%/+7.2% |
| F104 挖掘 #4190 | **none_robust**:原式多头腿 +1.8%/−2.1%,延长半衰期也没用;两位数的多头腿只来自把流动性放回来 = 已知族(`cross_mean(day_std(Amt),30)` +15.4%/+14.1%) |
| F105 挖掘 #25 | 归入已知族:`cross_max(day_std(Amt),30)`@hl1 +16.7%/+13.5%;原式@hl3 +11.8%/+8.9% |

入选式之间(训练段):F103′ 与 F105′ rank 相关 0.92,与已知族 0.87–0.95 —— 同一个因子;F101′、F102′ 与已知族 0.16–0.26,
和它五五混合后纯多头夏普 2.22 → 2.8–2.9(`runs/_batch_B01/final_overview.json`,试跑)。

## 收尾还要做的(15 条都 done 之后)

1. 写 `batches/B01_picks.yaml`(草稿 `B01_picks_draft.yaml` 只有第一组;F104 填 `kind: none_robust`,基准 `f_std30`;
   F106–F115 用各自 `handoff/<fid>/results/` 里最新结论的 `recommended_id`)。
2. 服务器:`scripts/batch_final.py batches/B01_picks.yaml`(约 10 分钟,只用训练段)→ 拉回 `runs/_batch_B01/final_overview.json`。
3. 本地:`scripts/batch_summary.py batches/B01_picks.yaml` → `research/alpha_distillation/B01_summary.md`,发给用户。
4. 各研究 `lab_findings` 合并进 `lab/findings.yaml`;commit;更新记忆。
5. F104 的报告要重出一次(`./scripts/study.sh report F104_kurt_masktop_amt`)并核对(修订者返回前是否已重出,看报告文件时间)。

## 用户定的规矩(不要改)

- 选拔口径:**多头腿净超额 / 纯多头夏普**,半衰期按纯多头书选;延长半衰期带来的净超额是有效的。
- 分工:总领 Opus 5.5;主研 Opus 5;执行(写代码、跑实验、读结果)Sonnet 5。**研究全程落盘**。
- 服务器上有别人的任务,不要相互打断;留出段每条因子只读一次。
