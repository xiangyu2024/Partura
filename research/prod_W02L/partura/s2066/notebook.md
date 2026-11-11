
## 第 1 轮

**信念**:本批 10 个候选全是 in_cov(Ret, Close, w) 一族(nt_cs_normalize 逐分钟截面标准化 + day_mean),3 个 head 的 score 全为负(-1.14 ~ -1.15,方向 -1),没有真正的发现;Close->Vwap 后 train/valid 符号翻转,说明这个量的截面主要是价格水平尺度,alpha 来源不明。所有 head 含 nt_*,E 位的核心无合法子树(nt_ 种子禁用),所以本轮 2 个位都是 N,另给 8 个 R 变体(in_corr 替换 in_cov)。
**事先预测**:
- N1(成交时间重心 day_centroid):可能出 head 的概率约 30%;若出,会是 Amt/Volume 质心的多日平滑 + 流动性分桶,来源是持仓结构(机构尾盘)。风险:被流动性/波动控制吃掉。
- N2(资金加权买卖方向 day_signed_ratio):出 head 的概率约 25%;若出,是 cross_zscore 或分桶版;风险是与 20 日反转相关。
- R:出替换/收录概率低(<10%),原 head 为负,in_corr(Ret, Amt) 是唯一值得一看的变体。
**上一轮预测**:无(第 1 轮)。
