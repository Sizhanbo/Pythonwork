# nonlocal关键字
# 内层函数修改外层嵌套函数的变量时，需用 `nonlocal` 声明。

def function_outer():
    print("外层函数开始执行...")
    var1 = 1  #属于嵌套作用域
    print(f"变量var1的值为：{var1}")

    def function_inner():
        print("内层函数开始执行...")
        # 修改嵌套作用域var1的值
        nonlocal var1
        var1 += 200

    # 函数内部定义的函数，只能在函数内部调用
    function_inner()
    print(f"变量var1的修改后的值为：{var1}")

# 调用外部函数
function_outer()
print("======================================")
# 与   全局变量与局部变量的关系类似，如果使用可变数据类型，内部函数可以直接访问修改外部函数的局部变量，即嵌套作用域变量
def function_outer2():
    print("外层函数开始执行...")
    list1 = [1,2,3]  #属于嵌套作用域
    print(f"变量var1的值为：{list1}")

    def function_inner2():
        print("内层函数开始执行...")
        # 修改嵌套作用域var1的值
        list1[1] = 200

    # 函数内部定义的函数，只能在函数内部调用
    function_inner2()
    print(f"变量var1的修改后的值为：{list1}")

function_outer2()