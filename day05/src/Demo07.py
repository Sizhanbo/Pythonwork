# dict属性:用于描述对象的属性
class Person:

    """
    这是一个人类
    """

    location = "地球"

    def __init__(self,name):
        """
        初始化人类示例
        :param name: 起的名字
        """
        self.name = name
        self.age = 0
        self.stage = "婴儿"

    def grow_up(self):
        """
        成长
        :param person: 要成长的人
        """
        self.age += 1
        if self.age <= 3:
            self.stage = "婴儿"
        elif self.age < 18:
            self.stage = "少年"
        elif self.age < 60:
            self.stage = "成年"
        else:
            self.stage = "老年"

        print(f"我叫{self.name}，我今年{self.age}岁了，我是{self.stage}")

    def study(self):
        """
        学习
        """
        if self.stage == "少年":
            print(f"我叫{self.name}，我正在学校里，如饥似渴，疯狂汲取知识，不虚度每一天！")
        else:
            print(f"我叫{self.name}，我正在日常的生活点点滴滴中学习，成长，进步！")

    def work(self):
        """
        工作
        """
        print(Person.location)
        if self.stage == "成年":
            print(f"我叫{self.name}，我勤奋努力的工作，正在工作")
        else :
            print(f"我叫{self.name}，我不是成年人，我不用工作")

    def retire(self):
        """
        退休
        """
        if self.stage == "老年":
            print(f"我叫{self.name}，我正在退休，正在享受退休生活")

# 创建对象，调用功能
xiaoming = Person("小明")
xiaohong = Person("小红")

xiaoming.work()

print(Person.__dict__)
print(xiaoming.__dict__)
print(xiaohong.__dict__)