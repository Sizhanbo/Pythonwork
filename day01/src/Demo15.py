# 赋值运算符
int1 = 10
print(int1)

# X=运算符
int2 = 100
int2 += 10
print(int2)

# 海象运算符  为某个变量计算赋值后，即时使用，该变量会被记录
a = 8
print((b := a+1) > 5)
print(b)