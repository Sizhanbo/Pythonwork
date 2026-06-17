# 形参定义

# 必须参数（位置参数）
def func(a,b,c):
    print(f"a:{a},b:{b},c:{c}")


func(1,2,3)
# 注意，不建议在同一个文件中定义同名的函数，因为同名函数是覆盖关系，即前边的函数会被后边的函数覆盖
def func(a, b):
    print(f"a:{a},b:{b}")

func(1,2)

# 关键字参数
def printInfo(name,age):
    print(f"name:{name},age:{age}")

printInfo("张三",18)
printInfo(name="李四",age=10)
printInfo(age=18,name="王五")

# 默认参数
def printInfo2(name,age=18):
    print(f"name:{name},age:{age}")

printInfo2("赵六")
printInfo2("赵六",20)
printInfo2(name="钱七")
printInfo2(age=50,name="钱七")