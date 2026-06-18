import os

# with 语句（推荐）：自动管理文件生命周期，代码块结束后自动关闭文件，简洁且安全
file_path = os.path.join(".", "..", "data", "a.txt")
with open(file_path, "w", encoding="utf-8") as f:
    f.write("abc")
print("写入文件成功")