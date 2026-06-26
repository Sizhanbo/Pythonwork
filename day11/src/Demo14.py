#  线程安全问题
"""
线程安全出现前提：
    1.多线程参与
    2.多线程共享数据
    3.多线程修改数据

出现线程安全最重要的原因：原子性问题
原子性：不可拆分的一个整体性质。每个进程在执行任务时，某些步骤是不能分割执行的，应该将所有该动作执行的代码看作一个原子性操作，操作过程中，不能让CPU执行操作同一个数据的代码
所以：多线程操作共享数据时，应该保持原子性操作不被插入打断，否则会出现线程安全问题
"""
import threading
from time import sleep

# 定义线程任务，累加1，执行N次
def add_num(value) :
    for i in range(10) :
        # value['value'] += 1  # 原始叠加1的操作，一句话完成

        #后续使用多个步骤完成叠加1的操作，每步之间做短暂停顿
        current_value = value['value']
        sleep(0.001)
        new_value = current_value + 1
        sleep(0.001)
        value['value'] = new_value
        sleep(0.001)
        print(f"{threading.current_thread().name}线程执行+1，此次结果为：{value['value']}")


if __name__ == '__main__':

    # 多线程共享数据
    shared_num = {"value": 0}

    t1 = threading.Thread(target=add_num, args=(shared_num,),name="小美")
    t2 = threading.Thread(target=add_num, args=(shared_num,),name="小帅")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    expected = 20  # 预期值
    actual = shared_num["value"]  # 实际值

    print(f"预期结果：{expected}，实际结果：{actual}")
    if expected == actual:
        print("没有出现数据安全问题")
    else:
        print("出现了数据安全问题")