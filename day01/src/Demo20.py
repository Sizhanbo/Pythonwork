# if语句基本格式：满足条件就执行不满足不执行
#if elif... else
# 请输入年龄，根据年龄判断你吃什么，0-3岁喝奶粉，4-20多吃，21-60吃保健品，60-120想吃啥吃啥，打印你是不是人？
age = input("根据年龄判断你需要吃什么，请输入年龄：")
if 0 < int(age) <= 3:
    print("喝奶粉")
elif 4 <= int(age) <=20:
    print("多吃")
elif 21 <= int(age) <= 60:
    print("吃保健品")
elif 60 <= int(age) <= 120:
    print("想吃啥吃啥")
else:
    print("是不是人？")