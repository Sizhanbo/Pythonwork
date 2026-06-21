#方法的调用顺序
class A:
    def func(self):
        print("A")

class B(A):
    def func(self):
        print("B")

class C(A):
    def func(self):
        print("C")

class D(C, B):
    pass

print(D.__mro__)

d = D()
d.func()