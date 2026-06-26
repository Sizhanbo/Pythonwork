# 多线程创建
# 交替打印示例
import threading
import time

# 线程执行目标函数，即任务
def print_num(start,end):
    for i in range(start,end+1):
        print(f"{threading.current_thread().name}号线程打印：{i}")
        time.sleep(0.1)

if __name__ == '__main__':
    # 创建线程对象
    t1 = threading.Thread(target=print_num,args=(1,5),name="小美")
    t2 = threading.Thread(target=print_num,args=(1,10),name="小帅")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("主线程结束")
