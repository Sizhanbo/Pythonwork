from collections.abc import Iterable, Iterator

# 验证可迭代对象
lst = [1, 2, 3]
print("列表是否可迭代:", isinstance(lst, Iterable))  # 输出：True
print("列表是否迭代器:", isinstance(lst, Iterator))  # 输出：False

# 生成迭代器
lst_iter = iter(lst)
print("迭代器是否可迭代:", isinstance(lst_iter, Iterable))  # 输出：True
print("迭代器是否迭代器:", isinstance(lst_iter, Iterator))  # 输出：True

# 遍历迭代器
# print(next(lst_iter))  # 输出：1
# print(next(lst_iter))  # 输出：2
# print(next(lst_iter))  # 输出：3
# print(next(lst_iter))  # 抛出 StopIteration 异常
print("===================================================")
# 创建迭代器对象后使用for循环遍历
it = iter(lst)
for i in it:
  print(i)

