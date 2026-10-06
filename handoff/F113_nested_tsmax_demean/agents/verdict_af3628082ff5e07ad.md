# verdict:F113_nested_tsmax_demean — agent af3628082ff5e07ad(工作流 wf_4811c95a-915)

- 状态:**失败(没有返回结果)**;开始 10-05 15:25,最后一次动作 10-05 15:34;工具调用 22 次
- 这是从 agent 的对话记录里**自动抽出来的动作流水**(命令、输出、写了哪些文件)。agent 的推理不在记录里 ——
  它的判断要看 `notes/F113_nested_tsmax_demean/journal.md` 和各 notes 文件。输出过长的地方截了中间。

## 动作流水

**10-05 15:25 · agent 的话**

I'll start by reading the required context files.

**10-05 15:25 · Bash** — Read previous round synthesis

```bash
cd /Users/wxy/Desktop/Partura && cat notes/F113_nested_tsmax_demean/synthesis.md
```

```
# F113_nested_tsmax_demean —— 批量扫描 s1 的综合(主研 Opus 5,2026-10-05)

口径:多头腿扣 15bp 净超额 `Lnet` / 纯多头夏普 `Lshp`,半衰期按纯多头书在 train 上选;
`tr|va|ut` = train 2018–2021 / valid 20220101–20230807 / utrain 两者。噪声带 Lnet ±3pp、Lshp ±0.3。
门槛 cov ≥ 0.95、dist ≥ 0.5。基准 `k_known = cross_mean(day_std(Amt), 30)`:+12.6 / +22.3 / **+15.4%**,Lshp +2.22。
原式 `v_base`:+1.6 / −1.7 / **+0.7%**,Lshp +0.17,LTO 4.0%,ρk −0.02,dist 0.58。
数据来源 `runs/F113_nested_tsmax_demean/sweep_s1.json`(189 变体)+ 同 tag 的市场解剖。

---

## 1. 它是什么(按**源码定义**逐层)

节点记号取自 `iso_*` / `abl_*` 的 why 字段:

| 节点 | 表达式 | 源码说它**实际**算什么 |
|---|---|---|
| A | `day_mean(Ret)` | 当天全部分钟收益的**等权**均值(没成交的分钟 Ret=0 也算一票) |
| B | `ts_max(A, 5)` | 近 5 日 A 的最大值 → 「最近一周最强的那一天的平均分钟收益」 |
| C | `sub(B, -5)` | **= B + 5**。常数被下一层 `cs_demean` 精确抵消 → 信息上是 no-op,但见 §2(a) |
| D | `cs_demean(C)` | B − 当日**截面均值**(是 mean 不是 median:会被当日涨停群拉动) |
| E | `ts_max(D, 30)` | 近 30 日 D 的最大值 → 「近 ~34 日内相对市场最强的一次脉冲」(**带符号**) |
| F | `pow_2(E)` | `pow_(x, 2)`:e>1 走 `x**2` 分支 → **毁掉符号**。「大幅上冲」与「长期远低于市场」同值 |
| G | `ts_max(F, 20)` | 再取 20 日最大 → 实际是 ~53 日的极端幅度平方 |
| H | `mul(G, 5)` | 正常数缩放,秩上完全无用(`abl_H` 与 `sub_H_div` 与原式**逐格相同** +0.7%) |
| I | `cs_demean(H)` | 第二次去均值:「我的 53 日极端幅度离市场典型值有多远」 |
| J | `pow_2(I)` | **第二次折叠**:上面那个距离的平方(两侧都变大) |
| K | `ts_max(J, 30)` | 近 30 日这个距离的最大值 → 「30 天里偏离过多少」 |
| L | `pow_1_5(K)` | K ≥ 0 故 `x**1.5` 保序 → 秩上无用(`iso_K` +0.8% vs 原式 +0.7%) |

**最终排序 + sg = −1 ⇒ 多头腿 = 「53 日极端脉冲幅度最接近市场典型值、且 30 天里没偏离过」的股票,
… (100 行略) …

**结论(否定性,但有据):原式的多头腿不可用(+0.7% / Lshp 0.17,6 年 3 年为负),
且对已知成交额族无增量(任何权重的叠加都不优于单跑已知族)。与上一轮读留出段得到的"负增量"一致。**
唯一值得继续的不是这条因子,是它的一个**叶子替换** `day_gini`(+6.3% / 1.44、ρo 0.06、ρk 0.20),
那实际上是一条新因子(日内集中度),应该按新因子对待 —— 第二批假设的重心就放在它身上。

---

## 5. 改进方向(已落成 `studies/F113_nested_tsmax_demean/hypo.yaml`,40 条,40/40 通过 hypo 检查)

1. **把 `+5` 全部删掉再跑一遍有信息的子树**(`h_s1`~`h_s7`、`h_g1`)—— 这是零成本的:`abl_C` 已证明收益不变而 dist 回到 1.00。
   若 `h_s3` / `h_s4` 拿到 ~+7.7% 且 dist ≥ 0.5,本因子才第一次有能过门槛的候选。
2. **拆开 `abl_J` 的 +12.4%**:`h_s1`(保号、不 NaN)对 `h_s2`(abs 折叠)—— 分清"符号有用"与"NaN 筛掉 57% 的票有用"。
3. **把折叠改成秩距离**(`h_r1`~`h_r3`):`fold_rank` 已给出 +3.0% / hl 20 的苗头,秩空间不会被量纲毁掉。
4. **把 day_gini 一族做到底**:最小形 `h_g3`、水平形 `h_g4`、去水平 `h_g5`、稳定性 `h_g7`、EMA 记忆 `h_m1`~`h_m3`、
   增量四件套 `h_k1`~`h_k3`、冻结状态中性 `h_f3`。
5. **按解剖下注**:冻结状态做叶子(`h_f1`/`h_f2`)、活跃度桶内/桶乘(`h_q1`/`h_q2`/`h_g6`)、
   稳健中心替代 cs_demean(`h_q3`)、用"市场 20 日平均分钟收益"做逐日符号翻转把择时写进表达式(`h_q4`/`h_q5`)。
6. **用新算子做原来做不了的事**:`day_gini` / `day_flat_ratio` / `day_pos_ratio` / `day_centroid` / `day_wmean(Ret,Amt)` /
   `day_signed_ratio(Ret,Amt)` / `in_pct` / `in_logchg` / `cross_ema` / `cross_zscore` / `cs_bucket_rank` / `cs_winsor` 都用上了。
```

**10-05 15:25 · Bash** — Read new operators batch 4

```bash
cd /Users/wxy/Desktop/Partura && sed -n '/第四批/,$p' docs/new_operators.md
```

