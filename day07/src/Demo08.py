# 自定义异常
class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)  # 自定义异常描述格式


# 创建异常对象   raise抛出异常   处理自己定义的异常
try :
    print("其他代码")
    raise MyError("自定义异常信息")
    print("其他代码")
except MyError as me:
    print(f"触发了自己定义的异常：{me.value}")
    print(f"触发了自己定义的异常：{me}")