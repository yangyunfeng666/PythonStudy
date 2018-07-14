
try:
    with open("ddd.txt",'w') as file:#with 自动的关注file 并且关闭他，解压代码
        print("文件打开了")
except :
    print("出错了")
