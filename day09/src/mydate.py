import datetime

# 获取当前日期时间
now = datetime.datetime.now()

# 常用日期格式示例
date_formats = {
    "年-月-日": now.strftime("%Y-%m-%d"),
    "月/日/年": now.strftime("%m/%d/%Y"),
    "日-月-年": now.strftime("%d-%m-%Y"),
    "完整日期": now.strftime("%Y年%m月%d日"),
    "星期几": now.strftime("%A"),
    "星期缩写": now.strftime("%a"),
    "月份全称": now.strftime("%B"),
    "月份缩写": now.strftime("%b"),
    "时:分:秒": now.strftime("%H:%M:%S"),
    "12小时制": now.strftime("%I:%M:%S %p"),
    "年份后两位": now.strftime("%y"),
    "完整年份": now.strftime("%Y")
}

print("当前日期时间:", now)
print("\n格式化日期示例:")
for format_name, formatted_date in date_formats.items():
    print(f"{format_name}: {formatted_date}")
