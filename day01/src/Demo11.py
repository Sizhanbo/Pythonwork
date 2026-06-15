# 字符的编码和解码
# ASCII码表：字符与数字的对应关系，一个字符占用一个字节，里边包含了所有基础字符

ascii_char = chr(97)
print(ascii_char)


# 指定码表,编码解码
txt = "你好101a"
bytes1 = txt.encode("utf-8")
print(bytes1)
print(bytes1.decode("utf-8"))