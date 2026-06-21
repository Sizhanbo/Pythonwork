# 异常传递:即内部解决不了，会传到上一级
try:
    try:
        try:
            print(1 / 0)  # 触发ZeroDivisionError
        except NameError as e:
            print("第三层", e)  # 不匹配，异常传递
    except TypeError as e:
        print("第二层", e)  # 不匹配，异常传递
except Exception as e:
    print("第一层", type(e), e)  # 捕获异常，输出：第一层 <class 'ZeroDivisionError'> division by zero


def a():

    print("其他代码")
    raise NameError("命名错误")
    print("其他代码")

def b():
    try:
        a()
    except Exception as e:
        print(e)

def c():
    b()

c()