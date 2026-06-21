# 异常处理：文件操作
import json

def read_config_file(file_path):
    try:
        with open(file_path,"r",encoding="utf-8") as f:
            print(f"正在读取文件：{file_path}...")
            content = f.read()
            # 将返回的数据，转成一个json对象
            return json.loads(content)
    except FileNotFoundError:
        print(f"文件不存在：{file_path}")
        return {}
    except json.JSONDecodeError as e:
        print(f"JSON解析错误：{e}")
        return {}
    except Exception as e:
        print(f"其他错误：{e}")
        return {}

data_json = read_config_file("../data/config.json")
print(data_json)
