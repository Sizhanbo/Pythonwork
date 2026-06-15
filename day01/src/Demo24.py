# while循环
"""
while 表达式:
    循环体  # 表达式为真时重复执行
else:
    语句  # 循环正常结束（未被break终止）时执行
"""

# 循环1-5
num = 1
while 1 <= num <= 5:
    print(f"当前数字是：{num}")
    num += 1  # 步进数为1(循环变量的变化情况)
else:
    print("num超过5了，不再打印")

print("后续执行其他代码")

# while练习
"""
模拟电池充电过程，每次充电1-5，0.4秒充一次，到100%结束
"""
import random
import time
all_amount = 0

while True:
    num = random.randint(1, 5)
    all_amount += num
    if all_amount >= 100:
        print("当前电量是:100")
        print("充电结束")
        break
    print(f"当前电量是：{all_amount}")
    time.sleep(0.4)
