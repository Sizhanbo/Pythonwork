#缓存装饰器（缓存函数返回结果）
def cache(func):
    cache_dict = {}
    def wrapper(*args):
        if args in cache_dict:
            return cache_dict[args]
        else:
            result = func(*args)
            cache_dict[args] = result
            return result
    return wrapper

@ cache
def fibo(n):
    if n <= 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)
print(fibo(10))
print(fibo(10))
