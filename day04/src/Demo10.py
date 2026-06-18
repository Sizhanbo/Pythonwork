# 文件拷贝
import os

# 整体读取，整体拷贝
def copyFile(source_file_path, dest_file_path):
    """
    文件拷贝
    :param source_file_path: 源文件路径
    :param dest_file_path: 目标文件路径
    :return: 无
    """
    # 打开源文件(二进制模式，兼容所有文件类型)
    source_file = open(source_file_path, "rb")
    # 读取文件内所有数据
    content = source_file.read()

    # 打开目标文件(二进制写入)
    dest_file = open(dest_file_path, "wb")
    # 写入数据到目标文件
    dest_file.write(content)

    # 关闭文件， 释放资源
    source_file.close()
    dest_file.close()


# 分块复制
def copyFile2(source_file_path, dest_file_path):
    """
    文件拷贝
    :param source_file_path: 源文件路径
    :param dest_file_path: 目标文件路径
    :return: 无
    """
    # 打开源文件(二进制模式，兼容所有文件类型)
    source_file = open(source_file_path, "rb")

    # 打开目标文件(二进制写入)
    dest_file = open(dest_file_path, "wb")

    # 分块读取(每次1024个字节), 避免大文件占用过多内容
    content = source_file.read(1024)
    while content:
        dest_file.write(content)
        content = source_file.read(1024)

    # 关闭文件， 释放资源
    source_file.close()
    dest_file.close()



def copyFile3(source_file_path, dest_file_path, chunk_size=1024):
    """
    文件拷贝
    :param source_file_path: 源文件路径
    :param dest_file_path: 目标文件路径
    :param chunk_size: 分块大小
    :return: 无
    """
    # 检查源文件是否存在
    if not os.path.isfile(source_file_path):
        print(f"源文件不存在：{source_file_path}")
        return

    # 复制操作，读取源文件(二进制模式，兼容所有文件类型)
    with open(source_file_path, "rb") as src:
        with open(dest_file_path, "wb") as  dest:
            # 反复读取写入
            while True:
                # 先读(每次读取到chunk中)
                chunk = src.read(chunk_size)
                if not chunk:  # 读取到空，文件结束
                    break
                dest.write( chunk)
    print(f"拷贝成功:{source_file_path} → {dest_file_path}")
    print(f"文件大小：{os.path.getsize(dest_file_path)}b")


data_dir =  os.path.join(os.pardir, "data")
source_file_path = os.path.join(data_dir, "a.jpg")
dest_file_path = os.path.join(data_dir, "b.jpg")
copyFile3(source_file_path, dest_file_path)
