#装饰器是 Python 中动态增强函数 / 类功能的高级语法，基于闭包实现，核心优势是不修改原始代码即可扩展功能，符合 "开放 - 封闭" 原则。
# 装饰器语法：
# 装饰器函数（接收函数为参数，返回新函数）
def decorator(func):
    def wrapper(*args, **kwargs):
        # 增强功能（前处理）
        result = func(*args, **kwargs)  # 调用原始函数
        # 增强功能（后处理）
        return result
    return wrapper

# 使用装饰器（@语法糖）
@decorator
def target_func():
    pass