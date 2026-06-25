# 闭包会保留外层变量的引用，可能导致内存占用（避免保留大对象）

# 外层变量若为可变类型（列表、字典），无需`nonlocal`即可修改
def outer():
    count = []
    def inner(item):
        count.append(item)  # 可变类型无需nonlocal
        return count
    return inner

add_item = outer()
print(add_item(1))  # 输出：[1]
print(add_item(2))  # 输出：[1, 2]
