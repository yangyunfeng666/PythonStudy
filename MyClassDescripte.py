class MyclassDescripte:
    def __get__(self, instance, owner):
        print("getting",self,instance,owner)

    def __set__(self, instance, value):
        print("setting",self,instance,value)

    def __delete__(self, instance):
        print("delete",self,instance)


class Test:
    x = MyclassDescripte()


test = Test()

print(test.x)

print(test)

print(Test)

test.x = 'hellp'

del  test.x


