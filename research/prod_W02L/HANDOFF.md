# W02L 交接(接手先读这个，再读 PROGRESS.md 最上面一节)

更新于 2026-11-10 12:00 EST(服务器 11-11 01:00)。

## 现在在哪

- **第 0 步**(服务器自己在跑，不用管):已打分 3282 / 5583 条，错误 0,过闸门 2513;A 下 head 6 个,B 下 0 个。`bash scripts/w02l_status.sh`(服务器)看进度。
- **流**:已建 48 / 80 条;已结束 31 / 240 个流-轮;新 head 17 个(B 下 ≥ 0.5、|ρK| < 0.5),详见服务器 `research/prod_W02L/report.md`(本机有拷贝)。
- **GP 任务**:已推送的流-轮在服务器 `prod_conductor` 里排队 / 运行(3 路显卡，中位 27 分钟一次搜索)。服务器自己跑，不用管。

## 本机流水线里正在半路的(如果会话断了，按这个补)

| 轮 | 流 | 停在 | 补的办法 |
|---|---|---|---|
| — | — | 本机这边没有半路的(都已推送) | 直接 `bash scripts/w02l_pending.sh` 看新 READY 的 |

每个流拿到 `partura/s<流>/r<k>/corr_1.md` 以后:工作流 stage `audit`,然后 `prod_round.sh finish <k> "<流>"`。
工作流:`w02l-round.js`,args `{round: k, seeds: [数字, ...], stage: "pi" | "audit"}`,**seeds 要传数字**。PI 用 Sonnet 5.5,审计用 Haiku 5.5。
每批的 token 记到 `TOKENS.md`。

然后循环:`bash scripts/w02l_pending.sh` 列出新 READY 的流 → `prod_round.sh fetch` → PI → corr → audit → finish。
**fetch 必须先于派 PI**(11-10 漏过一次:PI 要么拒绝，要么只凭上一轮快照写计划;后者要删掉 missions.yaml 和 notebook 新加的一节再重派)。

## 第 0 步结束以后

1. `--spearman-only` 补算 30 条 `ts_spearman`,然后再跑一次 `w02l_stage0.py ... --rescore`(给这些行补 D 和新闸门);
2. 重跑 MAKEUP.md 里的搜索;
3. 建剩下 32 条流;
4. 全部轮次结束后建 W02L 库，按 PLAN §7:两层合成并集 vs C(L∪X),拟合到 2025-12-31,test 2026 只读一次并记账;
5. 写 RESULT.md。

## 用户 11-10 定下的四件事(都已实现，在跑)

1. **head 改按尺子 D 判。**D = B + 每天市值 / 流动性 / 价位十分位哑变量。
   - 第 0 步(`w02l_stage0.py`)新增 D 和 discovery_D。D 只对 B ≥ 0.2 的算(D_MIN):2792 条过闸门的里只有 5 条 B ≥ 0.2;服务器超载时 D 约 1 分钟一行。
   - 自动建流(`w02l_lib.py --head-ruler D`,默认)按 discovery_D 选 head;素材排序和证据里的分数仍是 B。
   - 一个批次要等它的行都补算完(`current()`)才建流，所以新流会等补算进程。
   - 报告(`w02l_report.py`)按 `research/prod_W02L/d_scores.jsonl` 判 head。
     - 这个文件由 `w02l_backtest.py --d-jsonl` 写;`w02l_report.py --collect-d <文件>` 列出还缺 D 的候选(B ≥ 0.3、|ρK| < 0.5)。
     - 11-10 在算 81 个,`tmp/bt_new/dscore.log`。
   - GP 搜索的奖励仍是 B(改奖励等于重跑)。
2. **同学的引擎加了 `--semantics alphacube` 开关**(克隆 `factor-compute-fast`,分支 claude/fast-batch,提交 1fcee88)。
   - `src/ac_reference` 是我们的 AlphaCube 加 Partura 算子;`unified_calculation_ac.run` 同一套输入输出。
   - 6 条逐位等于我们的引擎(含 L380、X2278),8365 条全能解析。默认仍是 fork。
3. **第 0 步和 GP 打分的闸门换成 `diagnose.levels_ok`。**
   - 规则：原来的「不同取值比例 ≥ 0.5」,或者每天 ≥ 20 个不同值且十分位分界上靠代码顺序进组的不超过 20%。
   - 加后一条的原因：组合大小固定，并列按代码顺序取，见 `alphacube.metrics.long_short_weights`。
   - 旧行用 `w02l_stage0.py ... --rescore --follow` 补算，写到 `stage0/rescore/`,原文件不动，读的时候以 rescore 为准。
   - 跟到第 0 步结束;`--spearman-only` 跑完后要再跑一次 `--rescore`。
   - 11-10 12:20 起 4 个补算进程在跑(PARTURA_THREADS=4,日志 `stage0/rescore_w*.log`)。
   - 正在跑的 6 个第 0 步进程是旧代码(没杀),它们新写的行由 `--follow` 补。
