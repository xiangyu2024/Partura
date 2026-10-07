# 总领(协调者)的现状 —— B01 批次(15 条单因子)

_最后更新:2026-10-06 14:10 PDT,Opus 5.5 主会话。每到一个里程碑更新这一页。_

## ⏱⏱⏱⏱⏱⏱⏱ 现状快照(2026-10-06 21:03 PDT;最新,先读这段)

**e4 的倍数更正**:按式子的族数是 44 对 4;按**实测互不相关**的发现数(交易信号两两秩相关 < 0.7)是 **16 对 3**(2:0、5:1、9:2,三个种子同向)。
以后两个数都报、以实测的为准(指引 E10;`scripts/factorial_summary.py`、`episodes/e4_SUMMARY.md` 顶部的更正)。

**e5 消融:18 个 run 完成 16 个**(`episodes/e5_PLAN.md`;最后一格 seeds+priors 的种子 2、3 还在 screen `e5b` 里,种子 2 抽到很重的算子,一代约半小时)。
- 中间读数(每百次付费评估里实测互不相关的发现):对照 0.7 / seeds 0.9 / hood 1.2 / priors 1.8 / seeds+hood 2.6 / hood+priors 3.1 / 全开 4.1;seeds+priors 只有 1 个种子(2.5)。
  大致可加:三样各自都有贡献。跑完后:`./scripts/study.sh idea-pull` → `python scripts/factorial_summary.py I1_frozen_state 0=e4k:control shr=e4k:steer s=e5s h=e5h r=e5r sh=e5sh sr=e5sr hr=e5hr` → 写 `episodes/e5_SUMMARY.md`。
- **确定性核对通过**:`rr_e5s1`、`rr_e5h1`(同种子、同代码重跑)和原 run 逐个候选、逐个分数完全相同(最大差 0)。→ 搜索在给定种子和代码下是确定的;并行跑的校准没有干扰 e5;以后对照臂不用重跑。
- e5sr3 会在新版 `scripts/idea_search.py`(c26fdabde043,只多一个 `--halflives` 选项,默认值不变)下跑,其余 17 个是 51248194fc24;行为相同,指纹不同,写总结时注明。
- **先验规则的直接检验**(`scripts/prior_check.py`,`runs/_ideas/prior_check_*.json`):拿对照臂(没被指引过滤过)的 638 个存活候选来看,
  指引会碰到的只有 23%,几乎全是 D7(`div` × 0.5)一条,而且它不区分好坏(发现率 0.7% 对 1.0%,分数中位 +0.44 对 +0.47);
  「毁掉多头腿」的那些规则(根上的 z 分数、滚动标准差、滚动最小)各只碰到 1~2 个 —— 碰到的确实都很差(−4.1、−1.9、−1.1),但 GP 的随机树里很少出现这些结构。
  先验一臂的好处来自别处:没过门槛的比例从 30% 降到 21%(存档里看不到死掉的候选),以及等价 / 同族去重带来的多样性。
  **结论草稿**:从 Partura 自己的批量变体里学到的动作先验,换到 AlphaCube 的 GP 上大多用不上(两个生成器提出的东西不一样);要给 GP 定先验,得从 GP 自己的存档里学。
  用户的 AlphaCube 有约 22 个 GP 运行的存档(`/root/autodl-tmp/AlphaCube/mining_runs/*/checkpoints/archive_gen*.csv`,每个 250~570 个存活候选),还没用过 —— 这是先验这条线的下一步。

**e6 已起跑**(`episodes/e6_PLAN.md`;21:02 PDT 起):想法 `I7_beyond_liquidity`,奖励 `long_bucket`,半衰期 0/5/20/60,预算 384,发现线 0.75。
- screen `e6a`:种子 1、3(`scripts/server/run_idea_seeds.sh`,服务器端启动脚本现在在仓库里);screen `e6c`:种子 2,排在 `e5b` 后面。完成记在服务器 `logs/_e6b.log`(3 行)。
- 每个种子两臂估计 1~3 小时(取决于抽到的算子有多重)。跑完:`idea-pull` → `python scripts/episode_summary.py e6b I7_beyond_liquidity` →
  按 `e6_PLAN.md` 的规则读样本外:`scripts/idea_final.py e6b1_I7_beyond_liquidity e6b2_I7_beyond_liquidity e6b3_I7_beyond_liquidity`(服务器,记账)→ 写 `episodes/e6_SUMMARY.md`。

**等用户定**:2026-01 ~ 2026-08 那段没碰过的数据怎么用(见下一段快照);没读。

**AlphaCube 改造**:`partura-steering` 到 `0d93fa3` WP4(19:30)。已完成 WP1, WP6, WP2, WP3, WP5, WP9, WP4;还剩 WP7, WP8, WP10, WP11 和三项整分支验证。

## ⏱⏱⏱⏱⏱⏱ 现状快照(2026-10-06 18:24 PDT;已被上面那段更新)

