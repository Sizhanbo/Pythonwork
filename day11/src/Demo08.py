# 进程间通讯
# processing-pipe可以完成不同进程间的管道共享
import multiprocessing
import os

def send_data(pipe):
    """发送数据"""
    pipe.send("hello")
    print(f"发送数据成功，进程id:{os.getpid()}，接收数据:{pipe.recv()}")

def receive_data(pipe):
    """接收数据"""
    print(f"接收数据成功，进程id:{os.getpid()}，接收数据:{pipe.recv()}")
    pipe.send("word")


if __name__ == '__main__':
    con1,con2 = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=send_data, args=(con1,))
    p2 = multiprocessing.Process(target=receive_data, args=(con2,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()