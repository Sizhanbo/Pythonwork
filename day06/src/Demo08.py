# 多态应用
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class Dog(Animal):

    def make_sound(self):
        print("汪汪汪")

class Cat(Animal):

    def make_sound(self):
        print("喵喵喵")

class Bird(Animal):

    def make_sound(self):
        print("叽叽喳喳")

d = Dog("旺财")
c = Cat("咪咪")
b = Bird("小云")
a = Animal("小动物")


# 针对的是父类功能定义了一个函数
def animal_sound(animal):

    print(f"我的名字叫{animal.name}")
    animal.make_sound()

# 虽然定义方法时，是针对父类类型定义的方法，接收父类类型，因为父类类型有name属性，有make_sound方法，我才能像上述那样访问属性，调用函数
# 但是，在调用时，传入的参数，是子类对象，子类对象有make_sound方法
animal_sound(a)
animal_sound(d)
animal_sound(c)
animal_sound(b)

class Pig(Animal):
    def make_sound(self):
        print("哼哼哼")

animal_sound(Pig("元宝"))