# try-except-else语句
# 出现异常，执行except，未出现异常执行else

try:
    num = int(input("请输入数字："))
    print(f"接收到数字是：{num}")
    print(f"10/{num}={10 / num}")
except (ZeroDivisionError, ValueError) as e:
    print(f"除数出现了问题！")
    print(e)
else:
    print("除法结束了！计算出了正确的结果!")


print("后续代码执行...")