# 一次研究的操作手册(给做研究的 agent)

先读 `CLAUDE.md` 和 `docs/method.md`(为什么每条表达式都要重新推计划)。这份讲**怎么干**:
口径、工具、规矩、踩过的坑、要交什么。范例是 `research/alpha_distillation/F001_dwgated_covamtlow.md`
和 `notes/F001_dwgated_covamtlow/` —— 看它的**论证方式**(每个结论后面跟着哪个实验),不要抄它的实验清单。

---

## 0. 目标:提纯、分辨、升华

| | 要回答的问题 | 算做到了 |
|---|---|---|
| **分辨** | 这东西到底是什么?是不是某个已知暴露(成交额水平、规模、换手率、波动、动量、反转)换了个写法?和这批其他因子、和已知家族是不是同一个? | 有中性化的 R² 和残差表现、有 rank 相关、有"把可疑节点换成它的朴素等价物"的直接替换实验 |
| **提纯** | 预测力在树的哪一部分?哪些节点、指数、窗口、字段是多余的? | 给出一个**更小**的结构,在 train 和 valid 上保住(或超过)原式;每删一个节点都有实验 |
| **升华** | 看懂机制之后,能不能写出一个**更好用**的版本? | 见下面的"好用" |

**"好用"的口径**(用户的真实目标是 A 股纯多头,空头腿做不了):

1. **多头腿**:纯多头夏普、多头腿**净**超额(扣 15 bp 之后)。用户表里公布的"多头腿年化超额"是**毛**的;
   这批因子的多空差价普遍七八成来自空头腿,很多因子毛超额 +10% 而净超额只有一半甚至为负。
   一个把多头腿净超额从 +3% 做到 +8% 的版本,比一个把多空夏普从 3.5 做到 4.0 的版本有用得多。
2. 多空夏普(扣费)。
3. 换手、简单程度、邻域稳定性(窗口/指数换一档不塌)。
4. **必须过用户的两道门槛**:`cov`(有标签的格子里因子有值的比例)≥ 0.95,`dist`(取值离散度)≥ 0.5。
   过不了门槛的候选不能当结论(档位太少的因子,十分位书靠股票代码顺序破平局)。

三件事不一定都能做成。**"它 80% 是成交额水平,提纯后就是 `cross_max(day_sum(Amt), 9)`,没有升华空间"
是一个完全合格的结论**,只要证据在。不要为了有个"升华版"去凑。

---

## 1. 口径(和用户的 `pick_single_factors.py` 逐位一致,已复现过 15 行)

- **标签**:`open_vwap15` h=1 **可买入版** —— t 日收盘后决策,t+1 开盘 15 分钟 VWAP 买入,t+2 同一价卖出;
  t+1 开盘封涨停买不进的票标签是 NaN(放在多头里当天记 0,放在空头里也记 0 —— 这会抬高空头腿)。
- **数据段**:`train` 20180102–20211231、`valid` 20220101–20230807、`utrain` = 两者之和 = **用户的训练段**、
  `holdout` 20230808–20251231 = **用户的测试段**。
- **方向**:rank IC 的符号。**半衰期**:因果 EMA,在 {0,1,2,3,5,10,20} 里按扣费多空夏普选(`rank_by: ls`)。
  两者都只在 fit 段上定一次,然后原样用到别的段。
- **两本书**:前/后 10% 等权多空(gross 1),每单位换手 15 bp;多头腿当成一本纯多头书,减去当天
  有信号有标签的票的等权收益。
- **两套数字,别混**:
  - *决策口径*:方向/半衰期在 `train` 上定,`valid` 是没见过的。**挑变体只看这套。**
  - *用户口径*:方向/半衰期在 `utrain` 上定,对应用户表的"训练"列;`holdout` 对应"测试"列,**只在最后读一次**。

- **中性化的对象是实际交易的信号**(方向 × 面板、按选定半衰期平滑之后),不是原始日频面板。
  很多因子原始面板逐日抖得厉害(十分位书日换手 80%+、夏普为负),平滑后才值钱;在原始面板上控制变量
  只张成几个百分点,在平滑后的信号上可以张成一大半。两种 R² 都会打印,差得多本身就是一条信息。

`study.sh digest` 打印的列:`rIC`=rank IC,`hl`=半衰期,`LS`=扣费多空夏普,`Lgross/Lnet`=多头腿毛/净年化超额,
`Lshr`=多头腿占毛价差的比例,`TO`=多空日换手,`cov`/`dist`=两道门槛。

---

## 2. 工具:全部通过 `scripts/study.sh`(在 `~/Desktop/Partura` 下跑)

