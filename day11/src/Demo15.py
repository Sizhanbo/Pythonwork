# 线程安全问题解决：使用锁
"""
线程：threading.Lock()
多个线程操作同一个数据，需要使用同一个锁对象
"""

import threading
from time import sleep

# 定义线程任务，累加1，执行N次
def add_num(value,lock) :
    for i in range(1000) :
        lock.acquire() # 上锁
        try:
            #后续使用多个步骤完成叠加1的操作，每步之间做短暂停顿
            current_value = value['value']
            sleep(0.001)
            new_value = current_value + 1
            sleep(0.001)
            value['value'] = new_value
            sleep(0.001)
            print(f"{threading.current_thread().name}线程执行+1，此次结果为：{value['value']}")
        finally:
            lock.release() # 解锁
        sleep(0.0001)

if __name__ == '__main__':

    # 多线程共享数据
    shared_num = {"value": 0}
    # 创建互斥锁，被操作共享数据的多个线程使用
    lock = threading.Lock()

    t1 = threading.Thread(target=add_num, args=(shared_num,lock),name="小美")
    t2 = threading.Thread(target=add_num, args=(shared_num,lock),name="小帅")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    expected = 2000  # 预期值
    actual = shared_num["value"]  # 实际值

    print(f"预期结果：{expected}，实际结果：{actual}")
    if expected == actual:
        print("没有出现数据安全问题")
    else:
        print("出现了数据安全问题")