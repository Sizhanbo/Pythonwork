#读取数据
import os
data_path = os.path.join(os.pardir, "data")

file_name="b.txt"
file_path = os.path.join(data_path, file_name)

# 一次性读取文件中所有内容！不适用于大数据的
# with open(file_path, "r") as f:
#     data = f.read()
#     print(data)

    # 按行读取，适用于大型文本文档

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)

    for idx, line in enumerate(lines, start=1):
        print(f"第{idx}行：{line.strip()}")