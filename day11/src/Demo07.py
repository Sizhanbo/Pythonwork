# 进程间通讯
import multiprocessing
import random
import time


# 生产者：不停的生成随机数放入队列  是一个子进程
# 消费者：不停的从队列获取数据并处理  是一个子进程
# main进程，用于开启两个进程，观察结果

# 生产者进程逻辑
def producer(queue, stop_event):
    count_num = 0
    while count_num < 10:
        # 生成随机数
        random_num = random.randint(1, 100)
        queue.put(random_num)
        print(f"生产者放入了数据: {random_num}")
        count_num += 1
        time.sleep(random.random())  # 随机延迟，防止程序翻入过多的数据，同时为了演示
    stop_event.set()


# 消费者进程逻辑
def consumer(queue, stop_event):
    while not stop_event.is_set() or not queue.empty():
        # 获取数据
        try:
            data = queue.get(timeout=1)
            print(f"消费者获取了数据: {data}")
        except Exception:
            continue
        time.sleep(random.random())


# 主进程，开启消费者与生产者进程
if __name__ == '__main__':
    queue = multiprocessing.Queue(maxsize=5)
    stop_event = multiprocessing.Event()
    p1 = multiprocessing.Process(target=producer, args=(queue, stop_event))
    p2 = multiprocessing.Process(target=consumer, args=(queue, stop_event))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("所有数据已处理完毕")
