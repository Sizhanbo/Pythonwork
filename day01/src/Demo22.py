# match case 语句练习
# 根据不同月份，输出不同季节

month = int(input("请输入月份："))

match month:
    case 1 | 2 | 12:
        print(f"{ month}月为冬")
    case 3 | 4 | 5:
        print(f"{ month}月为春")
    case 6 | 7 | 8:
        print(f"{ month}月为夏")
    case 9 | 10 | 11:
        print(f"{ month}月为秋")
    case _:
        print(f"您没有输入正确的月份...")