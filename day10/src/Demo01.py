import copy

# 定义含嵌套列表的原始数据（模拟复杂业务数据）
user_data = [
    "张三",  # 顶层不可变数据（字符串）
    25,     # 顶层不可变数据（整数）
    ["北京", "13800138000"]  # 嵌套可变数据（列表）
]

# 浅拷贝
user_data_copy = copy.copy(user_data)

# 验证内存地址变化
print("原始数据地址:", id(user_data))       # 输出：原始数据地址: 28974056
print("拷贝数据地址:", id(user_data_copy))  # 输出：拷贝数据地址: 28974120（顶层地址不同）
print("嵌套列表地址是否相同:", id(user_data[2]) == id(user_data_copy[2])) # 输出：True（嵌套对象共享）

# 修改顶层不可变数据（无影响）
user_data[0] = "李四"

print("修改顶层后 - 原始数据:", user_data[0])      # 输出：李四
print("修改顶层后 - 拷贝数据:", user_data_copy[0])  # 输出：张三（不受影响）

# 修改嵌套可变数据（同步变化）
user_data[2][1] = "13900139000"
print("修改嵌套后 - 原始数据:", user_data[2][1])       # 输出：13900139000
print("修改嵌套后 - 拷贝数据:", user_data_copy[2][1])  # 输出：13900139000（同步修改）