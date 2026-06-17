# 匿名函数  lambda函数
# 有名字的函数
def function(a,b,op):
    return op(a,b)

def add(x,y):
    return x + y

def mul(x,y):
    return x * y

# 逻辑也是一段地址引用
print(id(add))

print(function(10, 20, add))
print(function(10, 20, mul))

print(function(10, 20, lambda a, b: a + b))
print(function(10, 20, lambda a, b: a * b))