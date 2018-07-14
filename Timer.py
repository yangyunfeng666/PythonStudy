import  time
class MyClassTime:

    def __add__(self, other):
        result = []
        propmel = '总共运行了：'
        for index in range(6):
            result.append(self.lasted[index]+other.lasted[index])
            if result[index]:
                propmel = (str(result[index])+str(self.unit[index]))
        return propmel

    def __init__(self):
        self.unit =['年','月','日','小时','分钟','秒']
        self.propmel =  '总共的时间'
        self.begin = 0
        self.end = 0

    def __str__(self):#打印自己
        return self.propmel

    # 开始计时
    def start(self):
        self.propmel ='请调用stop 关闭'
        self.begin = time.localtime()
        print("开始计时")
    # stop
    def stop(self):
        if not self.begin:
            print("请先调用start开始计时")
        else:
            self.end = time.localtime()
            self._calc()
    # 内部方法
    def _calc(self):
        self.lasted = []
        for index in range(6):
            self.lasted.append(self.end[index]-self.begin[index])
            if self.lasted[index]:
                self.propmel += (str(self.lasted[index])+str(self.unit[index]))
        print(self.propmel)
        self.begin = 0
        self.end = 0

t1 = MyClassTime()
print(t1)
t1.start()
input("dsdsd")
t1.stop()
print(t1)