```
**第四批(十条因子的综合里被反复要求的;共 23 个)**

| 算子 | 定义 | 谁要的、为什么 |
|---|---|---|
| `cs_bucket_demean(y, x)` | y 减去「x 的同一个十分位」内 y 的均值(保留量纲) | F101 / F107 / F110:折叠的中心应该是「同类股票的典型值」而不是全市场均值 —— 后者把书推进大票 |
| `cs_bucket_zscore(y, x)` | 同上再除以桶内标准差 | F101 / F106:各桶离散度相差数倍,去均值后的距离仍不可比 |
| `cs_robust_z(x)` | 截面 `(x − 中位数) / (1.4826·MAD)` | F113:重尾量的截面标准化 |
| `cs_first_low20 / cs_first_high20 / cs_last_high40 / cs_last_low40` | 与 `cs_first_low40` 等同语义,补齐 20% / 40% 两档 | F112 |
| `cs_state_rank(x, d)` | 当日 x 的截面均值在它自己近 d 日里的分位,**全市场同一个数** | F107 / F112 / F115:「只在某种市场状态下有效」以前写不进表达式;它可以当两条信号之间的权重,或 `select_where` 的条件 |
| `cs_flip_by_state(y, g)` | 市场级状态(g 的截面均值相对近 241 日中位数)高时取 +rank(y),低时取 −rank(y) | F104:最小的「按市场状态切日子」原语 |
| `day_at_max_ratio(x)` / `day_at_min_ratio(x)` | 当天取值等于当日最大(最小)值的分钟占比 | F106 / F110:封在涨停和封在跌停是两种事件,`day_flat_ratio` 分不开 |
| `day_distinct_ratio(x)` | 当天不同取值的个数 ÷ 有限分钟数 | F107:当天走过多少个价位(低价票在一个 tick 的格子上很粗) |
| `day_wstd(x, w)` | `|w|` 加权的总体标准差 | F101:资金经历的波动,不被没有成交的分钟稀释 |
| `day_topw_mean(y, w)` | `|w|` 最大的 10% 分钟上 y 的均值 | F115:一个节点完成「放量分钟的平均收益」,不用触发掩码 |
| `day_es_ratio_hi(x)` / `day_es_ratio_lo(x)` | 高于 95%(低于 5%)分位的分钟均值 ÷ 该分位;分位数接近 0 时 **NaN** | F106 / F109:手写的 `erm_*` 因子在分母上加 1e-6,把每个封板日变成 1e4 量级的值,因子读到的是「有没有封板」而不是尾部形状;这是同一个量、把那样的日子留作缺失 |
| `in_index(x)` | 分钟在一天里的位置 `t/(T−1)` | F115:按时间加权或比较 |
| `in_zscore_expand(x)` | 日内扩张窗口 z 分数(到当前分钟为止) | F110:「相对今天到目前为止是否异常」,日内因果 |
| `cross_madz(x, d)` | `cross_zscore` 的稳健版(中位数 / MAD,相对 EPS) | F104:分清「标准化这个想法不对」和「估计量太脆」 |
| `cross_flat_ratio(x, d)` | 近 d 日里与前一日取值完全相同的日子占比 | F111 |
| `cross_semistd_neg(x, d)` / `…_pos` | 正值序列日度对数变化的下行(上行)半标准差 | F112 |
| `cross_age(x)` | x 第一次有值以来的交易日数;数据起点就有值的股票从 10000 起算 | F105:不饱和的上市时间 |

已经有、不用新加的(告诉主研):三目选择用现成的 `select_where(c, a, b)`;近 d 日为正的占比 = `cross_mean(is_gt0(x), d)`;
「离截面中心多近」= `abs_(cs_demean(cs_rank(x)))` 的单调变换。

**主研们反复要、但属于数据层的**(6 条因子都提了,需要用户决定是否在 AlphaCube 的立方体里加字段):
- **流通市值 / 流通股本**(F105、F108、F110、F115…):有了它才能写真正的换手率 `day_sum(Amt) / FloatCap`、做规模中性;
  现在只能用价格或成交额水平做代理,而这两个代理在好几棵树上符号相反。
- **板块 / 涨跌幅限制宽度**(F104、F111、F112):科创板 ±20%、无「一字板」状态,多条因子在那里整体失效或被错判。

没有加的:`cs_bucket_rank2(y, x1, x2)`(二维 5×5 格子内排名)—— 算子语法目前只支持 1~2 个张量操作数;
「流通市值」字段 —— 立方体里没有,需要在数据层加(Partura 只把它当外部控制变量用)。这两条留给用户决定。

实现上的一个坑:引擎里 `cross_*` 内核如果写成逐日的 Python 循环会慢 60 倍以上;`cross_ema` 用分块的精确递推
(块内累加、块间进位)解决,和逐日递推的最大误差 1e-6。

加新算子的步骤:在 `ops_ext.py` 里写函数(docstring 写清定义)→ 加进 `NEW_OPERATORS` → 用已知答案核对 →
`rsync` 到服务器 → 在本表登记定义和理由。
```

**10-05 15:25 · Bash** — Read s2 sweep table

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh table F113_nested_tsmax_demean s2 --all 2>&1 | head -300
```

```
<persisted-output>
Output too large (72.2KB). Full output saved to: /Users/wxy/.claude/projects/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/tool-results/b83mcx3uf.txt

