"""
    数据工具包，对数据进行加工操作
"""

# 版本信息
__version__ = "0.1.0"
# 作者信息

__author__ = "szb"
__email__ = "abc@aaa.com"
__date__ = "2021/09/01"

# 声明，当使用from  包  import * 的方式使用包内容时，可以使用的模块
__all__ = [
    "io_tools",
    "clean_tools",
]

#暴露公共接口(成员)
from .io_tools import read_txt,write_txt
from .clean_tools import remove_duplicates,drop_null