4. **Hurst 修正并回 AlphaCube**(本机 AlphaCube-steering 分支 partura-steering 提交 4639d9f,已同步到服务器 vendor;没推远端)。
   - `day_hurst`:首尾 NaN 修剪，中间有缺口或 inf 给 NaN。
   - `cross_hurst`:窗口必须完整。
   - `ALPHACUBE_LEGACY_HURST=1` 恢复旧行为。
   - Partura 面板缓存和 rankban 指纹缓存对用到这两个算子的表达式加了盐(`dt_day.semantics_salt`),不会再读到旧值。
   - 11-10 之前第 0 步对含 Hurst 的成员是旧语义打的分(day_hurst 148 条、cross_hurst 25 条)。

## 审计顺带发现、还没处理的(低优先级)

- `day_pdf_quantile_bilateral_half_width`:2025 r3 审计说它取的是窗口端点分钟的收益差，不是半极差(AlphaCube `operators/legacy_specialized_dt.py` 约 350–362 行)。所以 pdf 系的机制叙述不成立，值本身是确定的。没核实、没改。
- 种子解析器(`partura/steer.py` 的 tokenizer)不认带引号的参数(如 `'median'`、`'rank'`),PI 只能用默认的 `'prob'`(2025 r3)。
- `cs_quantile_q75 / q50` 输出的是逐股票的 0/1 旗子，不是市场标量(2032 r3 审计);有 PI 把它当「市场状态」写机制。

## 等用户定的

(暂无。)

## 规矩(用户定的，别破)

- 服务器上文件只能放在 `c02_partura` 和 `bkxehsw` 里。
- 不杀不是自己起的进程。
- 2026 test 只按预先写好的规则读一次。

## 另一件事：同学的因子引擎 factor-compute(用户 11-09 晚要求；代码已改完，11-10 04:10 已向用户汇报)

- 位置：他的仓库在服务器 `bkxehsw/programs/factor-compute`(hwja222 的，**不要在里面改、不要切分支**)。
- 我们的改动放在克隆里:`c02_partura/factor-compute-fast`,分支 `claude/fast-batch`,提交 5dcbdec。push 地址已设成 DISABLED,不推他的远端。
- 接口：和我们一致。输入是 名字→表达式 JSON,读同一种 store(qmt-v2-fast-factor-store-1),输出是 (天, 股票) float32 npy 加 meta。
- 能不能算我们的因子：
  - 他原版能解析库里 5583 条，但 Partura 计划里的式子 2782 条有 1491 条不行(缺 49 个插件算子和日频字段)。
  - 克隆里加了 `operators/partura_ext.py`(ops_ext 原样搬过来)、`alphacube/dailyfields.py` 和 adapter 的日频叶子，现在 **8365/8365 全部能解析**。
  - `run()` 端到端冒烟测试通过:4 条，带日频字段，结果 COMPLETE。
- 速度：服务器负载约 116 时测的，同一组 4 条库因子(L671 L310 L819 L1350),2024 上半年 117 天 × 5220 只股票。
  - 他原来的 `run()`:一次一条、3 只 × 20 天分块、1 线程，约 824 秒/条。
  - 改成批量 evaluate + 自动分块 + 16 线程，约 262 秒/条(3.1 倍)。
  - 再关掉 NaN/inf 计数，约 119 秒/条，合计约 7 倍。两种设置的数值逐位相同。
  - 72 条抽样上：克隆的批量跑法(计数开着)84 秒/条，我们自己的引擎 48 秒/条。
  - 显卡：GP 占满(只剩约 2 GB),没测。
- 数值：抽样 72 条，他的引擎(克隆) vs 我们的 AlphaCube。
  - 57 条一致或只有浮点尾差。
  - 2 条只在开头热身期不同(他那边窗口不满给 NaN)。
  - 剩下的差异来自他刻意加的「有限值策略 v1」(common.py 末尾):
    - 相关系数去掉了 +EPS,方差为 0 时给 NaN;
    - where / 比较的条件是 NaN 时结果给 NaN;
    - rank 不计无效值;
    - Hurst 只用连续段。
  - 差得最多的两条:L380(两条日内价格滚动极值的相关，截面秩相关 0.86)、X2278(对相关再做 signedpower 放大，0.52)。
  - 他的修正更严谨。但我们库里的因子是在我们的语义下挑出来的，换到他的引擎上个别因子会变。
- 探针脚本都在 `Partura/tmp/fc_probe/`:compare_probe / speed_probe / count_probe / smoke_run。
