# 进程间通讯
import multiprocessing
import os
import random
import time

# 生产者：不停的生成随机数放入队列  是一个子进程
# 消费者：从队列获取数据并处理  是main进程

#生产者逻辑
def producer(queue):
    while True:
        random_num = random.randint(1, 100)
        queue.put(random_num)
        print(f"{multiprocessing.current_process().name}放入了数据: {random_num}")
        time.sleep(random.random()) #随机延迟，防止程序翻入过多的数据，同时为了演示


if  __name__ == '__main__':
    queue = multiprocessing.Queue(maxsize=5)  #创建队列
    producer_process = multiprocessing.Process(target=producer, args=(queue,), name="生产者", daemon=True)
    producer_process.start()
    time.sleep(5)
    print(queue.get())
    print(queue.get())

    print("生产完成")