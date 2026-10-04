审查员的实验不是一个阶段:配置里没有 `SA_audit`,`runs/F104_kurt_masktop_amt/` 下也没有 `audit1.json`。它是一个 exec 脚本
(`studies/F104_kurt_masktop_amt/audit_span.py`,tag `audit1`,输出在 `logs/F104_kurt_masktop_amt_audit1.log`)。
报告只会自动收录 `07_<阶段 id>.md`(该阶段有结果时)和 `07x_*.md`,所以它的结果与解读写在 **`07x_audit.md`** 里(报告第 7 节末尾);这个文件只是指路。
