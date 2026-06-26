# 批量向进程池中提交任务
# 计算某个数的平方，故意sleep0.5秒，模拟耗时操作
import multiprocessing
import os
import time

# 任务函数
def calculate(num):
    print(f"进程 {os.getpid()} 正在计算 {num} 的平方...")
    # 模拟耗时
    time.sleep(0.5)
    return num ** 2

# 进程池
# main中的需求：求进程池中所有进程运行时间之总和
if __name__ == '__main__':

    # 准备好开始时间
    start_time = time.time()

    # 准备进程池中的进程个数
    process_num = 5

    # 创建进程池
    pool = multiprocessing.Pool(process_num)

    # 提交任务
    # 同步操作
    # results = [pool.apply(calculate, (i+1,)) for i in range(10)]
    # 异步操作
    results = pool.map(calculate, range(10))

    # 关闭进程池
    pool.close()
    # 等待进程池中所有任务结束
    pool.join()

    # 执行main函数部分的其他后续操作
    print(f"任务结果：{results}")
