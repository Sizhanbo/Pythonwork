# 函数返回值
import random

# 函数遇到return后，会立即执行完毕
# 未写return，或者return后无返回值，默认返回None
def myfun():
    print("hello world")
    return
    print("hello world2")
print(myfun())

def myfun2():
    print("hello world")
print(myfun2())

# 函数返回值，可以返回1个值，也可以返回多个值，返回多个值时，会打包成元组
def getRandom():
    return random.randrange(1,10)
print(getRandom())

def getNames():
    return "小王", "小李", "小张",1,[1,2,3]
print(getNames())