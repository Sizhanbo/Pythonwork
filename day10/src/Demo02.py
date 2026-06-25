import copy

user_data = [
    "张三",  # 顶层不可变数据（字符串）
    25,     # 顶层不可变数据（整数）
    ["北京", "13800138000"]  # 嵌套可变数据（列表）
]
# 复用上面的user_data原始数据
user_data_deep = copy.deepcopy(user_data)

# 验证内存地址变化
print("深拷贝嵌套列表地址:", id(user_data_deep[2]))  # 输出：28974256（新地址）
print("地址是否独立:", id(user_data[2]) != id(user_data_deep[2])) # 输出：True

# 修改原始数据的嵌套内容（深拷贝不受影响）
user_data[2][1] = "13700137000"
print("修改后 - 原始嵌套数据:", user_data[2][1])       # 输出：13700137000
print("修改后 - 深拷贝嵌套数据:", user_data_deep[2][1])  # 输出：13900139000（完全独立）
