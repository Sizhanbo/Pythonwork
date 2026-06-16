# 列表增删改

list1 = [10, 20, 30, 40, 50]
"""
添加：
追加：列表.append(元素)
插入：列表.insert(索引,元素)  插入后，后续所有元素往后推一个索引
合并：列表.extend(其他列表) 该方法不会产生新的列表！而是会直接修改.前边的列表！
"""
list1.append(100)
print(list1)
list1.insert(2, 500)
print(list1)
print("===================================")
list2 = [1000, 2000]
list3 = list2.extend(list1)
print(list1)
print(list2)
print(list3)
print(id(list1))
print(id(list2))
print(id(list3))
print("以上为添加===================================")
"""
删除：
del 列表[索引]  删除指定位置索引
"""
print(list1)
del list1[2]
print(f"del list1[2]------")
print(list1)

list1.remove(30)  # 删除指定元素
print(f"list1:{list1}")

print("pop操作：")
ele = list1.pop()  # 弹栈操作，弹栈：从列表后边弹出一个元素
print(f"ele：{ele}")
print(f"list1:{list1}")
print(f"ele：{list1.pop()}")
print(f"list1:{list1}")
print(f"ele：{list1.pop(1)}")  # 指定索引弹栈
print(f"list1:{list1}")

list1.clear()  # 清空列表
print(f"list1: {list1}")

"""
修改：
列表[索引] = 新的值
列表[开始索引:结束索引] = [修改成的新元素] 
"""

list4 = [10, 20, 30, 40, 50]
list4[2] = 1000
print(f"list4: {list4}")

list4[1:4] = [100, 200]
print(f"list4: {list4}")