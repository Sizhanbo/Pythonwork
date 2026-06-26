# 进程间通讯
# multiprocessing.Value用于多进程之间共享值
import multiprocessing
import os


def add_num(value):
    for i in range(10):
        value.value += 1
        print(f"子进程{os.getpid()}做了+1动作:当前值:{value.value}")

    print(f"子进程{os.getpid()}:最终值:{value.value}")


if __name__ == '__main__':

    # 定义共享值
    value = multiprocessing.Value('i', 0)

    # 创建进程
    p1 = multiprocessing.Process(target=add_num, args=(value,))
    p2 = multiprocessing.Process(target=add_num, args=(value,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print(f"最终结果：{value.value}")