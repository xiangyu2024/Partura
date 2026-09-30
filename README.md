# Partura

**Partura 是 AlphaCube 的"提纯"层。**

AlphaCube 的 GP / RL 负责在巨大的符号空间里硬挖,挖出来的表达式常常预测得动、但没人知道为什么。
Partura 接手一条这样的表达式,回答三个问题:

1. 这棵树**到底在算什么**(按算子源码与实测探针,不按算子名字);
2. 预测力**来自哪一部分**,有没有更简单的解释(规模、价格、波动、动量、反转…);
3. 能不能**蒸馏**成一个更小、更稳、换手更低、看得懂的结构。

Partura 不拥有数据、引擎或回测器 —— 它们全部从 AlphaCube 导入(`partura.bridge`)。

---

## 装配

```bash
export ALPHACUBE_ROOT=~/Desktop/AlphaCube        # 不设则自动找同级目录
~/.venvs/alphacube/bin/python -m partura.cli --help
```

依赖与 AlphaCube 相同(torch / numpy / pandas / pyyaml),不额外装东西。

## 最重要的一条

**每条表达式都是一次新的研究。** 实验计划是从这棵树推出来的,探针集合也是;
上一条因子的配置**不能**改个表达式就拿来跑。唯一跨研究复用的是 `lab/findings.yaml` 里的结论,
而且它是**先验**,不是证据 —— 报告里依赖它就得在本研究里重新测一次。
详见 [`docs/method.md`](docs/method.md)。

## 五个命令

```bash
# 1. 这棵树在算什么(注册表 + 内核源码 + 实跑探针 + 实验室里的相关先验)
python -m partura.cli decompose "cross_max(day_cov(Amt, Low), 9)" \
    [--probes studies/<fid>/probes.py]

# 2. 从树结构 + 探针签名派生**候选**实验 —— 这是草稿,不是计划,要逐条删改
python -m partura.cli propose "<expr>" --factor-id <fid> --out configs/<fid>.draft.yaml

# 3. 跑一个实验阶段(一次引擎调用,变体之间共享子树)
python -m partura.cli run configs/<fid>.yaml \
    --store <cube> --stages S1_components --device cuda --gpu-fraction 0.045

# 4. 拼报告(生成段 = 表格,手写段 = notes/<fid>/*.md)
python -m partura.cli report configs/<fid>.yaml    # -> research/alpha_distillation/<fid>.md

# 5. 实验室笔记本:跨研究唯一复用的东西
python -m partura.cli lab                  # 全部结论
python -m partura.cli lab "<expr>"         # 只看与这棵树相关的
```

## 组成

| 模块 | 干什么 |
|---|---|
| `bridge.py` | 找到并导入 AlphaCube;记录 commit / 版本 / store,让报告里的每个数字可追溯 |
| `probes.py` | **可扩展的探针注册表**。内置探针只覆盖最普遍的问题(日轴因果性、分钟顺序、平移不变、齐次度、保序、缺失、取负、窗口单调、脉冲记忆);**本研究特有的问题写在 `studies/<fid>/probes.py`**,自动加载并在报告里单独标出。不适用就明说,跑不动就报错 —— 不猜 |
| `semantics.py` | **算子档案**:注册表声明 + 内核源码 + 所有适用探针的实测值 + 没跑的探针 |
| `propose.py` | **从树派生候选实验**:isolate / ablate / substitute(按探针签名找"只差一条性质"的兄弟)/ window / field,以及只在探针说相关时才出现的 magnitude / interaction。它提议,不决定 |
| `lab.py` | **实验室笔记本**:跨研究唯一复用的东西。每条结论带证据、出处、置信、**失效条件** |
| `decompose.py` | 表达式 → SSA 形式的可读程序 + 每个节点的结构角色 + 沿路径累计的真实回看天数 |
| `splits.py` | train / valid / holdout 三段 + **台账**:留出段被读过几次、打过多少条分,报告里必须写出来 |
| `panels.py` | 一次引擎调用算完整批表达式(CSE 共享子树),面板按内容寻址缓存到磁盘 |
| `diagnose.py` | 判别性度量:中性化残差、条件 IC(门控检验)、衰减曲线、逐年、极端日依赖、变体间 rank 相关 |
| `runner.py` | 一个阶段 = 一个问题:算面板 → 指标(方向只在训练段定一次)→ 诊断 → JSON |
| `report.py` | 生成段(全部表格)+ 手写段(`notes/<factor_id>/*.md`)拼成报告 |

## 方法上的几条硬规矩

- **算子语义只看实现**。`cross_*` 在这个项目里滚的是**交易日**轴,`day_*` 折叠的是**日内分钟**轴;
  名字不作数,探针作数(日轴因果性是实测出来的,不是假设出来的)。
- **方向只在训练段定一次**,之后原样用到验证段与留出段。每段重新选方向,样本外就没有意义了。
- **所有和钱有关的数字都扣成本**(15 bp 单边),并同时给日换手 —— AlphaCube 的历史结论是换手才是瓶颈。
- **留出段有台账**。反复用同一段留出数据挑变体,它就变成了第二个验证集;报告附录里写清楚它被读过几次。
- **变异要有理由**。每个变体的 `why` 字段说明它想证伪哪个假设;不做"随机再试 100 个相近公式"。
- **原始结果不覆盖**。每个阶段写自己的 JSON,面板缓存按表达式内容寻址。

## 目录

```
configs/     因子 + 实验计划(YAML)
notes/<fid>/ 报告里手写的那几节(假设、诊断、风险、下一步)
runs/<fid>/  每个阶段的 JSON、面板缓存、数据段台账
research/alpha_distillation/<fid>.md   最终报告
scripts/     服务器上的启动脚本
```

## 已完成的研究

| 因子 | 结论 | 报告 |
|---|---|---|
| `F001_dwgated_covamtlow`<br>`cross_max(mul(cross_max(day_cov(Amt,Low),9), pow_3(day_durbin_watson(Open))),5)` | 它 = **流动性水平 × 日内波动 × 极值记忆**,是已知的换手/低波动异象。`day_durbin_watson` 作用在价格水平上时其实是日内已实现方差(与 `day_var(Ret)` rank 相关 0.979);预测力由 `cross_max` 造出来(裸协方差 rank IC 只有 0.0128)。蒸馏成 2 个算子的 `cross_max(day_std(Amt), 9)` 后,扣 15bp 夏普 训练 +3.17 / 验证 +4.52 / **留出 +2.00**,原式是 +1.78 / +2.69 / **+1.01**,换手还低了 40%。 | [报告](research/alpha_distillation/F001_dwgated_covamtlow.md) |

复现:

```bash
export ALPHACUBE_ROOT=~/Desktop/AlphaCube
python -m partura.cli run configs/F001_dwgated_covamtlow.yaml --store <cube> \
    --stages S1_components S2_scale S3_gate S4_memory S5_fields S6_distil --device cuda --gpu-fraction 0.045
python -m partura.cli run configs/F001_dwgated_covamtlow.yaml --store <cube> --stages S7_distil2 ...
python -m partura.cli run configs/F001_dwgated_covamtlow.yaml --store <cube> --stages S8_final --holdout ...
python scripts/corr_all.py && python -m partura.cli report configs/F001_dwgated_covamtlow.yaml
```

服务器上直接用 `scripts/run_server.sh <stage...>`(`EXTRA=--holdout` 才读留出段)。
