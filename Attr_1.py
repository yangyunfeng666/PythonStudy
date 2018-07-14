
class Rectangle:
    def __init__(self,width=0,height=0):
        self.width = width
        self.height = height

    def __setattr__(self, key, value):
        if key == 'sequre':
            self.width = value
            self.height = value
        else:#操作他的属性方法
            # super().__setattr__(key,value) 1.种是重写super的setattr方法
            self.__dict__[key] = value#2 使用__dict__ 去更新
            # self.key = value#这个嵌套赋值，有问题

    def getAre(self):
        return self.width * self.height


c = Rectangle(4,5)
print(c.width)
print(c.height)
print(c.getAre())

print(c.__dict__)#属性字典
# c.__dict__.update()

