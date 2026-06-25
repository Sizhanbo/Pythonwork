# 闭包计数器：利用闭包（closure）实现的状态保持
# 闭包 = 内层函数 + 对外层函数变量的引用（即使外层函数已执行完毕）
def counter(start=0):
    """外层工厂函数，创建并返回一个闭包计数器"""
    count = start  # 外层函数的局部变量，被内层函数引用（形成闭包）

    def inner():
        """内层函数（闭包），每次调用返回递增后的 count 值"""
        nonlocal count  # 声明 count 来自外层作用域，而非新建局部变量
        count += 1      # 对 count 自增
        return count    # 返回自增后的值

    return inner  # 返回 inner 函数对象（注意：不是调用 inner()）


# 创建计数器实例，起始值为默认值 0
c = counter()

# 每次调用 c()，实际调用的是 inner()，count 值持久保留
print(c())  # 第1次: count=0→1, 输出 1
print(c())  # 第2次: count=1→2, 输出 2
print(c())  # 第3次: count=2→3, 输出 3

