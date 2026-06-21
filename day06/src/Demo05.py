# 多重继承
# Mage类  Warrior类   父类
# MagicWarrior类 子类
class Mage:
    def __init__(self, name, magic_power):
        self.name = name
        self.magic_power = magic_power

    def magic_attack(self):
        print(self.name + "使用了技能攻击")

    def show(self):
        print(self.name + "的魔法攻击力是：" + str(self.magic_power))

    def eat(self):
        print(f"{self.name}吃了")


class Warrior:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

    def attack(self):
        print(self.name + "使用了攻击")

    def show(self):
        print(self.name + "的攻击力是：" + str(self.strength))


class MagicWarrior(Mage, Warrior):
    def __init__(self, name, magic_power, strength):
        Mage.__init__(self, name, magic_power)
        Warrior.__init__(self, name, strength)

    def attack(self):
        print(self.name + "使用了技能攻击")
        self.magic_attack()
        Warrior.attack(self)


mw = MagicWarrior("小王", 100, 100)
mw.attack()

