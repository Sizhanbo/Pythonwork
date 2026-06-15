# 输入与输出
# 输入
# input("提示信息")`：接收用户键盘输入，返回字符串。

# input_str=input("请输入：")
# print(input_str)


# 输出
print("hello world")
str1 = "haha"
print(str1)
print("hehe", str1, end="------")  # end修改了默认的结束符，默认结束符为\n(换行)
print("heihei", str1)
print("gege")


# 格式化输出
# %d ：整数  %f ：浮点数

a=100
a1=10.21
print("整数：%d" % a)
print("整数：%d" % a1) #去掉小数后缀
print("浮点数：%f" % a1)
print( "整数：%d,浮点数：%.3f" % (a,a1))