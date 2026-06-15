"""
自动类型转换（隐式转换）**：

- 不同数值类型运算时，小类型转大类型（如 `int + float = float`）
- 整数除法结果为浮点数（如 `9 / 1 = 9.0`）
- 整数与字符串无法隐式转换
"""

int1=100
float1=1.0
print(int1+float1)
print(type(int1))
print(type(float1))
print(type(int1+float1))

"""
强制类型转换（显式转换）
格式
要转换的类型关键字(要转换的值)
"""

str1 = "100"
int2 = int(str1)
print(int2)
print(type(int2))

