# 元组，不能改变的序列
# 元组的不可变指的是元组所指向的内存中的内容不可变，但可以重新赋值。
tuple1 = (10, 20, 30, "a", 40)
tuple2 = (10, )
print(tuple1)
print(tuple2)
tuple3 = ()
print(tuple3)

tuple_xpr = (x for x in range(5))
print(tuple_xpr)
tuple4 = tuple(tuple_xpr)
print(tuple4)

tuple1 = (100, 200, 300, 400)
print(tuple1[2])       # 300（索引访问）
print(tuple1[1:3])     # (200, 300)（切片）
print(tuple1 + (500,)) # (100,200,300,400,500)（拼接）
print(200 in tuple1)   # True（成员判断）
print(tuple1 * 2)      # (100, 200, 300, 400,100, 200, 300, 400)
print(len(tuple1))     # 4

for e in tuple1:
    print(f"本次遍历的元素是：{e}")

tuple1 = (100, 200, 300)
print(id(tuple1), tuple1)
tuple1 = tuple1 + (1, 2, 3)
print(id(tuple1), tuple1)

#以下操作是否可执行？：
tuple2 = (1, [2, 3])
print(tuple2)
tuple2[1].append(4)  # 元组中两个元素都没有改变！改变的是元素的第二个元素列表，列表中添加了一个元素，但是元组中的列表没变，还是那个列表！
print(tuple2)
# tuple2[0] = 5