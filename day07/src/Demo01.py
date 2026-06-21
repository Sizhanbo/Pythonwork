# 异常：程序运行过程中出现的错误
# python的默认异常处理机制是 中断异常处理机制:中断程序，并且打印出异常的追踪信息，所属文件，所属代码，行数，异常信息
print("hello exception")
print(10/0) #出现除0异常
print("hello exception2") #不会执行


# 异常是一种可能性！
# 因为用户输入数据的不同，可能产生异常，也可能不会产生异常
num = int(input("请输入数字："))
print(10/num)

# 有些异常是可以通过逻辑缜密操作避免的，这样的情况，应该使用逻辑避免！
num = int(input("请输入数字："))
if num == 0:
    print("输入的数字不能为0")
    exit()
print(10/num)