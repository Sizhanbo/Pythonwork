import random
"""
	产生随机0-100分。
	0-59分		不及格
 	60-100分	   及格
		60-69         及格水平
        70-89         良好水平
        90-100       优秀水平      
	其他情况：数据出错                         
"""
score = random.randint(0,100)
print(f"score = {score}")
if 0 <= score <= 59:
    print("不及格")
elif 60 <= score <= 100:
    print("及格")
    if 60 <= score <= 69:
        print("及格水平")
    elif 70 <= score <= 89:
        print("良好水平")
    elif 90 <= score <= 100:
        print("优秀水平")
else:
    print("数据出错")
