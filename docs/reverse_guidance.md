# 反向指引 AlphaCube —— Partura 的定位与回路

## 定位(2026-10-05 用户改定)

Partura **不是** AlphaCube 的下游。

> AlphaCube 负责高熵、可扩展的经验发现;Partura 负责从成功与失败的实验里形成并更新研究信念,
> 再反过来改变 AlphaCube 的搜索策略;组合、风险与执行把发现变成可部署的收益。
> —— `AlphaCube × Partura Research Roadmap` §9

所以 Partura 的产出不只是「这条因子的升级版」,而是**对搜索的干预**,以及干预有没有用的证据。
要验证的不是「Partura 改出了更好的因子」,而是「随着研究一轮轮做下去,单位算力在没碰过的样本上的发现效率有没有提高」。

```
AlphaCube(GP / RL 搜索) ──表达式、轨迹、失败品──▶ Partura(批量扫描 · 市场解剖 · 综合 · 对账)
        ▲                                                        │
        └── 反向指引:奖励 · 评估 · 动作与子结构的先验 · 交给搜索的想法 ◀──┘
                      (每一次干预配一个同预算的对照搜索)
```

## 四类干预,和它们在仓库里的位置

| 干预 | 写在哪 | 怎么生效 |
|---|---|---|
| 奖励函数 | `guidance/<batch>.yaml` → `reward` | `partura/steer.py: reward()`(`long` / `long_tradable` / `long_bucket` / `long_marginal` / `long_screen`),运行时作为打分器装进 AlphaCube(`make_scorer`);排序在 GPU 上算的同值实现在 `partura/steer_fast.py`(`PARTURA_REWARD_DEVICE=cuda`) |
| 评估方法 | 同上 → `evaluation` | 门槛先行、方向按多头腿、半衰期按纯多头书、两段取差的那一段,都在同一个 `reward()` 里;同一笔钱检验、解剖在 `scripts/sweep*.py` / `anatomy.py` / `batch_cluster.py` |
| **动作 / 子结构的先验**(重点) | 同上 → `priors` | `partura/steer.py: Guidance` —— 改写(打分前化简、去重)、封禁、降权、升权。对生成器的作用方式是**接受-拒绝**:任何提议分布 P 经过它就变成 P × 权重,不要求生成器自己支持算子概率 |
| 交给搜索的想法 | 同上 → `ideas` | `scripts/idea_search.py <idea>`:种子进首代、想法里的算子多采样、候选必须留在想法的邻域里;同预算对照组 |

规则的证据有两种来源,都写在每条规则的 `evidence` 里:
- `lab/findings.yaml` 的结论(单条因子研究里实测出来、写明了失效条件的);
- `guidance/motif_stats_<tag>.json`(`scripts/motif_stats.py`):批量扫描里**成对**的统计 —— 同一个动作套在 15 条因子上,
  变体减它自己的底座。这是「动作价值」的直接估计:哪些外层动作有益、哪些是乘客、哪些把多头腿毁掉。

证据的范围是这一批种子的邻域,所以权重是**先验**;每一次干预实验去更新它。

## 规则怎么写

pattern 就是表达式,外加几个通配:

```
_            任意子树                 _1 _2 …     任意子树,同名处必须是同一棵
$w           任意数字                 {a|b|c}     这几个算子 / 叶子名之一
@price @flow @any                     该类叶子(Close/Open/High/Low/Vwap;Amt/Volume)
root: …                               只匹配最外层(默认匹配树里任何位置)
```

```yaml
- {id: B1_root_zscore_own_history, action: ban,     pattern: "root: {cross_zscore|ts_zscore}(_, $w)", why: …, evidence: [wrappers.mem_zscore]}
- {id: D7_ratio_with_soft_denominator, action: weight, w: 0.5, pattern: "div(_, _)", …}
- {id: C1_window1_identity, action: rewrite, pattern: "{ts_min|ts_max}(_, 1)", to: operand, …}
```

`Guidance.canonical(expr)` 做改写;`dedup_key` = 改写后的式子(**只并精确等价的**);
`family_key` 再把「只差价格字段换名」和「只在最外层多套一个保序函数(`pow_05(X)` 对 `X`)」的认作同族 —— 同族的少采样(0.3),不拒绝;
`weight(expr)` 是命中的规则权重之积(封禁为 0);`accept(expr, u)` 以 min(1, 权重 / 最大权重) 的概率放行。
匹配器读的是表达式**字符串**,所以同一套规则能用在 GP 的存档、RL 的轨迹、Partura 自己的扫描表上。

