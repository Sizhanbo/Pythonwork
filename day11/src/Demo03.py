# 进程池
"""
    multiprocessing.Pool([processes[,initializer[,initargs[,maxtasksperchild[,context]]]]])

    processes：规定了进程池中的进程数
    pool.apply(func)方法，是用于向进程池当中提交任务，分配进程操作。这个方法是同步执行的。即第二个任务要等第一个任务执行完毕后才能执行
    这种方式，无法体现同时运行的情况，自然没有运行效率的优越性
"""
import multiprocessing
import os
import random
import time


# 打印10个数字,每次间隔0.5秒
def func():
    for i in  range(10):
        print(f"{os.getpid()}进程打印: {i}")
        time.sleep(random.random())

if __name__ == "__main__":
    process_num = 2
    # 创建进程池，可以容纳5个进程
    pool = multiprocessing.Pool(process_num)

    for i in range(process_num):
        # 添加进程
        # pool.apply(func)  # 同步执行
        pool.apply_async(func)  # 异步执行

    pool.close()  # 关闭主进程(close指不再接受新任务)
    pool.join()  # 主进程等待进程池中的进程全部执行结束后，再结束

    print("主进程结束...")