# 字典
# 可以通过 {} 或 dict () 创建字典。

# 创建
shuihu = {"三国演义": "诸葛亮", "红楼梦": "王宝川", "水浒传": "宋江"}
dict1 = dict()
print(shuihu)
print(dict1)

baby = dict(name="小李",age=2,sex="男")
print(baby)

baby2 = dict([("name","小花"),("age",3),("sex","女")])
print(baby2)

digit_map = {x: x**2 for x in range(10)}
print(digit_map)

# 访问字典
baby = dict(name="李雷",age=2,sex="男")
print(baby["name"])
# print(baby["height"])  # 获取一个不存在的键，会直接报错
print(baby.get("name"))
print(baby.get("height"))  # 获取一个不存在的键, 不会报错，返回None值
print(baby.get("height",180))  # 默认值180

# 增删改
baby = dict(name="李雷",age=2,sex="男")
baby["height"] = 200
print(baby)
baby["name"] = "小花"
print(baby)

del baby["height"]
print(baby)

print(baby.pop("name"))
print(baby)

baby.clear()
print(baby)

# 其他动作
baby = dict(name="李雷",age=2,sex="男")
print("name" in baby)
print("height" in baby)
print(len(baby))

#遍历操作
# 遍历键
for key in baby.keys():
    print(key)

# 遍历值
for value in baby.values():
    print(value)

# 遍历  通过键获取值
for key in baby.keys():
    print(f"键：{key},值: {baby[key]}")

# 建议的遍历方式
print(baby.items())

for k,v in baby.items():
    print(f"键：{k},值: {v}")