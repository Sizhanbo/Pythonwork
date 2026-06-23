# 圆形模块，用于处理圆形面积与周长
import math

radius = 10
PI = math.pi

def area():
    """
    计算圆形面积
    :return: 返回圆形面积
    """
    return PI * radius * radius

def perimeter():
    """
    计算圆形周长
    :return: 圆形周长
    """
    return 2 * PI * radius