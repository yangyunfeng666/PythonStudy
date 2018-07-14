def cfs(cel):
    return  cel * 1.8 + 32
def sfc(hcs):
    return  (hcs - 32)/ 1.8

def test():
    print("测试，0摄氏度转华氏度 %.2f",cfs(0))
    print("测试，0华氏度转摄氏度 %.2f", sfc(0))

if __name__ == "__main__":#如果是主程序，那么执行
    test()