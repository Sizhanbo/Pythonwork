# 自定义异常需求
"""
某网站为ai学习网站
对学习人群年龄有要求，
如果年满十八岁，打印欢迎学习，
否则报出异常，并显示异常信息：不满十八岁，无法理解技术概要，并处理异常
"""

# 自定义异常,U18异常
class U18Error(Exception):
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return repr(self.value)

try:
    age = int(input("请输入年龄："))
    if age >= 18:
        print(f"欢迎来到ai学习网站，{age}岁的你，欢迎学习")
    else :
        raise U18Error("不满十八岁，无法理解技术概要")
except U18Error as ue:
    print("不满足进入ai学习网站的要求")
    print(ue)
except ValueError as ue:
    print("请输入数字！因为年龄是数字")