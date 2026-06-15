# 整数数据
"""
- 支持任意大小整数，含负整数
- 大数字可加下划线分组（如 `1_000_000`），Python 忽略下划线  只是为了方便观察，打印时会忽略下划线
- 类型判断：`type()`（严格判断类型）、`isinstance()`（考虑继承，如 `bool` 是 `int` 子类）
"""
num = 100000
num2 = -100000
print(num)
print(num2)

num3=100_00  #Python 忽略下划线  只是为了方便观察，打印时会忽略下划线
print(num3)




# 判断类型
num4 = 100
thisType = type(num4)
print(thisType)

myStr = "hello"
print(type(myStr))

# 判断是否为某种特定的类型
print(isinstance(num4, int))
print(isinstance(myStr, int))