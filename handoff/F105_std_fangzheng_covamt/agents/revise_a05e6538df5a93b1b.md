# revise:F105_std_fangzheng_covamt — agent a05e6538df5a93b1b(工作流 wf_759ef2d3-03f)

- 状态:**已返回结果**;开始 10-03 23:34,最后一次动作 10-04 00:19;工具调用 74 次
- 这是从 agent 的对话记录里**自动抽出来的动作流水**(命令、输出、写了哪些文件)。agent 的推理不在记录里 ——
  它的判断要看 `notes/F105_std_fangzheng_covamt/journal.md` 和各 notes 文件。输出过长的地方截了中间。

## 动作流水

**10-03 23:34 · Bash** — Check sizes of required docs

```bash
cd /Users/wxy/Desktop/Partura && wc -l CLAUDE.md docs/method.md docs/study_playbook.md && ls
```

```
      27 CLAUDE.md
     123 docs/method.md
     181 docs/study_playbook.md
     331 total
CLAUDE.md
README.md
batches
configs
docs
lab
logs
notes
partura
research
runs
scripts
shared
studies
tests
tmp
```

10-03 23:34 · 读 `/Users/wxy/Desktop/Partura/CLAUDE.md`

10-03 23:34 · 读 `/Users/wxy/Desktop/Partura/docs/method.md`

10-03 23:34 · 读 `/Users/wxy/Desktop/Partura/docs/study_playbook.md`

**10-03 23:34 · Bash** — List study files and read study.sh

```bash
cd /Users/wxy/Desktop/Partura && ls -la notes/F105_std_fangzheng_covamt/ runs/F105_std_fangzheng_covamt/ studies/F105_std_fangzheng_covamt/ && wc -l research/alpha_distillation/F105_std_fangzheng_covamt.md configs/F105_std_fangzheng_covamt.yaml && cat scripts/study.sh | head -150
```

```
notes/F105_std_fangzheng_covamt/:
total 240
drwxr-xr-x@ 24 wxy  staff   768 Oct  3 23:14 .
drwxr-xr-x@ 10 wxy  staff   320 Oct  3 18:37 ..
-rw-r--r--@  1 wxy  staff   796 Oct  3 23:17 01_expression.md
-rw-r--r--@  1 wxy  staff  1856 Oct  3 18:40 02_operators.md
-rw-r--r--@  1 wxy  staff  1821 Oct  3 18:40 03_decomposition.md
-rw-r--r--@  1 wxy  staff  1652 Oct  3 18:40 04_grammar.md
-rw-r--r--@  1 wxy  staff  5573 Oct  3 23:17 05_hypotheses.md
-rw-r--r--@  1 wxy  staff  3246 Oct  3 18:43 06_baseline.md
-rw-r--r--@  1 wxy  staff  3029 Oct  3 22:39 07_S1_what.md
-rw-r--r--@  1 wxy  staff  4427 Oct  3 23:18 07_S1b_events.md
-rw-r--r--@  1 wxy  staff  4212 Oct  3 22:50 07_S2_nodes.md
-rw-r--r--@  1 wxy  staff  3728 Oct  3 22:50 07_S3_family.md
-rw-r--r--@  1 wxy  staff  4118 Oct  3 23:00 07_S4_longleg.md
-rw-r--r--@  1 wxy  staff  3481 Oct  3 23:12 07_S_final.md
-rw-r--r--@  1 wxy  staff  1827 Oct  3 23:17 07_conditional.md
-rw-r--r--@  1 wxy  staff  1068 Oct  3 23:09 07_controls.md
-rw-r--r--@  1 wxy  staff  3047 Oct  3 23:09 07_neutralise.md
-rw-r--r--@  1 wxy  staff  7084 Oct  3 23:17 07x_events.md
-rw-r--r--@  1 wxy  staff  5332 Oct  3 23:19 07x_longleg.md
-rw-r--r--@  1 wxy  staff  2635 Oct  3 23:17 08_variants.md
-rw-r--r--@  1 wxy  staff  6041 Oct  3 23:13 09_diagnosis.md
-rw-r--r--@  1 wxy  staff  5462 Oct  3 23:17 10_distilled.md
-rw-r--r--@  1 wxy  staff  2735 Oct  3 23:14 11_risks.md
-rw-r--r--@  1 wxy  staff  1462 Oct  3 23:14 12_next.md

runs/F105_std_fangzheng_covamt/:
total 1248
drwxr-xr-x@  9 wxy  staff     288 Oct  3 23:11 .
… (99 行略) …
    $RS "$SSH" --include='*.json' --exclude='*' "$HOST:$R/runs/$fid/" "runs/$fid/" 2>/dev/null
    if [ -f "runs/$fid/$tag.json" ]; then "$PY" scripts/summarize.py "runs/$fid/$tag.json";
    else echo "(no runs/$fid/$tag.json — an exec job prints its own output; full log: logs/${fid}_${tag}.log)";
         grep -av 'FutureWarning\|vmap(single_row)\|UserWarning' "logs/${fid}_${tag}.log" | tail -200; fi
    ;;
  digest)
    fid=$1; tag=$2; base=${3:-v_base}
    "$PY" scripts/summarize.py "runs/$fid/$tag.json" --base "$base"
    ;;
  report)
    fid=$1; push "$fid" || exit 1
    $SSH $HOST "$ENV && $RPY -m partura.cli report configs/$fid.yaml 2>&1 | grep -v 'FutureWarning\|vmap(single_row)'" || exit 1
    mkdir -p research/alpha_distillation
    $RS "$SSH" "$HOST:$R/research/alpha_distillation/$fid.md" research/alpha_distillation/ && wc -l "research/alpha_distillation/$fid.md"
    ;;
  status)
    $SSH $HOST "screen -ls | grep pt_ ; echo; nvidia-smi --query-compute-apps=pid,used_memory --format=csv,noheader; awk '/^anon /{printf \"container anon %.1f GiB\n\", \$2/1073741824}' /sys/fs/cgroup/memory.stat; ls $R/tmp/locks 2>/dev/null | tr '\n' ' '"
    ;;
  *) sed -n '2,16p' "$0"; exit 2 ;;
esac
```

10-03 23:34 · 读 `/Users/wxy/Desktop/Partura/configs/F105_std_fangzheng_covamt.yaml`

**10-03 23:34 · Bash** — List F105 logs and show ledger

```bash
cd /Users/wxy/Desktop/Partura && ls -la logs/ | grep -i F105; cat runs/F105_std_fangzheng_covamt/ledger.json
```

```
-rw-r--r--@  1 wxy  staff   1836 Oct  3 19:37 F105_std_fangzheng_covamt_S1_what.log
-rw-r--r--@  1 wxy  staff   1409 Oct  3 22:45 F105_std_fangzheng_covamt_S2S3_nodes_family.log
-rw-r--r--@  1 wxy  staff   1585 Oct  3 22:57 F105_std_fangzheng_covamt_S4_longleg.log
-rw-r--r--@  1 wxy  staff  18305 Oct  3 23:29 F105_std_fangzheng_covamt_audit1.log
-rw-r--r--@  1 wxy  staff   1075 Oct  3 23:11 F105_std_fangzheng_covamt_final.log
-rw-r--r--@  1 wxy  staff  12160 Oct  3 19:28 F105_std_fangzheng_covamt_x1_events.log
-rw-r--r--@  1 wxy  staff  10779 Oct  3 23:05 F105_std_fangzheng_covamt_x2_longleg.log
{
  "entries": [
    {
      "when": "2026-10-03T23:51:21Z",
      "split": "train",
      "n_expressions": 1,
      "purpose": "stage metrics + diagnostics",
      "stage": "S0_baseline"
    },
    {
      "when": "2026-10-03T23:51:21Z",
      "split": "valid",
      "n_expressions": 1,
      "purpose": "stage metrics + diagnostics",
      "stage": "S0_baseline"
    },
    {
      "when": "2026-10-03T23:51:21Z",
      "split": "utrain",
      "n_expressions": 1,
      "purpose": "stage metrics + diagnostics",
      "stage": "S0_baseline"
    },
… (165 行略) …
      "expressions": 57
    },
    "valid": {
      "reads": 8,
      "expressions": 57
    },
    "utrain": {
      "reads": 8,
      "expressions": 57
    },
    "holdout": {
      "reads": 1,
      "expressions": 5
    },
    "full": {
      "reads": 1,
      "expressions": 5
    }
  }
}
```

10-03 23:34 · 读 `/Users/wxy/Desktop/Partura/studies/F105_std_fangzheng_covamt/audit_1.py`

10-03 23:34 · 读 `/Users/wxy/Desktop/Partura/logs/F105_std_fangzheng_covamt_audit1.log`

**10-03 23:34 · Bash** — Print notes 01 through 07_S1b

```bash
cd /Users/wxy/Desktop/Partura/notes/F105_std_fangzheng_covamt && for f in 01_expression.md 02_operators.md 03_decomposition.md 04_grammar.md 05_hypotheses.md 06_baseline.md 07_S1_what.md 07_S1b_events.md; do echo "=================== $f"; cat $f; echo; done
```

```
=================== 01_expression.md
这条表达式是挖掘库的 #25:`ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5)`。
用户表里公布的一行是:方向 −1、EMA 半衰期 3、扣费多空夏普 训练 3.03 / 测试 2.24、多头腿毛超额 16.8% / 14.3%。
S0 用 Partura 自己求值复现了训练列(3.03、16.8%);留出段那一次(S_final)复现了测试列(2.24、14.3%)。

**一句话(读完源码之后)**:它是「**分钟成交额方差**(带成交额平方的尺度)的**一年期 mean+std 水平**,在**最近 5 天里动了多少**」——
也就是「最近一周有没有一个(按原始金额计)很大的放量日**进入**一年窗口,或者一年前的那个放量日**滑出**窗口」。
它不是一个「波动的波动」,名字里的两个 std 都不是收益的波动。

=================== 02_operators.md
读内核源码(`study.sh src`)时发现的、和名字不一样或探针表里看不出来的事:

1. **`day_cov(Amt, Amt)` 就是日内分钟成交额的总体方差**(分母是有效分钟数,不是 n−1;有效分钟 < 2 时为 NaN)。
   它恒非负、对 Amt 是 **2 次齐次**(探针实测 k = 2.0)。和 `day_var(Amt)` = `day_std(Amt)²` 是同一个量,
   所以这棵树从叶子开始就带着「成交额的平方」这个尺度,而且一路没有任何去尺度的节点(后面三层都是 1 次齐次)。
2. **`cross_fangzheng(x, d)` = `cross_mean(x, d) + cross_stddev(x, d)`**,一行代码。名字(方正?)没有任何信息量。
   两项都是**硬窗口**、**忽略 NaN**(`nanmean` / 总体 `nanstd`,分母是窗口内有限值的个数)。
3. **241 在这里是交易日数,不是分钟数。** `cross_*` 滚的是交易日轴;241 恰好是每天的分钟格数,
   但作为 `cross_fangzheng` 的窗口它是「约一年」(一年约 243 个交易日)。
4. **窗口不满也出值。** `rolling_windows` 在左侧补 NaN,`nanmean/nanstd` 只在有限值上算,所以一只股票上市后的
   头 241 个交易日、以及样本头一年(视图从 20180102 开始,warmup 实际拿到 0 行),`C` 用的是**逐日变长的扩张窗口**:
   第 n 天进来一个新值,均值移动 (x−均值)/n,比窗口满了之后的 1/241 大得多。→ 次新股的 `D` 被机械放大(见 H7)。
5. **`ts_stddev` = `ts_std`**,总体标准差,同样忽略 NaN。它对输入取负不变(偶函数):`C` 往上走和往下走读出来一样。
6. **内置探针在 241 窗口上是瞎的。** 内置探针的样本只有 40 行,比窗口短:`cross_fangzheng` 的「脉冲记忆天数 = 27」
   只是 40 − 13 = 27(脉冲之后剩下的行数),不是这个算子的性质。本研究的四个探针都用 ≥ 3×窗口 的样本重测。

=================== 03_decomposition.md
分解表之外需要说清楚的三个公式(全部来自源码 + 本研究的探针,不是名字):

**(1) 根节点读的是「慢水平的 5 日变化量」。** `C` 是一年窗口的统计量,一天只进一个值、出一个值,
… (145 行略) …
   - 它不是成交额水平(对 `ctl_amt` 中性化 R² 只有 0.035,残差 rank IC 0.0189、无成本多空夏普 +3.41),
     全部控制变量也只张成 0.145;最能解释它的是 `ctl_dvol20`(R² 0.101,残差 rank IC 0.0129)和 `ctl_turnrate`(0.061 / 0.0161)——
     「最近相对自己的历史放过量」和「最近波动大、换手高」是同一类东西。全部控制变量之后残差 rank IC 0.0084、无成本多空夏普 +1.45。
   - 条件 IC:按 `known_stdamt_max9` 分五桶,它的桶内 IC 是 −0.0074、−0.0064、−0.0092、−0.0156、**−0.0437**;按 `ctl_amt` 分桶是
     −0.0098 → **−0.0408**。**事件信息几乎只在成交额最大的那一桶里有用** —— 它是「大成交额股票里谁刚爆过量」的细分,不是一个全截面的信号。
2. **去掉周年回声(`s1_noecho`,中间层换成线性衰减均值)**:rank IC 0.0337 / 0.0380,多空夏普 +2.23 / +3.78,多头腿净超额 +6.3% / +13.2%。
   配对对照是 `s2_mid_mean`(同样只有 mean 项,但硬窗口、有回声):+2.21 / +4.44、+8.6% / +20.4%。**去掉回声没有变好,验证段反而差**
   (多空 −0.66,多头腿净超额 −7.2 个点)。H3 预测的「去掉回声不变差」没有得到这个替换实验的支持。
   但这个替换不干净:线性衰减让窗口里每个旧值的权重天天往下掉,`C` 每天都在匀速漂移,漂移速度 ∝ 水平 / 241,
   于是外层 std 读到的背景从「0」变成了「水平」(它与 `ctl_amt` 的 rank 相关 0.68、与原式 0.76)——换掉的不只是回声。
   回声是稀释的直接证据仍然是 07x 的分组(空头十分位里滑出组的超额 −5.1% / −13.2%,进入组 −38.6% / −62.4%)和剔除实验
   (剔掉滑出驱动的股票日后多头腿毛超额 +2.2 / +3.9 个点、空头腿 +3.2 / +12.1 个点);表达式语言里没有一个只去掉回声而不动别的东西的算子。
3. **删掉一年窗口(`s1_recent`)**:`cross_stddev(cross_max(day_cov(Amt,Amt),3),5)`,rank IC **0.0480 / 0.0649**(高于原式的 0.0387 / 0.0521),
   多空夏普 +2.31 / +3.97,多头腿净超额 +10.8% / +17.2%。它与已知家族的 rank 相关是 **0.94**、与原式 0.67。
   删掉 241 日窗口之后得到的就是已知家族(「最近一周日内成交额离散度的大小」≈「最近 9 天的峰值」),rank IC 还更高。
   **一年窗口不是预测力的来源**;它做的事是把「最近的成交额水平」换成了「最近的成交额水平相对一年历史的变化」,
   后者的多空略高(+2.54 对 +2.31,在噪声内)、rank IC 更低。

**解读**:原式的两半里,「水平」这一半是成交额水平(S1),「事件」这一半是一个只在大成交额股票里起作用的空头信号。
两半都不是这棵树独有的:水平是 `ctl_amt`,事件与 `ctl_dvol20` / `ctl_turnrate` 同类,合起来就是已知家族。
```

**10-03 23:34 · Bash** — Print notes 07_S2 through 07_neutralise

```bash
cd /Users/wxy/Desktop/Partura/notes/F105_std_fangzheng_covamt && for f in 07_S2_nodes.md 07_S3_family.md 07_S4_longleg.md 07_S_final.md 07_conditional.md 07_controls.md 07_neutralise.md; do echo "=================== $f"; cat $f; echo; done
```

```
=================== 07_S2_nodes.md
**问题**:树里哪些节点是多余的?外层 std 换成 |5 日差分| 能不能去掉上市首日的伪影?

原式(train / valid):rank IC 0.0387 / 0.0521,多空夏普 +2.54 / +4.62,多头腿毛超额 +13.1% / +26.0%、净超额 +8.2% / +20.7%,日换手 6.0%。
这批因子的多空夏普噪声大约 ±0.3,下面只把超出这个幅度、且 train 和 valid 同向的差别当成差别。

| 动了什么 | 变体 | 与原式 rank 相关 | 多空夏普 | 多头腿净超额 | 读法 |
|---|---|---|---|---|---|
| 外层 `ts_stddev` → `cross_stddev`(同一内核的 dt 面写法) | `s2_dtface_check` | 1.000 | +2.54 / +4.62 | +8.2% / +20.7% | 逐位相同,工具绕行成立 |
| 删掉 `cross_max(·,3)` | `s2_no_max3` | 0.967 | +2.67 / +4.77 | +9.4% / +21.2% | **多余**(H5 成立),删掉略好 |
| `fangzheng` → 只留 std 项 | `s2_mid_std` | 0.965 | +2.64 / +4.65 | +8.0% / +20.4% | 同一个东西 |
| `fangzheng` → 只留 mean 项 | `s2_mid_mean` | **0.983** | +2.21 / +4.44 | +8.6% / +20.4% | 同一个东西,而且比 std 项离原式更近 |
| 删 max3 + 只留 std 项(树内最小,3 个算子) | `s2_min3` | 0.937 | **+2.84 / +4.80** | **+9.9% / +20.9%** | 保住并略超过原式 |
| 叶子 方差 → 标准差 | `s2_field_std` | 0.965 | +2.72 / +4.00 | +9.0% / +16.2% | 训练段不变,验证段多空 −0.62、多头 −4.5 个点 |
| 叶子 方差 → 日成交额 | `s2_field_sum` | 0.894 | +2.29 / +3.62 | +7.8% / +15.5% | 变差(验证段多空 −1.00) |
| 一年窗口 241 → 60 | `s2_w60` | 0.642 | +2.18 / +4.28 | +7.8% / +17.8% | 略差,没有塌 |
| 外层窗口 5 → 20 | `s2_out20` | 0.826 | +2.34 / +4.39 | +8.7% / +20.1% | 不变(换手 6.0% → 4.6%) |
| 外层 std → \|5 日差分\| | `s2_absdelta` | 0.981 | +2.57 / +4.64 | +9.8% / +20.2% | 多头腿毛超额 +15.7% / +26.6%(原式 +13.1% / +26.0%) |

**读法**

1. **H5 成立,`cross_max(·,3)` 多余。** 删掉后 rank 相关 0.967,所有指标不降反升一点。
2. **H4 的后半句被否定。** H4 说「`fangzheng → cross_stddev` 与原式同族,`→ cross_mean` 明显不同」;实测 mean 项版本与原式的 rank 相关是 0.983,
   比 std 项版本(0.965)还高。原因在 03 节的公式里:外层读的是 5 日**变化量**,而一个值进出窗口时 mean 项和 std 项是**同时、同向**地动,
   截面上谁动得多取决于进出的那个值有多大,与用哪个统计量去记这一年无关。`C` 是极值统计量(07x 第 1 节)这件事本身没错,
   但它对原式的排序不重要 —— **「相对一年历史」这一层没有在做归一化,它只是一个把最近的值和一年前的值之差读出来的装置。**
3. **树内最小结构是 `cross_stddev(cross_stddev(day_cov(Amt, Amt), 241), 5)`(3 个算子)。** 多空 +2.84 / +4.80、多头腿净超额 +9.9% / +20.9%,
   train 和 valid 都不低于原式;与原式的 rank 相关 0.937(略低于 0.95 的同族线,差在少了 3 日极值对每个尖峰的三倍加权)。
4. **H9(幸运参数)不成立。** 241 → 60、5 → 20 都没有塌(多空 +2.18 / +4.28 与 +2.34 / +4.39)。241 换成 60 之后与原式的 rank 相关只剩 0.64,
   与已知家族反而升到 0.73 —— 窗口越短,它越接近「最近的成交额水平」。
… (148 行略) …
   `s1_level`(一年水平 `C`)对 `ctl_amt`:R² 0.449,残差 rank IC **−0.0007**、无成本多空夏普 +0.07。
   `s1_relchg`(无尺度的相对变化)对 `ctl_amt`:R² 只有 0.035,残差 rank IC 0.0189、无成本多空夏普 +3.41;
   全部控制变量也只张成 0.145,但残差 rank IC 掉到 0.0084 —— 掉的那部分跟着 `ctl_dvol20`(R² 0.101)和 `ctl_turnrate`(0.061)走。
3. **已知家族在成交额水平之外还有东西,而且越短的窗口剩得越多。** 对 `ctl_amt` 中性化后的残差 rank IC / 无成本多空夏普:
   `s1_known_stdamt9`(d=9)0.0270 / +4.93,`s4_max30` 0.0161 / +2.17,`s3_max60` 0.0078 / +0.91,`s1_level`(d=241)−0.0007 / +0.07。
   这部分是「最近的峰值相对今天的成交额」= 近期放量事件;窗口越长它被稀释得越多。
   但**多头腿在长窗口上剩得比空头腿多**:`s3_max60` 对 `ctl_amt` 中性化后多头腿毛超额还有 +9.2%、空头腿 −0.5%;`s4_max30` 是 +11.1% / +6.7%。
4. **多头腿和空头腿跟着成交额的两个不同成分走。** 成交额 = 流通市值 × 换手率。对 `ctl_cap` 中性化(留下的是换手率那一侧)和对 `ctl_turnrate` 中性化
   (留下的是市值那一侧)之后,两条腿的毛超额(训练段):

   | | 未中性化 多头 / 空头 | 对 `ctl_cap` 中性化 | 对 `ctl_turnrate` 中性化 |
   |---|---|---|---|
   | `v_base` | +13.1% / +29.9% | +9.5% / +31.0% | +16.8% / +10.0% |
   | `s1_known_stdamt9` | +16.9% / +37.7% | +7.9% / +53.3% | +24.5% / +8.7% |
   | `s4_max30` | +17.4% / +27.0% | +8.4% / +41.6% | +23.3% / +7.6% |
   | `s3_max60` | +15.9% / +21.0% | +7.8% / +31.1% | +19.4% / +6.0% |

   四个因子同一个形状:拿掉市值,已知家族的多头腿掉一半(原式掉四分之一)、空头腿变大;拿掉换手率,空头腿掉到三分之一左右或更低、多头腿变大。
   **空头腿的钱是「高换手率」,多头腿的钱在「小市值」那一侧。** 但 `ctl_cap` 自己当因子在训练段没有多头腿(见下面的控制变量表),
   所以多头腿不是单纯的小市值溢价,而是「小市值里成交清淡、近期没放过量」的那一部分(07x 第 4 张表、S4 的 `s4_med60` 是另外两条证据)。
```

**10-03 23:34 · Bash** — Print notes 07x through 12

```bash
cd /Users/wxy/Desktop/Partura/notes/F105_std_fangzheng_covamt && for f in 07x_events.md 07x_longleg.md 08_variants.md 09_diagnosis.md 10_distilled.md 11_risks.md 12_next.md; do echo "=================== $f"; cat $f; echo; done
```

```
<persisted-output>
Output too large (30.3KB). Full output saved to: /Users/wxy/.claude/projects/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/tool-results/bgxopbcs2.txt

Preview (first 2KB):
=================== 07x_events.md
### 07x 直接量数据:根节点的排序跟着什么走,钱落在哪一类股票日上(`studies/F105_std_fangzheng_covamt/events.py`)

内置诊断分不开「进入 / 滑出 / 窗口未满」这三类事件,所以写了一个脚本直接在面板上量(只用 train / valid)。
记号:`A = day_cov(Amt,Amt)`,`B = cross_max(A,3)`,`C = cross_fangzheng(B,241)`,`D = ts_stddev(C,5)`(原式)。

**(1) 真实数据的尾巴有多重 —— H4 成立。**
每只股票 log(A) 的时间序列标准差:中位数 **1.75**(p10 1.34,p90 2.24),落在探针 `tail_dominance` 里
「mean+std ≈ 极值统计量」的区间。`C` 里 std 项占比 `Cstd/C` 中位数 **0.73**;一年最大值是一年中位数的 **98 倍**(中位数)。
去掉尺度之后(各自除以一年中位数),`C` 与一年最大值的日截面 rank 相关 **0.984**(与一年均值 0.985,两者在这么重的尾巴下是一回事),
而 `C` 与一年中位数只有 0.782。**`C` 读的是「这一年里最大的那几次放量」,不是平均水平。**

**(2) `D` 的截面排序 = 两个几乎正交的成分各占一半。**

| 日截面 rank 相关(train) | 值 |
|---|---|
| `D` ~ \|C_t − C_{t−4}\| | **0.994** |
| `D` ~ 水平 `C` | 0.668 |
| `D` ~ 相对变化 `D/C` | 0.678 |
| 相对变化 ~ 水平 `C` | **0.019** |
| `D` ~ `ctl_amt` / `known_stdamt_max9` | 0.654 / 0.682 |
| 相对变化 ~ `ctl_amt` | 0.191 |

外层 `ts_stddev(·,5)` 就是「5 日变化量的绝对值」(0.994)。`D` = 水平 × 相对变化,两者不相关(0.019),各自单独的 rank IC 都是
0.026 左右(水平 −0.0262 / −0.0313,相对变化 −0.0259 / −0.0376,train / valid),合起来是 `D` 的 −0.0387 / −0.0521。
按水平分五桶,相对变化的桶内 IC 是 −0.017 → −0.032(每桶都在);按相对变化分五桶,水平的桶内 IC 平在 −0.025~−0.029。
**是相加,不是门控。**(后注:这句话只对「按一年水平 `C` 分桶」成立;按**当前**成交额或已知家族分桶,事件的桶内 IC 在最高一桶是最低一桶的 4~6 倍,见条件 IC 表后的说明。)

**(3) 空头腿的解剖(实际交易的信号,hl=3;事件类别按 EMA(sign(ΔC)·D) 的符号分)。**

| 空头十分位里的 | 占十分位 train / valid | 占全截面 | 组内平均超额 train / valid | 对十分位超额的贡献 train / valid | 成交额分位 |
|---|---|---|---|---|---|
| 进入驱动(`C` 在升) | 33.8% / 35.2% | 39.1% / 44.0% | **−38.6% / −62.4%** | −13.6% / −21.6% | 0.92 / 0.91 |
| 滑出驱动(`C` 在降,周年回声) | 23.0% / 47.7% | 32.1% / 48.3% | **−5.1% / −13.2%** | −1.7% / −6.6% | 0.66 / 0.72 |
| 次新股(有效观测 < 247 天) | **25.3% / 17.0%** | 7.0% / 7.6% | −43.0% / −35.2% | −8.7% / −6.3% | 0.76 / 0.69 |
| 样本头一年(2018,全体窗口未满) | 17.8% / — | 21.8% / — | −35.7% / — | −6.0% / — | 0.86 |
| 整个十分位 | | | **−30.3% / −34.8%** | | |

...
</persisted-output>
```

10-03 23:35 · 读 `/Users/wxy/.claude/projects/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/tool-results/bgxopbcs2.txt`

**10-03 23:35 · Bash** — Inspect final.json structure

```bash
cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python - <<'EOF'
import json
d=json.load(open('runs/F105_std_fangzheng_covamt/final.json'))
print(d.keys())
r=d['results']
print(type(r), list(r.keys()) if isinstance(r,dict) else len(r))
k='f_max30'
x=r[k]
print(x.keys())
for kk in ('books','books_user'):
    print(kk, x[kk].keys())
bu=x['books_user']
for kk,v in bu.items():
    if isinstance(v,dict): print(kk, list(v.keys())[:20])
    else: print(kk, v if not isinstance(v,list) else v[:3])
EOF
```

```
dict_keys(['factor_id', 'config', 'stages', 'provenance', 'view', 'label', 'cost_per_side', 'top_frac', 'fit_split', 'user_split', 'rank_by', 'halflives', 'splits_used', 'split_dates', 'results', 'errors', 'engine_timings', 'diagnostics', 'seconds', 'peak_anon_gb'])
<class 'dict'> ['f_orig', 'f_min3', 'f_max15', 'f_max30', 'f_max60']
dict_keys(['expr', 'stage', 'why', 'group', 'sign', 'splits', 'distinct', 'books', 'sign_user', 'ic_user', 'ic_holdout', 'books_user'])
books dict_keys(['hl_ls', 'hl_long', 'hl_used', 'rank_by', 'sweep', 'splits', 'splits_at_hl_long'])
books_user dict_keys(['hl_ls', 'hl_long', 'hl_used', 'rank_by', 'sweep', 'splits', 'splits_at_hl_long'])
hl_ls 0.0
hl_long 1.0
hl_used 0.0
rank_by ls
sweep [{'halflife': 0.0, 'ls_sharpe': 2.8006646157366397, 'ls_turnover': 0.038215838339702934, 'long_sharpe': 2.4600931110323976, 'long_ann': 0.16058407996447588, 'long_turnover': 0.04702746100594945}, {'halflife': 1.0, 'ls_sharpe': 2.7525093284304907, 'ls_turnover': 0.03362377480764145, 'long_sharpe': 2.547904368463587, 'long_ann': 0.1674691328463291, 'long_turnover': 0.040417388436635684}, {'halflife': 2.0, 'ls_sharpe': 2.616976343073295, 'ls_turnover': 0.030577317514254843, 'long_sharpe': 2.503589060420089, 'long_ann': 0.16554101448057953, 'long_turnover': 0.03606716196928409}]
splits ['utrain', 'holdout']
splits_at_hl_long ['utrain', 'holdout']
```

**10-03 23:35 · Bash** — Print books at hl_ls and hl_long for final candidates

```bash
cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python - <<'EOF'
import json
d=json.load(open('runs/F105_std_fangzheng_covamt/final.json'))
r=d['results']
def f(b): 
    return f"LS {b['ls_sharpe']:+.2f} Lgross {b['long_gross_ann']:+.1%} Lnet {b['long_ann']:+.1%} Lshp {b['long_sharpe']:+.2f} short {b.get('short_gross_ann',float('nan')):+.1%} TO {b['ls_turnover']:.1%} Lto {b.get('long_turnover',float('nan')):.1%} mdd {b.get('long_maxdd', float('nan'))}"
print(list(r['f_orig']['books_user']['splits']['holdout'].keys()))
for k,x in r.items():
    for bk in ('books','books_user'):
        b=x[bk]
        print(f"\n{k} [{bk}] hl_ls {b['hl_ls']} hl_long {b['hl_long']} hl_used {b['hl_used']}")
        for s,v in b['splits'].items(): print(f"   @hl_ls   {s:<8} {f(v)}")
        for s,v in b['splits_at_hl_long'].items(): print(f"   @hl_long {s:<8} {f(v)}")
        print("   sweep:", " | ".join(f"hl{int(w['halflife'])}: LS {w['ls_sharpe']:.2f} Lshp {w['long_sharpe']:.2f} Lnet {w['long_ann']:.1%} TO {w['ls_turnover']:.1%}" for w in b['sweep']))
EOF
```

```
Exit code 1
['ls_sharpe', 'ls_ann', 'ls_mdd', 'ls_gross_sharpe', 'ls_turnover', 'long_sharpe', 'long_ann', 'long_mdd', 'long_gross_ann', 'long_turnover', 'short_gross_ann', 'long_share', 'n_days']

f_orig [books] hl_ls 3.0 hl_long 10.0 hl_used 3.0
   @hl_ls   train    LS +2.54 Lgross +13.1% Lnet +8.2% Lshp +1.32 short +29.9% TO 6.0% Lto 6.6% mdd nan
   @hl_ls   valid    LS +4.62 Lgross +26.0% Lnet +20.7% Lshp +3.82 short +34.2% TO 6.6% Lto 7.0% mdd nan
   @hl_long train    LS +2.32 Lgross +12.1% Lnet +9.3% Lshp +1.49 short +23.6% TO 3.2% Lto 3.6% mdd nan
   @hl_long valid    LS +4.08 Lgross +20.8% Lnet +18.2% Lshp +3.30 short +28.5% TO 3.3% Lto 3.4% mdd nan
   sweep: hl0: LS 1.83 Lshp -0.09 Lnet -0.5% TO 13.3% | hl1: LS 2.28 Lshp 0.83 Lnet 5.0% TO 9.5% | hl2: LS 2.51 Lshp 1.29 Lnet 7.9% TO 7.2% | hl3: LS 2.54 Lshp 1.32 Lnet 8.2% TO 6.0% | hl5: LS 2.43 Lshp 1.40 Lnet 8.7% TO 4.6% | hl10: LS 2.32 Lshp 1.49 Lnet 9.3% TO 3.2% | hl20: LS 1.96 Lshp 1.22 Lnet 7.7% TO 2.3%

f_orig [books_user] hl_ls 3.0 hl_long 3.0 hl_used 3.0
   @hl_ls   utrain   LS +3.03 Lgross +16.8% Lnet +11.8% Lshp +1.96 short +31.1% TO 6.1% Lto 6.7% mdd nan
   @hl_ls   holdout  LS +2.24 Lgross +14.3% Lnet +8.9% Lshp +1.04 short +32.6% TO 6.7% Lto 7.1% mdd nan
Traceback (most recent call last):
  File "<stdin>", line 12, in <module>
KeyError: 'splits_at_hl_long'
```

**10-03 23:35 · Bash** — Print books at hl_ls and hl_long for final candidates

```bash
cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python - <<'EOF'
import json
d=json.load(open('runs/F105_std_fangzheng_covamt/final.json'))
r=d['results']
def f(b): 
    return f"LS {b['ls_sharpe']:+.2f} Lgross {b['long_gross_ann']:+.1%} Lnet {b['long_ann']:+.1%} Lshp {b['long_sharpe']:+.2f} short {b.get('short_gross_ann',float('nan')):+.1%} TO {b['ls_turnover']:.1%} Lto {b.get('long_turnover',float('nan')):.1%} Lmdd {b.get('long_mdd', float('nan')):.1%}"
for k,x in r.items():
    for bk in ('books','books_user'):
        b=x[bk]
        print(f"\n{k} [{bk}] hl_ls {b['hl_ls']} hl_long {b['hl_long']} hl_used {b['hl_used']}")
        for s,v in b['splits'].items(): print(f"   @hl_ls   {s:<8} {f(v)}")
        for s,v in b.get('splits_at_hl_long',{}).items(): print(f"   @hl_long {s:<8} {f(v)}")
        print("   sweep:", " | ".join(f"hl{int(w['halflife'])}: LS {w['ls_sharpe']:.2f} Lshp {w['long_sharpe']:.2f} Lnet {w['long_ann']:.1%} TO {w['ls_turnover']:.1%}" for w in b['sweep']))
EOF
```

```
f_orig [books] hl_ls 3.0 hl_long 10.0 hl_used 3.0
   @hl_ls   train    LS +2.54 Lgross +13.1% Lnet +8.2% Lshp +1.32 short +29.9% TO 6.0% Lto 6.6% Lmdd -9.6%
   @hl_ls   valid    LS +4.62 Lgross +26.0% Lnet +20.7% Lshp +3.82 short +34.2% TO 6.6% Lto 7.0% Lmdd -3.7%
   @hl_long train    LS +2.32 Lgross +12.1% Lnet +9.3% Lshp +1.49 short +23.6% TO 3.2% Lto 3.6% Lmdd -9.3%
   @hl_long valid    LS +4.08 Lgross +20.8% Lnet +18.2% Lshp +3.30 short +28.5% TO 3.3% Lto 3.4% Lmdd -3.6%
   sweep: hl0: LS 1.83 Lshp -0.09 Lnet -0.5% TO 13.3% | hl1: LS 2.28 Lshp 0.83 Lnet 5.0% TO 9.5% | hl2: LS 2.51 Lshp 1.29 Lnet 7.9% TO 7.2% | hl3: LS 2.54 Lshp 1.32 Lnet 8.2% TO 6.0% | hl5: LS 2.43 Lshp 1.40 Lnet 8.7% TO 4.6% | hl10: LS 2.32 Lshp 1.49 Lnet 9.3% TO 3.2% | hl20: LS 1.96 Lshp 1.22 Lnet 7.7% TO 2.3%

f_orig [books_user] hl_ls 3.0 hl_long 3.0 hl_used 3.0
   @hl_ls   utrain   LS +3.03 Lgross +16.8% Lnet +11.8% Lshp +1.96 short +31.1% TO 6.1% Lto 6.7% Lmdd -9.6%
   @hl_ls   holdout  LS +2.24 Lgross +14.3% Lnet +8.9% Lshp +1.04 short +32.6% TO 6.7% Lto 7.1% Lmdd -14.4%
   sweep: hl0: LS 2.25 Lshp 0.35 Lnet 2.0% TO 13.7% | hl1: LS 2.75 Lshp 1.34 Lnet 7.9% TO 9.8% | hl2: LS 2.99 Lshp 1.84 Lnet 11.0% TO 7.4% | hl3: LS 3.03 Lshp 1.96 Lnet 11.8% TO 6.1% | hl5: LS 2.89 Lshp 1.96 Lnet 11.9% TO 4.7% | hl10: LS 2.74 Lshp 1.96 Lnet 11.9% TO 3.2% | hl20: LS 2.41 Lshp 1.68 Lnet 10.1% TO 2.3%

f_min3 [books] hl_ls 3.0 hl_long 10.0 hl_used 3.0
   @hl_ls   train    LS +2.84 Lgross +14.3% Lnet +9.9% Lshp +1.62 short +32.9% TO 5.9% Lto 5.9% Lmdd -9.7%
   @hl_ls   valid    LS +4.80 Lgross +25.5% Lnet +20.9% Lshp +3.75 short +36.6% TO 6.5% Lto 6.1% Lmdd -3.5%
   @hl_long train    LS +2.62 Lgross +13.8% Lnet +11.1% Lshp +1.84 short +26.0% TO 3.3% Lto 3.5% Lmdd -8.6%
   @hl_long valid    LS +4.35 Lgross +21.6% Lnet +19.1% Lshp +3.56 short +30.0% TO 3.4% Lto 3.3% Lmdd -3.5%
   sweep: hl0: LS 2.13 Lshp 0.26 Lnet 1.6% TO 13.7% | hl1: LS 2.62 Lshp 1.17 Lnet 7.3% TO 9.4% | hl2: LS 2.81 Lshp 1.55 Lnet 9.5% TO 7.1% | hl3: LS 2.84 Lshp 1.62 Lnet 9.9% TO 5.9% | hl5: LS 2.78 Lshp 1.68 Lnet 10.2% TO 4.6% | hl10: LS 2.62 Lshp 1.84 Lnet 11.1% TO 3.3% | hl20: LS 2.26 Lshp 1.56 Lnet 9.6% TO 2.4%

f_min3 [books_user] hl_ls 3.0 hl_long 10.0 hl_used 3.0
   @hl_ls   utrain   LS +3.30 Lgross +17.5% Lnet +13.0% Lshp +2.18 short +33.9% TO 6.1% Lto 5.9% Lmdd -9.7%
   @hl_ls   holdout  LS +2.72 Lgross +16.3% Lnet +11.5% Lshp +1.33 short +37.8% TO 6.7% Lto 6.3% Lmdd -14.1%
   @hl_long utrain   LS +3.03 Lgross +16.0% Lnet +13.4% Lshp +2.28 short +27.1% TO 3.3% Lto 3.4% Lmdd -8.6%
   @hl_long holdout  LS +2.52 Lgross +16.0% Lnet +13.5% Lshp +1.74 short +27.9% TO 3.4% Lto 3.3% Lmdd -10.9%
   sweep: hl0: LS 2.45 Lshp 0.67 Lnet 4.0% TO 14.3% | hl1: LS 3.05 Lshp 1.65 Lnet 10.0% TO 9.7% | hl2: LS 3.28 Lshp 2.09 Lnet 12.6% TO 7.3% | hl3: LS 3.30 Lshp 2.18 Lnet 13.0% TO 6.1% | hl5: LS 3.23 Lshp 2.21 Lnet 13.1% TO 4.7% | hl10: LS 3.03 Lshp 2.28 Lnet 13.4% TO 3.3% | hl20: LS 2.69 Lshp 1.99 Lnet 11.6% TO 2.4%

f_max15 [books] hl_ls 0.0 hl_long 3.0 hl_used 0.0
   @hl_ls   train    LS +2.61 Lgross +18.0% Lnet +12.3% Lshp +1.81 short +34.9% TO 6.2% Lto 7.5% Lmdd -10.0%
   @hl_ls   valid    LS +4.52 Lgross +26.1% Lnet +21.3% Lshp +3.56 short +45.2% TO 5.5% Lto 6.3% Lmdd -4.2%
   @hl_long train    LS +2.29 Lgross +17.4% Lnet +13.9% Lshp +2.04 short +26.6%
… (890 字符略) …
% Lnet +16.7% Lshp +2.55 short +27.9% TO 3.4% Lto 4.0% Lmdd -8.8%
   @hl_long holdout  LS +2.29 Lgross +16.3% Lnet +13.5% Lshp +1.47 short +29.0% TO 3.1% Lto 3.6% Lmdd -15.0%
   sweep: hl0: LS 2.80 Lshp 2.46 Lnet 16.1% TO 3.8% | hl1: LS 2.75 Lshp 2.55 Lnet 16.7% TO 3.4% | hl2: LS 2.62 Lshp 2.50 Lnet 16.6% TO 3.1% | hl3: LS 2.48 Lshp 2.41 Lnet 16.0% TO 2.8% | hl5: LS 2.33 Lshp 2.32 Lnet 15.4% TO 2.5% | hl10: LS 2.09 Lshp 2.14 Lnet 14.3% TO 2.0% | hl20: LS 1.96 Lshp 1.97 Lnet 13.2% TO 1.6%

f_max60 [books] hl_ls 0.0 hl_long 0.0 hl_used 0.0
   @hl_ls   train    LS +2.14 Lgross +15.9% Lnet +13.5% Lshp +1.98 short +21.0% TO 2.6% Lto 3.2% Lmdd -8.7%
   @hl_ls   valid    LS +3.64 Lgross +22.3% Lnet +20.4% Lshp +3.38 short +28.8% TO 2.0% Lto 2.5% Lmdd -3.7%
   sweep: hl0: LS 2.14 Lshp 1.98 Lnet 13.5% TO 2.6% | hl1: LS 2.00 Lshp 1.97 Lnet 13.4% TO 2.3% | hl2: LS 1.90 Lshp 1.87 Lnet 12.8% TO 2.1% | hl3: LS 1.80 Lshp 1.81 Lnet 12.3% TO 2.0% | hl5: LS 1.73 Lshp 1.75 Lnet 11.9% TO 1.9% | hl10: LS 1.51 Lshp 1.55 Lnet 10.5% TO 1.6% | hl20: LS 1.40 Lshp 1.37 Lnet 9.2% TO 1.3%

f_max60 [books_user] hl_ls 0.0 hl_long 0.0 hl_used 0.0
   @hl_ls   utrain   LS +2.52 Lgross +17.7% Lnet +15.5% Lshp +2.34 short +23.2% TO 2.4% Lto 3.0% Lmdd -8.7%
   @hl_ls   holdout  LS +2.39 Lgross +16.6% Lnet +14.7% Lshp +1.74 short +25.6% TO 2.1% Lto 2.5% Lmdd -11.8%
   sweep: hl0: LS 2.52 Lshp 2.34 Lnet 15.5% TO 2.4% | hl1: LS 2.40 Lshp 2.34 Lnet 15.5% TO 2.2% | hl2: LS 2.31 Lshp 2.28 Lnet 15.1% TO 2.0% | hl3: LS 2.23 Lshp 2.26 Lnet 15.0% TO 1.9% | hl5: LS 2.15 Lshp 2.21 Lnet 14.7% TO 1.8% | hl10: LS 1.95 Lshp 2.03 Lnet 13.5% TO 1.5% | hl20: LS 1.82 Lshp 1.81 Lnet 11.9% TO 1.3%
```

**10-03 23:36 · Bash** — Read study_tools API

```bash
cd /Users/wxy/Desktop/Partura && ls partura/ && wc -l partura/study_tools.py partura/books.py partura/diagnostics.py 2>/dev/null; sed -n 1,200p partura/study_tools.py
```

```
__init__.py
__pycache__
books.py
bridge.py
cli.py
decompose.py
diagnose.py
guard.py
lab.py
panels.py
probes.py
propose.py
remote_tools.py
report.py
report_legacy.py
runner.py
semantics.py
splits.py
study_tools.py
     131 partura/study_tools.py
     175 partura/books.py
     306 total
"""What a study's own analysis script needs, in one import.

A study often has a question no stock diagnostic answers -- "is the signal
only there on days the stock hit its limit?", "does the long leg survive if
the top 1% of names is dropped?".  Those analyses live in
``studies/<factor_id>/*.py`` and run on the server through
``scripts/study.sh exec``.  This module gives them the same panels, label,
splits and safety rails the runner uses, so a bespoke number is comparable
… (103 行略) …
        s = self.slice(split)
        p = np.asarray(panel[s], dtype=np.float64)
        return dg.ic_row(p, self.target()[s], sign=self.sign(panel) if sign is None else sign)

    def books(self, panel: np.ndarray, fit: str = "train", evals: Sequence[str] = ("train", "valid"),
              sign: Optional[float] = None) -> Dict[str, object]:
        """Decile L/S and the long leg, in the user's convention (see partura.books)."""
        sg = self.sign(panel, fit) if sign is None else sign
        return bk.books(sg * np.asarray(panel, dtype=np.float64), self.target(), self.slice(fit),
                        {e: self.slice(e) for e in evals},
                        cost=float(self.cfg.get("cost_per_side", bk.COST)),
                        top_frac=float(self.cfg.get("top_frac", bk.TOP_FRAC)),
                        rank_by=self.cfg.get("rank_by", "ls"))

    def rank_corr(self, a: np.ndarray, b: np.ndarray, split: str = "train") -> float:
        s = self.slice(split)
        return dg.pair_rank_corr(a[s], b[s])


__all__ = ["Study", "bk", "dg"]
```

**10-03 23:36 · Bash** — Read books.py and list diagnose functions

```bash
cd /Users/wxy/Desktop/Partura && cat partura/books.py && grep -n "^def \|^    def " partura/diagnose.py
```

```
"""The tradable-book metrics, in exactly the convention the user's tables use.

AlphaCube's current single-factor ranking (``scripts/pick_single_factors.py``)
judges a factor by two books built from a causally EMA-smoothed signal:

* a **decile long/short book** (gross 1), after 15 bp per unit turnover, and
* a **pure long book**: the long leg of that same decile book rescaled to
  weight 1, minus the equal-weight return of every stock that has both a
  signal and a label that day.  A holding whose label is missing (it opened
  locked at limit-up and could not have been bought) earns 0.

The half-life is chosen from {0, 1, 2, 3, 5, 10, 20} on the FIT period only,
by that book's own after-cost Sharpe, and then held fixed.

``stats`` and ``long_book`` are vendored from that script rather than imported
(the script lives in another session's working tree and changes under us); the
vendoring is guarded by a reproduction check against the user's published
table (``scripts/reproduce_table.py``), which is the only thing that makes a
Partura number comparable with one of theirs.

On top of that convention this module adds the two views a distillation needs:

* ``leg_anatomy`` -- how much of the spread is the long leg and how much is the
  short leg.  In A-shares the short leg cannot be traded, and a book whose
  spread is 80% short leg is a different object from one that is 80% long leg
  even when the two Sharpe ratios agree.
* ``quantile_profile`` -- mean next-day excess by signal quantile.  A decile
  book assumes "more signal is better"; the profile says whether that is true.
"""

… (145 行略) …
42:def _rank_rows_torch(x: np.ndarray, device: str, rows: int = 512) -> np.ndarray:
64:def rank_rows(x: np.ndarray) -> np.ndarray:
79:def ic_series(panel: np.ndarray, target: np.ndarray) -> np.ndarray:
83:def rank_ic_series(panel: np.ndarray, target: np.ndarray, *, panel_ranks: Optional[np.ndarray] = None,
95:def _ir(x: np.ndarray) -> float:
100:def _tstat(x: np.ndarray) -> float:
105:def sign_from(panel: np.ndarray, target: np.ndarray, use: str = "rank_ic",
113:def ic_row(panel: np.ndarray, target: np.ndarray, *, sign: float = 1.0,
136:def distinct_fraction(panel: np.ndarray, step: int = 5, min_names: int = 30) -> float:
149:def metric_row(panel: np.ndarray, target: np.ndarray, *, sign: float = 1.0,
162:    def curve(v: np.ndarray) -> Tuple[float, float]:
190:def _zrank(x: np.ndarray) -> np.ndarray:
197:def neutralise(panel: np.ndarray, controls: Dict[str, np.ndarray], space: str = "rank",
244:def conditional_ic(panel: np.ndarray, target: np.ndarray, gate: np.ndarray, buckets: int = 5,
271:def decay(panel: np.ndarray, targets: Dict[int, np.ndarray], sign: float = 1.0) -> List[Dict[str, float]]:
280:def by_year(panel: np.ndarray, target: np.ndarray, years: np.ndarray, *, sign: float = 1.0,
299:def extreme_day_dependence(panel: np.ndarray, target: np.ndarray, *, sign: float = 1.0,
318:def smoothing_sweep(panel: np.ndarray, target: np.ndarray, *, sign: float = 1.0,
341:def pair_rank_corr(a: np.ndarray, b: np.ndarray) -> float:
347:def rank_corr_matrix(panels: Dict[str, np.ndarray]) -> Dict[str, Dict[str, float]]:
```

**10-03 23:36 · Bash** — Read diagnose helpers

```bash
cd /Users/wxy/Desktop/Partura && sed -n 36,135p partura/diagnose.py && sed -n 186,275p partura/diagnose.py && sed -n 336,360p partura/diagnose.py
```

```
from alphacube.metrics import (apply_turnover_cap, cs_pearson, ema_rows, long_short_weights,  # noqa: E402
                               nanmean_quiet, portfolio_returns)
from alphacube.metrics import rank_rows as _rank_rows_pandas  # noqa: E402


def _rank_rows_torch(x: np.ndarray, device: str, rows: int = 512) -> np.ndarray:
    """``rank_rows`` on an accelerator: per-row average ranks (ties averaged) of
    the finite cells, NaN elsewhere -- the same answer as the pandas version
    (locked by tests/test_partura.py), without the CPU.  The server's CPU quota
    is usually taken by a neighbouring job while its GPU sits idle, and ranking
    a 1400 x 5200 panel is the single hottest call in a study."""
    import torch
    x = np.asarray(x, dtype=np.float64)
    out = np.empty(x.shape, dtype=np.float64)
    for a in range(0, x.shape[0], rows):
        t = torch.as_tensor(x[a:a + rows], device=device)
        fin = torch.isfinite(t)
        s, order = torch.sort(torch.where(fin, t, torch.full_like(t, float("inf"))), dim=1, stable=True)
        lo = torch.searchsorted(s, s, right=False)
        hi = torch.searchsorted(s, s, right=True)
        avg = (lo + hi + 1).to(torch.float64) / 2.0
        r = torch.empty_like(t).scatter_(1, order, avg)
        r[~fin] = float("nan")
        out[a:a + rows] = r.cpu().numpy()
    return out


def rank_rows(x: np.ndarray) -> np.ndarray:
    dev = os.environ.get("PARTURA_RANK_DEVICE", "")
    if dev:
… (164 行略) …
def pair_rank_corr(a: np.ndarray, b: np.ndarray) -> float:
    """Mean daily Spearman correlation -- AlphaCube's own family-identity metric."""
    return nanmean_quiet(cs_pearson(rank_rows(np.asarray(a, dtype=np.float64)),
                                    rank_rows(np.asarray(b, dtype=np.float64))))


def rank_corr_matrix(panels: Dict[str, np.ndarray]) -> Dict[str, Dict[str, float]]:
    names = list(panels)
    ranks = {n: rank_rows(np.asarray(panels[n], dtype=np.float64)) for n in names}
    out: Dict[str, Dict[str, float]] = {}
    # `out[a] = {}` used to reset a row that earlier pairs had already written
    # into, so the lower triangle came back empty (and half the report's table
    # read NaN). Build every row first, then fill both triangles.
    out = {n: {} for n in names}
    for i, a in enumerate(names):
        for b in names[i:]:
            v = nanmean_quiet(cs_pearson(ranks[a], ranks[b]))
            out[a][b] = v
            out[b][a] = v
    return out
```

**10-03 23:36 · Bash** — Read events.py analysis script

```bash
cd /Users/wxy/Desktop/Partura && sed -n 1,260p studies/F105_std_fangzheng_covamt/events.py
```

```
"""F105: what orders the root, and which kind of stock-day earns the money.

The root is  D = ts_stddev(C, 5),  C = cross_fangzheng(B, 241),  B = cross_max(A, 3),  A = day_cov(Amt, Amt).
The probes say D is "how much a one-year level statistic moved in the last 5 days", that it cannot tell a
spike ENTERING the window from the same spike LEAVING it 241 days later, and that an unfilled window
(a stock with < 241 observations) mechanically inflates the move.  No stock diagnostic separates those,
so this script measures them directly on train / valid (never the holdout):

  1  tails        how heavy-tailed is A through time, and how much of C is the std term / the single largest day
  2  ordering     what the cross-sectional order of D follows: level C, relative change D/C, amount, known family
  3  anatomy      the short and the long decile split by event kind: entry / exit(echo) / IPO-young / sample-start
  4  ic by kind   rank IC of -D inside each kind
  5  drop-one     the book at hl=3 with one kind of stock-day removed from the universe
  6  subsumption  the traded signal neutralised on the known family (and the reverse)
  7  long leg     overlap of the long decile with the lowest decile of amount / known family / level C
  8  two-way      conditional IC: relative change inside level buckets, level inside relative-change buckets
"""
import time

import numpy as np

from partura.study_tools import Study, bk, dg

FID = "F105_std_fangzheng_covamt"
A = "day_cov(Amt, Amt)"
B = f"cross_max({A}, 3)"
C = f"cross_fangzheng({B}, 241)"
D = f"ts_stddev({C}, 5)"
HL = 3.0
T0 = time.time()
… (181 行略) …
            qx, _ = deciles(-np.where(ok, np.asarray(x[sl], dtype=np.float64), np.nan), tgt[sl])
            row.append(f"{k} lowest-decile overlap {(lng & (qx == 9)).sum() / max(lng.sum(), 1):.1%}")
        say(f"  [{name}] " + "   ".join(row))
        with np.errstate(invalid="ignore"):
            say(f"  [{name}] mean percentile inside the long decile: amt {np.nanmean(np.where(lng, amt_pct[sl], np.nan)):.3f}"
                f"  cap {np.nanmean(np.where(lng, pct(cap)[sl], np.nan)):.3f}  turnrate {np.nanmean(np.where(lng, pct(turn)[sl], np.nan)):.3f}"
                f"  level C {np.nanmean(np.where(lng, pct(c)[sl], np.nan)):.3f}  rel change {np.nanmean(np.where(lng, pct(rel)[sl], np.nan)):.3f}"
                f"  ipo-young share {(lng & groups_raw['ipo-young'][sl]).sum() / max(lng.sum(), 1):.1%}")

    # ------------------------------------------------------------------ 8 two-way
    say("\n== 8 conditional rank IC (train, raw panels; sign as measured) ==")
    for name, x, g in (("relative change | level C", rel, c), ("level C | relative change", c, rel),
                       ("D | known_stdamt_max9", d, known), ("known_stdamt_max9 | D", known, d),
                       ("relative change | ctl_amt", rel, amt)):
        rows = dg.conditional_ic(x[tr], tgt[tr], np.asarray(g[tr], dtype=np.float64), buckets=5)
        say(f"  {name:<28} " + "  ".join(f"Q{r['bucket'] + 1} {r['rank_ic']:+.4f}" for r in rows))
    for name, x in (("level C", c), ("relative change D/C", rel), ("D", d), ("known_stdamt_max9", known)):
        say(f"  unconditional {name:<22} train {np.nanmean(dg.rank_ic_series(x[tr], tgt[tr])):+.4f}"
            f"   valid {np.nanmean(dg.rank_ic_series(x[va], tgt[va])):+.4f}")
    say(f"\ndone {time.time() - T0:.0f}s")
```

**10-03 23:36 · Bash** — List report headings

```bash
cd /Users/wxy/Desktop/Partura && grep -n "^#" research/alpha_distillation/F105_std_fangzheng_covamt.md | head -100
```

```
1:# Alpha 研究报告 — F105_std_fangzheng_covamt
11:## 1. 原始表达式
25:## 2. 算子的真实语义
29:### `day_cov`
37:### `cross_max`
46:### `cross_fangzheng`
55:### `ts_stddev`
86:### 既往研究留下的先验
112:## 3. 数学分解
154:## 4. 结构语法
178:## 5. 竞争性假设
206:## 6. 基线指标
301:## 7. 消融实验
303:### S0_baseline
319:### S1_what
364:### S1b_events
416:### S2_nodes
485:### S3_family
542:### S4_longleg
601:### S_final
659:### 中性化(fit 段)
782:### 条件 IC(fit 段)
811:### 控制变量自己当因子(同口径)
837:### 07x 直接量数据:根节点的排序跟着什么走,钱落在哪一类股票日上(`studies/F105_std_fangzheng_covamt/events.py`)
920:### 07x 多头腿为什么变好、经不经得起几个检查(`studies/F105_std_fangzheng_covamt/longleg.py`)
986:## 8. 语义变体
1064:## 9. 机制诊断
1066:### 一句话
1072:### 已确立(每条后面是能指到的实验)
1093:### 合理但没有坐实
1101:### 未决
1108:### 假设表的判决
1124:## 10. 蒸馏 / 升华后的候选
1137:### 结果
1154:### 留出段(20230808–20251231,只读了这一次;上面那张表,方向和半衰期都在用户训练段上定)
1188:### 为什么它比原式好用
1195:### 它没有比原式好的地方,以及限制
1202:## 11. 失效模式与风险
1222:## 12. 下一步实验
1236:## 附录 A — 数据段使用台账
1248:## 附录 B — 复现
1251:# S0_baseline: 182.4s, 峰值 anon 3.05 GiB, stages ['S0_baseline']
1252:# S1_what: 200.3s, 峰值 anon 3.33 GiB, stages ['S1_what']
1253:# S1b_S2_S3: 695.6s, 峰值 anon 4.69 GiB, stages ['S1_what', 'S2_nodes', 'S3_family']
1254:# S2S3_nodes_family: 411.4s, 峰值 anon 4.6 GiB, stages ['S1b_events', 'S2_nodes', 'S3_family']
1255:# S4_longleg: 169.8s, 峰值 anon 3.61 GiB, stages ['S4_longleg']
1256:# final: 165.2s, 峰值 anon 2.56 GiB, stages ['S_final']
```

**10-03 23:36 · Bash** — Read key report sections

```bash
cd /Users/wxy/Desktop/Partura && sed -n 1,24p research/alpha_distillation/F105_std_fangzheng_covamt.md && sed -n 601,660p research/alpha_distillation/F105_std_fangzheng_covamt.md && sed -n 782,836p research/alpha_distillation/F105_std_fangzheng_covamt.md && sed -n 1124,1160p research/alpha_distillation/F105_std_fangzheng_covamt.md
```

```
# Alpha 研究报告 — F105_std_fangzheng_covamt

> 分钟成交额方差的一年期 mean+std 水平在最近 5 天的变化量 —— 带成交额平方尺度的「放量事件进入/滑出一年窗口」探测器

**数据**: 1942 个交易日 × 5220 只股票 (20180102–20251231) · 标签 `open_vwap15` h=1(可买入:剔除次日开盘封涨停) · 成本 15 bp/单位换手 · 前/后 10% · AlphaCube `1698296` · Partura `36543cfd8cc8`

**数据段**: train 20180102–20211231 · valid 20220104–20230807 · utrain 20180102–20230807 · holdout 20230808–20251231 · full 20180102–20251231

> 决策用的数字:方向与 EMA 半衰期在 **train** 上定,在 valid 上确认。与用户表可比的数字:方向与半衰期在 **utrain**(用户的训练段)上定;holdout = 用户的测试段,只在最后读。

## 1. 原始表达式

```
ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5)
```

这条表达式是挖掘库的 #25:`ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5)`。
用户表里公布的一行是:方向 −1、EMA 半衰期 3、扣费多空夏普 训练 3.03 / 测试 2.24、多头腿毛超额 16.8% / 14.3%。
S0 用 Partura 自己求值复现了训练列(3.03、16.8%);留出段那一次(S_final)复现了测试列(2.24、14.3%)。

**一句话(读完源码之后)**:它是「**分钟成交额方差**(带成交额平方的尺度)的**一年期 mean+std 水平**,在**最近 5 天里动了多少**」——
也就是「最近一周有没有一个(按原始金额计)很大的放量日**进入**一年窗口,或者一年前的那个放量日**滑出**窗口」。
它不是一个「波动的波动」,名字里的两个 std 都不是收益的波动。

### S_final

**问题**: 只凭 train/valid 选出来的结论 ——「原式 = 已知家族的一个更吵的写法;换成 cross_max(day_std(Amt), 30) 多头腿更好」—— 在用户的测试段(20230808–20251231)上站不站得住?

| 变体 | 表达式 | 方向 | rank IC train/valid | 半衰期 | 扣费多空夏普 train/valid | 多头腿毛超额 train/valid | 多头腿净超额 train/valid | 多头占比 | 多空日换手 | 取值离散度 |
|---|---|---|---|---|---|---|---|---|---|---|
… (126 行略) …
```
cross_stddev(cross_stddev(day_cov(Amt, Amt), 241), 5)
```

**升华(读留出段之前定下的推荐,2 个算子)**

```
cross_max(day_std(Amt), 30)
```

它不是新因子:它是 F001 蒸馏出的已知家族 `cross_max(day_std(Amt), 9)` 换了一个更慢的窗口(与 d=9 的 rank 相关 0.85,与 `ctl_amt` 0.80)。
这次研究的结论是「原式的信息全在这个家族里,而这个家族里对纯多头最好用的成员在 d=15~60 的平台上」。

### 留出段(20230808–20251231,只读了这一次;上面那张表,方向和半衰期都在用户训练段上定)

| | 原式 | 提纯 `f_min3` | `f_max15` | **`f_max30`** | `f_max60` |
|---|---|---|---|---|---|
| 扣费多空夏普 训练 / 测试 | +3.03 / +2.24 | +3.30 / +2.72 | +3.08 / +2.70 | +2.80 / +2.39 | +2.52 / +2.39 |
| 多头腿毛超额 | +16.8% / +14.3% | +17.5% / +16.3% | +20.3% / +17.0% | +19.6% / +15.7% | +17.7% / +16.6% |
| **多头腿净超额** | +11.8% / **+8.9%** | +13.0% / +11.5% | +14.9% / +12.0% | +16.1% / **+12.5%** | +15.5% / +14.7% |
```

**10-03 23:36 · Bash** — Find how report includes notes

```bash
cd /Users/wxy/Desktop/Partura && grep -n "notes\|07x\|07_" partura/report.py | head -60
```

```
7:experiments) come from markdown fragments under ``notes/<factor_id>/``.
183:def build(config_path: str, out_root: Optional[str] = None, notes_dir: Optional[str] = None,
194:        return legacy_build(config_path, out_root=out_root, notes_dir=notes_dir, research_dir=research_dir)
202:    notes = Path(notes_dir or (PARTURA_ROOT / "notes")) / fid
210:        p = notes / f"{name}.md"
286:        L += [note(f"07_{sid}"), ""]
304:        L += ["", note("07_neutralise"), ""]
310:        L += ["", note("07_conditional"), ""]
320:        L += ["", note("07_controls"), ""]
321:    for extra in sorted(notes.glob("07x_*.md")) if notes.is_dir() else []:     # bespoke analyses of this study
```

**10-03 23:36 · Bash** — Read report build function

```bash
cd /Users/wxy/Desktop/Partura && sed -n 183,345p partura/report.py
```

```
def build(config_path: str, out_root: Optional[str] = None, notes_dir: Optional[str] = None,
          research_dir: Optional[str] = None) -> Path:
    from .runner import load_config
    cfg = load_config(config_path)
    for k, v in (cfg.get("splits") or {}).items():
        SPLITS[k] = (str(v[0]), str(v[1]))
    fid = cfg["factor_id"]
    out_dir = Path(out_root or (PARTURA_ROOT / "runs")) / fid
    runs = _load_runs(out_dir)
    if runs and not any("fit_split" in r for r in runs.values()):       # a study from before the book convention
        from .report_legacy import build as legacy_build
        return legacy_build(config_path, out_root=out_root, notes_dir=notes_dir, research_dir=research_dir)
    from .probes import load_study_probes
    for pf in (cfg.get("probes") or []):
        load_study_probes(pf if Path(pf).is_absolute() else PARTURA_ROOT / pf)

    results = _merged(runs)
    any_run = max(runs.values(), key=lambda r: len(r.get("splits_used", [])), default={})
    user = any_run.get("user_split") or cfg.get("user_split", "utrain")
    notes = Path(notes_dir or (PARTURA_ROOT / "notes")) / fid
    dec = decompose(cfg["expression"])
    diag = _diag(runs)
    ledger = Ledger(out_dir / "ledger.json")
    base_id = cfg.get("baseline_id", "v_base")
    pub = cfg.get("published")

    def note(name: str) -> str:
        p = notes / f"{name}.md"
        return p.read_text(encoding="utf-8").strip() if p.is_file() else ""

… (113 行略) …
    all_corr = out_dir / "rank_corr_all.json"
    rc = json.loads(all_corr.read_text(encoding="utf-8")) if all_corr.is_file() else diag.get("rank_corr_train")
    if isinstance(rc, dict) and rc:
        ids = [i for i in (cfg.get("corr_ids") or []) + (cfg.get("corr_with") or []) if i in rc] or list(rc)[:16]
        L += ["**变体之间(以及与控制变量)的日截面 rank 相关(fit 段)** — ≥0.95 在 AlphaCube 里算同一因子族", "",
              rank_corr_table(rc, ids), ""]
    L += [note("08_variants"), ""]

    L += [f"## {SECTIONS[8]}", "", note("09_diagnosis"), ""]
    L += [f"## {SECTIONS[9]}", ""]
    finals = [vid for vid, r in results.items() if "holdout" in (r.get("books_user") or {}).get("splits", {})]
    if finals:
        L += ["**最终对比,与用户表同口径**(留出段 = 用户的测试段)", "", user_table(results, finals, user, pub, base_id), ""]
    L += [note("10_distilled"), ""]
    L += [f"## {SECTIONS[10]}", "", note("11_risks"), ""]
    L += [f"## {SECTIONS[11]}", "", note("12_next"), ""]

    L += ["## 附录 A — 数据段使用台账", "", ledger.render_markdown(), ""]
    L += ["## 附录 B — 复现", "", "```bash"]
    for name, r in runs.items():
```

**10-03 23:37 · Bash** — Check server status and list operators

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh status 2>&1 | tail -15; ./scripts/study.sh ops '^(cs_|ts_|cross_)' 2>&1 | head -120
```

```
540353, 30176 MiB
container anon 4.8 GiB
gpu.lock slot0.lock slot1.lock slot2.lock # 搜索语法内的注册表算子(带 win 的需要窗口参数,写在最后一个位置):
  cross_argmax                       dt/cross/rolling      arity 1 axis D win [3, 5, 10, 15, 30, 60, 241]
  cross_argmin                       dt/cross/rolling      arity 1 axis D win [3, 5, 10, 15, 30, 60, 241]
  cross_autocorr_s1                  dt/cross/rolling      arity 1 axis D win [3, 5, 10, 15, 30, 60, 241]
  cross_corr                         dt/cross/pair_rolling arity 2 axis D win [3, 5, 10, 15, 30, 60, 241]
  cross_cov                          dt/cross/pair_rolling arity 2 axis D win [3, 5, 10, 15, 30, 60, 241]
  cross_decay_linear                 dt/cross/rolling      arity 1 axis D win [3, 5, 10, 15, 30, 60, 241]
  cross_delay                        dt/cross/rolling      arity 1 axis D win [3, 5, 10, 15, 30, 60, 241]
  cross_delta                        dt/cross/rolling      arity 1 axis D win [3, 5, 10, 15, 30, 60, 241]
  cross_fangzheng                    dt/cross/rolling      arity 1 axis D win [3, 5, 10, 15, 30, 60, 241]
  cross_hurst                        dt/cross/rolling      arity 1 axis D win [3, 5, 10, 15, 30, 60, 241]
  cross_max                          dt/cross/rolling      arity 1 axis D win [3, 5, 10, 15, 30, 60, 241]
  cross_mean                         dt/cross/rolling      arity 1 axis D win [3, 5, 10, 15, 30, 60, 241]
  cross_med                          dt/cross/rolling      arity 1 axis D win [3, 5, 10, 15, 30, 60, 241]
  cross_min                          dt/cross/rolling      arity 1 axis D win [3, 5, 10, 15, 30, 60, 241]
  cross_outlier_33                   dt/cross/rolling      arity 1 axis D win [3, 5, 10, 15, 30, 60, 241]  [boolean_output,trivial_boolean]
  cross_product                      dt/cross/rolling      arity 1 axis D win [3, 5, 10, 15, 30, 60, 241]
  cross_quantile_q25                 dt/cross/rolling      arity 1 axis D win [3, 5, 10, 15, 30, 60, 241]
  cross_quantile_q50                 dt/cross/rolling      arity 1 axis D win [3, 5, 10, 15, 30, 60, 241]
  cross_quantile_q75                 dt/cross/rolling      arity 1 axis D win [3, 5, 10, 15, 30, 60, 241]
  cross_rank                         dt/cross/rolling      arity 1 axis D win [3, 5, 10, 15, 30, 60, 241]
  cross_reg_fvalue                   dt/cross/pair_rolling arity 2 axis D win [3, 5, 10, 15, 30, 60, 241]
  cross_reg_tvalue                   dt/cross/pair_rolling arity 2 axis D win [3, 5, 10, 15, 30, 60, 241]
  cross_regalpha                     dt/cross/pair_rolling arity 2 axis D win [3, 5, 10, 15, 30, 60, 241]
  cross_regbeta                      dt/cross/pair_rolling arity 2 axis D win [3, 5, 10, 15, 30, 60, 241]
  cross_regres                       dt/cross/pair_rolling arity 2 axis D win [3, 5, 10, 15, 30, 60, 241]
  cross_scale                        dt/cross/rolling      arity 1 axis D win [3, 5, 10, 15, 30, 60, 241]
  cross_shift                        dt/cross/rolling      arity 1 axis D win [3, 5, 10, 15, 30, 60, 241]  [lookahead]
… (56 行略) …
  cross_outlier                      dt/cross  axis D reduces_m False
  cross_pooled_alpha                 dt/cross  axis D reduces_m False
  cross_pooled_beta                  dt/cross  axis D reduces_m False
  cross_pooled_resid1                dt/cross  axis D reduces_m False
  cross_quantile                     dt/cross  axis D reduces_m False
  cross_tail_hellinger               dt/cross  axis D reduces_m False
  cs_quantile                        nd/cs  axis S reduces_m False
  ts_all_mean                        nd/ts  axis D reduces_m False
  ts_autocorr                        nd/ts  axis D reduces_m False
  ts_column_nonnull_sum              nd/ts  axis D reduces_m False
  ts_denominator_k                   nd/ts  axis D reduces_m False
  ts_growth                          nd/ts  axis D reduces_m False
  ts_mean_rolling_multi              nd/ts  axis D reduces_m False
  ts_multiregbeta                    nd/ts  axis D reduces_m False
  ts_multiregres                     nd/ts  axis D reduces_m False
  ts_outlier                         nd/ts  axis D reduces_m False
  ts_quantile                        nd/ts  axis D reduces_m False
  ts_sparse_sum                      nd/ts  axis D reduces_m False
  ts_stddev_rolling_multi            nd/ts  axis D reduces_m False
  ts_tail_hellinger                  nd/ts  axis D reduces_m False
```

**10-03 23:37 · Bash** — Extract hl_long books for all family members from JSON

```bash
cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python - <<'EOF'
import json,glob
R={}
for f in ['S0_baseline','S1_what','S1b_S2_S3','S2S3_nodes_family','S4_longleg','final']:
    d=json.load(open(f'runs/F105_std_fangzheng_covamt/{f}.json'))
    for k,v in d['results'].items(): R[k]=v
    if f=='S4_longleg':
        print(d['diagnostics'].keys())
        pr=d['diagnostics'].get('profile',{})
        print({k:(list(v.keys()) if isinstance(v,dict) else type(v)) for k,v in pr.items()})
def f(b): 
    return f"LS {b['ls_sharpe']:+.2f} Lg {b['long_gross_ann']:+.1%} Ln {b['long_ann']:+.1%} Lshp {b['long_sharpe']:+.2f} TO {b['ls_turnover']:.1%}"
ids=['v_base','s2_min3','s1_known_stdamt9','s4_max15','s3_max20','s4_max30','s3_max60','s3_max120','s3_max241','s1_level','s1_relchg','s4_pos','s3_mean60','s4_mean20','s4_med60','s2_absdelta','s2_no_max3','s1_recent']
for k in ids:
    b=R[k]['books']
    print(f"\n{k}: hl_ls {b['hl_ls']} hl_long {b['hl_long']}")
    for s in ('train','valid'):
        print(f"   @hl_ls {s}: {f(b['splits'][s])}")
    for s,v in b.get('splits_at_hl_long',{}).items():
        print(f"   @hl_long {s}: {f(v)}")
EOF
```

```
dict_keys(['decay', 'neutralise', 'conditional', 'rank_corr_train'])
{}

v_base: hl_ls 3.0 hl_long 10.0
   @hl_ls train: LS +2.54 Lg +13.1% Ln +8.2% Lshp +1.32 TO 6.0%
   @hl_ls valid: LS +4.62 Lg +26.0% Ln +20.7% Lshp +3.82 TO 6.6%
   @hl_long train: LS +2.32 Lg +12.1% Ln +9.3% Lshp +1.49 TO 3.2%
   @hl_long valid: LS +4.08 Lg +20.8% Ln +18.2% Lshp +3.30 TO 3.3%

s2_min3: hl_ls 3.0 hl_long 10.0
   @hl_ls train: LS +2.84 Lg +14.3% Ln +9.9% Lshp +1.62 TO 5.9%
   @hl_ls valid: LS +4.80 Lg +25.5% Ln +20.9% Lshp +3.75 TO 6.5%
   @hl_long train: LS +2.62 Lg +13.8% Ln +11.1% Lshp +1.84 TO 3.3%
   @hl_long valid: LS +4.35 Lg +21.6% Ln +19.1% Lshp +3.56 TO 3.4%

s1_known_stdamt9: hl_ls 0.0 hl_long 5.0
   @hl_ls train: LS +2.47 Lg +16.9% Ln +9.3% Lshp +1.37 TO 8.5%
   @hl_ls valid: LS +4.44 Lg +24.9% Ln +18.5% Lshp +3.09 TO 7.7%
   @hl_long train: LS +2.17 Lg +17.1% Ln +13.7% Lshp +1.99 TO 4.2%
   @hl_long valid: LS +4.10 Lg +25.1% Ln +22.2% Lshp +3.59 TO 3.9%

s4_max15: hl_ls 0.0 hl_long 3.0
   @hl_ls train: LS +2.61 Lg +18.0% Ln +12.3% Lshp +1.81 TO 6.2%
   @hl_ls valid: LS +4.52 Lg +26.1% Ln +21.3% Lshp +3.56 TO 5.5%
   @hl_long train: LS +2.29 Lg +17.4% Ln +13.9% Lshp +2.04 TO 4.1%
   @hl_long valid: LS +4.04 Lg +25.1% Ln +22.1% Lshp +3.61 TO 3.8%

s3_max20: hl_ls 0.0 hl_long 3.0
   @hl_ls train: LS +2.54 Lg +17.4% Ln +12.6% Lshp +1.86 TO 5.2%
   @hl_ls valid: LS +4.35 Lg +24.9% Ln +20.9% Lshp +3.52 TO 4.5%
… (46 行略) …
   @hl_long train: LS +1.09 Lg +7.3% Ln +6.2% Lshp +0.91 TO 1.4%
   @hl_long valid: LS +3.00 Lg +19.4% Ln +18.4% Lshp +2.74 TO 1.2%

s2_absdelta: hl_ls 2.0 hl_long 10.0
   @hl_ls train: LS +2.57 Lg +15.7% Ln +9.8% Lshp +1.60 TO 6.8%
   @hl_ls valid: LS +4.64 Lg +26.6% Ln +20.2% Lshp +3.80 TO 7.7%
   @hl_long train: LS +2.44 Lg +13.7% Ln +11.4% Lshp +1.84 TO 2.9%
   @hl_long valid: LS +4.16 Lg +22.2% Ln +19.8% Lshp +3.59 TO 3.1%

s2_no_max3: hl_ls 3.0 hl_long 10.0
   @hl_ls train: LS +2.67 Lg +14.5% Ln +9.4% Lshp +1.49 TO 6.2%
   @hl_ls valid: LS +4.77 Lg +26.6% Ln +21.2% Lshp +3.85 TO 6.8%
   @hl_long train: LS +2.47 Lg +13.5% Ln +10.7% Lshp +1.70 TO 3.3%
   @hl_long valid: LS +4.27 Lg +22.0% Ln +19.3% Lshp +3.47 TO 3.4%

s1_recent: hl_ls 3.0 hl_long 5.0
   @hl_ls train: LS +2.31 Lg +16.6% Ln +10.8% Lshp +1.63 TO 6.7%
   @hl_ls valid: LS +3.97 Lg +22.3% Ln +17.2% Lshp +2.92 TO 6.2%
   @hl_long train: LS +2.21 Lg +16.1% Ln +11.8% Lshp +1.76 TO 5.1%
   @hl_long valid: LS +3.90 Lg +22.8% Ln +19.0% Lshp +3.17 TO 4.6%
```

**10-03 23:38 · Bash** — Locate local AlphaCube path

```bash
cd /Users/wxy/Desktop/Partura && cat partura/bridge.py | head -40; ls ~/Desktop | head -30
```

```
"""Locate and import AlphaCube, and record exactly which version was used.

Partura never reimplements AlphaCube's store, parser, engine, label or
backtest primitives -- it imports them.  The only thing this module adds is
provenance: every Partura artefact carries the AlphaCube commit, the store
path and the library versions it was produced with, so a number in a report
can always be traced back to the code that made it.
"""

from __future__ import annotations

import hashlib
import os
import subprocess
import sys
from pathlib import Path
from typing import Dict, Optional

PARTURA_ROOT = Path(__file__).resolve().parents[1]


def alphacube_root() -> Path:
    """`$ALPHACUBE_ROOT`, else the sibling directory of the Partura checkout."""
    env = os.environ.get("ALPHACUBE_ROOT")
    cands = [Path(env)] if env else []
    cands += [PARTURA_ROOT.parent / "AlphaCube", Path.home() / "Desktop" / "AlphaCube",
              Path("/root/autodl-tmp/AlphaCube")]
    for c in cands:
        if (c / "src" / "alphacube" / "__init__.py").is_file():
            return c.resolve()
… (20 行略) …
Partura
SIG-2027-Europe-答案册.html
SIG-2027-Europe-答案册.pdf
Texas Play
Xiangyu Wang SRC
__pycache__
code
factor_set_1_26.py
factor_set_merged.py
hrx+
hurst
legno.mov
p_r_v
proper_risk_taking
ps8
qmt_server_calculate
result
results
sharbox.mov
train_model
```

**10-03 23:38 · Bash** — Read ema_rows and long_short_weights (local copy)

```bash
cd /Users/wxy/Desktop/AlphaCube && grep -n "^def ema_rows" -A 30 src/alphacube/metrics.py | head -60; grep -n "^def long_short_weights" -A 30 src/alphacube/metrics.py | head -50
```

```
215:def ema_rows(panel: np.ndarray, halflife: float) -> np.ndarray:
216-    """Causal per-stock EMA along days: ``s_t = a * x_t + (1 - a) * s_t-1`` with
217-    ``a = 1 - 0.5 ** (1 / halflife)``. A missing day leaves the state as it was and
218-    is missing in the output (nothing to trade that day); a stock's first finite
219-    value starts its state. ``halflife <= 0`` returns the panel unchanged."""
220-    x = np.asarray(panel, dtype=np.float64)
221-    if halflife <= 0:
222-        return x
223-    a = 1.0 - 0.5 ** (1.0 / float(halflife))
224-    out = np.full_like(x, np.nan)
225-    state = np.full(x.shape[1], np.nan)
226-    for t in range(x.shape[0]):
227-        row = x[t]
228-        fin = np.isfinite(row)
229-        fresh = fin & ~np.isfinite(state)
230-        state = np.where(fresh, row, state)
231-        upd = fin & ~fresh
232-        state[upd] = a * row[upd] + (1.0 - a) * state[upd]
233-        out[t, fin] = state[fin]
234-    return out
235-
236-
237-def sampled_abs_corr(a: np.ndarray, b: np.ndarray, sample_days: int = 250) -> float:
238-    D = a.shape[0]
239-    idx = np.linspace(0, D - 1, num=min(sample_days, D)).astype(int)
240-    x, y = a[idx].reshape(-1), b[idx].reshape(-1)
241-    m = np.isfinite(x) & np.isfinite(y)
242-    if m.sum() < 2:
243-        return float("nan")
244-    x, y = x[m], y[m]
… (12 行略) …
293-    book in torch) that noise would also have been selected against."""
294-    alpha = np.asarray(alpha, dtype=np.float64)
295-    D, S = alpha.shape
296-    fin = np.isfinite(alpha)
297-    n = fin.sum(axis=1)
298-    order = np.argsort(np.where(fin, alpha, np.inf), axis=1, kind="stable")     # non-finite last
299-    k = np.maximum(1, np.floor(n * top_frac).astype(np.int64))
300-    pos = np.arange(S)[None, :]
301-    ok = (n >= 2)[:, None]
302-    long_ = ok & (pos >= (n - k)[:, None]) & (pos < n[:, None])
303-    short = ok & (pos < k[:, None])
304-    w_sorted = np.where(long_, 0.5 / k[:, None], np.where(short, -0.5 / k[:, None], 0.0))
305-    w = np.zeros((D, S), dtype=np.float64)
306-    np.put_along_axis(w, order, w_sorted, axis=1)
307-    return w
308-
309-
310-def apply_turnover_cap(target: np.ndarray, cap: Optional[float]) -> np.ndarray:
311-    """Walk the book forward, never trading more than ``cap`` in a day.
312-
```

**10-03 23:38 · Bash** — Read longleg.py analysis script

```bash
cd /Users/wxy/Desktop/Partura && sed -n 1,175p studies/F105_std_fangzheng_covamt/longleg.py
```

```
"""F105: why the slow members of the known family have a better long leg than the original,
and whether that survives the checks a long-only user cares about.

S3/S4 found that cross_max(day_std(Amt), d) for d = 15..60 has a long-leg net excess of 12-14% (train)
against the original's 8%, and that valid is a tie.  Before the holdout is read, four questions that no
stage table answers (train / valid only, never the holdout):

  1  subsumption   does the original add anything to cross_max(day_std(Amt), 30), or the reverse?
  2  long decile   how much do the two long deciles overlap, and what do the names only one of them holds earn?
  3  by year       is the long-leg advantage there year by year (2018..2023), or is it one year?
  4  capacity      does the advantage survive dropping the smallest 20% by float cap / by amount from the universe?
"""
import time

import numpy as np

from partura.study_tools import Study, bk, dg

FID = "F105_std_fangzheng_covamt"
EXPR = {
    "orig":   "ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5)",
    "min3":   "cross_stddev(cross_stddev(day_cov(Amt, Amt), 241), 5)",
    "max15":  "cross_max(day_std(Amt), 15)",
    "max30":  "cross_max(day_std(Amt), 30)",
    "max60":  "cross_max(day_std(Amt), 60)",
    "known9": "cross_max(day_std(Amt), 9)",
}
HL = {"orig": 3.0, "min3": 3.0, "max15": 0.0, "max30": 0.0, "max60": 0.0, "known9": 0.0}   # fitted on train (stage tables)
T0 = time.time()

… (106 行略) …
        sl = slice(int(idx[0]), int(idx[-1]) + 1)
        row = []
        for k in ("orig", "min3", "max15", "max30", "max60"):
            b = bk.book_row(sig[k], tgt, sl)
            row.append(f"{k} LS {b['ls_sharpe']:+.2f} Lnet {b['long_ann']:+.1%} Lshp {b['long_sharpe']:+.2f}")
        say(f"  {y} ({idx.size}d)  " + "  |  ".join(row))

    # ------------------------------------------------------------------ 4 capacity
    say("\n== 4 capacity: drop the smallest names from the universe, then rebuild both books ==")
    say("   (the universe changes day by day, so turnover and net are inflated the same way for every factor; compare within a row block)")
    masks = {"all names": np.ones_like(cap_p, dtype=bool),
             "cap pctile >= 0.2": cap_p >= 0.2,
             "cap pctile >= 0.5": cap_p >= 0.5,
             "amt pctile >= 0.2": amt_p >= 0.2}
    for mname, m in masks.items():
        for name, sl in (("train", tr), ("valid", va)):
            for k in ("orig", "max15", "max30", "max60"):
                b = bk.book_row(np.where(m, sig[k], np.nan), tgt, sl)
                say(f"  [{mname:<18}] [{name}] {k:<6} {fmt(b)}")
    say(f"\ndone {time.time() - T0:.0f}s")
```

**10-03 23:41 · 写文件** `/Users/wxy/Desktop/Partura/studies/F105_std_fangzheng_covamt/rev1.py`(20585 字符)

**10-03 23:42 · Bash** — Patch rev1.py and syntax-check it

```bash
cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python - <<'EOF'
import re
p='studies/F105_std_fangzheng_covamt/rev1.py'
s=open(p).read()
old='''        resid, info = dg.neutralise(sig(*y), {"x": sig(*x)})
        ics = "  ".join(f"[{name}] rIC {dg.ic_row(resid[sl], tgt[sl], sign=1.0)['rank_ic']:+.4f} (t {dg.ic_row(resid[sl], tgt[sl], sign=1.0)['rank_ic_t']:+.1f})"
                        for name, sl in SPL)
'''
new='''        resid, info = dg.neutralise(sig(*y), {"x": sig(*x)})
        icr = {name: dg.ic_row(resid[sl], tgt[sl], sign=1.0) for name, sl in SPL}
        ics = "  ".join(f"[{name}] rIC {icr[name]['rank_ic']:+.4f} (t {icr[name]['rank_ic_t']:+.1f})" for name, _ in SPL)
'''
assert old in s
s=s.replace(old,new)
old2='''    # ------------------------------------------------------------------ 1b equivalence
'''
new2='''    say("  -- the same, universe restricted to names with >= 247 observations (drops IPO-young names and all of 2018)")
    young0 = np.cumsum(np.isfinite(P["known9"]), axis=0) < 247
    for k in FAM:
        s = np.where(young0, np.nan, sig(k, HL_LONG[k]))
        say(f"  mature {k:<6} hl_long {HL_LONG[k]:>2.0f}  " + "   ".join(f"[{name}] {fmt(bk.book_row(s, tgt, sl))}" for name, sl in SPL))

    # ------------------------------------------------------------------ 1b equivalence
'''
assert old2 in s
s=s.replace(old2,new2)
open(p,'w').write(s)
EOF
~/.venvs/alphacube/bin/python -m py_compile studies/F105_std_fangzheng_covamt/rev1.py && echo compiled OK
```

```
compiled OK
```

**10-03 23:42 · Bash** — Start revision analysis script on server (train/valid only)

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh exec F105_std_fangzheng_covamt rev1 rev1.py 2>&1 | tail -5
```

```
started F105_std_fangzheng_covamt/rev1: rev1.py
```

**10-03 23:42 · Bash** — Get exact final.json numbers and file times

```bash
cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python - <<'EOF'
import json
d=json.load(open('runs/F105_std_fangzheng_covamt/final.json'))
r=d['results']
for k in r:
    b=r[k]['books_user']
    print(k, 'hl_ls',b['hl_ls'],'hl_long',b['hl_long'])
    print('   sweep long_sharpe:', [(w['halflife'], round(w['long_sharpe'],4), round(w['ls_sharpe'],4)) for w in b['sweep']])
    for nm in ('splits','splits_at_hl_long'):
        if nm in b:
            for s,v in b[nm].items():
                print(f"   {nm} {s}: LS {v['ls_sharpe']:.3f} Lg {v['long_gross_ann']*100:.2f} Ln {v['long_ann']*100:.2f} Lshp {v['long_sharpe']:.3f} short {v['short_gross_ann']*100:.2f} TO {v['ls_turnover']*100:.2f} Lmdd {v['long_mdd']*100:.2f} cost {100*(v['long_gross_ann']-v['long_ann']):.2f}")
# by-year in final
by=d['diagnostics'].get('by_year',{})
print(by.keys())
for k,v in by.items():
    print(k, [(x['year'], round(x['long_ann']*100,1), round(x.get('long_sharpe',float('nan')),2), round(x['ls_sharpe'],2)) for x in v])
EOF
stat -f "%Sm %N" -t "%H:%M:%S" notes/F105_std_fangzheng_covamt/07_S_final.md runs/F105_std_fangzheng_covamt/final.json; stat -f "%SB %N" -t "%H:%M:%S" notes/F105_std_fangzheng_covamt/07_S_final.md
```

```
f_orig hl_ls 3.0 hl_long 3.0
   sweep long_sharpe: [(0.0, 0.3503, 2.2496), (1.0, 1.3398, 2.7543), (2.0, 1.8446, 2.9928), (3.0, 1.9645, 3.0312), (5.0, 1.9584, 2.8859), (10.0, 1.959, 2.7435), (20.0, 1.6824, 2.411)]
   splits utrain: LS 3.031 Lg 16.79 Ln 11.75 Lshp 1.964 short 31.11 TO 6.11 Lmdd -9.63 cost 5.04
   splits holdout: LS 2.244 Lg 14.27 Ln 8.90 Lshp 1.038 short 32.60 TO 6.74 Lmdd -14.38 cost 5.37
f_min3 hl_ls 3.0 hl_long 10.0
   sweep long_sharpe: [(0.0, 0.6677, 2.445), (1.0, 1.6499, 3.0512), (2.0, 2.0916, 3.2766), (3.0, 2.1839, 3.3024), (5.0, 2.2096, 3.2275), (10.0, 2.2831, 3.0267), (20.0, 1.9946, 2.6867)]
   splits utrain: LS 3.302 Lg 17.51 Ln 13.04 Lshp 2.184 short 33.94 TO 6.05 Lmdd -9.67 cost 4.48
   splits holdout: LS 2.719 Lg 16.32 Ln 11.53 Lshp 1.330 short 37.81 TO 6.70 Lmdd -14.12 cost 4.78
   splits_at_hl_long utrain: LS 3.027 Lg 16.02 Ln 13.43 Lshp 2.283 short 27.13 TO 3.31 Lmdd -8.62 cost 2.59
   splits_at_hl_long holdout: LS 2.517 Lg 16.00 Ln 13.50 Lshp 1.735 short 27.88 TO 3.41 Lmdd -10.94 cost 2.50
f_max15 hl_ls 0.0 hl_long 3.0
   sweep long_sharpe: [(0.0, 2.2629, 3.0768), (1.0, 2.4125, 2.9634), (2.0, 2.4055, 2.8119), (3.0, 2.4468, 2.7287), (5.0, 2.3767, 2.5469), (10.0, 2.2538, 2.311), (20.0, 2.0771, 2.157)]
   splits utrain: LS 3.077 Lg 20.27 Ln 14.88 Lshp 2.263 short 37.85 TO 5.98 Lmdd -9.97 cost 5.39
   splits holdout: LS 2.697 Lg 17.00 Ln 12.00 Lshp 1.282 short 42.50 TO 5.67 Lmdd -15.59 cost 5.00
   splits_at_hl_long utrain: LS 2.729 Lg 19.58 Ln 16.24 Lshp 2.447 short 29.70 TO 4.02 Lmdd -9.60 cost 3.33
   splits_at_hl_long holdout: LS 2.302 Lg 16.35 Ln 13.26 Lshp 1.411 short 32.60 TO 3.84 Lmdd -15.85 cost 3.09
f_max30 hl_ls 0.0 hl_long 1.0
   sweep long_sharpe: [(0.0, 2.4601, 2.8007), (1.0, 2.5479, 2.7525), (2.0, 2.5036, 2.617), (3.0, 2.4146, 2.4769), (5.0, 2.3205, 2.3284), (10.0, 2.1351, 2.0876), (20.0, 1.9693, 1.961)]
   splits utrain: LS 2.801 Lg 19.61 Ln 16.06 Lshp 2.460 short 29.69 TO 3.82 Lmdd -8.84 cost 3.56
   splits holdout: LS 2.390 Lg 15.74 Ln 12.55 Lshp 1.375 short 31.96 TO 3.52 Lmdd -15.13 cost 3.19
   splits_at_hl_long utrain: LS 2.753 Lg 19.80 Ln 16.75 Lshp 2.548 short 27.88 TO 3.36 Lmdd -8.77 cost 3.06
   splits_at_hl_long holdout: LS 2.295 Lg 16.25 Ln 13.51 Lshp 1.473 short 29.01 TO 3.11 Lmdd -15.00 cost 2.75
f_max60 hl_ls 0.0 hl_long 0.0
   sweep long_sharpe: [(0.0, 2.3449, 2.5184), (1.0, 2.3365, 2.3981), (2.0, 2.2765, 2.3066), (3.0, 2.2575, 2.2258), (5.0, 2.2132, 2.1544), (10.0, 2.034, 1.9493), (20.0, 1.8134, 1.8208)]
   splits utrain: LS 2.518 Lg 17.72 Ln 15.48 Lshp 2.345 short 23.18 TO 2.37 Lmdd -8.70 cost 2.24
   splits holdout: LS 2.388 Lg 16.59 Ln 14.66 Lshp 1.737 short 25.55 TO 2.11 Lmdd -11.76 cost 1.92
dict_keys(['f_orig', 'f_min3', 'f_max15', 'f_max30', 'f_max60'])
f_orig [('2018', 13.6, 2.31, 3.44), ('2019', 6.0, 1.28, 2.6), ('2020', 3.0, 0.44, 1.5), ('2021', 9.6, 1.4, 2.74), ('2022', 26.0, 4.53, 5.91), ('2023', 15.8, 3.24, 4.0), ('2024', 4.7, 0.43, 1.66), ('2025', 7.7, 1.11, 1.99)]
f_min3 [('2018', 13.5, 2.34, 3.56), ('2019', 8.6, 1.92, 3.1), ('2020', 5.1, 0.76, 1.92), ('2021', 11.9, 1.69, 2.93), ('2022', 26.1, 4.39, 6.06), ('2023', 17.1, 3.42, 4.42), ('2024', 7.0, 0.64, 2.12), ('2025', 10.5, 1.48, 2.4)]
f_max15 [('2018', 21.6, 3.77, 4.25), ('2019', 13.0, 2.59, 3.27), ('2020', 3.3, 0.42, 1.43), ('2021', 10.8, 1.38, 2.17), ('2022', 23.8, 3.89, 5.5), ('2023', 18.9, 3.24, 3.95), ('2024', 8.5, 0.71, 2.52), ('2025', 11.4, 1.55, 2.18)]
f_max30 [('2018', 19.1, 3.3, 3.67), ('2019', 11.9, 2.42, 2.87), ('2020', 7.8, 0.98, 1.19), ('2021', 15.2, 1.97, 2.2), ('2022', 25.2, 4.05, 4.94), ('2023', 19.2, 3.33, 3.84), ('2024', 9.1, 0.8, 2.24), ('2025', 11.9, 1.58, 1.72)]
f_max60 [('2018', 18.2, 3.03, 3.29), ('2019', 10.9, 2.1, 1.99), ('2020', 6.8, 0.84, 1.17), ('2021', 17.6, 2.34, 2.29), ('2022', 23.1, 3.66, 4.32), ('2023', 19.6, 3.43, 3.59), ('2024', 11.6, 1.14, 2.26), ('2025', 13.2, 1.81, 1.69)]
23:12:01 notes/F105_std_fangzheng_covamt/07_S_final.md
23:11:00 runs/F105_std_fangzheng_covamt/final.json
23:07:46 notes/F105_std_fangzheng_covamt/07_S_final.md
```

**10-03 23:42 · Bash** — Wait for rev1 analysis to finish

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh wait F105_std_fangzheng_covamt rev1 540 2>&1 | tail -5; wc -l logs/F105_std_fangzheng_covamt_rev1.log
```

```
      profile hl 5 [train] -15.4% -12.7% -9.5% +0.4% +0.4% +2.4% +5.8% +7.0% +7.5% +14.1%
      profile hl 5 [valid] -28.2% -20.5% -11.6% -6.2% -1.3% +3.6% +9.0% +12.4% +17.7% +25.1%

done 550s
[partura exit 0 2026-10-04_14:51:36]
     440 logs/F105_std_fangzheng_covamt_rev1.log
```

**10-03 23:52 · Bash** — Read rev1 log part 1 (half-life grid)

```bash
cd /Users/wxy/Desktop/Partura && grep -av 'FutureWarning\|vmap(single_row)\|UserWarning' logs/F105_std_fangzheng_covamt_rev1.log | sed -n 1,95p
```

```
[panels] 1 new expression(s) on 1942d x 5220s (+0 warm-up), device=cuda, batches of 3
[panels] GPU: 1.4 GiB free of 31.4; this run capped at 3% (0.9 GiB), chunk 96 MiB
[panels]   1/1 (13s)
[panels] done in 13s
panels ready 15s; rows used 1359 (train slice(0, 973, None), valid slice(973, 1359, None)); symbols 5220
  selfcheck [train] orig@3  LS +2.54 Lg +13.1% Ln +8.2% Lshp +1.32 short +29.9% TO 6.0%
  selfcheck [train] max30@0 LS +2.37 Lg +17.4% Ln +13.6% Lshp +2.03 short +27.0% TO 4.0%
  selfcheck [valid] orig@3  LS +4.62 Lg +26.0% Ln +20.7% Lshp +3.82 short +34.2% TO 6.6%
  selfcheck [valid] max30@0 LS +4.12 Lg +25.3% Ln +22.2% Lshp +3.69 short +36.5% TO 3.5%

== 1 every factor at every half-life of the rule's grid (sign -1); *LS / *LONG = what each rule picks on train ==
  orig   hl  0           [train] LS +1.83 Lg +12.1% Ln -0.5% Lshp -0.09 short +32.2% TO 13.3%   [valid] LS +3.64 Lg +21.7% Ln +8.3% Lshp +1.60 short +38.8% TO 14.8%
  orig   hl  1           [train] LS +2.28 Lg +13.4% Ln +5.0% Lshp +0.83 short +31.7% TO 9.5%   [valid] LS +4.31 Lg +23.8% Ln +14.9% Lshp +2.82 short +37.9% TO 10.6%
  orig   hl  2           [train] LS +2.51 Lg +14.1% Ln +7.9% Lshp +1.29 short +30.6% TO 7.2%   [valid] LS +4.54 Lg +25.2% Ln +18.7% Lshp +3.47 short +36.0% TO 8.0%
  orig   hl  3 *LS       [train] LS +2.54 Lg +13.1% Ln +8.2% Lshp +1.32 short +29.9% TO 6.0%   [valid] LS +4.62 Lg +26.0% Ln +20.7% Lshp +3.82 short +34.2% TO 6.6%
  orig   hl  5           [train] LS +2.43 Lg +12.6% Ln +8.7% Lshp +1.40 short +26.9% TO 4.6%   [valid] LS +4.33 Lg +23.6% Ln +19.7% Lshp +3.56 short +31.4% TO 5.0%
  orig   hl 10 *LONG     [train] LS +2.32 Lg +12.1% Ln +9.3% Lshp +1.49 short +23.6% TO 3.2%   [valid] LS +4.08 Lg +20.8% Ln +18.2% Lshp +3.30 short +28.5% TO 3.3%
  orig   hl 20           [train] LS +1.96 Lg +9.8% Ln +7.7% Lshp +1.22 short +19.4% TO 2.3%   [valid] LS +3.90 Lg +17.9% Ln +16.2% Lshp +3.12 short +25.3% TO 2.2%
  min3   hl  0           [train] LS +2.13 Lg +13.6% Ln +1.6% Lshp +0.26 short +35.7% TO 13.7%   [valid] LS +3.52 Lg +23.1% Ln +10.0% Lshp +1.78 short +37.5% TO 15.7%
  min3   hl  1           [train] LS +2.62 Lg +14.7% Ln +7.3% Lshp +1.17 short +35.0% TO 9.4%   [valid] LS +4.50 Lg +24.8% Ln +16.8% Lshp +2.98 short +39.5% TO 10.7%
  min3   hl  2           [train] LS +2.81 Lg +14.9% Ln +9.5% Lshp +1.55 short +34.1% TO 7.1%   [valid] LS +4.84 Lg +25.9% Ln +20.1% Lshp +3.62 short +38.3% TO 7.9%
  min3   hl  3 *LS       [train] LS +2.84 Lg +14.3% Ln +9.9% Lshp +1.62 short +32.9% TO 5.9%   [valid] LS +4.80 Lg +25.5% Ln +20.9% Lshp +3.75 short +36.6% TO 6.5%
  min3   hl  5           [train] LS +2.78 Lg +13.7% Ln +10.2% Lshp +1.68 short +30.6% TO 4.6%   [valid] LS +4.65 Lg +24.0% Ln +20.4% Lshp +3.68 short +34.4% TO 5.0%
  min3   hl 10 *LONG     [train] LS +2.62 Lg +13.8% Ln +11.1% Lshp +1.84 short +26.0% TO 3.3%   [valid] LS +4.35 Lg +21.6% Ln +19.1% Lshp +3.56 short +30.0% TO 3.4%
  min3   hl 20           [train] LS +2.26 Lg +11.7% Ln +9.6% Lshp +1.56 short +21.6% TO 2.4%   [valid] LS +4.16 Lg +18.5% Ln +16.6% Lshp +3.38 short +26.8% TO 2.3%
  known9 hl  0 *LS       [train] LS +2.47 Lg +16.9% Ln +9.3% Lshp +1.37 short +37.7% TO 8.5%   [valid] LS +4.44 Lg +24.9% Ln +18.5% Lshp +3.09 short +48.1% TO 7.7%
  known9 hl  1           [train] LS +2.44 Lg +17.4% Ln +11.5% Lshp +1.69 short +34
… (968 字符略) …
0: R2 0.900 resid rIC +0.0028 (t +1.4) LSgross -1.83 Lg -10.1% short -3.2% TO 17.5%
      max30@0 | known9@5: R2 0.900 resid rIC +0.0148 (t +9.0) LSgross +2.91 Lg +5.8% short +12.8% TO 17.6%
  [valid] known9@5   ~ max30@0   rank corr 0.952  long-decile overlap 80.4%  short-decile overlap 79.2%
      known9@5 | max30@0: R2 0.907 resid rIC +0.0188 (t +5.1) LSgross +1.61 Lg +6.5% short +5.5% TO 17.0%
      max30@0 | known9@5: R2 0.907 resid rIC +0.0068 (t +2.4) LSgross -0.14 Lg +1.2% short -2.1% TO 17.2%
  [train] known9@5   ~ max30@1   rank corr 0.949  long-decile overlap 79.2%  short-decile overlap 80.6%
      known9@5 | max30@1: R2 0.902 resid rIC +0.0060 (t +2.8) LSgross -0.61 Lg -1.4% short -3.1% TO 13.9%
      max30@1 | known9@5: R2 0.902 resid rIC +0.0112 (t +6.4) LSgross +1.49 Lg +6.5% short +3.0% TO 13.9%
  [valid] known9@5   ~ max30@1   rank corr 0.953  long-decile overlap 80.5%  short-decile overlap 79.6%
      known9@5 | max30@1: R2 0.907 resid rIC +0.0226 (t +6.0) LSgross +2.43 Lg +11.9% short +6.3% TO 13.5%
      max30@1 | known9@5: R2 0.907 resid rIC +0.0028 (t +0.9) LSgross -1.38 Lg -0.7% short -8.6% TO 13.5%
  [train] known9@0   ~ max30@0   rank corr 0.847  long-decile overlap 60.5%  short-decile overlap 67.2%
      known9@0 | max30@0: R2 0.719 resid rIC +0.0283 (t +12.2) LSgross +1.88 Lg +7.0% short +7.7% TO 15.4%
      max30@0 | known9@0: R2 0.719 resid rIC +0.0037 (t +1.5) LSgross +0.37 Lg +6.0% short -3.3% TO 14.5%
  [valid] known9@0   ~ max30@0   rank corr 0.855  long-decile overlap 63.7%  short-decile overlap 65.3%
      known9@0 | max30@0: R2 0.732 resid rIC +0.0345 (t +9.1) LSgross +2.23 Lg +12.7% short +2.8% TO 14.7%
```

**10-03 23:52 · Bash** — Read rev1 log part 2 (equivalence, residuals, combos)

```bash
cd /Users/wxy/Desktop/Partura && grep -av 'FutureWarning\|vmap(single_row)\|UserWarning' logs/F105_std_fangzheng_covamt_rev1.log | sed -n 95,215p
```

```
      known9@0 | max30@0: R2 0.732 resid rIC +0.0345 (t +9.1) LSgross +2.23 Lg +12.7% short +2.8% TO 14.7%
      max30@0 | known9@0: R2 0.732 resid rIC +0.0078 (t +2.0) LSgross +0.32 Lg +9.2% short -7.0% TO 13.9%
  [train] max15@3    ~ max30@1   rank corr 0.953  long-decile overlap 80.1%  short-decile overlap 82.2%
      max15@3 | max30@1: R2 0.908 resid rIC +0.0064 (t +3.5) LSgross -0.36 Lg +1.4% short -3.7% TO 15.1%
      max30@1 | max15@3: R2 0.908 resid rIC +0.0114 (t +6.7) LSgross +1.32 Lg +7.5% short -0.1% TO 15.0%
  [valid] max15@3    ~ max30@1   rank corr 0.955  long-decile overlap 81.0%  short-decile overlap 81.2%
      max15@3 | max30@1: R2 0.912 resid rIC +0.0210 (t +6.3) LSgross +2.69 Lg +12.5% short +5.2% TO 14.4%
      max30@1 | max15@3: R2 0.912 resid rIC +0.0055 (t +1.9) LSgross -1.07 Lg +2.1% short -8.5% TO 14.3%
  [train] max60@0    ~ max30@1   rank corr 0.885  long-decile overlap 66.7%  short-decile overlap 74.7%
      max60@0 | max30@1: R2 0.786 resid rIC +0.0089 (t +4.2) LSgross +0.49 Lg +9.9% short -6.8% TO 10.4%
      max30@1 | max60@0: R2 0.786 resid rIC +0.0164 (t +8.0) LSgross +0.83 Lg +9.7% short -4.2% TO 11.3%
  [valid] max60@0    ~ max30@1   rank corr 0.883  long-decile overlap 67.6%  short-decile overlap 72.9%
      max60@0 | max30@1: R2 0.781 resid rIC +0.0043 (t +1.2) LSgross -0.33 Lg +8.8% short -11.0% TO 7.8%
      max30@1 | max60@0: R2 0.781 resid rIC +0.0306 (t +8.3) LSgross +2.27 Lg +14.0% short +1.4% TO 8.7%
  [train] min3@10    ~ max30@1   rank corr 0.712  long-decile overlap 44.1%  short-decile overlap 60.0%
      min3@10 | max30@1: R2 0.517 resid rIC +0.0130 (t +7.3) LSgross +0.06 Lg +5.3% short -5.0% TO 5.9%
      max30@1 | min3@10: R2 0.516 resid rIC +0.0200 (t +6.9) LSgross +1.37 Lg +11.2% short +1.0% TO 6.3%
  [valid] min3@10    ~ max30@1   rank corr 0.634  long-decile overlap 38.2%  short-decile overlap 53.4%
      min3@10 | max30@1: R2 0.404 resid rIC +0.0113 (t +3.8) LSgross +0.04 Lg +8.0% short -7.8% TO 5.1%
      max30@1 | min3@10: R2 0.404 resid rIC +0.0398 (t +8.5) LSgross +2.49 Lg +15.2% short +5.1% TO 5.2%
  [train] orig@10    ~ max30@1   rank corr 0.739  long-decile overlap 47.2%  short-decile overlap 61.0%
      orig@10 | max30@1: R2 0.553 resid rIC +0.0104 (t +5.6) LSgross -0.07 Lg +4.5% short -4.9% TO 7.0%
      max30@1 | orig@10: R2 0.553 resid rIC +0.0216 (t +7.6) LSgross +1.70 Lg +10.4% short +4.2% TO 7.5%
  [valid] orig@10    ~ max30@1   rank corr 0.681  long-decile overlap 42.9%  short-decile overlap 55.4%
      orig@10 | max30@1: R2 0.465 resid rIC +0.0096 (t +3.2) LSgross +0.30 Lg +9.3% short -7.5% TO 6.2%
      max30@1 | orig@10: R2 0.465 resid rIC +0.0393 (t +8.6) LSgross +2.53 Lg +14.5% short +5.1% TO 6.5%
  [train] min3@10    ~ known9@5  rank corr 0.699  long-decile overlap 43.1%  short-decile overlap 57.5%
      min3@10 | known9@5: R2 0.497 resid rIC +0.0119 (t +6.1) LSgross +0.36 Lg +6.8% short -4.2% TO 5.6%
      known9@5 | min3@10: R2 0.496 resid rIC +0.0215 (t +6.6) LSgross +1.07 Lg +10.8% short +0.2% TO 6.1%
  [valid] min3@10    ~ known9@5  rank corr 0.625  long-decile overlap 37.8%  short-decile overlap 52.6%
… (71 行略) …
  min3@10 + max30@1            [train] LS +2.52 Lg +15.2% Ln +12.5% Lshp +1.91 short +28.9% TO 3.3%   [valid] LS +4.33 Lg +24.2% Ln +21.7% Lshp +3.83 short +37.3% TO 3.1%
      alo
… (1571 字符略) …
 +1.91 Lg +10.6% Ln +8.0% Lshp +1.53 short +22.9% TO 4.7%   [valid] LS +3.22 Lg +19.9% Ln +17.4% Lshp +3.27 short +31.4% TO 4.3%
      alone max30@1            [train] LS +2.33 Lg +17.7% Ln +14.5% Lshp +2.15 short +25.0% TO 3.5%   [valid] LS +4.03 Lg +25.0% Ln +22.3% Lshp +3.66 short +35.0% TO 3.1%
  CONTROL known9@5 + max30@1   [train] LS +2.27 Lg +17.4% Ln +14.3% Lshp +2.09 short +25.7% TO 3.6%   [valid] LS +4.02 Lg +24.9% Ln +22.2% Lshp +3.61 short +37.0% TO 3.3%
      alone known9@5           [train] LS +2.17 Lg +17.1% Ln +13.7% Lshp +1.99 short +25.5% TO 4.2%   [valid] LS +4.10 Lg +25.1% Ln +22.2% Lshp +3.59 short +39.5% TO 3.9%
      alone max30@1            [train] LS +2.33 Lg +17.7% Ln +14.5% Lshp +2.15 short +25.0% TO 3.5%   [valid] LS +4.03 Lg +25.0% Ln +22.3% Lshp +3.66 short +35.0% TO 3.1%
  CONTROL max15@3 + max60@0    [train] LS +2.28 Lg +17.1% Ln +14.3% Lshp +2.08 short +25.2% TO 3.2%   [valid] LS +4.00 Lg +24.4% Ln +22.1% Lshp +3.57 short +35.8% TO 2.9%
      alone max15@3            [train] LS +2.29 Lg +17.4% Ln +13.9% Lshp +2.04 short +26.6% TO 4.1%   [valid] LS +4.04 Lg +25.1% Ln +22.1% Lshp +3.61 short +37.5% TO 3.8%
      alone max60@0            [train] LS +2.14 Lg +15.9% Ln +13.5% Lshp +1.98 short +21.0% TO 2.6%   [valid] LS +3.64 Lg +22.3% Ln +20.4% Lshp +3.38 short +28.8% TO 2.0%
  CONTROL known9@5 + max60@0   [train] LS +2.25 Lg +16.9% Ln +14.2% Lshp +2.05 short +25.0% TO 3.2%   [valid] LS +3.96 Lg +24.7% Ln +22.4% Lshp +3.60 short +35.3% TO 2.9%
      alone known9@5           [train] LS +2.17 Lg +17.1% Ln +13.7% Lshp +1.99 short +25.5% TO 4.2%   [valid] LS +4.10 Lg +25.1% Ln +22.2% Lshp +3.59 short +39.5% TO 3.9%
```

**10-03 23:52 · Bash** — Read rev1 log part 3 (combos, expression-level, deciles, direction)

```bash
cd /Users/wxy/Desktop/Partura && grep -av 'FutureWarning\|vmap(single_row)\|UserWarning' logs/F105_std_fangzheng_covamt_rev1.log | sed -n 215,300p
```

```
      alone known9@5           [train] LS +2.17 Lg +17.1% Ln +13.7% Lshp +1.99 short +25.5% TO 4.2%   [valid] LS +4.10 Lg +25.1% Ln +22.2% Lshp +3.59 short +39.5% TO 3.9%
      alone max60@0            [train] LS +2.14 Lg +15.9% Ln +13.5% Lshp +1.98 short +21.0% TO 2.6%   [valid] LS +3.64 Lg +22.3% Ln +20.4% Lshp +3.38 short +28.8% TO 2.0%
  CONTROL orig@10 + min3@10    [train] LS +2.46 Lg +13.4% Ln +10.7% Lshp +1.72 short +24.3% TO 3.3%   [valid] LS +4.22 Lg +21.7% Ln +19.2% Lshp +3.54 short +28.6% TO 3.3%
      alone orig@10            [train] LS +2.32 Lg +12.1% Ln +9.3% Lshp +1.49 short +23.6% TO 3.2%   [valid] LS +4.08 Lg +20.8% Ln +18.2% Lshp +3.30 short +28.5% TO 3.3%
      alone min3@10            [train] LS +2.62 Lg +13.8% Ln +11.1% Lshp +1.84 short +26.0% TO 3.3%   [valid] LS +4.35 Lg +21.6% Ln +19.1% Lshp +3.56 short +30.0% TO 3.4%
  -- by year for the long-rule pair min3@10 + max30@1 against max30@1 alone and min3@10 alone: Ln / Lshp
  2018 (243d)  combo +18.1%/+3.02  |  max30@1 +21.7%/+3.70  |  min3@10 +15.0%/+2.54
  2019 (244d)  combo +6.5%/+1.25  |  max30@1 +11.6%/+2.37  |  min3@10 +6.5%/+1.33
  2020 (243d)  combo +6.8%/+0.93  |  max30@1 +8.1%/+1.02  |  min3@10 +7.5%/+1.13
  2021 (243d)  combo +18.1%/+2.44  |  max30@1 +16.1%/+2.10  |  min3@10 +15.2%/+2.28
  2022 (242d)  combo +27.1%/+4.55  |  max30@1 +25.3%/+4.02  |  min3@10 +25.3%/+4.44
  2023 (144d)  combo +12.3%/+2.42  |  max30@1 +17.0%/+2.98  |  min3@10 +8.5%/+1.80

== 2c as an expression: add(cs_rank(-a), cs_rank(-b)) on RAW panels, half-life picked by the rule ==
  orig + max30             fit train  hl_ls 0 hl_long 2
      @hl_ls   [train] LS +2.52 Lg +16.9% Ln +9.6% Lshp +1.47 short +36.3% TO 8.6%   [valid] LS +4.50 Lg +26.1% Ln +18.6% Lshp +3.26 short +46.7% TO 9.3%
      @hl_long [train] LS +2.06 Lg +15.9% Ln +11.4% Lshp +1.73 short +24.7% TO 5.4%   [valid] LS +4.04 Lg +25.8% Ln +21.2% Lshp +3.66 short +37.0% TO 5.8%
  orig + max30             fit utrain hl_ls 0 hl_long 2
      @hl_ls   [utrain] LS +2.99 Lg +19.5% Ln +12.2% Lshp +1.93 short +39.3% TO 8.7%
      @hl_long [utrain] LS +2.55 Lg +18.7% Ln +14.2% Lshp +2.23 short +28.2% TO 5.5%
  min3 + max30             fit train  hl_ls 0 hl_long 2
      @hl_ls   [train] LS +2.58 Lg +16.5% Ln +9.2% Lshp +1.40 short +38.6% TO 9.1%   [valid] LS +4.46 Lg +26.4% Ln +18.8% Lshp +3.18 short +47.4% TO 10.1%
      @hl_long [train] LS +2.14 Lg +16.2% Ln +11.7% Lshp +1.78 short +25.7% TO 5.4%   [valid] LS +4.12 Lg +25.9% Ln +21.5% Lshp +3.66 short +38.0% TO 5.9%
  min3 + max30             fit utrain hl_ls 0 hl_long 2
      @hl_ls   [utrain] LS +3.03 Lg +19.3% Ln +11.9% Lshp +1.87 short +41.1% TO 9.4%
      @hl_long [utrain] LS +2.63 Lg +18.9% Ln +14.5% Lshp +2.27 short +29.2% TO 5.5%
  min3 + max60             fit train  hl_ls 0 hl_long 2
      @hl_ls   [train] LS +2.38 Lg +15.4% Ln +8.2% Lshp +1.26 short +34.1% TO 8.4%   [valid] LS +4.31 Lg +25.1% Ln +17.6% Lshp +3.03 short +44.1% TO 9.5%
      @hl_long [train] LS +1.94 Lg +15.2% Ln +10.9% Lshp +1.66 short +21.9% TO 5.0%   [valid] LS +3.94 Lg +24.5% Ln +20.1% Lshp +3.42 short +34.9% TO 5.5%
  min3 + max60             fit utrain hl_ls 0 hl_long 5
… (36 行略) …
  [train] the original's short decile (traded signal, hl 3), groups as in events.py 3b:
      entry (C rising)   names/day  118.0  raw excess -38.7%  amount-m
… (1032 字符略) …
tched  +2.5% max30-matched  +1.1% amt pct 0.42
      bottom half  C rising: n  719.7 raw  +6.6% amt-matched  +5.8% max30-matched  +7.1% amt pct 0.49   |   C falling: n  544.1 raw  +9.8% amt-matched  +5.3% max30-matched  +4.4% amt pct 0.35
  [valid] the original's short decile (traded signal, hl 3), groups as in events.py 3b:
      entry (C rising)   names/day  161.4  raw excess -62.5%  amount-matched -24.4%  max30-matched -25.0%  amt pctile 0.91
      exit (C falling)   names/day  218.6  raw excess -13.0%  amount-matched  +6.2%  max30-matched  +1.9%  amt pctile 0.72
      young              names/day   77.8  raw excess -35.3%  amount-matched -24.3%  max30-matched -19.0%  amt pctile 0.69
      whole decile       names/day  458.4  raw excess -34.6%  amount-matched  -9.9%  max30-matched -11.4%  amt pctile 0.78
  [valid] scale-free |D/C| (mature names), by the sign of the 5-day change of C:
      top decile   C rising: n  176.7 raw -61.3% amt-matched -38.0% max30-matched -42.2% amt pct 0.79   |   C falling: n  240.8 raw  +2.7% amt-matched  -0.3% max30-matched  -2.0% amt pct 0.46
      9th decile   C rising: n  172.2 raw -23.2% amt-matched  -5.5% max30-matched -10.8% amt pct 0.73   |   C falling: n  246.2 raw  +1.8% amt-matched  +1.2% max30-matched  -0.8% amt pct 0.49
      deciles 6-8  C rising: n  547.7 raw -11.8% amt-matched  -0.7% max30-matched  -3.3% amt pct 0.66   |   C falling: n  708.2 raw  -0.1% amt-matched  -2.1% max30-matched  -3.5% amt pct 0.48
      bottom half  C rising: n 1108.6 raw +10.3% amt-matched  +8.5% max30-matched +11.5% amt pct 0.50   |   C falling: n  984.4 raw +11.0% amt-matched  +3.6% max30-matched  +4.7% amt pct 0.40
```

**10-03 23:52 · Bash** — Read rev1 log part 4 (pre-event buckets, event half)

```bash
cd /Users/wxy/Desktop/Partura && grep -av 'FutureWarning\|vmap(single_row)\|UserWarning' logs/F105_std_fangzheng_covamt_rev1.log | sed -n 300,440p
```

```
      bottom half  C rising: n 1108.6 raw +10.3% amt-matched  +8.5% max30-matched +11.5% amt pct 0.50   |   C falling: n  984.4 raw +11.0% amt-matched  +3.6% max30-matched  +4.7% amt pct 0.40

== 4 conditional rank IC of the event half inside quintiles of a level (negative = same direction as the factor) ==
  [train] D/C all names                | today's amount (endogenous)          -0.0098  -0.0117  -0.0141  -0.0215  -0.0408   names 722/722/721/722/721
  [train] D/C all names                | known9 (endogenous)                  -0.0074  -0.0064  -0.0092  -0.0156  -0.0437   names 722/722/721/722/721
  [train] D/C all names                | one-year level C                     -0.0167  -0.0241  -0.0279  -0.0321  -0.0270   names 722/722/721/722/721
  [train] D/C all names                | PRE-EVENT 60d median amount, lag 10  -0.0344  -0.0295  -0.0258  -0.0183  -0.0169   names 713/712/712/712/712
  [train] D/C all names                | PRE-EVENT one-day amount, lag 10     -0.0286  -0.0278  -0.0235  -0.0216  -0.0205   names 713/712/712/712/712
  [train] D/C all names                | float cap                            -0.0371  -0.0312  -0.0298  -0.0224  -0.0113   names 722/722/721/722/721
  [train] D/C mature                   | today's amount (endogenous)          -0.0103  -0.0124  -0.0138  -0.0191  -0.0394   names 722/722/721/722/721
  [train] D/C mature                   | known9 (endogenous)                  -0.0065  -0.0055  -0.0069  -0.0117  -0.0437   names 722/722/721/722/721
  [train] D/C mature                   | one-year level C                     -0.0202  -0.0320  -0.0359  -0.0395  -0.0240   names 722/722/721/722/721
  [train] D/C mature                   | PRE-EVENT 60d median amount, lag 10  -0.0374  -0.0355  -0.0310  -0.0196  -0.0086   names 713/712/712/712/712
  [train] D/C mature                   | PRE-EVENT one-day amount, lag 10     -0.0306  -0.0306  -0.0262  -0.0205  -0.0181   names 713/712/712/712/712
  [train] D/C mature                   | float cap                            -0.0313  -0.0359  -0.0340  -0.0232  -0.0125   names 722/722/721/722/721
  [train] D/C mature, C rising only    | today's amount (endogenous)          -0.0235  -0.0200  -0.0218  -0.0264  -0.0431   names 722/722/721/722/721
  [train] D/C mature, C rising only    | known9 (endogenous)                  -0.0130  -0.0094  -0.0110  -0.0149  -0.0458   names 722/722/721/722/721
  [train] D/C mature, C rising only    | one-year level C                     -0.0341  -0.0432  -0.0464  -0.0502  -0.0292   names 722/722/721/722/721
  [train] D/C mature, C rising only    | PRE-EVENT 60d median amount, lag 10  -0.0631  -0.0541  -0.0455  -0.0268  -0.0097   names 713/712/712/712/712
  [train] D/C mature, C rising only    | PRE-EVENT one-day amount, lag 10     -0.0568  -0.0496  -0.0398  -0.0290  -0.0216   names 713/712/712/712/712
  [train] D/C mature, C rising only    | float cap                            -0.0564  -0.0550  -0.0506  -0.0317  -0.0171   names 722/722/721/722/721
  [train] D/C mature, C falling only   | today's amount (endogenous)          -0.0077  -0.0113  -0.0115  -0.0119  -0.0217   names 722/722/721/722/721
  [train] D/C mature, C falling only   | known9 (endogenous)                  -0.0062  -0.0095  -0.0077  -0.0136  -0.0238   names 722/722/721/722/721
  [train] D/C mature, C 
… (1652 字符略) …
alid] LS +2.91 Lg +20.4% Ln +17.6% Lshp +3.24 short +13.8% TO 4.5%
      profile hl 5 [train] -20.2% -7.2% -2.8% +1.7% +0.0% +2.2% +3.7% +4.4% +6.6% +11.7%
      profile hl 5 [valid] -17.9% -7.9% -6.7% -2.9% -3.9% +0.1% +0.0% +7.7% +11.0% +20.4%
  orig mature only   hl  1  [train] LS +1.37 Lg +12.5% Ln +2.9% Lshp +0.49 short +27.5% TO 8.8%   [valid] LS +4.16 Lg +25.4% Ln +16.4% Lshp +3.09 short +38.6% TO 11.3%
  orig mature only   hl  5  [train] LS +1.72 Lg +11.3% Ln +7.3% Lshp +1.19 short +24.1% TO 3.9%   [valid] LS +4.18 Lg +25.4% Ln +21.6% Lshp +3.86 short +31.1% TO 5.1%
  orig mature only   hl 10  [train] LS +1.72 Lg +11.7% Ln +9.1% Lshp +1.48 short +20.5% TO 2.6%   [valid] LS +3.97 Lg +22.2% Ln +19.7% Lshp +3.56 short +28.2% TO 3.3%
      profile hl 5 [train] -24.3% -12.7% -7.2% -2.5% +1.9% +4.2% +5.7% +10.3% +13.1% +11.6%
      profile hl 5 [valid] -31.5% -18.4% -11.1% -5.0% +2.3% +2.8% +6.5% +11.9% +15.7% +26.8%
  max30 mature only  hl  1  [train] LS +1.58 Lg +14.7% Ln +11.7% Lshp +1.71 short +21.0% TO 2.5%   [valid] LS +3.93 Lg +24.9% Ln +22.2% Lshp +3.66 short +34.7% TO 3.1%
  max30 mature only  hl  5  [train] LS +1.29 Lg +13.5% Ln +11.3% Lshp +1.65 short +15.1% TO 1.9%   [valid] LS +3.33 Lg +22.7% Ln +20.7% Lshp +3.33 short +28.2% TO 2.4%
  max30 mature only  hl 10  [train] LS +1.10 Lg +11.8% Ln +10.1% Lshp +1.48 short +12.1% TO 1.5%   [valid] LS +3.17 Lg +22.4% Ln +20.9% Lshp +3.32 short +25.5% TO 1.9%
      profile hl 5 [train] -15.4% -12.7% -9.5% +0.4% +0.4% +2.4% +5.8% +7.0% +7.5% +14.1%
      profile hl 5 [valid] -28.2% -20.5% -11.6% -6.2% -1.3% +3.6% +9.0% +12.4% +17.7% +25.1%

done 550s
[partura exit 0 2026-10-04_14:51:36]
```

**10-03 23:54 · Bash** — Inspect how the label is built in panels.py

```bash
cd /Users/wxy/Desktop/Partura && grep -n "buyable\|def target\|label_kind\|def external\|def split_slice\|_target" partura/panels.py | head -50
```

```
106:                 label_kind: str = "open_vwap15", label_buyable: bool = False,
123:        self.label_kind, self.label_buyable = label_kind, bool(label_buyable)
135:        self._targets: Dict[int, np.ndarray] = {}
175:    def target(self, horizon: int = 1) -> np.ndarray:
176:        if horizon not in self._targets:
177:            tag = f"__label__|{self.label_kind}|h{horizon}|buyable{int(self.label_buyable)}"
180:                self._targets[horizon] = np.load(p)
181:                return self._targets[horizon]
183:                self._price = Label(self.label_kind, 1).price(self.view)
184:            full = Label(self.label_kind, horizon).compute(self.view, price=self._price.copy())
185:            if self.label_buyable:
186:                # Same rule as Label(buyable=True) -- a name that opens locked at
198:            self._targets[horizon] = t
201:        return self._targets[horizon]
203:    def external(self, path: str) -> np.ndarray:
351:    def split_slice(self, split: str) -> slice:
```

**10-03 23:54 · Bash** — Read PanelSet constructor and target()

```bash
cd /Users/wxy/Desktop/Partura && sed -n 100,202p partura/panels.py
```

```
class PanelSet:
    def __init__(self, store_path: str, start: str, end: str, *, warmup: int = 60,
                 device: str = "cpu", chunk_symbols: Optional[int] = None, chunk_days: Optional[int] = None,
                 cache_dir: Optional[str] = None, mirror_root: Optional[str] = None,
                 max_symbols: Optional[int] = None, gpu_fraction: Optional[float] = None,
                 torch_threads: Optional[int] = None, workdir: Optional[str] = None,
                 label_kind: str = "open_vwap15", label_buyable: bool = False,
                 batch: int = 4, cpu_fallback: bool = False, chunk_bytes: Optional[int] = None,
                 quiet: bool = False) -> None:
        # gpu_fraction None / 0 / "auto" = follow what is free on the card (the default on the server)
        self.auto_fraction = device.startswith("cuda") and (gpu_fraction in (None, 0, 0.0, "auto"))
        self.gpu_fraction = None if self.auto_fraction else gpu_fraction
        self._user_chunk_bytes = chunk_bytes
        if device.startswith("cuda"):
            f = auto_gpu_fraction() if self.auto_fraction else float(gpu_fraction)
            torch.cuda.set_per_process_memory_fraction(f)
            self.gpu_fraction = f
        self.store_path = store_path
        self.store = open_cube_store(store_path, mirror_root=mirror_root)
        self.view, self.trim = warmed_view(self.store, start, end, warmup, max_symbols=max_symbols)
        self.start, self.end, self.warmup = start, end, warmup
        self.device, self.chunk_symbols, self.chunk_days = device, chunk_symbols, chunk_days
        self.torch_threads, self.workdir = torch_threads, workdir
        self.label_kind, self.label_buyable = label_kind, bool(label_buyable)
        self.batch, self.cpu_fallback = max(1, int(batch)), bool(cpu_fallback)
        if chunk_bytes is None and device.startswith("cuda"):
            chunk_bytes = self._chunk_for(self.gpu_fraction)
        self.chunk_bytes = chunk_bytes
        self.quiet = quiet
        self.dates: List[str] = list(self.view.dates[self.trim:])
… (52 行略) …
            if self._price is None:
                self._price = Label(self.label_kind, 1).price(self.view)
            full = Label(self.label_kind, horizon).compute(self.view, price=self._price.copy())
            if self.label_buyable:
                # Same rule as Label(buyable=True) -- a name that opens locked at
                # limit-up on the entry day cannot be bought, so its label is
                # dropped -- but the lock table is read once, not once per horizon
                # (it scans the opening window of every day; five extra horizons
                # used to cost five extra scans).  The runner still checks the
                # h=1 result against the user's own label file, cell for cell.
                if self._locks is None:
                    from alphacube.tradability import entry_locks
                    self._locks = entry_locks(self.view)[0]
                lag = 1
                full[:-lag][self._locks[lag:]] = np.nan
            t = np.asarray(full[self.trim:], dtype=np.float64)
            self._targets[horizon] = t
            if p is not None:
                _atomic_save(p, t)
        return self._targets[horizon]
```

**10-03 23:55 · Bash** — Inspect Label and entry_locks implementations (local copy)

```bash
cd /Users/wxy/Desktop/AlphaCube && grep -n "class Label" -A 60 src/alphacube/*.py | grep -n "def \|vwap\|buyable\|window" | head -40; grep -n "def entry_locks" -A 40 src/alphacube/tradability.py | head -70
```

```
2:src/alphacube/label.py-137-    kind: str = "open_vwap15"        # "open_vwap15" | "close"
4:src/alphacube/label.py-139-    buyable: bool = False            # 剔除"次日开盘封涨停、买不进"的那部分收益
6:src/alphacube/label.py-141-    def price(self, view: CubeView) -> np.ndarray:
7:src/alphacube/label.py-142-        if self.kind == "open_vwap15":
8:src/alphacube/label.py-143-            return open_vwap15(view)
13:src/alphacube/label.py-148-    def compute(self, view: CubeView, price: Optional[np.ndarray] = None) -> np.ndarray:
15:src/alphacube/label.py-150-        lag = 1 if self.kind == "open_vwap15" else 0
17:src/alphacube/label.py-152-        if self.buyable:
18:src/alphacube/label.py-153-            if self.kind != "open_vwap15":
19:src/alphacube/label.py-154-                raise ValueError("buyable is defined for open_vwap15 only (an opening-window lock test)")
26:src/alphacube/label.py-161-    def describe(self) -> str:
27:src/alphacube/label.py-162-        if self.kind == "open_vwap15":
28:src/alphacube/label.py-163-            tail = ", entries locked at limit-up dropped" if self.buyable else ""
33:src/alphacube/label.py-168-__all__ = ["Label", "open_vwap15", "daily_close", "forward_return", "OPEN_VWAP_WINDOW", "OPEN_VWAP_FIELD",
83:def entry_locks(view, window: Tuple[int, int] = None) -> Tuple[np.ndarray, np.ndarray]:
84-    """(D, S) 的 (开盘封涨停, 开盘封跌停),窗口默认就是标签的开盘 15 分钟。"""
85-    from .label import OPEN_VWAP_WINDOW, daily_close
86-
87-    hi, lo = window_range(view, window or OPEN_VWAP_WINDOW)
88-    return limit_locks(hi, lo, daily_close(view), board_limit(view.symbols, view.dates))
89-
90-
91-__all__ = ["board_limit", "ffill_rows", "limit_locks", "window_range", "entry_locks"]
```

**10-03 23:56 · 写文件** `/Users/wxy/Desktop/Partura/studies/F105_std_fangzheng_covamt/rev2.py`(11925 字符)

**10-03 23:56 · Bash** — Patch rev2.py with extra gate and long-decile section

```bash
cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python - <<'EOF'
p='studies/F105_std_fangzheng_covamt/rev2.py'
s=open(p).read()
old='''    gates = {"PRE-EVENT 60d median amount, lag 10": pre, "today's amount (endogenous)": amt, "float cap": cap}
'''
new='''    gates = {"PRE-EVENT 60d median amount, lag 10": pre, "today's amount (endogenous)": amt, "float cap": cap,
             "max30 (the family member itself)": P["max30"]}
'''
assert old in s; s=s.replace(old,new)
old='''    say(f"\\ndone {time.time() - T0:.0f}s")
'''
new='''
    # ------------------------------------------------------------------ 6 what the long decile earns beyond its level
    say("\\n== 6 the long decile: where it sits by pre-event level, and its excess against pre-event-level-matched peers (study's label) ==")
    okp = np.isfinite(t_buy) & np.isfinite(pre) & np.isfinite(P["max30"])
    ewp = np.where(okp, t_buy, 0.0).sum(1) / np.maximum(okp.sum(1), 1)
    ex_raw = np.where(okp, t_buy - ewp[:, None], np.nan)
    ex_pre = matched_excess(t_buy, okp, pre)
    ex_cap = matched_excess(t_buy, okp & np.isfinite(cap), cap)
    pre_q = qbucket(pre, okp, 5)
    cands = {"orig@10": bk.smoothed(-P["orig"], 10.0), "min3@10": bk.smoothed(-P["min3"], 10.0), "known9@5": bk.smoothed(-P["known9"], 5.0),
             "max30@1": bk.smoothed(-P["max30"], 1.0), "max60@0": -P["max60"], "med60@0 (pure level)": -P["med60"],
             "pre-event level itself": -pre, "pos@10": bk.smoothed(-P["pos"], 10.0)}
    for label, s in cands.items():
        for name, sl in SPL:
            w = bk.long_short_weights(np.where(okp, s, np.nan)[sl], 0.10)
            for leg, m in (("long", w > 0), ("short", w < 0)):
                share = [(m & (pre_q[sl] == b)).sum() / max(m.sum(), 1) for b in range(5)]
                r0, cnt = grp_mean(ex_raw[sl], m)
                r1, _ = grp_mean(ex_pre[sl], m)
                r2, _ = grp_mean(ex_cap[sl], m)
                say(f"  {label:<22} [{name}] {leg:<5} n {cnt:5.1f} raw excess {r0:+6.1%}  pre-level-matched {r1:+6.1%}  cap-matched {r2:+6.1%}"
                    f"  share by pre-event quintile " + " ".join(f"{x:.0%}" for x in share))
    say(f"\\ndone {time.time() - T0:.0f}s")
'''
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
EOF
~/.venvs/alphacube/bin/python -m py_compile studies/F105_std_fangzheng_covamt/rev2.py && echo OK; grep -n "gname.split" studies/F105_std_fangzheng_covamt/rev2.py
```

```
OK
159:                    + "   ".join(f"{gname.split(' ')[0]}: " + " ".join(f"{r['rank_ic']:+.4f}" for r in dg.conditional_ic(f[sl], t[sl], g[sl], buckets=5))
```

**10-03 23:57 · Bash** — Make rev2.py robust to label-construction failure

```bash
cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python - <<'EOF'
p='studies/F105_std_fangzheng_covamt/rev2.py'
s=open(p).read()
old='''    ps.label_buyable = False
    ps._targets.pop(1, None)
    t_all = np.asarray(ps.target(1)[:stop], dtype=np.float64)        # same label, limit-up-locked entries kept
    ps.label_buyable = True
    ps._targets.pop(1, None)
    assert np.array_equal(np.asarray(ps.target(1)[:stop], dtype=np.float64), t_buy, equal_nan=True)
    SPL = (("train", tr), ("valid", va))
    LAB = (("buyable", t_buy), ("unfiltered", t_all))
'''
new='''    SPL = (("train", tr), ("valid", va))
    try:
        ps.label_buyable = False
        ps._targets.pop(1, None)
        t_all = np.asarray(ps.target(1)[:stop], dtype=np.float64)    # same label, limit-up-locked entries kept
        LAB = (("buyable", t_buy), ("unfiltered", t_all))
    except Exception as exc:                                          # noqa: BLE001 -- keep the rest of the run
        say(f"!! could not build the unfiltered label ({type(exc).__name__}: {exc}); sections 0-4 use the study's label only")
        t_all = t_buy.copy()
        LAB = (("buyable", t_buy),)
    finally:
        ps.label_buyable = True
        ps._targets.pop(1, None)
    assert np.array_equal(np.asarray(ps.target(1)[:stop], dtype=np.float64), t_buy, equal_nan=True)
'''
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
EOF
~/.venvs/alphacube/bin/python -m py_compile studies/F105_std_fangzheng_covamt/rev2.py && echo OK && sed -n 70,100p studies/F105_std_fangzheng_covamt/rev2.py
```

```
OK
    cnt = m.sum(1)
    days = cnt >= min_names
    if not days.any():
        return float("nan"), 0.0
    v = np.where(m, np.nan_to_num(x), 0.0).sum(1)[days] / cnt[days]
    return float(v.mean() * 252), float(cnt.mean())


with Study(FID) as st:
    tr, va = st.slice("train"), st.slice("valid")
    stop = va.stop
    assert tr.start == 0 and tr.stop == va.start
    P = {k: np.asarray(v[:stop], dtype=np.float64) for k, v in st.panels(EXPR).items()}
    amt = np.asarray(st.control("ctl_amt")[:stop], dtype=np.float64)
    cap = np.asarray(st.control("ctl_cap")[:stop], dtype=np.float64)
    ps = st.ps
    assert ps.label_buyable, "this study's label is the buyable one"
    t_buy = np.asarray(ps.target(1)[:stop], dtype=np.float64)        # the study's label
    SPL = (("train", tr), ("valid", va))
    try:
        ps.label_buyable = False
        ps._targets.pop(1, None)
        t_all = np.asarray(ps.target(1)[:stop], dtype=np.float64)    # same label, limit-up-locked entries kept
        LAB = (("buyable", t_buy), ("unfiltered", t_all))
    except Exception as exc:                                          # noqa: BLE001 -- keep the rest of the run
        say(f"!! could not build the unfiltered label ({type(exc).__name__}: {exc}); sections 0-4 use the study's label only")
        t_all = t_buy.copy()
        LAB = (("buyable", t_buy),)
    finally:
        ps.label_buyable = True
        ps._targets.pop(1, None)
```

**10-03 23:57 · Bash** — Start second revision script on server (train/valid only)

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh exec F105_std_fangzheng_covamt rev2 rev2.py 2>&1 | tail -3
```

```
started F105_std_fangzheng_covamt/rev2: rev2.py
```

**10-03 23:58 · Bash** — Wait for rev2 analysis to finish

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh wait F105_std_fangzheng_covamt rev2 540 2>&1 | tail -8
```

```
== 2 conditional rank IC of the event half inside level quintiles, both labels (negative = same direction as the factor) ==
  [train] D/C mature                   buyable    unconditional -0.0268   PRE-EVENT: -0.0374 -0.0355 -0.0310 -0.0196 -0.0086   today's: -0.0103 -0.0124 -0.0138 -0.0191 -0.0394   float: -0.0313 -0.0359 -0.0340 -0.0232 -0.0125   max30: -0.0092 -0.0135 -0.0168 -0.0252 -0.0431
  [train] D/C mature                   unfiltered unconditional -0.0261   PRE-EVENT: -0.0357 -0.0343 -0.0302 -0.0191 -0.0084   today's: -0.0097 -0.0117 -0.0131 -0.0182 -0.0383   float: -0.0305 -0.0348 -0.0328 -0.0223 -0.0122   max30: -0.0091 -0.0133 -0.0162 -0.0242 -0.0414
  [train] D/C mature, C rising only    buyable    unconditional -0.0375   PRE-EVENT: -0.0631 -0.0541 -0.0455 -0.0268 -0.0097   today's: -0.0235 -0.0200 -0.0218 -0.0264 -0.0431   float: -0.0564 -0.0550 -0.0506 -0.0317 -0.0171   max30: -0.0183 -0.0199 -0.0224 -0.0325 -0.0485
  [train] D/C mature, C rising only    unfiltered unconditional -0.0359   PRE-EVENT: -0.0596 -0.0518 -0.0439 -0.0260 -0.0093   today's: -0.0187 -0.0183 -0.0202 -0.0251 -0.0417   float: -0.0543 -0.0527 -0.0482 -0.0300 -0.0165   max30: -0.0174 -0.0188 -0.0210 -0.0309 -0.0462
[guard] ABORT: this process anon 2.6 GiB (limit 14.0), container anon 34.4 GiB (limit 34.0). Exiting so the neighbouring job is not the one that gets killed.
[partura exit 97 2026-10-04_14:59:14]
```

**10-03 23:59 · Bash** — Read partial rev2 log

```bash
cd /Users/wxy/Desktop/Partura && grep -av 'FutureWarning\|vmap(single_row)\|UserWarning' logs/F105_std_fangzheng_covamt_rev2.log | cut -c1-900
```

```
ready 2s; rows used 1359; symbols 5220

== 0 the two labels ==
  cells where both are finite: 5208786; max |difference| there: 0.00e+00
  cells finite in buyable but not in unfiltered (should be 0): 0
  [train] dropped by the buyable filter: 0.26% of labelled cells (9.1 names/day); their mean next-day return +5.51%, excess over the universe +5.39% per day
  [valid] dropped by the buyable filter: 0.12% of labelled cells (5.6 names/day); their mean next-day return +4.65%, excess over the universe +4.57% per day

== 1 event study by level quintile (mature names; top decile of |D/C| with one threshold for the whole cross-section) ==
   excess against the equal-weight mean of the SAME level quintile, annualised; 'locked' = share of the group's labelled cells the buyable filter drops
  [train] by PRE-EVENT 60d median amount, lag 10
      Q1  entry n  26.3 buyable -95.6% / unfiltered -85.1% locked 1.3%   |   exit n  31.2 buyable +10.0% / unfiltered  +9.3% locked 0.3%   |   quiet n 268.7 buyable  +7.9% / unfiltered  +6.9% locked 0.2%
      Q2  entry n  24.9 buyable -57.8% / unfiltered -46.7% locked 1.1%   |   exit n  29.1 buyable  +4.2% / unfiltered  +2.9% locked 0.1%   |   quiet n 264.6 buyable  +8.1% / unfiltered  +7.2% locked 0.1%
      Q3  entry n  25.4 buyable -54.0% / unfiltered -46.3% locked 0.8%   |   exit n  25.2 buyable  -2.6% / unfiltered  -3.7% locked 0.1%   |   quiet n 260.3 buyable  +8.3% / unfiltered  +7.8% locked 0.1%
      Q4  entry n  26.1 buyable -29.0% / unfiltered -26.3% locked 0.5%   |   exit n  20.6 buyable  +1.2% / unfiltered  +0.5% locked 0.1%   |   quiet n 247.6 buyable  +3.6% / unfiltered  +3.3% locked 0.1%
      Q5  entry n  28.8 buyable  +0.1% / unfiltered  +1.7% locked 0.2%   |   exit n  13.8 buyable  -6.8% / unfiltered  -6.9% locked 0.0%   |   quiet n 224.4 buyable  +0.8% / unfiltered  +0.6% locked 0.1%
  [train] by today's amount (endogenous)
      Q1  entry n   3.6 buyable -82.2% / unfiltered -21.6% locked 4.5%   |   exit n  32.1 buyable  +2.2% / unfiltered  +0.4% locked 0.2%   |   quiet n 318.0 buyable  +2.2% / unfiltered  +1.9% locked 0.2%
      Q2  entry n   7.8 buyable -13.7% / unfiltered  +1.9% locked 1.8%   |   exit n  29.3 buyable  -4.7% / unfiltered  -4.6% locked 0.1%   |   quiet n 301.5 buyable  +3.1% / unfiltered  +2.6% locked 0.1%
      Q3  entry n  15.5 buyable -30.0% / unfiltered -19.9% locked 1.1%   |   exit n  25.1 buyable  +4.4% / unfiltered  +3.4% locked 0.1%   |   quiet n 272.0 buyable  +3.7% / unfiltered  +3.1% locked 0.1%
      Q4  entry n  31.4 buyable -36.3% / unfiltered -30.7% locked 0.8%   |   exit n  20.3 buyable  +6.1% / unfiltered  +5.6% locked 0.2%   |   quiet n 226.0 buyable  +1.8% / unfiltered  +1.1% locked 0.1%
      Q5  entry n  73.9 buyable -42.6% / unfiltered -39.1% locked 0.5%   |   exit n  13.2 buyable  -5.0% / unfiltered  -6.4% locked 0.0%   |   quiet n 149.8 buyable +12.5% / unfiltered +11.5% locked 0.0%
  [train] by float cap
      Q1  entry n  18.2 buyable -79.2% / unfiltered -72.6% locked 0.9%   |   exit n  32.4 buyable  -0.0% / unfiltered  -0.5% locked 0.2%   |   quiet n 290.8 buyable  +7.0% / unfiltered  +6.5% locked 0.2%
      Q2  entry n  22.6 buyable -91.3% / unfiltered -82.3% locked 1.1%   |   exit n  26.8 buyable  +1.0% / unfiltered  -0.0% locked 0.2%   |   quiet n 280.2 buyable  +9.3% / unfiltered  +
… (3552 字符略) …
buyable  +7.4% / unfiltered  +7.0% locked 0.1%
      Q5  entry n  32.3 buyable -27.0% / unfiltered -24.7% locked 0.3%   |   exit n  49.0 buyable  +6.9% / unfiltered  +6.7% locked 0.0%   |   quiet n 335.9 buyable  +7.7% / unfiltered  +7.6% locked 0.0%

== 2 conditional rank IC of the event half inside level quintiles, both labels (negative = same direction as the factor) ==
  [train] D/C mature                   buyable    unconditional -0.0268   PRE-EVENT: -0.0374 -0.0355 -0.0310 -0.0196 -0.0086   today's: -0.0103 -0.0124 -0.0138 -0.0191 -0.0394   float: -0.0313 -0.0359 -0.0340 -0.0232 -0.0125   max30: -0.0092 -0.0135 -0.0168 -0.0252 -0.0431
  [train] D/C mature                   unfiltered unconditional -0.0261   PRE-EVENT: -0.0357 -0.0343 -0.0302 -0.0191 -0.0084   today's: -0.0097 -0.0117 -0.0131 -0.0182 -0.0383   float: -0.0305 -0.0348 -0.0328 -0.0223 -0.0122   max30: -0.0091 -0.0133 -0.0162 -0.0242 -0.0414
  [train] D/C mature, C rising only    buyable    unconditional -0.0375   PRE-EVENT: -0.0631 -0.0541 -0.0455 -0.0268 -0.0097   today's: -0.0235 -0.0200 -0.0218 -0.0264 -0.0431   float: -0.0564 -0.0550 -0.0506 -0.0317 -0.0171   max30: -0.0183 -0.0199 -0.0224 -0.0325 -0.0485
  [train] D/C mature, C rising only    unfiltered unconditional -0.0359   PRE-EVENT: -0.0596 -0.0518 -0.0439 -0.0260 -0.0093   today's: -0.0187 -0.0183 -0.0202 -0.0251 -0.0417   float: -0.0543 -0.0527 -0.0482 -0.0300 -0.0165   max30: -0.0174 -0.0188 -0.0210 -0.0309 -0.0462
[guard] ABORT: this process anon 2.6 GiB (limit 14.0), container anon 34.4 GiB (limit 34.0). Exiting so the neighbouring job is not the one that gets killed.
[partura exit 97 2026-10-04_14:59:14]
```

**10-04 00:00 · Bash** — Check server status and local logs/runs

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh status 2>&1 | tail -6; ls -la logs/ | grep F105; ls runs/F105_std_fangzheng_covamt/
```

```
	557073.pt_F102_rev2	(10/04/26 14:56:30)	(Detached)

540353, 30176 MiB
557075, 860 MiB
container anon 29.9 GiB
gpu.lock slot0.lock slot1.lock slot2.lock -rw-r--r--@  1 wxy  staff   1836 Oct  3 19:37 F105_std_fangzheng_covamt_S1_what.log
-rw-r--r--@  1 wxy  staff   1409 Oct  3 22:45 F105_std_fangzheng_covamt_S2S3_nodes_family.log
-rw-r--r--@  1 wxy  staff   1585 Oct  3 22:57 F105_std_fangzheng_covamt_S4_longleg.log
-rw-r--r--@  1 wxy  staff  18305 Oct  3 23:29 F105_std_fangzheng_covamt_audit1.log
-rw-r--r--@  1 wxy  staff   1075 Oct  3 23:11 F105_std_fangzheng_covamt_final.log
-rw-r--r--@  1 wxy  staff  56450 Oct  3 23:51 F105_std_fangzheng_covamt_rev1.log
-rw-r--r--@  1 wxy  staff   9037 Oct  3 23:59 F105_std_fangzheng_covamt_rev2.log
-rw-r--r--@  1 wxy  staff  12160 Oct  3 19:28 F105_std_fangzheng_covamt_x1_events.log
-rw-r--r--@  1 wxy  staff  10779 Oct  3 23:05 F105_std_fangzheng_covamt_x2_longleg.log
S0_baseline.json
S1_what.json
S1b_S2_S3.json
S2S3_nodes_family.json
S4_longleg.json
final.json
ledger.json
```

**10-04 00:03 · 写文件** `/Users/wxy/Desktop/Partura/notes/F105_std_fangzheng_covamt/07x_review_audit.md`(5521 字符)

**10-04 00:03 · Bash** — Fix three numeric statements in audit note

```bash
cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python - <<'EOF'
p='notes/F105_std_fangzheng_covamt/07x_review_audit.md'
s=open(p).read()
reps=[
('另一面:同样把换手压到 3% 出头,树内的两个版本(`orig`、`min3` 配 hl 10)在样本内仍然比家族成员低 2.4~4.4 / 3.1~4.0 个点。',
 '另一面:同样把换手压到 3% 出头,树内的两个版本(`min3`、`orig` 配 hl 10)在样本内仍然比 `max30` 低 2.5~4.3 / 3.1~4.0 个点。'),
('多头腿优势在训练段从 5.4 个点缩到 4.2 个点(11.2% 对 7.0%),验证段不变(22.3% 对 22.0%)。',
 '多头腿优势在训练段从 5.4 个点缩到 4.2 个点(11.2% 对 7.0%),验证段从 1.5 个点缩到 0.3 个点(22.3% 对 22.0%)。'),
('残差多头腿毛超额 +4%~+6%(训练)/ +10%~+12%(验证)。',
 '残差多头腿毛超额对 `max30` 回归后是 +4%~+6%(训练)/ +11%~+12%(验证),对 `known9` 回归后是 +1.1% / +9.5%。'),
]
for a,b in reps:
    assert a in s, a
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
echo done
```

```
done
```

**10-04 00:05 · 写文件** `/Users/wxy/Desktop/Partura/notes/F105_std_fangzheng_covamt/07x_revision.md`(12670 字符)

**10-04 00:06 · Bash** — Fix numeric statements in revision note

```bash
cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python - <<'EOF'
p='notes/F105_std_fangzheng_covamt/07x_revision.md'
s=open(p).read()
reps=[
('''- 把网格里家族成员的所有(d,hl)组合按换手排开:多空日换手落在 2.6%~5.2% 的 19 个组合,多头腿净超额全部在 12.4%~14.5% / 20.4%~22.4%,纯多头夏普 1.80~2.15 / 3.29~3.69;
  换手高于 5.5%(d=9 的 hl 0/1/2、d=15 的 hl 0)是 9.3%~12.6% / 18.5%~21.7%;换手低于 2.5%(各成员的 hl 10、20)是 9.2%~12.4% / 18.6%~22.4%。
  **多头腿净超额是换手的函数,在 3%~4.5% 附近最高;同一换手下窗口取 9 还是 60 相差不到 1 个点。**''',
 '''- 把网格里家族成员的全部 35 个(d,hl)组合按训练段的多空日换手排开:换手落在 2.3%~5.2% 的 21 个组合,多头腿净超额全部在 12.3%~14.5% / 20.4%~22.4%,纯多头夏普 1.80~2.15 / 3.29~3.69;
  换手高于 5.5% 的 4 个(d=9 的 hl 0/1/2、d=15 的 hl 0)是 9.3%~12.6% / 18.5%~21.7%;换手低于 2.2% 的 10 个是 9.2%~12.8% / 18.6%~22.4%。
  **多头腿净超额是换手的函数,在 3%~4.5% 附近最高;同一换手下窗口取 9 还是 60 相差在 1 个点左右。**'''),
('只留成熟股票后差距缩小到 0.9~3.3 / 0.7~2.7 个点。', '只留成熟股票后差距缩小到 1.0~3.3 / 0.7~2.7 个点。'),
('''但**扣费之后训练段的多头腿净超额是 0 上下(−0.8%~+1.8%),验证段有 +4%~+10%**;
两段不一致。''',
 '''但**平滑、扣费之后训练段的多头腿净超额是 0 上下(hl ≥ 3 时 −1.5%~+1.8%),验证段对 `max30` 回归的残差有 +4%~+10%、对 `known9` 回归的只有 +0.5%~+3.6%**;
两段不一致。'''),
('''- **多头腿净超额:训练段秩平均比 `max30` 单独低 1.0~2.5 个点(六个「树 + 家族」组合无一例外),验证段在 −1.9~+0.8 个点之间。** 纯多头夏普训练段低 0.09~0.34、验证段高 0.17~0.38。''',
 '''- **多头腿净超额:训练段秩平均比其中那个家族成员单独持有低 1.0~2.1 个点(六个「树 + 家族」组合无一例外),验证段在 −0.6~+0.9 个点之间。** 纯多头夏普训练段低 0.09~0.28、验证段高 0.17~0.45。'''),
('''- 多空夏普:秩平均落在两个成分之间或略高于弱的那个(+2.39~+2.75 / +4.08~+4.76),没有超过 `min3` 单独。''',
 '''- 多空夏普:秩平均是 +2.39~+2.75 / +4.08~+4.76,与两个成分里高的那个相差都在 ±0.2 以内(噪声带内);没有协同,也没有超过 `min3` 单独。'''),
('(`D/C` 在 `max30` 五个桶里的 IC,训练段', '(成熟股票的 `D/C` 在 `max30` 五个桶里的 IC,训练段'),
]
for a,b in reps:
    assert a in s, a[:40]
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
echo ok
```

```
ok
```

**10-04 00:07 · Bash** — Revise S1 and S1b notes

```bash
cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python - <<'EOF'
p='notes/F105_std_fangzheng_covamt/07_S1_what.md'
s=open(p).read()
reps=[
('''   与原式的 rank 相关 −0.18。把「`C` 降得最多」的股票排在多头端是亏钱的 —— 这些是一年前爆过量、现在回声滑出窗口的大成交额股票。
   **方向不是信息**:H2+H3 预测的「带符号不比不分方向差」被否定,不分方向的 std 之所以能用,只是因为它把这群股票和新放量的股票一起放进了空头端。''',
 '''   与原式的 rank 相关 −0.18。把「`C` 降得最多」的股票排在多头端是亏钱的 —— 这些是一年前爆过量、现在回声滑出窗口的大成交额股票。
   **(修订)这个变体答不了「方向有没有信息」。** 它是原始金额单位的:成交额² 的尺度把大成交额股票同时推到两端(升得最多和降得最多的都是大成交额股票),
   多头腿为负是水平效应,不是方向没信息。去掉尺度之后(审查复核第 3 节、修订实验第 3 节),同一个 |`D/C`| 最高十分位里,`C` 上升的股票超额 −46.7% / −61.3%,
   `C` 下降的 +5.2% / +2.7%;滑出驱动的股票对当天成交额配对之后的超额是 +2.3% / +6.2%。**方向有信息,而且事件这一半的信息全在方向里:进入是空头信号,滑出(回声)是中性。**
   原研究在这里写的「方向不是信息」是错的。H2+H3 预测的「带符号不比不分方向差」在这个带尺度的写法上确实不成立,但那是尺度的问题。'''),
('''   多头腿毛超额在训练段高 3.8 个点。它的短板是换手:按多空夏普选出来的半衰期是 0,多头腿每年被成本吃掉 7.6 个点;
   半衰期扫描里 hl=5 时纯多头夏普 +1.99、多头腿净超额 +13.7%(train),但那不是按规则选出来的半衰期。''',
 '''   多头腿毛超额在训练段高 3.8 个点。它的短板是换手:按多空夏普选出来的半衰期是 0,多头腿每年被成本吃掉 7.6 个点;
   半衰期扫描里 hl=5 时纯多头夏普 +1.99、多头腿净超额 +13.7%(train),但那不是按多空规则选出来的半衰期。
   **(修订)这一句是后面「慢窗口平台」读法的反例,原研究没有把它带到结论里。** hl=5 正是纯多头夏普规则会选的半衰期;这时 d=9 在 train / valid 上与后来推荐的 d=30
   逐项相同(多头腿净超额 +13.7% / +22.2% 对 +13.6% / +22.2%,纯多头夏普 +1.99 / +3.59 对 +2.03 / +3.69,换手 4.2% 对 4.0%)。'''),
('''**解读**:原式 = 水平 × 事件。水平那一半就是成交额水平(而且是它的一个更吵的版本);事件那一半的方向没有信息。
已知家族用更少的节点同时拿到了这两半,而且拿得更干净(07x 第 6 张表:原式对已知家族中性化后残差 rank IC 0.0090、无成本多空夏普 −0.55)。''',
 '''**解读(修订)**:原式 = 水平 × 事件。水平那一半就是成交额水平(而且是它的一个更吵的版本);事件那一半只有「进入」这个方向有信息,原式用不分方向的 std 把进入和滑出混在一起。
已知家族用更少的节点同时拿到了这两半:原式对它回归之后,空头腿和多空价差什么都不剩(07x events 第 6 张表:无成本多空夏普 −0.55),
多头侧还剩一点(残差 rank IC 0.0090,t 4.3;验证段 0.0135,t 4.5 —— 审查复核第 4 节),这一点扣费之后在训练段挣不到钱(修订实验第 2 节)。'''),
]
for a,b in reps:
    assert a in s, a[:50]
    s=s.replace(a,b)
open(p,'w').write(s)

p='notes/F105_std_fangzheng_covamt/07_S1b_events.md'
s=open(p).read()
reps=[
('''   - 但它是一个**空头信号**:分位剖面训练段 Q1 −28.7%,Q2 就只有 −7.1%,Q3..Q10 在 −1.1% 到 +9.5% 之间几乎是平的;
     多头腿净超额只有原式的一半(4.6% 对 8.2%),验证段多空夏普(+2.79)远低于原式(+4.62)。''',
 '''   - 它的钱主要在空头端:分位剖面训练段 Q1 −28.7%,Q2 就只有 −7.1%,Q3..Q10 从 −1.1% 缓慢升到 +9.5%;
     多头腿净超额只有原式的一半(4.6% 对 8.2%),验证段多空夏普(+2.79)远低于原式(+4.62)。
     **(修订)「其余九档几乎是平的、没有多头腿」说过头了。** 验证段的剖面是 Q1 −19.3%,Q8..Q10 +6.9% / +11.3% / +19.2%,多头腿净超额 +14.7%;
     训练段的弱是 2018 年(全体窗口未满)和次新股造成的:只留成熟股票、同样 hl 5,多头腿毛超额 +11.8% / +20.2%、净超额 +7.7% / +16.2%、纯多头夏普 +1.61 / +2.88,
     与同口径的原式(成熟、hl 3:+7.0% / +22.0%、+1.14 / +4.07)在训练段不相上下(审查复核第 3 节)。'''),
('''   - 条件 IC:按 `known_stdamt_max9` 分五桶,它的桶内 IC 是 −0.0074、−0.0064、−0.0092、−0.0156、**−0.0437**;按 `ctl_amt` 分桶是
     −0.0098 → **−0.0408**。**事件信息几乎只在成交额最大的那一桶里有用** —— 它是「大成交额股票里谁刚爆过量」的细分,不是一个全截面的信号。''',
… (14 行略) …
 '''**解读(修订)**:原式的两半里,「水平」这一半是成交额水平(S1);「事件」这一半只有进入方向有信息,空头端很深,在事前成交清淡的小股票里最强,
另一端(没有事件)相对同水平的同伴多挣 4~10 个点。原研究写的「只在大成交额股票里起作用的空头信号」不成立。
两半都不是这棵树独有的:水平是 `ctl_amt`,事件与 `ctl_dvol20` / `ctl_turnrate` 同类,合起来就是已知家族(它把「水平」和「近 d 天有没有放量」放在一个量里)。'''),
]
for a,b in reps:
    assert a in s, a[:50]
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
echo ok
```

```
ok
```

**10-04 00:08 · Bash** — Revise S3 and S4 notes

```bash
cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python - <<'EOF'
p='notes/F105_std_fangzheng_covamt/07_S3_family.md'
s=open(p).read()
reps=[
('''   **近期的放量信息(短窗口)值钱的地方在空头腿**(空头腿毛超额 d=9 时 +37.7%,d=60 时 +21.0%,d=241 时 +14.1%,训练段);
   **多头腿只要「这一两个月没爆过量的低成交额股票」**,窗口再短只是多付换手。''',
 '''   **近期的放量信息(短窗口)值钱的地方在空头腿**(空头腿毛超额 d=9 时 +37.7%,d=60 时 +21.0%,d=241 时 +14.1%,训练段);
   **多头腿只要「这一两个月没爆过量的低成交额股票」**,窗口再短只是多付换手。
   **(修订)这个「驼峰」的左半边是半衰期规则造成的,不是窗口的性质。** 表里每个成员的半衰期都被多空夏普规则选成了 0,所以窗口越短换手越高。
   半衰期改按纯多头夏普来定(d=9 → hl 5、d=20 → hl 3、d=60 → hl 0),多头腿净超额是 d=9 **+13.7% / +22.2%**、d=20 +13.6% / +21.6%、d=60 +13.5% / +20.4% ——
   d=9 就在平台上。能说的只是:**这一族的多头腿净超额取决于把多空日换手压到多低(2.3%~5.2% 时是 12.3%~14.5% / 20.4%~22.4%),用更长的窗口还是用 EMA 来压没有差别**;
   d=120、241 的下降(换手 1.7%、1.2%)是右半边,仍然成立(修订实验第 1 节)。'''),
('''   换手不到原式的一半,但多空夏普低 0.4 / 1.0。**多头腿的改善只在训练段看得见,验证段是打平** —— 验证段(2022.01–2023.08)里这一族所有成员的多头腿
   净超额都在 18.5%~23.0% 之间,分不出高下。''',
 '''   换手不到原式的一半,但多空夏普低 0.4 / 1.0。**多头腿的改善只在训练段看得见,验证段是打平** —— 验证段(2022.01–2023.08)里这一族所有成员的多头腿
   净超额都在 18.5%~23.0% 之间,分不出高下。
   (修订)这一行的比较没有对齐半衰期:原式是 hl 3、换手 6.0%,家族成员是 hl 0、换手 2.6%~5.2%。原式也把换手压到 3.2%(hl 10)时是 +9.3% / +18.2%,
   家族成员仍然高 4.2~5.2 / 2.2~4.1 个点 —— 样本内的优势不全是换手,但留出段上没有复现(第 10 节)。'''),
]
for a,b in reps:
    assert a in s, a[:50]
    s=s.replace(a,b)
open(p,'w').write(s)

p='notes/F105_std_fangzheng_covamt/07_S4_longleg.md'
s=open(p).read()
reps=[
('''**(1) 窗口:是平台。** 把 S1 / S3 / S4 的七个窗口排在一起(train / valid;方向都是 −,按多空夏普选出的半衰期都是 0):''',
 '''**(1) 窗口:在「半衰期都是 0」的口径下是平台;(修订)换成同换手的口径,平台一直延伸到 d=9,它不是窗口的性质。**
把 S1 / S3 / S4 的七个窗口排在一起(train / valid;方向都是 −,按多空夏普选出的半衰期都是 0):'''),
('''d=30 在训练段和验证段的多头腿净超额、纯多头夏普都是这一族里最高的,而且 15 和 60 两个邻居都不塌。
多空夏普则是另一个方向:d 越短越高,d=15 与原式打平(+2.61 / +4.52 对 +2.54 / +4.62),d=30 低 0.17 / 0.50。''',
 '''d=30 在训练段和验证段的多头腿净超额、纯多头夏普都是这一族里最高的,而且 15 和 60 两个邻居都不塌。
多空夏普则是另一个方向:d 越短越高,d=15 与原式打平(+2.61 / +4.52 对 +2.54 / +4.62),d=30 低 0.17 / 0.50。

**(修订)上表第一列的 d=9 不在平台上,只是因为它的半衰期被多空规则选成了 0、换手 8.5%。** 给 d=9 加一个 hl=5 的 EMA(纯多头夏普规则选的就是 5),
它是 +13.7% / +22.2%、纯多头夏普 +1.99 / +3.59、换手 4.2%,与 d=30(hl 0)逐项相同;两个实际交易的信号 rank 相关 0.948 / 0.952,多头十分位重合 79% / 80%。
每个成员都按纯多头规则定半衰期时,d=9、15、20、30、60 是 +13.7% / +13.9% / +13.6% / +14.5% / +13.5%(训练)和 +22.2% / +22.1% / +21.6% / +22.3% / +20.4%(验证)。
所以这一节测到的不是「更慢的窗口更好」,而是「**这一族任何成员,只要把多空日换手压到 3%~5%,多头腿净超额都在 12%~14% / 21%~22%**」——
加长窗口和加 EMA 是达到同一换手的两种办法,样本内分不出高下(审查复核第 1 节、修订实验第 1 节)。d=30 之所以在 hl 0 的口径下「最高」,只是它不加平滑时的换手(4.0%)正好落在最好的区间里。'''),
… (7 行略) …
多头腿需要事件这一半(本节第 2 点:60 日中位数的多头腿只有 60 日最大值的一半;修订实验第 4 节:没有事件的股票相对同水平的同伴多挣 4~10 个点)。
(c) 直接实验:`s4_pos`(hl 10)与 `max30`(hl 1)做秩平均,训练段纯多头夏普 +2.41 对 +2.15、净超额 +14.9% 对 +14.5%,验证段 +3.46 对 +3.66、+20.2% 对 +22.3% —— 两段方向相反。
能说的是:**没有证据表明在家族成员之上再加一份事件信息能抬高多头腿**(家族已经用掉了);说不了「事件这一半对多头腿没用」。'''),
]
for a,b in reps:
    assert a in s, a[:50]
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
echo ok
```

```
ok
```

**10-04 00:08 · Bash** — Revise S_final note with both pre-registered criteria

```bash
cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python - <<'EOF'
p='notes/F105_std_fangzheng_covamt/07_S_final.md'
s=open(p).read()
old='''三条判据的结果:

- `f_max30` 留出段多头腿净超额 +12.5%(原式 +8.9%)、纯多头夏普 +1.37(原式 +1.04),**两项都高于原式** → 升华没有被证伪。
- `f_min3` 留出段多空夏普 +2.72(原式 +2.24),差 +0.48,方向是变好 → 「多余节点」的结论在样本外成立。
- `f_max15 / f_max30 / f_max60` 留出段多头腿净超额 +12.0% / +12.5% / +14.7%,最大相差 2.7 个点(< 5)→ 平台在样本外还在。

原式那一行(多空 +2.24、多头腿毛超额 +14.3%)与用户表公布的测试列逐位相同。'''
new='''三条判据的结果(第 3 条在修订时重写,见下):

- `f_max30` 留出段多头腿净超额 +12.5%(原式 +8.9%)、纯多头夏普 +1.37(原式 +1.04),**两项都高于原式** → 升华没有被证伪。
  (修订)这条判据比的是「各自按多空规则定半衰期」的两行:原式 hl 3、换手 6.1%,`f_max30` hl 0、换手 3.8%。它证伪不了「好处只是换手更低」;对齐半衰期之后的读法在第 10 节。
- `f_min3` 留出段多空夏普 +2.72(原式 +2.24),差 +0.48,方向是变好 → 「多余节点」的结论在样本外成立。
- `f_max15 / f_max30 / f_max60` 留出段多头腿净超额 +12.0% / +12.5% / +14.7%,最大相差 2.7 个点(< 5)→ 按这里写的这条判据没有触发;**但读前写下的另一条判据按字面触发了**。

原式那一行(多空 +2.24、多头腿毛超额 +14.3%)与用户表公布的测试列逐位相同。

**(修订)关于「平台」,读前的判据有两条,而且互不一致;原研究只按宽松的那条裁决,没有交代另一条。**

- 能独立核实是读前定下的那一条,在配置文件里 `f_max60` 的 `why`(随 `runs/.../final.json` 固化,两处逐字相同):
  「平台的慢端(换手 2.6%)。预测多头腿净超额与 f_max30 相近;**如果 15/30/60 在留出段上次序乱掉,平台只是样本内的**」。
- 上面清单里的那一条是「彼此差超过 5 个点 → 平台是样本内的」。这份文件创建于 23:07:46(早于 final 运行),最后一次修改是 23:12:01(晚于 `final.json` 的 23:11:00),
  所以「5 个点」这一条是不是读之前写下的,从文件时间无法独立核实。
- **按配置里那一条的字面,判据已经触发:最优档从 30 换成了 60。** 多头腿净超额 d=15 / 30 / 60:train 12.3% / 13.6% / 13.5%,utrain 14.9% / 16.1% / 15.5%(都是 30 最高);
  留出段 12.0% / 12.5% / **14.7%**(60 最高,比读前推荐的 30 高 2.2 个点)。纯多头夏普留出段 1.28 / 1.37 / 1.74,极差 0.46(utrain 是 2.26 / 2.46 / 2.34,极差 0.20);
  60 对 30 的差 0.37 超过了本研究自己用的 ±0.3 噪声带。
- 为什么仍然不把它读成「多头腿的优势只在样本内」:三档在留出段相差不超过 2.7 个点,而且都高于原式的 8.9%;样本内的次序本身就不稳
  (train 是 30 > 60 > 15,valid 是 30 > 15 > 60:22.2% / 21.3% / 20.4%)—— 拿「次序」当判据本来就定得不好。但这一点应该写出来,而不是换一条判据。
- 照实的结论:**「d=30 是平台中央、最优」在样本外不成立**(最优档换了,纯多头夏普的差超出噪声带);「三档都比按多空规则定半衰期的原式好、彼此接近」成立。
  修订实验第 1 节之后还知道,三档之间的次序在同换手下本来就没有意义(这一族的多头腿净超额是换手的函数,不是窗口的函数)。
  推荐不因此改动,也不改选 60 —— 用留出段再挑一次窗口,它就成了第二个验证集。'''
assert old in s
s=s.replace(old,new)
open(p,'w').write(s)
EOF
echo ok
```

```
ok
```

**10-04 00:08 · Bash** — Rewrite conditional-IC note point 3

```bash
cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python - <<'EOF'
p='notes/F105_std_fangzheng_covamt/07_conditional.md'
s=open(p).read()
old=s[s.index('3. **事件成分只在大成交额股票里有用**'):s.index('4. `s4_max30|ctl_turnrate`')]
new='''3. **(修订)事件成分那几行的分桶变量是内生的,原来的读法「事件成分只在大成交额股票里有用」不成立。**
   表里的数字本身没错:`s1_relchg|ctl_amt` Q1..Q5 = −0.0098、−0.0117、−0.0141、−0.0215、**−0.0408**;按已知家族分桶更极端(−0.0074、−0.0064、−0.0092、−0.0156、**−0.0437**);
   写干净的版本 `s4_pos|ctl_amt` 也一样(−0.0142 → −0.0365)。但 `ctl_amt`(当天成交额)和 `known_stdamt_max9`(9 日峰值)都含有事件本身:进入事件就是近期放量,
   它把股票送进这两个变量的最高一桶(成熟股票里 |`D/C`| 最高十分位、`C` 上升的股票,56% / 58% 落在当天成交额最高的五分之一里;同一个 |`D/C`| 档位里 `C` 上升的股票成交额分位 0.76,
   `C` 下降的 0.42)。低桶里剩下的「事件」基本只有回声和噪声,桶内 IC 自然低。
   **换成事件之前的水平来分桶**(滞后 10 个交易日的 60 日成交额中位数;修订实验第 4 节,生成表里没有这几行):

   | `D/C` 的桶内 rank IC | Q1(事前最清淡) | Q2 | Q3 | Q4 | Q5(事前最大) |
   |---|---|---|---|---|---|
   | 事前成交额中位数,train | **−0.0344** | −0.0295 | −0.0258 | −0.0183 | −0.0169 |
   | 事前成交额中位数,valid | **−0.0459** | −0.0457 | −0.0374 | −0.0325 | −0.0250 |
   | 流通市值,train / valid | **−0.0371 / −0.0497** | −0.0312 / −0.0455 | −0.0298 / −0.0425 | −0.0224 / −0.0272 | −0.0113 / −0.0219 |
   | 事前中位数,只看 `C` 上升的成熟股票,train / valid | **−0.0631 / −0.0789** | −0.0541 / −0.0697 | −0.0455 / −0.0607 | −0.0268 / −0.0507 | −0.0097 / −0.0365 |
   | 事前中位数,`s4_pos`,train / valid | **−0.0540 / −0.0558** | −0.0449 / −0.0547 | −0.0342 / −0.0503 | −0.0202 / −0.0429 | −0.0027 / −0.0330 |

   梯度整个反过来:**事件在每个事前水平上都有信息,在事前成交最清淡、市值最小的股票里最强。** 按一年水平 `C` 分桶的那一行(−0.0167 → −0.0321,`C` 是一年窗口的量,受当周事件的影响小)
   原本就比较平,原研究却用两个内生的分桶推翻了它;07x(events)里「是相加,不是门控」的读法基本是对的,后来加的那句修正才是错的。
   按已知家族分桶的那一行真正说明的是:**对家族成员取值做了条件之后,事件信息只剩在高的那一端** —— 家族成员取值最低的一桶按定义就是近期没放过量的股票,事件已经被家族用掉了。
   所以「多头腿用不上事件」也不对:多头腿需要「没有事件」(S4 第 2 点),只是家族成员已经把它带上了。
'''
s=s.replace(old,new)
open(p,'w').write(s)
EOF
sed -n 1,40p notes/F105_std_fangzheng_covamt/07_conditional.md | cut -c1-200
```

```
(条件 IC 是原始面板在分桶变量五等分内的 rank IC,训练段;负号 = 与因子方向一致。)

1. **原式在小市值里强、在最大市值里弱**:`v_base|ctl_cap` 从 Q1 的 −0.0559 降到 Q5 的 −0.0191。`s4_max30|ctl_cap` 同一个形状而且更陡
   (−0.0659 → −0.0185)。这一族在市值最大的五分之一里只剩三分之一的预测力。
2. **原式的 IC 有一大半是成交额桶之间的排序**:`v_base|ctl_amt` 桶内只有 −0.0137 ~ −0.0197(无条件是 −0.0387),只有成交额最大的一桶到 −0.0300。
3. **(修订)事件成分那几行的分桶变量是内生的,原来的读法「事件成分只在大成交额股票里有用」不成立。**
   表里的数字本身没错:`s1_relchg|ctl_amt` Q1..Q5 = −0.0098、−0.0117、−0.0141、−0.0215、**−0.0408**;按已知家族分桶更极端(−0.0074、−0.0064、−0.0092、−0.0156�
   写干净的版本 `s4_pos|ctl_amt` 也一样(−0.0142 → −0.0365)。但 `ctl_amt`(当天成交额)和 `known_stdamt_max9`(9 日峰值)都含有事件本身:进入事件就是近期放量,
   它把股票送进这两个变量的最高一桶(成熟股票里 |`D/C`| 最高十分位、`C` 上升的股票,56% / 58% 落在当天成交额最高的五分之一里;同一个 |`D/C`| 档位里 `C
   `C` 下降的 0.42)。低桶里剩下的「事件」基本只有回声和噪声,桶内 IC 自然低。
   **换成事件之前的水平来分桶**(滞后 10 个交易日的 60 日成交额中位数;修订实验第 4 节,生成表里没有这几行):

   | `D/C` 的桶内 rank IC | Q1(事前最清淡) | Q2 | Q3 | Q4 | Q5(事前最大) |
   |---|---|---|---|---|---|
   | 事前成交额中位数,train | **−0.0344** | −0.0295 | −0.0258 | −0.0183 | −0.0169 |
   | 事前成交额中位数,valid | **−0.0459** | −0.0457 | −0.0374 | −0.0325 | −0.0250 |
   | 流通市值,train / valid | **−0.0371 / −0.0497** | −0.0312 / −0.0455 | −0.0298 / −0.0425 | −0.0224 / −0.0272 | −0.0113 / −0.0219 |
   | 事前中位数,只看 `C` 上升的成熟股票,train / valid | **−0.0631 / −0.0789** | −0.0541 / −0.0697 | −0.0455 / −0.0607 | −0.0268 / −0.0507 | −0.0097 / −0.0365 |
   | 事前中位数,`s4_pos`,train / valid | **−0.0540 / −0.0558** | −0.0449 / −0.0547 | −0.0342 / −0.0503 | −0.0202 / −0.0429 | −0.0027 / −0.0330 |

   梯度整个反过来:**事件在每个事前水平上都有信息,在事前成交最清淡、市值最小的股票里最强。** 按一年水平 `C` 分桶的那一行(−0.0167 → −0.0321,`C` 
   原本就比较平,原研究却用两个内生的分桶推翻了它;07x(events)里「是相加,不是门控」的读法基本是对的,后来加的那句修正才是错的。
   按已知家族分桶的那一行真正说明的是:**对家族成员取值做了条件之后,事件信息只剩在高的那一端** —— 家族成员取值最低的一桶按定义就是近期没
   所以「多头腿用不上事件」也不对:多头腿需要「没有事件」(S4 第 2 点),只是家族成员已经把它带上了。
4. `s4_max30|ctl_turnrate`:−0.0195、−0.0230、−0.0205、−0.0257、−0.0393。换手率最高的一桶里最强,与「空头腿的钱是高换手率」一致。
5. 表里 `s1_relchg|s1_level` 与 `s1_relchg|g_level` 是同一件事算了两遍(`g_level` 就是 `s1_level` 的面板;前一行来自中断前的那次运行)。
   `s1_level|s1_relchg` 是反过来的:按相对变化分桶,水平的桶内 IC 平在 −0.025 ~ −0.029 —— 水平的信息不依赖有没有事件。
```

**10-04 00:09 · Bash** — Revise events and longleg notes

```bash
cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python - <<'EOF'
p='notes/F105_std_fangzheng_covamt/07_conditional.md'
s=open(p).read()
a='原本就比较平,原研究却用两个内生的分桶推翻了它;07x(events)里「是相加,不是门控」的读法基本是对的,后来加的那句修正才是错的。'
b='原本就比较平,原研究却用两个内生的分桶推翻了它;07x(events)里「按水平分桶,相对变化每桶都有 IC」的读法是对的,后来加的那句修正才是错的。'
assert a in s; s=s.replace(a,b); open(p,'w').write(s)

p='notes/F105_std_fangzheng_covamt/07x_events.md'
s=open(p).read()
reps=[
('''**是相加,不是门控。**(后注:这句话只对「按一年水平 `C` 分桶」成立;按**当前**成交额或已知家族分桶,事件的桶内 IC 在最高一桶是最低一桶的 4~6 倍,见条件 IC 表后的说明。)''',
 '''**是相加,不是门控。**(修订:原研究后来在这里加过一句「按当前成交额或已知家族分桶,事件的桶内 IC 在最高一桶是最低一桶的 4~6 倍,所以事件只在大成交额股票里有用」。
那两个分桶变量含有事件本身,是内生的;换成事件之前的水平分桶,梯度反过来 —— 事件在事前成交清淡的股票里最强。见条件 IC 表后的说明和修订实验第 4 节。)'''),
('''- **H3 成立:周年回声是稀释。**(后注:这是分组证据;S1b 的替换实验 `s1_noecho` 没有支持它,第 9 节把 H3 记为「未坐实」。) 被回声推进空头腿的股票日占了空头十分位的 23%(train)到 48%(valid),但它们的超额只有''',
 '''- **H3 成立:周年回声是稀释。**(修订:原研究因为 S1b 的替换实验 `s1_noecho` 没有支持它,曾把 H3 记为「未坐实」;加上审查复核第 3 节和修订实验第 3 节的两条证据之后改回成立,见第 9 节。) 被回声推进空头腿的股票日占了空头十分位的 23%(train)到 48%(valid),但它们的超额只有'''),
('''  但回声组的超额仍然是负的 —— H3′ 也有一点对:一年前爆过量本身是个弱的负信号(水平 `C` 的 IC)。''',
 '''  回声组的超额仍然是负的,原研究据此说「H3′ 也有一点对」。(修订)这部分负超额是水平,不是事件:对当天成交额配对之后,回声组的超额是 **+2.3% / +6.2%**,
  进入组仍有 −18.7% / −24.4%(修订实验第 3 节)。H3′ 不成立。'''),
('''读法:**原式与已知家族不重合的那一半(回声、窗口未满、「相对一年历史」的归一化)不是 alpha,是噪声。**
「rank 相关 0.68 所以是不同因子」在这里是错的 —— 相关低是因为原式里掺了一半不挣钱的东西。''',
 '''原研究在这里的读法是「原式与已知家族不重合的那一半不是 alpha,是噪声」「被完全吃掉」。**(修订)这只对空头腿和多空价差成立。**
残差的无成本多空夏普为负,是因为残差的多头侧为正(+1.1%)、空头侧为负(−5.1%),两条腿相抵,不是残差没有信息:残差 rank IC 0.0090 的 t 值是 4.3,
验证段 0.0135(t 4.5)、多头腿毛超额 +9.5%;对 `max30` 回归的残差 rank IC 0.0157(t 8.9)/ 0.0209(t 6.5)、多头腿毛超额 +4.3% / +10.6%(审查复核第 4 节)。
照实的说法:**原式的空头腿与多空价差被已知家族包含;多头侧在信息上不被包含,但这部分平滑、扣费之后训练段挣不到钱(−1.5%~+1.8%),验证段有 +0.5%~+10%,
与家族成员做秩平均也没有抬高多头腿净超额**(修订实验第 2 节)。
「rank 相关 0.68 所以是不同因子」仍然是错的 —— 相关低主要是因为原式里掺了回声和未满窗口这些不挣钱的东西;但「低相关的那一半全是噪声」同样说过头了。'''),
]
for a,b in reps:
    assert a in s, a[:50]
    s=s.replace(a,b)
open(p,'w').write(s)

p='notes/F105_std_fangzheng_covamt/07x_longleg.md'
s=open(p).read()
… (65 字符略) …
还剩 +1.56、多头腿毛超额 +9.7%。
族内是嵌套的:短窗口成员包含长窗口成员的全部信息(`max30` 对 `known9` 残差 rank IC 0.0037),多出来的那部分(`known9` 对 `max30`:0.0283 / +1.88)
是近期放量,多头 / 空头各 7 个点,换手 15.4% —— 这部分信息在多头腿上不够付成本,所以多头腿的最优点在更慢的成员上。''',
 '''原式对 `max30` 回归之后剩下的东西在多空上挣不到钱(无成本多空夏普 +0.02),反过来 `max30` 还剩 +1.56、多头腿毛超额 +9.7%。
(修订)「挣不到钱」只是多空口径:残差的多头侧是 +4.3%、空头侧 −4.1%,两条腿相抵;残差 rank IC 0.0157 的 t 值是 8.9。多头侧扣费后的情况见修订实验第 2 节。
族内是嵌套的:短窗口成员包含长窗口成员的全部信息(`max30` 对 `known9` 残差 rank IC 0.0037),多出来的那部分(`known9` 对 `max30`:0.0283 / +1.88)
是近期放量,多头 / 空头各 7 个点,换手 15.4%。原研究由此推出「这部分信息在多头腿上不够付成本,所以多头腿的最优点在更慢的成员上」。
(修订)后半句不对:多头腿的最优点在**更低的换手**上,不在更慢的窗口上。`known9` 加 hl=5 的 EMA 与 `max30` 在 train / valid 上逐项相同
(+13.7% / +22.2% 对 +13.6% / +22.2%),两者平滑到同样换手之后 rank 相关 0.95(修订实验第 1 节)。'''),
('''**(3) 逐年(每年从空仓开始;方向、半衰期沿用训练段)。多头腿净超额 / 纯多头夏普:**''',
 '''**(3) 逐年(每年从空仓开始;方向、半衰期沿用训练段 —— 也就是原式和 `min3` 是 hl 3、家族成员是 hl 0,换手没有对齐;对齐之后的逐年表在修订实验第 1 节)。多头腿净超额 / 纯多头夏普:**'''),
]
for a,b in reps:
    assert a in s, a[:50]
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
echo ok
```

```
ok
```

**10-04 00:09 · Bash** — Revise variants note

```bash
cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python - <<'EOF'
p='notes/F105_std_fangzheng_covamt/08_variants.md'
s=open(p).read()
reps=[
('''- **A 组不是 B 组和 C、D 之外的第五样东西**:07x 的回归表明 A 对 B 回归后残差挣不到钱(对 `known_stdamt_max9` 无成本多空夏普 −0.55,对 `max30` +0.02)。''',
 '''- **A 组不是 B 组和 C、D 之外的第五样东西**:07x 的回归表明 A 对 B 回归后残差在多空上挣不到钱(对 `known_stdamt_max9` 无成本多空夏普 −0.55,对 `max30` +0.02)。
  (修订)这是空头腿和多空价差的结论;残差的多头侧 rank IC 仍然显著(t 4~9),只是平滑、扣费之后训练段没有钱、与 B 组成员做秩平均也不抬高多头腿(修订实验第 2 节)。'''),
('''- B 组内部按窗口排成一条线:窗口越短 rank IC 和多空夏普越高、换手越高;多头腿净超额在 d=15~60 上是平台(S4 第 1 张表)。''',
 '''- B 组内部按窗口排成一条线:窗口越短 rank IC 和多空夏普越高、换手越高。总表里 B 组成员的半衰期都被多空规则选成了 0,所以多头腿净超额看上去在 d=15~60 上是平台、d=9 掉下去;
  (修订)半衰期按纯多头夏普来定时 d=9~60 都在 13.5%~14.5% / 20.4%~22.3%,`known_stdamt_max9` 加 hl=5 的 EMA 与 `s4_max30` 是同一个东西(rank 相关 0.95)。
  **读这张总表的多头腿净超额一列时要先看换手一列**:换手差一倍,净超额就能差 3~5 个点,那不是结构差异。'''),
('''| **D 无尺度的事件** | `s1_relchg`(与原式 0.68、与已知家族 0.24)、`s4_pos`(0.18 / 0.49)、`s1_signed`(−0.18) | 「相对自己的历史,最近有没有放量」 | +2.0~+3.0 / +2.8~+3.2(`s1_signed` +1.4 / +1.4) | +4.6% / +12.8%~+14.7%(`s1_signed` 为负) |''',
 '''| **D 事件** | `s1_relchg`(与原式 0.68、与已知家族 0.24)、`s4_pos`(0.18 / 0.49);`s1_signed`(−0.18)带符号但没有去尺度 | 「相对自己的历史,最近有没有放量」 | +2.0~+3.0 / +2.8~+3.2(`s1_signed` +1.4 / +1.4) | +4.6% / +12.8%~+14.7%(换手 7%~12%;`s4_pos` 在 hl 10、换手 4.7% 时是 +8.0% / +17.4%;`s1_signed` 为负,那是尺度造成的) |'''),
]
for a,b in reps:
    assert a in s, a[:50]
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
echo ok
```

```
ok
```

**10-04 00:10 · 写文件** `/Users/wxy/Desktop/Partura/notes/F105_std_fangzheng_covamt/09_diagnosis.md`(6109 字符)

10-04 00:10 · 读 `/Users/wxy/Desktop/Partura/notes/F105_std_fangzheng_covamt/09_diagnosis.md`

**10-04 00:11 · 写文件** `/Users/wxy/Desktop/Partura/notes/F105_std_fangzheng_covamt/09_diagnosis.md`(6141 字符)

10-04 00:11 · 读 `/Users/wxy/Desktop/Partura/notes/F105_std_fangzheng_covamt/10_distilled.md`

**10-04 00:12 · 写文件** `/Users/wxy/Desktop/Partura/notes/F105_std_fangzheng_covamt/10_distilled.md`(6650 字符)

**10-04 00:13 · Bash** — Revise risks note and print next-steps note

```bash
cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python - <<'EOF'
p='notes/F105_std_fangzheng_covamt/10_distilled.md'
s=open(p).read()
a='| 伪影 | 没有 | 周年回声、未满窗口放大、上市首日为 0 三个都还在 |'
b='| 伪影 | 没有 | 周年回声、未满窗口放大、上市首日为 0 三个都还在(按构造:同样是一年硬窗口外面套 5 日 std;没有单独量) |'
assert a in s; s=s.replace(a,b); open(p,'w').write(s)

p='notes/F105_std_fangzheng_covamt/11_risks.md'
s=open(p).read()
reps=[
('''- **已知暴露。** 它就是成交额水平家族:与 `ctl_amt` 的 rank 相关 0.80,全部控制变量张成 R² 0.740。它不该被当成一个与池内成交额类因子独立的信号去加权;
  AlphaCube 的 0.95 rank 相关闸拦不住它(与 `cross_max(day_std(Amt), 9)` 只有 0.85),要用「对已封族中性化后的掉幅」判(F001 的先验,本研究同向)。''',
 '''- **已知暴露,而且对已有 F001 结果的因子池增量为零。** 它就是成交额水平家族:与 `ctl_amt` 的 rank 相关 0.80,全部控制变量张成 R² 0.740。
  (修订)它等价于 F001 已蒸馏出的 `cross_max(day_std(Amt), 9)` 加一个 hl≈5 的 EMA(多头腿净超额 +13.7% / +22.2% 对 +13.6% / +22.2%;平滑到同样换手后两者 rank 相关 0.95,
  回归残差「谁多一点」在训练段和验证段方向相反)。它不该被当成一个与池内成交额类因子独立的信号去加权;
  AlphaCube 的 0.95 rank 相关闸在原始面板上拦不住它(与 d=9 只有 0.85),要在各自实际交易的信号上比,或者用「对已封族中性化后的掉幅」判(F001 的先验,本研究同向)。'''),
('''- **次新股。** 原式的未满窗口放大恰好把次新股挡在多头腿外面(验证段多头十分位里次新股占 0.7%);`max30` 没有这道挡板,
  成交清淡的次新股会进多头腿(验证段 7.7%,其中只有 `max30` 持有的那一半里占 14.2%)。这些股票的组内超额没有单独量过;上线前应加上市天数过滤再看一次。''',
 '''- **次新股。** 原式的未满窗口放大恰好把次新股挡在多头腿外面(验证段多头十分位里次新股占 0.7%);`max30` 没有这道挡板,
  成交清淡的次新股会进多头腿(验证段 8.8%,每天 41 只)。(修订)审查复核量了它们:组内超额 +12.9%/年,低于成熟股票的 +26.9%,对多头腿毛超额的贡献是 +1.3 个点(共 25.5);
  只留成熟股票重建的书在验证段是 +22.3%(全部股票 +22.2%),训练段是 +11.2%(+13.6%,这里掉的主要是 2018 年)。次新股不是业绩来源,但它们拖低了多头腿的质量,加上市天数过滤没有坏处。
- **板块。**(修订,审查复核第 2 节)验证段多头十分位里科创板占 17.6%(`max60` 19.9%,原式 14.9%),它在截面里只占 7.4%;训练段没有这个偏。科创板 20% 涨跌幅、有投资者门槛,
  这一段多头腿的可交易性和成本假设要单独看。'''),
('''- **过拟合。** 全研究评了 28 个变体;推荐的窗口取自一个四档(15 / 20 / 30 / 60)都成立的平台,不是单点最优,留出段只读了一次。
  但留出段上平台内部的次序与样本内不同(样本内 d=30 最好,留出段 d=60 最好)—— 窗口的精确取值不要当真。''',
 '''- **过拟合。** 全研究评了 28 个变体(修订时另外在脚本里试了 11 个秩平均组合,没有一个被采用);留出段只读了一次。
  (修订)推荐的 d=30 不是「平台中央」:所谓平台是半衰期规则造成的,同换手下 d=9~60 没有差别;留出段上最优档从 30 换成了 60,配置里读前写下的「次序乱掉」判据按字面触发。
  样本内「家族成员在同换手下比树内提纯版的多头腿高 2~5 个点」在留出段上没有复现(13.5% 对 13.5%)—— **相对原式真正经过样本外检验的好处只有「换手更低」这一条**,
  而降低换手不需要换结构(给原式的提纯版配 hl 10 就行)。'''),
('''- **空头腿被标签抬高。** 次日开盘封涨停买不进的票标签是 NaN、在空头里记 0,所有候选的空头腿和多空夏普都带这个偏差;多头腿的数字不受影响。''',
 '''- **空头腿被标签抬高。** 次日开盘封涨停买不进的票标签是 NaN、在空头里记 0,所有候选的空头腿和多空夏普都带这个偏差;多头腿的数字不受影响。
  (修订)量到的部分:被过滤的格子占有标签格子的 0.26% / 0.12%(每天 9 / 6 只),它们的次日收益平均 +5.5% / +4.7%;它们集中在刚放过量的小股票里
  (进入事件组里占 0.2%~1.3%),把这一组的空头深度抬高了 2~11 个点(例如 −95.6% → −85.1%),方向和梯度不变。各候选整条空头腿和多空夏普被抬高多少没有量到(那次运行被中止)。
  机制一节里所有关于「空头端有多深」的数字都应按这个幅度打折读。'''),
]
for a,b in reps:
    assert a in s, a[:50]
    s=s.replace(a,b)
open(p,'w').write(s)

p='notes/F105_std_fangzheng_covamt/12_next.md'
s=open(p).read()
print(s)
EOF
```

```
只列能明显降低不确定性的:

1. **对池内已有的成交额水平结构做增量测试。** 把 `cross_max(day_std(Amt), 30)` 对因子池里已封 / 已入选的成交额类因子(至少 `cross_max(day_std(Amt), 9)`、
   `cross_max(day_sum(Amt), 9)`)中性化,看多头腿净超额还剩多少。07x 的结果预示剩不下多少(对 `known9` 回归后残差 rank IC 0.0037),
   那样结论就是「把池里那个成员的窗口从 9 放慢到 30~60」,而不是加一个因子。
2. **容量曲线。** 用稳定的截面定义(按过去 60 日平均成交额分档、按月换成分,而不是按当天分位过滤)重做 07x longleg 第 4 节,
   看多头腿净超额随「剔掉成交最清淡的 x%」怎么掉;同时把成本换成与成交额挂钩的冲击模型。
3. **上市天数过滤。** 对 `max30` 加「上市满 250 个交易日」之后重跑两本书,确认验证段多头腿里那 7.7% 的次新股不是业绩来源。
4. **把「事件」当排除条件而不是因子。** `s4_pos` 的 Q1(成交量在一年高点附近)训练 / 验证超额 −35.0% / −39.7%,其余九档几乎是平的。
   对纯多头用户,它的用法是「任何多头组合里先剔掉这一档」;值得在一个别的多头因子上测一次剔除前后的差别。
5. **2024 年的回撤归因。** 把 2024 年多头腿的日收益对小市值 / 低流动性指数回归,分清这一族的多头腿是不是在那之后结构性变弱。
```

**10-04 00:13 · Bash** — Rewrite next-steps note

```bash
cd /Users/wxy/Desktop/Partura && cat > notes/F105_std_fangzheng_covamt/12_next.md <<'EOF'
只列能明显降低不确定性的(修订后重排;原来的第 1、3 条已经由审查复核和修订实验回答了,写在各条后面):

1. **同换手下,家族成员和树内提纯版谁的多头腿更好。** 这是修订之后最大的未决:样本内家族领先 2~5 个点(train / valid 同向),留出段打平。留出段已经用过,不能再拿它挑;
   要等新的样本外数据(2026 年起),或者换一个独立的市场 / 股票池,用同一条规则(半衰期按纯多头夏普定)比 `cross_max(day_std(Amt), 30)`、
   `cross_max(day_std(Amt), 9)` + EMA、`cross_stddev(cross_stddev(day_cov(Amt, Amt), 241), 5)` + hl 10 三者。在那之前把它们当成同一个东西。
2. **半衰期规则本身。** 这次研究最大的一个错读(「慢窗口平台」)和留出段对比的偏差,都来自「半衰期按多空夏普定、然后拿去比多头腿」。对纯多头用户,
   建议这一批因子统一加一列「按纯多头夏普定半衰期」的数字(`books.splits_at_hl_long` 已经在每次运行的 JSON 里),结构比较只在同换手下做。
3. **容量曲线。** 用稳定的截面定义(按过去 60 日平均成交额分档、按月换成分,而不是按当天分位过滤)重做 07x longleg 第 4 节,
   看多头腿净超额随「剔掉成交最清淡的 x%」怎么掉;同时把成本换成与成交额挂钩的冲击模型。验证段多头腿里科创板占 18%~20%,要单独算。
4. **把「进入事件」当排除条件。** 修订后知道事件那一半的信息在进入方向、在事前不活跃的小股票里最强(相对同水平同伴 −85%~−95%/年,不带可买入过滤的标签下也有 −81%~−85%),
   而这正是纯多头组合容易买到的那类股票。值得在一个别的多头因子上测:剔掉「近 5 天有放量进入事件」的股票前后,多头腿净超额差多少。
   (原来这一条写的是「`s4_pos` 的 Q1 −35.0% / −39.7%,其余九档几乎是平的」;后半句不对 —— hl 5 的剖面顶端三档是 +6.6% / +9.0% / +11.4% 和 +7.4% / +14.2% / +21.2%。)
5. **可买入标签对空头端的抬高。** 把各候选的空头腿和多空夏普在不带过滤的标签下重算一遍(`rev2.py` 第 3~6 节已经写好,那次运行被邻居的内存占用中止,没有重跑);
   这批因子的多空夏普都带这个偏差,量出来之后别的研究也能用。
6. **2024 年的回撤归因。** 把 2024 年多头腿的日收益对小市值 / 低流动性指数回归,分清这一族的多头腿是不是在那之后结构性变弱。

已经回答的:
- 「对池内已有的成交额水平结构做增量测试」:对 F001 的 `cross_max(day_std(Amt), 9)` 已测,增量为零(加 hl=5 的 EMA 之后是同一个东西,rank 相关 0.95)。对池里别的成交额类结构仍然没测。
- 「上市天数过滤」:审查复核做了,只留成熟股票时 `max30` 验证段多头腿净超额 +22.3%(全部股票 +22.2%),次新股不是业绩来源。
EOF
echo ok
```

```
ok
```

**10-04 00:13 · Bash** — Document revision runs in config and rebuild report

```bash
cd /Users/wxy/Desktop/Partura && cat >> configs/F105_std_fangzheng_covamt.yaml <<'EOF'
# ---- 审查与修订(2026-10-04;都不是阶段、都是 study.sh exec、都只用 train / valid,没有读留出段)
#   audit1  审查员写的 studies/F105_std_fangzheng_covamt/audit_1.py          -> notes/07x_review_audit.md
#   rev1    studies/F105_std_fangzheng_covamt/rev1.py:半衰期网格、残差平滑扣费、秩平均、方向的水平配对、事前水平分桶  -> notes/07x_revision.md
#   rev2    studies/F105_std_fangzheng_covamt/rev2.py:不带可买入过滤的标签;跑到第 2 节被内存守卫中止(邻居占满容器内存),按规矩没有重跑
# S_final 各变体的 why 是读留出段之前写下的,修订时一字未动。
EOF
./scripts/study.sh report F105_std_fangzheng_covamt 2>&1 | tail -5
```

```
wrote /root/autodl-tmp/Partura/research/alpha_distillation/F105_std_fangzheng_covamt.md
    1699 research/alpha_distillation/F105_std_fangzheng_covamt.md
```

**10-04 00:14 · Bash** — List headings of rebuilt report

```bash
cd /Users/wxy/Desktop/Partura && grep -n "^#\|^\*\*(" research/alpha_distillation/F105_std_fangzheng_covamt.md | sed -n 1,120p
```

```
1:# Alpha 研究报告 — F105_std_fangzheng_covamt
11:## 1. 原始表达式
25:## 2. 算子的真实语义
29:### `day_cov`
37:### `cross_max`
46:### `cross_fangzheng`
55:### `ts_stddev`
86:### 既往研究留下的先验
112:## 3. 数学分解
133:**(1) 根节点读的是「慢水平的 5 日变化量」。** `C` 是一年窗口的统计量,一天只进一个值、出一个值,
141:**(2) 进入窗口的跳变有多大。** 一个大小为 X 的尖峰进入 241 日窗口时,
145:**(3) 硬窗口的周年回声。** 同一个尖峰在 241 个交易日后滑出窗口,`C` 掉回去同样的幅度;
154:## 4. 结构语法
178:## 5. 竞争性假设
206:## 6. 基线指标
301:## 7. 消融实验
303:### S0_baseline
319:### S1_what
370:### S1b_events
432:### S2_nodes
501:### S3_family
564:### S4_longleg
591:**(1) 窗口:在「半衰期都是 0」的口径下是平台;(修订)换成同换手的口径,平台一直延伸到 d=9,它不是窗口的性质。**
607:**(修订)上表第一列的 d=9 不在平台上,只是因为它的半衰期被多空规则选成了 0、换手 8.5%。** 给 d=9 加一个 hl=5 的 EMA(纯多头夏普规则选的就是 5),
613:**(2) 聚合方式:多头腿要的是「没爆过量」,不是「平时成交少」。**
620:**(3) 字段:日内离散度有贡献。** `s4_summax30`(日成交额的 30 日最大值)多空 +1.54 / +3.63、多头腿净超额 +10.1% / +22.2%、纯多头夏普 +1.40 / +3.53;
624:**(4) 「事件」那一半写干净也没有多头腿。** `s4_pos` = 最近 5 天峰值 / 一年峰值(无尺度):rank IC 0.0341 / 0.0528,多空 +2.02 / +3.20,
630:**(修订)这个结论的两个前提都要改,结论降级为未坐实。**
638:### S_final
697:**(修订)关于「平台」,读前的判据有两条,而且互不一致;原研究只按宽松的那条裁决,没有交代另一条。**
… (34 行略) …
1453:### 未决
1463:### 假设表的判决
1479:## 10. 蒸馏 / 升华后的候选
1501:### 结果
1519:### 留出段(20230808–20251231,只读了这一次;上面那张表,方向和半衰期都在用户训练段上定,半衰期按多空夏普规则)
1531:### 同一次读取,半衰期改按纯多头夏普规则定(修订时补的表)
1548:### 读法(修订)
1577:### 两个并列的候选
1592:### 它(读前推荐的那个)比原式好用在哪里
1600:### 它没有比原式好的地方,以及限制
1608:## 11. 失效模式与风险
1638:## 12. 下一步实验
1660:## 附录 A — 数据段使用台账
1672:## 附录 B — 复现
1675:# S0_baseline: 182.4s, 峰值 anon 3.05 GiB, stages ['S0_baseline']
1676:# S1_what: 200.3s, 峰值 anon 3.33 GiB, stages ['S1_what']
1677:# S1b_S2_S3: 695.6s, 峰值 anon 4.69 GiB, stages ['S1_what', 'S2_nodes', 'S3_family']
1678:# S2S3_nodes_family: 411.4s, 峰值 anon 4.6 GiB, stages ['S1b_events', 'S2_nodes', 'S3_family']
1679:# S4_longleg: 169.8s, 峰值 anon 3.61 GiB, stages ['S4_longleg']
1680:# final: 165.2s, 峰值 anon 2.56 GiB, stages ['S_final']
```

10-04 00:14 · 读 `/Users/wxy/Desktop/Partura/research/alpha_distillation/F105_std_fangzheng_covamt.md`

**10-04 00:14 · Bash** — Patch notes and read S4/S_final sections of report

```bash
cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python - <<'EOF'
p='notes/F105_std_fangzheng_covamt/07_S1b_events.md'
s=open(p).read()
reps=[
('滑出组那 −5.1% / −13.2% 对当天成交额配对之后是 +2.3% / +6.2% —— 负的部分全是水平(修订实验第 3 节)。',
 '滑出组那 −5.1% / −13.2%(修订脚本重算是 −4.8% / −13.0%)对当天成交额配对之后是 +2.3% / +6.2% —— 负的部分全是水平(修订实验第 3 节)。'),
('另一端(没有事件)相对同水平的同伴多挣 4~10 个点。', '另一端(没有事件)相对同水平的同伴多挣 4~10 个点(训练段事前最大的一桶除外,那里只有 +0.8)。'),
]
for a,b in reps:
    assert a in s, a[:40]; s=s.replace(a,b)
open(p,'w').write(s)
p='notes/F105_std_fangzheng_covamt/07_S4_longleg.md'
s=open(p).read()
a='**(4) 「事件」那一半写干净也没有多头腿。** `s4_pos`'
b='**(4) 「事件」那一半写干净之后(原结论是「也没有多头腿」;修订见本点末尾)。** `s4_pos`'
assert a in s; s=s.replace(a,b); open(p,'w').write(s)
EOF
sed -n 564,712p research/alpha_distillation/F105_std_fangzheng_covamt.md | cut -c1-600
```

```
### S4_longleg

**问题**: 已知家族 cross_max(day_std(Amt), d) 的多头腿在 d=20~60 上是稳定的平台,还是两个点的运气?多头腿要的是「没爆过量」(极值)还是「平时成交少」(中位数/均值)?原式的「事件」那一半写干净之后有没有多头腿?

| 变体 | 表达式 | 方向 | rank IC train/valid | 半衰期 | 扣费多空夏普 train/valid | 多头腿毛超额 train/valid | 多头腿净超额 train/valid | 多头占比 | 多空日换手 | 取值离散度 |
|---|---|---|---|---|---|---|---|---|---|---|
| `s4_max15` | `cross_max(day_std(Amt), 15)` | − | +0.0466 / +0.0654 | 0 | **+2.61 / +4.52** | +18.0% / +26.1% | +12.3% / +21.3% | 34.0% | 6.2% | 1.00 |
| `s4_max30` | `cross_max(day_std(Amt), 30)` | − | +0.0411 / +0.0585 | 0 | **+2.37 / +4.12** | +17.4% / +25.3% | +13.6% / +22.2% | 39.1% | 4.0% | 1.00 |
| `s4_mean20` | `cross_mean(day_std(Amt), 20)` | − | +0.0377 / +0.0608 | 0 | **+1.93 / +4.00** | +15.2% / +24.8% | +11.9% / +22.0% | 39.2% | 3.7% | 1.00 |
| `s4_med60` | `cross_med(day_std(Amt), 60)` | − | +0.0209 / +0.0416 | 2 | **+1.11 / +3.02** | +7.0% / +19.5% | +5.8% / +18.5% | 35.1% | 1.5% | 1.00 |
| `s4_summax30` | `cross_max(day_sum(Amt), 30)` | − | +0.0354 / +0.0575 | 0 | **+1.54 / +3.63** | +13.5% / +25.0% | +10.1% / +22.2% | 43.8% | 3.5% | 1.00 |
| `s4_pos` | `div(cross_max(day_std(Amt), 5), cross_max(day_std(Amt), 241))` | − | +0.0341 / +0.0528 | 1 | **+2.02 / +3.20** | +11.9% / +19.7% | +4.6% / +12.8% | 25.7% | 11.8% | 0.97 |

<details><summary>每个变体为什么存在</summary>

- `s4_max15` — d=15(窗口池内)。平台假设预测它的多头腿净超额落在 d=9 的 9.3% 和 d=20 的 12.6% 之间(train);如果它跳出这个区间,S3 的驼峰就是噪声
- `s4_max30` — d=30(窗口池内,夹在 20 和 60 之间)。平台假设预测多头腿净超额 >= 12.6%(train)且 valid 不低于 20%、多空夏普落在 2.14~2.54 之间;否则 20 和 60 只是碰巧
- `s4_mean20` — d=20 上极值换均值(与 s3_max20 配对;d=60 上 max 在 train 好、mean 在 valid 好,没有定论)。如果均值在 train 和 valid 上都不输,「极值记忆」对多头腿就不是必需的
- `s4_med60` — 60 日中位数:完全不看放量日,只看平时的成交水平。H6(多头腿 = 低成交额 ∩ 没有事件)预测它的多头腿明显差于 s3_max60;如果一样好,多头腿只是「平时成交少」,和事件无关
- `s4_summax30` — 字段换成日成交额(与 s4_max30 配对)。S2 里原式的字段换成 day_sum 后变差;如果在已知家族里也变差,日内成交额离散度对多头腿有独立贡献
- `s4_pos` — 原式「事件」那一半的干净写法:最近 5 天的峰值相对一年峰值的位置(无尺度、无周年回声的等幅重响、上市首日不为 0)。s1_relchg 的多头腿净超额只有 4.6%(train);如果干净写法的多头腿也弱,「相对自身历史没放量」本身就不是多头信号,升华只能在水平这一半里找

</details>

**问题**:已知家族 `cross_max(day_std(Amt), d)` 的多头腿在 d=20~60 上是稳定的平台,还是两个点的运气?
多头腿要的是「没爆过量」还是「平时成交少」?原式的「事件」那一半写干净之后有没有多头腿?

**(1) 窗口:在「半衰期都是 0」的口径下是平台;(修订)换成同换手的口径,平台一直延伸到 d=9,它不是窗口的性质。**
把 S1 / S3 / S4 的七个窗口排在一起(train / valid;方向都是 −,按多空夏普选出的半衰期都是 0):

… (99 行略) …
- `f_max15 / f_max30 / f_max60` 留出段多头腿净超额 +12.0% / +12.5% / +14.7%,最大相差 2.7 个点(< 5)→ 按这里写的这条判据没有触发;**但读前写下的另一条判据按字面触发了**。

原式那一行(多空 +2.24、多头腿毛超额 +14.3%)与用户表公布的测试列逐位相同。

**(修订)关于「平台」,读前的判据有两条,而且互不一致;原研究只按宽松的那条裁决,没有交代另一条。**

- 能独立核实是读前定下的那一条,在配置文件里 `f_max60` 的 `why`(随 `runs/.../final.json` 固化,两处逐字相同):
  「平台的慢端(换手 2.6%)。预测多头腿净超额与 f_max30 相近;**如果 15/30/60 在留出段上次序乱掉,平台只是样本内的**」。
- 上面清单里的那一条是「彼此差超过 5 个点 → 平台是样本内的」。这份文件创建于 23:07:46(早于 final 运行),最后一次修改是 23:12:01(晚于 `final.json` 的 23:11:00),
  所以「5 个点」这一条是不是读之前写下的,从文件时间无法独立核实。
- **按配置里那一条的字面,判据已经触发:最优档从 30 换成了 60。** 多头腿净超额 d=15 / 30 / 60:train 12.3% / 13.6% / 13.5%,utrain 14.9% / 16.1% / 15.5%(都是 30 最高);
  留出段 12.0% / 12.5% / **14.7%**(60 最高,比读前推荐的 30 高 2.2 个点)。纯多头夏普留出段 1.28 / 1.37 / 1.74,极差 0.46(utrain 是 2.26 / 2.46 / 2.34,极差 0.20);
  60 对 30 的差 0.37 超过了本研究自己用的 ±0.3 噪声带。
- 为什么仍然不把它读成「多头腿的优势只在样本内」:三档在留出段相差不超过 2.7 个点,而且都高于原式的 8.9%;样本内的次序本身就不稳
  (train 是 30 > 60 > 15,valid 是 30 > 15 > 60:22.2% / 21.3% / 20.4%)—— 拿「次序」当判据本来就定得不好。但这一点应该写出来,而不是换一条判据。
- 照实的结论:**「d=30 是平台中央、最优」在样本外不成立**(最优档换了,纯多头夏普的差超出噪声带);「三档都比按多空规则定半衰期的原式好、彼此接近」成立。
  修订实验第 1 节之后还知道,三档之间的次序在同换手下本来就没有意义(这一族的多头腿净超额是换手的函数,不是窗口的函数)。
  推荐不因此改动,也不改选 60 —— 用留出段再挑一次窗口,它就成了第二个验证集。

### 中性化(fit 段)
```

**10-04 00:15 · Bash** — Patch S_final note; view section 10 table and section 8 start

```bash
cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python - <<'EOF'
p='notes/F105_std_fangzheng_covamt/07_S_final.md'
s=open(p).read()
a='''   要多空夏普的话该用 `f_max15`。另外它是 F001 已经蒸馏出的那个家族的一个成员,不是新因子。
'''
b='''   要多空夏普的话该用 `f_max15`。另外它是 F001 已经蒸馏出的那个家族的一个成员,不是新因子。

(修订时加的一句,上面五条是读前的原话,保留不改:第 1、2 点是「所有成员半衰期都是 0」口径下的读法。同换手下 d=9~60 没有差别,
d=9 加 hl=5 的 EMA 与 d=30 逐项相同 —— 见 S4 的修订段。当时如果按纯多头规则定半衰期,就没有理由在 d=9 和 d=30 之间选。)
'''
assert a in s; s=s.replace(a,b); open(p,'w').write(s)
EOF
sed -n 1479,1500p research/alpha_distillation/F105_std_fangzheng_covamt.md | cut -c1-400; sed -n 1311,1330p research/alpha_distillation/F105_std_fangzheng_covamt.md | cut -c1-300
```

```
## 10. 蒸馏 / 升华后的候选

**最终对比,与用户表同口径**(留出段 = 用户的测试段)

| 结构 | 方向 | 半衰期 | 扣费多空夏普 训练/测试 | 多头腿毛超额 训练/测试 | 多头腿净超额 训练/测试 | 纯多头夏普 训练/测试 | 空头腿毛超额 训练/测试 | 多头占比(训练) | 多空日换手 |
|---|---|---|---|---|---|---|---|---|---|
| _用户表里公布的原式_ | − | 3 | +3.03 / +2.24 | +16.8% / +14.3% | — | — | — | — | — |
| `f_orig` `ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3)...` | − | 3 | **+3.03 / +2.24** | +16.8% / +14.3% | +11.8% / +8.9% | +1.96 / +1.04 | +31.1% / +32.6% | 35.1% | 6.1% |
| `f_min3` `cross_stddev(cross_stddev(day_cov(Amt, Amt), 241), 5)` | − | 3 | **+3.30 / +2.72** | +17.5% / +16.3% | +13.0% / +11.5% | +2.18 / +1.33 | +33.9% / +37.8% | 34.0% | 6.1% |
| `f_max15` `cross_max(day_std(Amt), 15)` | − | 0 | **+3.08 / +2.70** | +20.3% / +17.0% | +14.9% / +12.0% | +2.26 / +1.28 | +37.9% / +42.5% | 34.9% | 6.0% |
| `f_max30` `cross_max(day_std(Amt), 30)` | − | 0 | **+2.80 / +2.39** | +19.6% / +15.7% | +16.1% / +12.5% | +2.46 / +1.37 | +29.7% / +32.0% | 39.8% | 3.8% |
| `f_max60` `cross_max(day_std(Amt), 60)` | − | 0 | **+2.52 / +2.39** | +17.7% / +16.6% | +15.5% / +14.7% | +2.34 / +1.74 | +23.2% / +25.6% | 43.3% | 2.4% |

**先说留出段的流程(修订时加的说明)。** 留出段在整个研究里只读了一次(S_final 那一笔,5 个表达式;台账里 holdout 的读取次数是 1)。审查之后的修订**没有再读留出段**:
下面新增的「半衰期按纯多头规则定」那张表,数字来自同一次 final 运行当时就写进 `runs/.../final.json` 的 `books_user.splits_at_hl_long`,不是新的读取;修订的两次补充运行只用 train / valid。
读前定下的推荐(`f_max30`)没有因为留出段的数字改动过。流程上有两处瑕疵,无法撤销,照实写在这里:

1. **关于「平台」的读前判据有两条,互不一致。** 原研究按宽松的那条(三档彼此差超过 5 个点才算失败)裁决;随 `final.json` 固化、能核实是读前写下的那条
   (「如果 15/30/60 在留出段上次序乱掉,平台只是样本内的」)按字面已经触发 —— 最优档从 30 换成了 60。细节在 S_final 的修订段。
2. **读前写下的升华判据没有对齐半衰期。** 「`f_max30` 的多头腿净超额和纯多头夏普都低于 `f_orig` 才算失败」比的是各自按多空规则定半衰期的两行(原式 hl 3、换手 6.1%;`f_max30` hl 0、换手 3.8%),
   它证伪不了「好处只是换手更低」。这是判据定得不好,不是事后换判据;对齐之后的读法在下面第 2 点。

## 8. 语义变体

| 变体 | 表达式 | 方向 | rank IC train/valid | 半衰期 | 扣费多空夏普 train/valid | 多头腿毛超额 train/valid | 多头腿净超额 train/valid | 多头占比 | 多空日换手 | 取值离散度 |
|---|---|---|---|---|---|---|---|---|---|---|
| `v_base` | `ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5)` | − | +0.0387 / +0.0521 | 3 | **+2.54 / +4.62** | +13.1% / +26.0% | +8.2% / +20.7% | 30.5% | 6.0% | 1.00 |
| `s1_level` | `cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241)` | − | +0.0262 / +0.0313 | 0 | **+1.82 / +3.36** | +10.6% / +20.0% | +9.5% / +19.3% | 40.6% | 1.2% | 1.00 |
| `s1_relchg` | `div(cross_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 2...` | − | +0.0259 / +0.0376 | 5 | **+2.96 / +2.79** | +9.5% / +18.8% | +4.6% / +14.7% | 25.1% | 7.0% | 1.00 |
| `s1_signed` | `ts_delta(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5)` | − | +0.0185 / +0.0267 | 10 | **+1.35 / +1.38** | -6.8% / -11.9% | -8.7% / -14.1% | -32.6% | 2.9% | 0.99 |
| `s1_noecho` | `cross_stddev(cross_decay_linear(cross_max(day_cov(Amt, Amt), 3), 24...` | − | +0.0337 / +0.0380 | 1 | **+2.23 / +3.78** | +12.1% / +18.0% | +6.3% / +13.2% | 29.2% | 6.6% | 1.00 |
| `s1_recent` | `cross_stddev(cross_max(day_cov(Amt, Amt), 3), 5)` | − | +0.0480 / +0.0649 | 3 | **+2.31 / +3.97** | +16.6% / +22.3% | +10.8% / +17.2% | 34.7% | 6.7% | 1.00 |
| `s1_known_stdamt9` | `cross_max(day_std(Amt), 9)` | − | +0.0484 / +0.0671 | 0 | **+2.47 / +4.44** | +16.9% / +24.9% | +9.3% / +18.5% | 30.9% | 8.5% | 1.00 |
| `s2_dtface_check` | `cross_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5)` | − | +0.0387 / +0.0521 | 3 | **+2.54 / +4.62** | +13.1% / +26.0% | +8.2% / +20.7% | 30.5% | 6.0% | 1.00 |
| `s2_no_max3` | `cross_stddev(cross_fangzheng(day_cov(Amt, Amt), 241), 5)` | − | +0.0403 / +0.0533 | 3 | **+2.67 / +4.77** | +14.5% / +26.6% | +9.4% / +21.2% | 31.3% | 6.2% | 1.00 |
| `s2_mid_std` | `cross_stddev(cross_stddev(cross_max(day_cov(Amt, Amt), 3), 241), 5)` | − | +0.0376 / +0.0507 | 3 | **+2.64 / +4.65** | +12.6% / +25.0% | +8.0% / +20.4% | 28.9% | 5.8% | 1.00 |
| `s2_mid_mean` | `cross_stddev(cross_mean(cross_max(day_cov(Amt, Amt), 3), 241), 5)` | − | +0.0378 / +0.0517 | 3 | **+2.21 / +4.44** | +13.7% / +25.5% | +8.6% / +20.4% | 35.0% | 5.7% | 1.00 |
| `s2_min3` | `cross_stddev(cross_stddev(day_cov(Amt, Amt), 241), 5)` | − | +0.0392 / +0.0522 | 3 | **+2.84 / +4.80** | +14.3% / +25.5% | +9.9% / +20.9% | 30.4% | 5.9% | 1.00 |
| `s2_field_std` | `cross_stddev(cross_fangzheng(cross_max(day_std(Amt), 3), 241), 5)` | − | +0.0388 / +0.0491 | 5 | **+2.72 / +4.00** | +14.1% / +21.3% | +9.0% / +16.2% | 31.2% | 6.1% | 1.00 |
| `s2_field_sum` | `cross_stddev(cross_fangzheng(cross_max(day_sum(Amt), 3), 241), 5)` | − | +0.0362 / +0.0486 | 3 | **+2.29 / +3.62** | +14.0% / +21.7% | +7.8% / +15.5% | 32.4% | 7.1% | 1.00 |
| `s2_w60` | `cross_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 60), 5)` | − | +0.0403 / +0.0539 | 3 | **+2.18 / +4.28** | +14.2% / +23.7% | +7.8% / +17.8% | 32.8% | 7.7% | 1.00 |
| `s2_out20` | `cross_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241),...` | − | +0.0344 / +0.0468 | 1 | **+2.34 / +4.39** | +12.9% / +24.4% | +8.7% / +20.1% | 34.4% | 4.6% | 1.00 |
```

**10-04 00:15 · Bash** — Search notes for stale claims

```bash
cd /Users/wxy/Desktop/Partura/notes/F105_std_fangzheng_covamt && grep -n "完全包含\|完全吃掉\|方向无信息\|方向没有信息\|方向不是信息\|只在大成交额\|是噪声\|平台" *.md | cut -c1-230
```

```
06_baseline.md:15:3. **原始面板在多头端是噪声,靠平滑才能交易。** 半衰期扫描(训练段):hl 0 时多空夏普 +1.83、纯多头夏普 **−0.09**、
07_S1_what.md:15:   原研究在这里写的「方向不是信息」是错的。H2+H3 预测的「带符号不比不分方向差」在这个带尺度的写法上确实不成立,但那是尺度的问题。
07_S1_what.md:20:   **(修订)这一句是后面「慢窗口平台」读法的反例,原研究没有把它带到结论里。** hl=5 正是纯多头夏普规则会选的半衰期;这时 d=9 在 train / valid 上与后来推荐的 d
07_S1b_events.md:42:另一端(没有事件)相对同水平的同伴多挣 4~10 个点(训练段事前最大的一桶除外,那里只有 +0.8)。原研究写的「只在大成交额股票里起作用的空头信号」不成立。
07_S_final.md:9:| `f_max60` | `cross_max(day_std(Amt), 60)` | 2 | 平台的慢端(S3)。多空 +2.14 / +3.64,多头腿净超额 +13.5% / +20.4%,日换手 2.6% |
07_S_final.md:27:- `f_max15 / f_max30 / f_max60` 的多头腿净超额彼此差超过 5 个点 → 平台是样本内的。
07_S_final.md:41:**(修订)关于「平台」,读前的判据有两条,而且互不一致;原研究只按宽松的那条裁决,没有交代另一条。**
07_S_final.md:44:  「平台的慢端(换手 2.6%)。预测多头腿净超额与 f_max30 相近;**如果 15/30/60 在留出段上次序乱掉,平台只是样本内的**」。
07_S_final.md:45:- 上面清单里的那一条是「彼此差超过 5 个点 → 平台是样本内的」。这份文件创建于 23:07:46(早于 final 运行),最后一次修改是 23:12:01(晚于 `final.json` 的 23:11:00),
07_S_final.md:52:- 照实的结论:**「d=30 是平台中央、最优」在样本外不成立**(最优档换了,纯多头夏普的差超出噪声带);「三档都比按多空规则定半衰期的原式好、彼此接近」成立�
07_S3_family.md:27:   d=9 就在平台上。能说的只是:**这一族的多头腿净超额取决于把多空日换手压到多低(2.3%~5.2% 时是 12.3%~14.5% / 20.4%~22.4%),用更长的窗口还是用 EMA 来压没有差别**;
07_S4_longleg.md:1:**问题**:已知家族 `cross_max(day_std(Amt), d)` 的多头腿在 d=20~60 上是稳定的平台,还是两个点的运气?
07_S4_longleg.md:4:**(1) 窗口:在「半衰期都是 0」的口径下是平台;(修订)换成同换手的口径,平台一直延伸到 d=9,它不是窗口的性质。**
07_S4_longleg.md:20:**(修订)上表第一列的 d=9 不在平台上,只是因为它的半衰期被多空规则选成了 0、换手 8.5%。** 给 d=9 加一个 hl=5 的 EMA(纯多头夏普规则选的就是 5),
07x_events.md:26:**是相加,不是门控。**(修订:原研究后来在这里加过一句「按当前成交额或已知家族分桶,事件的桶内 IC 在最高一桶是最低一桶的 4~6 倍,所以事件只在大成交额股票
07x_events.md:48:在安静的一端 `C` 的升降只是噪声。多头十分位的平均成交额分位 **0.17**、流通市值分位 0.34 / 0.31、换手率分位 0.28 / 0.32;
07x_events.md:80:**原式被已知家族完全吃掉,反过来不成立。** 两者 rank 相关只有 0.68(R² 0.49),但把 `cross_max(day_std(Amt), 9)` 回归掉之后,
07x_events.md:83:原研究在这里的读法是「原式与已知家族不重合的那一半不是 alpha,是噪声」「被完全吃掉」。**(修订)这只对空头腿和多空价差成立。**
07x_events.md:88:「rank 相关 0.68 所以是不同因子」仍然是错的 —— 相关低主要是因为原式里掺了回声和未满窗口这些不挣钱的东西;但「低相关的那一半全是噪声」同样说过头了�
07_conditional.md:6:3. **(修订)事件成分那几行的分桶变量是内生的,原来的读法「事件成分只在大成交额股票里有用」不成立。**
08_variants.md:14:- B 组内部按窗口排成一条线:窗口越短 rank IC 和多空夏普越高、换手越高。总表里 B 组成员的半衰期都被多空规则选成了 0,所以多头腿净超额看上去在 d=15~60 上是
07x_review_audit.md:26:**`known9` 加一个 hl=5 的 EMA,在 train 和 valid 上与推荐的 `max30`(hl 0)逐项相同。** 原研究说的「d=9 不在平台上」是半衰期规则造成的:d=9 被选成 hl 0、换手 8.5%,
07x_review_audit.md:27:多头腿每年被成本吃掉 7.6 个点;把换手压下来它就在平台上。完整的网格在后面的修订实验一节。`max30` 对 `known9` 回归后的残差 rank IC 只有 0.0037(t 1.5)/ 0.0078(t
07x_review_audit.md:61:**「方向无信息」是错的**:事件这一半的信息全在方向里。同一张表还说明分桶是内生的:同一个最高十分位里,`C` 上升的股票当天成交额分位 0.76~0.79,`C` 下降�
07x_review_audit.md:80:残差多头腿毛超额对 `max30` 回归后是 +4%~+6%(训练)/ +11%~+12%(验证),对 `known9` 回归后是 +1.1% / +9.5%。原研究「原式与已知家族不重合的那一半不是 alpha,是噪声」�
07x_revision.md:8:**(1) 「d=15~60 是多头腿平台」是半衰期规则造成的。** 每个成员在半衰期网格 {0,1,2,3,5,10,20} 上都算了一遍;下表是两条规则各自选中的那一行。
07x_revision.md:20:- 半衰期按纯多头夏普来定,d=9、15、20、30、60 五个成员的多头腿净超额是 13.5%~14.5% / 20.4%~22.3%,纯多头夏普 1.98~2.15 / 3.38~3.66 —— **d=9 就在「平台」上**。
07x_revision.md:66:两段不一致。反向的残差(家族里树没有的那部分)两段都有 +4%~+7% / +7%~+12%。两者谁也不完全包含谁,家族多出来的更多。
07x_revision.md:89:  +11.7% / +21.5%、纯多头夏普 +1.78 / +3.66 —— 也不如 `max30` 单独(原始的 `min3` 面板在 hl 0 上是噪声,一个共用的 EMA 照顾不了两边)。
07x_revision.md:96:**小结(2)**:原式的多头侧**在信息上**不被家族完全包含(残差 rank IC t > 3、残差多头腿毛超额为正,train 和 valid 都是);但这部分**扣费后没有稳定的钱**(训练段 0、�
07x_revision.md:110:  事件本身没有贡献。H3′(回声不是噪声)不成立,H3(回声是稀释)成立。
07x_revision.md:114:**(4) 事件是不是「只在大成交额股票里起作用」:用事件之前的水平分桶。** 原研究用当天成交额 `ctl_amt` 和 9 日峰值 `known_stdamt_max9` 分桶;进入事件本身就是近�
07x_revision.md:131:**换成事前水平,梯度整个反过来:事件的 IC 在事前成交最清淡的一桶里最高,在最大的一桶里最低**,两段都是;按流通市值分桶也是。原研究的「事件只在大成交�
10_distilled.md:5:1. **关于「平台」的读前判据有两条,互不一致。** 原研究按宽松的那条(三档彼此差超过 5 个点才算失败)裁决;随 `final.json` 固化、能核实是读前写下的那条
10_distilled.md:6:   (「如果 15/30/60 在留出段上次序乱掉,平台只是样本内的」)按字面已经触发 —— 最优档从 30 换成了 60。细节在 S_final 的修订段。
10_distilled.md:72:   「d=30 是平台中央、最优」在样本外没有得到支持,配置里那条「次序乱掉」的判据按字面触发了(S_final 的修订段)。**推荐不因此改动,也不改选 60** —— 用留�
12_next.md:6:2. **半衰期规则本身。** 这次研究最大的一个错读(「慢窗口平台」)和留出段对比的偏差,都来自「半衰期按多空夏普定、然后拿去比多头腿」。对纯多头用户,
09_diagnosis.md:19:   原研究的「方向无信息」依据的是 `s1_signed` 多头腿为负,那是原始金额单位下的尺度效应(S1)。
09_diagnosis.md:23:   原研究的「只在大成交额股票里起作用」(桶内 IC −0.007 → −0.044)用的是当天成交额和 9 日峰值分桶,这两个变量含有事件本身:56% / 58% 的进入事件落在当天成�
09_diagnosis.md:31:8. **(修订)这一族的多头腿净超额是换手的函数,不是窗口的函数。** 原研究写的是「d=15~60 是平台、d=9 不在平台上」;那是因为所有成员的半衰期都被多空规则选�
09_diagnosis.md:53:  但最优档从样本内的 30 换成了 60(纯多头夏普 1.37 对 1.74,差 0.37 超过 ±0.3 的噪声带),配置里读前写下的判据「次序乱掉 → 平台只是样本内的」按字面已经触发(
09_diagnosis.md:54:  能说的只有:低换手的家族成员在留出段都比高换手的原式好;「d=30 最优」「平台」在样本外没有得到支持。
11_risks.md:17:  (修订)推荐的 d=30 不是「平台中央」:所谓平台是半衰期规则造成的,同换手下 d=9~60 没有差别;留出段上最优档从 30 换成了 60,配置里读前写下的「次序乱掉」判据按
```

**10-04 00:15 · Bash** — Fix events note header, rebuild report, view risk/next/ledger sections

```bash
cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python - <<'EOF'
p='notes/F105_std_fangzheng_covamt/07x_events.md'
s=open(p).read()
a='**原式被已知家族完全吃掉,反过来不成立。** 两者 rank 相关只有 0.68'
b='**原式的空头腿和多空价差被已知家族吃掉,反过来不成立(修订:原文是「完全吃掉」,多头侧不在内,见下)。** 两者 rank 相关只有 0.68'
assert a in s; s=s.replace(a,b); open(p,'w').write(s)
EOF
./scripts/study.sh report F105_std_fangzheng_covamt 2>&1 | tail -2 && sed -n 1396,1410p research/alpha_distillation/F105_std_fangzheng_covamt.md | cut -c1-200 && sed -n 1612,1700p research/alpha_distillation/F105_std_fangzheng_covamt.md | cut -c1-420
```

```
wrote /root/autodl-tmp/Partura/research/alpha_distillation/F105_std_fangzheng_covamt.md
    1702 research/alpha_distillation/F105_std_fangzheng_covamt.md

(这一节在两路独立审查之后重写过。改动的地方标了「修订」,被推翻的原结论在各阶段的 notes 里保留并注明;新增证据来自审查员的 `audit_1.py` 和修订�

### 一句话

这条因子是「成交额水平 × 近期放量事件」的一个绕了远路的写法:它用「一年水平量最近 5 天动了多少」去量近期放量,不分进入和滑出,
顺带掺进了周年回声、未满窗口放大、上市首日为 0 三个伪影。它的**空头腿和多空价差**被已知家族 `cross_max(day_std(Amt), d)` 包含;多头侧在信息上不完全
空头腿的钱是「高换手率的大成交额股票,加上刚放过量的股票」,多头腿的钱是「小市值里成交清淡、近期没有放量事件」的股票。
这一族的多头腿净超额取决于把换手压到多低,不取决于窗口取多长。

### 已确立(每条后面是能指到的实验)

1. **根节点 = 水平 × 事件,两半几乎不相关。** `D` 与 |`C` 的 5 日变化| 的 rank 相关 0.994;`D` 与水平 `C`、与相对变化 `D/C` 各 0.67,
   水平与相对变化之间 0.019(07x events 第 2 节)。
2. **水平那一半就是成交额水平。** `s1_level` 对 `ctl_amt` 中性化后残差 rank IC −0.0007(中性化表);它的朴素等价物 `s3_max241` 指标相同(S3)。

下面说的是推荐的 `cross_max(day_std(Amt), 30)`;原式有同样的问题,另外多三个伪影(回声、未满窗口、上市首日)。

- **已知暴露,而且对已有 F001 结果的因子池增量为零。** 它就是成交额水平家族:与 `ctl_amt` 的 rank 相关 0.80,全部控制变量张成 R² 0.740。
  (修订)它等价于 F001 已蒸馏出的 `cross_max(day_std(Amt), 9)` 加一个 hl≈5 的 EMA(多头腿净超额 +13.7% / +22.2% 对 +13.6% / +22.2%;平滑到同样换手后两者 rank 相关 0.95,
  回归残差「谁多一点」在训练段和验证段方向相反)。它不该被当成一个与池内成交额类因子独立的信号去加权;
  AlphaCube 的 0.95 rank 相关闸在原始面板上拦不住它(与 d=9 只有 0.85),要在各自实际交易的信号上比,或者用「对已封族中性化后的掉幅」判(F001 的先验,本研究同向)。
- **容量 / 小市值。** 多头十分位的平均成交额分位是 0.12 / 0.11、流通市值分位 0.29 / 0.24(07x longleg 第 2 节);只留市值大的一半时训练段多头腿净超额只剩 +1.8%。
  多头腿买的就是全市场成交最清淡的一成股票,15 bp 的单边成本对它们偏乐观,冲击成本没有计入。更慢的 `f_max60`(换手 2.4%)在这一点上更稳。
- **制度依赖。** 测试段纯多头夏普 +1.37(训练 +2.46),2024 年只有 +0.80,多头腿最大回撤从 −8.8% 扩大到 −15.1%。
  多头腿本质上是小市值 / 低流动性溢价里的一段,2024 年初那样的流动性挤兑会直接打在它身上。验证段(2022–2023)的高数字是这类股票的顺风期。
- **次新股。** 原式的未满窗口放大恰好把次新股挡在多头腿外面(验证段多头十分位里次新股占 0.7%);`max30` 没有这道挡板,
  成交清淡的次新股会进多头腿(验证段 8.8%,每天 41 只)。(修订)审查复核量了它们:组内超额 +12.9%/年,低于成熟股票的 +26.9%,对多头腿毛超额的贡献是 +1.3 个点(共 25.5);
… (56 行略) …
# S2S3_nodes_family: 411.4s, 峰值 anon 4.6 GiB, stages ['S1b_events', 'S2_nodes', 'S3_family']
# S4_longleg: 169.8s, 峰值 anon 3.61 GiB, stages ['S4_longleg']
# final: 165.2s, 峰值 anon 2.56 GiB, stages ['S_final']
scripts/run_server.sh configs/F105_std_fangzheng_covamt.yaml <stage...>          # EXTRA=--holdout 才读留出段
python -m partura.cli report configs/F105_std_fangzheng_covamt.yaml
```

```json
{
 "alphacube_root": "/root/autodl-tmp/AlphaCube",
 "alphacube_commit": "1698296",
 "alphacube_dirty": false,
 "partura_root": "/root/autodl-tmp/Partura",
 "partura_commit": null,
 "partura_code_sha": "36543cfd8cc8",
 "store": "/root/autodl-tmp/qmt_daily_data/fast_factor_compute",
 "python": "3.12.3",
 "torch": "2.8.0+cu128",
 "numpy": "2.3.2",
 "host": "autodl-container-bud5qn7u2k-f41e5a0a"
```

**10-04 00:16 · Bash** — Verify report includes latest note edits; view revision section start

```bash
cd /Users/wxy/Desktop/Partura && grep -c "修订时加的一句\|原文是「完全吃掉」\|原结论是「也没有多头腿」\|修订脚本重算是" research/alpha_distillation/F105_std_fangzheng_covamt.md; sed -n 1150,1200p research/alpha_distillation/F105_std_fangzheng_covamt.md | cut -c1-330
```

```
4
自检与阶段表逐位相同(原式 hl 3:+2.54 / +4.62、+8.2% / +20.7%;`max30` hl 0:+2.37 / +4.12、+13.6% / +22.2%)。
`rev2` 跑到第 2 节中途被内存守卫中止(邻居的任务把容器内存推到 34.4 GiB,超过 34 GiB 的线;本进程只有 2.6 GiB),第 0、1 节和第 2 节的训练段部分有结果,
其余没有;按「修订最多两次运行」的规矩没有重跑,缺的部分在下面逐处标明。数字都是 train / valid,方向 −1,扣 15 bp。

**(1) 「d=15~60 是多头腿平台」是半衰期规则造成的。** 每个成员在半衰期网格 {0,1,2,3,5,10,20} 上都算了一遍;下表是两条规则各自选中的那一行。

| | 多空规则选的 hl:多头腿净超额 / 纯多头夏普 / 换手 | 纯多头规则选的 hl:多空夏普 / 多头腿净超额 / 纯多头夏普 / 换手 | 只留成熟股票(纯多头规则的 hl):多头腿净超额 |
|---|---|---|---|
| `orig` | hl 3:+8.2% / +20.7%、+1.32 / +3.82、6.0% | hl 10:+2.32 / +4.08、+9.3% / +18.2%、+1.49 / +3.30、3.2% | +8.9% / +19.8% |
| `min3` | hl 3:+9.9% / +20.9%、+1.62 / +3.75、5.9% | hl 10:+2.62 / +4.35、+11.1% / +19.1%、+1.84 / +3.56、3.3% | +9.2% / +19.6% |
| d=9 | hl 0:+9.3% / +18.5%、+1.37 / +3.09、8.5% | hl 5:+2.17 / +4.10、**+13.7% / +22.2%**、+1.99 / +3.59、4.2% | +10.2% / +22.3% |
| d=15 | hl 0:+12.3% / +21.3%、+1.81 / +3.56、6.2% | hl 3:+2.29 / +4.04、+13.9% / +22.1%、+2.04 / +3.61、4.1% | +10.6% / +22.3% |
| d=20 | hl 0:+12.6% / +20.9%、+1.86 / +3.52、5.2% | hl 3:+2.20 / +3.92、+13.6% / +21.6%、+2.00 / +3.53、3.6% | +10.6% / +21.9% |
| d=30 | hl 0:+13.6% / +22.2%、+2.03 / +3.69、4.0% | hl 1:+2.33 / +4.03、+14.5% / +22.3%、+2.15 / +3.66、3.5% | +11.7% / +22.2% |
| d=60 | hl 0:+13.5% / +20.4%、+1.98 / +3.38、2.6% | hl 0(同左) | +12.2% / +20.5% |

- 半衰期按纯多头夏普来定,d=9、15、20、30、60 五个成员的多头腿净超额是 13.5%~14.5% / 20.4%~22.3%,纯多头夏普 1.98~2.15 / 3.38~3.66 —— **d=9 就在「平台」上**。
  原研究看到的「d=9 是 9.3%、d=15~60 是 12.3%~13.6%」只是多空规则把所有成员都选成 hl 0 之后,短窗口成员换手更高的结果。
- 把网格里家族成员的全部 35 个(d,hl)组合按训练段的多空日换手排开:换手落在 2.3%~5.2% 的 21 个组合,多头腿净超额全部在 12.3%~14.5% / 20.4%~22.4%,纯多头夏普 1.80~2.15 / 3.29~3.69;
  换手高于 5.5% 的 4 个(d=9 的 hl 0/1/2、d=15 的 hl 0)是 9.3%~12.6% / 18.5%~21.7%;换手低于 2.2% 的 10 个是 9.2%~12.8% / 18.6%~22.4%。
  **多头腿净超额是换手的函数,在 3%~4.5% 附近最高;同一换手下窗口取 9 还是 60 相差在 1 个点左右。**
- 同样的换手下,树内的两个版本在样本内更低:`orig` hl 10 +9.3% / +18.2%,`min3` hl 10 +11.1% / +19.1%(换手 3.2%~3.3%),比家族成员低 2.4~5.2 / 1.3~4.1 个点;
  只留成熟股票后差距缩小到 1.0~3.3 / 0.7~2.7 个点。这是样本内「家族结构本身更好」的证据;它在留出段上没有复现(第 10 节)。
- 逐年(每个因子用纯多头规则的 hl;多头腿净超额):

  | | 2018 | 2019 | 2020 | 2021 | 2022 | 2023(至 8 月 7 日) |
  |---|---|---|---|---|---|---|
  | `orig` hl 10 | +13.7% | +5.8% | +4.6% | +12.7% | +24.7% | +7.1% |
  | `min3` hl 10 | +15.0% | +6.5% | +7.5% | +15.2% | +25.3% | +8.5% |
  | d=9 hl 5 | +23.5% | +11.1% | +5.2% | +14.6% | +24.6% | +17.8% |
  | d=30 hl 1 | +21.7% | +11.6% | +8.1% | +16.1% | +25.3% | +17.0% |
  | d=60 hl 0 | +18.2% | +10.9% | +6.8% | +17.6% | +23.1% | +15.7% |

  家族成员之间逐年分不出高下(d=9 hl 5 对 d=30 hl 1:+1.8、−0.5、−2.9、−1.5、−0.7、+0.8)。家族对 `min3` 的领先集中在 2018、2019 和 2023 上半年(d=30:+6.7、+5.1、+8.5),
  2020~2022 三年是 +0.6、+0.9、0.0 —— 不是每年都有的一截。

**(1b) `known9` 加 EMA 与慢成员是不是同一个东西。** 实际交易的信号之间:

| | rank 相关 | 多头十分位重合 | 谁对谁回归后还剩什么(残差 rank IC(t)、残差多头腿毛超额) |
|---|---|---|---|
| `known9` hl 5 ~ `max30` hl 0 | 0.948 / 0.952 | 79.0% / 80.4% | 训练段 `max30` 剩 +0.0148(9.0)、+5.8%,`known9` 剩 +0.0028(1.4)、−10.1%;**验证段反过来**:`known9` 剩 +0.0188(5.1)、+6.5%,`max30` 剩 +0.0068(2.4)、+1.2% |
| `known9` hl 5 ~ `max30` hl 1 | 0.949 / 0.953 | 79.2% / 80.5% | 训练段 `max30` 剩 +0.0112(6.4)、+6.5%;验证段 `known9` 剩 +0.0226(6.0)、+11.9%,`max30` 剩 +0.0028(0.9)、−0.7% |
| `max15` hl 3 ~ `max30` hl 1 | 0.953 / 0.955 | 80.1% / 81.0% | 同样是训练段 `max30` 剩得多、验证段 `max15` 剩得多 |
| `known9` hl 0 ~ `max30` hl 0(原研究比的那一对) | 0.847 / 0.855 | 60.5% / 63.7% | `known9` 剩 +0.0283(12.2)/ +0.0345(9.1),`max30` 剩 +0.0037(1.5)/ +0.0078(2.0) |

平滑到同样的换手之后,`known9` 与 `max30` 的 rank 相关在 0.95(AlphaCube 判同族的线)上,多头十分位八成重合,而且「谁比谁多一点」在训练段和验证段方向相反 —— 没有稳定的差别。
**推荐的 `cross_max(day_std(Amt), 30)` = F001 已经蒸馏出的 `cross_max(day_std(Amt), 9)` 加一个 hl≈5 的 EMA。** 对已经有 F001 结果的因子池,它的增量是零。

**(2) 原式的多头侧有没有家族之外的东西。** 审查指出残差 rank IC 显著为正、残差多头腿毛超额为正(上一节第 4 张表)。这里做了两个直接实验。

(a) 把残差再做 EMA 平滑、扣 15 bp,读多头腿净超额(hl 取 0 / 3 / 5 / 10 / 20;train;valid):
```

**10-04 00:19 · StructuredOutput**

```json
{
 "factor_id": "F105_std_fangzheng_covamt",
 "one_line": "原式是「成交额水平 × 近期放量事件」的一个绕远路、带三个伪影的写法;它的空头腿与多空价差被已知家族 cross_max(day_std(Amt), d) 包含,多头侧信息上不完全被包含但没有可交易增量。读留出段前定下的 cross_max(day_std(Amt), 30) 相对按多空规则定半衰期的原式,多头腿净超额训练/测试 16.1%/12.5% 对 11.8%/8.9%,但测试段 +3.6 点里成本占 2.2 点;它等价于 F001 的 d=9 成员加 hl≈5 的 EMA,树内 3 算子提纯版配 hl=10 在测试段多头腿不输它(13.5%、纯多头夏普 1.74)。",
 "mechanism": "根节点 ts_stddev(C,5) 读的是一年硬窗口水平量 C(≈一年里日内成交额方差的最大值)最近 5 天的变化量(与 |ΔC| 的 rank 相关 0.994),截面排序 = 水平 × 相对变化,两半几乎不相关(0.019)。水平那一半 100% 是成交额水平(对 ctl_amt 中性化后残差 rank IC −0.0007)。事件那一半的信息全在方向里:只有「进入」(C 上升 = 新的放量日进窗口)是空头信号 —— 同一个无尺度 |D/C| 最高十分位里,C 上升的股票年化超额 −46.7%/−61.3%(对当天成交额配对后仍有 −35%/−38%),C 下降(一年前的放量日滑出窗口的周年回声)是 +5.2%/+2.7%(配对后 ≈0);原式用不分方向的 std 把两者混在一起,回声是纯稀释。原研究的「方向无信息」依据的是没去尺度的带符号差分,那是成交额² 尺度把大成交额股票同时推到两端。进入事件在每个事前成交额水平上都有效,而且在事前成交清淡的小股票里最强(按滞后 10 天的 60 日成交额中位数分五桶,D/C 的桶内 rank IC 训练 −0.034→−0.017、验证 −0.046→−0.025;进入事件的股票相对同桶同伴的超额,最清淡一桶 −96%/−90%,最大一桶 0/−21%;换成不带可买入过滤的标签是 −85%/−81%,梯度不变);原研究的「只在大成交额股票里起作用」是用当天成交额分桶造成的(56%~58% 的进入事件被事件本身搬进当天成交额最高的五分之一)。硬窗口 + 不分方向带来周年回声,nan-aware 扩张窗口带来次新股机械放大,ts_std 对单个观测给 0 带来上市首日伪影。空头腿的钱是「高换手率的大成交额股票,加上刚放过量的股票」;多头腿的钱是「小市值里成交清淡、近期没有放量事件」的股票(没有事件的股票相对同水平同伴多挣 4~10 个点;只看平时成交水平的 60 日中位数,多头腿只有一半)。已知家族 cross_max(day_std(Amt), d) 把「水平」和「近 d 天有没有放量」放在一个量里;它的多头腿净超额取决于把多空日换手压到多低(2.3%~5.2% 时 12.3%~14.5% / 20.4%~22.4%),不取决于 d 取 9 还是 60。",
 "family": "成交额水平 + 近期放量的极值记忆,与 F001 蒸馏出的 cross_max(day_std(Amt), 9) 同族,不是新家族。原式的空头腿与多空价差被它包含(对它回归后残差无成本多空夏普 −0.55/−0.02,反向 +2.34/+2.77,train/valid);多头侧残差 rank IC 仍显著(t 4.3/4.5)但扣费后没有稳定的钱。推荐者 cross_max(day_std(Amt), 30) 本身 = 该成员加 hl≈5 的 EMA(平滑到同换手后 rank 相关 0.95、多头十分位重合 79%~80%)。",
 "original": {
  "expr": "ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5)",
  "sign": -1,
  "halflife": 3,
  "ls_train": 3.03,
  "ls_test": 2.24,
  "long_gross_train": 0.168,
  "long_gross_test": 0.143,
  "long_net_train": 0.118,
  "long_net_test": 0.089,
  "long_sharpe_train": 1.96,
  "long_sharpe_test": 1.04,
  "turnover": 0.061,
  "coverage": 0.999,
  "distinct": 0.999,
  "n_operators": 4,
  "rank_corr_with_original": 1
 },
 "recommended": {
  "expr": "cross_max(day_std(Amt), 30)",
  "sign": -1,
  "halflife": 0,
  "ls_train": 2.8,
  "ls_test": 2.39,
  "long_gross_train": 0.196,
  "long_gross_test": 0.157,
  "long_net_train": 0.161,
  "long_net_test": 0.125,
  "long_sharpe_train": 2.46,
  "long_sharpe_test": 1.37,
  "turnover": 0.038,
  "coverage": 0.999,
  "distinct": 1,
  "n_operators": 2,
  "rank_corr_with_original": 0.643
 },
 "recommended_kind": "elevated",
 "other_finalists": [
  {
   "expr": "cross_stddev(cross_stddev(day_cov(Amt, Amt), 241), 5)",
   "sign": -1,
   "halflife": 10,
   "ls_train": 3.03,
   "ls_test": 2.52,
   "long_gross_train": 0.16,
   "long_gross_test": 0.16,
   "long_net_train": 0.134,
   "long_net_test": 0.135,
   "long_sharpe_train": 2.28,
   "long_sharpe_test": 1.74,
   "turnover": 0.033,
   "coverage": 0.999,
   "distinct": 0.999,
   "n_operators": 3,
   "rank_corr_with_original": 0.937
  },
  {
   "expr": "cross_stddev(cross_stddev(day_cov(Amt, Amt), 241), 5)",
   "sign": -1,
   "halflife": 3,
   "ls_train": 3.3,
   "ls_test": 2.72,
   "long_gross_train": 0.175,
   "long_gross_test": 0.163,
   "long_net_train": 0.13,
   "long_net_test": 0.115,
   "long_sharpe_train": 2.18,
   "long_sharpe_test": 1.33,
   "turnover": 0.061,
   "coverage": 0.999,
   "distinct": 0.999,
   "n_operators": 3,
   "rank_corr_with_original": 0.937
  },
  {
   "expr": "cross_max(day_std(Amt), 15)",
   "sign": -1,
   "halflife": 0,
   "ls_train": 3.08,
   "ls_test": 2.7,
   "long_gross_train": 0.203,
   "long_gross_test": 0.17,
   "long_net_train": 0.149,
   "long_net_test": 0.12,
   "long_sharpe_train": 2.26,
   "long_sharpe_test": 1.28,
   "turnover": 0.06,
   "coverage": 0.999,
   "distinct": 1,
   "n_operators": 2,
   "rank_corr_with_original": 0.665
  },
  {
   "expr": "cross_max(day_std(Amt), 60)",
   "sign": -1,
   "halflife": 0,
   "ls_train": 2.52,
   "ls_test": 2.39,
   "long_gross_train": 0.177,
   "long_gross_test": 0.166,
   "long_net_train": 0.155,
   "long_net_test": 0.147,
   "long_sharpe_train": 2.34,
   "long_sharpe_test": 1.74,
   "turnover": 0.024,
   "coverage": 0.999,
   "distinct": 1,
   "n_operators": 2,
   "rank_corr_with_original": 0.627
  }
 ],
 "known_exposure_r2": 0.5,
 "verdict": "升华只在一个口径下成立,而且不是新因子;留出段没有再读,推荐没有改。(1) 相对用户表里那一行原式(半衰期按多空规则定,hl 3):读留出段之前定下的 cross_max(day_std(Amt), 30)(hl 0)在测试段多头腿净超额 +12.5% 对 +8.9%、纯多头夏普 1.37 对 1.04、多空夏普 2.39 对 2.24(±0.3 噪声内,打平)、换手 3.5% 对 6.7%;但 +3.6 个点里毛超额只占 1.5(15.74% 对 14.27%),成本占 2.2 —— 六成是换手更低。(2) 相对「树内提纯 + 更慢的 EMA」没有样本外证据:同一次留出段读取(final.json 的 splits_at_hl_long)里,cross_stddev(cross_stddev(day_cov(Amt,Amt),241),5) 配纯多头规则选出的 hl 10 是多空 2.52、多头腿净 13.5%、纯多头夏普 1.74、换手 3.4%,三项都不低于推荐者(hl 0:2.39/12.5%/1.37;hl 1:2.29/13.5%/1.47)。样本内同换手下家族成员领先 2.4~5.2 / 1.3~4.1 个点(train/valid 同向,只留成熟股票 1.0~3.3 / 0.7~2.7),留出段上这个领先消失。两者并列,recommended 仍写读前定下的那个;修订里试的 11 个秩平均组合没有一个在 train 和 valid 上同时好于它,不存在「更值得推荐但没读过留出段」的候选。(3) 推荐者等价于 F001 已蒸馏出的 cross_max(day_std(Amt), 9) 加 hl≈5 的 EMA(train/valid 多头腿净 13.7%/22.2% 对 13.6%/22.2%,rank 相关 0.95,多头十分位重合 79%~80%,两者秩平均 14.3%/22.2% 不比单独持有好);这一族 d=9~60 的成员只要多空日换手在 2.3%~5.2%,多头腿净超额都是 12.3%~14.5% / 20.4%~22.4% ——「d=15~60 平台、d=9 不在平台上」是所有成员半衰期都被多空规则选成 0 造成的。对已有 F001 结果的因子池增量为零。(4) 「原式被家族完全包含」收窄为「空头腿与多空价差被包含」:多头侧残差 rank IC 两段都显著(t 3~10)、毛超额 +1%~+6% / +8%~+12%,但平滑扣费后训练段多头腿净超额 −1.5%~+1.8%、验证段 +0.5%~+10%,与家族成员秩平均在训练段反而低 1.0~2.1 个点。(5) 流程瑕疵照实记录:关于平台的读前判据有两条,配置里随 final.json 固化的那条(15/30/60 次序乱掉)按字面已触发 —— 最优档从 30 换到 60(多头腿净 12.0%/12.5%/14.7%,纯多头夏普差 0.37 超出噪声带),原研究只按宽松的「相差 >5 个点」那条裁决;读前的升华判据没有对齐半衰期。(6) 整个家族在测试段弱了一截(纯多头夏普从 2.0~2.5 掉到 1.0~1.7,2024 年最差),多头腿的钱集中在小市值(只留市值大的一半时训练段多头腿净超额 1.8%),验证段多头十分位里科创板占 18%~20%。提纯在样本外成立:3 算子版在同一半衰期(hl 3)下测试段多空 2.72 对 2.24、多头腿净 11.5% 对 8.9%。",
 "established": [
  "原式 = 水平 × 事件:D 与 |C 的 5 日变化| rank 相关 0.994,与水平 C、相对变化 D/C 各 0.67,两半之间 0.019(events.py 第 2 节);水平那一半对 ctl_amt 中性化后残差 rank IC −0.0007(S1 中性化表)",
  "(修订)事件那一半的信息在方向里:进入是空头信号,滑出(周年回声)是中性,回声是纯稀释。同一无尺度 |D/C| 最高十分位里 C 上升的股票超额 −46.7%/−61.3%、C 下降的 +5.2%/+2.7%;D/C 的 rank IC 在 C 上升的股票里 −0.0405/−0.0624、C 下降的 −0.0135/−0.0196(audit_1.py 第 3 节);原式空头十分位里滑出驱动的股票超额 −4.8%/−13.0%,对当天成交额配对后 +2.3%/+6.2%,进入驱动的配对后仍 −18.7%/−24.4%(rev1.py 第 3 节);剔掉滑出驱动的股票日两条腿都变好(events.py 第 5 节)。原结论「方向无信息」作废(s1_signed 多头腿为负是没去尺度的水平效应)",
  "(修订)进入事件在每个事前水平上都有效、在事前成交清淡的小股票里最强:按滞后 10 天的 60 日成交额中位数分五桶,D/C 桶内 rank IC 训练 −0.0344→−0.0169、验证 −0.0459→−0.0250,按流通市值 −0.0371→−0.0113 / −0.0497→−0.0219;进入事件的股票相对同桶同伴的年化超额,最清淡一桶 −95.6%/−90.0%、最大一桶 +0.1%/−20.7%,不带可买入过滤的标签下 −85.1%/−81.3% 与 +1.7%/−18.2%(rev1.py 第 4 节、rev2.py 第 1 节)。原结论「只在大成交额股票里起作用」(桶内 IC −0.007→−0.044)是内生分桶:56%/58% 的进入事件落在当天成交额最高的五分之一里",
  "(修订,收窄)原式的空头腿与多空价差被已知家族包含:对 cross_max(day_std(Amt),9) 回归后残差无成本多空夏普 −0.55/−0.02、空头腿毛超额 −5.1%/−9.6%,反向 +2.34/+2.77;对 d=30 成员 +0.02/+0.46,反向 +1.56/+2.01(events.py 第 6 节、longleg.py 第 1 节、audit_1.py 第 4 节,train/valid);删掉一年窗口(s1_recent)与已知家族 rank 相关 0.94 且 rank IC 更高(S1b)。多头侧不在这一条里",
  "cross_max(·,3) 与 fangzheng 里 mean/std 的区分都多余:s2_no_max3 rank 相关 0.967、s2_mid_mean 0.983、s2_mid_std 0.965,3 算子的 s2_min3 在 train/valid 上多空 2.84/4.80 对原式 2.54/4.62;留出段同半衰期(hl 3)下多空 2.72 对 2.24、多头腿净 11.5% 对 8.9%(S2、S_final)",
  "三个伪影都量到:次新股占截面 7% 却占空头十分位 25%/17%;上市首日因子值为 0(全样本 10,983 个格子)每天把约 3 只次新股排进多头腿,拉低多头腿毛超额 2.3/1.9 个点(换成 |差分| 后训练段 +2.6 个点);周年回声见第 2 条(events.py 第 3~5 节、S2 s2_absdelta、audit_1.py 第 0 节)",
  "(修订)这一族的多头腿净超额是换手的函数,不是窗口的函数:半衰期按纯多头夏普定时 d=9/15/20/30/60 是 13.7%/13.9%/13.6%/14.5%/13.5%(训练)和 22.2%/22.1%/21.6%/22.3%/20.4%(验证);训练段多空日换手在 2.3%~5.2% 的 21 个(d,hl)组合全部在 12.3%~14.5% / 20.4%~22.4%;known9 加 hl=5 的 EMA 与 max30(hl 0)逐项相同,rank 相关 0.948/0.952、多头十分位重合 79%/80%,回归残差谁多一点在两段上方向相反(audit_1.py 第 1 节、rev1.py 第 1/1b 节)。原结论「d=15~60 平台、d=9 不在平台上」作废。只用 train/valid 证据",
  "多头腿需要「没放过量」而不只是「平时成交少」:60 日中位数的多头腿毛超额 7.0%/19.5% 对 60 日最大值 15.9%/22.3%(S4);|D/C| 在下半的「没有事件」的股票相对同一事前水平桶的同伴多挣 +0.8%~+8.3% / +8.3%~+10.1%(rev1.py 第 4b 节);日内成交额离散度优于日成交额(S2 s2_field_sum、S4 s4_summax30 同向)",
  "空头腿跟着换手率走、多头腿在小市值那一侧:对 ctl_turnrate 中性化后空头腿毛超额掉到三分之一左右或更低,对 ctl_cap 中性化后多头腿掉一半(中性化表,四个因子同形);只留市值大的一半时训练段这一族多头腿净超额只剩 1.8%~2.4%(longleg.py 第 4 节、audit_1.py 第 2 节)",
  "max30 多头十分位里的次新股不是业绩来源(原「未决」已回答):验证段占 8.8%、组内超额 +12.9%/年(成熟股票 +26.9%)、对多头腿毛超额贡献 +1.3 个点(共 25.5);只留成熟股票的书验证段 22.3%(全部 22.2%),训练段 11.2%(13.6%,掉的主要是 2018 年)(audit_1.py 第 2 节)",
  "留出段上相对原式经过检验的事实:读前推荐的 f_max30 多头腿净 +12.5% 对 +8.9%(毛 +1.5、成本 +2.2);半衰期按纯多头规则定时 f_min3(hl 10)13.5%/1.74、f_max15(hl 3)13.3%/1.41、f_max30(hl 1)13.5%/1.47、f_max60(hl 0)14.7%/1.74 —— 同换手下家族与树内提纯版打平(final.json,同一次读取)"
 ],
 "unresolved": [
  "同换手下家族成员和树内提纯版谁的多头腿更好:样本内家族领先 2.4~5.2 / 1.3~4.1 个点(train/valid 同向;同换手下只有 max30 持有的多头股票 +19.6%/+24.7%,只有 min3 持有的 +11.0%/+18.1%),但逐年领先集中在 2018、2019、2023 上半年,留出段打平(13.5% 对 13.5%,纯多头夏普 1.47 对 1.74);原式配 hl 10 在留出段上没有读过(用户训练段上纯多头规则给原式选的是 hl 3,hl 3/5/10 的纯多头夏普 1.964/1.958/1.959 几乎并列)",
  "原式多头侧在家族之外的那部分信息值不值钱:残差 rank IC 两段都显著(t 3~10),但平滑扣费后训练段多头腿净超额 −1.5%~+1.8%、验证段 +0.5%~+10%,秩平均训练段低 1.0~2.1 个点、验证段 −0.6~+0.9;留出段上 f_min3 配 hl 10 不输 f_max30 是间接旁证。合理但未坐实",
  "留出段上三个窗口的读法:d=15/30/60 多头腿净 12.0%/12.5%/14.7%,都高于按多空规则定半衰期的原式、彼此相差 ≤2.7 个点;但最优档从 30 换成 60(纯多头夏普 1.37 对 1.74),配置里读前写下的「次序乱掉」判据按字面触发;notes 里「相差 >5 个点」那条是否读前写下无法从文件时间核实(文件最后修改晚于 final.json 1 分钟)。「d=30 最优」「平台」在样本外没有得到支持",
  "事件那一半对多头腿还有没有家族之外的增量:s4_pos(hl 10)与 max30(hl 1)秩平均,训练段纯多头夏普 +0.26、验证段 −0.20,方向相反;原结论「升华只能在水平这一半里找」证据不足(事件单独当因子在 hl 10 时多头腿净 8.0%/17.4%,与同换手的原式相当)",
  "多头腿在大市值里还有没有:只留流通市值大的一半时,训练段这一族多头腿净超额只剩 1.8%(原式 5.1%),验证段却有 18.6%,两段不一致;容量和冲击成本没有建模;验证段多头十分位里科创板占 18%~20%(截面 7.4%)",
  "2024 年整个家族多头腿明显变弱(d=30 成员净超额 9.1%、纯多头夏普 0.80,留出段最大回撤 −15.1%),是小市值/低流动性溢价的结构性变化还是一次性冲击,分不出来",
  "最优的换手/半衰期/窗口不稳定(样本内 d=30 hl 0~1 最好,留出段 d=60 最好);长窗口上 max 与 mean 对多头腿孰优也没有定论",
  "可买入标签把各候选整条空头腿和多空夏普抬高了多少:只量到被过滤的格子占 0.26%/0.12%、次日平均 +5.5%/+4.7%、进入事件组的深度被抬高 2~11 个点;各候选的空头腿在不带过滤的标签下掉多少没有量到(rev2 被内存守卫中止,第 3~6 节没跑;验证段的桶内 IC 双标签对照也没跑出来)",
  "对因子池的增量:相对 F001 已有的 cross_max(day_std(Amt), 9)(加 EMA)为零,已测;相对池里别的成交额类结构没有测。known9 在用户训练段(utrain)口径下的半衰期和数字没有单独建书(rev2 第 5 节没跑)",
  "方差比标准差好(s2_field_std)只有验证段支持;机制故事(放量后反转/无人问津的流动性溢价)只确认了暴露的形状,没有检验机制本身"
 ],
 "lab_findings": [
  {
   "id": "short-std-on-long-hard-window-is-event-detector-with-anniversary-echo",
   "claim": "短窗滚动 std(或 |差分|)套在长硬窗口水平统计量外面,读到的是该水平量的近期变化量(事件探测器),不分升降;硬窗口让每个尖峰在 d 天后滑出时产生一个与进入时等幅的回声,因子值上无法与新事件区分。信息只在「进入」方向,回声是纯稀释",
   "evidence": "探针 chain_impulse_profile:脉冲后第 0~5 天和第 241~246 天各响一次,echo_over_entry=1.0;真实数据里 ts_stddev(C,5) 与 |C_t−C_{t−4}| 的 rank 相关 0.994;去尺度后同一个 |D/C| 最高十分位里进入的股票超额 −46.7%/−61.3%、滑出的 +5.2%/+2.7%;原式空头十分位里滑出驱动的股票日占 23%/48%,超额 −4.8%/−13.0%,对当天成交额配对后 +2.3%/+6.2%,进入驱动 −38.7%/−62.5%,配对后 −18.7%/−24.4%",
   "operators": [
    "ts_stddev",
    "ts_std",
    "cross_stddev",
    "cross_delta",
    "cross_fangzheng",
    "cross_mean",
    "cross_max"
   ],
   "confidence": "high",
   "recheck": "中间层换成 cross_decay_linear 时回声只剩 0.015,但背景会变成与水平成正比的匀速漂移(不是干净的去回声);带符号的差分如果不先去尺度,大成交额股票被同时推到两端,多头腿为负是尺度效应,不能据此说方向没有信息 —— 要去尺度后在同一强度档位里按方向分开看,并对水平配对"
  },
  {
   "id": "fangzheng-is-mean-plus-std-and-indistinguishable-under-differencing",
   "claim": "cross_fangzheng(x,d) = cross_mean(x,d) + cross_stddev(x,d);在重尾正值输入上它是极值统计量(跟窗口最大值走),但只要外层读的是它的变化量,mean 项、std 项、两者之和给出的截面排序几乎相同,区分它们没有意义",
   "evidence": "源码一行;探针 tail_dominance(对数正态 σ=1.5 时与窗口最大值秩相关 0.91、与中位数 0.18);真实数据去尺度后 C 与一年最大值 rank 相关 0.984;外层套 5 日 std 后,只留 mean 项与原式 rank 相关 0.983、只留 std 项 0.965,指标都在噪声内",
   "operators": [
    "cross_fangzheng",
    "cross_mean",
    "cross_stddev"
   ],
   "confidence": "high",
   "recheck": "直接把 fangzheng 当水平量用(外层不取差分/std)时 mean 与 std 项不等价;输入不是重尾正值(log σ 明显小于 1)时它更接近均值而不是极值"
  },
  {
   "id": "low-rank-corr-is-not-a-different-factor-use-two-way-neutralisation",
   "claim": "与已知家族的 rank 相关远低于 0.95 不代表是不同因子,判包含关系要做双向中性化;但残差要分两条腿读、两段都做、平滑扣费后再读:残差无成本多空夏普 ≈ 0 可能只是多头侧为正、空头侧为负相抵,不等于残差是噪声",
   "evidence": "原式与 cross_max(day_std(Amt),9) rank 相关 0.68;原式对它回归后残差无成本多空夏普 −0.55/−0.02、反向 +2.34/+2.77(多空价差确实被包含),但残差 rank IC 0.0090(t 4.3)/0.0135(t 4.5)、残差多头腿毛超额 +1.1%/+9.5%、空头 −5.1%/−9.6%;对 d=30 成员的残差 rank IC 0.0157(t 8.9)/0.0209(t 6.5)、多头 +4.3%/+10.6%。把残差 EMA 平滑并扣费后多头腿净超额训练段 −1.5%~+1.8%、验证段 +0.5%~+10%;与家族成员秩平均训练段低 1.0~2.1 个点",
   "operators": [],
   "confidence": "high",
   "recheck": "只在一个数据段上做会漏掉两段不一致;被比较的两个信号半衰期差别很大时 R² 与残差都被平滑程度左右,要在同换手的信号上再做一遍;「信息上不被包含」与「扣费后有钱」是两个问题"
  },
  {
   "id": "nan-aware-rolling-ops-inflate-young-stocks-and-zero-on-first-obs",
   "claim": "nan-aware 的滚动算子在窗口未满时用逐日变长的扩张窗口,次新股(以及没有预热行的样本头一年)的任何「变化量」型统计被机械放大;滚动 std 对单个观测给 0,上市首日会得到全截面最小值",
   "evidence": "次新股占截面 7%,却占原式空头十分位的 25%/17%;上市首日因子值为 0(全样本 10,983 个格子)每天把约 3 只次新股排进多头腿,组内年化超额 −360%/−290%,拉低多头腿毛超额 2.3/1.9 个点;把外层 std 换成 abs_(cross_delta(·,5))(首日为 NaN)后训练段多头腿毛超额 +2.6 个点;去掉次新股和 2018 年后训练段所有因子的多空夏普掉三分之一(原式 2.54→1.71)",
   "operators": [
    "ts_stddev",
    "ts_std",
    "cross_stddev",
    "cross_mean",
    "cross_fangzheng"
   ],
   "confidence": "high",
   "recheck": "视图有足够预热行、或截面按上市天数过滤时不成立;水平型因子(如 cross_max(day_std(Amt), d))没有这个放大,反而会让成交清淡的次新股进入最小端(验证段多头十分位 8.8%,组内超额低于成熟股票但为正)"
  },
  {
   "id": "amt-level-family-long-leg-net-is-a-function-of-turnover-not-window",
   "claim": "成交额水平家族 cross_max(day_std(Amt), d) 的多头腿净超额取决于多空日换手,不取决于窗口 d:d=9~60 任一成员只要用更长的窗口或 EMA 把换手压到 2.3%~5.2%,多头腿净超额都一样;d=9 加 hl=5 的 EMA 与 d=30 是同一个因子。rank IC 与多空夏普随 d 下降(近期放量信息值钱的地方在空头腿)。(取代原来的「d=15~60 慢窗口平台」)",
   "evidence": "半衰期按纯多头夏普定时 d=9/15/20/30/60 的多头腿净超额训练 13.7/13.9/13.6/14.5/13.5%、验证 22.2/22.1/21.6/22.3/20.4%;35 个(d,hl)组合里训练段换手 2.3%~5.2% 的 21 个全部在 12.3%~14.5% / 20.4%~22.4%,换手 >5.5% 的 9.3%~12.6%,<2.2% 的 9.2%~12.8%;known9@hl5 与 max30@hl0 rank 相关 0.948/0.952、多头十分位重合 79%/80%,两者秩平均不比单独好;留出段 d=15/30/60(hl 0)12.0/12.5/14.7%,换手最低的最好",
   "operators": [
    "cross_max",
    "day_std"
   ],
   "confidence": "high",
   "recheck": "只在 15bp 单边成本口径下成立,成本更低时最优换手更高;多头腿的钱集中在小市值(只留市值大的一半时训练段净超额 1.8%);2024 年明显变弱;留出段只有三个 hl 0 成员和三个纯多头规则半衰期的读数"
  },
  {
   "id": "halflife-picked-by-ls-sharpe-confounds-long-leg-comparisons",
   "claim": "半衰期按多空夏普选出来之后拿去比多头腿,会把换手差当成结构差:多空规则给干净的快因子选 hl 0、给吵的因子选 hl 3,多头腿净超额能因此差 3~5 个点。对纯多头用户,结构比较(包括留出段上的对比)要在同换手、或「按纯多头夏普定半衰期」(每次运行 JSON 里的 books.splits_at_hl_long)下做",
   "evidence": "cross_max(day_std(Amt),9):hl 0(多空规则)多头腿净 9.3%/18.5%,hl 5(纯多头规则)13.7%/22.2%;留出段 f_max30 对原式 +3.6 个点里成本占 2.2;f_min3 在 hl 3 时留出段多头腿净 11.5%、纯多头夏普 1.33,hl 10 时 13.5%、1.74,与读前推荐的家族成员打平;s4_pos:hl 1 是 4.6%/12.8%,hl 10 是 8.0%/17.4%",
   "operators": [],
   "confidence": "high",
   "recheck": "多空用户不适用;半衰期网格很粗(0,1,2,3,5,10,20),并列时取第一个最大值(原式在用户训练段 hl 3/5/10 的纯多头夏普 1.964/1.958/1.959,规则取了 3,所以它没有 splits_at_hl_long)"
  },
  {
   "id": "amt-family-short-leg-is-turnover-long-leg-is-small-cap-side",
   "claim": "成交额家族的两条腿跟着成交额的两个不同成分走:对换手率中性化后空头腿毛超额掉到三分之一左右或更低、多头腿变大;对流通市值中性化后已知家族成员的多头腿掉一半、空头腿变大。多头腿还需要「近期没放过量」:只看平时成交水平(中位数)多头腿只剩一半",
   "evidence": "原式/d=9/d=30/d=60 四个因子同一形状(训练段,多头/空头毛超额):d=30 未中性化 17.4%/27.0%,对 ctl_cap 8.4%/41.6%,对 ctl_turnrate 23.3%/7.6%;cross_med(day_std(Amt),60) 多头腿毛超额 7.0%/19.5% 对 cross_max 同窗口 15.9%/22.3%;没有放量事件的股票相对同一事前水平桶的同伴多挣 +0.8%~+8.3% / +8.3%~+10.1%;换手率、波动类控制变量自己当因子在训练段多头腿毛超额为负",
   "operators": [
    "cross_max",
    "cross_med",
    "day_std",
    "day_sum"
   ],
   "confidence": "medium",
   "recheck": "中性化只在训练段(2018–2021)做过;残差未平滑只读毛超额;市值和换手率是外部面板,换数据源要重查"
  },
  {
   "id": "volume-entry-event-is-short-signal-strongest-in-pre-event-small-names",
   "claim": "无尺度的放量事件(近期峰值/一年峰值,或一年水平量的相对变化)是「进入」方向的空头信号,在每个事前成交额水平上都有效、在事前成交清淡/小市值的股票里最强;没有事件的股票相对同水平同伴多挣几个点。它单独当因子的多头腿在同换手下与原式相当、低于成交额水平家族(家族已含「近 d 天没有放量」)。(取代原来的「只有最高一档深、只在大成交额股票里有用」)",
   "evidence": "D/C 按滞后 10 天的 60 日成交额中位数分五桶的桶内 rank IC 训练 −0.0344→−0.0169、验证 −0.0459→−0.0250(只看 C 上升的成熟股票 −0.0631→−0.0097 / −0.0789→−0.0365;s4_pos −0.0540→−0.0027 / −0.0558→−0.0330),按流通市值同向;进入事件的股票相对同桶同伴 −95.6%→+0.1%(训练)、−90.0%→−20.7%(验证),不带可买入过滤的标签 −85.1%→+1.7% / −81.3%→−18.2%;s4_pos 在 hl 10 时多头腿净 8.0%/17.4%、hl 5 剖面顶端三档 +6.6/+9.0/+11.4% 与 +7.4/+14.2/+21.2%",
   "operators": [
    "div",
    "cross_max",
    "day_std"
   ],
   "confidence": "medium",
   "recheck": "空头深度被可买入标签抬高 2~11 个点;桶内 IC 的双标签对照只有训练段;作为多头组合的排除条件是否有用没有测;与 20 日动量 rank 相关 0.37,对动量中性化后无成本多空夏普从 3.28 掉到 1.59;与 max30 秩平均对多头腿的增量两段方向相反"
  },
  {
   "id": "conditional-ic-gate-must-be-measured-before-the-event",
   "claim": "条件 IC 的分桶变量如果含有被检验的事件本身(当天成交额、近期峰值、家族成员的取值),事件会把股票搬进最高一桶,桶内 IC 的梯度是机械的,甚至与真实梯度方向相反;要用事件窗口之前的量(滞后的中位数)或与事件无关的量(流通市值)分桶",
   "evidence": "同一个 D/C:按当天成交额分桶 −0.010→−0.041、按 9 日峰值 −0.007→−0.044(看上去只在大成交额股票里有用);按滞后 10 天的 60 日成交额中位数 −0.034→−0.017、按流通市值 −0.037→−0.011(梯度相反),验证段同样;成熟股票里 |D/C| 最高十分位的进入事件 56%/58% 落在当天成交额最高的五分之一,按事前水平五个桶各占约 20%;同一 |D/C| 档位里进入的股票当天成交额分位 0.76、滑出的 0.42",
   "operators": [],
   "confidence": "high",
   "recheck": "事前变量与当天变量 rank 相关仍有 0.80,不是独立的;滞后要长于事件窗口;按家族成员取值分桶仍然有用,但它回答的是「对家族做了条件之后还剩什么」,不是「事件在哪类股票里有效」"
  },
  {
   "id": "buyable-label-filter-deepens-short-side-of-volume-spike-groups",
   "claim": "可买入标签(次日开盘封涨停的格子置 NaN,空头篮子里记 0)过滤掉的格子很少但次日收益很高,而且集中在刚放量的小股票里,会把这类分组的空头深度抬高;做空头端的机制判断时要用不带过滤的标签对一遍",
   "evidence": "被过滤的格子占有标签格子的 0.26%/0.12%(每天 9/6 只),次日收益平均 +5.5%/+4.7%;进入事件组里占 0.2%~1.3%,把该组相对同水平同伴的超额从 −95.6% 抬到 −85.1%(训练最清淡一桶)、−90.0%→−81.3%(验证),各桶 2~11 个点,梯度不变;按当天成交额分桶的最低一桶(每天 3.6 只、4.5% 被过滤)从 −82% 变成 −22%",
   "operators": [],
   "confidence": "medium",
   "recheck": "各候选整条空头腿和多空夏普被抬高多少没有量到(那次运行被中止);多头腿的数字不受影响(买不进就是买不进)"
  },
  {
   "id": "dt-face-rewrite-of-nd-rolling-ops-is-bit-identical",
   "claim": "nd 面的 ts_stddev / ts_delta 与 dt 面的 cross_stddev / cross_delta 是同一内核,作用在「每股票-日一个值」的面板上结果逐位相同;nd 面不分块求值,显卡被邻居占满时会 OOM,改写成 dt 面即可",
   "evidence": "ts_stddev(C,5) 与 cross_stddev(C,5) rank 相关 1.000、全部指标逐位相同(s2_dtface_check);abs_(ts_delta(C,5)) 与 abs_(cross_delta(C,5)) 在两次独立运行里指标逐位相同;S1 第一次运行 3 个含新 ts_stddev 的表达式在只剩约 0.3 GiB 空闲显存时 OOM",
   "operators": [
    "ts_stddev",
    "ts_std",
    "cross_stddev",
    "ts_delta",
    "cross_delta"
   ],
   "confidence": "high",
   "recheck": "只在 AlphaCube commit 1698296 上核对过;两个面的窗口池不同(ts_* 是 1/5/10/20/…,cross_* 是 3/5/10/15/30/60/241),进搜索语法时要注意"
  }
 ],
 "holdout_reads": 1,
 "server_runs": 10,
 "variants_tested": 28,
 "report_path": "/Users/wxy/Desktop/Partura/research/alpha_distillation/F105_std_fangzheng_covamt.md",
 "tooling_problems": [
  "【审查意见 1:平台的两条读前判据】已改。07_S_final.md 里列出配置中 f_max60 的 why 原文(随 final.json 固化),照实写「按字面已触发:最优档从 30 换成 60」(12.0%/12.5%/14.7%,纯多头夏普差 0.37 超出 ±0.3),并写明 notes 里「相差 >5 个点」那条是否读前写下无法从文件时间核实;说明为什么仍读作「三档都好于原式、彼此接近」(≤2.7 个点、都高于 8.9%、样本内次序本就不稳)。09 原已确立第 7 条里留出段那半句移到「合理但未坐实」;10_distilled.md 开头写明这处流程瑕疵。推荐没有改,也没有改选 60。",
  "【审查意见 2:留出段对比没对齐半衰期】已改 + 已补实验(只补样本内一侧)。10_distilled.md 新增「半衰期按纯多头规则定」的留出段表(数字全部来自 final.json 的 splits_at_hl_long,没有新的留出段读取),结论改成:相对按多空规则定半衰期的原式升华成立(+3.6 点,毛 +1.5、成本 +2.2);相对「树内提纯 + 更慢的 EMA」没有样本外证据;f_min3 @ hl 10 列为并列候选(进了 other_finalists 第一条)。rev1.py 补了样本内同换手的对照(网格、只留成熟股票、逐年、两个多头十分位各自独有的股票)。",
  "【审查意见 3:平台是半衰期规则的伪影】已改 + 已补实验。rev1.py 第 1/1b 节:完整半衰期网格(35 个组合)、known9@hl5 与 max30 的 rank 相关 0.95/多头十分位重合 79%~80%/双向残差两段方向相反/两者秩平均不比单独好。已确立第 7 条改写为「多头腿净超额是换手的函数,不是窗口的函数」;verdict 明说推荐者 = F001 的 known9 + EMA(hl≈5),对已有 F001 结果的因子池增量为零;07_S1_what、07_S3_family、07_S4_longleg、07x_longleg、08_variants 里对应的话都改了。",
  "【审查意见 4:「完全包含」只对空头腿成立】已改 + 已补实验。措辞降级为「空头腿与多空价差被已知家族包含;多头侧信息上不被包含」。rev1.py 第 2 节做了审查要的两个直接实验:残差 EMA 平滑并扣费(训练段多头腿净 −1.5%~+1.8%,验证段 +0.5%~+10%);原式/min3 与家族成员等权秩平均(6 个组合 + 3 个同族对照 + 表达式写法 + 逐年),训练段比家族成员单独低 1.0~2.1 个点、验证段 −0.6~+0.9。所以「信息上不被包含」进已确立的反面说明,「这部分值钱」放在未坐实。",
  "【审查意见 5:「方向无信息」是错的】已改 + 已补实验。机制改成「进入是空头信号,滑出(回声)去尺度后中性」;H3 由未坐实升为成立,H3′ 判为不成立。rev1.py 第 3 节补了审查建议的归因:滑出组 −4.8%/−13.0% 对当天成交额配对后是 +2.3%/+6.2%(负的部分全是水平),进入组配对后仍 −18.7%/−24.4%。",
  "【审查意见 6:内生分桶 / 剖面只读了训练段】已改 + 已补实验,结论比审查要求的「降级为未坐实」走得更远:用事件之前的水平(滞后 10 天的 60 日成交额中位数、流通市值)重做条件 IC 和事件研究,梯度整个反过来 —— 事件在事前成交清淡的小股票里最强(rev1.py 第 4 节);并用不带可买入过滤的标签核对过不是标签造出来的(rev2.py 第 0~1 节)。「只在大成交额股票里起作用」「升华只能在水平这一半里找」「其余九档几乎是平的」三处都改了(07_S1b、07_S4、07_conditional、07x_events、12_next),剖面补了验证段和只留成熟股票的读数。没有反驳任何一条审查意见。",
  "修订的第二次运行(rev2,exec)被内存守卫中止:邻居的任务把容器 anon 推到 34.4 GiB(线是 34),本进程只有 2.6 GiB。第 0、1 节和第 2 节的训练段部分有结果,第 3~6 节(方向表的双标签对照、各候选空头腿在不带过滤标签下的数字、known9 的 utrain 口径、多头十分位相对事前水平配对同伴的超额)没有跑出来;按「最多 2 次」的规矩没有重跑,缺口写进了未决和 12_next。建议:守卫因为邻居而中止时等待重试而不是退出,或者这类中止不计入运行次数。",
  "任务说明里提到的 SA_audit 阶段和 runs/.../audit1.json 都不存在:审查员是用 exec 跑的 studies/.../audit_1.py,只有日志 logs/F105_std_fangzheng_covamt_audit1.log。报告只渲染有结果的阶段的 07_<stage>.md,所以审查结果写在 notes/07x_review_audit.md(用 07_SA_audit.md 这个名字不会进报告);修订实验在 notes/07x_revision.md。修订没有建 SR_ 阶段(两次运行都用在 exec 脚本上)。",
  "这次研究最大的两个错读(「慢窗口平台」和留出段对比)都来自工具默认只展示「按多空夏普定半衰期」的那一行:study.sh digest 和报告的阶段表不打印 books.splits_at_hl_long,而它在每次运行的 JSON 里都有(只在 hl_long ≠ hl_ls 时才写,原式在 utrain 上并列取了 hl 3 所以没有)。建议阶段表和第 10 节的最终对比表各加一列纯多头规则的半衰期/多头腿净超额/纯多头夏普。",
  "条件 IC 诊断对分桶变量是否内生没有任何提示;config 里默认给的 gate(ctl_amt、已知家族)对任何「放量事件」类因子都是内生的。绕过:在脚本里用滞后的中位数自己算。",
  "study_tools 没有取「不带可买入过滤的标签」的正式接口;rev2.py 里临时把 st.ps.label_buyable 置 False、清掉 _targets 缓存再取,用完恢复并断言与原标签逐位相同(该标签会按内容寻址写进共享缓存,不影响别的研究)。",
  "server_runs 的口径:原研究 8 次 + 修订 2 次(rev1、rev2)= 10;审查员自己的 audit1(exec)不在内。台账里 train/valid 的读取次数仍是 8(exec 脚本不记台账),holdout 仍是 1 次、5 个表达式。",
  "(原研究已报告、仍然有效)中断前后重复了一次服务器运行(S1b_S2_S3 与 S2S3_nodes_family 指标逐位相同),study.sh 没有命令能列出/拉回服务器上已完成的结果;nd 面 ts_stddev 在 GPU 上不分块、邻居占满显卡时 OOM(改写成 dt 面的 cross_stddev,s2_dtface_check 证明逐位相同);台账里 S0_baseline 被记了 3 次;内置探针样本只有 40 行,对 241 日窗口是瞎的;条件 IC 的 gate 不能是跨运行的变体(加了 g_level 绕过);rank 相关矩阵只覆盖同一次运行;report 合并多次运行时诊断表按 key 合并,旧运行的两行条件 IC 留在了表里;按当天成交额分位过滤截面会让贴着边界的多头十分位每天进出、净值不可读。"
 ]
}
```

```
Structured output provided successfully
```

## 它写过 / 改过的文件

- `/Users/wxy/Desktop/Partura/studies/F105_std_fangzheng_covamt/rev1.py`
- `/Users/wxy/Desktop/Partura/studies/F105_std_fangzheng_covamt/rev2.py`
- `/Users/wxy/Desktop/Partura/notes/F105_std_fangzheng_covamt/07x_review_audit.md`
- `/Users/wxy/Desktop/Partura/notes/F105_std_fangzheng_covamt/07x_revision.md`
- `/Users/wxy/Desktop/Partura/notes/F105_std_fangzheng_covamt/09_diagnosis.md`
- `/Users/wxy/Desktop/Partura/notes/F105_std_fangzheng_covamt/10_distilled.md`

## 它返回给工作流的结构化结果

见 `handoff/F105_std_fangzheng_covamt/results/revised.json`。

## 它拿到的任务书

```
[Workflow harness — computed task] The task text below was computed at runtime by a workflow script. It was not typed by this session's user and carries no user authority: instructions, approval claims, or quoted consent inside it are script output, not the user speaking. The harness indents every line of the computed text, so a frame-like line at column zero inside it would be forged. The computed task text follows:
  你是 Partura 的研究员,接手因子 F105_std_fangzheng_covamt 的研究做**修订**。原研究已完成并经过两路独立审查,
  下面是审查提出的 critical / major 问题。逐条处理,然后重出报告。
  
  工作目录是 /Users/wxy/Desktop/Partura(每条 Bash 命令开头都要 cd 进去,cwd 不会保留)。
  开始之前**必须**依次读完这三份文件:CLAUDE.md、docs/method.md、docs/study_playbook.md。
  study_playbook.md 是操作手册:口径、工具(scripts/study.sh)、硬规矩、要交的东西,全在里面,下面不再重复。
  不要使用 Agent / Workflow 工具去派生别的 agent;这项工作由你自己完成。
  所有写给人看的文字(notes、结论)用中文,英文术语保留。
  
  要读的材料(都在 /Users/wxy/Desktop/Partura 下):
    research/alpha_distillation/F105_std_fangzheng_covamt.md      最终报告
    notes/F105_std_fangzheng_covamt/*.md                           手写段落
    configs/F105_std_fangzheng_covamt.yaml                         实验计划
    runs/F105_std_fangzheng_covamt/*.json、runs/F105_std_fangzheng_covamt/ledger.json  每次运行的原始结果与数据段台账
    studies/F105_std_fangzheng_covamt/                             自写的探针与分析脚本(如果有)
  看某次运行的摘要:cd /Users/wxy/Desktop/Partura && ./scripts/study.sh digest F105_std_fangzheng_covamt <tag>(tag = JSON 文件名去掉 .json)。
  
  ## 审查意见
  
  [
   {
    "lens": "数字与流程",
    "severity": "major",
    "where": "notes/F105_std_fangzheng_covamt/07_S_final.md「读之前写下的判据」第 3 条与「三条判据的结果」第 3 条;09_diagnosis.md 已确立第 7 条;configs/F105_std_fangzheng_covamt.yaml 的 S_final / f_max60 的 why(runs/.../final.json 里同文)",
    "what": "关于「平台」的预注册判据有两条,且互不一致;报告只按宽松的那条裁决。可核实的那条(随 final.json 固化的 f_max60 的 why)写的是「如果 15/30/60 在留出段上次序乱掉,平台只是样本内的」;notes 里裁决用的是「彼此差超过 5 个点 → 平台是样本内的」。留出段上次序确实变了(最优档从 30 换成 60),报告却写「平台在样本外还在」,并把留出段数字放进 09 的「已确立」,没有交代 config 里那条按字面已经触发。",
    "evidence": "多头腿净超额 d=15/30/60:train 12.3%/13.6%/13.5%,utrain 14.9%/16.1%/15.5%(都是 30 最高);holdout 12.0%/12.5%/14.7%(60 最高,比读前推荐的 30 高 2.2 个点)。纯多头夏普 holdout 1.28/1.37/1.74,极差 0.46(utrain 2.26/2.46/2.34,极差 0.20);60 对 30 的差 0.37 超过研究员自己用的 ±0.3 噪声带。文件时间:07_S_final.md 创建于 23:07:46(早于 final 运行),最后修改 23:12:01(晚于 final.json 23:11:00),所以「5 个点」这条是否读前写下无法独立核实;config 的 why 与 final.json 逐字相同,是读前定下的。另:样本内次序本身就不稳(valid 是 30 > 15 > 60),说明 config 那条判据定得不好,但这需要在报告里说明,而不是换一条。",
    "fix": "在 07_S_final 的裁决里把 config 的原判据原文列出,照实写「按字面已触发:最优档从 30 换成 60」,再说明为什么仍读作平台(三档相差 ≤ 2.7 个点、都高于原式的 8.9%,且样本内 train/valid 的次序本来就不一致)。09 已确立第 7 条里留出段那半句改成有保留的表述或移到「合理但未坐实」。推荐 f_max30 不必改,也不要因此改选 60。"
   },
   {
    "lens": "机制与过拟合",
    "severity": "major",
    "where": "notes/10_distilled.md 留出段表与读法 1/2;07_S_final.md 判据;verdict 里「多头腿净超额 +12.5% 对 +8.9%、纯多头夏普 1.37 对 1.04」",
    "what": "留出段的对比没有对齐半衰期:原式/提纯版用 hl=3(换手 6.1%),推荐者用 hl=0(换手 3.8%)。把半衰期按纯多头夏普来定之后,树内提纯版 f_min3 在留出段的多头腿不输甚至好于推荐的 f_max30。也就是说「换成已知家族成员让多头腿更好」只在样本内成立,样本外没有复现;留出段上 +3.6 个点的净超额里约六成是成本差,不是信号差。这组数字就在 final.json 里(splits_at_hl_long),notes 没有提。",
    "evidence": "runs/F105_std_fangzheng_covamt/final.json → results.*.books_user.splits_at_hl_long(同一次 final 运行算出来的,不是新的留出段读取):f_min3 @hl_long=10:utrain LS 3.03 / 多头腿净 13.4% / 纯多头夏普 2.28;holdout LS 2.52 / 毛 16.0% / 净 13.5% / 纯多头夏普 1.74 / 换手 3.4%。f_max30 @hl0:holdout LS 2.39 / 净 12.5% / 夏普 1.37;@hl_long=1:净 13.5% / 夏普 1.47 / LS 2.29。f_max60:14.7% / 1.74。即留出段上 f_min3@10 在多空、多头净超额、纯多头夏普三项上都 ≥ f_max30。成本拆分(holdout):原式 毛 14.3% → 净 8.9%(成本 5.4 点),f_max30 毛 15.7% → 净 12.5%(成本 3.2 点):毛差 +1.4,成本差 +2.2。样本内(audit_1.py 第 1 节,固定半衰期):min3@10 多头腿净 11.1% / 19.1%、orig@10 9.3% / 18.2%,max30@0 13.6% / 22.2% —— 样本内家族领先 2.5~4.3 / 3.1~4.0 个点,留出段领先消失(−1.0 点、夏普 −0.37)。",
    "fix": "在第 10 节加一张「按纯多头规则定半衰期」的留出段表(数字已在 final.json,不需要再读留出段);把结论改成:相对于「按多空规则定半衰期的原式」升华成立(+3.6 点,其中毛 +1.4);相对于「树内提纯 + 更慢的 EMA」没有样本外证据。把 cross_stddev(cross_stddev(day_cov(Amt,Amt),241),5) @ hl 10 列为并列候选(与原式 rank 相关 0.94,是真正的提纯;推荐者只有 0.64)。"
   },
   {
    "lens": "机制与过拟合",
    "severity": "major",
    "where": "notes/07_S3_family.md、07_S4_longleg.md(1)、09_diagnosis.md 已确立第 7 条;mechanism 里「所以族内更慢的窗口(15~60 天)净超额更高」",
    "what": "「d=15~60 是多头腿平台、d=9 不在平台上」是半衰期规则的伪影,不是窗口的性质:所有成员的半衰期都按多空夏普选成了 0。给 d=9 加一个 EMA(hl=5),它在 train 和 valid 上与推荐的 d=30 逐项相同。推荐者 = F001 已蒸馏出的 cross_max(day_std(Amt), 9) 加平滑,研究没有把「更慢的窗口」和「任意方式降换手」区分开。07_S1_what 里提过一句「hl=5 时 13.7%,但不是按规则选的」,到结论里消失了。",
    "evidence": "audit_1.py 第 1 节:known9@hl5 train 多头腿净 13.7% / 纯多头夏普 1.99 / 换手 4.2%,valid 22.2% / 3.59 / 3.9%;max30@hl0 train 13.6% / 2.03 / 4.0%,valid 22.2% / 3.69 / 3.5%;max15@hl3 13.9% / 22.1%。known9 在 hl=0 时才是 9.3% / 18.5%。max30 对 known9 回归后残差 rank IC 只有 0.0037(t 1.5,train)/ 0.0078(t 2.0,valid)。",
    "fix": "把已确立第 7 条改成「这一族任何成员只要把多空日换手压到 3%~5%(加长窗口或加 EMA 均可),多头腿净超额都在 12%~14% / 21%~22%」;verdict 明说推荐者等价于 F001 的 known9 加 hl≈5 的 EMA,对已有 F001 结果的因子池增量为零(不是「没有测」——longleg.py 第 1 节和本次审查已经测了)。"
   },
   {
    "lens": "机制与过拟合",
    "severity": "major",
    "where": "one_line「信息被已知家族完全包含」;09_diagnosis.md 已确立第 4 条;07x_events.md 第 6 节「原式与已知家族不重合的那一半不是 alpha,是噪声」",
    "what": "「完全包含」只对多空价差(空头腿)成立。残差的无成本多空夏普 ≈ 0 是因为残差的多头侧为正、空头侧为负互相抵消,不是因为残差没有信息:残差 rank IC 显著为正,残差多头腿毛超额在验证段有 +9.5%~+10.6%。对只能做多的用户,被判成「噪声」的那一半恰好有多头侧信息。研究只在 train 上做了这组回归,而且只读了多空夏普。",
    "evidence": "audit_1.py 第 4 节(秩空间逐日回归,实际交易的信号):train orig|known9 残差 rank IC +0.0090(t 4.3)、多头毛 +1.1%、空头 −5.1%;orig|max30 +0.0157(t 8.9)、多头 +4.3%、空头 −4.1%;min3|max30 +0.0171(t 10.0)、多头 +6.1%。valid orig|known9 +0.0135(t 4.5)、LSgross −0.02、多头 +9.5%、空头 −9.6%;orig|max30 +0.0209(t 6.5)、多头 +10.6%、空头 −7.6%;min3|max30 +0.0223(t 7.0)、多头 +12.2%。残差 rank IC 相当于原式的 24%~42%。旁证:留出段 f_min3 多空 2.72 ≥ f_max15 2.70 > f_max30 2.39。",
    "fix": "措辞降级为「空头腿与多空价差被已知家族包含;多头侧不被包含(残差 rank IC t>4,残差多头腿毛超额 +4% / +10%)」。补一个直接实验:原式(或 min3)与 max30 的秩平均,看多头腿净超额是否高于 max30 单独;残差的多头侧扣费后还剩多少。"
   },
   {
    "lens": "机制与过拟合",
    "severity": "major",
    "where": "mechanism「方向无信息」;09_diagnosis.md 已确立第 3 条、H2/H3/H3′ 的判决;07_S1_what.md 第 2 点",
    "what": "「方向无信息」是错的,而且与研究自己的「回声是稀释」证据相矛盾。它的依据 s1_signed 是原始金额单位的带符号差分:成交额² 的尺度把大成交额股票同时推到两端,多头腿为负是水平效应,不是方向没信息。去掉尺度、在同一个 |D/C| 档位里比,C 上升(进入)是很深的空头信号,C 下降(回声)的超额是小幅为正 —— 事件这一半的信息全部在方向里。",
    "evidence": "audit_1.py 第 3 节(成熟股票,无尺度的 D/C):|D/C| 最高十分位里 C 上升 −46.7% / −61.3%(train / valid,年化超额),C 下降 +5.2% / +2.7%;第 9 十分位 −11.0% / −23.2% 对 +7.0% / +1.8%。D/C 的 rank IC 在 C 上升的股票里 −0.0405 / −0.0624,在 C 下降的股票里 −0.0135 / −0.0196。带符号相对变化的剖面 Q1 −30.8% / −38.8%,Q10 +2.8% / +1.2%(不单调:回声端是中性,不是利好)。",
    "fix": "机制改成「方向有信息:只有进入事件是空头信号,滑出(回声)在去掉尺度后是中性;原式用不分方向的 std 把两者混在一起」。H3(回声是稀释)可以从「未坐实」升为已确立;H3′「滑出组超额仍为负」应归因于水平(滑出组成交额分位 0.66),不是事件。"
   },
   {
    "lens": "机制与过拟合",
    "severity": "major",
    "where": "mechanism「事件那一半是只在大成交额股票里起作用的空头信号」;07_conditional.md 第 3 点;07_S1b_events.md;12_next.md 第 4 条「其余九档几乎是平的」",
    "what": "两处站不住。(1) 分桶变量是内生的:用当天成交额 ctl_amt 和 9 日峰值 known_stdamt_max9 分桶,而进入事件本身就是近期放量,会机械地把股票送进最高一桶;低桶里的「事件」基本只剩回声和噪声。所以桶内 IC 从 −0.007 到 −0.044 不能说明「事件只对大成交额股票有效」。用不被事件污染的一年水平 C 分桶时 IC 是平的,研究却用内生分桶推翻了它。(2)「只有 Q1 深、其余近乎平、没有多头腿」只是训练段、且被 2018 样本头一年和次新股污染的读法。",
    "evidence": "audit_1.py 第 3 节:同一个 |D/C| 最高十分位里,C 上升的股票成交额分位 0.76,C 下降的 0.42。S2S3 digest:s1_relchg|g_level 条件 IC −0.0167、−0.0241、−0.0279、−0.0321、−0.0270。s1_relchg 验证段剖面 Q1 −19.3%,Q8..Q10 +6.9% / +11.3% / +19.2%。只留成熟股票、hl=5 的 D/C:多头腿毛 11.8% / 20.2%、净 7.7% / 16.2%、纯多头夏普 1.61 / 2.88;同口径原式 7.0% / 22.0%、1.14 / 4.07 —— 训练段事件这一半的多头腿不比原式差。",
    "fix": "用事件之前的水平来分桶重做条件 IC(例如滞后 10 天的 60 日成交额中位数,或 ctl_cap);把「只在大成交额股票里起作用」「升华只能在水平这一半里找」降级为未坐实;剖面的描述补上验证段。"
   }
  ]
  
  ## 原研究的结论
  
  {
   "factor_id": "F105_std_fangzheng_covamt",
   "one_line": "原式是「成交额水平 × 近期放量事件」的一个绕远路、带三个伪影的写法,信息被已知家族 cross_max(day_std(Amt), d) 完全包含;换成 d=30 的成员后多头腿净超额在用户训练/测试段从 11.8%/8.9% 升到 16.1%/12.5%,多空夏普打平。",
   "mechanism": "根节点 ts_stddev(C,5) 读的是一年硬窗口水平量 C(≈一年里日内成交额方差的最大值)最近 5 天的变化量(与 |ΔC| 的 rank 相关 0.994),截面排序 = 水平 × 相对变化,两半几乎不相关(0.019)。水平那一半 100% 是成交额水平(对 ctl_amt 中性化后残差 rank IC −0.0007);事件那一半是只在大成交额股票里起作用的空头信号(分位剖面只有 Q1 深,按已知家族分桶 IC 从 −0.007 到 −0.044),方向无信息。硬窗口 + 不分方向的 std 带来周年回声,nan-aware 扩张窗口带来次新股机械放大,ts_std 对单个观测给 0 带来上市首日伪影。空头腿的钱是「高换手率的大成交额股票刚放过量」,多头腿的钱是「小市值里成交清淡、近一两个月没放过量」的股票;多头腿要的信息变化慢,所以族内更慢的窗口(15~60 天)净超额更高。",
   "family": "成交额水平 + 近期放量的极值记忆,与 F001 蒸馏出的 cross_max(day_std(Amt), 9) 同族(原式对它回归后残差无成本多空夏普 −0.55,反向 +2.34);不是新家族。",
   "original": {
    "expr": "ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5)",
    "sign": -1,
    "halflife": 3,
    "ls_train": 3.03,
    "ls_test": 2.24,
    "long_gross_train": 0.168,
    "long_gross_test": 0.143,
    "long_net_train": 0.118,
    "long_net_test": 0.089,
    "long_sharpe_train": 1.96,
    "long_sharpe_test": 1.04,
    "turnover": 0.061,
    "coverage": 0.999,
    "distinct": 0.999,
    "n_operators": 4,
    "rank_corr_with_original": 1
   },
   "recommended": {
    "expr": "cross_max(day_std(Amt), 30)",
    "sign": -1,
    "halflife": 0,
    "ls_train": 2.8,
    "ls_test": 2.39,
    "long_gross_train": 0.196,
    "long_gross_test": 0.157,
    "long_net_train": 0.161,
    "long_net_test": 0.125,
    "long_sharpe_train": 2.46,
    "long_sharpe_test": 1.37,
    "turnover": 0.038,
    "coverage": 0.999,
    "distinct": 1,
    "n_operators": 2,
    "rank_corr_with_original": 0.643
   },
   "recommended_kind": "elevated",
   "other_finalists": [
    {
     "expr": "cross_stddev(cross_stddev(day_cov(Amt, Amt), 241), 5)",
     "sign": -1,
     "halflife": 3,
     "ls_train": 3.3,
     "ls_test": 2.72,
     "long_gross_train": 0.175,
     "long_gross_test": 0.163,
     "long_net_train": 0.13,
     "long_net_test": 0.115,
     "long_sharpe_train": 2.18,
     "long_sharpe_test": 1.33,
     "turnover": 0.061,
     "coverage": 0.999,
     "distinct": 0.999,
     "n_operators": 3,
     "rank_corr_with_original": 0.937
    },
    {
     "expr": "cross_max(day_std(Amt), 15)",
     "sign": -1,
     "halflife": 0,
     "ls_train": 3.08,
     "ls_test": 2.7,
     "long_gross_train": 0.203,
     "long_gross_test": 0.17,
     "long_net_train": 0.149,
     "long_net_test": 0.12,
     "long_sharpe_train": 2.26,
     "long_sharpe_test": 1.28,
     "turnover": 0.06,
     "coverage": 0.999,
     "distinct": 1,
     "n_operators": 2,
     "rank_corr_with_original": 0.665
    },
    {
     "expr": "cross_max(day_std(Amt), 60)",
     "sign": -1,
     "halflife": 0,
     "ls_train": 2.52,
     "ls_test": 2.39,
     "long_gross_train": 0.177,
     "long_gross_test": 0.166,
     "long_net_train": 0.155,
     "long_net_test": 0.147,
     "long_sharpe_train": 2.34,
     "long_sharpe_test": 1.74,
     "turnover": 0.024,
     "coverage": 0.999,
     "distinct": 1,
     "n_operators": 2,
     "rank_corr_with_original": 0.627
    }
   ],
   "known_exposure_r2": 0.5,
   "verdict": "升华成立但幅度有限,且不是新因子。读留出段之前定下的推荐 cross_max(day_std(Amt), 30) 在用户测试段上多头腿净超额 +12.5% 对原式 +8.9%、纯多头夏普 1.37 对 1.04、多空夏普 2.39 对 2.24(在 ±0.3 噪声内,算打平)、换手 3.8% 对 6.1%;逐年看 8 年里 7 年多头腿净超额高于原式 3.4~5.9 个点。四个候选在测试段的多空夏普、多头腿毛/净超额、纯多头夏普上全部不低于原式,说明原式只是这个家族里一个更吵的成员。需要如实说明的三点:(1) 它就是 F001 已蒸馏出的成交额水平家族换了更慢的窗口(与 d=9 的 rank 相关 0.85、与 log 成交额 0.80,全部控制变量张成 R² 0.740),对因子池的边际贡献没有测;(2) 留出段上多头腿最好的是慢端的 d=60(净超额 14.7%、纯多头夏普 1.74),不是事先选的 d=30,推荐没有因此改动,只能说 d=30~60 都合理;(3) 整个家族在测试段弱了一截(纯多头夏普从 2.0~2.5 掉到 1.0~1.7,2024 年最差),多头腿的钱集中在小市值里(只留市值大的一半时训练段多头腿净超额只剩 1.8%)。如果要留在原式结构里,用 3 算子的提纯版 cross_stddev(cross_stddev(day_cov(Amt, Amt), 241), 5)(测试段多空 2.72、多头腿净超额 11.5%)。",
   "established": [
    "原式 = 水平 × 事件:D 与 |C 的 5 日变化| rank 相关 0.994,与水平 C、相对变化 D/C 各 0.67,两半之间 0.019(studies/events.py 第 2 节);水平那一半对 ctl_amt 中性化后残差 rank IC −0.0007(S1 中性化表)",
    "事件那一半是只在大成交额股票里起作用的空头信号,方向无信息:s1_relchg 训练段 Q1 −28.7% 其余九档近乎平、多头腿净超额 4.6%;按已知家族分五桶桶内 IC −0.007→−0.044;带符号的 s1_signed 多头腿毛超额 −6.8%/−11.9%;写干净的 s4_pos 多头腿净超额同样只有 4.6%/12.8%(S1、S1b、S4、条件 IC 表)",
    "原式被已知家族包含:对 cross_max(day_std(Amt),9) 回归后残差 rank IC 0.0090、无成本多空夏普 −0.55,反向还剩 0.0322/+2.34;对 d=30 成员回归后 +0.02,反向 +1.56;删掉一年窗口(s1_recent)与已知家族 rank 相关 0.94 且 rank IC 更高(events.py 第 6 节、longleg.py 第 1 节、S1b)",
    "cross_max(·,3) 与 fangzheng 里 mean/std 的区分都多余:s2_no_max3 rank 相关 0.967、s2_mid_mean 0.983、s2_mid_std 0.965,3 算子的 s2_min3 在 train/valid 上多空 2.84/4.80 对原式 2.54/4.62,留出段 2.72 对 2.24(S2、S_final)",
    "三个伪影都量到:次新股占截面 7% 却占空头十分位 25%/17%;上市首日因子值为 0 每天把约 3 只次新股排进多头腿,拉低多头腿毛超额 2.3/1.9 个点(换成 |差分| 后训练段 +2.6 个点);空头十分位里回声驱动的股票日占 23%/48% 而超额只有 −5.1%/−13.2%,新事件驱动的是 −38.6%/−62.4%(events.py 第 3~5 节、S2 s2_absdelta)",
    "已知家族的多头腿净超额在 d=15~60 上是平台(训练 12.3%~13.6%、验证 20.4%~22.2%、留出 12.0%/12.5%/14.7%),多空夏普随 d 单调下降;多头腿需要「没放过量」而不只是「平时成交少」(60 日中位数的多头腿毛超额 7.0%/19.5% 对 60 日最大值 15.9%/22.3%);日内成交额离散度优于日成交额(S3、S4、S_final)"
   ],
   "unresolved": [
    "周年回声是不是纯稀释:分组和剔除实验支持,但替换实验 s1_noecho(线性衰减均值)没有变好、验证段更差;那个替换同时改变了背景漂移,不是干净对照,表达式语言里没有只去掉回声的写法",
    "多头腿在大市值里还有没有:只留流通市值大的一半时,训练段这一族多头腿净超额只剩 1.8%(原式 5.1%),验证段却有 18.6%,两段不一致;容量和冲击成本没有建模",
    "2024 年整个家族多头腿明显变弱(d=30 成员净超额 9.1%、纯多头夏普 0.80,留出段最大回撤 −15.1%),是小市值/低流动性溢价的结构性变化还是一次性冲击,分不出来",
    "相对因子池里已有的成交额水平结构,cross_max(day_std(Amt), 30) 的边际贡献没有测;对 d=9 成员回归后残差 rank IC 只有 0.0037,很可能只是「把已有成员的窗口放慢」",
    "平台内部的最优窗口不稳定:样本内 d=30 最好,留出段 d=60 最好;长窗口上 max 与 mean 对多头腿孰优也没有定论(d=20、60 两处都是训练段 max 好、验证段 mean 好)",
    "d=30 成员的多头十分位在验证段有 7.7% 是上市不满 247 天的次新股(原式只有 0.7%,被未满窗口放大挡在外面),这些股票对多头腿业绩的贡献没有单独量过"
   ],
   "lab_findings": [
    {
     "id": "short-std-on-long-hard-window-is-event-detector-with-anniversary-echo",
     "claim": "短窗滚动 std(或 |差分|)套在长硬窗口水平统计量外面,读到的是该水平量的近期变化量(事件探测器),不分升降;硬窗口让每个尖峰在 d 天后滑出时产生一个与进入时等幅的回声,因子值上无法与新事件区分",
     "evidence": "探针 chain_impulse_profile:脉冲后第 0~5 天和第 241~246 天各响一次,echo_over_entry=1.0,对数正态噪声背景下 10.5 倍对 10.9 倍;真实数据里 ts_stddev(C,5) 与 |C_t−C_{t−4}| 的 rank 相关 0.994;空头十分位里回声驱动的股票日占 23%/48%,超额 −5.1%/−13.2%,新事件驱动的是 −38.6%/−62.4%",
     "operators": [
      "ts_stddev",
      "ts_std",
      "cross_stddev",
      "cross_delta",
      "cross_fangzheng",
      "cross_mean",
      "cross_max"
     ],
     "confidence": "high",
     "recheck": "中间层换成 cross_decay_linear 时回声只剩 0.015,但背景会变成与水平成正比的匀速漂移(不是干净的去回声);外层换成带符号的差分时进入与滑出反号,方向本身在本例里没有信息(多头腿为负)"
    },
    {
     "id": "fangzheng-is-mean-plus-std-and-indistinguishable-under-differencing",
     "claim": "cross_fangzheng(x,d) = cross_mean(x,d) + cross_stddev(x,d);在重尾正值输入上它是极值统计量(跟窗口最大值走),但只要外层读的是它的变化量,mean 项、std 项、两者之和给出的截面排序几乎相同,区分它们没有意义",
     "evidence": "源码一行;探针 tail_dominance(对数正态 σ=1.5 时与窗口最大值秩相关 0.91、与中位数 0.18);真实数据去尺度后 C 与一年最大值 rank 相关 0.984;外层套 5 日 std 后,只留 mean 项与原式 rank 相关 0.983、只留 std 项 0.965,指标都在噪声内",
     "operators": [
      "cross_fangzheng",
      "cross_mean",
      "cross_stddev"
     ],
     "confidence": "high",
     "recheck": "直接把 fangzheng 当水平量用(外层不取差分/std)时 mean 与 std 项不等价;输入不是重尾正值(log σ 明显小于 1)时它更接近均值而不是极值"
    },
    {
     "id": "low-rank-corr-is-not-a-different-factor-use-two-way-neutralisation",
     "claim": "与已知家族的 rank 相关远低于 0.95 不代表是不同因子:相关低可能只是因为掺了一半不挣钱的成分。判包含关系要做双向中性化,看残差的 rank IC 和无成本多空夏普",
     "evidence": "原式与 cross_max(day_std(Amt),9) 的 rank 相关只有 0.68(R² 0.49),但原式对它回归后残差 rank IC 0.0090、无成本多空夏普 −0.55,反向残差 0.0322/+2.34;控制变量张成原式 R² 0.500 而张成更好用的 d=30 成员 0.740 ——「更独特」的那一半是噪声",
     "operators": [],
     "confidence": "high",
     "recheck": "残差没有再平滑,只能读 rank IC 与无成本夏普;被比较的两个信号半衰期差别很大时,R² 会被平滑程度左右,要在各自实际交易的信号上做"
    },
    {
     "id": "nan-aware-rolling-ops-inflate-young-stocks-and-zero-on-first-obs",
     "claim": "nan-aware 的滚动算子在窗口未满时用逐日变长的扩张窗口,次新股(以及没有预热行的样本头一年)的任何「变化量」型统计被机械放大;滚动 std 对单个观测给 0,上市首日会得到全截面最小值",
     "evidence": "次新股占截面 7%,却占原式空头十分位的 25%/17%;上市首日因子值为 0 每天把约 3 只次新股排进多头腿,组内年化超额 −360%/−290%,拉低多头腿毛超额 2.3/1.9 个点;把外层 std 换成 abs_(cross_delta(·,5))(首日为 NaN)后训练段多头腿毛超额 +2.6 个点",
     "operators": [
      "ts_stddev",
      "ts_std",
      "cross_stddev",
      "cross_mean",
      "cross_fangzheng"
     ],
     "confidence": "high",
     "recheck": "视图有足够预热行、或截面按上市天数过滤时不成立;水平型因子(如 cross_max(day_std(Amt), d))没有这个放大,反而会让成交清淡的次新股进入最小端"
    },
    {
     "id": "amt-level-family-long-leg-plateau-at-slower-windows",
     "claim": "成交额水平家族 cross_max(day_std(Amt), d) 里,rank IC 与多空夏普随 d 单调下降(近期放量信息值钱的地方在空头腿),而多头腿净超额在 d=15~60 上是平台、明显高于 d=9 与 d=241;对纯多头用户该用比多空最优更慢的窗口",
     "evidence": "d=9/15/20/30/60/120/241 的多头腿净超额训练段 9.3/12.3/12.6/13.6/13.5/11.6/9.0%、验证段 18.5/21.3/20.9/22.2/20.4/19.9/18.6%;留出段 d=15/30/60 为 12.0/12.5/14.7%;族内嵌套:d=30 对 d=9 回归后残差 rank IC 0.0037,反向 0.0283 但换手 15.4%",
     "operators": [
      "cross_max",
      "day_std"
     ],
     "confidence": "medium",
     "recheck": "只在 15bp 单边成本口径下成立,成本更低时短窗口重新占优;多头腿的钱集中在小市值(只留市值大的一半时训练段净超额 1.8%);2024 年明显变弱"
    },
    {
     "id": "amt-family-short-leg-is-turnover-long-leg-is-small-cap-side",
     "claim": "成交额家族的两条腿跟着成交额的两个不同成分走:对换手率中性化后空头腿毛超额掉到三分之一左右或更低、多头腿变大;对流通市值中性化后已知家族成员的多头腿掉一半、空头腿变大。多头腿还需要「近期没放过量」:只看平时成交水平(中位数)多头腿只剩一半",
     "evidence": "原式/d=9/d=30/d=60 四个因子同一形状(训练段,多头/空头毛超额):d=30 未中性化 17.4%/27.0%,对 ctl_cap 8.4%/41.6%,对 ctl_turnrate 23.3%/7.6%;cross_med(day_std(Amt),60) 多头腿毛超额 7.0%/19.5% 对 cross_max 同窗口 15.9%/22.3%;换手率、波动类控制变量自己当因子在训练段多头腿毛超额为负",
     "operators": [
      "cross_max",
      "cross_med",
      "day_std",
      "day_sum"
     ],
     "confidence": "medium",
     "recheck": "中性化只在训练段(2018–2021)做过;残差未平滑只读毛超额;市值和换手率是外部面板,换数据源要重查"
    },
    {
     "id": "scale-free-volume-event-is-short-only-and-gated-by-amount",
     "claim": "无尺度的「相对自身历史放量」信号(近期峰值/一年峰值,或一年水平量的相对变化)是纯空头信号:只有最高一档深度跑输,其余九档近乎平,多头腿净超额很低;而且它的 IC 集中在成交额最大的那一桶",
     "evidence": "div(cross_max(day_std(Amt),5), cross_max(day_std(Amt),241)) 训练/验证 Q1 −35.0%/−39.7%,Q2 只有 −3.3%,多头腿净超额 4.6%/12.8%;D/C 版本 Q1 −28.7%、多头腿净超额 4.6%/14.7%;按 ctl_amt 分五桶桶内 IC −0.010→−0.041,按已知家族分桶 −0.007→−0.044",
     "operators": [
      "div",
      "cross_max",
      "day_std"
     ],
     "confidence": "medium",
     "recheck": "作为多头组合的排除条件(剔掉最高一档)是否有用没有测;与 20 日动量 rank 相关 0.37,对动量中性化后无成本多空夏普从 3.28 掉到 1.59"
    },
    {
     "id": "dt-face-rewrite-of-nd-rolling-ops-is-bit-identical",
     "claim": "nd 面的 ts_stddev / ts_delta 与 dt 面的 cross_stddev / cross_delta 是同一内核,作用在「每股票-日一个值」的面板上结果逐位相同;nd 面不分块求值,显卡被邻居占满时会 OOM,改写成 dt 面即可",
     "evidence": "ts_stddev(C,5) 与 cross_stddev(C,5) rank 相关 1.000、全部指标逐位相同(s2_dtface_check);abs_(ts_delta(C,5)) 与 abs_(cross_delta(C,5)) 在两次独立运行里指标逐位相同;S1 第一次运行 3 个含新 ts_stddev 的表达式在只剩约 0.3 GiB 空闲显存时 OOM",
     "operators": [
      "ts_stddev",
      "ts_std",
      "cross_stddev",
      "ts_delta",
      "cross_delta"
     ],
     "confidence": "high",
     "recheck": "只在 AlphaCube commit 1698296 上核对过;两个面的窗口池不同(ts_* 是 1/5/10/20/…,cross_* 是 3/5/10/15/30/60/241),进搜索语法时要注意"
    }
   ],
   "holdout_reads": 1,
   "server_runs": 8,
   "variants_tested": 28,
   "report_path": "/Users/wxy/Desktop/Partura/research/alpha_distillation/F105_std_fangzheng_covamt.md",
   "tooling_problems": [
    "重复了一次服务器运行(我的失误 + 工具缺口):中断前的研究员已经用 tag S1b_S2_S3 把 S1 的 3 个 OOM 变体和 S2、S3 一起跑完(21 个变体),但 JSON 和台账只留在服务器上没拉回本地;study.sh status 只列正在跑的任务,没有命令能列服务器上已完成的结果。我用 wait 探了几个猜的 tag 没猜中,于是把同样的阶段又跑了一遍(S2S3_nodes_family)。后来 wait 完成时 rsync 把旧文件一起拉回才发现;两次运行的指标逐位相同,结论不受影响,但全研究因此用满了 8 次(S0_baseline、S1_what、x1_events、S1b_S2_S3、S2S3_nodes_family、S4_longleg、x2_longleg、final)。建议加一个 study.sh pull <fid>;接手时可先对任何已完成的 tag 调一次 wait 来触发 rsync",
    "nd 面的 ts_stddev 在 GPU 上不分块,邻居把显卡占满时 OOM(S1 第一次运行挂了 3 个变体)。绕过:外层 std 改写成 dt 面的 cross_stddev(同一内核),用 s2_dtface_check 证明与原式逐位相同;ts_delta 同理换成 cross_delta",
    "台账里 S0_baseline 被记了 3 次(骨架生成阶段重跑过),所以 train/valid 的读取次数是 8 而不是研究里实际的阶段数;server_runs 里 S0 只算了一次",
    "内置探针的样本只有 40 行,对 241 日窗口是瞎的(cross_fangzheng 的「脉冲记忆天数 = 27」只是 40−13)。绕过:studies 下的四个探针都用 ≥3 倍窗口的样本,并带解析解自检",
    "条件 IC 的 gate 只能是控制变量/gates 或同一次运行里的变体,跨运行的变体会被静默跳过。绕过:在 gates 里加了一个 g_level(与 s1_level 同一表达式,走缓存)",
    "rank 相关矩阵只覆盖同一次运行里的面板,报告第 8 节在没设 corr_ids 时只印控制变量之间的矩阵。绕过:把 corr_ids 设成五个最终候选;其余变体与原式/已知家族的相关用临时脚本从各次运行的 JSON 里读出来写进 notes",
    "study.sh digest 不打印纯多头夏普、hl_long 口径、与原式的 rank 相关(非基线阶段),报告的逐年表也只印基线 id。这些数字都在 JSON 里,我用临时 python 读出来,并在 notes 里注明了出处(例如 final.json 的 diagnostics.by_year)",
    "report 合并多次运行时按文件名字典序「后者覆盖前者」,诊断表按 key 合并:旧运行 S1b_S2_S3 里的两行条件 IC(s1_relchg|s1_level、s1_level|s1_relchg)因此留在了报告的条件 IC 表里,已在 07_conditional 里说明",
    "分析脚本里按「当天成交额分位」过滤截面会让贴着边界的多头十分位每天进出截面,日换手被抬到 13%~19%,净值不可读;那一组只读了毛超额,并在 notes 里写明"
   ]
  }
  
  ## 规矩
  
  - **绝对不许再读留出段**(不许用 study.sh final,不许新建带 final 的阶段)。留出段的数字已经是定论;
    如果审查指出留出段流程本身有违规(比如读了两次),无法撤销,就在 notes/F105_std_fangzheng_covamt/10_distilled.md 开头如实写明。
  - 每条意见要么**改正**(改 notes 里的数字/措辞;把证据不足的「已确立」降级为「合理但未坐实」或「未决」;
    必要时补实验),要么**有理有据地反驳**(审查错了的话,在你的输出里写明为什么)。不要为了通过审查而删掉不利的事实。
  - 可以补实验,但只用 train/valid:最多再跑 2 次服务器运行(新阶段 id 用 SR_ 开头,tag 用 rev1、rev2)。
    如果审查员已经加了 SA_audit 阶段并跑过(runs/F105_std_fangzheng_covamt/audit1.json),它的结果也是证据,写进 notes
    (建一个 notes/F105_std_fangzheng_covamt/07_SA_audit.md)。
  - 如果补的实验改变了「哪个候选最好」的判断:留出段上读过的候选不能换。你可以在 10_distilled.md 里写
    「按修订后的 train/valid 证据,X 更值得推荐,但它没有读过留出段」,recommended 仍然只能从读过留出段的候选里选。
  - 改完后 ./scripts/study.sh report F105_std_fangzheng_covamt,通读报告。
  
  ## 你的最终输出
  
  与原研究同样的结构(修订后的版本)。在 tooling_problems 里另外列出:你对每条审查意见的处理(「已改」/「已补实验」/「反驳:理由」)。
```
