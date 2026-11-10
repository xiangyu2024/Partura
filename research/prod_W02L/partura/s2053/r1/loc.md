# 定位:种子 2053,P 组,第 1 轮(只含 train / valid)

快照:prods2053M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(0 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|

## 共性:0 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|

## 拆解(0 次评估)

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)

## 总领补注(2026-11-10):为什么这一节是空的

本流第 1 批 B157(主题 T30,结构核心 `day_argmax(in_local_mean(in_slice(Volume, a, b), 5))`)的 9 个成员在第 0 步**全部没过闸门**,所以没有 head、也没有 material:
覆盖率都是 0.999,但「不同取值比例」只有 0.035–0.053(闸门要求 ≥ 0.5)。原因是它们输出的是日内分钟序号(0–236 的整数),每天截面上只有两百来个不同值，不是因子退化。

| 成员 | 表达式 |
|---|---|
| L911 | day_argmax(in_local_mean(in_slice(Volume, 2, 237), 5)) |
| L928 | day_argmax(in_local_mean(in_slice(Volume, 16, 226), 5)) |
| L945 | day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)) |
| L912 / L929 / L946 | day_argmin(in_slice_from_start(<同上的平滑量>, day_argmax(<同上>))):峰值之前的低谷时刻 |
| L913 / L930 / L947 | day_argmin(in_slice_to_end(<同上的平滑量>, day_argmax(<同上>))):峰值之后的低谷时刻 |

可以这样用：把这个核心在日期方向上平滑(例如 cross_mean / cross_ema 若干天)或做截面变换以后，就是连续值，可以作 E 位核心;也可以把它当成 N 位的思路来源(成交量峰值出现在什么时候)。本轮没有 R(没有 head)。
