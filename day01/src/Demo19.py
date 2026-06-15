# 身份运算符   id展示对象地址(身份)
int1 = 1
int2 = 1
bool1 = True

print(id(int1))
print(id(int2))
print(id(bool1))

print(int1 == int2)
print(int1 is int2)

print(int1 == bool1)
print(int1 is bool1)

print(1+2*3)
