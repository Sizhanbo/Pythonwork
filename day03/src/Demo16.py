# python内置配合lambda的函数
# 匿名函数常与 `sorted()`、`map()`、`filter()`、`reduce()` 等内置函数搭配
from functools import reduce

# 这里希望以年龄进行排序动作
student_list = [
    {"name": "小王", "age": 18},
    {"name": "小张", "age": 19},
    {"name": "小李", "age": 17},
    {"name": "小王", "age": 16},
    {"name": "小王", "age": 20},
]

sorted_student_list = sorted(student_list, key= lambda item: item["age"])
print(sorted_student_list)

# 求列表中每个元素的平方
list1 = [1,2,3,4,5]
print(list(map(lambda x: x ** 2, list1)))

# 过滤列表中偶数,偶数满足条件，留下来，奇数不要
list1 = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x: x % 2 == 0, list1)))

list1 = [1,2,3,4,5]
# 类加列表中的数据
print(reduce(lambda x, y: x + y, list1))
# 求5的阶乘>> 1-5的累乘
print(reduce(lambda x, y: x * y, list1))