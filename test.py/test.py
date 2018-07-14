temp = ['dsdd','dsdsd','dsadasda']
print(temp)




num = [1,2,34,5,2,434,52,5233]
num.sort()#指定方法进行排序
print(num)

newstr ="{0} Love {b} {c}".format("I",b="fish.com",c="com")
print(newstr)
gg = "{0:.1f}{1}".format(27.665,"GB")#:是格式化的开始符合
print(gg)
ss = '%c' % 97 # % 号转义通过% 把取97的ASCII码
print(ss)
snat = '%c %c %c' % (98,99,48)#使用元组来替换多个参数的格式化
print(snat)
ss = '%s' % "I love"
print(ss)
result = '%d + %d = %d' % (4,5,4+5)
print(result)
print('%x' % 10)#十进制
print('%X' % 10)#十进制
print('%f' % 27.444)#付点类型
print('%e' % 12.3232)#科学计数法e
print('%E' % 12.3232)#科学技术法E
print('%5.1f' % 23.333)#m.n m是最小总宽度，n是小数点后面的位数
print('%.2e'% 1212.32332)
print('%+d' % 1212.32332)#显示正负号
print("\'")#转义字符\
print('%#o' % 12)#显示 # 如果是八进制0o 如果是十六进制0x 如果是十进制什么都不显示
print('%10d' % 5)#使用00来填充位置
print('%-10d' % 5)#使用00来填充位置在后面
print('\\')
sss = list()
print(sss)

print(list("dsdsdsd"))#把数据转成列表 字符串数组
num = [1,2,3,2,323,4,3,32,5,3464,2,312,422]
print(max(num))#取数组的最大值
print(max(1,2,3,4,5,6))
print(min(num))#返回数组的最小值
print(min('112321300320'))#注意数据的类型必须是相同的，
print(sum(num))#求和
print(sorted(num))#排序
print(list(reversed(num)))#倒序排reversed 返回迭代器
a = [1,2,3,4,5,7]
b = [2,3,4,2,32,4,2]
print(list(zip(a,b)))#列表a 和b 成对的打包
#定义一个函数
def myFirstFunction():
    print("这是我创建第一个函数：")
    print("我表示很激动")
myFirstFunction()#往上查找函数

def mySecondFunction(name,name2):
    print(name+":"+name2+"爱你哟")

mySecondFunction('张佳楠',"杨云锋")
#数据相加
def addsum(num1,num2):
    '函数文档'
    return (num1+num2)

print(addsum(1,3))
#打印函数文档
print(addsum.__doc__)
print(print.__doc__)

mySecondFunction(name='张佳楠',name2='杨云锋')
#默认的参数，在初始化的给形式参数赋值
def saySome(name='小金鱼',world = '让编程改变世界'):
    '苍老师好美'
    print(name+'->'+"大师的撒大大")
saySome('苍井空')
#收集参数 不知道参数有多少个 *开头
def test(*parems,exp = 9):
    print('参数的长度是',len(parems),exp)
    print('第二个参数是',parems[1])
test(1,2,'xiao驾驭',exp='dsds')

print(type(test))
#python严格来说这样函数没有过程
#参数是动态的类型
#可以返回多个返回值
def back():
    return 1,2,3,4
print(back())#返回的元组
#在函数的声明的时候，内部的局部变量，只能在函数内部访问。
#全局变量的使用可以在任何地方访问。
#在局部修改全局变量，Python会为全局变量会新建一个一样的值在局部变量。

def fff(price,count):
    newprice = 50
    print("新的价格"+str(newprice))

newprice = 100
fff(price=110,count=80)
print(newprice)

count = 5
def sum():
    global  count
    count = 10
print(count)

def fun1():
    print("fun1 的数据")
    def fun2():
        print("fun2 的数据")
    fun2() #只能在函数fun1内部调用

fun1()

def funx(x):
    def funy(y):
        return x*y
    return funy

i = funx(4)
print(type(i))
print(funx(5)(5))
#使用容器对象，
def funz():
    x = [6]
    def funm():
        x[0]*=x[0]
        return x[0]
    return funm()

print(funz())

#使用nolocal 处理内部变量
def funu():
    x = 6
    def funm():
        nonlocal x
        x*=x
        return x
    return funm()

print(funz())
#匿名函数 lambal表达式
def d(x,y):
   return 2 * x + 1 + y

g = lambda x,y:2 * x +1+y #：前面是函数的参数，函数的后面是函数的返回值 可以简介函数
print(g(5,4))

# filter 过滤器 保留关注的事情
#如果第一个参数是None时候是把第二个迭代器里面的对象为ture的筛选出来
print(list(filter(None,[1,'r',False,True])))
#如果第一个参数是方法，那么会把第二个参数集合的东西都忘方法里面，然后返回为true的集合数据
#方法一个集合
def fund(x):
    return x % 2
print(list(filter(fund,range(10))))
print(list(filter(lambda x: x % 2,range(10))))
#map 映射处理加工
#是把集合的每一个元素在map的第一个参数的方法进行加工，然后返回再组成一个集合返回
print(list(map(lambda x: 2* x,range(10))))


def jieche(x):
    result = x;
    for i in range(1,x):
        result *= i
    return result

print(jieche(5))

