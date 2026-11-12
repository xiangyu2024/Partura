
## 第 2 轮

**信念**:第 1 轮 N 位(质心、signed_ratio)和 R 都没产出 head;本批 heads 全为负分,只有两个子树在共性表里明显抬分:day_centroid(pow_3(pow_1_5(Volume)))(+2.37)和 day_hurst(cross_ema(pow_1_5(Volume),60))(+1.83)。第 1 轮含质心的 cross_min 外围最好 -0.34,说明质心核心比 in_cov / 偏度峰度族的底子好,但外围还没找对。heads 含 nt_* 不能当核心。
**上一轮预测**:预测 N1(质心)30% 出 head、N2(signed_ratio)25%、R <10%——实际三者都 0 个 head,质心最接近(-0.34)。预测方向对(质心 > signed_ratio),过线概率高估。
**本轮事先预测**:
- E1(质心核心,外围 zscore/stddev/分桶/与 Ret 质心作差):出 head 概率约 25%;若出,最可能是分桶后的 cross_zscore 或与 Ret 质心差,来源是机构调仓日放量时点漂移。风险:被流动性/市值控制吃掉。
- E2(Hurst 核心):出 head 概率约 15%;Hurst 噪声大,若出会是 20 日均值 / 分桶版。
- 不做 R:本批可 R 的 head 只有 nt_* 版本(R 已试),变体 +0.18 的窗口调整不改本质。
