# # 另一个导包案例的使用--- data_process包的使用
# import data_process.io_tools
# data_process.io_tools.read_txt("data.txt")
#
# import data_process.clean_tools as ct
# print(ct.drop_null([1, 2, 3, None, 4, 5, 6]))
#
# from data_process import io_tools
# io_tools.write_txt(["1", "2", "3"], "data.txt")
#
# # 导入暴露出来的接口
# from data_process import read_txt,write_txt,remove_duplicates,drop_null
# read_txt("test.txt")

