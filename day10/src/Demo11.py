# 构建闭包
def make_multiplier(x, y):
    def multiplier(n):
        return x * n + y
    return multiplier

p=make_multiplier(2,3)
print(p(5)) #   13

