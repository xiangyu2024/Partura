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

## 三个命令

```bash
# 1. 看清楚这棵树在算什么(注册表 + 源码 + 实跑探针)
python -m partura.cli decompose "cross_max(day_cov(Amt, Low), 9)"

# 2. 跑一个实验阶段(一次引擎调用,变体之间共享子树)
python -m partura.cli run configs/F001_dwgated_covamtlow.yaml \
    --store <cube> --stages S1_components --device cuda --gpu-fraction 0.045

# 3. 把所有阶段的 JSON 拼成研究报告
python -m partura.cli report configs/F001_dwgated_covamtlow.yaml
# -> research/alpha_distillation/<factor_id>.md
```

## 组成

| 模块 | 干什么 |
|---|---|
| `bridge.py` | 找到并导入 AlphaCube;记录 commit / 版本 / store,让报告里的每个数字可追溯 |
| `semantics.py` | **算子档案**:注册表声明 + 内核源码 + 六类实测探针(日轴因果性、分钟顺序依赖、平移不变、齐次度、保序、缺失行为) |
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
