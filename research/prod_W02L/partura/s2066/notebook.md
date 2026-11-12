
## 第 1 轮

**信念**:本批 10 个候选全是 in_cov(Ret, Close, w) 一族(nt_cs_normalize 逐分钟截面标准化 + day_mean),3 个 head 的 score 全为负(-1.14 ~ -1.15,方向 -1),没有真正的发现;Close->Vwap 后 train/valid 符号翻转,说明这个量的截面主要是价格水平尺度,alpha 来源不明。所有 head 含 nt_*,E 位的核心无合法子树(nt_ 种子禁用),所以本轮 2 个位都是 N,另给 8 个 R 变体(in_corr 替换 in_cov)。
**事先预测**:
- N1(成交时间重心 day_centroid):可能出 head 的概率约 30%;若出,会是 Amt/Volume 质心的多日平滑 + 流动性分桶,来源是持仓结构(机构尾盘)。风险:被流动性/波动控制吃掉。
- N2(资金加权买卖方向 day_signed_ratio):出 head 的概率约 25%;若出,是 cross_zscore 或分桶版;风险是与 20 日反转相关。
- R:出替换/收录概率低(<10%),原 head 为负,in_corr(Ret, Amt) 是唯一值得一看的变体。
**上一轮预测**:无(第 1 轮)。

## 第 3 轮

**信念**:前两轮 4 个 GP 位 0 个 head。唯一正分线索是 Hurst 核心:sub(day_hurst(cross_ema(pow_1_5(Volume),60)), day_hurst(Volume)) train +1.23 / valid +0.27(典型日内量形状 vs 今日原始形状的持续性差)。质心核心(Volume^4.5 质心)只有 ts_min 型的 train 正 valid 负,不再押。cross_med(Ret,60) 与量形状矩的 head 全是 -2 级别,只当 R 的窗口调整来源。
**事先预测**:
- E(Hurst 核心,外围换成别字段 Hurst 差 / 分桶 / zscore):过线概率约 25%;若出,最可能是 sub(核心, day_hurst(Amt)) 或分桶版,valid 比 train 弱,机制是执行习惯。风险:valid 仍 <0.5。
- N(今日量形状对自身典型形状的相关 / L1 偏离):出 head 概率约 20%;day_corr 对停牌常数返回 0 可能引入伪影,L1 版更稳。风险被流动性控制吃掉。
- R:出收录/替换概率 <10%(头分 -2 以下,增益 0.4 也到不了 0.5)。
**上一轮预测对不对**:r2 预测 E-质心、E-Hurst 各约 30% 出 head,实际都 0;Hurst 位有正分(最好 +0.27)但没过 0.5,方向对、强度估高;质心位完全落空。