#递归的，1.调用函数的自身，2.有一个正确的返回条件
def dg(x):
    if x==1:
        return 1
    else:
        return x*dg(x-1)

print(dg(5))
#斐波那契数列
#（1）迭代使用

def fun(n):
    n1 = 1
    n2 = 1
    n3 = 1
    if n < 1 :
       result -1

    while n-2 >0:
        n3 = n2+n1
        n1 = n2
        n2 = n3
        n -= 1

    return  n3
result = fun(20)

if result == -1:
    print("数据有无")
else:
    print("总共有%d" % result)

#递归实现
def fund(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return  fund(n-1)+fund(n-2)

print("总共有%d" % fund(20))
#分治思想

#汉诺塔
def hanota(n,x,y,z):
    if n == 1:
       print(x,"-->",z)
    else:
        hanota(n-1,x,z,y) # 将n-1个盘子从x移动到y
        print(x, "-->", z)# 将盘子从x 移动到z
        hanota(n-1,y,x,z) #将 n-1 个盘子从y 移动到z

hanota(3,'x','y','z')
#字典（映射（1对1 1对多））由多个建和值组合在一起{}
dicts = {'李宁':'一切皆有可能','我':'干吧少来'}
print('我的口号是',dicts['我'])
dircts = {1:'one',2:'two',3:'three'}
dircts[1]
dirc1 = dict(((1,'one'),(2,'two')))#声明方式
print(dirc1)
dirc2 = dict(小金鱼='one',密码='12345')#直接建值形式
print(dirc2)
dirc2['密码']= '12dsds'#修改
dirc2['天才']= '百分之九十九的汗水+百分之一的灵感，但是百分之一的灵感远远比百分之九十九的汗水强很多'#如果没有建那么添加建和值进去
print(dirc2)
#内建方式
print(dirc2.fromkeys(('密码')))#得到值，如果没有返回None

for i in dirc2.keys():#读取建
    print(i)

for i in dirc2.items():#索引items
    print(i)

for i in dirc2.values():#索引值
    print(i)
print(dirc2.get('密码','无用'))#得到方法

#检测数据的成员是否在
print('密码' in dirc2) #使用建是否在字典中

a = {'a':'xxx'}
b = a
a = {}
print(b)
a = {'a':'xxx'}
b = a
a.clear()#清楚是都能清楚b
print(b)

c = {'cc':'dsds'}
d = c.copy()#浅拷贝是取值
e = d #赋值 地址拷贝
print(id(c))
print(id(d))
print(id(e))

f = c.pop('cc')#弹出值 以建时候取出
print(f)
print(c)
h = d.popitem();#弹出项
print(h)
print(d)

d.setdefault('小标',"values")
print(d)
m = {'小标':'cao'}
d.update(m)#修改某项的值
print(d)

#集合在所以的数据是唯一，无序的，不支持索引
##创建集合
set1 = {1,2,3,4,1,3,5,6}
print(set1)
###创建使用set 创建工厂函数
set2 = set((1,2,3,4,5,6))
print(set2)
set3 = set((1,2,3,0,14,5,3,2,1))
###Python的方法的数据是无序的，不能保证原来的数据的顺序得到保留
print(list(set3))
print(1 in set3)#取值
set3.add(8)
print(set3)
set3.remove(8)
print(set3)
###不可变的set 没有添加方法
set4 = frozenset([1,2,3,4,5])

## 打开文件

file = open('//Users//yangyunfeng//Documents//AI//test//read.txt','r+t')
print(type(file))
print(file.read(5))#读取方法
print(file.tell())#读取当前位置
file.seek(0,0)#重新回到文件开头位置
print(file.readline())#读取一行数据
for each_line in file:#读取每行数据，然后打印出来
    print(each_line)
file.seek(0,0)
file.write("我是AI 工程师")
file.close();#关闭文件

def save_file(boy,girl,count):
    boy_file_name = '//Users//yangyunfeng//Documents//AI//test//boy_' + str(count) + '.txt'
    girl_file_name = '//Users//yangyunfeng//Documents//AI//test//girl_' + str(count) + '.txt'

    boy_file = open(boy_file_name, 'w')
    girl_file = open(girl_file_name, 'w')
    boy_file.writelines(boy)
    girl_file.writelines(girl)
    boy_file.close()
    girl_file.close()


def split_file(file_name):
    testFile = open(file_name,'r')
    boy = []
    girl = []
    count = 1
    for each_line in testFile:
        if each_line[:6] != '======':
            (role,linespoce) = each_line.split('：',1)
            if role == '小甲鱼':
                boy.append(linespoce)
            if role == '客服':
                girl.append(linespoce)
        else:
            save_file(boy,girl,count)
            count += 1
            boy = []
            girl = []
    save_file(boy,girl,count)
    testFile.close()

split_file('//Users//yangyunfeng//Documents//AI//test//test.txt')


# 模块 包含定义文件的打包
import random,os,time
scrite = random.randint(0,100)
print(scrite)
print(os.name,os.curdir,os.listdir(os.curdir),os.getcwd())
print(os.path.getctime('//Users//yangyunfeng//Documents//AI//test//test.txt'))
print(time.gmtime(os.path.getctime('//Users//yangyunfeng//Documents//AI//test//test.txt')))

