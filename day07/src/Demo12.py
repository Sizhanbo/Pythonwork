import requests
from requests.exceptions import RequestException, Timeout, ConnectionError
# 发送网络请求，请求一个URL，并返回JSON数据

def fetch_data(url, timeout=5):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()  # 检查HTTP状态码
        return response.json()
    except Timeout:
        print(f"请求 {url} 超时")
        return None
    except ConnectionError:
        print(f"无法连接到 {url}")
        return None
    except requests.HTTPError as e:
        print(f"HTTP 错误: {e}")
        return None
    except RequestException as e:
        print(f"请求异常: {e}")
        return None
    except Exception as e:
        print(f"其他错误: {e}")
        return None

print(fetch_data("https://v1.hitokoto.cn/"))