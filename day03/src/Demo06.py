# 可变参数
# 求任意个数的和
def add(*nums):
    print(nums)
    print(type(nums))
    print(f"求{nums}的和")
    return sum(nums)

result = add(1,2,3)
print( result)
result = add(1,2,3,4,5,6)
print( result)

def showInfo(**info):
    print(info)
    print(type(info))

showInfo(name="张三", age=18)

# 特殊情况：可变参与与正常参数混用
def add2(name, *nums):
    print(nums)
    print(type(nums))
    print(f"{name}在求{nums}的和")
    return sum(nums)


print(add2("张三", 1, 2, 3))

# 在可变参数后，加一个普通参数时，需要使用关键字的方式赋值
def add3(name, *nums, desp):
    print(nums)
    print(type(nums))
    print(f"{name}在求{nums}的和,{desp}")
    return sum(nums)

print(add3("张三", 1, 2, 3, desp="这道题好难呀！"))


def showInfo2(desp,**info):
    print(info)
    print(f"描述信息：{desp}")
    print(type(info))

showInfo2("这是个字典", name="张三", age=18)
showInfo2(desp="这是个字典2", name="李四", age=18)