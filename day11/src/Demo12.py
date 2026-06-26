# 自定义线程类
# 只需继承threading.Thread即可
import threading
import time


class MyThread(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        print(f"线程{threading.current_thread().name}开始执行 | 线程ID: {self.ident}")
        time.sleep(1)
        print(f"线程{threading.current_thread().name}结束执行")


if __name__ == '__main__':
    t1 = MyThread("小美")
    t2 = MyThread("小帅")
    t3 = MyThread("大壮")
    t1.start()
    t2.start()
    t3.start()

    print(threading.current_thread().name)
