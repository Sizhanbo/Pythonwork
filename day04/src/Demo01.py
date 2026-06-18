# 从这里，通过相对路径找a.txt
# ./../data/a.txt
import os.path

print(os.path.isfile("./../data/a.txt"))

file_path = os.path.join(".","..", "data", "a.txt")
print(file_path)
print(os.path.isfile(file_path))

current_dir = os.getcwd()  # 返回当前工作目录路径
print(current_dir)