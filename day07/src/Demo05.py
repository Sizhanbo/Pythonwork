# try-except-els-finally语句
# 尝试执行try中的代码
# -如果try中的代码没有异常，则执行else中的代码
# -如果try中的代码有异常，则执行except中的代码
# -不管try中的代码是否异常，都会执行finally中的代码

try:  # 要执行的语句，可能包含异常
    num = int(input("请输入数字："))
    print(f"接收到数字是：{num}")
    print(f"10/{num}={10 / num}")
except (ZeroDivisionError, ValueError) as e:  # 出现异常后要执行的语句
    print(f"除数出现了问题！")
    print(e)
except:
    print("出现了问题！")
else:  # 没有出现异常后要执行的语句
    print("除法结束了！计算出了正确的结果!")
finally:  # 无论是否出现异常，都会执行的语句
    print("必须要执行的代码...")

print("后续代码正常执行...")