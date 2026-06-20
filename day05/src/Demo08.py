# python中不同方法的定义
# 实例方法    类方法     静态方法
class Person:

    home = "中国"

    def __init__(self,name):
        self.name = name  # 实例属性

    # 实例方法
    def introduce(self):
        print(f"我叫{self.name}")
        print(f"我来自{Person.home}")  # 实例犯法，可以访问类属性
        # print(f"我来自{self.home}")

    # 类方法
    @classmethod
    def get_home(cls):
        print(f"所有人类来自: {cls.home}")
        # print(f"所有人类来自: {cls.name}")  # 类方法，无法访问对象属性

    # 静态方法
    @staticmethod
    def my_static_method():
        print("这是一个静态方法")
        # print(f"所有人类来自: {name}")  # 静态方法，无法访问对象属性
        print(f"所有人类来自: {Person.home}") # 静态方法，虽然可以访问类属性，但是不建议使用，因为这种使用方式，没有其定义时的内部关系


    #调用实例方法
p = Person("张三")
p2 = Person("李四")

p.introduce()
p2.introduce()

#调用类方法
Person.get_home()

#调用静态
Person.my_static_method()


