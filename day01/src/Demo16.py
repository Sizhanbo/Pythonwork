# 比较运算符，最终结果一定是布尔值，方便后续判断，执行不同的分支逻辑
int1 = 100
int2 = 200
print(int1 == int2)

int3 = 300
str1 = "100"
print( int3 == str1)  # 字符串数字，可以与 整数进行==号的判断
# print( int3 > str1)  # 字符串数字，不可以与 整数进行大小判断的

str2 = "abcddd"
str3 = "acc"
print( str2 == str3)
print( "a" < "b")  #  字符串英文字符是按照字母顺序进行比较的
print( "a" > "A")  #  字符串比较按 ASCII 码逐字符比较
print( str2 < str3)