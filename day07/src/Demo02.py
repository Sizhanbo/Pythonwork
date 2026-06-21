# 异常的捕获处理
"""
try:
    # 可能发生异常的代码
except:
    # 异常处理逻辑

print("后续代码")

- 无异常：忽略 except 代码，继续执行后续内容
- 有异常：跳过 try 中剩余代码，执行 except 代码
"""

try:
    num = int(input("请输入数字："))
    print(f"接收到数字是：{num}")
    print(f"10/{num}={10/num}")
    print("除法计算结束啦！")
except:
    print("除法错误！")

print(f"后续代码执行了！")