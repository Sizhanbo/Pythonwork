import os
def replace_text_in_file(input_path, output_path, old_str, new_str, encoding="utf-8"):
    """
    替换文本文件中的指定字符串
    :param input_path: 输入文件路径
    :param output_path: 输出文件路径
    :param old_str: 要替换的旧字符串
    :param new_str: 替换后的新字符串
    :param encoding: 文件编码（默认UTF-8）
    """
    try:
        with open(input_path, "r", encoding=encoding) as input_file:
            content = input_file.read()
            new_content = content.replace(old_str, new_str)
        with open(output_path, "w", encoding=encoding) as output_file:
            output_file.write(new_content)
        print(f"替换成功，已保存到{output_path}")
    except FileNotFoundError:
        print(f"输入文件{input_path}不存在")
    except Exception as e:
        print(f"发生错误：{e}")

data_dir =  os.path.join(os.pardir, "data")
source_file_path = os.path.join(data_dir, "v.txt")
dest_file_path = os.path.join(data_dir, "v2.txt")
replace_text_in_file(source_file_path, dest_file_path, "a", "c")

