
try:
    int('abc')
    d = 1 + '1'#try语句出错会中断运行到错误
    file = open("xxx.txt")
    for file_line in file:
        print(file_line)
    file.close()
except OSError as result:
    print("文件出错啦,出错的原因是"+str(result))
except TypeError as reason:
    print("类型出错了")
except:#所以的错误提示
    print("出错了")
finally:#最后执行
    print("反正我都要执行")

raise ZeroDivisionError('被除数为零的异常')

