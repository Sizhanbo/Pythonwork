# continue:跳出当前这轮循环，直接进入下一轮循环

# for num in range(10):
#     # 如果是4就跳出不打印
#     if num == 4:
#         continue
#     print(f"当前循环到的元素是:{num}")

"""
有如下主题：posts = [
    "今天天气真好",
    "spam广告内容",
    "分享一个有趣的故事",
    "垃圾邮件推广",
    "Python编程技巧"
]
有如下禁用关键字：spam_keywords = ["spam", "广告", "垃圾"]

请过滤，即遍历所有主题，包含禁用关键字的不显示
"""
posts = [
    "今天天气真好",
    "广告内容",
    "分享一个有趣的故事",
    "垃圾邮件推广",
    "Python编程技巧"
]

spam_keywords = ["广告", "垃圾"]

for post in posts:

    hasSpam = False
    # 判断是否包含敏感词
    for spam_keyword in spam_keywords:
        if spam_keyword in post:
            print(f"{post}含有垃圾词汇，予以过滤！")
            hasSpam = True

    if not hasSpam:
        print(f"本次主题:{post}")