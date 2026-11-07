# 种子 912 笔记本(PI)

## 第 1 轮

### 对本种子 alpha 来源的信念(只依据 M 第 1 批的 1 个 head 和 112 个已评分候选)

- 唯一的 head:`cs_first_high40(ts_var(day_durbin_watson(Vwap), 1), ts_var(sqrt(day_durbin_watson(Vwap)), 10))`,sign -1,hl 5,train +0.58 / valid +1.66。
- 读源码后的事实:
  - `day_durbin_watson` 不去均值,是 sum(diff^2) / sum(x^2)(分母 +1e-8)。对价格 Vwap 就是 分钟 Vwap 变动均方 / 价格^2,
    即日内已实现方差的无量纲版本(含低价股的最小变动价位效应);sqrt 后是日内已实现波动率。
  - `ts_var(sqrt(DW), 10)` = 已实现波动率的 10 日方差 = vol-of-vol(记作 C)。
  - `ts_var(x, 1)`:`nanstd_last` 在窗口只有 1 个点或全是 NaN 时返回 0,所以 `ts_var(DW, 1)` 是整张常数 0 面板。
    `day_corr(Low, Low)`、`day_pos_ratio(Vwap)` 也几乎是常数(corr 自己对自己约 1,正比例约 1)。M 的 GP 把这类常数当作 并列全按列序打破 的键来用。
  - `cs_first_high40(y, x)` = rank(y) + 1(x 在前 40% 的整块并列内);y 常数 => rank(y) 就是股票列序。sign -1 => 做多的是 非高 vol-of-vol 带 里列序靠前的名字。
    列序对应交易所与板块(规则 §4 明说携带板块信息),具体是哪一段我不知道(若按代码排序,最靠前的大概是深市主板 / 中小板,但没有证据)。
  - 拆解印证:常数键换成 DW 本身 train 从 +0.58 掉到 -1.75;去 sqrt 或 Vwap 换 Close 变化不大(+0.40 / +0.24);窗口 1->2 掉到 -0.85;
    门槛自己单独作为信号(分子 ts_var(sqrt(DW),10)) train 只有 +0.07、valid +1.04。
- 信念:head 的 alpha 主要来自 板块 / 列序偏好 和 一个 low vol-of-vol 带的组合,vol-of-vol 的连续排序本身在 train 上几乎没有内容(+0.07),
  valid 上有(+1.04),两段不一致,所以不能直接相信它是稳定的 vol-of-vol 溢价。
  - 对 OOS 的担心:板块相对表现随行情轮动(2018-2021 与 2022-2023 的主板 / 创业板相对强弱不同),valid +1.66 比 train +0.58 高很多,可能含有这个成分。
- 富集结果里 C 的含有者均值差 +1.46(32 个候选),基本都是 带门槛 的写法,不能分开 门槛 与 vol-of-vol。

### 本轮三个任务与事先预测

1. **E 位,核心 C = `ts_var(sqrt(day_durbin_watson(Vwap)), 10)`**,12 个种子,全部是连续 rank 构造(水平中性 bucket_rank、rank 差、自身历史 rank 变化、Low 路径对照、BoardCode 板块优先、ListAge 排除),
   不含常数键与分位门槛。
   - 预测:产出 >= 1 个 head 的概率约 25%。
   - 若产出,最可能是 `add(cs_rank(C), BoardCode)` 或带 ListAge 的写法(它们保住了 板块 成分),sign -1,hl 5 或 20,valid 比 train 高;
     纯水平中性的写法(bucket_rank 对波动水平 / 市值 / 成交额,rank 差)在 train 上多半 < 0.5,因为我认为连续 vol-of-vol 排序自己没有稳定内容。
   - 若 E 全灭而 board 键的写法也不行:说明 head 的收益依赖 列序 而不是 BoardCode 能表达的板块,下一轮要想别的办法抓列序(例如 ListAge / LimitWidth 的并列块结构)。
2. **N 位,隔夜 / 盘中拆分**(Ov = log Open - log 前收,Id = log Close - log Open),13 个种子:水平、差、衔接(ts_corr / ts_regbeta / sign 乘积)、skew、方差占比、ListAge 排除。
   - 预测:产出 head 的概率约 12%,较有希望的是 sub(ts_mean(cs_rank Ov, 20), ts_mean(cs_rank Id, 20)) 一族,方向未知(文献主张隔夜持续、盘中反转,但 A 股可能相反)。
   - 主要失败模式:新股连板、涨跌停锁死的名字在两端占满;20 日总收益(反转控制)里 Ov + Id 的重叠;换手 / 流动性相关;
     ts_corr / ts_regbeta 在 40 日窗口不满时(上市 / 复牌后)退化。
   - 这是本种子第 1 个 N 位,必须让它至少有一个能通过审计;若审计没通过,第 2 轮另写一个 N(备选:把 vol-of-vol 推广到别的日内结构统计的跨日不稳定性,
     如 ts_std(day_gini(Amt), 20)、ts_std(day_centroid(Amt), 20)、ts_std(day_autocorr_n1(in_pct(Vwap, 1)), 20))。
3. **R 组,10 个变体**,把 head 里的常数键换成显式的 BoardCode / LimitWidth / ListAge(及其反向),并改窗口 / 带宽 / sqrt / Vwap->Close。
   - 预测:任何变体 score >= 0.68 并 替换 / 收录 的概率约 10%。
   - 更重要的是信息:BoardCode 版本 ≈ head(若不是,说明列序里有 BoardCode 表达不了的信息);neg(BoardCode) 版本大幅变差 => 偏好 主板;
     LimitWidth / ListAge 版本和 BoardCode 版本对比 => 板块的哪个维度(涨跌幅限制 / 上市年龄)有内容。

### 上一轮预测对不对

(第 1 轮,没有上一轮。)

### 本轮做过的检查

- 全部 35 个表达式(E 12 + N 13 + R 10)在合成 cube(60 只 x 140 日,含停牌 / 未上市 / FloatCap 日频字段)上跑通,无报错,最近 60 日覆盖率 >= 0.8;
  这只能说明语法 / 形状没问题,合成数据里 BoardCode / ListAge 基本是常数,不说明任何收益。
- 没有任何分母含除法;所有 rank 构造有界。
- `c06_check.py 912 1`:ADMISSIBLE。
