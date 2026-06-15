# 浮点型数据
"""
- 带小数点的数，计算可能有精度误差（可通过 `decimal` 模块解决）
- 支持科学计数法（如 `1.3e7` 表示 `13000000.0`）

计算机当中没有负数，也没有小数。
小数是经过整数算法记录的数据，是非精确数据，是近似数，存在误差

使用decimal来表示精确数字
"""

num = 0.1
print(num)
num2 = 0.2
print(num2)
num3 = num + num2
print(num3)   #0.30000000000000004
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2"))
print(Decimal(0.1) + Decimal(0.2))

