#需要额外一层函数接收参数，实现装饰器的灵活配置
from math import sqrt

# 求根号n次
def times(n):
    # 将参数转换为非负数
    def get_absolute(f):
        def inner(x):
            x = abs(x)
            for i in range(n):
                x = f(x)
            return x
        return inner
    return get_absolute

@times(2)
def func(x):
    """开根号"""
    return sqrt(x)

print(func(-16))  # 2.0