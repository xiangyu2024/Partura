# F108_max_ntkurt_close — 交接状态

_自动生成于 2026-10-04 13:38(`python scripts/recorder.py --brief F108_max_ntkurt_close` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #3264(批次 B01_single_factors)
- 表达式:`day_max(pow_1_5(pow_2(nt_ts_kurt(Close, 30))))`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- 留出段:**还没读过**(只能读一次;读之前要在 `10_distilled.md` 里写下候选排序和判据)。
- agent `study:F108_max_ntkurt_close`(wf_759ef2d3-03f):失败,几乎没做事(不用看)
- agent `study:F108_max_ntkurt_close#2`(wf_759ef2d3-03f):失败,几乎没做事(不用看)
- agent `study:F108_max_ntkurt_close#3`(wf_759ef2d3-03f):失败,几乎没做事(不用看)
- agent `study:F108_max_ntkurt_close`(wf_08351f46-81b):中断,最后动作 10-04 13:10 → `handoff/F108_max_ntkurt_close/agents/study_a8fce7ad1c5d7e7c7.md`
- agent `work:F108_max_ntkurt_close#0`(wf_3cafb924-05e):已返回结果,最后动作 10-04 13:27 → `handoff/F108_max_ntkurt_close/agents/work_R0_acc5c7be5b1f0b5d1.md`
- agent `lead:F108_max_ntkurt_close#1`(wf_3cafb924-05e):失败,几乎没做事(不用看)
- agent `lead:F108_max_ntkurt_close#1`(wf_3cafb924-05e):失败,几乎没做事(不用看)
- agent `lead:F108_max_ntkurt_close#1`(wf_48864a04-f0a):还在跑(如果这就是你自己,不用看它的流水)

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F108_max_ntkurt_close` 看服务器上的 tag,`./scripts/study.sh digest F108_max_ntkurt_close <tag>` 重看结果)。

## 研究现状(`notes/F108_max_ntkurt_close/state.md`,10-04 12:54 更新)—— **先读这个文件**

# F108_max_ntkurt_close 研究现状(每次整个覆盖重写;接手先读这一页)

最后更新:x1_anatomy 已提交、结果还没读(第 1 次服务器运行)。

## 1. 一句话现状

源码读完、四个自写探针在服务器上自检通过、假设表定稿(`05_hypotheses.md`)、notes 01~05 已写;
第一个实验 `x1_anatomy`(exec,真实数据上的解剖)正在服务器上跑,**结果未读**。配置里还只有 `S0_baseline`,留出段未读。

## 2. 中间结果(已经量到的事实)

**S0 基线**(`runs/F108_max_ntkurt_close/S0_baseline.json`,`study.sh digest … S0_baseline`):
- 决策口径(方向/半衰期在 train 上定):方向 −;多头口径半衰期 20,多头腿净超额 train +0.3% / valid +2.5%,纯多头夏普 +0.05 / +0.46,
  多头腿毛超额 +3.9% / +6.2%,多头日换手 4.7%;多空口径半衰期 5,多空夏普 +2.83 / +2.53,空头腿毛超额(train)+48.3%。
- 用户口径(utrain 上定):多头口径半衰期 20,Lnet +1.0%,Lshp +0.15,Lgross +4.6%;多空口径半衰期 10,LS +2.82(复现了用户表的 2.82)。
- 固定半衰期(train,多头腿净超额):hl0 −57.4%(多头换手 85%)/ hl2 −13.1% / hl5 −4.1% / hl10 −0.9% / hl20 +0.3%。原始逐日面板几乎是噪声。
- 分位剖面(train,Q1 空头端 → Q10 多头端):−30.9 −14.8 −3.7 +2.5 +7.0 +8.1 +8.4 +10.3 +9.4 **+3.9**;valid:−30.9 −1.3 +2.8 +4.9 +6.1 +4.5 +4.3 +1.0 +2.4 +6.2。
  钱几乎全在空头端 Q1;多头端 Q10 在 train 上低于 Q5~Q9。
- 中性化(fit 段,交易信号):all_controls R² 0.311(原始面板 0.110),残差 rIC +0.0209(原 +0.0321),残差 Lgross +12.7%、short +11.6%。
  单个:ctl_cap R² 0.152,残差 Lgross +11.3% / Lnet +6.4% / short +28.5%;ctl_ivol R² 0.105,残差 short 只剩 +8.1%;ctl_dvol20 残差 short +4.5%;ctl_turnrate 残差 short +4.8%。
- 条件 IC:按 ctl_cap 五档 +0.035 +0.038 +0.040 +0.033 +0.021;按 ctl_amt 五档 +0.015 +0.022 +0.032 +0.047 +0.062(成交越活跃越有效;注意当天成交额对跳变是内生的)。
- 与控制变量的秩相关(交易信号,方向已对齐为「低 D 为正」):known_ivol_max9 −0.44,ctl_cap +0.38,ctl_ivol −0.31,ctl_dvol20 −0.30,ctl_turnrate −0.25,ctl_amt +0.14,
  ctl_price +0.10,known_stdamt_mean30 +0.08,known_stdamt_max9 +0.02。**与成交额水平家族几乎正交**。
- 逐年(多头腿净超额):2018 −4.1 / 2019 +5.8 / 2020 +4.7 / 2021 −5.4 / 2022 −0.3 / 2023 +7.0。衰减:rank IC h1 +0.032 → h20 +0.064(慢变量)。
- 已知家族自己当因子(train/valid 多头腿净超额):known_stdamt_mean30 +12.6% / +22.3%(hl 0),known_stdamt_max9 +13.7% / +22.2%(hl 5)。

**源码 + 探针**(`study.sh src …`、`studies/F108_max_ntkurt_close/probes.py`,服务器上 `decompose` 自检全部通过):
- `nt_ts_kurt(Close,30)`:窗口是**当天的 30 分钟**(NT 面逐日把(分钟×股票)切片递给 ND 内核,内核沿第 0 轴 = 分钟轴滚);左侧补 NaN,不跨日。
- 核是 `m4/(var²+EPS)−3`,服务器实测 EPS = 1e-09;var ≤ EPS 给 NaN。价格水平(元)上不是无量纲:两价位各半相差 1 tick 读 −2.6154(应为 −2),
  1 tick 毛刺读 −2.7119(应为 +25.03),1 元毛刺读 +25.0345。
- 残缺窗口:第 0 分钟 NaN,第 1 分钟(2 点)恒 −2,第 2 分钟(3 点)恒 −1.5。高斯游走上 53% 的「股票-日」全天最大 \|K\| 就是开盘两点窗。
- 跳变响应:水平跳变后新水平分钟数 1/2/3/4/5/6 → K = 25.03/10.07/5.11/2.65/1.20/0.25;只有头 3 分钟 > 3(27~29 分钟后有回声)。跳幅/噪声 = 3/5/10/20 → K 中位数 0.5/4.1/14.3/21.5。
- 整棵树在合成股票上(收益过程相同、只差价格水平):2 元 → fold-active 99%、中位 max\|K\| 2.71;5 元 75%;10 元 38%;20 元 25%;50 元 21%;200 元 16%、中位 3.49。
- `pow_2` 是偶函数(`e>1` 用普通幂),`pow_1_5` 只因为前面平方过才不出 NaN;合起来 = \|K\|³。`day_max` = nanmax。

## 3. 研究过程与逻辑

1. 接手时只有 S0。按手册顺序:digest / overview / decompose → 逐个算子读内核源码。
2. 读出来和名字不一样的四处(详见 `02_operators.md`):窗口是日内 30 分钟不是 30 日;开头残缺窗口有确定读数(−2、−1.5);
   峰度核带 EPS、在价格水平上有尺度;`pow_2` 是真折叠。由此树的真实形状是 `D = max(Kmax, −Kmin)³`,
   折叠只在全天 Kmax < 3 时起作用 —— 而那正是 D 最小的一段 = 多头端(`03_decomposition.md`)。
3. 为此写了四个探针(EPS 拐点 / 残缺窗口 / 跳变响应 / 整棵树按价格水平),每个带解析解自检。
4. 写假设表(H1~H13),再写 x1:先在真实数据上量「三段各占多少、多头十分位落在哪一段、空头腿有多少是买不进的票、
   朴素替身像不像、市值层内和已知家族多头池内的双重排序、显式日轴记忆与剔除式组合的预览」,然后才设计 S1。
   x1 的面板(Kmax、Kmin 等)会进共享缓存,S1 里复用不花钱。

## 4. 假设表

| # | 假设 | 状态 | 证据与出处 | 还差什么 |
|---|---|---|---|---|
| H1 | 按名字读:窗口是 30 个交易日 | 源码上已否定,待实测 | 内核 axis=0 + NT 面逐日切片;窗口池 [3..60] | x1 §0 的同构对照 |
| H2 | 折叠只在低尾起作用,而低尾就是多头端(多头端排序由 \|Kmin\| 伪影决定) | 未验证 | 公式上成立(`03`) | x1 §1/§3;S1 n_kmax / n_kmin |
| H3 | 立方 = EMA 下的日轴软极值 | 未验证 | — | S1 n_abs 固定半衰期表;x1 §9a |
| H4 | 信号在最极端窗口(事件)不在平均峰度 | 未验证 | — | S1 n_mean |
| H5 | 空头腿是已知暴露(波动/换手/彩票) | 部分支持 | S0 中性化:ivol/dvol20/turnrate 任一个都把 short 从 +30.6% 压到 +4~8% | x1 §6/§7 替身 |
| H6 | 量的是孤立跳变的信噪比 | 未验证 | 探针 jump_response | x1 §6/§7 zabs |
| H7 | 方向被丢掉了:上跳还是下跳 | 未验证 | — | x1 §6 zup/zdn;S2 |
| H8 | EPS/tick 伪影,按价格分层 | 合成数据支持,真实数据未验证 | 探针 tree_by_price_level | x1 §1–§2 |
| H9 | 多头腿弱是因为多头端 = 大市值 | 部分支持 | S0:cap 中性化后 Lgross +3.9% → +11.3% | x1 §8a |
| H10 | 空头腿被买不进的票抬高 | 未验证 | — | x1 §5 |
| H11 | 对纯多头的用处是「剔除器」叠在成交额水平家族上 | 未验证 | 与已知家族秩相关 ≈ 0 | x1 §8b/§9b;S3 |
| H12 | 窗口 30 不特殊 | 未验证 | — | S1 w_15 / w_60 |
| H13 | 字段不特殊;Ret 版退化成波动 | 未验证 | 公式(Ret 的 var² ≪ EPS) | S1 f_vwap / f_ret |

## 5. 当前的候选

还没有。唯一确定会进 S_final 的是:原式(新 id `f_orig`)和已知家族基准 `cross_mean(day_std(Amt), 30)`。
原式在多头口径下本身很弱(train/valid 多头腿净超额 +0.3% / +2.5%),这是所有候选要比过的第一条基准。

## 6. 后面的研究思路(服务器运行预算 8 次,已用 1 次)

1. **读 x1**(在跑)。看:① §0 窗口轴与折叠恒等式;② §1–§3 多头十分位是不是落在折叠段、按价格分层;③ §5 空头腿的买不进占比;
   ④ §6/§7 替身(zabs/zup/zdn/jmax/rkurt/ckurt)像不像;⑤ §8/§9 剔除式组合有没有戏。
2. **S1_nodes**(run):节点必要性。计划变体:`n_kmax = day_max(K)`(不折叠)、`n_kmin = day_min(K)`(只留伪影段)、
   `n_abs = day_max(abs_(K))`(去立方)、`n_mean = day_mean(pow_2(K))` 或 `day_mean(K)`、`w_15` / `w_60`、`f_vwap`、`f_ret`。
   NT 面变体每个约 4 分钟(显卡被邻居占着,走 CPU),一个阶段不超过 6 个新的 NT 变体(n_kmax / n_kmin 已在 x1 里算过)。
3. **S2_mechanism**(run):DT 面的便宜替身与方向拆分(滚动 z 分数的上跳/下跳)、显式日轴记忆(`cross_max` / `cross_mean` 套在日频读数外面)。
   如果某个替身与原式交易信号秩相关 > 0.8 且多头腿不输,它就是提纯结果(便宜、无 NT 面、无 EPS 伪影)。
4. **S3_longonly**(run):对纯多头的用法 —— 与已知家族的秩和 / 剔除式组合,和已知家族单独在**同一半衰期**下比;残差的多头腿。
5. **S_final**:≤ 5 个,含 `f_orig` 和已知家族基准。读之前把排序和判据写进 `10_distilled.md`。
- 明确不做:不为多空夏普优化(用户做不了空头);不在 valid 上重新拟合方向/半衰期;不做「再试一批相近窗口/指数」式的搜索。

## 7. 留出段

**未读**。`runs/F108_max_ntkurt_close/ledger.json` 里只有 train / valid / utrain 的记录。读前登记要写在 `10_distilled.md`(还没写)。

## 8. 给接手者的提醒

- 服务器上 `x1_anatomy` 可能还在跑或刚跑完:`./scripts/study.sh wait F108_max_ntkurt_close x1_anatomy`,日志在 `logs/F108_max_ntkurt_close_x1_anatomy.log`。
  脚本每一节都包了 try/except,某一节失败不影响别的节。
- 显卡被邻居占满(29.5/32 GiB),Partura 自动走 CPU:NT 面表达式约 4 分钟一条,还要排 3 个运行槽位(这次排了 495 秒)。
- 本机 `~/Desktop/AlphaCube` 是另一个 commit,但 `nankurt_last`、NT 面逐日调用这两处与服务器源码一致(服务器源码用 `study.sh src` 看过,EPS 用探针在服务器上实测过)。
- 本机可以用随机数据干跑脚本:`scratchpad/fake_study.py`(临时目录,不在项目里)只是个形状检查器,丢了重写即可。
- `in_delta(Close, 1)` 这类不在窗口池里的窗口没试过能不能解析,x1 里没用它。
- 数据从 20180102 开始、没有预热行(`+0 warm-up`),日轴滚动算子在最初几十行是残缺窗口。

## 研究日志(`notes/F108_max_ntkurt_close/journal.md`:3 条,其中研究员自己写的 2 条)

最近的 12 条(完整的看文件):

### 2026-10-04 12:54 读完源码:窗口是日内 30 分钟不是 30 日;峰度核带 EPS;折叠只作用在多头端。假设表定稿,x1 已提交

看到了什么(源码 + 服务器探针,无数据实验):
- nt_ts_kurt(Close,30) 滚的是当天的分钟轴(NT 面逐日把 分钟×股票 切片递给 ND 内核),不跨日;左侧补 NaN,第 1 分钟两点窗恒读 -2,第 2 分钟恒读 -1.5。
- 核 = m4/(var^2+EPS)-3,服务器实测 EPS=1e-09;价格水平(元)上不是无量纲:1 tick 毛刺读 -2.7119(无量纲应为 +25.03),1 元毛刺读 +25.03。
- pow_2 是偶函数、pow_1_5 在它后面才合法:D = max(Kmax, -Kmin)^3;-Kmin < 3 <= 25,所以折叠只在全天 Kmax<3 时起作用 = D 最小的一段 = 多头端。
- 合成股票(同收益过程、不同价格):2 元 fold-active 99%,200 元 16%。
判断:H1(按名字读成 30 日)在源码上已否定,待 x1 §0 实测;H2/H8(多头端由伪影排序、按价格分层)成为主线。
S0 基线:多头口径 hl20 Lnet +0.3%/+2.5%,LS(hl5)+2.83/+2.53,剖面 Q1 -30.9% 其余平、Q10 低于 Q8-Q9。预期:内容主要在空头端。
下一步:读 x1(真实数据上三段占比、十分位画像、买不进占比、替身、双重排序、剔除式组合预览),再定 S1。
不做:不为多空夏普优化;不在 valid 上重拟合方向/半衰期。

### 2026-10-04 13:26 [执行] R0 建档完成:核对 01~05(完整未改),新建 06_baseline.md,02/03 各补一小节;发现发布值 Lnet+5.6% 对不上

看到了什么:
- brief/digest(S0_baseline)/overview_for.py/decompose 复核了一遍,01~05 已有内容与服务器实测一致,没有需要重写的地方。
- 新建 06_baseline.md:S0 头条数字(hlL20 多头腿净超额 train+0.3%/valid+2.5%,hlS5 多空夏普 train+2.83/valid+2.53)、
  分位剖面(train/valid 两段都不单调,Q10 低于 Q5~Q9)、逐年、衰减、10 个控制变量的中性化表、rank 相关都落了表。
- 02_operators.md/03_decomposition.md 各补一小节:齐次度(nt_ts_kurt None,pow_2 2.0,pow_1_5 1.5,day_max 1.0)、
  输出类型(四个都是连续值,没有布尔/档位)、有没有用到未来数据(没有)、恒等节点(没有)、重复子树(没有)。

异常(写进 results/R0.md,没有下结论,留给主研判断):
- 用户发布值 Lnet(训练)+5.6% 对不上:utrain 口径 hlL=20 读 +1.0%,train 段固定半衰期表 hl=10 读 -0.9%,
  两个都不是同一半衰期同一数据段的严格对照,没找到"utrain+固定hl10"的直接读数去坐实。LS(2.82)对上了。
- digest 的"中性化"表实际用的是 hlL=20 信号(不是标题看起来像的多空口径);同一"未中性化"状态下 LTO 读 5.2%,
  头条数字读 4.7%,两个数字不一致,来源没查。
- digest(hlL=20 信号)与 overview_for.py(发布半衰期10信号)给出两套不同的 all_controls R²(0.311 vs 0.289)和
  rank 相关列表,口径不同不能混用,已在 06_baseline.md 分节标注。

下一步(留给主研):读 x1_anatomy 结果、判断 H1~H13 状态;决定要不要补一次 utrain+固定hl10 的读数去核实发布值差异。
不做:没有碰 state.md(按分工是主研的文件);没有读 x1_anatomy 结果;没有动 01/04/05 已有内容、没有动 orders/ 之外的任何文件。

### 2026-10-04 13:29 [auto] x1_anatomy 跑完(exit 97);重看结果:logs/F108_max_ntkurt_close_x1_anatomy.log

## 工单与结果卡(`notes/F108_max_ntkurt_close/orders/`、`notes/F108_max_ntkurt_close/results/`)

- R0:工单 —,结果卡 有

## 配置里的实验计划(`configs/F108_max_ntkurt_close.yaml`)

- 标题:(读完这棵树之后,用一句话写它是什么)
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F108_max_ntkurt_close`)

