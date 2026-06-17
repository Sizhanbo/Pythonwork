# 函数内部属于局部作用域，不能直接访问，修改全局变量
# global关键字  声明该变量为全局变量
var1 = 100
def function_a():
    global var1
    var1 = 200 + var1

print(f"修改前：{var1}")
function_a()
print(f"修改后：{var1}")

# 当全局变量为可变类型时，函数内不使用 global 声明，也可以对其内容进行修改，本质为传址
list1 = [1,2,3]
def function_b():
    list1[1] = 100

print(f"修改前：{list1}")
function_b()
print(f"修改后：{list1}")