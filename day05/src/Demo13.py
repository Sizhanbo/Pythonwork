# 动态操作

# 动态添加类方法 / 静态方法

class Person:
    pass

# 动态添加类方法
@classmethod
def abc(cls):
    print(f"类名: {cls.__name__}")

Person.get_class = abc
Person.get_class()

@staticmethod
def xyz():
    print("这是一个静态方法")

Person.say_hello = xyz
Person.say_hello()