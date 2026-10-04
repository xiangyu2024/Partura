审查员的反驳实验没有以配置阶段的形式存在:它是一个 exec 脚本(`studies/F101_day_shine_retstd/audit_1.py`,tag `audit1`),
配置里没有 `SA_audit` 阶段,`runs/F101_day_shine_retstd/` 下也没有 `audit1.json`,数字只在 `logs/F101_day_shine_retstd_audit1.log` 里。

报告生成器只收录「有阶段结果的 `07_<stage_id>.md`」和 `07x_*.md`,所以这份文件不会进报告。它的内容写在三处:

- `07x_review1_audit.md` —— 审查员脚本的四段结果(A:Volume 是否必需;B:原式自己的双重排序与平台对照;C:空头腿按收益贡献拆;D:F001 的日内波动 + 极值记忆族)和我的核对。
- `07_SR_rivals.md` —— 我用正式口径补的阶段(tag `rev1`),独立复现了 A 段的三条折叠,并把比值和 F001 族的折叠放进了正式表。
- `07x_review2_rev2.md` —— 我补的分析(tag `rev2`):排名折叠空头腿的低侧 / 高侧逐年拆分、`J == 0` 的收益贡献与构成、多头十分位对平台的逐年对照、三个 F001 家族、同格子比较、无掩码的爆发比。

三处都只读 train / valid。留出段的读取次数仍然是 1(`runs/F101_day_shine_retstd/ledger.json`)。
