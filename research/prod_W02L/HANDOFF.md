# W02L 交接(接手先读这个，再读 PROGRESS.md 最上面一节)

更新于 2026-11-12 21:20 EST(服务器 11-13 10:20)。

## 现在在哪

- **轮次:** 240 / 240 计划已推送;已结束 239,最后一个 2080 r3 在服务器上搜索。80 条流全部建好。
- **新 head(尺子 D ≥ 0.5、|ρK| < 0.5):** 208 个(不重复表达式),D 打分到第 11 批(`d_scores.jsonl` 641 行)。最好 2034 r3 b +1.44、2029 +1.26;
  11-12 晚新出一族 2079 r3(上一分钟成交额领先下一分钟收益的日内相关)D +1.07。详见 `report.md`。
- **第 0 步 ts_spearman 补算:** 9 / 22。6 个 CPU 进程在跑(慢);`tmp/sp_restart2.sh`(本机 `scripts/server/w02l_sp_restart2.sh`)在 2080 r3 推送后、
  GP ≤ 2 个时起一个 GPU 补算进程(`PARTURA_GPU_LOCK=gpus0`,`--steal-min 30`,日志 `stage0/sp_g3.log`)。22 块全有输出后停 CPU 进程，再跑一次 `--rescore`。
- **进度看板:** https://claude.ai/artifact/D9UG9RbFhTRC53HkQhV1WB;`scripts/w02l_progress.py`(服务器)+ `scripts/w02l_progress_fetch.sh`(本机)。

## 剩下的步骤(按顺序)

1. 等 2080 r3 结束(240/240),跑最后一批尺子 D(`w02l_report.py --collect-d` → `w02l_backtest.py --d-jsonl`),更新 report。
2. ts_spearman 补完 → `w02l_stage0.py ... --rescore`。
3. **补跑**(用户定：全部轮次结束后再跑，不和正常轮次重叠):`source tmp/w02l_env.sh; nohup bash scripts/server/w02l_makeup.sh research/prod_W02L/makeup_list.txt &`
   (37 个 GP 位 / 33 轮;做法见 MAKEUP.md 顶部)。再补评 MAKEUP.md 里的 2 个 R 组。补跑产出照常算 D。
4. 建 W02L 库 + PLAN §7 判读：两层合成 C(L∪X∪W02L) vs C(L∪X),拟合到 2025-12-31,2026 test 只读一次并记账(`ledger_prod.json`)。
   参考 W01 的 `scripts/prod_two_level.py`(build / read / overlay)。建库时的检查清单见 PROGRESS(34 条坏 in_regres、day_pdf_quantile_single(left=False)、
   2048 r2 a 的市值非线性、饱和的 day_product head、近重复去重 |ρ| ≥ 0.7)。
5. 写 RESULT.md。

## 本机流水线里正在半路的

| 轮 | 流 | 停在 | 补的办法 |
|---|---|---|---|
| — | — | 没有(240 轮都已推送) | — |

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
- `day_pdf_quantile_single(..., left=False)`:右尾分支对降序的累计量做 `searchsorted`(AlphaCube `operators/legacy_specialized_dt.py` 305–307 行)。11-10 本机核实：输出退化成当日第一或最后一分钟的值(n=0.05 时取最后一分钟，n≥0.5 时多半取第一分钟)。2061 r1 审计发现。没改(改了会变语义);库里含 `False` 的成员要单独核对。
- `in_regres(Ret, in_mean_full(Ret), 20)`:因变量当天是常数，残差恒为 0(本机实测约 1e-12),标准化以后只剩浮点噪声。库里有 34 条(全是这个写法);11-10 已算 D 的候选里没有它们。已写进 rules.md §4,PI 和审计员都会看到。**建库(PLAN §7)时要把这 34 条标成定义坏掉**;另外要查冠军合成有没有用到它们。2062 r1 审计发现。
- **前视算子** `cross_shift` / `ts_shift` / `in_local_mean`(2041 r2 审计发现，总领核实:`cross_shift(x,1)` 取的是第二天的值)。GP 本来就会丢掉含这些算子的种子(`gp.py` 的 `contains_lookahead`),所以搜索没泄漏;D-head 里一条都没有。受影响的轮次:2041 r2 位 b(审计已判普通 GP)、2052 r2 两个位(14/14、10/12 是前视种子)、2053 r1 两个位(8/10、9/9),后两者实际上大半是普通 GP;2052 r2 的 R 里有 `in_local_mean` 变体被打了分(都是负分，没进 head 和报告)。11-11 起 `c06_check.py` 在草稿检查时直接判不合格,finalize 时把它们当划掉处理(种子和 R 变体都去掉)。

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