Preview (first 2KB):
== F113_nested_tsmax_demean  批量扫描 s2:235 个变体(只用 train 2018–2021 / valid 2022–202308;方向 sg 与半衰期 hlL 在 train 上定,半衰期按纯多头书选)==
Lnet = 多头腿净超额(扣 15bp,年化),Lshp = 纯多头夏普:train | valid | utrain(用户训练段);LTO = 多头日换手;LS = 多空夏普;
空头腿 = 等权 − 最低十分位(毛,年化):大 = 钱在空头腿(纯多头用不上);为负 = 最低十分位反而跑赢,值得把方向反过来看。
ρo / ρk = 交易信号与原式 / 已知成交额族的 rank 相关;✗ = 没过门槛(cov ≥ 0.95、dist ≥ 0.5),不能当候选。
id                     kind     sg hlL | Lnet tr     va     ut   | Lshp tr    va    ut  | LTO   | LS tr   va  | 空头腿 tr   va   |  ρo    ρk  | cov  dist   | expr
v_base                 base     -1   1 |  +1.6%  -1.7%  +0.7% | +0.39 -0.52 +0.17 |  4.1% | +2.59 +2.39 | +25.2% +25.7% | +1.00 -0.02 | 1.00 0.58   | pow_1_5(ts_max(pow_2(cs_demean(mul(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(day_mean(Ret), 5), -5)), 30)), 20), 5))), 30))
k_known                bench    -1   0 | +12.6% +22.3% +15.4% | +1.78 +3.46 +2.22 |  3.4% | +1.87 +3.70 | +21.1% +33.8% | -0.02 +1.00 | 1.00 1.00   | cross_mean(day_std(Amt), 30)
---------------------------------------- 全部变体,按 utrain 纯多头夏普排序
k_known_xfrozen        bench    +1   3 | +16.4% +23.2% +18.5% | +2.81 +3.98 +3.15 |  3.4% | +4.27 +4.99 | +25.4% +22.4% | +0.04 +0.56 | 1.00 1.00   | cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Ret), 15))
h_k2_gini_overlay      hypo     -1   0 | +14.6% +23.9% +17.2% | +2.19 +4.04 +2.66 |  4.2% | +2.71 +4.76 | +30.4% +39.4% | -0.01 +0.98 | 1.00 0.91   | add(cs_rank(cross_mean(day_std(Amt), 30)), mul(cs_rank(cross_mean(day_gini(Ret), 30)), 0.25))
sub_J_pow_1_5          substitu -1   1 | +13.3% +10.2% +12.4% | +2.53 +2.00 +2.39 |  5.9% | +2.80 +2.49 | +26.5% +21.8% | +0.86 +0.17 | 0.43 0.66 ✗ | pow_1_5(ts_max(pow_1_5(cs_demean(mul(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(day_mean(Ret), 5), -5)), 30)), 20), 5))), 30))
...
</persisted-output>
```

10-05 15:25 · 读 `/Users/wxy/.claude/projects/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/tool-results/b83mcx3uf.txt`

10-05 15:25 · 读 `/Users/wxy/.claude/projects/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/tool-results/b83mcx3uf.txt`

10-05 15:25 · 读 `/Users/wxy/.claude/projects/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/tool-results/b83mcx3uf.txt`

**10-05 15:27 · agent 的话**

Now let me check the hypo format and available operators before writing hypothesis batch 3.

**10-05 15:27 · Bash** — Check hypo yaml format and study.sh usage

```bash
cd /Users/wxy/Desktop/Partura && head -30 studies/F113_nested_tsmax_demean/hypo.yaml && echo "=== LS studies dir ===" && ls studies/F113_nested_tsmax_demean/ && echo "=== study.sh usage ===" && sed -n '1,60p' scripts/study.sh
```

```
# F113_nested_tsmax_demean —— 第二批假设(主研 Opus 5,2026-10-05,基于批量扫描 s1 的大表)
#
# 节点记号(来自 iso_*/abl_* 的 why 字段):
#   A=day_mean(Ret)  B=ts_max(A,5)  C=sub(B,-5)  D=cs_demean(C)  E=ts_max(D,30)  F=pow_2(E)
#   G=ts_max(F,20)   H=mul(G,5)     I=cs_demean(H) J=pow_2(I)    K=ts_max(J,30)  L=pow_1_5(K)
#
# 这一批围绕大表里的四条结论:
#   (1) C 的 +5 在信息上被下一层 cs_demean 精确抵消,但把 float32 的截面分辨率砸掉了
#       (iso_B dist 1.00 → iso_C dist 0.22;abl_C 收益不变而 dist 回到 1.00)。
#       → 凡是原式的子树,都重写一遍"去掉 +5"的版本,看 dist 能不能救回来。
#   (2) 第二层折叠(I+J)是损害:abl_I +8.6%、abl_J +12.4%,但一个爆 dist、一个爆 cov
#       (pow_1_5 对负数返回 NaN → cov 0.43)。→ 用不会 NaN 的写法把"去掉折叠"重做一遍。
#   (3) 唯一过门槛且明显赢原式的叶子替换是 day_gini(+6.3% / Lshp 1.44,cov 1.00 dist 0.97);
#       推断:双层折叠只在**有界、无尺度**的叶子上无害。→ 成批试有界叶子 + 把 gini 化简到最小形。
#   (4) 解剖:原式只在成交额最高 20%(+8.8%)和近 15 日有冻结盘口(+11.9%)的段内有信息,
#       在无冻结的 93.5% 里是 −2.3%。→ 直接拿 day_flat_ratio 当叶子,并在活跃度/冻结度桶内做中性。

h_s1_nofold_signed:    {expr: "ts_max(cs_demean(ts_max(pow_2(ts_max(cs_demean(ts_max(day_mean(Ret), 5)), 30)), 20)), 30)", why: "abl_J 的 +12.4% 是真结构还是 pow_1_5 把 57% 的票 NaN 掉换来的子universe:去掉 +5、去掉外层 pow_1_5,cov 应回到 1.00"}
h_s2_nofold_abs:       {expr: "abs_(ts_max(cs_demean(ts_max(pow_2(ts_max(cs_demean(ts_max(day_mean(Ret), 5)), 30)), 20)), 30))", why: "和 h_s1 只差一个 abs_:分离「符号有用」(h_s1 赢)与「universe 筛选有用」(两条都塌)"}
h_s3_isoG_nosub:       {expr: "ts_max(pow_2(ts_max(cs_demean(ts_max(day_mean(Ret), 5)), 30)), 20)", why: "iso_G 的 +7.7% / Lshp 1.16 只因 dist 0.26 作废;去掉 +5 之后 dist 若回到 ~1 就是一条能用的候选"}
h_s4_isoF_nosub:       {expr: "pow_2(ts_max(cs_demean(ts_max(day_mean(Ret), 5)), 30))", why: "iso_F(+7.7% / 1.18,dist 0.24)去掉 +5:同上,且比 h_s3 少一层 MAX,检验 G 这层是否多余"}
h_s5_isoE_nosub:       {expr: "ts_max(cs_demean(ts_max(day_mean(Ret), 5)), 30)", why: "iso_E 的带符号版(+1.7%,dist 0.27):去掉 +5 后它和 h_s4 的差就是 pow_2 折叠本身的净效果"}
h_s6_isoI_nosub:       {expr: "cs_demean(ts_max(pow_2(ts_max(cs_demean(ts_max(day_mean(Ret), 5)), 30)), 20))", why: "iso_I(+7.7%,dist 0.26)去掉 +5:第二次 cs_demean 是否只是把 h_s3 平移(两条应几乎同分)"}
h_s7_win50_outer:      {expr: "ts_max(pow_2(ts_max(cs_demean(ts_max(day_mean(Ret), 5)), 50)), 20)", why: "win_E_50 是 15 个窗口变体里最好的(+1.1%);在去掉 +5 的干净树上再试一次,看是不是真有平台"}

h_r1_rankdist:         {expr: "abs_(cs_demean(cs_rank(ts_max(pow_2(ts_max(cs_demean(ts_max(day_mean(Ret), 5)), 30)), 20))))", why: "fold_rank(+3.0%,hl 20)说明「离截面中位有多远」才是可用的折叠;把它写在干净子树上,彻底避开 pow_2 的量纲爆炸"}
h_r2_rankdist_mem:     {expr: "ts_max(abs_(cs_demean(cs_rank(ts_max(pow_2(ts_max(cs_demean(ts_max(day_mean(Ret), 5)), 30)), 20)))), 30)", why: "原式的全部逻辑(「30 天里没偏离过典型值」)在秩空间重写一遍:若原式的 +0.7% 只是被量纲毁掉的 h_r1,这条应接近 h_r1 或更好"}
h_r3_rankdist_bk:      {expr: "cs_bucket_rank(abs_(cs_demean(cs_rank(ts_max(pow_2(ts_max(cs_demean(ts_max(day_mean(Ret), 5)), 30)), 20)))), cross_mean(day_sum(Amt), 30))", why: "原式段内只在成交额最高 20% 有信息:在成交额十分位内做桶内排名,若 h_r1 的分数全掉光,说明它就是活跃度分类器"}

