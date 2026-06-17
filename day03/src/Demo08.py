# 说明文档
def add(name,num1,num2):
    """
    某人计算两个数的和方法
    :param name: 计算和的人名
    :type name: str
    :param num1: 参与计算的第一个数
    :type num1: int
    :param num2: 参与计算的第二个数
    :type num2: int
    :return 两个数的和
    :rtype int
    """
    print(f"{name}在计算{num1}与{num2}的和")
    return num1 + num2

print(add("小王", 1, 2))
help(add)