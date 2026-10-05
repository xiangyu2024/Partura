# 总领(协调者)的现状 —— B01 批次(15 条单因子)

_最后更新:2026-10-04 13:15 PDT,Opus 5.5 主会话(用户额度将尽时写的)。每到一个里程碑更新这一页。_

## 现在在跑什么

_更新:2026-10-04 23:10 PDT(第三次额度重置之后)。_

| 工作流(任务号 / run id) | 内容 | 模型 |
|---|---|---|
| `wu9usqqmj` / `wf_e3cc1b20-34b` | **F106–F115 全部 10 条**,从磁盘状态接着做(23:05 启动;chunk 10,max_rounds 6) | 主研 Opus 5,执行 Sonnet 5 |
| 后台记录器 `scripts/recorder.py --loop 150` | 写 `handoff/` | 无(普通进程;**Mac 重启后要手动再起**,见 README) |

经过:13:40 起的 `wf_48864a04-f0a` 跑了约两小时(54 个 agent、970 万 token),16:45 前后撞上用户的会话限额(所有模型共用,18:30 重置),
10 条都停在第二轮中途;期间 Mac 重启过一次(记录器和 caffeinate 都没了,23:00 已重起)。23:05 按磁盘状态重启。

**额度是硬约束**:一个限额窗口大约够 50 多个 agent。为了省,23:00 做了瘦身(脚本与 `recorder.py`):
每个 agent 不再通读 playbook(任务书里有规矩摘要);`state.md` 限 10 KB;交接页只放最近 5 条日志、不引导去读动作流水;
成文工单执行完直接进「整理结论」(少一轮主研);否定结论只做数字审查;只有出现 critical 或 ≥ 2 条 major 才修订。

**已读测试段的新结果(多头口径,多头腿净超额 训练/测试)**
- F106(读留出段的 tag 是 `S_final`):原式 −5.8% / −3.2%(多头腿不可用);事前第一推荐 = 已知族基准 +15.4% / +14.1%;
  「已知族 + 剔除近 15 日涨停票」+17.6% / +14.9%(夏普 2.55 / 1.60,对已知族 2.22 / 1.51 —— 测试段增量在噪声内)。
- F107(tag `final`):原式 +1.7% / +1.4%;事前第一推荐的提纯版 `cross_mean(abs_(cs_demean(day_skew(Low))), 20)`@hl10 +5.4% / +4.3%;
  与已知族相加 +12.8% / +8.0%,不如已知族自己;验证段看着更好的日收益替身 +7.4% / +1.2%(测试段塌了)。
- F109(tag `S_final`):原式 −3.2% / +2.9%;本因子的候选没有一条两段都站得住(+4.8/−2.3、+3.4/+2.9、+3.5/−1.2);第一推荐 = 已知族基准。
这三条都还差成文和结论(`study.json`)。

**两个坑(已处理,接手的人要知道)**
1. 工作流会把**启动那一刻用户最近的一句话**原样转给这次运行里的每个 agent,并声明它高于脚本文本。13:10 那次启动时用户最近的话是
   「快写 state.md,我马上就要没有额度了」→ F109、F110 的执行因此**放下工单去写 state.md**。现在每个 prompt 开头的
   「你在整件事里的位置」明确写了:那句话是说给总领听的、已被处理,不得因此跳过或缩减任务。**启动工作流之前,留意用户最后一句话是什么。**
2. **服务器内存被邻居占满**:13:30 起另一个会话的 GP/RL 挖掘(`gp_hit_2`、`rl_hit_2`)+ 6 个 `long_report.py` 把容器 anon 顶到 37–38 GiB;
   Partura 的内存守卫要求 < 30 GiB 才开工(实际上限约 40 GiB,超了会 OOM 连带杀掉邻居),所以任务都在排队。
   这是对的,**不要绕过守卫、不要动邻居的进程**;排队等待上限已从 45 分钟调到 3 小时(`PARTURA_MEM_WAIT_S`),超时退出码 97,执行会重跑。

3. **14:30 起服务器全部归 Partura**(用户说另一个会话的任务已停;实测 GPU 0 MiB、容器 anon 0.5 GiB、没有别的 screen)。
   并发槽从 3 调到 6(`scripts/study.sh` 里的 `PARTURA_SLOTS`);引擎求值仍然一次一个(GPU 锁),诊断可以并行。
   如果以后又有邻居任务:把槽调回 3,其余守卫逻辑不用动。

**如果一切都停了**(额度耗尽、Mac 睡眠):什么都不会丢。按 `handoff/README.md`「接着跑」一节:
`python scripts/recorder.py --state batches/B01_single_factors.yaml` → 去掉 done 的 → 起 `workflows/partura_tiered.js`。

## 仓库

GitHub 私有仓库 **https://github.com/xiangyu2024/Partura**(2026-10-04 建;分支 `main`;只有用户本人是协作者,别人要看由用户邀请)。
本机 `~/Desktop/Partura` 的 `origin`;用 HTTPS + macOS 钥匙串里的凭据推(和 AlphaCube 一样)。**每个里程碑**:
`git add -A . && git commit -m "…" && git push`(`runs/*.json`、`logs/`、`handoff/` 都在版本库里;面板缓存 `runs/_panels/`、`*.npy` 不进)。
仓库里有服务器的 SSH 地址(`scripts/study.sh`),没有任何密码或密钥。

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
