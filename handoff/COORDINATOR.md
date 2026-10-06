# 总领(协调者)的现状 —— B01 批次(15 条单因子)

_最后更新:2026-10-05 13:45 PDT,Opus 5.5 主会话。每到一个里程碑更新这一页。_

## ★ 2026-10-05 傍晚:定位改了 —— Partura 不再是 AlphaCube 的下游(先读这一段)

用户给了路线图 `~/Downloads/AlphaCube_Partura_Research_Reading_Roadmap.docx`(文字摘录在 `docs/roadmap_2026-10_extract.txt`),并要求:
「多加一个块叫**反向指引 alphacube**。你的研究结论,可以变成指引 alphacube:改进奖励函数,改进评估因子方法,(重要)改进拒绝或者降低哪些
action 或者子结构的出现概率,增加你觉得有意思的可能研究方向的办法。我们现在研究一个 idea,只能自己生成一些因子,其实应该把想法给
alphacube 化,然后暴力搜索一下(短暂一下)。」定位与做法写在 **`docs/reverse_guidance.md`** 和 `CLAUDE.md` 开头。

**已经建好的(都在仓库里,服务器已同步)**
- `guidance/B01.yaml`:7 条奖励、7 条评估、33 条先验(5 封禁 / 14 降权 / 7 升权 / 7 改写去重)、已知池、5 个想法;每条带证据。
- `partura/steer.py`:模式匹配器(读表达式字符串)、`Guidance`(canonical / dedup_key / weight / accept)、奖励 `reward()`
  (`long` / `long_tradable` / `long_bucket` / `long_marginal` / `long_screen`;方向按多头腿、半衰期按纯多头书、分数取 train 与 valid 较差的)。
- `scripts/motif_stats.py` → `guidance/motif_stats_s2.json`:同一个动作套在 15 条因子上的成对统计(先验的证据)。
- `scripts/idea_search.py` + `./scripts/study.sh idea <id> [--budget 192 --population 48 --tag e1]`(`idea-log <id>` 看日志,`idea-pull` 拉证据):
  把一个想法交给 AlphaCube 的 GP 短搜,steer 臂(种子 + 算子加权 + 过指引 + 留在邻域)对 control 臂(同预算、同奖励、不带干预)。
  **不改 AlphaCube 的文件**:运行时替换 `alphacube.mining.scoring.make_scorer`、`TypedTreeGenerator.acceptable` / `._pick`。
  冒烟测试通过(预算 16,465 秒);第一代约 5 分钟,全市场大约 6~10 秒一个候选。
- `scripts/guidance_report.py` → `research/alpha_distillation/B01_reverse_guidance.md`(给用户看的;有干预实验时自动带上结果)。
- `scripts/merge_lab.py`:14 份对账的 101 条 lab 结论已并入 `lab/findings.yaml`(共 154 条)。`handoff/TOOLING.md`:主研们报的工具问题与处置。

**这一轮顺手修掉的错**(都影响结论,第三轮因此整轮重跑)
- `cross_ema` 在成交额量级的输入上溢出成 NaN(float32;F105 主研发现)→ 改在 float64 里算;缓存里 186 张相关面板已清。
- 9 个新算子被 AlphaCube 的自检错标成 boolean(进不了 GP 词表、不能当根)→ `ops_ext` 建注册表后清标。
- `scripts/sweep.py`:`dist` 门槛改算在实际交易的信号上;`cs_first_*` / `cs_last_*` 为根的变体锁定方向。
- `scripts/sweep_final.py`:候选按被选中时的方向读测试段。

**正在跑(2026-10-05 约 18:00 PDT 起)**
- 服务器 screen `idea_I2_dispersion_fold`:想法 I2(日内离散度的折叠)两臂各 192 个候选,奖励 `long_marginal`;日志 `logs/_idea_I2_dispersion_fold.log`,
  产出 `episodes/e1_I2_dispersion_fold/evidence.json`。
- 服务器 screens `r3_F1xx`:第三轮(tag `s3`)15 条全部重跑(4 个槽;之前 9 条跑完的结果是旧 `cross_ema` 下的,作废)。