## 想法 → AlphaCube → 短搜索(Research Episode)

以前研究一个想法,只能自己写几十个表达式。现在一个想法写成:

```yaml
- id: I1_frozen_state
  hypothesis: 盘口冻结是一个持续几周的状态……哪一种写法、多长的记忆最能标出它
  seeds: ["cross_max(day_zero_ratio(Ret), 15)", …]
  grammar: {day_ops: [day_zero_ratio, day_flat_ratio, …], memory_ops: [cross_max, cross_ema, …]}
  reward: long_bucket
```

`./scripts/study.sh idea I1_frozen_state` 在服务器上跑两臂(各 `--budget` 个候选,默认 192):

- **steer**:种子进首代;想法里的算子采样概率 × `--boost`;每棵候选树过 `Guidance.accept`;必须含想法的核心算子;
- **control**:同一个 GP、同一个奖励、同样的预算与随机种子、同一个算子库,不带任何干预。

两臂用同一把尺子(同一个 Partura 奖励)。产出 `episodes/<tag>_<idea>/`:

```
evidence.json     两臂各自:评估了多少、过门槛多少、两段多头腿都站得住的多少、其中互不重复且不在已知池里的多少
                  = 每百次评估的发现数;以及各臂的前 80 个候选
steer/  control/  AlphaCube 自己的运行目录(checkpoints/archive_gen*.csv 是全部存档)
episode.md        假设 / 干预 / 对照 / 证据 / 信念更新(最后一节由研究者写)
```

信念更新之后回到 `guidance/<batch>.yaml`:规则的权重、状态、证据随之改。搜索只看 2018-01 ~ 2023-08-07(train + valid),
测试段不打开;搜到的候选要进批量扫描和按规则的测试段读数,才算数。

### 什么算「发现」,什么算「比基准好」(2026-10-06 定下来的三条)

1. **发现**只有一个定义:`partura.steer.is_discovery`。水平类奖励 = 分数(两段里较差的纯多头夏普)过线;
   成对奖励(`long_marginal` / `long_screen`)= 合并段过线,**并且** train、valid 各自 ≥ 0.5 —— 合并段的 5.6 年里 train 占 4 年。
   数的时候按**族**数(`Guidance.family_key`),换皮不算新发现。
2. **成对奖励带大小**:`score = IR × min(1, 每年多赚 / 1 个点)`(`partura.steer._sized`)。成对差的信息比没有量纲,
   每天换掉书里一两只票、换得略好而且很稳,信息比能到 2~3 而账面一年只多 0.2 个点(e3_I1 对照臂的 22 个「发现」全是这一种)。
3. **比基准好**用同一天相减的逐日净超额之差判(年化差、信息比、测试段 t),不用两个年化数相减(`scripts/sweep_final.py` 的成对表,
   `scripts/paired_table.py`)。样本内的成对信息比 ≈ 1 在这批数据上对应的样本外 t 不到 1(`studies/K001_known_screens/README.md`)。

每次短搜的证据文件记 `code`(脚本与奖励的文件指纹)、`screen_base`、`reward_device`。服务器端的启动脚本不会同步代码:
起之前先 `./scripts/study.sh code`。

## 和 AlphaCube 本体的关系

到 2026-10-06 为止,奖励与采样钩子都是运行时装上的(`alphacube.mining.scoring.make_scorer`、`TypedTreeGenerator.acceptable` / `._pick`),
服务器上的 AlphaCube 目录没有动。

2026-10-05 用户授权(「你的需求我全部满足」「Partura 的权限等级比 AlphaCube 高」)之后,这些钩子正在并进 AlphaCube 本体:
设计 `docs/alphacube_steering_design.md`(生成器的 `op_weight / accept / daily_fields / leaf_slots`、打分器注册表 `register_scorer`、
插件加载、日频字段叶子 `DailyFeature`、修 `mutate_window` / `mutate_constant` 绕过封禁的漏洞),实现在 AlphaCube 的 `partura-steering` 分支
(worktree `~/Desktop/AlphaCube-steering`);不传新参数时行为与随机数流逐位不变。进度看 `handoff/COORDINATOR.md` 顶部。
