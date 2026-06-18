#文本文件内容替换工具
import os


def batch_rename_files(dir_path,  prefix="file", ext=".txt"):
    """
    批量重命名文件
    :param dir_path: 文件夹路径
    :param prefix: 文件名前缀
    :param ext: 文件扩展名
    :return: 无
    """
    # 检查文件夹是否存在
    if not os.path.isdir(dir_path):
        print(f"文件夹不存在：{dir_path}")
        return
    # 获取文件夹内所有文件
    file_list = os.listdir(dir_path)
    print(file_list)

    for idx, file_name in enumerate(file_list, 1):
        print(file_name)
        file_path = os.path.join(dir_path, file_name)
        print(file_path)
        if os.path.isfile(file_path):
            new_file_name = f"{prefix}{idx}{ext}"
            print("新名字",new_file_name)
            new_file_path = os.path.join(dir_path, new_file_name)
            os.rename(file_path, new_file_path)
            print(f"重命名成功：{file_path} → {new_file_path}")

data_dir = os.path.join(os.pardir, "data","w")
batch_rename_files(data_dir,"my")