服务器上的 AlphaCube 才是算子实现的**唯一事实来源**(本机那份是另一个 commit,还有别人没提交的改动)。

```bash
cd ~/Desktop/Partura
./scripts/study.sh ops '^cross_'                 # 有哪些算子(名字、面/族/类、可用窗口)
./scripts/study.sh src day_skew cs_demean        # 内核源码 —— 每个用到的算子都要读,不要按名字猜
./scripts/study.sh decompose <fid>               # 算子档案(探针实测)+ SSA 分解 + 实验室里的相关先验
./scripts/study.sh propose <fid>                 # 从这棵树派生的候选实验 —— 草稿,要删改
./scripts/study.sh check <fid>                   # 配置里每条表达式能不能解析、是不是合法的根。run 之前必跑
./scripts/study.sh run <fid> <tag> <stage...>    # 起一个阶段(立刻返回);tag 是输出文件名
./scripts/study.sh wait <fid> <tag>              # 等它(最多 540 秒,没完就再调一次);完了自动拉回并打印摘要
./scripts/study.sh digest <fid> <tag> [base_id]  # 重看某次的摘要
./scripts/study.sh exec <fid> <tag> <script.py>  # 跑 studies/<fid>/<script.py>(自己写的分析),同样用 wait 等
./scripts/study.sh final <fid> <tag> <stage>     # 读留出段的那一次(整个研究只许一次)
./scripts/study.sh report <fid>                  # 推 notes、在服务器上拼报告、拉回 research/alpha_distillation/<fid>.md
./scripts/study.sh status                        # 服务器上现在有哪些 Partura 任务
```

- `wait` 要给 Bash 工具设 `timeout: 600000`。排队是正常的:服务器同时最多 3 个 Partura 进程,GPU 上的求值一次只跑一个。
  等的时候去写 notes、想下一个阶段,不要空等。
- 一个阶段的耗时 ≈ 排队 + 新表达式求值(普通日频/日内折叠算子几秒一条;**NT 面(`nt_*`)和手写库的 `in_*` 重算子
  几十秒到几分钟一条**)+ 每个变体约 20 秒的指标。**一个阶段不超过 12 个变体**(重算子不超过 8 个)。
- 面板按表达式内容缓存、所有研究共享:重复的子树、控制变量、别的研究算过的东西都不花钱。

### 自己写分析:`studies/<fid>/*.py`

没有现成诊断能回答的问题,就写脚本(这才是"每条表达式都不一样"的落点):

```python
import numpy as np
from partura.study_tools import Study, bk, dg
with Study("<fid>") as st:                       # 自带排队、内存守卫、共享缓存
    p = st.panels({"x": "day_skew(Low)"})["x"]   # (天, 股票) float32
    cap = st.control("ctl_cap")                  # 配置里的控制变量 / 已知家族,按名字取
    tgt, tr, va = st.target(), st.slice("train"), st.slice("valid")
    print(st.books(p, fit="train", evals=("train", "valid"))["splits"])   # 和表里同口径的两本书
    print(st.ic(p, "valid"))
```

`st.slice("holdout")` 会直接报错 —— 留出段不从分析脚本里读。脚本里用 `print` 输出,`wait` 会把日志尾部打出来。

### 自己写探针:`studies/<fid>/probes.py`

见 `docs/method.md` §3 和 `studies/F002_crosscov_highvar/probes.py`。在配置里加 `probes: [studies/<fid>/probes.py]`,
`decompose` 和报告会自动带上。**先在已知答案的算子上自检,再拿去读未知算子。**

---

## 3. 配置文件 `configs/<fid>.yaml`

骨架已经生成(S0_baseline 已跑完,结果在 `runs/<fid>/S0_baseline.json`)。你要做的是往后加阶段:

```yaml
stages:
  - id: S1_xxx
    question: "这一组实验在回答哪一个问题?(一句可证伪的话)"
    variants:
      - {id: a_no_abs, group: ablate, expr: "cs_demean(day_skew(Low))", why: "去掉 abs:如果预测力来自偏度的幅度而不是方向,这个应该塌"}
```

- 变体 id 全研究唯一。`why` 必须写它想证伪什么。
- `diagnostics:` 里的 `neutralise / profile / decay / by_year` 列变体 id;`conditional:` 列 `{factor, gate, buckets}`
  (gate 可以是控制变量名或 gates 里的名字)。想对别的变体做中性化就把 id 加进去。
- `controls:` / `gates:` 可以按这棵树的嫌疑**增加**(比如怀疑它是涨跌停效应,就加一个涨跌停相关的控制);
  共享的那几个别删,`corr_with` 里列的面板会和变体一起进 rank 相关矩阵。
