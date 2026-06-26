# 自定义进程类
"""
通过继承 `Process` 类，可更灵活地封装进程逻辑
run方法为该进程要执行的逻辑
"""
import multiprocessing
import os
import random
from time import sleep

class Worker(multiprocessing.Process):

    # 初始化方法
    def __init__(self, task_id):
        super().__init__()
        self.task_id = task_id


    # 必须定义run方法，即该进程要执行社么
    def run(self):
        print(f"进程{self.task_id}:{os.getpid}开始执行...其父({os.getppid()})进程")
        time_sleep = random.random()
        print(f"进程{self.task_id}休眠{time_sleep}秒")
        sleep(time_sleep)
        print(f"进程{self.task_id}执行完毕...")

if __name__ == '__main__':

    print("主进程开启")
    w1 = Worker("小美")
    w2 = Worker("小帅")
    w3 = Worker("小叮当")

    #开启进程
    w1.start()
    w2.start()
    w3.start()

    #主线程等待开启的子线程
    w1.join()
    w2.join()
    w3.join()

    print("主进程运行结束")