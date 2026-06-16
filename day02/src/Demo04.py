# 字符串 字符串是不可变、有序的字符序列
str1 = "abc"
print(str1)
str1 = "xyz"  # 字符串变量可以重新赋值
print(str1)

print(str1[0])
print(str1[1:2])
print(str1 + "xyz")
print(str1 * 3)

print("--------------")
print("x" in str1)

# 常见字符串函数
print(str1.upper()) #修改大小写
print(str1.lower())
print(str1.title()) #首字母大写

print(str1.find("x"))
print(str1.find("a"))

str1 = "xyzxyz"
print(f"str1:{str1}")
print('str1.replace("x", "a")')
str2 = str1.replace("x", "a")
print(str2)

# 字符串分割与拼接
str3 = "www.baidu.com"
x = str3.split( ".")
print(x)
print(type(x))

str4 = "$".join(x)
print(str4)

# 原始字符串打印
print("hello\nworld")
print(r"hello\nworld")