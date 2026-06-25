#生成器（函数）
def gen():
    for i in range(10):
        yield i


print(type (gen()))
print(list(gen()))
print(tuple(gen()))
g = gen()
while True:
    try:
        print(next(g))
    except StopIteration:
        break
print("===================================")

def fibo():  # 斐波那契数列
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

f = fibo()
print(next(f))  # 1
print(next(f))  # 1
print(next(f))  # 2
print(next(f))  # 3
print(next(f))  # 5

print("===================================")

def fibo(n):   # 斐波那契数列
      a, b, counter = 0, 1, 0
      while counter < n:
            yield b
            a, b, counter = b, a + b, counter + 1
      return "done"

f = fibo(10)
try:
      while True:
            print(next(f))
except StopIteration as result:
      print("StopIteration", result)   # StopIteration done




