# 类的定义
class Person:
    """
    定义人类
    """
    # 类属性(被所有对象共享使用)
    home = "earth"

    # 构造方法(用于初始化实例属性)
    # 空参构造
    # def __init__(self):
    #     """
    #     初始化对象
    #     """
    #     self.age = 0

    # 带参构造
    def __init__(self,age):
        """
        初始化对象
        """
        self.age = age

    def eat(self):
        print(f"{self.age}岁的我在eating...")

    def drink(self):
        print("drinking...")

# 类的使用
# 直接通过 “类名.成员名” 访问类的属性或方法（无需创建对象）,较少使用。
# 访问类属性
Person.home = "moon"
print(Person.home)
# print(Person.age)  # AttributeError: type object 'Person' has no attribute 'age'


# 访问类方法
func_eat = Person.eat
print(func_eat)
# func_eat()  # 因为这里调用Person中的eat方法时，需要一个Person对象作为self传入的，而此时，没有Person对象，所以报错！

# 访问说明文档
print(Person.__doc__)

# 类的实例化
# 通过 “类名 ()” 创建对象（实例），并通过 “对象.成员名” 访问实例属性和方法。
# 创建对象(实例化)
p = Person(18)
print(p)

# 用对象访问属性
# 类属性
print(p.home)
# 对象属性
print(p.age)

# 调用实例方法
p.eat()
p.drink()

# 虽然使用类名获取了某个方法，但是该方法，也可以被正常调用的,因为调用方法时，可以手动传入要调用该方法的对象，相当于给函数的self赋值了！
func_eat = Person.eat
func_eat(p)
Person.eat(p)