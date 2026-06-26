# 多线程池操作
# concurrent.futures.ThreadPoolExecutor(max_workers=None, thread_name_prefix="", initializer=None, initargs=()) 线程池管理类
# 线程需求：网络请求
import threading
import time
from concurrent.futures.thread import ThreadPoolExecutor

import requests


# 模拟网络请求
def fetch_url(url):
    print(f"{threading.current_thread().name}正在请求的url为：{url}")
    try:
        start_time = time.time()
        response = requests.get(url, timeout=3)
        return f"{threading.current_thread().name}访问的{url}返回的状态码：{response.status_code}"
    except Exception as e:
        return f"{threading.current_thread().name}访问的{url}发生异常：{e}"
    finally:
        end_time = time.time()
        print(f"{threading.current_thread().name}访问{url}，用时{end_time - start_time}线程结束")


if __name__ == '__main__':
    url_list = [
        "https://www.baidu.com",
        "https://www.google.com",
        "https://www.github.com",
        "https://www.python.org"
    ]

    start_time = time.time()

    with ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(fetch_url, url_list)
        print( results)
        print( type(results))
        # 由于返回的数据是generator生成器，这里选择转成list列表
        results_list = list(results)

    for result in results_list:
        print( result)

    end_time = time.time()
    print(f"访问{url_list}地址，共耗时：{end_time - start_time}秒")
