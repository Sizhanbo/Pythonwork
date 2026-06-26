# 多进程操作
import multiprocessing
import time

def write(event):
   with open('../date/file.txt', 'a', encoding='utf-8') as f:
       count = 0
       while count <= 5:
           f.write('写入第%d行数据\n' % count)
           f.flush()  # 强制落盘
           count += 1
           time.sleep(0.1)
   print('写入完成...')
   event.set()  # 通知 read：写入完成了

def read(event):
    with open('../date/file.txt', 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if line:
                print(f"读取数据->:{line.strip()}")
            else:
                # 检查写入是否完成
                if event.is_set():
                    print("读进程：写完了，也读完了，结束...")
                    break
                else:
                    print("读进程：还没写完，等待...")
                    time.sleep(0.1)  # 等一会再读

if __name__ == '__main__':
    # 清空文件
    open('../date/file.txt', 'w').close()
    
    # 创建共享 Event
    event = multiprocessing.Event()
    
    pw = multiprocessing.Process(target=write, args=(event,), name='write_process')
    pr = multiprocessing.Process(target=read, args=(event,), name='read_process')
    
    pw.start()
    pr.start()
    
    pw.join()
    pr.join()
