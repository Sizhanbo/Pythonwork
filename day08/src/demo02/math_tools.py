"""
数学工具模块
包含常用的算术运算、数值处理功能
"""
import sys

# 常量
PI = 3.1415926
E = 2.71828

# 普通函数
def add(a: int | float, b: int | float):
    """求两个数的和"""
    return a + b

def multiply(a: int | float, b: int | float):
    """求两个数的积"""
    # return a * b
    return _format_number(a * b)

#数值:1 1 2 3 5 8  ...
#项数:1 2 3 4 5 6  ...
def fibonacci(n: int) :
    """
    斐波那契数列
    :param n: 项数
    :return: 项值
    """
    if n < 0:
        raise ValueError("项数不能为负数")
    elif n == 1 or n ==2:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)


def _format_number(n: int | float):
    """
    # 辅助函数，用于将计算结果格式化，小数保留2位
    :param n: 要格式化的整数或者小数
    :return: 格式化后的字符串
    """
    return f"{n:.2f}" if isinstance(n, float) else str(n)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __hello(self):
        print("hello__")

    def _hello(self):
        print("hello_")

    def hello(self):
        print("hello")

# 代码自测
if __name__ == "__main__":
    print(add(1, 2))
    print(multiply(1, 2))
    print(fibonacci(10))
    print(f"2 + {PI} = {add(2, PI)}")
    print(f"2 + {PI} = {_format_number(add(2, PI))}")
    # print(__dict__) 自己模块无法直接用__dict__方式访问自身
    print(globals())
    print(sys.modules[__name__].__dict__)
    import __main__

    print(__main__.__dict__)