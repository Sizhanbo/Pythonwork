# 文件指针操作
# 模式r+
# tell()`获取当前指针位置
# seek(偏移量,参数2)`移动指针    参数2：0 文件开头，1 当前位置，2 文件末尾
# 文件结尾为追加操作，其他位置为覆盖操作
import os

print(os.pardir)
data_dir =  os.path.join(os.pardir, "data")
file_name = "e.txt"
print(f"文件夹：{data_dir}")
print(f"文件：{file_name}")
file_path = os.path.join(data_dir, file_name)

with open(file_path,"r+", encoding="utf-8") as f:
    print("当前指针位置：", f.tell())
    print(f.read(1))
    print("当前指针位置：", f.tell())
    f.seek(0,1)
    f.write("xxx")
    f.seek(0,0)
    f.write("yy")
    f.seek(0,2)
    f.write("z")
