class C:
    def __init__(self):
        self.size = 1


    def getSize(self):
        return  self.size

    def setSize(self,size):
        self.size = size

    def delSize(self):
        del self.size

    x = property(getSize,setSize,delSize)#设置属性方法的代理为x


    def __getattribute__(self, item):#定义属性被访问时候
        print("__getattribute__")
        return  super().__getattribute__(item)
    def __getattr__(self, item):#定义一个没有属性的访问时候
        print("getattr")
    def __setattr__(self, key, value):#设置属性时候调用
        print("setattr")
        return super().__setattr__(key,value)
    def __delattr__(self, item):#删除属性时候调用
        print("__delattr__")
        super().__delattr__(item)

c = C()

c.x = 1

print(c.size)

del c.x

print(getattr(c,'size','没有这个属性'))


class Rectangle:
    def __init__(self,width=0,height=0):
        self.width = width
        self.height = height

    def __setattr__(self, key, value):
        if key == 'sequre':
            self.width = value
            self.height = value
        else:
            self.key = value

    def getAre(self):
        return self.width * self.height


