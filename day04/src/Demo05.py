# 文件写出动作
# 二进制文件写出
import os

# 用二进制方式写出文本
file_path = os.path.join(".","..", "data", "c.txt")

with open(file_path, "wb") as f:

    bytes1 = "abc你好".encode("utf-8")
    f.write(bytes1)
    # 用什么编码表写出数据，查看这个文件时，使用对应的编码表打开观察数据，否则乱码


# 用二进制方式写出图片
# 先读数据
file_path = os.path.join(".","..", "data", "a.jpg")
with open(file_path, "rb") as f:
    data = f.read()

# 后写数据
file_path = os.path.join(".","..", "data", "c.jpg")
with open(file_path, "wb") as f:
    f.write(data)