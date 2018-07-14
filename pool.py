class Trutle:
    def __init__(self,x):
        self.x = x

class Fish:
    def __init__(self,y):
        self.y = y

class Pool:
     def __init__(self,x,y):#组合 把类放到一起
         self.trutle = Trutle(x)
         self.fish = Fish(y)
     def show(self):
         print("水池里面有%d只乌龟，鱼有%d条" % (self.trutle.x,self.fish.y))
pool = Pool(1,10)
pool.show()

class A:
    pass
class B(A):pass

a  = A()
b = B()

print(issubclass(B,B))
print(issubclass(B,A))
print(issubclass(B,(Fish,Pool,object)))#object是所有类的基类
print(isinstance(a,A))
print(isinstance(b,Fish))

#这里str类不能改变，我们只能在init之前做处理，把他转换成大写然后再传递给str
class CapStr(str):
    def __new__(cls,string):#重写new方法
        string = str.upper(string)
        return str.__new__(cls,string)

v = CapStr("I love You Zhangjialan")
print(v)
#析构函数在垃圾回收机制时候才调用，什么时候触发垃圾回收呢，他没有引用了
class cc:
    def __init__(self):
        print("cc 初始化了")
    def __del__(self):
        print("垃圾回收了")

vv = cc();
c1 = vv;
c2 = c1
del c2
del c1
del vv


class new_int(int):
        def __add__(self, other):
            return int.__sub__(self,other)
        def __sub__(self, other):
            return int.__add__(self,other)
        def __radd__(self, other):#反向加
            return int.__sub__(self,other)
        def __iadd__(self, other):#增量加
            return int.__sub__(other,self)

a = new_int(5)
b = new_int(7)
print(a+b)
print(1+b)
a+=5
print(a)