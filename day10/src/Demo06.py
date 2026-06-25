#生成器
gen=(x for x in range(10))


# print(list(gen))  #转成列表 只能迭代一次
# print(tuple(gen)) #转成元组


for num in gen:
    print(num, end=" ")