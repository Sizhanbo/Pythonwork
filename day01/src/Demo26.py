# for循环
"""
for 临时变量 in 可迭代对象:
    循环体
else:
    语句  # 循环正常结束时执行
"""

numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 定义变量记录索引
# index = 0
#
# for value in numbers:
#     print(f"当前遍历到的数字是：{index}：{value}")
#     index += 1

# 了解  枚举方式
# for index,value in enumerate(numbers):
#     print(f"当前遍历到的数字是：{index}：{value}")
#     index += 1

# 遍历字符串
# for i in "hello world":
#     print(i)

# range列表
# for i in range(10):
# 	print(i)

# range与列表一起使用
# numbers = [2, 3, 5, 7, 11, 13, 17, 19]
# length = len(numbers)
# print(length)  # 获取列表长度
#
# for index  in range(len(numbers)):
#     print(f"索引{index}：{numbers[index]}")


for numx in range(10,20,3):
    print(numx)