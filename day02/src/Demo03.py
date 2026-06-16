# 列表遍历
list1 = [10, 20, 30, 40, 50]
for x, y in enumerate(list1):
    print(f"x={x},y={y}")
for i in range(len(list1)):
    print(f"本次遍历的元素是：list1[{i}]:{list1[i]}")

# 列表推导式
# 立方列表
squares = [x ** 2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
# 使用现有列表的列表推导式
list1 = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in list1]
print(squares)  # [1, 4, 9, 16, 25]

# 带条件筛选
list2 = [x for x in range(5) if x % 2 == 0]
print(list2)

# 多循环嵌套
list3 = [(i, j) for i in [1, 2, 3] for j in ['a', 'b']]  # 笛卡尔积
print(list3)

# 列表相加
list1 = [100, 200, 300]
list2 = ["a", "b", "c"]
print(list1 + list2)  # [100, 200, 300, 'a', 'b', 'c']

# 列表相乘
list1 = [100, 200, 300]
print(list1 * 2)  # [100, 200, 300, 100, 200, 300]

# 检查成员
list1 = [100, 200, 300]
print(100 in list1)  # True

# 获取长度
list1 = [100, 200, 300]
print(len(list1))  # 3

# 最值/求和
list1 = [100, 200, 300, 400, 500]
print(max(list1))  # 500
print(min(list1))  # 100
print(sum(list1))  # 1500

