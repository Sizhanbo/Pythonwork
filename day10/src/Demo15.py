#计时装饰器（统计函数执行时间）
import time
def timer(func):
    """计时装饰器"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 耗时 {end - start} 秒")
        return result
    return wrapper

@ timer
def test(n):
    return sum(range(n))


print(test(1000000))


