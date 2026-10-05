# 总领(协调者)的现状 —— B01 批次(15 条单因子)

_最后更新:2026-10-04 13:15 PDT,Opus 5.5 主会话(用户额度将尽时写的)。每到一个里程碑更新这一页。_

## 现在在跑什么(2026-10-05 起:方法改了,先读这一节)

**用户 2026-10-05 的批评与要求**:逐轮「主研下工单 → 执行跑 → 再裁决」太慢,15 条表达式不该研究这么久。要求:
(1) 假设成批提、成批看回测;(2) 研究实际市场 —— 分股票范围、分时间段看因子在哪有效,推断原因、给改进方向;
(3) 可以改最小的子结构(Ret ↔ 量的变化率 等);(4) 对算子的理解必须来自函数定义,不是名字;
(5) 可以一边研究一边补算子库(直接要用的 / 缺了可惜的 / 有创意的)。

**新流程(都是脚本,不耗模型额度;服务器上跑,不依赖本机)**
1. `scripts/sweep.py <fid> --tag s1 [--extra studies/<fid>/hypo.yaml]`:一条因子一次生成 70~260 个变体
   (删节点 / 换成实测性质相近的算子 / 换窗口 / 换字段 / 换叶子含 Ret↔in_pct(Volume) / 外加日轴记忆 / 折叠 / 缩尾 / 分桶中性 /
   对已知族残差 / 叠在已知族上 / 用户或主研给的额外假设),一次算完,出按多头净超额排序的回测表(只用 train / valid)。
2. `scripts/anatomy.py <fid> --sweep s1`:原式、已知族、最好的 8 个变体的**市场解剖** —— 板块、流通市值 / 成交额 / 价格五分位、
   上市时间、近 15 日是否有冻结盘口;逐年;市场近 20 日涨跌、波动高低、截面离散度、放量缩量。
3. `workflows/partura_batch_synthesis.js`:每条因子一个 Opus 5 主研,**只一轮**:读回测表 + 解剖 + 算子定义 → `notes/<fid>/synthesis.md`
   (它是什么 / 预测力在哪 / 在哪类股票和时段有效及原因 / 相对已知族的增量)+ `studies/<fid>/hypo.yaml`(20~40 条第二批假设)+ 要求的新算子。
4. 总领把值得加的新算子实现进 `partura/ops_ext.py`(登记在 `docs/new_operators.md`),再跑第二轮 `sweep.py --tag s2 --extra …`。
5. `scripts/sweep_final.py <fid> --sweep s2`:按**写死的规则**(各类里用户训练段纯多头夏普最高、过门槛、train 和 valid 多头腿都为正)
   选出候选,只对它们读测试段,出最终表。
- 看一条因子的表:`./scripts/study.sh table <fid> s1`;一键全跑:服务器上 `tmp/run_all_sweeps.sh`(`TAG=s2 EXTRA=…`)。
- 服务器独占时:`PARTURA_SLOTS=6 PARTURA_GPU_WAYS=2`(两条引擎线并行)。有邻居时去掉 `PARTURA_GPU_WAYS`、槽调回 3。

**进度**:2026-10-05 10:20 PDT 15 条的 s1 扫描 + 解剖在服务器上排队跑(F114 已完成并在做综合的试点,工作流 `wf_2b8259ae-98e`)。
旧的分层逐轮工作流(`partura_tiered.js`)已停用;它留下的 state.md / 工单 / 结果卡 / 5 条因子的测试段读数仍然有效,综合时可参考。

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
