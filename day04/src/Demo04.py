# 文件写出动作
import os

file_path = os.path.join(".", "..", "data", "b.txt")

# with open(file_path, "w", encoding="utf-8") as f:
#     f.write("abc")
#     f.write("def")
#     f.write("ghi")
# print("写入文件成功")
#


# with open(file_path, "w", encoding="utf-8") as f:
#     lines = ["abc", "def", "ghi" + os.linesep] * 4
#     f.writelines(lines)
#
# print("追加文件成功")

with open(file_path, "w", encoding="utf-8") as f:
    lines = ["abc", "def", "ghi" + os.linesep] * 4

    for line in lines:
       print(line, file=f)

print("追加文件成功")
