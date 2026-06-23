import math
import math_tools
print(dir(math))

members = dir(math_tools)
print(members)

for member in members:
    if not member.startswith("_"):
        print(member, getattr(math_tools, member))

print("===========================")
print(math_tools.add)
print(math_tools.add.__name__)
print(math_tools.add.__doc__)
print(math_tools.add.__annotations__)

print("===========================")
def test_func():
    pass

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


print("当前作用域的名称：")
for name in dir():
    if not name.startswith("_"):
        print(f"  {name}")  # 输出：math_tools、test_func等