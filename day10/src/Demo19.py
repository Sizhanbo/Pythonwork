def log_decorator(prefix="INFO"):
    """带参数的日志装饰器"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"[{prefix}] 调用函数：{func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 使用带参数的装饰器
@log_decorator(prefix="DEBUG")
def subtract(a, b):
    return a - b

print(subtract(5, 3))  # 输出：[DEBUG] 调用函数：subtract → 2