try:
    a = int('123')

except OSError as reason:
    print("文件出错啦")
else :
    print("上面没有出错")


