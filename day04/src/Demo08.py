# 常见文件操作函数
# os.rename(old, new)
import os

print(os.pardir)
data_dir = os.path.join(os.pardir, "data")
file_name = "g.txt"
print(f"文件夹：{data_dir}")
print(f"文件：{file_name}")
file_path = os.path.join(data_dir, file_name)
print(file_path)
print(os.path.abspath(file_path))

print(os.path.dirname(file_path))
print(os.path.dirname(os.path.abspath(file_path)))
print("=========================================")

new_file_name = os.path.join(data_dir, "f.txt")
# os.rename(file_path, new_file_name)
dir_path = os.path.join(data_dir, "h")
dest_dir_path = os.path.join(data_dir, "i")
# os.rename(dir_path, dest_dir_path)

k_dir_path = os.path.join(data_dir, "j" ,"k")
# os.mkdir(k_dir_path)  # 创建目录 mkdir 只是创建一个目录，不能创建多级目录 父目录必须存在

p_dir_path = os.path.join(data_dir, "n", "o", " p")
# os.makedirs(p_dir_path) # 创建多级目录 makedirs 可以创建多级目录 包括父目录不存在的情况

print(os.getcwd())

s_dir_path = os.path.join(data_dir, "q", "r", "s")
os.makedirs(s_dir_path)
# os.removedirs(s_dir_path)

pic_c_path = os.path.join(data_dir, "c.jpg")
print(os.path.getsize(pic_c_path))

# 无法获取文件夹大小
print(os.path.getsize(s_dir_path))