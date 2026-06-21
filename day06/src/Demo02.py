# @property 装饰器可将方法伪装成属性，简化接口调用，同时支持读写控制。

# 被@property 装饰器修饰的方法，可以直接像属性一样访问
# 数据封装：实现对私有属性的安全访问
class Person:
    def __init__(self, age):

        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0 or age > 120:
            print('年龄范围错误')
            return
        self.__age = age
    @property
    def eat(self):
        print('吃吃吃')


p= Person(18)
p.eat
p.age = 180
print(p.age)

# 动态计算：返回基于其他属性计算得出的值
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14 * self._radius ** 2

c = Circle(5)
print(c.area)
