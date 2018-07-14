#迭代器
for i in "fishc":
    print(i)

it = iter("fishc")#得到对象的迭代器对象

print(next(it))#返回迭代器下个值
print(next(it))

#斐波那契数列
class Fibs :
    def __init__(self,n = 10):
        self.a = 0
        self.b = 1
        self.n = n
    def __iter__(self):
        return self

    def __next__(self):
        self.a ,self.b = self.b ,self.a + self.b #多数据赋值以，分开
        if self.a > self.n:
            raise  StopIteration
        else:
            return self.a

fibs = Fibs(100)
for i in fibs:
        print(i)
