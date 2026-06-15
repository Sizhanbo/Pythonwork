# 逻辑运算符   通常是布尔值参与逻辑计算
# 与运算 必须同时满足为真，否则为假
boo1 = True
boo2 = False
boo3 = True
boo4 = False

print(boo1 and boo2)
print(boo1 and boo3)
print(boo2 and boo4)

age = 18
height = 130
print(age >= 18 and height >= 180)

# 或运算 只要满足一个为真，则结果为真
print(age >= 18 or height >= 180)

# 非运算 逻辑取反
print(not boo1)