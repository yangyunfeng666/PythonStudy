#容器不可变例子1

class NoChangeContain:
    def __init__(self,*args):#参数可变数量的
        self.temp = [x for x in args]
        self.count = {}.fromkeys(range(len(self.temp)),0)#定义计算器 字典类型的

    def __len__(self):
       return len(self.temp)# 取得序列的长度

    def __getitem__(self, item):
        self.count[item] += 1
        print("item",self.count[item])
        return  self.temp[item]

c1 = NoChangeContain(1,2,3,4,5)
c2 = NoChangeContain(2,3,1,4,7,32,4,1)
print(c1[1])
print(c2[1])
print(c1.count)
print(c1[1]+c2[1])
print(c2.count)
