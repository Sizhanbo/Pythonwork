import json

# 准备字典数据  >> 为了转成json字符串
data = {
    "name": "张三",
    "age": 25,
    "is_student": False,
    "hobbies": ["reading", "coding"]
}

json_str = json.dumps(data, ensure_ascii=False, indent=2)
print(json_str)
print(type(json_str))

# 准备json字符串 >> 为了转成字典
data2 = json.loads(json_str)
print(data)
print(data2)