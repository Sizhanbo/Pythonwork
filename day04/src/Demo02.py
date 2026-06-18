import os
#常规读取
file_path = os.path.join(".", "..", "data", "a.txt")

f = open(file_path, "r", encoding="utf-8")
print(f.read())


f.close()
