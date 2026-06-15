# 布尔类型bool
"""
- 只有 `True` 和 `False`（`True==1`，`False==0`，但 `is` 判断身份(即是否是同一个对象，是否在内存中占据相同的位置)）
- 被判断成假值的有：`None`、`0`、`0.0`、空容器（空列表 / 元组 / 字典等）、`False`
"""

print(bool(None))

print(True ==0 )
print(False ==0 )
#print(True is 1)


print("===================")
num=100
num2=100
print(num is num2)
print("===================")

print(bool([]))
print(bool([1,2,3]))


