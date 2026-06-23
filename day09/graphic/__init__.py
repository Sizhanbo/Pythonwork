# 模块中有__all__ 用于指定，当from 模块 import * 时，导入的成员。如果模块没给all属性，则默认所有的非私有成员都可以使用

# 包中，__init__.py文件中，__all__属性  用于指定，当from 包 import * 时，导入的模块。
# 如果包的init中没给all属性，则没有默认模块可以使用

__all__ = [
    "circle",
    "rectangle",
]