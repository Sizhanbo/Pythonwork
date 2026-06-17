# 函数间互相调用
def funb(a,b):
    print(f"b：我的第一个变量{a}")
    print(f"b：我的第一个变量{b}")
    print("b：我执行了...")
    c = 100

def funa():
    print("a:我开始了")
    print("a:我调用了b")
    funb(10,20)
    # print(a) a变量只属于funb函数，在funa中没有定义，不能使用
    # print(c) a变量只属于funb函数，在funa中没有定义，不能使用
    print("a:我调用的b结束了")

    print("a:我开始定义一个函数c")
    def func():
        print("c:我开始了")
        print("c:我结束了")

    print("a:我开始调用函数c")
    func()

    print("a:我结束了")


funb(10,20)
funa()