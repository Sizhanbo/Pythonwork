# 不使用递归解决阶乘问题
# n * （n-1） * (n-2) * .. * 1
def get_factorial(num):

    #定义变量，记录最终结果
    result = 1
    for n in range(1, num+1):
        result *= n

    #返回阶乘结果
    return result

print(get_factorial(5))


def get_factorial2(n):
    return n * get_factorial(n - 1) if n > 1 else 1