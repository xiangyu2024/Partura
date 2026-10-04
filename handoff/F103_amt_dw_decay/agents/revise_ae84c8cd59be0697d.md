# revise:F103_amt_dw_decay — agent ae84c8cd59be0697d(工作流 wf_759ef2d3-03f)

- 状态:**已返回结果**;开始 10-04 00:01,最后一次动作 10-04 00:29;工具调用 83 次
- 这是从 agent 的对话记录里**自动抽出来的动作流水**(命令、输出、写了哪些文件)。agent 的推理不在记录里 ——
  它的判断要看 `notes/F103_amt_dw_decay/journal.md` 和各 notes 文件。输出过长的地方截了中间。

## 动作流水

**10-04 00:01 · Bash** — List Partura project files and doc sizes

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

10-04 00:01 · 读 `/Users/wxy/Desktop/Partura/CLAUDE.md`

10-04 00:01 · 读 `/Users/wxy/Desktop/Partura/docs/method.md`

10-04 00:01 · 读 `/Users/wxy/Desktop/Partura/docs/study_playbook.md`

**10-04 00:01 · Bash** — List F103 study files with timestamps

```bash
cd /Users/wxy/Desktop/Partura && ls -la notes/F103_amt_dw_decay/ runs/F103_amt_dw_decay/ studies/F103_amt_dw_decay/ logs/ | head -100 && wc -l research/alpha_distillation/F103_amt_dw_decay.md configs/F103_amt_dw_decay.yaml notes/F103_amt_dw_decay/*.md
```

```
logs/:
total 904
drwxr-xr-x@ 43 wxy  staff   1376 Oct  3 23:59 .
drwxr-xr-x@ 21 wxy  staff    672 Oct  3 16:41 ..
-rw-r--r--@  1 wxy  staff   1603 Oct  3 19:41 F101_day_shine_retstd_S1_parts.log
-rw-r--r--@  1 wxy  staff   1311 Oct  3 20:01 F101_day_shine_retstd_S2_background.log
-rw-r--r--@  1 wxy  staff  19380 Oct  3 23:21 F101_day_shine_retstd_audit1.log
-rw-r--r--@  1 wxy  staff   1151 Oct  3 23:00 F101_day_shine_retstd_final.log
-rw-r--r--@  1 wxy  staff   8282 Oct  3 19:28 F101_day_shine_retstd_look.log
-rw-r--r--@  1 wxy  staff   5427 Oct  3 19:50 F101_day_shine_retstd_look2.log
-rw-r--r--@  1 wxy  staff  17727 Oct  3 22:45 F101_day_shine_retstd_look3.log
-rw-r--r--@  1 wxy  staff   1468 Oct  3 23:36 F101_day_shine_retstd_rev1.log
-rw-r--r--@  1 wxy  staff  34616 Oct  3 23:41 F101_day_shine_retstd_rev2.log
-rw-r--r--@  1 wxy  staff   8723 Oct  3 23:33 F102_kurt_autocorr_audit1.log
-rw-r--r--@  1 wxy  staff   1176 Oct  3 23:15 F102_kurt_autocorr_final.log
-rw-r--r--@  1 wxy  staff   1648 Oct  3 23:54 F102_kurt_autocorr_rev1.log
-rw-r--r--@  1 wxy  staff   2081 Oct  3 19:50 F102_kurt_autocorr_s12.log
-rw-r--r--@  1 wxy  staff   1920 Oct  3 22:53 F102_kurt_autocorr_s3.log
-rw-r--r--@  1 wxy  staff  17421 Oct  3 19:32 F102_kurt_autocorr_x1.log
-rw-r--r--@  1 wxy  staff  11796 Oct  3 20:05 F102_kurt_autocorr_x2.log
-rw-r--r--@  1 wxy  staff  12620 Oct  3 23:04 F102_kurt_autocorr_x3.log
-rw-r--r--@  1 wxy  staff   1946 Oct  3 19:34 F103_amt_dw_decay_S1_structure.log
-rw-r--r--@  1 wxy  staff   1650 Oct  3 23:19 F103_amt_dw_decay_S2_distil.log
-rw-r--r--@  1 wxy  staff  19904 Oct  3 23:54 F103_amt_dw_decay_audit1.log
-rw-r--r--@  1 wxy  staff   1101 Oct  3 23:26 F103_amt_dw_decay_final.log
-rw-r--r--@  1 wxy  staff  11410 Oct  3 19:40 F103_amt_dw_decay_x1.log
-rw-r--r--@  1 wxy  staff  10100 Oct  3 19:56 F103_amt_dw_decay_x2.log
-rw-r--r--@  1 wxy  staff  21684 Oct  3 23:04 F103_amt_dw_decay_x3.log
-rw-r--r--@  1 wxy  staff   1750 Oct  3 19:44 F104_kurt_masktop_amt_S1_mask.log
-rw-r--r--@  1 wxy  staff   1806 Oct  3 19:57 F104_kurt_masktop_amt_S2_resid.log
… (64 行略) …
      22 notes/F103_amt_dw_decay/02_operators.md
      19 notes/F103_amt_dw_decay/03_decomposition.md
      17 notes/F103_amt_dw_decay/04_grammar.md
      38 notes/F103_amt_dw_decay/05_hypotheses.md
      31 notes/F103_amt_dw_decay/06_baseline.md
      41 notes/F103_amt_dw_decay/07_S1_structure.md
      42 notes/F103_amt_dw_decay/07_S2_distil.md
      18 notes/F103_amt_dw_decay/07_S_final.md
       8 notes/F103_amt_dw_decay/07_conditional.md
       6 notes/F103_amt_dw_decay/07_controls.md
      15 notes/F103_amt_dw_decay/07_neutralise.md
      60 notes/F103_amt_dw_decay/07x_x1_anatomy.md
      91 notes/F103_amt_dw_decay/07x_x2_interaction.md
     143 notes/F103_amt_dw_decay/07x_x3_family.md
      13 notes/F103_amt_dw_decay/08_variants.md
      66 notes/F103_amt_dw_decay/09_diagnosis.md
      87 notes/F103_amt_dw_decay/10_distilled.md
      17 notes/F103_amt_dw_decay/11_risks.md
      10 notes/F103_amt_dw_decay/12_next.md
    2216 total
```

**10-04 00:01 · Bash** — Read F103 notes 01 through 06

```bash
cd /Users/wxy/Desktop/Partura && for f in 01_expression 02_operators 03_decomposition 04_grammar 05_hypotheses 06_baseline; do echo "=================== $f"; cat -n notes/F103_amt_dw_decay/$f.md; done
```

```
=================== 01_expression
     1	**来历**:挖掘库 #820(GP 搜出来的)。用户表里公布的那一行:方向 −、半衰期 2,扣费多空夏普 训练 +3.53 / 测试 +3.18,多头腿年化毛超额 +12.8% / +12.4%。
     2	Partura 自己求值复现了这一行(S0 复现训练段,S_final 复现测试段)。
     3	
     4	**一句话**:它把「当天收盘集合竞价的成交额」乘上「这只股票最近 30 天**平均**日内成交额曲线的粗糙度」的三次方,再取 5 日最大值;
     5	方向为负 —— **成交活跃、而且成交长期挤在少数几分钟里的股票,之后跑输**。
     6	
     7	读完源码、做完拆解之后的版本(证据见第 7~10 节):
     8	
     9	- 七个算子里有三个是多余的:`ts_min(·,1)` 是恒等,`cross_max(·,5)` 只是低通,`day_close(Amt)`(收盘竞价那一根)换成全天成交额反而更好。
    10	  只删这三处(5 个算子),留出段多空夏普 +3.52(原式 +3.18),多头腿净超额 +9.2%(原式 +5.5%)。
    11	- 剩下的骨架是 **成交额水平 × (30 日平均曲线的集中度)^k**。成交额水平是已知家族(F001);集中度这一支是这棵树带来的东西,
    12	  它**只在成交活跃的票里、主要在空头端**有稳定的预测力。两条腿在时间上轮动:2018–2020 和 2024–2025 集中度强,2021–2023 成交额水平强。
    13	- 原式的指数 3 让集中度占了八成权重:多空夏普不差,但多头腿弱(净超额 +5.6% / +5.5%)。把指数降到 2(两条腿各占一半)之后,
    14	  多头腿净超额 +12.3% / +12.6%、纯多头夏普 +2.18 / +2.07,多空夏普 +3.45 / +3.10 —— 这是最终推荐的版本。多头腿多出来的部分来自成交额水平那条腿和更低的换手,不来自集中度。
=================== 02_operators
     1	七个算子的内核源码逐个读过(`study.sh src`),和名字不一样、或者探针表里看不出来的地方:
     2	
     3	- **`cross_decay_linear(Amt, 30)` 不是截面运算,也不是把一天压成一个数**。`Amt` 是 (天, 股票, 241 分钟) 的立方体,
     4	  `cross_*` 沿**交易日轴**滚:对每只股票的**每一个分钟槽位**,取最近 30 个交易日同一分钟的成交额做线性衰减加权平均
     5	  (权重 1…30,当天最重;缺失的天从分母里剔掉,所以前 29 天也有值)。输出仍然是一条 241 点的日内曲线 ——
     6	  **这只股票最近 30 天的"平均日内成交额曲线"**。权重的有效样本数是 (Σw)²/Σw² = 465²/9455 ≈ 22.9 天。
     7	- **`day_durbin_watson` 在这里既不是自相关检验,也不是 F001 里的"已实现方差"**。源码是
     8	  `Σ_m (x_m − x_{m−1})² / (Σ_m x_m² + 1e−8)`,分母是 Σx² 不是方差(探针:齐次度 0、平移不变 = False)。
     9	  F001 喂的是价格水平,所以 ≈ 分钟收益的方差;这里喂的是**一条非负的成交额曲线**,它量的是这条曲线的
    10	  **粗糙度/尖峰度**:曲线越平滑(相邻分钟差不多)越接近 0,孤立尖峰越多越接近 2。
    11	  对一条"水平 b 上叠加独立噪声"的曲线,DW ≈ 2·CV²/(1+CV²);对一个孤立在末端的尖峰 s,它贡献 ≈ s²/Σx²。
    12	  实验室里那条"DW 作用在价格水平上 ≈ 已实现方差"的先验在这棵树上**不适用**(操作数换了)。
    13	- **`day_close(Amt)` 是"最后一个非 NaN 分钟"的成交额**(`day_last` 的别名),不是收盘价、也不是全天成交额。
    14	  在 241 网格上最后一根是 15:00,A 股的收盘集合竞价(14:57–15:00)撮合量记在这一根上 ——
… (97 行略) …
    12	3. **多空夏普对半衰期不敏感,多头腿却明显喜欢慢的。** 半衰期扫描:多空夏普在 hl 2~10 上是 +4.14 / +4.12 / +4.13 / +4.09(平台),
    13	   而纯多头夏普从 hl 2 的 +1.30 一路升到 hl 10 的 **+1.86**(换手 8% → 4%)。按"多空夏普最大"的规则选中 hl 2 只赢了 0.01,
    14	   代价是多头腿多付一倍换手。**这是升华的第一条线索:多头端是慢变量。**
    15	4. **它是慢特征,不是事件信号。** rank IC 随预测期单调上升(h1 0.0393 → h5 0.0623 → h20 0.0802)。
    16	5. **逐年都为正,但在走弱。** 多空夏普 2018 +5.43、2019 +6.22、2020 +4.19、2021 +1.78、2022 +2.87、2023(到 8 月)+1.17;
    17	   多头腿毛超额 2019 +22.6%、2020 +19.6%,2021 只有 +3.7%、2023 +6.1%。valid 的 rank IC(0.0279)是 train(0.0393)的七成。
    18	6. **已知暴露张成的不多(R² 0.227),但被张成的那部分恰好是空头腿。** 对全部九个控制变量中性化后:
    19	   rank IC 0.0358 → 0.0172(掉 52%),无成本多空夏普 +5.36 → +2.83;**空头腿从 +42.8% 掉到 +9.1%,多头腿毛超额只从 +13.5% 掉到 +11.4%**。
    20	   也就是说空头腿的大部分是"高成交额 / 高波动 / 高动量的热门股之后下跌"这个已知效应,多头腿那 11% 不在这些控制变量里。
    21	   单个控制变量里拿走最多的是 `ctl_amt`(R² 0.081,残差 rank IC 0.0253)、`ctl_mom20`(0.073,0.0280)、`ctl_ivol`(0.064,0.0269);
    22	   `ctl_cap`、`ctl_price`、`ctl_rev1` 基本不动它(残差 rank IC 0.0356 / 0.0358 / 0.0357)。
    23	
    24	另外两条和"它是不是成交额水平家族"有关的事实:
    25	
    26	- 与已知家族的日截面 rank 相关只有 `known_stdamt_max9` 0.41、`known_ivol_max9` 0.33、`known_amt_max9` 0.31、`ctl_amt` 0.28 ——
    27	  远低于 0.95 的同族线,也低于一个齐次度 1 的成交额量应有的水平。
    28	- 但**同口径下成交额家族的多头腿比它好**:`known_stdamt_max9` 多头腿毛超额 +16.9% / +24.9%(train / valid)、多空夏普 +2.47 / +4.44;
    29	  原式是 +13.5% / +10.9%、+4.14 / +2.22。原式赢在 train 的多空夏普(靠空头腿),输在 valid 和多头腿。
    30	- 按 `ctl_amt` 五分桶的条件 rank IC 从 −0.0113 单调走到 **−0.0544**(差 4.8 倍):它几乎只在成交活跃的股票里有效;
    31	  按 `ctl_cap` 分桶则是小市值更强(−0.0493 → −0.0238)。
```

**10-04 00:01 · Bash** — Read F103 config and holdout ledger

```bash
cd /Users/wxy/Desktop/Partura && cat -n configs/F103_amt_dw_decay.yaml && cat runs/F103_amt_dw_decay/ledger.json
```

```
     1	# Partura study F103_amt_dw_decay  (挖掘 / #820)
     2	# 这份文件只有 S0_baseline 是生成的。后面的阶段、变体、额外控制变量、探针,都要按**这棵树**来写。
     3	factor_id: F103_amt_dw_decay
     4	title: "收盘集合竞价成交额 × (30 日平均日内成交曲线的粗糙度)³,套 5 日极值记忆"
     5	expression: "cross_max(mul(day_close(Amt), ts_min(pow_3(day_durbin_watson(cross_decay_linear(Amt, 30))), 1)), 5)"
     6	baseline_id: v_base
     7	probes: [studies/F103_amt_dw_decay/probes.py]   # 本研究新增的探针(每个都带已知答案的自检)
     8	
     9	# 用户表里公布的这一行(pick_single_factors 的口径);S0 要先把它复现出来
    10	published: {sign: -1, hl: 2, ls: [3.53, 3.18], long: [0.128, 0.124], lib: "挖掘", name: "#820"}
    11	
    12	label: {kind: open_vwap15, horizon: 1, buyable: true,
    13	        verify_against: /root/autodl-tmp/AlphaCube/_bench/trainto/allfac_buyable/_target.npy}
    14	cost_per_side: 0.0015
    15	top_frac: 0.10
    16	rank_by: ls
    17	horizons: [1, 2, 3, 5, 10, 20]
    18	warmup: 60
    19	
    20	# train + valid = 用户的训练段(utrain);holdout = 用户的测试段,只在最后读一次
    21	splits:
    22	  train:   ["20180102", "20211231"]
    23	  valid:   ["20220101", "20230807"]
    24	  utrain:  ["20180102", "20230807"]
    25	  holdout: ["20230808", "20251231"]
    26	  full:    ["20180102", "20251231"]
    27	fit_split: train
    28	user_split: utrain
    29	
    30	# ---- 这一批共用的控制变量(都是日频、因果、只用到 t 日收盘)。按这棵树的嫌疑增删。
… (269 行略) …
      "expressions": 32
    },
    "valid": {
      "reads": 7,
      "expressions": 32
    },
    "utrain": {
      "reads": 7,
      "expressions": 32
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

**10-04 00:01 · Bash** — Read F103 stage notes and variants note

```bash
cd /Users/wxy/Desktop/Partura && for f in 07_S1_structure 07_S2_distil 07_S_final 07_conditional 07_controls 07_neutralise 08_variants; do echo "=================== $f"; cat -n notes/F103_amt_dw_decay/$f.md; done
```

```
=================== 07_S1_structure
     1	**问题**:预测力在收盘竞价额支、粗糙度支,还是两者的乘积里?`ts_min` / `pow_3` / `cross_max` 各自是不是多余的?
     2	
     3	**结果**(引擎求值,和 X1 的数值重建互相印证):
     4	
     5	| 变体 | 做了什么 | 多空夏普 tr / va | 多头腿净超额 tr / va | 与原式 rank 相关 |
     6	|---|---|---|---|---|
     7	| 原式 | — | +4.14 / +2.22 | +6.3% / +3.6% | 1.00 |
     8	| `a_no_tsmin` | 删 `ts_min(·,1)` | +4.14 / +2.22 | +6.3% / +3.6% | 1.00 |
     9	| `a_A5` | 只留收盘竞价额(5 日峰值) | +1.81 / **+3.69** | +7.1% / **+18.0%** | 0.50 |
    10	| `a_C` | 只留粗糙度 | +1.79 / **−1.75** | +4.6% / −21.1% | 0.49 |
    11	| `e_pow1` | 指数 3 → 1 | +2.70 / +3.63 | +5.8% / +14.3% | 0.77 |
    12	| `e_pow2` | 指数 3 → 2 | +3.60 / +3.12 | +6.6% / +9.6% | 0.95 |
    13	| `m_none` | 删 5 日极值 | **+4.35** / +2.41 | +7.1% / +4.1% | 0.84 |
    14	| `m_mean5` | 极值 → 均值 | +4.26 / +2.49 | +7.8% / +6.2% | 0.98 |
    15	| `f_sum` | 收盘竞价额 → 全天成交额 | +3.79 / +2.77 | **+9.5% / +7.4%** | 0.89 |
    16	| `f_share` | 收盘竞价额 → 尾盘占比 | +1.52 / −1.96 | +6.2% / −17.7% | 0.56 |
    17	| `i_rankmul` | 两支各自排名后相乘 | +2.77 / −0.08 | +0.2% / −16.3% | 0.81 |
    18	| `i_addrank` | 两支排名等权相加 | +4.01 / +1.81 | +7.6% / +3.2% | 0.95 |
    19	
    20	**解读**:
    21	
    22	1. **`ts_min(·,1)` 多余**:每个指标逐位相同。
    23	2. **两支单独都不是原式。** `a_A5` 是成交额水平家族(与 `known_amt_max9` 的 rank 相关 0.88、与 `ctl_amt` 0.87;对 `ctl_amt` 中性化 R² 0.748、
    24	   rank IC 0.0392 → 0.0101),train 弱(+1.81)、valid 强(+3.69)。`a_C` 单独几乎没有 rank IC(train +0.0051),
    25	   而且**方向在 valid 反过来**(rank IC −0.0322,十分位剖面从 train 的"Q1 −27.2%、其余平"变成 valid 的单调反向);
    26	   逐年看是 2018 +1.85、2019 +4.08、2020 +3.34 之后 2021 −0.70、2022 −1.03、2023 −3.44。
    27	3. **裸的 `C` 是两个方向相反的东西的混合。** 它与 `ctl_amt` 的 rank 相关 −0.54:一半是"冷清/小票"(这一半在 2021 年之后是正收益),
    28	   另一半是"相对于自身流动性而言曲线粗糙"。对 `ctl_amt` 中性化之后 `a_C` 的 rank IC 从 0.0045 升到 **0.0247**(R² 0.297,无成本多空夏普 +2.41 → +4.54);
    29	   对全部控制变量中性化之后残差 rank IC 0.0162、无成本多空夏普 **+5.47**(R² 0.460)。**乘上 `A` 的作用,就是替 `C` 做了一次粗糙的成交额中性化**
… (100 行略) …
    10	  它们的稳健性是把权重还给成交额水平换来的。中性化之后的 rank IC 却都落在同一个范围:原式 0.0172、`d_sum_k2` 0.0123、`e_peak_k2` 0.0142、`x_std9_k1` 0.0170、`b_stdamt9` 0.0193 ——
    11	  **不在已知暴露里的那部分,各个版本差不多大**(train 上 rank IC 0.012~0.019),区别只在外面裹了多少成交额水平。
    12	- **多头腿与市值**:只对 `ctl_cap` 中性化,多空的 rank IC 都不降反升(`d_sum_k2` 0.0404 → 0.0427,`x_std9_k1` 0.0472 → 0.0506,`b_stdamt9` 0.0484 → 0.0543),
    13	  但多头腿毛超额掉一截:`d_sum_k2` +14.9% → +9.0%,`x_std9_k1` +17.5% → +10.1%,`b_stdamt9` +16.9% → +7.9%;原式只从 +13.5% 到 +12.4%。
    14	  候选的多头腿比原式多出来的那部分,相当一部分是小市值倾斜(X3-E 用另一种做法量到的是同一件事)。
    15	- 残差的扣费夏普普遍为负,是因为残差没有再平滑、换手 20%~45%;alpha 还在不在看 rank IC 和无成本夏普。
=================== 08_variants
     1	总表里 29 行,其实只有一条轴上的几个位置。读法:
     2	
     3	- **同一个东西的不同写法(rank 相关 ≥ 0.95,或者就是同一棵树)**:`v_base` = `a_no_tsmin` = `f_orig`(1.00);`m_mean5`(0.98)、`e_pow2`(0.95)、`i_addrank`(0.95)与原式同族;
     4	  `x_std9_k1_w15` / `x_std9_k1_w60` 与 `x_std9_k1`(0.98 / 0.99);`b_stdamt9` = `f_stdamt9` = 配置里的 `known_stdamt_max9`;`d_sum_k3` = `f_sum_k3`,`d_sum_k2` = `f_sum_k2`,`x_std9_k1` = `f_std9_k1`。
     5	- **一条从"集中度为主"到"成交额水平为主"的轴**,用与 `ctl_amt` 的 rank 相关当坐标:`a_C` −0.54 ≈ `f_share` −0.53(两者相关 0.93)→ `i_rankmul` 0.04 → 原式 0.28 →
     6	  `d_sum_k3` 0.47 → `x_std9_k2` 0.51 → `d_sum_k2` 0.74 ≈ `x_std9_k1` 0.75 → `e_peak_k2` 0.86 → `a_A5` 0.87 ≈ `b_stdamt9` 0.89 ≈ `g_stdB` 0.90 → `d_sum_k1` 0.94 → `d_amt` 1.00。
     7	  **沿这条轴往右走,train 的多空夏普先升后降(峰在 0.3~0.5:原式 +4.14、`d_sum_k3` +3.93、`x_std9_k2` +4.16),valid 的多空夏普一路变好、到 0.75 以上持平在 +3.7~+4.4;往左到 0.04 附近 valid 已经不赚钱(`i_rankmul` −0.08),再往左是亏钱。**
     8	  这张表里几乎所有的差别都能用"它在这条轴上的位置"解释;真正不在轴上的只有两件事:水平腿用 `day_std(Amt)` 的 9 日峰值还是 `day_sum(Amt)`(前者在不活跃的票里也有排序力),
     9	  以及集中度用哪种写法(DW / 峰值占比 —— 两段上分不出高下)。
    10	- **相邻的两个接近同族,两端是两个东西**:`d_sum_k3`–`d_sum_k2` 0.93,`d_sum_k2`–`d_sum_k1` 0.92,`x_std9_k1`–`b_stdamt9` 0.93,而原式–`b_stdamt9` 只有 0.41。
    11	- **哪一列该信**:多头腿净超额和换手要和半衰期一起读 —— 原式和 `x_std9_*` 选中的半衰期是 0~2(换手 7%~10%),`d_sum_*` 是 10~20(换手 2%~4%);
    12	  同一个信号把半衰期从 2 调到 10,train 多头腿净超额能差 2~3 个点(原式 +6.3% → +9.4%,`x_std9_k1` +11.5% → +13.8%),而多空夏普几乎不动。S_final 的摘要里有固定半衰期的对照。
    13	- 全部变体的 `cov` 都是 1.00;`dist` 除 `i_addrank`(0.73,两个排名相加会撞值)外都是 1.00 —— 两道门槛都不构成约束。
```

**10-04 00:01 · Bash** — Read F103 diagnosis, distilled, risks, next notes

```bash
cd /Users/wxy/Desktop/Partura && for f in 09_diagnosis 10_distilled 11_risks 12_next; do echo "=================== $f"; cat -n notes/F103_amt_dw_decay/$f.md; done
```

```
=================== 09_diagnosis
     1	**一句话**:这棵树是「成交额水平 ×(最近 30 天平均日内成交曲线的集中度)^k」。成交额水平是已知家族;集中度是这棵树带来的东西,
     2	它**只在成交活跃的票里、只在空头端**有稳定的预测力。两条腿在时间上轮动,原式把八成权重押在了集中度上。
     3	
     4	### 已确立(每条后面是实验)
     5	
     6	1. **七个算子里三个是多余的。** `ts_min(·,1)` 是恒等(探针 `window_one_is_identity`;S1 `a_no_tsmin` 逐位相同)。`cross_max(·,5)` 只是低通(S1:删掉 +4.35 / +2.41、换成均值 +4.26 / +2.49,原式 +4.14 / +2.22),
     7	   原因在 X3-H:书是对原始数值做 EMA 的,重尾的正数做 EMA 本身就是带衰减的峰值记忆。`day_close(Amt)`(收盘集合竞价那一根)换成全天成交额,多头腿两段都更好(S1 `f_sum`:+9.5% / +7.4% 对 +6.3% / +3.6%)。
     8	   三个一起删(`d_sum_k3`):train / valid +3.93 / +2.88;**留出段 +3.52,原式 +3.18**。
     9	2. **两条腿缺一不可,尺度也不能约掉。** 只留收盘竞价额 +1.81 / +3.69,只留粗糙度 +1.79 / **−1.75**(S1)。把 `A` 换成尺度无关的尾盘占比(`f_share`)−1.96,
    10	   两支排名后相乘(`i_rankmul`,与成交额相关 0.04)−0.08:去掉成交额水平,剩下的在 valid 上不赚钱。
    11	3. **`C` 是"先平均、再量粗糙度",这个顺序不能换。** 逐日独立的分钟噪声被 30 日平均压掉(探针 `noise_averaging_exponent`:DW ∝ N^−0.985),留下的是每天都出现在同一分钟的结构和大到平均不掉的尖峰。
    12	   换成"先逐日算 DW、再平均"之后与 `C` 的相关只有 0.709、与成交额水平 −0.76,代进整树 +1.00 / +1.14(X1-6);用当日 DW 则方向都反(X2-e:−1.38 / −2.77)。窗口 10~60、线性衰减还是等权都是同一个平台(X2-e)。
    13	4. **原式与成交额的相关只有 0.28,是因为 `C³` 把 `A` 的尺度约掉了一半多**(X1-4:`log C ~ log 成交额` 的斜率 −0.174,乘 3 是 −0.52)。所以"全部控制变量 R² 只有 0.227"不说明它新,
    14	   只说明它把最大的已知暴露抵消了(中性化表)。
    15	5. **交互是真的,而且是单边的。** `C` 的条件 rank IC 随成交额五分桶从 −0.0028 走到 −0.0611(S1)。5×5 依次分组里两段都稳定的只有一个角:成交最活跃、曲线又最集中的那 4% 股票,
    16	   次日超额年化 −75% / −64%(用 `C`,X2-b)、−75% / −79%(用峰值占比,X3-F)。成交额低的那几行里,集中度的方向 train 和 valid 相反。
    17	   **集中度是一个"避雷"变量:它告诉你哪些活跃票不能碰,不告诉你该买什么。**
    18	6. **空头端是近期打过板的活跃票。** train 上空头十分位最近 5 日内有过涨停的比例 20.68%(多头十分位 1.37%),成交额 / 波动 / 动量的截面百分位都在 0.62~0.66(X1-8)。
    19	   对全部控制变量中性化后空头腿从 +42.8% 掉到 +9.1%。空头腿没有被"封涨停买不进记 0"抬高:空头十分位的标签缺失率 1.25%,低于全市场的 1.54%(H8b 不成立)。
    20	7. **多头腿的钱来自成交额水平那条腿,而且大半是小市值倾斜。** 成交额水平占比高的候选,多头十分位的市值百分位只有 0.19~0.31(原式 0.46 / 0.38);对市值做秩中性化后,
    21	   `day_sum·C²` 的多头腿净超额从 +7.4% / +13.8% 掉到 +1.8% / +2.2%(X3-E);只对 `ctl_cap` 中性化,多头腿毛超额 +14.9% → +9.0%(中性化表)。
    22	8. **两条腿轮动。** 逐年多空夏普(X3-C、S_final):成交额水平(`day_sum`)2020 年 +0.19、2022 年 +4.07;集中度单独(`p_peak`)2020 年 +4.94、2023 年上半年 −0.28;
    23	   留出段里 2024 / 2025 年 F001 的蒸馏结果是 +2.21 / +2.11,集中度占比最高的 `f_sum_k3` 是 +3.59 / +3.08。**valid(2022-01~2023-08)恰好是成交额水平最强、集中度最弱的一段**(控制变量表)。
    24	9. **"保序的外层变换是 no-op"在这套口径下不成立。** 同一面板取 `log` 或截面排名之后逐日排名不变、rank IC 逐位相同,书却差 0.4~1.1 个夏普(X3-H)。指数 k 因此既定配比、也定尾部有多重。
    25	10. **留出段:事前写下的三条判据都过了。** 纯删节点 `f_sum_k3` +3.52(原式 +3.18);事前推荐的 `f_std9_k1` 多头腿净超额 +11.6%、纯多头夏普 +1.55(原式 +5.5%、+1.04),多空夏普 +3.14;
    26	    `f_std9_k1` 比已知家族基准 `f_stdamt9`(+2.55)高 0.59。
    27	
    28	### 合理但没坐实
    29	
