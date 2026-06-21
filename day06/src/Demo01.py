# 封装person类 隐藏age
# python 中通过 “双下划线”（`__属性名`/`__方法名`）实现私有化
# 私有化后的成员仅能在类内部访问
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0 and age <= 120:
            self.__age = age
        else:
            print("年龄范围错误")

    def show(self):
        print("姓名：%s, 年龄：%d" % (self.name, self.__age))



p=Person("张三", 18)
p.show()
p.set_age(p.get_age()-10)
p.show()
