# 传值与传址
# 传值案例
def changeInt(a):

    print(f"a的id：{id(a)}")
    print(f"函数内部修改a的值之前，a的值是：{a}")
    a = 100
    print(f"a的id：{id(a)}")
    print(f"函数内部修改a的值之后，a的值是：{a}")

b = 200
print(f"b的id：{id(b)}")
changeInt(b)
print(f"函数外部作为参数传入的b的值是：{b}")
print(f"===================================")

# 传址案例
def changList(mylist):
    print(f"函数内部修改列表mlist的值之前，mlist的值是：{mylist}")
    print(f"mylist的id：{id(mylist)}")
    mylist[1] = 100
    print(f"mylist的id：{id(mylist)}")
    print(f"函数内部修改列表mlist的值之后，mlist的值是：{mylist}")

mlist = [1, 2, 3]
print(f"mlist的id：{id(mlist)}")
changList(mlist)
print(f"函数外部作为参数传入的mlist的值是：{mlist}")