h_g1_gini_nosub:       {expr: "pow_1_5(ts_max(pow_2(cs_demean(mul(ts_max(pow_2(ts_max(cs_demean(ts_max(day_gini(Ret), 5)), 30)), 20), 5))), 30))", why: "nosc_A_day_gini 去掉 +5:白送的清理(dist 0.97→应为 1.00),收益若不变就确认 C 节点纯属精度损失"}
… (45 行略) …
  [ -f "$f" ] || printf '# %s 研究日志\n\n只追加、不改写。[auto] 是工具自己记的(启动了什么、什么时候跑完);其余是研究员写的:\n每看完一个结果,写下它说明了什么、哪条假设变了、下一步做什么。接手的人先读这里(`./scripts/study.sh brief %s`)。\n' "$1" "$1" > "$f"
}
jlog() {    # jlog <fid> <text>: one automatic line
  jinit "$1"; printf '\n### %s [auto] %s\n' "$(date '+%Y-%m-%d %H:%M')" "$2" >> "$(jfile "$1")"
}
notice() {  # a standing notice from the coordinator to whoever is working on this study (handoff/NOTICE.md);
            # it stops appearing for a study once that study's notes/<fid>/state.md is newer than the notice
  local f="handoff/NOTICE.md" s="notes/${1:-}/state.md"
  [ -n "${1:-}" ] && [ -f "$f" ] || return 0
  [ -f handoff/NOTICE.fids ] && ! grep -qx "$1" handoff/NOTICE.fids && return 0   # addressed to listed studies only
  [ -f "$s" ] && [ "$s" -nt "$f" ] && return 0
  echo; sed "s/<fid>/$1/g" "$f"
}
trap 'notice "${fid:-}"' EXIT
remind() {  # what every finished result ends with
  echo
  echo "📝 往下做之前先记日志(研究随时可能中断、换人或换模型接手;没落盘的判断会丢):"
  echo "   ./scripts/study.sh note $1 \"<一句话:这次看到了什么>\" <<'EOF'"
  echo "   这次结果说明什么(带关键数字)/ 哪条假设因此变了 / 下一步打算做什么、为什么"
  echo "   EOF"
```

**10-05 15:28 · Bash** — Find where new operators are implemented

```bash
cd /Users/wxy/Desktop/Partura && grep -rn "cs_bucket_demean\|cs_robust_z\|cross_age\|day_at_max_ratio\|day_topw_mean\|cs_state_rank\|cross_madz\|day_es_ratio_hi\|in_zscore_expand\|cross_flat_ratio\|cross_semistd\|day_wstd\|cs_flip_by_state\|in_index\|cs_first_low20\|select_where\|day_distinct_ratio\|in_zscore_expand" --include=*.py -l | head -20
```

```
(eval):1: no matches found: --include=*.py
```

**10-05 15:28 · Bash** — Check hypo subcommand in study.sh

```bash
cd /Users/wxy/Desktop/Partura && grep -n "hypo" scripts/study.sh | head -40
```

```
20:#   study.sh hypo <fid>                    check that studies/<fid>/hypo.yaml (hypotheses for the next sweep) parses
144:  hypo)      # do the hypotheses in studies/<fid>/hypo.yaml parse?  (they go into the next batch sweep)
146:    $SSH $HOST "$ENV && $RPY scripts/check_hypo.py studies/$fid/hypo.yaml 2>&1 | grep -v 'FutureWarning\|vmap(single_row)\|UserWarning'"
148:  hypo3)     # same check for the third batch, studies/<fid>/hypo3.yaml
150:    $SSH $HOST "$ENV && $RPY scripts/check_hypo.py studies/$fid/hypo3.yaml 2>&1 | grep -v 'FutureWarning\|vmap(single_row)\|UserWarning'"
```

**10-05 15:28 · Bash** — Find partura python files

```bash
cd /Users/wxy/Desktop/Partura && ls partura/ 2>/dev/null; echo "---"; find . -name "ops_ext.py" -o -name "*.py" -path "*partura*" 2>/dev/null | head -20
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
ops_ext.py
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
---
./partura/runner.py
./partura/decompose.py
./partura/report_legacy.py
./partura/books.py
./partura/semantics.py
./partura/study_tools.py
./partura/bridge.py
./partura/propose.py
./partura/__init__.py
./partura/diagnose.py
./partura/cli.py
./partura/guard.py
./partura/splits.py
./partura/ops_ext.py
./partura/probes.py
./partura/report.py
./partura/lab.py
./partura/panels.py
./partura/remote_tools.py
./tests/test_partura.py
```

**10-05 15:28 · Bash** — List operator function signatures in ops_ext

```bash
cd /Users/wxy/Desktop/Partura && grep -n "^def \|^NEW_OPERATORS" partura/ops_ext.py | head -80
```

```
31:def _f(x: torch.Tensor) -> torch.Tensor:
38:def in_pct(x: torch.Tensor, d: int) -> torch.Tensor:
56:def in_logchg(x: torch.Tensor, d: int) -> torch.Tensor:
74:def _day(v: torch.Tensor, ok: torch.Tensor) -> torch.Tensor:
80:def day_flat_ratio(x: torch.Tensor) -> torch.Tensor:
96:def day_pos_ratio(x: torch.Tensor) -> torch.Tensor:
107:def day_wmean(x: torch.Tensor, w: torch.Tensor) -> torch.Tensor:
120:def day_signed_ratio(x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
134:def day_gini(x: torch.Tensor) -> torch.Tensor:
153:def day_centroid(x: torch.Tensor) -> torch.Tensor:
170:def cross_ema(x: torch.Tensor, d: int) -> torch.Tensor:
202:def cross_zscore(x: torch.Tensor, d: int) -> torch.Tensor:
220:def _pct_rank(x: torch.Tensor, ok: torch.Tensor) -> torch.Tensor:
228:def cs_bucket_rank(y: torch.Tensor, x: torch.Tensor) -> torch.Tensor:
249:def cs_winsor(x: torch.Tensor) -> torch.Tensor:
262:def day_zero_ratio(x: torch.Tensor) -> torch.Tensor:
277:def cross_valid_count(x: torch.Tensor, d: int) -> torch.Tensor:
289:def _tail_mean(x: torch.Tensor, d: int, q: float, low: bool) -> torch.Tensor:
300:def cross_tail_mean_q25(x: torch.Tensor, d: int) -> torch.Tensor:
309:def cross_tail_mean_q75(x: torch.Tensor, d: int) -> torch.Tensor:
315:def _lexi(y: torch.Tensor, x: torch.Tensor, lo: float, hi: float, shift: float) -> torch.Tensor:
324:def cs_first_low40(y: torch.Tensor, x: torch.Tensor) -> torch.Tensor:
336:def cs_first_high40(y: torch.Tensor, x: torch.Tensor) -> torch.Tensor:
342:def cs_last_high20(y: torch.Tensor, x: torch.Tensor) -> torch.Tensor:
350:def cs_last_low20(y: torch.Tensor, x: torch.Tensor) -> torch.Tensor:
356:def day_flat_run_max(x: torch.Tensor) -> torch.Tensor:
375:def in_madz(x: torch.Tensor, d: int) -> torch.Tensor:
396:def _buckets(x: torch.Tensor, ok: torch.Tensor) -> torch.Tensor:
401:def cs_bucket_demean(y: torch.Tensor, x: torch.Tensor) -> torch.Tensor:
420:def cs_bucket_zscore(y: torch.Tensor, x: torch.Tensor) -> torch.Tensor:
… (7 行略) …
485:def cs_state_rank(x: torch.Tensor, d: int) -> torch.Tensor:
500:def cs_flip_by_state(y: torch.Tensor, g: torch.Tensor) -> torch.Tensor:
518:def day_at_max_ratio(x: torch.Tensor) -> torch.Tensor:
532:def day_at_min_ratio(x: torch.Tensor) -> torch.Tensor:
543:def day_distinct_ratio(x: torch.Tensor) -> torch.Tensor:
557:def day_wstd(x: torch.Tensor, w: torch.Tensor) -> torch.Tensor:
571:def day_topw_mean(y: torch.Tensor, w: torch.Tensor) -> torch.Tensor:
583:def _es_ratio(x: torch.Tensor, q: float, hi: bool) -> torch.Tensor:
596:def day_es_ratio_hi(x: torch.Tensor) -> torch.Tensor:
607:def day_es_ratio_lo(x: torch.Tensor) -> torch.Tensor:
615:def in_index(x: torch.Tensor) -> torch.Tensor:
626:def in_zscore_expand(x: torch.Tensor) -> torch.Tensor:
642:def cross_madz(x: torch.Tensor, d: int) -> torch.Tensor:
657:def cross_flat_ratio(x: torch.Tensor, d: int) -> torch.Tensor:
672:def _semistd(x: torch.Tensor, d: int, neg: bool) -> torch.Tensor:
686:def cross_semistd_neg(x: torch.Tensor, d: int) -> torch.Tensor:
694:def cross_semistd_pos(x: torch.Tensor, d: int) -> torch.Tensor:
700:def cross_age(x: torch.Tensor) -> torch.Tensor:
713:NEW_OPERATORS = ("in_pct", "in_logchg", "day_flat_ratio", "day_pos_ratio", "day_wmean", "day_signed_ratio",
725:def install() -> None:
```

**10-05 15:28 · Bash** — Read bucket/state operator sources

```bash
cd /Users/wxy/Desktop/Partura && sed -n '396,520p' partura/ops_ext.py
```

```
def _buckets(x: torch.Tensor, ok: torch.Tensor) -> torch.Tensor:
    return torch.ceil(_pct_rank(x, ok) * 10.0).clamp(1, 10)


@op("nd", "cs", arity=2)
def cs_bucket_demean(y: torch.Tensor, x: torch.Tensor) -> torch.Tensor:
    """``y`` minus the mean of ``y`` over the stocks in the same decile of ``x`` that day.
    Keeps y's units and magnitude (``cs_bucket_rank`` throws them away), so a fold
    ``abs_(cs_bucket_demean(y, x))`` measures 'distance from what is typical FOR ITS OWN
    x-bucket' instead of from the whole-market mean.  NaN where either is missing or the
    bucket has fewer than 2 names.  (Requested by F101, F107, F110.)"""
    y, x = _f(y), _f(x)
    ok = torch.isfinite(y) & torch.isfinite(x)
    bx = _buckets(x, ok)
    out = torch.full_like(y, NAN)
    for b in range(1, 11):
        m = ok & (bx == b)
        n = m.sum(-1, keepdim=True)
        mu = torch.where(m, y, torch.zeros_like(y)).sum(-1, keepdim=True) / n.clamp(min=1).to(y.dtype)
        out = torch.where(m & (n >= 2), y - mu, out)
    return out


@op("nd", "cs", arity=2)
def cs_bucket_zscore(y: torch.Tensor, x: torch.Tensor) -> torch.Tensor:
    """As ``cs_bucket_demean`` but divided by the bucket's own population std (+EPS):
    comparable across buckets whose dispersion differs severalfold.  (F101, F106.)"""
    y, x = _f(y), _f(x)
    ok = torch.isfinite(y) & torch.isfinite(x)
    bx = _buckets(x, ok)
… (75 行略) …
    """``+rank(y)`` on days when the market-level state is HIGH and ``-rank(y)`` when it is
    low: state = the day's cross-sectional mean of ``g`` compared with the median of that
    series over the last 241 days; rank(y) is centred on 0 (percentile - 0.5).

    The minimal way to say 'y works in one kind of market and reverses in the other'
    inside an expression.  If y simply stops working in the other state, the flipped
    version will be clearly WORSE than y -- which is itself the test.  (F104.)"""
    y = _f(y)
    m = _market_series(g)
    hi = _trailing_rank(m, 241) > 0.5
    ok = torch.isfinite(y)
    r = _pct_rank(y, ok) - 0.5
    sgn = torch.where(hi, torch.ones_like(m), -torch.ones_like(m)).unsqueeze(-1)
    return torch.where(ok, r * sgn, torch.full_like(y, NAN))


@op("dt", "day", arity=1)
def day_at_max_ratio(x: torch.Tensor) -> torch.Tensor:
    """Share of the day's finite minutes whose value equals the day's maximum.
    On Close / High: time spent pinned at the day's high -- a limit-up lock reads near 1,
```

**10-05 15:28 · Bash** — Read day/cross new operator sources

```bash
cd /Users/wxy/Desktop/Partura && sed -n '518,712p' partura/ops_ext.py
```

```
def day_at_max_ratio(x: torch.Tensor) -> torch.Tensor:
    """Share of the day's finite minutes whose value equals the day's maximum.
    On Close / High: time spent pinned at the day's high -- a limit-up lock reads near 1,
    a normal day near 1/240.  (F106, F110: 'locked at the top' vs 'locked at the bottom'
    are different events and ``day_flat_ratio`` cannot tell them apart.)"""
    x = _f(x)
    ok = torch.isfinite(x)
    n = ok.sum(-1)
    mx = torch.where(ok, x, torch.full_like(x, float("-inf"))).max(dim=-1, keepdim=True).values
    r = ((x == mx) & ok).sum(-1).to(x.dtype) / n.clamp(min=1).to(x.dtype)
    return _day(r, n > 1)


@op("dt", "day", arity=1)
def day_at_min_ratio(x: torch.Tensor) -> torch.Tensor:
    """Share of the day's finite minutes whose value equals the day's minimum."""
    x = _f(x)
    ok = torch.isfinite(x)
    n = ok.sum(-1)
    mn = torch.where(ok, x, torch.full_like(x, float("inf"))).min(dim=-1, keepdim=True).values
    r = ((x == mn) & ok).sum(-1).to(x.dtype) / n.clamp(min=1).to(x.dtype)
    return _day(r, n > 1)


@op("dt", "day", arity=1)
def day_distinct_ratio(x: torch.Tensor) -> torch.Tensor:
    """Number of DISTINCT values among the day's finite minutes, divided by their count:
    1/n = one price all day, 1 = every minute different.  On a price: how many price
    levels the day visited -- coarse for low-priced stocks on a one-tick grid.  (F107.)"""
    x = _f(x)
… (143 行略) …


@op("dt", "cross", arity=1, requires_window=True)
def cross_semistd_pos(x: torch.Tensor, d: int) -> torch.Tensor:
    """Upside semi-deviation of the daily log change of a positive ``x`` over ``d`` days."""
    return _semistd(x, d, False)


@op("dt", "cross", arity=1)
def cross_age(x: torch.Tensor) -> torch.Tensor:
    """Trading days since ``x`` first had a finite value: 0 on that day, +1 every trading
    day after (suspensions included); NaN before.  A stock that is already finite on the
    first day of the data is treated as old (its age starts at 10000), because the data
    cannot say when it listed.  Unlike ``cross_valid_count`` it does not saturate at the
    window.  (F105.)"""
    x = _f(x)
    seen = torch.cummax(torch.isfinite(x).to(x.dtype), dim=0).values
    age = torch.cumsum(seen, dim=0) - 1.0
    old = torch.isfinite(x[:1]).to(x.dtype) * 10000.0
    return torch.where(seen > 0, age + old, torch.full_like(x, NAN))
```

**10-05 15:28 · Bash** — Read lexi screen semantics and select_where

```bash
cd /Users/wxy/Desktop/Partura && sed -n '315,356p' partura/ops_ext.py && echo "=== select_where ===" && grep -rn "select_where" partura/*.py scripts/*.py 2>/dev/null | head -10 && echo "=== check_hypo ===" && sed -n '1,40p' scripts/check_hypo.py
```

```
def _lexi(y: torch.Tensor, x: torch.Tensor, lo: float, hi: float, shift: float) -> torch.Tensor:
    """rank(y) in (0, 1], shifted by ``shift`` for the stocks whose x-rank is in (lo, hi]."""
    y, x = _f(y), _f(x)
    ok = torch.isfinite(y) & torch.isfinite(x)
    rx, ry = _pct_rank(x, ok), _pct_rank(y, ok)
    return torch.where(ok, ry + shift * ((rx > lo) & (rx <= hi)).to(y.dtype), torch.full_like(y, NAN))


@op("nd", "cs", arity=2)
def cs_first_low40(y: torch.Tensor, x: torch.Tensor) -> torch.Tensor:
    """Rank of ``y`` (in (0, 1]) with every stock in the LOWEST 40% of ``x`` placed above
    every other stock: ``rank(y) + 1`` there, ``rank(y)`` elsewhere.

    'Trade y only where x is low' as an expression: the top of the output is drawn from
    the low-x segment, ordered by y, while every stock keeps a distinct value (no NaN,
    no ties), so the book is still measured against the whole market.  Use it when the
    anatomy says a signal selects only inside one segment (small / illiquid names)."""
    return _lexi(y, x, -1.0, 0.4, 1.0)


@op("nd", "cs", arity=2)
def cs_first_high40(y: torch.Tensor, x: torch.Tensor) -> torch.Tensor:
    """As ``cs_first_low40`` but the HIGHEST 40% of ``x`` come first."""
    return _lexi(y, x, 0.6, 1.0, 1.0)


@op("nd", "cs", arity=2)
def cs_last_high20(y: torch.Tensor, x: torch.Tensor) -> torch.Tensor:
    """Rank of ``y`` with every stock in the HIGHEST 20% of ``x`` placed BELOW every other
    stock (``rank(y) - 1`` there).  An exclusion screen: those names can never reach the
… (27 行略) …

try:
    d = yaml.safe_load(Path(sys.argv[1]).read_text(encoding="utf-8")) or {}
except yaml.YAMLError as exc:
    mark = getattr(exc, "problem_mark", None)
    where = f"第 {mark.line + 1} 行第 {mark.column + 1} 列附近" if mark else ""
    print(f"YAML 写法有误 {where}:{getattr(exc, 'problem', exc)}\n"
          "常见原因:键后面的冒号要跟一个空格(`h_x: {expr: \"…\", why: \"…\"}`);表达式里的引号要成对;why 里有冒号时整句加引号。")
    sys.exit(2)
bad = 0
for i, v in d.items():
    e = v["expr"] if isinstance(v, dict) else str(v)
    try:
        parse_research(e)
        print(f"OK    {i}")
    except Exception as exc:  # noqa: BLE001
        bad += 1
        print(f"FAIL  {i}: {type(exc).__name__}: {str(exc)[:220]}\n      {e[:200]}")
print(f"{len(d) - bad}/{len(d)} parse")
sys.exit(1 if bad else 0)
```

**10-05 15:30 · Bash** — Read day_gini definition

```bash
cd /Users/wxy/Desktop/Partura && sed -n '134,170p' partura/ops_ext.py && echo "=== ops with scalar/select ===" && grep -rn "select_where\|def is_gt0\|\"sub\"\|'sub'" partura/semantics.py partura/panels.py 2>/dev/null | head
```

```
def day_gini(x: torch.Tensor) -> torch.Tensor:
    """Gini coefficient of ``|x|`` across the day's finite minutes: 0 = spread evenly,
    -> 1 = everything in a few minutes.  Scale-free and bounded, so unlike
    ``day_kurt`` / max-share it cannot be dominated by one print, and unlike
    ``day_std / day_mean`` it does not explode on thin days."""
    x = _f(x).abs()
    ok = torch.isfinite(x)
    n = ok.sum(-1)
    v = torch.where(ok, x, torch.full_like(x, float("inf")))          # missing minutes sort last
    v, _ = torch.sort(v, dim=-1)
    v = torch.where(torch.isfinite(v), v, torch.zeros_like(v))
    idx = torch.arange(1, x.shape[-1] + 1, device=x.device, dtype=x.dtype)
    tot = v.sum(-1)
    nf = n.to(x.dtype)
    g = (2.0 * (v * idx).sum(-1) / (nf.clamp(min=1) * tot.clamp(min=1e-30))) - (nf + 1.0) / nf.clamp(min=1)
    return _day(g, (n > 1) & (tot > 0))


@op("dt", "day", arity=1)
def day_centroid(x: torch.Tensor) -> torch.Tensor:
    """Centre of mass of ``|x|`` along the minute axis, scaled to [0, 1]:
    ``sum(t * |x[t]|) / sum(|x|) / (T - 1)``.  0 = all at the open, 1 = all at the
    close, 0.5 = symmetric.  On Volume / Amt: *when* in the day the trading happened --
    information that every order-free statistic (std, kurt, gini) throws away."""
    x = _f(x).abs()
    ok = torch.isfinite(x)
    v = torch.where(ok, x, torch.zeros_like(x))
    T = x.shape[-1]
    t = torch.arange(T, device=x.device, dtype=x.dtype) / max(T - 1, 1)
    tot = v.sum(-1)
    return _day((v * t).sum(-1) / tot.clamp(min=1e-30), tot > 0)


# ----------------------------------------------------------------------------- day axis (cross_*)

@op("dt", "cross", arity=1, requires_window=True)
def cross_ema(x: torch.Tensor, d: int) -> torch.Tensor:
=== ops with scalar/select ===
```

**10-05 15:32 · 写文件** `/Users/wxy/Desktop/Partura/studies/F113_nested_tsmax_demean/hypo3.yaml`(8286 字符)

**10-05 15:32 · Bash** — Parse-check hypothesis batch 3

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh hypo3 F113_nested_tsmax_demean 2>&1 | tail -40
```

```
OK    h3_g6_bdemean
OK    h3_g6_bz
OK    h3_g6_fold
FAIL  h3_g6_bk_age: ParseError: an ND-face operator needs a one-value-per-stock-day operand, got cross_age(Amt) (wrap the minute-level subtree in day_*)
      cs_bucket_rank(cross_mean(day_gini(Ret), 30), cross_age(Amt))
OK    h3_g6_hiliq
OK    h3_g6_w5
OK    h3_g6_distinct
OK    h3_g6_wstd
OK    h3_g6_topw
OK    h3_g6_eshi
OK    h3_g6_volchg
OK    h3_g6_inz
OK    h3_tree_bdemean
OK    h3_tree_bz
OK    h3_tree_robustz
OK    h3_jscreen
OK    h3_jkeep
OK    h3_gini_madz
OK    h3_gini_madz_bk
OK    h3_gini_semistd
OK    h3_atmax_tree
OK    h3_atmin_bk
FAIL  h3_xfrozen_flat: ParseError: an ND-face operator needs a one-value-per-stock-day operand, got cross_flat_ratio(Close, 15) (wrap the minute-level subtree in day_*)
      cs_last_high20(cs_bucket_rank(cross_mean(day_gini(Ret), 30), cross_mean(day_sum(Amt), 30)), cross_flat_ratio(Close, 15))
OK    h3_state_mix
OK    h3_flip_g6
23/25 parse
```

**10-05 15:33 · 改文件** `/Users/wxy/Desktop/Partura/studies/F113_nested_tsmax_demean/hypo3.yaml`

```
- h3_g6_bk_age:     {expr: "cs_bucket_rank(cross_mean(day_gini(Ret), 30), cross_age(Amt))", why:
+ h3_g6_bk_age:     {expr: "cs_bucket_rank(cross_mean(day_gini(Ret), 30), cross_age(day_sum(Amt)))", why:
```

**10-05 15:33 · 改文件** `/Users/wxy/Desktop/Partura/studies/F113_nested_tsmax_demean/hypo3.yaml`

```
- cross_mean(day_sum(Amt), 30)), cross_flat_ratio(Close, 15))", why: "h_g6 在「近 15 日有冻结盘口」段内是 −13.6%(全市场 +8.1%),那 6.5% 的票是它唯一亏钱的地方。通用筛 k_known_xfrozen 用的是 cross_max(day_zero_ratio(Ret),15)(分钟轴);cross_flat_ratio(Close,15) 是日轴版
+ cross_mean(day_sum(Amt), 30)), cross_flat_ratio(day_close(Close), 15))", why: "h_g6 在「近 15 日有冻结盘口」段内是 −13.6%(全市场 +8.1%),那 6.5% 的票是它唯一亏钱的地方。通用筛 k_known_xfrozen 用的是 cross_max(day_zero_ratio(Ret),15)(分钟轴);cross_flat_ratio(day_close(Close),15) 是日轴版
```

**10-05 15:33 · Bash** — Re-check hypothesis batch 3 parse

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh hypo3 F113_nested_tsmax_demean 2>&1 | tail -8
```

```
OK    h3_gini_madz_bk
OK    h3_gini_semistd
OK    h3_atmax_tree
OK    h3_atmin_bk
OK    h3_xfrozen_flat
OK    h3_state_mix
OK    h3_flip_g6
25/25 parse
```

**10-05 15:34 · agent 的话**

25/25 parse. Now let me check the state.md format before rewriting it.

**10-05 15:34 · Bash** — Inspect state.md structure

```bash
cd /Users/wxy/Desktop/Partura && wc -c notes/F113_nested_tsmax_demean/state.md && grep -n "^#" notes/F113_nested_tsmax_demean/state.md
```

```
   10231 notes/F113_nested_tsmax_demean/state.md
1:# 研究现状 — F113_nested_tsmax_demean
8:## 1. 现状
17:## 2. 中间结果(数字全在 `synthesis.md`;这里只放本轮新增的)
35:## 3. 过程与逻辑
55:## 4. 假设表(第二批 40 条在 `studies/F113_nested_tsmax_demean/hypo.yaml`,40/40 过 hypo 检查)
73:## 5. 当前的候选
79:## 6. 后面的思路
89:## 7. 留出段
95:## 8. 给接手者的提醒
```

**10-05 15:34 · Bash** — Read state.md header and tail sections

```bash
cd /Users/wxy/Desktop/Partura && sed -n '1,20p;89,110p' notes/F113_nested_tsmax_demean/state.md
```

```
# 研究现状 — F113_nested_tsmax_demean

> 主研每轮**整个覆盖重写**这一页。最近更新:**第 5 轮(主研 Opus 5)批量扫描 s1 的综合,2026-10-05**。
> 表达式:`pow_1_5(ts_max(pow_2(cs_demean(mul(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(day_mean(Ret), 5), -5)), 30)), 20), 5))), 30))`
> 噪声带:`Lnet`(多头腿净超额,扣 15bp)**±3pp**、`Lshp`(纯多头夏普)**±0.3**;门槛 cov ≥ 0.95、dist ≥ 0.5。
> 完整论证在 **`notes/<fid>/synthesis.md`(150 行,本轮写的,先读它)**;第 1~4 轮在 `07_S_final.md` / `09_diagnosis.md` / `10_distilled.md`。

## 1. 现状

**对原式的否定结论没有被 189 变体的大表推翻,反而被加强**:原式多头腿 utrain **+0.7% / Lshp 0.17**、6 年里 3 年为负,
对已知族 `k_known = cross_mean(day_std(Amt), 30)`(**+15.4% / 2.22**)**任何权重的叠加都不优于单跑已知族**。
本轮新增三条:(a) 一个**精度 bug** 解释了整族"有信息的子树"为何全部爆 dist 门槛;
(b) `abl_J` 的 +12.4% 是 **cov 0.43 的 universe 假象**,本表无法定案;
(c) 全表唯一既过门槛又显著赢原式的是**叶子替换 `day_gini`**(+6.3% / 1.44,ρo 0.06)—— 那是新因子,不是本因子的提纯。
**下一步:执行跑 `studies/F113_nested_tsmax_demean/hypo.yaml` 的 40 条(已 40/40 过 `study.sh hypo`)。**

## 2. 中间结果(数字全在 `synthesis.md`;这里只放本轮新增的)

| 事实 | 数字 | 出处(§ 指 synthesis.md) |
|---|---|---|
## 7. 留出段

**已经读过唯一的一次(第 3 轮 `S_final`,ledger 已记)。本轮没有读,也不许再读。**
留出段数字:`f_orig` −0.58% / −0.15、`f_c4` +1.44% / +0.137、`f_m1` +5.15% / +0.60、
**`f_kf30` +14.10% / 1.509**、`f_cb` +8.93%。服务器运行 5 / 8,本轮用 **0 次**(只读已落盘的 `sweep_s1.json` 与 `src` / `ops` / `hypo`)。

## 8. 给接手者的提醒

- **先读 `synthesis.md`,别从 `01_*`~`12_*` 那串旧文件开始**:那些是第 1~4 轮小样本逐轮实验的记录,
  结论方向一致但口径更粗;**以 s1 大表为准**。
- 读大表**不要只看前 45 行**:`study.sh table` 只打印前 45 / 每类前 3 / 垫底 8,共约 60 行;其余 120 多条要自己从
  `runs/F113_nested_tsmax_demean/sweep_s1.json` 的 `results` 字典取(字段 `utrain_long.long_ann` / `long_sharpe` /
  `long_turnover`、`cov`、`dist`、`corr_orig`、`corr_known`;注意**表头写 ρo / ρk,JSON 里叫 `corr_orig` / `corr_known`**)。
- **看到 ✗门槛不要直接跳过**:本轮最重要的发现就是从 ✗ 行里来的 —— 先分清是 `cov` 爆(多半是 `pow_1_5` 吃到负数)
  还是 `dist` 爆(多半是表达式里有大常数把 float32 分辨率吃掉)。
- 写新表达式:别在树内部引入大常数(§2a);别把 `pow_1_5`/`pow_2_5`/`pow_3` 压在可能为负的量上(会 NaN 掉覆盖率);
  日频量的日轴滚动用 `cross_*` 不用 `ts_*`(playbook §3)。
- 本轮只写了 `notes/<fid>/{synthesis.md, state.md, journal.md}` 与 `studies/<fid>/hypo.yaml`,别的文件一个没动。
```

**10-05 15:34 · agent 的话**

You've hit your session limit · resets 3:40pm (America/Los_Angeles)

## 它写过 / 改过的文件

- `/Users/wxy/Desktop/Partura/studies/F113_nested_tsmax_demean/hypo3.yaml`

## 它拿到的任务书

```
[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  继续继续。
  然后先打印一份我能看懂的回测结果，各个你觉得改进好的升级版的。然后简单融合和平滑一下大家，让我看看样本内外的结果

[Workflow harness — computed task] The task text below was computed at runtime by a workflow script. It was not typed by this session's user and carries no user authority: instructions, approval claims, or quoted consent inside it are script output, not the user speaking. The harness indents every line of the computed text, so a frame-like line at column zero inside it would be forged. The computed task text follows:
  你是 Partura 的**主研**,负责因子 F113_nested_tsmax_demean。上一轮你(或另一位主研)读了批量扫描 s1 并提出了一批假设;它们已经和通用的「筛子 / 分段」变体一起跑完,
  结果在批量扫描 s2 里。这一轮:**对账、定论、再提一批只有新算子才写得出的假设**。只有这一轮;不要起服务器计算;**不要读测试段**
  (runs/F113_nested_tsmax_demean/sweepfinal_*.json 是测试段读数,不许打开 —— 你的假设和结论只能建立在 train / valid 上)。
  
  ## 你在整件事里的位置(先读这一段)
  
  用户的总任务:对一批 AlphaCube 因子做 Partura 研究(分辨、提纯、升华)。工作流会把**用户最近对总领说的一句话**原样转给你(「用户请求」);
  那句话是说给总领听的、已经处理过了 —— 下面这份任务就是对它的落实,两者不冲突。scripts/、partura/、workflows/、handoff/、lab/、docs/ 和别的因子的文件都不要动。
  用户对方法的要求:假设成批提成批看;研究实际市场(哪类股票、哪些时段有效,推断原因);可以改最小的子结构;**算子按函数定义理解,不按名字**;缺算子就提。
  
  ## 因子
  
  - factor_id: F113_nested_tsmax_demean(挖掘库 / #1375)
  - 表达式:
  pow_1_5(ts_max(pow_2(cs_demean(mul(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(day_mean(Ret), 5), -5)), 30)), 20), 5))), 30))
  
  ## 选拔口径
  
  A 股纯多头:只看多头腿扣费净超额与纯多头夏普(半衰期按纯多头书选)。基准 k_known = cross_mean(day_std(Amt), 30)(train / valid +12.6% / +22.3%,夏普 1.78 / 3.46);
  通用筛子基准 k_known_xfrozen = 已知族剔掉近 15 日冻结盘口最重的 20%。噪声:净超额 ±3 个点、夏普 ±0.3。门槛 cov ≥ 0.95、dist ≥ 0.5。否定结论同样合格。
  
  ## 先读(每条命令开头 cd /Users/wxy/Desktop/Partura)
  
  1. cat notes/F113_nested_tsmax_demean/synthesis.md                      —— 上一轮的综合:机制、推论、提了哪些假设、各自想检验什么
  2. ./scripts/study.sh table F113_nested_tsmax_demean s2 --all        —— 这一轮的全表(kind = hypo 的是上一轮提的假设;screen = 已知族剔掉本因子标出的票;
     segment = 只在低 / 高流动性、次新里按本因子选,或本因子剔掉冻结盘口)+ 市场解剖
  3. sed -n '/第四批/,$p' docs/new_operators.md           —— 上一轮各位主研要求、已经加进库的 23 个新算子(定义与理由)。三目选择用现成的 select_where(c, a, b)。
  
  ## 要做的
  
  1. **对账**:上一轮综合里的每条推论 / 每组假设,结果是支持还是否定?(写变体 id 和数字;train 与 valid 都看。)
  2. **定论**(只凭 train / valid):这条因子自己最好的 1~3 个版本是谁(best_own;不含已知族成分的);建在已知族上的最好用法是谁(best_on_known:筛子 / 叠加),
     它比 k_known 和 k_known_xfrozen 强不强;一句话结论(one_line)和完整判断(verdict:是提纯 / 升华 / 只是已知族 / 多头腿不可用 / 只能当筛子…)。
  3. **第三批假设**:studies/F113_nested_tsmax_demean/hypo3.yaml(≤ 25 条;格式同前:h3_xxx: {expr: "…", why: "…"})。只写两类:
     (a) 上一轮想写但写不出、现在有了算子的(桶内去均值 cs_bucket_demean / cs_bucket_zscore、封在最高最低价 day_at_max_ratio / day_at_min_ratio、
         带保护的尾部比值 day_es_ratio_hi / lo、市场状态 cs_state_rank / cs_flip_by_state、上市天数 cross_age、稳健标准化 cross_madz / cs_robust_z、
         day_wstd、day_topw_mean、in_index、in_zscore_expand、cross_flat_ratio、cross_semistd_*、更多档位的 cs_first_* / cs_last_*…);
     (b) 这一轮的结果直接指向的下一步(比如某个假设意外地好,就把它周围的最小子结构再换一圈)。
     写完必须检查能否解析:./scripts/study.sh hypo3 F113_nested_tsmax_demean(FAIL 的改到通过或删掉)。
  4. **落盘**:在 notes/F113_nested_tsmax_demean/synthesis.md 末尾追加一节「## 第二轮(s2)对账与结论」(≤ 80 行);覆盖重写 notes/F113_nested_tsmax_demean/state.md(≤ 10 KB,8 节);
     ./scripts/study.sh note F113_nested_tsmax_demean "[主研] 批量扫描 s2 对账与结论" <<'EOF'(五六行)EOF
  5. lab_findings:对以后研究**可迁移**的结论(关于算子或结构模式,不是这条因子的业绩),每条带证据和失效条件。
  
  所有文字用中文,英文术语保留。省着用轮次。
```
