# set集合
# 集合是**可变、无序、无重复**的元素集合
# 使用 `{}` 或 `set()` 定义，适用于去重、快速数据判断等集合运算场景
# 因为没有索引，所以不能使用索引或切片访问。

#创建
set1 = {"b",1,1,2,3,4,5,"a"}
print(set1)

set2 = set()
print(set2)

set3 = set(['x','y','z'])
print(set3)

set4 = {x for x in range(10)}
print(set4)

set5 = {x for x in range(10) if x % 2 == 0}
print(set5)

# 增删改
set6 = {"b",1,1,2,3,4,5,"a"}
set6.add("x")
print(set6)

set6.update([100,200])
print(set6)

# 删除
set7 = {"b",1,1,2,3,4,5,"a"}
set7.remove(2)
print(set7)
# set7.remove(2)  # remove只能删除存在的元素
# print(set7)
set7.discard(2)  # discard可以删除不存在的元素
print(set7)

print(set7.pop()) # 表现上是随机删除了一个元素
set7.clear()
print(set7)

# 遍历
set8 = {"b",1,1,2,3,4,5,"a"}
for e in set8:
    print(f"本次遍历的元素是：{e}")

# 集合运算
a = {1,2,3,4}
b = {3,4,5,6}
print(a | b)  # 并集：{1,2,3,4,5,6}
print(a & b)  # 交集：{3,4}
print(a - b)  # 差集：{1,2}（a中有b中无）
print(b - a)  # 差集：{5,6}（a中有b中无）
print(a ^ b)  # 对称差：{1,2,5,6}（互不包含的元素）