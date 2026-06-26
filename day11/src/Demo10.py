# 验证多线程共享数据
# 需求：一个列表，在main进程中操作，同时将该列表交给两个不同的线程操作，修改数据。观察结果。
import os
import threading


# 向列表中添加10个元素
def func(list1):
    for i in range(10):
        list1.append(i)
        print(f"线程添加了元素{i}")

    print(f"线程中的列表id为：{id(list1)}")


if __name__ == "__main__":
    # 准备数据
    list2 = []

    # 将数据交给不同的线程处理
    p1 = threading.Thread(target=func, args=(list2, ))
    p2 = threading.Thread(target=func, args=(list2, ))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    # 观察数据的改变情况
    print(f"main中的列表id为：{id(list2)}")
    print(f"main中的数据为：{list2}")
