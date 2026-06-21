# 断言 assert，用于调试

def add(x,y):
    assert isinstance(x,int) and isinstance(y,int),"参数类型错误： 仅支持数字相加"
    return x+y

try:

    print(add(10,"中"))

except AssertionError as ae:
    print(ae)

print("后续代码执行...")