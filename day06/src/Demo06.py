# 父类（基类）
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        # 父类的通用方法
        # print(f"{self.name}发出声音")
        pass

    def move(self):
        # 父类的移动方法
        # print(f"{self.name}开始移动")
        pass


# 子类1 - 狗类（重写父类方法）
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed  #子类特有对象属性

    # 重写父类的make_sound方法
    def make_sound(self):
        print(f"{self.name}汪汪叫：汪汪汪！")

    # 重写父类的move方法
    def move(self):
        print(f"{self.name}摇着尾巴跑来跑去")


# 子类2 - 猫类（重写父类方法）
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color   #子类特有对象属性

    # 重写父类的make_sound方法
    def make_sound(self):
        print(f"{self.name}喵喵叫：喵~喵~")

    # 重写父类的move方法
    def move(self):
        print(f"{self.name}优雅地踱步")

# 测试方法重写
print("=== 方法重写测试 ===")

# 创建不同动物对象
dog = Dog("旺财", "金毛")
cat = Cat("咪咪", "橘色")
generic_animal = Animal("普通动物")

# 调用重写后的方法
animals = [dog, cat, generic_animal]

for animal in animals:
    print(f"\n--- {animal.name} ---")
    animal.make_sound()  # 调用各自重写后的方法
    animal.move()  # 调用各自重写后的方法