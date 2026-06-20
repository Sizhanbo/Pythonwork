# 定义功能,面向过程
def grow_up(person):
    """成长"""
    person['age'] += 1
    if person['age'] <= 3:
        person['stage'] = '婴儿'
    elif person['age'] <= 18:
        person['stage'] = '少年'
    elif person['age'] <= 60:
        person['stage'] = '成年'
    else:
        person['stage'] = '老年'
    print(f"{person['name']}现在{person['age']}岁，处于{person['stage']}阶段")


def study(person):
    """学习"""
    if person['stage'] == '少年':
        print(f"{person['name']}正在学校认真学习")
    else:
        print(f"{person['name']}在人生中不断学习成长")


def work(person):
    """工作"""
    if person['stage'] == '成年':
        print(f"{person['name']}努力工作，为社会做贡献")
    else:
        print(f"{person['name']}还未到工作年龄")


def retire(person):
    """退休"""
    if person['stage'] == '老年':
        print(f"{person['name']}安享晚年，回顾人生")


# 记录数据
person = {'name': '小明', 'age': 0, 'stage': '婴儿'}

for year in range(80):
    grow_up(person)
    if person['stage'] == '少年':
        study(person)
    elif person['stage'] == '成年':
        work(person)
    elif person['stage'] == '老年':
        retire(person)

person = {'name': '小红', 'age': 0, 'stage': '婴儿'}

for year in range(80):
    grow_up(person)
    if person['stage'] == '少年':
        study(person)
    elif person['stage'] == '成年':
        work(person)
    elif person['stage'] == '老年':
        retire(person)
