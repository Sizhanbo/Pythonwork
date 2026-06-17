# 变量引用
a = "abc"
print(f"{a} 的引用地址是：{id(a)}")
b = "xyz"
print(f"{b} 的引用地址是：{id(b)}")
a = b
print(f"{a} 的引用地址是：{id(a)}")