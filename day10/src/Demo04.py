#自定义迭代器
class MyIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.lst):
            print("迭代完成")
            raise StopIteration
        else:
            item = self.lst[self.index]
            self.index += 1
            return item

my_iter = MyIterator([1, 2, 3, 4, 5])
for item in my_iter:
    print(item)