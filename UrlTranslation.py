import urllib.request
import urllib.parse
import  time as t
import timeit as ti
import  hashlib
timezone =int(round(t.time()*1000))
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
data = {}
header = {}
header['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
data['i']= '我是帅哥'
data['from'] = 'AUTO'
data['to'] =  'AUTO'
print(timezone)
hl = hashlib.md5()
hl.update(str(timezone).encode(encoding='utf-8'))
sign = hl.hexdigest()
print("sign = %s" % sign)

data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] =  timezone
data['sign'] = sign
data['doctype']='json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CLICKBUTTION'
data['typoResult']= 'false'
data = urllib.parse.urlencode(data).encode("utf-8")
request = urllib.request.Request(url,data)
#追加header
request.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36')
response = urllib.request.urlopen(request)
print(request.headers)
html = response.read().decode("utf-8")
print(html)