**它们跑完之后(按顺序)**
1. `./scripts/study.sh idea-pull`;`python scripts/guidance_report.py guidance/B01.yaml`(干预实验进报告);在 `episodes/e1_…/episode.md` 写信念更新,回改 `guidance/B01.yaml` 的权重 / 状态。
2. 拉回 `runs/<fid>/*_s3.json`(`rsync --include='*_s3.json'`);服务器 `scripts/batch_cluster.py … --tag s3` → `scripts/batch_fuse.py … --tag s3`(融合的测试段读数,记账)。
3. 本机 `scripts/motif_stats.py … --tag s3`、`scripts/batch2_summary.py … --tag s3`、`scripts/readable_report.py … --tag s3` → 发给用户(用户要的是好读的那种)。
4. 再跑 1~2 个想法(I1 当筛子 `long_screen`、I5 只换奖励不限结构 —— 后者是「先验本身有没有用」最干净的检验)。
5. F111 的对账因断网没回来(`resumeFromRunId: "wf_4811c95a-915"` 可补);不影响第三轮(它的 `hypo3.yaml` 已写好并通过校验)。
6. commit + push;更新记忆。

## ▶ 2026-10-05 14:55 PDT:用户说「继续」,已恢复(13:53–14:55 曾全部暂停)

用户恢复时加了两件事,**都已交付**(15:20):
1. 「先打印一份我能看懂的回测结果,各个你觉得改进好的升级版的」→ `research/alpha_distillation/B01_upgrades_and_fusion.md`
   (`scripts/readable_report.py batches/B01_single_factors.yaml --tag s2`,本机跑;表 1 = 9 个独立升级版,表 2 = 已知族的升级版,带大白话说明和完整表达式)。
2. 「简单融合和平滑一下大家,让我看看样本内外的结果」→ 服务器 `scripts/batch_fuse.py batches/B01_single_factors.yaml --tag s2`
   (成员按规则只看样本内选;融合 = 成员截面 z-rank 等权均值;测试段**已读,记账**在 `runs/_batch_B01/ledger.json`)→ `runs/_batch_B01/fuse_s2.json`,曲线 `B01_fusion_curves.svg/.png`。
   多头净超额 样本内 / 样本外(纯多头夏普):已知族单独 +15.4 / +14.1(2.22 / 1.51);**原式 15 条等权 +15.8 / +11.1(3.26 / 1.63)**;
   升级版 15 条等权 +20.2 / +16.0(3.65 / 1.63);**独立 9 个等权 +20.1 / +17.3(3.95 / 1.93)**,8 年都在 +15~+22%;
   已知族簇首单独 +18.1 / +16.8(3.16 / 1.74);独立 9 + 已知族簇首(10 个等权)+20.3 / +17.7(3.91 / 1.87);一半已知族簇首 + 一半独立 9 个 +20.2 / +18.3(3.62 / 1.82)。
   平滑:成员各自平滑后再融合,融合后再平滑不加收益(换手 3.0% → 1.3%,样本外夏普不变 ~1.9,回撤 −14.1% → −10.5%);不先各自平滑直接融合明显更差。
   风险:样本外最大回撤都在 2024-01-16~02-06(微盘股踩踏),升级版融合 −13~−17%,原式融合只有 −5%。
- 对账轮工作流已用 `resumeFromRunId: "wf_4811c95a-915"` 续上(task `w35xy9gym`);recorder 与 caffeinate 已重启。
- 跨因子聚类 `scripts/batch_cluster.py … --tag s2`(只用训练段)已跑完:24 个簇,`runs/_batch_B01/cluster_s2.json`;总表 `B01_batch_summary.md` 已带「0.5 跨因子」一节。
- `scripts/sweep_final.py` 改了一处:候选按**被选中时的方向**读测试段(第二轮 120 个读数里只有 F106.abl_M 一个弱候选受影响,已在第三轮自然被覆盖)。

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

**进度(2026-10-05 13:45 PDT)**
- 第一轮(tag `s1`):15 条的扫描 + 解剖 + 综合(`notes/<fid>/synthesis.md`、`studies/<fid>/hypo.yaml`)全部完成。
- 新算子:`partura/ops_ext.py` 共 45 个(定义与理由见 `docs/new_operators.md`),都用手算答案核过、已部署到服务器。
  没做的:`cs_bucket_rank2`(要 3 个张量操作数,文法只支持 2 个);**数据层字段**(流通市值 / 流通股本、板块与涨跌幅限制宽度)——
  6 条因子的综合都要,这要动 AlphaCube 的数据层,**已问用户,等答复,不要自己动**。
