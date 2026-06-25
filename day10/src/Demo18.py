class RetryDecorator:
    def __init__(self, max_retry=2):
        self.max_retry = max_retry

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for i in range(self.max_retry):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"第{i + 1}次执行失败：{e}")
            raise Exception(f"{self.max_retry}次执行均失败")

        return wrapper


# 使用类装饰器（重试5次）
@RetryDecorator(max_retry=5)
def risky_operation():
    import random
    x = random.random()
    if x < 0.7:
        raise ValueError("随机失败")
    return f"执行成功:{x}"


#print(risky_operation())  # 失败时重试，成功则返回结果
# 失败时抛出异常
try:
    print(risky_operation())
except Exception as e:
    print(e)
