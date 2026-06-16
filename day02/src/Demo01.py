# 列表 List
# 格式: 变量 = []
# 直接给值
list1 = [1, 2, 3, 4, 5]
print(list1)
print("------------------------")
list3=[x**2 for x in range(5)]
print(list3)


print("------------------------")
# 通过索引访问
print(list1[2])  # 正向索引
print(list1[-2])  # 反向索引
print("------------------------")
list2 = list1[1:3]
print(list2)
print("------------------------")
