## 怎么读总表,以及哪些变体其实是同一个东西

全研究在引擎里评估过 **14 个表达式变体**,分三个阶段:`S0_baseline`(1)、`S1_long`(8)、`S_final`(5)。
另有 numpy 侧 `studies/F110_ret_fair_log/x1_anatomy.py` 的 C/D/E 段(约 20 个组合,**固定 hl20**,不进引擎总表)。
读总表之前先看懂下面三件事,否则很容易把同一个东西数成两次,或把两段不同口径的数字放在一起比。

---

### 一、四段与两种拟合口径(最容易弄错的地方)

| 段 | 日期 | 天数 | 用途 | JSON 路径 |
|---|---|---|---|---|
| `train` | 2018–2021 | 973 | **fit 段**:方向与半衰期在这里定 | `results.<id>.books.by_rank.*.splits.train` |
| `valid` | 20220101–20230807 | 386 | 样本外检验(研究期内可反复读) | `results.<id>.books.by_rank.*.splits.valid` |
| `utrain` | train + valid | 1359 | **用户训练段**,与用户那张表同口径的拟合 | `results.<id>.books_user.by_rank.*.splits.utrain` |
| `holdout` | 20230808–20251231 | 581 | **用户测试段,全研究只读一次(已读)** | `results.<id>.books_user.by_rank.*.splits.holdout` |

**`books` 与 `books_user` 是两次不同的拟合**:`books` 的半衰期/方向拟在 train 上(给 train/valid 两列),
`books_user` 拟在 utrain 上(给 utrain/holdout 两列)。
⇒ **谈「样本外变化」时要用同一拟合口径的那一对**:`utrain → holdout` 才是干净的对比,
`valid → holdout` 跨了两次拟合。本研究 J5 的「差距收窄 −7.4 点 → −1.26 点」用的就是 `utrain → holdout`。
(本例里 5 条候选两种拟合给出的 `hlL`/`hlS` 恰好全相同 —— 4 条结构候选 hl20、`f_known30` hl0,符号全 −1 ——
所以四段可以放在一张表里读;**这是运气,不是一般规律。**)

### 二、工具会让人读错的四个地方(都踩过)

1. **`digest` / `summarize.py` 主表的 `LTO`、`short` 两列只取第一个 split**;
   「与用户表同口径」那张表的 `LTO`/`short` 单列实际是 **utrain** 的值,**不是 holdout** 的
   (例:`f_cvxD20` 控制台 `LTO` 3.5%、`short` 28.2% = utrain 行;holdout 真值是 3.3% / 24.5%)。
   ⇒ **holdout 的 `Lg`/`LTO`/`short` 必须直接从 `runs/F110_ret_fair_log/S_final.json` 按 `splits.holdout` 读。**
2. **固定半衰期表(`sweep`)只在 fit 段算**;`neutralise` / `conditional` 也只有 fit 段。不是谁漏贴了。
3. **`profile`(分位剖面)只有 `train`/`valid`**,JSON 里**没有 holdout 的 profile** ⇒ 顶档单调性在留出段上验不了。
4. **`distinct`(`dist` 列)是变体级别的单一标量**,不分段 —— 一个变体只有一个 `dist`,四段通用。
5. `exec` 跑的自写脚本**不产生 JSON**,重看结果读 `logs/F110_ret_fair_log_<tag>.log`。

### 三、哪些变体其实是同一个东西

**完全同树(引擎 `check` 自己会报出来)**:
- `S_final/f_orig` ≡ `S0_baseline/v_base` ≡ 配置顶层 `expression`(原式)⇒ `rank corr = 1.000`,这是一道 canary。
- `S_final/f_cmT20` ≡ `S1_long/w_cmT20`;`f_cvxD20` ≡ `w_cvxD20`;`f_cmDsig20` ≡ `w_cmDsig20`;`f_known30` ≡ `w_known30`。
⇒ **`S_final` 的 5 条没有一条是新表达式**,它们就是前两阶段挑出来的 5 条拿去读留出段。
总表里 14 行里**只有 9 个不同的树**(1 + 8,`S_final` 的 5 条全是重复)。

**数学上等价、但写法不同(R1 的 0 段证过)**:
原式里的 `sub(div(day_last(Close), day_first(Open)), 1)` 与 `div(sub(day_last(Close), day_first(Open)), day_first(Open))`
**完全等价**(都是日内开盘→收盘收益 `D`)。后一种写法是 R2/R3 全部候选的基础 ——
它让 `cross_mean` 能套在外面。**不要把这两种写法当成两个变体。**

**机制上成对、要配着读的**:
- `f_cvxD20`(权重 `|D|`)与 `f_cmDsig20`(权重 `day_std(Ret)`)是**机制孪生**(train corr **+0.899**),
  故意同时带进留出段:两条都站住 ⇒「按当天波动尺度加权」是机制;只站住一条 ⇒ 只是某个写法的运气。
  实测两条都站住(四段 `Ln` 全部 ≥ +7.5%),但**排序在段之间翻了** ⇒ 机制保留在「未坐实」。
- `w_cmD20`(`cross_mean(D,20)`,无权重)是**权重那一问的零点**:它 +5.2%/+7.3% **高于原式权重**的 +4.2%/+5.7%
  ⇒ 整条事件机器是纯损失。读权重那张表必须带上它,否则会把「`S` 不如 `|D|`」误读成「权重有用、只是写法不好」。

**不是候选、只是对照的**:
`w_cmD60`(窗口 60,被淘汰)、`w_cmD20lag10`(砍最近 10 天,H15 对照)、`w_cmDcc20`(收盘到收盘,H5/H17 对照)。
这三条进总表是为了杀假设,**不要把它们的数字当成「候选的表现区间」。**

### 四、读单个数字之前的三道检查

1. **哪一段、哪种拟合**(`books` 还是 `books_user`)?跨拟合的对比要说明。
2. **哪种口径**:`Ln`/`Lshp`(纯多头书,`rank_by: long`,**第一判据**)还是 `LS`(多空书,次要信息)?
   半衰期也分两套(`hlL` / `hlS`)。本研究全部结论用多头口径。
3. **逐年表的 2023 那一行是 valid 146 天 + holdout 96 天的混合口径**,不能当 holdout 读;
   只有 **2024、2025** 完全落在 holdout 里。年度 `Lshp` 与整段 `Lshp` 也不是同一个口径
   (`f_cvxD20` 2024 +1.22、2025 +2.01,整段只有 +1.17 —— 差额来自 2023 后段那 96 天约为零,按加权算术反推)。
