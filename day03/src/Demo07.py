# 参数解包
def add(num1,num2,num3):
    print(f"求{num1}与{num2}与{num3}的和")
    return num1 + num2 + num3


print(add(1, 2, 3))

tuple1 = (1, 2, 3)
print(add(*tuple1))

list1 = [1,2,3]
print(add(*list1))

dict1 = {"num1":1,"num2":2,"num3":3}
print(add(**dict1))
print("==============")
# 强制位置 / 关键字参数
"""
- `/` 前的参数必须用位置传递；
- `*` 后的参数必须用关键字传递。
"""
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)

f(1, 2, 3, d=4, e=5, f=6)  # 正确：a、b 位置传递；e、f 关键字传递
f(1, 2, 3, 4, e=5, f=6)  # 正确：a、b 位置传递；e、f 关键字传递