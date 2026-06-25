from functools import wraps

def decorator(func):
    @wraps(func)  # 保留原始函数元信息
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@decorator
def test():
    """测试函数"""
    pass

print(test.__name__)  # 输出：test（未用wraps则输出wrapper）
print(test.__doc__)  # 输出：测试函数（未用wraps则输出None）