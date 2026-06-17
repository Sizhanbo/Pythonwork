# 全局变量与局部变量
sum = 0

for i in range(1, 101):
    sum += i

print(sum)

sum2 = 0
def add(num1,num2):
    sum2 = num1 + num2  # 函数内部定义了变量，与全局变量重名，此时，函数内部访问的sum2与全局sum2没有任何关系！！
    print(f"求{num1}与{num2}的和,和为{sum2}")
    return sum2


print(add(100, 200))
print(sum2)