… (134 行略) …
     9	- **容量与成本。** 多头端是全市场成交额最低的那一两成股票;日换手 3.5%~3.9%(半衰期 10),15 bp 单边成本下多头腿每年付出约 3 个点(毛 +15.6% → 净 +12.6%)。
    10	  实际冲击成本在这类股票上会明显高于 15 bp,净超额对成本假设敏感。
    11	- **对平滑方式的依赖。** 原始日频面板不平滑时多空夏普只有 +1.17(换手 27%),半衰期 10 才到 +3.33;而且平滑必须作用在**原始数值**上(重尾 → 带衰减的峰值记忆),
    12	  先取 `log` 或排名再平滑会掉 0.7~1.1 个夏普(X3-H)。换一套组合 / 平滑流程(比如先截面标准化再 EMA),这个因子的表现会变。
    13	  同理,单日的异常成交额(数据错误、复牌首日)会在信号里停留十来天。
    14	- **制度依赖。** (a) 241 根分钟网格的版式:9:30 那根是开盘集合竞价、15:00 那根是收盘集合竞价;沪市 2018-08-20 之前没有收盘集合竞价,那 7 个半月 `C` 在沪深之间有系统性差异(X2-c)。
    15	  交易所再改竞价规则,`C` 的截面分布会跟着变。(b) 标签剔除了次日开盘封涨停买不进的票;空头端五分之一是近期打过板的票,涨跌停制度改变会直接影响空头腿。
    16	- **泄漏。** 没有发现:所有日轴算子的因果性探针通过,标签是 t+1 开盘 15 分钟 VWAP 到 t+2 同一价,因子只用到 t 日 15:00。
    17	- **过拟合。** 全研究在 train / valid 上看过 24 个引擎变体和三份脚本里约 80 行数值重建;最终结构只有两个参数(平均窗口 30、指数 2),邻域(窗口 10~60、指数 1~3、DW / 峰值占比 / CV)都是平台或单调曲线,没有孤立的尖峰。
=================== 12_next
     1	只列能明显降低不确定性的:
     2	
     3	1. **把空头端那个角当成剔除名单来测。** 这棵树最稳的发现是"成交最活跃 × 平均曲线最集中"的 4% 股票次日年化 −75% 上下(train / valid 都是)。
     4	   对一个纯多头的使用者,它的用法不是十分位多头书,而是从任何多头组合里剔掉这些票。需要一个带持仓约束的组合回测,十分位口径回答不了。
     5	2. **集中度那条腿在 2024–2025 年是不是真的回来了。** 留出段的排序(`f_sum_k3` > `f_sum_k2` > `f_stdamt9`)指向"是",但没有直接量过成交额中性的集中度在那段时间的 rank IC。
     6	   等 2026 年的数据进来之后,用新数据量(不要回头再读这段留出段)。它决定指数该往 3 还是往 1 调。
     7	3. **市值中性口径下的多头腿。** 在市值分层内部建多头书(或对市值 + 行业中性),看推荐版的多头腿还剩多少。现在只知道 train / valid 上秩中性化之后剩 +2% 左右。
     8	4. **与 F001 蒸馏结果一起放进组合时的边际贡献。** 两者 rank 相关 0.74;留出段上集中度给已知家族加了 0.59 个多空夏普,但那是乘法合成的结果,不是组合层面的边际。
     9	5. **"开盘第一分钟成交占比"单独立项。** `p_peak` 九成就是它;它在峰值落在开盘的 2,800 多只股票里组内 rank IC −0.046 / −0.021,而"收盘集合竞价占比"方向不稳。
    10	   这是一个比 DW 更可解释的集中度写法,值得作为独立因子走一遍同样的流程(这次没有把它放进留出段)。
```

**10-04 00:01 · Bash** — Read F103 custom analysis notes x1 x2 x3

```bash
cd /Users/wxy/Desktop/Partura && for f in 07x_x1_anatomy 07x_x2_interaction 07x_x3_family; do echo "=================== $f"; cat -n notes/F103_amt_dw_decay/$f.md; done
```

```
=================== 07x_x1_anatomy
     1	**脚本** `studies/F103_amt_dw_decay/x1_anatomy.py`(只读 train / valid)。它不是在挑变体,而是在量这棵树的两支各是什么、谁说了算。
     2	
     3	**1. `ts_min(·, 1)` 是恒等。** 删掉它之后与原式的 rank 相关 1.000000,NaN 位置一致率 1.000000,最大相对差 0。
     4	
     5	**2. `day_close(Amt)` 就是 15:00 那一根 = 收盘集合竞价成交额**(100% 的格子里与第 240 列相同)。版式核对:
     6	
     7	| | 14:58–14:59 两根 / 全天(中位) | 15:00 那根 / 全天(中位) |
     8	|---|---|---|
     9	| 沪市,2018-08-17 之前 | **1.45%**(只有 0.3% 的格子为 0)—— 还在连续竞价 | 0.90% |
    10	| 深市,同期 | 0.00%(82.6% 为 0) | 1.34% |
    11	| 沪市,2018-08-20 之后(train) | 0.00%(70.9% 为 0) | 1.17% |
    12	| 深市,同期 | 0.00%(56.6% 为 0) | 1.21% |
    13	
    14	沪市在 2018-08-20 引入收盘集合竞价之前,最后一根只是连续竞价的普通一分钟(H9 的前提成立,后果在 X2 里量)。
    15	开盘那边:9:30 那根中位只占全天 0.3%~0.4%,9:31 那根占 1.0%~1.9%。
    16	
    17	**3. 两支在 log 空间里几乎等权,而且彼此负相关。** 日截面离散度:`log max5(A)` 1.211,`3·log C` 1.289(`log C` 0.430),`log G` 1.425。
    18	`max5(A)` 与 `C` 的 rank 相关 **−0.416**。秩空间里 `G` 被 `C` 单独张成 0.257、被 `max5(A)` 单独张成 0.259、被两者一起张成 **0.864** ——
    19	`G` 基本就是两支的排名相加,谁也不主导。
    20	
    21	**4. `C³` 约掉了 `A` 一半多的成交额尺度(H6 的前半句成立)。** 截面回归斜率:`log C ~ log day_sum` 为 **−0.174**(乘 3 = −0.521),
    22	`log A ~ log day_sum` 为 +0.935。所以 `A·C³ ∝ 成交额^0.41 × (与成交额无关的粗糙度)³`:
    23	整棵树大约是"两成成交额水平 + 八成**成交额中性的粗糙度**"。这解释了它与 `ctl_amt` 的 rank 相关为什么只有 0.28。
    24	
    25	**5. `C` 主要是内部分钟的块状噪声,集合竞价那几根是次要成分 —— 但预测力恰恰在次要成分上(见 X2 第 e 节;更直接的证据在 X3-D:纯内部的 DW 对成交额中性化后 train 残差 rank IC 只有 −0.0086,`C` 是 −0.0253)。**
    26	秩空间里 `C` 被"切掉首尾 5 根的内部 DW"张成 0.691,被平均曲线的收盘竞价占比张成 0.182,三者(内部 + 收盘占比 + 首根占比)合计 0.816;
    27	30 日的日成交额变异系数只张成 0.079(逐日的"放量日独占平均曲线"不是主因,先按日归一再平均的版本与 `C` 的相关是 0.930)。
    28	`C` 与 `ctl_amt` 的 rank 相关 **−0.539**、与市值 −0.379、与价格 −0.425:**裸的 `C` 首先是个"冷清/小票"的代理**。
    29	
… (247 行略) …
   124	峰值在盘中别处(每天约 420 只,一次性的大单没被 30 天平均掉)−0.0523 / −0.0299;峰值在收盘竞价 −0.0182 / **+0.0184**(方向反了)。
   125	"收盘集合竞价占比"单独当因子是 +1.12 / −1.68 —— **收盘竞价那一根带来的集中度是最不稳的一种**;这和 S1 里把 `A` 换成尾盘占比(`f_share`)在 valid 上 −1.96 是同一件事。
   126	
   127	**H. 保序变换在这套口径下不是 no-op(H18 成立)。** 书是先对**原始数值**做 EMA、再排名的。同一个面板、逐日排名完全相同,只换 EMA 的对象:
   128	
   129	| | 半衰期 | 多空夏普 tr / va | 多头腿净超额 tr / va | 换手 |
   130	|---|---|---|---|---|
   131	| `day_sum` 原值 | 5 | +1.42 / +3.68 | +9.4% / +21.0% | 4.0% |
   132	| `log(day_sum)` | 3 | +1.03 / +3.47 | +4.5% / +19.1% | 5.5% |
   133	| `day_sum·C` 原值 | 10 | +2.36 / +3.97 | +12.5% / +20.7% | 3.3% |
   134	| `log(day_sum·C)` | 2 | +1.80 / +3.50 | +3.2% / +12.7% | 9.1% |
   135	| `day_sum·C²` 原值 | 10 | +3.33 / +3.78 | +11.4% / +14.5% | 4.0% |
   136	| `log(day_sum·C²)` | 5 | +2.60 / +3.42 | +6.3% / +13.7% | 5.9% |
   137	| `rank(day_sum·C²)` | 5 | +2.27 / +3.08 | +7.4% / +13.8% | 6.0% |
   138	| `day_sum·p_peak²` 原值 | 5 | +3.10 / +3.97 | +13.6% / +15.5% | 4.6% |
   139	| `rank(day_sum·p_peak²)` | 2 | +2.25 / +3.51 | +9.2% / +13.3% | 7.5% |
   140	
   141	rank IC 逐位相同(例如 k = 2 三行都是 0.0464 / 0.0491),书却不同:train 上多空夏普差 0.4~1.1(valid 0.2~0.7),train 上多头腿净超额少三分之一到四分之三。重尾的正数直接做 EMA,等于"带衰减的峰值记忆":一次放量之后这只票会在高位停留很多天;
   142	先取 `log` 或排名再做 EMA 就成了普通的均值平滑,换手更高、表现更差。**这解释了两件事**:(1) 原式外层的 `cross_max(·,5)` 为什么可以删 —— EMA 作用在重尾量上已经在做同一件事;
   143	(2) 指数 k 不只是在给两支定权,它还决定尾部有多重。这条对实验室里"保序外层变换是 no-op"的先验是一个修正:**那条只在半衰期 = 0 时成立。**
```

**10-04 00:02 · Bash** — Read the reviewer's audit log output

```bash
cd /Users/wxy/Desktop/Partura && cat logs/F103_amt_dw_decay_audit1.log
```

```
== 0. 内部函数源码(服务器上的 AlphaCube) ==
--- alphacube.operators.dt_cross.rolling_reduce  (2 lines)
def rolling_reduce(x: torch.Tensor, d: int, reducer, axis: int = 0) -> torch.Tensor:
    return reducer(rolling_windows(x, d, axis))
--- alphacube.operators.dt_cross.decay_linear_last  (9 lines)
def decay_linear_last(w: torch.Tensor) -> torch.Tensor:
    """Linearly-weighted (most recent = heaviest) mean over valid entries."""
    d = w.shape[-1]
    weights = torch.arange(1, d + 1, dtype=w.dtype, device=w.device)
    valid = ~torch.isnan(w)
    w_filled = torch.where(valid, w, torch.zeros_like(w))
    weighted_sum = (w_filled * weights).sum(dim=-1)
    weight_total = (valid.to(w.dtype) * weights).sum(dim=-1)
    return torch.where(weight_total > EPS, weighted_sum / weight_total, torch.full_like(weighted_sum, float("nan")))
--- alphacube.operators.dt_cross.nanmax_last  (4 lines)
def nanmax_last(w: torch.Tensor) -> torch.Tensor:
    filled = torch.where(torch.isnan(w), torch.full_like(w, float("-inf")), w)
    out = filled.max(dim=-1).values
    return torch.where(torch.isnan(w).all(dim=-1), torch.full_like(out, float("nan")), out)
--- alphacube.operators.dt_day.last_valid_last  (13 lines)
def last_valid_last(w: torch.Tensor) -> torch.Tensor:
    """Last non-NaN value along the last dim; NaN if the slice has none.
    Shared by DT's `day_last`/`in_last`, same contract as `first_valid_last`.
    """
    d = w.shape[-1]
    idx = torch.arange(d, device=w.device).expand_as(w)
    valid = ~torch.isnan(w)
    idx_when_valid = torch.where(valid, idx, torch.full_like(idx, -1))
    last_idx = idx_when_valid.max(dim=-1, keepdim=True).values
    has_valid = last_idx >= 0
… (187 行略) …
-- 控制变量: 换手率+市值  (组内 R2 train 0.195 / valid 0.121)
原始 C 最高组                      -75.4    -63.6    -86.6    -86.9    -77.7    -50.3    -80.9    -34.6
残差 C 最高组                      -51.5    -44.7    -53.6    -57.4    -56.6    -38.4    -57.8    -22.8
已知暴露拟合值 最高组                   -74.4    -85.5    -63.6    -78.1    -78.8    -77.0    -97.9    -64.8
原始 C (5-1)                    -88.4    -34.3    -85.6   -111.8   -114.8    -41.3    -58.7     +6.8
残差 C (5-1)                    -58.5    -13.5    -48.5    -76.0    -81.4    -28.2    -32.3    +18.0
原始 C 组内 rank IC             -0.0613  -0.0254  -0.0604  -0.0806  -0.0705  -0.0337  -0.0359  -0.0078
残差 C 组内 rank IC             -0.0371  -0.0038  -0.0352  -0.0487  -0.0472  -0.0175  -0.0127  +0.0111
拟合值 组内 rank IC              -0.0706  -0.0727  -0.0612  -0.0883  -0.0778  -0.0553  -0.0731  -0.0721
-- 控制变量: 全部已知  (组内 R2 train 0.410 / valid 0.327)
原始 C 最高组                      -68.6    -57.9    -85.4    -86.5    -68.0    -35.9    -74.7    -29.8
残差 C 最高组                      -32.5    -21.7    -37.7    -40.0    -28.5    -24.4    -29.7     -8.2
已知暴露拟合值 最高组                   -66.7    -74.6    -73.3    -88.3    -66.1    -39.6    -89.8    -49.0
原始 C (5-1)                    -81.1    -28.1    -80.8   -111.6   -104.1    -27.6    -51.3    +10.8
残差 C (5-1)                    -33.6    +12.5    -31.9    -46.4    -45.5    -10.4     -0.2    +33.9
原始 C 组内 rank IC             -0.0590  -0.0232  -0.0588  -0.0812  -0.0670  -0.0289  -0.0335  -0.0060
残差 C 组内 rank IC             -0.0230  +0.0057  -0.0226  -0.0300  -0.0278  -0.0113  -0.0015  +0.0177
拟合值 组内 rank IC              -0.0646  -0.0482  -0.0588  -0.0875  -0.0773  -0.0342  -0.0544  -0.0379
[audit] done 389s
[partura exit 0 2026-10-04_14:54:13]
```

**10-04 00:02 · Bash** — Inspect structure of final.json

```bash
cd /Users/wxy/Desktop/Partura && python3 - <<'EOF'
import json
d=json.load(open('runs/F103_amt_dw_decay/final.json'))
print(d.keys())
def show(o,depth=0,maxd=3,pre=''):
    if isinstance(o,dict):
        for k,v in o.items():
            t=type(v).__name__
            s=''
            if isinstance(v,(int,float,str,bool)) or v is None: s=repr(v)[:80]
            elif isinstance(v,list): s=f'list[{len(v)}]'
            print(pre+str(k),t,s)
            if depth<maxd: show(v,depth+1,maxd,pre+'   ')
    elif isinstance(o,list) and o and isinstance(o[0],dict) and depth<maxd:
        show(o[0],depth+1,maxd,pre+'   [0].')
v=d['variants'] if 'variants' in d else None
print(type(v))
if isinstance(v,list):
    show(v[0],0,2)
else:
    k=list(v.keys())[0]; print(k); show(v[k],0,2)
EOF
```

```
Exit code 1
dict_keys(['factor_id', 'config', 'stages', 'provenance', 'view', 'label', 'cost_per_side', 'top_frac', 'fit_split', 'user_split', 'rank_by', 'halflives', 'splits_used', 'split_dates', 'results', 'errors', 'engine_timings', 'diagnostics', 'seconds', 'peak_anon_gb'])
<class 'NoneType'>
Traceback (most recent call last):
  File "<stdin>", line 20, in <module>
AttributeError: 'NoneType' object has no attribute 'keys'
```

**10-04 00:02 · Bash** — Inspect results structure of final.json

```bash
cd /Users/wxy/Desktop/Partura && python3 - <<'EOF'
import json
d=json.load(open('runs/F103_amt_dw_decay/final.json'))
def show(o,depth=0,maxd=3,pre=''):
    if isinstance(o,dict):
        for k,v in o.items():
            t=type(v).__name__
            s=''
            if isinstance(v,(int,float,str,bool)) or v is None: s=repr(v)[:100]
            elif isinstance(v,list): s=f'list[{len(v)}]'
            print(pre+str(k),t,s)
            if depth<maxd: show(v,depth+1,maxd,pre+'   ')
    elif isinstance(o,list) and o and isinstance(o[0],dict) and depth<maxd:
        show(o[0],depth+1,maxd,pre+'   [0].')
r=d['results']
print(type(r), len(r))
if isinstance(r,list): show(r[0],0,3)
else:
    k=list(r.keys())[0]; print(k); show(r[k],0,3)
print('diag keys', d['diagnostics'].keys() if isinstance(d['diagnostics'],dict) else type(d['diagnostics']))
print(d['stages'], d['splits_used'], d['halflives'])
EOF
```

```
<class 'dict'> 5
f_orig
expr str 'cross_max(mul(day_close(Amt), ts_min(pow_3(day_durbin_watson(cross_decay_linear(Amt, 30))), 1)), 5)
stage str 'S_final'
why str '原式(7 个算子)'
group str 'final'
sign float -1.0
splits dict 
   train dict 
      sign float -1.0
      ic float 0.01930447112968993
      icir float 0.4461308144289802
      ic_t float 13.916135260420633
      rank_ic float 0.03927507962238811
      rank_icir float 0.5113378874076997
      rank_ic_t float 15.950136091924357
      ic_pos float 0.6988694758478932
      coverage float 0.6910973684106901
      coverage_labelled float 0.99920783881081
      n_days int 973
   valid dict 
      sign float -1.0
      ic float 0.012461839211841491
      icir float 0.28623428195305745
      ic_t float 5.623611363506585
      rank_ic float 0.027891842229732837
      rank_icir float 0.29174670459111784
      rank_ic_t float 5.731913284493574
      ic_pos float 0.6450777202072538
      coverage float 0.8946648005876163
… (161 行略) …
         long_ann float 0.07165360237033395
         long_mdd float -0.0691695645546433
         long_gross_ann float 0.10164044228668472
         long_turnover float 0.039692259723214086
         short_gross_ann float 0.2669921708364147
         long_share float 0.27572287059892714
         n_days int 581
profile dict 
   train list list[10]
         [0].quantile int 1
         [0].excess_ann float -0.4379651868659651
         [0].sharpe float -6.320135641780881
         [0].win float 0.34121274409044194
   valid list list[10]
         [0].quantile int 1
         [0].excess_ann float -0.29100282898397795
         [0].sharpe float -3.803482553130161
         [0].win float 0.39896373056994816
diag keys dict_keys(['by_year', 'by_year_scope', 'rank_corr_train'])
['S_final'] ['train', 'valid', 'utrain', 'holdout', 'full'] [0.0, 1, 2, 3, 5, 10, 20]
```

**10-04 00:02 · Bash** — Extract books at chosen and long-optimal half-lives from final.json

```bash
cd /Users/wxy/Desktop/Partura && python3 - <<'EOF'
import json
d=json.load(open('runs/F103_amt_dw_decay/final.json'))
r=d['results']
def row(s):
    return f"LS {s['ls_sharpe']:+.3f} | Lgross {s['long_gross_ann']*100:+.2f}% | Lnet {s['long_ann']*100:+.2f}% | Lshr {s['long_sharpe']:+.3f} | Lmdd {s['long_mdd']*100:+.1f}% | TO {s['ls_turnover']*100:.2f}% | LTO {s['long_turnover']*100:.2f}% | share {s['long_share']:.3f} | short_gross {s['short_gross_ann']*100:+.1f}%"
for k,v in r.items():
    print('=====',k, v['expr'])
    b=v['books']; bu=v['books_user']
    print(' decision: hl_ls',b['hl_ls'],'hl_long',b['hl_long'],'hl_used',b['hl_used'])
    for sp in ('train','valid'):
        print('   ',sp,'@hl_used', row(b['splits'][sp]))
    for sp in ('train','valid'):
        print('   ',sp,'@hl_long', row(b['splits_at_hl_long'][sp]))
    print(' user: hl_ls',bu['hl_ls'],'hl_long',bu['hl_long'],'hl_used',bu['hl_used'])
    for sp in ('utrain','holdout'):
        print('   ',sp,'@hl_used', row(bu['splits'][sp]))
    for sp in ('utrain','holdout'):
        print('   ',sp,'@hl_long', row(bu['splits_at_hl_long'][sp]))
    print(' user sweep (utrain):')
    for s in bu['sweep']:
        print('     hl',s['halflife'],'LS',round(s['ls_sharpe'],3),'TO',round(s['ls_turnover']*100,2),'Lshr',round(s['long_sharpe'],3),'Lnet',round(s['long_ann']*100,2),'LTO',round(s['long_turnover']*100,2))
    print(' ic_holdout rank_ic', v['ic_holdout']['rank_ic'], ' ic_user', v['ic_user']['rank_ic'])
print(json.dumps(d['diagnostics']['rank_corr_train'],indent=0)[:3000])
print(d['diagnostics']['by_year_scope'])
EOF
```

```
Exit code 1
===== f_orig cross_max(mul(day_close(Amt), ts_min(pow_3(day_durbin_watson(cross_decay_linear(Amt, 30))), 1)), 5)
 decision: hl_ls 2.0 hl_long 10.0 hl_used 2.0
    train @hl_used LS +4.140 | Lgross +13.47% | Lnet +6.31% | Lshr +1.301 | Lmdd -8.9% | TO 8.46% | LTO 9.47% | share 0.239 | short_gross +42.8%
    valid @hl_used LS +2.216 | Lgross +10.94% | Lnet +3.61% | Lshr +0.663 | Lmdd -4.2% | TO 8.46% | LTO 9.69% | share 0.277 | short_gross +28.5%
    train @hl_long LS +4.089 | Lgross +12.43% | Lnet +9.41% | Lshr +1.856 | Lmdd -7.7% | TO 3.63% | LTO 3.99% | share 0.280 | short_gross +32.0%
    valid @hl_long LS +2.066 | Lgross +7.78% | Lnet +4.53% | Lshr +0.732 | Lmdd -6.8% | TO 3.78% | LTO 4.30% | share 0.254 | short_gross +22.9%
 user: hl_ls 2.0 hl_long 10.0 hl_used 2.0
    utrain @hl_used LS +3.533 | Lgross +12.75% | Lnet +5.57% | Lshr +1.108 | Lmdd -9.1% | TO 8.43% | LTO 9.50% | share 0.248 | short_gross +38.7%
    holdout @hl_used LS +3.180 | Lgross +12.41% | Lnet +5.47% | Lshr +1.044 | Lmdd -7.1% | TO 8.20% | LTO 9.19% | share 0.253 | short_gross +36.6%
    utrain @hl_long LS +3.395 | Lgross +11.11% | Lnet +8.05% | Lshr +1.487 | Lmdd -7.7% | TO 3.64% | LTO 4.05% | share 0.274 | short_gross +29.4%
    holdout @hl_long LS +2.923 | Lgross +10.16% | Lnet +7.17% | Lshr +1.260 | Lmdd -6.9% | TO 3.60% | LTO 3.97% | share 0.276 | short_gross +26.7%
 user sweep (utrain):
     hl 0.0 LS 2.793 TO 14.34 Lshr -0.555 Lnet -2.66 LTO 17.61
     hl 1.0 LS 3.265 TO 10.56 Lshr 0.512 Lnet 2.5 LTO 12.22
     hl 2.0 LS 3.533 TO 8.43 Lshr 1.108 Lnet 5.57 LTO 9.5
     hl 3.0 LS 3.504 TO 7.12 Lshr 1.292 Lnet 6.63 LTO 7.97
     hl 5.0 LS 3.473 TO 5.51 Lshr 1.385 Lnet 7.27 LTO 6.14
     hl 10.0 LS 3.395 TO 3.64 Lshr 1.487 Lnet 8.05 LTO 4.05
     hl 20.0 LS 3.219 TO 2.32 Lshr 1.394 Lnet 7.64 LTO 2.57
 ic_holdout rank_ic 0.03867540871856646  ic_user 0.03604187165066998
===== f_sum_k3 mul(day_sum(Amt), pow_3(day_durbin_watson(cross_decay_linear(Amt, 30))))
 decision: hl_ls 20.0 hl_long 20.0 hl_used 20.0
    train @hl_used LS +3.927 | Lgross +13.12% | Lnet +11.08% | Lshr +2.244 | Lmdd -5.9% | TO 2.40% | LTO 2.69% | share 0.285 | short_gross +32.9%
    valid @hl_used LS +2.879 | Lgross +9.75% | Lnet +7.52% | Lshr +1.454 | Lmdd -4.7% | TO 2.54% | LTO 2.96% | share 0.275 | short_gross +25.7%
Traceback (most recent call last):
  File "<stdin>", line 13, in <module>
KeyError: 'splits_at_hl_long'
```

**10-04 00:02 · Bash** — Extract remaining candidates' books from final.json

```bash
cd /Users/wxy/Desktop/Partura && python3 - <<'EOF'
import json
d=json.load(open('runs/F103_amt_dw_decay/final.json'))
r=d['results']
def row(s):
    return f"LS {s['ls_sharpe']:+.3f} | Lgross {s['long_gross_ann']*100:+.2f}% | Lnet {s['long_ann']*100:+.2f}% | Lshr {s['long_sharpe']:+.3f} | Lmdd {s['long_mdd']*100:+.1f}% | TO {s['ls_turnover']*100:.2f}% | LTO {s['long_turnover']*100:.2f}% | share {s['long_share']:.3f} | short_gross {s['short_gross_ann']*100:+.1f}%"
for k,v in r.items():
    if k=='f_orig': continue
    print('=====',k, v['expr'])
    b=v['books']; bu=v['books_user']
    print(' decision: hl_ls',b['hl_ls'],'hl_long',b['hl_long'],'hl_used',b['hl_used'])
    for sp in ('train','valid'):
        print('   ',sp,'@hl_used', row(b['splits'][sp]))
    if 'splits_at_hl_long' in b:
      for sp in ('train','valid'):
        print('   ',sp,'@hl_long', row(b['splits_at_hl_long'][sp]))
    print(' user: hl_ls',bu['hl_ls'],'hl_long',bu['hl_long'],'hl_used',bu['hl_used'])
    for sp in ('utrain','holdout'):
        print('   ',sp,'@hl_used', row(bu['splits'][sp]))
    if 'splits_at_hl_long' in bu:
      for sp in ('utrain','holdout'):
        print('   ',sp,'@hl_long', row(bu['splits_at_hl_long'][sp]))
    print(' user sweep (utrain):')
    for s in bu['sweep']:
        print('     hl',s['halflife'],'LS',round(s['ls_sharpe'],3),'TO',round(s['ls_turnover']*100,2),'Lshr',round(s['long_sharpe'],3),'Lnet',round(s['long_ann']*100,2),'LTO',round(s['long_turnover']*100,2))
    print(' ic_holdout rank_ic', v['ic_holdout']['rank_ic'], ' ic_user', v['ic_user']['rank_ic'])
print(json.dumps(d['diagnostics']['rank_corr_train'])[:3000])
print(d['diagnostics']['by_year_scope'])
EOF
```

```
===== f_sum_k3 mul(day_sum(Amt), pow_3(day_durbin_watson(cross_decay_linear(Amt, 30))))
 decision: hl_ls 20.0 hl_long 20.0 hl_used 20.0
    train @hl_used LS +3.927 | Lgross +13.12% | Lnet +11.08% | Lshr +2.244 | Lmdd -5.9% | TO 2.40% | LTO 2.69% | share 0.285 | short_gross +32.9%
    valid @hl_used LS +2.879 | Lgross +9.75% | Lnet +7.52% | Lshr +1.454 | Lmdd -4.7% | TO 2.54% | LTO 2.96% | share 0.275 | short_gross +25.7%
 user: hl_ls 10.0 hl_long 20.0 hl_used 10.0
    utrain @hl_used LS +3.640 | Lgross +11.76% | Lnet +8.43% | Lshr +1.658 | Lmdd -7.2% | TO 3.86% | LTO 4.41% | share 0.243 | short_gross +36.6%
    holdout @hl_used LS +3.518 | Lgross +12.32% | Lnet +9.23% | Lshr +1.765 | Lmdd -5.1% | TO 3.66% | LTO 4.09% | share 0.258 | short_gross +35.4%
    utrain @hl_long LS +3.628 | Lgross +12.16% | Lnet +10.09% | Lshr +2.015 | Lmdd -5.9% | TO 2.41% | LTO 2.74% | share 0.283 | short_gross +30.9%
    holdout @hl_long LS +3.331 | Lgross +12.63% | Lnet +10.65% | Lshr +1.989 | Lmdd -5.4% | TO 2.37% | LTO 2.61% | share 0.307 | short_gross +28.6%
 user sweep (utrain):
     hl 0.0 LS 1.476 TO 25.05 Lshr -3.125 Lnet -14.76 LTO 29.09
     hl 1.0 LS 2.887 TO 13.91 Lshr -0.536 Lnet -2.61 LTO 15.91
     hl 2.0 LS 3.339 TO 9.65 Lshr 0.455 Lnet 2.26 LTO 10.99
     hl 3.0 LS 3.537 TO 7.8 Lshr 0.984 Lnet 4.93 LTO 8.89
     hl 5.0 LS 3.624 TO 5.87 Lshr 1.299 Lnet 6.57 LTO 6.69
     hl 10.0 LS 3.64 TO 3.86 Lshr 1.658 Lnet 8.43 LTO 4.41
     hl 20.0 LS 3.628 TO 2.41 Lshr 2.015 Lnet 10.09 LTO 2.74
 ic_holdout rank_ic 0.043584156155321074  ic_user 0.038870737294567394
===== f_sum_k2 mul(day_sum(Amt), pow_2(day_durbin_watson(cross_decay_linear(Amt, 30))))
 decision: hl_ls 10.0 hl_long 20.0 hl_used 10.0
    train @hl_used LS +3.326 | Lgross +14.88% | Lnet +11.38% | Lshr +1.983 | Lmdd -6.9% | TO 3.95% | LTO 4.63% | share 0.281 | short_gross +38.0%
    valid @hl_used LS +3.781 | Lgross +17.93% | Lnet +14.53% | Lshr +2.697 | Lmdd -3.9% | TO 3.84% | LTO 4.50% | share 0.331 | short_gross +36.2%
    train @hl_long LS +3.046 | Lgross +14.74% | Lnet +12.61% | Lshr +2.189 | Lmdd -5.9% | TO 2.44% | LTO 2.83% | share 0.329 | short_gross +30.1%
    valid @hl_long LS +3.773 | Lgross +17.33% | Lnet +15.26% | Lshr +2.811 | Lmdd -3.8% | TO 2.42% | LTO 2.74% | share 0.356 | short_gross +31.4%
 user: hl_ls 10.0 hl_long 20.0 hl_used 10.0
    utrain @hl_used LS +3.446 | Lgross +15.74% | Lnet +12.30% | Lshr +2.179 | Lmdd -6.9% | TO 3.89% | LTO 4.56% | share 0.296 | short_gross +37.5%
    holdout @hl_used LS +3.099 | Lgross +15.58% | Lnet +12.64% | Lshr +2.071 | Lmdd -5.2% | TO 3.45% | LTO 3.88% | share 0.311 | short_gross +34.6%
    utrain @hl_long LS +3.233 | Lgross +15.48% | Lnet +13.39% | Lshr +2.360 | Lmdd -5.9% | TO 2.40% | LTO 2.77% | share 0.337 | short_gross +30.4%
    holdout @hl_long LS +2.876 | Lgross +15.34% | Lnet +13.54% | Lshr +2.233 | Lmdd -5.1% | TO 2.15% | LTO 2.39% | share 0.355 | short_gross +27.8%
 user sweep (utrain):