**e4 确认实验(事先约定 `episodes/e4_PLAN.md`,结果 `episodes/e4_SUMMARY.md`)**
- 参照 = 未筛的已知族(e4k,三个种子):带指引 **44 族**发现 / 393 次评估,对照 **4 族** / 427 次;三个种子全部同向(9:0、22:1、13:3)。按事先的标准(≥ 2 倍且 ≥ 2 个种子同向)**成立**:
  想法 + 指引在「有东西可找」的地方把搜索效率提高了约 10 倍。44 族里没有一族是种子本身。
- 参照 = 已做通用筛子的已知族(e4p):两臂都是 0(931 次评估)。通用冻结筛子之外,这个邻域里没有可剔的票。
- **样本外**(规则写在读之前,`scripts/idea_final.py`,`episodes/e4k1_e4k2_e4k3_final.json`):每个种子 × 臂的头名共 5 个,原样重建后都复现了搜索的数字,测试段成对差 −0.9 ~ +0.6 个点,**t 全部 < 1**(带指引 0/3,对照 0/2)。
  → 搜索效率是真的,但「对已知族做筛子」这个想法没有样本外内容。方法通了,想法到此为止。

**校准:这批因子赚的是哪一种钱**(`research/alpha_distillation/B01_reward_calibration.md`,`scripts/reward_probe.py`)
- 第四轮的 12 个独立成员(及其核心)在三种口径下打分:原口径 → 可交易池(躲垃圾票不再算超额)→ 桶内(偏向低流动性不再算超额)。
- 「典型性」折叠:原口径 valid +1.69 → 可交易池 −0.97(= 在躲垃圾票)。其余成员:可交易池里 1.3 ~ 3.5 → 桶内 −2.1 ~ +0.1(= 流动性倾斜)。
  桶内两段都为正的只有两条:`ts_pearson(day_last(Close), 20)` +0.56 / +0.94、`cs_bucket_demean(cross_mean(day_gini(Ret), 30), LIQ)` +0.49 / +0.68。
- 所以 2022 年以后这批因子的多头超额 = 躲垃圾票 + 流动性倾斜,不是新的选股内容 —— 和「融合比已知族只多 2.3 个点、t 0.6」是同一件事。

**⚠ 要请用户定的一件事:服务器的数据其实到 2026-08-17(增量到 9 月中)**
- `/root/autodl-tmp/qmt_daily_data/fast_factor_compute`:2092 个交易日,20180102 ~ 20260817;`incremental/segments` 到 20260916。我们所有的划分都只到 20251231。
- 2026-01 ~ 2026-08 约 150 个交易日**从没被任何读数碰过**。我没有读它,也不要在用户同意之前读:读一次就不再干净。
- 建议(等用户回答):把它当作一次性的前推检验,事先写死读什么(第四轮融合 A / C 对已知族的成对差;原式融合;通用冻结筛子;e6 若有发现),只读一次、记账。

**服务器上正在跑:e5 消融**(事先约定 `episodes/e5_PLAN.md`;17:57 起,`tmp/run_e5.sh`,screen `e5a` / `e5b`;随后 screen `e5rr` 自动重跑 e5s1 / e5h1 作确定性核对)
- 2×2×2:带指引一臂的三个开关 seeds / hood / priors(`scripts/idea_search.py --parts`),每格三个种子,只跑带指引的一臂;对照和全开两格用 e4k 的。
- 完成记在服务器 `logs/_e5.log`(共 18 + 2 行),预计 20:15 PDT 前后跑完。
- **跑完之后**:`./scripts/study.sh idea-pull` → `python scripts/factorial_summary.py I1_frozen_state 0=e4k:control shr=e4k:steer s=e5s h=e5h r=e5r sh=e5sh sr=e5sr hr=e5hr`
  → 按 `e5_PLAN.md` 的标准写 `episodes/e5_SUMMARY.md`;核对 `rr_e5s1` / `rr_e5h1` 与原 run 是否一致(同种子同代码应当一致)。
- 注意:e5 进行期间**不要同步 `scripts/idea_search.py`**(本机已加 `--halflives`,服务器上还是 e5 起跑时的版本 51248194fc24);等 e5 全部结束再 `./scripts/study.sh code`。
- 教训:对照实验进行时别在同一张卡上跑别的东西。这次并行跑的校准是靠 GPU 锁排上队的(日志里 `got lock 'gpu' after 386s`),没有超占显存,但我事先的估计是错的。

**下一个实验 e6(事先约定 `episodes/e6_PLAN.md`,还没跑)**:想法 `I7_beyond_liquidity`,奖励 `long_bucket`,半衰期 0/5/20/60,每臂预算 384,三个种子;发现线 0.75。
起跑命令(e5 结束、`study.sh code` 之后,在服务器上仿照 `tmp/run_e4.sh` 写 `tmp/run_e6.sh`):
`scripts/idea_search.py I7_beyond_liquidity --budget 384 --population 48 --tag e6b<seed> --seed <seed> --halflives 0,5,20,60 --threshold 0.75`;
读样本外:`scripts/idea_final.py e6b1_I7_beyond_liquidity e6b2_… e6b3_…`。

