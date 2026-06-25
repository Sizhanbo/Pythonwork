# 全局作用域
x = "global"

def outer():
    x = "enclosing"          # 外层嵌套作用域（Enclosing）

    def inner():
        x = "local"         # 局部作用域（Local）
        print("inner:", x)  # 找到局部 x -> local

    def shadow_builtin():
        # 局部遮蔽内置：在本作用域内，len 不再是内置函数
        len = "I'm not len!"
        print("shadow_builtin len:", len)  # 找到局部 len -> I'm not len!
        # 如需使用内置 len，可用 globals()/builtins.len
        print("builtins.len:", __builtins__.len([1, 2, 3]))

    def use_builtin():
        # 未遮蔽时直接使用内置
        print("use_builtin len:", len([1, 2, 3,4]))

    inner()
    shadow_builtin()
    use_builtin()
    print("outer:", x)         # 找到外层 x -> enclosing

outer()