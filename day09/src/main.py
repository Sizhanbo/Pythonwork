# 导入其他模块并使用
#   导入                          使用
# import 模块                 模块名.成员(属性/函数)
# from 模块 import 成员            成员
# from 模块 import *             任意成员
# import 包.模块               包名.模块名.成员(属性/函数)
# from 包  import 模块           模块名.成员
# from 包.模块 import 成员          成员
# from 包  import *             任意模块名.成员
# import os
# import pygame

# # 导入包内模块
# import graphic.circle
# print(graphic.circle.area())

# # 导入包内的模块
# from graphic import rectangle
# print(rectangle.area())
#
# # 导入包内模块的成员
# from graphic.circle import area
# print(area())
#
# print(os)  # 模块点进去是该模块的源代码
# print(pygame)  # 包点进去是包的init文件


# 配合__init__.py包初始化文件使用，指定包中可以使用的模块，没有在all属性中指定的模块，无法使用！
from graphic import *
print(circle.area())
# print(rectangle.area())