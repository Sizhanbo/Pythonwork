# os.walk () 递归遍历文件夹
"""
os.walk(
 top,          # 根目录路径
 topdown=True, # 遍历顺序（True=自顶向下，False=自底向上）
 onerror=None, # 错误处理函数（可选）
 followlinks=False # 是否通过软链接访问目录（可选）
)
"""
import os

data_dir = os.path.join(os.pardir, "data")


# all_data = os.walk(data_dir)
# print(type(all_data))
# print(all_data)

# for root, dirs, files in os.walk(data_dir):
#     print(f"当前目录：{root}")
#     print(f"子目录：{dirs}")
#     print(f"文件：{files}")
#     print("=========================================")

# 批量查找目录下的所有`.txt`文件
def find_txt_files(root_dir):
    """
    批量查找目录下的所有`.txt`文件
    :param root_dir: 要遍历的文件夹，在该文件夹当中获取所有的txt文件
    :return: 返回存放了所有txt文件的列表
    """
    txt_files = []
    for root, dirs, files in os.walk(data_dir):
        print(f"当前目录：{root}")
        print(f"子目录：{dirs}")
        print(f"文件：{files}")
        for file in files:
            if file.endswith(".txt"):
                file_abs_path = os.path.abspath(file)
                txt_files.append(file_abs_path)

    return txt_files


result = find_txt_files(data_dir)
for txt_file in result:
    print(txt_file)
