class MyTest:
    #属性
    color = 'green'
    weight = 4
    legs = 4
    mouth = '4月'
    def metouh(self):
        print('睡了')

tt = MyTest()

class MyList(list):pass #myList继承于list集合方法和属性
mylist = MyList()
mylist.append(4)
mylist.append(5)
mylist.append(2)
print(mylist)
mylist.sort()
print(mylist)

class boll:
    def __init__(self,name):#自定义构造方法 覆盖了默认的构造函数
        self.name = name
    def setname(self,name):#设置方法需要传递self，这个是自己对象的指针
        self.name = name
    def kick(self):
        print("朝你妹的，我叫%s该死的谁提我" % self.name)

a = boll('张佳楠')
a.setname('张佳楠')
b = boll('张佳楠')
b.setname('杨云锋')
a.kick()
b.kick()
c = boll('杨二娃')
c.kick()
import  random as r
class Fish:
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)
    def move(self):
        print('我的位置是:',self.x,self.y)

class Goldfish(Fish):pass
class XiaoYu(Fish):pass
class Shark(Fish):#鲨鱼
    def __init__(self):
       # Fish.__init__(self)#1.调用父类未绑定的用的方法
        super().__init__() # 2.使用super方法调用
        self.huagury = True
    def eat(self):
        if self.huagury==True:
            print("吃货的数据你不懂")
            self.huagury = False
        else:
            print("我是包的")
fiseh = Fish()
fiseh.move()

gloadFish = XiaoYu()
gloadFish.move()

shark = Shark()
shark.eat()
shark.move()