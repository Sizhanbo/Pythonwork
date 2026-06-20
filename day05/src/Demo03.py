# # 面向对象实现"游戏装备"
# class Equipment:
#     def __init__(self,name, level):
#         """
#         初始化装备
#         :param name: 名字
#         :param level: 等级
#         """
#         self.name = name
#         self.level = level
#
# # 武器类
# class Weapon(Equipment):
#     def equip(self):
#         """
#         装备武器
#         """
#         print(f"拿起{self.name} (等级{self.level}) → 攻击力+ {self.level*10}")
#
# # 护甲类
# class Armor(Equipment):
#
#     def equip(self):
#         """
#         装备护甲
#         """
#         print(f"穿上{self.name} (等级{self.level}) → 防御力+ {self.level * 8}")
#
# # 全能装备类
# class Artifact(Equipment):
#
#     def equip(self):
#         """
#         装备全嗯那个装备
#         """
#         print(f"激活{self.name} (等级{self.level}) → 全属性+ {self.level * 5}")
#
# sword = Weapon("屠龙剑", 5)
# shield = Armor("圣光盾", 3)
# ring = Artifact("圣光戒指", 7)
#
# sword.equip()
# shield.equip()
# ring.equip()

#游戏装备
class Equipment:
    def __init__(self, name, level):
        """
        初始化装备
        :param name: 名字
        :param level: 等级
        """
        self.name = name
        self.level = level
#武器类
class Weapon(Equipment):
    def equip(self):
        """
        装备武器
        """
        print(f"拿起{self.name} (等级{self.level}) → 攻击力+ {self.level*10}")
#护甲类
class Armor(Equipment):
    def equip(self):
        """
        装备护甲
        """
        print(f"穿上{self.name} (等级{self.level}) → 防御力+ {self.level * 8}")
#全能装备类
class Artifact(Equipment):
    def equip(self):
        """
        装备全能装备
        """
        print(f"激活{self.name} (等级{self.level}) → 全属性+ {self.level * 5}")

Weapon("屠龙剑", 5).equip()
Armor("圣光盾", 3).equip()
Artifact("圣光戒指", 7).equip()
