# 继承
"""
class 子类名(父类名):
    子类体
"""


# Person为父类，Student为子类
# 父类
class Person:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name}吃了")


# 子类
class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def study(self):
        print(f"{self.name}在{self.grade}学习")


p = Person("张三")
p.eat()
s = Student("张三", "大一")
print(s.name)
s.study()