# __init__构造方法
class Person:

    # 可以接收多个参数，用于对象初始化，包括对象的属性赋值
    def __init__(self,name,age):
        self.abc = 123
        print("我创建了！")
        self.name = name
        self.age = age
        for i in range(10):
            print(i)
        return # 可以存在于构造方法，但是仅用于标识函数结束

p = Person("张三",18)
# print(p)
# print(p.abc)
# print(p.name)
# print(p.age)

# p = Person()
# print(p)

