# 主动抛出异常
# raise 异常类型("异常描述")

def add(x,y):

    if isinstance(x,int) and isinstance(y,int):
        return x+y
    else:
        # 主动抛出一个异常
        raise TypeError("参与加法计算的数据必须为数字，不能是其他类型！")

try:
    print(add(10,"中"))
except TypeError as te:
    print(te)

print("后续代码执行...")