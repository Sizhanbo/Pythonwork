# 字符串格式化
"""
- 按顺序：`"{} {}".format(a, b)`
- 指定位置：`"{0} {1}".format(a, b)`
- 指定参数：`"{name} {age}".format(name="张三", age=18)`
- 数字格式化：`"{:*^20,.2f}".format(31415.9)`（居中、补 *、千分位、保留 2 位小数）
"""
str1 = "a"
str2 = "b"
print("第一个字母：" + str1 + "，第二个字母: " + str2)
print("第一个字母：{}，第二个字母: {}".format(str1, str2))
print("第一个字母：{1}，第二个字母: {0}".format(str1, str2))

name = "小张"
age = 18
print("我叫{}，我今年{}岁了".format(name, age))
print("我叫{myname}，我今年{myage}岁了".format(myname="小芳", myage=18))


numpi = 3.14159
print("圆周率是：{:.2f}".format(numpi))

# : 表示开始格式化，^居中  *除了要表示的数据外，剩余位置用*填充   20要展示出20个字符    ,数字大时，每3位加千分符  .2f 保留两位小数
print("{:*^20,.2f}".format(1215143.14159))

# f - 字符串
print(f"第一个字母：{str1}，第二个字母: {str2}")
print(f"我叫{name}，我今年{age}岁了")
print(f"我叫{name =}，我今年{age= }岁了")