- 第二轮(tag `s2`):15 条的扫描(含第二批假设)+ 解剖 + 按规则读测试段全部完成,`runs/<fid>/{sweep,anatomy,sweepfinal}_s2.json` 已拉回本机;
  总表 `research/alpha_distillation/B01_batch_summary.md`(`scripts/batch2_summary.py … --tag s2`)已发给用户(commit `6c33dff`)。
- **正在跑(14:55 续跑)**:对账轮,工作流 run `wf_4811c95a-915`(`partura_batch_synthesis.js`,`round: 2`,15 个 Opus 5 主研,标签 `verdict:<fid>`):
  读 `./scripts/study.sh table <fid> s2 --all`(只有 train / valid),写哪些假设被证实 / 证伪、最好的版本、`lab_findings`,
  并用最新 23 个算子写第三批假设 `studies/<fid>/hypo3.yaml`(用 `./scripts/study.sh hypo3 <fid>` 自查)。结果由 recorder 落到 `handoff/<fid>/results/verdict.json`。
  被额度打断时:`Workflow({scriptPath: 同一个脚本, resumeFromRunId: "wf_4811c95a-915"})`,做完的不会重跑。
- 已完成:`scripts/batch_cluster.py batches/B01_single_factors.yaml --tag s2` 的试跑(只用训练段),`runs/_batch_B01/cluster_s2.json`。

**接下来(按顺序)**
1. 对账轮回来后:`for f in studies/*/hypo3.yaml` 都过 `./scripts/study.sh hypo3 <fid>`;把 `studies/` 同步到服务器;
   服务器上 `tmp/run_round3.sh <15 个 fid>`(tag `s3`,`--extra studies/$fid/hypo.yaml,studies/$fid/hypo3.yaml`,日志 `logs/<fid>_round3.log`,screen `r3_F1xx`)。
2. 拉回 `runs/<fid>/{sweep,anatomy,sweepfinal}_s3.json`(`./scripts/study.sh table <fid> s3` 会拉)。
3. 服务器:`scripts/batch_cluster.py batches/B01_single_factors.yaml --tag s3`(只用训练段)→ `scripts/batch_fuse.py batches/B01_single_factors.yaml --tag s3`(融合的测试段读数,记账;第二轮的融合已按用户要求读过一次)。
4. 本机:`scripts/batch2_summary.py … --tag s3` + `scripts/readable_report.py … --tag s3`(好读的那份,用户要的是这种)→ 发给用户。
5. 各 `handoff/<fid>/results/verdict.json` 的 `lab_findings` 合并进 `lab/findings.yaml`;更新本页与记忆;commit + push。

旧的分层逐轮工作流(`partura_tiered.js`)已停用;它留下的 state.md / 工单 / 结果卡仍可参考。

## 仓库

GitHub 私有仓库 **https://github.com/xiangyu2024/Partura**(2026-10-04 建;分支 `main`;只有用户本人是协作者,别人要看由用户邀请)。
本机 `~/Desktop/Partura` 的 `origin`;用 HTTPS + macOS 钥匙串里的凭据推(和 AlphaCube 一样)。**每个里程碑**:
`git add -A . && git commit -m "…" && git push`(`runs/*.json`、`logs/`、`handoff/` 都在版本库里;面板缓存 `runs/_panels/`、`*.npy` 不进)。
仓库里有服务器的 SSH 地址(`scripts/study.sh`),没有任何密码或密钥。

## 第二轮的结论(多头腿净超额 训练 / 测试,括号纯多头夏普;完整见 `research/alpha_distillation/B01_batch_summary.md`)

对照:已知族 `cross_mean(day_std(Amt), 30)` +15.4% / +14.1%(2.22 / 1.51);通用筛子 `k_known_xfrozen`(已知族剔掉近 15 日冻结盘口最重的 20%)+18.5% / +14.7%(3.15 / 1.56)。

