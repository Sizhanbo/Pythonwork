# 导入模块  给与别名
import math_tools as mt

# 使用模块别名.成员的方式调用模块成员
#print(mt.__format_number(1.23456)) #程序员不应该自己手动调用模块中带_的功能
print(mt.multiply(1, 2))

print(mt.PI)

p = mt.Person("jack",18)
p.hello()
p._hello()  # 程序员应该自己不手动调用在类中_定义的私有功能  __hello方法被语法限制，无法调用

print(mt.__dict__)  # 可以看到模块中的属性
print(mt.Person.__dict__)   # 可以看到类中的属性
print(p.__dict__)  # 可以看到对象中的属性
