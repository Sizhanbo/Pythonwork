#动态操作
import types

# 用python提供的语法完成的动态添加对象方法
class Person:

    def __init__(self,name):
        self.name = name


p = Person("张三")
# 动态添加对象方法

# 定义一个普通函数
def func_eat(self):
    print(f"{self.name}在吃吃吃")

p.eat = types.MethodType(func_eat,p)
# 满足了，在Person类中定义一个对象方法

p.eat()