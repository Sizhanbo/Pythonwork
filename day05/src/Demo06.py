class Person:

    home = "earth"

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self)
        print(Person.home)
        print(f"{self.name} 吃饭")

    def drink(self):
        print(f"{self.name} 喝水")

    # 内部调用其他方法
    def eat_and_drink(self):
        self.eat()  # 调用实例方法
        self.drink()  # 调用实例方法
        print(f"姓名：{self.name}")  # 访问实例属性

p = Person("张三")
p.eat()
p2 = Person("李四")
p2.eat()

p.eat_and_drink()
p2.eat_and_drink()