# 线程安全问题解决：条件变量
import random
import threading
from time import sleep


# 生产者与消费者共同分享一个队列数据
# 队列是自定义的一个队列，其中要求最多有2个数据
# 生产者一直生产，队列中有两个数据时，不再生产，等待消费者消费
# 消费者一直消费，队列中没有数据时，不再消费，等待生产者生产

class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = []
        self.cond = threading.Condition()  # 条件变量
    # p线程
    def put(self, item):
        with self.cond:  # 上锁
            while len(self.queue) >= self.max_size:
                print("队列已满，不再生产，生产等待")
                self.cond.wait()  # 本线程等待，等待该锁作用上的其他线程执行
            self.queue.append( item)
            print(f"生产者: 生产了一个数据 -> {item} | 队列全部数据：{self.queue}")
            self.cond.notify()

    # g线程
    def get(self):
        with self.cond:  # 上锁
            while len(self.queue) <= 0:
                print("队列已空，不再消费，消费等待")
                self.cond.wait() # 本线程等待，等待该锁作用上的其他线程执行
            item = self.queue.pop(0)
            print(f"消费者: 消费了一个数据 -> {item} | 队列全部数据：{self.queue}")
            self.cond.notify()
            return item

# 生产者与消费者
def producer(queue):
    for i in range(5):
        queue.put(i)
        sleep(random.random())
def consumer(queue):
    for i in range(5):
        queue.get()
        sleep(random.random())

if __name__ == '__main__':
    queue = Queue(max_size=2)
    t_p = threading.Thread(target=producer, args=(queue,))
    t_c = threading.Thread(target=consumer, args=(queue,))
    t_p.start()
    t_c.start()
    t_p.join()
    t_c.join()

    print("主线程结束")