| 因子 | 原式 | 独立于已知族的最好版本 | 建在已知族上的最好版本 |
|---|---|---|---|
| F101 | +7.1 / +7.1 | 一处 `Volume` 差分换 `Amt`:+9.7 / +7.2(2.68 / 1.60),ρk 0.16 | 低流动性 40% 里按 F101 反向选:+16.0 / +15.6(2.67 / 2.03) |
| F102 | +8.9 / +2.5 | `cross_max(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 60)`:+11.3 / +7.0(2.85 / 1.45) | 已知族在本因子高 40% 里:+16.3 / +14.0 |
| F103 | +8.1 / +7.2 | (落在已知族) | 已知族连剔冻结盘口 + 次新:**+18.1 / +16.8(3.16 / 1.74)** |
| F104 | +1.8 / −2.1 | (无;原式不可用) | `day_std(nt_cs_mask_top_replace_mean_neg(sqrt(Amt)))` +15.1 / +12.6;筛子 +18.5 / +14.5 |
| F105 | +11.8 / +8.9 | 原式 + 冻结盘口筛子:+13.3 / +10.2(2.75 / 1.22) | — |
| F106 | −5.8 / −3.2 | `sub(cs_rank(neg(cross_mean(day_zero_ratio(Ret), 30))), cs_rank(cross_mean(day_sum(Amt), 30)))`:+12.1 / +15.5(2.08 / 1.70),ρk 0.46 | — |
| F107 | +1.7 / +1.4 | **`cross_ema(abs_(cs_demean(day_gini(Low))), 30)`:+11.7 / +11.2(2.87 / 2.10)**,8 年全正 | — |
| F108 | +1.0 / −3.2 | (无) | `day_max(pow_2(nt_ts_std(Amt, 30)))` +16.5 / +13.3;筛子 +17.8 / +14.7 |
| F109 | −3.2 / +2.9 | (无稳健版本) | — |
| F110 | −0.2 / −0.8 | `cross_ema(pow_3(sub(div(day_last(Close), day_first(Open)), 1)), 30)`:+8.8 / +12.5(1.79 / 1.11) | — |
| F111 | +12.3 / +6.0 | 原式 + 冻结盘口筛子:+13.5 / +7.7(2.46 / 1.05) | — |
| F112 | +4.2 / +6.9 | `signedpower(cs_mask_top_replace_mean_neg(add(day_quantile(Close), day_kurt(High))))`:+8.4 / +7.9(1.85 / 1.53) | — |
| F113 | +0.7 / −0.6 | (无) | 叠加 0.25:+14.8 / +15.1;低流动性分段 +10.7 / +13.3 |
| F114 | +3.6 / +0.2 | (无) | 已知族秩 + 0.5 × `cross_mean(day_flat_ratio(Close), 15)` 秩:+15.7 / +15.4(2.80 / 1.68) |
| F115 | +4.1 / +1.8 | (无稳健版本) | — |

跨因子的共同发现:(1) 选股力集中在约 6.5% 的冻结盘口票(封板 / 停牌),剔掉它们是最通用的一招;(2) `+1e-6` 一类绝对小量分母把因子变成涨跌停探测器;
(3) 很多书是流动性倾斜、桶内选股为负;(4) 用户说的 Ret ↔ 量变化率互换在 F101 成立,在 F102 / F104 / F114 不成立。
测试段一共读了约一百个候选(按规则、记账),榜首有向上的选择偏差。

## 用户定的规矩(不要改)

- 选拔口径:**多头腿净超额 / 纯多头夏普**,半衰期按纯多头书选;延长半衰期带来的净超额是有效的。
- 分工:总领 Opus 5.5;主研 Opus 5;执行(写代码、跑实验、读结果)Sonnet 5。**研究全程落盘**(额度随时会断,换模型要接得上)。
- 研究方法(2026-10-05):假设成批提、成批看回测;分股票范围 / 分时间段看因子在哪有效并推断原因;可以改最小的子结构;
  **对算子的理解必须来自函数定义**,不是名字;可以边研究边补算子库。
- 服务器:2026-10-04 14:30 起用户说"全面归你用";但**不是自己起的进程一律不杀**,`/root/autodl-tmp/AlphaCube` 当只读(新算子放 `partura/ops_ext.py`)。
- 测试段(留出段)只按写死的规则读、每次记账;不许按测试段的数字挑候选。
- GitHub 仓库保持私有,只有用户能邀请别人;凭据不打印、不外发。
- 汇报用中文,结论先行,数字都是扣费后的。