… (30 行略) …
    train @hl_used LS +2.472 | Lgross +16.87% | Lnet +9.26% | Lshr +1.371 | Lmdd -10.7% | TO 8.53% | LTO 10.07% | share 0.309 | short_gross +37.7%
    valid @hl_used LS +4.437 | Lgross +24.92% | Lnet +18.47% | Lshr +3.092 | Lmdd -4.4% | TO 7.73% | LTO 8.53% | share 0.341 | short_gross +48.1%
    train @hl_long LS +2.174 | Lgross +17.11% | Lnet +13.70% | Lshr +1.992 | 
… (2713 字符略) …
std9_k1": 0.8594739066129753, "f_stdamt9": 0.7413267226306695, "ctl_amt": 0.7445991437629734, "ctl_cap": 0.39589173913655523, "ctl_turnrate": 0.409370338984404, "ctl_ivol": 0.40398882988173374, "ctl_dvol20": 0.331133341891465, "ctl_price": 0.2318687132395211, "ctl_rev1": 0.07077833565956432, "ctl_mom20": 0.3169401959823255, "known_amt_max9": 0.6855759105296519, "known_stdamt_max9": 0.7413267226306695, "known_ivol_max9": 0.3313878232491323, "ref_base": 0.745168134833809, "ref_A5": 0.7046624420919942, "ref_C": 0.08455442369507607}, "f_std9_k1": {"f_orig": 0.6474741812932763, "f_sum_k3": 0.7399295047327916, "f_sum_k2": 0.8594739066129753, "f_std9_k1": 1.0, "f_stdamt9": 0.9303417300849606, "ctl_amt": 0.7539435560758352, "ctl_cap": 0.41507377479376684, "ctl_turnrate": 0.40085102469075695, "ctl_ivol": 0.34425408583692335, "ctl_dvol20": 0.45936331043361434, "ctl_price": 0.2674220283398629, "ctl_rev1": -0.009096948076589988, "ctl_mom20": 0.30212757897659365, "known_amt_max9": 0.8380009550893623, "known_stdamt_max9": 0.9303417300849606, "known_ivol_max9": 0.4498093136376241, "ref_base": 0.6474741812932763, "ref_A5": 0.7740070441583977, "ref_C": -0.07425402509024856}, "f_stdamt9": {"f_orig": 0.4118974628512611, "f_sum_k3": 0.5205022575586071, "f_sum_k2": 0.7413267226306695, "f_std9_k1": 0.9303417300849606, "f_stdamt9": 1.0, "ctl_amt": 0.8884400267684931, "ctl_cap": 0.49477380742033733, "ctl_turnrate": 0.4680378823668786, "ctl_ivol": 0.3048925165565681, "ctl_dvol20": 0.5298942543716674, "ctl_price": 0.3773560909874716, "ctl_rev1": -0.016583339155172815, "ctl_mom20": 0.27118501937575923, "known_amt_max9": 0.9629155059841004, "
['20180102', '20251231']
```

**10-04 00:04 · Bash** — Check file timestamps, final log, and study.sh wrapper

```bash
cd /Users/wxy/Desktop/Partura && stat -f "%Sm %N" -t "%Y-%m-%d %H:%M:%S" configs/F103_amt_dw_decay.yaml notes/F103_amt_dw_decay/10_distilled.md runs/F103_amt_dw_decay/final.json logs/F103_amt_dw_decay_final.log studies/F103_amt_dw_decay/audit_1.py logs/F103_amt_dw_decay_audit1.log && cat logs/F103_amt_dw_decay_final.log && cat scripts/study.sh
```

```
2026-10-03 23:22:50 configs/F103_amt_dw_decay.yaml
2026-10-03 23:34:34 notes/F103_amt_dw_decay/10_distilled.md
2026-10-03 23:26:41 runs/F103_amt_dw_decay/final.json
2026-10-03 23:26:42 logs/F103_amt_dw_decay_final.log
2026-10-03 23:47:14 studies/F103_amt_dw_decay/audit_1.py
2026-10-03 23:54:13 logs/F103_amt_dw_decay_audit1.log
[probes] studies/F103_amt_dw_decay/probes.py: +isolated_spike_response, noise_averaging_exponent, impulse_footprint, window_one_is_identity, trailing_nan_fallback
/root/autodl-tmp/AlphaCube/src/alphacube/operators/dt_in.py:785: FutureWarning: We've integrated functorch into PyTorch. As the final step of the integration, `functorch.vmap` is deprecated as of PyTorch 2.0 and will be deleted in a future version of PyTorch >= 2.3. Please use `torch.vmap` instead; see the PyTorch 2.0 release notes and/or the `torch.func` migration guide for more details https://pytorch.org/docs/main/func.migrating.html
  return vmap(single_row)(x).unsqueeze(-1)
[runner] 14:23:39 label == /root/autodl-tmp/AlphaCube/_bench/trainto/allfac_buyable/_target.npy
[runner] 14:23:40 metrics: 5 variants; decision splits ['train', 'valid'], fit on 'train'; HOLDOUT WILL BE READ
[runner] 14:25:35 diagnostics: by_year
[runner] 14:25:43 diagnostics: rank correlation matrix (19 panels)
[runner] wrote /root/autodl-tmp/Partura/runs/F103_amt_dw_decay/final.json (184.0s, peak anon 2.61 GiB)
[partura exit 0 2026-10-04_14:26:42]
#!/bin/bash
# One study's lifeline to the server.  Run from the Mac, in ~/Desktop/Partura.
# Each subcommand touches ONLY this study's files (configs/<fid>.yaml, studies/<fid>/, notes/<fid>/,
# runs/<fid>/), so several studies can run side by side without stepping on each other.
#
#   study.sh ops [regex]                   list operators (name, face/family/category, windows) — the vocabulary
#   study.sh src <operator> [...]          print the server's kernel source of an operator (the source of truth)
#   study.sh check <fid>                   parse every expression of the config on the server (do this before `run`)
#   study.sh decompose <fid>               operator dossiers + SSA decomposition + lab priors, on the server
#   study.sh propose <fid>                 candidate experiments derived from the tree (a DRAFT to curate)
#   study.sh run <fid> <tag> <stage...>    push config, start the stages on the server (returns at once)
#   study.sh final <fid> <tag> <stage>     same, but reads the HOLDOUT (once per study -- it is ledgered)
#   study.sh exec <fid> <tag> <script.py>  run studies/<fid>/<script.py> on the server (returns at once)
#   study.sh wait <fid> <tag> [seconds]    wait (default 540 s) for that job; on completion pull + print the digest
#   study.sh digest <fid> <tag> [base_id]  re-print the digest of a finished run
… (63 行略) …
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

10-04 00:04 · 读 `/Users/wxy/Desktop/Partura/studies/F103_amt_dw_decay/audit_1.py`

**10-04 00:05 · Bash** — Read the study_tools API

```bash
cd /Users/wxy/Desktop/Partura && ls partura/ && wc -l partura/study_tools.py partura/books.py 2>/dev/null; sed -n 1,200p partura/study_tools.py
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

**10-04 00:05 · Bash** — Read books.py helper functions

```bash
cd /Users/wxy/Desktop/Partura && cat partura/books.py
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

… (125 行略) …
    with np.errstate(invalid="ignore", divide="ignore"):
        q = np.floor(pos / np.maximum(cnt, 1)[:, None] * n)
    q = np.where(ok, q, np.nan)
    r = np.where(ok, t, 0.0)
    ew = np.where(cnt > 0, r.sum(1) / np.maximum(cnt, 1), np.nan)
    rows = []
    for k in range(n):
        sel = (q == k)
        m = sel.sum(1)
        with np.errstate(invalid="ignore", divide="ignore"):
            ex = np.where(m > 0, (r * sel).sum(1) / np.maximum(m, 1) - ew, np.nan)
        f = ex[np.isfinite(ex)]
        rows.append({"quantile": k + 1, "excess_ann": float(f.mean() * 252) if f.size else float("nan"),
                     "sharpe": float(f.mean() / f.std() * np.sqrt(252)) if f.size > 2 and f.std() > 0 else float("nan"),
                     "win": float((f > 0).mean()) if f.size else float("nan")})
    return rows


__all__ = ["HALFLIVES", "TOP_FRAC", "COST", "stats", "long_book", "short_leg_excess", "smoothed",
           "fit_halflives", "book_row", "books", "quantile_profile"]
```

**10-04 00:05 · Bash** — List report headings and check server status

```bash
cd /Users/wxy/Desktop/Partura && grep -n '^#' research/alpha_distillation/F103_amt_dw_decay.md | head -80 && ./scripts/study.sh status
```

```
1:# Alpha 研究报告 — F103_amt_dw_decay
11:## 1. 原始表达式
32:## 2. 算子的真实语义
36:### `day_close`
46:### `cross_decay_linear`
55:### `day_durbin_watson`
65:### `pow_3`
73:### `ts_min`
82:### `mul`
90:### `cross_max`
121:### 既往研究留下的先验
155:## 3. 数学分解
200:## 4. 结构语法
220:## 5. 竞争性假设
261:## 6. 基线指标
356:## 7. 消融实验
358:### S0_baseline
374:### S1_structure
450:### S2_distil
529:### S_final
570:### 中性化(fit 段)
670:### 条件 IC(fit 段)
693:### 控制变量自己当因子(同口径)
1014:## 8. 语义变体
1086:## 9. 机制诊断
1091:### 已确立(每条后面是实验)
1115:### 合理但没坐实
1124:### 未决
1132:### 假设的判决
1155:## 10. 蒸馏 / 升华后的候选
1168:### 读留出段之前定下的候选(只凭 train / valid;这一段写于 `study.sh final` 之前,之后没有改过)
1209:### 读完留出段之后(上面那段没有再动;留出段只读了这一次)
1256:## 11. 失效模式与风险
1276:## 12. 下一步实验
1289:## 附录 A — 数据段使用台账
1301:## 附录 B — 复现
1304:# S0_baseline: 193.7s, 峰值 anon 3.04 GiB, stages ['S0_baseline']
1305:# S1_structure: 355.3s, 峰值 anon 4.08 GiB, stages ['S1_structure']
1306:# S2_distil: 496.2s, 峰值 anon 4.16 GiB, stages ['S2_distil']
1307:# final: 184.0s, 峰值 anon 2.61 GiB, stages ['S_final']

540353, 30176 MiB
container anon 26.2 GiB
gpu.lock slot0.lock slot1.lock slot2.lock
```

**10-04 00:05 · Bash** — Find how the report maps note files to sections

```bash
cd /Users/wxy/Desktop/Partura && grep -n "notes\|07_\|07x\|note(" partura/report.py | head -80
```

```
7:experiments) come from markdown fragments under ``notes/<factor_id>/``.
183:def build(config_path: str, out_root: Optional[str] = None, notes_dir: Optional[str] = None,
194:        return legacy_build(config_path, out_root=out_root, notes_dir=notes_dir, research_dir=research_dir)
202:    notes = Path(notes_dir or (PARTURA_ROOT / "notes")) / fid
209:    def note(name: str) -> str:
210:        p = notes / f"{name}.md"
231:    L += [f"## {SECTIONS[0]}", "", "```", cfg["expression"], "```", "", note("01_expression"), ""]
244:    L += [note("02_operators"), ""]
245:    L += [f"## {SECTIONS[2]}", "", dec.render_markdown(), "", note("03_decomposition"), ""]
246:    L += [f"## {SECTIONS[3]}", "", note("04_grammar"), ""]
247:    L += [f"## {SECTIONS[4]}", "", note("05_hypotheses"), ""]
277:    L += [note("06_baseline"), ""]
286:        L += [note(f"07_{sid}"), ""]
304:        L += ["", note("07_neutralise"), ""]
310:        L += ["", note("07_conditional"), ""]
320:        L += ["", note("07_controls"), ""]
321:    for extra in sorted(notes.glob("07x_*.md")) if notes.is_dir() else []:     # bespoke analyses of this study
332:    L += [note("08_variants"), ""]
334:    L += [f"## {SECTIONS[8]}", "", note("09_diagnosis"), ""]
339:    L += [note("10_distilled"), ""]
340:    L += [f"## {SECTIONS[10]}", "", note("11_risks"), ""]
341:    L += [f"## {SECTIONS[11]}", "", note("12_next"), ""]
```

**10-04 00:05 · Bash** — Read the report build function

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

**10-04 00:06 · Bash** — Extract neutralisation numbers from run JSONs

```bash
cd /Users/wxy/Desktop/Partura && python3 - <<'EOF'
import json
for tag in ('S0_baseline','S1_structure','S2_distil'):
    d=json.load(open(f'runs/F103_amt_dw_decay/{tag}.json'))
    ne=d['diagnostics'].get('neutralise')
    if not isinstance(ne,dict): print(tag,'no neutralise'); continue
    for vid,entry in ne.items():
        for ctl,rec in entry.items():
            if ctl in ('_traded_signal','all_controls','ctl_amt','ctl_cap'):
                print(tag,vid,ctl,'r2',rec.get('r2'),'r2raw',rec.get('r2_raw_panel'),'ric',round(rec['rank_ic'],4),'gross_shr',round(rec.get('ls_gross_sharpe',float('nan')),2),'Lgross',round(rec['long_gross_ann']*100,1),'Sgross',round(rec.get('short_gross_ann',float('nan'))*100,1))
EOF
```

```
S0_baseline v_base _traded_signal r2 0.0 r2raw None ric 0.0358 gross_shr 5.36 Lgross 13.5 Sgross 42.8
S0_baseline v_base all_controls r2 0.22748648319693301 r2raw 0.22997237548538477 ric 0.0172 gross_shr 2.83 Lgross 11.4 Sgross 9.1
S0_baseline v_base ctl_amt r2 0.08059927609391876 r2raw None ric 0.0253 gross_shr 3.51 Lgross 12.9 Sgross 21.6
S0_baseline v_base ctl_cap r2 0.03364082091640966 r2raw None ric 0.0356 gross_shr 5.34 Lgross 12.4 Sgross 42.2
S1_structure a_C _traded_signal r2 0.0 r2raw None ric 0.0045 gross_shr 2.41 Lgross 8.7 Sgross 26.9
S1_structure a_C all_controls r2 0.4595787321641666 r2raw 0.45746212337650216 ric 0.0162 gross_shr 5.47 Lgross 8.2 Sgross 35.1
S1_structure a_C ctl_amt r2 0.2965624813768896 r2raw None ric 0.0247 gross_shr 4.54 Lgross 7.1 Sgross 46.6
S1_structure a_C ctl_cap r2 0.1486386828627463 r2raw None ric 0.0042 gross_shr 2.35 Lgross 7.7 Sgross 26.0
S1_structure a_A5 _traded_signal r2 0.0 r2raw None ric 0.0392 gross_shr 2.39 Lgross 12.9 Sgross 25.9
S1_structure a_A5 all_controls r2 0.8074270181152879 r2raw 0.7793263685463668 ric 0.0123 gross_shr 1.87 Lgross -1.5 Sgross 12.7
S1_structure a_A5 ctl_amt r2 0.7475629332413237 r2raw None ric 0.0101 gross_shr 1.93 Lgross -0.7 Sgross 16.4
S1_structure a_A5 ctl_cap r2 0.25901954869048094 r2raw None ric 0.0452 gross_shr 2.66 Lgross 5.5 Sgross 42.6
S2_distil d_sum_k2 _traded_signal r2 0.0 r2raw None ric 0.0404 gross_shr 3.75 Lgross 14.9 Sgross 38.0
S2_distil d_sum_k2 all_controls r2 0.5544908169578296 r2raw 0.6390696307758089 ric 0.0123 gross_shr 1.81 Lgross 8.2 Sgross 4.2
S2_distil d_sum_k2 ctl_amt r2 0.4620975840576621 r2raw None ric 0.0182 gross_shr 2.26 Lgross 9.9 Sgross 8.5
S2_distil d_sum_k2 ctl_cap r2 0.16307049462902776 r2raw None ric 0.0427 gross_shr 3.8 Lgross 9.0 Sgross 42.4
S2_distil x_std9_k1 _traded_signal r2 0.0 r2raw None ric 0.0472 gross_shr 4.03 Lgross 17.5 Sgross 42.9
S2_distil x_std9_k1 all_controls r2 0.6455795274761202 r2raw 0.6426926825602824 ric 0.017 gross_shr 3.37 Lgross 12.3 Sgross 10.9
S2_distil x_std9_k1 ctl_amt r2 0.5440713566169064 r2raw None ric 0.0263 gross_shr 3.66 Lgross 12.4 Sgross 14.8
S2_distil x_std9_k1 ctl_cap r2 0.183361244990204 r2raw None ric 0.0506 gross_shr 4.06 Lgross 10.1 Sgross 49.7
S2_distil e_peak_k2 _traded_signal r2 0.0 r2raw None ric 0.0473 gross_shr 3.52 Lgross 17.4 Sgross 40.6
S2_distil e_peak_k2 all_controls r2 0.7240146037326453 r2raw 0.7968448897440935 ric 0.0142 gross_shr 2.07 Lgross 9.5 Sgross 3.5
S2_distil e_peak_k2 ctl_amt r2 0.6068285052124051 r2raw None ric 0.0265 gross_shr 2.72 Lgross 11.4 Sgross 11.3
S2_distil e_peak_k2 ctl_cap r2 0.13765883940665358 r2raw None ric 0.0495 gross_shr 3.39 Lgross 11.3 Sgross 43.8
S2_distil b_stdamt9 _traded_signal r2 0.0 r2raw None ric 0.0484 gross_shr 3.24 Lgross 16.9 Sgross 37.7
S2_distil b_stdamt9 all_controls r2 0.8335422737682812 r2raw 0.8335422737682812 ric 0.0193 gross_shr 5.03 Lgross 10.2 Sgross 17.2
S2_distil b_stdamt9 ctl_amt r2 0.7901074276491784 r2raw None ric 0.027 gross_shr 4.93 Lgross 11.8 Sgross 20.7
S2_distil b_stdamt9 ctl_cap r2 0.2536778351279166 r2raw None ric 0.0543 gross_shr 3.47 Lgross 7.9 Sgross 53.3
```

**10-04 00:06 · Bash** — Compute return and volatility decomposition from already-read final.json

```bash
cd /Users/wxy/Desktop/Partura && python3 - <<'EOF'
import json
d=json.load(open('runs/F103_amt_dw_decay/final.json'))
r=d['results']
for k in r:
    bu=r[k]['books_user']
    for which in ('splits','splits_at_hl_long'):
        if which not in bu: continue
        for sp in ('utrain','holdout'):
            s=bu[which][sp]
            vol=s['ls_ann']/s['ls_sharpe']
            lvol=s['long_ann']/s['long_sharpe']
            print(f"{k:10s} {which:18s} {sp:8s} ls_ann {s['ls_ann']*100:+6.2f}% vol {vol*100:5.2f}% shr {s['ls_sharpe']:+.2f} | L net {s['long_ann']*100:+6.2f}% Lvol {lvol*100:5.2f}% Lshr {s['long_sharpe']:+.2f} mdd {s['long_mdd']*100:+.1f}% | ls_mdd {s['ls_mdd']*100:+.1f}%")
# by year
by=d['diagnostics']['by_year']
for k,rows in by.items():
    print(k, ' '.join(f"{x['year']}:{x['ls_sharpe']:+.2f}|{x['long_ann']*100:+.1f}%" for x in rows))
EOF
```

```
f_orig     splits             utrain   ls_ann +19.37% vol  5.48% shr +3.53 | L net  +5.57% Lvol  5.03% Lshr +1.11 mdd -9.1% | ls_mdd -5.6%
f_orig     splits             holdout  ls_ann +18.31% vol  5.76% shr +3.18 | L net  +5.47% Lvol  5.23% Lshr +1.04 mdd -7.1% | ls_mdd -3.6%
f_orig     splits_at_hl_long  utrain   ls_ann +17.52% vol  5.16% shr +3.39 | L net  +8.05% Lvol  5.41% Lshr +1.49 mdd -7.7% | ls_mdd -4.5%
f_orig     splits_at_hl_long  holdout  ls_ann +15.71% vol  5.38% shr +2.92 | L net  +7.17% Lvol  5.69% Lshr +1.26 mdd -6.9% | ls_mdd -3.0%
f_sum_k3   splits             utrain   ls_ann +21.28% vol  5.85% shr +3.64 | L net  +8.43% Lvol  5.09% Lshr +1.66 mdd -7.2% | ls_mdd -4.2%
f_sum_k3   splits             holdout  ls_ann +21.08% vol  5.99% shr +3.52 | L net  +9.23% Lvol  5.23% Lshr +1.77 mdd -5.1% | ls_mdd -3.2%
f_sum_k3   splits_at_hl_long  utrain   ls_ann +19.69% vol  5.43% shr +3.63 | L net +10.09% Lvol  5.01% Lshr +2.02 mdd -5.9% | ls_mdd -4.9%
f_sum_k3   splits_at_hl_long  holdout  ls_ann +18.80% vol  5.64% shr +3.33 | L net +10.65% Lvol  5.36% Lshr +1.99 mdd -5.4% | ls_mdd -3.6%
f_sum_k2   splits             utrain   ls_ann +23.69% vol  6.87% shr +3.45 | L net +12.30% Lvol  5.64% Lshr +2.18 mdd -6.9% | ls_mdd -7.0%
f_sum_k2   splits             holdout  ls_ann +22.46% vol  7.25% shr +3.10 | L net +12.64% Lvol  6.11% Lshr +2.07 mdd -5.2% | ls_mdd -3.8%
f_sum_k2   splits_at_hl_long  utrain   ls_ann +21.15% vol  6.54% shr +3.23 | L net +13.39% Lvol  5.67% Lshr +2.36 mdd -5.9% | ls_mdd -6.3%
f_sum_k2   splits_at_hl_long  holdout  ls_ann +19.96% vol  6.94% shr +2.88 | L net +13.54% Lvol  6.06% Lshr +2.23 mdd -5.1% | ls_mdd -4.2%
f_std9_k1  splits             utrain   ls_ann +25.90% vol  7.23% shr +3.58 | L net +13.29% Lvol  5.84% Lshr +2.27 mdd -8.6% | ls_mdd -8.9%
f_std9_k1  splits             holdout  ls_ann +25.72% vol  8.19% shr +3.14 | L net +11.64% Lvol  7.53% Lshr +1.55 mdd -9.2% | ls_mdd -5.2%
f_std9_k1  splits_at_hl_long  utrain   ls_ann +22.78% vol  7.12% shr +3.20 | L net +15.59% Lvol  5.98% Lshr +2.61 mdd -6.7% | ls_mdd -7.6%
f_std9_k1  splits_at_hl_long  holdout  ls_ann +21.68% vol  7.89% shr +2.75 | L net +14.16% Lvol  7.36% Lshr +1.92 mdd -8.4% | ls_mdd -4.8%
f_stdamt9  splits             utrain   ls_ann +23.66% vol  8.04% shr +2.94 | L net +11.90% Lvol  6.55% Lshr +1.82 mdd -10.7% | ls_mdd -10.4%
f_stdamt9  splits             holdout  ls_ann +24.53% vol  9.62% shr +2.55 | L net  +8.19% Lvol  9.20% Lshr +0.89 mdd -15.4% | ls_mdd -10.7%
f_stdamt9  splits_at_hl_long  utrain   ls_ann +21.37% vol  8.04% shr +2.66 | L net +16.13% Lvol  6.69% Lshr +2.41 mdd -9.6% | ls_mdd -10.7%
f_stdamt9  splits_at_hl_long  holdout  ls_ann +21.04% vol  9.56% shr +2.20 | L net +13.23% Lvol  9.44% Lshr +1.40 mdd -15.8% | ls_mdd -10.3%
f_orig 2018:+5.43|+1.9% 2019:+6.22|+15.2% 2020:+4.19|+11.6% 2021:+1.78|-3.9% 2022:+2.87|+6.5% 2023:+2.05|+2.7% 2024:+2.86|+0.3% 2025:+3.34|+9.1%
f_sum_k3 2018:+4.73|+5.8% 2019:+4.95|+15.3% 2020:+4.27|+11.4% 2021:+2.37|+2.4% 2022:+3.90|+10.3% 2023:+2.64|+5.9% 2024:+3.59|+7.4% 2025:+3.08|+10.0%
f_sum_k2 2018:+4.89|+14.3% 2019:+4.29|+14.0% 2020:+2.26|+6.1% 2021:+2.68|+10.7% 2022:+4.86|+16.5% 2023:+3.44|+14.4% 2024:+2.89|+9.5% 2025:+2.60|+12.9%
f_std9_k1 2018:+5.67|+19.8% 2019:+4.55|+13.6% 2020:+2.08|+4.6% 2021:+2.22|+7.6% 2022:+5.34|+19.8% 2023:+3.75|+15.4% 2024:+3.01|+8.1% 2025:+2.72|+12.7%
f_stdamt9 2018:+4.02|+18.5% 2019:+3.32|+9.7% 2020:+1.20|-0.2% 2021:+2.07|+8.7% 2022:+5.41|+20.5% 2023:+4.01|+17.0% 2024:+2.21|+3.0% 2025:+2.11|+8.4%
```

**10-04 00:08 · 写文件** `/Users/wxy/Desktop/Partura/studies/F103_amt_dw_decay/rev1_matched.py`(14015 字符)

**10-04 00:08 · 改文件** `/Users/wxy/Desktop/Partura/studies/F103_amt_dw_decay/rev1_matched.py`

```
-           f"sign(train): " + "  ".join(f"{k} {st.sign(np.concatenate([v, np.full((P['G'].shape[0] - cut, v.shape[1]), np.nan)])):+.0f}"
                                       for k, v in V.items()), flush=True)
+           f"sign(train): " + "  ".join(f"{k} {st.sign(v):+.0f}" for k, v in V.items()), flush=True)
```

**10-04 00:08 · Bash** — Syntax-check the rev1 script and inspect sign_from

```bash
cd /Users/wxy/Desktop/Partura && ~/.venvs/alphacube/bin/python -m py_compile studies/F103_amt_dw_decay/rev1_matched.py && echo compiled OK && grep -n "def sign_from" -A12 partura/diagnose.py | head -30
```

```
compiled OK
105:def sign_from(panel: np.ndarray, target: np.ndarray, use: str = "rank_ic",
106-              target_ranks: Optional[np.ndarray] = None) -> float:
107-    s = (rank_ic_series(panel, target, target_ranks=target_ranks) if use == "rank_ic"
108-         else ic_series(panel, target))
109-    m = nanmean_quiet(s)
110-    return -1.0 if (np.isfinite(m) and m < 0) else 1.0
111-
112-
113-def ic_row(panel: np.ndarray, target: np.ndarray, *, sign: float = 1.0,
114-           target_ranks: Optional[np.ndarray] = None) -> Dict[str, float]:
115-    """Prediction metrics only (no book): what a stage needs for every variant
116-    when the money side is reported by ``partura.books``."""
117-    raw = np.asarray(panel, dtype=np.float64)
```

**10-04 00:08 · Bash** — Launch the rev1 supplementary analysis on the server

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh exec F103_amt_dw_decay rev1 rev1_matched.py && sleep 5 && ./scripts/study.sh status
```

```
started F103_amt_dw_decay/rev1: rev1_matched.py
	559534.pt_F103_rev1	(10/04/26 15:08:49)	(Detached)

540353, 30176 MiB
container anon 23.9 GiB
gpu.lock slot0.lock slot1.lock slot2.lock
```

**10-04 00:09 · Bash** — Read generated report header, final table and S_final section

```bash
cd /Users/wxy/Desktop/Partura && sed -n 1155,1168p research/alpha_distillation/F103_amt_dw_decay.md && sed -n 1,31p research/alpha_distillation/F103_amt_dw_decay.md && sed -n 529,570p research/alpha_distillation/F103_amt_dw_decay.md
```

