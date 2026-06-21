# 针对不同异常类型执行差异化处理，并可获取异常详情
"""
- 异常信息格式：冒号前为异常类型，冒号后为描述信息
- 一个 except 可处理多种异常，需将异常类型放入元组
- 最后一个无类型 except 作为通配符，捕获所有未匹配的异常
"""
try:
    num = int(input("请输入数字："))
    print(f"接收到数字是：{num}")
    print(f"10/{num}={10 / num}")
    f = open("./test.txt","r",encoding="utf-8")
except (ZeroDivisionError, ValueError) as e:
    print(f"除数出现了问题！")
    print(e)
except:
    print("出现了问题！")

print("后续代码执行...")