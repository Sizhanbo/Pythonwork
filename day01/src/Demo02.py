a=1
var = 10
result = a + var
print("打印结果:",result)


# 定义多个变量 字符串可以与字符串相加，会合并字符串。数字不能与字符串相加，不能直接合并
name,name2,name3 = "小王","小张","小李"
#单独打印
print(name)
print(name2)
print(name3)
print(name3)


q1 = q2 = q3 = 100
print(q1)
print(q2)
print(q3)
qa = q1 + q2 + q3
print(qa)
print(q1 + q2 + q3)

# python中定义变量，不建议重名，如果同一个变量多次赋值，不会报错，而是数值覆盖
# 将定义变量与赋值变量两个动作合在一起执行
a = 200
print(a)
