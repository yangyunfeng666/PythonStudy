import pickle

pickle_list = ['dsadas',1212,['dsd','小金鱼']]

pickle_file = open('//Users//yangyunfeng//Documents//AI//test//pickle_file.pkl','wb')

pickle.dump(obj=pickle_list, file=pickle_file)

pickle_file.close()

pickle_file_r = open('//Users//yangyunfeng//Documents//AI//test//pickle_file.pkl','rb')
#读取数据
vaule = pickle.load(pickle_file_r)

pickle_file_r.close()
print(vaule)




def funX(x):
    print("x=%d" % x)
    def funZ(z):
        return x+z;
    def funY(y,m):
        print("y =%d " % y +"m =%d" % m)
        return funZ
    return funY
print(funX(1)(2,4)(3))