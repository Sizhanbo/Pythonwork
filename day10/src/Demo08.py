# `send()`可在唤醒生成器的同时传递数据，实现双向通信：send()发送的数据作为yield表达式的结果
def echo_back():
    while True:
        x = yield
        if x == "quit":
            break
        yield f"收到: {x}"


g = echo_back()
next(g)
print(g.send("hello"))
print(g.send("quit"))
print(g.send("Python"))
print(g.send(1234))