- `S0_baseline`  10-04 11:50  1 个变体  → `./scripts/study.sh digest F108_max_ntkurt_close S0_baseline`
- `x1_anatomy`(自写脚本的输出)  10-04 13:13  exit 97  → `logs/F108_max_ntkurt_close_x1_anatomy.log`

## 已写的 notes(`notes/F108_max_ntkurt_close/`)

- `01_expression.md`  1293 字节  10-04 13:04
- `02_operators.md`  5542 字节  10-04 13:24
- `03_decomposition.md`  4780 字节  10-04 13:25
- `04_grammar.md`  2420 字节  10-04 12:34
- `05_hypotheses.md`  5958 字节  10-04 12:23
- `06_baseline.md`  9595 字节  10-04 13:24
- `journal.md`  3659 字节  10-04 13:29
- `state.md`  9521 字节  10-04 12:54

## 自写的探针与分析脚本(`studies/F108_max_ntkurt_close/`)

- `probes.py`  10-04 12:16  Probes this tree needs:  day_max(pow_1_5(pow_2(nt_ts_kurt(Close, 30)))).
- `x1_anatomy.py`  10-04 12:21  x1 -- anatomy of  day_max(pow_1_5(pow_2(nt_ts_kurt(Close, 30))))  on real data.

## 结构化结果(`handoff/F108_max_ntkurt_close/results/`)

(还没有)