**AlphaCube 改造(工作流 `wf_a9e46c78-369`,仍在跑)**:`partura-steering` 到 `b12dca2` WP5(17:24;生成器钩子)。已完成 WP1, WP6, WP2, WP3, WP5;还剩 WP9, WP4, WP7, WP8, WP10, WP11 和三项整分支验证。

## ⏱⏱⏱⏱⏱ 现状快照(2026-10-06 16:25 PDT;已被上面那段更新)

**今天下午的三个更正 / 对账(都已推送,最后一条提交见 `git log`)**

1. **K001 筛子研究:搜到的筛子样本外没有站住。**(`studies/K001_known_screens/README.md`「结果」;规则写在看结果之前)
   九个单层两成筛子 + 样本内前六个多层筛子,测试段上对已知族的成对差 t 最高 1.1;通用冻结筛子自己样本内 +3.1 个点、样本外 +0.9 个点(t = 0.6),
   增益集中在 2018–2020(逐年 +6.5 / +3.4 / +4.8,之后平均 +0.9)。「成交集中价位不稳」当筛子是空操作。→ 指引 U5 由升权改为备注,R1 加了样本外读数。
2. **第四轮融合对已知族的样本外优势:+2.3 个点 / 年,t = 0.6。**(`runs/_batch_B01/paired_fusions.json`;好读版报告表 3b)
   同一天相减:独立 12 个的融合 − 15 条原式的融合 = 样本内 +5.5、样本外 **+6.5**(t 1.5,幅度没缩水);− 已知族 = 样本内 +5.1(t 2.1)、样本外 **+2.3**(t 0.6)。
   三轮都是这个量级(s2 +3.2 / t 0.8;s3 +1.6 / t 0.4)。原式的融合样本外比已知族**差** 4.3 个点。
   说法要改成:「升级把一批比已知族差的原式变成了不比它差、夏普更高(1.98 对 1.52)的东西;比已知族好多少,两年半的样本分不出来」。指引规则 E9:比基准好一律用成对差判。
3. **e3_I1 的参照写错了,而且「打平」是尺子的问题。**(`episodes/e3_I1_frozen_state/belief.md`)
   服务器上跑的是旧版 `scripts/idea_search.py`(`tmp/after_round4.sh` 直接起的,没先同步)→ 参照是没做过筛子的已知族。
   按成对信息比数 26 对 22;按「账面每年多赚 ≥ 1 个点、两段都是」数,带指引 **11 族**、对照 **0 族**(事后读数)。对照臂的发现是又小又稳的改动(信息比 2~3、账面 +0.2~0.8 个点)。

**因此改的代码**
- `partura/steer.py: _sized` —— 成对奖励带大小:`IR × min(1, 每年多赚 / 1 个点)`;`score / score_train / score_valid` 都带大小,另返回 `ir_*`、`dann_*`。指引 R8。
- `partura/steer_fast.py` —— 奖励里的排序 / 桶内排名 / 并列带 / 十分位书搬到 torch(`PARTURA_REWARD_DEVICE=cuda`;出错回退原版)。
  服务器实测(`scripts/reward_bench.py`,真实面板 8 个):4.9 / 5.0 / 10.9 / 7.4 / 7.9 秒 → 1.2~1.4 秒,所有返回值相对差 ≤ 3.5e-14。
  之前每个候选 ~10~16 秒里有一半是奖励;现在 ~6.5 秒(面板 ~5 秒)。这是目前量到的最大一项搜索效率改进(1.6~2.5 倍),比先验大。