- 留出段那一次:单独建一个阶段(通常叫 `S_final`),放 **≤ 5 个**最终候选(必须含原式,变体写 `final: true`),
  用 `study.sh final` 跑。**候选必须在读留出段之前、只凭 train/valid 的数字选定,并把理由写进 notes。**

### 表达式语言的坑(都踩过)

- 常数是"铺满分钟轴的退化值":`sub(x, 1)` 的结果喂给 ND 面算子(`ts_*`、`cs_*`)会在引擎里报错。
  要收益率就用毛比值 `div(a, b)`(秩等价),或者把常数运算放在最外层。
- 根必须是"每股票-日一个值"且不是布尔。分钟级的中间量要先 `day_*` 折叠。
- `cross_*` 滚的是**交易日**轴(不是截面);`cs_*` 才是截面;`nt_*` 是逐分钟的截面/日轴;`in_*` 是日内分钟轴。
- 保序的外层一元变换(`pow_3`、`cs_rank`、`sigmoid`…)单独作用时对 rank IC 和十分位书**毫无影响**
  (F001 的结论,`decompose` 输出末尾的实验室先验里有)—— 别把它当成一个"变体"来试。
- 手写库的通用调用带字面量参数(`in_slice(x, 2, 237)`、`day_quantile(x, 0.95)`),签名看 `src`。

---

## 4. 硬规矩

1. **只动自己的文件**:`configs/<fid>.yaml`、`studies/<fid>/`、`notes/<fid>/`。不改 `partura/`、`scripts/`、
   `lab/findings.yaml`、别的因子的任何文件。工具有问题就绕过去,并在最后的汇报里写清楚。
2. **服务器上不是只有你**。不用 `--cpu-fallback`、不调大显存占比、不杀任何不是你起的进程、
   不碰 `/root/autodl-tmp/AlphaCube`(只读)。除了 `study.sh` 之外不要自己 ssh 上去跑计算。
3. **留出段只读一次**,而且只通过 `study.sh final`。读之前候选已经定死;读之后不许再改候选、不许再跑新的 final。
   留出段的数字不好看,就照实写 —— 那正是它的用处。
4. **方向与半衰期不重新拟合**:报告里任何 valid / holdout 的数字,都必须是 fit 段定好的方向和半衰期。
5. **每个结论都要能指到一个实验**。"这像是流动性溢价"不是结论;"对 ctl_amt 中性化后 rank IC 掉了 56%"才是。
   分清三档:已确立的证据 / 合理但没坐实的解读 / 未决。
6. **不凑数**。不要因为某个变体在 valid 上高了 0.1 就宣布它更好:看 train 和 valid 是否同向、
   邻域是否稳、多头腿是否也跟着变好。这批因子的测试段噪声大约是多空夏普 ±0.3。
7. 实验要有理由:一个阶段回答一个问题,全研究的服务器运行控制在 **8 次以内**(含 final)。

---

## 5. 要交的东西

`notes/<fid>/` 下的手写段落(中文,英文术语保留;写法看 F001 的 notes):

| 文件 | 内容 |
|---|---|
| `01_expression.md` | 这条因子的来历、一句话说它是什么 |
| `02_operators.md` | (可选)读源码时发现的、探针表里看不出来的事 |
| `03_decomposition.md` | 分解表之外需要说明的:关键公式、容易被名字骗的地方 |
| `04_grammar.md` | 结构语法:事件 → 记忆 → 门控 → 放大… |
| `05_hypotheses.md` | 竞争性假设表:每条写"预测什么""哪个实验能杀死它"。**在跑实验之前写** |
| `06_baseline.md` | 基线读法:钱在多头腿还是空头腿、分位剖面是不是单调、逐年、衰减 |
| `07_<stage_id>.md` | 每个阶段的结论(问题 → 结果 → 解读),文件名里的 stage_id 要和配置一致 |
| `07_neutralise.md` / `07_conditional.md` / `07_controls.md` | 对应诊断表的解读 |
| `07x_<name>.md` | 自己写的分析(studies/ 下脚本)的结果与解读 |
| `08_variants.md` | 怎么读总表、哪些变体其实是同一个东西 |
| `09_diagnosis.md` | 机制诊断:已确立 / 合理但未坐实 / 未决 |
| `10_distilled.md` | 提纯与升华的结果、为什么比原式好(或为什么没有更好的)、留出段表的解读 |
| `11_risks.md` | 失效模式:泄漏、过拟合、尺度污染、已知暴露、容量、成本、制度依赖 |
| `12_next.md` | 只列能显著降低不确定性的下一步 |

最后 `./scripts/study.sh report <fid>`,并**把生成的报告从头读一遍**:表里有没有空的、notes 里引的数字和表对不对得上。
