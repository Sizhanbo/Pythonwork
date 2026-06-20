# 动态操作
class Person:
    pass

p = Person()
p2 = Person()
print(p)
print(p2)

# 动态添加对象属性
p.name = "张三"
p.age = 18

print(p.name,p.age)
# print(p2.name,p2.age)