- `scripts/idea_search.py`:证据里记 `code`(文件指纹)、`screen_base`、`reward_device`、原始信息比与每年多赚。
- `scripts/study.sh code`:一次同步全部代码(partura / scripts / guidance / batches / tests / configs)。**服务器端的启动脚本(tmp/*.sh)不会同步,起之前先跑它。**
- `scripts/sweep_final.py` 成对表、`scripts/paired_table.py`;`scripts/readable_report.py` 表 3b;`scripts/guidance_report.py` 第 6 条结论。
- 测试 56 例通过(`tests/test_steer_fast.py` 7 例:原版 vs torch 版逐数相同)。

**服务器上正在跑:e4 确认实验**(事先约定 `episodes/e4_PLAN.md`;16:19 PDT 起,`tmp/run_e4.sh`,两个 screen 各占一路 GPU)
- screen `e4k`:`--screen-base known`,种子 1、2、3 依次 → `episodes/e4k{1,2,3}_I1_frozen_state/`,日志 `logs/_idea_e4k{n}_I1.log`
- screen `e4p`:`--screen-base pool`,种子 1、2、3 依次 → `episodes/e4p{1,2,3}_I1_frozen_state/`
- 每个种子两臂约 35~40 分钟;全部跑完约 2 小时。完成记在服务器 `logs/_e4.log`。
- **跑完之后**:`./scripts/study.sh idea-pull` → `python scripts/episode_report.py` → 按 `e4_PLAN.md` 的判读写 `episodes/e4_SUMMARY.md` 和各卡的 `belief.md`
  (主指标:每个种子两臂各自的发现族数;带指引合计 ≥ 对照 2 倍且至少两个种子同向才算有证据)→ `python scripts/guidance_report.py guidance/B01.yaml --tag s4`。

**AlphaCube 改造(实现工作流 `wf_a9e46c78-369`,仍在跑)**:分支 `partura-steering` 16:18 时到 `cc6619b` WP3(14:15 提交;正在审查 / 修)。
还剩 WP5, WP9, WP4, WP7, WP8, WP10, WP11 和三项整分支验证,按现在的速度还要 8~12 小时。结束之后总领要做的事不变(见下面 22:00 那段「实现完成之后」)。
注意:并入后 WP11 的 `ac-plugin` 分支和主分支在 `partura/steer.py`、`scripts/idea_search.py` 上差得更多了(今天加了 `steer_fast`、带大小的奖励、指纹),合并时以**主分支为准**。

**接下来(按顺序)**
1. e4 的结果 → 判读 → 指引更新。
2. 实现工作流结束 → 验证 → 并入 AlphaCube main → 同步服务器 → 建日频字段库 → 合并 Partura `ac-plugin` → 用正式钩子重跑一个短搜作验收。
3. 第五轮:带流通市值 / 涨跌幅宽度的假设(`DailyFeature` 叶子)。筛子不再当通用变体(K001)。
4. 搜索效率的下一项:候选的门槛失败率 13~39%(付了面板钱才知道是废品)→ 先在小样本(1/8 股票)上算面板、过了再算全市场(多保真度);还没做。
5. `handoff/TOOLING.md` 里剩下的工具项。

## ⏱⏱⏱⏱ 现状快照(2026-10-06 14:10 PDT;已被上面 16:25 那段更新 —— 其中「I1 参照 = 已做通用筛子的已知族」「第三次打平」两句作废)

**第四轮(s4,带全部修正)已完成并交付**(提交 `ece6845`;报告 `research/alpha_distillation/B01_upgrades_and_fusion.md`、`B01_batch2_summary.md`)。
多头净超额 样本内 / 样本外(纯多头夏普);样本内 = 2018-01 ~ 2023-08-07,样本外 = 2023-08-08 ~ 2025-12-31,扣 15 bp:

| 组合(等权,成员各自平滑) | 净超额 | 夏普 |
|---|---|---|
| 15 条原式 | +14.9% / +9.8% | 3.24 / 1.61 |
| 15 条升级版 | +20.4% / +16.2% | 3.50 / 1.67 |
| **独立的 12 条升级版** | **+20.5% / +16.4%** | **3.95 / 1.97** |
| 独立 12 条 + 已知族头名 | +20.5% / +16.6% | 3.90 / 2.02 |
| 已知族头名 `F114.h3_xfr_plus_slowf` 单独 | +19.5% / +14.7% | 3.48 / 1.95 |
| 已知成交额族(基准) | +15.4% / +14.1% | 2.22 / 1.51 |

样本外最大回撤 −12.4%;逐年 +15% ~ +24%。所有升级版融合在 2024-01-16 ~ 02-06(微盘股踩踏)丢 12~17 个点的超额,原式融合那段约 +0.8%。
三轮(s2 / s3 / s4)的独立成员融合都落在 样本内 +20% / 样本外 +16~17%、夏普 ≈ 4 / ≈ 1.9~2.0 —— 修掉审查查出的缺陷之后结论没变。

**想法短搜 e3(成对信息比口径)两个都跑完,实验卡已写**(`episodes/e3_*/episode.md`)
- I2 离散度折叠(对池子的边际):带指引最好 +0.60(train +1.18 / valid −0.93),对照最好 −0.27,谁也没到 1.0。量对了之后结论是「2018–2021 加分、2022 起减分」,不是发现。
- I1 冻结盘口筛子(参照 = 已做通用筛子的已知族):按新定义的「发现」带指引 26 个 / 18 族,对照 22 个 / 20 族 —— **第三次打平**。
  两臂找到的是不同类型的筛子:带指引 = 封板(`cross_mean(day_at_max_ratio(Vwap), 15)`,train +1.46 / valid +1.41);
  对照 = 成交集中价位不稳(`ts_std(day_topw_mean(Volume, Close), 20)`,+2.03 / +1.60)。
- **到现在没有证据说指引提高了搜索效率**(每臂 ~150 次评估量不出来;规则 E7:要几千次)。指引目前确定有用的只是「不为等价写法重复付钱」。

**今天下午加进代码的(都已推送,最后一条提交 `3d2d99b`)**
- `partura/steer.py: is_discovery` —— 「发现」的唯一定义:水平类奖励 = 分数过线;成对奖励 = 合并段过线 **且** train、valid 各自 ≥ 0.5(合并段被 4 年的 train 主导)。
  `scripts/idea_search.py`、`scripts/episode_report.py`、`scripts/guidance_report.py` 共用。指引规则 E8。
- `family_key` 认最外层保序函数(`pow_05(X)` 与 `X` 同族;规则 C9,0.3 的概率放行);实验卡和指引报告按「族」另数一遍。
- `scripts/sweep_final.py`:`--onknown N`;每个候选和 `k_known` / `k_known_xfrozen` 的**成对逐日差**(年化差 / 信息比 / t 值),比两个年化数相减灵敏得多。
- 测试 48 例通过。

**服务器上正在跑:K001 筛子研究**(screen `k001`,`tmp/run_k001.sh`,日志 `logs/K001_known_screens_s1.log`)
- 不是用户表里的因子:底座 = 已知族,45 条假设(`studies/K001_known_screens/hypo.yaml`)= 短搜两臂找到的筛子各当一次通用筛子(单层 20 / 10 / 5%、叠在冻结筛子上的两层、三层、四层、只罚不剔)。
- **测试段读数规则写在看结果之前**:`studies/K001_known_screens/README.md`(九个单层两成筛子原样全读 + 样本内前 6;判读 = 对已知族 / 对通用筛子的成对差 t ≥ 2 且样本内同号)。
- 跑完之后:`rsync` 拉回 `runs/K001_known_screens/`,把结论写进 `studies/K001_known_screens/README.md` 的「结果」一节和 `episodes/e3_I1_frozen_state/belief.md`;
  成立的筛子进 `scripts/sweep.py` 的通用变体(和 `k_known_xfrozen` 并排当基准)和指引的 U5。

**AlphaCube 改造(实现工作流 `wf_a9e46c78-369`,仍在跑)**:`~/Desktop/AlphaCube-steering` 分支 `partura-steering` 已有
`1167f00` WP1、`6a4bda1`+`da4898f` WP6、`2d665e2`+`3c2e68c` WP2;14:00 时 WP3(`store.py` 的日频字段读取)正在实现。还剩 WP5, WP9, WP4, WP7, WP8, WP10, WP11 和三项整分支验证。
结束之后总领要做的事不变(见下面 22:00 那段「实现完成之后」)。被打断就按那里的命令续跑。

**接下来(按顺序)**
1. K001 的结果 → 结论 → 通用筛子基准 / 指引更新。
2. 实现工作流结束 → 验证 → 并入 AlphaCube main → 同步服务器 → 建日频字段库 → 合并 Partura `ac-plugin`(以主分支行为为准)→ 用正式钩子重跑一个短搜作验收。
3. 第五轮:带流通市值 / 涨跌幅宽度的假设(`DailyFeature` 叶子)+ K001 里成立的筛子当通用变体。
4. 大预算的先验效率实验(每臂几千次评估,I5),要等 AlphaCube 有按时间的预算 / 正式钩子。
5. `handoff/TOOLING.md` 里剩下的工具项。


## ⏱⏱⏱ 现状快照(2026-10-06 10:30 PDT;最新,先读这段)

**昨夜**:审查工作流 `wf_b7c13476-92d` 跑完(93 个 agent,1240 万 token —— 就是它把额度用光的;1:50 重置)。实现工作流在第一个包的审查处被额度打断,今天 09:55 已原样续跑。

**审查的结果与处置**:`handoff/REVIEW_FINDINGS.md`(逐条)。24 条成立(13 条 high 全部被复现)、31 条被推翻。今天上午已修 23 条(只剩「报告口径」那条刚修完、等第四轮验证),
回归测试 `tests/test_ops_ext.py`(14 例)+ `tests/test_steer.py`(14 例),全部通过(`ALPHACUBE_ROOT=~/Desktop/AlphaCube PYTHONPATH=~/Desktop/AlphaCube/src:. ~/.venvs/alphacube/bin/python -m pytest tests/ -q` → 46 passed)。
影响结论的几条:
- **筛子 / 分段算子在并列块里按股票顺序任意切**(`_lexi`)。「剔上市最短两成」实际只有 7 个点是次新、13 个点是任意的老票 → 第三轮里所有以 `cross_valid_count` 当键的读数作废
  (含 F103 的「连剔冻结盘口 + 次新 +18.1 / +16.8」那一行的第二层)。已改成整块并列进带。
- **对池子的边际奖励两边不在同一个股票池**(候选自己的缺失会移动它的基准)→ 改成同一批格子上的成对逐日差的信息比(`partura/steer.py: reward`,`PAIRED`)。
- **`dedup_key` 把所有价格叶子并成一个**(`sub(High, Low)` 与 `sub(Close, Open)` 被当成同一个候选)→ 只做精确等价;价格换名的兄弟改成「少采样」(`family_key`)。
- **指引报告里「+1e-6 删掉后 7 例全部变好」没有证据** → 已更正,对应规则由封禁降为降权。
- 5 个算子的数值问题(float32 / 成交额量级)。

**同时做的口径改动**(用户已同意)
- 半衰期网格加 40 / 60(`partura/books.py`:`HALFLIVES = USER_HALFLIVES + (40, 60)`);落在 40 / 60 的行与用户原表不可比。
- 批量扫描里**变体的方向按训练段纯多头书定**(原式与基准仍按 rank IC 的符号;根是筛子的锁 +1)—— `scripts/sweep.py: score`,字段 `sign_by`。
- 已知族的判定逐候选实测(`scripts/batch_cluster.py: is_known` → `info[k].known_like`),聚类、融合、两份报告共用。
- 新算子:`cs_last_high10 / high05 / low10 / low05`(更细的筛子档位)。扩展库现在 49 个。

**服务器上正在跑**
- 第四轮(tag `s4`,screens `r4_F1xx`,4 个槽):15 条全部重跑(算子修正 + 新方向规则 + 新半衰期网格;假设表同第三轮)。日志 `logs/<fid>_round4.log`。
- screen `after_r4`(`tmp/after_round4.sh`):等第四轮结束 → `batch_cluster --tag s4` → `batch_fuse --tag s4`(融合的测试段读数,记账)→ 两个想法短搜重跑(tag `e3`:
  I2 用成对信息比的边际奖励;I1 当筛子、参照改成已做通用筛子的已知族)。进度看 `logs/_after_round4.log`。
- **跑完之后**:拉回 `runs/<fid>/*_s4.json`、`runs/_batch_B01/{cluster,fuse}_s4.json`、`./scripts/study.sh idea-pull`;
  `python scripts/motif_stats.py batches/B01_single_factors.yaml --tag s4`;`python scripts/readable_report.py … --tag s4`(先给 s4 的新成员补 `NOTES`);
  `python scripts/batch2_summary.py … --tag s4`;`python scripts/episode_report.py`;`python scripts/guidance_report.py guidance/B01.yaml --tag s4`;发给用户。

**想法短搜的三条结论**(实验卡 `episodes/e2_*/episode.md`;都是旧奖励口径,e3 会按新口径重跑其中两个)
- I2:离散度折叠在 2018–2021 给池子加 0.3~0.6 夏普,2022-01~2023-08 持平;旧奖励取两段较差者 → 全负。被否定的是奖励写法。
- I5:每臂 ~124 次评估,桶内口径下发现率 <1%,量不出先验的作用;要几千次评估。
- I1:带指引 41 个过线、对照 35 个,最好 +0.46 对 +0.45 —— 打平。已知族的多头书有垃圾尾巴,任何标出异常票的量都能剔掉一部分;筛子的参照必须是已做通用筛子的已知族。

**AlphaCube 改造**:实现工作流 `wf_a9e46c78-369` 续跑中(WP1 已提交 `1167f00`,在 `~/Desktop/AlphaCube-steering` 分支 `partura-steering`)。它结束后的事见下面 22:00 那段的「实现完成之后」。
注意:WP11(Partura 迁移)在 `~/Desktop/Partura-steering` 分支 `ac-plugin` 上做,它基于昨晚的提交;今天主分支上 `partura/ops_ext.py`、`scripts/idea_search.py` 改了很多,合并 `ac-plugin` 时以**主分支的行为为准**逐处合。

## ⏱⏱ 现状快照(2026-10-05 22:00 PDT;比下面 19:45 那一段新,先读这段)

**AlphaCube 改造:设计已定,正在实现**
- 设计工作流 `wf_8604f186-483` 已完成(12 个 agent 全部返回)。最终设计:`docs/alphacube_steering_design.md`(日频字段 = 新叶子类 `DailyFeature`,形状复用 COLLAPSED;
  生成器四个可选关键字 `op_weight / accept / daily_fields(+daily_leaf_prob) / leaf_slots` + `hook_rng`;打分器注册表 `register_scorer`,工厂能拿到 `dates / warmup`;
  插件加载 `--plugin` / `ALPHACUBE_PLUGINS` / `load_plugins`;`@op(..., real_valued=True)`;修 `mutate_window / mutate_constant` 与 `generate()` 回退绕过接受检查的漏洞;
  `run_mining` 只多一个参数 `daily_root`,其余走 `gp_params`)。基线测试:617 passed / 10 skipped / 1 xfailed(约 2 分钟)。11 个工作包(WP1–WP11,文件归属互不相交)。
- **实现工作流 `wf_a9e46c78-369`(2026-10-05 21:55 起,串行,一个包一个包做)**:Sonnet 5 实现并提交 → Opus 5 对着设计审查并写测试攻击 → 有缺陷则 Opus 5 修复 → 全部做完后
  三项整分支验证(默认行为与基线逐位相同 / 新能力端到端 / 整套测试与文档)。顺序:WP1, WP6, WP2, WP3, WP5, WP9, WP4, WP7, WP8, WP10(可选), WP11(Partura 迁移)。
  代码在 **git worktree** 里:`~/Desktop/AlphaCube-steering`(分支 `partura-steering`,基于 517fd09)、`~/Desktop/Partura-steering`(分支 `ac-plugin`)。每个包一条提交(标题以 `WPn:` 开头),
  所以断了也不丢;实现者会先看 git log,已有 `WPn:` 提交的包不重做。
  续跑:`Workflow({scriptPath: "…/workflows/scripts/alphacube-steering-implement-wf_a9e46c78-369.js", resumeFromRunId: "wf_a9e46c78-369", args: <handoff/workflows/impl_args.json 的内容>})`。
- **实现完成之后(总领做,不要让 agent 做)**:看三项验证的结论 → 把 `partura-steering` 并进 AlphaCube 的 `tradable-backtest` 和 `main`(用户的规矩:推了就并入 main)并 push →
  rsync `src/` 与 `scripts/build_daily_fields.py` 到服务器 `/root/autodl-tmp/AlphaCube/`(先确认服务器上没有别人的 AlphaCube 进程)→ 在服务器上跑建库脚本(数据放 `/root/autodl-tmp/AlphaCube/daily_fields/`)→
  合并 Partura 的 `ac-plugin` → 用正式钩子重跑一个想法短搜作验收 → 第四轮(带流通市值的假设)。

**审查工作流 `wf_b7c13476-92d` 仍在跑**(21:41 时已有 56 个 agent 返回;结果在 `handoff/workflows/wf_b7c13476-92d/`)。回来之后:修 `survived` 里的缺陷(先 high)、补测试、受影响的结果重跑。

**想法短搜(tag `e2`,修过奖励之后)的证据**(`episodes/e2_*/evidence.json`;两臂各预算 192,实际付费评估 100~170 个):
| 想法 | 奖励 | 带指引 | 对照 | 读法 |
|---|---|---|---|---|
| I2 日内离散度折叠 | `long_marginal`(与池子五五混合减池子,train / valid 取差的) | 0 个过线(≥0.2),最好 +0.02 | 0 个,最好 +0.10 | **这个奖励在这两段上谁也过不了**:valid(2022-01~2023-08)是已知族最强的一段(夏普约 4),任何东西五五掺进去都稀释它,取两段较差者就恒为负。合并段上独立因子对池子是 +0.3~+0.4 夏普(见 `cluster_s2` 的五五混合)。→ R3 与 R4 不能叠用:边际奖励要在合并段上量,或取两段增量的均值 |
| I5 不限结构、只换奖励 | `long_bucket`(可交易池 + 成交额桶内) | 0 个过线(≥1.0),最好 0.58 | 0 个,最好 0.29 | 192 的预算在桶内口径下谁也到不了 1.0;带指引的最好值高一倍,但样本太小,**不能说先验有效**。要么加预算,要么把过线标准降到 0.5 再比 |
| I1 冻结盘口当筛子 | `long_screen`(已知族排掉候选最高两成,减已知族) | **44 个过线(≥0.2),最好 +0.46** | (22:00 还在跑) | 这条通了。最好的是「10 分钟滚动方差为零的分钟占比,在同价位股票里排名」—— 把最小报价单位造成的假冻结(低价股零收益分钟天然多)扣掉了,是人没写过的写法 |
首跑(tag `e1`)的结论作废(奖励两边股票池不一致)。

## ⏱ 现状快照(2026-10-05 19:45 PDT;用户提醒额度将尽 —— 接手的人先读这一段)

**用户刚给的两句授权(原话)**:「你的需求我全部满足」「partura的权限等级比alphacube高」。总领的理解与安排:
(1) 数据层字段(流通市值 / 流通股本、涨跌幅限制宽度 / 板块)可以加;(2) 半衰期网格可以加 40 / 60;(3) 指引钩子可以并进 AlphaCube 本体;
(4) Partura 可以改 AlphaCube —— 在 `~/Desktop/AlphaCube` 开分支做、向后兼容(不传新参数时行为与随机数流不变)、测试通过后再同步到服务器的
`/root/autodl-tmp/AlphaCube/src`(2026-10-05 核对过:服务器 src 与本机 HEAD `517fd09` 逐字节相同;scripts/ 有两个 .sh 不同、tests/ 服务器缺几个文件)。
服务器上不是自己起的进程照旧不杀。

**所有 agent 的产出都在仓库里**:`handoff/workflows/<run_id>/`(每个 agent 的返回值一份 JSON + `journal.jsonl` 原件 + `INDEX.json`),
由 `scripts/wf_dump.py --loop 120` 每两分钟从会话目录抄一次(普通进程,不耗额度;重启命令:
`(nohup ~/.venvs/alphacube/bin/python scripts/wf_dump.py --loop 120 > logs/_wf_dump.log 2>&1 &)`)。每条因子的结论照旧在 `handoff/<fid>/`(recorder)。

**正在跑的两个工作流(被额度打断后原样续跑,做完的 agent 走缓存)**
| 工作流 | run id | 做什么 | 续跑 |
|---|---|---|---|
| partura-review-audit | `wf_b7c13476-92d` | 对抗式审查:6 个维度(奖励数学 / 匹配器与规则 / GP 钩子 / 成对统计 / 流水线与样本外纪律 / 筛子算子与可交易池)各一位 Opus 5 审查者 + 45 个扩展算子分 9 组由 Sonnet 5 写朴素参考实现逐元素对拍;每条发现再由 Opus 5 复现或推翻 | `Workflow({scriptPath: "…/workflows/scripts/partura-review-audit-wf_b7c13476-92d.js", resumeFromRunId: "wf_b7c13476-92d"})` |
| alphacube-steering-design | `wf_8604f186-483` | 5 位读者摸清 AlphaCube(表达式 / 引擎 / 挖掘 / 存储与数据 / 测试)→ 3 位架构师各出一份设计(日频字段进表达式 + 指引钩子进本体 + Partura 迁移)→ 3 位评审打分 → 综合成最终设计与工作包 | 同上,脚本 `alphacube-steering-design-wf_8604f186-483.js`,`resumeFromRunId: "wf_8604f186-483"` |
脚本都在 `~/.claude/projects/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/workflows/scripts/`。
**拿到结果之后**:审查 → 把 `survived` 里的缺陷逐条修掉(先 high),补测试,受影响的结果重跑;设计 → 总领过一遍 `final`,再起实现工作流
(在 AlphaCube 的 git worktree 里按工作包实现 → 跑测试 → 对抗式审查 → 合并 → 同步服务器 → 建日频字段库)。

**服务器上正在跑(screen)**
- `idea_I2_dispersion_fold`:想法 I2 的干预实验重跑(tag `e2`,奖励 `long_marginal`,两臂各 192);日志 `logs/_idea_I2_dispersion_fold.log`。
- `idea_I5`:想法 I5(只换奖励 `long_bucket`、不限结构 = 先验本身的检验)跑完接着跑 I1(当筛子,`long_screen`);日志 `logs/_idea_I5_within_bucket_anything.log`、`logs/_idea_I1_frozen_state.log`。
  结果用 `./scripts/study.sh idea-pull` 拉到 `episodes/e2_*/evidence.json`,`python scripts/guidance_report.py guidance/B01.yaml` 会把它们写进指引报告第四节。
  e1(首跑)的结论作废:对池子的边际奖励两边股票池不一致(已修:`RewardContext.pool_in_universe`),带指引的一臂把预算花在同一个种子的等价包裹上
  (已修:`steer.simplify` / `nonneg`、接受钩子按规范形去重、规则 D15~D17)。

**第三轮(tag `s3`)已全部完成**(15 条;修过 cross_ema 溢出、dist 门槛、筛子方向之后的重跑):`runs/<fid>/{sweep,anatomy,sweepfinal}_s3.json` 已拉回本机;
聚类 `runs/_batch_B01/cluster_s3.json`(24 簇;已知族簇首 `F114.h3_xfr_plus_state`;独立簇首 8 个)、融合 `runs/_batch_B01/fuse_s3.json`(测试段已读、记账)。
融合读数(成员各自平滑后等权;多头净超额 样本内 / 样本外,括号纯多头夏普):原式 15 条 +15.8 / +11.1(3.26 / 1.63);升级版 15 条 +20.4 / +15.9(3.53 / 1.63);
**独立 9 个 +20.1 / +15.7(3.99 / 1.88)**;已知族簇首单独 +19.4 / +13.8(3.51 / 1.87);独立 9 + 簇首 +21.0 / +15.9(3.95 / 1.88);一半一半 +21.2 / +15.5(3.75 / 1.81)。
和第二轮(独立 9 个 +20.1 / +17.3,3.95 / 1.93)在噪声内一致:第三批假设没有把样本外再往上推。
独立 9 个(s3):F101.fld_Volume_Amt、F102.h3_age_bucket、F103.nosc_B_cross_semistd_neg、F107.h3_blend_own2_ema30、F110.h3_cvx_xage、F111.h3_best2、F112.iso_E、F113.h3_g6_bdemean、F115.h3_raw_amt。

**还没做的(按顺序)**
1. 用 s3 重出给用户看的两份:`python scripts/readable_report.py batches/B01_single_factors.yaml --tag s3`(先给 s3 新成员在 `NOTES` 里补一句大白话说明)、
   `python scripts/batch2_summary.py … --tag s3`;`python scripts/motif_stats.py … --tag s3` 后重出指引报告。
2. 半衰期网格加 40 / 60(用户已同意):建议保留原网格的读数,另在最优半衰期顶到 20 时加算 40 / 60(`partura/books.py` 的 `HALFLIVES`、`scripts/sweep.py` 的 `score`)。等审查工作流结束再改这两个文件。
3. 新算子(5 位主研要):与方向无关的剔除 `cs_drop_high20 / low20`(置 NaN 而不是压到最底)、更细的档位 `cs_last_high10 / 05`。
4. F111 的对账没回来(断网);`handoff/TOOLING.md` 里「待修 / 待做」的各项。
5. 实现工作流(见上)→ 日频字段库 → 第四轮(带流通市值的假设)→ 最终总表与指引 v2。

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
