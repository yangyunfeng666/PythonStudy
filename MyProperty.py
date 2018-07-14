class MyProperty:
    def __init__(self,getm = None,setm= None,delm = None):
        self.getm = getm
        self.setm = setm
        self.delm = delm

    def __get__(self, instance, owner):
        return self.getm(instance)

    def __set__(self, instance, value):
        self.setm(instance,value)

    def __delete__(self, instance):
        self.delm(instance)


class Method :
    def __init__(self):
        self._x = '呜呜呜呜'

    def getX(self):
        return self._x

    def setX(self,value):
        self._x = value

    def delX(self):
        del self._x

    x = MyProperty(getX,setX,delX)


test = Method()

print(test.x)

test.x = '1231231'

print(test.x)

print(getattr(test,'x','没有这个属性'))
del  test.x

print(getattr(test,'x','没有这个属性'))