```
## 10. 蒸馏 / 升华后的候选

**最终对比,与用户表同口径**(留出段 = 用户的测试段)

| 结构 | 方向 | 半衰期 | 扣费多空夏普 训练/测试 | 多头腿毛超额 训练/测试 | 多头腿净超额 训练/测试 | 纯多头夏普 训练/测试 | 空头腿毛超额 训练/测试 | 多头占比(训练) | 多空日换手 |
|---|---|---|---|---|---|---|---|---|---|
| _用户表里公布的原式_ | − | 2 | +3.53 / +3.18 | +12.8% / +12.4% | — | — | — | — | — |
| `f_orig` `cross_max(mul(day_close(Amt), ts_min(pow_3(day_durbin_wat...` | − | 2 | **+3.53 / +3.18** | +12.8% / +12.4% | +5.6% / +5.5% | +1.11 / +1.04 | +38.7% / +36.6% | 24.8% | 8.4% |
| `f_sum_k3` `mul(day_sum(Amt), pow_3(day_durbin_watson(cross_decay_lin...` | − | 10 | **+3.64 / +3.52** | +11.8% / +12.3% | +8.4% / +9.2% | +1.66 / +1.77 | +36.6% / +35.4% | 24.3% | 3.9% |
| `f_sum_k2` `mul(day_sum(Amt), pow_2(day_durbin_watson(cross_decay_lin...` | − | 10 | **+3.45 / +3.10** | +15.7% / +15.6% | +12.3% / +12.6% | +2.18 / +2.07 | +37.5% / +34.6% | 29.6% | 3.9% |
| `f_std9_k1` `mul(cross_max(day_std(Amt), 9), day_durbin_watson(cross_d...` | − | 2 | **+3.58 / +3.14** | +19.1% / +16.9% | +13.3% / +11.6% | +2.27 / +1.55 | +43.1% / +44.1% | 30.7% | 6.9% |
| `f_stdamt9` `cross_max(day_std(Amt), 9)` | − | 0 | **+2.94 / +2.55** | +19.2% / +15.2% | +11.9% / +8.2% | +1.82 / +0.89 | +40.7% / +46.0% | 32.0% | 8.3% |

### 读留出段之前定下的候选(只凭 train / valid;这一段写于 `study.sh final` 之前,之后没有改过)
# Alpha 研究报告 — F103_amt_dw_decay

> 收盘集合竞价成交额 × (30 日平均日内成交曲线的粗糙度)³,套 5 日极值记忆

**数据**: 1942 个交易日 × 5220 只股票 (20180102–20251231) · 标签 `open_vwap15` h=1(可买入:剔除次日开盘封涨停) · 成本 15 bp/单位换手 · 前/后 10% · AlphaCube `1698296` · Partura `36543cfd8cc8`

**数据段**: train 20180102–20211231 · valid 20220104–20230807 · utrain 20180102–20230807 · holdout 20230808–20251231 · full 20180102–20251231

> 决策用的数字:方向与 EMA 半衰期在 **train** 上定,在 valid 上确认。与用户表可比的数字:方向与半衰期在 **utrain**(用户的训练段)上定;holdout = 用户的测试段,只在最后读。

## 1. 原始表达式

```
cross_max(mul(day_close(Amt), ts_min(pow_3(day_durbin_watson(cross_decay_linear(Amt, 30))), 1)), 5)
```

… (37 行略) …
**问题**:样本外(用户的测试段 2023-08-08 ~ 2025-12-31):删节点、改配比、换水平腿,这三步各自还成立吗?这棵树在留出段上有没有给已知家族加东西?

上表是决策口径(train / valid),与 S2 里同一棵树的行逐位相同(`f_sum_k3` = `d_sum_k3`,`f_sum_k2` = `d_sum_k2`,`f_std9_k1` = `x_std9_k1`,`f_stdamt9` = `b_stdamt9`)。
**留出段的数字在第 10 节那张"与用户表同口径"的表里**,判读也在那里。这里只记这次运行另外给出的逐年表(方向 / 半衰期在 utrain 上定;每格是 扣费多空夏普 | 多头腿净超额;2023 是全年,跨了 utrain 和留出段):

| | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|
| `f_orig` | +5.43 \| +1.9% | +6.22 \| +15.2% | +4.19 \| +11.6% | +1.78 \| −3.9% | +2.87 \| +6.5% | +2.05 \| +2.7% | +2.86 \| +0.3% | +3.34 \| +9.1% |
| `f_sum_k3` | +4.73 \| +5.8% | +4.95 \| +15.3% | +4.27 \| +11.4% | +2.37 \| +2.4% | +3.90 \| +10.3% | +2.64 \| +5.9% | +3.59 \| +7.4% | +3.08 \| +10.0% |
| `f_sum_k2` | +4.89 \| +14.3% | +4.29 \| +14.0% | +2.26 \| +6.1% | +2.68 \| +10.7% | +4.86 \| +16.5% | +3.44 \| +14.4% | +2.89 \| +9.5% | +2.60 \| +12.9% |
| `f_std9_k1` | +5.67 \| +19.8% | +4.55 \| +13.6% | +2.08 \| +4.6% | +2.22 \| +7.6% | +5.34 \| +19.8% | +3.75 \| +15.4% | +3.01 \| +8.1% | +2.72 \| +12.7% |
| `f_stdamt9` | +4.02 \| +18.5% | +3.32 \| +9.7% | +1.20 \| −0.2% | +2.07 \| +8.7% | +5.41 \| +20.5% | +4.01 \| +17.0% | +2.21 \| +3.0% | +2.11 \| +8.4% |

两条腿的轮动在留出段里继续:2024–2025 年成交额水平那条腿(`f_stdamt9`)回落到 +2.2 / +2.1,而集中度占比最高的两个(`f_orig`、`f_sum_k3`)是 +2.9 / +3.3 和 +3.6 / +3.1。
`f_sum_k2` 是五个里唯一一个八年里每一年多空夏普都在 +2.2 以上、多头腿净超额都在 +6% 以上的。

五个候选彼此的 rank 相关(train):`f_orig`–`f_sum_k3` 0.86,`f_sum_k3`–`f_sum_k2` 0.93,`f_sum_k2`–`f_std9_k1` 0.86,`f_std9_k1`–`f_stdamt9` 0.93,`f_orig`–`f_stdamt9` 0.41 ——
它们排成一条从"集中度为主"到"成交额水平为主"的链,相邻两个接近同族,两端是两个东西。

### 中性化(fit 段)
```

**10-04 00:09 · Bash** — Wait for the rev1 job to finish

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh wait F103_amt_dw_decay rev1 2>&1 | tail -5
```

```
C 最低组 - 这批票平均                         +17.4    -12.4     +1.4    +27.9    +32.3     +7.8     -5.6    -23.7
组内 rank IC                          -0.0311  +0.0124  -0.0236  -0.0495  -0.0443  -0.0068  +0.0051  +0.0247
   (t)                                 -6.9     +2.1     -2.6     -5.7     -5.8     -0.7     +0.7     +2.6
[rev1] done 220s
[partura exit 0 2026-10-04_15:12:33]
```

**10-04 00:12 · Bash** — Read the full rev1 log

```bash
cd /Users/wxy/Desktop/Partura && grep -av 'FutureWarning\|vmap(single_row)\|UserWarning' logs/F103_amt_dw_decay_rev1.log
```

```
[panels] GPU has 1.9 GiB free (< 6.0 needed to stay out of the neighbours' way): this run computes on the CPU with 256 MiB chunks
[rev1] panels ready 1s; rows 0..1359 (20180102..20230807); sign(train): orig -1  dsum*C^3 -1  dsum*C^2 -1  dsum*C^1 -1  dsum -1  std9*C -1  std9 -1

== A. 固定半衰期下的两本书(方向一律 -1)。每格 = 扣费多空夏普 | 多空净年化 | 多头腿毛超额 | 多头腿净超额 | 纯多头夏普 | 多头腿最大回撤 | 多空日换手 ==

orig:  按多空夏普选的半衰期 train 2 / utrain 2;  按纯多头夏普选 train 10 / utrain 10
   utrain 各半衰期 多空夏普: hl0 +2.79  hl1 +3.27  hl2 +3.53  hl3 +3.50  hl5 +3.47  hl10 +3.39  hl20 +3.22
   utrain 各半衰期 多头腿净超额: hl0 -2.7%  hl1 +2.5%  hl2 +5.6%  hl3 +6.6%  hl5 +7.3%  hl10 +8.1%  hl20 +7.6%
   utrain 各半衰期 纯多头夏普: hl0 -0.56  hl1 +0.51  hl2 +1.11  hl3 +1.29  hl5 +1.39  hl10 +1.49  hl20 +1.39
   hl0   train +3.38 | +18.4% | +11.6% |  -1.8% | -0.38 | -14.1% | 14.5%    valid +1.45 |  +8.5% |  +8.3% |  -5.0% | -0.99 |  -9.7% | 14.1%    utrain +2.79 | +15.6% | +10.7% |  -2.7% | -0.56 | -21.5% | 14.3%
   hl2   train +4.14 | +21.7% | +13.5% |  +6.3% | +1.30 |  -8.9% |  8.5%    valid +2.22 | +13.3% | +10.9% |  +3.6% | +0.66 |  -4.2% |  8.5%    utrain +3.53 | +19.4% | +12.8% |  +5.6% | +1.11 |  -9.1% |  8.4%
   hl5   train +4.13 | +20.7% | +12.7% |  +8.1% | +1.62 |  -7.0% |  5.5%    valid +2.15 | +13.1% |  +9.8% |  +5.0% | +0.86 |  -4.7% |  5.6%    utrain +3.47 | +18.5% | +11.9% |  +7.3% | +1.39 |  -7.0% |  5.5%
   hl10  train +4.09 | +19.5% | +12.4% |  +9.4% | +1.86 |  -7.7% |  3.6%    valid +2.07 | +12.5% |  +7.8% |  +4.5% | +0.73 |  -6.8% |  3.8%    utrain +3.39 | +17.5% | +11.1% |  +8.1% | +1.49 |  -7.7% |  3.6%
   hl20  train +3.95 | +18.0% | +11.4% |  +9.5% | +1.86 |  -6.5% |  2.3%    valid +1.79 | +10.2% |  +5.0% |  +2.9% | +0.46 |  -8.9% |  2.4%    utrain +3.22 | +15.8% |  +9.6% |  +7.6% | +1.39 |  -8.9% |  2.3%

dsum*C^3:  按多空夏普选的半衰期 train 20 / utrain 10;  按纯多头夏普选 train 20 / utrain 20
   utrain 各半衰期 多空夏普: hl0 +1.48  hl1 +2.89  hl2 +3.34  hl3 +3.54  hl5 +3.62  hl10 +3.64  hl20 +3.63
   utrain 各半衰期 多头腿净超额: hl0 -14.8%  hl1 -2.6%  hl2 +2.3%  hl3 +4.9%  hl5 +6.6%  hl10 +8.4%  hl20 +10.1%
   utrain 各半衰期 纯多头夏普: hl0 -3.13  hl1 -0.54  hl2 +0.46  hl3 +0.98  hl5 +1.30  hl10 +1.66  hl20 +2.02
   hl0   train +1.75 | +11.4% |  +6.6% | -15.3% | -3.18 | -59.7% | 25.1%    valid +0.75 |  +4.6% |  +8.7% | -13.5% | -2.98 | -21.5% | 24.9%    utrain +1.48 |  +9.5% |  +7.2% | -14.8% | -3.13 | -80.3% | 25.1%
   hl2   train +3.56 | +22.6% | +10.2% |  +1.9% | +0.37 | -13.3% |  9.7%    valid +2.76 | +17.1% | +11.5% |  +3.2% | +0.66 |  -5.3% |  9.6%    utrain +3.34 | +21.1% | +10.6% |  +2.3% | +0.46 | -13.5% |  9.7%
   hl5   train +3.79 | +23.0% | +11.1% |  +6.0% | +1.19 |  -9.7% |  5.9%    valid +3.19 | +19.7% | +13.0% |  +7.9% | +1.55 |  -3.5% |  5.9%    utrain +3.62 | +22.1% | +11.6% |  +6.6% | +1.30 |  -9.7% |  5.9%
   hl10  train +3.92 | +22.6% | +12.2% |  +8.8% | +1.76 |  -7.2% |  3.9%    valid +2.96 | +17.9% | +10.8% |  +7.3% | +1.39 |  -4.0% |  3.9%    utrain +3.64 | +21.3% | +11.8% |  +8.4% | +1.66 |  -7.2% |  3.9%
   hl20  train +3.93 | +21.2% | +13.1% | +11.1% | +2.24 |  -5.9% |  2.4%    valid +2.88 | +15.8% |  +9.8% |  +7.5% | +1.45 |  -4.7% |  2.5%    utrain +3.63 | +19.7% | +12.2% | +10.1% | +2.02 |  -5.9% |  2.4%

dsum*C^2:  按多空夏普选的半衰期 train 10 / utrain 10;  按纯多头夏普选 train 20 / utrain 20
   utrain 各半衰期 多空夏普: hl0 +1.22  hl1 +2.58  hl2 +3.06  hl3 +3
… (641 字符略) …
0    +5.28    +3.78    +5.58    +2.60
   (t)                                 +9.7     +7.4     +7.8     +6.5     +3.5     +3.5     +6.8     +3.2
剔 已知两类                                +6.67    +5.85    +6.87    +8.31    +6.17    +5.30    +7.14    +3.67
   (t)                                 +9.2     +6.9     +6.2     +6.2     +3.4     +3.8     +6.6     +2.8
剔 已知两类 + C角落                          +7.11    +5.94    +7.43    +8.98    +6.56    +5.48    +7.31    +3.64
   (t)                                 +9.4     +6.6     +6.4     +6.5     +3.5     +3.6     +6.5     +2.4
增量:已知两类之后再剔 C角落                       +0.45    +0.09    +0.55    +0.67    +0.38    +0.18    +0.17    -0.04
   (t)                                 +4.8     +0.6     +3.5     +5.1     +1.9     +0.8     +0.9     -0.1
增量:C角落之后再剔 已知两类                       +3.98    +3.30    +3.83    +5.37    +3.33    +3.39    +3.95    +2.20
   (t)                                 +8.0     +5.6     +5.8     +5.9     +2.7     +3.2     +5.5     +2.2

D3. 干净的活跃票(成交额最高 1/5、不在已知两类里)内部按 C 再五分:最高 / 最低组相对这批票平均的次日超额(年化 %)与组内 rank IC
                                      train    valid     2018     2019     2020     2021     2022     2023
C 最高组 - 这批票平均                         -16.0    +10.0    -13.9    -28.1    -24.5     +2.7     +3.6    +20.7
C 最低组 - 这批票平均                         +17.4    -12.4     +1.4    +27.9    +32.3     +7.8     -5.6    -23.7
组内 rank IC                          -0.0311  +0.0124  -0.0236  -0.0495  -0.0443  -0.0068  +0.0051  +0.0247
   (t)                                 -6.9     +2.1     -2.6     -5.7     -5.8     -0.7     +0.7     +2.6
[rev1] done 220s
[partura exit 0 2026-10-04_15:12:33]
```

**10-04 00:15 · 写文件** `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07x_x4_audit.md`(5147 字符)

**10-04 00:16 · 写文件** `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07x_x5_rev1.md`(7918 字符)

**10-04 00:17 · 改文件** `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07x_x5_rev1.md`

```
- - **均值不稳定**:多空的均值增量 train 为正(+0.67),valid 为负(−0.30);多头腿的均值增量两段都为负。
+ - **均值不稳定**:多空的均值增量 train 为正(+0.67),valid 为负(−0.30);多头腿的均值增量在半衰期 2 下两段都为负(−0.19 / −0.73),半衰期 10 下是 +0.11 / −0.37。
```

**10-04 00:17 · 写文件** `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07_SA_audit.md`(339 字符)

**10-04 00:17 · 写文件** `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/01_expression.md`(1693 字符)

10-04 00:17 · 读 `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/01_expression.md`

10-04 00:17 · 读 `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/09_diagnosis.md`

10-04 00:17 · 读 `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/10_distilled.md`

10-04 00:17 · 读 `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/11_risks.md`

10-04 00:17 · 读 `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/12_next.md`

10-04 00:17 · 读 `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07_S1_structure.md`

10-04 00:17 · 读 `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07_S2_distil.md`

10-04 00:17 · 读 `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07_S_final.md`

10-04 00:17 · 读 `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07_neutralise.md`

10-04 00:17 · 读 `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/08_variants.md`

10-04 00:17 · 读 `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07x_x2_interaction.md`

10-04 00:17 · 读 `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07x_x3_family.md`

10-04 00:17 · 读 `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07x_x1_anatomy.md`

**10-04 00:17 · agent 的话**

Now writing the revised notes, starting with 01_expression.

**10-04 00:17 · 写文件** `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/01_expression.md`(1696 字符)

**10-04 00:17 · 改文件** `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07_S1_structure.md`

```
-    多头腿在两段上都更好(+9.5% / +7.4%),换手从 8.5% 降到 3.7%(选中的半衰期从 2 变成 10)。`A` 支要的是成交额水平,收盘那一根只是一个更抖的代理。
6. **`cross_max(·,5)` 不是机制(H7 成立)。** 删掉(`m_none`)或换成均值(`m_mean5`)在两段上都略好于原式,换手更低(7.0% / 6.5% 对 8.5%)。
   实验室里"恒正的水平量取极值只是低通"那条先验在这棵树上重新测了一次,成立。
+    表里多头腿净超额是 +9.5% / +7.4% 对原式的 +6.3% / +3.6%,换手 3.7% 对 8.5% —— **但这比的是半衰期 10 对半衰期 2**(`f_sum` 选中 10,原式选中 2)。
   (修订:同为半衰期 10 时原式是 +9.4% / +4.5%、换手 3.6%,所以"多头腿更好"在 train 上不存在,valid 上 +2.9 个点;换手下降全部来自半衰期。见 X4、X5。)
   `A` 支要的是成交额水平,收盘那一根只是一个更抖的代理 —— 这半句不受影响(多空夏普 valid +0.55、同半衰期下的多空配对差也为正)。
6. **`cross_max(·,5)` 不是机制(H7 成立)。** 删掉(`m_none`)或换成均值(`m_mean5`)在两段上都略好于原式,换手更低(7.0% / 6.5% 对 8.5%;这里的换手差也有半衰期的成分:`m_none` 选中 5,原式选中 2)。
   实验室里"恒正的水平量取极值只是低通"那条先验在这棵树上重新测了一次,成立。
   (修订:它"多余"的前提是下游有半衰期 ≥ 5 的 EMA。不平滑时 utrain 多空夏普 原式 +2.79、删掉 `cross_max` 的 `A·C³` 是 −1.45;半衰期 2 时 +3.53 对 +3.20。见 X4-A。)
```

**10-04 00:18 · 改文件** `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07_S2_distil.md`

```
-    多头腿净超额 +11.1% / +7.5%(原式 +6.3% / +3.6%),换手从 8.5% 降到 2.4%。多头腿的改善主要是成本:毛超额 +13.1% / +9.8% 与原式 +13.5% / +10.9% 相当。
+    多头腿净超额 +11.1% / +7.5%(原式 +6.3% / +3.6%),换手从 8.5% 降到 2.4%。多头腿的改善主要是成本:毛超额 +13.1% / +9.8% 与原式 +13.5% / +10.9% 相当。
   (修订:这里比的是半衰期 20 对半衰期 2,省下的成本是**半衰期**省的,不是删节点省的。同为半衰期 10 时:原式 +4.09 / +2.07、多头腿净 +9.4% / +4.5%、换手 3.6%;
   `d_sum_k3` +3.92 / +2.96、+8.8% / +7.3%、换手 3.9%。删节点在同半衰期下改善的是多空(日度配对差 +3.1% / +5.4% 每年,t +2.5 / +3.2),多头腿没有显著差别(−0.6% / +2.8%)。见 X4、X5。)
```

**10-04 00:18 · 改文件** `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07_S2_distil.md`

```
- 4. **水平腿换成 F001 的蒸馏结果,train 上有增量、valid 上持平。** `x_std9_k1` 相对 `b_stdamt9`:多空夏普 +0.85 / −0.08,纯多头夏普 +0.55 / +0.16;
   相对同指数的 `d_sum_k1`:+0.96 / +0.39。
+ 4. **水平腿换成 F001 的蒸馏结果,train 上有增量、valid 上持平。** `x_std9_k1` 相对 `b_stdamt9`:多空夏普 +0.85 / −0.08,纯多头夏普 +0.55 / +0.16;
   相对同指数的 `d_sum_k1`:+0.96 / +0.39。
   (修订:纯多头夏普的 +0.55 / +0.16 是半衰期 2 对半衰期 0 的差。同一个半衰期下,乘 `C` 之后多头腿净超额在每一档都不高于 `b_stdamt9` 自己 ——
   半衰期 2:−1.1% / −4.0% 每年(t −0.9 / −2.8);半衰期 10:+0.7% / −2.1%。`C` 给已知家族加的只有多空的均值(train +5.0%,valid −1.9%)和两段都在的波动降低(约一成)。见 X5-B、X5-C。)
```

**10-04 00:18 · 改文件** `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07_S_final.md`

```
- 两条腿的轮动在留出段里继续:2024–2025 年成交额水平那条腿(`f_stdamt9`)回落到 +2.2 / +2.1,而集中度占比最高的两个(`f_orig`、`f_sum_k3`)是 +2.9 / +3.3 和 +3.6 / +3.1。
`f_sum_k2` 是五个里唯一一个八年里每一年多空夏普都在 +2.2 以上、多头腿净超额都在 +6% 以上的。
+ 2024–2025 年成交额水平那条腿(`f_stdamt9`)的多空夏普回落到 +2.2 / +2.1,而集中度占比最高的两个(`f_orig`、`f_sum_k3`)是 +2.9 / +3.3 和 +3.6 / +3.1。
(修订:原文把这读成"两条腿的轮动在留出段里继续"。这个读法没有坐实:train / valid 上 `C` 的增量是 2018–2020 为正、2021–2023 为零或负的单调衰减(X4-E、X5-B),不是轮动;
留出段这两年的排序是一次观测,而且夏普差里大部分是波动而不是均值 —— 见第 10 节"留出段那 +0.59 是什么"。)
`f_sum_k2` 是五个里唯一一个八年里每一年多空夏普都在 +2.2 以上、多头腿净超额都在 +6% 以上的(其中 2024、2025 两年是读留出段之后才看到的,不能当成事前选它的理由)。
```

**10-04 00:18 · 改文件** `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07_neutralise.md`

```
-   **不在已知暴露里的那部分,各个版本差不多大**(train 上 rank IC 0.012~0.019),区别只在外面裹了多少成交额水平。
+   **不在已知暴露里的那部分,各个版本同一个量级**(train 上 rank IC 0.012~0.019),区别主要在外面裹了多少成交额水平。
  (修订:量级相同,但排序要说清楚 —— **`d_sum_k2` 的残差是各候选里最小的**:rank IC 0.0123、无成本多空夏普 +1.81;原式 0.0172 / +2.83,`x_std9_k1` 0.0170 / +3.37,`e_peak_k2` 0.0142 / +2.07,`b_stdamt9` 0.0193 / +5.03。
  已知家族基准 `b_stdamt9` 自己的残差反而最大。按"已知暴露之外还剩多少"排,原报告事后改选的 `d_sum_k2` 排在最后。)
```

**10-04 00:18 · 改文件** `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/08_variants.md`

```
- 同一个信号把半衰期从 2 调到 10,train 多头腿净超额能差 2~3 个点(原式 +6.3% → +9.4%,`x_std9_k1` +11.5% → +13.8%),而多空夏普几乎不动。S_final 的摘要里有固定半衰期的对照。
+ 同一个信号把半衰期从 2 调到 10,train 多头腿净超额能差 2~3 个点(原式 +6.3% → +9.4%,`x_std9_k1` +11.5% → +13.8%),而多空夏普几乎不动。
  **所以这张总表里的多头腿净超额不能跨行直接比**;七个关键版本在同一个半衰期下的对照在 X4-A 和 X5-A(修订时补的),结构上的结论以那两张表和日度配对差为准:
  同半衰期下,删节点改善的是多空不是多头腿;多头腿净超额最高的是不带 `C` 或只带一次方的成交额水平家族(`b_stdamt9`、`d_sum_k1`、`x_std9_k1`),带 `C²`、`C³` 的更低。
```

**10-04 00:18 · 改文件** `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07x_x2_interaction.md`

```
- (后记:这是 2021–2023 年上半年的事实;留出段(2023-08 起)里集中度占比高的版本多空夏普反而最高,这条腿没有死,是在轮动 —— 见 X3-C 和第 9、10 节。)
+ (后记:这是 2021–2023 年上半年的事实;留出段(2023-08 起)里集中度占比高的版本多空夏普反而最高。
修订:原后记据此写"这条腿没有死,是在轮动",证据不够 —— 留出段只有一次观测,而且那个夏普差大部分是波动降低而不是均值(第 10 节);train / valid 上看到的是单调衰减。这张表的原读法维持。
另外,"成交额最高 1/5 里 `C` 的条件 IC 仍是 −0.033 / −0.035"那个角落也不是 `C` 特有的:对换手率、波动、动量、涨停史等做组内残差后,2021–2023 年是 −0.011 / −0.002 / +0.018(X4-C)。)
```

**10-04 00:18 · 改文件** `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07x_x2_interaction.md`

```
- **多头端(左上/上方)在 train 上要"成交额低且不粗糙",在 valid 上要"成交额低且粗糙" —— 粗糙度对多头腿没有稳定的贡献,它是一个只在空头端有用的"避雷"变量。**
+ **多头端(左上/上方)在 train 上要"成交额低且不粗糙",在 valid 上要"成交额低且粗糙" —— 粗糙度对多头腿没有稳定的贡献,它是一个只在空头端有用的"避雷"变量。**
(修订:右下角"两段都稳定"这个事实成立,但它不是 `C` 特有的。同一行里把 `C` 换成换手率,最高组是 −74.9% / −94.6%;角落里 46% / 44% 是近 5 日涨停过的票,
剔掉换手率角落和近期涨停票之后,角落里剩下的票是 −23.8% / −2.1%。"避雷"的功能在 2021 年之后已经被换手率 / 涨停史覆盖 —— X4-C、X5-D。)
```

**10-04 00:18 · 改文件** `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07x_x3_family.md`

```
-   (后记:留出段上这个增量是 +0.59,见第 10 节 —— "只在 train 上"应读作"valid 上没有"。)
+   (后记:留出段上这个增量是 +0.59,见第 10 节 —— "只在 train 上"应读作"valid 上没有"。
  修订:这里的 +0.85 / −0.08 比的是半衰期 2 对半衰期 0;而且夏普差混着均值和波动。同半衰期的日度配对差:多空均值 train +5.0% / 年(t +4.0)、valid −1.9%;
  乘 `C` 之后波动两段都低一成,单这一项就给夏普 +0.3 上下。留出段的 +0.59 里 +0.44 是波动、+0.15 是均值。原读法"只在 train 上"对均值而言是对的。见 X5-B、X5-C。)
```

**10-04 00:18 · 改文件** `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07x_x3_family.md`

```
- **两条腿在时间上是互补的**:成交额水平在 2020 年几乎失效(+0.19),集中度在 2020 年最强(+4.94);2022–2023 年反过来。
+ **两条腿在时间上是互补的**:成交额水平在 2020 年几乎失效(+0.19),集中度在 2020 年最强(+4.94);2022–2023 年反过来。
(修订:"互补"在这六年里成立;但它不等于"轮动、会回来"。集中度在已知暴露之外的成分是 2018–2020 强、2021 减半、2022–2023 为零的单调衰减(下面的 D 节、X4-C、X5-D),这六年里只切换了一次。)
```

**10-04 00:18 · 改文件** `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07x_x3_family.md`

```
- - (后记:这一节的"2021 年起没有了"说的是 2021 年到 2023 年 8 月。留出段里集中度那条腿并没有继续失效 —— `f_std9_k1` 比 `f_stdamt9` 高 0.59 个多空夏普 —— 所以这是一段时期的事实,不是结构性的结论;见第 9、10 节。)
+ - (后记:这一节的"2021 年起没有了"说的是 2021 年到 2023 年 8 月。留出段里 `f_std9_k1` 比 `f_stdamt9` 高 0.59 个多空夏普。
  修订:原后记据此写"集中度那条腿并没有继续失效,所以这是一段时期的事实,不是结构性的结论"。这个推断撤回:那 +0.59 里 +0.44 来自波动降低(train / valid 上就有的效应)、只有 +0.15 来自均值(+1.2% / 年,不到 1 个标准误),
  留出段也没有量过成交额中性的集中度的 rank IC。本节的原读法 —— 已知家族之外的成分 2021 年起没有预测力 —— 没有被留出段推翻;它之后有没有恢复是未决,见第 9、10 节。)
```

**10-04 00:18 · 改文件** `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07_S1_structure.md`

```
- 收盘那一根只是一个更抖的代理 —— 这半句不受影响(多空夏普 valid +0.55、同半衰期下的多空配对差也为正)。
+ 收盘那一根只是一个更抖的代理 —— 这半句不受影响(多空夏普 valid +0.55;连同 `cross_max` 一起删掉的 `day_sum·C³` 在同半衰期下对原式的多空配对差也为正,X4-B)。
```

10-04 00:19 · 读 `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/09_diagnosis.md`

**10-04 00:20 · 写文件** `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/09_diagnosis.md`(8423 字符)

**10-04 00:21 · 改文件** `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/09_diagnosis.md`

```
- (+1.2% / 年,按 utrain 上配对差的波动折算不到 1 个标准误;两个夏普之差本身的标准误约 0.3~0.4,+0.59 约 1.5 个标准误)。
+ (+1.2% / 年,按 utrain 上配对差的波动折算不到 1 个标准误;审查的估计是两个夏普之差本身的标准误约 0.3~0.4,+0.59 约 1.5 个标准误)。
```

**10-04 00:21 · Bash** — Back up the original 10_distilled note to scratch

```bash
mkdir -p /private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad && cd /Users/wxy/Desktop/Partura && cp notes/F103_amt_dw_decay/10_distilled.md /private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/10_distilled.orig.md && sed -n 41,43p notes/F103_amt_dw_decay/10_distilled.md | cut -c1-80 && sed -n 85,87p notes/F103_amt_dw_decay/10_distilled.md | cut -c1-60
```

```
### 读完留出段之后(上面那段没有再动;留出段只读了这一次)


**勘误**(读之前那段里的一处不准确,保留原文
它相对 `d_sum_k2` 的多头腿净超额是 +2.2% / +1.0%,
```

**10-04 00:21 · 写文件** `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/10_head.md`(1270 字符)

**10-04 00:22 · 写文件** `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/10_tail.md`(8566 字符)

**10-04 00:22 · Bash** — Splice the revised 10_distilled note, keeping the pre-holdout body verbatim

```bash
cd /Users/wxy/Desktop/Partura && python3 - <<'EOF'
S='/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/'
orig=open(S+'10_distilled.orig.md',encoding='utf-8').read().split('\n')
i=[k for k,l in enumerate(orig) if l.startswith('### 读完留出段之后')][0]
pre=orig[:i]
old_hdr='### 读留出段之前定下的候选(只凭 train / valid;这一段写于 `study.sh final` 之前,之后没有改过)'
assert pre[0]==old_hdr, pre[0]
pre[0]='### 读留出段之前定下的候选(只凭 train / valid;原研究员自述写于 `study.sh final` 之前、之后没有改过 —— 见修订说明第 2 条;正文原样保留)'
head=open(S+'10_head.md',encoding='utf-8').read()
tail=open(S+'10_tail.md',encoding='utf-8').read()
new=head+'\n'.join(pre)+'\n'+tail
open('notes/F103_amt_dw_decay/10_distilled.md','w',encoding='utf-8').write(new)
# verify verbatim body
new_lines=new.split('\n')
j=[k for k,l in enumerate(new_lines) if l.startswith('### 读留出段之前定下的候选')][0]
assert new_lines[j+1:j+i]==orig[1:i]
print('pre-holdout body preserved verbatim:', i-1, 'lines; total', len(new_lines))
EOF
grep -n '^###\|^\*\*推荐\|^\*\*并排\|^\*\*纯提纯' notes/F103_amt_dw_decay/10_distilled.md | cut -c1-90
```

```
pre-holdout body preserved verbatim: 40 lines; total 170
1:### 修订说明(审查之后加的,先读这一段)
19:### 读留出段之前定下的候选(只凭 train / valid;原研究员自述写于 `st
60:### 读完留出段之后(留出段只读了这一次;本节在审查后重写,旧版�
137:### 推荐
139:**推荐(协议内):事前登记的首选 `f_std9_k1` = `mul(cross_max(day_std(Amt), 9
148:**并排:事后改选的 `f_sum_k2` = `mul(day_sum(Amt), pow_2(C))`(原报告的推荐
156:**纯提纯:`f_sum_k3` = `mul(day_sum(Amt), pow_3(C))`。** 这是"同一个因子少�
```

**10-04 00:23 · 写文件** `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/11_risks.md`(2491 字符)

**10-04 00:23 · 改文件** `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/11_risks.md`

```
- 最终结构两个参数(极值窗口 9、平均窗口 30),邻域(平均窗口 15 / 60、指数 1~2)是平台。
+ 最终结构两个参数(极值窗口 9、平均窗口 30):平均窗口 15 / 60、指数 1~2 的邻域是平台(S2);极值窗口 9 是沿用 F001 的,这次没有扫。
```

10-04 00:23 · 读 `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/12_next.md`

**10-04 00:23 · 写文件** `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/12_next.md`(1037 字符)

**10-04 00:23 · Bash** — Regenerate the F103 report and list its headings

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh report F103_amt_dw_decay 2>&1 | tail -5 && grep -n '^## \|^### ' research/alpha_distillation/F103_amt_dw_decay.md | sed -n 1,80p
```

```
wrote /root/autodl-tmp/Partura/research/alpha_distillation/F103_amt_dw_decay.md
    1669 research/alpha_distillation/F103_amt_dw_decay.md
11:## 1. 原始表达式
40:## 2. 算子的真实语义
44:### `day_close`
54:### `cross_decay_linear`
63:### `day_durbin_watson`
73:### `pow_3`
81:### `ts_min`
90:### `mul`
98:### `cross_max`
129:### 既往研究留下的先验
163:## 3. 数学分解
208:## 4. 结构语法
228:## 5. 竞争性假设
269:## 6. 基线指标
364:## 7. 消融实验
366:### S0_baseline
382:### S1_structure
461:### S2_distil
544:### S_final
587:### 中性化(fit 段)
689:### 条件 IC(fit 段)
712:### 控制变量自己当因子(同口径)
1042:### X4 — 审查员的反驳实验(`audit_1.py`,tag `audit1`)
1121:### X5 — 修订阶段的补充分析(`rev1_matched.py`,tag `rev1`)
1234:## 8. 语义变体
1308:## 9. 机制诊断
1315:### 已确立(每条后面是实验)
1359:### 合理但没坐实
1373:### 未决
1382:### 假设的判决
1405:## 10. 蒸馏 / 升华后的候选
1418:### 修订说明(审查之后加的,先读这一段)
1436:### 读留出段之前定下的候选(只凭 train / valid;原研究员自述写于 `study.sh final` 之前、之后没有改过 —— 见修订说明第 2 条;正文原样保留)
1477:### 读完留出段之后(留出段只读了这一次;本节在审查后重写,旧版的结论改了什么见开头的修订说明)
1554:### 推荐
1588:## 11. 失效模式与风险
1617:## 12. 下一步实验
1632:## 附录 A — 数据段使用台账
1644:## 附录 B — 复现
```

**10-04 00:24 · Bash** — Read report sections 1 and 6

```bash
cd /Users/wxy/Desktop/Partura && sed -n 1,40p research/alpha_distillation/F103_amt_dw_decay.md | cut -c1-600 && echo ------- && sed -n 269,330p research/alpha_distillation/F103_amt_dw_decay.md | cut -c1-400
```

```
# Alpha 研究报告 — F103_amt_dw_decay

> 收盘集合竞价成交额 × (30 日平均日内成交曲线的粗糙度)³,套 5 日极值记忆

**数据**: 1942 个交易日 × 5220 只股票 (20180102–20251231) · 标签 `open_vwap15` h=1(可买入:剔除次日开盘封涨停) · 成本 15 bp/单位换手 · 前/后 10% · AlphaCube `1698296` · Partura `36543cfd8cc8`

**数据段**: train 20180102–20211231 · valid 20220104–20230807 · utrain 20180102–20230807 · holdout 20230808–20251231 · full 20180102–20251231

> 决策用的数字:方向与 EMA 半衰期在 **train** 上定,在 valid 上确认。与用户表可比的数字:方向与半衰期在 **utrain**(用户的训练段)上定;holdout = 用户的测试段,只在最后读。

## 1. 原始表达式

```
cross_max(mul(day_close(Amt), ts_min(pow_3(day_durbin_watson(cross_decay_linear(Amt, 30))), 1)), 5)
```

**来历**:挖掘库 #820(GP 搜出来的)。用户表里公布的那一行:方向 −、半衰期 2,扣费多空夏普 训练 +3.53 / 测试 +3.18,多头腿年化毛超额 +12.8% / +12.4%。
Partura 自己求值复现了这一行(S0 复现训练段,S_final 复现测试段)。

**一句话**:它把「当天收盘集合竞价的成交额」乘上「这只股票最近 30 天**平均**日内成交额曲线的粗糙度」的三次方,再取 5 日最大值;
方向为负 —— **成交活跃、而且平均日内成交曲线粗糙 / 集中的股票,之后跑输**;钱主要在空头腿。

读完源码、做完拆解、再经过一轮审查修订之后的版本(证据见第 7~10 节;修订改了什么见第 10 节开头):

- **提纯成立。** 七个算子里三个可以删:`ts_min(·,1)` 是恒等;`cross_max(·,5)` 只是低通(前提是下游有半衰期 ≥ 5 的 EMA,不平滑时它有用);`day_close(Amt)`(收盘竞价那一根)换成全天成交额。
  删完是 `mul(day_sum(Amt), pow_3(C))`(5 个算子)。同一个半衰期(10)下,它的多空净收益比原式每年高 3.8 个点(utrain 配对 t +3.7,六年每年为正);
  留出段多空夏普 +3.52,原式 +3.18(原式也用半衰期 10 是 +2.92)。**多头腿在同半衰期下没有改善**(utrain +0.4 个点,t +0.3;留出段 +9.2% 对 +7.2%)。
- **原式的多头腿弱,有一部分只是半衰期选得太快。** 用户表里那一行按多空夏普选中半衰期 2(只比半衰期 10 高 0.14);原式自己换成半衰期 10,多头腿净超额就从 +5.6% / +5.5% 到 +8.1% / +7.2%(训练 / 测试),
  换手从 8.4% 降到 3.6%,代价是多空夏普 +3.53 / +3.18 → +3.39 / +2.92。原报告把这一步记成了"删节点降换手",不对。
- 剩下的骨架是 **成交额水平 × (30 日平均曲线的集中度)^k**。成交额水平是已知家族(F001)。集中度这一支在已知暴露之外的成分**只在 2018–2020 年(GP 的样本内)存在**,
… (53 行略) …
**逐年**

| 年份 | 天数 | 扣费多空夏普 | 多头腿毛超额 | 多头腿净超额 | 空头腿毛超额 | 多空日换手 |
|---|---|---|---|---|---|---|
| 2018 | 243 | +5.43 | +8.0% | +1.9% | +49.6% | 7.7% |
| 2019 | 244 | +6.22 | +22.6% | +15.2% | +48.5% | 8.7% |
| 2020 | 243 | +4.19 | +19.6% | +11.6% | +41.3% | 9.1% |
| 2021 | 243 | +1.78 | +3.7% | -3.9% | +31.7% | 8.8% |
| 2022 | 242 | +2.87 | +13.8% | +6.5% | +32.4% | 8.4% |
| 2023 | 144 | +1.17 | +6.1% | -1.5% | +21.9% | 8.8% |

**不同预测期的 rank IC(fit 段)**

| 变体 | h=1 | h=2 | h=3 | h=5 | h=10 | h=20 |
|---|---|---|---|---|---|---|
| `v_base` | +0.0393 | +0.0497 | +0.0551 | +0.0623 | +0.0726 | +0.0802 |
| `a_C` | +0.0051 | +0.0052 | +0.0050 | +0.0038 | +0.0005 | -0.0055 |
| `a_A5` | +0.0448 | +0.0573 | +0.0642 | +0.0741 | +0.0897 | +0.1045 |
| `d_sum_k2` | +0.0464 | +0.0586 | +0.0655 | +0.0737 | +0.0845 | +0.0953 |
| `x_std9_k1` | +0.0512 | +0.0648 | +0.0722 | +0.0818 | +0.0948 | +0.1062 |
```

**10-04 00:24 · 改文件** `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/01_expression.md`

```
-   这是三个非基准候选里唯一不带选择偏差的样本外数字。**原报告读完留出段之后
+   它是读留出段之前登记的推荐,这一行才是这次研究对"推荐"的干净的样本外判决。**原报告读完留出段之后
```

**10-04 00:24 · Bash** — Read report section 8 tables

```bash
cd /Users/wxy/Desktop/Partura && sed -n 1234,1310p research/alpha_distillation/F103_amt_dw_decay.md | cut -c1-330
```

```
## 8. 语义变体

| 变体 | 表达式 | 方向 | rank IC train/valid | 半衰期 | 扣费多空夏普 train/valid | 多头腿毛超额 train/valid | 多头腿净超额 train/valid | 多头占比 | 多空日换手 | 取值离散度 |
|---|---|---|---|---|---|---|---|---|---|---|
| `v_base` | `cross_max(mul(day_close(Amt), ts_min(pow_3(day_durbin_watson(cross_...` | − | +0.0393 / +0.0279 | 2 | **+4.14 / +2.22** | +13.5% / +10.9% | +6.3% / +3.6% | 23.9% | 8.5% | 1.00 |
| `a_no_tsmin` | `cross_max(mul(day_close(Amt), pow_3(day_durbin_watson(cross_decay_l...` | − | +0.0393 / +0.0279 | 2 | **+4.14 / +2.22** | +13.5% / +10.9% | +6.3% / +3.6% | 23.9% | 8.5% | 1.00 |
| `a_A5` | `cross_max(day_close(Amt), 5)` | − | +0.0448 / +0.0613 | 3 | **+1.81 / +3.69** | +12.9% / +23.5% | +7.1% / +18.0% | 33.2% | 6.3% | 1.00 |
| `a_C` | `day_durbin_watson(cross_decay_linear(Amt, 30))` | − | +0.0051 / -0.0322 | 1 | **+1.79 / -1.75** | +8.7% / -16.7% | +4.6% / -21.1% | 24.4% | 6.1% | 1.00 |
| `e_pow1` | `cross_max(mul(day_close(Amt), day_durbin_watson(cross_decay_linear(...` | − | +0.0477 / +0.0548 | 3 | **+2.70 / +3.63** | +12.4% / +21.0% | +5.8% / +14.3% | 24.9% | 7.4% | 1.00 |
| `e_pow2` | `cross_max(mul(day_close(Amt), pow_2(day_durbin_watson(cross_decay_l...` | − | +0.0449 / +0.0422 | 3 | **+3.60 / +3.12** | +13.3% / +16.4% | +6.6% / +9.6% | 24.7% | 7.7% | 1.00 |
| `m_none` | `mul(day_close(Amt), pow_3(day_durbin_watson(cross_decay_linear(Amt,...` | − | +0.0435 / +0.0317 | 5 | **+4.35 / +2.41** | +13.5% / +10.8% | +7.1% / +4.1% | 23.9% | 7.0% | 1.00 |
| `m_mean5` | `cross_mean(mul(day_close(Amt), pow_3(day_durbin_watson(cross_decay_...` | − | +0.0406 / +0.0299 | 3 | **+4.26 / +2.49** | +13.2% / +11.8% | +7.8% / +6.2% | 24.2% | 6.5% | 1.00 |
| `f_sum` | `cross_max(mul(day_sum(Amt), pow_3(day_durbin_watson(cross_decay_lin...` | − | +0.0417 / +0.0362 | 10 | **+3.79 / +2.77** | +12.5% / +10.6% | +9.5% / +7.4% | 26.4% | 3.7% | 1.00 |
| `f_share` | `cross_max(mul(div(day_close(Amt), day_sum(Amt)), pow_3(day_durbin_w...` | − | +0.0060 / -0.0293 | 3 | **+1.52 / -1.96** | +9.8% / -13.7% | +6.2% / -17.7% | 32.6% | 5.0% | 1.00 |
| `i_rankmul` | `cross_max(mul(cs_rank(day_close(Amt)), cs_rank(day_durbin_watson(cr...` | − | +0.0341 / +0.0103 | 0 | **+2.77 / -0.08** | +8.3% / -8.2% | +0.2% / -16.3% | 16.4% | 11.0% | 1.00 |
| `i_addrank` | `add(cs_rank(cross_max(day_close(Amt), 5)), cs_rank(day_durbin_watso...` | − | +0.0418 / +0.0239 | 2 | **+4.01 / +1.81** | +15.1% / +10.5% | +7.6% / +3.2% | 26.9% | 9.4% | 0.73 |
| `d_sum_k3` | `mul(day_sum(Amt), pow_3(day_durbin_watson(cross_decay_linear(Amt, 3...` | − | +0.0410 / +0.0336 | 20 | **+3.93 / +2.88** | +13.1% / +9.8% | +11.1% / +7.5% | 28.5% | 2.4% | 1.00 |
| `d_sum_k2` | `mul(day_sum(Amt), pow_2(day_durbin_watson(cross_decay_linear(Amt, 3...` | − | +0.0464 / +0.0491 | 10 | **+3.33 / +3.78** | +14.9% / +17.9% | +11.4% / +14.5% | 28.1% | 4.0% | 1.00 |
| `d_sum_k1` | `mul(day_sum(Amt), day_durbin_watson(cross_decay_linear(Amt, 30)))` | − | +0.0474 / +0.0604 | 10 | **+2.36 / +3.97** | +15.4% / +23.3% | +12.5% / +20.7% | 35.3% | 3.3% | 1.00 |
| `d_amt` | `day_sum(Amt)` | − | +0.0419 / +0.0646 | 5 | **+1.42 / +3.68** | +13.0% / +24.2% | +9.4% / +21.0% | 41.9% | 4.0% | 1.00 |
| `b_stdamt9` | `cross_max(day_std(Amt), 9)` | − | +0.0484 / +0.0671 | 0 | **+2.47 / +4.44** | +16.9% / +24.9% | +9.3% / +18.5% | 30.9% | 8.5% | 1.00 |
| `x_std9_k1` | `mul(cross
… (1749 字符略) …


- **同一个东西的不同写法(rank 相关 ≥ 0.95,或者就是同一棵树)**:`v_base` = `a_no_tsmin` = `f_orig`(1.00);`m_mean5`(0.98)、`e_pow2`(0.95)、`i_addrank`(0.95)与原式同族;
  `x_std9_k1_w15` / `x_std9_k1_w60` 与 `x_std9_k1`(0.98 / 0.99);`b_stdamt9` = `f_stdamt9` = 配置里的 `known_stdamt_max9`;`d_sum_k3` = `f_sum_k3`,`d_sum_k2` = `f_sum_k2`,`x_std9_k1` = `f_std9_k1`。
- **一条从"集中度为主"到"成交额水平为主"的轴**,用与 `ctl_amt` 的 rank 相关当坐标:`a_C` −0.54 ≈ `f_share` −0.53(两者相关 0.93)→ `i_rankmul` 0.04 → 原式 0.28 →
  `d_sum_k3` 0.47 → `x_std9_k2` 0.51 → `d_sum_k2` 0.74 ≈ `x_std9_k1` 0.75 → `e_peak_k2` 0.86 → `a_A5` 0.87 ≈ `b_stdamt9` 0.89 ≈ `g_stdB` 0.90 → `d_sum_k1` 0.94 → `d_amt` 1.00。
  **沿这条轴往右走,train 的多空夏普先升后降(峰在 0.3~0.5:原式 +4.14、`d_sum_k3` +3.93、`x_std9_k2` +4.16),valid 的多空夏普一路变好、到 0.75 以上持平在 +3.7~+4.4;往左到 0.04 附近 valid 已经不赚钱(`i_rankmul` −0.08),再往左是亏钱。**
  这张表里几乎所有的差别都能用"它在这条轴上的位置"解释;真正不在轴上的只有两件事:水平腿用 `day_std(Amt)` 的 9 日峰值还是 `day_sum(Amt)`(前者在不活跃的票里也有排序力),
  以及集中度用哪种写法(DW / 峰值占比 —— 两段上分不出高下)。
- **相邻的两个接近同族,两端是两个东西**:`d_sum_k3`–`d_sum_k2` 0.93,`d_sum_k2`–`d_sum_k1` 0.92,`x_std9_k1`–`b_stdamt9` 0.93,而原式–`b_stdamt9` 只有 0.41。
- **哪一列该信**:多头腿净超额和换手要和半衰期一起读 —— 原式和 `x_std9_*` 选中的半衰期是 0~2(换手 7%~10%),`d_sum_*` 是 10~20(换手 2%~4%);
  同一个信号把半衰期从 2 调到 10,train 多头腿净超额能差 2~3 个点(原式 +6.3% → +9.4%,`x_std9_k1` +11.5% → +13.8%),而多空夏普几乎不动。
  **所以这张总表里的多头腿净超额不能跨行直接比**;七个关键版本在同一个半衰期下的对照在 X4-A 和 X5-A(修订时补的),结构上的结论以那两张表和日度配对差为准:
  同半衰期下,删节点改善的是多空不是多头腿;多头腿净超额最高的是不带 `C` 或只带一次方的成交额水平家族(`b_stdamt9`、`d_sum_k1`、`x_std9_k1`),带 `C²`、`C³` 的更低。
- 全部变体的 `cov` 都是 1.00;`dist` 除 `i_addrank`(0.73,两个排名相加会撞值)外都是 1.00 —— 两道门槛都不构成约束。

## 9. 机制诊断

**一句话**:这棵树是「成交额水平 ×(最近 30 天平均日内成交曲线的集中度)^k」。成交额水平是已知家族;集中度这一支在已知暴露之外的成分**只在 2018–2020 年看得到**。
```

**10-04 00:24 · Bash** — Regenerate report and read section 10 and appendix

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh report F103_amt_dw_decay 2>&1 | tail -2 && awk 'NR>=1405 && NR<=1420' research/alpha_distillation/F103_amt_dw_decay.md | cut -c1-260 && echo ... && awk 'NR>=1477 && NR<=1560' research/alpha_distillation/F103_amt_dw_decay.md | cut -c1-200 && echo ... && sed -n 1632,1669p research/alpha_distillation/F103_amt_dw_decay.md | cut -c1-220
```

```
wrote /root/autodl-tmp/Partura/research/alpha_distillation/F103_amt_dw_decay.md
    1669 research/alpha_distillation/F103_amt_dw_decay.md
## 10. 蒸馏 / 升华后的候选

**最终对比,与用户表同口径**(留出段 = 用户的测试段)

| 结构 | 方向 | 半衰期 | 扣费多空夏普 训练/测试 | 多头腿毛超额 训练/测试 | 多头腿净超额 训练/测试 | 纯多头夏普 训练/测试 | 空头腿毛超额 训练/测试 | 多头占比(训练) | 多空日换手 |
|---|---|---|---|---|---|---|---|---|---|
| _用户表里公布的原式_ | − | 2 | +3.53 / +3.18 | +12.8% / +12.4% | — | — | — | — | — |
| `f_orig` `cross_max(mul(day_close(Amt), ts_min(pow_3(day_durbin_wat...` | − | 2 | **+3.53 / +3.18** | +12.8% / +12.4% | +5.6% / +5.5% | +1.11 / +1.04 | +38.7% / +36.6% | 24.8% | 8.4% |
| `f_sum_k3` `mul(day_sum(Amt), pow_3(day_durbin_watson(cross_decay_lin...` | − | 10 | **+3.64 / +3.52** | +11.8% / +12.3% | +8.4% / +9.2% | +1.66 / +1.77 | +36.6% / +35.4% | 24.3% | 3.9% |
| `f_sum_k2` `mul(day_sum(Amt), pow_2(day_durbin_watson(cross_decay_lin...` | − | 10 | **+3.45 / +3.10** | +15.7% / +15.6% | +12.3% / +12.6% | +2.18 / +2.07 | +37.5% / +34.6% | 29.6% | 3.9% |
| `f_std9_k1` `mul(cross_max(day_std(Amt), 9), day_durbin_watson(cross_d...` | − | 2 | **+3.58 / +3.14** | +19.1% / +16.9% | +13.3% / +11.6% | +2.27 / +1.55 | +43.1% / +44.1% | 30.7% | 6.9% |
| `f_stdamt9` `cross_max(day_std(Amt), 9)` | − | 0 | **+2.94 / +2.55** | +19.2% / +15.2% | +11.9% / +8.2% | +1.82 / +0.89 | +40.7% / +46.0% | 32.0% | 8.3% |

### 修订说明(审查之后加的,先读这一段)

这一节在两路独立审查之后重写过。留出段的流程和原报告的写法有下面几处问题,照实写在这里:
...
### 读完留出段之后(留出段只读了这一次;本节在审查后重写,旧版的结论改了什么见开头的修订说明)

最上面那张表是用户口径:方向和半衰期在 utrain(2018-01 ~ 2023-08-07)上定,测试 = 留出段(2023-08-08 ~ 2025-12-31,581 个交易日)。原式那一行复现了用户表(+3.53 / +3.1

**同一张表,每个候选两个半衰期。** "官方"= 在 utrain 上按多空夏普选的(用户表的规则,最上面那张表就是这一行);另一行 = 在 utrain 上按纯多头夏普选的�

| | 半衰期 | 多空夏普 训练 / 测试 | 多头腿毛超额 | 多头腿净超额 | 纯多头夏普 | 多头腿最大回撤(测试) | 多空日换手(测试) |
|---|---|---|---|---|---|---|---|
| `f_orig` | 2(官方) | +3.53 / +3.18 | +12.8% / +12.4% | +5.6% / +5.5% | +1.11 / +1.04 | −7.1% | 8.2% |
| `f_orig` | 10 | +3.39 / +2.92 | +11.1% / +10.2% | +8.1% / +7.2% | +1.49 / +1.26 | −6.9% | 3.6% |
| `f_sum_k3` | 10(官方) | +3.64 / **+3.52** | +11.8% / +12.3% | +8.4% / +9.2% | +1.66 / +1.77 | −5.1% | 3.7% |
… (92 行略) …
# final: 184.0s, 峰值 anon 2.61 GiB, stages ['S_final']
scripts/run_server.sh configs/F103_amt_dw_decay.yaml <stage...>          # EXTRA=--holdout 才读留出段
python -m partura.cli report configs/F103_amt_dw_decay.yaml
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
}
```
```

**10-04 00:25 · Bash** — Verify config timestamp and ledger unchanged; skim section 9 rendering

```bash
cd /Users/wxy/Desktop/Partura && stat -f "%Sm %N" -t "%Y-%m-%d %H:%M:%S" configs/F103_amt_dw_decay.yaml runs/F103_amt_dw_decay/*.json && python3 -c "
import json
d=json.load(open('runs/F103_amt_dw_decay/ledger.json'))
print(d['summary'])" && ls -la runs/F103_amt_dw_decay/ && sed -n 1308,1404p research/alpha_distillation/F103_amt_dw_decay.md | cut -c1-140 | head -60
```

```
2026-10-03 23:22:50 configs/F103_amt_dw_decay.yaml
2026-10-03 17:43:26 runs/F103_amt_dw_decay/S0_baseline.json
2026-10-03 19:34:22 runs/F103_amt_dw_decay/S1_structure.json
2026-10-03 23:19:17 runs/F103_amt_dw_decay/S2_distil.json
2026-10-03 23:26:41 runs/F103_amt_dw_decay/final.json
2026-10-03 23:26:41 runs/F103_amt_dw_decay/ledger.json
{'train': {'reads': 7, 'expressions': 32}, 'valid': {'reads': 7, 'expressions': 32}, 'utrain': {'reads': 7, 'expressions': 32}, 'holdout': {'reads': 1, 'expressions': 5}, 'full': {'reads': 1, 'expressions': 5}}
total 904
drwxr-xr-x@  7 wxy  staff     224 Oct  3 23:26 .
drwxr-xr-x@ 19 wxy  staff     608 Oct  3 17:37 ..
-rw-r--r--@  1 wxy  staff   34269 Oct  3 17:43 S0_baseline.json
-rw-r--r--@  1 wxy  staff  110135 Oct  3 19:34 S1_structure.json
-rw-r--r--@  1 wxy  staff  203127 Oct  3 23:19 S2_distil.json
-rw-r--r--@  1 wxy  staff  100934 Oct  3 23:26 final.json
-rw-r--r--@  1 wxy  staff    4445 Oct  3 23:26 ledger.json
## 9. 机制诊断

**一句话**:这棵树是「成交额水平 ×(最近 30 天平均日内成交曲线的集中度)^k」。成交额水平是已知家族;集
原式把八成权重押在集中度上:多空夏普不差,多头腿弱。多头腿能改善的部分,一块是把半衰期调慢,一块是�

(本节在审查后修订过。原来的"已确立"第 1、5、8、10 条有改写或降级,新增了第 2、9 条;改动处标了"修订"�

### 已确立(每条后面是实验)

1. **七个算子里三个可以删;删完多空更好,多头腿不因此变好。** `ts_min(·,1)` 是恒等(探针 `window_one_is_identity
   `cross_max(·,5)` 只是低通(S1:删掉 +4.35 / +2.41、换成均值 +4.26 / +2.49,原式 +4.14 / +2.22),原因在 X3-H:书是对原始�
   **所以它"多余"的前提是下游有半衰期 ≥ 5 的 EMA**:不平滑时 utrain 多空夏普 原式 +2.79、删掉它的 `A·C³` �
   三个一起删(`d_sum_k3`),**同一个半衰期(10)下**多空净收益比原式每年高 +3.1% / +5.4% / +3.8%(train / valid / utrain,�
   多头腿净超额差 −0.6% / +2.8% / +0.4%(utrain t +0.3)(X4-B、X5-B)。**留出段多空夏普 +3.52,原式 +3.18(半衰期 2)/ +2.9
   (修订:原文写"换成全天成交额,多头腿两段都更好(+9.5% / +7.4% 对 +6.3% / +3.6%)",比的是半衰期 10 对半衰期 2;�
… (25 行略) …
   乘 `C` 等于减掉一部分成交额水平暴露。对冲之后的 alpha:train +6.7% / 年(t +6.5),valid +1.9%(t +1.3)。书的年化�
   valid(2022-01~2023-08)是成交额水平最强的一段(控制变量表),这一条不变。
10. **"保序的外层变换是 no-op"在这套口径下不成立。** 同一面板取 `log` 或截面排名之后逐日排名不变、rank 
11. **留出段:事前写下的四条判据,三条过了,一条没过。**(修订:原文写"三条判据都过了",漏了没过的那条。)
    - 提纯(`f_sum_k3` 的多空夏普不低于原式 0.3 以上):+3.52 对 +3.18,**过**。
    - 升华(事前首选 `f_std9_k1` 的多头腿净超额、纯多头夏普都高于原式,多空夏普不低 0.3 以上):+11.6%、+1.55 �
      都换成半衰期 10 是 +14.2%、+1.92 对 +7.2%、+1.26,多空 +2.75 对 +2.92,也过。
    - "给已知家族加了东西"(`f_std9_k1` 的多空夏普比 `f_stdamt9` 高 0.3 以上、纯多头夏普不低于它):+3.14 对 +2.55
    - **没过的一条**(配置里 `f_sum_k2` 的 `why`:"若留出段上它不如 `f_sum_k3`,'指数 3 是 train 的局部最优'这个读�
      **指数从 3 降到 2 这一步在留出段的多空夏普上是亏的。**

### 合理但没坐实

- **经济解释**:平均日内成交曲线粗糙 / 集中、同时成交又很活跃的股票,是散户追逐的题材票,之后跑输。�
  (修订:原文把"成交长期挤在开盘第一分钟(`day_argmax(B)` 68% / 87% 落在 9:31)"写成这棵树的描述。那是峰值占�
  `C` 与首根占比的 rank 相关只有 0.109、与头两根占比 0.131、与收盘竞价占比 0.422、与 `p_peak` 0.426,它 69% 被�
  X2-e 里换成"收盘竞价占比"的版本(+3.51 / +3.91)也不输"头两根占比"的版本(+2.97 / +3.53)。`C` 里有预测力的更�
- **"集中度那条腿在 2024–2025 年回来了 / 两条腿轮动"**(修订:从"已确立"第 8 条降下来)。留出段多空夏普的
  但 (a) train / valid 上 `C` 的增量是单调衰减,六年里只切换了一次,谈不上轮动;(b) `f_std9_k1` 比 `f_stdamt9` 高的 
  **只换波动 +0.44,均值 +0.15**(+1.2% / 年,按 utrain 上配对差的波动折算不到 1 个标准误;审查的估计是两个夏普
```

**10-04 00:25 · Bash** — Verify C correlation figures in x1/x2 logs

```bash
cd /Users/wxy/Desktop/Partura && grep -an "首根\|头两根\|开盘 10\|开盘10\|收盘竞价占比\|p_peak\|0\.109\|0\.131\|0\.422\|0\.426" logs/F103_amt_dw_decay_x1.log logs/F103_amt_dw_decay_x2.log | cut -c1-260 | head -30
```

```
logs/F103_amt_dw_decay_x1.log:35:A                                  +0.380     -0.426     +0.862
logs/F103_amt_dw_decay_x1.log:40:p_close 平均曲线尾盘占比                   +0.325     +0.422     -0.076
logs/F103_amt_dw_decay_x1.log:41:p_open 平均曲线首根占比                    +0.376     +0.109     +0.298
logs/F103_amt_dw_decay_x2.log:57:p_peak 峰值分钟占比              corr(.,eps_C) +0.535   corr(.,C) +0.426   corr(.,G) +0.578
logs/F103_amt_dw_decay_x2.log:58:p_first2 头两根占比             corr(.,eps_C) +0.296   corr(.,C) +0.131   corr(.,G) +0.399
logs/F103_amt_dw_decay_x2.log:59:p_open10 开盘10分钟占比          corr(.,eps_C) +0.123   corr(.,C) -0.027   corr(.,G) +0.262
logs/F103_amt_dw_decay_x2.log:60:p_close 收盘竞价占比             corr(.,eps_C) +0.320   corr(.,C) +0.422   corr(.,G) +0.325
logs/F103_amt_dw_decay_x2.log:97:day_sum*p_peak^3.19        -  5 +0.0541 +0.0576  +3.60 +3.63  +16.8%/+16.0%  +12.9%/+12.7%  +2.09/+2.28   4.6% +0.577  | hlL 10: Lnet +14.4%/+13.7% Lshp +2.31/+2.43  corr(X,C) +0.426
logs/F103_amt_dw_decay_x2.log:98:day_sum*p_first2^2.66      -  5 +0.0481 +0.0584  +2.97 +3.53  +13.6%/+15.0%  +10.3%/+12.0%  +1.59/+2.07   4.1% +0.433  | hlL 20: Lnet +10.5%/+15.2% Lshp +1.60/+2.76  corr(X,C) +0.131
logs/F103_amt_dw_decay_x2.log:100:day_sum*p_close^4.08       -  3 +0.0431 +0.0430  +3.51 +3.91  +11.7%/+12.3%   +7.2%/ +8.1%  +1.22/+1.66   5.5% +0.564  | hlL 10: Lnet  +9.7%/+10.2% Lshp +1.61/+1.96  corr(X,C) +0.422
```

**10-04 00:25 · Bash** — Collect final structured numbers for all candidates

```bash
cd /Users/wxy/Desktop/Partura && python3 - <<'EOF'
import json
d=json.load(open('runs/F103_amt_dw_decay/final.json'))
for k,v in d['results'].items():
    bu=v['books_user']
    u,h=bu['splits']['utrain'],bu['splits']['holdout']
    print(k, 'cov',round(v['ic_user']['coverage_labelled'],4),'dist',v['distinct'],'hl',bu['hl_used'],
          'ls',round(u['ls_sharpe'],3),round(h['ls_sharpe'],3),'Lg',round(u['long_gross_ann'],4),round(h['long_gross_ann'],4),
          'Ln',round(u['long_ann'],4),round(h['long_ann'],4),'Ls',round(u['long_sharpe'],3),round(h['long_sharpe'],3),'TO',round(u['ls_turnover'],4),
          'corr_orig',round(d['diagnostics']['rank_corr_train']['f_orig'][k],3))
EOF
```

```
f_orig cov 0.9993 dist 1.0 hl 2.0 ls 3.533 3.18 Lg 0.1275 0.1241 Ln 0.0557 0.0547 Ls 1.108 1.044 TO 0.0843 corr_orig 1.0
f_sum_k3 cov 0.9993 dist 1.0 hl 10.0 ls 3.64 3.518 Lg 0.1176 0.1232 Ln 0.0843 0.0923 Ls 1.658 1.765 TO 0.0386 corr_orig 0.861
f_sum_k2 cov 0.9993 dist 1.0 hl 10.0 ls 3.446 3.099 Lg 0.1574 0.1558 Ln 0.123 0.1264 Ls 2.179 2.071 TO 0.0389 corr_orig 0.745
f_std9_k1 cov 0.9993 dist 1.0 hl 2.0 ls 3.58 3.142 Lg 0.191 0.1693 Ln 0.1329 0.1164 Ls 2.274 1.547 TO 0.0691 corr_orig 0.647
f_stdamt9 cov 0.9993 dist 1.0 hl 0.0 ls 2.943 2.551 Lg 0.1916 0.1517 Ln 0.119 0.0819 Ls 1.817 0.89 TO 0.0827 corr_orig 0.412
```

**10-04 00:27 · Bash** — Check report table integrity and leftover outdated phrases

```bash
cd /Users/wxy/Desktop/Partura && python3 - <<'EOF'
import re
L=open('research/alpha_distillation/F103_amt_dw_decay.md',encoding='utf-8').read().split('\n')
# check markdown tables: consistent column counts within each table block
bad=0
i=0
while i<len(L):
    if L[i].startswith('|'):
        j=i
        while j<len(L) and L[j].startswith('|'): j+=1
        def ncol(s):
            s=s.replace('\\|','')
            return s.count('|')
        n0=ncol(L[i])
        for k in range(i,j):
            if ncol(L[k])!=n0:
                bad+=1; print('col mismatch line',k+1,ncol(L[k]),'vs',n0, L[k][:90])
        i=j
    else: i+=1
print('table blocks checked; mismatches:',bad)
# any leftover claims
for pat in ['主要是 9:31','三条判据都过','这棵树最稳的发现','轻微选择偏差','最终推荐:']:
    for k,l in enumerate(L):
        if pat in l: print(pat,'@',k+1, l[:120])
EOF
```

```
col mismatch line 693 8 vs 7 | v_base|ctl_cap | -0.0493 | -0.0444 | -0.0458 | -0.0379 | -0.0238 |
col mismatch line 694 8 vs 7 | v_base|ctl_amt | -0.0113 | -0.0164 | -0.0236 | -0.0378 | -0.0544 |
col mismatch line 695 8 vs 7 | a_C|ref_A5 | -0.0019 | -0.0064 | -0.0150 | -0.0300 | -0.0514 |
col mismatch line 696 8 vs 7 | a_A5|ref_C | -0.0142 | -0.0396 | -0.0542 | -0.0599 | -0.0688 |
col mismatch line 697 8 vs 7 | a_C|ctl_amt | -0.0028 | -0.0080 | -0.0187 | -0.0355 | -0.0611 |
col mismatch line 698 8 vs 7 | d_sum_k2|ctl_amt | -0.0066 | -0.0120 | -0.0219 | -0.0371 | -0.0491 |
col mismatch line 699 8 vs 7 | d_sum_k2|ctl_cap | -0.0679 | -0.0591 | -0.0574 | -0.0445 | -0.0202 |
col mismatch line 700 8 vs 7 | x_std9_k1|ctl_amt | -0.0271 | -0.0230 | -0.0275 | -0.0367 | -0.0462 |
col mismatch line 701 8 vs 7 | x_std9_k1|ctl_cap | -0.0762 | -0.0671 | -0.0638 | -0.0492 | -0.0236 |
table blocks checked; mismatches: 9
主要是 9:31 @ 1364   X2-e 里换成"收盘竞价占比"的版本(+3.51 / +3.91)也不输"头两根占比"的版本(+2.97 / +3.53)。`C` 里有预测力的更像是首尾几根和没被平均掉的尖峰(X3-D:纯内部的 DW 残差 rank IC −0.0
三条判据都过 @ 1351 11. **留出段:事前写下的四条判据,三条过了,一条没过。**(修订:原文写"三条判据都过了",漏了没过的那条。)
三条判据都过 @ 1429 3. **原报告漏了一条没过的判据。** 配置里给 `f_sum_k2` 写的那条判据在留出段上没过(多空夏普 +3.10 对 `f_sum_k3` 的 +3.52,低 0.42,超过 ±0.3 的噪声),而原报告写的是"事前写下的三条判据
这棵树最稳的发现 @ 1334    (修订,降级:原文把这个角称为"集中度是一个避雷变量""这棵树最稳的发现"。替换实验说它是已知的"活跃 × 热门"效应,`C` 只是代理之一 ——
```

**10-04 00:29 · StructuredOutput**

```json
{
 "factor_id": "F103_amt_dw_decay",
 "one_line": "成交额水平 ×(最近 30 天平均日内成交额曲线的粗糙度/集中度)³:成交活跃、且平均日内成交曲线粗糙/集中的股票之后跑输,钱主要在空头腿。集中度在已知暴露(换手率/波动/涨停史)之外的成分只在 2018–2020 年看得到;多头腿的钱来自已知的成交额水平家族。(C 里有预测力的更像首尾几根与没被平均掉的尖峰,未坐实。)",
 "mechanism": "原式 = cross_max(A·C³, 5),A = day_close(Amt) 是收盘集合竞价那一根的成交额(带成交额尺度),C = day_durbin_watson(cross_decay_linear(Amt,30)) 是\"先把 241 根分钟成交额逐分钟做 30 日平均、再量这条平均曲线的粗糙度\"(尺度无关)。读源码+拆解+审查修订后:(1) 三个节点可删:ts_min(·,1) 恒等;cross_max(·,5) 只是低通——前提是下游有半衰期 ≥ 5 的 EMA(不平滑时 utrain 多空夏普 原式 +2.79、删掉它 −1.45);收盘竞价那一根换成全天成交额。同半衰期(10)下删完多空净收益每年 +3.8%(utrain 配对 t +3.7,六年每年为正),多头腿没有差别(+0.4%,t +0.3)。(2) 骨架是「成交额水平 × 集中度^k」,两条腿缺一不可,\"先平均再折叠\"不可交换。(3) C³ 把 A 的成交额尺度约掉一半多(log C 对 log 成交额斜率 −0.174,×3),所以原式与 ctl_amt 相关只有 0.28、全部控制变量 R² 0.227——是抵消不是新颖。(4) 交互是真的:集中度只在成交活跃的票里排得动,\"成交最活跃 × 曲线最集中\"的 4% 股票次日超额年化 −75%/−64%;但这个角落不是集中度特有的——同一行里按换手率取最高组是 −75%/−95%(日内波动、动量、小市值同样深),角落里 46%/44% 是近 5 日涨停票,C 对已知暴露做组内残差后 rank IC train −0.023、valid +0.006(逐年 −0.023/−0.030/−0.028/−0.011/−0.002/+0.018),当剔除名单在\"换手率角落 ∪ 近 5 日涨停票\"之外只多 +0.45%/+0.09% 每年:2021 年起这部分已被换手率/波动/涨停史解释。(5) C 给已知家族加的多空均值只在 2018–2020 年(F001 蒸馏×C − F001 蒸馏,同半衰期,逐年 +4.3/+9.4/+7.0/−0.7/−1.5/−2.6%);2021–2023 成交额水平强、集中度增量为零,是否回归待新数据。三段都稳定的只有一件事:乘 C 之后书的波动低一成到两成(等于减掉一部分成交额水平暴露,beta −0.15~−0.6)。(6) 多头腿:原式把半衰期从 2 换成 10 就 +2.5 点(utrain)/+1.7 点(留出段);其余的改善来自把权重交给成交额水平这个已知家族——同半衰期下纯 day_sum(Amt)、F001 蒸馏结果自己的多头腿净超额不输任何带 C 的版本。指数 k 是两条腿的配比旋钮(同时决定尾部多重)。",
 "family": "成交额水平 × 30 日平均日内成交曲线的集中度。水平腿与 F001 同族(成交额水平 + 峰值记忆),多头腿就是这个家族的多头腿。集中度腿在 2018–2020 年有已知家族之外的成分,2021–2023 年没有;留出段一次观测(带 C 的版本比 F001 蒸馏结果高 0.59 个多空夏普,其中 0.44 来自波动降低、0.15 来自均值,均值不到 1 个标准误)不足以说明它恢复了,未坐实。推荐版与 F001 蒸馏结果 rank 相关 0.93,被全部控制变量张成 0.646。",
 "original": {
  "expr": "cross_max(mul(day_close(Amt), ts_min(pow_3(day_durbin_watson(cross_decay_linear(Amt, 30))), 1)), 5)",
  "ls_train": 3.533,
  "ls_test": 3.18,
  "long_gross_train": 0.1275,
  "long_gross_test": 0.1241,
  "long_net_train": 0.0557,
  "long_net_test": 0.0547,
  "long_sharpe_train": 1.108,
  "long_sharpe_test": 1.044,
  "sign": -1,
  "halflife": 2,
  "turnover": 0.0843,
  "coverage": 0.9993,
  "distinct": 1,
  "n_operators": 7,
  "rank_corr_with_original": 1
 },
 "recommended": {
  "expr": "mul(cross_max(day_std(Amt), 9), day_durbin_watson(cross_decay_linear(Amt, 30)))",
  "ls_train": 3.58,
  "ls_test": 3.142,
  "long_gross_train": 0.191,
  "long_gross_test": 0.1693,
  "long_net_train": 0.1329,
  "long_net_test": 0.1164,
  "long_sharpe_train": 2.274,
  "long_sharpe_test": 1.547,
  "sign": -1,
  "halflife": 2,
  "turnover": 0.0691,
  "coverage": 0.9993,
  "distinct": 1,
  "n_operators": 5,
  "rank_corr_with_original": 0.647
 },
 "recommended_kind": "elevated",
 "other_finalists": [
  {
   "expr": "mul(day_sum(Amt), pow_3(day_durbin_watson(cross_decay_linear(Amt, 30))))",
   "ls_train": 3.64,
   "ls_test": 3.518,
   "long_gross_train": 0.1176,
   "long_gross_test": 0.1232,
   "long_net_train": 0.0843,
   "long_net_test": 0.0923,
   "long_sharpe_train": 1.658,
   "long_sharpe_test": 1.765,
   "sign": -1,
   "halflife": 10,
   "turnover": 0.0386,
   "coverage": 0.9993,
   "distinct": 1,
   "n_operators": 5,
   "rank_corr_with_original": 0.861
  },
  {
   "expr": "mul(day_sum(Amt), pow_2(day_durbin_watson(cross_decay_linear(Amt, 30))))",
   "ls_train": 3.446,
   "ls_test": 3.099,
   "long_gross_train": 0.1574,
   "long_gross_test": 0.1558,
   "long_net_train": 0.123,
   "long_net_test": 0.1264,
   "long_sharpe_train": 2.179,
   "long_sharpe_test": 2.071,
   "sign": -1,
   "halflife": 10,
   "turnover": 0.0389,
   "coverage": 0.9993,
   "distinct": 1,
   "n_operators": 5,
   "rank_corr_with_original": 0.745
  },
  {
   "expr": "cross_max(day_std(Amt), 9)",
   "ls_train": 2.943,
   "ls_test": 2.551,
   "long_gross_train": 0.1916,
   "long_gross_test": 0.1517,
   "long_net_train": 0.119,
   "long_net_test": 0.0819,
   "long_sharpe_train": 1.817,
   "long_sharpe_test": 0.89,
   "sign": -1,
   "halflife": 0,
   "turnover": 0.0827,
   "coverage": 0.9993,
   "distinct": 1,
   "n_operators": 2,
   "rank_corr_with_original": 0.412
  }
 ],
 "known_exposure_r2": 0.646,
 "verdict": "提纯成立;升华按事前判据成立,但升华出来的多头腿不是这棵树的。推荐的是【事前登记的首选】f_std9_k1 = mul(cross_max(day_std(Amt), 9), day_durbin_watson(cross_decay_linear(Amt, 30)))(5 个算子,原式 7 个):用户口径 训练/测试(与原式同为半衰期 2)多头腿净超额 +5.6%/+5.5% → +13.3%/+11.6%,纯多头夏普 +1.11/+1.04 → +2.27/+1.55,多空夏普 +3.53/+3.18 → +3.58/+3.14,换手 8.4% → 6.9%;只做多头改用半衰期 10(utrain 上按纯多头夏普选的):+15.6%/+14.2%、+2.61/+1.92、换手 3.4%、多空 +3.20/+2.75。这一行不带选择偏差。必须说明的六点:(1) 原报告读完留出段后把推荐改成了 f_sum_k2 = mul(day_sum(Amt), pow_2(C))(+12.3%/+12.6%、+2.18/+2.07、+3.45/+3.10)——那一行是在三个非基准候选里按留出段多头腿选出来的,测试列带选择偏差,不是干净的样本外;本次修订把推荐改回事前登记者,f_sum_k2 列在 other_finalists 里作事后备选。train/valid 上同半衰期它的多头腿显著不如事前首选(−3.3%/年,t −4.0),中性化后残差也是各候选里最小的(rank IC 0.0123)。(2) 事前判据四条过了三条:纯删节点 f_sum_k3 留出段多空夏普 +3.52 对原式 +3.18;f_std9_k1 多头腿高于原式、多空 +3.14;它比 F001 蒸馏结果(+2.55)高 0.59。没过的一条:f_sum_k2 比 f_sum_k3 低 0.42——指数 3→2 这一步在留出段多空夏普上是亏的(原报告漏报)。(3) 多头腿的改善以原式@半衰期 10 为基准拆三步(utrain/留出段):只改半衰期 2→10 +2.5/+1.7 点(原式自己就拿得到,代价是多空夏普 3.53/3.18 → 3.39/2.92);删三个节点 +0.4/+2.1 点;指数 3→2 +3.9/+3.4 点(加的是已知暴露)。换手下降全部来自半衰期,不是删节点;原报告的\"+5.5% → +12.6%\"按同半衰期应读作 +7.2% → +12.6%。(4) 对纯多头,多头腿收益来自成交额水平这个已知家族:同半衰期(10)utrain 多头腿净超额 纯 day_sum +13.9%、day_sum·C +14.9%、F001 蒸馏 +15.7%,推荐者 +15.6%、f_sum_k2 +12.3%;乘 C 的配对差不为正(F001 蒸馏×C − F001 蒸馏 @2:−1.9%/年,t −2.1)。推荐者与 F001 蒸馏 rank 相关 0.93、已知暴露 R² 0.646(原式的 0.227 是尺度抵消,f_sum_k2 是 0.554):库里已有 F001 蒸馏结果的话,它是同一个因子的低波动写法,不是新因子。(5) 留出段上它比 F001 蒸馏高的 0.59 个多空夏普里 0.44 是波动、0.15 是均值;集中度在已知家族之外的 alpha 没有被留出段证实,\"两条腿轮动\"撤回。(6) 若只看多空夏普,纯删节点的 f_sum_k3 = mul(day_sum(Amt), pow_3(C))(与原式 0.86,留出段 +3.52,同半衰期下多空每年 +3.8%、t +3.7)是同一个因子的提纯版,须配半衰期 ≥ 5 的 EMA。",
 "established": [
  "七个算子里三个可删;删完多空更好、多头腿不因此变好:ts_min(·,1) 恒等(探针 + S1 a_no_tsmin 逐位相同);cross_max(·,5) 只是低通(S1:删掉 +4.35/+2.41、换均值 +4.26/+2.49,原式 +4.14/+2.22),前提是下游有半衰期 ≥ 5 的 EMA(半衰期 0 时 utrain 多空夏普 原式 +2.79、删掉它 −1.45,X4-A);收盘竞价额换成全天成交额。三个一起删,同半衰期 10 下多空净收益比原式每年 +3.1%/+5.4%/+3.8%(train/valid/utrain,t +2.5/+3.2/+3.7,六年每年为正),多头腿 −0.6%/+2.8%/+0.4%(t +0.3)(X4-B、X5-B);留出段多空夏普 +3.52 对原式 +3.18(@2)/+2.92(@10)(S_final)。",
  "原式的多头腿弱有一部分只是半衰期:按多空夏普选中的半衰期 2 只比 10 高 0.05/0.14,换手 8.4% 对 3.6%。只改半衰期,utrain 多头腿净超额 +5.6% → +8.1%(配对差 +2.5%,t +2.4),留出段 +5.5% → +7.2%;多空夏普 3.53 → 3.39、留出段 3.18 → 2.92(X4、final.json 的 splits_at_hl_long)。换手下降全部来自半衰期,不是删节点。",
  "骨架是「成交额水平 × 30 日平均曲线集中度^k」,两条腿缺一不可、尺度不能约掉、平均必须在折叠之前:只留 A +1.81/+3.69,只留 C +1.79/−1.75,A 换成尾盘占比 valid −1.96,排名相乘 valid −0.08(S1);先逐日 DW 再平均代入整树 +1.00/+1.14(X1-6);当日 DW 方向都反 −1.38/−2.77(X2-e);窗口 10~60 是平台。",
  "原式被全部控制变量张成的 R² 只有 0.227,是因为 C³ 把 A 的成交额尺度约掉一半多(log C 对 log 成交额斜率 −0.174,X1-4),不是因为它新;中性化后 rank IC 0.0358 → 0.0172,空头腿 +42.8% → +9.1%(S0 中性化表)。各候选的 R²:f_sum_k2 0.554、f_std9_k1 0.646、F001 蒸馏 0.834;中性化后的残差 f_sum_k2 最小(rank IC 0.0123、无成本多空夏普 +1.81;原式 0.0172/+2.83,f_std9_k1 0.0170/+3.37,F001 蒸馏 0.0193/+5.03)(S2 中性化表)。",
  "集中度只在成交活跃的票里排得动(C 的条件 rank IC 按成交额五分桶 −0.0028 → −0.0611,S1),「成交最活跃 × 最集中」的 4% 次日超额年化 −75%/−64%(X2-b);低成交额行方向 train/valid 相反(X2-b、X3-F)。但这个角落不是集中度特有的:同一行里按换手率取最高组 −74.9%/−94.6%、日内波动 −72.0%/−91.2%、动量 −64.3%/−90.3%;角落里 46%/44% 近 5 日涨停过,剔掉后 −34.8%/−17.7%;C 对全部已知暴露做组内残差后 rank IC −0.0230/+0.0057,逐年 −0.023/−0.030/−0.028/−0.011/−0.002/+0.018(X4-C);当剔除名单,在「换手率角落 ∪ 近 5 日涨停票」(+6.7%/+5.9% 每年)之外再剔 C 角落只多 +0.45%(t +4.8)/+0.09%(t +0.6)(X5-D)。C 特有的成分只在 2018–2020 年存在。",
  "多头腿的钱来自成交额水平这个已知家族,乘 C 不给多头腿加收益:同半衰期 10 的 utrain 多头腿净超额 纯 day_sum +13.9%、day_sum·C +14.9%、F001 蒸馏 +15.7%、F001 蒸馏×C +15.6%、day_sum·C² +12.3%、day_sum·C³ +8.4%、原式 +8.1%(X5-A);配对差 day_sum·C² − day_sum:+1.1%/−8.3%(t −3.1)/−1.6%(X4-B),F001 蒸馏×C − F001 蒸馏 @2:−1.1%/−4.0%(t −2.8)/−1.9%(t −2.1)(X5-B)。多头十分位市值百分位 0.19~0.31,市值中性后 day_sum·C² 的多头腿净超额只剩约 +2%(X3-E)。",
  "C 给已知家族加的多空均值只在 2018–2020 年,两段都在的是波动降低:F001 蒸馏×C − F001 蒸馏(同半衰期 2)多空净收益逐年 +4.3/+9.4/+7.0/−0.7/−1.5/−2.6%;对成交额水平收益的 beta −0.15,对冲后 alpha train +6.7%(t +6.5)、valid +1.9%(t +1.3);年化波动 train 8.4% → 7.5%、valid 7.1% → 6.5%,只换波动的夏普 +0.28/+0.38(X4-E、X5-B、X5-C)。valid 是成交额水平的大年(控制变量表)。",
  "留出段:事前写下的四条判据三条过、一条没过(S_final)。过:f_sum_k3 多空夏普 +3.52 对原式 +3.18;事前首选 f_std9_k1 多头腿净超额 +11.6%、纯多头夏普 +1.55 高于原式 +5.5%、+1.04(同为半衰期 2;都用 10 是 +14.2%/+1.92 对 +7.2%/+1.26),多空 +3.14 对 +3.18;f_std9_k1 比 F001 蒸馏(+2.55)高 0.59(按字面过)。没过:f_sum_k2 +3.10 比 f_sum_k3 +3.52 低 0.42。",
  "事前首选相对原式在同半衰期下两本书都更好(utrain,半衰期 2:多空 +6.5%/年、多头腿 +7.7%/年,t 都是 +2.9),优势全在成交额水平强的年份,2019–2020 年原式更好;它的多头腿在 train/valid 上同半衰期显著好于事后改选的 f_sum_k2(+2.4%/+5.5%/+3.3%,t +2.5/+3.5/+4.0)(X5-B)。",
  "「保序的外层一元变换是 no-op」在先 EMA 后排名、半衰期 > 0 的口径下不成立:同一面板取 log 或排名后 rank IC 逐位相同,书差 0.4~1.1 个夏普(X3-H)。"
 ],
 "unresolved": [
  "集中度在已知暴露之外的成分 2023 年 8 月之后有没有恢复:train/valid 上 2021 年起为零;留出段只有一次间接观测(带 C 的版本多空夏普高 0.59,其中 0.44 是波动、0.15 是均值,均值差 +1.2%/年不到 1 个标准误),没有放 day_sum 基准,也没有量成交额中性集中度的 rank IC(不能再读)。「两条腿轮动」从已确立降级到这里。",
  "乘 C 的版本留出段多头腿更稳(最大回撤 F001 蒸馏 −15.4%、f_std9_k1 −9.2%、f_sum_k2 −5.2%)是不是可依赖的性质:train/valid 上对应的是波动低一成、多头腿均值不增;同样的波动降低能不能用更便宜的办法拿到(部分中性化、与低相关因子等权)没有测。",
  "指数对多空夏普没有稳定的最优值:k=3 对 k=2 是 train +3.93/+3.33、valid +2.88/+3.78、留出段 +3.52/+3.10;多头腿则 k 越小越好,但那只是成交额水平的权重越高越好。",
  "多头腿是不是 alpha:对市值做秩中性化后 train/valid 多头腿净超额只剩约 +2%(X3-E,量的是 day_sum·C²);f_std9_k1 和留出段的市值中性版本都没有量。",
  "f_sum_k2 的留出段数字带选择偏差(读完留出段后在三个非基准候选里按多头腿选出;审查估计纯多头夏普预期上偏 0.2~0.3),不能当样本外数字用。",
  "C 里到底哪部分有预测力:构成上 69% 是内部块状噪声,残差 rank IC 的对比(纯内部 DW −0.0086 对 C −0.0253)提示是首尾几根与没被平均掉的尖峰,不是「主要是 9:31」(C 与首根占比 rank 相关 0.109、与收盘竞价占比 0.422);DW 还是峰值占比 train/valid 分不出高下,留出段没有放峰值占比候选。经济解释(散户追逐的题材票)只有间接证据。",
  "10_distilled 里「读留出段之前」那一段自述写于 final 之前,但文件修改时间(23:34)晚于 final(23:26),无法从文件时间核实;能独立佐证事前登记的只有配置文件 S_final 各候选的 why(修改时间 23:22:50,final 23:23:39 启动)。"
 ],
 "lab_findings": [
  {
   "id": "F103-L1",
   "claim": "「保序的外层一元变换是 no-op」只在 EMA 半衰期 = 0 时成立。用户口径是先对原始数值做 EMA 再排名:重尾正数直接做 EMA ≈ 带衰减的峰值记忆;先取 log 或截面排名再做 EMA 就成了普通均值平滑,换手更高、表现更差。指数 k 因此既定配比也定尾部多重。",
   "evidence": "X3-H:同一面板逐日排名相同、rank IC 逐位相同(0.0464/0.0491),day_sum·C² 原值 +3.33/+3.78、多头腿净 +11.4%/+14.5%;log 版 +2.60/+3.42、+6.3%/+13.7%;rank 版 +2.27/+3.08、+7.4%/+13.8%。day_sum、day_sum·C、day_sum·p_peak² 同向(train 差 0.4~1.1 夏普)。",
   "operators": [
    "pow_3",
    "pow_2",
    "log",
    "cs_rank",
    "sigmoid"
   ],
   "confidence": "high",
   "recheck": "半衰期选中 0 时退化为 no-op;操作数本身有界或已是排名时差别小;如果建书流程改成先截面标准化/排名再平滑,这条不适用。playbook 里「别把保序变换当成变体来试」需要加这个限定。"
  },
  {
   "id": "F103-L2",
   "claim": "对恒正、重尾的水平量,外层 cross_max(·, d) 在下游有半衰期 ≥ 5 的 EMA 时是多余的:EMA 作用在原始数值上已经在做「峰值记忆」,删掉或换成 cross_mean 多空不掉。没有 EMA 或半衰期 ≤ 2 时它不是多余的。",
   "evidence": "S1:原式 +4.14/+2.22;删 cross_max(·,5) +4.35/+2.41(选中半衰期 5);换 cross_mean +4.26/+2.49。同半衰期 10 下删三个节点的 day_sum·C³ 对原式的多空配对差 +3.8%/年(utrain,t +3.7),留出段 +3.52 对 +3.18。反例(X4-A):半衰期 0 时 utrain 多空夏普 原式 +2.79、删掉 cross_max 的 A·C³ −1.45;半衰期 2 时 +3.53 对 +3.20。",
   "operators": [
    "cross_max",
    "cross_mean"
   ],
   "confidence": "high",
   "recheck": "操作数正负混杂时不成立(F001:极值 = 取幅度);换手的差别必须在同一个半衰期下比(本研究第一版把半衰期 2→10 的换手下降记到了删节点头上,同半衰期下 3.6% 对 3.9%);只在 15bp 成本、EMA 口径下测过。"
  },
  {
   "id": "F103-L3",
   "claim": "窗口为 1 的日轴滚动算子(ts_min(x,1)、ts_max(x,1) 等)是逐位恒等,只是 GP 用来把 dt 面的量「过」到 nd 面的换面节点,可以直接删。",
   "evidence": "探针 window_one_is_identity(自检:ts_max(x,1) 恒等、ts_delay(x,1) 不是);S1 a_no_tsmin 与原式 rank 相关 1.000000、NaN 位置一致、所有指标逐位相同。",
   "operators": [
    "ts_min",
    "ts_max",
    "cross_max",
    "cross_decay_linear"
   ],
   "confidence": "high",
   "recheck": "ts_delay 等带位移的算子窗口 1 不是恒等;窗口 1 的 stddev/corr 类会给 NaN,需单独看。"
  },
  {
   "id": "F103-L4",
   "claim": "day_durbin_watson 喂非负的成交额/成交量曲线时量的是曲线的粗糙度/尖峰度(Σ(Δx)²/Σx²,孤立尖峰在中间的响应是末端的 2 倍),既不是自相关也不是已实现方差。喂当日曲线时它主要是流动性差的代理(块状噪声);只有先跨日平均再喂进去才留下持久的日内形状。",
   "evidence": "探针 isolated_spike_response(= (h−1)²/(M−1+h²),中间 ×2)、noise_averaging_exponent(DW ∝ N^−0.985)。X1:当日 DW(Amt) 与成交额水平 rank 相关 −0.67;X2-e:day_sum × 当日 DW 方向都反(−1.38/−2.77),30 日平均后的版本 +3.93/+2.88。",
   "operators": [
    "day_durbin_watson",
    "cross_decay_linear",
    "cross_mean"
   ],
   "confidence": "high",
   "recheck": "操作数是价格水平(≈ 已实现方差,F001)或收益序列(≈ 一阶自相关)时语义完全不同;曲线含负值时不适用。"
  },
  {
   "id": "F103-L5",
   "claim": "「cross_*(分钟级操作数) → day_* 非线性折叠」与「day_* 折叠 → 日轴平均」不可交换:前者先把逐日独立的分钟噪声压掉(有效样本 (Σw)²/Σw²,decay_linear 30 ≈ 22.9 天),量的是平均曲线的形状;后者是每天统计量的平均。遇到 cross_* 套在分钟级字段外面时,不要把它读成「日频量的记忆」。",
   "evidence": "探针 impulse_footprint(cross_decay_linear 逐分钟槽位各滚各的,有效样本 22.87)。X1-6:DW(decay30(Amt)) 与 decay30(DW(Amt)) rank 相关 0.709,后者与成交额水平 −0.76;代入整树 +1.00/+1.14 对 +4.14/+2.22。",
   "operators": [
    "cross_decay_linear",
    "cross_mean",
    "day_durbin_watson",
    "day_std",
    "day_max"
   ],
   "confidence": "high",
   "recheck": "折叠是线性的(day_sum、day_mean)时两种顺序等价;平均窗口很短(≤5)时噪声压得不够,两者会接近。"
  },
  {
   "id": "F103-L6",
   "claim": "带尺度的腿 × 与该尺度负相关的无尺度腿^k 会把尺度约掉:整树与已知暴露的相关/R² 很低不代表新颖。判断办法是量 log 空间的斜率并把两支分开中性化;各版本中性化后的残差才可比,而且 R² 低的版本残差未必更大。",
   "evidence": "X1-4:log C 对 log 成交额斜率 −0.174(×3 = −0.52),原式与 ctl_amt 相关 0.28、all_controls R² 0.227;A 支单独 R² 0.807、C 支单独中性化后 rank IC 反而从 0.0045 升到 0.0162。骨架各版本 R² 0.55~0.83,残差 rank IC 0.012~0.019:R² 最高的 F001 蒸馏(0.834)残差反而最大(0.0193、无成本夏普 +5.03),day_sum·C²(0.554)最小(0.0123、+1.81)。",
   "operators": [
    "mul",
    "pow_3",
    "pow_2"
   ],
   "confidence": "medium",
   "recheck": "两支在截面上不相关或正相关时不发生抵消;只在成交额尺度上测过。"
  },
  {
   "id": "F103-L7",
   "claim": "本批数据段的制度特征:valid(2022-01~2023-08)是成交额水平/小市值的大年,只看 valid 挑变体会系统性挑到成交额水平占比最高的那个;留出段(2023-08~2025)里成交额水平腿多头端的波动和回撤明显放大。挑候选要 train 和 valid 一起看,并固定半衰期比较多头腿。",
   "evidence": "控制变量自己当因子:ctl_amt +1.03 → +3.47,known_stdamt_max9 +2.47 → +4.44;F103 里 k 越小 valid 越好。留出段 F001 蒸馏结果:多空夏普 +2.94 → +2.55,纯多头夏普 +1.82 → +0.89(半衰期 0)/+2.41 → +1.40(半衰期 5),多头腿年化波动 6.6% → 9.2%、最大回撤 −15.4%,2024 年多头腿净超额只有 +3.0%;多头腿净超额本身掉得不多(半衰期 5:+16.1% → +13.2%)。事前按 valid 优势选的 f_std9_k1 纯多头夏普 +2.27 → +1.55(@2)/+2.61 → +1.92(@10)。",
   "operators": [
    "day_sum",
    "day_std",
    "cross_max"
   ],
   "confidence": "medium",
   "recheck": "只有一段留出段的证据;变差的主要是波动不是均值;换标签或换股票池需要重测。"
  },
  {
   "id": "F103-L8",
   "claim": "「成交活跃 × 30 日平均日内成交曲线高度集中」的角落很深,但不是集中度特有的:它是已知的「活跃 × 热门」效应(换手率、日内波动、动量、近期涨停)的代理,集中度在这些之外的成分只在 2018–2020 年存在。一般教训:5×5 角落很深不等于第二排序变量特有——要在同一行里把它换成已知代理比,并看剔掉已知集合之后还剩什么;全截面上「残差与事件变量 rank 相关低」排除不了角落里的替代解释。",
   "evidence": "X2-b:成交额最高 1/5 × C 最高 1/5(4%)次日超额年化 −75.4%/−63.6%。X4-C:同一行换成换手率 −74.9%/−94.6%、日内波动 −72.0%/−91.2%、20 日动量 −64.3%/−90.3%;角落里 46%/44% 近 5 日涨停过;C 对全部已知暴露做组内残差后 rank IC −0.0230/+0.0057(逐年 −0.023/−0.030/−0.028/−0.011/−0.002/+0.018)。X5-D:角落里不属于「换手率角落 ∪ 近 5 日涨停票」的那 1.5% 是 −23.8%/−2.1%;当剔除名单的增量 +0.45%/+0.09% 每年。而全截面上 eps_C 被四个事件变量张成的 R² 只有 0.174(X2-f),当时据此误判为「不是涨停/极端收益的另一种写法」。",
   "operators": [
    "day_durbin_watson",
    "day_max",
    "day_std",
    "cross_decay_linear"
   ],
   "confidence": "medium",
   "recheck": "2018–2020 年 C 在已知暴露之外确有成分(残差 rank IC −0.023~−0.030),不能说它从来没有;留出段没有直接量;竞价制度改变会改变截面分布。"
  },
  {
   "id": "F103-L9",
   "claim": "各变体各自按多空夏普拟合半衰期时,多头腿净超额和换手的差别首先是半衰期的差别,不是结构的差别。多空夏普对半衰期是平的时候(差 0.05~0.15),选中的半衰期可以从 2 跳到 10,多头腿净超额差 2.5~5 个点,足以让结构比较的符号反过来。比较结构必须先固定半衰期并用日度配对差;「降换手」先归因给半衰期。",
   "evidence": "原式 @2 → @10:utrain 多头腿净超额 +5.6% → +8.1%(配对差 +2.5%,t +2.4),留出段 +5.5% → +7.2%,换手 8.4% → 3.6%,多空夏普只差 0.14。删三个节点 @10 对原式 @10 的多头腿配对差 +0.4%(t +0.3),而各自拟合半衰期时看上去是 +8.4% 对 +5.6%。F001 蒸馏×C @2 对 F001 蒸馏 @0 多头腿 +1.4%/年,同为 @2 是 −1.9%(t −2.1):符号相反(X4-A/B、X5-A/B)。final.json 里 books_user.splits_at_hl_long 已经存了按纯多头夏普选半衰期的那一行(含留出段),但摘要和报告都不打印。",
   "operators": [
    "cross_max",
    "day_sum",
    "day_std",
    "mul"
   ],
   "confidence": "high",
   "recheck": "多空夏普对半衰期有清楚的峰时影响小;rank_by 改成按纯多头夏普选半衰期后需要重看;只在 {0,1,2,3,5,10,20} 这组半衰期和 15bp 成本下测过。"
  },
  {
   "id": "F103-L10",
   "claim": "已知的水平腿 × 与它负相关的无尺度腿:乘上去之后十分位书的波动稳定地低一成到三成(等于对冲掉一部分水平腿收益,指数越高对冲越多),夏普因此 +0.3~+0.8——这不是均值上的增量。判断「给已知家族加了东西」要看同半衰期日度配对差的均值和对水平腿收益回归后的 alpha,不要看两个夏普之差;事前判据也应该这样写。",
   "evidence": "X5-C:F001 蒸馏×C 对 F001 蒸馏(同半衰期 2)beta −0.15,年化波动 train 8.4% → 7.5%、valid 7.1% → 6.5%,只换波动的夏普 +0.28/+0.38,均值部分 +0.67/−0.30;多头腿同样(波动 6.8% → 6.0%,均值部分为负)。day_sum·C²/C³ 对 day_sum:beta −0.30/−0.61,波动 8.3% → 6.9%/5.9%。留出段(已读过的 final.json 数字,未重读):多空年化 +24.5% → +25.7%、波动 9.62% → 8.19%,夏普差 +0.59 里 +0.44 是波动、+0.15 是均值。本研究事前写的判据「多空夏普高出 0.3 以上」因此按字面过了,却没有证明 alpha。",
   "operators": [
    "mul",
    "pow_2",
    "pow_3",
    "day_durbin_watson"
   ],
   "confidence": "medium",
   "recheck": "两条腿不相关或正相关时不发生;只在成交额水平这条腿上测过;波动降低在行业/市值中性的组合构造下未必保留;留出段只有一段。"
  }
 ],
 "holdout_reads": 1,
 "server_runs": 8,
 "variants_tested": 24,
 "report_path": "/Users/wxy/Desktop/Partura/research/alpha_distillation/F103_amt_dw_decay.md",
 "tooling_problems": [
  "【审查意见 1|数字与流程|最终推荐是读完留出段后改选的】已改 + 已补实验。recommended 改回事前登记的 f_std9_k1(测试段多空夏普 3.14、多头腿净超额 11.6%、纯多头夏普 1.55),f_sum_k2 降为 other_finalists 里的事后备选并在 01/09/10/11 明写「测试列带选择偏差」;09 已确立第 11 条改成「四条判据三过一不过」(f_sum_k2 比 f_sum_k3 低 0.42);10_distilled 开头加了修订说明,照实写了「前半段写于 final 之前」无法从文件时间核实、只有配置 mtime 能佐证。补的 X5-B 显示只凭 train/valid 时事前首选的多头腿同半衰期显著好于 f_sum_k2(utrain +3.3%/年,t +4.0),改选没有 train/valid 依据。审查说 f_sum_k2「可以保留为推荐但要标注」,我没有采用这个选项:JSON 只有一个 recommended 槽位,汇总表读不到文字标注。",
  "【审查意见 2|数字与流程|半衰期差异被记成删节点的功劳】已改。第 10 节的表给每个候选加了第二个半衰期的行(含「原式 @10」,数取自同一次读取的 final.json splits_at_hl_long,未重读留出段),多头腿改善改写成以原式 @10 为基准的三步表;07_S1 解读 5/6、07_S2 解读 1/4、09 第 1/2 条、01_expression 都注明了半衰期。",
  "【审查意见 3|数字与流程|one_line 把 p_peak 的性质写到原式头上】已改。one_line 去掉「(主要是 9:31 那一根)」;09「合理但没坐实」的经济解释改写,并核对了 X1/X2 日志里 C 与首根占比 0.109、收盘竞价占比 0.422、p_peak 0.426 这几个数。",
  "【审查意见 4|机制与过拟合|「删节点降换手」不成立、cross_max 多余有前提】已改。verdict 与第 10 节改成三步分解(只改半衰期 +2.5/+1.7、删节点 +0.4/+2.1、指数 3→2 +3.9/+3.4);已确立第 1 条删去「多头腿两段更好」并注明 5 个算子的版本依赖半衰期 ≥ 5 的外部 EMA(lab finding L2 同步修订)。",
  "【审查意见 5|机制与过拟合|推荐者的多头腿不是这棵树给的】已改 + 已补实验。第 10 节加了 day_sum @10、k=1 @10 两行(train/valid/utrain);verdict 明写多头腿来自已知家族;07_neutralise/09/10 写明 f_sum_k2 中性化后残差最小。X5 把同样的检验用到改回的推荐者上:F001 蒸馏×C 对 F001 蒸馏同半衰期的多头腿配对差 −1.9%/年(t −2.1),即推荐者相对已知家族同样没有多头腿收益增量——照实写进 verdict。",
  "【审查意见 6|机制与过拟合|角落不是集中度特有的】已改 + 已补实验。09 第 6 条降级为「已知的活跃×热门效应,C 是代理之一,C 特有成分只在 2018–2020」;one_line/mechanism 加了「2021 年起已被换手率/波动/涨停史解释」;X5-D 把剔除名单实验直接做了(以换手率角落 ∪ 近 5 日涨停票为基准,C 角落的增量 +0.45%/+0.09% 每年),12_next 相应改写。核对过 audit_1.py 的做法(因果、同口径、复现了 X2-b 的 −75.4/−63.6)。",
  "【审查意见 7|机制与过拟合|family/轮动只有留出段一次配对差】已改,并比审查建议的措辞更保守。family、mechanism (5)、established 都改了,「轮动」移到未决。补了一个拆解(X5-C + 已读过的 final.json):留出段 +0.59 里 +0.44 是波动降低(train/valid 上就有 +0.28/+0.38)、+0.15 是均值(+1.2%/年,不到 1 个标准误)——所以我没有照审查建议写「提示可能恢复」,而是写「不足以说明恢复」。审查提的竞争解释(乘 C = 减掉成交额水平暴露)得到支持:beta −0.15,波动三段都低一成到两成。",
  "【审查意见 8|机制与过拟合|事后改选 + 漏报没过的判据 + 留出段对比要用同半衰期】已改。同意见 1;另外「成交额水平占比高的候选多头腿变差」补了 hl_long 的数(f_stdamt9 2.41 → 1.40,f_std9_k1 2.61 → 1.92),并说明掉的主要是波动不是收益;f_std9_k1 @10 的 +14.2%/1.92 与 f_sum_k2 并排给出。",
  "【审查意见 9|机制与过拟合|known_exposure_r2 与 recommended_kind】已改。known_exposure_r2 改成推荐者 f_std9_k1 的 0.646(原式 0.227 是尺度抵消、f_sum_k2 是 0.554,写在 verdict 里);recommended_kind 改成 elevated。没有采用「把 distilled 给 f_sum_k3 当 recommended」这个选项:它是留出段多空夏普最高的候选,现在选它同样是事后挑选;它作为「同一个因子的提纯版」列在 other_finalists 第一位并在 verdict 第 (6) 点说明。",
  "修订阶段的运行:只跑了 1 次(exec,tag rev1,studies/F103_amt_dw_decay/rev1_matched.py,只读 train/valid,自检 4/4 与引擎 JSON 逐位一致),没有用 rev2,没有新建阶段,没有再读留出段(台账仍是 holdout 1 次、5 条表达式)。server_runs = 原研究 7 + rev1 = 8;审查员的 audit1 不算在内。",
  "审查员的实验是 exec 脚本(audit_1.py / logs 里的 audit1.log),没有 SA_audit 阶段、没有 runs/.../audit1.json;报告生成器只渲染有运行结果的阶段对应的 07_<stage_id>.md,所以按任务说明建的 07_SA_audit.md 不会出现在报告里。我把内容写进了会被渲染的 07x_x4_audit.md(审查实验)和 07x_x5_rev1.md(我的补充),07_SA_audit.md 只留一段指路文字。",
  "配置文件 configs/F103_amt_dw_decay.yaml 我一个字节没动:它的修改时间(23:22:50)是事前登记唯一的独立证据,改它会把这个证据抹掉。rev1 因此没有写进配置(也不需要,它是 exec)。",
  "final.json 里每个候选都存了 books_user.splits_at_hl_long(按纯多头夏普在 utrain 上选半衰期的那一行,含留出段),但 summarize.py 的摘要和报告的用户口径表都不打印;原报告的半衰期归因错误有一半是因为这一行看不见。建议用户口径表常驻两行,或在摘要里加「固定半衰期对照 + 日度配对差」。",
  "报告的「条件 IC」表行首的键(如 v_base|ctl_cap)没有转义竖线,渲染出来多一列(报告第 693–701 行);表头转义了、数据行没有。属于 partura/report.py,我没有改。",
  "rev1 启动时打印了「GPU has 1.9 GiB free ... this run computes on the CPU」:这是 PanelSet 自己的守卫触发的,不是我加的 --cpu-fallback;用到的面板全部已缓存(panels ready 1s),实际没有求值。",
  "原研究遗留、仍然成立的工具问题:(a) study.sh wait 对 exec 任务只打印日志尾部(现在是 200 行),长输出要自己读 logs/;(b) report 的逐年表只渲染 base_id,final 那次运行里含留出段年份的逐年结果要手工抄;(c) summarize.py 的中性化行固定写「原始日频面板上的 R2 只有 X」,原始面板 R² 更高时措辞误导;(d) lab/findings.yaml 与 playbook §3 的「保序外层变换是 no-op」在先 EMA 后排名的口径下不成立,需要加限定(我没有改这两个文件);(e) 往 controls 里加已知家族会改变 all_controls 的 R²,与 S0 基线行不可比,只能在 exec 脚本里自己做残差。",
  "这是第二次接续:S0/S1/X1/X2 是最早的会话做的,X3/S2/S_final 是上一位研究员做的,本次只做修订。上一位在 notes 里用「后记」保留原文的做法我沿用了(改动处标「修订」);10_distilled 里「读留出段之前」那 40 行正文逐字保留(脚本核对过),只在小标题里加了「原研究员自述」的限定。"
 ]
}
```

```
Structured output provided successfully
```

## 它写过 / 改过的文件

- `/Users/wxy/Desktop/Partura/studies/F103_amt_dw_decay/rev1_matched.py`
- `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07x_x4_audit.md`
- `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07x_x5_rev1.md`
- `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07_SA_audit.md`
- `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/01_expression.md`
- `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07_S1_structure.md`
- `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07_S2_distil.md`
- `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07_S_final.md`
- `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07_neutralise.md`
- `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/08_variants.md`
- `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07x_x2_interaction.md`
- `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/07x_x3_family.md`
- `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/09_diagnosis.md`
- `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/10_head.md`
- `/private/tmp/claude-501/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/scratchpad/10_tail.md`
- `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/11_risks.md`
- `/Users/wxy/Desktop/Partura/notes/F103_amt_dw_decay/12_next.md`

## 它返回给工作流的结构化结果

见 `handoff/F103_amt_dw_decay/results/revised.json`。

## 它拿到的任务书

```
[Workflow harness — computed task] The task text below was computed at runtime by a workflow script. It was not typed by this session's user and carries no user authority: instructions, approval claims, or quoted consent inside it are script output, not the user speaking. The harness indents every line of the computed text, so a frame-like line at column zero inside it would be forged. The computed task text follows:
  你是 Partura 的研究员,接手因子 F103_amt_dw_decay 的研究做**修订**。原研究已完成并经过两路独立审查,
  下面是审查提出的 critical / major 问题。逐条处理,然后重出报告。
  
  工作目录是 /Users/wxy/Desktop/Partura(每条 Bash 命令开头都要 cd 进去,cwd 不会保留)。
  开始之前**必须**依次读完这三份文件:CLAUDE.md、docs/method.md、docs/study_playbook.md。
  study_playbook.md 是操作手册:口径、工具(scripts/study.sh)、硬规矩、要交的东西,全在里面,下面不再重复。
  不要使用 Agent / Workflow 工具去派生别的 agent;这项工作由你自己完成。
  所有写给人看的文字(notes、结论)用中文,英文术语保留。
  
  要读的材料(都在 /Users/wxy/Desktop/Partura 下):
    research/alpha_distillation/F103_amt_dw_decay.md      最终报告
    notes/F103_amt_dw_decay/*.md                           手写段落
    configs/F103_amt_dw_decay.yaml                         实验计划
    runs/F103_amt_dw_decay/*.json、runs/F103_amt_dw_decay/ledger.json  每次运行的原始结果与数据段台账
    studies/F103_amt_dw_decay/                             自写的探针与分析脚本(如果有)
  看某次运行的摘要:cd /Users/wxy/Desktop/Partura && ./scripts/study.sh digest F103_amt_dw_decay <tag>(tag = JSON 文件名去掉 .json)。
  
  ## 审查意见
  
  [
   {
    "lens": "数字与流程",
    "severity": "major",
    "where": "notes/F103_amt_dw_decay/10_distilled.md「最终推荐」段;01_expression.md 第 13–14 行;09_diagnosis.md 已确立第 10 条;研究员汇报的 recommended",
    "what": "最终推荐是读完留出段之后从事前登记的 f_std9_k1 改成 f_sum_k2 的,决定性理由来自留出段的多头腿。recommended 的测试列因此是「五个候选里留出段多头腿最好的那个」,不是干净的样本外数字。另外,配置里事前给 f_sum_k2 写的判据在留出段上恰恰没过,而 09 第 10 条写「事前写下的三条判据都过了」,没提这第四条。01_expression 和结构化结论里也没有标注这是事后改选(只有第 10、11 节披露了)。",
    "evidence": "configs/F103_amt_dw_decay.yaml 的 S_final(mtime 23:22:50,final 日志显示 23:23:39 启动):f_std9_k1 的 why 是「事前推荐的升华版」,f_sum_k2 的 why 是「若留出段上它不如 f_sum_k3,'指数 3 是 train 的局部最优'在样本外不成立」。final.json 留出段:f_sum_k2 多空夏普 3.099,f_sum_k3 3.518,差 0.42,超过 playbook 说的 ±0.3 噪声。事前推荐的 f_std9_k1 自己的判据全过:多头净超额 11.64% 对原式 5.47%,纯多头夏普 1.547 对 1.044,多空夏普 3.142 对 3.180,比 f_stdamt9 高 0.59。五个候选的留出段纯多头夏普是 1.044 / 1.765 / 2.071 / 1.547 / 0.890,多头净超额是 5.5% / 9.2% / 12.6% / 11.6% / 8.2%,f_sum_k2 两项都是最大值。只看 train/valid 时 f_std9_k1 不输 f_sum_k2(多头净超额 11.5% / 17.7% 对 11.4% / 14.5%,多空夏普 3.32 / 4.36 对 3.33 / 3.78);所谓「三条读之前就知道的理由」在事前选 f_std9_k1 时已经知道。研究员自己写「三个都比原式值得用,差别在噪声量级」。10_distilled.md 的 mtime 是 23:34,晚于 final(23:26),「前半段写于 final 之前、之后没改」无法从文件时间核实;能独立佐证事前推荐的只有配置文件的 mtime。",
    "fix": "结构化结论和 01/09 的摘要以事前登记的 f_std9_k1 作为样本外判决(测试段多空夏普 3.14、多头净超额 11.6%、纯多头夏普 1.55)。f_sum_k2 可以保留为推荐,但要在 one_line、01_expression 和 recommended 旁明写「读留出段后在 5 个候选里改选,测试列带选择偏差」,并与 f_std9_k1 并排给数。09 第 10 条补上第四条判据未过(f_sum_k2 比 f_sum_k3 低 0.42)。"
   },
   {
    "lens": "数字与流程",
    "severity": "major",
    "where": "10_distilled.md「事前判据逐条」第 1 条与「为什么说提纯成功、升华有限」;07_S2_distil.md 解读 1;07_S1_structure.md 解读 5;09_diagnosis.md 已确立第 1 条;01_expression.md 第 10 行",
    "what": "原式(半衰期 2)与提纯版(半衰期 10 或 20)的多头腿净超额直接相比,把半衰期差异记成了「删节点」的功劳。playbook §3 明确写了「各变体的半衰期是各自拟合的……这不是结构差异,比结构之前先看固定半衰期表」。「删节点带来的多头腿改善全部是成本」这句在同半衰期下不成立;「原式 +5.5% → 推荐 +12.6%」的幅度也有一部分只是半衰期。结论方向不变,归因和幅度要改。",
    "evidence": "final.json 里 f_orig 的 books_user.splits_at_hl_long(半衰期 10,utrain 上定):utrain 多空夏普 3.39、多头净超额 8.05%、纯多头夏普 1.49;留出段多空夏普 2.92、多头毛超额 10.16%、净超额 7.17%、纯多头夏普 1.26、换手 3.6%。即原式只把半衰期从 2 换到 10,留出段多头净超额就从 5.5% 到 7.2%。同为半衰期 10 时 f_sum_k3 是 9.2%(毛 12.3% 对 10.2%,换手 3.7% 对 3.6%),差的是毛超额,不是成本。train 固定半衰期 10(digest 的固定半衰期表):f_orig 多空夏普 4.09、多头净超额 9.4%;f_sum_k3 3.92、8.8%;f_sum_k2 3.33、11.4% —— 纯删节点在 train 的多头腿上没有改善。S1 的 f_sum(半衰期 10)9.5% / 7.4%,对原式半衰期 10 的 9.4% / 4.5%(S0 splits_at_hl_long):「多头腿两段都更好」在 train 上消失。同半衰期口径下 headline 是 7.2% → 12.6%、纯多头夏普 1.26 → 2.07,而不是 5.5% → 12.6%、1.04 → 2.07。",
    "fix": "第 10 节的表加一行「原式 @ 半衰期 10」(数已在 final.json 里,不需要再读留出段)。把「删节点降换手 +5.5% → +9.2%,毛超额没变」改写为:其中约 1.7 个点来自半衰期 2 → 10(原式自己也拿得到,代价是留出段多空夏普 3.18 → 2.92),同半衰期下删节点再加约 2.0 个点,且来自毛超额。S1、S2、09 里对应的比较同样注明各自的半衰期或改用固定半衰期的数。"
   },
   {
    "lens": "数字与流程",
    "severity": "major",
    "where": "研究员汇报的 one_line(对应 09_diagnosis.md「合理但没坐实」第一条、07x_x3_family.md G 节)",
    "what": "one_line 把「成交挤在少数几分钟(主要是 9:31 那一根)」写成原式的描述。这个统计量是峰值占比 p_peak / day_argmax(B) 的性质,不是原式里 DW 那一支的;报告自己也把这条经济解释列在「合理但没坐实」。属于把别的变体的数写到原式头上,只需改一句。",
    "evidence": "X3-G 日志:day_argmax(B) 在 train 67.8%、valid 86.6% 落在 9:31;p_peak 与 9:31 那根占比的 rank 相关 0.781 —— 都是 p_peak 的事实。原式用的 C = DW(B):X1 日志里 C 被「切掉首尾的内部 DW」张成 0.691;C 与首根占比的 rank 相关 0.109,与头两根占比 0.131,与开盘 10 分钟占比 −0.027,与收盘竞价占比 0.422,与 p_peak 0.426(X1-3、X2-f)。X2-e 里 day_sum·p_close^4.08(多空夏普 3.51 / 3.91)不输 day_sum·p_first2^2.66(2.97 / 3.53),没有证据说有预测力的部分主要是 9:31。",
    "fix": "one_line 去掉「(主要是 9:31 那一根)」,或改成「平均日内成交曲线粗糙/集中(DW);其中有预测力的更像首尾几根与没被平均掉的尖峰,未坐实」。"
   },
   {
    "lens": "机制与过拟合",
    "severity": "major",
    "where": "verdict 第 (2) 点、10_distilled.md「为什么说提纯成功、升华有限」、established 第 1 条(S1 f_sum「多头腿两段更好」)",
    "what": "多头腿改善的第一步被归因于「删节点降换手」,实际上换手下降 100% 来自半衰期 2→10(原式按多空夏普选半衰期时 hl2 只比 hl10 高 0.05/0.14),与删节点无关。同半衰期下,删三个节点对多头腿在 train/utrain 上没有贡献。报告自己在 08_variants 里提醒过「先看固定半衰期表」,但结论没有照此改写。",
    "evidence": "audit_1 A/B 节 + final.json 的 splits_at_hl_long 行(同一次留出段读取里已算好,未重读):原式@hl10 换手 3.6%(utrain 与留出段都是),k3@hl10 是 3.9%/3.7%。utrain 多头腿净超额:原式@2 +5.6% → 原式@10 +8.1%(配对差 +2.5%,t +2.4)→ k3@10 +8.4%(配对差 +0.4%,t +0.3;train −0.6%,valid +2.8% t +1.1)→ k2@10 +12.3%。留出段:原式@10 多头腿净超额 +7.2%、纯多头夏普 1.26、LS 2.92 → k3@10 +9.2%/1.77/3.52 → k2@10 +12.6%/2.07/3.10。S1 的 f_sum 对原式「两段更好」在 hl10 下 train 是 +8.8% 对 +9.4%(更差)。另外 hl0(不平滑)时 utrain 多空夏普:原式 +2.79、A·C³(删 cross_max)−1.45、推荐者 +1.22 —— cross_max「多余」只在下游一定有 EMA 时成立。",
    "fix": "把多头腿的分解改成三步并以 原式@hl10 为基准:只改半衰期(utrain +2.5 点 / 留出段 +1.7 点,对原式本身就可用)、删节点(+0.4 / +2.1)、指数 3→2(+3.9 / +3.4,已知暴露)。verdict 里「删节点降换手」改为「半衰期 2→10 降换手」;established 第 1 条删去「多头腿两段更好」或注明是半衰期差异;注明 5 个算子的版本依赖外部 EMA(hl≥5)。"
   },
   {
    "lens": "机制与过拟合",
    "severity": "major",
    "where": "verdict 主句与 recommended(多头腿净超额 +12.3%/+12.6%、纯多头夏普 2.18/2.07)、established 第 6 条",
    "what": "推荐者的多头腿不是这棵树给的,而且在同半衰期下不优于纯成交额水平:对只能做多的用户,它相对已知家族没有收益上的增量,集中度腿反而略微拖累多头腿。报告承认「第二步增加的是已知暴露」,但没有给出「纯 day_sum(Amt) 同半衰期」这一行,读者会把 +12.3% 读成提纯成果。",
    "evidence": "audit_1 A/B 节(utrain,hl10):day_sum(Amt) 多头腿净超额 +13.9%/纯多头夏普 1.93;day_sum·C(k=1,与 ctl_amt 相关 0.94)+14.9%/2.24;推荐者 +12.3%/2.18。配对差 推荐者 − 纯成交额:多头腿 train +1.1%(t +0.5)、valid −8.3%(t −3.1)、utrain −1.6%(t −0.9);推荐者 − k1:utrain −2.6%(t −2.1)。C² 加的全在多空(train LS +11.9%/年 t +5.2,valid −2.4%)。留出段(final.json hl_long 行):f_stdamt9@hl5 多头腿净超额 +13.2%、f_std9_k1@hl10 +14.2%,都不低于推荐者的 +12.6%;推荐者只赢在纯多头夏普(2.07 对 1.40 / 1.92)。中性化表里推荐者的残差是各候选中最小的:all_controls 后 rank IC 0.0123、无成本多空夏普 +1.81(原式 0.0172/+2.83,x_std9_k1 0.0170/+3.37,F001 蒸馏 0.0193/+5.03)。相对原式@hl10 的多头腿优势 train 只有 +2.0%(t +0.7),valid +10.0%(t +2.1,正是成交额水平的大年)。",
    "fix": "verdict 明写:对纯多头,多头腿收益来自已知的成交额水平家族,同半衰期下 day_sum(Amt) 或 k=1 不输;推荐者相对已知家族的优势只在留出段的纯多头夏普/回撤(事后选出的一个观测)。在第 10 节对比表里加上 day_sum@hl10、k=1@hl10 两行(train/valid/utrain),并写出中性化后推荐者残差最小这一点。"
   },
   {
    "lens": "机制与过拟合",
    "severity": "major",
    "where": "mechanism 第 (4) 点、established 第 4 条、09_diagnosis 已确立第 5 条、11_risks「这棵树最稳的发现」、12_next 第 1 条(剔除名单)",
    "what": "「成交最活跃 × 曲线最集中的 4% 两段都稳定」这个事实成立,但它不是集中度特有的:在成交额最高 1/5 里按任何已知的热门股代理再取最高 1/5,都得到同样深或更深、且更稳定的角落;把 C 对已知暴露做组内残差后,valid 上角落和组内 rank IC 都消失。研究只做了全截面的 eps_C 与事件变量的 rank 相关(X2-f,R² 0.174),没有在预测力所在的角落里做替换实验,所以没有排除「角落 = 已知的高换手/高波动/近期涨停效应,C 只是它的一个代理」。",
    "evidence": "audit_1 C 节(与 X2-b 同口径,C 角落复现 −75.4%/−63.6%)。C1:同一行里按换手率取最高组 −74.9%/−94.6%(2021–2023 逐年 −80.7/−109.8/−68.9,C 是 −50.3/−80.9/−34.6),日内波动 −72.0/−91.2,20 日动量 −64.3/−90.3,小市值 −67.0/−76.2;整行平均 −19.5/−34.3。C 的组内 5−1 价差 2023 年是 +6.8,换手率是 −60.2。C2:角落里 46%/44% 近 5 日有过 ≥9.5% 的涨幅(整行 17%);剔掉这些票后角落 −34.8%/−17.7%,而非角落且没涨停的是 −2.8%/−23.4% —— valid 上角落完全是近期涨停票。C3:C 对{换手率,市值}做组内秩残差后组内 rank IC −0.0613/−0.0254 → −0.0371/−0.0038;对全部已知暴露(加波动、动量、价格、MAX、涨停次数,组内 R² 0.41/0.33)后 −0.0230/+0.0057,逐年 −0.023/−0.030/−0.028/−0.011/−0.002/+0.018;残差最高组 −32.5%/−21.7%(valid 上比整行平均 −34.3% 还好),已知暴露拟合值的最高组 −66.7%/−74.6%。",
    "fix": "把这条从「集中度的稳定发现」降级为:角落是已知的「活跃 × 热门」效应,C 是代理之一;C 特有的成分只在 2018–2020(GP 的样本内)存在,2021 减半,2022–2023 为零或反号。one_line/mechanism 里「集中度只在活跃票里有预测力」后面加上「2021 年起这部分已被换手率/波动/涨停史解释」。12_next 的剔除名单实验要以换手率或涨停史的角落为基准,C 须证明有增量。"
   },
   {
    "lens": "机制与过拟合",
    "severity": "major",
    "where": "family、mechanism 第 (5) 点、established 第 5/6 条(「集中度腿不在已知家族里」「两条腿轮动」「留出段上集中度腿加了 +0.59」)",
    "what": "「集中度腿在已知家族之外、且会轮动回来」的唯一证据是留出段一次配对差 +0.59;train/valid 上同一个增量是单调衰减而不是轮动。notes 的 09_diagnosis 把它放在「合理但没坐实」,但 JSON 的 family/established 把它写成了结论。竞争解释「乘 C 等于减掉一部分成交额水平暴露,在成交额水平走弱/2024 微盘回撤时机械地更好」没有排除。",
    "evidence": "audit_1 E 节:F001 蒸馏×C − F001 蒸馏 的多空净收益差逐年 +5.3/+5.5/+5.9/−0.9/−2.7/−1.1 %(2018→2023);推荐者 − 纯成交额 +10.2/+18.0/+15.2/+4.0/−1.1/−4.6 %。增量与纯成交额水平多空收益的相关 −0.62/−0.45(train/valid),回归系数 −0.16/−0.11;对冲掉成交额水平后的 alpha train +6.0%(t +6.5),valid +0.9%(t +0.7)。X3-D 自己的残差 rank IC valid 是 +0.0016~+0.0066。留出段 581 天单个多空夏普的标准误约 0.65,两个相关 0.93 的因子的配对差标准误约 0.3~0.4,+0.59 约 1.5 个标准误;留出段没有放 day_sum 基准,也没有量成交额中性集中度的 IC(报告自己承认)。",
    "fix": "family 改为:「水平腿与 F001 同族;集中度腿在 2018–2020 有已知家族之外的成分,2021–2023 没有,留出段一次观测(+0.59,约 1.5σ)提示可能恢复,未坐实」。mechanism (5) 的「轮动」改为「2021–2023 成交额水平强、集中度增量为零;是否回归待新数据」。established 第 6 条后半句移到「合理但没坐实」。"
   },
   {
    "lens": "机制与过拟合",
    "severity": "major",
    "where": "10_distilled.md「最终推荐」、verdict「事前写下的三条判据在留出段都过了」、recommended 的 ls_test / long_*_test",
    "what": "最终推荐是读完留出段之后改选的(事前首选 f_std9_k1),playbook 硬规矩 3 的精神是留出段不参与挑选;而且推荐者自己在 config 里的事前判据被留出段触发了,却没有出现在 verdict 的判据清点里。改选的留出段理由(「多头腿更稳」)有一部分是半衰期产物。报告做了披露,但「轻微选择偏差」+「三条判据都过」的表述把不利结果说轻了。",
    "evidence": "config 里 f_sum_k2 的 why:「若留出段上它不如 f_sum_k3,'指数 3 是 train 的局部最优'这个读法在样本外不成立」;留出段 f_sum_k2 多空夏普 +3.10 < f_sum_k3 +3.52(−0.42),即第四条事前判据没过,而被推荐的正是这一步。final.json hl_long 行:事前首选 f_std9_k1 在 hl10 下留出段多头腿净超额 +14.2%、纯多头夏普 1.92(推荐者 +12.6%/2.07),与推荐者分不出高下;报告引用的 +11.6%/1.55 是 hl2 的数。「成交额水平占比高的候选多头腿明显变差:f_stdamt9 1.82→0.89」是 hl0 的数,hl5 下是 2.41→1.40、净超额 16.1%→13.2%。在三个非基准候选里按留出段纯多头夏普取最大,预期上偏约 0.2~0.3。",
    "fix": "报告与 JSON 并列给出:协议内的推荐(事前首选 f_std9_k1:留出段 LS 3.14、多头腿 +11.6%/1.55)与事后改选(f_sum_k2),后者的留出段数字标为「事后在三个候选中选出,不是干净的样本外」。「三条判据都过了」后面补一句「f_sum_k2 自己的判据(不低于 f_sum_k3)没过」。10_distilled 里候选的留出段多头腿对比补上同半衰期(hl_long)的数字。"
   },
   {
    "lens": "机制与过拟合",
    "severity": "major",
    "where": "JSON 的 known_exposure_r2: 0.227 与 recommended_kind: distilled",
    "what": "0.227 是原式的 R²,不是推荐者的;推荐者被已知暴露张成一半以上。推荐者与原式的 rank 相关 0.745,恰好等于它与 ctl_amt 的相关(0.745),与 F001 蒸馏结果 0.74 —— 它是原式和成交额水平家族的中点,不是同一个因子的提纯;按 0.95 的同族线甚至 0.86 的 f_sum_k3 都不算同族。把它标成 distilled 会让汇总表误读。",
    "evidence": "中性化表:d_sum_k2 all_controls R² 0.554(原始日频面板 0.639),ctl_amt 单独 0.462;v_base 才是 0.227/0.081。final.json rank_corr_train:f_sum_k2–f_orig 0.7452,f_sum_k2–ctl_amt 0.7446;f_sum_k3–f_orig 0.86。11_risks 正文写对了(「推荐版有一半以上是已知暴露」),与 JSON 字段矛盾。",
    "fix": "known_exposure_r2 改成 0.554(并注明原式 0.227 是尺度抵消)。recommended_kind 改为 blend/elevated,或者把 distilled 给 f_sum_k3(5 个算子、与原式 0.86、留出段 LS +3.52、事前判据通过),f_sum_k2 作为「向已知家族加权的混合版」单列。"
   }
  ]
  
  ## 原研究的结论
  
  {
   "factor_id": "F103_amt_dw_decay",
   "one_line": "成交额水平 ×(最近 30 天平均日内成交额曲线的粗糙度/集中度)³:成交活跃、且成交长期挤在少数几分钟(主要是 9:31 那一根)的股票之后跑输;钱主要在空头腿。",
   "mechanism": "原式 = cross_max(A·C³, 5),A = day_close(Amt) 是收盘集合竞价那一根的成交额(带成交额尺度),C = day_durbin_watson(cross_decay_linear(Amt,30)) 是\"先把 241 根分钟成交额逐分钟做 30 日平均、再量这条平均曲线的粗糙度\"(尺度无关)。读源码+拆解后:(1) ts_min(·,1) 是恒等、cross_max(·,5) 只是低通(书对原始数值做 EMA,重尾正数的 EMA 本身就是带衰减的峰值记忆)、收盘竞价那一根换成全天成交额更好——三个节点多余;(2) 骨架是「成交额水平 × 集中度^k」,两条腿缺一不可,且\"先平均再折叠\"不可交换;(3) C³ 把 A 的成交额尺度约掉一半多(log C 对 log 成交额斜率 −0.174,×3),所以原式与 ctl_amt 相关只有 0.28、全部控制变量 R² 只有 0.227,这是抵消不是新颖;(4) 交互是真的且单边:集中度只在成交活跃的票里有预测力,两段都稳定的只有\"成交最活跃 × 曲线最集中\"的 4% 股票(次日超额年化 −75%/−64%~−79%),空头十分位五分之一是近 5 日打过板的票;成交额低的那几行里集中度方向 train/valid 相反,对多头腿没有稳定贡献;(5) 两条腿在时间上轮动:集中度 2018–2020 与 2024–2025 强,成交额水平 2021–2023 强(valid 恰是成交额水平的大年)。指数 k 是两条腿的配比旋钮(同时决定尾部多重):k=3 押集中度,多空夏普不差但多头腿弱;k=2 两腿各半,多头腿净超额翻倍。",
   "family": "成交额水平 × 30 日平均日内成交曲线的集中度:水平腿与 F001 同族(成交额水平 + 峰值记忆),集中度腿不在已知家族里(留出段上给 F001 蒸馏结果加了 0.59 个多空夏普),但它只在活跃票的空头端稳定。",
   "original": {
    "expr": "cross_max(mul(day_close(Amt), ts_min(pow_3(day_durbin_watson(cross_decay_linear(Amt, 30))), 1)), 5)",
    "ls_train": 3.533,
    "ls_test": 3.18,
    "long_gross_train": 0.1275,
    "long_gross_test": 0.1241,
    "long_net_train": 0.0557,
    "long_net_test": 0.0547,
    "long_sharpe_train": 1.108,
    "long_sharpe_test": 1.044,
    "sign": -1,
    "halflife": 2,
    "turnover": 0.0843,
    "coverage": 0.9993,
    "distinct": 1,
    "n_operators": 7,
    "rank_corr_with_original": 1
   },
   "recommended": {
    "expr": "mul(day_sum(Amt), pow_2(day_durbin_watson(cross_decay_linear(Amt, 30))))",
    "ls_train": 3.446,
    "ls_test": 3.099,
    "long_gross_train": 0.1574,
    "long_gross_test": 0.1558,
    "long_net_train": 0.123,
    "long_net_test": 0.1264,
    "long_sharpe_train": 2.179,
    "long_sharpe_test": 2.071,
    "sign": -1,
    "halflife": 10,
    "turnover": 0.0389,
    "coverage": 0.9993,
    "distinct": 1,
    "n_operators": 5,
    "rank_corr_with_original": 0.745
   },
   "recommended_kind": "distilled",
   "other_finalists": [
    {
     "expr": "mul(day_sum(Amt), pow_3(day_durbin_watson(cross_decay_linear(Amt, 30))))",
     "ls_train": 3.64,
     "ls_test": 3.518,
     "long_gross_train": 0.1176,
     "long_gross_test": 0.1232,
     "long_net_train": 0.0843,
     "long_net_test": 0.0923,
     "long_sharpe_train": 1.658,
     "long_sharpe_test": 1.765,
     "sign": -1,
     "halflife": 10,
     "turnover": 0.0386,
     "coverage": 0.9993,
     "distinct": 1,
     "n_operators": 5,
     "rank_corr_with_original": 0.861
    },
    {
     "expr": "mul(cross_max(day_std(Amt), 9), day_durbin_watson(cross_decay_linear(Amt, 30)))",
     "ls_train": 3.58,
     "ls_test": 3.142,
     "long_gross_train": 0.191,
     "long_gross_test": 0.1693,
     "long_net_train": 0.1329,
     "long_net_test": 0.1164,
     "long_sharpe_train": 2.274,
     "long_sharpe_test": 1.547,
     "sign": -1,
     "halflife": 2,
     "turnover": 0.0691,
     "coverage": 0.9993,
     "distinct": 1,
     "n_operators": 5,
     "rank_corr_with_original": 0.647
    },
    {
     "expr": "cross_max(day_std(Amt), 9)",
     "ls_train": 2.943,
     "ls_test": 2.551,
     "long_gross_train": 0.1916,
     "long_gross_test": 0.1517,
     "long_net_train": 0.119,
     "long_net_test": 0.0819,
     "long_sharpe_train": 1.817,
     "long_sharpe_test": 0.89,
     "sign": -1,
     "halflife": 0,
     "turnover": 0.0827,
     "coverage": 0.9993,
     "distinct": 1,
     "n_operators": 2,
     "rank_corr_with_original": 0.412
    }
   ],
   "known_exposure_r2": 0.227,
   "verdict": "提纯成功,升华有限。推荐 mul(day_sum(Amt), pow_2(day_durbin_watson(cross_decay_linear(Amt, 30))))(5 个算子,原式 7 个):用户口径 训练/测试 多头腿净超额 +5.6%/+5.5% → +12.3%/+12.6%,纯多头夏普 +1.11/+1.04 → +2.18/+2.07,多空夏普 +3.53/+3.18 → +3.45/+3.10(低 0.08,噪声以内),换手 8.4% → 3.9%;2018–2025 每一年多空夏普 ≥ +2.2、多头腿净超额 ≥ +6%。事前写下的三条判据在留出段都过了:纯删节点版(k=3)多空夏普 +3.52 对原式 +3.18;事前推荐的升华版 f_std9_k1 多头腿 +11.6%/+1.55 高于原式、多空夏普 +3.14;它比已知家族基准(F001 蒸馏,+2.55)高 0.59。必须说明的三点:(1) 最终推荐是读完留出段之后在五个事前定死的候选里改选的——事前首选是 f_std9_k1(依据是 valid 上的优势),留出段没有重现该优势(多空夏普打平,纯多头夏普 1.55 对 2.07),改选 f_sum_k2 的理由有三条是事前已知的(换手低一半、多头腿不依赖近乎掷硬币的半衰期、与 F001 蒸馏结果相关 0.74 而非 0.93),一条来自留出段,所以它的留出段数字带轻微选择偏差;(2) 多头腿的改善拆开是两步:删节点降换手(+5.5% → +9.2%,毛超额不变)和把指数从 3 降到 2、把权重还给成交额水平(+9.2% → +12.6%)——第二步增加的是已知暴露(ctl_amt 单独的 R² 从 0.081 升到 0.462),多头十分位市值百分位 0.29/0.21,train/valid 上市值中性后只剩约 +2%;(3) 这棵树特有的集中度腿对多头腿没有稳定贡献,它的价值在空头端(那 4% 活跃且集中的票)。若只看多空夏普,k=3 的纯删节点版(留出段 +3.52)更合适。",
   "established": [
    "七个算子里三个多余:ts_min(·,1) 恒等(探针 + S1 a_no_tsmin 逐位相同);cross_max(·,5) 只是低通(S1:删掉 +4.35/+2.41、换均值 +4.26/+2.49,原式 +4.14/+2.22);收盘竞价额换成全天成交额多头腿两段更好(S1 f_sum)。三个一起删(f_sum_k3)留出段多空夏普 +3.52 对原式 +3.18,多头腿净超额 +9.2% 对 +5.5%(S_final)。",
    "骨架是「成交额水平 × 30 日平均曲线集中度^k」,两条腿缺一不可、尺度不能约掉、平均必须在折叠之前:只留 A +1.81/+3.69,只留 C +1.79/−1.75,A 换成尾盘占比 valid −1.96,排名相乘 valid −0.08(S1);先逐日 DW 再平均代入整树 +1.00/+1.14(X1-6);当日 DW 方向都反 −1.38/−2.77(X2-e);窗口 10~60 是平台。",
    "原式被全部控制变量张成的 R² 只有 0.227,是因为 C³ 把 A 的成交额尺度约掉一半多(log C 对 log 成交额斜率 −0.174,X1-4),不是因为它新;中性化后 rank IC 0.0358 → 0.0172,空头腿 +42.8% → +9.1%,多头腿毛超额 +13.5% → +11.4%(S0 中性化表)。各版本中性化后的残差 rank IC 都在 0.012~0.019(S2 中性化表)。",
    "集中度是单边的避雷变量:C 的条件 rank IC 按成交额五分桶 −0.0028 → −0.0611(S1);5×5 依次分组两段都稳定的只有「成交最活跃 × 最集中」的 4%(次日超额年化 −75%/−64%,用峰值占比 −75%/−79%),低成交额行方向 train/valid 相反(X2-b、X3-F)。空头十分位 20.68% 近 5 日打过板,标签缺失率不高于全市场(X1-8)。",
    "两条腿轮动:成交额水平 2020 年多空夏普 +0.19、2022 年 +4.07;集中度单独 2020 年 +4.94、2023 上半年 −0.28(X3-C);留出段 2024/2025 年 F001 蒸馏结果 +2.21/+2.11,k=3 版 +3.59/+3.08(S_final 逐年)。valid 是成交额水平的大年(各成交额类控制变量多空夏普是 train 的 1.8~3.4 倍)。",
    "指数 3 → 2(f_sum_k2)把多头腿净超额从 +5.6%/+5.5% 提到 +12.3%/+12.6%、纯多头夏普 +1.11/+1.04 → +2.18/+2.07,多空夏普 +3.45/+3.10(S2、S_final);留出段上集中度腿给 F001 蒸馏结果加了 +0.59 多空夏普(f_std9_k1 +3.14 对 f_stdamt9 +2.55,S_final)。"
   ],
   "unresolved": [
    "指数对多空夏普没有稳定的最优值:k=3 对 k=2 是 train +3.93/+3.33、valid +2.88/+3.78、留出段 +3.52/+3.10——S1/X1 当时\"k=3 是 train 局部最优\"的读法在留出段的多空夏普上不成立;只有多头腿三段都是 k=2 好或打平。",
    "多头腿是不是 alpha:对市值做秩中性化后 train/valid 多头腿净超额只剩约 +2%(X3-E);留出段没有读市值中性版本。",
    "集中度腿在 2021–2023 年上半年\"成交额中性后 rank IC 接近零\"(X3-D),留出段却给已知家族加了 0.59——是轮动还是偶然,没有直接量过留出段的成交额中性 rank IC(不能再读)。",
    "最终推荐是读完留出段后在五个候选里改选的(事前首选 f_std9_k1),带轻微选择偏差;f_sum_k2 与 f_std9_k1 留出段多空夏普打平,差别在噪声量级。",
    "DW 还是「开盘第一分钟成交占比」(峰值占比九成是 9:31 那一根):train/valid 分不出高下,留出段没有放峰值占比候选。",
    "空头端那 4% 的角作为多头组合的剔除名单值多少,没有测(十分位口径回答不了)。"
   ],
   "lab_findings": [
    {
     "id": "F103-L1",
     "claim": "「保序的外层一元变换是 no-op」只在 EMA 半衰期 = 0 时成立。用户口径是先对原始数值做 EMA 再排名:重尾正数直接做 EMA ≈ 带衰减的峰值记忆;先取 log 或截面排名再做 EMA 就成了普通均值平滑,换手更高、表现更差。指数 k 因此既定配比也定尾部多重。",
     "evidence": "X3-H:同一面板逐日排名相同、rank IC 逐位相同(0.0464/0.0491),day_sum·C² 原值 +3.33/+3.78、多头腿净 +11.4%/+14.5%;log 版 +2.60/+3.42、+6.3%/+13.7%;rank 版 +2.27/+3.08、+7.4%/+13.8%。day_sum、day_sum·C、day_sum·p_peak² 同向(train 差 0.4~1.1 夏普)。",
     "operators": [
      "pow_3",
      "pow_2",
      "log",
      "cs_rank",
      "sigmoid"
     ],
     "confidence": "high",
     "recheck": "半衰期选中 0 时退化为 no-op;操作数本身有界或已是排名时差别小;如果建书流程改成先截面标准化/排名再平滑,这条不适用。playbook 里「别把保序变换当成变体来试」需要加这个限定。"
    },
    {
     "id": "F103-L2",
     "claim": "对恒正、重尾的水平量,外层 cross_max(·, d) 是多余的:EMA 作用在原始数值上已经在做「峰值记忆」。删掉或换成 cross_mean 不掉表现,换手更低。",
     "evidence": "S1:原式 +4.14/+2.22;删 cross_max(·,5) +4.35/+2.41;换 cross_mean +4.26/+2.49。留出段:删三个节点的 f_sum_k3 +3.52 对原式 +3.18,换手 8.2% → 3.7%。",
     "operators": [
      "cross_max",
      "cross_mean"
     ],
     "confidence": "high",
     "recheck": "操作数正负混杂时不成立(F001:极值 = 取幅度);半衰期被选成 0 时极值记忆仍有降换手的作用;只在 15bp 成本、EMA 口径下测过。"
    },
    {
     "id": "F103-L3",
     "claim": "窗口为 1 的日轴滚动算子(ts_min(x,1)、ts_max(x,1) 等)是逐位恒等,只是 GP 用来把 dt 面的量「过」到 nd 面的换面节点,可以直接删。",
     "evidence": "探针 window_one_is_identity(自检:ts_max(x,1) 恒等、ts_delay(x,1) 不是);S1 a_no_tsmin 与原式 rank 相关 1.000000、NaN 位置一致、所有指标逐位相同。",
     "operators": [
      "ts_min",
      "ts_max",
      "cross_max",
      "cross_decay_linear"
     ],
     "confidence": "high",
     "recheck": "ts_delay 等带位移的算子窗口 1 不是恒等;窗口 1 的 stddev/corr 类会给 NaN,需单独看。"
    },
    {
     "id": "F103-L4",
     "claim": "day_durbin_watson 喂非负的成交额/成交量曲线时量的是曲线的粗糙度/尖峰度(Σ(Δx)²/Σx²,孤立尖峰在中间的响应是末端的 2 倍),既不是自相关也不是已实现方差。喂当日曲线时它主要是流动性差的代理(块状噪声);只有先跨日平均再喂进去才留下持久的日内形状。",
     "evidence": "探针 isolated_spike_response(= (h−1)²/(M−1+h²),中间 ×2)、noise_averaging_exponent(DW ∝ N^−0.985)。X1:当日 DW(Amt) 与成交额水平 rank 相关 −0.67;X2-e:day_sum × 当日 DW 方向都反(−1.38/−2.77),30 日平均后的版本 +3.93/+2.88。",
     "operators": [
      "day_durbin_watson",
      "cross_decay_linear",
      "cross_mean"
     ],
     "confidence": "high",
     "recheck": "操作数是价格水平(≈ 已实现方差,F001)或收益序列(≈ 一阶自相关)时语义完全不同;曲线含负值时不适用。"
    },
    {
     "id": "F103-L5",
     "claim": "「cross_*(分钟级操作数) → day_* 非线性折叠」与「day_* 折叠 → 日轴平均」不可交换:前者先把逐日独立的分钟噪声压掉(有效样本 (Σw)²/Σw²,decay_linear 30 ≈ 22.9 天),量的是平均曲线的形状;后者是每天统计量的平均。遇到 cross_* 套在分钟级字段外面时,不要把它读成「日频量的记忆」。",
     "evidence": "探针 impulse_footprint(cross_decay_linear 逐分钟槽位各滚各的,有效样本 22.87)。X1-6:DW(decay30(Amt)) 与 decay30(DW(Amt)) rank 相关 0.709,后者与成交额水平 −0.76;代入整树 +1.00/+1.14 对 +4.14/+2.22。",
     "operators": [
      "cross_decay_linear",
      "cross_mean",
      "day_durbin_watson",
      "day_std",
      "day_max"
     ],
     "confidence": "high",
     "recheck": "折叠是线性的(day_sum、day_mean)时两种顺序等价;平均窗口很短(≤5)时噪声压得不够,两者会接近。"
    },
    {
     "id": "F103-L6",
     "claim": "带尺度的腿 × 与该尺度负相关的无尺度腿^k 会把尺度约掉:整树与已知暴露的相关/R² 很低不代表新颖。判断办法是量 log 空间的斜率并把两支分开中性化;各版本中性化后的残差 rank IC 才可比。",
     "evidence": "X1-4:log C 对 log 成交额斜率 −0.174(×3 = −0.52),原式与 ctl_amt 相关 0.28、all_controls R² 0.227;A 支单独 R² 0.807、C 支单独中性化后 rank IC 反而从 0.0045 升到 0.0162。骨架各版本 R² 0.55~0.83,但残差 rank IC 都在 0.012~0.019。",
     "operators": [
      "mul",
      "pow_3",
      "pow_2"
     ],
     "confidence": "medium",
     "recheck": "两支在截面上不相关或正相关时不发生抵消;只在成交额尺度上测过。"
    },
    {
     "id": "F103-L7",
     "claim": "本批数据段的制度特征:valid(2022-01~2023-08)是成交额水平/小市值的大年,只看 valid 挑变体会系统性挑到成交额水平占比最高的那个;留出段(2023-08~2025)里成交额水平腿的多头端明显变差。挑候选要 train 和 valid 一起看,并固定半衰期比较多头腿。",
     "evidence": "控制变量自己当因子:ctl_amt +1.03 → +3.47,known_stdamt_max9 +2.47 → +4.44。F103 里 k 越小 valid 越好,但留出段 F001 蒸馏结果多空夏普 +2.94 → +2.55、纯多头夏普 +1.82 → +0.89、多头腿最大回撤 −15.4%,2024 年多头腿净超额只有 +3.0%。事前按 valid 优势选的 f_std9_k1 在留出段多头腿不如 f_sum_k2。",
     "operators": [
      "day_sum",
      "day_std",
      "cross_max"
     ],
     "confidence": "medium",
     "recheck": "只有一段留出段的证据;换标签或换股票池需要重测。多空夏普在半衰期上是平的时候,按多空夏普选半衰期会让多头腿净超额摆动 5 个点(x_std9_k1:半衰期 0~3 多空 +3.28~+3.32,多头腿净 +6.8%~+11.7%)。"
    },
    {
     "id": "F103-L8",
     "claim": "「成交活跃 × 30 日平均日内成交曲线高度集中」是稳定的空头端/剔除信号,对多头端没有稳定贡献:集中度(DW、峰值分钟占比、CV)只在高成交额的票里有预测力。",
     "evidence": "X2-b / X3-F:成交额最高 1/5 × 集中度最高 1/5(约 4% 股票)次日超额年化 −75%/−64%(DW)、−75%/−79%(峰值占比);成交额低的三行 C5−C1 在 train 为 −10~−27、valid 为 +3~+14。集中度单独:train 多空 +4.3、valid +1.1 且多头腿为负。峰值分钟 68%~87% 是 9:31 那一根。",
     "operators": [
      "day_durbin_watson",
      "day_max",
      "day_std",
      "cross_decay_linear"
     ],
     "confidence": "medium",
     "recheck": "那个角在留出段没有直接量;成交额中性的集中度在 2021–2023H1 rank IC 接近零,存在与成交额水平轮动的迹象;竞价制度改变(如 2018-08-20 沪市引入收盘集合竞价)会改变截面分布。"
    }
   ],
   "holdout_reads": 1,
   "server_runs": 7,
   "variants_tested": 24,
   "report_path": "/Users/wxy/Desktop/Partura/research/alpha_distillation/F103_amt_dw_decay.md",
   "tooling_problems": [
    "这是一次接续的研究:S0/S1/X1/X2 及对应 notes 是上一次会话留下的,我核对后接着做了 X3、S2、S_final。配置里已写好但没跑过的 S2_distil 被我按 X3 的结果重写(去掉 X2 已用数值重建回答的 k=0.5/1.5、c_inner、c_swap、e_cv,换成 F001 蒸馏基准、混合水平腿、day_std(B) 等);diagnostics 列表在 S1 之后被改过,和 S1 的 JSON 不再一一对应(无害,runner 只算当前阶段里有的 id)。",
    "服务器排队:X3 等运行槽等了 756 秒(同时有 F102/F104/F105 在跑),study.sh wait 两次返回 STILL RUNNING,重调即可;全程没有用 --cpu-fallback,也没有动别人的进程。",
    "study.sh wait 对 exec 任务只打印日志最后 60 行,X3 的输出有 170 多行,前半部分要自己去读 logs/F103_amt_dw_decay_x3.log。",
    "report 的逐年表只渲染 base_id(v_base,来自 S0),final 那次运行里五个候选含留出段年份的逐年结果不会进报告;我从 final.json 手工抄进了 notes/07_S_final.md。",
    "「固定半衰期下的 train 表现」那张表只在 final 的摘要里打印,S2 的摘要里没有;比较结构时需要的各半衰期多头腿数字,我是用临时 python 从 JSON 的 sweep 里抽的。按多空夏普选半衰期(rank_by: ls)在多空夏普对半衰期是平的时候会让多头腿净超额摆动 5 个点,建议摘要里常驻固定半衰期对照。",
    "summarize.py 的中性化行固定写「原始日频面板上的 R2 只有 X」,即使原始面板的 R² 更高(如 d_sum_k2:交易信号 0.554、原始面板 0.639),措辞会误导。",
    "实验室先验和 playbook 里「保序外层变换是 no-op,别当成变体来试」在当前口径(先 EMA 后排名、半衰期 > 0)下不成立(X3-H),建议修订 lab/findings.yaml 那一条的失效条件和 playbook §3 的提示;我没有改这两个文件。",
    "想把 F001 蒸馏结果当作控制变量做中性化,但往 controls 里加一项会改变 all_controls 的 R²、与 S0 的基线行不可比,所以没有改 controls,改在 exec 脚本(x3_family.py)里用 dg.neutralise 自己做;残差只能在原始日频面板上算,口径与报告里的中性化表(交易信号)略有不同,notes 里已注明。",
    "check 在 diagnostics 列表里出现尚未定义的阶段 id 时会打印 note(无害);final 阶段的变体与 S2 里同一棵树被正确识别为只求值一次。",
    "读留出段之前写的 notes/10_distilled.md 前半段里有一处小的不准确(对 e_peak_k2 多头腿的描述),按「读后不改」的约定保留原文,在同一文件末尾加了勘误;几份上一次会话写的 notes 里与留出段结果不符的读法,我没有改原文,只加了标明「后记」的一行。"
   ]
  }
  
  ## 规矩
  
  - **绝对不许再读留出段**(不许用 study.sh final,不许新建带 final 的阶段)。留出段的数字已经是定论;
    如果审查指出留出段流程本身有违规(比如读了两次),无法撤销,就在 notes/F103_amt_dw_decay/10_distilled.md 开头如实写明。
  - 每条意见要么**改正**(改 notes 里的数字/措辞;把证据不足的「已确立」降级为「合理但未坐实」或「未决」;
    必要时补实验),要么**有理有据地反驳**(审查错了的话,在你的输出里写明为什么)。不要为了通过审查而删掉不利的事实。
  - 可以补实验,但只用 train/valid:最多再跑 2 次服务器运行(新阶段 id 用 SR_ 开头,tag 用 rev1、rev2)。
    如果审查员已经加了 SA_audit 阶段并跑过(runs/F103_amt_dw_decay/audit1.json),它的结果也是证据,写进 notes
    (建一个 notes/F103_amt_dw_decay/07_SA_audit.md)。
  - 如果补的实验改变了「哪个候选最好」的判断:留出段上读过的候选不能换。你可以在 10_distilled.md 里写
    「按修订后的 train/valid 证据,X 更值得推荐,但它没有读过留出段」,recommended 仍然只能从读过留出段的候选里选。
  - 改完后 ./scripts/study.sh report F103_amt_dw_decay,通读报告。
  
  ## 你的最终输出
  
  与原研究同样的结构(修订后的版本)。在 tooling_problems 里另外列出:你对每条审查意见的处理(「已改」/「已补实验」/「反驳:理由」)。
```
