# @property装饰的方法不要和变量重名，否则可能导致无限递归。

# 这里 name属性与name函数同名，报错！如果没有在__init__当中去定义name，会报错RecursionError: maximum recursion depth exceeded




#一个__修饰的属性，是私有属性，强制的语法上不能访问该名称的属性(但是，本质上不是不能访问，本质上是python将我们定义的__属性改名了)
class Person:
    def __init__(self):
        self.__name = "zs"

p = Person()
# print(p.__name)
print(p.__dict__)
print(p._Person__name)